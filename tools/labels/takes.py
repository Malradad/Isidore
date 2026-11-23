# 48 audited playbook takes, in teacher-audit.md order. Flags coded ONLY from what he said/knew before entry.
# D = 2nd+ playbook trade of the day, or after "done" ; F = day he flagged (no-trade/bad PA/chop he named/gamble/demo-only/eval-only week)
# X = he graded it below A or called it invalid/pattern/degen/teaching/doubtful before entry ; T = outside window (after 11:00, or pre-open with no news release)
# B = against his bias or his equal-highs/lows rule ; P = for the audience (chat poll, indicator showcase, "for you guys")
T=[("2026-11-02 09:39","",'W',0.8),("2026-11-02 10:10","DX",'W',2.1),("2026-10-02 09:42","",'W',1.0),
("2026-09-11 08:38","",'W',None),("2026-09-29 09:31","F",'W',None),("2026-09-04 ~09:4x","",'BE',0),
("2026-09-04 10:14","D",'L',-1.15),("2026-09-04 08:44","X",'W',2.2),("2026-09-04 09:14","DX",'BE',0),
("2026-08-12 09:49","F",'BE',0),("2026-07-14 09:45","F",'L',-0.5),("2026-03-11 09:59","P",'W',0.3),
("2026-03-11 10:32","D",'BE',0),("2026-02-13 10:26","",'W',2.4),("2025-10-15 09:42","XP",'L',-0.5),
("2025-10-15 09:44","DXP",'L',-1),("2025-10-15 09:51","D",'W',2.9),("2025-10-09 pre-09:13","XT",'W',3.0),
("2025-10-09 10:49 gold","D",'BE',0),("2025-10-09 11:00","DT",'BE',0),("2025-01-22 10:06","FB",'BE',0),
("2025-01-22 10:57","DF",'L',-1),("2025-01-22 11:08","DFT",'L',-1),("2025-01-22 11:15","DFT",'BE',0),
("2025-01-22 ~11:21","DFT",'W',1),("2024-03-01 10:05","D",'W',1.5),("2023-09-06 08:49","T",'W',1.3),
("2023-09-05 09:12","T",'W',None),("2023-09-05 10:11","X",'L',-1),("2023-09-05 10:18","DF",'W',2),
("2023-02-24 pre-08:44","T",'W',None),("2023-02-24 10:12","F",'W',None),("2023-02-24 10:23","DF",'L',-1),
("2023-02-24 10:24","DFX",'BE',0),("2023-04-21 09:32","X",'L',-1),("2023-04-21 09:46","DX",'L',-1),
("2023-04-21 10:18","D",'W',None),("2023-04-21 10:51","D",'W',None),("2023-12-19 11:03","BT",'W',None),
("2023-12-19 11:26","DBTP",'L',-1),("2024-01-12 11:04","T",'W',1.5),("2026-03-06 09:34","",'W',1),
("2026-06-05 08:38","",'W',0.5),("2026-02-11 08:52","X",'BE',0),("2024-10-30 09:55","F",'W',0.7),
("2024-10-30 10:56","DXF",'L',-1),("2024-10-30 11:24","DTF",'W',0.9),("2023-03-14 ~10:47","X",'W',0.5)]
assert len(T)==48
def rec(rows):
    w=sum(r[2]=='W' for r in rows); b=sum(r[2]=='BE' for r in rows); l=sum(r[2]=='L' for r in rows)
    rs=[r[3] for r in rows if r[3] is not None]
    return f"{len(rows):>2} | {w}W/{b}BE/{l}L | win {100*w/len(rows):.0f}% | loss {100*l/len(rows):.0f}% | avgR {sum(rs)/len(rs):+.2f} (n={len(rs)})" if rows else "0"
print("ALL      ",rec(T))
print("CLEAN    ",rec([r for r in T if not r[1]]))
print("1 FLAG   ",rec([r for r in T if len(r[1])==1]))
print("2+ FLAGS ",rec([r for r in T if len(r[1])>=2]))
for f in "DFXTBP": print(f"has {f}    ",rec([r for r in T if f in r[1]]))
print("first trade of day, no F/X",rec([r for r in T if 'D' not in r[1] and 'F' not in r[1] and 'X' not in r[1]]))
print("first trade of day       ",rec([r for r in T if 'D' not in r[1]]))
print("not first                ",rec([r for r in T if 'D' in r[1]]))
for r in T: print(r)
