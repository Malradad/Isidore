"""Round 3 split by stream: training streams (outcomes shown) vs test streams (blind)."""
import csv, os
TRAIN = ['JUDH0MmuhQs', 'YKRoRbq1BTU', 'j0tG6Mj-ds4', 'yVWktthvtJQ', 'chlCV294CTk', 'JrAXEtFejNw', 'YTBcXcI70io', 'nE8GE9YBd8k']
inp = list(csv.DictReader(open('journal/decisions/inputs.csv', encoding='utf-8')))
oc = {r['id']: r for r in csv.DictReader(open('journal/decisions/outcomes.csv', encoding='utf-8'))}
vid = lambda i: i.split('_', 1)[1].rsplit('_', 1)[0]
tr = [r for r in inp if vid(r['id']) in TRAIN]; te = [r for r in inp if vid(r['id']) not in TRAIN]
os.makedirs('journal/decisions/training', exist_ok=True)
with open('journal/decisions/training/training.md', 'w', encoding='utf-8') as f:
    f.write("# Round 3 training set — his decisions WITH outcomes (8 streams)\n\nStudy these: the frames "
            "(source/streams/decision-frames/<id>/), the context pack (journal/decisions/context/<id>.txt), then his call, "
            "his words and what happened. Learn what separates his good takes from his traps and his right skips from missed winners.\n"
            "Audit flags (codex/teacher-audit.md classification): D 2nd+ trade/after done · F flagged day · X graded <A/invalid · "
            "T outside window · B against bias · P audience.\n\n")
    for r in tr:
        o = oc[r['id']]
        f.write(f"## {r['id']} — {r['date']} {r['market_time']} {r['side']} {r['symbol']} {r['tf']}\n"
                f"- **his call:** {o['call']} · entry {o['entry']} · stop {o['stop']} · target {o['target']}\n"
                f"- **result:** {o['result']}\n- **his words:** {o['his_words']}\n\n")
with open('journal/decisions/training/test-ids.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(te[0])); w.writeheader(); w.writerows(te)
print('train', len(tr), 'test', len(te))
