---
type: definition
subject: higher-categories
prereqs:
  - "Def - Simplicial Set"
  - "Def - Segal Category and Complete Segal Space"
  - "Def - Pullback and Pushout"
  - "Def - Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

$\Delta$ is the **simplex category** (objects the ordinals $[m] = \{0 < 1 < \dots < m\}$, morphisms order-preserving maps). An **$n$-fold simplicial set** is a functor $(\Delta^{op})^n \to \mathbf{Set}$; equivalently, by currying, a functor $\Delta^{op} \to [\,n{-}1\text{-fold simplicial sets}\,]$. We write a Tamsamani–Simpson $n$-category as $A$, with $A_m \in \{(n{-}1)\text{-categories}\}$ its "space of $m$-simplices" in the *first* simplicial direction; $A_0$ is the **object piece**, $A_1$ the **morphism piece**, and the **spine / Segal map** is
$$
A_m \longrightarrow A_1 \times_{A_0} A_1 \times_{A_0} \cdots \times_{A_0} A_1 \qquad (m \text{ factors}),
$$
the iterated [[Def - Pullback and Pushout|fibre product]] over $A_0$. Here $\times_{A_0}$ is taken in the world of $(n-1)$-categories. We write $\simeq$ for an **$(n-1)$-equivalence** — the inductively-defined notion of equivalence one dimension down. The recursion bottoms out at $n=0$: a $0$-category is a **set** (a discrete object). The full registry is on [[Higher Categories — Other Definitions of Weak n-Categories]].

---

# Axiom Motivation

The previous page defined Segal categories and complete Segal spaces — one-step models of $(\infty,1)$-categories, where the morphism piece $X_1$ is a *space* and the Segal condition controls composition in a single direction. The Tamsamani–Simpson definition asks the obvious next question: **what if the morphism piece is itself an $(n-1)$-category, and we apply the Segal idea once per dimension?** The motivation is to get *all* of weak $n$-category theory out of the *single* Segal condition, iterated, with no new coherence data introduced at any stage. It is the most economical of the geometric definitions precisely because it reuses one idea $n$ times.

Begin one dimension at a time. A weak $1$-category should be an ordinary [[Def - Category|category]]: objects, hom-*sets*, composition. Record it as a simplicial *set* $A : \Delta^{op} \to \mathbf{Set}$ (its nerve) and impose the Segal condition $A_m \cong A_1 \times_{A_0} \cdots \times_{A_0} A_1$ — composition is then "a property", exactly as for the [[Def - Segal Category and Complete Segal Space|Segal models]]. For a weak $2$-category we want hom-*categories* rather than hom-sets, because between two morphisms there should be $2$-cells. So we let the morphism piece $A_1$ be not a set but a *$1$-category*, i.e. we record the whole thing as a functor $A : \Delta^{op} \to \{1\text{-categories}\}$ — a *simplicial object in categories* — and again impose the Segal condition, now with the fibre products taken in categories and "$\cong$" relaxed to "equivalence of categories". The hom-category between objects $x, y$ is the fibre of $A_1 \to A_0 \times A_0$ over $(x,y)$, and the Segal condition makes composition of these hom-categories exist and be coherent up to equivalence.

The pattern is now forced. A weak $n$-category should have hom-objects that are weak $(n-1)$-categories. So *define* a Tamsamani–Simpson $n$-category to be a functor $A : \Delta^{op} \to \{(n-1)\text{-categories}\}$ satisfying the Segal condition, where the fibre products are taken among $(n-1)$-categories and the Segal maps are required to be *$(n-1)$-equivalences* — the notion of equivalence supplied by the previous stage of the recursion. Unfolding the recursion, $A$ is an **$n$-fold simplicial set** $(\Delta^{op})^n \to \mathbf{Set}$ satisfying a Segal condition in each of the $n$ simplicial directions, with appropriate "constancy/globularity" conditions ensuring that the higher directions really do encode *cells between cells* and not an unrelated $n$-fold grid.

Why iterate the *Segal* condition rather than inventing fresh coherence at each level? Because the Segal condition already says "composition exists and is unique up to the next level's equivalence", and "the next level's equivalence" is exactly what the recursion provides. So coherence at level $k$ is automatically governed by equivalence at level $k$, with no separate associator-pentagon data to write down. This is the design payoff: a single idea, recursively applied, generates the entire infinite hierarchy of coherence conditions that the algebraic definitions must spell out by hand.

What goes wrong if we drop the Segal condition in some direction? Then composition in that dimension is unconstrained — the $m$-simplices bear no relation to chains of $1$-simplices — and the structure ceases to be a higher category in that direction; it is just an $n$-fold grid of sets. What if we demand strict equality instead of $(n-1)$-equivalence in the Segal maps? Then we rebuild *strict* $n$-categories, which are known to be too rigid (they fail to model homotopy $3$-types and beyond). And what about the **constancy condition** — the requirement that $A_0$ (and, inductively, the degenerate pieces) be *discrete* in the appropriate sense? Dropping it allows "objects" to carry spurious higher structure that double-counts cells, breaking the correspondence with the intended notion; this is the iterated analogue of the discreteness-of-$X_0$ condition for [[Def - Segal Category and Complete Segal Space|Segal categories]]. Each axiom is therefore load-bearing: Segal supplies composition, equivalence (not equality) supplies weakness, and constancy supplies the correct bookkeeping of cells.

---

# The Definition

Define **weak $n$-categories in the Tamsamani–Simpson sense** by induction on $n$.

**Base case $n = 0$.** A Tamsamani–Simpson **$0$-category** is a **set**. The notion of **$0$-equivalence** is **bijection**.

**Inductive step.** Suppose the category of Tamsamani–Simpson $(n-1)$-categories and the notion of **$(n-1)$-equivalence** are defined. A Tamsamani–Simpson **$n$-category** is a functor
$$
A : \Delta^{op} \longrightarrow \{\text{Tamsamani–Simpson } (n-1)\text{-categories}\}, \qquad [m] \mapsto A_m,
$$
satisfying:

1. **Constancy / discreteness.** $A_0$ is a *discrete* $(n-1)$-category (a set), playing the role of the set of objects.

2. **Segal condition.** For each $m \ge 2$, the Segal map
$$
A_m \longrightarrow A_1 \times_{A_0} A_1 \times_{A_0} \cdots \times_{A_0} A_1 \qquad (m \text{ factors})
$$
is an **$(n-1)$-equivalence**, where the [[Def - Pullback and Pushout|fibre products]] are taken in Tamsamani–Simpson $(n-1)$-categories.

A morphism of Tamsamani–Simpson $n$-categories is a natural transformation of such functors. Composing the Segal-inverse with the long-edge face $d_1 : A_2 \to A_1$ gives the (homotopy-unique) **composition** $A_1 \times_{A_0} A_1 \to A_1$ up to $(n-1)$-equivalence.

**The notion of $n$-equivalence.** A morphism $f : A \to B$ of Tamsamani–Simpson $n$-categories is an **$n$-equivalence** if it is (i) **essentially surjective** — surjective on objects up to equivalence in the truncated homotopy category — and (ii) **fully faithful** — for all objects $x, y$ the induced morphism of hom-$(n-1)$-categories $A(x,y) \to B(fx, fy)$ is an $(n-1)$-equivalence. This closes the recursion, supplying the equivalence notion needed by the next stage. (**Simpson's** variant builds the same notion using the language of *Segal categories enriched iteratively*, producing an equivalent theory with better-behaved limits.)

---

# Categorical / Structural Definition

Structurally, the definition is **iterated internal/enriched category theory done up to homotopy**. A weak $1$-category is a category. A weak $2$-category is a category *weakly enriched* in weak $1$-categories. A weak $n$-category is a category weakly enriched in weak $(n-1)$-categories — where "weakly enriched" is made precise by recording the enrichment as a Segal-type simplicial object rather than as strict hom-objects with strict composition. This places Tamsamani–Simpson exactly parallel to the [[Def - Enriched Category|enriched-category]] approach (Trimble's definition is the same idea with the enrichment controlled by an operad instead of by a Segal condition), and parallel to the [[Def - Segal Category and Complete Segal Space|complete-Segal-space]] approach (which is the $n=1$ case, $A_1$ a space, plus completeness).

The single conceptual content is: **an $n$-category is an $n$-fold simplicial set in which each simplicial direction satisfies the Segal condition relative to the equivalence notion of the directions below it.** Every coherence law of a weak $n$-category — associativity, the pentagon, the interchange laws, and their higher analogues — is a *consequence* of these iterated Segal conditions, never a separate axiom. That is the structural slogan and the reason the definition is so economical.

---

# Relate to Other Fields / Compression

The Tamsamani–Simpson definition is the higher-categorical incarnation of the principle, ubiquitous in homotopy theory, that **"weak structure = simplicial object satisfying a Segal-type condition"**. The same template defines $A_\infty$- and $E_\infty$-spaces (Segal/Γ-space conditions), homotopy-coherent diagrams (the homotopy-coherent nerve), and descent data (the Čech nerve with a sheaf condition). In each, a strict algebraic structure is replaced by a simplicial object whose lower pieces determine the higher ones up to homotopy. Tamsamani–Simpson is this template applied $n$ times to the structure "category".

**True name:** A Tamsamani–Simpson $n$-category is *an $n$-fold simplicial set that is Segal in every direction and discrete on its object pieces* — operationally, "iterate `$A_m \simeq A_1 \times_{A_0} \cdots \times_{A_0} A_1$` once per dimension, with `$\simeq$` the equivalence from one dimension down". The whole definition is one equation, recursively quantified over dimensions.

---

# Examples / Corollaries

**Is an instance — an ordinary category, as a Tamsamani–Simpson $1$-category.** For $n = 1$ the definition is: a functor $\Delta^{op} \to \mathbf{Set}$ with $A_0$ discrete and the Segal maps *bijections* ($0$-equivalences are bijections). This is exactly the [[Def - Kan Complex and the Nerve|nerve]] characterisation of an ordinary [[Def - Category|category]]: a simplicial set is a nerve iff its Segal maps are bijections. So Tamsamani–Simpson $1$-categories *are* ordinary categories — the level-$1$ sanity check.

**Is an instance — a bicategory, as a Tamsamani–Simpson $2$-category.** For $n = 2$, $A$ is a simplicial object in categories with $A_0$ a set and the Segal maps equivalences of categories. The hom-category between $x$ and $y$ is the fibre of $A_1$ over $(x,y)$; composition is the Segal-inverse followed by $d_1$, associative up to the equivalence supplied by $A_3$. Tamsamani proved these are equivalent to **bicategories** — the level-$2$ sanity check, which the definition passes.

**Is an instance (groupoidal case) — the Poincaré $n$-groupoid of a space.** Truncating a [[Def - Topological Space|space]]'s singular complex at level $n$ and taking the evident $n$-fold structure gives a Tamsamani–Simpson $n$-*groupoid* (all cells invertible up to higher equivalence) modelling the $n$-type of the space. This is the [[Thm - The Homotopy Hypothesis|homotopy hypothesis]] at finite level: weak $n$-groupoids model homotopy $n$-types.

**Is NOT an instance — an arbitrary $n$-fold simplicial set.** A general functor $(\Delta^{op})^n \to \mathbf{Set}$ is *not* a Tamsamani–Simpson $n$-category: without the Segal conditions there is no composition, and without the constancy conditions the object pieces carry spurious structure. It is the raw data with none of the categorical content.

**Is NOT an instance — a strict $n$-category for $n \ge 3$ as a model of all $n$-types.** A *strict* $n$-category does satisfy the Segal conditions with strict *equality*, so it is a (very special) Tamsamani–Simpson $n$-category. But the strict $n$-groupoids do **not** model all homotopy $n$-types for $n \ge 3$ — the standard witness is that no strict $3$-groupoid has the homotopy type of $S^2$ (its Whitehead product / Postnikov data cannot be realised strictly). So strictness is a genuine loss: the Tamsamani–Simpson definition *needs* the equivalence-not-equality relaxation to be correct, and the strict ones are an instance that fails to be representative.

**Calibration check.** Verify that unwinding the $n=1$ definition gives precisely the Segal/nerve condition for ordinary categories, and that the $n=2$ hom-pieces are categories (not sets). Check that the recursion's equivalence notion at level $n$ is "essentially surjective + fully faithful in hom-$(n-1)$-categories", and that this reduces at $n=1$ to the usual "essentially surjective + fully faithful" for functors. If you can explain why iterating the *Segal condition* avoids ever writing down a pentagon axiom — because coherence at each level is governed by equivalence at the level below — you have understood the definition.

---

# Unlocked by This

> [!tip] $(\infty,n)$-Categories and the Cobordism Hypothesis *(from Higher Algebra / Mathematical Physics)*
> Letting the recursion run to $\infty$ (replacing "$(n-1)$-category" by "space" at the bottom and never truncating) yields **$(\infty,n)$-categories** in the iterated-Segal style — Rezk's $\Theta_n$-spaces and Barwick's $n$-fold complete Segal spaces are the descendants. These are the natural home of the **cobordism hypothesis** of Baez–Dolan and Lurie: the $(\infty,n)$-category of fully-extended topological field theories is freely generated by one fully-dualizable object.

> [!tip] Higher Stacks *(from Algebraic Geometry)*
> Simpson developed the $n$-category machinery precisely to build **higher stacks** — sheaves of $n$-groupoids on a site, the objects of higher and **derived algebraic geometry**. The Segal-style definition is what makes the descent (gluing) conditions for higher stacks tractable, since descent is itself a Segal/Čech condition one level up.
