---
name: paper-notes
description: >
  Rewrite a finished research paper into a self-contained, re-enterable Obsidian note-set: a map page with a
  type index, section pages, and Def / Thm / Constr subpages, with every unfamiliar term backchained to an
  anchor concept the reader already knows. Use whenever the user points at a paper (in `paper_source/` or
  `sources/`) and asks for notes on it, a breakdown of it, a reading guide for it, or wants to "understand what
  each result is for" without reading the proofs. Trigger phrases: "make notes on this paper," "break down this
  paper," "write up this paper," "paper notes for X," "what does each theorem in X let me do," "backchain this
  paper," "make this paper re-enterable," "type cards for this paper." Distinct from polymath-notes (which
  writes chapter-level study notes with exercises from textbooks and lecture notes) and from prereq-backchain
  (which plans what to study). This skill takes a *specific finished paper* as input and produces a note-set
  optimised for skimming the logical spine, climbing any hypothesis down to anchors, and dropping into a full
  proof only on purpose.
---

# Paper Notes — Obsidian Edition

A specialisation of [`polymath-notes`](../polymath-notes/SKILL.md) and `prereq-backchain` for a single finished paper.

Same philosophy — self-containedness, insight density, progressive disclosure, David-Tong-style prose for everything that is not a formal statement. Same Obsidian mechanics. The difference is the input and the job. The input is a paper somebody else wrote, in the order they chose to write it, with the proofs in the way. The job is to rewrite it so that the owner can:

1. **understand what every result is for without reading any proof**;
2. **click into a definition-or-justification chain from anywhere and climb it until they hit concepts they already know**;
3. **drop into the full proof only when they choose to**.

`prereq-backchain` backchains a *subject* to plan study. This skill backchains a *paper* to make it comprehensible.

**Read first, every time:**

- `references/paper-note-templates.md` — the page-level skeletons this skill produces (map, section, `Def -`, `Thm -`, `Constr -`, prereq DAG).
- `../polymath-notes/references/obsidian-patterns.md` — **the source of truth for all low-level Obsidian syntax**: wikilinks `[[Page]]` / `[[Page|alias]]`, transclusion `![[Page#Section]]`, collapsible callouts, foldable bullets, frontmatter, Windows-portable filenames, and math delimiters (Obsidian uses standard `$...$` and `$$...$$`; never Notion's variant, never `\(...\)`). None of those rules are restated here. When this skill and that file appear to disagree, that file wins.
- `../polymath-notes/SKILL.md` — Core Philosophy and Writing Style. Everything there about register, prose over bullets, no abbreviation, no hedge stacking, concrete before abstract, and formulaic specification of every geometric object applies here unchanged.
- `Study notes/Prerequisite DAG.md` — the anchor set (see *Anchors* below).

---

## The output structure

For one paper, the skill produces a folder under `Study notes/Papers/<Paper Short Title> (<Authors>)/` containing:

| Page | Filename | What it is |
|---|---|---|
| Map page | `Map - <Paper Short Title>.md` | One paragraph on what the paper does; the **type index** (every theorem, lemma, proposition, corollary and construction with its one-line type card and a link); the local prerequisite DAG in summary; a suggested reading order. |
| Section pages | `§N.M <Section Title>.md` | One per section or coherent cluster of results. Holds the narrative and the full type cards; proofs folded; subpages linked. |
| Definition subpages | `Def - <name>.md` | One per term the reader might not know (decided by the DAG — see *Anchors*). |
| Theorem subpages | `Thm - <name>.md` | Statement, type card, strategy line, folded proof. |
| Construction / assumption subpages | `Constr - <name>.md` | One per object that later appears as a *hypothesis* of some theorem, so that hypothesis is a link, not a black box. |
| Local prereq DAG | `Prereq DAG - <Paper Short Title>.md` | The backchain as an indented dependency list, bottoming out at anchors. |

Section-page filenames carry the paper's own section numbers. This is deliberate: it makes "where was that in the paper" a one-glance question and keeps the note-set aligned with the PDF the reader will have open alongside it.

Every page gets YAML frontmatter. Use `type: paper-map`, `type: paper-section`, `type: definition`, `type: theorem`, `type: construction`, `type: prereq-dag`, plus `paper:` (a short citation key), `subject:`, `prereqs:`, and `tags:`. Schema details are in `obsidian-patterns.md`; the `paper:` and the four new `type:` values are this skill's additions.

---

## The rules

### A. Type-first

**Every result carries an always-visible type card.** Before any proof, and again in the map page's type index, each theorem, lemma, proposition, corollary and construction gets a short block stating three things in words, with links:

- **Given** — the hypotheses, each one a wikilink to its `Def -` or `Constr -` subpage. Never an undefined term inline.
- **Produces** — the object or bound the result yields, *with its type*: what space it lives in, what it is a function of, whether it is a number, a measure, an identity, a bound.
- **Lets you** — the operational payoff. One sentence: "under these assumptions you may now construct / compute / bound / replace X."

The governing rule: **reading only the type cards, top to bottom, should give a correct mental model of the paper's logical spine.** Test it by reading only the type index on the map page and asking whether the paper's argument is recoverable from it. If a step in the spine is missing, some result's "Lets you" line is wrong.

Type cards are **non-folding**. They are the thing that must survive a skim. Write them as a `> [!abstract] Type card` callout with no `-` on the marker, so it renders expanded and cannot be collapsed away by accident.

**Type-first at the object level, too.** Every function, operator, measure, kernel or map introduced anywhere states its signature explicitly at first use — domain and codomain, the space each input lives in, what it returns, and any normalisation or reference measure. The heat kernel is $p : (0,\infty) \times X \times X \to (0,\infty)$, a density with respect to the Riemannian volume $\mathrm{vol}_g$, not "the heat kernel". The loop measure is a $\sigma$-finite — emphatically not finite — measure on the space of unrooted unparametrised loops. A sum is over what index set, ranging over what. An integral is against which measure on which space.

If a symbol appears exactly once, prefer prose to a symbol. Otherwise declare it, type it, and never reuse it for anything else. Follow the terminology and notation discipline already in `obsidian-patterns.md`: standard field names with the tradition named when traditions disagree, no coined Capitalised terms, one symbol one meaning.

### B. A definition subpage for every term the reader might not know

Decide "might not know" against the DAG, not by intuition. Any concept whose home subject sits below anchor familiarity gets a `Def -` subpage. Each such page contains, in this order:

1. **Plain-language gloss first.** One or two sentences that would satisfy someone who will never read the formal version. This comes *before* the formal definition, always.
2. **The formal definition.**
3. **The type or signature of every object the definition introduces.**
4. **One minimal example**, and where it earns its place, **one near-miss non-example** — an object that fails exactly one clause, with that clause named.
5. **"Used in this paper at:"** — a list of backlinks to every page that consumes the definition.

A `Def -` page may reference other `Def -` pages. That is the backchain in action, not a failure of self-containedness.

### C. Backchain until it bottoms out at anchors

For each definition and each theorem, list the concepts it depends on. For every dependency that is not an anchor, create (or link) a subpage and recurse. Stop when every leaf is an anchor.

**Anchors** are the concepts the reader already owns. The authority is `Study notes/Prerequisite DAG.md`: a node marked 🟢 (familiarity roughly $\geq 7$) is an anchor, and so is anything the owner's background paragraph in `CLAUDE.md` names as strong. A 🔵 node is not an anchor even if it feels elementary. When the DAG is ambiguous for a specific concept — the node exists but the paper uses a corner of it the node does not obviously cover — ask, rather than guessing; a wrongly-assumed anchor is the one failure mode this skill exists to prevent.

Record the result in `Prereq DAG - <Paper Short Title>.md` as an **indented dependency list**, deepest anchors at the leaves, so the whole reduction is visible at a glance and the reader can confirm nothing bottoms out at something they do not actually know. Mark anchors explicitly (🟢) and mark every non-anchor with a link to its subpage. The page is a checklist as much as a map: an unmarked leaf is a bug.

### D. Assumptions built from earlier constructions get linkable subpages

When a theorem's hypothesis is itself the output of an earlier construction — "let $V_\phi$ be the weighted potential measure", "let $\tau$ be the standard-form loxodromic representative", "assume the kernel is the periodisation (11)" — that construction lives on its own `Constr -` page and the hypothesis links to it.

**Links are bidirectional.** The `Constr -` page carries a "Consumed by" section listing every theorem that assumes it; each theorem's type card links back to the constructions it assumes. Keeping both directions is what makes the graph climbable: from a theorem you go up to its assumptions, and from an assumption you go down to everything it is load-bearing for.

Net effect: the reader can land on any theorem and climb its hypotheses, construction by construction, until reaching anchors, then climb back down, without ever hitting an unexplained assumption.

### E. Tedious proofs and calculations are folded and genuinely skippable

Full proofs and long calculations go inside a collapsed-by-default callout, `> [!note]- Proof (skippable)`. Use the nesting and blank-line rules from `obsidian-patterns.md`. Long routine computations that are not proofs — a change of variables, an evaluation of a Gaussian-type integral — get their own `> [!note]- Calculation (skippable)` fold.

Immediately above the fold, always visible, two things:

- the **type card**, and
- a single **strategy line** naming the one or two moves the proof turns on.

A strategy line is not a proof sketch. It names moves. "Unfold the conjugacy-class sum over cosets of the cyclic centraliser, then collapse the $\mathrm{d}t/t$ integral into $V_\phi$ via Lemma 2.11" is a strategy line. "First we show that the series converges, then we exchange the order of integration, then we substitute" is not — it describes the shape of a proof without naming what makes it work.

The test: **the reader should be able to take the result on faith and move on having read only the type card and the strategy line.** If taking the result on faith after reading those two leaves them unable to use it correctly downstream, the type card is underspecified.

### F. Self-containedness and re-entry

Every page must be comprehensible from itself via links. Order on every page: **notation registry first, motivation second, then content.** The notation registry is not optional and is never folded — it is the first thing a reader sees on returning after months, and it is what lets them read the formal statement below it without navigating away.

A page is "done" only when the owner could open it cold after months and reach full understanding by clicking links — never needing knowledge that appears nowhere in the graph. Where a hypothesis or a definition is short, prefer Obsidian transclusion (`![[Def - X#The Definition]]`) over restatement, so the statement stays in sync with its source.

**What this skill does not produce.** No exercises, no exercise indices, no difficulty tags, no "legal operations" or "sources and targets" apparatus. Those belong to `polymath-notes` and to a *subject*, not to a paper. If, while writing, a result turns out to deserve drills, note it in the map page's closing section as a pointer to `exercise-builder` rather than building them here.

---

## Procedure

Two passes, for the same reason `polymath-notes` uses two: a paper read once and written up in one go produces notes whose early pages do not know what the later pages need. Keep working notes in `.scratch/` (already gitignored; see `polymath-notes/SKILL.md` § Working Memory) so the inventory survives a context reset.

### Pass 1 — Skim: build the inventory

Read the whole paper. Extract text with `pdftotext -layout`, or `python3 -c "from pypdf import PdfReader; ..."` if poppler is absent. Then produce, as scratch files, four things:

1. **The result inventory.** Every definition, theorem, lemma, proposition, corollary, remark, and construction, with its paper number, its one-line content, and which section it lives in. Remarks matter — papers routinely hide a definition inside a remark (this paper defines the jump-process homotopy mass in Remark 3.1), and a remark that is load-bearing gets a page like anything else.
2. **The term list**, each term tagged `anchor` or `needs-subpage` against the DAG. Be honest here: the whole value of the note-set is that the `needs-subpage` list is complete.
3. **The backchain** — the local prereq DAG, recursed to anchors.
4. **The page split** — which sections become which pages, and which results become `Def -`, `Thm -` or `Constr -` subpages.

**Confirm the split and the `needs-subpage` list with the user before writing if either is large** (more than roughly ten section pages, or more than roughly twenty-five definition subpages). If the user has already specified a split or an explicit needs-subpage list in their request, adopt it and report any revisions you make rather than blocking on confirmation.

Deciding `Def -` versus `Constr -` versus neither:

- **`Def -`** if it is a *term* — something with a definition the reader might not know.
- **`Constr -`** if it is an *object the paper builds* and then later *assumes*. The test is whether it ever appears as a hypothesis. The Brownian loop measure is a `Constr -` because Theorem 3.2 assumes it; the Selberg zeta function is a `Def -` because theorems conclude *about* it rather than assuming it.
- **Neither** if it appears once, in one place, and is fully explained where it appears. Prose on the section page.

A single object can warrant both a `Def -` for the general notion and a `Constr -` for this paper's particular instance. When that happens, the `Constr -` page opens by transcluding the `Def -` page's definition section.

### Pass 2 — Write: sequentially, one page at a time

Order: **map page and prereq DAG first**, then section pages in paper order, then subpages. Write one page fully before starting the next; do not leave stubs to fill in later.

Writing the map page first is what makes the type index coherent — you draft each type card once at the map level, then expand the same card on the section page and again on the subpage. The three copies must agree; the map version is the shortest, the subpage version the fullest, and none of them may contradict the others.

Only wikilink a page that exists or is being created in the same batch. Everything else is **bold plain text** — clicking a wikilink to a missing file creates an empty stub in Obsidian. Since the subpages are written last, keep the filename manifest in `.scratch/` and hold to it exactly.

### Pass 3 — Self-check

Run the checklist below, then run the mechanical audits shipped with `polymath-notes` over the new folder: `find-math-bugs.py`, `find-latex-bugs.py`, `find-wikilink-bugs.py`, and the wikilink-resolution audit. Do **not** run `autolinker.py` over a paper folder — it is tuned for the subject vault's canonical term names and will mislink paper-local notation.

Then commit with a descriptive message. Push only when the user asks.

---

## Self-check

Before declaring a paper note-set complete, verify each of the following and report the result.

**Type-first (rule A)**

1. Every theorem, lemma, proposition, corollary and construction has a type card with all three fields — Given, Produces, Lets you.
2. Reading only the map page's type index gives a correct account of the paper's logical spine. Verify by writing out that account and comparing it against the paper's own introduction.
3. Every "Given" entry is a wikilink, not a bare term. Mechanical check: no type card contains a capitalised defined term outside `[[ ]]`.
4. Every function, operator, measure and map states its signature — domain, codomain, reference measure where relevant — at first use on each page where it appears.
5. Type cards are non-folding (`> [!abstract] Type card`, no `-` on the marker).

**Definitions and backchaining (rules B, C)**

6. Every non-anchor term has a `Def -` subpage. Mechanical check: grep the section pages for defined-looking terms and confirm each resolves.
7. Every `Def -` page leads with a plain-language gloss, before the formal definition.
8. Every `Def -` page gives the type of every object it introduces, one minimal example, and a "Used in this paper at" backlink list.
9. `Prereq DAG - <paper>.md` bottoms out at anchors only. Every leaf is either marked 🟢 or is a link to a page in this folder. An unmarked leaf is a bug.
10. No anchor was assumed that the DAG does not support. Spot-check three leaves against `Study notes/Prerequisite DAG.md`.

**Assumptions (rule D)**

11. Every object that appears as a hypothesis of some theorem has a `Constr -` page.
12. Every `Constr -` page has a "Consumed by" section, and every theorem listed there links back to it from its type card. Both directions present.
13. Landing on any theorem page, every hypothesis is climbable in one click.

**Proofs (rule E)**

14. Every proof is inside a collapsed `> [!note]- Proof (skippable)` callout.
15. Every folded proof has a visible type card and a visible strategy line immediately above it.
16. Every strategy line names moves, not proof shape.

**Re-entry (rule F)**

17. Every page opens with a notation registry, unfolded, before any formal content.
18. Spot-check three subpages cold: is each comprehensible from itself plus one click?
19. All math uses Obsidian delimiters `$...$` / `$$...$$`; no LaTeX inside any `[[ ]]`; every wikilink resolves; every transclusion anchor points at a real section.
20. Filenames are Windows-portable — none of `< > : " / \ | ? *`.

Report as: "Paper-notes self-check: N of 20 verified" plus any item that required a fix.
