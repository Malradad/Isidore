# Round 3 — calibrated blind read (2026-11-26)

Training: 61 decisions from 8 streams with outcomes (`training/lessons.md`). Test: 154 decisions from 29 other streams,
blind (`labels-r3.csv`, `training/r3-report.md`). Calls: 13 TAKE / 141 SKIP.

## Result (his audited playbook takes that fall in the test streams: 27)
| | R1 chart only | R2 + context | R3 + training |
|---|---|---|---|
| Izzy TAKE | 6 → 2W/3BE/1L, +0.10R | 2 → 2W, +1.00R | **6 → 6W, +1.12R** |
| Izzy SKIP | 19 → 13W/3BE/3L, +0.55R | 25 → 15W/6BE/4L, +0.51R | 21 → 11W/6BE/4L, +0.38R |
| his clean winners taken (of 4) | 0 | 1 | 3 |
| his 2+-flag trades taken (of 8) | 1 | 0 | 0 |

## Contamination — my fault, and it matters
`codex/context.md` named four test ids with results (my round-1 lessons). Three of R3's six winning TAKEs are among
them (2026-06-05_3, 2026-09-11_4, 2026-11-02_2), and the labeler flagged them. **Uncontaminated, R3 took 3 audited
playbook trades, 3 wins** (2023-09-06_1, 2024-01-12_2, 2024-03-01_4), and none of the rule-breaking ones.
Fixed: decision ids removed from codex/context.md. Context packs that mention earlier trades that day are "what he
knew", so they stay.

## Read ~
- Precision holds across rounds 2–3: when context-aware Izzy says TAKE on his playbook trades, it has won every time
  (clean rows: 2 + 3). It never took a rule-breaking trade.
- Recall is still low: 13 TAKEs across 29 stream days (~0.45/day) vs the 1–2/day target. Many test days are flagged
  days (straddles, PM, eval/game streams), so part of that is right.
- Historical streams are now used up as a clean test. **The honest next test is forward: shadow him live.**
