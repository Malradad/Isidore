# Labeled record — all 48 playbook takes and the skips (2026-11-23, Izzy)

Source: `codex/teacher-audit.md` (37 of 37 streams, Audrey's logs in `source/streams/`).
**Method (blind as far as possible):** each take is flagged only from what he said or could know *before entry*:
his own grade, the day he'd announced, the time, his bias, and whether he'd already traded. Outcomes come from
the audit (his words; 7 ✓px). The labeler knew the outcomes, so this is not fully blind ~; every flag points to a
quote in the stream log so it can be re-checked.

Flags: **D** 2nd+ playbook trade of the day or after "done" · **F** day he flagged (no-trade / bad PA / chop he named /
gamble day / demo-only / eval-only week) · **X** he graded it below A or called it invalid, pattern, degen, teaching or
doubtful before entry · **T** outside his window (after 11:00, or pre-open with no news release) · **B** against his
bias or his equal-highs/lows rule · **P** for the audience (chat poll, indicator showcase, "for you guys").

## Results (takes)
| group | n | W/BE/L | win | loss | avg R (n with R) |
|---|---|---|---|---|---|
| all | 48 | 26/10/12 | 54% | 25% | +0.36 (40) |
| **clean (no flag)** | 7 | 6/1/0 | 86% | 0% | +0.95 (6) |
| **first trade of the day, not F or X** | 13 | 12/1/0 | 92% | 0% | +0.98 (9) |
| first trade of the day (any) | 26 | 18/4/4 | 69% | 15% | +0.61 (20) |
| 2nd+ trade / after done (D) | 22 | 8/6/8 | 36% | 36% | +0.11 (20) |
| flagged day (F) | 15 | 6/4/5 | 40% | 33% | +0.01 (13) |
| graded < A / invalid (X) | 13 | 4/3/6 | 31% | 46% | +0.18 (13) |
| audience (P) | 4 | 1/0/3 | 25% | 75% | −0.55 (4) |
| against bias / EQ rule (B) | 3 | 1/1/1 | — | — | n too small |
| outside window (T) | 12 | 8/2/2 | 67% | 17% | +0.63 (9) |
| one flag | 22 | 14/4/4 | 64% | 18% | +0.45 (16) |
| two or more flags | 19 | 6/5/8 | 32% | 42% | +0.08 (18) |

## Skips with a known outcome (by his reason)
Outcomes are only known when he or price showed what happened, and he comments more on dramatic moves, so this
over-counts skips that "worked". Read as direction, not rate.
| his reason | skip cost a winner | skip was right |
|---|---|---|
| quality: chop, gap too small, B/eval-only, no close, no trigger | 2 | 9 |
| equal highs / data wick / buyside above (no-short rule) + no trades between data high and low | 5 | 0 |
| already done / up for the week | 3 | 2 |
| before red-folder news | 2 | 1 |
| against his bias | 1 | 0 |
| missed it / psychology / chat veto (not a rule) | 6 | 0 |

## What it says ~
1. **His record is two different traders.** First trade of the day on a day he hadn't flagged, graded A or better:
   12W / 1BE / 0L, ≈ +1R. Everything else: ≈ breakeven (2+ flags: 6W/5BE/8L, +0.08R). His published record blends them.
2. **The flags that matter are his own words before entry:** a second trade, a day he called bad, a grade below A,
   an audience trade. Each roughly halves the win rate. These are exactly the rules Izzy can follow every time.
3. **His 11:00 cutoff is not supported** (outside-window takes 8W/2BE/2L). Keep it as his rule, but it is not where his losses are.
4. **His quality filters are right; his context vetoes cost winners.** Chop / small gap / no close skips were right
   9 of 11. The no-short-under-equal-highs/data-wick rule skipped 5 winners and is right 0 of 5 in what we can see —
   the P7 backtest decides it.
5. **Frequency:** clean first-trade A setups appeared on 13 of 37 stream days. Streams are chosen days, so this
   says nothing yet about ≥ 3/week; P8 (backtester) measures it on price.

## Izzy rules this supports (forward test, not live)
- One playbook trade per day; after a win or after "done", nothing.
- Skip any day the context flags as bad before the open (200+ pt overnight, range-bound/both sides swept, news chop).
- Take only A/A+ (sweep + inversion + discount/premium); never B; never a trade "to show something".
- Quality filters stay hard: candle close through the gap (and volume imbalance), no chop, gap big enough.

## Labels (takes)
| # | take (NY) | flags | result | R |
|---|---|---|---|---|
| 1 | 2026-11-02 09:39 | clean | W | 0.8 |
| 2 | 2026-11-02 10:10 | DX | W | 2.1 |
| 3 | 2026-10-02 09:42 | clean | W | 1.0 |
| 4 | 2026-09-11 08:38 | clean | W | ? |
| 5 | 2026-09-29 09:31 | F | W | ? |
| 6 | 2026-09-04 ~09:4x | clean | BE | 0 |
| 7 | 2026-09-04 10:14 | D | L | -1.15 |
| 8 | 2026-09-04 08:44 | X | W | 2.2 |
| 9 | 2026-09-04 09:14 | DX | BE | 0 |
| 10 | 2026-08-12 09:49 | F | BE | 0 |
| 11 | 2026-07-14 09:45 | F | L | -0.5 |
| 12 | 2026-03-11 09:59 | P | W | 0.3 |
| 13 | 2026-03-11 10:32 | D | BE | 0 |
| 14 | 2026-02-13 10:26 | clean | W | 2.4 |
| 15 | 2025-10-15 09:42 | XP | L | -0.5 |
| 16 | 2025-10-15 09:44 | DXP | L | -1 |
| 17 | 2025-10-15 09:51 | D | W | 2.9 |
| 18 | 2025-10-09 pre-09:13 | XT | W | 3.0 |
| 19 | 2025-10-09 10:49 gold | D | BE | 0 |
| 20 | 2025-10-09 11:00 | DT | BE | 0 |
| 21 | 2025-01-22 10:06 | FB | BE | 0 |
| 22 | 2025-01-22 10:57 | DF | L | -1 |
| 23 | 2025-01-22 11:08 | DFT | L | -1 |
| 24 | 2025-01-22 11:15 | DFT | BE | 0 |
| 25 | 2025-01-22 ~11:21 | DFT | W | 1 |
| 26 | 2024-03-01 10:05 | D | W | 1.5 |
| 27 | 2023-09-06 08:49 | T | W | 1.3 |
| 28 | 2023-09-05 09:12 | T | W | ? |
| 29 | 2023-09-05 10:11 | X | L | -1 |
| 30 | 2023-09-05 10:18 | DF | W | 2 |
| 31 | 2023-02-24 pre-08:44 | T | W | ? |
| 32 | 2023-02-24 10:12 | F | W | ? |
| 33 | 2023-02-24 10:23 | DF | L | -1 |
| 34 | 2023-02-24 10:24 | DFX | BE | 0 |
| 35 | 2023-04-21 09:32 | X | L | -1 |
| 36 | 2023-04-21 09:46 | DX | L | -1 |
| 37 | 2023-04-21 10:18 | D | W | ? |
| 38 | 2023-04-21 10:51 | D | W | ? |
| 39 | 2023-12-19 11:03 | BT | W | ? |
| 40 | 2023-12-19 11:26 | DBTP | L | -1 |
| 41 | 2024-01-12 11:04 | T | W | 1.5 |
| 42 | 2026-03-06 09:34 | clean | W | 1 |
| 43 | 2026-06-05 08:38 | clean | W | 0.5 |
| 44 | 2026-02-11 08:52 | X | BE | 0 |
| 45 | 2024-10-30 09:55 | F | W | 0.7 |
| 46 | 2024-10-30 10:56 | DXF | L | -1 |
| 47 | 2024-10-30 11:24 | DTF | W | 0.9 |
| 48 | 2023-03-14 ~10:47 | X | W | 0.5 |
