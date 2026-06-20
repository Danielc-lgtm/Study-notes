---
type: definition
subject: higher-categories
prereqs:
  - "Def - Globular Operad"
  - "Def - Contraction on a Globular Operad"
  - "Def - The Free Strict ω-Category Monad"
  - "Def - Algebra for a Monad"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Let $(T, \eta, \mu)$ be the [[Def - The Free Strict ω-Category Monad|free strict ω-category monad]] on **globular sets**, with $T1 = \mathrm{pd}$ the **pasting diagrams**. Let $\mathbf{OC}$ denote the category of [[Def - Globular Operad|globular]] **operads-with-contraction**: objects are pairs $(P, \chi)$ with $P$ a globular operad and $\chi$ a [[Def - Contraction on a Globular Operad|contraction]] on $P$; morphisms $(P, \chi) \to (P', \chi')$ are operad maps $f : P \to P'$ that **preserve the contraction**, $f(\chi_\pi(\alpha^-, \alpha^+)) = \chi'_\pi(f\alpha^-, f\alpha^+)$. The initial object of $\mathbf{OC}$ is written $(L, \chi)$ and called the **Batanin–Leinster operad**. For a globular operad $P$, $\mathrm{Alg}(P)$ is its category of [[Def - Algebra for a Monad|algebras]] (algebras for the induced monad $T_P$). For the $n$-truncated theory, $T^{(n)}$ is the free strict $n$-category monad on $n$-globular sets, $L_n$ the initial $n$-operad-with-contraction, and $\mathbf{Wk\text{-}n\text{-}Cat} = \mathrm{Alg}(L_n)$. The full symbol registry is on [[Higher Categories — Globular Operads and Weak n-Categories]].

This is a **compound page**: it defines two interlocking notions — **weak $\omega$-category** and **weak $n$-category** — because the $n$-categorical definition is the truncation of the $\omega$-categorical one and neither is fully usable without the other. The terms **strict ω-category**, **unbiased bicategory**, and **tame** belong to chapters whose pages are not yet in the vault; they appear in bold and are restated as needed.

---

# Axiom Motivation

This is the culminating definition of the book, and the way to motivate it is to recall the two ingredients we have assembled and see that they fit together with exactly one degree of freedom left to fix. We have, on one hand, the [[Def - The Free Strict ω-Category Monad|free strict ω-category monad]] $T$, whose terminal operad $1$ gives strict $\omega$-categories — too rigid, no room for genuine higher structure. We have, on the other, the notion of a [[Def - Contraction on a Globular Operad|contraction]], which equips a globular operad with a coherent infinite tower of weak composites and coherence cells. The remaining question is: *which* globular operad with a contraction should we use? Different choices give different (a priori different) theories of weak $\omega$-category; we want a canonical one.

The desideratum is canonicity, and there is exactly one canonical choice available: the **initial** operad-with-contraction. Why initial? Consider what is wrong with the alternatives. If we picked an operad with *too many* operations, we would be specifying more ways of composing than coherence requires — for instance, declaring a hundred unrelated ways to compose $f \cdot g \cdot h$ and then forcing them coherently isomorphic, which is bizarre and arbitrary. If we picked one with *too few*, we would lack the operations the contraction demands. The initial object threads the needle: it is *freely generated* by the contraction, containing exactly the operations forced into existence by "every parallel pair must lift" and nothing extraneous. It is the most economical, least arbitrary operad that carries a contraction. Every other operad-with-contraction receives a unique map *from* it, which means: any structure that has weak composites and coherence at all is, canonically, a structure over $L$. That universal property is the precise sense in which $L$-algebras are "*the* weak $\omega$-categories" rather than "*a* notion of weak $\omega$-category".

Granting that the operad must be $L$, the definition writes itself: a **weak $\omega$-category is an $L$-algebra**. Unwind what that says. A globular set $X$ is a weak $\omega$-category when, for every pasting diagram $\pi$, every operation $\theta \in L(\pi)$, and every labelling of $\pi$ by cells of $X$, there is a composite cell — and the operations $\theta$ include both the (unbiased) weak composites and all the coherence cells, with the contraction guaranteeing the coherence cells relate the composites correctly. So an $L$-algebra is a globular set in which you can compose any pasteable diagram, in coherently-many ways, with all coherences present. That is exactly the informal meaning of "weak $\omega$-category", now made precise.

The single subtlety, and the reason this is a compound definition, is **truncation to finite $n$**. We would like a weak $n$-category to be "a weak $\omega$-category with only trivial cells above dimension $n$". The naive attempt — take $L$-algebras supported in dimensions $\leq n$ — almost works but fails in the *top* dimension. In dimensions below $n$, coherence cells can be supplied one dimension up, deferring any relation upward, exactly as in the infinite case. But in dimension $n$ there is no dimension $n+1$ to defer to: the coherence between two competing $n$-fold composites cannot be witnessed by an $(n+1)$-cell, so it must be an *equality*. This is what the "all diagrams commute" coherence theorem for bicategories expresses, and it is why the finite definition needs the extra condition of **tameness**: in the top dimension, parallel operations with the same image are forced equal. So a weak $n$-category is an $L_n$-algebra where $L_n$ is the initial *tame* operad-with-contraction in $n$ dimensions. Drop tameness and you would get a structure with spurious distinct-but-parallel top cells that ought to be equal; impose it one dimension too low and you would strictify prematurely, losing genuine weakness below $n$. Tameness placed exactly at dimension $n$ is the unique correct adjustment.

Why this definition and not a nearby variant? One could refine $L$ by separating out a **system of compositions** (a chosen weak composite per pasting diagram) and a **coherence** (the cells relating them) — this is Batanin's route and a variant of Leinster's; the resulting algebras agree, so the variation does not change the notion of weak $\omega$-category, only the presentation of the operad. One could also weaken the morphisms: the maps in $\mathbf{Wk\text{-}\omega\text{-}Cat}$ as defined preserve the $L$-structure *strictly*, which is admittedly a defect (there is as yet no satisfactory notion of *weak* $\omega$-functor or of equivalence of weak $\omega$-categories — Leinster flags this as the state of the art). But the *objects* — the weak $\omega$-categories themselves — are pinned down exactly by initiality plus contraction.

The test of the motivation: a reader who accepts "contraction = coherent tower of weak composites and coherences" and "we want the canonical such operad" should be able to deduce that the operad must be initial in $\mathbf{OC}$, that a weak $\omega$-category is therefore an $L$-algebra, and that the only adjustment needed to truncate to dimension $n$ is to force equalities in the top dimension via tameness.

---

# The Definition

> **The Batanin–Leinster operad.** The category $\mathbf{OC}$ of globular operads-with-contraction has an **initial object** (Leinster Prop. 9.2.2; see [[Thm - The Initial Contractible Globular Operad Exists]]), written $(L, \chi)$ and called the **Batanin–Leinster operad**. It is characterised up to unique isomorphism by: $L$ is a globular operad, $\chi$ is a contraction on it, and for every operad-with-contraction $(P, \chi')$ there is a *unique* contraction-preserving operad map $(L, \chi) \to (P, \chi')$.

> **Weak $\omega$-category.** A **weak $\omega$-category** is an **$L$-algebra**: a globular set $X$ equipped with an action of the Batanin–Leinster operad $L$ (equivalently, an [[Def - Algebra for a Monad|algebra]] for the induced monad $T_L$). The category of weak $\omega$-categories and ($L$-structure-preserving, strict) maps is $\mathbf{Wk\text{-}\omega\text{-}Cat} = \mathrm{Alg}(L)$.

> **Weak $n$-category.** For $n \in \mathbb{N}$, let $T^{(n)}$ be the free strict $n$-category monad on $n$-globular sets (it is cartesian, Leinster Thm F.2.1), and let $\mathbf{OC}_n$ be the category of $n$-globular operads equipped with a **contraction** — a precontraction on a **tame** map (see [[Def - Contraction on a Globular Operad]]). Then $\mathbf{OC}_n$ has an initial object $(L_n, \chi)$, and a **weak $n$-category** is an **$L_n$-algebra**: $\mathbf{Wk\text{-}n\text{-}Cat} = \mathrm{Alg}(L_n)$.

A weak $n$-category may equivalently be regarded as a weak $\omega$-category that is **trivial above dimension $n$** — all cells above dimension $n$ are identities, equivalently the $n$-truncation embeds $\mathbf{Wk\text{-}n\text{-}Cat}$ as a full subcategory of $\mathbf{Wk\text{-}\omega\text{-}Cat}$ on the structures supported in dimensions $\leq n$, with the top-dimensional tameness condition automatically met.

In low dimensions the definition reduces to the expected classical notions (Leinster Thm 9.4.1):
$$
\mathbf{Wk\text{-}0\text{-}Cat} \simeq \mathbf{Set}, \qquad \mathbf{Wk\text{-}1\text{-}Cat} \simeq \mathbf{Cat}, \qquad \mathbf{Wk\text{-}2\text{-}Cat} \simeq \mathbf{UBicat}_{str}.
$$
See [[Thm - Weak 2-Categories are Bicategories]].

---

# Categorical / Structural Definition

The structurally cleanest statement uses the universal property and the algebra construction together. The assignment $P \mapsto \mathrm{Alg}(P)$ from globular operads to categories is functorial: a globular-operad map $f : P \to P'$ induces a functor $f^\ast : \mathrm{Alg}(P') \to \mathrm{Alg}(P)$ (restrict the action along $f$). Now feed in the universal property of $L$. For *any* operad-with-contraction $(P, \chi')$ there is a unique map $(L, \chi) \to (P, \chi')$, hence a canonical functor
$$
\mathrm{Alg}(P) \longrightarrow \mathrm{Alg}(L) = \mathbf{Wk\text{-}\omega\text{-}Cat}.
$$

> Therefore: **any algebra for any operad-with-contraction is canonically a weak $\omega$-category.** This is the operational content of initiality — $L$-algebras are the universal recipients of all "weak-composition-and-coherence" structures.

Two instances of this functor pin the definition down at the extremes. Mapping $L \to 1$ (the unique map to the terminal, strict operad, which carries the trivial contraction) induces $\mathbf{Str\text{-}\omega\text{-}Cat} = \mathrm{Alg}(1) \to \mathbf{Wk\text{-}\omega\text{-}Cat}$, exhibiting **every strict $\omega$-category as a weak one** — and this functor is full and faithful, since contractibility of $L$ makes $L(\pi)$ non-empty for every $\pi$, so a strict map between strict $\omega$-categories is the same whether viewed strictly or weakly. At the other extreme, a **contractible globular set** $X$ (one for which $X \to 1$ is contractible) acquires a weak $\omega$-category structure: its endomorphism operad $\mathrm{End}(X)$ inherits a contraction, the unique map $L \to \mathrm{End}(X)$ is an $L$-algebra structure, and so $X$ is canonically a weak $\omega$-category. This is the directed analogue of "a contractible space is an $\infty$-groupoid", and it is how Leinster constructs his examples.

The structural reading of truncation is via the **forgetful/truncation adjunction** between $n$-globular sets and $\omega$-globular sets. The free strict $n$-category monad $T^{(n)}$ is the $n$-truncation of $T$, the category $\mathbf{OC}_n$ is the $n$-truncated version of $\mathbf{OC}$, and $L_n$ is the image of the initial-object construction in $n$ dimensions. The single structural difference is that the top-dimensional pairing $(s,t) : L_n(\pi) \to \mathrm{Par}_{L_n}(\pi)$ must be a *bijection* (tameness) rather than merely a surjection — which forces $L_n(\pi)$ in top dimension to be *exactly* the set of parallel pairs below, making $L_n$ entirely determined by its $(n-1)$-dimensional part. This is the precise categorical content of "coherence in the top dimension becomes equality".

---

# Relate to Other Fields / Compression

The Batanin–Leinster definition is one entry in the larger landscape of definitions of weak $n$-category, and placing it there is the most compressive way to remember it. The definitions split into two families. The **algebraic** ones — Batanin, Leinster, **Penon weak ω-category**, Trimble — make composition *given structure*: there is a chosen operad (or operad-like gadget) of operations, and an algebra performs them; the present definition is the cleanest algebraic one. The **non-algebraic / geometric** ones — [[Def - Quasi-Category|quasi-categories]], Segal categories, complete Segal spaces, Tamsamani–Simpson $n$-categories — make composition a *property*, defined only up to contractible choice via filler conditions on a simplicial-type object. The contraction here is the algebraic mirror of the geometric "fillers exist": where a [[Def - Kan Complex and the Nerve|Kan complex]] *has* fillers, the operad $L$ *chooses* them.

**True name:** *a weak $\omega$-category is "a globular set in which every pasteable diagram can be composed in coherently-many ways" — an $L$-algebra — and a weak $n$-category is the same with all coherences above dimension $n$ collapsed to equalities.* Operationally, never reason from the formal $L$-action; reason from "I can compose anything, the composites are associative-and-unital up to coherent isomorphism, and in an $n$-category the top-dimensional coherences are honest equations." The strict case is the special case where the composites are unique and the coherences are identities.

The deepest compression is the **homotopy hypothesis** corner. Restricting to *invertible* cells, weak $\omega$-groupoids should be equivalent to topological spaces / homotopy types — this is Grothendieck's homotopy hypothesis, and the Grothendieck–Maltsiniotis definition via **coherators** is a close relative of the operad-with-contraction here. The fact that a contractible globular set is a weak $\omega$-category is the algebraic shadow of "a contractible space is an $\infty$-groupoid". This positions the entire definition as the directed, algebraic answer to "what is the combinatorial structure of a space?".

---

# Examples / Corollaries

**Is an instance — every strict $\omega$-category.** Via the full and faithful functor $\mathbf{Str\text{-}\omega\text{-}Cat} \to \mathbf{Wk\text{-}\omega\text{-}Cat}$ induced by $L \to 1$, every strict $\omega$-category is a weak one. Concretely, an $L$-algebra structure can always be obtained from a strict-composition structure by composing strictly and taking every coherence cell to be an identity. Strict $\omega$-categories are exactly the weak ones in which all the coherence cells happen to be identities.

**Is an instance — a contractible globular set as a weak $\omega$-groupoid.** Any contractible globular set $X$ (every parallel pair of $n$-cells is joined by an $(n+1)$-cell) is canonically a weak $\omega$-category, in fact a weak $\omega$-*groupoid*, because all its cells are invertible up to higher cells. This is the algebraic version of a contractible space, and it is the base case from which the homotopy-hypothesis examples are built.

**Is an instance — a bicategory as a weak $2$-category.** By Leinster's Theorem 9.4.1, $\mathbf{Wk\text{-}2\text{-}Cat} \simeq \mathbf{UBicat}_{str}$, and unbiased bicategories are essentially the same as classical [[Def - 2-Category and Bicategory|bicategories]] (by the biased-equals-unbiased coherence results). So the monoidal categories, the bicategory of categories-functors-natural-transformations, and the fundamental $2$-groupoid of a space are all weak $2$-categories in this sense. See [[Thm - Weak 2-Categories are Bicategories]].

**Is NOT an instance — a globular set with composites but no coherence.** A globular set equipped with chosen binary composites of $1$-cells and $2$-cells but *no associator or interchange cells* is not a weak $\omega$-category: it is not an $L$-algebra, because $L$ contains coherence operations (associators, interchangers) that the structure cannot interpret. Having composites is necessary but radically insufficient; the coherence cells, supplied by the contraction, are the substance.

**Is NOT an instance — a "weak $3$-category" carrying spurious distinct parallel top cells.** A candidate weak $3$-category in which two parallel $3$-cells with the same source, target, and image are nonetheless declared distinct violates **tameness** at the top dimension and is *not* a weak $3$-category in the Batanin–Leinster sense. The tameness condition forces such pairs to be equal; without it one obtains a precontractible but non-contractible structure, which is a different (and worse-behaved) object.

**Calibration check.** Verify that the strict $\omega$-categories sit inside the weak ones as exactly those with identity coherence cells, by examining the functor induced by $L \to 1$. Confirm that a weak $1$-category is an ordinary category by tracing the equivalence $\mathbf{Wk\text{-}1\text{-}Cat} \simeq \mathbf{Cat}$ (the initial $1$-operad-with-contraction is the terminal $1$-operad, whose algebras are categories). Finally, explain in one sentence why a weak $n$-category needs tameness in dimension $n$ but a weak $\omega$-category needs no such condition anywhere — if you can, you have understood the one subtlety in the definition.

---

# Unlocked by This

> [!tip] The Comparison Problem and the Homotopy Hypothesis *(from Higher Category Theory)*
> With a definition of weak $\omega$-category in hand, the central open problems become comparisons: are the algebraic (Batanin, Leinster, **Penon**) and geometric ([[Def - Quasi-Category|quasi-category]], Segal-space) definitions equivalent? For $(\infty,1)$-categories the **Bergner–Joyal–Lurie** comparison answers yes; for general weak $\omega$-categories it is largely open. Restricting to groupoids gives the **homotopy hypothesis**: weak $\omega$-groupoids $\simeq$ homotopy types.

> [!tip] Weak ∞-Functors and Equivalences *(state of the art)*
> The maps in $\mathbf{Wk\text{-}\omega\text{-}Cat}$ as defined are *strict*. A satisfactory notion of **weak $\omega$-functor** and of **equivalence of weak $\omega$-categories** is not yet part of the theory — a genuine gap. Progress on this is one of the active frontiers, tied to the use of **coherators** and to model-categorical presentations of $\omega$-categories.

> [!tip] Derived and Higher Algebra *(from Homological Algebra)*
> Weak higher categories are the natural home for **derived categories**, **abelian categories** with their derived functors, and **stable $\infty$-categories**: the coherence data a contraction supplies is exactly what is needed to make "composition of chain maps up to homotopy, up to homotopy of homotopies, ..." into an honest categorical structure. The operadic definition is one route into this machinery; the model-categorical and quasi-categorical routes are the others.
