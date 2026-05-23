---
type: exercise-index
subject: linear-algebra
section: "3C"
tags: [algebra, linear-algebra]
---

## §3C Matrices — Exercises

This section introduces the [[Def - Matrix of a Linear Map|matrix representation]] of a linear map and the operations of [[Def - Matrix Multiplication|matrix addition and multiplication]] that make the matrix isomorphism $\mathcal{L}(V, W) \cong \mathbf{F}^{m, n}$ a structure-preserving identification. The exercises drill three skills. *First*, verifying that the matrix-of-a-linear-map assignment respects the vector-space operations (sum, scalar multiplication) — establishing that $\mathcal{M}$ is itself a linear map. *Second*, computing the [[Def - Dimension|dimension]] of $\mathcal{L}(V, W)$ via the matrix isomorphism, and exhibiting an explicit basis of $\mathcal{L}(V, W)$ via matrix units. *Third*, using matrix multiplication as the operational shadow of composition, including the corollary rank inequality $\operatorname{rank}(AB) \leq \min\{\operatorname{rank} A, \operatorname{rank} B\}$. The themes converge on the **[[Def - Dimension|dimension]] formula** $\dim \mathcal{L}(V, W) = mn$, the simplest non-trivial application of the matrix isomorphism.

- [[Ex - Matrix of a sum of linear maps is the sum of matrices]] (⭐) — additivity and homogeneity of the matrix-of-a-linear-map assignment; computes entries directly to verify ([[Def - Matrix of a Linear Map]], [[Def - Linear Map]]).
- [[Ex - The space of linear maps has dimension mn]] (⭐⭐) — establishes $\dim \mathcal{L}(V, W) = mn$ via the matrix isomorphism; uses the linear-map lemma for surjectivity ([[Def - Matrix of a Linear Map]], [[Thm - Linear Map Determined by Action on Basis]], [[Thm - Two Vector Spaces Isomorphic iff Same Dimension]]).
- [[Ex - Rank of a product is bounded by individual ranks]] (⭐⭐) — rank inequality for matrix and operator products; uses rank–nullity applied to the restriction $S|_{\operatorname{range} T}$ ([[Def - Rank of a Linear Map]], [[Def - Matrix Multiplication]], [[Thm - Fundamental Theorem of Linear Maps]]).
