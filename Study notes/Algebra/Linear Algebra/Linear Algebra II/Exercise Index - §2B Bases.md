---
type: exercise-index
subject: linear-algebra
section: "2B"
tags: [algebra, linear-algebra]
---

## §2B Bases — Exercises

The exercises of §2B drill the construction of bases by the two structural operations — **reducing** a spanning list ([[Thm - Every Spanning List Contains a Basis|2.30]]) and **extending** an independent list ([[Thm - Every Linearly Independent List Extends to a Basis|2.32]]) — and the use of the resulting bases to compute dimensions and to set up direct-sum decompositions. The defining property of a basis is **unique expansion**: every vector has exactly one coefficient tuple, which installs coordinates on the space. The corollary "every finite-dimensional space has a basis" is what makes the chapter's whole apparatus computational; the corollary "every subspace has a direct-sum complement" (2.33) is what makes finite-dimensional algebra structurally clean.

- [[Ex - Polynomials of degree at most n form a basis]] (⭐) — verifies $1, z, z^2, \ldots, z^n$ is a basis of $\mathcal{P}_n(F)$; the canonical polynomial-space basis. Also appears in §2A as a foundational example ([[Def - Basis]], [[Def - Linear Independence]], [[Def - Linear Combination and Span]]).
- [[Ex - Sum of dimensions in direct sum]] (⭐⭐) — given $V = U \oplus W$ with bases of $U$ and $W$, proves that the concatenated list is a basis of $V$, giving $\dim V = \dim U + \dim W$. The structural construction of bases of direct sums ([[Def - Basis]], [[Def - Direct Sum]], [[Def - Dimension]], [[Thm - Dimension of a Sum of Subspaces]]).
- [[Ex - Constructing a basis from a spanning list]] (⭐) — applies the reduction of 2.30 to a redundant spanning list in $F^2$ to produce a basis. Also appears in §2A as the concrete realisation of 2.30. The dual of basis extension ([[Def - Linear Combination and Span]], [[Def - Basis]], [[Thm - Every Spanning List Contains a Basis]]).
