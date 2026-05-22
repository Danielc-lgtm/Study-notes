---
type: exercise-index
subject: linear-algebra
section: "3A"
tags: [algebra, linear-algebra]
---

## §3A The Vector Space of Linear Maps — Exercises

This section introduces the basic notion of a [[Def - Linear Map|linear map]] and the structure of $\mathcal{L}(V, W)$ as a vector space under pointwise operations. The exercises drill three skills. *First*, recognising when a function is linear and when it is not, via the two axioms. *Second*, exploiting the vector-space structure of $\mathcal{L}(V, W)$ — building new linear maps from old by sums, scalar multiples, and composition — and recognising properties that fail to be closed under sum (injectivity, surjectivity, invertibility). *Third*, using the operational form of linearity, $T(\sum \lambda_k v_k) = \sum \lambda_k Tv_k$, which is the workhorse of every later computation. The themes converge on the **[[Thm - Linear Map Determined by Action on Basis|linear-map lemma]]**: a linear map is finite data once a basis is chosen.

- [[Ex - A linear map from R to R is multiplication by a scalar]] (⭐) — every linear map on a one-dimensional space is a scalar multiplication; uses the operational form of linearity ([[Def - Linear Map]]).
- [[Ex - Sum of injective linear maps need not be injective]] (⭐) — properties of linear maps that fail to be preserved under sum; uses the negation trick $(I, -I) \mapsto 0$ ([[Def - Linear Map]], [[Def - Null Space and Range]]).
- [[Ex - Linear maps preserve linear combinations]] (⭐) — induction on the number of summands; converts the two axioms (additivity, homogeneity) into the operational form $T(\sum \lambda_k v_k) = \sum \lambda_k Tv_k$ ([[Def - Linear Map]]).
