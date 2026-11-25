# Round 3 lessons: what separates his good calls from his bad ones (2026-11-25) ~

Source: the 61 training decisions in `training.md` (8 streams), their context packs and pre-decision frames,
read against `codex/context.md`, `feel.md`, `playbook.md` (video batches 1–3), `reasoning.md`, `markets.md`,
`risk.md`. Many training rows end "see row N", so the result is known for about half. Every lesson cites ids.
All of this is `~`, Izzy's reading, until the blind test is scored.

## 1. His own words grade the trade before price does
His label at entry predicts the result better than the chart does.
- **Takes he talks down lost or went BE.** "Warm-up… degen play… one contract" (2023-04-21_1, −$200);
  "I'm just degen-ing" (2023-04-21_2, −$200); "just a B setup… no break even for this play… like 50%"
  (2025-01-22_8, stopped); "I don't even like this retrace" (2025-01-22_9, loss/BE); "on paper so you guys watch
  me execute" (2026-03-06_4, BE); "chat voted" (2026-03-06_5, +3R round-tripped to BE); "a micro here for fun"
  (2026-07-14_7, stopped); "B setup… half size… probably will not work" (2026-07-14_5, lost, `context.md`);
  "just because the indicator alerted it" (2025-10-15 showcase, 2025-10-15_3 lost, `context.md`).
- **Takes he backs win.** 2026-03-06_2 (09:34, bearish bias, "that's a little faster candle… there's the entry",
  +1R, then "done for the day"). 2023-04-21_3 (10:18, "if we get the FVG right here I'll take this long", equal
  highs above, +10 pts and the draw was hit). 2026-10-02_9 (09:42, his "only trade of the day", after waiting
  three candles for the close).
- **Rule:** words like eval only, B, degen, warm-up, for fun, paper, one micro, chat voted, educational,
  horrible trade = SKIP for Izzy, even when he clicks. Words like A/A+, live account, only trade of the day,
  "my bread and butter", bias + discount + "we just hit my zone" = the candidate.

## 2. Judge the day first
- **News-day straddles are a gamble, not the playbook.** 2026-07-14_1 and 2026-09-04_1 worked, 2026-03-06_1
  "bottom ticked" and failed. He says "it is a gamble, 100%". Izzy doesn't take the straddle; Bot can't place
  it inside risk.md anyway. Call SKIP and note "news gamble".
- **News days: 08:30–09:30 is a killzone.** The first clean move after the release, with bias, is tradable
  (2026-09-04_3, 08:44 short with bearish bias and sellside below). Not "pre-open".
- **Bad-tape days:** when he says search-and-destroy, "price action is bad", or reaches for Bitcoin on the 1m
  (2023-04-21_1/2, 2025-01-22_7), take nothing, or at most the one clean A that appears later.
- **Indicator showcases and teaching streams** (2025-10-15) are not decisions. Whatever he clicks there is a
  demo. SKIP unless it is clearly an A on its own.
- **"Done" is final.** After he says he's done (2026-03-06_2 → 03-06_3/4/5; 2024-10-30_20 → 22/23) every later
  take is paper/eval/one micro and the results were BE or worse.

## 3. Time
- **09:30–10:00, the Judas swing, is where the A setups are.** 2026-03-06_2 (09:34), 2026-10-02_9 (09:42),
  and the missed winners 2026-07-14_2 (09:23), 2026-07-14_4 (09:37), 2026-09-04_9 (09:29) all sit in or at the
  edge of that window.
- **10:00–10:20 is the second chance** if the first window didn't trade: 2023-04-21_3 (10:18) won.
- **After ~10:30 the takes are mostly eval noise:** 2025-01-22_8/9/10 (11:00–11:15), 2026-03-06_5 (10:32),
  2026-07-14_7/9 (10:15–10:22), the 2024-10-30 eval string (10:56–11:43). Exceptions (2025-01-22_11 won at
  11:21; 2023-04-21_4 +5 pts at the 10:50 macro) were small and on eval. Late = SKIP unless nothing traded
  earlier and it is clearly A.

## 4. The sweep, the location, the draw
- **The good longs come off a swept low into discount / the 0.5**: 2026-10-02_9 (swept sellside, tapped the
  50%), 2026-07-14_2 ("reaction at the point five… CISD"), 2026-07-14_4 ("in discount, delivering off a FVG,
  swept liquidity").
- **Premium entries are skips** for him (2026-10-02_5 "I never long way up here"), but 2026-10-02_6 (an eval
  long "too high" to the buyside) worked. A short-hop to an obvious draw can work; it's still not his A.
- **The draw decides.** Equal highs, buyside, data highs = good. A protected high is a B at best
  (2024-10-30_12/13). A data high above = no shorts (2024-10-30_1, 2026-09-04_11). Equal lows below a long break
  his rule (2025-01-22_3/4).
- **No BE point = no trade** (2026-10-02_7 skipped; 2025-01-22_8 had "no break even for this play" and lost).
- **RR < 1 = skip**, even if the target then hits (2026-10-02_13, RR 0.64): skipping a negative-R trade is
  right even when it works.

## 5. How the candle prints
- **Wait for the close.** 2026-10-02_8 (no close → skip) became 2026-10-02_9 (closed → take). 2024-10-30_4,
  _22, _23: no close, and the close "saved" him (price fell after _23).
- **A faster, decisive candle is the green light**: 2026-03-06_2 "a little faster candle"; 2025-01-22_9 lost
  after a slow retrace ("winning trades accelerate quicker").
- **But don't over-require the higher TF.** His missed winners were 30s/1m inversions skipped because the 3m/5m
  hadn't closed (2026-07-14_4, 2024-10-30_3/5, 2026-09-04_9/10). In his core window, with bias, a sweep and
  discount, a light-bulb close on the 30s/1m is enough.

## 6. Right skips vs missed winners
- **Right skips:** no close; after done; counter to a data-high draw; premium; RR < 1; no BE point.
- **Missed winners:** in-window, in-discount, post-sweep 30s/1m inversions he skipped for a technicality or
  inattention (2026-07-14_2/4, 2026-09-04_9, 2025-01-22_2/6). **This is where Izzy should be bolder than round 2**:
  when the day, bias, time, sweep and draw are all right and the candle closes, TAKE, even if he hesitates.

## 7. Izzy's order of judgment for the blind test
1. **Day:** news gamble / showcase / no-trade / bad tape / after done → SKIP.
2. **Bias and time:** with his stated bias, 08:30–09:30 on news days, 09:30–10:00 first, 10:00–10:20 second.
3. **Sweep and draw:** swept a named level, entry in discount (long) / premium (short), engineered draw, RR ≥ 1,
   BE point present.
4. **Candle:** closed, fast, decisive. No close → SKIP.
5. **Call:** the best 1–2 per stream day, first quality trade preferred. Not after a win, and never after "done".
