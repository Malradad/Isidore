# Evolution log

_Session entries: date · what was learned · decision · maker response · performance · lesson._

## 2026-11-18 · First web search on the Teacher
- **Learned:** the Teacher is Dodgy (Ryan, @DodgysDD). ICT-school NQ day trader.
  Core setup: iFVG, a fair value gap that fails on a candle close and flips roles;
  filtered by HTF bias and killzones; targets internal liquidity. Wrote
  portrait, playbook, reasoning, markets, risk, claims.
- **Decision:** treat iFVG as a mechanical hypothesis to backtest on NQ, not as truth.
  Treat his win-rate marketing as untested claims.
- **Doubts:** reports of losses explained away as not live; earnings come mostly
  from teaching; risk rules almost unknown; official rulebook not found.
- **Gaps:** stop placement, sizing, entry timeframe, exact killzone times,
  his "internal liquidity rule". Several sources (whop.com, trustpilot.com,
  threadreaderapp.com) were blocked by the session network.
- **Maker response:** pending.

## 2026-11-18 · Maker teaches the stop
- **Learned (✓ maker):** the stop is a candle close back through the inverted gap.
  A green candle inverts a red (bearish) gap → stop is a red candle closing back
  below it; the reverse for shorts. Wicks don't count.
- **Lesson:** the setup is symmetrical and close-based end to end. The gap is
  the whole trade: entry, thesis, and exit.
- **Isidore's concern:** close-based stops make loss size variable. Backtest must
  measure the tail of losses and test a backup hard stop.
- **Still open:** which timeframe's close; whether he keeps a hard stop; sizing.

## 2026-11-18 · First three videos (newest first)
- **Studied:** "The Most Accurate IFVG Indicator" (2026-10-26), "The Wrong Way to
  Trade IFVG's" (2026-06-05), "Watch This if You Think You Know How Liquidity Works" (2026-05-28).
- **Learned:** the A+ iFVG: HTF level → one clean sweep → V-shape → inversion close →
  strong volume → target engineered liquidity, in his direction. Repeated sweeps and
  random targets are his named failure modes. Oct 2026 model adds order flow.
- **Conflict found:** the maker's stop (close back through the gap) is one of three
  stops he uses. He also uses swing stops and stops under strong candles.
- **Decision:** default to the maker's close stop; ask the maker which stop when.
- **Maker response:** pending. Agreed earlier to study newest first.
- **Next:** frames from his charts to see the A+ setup; then backtest claims 4 and 5.

## 2026-11-18 · Maker confirms the three stops
- **Decision:** proposed close stop by default, swing stop on weak volume, candle
  stop on strong volume.
- **Maker response:** confirmed ("what he says is also true").
- **Lesson:** stop placement follows the strength of the inversion. Backtest all three
  and compare, and test the volume rule that picks between them.

## 2026-11-18 · Maker teaches the gap timeframes
- **Learned (✓ maker):** he looks for gaps on 30 s, 1 m, 2 m, 3 m and 5 m.
- **Open:** how he chooses between them for a given trade, and whether the stop
  close is read on the same timeframe as the entry.
- **Backtest implication:** run the setup on all five timeframes and compare.

## 2026-11-18 · Maker trades MNQ
- **Learned (✓ maker):** the maker trades MNQ most of the time; NQ is too large for now. Be flexible.
- **Decision:** study and backtest on NQ charts (identical price, longer history);
  size, paper trade and trade in MNQ ($2/point). NQ only when the maker raises the allocation.

## 2026-11-18 · Maker's sizing
- **Learned (✓ maker):** 1–3 MNQ per trade, $200–$250 risk, depending on setup and risk.
- **Implication:** stop distance sets the contract count: ~33–42 pts → 3 MNQ,
  ~50–62 → 2, ~100–125 → 1. Fixed-dollar risk, flexible size.
- **Decision:** these are Isidore's starting limits.
- **Open:** account size, daily loss limit, max trades per day.

## 2026-11-18 · Paper trading approved
- **Maker response:** "try one order now" — approval to paper trade in TradingView ("Isidore", $50K).
- **First order:** a mechanics test (03:00 NY, outside killzones), not a strategy trade.

## 2026-11-18 · First backtest, strategy v0.2 (TradingView, default inputs)
- 30s +$191 (13 tr, PF 1.21) · 1m +$996 (13, PF 2.49) · **2m −$407 (10, PF 0.66)** · 3m +$706 (18, PF 1.66) · 5m +$187 (14, PF 1.15).
- History on the maker's plan was longer than Isidore estimated: 2m ≈ 6 weeks, 5m ≈ 3.5 months.
- **Lesson:** 10–18 trades per timeframe is noise; the ranges overlap. No conclusion yet.
  Need far more trades (longer data) before tuning. Max drawdown stayed under $850 everywhere.
- Alert "Izzy setups" is live on the 2m chart; strategy compiled first try.

## 2026-11-18 · Studied: new 2026 model, "IFVG's Don't Work", "IFVG's can NEVER fail"
- **Learned:** trend-line liquidity is now his #1 target; momentum candles only; most trades
  09:30–10:00 on the Judas swing; one false move per morning; one trade a day; breakeven at
  the internal draw; more confluence (OB, CISD, 50% HTF retracement).
- **Contradiction resolved:** both titles say the pattern only works with context, momentum
  and engineered liquidity. "Never fail" is hype (unfalsifiable).
- **Tension with the maker's all-hours test:** he trades almost only 09:30–10:00. Fine for
  mechanics testing; for performance, compare all-hours vs 09:30–11:00 (claim 9).
- **Code next (v0.4 candidates):** momentum-candle filter (body/range), max 1 trade/day option,
  "first false move only" after 09:30, trend-line liquidity detection (harder).

## 2026-11-18 · Studied: "Simplest IFVG Model" (Jul 2026), "How I Trade IFVGs Differently" (Oct 2026)
- **Learned:** his ranking — target first (fuel), one-sided liquidity, location, inversion
  off an HTF gap, push-through ≤ ~7 candles, then risk. Fuel on both sides = no trade.
  Four questions before entry. iFVG 30s–5m, bias 15m+.
- **Code v0.4 candidates (in priority order):** (1) fuel target = top of the unbroken
  lower-high chain; (2) skip when untaken fuel is on both sides; (3) push-through ≤ 7 candles;
  (4) momentum candle body filter; (5) location: entry in the lower/upper half of the
  sweep→target range; (6) max 1 trade/day option.
- **Remaining:** Masterclass, Comparing top 3 models, Scalping, Best trade 10R, $73K month,
  three live streams.

## 2026-11-18 · Execution: first alert-driven paper trade (Test 4)
- **Did:** v0.4 webhook alerts on 30s–5m → ntfy relay → waiter (0.79 s pipe). Took ONE trade
  on the first CONFIRMED: 1m LONG A, 3 MNQ, alert risk $120. Fill 27,420.25 (6.25 pts chase),
  stop moved to the alert's 27,394, stopped at 27,392.50 → **−$166.50**. `journal/2026-11-18.md`.
- **Learned ~:** the click lag (~22 s) and the chase cost more than the setup's own edge can
  absorb on a 20-pt stop. ARMED values change at the close (the stop jumped from Swing to
  Inversion candle), so size from CONFIRMED only. 1m alerts are noisy (ARMED → CANCELLED → ARMED within 2 min).
- **Decided:** stage on ARMED, click on CONFIRMED without retyping the ticks, then fix the
  prices after the fill. Proposal for the maker: skip a fill that would be more than ~25% of
  the stop distance away from the alert entry.
- **Maker:** approved the test (all hours, the alert as the plan). No level change; one trade is not evidence.

## 2026-11-18 · TradingView connector, Python backtester, first deep test
- **Did:** confirmed the official TradingView MCP connector (35 tools, no order tools). Pulled MNQ1! bars:
  1m 7,683 (10–18 Nov), 5m 5,537 (21 Oct–18 Nov); 2m/3m not offered. Built `tools/backtest/izzy_bt.py`,
  a bar-by-bar port of v0.4 that matches TradingView trade for trade (5m 49/49, 1m 15/15). Built the lab
  script "Izzy iFVG lab" (v0.5 filters as inputs) and ran Deep Backtesting on 1m, Jan 2025 – Nov 2026.
- **Learned ✓ (price):** **v0.4 loses**: 1,264 trades, PF 0.91, −$5,863 after costs, DD $8,007.
  Max 1 trade/day is the only positive variant (PF 1.05, +$1,107, DD $1,978). First vs 3rd+ sweep,
  momentum candles and 09:30–10:00 made no real difference. Engineered targets slightly better than
  single highs, still negative. My fuel target hurt (win rate 14%). His full A+ stack: 13 trades in 23 months.
- **Claims judged:** 4 ✗, 5 ~, 8 ✓, 9 ✗, 10 ✗. `journal/backtests/2026-11-18-deep.md`.
- **Decided ~:** no live-trading proposal can rest on v0.4. Paper trading v0.4 alerts is execution
  practice only. If paper continues, use max 1 trade/day. The edge, if any, lives in judgement I have not
  yet coded (HTF delivery, bias, "what's to the left") — next study must extract that from his charts.
- **Maker:** not yet reviewed.

## 2026-11-18 · NY killzones + Dodgy's filters (maker request)
- **Did:** deep 1m test, Jan 2025 – Nov 2026, AM 08:30–11:00 + PM 13:30–16:00, only setups Dodgy would take
  (engineered target, momentum, push ≤ 7, first sweep, grade ≥ B, 1/day).
- **Learned ✓ (price):** 103 trades, PF 0.80, −$1,346. All killzone signals: PF 0.85, −$12,348. Killzones and
  his filters do not create an edge in my model. Longs PF 1.14 vs shorts 0.57: the edge that shows is the trend.
- **Decided ~:** next test is HTF bias on (trade with the 1h/4h trend), AM only. `journal/backtests/2026-11-18-deep.md`.
- **Maker:** asked for this test; review pending.

## 2026-11-18 · + HTF bias (maker request)
- **Learned ✓ (price):** killzones + Dodgy's filters + HTF EMA bias: 1h PF 0.62 (56 tr, −$1,509), 4h PF 0.77
  (55 tr, −$808). An EMA bias does not create an edge. Every mechanical variant tested so far is negative.
- **Decided ~:** stop tuning filters. Next: code his real bias (HTF PD array delivery / draw on liquidity) from
  chart examples, or conclude the edge is discretionary.

## 2026-11-18 · First audited live stream (KhQiTa8YxJk, 2 Nov 2026, Audrey's log)
- **Seen:** ~7 setups, **2 taken** (both 30s longs, ~0.8–1R, both won), 5 skipped (chop, tiny gap,
  no obvious liquidity, "eval only", already 2/2).
- **Lesson 1 — selection is the method.** He passes on most inversions. My code takes them all and
  loses (23-month backtest). The difference is his skip list, so his skips are now training data.
- **Lesson 2 — his live style ≠ my code:** quick breakeven, ~1:1 targets on 30s, sells early, stops
  after two wins. My v0.4 holds for far liquidity targets. Test his management, not mine.
- **Lesson 3 — context he named before entries:** 4h inverse for bias, BPR (balanced price range)
  holding, Judas swing expected at the open, LRLR (low-resistance liquidity run) above, "momentum
  candle trading out of chop", CISD + IFVG as the "dream trade".
- **Lesson 4 — his own grading exists:** live account = A/A+, eval = B in chop. Use as labels.
- **Doubts:** one stream, two wins, is nothing. "Done for the day" then traded again. Hype
  ("best trader alive"). Live vs eval claims can't be verified; prices can.
- **Next:** audit his trades against real NQ prices (connector); code and test: chop filter,
  30s entries, BE at ~0.5–1R, 1R target, stop after 2 wins/day, require a named HTF PD array.

## 2026-11-18 · Every timeframe, out of sample, exits, session-end fix (maker: "yes")
- **Did:** deep 1m (from 2023-11-19) and 5m (from 2019-06) runs of v0.4 baseline and max 1/day, split by era;
  three exits on 5m; added the session-end flatten to Python and the lab (TradingView v2.0). 30s/2m/3m not
  available through the connector.
- **Learned ✓ (price):** no variant holds in both halves. Best: 5m max 1/day, 1,820 trades, PF 1.05, +$5.5K over
  7.5 years (~$3/trade), negative in 2019–22. Exits barely matter. Session-end fix cut the worst loss −$2,063 → −$233.
- **Decided ~:** stop tuning the mechanical model. Priority moves to auditing Dodgy's on-stream trades.
- **Maker:** approved the plan; review of the summary pending.

## 2026-11-19 · Teacher audit: streams 2–4 (NFP 2 Oct, CPI 11 Sep, gamble stream 29 Sep)
- **Learned:** his serious trading is ~1 playbook trade a day, then he stops, even on good setups.
  5 playbook takes so far, all wins in his words; none price-checked yet.
- **Big finding:** a lot of his stream "results" are not the playbook: (N) news straddles with no stop
  to pass evals (2) and a gamble stream (26 takes, 4 accounts blown). Any P&L he shows mixes these in.
- **Rules confirmed on stream:** no close, no trade (waited 10 min); skip when price is in premium,
  RR is poor, or there's no internal liquidity for a breakeven point; BE at the model entry.
- **Context terms to code:** news-candle data highs/lows as targets; "last low-resistance high";
  CPI/NFP-day behaviour after the 08:30 candle.
- **Next:** price-check the 5 playbook takes (TradingView quota reset today), and test
  "1 trade/day + his skip filters (premium, RR, no-BE-point)" in the backtester.

## 2026-11-22 · Claim 11 (multi-TF confluence) and the first price-checked teacher trades
- **Did:** coded claim 11 into the lab (v3.0) and Python (verified: same 31 trades on recent bars); deep 1m
  test 2023-11 → 2026-11, versions A and B with aligned controls. Price-checked his 5 playbook takes.
- **Learned ✓ (price):** claim 11 not supported: A PF 0.88 vs control 0.91, B 0.906 vs 0.907.
  His 5 playbook takes all hold up: 4 hit his target first (stops untouched), 1 went his way.
- **Decided ~:** the gap between my mechanical rules (losing) and his picks (5/5) is the thing to study.
  Next: label every skip/take in Audrey's logs with the context he named and look for what separates them.
- **Maker:** approved both tasks (relayed); merge to main awaits the maker's direct OK.

## 2026-11-22 · Audit: stream 5 (4 Sep NFP) + Izzy's price check
- **Price check:** his first 5 playbook takes hold up against real NQ prices (4 hit target before stop,
  1 right direction). My mechanical versions lose; his picks win → the edge is in selection/context.
- **Stream 5:** first non-win: a carried long went to BE after nearly hitting target (he planned "out by
  10:00" and didn't), then a 30s long stopped for −1R after he **widened the stop**. Record now 5W/1BE/1L.
- **Lesson:** his losses here come from breaking his own rules (time exit, moving the stop). Izzy's rules
  must include the ones he breaks: honor time exits; never widen a stop (already in codex/risk.md).
- **New claims:** news-day "data high hits 90% of the time"; "10 AM reversal". Both testable.

## 2026-11-22 · Audit: stream 6 (4 Sep NFP, part 1)
- **Takes:** eval short after the NFP candle (+~47 pts, closed early) and a **live** long he himself called
  "not a good trade… a pattern trade" → BE. Record 6W/2BE/1L across 9 playbook takes.
- **Lesson:** all his non-wins so far sit on one day, and they share a pattern: he took a setup he had just
  described as having no context, justified by a "93%" statistic. Context-free trades = his weak spot too.
- **Missed winner:** after his BE he skipped a 30s long that ran ~+70 pts ("didn't re-enter"). Re-entry
  after BE is an open question for the playbook.

## 2026-11-22 · Audit: stream 7 (16 Aug, Sunday Asia, paper)
- Not playbook: two paper trades he called "invalid" and "for fun". Logged as (P), excluded from the record.
- **Important caveat, in his words:** "when I'm streaming I probably have a 95% win rate… all my own plays
  off stream I lose on." The audit can measure his on-stream selection, not his whole P&L.
- "Lower your R to raise win rate": his win rate is partly small targets — judge him in R, not win %.

## 2026-11-22 · Audit: stream 8 (12 Aug CPI)
- **No live trade** ("no trade day"); one funded 1m long → BE in chop. Record 6W/3BE/1L over 10 takes, ≈ +0.6R avg ~.
- **First straddle loss:** paper CPI straddle ≈ −$10.7k (slipped 53 pts on the spike). The "news gamble" is risky,
  as he says himself; it confirms keeping (N) out of anything Izzy does.
- **Rules he states:** "if the market doesn't prove the bias, no trade"; "I need an IFVG to enter, minimally";
  "don't drop to the 1m in chop". Daily bias overrides even an "A plus" counter-trend setup.

## 2026-11-22 · Audit: stream 9 (7 Aug NFP)
- **No playbook trade** (only the straddle, +$246 on a competition account); 8 skips. He skipped his one "A"
  long (data-low sweep + CISD) and it hit target.
- **New context rule:** price between two external PD arrays (15m BPR and 3m gap) → no continuation trades;
  wait for engineered liquidity to build, then trade toward it. Also: no longs right on top of a data low.
- **Bias flag:** ~$65k/month from Discord. Record still 6W/3BE/1L over 10 playbook takes.
