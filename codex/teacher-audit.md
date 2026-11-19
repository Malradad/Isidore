# Teacher audit — Dodgy's on-stream trades

Every TAKE and SKIP from his live streams (Audrey's logs in `source/streams/`), scored against
what price actually did. Unedited streams, so this is his real record, not his highlight reel.
`his` = his own words · `~` = read from frames · `✓px` = checked against real NQ/MNQ prices.

Three kinds of trading appear on stream; only (A) is his playbook:
**(A) playbook** · **(N) news straddle** (buy-stop + sell-stop around CPI/NFP to pass an eval; no stop) ·
**(G) eval gamble** (stream announced as "aggressively taking plays that aren't A+").

## Takes — (A) playbook
| stream | market time (NY) | tf | side | account | entry | stop | target | result (his) | R | ✓px | setup context he named |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-02 KhQiTa8YxJk | 09:39:21 | 30s | L | live+evals | 28,695.50 ~ | 28,660.25 ~ | 28,723.50 ~ | TP | +0.8 ~ | — | 30s inverse off manipulation leg; 4h inverse bias |
| 2026-11-02 KhQiTa8YxJk | 10:10:12 | 30s | L | Vest, light | 28,720.25 ~ | 28,706.00 ~ | 28,750.00 ~ | TP (~$600) | ~+2.1 ~ | — | B setup; BPR holding; momentum candle out of chop; CISD; LRLR above |
| 2026-10-02 JUDH0MmuhQs | 09:42:57 | 1m | L | props (copy) | 31,154.25 ~ (model 31,146.50) | 31,101.75 ~ (OB) | 31,190 partial, runner 31,223 | partial at high, runner BE | ~+0.7 to +1.3 ~ | — | NFP day; sweep of sellside into 50% discount; 1m IFVG + OB; waited ~10 min for the close; "only trade of the day" |
| 2026-09-11 7vLdDIq4J0A | 08:38:09 | 1m | L | ? (1 mini) | ~29,350 ~ | swing low (not shown) | data highs ~29,400 ~ | TP (~$1,000, ~+50 pts) | ? | — | CPI day; V-shape; inverse to the news candle's data highs; BE at rejection block; then "done for the day" |
| 2026-09-29 oiJnEazL4Lg | 09:31:42 | 1m | S | live (+eval) | ? | "probably no stop" | equal lows | win (his) | ? | — | Judas swing off the open; CISD + IFVG after sweeping the high; LLR |

## Takes — (N) news straddles and (G) eval gamble (not playbook; logged for honesty)
| stream | what | result (his) |
|---|---|---|
| 2026-10-02 JUDH0MmuhQs | (N) NFP straddle, 4 minis, no stop, to pass a Lucid eval | long leg filled, "+$5,000", passed |
| 2026-09-11 7vLdDIq4J0A | (N) CPI straddle, 4 minis each side, "no stop loss for this" | short leg, "got funded" |
| 2026-09-29 oiJnEazL4Lg | (G) 26 takes on Apex 25K evals, often no stop ("stop loss is the account") | **4 accounts blown**, 5th passed |

## Skips (with what happened next)
| stream | market time (NY) | tf | side | his reason | what price did ~ |
|---|---|---|---|---|---|
| 2026-11-02 KhQiTa8YxJk | 09:33:00 | 30s | L | gap too small, choppy, nothing obvious | — |
| 2026-11-02 KhQiTa8YxJk | 09:54:09 | 30s | L | eval-only: terrible liquidity, chop | "already getting wrecked" (his) |
| 2026-11-02 KhQiTa8YxJk | 09:56:07 | 30s | L | tiny 30s, eval trade, chop | — |
| 2026-11-02 KhQiTa8YxJk | 10:01:10 | 30s | L | decent EV play, not live | — |
| 2026-11-02 KhQiTa8YxJk | 10:31:55 | 1m | S | A+ from 4h gap, skipped: already 2/2 | in profit ~ (28,848 → 28,809) |
| 2026-10-02 JUDH0MmuhQs | 08:38:36 | 1m | S | buyside still above, "shorting a freight train" | worked (his: "can't believe that short worked") |
| 2026-10-02 JUDH0MmuhQs | 08:43:28 | 1m | L | too high in premium; eval-only | — |
| 2026-10-02 JUDH0MmuhQs | 08:48:49 | 30s | L | too high; eval play at most | worked (his: "the eval play worked") |
| 2026-10-02 JUDH0MmuhQs | 09:33:18 | 1m | L | RR trash; 30s had no internal liquidity / no BE point | — |
| 2026-10-02 JUDH0MmuhQs | 09:39:20 | 1m | L | no close yet: "you can't jump the gun" | then closed → became his trade |
| 2026-10-02 JUDH0MmuhQs | 09:59:04 | 1m | L | "didn't go the first time"; negative R (~0.64) | hit target (his) |
| 2026-09-11 7vLdDIq4J0A | 09:31:57 | 2m | L | no close; no internal liquidity | — |
| 2026-09-11 7vLdDIq4J0A | 09:34:27 | 1m | L | done for the day: "following my rules" | stopped out / maybe saved (his) |
| 2026-09-11 7vLdDIq4J0A | 09:46:02 | 30s | L | not in (commentary) | BE (his) |
| 2026-09-11 7vLdDIq4J0A | 09:49:43 | 15s | L | price action already bad: "why trust this setup" | — |
| 2026-09-11 7vLdDIq4J0A | 10:07:17 | 1m | S | (maybe, if zone breaks) | — |
| 2026-09-11 7vLdDIq4J0A | 10:21:01 | 3m | L | eval-only ~1R; already done | — |

## Running score
- Streams audited: **4 of 37** · **(A) playbook takes: 5, all wins by his words** (2 full TP, 1 partial+runner BE,
  1 TP ~+50 pts, 1 live short "won") · Skips: 18 (+4 in the gamble stream) · Price-checked: 0
- (N) news straddles: 2 (both "passed") · (G) eval gamble: 4 accounts blown, 1 passed.
- Verdict: none yet. 5/5 in his words is not evidence; price checks needed, and ≥ 10 streams.

## Patterns (update as streams come in)
- **About one playbook trade per day, then he stops** — even skipping setups he calls good or A+
  ("I'm done… following my rules"). Matches the only positive backtest variant (max 1 trade/day).
- **No close, no trade:** waited ~10 min for a 1m close rather than front-run (JUDH0MmuhQs 09:33–09:42).
- **Skip reasons so far:** chop / no obvious liquidity (5) · too high in premium / location (3) ·
  bad or negative RR (2) · no internal liquidity = no breakeven point (3) · already done for the day (4).
- **Management:** BE "where the BE should be" (model entry / rejection block), partial at ~1R or the
  first high, hold one runner. Targets: news-candle "data highs/lows", "last low-resistance high", equal lows.
- **Days:** 2 of 4 audited streams are CPI/NFP days; his playbook trade came after the news candle,
  targeting its data highs.
- **Honesty flags:** his account results mix (N) straddles and (G) gambling with playbook trades;
  "100% win rate this week", "80% win rate, avg RR 1.5" are claims to test, not facts.
- Skips cite **chop / no obvious liquidity / gap too small** most often (3 of 5).
- Takes: quick breakeven, ~1:1 targets, both on 30s, both longs with a 4h bullish bias.
