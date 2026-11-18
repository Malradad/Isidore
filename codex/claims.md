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

**Running record:** 10 claims · 5 judged (1 supported, 1 partly, 3 not) · hit rate 1–1.5 / 5

All five judged on Izzy's mechanical v0.4 model (1m MNQ, Jan 2025 – Nov 2026, Deep Backtesting). A ✗ judges that coding of the rule, not every reading of it.
