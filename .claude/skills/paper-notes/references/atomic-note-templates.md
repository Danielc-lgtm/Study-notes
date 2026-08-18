# Atomic Note Templates

Two kinds of atomic note come out of a paper backchain: **prerequisite notes** and **paper-result stubs**. Both are newly created for the paper and both live **in the paper's own folder** `Study notes/paper/[Short Title]/`, alongside the companion page. Both reuse the vault's existing `Def -`/`Thm -` types and introduce a new `Lemma -` type. Follow `../polymath-notes/references/templates.md` for the full Def/Thm section structure and `obsidian-patterns.md` for syntax; the templates here are the paper-notes-specific shape and the placement rules.

`Lemma -` is a new atomic type in this vault. Structure it exactly like `Thm -` (statement-first, then intuition, then proof), just for a result that is auxiliary rather than headline. Use `Lemma -` for the paper's own auxiliary results and for named external lemmas the paper leans on that deserve a reusable page.

---

## Part 1 — Prerequisite atomic notes (in the paper folder)

A concept the paper uses that lives **above the floor** and has **no existing vault note** (Rule 1). Create it **in this paper's own folder**, `Study notes/paper/[Short Title]/`, alongside the companion page and the paper-result stubs. Everything newly created for the paper lives together in that one folder — the note-set is self-contained.

**Placement — one flat folder per paper.**

- absolute continuity of measures → `Study notes/paper/[Short Title]/Def - Absolute Continuity of Measures.md`
- Radon–Nikodym theorem → `Study notes/paper/[Short Title]/Thm - Radon–Nikodym Theorem.md`
- the spectral theorem for compact self-adjoint operators → `Study notes/paper/[Short Title]/Thm - Spectral Theorem for Compact Self-Adjoint Operators.md`

**The one exception — reuse, do not duplicate.** Before creating a prerequisite note, search the vault (`grep`/`find` over `Study notes/`) for an existing note on that concept. If one exists **anywhere** in the vault — in a subject folder, or in another paper's folder — **wikilink it from the recall instead of copying it into this paper's folder**. Only concepts the vault does not yet cover get a new note here. (This replaces the earlier convention of scattering prerequisite notes into subject-area folders; new notes are now paper-local, so one paper is one folder.)

These notes follow the `polymath-notes` Def/Thm structure, **scaled to what the paper needs**: enough that the concept is fully usable and correctly typed, without necessarily the full topic-page apparatus (no exercises, no legal-operations section — those belong to `polymath-notes`/`exercise-builder`). A single-mention, non-load-bearing term may not warrant a full note at all — a point-of-use recall (or a scoped stub carrying only the fact the paper uses) suffices; reserve the full apparatus below for concepts whose properties the proofs actually lean on, and cluster tightly-related prerequisites into one compound note rather than many tiny ones (Rule 1). Write them in the thesis voice (motivate, state formally, then unpack concretely). Verify from a source and cite it (Rule 6).

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

[The symbols this definition needs, each typed (notation-discipline.md). A brief list or paragraph — the reader may land here cold from a recall callout.]

---

# Axiom Motivation

[Thesis-voice, intuition-first: what problem does this object solve, what should it capture and exclude, why this definition and not a nearby variant. For a definition with two or more independent conditions, say what breaks if each is dropped (a concrete counterexample), as in the polymath Def template. Aim for a few paragraphs — enough that a floor-level reader could have invented the definition. Keep to what the paper actually leans on; do not balloon a prerequisite into a full chapter.]

---

# The Definition

> **Definition ([standard name]).** [The formal statement, fully typed. State the primary form; note standard equivalent formulations in a sentence.]

[Then unpack it in the smallest concrete instance, thesis-style.]

**Standard names.** [Attribute the term and give alternate names across subfields (Rule 4): "the Radon–Nikodym derivative, also called the density of $\mu$ with respect to $\nu$."]

---

# Examples and Non-Examples

[At least one "is an instance" and one "is NOT an instance", each probing a different part of the definition. Prose paragraphs. Close with a one-line calibration check: a small verification the reader can do if they understood it.]

---

# Where the paper uses this

[One or two sentences: which result in the paper needs this concept, and link back to the companion page section. This is the paper-prereq's tie to its origin — keep it short. **[[Paper - [Short Title]]]**, §N.]

---

# Verified against

[The source you confirmed the definition against (Rule 6). "Folland, *Real Analysis*, §3.2." If anything is uncertain, flag it with the ⚠️ marker.]
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

[Symbols, typed.]

---

# Statement

> **Theorem ([standard name]).** [Hypotheses, each typed and quantified; then the conclusion. One block. Use `> **Lemma ([name]).**` for a lemma.]

---

# Why It's True

[Thesis-voice intuition for why to expect the result, independent of the proof. Include a one-sentence mechanism summary in bold.]

---

# Proof

> [!note]- Proof
> [A gap-free proof (Rule 5) if it is short or illuminating, in the thesis's labelled-step style. If the standard proof is long and not illuminating for the paper's purposes, give a proof sketch with the key idea and cite a full source — and say which you did. Verify the statement and proof against a source (Rule 6).]

---

# Where the paper uses this

[Which paper result invokes it, linked back to the companion page. **[[Paper - [Short Title]]]**, §N.]

---

# Verified against

[Source (Rule 6); flag any uncertainty with ⚠️.]
```

---

## Part 2 — Paper-result stub notes

For the paper's **own** principal definitions and theorems. These make the paper's results reusable and greppable across the vault **without duplicating the full exposition** — the full treatment (motivation, gap-free proof, recalls) lives in the companion page; the stub carries the formal statement, its typing, and a one-line intuition, then links back.

Placement: **in the paper folder**, `Study notes/paper/[Short Title]/Def - [Name].md` (or `Thm -`, `Lemma -`). Naming uses the concept's name, not the paper's number, so it is a usable wikilink target (`Def - Interaction Hypergraph`, not `Def - Definition 3.2`).

### Paper definition stub

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

# Statement

> **Definition ([paper's name for it]).** [The formal statement, fully typed. Attribute it to the paper: "introduced by the authors as …". If the concept has a standard name from the wider literature, give that too (Rule 4); if it is genuinely novel, say so.]

**In one line.** [The plain-language what-and-why — the intuition a reader needs to recognise the object. One or two sentences.]

**Full treatment:** [[Paper - [Short Title]]], §N — motivation, the concrete unpacking, and how it is used.

[Recall any above-floor term the statement uses, with a `[!recall]-` or a link to its atomic note, so the stub is self-sufficient.]
```

### Paper theorem / lemma stub

```markdown
---
type: theorem            # or: lemma
subject: [primary-field-slug]
prereqs:
  - "Def - [paper object, linked to its stub]"
  - "Thm - [above-floor dependency, linked to its atomic note]"
tags: [paper, primary-field-tag]
source: "[paper Short Title]"
paper-ref: "Theorem [paper's number]"
---

# Statement

> **Theorem ([paper's name / paper-ref]).** [Hypotheses typed and quantified; conclusion. One block.]

**In one line.** [What the theorem buys, in plain words — the mechanism in a sentence.]

**Full treatment and gap-free proof:** [[Paper - [Short Title]]], §N.

[Recall or link every above-floor term in the statement so the stub stands alone.]
```

---

## Placement summary

| Note | Lives in | Full or stub |
|---|---|---|
| Prerequisite `Def -`/`Thm -`/`Lemma -` (new) | this paper's folder (`Study notes/paper/[Short Title]/`) | full (scaled to need) |
| Prerequisite that already exists in the vault | wherever it already is — **wikilinked, not copied** | (reused as-is) |
| Paper's own `Def -`/`Thm -`/`Lemma -` | this paper's folder (`Study notes/paper/[Short Title]/`) | stub → links to companion |
| Companion page | this paper's folder (`Study notes/paper/[Short Title]/`) | full walk-through |

Everything newly created for the paper lives in the one folder `Study notes/paper/[Short Title]/`. Every atomic note carries a `source:` field naming the paper, and a "Where the paper uses this" / "Full treatment" link back, so the backchain is navigable in both directions. Forward references to concepts with no page yet are **bold plain text**, never wikilinks.
