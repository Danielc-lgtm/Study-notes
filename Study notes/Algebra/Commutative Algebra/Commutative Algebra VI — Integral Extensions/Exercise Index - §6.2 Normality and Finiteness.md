---
type: exercise-index
subject: commutative-algebra
section: "6.2"
tags: [algebra, commutative-algebra]
---

## §6.2 Normality and Finiteness — Exercises

The exercises of §6.2 drill the structural payoffs of integrality: the field/maximality criterion, the computation of normalizations, and the descent of finiteness through towers. Here you practise reading field-ness off a minimal integral equation (the inversion trick that powers Zariski's lemma and the Nullstellensatz), and the delicate finiteness-descent of the Artin–Tate lemma, where all three of a Noetherian base, finite-type-above, and module-finite-above are load-bearing. These problems connect the chapter to its downstream destinations — the going-up theory, Noether normalization, and the geometry of finite maps. The normalization computations of §6.1 ([[Ex - Z[sqrt 5] is not integrally closed]], [[Ex - The integral closure of k[t^2,t^3] resolves the cusp]]) also belong to the normality theme and are cross-referenced from here.

- [[Ex - An integral domain integral over a field is a field]] (⭐⭐) — prove a domain integral over a field $k$ is a field by inverting a minimal monic equation (domain forces nonzero constant term, field inverts it), with the counterexample $k \times k$ showing the domain hypothesis is necessary; the engine of Zariski's lemma (Atiyah–Macdonald 5.7) ([[Def - Integral Element and Integral Extension]], [[Def - Integral Domain]], [[Def - Unit and Field]], [[Thm - Integral Extensions and Fields (Domain Criterion)]]).

- [[Ex - The finiteness lemma for A in B in C]] (⭐⭐⭐) — the Artin–Tate lemma: with $A$ Noetherian, $C$ finite-type over $A$, $C$ finite over $B$, show $B$ is finite-type over $A$, by manufacturing a Noetherian intermediate ring $A'$ from the structure constants over which $C$ becomes module-finite, then trapping $B$ as a submodule (Example Sheet 3 Q4) ([[Def - Finite and Finite-Type Algebra]], [[Def - Noetherian Ring]], [[Thm - Characterizations of Integrality (Module-Finite Criterion)]], [[Thm - Transitivity of Integrality and Finiteness]], [[Thm - Hilbert's Basis Theorem]]).

- [[Ex - The integral closure of k[t^2,t^3] resolves the cusp]] (⭐⭐) — the cusp normalization $\overline{k[t^2,t^3]} = k[t]$, the geometric face of normality: non-normal coordinate ring $=$ singular curve, integral closure $=$ smooth model, with the finite birational map $t \mapsto (t^2, t^3)$ resolving the cusp ([[Def - Integral Closure and Normal Domain]], [[Thm - The Integral Closure is a Subring]], [[Thm - A UFD is Integrally Closed]], [[Def - Field of Fractions]]).
