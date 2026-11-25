# P9 grader vs his eye, 2026-11-23 → run 2026-11-25

The main Izzy session relayed the request: the maker said "do what you think is necessary". Simulation only. The
live strategy and alerts are untouched.

## What's built
- **Setup list:** 119 audited NQ setups inside the 1m history (≥ 2023-11-20), from `codex/teacher-audit.md`:
  34 playbook takes and 85 timed skips. Parser: `tools/audit/setups.py`. List with grades:
  `2026-11-23-grader-check-setups.json`.
  - Two grades corrected by hand: 7 Aug 10:16 = "A"; 11 Feb 09:29 = "nothing light bulb", below A.
  - His stated grades: A+ ×9, A ×2, A− ×5, B ×6, pattern ×5, invalid ×1, light bulb ×1. The rest are ungraded.
    For takes, "no X flag" in `journal/labels/2026-11-23-labeled-record.md` stands for A or better.
- **Audit mode** in the grader (`tools/pine/izzy_grades.pine` v4; TradingView `USER;bcaedcac7eac46e4a3a57ce171d1cf3a` v4.0):
  - It fires only within ±2 min of each audited timestamp (all 119, sorted, pointer scan) and ignores the session
    window and the daily caps.
  - It exits on the next bar, so signals don't block each other.
  - It logs side|grade|score|location|sweep|chop|gap size.
  - Inputs: `in_25` audit on, `in_26` window (min); `in_16` = 100000 and `in_17` = 1 give a 1-lot every time.

## Blocked
Deep Backtest timed out three times at 60 s: 2023-11→2026-11, then each 18-month half. Then the daily
TradingView quota ran out (10-minute cooldown, then the next day). No grader-vs-his-eye numbers yet.

## Plan when the quota resets (≤ 6 calls)
1. Run audit mode on 1m in windows of about 6 months each (2023-11→24-05, 24-05→24-11, 24-11→25-05, 25-05→25-11,
   25-11→26-05, 26-05→26-11), `include_trades` 100.
2. Match signals to setups (same side, ±2 min). Build the confusion table: his call (take A+/A, take below A, skip A+
   for context, quality skip) × engine call (fired A+/A, fired lower grade, no fire). Add his outcomes by cell.
3. Fix the coding where we disagree, his way:
   - dealing range = swept level → opposite swing;
   - gap clarity against the 10–30 candles around it; 10–20 pt sweet spot;
   - B only with an obvious draw;
   - protected high.
   Re-check agreement.
4. Only then: one A+ 1m AM rerun per half, plus the tighter P7 (equal pair within 1R; real CPI/NFP dates).

## Addendum (relayed): his loss reasons become grader fixes (codex/playbook.md "Video study, batch 2", claims 26–28)
Each fix is coded as an input, so its effect can be shown on the audited setups and on price.
1. **No BE point → skip.** No internal high/low (untaken swing) or unfilled gap between entry and target.
2. **Protected-high/low target → skip.** The target is a swing that took another swing inside an FVG (a rejection
   block).
3. **Reversal speed.** No more than ~6 candles from the sweep extreme to the inversion (claim 26).
4. **Same leg.** The gap must belong to the current V-shape leg (formed after the sweep extreme), not an older leg.
5. **Engineered target.** Equal highs/lows or a multi-touch trend line. Asia/London highs count only when paired
   with one of those.
6. **Daily stops.** One trade per session (a BE doesn't count), and stop after 2 losses (claim 28).
7. **Window** 09:30–11:00 (his 5 rules).

Order: first measure the v3 grader against his calls (step 1). Then add fixes 1–7 one at a time. Report each fix's
change in agreement with his calls and its PF per half (A+ 1m AM).

---

## Results (run 2026-11-25, quota reset)
Grader v6 (`tools/pine/izzy_grades.pine`; TradingView v6.0).
- Audit mode ran on 1m in seven 3–6-month windows around the audited dates.
- 37 engine fires. Matching and scoring: `tools/audit/grader_check.py`. Full output:
  `2026-11-23-grader-check-audit.txt`.
- Bug found and fixed: Pine evaluates both sides of `and`, so the timestamp pointer read past the end of the array.
  That is why the first runs failed.

### 1. Does the engine even see his setups?
**Mostly not.** It fired on the same side within ±3 min on **32 of 119** audited setups, and on **6 of his 24 A-level
takes**.
- Coverage by his timeframe: 1m 13/35 · 30s 9/38 · 2m 4/13 · 3m 1/10 · 5m 2/6 · 15s 0/7.
- His entries are mostly on 30s/2m/3m candles, which a 1m engine can't reproduce. TradingView can't backtest 30s,
  2m or 3m.
- A clear coding gap: his "sweep" is often an **internal** low/high, while mine is only PDH/PDL, overnight or London.
  Example: 2 Oct 09:42, "sweep of sellside into 50% discount". My engine saw no sweep there and put it at 83% of the
  session range.

### 2. Where it fires (32 setups): his call vs mine
| | engine A+/A | engine lower grade |
|---|---|---|
| his A-level (take ≥ A, or an A+/A he skipped for context) — 12 | **5** | 7 |
| his below-A (take < A, or a quality skip) — 20 | **7** | 13 |

Agreement is 18/32 (56%), barely better than chance. On the A+ setups he skipped only for context (bias, done for the
day), the engine also said A+ in 4 of 6.

### 3. His loss reasons as grader fixes (effect on the same 32 setups)
| fix | his A kept | his below-A wrongly passed | read |
|---|---|---|---|
| v3 grader | 5/12 | 7/20 | — |
| 1 dealing range = swept extreme → opposite swing | 3/12 | 7/20 | worse (my "opposite swing" coding ~) |
| 2 BE point before target | 5/12 | 7/20 | no effect: as coded, almost every setup has one |
| 3 no protected target | 4/12 | 6/20 | small |
| 4 reversal ≤ 6 candles | 3/12 | 1/20 | **sharp**: fewer A's but almost no false ones |
| 5 same leg | 4/12 | 3/20 | helps |
| 6 engineered target (equal highs/lows) | 2/12 | 1/20 | sharp but drops most of his A's |
| 7 window 09:30–11:00 | 5/12 | 3/20 | **helps, loses none** |
| window + reversal ≤ 6 | 3/12 | **0/20** | every engine A is one of his |
| window + same leg | 4/12 | 1/20 | 4 of 5 engine A's are his |

**Read ~:** his loss reasons do make my "A" look like his. With window + reversal speed or window + same leg, nearly
every engine A is a setup he'd call A. But that is on 12 vs 20 setups, so it is direction, not proof.

### 4. Do those fixes add an edge on price? (A+ 1m AM, the out-of-sample half May 2025 → Nov 2026)
Summed over three 6-month windows; 18-month windows time out with the heavier v6 script.

| A+ 1m AM | records | PF |
|---|---|---|
| baseline (P8) | 378 | 0.75 |
| + reversal ≤ 6 candles | 284 | **0.76** |
| + same leg | 259 | **0.83** |

Neither turns the second half positive, so neither passes "holds in both halves". The first half wasn't run (quota).

## Verdict ~
- The engine and his eye agree only where the engine can see what he sees, and that is a third of his setups.
- Coding his loss reasons makes my A's look like his A's (precision up), but on price the A+ set still loses in
  2025–26 (0.76–0.83).
- Two possibilities remain:
  - What he selects is mostly on sub-minute and 2–3-minute candles plus internal sweeps, which this setup can't test.
  - His edge is in the day filter (first trade, unflagged day), not the setup grade.

## Next (proposed)
1. Internal-liquidity sweeps: an untaken swing low/high from the last 1–2 hours counts as the sweep, then re-audit.
   This is the biggest coding gap found.
2. 5m and 15m context on his setups (TradingView-testable), instead of trying to copy 30s entries.
3. Forward-log his next streams with the grader live (v0.5 alerts already carry feel data) instead of more history
   mining.

---

## Addendum 2 (relayed, 2026-11-25): his location and the Judas swing (codex/playbook.md "Video study, batch 3")
Grader v7 (TradingView v7.0). MNQ 5m; costs as before; $600 risk, ≤ 20 micros. 5m was used because a whole half runs
in one call (quota).

**Location = 0.5 of the latest impulse leg** (`Dealing range = "Impulse leg (his 0.5)"`).
- The leg runs between the last swing high and the last swing low (pivot strength 3), extended as new extremes print
  (~ my reading of "the latest obvious leg").
- Longs below 0.4 count as discount, as before.

| A+ 5m AM | 2019–22 | 2023–26 |
|---|---|---|
| session range (P8) | 0.93 (190 rec, ~1.0/wk) | 0.81 (247, ~1.2/wk) |
| **impulse-leg 0.5** | **0.85** (74, ~0.4/wk) | **1.15** (109, ~0.5/wk) |

**Judas-only** (`fxJudas`), my coding ~:
- Entry 09:30–10:00 (the 10:00 bar included), one per day, any grade.
- The 09:30 draw = the nearer untaken prior-day extreme. Longs need the draw above; shorts below.
- A false move between 09:30 and 10:00 must first take a marked pool against the draw: PDH/PDL, the pre-market
  (18:00–09:30) high/low, the London high/low, a data-candle wick, or the 09:30 candle's high/low.
- Then the usual inversion entry and management.

| Judas-only 5m | trades/wk | PF 2019–22 | PF 2023–26 |
|---|---|---|---|
| all | 1.2 / 1.1 | **0.71** (216 rec) | **1.13** (229 rec) |
| longs | | 0.62 | 1.39 |
| shorts | | 0.78 | 0.74 |

**Read ~:**
- Both of his own definitions help in 2023–26 but lose in 2019–22, so neither holds in both halves.
- The 2023–26 gain comes from longs (Judas longs 1.39), which matches the bull market of those years. That is a
  warning sign, not an edge.
- Frequency: Judas setups come about once a week on 5m, against his "every stat… 9:30–10".
- Not tested (quota): 1m Judas, and a Judas + impulse-location combination. The draw/bias definition is the weakest
  part of the coding. His bias comes from higher-timeframe FVG inversions, which I haven't coded.
