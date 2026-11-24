import csv, sys, re, collections
lb = {r['id']: r for r in csv.DictReader(open(sys.argv[1], encoding='utf-8'))}
oc = {r['id']: r for r in csv.DictReader(open(sys.argv[2], encoding='utf-8'))}
def take_res(t):
    t = t.lower()
    if re.search(r'not filled|no trigger|\?$|^$|see row', t): return '?'
    if re.search(r'stop|loss|−\$|-\$|cut|blown|wrecked|cooked', t) and not re.search(r'stopped? (at )?(be|break)', t): return 'L'
    if re.search(r'\bbe\b|break ?even|scratch|0 \(', t) and not re.search(r'tp|\+', t): return 'BE'
    if re.search(r'tp|win|\+|profit|green|printed|passed', t): return 'W'
    if re.search(r'\bbe\b|break ?even', t): return 'BE'
    return '?'
def skip_res(t):
    t = t.lower()
    if re.search(r'worked|hit target|ran|bounced|printed|cost a winner|would have won|tp', t): return 'missed-W'
    if re.search(r'right|failed|wrecked|no trigger|saved|stopped|be\b|break ?even|fell|loss', t): return 'right'
    return '?'
rows = []
for i, o in oc.items():
    l = lb.get(i)
    if not l: continue
    call = l['izzy_call'].strip().upper()[:4]
    res = take_res(o['result']) if o['call'] == 'TAKE' else skip_res(o['result'])
    try: conf = int(l['confidence'])
    except: conf = None
    rows.append((i, o['call'], call, res, conf, l.get('notes', ''), l.get('closure_total_10', '')))
n = len(rows)
agree = sum(r[1] == r[2] for r in rows)
print(f"labeled {n}; izzy calls TAKE {sum(r[2]=='TAKE' for r in rows)} / SKIP {sum(r[2]=='SKIP' for r in rows)}; agree with him {agree} ({100*agree/n:.0f}%)")
cm = collections.Counter((r[1], r[2]) for r in rows); print("his→izzy:", dict(cm))
print("\nHIS TAKES by izzy call (result W/BE/L/?):")
for c in ('TAKE', 'SKIP'):
    k = collections.Counter(r[3] for r in rows if r[1] == 'TAKE' and r[2] == c); print(f"  izzy {c}: {dict(k)}")
print("\nHIS SKIPS by izzy call (missed-W / right / ?):")
for c in ('TAKE', 'SKIP'):
    k = collections.Counter(r[3] for r in rows if r[1] == 'SKIP' and r[2] == c); print(f"  izzy {c}: {dict(k)}")
print("\nHIS TAKES, izzy TAKE by confidence:")
for cf in range(1, 6):
    k = collections.Counter(r[3] for r in rows if r[1] == 'TAKE' and r[2] == 'TAKE' and r[4] == cf)
    if k: print(f"  conf {cf}: {dict(k)}")
cont = [r[0] for r in rows if 'contaminat' in (r[5] or '').lower()]; print("\ncontaminated:", len(cont))
w = csv.writer(open(sys.argv[3], 'w', newline='')); w.writerow(['id','his_call','izzy_call','result','conf','closure'])
for r in rows: w.writerow([r[0], r[1], r[2], r[3], r[4], r[6]])
