# Paper-Note Page Templates

The page-level skeletons produced by the `paper-notes` skill. Six shapes: map page, section page, `Def -`, `Thm -`, `Constr -`, and the local prerequisite DAG.

Low-level Obsidian syntax is **not** repeated here. Wikilinks, transclusion, collapsible callouts, foldable bullets, frontmatter schema, Windows-portable filenames, and the math-delimiter rules all live in `../../polymath-notes/references/obsidian-patterns.md`, which is the source of truth. Read it first. Two reminders only, because they are the ones most easily lost when transcribing from a PDF:

- Math is `$...$` inline and `$$...$$` display. Nothing else.
- Never put `$...$` inside `[[ ]]`. Wikilink display text uses Unicode: `[[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]]`, `[[Def - Sigma-Finite Measure|σ-finite]]`.

---

## The type-card block

The one construct this skill adds. It appears on the map page (compressed), on the section page (full), and on each `Thm -` / `Constr -` subpage (full). Always a **non-folding** `[!abstract]` callout — no `-` on the marker — so it survives a skim and cannot be collapsed away.

```markdown
> [!abstract] Type card — Theorem 3.5 (mass of the subordinate Brownian loop measure)
> **Given.** A [[Def - Bernstein Function and the Lévy–Khintchine Representation|Bernstein function]] $\phi$ satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]]; a [[Def - Primitive Hyperbolic Element and Translation Length|primitive closed geodesic]] $\gamma \in \mathcal{P}_X$ of length $\ell_\gamma$; a winding number $m \geq 1$.
>
> **Produces.** A closed-form value for $\mu_X^\phi(\mathcal{C}_X(\gamma^m))$ — a single non-negative real number — as one integral of an explicit heat-kernel factor against the [[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]] $V_\phi$.
>
> **Lets you.** Replace the double $(t,s)$ integral by a single integral against $V_\phi$, which is what makes every later special case — Brownian, killing, α-stable, shifted α-stable — a one-line substitution of $V_\phi$.
```

Three fields, always in this order, always all three.

- **Given** — every hypothesis, each a wikilink to its `Def -` or `Constr -` page. A bare undefined term here is a bug.
- **Produces** — the object *with its type*. Not "a formula" but "a non-negative real number", "a σ-finite measure on $(0,\infty)$", "an identity between two meromorphic functions on $\mathrm{Re}(s) > \delta$".
- **Lets you** — one sentence of operational payoff. What you may now do that you could not do before.

The strategy line is a separate visible paragraph, sitting between the type card and the folded proof:

```markdown
**Strategy.** Evaluate the spatial integral by the Wang–Xue identity (Lemma 3.4), then collapse the $\mathrm{d}t/t$ integral into $V_\phi$ by Lemma 2.11.

> [!note]- Proof (skippable)
> [the full proof]
```

---

## Map page

Filename: `Map - <Paper Short Title>.md`.

````markdown
---
type: paper-map
paper: "<CiteKey>"
subject: <subject-slug>
title: "<Full Paper Title> — <Authors>"
tags: [paper, <area-tag>, <subject-tag>]
---

# What this paper does

[One paragraph. Not an abstract — an account of the move the paper makes. What object it builds, what it computes about that object, and what the payoff is. Written so that reading only this paragraph leaves the reader able to say what the paper is for.]

[A second paragraph naming the paper's one central identity or construction, as a display equation, and saying in words what it says. This is the thing every other result is in service of.]

**Source.** `paper_source/<filename>.pdf` — <full citation>.

---

# Notation registry

[Every symbol used anywhere in this note-set, with its type. Always visible, never folded. Opens with a standing-convention preamble when the paper fixes conventions the reader might otherwise mis-apply — sign of the Laplacian, speed of the process, orientation, normalisation of a measure.]

- $X = \Gamma \backslash \mathbb{H}^2$ — the quotient surface; $\Gamma$ a torsion-free Fuchsian group
- $p_X(t,x,y)$ — heat kernel, $p : (0,\infty) \times X \times X \to (0,\infty)$, a density with respect to $\mathrm{vol}_g$
- [...]

---

# Type index

[Every theorem, lemma, proposition, corollary and construction in the paper, in paper order, with a compressed type card and a link. This is the skimmable spine: reading only this section, top to bottom, must give a correct mental model of the paper's argument.]

## §2 <Section title> → [[§2.1–2.2 <Section Title>|section page]]

- **[[Constr - The Brownian Loop Measure|Definition 2.1 — Brownian loop measure]]** — *Given* a complete orientable Riemannian surface $(X,g)$. *Produces* a σ-finite measure on the space of unrooted unparametrised loops. *Lets you* speak of "the measure of a set of loops" without a probability normalisation.
- **[[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]]** — *Given* [...]. *Produces* [...]. *Lets you* [...].

## §3 <Section title> → [[§3 <Section Title>|section page]]

[...]

---

# Local prerequisite DAG

[Two or three sentences summarising what the paper reduces to, then a link.]

The full backchain, with every leaf either an anchor or a page in this folder, is on [[Prereq DAG - <Paper Short Title>]].

---

# Suggested reading order

[Prose, not a bare list. Name a first pass that reads only type cards, a second pass that reads the section pages, and the points where dropping into a proof actually pays. Say explicitly which sections can be skipped on a first reading and what is lost by skipping them.]

---

# What this paper leaves open

[The paper's own stated open questions, plus anything the note-set noticed: a hypothesis that looks stronger than needed, a special case that collapses, a construction that plainly extends. Keep honest about which is which.]
````

---

## Section page

Filename: `§N.M <Section Title>.md` — the paper's own section numbering, so the note-set stays aligned with the PDF.

````markdown
---
type: paper-section
paper: "<CiteKey>"
subject: <subject-slug>
section: "<N.M>"
prereqs:
  - "Def - <X>"
  - "Constr - <Y>"
tags: [paper, <area-tag>]
---

# Notation

[Every symbol used on this page and its subpages, with its type. Unfolded, first. Restated even where it duplicates the map page — this page must be readable cold.]

---

# What this section is for

[David-Tong-register prose. What problem the section solves, what the previous section left dangling, and what the next section will need from this one. Two to four paragraphs. Concrete before abstract: open with the difficulty, arrive at the construction.]

---

# Results

[Each result: a heading, the type card, the statement (transcluded from the subpage where the statement is short, restated where transclusion would be bulky), the strategy line, and a link to the subpage carrying the full proof. Interleave the narrative prose between results — the section page is a guided read, not a list.]

## Lemma 2.11 — collapsing the time integral

> [!abstract] Type card — Lemma 2.11
> **Given.** [...]
>
> **Produces.** [...]
>
> **Lets you.** [...]

![[Thm - Collapsing the Time Integral into the Weighted Potential Measure#Statement]]

**Strategy.** [One or two moves.]

Full proof and the input-broadening discussion: [[Thm - Collapsing the Time Integral into the Weighted Potential Measure]].

[Prose paragraph on what this buys, leading into the next result.]

## Theorem 3.5 — [...]

[...]

---

# Worked special cases

[Where the paper specialises a general formula — Brownian, killing, α-stable — give each case its visible one-line answer and fold the computation.]

**Brownian ($\phi(\lambda) = \lambda$).** $V_\phi(\mathrm{d}s) = \mathrm{d}s/s$, and the mass is $\frac{1}{m}\cdot\frac{1}{e^{L}-1}$.

> [!note]- Calculation (skippable)
> [the substitution and the integral identity]

---

# What to carry forward

[One paragraph naming exactly what later sections use from this one. This is the section's export list — if a later section needs something not named here, either this list or that section is wrong.]
````

---

## Definition subpage

Filename: `Def - <Concept Name>.md`.

````markdown
---
type: definition
paper: "<CiteKey>"
subject: <subject-slug>
prereqs:
  - "Def - <dependency>"
tags: [paper, <area-tag>]
---

# Notation

[Symbols this page uses, typed. Unfolded, first.]

---

# In plain language

[One or two sentences. What this thing *is*, said to someone who will never read the formal version. This section is mandatory and comes before the formal definition — it is the single highest-value paragraph on the page for a cold re-entry.]

[Then a paragraph of David-Tong-register motivation: what goes wrong without this concept, what the definition is engineered to make true. Where the definition has independent clauses, say what each clause is buying.]

---

# The definition

> **Definition (<name>).** [The formal statement. Precise, complete, in the paper's own convention, with the convention named.]

[Equivalent formulations, when the paper or the literature uses more than one, with a sentence on which is operationally more useful and why.]

---

# Types and signatures

[Every object the definition introduces, with its type. One bullet each.]

- $\phi : (0,\infty) \to [0,\infty)$ — the Bernstein function; smooth, non-negative, with alternating-sign derivatives from the first onward.
- $\nu$ — the Lévy measure, a measure on $(0,\infty)$ with $\int_0^\infty (1 \wedge s)\,\nu(\mathrm{d}s) < \infty$; not finite in general.

---

# Example

[One minimal example, worked concretely enough to be checkable. Not a list of examples — one, done properly.]

**Near-miss non-example.** [An object failing exactly one clause, with that clause named and the consequence of the failure spelled out. Include when the definition has a clause whose necessity is not obvious; omit when it would be padding.]

---

# Used in this paper at

- [[Thm - <name>]] — [how it is used there, in a clause]
- [[Constr - <name>]] — [...]

---

# Where this sits in my DAG

[One or two sentences: which DAG node this concept's home subject is, whether it is an anchor, and — for non-anchors — what it reduces to. Links onward to whatever it depends on. This is the local rung of the backchain.]
````

---

## Theorem subpage

Filename: `Thm - <Theorem Name>.md`. Used for theorems, lemmas, propositions and corollaries alike; the blockquote label distinguishes them.

````markdown
---
type: theorem
paper: "<CiteKey>"
subject: <subject-slug>
prereqs:
  - "Def - <X>"
  - "Constr - <Y>"
tags: [paper, <area-tag>]
---

# Notation

[Typed symbol list. Unfolded, first.]

---

# Type card

> [!abstract] Type card — Theorem N.M (<short name>)
> **Given.** [Every hypothesis, each a wikilink.]
>
> **Produces.** [The object, with its type.]
>
> **Lets you.** [One sentence of operational payoff.]

---

# Statement

> **Theorem N.M (<name>).** [The precise formal statement, hypotheses and conclusion in one block, in the paper's numbering.]

[Companion or specialised forms as further blockquotes, with a sentence tying them together.]

---

# Why it is true

[The intuition, independent of the proof. Not a proof sketch — the reason one should expect the result. Include a single bolded one-line mechanism summary. Written in David-Tong register.]

---

# Strategy

**Strategy.** [The one or two moves the proof turns on, named. This line plus the type card must be enough to take the result on faith and use it correctly downstream.]

> [!note]- Proof (skippable)
> [The complete proof, in the paper's steps, with each step's purpose named before its computation. Long sub-computations get their own nested `> > [!note]- Calculation (skippable)` fold.]

---

# What this assumes, and where to climb

[Prose walking the hypotheses one at a time: for each, which `Constr -` or `Def -` page carries it, and — briefly — what would break without it. This is the upward half of rule D, and it is what makes the theorem page a valid entry point into the paper.]

---

# What consumes this

- [[Thm - <downstream result>]] — [in a clause, how this feeds it]
- [[§N <Section Title>]] — [...]

---

# Reading it against the rest of the paper

[Optional. Where the result sits relative to the literature the paper cites, or relative to a result elsewhere in the note-set that has the same shape. Only when there is something real to say.]
````

---

## Construction / assumption subpage

Filename: `Constr - <Object Name>.md`. One per object that later appears as a hypothesis.

````markdown
---
type: construction
paper: "<CiteKey>"
subject: <subject-slug>
prereqs:
  - "Def - <X>"
tags: [paper, <area-tag>]
---

# Notation

[Typed symbol list. Unfolded, first.]

---

# In plain language

[What this object is and why the paper builds it. One or two sentences, then a motivating paragraph.]

---

# The construction

> **Construction / Definition N.M (<name>).** [The formal construction. Every ingredient named and typed; every choice made explicit, with a note on which choices the result is independent of.]

[When the object is this paper's instance of a general notion, transclude the general definition here rather than restating it:]

![[Def - <general notion>#The definition]]

---

# Type card

> [!abstract] Type card — <object>
> **Given.** [What must be in hand to perform the construction.]
>
> **Produces.** [The object, with its type — what space it lives in, what it is a function of, what it is normalised against.]
>
> **Lets you.** [What downstream results become available once you have it.]

---

# Properties relied on later

[Each property the paper actually uses, as a named item with a sentence of justification or a link to where it is proved. Only the ones that get used — this is not a survey.]

**Restriction.** [...]

**Conformal invariance.** [...]

---

# Consumed by

[The downward half of rule D. Every theorem and section that assumes this object.]

- [[Thm - <name>]] — assumed as [which hypothesis]
- [[Thm - <name>]] — [...]

---

# Where this sits in my DAG

[Which anchors it reduces to; what non-anchor concepts it stands on, each linked.]
````

---

## Local prerequisite DAG page

Filename: `Prereq DAG - <Paper Short Title>.md`.

The point of this page is a single glance that answers "does this bottom out at things I actually know?" So: an indented dependency list, anchors marked 🟢 at the leaves, every non-anchor a link. Not a graph diagram, not prose.

````markdown
---
type: prereq-dag
paper: "<CiteKey>"
subject: <subject-slug>
tags: [paper, prereq-dag]
---

# How to read this page

[Two or three sentences. Indentation is dependency: a child is something its parent needs. 🟢 marks an anchor — a concept from a 🟢 node of `Study notes/Prerequisite DAG.md`, where the backchain stops. Every non-anchor is a link to a page in this folder. An unlinked, unmarked leaf is a bug, and finding one is the point of reading this page.]

---

# Anchors this paper stands on

[The full anchor list up front, so the reader can sanity-check the floor before reading the tree. One line each, naming the DAG node it comes from.]

- 🟢 **Heat kernel and heat semigroup** — from *Analysis of PDEs*, *Spectral Theory*
- 🟢 **Brownian motion, Brownian bridge, disintegration by endpoint** — from *SDEs*, *Advanced Probability*
- [...]

---

# The backchain

## <Top-level result 1>

- [[Thm - <name>]]
	- [[Constr - <hypothesis object>]]
		- [[Def - <term>]]
			- 🟢 anchor concept
			- 🟢 anchor concept
		- 🟢 anchor concept
	- [[Def - <term>]]
		- 🟢 anchor concept

## <Top-level result 2>

[...]

---

# Leaves that are not anchors

[Ideally empty. If a leaf genuinely cannot be reduced to an anchor — the paper cites a black-box result from a subject the reader has not studied — say so here explicitly, name the result, and say what would have to be studied to close the gap. An honest gap recorded here is far better than a silent one buried in the tree.]
````
