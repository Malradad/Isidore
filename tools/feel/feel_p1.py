import json,datetime as dt,itertools
D=json.load(open(__import__('sys').argv[1]))  # trade lists from run-pine-backtest, keyed by range start
rows=[]
for k,tr in D.items():
    for t in tr:
        c=t['entry']['comment'].split('|')
        r={'side':c[0],'pnl':t['profit'],'t':t['entry']['t'],'qty':t['qty']}
        for f in c[1:]:
            key='rb' if f.startswith('rb') else 'rp' if f.startswith('rp') else f[0]; val=f[len(key):]
            r[key]=None if val in ('na','') else float(val)
        r['y']=dt.datetime.utcfromtimestamp(r['t']).year
        rows.append(r)
rows.sort(key=lambda r:r['t'])
# normalise pnl per contract to remove sizing noise? keep $ as traded; also R-ish: pnl/qty
for r in rows: r['pc']=r['pnl']/r['qty']
def st(s,key='pnl'):
    g=sum(r[key] for r in s if r[key]>0); l=-sum(r[key] for r in s if r[key]<0)
    n=len(s); w=sum(r[key]>0 for r in s)
    return n, (w/n*100 if n else 0), (g/l if l else float('inf')), sum(r[key] for r in s)
def fmt(s):
    n,w,pf,net=st(s); return f"n={n:3d} win={w:4.1f}% PF={pf:4.2f} net={net:8.0f}"
H1=[r for r in rows if r['y']<=2022]; H2=[r for r in rows if r['y']>=2023]
print('ALL',fmt(rows)); print('H1',fmt(H1)); print('H2',fmt(H2))
for y in range(2019,2027): print(y,fmt([r for r in rows if r['y']==y]))
feats=['b','c','v','h','rb','rp','p','x','f']
import statistics
print('\n== median buckets per feature (split at full-sample tertiles) ==')
for f in feats:
    vals=sorted(r[f] for r in rows if r.get(f) is not None)
    if len(set(vals))<4:
        cuts=sorted(set(vals))
    q=[vals[len(vals)//3],vals[2*len(vals)//3]]
    print(f'-- {f} tertile cuts {q}')
    for name,cond in [('low',lambda v:v<q[0]),('mid',lambda v:q[0]<=v<q[1]),('high',lambda v:v>=q[1])]:
        for hn,H in [('H1',H1),('H2',H2)]:
            s=[r for r in H if r.get(f) is not None and cond(r[f])]
            if s: print(f'   {name:4s} {hn} {fmt(s)}')

print('\n== candidates by year ==')
cands={'c<81':lambda r:r['c']<81,'c>=81':lambda r:r['c']>=81,
 'x>=4':lambda r:r['x'] is not None and r['x']>=4,'x<=3':lambda r:r['x'] is not None and r['x']<=3,
 'f>0':lambda r:r['f'] is not None and r['f']>0 and r['x'] is not None,'f=0':lambda r:r['f']==0 and r['x'] is not None,
 'v<1.03':lambda r:r['v']<1.03,'v>=1.03':lambda r:r['v']>=1.03,
 'h<1.96':lambda r:r['h']<1.96,'h>=2.54':lambda r:r['h']>=2.54,'b>=77':lambda r:r['b']>=77}
for n,cf in cands.items():
    print(n, ' | '.join(f"{y}:{st([r for r in rows if r['y']==y and cf(r)])[0]}/{st([r for r in rows if r['y']==y and cf(r)])[2]:.2f}" for y in range(2020,2027)))
X=[r for r in rows if r['x'] is not None]
print('\nx-era', fmt(X), 'first', dt.datetime.utcfromtimestamp(X[0]['t']))
for xv in range(1,6): print(' x=',xv,fmt([r for r in X if r['x']==xv]))
for a,b_ in [(2023,2024),(2025,2026)]:
    S=[r for r in X if a<=r['y']<=b_]
    print(a,b_,'x>=4',fmt([r for r in S if r['x']>=4]),'| x<=3',fmt([r for r in S if r['x']<=3]))
    print(a,b_,'f>0 ',fmt([r for r in S if r['f']>0]),'| f=0 ',fmt([r for r in S if r['f']==0]))
print('\nside', 'L',fmt([r for r in rows if r['side']=='L']),'S',fmt([r for r in rows if r['side']=='S']))

print('\n== combined feel score (x-era only): +1 late cross x>=4, +1 no flip, +1 vol>=1.03 ==')
for r in X: r['score']=(r['x']>=4)+(r['f']==0)+(r['v']>=1.03)
for a,b_ in [(2023,2024),(2025,2026),(2023,2026)]:
    S=[r for r in X if a<=r['y']<=b_]
    for sc in range(4): 
        s=[r for r in S if r['score']==sc]
        if s: print(a,b_,'score',sc,fmt(s))
    print(a,b_,'score=3',fmt([r for r in S if r['score']==3]),'| <3',fmt([r for r in S if r['score']<3]))
# per-contract check of x>=4 to rule out sizing artefact
for a,b_ in [(2023,2024),(2025,2026)]:
    S=[r for r in X if a<=r['y']<=b_]
    print('per-contract',a,b_,'x>=4',st([r for r in S if r['x']>=4],'pc')[2],'x<=3',st([r for r in S if r['x']<=3],'pc')[2])
