# Izzy alert waiter

Izzy sleeps until TradingView sends an alert. No polling, no Claude usage while waiting.

```
TradingView alert ──webhook──▶ ntfy.sh/<secret topic> ──stream──▶ wait-alert.ps1 (background, on the PC)
                                                                       │ exits with the alert JSON
                                                                       ▼
                                                              Claude (Izzy) wakes up
```

## One-time setup (PC)
1. `powershell -NoProfile -File tools\waiter\new-topic.ps1` → prints the webhook URL. The topic is
   stored in `tools\waiter\.topic` (git-ignored). Treat it like a password: anyone who knows it can
   read or send alerts.
2. TradingView: two-factor authentication must be on to use webhooks.
3. For each timeframe (30S, 1, 2, 3, 5): Create alert → Izzy iFVG v0.4 → "alert() function calls only"
   → open-ended → Notifications: **Webhook URL** = the printed URL (+ app/popup) → "Izzy setups <tf>".

## Loop (what Izzy does)
1. Start `wait-alert.ps1` as a **background** command.
2. When it exits, read the JSON:
   - **ARMED** (~45 s before close): screenshot the chart, run the four questions (target/fuel,
     location, confirmation, risk), check rules, and **pre-stage the ticket** (side, qty, SL/TP ticks).
     Decide TAKE or SKIP now; write the reason.
   - **CONFIRMED**: if TAKE and rules still pass → click Buy/Sell once on the staged ticket, then set
     SL/TP to the exact alert prices. If no ARMED came first, judge it now (faster, same checklist).
   - **CANCELLED**: clear the staged ticket; log "cancelled".
3. Journal every alert (taken or skipped, with reason). Commit and push.
4. Start the waiter again.

## Alert JSON
`{"izzy":"ARMED|CONFIRMED|CANCELLED","side":"LONG","grade":"A","score":4,"symbol":"MNQ1!","tf":"2",
"entry":…,"stop":…,"target":…,"qty":2,"risk_pts":…,"risk_usd":…,"stop_mode":"Swing","gap_edge":…,
"sweep":true,"strong_vol":false,"engineered_target":true,"momentum":true,"push_ok":true,
"bar_close":"…","sent":"…"}`
