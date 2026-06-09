---
type: exercise-index
subject: commutative-algebra
section: "2.2"
tags: [algebra, commutative-algebra]
---

## §2.2 Algebras and Hilbert's Basis Theorem — Exercises

The exercises of §2.2 drill the distinction between finitely generated *algebras* and finitely generated *modules*, the reach and the limits of Hilbert's basis theorem, and the additivity of length. The recurring technique is a *degree* argument: the gap between algebra and module generation is unbounded degree, the failure of subalgebras to be Noetherian is degree confinement of generators, the lower bound on generators of a monomial ideal is a degree-stripped dimension count, and the additivity of length is a telescoping of short exact sequences. The cautionary exercise — a non-Noetherian subalgebra of a Noetherian ring — sharpens the precise hypothesis Hilbert requires (finite generation as an algebra), which subalgebras can lack.

- [[Ex - A finitely generated algebra need not be a finitely generated module]] (⭐) — prove $k[T_1, \dots, T_n]$ is a finitely generated $k$-algebra (by the variables) but not a finitely generated $k$-module (infinite-dimensional), via the degree bound that $k$-linear combinations cannot exceed the maximum degree present while algebra multiplication reaches every degree; the canonical separation, closing only under integrality of the generators ([[Def - Finitely Generated Algebra]], [[Def - Algebra over a Ring (R-algebra)]], [[Def - Finitely Generated Module]], [[Def - Polynomial Ring]]).

- [[Ex - A subalgebra of a Noetherian algebra need not be Noetherian]] (⭐⭐⭐) — show the subalgebra $k[T_1 T_2, T_1 T_2^2, \dots] \subseteq k[T_1, T_2]$ is not Noetherian, by grading with $T_1$-degree to prove the chain of ideals $(u_1) \subsetneq (u_1, u_2) \subsetneq \cdots$ is strict (generators live in degree $1$, products escape to higher degree, so the bottom layer cannot be finitely generated); the counterexample showing Hilbert needs the algebra finitely generated ([[Def - Finitely Generated Algebra]], [[Def - Noetherian Ring]], [[Thm - Hilbert's Basis Theorem (Algebra Form)]], [[Def - Noetherian and Artinian Module]]).

- [[Ex - Unboundedly many generators in k of X and Y]] (⭐⭐) — prove the monomial ideal $\mathfrak{a}_n = (X^iY^{n-i})$ of $k[X,Y]$ needs $\geq n+1$ generators, by passing to $\mathfrak{a}_n/\mathfrak{m}\mathfrak{a}_n$ (a Nakayama-style minimal-generator count), identifying it with the $(n+1)$-dimensional degree-$n$ part, and noting any generating set must span it; Noetherian gives finiteness but never a uniform bound ([[Def - Ideal]], [[Def - Polynomial Ring]], [[Def - Noetherian Ring]], [[Thm - Hilbert's Basis Theorem (Algebra Form)]]).

- [[Ex - Composition length is additive on exact sequences]] (⭐⭐) — prove that any additive invariant $\lambda$ (in particular length) satisfies $\sum_{i=0}^n (-1)^i \lambda(M_i) = 0$ along a finite exact sequence, by cutting at the images $Z_i = \ker(M_i \to M_{i+1})$ into short exact sequences and telescoping with signs; the prototype Euler-characteristic identity and the seed of the Grothendieck group ([[Def - Composition Series and Length]], [[Def - Exact Sequence and Short Exact Sequence]], [[Thm - Length is Additive and Finite iff Noetherian and Artinian]]).
