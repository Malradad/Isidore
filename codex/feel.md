# Feel — how a candle prints, made measurable

"Hindsight" (his word) = the reaction that has **already printed** before entry, plus **how** the entry candle
forms live. A finished OHLC bar hides the second part. This file turns his live "feel" into features that are
recorded on every setup, learned from outcomes, and scored automatically (muscle memory).

## What he reads (his words → feature)
| His words | Feature | Measured how |
|---|---|---|
| "I like taking trades off speed"; "a slow open I don't trade" | **cross speed** | seconds from candle open until price first closes beyond the gap edge (live: tick time; history: lower-TF bars) |
| "light bulb candle", "death/birth candle", "massive momentum" | **decisiveness** | body % of range; close location in range (near the extreme = strong) |
| "it wicked through and came back", "can't jump the gun", "no close yet" | **flips** | times price crossed the gap edge and back before the close |
| "huge volume… then an even bigger reversal" | **volume burst** | candle volume ÷ 20-bar average; share of it traded before the cross |
| "V-shape", "reaction in hindsight… orders got filled" | **reaction sharpness** | bars and points from the sweep extreme to the inversion close |
| "trading in chop", "snakey pattern" | **chop before** | overlap of the last N candles (range compression) before the setup |
| "push-through ratio" | **candles to invert** | bars from gap creation to the inverting close (≤ 7) |

## The two kinds of hindsight
- **Legitimate:** anything already closed before the entry (sweep, reaction, gap, chop). Use it.
- **Bias:** knowing what happened after. Never use it when judging context. Labels of his streams are done
  **blind**: frames up to the entry only; outcome scored separately.

## How it becomes muscle memory
1. **Record:** strategy v0.5 tracks every forming candle tick by tick (`varip`) and puts cross speed, flips,
   close location, body %, volume burst into every ARMED/CONFIRMED alert. Bot logs every alert, traded or not.
   History: Izzy rebuilds the same features from 15s/30s bars for backtests.
2. **Label:** each setup gets its outcome (price) and, where available, his decision (take/skip from streams).
3. **Learn:** compare winners vs losers and his takes vs skips on these features; find the thresholds that matter.
4. **Score:** encode the result as a "feel score" in the strategy. Every ARMED alert carries it; Izzy's TAKE/SKIP
   uses it alongside the seven context questions (`codex/context.md`).
5. **Keep learning:** every new setup adds a row; the thresholds are re-checked monthly, out of sample.

## What the data says so far (P6, 2026-11-22, `journal/backtests/2026-11-22-feel.md`)
- ~ **Cross timing holds; read it as speed into the close.** On his mechanical model (P1, MNQ 5m, 1m data
  2023-11→2026-11), a first 1m close beyond the gap at minute 4–5 of the candle beat minute 1–3 in both periods:
  PF 2.19 vs 0.67, then 1.05 vs 0.65. A candle that crossed in minute 1 and then sat has lost its push.
- ~ **Flips hurt** in both periods (0.63, 0.46), but only on 23 trades.
- ✗ **Body %, chop before, volume burst, and reaction bars/points** flip sign or fail between halves. Don't
  score them yet.
- ~ **Feel score v0** (late cross + no flip + volume ≥ 1.03): score 3 has PF 2.96, then 1.00; score < 3 has
  0.63, then 0.69. It ranks trades but does not create an edge on its own.
- Next: the same tags on v0.4 max-1/day, then check against Bot's live `cross_s` log. For live 5m alerts,
  "late" means cross_s ≥ 180.
