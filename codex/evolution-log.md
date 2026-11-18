# Evolution log

_Session entries: date · what was learned · decision · maker response · performance · lesson._

## 2026-11-18 · First web search on the Teacher
- **Learned:** the Teacher is Dodgy (Ryan, @DodgysDD). ICT-school NQ day trader.
  Core setup: iFVG, a fair value gap that fails on a candle close and flips roles;
  filtered by HTF bias and killzones; targets internal liquidity. Wrote
  portrait, playbook, reasoning, markets, risk, claims.
- **Decision:** treat iFVG as a mechanical hypothesis to backtest on NQ, not as truth.
  Treat his win-rate marketing as untested claims.
- **Doubts:** reports of losses explained away as not live; earnings come mostly
  from teaching; risk rules almost unknown; official rulebook not found.
- **Gaps:** stop placement, sizing, entry timeframe, exact killzone times,
  his "internal liquidity rule". Several sources (whop.com, trustpilot.com,
  threadreaderapp.com) were blocked by the session network.
- **Maker response:** pending.

## 2026-11-18 · Maker teaches the stop
- **Learned (✓ maker):** the stop is a candle close back through the inverted gap.
  A green candle inverts a red (bearish) gap → stop is a red candle closing back
  below it; the reverse for shorts. Wicks don't count.
- **Lesson:** the setup is symmetrical and close-based end to end. The gap is
  the whole trade: entry, thesis, and exit.
- **Isidore's concern:** close-based stops make loss size variable. Backtest must
  measure the tail of losses and test a backup hard stop.
- **Still open:** which timeframe's close; whether he keeps a hard stop; sizing.

## 2026-11-18 · First three videos (newest first)
- **Studied:** "The Most Accurate IFVG Indicator" (2026-10-26), "The Wrong Way to
  Trade IFVG's" (2026-06-05), "Watch This if You Think You Know How Liquidity Works" (2026-05-28).
- **Learned:** the A+ iFVG: HTF level → one clean sweep → V-shape → inversion close →
  strong volume → target engineered liquidity, in his direction. Repeated sweeps and
  random targets are his named failure modes. Oct 2026 model adds order flow.
- **Conflict found:** the maker's stop (close back through the gap) is one of three
  stops he uses. He also uses swing stops and stops under strong candles.
- **Decision:** default to the maker's close stop; ask the maker which stop when.
- **Maker response:** pending. Agreed earlier to study newest first.
- **Next:** frames from his charts to see the A+ setup; then backtest claims 4 and 5.

## 2026-11-18 · Maker confirms the three stops
- **Decision:** proposed close stop by default, swing stop on weak volume, candle
  stop on strong volume.
- **Maker response:** confirmed ("what he says is also true").
- **Lesson:** stop placement follows the strength of the inversion. Backtest all three
  and compare, and test the volume rule that picks between them.

## 2026-11-18 · Maker teaches the gap timeframes
- **Learned (✓ maker):** he looks for gaps on 30 s, 1 m, 2 m, 3 m and 5 m.
- **Open:** how he chooses between them for a given trade, and whether the stop
  close is read on the same timeframe as the entry.
- **Backtest implication:** run the setup on all five timeframes and compare.

## 2026-11-18 · Maker trades MNQ
- **Learned (✓ maker):** the maker trades MNQ most of the time; NQ is too large for now. Be flexible.
- **Decision:** study and backtest on NQ charts (identical price, longer history);
  size, paper trade and trade in MNQ ($2/point). NQ only when the maker raises the allocation.

## 2026-11-18 · Maker's sizing
- **Learned (✓ maker):** 1–3 MNQ per trade, $200–$250 risk, depending on setup and risk.
- **Implication:** stop distance sets the contract count: ~33–42 pts → 3 MNQ,
  ~50–62 → 2, ~100–125 → 1. Fixed-dollar risk, flexible size.
- **Decision:** these are Isidore's starting limits.
- **Open:** account size, daily loss limit, max trades per day.

## 2026-11-18 · Paper trading approved
- **Maker response:** "try one order now" — approval to paper trade in TradingView ("Isidore", $50K).
- **First order:** a mechanics test (03:00 NY, outside killzones), not a strategy trade.
