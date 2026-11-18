# Bot's in-page code

Bot's in-page trigger, watchdog and auto-restage live inside the TradingView tab and are lost when
Chrome restarts. **Bot must keep the current source here** (`trigger.js`) and reinstall it from this
file after every restart. Limits it must enforce: paper "Isidore" only, MNQ, one position at a time,
**freshness ≤ 15 s** (codex/risk.md), duplicate guard (tf + side + bar_close), balance ≥ $47,500.
