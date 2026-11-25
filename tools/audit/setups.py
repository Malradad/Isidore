"""Parse codex/teacher-audit.md (Takes (A) + Skips) into audited NQ setups inside the 1m history (>= 2023-11-20)."""
import re, json, sys
src = open(sys.argv[1] if len(sys.argv) > 1 else 'codex/teacher-audit.md').read()
def section(name):
    m = re.search(r'## ' + re.escape(name) + r'.*?\n(.*?)(\n## |\Z)', src, re.S)
    return [l for l in m.group(1).split('\n') if l.startswith('| 20')]
def grade_of(txt):
    t = txt.lower()
    if 'invalid' in t: return 'invalid'
    if 'pattern' in t: return 'pattern'
    if re.search(r'a\+|a plus', t): return 'A+'
    if re.search(r'a−|a minus|a-\b', t): return 'A-'
    if re.search(r'\bb−|b-minus|\bb setup|"a b|rated b|a b\b|\bb\b setup', t): return 'B'
    if 'light bulb' in t: return 'light bulb'
    if re.search(r'"a"|"a setup"|an a setup|a setup"', t): return 'A'
    return ''
out = []
for kind, rows in (('TAKE', section('Takes — (A) playbook')), ('SKIP', section('Skips'))):
    for l in rows:
        c = [x.strip() for x in l.strip('|').split('|')]
        date = c[0][:10]
        if date < '2023-11-20': continue
        m = re.search(r'(\d{1,2}):(\d\d)(?::(\d\d))?', c[1])
        if not m: continue
        side = c[3] if kind == 'TAKE' else c[3]
        if side not in ('L', 'S'): continue   # drops ES/YM/gold/unknown
        hh, mm, ss = int(m.group(1)), int(m.group(2)), int(m.group(3) or 0)
        ctx = ' '.join(c[4:])
        out.append(dict(kind=kind, date=date, t=f'{hh:02d}:{mm:02d}:{ss:02d}', tf=c[2], side=side,
                        grade=grade_of(ctx), text=ctx[:160]))
json.dump(out, sys.stdout, indent=0)
