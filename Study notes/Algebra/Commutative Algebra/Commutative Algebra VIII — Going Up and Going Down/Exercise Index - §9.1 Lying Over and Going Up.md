---
type: exercise-index
subject: commutative-algebra
section: "9.1"
tags: [algebra, commutative-algebra]
---

## §9.1 Lying Over and Going Up — Exercises

The exercises of §9.1 drill the *good behaviour of the contraction map* $\iota^* : \operatorname{Spec} B \to \operatorname{Spec} A$ for an integral extension: that it is surjective ([[Thm - Lying Over|lying over]]), that its fibres are antichains and (when module-finite) finite ([[Thm - Incomparability|incomparability]]), and that chains lift upward ([[Thm - Going Up|going up]]). The unifying technique is the fibre dictionary — the fibre over $\mathfrak{p}$ is $\operatorname{mSpec} B_{\mathfrak{p}}$, equivalently $\operatorname{Spec}$ of the fibre ring $B \otimes_A \kappa(\mathfrak{p})$ — which turns every geometric question about the fibre into the study of one explicit ring over a field. The prototype throughout is the branched cover $\operatorname{Spec}\mathbb{Z}[i] \to \operatorname{Spec}\mathbb{Z}$, where the fibre ring $\mathbb{F}_p[X]/(X^2+1)$ makes lying over and incomparability fully computable.

- [[Ex - Primes of Z[i] over a rational prime]] (⭐⭐) — compute the fibre of $\operatorname{Spec}\mathbb{Z}[i] \to \operatorname{Spec}\mathbb{Z}$ over each rational prime by reducing to the factorisation of $X^2+1$ in $\mathbb{F}_p$, getting ramified ($p=2$), split ($p\equiv 1 \bmod 4$), inert ($p\equiv 3 \bmod 4$); the model computation of a fibre via the fibre ring ([[Def - The Induced Map on Spectra]], [[Thm - Lying Over]], [[Thm - Incomparability]], [[Def - Gaussian Integers]], [[Def - Prime and Maximal Ideal]], [[Thm - Maximal and Prime Ideals via Quotients]]).

- [[Ex - The induced map on Spec is surjective for integral extensions]] (⭐⭐) — prove $\iota^*$ surjective by showing $B_{\mathfrak{p}} \neq 0$ and translating a maximal ideal of $B_{\mathfrak{p}}$ back to a prime over $\mathfrak{p}$, drilling the fibre-equals-$\operatorname{mSpec} B_{\mathfrak{p}}$ dictionary and the "localize to force a prime" move ([[Thm - Lying Over]], [[Def - The Induced Map on Spectra]], [[Def - Lying Over, Going Up, Going Down]], [[Thm - Prime Ideals of a Localization]], [[Thm - Integral Extensions and Fields (Domain Criterion)]], [[Def - Multiplicative Set and Localization]]).

- [[Ex - Fibres of a finite map are finite]] (⭐⭐) — show every fibre of a module-finite extension is finite by recognising the fibre ring $B \otimes_A \kappa(\mathfrak{p})$ as a finite-dimensional algebra over a field, hence Artinian, hence with finitely many primes — all maximal by incomparability ([[Thm - Incomparability]], [[Def - The Induced Map on Spectra]], [[Def - Local Ring and Residue Field]], [[Def - Finitely Generated Module]], [[Thm - Lying Over]]).

- [[Ex - A chain of primes lifts along a finite extension]] (⭐⭐) — lift a strict chain $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ together with a prime over $\mathfrak{p}_0$ to a strict chain in $\operatorname{Spec} B$ by iterating going up, with strictness from incomparability; the engine of $\dim A \leq \dim B$ ([[Thm - Going Up]], [[Thm - Lying Over]], [[Thm - Incomparability]], [[Def - Krull Dimension and Height]], [[Def - The Induced Map on Spectra]]).
