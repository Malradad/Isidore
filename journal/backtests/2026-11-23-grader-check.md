# P9 grader vs his eye, 2026-11-23 (in progress: blocked by the TradingView quota)

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
