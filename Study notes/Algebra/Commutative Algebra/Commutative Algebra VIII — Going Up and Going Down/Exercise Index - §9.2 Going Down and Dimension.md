---
type: exercise-index
subject: commutative-algebra
section: "9.2"
tags: [algebra, commutative-algebra]
---

## §9.2 Going Down and Dimension — Exercises

The exercises of §9.2 drill the *downward* and *dimension* halves of the chapter. [[Thm - Going Down for Integrally Closed Domains|Going down]] is the one Cohen–Seidenberg theorem that can fail, and the headline exercise constructs an explicit failure on a non-normal base — the "two lines glued at a point" — to show that normality is genuinely needed. The dimension exercise assembles lying over, going up, and incomparability into $\dim A = \dim B$ (notably without going down), then uses Noether normalization to compute $\dim k[X_1,\dots,X_n] = n$ and the dimension formula $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$ (ES4 Q3). The unifying technique is chain manipulation: lifting chains up (going up), contracting them without collapse (incomparability), and lifting them down (going down, when normal).

- [[Ex - Going down can fail without normality]] (⭐⭐⭐) — construct an integral extension $A \subseteq B = k[u]\times k[v]$ with $A$ the non-normal subring $\{(f,g) : f(0)=g(0)\}$, and exhibit a chain $\mathfrak{p}_2 \subsetneq \mathfrak{p}_1$ and prime $\mathfrak{q}_1$ over $\mathfrak{p}_1$ with no $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ over $\mathfrak{p}_2$; the sharpness witness for the going-down theorem ([[Thm - Going Down for Integrally Closed Domains]], [[Def - Integral Closure and Normal Domain]], [[Def - Lying Over, Going Up, Going Down]], [[Def - The Induced Map on Spectra]], [[Def - Prime and Maximal Ideal]]).

- [[Ex - Dimension is preserved under integral extension]] (⭐⭐) — prove $\dim A = \dim B$ for an integral extension by the two-sided chain argument (lift up via lying over and going up for $\dim A \leq \dim B$; contract via incomparability for $\dim B \leq \dim A$), then deduce $\dim k[X_1,\dots,X_n] = n$ and $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$ ([[Thm - Integral Extensions Preserve Dimension]], [[Thm - Lying Over]], [[Thm - Going Up]], [[Thm - Incomparability]], [[Thm - Going Down for Integrally Closed Domains]], [[Def - Krull Dimension and Height]]).

- [[Ex - A chain of primes lifts along a finite extension]] (⭐⭐) — lift a strict chain together with a prime over its bottom to a strict chain upstairs by iterating going up with incomparability for strictness; the chain-lifting half of dimension preservation, shared with §9.1 ([[Thm - Going Up]], [[Thm - Lying Over]], [[Thm - Incomparability]], [[Def - Krull Dimension and Height]]).
