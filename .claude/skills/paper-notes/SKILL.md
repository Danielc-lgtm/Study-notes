---
name: paper-notes
description: >
  Turn a single research paper (usually a PDF in paper_source/ or sources/) into a self-contained set of
  Obsidian notes, so that a reader competent at undergraduate analysis, linear algebra, and elementary
  probability — but NOT a specialist in the paper's field — can follow every definition, theorem, and
  reasoning step without looking anything up. Everything the paper uses above that undergraduate floor
  (measure theory, functional analysis, differential and hyperbolic geometry, stochastic processes, group
  theory beyond the basics, information theory, …) is backchained recursively into atomic Def/Thm/Lemma notes
  and recalled at point of use; every proof is rewritten gap-free; every symbol is typed. Use whenever the
  user points at a paper and asks to make notes on it, understand it, or read it without chasing references.
  Trigger phrases: "turn this paper into notes," "make notes on this paper," "self-contained notes from this
  PDF," "backchain this paper," "break down this paper," "make this paper readable without looking things up,"
  "explain this paper so a non-specialist can follow it," "read this paper for me and write it up," "notes on
  the paper in paper_source." Distinct from polymath-notes (chapter-level study notes with exercises from
  textbooks) and prereq-backchain (plans a subject to study). This skill takes ONE finished paper and produces
  a companion page that walks it section by section in the prose voice of the reference thesis, plus reusable
  atomic prerequisite notes and paper-result stubs, all wikilinked into the vault.
---

# Paper Notes — Self-Contained From a Single Paper

A skill for rewriting one finished research paper into an Obsidian note-set that a strong generalist — not a specialist in the paper's field — can read front to back, checking every step, without ever leaving the page to look something up. Where `polymath-notes` builds chapter-level study notes from textbooks and `exercise-builder` builds drills, this skill takes a *specific paper* and makes it *legible to a non-specialist* by backchaining everything it uses down to an undergraduate floor.

The deliverable is **one folder per paper**, `Study notes/paper/[Short Title]/`, holding:
- A short **hub page** with the plain-language abstract, the floor statement, the paper-wide Notation and Standing Conventions, the Prerequisites map, a table of contents linking each section page, and the Verification log.
- One **section page per paper section**, structured as a polymath-style **index / concept map**: a foldable-bullet list of every named item in that section (definition, theorem, lemma, corollary, proposition, remark, example, and any standalone paragraph carrying an argument), each entry wikilinking to its atomic subpage and holding an indented child bullet with the formal statement plus a 3–5 sentence unpacking. Each section page is **modularly self-contained** — a reader landing on §5 without having read §2–§4 can follow it, because §5 opens with a "Prerequisites recap" section that recalls (or transcludes) every earlier-section definition it uses.
- One **atomic subpage per named paper item**: every Def X, Thm X, Lemma X, Cor X, Prop X, Remark X, and Example X becomes its own `Def -`/`Thm -`/`Lemma -`/`Cor -`/`Prop -`/`Remark -`/`Ex -` page in the folder, fully self-contained (own recalls, own formal statement, own gap-free proof or worked case). Standalone paragraphs of argument that do not carry a paper number can become `Remark -` pages if they are load-bearing.
- **Atomic prerequisite notes** for every above-floor concept the vault does not already have (same folder). Prerequisites already elsewhere in the vault are wikilinked, not duplicated.

The reader has two entry modes. **Big-picture mode**: open a section page, scan the foldable-bullet index — you see every named item's statement inline without leaving the page. **Detail mode**: click into an atomic subpage — you get the full motivation, gap-free proof, and all point-of-use recalls; you can jump in cold without reading anything else.

---

## Read first, every time

Before writing a single note, read these in order. This is not optional; the skill's entire quality bar is set by the first item.

1. **The reference thesis — the prose exemplar.** `paper_source/Chiang Sung En-Thesis.pdf` (extract with `pdftotext -layout`, or `pymupdf`/`pypdf` if poppler is absent — `pip install pymupdf` then `import pymupdf`). **Study its prose closely before writing anything.** For paper notes the thesis governs the writing voice and *supersedes* the David-Tong register used elsewhere in the vault. What you replicate from it is specified in **The Prose Standard** below — read that section against the thesis open beside you.
2. `references/notation-discipline.md` — the typing, terminology, and prose-over-compression rules (Rules 3, 4, 7 below live here in full; the body only summarises them).
3. `references/companion-page-template.md` — the section-by-section companion-page skeleton.
4. `references/recall-callouts.md` — the point-of-use recall callout, the external-input callout, and the uncertainty marker.
5. `references/atomic-note-templates.md` — the prerequisite `Def -`/`Thm -`/`Lemma -` note and the paper's-own-result stub note.
6. `references/obsidian-patterns.md` (a symlink to the polymath-notes copy — **the source of truth for Obsidian syntax**: wikilinks, transclusion, collapsible callouts, math delimiters `$...$` / `$$...$$`, never LaTeX inside `[[ ]]`, Windows-portable filenames, YAML frontmatter). When this skill and that file disagree on *syntax*, that file wins — **with two deliberate paper-notes carve-outs**: (a) callout *titles* (fold lines) use Unicode, not LaTeX, for portability across Obsidian versions and themes, even though `obsidian-patterns.md` says markdown renders in titles (LaTeX in a callout *body* is fine — the carve-out is titles only); and (b) the custom callout labels `[!recall]` (a paper-notes device) and `[!cite]` (a native `quote` alias) are intended and permitted, not to be "corrected" against that file's callout-type list. See `references/recall-callouts.md`.
7. `../polymath-notes/SKILL.md` — **Core Philosophy only** (self-containedness via DAG links, hierarchical structure, connections, insight density). Reuse its atomic note types and its Obsidian conventions. **Do not** import its *Writing Style* section — the thesis replaces it here — and **do not** run its `autolinker.py` over a paper folder (it mislinks paper-local notation).

**Do NOT consult the Notion prerequisite DAG for this skill.** Backchaining here bottoms out at a fixed undergraduate floor (below), not at the vault's anchor set. The DAG is for planning what to study; this skill makes one paper self-contained against a fixed floor.

---

## The reader model — and the backchaining floor

**Write for a reader who has graduate-level command of undergraduate analysis, linear algebra, and elementary probability, and *nothing* above that.** They can do ε–δ analysis, integrate and differentiate, diagonalise a matrix, manipulate a basis, compute with random variables and expectations over discrete and continuous distributions, and follow a clean proof. They cannot be assumed to know measure theory, Lebesgue integration, functional analysis, the spectral theorem for operators, manifolds or curvature, hyperbolic geometry, stochastic processes and Itô calculus, information theory beyond the definition of entropy, group/ring theory beyond first courses, category theory, or any specialist apparatus of the paper's field.

Concretely, **the floor is exactly this:**

- **Analysis:** limits, continuity, uniform continuity, ε–δ, sequences and series, Riemann integration, differentiation in one and several real variables, Taylor's theorem, the basic inequalities (Cauchy–Schwarz, triangle, AM–GM), pointwise vs. uniform convergence.
- **Linear algebra:** vector spaces over $\mathbb{R}$ and $\mathbb{C}$, bases and dimension, linear maps and matrices, rank–nullity, determinants, eigenvalues and eigenvectors, inner products, orthogonality, the finite-dimensional spectral theorem for symmetric/Hermitian matrices.
- **Elementary probability:** sample spaces, events, discrete and continuous random variables, probability mass and density functions, expectation and variance, independence, conditional probability and Bayes' rule, the common distributions, the (elementary, non-measure-theoretic) law of large numbers and central limit theorem as facts.

Everything the paper uses that lives **above** this floor is a *gap* the notes must close. There are three failure modes, each of which the rules below exist to prevent:

1. **An untyped symbol.** A symbol appears and the reader cannot say what it is — its domain, codomain, the space it lives in, what a measure is over, what an operator acts on. Bug (Rule 3).
2. **An unexpanded term.** A word or predicate appears — "absolutely continuous", "geometrically finite", "sub-Gaussian", "faithful to the graph" — that the reader cannot turn into a precise statement. Bug (Rules 1, 2).
3. **A leap in a proof.** A step reads "clearly", "it follows", "by [X]" and the reader cannot reconstruct the missing reasoning. Bug (Rule 5).

---

## The Prose Standard — replicate the thesis

**The reference thesis is the voice every paper note must be written in.** Read it before writing, and hold specific passages in mind as calibration. The following features are what you are replicating — not the thesis's subject matter, its *manner*.

**Motivation leads; the formal statement is the punchline; intuition is reinforced around it.** The thesis motivates before it formalises — at the section level, and in the sentences that set up each object — so a definition arrives as the punchline of an explanation, not cold. But the numbered definition itself is then stated crisply and formally *first*, and the deeper intuition follows it. The model passage: the Kullback–Leibler divergence is stated formally as Definition 2.1.8, $D_{KL}(P\|Q) = \sum_x P(x)\log\frac{P(x)}{Q(x)}$, and only *then* does Remark 2.1.3 re-derive it as "excess surprise" — defining entropy as "the average amount of surprise", building the cross-entropy $H(P,Q)$, and landing on the intuition identity $D_{KL}(P\|Q) = H(P,Q) - H(P)$. Reproduce this shape: *motivating prose that leads up to the object → the crisp formal statement → a concrete unpacking → a remark that re-explains the intuition*. The formal statement is never buried behind the intuition; the intuition sets it up and then re-illuminates it.

**Unpack every general statement in its smallest concrete case, right after stating it.** The thesis states the general object first and then makes it concrete: Definition 2.1.1 gives the general Lancaster product $\prod_{i}\big(P^{*}_{X_i} - P_{X_i}\big)$, and immediately after, the bivariate case is spelled out as $\Delta_L P = P_{XY} - P_X P_Y$; Definition 2.1.3 gives the general Möbius inversion formula, and Example 2.1.1 then works it out on the three-element chain with the actual $3\times 3$ zeta and Möbius matrices; the subset lattice on $\{X,Y,Z\}$ is enumerated in all eight elements right after its general definition. The general statement is the opening move; the concrete instance is the unpacking that follows and makes it obvious — not a substitute for stating the general form first. When a *motivating scenario* helps, it may precede the definition as prose; the numeric worked instance comes *after* the formal statement, never before it.

**Definitions are numbered, named, and formal; then surrounded by Remarks and Examples that supply intuition.** The thesis pattern is `Definition (Name)` → optional `Remark (Intuition: …)` → `Example (worked, with explicit computation)`. Reproduce this rhythm: a crisp formal statement, then the intuition and a worked instance around it. Intuition lives in prose and in worked examples, never as a substitute for the formal statement.

**Proofs are written as labelled, justified steps — no leaps.** The thesis proof of V-structure detection consistency splits into "Direction 1" / "Direction 2" and then proceeds by bolded lead-ins — "Apply contrapositive of the contraction axiom:", "Apply d-separation to marginal independence:", "Identify unblocked path through Z:", "Establish Z as collider:", "Conclude V-structure:" — each a single justified move. Its independence computations show every line ($\sum_z P(X,Y,Z) = \sum_z P(X)P(Y)P(Z\mid X,Y) = P(X)P(Y)\sum_z P(Z\mid X,Y) = P(X)P(Y)$). Your rewritten proofs read like this: one justified step per line or per bolded move, nothing left to "clearly".

**Sections open by orienting the reader.** Each thesis section begins by recalling where we are and previewing where we go — "Having introduced interaction measures … and established the framework of graphical models and causality, we now explore how these complementary approaches can be combined" — often with the guiding questions stated as questions. Open each companion-page section the same way.

**Honest about provenance and difficulty.** The thesis says plainly "We now prove a result that was stated in Ref. [1] without proof and for which, to the best of our knowledge, a proof is not found in the literature. Here we provide a detailed original proof." Carry that honesty: name where a result comes from, say when you are supplying reasoning the paper omitted, and mark what you could not verify (Rule 6).

**Prose over bullets, but bullets for genuinely enumerable content.** The thesis uses flowing paragraphs for reasoning and reserves bullet lists for parallel enumerations (lattice operations, the cases of a theorem, the clauses of a definition). Match that: explanations are paragraphs; enumerations are lists.

Two registers coexist, exactly as in `polymath-notes`: **formal** for definition and theorem *statements*; **thesis-prose** for everything else — motivation, intuition, the unpacking of a definition, the connective tissue of a proof, the section openers. The difference from the rest of the vault is only *which* prose exemplar governs: here it is the thesis, not David Tong.

---

## The Seven Rules

Every paper note is bound by all seven. Rules 3, 4, and 7 are specified in full in `references/notation-discipline.md`; the summaries here are pointers, not the whole rule.

### Rule 1 — Backchain to the floor, recursively

Assume only the undergraduate floor. For **every** concept, notation, or result the paper uses that lives above the floor, close the gap. **Whether or not an atomic note already exists, the term still gets the full two-part point-of-use recall of Rule 2** (formal-and-typed *and* plain-language) on the companion page — the recall, not the linked note, is what guarantees the reading surface is floor-legible. The steps below decide where the *durable* note lives; they never replace the recall.

- **If a note already exists elsewhere in the vault** covering that concept, wikilink it from the recall — **do not duplicate it into the paper folder.** Search the vault first (`grep`/`find` over `Study notes/`) — the vault already has deep Measure Theory, Advanced Probability, Functional-Analysis-flavoured Linear Algebra, Differential Geometry, Topology, Group/Ring/Module theory, and more; reuse it. **But an existing note is written for the vault owner's specialist background (see `CLAUDE.md`) and is usually *not* floor-legible** — so linking it is not enough: the point-of-use recall must still carry the full floor-level content, and if that note's *own* machinery is above the floor and the proof leans on it, those sub-concepts get their own recalls too, so the companion page bottoms out at the floor even though the linked note does not.
- **If no note exists,** create an atomic `Def -`, `Thm -`, or `Lemma -` note for it (template in `references/atomic-note-templates.md`), placed **in this paper's own folder** — `Study notes/paper/[Short Title]/Thm - Radon–Nikodym Theorem.md`. Every note newly created for the paper lives in that single folder alongside the companion page; there is no scattering into subject-area folders. (This replaces the earlier convention of placing prerequisite notes in the subject hierarchy — they are now paper-local, so one paper's note-set is one self-contained folder.) Full placement rules: `references/atomic-note-templates.md`.
- **Scale the durable note to how load-bearing the concept is.** A concept whose *properties are actually used* in a reasoning step the reader must follow gets a full atomic note (with the axiom-motivation / statement apparatus of the template). A concept that is mentioned once and only in passing needs the point-of-use recall alone — or at most a scoped stub carrying only the one fact the paper uses — not a full stand-alone note. Cluster tightly-related prerequisites into a single compound atomic note (as `polymath-notes` does with compound definition pages) rather than spawning many tiny notes. The recall coverage is exhaustive; the *note* granularity is proportional to use.
- **Then recurse on each new note's own prerequisites.** A Radon–Nikodym note needs absolute continuity of measures and the notion of a $\sigma$-finite measure; each of those, if above the floor and not yet in the vault, gets its own atomic note, until every leaf bottoms out at the floor. The backchain terminates because the floor is fixed and finite.

Build the backchain as an explicit per-section prerequisite list during Pass 1 (Procedure below), so Pass 2 writes the atomic notes before the companion section that needs them.

`prereq-backchain` backchains a *subject* to plan study; this skill backchains a *paper* until every step reads without leaving the page.

### Rule 2 — Recall every unfamiliar term at its point of use, with a picture the reader can hold

Whenever the paper (or your own exposition) uses a term or notation above the floor, insert a collapsible recall **right where it is used** — not only a wikilink to its atomic note. The recall has **three fields**, not two:

1. **Formally** — the precise, typed definition (the formal content).
2. **In words** — a plain-language paraphrase using *no other above-floor jargon*. If the paraphrase must use another above-floor term, either replace it with a floor-level phrase or nest a `> [!recall]-` for that term inside this one. This field must land: reading it alone, a floor-level reader must be able to state, in their own words, what the object is.
3. **Concretely** — a specific mental model the reader can hold: a small example ($n = 2$, or the smallest non-trivial instance), a physical picture (a rubber sheet, a cylinder, a random walk on $\mathbb{Z}$), a computation they can do on paper, or a picture-in-words with explicit coordinates. Never "See [[Def - X]]" as the whole of this field. A recall without a concrete anchor fails.

```markdown
> [!recall]- Absolutely continuous (μ ≪ ν)
> **Formally:** for measures $\mu, \nu$ on a measurable space $(X, \mathcal{F})$, $\mu \ll \nu$ means every $\nu$-null set is $\mu$-null: $\nu(A) = 0 \Rightarrow \mu(A) = 0$ for all $A \in \mathcal{F}$.
> **In words:** $\nu$ sees at least everything $\mu$ sees. Wherever $\mu$ puts positive mass, $\nu$ already put some.
> **Concretely:** on $\mathbb{R}$, Lebesgue measure $\lambda$ (length) and the standard normal measure $\gamma$ (bell curve density) satisfy $\gamma \ll \lambda$: any set of zero length also has zero probability, because $\gamma$ has a density $\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ with respect to $\lambda$. But $\lambda \not\ll \delta_0$: the single point $\{0\}$ has $\delta_0(\{0\}) = 1 \ne 0$ yet $\lambda(\{0\}) = 0$. See [[Def - Absolute Continuity of Measures]].
```

The recall is collapsed (`-`) so a knowing reader is not slowed. **Do not economise on length** — Rule 7 governs. A recall that runs eight lines but leaves the reader holding a picture is a win; a recall that runs three lines of dense jargon and links out is a bug. Nested recalls are permitted (a `> > [!recall]-` inside a `> [!recall]-`). Duplicate freely across sections.

**Failure modes to watch for.** The following are the specific bugs the "In words" and "Concretely" fields exist to prevent — each is a Rule-2 violation:

- **Jargon-in-plain-language.** A paraphrase that reads "the non-trivial non-peripheral primitive hyperbolic element with axis the imaginary half-line and translation length $\ell$" is not plain language — every one of "non-trivial", "non-peripheral", "primitive", "hyperbolic (of a group element)", "axis", "translation length" is above the floor. Fix: rewrite in floor-level words *or* nest a recall for each term inside this one.
- **Metaphor-with-no-referent.** "The strip is one period of the cylinder that $\langle\tau\rangle$ wraps up" reads like exposition but leaves the reader unable to name what the strip *is*. Fix: give the strip's coordinates (an explicit set of complex numbers with explicit bounds), and separately give the physical picture.
- **See-the-definition-page-only.** "See [[Def - X]]" as the entire "In words" field is a total failure — the recall exists so the reader does not have to click through. Fix: put the plain-language content on this page, then wikilink for further detail.
- **Type-collision hidden in a name.** "Free homotopy classes correspond bijectively to conjugacy classes" makes sense only once the reader has *both* concepts. If a floor reader has neither, define both on the page — do not lean on the correspondence to do the defining work.

Full callout catalogue — recall (three-field), external-input, uncertainty — in `references/recall-callouts.md`.

### Rule 3 — Type everything (see `references/notation-discipline.md`)

Every object gets its full type/signature at first appearance: domain and codomain of every map, the space each element lives in, exactly what a measure is a measure *over* and whether it is finite/$\sigma$-finite/a probability measure, what an operator acts on, whether a symbol is free, bound, or quantified (and over what), and physical units where applicable. One symbol means one thing throughout; type-check every expression before writing it; both sides of every equation carry the same type. The companion page opens with a **Notation and Standing Conventions** section that types every symbol used across the paper. Full rule and the signature-table format: `references/notation-discipline.md`.

### Rule 4 — Standard terminology only (see `references/notation-discipline.md`)

Name every concept with the literature's name and attribute the field: "this is the **Radon–Nikodym derivative**", "this is the **Fenchel conjugate** (also called the Legendre transform in the smooth case)". Give both names when subfields differ. No coined compound-noun jargon, no Capitalised pseudo-terms invented for the notes, no repurposing of a standard symbol to mean something new. If a concept genuinely has no standard name, say so explicitly and describe it rather than minting a term. Full rule: `references/notation-discipline.md`.

### Rule 5 — Rewrite every proof gap-free

Reproduce every proof the paper gives, with **no leaps**. Expand each "it follows", "clearly", "one checks", "by [X]" into an explicit, justified step in the labelled-step style of the thesis. When the paper cites an external lemma it does not prove, do not silently import it: state it, type it, give its intuition, and cite the source in an **external-input callout** (`references/recall-callouts.md`), including the proof *only* when it is short or genuinely illuminating — otherwise the reader may take it on faith with its precondition and conclusion stated exactly. When the paper's own proof has a gap you must fill from your own knowledge, say so (Rule 6) and fill it. A proof in the notes is acceptable only when a floor-level reader could check every line on paper without drawing on anything off the page.

### Rule 6 — Verify, and be honest about uncertainty

When you supply a definition, a lemma, or a fact from your own knowledge rather than from the paper, **web-search to confirm it and cite a source** (a textbook, a canonical reference, a well-established online source). Never present confidently-wrong mathematics. When you remain unsure — a constant you could not pin down, a hypothesis you suspect the paper states loosely, a step you filled but could not fully verify — **flag it with a visible marker** (the uncertainty callout / inline `⚠️` marker in `references/recall-callouts.md`), stated plainly, rather than hiding the doubt. **Also mark, with the same visible marker, every place where the notes offer an intuition that has not been made rigorous** — a heuristic picture, a "morally this is why" remark, a plausibility argument standing in for a proof — stating plainly that it is intuition, not a formal derivation. The companion page ends with a short **Verification log** recording what was checked against which source, what remains flagged as uncertain, and where an intuition is stated but not yet formalised. Honesty about a gap is worth more than a smooth surface that misleads.

### Rule 7 — Prose over compression (see `references/notation-discipline.md`)

Comprehensive standard prose is preferred to compact formalism, **even when it runs several times longer**. Introduce a symbol only when prose would genuinely be worse (a computation, a precise quantified statement, a signature); never write a formula that merely restates a sentence you already wrote. The thesis is expansive on purpose — it re-explains, it unpacks, it walks the concrete case — and your notes should be too. Full rule, with the test for "does this formula earn its place": `references/notation-discipline.md`.

---

## What you produce

For one paper, the note-set is **one folder** — `Study notes/paper/[Short Title]/` — holding the hub page, one section page per paper section, and every atomic note newly created for that paper. The only thing that lives outside the folder is an already-existing vault note for a prerequisite, which is wikilinked from the recall rather than duplicated (Rule 1's exception).

There are **four kinds of page**, all in that single folder:

### 1. The hub page

`Study notes/paper/[Short Title]/Paper - [Short Title].md` — the paper's entry point. It carries the header (full citation, plain-language abstract, the explicit floor statement), the **paper-wide Notation and Standing Conventions** section (Rule 3), the **Prerequisites map** (the backchain — every above-floor concept wikilinked to its atomic prerequisite note, with a one-line reminder), a **table of contents** linking each section page in order, and the **Verification log**. This is a short page: it does not carry the paper's content, only its scaffolding.

### 2. Section pages — modular, self-contained indices

`Study notes/paper/[Short Title]/Paper - [Short Title] — §N [Section].md` — one per paper section. These are **polymath-style index pages**, not narrative walk-throughs. Each opens with:

1. A one-paragraph **section opener** (orient the reader; recall where we are and preview what this section does).
2. A **Prerequisites recap** — every earlier-section paper result and every external above-floor concept the section uses, each as either a `> [!recall]-` callout with the formal statement + plain-language meaning, or a `![[...]]` transclusion of a prior section's stub. The purpose: a reader who lands on §5 without having read §2–§4 can still follow it. **The rule is strict**: nothing above the floor is used without being recalled or transcluded on this page.
3. A **Concept map** — the section's named items (Definitions, Theorems, Corollaries, Lemmas, Propositions, Remarks, Examples) as **foldable bullets in the paper's order**. Each entry is a parent bullet whose text is a wikilink to the item's atomic subpage, with an indented child bullet holding a 3–5 sentence unpacking that names the formal statement, the intuition, and where it is used. Folding the parent collapses the child; the wikilink remains clickable in Editing and Reading view because it is ordinary Markdown (do not use HTML `<details>` — wikilinks inside HTML tags are not clickable in Obsidian). Sub-sections (§3.1, §3.2, …) are `###` sub-headers under the concept map; do not re-order.
4. A **Section verification log** — the section's honesty record (Rule 6): what was checked, what is flagged uncertain, what is intuition-not-proof.

The reader has two entry modes: **fold-out mode** — read the section's index without leaving the page, seeing every statement inline; **click-through mode** — jump into an atomic subpage for the full proof, motivation, and recalls. Both modes must work.

### 3. Atomic subpages for every named paper item

**One subpage per named item.** Every Def X, Thm X, Lemma X, Cor X, Prop X, Remark X, and Example X in the paper becomes its own file in the paper folder:

- `Def - [Name].md`, `Thm - [Name].md`, `Lemma - [Name].md`, `Cor - [Name].md`, `Prop - [Name].md`, `Remark - [Name].md`, `Ex - [Name].md`.

The naming uses the concept's name (`Thm - Homotopy Decomposition for Hyperbolic Surfaces`), not the paper's number, so the page is a usable wikilink target across the vault. The paper's number lives in the YAML `paper-ref` field.

Each atomic subpage is **fully self-contained**: it carries its own Notation section (with `> [!recall]-` callouts for every above-floor term it uses — do not assume the reader has read the section page or any earlier subpage), its own formal Statement, its own intuition, its own gap-free proof or worked-out example (in `> [!note]-` collapsibles), and a "Where the paper uses this" link back to the section page and any downstream results. A reader who lands on `Thm - Homotopy Decomposition for Hyperbolic Surfaces.md` cold — through Obsidian search, a wikilink from a different paper, or an old bookmark — must be able to read and check it without opening any other file.

**Standalone paragraphs of argument.** When the paper has a paragraph that carries a substantive argument or definition-in-prose without a number, and that argument is *load-bearing* (a later result depends on it), promote it to a `Remark - [Descriptive Name].md` subpage so it is greppable, wikilinkable, and holds its own recalls. Non-load-bearing prose stays on the section page.

**Scale each subpage to what the paper actually needs.** A definition whose properties are hammered on in later proofs gets the full apparatus (Axiom Motivation with per-condition failure analysis, Examples and Non-Examples with a calibration check). A remark that just names a comparison to prior literature is one paragraph plus a link. The polymath-notes Def/Thm template is the ceiling; scale down to fit. Skip polymath-specific sections that make no sense for a paper item (Convergent Strategies, Sources and Targets in the polymath sense, Bridges, Legal Operations, Cross-Field Exercise Suggestions — these belong to `polymath-notes`/`exercise-builder`).

### 4. Atomic prerequisite notes

`Def -`/`Thm -`/`Lemma -` notes for every above-floor **prerequisite** concept the vault does not already have — same folder, same self-containment discipline as the paper-item subpages. **If a note for the concept already exists elsewhere in the vault, wikilink it instead of duplicating** (searchable with `grep`/`find` over `Study notes/`).

**Wikilink everything.** Every above-floor term on the section page (recap or concept-map bullet) links to its atomic note; every atomic subpage links back to the section page and to any subpages it depends on; every wikilink resolves before commit. Forward references to concepts with no page yet are **bold plain text**, never wikilinks (an unresolved `[[ ]]` creates an empty stub when clicked).

**De-jargon aggressively.** The emphasis of this skill over `polymath-notes` is that every above-floor term gets a plain-language unpacking, not just a formal recall. If the term has both a formal name and an operational-intuition name, give both (Rule 4). The reader is a strong generalist, not a specialist — write for someone who has never met the concept.

---

## Procedure

Keep working notes in `.scratch/` (gitignored — create the directory and the `.gitignore` entry if absent). The backchain inventory, the symbol table, and the per-section prerequisite list are the things future-you will most want cached.

### Pass 0 — Read the thesis for style

Extract and read the reference thesis (`paper_source/Chiang Sung En-Thesis.pdf`). Internalise the prose features in **The Prose Standard**. Do not skip this even on a re-run — the voice is the deliverable's defining quality, and it is easy to drift back into terse specification register.

### Pass 1 — Read the paper and build the backchain

**Identify the target paper first.** The target is the PDF the user pointed at — in `paper_source/` or `sources/` — that is **not** the reference thesis `Chiang Sung En-Thesis.pdf` (the thesis is the style exemplar read in Pass 0, never the subject of the notes). If more than one non-thesis candidate is present and the user did not name one, ask which paper before proceeding.

Read the whole paper (extract with `pdftotext -layout`, or `pymupdf`/`pypdf` if poppler is absent; if the paper is long, extract its table of contents first and read section by section rather than loading it whole — mirror the `polymath-notes` trimmed-PDF workflow). Produce, in `.scratch/`:

1. **Result inventory** — every definition, theorem, lemma, proposition, corollary, and construction, with the paper's numbering. Remarks routinely hide definitions; catch them.
2. **Symbol table** — every symbol with its full type (Rule 3). Surface collisions (one letter for two things) and resolve them with a distinct glyph, recording the choice.
3. **Above-floor term list** — every concept, predicate, and notation above the floor. For each: does a vault note exist (link it) or must one be created (mark it, and recurse on *its* prerequisites)? This is the backchain worklist and the most common thing to under-build — be exhaustive.
4. **Import list** — every external result the paper invokes without proof; each becomes an external-input callout (and, if the reader will reuse it, an atomic `Thm -`/`Lemma -` note).
5. **Per-section prerequisite list** — for each paper section, which atomic notes must exist before its companion section is written. This orders Pass 2.

If the paper is large or the section split is non-obvious, confirm the split with the user before writing.

### Pass 2 — Write

Order: create the atomic prerequisite notes a section needs, then write that companion section, then its paper-result stubs — section by section through the paper. Write each page fully; no stubs-as-placeholders on the reading path. Only wikilink pages that exist or are being written in the same batch.

**For a long paper, commit and push incrementally as you go** — after each section (its atomic notes, its companion section, its stubs), stage and commit with a descriptive message ("Paper notes: [Short Title] §3 — Radon–Nikodym backchain + gap-free proof of Thm 3.1") and push. This preserves work across a long task and is the workflow the user expects for multi-section papers. Push **per the repository's git workflow and the session's branch requirements** — the working branch the session designates, not `main` directly unless that is the repo's stated convention. The point is incremental commits and pushes across a long paper, not batching everything to the end; where the repository's convention is push-on-request, commit each section and push when the user asks.

### Pass 2.5 — De-jargon audit (enter the floor reader's mindstate)

Before the leon pass, do an explicit **de-jargon walk** of every page you wrote. **Read every sentence with the mindset of the floor reader** — someone who has done a good undergraduate degree in maths and has never met your paper's field. For every sentence:

1. **List every noun and adjective** that would not appear in a first-year analysis / probability / linear algebra course. That is the sentence's jargon load.
2. **For each jargon word, ask**: "Can the reader, at this point on the page, produce a concrete mental model of what this refers to — a set of points, a formula, a picture with explicit coordinates?" Not "have they seen the word before"; not "is there a wikilink"; not "is there a definition somewhere on the page". The test is *concrete mental model in working memory, right now*.
3. **If the answer is no**, the sentence has failed the reader. Fix it by:
   - (a) replacing the word with a floor-level phrase that carries the same content; or
   - (b) inserting a `> [!recall]-` callout with the full three-field form (Formally / In words / Concretely) *before* the sentence; or
   - (c) rewriting the sentence to define the word in place with an explicit example.

The specific failure mode this pass catches: a recall or an atomic subpage that *looks* self-contained because it names all its terms and links to them, but whose "In words" field is itself jargon-heavy — "the non-trivial non-peripheral primitive hyperbolic $\tau$ conjugated to standard form with axis the imaginary half-line and translation length $\ell_\gamma$". The formal content is right, but no floor reader can *see* what is being described. That is a Rule-2 failure and it is caught only by explicitly entering the reader's mindstate — the mechanical audits below will not catch it, because syntactically everything is fine.

**Concrete drill.** Pick three atomic subpages at random. For each, cover the wikilinks and the "Formally" fields with a hand; read only the "In words" and "Concretely" fields and any prose you wrote. If a floor reader could not draw a picture, name a small example, or write a formula from what remains, the subpage fails. Rewrite before continuing.

### Pass 3 — Low-context-reader pass (leon-proofreader)

After a companion page is drafted, run a low-context-reader pass over it with the **`leon-proofreader` skill** — invoke it through the Skill tool (`Skill(skill: "leon-proofreader")`, or `/leon-proofreader`) in review mode over the companion page; if it is unavailable in the session, do the pass in its spirit. Read the page as someone with exactly the floor and nothing above it, walking top to bottom, and check every place the reader's attention is directed. Specifically for paper notes:

- Does any statement use a term that has not yet been recalled or typed above it? (A forward-used term is the paper-notes analogue of leon's "read below / assumed above" contradiction.)
- Is every "see [X]" / "recall" / "by the lemma above" referent actually present where claimed?
- Does each section opener orient the reader, and does the order of sections respect dependencies (nothing used before it is introduced)?
- Is any instruction to the reader ("take on faith", "we defer this to §5") clear about what is required now versus later?

Fix what the pass surfaces before the self-check.

### Pass 4 — Self-check and mechanical audits

Run the self-check below, plus the mechanical audits shared with `polymath-notes` — run them from the repo root as `python3 .claude/skills/polymath-notes/scripts/find-math-bugs.py`, and likewise `find-latex-bugs.py` and `find-wikilink-bugs.py` — and a wikilink-resolution audit (every `[[ ]]` resolves to a real file; every `![[ ]]` transclusion points to real content). **Do not run `autolinker.py`** over the paper folder — it mislinks paper-local notation. Then report.

---

## Self-check

Verify each item and report which passed and which required a fix.

**The floor and self-containment (the point of the skill)**

1. **Floor respected.** The hub page states the floor explicitly, and nothing above the floor is used without being either recalled (Rule 2, three-field form) or created as an atomic subpage and linked. Pick two section pages and two atomic subpages, read them as a floor-level reader: no unexpanded term survives.
2. **Recall coverage.** Every above-floor term in a statement or proof has a three-field point-of-use `[!recall]-` (Formally / In words / Concretely). Grep the section for the above-floor term list from Pass 1; each occurrence is covered.
3. **Backchain terminates at the floor.** Every atomic note's own prerequisites are either floor-level or themselves have atomic notes; no atomic note leaves a dangling above-floor dependency.
3a. **Jargon-free "In words" and picture-carrying "Concretely".** For every recall on every page, verify (a) the "In words" field uses no above-floor jargon — every noun/adjective is either floor-level or itself unpacked in a nested recall; (b) the "Concretely" field gives a specific mental model — a small example, a physical picture, a computation the reader can do, or explicit coordinates. A recall whose "Concretely" is empty or is "See [[Def - X]]" is a bug. Spot-check three recalls at random; if any fail, the whole page needs a de-jargon pass.
3b. **De-jargon audit performed.** Pass 2.5 was carried out on every page — for every sentence, the jargon load was listed and each jargon word was either replaced, recalled inline with the three-field form, or defined in place with a concrete example. Report what was flagged and what was fixed.

**Typing and terminology (Rules 3, 4)**

4. **Full typing.** Every symbol in the Notation section and at first use carries its type (domain/codomain, ambient space, what a measure is over, free/bound/quantified). Both sides of every displayed equation share a type. Collisions are resolved by distinct glyphs.
5. **Standard names only.** Every concept is named with the literature's term and the field attributed; no coined jargon, no repurposed standard symbols; genuinely unnamed concepts are flagged as such.

**Proofs and honesty (Rules 5, 6)**

6. **Gap-free proofs.** Pick two rewritten proofs; every step is a justified move a floor-level reader can check, with no "clearly"/"it follows"/bare "by [X]" left unexpanded. External lemmas appear as external-input callouts with precondition, conclusion, intuition, and source.
7. **Verification, flagged uncertainty, and unformalised intuition.** Every definition or lemma supplied from your own knowledge was web-searched and carries a citation. Everything you remained unsure of is flagged with the visible uncertainty marker, and every intuition stated without a formal derivation is marked as intuition-not-proof. The Verification log is present and records what was checked, what is flagged uncertain, and where intuition stands in for formalisation.

**Prose (Rules 1, 2, 7 and the Prose Standard)**

8. **Thesis voice.** Definitions are introduced intuition-first then formalised then unpacked in a concrete case; proofs are labelled justified steps; sections open by orienting the reader; prose is expansive, not compressed. Spot-check against the thesis passages named in The Prose Standard.
9. **Prose over compression.** No formula merely restates an adjacent sentence; symbols are introduced only where prose would be worse.

**Structure and mechanics**

10. **Output structure.** Everything newly created for the paper lives in the single folder `Study notes/paper/[Short Title]/`: the hub `Paper - [Short Title].md`, one section page per paper section `Paper - [Short Title] — §N [Section].md`, one atomic subpage per named paper item, and the atomic prerequisite notes. The only prerequisites outside that folder are ones that already had a note elsewhere in the vault, which are wikilinked, not duplicated.
11. **Modular self-containment of section pages.** A reader can open any single section page cold and read it without opening any other section page. Every earlier-section paper result and every above-floor prerequisite used in the section is present as a `> [!recall]-` callout or a transclusion in that section's Prerequisites recap. Spot-check: pick one section, list every above-floor term it uses, verify each is on the page.
12. **Modular self-containment of atomic subpages.** A reader can land on any atomic subpage cold — through Obsidian search, a wikilink from a different note, an old bookmark — and read it without opening any other file. Every above-floor term in its Statement / Proof / Example is recalled in that subpage's own Notation or `> [!recall]-` callouts. Spot-check three random subpages.
13. **Every named paper item is an atomic subpage.** Every Definition, Theorem, Lemma, Corollary, Proposition, Remark, and Example the paper numbers or names has its own subpage in the folder. Mechanical check: grep the paper for `Definition\|Theorem\|Lemma\|Corollary\|Proposition\|Remark\|Example` items with paper numbers, and verify each has a corresponding subpage (naming is by concept, not by paper number — cross-check via the `paper-ref` YAML field).
14. **Section page is a concept-map index.** Every section page uses foldable bullets (parent = wikilink to subpage, indented child = 3–5 sentence unpacking), in the paper's order, one per named item. No HTML `<details>`. The page carries no long narrative and no gap-free proofs — those live in the atomic subpages.
15. **Low-context pass done.** Pass 3 was run and its findings fixed.
16. **Mechanics clean.** Math is `$...$`/`$$...$$`; no LaTeX inside `[[ ]]`; every wikilink resolves; filenames are Windows-portable (`< > : " / \ | ? *` all avoided; `§`, `—`, and Unicode math are fine); `find-math-bugs.py`, `find-latex-bugs.py`, `find-wikilink-bugs.py` and the resolution audit come back clean.

**Report** as: "Paper-notes self-check: N of 16 verified", plus any item that required a fix and the low-context-pass result.
