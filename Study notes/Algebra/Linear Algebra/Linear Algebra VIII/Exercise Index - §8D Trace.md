---
type: exercise-index
subject: linear-algebra
section: "8D"
tags: [algebra, linear-algebra]
---

## §8D Trace — Exercises

Section 8D introduces the trace as the simplest similarity invariant — basis-independent, linear, cyclic. The exercises drill two foundational skills: (i) extracting eigenvalue information from a matrix without diagonalising, by exploiting the trace identity $\operatorname{tr} T = \sum d_k \lambda_k$; (ii) using the algebraic structure of the trace (linearity, cyclicity) to prove operator-theoretic statements like "the identity is not a commutator". The trace will recur in [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] as the negative of the next-to-leading coefficient of the characteristic polynomial, and in [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] as the foundation of the Hilbert–Schmidt inner product on operators.

- [[Ex - Trace is basis-independent and equals tr of any matrix]] (⭐) — establishes the cyclic property $\operatorname{tr}(AB) = \operatorname{tr}(BA)$, deduces conjugation-invariance, deduces basis-independence of the operator trace, verifies linearity and $\operatorname{tr}(I) = \dim V$ ([[Def - Trace]], [[Def - Change of Basis Matrix]], [[Def - Matrix of a Linear Map]]).

- [[Ex - Sum of algebraic multiplicities equals dimension]] (⭐) — companion result: dimensions of generalized eigenspaces sum to $\dim V$. Combined with the trace identity, this gives $\operatorname{tr} T = \sum_k d_k \lambda_k$ ([[Def - Algebraic and Geometric Multiplicity]], [[Thm - Generalized Eigenspace Decomposition]]).

- [[Ex - Operators with the same characteristic polynomial need not have the same Jordan form]] (⭐⭐) — uses trace and other invariants to distinguish operators; demonstrates that trace alone (or trace + determinant) is insufficient to determine similarity, while the full Jordan form is ([[Def - Trace]], [[Def - Jordan Basis and Jordan Form]], [[Thm - Trace Equals Sum of Eigenvalues]]).

The section's recurring move is "compute the trace from any matrix, equate with the sum of eigenvalues with multiplicity". The recurring trigger is "extract an unknown eigenvalue when most are known": *e.g.* the partition $\operatorname{tr} T = $ sum yields one missing eigenvalue when two of three are given. Students returning to the section should re-derive the cyclic property of the trace (the master identity for all consequences) and the spectral identity $\operatorname{tr} T = \sum d_k \lambda_k$ via the upper-triangular form.
