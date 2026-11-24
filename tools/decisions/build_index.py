"""Build the decision dataset from Audrey's stream logs.
inputs.csv  = what a blind labeler may see (no result, no words, no frames after the decision)
outcomes.csv = his call, his words, result (kept apart; joined only after blind labeling)"""
import csv, os, re, glob, sys
root = sys.argv[1] if len(sys.argv) > 1 else '.'
S = os.path.join(root, 'source/streams')
def secs(t):
    m = re.match(r'~?\s*(\d+):(\d\d):(\d\d)', t.strip()); return None if not m else int(m[1])*3600+int(m[2])*60+int(m[3])
ins, outs = [], []
for f in sorted(glob.glob(os.path.join(S, '*.trades.md'))):
    name = os.path.basename(f)[:-10]; date, vid = name.split(' ', 1)
    lines = open(f, encoding='utf-8').read().splitlines()
    hdr = next((l for l in lines if l.startswith('| #')), None)
    if not hdr: continue
    cols = [c.strip().lower() for c in hdr.strip('|').split('|')]
    for l in lines:
        if not re.match(r'^\| *\d+ *\|', l): continue
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if len(cells) < len(cols): cells += [''] * (len(cols) - len(cells))
        r = dict(zip(cols, cells))
        ev = re.sub(r'[^A-Z].*', '', r.get('event', '').replace('~', '').strip().upper())
        if ev not in ('TAKE', 'SKIP'): continue
        st = r.get('stream time', ''); s = secs(st)
        did = f"{date}_{vid}_{r['#']}"
        fdir = os.path.join(S, 'frames', vid, st.replace('~', '').strip().replace(':', '-'))
        pre = []
        if s is not None and os.path.isdir(fdir):
            for fr in sorted(os.listdir(fdir)):
                fs = secs(fr.replace('-', ':').split('.')[0])
                if fs is not None and fs <= s: pre.append(os.path.relpath(os.path.join(fdir, fr), root))
        mt = r.get('market time (ny)', r.get('day (his words)', ''))
        ins.append(dict(id=did, date=date, market_time=mt, side=r.get('side', ''), symbol=r.get('symbol', ''),
                        tf=r.get('tf', ''), frames_pre=';'.join(pre)))
        outs.append(dict(id=did, call=ev, account=r.get('account', ''), entry=r.get('entry', ''), stop=r.get('stop', ''),
                         target=r.get('target', ''), result=r.get('result', ''), his_words=r.get('his words', '')))
os.makedirs(os.path.join(root, 'journal/decisions'), exist_ok=True)
for fn, rows in (('inputs.csv', ins), ('outcomes.csv', outs)):
    with open(os.path.join(root, 'journal/decisions', fn), 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
n = len(ins); withf = sum(1 for r in ins if r['frames_pre'])
print(f"decisions {n} (take {sum(o['call']=='TAKE' for o in outs)}, skip {sum(o['call']=='SKIP' for o in outs)}); with pre-decision frame {withf}")
