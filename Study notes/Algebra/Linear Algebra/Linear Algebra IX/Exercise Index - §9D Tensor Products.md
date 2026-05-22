---
type: exercise-index
subject: linear-algebra
section: "9D"
tags: [algebra, linear-algebra]
---

## §9D Tensor Products — Exercises

The exercises of §9D drill the universal-property pattern: to construct a linear map on a tensor product, always construct a bilinear map on the Cartesian product and let the universal property do the lifting. This is the most important single technique in §9D, and it is what makes tensor products useful across algebra, geometry, and physics. The master pattern is "bilinear data $\Rightarrow$ linear data via $V \otimes W$", with the universal property as the rigorous formulation.

- [[Ex - Tensor product of two copies of F^2 has dimension 4]] (⭐) — compute $\dim(V \otimes V) = 4$ for $V = \mathbb{F}^2$, exhibit a basis $\{e_i \otimes e_j\}$, identify $V \otimes V \cong M_2(\mathbb{F})$ via the outer product $u \otimes v \mapsto u v^t$, and show that $e_1 \otimes e_1 + e_2 \otimes e_2$ is **not** an elementary tensor (it corresponds to the identity matrix, which has rank 2; elementary tensors are rank-one matrices). The exercise establishes the matrix model of $V \otimes V$ and the rank obstruction to factorability ([[Def - Tensor Product of Vector Spaces]], [[Thm - Universal Property of the Tensor Product]])

- [[Thm - Universal Property of the Tensor Product]] — the headline theorem of §9D, with proof via "define on a basis and verify it gives the right answer on elementary tensors via bilinearity". The natural isomorphism $\mathcal{B}(V, W; U) \cong \mathcal{L}(V \otimes W, U)$ is the canonical formulation.

- **Associativity exercise (⭐⭐).** Show that $(U \otimes V) \otimes W \cong U \otimes (V \otimes W)$ canonically as vector spaces. *Technique drilled:* the universal property as a definition — both sides have the same universal property for trilinear maps out of $U \times V \times W$, hence are canonically isomorphic. Uses [[Def - Tensor Product of Vector Spaces]], [[Thm - Universal Property of the Tensor Product]].

- **Trace as a tensor functional exercise (⭐⭐).** Show that the trace $\operatorname{tr} : \mathcal{L}(V) \to \mathbb{F}$ is the canonical "contraction" $V^* \otimes V \to \mathbb{F}$ (under the identification $V^* \otimes V \cong \mathcal{L}(V)$), sending $\varphi \otimes v$ to $\varphi(v)$. *Technique drilled:* using the universal property to convert the bilinear evaluation pairing into a linear functional. Uses [[Def - Tensor Product of Vector Spaces]], [[Thm - Universal Property of the Tensor Product]], [[Def - Dual Space]].
