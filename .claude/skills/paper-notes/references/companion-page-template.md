# Companion Page Template — index + story + section indices

The paper's reading surface has three layers: an **index page** at the top of the paper folder (front door), a **Whole-Paper Story page** in `Subpages/` (a single coherent narrative — the primary reading deliverable), and **one section page per paper section** in `Subpages/` (polymath-style concept-map indices linking to atomic subpages). Every named paper item and every load-bearing paragraph gets its own atomic subpage (see `atomic-note-templates.md`).

The index is short scaffolding — it names the paper, links prominently to the Whole-Paper Story, and lists the section pages. The Whole-Paper Story is the *reading experience* — a reader who wants to understand the paper reads it top to bottom. The section pages are for looking things up and for depth — big-picture indices that click through to atomic subpages.

Follow `notation-discipline.md` for typing and terminology, `recall-callouts.md` for the callouts, and the reference thesis for the prose voice. Every subpage is written intuition-first, then formal, then unpacked in a concrete case (the Prose Standard in SKILL.md).

Filename pattern (**index at the top of the folder, everything else in `Subpages/`**):
- Index: `Study notes/paper/[Short Title]/Paper - [Short Title].md`
- Story: `Study notes/paper/[Short Title]/Subpages/Paper - [Short Title] — Whole-Paper Story.md`
- Section: `Study notes/paper/[Short Title]/Subpages/Paper - [Short Title] — §N [Section].md`

Obsidian resolves wikilinks by filename regardless of subfolder, so cross-links across the index/Subpages split still work with bare `[[Filename]]` targets.

The `[Short Title]` is a few words identifying the paper (Windows-portable: no `< > : " / \ | ? *`).

---

## Index page template (at the top of the folder)

```markdown
---
type: paper
paper: "[Full citation: Authors, Title, venue, year]"
authors: [Author One, Author Two]
subject: [primary-field-slug]
tags: [paper, primary-field-tag, secondary-field-tag]
---

# Paper — [Short Title]

> [!tip] Whole-paper story — read this first
> **[[Paper - [Short Title] — Whole-Paper Story|The whole paper as one connected story]]** — a single top-to-bottom narrative with mental pictures at every step, in the voice of `paper_source/example.md`. If you are here to understand the paper (rather than look up a specific theorem), start there.

> [!abstract] What this paper does
> [A one-to-two-paragraph plain-language account, thesis voice: what problem it addresses, what it establishes, why that matters. State it so a floor-level reader understands the point of the paper before any machinery appears.]

**Citation.** [Full citation, with a link or DOI if available.]

**The floor.** These notes assume only undergraduate analysis, linear algebra, and elementary probability. Everything above that floor is recalled at its point of use or written out in a linked atomic note; every proof is rewritten so that each step is checkable without leaving the page.

**How to read this.** Three entry modes:
- **Story:** read the [[Paper - [Short Title] — Whole-Paper Story|Whole-Paper Story]] top to bottom.
- **Big-picture:** open a section page below — every named item and every load-bearing argument appears as one foldable bullet with statement + short unpacking.
- **Detail:** click into any atomic subpage from a section page — full proof, motivation, and recalls; self-contained cold.

Every section page is **modularly self-contained** — you can open §5 without reading §2–§4.

---

# Notation and Standing Conventions

[The paper-wide signature table (notation-discipline.md, Rule 3): every symbol used in more than one section, with its full type and its meaning. Standing conventions (units, sign, default assumption) go in a preamble paragraph above the table. Section-local symbols live on the section page or on the atomic subpage that introduces them.]

| Symbol | Type | Meaning |
|---|---|---|
| ... | ... | ... |

---

# Prerequisites (backchained to the floor)

[The backchain map (Rule 1): a wikilinked list of every above-floor concept, grouped by field, each with a one-line reminder. Concepts with existing vault notes link to them; concepts you created an atomic note for link to the new note.]

**From measure-theoretic probability.** [[Def - Absolute Continuity of Measures|absolute continuity]] ($\mu \ll \nu$ — wherever $\mu$ has mass, $\nu$ does too), [[Thm - Radon–Nikodym Theorem|the Radon–Nikodym theorem]] (an absolutely continuous measure has a density), …

**From [field].** [[Def - ...]] (one-line reminder), …

---

# Sections

- **[[Paper - [Short Title] — §1 [Title]|§1 — [Title]]]** — one-line description of what the section does.
- **[[Paper - [Short Title] — §2 [Title]|§2 — [Title]]]** — …
- …

---

# External inputs

[Consolidated list of every result the paper imports without proof — each as an external-input callout with statement, type, intuition, and source. Optional if there are only one or two.]

---

# Verification log

[The paper-wide honesty record (Rule 6). Three lists — Verified, Flagged / uncertain, Intuition not yet formalised. Merges the per-section verification logs from every section page.]
```

---

## Whole-Paper Story page template (mandatory; in `Subpages/`)

Filename: `Subpages/Paper - [Short Title] — Whole-Paper Story.md`.

**The exemplar is `paper_source/example.md`.** Read it end to end before writing. The template below records the structural elements; it does not substitute for reading the exemplar's prose voice.

```markdown
---
type: paper-story
paper: "[Full citation]"
tags: [paper, primary-field-tag, story]
---

# [Short Title] — the whole paper as one connected story

[**One opening paragraph in the exemplar's voice.** Announce the frame: "Here's the whole mental picture as one connected story. I'll keep it in ordinary language, pull in symbols only where they're carrying weight, and make each of your [N] pieces flow into the next — because they really are one chain, not [N] facts." Adapt the phrasing to the paper; keep the *promise* — one narrative, mental pictures over machinery, connective sentences between sections.]

## 1. [Section 1's job, phrased as the story-step it plays]

[The first section walked as prose. Every named object gets a mental picture in the sentence that introduces it. Symbols only where they carry weight (a computation, a specific formula). Argue every construction the paper argues for; don't state facts. Close with the connective sentence that carries the reader into §2 — name the mechanism, not the section number.]

## 2. [Section 2's job — phrased so §1's story-step motivates §2's]

[…]

## 3. [continues, one section per level-2 header, in the paper's order …]

[Every paper section appears in some level-2 header of the story. Do not skip. Do not summarise the section as a bullet list — write it as a paragraph, or several, in prose. Where the paper walks a construction the reader must feel the mechanism of, walk it in the story too (see the exemplar's §4 "Descent = summing over the group (periodisation)" paragraph — a whole construction laid out step by step in the story's own voice).]

[**Sprinkle "one-line versions to hold onto"** where useful — the exemplar's "based loop = element; free loop = conjugacy class; the difference between them = the freedom to move the basepoint = conjugation; the invariant that survives = the geodesic length." One per section is roughly right.]

## [N+1]. [If the paper has a coordinate/convention section — "Standard form" in the exemplar — walk it as its own step.]

## The whole picture in one paragraph

[A single dense paragraph that folds the entire paper into one continuous sentence-chain — the paper's whole story compressed to what a reader can carry away in their head. This is the payoff. See the exemplar's final paragraph.]
```

**Coverage.** Every paper section appears in the story. Every named theorem and every load-bearing paragraph the paper makes a fuss over appears as a *character in the narrative* — walked as prose with a mental picture, not merely mentioned as "see [[Thm - X]]". Wikilink every named item you mention (so a reader wanting depth can jump), but the story is complete without any click-through: the reader who never clicks a link still gets the whole picture.

**Style discipline** (all from `paper_source/example.md`):
- Ordinary language; symbols only where they carry weight.
- Every object gets a mental picture in prose ("*not* a matrix, but **an oriented geodesic line with a translation length**").
- Every joint gets a "why" ("Why two boundary points: the fixed points of the Möbius map solve a quadratic, and the sign of its discriminant is …").
- Connective sentences at every section boundary that name the mechanism ("And here's the payoff of Section 3's whole setup …").
- Optional pull-quotes for one-line summaries the reader should carry.

---

## Section page template (the concept-map index)

```markdown
---
type: paper-section
paper: "[Full citation]"
section: "N — [Title]"
tags: [paper, primary-field-tag]
---

# §N — [Paper's Section Title]

Back to the [[Paper - [Short Title]|hub]]. **[One-paragraph section opener, thesis voice: orient the reader, recall where we are in the paper, preview what this section does, state the guiding question. This is the only extended prose on the section page.]**

---

## Prerequisites recap

[Every earlier-section paper result and every external above-floor concept used in this section, as `> [!recall]-` callouts and/or transclusions. The rule is strict: a reader who lands on this section without having read any prior section must find every prerequisite here.]

> [!recall]- Selberg zeta function (Definition 4.1)
> **Formally:** [precise statement, typed]
> **In words:** [plain-language meaning] See [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent]].

> [!recall]- Absolutely continuous (μ ≪ ν)
> **Formally:** …
> **In words:** … See [[Def - Absolute Continuity of Measures]].

[Also list the atomic paper-item subpages this section builds on, with a one-line reminder each:]

**From earlier sections.** [[Thm - Homotopy Decomposition for Hyperbolic Surfaces|Theorem 3.2]] (the lift-and-unfold identity for one homotopy class), …

---

## Concept map

[Every named item in this section as a foldable bullet, in the paper's order. Parent = wikilink to the atomic subpage (using the concept's name, not the paper number); child = 3–5 sentence unpacking naming the formal statement, the intuition, and where the result is used. Sub-sections of the paper (§3.1, §3.2) are `###` sub-headers grouping the bullets; do not re-order.]

### §N.1 — [Sub-section Title]

- **[[Def - [Concept Name]|Definition N.1 (Concept Name)]]** — Introduces $X$ as the object $X := \{\ldots\}$, typed as $X : A \to B$. Motivated by the question "…", it captures the class of $A$'s with property $P$ and excludes those with $Q$. In one line: [the operational essence]. Used in [[Thm - …|Theorem N.3]] and downstream in §N+1.
  - [A second layer of detail if the item deserves it — an equivalent formulation, a subtle typing pitfall, or a link to the ambient context.]

- **[[Thm - [Result Name]|Theorem N.2 (Result Name)]]** — Under hypothesis $H$, conclusion $C$. The mechanism: [one-sentence intuition]. Proved by [one-phrase proof strategy]. Used to give [[Cor - …|Corollary N.4]] and drives the argument of §N.2.

- **[[Remark - [Descriptive Name]|Remark N.5]]** — Points out that [what the remark observes]. Its relevance: [why it matters for later results].

- **[[Ex - [Descriptive Name]|Example N.6]]** — Works out [the concrete case], giving [the explicit value]. Calibrates: [what invariant the example checks].

### §N.2 — [Sub-section Title]

- …

---

## Section verification log

**Verified.** [What was rigorously reproduced.]
**Flagged / uncertain.** [What is flagged with ⚠️.]
**Intuition not yet formalised.** [Heuristics stated without formal derivation.]
```

---

## The foldable-bullet format — details

The concept map's `- **[[…]]** — text` bullet is Obsidian's default Markdown outline: click the fold triangle next to the bullet to collapse the child bullets under it. Requirements:

- **Parent bullet:** starts with `- ` and holds the wikilink to the atomic subpage as bold text (`- **[[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3 (Selberg zeta identity)]]** — …`). The `**…**` is Markdown bold, not a callout; the wikilink stays clickable in Reading view because it is ordinary Markdown.
- **Child bullets:** indented (two spaces or a tab), plain `- …`. Fold the parent to collapse the children.
- **Do NOT use `> [!details]` or HTML `<details>` for concept-map entries** — wikilinks inside HTML tags are not clickable in Obsidian and HTML details do not collapse reliably in Reading view.
- **Item order** matches the paper's own numbering. Do not reorder, do not renumber, do not merge.
- **One bullet per named item** — Def N.1, Rem N.2, Thm N.3, … are separate bullets even when they are tightly related.
- **Sub-sections** (§N.1, §N.2) are `###` sub-headers grouping the bullets, not levels of nesting.

## The Prerequisites recap — details

Two ways to build the recap:

1. **Point-of-use `> [!recall]-` callout** — a paper-notes staple; the callout body carries both the formal statement (typed) and the plain-language meaning, plus a wikilink to the atomic note. Best when the reader needs a compact, section-local reminder.
2. **Transclusion** `![[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent#The Definition]]` — pulls the formal Definition block into the section page verbatim. Best when the definition is short, or when the reader benefits from seeing the *exact* text used elsewhere.

Choose per prerequisite. When in doubt, use the recall callout: it is faster to write, more compact to fold, and carries the plain-language unpacking that transclusion lacks.

**Duplication across sections is intentional.** A term used in §3, §5, and §7 has three recall callouts, one per section — a floor-level reader lands on a section cold and finds everything there. Do not deduplicate; the section page is the reader's local ledger.
