---
type: exercise-index
subject: linear-algebra
section: "1C"
tags: [algebra, linear-algebra]
---

## §1C Subspaces and Direct Sums — Exercises

LADR §1C introduces [[Def - Subspace|subspaces]] (subsets closed under the vector-space operations), sums of [[Def - Subspace|subspaces]], and direct sums (sums with unique decomposition). The section's exercises drill **verifying subspace closure**, **computing sums and intersections**, **certifying directness via [[Thm - Direct Sum of Two Subspaces]]** (the two-subspace pairwise-intersection criterion) and via [[Thm - Conditions for a Direct Sum]] (the zero-uniqueness criterion in general). The unifying frame is the **lattice structure on subspaces**: intersection is meet, sum is join, and direct sum is the canonical "join with uniqueness". A reader who internalizes the operations of this lattice, and when to upgrade from sum to direct sum, has mastered the structural skeleton of linear algebra at the subspace level.

- [[Ex - Sum of two subspaces is the smallest containing both]] (⭐) — universal-property characterization of the sum as the lattice-theoretic join in $\operatorname{Sub}(V)$; drills the standard "exhibit + absorb" template ([[Def - Subspace]], [[Def - Sum of Subspaces]]).
- [[Ex - Intersection of subspaces is a subspace]] (⭐) — arbitrary intersection of subspaces is a subspace; drills the universally-quantified closure pattern that generalizes to [[Def - Subgroup|subgroups]], [[Def - Submodule|submodules]], closed sets, $\sigma$-algebras ([[Def - Subspace]]).
- [[Ex - Union of subspaces is a subspace iff one contains the other]] (⭐⭐) — biconditional with contrapositive proof in the hard direction; demonstrates that the union is the *wrong* join in the subspace lattice and why sums are needed ([[Def - Subspace]], [[Def - Sum of Subspaces]]).
- [[Ex - Subspaces of F^2 are classified]] (⭐⭐) — classification of low-dimensional subspaces: $\{0\}$, lines through origin, all of $\mathbb{F}^2$; uses the determinant $ad - bc$ as the algebraic test for "two vectors span $\mathbb{F}^2$" ([[Def - Subspace]]).
- [[Ex - Even and odd functions form a direct sum decomposition]] (⭐⭐) — the involution-symmetrization decomposition $\mathbb{R}^\mathbb{R} = V_e \oplus V_o$; prototype of "decompose under an involution into $\pm 1$ eigenspaces" that recurs in symmetric/antisymmetric tensors, Hermitian/skew-Hermitian operators, real/imaginary parts ([[Def - Subspace]], [[Def - Direct Sum]], [[Thm - Direct Sum of Two Subspaces]]).
