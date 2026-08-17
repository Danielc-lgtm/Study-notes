# Paper-Note Page Templates

Page skeletons for the `paper-notes` skill. Seven shapes: map, section, `Def -`, `Thm -`, `Constr -`, `Ext -`, prereq DAG.

Low-level Obsidian syntax is **not** repeated here — see `../../polymath-notes/references/obsidian-patterns.md`, which is the source of truth. Two reminders, because they are the ones most easily lost when transcribing from a PDF:

- Math is `$...$` inline and `$$...$$` display. Nothing else.
- Never put `$...$` inside `[[ ]]`. Wikilink display text uses Unicode: `[[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]]`, `[[Def - Sigma-Finite Measure|σ-finite]]`.

**Page order is fixed and identical across page types.** Signature → Type card → Statement/Definition/Construction → Discharges/Depends on → Proof (folded) → Checks → Consumed by → Commentary (folded). Formal content above; prose folded at the foot.

---

## The three recurring blocks

### 1. Signature block — always first

A two-column table. **Every symbol used on the page appears.** The right column gives a *type*, never a name.

```markdown
# Signature

| symbol | type |
|---|---|
| $(X,g)$ | complete orientable Riemannian surface; $\partial X$ possibly non-empty |
| $\Delta_X$ | $-\operatorname{div}_g\operatorname{grad}_g$; self-adjoint on $L^2(X,\mathrm{vol}_g)$; $\operatorname{spec}\subseteq[0,\infty)$ |
| $p_X$ | $(0,\infty)\times X\times X\to(0,\infty)$; symmetric; density w.r.t. $\mathrm{vol}_g$; kernel of $e^{-t\Delta_X}$ |
| $W^t_{x\to y}$ | measure on $C([0,t],X)$; **unnormalised**: $\lvert W^t_{x\to y}\rvert = p_X(t,x,y)$ |
| $\mu_X$ | $\sigma$-finite measure on $\mathcal{C}_X$; $\mu_X(\mathcal{C}_X)=\infty$ |
| $V_\phi$ | $\sigma$-finite measure on $(0,\infty)$; **not** finite |
| $m$ | $\in\mathbb{Z}_{\geq1}$ |

**Conventions.** $\Delta_X\geq0$ (opposite sign to the analyst's). Brownian motion at speed $2$: generator $-\Delta_X$, not $-\tfrac12\Delta_X$. Dirichlet conditions on $\partial X$. Throughout, $\kappa$ and $s$ are linked by
$$s=\tfrac12+\sqrt{\tfrac14+\kappa}\iff\kappa=s(s-1).$$
```

Flag symbol collisions here rather than letting the reader discover them: *"$L$ is real ($=m\ell_\gamma$) in §3–§6 and complex ($=mL_\gamma$) in §7"*; *"$s$ is the subordination variable in §2–§3 and the spectral parameter in §4–§6"*.

### 2. Type card — always second, never folds

```markdown
# Type card

> [!abstract] Type card — Theorem 3.5 (mass of the subordinate loop measure)
> **Given.**
> **(H1)** $\phi$ a [[Def - Bernstein Function and the Lévy–Khintchine Representation|Bernstein function]] satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|(A2.3)]]: $b>0$ or $\nu(0,\infty)=\infty$.
> **(H2)** $\gamma\in\mathcal{P}_X$ with translation length $\ell_\gamma>0$.
> **(H3)** $m\in\mathbb{Z}_{\geq1}$; set $L:=m\ell_\gamma$.
>
> **Produces.** $\mu^\phi_X(\mathcal{C}_X(\gamma^m))\in[0,\infty]$, in closed form
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(\mathrm{d}s).$$
>
> **Lets you.** Replace the double $(t,s)$ integral by one integral against $V_\phi$; every special case is then a one-line substitution of a measure on $(0,\infty)$.
```

- **Given** — numbered **(H1)…(Hn)**, each a typed proposition, symbolic or a wikilink. Never a sentence listing them.
- **Produces** — the object *with its type*, and the formula when there is one. "A non-negative real number", "a $\sigma$-finite measure on $(0,\infty)$", "an identity of meromorphic functions on $\operatorname{Re}(s)>\delta$" — not "a formula".
- **Lets you** — one sentence.

### 3. Strategy line and folded proof

```markdown
**Strategy.** Evaluate the spatial integral by [[Ext - Wang–Xue Strip Identity|(WX)]], then collapse $\int_0^\infty\mathrm{d}t/t$ into $V_\phi$ by [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]].

> [!note]- Proof (skippable)
> **Step 1.** By (H1) and [[Ext - Phillips Subordination|(PH)]], $p^\phi_{\mathbb{H}^2}(t,z,w)=\int_{[0,\infty)}p_{\mathbb{H}^2}(s,z,w)\,\psi^\phi_t(\mathrm{d}s)$. Substituting into (14),
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}\int_{[0,\infty)}p_{\mathbb{H}^2}(s,z,\tau^mz)\,\psi^\phi_t(\mathrm{d}s)\,\mathrm{d}\rho(z).$$
> **Step 2.** Integrand $\geq0$, so [[Thm - Fubini-Tonelli Theorem|Tonelli]] exchanges the $z$- and $s$-integrals. By (H2), (H3) and (WX) the inner integral is $\frac{\ell_\gamma}{2\sinh(L/2)}h(s)$ with $h(s)=\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt{\pi s}}$.
> **Step 3.** Apply Lemma 2.11 to $h$. $\;\square$
```

Every step cites a labelled hypothesis, a linked page, or an explicit computation.

---

## Definition subpage

Filename `Def - <Concept>.md`.

````markdown
---
type: definition
paper: "<CiteKey>"
subject: <subject-slug>
prereqs: ["Def - <dep>"]
tags: [paper, <area-tag>]
---

# Signature

| symbol | type |
|---|---|
| ... | ... |

---

# Definition

> **Definition (<name>).** [Formal statement. When there are $n\geq2$ independent conditions, number them:]
> **(D1)** $\dots$
> **(D2)** $\dots$
> **(D3)** $\dots$

**Gloss.** [At most ONE sentence, and only when the formal statement is genuinely opaque without it. Anything longer is Commentary.]

[Equivalent formulations as a second blockquote, with a clause-level note on which is operationally cheaper to check.]

---

# Type card

> [!abstract] Type card — <name>
> **Given.** **(H1)** … **(H2)** … *(the data the definition consumes)*
>
> **Produces.** *(the object, with its type)*
>
> **Lets you.** *(one sentence)*

---

# Depends on

- [[Def - <X>]] — used for (D1) only
- 🟢 *anchor concept* — used for (D2)

---

# Checks

**Instance.** $\dots$ — (D1) holds because $\dots$; (D2) because $\dots$

**Non-instance.** $\dots$ — satisfies (D1), (D3); **fails (D2)**, because $\dots$. Consequence: $\dots$

[A non-instance is required whenever a clause's necessity is not obvious. It must name the clause it fails.]

---

# Used at

- [[Thm - <name>]] — as (H2)
- [[Constr - <name>]] — in the construction of $\dots$

---

# Commentary

> [!note]- Commentary (skippable)
> [Motivation, intuition, history, "why this definition and not a nearby variant", cross-references. Tong register permitted here and nowhere else.]
````

---

## Theorem subpage

Filename `Thm - <Name>.md`. Used for theorems, lemmas, propositions and corollaries the paper states as its own; the blockquote label distinguishes them.

````markdown
---
type: theorem
paper: "<CiteKey>"
subject: <subject-slug>
prereqs: ["Def - <X>", "Constr - <Y>", "Ext - <Z>"]
tags: [paper, <area-tag>]
---

# Signature

| symbol | type |
|---|---|
| ... | ... |

---

# Type card

> [!abstract] Type card — Theorem N.M (<short name>)
> **Given.** **(H1)** … **(H2)** … **(H3)** …
>
> **Produces.** …
>
> **Lets you.** …

---

# Statement

> **Theorem N.M (<name>).** Assume (H1)–(H3). Then
> $$\dots\tag{N}$$

[Specialisations as further blockquotes, each stating which hypotheses it strengthens.]

---

# Discharges

[The imported results this proof consumes, one line each: name, what it is applied to, what it returns. This is the section that makes the proof checkable without opening it.]

| result | applied to | returns |
|---|---|---|
| [[Ext - Wang–Xue Strip Identity\|(WX)]] | $\int_{F_\tau}p_{\mathbb{H}^2}(s,z,\tau^mz)\,\mathrm{d}\rho$ | $\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt{\pi s}}$ |
| [[Thm - Fubini-Tonelli Theorem\|Tonelli]] | non-negative integrand on $(0,\infty)\times F_\tau\times[0,\infty)$ | exchange of $\int\mathrm{d}\rho$ and $\int\psi^\phi_t$ |

---

# Proof

**Strategy.** [One or two moves, named.]

> [!note]- Proof (skippable)
> **Step 1.** …
> **Step 2.** …

---

# Consumed by

- [[Thm - <downstream>]] — as (H1)
- [[§N <Section Title>]]

---

# Commentary

> [!note]- Commentary (skippable)
> [Why one should expect it; the one-line mechanism; where it sits relative to the literature; what breaks without each hypothesis.]
````

---

## Construction subpage

Filename `Constr - <Object>.md`. One per object that later appears as a hypothesis.

````markdown
---
type: construction
paper: "<CiteKey>"
subject: <subject-slug>
prereqs: ["Def - <X>"]
tags: [paper, <area-tag>]
---

# Signature

| symbol | type |
|---|---|
| ... | ... |

---

# Construction

> **Construction / Definition N.M (<name>).** [Every ingredient typed; every choice explicit, with a note on which choices the output is independent of, and why.]
> $$\dots\tag{N}$$

[When this is the paper's instance of a general notion, transclude the general definition:]

![[Def - <general notion>#Definition]]

**Well-definedness.** [The one check that the construction does not depend on the choices made — stated, and either discharged in a line or linked.]

---

# Type card

> [!abstract] Type card — <object>
> **Given.** **(H1)** … **(H2)** …
>
> **Produces.** *(the object with its type: which space, what it is a function of, what it is normalised against, whether finite)*
>
> **Lets you.** …

---

# Depends on

- [[Def - <X>]] — for …

---

# Properties

[Only the properties actually consumed later. Each as a labelled symbolic statement, with its consumer named.]

**(P1) Restriction.** $X'\subseteq X$ open $\implies\ \mathrm{d}\mu_{X'}(\eta)=\mathbf{1}_{\eta\subseteq X'}\,\mathrm{d}\mu_X(\eta)$. *Consumed by:* [[Ext - <name>]].

**(P2) Conformal invariance.** $\mu_{X,e^{2\sigma}g}=\mu_{X,g}$ for every $\sigma\in C^\infty(X,\mathbb{R})$. *Consumed by:* … *Fails for:* …

---

# Consumed by

- [[Thm - <name>]] — as (H1)
- [[Thm - <name>]] — as (H2)

---

# Commentary

> [!note]- Commentary (skippable)
> […]
````

---

## External-result subpage

Filename `Ext - <Name>.md`. One per result the paper invokes but does not prove. **The point of the page is that a reader who accepts it on blind faith can still follow every proof that uses it** — so precondition and conclusion must be exact.

````markdown
---
type: external
paper: "<CiteKey>"
subject: <subject-slug>
tags: [paper, external, <area-tag>]
---

# Signature

| symbol | type |
|---|---|
| ... | ... |

---

# Statement

> **(WX) Wang–Xue strip identity.** *Precondition:*
> **(P1)** $s>0$;
> **(P2)** $m\in\mathbb{Z}_{\geq1}$, $\ell_\gamma>0$, $L:=m\ell_\gamma$;
> **(P3)** $\tau\in\mathrm{PSL}(2,\mathbb{R})$ in standard form $\tau:z\mapsto e^{\ell_\gamma}z$, $F_\tau=\{1\leq\operatorname{Im}z<e^{\ell_\gamma}\}$;
> **(P4)** $p_{\mathbb{H}^2}$ the speed-$2$ Brownian heat kernel on $\mathbb{H}^2$.
>
> *Conclusion:*
> $$\int_{F_\tau}p_{\mathbb{H}^2}\big(s,z,e^Lz\big)\,\mathrm{d}\rho_{\mathbb{H}^2}(z)=\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}.$$

---

# Type card

> [!abstract] Type card — (WX)
> **Given.** (P1)–(P4).
>
> **Produces.** A positive real number, factorising as *(geometric prefactor)* $\times$ *(analytic factor in $(s,L)$)*.
>
> **Lets you.** Discharge the spatial integral of [[Thm - …|Theorem 3.2]] completely, leaving a one-dimensional integral in $t$.

---

# Status

- **Proved here:** no.
- **Source:** [WX25, Lemma 3.2].
- **DAG node that would close this:** *<node name>* (🔵/🟢).
- **What is safe to assume:** the conclusion, verbatim, under (P1)–(P4). Nothing about the proof is used downstream.

---

# Used at

- [[Thm - <name>]] — with $a=\tfrac14$, $b=L^2/4$
- [[Thm - <name>]] — with $a=\tfrac14+\kappa$, $b=L^2/4$

---

# Commentary

> [!note]- Commentary (skippable)
> [Why the statement has the shape it has; what the analogous statement in another dimension or setting is; how hard the gap is to close.]
````

---

## Section page

Filename `§N.M <Section Title>.md` — the paper's own numbering, so the note-set stays aligned with the PDF.

````markdown
---
type: paper-section
paper: "<CiteKey>"
subject: <subject-slug>
section: "<N.M>"
prereqs: [...]
tags: [paper, <area-tag>]
---

# Signature

| symbol | type |
|---|---|
| ... | ... |

**Conventions.** […]

---

# Results

[One `##` per result. Each: type card, statement (transcluded where short), strategy line, link to the subpage. **No connecting narrative here** — the narrative is in the section's Commentary block at the foot.]

## Lemma 2.11 — collapsing the time integral

> [!abstract] Type card — Lemma 2.11
> **Given.** **(H1)** … **(H2)** …
>
> **Produces.** …
>
> **Lets you.** …

![[Thm - Collapsing the Time Integral into the Weighted Potential Measure#Statement]]

**Strategy.** […] · Full page: [[Thm - Collapsing the Time Integral into the Weighted Potential Measure]].

## Theorem 3.5 — …

[…]

---

# Special cases

[Where the paper specialises a general formula, a table of substitutions with the visible answer, and the computation folded.]

| $\phi(\lambda)$ | $V_\phi(\mathrm{d}s)$ | $I_\phi(L)$ | $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ |
|---|---|---|---|
| $\lambda$ | $\mathrm{d}s/s$ | $e^{-L/2}/L$ | $\frac1m\cdot\frac{1}{e^L-1}$ |

> [!note]- Calculation (skippable)
> […]

---

# Exports

[Exactly what later sections consume from this one, as a numbered list of typed statements. If a later section needs something not listed, either this list or that section is wrong.]

**(E1)** $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{e^{(1-s)L}}{e^L-1}$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, $L=m\ell_\gamma$. → §4, §5, §6.
**(E2)** … → §7.

---

# Commentary

> [!note]- Commentary (skippable)
> [What the section is for, the difficulty it resolves, the narrative connecting the results. Tong register permitted.]
````

---

## Map page

Filename `Map - <Paper Short Title>.md`.

````markdown
---
type: paper-map
paper: "<CiteKey>"
subject: <subject-slug>
title: "<Full Paper Title> — <Authors>"
tags: [paper, <area-tag>]
---

# Signature

[The global symbol table: every symbol used anywhere in the note-set, typed. This is the page a returning reader opens first, and it must be sufficient to read any type card in the index below.]

| symbol | type |
|---|---|
| ... | ... |

**Conventions.** […] **Collisions.** […]

---

# The one identity

$$\dots$$

[Two sentences: what it says, and what every other result does to it. No more.]

**Source.** `paper_source/<file>.pdf` — <full citation>.

---

# Type index

[Every result in paper order, with a compressed type card and a link. Reading only this section must give a correct account of the logical spine. Group by section with a link to the section page.]

## §2 <title> → [[§2.1–2.2 <Section Title>|section]]

- **[[Constr - …|Definition 2.1]]** — *Given* (H1) $(X,g)$ complete orientable Riemannian surface; (H2) $p_X$, $W^t_{x\to x}$. *Produces* a $\sigma$-finite measure on $\mathcal{C}_X$ of infinite total mass. *Lets you* assign mass to a family of loops with no normalisation, and inherit (P1) restriction, (P2) conformal invariance.

---

# Imported results

[Every `Ext -` page in one table — the complete list of what must be taken on faith, with what each is used for. This is the honest inventory of the note-set's floor.]

| result | precondition (abbrev.) | used at | closes with |
|---|---|---|---|
| [[Ext - …]] | … | §3, §7 | *<DAG node>* |

---

# Prerequisite DAG

[Two sentences, then the link to [[Prereq DAG - <Paper Short Title>]].]

---

# Reading order

[Three passes, terse: what each pass reads, and what is skippable with what cost. A list, not prose.]

---

# Open

[The paper's stated open questions and anything the note-set noticed, each stated as a precise question rather than a gesture.]
````

---

## Local prerequisite DAG page

Filename `Prereq DAG - <Paper Short Title>.md`. An indented dependency list; anchors marked 🟢 at the leaves; every non-anchor a link. Not a diagram, not prose.

````markdown
---
type: prereq-dag
paper: "<CiteKey>"
subject: <subject-slug>
tags: [paper, prereq-dag]
---

# How to read

Indentation is dependency. 🟢 marks an anchor — a concept from a 🟢 node of `Study notes/Prerequisite DAG.md`, where the backchain stops. Every non-anchor is a link. **An unlinked, unmarked leaf is a bug**, and finding one is the point of this page.

---

# Anchors

[The floor, up front, so it can be sanity-checked before reading the tree. One line each, naming the DAG node and the specific facts used.]

- 🟢 **Heat semigroup and kernel** — *Analysis of PDEs*, *Functional Analysis*. Used: $e^{-t\Delta}$ strongly continuous contraction; kernel as density; $p(t,x,x)\sim1/4\pi t$ on a surface; $\operatorname{Tr}e^{-t\Delta}=\int p(t,x,x)$.

---

# Backchain

## <Top-level result>

- [[Thm - <name>]]
	- [[Constr - <hypothesis object>]]
		- [[Def - <term>]]
			- 🟢 …
		- [[Ext - <import>]] ← **gap**
	- 🟢 …

---

# Gaps

[Leaves that are not anchors. Each: the `Ext -` page carrying it, what it is used for, and what would close it. An honest gap recorded here is far better than a silent one buried in the tree. Ideally the list matches the `Ext -` inventory on the map page exactly.]
````
