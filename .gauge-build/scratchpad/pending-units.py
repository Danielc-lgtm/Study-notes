#!/usr/bin/env python3
"""Emit per-chapter workflow args for only the jobs whose pages are not yet on disk.

Reads units.json (chapters III-XIII + SIGNS) and scans the vault; for each unit,
keeps a job iff at least one of its pages is missing. Writes chapargs-pending/<C>.json
as {"units":[{"unit","jobs":[<slim jobs>]}]}, ready to paste into Workflow args.

Robust to container reclamation: it relies only on files on disk, not the workflow cache.
Run from either the live scratchpad or .gauge-build/scratchpad (VAULT is absolute).
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = "/home/user/Study-notes/Study notes/Geometry/Gauge Theory"
ROMAN = ['', 'I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII']
units = json.load(open(f"{HERE}/units.json"))
def chap(u): return 'SIGNS' if u['unit'] == 'SIGNS' else u['unit'].rsplit('-', 1)[0]
def exists(p): return os.path.exists(f"{VAULT}/Gauge Theory {ROMAN[p['chapnum']]}/{p['name']}.md")
def slim_job(j):
    o = {'pages': [{'id': p['id'], 'name': p['name'], 'type': p['type'], 'chapnum': p['chapnum']} for p in j['pages']]}
    if j.get('note'): o['note'] = j['note']
    return o
groups, stats = {}, {}
for u in units:
    pend = [j for j in u['jobs'] if not all(exists(p) for p in j['pages'])]
    done = len(u['jobs']) - len(pend)
    stats[u['unit']] = (done, len(u['jobs']))
    if pend:
        groups.setdefault(chap(u), []).append({'unit': u['unit'], 'jobs': [slim_job(j) for j in pend]})
os.makedirs(f"{HERE}/chapargs-pending", exist_ok=True)
# clear stale
for f in os.listdir(f"{HERE}/chapargs-pending"):
    os.remove(f"{HERE}/chapargs-pending/{f}")
for c, us in groups.items():
    json.dump({'units': us}, open(f"{HERE}/chapargs-pending/{c}.json", 'w'), ensure_ascii=False, separators=(',', ':'))
tot_pages = sum(len(j['pages']) for us in groups.values() for u in us for j in u['jobs'])
print("Pending per chapter (file bytes):")
for c in sorted(groups, key=lambda x: (len(x), x)):
    nj = sum(len(u['jobs']) for u in groups[c]); np = sum(len(j['pages']) for u in groups[c] for j in u['jobs'])
    print(f"  {c:6s} {nj:3d} jobs {np:3d} pages  {os.path.getsize(f'{HERE}/chapargs-pending/{c}.json')} bytes  units={[u['unit'] for u in groups[c]]}")
print(f"TOTAL pending: {tot_pages} pages across {len(groups)} chapters")
print("Per-unit (done/total):", {k: f"{d}/{t}" for k, (d, t) in stats.items() if d < t})
