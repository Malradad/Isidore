# Claims ledger

Every testable prediction, judged against real prices. Never use his recap as the result.

| # | Source | Instrument | Claim | Judged by | Due | Result | Notes |
|---|---|---|---|---|---|---|---|
| 1 | YouTube title | iFVG model | "80% winrate" | Backtest on NQ with his rules | When rules are known | — | Marketing; stop and target undefined |
| 2 | YouTube title | iFVG model | "Beats 90% of trading strategies" | Not testable as stated | — | — | Marketing |
| 3 | youtube/hd8OyKtQfx0 @ 00:00:16 | — | "I will still show every loss I take" | Compare his live streams vs. recaps | Ongoing | — | Contradicts a Trustpilot review |
| 4 | youtube/hd8OyKtQfx0 @ 00:01:47 | NQ | First sweep + iFVG works far more than 3rd+ sweep in the same range | Backtest | ✓ 2026-11-18 | ✗ Not supported | Deep 1m 2025-01→2026-11: 1st sweep PF 0.91 (1,264 tr) vs 3rd+ PF 0.93 (1,255). `journal/backtests/2026-11-18-deep.md` |
| 5 | youtube/hd8OyKtQfx0 @ 00:04:28 | NQ | iFVGs targeting engineered liquidity win more than ones targeting a single high | Backtest | ✓ 2026-11-18 | ~ Direction yes, no edge | Engineered PF 0.93 (935 tr) vs single PF 0.88 (1,256); both lose after costs |
| 6 | youtube/ETRextCcwCo @ 00:01:03 | NQ | Inversions with a delta flip are stronger | Backtest with volume data | Later | — | Needs order-flow data |
| 7 | youtube/oenzNA9OHU4 | — | iFVGs "can almost never fail if used properly" | Not testable as stated: failures are blamed on the user | — | — | Hype |
| 8 | youtube/zAZqCeckrwg | NQ | One trade a day beats several | Backtest: max 1 vs max 3 trades/day | ✓ 2026-11-18 | ✓ Supported | Max 1/day PF 1.05, +$1,107, DD $1,978 (472 tr) vs max 3 PF 0.91, −$5,863, DD $8,007. Only positive variant; thin |
| 9 | youtube/E1BIVjBwLxQ | NQ | Most good setups now come 09:30–10:00 (Judas swing) | Backtest by hour | ✓ 2026-11-18 | ✗ Not supported | 09:30–10:00 only: PF 0.92, −$1,174 (166 tr). Slightly better than all hours, still losing |
| 10 | youtube/E1BIVjBwLxQ | NQ | Momentum (big-body) inversion candles beat choppy ones | Backtest with body/wick filter | ✓ 2026-11-18 | ✗ Not supported | Body ≥ 60% of range: PF 0.90 (1,242) vs non-momentum PF 0.90 (1,209) |

| 11 | maker, 2026-11-18 | MNQ | **A (maker's exact version):** one closing moment inverts gaps on 2+ timeframes in the same direction (identical bar_close) = strong setup. **B:** same direction on 2+ TFs within 5 min | Backtest A: identical-bar_close multi-TF signals vs single-TF signals **at the same aligned close times** (controls for time of day). B: ≤5 min window vs single. PF, win %, by year | ✓ 2026-11-22 | ✗ Not supported | Deep 1m 2023-11→2026-11, daily limits off. **A:** confluence PF 0.88 (2,527 tr) vs single-TF at the same aligned closes PF 0.91 (5,818). **B (≤5 min):** PF 0.906 (3,180) vs 0.907 (7,878). No difference; both lose. `journal/backtests/2026-11-22-claim11.md` |

| 12 | streams/2026-09-04 N6eOC8wtapo @ 01:23:48 | NQ | "The data high is going to hit 90% of the time" ("93%", chlCV294CTk 01:33:08). **4 Sep 2026: missed by ~2.5 pts; 5 Jun 2026 NFP: missed again** (15m high after the news bar 30,135.50 vs 30,151.75; that day he said "data wicks get tapped 86%", f4LM3kNzquo 01:22:46) | Backtest: on CPI/NFP days, % of sessions where price trades above the 08:30 candle's high (and the relative equal highs) by 11:00 | Next quota | — | Testable; core to his news-day trades |
| 13 | streams/2026-09-04 N6eOC8wtapo @ 00:47:59 | NQ | "10 AM reversals have been so strong" — the 09:30–10:00 move tends to reverse around 10:00 | Backtest: direction 09:30→10:00 vs 10:00→10:30, % opposite, by month | Next quota | — | Testable |

| 14 | streams/2026-07-14 nE8GE9YBd8k @ 00:11:28 | NQ | News straddle "works 85–90%… failed twice out of ~30" | Count straddles in audited streams + backtest stop-entry straddles at 08:30 on CPI/NFP | Ongoing | 1 loss (12 Aug, −$10.7k paper) in 6 seen | Gambling category, never for Izzy |

| 15 | streams/2025-08-10 rKxoMCjqfgQ @ 00:14:40 | NQ | His liquidity tier list: S/A pools get hit more often than C/F | Backtest: classify pools by tier, measure % reached within the session | Next quota | — | Directly tests context Q2 |

| 16 | streams/2025-01-22 j0tG6Mj-ds4 @ 01:15:55 | NQ | "If we get over a 200-point overnight move, New York AM usually sucks" | Backtest: overnight range > 200 pts vs not → v0.4/1-per-day results 09:30–11:00 | ✓ 2026-11-22 | ✗ Not supported alone | On his own model (P1, 5m): filter alone PF 0.69 (2019–22) / 0.92 (2023–26) vs no filter 0.75 / 1.04 — worse in both. Helps only inside the full filter set. `journal/backtests/2026-11-22-plan.md` |

| 17 | streams/2023-09-04 ErsWq6j87uY @ 00:51:23 | MNQ | His mechanical model (PDH/PDL sweep → last single opposite 5m/15m FVG inversion, London/NY, 1/day) is profitable: "80% at least", "guaranteed profitable after two weeks" | Deep backtest on MNQ 5m/15m, 2019–2026, split by year | ✓ 2026-11-22 | ✗ Not supported as stated; ~ promising with all his filters | Pure model 5m: PF 0.75 (2019–22) / 1.04 (2023–26), win 23–25% (not 80%). 15m: 1.38 / 0.88. **With all his no-trade filters + 10:00 exit: PF 1.20 (36 tr) / 1.40 (58 tr)** — holds in both halves but only 94 trades; no single filter helps alone. `journal/backtests/2026-11-22-plan.md` |

| 18 | youtube/20250630 gpn8BvK-G4s | NQ | Hourly inversion after a sweep sets the session bias, right ~90% (neutral in chop) | Backtest: 1h iFVG-after-sweep → session bias; % of sessions price reaches the next 1h high/low in that direction; then as a filter on P1+filters and v0.4 1/day | Next quota | — | Real bias definition (replaces the EMA proxy) |
| 19 | codex/feel.md (his "I like taking trades off speed"; "can't jump the gun") | MNQ | Feel features of the inversion candle (cross speed, flips, decisiveness, volume, chop, reaction) separate winners from losers | P1 5m with features from 1m bars, PF by tertile in both halves | ✓ 2026-11-22 | ~ Partly | Only **cross timing** holds: a late cross (minute 4–5 of the 5m candle) has PF 2.19 / 1.05 vs an early cross 0.67 / 0.65 (2023–24 / 2025–26). Fast-at-the-open is *worse*. Flips are worse in both periods (n=23). Body %, chop, volume and reaction reverse or fail between halves. `journal/backtests/2026-11-22-feel.md` |

**Running record:** 19 claims · 9 judged (1 supported, 3 partly, 5 not) · hit rate 1–3 / 9

All five judged on Izzy's mechanical v0.4 model (1m MNQ, Jan 2025 – Nov 2026, Deep Backtesting). A ✗ judges that coding of the rule, not every reading of it.
