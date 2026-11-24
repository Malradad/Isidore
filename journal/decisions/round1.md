# Round 1 — blind chart-only read vs his calls (2026-11-24)

Labeler: fresh Izzy session that never saw outcomes (`labels-blind.csv`, `labels-blind-notes.md`). Inputs: frames at or
before each decision only (132 with Audrey's strips, 79 single frames, 10 unusable). 31 rows flagged "contaminated"
by the labeler (P&L overlays, later frames seen) — none of them among his 48 playbook takes.
Scored with `tools/decisions/score.py` and a join to `tools/labels/takes.py`.

## Result
- Izzy called **36 TAKE / 169 SKIP / 10 ?**. It agreed with his call on 52% of decisions. He took 103, so Izzy is far
  stricter: it skipped 77 of his takes.
- **On his 48 audited playbook takes (47 matched):**

| blind Izzy | n | his result W/BE/L | avg R |
|---|---|---|---|
| TAKE | 13 | 7 / 3 / 3 | +0.46 |
| SKIP | 32 | 17 / 6 / 9 | +0.23 |

  Some separation, not much. Confidence was low throughout (2–3 of 5 on 82% of rows).
- **His clean winners** (first trade of the day on an unflagged day, A grade; 7 trades): Izzy took 2 (10-02, 03-06),
  skipped 4, and had 1 unusable. **His 2+-flag trades** (19): Izzy took 3 (1L, 1BE, 1W) and skipped 15 — it avoided
  most of his rule-breaking trades from the chart alone.
- **Izzy's three TAKE-losses** (07-14 09:45, 10-15 09:44, 09-05 10:11) were on a day he'd called a no-trade day, an
  indicator showcase, and a teaching example. Those flags live in his words, not on the chart.

## Lessons
1. **News-day pre-open is in his playbook.** Izzy skipped 09-11 08:38 and 06-05 08:38 as "pre-open". Both won. After a
   CPI/NFP release, 08:30–09:30 is a killzone for him, not "pre-open" (codex/context.md Q7).
2. **Day-level context isn't on the chart.** No-trade days, bias, done-for-the-day, audience trades are in what he
   *said before* the trade. A chart-only read can't see them, which caps how well it can select.
3. **"Second attempt" isn't always a skip.** 11-02 09:39 was a second sweep of the same lows and won; his rule is "up to 3
   attempts if ≥ 2R" (teacher-audit, 15 Oct 2025).
4. **Izzy is too strict for ≥ 3 trades/week.** 36 TAKE across 37 stream days ≈ 1 per stream day.

## Round 2 (next)
A new fresh labeler gets the frames **plus a context pack** per decision (`journal/decisions/context/<id>.txt`): the day
type and his own words from the stream start to 30 s before the decision (his plan + the last 15 minutes). That's what
he knew; nothing after. It also gets lessons 1 and 3. Then the same scoring.
