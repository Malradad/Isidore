# Teacher audit — Dodgy's on-stream trades

Every TAKE and SKIP from his live streams (Audrey's logs in `source/streams/`), scored against
what price actually did. Unedited streams, so this is his real record, not his highlight reel.
`his` = his own words · `~` = read from frames · `✓px` = checked against real NQ/MNQ prices.

Three kinds of trading appear on stream; only (A) is his playbook:
**(A) playbook** · **(N) news straddle** (buy-stop + sell-stop around CPI/NFP to pass an eval; no stop) ·
**(G) eval gamble** (stream announced as "aggressively taking plays that aren't A+") · **(C) chat-poll trades he disagreed with** · **(P) paper/for fun** (outside his session, "I don't really trade Asia").

## Takes — (A) playbook
| stream | market time (NY) | tf | side | account | entry | stop | target | result (his) | R | ✓px | setup context he named |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-02 KhQiTa8YxJk | 09:39:21 | 30s | L | live+evals | 28,695.50 ~ | 28,660.25 ~ | 28,723.50 ~ | TP | +0.8 ~ | ✓px TP first (fill 28,711.75 at the minute close; worst −24 pts, stop never touched) | 30s inverse off manipulation leg; 4h inverse bias |
| 2026-11-02 KhQiTa8YxJk | 10:10:12 | 30s | L | Vest, light | 28,720.25 ~ | 28,706.00 ~ | 28,750.00 ~ | TP (~$600) | ~+2.1 ~ | ✓px TP first (fill 28,719.25; no adverse move) | B setup; BPR holding; momentum candle out of chop; CISD; LRLR above |
| 2026-10-02 JUDH0MmuhQs | 09:42:57 | 1m | L | props (copy) | 31,154.25 ~ (model 31,146.50) | 31,101.75 ~ (OB) | 31,190 partial, runner 31,223 | partial at high, runner BE | ~+0.7 to +1.3 ~ | ✓px partial 31,190 first (fill 31,146.50 = his model entry; worst −1.75 pts) | NFP day; sweep of sellside into 50% discount; 1m IFVG + OB; waited ~10 min for the close; "only trade of the day" |
| 2026-09-11 7vLdDIq4J0A | 08:38:09 | 1m | L | ? (1 mini) | ~29,350 ~ | swing low (not shown) | data highs ~29,400 ~ | TP (~$1,000, ~+50 pts) | ? | ✓px 29,400 reached (fill 29,371.75; worst −29 pts; his stop not logged) | CPI day; V-shape; inverse to the news candle's data highs; BE at rejection block; then "done for the day" |
| 2026-09-29 oiJnEazL4Lg | 09:31:42 | 1m | S | live (+eval) | ? | "probably no stop" | equal lows | win (his) | ? | ~px direction right: +110 pts after 2 h (best +132, worst −43); levels not logged | Judas swing off the open; CISD + IFVG after sweeping the high; LLR |
| 2026-09-04 N6eOC8wtapo | before 09:50 (carried) | 1m | L | funded (~30 copy) | 29,599.50 ~ | 29,539.50 ~ | 29,694 (data high) | **BE** after coming ~2.5 pts from target; gave back ~+92 pts open | ~0 | — | NFP day; Judas swing re-entry; data high = relative equal highs + 08:30 high; planned "out by 10:00" but didn't exit |
| 2026-09-04 N6eOC8wtapo | 10:14:30 | 30s | L | funded | ~29,629 ~ | 29,603.75 ~ → **widened** to 29,594.75 | 29,694 | **stop (−1R; ~−35 pts vs widened stop)** | −1.0 to −1.3 | — | "A setup", delivering from a gap, data high above; stop widened mid-trade |
| 2026-09-04 chlCV294CTk | 08:44:34 | 1m/2m | S | eval | 29,558 ~ | 29,579 ~ | sellside 29,475 ~ | **closed early, ~+47 pts** | ~+2.2 ~ | — | NFP day after the 08:30 candle; "B setup… coming out the two minute"; exited early (eval already passed) |
| 2026-09-04 chlCV294CTk | 09:14:14 | 2m | L | **live** (+funded, see 09:50 row) | 29,564.50 ~ | 29,535.25 ~ | 29,694.25 (data high) | **BE** (moved to BE before the open) | 0 | — | He called it "not a good trade… a pattern trade due to RR and statistics"; 25 min earlier he said such longs are pattern trading |
| 2026-08-12 MHyNCqLCI7k | 09:49:12 | 1m (5m inverse) | L | funded (not live) | ~29,970.50 ~ | ~29,915 ~ → BE | buyside above | **BE** | 0 | — | CPI day; bullish daily bias; chop under 30,000; he later: "don't drop to the 1m in chop" |
| 2026-07-14 nE8GE9YBd8k | 09:45:35 | 2m | L | **live** (micros, half size) | ~29,797 ~ | ~29,743 ~ | ~29,849.75 (1R) | **cut early, ~−0.5R** ("down ~$300") | −0.5 | — | CPI day he had called a no-trade day; "strength of ES"; no 3m close, bad price action |
| 2026-03-11 Lprbu9HeOCI | 09:59:15 | 4m | L | Lucid evals (MNQ) | ~25,103 ~ | 25,062.50 ~ | "up here" | **partial at target, rest BE** (small win) | ~+0.3 ~ | — | CPI day; chat poll said yes and he agreed: "four minute looks really good" |
| 2026-03-11 Lprbu9HeOCI | 10:32:18 | 1m | S | Lucid evals (MNQ) | ~24,993 ~ | 25,020.75 ~ | equal lows ~24,950 | **BE** ("break even saved me") | 0 | — | his own call, toward equal lows |
| 2026-02-13 7w6pya1dubs | 10:26:59 | 30s | L | Alpha evals | ~24,818.50 ~ | ~24,805.50 ~ | ~24,850 (the high) | **TP** | ~+2.4 ~ | — | CPI day; "little 30-second inverse" to the high |
| 2025-10-15 YTBcXcI70io | 09:42:04 | 1m/30s | L | Apex (half size) | ~24,963 ~ | 24,947.25 ~ | 25,045.50 (buy side) | **stop** | −0.5 | — | indicator launch day; "I don't love this… bad play" |
| 2025-10-15 YTBcXcI70io | 09:44:55 | 30s/1m | L | Apex (full) | ~24,978 ~ | ? | 25,045.50 | **stop** | −1.0 | — | "I know it's invalid, but I'm trying to take what the indicator is gonna alert" |
| 2025-10-15 YTBcXcI70io | 09:51:48 | 30s | L | Apex (full) | 24,953.25 ~ | 24,926.25 ~ | 25,045.50 | **out early, ~+78 pts** (target hit later) | ~+2.9 | — | third attempt at the same idea; "footprints sold it"; rule: retry only if ≥ 2R |
| 2025-10-09 q-cngrviF2A | pre-09:13 | 3m | S | Apex (half, micros) | 25,321.25 ~ | 25,330 ~ → **widened** 25,334.50 | 25,293.75 (LRLR) | **TP** after widening stop "last second" | ~+3 (vs original) | — | "a B… just guessing"; would have been stopped without the widen |
| 2025-10-09 q-cngrviF2A | 10:49:51 | 5m | L (gold) | Apex (2 micros) | ~4,035 ~ | ~4,029.5 ~ | 4,046.2 (equal highs, 1R) | **BE** | 0 | — | gold model window 8–12 |
| 2025-10-09 q-cngrviF2A | 11:00:07 | 5m | L | Apex ("really light") | ~25,250 ~ | 25,220.25 ~ | 25,349 (LRLR) | **BE** | 0 | — | late session |

## Takes — (N) news straddles and (G) eval gamble (not playbook; logged for honesty)
| stream | what | result (his) |
|---|---|---|
| 2026-10-02 JUDH0MmuhQs | (N) NFP straddle, 4 minis, no stop, to pass a Lucid eval | long leg filled, "+$5,000", passed |
| 2026-09-04 chlCV294CTk | (N) NFP straddle "full port", 4 minis, eval | short leg to target, passed (his) |
| 2026-07-14 nE8GE9YBd8k | (N) CPI straddle on paper; (P) 2 funded micro trades "for fun" | straddle ~+$5.1k paper; micros: short −1R, long +1R (net ~0) |
| 2026-08-12 MHyNCqLCI7k | (N) CPI straddle on paper; data "leaked" early, buy stop filled ~53 pts high, reversed | **≈ −$10.7k paper** (first straddle loss) |
| 2026-08-12 MHyNCqLCI7k | (P) paper 30s long he "didn't love"; (O) funded short at the "30k level", "not really my model" | long: 3 of 4 to target; short: got out (P&L not said) |
| 2026-08-07 qbHHGoPD6Yc | (N) NFP straddle on paper + Tenacity competition account | long leg; +$245.64 (competition) |
| 2025-10-09 q-cngrviF2A | (P) 2 paper trades ("complete pattern trade"; "for fun") | BE; not shown |
| 2025-11-14 imzrLPjXVxE | (P) two PM paper shorts ("this just shows why I don't trade PM") | 1 likely stopped, 1 open +£319 at stream end |
| 2026-02-13 7w6pya1dubs | (N) CPI straddle + **hedging across Apex accounts** (long in one, short in another); (P) 1m "F/U long… for fun, accounts I don't really care about" | straddle: "passed five Topsteps"; F/U long cut for a loss |
| 2026-03-11 Lprbu9HeOCI | (N) CPI straddle on paper; (C) chat-poll short he disagreed with ("trading through a 15 minute") | straddle ~TP; poll short −$167.50 (−1R) |
| 2026-04-03 jOmHQ7INwFw | (N) NFP straddle on ~20 Apex evals, 6 minis each ("complete gambling… risk management: nonexistent") | long leg; "all 20 passed" (his) |
| 2026-08-16 7ZBHfQC6Nss | (P) Asia paper trades, "invalid according to my model" short and a "for fun… gambling" long | short ~BE (−5.5 pts), long +0.7R |
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
| 2026-09-04 N6eOC8wtapo | ~10:29 | 1m | L | external gap above; no CISD; "one confluence is not enough" | price kept falling ~ |
| 2026-09-04 N6eOC8wtapo | 11:19:57 | — | S | (leaving) "only long if we sweep sell side" | — |
| 2026-09-04 chlCV294CTk | 08:37:23 | 1m | L | no structure, sellside below: "pattern trader" | — |
| 2026-09-04 chlCV294CTk | 09:29:35 | 30s | L | ("looks so good") just stopped at BE, didn't re-enter | **ran ~+70 pts** ~ (missed winner) |
| 2026-09-04 chlCV294CTk | 09:31:27 | 5m | L | no real entry, would be a chase | — |
| 2026-09-04 chlCV294CTk | 09:37:23 | — | S | data high above; no draw on liquidity down | — |
| 2026-09-04 chlCV294CTk | 09:42:26 | 15s/30s | L | internal liquidity build-up "sucks"; rejecting BPR/0.705 | — |
| 2026-08-12 MHyNCqLCI7k | 09:35:08 | 2m | S | against daily bias: "rather wait for a long" | — |
| 2026-08-12 MHyNCqLCI7k | 09:41:59 | 1m | L | no internal draw, into a high that rejected a big gap | — |
| 2026-08-12 MHyNCqLCI7k | 09:53:07 | 3m | S | "A plus" from premium, skipped only for bullish bias | — (day chopped; bias wrong per him later) |
| 2026-08-12 MHyNCqLCI7k | 10:06:22 | 30s | L | pattern trade / eval play | — |
| 2026-08-12 MHyNCqLCI7k | 10:18:40 | 3m | L | candle never closed above the gap | — |
| 2026-08-07 qbHHGoPD6Yc | 08:44:28 | — | S | "not interested in any trade" after the news | — |
| 2026-08-07 qbHHGoPD6Yc | 09:26:22 | 30s | L | "textbook" but no longer bullish | — |
| 2026-08-07 qbHHGoPD6Yc | 09:31:00 | 1m | L | too close to the data low → would be BE, wants full TP | — |
| 2026-08-07 qbHHGoPD6Yc | 09:36:40 | 2m | S | against bias: "rather wait for a long" | — |
| 2026-08-07 qbHHGoPD6Yc | 09:49:32 | 1m | S | middle of the range, two draws on liquidity | — |
| 2026-08-07 qbHHGoPD6Yc | 09:55:51 | 2m | S | eval play, not funded | — |
| 2026-08-07 qbHHGoPD6Yc | 10:08:25 | 30s | S | tape-reading only | "just got wrecked" (his) |
| 2026-08-07 qbHHGoPD6Yc | 10:16:30 | 2m/3m | L | "A" long off data-low sweep + CISD, skipped (psychology/weekend) | **hit target** ~ (R:R 1.23) |
| 2026-07-14 nE8GE9YBd8k | 09:23:21 | 30s | L | didn't see it ("textbook… light bulb candle, CISD") | — |
| 2026-07-14 nE8GE9YBd8k | 09:30:44 | 30s | L | targets not engineered | — |
| 2026-07-14 nE8GE9YBd8k | 09:37:45 | 3m | L | "A plus" (discount, off FVG, swept) but never closed | — |
| 2026-07-14 nE8GE9YBd8k | 10:23:47 | 5m | S | pattern trade, shorting into a BPR | — |
| 2026-07-14 nE8GE9YBd8k | 10:47:00 | 3m/5m | S | "mentally in", not trading (already lost) | — |
| 2026-04-03 jOmHQ7INwFw | Tue 31 Mar (recap) | — | S | "mechanically good" but don't fade data highs above | — |
| 2026-04-03 jOmHQ7INwFw | Thu 2 Apr 10:25 (recap) | 5m | S | called it A+, but: first inverse out of a giant pump — don't short it | — |
| 2026-03-11 Lprbu9HeOCI | 08:41:43 | 1m | S | tape-read only (death candle, breaker) | BE by his words |
| 2026-03-11 Lprbu9HeOCI | 09:05:12 | 3m | L | chat poll vetoed it (to data highs) | **hit target** ~ (~2R his words) |
| 2026-03-11 Lprbu9HeOCI | 10:51:24 | — | L | pattern-wise only; getting off | — |
| 2026-02-13 7w6pya1dubs | 08:34:47 | 30s | L | tape-read before the open | — |
| 2026-02-13 7w6pya1dubs | 08:36:42 | 1m | S | 70-pt stop, hourly not broken, bad targets | — |
| 2026-02-13 7w6pya1dubs | 09:39:44 | 5m | S | called it, tape-read only | **TP** (his) |
| 2026-02-13 7w6pya1dubs | 09:43:33 | 1m | L | "A+", but against his bias | **hit target** ~ (data high) |
| 2026-02-13 7w6pya1dubs | 09:55:14 | 1m/30s | L | B setup; missed the 30s | — |
| 2025-11-14 imzrLPjXVxE | 14:30:32 | 1m | L | tape-read only (PM) | failed ("getting cooked") |
| 2025-10-09 q-cngrviF2A | 09:53:15 | — | S (YM) | tape/chase call, no position | YM level hit (his) |

## Running score
- Streams audited: **20 of 37** (4 with no trading) (incl. 2 with no trading: weekly outlook, 1 Mar joke clip) · **(A) playbook takes: 20 → 10 wins (1 small), 6 breakeven, 4 losses** (his words; first 5 ✓px) ·
  Skips: 55 (+4 in the gamble stream) · Price-checked: 5 of 20. Avg ≈ +0.65R per take ~ (≈ +13R total; one win only because he widened the stop) (wins ~+0.7–2.2R, 3 × 0R, 1 × −1R).
- **Breakevens and the loss all came on one day (4 Sep NFP)**, the day the "93%" data high missed by ~2.5 pts.
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
- **His losses come from breaking his own rules** (4 Sep): planned "out by 10:00", didn't exit, rode a
  near-target winner back to BE; then widened the stop on the next trade and took −1R+.
- **Both his losses came on days he'd flagged as bad** (4 Sep: no-context pattern trades; 14 Jul: CPI day he
  called a no-trade day in advance, "inside this range you're just guessing"). On clean days he wins.
- **Bias (1 Mar lesson):** hard vs soft bias from the 15m/1h/4h FVG inversion; "stop-loss placement is basically
  just a close back above the inversion" — matches the maker's confirmed stop rule ✓.
- **Trend-line targets cut both ways (14 Nov 2025):** "most of my losses come from going to trendline liquidity
  and not being able to break it, but my best wins also occur there." Don't trade a flag with trend-line
  liquidity on both sides. PM session is not his ("why I don't trade PM").
- **His beginner rules (3 Apr):** one trade a day; trade only 09:30–10:30, favourite 09:30–09:50; if there's no
  draw on liquidity, wait for New York to form one. Don't fade data highs; don't short the first inverse out of
  a giant pump. Bias: inside weekly + monthly FVG → bullish; "fully bullish" after the daily FVG inverts.
- **Between two external PD arrays → no continuation trades;** wait for stop losses to build (engineered
  liquidity), then trade toward them. Count resting orders on each side to pick the draw (7 Aug).
- **No-trade days so far: 2 of 9 streams** (12 Aug, 7 Aug) — both news days where he only did the straddle.
- **"No trade day" is a real outcome:** 12 Aug (CPI) he took no live trade: "if the market doesn't prove the
  bias, no trade"; skipped an "A plus" short only because it fought his daily bias.
- **Time as a rule:** "10 AM reversals"; "I literally trade based off time."
- **Selection warning (his own words, 7ZBHfQC6Nss 00:37:51):** "when I'm streaming… I probably have a 95%
  win rate… It's all my own plays off stream I lose on." So on-stream trades may not represent his full
  record. The audit measures his *on-stream selection*, which is still what we can learn from.
- **"From 60% to 80% win rate: lower your R"** (01:13:05): his high win rate comes partly from small targets.
- **Straddle on ~20 evals at once (3 Apr):** the eval-passing business is a big part of his activity.
- **Off-stream losses he admits:** "lost 10k in like 30 seconds… on my live account" (Feb/Mar 2026); "most money I've ever lost… like 30k" (11 Mar).
- **Bias skips that would have won: 3** so far (2 Nov A+ short, 12 Aug ×0, 13 Feb A+ long): his bias filter costs
  him some winners — test whether it pays overall.
- **Hedging across prop accounts** (13 Feb): opposite positions on different eval accounts to pass one — gaming firm rules.
- **Re-entry rule (15 Oct 2025):** up to 3 attempts at the same idea if it's ≥ 2R; never retry a 1R idea.
  Size down when he doesn't like it ("half size so I'm not down 2R yet").
- **His indicator can hide losers:** the "remove losing setups" display option means its chart history (and any
  marketing win rate shown from it) is not evidence.
- **"I've made more money off of Discord than I have trading"** (15 Oct 2025, his words).
- **"I probably have like a 40% win rate on my eval accounts… I just don't alert the trades because a lot of them
  lose"** (9 Oct 2025). Confirms selection: what he shows ≠ what he trades.
- **Weekly stop:** "once I'm up 5R or more in a week, I'm done" (live). Uses micros on props, minis on live.
- **Income:** "about 65k a month" from his Discord (7 Aug) — teaching, not trading, may be his main income.
- **Honesty flags:** his account results mix (N) straddles and (G) gambling with playbook trades;
  "100% win rate this week", "80% win rate, avg RR 1.5" are claims to test, not facts.
- Skips cite **chop / no obvious liquidity / gap too small** most often (3 of 5).
- Takes: quick breakeven, ~1:1 targets, both on 30s, both longs with a 4h bullish bias.
