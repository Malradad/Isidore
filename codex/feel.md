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
