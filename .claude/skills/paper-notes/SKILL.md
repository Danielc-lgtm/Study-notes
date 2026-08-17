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

The deliverable is a **companion page** that walks the paper section by section — carrying the paper's own definitions and theorems, point-of-use recalls for everything unfamiliar, and gap-free proofs — plus **atomic `Def -`/`Thm -`/`Lemma -` notes** for every prerequisite above the floor and reusable **stub notes** for the paper's own principal results, all wikilinked into the vault so the paper's machinery cross-links with the existing study notes.

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

- **If a note already exists in the vault** covering that concept, wikilink it from the recall. Search the vault first (`grep`/`find` over `Study notes/`) — the vault already has deep Measure Theory, Advanced Probability, Functional-Analysis-flavoured Linear Algebra, Differential Geometry, Topology, Group/Ring/Module theory, and more; reuse it. **But an existing note is written for the vault owner's specialist background (see `CLAUDE.md`) and is usually *not* floor-legible** — so linking it is not enough: the point-of-use recall must still carry the full floor-level content, and if that note's *own* machinery is above the floor and the proof leans on it, those sub-concepts get their own recalls too, so the companion page bottoms out at the floor even though the linked note does not.
- **If no note exists,** create an atomic `Def -`, `Thm -`, or `Lemma -` note for it (template in `references/atomic-note-templates.md`), placed **in its natural subject-area folder, nested under a topic-page subfolder exactly as the vault stores every leaf note** — e.g. a Radon–Nikodym note at `Study notes/Probability/Measure Theory/[Topic]/Thm - Radon–Nikodym Theorem.md`, never bare under the subject folder. If the field has no host topic page, create a topic-page subfolder for it (a minimal topic page, or a catch-all such as `Prerequisites from [Short Title]/`). If the field is not represented at all (e.g. the vault has no Hyperbolic Geometry folder), create the `[Area]/[Subject]/[Topic]/` chain. These notes are **vault assets, not paper-local**: they live in the subject hierarchy, not the paper's folder, because the next paper will reuse them. Full placement rules and the new-field case: `references/atomic-note-templates.md`.
- **Scale the durable note to how load-bearing the concept is.** A concept whose *properties are actually used* in a reasoning step the reader must follow gets a full atomic note (with the axiom-motivation / statement apparatus of the template). A concept that is mentioned once and only in passing needs the point-of-use recall alone — or at most a scoped stub carrying only the one fact the paper uses — not a full stand-alone note. Cluster tightly-related prerequisites into a single compound atomic note (as `polymath-notes` does with compound definition pages) rather than spawning many tiny notes. The recall coverage is exhaustive; the *note* granularity is proportional to use.
- **Then recurse on each new note's own prerequisites.** A Radon–Nikodym note needs absolute continuity of measures and the notion of a $\sigma$-finite measure; each of those, if above the floor and not yet in the vault, gets its own atomic note, until every leaf bottoms out at the floor. The backchain terminates because the floor is fixed and finite.

Build the backchain as an explicit per-section prerequisite list during Pass 1 (Procedure below), so Pass 2 writes the atomic notes before the companion section that needs them.

`prereq-backchain` backchains a *subject* to plan study; this skill backchains a *paper* until every step reads without leaving the page.

### Rule 2 — Recall every unfamiliar term at its point of use

Whenever the paper (or your own exposition) uses a term or notation that is above the floor, insert a collapsible recall **right where it is used** — not only a wikilink to its atomic note. The recall gives **both** the formal definition **and** a plain-language statement of what it means or does:

```markdown
> [!recall]- Absolutely continuous (μ ≪ ν)
> **Formally:** for measures $\mu, \nu$ on a measurable space $(X, \mathcal{F})$, $\mu$ is absolutely continuous with respect to $\nu$, written $\mu \ll \nu$, if every $\nu$-null set is $\mu$-null: $\nu(A) = 0 \Rightarrow \mu(A) = 0$ for all $A \in \mathcal{F}$.
> **In words:** $\nu$ cannot be blind to anything $\mu$ sees — wherever $\mu$ puts mass, $\nu$ already puts some. This is exactly the condition under which $\mu$ has a density with respect to $\nu$ (the Radon–Nikodym derivative). See [[Def - Absolute Continuity of Measures]].
```

The recall is collapsed (`-`) so a reader who knows the term is not slowed, and one click away for a reader who does not. Full callout catalogue — recall, external-input, uncertainty — in `references/recall-callouts.md`. The wikilink to the atomic note goes *inside* the recall (or right after it); the recall itself must be self-sufficient, so a reader who never clicks the link still gets both the formal content and the intuition. Duplicate a recall freely at each new section that uses the term — a collapsed one-liner is cheaper to re-read than to hunt down.

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

For one paper, the note-set has three kinds of page. All live under a single paper folder except the reusable prerequisite notes, which live in the subject hierarchy.

### 1. The companion page (the reading surface)

`Study notes/Papers/[Short Title]/Paper - [Short Title].md` — walks the paper section by section in the thesis voice, carrying the point-of-use recalls and the gap-free proofs. This is the page a reader opens to read the whole paper. Skeleton in `references/companion-page-template.md`. It opens with a header (full citation, plain-language abstract, the explicit floor statement), a **Notation and Standing Conventions** section (Rule 3), and a **Prerequisites** map (the backchain — every above-floor concept wikilinked to its atomic note), then one section per paper section, then **External inputs** and the **Verification log**.

**For a long paper, split the reading surface** into one page per paper section — `Paper - [Short Title] — §N [Section].md` — with `Paper - [Short Title].md` as a short hub that carries the header, the Notation and Standing Conventions table, the prerequisites map, a table of contents linking the section pages in order, and the **Verification log** (so Rule 6's honesty record still has a home in a split note-set). Split only at the paper's own section boundaries, exactly as `polymath-notes` splits a topic page at sub-chapter boundaries. Default to the single page; split when a single file would become unwieldy.

### 2. Atomic prerequisite notes (vault assets)

`Def -`/`Thm -`/`Lemma -` notes for every above-floor concept the paper uses that the vault does not already have, each in its **natural subject-area folder** (Rule 1), following the atomic-note template. These follow the `polymath-notes` Def/Thm structure (Notation → Axiom Motivation / Statement → the formal content → intuition → examples), scaled to what the paper needs — enough that the concept is fully usable and cross-links with existing study notes, without necessarily the full topic-page apparatus. `Lemma -` is a new atomic type, structured like `Thm -` (see the template). Reuse an existing vault note wherever one exists rather than duplicating it.

### 3. Paper-result stub notes

`Def -`/`Thm -`/`Lemma -` notes for the paper's *own* principal definitions and theorems, placed **in the paper folder** `Study notes/Papers/[Short Title]/`, each giving the formal statement, its typing, and a one-line intuition, then linking back to the companion page for the full treatment (motivation, gap-free proof, recalls). These make the paper's results reusable and greppable across the vault without duplicating the full exposition. Stub template in `references/atomic-note-templates.md`.

**Wikilink everything.** Every above-floor term in the companion page links to its atomic note; every paper result links to its stub; every stub and atomic note links back appropriately. Follow the vault's actual folder conventions (`obsidian-patterns.md`). Forward references to concepts with no page yet are **bold plain text**, never wikilinks (an unresolved `[[ ]]` creates an empty stub when clicked).

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

1. **Floor respected.** The companion page states the floor explicitly, and nothing above the floor is used without being either recalled (Rule 2) or created as an atomic note and linked. Pick two sections and read them as a floor-level reader: no unexpanded term survives.
2. **Recall coverage.** Every above-floor term in a statement or proof has a point-of-use `[!recall]-` (or an atomic note linked with a one-line reminder) giving *both* formal content and plain-language meaning. Grep the section for the above-floor term list from Pass 1; each occurrence is covered.
3. **Backchain terminates at the floor.** Every atomic note's own prerequisites are either floor-level or themselves have atomic notes; no atomic note leaves a dangling above-floor dependency.

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

10. **Output structure.** The companion page exists at `Study notes/Papers/[Short Title]/Paper - [Short Title].md` (or a hub + section pages for a long paper); atomic prerequisite notes are in their natural subject folders; paper-result stubs are in the paper folder and link back to the companion.
11. **Low-context pass done.** Pass 3 was run and its findings fixed.
12. **Mechanics clean.** Math is `$...$`/`$$...$$`; no LaTeX inside `[[ ]]`; every wikilink resolves; filenames are Windows-portable (`< > : " / \ | ? *` all avoided; `§`, `—`, and Unicode math are fine); `find-math-bugs.py`, `find-latex-bugs.py`, `find-wikilink-bugs.py` and the resolution audit come back clean.

**Report** as: "Paper-notes self-check: N of 12 verified", plus any item that required a fix and the low-context-pass result.
