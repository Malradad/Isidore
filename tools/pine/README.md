# Izzy iFVG — TradingView strategy

`isidore_ifvg.pine` turns the playbook into code that reacts the moment a candle closes.
Use it to **backtest** (Strategy Tester) and **forward test** on the live chart.
Paper / research only.

## Install (2 minutes)
1. TradingView → open the **MNQ1!** chart → set the timeframe (start with **2m**).
2. Bottom panel → **Pine Editor** → *Open* → *New strategy*. Delete everything in it.
3. Paste the whole contents of `isidore_ifvg.pine` → **Save** (name it "Izzy iFVG") → **Add to chart**.
4. Open **Strategy Tester** (bottom panel) → *Overview* and *List of trades*.
5. Screenshot both tabs and save them to `journal/backtests/` (or send them to Izzy).

## Alerts (v0.2)
Every setup the strategy takes also fires a TradingView alert, once, at the bar close, with JSON:
`{"izzy":"setup","side":"LONG","grade":"A","symbol":"MNQ1!","tf":"2","entry":…,"stop":…,"target":…,"qty":2,"risk_pts":…,"stop_mode":"Swing","sweep":true,"strong_vol":false,"engineered_target":true,"time":"2026-11-18 09:42:00"}`

Create it: chart → **Alerts (⏰) → Create alert** → Condition: **Izzy iFVG** → **"alert() function calls only"** →
Expiration: open-ended → Notifications: popup + app (+ webhook later) → Create.
Izzy reads the alert log during the session, decides TAKE / SKIP, then enters with the pre-staged ticket.

## What it does
| Rule | Code | Source |
|---|---|---|
| Fair value gap (3-candle gap) | gaps ≥ 4 ticks, live 40 bars | playbook |
| Inversion = candle **closes** through the gap | long: close above a bearish gap; short: close below a bullish gap | playbook |
| One clean liquidity sweep first | price takes a swing low/high, inversion within 15 bars, **first sweep only** | Dodgy, "Wrong Way to Trade IFVGs" |
| Trade window | **all hours by default (v0.3, maker)**; optional 09:30–11:00 New York window | maker / killzones |
| Stops ✓ | Auto: strong volume → under inversion candle; weak → swing; normal → close back through gap (swing as hard stop) | maker |
| Target | nearest untaken swing high/low if ≥ 1R, else 1R | Dodgy (engineered liquidity, 1:1 live) |
| Size ✓ | $225 risk ÷ (stop × $2), max 3 MNQ, skip if < 1 | maker |
| Daily limits | max 3 trades, stop after 2 losses or –$500 | Izzy's proposal |
| Grade | +1 sweep, +1 strong volume, +1 equal highs/lows target → B / A / A+ | Dodgy's checklist |
| Costs | $0.62/contract commission, 1 tick slippage | estimate |

## Not in v0.1 (yet)
- **Delta / order flow** — TradingView basic volume only; uses volume vs average as a stand-in.
- **SMT with ES**, **HTF PD array**, and the **V-shape** check (approximated by sweep → inversion within 15 bars).
- **Bias** is manual (input) or a simple HTF EMA filter. Set it each morning.

## History on the Pro plan
~10,000 bars: about 1 week on 1m, 2 weeks on 2m, 5–7 weeks on 5m. Enough to check it works,
not enough to prove an edge. Longer tests need Deep Backtesting (Premium) or downloaded data.
