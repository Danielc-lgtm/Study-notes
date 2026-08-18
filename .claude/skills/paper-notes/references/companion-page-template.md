# Companion Page Template — hub + section indices

The paper's reading surface is **not one long walk-through**. It is a **hub page** plus **one section page per paper section**, each structured as a polymath-style concept-map index. Every named paper item is its own atomic subpage (see `atomic-note-templates.md`); the section page's job is to give the reader the big picture at a glance and provide the self-contained recap that makes the section readable cold.

Follow `notation-discipline.md` for typing and terminology, `recall-callouts.md` for the callouts, and the reference thesis for the prose voice. Every subpage is written intuition-first, then formal, then unpacked in a concrete case (the Prose Standard in SKILL.md).

Filename pattern:
- Hub: `Study notes/paper/[Short Title]/Paper - [Short Title].md`
- Section: `Study notes/paper/[Short Title]/Paper - [Short Title] — §N [Section].md`

The `[Short Title]` is a few words identifying the paper (Windows-portable: no `< > : " / \ | ? *`).

---

## Hub page template

```markdown
---
type: paper
paper: "[Full citation: Authors, Title, venue, year]"
authors: [Author One, Author Two]
subject: [primary-field-slug]
tags: [paper, primary-field-tag, secondary-field-tag]
---

# Paper — [Short Title]

> [!abstract] What this paper does
> [A one-to-two-paragraph plain-language account, thesis voice: what problem it addresses, what it establishes, why that matters. State it so a floor-level reader understands the point of the paper before any machinery appears.]

**Citation.** [Full citation, with a link or DOI if available.]

**The floor.** These notes assume only undergraduate analysis, linear algebra, and elementary probability. Everything above that floor is recalled at its point of use or written out in a linked atomic note; every proof is rewritten so that each step is checkable without leaving the page.

**How to read this.** Each section page is a **concept-map index** — foldable bullets holding every named paper item's statement inline. Fold-out mode: read the section page top to bottom without leaving it. Click-through mode: click into any atomic subpage for the full proof and motivation. **Every section page is modularly self-contained** — you can open §5 without reading §2–§4.

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
