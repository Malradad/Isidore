# Decision dataset — learning his selection and feel (started 2026-11-24)

Maker's call (2026-11-23): his strategy is an entry confluence; the edge is **selection and feel**. So Izzy learns from
his real decisions, not from more rules.

## Files
- `inputs.csv` — one row per on-stream TAKE or SKIP (215, all 37 streams): id, date, market time, side, symbol, tf,
  frames from **at or before** the decision. Nothing after it. This is all a blind labeler may see.
- `outcomes.csv` — his call (TAKE/SKIP), levels, result, his words. **Hidden from the blind labeler.** Joined after.
- `source/streams/decision-frames/<id>/` — Audrey's pre-decision strip: the chart at −60, −30, −15, −5 and 0 s.
- `labels-blind.csv` — the blind labeler's read of each decision (below).
- Built by `tools/decisions/build_index.py` (re-run when Audrey adds logs).

## Protocol
1. **Blind read** (a fresh Izzy session that has never seen the audit or the outcomes): for each id, from the frames
   only, answer the seven context questions (`codex/context.md`), his closure score and feel (`codex/feel.md`), and
   make a call: TAKE / SKIP, with confidence 1–5 and one sentence why.
2. **Join and score:** blind call vs his call vs outcome. Where does Izzy agree with him? Where he took and lost,
   did Izzy see it? Where he skipped a winner, did Izzy?
3. **Learn:** each disagreement becomes a written lesson in `codex/feel.md` / `codex/context.md`, cited by id.
4. **Shadow live** (later): Izzy calls TAKE/SKIP in real time on his stream days; Audrey logs his call.

## Rules
- No outcome leaks into the blind read: no trades.md, teacher-audit, claims, evolution-log, journal/labels, portrait.
- Frames after the decision never go in `inputs.csv` or `decision-frames/`.
- Every lesson cites a decision id.
