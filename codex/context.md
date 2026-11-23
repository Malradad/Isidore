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

## Q1/Q7 detail: how he sets the bias (youtube/20250630 gpn8BvK-G4s "Foolproof Bias")
- **Bias = his own entry model, run on the 1h (or 4h):** a sweep of a level, then a candle closing through an
  hourly FVG (an hourly inversion) → bullish (or bearish) for the rest of that session, only longs (shorts),
  "until the next hourly high (low)". "Time is fractal."
- **No hourly inversion → no bias** ("I can't be bullish unless it breaks") → neutral or the other way.
- **Chop → neutral.** "When I get the bias wrong, we're usually chopping." Inside consolidation, even with an
  hourly inversion, stay neutral and open to both sides.
- **"Marry" the bias (and size up) only when it's obvious:** big sweep, in discount, giant momentum back —
  "if I back up 10 feet from my screen and can still see it." Most days have no clean hourly inversion.
- **Skip:** an inversion that stopped just short of a low → expect that low to be retaken first.
- His claim: right ~90% with context, ~70% "pattern trading". Untested (claim in claims.md).
- My EMA proxy for bias failed in the backtest; this is the real definition and is mechanical → testable.

## Q4 detail: what makes it A+ (youtube/20250608 -xLZ2ekyja4 "Five A+ iFVG Setups")
HTF FVG to the left (or same-TF) · sweep of a low **into** it · inversion out with momentum · **in discount**
(below 50% of the range, or of the leg) for longs / premium for shorts · at or near the low of day · a single
FVG (adjacent ones can be combined) · the **lowest** entry is A+, a second higher entry is only A.
Stop: close back through the FVG, or hard under the order block. Scale half at the 50% level / 1R.

## Q2 detail: his liquidity-target tier list (streams/2025-08-10 rKxoMCjqfgQ @ 00:14:40)
| Tier | Target |
|---|---|
| **S** | perfect equal highs/lows > 3 candles apart; data high/low with a giant wick |
| **A** | perfect equal highs/lows 1–3 candles apart; trend-line liquidity with 5+ perfect touches |
| **B** | high/low inside an old FVG; trend line with 2–3 touches; NWOG/NDOG; relative equal highs/lows; previous session highs/lows (day, Asia, London) |
| **C** | unbalanced inefficiencies; volume imbalances |
| **F** | "protected" highs/lows (took out another inside an FVG); order blocks |
Tiers combine: two B's (e.g. a London high inside an FVG) → an A. Prefer S/A targets; C/F alone are weak draws.
"The IFVGs are the entry model, but the delivery and reactions from previous PD arrays… that's what makes you money."

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
