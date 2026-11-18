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

## The maker's own sizing (✓ maker, 2026-11-18)
- **1, 2 or 3 MNQ** per trade, depending on the setup and the risk.
- **Risk per trade: $200–$250.**
- What that implies for the stop (risk ÷ ($2 × contracts)):
  | Contracts | Stop at $200 | Stop at $250 |
  |---|---|---|
  | 1 MNQ | 100 pts | 125 pts |
  | 2 MNQ | 50 pts  | 62 pts  |
  | 3 MNQ | 33 pts  | 42 pts  |
- So: tight stop (strong-volume candle stop) → 3 contracts; wide stop (swing stop)
  → 1 contract. Risk in dollars stays roughly fixed; contracts flex.
- These are Isidore's **starting limits** for paper and live trading.

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

## Execution in TradingView paper (tested 2026-11-18, journal Tests 1–2)
- **Shift+B / Shift+S:** market order in ~1–2 s, no dialog, but **no stop attaches**
  (TradingView has no default-stop setting). Adding the stop took Izzy 20–33 s.
- **Rule:** never use bare hotkeys for real money. On paper, allowed only if the stop
  is added immediately after.
- **Tested (journal Test 3):** pre-staged ticket fills in **~0.8 s with the bracket
  attached**. This is the entry method. ✓
- **Never click the chart's floating BUY/SELL buttons**: with one-click trading on they
  are instant market orders with no stop (caused one unplanned 12-s naked trade).
  Open the ticket with the **Trade** button.
- After each order the ticket resets and the TP/SL toggles switch off: **re-stage after every entry.**
- **Preferred:** keep the order ticket pre-staged during the session (qty, SL and TP
  toggles on, distances in ticks), so one click on Buy/Sell enters *with* the bracket.
  Then adjust the stop/target to the real levels.

## Alert freshness (✓ maker, 2026-11-18)
- **An alert seen more than 15 s after its bar_close is never traded.** Log it as
  "skipped: stale X s" with TradingView delay (sent − bar_close) and browser delay (seen − sent).
- Bot may not raise this limit. Only the maker can change it.
- Cause of the 63 s miss: Chrome paused the hidden/covered tab (TradingView fired on time).
  Chrome must be launched with: `--disable-features=CalculateNativeWinOcclusion
  --disable-backgrounding-occluded-windows --disable-renderer-backgrounding
  --disable-background-timer-throttling`, TradingView in its own visible window.
