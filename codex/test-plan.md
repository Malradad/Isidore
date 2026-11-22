# Test plan — what the audit says to test next (2026-11-22)

Built from 29 audited streams (codex/teacher-audit.md) and the backtests so far. The pattern: the raw iFVG
trigger has no edge; his on-stream picks win (5/5 price-checked); his losses cluster on days he flagged as bad.
So test **his context and his days**, not more trigger variations. Every test: MNQ/NQ, costs as v0.4,
split by year (a rule only counts if it holds in both halves), report PF, win %, net, max DD, trades, avg R.

## Priority 1 — his own mechanical model (claim: playbook "Mechanical model (his 2023 class)")
PDH/PDL taken in London or NY (not Asia) → the **last single opposite 5m (and separately 15m) FVG** closed through
with displacement → entry at that close. Stop: close back through the inversion (hard stop at the swing).
Target: next internal high/low; variant B: scale there + runner to the next S/A pool. One trade per day;
if it played out in London, no NY trade. Never trade inside yesterday's range. 2019 → now on 5m.

## Priority 2 — "when not to trade" filters (applied to P1 and to v0.4 max-1/day)
a. Overnight range (18:00–09:30) > 200 NQ pts → skip NY AM. (claim, 22 Jan 2025)
b. CPI/NFP days: no trade while price is between the 08:30 candle's high and low. (11 Jun 2025, 7 Aug)
c. Broadening formation: both sides of the prior range already swept → skip. (5 Sep 2023)
d. No longs with untaken equal lows below / no shorts with equal highs above. (his "first rule", 2023 → 2026)
e. Window: 09:30–10:30 vs 09:30–09:50 vs all day.
Report each filter alone and all together.

## Priority 3 — his trade management
On P1 (and v0.4 max-1/day): BE at the first internal high/low after entry; partial there + runner to target;
time exit at 10:00 if the target isn't hit ("10 AM reversal") vs no time exit.

## Priority 4 — target quality (context Q2)
Classify each signal's target by his tier list (S/A/B/C/F, codex/context.md). Compare PF and % target-hit by tier.

## Priority 5 — his news-day claims (cheap, descriptive)
a. "Data high hits ~90%": on CPI/NFP days, % of sessions where price trades above the 08:30 candle high (and,
   separately, the nearest relative equal highs) before 11:00.
b. "10 AM reversal": direction 09:30→10:00 vs 10:00→10:30, % opposite, by month.
c. Bias filter cost: P1 with vs without his bias (inside weekly+monthly FVG → only longs; daily FVG inversion flips).

## Not worth quota now
More inversion-trigger tuning; multi-TF confluence (claim 11, done, not supported).

## Priority 6 — feel (codex/feel.md), the maker's "muscle memory" request (2026-11-22)
Rebuild the live feel features historically from lower-timeframe bars (`request.security_lower_tf`, e.g. 15s/30s
inside 1m/5m; in Python from 1m inside 5m): **cross speed** (time into the candle when price first closed beyond
the gap edge), **flips** (crossed back before the close), **close location**, **body %**, **volume burst**,
**chop before** (overlap of the prior N candles), **reaction sharpness** (bars/points from sweep extreme to the
inversion close). On the P1 + filters rule set and on v0.4 max-1/day: does each feature separate winners from
losers, in both halves? Report the thresholds that hold, then a combined "feel score". Live alerts (v0.5) already
carry cross_s, flips, close_loc, body_pct, vol_ratio, vol_before_cross for the forward test.
