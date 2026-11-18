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
