# Companion Page Template

The companion page is the reading surface: the page a reader opens to read the whole paper front to back, in the thesis voice, checking every step, without leaving the page. One companion page per paper (or, for a long paper, a short hub page plus one page per paper section — see the note at the end).

Follow `notation-discipline.md` for typing and terminology, `recall-callouts.md` for the callouts, and the reference thesis for the prose voice. Every section is written intuition-first, then formal, then unpacked in a concrete case (the Prose Standard in SKILL.md).

Filename: `Study notes/Papers/[Short Title]/Paper - [Short Title].md`. The `[Short Title]` is a few words identifying the paper (Windows-portable: no `< > : " / \ | ? *`).

---

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
> [A one-to-two-paragraph plain-language account of the paper's goal and result, in thesis voice: what problem it addresses, what it establishes, and why that matters. State it so a floor-level reader understands the point of the paper before any machinery appears. Model on the thesis's Motivation section, which names the two research goals in plain words before any formalism.]

**Citation.** [Full citation, with a link or DOI if available.]

**The floor.** These notes assume only undergraduate analysis, linear algebra, and elementary probability. Everything the paper uses above that floor is recalled at its point of use or written out in a linked atomic note; every proof is rewritten so that each step is checkable without leaving the page. [If the paper's field has one unavoidable prerequisite that pervades everything — e.g. "the whole paper lives in measure-theoretic probability" — name it here and point to the atomic notes that establish it.]

**How to read this.** [One or two sentences: read top to bottom; expand a `[!recall]-` callout only if the term is unfamiliar; the Prerequisites map lists the atomic notes; the paper's own results have stub notes linked at each theorem.]

---

# Notation and Standing Conventions

[The signature table (notation-discipline.md, Rule 3): every symbol used anywhere in the paper, with its full type and its meaning. Open with a standing-conventions paragraph if the paper fixes any convention — units, sign, a default assumption ("all variables discrete unless stated", "$c = 1$"), a symbol collision you resolved with a distinct glyph. State the collision resolutions explicitly.]

| Symbol | Type | Meaning |
|---|---|---|
| ... | ... | ... |

[When a convention diverges between the paper and standard usage, add a `> [!warning] Convention:` callout naming both.]

---

# Prerequisites (backchained to the floor)

[The backchain map (Rule 1): a wikilinked list of every above-floor concept the paper uses, grouped by field, each with a one-line reminder of what it is. Concepts with an existing vault note link to it; concepts you created an atomic note for link to the new note. This is the reader's index into the atomic notes — a reader can see, before starting, exactly what machinery the paper leans on and where each piece is written out.]

**From measure-theoretic probability.** [[Def - Absolute Continuity of Measures|absolute continuity]] ($\mu \ll \nu$ — wherever $\mu$ has mass, $\nu$ does too), [[Thm - Radon–Nikodym Theorem|the Radon–Nikodym theorem]] (an absolutely continuous measure has a density), …

**From [field].** [[Def - ...]] (one-line reminder), …

[Everything here is also recalled at its point of use in the sections below — this map is the overview, the recalls are the just-in-time reminders. Do not rely on the map alone for self-containment.]

---

# §1 [Paper's Section Title]

[Open by orienting the reader, thesis-style: recall where we are, preview what this section does, and — where the thesis does this — state the guiding questions as questions. "Having fixed the notation and the objects, we now turn to the paper's first construction: …"]

[Then walk the section. For each definition the paper states:]

**Definition (paper's name, paper's number).** [Motivate it first: say in plain words what the object is and what problem it solves, leading up to the statement. Then state it formally and crisply, fully typed. Then unpack the formal statement in its smallest concrete instance, as the thesis unpacks the general Lancaster measure (Definition 2.1.1) into the $D = 2$ case $\Delta_L P = P_{XY} - P_X P_Y$ immediately after stating it. The formal statement is the opening move; the concrete case is the unpacking that follows.]

[Insert a point-of-use recall for every above-floor term the definition uses:]

> [!recall]- [term]
> **Formally:** [precise statement, typed]
> **In words:** [plain-language meaning] See [[Def - term]].

[Give the paper's own definition a stub note and wikilink it: **[[Def - Paper's Object]]**.]

[For each theorem the paper states and proves:]

**Theorem (paper's name, paper's number).** [State it formally and fully typed as a blockquote:]

> **Theorem ([name]).** [Hypotheses, each typed and with its quantifier explicit; then the conclusion. One block.]

[Then, before the proof: a paragraph of *why one should expect this to be true* (thesis voice — intuition independent of the proof), and a plain-language paraphrase of what the theorem buys.]

[Then the gap-free proof (Rule 5), in the thesis's labelled-step style:]

**Proof.** [Split bidirectional proofs into "Direction 1"/"Direction 2" as the thesis does. Proceed by bolded lead-ins, one justified move each:]

**[First move — what it establishes]:** [the move, with every step justified; expand every "clearly"/"it follows"/"by X" into explicit reasoning. Show computations line by line.]

**[Second move]:** [...]

[When the proof invokes an external result the paper does not prove, use an external-input callout (recall-callouts.md) rather than a bare citation:]

> [!cite]- External input — [Name of result]
> **Statement (typed):** [precondition → conclusion]
> **Why it's true (intuition):** [one or two sentences]
> **Source:** [citation]. [Include the proof only if short or illuminating; otherwise: "Take on faith with the precondition and conclusion above."]

[Flag anything you could not verify or filled from your own knowledge with the uncertainty marker (recall-callouts.md).]

[Longer digressions, alternative proofs, or worked numerical checks go in a collapsible `> [!note]- ...` so the main line stays readable, exactly as the thesis folds detail — but the main reasoning line stays above the fold and checkable.]

---

# §2 [Paper's Section Title]

[Same pattern. Open by orienting; recall earlier objects with a collapsed `[!recall]-` chip rather than assuming them carried over.]

...

---

# External inputs

[A consolidated list of every result the paper imports without proof — each as an external-input callout with statement, type, intuition, and source. This duplicates the inline callouts on purpose (Rule 7 favours the reader over DRY): it is the reader's single ledger of "what this paper stands on". Optional if there are only one or two, which can live inline.]

---

# Verification log

[The honesty record (Rule 6). Three short lists:]

**Verified.** [Each definition or lemma you supplied from your own knowledge, with the source you confirmed it against. "Radon–Nikodym theorem statement checked against Folland, *Real Analysis*, Thm 3.8." ]

**Flagged / uncertain.** [Everything you marked with the uncertainty marker, gathered here: what you were unsure of and why. If empty, say "No unresolved uncertainties." Do not leave this blank — an empty log should be an explicit statement that nothing is outstanding, not an omission.]

**Intuition not yet formalised.** [Every place where the notes give an intuition, heuristic, or plausibility picture that has not been made rigorous — gathered from the ⚠️ / intuition-not-proof markers in the body. Name each and say what a full formalisation would need. If empty, say so explicitly.]
```

---

## Long papers: hub + section pages

When a single companion page would become unwieldy, split the reading surface at the paper's own section boundaries:

- `Study notes/Papers/[Short Title]/Paper - [Short Title].md` becomes a **hub**: it carries the header (`# Paper — [Short Title]`, the abstract, the floor statement), the **Notation and Standing Conventions** table, the **Prerequisites** map, a one-line table of contents linking each section page in order, and the **Verification log**.
- Each paper section becomes `Study notes/Papers/[Short Title]/Paper - [Short Title] — §N [Section].md`, holding that section's walk-through (opener, definitions, theorems, gap-free proofs, recalls). Each section page opens by orienting the reader and recalls earlier objects with collapsed `[!recall]-` chips, so it is readable on its own.

Split only at the paper's real section boundaries, and only when length demands it. Default to the single page. This mirrors how `polymath-notes` splits a topic page at sub-chapter boundaries with cross-references between them.
