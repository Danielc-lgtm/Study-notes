---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Hermitian Vector Bundle"
tags: [gauge-theory, frame-bundle, orthonormal, reduction]
---

# The Definition

> [!definition] Orthonormal frame bundle
> If $(E,h)$ is a rank-$r$ real Euclidean bundle, its **orthonormal frame bundle**
> $$O(E)_x=\operatorname{Iso}_{\mathrm{isom}}(\mathbb R^r,E_x)$$
> is a principal $O(r)$-subbundle of $\operatorname{Fr}(E)$. If $E$ is oriented, the positively oriented frames form the principal $SO(r)$-bundle $SO(E)$. For a Hermitian bundle, unitary frames form a principal $U(r)$-bundle $U(E)$.

# Why This Is a Bundle

Smooth Gram–Schmidt turns any local frame into a local orthonormal frame. Two orthonormal frames differ by a unique orthogonal or unitary matrix, so the relevant right action is free and transitive on every fibre. These local frames supply principal-bundle charts.

# Structural Meaning

The inclusions
$$O(E)\subset\operatorname{Fr}(E),\qquad U(E)\subset\operatorname{Fr}(E)$$
are reductions of structure group. Conversely, an $O(r)$-reduction defines a Euclidean metric by declaring every reduced frame to be an isometry; this is independent of frame because $O(r)$ preserves the standard inner product. Thus a metric and an orthogonal reduction are equivalent data. The same proof applies to Hermitian metrics and $U(r)$.

# Examples / Corollaries

For a Riemannian manifold $(B,g)$, $SO(TB)$ is the bundle on which the Levi–Civita principal connection lives. Spin structures later lift this $SO(r)$-bundle through $Spin(r)\to SO(r)$.
