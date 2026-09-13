# Atomic Note Templates

Two kinds of atomic note come out of a paper backchain, and both live **in the paper's own folder** `Study notes/paper/[Short Title]/Subpages/`, alongside the hub and section pages:

1. **Prerequisite notes** — atomic notes for above-floor concepts the paper leans on that the vault does not already have.
2. **Paper-item subpages** — one subpage per named item in the paper (Def X, Thm X, Lemma X, Cor X, Prop X, Remark X, Ex X). Every named item gets its own file, so a reader can jump into any one cold.

Both kinds are **fully self-contained**: their own Notation with `> [!recall]-` callouts for every above-floor term they use, their own formal statement, their own intuition, their own gap-free proof or worked case. A reader who lands on the file through Obsidian search or a wikilink from elsewhere in the vault must be able to read and check it without opening any other file.

`Lemma -`, `Cor -`, `Prop -`, `Remark -` are new atomic types in this vault. Structure `Lemma -`/`Cor -`/`Prop -` exactly like `Thm -` (statement-first, then intuition, then proof), scaled to the item's weight. Structure `Remark -` as statement + intuition + short explanation, no full proof apparatus. Structure `Ex -` (paper examples, not exercises) as statement + computation + calibration.

---

## Part 1 — Prerequisite atomic notes (above-floor concepts)

Concepts the paper uses that live **above the floor** and have **no existing vault note** (Rule 1). Create them **in this paper's own folder**, `Study notes/paper/[Short Title]/Subpages/`.

**Placement — one flat folder per paper.**
- absolute continuity of measures → `Study notes/paper/[Short Title]/Subpages/Def - Absolute Continuity of Measures.md`
- Radon–Nikodym theorem → `Study notes/paper/[Short Title]/Subpages/Thm - Radon–Nikodym Theorem.md`

**The one exception — reuse, do not duplicate.** Search the vault first (`grep`/`find` over `Study notes/`). If a note exists **anywhere** — subject folder or another paper's folder — **wikilink it instead of copying**. Only concepts the vault does not yet cover get a new note here.

Scale each prerequisite note to the paper's needs (Rule 1). A concept whose properties are hammered on gets the full apparatus. A single-mention term gets a scoped stub carrying only the fact the paper uses. Cluster tightly-related prerequisites into one compound note.

### Prerequisite definition note

```markdown
---
type: definition
subject: [subject-slug]
prereqs:
  - "Def - [floor-or-existing dependency]"
tags: [area-tag, subject-tag, paper-prereq]
source: "[paper Short Title]"
---

# Notation

[Symbols this definition needs, each typed (notation-discipline.md). Recall any above-floor prerequisite of the definition itself with a `> [!recall]-` callout, so the page stands alone.]

---

# Axiom Motivation

[Thesis-voice, intuition-first: what problem does this object solve, what should it capture and exclude, why this definition and not a variant. For a definition with n ≥ 2 conditions, do per-condition failure analysis. A few paragraphs is fine; do not balloon a prerequisite into a chapter.]

---

# The Definition

> **Definition ([standard name]).** [Formal statement, fully typed. Note standard equivalent formulations.]

[Unpack in the smallest concrete instance, thesis-style.]

**Standard names.** [Literature's name + alternate names (Rule 4).]

---

# Examples and Non-Examples

[At least one "is an instance" and one "is NOT". Close with a `**Calibration check.**` line: a small verification the reader can perform.]

---

# Where the paper uses this

[Which paper result needs this concept, wikilinked to the relevant section page and item subpage. **[[Paper - [Short Title]]]**, §N.]

---

# Verified against

[Source (Rule 6); flag uncertainty with ⚠️.]
```

### Prerequisite theorem / lemma note

```markdown
---
type: theorem            # or: lemma
subject: [subject-slug]
prereqs:
  - "Def - [dependency]"
tags: [area-tag, subject-tag, paper-prereq]
source: "[paper Short Title]"
---

# Notation

[Symbols, typed. Recall above-floor prerequisites.]

---

# Statement

> **Theorem ([standard name]).** [Hypotheses typed and quantified; conclusion. One block. Use `> **Lemma ([name]).**` for a lemma.]

---

# Why It's True

[Thesis-voice intuition, independent of the proof. One-sentence mechanism summary in bold.]

---

# Proof

> [!note]- Proof
> [The complete proof (Rule 5), at or above the thesis floor — `prose-and-proof-standard.md` §6: named assumptions and goal, labelled blocks with bold lead-ins, a justification on every displayed line, every hypothesis invoked by name, all directions and cases, a closing sentence. Never a sketch: a prerequisite note exists precisely so that the result it states is *proved* somewhere in the vault. Results it uses in turn are wikilinked to pages with complete proofs. Verify against a source (Rule 6) and cite it.]

---

# Where the paper uses this

**[[Paper - [Short Title]]]**, §N.

---

# Verified against

[Source; flag uncertainty with ⚠️.]
```

---

## Part 2 — Paper-item subpages

**Every named item in the paper is its own subpage** in `Study notes/paper/[Short Title]/Subpages/`. The paper's own Definitions, Theorems, Lemmas, Corollaries, Propositions, Remarks, and Examples each get a file. Naming uses the concept's name, not the paper number (`Thm - Homotopy Decomposition for Hyperbolic Surfaces`, not `Thm - Theorem 3.2`), so the file is a usable wikilink target. The paper number lives in the YAML `paper-ref` field.

Each subpage is **fully self-contained**: it can be opened cold, without reading any section page or any other subpage. That means:

- **Its own Notation section** — every symbol it uses, typed; every above-floor term recalled with a `> [!recall]-` callout carrying formal statement + plain-language meaning.
- **Its own formal Statement** — the paper's exact statement, typed.
- **Its own Motivation / Why-It's-True** — thesis-voice intuition, independent of the proof.
- **Its own Proof / Computation / Worked Example** — gap-free (Rule 5) and at the thesis floor, in a `> [!note]-` collapsible. External inputs the proof invokes appear as `> [!cite]-` callouts inline, each linked to the atomic page (or existing vault page) where that input is proved in full.
- **Where the paper uses this** — a link back to the section page and to any downstream results, so the DAG is navigable both ways.

**Scale to the item.** A theorem that carries a section gets the full apparatus (Motivation → Why-It's-True → Rederivation Scaffold → Formal Proof). A remark that is one paragraph in the paper gets a short subpage (Notation → Statement → Intuition → one link). Match the item's weight, do not pad.

**Skip polymath-only sections.** No Convergent Strategies, no Sources-and-Targets in the polymath sense, no Bridges, no Legal Operations, no Cross-Field Exercise Suggestions — those belong to `polymath-notes`/`exercise-builder`. Paper-item subpages are lighter than polymath topic-page subpages; the goal is de-jargoning and self-containment, not the polymath spaced-retrieval apparatus.

### Paper-item definition subpage

```markdown
---
type: definition
subject: [primary-field-slug]
prereqs:
  - "Def - [above-floor dependency, linked to its atomic note]"
tags: [paper, primary-field-tag]
source: "[paper Short Title]"
paper-ref: "Definition [paper's number]"
---

# Notation

[Every symbol this definition uses, typed. Recall every above-floor term with a `> [!recall]-` callout so the page stands alone.]

> [!recall]- [Above-floor term A]
> **Formally:** [precise statement, typed]
> **In words:** [plain-language meaning] See [[Def - term A]].

---

# Statement

> **Definition ([paper's name for it], paper's number).** [The formal statement, fully typed. Attribute to the paper: "introduced by the authors as …" If there is a standard literature name (Rule 4), give that too; if genuinely novel, say so.]

---

# In One Line

[The plain-language what-and-why — one or two sentences that recognise the object.]

---

# Motivation and Unpacking

[Thesis-voice: why the paper introduces this, what problem it solves, what the alternative variants would give. Then unpack in the smallest concrete instance the paper considers or that a reader can compute.]

---

# Where the paper uses this

Introduced in [[Paper - [Short Title] — §N [Section]|§N]]; downstream in [[Thm - …]], [[Cor - …]], …
```

### Paper-item theorem / lemma / corollary / proposition subpage

```markdown
---
type: theorem            # or: lemma / corollary / proposition
subject: [primary-field-slug]
prereqs:
  - "Def - [paper object, linked to its subpage]"
  - "Thm - [above-floor dependency, linked to its atomic note]"
tags: [paper, primary-field-tag]
source: "[paper Short Title]"
paper-ref: "Theorem [paper's number]"
---

# Notation

[Symbols, typed. Recall every above-floor term used in the Statement / Proof with a `> [!recall]-` callout.]

---

# Statement

> **Theorem ([paper's name / paper-ref]).** [Hypotheses typed and quantified; conclusion. One block.]

---

# In One Line

[What the theorem buys, in plain words — the mechanism in a sentence.]

---

# Why It's True

[Thesis-voice intuition, independent of the proof. One-sentence mechanism summary in bold.]

---

# Proof

> [!note]- Gap-free proof
> [The paper's proof rewritten with every step justified (Rule 5), at or above the thesis floor (`prose-and-proof-standard.md` §6). External results appear as `> [!cite]-` callouts, each pointing at an atomic page (or an existing vault page) where that result is proved in full. If the paper's proof has a gap you filled, mark it with ⚠️.]

---

# Where the paper uses this

Introduced in [[Paper - [Short Title] — §N [Section]|§N]]; used in [[Thm - …]], [[Cor - …]], …
```

### Paper-item Remark subpage

```markdown
---
type: remark
subject: [primary-field-slug]
prereqs:
  - "…"
tags: [paper, primary-field-tag]
source: "[paper Short Title]"
paper-ref: "Remark [paper's number]"
---

# Statement

> **Remark ([paper-ref]).** [The remark's content in the paper's own words, or a faithful paraphrase.]

---

# In One Line

[What the remark observes, in one plain sentence.]

---

# Unpacking

[Thesis-voice: what the remark points at, why it matters, what it warns against or invites. Recall any above-floor term with a `> [!recall]-` callout so the page stands alone. If the remark carries a small argument (a short computation, a comparison, a re-derivation), include it here in full — the point of the subpage is that the argument is preserved and greppable.]

---

# Where the paper uses this

[Section link, and any downstream item that leans on the remark.]
```

### Paper-item Example subpage

```markdown
---
type: example
subject: [primary-field-slug]
prereqs:
  - "…"
tags: [paper, primary-field-tag]
source: "[paper Short Title]"
paper-ref: "Example [paper's number]"
---

# Statement

> **Example ([paper-ref]).** [The specific instance the paper works out, fully typed.]

---

# Computation

[The full worked case, gap-free. If the paper elides a step, fill it and flag with ⚠️ if unsure.]

---

# Calibration

[What this example calibrates: which invariant it checks, which parameter regime it probes, which alternative it rules out. One or two sentences.]

---

# Where the paper uses this

[Section link, and any downstream item that leans on this example.]
```

---

## Part 3 — Load-bearing-paragraph subpages (mandatory)

**Every paragraph the paper argues for gets its own subpage.** The section pages are indices — they *link* to arguments, they never *carry* them. So whenever the paper devotes more than a sentence to *establishing* a fact rather than *stating* it, that argument is promoted to its own `Remark - [Descriptive Name].md` subpage in `Subpages/`, and the section page's concept map gets one more foldable bullet pointing at it.

### The test for load-bearing

Not every paragraph is load-bearing. The test:

- Does the paragraph carry a **computation** the reader needs to follow (a change of variables, an integration by parts, an evaluation of a limit, a coset enumeration)? → Load-bearing.
- Does it carry an **identification** of one object with another (this sum equals that integral; this random-walk semigroup is that operator; this loop-mass integral is that Selberg zeta value)? → Load-bearing.
- Does it establish an **invariance property** the later argument depends on (Γ-invariance of a kernel, ⟨τ⟩-invariance of an integrand, conformal invariance of a measure)? → Load-bearing.
- Does it walk a **dictionary between two languages** (Wick rotation between quantum and diffusion; abelianisation between fundamental group and homology; Poincaré series ↔ orbit growth)? → Load-bearing.
- Does it establish a **descent / periodisation construction** (downstairs kernel = sum over the group of upstairs kernel; class-mass isolated by restricting the periodisation to one conjugacy class)? → Load-bearing.

Compare to non-load-bearing prose: pure section-opener text ("we now turn to §5.2, the cusped case"), one-line pointers ("recall §3.1's formula"), summary sentences at the end of a section. These stay on the section page.

**When in doubt, promote.** A promoted paragraph becomes a greppable, wikilinkable, self-contained note. A paragraph left inline on the section page is invisible outside its section and re-fills the section page with the very prose the concept-map format is meant to compress.

### Descriptive-name examples

Named paper remarks:
- `Remark - Bosonic Partition Function Interpretation.md` (the paper's Remark 4.4)
- `Remark - Range of Killing Rate.md` (the paper's Remark 3.7)

Unnumbered load-bearing paragraphs (from the reference Brownian-loops paper):
- `Remark - Descent of the Heat Kernel by Periodisation.md` — the paragraph identifying $p_X(t,z,w) = \sum_{h\in\Gamma} p_{\mathbb{H}^2}(t,\tilde z, h\tilde w)$ and explaining why this sum is *pre-sorted by homotopy class*.
- `Remark - Collapsing the Conjugacy Sum to One Strip.md` — the argument that the double structure "sum over $[\tau^m]_{\mathrm{conj}}$ × integrate over $X$" collapses to one integral over $\mathcal F_\tau$ via the centraliser $\langle\tau\rangle$.
- `Remark - Standard Form as Coordinates on the Axis.md` — the paragraph explaining why conjugating $\tau$ inside $\mathrm{PSL}(2,\mathbb{R})$ to $z\mapsto e^\ell z$ is the natural coordinate for the strip computation.
- `Remark - Wick Rotation Dictionary.md` — the paragraph translating quantum $e^{-it\hat H/\hbar}$ into diffusion $e^{-\tau\hat H/\hbar}$ under $t = -i\tau$.

### Template for a load-bearing-paragraph subpage

```markdown
---
type: remark
subject: [primary-field-slug]
prereqs:
  - "[whatever above-floor concepts the argument uses]"
tags: [paper, primary-field-tag]
source: "[paper Short Title]"
paper-ref: "unnumbered; §N — [short description of the paragraph]"
---

# Notation

[Every symbol the argument uses, typed. Three-field `> [!recall]-` for every above-floor term — same discipline as any other atomic subpage.]

---

# Claim / Identity

> **Claim (descriptive name).** [The precise statement the paragraph is arguing for — a specific identity, an equality of measures, a periodisation formula, whatever the paper's own prose established. Fully typed.]

---

# In One Line

[One or two plain-language sentences: what is being claimed and why it matters. Same discipline as the "In One Line" field on paper-item subpages.]

---

# Why It's True

[Thesis-voice intuition — the mental picture behind the argument, in bold at least one line of "mechanism in one sentence".]

---

# Derivation

> [!note]- Gap-free derivation
> [The paper's argument rewritten with every step justified (Rule 5). Labelled-step style — each move on its own line with its bolded lead-in.]

---

# Where the paper uses this

[Section link and downstream items. This paragraph is load-bearing precisely because a downstream result depends on it — name the dependency.]
```

---

## Placement summary

| Note | Lives in | Full or scoped |
|---|---|---|
| Prerequisite `Def -`/`Thm -`/`Lemma -` (new) | this paper's `Subpages/` folder | full (scaled to need) |
| Prerequisite that already exists in the vault | wherever it already is — **wikilinked, not copied** | (reused as-is) |
| Paper-item `Def -`/`Thm -`/`Lemma -`/`Cor -`/`Prop -`/`Remark -`/`Ex -` subpage | this paper's `Subpages/` folder | one per named item, self-contained |
| Load-bearing paragraph as `Remark - [Descriptive Name]` | this paper's `Subpages/` folder | one per argued paragraph, self-contained |
| Section page (concept-map index) | this paper's `Subpages/` folder | one per paper section |
| Whole-Paper Story page | this paper's `Subpages/` folder | one per paper (mandatory) |
| Index page | this paper's folder (top level) | one per paper |

Everything newly created for the paper lives in the one folder `Study notes/paper/[Short Title]/` — with the **index at the top of the folder** and every other page in the `Subpages/` subfolder beside it. Every atomic subpage carries a `source:` field naming the paper, a `paper-ref:` field (paper number for named items; `"unnumbered; §N — description"` for load-bearing paragraphs), and a "Where the paper uses this" link, so the DAG is navigable both ways. Forward references to concepts with no page yet are **bold plain text**, never wikilinks.
