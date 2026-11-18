#!/usr/bin/env python3
"""Isidore iFVG backtester.

Step 1: a bar-by-bar port of tools/pine/isidore_ifvg.pine (v0.4, default inputs),
so its trades can be checked against TradingView's Strategy Tester.
Step 2: switches for what Pine does badly (see Config: fuel_target, skip_two_sided,
max_trades, window, mom_filter, sweep_rank).

Bars: CSV with t (unix sec UTC, bar open), o, h, l, c, v. 2m/3m are built from 1m.

Pine semantics mirrored
- Script runs at each bar close. strategy.entry -> market fill at the NEXT bar's open
  (+1 tick slippage). strategy.exit stop/limit are live from that fill bar on.
- strategy.close (close-through-gap, EOD flat) -> next bar's open (+1 tick slippage).
- Stop and limit in one bar: TradingView's broker emulator assumes the path
  open -> nearest extreme -> other extreme -> close.
- Stop orders fill at stop (or the open if the bar gaps past it) +1 tick slippage;
  limits fill at the limit price (or the open if it gaps through) with no slippage.
- Commission $0.62 per contract per side. MNQ: $2/point, tick 0.25.
- Trading day = CME session (starts 18:00 New York), like time("D") on futures.
"""
from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass, field, asdict, replace
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")
TICK = 0.25
PV = 2.0  # MNQ $ per point


# ───────── data ─────────
@dataclass
class Bar:
    t: int
    o: float
    h: float
    l: float
    c: float
    v: float


def load_csv(path: str) -> list[Bar]:
    with open(path) as f:
        r = csv.DictReader(f)
        return [Bar(int(float(x["t"])), float(x["o"]), float(x["h"]), float(x["l"]),
                    float(x["c"]), float(x["v"])) for x in r]


def resample(bars: list[Bar], minutes: int) -> list[Bar]:
    """Aggregate 1m bars into N-minute bars aligned to clock minutes (18:00 NY is aligned for 2/3/5)."""
    out: list[Bar] = []
    step = minutes * 60
    for b in bars:
        k = b.t - (b.t % step)
        if out and out[-1].t == k:
            x = out[-1]
            x.h = max(x.h, b.h); x.l = min(x.l, b.l); x.c = b.c; x.v += b.v
        else:
            out.append(Bar(k, b.o, b.h, b.l, b.c, b.v))
    return out


def ny(t: int) -> datetime:
    return datetime.fromtimestamp(t, timezone.utc).astimezone(NY)


def trade_day(t: int) -> str:
    """CME trading date: bars from 18:00 NY belong to the next day."""
    return (ny(t) + timedelta(hours=6)).strftime("%Y-%m-%d")


def in_window(t: int, start: str, end: str) -> bool:
    """Bar open time within [start, end) New York, 'HHMM'."""
    d = ny(t)
    m = d.hour * 60 + d.minute
    s = int(start[:2]) * 60 + int(start[2:])
    e = int(end[:2]) * 60 + int(end[2:])
    return s <= m < e


# ───────── config ─────────
@dataclass
class Config:
    # v0.4 inputs (defaults = Pine defaults)
    min_gap_ticks: int = 8
    max_gap_age: int = 40
    max_push: int = 7
    require_sweep: bool = True
    piv_len: int = 3
    sweep_window: int = 15
    max_sweeps: int = 1
    window: tuple[str, str] | None = None      # None = all hours (v0.4 default); e.g. ("0930","1100")
    flat_window: tuple[str, str] = ("1655", "1700")
    bias: str = "Both"
    stop_mode: str = "Auto (volume)"
    strong_mult: float = 1.5
    weak_mult: float = 1.0
    vol_len: int = 20
    buf_ticks: int = 2
    tgt_mode: str = "Liquidity, fallback R"
    rr: float = 1.0
    min_rr: float = 1.0
    eq_tol_ticks: int = 8
    be_at_r: float = 0.0
    risk_usd: float = 225.0
    max_qty: int = 3
    mom_min: float = 0.6
    max_trades: int = 3
    max_losses: int = 2
    max_day_loss: float = 500.0
    min_score: int = 1
    commission: float = 0.62
    slip_ticks: int = 1
    # ── v0.5 candidates (off = identical to Pine v0.4) ──
    min_sweeps: int = 1            # 3 = only 3rd+ sweeps in the window (claim 4)
    eng_mode: str = "Any"          # "Engineered only" | "Single only" (claim 5)
    mom_mode: str = "Any"          # "Momentum only" | "Non-momentum only" (claim 10)
    push_filter: bool = False      # require push-through <= max_push (v0.4 only scores it)
    fuel_target: bool = False      # target = top of the fuel chain (when >= 2 levels)
    skip_two_sided: bool = False   # skip when a fuel chain (>= 2) also sits on the opposite side
    one_false_move: bool = False   # only the first signal of the day may trade


# ───────── engine ─────────
@dataclass
class Signal:
    i: int
    side: int          # 1 long, -1 short
    entry_ref: float   # signal close
    sl: float
    tp: float
    qty: int
    dist: float
    mode: str
    gap: float         # close-through level
    score: int
    sweep_count: int
    engineered: bool
    momentum: bool
    push: int | None
    strong_vol: bool
    hour: int
    two_sided: bool


@dataclass
class Trade:
    side: int
    entry_t: int
    entry_px: float
    exit_t: int = 0
    exit_px: float = 0.0
    qty: int = 0
    sl: float = 0.0
    tp: float = 0.0
    reason: str = ""
    pnl: float = 0.0
    r: float = 0.0
    sig: Signal | None = None


def pivots(bars, n):
    """Pine ta.pivothigh/low(n, n): value confirmed n bars later. Ties are allowed on the
    left side, not on the right (verified against TradingView 2026-11-18)."""
    ph = [None] * len(bars); pl = [None] * len(bars)
    for i in range(2 * n, len(bars)):
        c = i - n
        hc, lc = bars[c].h, bars[c].l
        if all(bars[c - k].h <= hc for k in range(1, n + 1)) and all(bars[c + k].h < hc for k in range(1, n + 1)):
            ph[i] = hc
        if all(bars[c - k].l >= lc for k in range(1, n + 1)) and all(bars[c + k].l > lc for k in range(1, n + 1)):
            pl[i] = lc
    return ph, pl


def fuel_chain(levels: list[float], px: float, side: int) -> tuple[float | None, int]:
    """Fuel (Dodgy): untaken swing points stacked away from price. Walk the untaken pivots
    from newest to oldest; each must be further from price than the last (a staircase of
    lower highs above price for longs, higher lows below for shorts). Returns (top of the
    chain, chain length). Same as f_fuel in tools/pine/isidore_ifvg_lab.pine."""
    last = None; n = 0
    for v in reversed(levels):
        if (v > px) if side == 1 else (v < px):
            if last is None or ((v > last) if side == 1 else (v < last)):
                last = v; n += 1
            else:
                break
    return last, n


def run(bars: list[Bar], cfg: Config, collect_signals: bool = False):
    n = len(bars)
    tick = TICK
    ph, pl = pivots(bars, cfg.piv_len)
    phs: list[float] = []; pls: list[float] = []
    gaps: list[list] = []  # [top, bot, dir, bar]
    sweep_low_bar = sweep_high_bar = None
    sweep_low_px = sweep_high_px = None
    sweep_low_cnt = sweep_high_cnt = 0
    vols: list[float] = []

    trades: list[Trade] = []
    signals: list[Signal] = []
    pos: Trade | None = None
    pending_entry: Signal | None = None
    pending_close: str | None = None
    trade_gap = None; use_close_x = False; trade_risk = None
    cur_day = None; day_trades = day_losses = 0; day_start_net = 0.0; net = 0.0
    day_first_sig_used = False
    seen = 0

    def slip(px, side_mult):
        return px + side_mult * cfg.slip_ticks * tick

    def close_pos(i, px, reason):
        nonlocal pos, net
        pos.exit_t = bars[i].t; pos.exit_px = px; pos.reason = reason
        pts = (px - pos.entry_px) * pos.side
        pos.pnl = pts * PV * pos.qty - 2 * cfg.commission * pos.qty
        pos.r = pts / pos.sig.dist if pos.sig.dist else 0.0
        net += pos.pnl
        trades.append(pos); pos = None

    for i in range(n):
        b = bars[i]
        day = trade_day(b.t)
        # ── broker: orders placed at the previous close fill at this open ──
        if pending_close and pos:
            close_pos(i, slip(b.o, -pos.side), pending_close)
        pending_close = None
        if pending_entry and pos is None:
            s = pending_entry
            pos = Trade(s.side, b.t, slip(b.o, s.side), qty=s.qty, sl=s.sl, tp=s.tp, sig=s)
        pending_entry = None
        # ── broker: stop / limit intrabar ──
        if pos:
            for _ in range(1):
                side = pos.side
                stop, lim = pos.sl, pos.tp
                # gap through at the open
                if (side == 1 and b.o <= stop) or (side == -1 and b.o >= stop):
                    close_pos(i, slip(b.o, -side), "stop"); break
                if (side == 1 and b.o >= lim) or (side == -1 and b.o <= lim):
                    close_pos(i, b.o, "target"); break
                hit_stop = (b.l <= stop) if side == 1 else (b.h >= stop)
                hit_lim = (b.h >= lim) if side == 1 else (b.l <= lim)
                if hit_stop and hit_lim:
                    high_first = (b.h - b.o) <= (b.o - b.l)  # open nearer the high -> high first
                    lim_first = high_first if side == 1 else not high_first
                    if lim_first:
                        close_pos(i, lim, "target")
                    else:
                        close_pos(i, slip(stop, -side), "stop")
                elif hit_stop:
                    close_pos(i, slip(stop, -side), "stop")
                elif hit_lim:
                    close_pos(i, lim, "target")

        # ── script at bar close ──
        if day != cur_day:
            cur_day = day; day_trades = 0; day_losses = 0; day_start_net = net
            day_first_sig_used = False
        # Pine: reset first, then count trades that closed on this bar
        for x in trades[seen:]:
            if x.pnl < 0:
                day_losses += 1
        seen = len(trades)

        # swings
        if ph[i] is not None:
            phs.append(ph[i]); phs[:] = phs[-40:]
        if pl[i] is not None:
            pls.append(pl[i]); pls[:] = pls[-40:]
        swept_low = any(b.l < v for v in pls)
        pls[:] = [v for v in pls if not b.l < v]
        swept_high = any(b.h > v for v in phs)
        phs[:] = [v for v in phs if not b.h > v]
        if swept_low:
            sweep_low_cnt = sweep_low_cnt + 1 if sweep_low_bar is not None and i - sweep_low_bar <= cfg.sweep_window else 1
            sweep_low_bar = i; sweep_low_px = b.l
        elif sweep_low_bar is not None and i - sweep_low_bar <= cfg.sweep_window and b.l < sweep_low_px:
            sweep_low_px = b.l
        if swept_high:
            sweep_high_cnt = sweep_high_cnt + 1 if sweep_high_bar is not None and i - sweep_high_bar <= cfg.sweep_window else 1
            sweep_high_bar = i; sweep_high_px = b.h
        elif sweep_high_bar is not None and i - sweep_high_bar <= cfg.sweep_window and b.h > sweep_high_px:
            sweep_high_px = b.h
        long_sweep_ok = sweep_low_bar is not None and i - sweep_low_bar <= cfg.sweep_window and cfg.min_sweeps <= sweep_low_cnt <= cfg.max_sweeps
        short_sweep_ok = sweep_high_bar is not None and i - sweep_high_bar <= cfg.sweep_window and cfg.min_sweeps <= sweep_high_cnt <= cfg.max_sweeps

        # gaps
        if i > 2:
            if b.l > bars[i - 2].h and b.l - bars[i - 2].h >= cfg.min_gap_ticks * tick:
                gaps.append([b.l, bars[i - 2].h, 1, i])
            if b.h < bars[i - 2].l and bars[i - 2].l - b.h >= cfg.min_gap_ticks * tick:
                gaps.append([bars[i - 2].l, b.h, -1, i])
        long_inv = short_inv = False
        long_gap_bot = short_gap_top = None
        long_age = short_age = None
        for g in reversed(list(gaps)):
            top, bot, d, gb = g
            if i - gb > cfg.max_gap_age:
                gaps.remove(g)
            elif i > gb:
                if d == -1 and b.c > top and b.c > b.o:
                    long_inv = True
                    long_gap_bot = bot if long_gap_bot is None else min(long_gap_bot, bot)
                    long_age = i - gb if long_age is None else min(long_age, i - gb)
                    gaps.remove(g)
                elif d == 1 and b.c < bot and b.c < b.o:
                    short_inv = True
                    short_gap_top = top if short_gap_top is None else max(short_gap_top, top)
                    short_age = i - gb if short_age is None else min(short_age, i - gb)
                    gaps.remove(g)

        # filters
        vols.append(b.v)
        vavg = sum(vols[-cfg.vol_len:]) / cfg.vol_len if len(vols) >= cfg.vol_len else None
        vratio = b.v / vavg if vavg else 1.0
        strong = vratio >= cfg.strong_mult
        weak = vratio < cfg.weak_mult
        rng = b.h - b.l
        momentum = rng > 0 and abs(b.c - b.o) / rng >= cfg.mom_min
        in_kz = cfg.window is None or in_window(b.t, *cfg.window)
        in_flat = in_window(b.t, *cfg.flat_window)
        mode = cfg.stop_mode if cfg.stop_mode != "Auto (volume)" else (
            "Inversion candle" if strong else "Swing" if weak else "Close back through gap")

        def qty_for(dist):
            dd = dist * PV
            return min(math.floor(cfg.risk_usd / dd), cfg.max_qty) if dd > 0 else 0

        def near_count(arr, lvl):
            return sum(1 for v in arr if abs(v - lvl) <= cfg.eq_tol_ticks * tick) if lvl is not None else 0

        sig: Signal | None = None
        # long
        l_sl = (b.l if mode == "Inversion candle" else (sweep_low_px if sweep_low_px is not None else b.l)) - cfg.buf_ticks * tick
        l_dist = b.c - l_sl
        above = [v for v in phs if v > b.c]
        l_liq = min(above) if above else None
        l_eng = near_count(phs, l_liq) >= 2
        l_fuel, l_fn = fuel_chain(phs, b.c, 1)
        _, l_opp = fuel_chain(pls, b.c, -1)
        if cfg.fuel_target and l_fn >= 2:
            l_liq = l_fuel
        l_tp = l_liq if cfg.tgt_mode.startswith("Liquidity") and l_liq is not None and (l_liq - b.c) >= cfg.min_rr * l_dist else b.c + cfg.rr * l_dist
        l_push = long_age is not None and long_age <= cfg.max_push
        l_score = long_sweep_ok + strong + l_eng + momentum + l_push
        l_qty = qty_for(l_dist)
        long_sig = long_inv and in_kz and cfg.bias != "Short only" and (long_sweep_ok or not cfg.require_sweep) and l_dist > 0 and l_qty >= 1
        # short
        s_sl = (b.h if mode == "Inversion candle" else (sweep_high_px if sweep_high_px is not None else b.h)) + cfg.buf_ticks * tick
        s_dist = s_sl - b.c
        below = [v for v in pls if v < b.c]
        s_liq = max(below) if below else None
        s_eng = near_count(pls, s_liq) >= 2
        s_fuel, s_fn = fuel_chain(pls, b.c, -1)
        _, s_opp = fuel_chain(phs, b.c, 1)
        if cfg.fuel_target and s_fn >= 2:
            s_liq = s_fuel
        s_tp = s_liq if cfg.tgt_mode.startswith("Liquidity") and s_liq is not None and (b.c - s_liq) >= cfg.min_rr * s_dist else b.c - cfg.rr * s_dist
        s_push = short_age is not None and short_age <= cfg.max_push
        s_score = short_sweep_ok + strong + s_eng + momentum + s_push
        s_qty = qty_for(s_dist)
        short_sig = short_inv and in_kz and cfg.bias != "Long only" and (short_sweep_ok or not cfg.require_sweep) and s_dist > 0 and s_qty >= 1

        hour = ny(b.t).hour
        if long_sig:
            sig = Signal(i, 1, b.c, l_sl, l_tp, l_qty, l_dist, mode, long_gap_bot, int(l_score),
                         sweep_low_cnt, l_eng, momentum, long_age, strong, hour, l_opp >= 2)
        elif short_sig:
            sig = Signal(i, -1, b.c, s_sl, s_tp, s_qty, s_dist, mode, short_gap_top, int(s_score),
                         sweep_high_cnt, s_eng, momentum, short_age, strong, hour, s_opp >= 2)
        if sig and collect_signals:
            signals.append(sig)

        # v0.5 gates
        if sig and cfg.eng_mode != "Any" and sig.engineered != (cfg.eng_mode == "Engineered only"):
            sig = None
        if sig and cfg.mom_mode != "Any" and sig.momentum != (cfg.mom_mode == "Momentum only"):
            sig = None
        if sig and cfg.push_filter and (sig.push is None or sig.push > cfg.max_push):
            sig = None
        if sig and cfg.skip_two_sided and sig.two_sided:
            sig = None
        if sig and cfg.one_false_move:
            if day_first_sig_used:
                sig = None
            else:
                day_first_sig_used = True

        can_trade = day_trades < cfg.max_trades and day_losses < cfg.max_losses and (net - day_start_net) > -cfg.max_day_loss
        if pos is None and can_trade and sig and sig.score >= cfg.min_score and i + 1 < n:
            pending_entry = sig
            trade_gap = sig.gap; use_close_x = sig.mode == "Close back through gap"; trade_risk = sig.dist
            day_trades += 1
        if pos:
            if use_close_x and trade_gap is not None and ((pos.side == 1 and b.c < trade_gap) or (pos.side == -1 and b.c > trade_gap)):
                pending_close = "close thru gap"
            if cfg.be_at_r > 0:
                if pos.side == 1 and b.h >= pos.entry_px + cfg.be_at_r * trade_risk:
                    pos.sl = pos.entry_px
                if pos.side == -1 and b.l <= pos.entry_px - cfg.be_at_r * trade_risk:
                    pos.sl = pos.entry_px
            if in_flat:
                pending_close = "EOD flat"
    if pos:  # open at the end: mark to last close (TradingView leaves it open; excluded from stats)
        pos.reason = "open"
    return trades, signals


# ───────── report ─────────
def stats(trades: list[Trade]) -> dict:
    t = [x for x in trades if x.reason != "open"]
    if not t:
        return dict(trades=0, net=0.0, win=0.0, pf=None, avg_r=None, maxdd=0.0)
    wins = [x.pnl for x in t if x.pnl > 0]; losses = [x.pnl for x in t if x.pnl <= 0]
    eq = 0.0; peak = 0.0; dd = 0.0
    for x in t:
        eq += x.pnl; peak = max(peak, eq); dd = max(dd, peak - eq)
    return dict(trades=len(t), net=round(sum(x.pnl for x in t), 2),
                win=round(len(wins) / len(t), 3),
                pf=round(sum(wins) / -sum(losses), 2) if losses and sum(losses) < 0 else None,
                avg_r=round(sum(x.r for x in t) / len(t), 2), maxdd=round(dd, 2))


def fmt_trade(x: Trade) -> str:
    return (f"{ny(x.entry_t):%m-%d %H:%M} {'L' if x.side == 1 else 'S'} {x.qty} @ {x.entry_px:.2f}"
            f" -> {ny(x.exit_t):%m-%d %H:%M} {x.exit_px:.2f} {x.reason:14s} {x.pnl:+8.2f} {x.r:+.2f}R"
            f" [{x.sig.mode[:5]} g{x.sig.score}]")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--tf", type=int, default=0, help="resample 1m CSV to N minutes")
    ap.add_argument("--from", dest="dfrom", default=None, help="NY date YYYY-MM-DD: first bar to trade (warm-up kept)")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    bars = load_csv(a.csv)
    if a.tf:
        bars = resample(bars, a.tf)
    tr, _ = run(bars, Config())
    if a.dfrom:
        tr = [x for x in tr if ny(x.entry_t).strftime("%Y-%m-%d") >= a.dfrom]
    print(stats(tr))
    if a.list:
        for x in tr:
            print(fmt_trade(x))


if __name__ == "__main__":
    main()
