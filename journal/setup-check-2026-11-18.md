# Setup check — 2026-11-18

Requested by the Isidore cloud session. Read-only check: no trades, no orders, no clicks.

## 1. Standing approval
- Found, but as `CLAUDE.local.md.txt` (untracked). The `.txt` extension means Claude Code does **not** load it as instructions; it was read as a file only. Rename to `CLAUDE.local.md` if it should load.
- Rules, if the maker confirms it:
  - Paper Trading account "Isidore" only; stop if a real broker is connected.
  - MNQ1! only, 1–3 contracts, max $250 risk/trade, stop on every position.
  - Playbook setups only, inside the morning plan, 9:30–11:00 New York.
  - Stop for the day after 2 losses or −$500.
  - Log every trade in `journal/` with screenshots; ask the maker only for unexpected dialogs, errors, or rule conflicts.

## 2. Permission rules
- `.claude/settings.local.json` does not exist. `.claude/` holds only `agents/`.
- Global `~/.claude/settings.json` has no permission rules (only `autoUpdatesChannel`, `theme`).
- So: no allow rules for Claude in Chrome or git.

## 3. TradingView state
- **Not confirmed.** This session's Chrome tab group was empty (one new tab created, `chrome://newtab/`). Tabs opened by other sessions or the maker are not visible to it, so the TradingView tab, the "Isidore" Paper Trading broker, and open positions/orders could not be checked.
- Did not open TradingView in a new tab to avoid a second live chart/broker session without the maker's say.

## 4. Commit/push
- See the session report for whether any step prompted.
