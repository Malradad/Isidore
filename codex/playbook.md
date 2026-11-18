# Playbook — setups

One entry per setup. Add the first time it appears; strengthen or weaken as evidence comes in.

## iFVG — inversion fair value gap (his core setup)
- **Status:** ~ · times seen on stream: 0 · tested: 0 · hit rate: —
- **Market & timeframe:** NQ (also ES, gold, forex majors). Intraday; entry
  timeframe unconfirmed (1m–15m likely). Bias from 1H, 4H, 1D, 1W, 1M.
- **Background:** a fair value gap (FVG) is a three-candle imbalance: the wicks of
  candles 1 and 3 don't overlap, leaving a gap. Price often returns to fill it.
- **Trigger:** a candle **closes** through an FVG (not just wicks).
  - Bearish FVG closed above → now support → look **long**.
  - Bullish FVG closed below → now resistance → look **short**.
- **Entry:** on the close of the candle that closes through the gap. He does
  not wait for a retrace (X thread, 2023-12-31). Many ICT traders wait for the retest; he doesn't.
- **Filters:**
  - Direction must agree with higher-timeframe bias.
  - Must form or be tested inside a killzone (London, NY AM, NY PM). Outside → ignore.
  - Graded on: timeframe confluence, killzone, HTF agreement, gap quality, liquidity context.
- **Target:** internal liquidity: data highs/lows, old highs/lows inside FVGs,
  equal highs/lows. Goes long when internal liquidity above hasn't been taken.
- **Stop:** ✓ (maker, 2026-11-18) a **candle close** back through the inverted gap, not a price touch.
  - Long (green candle closed above a bearish gap): exit if a red candle closes back below the gap.
  - Short (red candle closed below a bullish gap): exit if a green candle closes back above the gap.
  - Wicks back into or through the gap don't stop him out; only the close does.
- **Invalidation:** same as the stop: the inversion has failed.
- **Isidore's note (~):** a close-based stop has no fixed price. One fast candle
  can close far past the gap, so the real loss on a trade is unknown until the
  candle closes. Position size can't be set from the stop alone. For the
  backtest, Isidore will measure the worst losses this produces on NQ and test
  a backup hard stop (e.g. beyond the gap's far edge plus a buffer) alongside it.
- **Why he believes it:** a failed gap shows the side that created it was
  overwhelmed; the gap then becomes a level for the winning side. ~
- **Sources:** `source/web/search-2026-11-18.md`
