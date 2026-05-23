---
type: exercise-index
subject: differential-geometry
section: "11.2"
tags: [geometry, differential-geometry, lie-groups]
---

## §11.2 The Lie Algebra of a Lie Group — Exercises

This section drills the [[Def - The Lie Algebra of a Lie Group|Lie algebra]] construction: identifying $\mathfrak{g} = T_e G$ as a vector space, computing the bracket via [[Def - Left-Invariant Vector Field|left-invariant vector fields]] or matrix commutators, and verifying that the construction is functorial. The exercises develop the universal technique of differentiating defining equations at the identity to extract the Lie subalgebra of a matrix Lie [[Def - Group|group]]. The most reusable technique drilled is: parametrize a curve $A(t) = I + tX + O(t^2)$ in $G$, substitute into the defining equation, expand to first order, read off the linear constraint on $X$.

- [[Ex - The Lie Algebra of SO(3) is Antisymmetric Matrices]] (⭐⭐) — differentiating $A^T A = I$ and $\det A = 1$ at $I$ to extract antisymmetry; identifies $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$ via the hat map ([[Def - The Lie Algebra of a Lie Group]], [[Thm - The Closed Subgroup Theorem]], [[Def - Lie Group]])
- [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]] (⭐⭐) — verifies that the abstract bracket on $\mathfrak{g}$ via left-invariant vector fields coincides with the matrix commutator $[A, B] = AB - BA$ for matrix Lie [[Def - Group|groups]] ([[Def - Left-Invariant Vector Field]], [[Def - The Lie Bracket of Vector Fields]], [[Def - The Lie Algebra of a Lie Group]])
- [[Ex - The Lie Algebra of GL(n,R) is the Space of n by n Matrices]] (⭐) — open-submanifold case; the ambient vector space is the Lie algebra with no constraint ([[Def - The Lie Algebra of a Lie Group]], [[Def - Lie Group]])
