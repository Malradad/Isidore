# Backtester

`izzy_bt.py` is a bar-by-bar Python port of `tools/pine/isidore_ifvg.pine` (v0.4), checked trade for
trade against TradingView's Strategy Tester (journal/backtests/2026-11-18-deep.md). The v0.5 lab filters
(`Config`: `min_sweeps`, `eng_mode`, `mom_mode`, `push_filter`, `fuel_target`, `skip_two_sided`,
`one_false_move`, `max_trades`, `window`) match the inputs of `tools/pine/isidore_ifvg_lab.pine`.

```
python3 tools/backtest/izzy_bt.py data/ohlcv/MNQ1_5m.csv --list
python3 tools/backtest/izzy_bt.py data/ohlcv/MNQ1_1m.csv --tf 2      # 2m from 1m
```

Data: CSV `t,o,h,l,c,v` (unix seconds UTC, bar open). Pull it with the TradingView connector's
`get-ohlcv` (columns format); the connector saves large results to a file, convert with a few lines of
Python. `data/` is git-ignored.

**Depth:** the connector's OHLCV holds only ~5½ days of 1m and ~4 weeks of 5m. For real sample size, use
the lab script with `run-pine-backtest` and `date_from` (Deep Backtesting, 1m back to 2025-01-01 at least).
Use Python for fast iteration and per-signal analysis; use Deep Backtesting for verdicts.
Limit: TradingView runs 2 backtests at a time per user, and there is a daily tool-call quota.
