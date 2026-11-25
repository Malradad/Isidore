"""P9: match grader audit-mode fires (TradingView trade lists, version 6.0) to his audited setups; score each fix."""
import json, glob, sys, datetime as dt
from zoneinfo import ZoneInfo
NY = ZoneInfo('America/New_York')
fires = {}
for f in glob.glob(sys.argv[1]):
    for line in open(f):
        try: d = json.loads(line)
        except Exception: continue
        msg = d.get('message'); c = msg.get('content') if isinstance(msg, dict) else None
        if not isinstance(c, list): continue
        for p in c:
            if p.get('type') != 'tool_result': continue
            cc = p.get('content'); texts = [cc] if isinstance(cc, str) else [x.get('text', '') for x in (cc or []) if isinstance(x, dict)]
            for t in texts:
                if '"version":"6.0"' in t and '"audit"' in t:
                    for tr in json.loads(t)['report']['trades']:
                        fires[tr['entry']['t']] = tr['entry']['comment']
F = []
for t, cm in sorted(fires.items()):
    c = cm.split('|'); kv = {x[0]: x[1:] for x in c[2:]}
    F.append(dict(t=dt.datetime.fromtimestamp(t, NY), side=c[0], grade=c[1], score=int(kv['k']), loc=int(kv['l']) / 100,
                  sweep=kv['s'] == '1', chop=float(kv['h']), loc2=int(kv['m']) / 100, be=kv['b'] == '1', prot=kv['p'] == '1',
                  rev=int(kv['v']), leg=kv['n'] == '1', eng=kv['e'] == '1'))
setups = json.load(open('journal/backtests/2026-11-23-grader-check-setups.json'))
flags = {}
for l in open('journal/labels/2026-11-23-labeled-record.md'):
    if l.startswith('| ') and l[2:3].isdigit():
        c = [x.strip() for x in l.strip('|').split('|')]; flags[(c[1][:10], c[1][11:16])] = c[2]
rows = []
for s in setups:
    st = dt.datetime.fromisoformat(s['date'] + 'T' + s['t']).replace(tzinfo=NY)
    same = [f for f in F if f['side'] == s['side'] and abs((f['t'] - st).total_seconds()) <= 180]
    fl = flags.get((s['date'], s['t'][:5]), '')
    if s['kind'] == 'TAKE':
        good = not ('X' in fl or s['grade'] in ('B', 'A-', 'pattern', 'invalid'))
    else:
        good = s['grade'] in ('A+', 'A')
    rows.append(dict(s=s, his_good=good, f=min(same, key=lambda f: abs((f['t'] - st).total_seconds())) if same else None))
def grade(f, use_loc2):
    l = f['loc2'] if use_loc2 else f['loc']
    if f['chop'] >= 2.6: return 'B'
    if 0.4 <= l <= 0.6: return 'A-'
    if f['sweep'] and l < 0.4: return 'A+'
    if f['sweep'] or l < 0.4: return 'A'
    return 'C'
fixes = {
    'v3 grader (as is)': lambda f: True,
    '1 dealing range swept->opposite swing': None,
    '2 BE point before target': lambda f: f['be'],
    '3 no protected target': lambda f: not f['prot'],
    '4 reversal <= 6 candles': lambda f: f['rev'] <= 6,
    '5 same leg': lambda f: f['leg'],
    '6 engineered target': lambda f: f['eng'],
    '7 window 09:30-11:00': lambda f: dt.time(9, 30) <= f['t'].time() <= dt.time(11, 0),
}
fired = [r for r in rows if r['f']]
print(f"setups {len(rows)}, engine fired (same side, ±3 min) on {len(fired)}; his good {sum(r['his_good'] for r in rows)}")
print('| fix | engine "A" on fired | agree with him | his-good he/eng both A | his-bad engine A (false A) |')
for name, fn in fixes.items():
    agree = tp = fp = nA = 0
    for r in fired:
        f = r['f']; g = grade(f, name.startswith('1'))
        eA = g in ('A+', 'A') and (fn(f) if fn else True)
        nA += eA; agree += (eA == r['his_good']); tp += (eA and r['his_good']); fp += (eA and not r['his_good'])
    print(f"| {name} | {nA}/{len(fired)} | {agree}/{len(fired)} ({agree/len(fired):.0%}) | {tp}/{sum(r['his_good'] for r in fired)} | {fp}/{sum(not r['his_good'] for r in fired)} |")
print()
combos = {'window': ['7'], 'window+rev6': ['7', '4'], 'window+leg': ['7', '5'], 'window+rev6+leg': ['7', '4', '5'],
          'window+eng': ['7', '6'], 'window+leg+eng': ['7', '5', '6']}
fx = {k.split()[0]: v for k, v in fixes.items() if v}
G = sum(r['his_good'] for r in fired); B = len(fired) - G
print('| combo | his-A kept (TPR) | his-below-A passed (FPR) | engine A |')
for name, ks in combos.items():
    tp = fp = 0
    for r in fired:
        f = r['f']; eA = grade(f, False) in ('A+', 'A') and all(fx[k](f) for k in ks)
        tp += eA and r['his_good']; fp += eA and not r['his_good']
    print(f'| {name} | {tp}/{G} ({tp/G:.0%}) | {fp}/{B} ({fp/B:.0%}) | {tp+fp} |')
print()
print('coverage by his timeframe (takes+skips, engine fired same side):')
from collections import defaultdict
cov = defaultdict(lambda: [0, 0])
for r in rows:
    tf = r['s']['tf'].split('/')[0].split(' ')[0]
    cov[tf][0] += 1; cov[tf][1] += bool(r['f'])
for tf, (n, k) in sorted(cov.items(), key=lambda x: -x[1][0]): print(f'  {tf}: {k}/{n}')
