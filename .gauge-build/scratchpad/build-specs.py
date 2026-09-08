#!/usr/bin/env python3
"""Turn manifest-1/2/3.md into per-page spec files + an index for the writing workflow.

Manifest format (per registry-prompt.md):
  ## Gauge Theory N — <Title>            (folder: Gauge Theory N/)
  ...
  ### §N.K <Section Title>
  - `Def - X` — type: definition; source items: ...; prereqs: [...]; spec: ...
  - `Thm - Y` — type: theorem; ...; statement: ...; proof: ...; spec: ...
  - `Ex - Z` — type: exercise; difficulty: ⭐⭐; ...
  - `Exercise Index - §N.K <Title>` — lists: [...]
A bullet may continue over following indented / non-bullet lines until the next bullet or header.
"""
import json, os, re, sys, hashlib
S = "/tmp/claude-0/-home-user-Study-notes/a00e52f1-c9a2-537c-a39b-06f8e3c8a9c6/scratchpad"
OUT = f"{S}/specs"; os.makedirs(OUT, exist_ok=True)
ROMAN = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10,"XI":11,"XII":12,"XIII":13}
chap_re = re.compile(r"^##\s+(Gauge Theory ([IVX]+) — .+?)\s*(?:\(folder:.*\))?\s*$")
sec_re  = re.compile(r"^###\s+(§(\d+)\.(\d+)\s+.+?)\s*$")
item_re = re.compile(r"^\s*[-*]\s+`((?:Def|Thm|Ex|Exercise Index|Gauge Theory) - ?[^`]*|Gauge Theory[^`]*)`\s*—?\s*(.*)$")
pages = []; chapter=None; chapnum=None; section=None; secid=None; cur=None; chap_pre=[]
def flush():
    global cur
    if cur: pages.append(cur); cur=None
for mf in sorted(f for f in os.listdir(S) if re.fullmatch(r"manifest-\d\.md", f)):
    for raw in open(f"{S}/{mf}", encoding="utf-8"):
        line = raw.rstrip("\n")
        m = chap_re.match(line)
        if m:
            flush(); chapter=m.group(1).strip(); chapnum=ROMAN.get(m.group(2)); section=None; secid=None; chap_pre=[]; continue
        m = sec_re.match(line)
        if m:
            flush(); section=m.group(1).strip(); secid=f"{m.group(2)}.{m.group(3)}"; continue
        if line.startswith("## ") or line.startswith("# "):
            flush(); continue
        m = item_re.match(line)
        if m and chapter:
            flush()
            name=m.group(1).strip()
            cur={"name":name,"chapter":chapter,"chapnum":chapnum,"section":section,"secid":secid,"rest":[m.group(2)]}
            continue
        if cur is not None:
            if line.strip()=="" and cur["rest"] and cur["rest"][-1].strip()=="":
                continue
            cur["rest"].append(line)
        elif chapter and not section:
            chap_pre.append(line)
    flush()
# classify + write
index=[]
for p in pages:
    name=p["name"]; body="\n".join(p["rest"]).strip()
    if name.startswith("Def - "): typ="definition"
    elif name.startswith("Thm - "): typ="theorem"
    elif name.startswith("Ex - "): typ="exercise"
    elif name.startswith("Exercise Index - "): typ="exercise-index"
    elif name.startswith("Gauge Theory"): typ="topic"
    else: typ="unknown"
    if re.search(r'[<>:"/\\|?*]', name): print("NON-PORTABLE NAME:", name)
    pid=hashlib.md5(name.encode()).hexdigest()[:8]
    diff=None
    md=re.search(r"difficulty:\s*(⭐+)", body)
    if md: diff=md.group(1)
    rec={"id":pid,"name":name,"type":typ,"chapter":p["chapter"],"chapnum":p["chapnum"],"section":p["section"],"secid":p["secid"],"difficulty":diff}
    index.append(rec)
    with open(f"{OUT}/{pid}.md","w",encoding="utf-8") as f:
        f.write(f"# PAGE SPEC\n\n- **Filename:** `{name}.md`\n- **Type:** {typ}\n- **Chapter:** {p['chapter']}  (folder `Gauge Theory {['','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII'][p['chapnum']]}/`)\n- **Section:** {p['section']}\n\n## Spec (from the manifest)\n\n{body}\n")
json.dump(index, open(f"{OUT}/index.json","w"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(index),"pages;", Counter(r["type"] for r in index)); print(Counter(r["chapnum"] for r in index))
dups=[n for n,c in Counter(r["name"] for r in index).items() if c>1]
print("DUPLICATE NAMES:", dups)
idx={l.split("\t")[0] for l in open(f"{S}/vault-index.txt") if "\t" in l}
print("COLLIDE WITH EXISTING VAULT PAGES:", [r["name"] for r in index if r["name"] in idx])
