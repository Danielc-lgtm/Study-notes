---
name: paper-notes
description: >
  Rewrite a finished research paper into a self-contained, machine-checkable Obsidian note-set: a map page with a
  type index, section pages, and Def / Thm / Constr / Ext subpages, in which every page opens with a typed
  signature block, every hypothesis is a symbolic proposition, every invoked external result is stated with exact
  preconditions and conclusion, and all prose is demoted to the bottom or folded away. Use whenever the user
  points at a paper (in `paper_source/` or `sources/`) and asks for notes on it, a breakdown of it, a reading
  guide for it, or wants to "understand what every result is for" without reading the proofs. Trigger phrases:
  "make notes on this paper," "break down this paper," "write up this paper," "paper notes for X," "what does
  each theorem in X let me do," "backchain this paper," "make this paper re-enterable," "type cards for this
  paper." Distinct from polymath-notes (which writes chapter-level study notes with exercises from textbooks and
  lecture notes) and from prereq-backchain (which plans what to study). This skill takes a *specific finished
  paper* as input and produces a note-set optimised for typechecking the logical spine, climbing any hypothesis
  down to anchors, and dropping into a full proof only on purpose.
---

# Paper Notes — Obsidian Edition

A specialisation of [`polymath-notes`](../polymath-notes/SKILL.md) and `prereq-backchain` for a single finished paper.

## The reader model

**Write for a reader who is a slightly less pedantic Lean.**

They have the definitions somewhere but have forgotten which ones, they cannot resolve an ambiguous English predicate into a proposition, and they will not accept a step whose hypothesis they cannot check. What they *will* do, cheerfully, is take a result on faith — provided its precondition and its conclusion are both stated precisely enough to be applied.

So the job is: **find the minimal reconstruction that makes the whole paper typecheck, and lay it out so that checking it is cheap.** Three failure modes follow directly.

1. **An untyped symbol.** $p$ appears and the reader does not know its domain, codomain, or reference measure. Bug.
2. **An ambiguous predicate.** "$\Gamma$ acts freely and properly discontinuously", "the form is regular", "$X$ is geometrically finite", "$P$ is polar". Each is a proposition the reader cannot expand. Either write it symbolically at point of use, or link to a page whose definition gives it as numbered symbolic clauses. **Prose predicates are bugs.**
3. **An unstated import.** A proof says "by the Wang–Xue identity" or "by the trace formula" and the reader does not know what those say. Even a black box must have a precondition and a conclusion, or the chain does not typecheck.

Everything below serves that. `prereq-backchain` backchains a *subject* to plan study; this skill backchains a *paper* until it typechecks.

**Read first, every time:**

- `references/paper-note-templates.md` — the page skeletons (map, section, `Def -`, `Thm -`, `Constr -`, `Ext -`, prereq DAG).
- `../polymath-notes/references/obsidian-patterns.md` — **the source of truth for all low-level Obsidian syntax**: wikilinks `[[Page]]` / `[[Page|alias]]`, transclusion `![[Page#Section]]`, collapsible callouts, tables, frontmatter, Windows-portable filenames, and math delimiters (Obsidian uses standard `$...$` and `$$...$$`; never Notion's variant, never `\(...\)`; never LaTeX inside `[[ ]]`). None of those rules are restated here. When this skill and that file appear to disagree, that file wins.
- `../polymath-notes/SKILL.md` — Core Philosophy only. **Its Writing Style section does *not* apply here**: this skill's register is specification, not David Tong. Tong-style prose is permitted only inside the folded `Commentary` block at the foot of a page.
- `Study notes/Prerequisite DAG.md` — the anchor set (see *Anchors*).

---

## Page order is fixed

Every page, without exception, in this order. **Formal content first; prose last or folded.**

| # | Section | Folding |
|---|---|---|
| 1 | `# Signature` — typed declaration table | never |
| 2 | `# Type card` — Given / Produces / Lets you | never |
| 3 | `# Statement` (Thm, Ext) or `# Definition` (Def) or `# Construction` (Constr) | never |
| 4 | `# Discharges` (Thm) or `# Depends on` (Def, Constr) | never |
| 5 | `# Proof` — `> [!note]- Proof (skippable)`, with a visible `**Strategy.**` line above it | folded |
| 6 | `# Checks` (Def, Constr) — instance / non-instance | never, but terse |
| 7 | `# Consumed by` / `# Used at` | never |
| 8 | `# Commentary` — `> [!note]- Commentary (skippable)` | folded |

Anything a reader needs in order to *apply* the result is above the fold. Anything that explains *why one might care* is in Commentary. If you find yourself writing a paragraph of motivation in section 3, it belongs in section 8.

**Length target: 60–110 lines per subpage.** Density comes from symbols, not from sentences. A page that has grown past 130 lines almost always has prose that belongs in Commentary, or a second concept that belongs on its own page.

---

## The rules

### A. Signature block first

Every page opens with `# Signature`: a two-column table, **symbol** and **type / defining property**. Every symbol used anywhere on the page appears in it. No exceptions, including on section and map pages.

A type is not a name. Write

| symbol | type |
|---|---|
| $p_X$ | $(0,\infty)\times X\times X\to(0,\infty)$; symmetric; density w.r.t. $\mathrm{vol}_g$; kernel of $e^{-t\Delta_X}$ |
| $\mu_X$ | $\sigma$-finite measure on $\mathcal{C}_X$; $\mu_X(\mathcal{C}_X)=\infty$ |
| $V_\phi$ | $\sigma$-finite measure on $(0,\infty)$; **not** finite |

not "the heat kernel", "the loop measure", "the weighted potential measure".

Include, wherever they apply: domain and codomain; the reference measure a density is taken against; whether a measure is finite, $\sigma$-finite, or a probability; whether a sum ranges over primitives or all iterates; which normalisation is in force. **Standing conventions** (sign of the Laplacian, speed of the process, boundary conditions) go in a short block immediately after the table, as displayed equations where possible.

### B. No ambiguous predicate

Every predicate applied to an object must be checkable. Two legal forms:

- **Symbolic at point of use.** "$\Gamma$ acts freely: $\forall h\in\Gamma\setminus\{1\},\ \forall z\in\mathbb{H}^2,\ hz\neq z$."
- **A link to a page whose `# Definition` gives numbered symbolic clauses.** `[[Def - Free and Properly Discontinuous Action]]`.

Predicates that always need one of the two: *free*, *properly discontinuous*, *regular*, *Markovian*, *closed* (of a form), *geometrically finite*, *polar*, *primitive*, *peripheral*, *trace class*, *σ-finite*, *conservative*, *complete*, *unitary*, *torsion-free*. When in doubt, it needs one.

**Number the clauses.** A definition with $n$ independent conditions states them as **(D1)…(Dn)**, and downstream pages cite them by number: "fails (D2)", "uses only (D1) and (D3)". This is what makes a non-instance checkable in one line instead of a paragraph.

### C. Hypotheses are labelled propositions

The `# Type card`'s **Given** field is a numbered list **(H1)…(Hn)** of typed propositions, not a sentence. Each is either symbolic or a wikilink to the page defining it. The `# Statement` then quantifies over exactly those. The `# Discharges` section says which hypothesis each invoked result consumes.

```markdown
> [!abstract] Type card — Theorem 3.5
> **Given.**
> **(H1)** $\phi$ a [[Def - Bernstein Function|Bernstein function]] with $b>0$ or $\nu(0,\infty)=\infty$ ([[Constr - Assumption 2.3|Assumption 2.3]]).
> **(H2)** $\gamma\in\mathcal{P}_X$, $\ell_\gamma>0$ its translation length.
> **(H3)** $m\in\mathbb{Z}_{\geq1}$; write $L:=m\ell_\gamma$.
>
> **Produces.** $\mu^\phi_X(\mathcal{C}_X(\gamma^m))\in[0,\infty]$, in closed form: $\dfrac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L)$.
>
> **Lets you.** Replace the double $(t,s)$ integral by one integral against $V_\phi$; each special case is then one substitution.
```

**Produces** states the object *and its type*, with the formula when there is one. **Lets you** is one sentence of operational payoff. All three fields, always, in this order. Type cards are **non-folding**: `> [!abstract] Type card`, no `-` on the marker.

### D. Every import gets an `Ext -` page

When a proof invokes a result the paper does not prove — a cited lemma, a classical theorem, an analytic identity — that result gets an `Ext -` page stating:

- its **signature** (what the symbols are);
- its **precondition**, symbolically, as numbered clauses;
- its **conclusion**, symbolically;
- **Status**: not proved here; the source; the DAG node that would close the gap.

The test: **a reader who accepts the `Ext -` page on blind faith must be able to follow every proof that uses it.** If they would have to go and read the source to know what was applied, the page is underspecified.

This includes analytic identities that feel too small to name. If $\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ discharges six computations, it is an `Ext -` page with precondition $a,b>0$, and each of those six cites it with its $a$ and $b$.

### E. Proofs are folded; what is above the fold is enough to apply the result

Full proofs and long computations go inside `> [!note]- Proof (skippable)` and `> [!note]- Calculation (skippable)`, collapsed. Above the fold, always visible: the **type card**, and a one-line **`**Strategy.**`** naming the one or two moves the proof turns on.

Inside the fold, every step names what it consumes: "by (H2) and [[Ext - Tonelli]]", not "by a standard argument". A proof step whose justification is not a link or a labelled hypothesis is a bug.

A strategy line names moves. *"Unfold the conjugacy-class sum over cosets of $C_\Gamma(\tau^m)=\langle\tau\rangle$, then collapse $\int\mathrm{d}t/t$ into $V_\phi$ via Lemma 2.11"* is a strategy line. *"First we show convergence, then exchange integrals"* is not.

### F. Backchain until every leaf is an anchor

For each definition, theorem and construction, list its dependencies. Every non-anchor dependency gets a page and recurses. Stop at anchors.

**Anchors** are what the reader already owns. The authority is `Study notes/Prerequisite DAG.md`: a 🟢 node (familiarity roughly $\geq 7$) is an anchor, as is anything the owner's background paragraph in `CLAUDE.md` names as strong. A 🔵 node is not an anchor even if it feels elementary. When the DAG is ambiguous for a corner of a node, ask rather than guess — a wrongly assumed anchor is the failure this skill exists to prevent.

Record the reduction in `Prereq DAG - <Paper Short Title>.md` as an indented list, anchors marked 🟢 at the leaves, every non-anchor a link. An unmarked, unlinked leaf is a bug. Gaps that genuinely cannot be closed are listed explicitly in a final section, each naming the `Ext -` page that carries it.

### G. Assumptions that are outputs of earlier constructions are `Constr -` pages, linked both ways

When a hypothesis is itself something the paper built — "let $V_\phi$ be the weighted potential measure", "let $\tau$ be the standard-form representative" — it lives on a `Constr -` page, and the hypothesis is a link.

**Bidirectional.** The `Constr -` page carries `# Consumed by` listing every result that assumes it; each such result's type card links back. Both directions present, or the graph is not climbable.

### H. Prose last

Motivation, intuition, historical remarks, "why this is the natural object", comparisons with other sections — all of it goes in the folded `# Commentary` block at the foot of the page. This is where Tong-register writing is allowed and welcome; it is not allowed anywhere else.

The one exception: a `Def -` page may carry a **single sentence** of gloss immediately under `# Definition`, tagged `**Gloss.**`, when the formal definition is genuinely opaque without it. One sentence. Anything longer is Commentary.

**What this skill does not produce.** No exercises, no difficulty tags, no "legal operations" or "sources and targets" apparatus — those belong to `polymath-notes` and to a *subject*. If a result deserves drills, note it once in the map page's closing section as a pointer to `exercise-builder`.

---

## Procedure

Keep working notes in `.scratch/` (gitignored).

### Pass 1 — Skim: build the inventory

Read the whole paper. Extract text with `pdftotext -layout`, or `python3 -c "from pypdf import PdfReader; ..."` if poppler is absent. Produce four scratch files:

1. **The result inventory** — every definition, theorem, lemma, proposition, corollary, remark and construction, with paper number and section. Remarks matter: papers routinely hide a definition in one.
2. **The symbol table** — every symbol in the paper with its type. Building this first is what makes the signature blocks cheap later, and it surfaces collisions (the paper reusing $s$ for two things, $L$ real in one section and complex in another) that must be flagged in the notes.
3. **The predicate list** — every predicate applied to an object anywhere in the paper, each tagged *symbolic at point of use* or *needs a page*. This is the rule-B worklist and it is the one most often under-built.
4. **The import list** — every result the paper invokes but does not prove. This is the `Ext -` worklist. Include analytic identities.

Then the term list (anchor / needs-subpage against the DAG), the backchain, and the page split.

**Confirm the split and the needs-subpage list with the user before writing if either is large** (more than roughly ten section pages, or twenty-five definition subpages). If the user has already specified a split, adopt it and report revisions rather than blocking.

Deciding the page type:

- **`Def -`** — a *term*: something with a definition the reader might not know.
- **`Thm -`** — a result the paper *states as its own*, whether or not it proves it in full.
- **`Constr -`** — an *object the paper builds and later assumes*. Test: does it ever appear as a hypothesis?
- **`Ext -`** — a result the paper *invokes without proof*. Test: is its justification a citation?
- **Neither** — appears once, fully explained where it appears. Prose in the section page.

`Thm -` and `Ext -` can both apply: a numbered result of the paper that the paper cites rather than proves. Prefer `Ext -` and say so in Status — the reader's question is "may I assume this?", and `Ext -` answers it.

### Pass 2 — Write

Order: map page and prereq DAG first, then section pages in paper order, then subpages. Write one page fully before the next; no stubs.

Only wikilink pages that exist or are being created in the same batch; everything else is bold plain text. Keep the filename manifest in `.scratch/`.

### Pass 3 — Self-check

Run the checklist below, then the mechanical audits shipped with `polymath-notes` (`find-math-bugs.py`, `find-latex-bugs.py`, `find-wikilink-bugs.py`) plus a wikilink-resolution and transclusion-anchor audit over the new folder. Do **not** run `autolinker.py` over a paper folder — it is tuned for the subject vault's canonical term names and will mislink paper-local notation.

Commit with a descriptive message. Push only when the user asks.

---

## Self-check

Verify each and report.

**Typing (rules A, B, C)**

1. Every page opens with `# Signature`, and every symbol used on the page appears in the table.
2. Every entry in the table gives a *type*, not a name: domain and codomain for maps; reference measure for densities; finite / $\sigma$-finite / probability for measures; index set for sums.
3. No ambiguous predicate anywhere above the fold. Grep the folder for *free*, *properly discontinuous*, *regular*, *Markovian*, *geometrically finite*, *polar*, *primitive*, *peripheral*, *trace class*, *torsion-free*, *unitary*: each occurrence is either symbolic on the spot or inside a wikilink.
4. Every multi-clause definition numbers its clauses **(D1)…(Dn)**, and every non-instance names the clause it fails.
5. Every type card's **Given** is a numbered list **(H1)…(Hn)** of typed propositions.
6. Every type card has all three fields, and **Produces** states a type.
7. Type cards are non-folding.

**Imports (rule D)**

8. Every result invoked without proof has an `Ext -` page.
9. Every `Ext -` page states precondition and conclusion symbolically, and a Status line naming the source.
10. Blind-faith test: pick three proofs; assuming only the `Ext -` pages they cite, does each proof typecheck?

**Proofs (rule E)**

11. Every proof is folded, under a visible type card and a visible `**Strategy.**` line.
12. Inside every fold, each step cites a labelled hypothesis, a linked page, or an explicit computation.
13. Every strategy line names moves, not proof shape.

**Structure (rules F, G, H)**

14. Page order matches the fixed table; prose is in the folded `# Commentary` block and nowhere else.
15. No subpage exceeds ~130 lines without a reason.
16. `Prereq DAG - <paper>.md` bottoms out at anchors only; unmarked, unlinked leaves are bugs; gaps are listed with their `Ext -` pages.
17. Every `Constr -` page has `# Consumed by`, and every result listed there links back from its type card.
18. Landing on any theorem page, every hypothesis is climbable in one click.

**Mechanics**

19. All math uses `$...$` / `$$...$$`; no LaTeX inside any `[[ ]]`; every wikilink resolves; every transclusion anchor points at a real heading.
20. Filenames are Windows-portable — none of `< > : " / \ | ? *`.

Report as: "Paper-notes self-check: N of 20 verified" plus any item that required a fix.
