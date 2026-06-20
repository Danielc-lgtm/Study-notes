---
type: definition
subject: higher-categories
prereqs:
  - "Def - Monad and Comonad"
  - "Def - Adjunction"
  - "Def - Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

A **globular set** $X$ is a sequence of sets $X_0, X_1, X_2, \dots$ (cells of each dimension) with source and target maps $s, t : X_{n+1} \to X_n$ satisfying the **globularity equations** $ss = st$ and $ts = tt$ (the source and target of a cell share their own source, and share their own target). A cell in $X_n$ is an **$n$-cell**; a $0$-cell is an object, a $1$-cell an arrow, a $2$-cell an arrow-between-arrows. A globular set is **reflexive** if it additionally carries identity-inserting maps $i : X_n \to X_{n+1}$ with $s i = t i = \mathrm{id}$, giving a degenerate $(n+1)$-cell on every $n$-cell. We write $H$ for the **Penon monad** on reflexive globular sets, $\eta, \mu$ for its unit and multiplication, and **str-ω-Cat** for strict ω-categories. The terms "globular set", "reflexive globular set", "strict ω-category", and "globular operad" are developed in companion chapters of this vault that are not yet written, so they appear here as **bold plain text** and are recalled inline. The full registry is on [[Higher Categories — Other Definitions of Weak n-Categories]].

---

# Axiom Motivation

The Batanin–Leinster route to weak ω-categories carries a lot of machinery: the free strict ω-category monad, the bicategory of operads over it, contractions, and the initial contractible operad. Penon's question was whether all of that could be compressed into a single, self-contained monad whose algebras are weak ω-categories — no operads, no choice of generating data, just one universal construction. The motivation for the definition is therefore best understood as a search for the *most economical* algebraic encoding of "a higher category with chosen, weakly-coherent composites".

Start from what we are trying to capture. A **strict** ω-category is the easy, rigid thing: a globular set with composition operations in every dimension that are *strictly* associative and unital and *strictly* satisfy the interchange law. We know exactly what these are, and we know they are too rigid — the strict ones do not model homotopy types beyond dimension $3$, so they are the wrong notion of "higher category". A **weak** ω-category should be the same shape of object, but with all those equalities relaxed to *invertible coherence cells*: associativity holds only up to a specified $(n+1)$-cell, and so on up. The design problem is to specify "and so on up" without writing down an infinite list of coherence axioms by hand.

Penon's decisive idea is to encode the weakening as a comparison *to* the strict world. Consider, over a given reflexive globular set $X$, all the ways of presenting $X$ as the underlying globular set of something that *maps* to a strict ω-category in a controlled way — a **stretching**. A stretching over $X$ is a triple $(M, X \to M, M \to Q)$ where $Q$ is a strict ω-category, the map $M \to Q$ is the identity on underlying cells (it "stretches" $M$ onto $Q$ without changing cells), and it comes equipped with a **contraction**: for any two parallel $n$-cells of $M$ that become *equal* in $Q$, a chosen $(n+1)$-cell of $M$ connecting them. The contraction is exactly the device that turns equalities (which hold strictly in $Q$) into coherence cells (which hold weakly in $M$). The Penon monad $H$ is built from the *universal*, or *free*, stretching over $X$: $HX$ is the reflexive globular set underlying the initial stretching on $X$. Its algebras — globular sets $X$ with a structure map $HX \to X$ — are exactly the Penon weak ω-categories.

Why this specific construction and not a nearby variant? The contraction is non-negotiable: drop it, and the comparison $M \to Q$ records *that* cells become equal in the strict world but provides no cell witnessing it weakly, so there is no weak associator and the algebras degenerate to something with no coherence data. Strengthen it — demand the chosen connecting cells be *invertible on the nose* or be *unique* — and you over-rigidify: uniqueness of the coherence cells collapses the weak structure back towards the strict one (the same phenomenon by which *unique* inner-horn fillers give ordinary categories rather than [[Def - Quasi-Category|quasi-categories]]). The contraction's chosen-but-not-unique cells are the Goldilocks condition, precisely as in every other definition in this chapter.

A subtler axiom is **reflexivity**, and here lies a famous correction. Penon's original 1999 definition used *non-reflexive* globular sets. Cheng and Makkai observed that this is too weak: without chosen degeneracies, the resulting weak ω-categories lack the strict identity cells one expects, and the definition fails to recover the right low-dimensional structures. The repair is to run the entire construction over *reflexive* globular sets, so that identities are part of the data from the start and the stretching respects them. Dropping reflexivity is therefore not a harmless simplification — it produces a genuinely different, defective notion. This is a good illustration of how delicate the design of a higher-categorical definition is: a single choice of base category changes whether the definition is correct.

---

# The Definition

Let $\mathbf{RGlob}$ be the category of **reflexive globular sets** and $\mathbf{str\text{-}\omega\text{-}Cat}$ the category of **strict ω-categories**; there is a forgetful functor $U : \mathbf{str\text{-}\omega\text{-}Cat} \to \mathbf{RGlob}$.

A **stretching** consists of a reflexive globular set $M$, a strict ω-category $Q$, a map $p : M \to UQ$ of reflexive globular sets that is **identity-on-cells** in each dimension, together with a **contraction** on $p$: for every pair of parallel $n$-cells $a, b \in M_n$ (same source, same target) with $p(a) = p(b)$ in $Q$, a chosen $(n+1)$-cell $[a,b] \in M_{n+1}$ with source $a$ and target $b$, such that $p([a,b])$ is the identity (degenerate) cell. Morphisms of stretchings are the evident commuting maps respecting the chosen contraction cells.

For each reflexive globular set $X$ there is a **free (universal) stretching** $X \to M_X \to Q_X$: an initial object among stretchings under $X$. Define
$$
H X := M_X \in \mathbf{RGlob},
$$
the reflexive globular set underlying the universal stretching on $X$. This assignment is the functor part of a **[[Def - Monad and Comonad|monad]]** $(H, \eta, \mu)$ on $\mathbf{RGlob}$, the **Penon monad**, where the unit $\eta_X : X \to HX$ is the universal map and the multiplication $\mu_X : HHX \to HX$ comes from the universal property.

A **Penon weak ω-category** is an **[[Def - Monad and Comonad|algebra]]** for $H$: a reflexive globular set $X$ together with a structure map $\theta : HX \to X$ satisfying the unit law $\theta \circ \eta_X = \mathrm{id}_X$ and the associativity law $\theta \circ H\theta = \theta \circ \mu_X$. A **morphism** of Penon weak ω-categories is a morphism of $H$-algebras. A **Penon weak $n$-category** is obtained by truncating: an $H$-algebra whose underlying globular set has no nondegenerate cells above dimension $n$.

---

# Categorical / Structural Definition

The structural content is best stated as a free–forgetful **[[Def - Adjunction|adjunction]]** whose induced monad is $H$. The category of stretchings forgets, in two stages, to reflexive globular sets: a stretching $X \to M \to Q$ has an underlying $X$. The universal-stretching construction is the *left adjoint* to a forgetful functor (from stretchings, or equivalently from a comma-category built over $U : \mathbf{str\text{-}\omega\text{-}Cat} \to \mathbf{RGlob}$), and a **[[Def - Adjunction|left adjoint followed by the forgetful functor]]** is exactly a monad. So $H$ is not an ad hoc gadget but the monad of an adjunction, and "Penon weak ω-category $=$ $H$-algebra" places the definition inside the standard **monadic** framework: weak ω-categories are the [[Def - Monad and Comonad|Eilenberg–Moore algebras]] of a single monad on a presheaf-like base.

This is the cleanest way to compare Penon with **Batanin–Leinster**. The Batanin–Leinster definition also produces a monad on globular sets — the monad of the initial contractible **globular operad** $L$ — and its weak ω-categories are the $L$-algebras. Both definitions are thus "algebras for a monad on (reflexive) globular sets"; the comparison problem is whether the two monads have equivalent categories of algebras. They are not literally the same monad — Penon's is built from stretchings and contractions on a single comparison map, the Batanin–Leinster one from an operad of pasting diagrams — but Cheng's analysis (after the reflexive correction) shows the definitions are very closely related and produce the same notion in low dimensions, with full equivalence the expected but technically demanding statement. The structural lesson is that *the choice of monad is the choice of definition*, and the algebraic definitions of this chapter are exactly a list of monads on globular sets.

---

# Relate to Other Fields / Compression

Penon's construction is, in compressed form, the **comma-category / glued** construction applied to the forgetful functor from strict ω-categories. You take the strict world (which you understand), you consider all *weak* objects equipped with a structured comparison to it (the stretchings), you take the universal such comparison, and you read off the monad. The same shape recurs whenever one builds a weak notion by "freely resolving" a strict one against a contraction — it is the algebraic mirror of the **fibrant replacement** move in [[Def - Model Category|model category theory]], where a poorly-behaved object is replaced by a weakly-equivalent well-behaved one and the replacement is governed by lifting (contraction is the globular form of a lifting against parallel pairs).

**True name:** A Penon weak ω-category is *a reflexive globular set equipped with chosen, coherently-related composites and coherence cells, all of them generated freely from one universal stretching* — operationally, "a globular set on which the single Penon monad acts". When you meet the phrase, do not picture the stretching machinery; picture an $H$-algebra, i.e. a globular set with one structure map $HX \to X$, exactly parallel to how a group is "a set with one structure map" for the free-group monad.

---

# Examples / Corollaries

**Is an instance — every strict ω-category.** A strict ω-category is in particular a reflexive globular set with composition, and the strict composites are a (degenerate) choice of weak composites, so every strict ω-category is a Penon weak ω-category. The structure map $HX \to X$ uses the strict operations to evaluate every freely-generated composite and sends every contraction cell to an identity. This is the analogue of "every abelian group is a group": the rigid objects sit inside the weak ones as a special case where all the coherence cells happen to be identities.

**Is an instance — the Penon weak $1$-categories are ordinary categories.** Truncating to dimension $1$, an $H$-algebra is a reflexive globular set with $0$-cells and $1$-cells, chosen composites of composable $1$-cells, chosen identities, and — because there are no nondegenerate $2$-cells — the coherence cells are forced to be identities, so associativity and unitality hold *strictly*. The result is exactly an ordinary **[[Def - Category|category]]**. This is the first mandatory sanity check (truncation to level $1$), and Penon's definition passes it.

**Is an instance — Penon weak $2$-categories are bicategories.** At dimension $2$ the chosen $2$-cells from the contraction become the associator and unitor isomorphisms, and the universal property forces them to satisfy the pentagon and triangle coherences. The truncated $H$-algebras are therefore (equivalent to) **bicategories** — the level-$2$ sanity check, which several early definitions failed and Penon's passes (after the reflexive correction).

**Is NOT an instance — a bare reflexive globular set with no structure map.** A reflexive globular set $X$ on its own is *not* a Penon weak ω-category: it has cells and identities but no composition. There is no canonical map $HX \to X$ — providing one is precisely the additional data. This is the analogue of "a set is not a group": the underlying data is necessary but the algebra structure is the whole point.

**Is NOT an instance — the non-reflexive Penon construction.** Penon's *original*, non-reflexive definition does **not** correctly capture weak ω-categories: its algebras lack the expected strict identities, and the definition fails to recover the right structures (this is the Cheng–Makkai observation). It is the standard cautionary non-example — a definition that looks right but is subtly defective until reflexivity is restored.

**Calibration check.** Verify that the two algebra axioms $\theta \circ \eta_X = \mathrm{id}_X$ and $\theta \circ H\theta = \theta \circ \mu_X$ are exactly the unit and associativity laws for an algebra over the monad $H$ (compare with any [[Def - Monad and Comonad|monad algebra]]). Check that truncating an $H$-algebra to dimension $0$ leaves just a set (a discrete higher category). If you can explain *why* the contraction cells must be chosen-but-not-unique — rather than unique — by appealing to the same over-rigidification that makes *unique* horn-fillers collapse a [[Def - Quasi-Category|quasi-category]] to an ordinary category, you have understood the definition.

---

# Unlocked by This

> [!tip] Grothendieck–Maltsiniotis Weak ω-Groupoids *(from Higher Algebra)*
> Restricting the Penon-style "algebras for a globular monad" philosophy to the *invertible* case, and replacing the specific monad by a general **coherator**, gives the **Grothendieck–Maltsiniotis** definition of weak ω-groupoid. This is the precise algebraic object for which the **homotopy hypothesis** is conjectured, and it is the most direct descendant of Penon's one-monad approach.

> [!tip] Identity Types and Weak ω-Groupoids *(from Homotopy Type Theory)*
> In **homotopy type theory**, every type $A$ carries identity types $a =_A b$, then identity types of those, without end. Lumsdaine and van den Berg–Garner proved this tower makes every type a weak ω-groupoid in essentially Penon's algebraic sense — the operations are the path-induction-generated composites, and the coherence cells come from the contractibility of based path spaces. Penon's globular-algebraic stance is, in this light, the categorical shadow of the **Curry–Howard–Lambek** correspondence one dimension at a time.
