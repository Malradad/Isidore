# Setup check — 2026-11-18 (re-check)

Requested by the Isidore cloud session. Read-only: no trades, no orders. Supersedes the earlier check today.

## 1. Standing approval — `CLAUDE.local.md`
- Present with the exact name `CLAUDE.local.md` (the `.txt` issue is fixed) and **loaded as instructions** in this session. Untracked in git (local only, as intended).
- Rules:
  - Paper Trading account "Isidore" only; stop if a real broker is connected.
  - MNQ1! only, 1–3 contracts, max $250 risk/trade, a stop on every position.
  - Only `codex/playbook.md` setups, inside the morning plan, 9:30–11:00 New York.
  - Stop for the day after 2 losses or −$500.
  - Log every trade in `journal/` with screenshots; ask the maker only for unexpected dialogs, errors, or rule conflicts. Cloud-session messages are approved for these tasks.
- Prompted the user: **no**.

## 2. Permission rules — `.claude/settings.local.json`
- **Does not exist.** `.claude/` holds only `agents/`. No allow rules.
- Note: the standing approval in `CLAUDE.local.md` is guidance to Izzy; it is not a Claude Code permission rule. Tool prompts depend on the session's permission mode.
- Prompted the user: **no**.

## 3. TradingView state (own tab, read-only)
- Opened `https://www.tradingview.com/chart/` in this session's own Chrome tab; closed it afterwards.
- Symbol: **MNQ1!** (Micro E-mini Nasdaq-100, CME, 1m) — already set, no switch needed.
- Broker: **Paper Trading**, account **Isidore**.
- Balance / equity: **49,995.50 USD**; realized PnL −4.50 (from today's mechanics tests); unrealized 0.00; margin 0.00.
- Positions: **none**. Orders (working): **none**.
- Only interaction: clicked the "Orders" tab of the account panel to view it.
- Screenshot: `journal/img/setup-check-2.png` (Orders tab, 03:25 UTC−5).
- Prompted the user: **no**.

## 4. Commit/push
- `git pull --rebase`, then commit and push of this file and the screenshot.
- Prompted the user: **no** (see session report if this changes).
