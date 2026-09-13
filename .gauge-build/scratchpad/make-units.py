#!/usr/bin/env python3
"""Partition specs/index.json into work units for the write/review workflows.

A unit is a list of subpages (Def/Thm/Ex) from ONE chapter, in manifest (dependency) order,
of at most MAX pages, never splitting inside a section when avoidable. Topic pages and exercise
indices are excluded (they are written by the assembly step).
Writes units.json: [{unit, chapnum, pages:[{id,name,type,chapnum,section,secid,difficulty}]}]
and chapters.json: [{chapnum, title, manifestFile, topicId, indexIds}]
"""
import json, sys
S = "/tmp/claude-0/-home-user-Study-notes/a00e52f1-c9a2-537c-a39b-06f8e3c8a9c6/scratchpad"
MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 12
ONLY = set(int(x) for x in sys.argv[2].split(",")) if len(sys.argv) > 2 else None
SIGN_PAGES = ["Def - The Hopf Bundle", "Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds", "Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree", "Thm - Gauge Variation of the Chern-Simons Functional"]
SIGN_NOTE = "These four pages share one sign ledger. Read the section 'Orientation and sign ledger' of conventions.md. Write Def - The Hopf Bundle first, computing every sign under the fixed orientation conventions and recording them in its # Sign ledger section; then write the three theorem pages consistently with that ledger, wikilinking the ledger rather than re-deriving the signs."
ROMAN = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII']
index = json.load(open(f"{S}/specs/index.json"))
chapters = {}
for r in index:
    c = chapters.setdefault(r["chapnum"], {"chapnum": r["chapnum"], "title": r["chapter"], "manifestFile": f"manifest-{1 if r['chapnum']<=6 else (2 if r['chapnum']<=11 else 3)}.md", "topicId": None, "indexIds": [], "subpages": []})
    if r["type"] == "topic": c["topicId"] = r["id"]
    elif r["type"] == "exercise-index": c["indexIds"].append(r["id"])
    elif r["type"] in ("definition", "theorem", "exercise"): c["subpages"].append(r)
    else: print("UNKNOWN TYPE:", r["name"])
units = []
sign_jobs = [r for cn in chapters for r in chapters[cn]["subpages"] if r["name"] in SIGN_PAGES]
for cn in sorted(chapters):
    if ONLY and cn not in ONLY: continue
    c = chapters[cn]
    c["subpages"] = [r for r in c["subpages"] if r["name"] not in SIGN_PAGES]
    # group by section, then pack sections greedily into units of <= MAX pages
    by_sec = []
    for r in c["subpages"]:
        if by_sec and by_sec[-1][0] == r["secid"]: by_sec[-1][1].append(r)
        else: by_sec.append((r["secid"], [r]))
    cur = []
    k = 1
    def tojobs(rows):
        jobs=[]; i=0
        while i < len(rows):
            r=rows[i]
            if r["type"]=="exercise" and i+1 < len(rows) and rows[i+1]["type"]=="exercise" and rows[i+1]["secid"]==r["secid"]:
                jobs.append({"pages":[r, rows[i+1]]}); i+=2
            else:
                jobs.append({"pages":[r]}); i+=1
        return jobs
    def flush():
        global cur, k
        if cur:
            units.append({"unit": f"{ROMAN[cn]}-{k}", "chapnum": cn, "jobs": tojobs(cur)}); k += 1; cur = []
    for secid, rows in by_sec:
        if len(rows) > MAX:            # a huge section: split it
            flush()
            for i in range(0, len(rows), MAX):
                cur = rows[i:i+MAX]; flush()
            continue
        if len(cur) + len(rows) > MAX: flush()
        cur += rows
    flush()
if sign_jobs and (not ONLY or any(r["chapnum"] in ONLY for r in sign_jobs)):
    order={n:i for i,n in enumerate(SIGN_PAGES)}
    sign_jobs.sort(key=lambda r: order[r["name"]])
    units.append({"unit": "SIGNS", "chapnum": 3, "jobs": [{"pages": sign_jobs, "note": SIGN_NOTE}]})
json.dump(units, open(f"{S}/units.json", "w"), ensure_ascii=False, indent=1)
json.dump([{k: v for k, v in c.items() if k != "subpages"} for c in chapters.values()], open(f"{S}/chapters.json", "w"), ensure_ascii=False, indent=1)
tot = sum(len(j["pages"]) for u in units for j in u["jobs"]); nj = sum(len(u["jobs"]) for u in units)
print(f"{len(units)} units, {nj} jobs, {tot} subpages; per chapter:", {ROMAN[cn]: len(chapters[cn]['subpages']) for cn in sorted(chapters) if not ONLY or cn in ONLY})
for u in units: print(f"  {u['unit']:8s} {len(u['jobs']):3d} jobs {sum(len(j['pages']) for j in u['jobs']):3d} pages  sections {sorted(set(p['secid'] for j in u['jobs'] for p in j['pages']))}")
