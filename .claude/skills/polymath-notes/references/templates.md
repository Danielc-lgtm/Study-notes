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

[List every symbol, convention, and notational choice used anywhere in this topic's subpages. This section is always visible — NOT in a collapsible section. It is the first thing the reader sees when returning after a long absence. Format as a definition list or bullet list.

**Standing-convention preamble (when applicable):** When the topic relies on a convention (units, sign, default-assumption such as "all rings commutative with 1", "$c = 1$ throughout", "all manifolds Hausdorff second countable"), open the registry with a paragraph explaining the choice, with a recipe for converting between conventions if relevant. When conventions diverge between standard sources, include a `> [!warning] Convention:` callout. Example: `Special Relativity I` line 11.]

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

[Write in the thesis register (`prose/Chiang Sung En-Thesis.pdf`; specification in `prose-and-proof-standard.md` Part I): orient the reader, pose the guiding questions as questions, name the competing approaches and what goes wrong without this one, give the roadmap — the thesis's §1.1 Motivation and its §3.1 opener are the calibration passages. Measured first-person-plural academic voice; every claim with its reason; concrete problem before abstract solution. Open with a hook in the first sentence: `Modules I` opens "Here is the entire topic in one sentence: a module is a vector space over a ring."]

[**Structural-backbone display equation (when applicable):** When the topic has a hierarchy or classification at its core, state it as a single display equation in Motivation that the rest of the chapter references. Example: `Rings II` line 41 places `field ⊂ ED ⊂ PID ⊂ UFD ⊂ ID` as a display.]

[**Audience-assumption paragraph (closing):** State what the reader is assumed to know — which background topics they should have refreshed before working through this one. This is the most useful single addition for spaced re-entry. Example: `Special Relativity I` line 48.]

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
> Now that you have ideals and the Zariski topology, you can define **affine varieties** as zero sets of ideals.

- **[[Ex - Proving compactness of the closed unit interval]]** (⭐⭐)
	- Show that $[0,1]$ is compact in the standard topology.

[Every exercise in the topic's exercise list must appear in the concept map at the appropriate sub-chapter section, with an inline difficulty tag `(⭐)`/`(⭐⭐)`/`(⭐⭐⭐)` after the wikilink and a one-line description below. Exercises are interleaved with the definitions and theorems they drill, not segregated below them.]

> [!note] Exercise Index — §X.1
> [[Exercise Index - §X.1 Section Title]]

[The wikilink in this callout must be byte-identical to the filename of the Exercise Index page it points to. Choose one `[Section Title]` string per section and use it verbatim in all three places — the `## §X.1 [Section Title]` concept-map header, this callout's wikilink, and the Exercise Index page's filename — so the link always resolves. A mismatch (a fuller title in the header than in the filename, say) silently breaks the link.]

[**`Unlocked:` callout placement:** every sub-chapter section in the concept map should contain at least one `> [!tip] Unlocked: [Concept Name] *(from [Advanced Field])*` callout, unless the section genuinely unlocks nothing downstream. No cap on the number of unlocks per section — `Special Relativity I §1.3` has three. Multi-paragraph callouts are permitted when the downstream concept is paradigm-shifting (e.g., the equivalence principle unlocking from Minkowski space — `Def - Minkowski Space.md` line 87 is the model). Forward references to pages that do not yet exist must be **bold plain text**, not wikilinks.]

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

1. **[Operation name]** — [Full prose description: how it works, when to use it, the typical pattern of application, input type, and an example problem where this is the key step. Include wikilinks to relevant definitions and theorems. Written as a self-contained paragraph. Inline `*Trigger:*` and `*Pattern:*` italic markers at the end of the prose are **permitted and encouraged** — they aid spaced-retrieval scanning. Example pattern: `Topology II` line 211 "*Trigger:* compactness + a sequence/net... *Pattern:* 'by compactness, pass to a convergent subnet $x_{\alpha_k} \to x_\infty$' and continue with the limit."]

2. **[Operation name]** — [...]

[Aim for 7+ legal operations. No upper cap.]

**Illegal but tempting operations:**

> [!warning] 1. [Operation name]
> [Why it is tempting. Why it fails — with a **concrete counterexample**. **What additional condition would make it legal** — naming the repair condition explicitly is the gold-standard pattern (`Rings II` lines 145–158 demonstrates "becomes legal exactly when the ring is a PID"). Written as a self-contained paragraph with wikilinks.]

> [!warning] 2. [Operation name]
> [...]

[Aim for 3+ illegal-but-tempting operations. No upper cap.]

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

---

# Imported Results

[**Include ONLY if the chapter uses a result without proof** under the single exception of the Proof Standard (`prose-and-proof-standard.md` §5: a result whose complete published proof is genuinely book-length). The normal chapter proves everything it mentions and has no such section. One bullet per import:]

- **[Name of the result]** — used in [[Thm - Page That Uses It]] (callout "Imported without proof: …"). Complete proof in [Author, *Title*, section/pages]. Imported rather than proved because [one sentence].

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

[Any notation specific to this definition. Always restate the essential symbols — the reader may jump directly to this page. Written as a brief paragraph or concise list. Link to the parent topic page for the full registry.

**Standing-convention preamble (when applicable):** When the topic depends on a convention, open the Notation section with a paragraph stating the convention before the symbol list. Include `> [!warning] Convention:` callouts where the convention diverges between sources (e.g., signature convention in `Def - Minkowski Space and the Metric.md` line 44).]

[**Compound page preamble (when applicable):** If the page title lists multiple concepts, add one explanatory sentence after Notation: "This is a compound page: it defines [N] interlocking notions — [list] — because they are introduced together and none is fully usable without the others." Pattern: `Def - Module Homomorphism.md` line 19.]

---

# Axiom Motivation

[The minimal information needed to INVENT this definition. Written as flowing prose paragraphs.]

[**Per-axiom failure analysis is required for any definition with $n \geq 2$ independent axioms.** Each axiom must get its own "what breaks if dropped" treatment with a concrete counterexample. A single "what if weakened" sentence at the end does not suffice.]

[Address these questions in natural prose flow: What are the desiderata — what properties do we want a thing satisfying this definition to have? What examples should it capture, and what should it exclude? For each axiom: what breaks if we drop it? What is excluded if we strengthen it? Sometimes the best motivation is to jump ahead: show a theorem that relies on this definition and explain which part would fail with a different definition.]

[The goal is not just "why is this definition useful" but "why THIS SPECIFIC definition and not a nearby variant." The test: "Could a reader who has never seen this definition invent it from the motivation alone?" Calibration bars: `Def - Group.md`, `Def - Normal Subgroup.md`, `Def - The Total Derivative.md`, `Def - Topological Space.md`. Aim for 4+ paragraphs for any non-trivial definition.]

---

# The Definition

[The formal definition, clearly stated. Use standard mathematical notation. If there are multiple equivalent formulations, state the primary one and note the equivalences.]

---

# Categorical Definition

[**Required when a natural categorical or structural formulation exists**; optional otherwise. Heading may be relabelled `# Categorical / Structural Definition` when more structural than category-theoretic.]

[Definitions that should typically have one: group, ring, module, ring homomorphism, ideal, topological space, continuous map, σ-algebra, measurable function, holomorphic function, manifold, Lie group, sheaf, any definition with a natural universal property / morphism structure.]

[State the categorical definition and explain it self-containedly: define the relevant categorical concepts (universal property, functor, adjunction, etc.) enough that a reader unfamiliar with category theory can follow the construction. Then explain how the categorical definition relates to the concrete definition above.]

---

# Relate to Other Fields / Compression

[Explain this definition by connecting it to something from a different field. The connection must be precise, written as a prose paragraph:]
- "This is literally the same construction as X, specialized to the category of Y"
- "This is the analogue of X when you replace condition A with condition B"
- "This generalizes X by dropping assumption Z"

[**"True name" callout:** when the definition has a true name — the operational characterisation distinct from the formal definition — state it explicitly as a short labelled paragraph here:]

**True name:** [The operational form. Example: `Def - Compact Space.md` line 63: "The 'true name' of compactness in analysis is the net-subnet form: every net has a convergent subnet, and in metric spaces, every sequence has a convergent subsequence (Bolzano–Weierstrass)."]

[If the concept is genuinely novel and not analogous to anything, say so explicitly rather than forcing a bad analogy.]

---

# Examples / Corollaries

[Concrete examples and non-examples, followed by immediate corollaries. Written as prose paragraphs, one per example or corollary.]

[Examples should include both "is an instance" and "is NOT an instance" cases, each probing a different aspect of the definition. **At least one "is NOT" example** is required for any non-trivial definition. **Every example is verified on the page**: check the clauses of the definition one by one for the instance and exhibit the failing clause for the non-instance, with every line justified as in the thesis's Example 2.2.1 — an asserted example violates the Proof Standard. Corollaries serve as calibration checks: if the reader can verify each one after reading the definition, they have understood it correctly. Each corollary is proved here or wikilinked to the page that proves it. Choose corollaries that test different aspects or axioms of the definition.]

[**End the section with an explicit `**Calibration check.**` paragraph** naming 2–3 small verifications the reader should be able to perform. Patterns: `Def - Group.md` line 94, `Def - Topological Space.md` line 110, `Def - Compact Space.md` line 101.]

---

# Unlocked by This

[INCLUDE ONLY IF this definition (together with its neighbors) unlocks concepts from downstream topics in the prereq DAG. **No upper length cap.**]

> [!tip] [Concept Name] *(from [Advanced Field])*
> [Preview of any length appropriate to the downstream concept. For routine downstream concepts a 1–3 sentence preview suffices; for paradigm-shifting downstream concepts, write extended-form multi-paragraph callouts that essentially deliver a mini-essay on the downstream theory (e.g., `Def - Minkowski Space and the Metric.md` line 87's "Metric as the Central Object of Physics" callout walks from $\eta_{\mu\nu}$ to $g_{\mu\nu}(x)$ to the equivalence principle to curvature). Name the downstream concept in **bold**; do NOT wikilink it unless its page already exists in the vault — a wikilink to a missing page creates an empty stub when clicked in Obsidian.]
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

# Statement

[**Required.** A precise, formal statement of the theorem, written as a blockquote starting `> **Theorem (name).**` (or `> **Lemma.**`, `> **Corollary.**`). The Statement is the canonical formal statement of the result, the thing a returning reader looks at first. Do not bury the statement inside Motivation as a passing display equation, and do not skip this section. Hypotheses and conclusion in one block; corollaries/companion statements may follow as additional blockquotes.

Example:

> **Theorem (Inverse Function Theorem).** Let $U \subseteq \mathbb{R}^n$ be open, $f \in C^k(U, \mathbb{R}^n)$ with $k \geq 1$, and $x_0 \in U$ a point where $Df_{x_0} : \mathbb{R}^n \to \mathbb{R}^n$ is invertible. Then there is an open neighbourhood $U_0$ of $x_0$ such that $f|_{U_0}$ is a $C^k$-diffeomorphism onto its image, with $D(f|_{U_0})^{-1}_{f(x)} = (Df_x)^{-1}$.

One-sentence callouts (e.g. "the conclusion is local — see Why Is It True") may follow the blockquote when they aid recognition.]

---

# Motivation

[What question does this theorem answer? What mathematical problem or gap existed before it? Why should one expect a result like this to exist? Written as prose paragraphs. The motivation should *not* re-state the formal statement — the Statement section above is for that. The motivation explains the *role* and *importance* of the theorem in human terms.]

---

# Sources and Targets

[This is NOT a simple "Input: X, Output: Y" list. This section is about recognizing when the theorem applies (sources) and how to use its conclusion (targets), with emphasis on nonobvious connections.]

[**Aim for at least 3 disguised sources and 3 target combinations, each as a multi-sentence prose paragraph.** A one-paragraph Sources block that names the precondition without giving B → A bridges is a quality failure. Gold-standard examples: `Thm - First Isomorphism Theorem.md`, `Thm - Orbit-Stabiliser Theorem.md`, `Thm - The Inverse Function Theorem.md`.]

**Sources (Input Broadening)**

[The theorem requires precondition $A$. For each source property $B$:]

[Write as prose paragraphs. State property $B$ precisely, explain why $B \implies A$ (the bridge argument), note why this implication is nonobvious, and give an example problem where starting from $B$ you would invoke this theorem. Aim for properties $B$ that are commonly encountered in problems. These should be derived from exercises: after seeing the theorem used in many problems, what were the actual starting points?]

**Targets (Output Amplification)**

[The theorem gives conclusion $C$. For each target combination:]

[Write as prose paragraphs. State the additional property $D$, explain how $C$ combined with $D$ gives a further result $E$, note why this combination is nonobvious, and explain why it is useful. The target section is about how the theorem can be used and combined with other results. Also derived from exercises.]

---

# Why Is It True

[An explanation for why one should EXPECT this theorem to be true, independent of the formal proof. This is NOT a proof sketch — it is the intuition that makes the proof unsurprising. Written as prose paragraphs. No length constraint — write as much as needed for the full intuition.]

[**Include at least one bolded one-liner mechanism summary** capturing the entire intuition in a single sentence. Patterns: `Thm - Dominated Convergence Theorem.md` line 50 "**the dominator $g$ does two jobs — it makes $2g \pm (f_n - f) \geq 0$ so Fatou is legal, and it is integrable so $\int 2g$ can be cancelled.**"; `Thm - Central Limit Theorem.md` line 55; `Thm - Orbit-Stabiliser Theorem.md` line 80.]

---

# What Makes This Hard

[2–3 sentences identifying: where in the proof most people get stuck, what the non-obvious step is, and what the most common error is when attempting the proof. This is directly useful for spaced practice — when returning after months, this tells the reader where to focus their rederivation effort.]

---

# Rederivation Scaffold

[The key section for spaced practice. Open with an explicit reader contract: "**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**"]

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

[**Every lemma callout must contain all four fields**: `**Statement:**`, `**Hint:**`, `**Why needed:**`, and a nested `> [!note]- Full proof` callout. Omitting Hint or Why-needed is a quality failure. The Algebra / Multivariate / Topology lemma decompositions set the bar. **Each `Full proof` is itself complete at the thesis floor** (`prose-and-proof-standard.md` §6): named assumptions and goal, bold lead-ins, a justification on every displayed line, all cases, a closing sentence. A lemma whose Full proof is missing or is a sketch is caught by `find-unproved-theorems.py` and is a Proof Standard violation.]

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
> [The complete, formal proof. Ground truth for verification after attempting rederivation from the scaffold. **The thesis's fully written proofs are the minimum level of detail** — `prose-and-proof-standard.md` §6 lists the eleven features and §8 shows a model. In particular:]
>
> [Open by naming what is assumed and what must be shown: "Let … . We need to show … ."]
>
> [**When the theorem has well-posedness preconditions** (e.g. "the quotient exists", "the integral converges"), open the proof with **"Step 0 — [precondition]"** verifying it, separately from the substantive proof. See `Thm - First Isomorphism Theorem.md` line 163 for the pattern.]
>
> [Organise by labelled blocks — **Direction 1 / Direction 2** for an equivalence, **Case 1 / Case 2** (with a sentence showing the cases exhaust), **Part I / Part II**, **Step 1, 2, …** — each announced with what it establishes, each move introduced by a bold lead-in naming it. Every displayed equality, inequality, or implication carries its justification on the same line: "(by Lemma 2)", "(since … )", "(by the dominated convergence theorem; the dominating function is $g$)". Every hypothesis is invoked by name at the point it is used. Well-definedness and existence are checked clause by clause. Both directions, all cases, all parts are written out; "similarly" is expanded. Numbered intermediate lines are combined explicitly ("Combining (3) and (5) …"). Other results are used only by wikilink to a page whose Formal Proof is complete, with the statement restated at the point of use. Close in words: "Therefore … ." A sketch, a citation in place of an argument, or "clearly" anywhere in this callout means the page is not finished.]

---

# Cross-Field Exercise Suggestions

[Intentionally loose: find the most out-of-distribution, least obvious contexts where the theorem can be applied. This battle-tests the Sources — can you recognize the theorem's applicability in unfamiliar settings? Does not have to involve a different field; surprising applications within the same field count.]

[Aim for 3+ genuinely different fields/contexts. For each suggestion, written as a prose paragraph: describe the problem context, explain why the theorem applies (which property $B$ maps to the theorem's precondition $A$), and why this application is nonobvious. Use web search to find surprising applications.]

---

# Bridges

[Links to related theorems and concepts. **Each bridge must be a self-contained prose paragraph that explains the construction**, not a chain of wikilinks. A bridge of the form "X is the Y of Z; W is the V; Q runs on R" without unpacking is too compressed — every clause must be unpacked enough that a reader unfamiliar with the identification gets actual help. Gold-standard pattern: `Rings II` line 198 — "this ideal is principal, generated by a single polynomial $m$ — and that generator is the minimal polynomial of $A$".]

- **[Related theorem/concept]** — [How it relates: generalization, special case, dual, analogue in a different category, etc. With wikilinks. Multiple sentences, not a one-line tag.]

---

# Unlocked by This

[INCLUDE ONLY IF this theorem unlocks downstream concepts. **No upper length cap.**]

> [!tip] [Concept Name] *(from [Advanced Field])*
> [Preview of any length appropriate to the downstream concept; 1–3 sentences for routine concepts, multi-paragraph mini-essays for paradigm-shifting downstream concepts. Name the downstream concept in **bold**; do NOT wikilink it unless its page already exists in the vault.]
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

[Written as four labelled paragraphs, each substantive prose (multiple sentences). One-phrase content under any label is a quality failure.]

**Problem class:** [Which type of problem this is, referencing the topic page's problem-solving strategy. Multiple sentences naming the class and why the routine of that class applies.]

**Assumption pattern:** [What makes this instance recognizable — which assumptions are present and what they unlock. Multiple sentences naming the assumptions and tracing what each is good for.]

**Theorem routing:** [Which theorem or theorems convert the assumptions to the target. State the route explicitly with wikilinks. Multiple sentences naming each link of the route and why the chain is correct.]

**Key decision point:** [The non-obvious choice that makes this problem interesting — what makes it harder than direct application of the theorem. Multiple sentences identifying the choice and why the natural alternative fails.]

---

# Legal Operations Used

[Which legal operations from the topic page are deployed, and in what order. Written as a numbered list. Each entry **references the topic page's Legal Operations by number** ("operation 4 from the topic page") and is followed by a prose paragraph explaining how that operation is applied in this exercise.]

---

# Hints

[Progressive hints as collapsible callouts, from gentle nudge to near-giveaway. **No upper cap on the number of hints** — use as many as the problem requires for a graduated descent (typically 2–5 hints). Each hint must be strictly more revealing than the previous.]

> [!note]- Hint 1
> [Identifies the problem class or key technique.]

> [!note]- Hint 2
> [Names the specific theorem or construction.]

> [!note]- Hint 3
> [Gives the key computational step or trick.]

---

# Solution

**Three-tier structure (all four elements mandatory):**
1. A **plan paragraph** between `# Solution` and Step 1 summarizing the entire route (~3 sentences).
2. Per-step bolded summary lines stating the result of each step.
3. A `> [!note]- Derivation` callout under each step with the full computation.
4. A final `> [!note]- Complete formal solution` callout giving a clean self-contained proof.

Collapsing the derivation layer into a single block (no per-step structure) is a quality failure. `Rings II/Ex - In a principal ideal domain irreducibles are prime.md`, `Group Theory III/Ex - No group of order 132 is simple.md`, and `Modules II/Ex - Computing the Smith normal form.md` set the bar.

[Plan paragraph: ~3 sentences naming the route. "The proof breaks into three steps. Step 1 establishes [X] using [Y]; Step 2 leverages [X] to derive [Z]; Step 3 combines [Z] with [W] to get the conclusion. The non-obvious move is in Step 2, where we [...]."]

**Step 1: [Name — what this step achieves]**

[Statement of the result of this step. Enough detail to know the claim without expanding.]

> [!note]- Derivation
> [Full derivation. Recall any theorem or definition used, with wikilinks and restatement of the theorem statement. Each claim independently verifiable.]

**Step 2: [Name]**

[Result.]

> [!note]- Derivation
> [Full derivation.]

> [!note]- Complete formal solution
> [Complete, cleaned-up solution as a single self-contained proof at the thesis floor (`prose-and-proof-standard.md` §6): named goal, labelled blocks, a justification on every line, every case, a closing sentence. Every theorem invoked is wikilinked to a page whose Formal Proof is complete and restated at the point of use — a solution that leans on an unproved result is itself a Proof Standard violation.]

[**Optional add-ons used in upper-tier exercises:**]

[**"Illegal but tempting alternative route"** — a `> [!warning]` callout at the end of Solution explaining why an obvious alternative approach fails. Example: `Ex - Cauchy's theorem via a cyclic action.md` lines 157–158 — "Why the auxiliary group must be $\mathbb{Z}/p$, not $G$ and not $S_p$".]

[**Sanity-check via independent route** — compute the answer by a second method as confidence check. `Ex - Evaluating an integral via residues.md` lines 105–106: "Verification via real-variable calculus: $\int dx/(1+x^2) = \arctan x$, so the result is $\pi$".]

[**Frame-invariance check (physics)** — verify two reference frames or coordinate choices give the same physical answer.]

---

# Key Takeaways

[Elaborate prose paragraphs — **NOT terse bullets, and NOT section headings with sub-bullets**. Each takeaway is a self-contained insight paragraph of at least 6 lines of prose. The reader should finish each takeaway knowing how to solve a class of problems, not just this one.]

[Aim for 3+ takeaways.]

**[Takeaway 1 — a descriptive phrase]**

[Full paragraph: what feature of the problem signals this approach? When else does this pattern apply? Give concrete examples of other problems where the same technique works. Explain what to look for — the "trigger" — and what the general pattern of application is.]

**[Takeaway 2 — a descriptive phrase]**

[Full paragraph...]

[**Optional cross-link to companion exercises:** a closing paragraph naming related exercises that drill the same or complementary techniques. Example: `Rings I/Ex - Boolean rings are commutative.md` line 165 references "see [[Ex - Generating sets that are not bases]]".]
```

---

## Exercise Index Page Template

One page per sub-chapter section. Lists all exercises with per-exercise dependency links. The filename — `Exercise Index - §X.Y [Section Title].md` — must be byte-identical to the wikilink in the parent topic page's exercise-index callout: use the exact `[Section Title]` string the topic page uses for that section's `## §X.Y` concept-map header, so the callout link resolves.

```markdown
---
type: exercise-index
subject: [subject-slug]
section: "[section number]"
tags: [area-tag, subject-tag]
---

## §X.Y [Section Title] — Exercises

[**Contextualizing preamble paragraph** framing the section's purpose and naming the techniques drilled across its exercises. One paragraph before the bullet list. `Group Theory I/Exercise Index - §1.1 Basic Concepts.md` and `Group Theory III/Exercise Index - §1.7 Sylow's Theorems.md` demonstrate the pattern.]

- [[Ex - Exercise Name]] (⭐⭐) — one-line description of technique/pattern drilled ([[Def - A]], [[Thm - B]], [[Def - C]])
- [[Ex - Exercise Name]] — one-line description ([[Thm - D]], [[Def - E]])
- [[Ex - Exercise Name]] — one-line description ([[Def - F]], [[Thm - G]], [[Thm - H]])

[Aim for at least 3 exercises per section.]

[The parenthesised wikilinks after each exercise are the complete list of definitions and theorems invoked in that exercise's solution — per-exercise prerequisites, not section-level prerequisites. This lets the reader see exactly which concepts each exercise drills. Enclose the list in parentheses, never square brackets: a `[` placed immediately before a `[[wikilink]]` produces `[[[`, which Obsidian mis-parses, breaking the link.]
```
