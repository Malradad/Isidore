"""Context pack per decision = what he knew: day type + his words from the stream start to 30 s before the decision
(first 8 min = his plan, plus the last 15 min). Nothing after. Written to journal/decisions/context/<id>.txt"""
import csv, os, re, glob, json, sys
root = sys.argv[1] if len(sys.argv) > 1 else '.'
S = os.path.join(root, 'source/streams'); out = os.path.join(root, 'journal/decisions/context'); os.makedirs(out, exist_ok=True)
def secs(t):
    m = re.search(r'(\d+):(\d\d):(\d\d)', t or ''); return None if not m else int(m[1])*3600+int(m[2])*60+int(m[3])
oc = list(csv.DictReader(open(os.path.join(root, 'journal/decisions/outcomes.csv'), encoding='utf-8')))
n = 0
for o in oc:
    date, rest = o['id'].split('_', 1); vid = rest.rsplit('_', 1)[0]
    base = f"{date} {vid}"; tx = os.path.join(S, base + '.txt'); meta = os.path.join(S, base + '.meta.json')
    title = ''
    if os.path.exists(meta):
        try: title = json.load(open(meta, encoding='utf-8')).get('title', '')
        except Exception: pass
    day = [k for k in ('CPI', 'NFP', 'FOMC', 'PPI', 'GDP', 'ISM') if k.lower() in title.lower()]
    d = secs(o['stream_time']); lines = []
    if d is not None and os.path.exists(tx):
        cut = d - 30
        for l in open(tx, encoding='utf-8', errors='ignore'):
            t = secs(l[:12])
            if t is None or t > cut: continue
            if t <= 480 or t >= cut - 900: lines.append(l.rstrip())
    with open(os.path.join(out, o['id'] + '.txt'), 'w', encoding='utf-8') as f:
        f.write(f"date: {date}\nday type (from stream title): {', '.join(day) or 'none named'}\n")
        f.write("his words, stream start → 30 s before the decision (first 8 min + last 15 min only):\n")
        f.write('\n'.join(lines) if lines else '(none available)'); f.write('\n')
    n += 1
print('context packs', n)
