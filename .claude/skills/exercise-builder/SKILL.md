---
name: exercise-builder
description: >
  Create practice exercises for computational and mathematical skill-building as interlinked Obsidian markdown
  pages in the vault. Six modes: (1) algorithm & data-structure atomic derivations; (2) competitive-programming
  problems rephrased to formal specifications; (3) calculation drills for integration, ODEs, PDEs, and
  multivariate calculus; (4) mathematical-modeling / physical-formulation exercises (set up the equations, do
  not solve); (5) approximation-method exercises centred on validity conditions; (6) exam-level exercises for
  topics already in the vault, tightly linked to existing definition and theorem pages with full
  rigorous-solution toggles. Trigger phrases: "exercises for X," "practice X," "drill X," "algorithm
  derivations," "competitive programming," "ICPC problems," "practice integrals," "calculation drill,"
  "formulate this physically," "model this system," "approximation exercises," "more exercises on X," "exam-level
  exercises for X," "harder problems on X."
---

# Exercise Builder — Obsidian Edition

A skill for creating practice exercises for computational and mathematical skill-building, written as interlinked Obsidian markdown pages in the study vault. It is the practice-generating companion to the `polymath-notes` skill: where `polymath-notes` builds the conceptual scaffolding (topic pages, definitions, theorems), this skill builds the drill material that turns that scaffolding into fluency.

The skill has **six modes**, each triggered by a different kind of request:

1. **Algorithm & Data Structure Derivations** — atomic derivations of standard and advanced algorithms.
2. **Competitive Programming Problems** — real contest problems rephrased to formal specifications.
3. **Calculation Drills** — integration, ODEs, PDEs, multivariate calculus.
4. **Mathematical Modeling / Physical Formulation** — set up the equations from a physical description; do not solve.
5. **Approximation Methods** — drill *when* an approximation is valid, not just how to compute it.
6. **Exam-Level Exercises for Existing Vault Topics** *(primary mode)* — additional exam-level exercises tightly integrated with notes already in the vault.

All six produce **Obsidian markdown files in the vault**, never Notion pages, and follow the repo's formatting conventions exactly (see [Obsidian Formatting](#obsidian-formatting) below and `../polymath-notes/references/obsidian-patterns.md`).

---

## Core Philosophy

This skill creates practice exercises structured for efficient spaced practice in 5-minute chunks. Every exercise should be structured so that:

1. The user can attempt it in a 5-minute practice session — or it is broken into subparts that each take approximately 5 minutes.
2. There are hints at the right level: the minimal information needed to unblock, not a full solution walkthrough.
3. The solution includes not just the answer but *why this approach works* and *when to use it*.
4. Each exercise builds a transferable skill, not just knowledge of a specific problem.

The unifying thread across all six modes is **sources and targets**: recognising what you have (the problem's structure, the given assumptions) and what you need (the output, the proof target, the quantity to compute), then routing through known techniques. Every exercise drills this recognition skill. A solution that produces the right number but does not make the reader better at recognising *when to reach for this technique again* has failed the core test, regardless of how clean the arithmetic is.

---

## Cross-Cutting Patterns

These patterns are inherited from `polymath-notes` and apply across **all six modes**. They are not a separate mode — they are elements to weave into every category where relevant. When a mode's structure calls for "atomic rederivation," "convergent strategy," "legal operations," or a "why does it work" note, this is what those terms mean.

### Atomic Rederivation

The minimal information needed to reconstruct a solution from scratch. Structure:

- **Key insight** — the single recognition that unlocks the problem.
- **Subgoal decomposition** — each subgoal gives the *minimum* hint needed to rederive that step (not the step itself; the hint that lets you find the step). Mark the non-obvious subgoal as *Key insight*.
- **Full solution** in a collapsible callout: `> [!note]- Full solution` (or `> [!note]- Full pseudocode` for Mode 1).

Design criterion: **reading only the hints should let you reconstruct the full solution.** If the hints leave a genuine gap that the full-solution callout has to fill with a surprise, the decomposition is incomplete — add the missing subgoal.

### Convergent Problem-Solving Strategies

When building a *set* of exercises in any mode, extract the recurring patterns into a strategy section. This is condensed **bottom-up from the solved exercises**, never written top-down from theory. After solving many problems, ask: "what did I actually do? which step was the crux?" When most problems route through the same few patterns, those patterns *are* the strategy. The section contains:

- **Common targets** — what are we usually trying to find, prove, or compute in this problem class?
- **Common assumption patterns** — what structural features do problems in this class typically present?
- **Strategy catalog** — for each strategy: name; when to use it (trigger condition); what it gives you; template or recipe; common pitfalls.
- **Decision procedure** — given a new problem, how to choose which strategy applies.

For Mode 2 this lives in a `# Convergent Strategies` section on the index page; for Mode 3 and Mode 5 it is the closing `# Convergent Strategy Summary` / `# Validity Heuristics Summary` decision tree; for Mode 6 it is the per-exercise `# Convergent Strategy` section that mirrors the `polymath-notes` exercise template.

### Legal Operations

The moves that are allowed and useful in a problem domain, and the moves that are **illegal but tempting**. For each legal operation: how it works, and when to use it (the trigger condition). For each illegal-but-tempting operation: why it fails (a *concrete counterexample*), and what additional condition would make it legal. Reuse the `> [!warning]` callout for the illegal-but-tempting entries, exactly as the topic-page Legal Operations sections do. In Mode 6 the exercise's `# Legal Operations Used` section references the topic page's Legal Operations by number rather than re-deriving them.

### "Why Does It Work"

For algorithms, techniques, and theorems used in solutions: *why you should expect them to work*, independent of the formal proof. The intuition that makes the result unsurprising. This is the same standard as the `# Why Is It True` section on `polymath-notes` theorem subpages — not a proof sketch, but the mechanism stated so plainly that the correctness stops being a surprise. Include a single **bolded one-line mechanism summary** wherever one exists.

---

## The Six Modes

### Mode 1: Algorithm & Data Structure Derivations

**Trigger:** "algorithm derivations," "derive Dijkstra," "atomic derivation of segment tree," "algorithm catalog," "data structure derivations."

Create a catalog of atomic derivations for commonly-used and advanced algorithms and data structures. This follows the `polymath-notes` "minimal information for maximal reconstruction" pattern, organised as a **flat list (or loosely grouped by theme)** rather than a prerequisite DAG, since algorithms are more independent of one another than mathematical theorems are.

**Structure per algorithm / data structure** (one page each, or grouped thematically):

- **Problem it solves** — what input/output specification does this address?
- **Why does it work** — the core invariant or structural insight that makes the algorithm correct. Not a proof sketch; the intuition that makes correctness unsurprising. For a data structure: what structural property is maintained, and why that property is exactly what enables the desired operations.
- **Key complexity claim** — time and space complexity, *with a justification of why*, not just the big-O.
- **Atomic rederivation scaffold** — numbered subgoals, each a minimum hint to reconstruct that part of the algorithm; mark the non-obvious step as *Key insight*.
- **Full pseudocode** in a collapsible callout: `> [!note]- Full pseudocode`.
- **Legal operations / key design decisions** — why each choice and not the obvious alternative. For example: "why a min-heap and not a sorted array? `decrease-key` is $O(\log n)$ versus $O(n)$."
- **Trigger conditions** — when to reach for this algorithm: what structural features of a problem signal it is the right tool. *This is the transferable skill* and is the most important field on the page.
- **Variants & extensions** — a brief list. For Dijkstra: Bellman–Ford for negative edges, A\* with an admissible heuristic, bidirectional Dijkstra.

**Grouping.** Organise by theme (graph algorithms, tree data structures, string algorithms, dynamic-programming patterns, and so on) but impose no artificial dependency ordering. Cross-reference with wikilinks where one algorithm uses another as a subroutine (Dijkstra wikilinks the priority-queue / binary-heap page; Kruskal wikilinks the union-find page).

**Scope.** Standard algorithms (Dijkstra, Kruskal/Prim, BFS/DFS, binary search, mergesort, quicksort, the common dynamic-programming patterns) and advanced data structures (segment trees, Fenwick/binary-indexed trees, suffix arrays, union-find, balanced binary search trees, tries, persistent data structures, heavy-light decomposition). Prioritise algorithms that are frequent in competitive programming.

**Page type.** Use a `type: algorithm` (or `type: derivation`) frontmatter value with `subject`, `tags`, and a `prereqs` list of any algorithm/data-structure pages used as subroutines. Files live in a dedicated subject folder, e.g. `Study notes/Computer Science/Algorithms/`, named `Algorithm - Dijkstra.md`, `Data Structure - Segment Tree.md`, or grouped, e.g. `Graph Algorithms - Shortest Paths.md`.

### Mode 2: Competitive Programming Problems

**Trigger:** "competitive programming problems," "ICPC problems," "UKIEPC problems," "Leetcode hard," "Topcoder problems," "give me CP problems on [topic]."

Source actual problems from competitive-programming contests, rephrase them to remove narrative fluff, and create exercise pages with atomic rederivation scaffolds.

**Sourcing.** Web-search and download problems (plus available editorials and solutions) from: past ICPC regional and world-final sets, UKIEPC sets, Leetcode Hard, Topcoder Division 1, and Codeforces Division 1 (rating 1800+). De-emphasise computational geometry unless it is specifically requested. **Cite the source** — contest name, year, and problem letter or number — in the page frontmatter (`source:`) and on the page.

**Rephrasing — critical.** Remove **all** narrative and story framing. Replace it with a formal specification:

- **Input** — what it represents (a graph, a sequence, a matrix) and its constraints.
- **Output** — what it should satisfy, or what is computed, optimised, or decided.
- **Constraints** — time and space limits, input-size bounds.

For example, "Alice is planning a trip through $N$ cities connected by $M$ roads, minimising fuel..." becomes "Given a weighted graph with $N$ vertices and $M$ edges, find the minimum-cost Hamiltonian path, or determine that none exists."

**Page structure.** An **index page** lists each problem as a foldable bullet (using the repo's concept-map foldable-bullet convention: the parent bullet holds the wikilinked problem name + difficulty + source; the child bullet holds the formal Input / Output / Constraints), with a linked subpage per problem. If enough problems share patterns, add a `# Convergent Strategies` section to the index (see [Cross-Cutting Patterns](#convergent-problem-solving-strategies)).

**Per-problem subpage:**

- **Problem Statement** — the rephrased formal specification.
- **Classification** — Target (optimisation / counting / decision / construction); Key structural feature (what determines the approach — "DAG structure enables dynamic programming," "monotonicity enables binary search on the answer"); Algorithm/technique used.
- **Atomic Rederivation** — Key insight (the single recognition that unlocks it); subgoal decomposition with minimum hints, marking the non-obvious steps.
- **Solution** — full pseudocode in a collapsible callout `> [!note]- Solution`, with complexity annotations.
- **Why This Approach Works** — why the key insight is correct, and what structural property it exploits.
- **Technique Trigger** — the transferable rule: "When you see $X$, consider $Y$ because $Z$."

**Difficulty ordering.** ★ (standard application), ★★ (non-obvious reduction or combination), ★★★ (significant insight or several techniques composed). Use the ⭐ glyph in frontmatter `difficulty` to match the rest of the vault.

### Mode 3: Calculation Drills (Integration, ODEs, PDEs, Multivariate Calculus)

**Trigger:** "practice integrals," "ODE exercises," "PDE exercises," "calculation drill," "solve this integral," "integration practice," "physics calculation exercises," "multivariate calculus exercises," "inverse function theorem problems," "implicit function theorem."

Create exercise sets for the computational skills needed in physics and engineering: integration techniques, solving ODEs, solving PDEs, and multivariate calculus (inverse function theorem, implicit function theorem, change of variables, Lagrange multipliers, the Stokes / divergence / Green's theorems, and differential forms).

**Design principles:**

1. **Formula/technique sheet at the top** — a self-contained collapsible callout listing every technique and formula needed to solve all exercises in the set. *Every exercise in the set must be solvable using only this sheet.* It serves both as a reference and as a study target in its own right.
2. **Increasing difficulty** — from routine single-technique application to multi-step combinations.
3. **Physics/engineering relevance** — prefer integrals, ODEs, and PDEs that arise in real physics and engineering; state the physical context whenever possible (this integral is the field of a charged ring; this ODE is a damped oscillator; this PDE is the heat equation on a rod).
4. **Technique recognition** — for each exercise, explain what structural feature tells you which technique to apply. *This is the transferable skill.*

**Page structure.**

- A top collapsible callout `> [!note]- 📋 Formula & Technique Sheet` containing:
  - A **Techniques Catalog** — per technique: Formula/method; When to use (a *specific* trigger condition); Common pitfalls; Template skeleton.
  - A **Key Formulas** list — standard integrals, ODE solution forms, Green's functions, and so on.
- Then **Exercises**, each with: a self-contained statement (with physical context if applicable); a *Technique signal* line (what tells you which technique); a collapsible `> [!note]- 💡 Hint` callout (identify the technique and the key first step — do **not** solve); a collapsible `> [!note]- ✅ Solution` callout (the full solution, with each step annotated with **why** not just **what**, plus a closing "Why this technique" note).
- End with a `# Convergent Strategy Summary` written as a **decision tree**: "If the integral has form $X$, use technique $Y$ because $Z$."

**Sourcing.** Web-search exercise sheets from: MIT OpenCourseWare (18.01, 18.02, 18.03, 18.04, 18.152), Cambridge Mathematical Tripos past papers, ETH analysis and physics sheets, and textbook problem sets (Apostol, Boas, Strauss, Evans). Select the physics- and engineering-relevant problems and arrange them by difficulty.

**File location.** A drill set lives alongside the topic it relates to, e.g. `Study notes/Analysis/.../Calculation Drill - Contour Integration.md`, or as a standalone set under the relevant subject folder. Use `type: exercise-set` (or `type: drill`) frontmatter.

### Mode 4: Mathematical Modeling / Physical Formulation

**Trigger:** "formulate this physically," "model this system," "set up the equations," "physical formulation exercises," "what equations govern this," "formulation drill."

Given a physical description, the exercise is to determine *what equations to set up and what theorems are relevant* — **without solving**. This drills the translation from physical reality to mathematical language. Cover at least two formulation types:

- **Differential-equation formulations** — PDE/ODE boundary-value problems from fluid dynamics, heat transfer, electromagnetism, wave propagation, quantum mechanics, and so on.
- **Linear-algebra formulations** — systems of linear equations from statics (force/moment balance $\to A\mathbf{x} = \mathbf{b}$), structural analysis, finite-element discretisations, circuit networks (mesh or nodal analysis), least-squares, and linear programming. Here the exercise is to identify the unknowns, assemble the system matrix, and state the constraints.

Recognising **which framework** a physical problem maps to is itself a core skill, and is the reason the two formulation types live in one mode.

**Design principles:**

1. **Self-contained theory toggles** — each problem carries a collapsible callout containing *all* theory needed to formulate the model, explained from scratch (for a circuits problem: Kirchhoff's laws, Ohm's law, the capacitor and inductor constitutive relations). Usable regardless of the reader's background.
2. **Diverse domains** — statics, dynamics, rigid-body mechanics, fluid dynamics, electromagnetism, circuits, thermodynamics, heat transfer, structural analysis, finite elements, special relativity, waves and acoustics, quantum mechanics. The point is to recognise modelling patterns that recur across domains.
3. **Legal operations frame** — per domain, identify the legal operations (conservation laws, constitutive relations, boundary-condition types, symmetry arguments, equilibrium conditions, compatibility equations) and how each constrains the formulation.
4. **Formulation only** — the exercise *ends* once the equations are written. No solving.

**Page structure.**

- `# Overview`.
- A `# Cross-Domain Legal Operations` section:
  - **Conservation laws** — *trigger:* stuff flows or accumulates.
  - **Constitutive relations** (Hooke, Ohm, Fourier, Fick, Newtonian viscosity) — *trigger:* relating a flux, stress, or force to a driving gradient.
  - **Boundary conditions** — Dirichlet, Neumann, Robin, periodic, radiation.
  - **Symmetry reduction** — *trigger:* rotational, translational, or planar symmetry.
  - **Dimensional analysis** — natural scales and dimensionless groups.
- Then **Problems**, each with:
  - A collapsible `> [!note]- 📖 Required Theory` callout, **self-contained**: Governing equations with each term explained; Key theorems stated precisely with a why-true note; Legal operations for this domain; Common modelling assumptions with their validity conditions (e.g. "incompressible flow when the Mach number $\mathrm{Ma} < 0.3$").
  - A **Physical description** — the "input" to be translated.
  - A **Task** list: What are the governing equations? What boundary conditions? What simplifying assumptions, and why? What is the resulting mathematical problem?
  - A collapsible `> [!note]- 💡 Hint`.
  - A collapsible `> [!note]- ✅ Model Solution`: Step 1 identify the physics; Step 2 governing equations with justification; Step 3 boundary conditions with type and justification; Step 4 simplifying assumptions with validity; Step 5 the final clean mathematical formulation; plus a closing "Why this formulation" note. **The solution stops at the formulation — never solve the equations.**

**Sourcing.** Web-search from: engineering textbook sheets (Çengel, Incropera, Griffiths, Landau & Lifshitz, Batchelor), structural/FEM texts (Hibbeler, Cook, Zienkiewicz), circuit texts (Nilsson & Riedel, Hayt), university exams (Cambridge Engineering Tripos, MIT, Stanford, Imperial), and fluids sheets (Acheson, Kundu). Aim for at least 3–4 different physics domains per set, mixing DE-type and linear-algebra-type formulations.

### Mode 5: Approximation Methods

**Trigger:** "approximation exercises," "when is Taylor expansion valid," "Stirling approximation," "linearization exercises," "when can I approximate," "asymptotic expansion practice," "approximation methods drill."

The key skill is knowing **when** an approximation is valid, not just how to compute it. Covers Taylor expansion, Stirling's approximation, the saddle-point / Laplace method, linearisation, the small-angle approximation, WKB, perturbation theory, and continuum limits.

**Design principles:**

1. **Rigorous theory toggle per method** — a collapsible callout with the rigorous mathematical foundation (Taylor's theorem with the Lagrange remainder, the multivariable version, and the radius of convergence; Stirling with error bounds and the next-order corrections; and so on). This grounds the informal heuristics. Each toggle also includes an **Informal heuristic** (what physicists mean by "expand to first order," and when it is safe) and a **Validity-condition quick-check** (the fast test — e.g. "the expansion parameter $\varepsilon$ satisfies $|\varepsilon| \ll 1$ *and* the higher-order terms decay").
2. **Validity conditions as the core skill** — every exercise solution must explicitly state: (a) which approximation was used; (b) what condition makes it valid here; (c) what would break if the condition failed; (d) how to estimate the error.
3. **Diverse fields** — thermodynamics, quantum mechanics, statistical mechanics, optics, fluid dynamics, electromagnetism, astrophysics. Recognise the *context pattern* for when an approximation applies, across domains.
4. **Informal heuristics + rigorous backing** — provide both the quick heuristic and the rigorous statement; the exercises drill translating between the two levels.

**Page structure.**

- A `# Rigorous Foundations` section with one collapsible callout per method: `> [!note]- 📐 [Method] (Rigorous)` (full statement, validity conditions, error bound, informal heuristic, validity quick-check).
- Then **Exercises**, each with: a statement from a physics or engineering context; a difficulty rating; a collapsible `> [!note]- 💡 Hint` (which approximation, and what the small parameter is); a collapsible `> [!note]- ✅ Solution` (Approximation used; Why valid here — identify the small parameter, verify the condition, estimate the error; What would break; The calculation).
- Include at least one **trap problem** (★★★) where a commonly-applied approximation is **not** valid — the exercise is to recognise this and explain why.
- End with a `# Validity Heuristics Summary`: a decision table — "When you see $X$ in domain $Y$, approximation $Z$ is likely valid because $W$; check condition $V$ before applying."

**Sourcing.** Web-search from: physics textbook exercises (Griffiths, Sakurai, Pathria, Jackson, Landau & Lifshitz), applied-mathematics texts (Bender & Orszag — essential for asymptotics), engineering estimation problems, and past physics exams. **Trap problems where the obvious approximation fails are the most valuable** — prioritise finding them.

### Mode 6: Exam-Level Exercises for Existing Vault Topics

**Trigger:** "more exercises on X," "exam-level exercises for X," "harder problems on X," "add exercises to X" — where $X$ is a subject that **already has study notes in the vault**.

**This is the primary mode.** Given a topic that already has a topic page plus definition and theorem subpages in the vault, generate additional high-quality, exam-level exercises that integrate tightly with the existing notes. Use this mode when the goal is to *deepen practice on material already studied*, rather than to build a standalone drill set.

**Before writing anything:**

1. **Locate the topic's existing pages** in the vault — the topic page, all `Def -` and `Thm -` subpages, existing `Ex -` pages, and the Exercise Index pages. Read them to learn: the exact page titles to wikilink; the Legal Operations section of the topic page; the available definitions and theorems; and the difficulty and style of the existing exercises (so new ones *extend* rather than *duplicate*). Use `grep`/`find` over `Study notes/[Subject Area]/[Topic]/`.
2. **Identify which sections or theorems are under-exercised** and target those.

**Three criteria define this mode — all mandatory:**

**Criterion 1 — Maximal self-containedness via linking.** Every technical term in the problem statement and the solution must either be **wikilinked** to its page in the existing notes, or — if it has no page — explained inline in **bold**. Every theorem, lemma, or property invoked in the solution must be wikilinked to its `Thm -` / `Def -` page (or explained inline if no page exists). Use **transclusion** (`![[Page#Section]]`) in a `**Recall:**` section at the top of each exercise to embed the exact statements of the definitions and theorems the exercise depends on, exactly as the existing `Ex -` pages do. A reader with zero prior context should be able to reach full understanding by reading the page and clicking its links. *This is a higher self-containedness bar than any other mode.*

**Criterion 2 — Full rigorous solution in a toggle, immediately after the problem.** Directly after the problem description (and its Recall section) place a single collapsible callout containing a complete, rigorous, self-contained solution. Use the repo's collapsed-by-default callout syntax `> [!note]- Full solution` (the trailing `-` collapses it). Inside, follow the repo's established solution structure: a plan paragraph (~3 sentences summarising the whole route), per-step bolded summary lines, a nested `> [!note]- Derivation` callout under each step with the full computation, and a final `> [!note]- Complete formal solution` callout giving a clean self-contained proof. The solution must be **genuinely rigorous** — no skipped steps, every invoked result linked or proved. Progressive `> [!note]- Hint N` callouts may still appear between the problem and the full-solution toggle, but the full rigorous solution toggle is the required centrepiece of this mode.

**Criterion 3 — Source from top-university exams, with official solutions.** Web-search for exam questions from top universities — MIT, Imperial, Cambridge (Tripos), Stanford, ETH, Princeton, Harvard, Oxford — and qualifying exams. Aim for genuinely difficult problems, but specifically ones where the difficulty is calibrated so that *"because the relevant theorem is linked in the Recall section, the solver knows which theorem to reach for"* — the challenge is in the **execution** and in **recognising how to apply a known tool**, not in guessing an obscure result. Prefer problems for which an officially released solution exists (official exam solutions, problem-set solution keys, instructor solutions); find these and base the written solution on the official version, **citing the source** (university, course code, year). When no official solution exists, solve it rigorously yourself and say so.

**Page structure for Mode 6** — one `Ex -` subpage per exercise, following the existing exercise template exactly:

- **Frontmatter:** `type: exercise`, `subject:`, `difficulty:` (⭐ rating), `prereqs:` (the `Def -`/`Thm -` page titles used), `tags:`, and a `source:` field citing the university / course / year.
- `# Problem Statement` — the problem, with all technical terms wikilinked.
- `**Recall:**` — transclusions (`![[...#Section]]`) of every definition and theorem the exercise depends on, plus brief bold restatements of any companion facts that have no page.
- The `> [!note]- Full solution` toggle (Criterion 2), placed immediately after the problem and recall.
- `# Convergent Strategy` (the four labelled paragraphs: **Problem class**, **Assumption pattern**, **Theorem routing**, **Key decision point**), `# Legal Operations Used` (wikilinked to the topic page's Legal Operations section by number), progressive `> [!note]- Hint N` callouts, and a `# Key Takeaways` section, all matching the existing `Ex -` pages.

**Also update the relevant Exercise Index page(s)** to list each new exercise as a foldable bullet: the wikilinked name + a one-line summary + the difficulty tag + the dependency wikilinks in parentheses (parentheses, never square brackets). The wikilink to the new file must be **byte-identical** to the new file's title.

---

## Obsidian Formatting

The skill produces Obsidian markdown files in the vault, never Notion pages. Any instruction inherited from a Notion workflow (toggles, callout blocks, embeds) must be rendered in Obsidian syntax. Per `../polymath-notes/references/obsidian-patterns.md`:

- **Math.** `$...$` inline, `$$...$$` display. Never backtick-dollar. Wrap every variable and symbol in prose in `$...$`. Use only core MathJax/KaTeX commands — no amsmath or physics-package macros, no `\newcommand`. **Never** put `$...$` inside a wikilink; use Unicode characters in wikilink display text instead (σ, ℝ, →, Lᵖ, …).
- **Links.** `[[wikilinks]]` for all cross-references. A wikilink target must already exist or be created in the same batch; otherwise write the term in **bold plain text** (a wikilink to a missing page creates an empty stub when clicked in Obsidian). This matters most in Mode 1 and Mode 2, where many referenced algorithms may not have pages yet — bold them until the page exists.
- **Transclusion.** `![[Page#Section]]` for the Recall sections in Mode 6.
- **Collapsible toggles.** Use callout syntax `> [!note]- Title` — the trailing `-` collapses by default. Nest by adding `> >`. Use `> [!warning]` for illegal-but-tempting-route warnings, and `> [!tip]` for unlocked-downstream callouts. **Do NOT use HTML `<details>`/`<summary>`** — wikilinks inside them are not clickable in Obsidian, and they do not collapse reliably in Reading view. Every toggle the original specification described as a Notion toggle becomes a collapsible callout here.
- **Foldable bullets** (Mode 2 index pages, Mode 6 index updates) use the repo's concept-map convention: a parent bullet with the wikilinked name, an indented single-line child bullet with the statement. Do not use `<details>` for these.
- **File location.** Exercise and drill pages go in `Study notes/[Subject Area]/[Topic]/` alongside the topic pages they relate to, following the existing `Ex - [Name].md` and `Exercise Index - §X.Y [Section Title].md` naming. Windows-portable filenames only — no `< > : " / \ | ? *` characters (spell out fractions and asterisked notation, per `obsidian-patterns.md`).
- **Frontmatter.** Follow the existing exercise frontmatter pattern (`type`, `subject`, `difficulty`, `prereqs`, `tags`) shown in the repo's `Ex -` pages; add a `source:` field for Modes 2 and 6.

For the full specification, see `../polymath-notes/references/obsidian-patterns.md`. This skill's own `references/` directory points at that file rather than duplicating it.

---

## Integration with polymath-notes

This skill is designed to dovetail with `polymath-notes`, not to stand apart from it:

- Exercises **wikilink to** the definitions, theorems, and topic pages created by `polymath-notes`.
- The `# Legal Operations Used` section **references the topic page's Legal Operations section** by wikilink and by number.
- **Recall sections use transclusion** from the definition and theorem subpages.
- When adding exercises to an existing topic, **update the relevant Exercise Index page** (Mode 6 mandates this).
- Mode 1 algorithm derivations follow the **same atomic-rederivation and "why is it true" patterns** as `polymath-notes` theorem subpages — the algorithm page is, structurally, a theorem page whose "theorem" is the algorithm's correctness and complexity claim.

---

## Quality Standards

**For hints.** *Bad:* "Use dynamic programming." *Good:* "The subproblems have optimal substructure: the best solution for positions $1..i$ depends only on the best solutions for $1..j$ with $j < i$. Define $\mathrm{dp}[i]$ as the minimum cost to reach position $i$, and consider which previous positions transition to $i$." The hint identifies the key recognition but leaves the execution to the user.

**For technique recognition (trigger conditions).** *Bad:* "Use integration by parts when you have a product." *Good:* "Use integration by parts when you have a product of two functions where one gets simpler on differentiation (polynomials, logarithms) and the other has a known antiderivative (exponentials, trigonometric functions). The LIATE rule gives a rough heuristic: Logarithmic $>$ Inverse-trig $>$ Algebraic $>$ Trigonometric $>$ Exponential for the choice of the factor to differentiate."

**For theory toggles (Mode 4).** They must be genuinely self-contained. The test: *could someone with strong mathematical maturity but zero background in the specific domain read the toggle and formulate the model?* If not, add more context — the governing equations stated precisely, what each term means physically, the boundary-condition types and when each applies, and the modelling assumptions with their validity conditions.

**For approximation validity (Mode 5).** Every solution explicitly identifies the approximation used, the small parameter, the validity condition, an error estimate (even a rough one), and a scenario where the approximation would fail. **Trap problems** where the obvious approximation is invalid are especially valuable.

**For Mode 6.** Every technical term and every invoked result is linked or explained (Criterion 1); the full rigorous-solution toggle skips no steps (Criterion 2); problems come from named top-university exams with official solutions cited where they exist (Criterion 3).

**Across all modes.** Each exercise must build a transferable skill — after solving it, the reader should be better at recognising *when to reach for this technique again*, not merely able to reproduce this one answer. An exercise whose takeaway is specific to its own numbers has failed the core test.

---

## Interaction with Other Skills

- **polymath-notes** — algorithm derivations and exercises follow the same atomic-rederivation and "why is it true" patterns; Mode 3–6 exercises reference theory from `polymath-notes` pages, and Mode 6 cannot run without an existing `polymath-notes` topic to attach to.
- **prereq-backchain** — after a study plan is identified, `exercise-builder` creates the practice materials for each topic in the plan.
- **research-connector** — cross-field exercises (a technique applied in a distant domain) drill the same recognition skill that `research-connector` demands; a surprising application surfaced by `research-connector` is a natural Mode 3 or Mode 5 exercise.
