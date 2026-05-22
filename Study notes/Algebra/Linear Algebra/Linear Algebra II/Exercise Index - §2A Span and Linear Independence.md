---
type: exercise-index
subject: linear-algebra
section: "2A"
tags: [algebra, linear-algebra]
---

## §2A Span and Linear Independence — Exercises

The exercises of §2A drill the two fundamental operations on lists of vectors: forming a span (the smallest subspace containing the list) and verifying linear independence (uniqueness of expansion of the zero vector). The technical heart is the **linear dependence lemma** — if a list is dependent, some vector is in the span of its predecessors, and that vector can be removed without changing the span. This lemma is the engine of the chapter's structural theorems (the length inequality 2.22, the reduction 2.30) and the diagnostic tool for identifying redundancy. Almost every concrete problem in this section is solved by left-to-right testing of vectors against partial spans, equivalent in matrix form to Gaussian elimination.

- [[Ex - Constructing a basis from a spanning list]] (⭐) — applies the reduction algorithm of [[Thm - Every Spanning List Contains a Basis|LADR 2.30]] to the list $(1, 2), (3, 6), (4, 7), (5, 9)$ in $F^2$; produces the basis $(1, 2), (4, 7)$ ([[Def - Linear Combination and Span]], [[Def - Linear Independence]], [[Def - Basis]], [[Thm - Every Spanning List Contains a Basis]]).
- [[Ex - Removing redundancy from a linearly dependent list]] (⭐) — given a 4-vector list in $\mathbb{R}^3$ (known dependent), finds the smallest $k$ such that $v_k$ is in the span of its predecessors, with explicit relation $v_3 = 3 v_1 + 2 v_2$ ([[Def - Linear Combination and Span]], [[Def - Linear Independence]], [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List]]).
- [[Ex - Polynomials of degree at most n form a basis]] (⭐) — verifies $1, z, z^2, \ldots, z^n$ is a basis of $\mathcal{P}_n(F)$, exhibiting both spanning (immediate from the definition) and independence (from the "polynomial with infinitely many roots is zero" fact); this is the canonical basis used throughout polynomial linear algebra ([[Def - Basis]], [[Def - Linear Independence]], [[Def - Linear Combination and Span]]).
