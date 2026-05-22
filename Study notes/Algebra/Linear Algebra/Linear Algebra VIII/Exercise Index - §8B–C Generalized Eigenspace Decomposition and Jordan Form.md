---
type: exercise-index
subject: linear-algebra
section: "8B-8C"
tags: [algebra, linear-algebra]
---

## §8B–C Generalized Eigenspace Decomposition and Jordan Form — Exercises

Sections 8B and 8C are the structural heart of the chapter: the generalized eigenspace decomposition (8B) and the Jordan form (8C). The exercises in this combined index drill the two main skills the structural theorems unlock: (i) distinguishing operators with the same characteristic polynomial but different Jordan forms — i.e., recognising that the characteristic polynomial is not a complete similarity invariant; (ii) extracting structural and divisibility constraints on the operator's minimal polynomial and similar invariants. The thread connecting these is the principle that the Jordan form is the *complete* similarity invariant on a complex space, finer than the characteristic polynomial alone, and that the relationship between $T$ and polynomials in $T$ is governed by the ideal-theoretic structure of $\mathbb{C}[x]$.

- [[Ex - Operators with the same characteristic polynomial need not have the same Jordan form]] (⭐⭐) — exhibits two operators on $\mathbb{C}^4$ with $p_T(z) = (z - 1)(z - 5)^3$ but block partitions $(3)$ vs $(1, 1, 1)$ at $\lambda = 5$, hence different Jordan forms ([[Def - Jordan Basis and Jordan Form]], [[Def - Algebraic and Geometric Multiplicity]], [[Def - Minimal Polynomial]]).

- [[Ex - Minimal polynomial divides any polynomial that kills the operator]] (⭐⭐) — uses the division algorithm in $\mathbb{C}[x]$ to show $m_T \mid q$ for any $q$ with $q(T) = 0$; applies to the characteristic polynomial via Cayley–Hamilton ([[Def - Minimal Polynomial]], [[Def - Polynomial of an Operator]], [[Thm - Division Algorithm for Polynomials (LA)]]).

- [[Ex - Jordan form of a 3x3 nilpotent matrix]] (⭐⭐) — explicit Jordan-basis construction for a nilpotent operator, the nilpotent-case heart of [[Thm - Existence of Jordan Form]] ([[Def - Nilpotent Operator]], [[Def - Jordan Basis and Jordan Form]], [[Thm - Existence of Jordan Form]]).

The section's recurring move is "decompose into generalized eigenspaces, work block-by-block, read off the Jordan structure from null-space dimensions". The recurring trigger is "two operators with the same algebraic data — characteristic polynomial, minimal polynomial — that are nevertheless not similar": this is the prototypical failure mode that motivates the full Jordan form as the *complete* invariant. Students returning to this section should re-derive the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] (the headline theorem of 8B) and the construction of a Jordan basis for a nilpotent operator (the heart of 8C).
