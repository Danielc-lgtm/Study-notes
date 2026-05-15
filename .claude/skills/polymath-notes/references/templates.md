# Page Templates

This document contains the exact structure for each page type created by the polymath-notes skill. When creating Obsidian pages, follow these templates, using the formatting patterns described in `obsidian-patterns.md`.

---

## Topic Page Template

The topic page is the hub for a mathematical topic (chapter-level). Use appropriate emoji in the title or frontmatter.

```markdown
---
type: topic
subject: [subject-slug]
chapter: "[section range]"
title: "[Full Title]"
tags: [area-tag, subject-tag]
---

# Notation Registry

[List every symbol, convention, and notational choice used anywhere in this topic's subpages. This section is always visible — NOT in a collapsible section. It is the first thing the reader sees when returning after a long absence. Format as a definition list or bullet list.]

[Example format:]
- $G, H, K, N$ — groups (typically finite unless stated otherwise)
- $e$ or $1_G$ — identity element of $G$
- $|G|$ — order (number of elements) of $G$
- $H \leq G$ — $H$ is a subgroup of $G$
- $H \trianglelefteq G$ — $H$ is a normal subgroup of $G$
- $G/H$ — quotient group (set of left cosets $gH$)

---

# Motivation

[Why does this topic exist? What concrete mathematical problems does it solve? What breaks without it? What questions motivated its development?]

[Write so that someone who has forgotten everything about the topic can read this and understand why they should care. Be specific — not "this is important because it generalizes X" but "without this, we cannot do Y, and the specific obstacle is Z."]

[Write in David Tong style: conversational, precise, building from the concrete problem to the abstract solution.]

---

# Concept Map

[All definitions, theorems, and exercises for this chapter. Each entry is a foldable bullet: a parent bullet holding the wikilinked name, and an indented child bullet holding the formal statement (3–5 sentences with key details, examples, and connections). Folding the parent (Obsidian list folding) collapses the statement; the wikilink stays clickable in both Editing and Reading view because it is ordinary Markdown. Definitions, theorems, and exercises are interleaved in natural reading order following the source material.]

[Do NOT use HTML `<details>`/`<summary>` for concept-map entries — wikilinks inside HTML tags are not clickable in Obsidian, and `<details>` blocks containing markdown do not collapse reliably in Reading view. See `obsidian-patterns.md` for the foldable-bullet pattern. Keep the parent bullet and the child statement each to a single line so the entry folds reliably in Reading view.]

## §X.1 [Section Title]

- **[[Def - Topology]]**
	- A topology on a set $X$ is a collection $\tau \subseteq \mathcal{P}(X)$ containing $\emptyset$ and $X$, closed under arbitrary unions and finite intersections. The pair $(X, \tau)$ is a topological space. The elements of $\tau$ are called open sets. The discrete topology ($\tau = \mathcal{P}(X)$) and indiscrete topology ($\tau = \{\emptyset, X\}$) are the finest and coarsest topologies on any set, with every other topology lying between them.

- **[[Thm - Extreme Value Theorem]]**
	- If $X$ is compact and $f : X \to \mathbb{R}$ is continuous, then $f$ attains its maximum and minimum. This is a direct consequence of two facts: continuous images of compact sets are compact, and compact subsets of $\mathbb{R}$ are closed and bounded (Heine-Borel). The theorem fails without compactness: $f(x) = x$ on $(0,1)$ has no maximum.

> [!tip] Unlocked: Affine Variety *(from Algebraic Geometry)*
> Now that you have ideals and the Zariski topology, you can define affine varieties as zero sets of ideals. See [[Def - Affine Variety]].

- **[[Ex - Proving compactness of the closed unit interval]]**
	- Show that $[0,1]$ is compact in the standard topology. (⭐⭐)

> [!note] Exercise Index — §X.1
> [[Exercise Index - §X.1 Section Title]]

## §X.2 [Section Title]

[Continue with same pattern...]

---

# Sources and Targets

[Derived post-hoc from exercises. After solving a wide variety of exercises in this field:]

**Targets — What do we usually try to prove?**

[Written as prose paragraphs. Enumerate the recurring types of conclusions: existence, uniqueness, convergence, bounds, isomorphism, non-simplicity, etc. Explain why these are the natural targets in this field — what makes these the important questions. A reader with no background should understand what the "game" of this field is.]

**Sources — What assumptions do we usually leverage?**

[Written as prose paragraphs. Enumerate the recurring types of hypotheses and what each unlocks. Explain the relationship between common assumptions and the targets above — which assumptions route to which conclusions and why.]

---

# Legal Operations

[What operations/manipulations/moves are allowed in this domain? What operations are illegal but intuitively tempting? Fully self-contained: a person with zero background should understand everything on this page.]

[These should function as the "instrumental convergent subgoals" of problem-solving — almost all solutions route through some subset of these operations. When stuck on a problem, the reader should be able to scan this list and try each legal operation to see if it makes progress.]

**Legal operations:**

1. **[Operation name]** — [Full prose description: how it works, when to use it (trigger condition), the typical pattern of application, input type, and an example problem where this is the key step. Include wikilinks to relevant definitions and theorems. Written as a self-contained paragraph.]

2. **[Operation name]** — [...]

[Aim for 7+ legal operations.]

**Illegal but tempting operations:**

> [!warning] 1. [Operation name]
> [Why it is tempting. Why it fails — with a concrete counterexample. What additional condition would make it legal. Written as a self-contained paragraph with wikilinks.]

> [!warning] 2. [Operation name]
> [...]

[Aim for 3+ illegal-but-tempting operations.]

---

# Problem-Solving Strategy

[Written entirely as self-contained prose paragraphs — NOT as a table or numbered decision tree. The insight density principle applies: this should be a flowing explanation of how to approach problems in this field, such that a reader with no background could read it and substantially improve their ability to solve a wide variety of exercises.]

[Cover: what are the main problem classes (what you are trying to prove), what assumption patterns typically appear for each class, which theorems route from which assumptions to which conclusions, and why this enumeration covers the important cases. The justification for why these are the right categories is as important as the categories themselves.]

[Include wikilinks to theorems throughout.]

---

# Most Reusable Properties

[Bullet-point format but each bullet is a comprehensive paragraph.]

- **[[Thm - First Isomorphism Theorem|First Isomorphism Theorem]]**: $G/\ker(\varphi) \cong \text{im}(\varphi)$. [A full paragraph explaining the common pattern of how this is used — what it is typically combined with, the common setup that calls for it, what makes it the first thing to reach for in many situations, and how to recognize when it applies in non-obvious contexts.]

- **[[Thm - Lagrange's Theorem|Lagrange's Theorem]]**: $|H|$ divides $|G|$. [Full paragraph...]

[Aim for 4–5 items.]

---

# Bridges

[How this topic connects to other fields. Written as self-contained prose paragraphs. Each bridge identifies the specific construction or theorem creating the connection. Definitions and theorems from the other field should be explained within the paragraph (not assumed known) and wikilinked if pages exist for them.]

1. **[Other field/topic]** — [Full paragraph: the specific connection, which theorem or construction creates the bridge, what transfers from this topic to that field or vice versa. Rigorous and precise — not "this is related to X" but "this is literally the same construction as X, specialized to the category of Y."]

2. **[Other field/topic]** — [...]

---

# Insights

[Conceptual insights that do not fit neatly into the categories above. These can include: unifying frames for the topic, true names for key concepts, cross-cutting observations, surprising connections, heuristics, trigger-reaction patterns that deserve elaboration, or any other high-density insight worth recording.]

[Written as prose paragraphs. Each insight should be self-contained and should make the reader see the topic differently or solve problems more effectively.]

```

---

## Definition Subpage Template

Each definition gets its own page. Every section is written in paragraph form — maximize insight density without sacrificing volume. No abbreviation.

```markdown
---
type: definition
subject: [subject-slug]
prereqs:
  - "Def - [Dependency 1]"
  - "Def - [Dependency 2]"
tags: [area-tag, subject-tag]
---

# Notation

[Any notation specific to this definition. Always restate the essential symbols — the reader may jump directly to this page. Written as a brief paragraph or concise list. Link to the parent topic page for the full registry.]

---

# Axiom Motivation

[The minimal information needed to INVENT this definition. Written as flowing prose paragraphs.]

[Address these questions in natural prose flow: What are the desiderata — what properties do we want a thing satisfying this definition to have? What examples should it capture, and what should it exclude? What breaks if we weaken any part (give a concrete undesirable thing that would be included)? What breaks if we strengthen any part (give a concrete desirable thing that would be excluded)? Sometimes the best motivation is to jump ahead: show a theorem that relies on this definition and explain which part would fail with a different definition.]

[The goal is not just "why is this definition useful" but "why THIS SPECIFIC definition and not a nearby variant."]

---

# The Definition

[The formal definition, clearly stated. Use standard mathematical notation. If there are multiple equivalent formulations, state the primary one and note the equivalences.]

---

# Categorical Definition

[INCLUDE ONLY IF a natural categorical formulation exists.]

[State the categorical definition and explain it self-containedly: define the relevant categorical concepts (universal property, functor, adjunction, etc.) enough that a reader unfamiliar with category theory can follow the construction. Then explain how the categorical definition relates to the concrete definition above.]

---

# Relate to Other Fields / Compression

[Explain this definition by connecting it to something from a different field. The connection must be precise, written as a prose paragraph:]
- "This is literally the same construction as X, specialized to the category of Y"
- "This is the analogue of X when you replace condition A with condition B"
- "This generalizes X by dropping assumption Z"

[If the concept is genuinely novel and not analogous to anything, say so explicitly rather than forcing a bad analogy.]

---

# Examples / Corollaries

[Concrete examples and non-examples, followed by immediate corollaries. Written as prose paragraphs, one per example or corollary.]

[Examples should include both "is an instance" and "is NOT an instance" cases, each probing a different aspect of the definition. Corollaries serve as calibration checks: if the reader can verify each one after reading the definition, they have understood it correctly. Choose corollaries that test different aspects or axioms of the definition.]

---

# Unlocked by This

[INCLUDE ONLY IF this definition (together with its neighbors) unlocks concepts from downstream topics in the prereq DAG.]

> [!tip] [Concept Name] *(from [Advanced Field])*
> [1–3 sentence preview: now that you have this definition, you can understand this more advanced concept. Wikilink to its eventual page.]
```

---

## Theorem Subpage Template

Each significant theorem gets its own page.

```markdown
---
type: theorem
subject: [subject-slug]
prereqs:
  - "Def - [Dependency 1]"
  - "Thm - [Dependency 2]"
tags: [area-tag, subject-tag]
---

# Notation

[Restate key notation for self-containedness. A reader jumping directly here must understand the notation without navigating elsewhere. Link to the parent topic page for the full registry.]

---

# Motivation

[What question does this theorem answer? What mathematical problem or gap existed before it? Why should one expect a result like this to exist? Written as prose paragraphs.]

---

# Sources and Targets

[This is NOT a simple "Input: X, Output: Y" list. This section is about recognizing when the theorem applies (sources) and how to use its conclusion (targets), with emphasis on nonobvious connections.]

**Sources (Input Broadening)**

[The theorem requires precondition $A$. For each source property $B$:]

[Write as prose paragraphs. State property $B$ precisely, explain why $B \implies A$ (the bridge argument), note why this implication is nonobvious, and give an example problem where starting from $B$ you would invoke this theorem. Aim for properties $B$ that are commonly encountered in problems. These should be derived from exercises: after seeing the theorem used in many problems, what were the actual starting points?]

**Targets (Output Amplification)**

[The theorem gives conclusion $C$. For each target combination:]

[Write as prose paragraphs. State the additional property $D$, explain how $C$ combined with $D$ gives a further result $E$, note why this combination is nonobvious, and explain why it is useful. The target section is about how the theorem can be used and combined with other results. Also derived from exercises.]

---

# Why Is It True

[An explanation for why one should EXPECT this theorem to be true, independent of the formal proof. This is NOT a proof sketch — it is the intuition that makes the proof unsurprising. Written as prose paragraphs. No length constraint — write as much as needed for the full intuition.]

---

# What Makes This Hard

[2–3 sentences identifying: where in the proof most people get stuck, what the non-obvious step is, and what the most common error is when attempting the proof. This is directly useful for spaced practice — when returning after months, this tells the reader where to focus their rederivation effort.]

---

# Rederivation Scaffold

[The key section for spaced practice. Self-sufficient: reading ONLY this section should let the reader reconstruct the full proof without any other reference.]

**High-level strategy:**
[2–3 sentences: the overall approach and the key idea or trick.]

**Subgoal decomposition:**

1. **[Subgoal 1]:** Show that [target].
   - *Hint:* [Minimal hint — one sentence identifying the key technique]
   - *Why needed:* [How this feeds into the next step]

2. **[Subgoal 2]:** Show that [target].
   - *Hint:* [...]
   - *Why needed:* [...]

---

# Lemma Decomposition

[Each lemma independently practiceable in approximately 5 minutes. Each lemma is a collapsible callout; the full proof is a nested collapsible callout inside it.]

> [!note]- Lemma 1: [Statement]
> **Statement:** [Precise statement]
>
> **Hint:** [One key idea for proving]
>
> **Why needed:** [How it is used in the main proof]
>
> > [!note]- Full proof
> > [Complete formal proof]

> [!note]- Lemma 2: [Statement]
> [Same structure]

---

# Formal Proof

> [!note]- Complete formal proof
> [The complete, formal proof. Ground truth for verification after attempting rederivation from the scaffold.]

---

# Cross-Field Exercise Suggestions

[Intentionally loose: find the most out-of-distribution, least obvious contexts where the theorem can be applied. This battle-tests the Sources — can you recognize the theorem's applicability in unfamiliar settings? Does not have to involve a different field; surprising applications within the same field count.]

[For each suggestion, written as a prose paragraph: describe the problem context, explain why the theorem applies (which property $B$ maps to the theorem's precondition $A$), and why this application is nonobvious.]

---

# Bridges

[Links to related theorems and concepts. Written as prose paragraphs.]

- **[Related theorem/concept]** — [How it relates: generalization, special case, dual, analogue in a different category, etc. With wikilinks.]

---

# Unlocked by This

[INCLUDE ONLY IF this theorem unlocks downstream concepts.]

> [!tip] [Concept Name] *(from [Advanced Field])*
> [1–3 sentence preview with wikilink.]
```

---

## Exercise Subpage Template

Each exercise gets its own page. Self-containedness is paramount.

```markdown
---
type: exercise
subject: [subject-slug]
difficulty: "⭐⭐"
prereqs:
  - "Def - [Prereq 1]"
  - "Thm - [Prereq 2]"
tags: [area-tag, subject-tag]
---

# Problem Statement

[The exercise as stated. Include all given information and what needs to be shown or computed.]

**Recall:**

[Self-contained restatement of all definitions and conventions needed to understand the problem. Use transclusion where appropriate:]

![[Def - Normal Subgroup#The Definition]]

[Or brief restatements with wikilinks when transclusion is too bulky:]

A [[Def - Normal Subgroup|normal subgroup]] $H \trianglelefteq G$ is a subgroup satisfying $gHg^{-1} = H$ for all $g \in G$...

[The reader should understand the problem WITHOUT clicking any links. Links are for deeper understanding.]

---

# Convergent Strategy

[Written as prose paragraphs. Focus on what it is about the problem that makes a particular technique suitable or helpful.]

**Problem class:** [Which type of problem this is, referencing the topic page's problem-solving strategy.]

**Assumption pattern:** [What makes this instance recognizable — which assumptions are present and what they unlock.]

**Theorem routing:** [Which theorem or theorems convert the assumptions to the target. State the route explicitly with wikilinks.]

**Key decision point:** [The non-obvious choice that makes this problem interesting — what makes it harder than direct application of the theorem.]

---

# Legal Operations Used

[Which legal operations from the topic page are deployed, and in what order. Written as a numbered list with prose descriptions of how each is applied in this specific problem.]

---

# Hints

[Progressive hints as collapsible callouts, from gentle nudge to near-giveaway. 2–4 hints.]

> [!note]- Hint 1
> [Identifies the problem class or key technique.]

> [!note]- Hint 2
> [Names the specific theorem or construction.]

> [!note]- Hint 3
> [Gives the key computational step or trick.]

---

# Solution

[Hierarchical structure: the top level shows the highest-density insight — the key idea and result of each step. Collapsible callouts reveal progressively more detail.]

**Step 1: [Name — what this step achieves]**

[Statement of the result of this step. Enough detail to know the claim without expanding.]

> [!note]- Derivation
> [Full derivation. Recall any theorem or definition used, with wikilinks and restatement of the theorem statement. Each claim independently verifiable.]

**Step 2: [Name]**

[Result.]

> [!note]- Derivation
> [Full derivation.]

> [!note]- Complete formal solution
> [Complete, cleaned-up solution as a single self-contained proof. Every step justified, no gaps.]

---

# Key Takeaways

[Elaborate prose paragraphs — NOT terse bullets. Each takeaway is a self-contained insight paragraph focusing on what makes the technique suitable for this type of problem and maximizing generalization.]

**[Takeaway 1 — a descriptive phrase]**

[Full paragraph: what feature of the problem signals this approach? When else does this pattern apply? Give concrete examples of other problems where the same technique works. Explain what to look for — the "trigger" — and what the general pattern of application is. The reader should finish this paragraph knowing how to solve a class of problems, not just this one.]

**[Takeaway 2 — a descriptive phrase]**

[Full paragraph...]
```

---

## Exercise Index Page Template

One page per sub-chapter section. Lists all exercises with per-exercise dependency links.

```markdown
---
type: exercise-index
subject: [subject-slug]
section: "[section number]"
tags: [area-tag, subject-tag]
---

## §X.Y [Section Title] — Exercises

- [[Ex - Exercise Name]] — one-line description of technique/pattern drilled ([[Def - A]], [[Thm - B]], [[Def - C]])
- [[Ex - Exercise Name]] — one-line description ([[Thm - D]], [[Def - E]])
- [[Ex - Exercise Name]] — one-line description ([[Def - F]], [[Thm - G]], [[Thm - H]])

[Aim for at least 3 exercises per section.]

[The parenthesised wikilinks after each exercise are the complete list of definitions and theorems invoked in that exercise's solution — per-exercise prerequisites, not section-level prerequisites. This lets the reader see exactly which concepts each exercise drills. Enclose the list in parentheses, never square brackets: a `[` placed immediately before a `[[wikilink]]` produces `[[[`, which Obsidian mis-parses, breaking the link.]
```
