---
type: exercise-index
subject: commutative-algebra
section: "5.2"
tags: [algebra, commutative-algebra]
---

## §5.2 Nakayama and Minimal Generators — Exercises

The exercises of §5.2 drill the everyday use of [[Thm - Nakayama's Lemma|Nakayama's lemma]]: the residue-field reduction $M \rightsquigarrow M/𝔪M$ and the lifting of conclusions back to the module. The unifying technique is the three-step pattern that runs the whole subject — *reduce modulo 𝔪 to land in a $k$-vector space, solve the linear-algebra question there, lift with Nakayama* — applied to generation (a spanning set lifts to a generating set), to counting (the minimal number of generators is a residue-field dimension), and to vanishing (a tensor product vanishes already at the residue field). The geometric payoff threaded through these is the **cotangent space** $𝔪/𝔪²$ and the **embedding dimension** $\dim_k 𝔪/𝔪²$, the first algebraic invariant of a point that detects smoothness. Each exercise turns an intractable module statement into a finite computation over the field $k = R/𝔪$.

- [[Ex - Generators lifting from M over mM]] (⭐) — lift a spanning set of $M/𝔪M$ to a generating set of $M$ over a local ring, by naming the submodule $N$ they generate and recognising the spanning hypothesis as $𝔪M + N = M$, then applying the submodule form of Nakayama; the clean prototype of "reduce and lift" ([[Thm - Nakayama's Lemma]], [[Thm - Generators Modulo the Maximal Ideal]], [[Def - Local Ring and Residue Field]], [[Def - Finitely Generated Module]], [[Def - Submodule]]).

- [[Ex - Minimal generators of the maximal ideal and the cotangent space]] (⭐⭐) — apply the generator-lifting theorem to the module $M = 𝔪$ itself (so $𝔪M = 𝔪²$ and the reduction is the cotangent space $𝔪/𝔪²$), proving generators of $𝔪$ correspond to spanning sets of $𝔪/𝔪²$ and that the minimal number is $\dim_k 𝔪/𝔪²$, the embedding dimension ([[Thm - Generators Modulo the Maximal Ideal]], [[Thm - Nakayama's Lemma]], [[Def - Minimal Generating Set and the Cotangent Space]], [[Def - Noetherian Ring]], [[Def - Local Ring and Residue Field]]).

- [[Ex - Tensor of nonzero finitely generated modules over a local ring is nonzero]] (⭐⭐) — show $M ⊗_A N = 0 ⇒ M = 0$ or $N = 0$ over a local ring, by base-changing the equation to the residue field (so $M ⊗_A N$ becomes $(M/𝔪M) ⊗_k (N/𝔪N)$), settling it by dimension-counting over $k$, and lifting with Nakayama; the "reduce to the field, then lift" method in its purest form ([[Thm - Nakayama's Lemma]], [[Thm - Universal Property of the Tensor Product of Modules]], [[Def - Local Ring and Residue Field]], [[Def - Finitely Generated Module]]).
