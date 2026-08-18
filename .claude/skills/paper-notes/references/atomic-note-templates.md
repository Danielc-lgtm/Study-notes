# Atomic Note Templates

Two kinds of atomic note come out of a paper backchain, and both live **in the paper's own folder** `Study notes/paper/[Short Title]/`, alongside the hub and section pages:

1. **Prerequisite notes** — atomic notes for above-floor concepts the paper leans on that the vault does not already have.
2. **Paper-item subpages** — one subpage per named item in the paper (Def X, Thm X, Lemma X, Cor X, Prop X, Remark X, Ex X). Every named item gets its own file, so a reader can jump into any one cold.

Both kinds are **fully self-contained**: their own Notation with `> [!recall]-` callouts for every above-floor term they use, their own formal statement, their own intuition, their own gap-free proof or worked case. A reader who lands on the file through Obsidian search or a wikilink from elsewhere in the vault must be able to read and check it without opening any other file.

`Lemma -`, `Cor -`, `Prop -`, `Remark -` are new atomic types in this vault. Structure `Lemma -`/`Cor -`/`Prop -` exactly like `Thm -` (statement-first, then intuition, then proof), scaled to the item's weight. Structure `Remark -` as statement + intuition + short explanation, no full proof apparatus. Structure `Ex -` (paper examples, not exercises) as statement + computation + calibration.

---

## Part 1 — Prerequisite atomic notes (above-floor concepts)

Concepts the paper uses that live **above the floor** and have **no existing vault note** (Rule 1). Create them **in this paper's own folder**, `Study notes/paper/[Short Title]/`.

**Placement — one flat folder per paper.**
- absolute continuity of measures → `Study notes/paper/[Short Title]/Def - Absolute Continuity of Measures.md`
- Radon–Nikodym theorem → `Study notes/paper/[Short Title]/Thm - Radon–Nikodym Theorem.md`

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
> [Gap-free proof (Rule 5) if short or illuminating, in the thesis's labelled-step style. Otherwise: a proof sketch with the key idea, and cite a full source — and say which. Verify against a source (Rule 6).]

---

# Where the paper uses this

**[[Paper - [Short Title]]]**, §N.

---

# Verified against

[Source; flag uncertainty with ⚠️.]
```

---

## Part 2 — Paper-item subpages

**Every named item in the paper is its own subpage** in `Study notes/paper/[Short Title]/`. The paper's own Definitions, Theorems, Lemmas, Corollaries, Propositions, Remarks, and Examples each get a file. Naming uses the concept's name, not the paper number (`Thm - Homotopy Decomposition for Hyperbolic Surfaces`, not `Thm - Theorem 3.2`), so the file is a usable wikilink target. The paper number lives in the YAML `paper-ref` field.

Each subpage is **fully self-contained**: it can be opened cold, without reading any section page or any other subpage. That means:

- **Its own Notation section** — every symbol it uses, typed; every above-floor term recalled with a `> [!recall]-` callout carrying formal statement + plain-language meaning.
- **Its own formal Statement** — the paper's exact statement, typed.
- **Its own Motivation / Why-It's-True** — thesis-voice intuition, independent of the proof.
- **Its own Proof / Computation / Worked Example** — gap-free (Rule 5), in a `> [!note]-` collapsible. External inputs the proof invokes appear as `> [!cite]-` callouts inline.
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
> [The paper's proof rewritten with every step justified (Rule 5), in the thesis's labelled-step style. External lemmas appear as `> [!cite]-` callouts. If the paper's proof has a gap you filled, mark it with ⚠️.]

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

## Part 3 — Standalone-paragraph subpages

When the paper has a paragraph carrying a substantive argument or a definition-in-prose without a number, and that argument is **load-bearing** (a later item depends on it), promote it to a `Remark - [Descriptive Name].md` subpage. This preserves the argument as a greppable, wikilinkable, self-contained note. Non-load-bearing prose stays on the section page as part of the section opener or as inline commentary next to the concept-map bullet.

Descriptive-name examples:
- `Remark - Bosonic Partition Function Interpretation.md` (the paper's Remark 4.4)
- `Remark - Range of Killing Rate.md` (the paper's Remark 3.7)
- `Remark - Motivation for the Path-Integral Digression.md` (an unnumbered load-bearing paragraph opening a section)

---

## Placement summary

| Note | Lives in | Full or scoped |
|---|---|---|
| Prerequisite `Def -`/`Thm -`/`Lemma -` (new) | this paper's folder | full (scaled to need) |
| Prerequisite that already exists in the vault | wherever it already is — **wikilinked, not copied** | (reused as-is) |
| Paper-item `Def -`/`Thm -`/`Lemma -`/`Cor -`/`Prop -`/`Remark -`/`Ex -` subpage | this paper's folder | one per named item, self-contained |
| Section page (concept-map index) | this paper's folder | one per paper section |
| Hub page | this paper's folder | one per paper |

Everything newly created for the paper lives in the one folder `Study notes/paper/[Short Title]/`. Every atomic subpage carries a `source:` field naming the paper, a `paper-ref:` field naming the paper number, and a "Where the paper uses this" link, so the DAG is navigable both ways. Forward references to concepts with no page yet are **bold plain text**, never wikilinks.
