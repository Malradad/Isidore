# Teacher audit — Dodgy's on-stream trades

Every TAKE and SKIP from his live streams (Audrey's logs in `source/streams/`), scored against
what price actually did. Unedited streams, so this is his real record, not his highlight reel.
`his` = his own words · `~` = read from frames · `✓px` = checked against real NQ/MNQ prices.

## Takes
| stream | market time (NY) | tf | side | account | entry | stop | target | result (his) | R | ✓px | setup context he named |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-02 KhQiTa8YxJk | 09:39:21 | 30s | L | live+evals | 28,695.50 ~ | 28,660.25 ~ | 28,723.50 ~ | TP | +0.8 ~ | — | 30s inverse off manipulation leg; 4h inverse bias |
| 2026-11-02 KhQiTa8YxJk | 10:10:12 | 30s | L | Vest, light | 28,720.25 ~ | 28,706.00 ~ | 28,750.00 ~ | TP (~$600) | ~+2.1 ~ | — | B setup; BPR holding; momentum candle out of chop; CISD; LRLR above |

## Skips (with what happened next)
| stream | market time (NY) | tf | side | his reason | what price did ~ |
|---|---|---|---|---|---|
| 2026-11-02 KhQiTa8YxJk | 09:33:00 | 30s | L | gap too small, choppy, nothing obvious | — |
| 2026-11-02 KhQiTa8YxJk | 09:54:09 | 30s | L | eval-only: terrible liquidity, chop | "already getting wrecked" (his) |
| 2026-11-02 KhQiTa8YxJk | 09:56:07 | 30s | L | tiny 30s, eval trade, chop | — |
| 2026-11-02 KhQiTa8YxJk | 10:01:10 | 30s | L | decent EV play, not live | — |
| 2026-11-02 KhQiTa8YxJk | 10:31:55 | 1m | S | A+ from 4h gap, skipped: already 2/2 | in profit ~ (28,848 → 28,809) |

## Running score
- Streams audited: 1 of 37 · Takes: 2 (2 W / 0 L, his words) · Skips: 5 · Price-checked: 0
- Verdict: none yet. Needs ≥ 10 streams and price checks.

## Patterns (update as streams come in)
- Skips cite **chop / no obvious liquidity / gap too small** most often (3 of 5).
- Takes: quick breakeven, ~1:1 targets, both on 30s, both longs with a 4h bullish bias.
