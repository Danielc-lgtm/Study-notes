---
name: paper-notes
description: >
  Rewrite a finished research paper into a SELF-CONTAINED Obsidian note-set: a Map page plus one page per
  paper section, where each section page writes out every symbol, predicate, and imported result it uses as
  literal text, so a non-specialist reads it front-to-back — fast and rigorously — without ever leaving the
  page or matching jargon to its meaning. Types come first (signatures before prose, hypotheses as numbered
  symbolic propositions), but formalism is in service of comprehension: every unfamiliar term is expanded to
  its minimal symbolic reconstruction at point of use, no wikilink is ever load-bearing, and every proof is
  checkable above the fold. Use whenever the user points at a paper (in `paper_source/` or `sources/`) and
  asks for notes on it, a breakdown, a reading guide, or wants to "understand what every result is for" and be
  able to read the paper without chasing references. Trigger phrases: "make notes on this paper," "break down
  this paper," "self-contained notes for X," "make this paper readable without looking things up," "reading
  guide for X," "what does each theorem in X let me do." Distinct from polymath-notes (chapter-level study
  notes with exercises from textbooks) and prereq-backchain (plans what to study). This skill takes a *specific
  finished paper* and produces a note-set optimised for reading the whole paper on the reading surface alone,
  typechecking every step in place, and taking any import on blind faith with its precondition and conclusion
  stated exactly.
---

# Paper Notes — Self-Contained Edition

A specialisation of [`polymath-notes`](../polymath-notes/SKILL.md) and `prereq-backchain` for a single finished paper.

## The reader model

**Write for a strong mathematician who is *not* a specialist in the paper's fields, and who must be able to read your notes without looking anything up.**

They have graduate command of the anchor set (below) and nothing above it. They cannot resolve an English predicate — "acts freely", "regular Dirichlet form", "geometrically finite" — into a proposition. They will not accept a step whose hypothesis they cannot check. They *will* take a result on faith, provided its precondition and conclusion are both stated precisely enough to apply. And — the property this skill exists to guarantee — **they will not leave the page.** Every term is expanded where it is used; every import is stated where it is invoked; every proof is checkable in place.

The metaphor to hold: a non-specialist reading the paper would search up each unfamiliar term one by one, reducing jargon to the content it points at, until everything bottoms out at something they know. **Your job is to do all of that reduction in advance and lay it on the page, so none of that searching is ever necessary.** Three failure modes follow:

1. **An untyped symbol.** $p$ appears and the reader does not know its domain, codomain, or reference measure. Bug — put it in the section's signature table.
2. **An unexpanded predicate.** "$\Gamma$ acts freely", "the form is regular", "$P$ is polar". Each is a proposition the reader cannot expand. Write it symbolically, on the page, at point of use. **A bare jargon name in a statement is a bug.**
3. **An unstated import.** "by the Wang–Xue identity", "by the trace formula". Even a black box must carry its precondition and conclusion on the page, or the chain does not typecheck.

`prereq-backchain` backchains a *subject* to plan study; this skill backchains a *paper* until it typechecks **and reads without leaving the page.**

**Read first, every time:**

- `references/paper-note-templates.md` — the page skeletons (Map, section, and the two reference pages).
- `../polymath-notes/references/obsidian-patterns.md` — **source of truth for Obsidian syntax**: wikilinks, transclusion, collapsible callouts, tables, frontmatter, Windows-portable filenames, math delimiters (`$...$` / `$$...$$`; never `\(...\)`; never LaTeX inside `[[ ]]`). Not restated here. When this skill and that file disagree, that file wins.
- `../polymath-notes/SKILL.md` — Core Philosophy only. **Its Writing Style does not apply**: the register here is specification, with Tong-style prose permitted only in a folded `Commentary` block.
- `Study notes/Prerequisite DAG.md` — the anchor set (see *Anchors*).

---

## The reading surface is the deliverable

The note-set has one **reading surface**: the **Map** plus **one page per paper section**. A reader opens only those, in order, to read the entire paper. There are no per-result subpages on the reading path — the v-fragmented "96 atomic pages" design, where reading one result meant opening eight others, is exactly what this skill replaces.

Two **optional reference pages** sit under the Map, linked but never required to read a section:

- **`External Inputs and Gaps`** — the consolidated ledger of every imported result, each with precondition→conclusion, source, and gap-depth. The honest floor.
- **`Anchors and Prerequisites`** — the anchor set named explicitly, the backchain of every term to it, and a repair order for the gaps.

Granularity is fixed at the **section**: one paper section = one page = one logical movement. A section is the largest unit that completes one movement (hence the largest that can be made self-contained with bounded length) and the smallest unit at which a linear reader never has to leave the page. If a paper section is huge, keep it one page and lean on the Spine skim-layer and anchored subheadings; fold detachable digressions into a single collapsible rather than spawning a file.

**Single-sourcing without a build step.** Recurring cores (a standing convention, a heavy definition like "Bernstein function", a reused import) are authored **once, verbatim**, in a scratch cores file, and copied identically into every section that uses them. Duplication across a handful of section pages is the accepted cost of self-containment — the user's priority is self-containedness over DRY. Do **not** build a transclusion pipeline or a code tool to deduplicate; hand-copy the canonical text and keep the copies identical.

---

## Rule 1 — Types first, on the page

Every section page opens with a `# A. Standing setup` that inlines, as literal text bottoming at the anchor set, **every** standing and geometric object the section uses (so dropping straight into the section needs nothing from earlier pages), followed by a **signature table** (symbol | type — every symbol used on the page) and a **standing-conventions** block.

A type is not a name: give domain and codomain for maps; the reference measure for densities; finite / $\sigma$-finite / probability for measures; the index set for sums. Flag notation collisions here. **Resolve a collision by a distinct glyph** when a shared one would force per-section rewrites — e.g. rename the subordination/proper-time variable to `u` and reserve `s` for the spectral parameter, rather than writing "$s$ means two things".

Every result is stated types-first: its hypotheses as numbered symbolic propositions **(H1)…(Hn)**, and multi-clause definitions as numbered clauses **(D1)…(Dn)**. But a numbered hypothesis is only useful if its content is *on the page*: write "(H1) $\phi$ Bernstein — $\phi(\lambda)=a+b\lambda+\int(1-e^{-\lambda u})\nu(\mathrm du)$, with $b>0$ or $\nu(0,\infty)=\infty$", never "(H1) $\phi$ Bernstein satisfying Assumption 2.3" pointing elsewhere.

---

## Rule 2 — Every jargon token is expanded on the page, in one of four tiers

For every symbol, predicate, or imported result a statement uses, its minimal reconstruction appears **on the page** as literal markdown, in exactly one of four forms, chosen by length and by first-versus-later use. The reader meets full symbolic content before any wikilink.

- **T0 — inline gloss** (reconstruction ≤ 1 line, predicate used in prose): **bold term** — em-dash — symbolic clause bottoming at anchors — em-dash — plain-language parenthetical, in the running sentence. Example: "$\Gamma$ acts **freely** — $\forall h\in\Gamma\setminus\{1\}\,\forall z:\ hz\neq z$ (no non-identity isometry fixes a point) — and **properly discontinuously** — $\forall K\Subset\mathbb H^2:\ \#\{h:hK\cap K\neq\varnothing\}<\infty$." Duplicate freely at every occurrence; a one-liner is cheaper to re-read than to resolve.
- **T1 — expanded core callout** (2–12 lines, first load-bearing use): `> [!def]+ term` (expanded by default), carrying the canonical core text.
- **T2 — collapsed recall chip** (the term was expanded earlier in this section, or is an object from an earlier section used only through its end-formula): `> [!recall]- term` (collapsed), carrying the shorter recall core.
- **T3 — import box** (an external result invoked without proof): `> [!import]- name — Says / Needs / Gives`, giving the conclusion (Says, symbolic), the preconditions (Needs, symbolic, no bare jargon), what you may now write (Gives), and the sentence "assume freely; nothing here re-proves it." Mark a genuine gap as such, with a one-line Status naming the source.

**The "used here" line lives outside the fold.** Every T1/T2/T3 callout is preceded by one line — outside the callout — stating the single consequence *this* argument consumes ("**Used here —** only that it yields a well-defined $I_\phi$; no other property is used"). So even a collapsed or broken fold leaves the typecheck-critical fact visible.

**The scissor test is the acceptance criterion.** Delete every wikilink on the page; every statement and every proof must still typecheck from what remains rendered. A wikilink may appear **only** in the foot's "Climb" line, after all inlined content, never inside a Statement / Hypothesis / Signature / Discharge / Import. **No live transclusion `![[X#Y]]` as a self-containment device** — it is a load-bearing link and renders as raw text outside Obsidian.

---

## Rule 3 — Proofs are checkable above the fold

Each result carries a **Discharge table** above the fold: `| step | apply | to | get |`, one row per move, every symbol in it typed on the page and every predicate an import or recall above it. Close it with "Every symbol is typed above; the block typechecks with nothing off-page." The prose proof is folded beneath in `> [!note]- Proof (skippable)`, each step citing a labelled hypothesis, an import's *Gives*, or an explicit computation. Worked numerical checks fold into `> [!note]- Verification of … (skippable)` and every number must be reproducible from the page's own cores.

---

## Rule 4 — Prose last

Motivation, intuition, history, "why this is the natural object", cross-section narrative — all of it in the folded `> [!note]- Commentary (skippable)` at the foot. This is where Tong-register writing is allowed and welcome; nowhere else. The body is specification register. Commentary and worked checks are held to the same faithfulness bar as statements: no unsourced claim, every number reproducible on the page.

---

## The section page skeleton (A/B/C/D)

Fixed, per `references/paper-note-templates.md`:

- **A. Standing setup** — inlined standing/geometric objects + signature table + standing conventions + T2 recall chips for earlier-section objects.
- **B. Spine of §N (skim layer)** — a numbered list, one line per result in order, each a `*Given* … ⊢ *Produces* …` type card. A reader who reads only B has the section's logical content.
- **C. The results** — one `## §N.k` per result: new symbols → expansions (T0–T3, each with its "used here" line) → Statement (H1…Hn) → Discharge table → folded Proof → optional folded worked checks → optional `> [!warning]` when a hypothesis's exact form is the whole content.
- **D. Exports, climb, commentary** — Exports (numbered typed statements later sections consume, each tagged with its consumers) → Climb (optional wikilinks: sibling sections + the two reference pages; deletable with zero loss) → folded Commentary.

The Map and the two reference pages have their own skeletons in the templates file.

---

## Faithfulness guards

- **Model-scoped cores.** Any clause naming a geometric model ($\mathbb H^2$ vs $\mathbb H^3$, real vs complex length, hyperbolic vs loxodromic) is written per model; never hand-copy a model-specific one-liner across the boundary.
- **Canonical corrected facts** (so a re-run cannot reintroduce known bugs): state assumptions in their exact form (e.g. "$b>0$ or $\nu(0,\infty)=\infty$", not "$a=0$"); carry reality bounds ($\kappa\ge-\tfrac14$); state the index set of every "total mass" (non-trivial, non-peripheral classes).
- **Every number reproducible.** A worked value in a fold must follow from the cores on the page, not from an off-page source.

**What this skill does not produce.** No exercises, no difficulty tags, no "legal operations" apparatus — those belong to `polymath-notes`. If a result deserves drills, note it once on the Map as a pointer to `exercise-builder`.

---

## Procedure

Keep working notes in `.scratch/` (gitignored).

### Pass 1 — Skim: build the inventory and lock the cores

Read the whole paper (extract with `pdftotext -layout`, or `pypdf` if poppler is absent). Produce:

1. **Result inventory** — every definition, theorem, lemma, proposition, corollary, remark, construction, with paper number and section. Remarks routinely hide definitions.
2. **Symbol table** — every symbol with its type; surfaces collisions (one letter for two things) that get distinct glyphs.
3. **Jargon list** — every predicate/term a non-specialist would look up, tagged by tier (T0/T1/T2/T3) and by which anchor it bottoms out at. This is the coverage worklist; it is the one most often under-built.
4. **Import list** — every result invoked without proof; each becomes a T3 box and a row of the `External Inputs and Gaps` ledger. Include analytic identities that feel too small to name.
5. **The anchor set** — from the DAG (🟢 nodes) and the owner's `CLAUDE.md` background. State calibration calls (a 🔵 node treated as an anchor) explicitly on the Anchors page rather than silently.
6. **The canonical cores** — author, once and verbatim in `.scratch/`, the standing-conventions block and every recurring core (heavy definitions, reused imports). Section pages copy these identically.

**Confirm the section split and the anchor calibration with the user if either is large or contested.** If the user specifies a split, adopt it.

### Pass 2 — Write

Order: the canonical cores; then the Map; then section pages in paper order; then the two reference pages. Write one page fully before the next; no stubs. Only wikilink pages that exist or are being written in the same batch.

### Pass 3 — Self-check

Run the checklist below and the mechanical audits from `polymath-notes` (`find-math-bugs.py`, `find-latex-bugs.py`, `find-wikilink-bugs.py`) plus a wikilink-resolution audit. Do **not** run `autolinker.py` over a paper folder — it mislinks paper-local notation. Commit with a descriptive message; push only when the user asks.

---

## Self-check

Verify each and report.

**Self-containment (the point of this skill)**

1. **Scissor test.** On every section page, deleting all wikilinks leaves every statement and proof typecheckable from what remains.
2. **Reading surface.** A reader opens only the Map + section pages, in order, to read the whole paper; no subpage is on the reading path.
3. **Coverage.** Every non-anchor term in a Statement/Hypothesis/Signature/Discharge/Import is expanded on the page (T0–T3). Grep each section for the jargon list; each occurrence is expanded, not a bare name.
4. **No load-bearing links.** No wikilink inside any Statement/Hypothesis/Signature/Discharge/Import; wikilinks appear only in the foot's Climb line and are deletable with zero loss. No live `![[ ]]` transclusion used for self-containment.
5. **"Used here" lines** sit outside every T1/T2/T3 fold.

**Typing**

6. Every section opens with `# A. Standing setup` inlining every standing object + a signature table (every symbol typed, collisions flagged) + the standing-conventions block.
7. Every result is types-first: hypotheses **(H1)…(Hn)** as symbolic propositions with content on the page; multi-clause definitions numbered **(D1)…(Dn)**.
8. Notation collisions resolved by distinct glyphs, restated on every section page.

**Imports**

9. Every imported result has a T3 box with Says / Needs / Gives and "assume freely", and a row on `External Inputs and Gaps` with source and gap-depth.
10. Blind-faith test: pick three proofs; granting only the T3 boxes on their pages, each typechecks.

**Proofs**

11. Every result has a Discharge table above the fold; the prose proof is folded and every step cites a labelled hypothesis, an import's *Gives*, or a computation.

**Structure**

12. Page order is A/B/C/D; the Spine skim-layer is present; prose is only in the folded Commentary.
13. Section pages are the paper's own sectioning; detachable digressions are folded, not spawned as files.
14. `External Inputs and Gaps` lists every import; `Anchors and Prerequisites` bottoms out at anchors and ranks the gaps.

**Mechanics**

15. Math is `$...$` / `$$...$$`; no LaTeX inside `[[ ]]`; every wikilink resolves; filenames are Windows-portable (none of `< > : " / \ | ? *`; `§` is fine).

Report as: "Paper-notes self-check: N of 15 verified" plus any item that required a fix, and the scissor-test result per section page.
