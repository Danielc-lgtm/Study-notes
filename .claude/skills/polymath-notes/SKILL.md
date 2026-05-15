---
name: polymath-notes
description: >
  Create structured mathematical study notes as interlinked Obsidian markdown pages from uploaded lecture notes,
  textbooks, and papers (supplemented by web search). Use whenever the user asks to create study notes, write up
  a topic, or study an area of mathematics, physics, or theoretical computer science. Trigger phrases: "create
  notes on X," "study X," "write up X," "add X to my notes," "I want to learn X." Also trigger for specific
  components: "legal operations in X," "sources and targets for theorem Y," "axiom motivation for definition Z,"
  "why is theorem X true," "most reusable properties in X," "relate X to Y." Creates chapter-level topic pages
  with definition, theorem, and exercise subpages — designed for spaced retrieval practice with rapid context
  re-entry across many subjects studied simultaneously. Content follows uploaded source material structure by
  default, enriched with the skill's elements (axiom motivations, sources and targets, legal operations,
  convergent strategies, insight standards, etc.).
---

# Polymath Notes — Obsidian Edition

A skill for creating structured mathematical study notes as interlinked Obsidian markdown pages, designed for polymathic study across many fields simultaneously.

## Context

The user studies approximately 130 subjects simultaneously, organized via a prerequisite DAG. They may not return to a given topic for weeks or months. The notes must support rapid context re-entry, self-contained understanding from any entry point, and high-density insight that enables rederivation from minimal hints. The vault lives in a GitHub repo and is managed through Claude Code.

---

## Core Philosophy

Six principles govern every page, section, and sentence in the notes.

### 1. Hierarchical Structure

The top-level page shows the big picture: all notation, definitions, theorems, and exercises for a chapter in one place. Every layer deeper reveals more detail. The concept map on the topic page has toggles containing rigorous statements; each toggle links to a full subpage; each subpage has its own toggles for proofs, derivations, and worked solutions. The same principle applies to all content: conceptual insight and motivation are the first visible thing at every level, and details are progressively revealed through collapsible sections and linked pages. A reader should be able to choose their depth of engagement at every point.

### 2. Self-Containedness Everywhere (via DAG Links)

Someone with zero background in a subject should be able to jump into any page — exercise, definition, theorem — and understand what is going on, either from the page itself or by clicking through linked pages. Exercises have a Recall section restating all definitions and theorems used, with wikilinks to those pages. Definitions and theorems similarly link to and recall their own dependencies. The DAG structure of wikilinks is what makes this work: every concept is reachable from every other concept through a chain of links, and each link leads to a page that is itself self-contained.

Use Obsidian transclusion (`![[Page Name#Section]]`) for Recall sections wherever possible. This embeds the actual definition or theorem statement inline, so the reader sees the full content without navigating away, and changes to the source propagate automatically. When transclusion would be too bulky or when a condensed restatement is more appropriate, write a brief restatement in your own words and include a wikilink.

### 3. Connections

Use the DAG wikilink structure to surface conceptual connections — both within a subject and across subjects. Linking should be frequent and intentional. When a definition in group theory is the same construction as one in topology, link them. When a proof technique in analysis is an instance of a general pattern used in probability, link the pattern. The Obsidian graph view makes these connections visible: every wikilink is an edge in the graph, and the resulting structure should reflect the true dependency and analogy structure of mathematics.

### 4. Self-Containedness with Respect to Time

Exercises are broken into subparts and lemmas such that a reader can jump in, gain enough context from a single subpart, and practice just that piece in approximately 5 minutes. Alternatively, a reader can take the subparts as given and attempt the full exercise. This decomposition also applies to theorem proofs: the lemma decomposition breaks a proof into independently-practiceable chunks, each in its own collapsible section with statement, hint, and full proof.

### 5. Insight Density Maximized Without Sacrificing Volume

The goal is high density (a small amount of information enables reconstructing a lot) AND high volume (do not abbreviate, do not omit, do not sacrifice completeness). Every section should focus on the kind of insight that would allow the reader to rederive the exercise, definition, or theorem from a minimal hint — given an understanding of what assumptions can be leveraged and what we are trying to achieve. But the total amount of insight should also be large: multiple perspectives, multiple examples, multiple connections. The appearance of conciseness comes from hierarchical structure (collapsible sections, linked subpages), never from omitting content.

The Conceptual Insight Standards section below describes the specific types of high-density insight to aim for.

### 6. Large Total Content via Web Search, Structured Digestibly

The user uploads lecture notes as the basis for each topic. Claude Code should do frequent web searches for additional lecture notes, textbooks, papers, exercise sheets, and exam papers to supplement the uploaded material. Search queries like "[topic] lecture notes pdf", "[topic] exercises university", "[topic] qualifying exam problems solved", "[topic] textbook exercises solutions" are useful. The total content should be large — more examples, more exercises, more perspectives than any single source provides — but structured digestibly through the hierarchical principle and DAG-linked pages.

---

## Conceptual Insight Standards

The following describes the types of high-density insight that should permeate the notes. These are what make the difference between notes that are formally correct and notes that enable genuine understanding and rederivation. A note that is formally correct but lacks these insights is not yet good enough.

### Universal Principles

These are structural patterns of insight that apply across all mathematical fields. When writing any section of any page, actively look for opportunities to deploy these.

**Unifying Frames.** A single perspective that reinterprets many objects, results, or techniques in a field as instances of one underlying idea. When a good unifying frame exists for a topic, state it prominently in the Motivation section and show how specific constructions are instances of it. Example: in stochastic processes, the underlying reality is a space of sample paths with their associated measures — finite-dimensional distributions are marginalizations, existence questions are clearest at the sample-path level, and observations "rule out" inconsistent paths (making the framework fundamentally Bayesian). Example: in linear algebra, a vector is a platonic object and its representation under a basis is a particular viewing — the uniqueness of decomposition with respect to a basis is the central fact from which everything else (injectivity, surjectivity, rank-nullity) flows.

**True Names.** The characterization of a concept that is maximally operational for problem-solving, as opposed to the "official" definition. When the true name differs from the standard definition, state both and explain why the true name is more useful in practice. Example: the true name of compactness in analysis is "bounded sequence implies convergent subsequence," not the open-cover definition. This is what you actually reach for when proving compactness or using compact operators.

**Input-Type Broadening (Backpropagation).** For each major theorem or tool, identify the conditions under which it applies (its "input type") and then actively work to broaden recognition of when those conditions are met, by building bridges from diverse source situations. Example: DCT requires a dominating function — for a Cauchy sequence {fₙ}, take fₙ + ε as the dominating function, bridging Cauchy sequences to DCT's input type. Once this bridge is built, encountering a Cauchy sequence should trigger thinking about DCT. In Legal Operations sections, each technique should have its input type explicitly stated along with known bridges.

**Trigger-Reaction Patterns.** Compact procedural associations: "when you see X, do Y." These should be scattered throughout the notes wherever they arise naturally — in Legal Operations, in theorem pages, in exercise takeaways, in definition pages. They are among the highest-density insight formats: a single sentence can unlock the solution to a class of problems. Examples: "prove an infinite sum converges → bound each term by ε2⁻ⁿ"; "see a difference inside an integral → Mean Value Theorem"; "want to pass a limit inside an integral → DCT or MCT"; "proving continuity ⟺ proving boundedness (for linear maps)." Write these as they arise; do not collect them in a separate section.

**Inheritance — "Where Does the Property Come From?"** Properties like compactness, completeness, and convergence have to come from somewhere. They are often inherited from a simpler or more fundamental space. Always ask and answer: where is this property actually coming from? Example: the diagonal argument for proving compactness of sequences of sequences works by "inheriting compactness from ℝ" — at each point, extract a convergent subsequence using the compactness of ℝ, then diagonalize. Completeness of Lᵖ ultimately derives from completeness of ℝ. Manifold properties pull back to Euclidean space.

**Local-to-Global Propagation.** When a local property is satisfied at every point or within a set, ask whether it assembles into a coherent global property. Example: the implicit function theorem gives local structure at each point of a preimage; assembling these local charts gives the manifold structure of the preimage. When local conditions hold everywhere in a set, check whether they add up to a global structure.

**Platonic-vs-Representation / Abstract-Before-Concrete.** Distinguish the mathematical object itself from any particular way of representing or viewing it. Definitions should be understood at the abstract level first, with concrete representations as instances. Example: a tangent vector is an abstract object; its representation as a tuple of numbers depends on a choice of chart. The projection map in the tangent bundle is the price of keeping things general enough to work "up to isomorphism."

**Density as a Strategic Lever.** Many problems in analysis are solved by approximating with a dense subclass (typically smooth or simple functions), solving the problem there, and passing to the limit. The density strategy converts hard problems about general functions into tractable problems about nice functions plus an approximation error to control. When encountering a problem about a general object in a space with a known dense subclass, this pattern should be one of the first things tried.

**Truncation / Anti-Truncation.** A dual pair of techniques for handling infinite-dimensional or infinite-sum problems. Truncation makes things finite; anti-truncation bounds what is left over. These show up whenever you need to go between "for each finite piece" and "for the whole infinite object." Example: in Hilbert spaces, each element has finite norm so coefficients in any basis expansion must decay. This decay is what makes weak convergence work. To convert weak to strong convergence, control the tail norm via anti-truncation.

### Domain-Specific Insight Examples

Beyond the universal principles, individual fields have their own characteristic insight patterns. These are examples of what field-specific insight looks like — they illustrate the quality bar, not an exhaustive taxonomy.

**Escape-to-Infinity as Divergence Mechanism (Analysis).** When two notions of convergence can diverge, the specific mechanism is often that "mass escapes to infinity" — a bump moves out but does not shrink. DCT and MCT are precisely conditions that rule out this escape. Similarly, weak convergence fails to imply strong convergence in Hilbert spaces via the same mechanism: the orthonormal basis eₙ converges weakly to 0 but not strongly. When writing about convergence notions, always identify what mechanism causes the gap between them and what conditions close the gap.

**Manifold Properties Pull Back to Euclidean Space (Geometry).** Most properties of manifolds become clear once you pull them back to the underlying Euclidean space. The manifold inherits its structure from the simpler object we already understand — the complexity is in the gluing, not in the local behavior.

These examples are illustrative. Each field will generate its own characteristic insight patterns as you study it. The skill's insight standards should grow as the user contributes their own axiom motivations, conceptual frames, and problem-solving insights through study. When the user provides new insights (in conversation, in their personal notes, or by reference to their work), incorporate them into the notes and — when they represent a general pattern — into the skill's examples over time. The goal is that the skill's conceptual insight standards become a growing distillation of the user's own mathematical taste, so that the skill can generate notes at a comparable level of insight even for topics the user has not studied yet.

---

## Writing Style

The notes have two registers. **Formal definitions and theorem statements** should be precise, complete, and stated in standard mathematical language. Everything else — motivations, axiom motivations, "why is it true" explanations, legal operations, bridges, takeaways, problem-solving strategies — should be written in the style of David Tong's Cambridge lecture notes: conversational but precise, clean but never dry, always grounding abstract machinery in the concrete problems it solves.

Tong's style has specific qualities worth emulating:

He writes as if he is talking to you at a whiteboard. Each paragraph advances the reader's understanding, and the text flows naturally from problem to concept to definition, rather than presenting labeled sections with disconnected content. When introducing a concept, he opens with the situation that calls for it — what you are trying to do, what goes wrong without the concept, and why this specific construction resolves the difficulty. The formal definition arrives as the punchline, not the starting point.

He mixes short, direct sentences with longer explanatory ones. "Gauge symmetry is, at heart, a redundancy in our description of the world. Yet it is a redundancy that has enormous utility" — this is the rhythm to aim for. He is honest about difficulty and about what is genuinely deep versus what is merely technical.

He weaves in the bigger picture alongside the details. The notes should do both: a motivation that illuminates the grand structure, followed by the precise computation that makes it rigorous.

Specific principles:

- **Prose over bullets.** Use flowing paragraphs for motivations, insights, and explanations. Reserve numbered or bulleted lists for genuinely enumerative content (lists of assumptions, lists of operations, lists of examples) where the items are parallel in structure. Even Legal Operations, which are naturally list-like, should have prose explanations under each item.
- **Build from what the reader knows.** The notes should be self-contained relative to the user's existing knowledge. Explain concepts that are outside the user's background; do not explain concepts the user already knows well. The user's background is described in the CLAUDE.md file and evolves over time.
- **Concrete before abstract.** Motivate definitions with the specific problems they solve before stating them. Explain theorems with simple cases and intuition before giving formal statements. The formal statement is the destination; the motivation is the path that makes it unsurprising.
- **No hedge stacking.** Do not write "this might potentially be useful." Be direct and confident when stating mathematical facts. Reserve hedging for genuinely uncertain claims.
- **Not inspirational.** Do not write "this beautiful theorem reveals deep connections." Write the explanation that makes the connection visible, and let the reader draw their own conclusions.
- **No abbreviation.** Write full words and phrases. Do not abbreviate "with respect to" as "w.r.t." or "if and only if" as "iff" in prose (mathematical notation like ⟺ in formal statements is fine). Every section should read as complete, polished prose.
- **Brief historical or philosophical asides when they illuminate.** A sentence about what problem led to a definition, or a remark about why a particular formulation is odd or surprising, can ground the mathematics in human experience. But keep these brief and relevant — they should clarify, not decorate.

What NOT to write: labeled headers within explanations ("Trigger:", "Action:", "Principle:"), excessive parallelism in sentence structure, bullet-point prose where flowing text would work, hedge stacking ("potentially," "might possibly"), or anything that reads like corporate communication or a textbook's marginal notes.

---

## Workflow

### Step 1: Determine scope and mode

The user will request either:
- **A full topic page** (e.g., "create notes on Fredholm theory" or "chapter 3 of functional analysis") — create the topic page and all definition/theorem/exercise subpages. A topic page is more like a chapter than a summary — there can be many topic pages for one subject. The length is unconstrained.
- **A single component** (e.g., "what are the legal operations in measure theory" or "axiom motivation for the Zariski topology") — produce just that component. See Component-Only Mode below.

### Step 2: Check for existing pages

Before creating any page, search the Obsidian vault for existing pages covering the same concepts. Use `grep`, `find`, or search the vault directory to check whether definition or theorem pages already exist. If they do, link to them with wikilinks rather than creating duplicates.

### Step 3: Gather source material

The notes are built from source material, not from scratch. Two sources:

1. **User uploads** — the user uploads lecture notes, textbook chapters, or papers. These are the primary source. **No content from uploaded source material should be missed** — every definition, theorem, proof, and exercise in the uploaded material must be included in the notes.
2. **Web search** — search the web for additional lecture notes, textbooks, exercise sheets, and exam papers on the topic. Use queries like "[topic] lecture notes pdf", "[topic] exam questions solutions", "[topic] exercises university". These supplement the user's uploads with additional exercises, alternative expositions, and coverage of material the uploads may lack.

The **structure of the uploaded lecture notes is the default structure** for the topic page. Follow the order in which concepts are presented in the source material. Only deviate when there is a specific reason to (e.g., a DAG violation where the source introduces a concept before its prerequisites).

### Step 3.5: Check user's personal notes

The user may provide a link to their personal notes (a Notion page or other source) containing terse, low-context bulletpoints — framings, observations, and connections discovered during study. If a Notion link is provided and the Notion MCP is connected, fetch the page directly. If the MCP is not connected, ask the user to paste the relevant content. When personal notes are provided:

1. Fetch the page and scan for relevant entries
2. Reverse-engineer the full conceptual insight from the terse shorthand, using the user's mathematical background and the surrounding context of the topic
3. Incorporate the insight seamlessly into the study notes at the appropriate location — as part of axiom motivations, "why is it true" explanations, legal operations, bridges, insights, or trigger-reaction patterns
4. Do NOT reproduce the bulletpoints verbatim or in a separate section. The goal is that the final notes read as if the insight was always part of the explanation

### Step 4: Generate content

Read the templates in `references/templates.md` for the exact structure of each page type. Read `references/obsidian-patterns.md` for Obsidian-specific formatting patterns (collapsible sections, equations, links, transclusion, frontmatter, etc).

When generating content:

- Write mathematical notation using standard LaTeX: `$...$` for inline math, `$$...$$` for display math. Obsidian uses MathJax/KaTeX and renders both correctly.
- Be precise and formal in definitions and theorem statements.
- Write all other content in David Tong style prose (see Writing Style above).
- For proofs, structure them as small independently-provable lemmas in collapsible sections.
- For cross-field connections, only include connections that are precise and operational, not vague analogies.
- Permeate the notes with the Conceptual Insight Standards — unifying frames, true names, trigger-reaction patterns, input-type broadening, and the other insight types described above.
- **Follow the source material's structure by default.** The skill's elements (axiom motivations, sources and targets, legal operations, insights, etc.) are added to the source material's structure, not imposed over it.
- **Include every element when suitable, but do not force it.** Every section described in the templates should be included when there is genuine content for it. If a particular theorem genuinely has no good cross-field exercise suggestions, omit that section rather than padding with weak content.
- **Aim just above the user's range.** For each chapter, when the definitions and theorems are sufficient to define or understand concepts from a more advanced field (e.g., group theory unlocks definitions in algebraic geometry), include those advanced concepts in the chapter's concept map. Use web search to identify what is unlocked. State them concisely, linked to their eventual home in the DAG. Do not include full axiom motivations or proofs for these; those belong in future topic pages. The purpose is forward motivation, early exposure, and working-memory exploitation.
- **Add YAML frontmatter to every page.** See `references/obsidian-patterns.md` for the schema.

### Step 5: Write all pages to the vault

Write each page as a markdown file in the appropriate location in the Obsidian vault. The vault structure follows the subject hierarchy:

```
Study notes/
  [Subject Area]/
    [Topic].md                    # topic page
    [Topic]/
      Def - [Name].md            # definition subpage
      Thm - [Name].md            # theorem subpage
      Ex - [Name].md             # exercise subpage
      Exercise Index - §X.Y.md   # exercise index
```

All pages use wikilinks (`[[Def - Group]]`) for internal cross-references. After writing all pages, verify that every wikilink resolves to an existing file. If a link target does not exist yet (it refers to a definition from another topic not yet written), the wikilink is left as-is — Obsidian will show it as an unresolved link, which is fine and serves as a natural TODO indicator.

### Step 6: Cross-link

After all pages are created, scan every page for references to defined concepts and ensure they use wikilinks. This includes references in Legal Operations, Problem-Solving Strategy, Most Reusable Properties, Bridges, Insights, and prose throughout. The same concept may be linked with different display text: `[[Def - Compactness|compact]]` and `[[Def - Compactness|compactness]]` both linking to the same page.

### Step 7: Commit to repository

After all pages are written and cross-linked, stage and commit the new files to the git repository with a descriptive commit message (e.g., "Add Group Theory I — §1.1–1.2 notes with 12 definitions, 5 theorems, 8 exercises"). Push if the user has requested it. This ensures all work is preserved even if the session ends.

### Step 8: Self-Evaluation

Run the self-evaluation checklist (see Quality Standards below). Report which items passed and any that required fixes.

---

## Page Types

There are five page types. See `references/templates.md` for complete templates.

### Topic Page

A chapter-level page containing the study notes for a mathematical topic. There can be multiple topic pages per subject (e.g., "Group Theory I — §1.1–1.2", "Group Theory II — §1.5–1.7"). Each topic page is self-contained: its own Notation Registry, Motivation, Concept Map, Sources and Targets, Legal Operations, Problem-Solving Strategy, Most Reusable Properties, Bridges, and Insights.

**Concept map format:** This is the single place where the reader sees all definitions, theorems, and exercises for the chapter. Each entry is a **foldable bullet**: a parent bullet holding the wikilinked name, with an indented child bullet holding an unambiguous, rigorous statement or definition (3–5 sentences with key details, examples, and connections). Folding the parent bullet collapses the statement; the wikilink stays clickable in both Editing and Reading view because it is ordinary Markdown. Each name links to the full subpage. Definitions, theorems, and exercises are interleaved in natural reading order following the source material. Do not use HTML `<details>` blocks for concept-map entries — wikilinks inside HTML tags are not clickable in Obsidian, and such blocks do not collapse reliably in Reading view.

**Non-definition/theorem content:** If the source material does not fit neatly into definition/theorem format (e.g., extended explanations, derivations, computational techniques), the concept map entries become subchapter-style page links, and the linked pages contain the explanatory content organized according to the core philosophy principles.

**Sizing:** A topic page covers a natural sub-chapter unit of the source material, typically a range of sections (e.g., §1.1–1.2). There is no cap on the number of definition/theorem entries a topic page may contain; split topic pages only at natural sub-chapter boundaries that follow the source material's section structure, with cross-references between them.

**"Aim just above the user's range":** For each chapter, when the definitions and theorems unlock concepts from a more advanced field, include those advanced concepts in the concept map (use web search to find them). Mark them clearly as previews.

Contains the following sections (see templates for full structure):

1. **Notation Registry** — always visible (not collapsed), every symbol used in the topic's subpages
2. **Motivation** — why this topic exists, what problems it solves, clarity and unambiguousness emphasized
3. **Concept Map** — all definitions, theorems, exercises as foldable bullets (wikilinked name on the parent, statement on an indented child), per-section exercise index callouts
4. **Sources and Targets (topic-level)** — Targets: "what sorts of properties or desiderata do we usually try to prove in this subject?" Sources: "what sorts of assumptions are usually given or leveraged?" Both derived post-hoc from exercises
5. **Legal Operations** — fully self-contained (a person with zero background should understand), derived post-hoc from exercises. 7+ legal operations, 3+ "illegal but tempting" with counterexamples
6. **Problem-Solving Strategy** — written as self-contained paragraphs (not tables), explaining when to use which techniques and why, such that a reader with no background could substantially improve their ability to solve exercises. Follows the insight density principle
7. **Most Reusable Properties** — bullet-point format but each bullet is a comprehensive paragraph with wikilinks and "Typical use" descriptions
8. **Bridges** — self-contained paragraphs, connections as rigorous as possible, definitions and theorems from other fields explained or linked (or both)
9. **Insights** — a dedicated section for conceptual insights that do not fit neatly into the other categories: unifying frames for the topic, true names, cross-cutting observations, surprising connections, heuristics, and any other high-density insight worth recording. Written as prose paragraphs

### Definition Subpage

A page for a single definition (or a small cluster of tightly related definitions). Contains the material needed to reconstruct the definition from scratch. Every section is written in paragraph form — maximize insight density without sacrificing volume. No abbreviation of phrases or words.

**Compound definitions:** When a definition page covers multiple related concepts (e.g., "Ring Homomorphism, Isomorphism, Characteristic"), every concept in the title must receive a proper, complete definition — not just a passing mention. A concept listed in the title but given only a one-sentence mention elsewhere is a quality failure.

Contains:
1. **Notation** — restated for self-containedness
2. **Axiom Motivation** — the minimal information needed to invent this definition: desiderata, what should it capture and exclude, what breaks if weakened or strengthened, sometimes a forward-reference to a theorem that requires it
3. **The Definition** — formal statement
4. **Categorical Definition** — when a natural categorical formulation exists. Must be self-contained: explain the relevant categorical concepts, do not assume the reader knows category theory unless the topic page is itself about category theory
5. **Relate to Other Fields / Compression** — precise cross-field connections
6. **Examples / Corollaries** — concrete examples and non-examples, and immediate corollaries that serve as calibration checks: if the reader can verify each one, they have understood the definition correctly. Include both "is an instance" and "is NOT an instance" examples. Each should probe a different aspect of the definition
7. **Unlocked by This** — downstream concepts from more advanced fields (optional)

### Theorem Subpage

A page for a single theorem. Contains the material needed to understand, apply, and rederive the theorem.

Contains:
1. **Notation** — restated for self-containedness
2. **Motivation** — what question this answers, what gap existed before
3. **Sources and Targets (theorem-level)** — fundamentally different from a simple "assumptions and conclusions" list. See detailed description below.
4. **Why Is It True** — intuition independent of the formal proof, NOT a proof sketch. No length constraint.
5. **What Makes This Hard** — 2–3 sentences identifying where most people get stuck, what the non-obvious step is, and what the common errors are. Directly useful for spaced practice: when returning after months, this tells the reader where to focus.
6. **Rederivation Scaffold** — high-level strategy (2–3 sentences) plus subgoal decomposition with minimal hints. Self-sufficient: reading only this section should let the reader reconstruct the full proof.
7. **Lemma Decomposition** — each lemma independently practiceable in approximately 5 minutes, in collapsible sections with statement, hint, why needed, and full proof
8. **Formal Proof** — complete proof in a collapsible section (ground truth for verification)
9. **Cross-Field Exercise Suggestions** — intentionally loose: find the most out-of-distribution, least obvious contexts where the theorem applies, to battle-test the Sources. Does not have to be from a different field. Use web search to find surprising applications.
10. **Bridges** — links to related theorems/concepts
11. **Unlocked by This** — downstream concepts (optional)

**Detailed description of Sources and Targets for theorems:**

This is NOT a simple list of "Input: X, Output: Y." The theorem has a precondition A.

**Sources (input broadening):** Find a wide variety of properties B such that B implies A, so that the reader can recognize the theorem applies to objects with property B — even when B looks nothing like A at first glance. Aim for B where the implication B → A is nonobvious, and where B is a commonly encountered assumption in problems. These should be derived downstream from exercises: after seeing the theorem used in many problems, what were the actual starting points that led to invoking it? For each B: state B precisely, explain why B → A holds (the bridge argument), and give an example problem where starting from B you would invoke this theorem.

**Targets (output amplification):** The theorem gives conclusion C. Find corollaries of C, but also find properties D and E such that C combined with D implies E, where the combination is nonobvious. The target section is about how the theorem can be used and combined with other results to derive further properties. Also derived downstream from exercises. For each combination: state the additional property D, state what you get (E), and explain why this combination is useful.

### Exercise Subpage

A page for an exercise or problem. Self-containedness is paramount: a reader should be able to open any exercise subpage cold and fully understand the problem, strategy, and solution without clicking away.

Contains six sections (Sources and Targets is NOT included — it was removed):
1. **Problem Statement** — with full Recall section restating all needed definitions (using transclusion `![[Def - Name#The Definition]]` where appropriate), with wikilinks to definition/theorem subpages
2. **Convergent Strategy** — problem class, assumption pattern, theorem routing with explicit route, key decision point. Focus on what it is about the problem that makes a particular technique suitable or helpful
3. **Legal Operations Used** — which operations from the topic page and how they are applied
4. **Hints** — progressive collapsible hints (2–4), from gentle nudge to near-giveaway
5. **Solution** — hierarchical structure where the top level gives the highest-density insight (the key idea and result of each step), and collapsible sections allow gradually looking at the solution in more detail. Complete formal solution in a final collapsible section. Every invoked theorem or definition restated at point of use with wikilinks.
6. **Key Takeaways** — elaborate paragraphs (not terse bullets) focusing on what makes the technique suitable for this type of problem and maximizing generalization: being able to solve a wide variety of similar problems. Each takeaway should be a self-contained insight paragraph.

**Difficulty calibration:** Each exercise has a difficulty tag in its YAML frontmatter: ⭐ (routine application of one theorem), ⭐⭐ (requires combining theorems or a non-obvious step), ⭐⭐⭐ (competition-level or requires genuine creativity). This helps with session planning when studying across many subjects.

### Exercise Index Page

One page per sub-chapter section listing all exercises for that section. Each exercise wikilink is followed by bracketed wikilinks to every definition and theorem used in that exercise's solution. Aim for at least 3 exercises per sub-chapter section. Integrated into the topic page's concept map as a callout at the end of each section.

---

## Component-Only Mode

When the user requests a single component (not a full topic page), produce just that section. Components that can be requested individually:

- Notation registry, axiom motivation, sources and targets (topic-level or theorem-level), why is it true, legal operations, problem-solving strategy, most reusable properties, rederivation scaffold, cross-field exercise suggestions, convergent strategy, solution, bridges, categorical definition, relate to other fields, insights

In component-only mode, output the content in chat. If the user asks to add it to an existing page, write it to the appropriate file.

---

## Quality Standards — Self-Evaluation Checklist

Before finalizing, evaluate against this checklist. For each item, verify compliance and fix issues before presenting the result.

**Completeness:**

1. **Source coverage.** Every definition, theorem, proof, and exercise in the uploaded source material appears in the notes. If anything was omitted, add it.
2. **Exercise coverage.** Each sub-chapter section has at least 3 exercises. If any section has fewer, search the web for additional exercises.
3. **Per-section exercise index exists.** Each sub-chapter section has a dedicated exercise index page integrated into the concept map as a callout.
4. **Cross-linking.** Every reference to a defined concept throughout all pages uses a wikilink to the relevant subpage. Spot-check at least 5 references in Legal Operations, Problem-Solving Strategy, and Bridges.
5. **Frontmatter present.** Every page has YAML frontmatter with type, subject, and prereqs fields.

**Quality — Self-Containedness:**

6. **Self-containedness spot-check.** Pick 3 random subpages: can a reader understand the page without clicking any links? Are definitions restated (via transclusion or restatement) at point of use? Are theorem statements recalled when invoked? If not, add the missing context.
7. **Exercise recall completeness.** Each exercise has a Recall section restating or transcluding all definitions and theorems needed to understand the problem, with wikilinks.

**Quality — Insight:**

8. **Axiom motivations are inventive, not descriptive.** Each definition subpage's axiom motivation passes the test: "Could a reader who has never seen this definition invent it from the motivation alone?" If not, strengthen it.
9. **"Why Is It True" is independent of the proof.** Each theorem's "Why Is It True" conveys intuition without being a proof sketch. If it reads like an abbreviated proof, rewrite it.
10. **Rederivation scaffolds are self-sufficient.** Each scaffold passes the test: "Could someone who has seen this proof before but forgotten it reconstruct it from the scaffold alone?"
11. **Legal Operations are actionable.** The reader can scan the list when stuck on a problem and try each operation. If any operation is too vague to attempt, make it concrete.
12. **Problem-Solving Strategy is self-contained.** A reader with no background in the field could read this section and substantially improve their ability to solve exercises. Written in paragraph form, not tables.
13. **Concept map sections are substantive.** Each collapsible section in the concept map contains 3–5 sentences with key details, examples or non-examples, and connections — not just a terse 1-sentence restatement.
14. **Insight density.** Spot-check 3 random pages: does the content exhibit the Conceptual Insight Standards? Are there trigger-reaction patterns, unifying frames, true names, or input-type broadening where appropriate?

**Quality — Format:**

15. **Prose over bullets in motivations.** Motivations, "Why Is It True," axiom motivations, problem-solving strategy, bridges, and takeaways use flowing paragraphs, not bullet-point inventories.
16. **No abbreviation.** Full words and phrases throughout prose sections.
17. **Compound definition completeness.** For every definition page whose title lists multiple concepts, verify that every concept receives a proper, complete definition.
18. **Hierarchical structure.** Exercise solutions use the hierarchical principle: top level shows highest-density insight, collapsible sections reveal progressively more detail.
19. **Difficulty tags present.** Every exercise has a difficulty tag (⭐/⭐⭐/⭐⭐⭐) in its frontmatter.

**Quality — New Features:**

20. **Theorem Sources and Targets quality.** For at least 2 theorems, verify that the Sources contain nonobvious B → A bridges (not just restating the precondition), and Targets contain nonobvious C + D → E combinations (not just restating the conclusion).
21. **"What Makes This Hard" present.** Every theorem subpage has a "What Makes This Hard" section identifying the non-obvious step.
22. **Insights section exists.** The topic page has an Insights section with at least 2 substantive prose paragraphs.
23. **Web search supplementation.** At least 2 web searches were performed for additional exercises, perspectives, or "aim above range" concepts beyond the uploaded source material.
24. **Topic-level Sources and Targets.** The topic page has a Sources and Targets section with recurring proof targets and assumption patterns, written as prose and derived from the exercises.

**Report:** After checking, briefly report which items passed and any that required fixes. If all items pass, state "Self-evaluation passed: all 24 checklist items verified."
