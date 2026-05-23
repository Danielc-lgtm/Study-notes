---
type: exercise-index
subject: linear-algebra
section: "3B"
tags: [algebra, linear-algebra]
---

## §3B Null Spaces and Ranges — Exercises

This section is the heart of finite-dimensional linear algebra: the [[Def - Null Space and Range|null space and range]] of a linear map, and the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem]] $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$. The exercises drill three skills. *First*, applying rank–nullity to convert dimensional information from one form to another (kernel size to image size and back). *Second*, using the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] together with rank–nullity to construct linear maps with prescribed null space and range — the canonical "build a map with property P" pattern. *Third*, deriving rank inequalities for compositions and other constructed maps from the basic structural fact that "the image of a [[Def - Subspace|subspace]] under a linear map has [[Def - Dimension|dimension]] at most that of the [[Def - Subspace|subspace]]". The themes converge on the **rank–nullity theorem** as the central conservation law.

- [[Ex - Rank of a product is bounded by individual ranks]] (⭐⭐) — rank of a composition is bounded by the rank of each factor; uses two applications of rank–nullity ([[Def - Rank of a Linear Map]], [[Def - Null Space and Range]], [[Thm - Fundamental Theorem of Linear Maps]]).
- [[Ex - Null space and range of a projection]] (⭐⭐) — for an idempotent $P^2 = P$, the null space and range decompose $V$ as a direct sum; uses the identity $v = (v - Pv) + Pv$ ([[Def - Null Space and Range]], [[Thm - Fundamental Theorem of Linear Maps]]).
- [[Ex - Existence of a linear map with prescribed null space and range]] (⭐⭐) — the necessary-and-sufficient dimensional condition $\dim X + \dim Y = \dim V$; uses the linear-map lemma to construct with the right basis adaptation ([[Thm - Fundamental Theorem of Linear Maps]], [[Thm - Linear Map Determined by Action on Basis]], [[Def - Null Space and Range]]).
