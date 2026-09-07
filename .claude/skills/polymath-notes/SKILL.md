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

**The prose baseline for the entire vault is the owner's thesis, `prose/Chiang Sung En-Thesis.pdf`.** Read it before writing (extract with `pymupdf`; see `references/prose-and-proof-standard.md` §1 for the calibration passages with page numbers) and keep it open while writing. `references/prose-and-proof-standard.md` is the full specification of the register and of the proof standard below; this section is its summary. (Earlier drafts of this skill named David Tong's lecture notes as the exemplar; the thesis replaces that register everywhere.)

The notes have two registers. **Formal definitions and theorem statements** are precise, complete, and stated in standard mathematical language, with labelled parts when there are several. Everything else — motivations, axiom motivations, "why is it true" explanations, legal operations, bridges, takeaways, problem-solving strategies — is written in the thesis's expository register, whose shape is always the same:

1. **Orient** — say where the reader is and what this piece does; pose the guiding question as a question.
2. **Motivate** — name the problem, the alternatives, and what goes wrong without the construction, in ordinary academic prose (the thesis's "globalist versus localist" paragraphs in §1.1 are the model).
3. **State formally** — the definition or theorem as the punchline, crisp and complete.
4. **Unpack immediately in the smallest concrete case** — the bivariate instance, the three-element lattice with its actual $3 \times 3$ matrices, the five partitions of $\{X, Y, Z\}$ written out. A general statement that has not been instantiated is not yet explained.
5. **Re-explain in a remark titled by its purpose** — the thesis's *(Intuition: …)*, *(Significance of …)*, *(Importance of the … assumption)*, *(Verification of …)* remarks; in the vault these are the Axiom Motivation, Why Is It True, What Makes This Hard, and True-name sections, and the standard for their content is the thesis's: an intuition is re-derived, not asserted.
6. **Close in words** — after every result and computation, a sentence saying what has been shown and what it means.

The voice is the thesis's: a measured academic first-person plural ("we now prove", "we need to show", "note that"), direct, unornamented, expansive on purpose. Every claim travels with its reason on the same line ("since …", "because …", "by …"). The thesis re-explains — "In other words, …", "Intuitively, …" — and the notes do too: comprehensive prose is preferred over compact formalism even when it runs several times longer, and a formula is introduced only where prose would genuinely be worse.

Specific principles:

- **Prose over bullets.** Use flowing paragraphs for motivations, insights, and explanations. Reserve numbered or bulleted lists for genuinely enumerative content (lists of assumptions, lists of operations, lists of examples) where the items are parallel in structure. Even Legal Operations, which are naturally list-like, should have prose explanations under each item.
- **Build from what the reader knows.** The notes should be self-contained relative to the user's existing knowledge. Explain concepts that are outside the user's background; do not explain concepts the user already knows well. The user's background is described in the CLAUDE.md file and evolves over time.
- **Concrete before abstract.** Motivate definitions with the specific problems they solve before stating them. Explain theorems with simple cases and intuition before giving formal statements. The formal statement is the destination; the motivation is the path that makes it unsurprising.
- **No hedge stacking.** Do not write "this might potentially be useful." Be direct and confident when stating mathematical facts. Reserve hedging for genuinely uncertain claims.
- **Not inspirational.** Do not write "this beautiful theorem reveals deep connections." Write the explanation that makes the connection visible, and let the reader draw their own conclusions.
- **No abbreviation.** Write full words and phrases. Do not abbreviate "with respect to" as "w.r.t." or "if and only if" as "iff" in prose (mathematical notation like ⟺ in formal statements is fine). Every section should read as complete, polished prose.
- **No proof requires the reader to visualise a shape described only in words.** Every geometric object — contour, region, domain, surface, curve, distribution, neighbourhood — that appears in a definition, theorem, or proof must come with an explicit *formulaic* specification alongside any verbal description. Write "the annulus $\{z \in \mathbb{C} : r < |z - z_0| < R\}$" not "the annulus"; write "the keyhole contour $\gamma = \gamma_R \cup \gamma_\delta \cup \gamma_+ \cup \gamma_-$, with $\gamma_R(t) = z_0 + R e^{i(\theta_0 + t)}$ for $t \in [\theta_1, 2\pi - \theta_1]$, $\gamma_\delta(t) = z_0 + \delta e^{i(2\pi - \theta_1 - t)}$, and $\gamma_\pm$ the two radial corridor segments at angles $\pm\theta_1$, then $\delta, \theta_1 \to 0$" not "the keyhole contour, indented around the branch point". When two proofs of the same theorem exist — one coordinate/algebraic, one geometric — **prefer the coordinate one**. Examples: Goursat's lemma uses **axis-aligned rectangle subdivision** (subdivide $[a,b] \times [c,d]$ into four congruent sub-rectangles $[a,(a+b)/2] \times [c,(c+d)/2]$, etc.) not triangle subdivision; deformation arguments use [[Thm - Green's Theorem|Green's theorem]] applied to an explicit parametrised region when regularity permits, not "deform the contour by homotopy"; orientations are stated via the determinant / volume-form criterion, not "right-hand rule". This is not anti-geometric: the intuitive picture stays in the prose, but every geometric claim has a parallel analytic specification that stands on its own. A reader following the proof on paper, without drawing a single picture, should be able to reconstruct every region, curve, and limit from the formulas. The shape-in-words pattern fails three groups: readers who think algebraically by default, readers who cannot easily visualise (aphantasia and intermediates), and the future-self reader re-entering the page after months without the picture in working memory.
- **Brief historical or philosophical asides when they illuminate.** A sentence about what problem led to a definition, or a remark about why a particular formulation is odd or surprising, can ground the mathematics in human experience. But keep these brief and relevant — they should clarify, not decorate.

- **Standard terminology, typed symbols.** Every concept carries the literature's name; no coined compound nouns used as if established. Every symbol is declared and typed at its first use and keeps one meaning for the whole page.

What NOT to write: labeled headers within explanations ("Trigger:", "Action:", "Principle:"), excessive parallelism in sentence structure, bullet-point prose where flowing text would work, hedge stacking ("potentially," "might possibly"), whiteboard chattiness, or anything that reads like corporate communication or a textbook's marginal notes.

---

## The Proof Standard

**Every theorem, lemma, proposition, or corollary that the notes mention is proved, in full, with self-contained rigour, and the thesis's fully written proofs are the minimum level of detail.** The complete rule, the eleven-point description of the thesis floor, the placement rules, the model proof, and the single permitted exception are in `references/prose-and-proof-standard.md` Part II; what follows is the summary that every page must satisfy.

- **Mentioned means proved.** A result that is stated on a concept map, given a `Thm -` page, invoked inside a proof, used in an exercise solution, used to verify an example on a definition page, or named in a Bridge or Insight as something the reader may lean on, has a complete proof in the vault, on that result's own page (`# Formal Proof`, fed by `# Lemma Decomposition`). Every other place that uses it wikilinks that page and restates the statement at the point of use.
- **No statement-only pages.** Never create `Thm - X (Statement)`, and never write a `Thm -` page whose Formal Proof is a sketch, a citation, or empty. When a page being written depends on an existing statement-only page, supply the complete proof on that page or write a new fully proved page and link that instead.
- **The thesis floor, on every proof.** Open by naming what is assumed and what must be shown. Organise by labelled blocks (Direction 1 / Direction 2, Case 1 / Case 2, Part I / Part II, Step 0, 1, …), each announced with what it establishes. Introduce each move with a bold lead-in naming it. Put a justification on every displayed line ("(by factorization)", "(since …)", "(by Lemma 2)"). Invoke every hypothesis by name where it is used. Spell out well-definedness, existence, and equivalence-relation checks clause by clause. Prove both directions, all cases, all parts — "similarly" is expanded, not written. Combine numbered intermediate results explicitly. Close in words. Cite the theorem that licenses every interchange of limit, sum, integral, or derivative, and verify every regularity condition where it is used. No "clearly", "obviously", "it is easy to see", "one checks", "left to the reader", "omitted".
- **Depth is not an excuse.** Elliptic regularity, Sobolev embedding, Sard–Smale, the Hodge theorem, Chern–Weil, Weitzenböck, moduli-space compactness — proved in full on their own pages, however long; length is handled by lemma decomposition and collapsible structure, never by omission.
- **The single exception — an imported result.** A result whose complete published proof is genuinely book-length (of the order of fifty pages or more even in the most efficient textbook treatment: Freedman's classification, Donaldson's diagonalisation theorem with its analytic package, Uhlenbeck compactness, the Atiyah–Singer index theorem) may be used without proof only inside a `> [!warning] Imported without proof: …` callout that states it exactly, cites a complete published proof by section or page, describes the architecture of that proof, and says why it is imported; it never gets a `Thm -` page or a theorem blockquote; every consequence drawn from it is proved in full with the import named as an explicit hypothesis; and the topic page lists it under `# Imported Results`. Import is the last resort for that handful of results, not a category for anything long.
- **Definitions and exercises are held to the same rule.** Every example on a definition page is verified to be an instance, every non-example verified to fail, every corollary proved on the page or wikilinked to its proof; every exercise's `Complete formal solution` is a complete proof, and every theorem it invokes links to a page with a complete proof.
- **Mechanical gate.** `python3 .claude/skills/polymath-notes/scripts/find-unproved-theorems.py "<unit>"` must come back clean before a unit is committed; the P1 grep for "clearly / obviously / similarly / omitted / sketch" is reviewed line by line.

---

## Source Material

PDF source materials — lecture notes, textbook chapters, papers — are stored in the `sources/` directory of the repository. These are the primary inputs the notes are built from.

When a prompt places a partial-content restriction on a particular PDF (for example, "use only up to Chapter 4" or "only the special relativity sections"), do not read the whole file. First inspect the table of contents to identify the page range covering the relevant chapters — extract the front matter with a tool such as `pdftotext <file> - | head -150`, or read the bookmarks/outline. Then use `qpdf` to extract only the needed pages into a trimmed file before reading:

```
qpdf <file> --pages . <start>-<end> -- /tmp/<name>-trimmed.pdf
```

Read only the trimmed file. This keeps the context window lean and avoids pulling in chapters that are out of scope. The same approach is worthwhile even for PDFs without an explicit restriction: extracting the chapters currently being worked on, rather than reading a large PDF in full, preserves detail fidelity for the section being written.

When multiple source PDFs cover the same topic (e.g., two different lecture notes on group theory), do not default to following one source and ignoring the others. During Pass 1, skim all sources and build a unified content map that identifies the strengths of each — clearer expositions, better exercises, unique coverage, alternative proofs or perspectives.

In Pass 2, use your judgment to combine sources in whatever way produces the best notes. This might mean following one source's structure while pulling exercises from another, interleaving sections from different sources, synthesizing a hybrid ordering, or any other approach. The goal is notes that are better than any single source alone. When sources offer genuinely different proofs or perspectives on the same result, consider including both.

---

## Working Memory (`.scratch/`)

Creating a full topic page is a long task: many source pages skimmed, a content map built, dozens of subpages written, a filename manifest to keep consistent, a link audit to run. Far more passes through this material than fit comfortably in one context window. Use a `.scratch/` directory at the repository root as persistent working memory to extend your effective context.

`.scratch/` is for your own working notes, not vault content — it must be listed in the repository's `.gitignore` so it is never committed. If the directory or the `.gitignore` entry does not exist yet, create them. Within `.scratch/` you have full freedom of structure; organize it however serves the task.

Write to it proactively, whenever future-you would benefit. Useful things to cache:

- **The Pass 1 content map** — the inventory of every chapter, theorem, definition, and exercise across the sources, with notes on each source's strengths. This is the master plan for Pass 2 and is referred to constantly; losing it means re-skimming the PDFs.
- **The filename manifest** — the exact intended filename of every page being created, so wikilinks resolve and cross-references stay consistent. Recoverable with `find`, but cheaper to keep written down.
- **A running log** — decisions made, the section currently being written, what is done and what remains, problems hit and how they were fixed.
- **Source digests** — condensed summaries of source material already read, so it need not be re-read.
- **Reusable tooling** — for instance the link-audit script, so it does not have to be reconstructed.

Read from `.scratch/` whenever you need to recall earlier context — on returning to a task, consult it before re-reading sources or re-deriving a plan. Treat reading and writing `.scratch/` as a normal part of the workflow; no need to ask permission.

---

## Workflow

### Step 1: Determine scope and mode

The user will request either:
- **A full topic page** (e.g., "create notes on Fredholm theory" or "chapter 3 of functional analysis") — create the topic page and all definition/theorem/exercise subpages. A topic page is more like a chapter than a summary — there can be many topic pages for one subject. The length is unconstrained.
- **A single component** (e.g., "what are the legal operations in measure theory" or "axiom motivation for the Zariski topology") — produce just that component. See Component-Only Mode below.

### Step 2: Check for existing pages

Before creating any page, search the Obsidian vault for existing pages covering the same concepts. Use `grep`, `find`, or search the vault directory to check whether definition or theorem pages already exist. If they do, link to them with wikilinks rather than creating duplicates.

**Existing abbreviated treatments to be aware of.** The vault already contains compact, Frankel-depth treatments of several subjects under `Study notes/Geometry/Geometry of Physics/`:

- `Riemannian Geometry/` (RG I–IV) — connections, geodesics, Riemann curvature, classical surfaces
- `Algebraic Topology/` (AT I–III) — singular homology + de Rham, $\pi_1$ + covering spaces, higher homotopy + Chern forms
- `Hodge Theory/` (Hodge I) — Hodge star, decomposition, Bochner
- `Spinors/` — Clifford, Dirac equation, spin bundle
- `General Relativity/` (GR I) — Einstein equations, Schwarzschild
- `Geometric Mechanics/` (GM I) — symplectic manifolds, Hamiltonian dynamics
- `Thermodynamics/` (Thermo I) — Caratheodory's form-theoretic second law

These pages were written to Frankel's *Geometry of Physics* depth — enough to support the physics-bridge program of Differential Geometry, but not a full standalone treatment of any of these subjects.

**When the user asks for a deeper / more complete treatment of one of these subjects** (e.g., "make full Algebraic Topology notes following Hatcher", "write up Riemannian Geometry from do Carmo"), do NOT overwrite or extend the Geometry-of-Physics pages. Instead:

1. **Create a new peer subject folder** at the top level of the relevant area — e.g., `Study notes/Geometry/Algebraic Topology/` as a peer to `Differential Geometry/` and to `Geometry of Physics/`. Or `Study notes/Physics/General Relativity/` as a peer to `Special Relativity/`. The new folder is independent: its topic pages, definitions, theorems, and exercises live entirely inside it.

2. **Link to the existing Geometry-of-Physics pages when adequate.** For routine definitions and theorems the Geometry-of-Physics page may already be at the right depth; in that case, wikilink to the existing page rather than re-writing it. For example, a deep Algebraic Topology treatment might still link to `[[Def - Singular Simplex]]` (under Geometry of Physics) for the basic definition. Filename uniqueness across the vault is preserved automatically by Obsidian's wikilink resolution.

3. **Copy and substantially expand a page when the existing depth is insufficient.** When the deeper treatment needs more (extra examples, an alternative proof, a deeper categorical framing, more exercises), create a NEW page in the new subject folder with a distinct filename (e.g., add a suffix or rephrase: `Def - Singular Homology.md` already exists, so the new page could be `Def - Singular Homology (Hatcher Treatment).md`, or — more commonly — the new chapter's topic page absorbs the deeper exposition and the existing Def page is left in place). Document the relationship in the new page's Bridges section.

4. **Do not delete or rename Geometry-of-Physics pages.** They remain the physics-bridge gateway. The new standalone treatment is additive.

This pattern mirrors how `Special Relativity/` and `General Relativity/` already coexist: SR has its own folder with its own topic pages and subpages; if a fuller GR treatment is later requested, it would go under `Physics/General Relativity (Standalone)/` or similar, not into the Geometry-of-Physics gateway.

**Gauge Theory is a standalone peer subject, not a Geometry-of-Physics gateway.** The series lives at `Study notes/Geometry/Gauge Theory/`, beside `Differential Geometry/`, and is built from `sources/IntroGaugeTheory_LectNotes.pdf` (Haydys) and `sources/mathematical_gauge_theory.pdf` (Wernli) with every theorem proved in full under the Proof Standard. Link to it — not to the Geometry-of-Physics folders — for connections on vector and principal bundles, curvature, holonomy, characteristic classes, Yang–Mills and Maxwell theory, spin geometry and Dirac operators, Sobolev and elliptic theory, Fredholm maps and degree, Seiberg–Witten theory, and four-manifold topology. The earlier Geometry-of-Physics `Gauge Theory/` folder was removed when the standalone series was created; no page should link to its old chapter titles.

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

Read the templates in `references/templates.md` for the exact structure of each page type. Read `references/obsidian-patterns.md` for Obsidian-specific formatting patterns (collapsible sections, equations, links, transclusion, frontmatter, etc). Read `references/prose-and-proof-standard.md` and the thesis it points at (`prose/Chiang Sung En-Thesis.pdf`) before writing any page — together they fix the prose register and the minimum proof standard for the whole vault, and neither can be inferred from the templates alone.

When generating content:

- **Work through source material in two passes.**
  - *Pass 1 (skim):* For each source PDF, extract the table of contents and skim each chapter lightly — read only theorem statements, definition names, and section summaries, not full proofs or exposition. Write a content map listing every key concept, theorem, and definition across all chapters.
  - *Pass 2 (write):* Work through sequentially — read one chapter in full, write all pages for that section, then move to the next. Use the content map from Pass 1 to add forward references and identify cross-chapter connections while working on early chapters.
- Write mathematical notation using standard LaTeX: `$...$` for inline math, `$$...$$` for display math. Obsidian uses MathJax/KaTeX and renders both correctly.
- Be precise and formal in definitions and theorem statements.
- Write all other content in the thesis register (see Writing Style above and `references/prose-and-proof-standard.md` Part I).
- Prove every theorem the notes mention, in full, at or above the thesis floor (see The Proof Standard above and `references/prose-and-proof-standard.md` Part II). Structure each proof as small independently-provable lemmas in collapsible sections, each with its own complete proof, and assemble them in a complete `# Formal Proof`. Never leave a sketch, a citation, or a "(Statement)" page where a proof should be.
- For cross-field connections, only include connections that are precise and operational, not vague analogies.
- Permeate the notes with the Conceptual Insight Standards — unifying frames, true names, trigger-reaction patterns, input-type broadening, and the other insight types described above.
- **Follow the source material's structure by default.** The skill's elements (axiom motivations, sources and targets, legal operations, insights, etc.) are added to the source material's structure, not imposed over it.
- **Include every element when suitable, but do not force it.** Every section described in the templates should be included when there is genuine content for it. If a particular theorem genuinely has no good cross-field exercise suggestions, omit that section rather than padding with weak content.
- **Aim just above the user's range.** For each chapter, when the definitions and theorems are sufficient to define or understand concepts from a more advanced field (e.g., group theory unlocks definitions in algebraic geometry), include those advanced concepts in the chapter's concept map. Use web search to identify what is unlocked. State them concisely, naming the downstream concept in bold; wikilink it only if its page already exists in the vault, since clicking a wikilink to a missing page creates an empty stub in Obsidian. Do not include full axiom motivations or proofs for these; those belong in future topic pages. The purpose is forward motivation, early exposure, and working-memory exploitation.
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

All pages use wikilinks (`[[Def - Group]]`) for internal cross-references. Only wikilink a page that exists or that is being created in the same batch. A forward reference to a concept from a subject not yet in the vault — for instance in an "Unlocked by This" preview — must be written as **bold plain text**, not a wikilink: in Obsidian, clicking a wikilink whose target file does not exist creates an empty stub page. Verification that every wikilink resolves happens in Step 6.

### Step 6: Cross-link

After all pages are created, scan every page for references to defined concepts and ensure they use wikilinks. This includes references in Legal Operations, Problem-Solving Strategy, Most Reusable Properties, Bridges, Insights, and prose throughout. The same concept may be linked with different display text: `[[Def - Compactness|compact]]` and `[[Def - Compactness|compactness]]` both linking to the same page.

**Comprehensiveness rule.** **Every** occurrence of jargon — even a single occurrence buried in prose, even when the jargon is not the exact name of any page — must wikilink to the page that introduces that concept, *unless* the jargon is a forward reference to a concept the vault does not yet define. Two implications:

- If the jargon's filename uses a slightly different phrasing (e.g. the page is `Def - Riemannian Metric` and the prose says "the metric"), use a display-text wikilink: `[[Def - Riemannian Metric|metric]]`. Singular/plural and capitalisation are fine to vary in display text, never inside the `[[ ]]` target. No LaTeX inside the target.
- Exceptions where the bold-plain-text convention is preserved: text inside Unlocked callouts, Bridges, Insights, "Sources and Targets" prose, "True name" lines, and the Notation Registry — these sections curate the gateway from one chapter to the next and intentionally keep forward references bold plain text. Do not retroactively wikilink there.

**Mechanise this.** Maintain an auto-linker at `.claude/skills/polymath-notes/scripts/autolinker.py` that walks the vault, extracts canonical terms from every `Def - <name>.md` and `Thm - <name>.md` filename (with plural/lowercase variants), and inserts a wikilink at the first body-text occurrence in every other page. The auto-linker must:

- Skip protected regions: YAML frontmatter, `$...$` and `$$...$$` math, fenced code, inline code, existing `[[ ]]` and `![[ ]]`, and lines beginning with `#`.
- Skip sections whose header is one of: Notation, Notation Registry, Unlocked by This, Sources and Targets, Bridges, Insights, Calibration check, True name, Relate to Other Fields.
- Skip self-links (a page linking to its own definition).
- Cap insertions per file (e.g. 10) so a single page does not become a wikilink soup.
- Carry a target blocklist for definitions whose name collides too broadly with English usage to auto-link safely. The current blocklisted targets, learned the hard way during the May 2026 vault-wide pass, are `Def - Field` (always loses to "vector field" / "gauge field" / "magnetic field"), `Def - Independence` (loses to "coordinate-independence" / "path-independence"), and `Def - Primitive (Antiderivative)` (loses to "primitive root" / "primitive ideal" / "primitive permutation group"). Extend this list whenever a new false-positive pattern is discovered. **Never remove an entry from the blocklist without re-verifying that the term has stopped being ambiguous in the vault.**

Run `python3 .claude/skills/polymath-notes/scripts/autolinker.py --apply --max-per-file 10` as part of Step 6 after a batch of new pages is written. Inspect the diff, revert any obvious false positives via `find -exec perl -i -pe 's{\[\[Def - X\|([^\]]+)\]\]}{$1}g' {} +`, add the offending target to the blocklist, and re-run.

Then run a mechanical link audit over the whole vault. After stripping `$...$` / `$$...$$` math and code spans — where `[[...]]` can be ordinary notation such as the power-series ring `R[[X]]` — every remaining `[[wikilink]]` must resolve to an existing `.md` file, and every `![[transclusion]]` (including its `#section` anchor) must point to real content. Any unresolved wikilink is a bug: either the target filename is wrong (fix the link) or it is a forward reference that should be bold plain text (unlink it). The audit must come back clean before Step 7.

**Math-region audit.** Also run `python3 .claude/skills/polymath-notes/scripts/find-math-bugs.py` to detect inline math regions with whitespace immediately after the opening `$` or before the closing `$` — both patterns cause KaTeX/Obsidian to fail to close the math, silently swallowing following prose. Apply `fix-math-bugs.py --apply` to repair them mechanically (strips internal whitespace at both math boundaries).

**LaTeX-pattern audit.** Run `python3 .claude/skills/polymath-notes/scripts/find-latex-bugs.py` to detect deeper math-rendering bugs that the whitespace audit misses: (a) `$X$` re-entry inside `\text{...}` without surrounding spaces (e.g. `\text{ is a$\sigma$-algebra}`), which KaTeX renders incorrectly; (b) unpaired `$$` display-math delimiters; (c) brace imbalance and `\\` line breaks in inline math outside `\begin{...}\end{...}` environments; (d) `\left( ... \right)` mismatch. The fix for `\text{$X$Y}` patterns is the split-text idiom: `\text{ ... } X \text{...}` — see `references/obsidian-patterns.md`.

**Wikilink content audit.** Run `python3 .claude/skills/polymath-notes/scripts/find-wikilink-bugs.py` to detect malformed wikilinks: markdown formatting inside display text (`[[X|**Y**]]` renders as literal `**Y**`), nested wikilinks (`[[X - [[Y|Z]]|W]]`), LaTeX inside display (`[[X|$Y$]]` — Obsidian does NOT process math inside wikilink display text, so the dollars render literally), and HTML inside display. Apply three fixers in this order:

- `fix-wikilink-bugs.py --apply` — formatting-in-display fixes (moves `**`/`*`/`__`/`~~`/`` ` `` markers outside the wikilink).
- `fix-nested-wikilinks.py --apply` — collapses nested wikilinks `[[X - [[Y|Z]]|W]]` to `[[Y|W]]`.
- `fix-latex-in-display.py --apply` — substitutes LaTeX commands inside display text with Unicode (e.g. `\sigma`→σ, `\mathbb{R}`→ℝ, `\to`→→, `\Rightarrow`→⇒) and strips the surrounding `$` markers.

**Unproved-theorem audit.** Run `python3 .claude/skills/polymath-notes/scripts/find-unproved-theorems.py "<unit folder>"` to detect violations of the Proof Standard that a scanner can see: statement-only pages (`(Statement)` in the filename), `Thm -`/`Lemma -`/`Prop -`/`Cor -` pages with no `# Formal Proof` section or one that is empty or self-confessedly a sketch, lemma callouts without a nested `Full proof`, and every wikilink into a statement-only page. Every finding is fixed by writing the proof (or, for the handful of book-length results, by converting the use into the `Imported without proof` callout and registering it on the topic page). A clean run is necessary, not sufficient: the line-by-line P1 audit still has to be done.

When writing the scanner itself: be careful that the math-stripping step preserves NEWLINES (replace non-newline chars with spaces) so line-numbering across the stripped and original text stays in sync. And do *not* strip math before checking for `$` in display text — perform the LaTeX-in-display check on the original text or split it into two passes.

See `references/obsidian-patterns.md` for the full rule and offender patterns.

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

1. **Notation Registry** — always visible (not collapsed), every symbol used in the topic's subpages. When the topic relies on a convention (units, sign, default-assumption, default closure such as "all groups finite unless stated"), open with a **standing-convention preamble paragraph** that names the convention, explains the choice, and (where applicable) gives a recipe for converting between conventions. `Special Relativity I` line 11 demonstrates the pattern with the $c = 1$ convention.
2. **Motivation** — why this topic exists, what problems it solves. Written in the thesis register (multiple paragraphs: orient, pose the guiding questions as questions, name the competing approaches and what goes wrong without the new one, give the roadmap — `prose/Chiang Sung En-Thesis.pdf` §1.1 and the §3.1 opener are the calibration passages). Required elements:
   - A clear opening hook in the first sentence — `Modules I` opens "Here is the entire topic in one sentence: a module is a vector space over a ring."
   - When the topic has a **structural backbone** (a hierarchy, a classification, a flow of implications), state it as a **display equation in Motivation**: e.g., `Rings II` line 41 places the hierarchy `field ⊂ ED ⊂ PID ⊂ UFD ⊂ ID` as a single display, referenced throughout the chapter.
   - A closing **audience-assumption paragraph** stating what the reader is assumed to know (which background topics they should have refreshed before working through this one). `Special Relativity I` line 48 demonstrates the pattern.
3. **Concept Map** — all definitions, theorems, and exercises as foldable bullets, wikilinked name on the parent, statement on an indented child (3–5 sentences with key details, examples or non-examples, and connections — not just a one-sentence restatement). **Exercises must appear inside the concept map with inline difficulty tags** `(⭐)`/`(⭐⭐)`/`(⭐⭐⭐)`, in natural reading order alongside the definitions and theorems they drill — `Multivariate Analysis II`, `Topology II`, `Complex Analysis II`, `Special Relativity I` all demonstrate this. **Each concept-map section must end with a `> [!note] Exercise Index — §X.Y` callout pointing to the index page.**
4. **"Unlocked" tips in the concept map** — when a section's definitions and theorems unlock concepts from a more advanced field, include at least one `> [!tip] Unlocked: [Concept Name] *(from [Advanced Field])*` callout inline at the appropriate point in the concept map. **No upper cap on the number of unlocks per section** — `Special Relativity I §1.3` has three unlocks, and that is correct when three different downstream fields are unlocked. The "aim just above the user's range" principle (`Skill core philosophy #6 / workflow Step 4`) is enforced at this level: *every* sub-chapter section should have at least one Unlocked tip unless the section genuinely unlocks nothing downstream.
5. **Sources and Targets (topic-level)** — Targets: "what sorts of properties or desiderata do we usually try to prove in this subject?" Sources: "what sorts of assumptions are usually given or leveraged?" Written as **flowing prose paragraphs**, not as inline numbered lists. The 5-targets / 5-sources / routing pattern emerged across multiple gold-standard pages (`Group Theory I` lines 121–128, `Rings II` lines 107–113, `Special Relativity I` lines 121–127) — name 5 recurring targets, 5 recurring sources, and the **routes** between them.
6. **Legal Operations** — fully self-contained (a person with zero background should understand), derived post-hoc from exercises. 7+ legal operations, 3+ "illegal but tempting" with counterexamples. Each legal operation is a numbered named item followed by prose; inline `*Trigger:*` and `*Pattern:*` italic markers are **permitted** (they aid spaced-retrieval scanning) — `Topology II`, `Complex Analysis II`, `Special Relativity I` use them. Each "illegal but tempting" item should name **(a)** the concrete counterexample and **(b)** the additional condition that would make the operation legal — `Rings II` lines 145–158 sets the bar.
7. **Problem-Solving Strategy** — written as self-contained paragraphs (not tables), explaining when to use which techniques and why, such that a reader with no background could substantially improve their ability to solve exercises. Close with a meta-strategy paragraph naming the single unifying question of the chapter — `Rings II` closes "every question in this chapter is the question 'how much of $\mathbb{Z}$ survives here?'".
8. **Most Reusable Properties** — bullet-point format but each bullet is a comprehensive paragraph with wikilinks and "Typical use" descriptions (either embedded in prose or labelled `**Typical use:**`).
9. **Bridges** — self-contained prose paragraphs. **Each bridge must explain the construction**, not name it. A bridge of the form "X is the Y of Z; W is the V" without unpacking is too compressed (this was the failure mode in `Advanced Probability I` line 136). Rigorous patterns: `Rings II` line 198 ("this ideal is principal, generated by a single polynomial $m$ — and that generator is the minimal polynomial of $A$"). When the bridge references a downstream textbook section, naming it explicitly is welcome.
10. **Insights** — a dedicated section for conceptual insights that do not fit neatly into the other categories: **unifying frames** for the topic, **true names**, **trigger-reaction patterns**, **inheritance observations**, cross-cutting observations, surprising connections, heuristics, and any other high-density insight worth recording. Written as prose paragraphs. **Either format permitted**: bold-punchline-as-first-sentence (Algebra style) or labelled category prefix (`**The unifying frame**`, `**The true name**`, `**A trigger-reaction pattern**`, etc. — Topology/Complex Analysis style). The labelled style makes cross-vault patterns greppable.
11. **Imported Results** — present **only** when the chapter uses a result without proof under the single exception of the Proof Standard. One entry per imported result: its name, the page and callout where it is used, the published source of a complete proof, and one sentence on why it is imported rather than proved. A chapter that proves everything it mentions — the normal case — has no such section.

### Definition Subpage

A page for a single definition (or a small cluster of tightly related definitions). Contains the material needed to reconstruct the definition from scratch. Every section is written in paragraph form — maximize insight density without sacrificing volume. No abbreviation of phrases or words.

**Compound definitions:** When a definition page covers multiple related concepts (e.g., "Ring Homomorphism, Isomorphism, Characteristic"), every concept in the title must receive a proper, complete definition — not just a passing mention. A concept listed in the title but given only a one-sentence mention elsewhere is a quality failure. The page must announce its compound nature with a single explanatory sentence between Notation and Axiom Motivation: "This is a compound page: it defines [N] interlocking notions — [list] — because they are introduced together and none is fully usable without the others."

Contains:
1. **Notation** — restated for self-containedness. When the topic depends on a convention (units, sign, default assumption such as "all rings commutative with $1$", "all manifolds Hausdorff second countable", "$c = 1$ throughout this topic", "all measures are σ-finite"), open the Notation section with a **standing-convention preamble paragraph** stating the convention before the symbol list — and include a `> [!warning] Convention:` callout when the convention diverges between standard sources.
2. **Axiom Motivation** — the minimal information needed to invent this definition. Required content:
   - Desiderata and what the definition should capture and exclude.
   - **Per-axiom failure analysis.** For any definition with $n \geq 2$ independent axioms, address each axiom in turn: what breaks if you drop it (concrete counterexample), what would be excluded if you strengthened it. A single "what if weakened" sentence at the end does not suffice — every axiom must be stressed.
   - Sometimes the best motivation is a forward-reference to a theorem that relies on this definition: show what part of that theorem would fail with a different definition.
   The test of a successful Axiom Motivation is "Could a reader who has never seen this definition invent it from the motivation alone?" Aim for 4+ paragraphs of flowing prose for any non-trivial definition; the algebra/analysis vault gold-standards (`Def - Group.md`, `Def - Normal Subgroup.md`, `Def - The Total Derivative.md`, `Def - Topological Space.md`) are the calibration bar.
3. **The Definition** — formal statement. State the primary form, then note any equivalent formulations.
4. **Categorical Definition** — **required when a natural categorical or structural formulation exists**, optional otherwise. (Heading may be relabelled "Categorical / Structural Definition" when the content is more structural than strictly category-theoretic.) Must be self-contained: explain the relevant categorical concepts. Definitions that should typically have one: group, ring, module, ring homomorphism, ideal, topological space, continuous map, σ-algebra, measurable function, holomorphic function, manifold, Lie group, sheaf, category-theoretic-feel definitions generally.
5. **Relate to Other Fields / Compression** — precise cross-field connections. When the definition has a **"true name"** (the characterisation maximally operational for problem-solving, distinct from the official definition), state it explicitly as a short labelled paragraph here: "**True name:** [the operational form]". The "true name" sentence is one of the highest-leverage retrieval aids in the vault.
6. **Examples / Corollaries** — concrete examples and non-examples, and immediate corollaries that serve as calibration checks: if the reader can verify each one, they have understood the definition correctly. Include both "is an instance" and "is NOT an instance" examples — at least one "is NOT" for any non-trivial definition. Each example should probe a different aspect of the definition. **Every example is verified on the page** — the clauses of the definition are checked one by one for the instance, and the failing clause is exhibited for the non-instance, in the manner of the thesis's Example 2.2.1 (every line justified) — and every corollary is proved on the page or wikilinked to the page that proves it; an asserted example is a Proof Standard violation. End the section with an explicit **`**Calibration check.**`** paragraph naming 2–3 small verifications the reader should be able to perform if they have understood the definition.
7. **Unlocked by This** — downstream concepts from more advanced fields. **No length cap.** A 1–3 sentence preview is enough for routine downstream concepts; for paradigm-shifting downstream concepts (e.g., the equivalence principle in GR unlocking from Minkowski space; the holomorphic functional calculus unlocking from Cauchy's integral formula), write extended-form multi-paragraph callouts that essentially deliver mini-essays on the downstream theory. Forward references to pages that do not yet exist must be **bold plain text**, not wikilinks (Obsidian creates empty stub pages when wikilinks to missing files are clicked).

### Theorem Subpage

A page for a single theorem. Contains the material needed to understand, apply, and rederive the theorem.

Contains:
1. **Notation** — restated for self-containedness. Apply the standing-convention preamble pattern from Definition subpage §1 when relevant.
2. **Statement** — **required.** The precise, formal statement of the theorem, written as a blockquote starting `> **Theorem (name).**` (or `> **Lemma.**`, `> **Corollary.**`). Hypotheses and conclusion in one block. **Companion/specialised forms**: when a theorem has a general statement and a specialised form (e.g. "bijective form holds for any group, counting form needs finiteness"), use two blockquotes back-to-back plus a one-paragraph remark tying them together — `Thm - Orbit-Stabiliser Theorem.md` and `Thm - The Inverse Function Theorem.md` demonstrate the pattern. The Statement section comes immediately after Notation and before Motivation — a reader returning after months should find the formal statement at the top of the page, not buried as a display equation inside Motivation.
3. **Motivation** — what question this answers, what gap existed before. Should *not* re-state the formal statement (the Statement section above is for that); it explains the *role* and *importance* of the theorem.
4. **Sources and Targets (theorem-level)** — fundamentally different from a simple "assumptions and conclusions" list. See detailed description below. **Aim for at least 3 disguised sources (B → A bridges with example problems) and 3 target combinations (C + D → E), each as a multi-sentence prose paragraph.** A one-paragraph Sources block that names the precondition without giving B → A bridges is a quality failure (`Thm - First Isomorphism Theorem.md`, `Thm - Orbit-Stabiliser Theorem.md`, `Thm - The Inverse Function Theorem.md` set the bar).
5. **Why Is It True** — intuition independent of the formal proof, NOT a proof sketch. No length constraint. **Include at least one bolded one-liner mechanism summary** capturing the entire intuition in a single sentence — e.g., `Thm - Dominated Convergence Theorem.md` "the dominator $g$ does two jobs — it makes $2g \pm (f_n - f) \geq 0$ so Fatou is legal, and it is integrable so $\int 2g$ can be cancelled."
6. **What Makes This Hard** — 2–3 sentences identifying where most people get stuck, what the non-obvious step is, and what the common errors are. Directly useful for spaced practice: when returning after months, this tells the reader where to focus.
7. **Rederivation Scaffold** — high-level strategy (2–3 sentences) plus subgoal decomposition with minimal hints. Self-sufficient: reading only this section should let the reader reconstruct the full proof. Open with an explicit reader contract: "**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**"
8. **Lemma Decomposition** — each lemma independently practiceable in approximately 5 minutes, in collapsible callouts. **Every lemma callout must contain four fields:** `**Statement:**`, `**Hint:**`, `**Why needed:**`, and a nested `> [!note]- Full proof` callout. Omitting Hint or Why-needed is a quality failure (the Algebra / Multivariate / Topology lemma decompositions set the bar; Measure Theory / Advanced Probability theorems used to omit these — the new requirement closes that gap).
9. **Formal Proof** — the complete proof in a collapsible section, at or above the thesis floor (The Proof Standard above; `references/prose-and-proof-standard.md` §6 lists the eleven features every proof has, and §8 shows a model). It opens by naming what is assumed and what must be shown; it is organised by labelled blocks with bold lead-ins; every displayed line carries its justification; every hypothesis is invoked by name where it is used; both directions, all cases, all parts are written out; it closes in words. When the theorem has well-posedness preconditions (e.g. "the quotient exists", "the integral converges"), open the proof with **"Step 0 — [precondition]"** verifying it, separately from the substantive proof — see `Thm - First Isomorphism Theorem.md` for the pattern. It may cite the page's own lemmas by number and other results only by wikilink to a page whose Formal Proof is complete, restating the cited statement at the point of use. A sketch, a citation in place of an argument, or an empty section is not a Formal Proof; a page with one is not finished.
10. **Cross-Field Exercise Suggestions** — intentionally loose: find the most out-of-distribution, least obvious contexts where the theorem applies, to battle-test the Sources. Does not have to be from a different field. Use web search to find surprising applications. Aim for 3+ genuinely different fields/contexts.
11. **Bridges** — links to related theorems and concepts. **Each bridge must be a self-contained prose paragraph that explains the construction**, not a chain of wikilinks. A bridge of the form "X is the Y of Z; W is the V; Q runs on R" is too compressed — every clause must be unpacked enough that a reader unfamiliar with the identification gets actual help.
12. **Unlocked by This** — downstream concepts (optional). Same no-length-cap rule as for definition subpages.

**Detailed description of Sources and Targets for theorems:**

This is NOT a simple list of "Input: X, Output: Y." The theorem has a precondition A.

**Sources (input broadening):** Find a wide variety of properties B such that B implies A, so that the reader can recognize the theorem applies to objects with property B — even when B looks nothing like A at first glance. Aim for B where the implication B → A is nonobvious, and where B is a commonly encountered assumption in problems. These should be derived downstream from exercises: after seeing the theorem used in many problems, what were the actual starting points that led to invoking it? For each B: state B precisely, explain why B → A holds (the bridge argument), and give an example problem where starting from B you would invoke this theorem.

**Targets (output amplification):** The theorem gives conclusion C. Find corollaries of C, but also find properties D and E such that C combined with D implies E, where the combination is nonobvious. The target section is about how the theorem can be used and combined with other results to derive further properties. Also derived downstream from exercises. For each combination: state the additional property D, state what you get (E), and explain why this combination is useful.

### Exercise Subpage

A page for an exercise or problem. Self-containedness is paramount: a reader should be able to open any exercise subpage cold and fully understand the problem, strategy, and solution without clicking away.

Contains six sections (Sources and Targets is NOT included — it was removed):
1. **Problem Statement** — with full Recall section restating all needed definitions (using transclusion `![[Def - Name#The Definition]]` where appropriate), with wikilinks to definition/theorem subpages. Transclusion is the default: pure restatement-with-wikilink is acceptable only when transclusion would be too bulky for the problem statement.
2. **Convergent Strategy** — written as four labelled paragraphs, each substantive prose (multiple sentences): **Problem class:** [type of problem, referencing the topic page's problem-solving strategy], **Assumption pattern:** [what makes this instance recognizable — which assumptions are present and what they unlock], **Theorem routing:** [which theorem(s) convert the assumptions to the target, stated as an explicit route with wikilinks], **Key decision point:** [the non-obvious choice that makes this problem interesting]. One-phrase content under each label is a quality failure.
3. **Legal Operations Used** — numbered list referring back to the topic page's Legal Operations by number ("operation 4 from the topic page"). Each entry is a prose paragraph explaining *how* that operation is applied in this exercise.
4. **Hints** — progressive collapsible hints from gentle nudge to near-giveaway. **No upper or lower cap on the number of hints**; use as many as the problem requires for a graduated descent (typically 2–5). Each hint must be in a `> [!note]-` callout and strictly more revealing than the previous.
5. **Solution** — **three-tier mandatory structure**: (a) a **plan paragraph** between `# Solution` and Step 1 summarizing the entire route (~3 sentences); (b) top-level step summaries (one bolded statement per step); (c) a `> [!note]- Derivation` callout under each step with the full computation; (d) a final `> [!note]- Complete formal solution` callout at the bottom giving a clean self-contained proof at the thesis floor (every line justified, every case, closing in words). Collapsing the derivation layer into a single block (no per-step structure) is a quality failure. Every invoked theorem or definition restated at point of use with wikilinks, and every invoked theorem's wikilink points to a page whose Formal Proof is complete — a solution that leans on an unproved result inherits the violation.
6. **Key Takeaways** — elaborate prose paragraphs (multiple sentences each, **not terse bullets and not section headings with sub-bullets**). Each takeaway is a self-contained insight paragraph focused on the reusable principle, the trigger condition for recognizing the technique elsewhere, and the transferable diagnostic. Aim for 3+ takeaways, each 6+ lines of prose.

**Optional add-ons (used in upper-tier exercises across multiple subjects):**

- **"Illegal but tempting alternative route" callout.** A `> [!warning]` callout at the end of Solution explaining why an obvious alternative approach fails. Concrete pattern: `Ex - Cauchy's theorem via a cyclic action.md` lines 157–158 explains "Why the auxiliary group must be $\mathbb{Z}/p$, not $G$ and not $S_p$".
- **Sanity-check via independent route.** A short verification step at the end of Solution computing the answer by a second method as a confidence check.
- **Frame-invariance / viewpoints-must-agree check.** In physics exercises, an explicit verification that two distinct reference frames or coordinate choices give the same physical answer.
- **Cross-link to companion exercises.** Final paragraph of Key Takeaways naming related exercises elsewhere in the vault.

**Difficulty calibration:** Each exercise has a difficulty tag in its YAML frontmatter: ⭐ (routine application of one theorem), ⭐⭐ (requires combining theorems or a non-obvious step), ⭐⭐⭐ (competition-level or requires genuine creativity). This helps with session planning when studying across many subjects.

### Exercise Index Page

One page per sub-chapter section listing all exercises for that section. **Required:** at least 3 exercises per sub-chapter section — if a section has fewer, web-search to add exercises. Each exercise wikilink is followed by **(a)** the inline difficulty tag `(⭐)`/`(⭐⭐)`/`(⭐⭐⭐)`, **(b)** a substantive one-line technique description naming the reusable principle drilled, and **(c)** a parenthesised list of wikilinks to every definition and theorem used in that exercise's solution (parentheses, not square brackets — a `[` against a `[[` opener breaks the link). The page should **open with a one-paragraph contextualizing preamble** framing the section's purpose before the bullet list, as `Group Theory I/Exercise Index - §1.1 Basic Concepts.md` and `Group Theory III/Exercise Index - §1.7 Sylow's Theorems.md` demonstrate. Integrated into the topic page's concept map as a callout at the end of each section.

---

## Component-Only Mode

When the user requests a single component (not a full topic page), produce just that section. Components that can be requested individually:

- Notation registry, axiom motivation, sources and targets (topic-level or theorem-level), why is it true, legal operations, problem-solving strategy, most reusable properties, rederivation scaffold, cross-field exercise suggestions, convergent strategy, solution, bridges, categorical definition, relate to other fields, insights

In component-only mode, output the content in chat. If the user asks to add it to an existing page, write it to the appropriate file.

---

## Study Orchestrator Mode

When the user asks "what should I study next," "pick a subject," "plan my study," "what's high leverage right now," or otherwise delegates the choice of topic rather than naming one, enter Study Orchestrator mode. The job is to route the polymathic programme — pick the next subject to study based on prerequisite readiness, downstream leverage, and interest — not to produce content for a named topic.

The single source of truth for this decision is the prerequisite DAG, mirrored into the vault at `Study notes/Prerequisite DAG.md`. Read that file first, every time. Do not answer from memory of prior sessions: nodes get updated, prereqs get satisfied, interest scores drift.

### Prerequisite DAG reference

**What it is.** The master study-planning document for the polymathic vault. Each node is a subject; each node's fields encode its prerequisites, its connections to other subjects, whether it has been studied, what it unlocks downstream, and one or two reference textbooks or papers. The Notion original lives at https://www.notion.so/35bf76ffda148143abcad0be3ca296f4; the working copy Claude Code reads and edits is `Study notes/Prerequisite DAG.md`. The vault copy is authoritative for orchestration; the Notion page is the human-facing mirror.

**Legend.**

- 🟢 — **Anchor.** Foundation already solid / known well; can be assumed as background when studying downstream nodes.
- 🔵 — **Study target.** Not yet studied, or in progress. This is what orchestration is picking among.
- ⭐ — **High-leverage hub.** Gates many downstream nodes. Prioritising these compounds — one hub studied unlocks a wide swath of downstream subjects. The top three hubs are Topology, Differential Geometry, and Category Theory.

**Node format.** Every node is a collapsed-by-default Obsidian callout whose title line has the form `> [!note]- 🔵 Subject Name (familiarity, interest)` (the emoji reflects status, familiarity and interest are each roughly 1–10; some nodes omit the score pair). The `-` after `[!note]` is what makes the callout collapsed by default — do not drop it. The callout body holds the fields: every body line is prefixed `> `, each field is a bold-labelled paragraph, and fields are separated by a line containing just `>` (the callout-internal blank line). Consecutive node callouts are separated by a true blank line — without it Obsidian merges adjacent callouts into one. Preserve this layout when editing: keep the `> ` prefix on every body line (an unprefixed line after a callout gets absorbed into it as a lazy continuation), and never use HTML `<details>` blocks — they do not collapse reliably in Reading view and Obsidian does not parse markdown inside them (see `references/obsidian-patterns.md`). Fields (any subset may appear on a given node):

- **Prereqs:** — the incoming edges of the DAG for this node, referring to other node names.
- **Connects:** — nontrivial two-way relationships to other nodes (analogy, cross-pollination) that are not strict prereqs.
- **Note:** — the substantive one-paragraph description: what the subject is, why it matters, why it is placed where it is placed.
- **Unlocks:** — the outgoing edges: downstream subjects, applications, or research programmes this node opens up.
- **Reference(s):** / **Key refs:** — one or two textbooks or papers used as the primary source when the subject is studied.
- **Description:** — occasional longer prose block when the subject needs more framing than **Note:** allows.
- **Gaps:** — for 🔵 nodes, what specifically is missing / not yet studied.
- **Status:** — for 🟢 nodes, a one-line summary of how the subject is currently used.

Not every field appears on every node — a node freshly added to the DAG might have only **Prereqs:** and **Note:**; a mature anchor might have **Status:** and nothing else.

**Sections.** Nodes are grouped under `##` headers by area: Foundations, Geometry, Analysis, Stochastics, Algebra, Probability, Category Theory, Foundations and Logic, Physics, Computation, Engineering, Statistics, Mechanism Design / Game Theory, Niche Connecting Fields, Cutting-Edge Subfields. Section membership is loose — a node about categorical probability might live under Category Theory or under Probability depending on where its primary payload sits.

**Synergy clusters.** After the by-area sections, the document lists numbered `## Cluster N: Title` blocks. Each cluster has a `**Members:**` line naming the nodes in it, followed by a `> 💡` blockquote stating the unifying theme — the single idea that makes the members feel like one subject rather than several. Clusters are the polymathic payoff: they say "if you study these together, you will see a picture that studying them separately would obscure." Guiding strategy — **diversity through specialization**: prioritize hub fields (⭐) that force genuine breadth rather than chasing many shallow subjects. A cluster whose members are mostly 🔵 is a target for a coordinated study campaign.

**Maintenance.** Edit `Study notes/Prerequisite DAG.md` directly when a node changes state (🔵 → 🟢 once studied, familiarity / interest scores updated), when a new node is added, or when a new prereq / connection is discovered. When a node belongs to a synergy cluster, update that cluster's **Members:** line in the same edit — otherwise the cluster drifts out of sync with the by-area listing. The top hubs (Topology, Differential Geometry, Category Theory) gate the most downstream subjects, so prereq-graph edits near them cascade widely; check downstream nodes when a hub's status changes.

### Picking the next subject

The Study Orchestrator's job on each invocation:

1. **Read `Study notes/Prerequisite DAG.md` in full.** Do not skip. Every scoring decision is grounded in the current file.
2. **Filter to eligible study targets.** A node is eligible if it is 🔵 (not yet studied) and every entry on its **Prereqs:** line is either 🟢 in the DAG or already treated as background from the owner's stated background in `CLAUDE.md`. Nodes with unmet prereqs are not eligible — surface them separately as "unlocks after you finish X."
3. **Rank by `interest × leverage`.** Interest is the second number in the score pair on the node's callout title line. Leverage is roughly (a) whether the node is marked ⭐, (b) how many downstream nodes name it on their **Prereqs:** line, and (c) how many synergy clusters list it in **Members:**. A ⭐ node that gates a large downstream cone and appears in two or three clusters beats a niche node of comparable interest.
4. **Prefer synergy over isolation.** When two candidates are close on interest × leverage, pick the one whose cluster has more 🔵 members ready to be studied next — that is the "diversity through specialization" heuristic in action.
5. **Recommend one primary subject plus one or two adjacent bridging subjects.** Explain the pick in terms of what it unlocks (name specific downstream nodes) and what synergy clusters it activates. Cite the node's **Reference(s):** as the source material to start from.
6. **Treat `Study notes/Prerequisite DAG.md` as source of truth going forward.** Once a subject is picked and the user agrees, subsequent content-generation work (Steps 1–8 of the standard workflow) should still cross-reference the DAG — the picked node's **Note:** and **Unlocks:** fields feed directly into the topic page's Motivation and "Unlocked by This" callouts.

If the user's request names a subject directly, skip orchestration and go to the normal workflow — but still glance at the DAG entry for that subject so the topic page's Motivation, Bridges, and "Unlocked by This" sections stay consistent with the DAG's framing.

---

## Quality Standards — Self-Evaluation Checklist

Before finalizing, evaluate against this checklist. For each item, verify compliance and fix issues before presenting the result.

**Completeness:**

1. **Source coverage.** Every definition, theorem, proof, and exercise in the uploaded source material appears in the notes. If anything was omitted, add it.
2. **Exercise coverage.** Each sub-chapter section has at least 3 exercises. If any section has fewer, search the web for additional exercises.
3. **Per-section exercise index exists.** Each sub-chapter section has a dedicated exercise index page integrated into the concept map as a callout.
4. **Cross-linking and link audit.** Every reference to a defined concept throughout all pages uses a wikilink to the relevant subpage. The vault-wide link audit from Step 6 returns zero unresolved wikilinks and zero broken transclusions — every `[[...]]` resolves to an existing file, with forward references to not-yet-written subjects written as bold plain text instead.
5. **Frontmatter present.** Every page has YAML frontmatter with type, subject, and prereqs fields.
6. **Notation coverage.** Every pivotal variable that appears in a Statement, The Definition, or display math `$$...$$` on a Def/Thm subpage must be introduced *somewhere prior*: either in the Notation section, or earlier in the same Statement via an explicit introduction ("Let $X$ be …", "for an operator $T \in \mathcal{L}(V)$", "with $A = …$"). Pivotal means capital Latin letters and Greek morphism names ($\varphi$, $\pi$, $\sigma$, $\tau$, etc.) used as named objects, not loop indices. The Ideal Correspondence theorem failure case was: Notation defined $R, I, \pi$ but the Statement introduced $J \mapsto J/I$ and $L \mapsto \pi^{-1}(L)$ with $J$ and $L$ *appearing cold* — neither in Notation nor introduced inline. Run `.claude/skills/polymath-notes/scripts/find-notation-gaps.py` as a sanity check; the script reports candidate gaps but is conservative (high recall, moderate precision — many flagged "gaps" are conventional symbols or inline introductions that are fine). Treat its output as a triage list, not a definitive bug list.

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
25. **Theorem Statement section present and formal.** Every theorem subpage has a `# Statement` section, placed immediately after `# Notation` and before `# Motivation`, containing the precise formal statement of the theorem in a `> **Theorem.**` blockquote. The Statement section must not be empty, must not be a paraphrase or motivation, and must not be the same header under another name (`# Formal Statement`, `# The Statement`, etc.). Mechanical check: `grep -L "^# Statement$" Thm-*.md` should return no files.

**Cross-subject enforcement (mechanical checks that match cross-vault quality dimensions):**

26. **Concept map has `Unlocked:` callouts.** Every topic page concept-map section unlocks at least one downstream concept via a `> [!tip] Unlocked:` callout, unless the section genuinely unlocks nothing. Mechanical check: `grep -c "> \[!tip\] Unlocked:" $TOPICPAGE` should be at least the number of `## §` sub-chapter sections on the page (allowing zero only when the section is purely consolidation).
27. **Exercises appear in the concept map with difficulty tags.** Every exercise that appears in the topic's Exercise Index also appears in the concept map under its sub-chapter section, with an inline `(⭐)`/`(⭐⭐)`/`(⭐⭐⭐)` tag. Mechanical check: `grep -E "^- \*\*\[\[Ex - " $TOPICPAGE | grep -v "(⭐"` should return no lines (every exercise bullet has a difficulty tag).
28. **Bridges are not wikilink chains.** Every bridge bullet in the topic page's Bridges section contains at least one full sentence of explanatory prose per wikilink — not a chain of "X is Y; W is V; Q is R" without unpacking. Spot-check: any Bridge entry whose wikilink count exceeds its sentence count is flagged for rewriting.
29. **Categorical Definition present where natural.** For definition pages on group, ring, module, ring homomorphism, ideal, topological space, continuous map, σ-algebra, measurable function, holomorphic function, manifold, Lie group: a `# Categorical Definition` or `# Categorical / Structural Definition` section must be present. Mechanical check: `grep -L "^# Categorical" "Def - Group.md" "Def - Ring.md" ...` should return no files in that fixed list.
30. **"Calibration check" present at end of Examples.** Every non-trivial definition page ends its Examples / Corollaries section with a paragraph or bullet labelled `**Calibration check**`. Mechanical check: `grep -L "Calibration check" Def-*.md` should approximate zero.
31. **Lemma callouts have Hint and Why-needed.** Every `> [!note]- Lemma N:` callout in a theorem subpage contains both `**Hint:**` and `**Why needed:**` fields. Mechanical check: for each theorem file, count `> \[!note\]- Lemma` matches vs `Hint:` and `Why needed:` matches in the same regions — they should agree.
32. **Exercise Solution three-tier structure.** Every exercise's `# Solution` section has (a) a non-callout plan paragraph between `# Solution` and the first step header, (b) per-step bolded summary lines, (c) `> [!note]- Derivation` callouts under each step, (d) a `> [!note]- Complete formal solution` callout at the bottom. Mechanical check: `grep -c "> \[!note\]- Derivation" "Ex - X.md"` should be ≥ 1 and `grep -c "> \[!note\]- Complete formal solution"` should equal 1.
33. **Exercise Convergent Strategy has all four labels with prose.** Every exercise's Convergent Strategy section contains `**Problem class:**`, `**Assumption pattern:**`, `**Theorem routing:**`, `**Key decision point:**`, each followed by a multi-sentence paragraph (not a one-phrase tag).
34. **Exercise indices are populated.** Every exercise index page has at least 3 enumerated exercises and opens with a contextualizing paragraph before the exercise list. Mechanical check: each `Exercise Index - *.md` file has ≥ 3 `[[Ex -` wikilinks and at least one paragraph of non-bullet prose before the first bullet.
35. **Inline difficulty tags in exercise indices.** Every exercise wikilink in an Exercise Index has an inline `(⭐)`/`(⭐⭐)`/`(⭐⭐⭐)` immediately after it. Mechanical check: `grep -E "^- \[\[Ex - " Exercise-Index-*.md | grep -v "(⭐"` should return no lines.
36. **No content-subtraction caps.** The skill imposes no upper caps on the number of hints, the length of Unlocked callouts, the length of Bridges, the number of legal operations, or the number of Unlocked tips per section. Caps in earlier drafts of the skill (e.g., "2–4 hints") are explicitly removed — graduated descent should use as many hints as the problem requires.
37. **Statement-section header normalization.** Theorem subpages use exactly the header `# Statement` (not `# Formal Statement`, `# Theorem Statement`, `# The Statement`). Mechanical check: `grep -l "^# Formal Statement\|^# Theorem Statement\|^# The Statement" Thm-*.md` should return no files.

**Prose register and Proof Standard (the thesis baseline):**

38. **Thesis register.** Spot-read three explanatory sections (a topic-page Motivation, a Def Axiom Motivation, a Thm Why Is It True) against the calibration passages in `references/prose-and-proof-standard.md` §1: each orients, motivates, states formally, unpacks in the smallest concrete case, re-explains, and closes in words, in the thesis's measured first-person-plural academic voice. Any section in whiteboard-chat, slogan, or labelled-fragment register is rewritten.
39. **Every theorem mentioned is proved.** Every `Thm -`/`Lemma -`/`Prop -`/`Cor -` page in the unit has a `# Formal Proof` that is complete at the thesis floor (the eleven points of `references/prose-and-proof-standard.md` §6), and every theorem invoked anywhere in the unit — in a proof, a solution, a definition's examples, a bridge — wikilinks a page whose Formal Proof is complete and restates the statement at the point of use. Mechanical check: `python3 .claude/skills/polymath-notes/scripts/find-unproved-theorems.py "<unit>"` returns zero findings.
40. **No statement-only pages, no sketches.** No page created in the unit is named `… (Statement)`, no link added in the unit points at one, and no Formal Proof or lemma Full proof contains "sketch", "omitted", "beyond the scope", "we do not prove", or "left to the reader". The P1 grep (`clearly / obviously / it is easy to see / similarly / analogous / left to the reader / omitted / sketch`) has been reviewed line by line and every hit expanded.
41. **Imports are registered, and rare.** Every use of a result without proof is in the `> [!warning] Imported without proof: …` callout form with exact statement, published source by section or page, proof architecture, and reason; the topic page lists each under `# Imported Results`; and each is genuinely book-length (Freedman, Donaldson's diagonalisation package, Uhlenbeck compactness, Atiyah–Singer, and little else). Anything shorter has been proved instead.
42. **Thesis-floor audit of two proofs.** The two longest proofs in the unit have been checked point by point against §6 of the standard: named assumptions and goal, labelled blocks, bold lead-ins, a justification on every displayed line, hypotheses invoked by name, clause-by-clause well-definedness, all directions and cases, explicit combination of numbered lines, closing sentence, typed symbols.

**Cross-subject parity check (the highest-leverage enforcement, run before declaring any subject batch complete):**

Pick three subject areas that are "established" in the vault (Group Theory, Multivariate Analysis, Special Relativity are the current gold-standard exemplars). For the subject you have just authored, sample one topic page, two definition subpages, two theorem subpages, and two exercise subpages, and compare against the gold-standard exemplars along every dimension above. **Any dimension where your new subject is materially behind a gold-standard exemplar should trigger a rewrite of the relevant section — the bar is "as good as the best existing subject," not "passes the spec minimum."** This is the mechanism that catches the cross-subject drift documented in the vault audit.

**Report:** After checking, briefly report which items passed and any that required fixes. If all items pass, state "Self-evaluation passed: all 42 checklist items verified plus cross-subject parity check."
