# Blind labels: method notes (Izzy, blind session, 2026-11-24)

`labels-blind.csv` has 215 rows, one per id in `inputs.csv`. It was made without opening outcomes.csv, trades.md, the
stream transcripts, teacher-audit, claims, evolution-log, portrait, heart, journal/labels or journal/backtests.

- **Frames:** 132 rows use Audrey's strips (`decision-frames/<id>/` m060, m015, m005 and m000; m030 was skipped). 79
  rows use the single `frames_pre` frame, because their strip had not landed when they were labelled. Audrey's strips
  arrived later for 53 of those 79. They were not re-labelled, because I had by then seen later frames of the same
  streams.
- **No usable frame (10):** call "?" and confidence 0. Six rows have no pre-decision frame, or the chart isn't on
  screen (decided before the stream, a Minecraft or menu screen, or a teaching drawing). Four rows show the wrong chart:
  gold traded with NQ shown (twice), NQ traded with BTC shown, and a blank pane.
- **Contaminated (31):** the `notes` column says why. Most cases are on-screen account or P&L overlays, open-position
  P&L, or "blown account" counters (the 2026-09-29 stream). A few are rows I labelled after already seeing a later frame
  of the same stream. Their calls are still on the setup only, but give them less weight when scoring.
- **Multi-entry rows** (one id holding several entry times) are judged on the first entry only.
- **How I decided:** the seven context questions (context.md), then his closure score /10 (feel.md), then his batch-2
  loss reasons (playbook.md). Rules that weighed most: no close yet, pre-open or after 11:00, RR under 1 from the actual
  entry, a target already swept, liquidity still on both sides or a sweep not yet taken, flipping or re-entering
  minutes after a trade, and chop. News straddles were always SKIP. TAKE needed a sweep of a named level, a fast V or
  rejection, a clean draw at about 1.5R or better, and a time inside his window.
- **Result:** 36 TAKE, 169 SKIP, 10 "?". Scoring against outcomes is for the main Izzy.
