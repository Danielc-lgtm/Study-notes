---
type: topic
subject: higher-categories
chapter: "Leinster 1.2, 1.4, 3, App B"
title: "Higher Categories — Strict n-Categories and Notions of Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation Registry

This chapter works in two registers that meet in the **periodic table**: the *globular* world of strict $n$-categories (cells in every dimension, composed strictly) and the *monoidal* world (one object, tensored coherently). The standing convention is that "strict" means all structural isomorphisms are identities, "weak" means they are coherent isomorphisms, and "lax/oplax" means they are coherent but not necessarily invertible morphisms with a chosen direction. We deliberately keep the **biased** binary tensor $\otimes$ separate from the **unbiased** all-arity family $\otimes_n$; they describe the same objects (Theorem [[Thm - Biased and Unbiased Monoidal Categories Coincide]]) but the unbiased presentation makes coherence transparent.

- $X_n$ — the set of **$n$-cells** of a globular set; $s, t : X_n \to X_{n-1}$ — source and target
- $\mathbb{G}$ — the **globe category**, objects $[0], [1], [2], \dots$; a [[Def - Globular Set|globular set]] is a presheaf $\mathbb{G}^{op}\to\mathbf{Set}$
- $\sigma_n, \tau_n : [n-1] \to [n]$ — the cosource and cotarget generators of $\mathbb{G}$
- $s_p, t_p$ — iterated $p$-source and $p$-target of an $n$-cell ($p < n$)
- $\circ_p$ — composition of $n$-cells along a shared $p$-dimensional boundary; $1_a$ — degenerate (identity) cell
- $G_n$ — the **standard $n$-globe**, the free globular set on a single $n$-cell, $G_n = \mathbb{G}(-, [n])$
- $n\text{-}\mathbf{Cat}$, $\omega\text{-}\mathbf{Cat}$ — strict $n$-categories / strict $\omega$-categories and their strict functors
- $\otimes : \mathcal{C}\times\mathcal{C}\to\mathcal{C}$, $I$ — the **biased** binary tensor and unit; $\alpha, \lambda, \rho$ — associator and unitors
- $\otimes_n : \mathcal{C}^n \to \mathcal{C}$ — the **unbiased** $n$-ary tensor; $\otimes_0() = I$, $\otimes_1 = \mathrm{id}$; $\gamma, \iota$ — composition and unit isomorphisms
- $\beta_{A,B} : A\otimes B \to B\otimes A$ — braiding; a **symmetry** if $\beta_{B,A}\beta_{A,B} = 1$
- $\varphi, \varphi_0$ — the tensor and unit comparisons of a [[Def - Weak and Lax Monoidal Functor|monoidal functor]]
- $\mathbf{1}$ — the terminal category (one object, one arrow), the unit for $\times$ on $\mathbf{Cat}$
- $\mathbf{y}$ — the [[Thm - The Yoneda Lemma|Yoneda embedding]]
- "$k$-tuply monoidal $n$-category" — an $(n+k)$-category with one cell in each dimension below $k$ (the periodic-table coordinate)

---

# Motivation

Here is the entire chapter in one sentence: there are two roads up the dimension ladder of category theory — *adding more [[Def - Dimension|dimensions]] of arrows* (globular, strict $n$-categories) and *adding more ways of multiplying objects* (monoidal categories) — and they are the same road, because **going up a dimension and looking at a single object is the same as gaining a multiplication.** This is the **periodic table** of Baez and Dolan, and assembling it is the goal toward which everything here is aimed.

An ordinary [[Def - Category|category]] composes arrows in one dimension. A [[Def - 2-Category and Bicategory|2-category]] composes $2$-cells too; an $n$-category composes cells up to dimension $n$. To even *state* this we need the bare cellular data — a [[Def - Globular Set|globular set]], a tower of sets $X_0 \leftleftarrows X_1 \leftleftarrows X_2 \cdots$ with each cell having a single source and a single target one dimension down — and then composition imposed *strictly* in every dimension, giving a strict $n$-category. Strictness is the clean, computable starting point, and it is genuinely correct for the leading example $\mathbf{Cat}$. But it is ultimately too rigid: strictification works in low dimensions and *fails* from dimension three, and understanding why is half the point of higher category theory.

The other road begins from the observation, already on [[Def - Monoidal Category]], that **a monoidal category is a one-object [[Def - 2-Category and Bicategory|bicategory]]** — going up one dimension and restricting to a single object turns horizontal composition into a tensor product. So a [[Def - Monoidal Category|monoidal category]] is "a category with a multiplication," obtained by climbing one rung and forgetting all but one object. Repeating the move — climb a rung, take one object and one $1$-cell — adds a *braiding* (the [[Higher Categories — Strict n-Categories and Notions of Monoidal Category#§3 Coherence and the Periodic Table|Eckmann–Hilton]] argument forces a swap to appear); climbing once more *stabilizes* the braiding to a symmetry. This is the periodic table, the structural backbone of the chapter:

$$\boxed{k\text{-tuply monoidal } n\text{-category} \;=\; (n+k)\text{-category with only one cell in each dimension} < k.}$$

| $n=0$ | $n=1$ | $n=2$ |
|---|---|---|
| set | category | $2$-category |
| monoid | monoidal category | monoidal $2$-category |
| commutative monoid | braided monoidal category | braided monoidal $2$-category |
| " | symmetric monoidal category | sylleptic monoidal $2$-category |
| " | " | symmetric monoidal $2$-category |

The coherence machinery is the price of admission to either road. Once associativity holds only up to isomorphism, you must prove those [[Def - Isomorphism|isomorphisms]] cohere — and the cleanest way to do that is the **unbiased** reformulation, where the $n$-ary tensor $\otimes_n$ is primitive for every $n$ and coherence becomes nearly a tautology ([[Thm - Coherence for Unbiased Monoidal Categories]]). The unbiased and biased pictures agree ([[Thm - Biased and Unbiased Monoidal Categories Coincide]]), and both are equivalent to *strict* monoidal categories ([[Thm - Strictification of Monoidal Categories]]) — the low-dimensional miracle whose failure upstairs is the whole reason weak higher categories exist.

This chapter assumes you are comfortable with [[Def - Category|categories]], [[Def - Functor|functors]], [[Def - Natural Transformation|natural transformations]], [[Def - Presheaf|presheaves]], and the [[Thm - The Yoneda Lemma|Yoneda lemma]], and that you have met [[Def - Monoidal Category|monoidal categories]] and [[Def - 2-Category and Bicategory|2-categories/bicategories]] (Category Theory V and the first Higher Categories chapter). It does *not* assume any prior higher-categorical experience; everything globular is built from scratch. Refresh [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]] and [[Def - Enriched Category|enriched categories]] before §1 and §2 respectively.

---

# Concept Map

## §1 Globular Sets and Strict n-Categories

- **[[Def - Globular Set]]**
	- A globular set is the bare cellular skeleton of a higher category: a set $X_n$ of $n$-cells for each $n \geq 0$, with source and target maps $s, t : X_n \to X_{n-1}$ satisfying the **globularity equations** $ss = st$ and $ts = tt$, which say that the source and target of any cell are *parallel* one dimension down (a $2$-cell is a bigon between parallel arrows). Equivalently it is a [[Def - Presheaf|presheaf]] on the globe category $\mathbb{G}$, so $\mathbf{GSet}$ is a topos with all limits and colimits. The representable presheaves are the standard globes $G_n$, the free globular set on a single $n$-cell, related to globular sets exactly as the simplices $\Delta^n$ relate to [[Def - Simplicial Set|simplicial sets]].

- **[[Def - Strict n-Category and Strict ω-Category]]**
	- A strict $\omega$-category is a globular set with associative, unital composition $\circ_p$ of $n$-cells along a shared $p$-boundary, for every $p < n$, satisfying the **interchange law** between distinct composition dimensions (the law that makes a pasting diagram have a single well-defined composite). A strict $n$-category truncates this to dimension $n$: a strict $0$-category is a set, a strict $1$-category is a [[Def - Category|category]], a strict $2$-category is a [[Def - 2-Category and Bicategory|2-category]] with $\circ_0$ horizontal and $\circ_1$ vertical. Equivalently, by iterated enrichment, a strict $(n{+}1)$-category is a category enriched in strict $n$-categories — the inductive definition that bypasses globular sets. The free strict $\omega$-category monad on $\mathbf{GSet}$ is **cartesian**, the foundation of globular [[Def - Operad|operads]].

> [!tip] Unlocked: [[Def - The Free Strict ω-Category Monad|The Free Strict ω-Category Monad]] and [[Def - Globular Operad|Globular Operads]] *(from Higher Category Theory)*
> The free-strict-ω-category functor on [[Def - Globular Set|globular sets]] gives a monad $T$ whose operations are **globular pasting diagrams**, and $T$ is **cartesian**. A **globular operad** is a cartesian map $P \to T$, and algebras for the initial contractible one are **Batanin–Leinster weak ω-categories** — see [[Higher Categories — Globular Operads and Weak n-Categories]].

> [!tip] Unlocked: [[Thm - The Homotopy Hypothesis|The Homotopy Hypothesis]] *(from Algebraic Topology)*
> A weak ω-**groupoid** (all cells weakly invertible) should model a topological space up to [[Def - Homotopy|homotopy]] — **Grothendieck's homotopy hypothesis**. The *strict* version is provably too weak (strict ω-groupoids capture only products of Eilenberg–MacLane spaces), which is the cleanest evidence that strictness must be relaxed.

> [!note] Exercise Index — §1
> [[Exercise Index - §1 Globular Sets and Strict n-Categories]]

## §2 Unbiased Monoidal Categories

- **[[Def - Unbiased Monoidal Category]]**
	- An unbiased monoidal category takes the $n$-ary tensor $\otimes_n : \mathcal{C}^n \to \mathcal{C}$ as primitive for *every* $n$ (with $\otimes_0() = I$ the unit and $\otimes_1 = \mathrm{id}$), rather than singling out the binary $\otimes$ and bracketing. The coherence data is a composition isomorphism $\gamma$ (comparing "tensor sublists, then tensor results" with "tensor the flat concatenation") and a unit isomorphism $\iota$, subject to just **two** axioms: associativity coherence (re-partitioning in two stages = one stage) and unit coherence. Structurally it is a **pseudo-algebra for the free-monoidal-category $2$-monad**, equivalently an algebra for the lists/As operad in $\mathbf{Cat}$ — "a categorified [[Def - Monoid in a Monoidal Category|monoid]]." The pentagon of the biased [[Def - Monoidal Category|monoidal category]] is recovered as the length-four instance of the single associativity axiom.

- **[[Def - Weak and Lax Monoidal Functor]]**
	- A lax monoidal functor $F : \mathcal{C}\to\mathcal{D}$ carries a tensor comparison $\varphi_{A,B}: FA \boxtimes FB \to F(A\otimes B)$ and unit comparison $\varphi_0 : J \to FI$ (not necessarily invertible), coherent with associativity and units; reversing the arrows gives **oplax**, requiring isomorphisms gives **weak (strong)**, requiring identities gives **strict**. The four flavours are exactly the four kinds of pseudo-algebra morphism in $2$-monad theory. The decisive example: a [[Def - Monoid in a Monoidal Category|monoid]] in $\mathcal{D}$ is a *lax* monoidal functor $\mathbf{1}\to\mathcal{D}$ (multiplication $= \varphi$, unit $= \varphi_0$), so laxness is exactly what lets functors transport algebraic structure.

- **[[Thm - Biased and Unbiased Monoidal Categories Coincide]]**
	- There is a $2$-equivalence $\mathbf{MonCat}_{\mathrm{u}} \simeq \mathbf{MonCat}_{\mathrm{b}}$: every unbiased monoidal category has an underlying biased one ($\otimes := \otimes_2$), every biased one extends to an unbiased one (left-bracketed iterated $\otimes$), and these are mutually inverse up to monoidal equivalence. The forward direction is free; the backward direction defines $\gamma$ by re-bracketing and needs exactly [[Thm - Mac Lane Coherence Theorem|Mac Lane coherence]] to be well-defined. The upshot: the biased binary tensor and pentagon are a *presentation* of the unbiased object, the pentagon being the relation that makes the binary generator generate the correct operad of arities.

> [!tip] Unlocked: Monoidal Monads and the Probability Monad *(from Categorical Probability)*
> A **monoidal monad** is a monad whose endofunctor is lax monoidal compatibly with $\eta, \mu$; its algebras inherit a monoidal structure. This is how $\otimes$ on [[Def - Module|modules]], [[Def - Convolution|convolution]] on measures, and the **probability monad** underlying Markov categories all arise — a direct instance of lax monoidal functoriality.

> [!tip] Unlocked: Eₙ-Algebras and the Little Disks Operad *(from Algebra and Topology)*
> Swap the lists/As operad for the **little $n$-disks operad** $E_n$ and an "unbiased $E_n$-monoidal category" is the categorical home of $n$-fold loop spaces. This is the input to **factorization algebras** and the operadic backbone of [[Higher Categories — Operads and Multicategories]].

> [!note] Exercise Index — §2
> [[Exercise Index - §2 Unbiased Monoidal Categories]]

## §3 Coherence and the Periodic Table

- **[[Thm - Coherence for Unbiased Monoidal Categories]]**
	- In any unbiased monoidal category every diagram of canonical maps (composites of $\gamma^{\pm}, \iota^{\pm}$) commutes; equivalently, between any two formal tensor expressions in the same objects in the same order there is *at most one* canonical map. The mechanism: a formal expression is a tree, every tree contracts to the single arity-$m$ corolla $\otimes_m$ by $\gamma$, and the associativity axiom forces the contraction to be unique — there is one operation per arity, so "many composites" collapse. Transporting this across the biased/unbiased equivalence yields [[Thm - Mac Lane Coherence Theorem|Mac Lane's biased coherence theorem]] as a corollary; this is the cleanest known proof of it.

- **[[Thm - Strictification of Monoidal Categories]]**
	- Every [[Def - Monoidal Category|monoidal category]] is monoidally equivalent to a *strict* one, so one may always assume the tensor is strictly associative and unital. The construction trades the non-strict $\otimes$ for the always-strict functor composition $\circ$: embed $\mathcal{C}$ via [[Thm - The Yoneda Lemma|Yoneda]] among "tensoring operators," whose tensor is composition; coherence is exactly what makes the embedding monoidal. This is a **low-dimensional miracle**: it holds for monoidal categories (one-object bicategories) and for [[Thm - Strictification of Bicategories|bicategories]], but **fails for tricategories** — the first obstruction is the Eckmann–Hilton braiding, the structural reason weak higher categories are unavoidable from dimension three.

- **[[Ex - The Eckmann-Hilton argument]]** (⭐⭐)
	- Show that two unital binary operations on a set that satisfy the interchange law are equal, associative, and commutative — the algebraic heart of why a one-object, one-$1$-cell bicategory ($=$ a braided monoidal category) acquires commutativity, and why $\pi_n$ is abelian for $n \geq 2$.

- **[[Ex - A monoidal category is a one-object unbiased bicategory]]** (⭐⭐)
	- Verify that restricting an (unbiased) bicategory to a single $0$-cell yields exactly an (unbiased) monoidal category, with horizontal composition becoming $\otimes_n$ — the bottom row of the periodic table made precise.

- **[[Ex - Climbing the periodic table by stabilization]]** (⭐⭐⭐)
	- Trace the periodic table: a $k$-tuply monoidal $n$-category is an $(n+k)$-category with one cell below dimension $k$; show monoidal $=$ one-object bicategory, braided $=$ one-object-one-$1$-cell tricategory (via Eckmann–Hilton), and that the rows stabilize to symmetric after enough steps (Baez–Dolan stabilization).

> [!tip] Unlocked: The Stabilization Hypothesis and Symmetric Monoidal ∞-Categories *(from Higher Category Theory)*
> Baez–Dolan's **stabilization hypothesis** says the $k$-tuply monoidal $n$-categories stabilize once $k \geq n+2$, becoming **symmetric monoidal**. In the ∞-categorical refinement this is the **Breen–Baez–Dolan** picture realized by Lurie's $E_k$-algebras and is the structural source of stable homotopy theory and **symmetric monoidal $(\infty,n)$-categories**.

> [!tip] Unlocked: The Cobordism Hypothesis *(from Topological Field Theory)*
> A fully extended **TQFT** is a symmetric monoidal functor from the $(\infty,n)$-category of cobordisms to a symmetric monoidal target; **the cobordism hypothesis** (Baez–Dolan, Lurie) says it is determined by a single fully dualizable object. The periodic table is the bookkeeping that even lets this statement be formulated.

> [!note] Exercise Index — §3
> [[Exercise Index - §3 Coherence and the Periodic Table]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The exercises and theorems of this chapter chase a small set of recurring goals. The most characteristic is a **coherence claim**: showing that two ways of composing, bracketing, or swapping agree — that "the" canonical map between two configurations is well-defined. A second is an **equivalence of presentations**: proving that two superficially different definitions (biased/unbiased, globular/enriched, strict/weak) describe the same objects up to (monoidal, bi-, or $2$-) equivalence. A third is a **strictness verdict**: deciding whether a given weak structure can be replaced by a strict equivalent, and if not, identifying the obstruction. A fourth is a **dimension-shift identification**: recognising a structure in one row of the periodic table as a degenerate (one-object) instance of a structure one dimension up. A fifth is **construction of free objects and their monads** — the free strict $\omega$-category, the free monoidal category — and proving the resulting monad is well-behaved (cartesian). These five — cohere, identify presentations, decide strictness, shift dimension, build free structures — recur because each is a way of pinning down what a higher structure *is* up to the only equality that matters in this subject, namely equivalence.

**Sources — what assumptions do we usually leverage?**

The hypotheses are equally stereotyped. **A globular/cellular presentation is given** — a tower of cells with sources and targets — and the move is to recognise it as a presheaf on $\mathbb{G}$ and inherit limits, colimits, and the free-forgetful adjunction for free. **An $n$-ary universal property is given** — a tensor or product representing multilinear/multivariable maps — and the move is to read off an *unbiased* structure directly, with canonical $\gamma$'s, sidestepping the pentagon. **Coherence is available** — every canonical diagram commutes — and the move is to suppress brackets, build maps from bracket-free expressions, and strictify. **A one-object (or one-cell) restriction is in force** — and the move is to climb the periodic table, reading horizontal composition as a tensor and invoking Eckmann–Hilton to manufacture commutativity. **A monad or operad is given on a category with pullbacks** — and the move is to ask whether it is cartesian, the gate to a clean theory of generalized operads. The recurring routing: a cellular source runs through "presheaf on a shape category" to limits/colimits and free monads; a universal-property source runs through "unbiased structure" to coherence and strictification; a one-object source runs through Eckmann–Hilton to the periodic table. The [[Higher Categories — Strict n-Categories and Notions of Monoidal Category#Problem-Solving Strategy|Problem-Solving Strategy]] makes these explicit.

---

# Legal Operations

These are the moves almost every problem in the chapter is assembled from. When stuck, scan the list and try each. Everything is self-contained.

**Legal operations:**

1. **Recognise cellular data as a presheaf on a shape category.** A tower of sets with source/target (or face) maps satisfying the globularity (or simplicial) equations *is* a [[Def - Presheaf|presheaf]] on the globe category $\mathbb{G}$ (or $\Delta$). Once you see this, you inherit all [[Def - Limit and Colimit|limits and colimits]] (computed dimensionwise), cartesian closure, the topos structure, and the free objects (representables $=$ standard globes $G_n$). *Trigger:* any "tower of sets with structure maps." *Pattern:* "this is $[\mathbb{S}^{op}, \mathbf{Set}]$ for the shape $\mathbb{S}$, so limits/colimits/free objects are free."

2. **Impose composition strictly, dimension by dimension, and check interchange.** To make a [[Def - Globular Set|globular set]] a strict $\omega$-category, give each $\circ_p$ associatively and unitally, then verify the [[Thm - The Interchange Law|interchange law]] for every pair of dimensions — that is the *only* cross-dimensional axiom, and it is exactly what makes a pasting diagram have a single composite. *Trigger:* "compose cells in more than one dimension." *Pattern:* "associativity + identities in each direction, then interchange between directions."

3. **Switch between globular and iterated-enriched definitions.** A strict $(n{+}1)$-category is a category [[Def - Enriched Category|enriched]] in strict $n$-categories. Use the enriched form to build examples inductively and to get functoriality of composition (which *is* interchange) for free; use the globular form to reason about individual cells. *Trigger:* "define an $n$-category" or "prove composition is functorial." *Pattern:* "enrich in the level below; interchange is functoriality."

4. **Pass from biased to unbiased and back.** Replace a binary tensor + pentagon by the all-arity family $\otimes_n$ + the single associativity axiom, or vice versa, using [[Thm - Biased and Unbiased Monoidal Categories Coincide]]. Coherence questions become trivial in the unbiased frame (one operation per arity); concrete examples are often cleaner biased. *Trigger:* "prove a coherence identity" or "an $n$-ary tensor is given." *Pattern:* "go unbiased to cohere, go biased to compute."

5. **Cite coherence to suppress brackets.** By [[Thm - Coherence for Unbiased Monoidal Categories|coherence]], any two canonical maps between the same two bracketings are equal, so write $A_1 \otimes \cdots \otimes A_n$ with no brackets and treat all parenthesizations as canonically equal. *Trigger:* a calculation drowning in associators. *Pattern:* "both maps are canonical with the same source and target, hence equal by coherence."

6. **Strictify.** By [[Thm - Strictification of Monoidal Categories|strictification]], replace a monoidal category by an equivalent strict one, do the calculation with strict $\otimes$, and transport back along the monoidal equivalence. Legitimate for any property invariant under monoidal equivalence. *Trigger:* "without loss of generality" appetite, or a string-diagram identity. *Pattern:* "assume strict, compute, transport."

7. **Restrict to one object (one cell) to descend the periodic table.** A one-object [[Def - 2-Category and Bicategory|bicategory]] is a [[Def - Monoidal Category|monoidal category]]; a one-object-one-$1$-cell tricategory is a braided monoidal category. To study a monoidal-type structure, view it one dimension up with a single object; to manufacture commutativity, take one more object/cell and run Eckmann–Hilton. *Trigger:* "one object" or "two compatible products." *Pattern:* "climb a dimension, take one cell, read horizontal composition as $\otimes$."

8. **Run the Eckmann–Hilton argument.** Two unital binary operations sharing a unit and satisfying interchange are equal, associative, and commutative. Use it to collapse degenerate higher structures and to *produce* braidings/symmetries from interchange. *Trigger:* "interchange law + two unital operations on the same objects." *Pattern:* "$a \cdot b = (a \star 1)\cdot(1 \star b) = (a \cdot 1)\star(1\cdot b) = a \star b$, and symmetrically — so the two products agree and commute."

9. **Build the free structure and study its monad.** Form the free strict $\omega$-category on a globular set (or the free monoidal category on a category) and ask whether the generating monad is **cartesian** (preserves pullbacks; unit and multiplication cartesian). Cartesianness is the gate to the operadic theory of weak structures. *Trigger:* "free higher category" or "what are the pasting diagrams." *Pattern:* "operations of the free monad $=$ pasting diagrams; check the monad is cartesian."

**Illegal but tempting operations:**

> [!warning] 1. Assuming every weak $n$-category is equivalent to a strict one
> [[Thm - Strictification of Monoidal Categories|Strictification]] holds for monoidal categories and [[Thm - Strictification of Bicategories|bicategories]], so it is tempting to assume it always holds. It **fails for tricategories**: the braided monoidal category $\mathbf{Braid}$ (one object, one $1$-cell of a tricategory) is *not* equivalent to anything strict, because the braiding $\beta$ with $\beta^2 \neq 1$ is genuine information no strict model can carry. The operation becomes legal exactly in dimension $\leq 2$; from dimension $3$ the obstruction is the Eckmann–Hilton braiding, and pretending it away loses the very content the structure encodes.

> [!warning] 2. Treating a simplicial set as a globular set (or conflating the two shapes)
> Both are presheaf categories of "cells," so it is tempting to move between them freely. But a [[Def - Simplicial Set|simplicial set]]'s $2$-cell is a *triangle* with three faces satisfying the simplicial identities, while a [[Def - Globular Set|globular set]]'s $2$-cell is a *bigon* with a single source and target satisfying globularity. A triangle is not a bigon: the face maps and the equations differ. They model the same higher-categorical content only after a nontrivial comparison (the nerve / homotopy-coherent machinery), never by literal identification.

> [!warning] 3. Forgetting interchange when composing in two dimensions
> Having defined vertical and horizontal composition of $2$-cells, it is tempting to call the result a $2$-category. Without the [[Thm - The Interchange Law|interchange law]], a $2\times 2$ grid of $2$-cells has two unequal values (horizontal-then-vertical $\neq$ vertical-then-horizontal), so "the composite of the diagram" is undefined and pasting is meaningless. The structure is a $2$-category only once interchange holds; it is the single axiom that makes the two-dimensional calculus consistent, and it is exactly functoriality of horizontal composition.

> [!warning] 4. Believing the pentagon is an arbitrary or ad hoc axiom
> The pentagon looks like a mysterious five-sided choice, so it is tempting to treat it as one coherence law among many possible ones. In fact it is forced: it is the unique relation making the binary tensor generate the correct operad of arities, equivalently the length-four instance of the single unbiased associativity axiom ([[Thm - Biased and Unbiased Monoidal Categories Coincide]]). Drop it and re-bracketing a four-fold tensor becomes ambiguous, with a concrete five-object diagram of associators that fails to commute. The pentagon is necessary and sufficient, not optional.

---

# Problem-Solving Strategy

The problems here are won at the moment you decide which of the two roads — globular or monoidal — you are on, and whether you want the strict, weak, biased, or unbiased presentation. Begin by classifying.

If the problem **hands you cellular data** — a tower of cells with sources and targets, or a request to define an $n$-category — your first move is structural recognition: this is a [[Def - Globular Set|globular set]], a [[Def - Presheaf|presheaf]] on $\mathbb{G}$, and that identification gives you limits, colimits, free objects, and the topos toolkit for nothing. To put composition on it, work dimension by dimension (associativity and identities in each direction) and then *check interchange between every pair of dimensions* — interchange is the only cross-dimensional axiom and the usual place a "would-be $n$-category" fails. When building examples or proving composition is functorial, switch to the [[Def - Enriched Category|iterated-enriched]] definition, where interchange is automatic (it is functoriality of the enriched composition) and the induction "enrich in the level below" generates the whole tower.

If the problem **is about a tensor product** — proving a coherence identity, comparing definitions, or transporting structure — decide between biased and unbiased *based on the task*. For coherence questions, go [[Def - Unbiased Monoidal Category|unbiased]] immediately: in the unbiased frame there is one operation per arity, so any two canonical maps with the same source and target are equal by [[Thm - Coherence for Unbiased Monoidal Categories|coherence]], and the question dissolves. For concrete computations, the [[Def - Monoidal Category|biased]] binary tensor is usually cleaner, and you may move between the two freely by [[Thm - Biased and Unbiased Monoidal Categories Coincide]]. When a calculation threatens to drown in associators, [[Thm - Strictification of Monoidal Categories|strictify]]: replace the category by a strict equivalent, compute with brackets suppressed, and transport back — valid for any monoidal-equivalence-invariant property, which is almost all of them.

If the problem **involves transporting algebraic structure** — does a functor send [[Def - Monoid in a Monoidal Category|monoids]] to monoids, modules to modules — the right notion is a [[Def - Weak and Lax Monoidal Functor|lax (or weak) monoidal functor]], and the diagnostic is the comparison map: is it invertible, and which way does it point? Lax (into $F$ of the tensor, possibly non-invertible) transports monoids; oplax transports comonoids; weak gives monoidal equivalence. Remember the touchstone: a monoid *is* a lax functor from the terminal monoidal category, so "carries algebra" and "is lax monoidal" are the same condition.

If the problem **has a one-object (or one-cell) flavour** — two compatible products, a structure with a single object — climb the periodic table. View the structure one dimension up with a single $0$-cell, so horizontal composition becomes a tensor; if it has a single $1$-cell too, run the [[Ex - The Eckmann-Hilton argument|Eckmann–Hilton argument]] to extract a braiding or a commutativity. This is the engine behind "monoidal $=$ one-object bicategory," "braided $=$ one-object-one-$1$-cell tricategory," and the abelianness of higher homotopy [[Def - Group|groups]].

The meta-strategy threading all of this: **every question in this chapter is the question "what is this structure, up to the right notion of sameness?"** — and the right notion is never equality of objects but equivalence. Strictness, biasedness, and the choice of shape are presentation artefacts that coherence and strictification let you change at will, *until* you reach dimension three, where strictification fails and the surviving coherence cells become genuine content. Knowing which simplifications are free (dimensions $\leq 2$) and which are forbidden (the Eckmann–Hilton braiding upstairs) is the whole art.

---

# Most Reusable Properties

- **[[Thm - Coherence for Unbiased Monoidal Categories|Coherence]]** (every canonical diagram commutes): the single most-used fact in the chapter, because it is *free* the moment a coherent tensor is in sight. Reach for it whenever two ways of bracketing, comparing, or assembling tensors threaten to differ — you never need to compute the associator string, only observe that both maps are canonical with the same endpoints. Its most powerful disguised use is licensing *bracket-free notation* and *string diagrams*: every tensor-network identity silently invokes it. Recognise its applicability whenever a calculation is about to fill with associators and unitors.

- **[[Thm - Strictification of Monoidal Categories|Strictification]]** (every monoidal category is equivalent to a strict one): the workhorse for *simplification*. The recognisable setup is "this proof would be clean if only $\otimes$ were strictly associative." Strictify, compute, transport — valid for any monoidal-equivalence-invariant property. Internalising it pays compound interest because it removes coherence bookkeeping from essentially every monoidal calculation; the only caveat, itself reusable, is that it stops working at dimension three.

- **[[Def - Globular Set|Globular set = presheaf on 𝔾]]**: the structural recognition that hands you limits, colimits, free objects, and a topos for free. Its typical use is to convert "a tower of cells with structure maps" into a categorical object with all the standard machinery, and to identify the standard globes $G_n$ (representables) as the basic shapes that probe and build everything. More reusable than any single theorem about $n$-categories, because it underlies all of them.

- **The interchange law** (functoriality of cross-dimensional composition): the one axiom that makes higher composition consistent. Its typical use is as the *check* that distinguishes a genuine [[Def - 2-Category and Bicategory|2-category]] from a category-with-extra-arrows, and as the *engine* of the Eckmann–Hilton argument that manufactures braidings and commutativity. Whenever two compositions can act on the same cells, interchange is the first thing to write down and the last thing to forget.

- **[[Thm - Biased and Unbiased Monoidal Categories Coincide|Biased = unbiased]]**: the licence to pick the convenient presentation. Reach for it to convert a coherence problem (best unbiased) into a computation (best biased) or to recognise that an all-arity universal-property tensor *is* an ordinary monoidal category without checking the pentagon by hand. It reframes the pentagon as a *presentation relation* rather than a mysterious axiom, which is the conceptual unlock of the chapter.

---

# Bridges

1. **Algebraic geometry — the periodic table as a map of "spaces of operations."** The running theme that going up a dimension and restricting to one object yields a multiplication is, in algebraic geometry, the statement that the **loop space** and **classifying space** constructions trade dimensions for group structure. Concretely, for a space $X$ with basepoint, the based loop space $\Omega X$ has a multiplication (concatenate loops) that is associative *up to homotopy* — an $A_\infty$-structure — and $\Omega$ applied again braids it (Eckmann–Hilton), which is the topological avatar of the periodic table's column. The algebro-geometric payoff is the **derived category of coherent sheaves** on a variety, whose monoidal structure (derived tensor $\otimes^{\mathbb{L}}$) is associative only up to coherent homotopy; strictification fails there exactly as it fails for tricategories, which is why the modern formulation uses symmetric monoidal stable $\infty$-categories.

> [!note]- Algebraic geometry background
> A **commutative ring** $R$ (e.g. polynomials $k[x_1, \dots, x_n]$) has a **prime spectrum** $\mathrm{Spec}\,R$, the set of its prime ideals, topologized by the **Zariski topology** (closed sets are the zero loci of subsets of $R$). This is the geometric object dual to the algebra: the contravariant assignment $R \mapsto \mathrm{Spec}\,R$ is the **ring–geometry dictionary**, and $\mathbf{AffSch} \simeq \mathbf{CRing}^{op}$. A **sheaf** on $\mathrm{Spec}\,R$ assigns compatible data to open sets; **coherent sheaves** are the geometric analogue of finitely generated modules. The **derived category** $D^b(\mathrm{Coh}\,X)$ is built from complexes of coherent sheaves with quasi-isomorphisms inverted, and it carries a **derived tensor product** $\otimes^{\mathbb{L}}$ (resolve, then tensor) that is symmetric monoidal *up to coherent homotopy*. The categorical lesson the chapter supplies: this monoidal structure cannot be strictified (it lives in dimension $> 2$), which is precisely why $\infty$-categorical foundations are needed to handle it cleanly — the same Eckmann–Hilton/strictification-failure phenomenon studied here.

2. **Algebraic topology — Eckmann–Hilton and the abelianness of higher homotopy groups.** The classical theorem that $\pi_n(X)$ is abelian for $n \geq 2$ is *exactly* the [[Ex - The Eckmann-Hilton argument|Eckmann–Hilton argument]]: on $\pi_n$ there are two composition operations (concatenation in two different coordinate directions) that share a unit and satisfy interchange, and Eckmann–Hilton forces them to coincide and to be commutative. In our language, $\pi_n(X)$ is the endomorphisms of a point in a one-object-one-$1$-cell-...-one-$(n-1)$-cell higher groupoid, which is a $k$-tuply monoidal structure with $k \geq 2$, hence symmetric. This is the periodic table predicting a hundred-year-old homotopy theorem.

3. **Categorical probability and Markov categories — symmetric monoidal as the home of "parallel processes."** A [[Def - Monoidal Category|symmetric monoidal category]] is the algebra of resources combined in parallel ($\otimes$) and in series ($\circ$); **Markov categories** are symmetric monoidal categories with extra copy and discard maps, in which a morphism $X \to Y$ is a "stochastic process" and the symmetry encodes that the order of independent inputs is irrelevant. The chapter grounds this directly: the symmetric (not merely braided) structure is the top of the relevant periodic-table column, and a **probability monad** (Giry, distribution) is a [[Def - Weak and Lax Monoidal Functor|monoidal monad]] whose algebras are the convex spaces on which probabilistic reasoning takes place. The user's research on categorical systems and agent foundations runs on exactly this symmetric monoidal / copy-discard substrate.

4. **Logic and type theory — coherence as proof normalization.** A monoidal category models the multiplicative fragment of (linear) logic, with $\otimes$ the conjunction and an internal hom the implication; the structural rules of associativity and unit are exactly the associator and unitors. [[Thm - Coherence for Unbiased Monoidal Categories|Coherence]] is then the semantic statement that proofs differing only by these structural rules are *equal*, and [[Thm - Strictification of Monoidal Categories|strictification]] is the existence of a normal form in which the structural rules are invisible — the categorical counterpart of cut-elimination for associativity. This is one face of the **Curry–Howard–Lambek** correspondence between proofs, programs, and morphisms.

---

# Insights

**The unifying frame: dimension and multiplication are interchangeable.** The one idea organising the whole chapter is that *climbing a dimension and looking at a single object is the same as gaining a multiplication.* A [[Def - Monoidal Category|monoidal category]] is a one-object [[Def - 2-Category and Bicategory|bicategory]]; a braided monoidal category is a one-object-one-$1$-cell tricategory; a [[Def - Monoid in a Monoidal Category|monoid]] is a one-object category. Every row of the periodic table is the previous structure "with one fewer object and one more multiplication," and every column is "one dimension up with the same number of degenerate cells." Once this frame is installed, results that look like separate theorems — that higher homotopy groups are abelian, that monoidal categories have associators, that symmetric structures stabilize — are seen to be the same statement read along different axes of one table.

**The true name of coherence is "one operation per arity."** The textbook coherence theorem is stated as "every diagram of associators and unitors commutes," which sounds like a fact you must verify diagram by diagram. The operational truth, visible only in the [[Def - Unbiased Monoidal Category|unbiased]] picture, is that the operad of tensorings has *exactly one operation of each arity*, so there is simply nothing for two canonical maps to disagree about: both factor through the unique arity-$m$ corolla $\otimes_m$. When you meet a coherence question, do not picture a pentagon — picture a tree contracting to a single node, uniquely. That is why the pentagon is necessary and sufficient and why the unbiased coherence proof is almost a tautology.

**Strictification is a low-dimensional miracle, and its failure is the subject's reason for existing.** It is tempting to conclude from "every monoidal category is strict up to equivalence" and "every bicategory is biequivalent to a strict $2$-category" that weakness is always a removable convenience. The decisive insight is that this *stops* at dimension three: not every [[Higher Categories — Strict n-Categories and Notions of Monoidal Category#§3 Coherence and the Periodic Table|tricategory]] is equivalent to a strict $3$-category, and the obstruction is the braiding manufactured by Eckmann–Hilton. So weak higher categories are not a technical inconvenience to be strictified away; from dimension three the coherence cells carry irreducible information. The entire apparatus of operads, opetopes, and globular operads in the rest of these notes exists precisely because this miracle runs out.

**Interchange is the seed of commutativity.** A single axiom — that the two ways of contracting a grid of cells agree — is doing far more than ensuring pasting is well-defined. Fed two unital operations sharing a unit, interchange *forces* them to be equal, associative, and commutative: this is the [[Ex - The Eckmann-Hilton argument|Eckmann–Hilton argument]], and it is the mechanism by which braidings and symmetries appear as you climb the periodic table, and by which $\pi_n$ becomes abelian. The trigger to internalise: whenever you see two compatible operations on the same objects with a shared unit, expect commutativity to be forced, not assumed. Commutativity in higher mathematics is very often interchange in disguise.

**Choice of shape is a modelling decision, not a mathematical given.** Globes, simplices, opetopes, cubes — each is a different *shape category* whose presheaves carry the cells of a higher structure, and the choice trades convenience in one direction for difficulty in another. Globes make *strict* composition cleanest (one source, one target, unique composites) but make *weak* composition hardest (forcing the globular-operad machinery); simplices make weak composition natural (the quasi-category story) but obscure strict algebra. There is no canonical shape; there are only shapes suited to particular questions. Recognising that a definitional dispute in higher category theory is often a *shape* dispute, not a substantive one, is among the most clarifying meta-insights the subject offers.
