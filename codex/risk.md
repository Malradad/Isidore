# Risk — how he protects capital

_Almost nothing known yet. This is the biggest gap in the codex._

## What's reported (~)
- Warns against re-buying $50K prop evaluations after blowing one:
  "the illusion of a clean slate" hides the same broken habits.
- One ex-member: losses were often explained as not taken on a live or funded
  account. Isidore will judge his risk only from what can be checked.

## Stop rule (✓ maker, 2026-11-18)
- Exit on a candle close back through the inverted gap. Wicks don't count.
- Consequence: loss per trade is variable and set by the size of the exit
  candle, not by a level chosen in advance. A large NQ candle (news, open)
  can make one loss several times the normal size.

## Stop choice (✓ maker, 2026-11-18)
- Default: close back through the gap.
- Weak volume behind the inversion: swing low/high of the sweep (wider, survives a dip).
- Strong volume: just beyond the inversion candle (tighter, better R).
- The stop sets the size: wider stop → fewer contracts, so risk per trade stays fixed.

## Sizing in MNQ (✓ maker trades MNQ)
- Contracts = risk in $ ÷ (stop distance in points × $2).
- Example: $200 risk, 25-point stop → 200 ÷ (25 × 2) = 4 MNQ.
- If that gives less than 1 contract, the stop is too wide for the risk: skip the trade.

## Unknown (watch for on stream)
- Which timeframe's close counts for the stop (same as entry?).
- Whether he also uses a hard stop as a disaster backup.
- Position size, risk per trade, daily loss limit.
- Max trades per day; what he does after a loss.
- Whether he trades live, funded, or sim, and whether he shows it.
