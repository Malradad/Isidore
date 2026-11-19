# Context — what decides whether an inversion is a trade

The inversion (a candle closing through a gap) is only the trigger. Mechanically it has no edge
(23-month backtest, 1,264 trades, PF 0.91). The Teacher passes on most inversions; what he checks
before taking one is **context**. This file breaks context into questions Izzy can answer at ARMED.
Sources: teacher-audit.md (streams), playbook.md (videos). `~` = Izzy's reading.

## The seven context questions (asked before every trade)
| # | Question | His words / evidence | How Izzy can check it |
|---|---|---|---|
| 1 | **Where is price coming from?** Is this a reaction off a higher-timeframe level (HTF gap, BPR, OB, 50% of the move)? | "What's to the left?"; "delivery out of the fair value gap"; "tap into the 50%" | Mark HTF gaps/BPRs/OBs (15m–4h) before the session; is the sweep low inside one? |
| 2 | **Where is price going?** Is there clear liquidity to target — equal highs/lows, trend-line stops, data highs/lows, the last low-resistance high? | "Target first"; "fuel"; "LRLR"; "data highs" | List untaken engineered levels above/below; is one within reach? |
| 3 | **Is the liquidity one-sided?** One side already swept, the other still there. | "Holy grail"; fuel on both sides = sit out | Has the opposite side been taken this session? |
| 4 | **Is the location right?** Longs in discount, shorts in premium, near the sweep, not after the move ran. | "Way too high in premium… I never long up here" | Entry in the lower (long) / upper (short) half of the sweep→target range |
| 5 | **Is the market trading or chopping?** Clean displacement vs overlapping candles. | "You're trading in chop"; "momentum candle trading out of chop" | Range compression / candle overlap before the inversion |
| 6 | **Is the risk worth it?** RR ≥ ~1, and a breakeven point (internal liquidity) exists. | "RR is kind of trash"; "no built-up internal liquidity… no break even point"; "negative R" | Target distance ÷ stop distance; an untaken internal high/low between entry and target |
| 7 | **Is it the right time and day?** Judas swing off 09:30, the first move after CPI/NFP, first setup of the day, not already done. | "One false move"; "done for the day… following my rules"; data highs after news | Time window; news calendar; trades taken today |

## Grades (his own)
- **Live / A–A+:** 1–7 mostly yes, momentum candle, clean target.
- **Eval-only / B:** valid inversion but chop, poor location or thin liquidity.
- **No trade:** no close yet, negative RR, already traded, or fuel on both sides.

## How this gets learned
1. **Label:** every TAKE and SKIP in his streams gets answers to 1–7 (from his words + key frames).
2. **Compare:** which questions separate his takes from his skips, and his winners from losers (price-checked).
3. **Code what's codeable** (2, 4, 5, 6, 7 are mostly measurable; 1 and 3 need HTF level marking) and backtest.
4. **Judge at ARMED:** Izzy answers 1–7 for every live alert, writes TAKE/SKIP + reason; the study shows
   whether the judged trades beat the raw ones.
