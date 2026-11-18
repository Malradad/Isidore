# Visual notes — what his charts actually look like

Frames live in `source/frames/<video id>/` (frame N = (N-1)×10 s; live streams ×15 s).

## His chart setup (✓ seen, `frames/ETRextCcwCo/0014.jpg`, `0030.jpg`, Oct 2026)
- **Instrument / timeframe:** `NQ1!` (front-month NQ futures) on the **2-minute** chart, TradingView.
- **Indicator:** "iFVG Ultimate+ Deluxe | DodgysDD (2m)".
- **Grey boxes:** fair value gaps.
- **Short horizontal lines labelled `DD+` (blue) / `DD-` (red):** where an inversion fired —
  blue = bullish inversion (long), red = bearish (short).
- **Risk label on the line:** e.g. "DD+ 1 contracts = $1,110" — position size for the
  stop distance at his chosen risk.
- **Session in view:** ~06:40–10:10 New York time; the 09:30 cash open is where the
  biggest candles appear.

## His checklist panel (✓ seen, bottom-right of chart)
"Setup Grade" (e.g. B, B+) graded from six checks, each ✓ or ✗:
1. **Liquidity Sweep**
2. **HTF PDA Delivery** — price reached a higher-timeframe PD array (level)
3. **Delta Imbalance** — order-flow confirmation
4. **IFVG** — the inversion itself
5. **Clear Targets** — engineered liquidity to aim at
6. **SMT w/ ES** — divergence between NQ and ES

This matches the A+ list in `playbook.md` almost one-to-one, plus SMT.
In both frames: sweep ✓, HTF ✓, iFVG ✓; delta ✗, clear targets ✗, SMT ✗ → grade B / B+.

## Examples to build (need dense frames)
- [ ] ETRextCcwCo @ 02:10 — his "A+ looking back" short, ~4R
- [ ] ETRextCcwCo @ 04:52 — big green candles swallowing a big red one
- [ ] hd8OyKtQfx0 @ 01:10 — clean-looking 3m iFVG that fails (no engineered liquidity, second sweep)
- [ ] hd8OyKtQfx0 @ 04:10 — uglier setup that works because it targets 4 stacked highs
