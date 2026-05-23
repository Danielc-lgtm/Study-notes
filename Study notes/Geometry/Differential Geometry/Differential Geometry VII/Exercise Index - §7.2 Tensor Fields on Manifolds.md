---
type: exercise-index
subject: differential-geometry
section: "7.2"
tags: [geometry, differential-geometry, tensor-fields]
---

## §7.2 Tensor Fields on Manifolds — Exercises

This section drills the manifold-level extension of fibre-level multilinear algebra. The exercises focus on **computing tensor fields in charts** (especially under coordinate changes), the **transformation rule** for components, and the **pullback computation recipe** (substitute coordinates, expand differentials). The metric-in-polar-coordinates exercise is the canonical worked example: it shows how the *same* geometric object (the Euclidean metric) has different component matrices in different charts, with the polar components $g_{rr} = 1, g_{\theta\theta} = r^2, g_{r\theta} = 0$ reproducing the familiar line element $ds^2 = dr^2 + r^2 d\theta^2$.

- [[Ex - Computing the Pullback of a Tensor Field in Coordinates]] (⭐⭐) — apply the naturality identities ($F^* \otimes = \otimes F^*$, $F^*(fA) = (f \circ F)F^*A$) and the chain rule to compute the pullback of $x^2\, dy \otimes dy$ under the polar map ([[Def - Pullback of a Covariant Tensor Field]], [[Thm - Pullback Commutes with Tensor Product]]).

- [[Ex - The Metric Tensor in Polar Coordinates]] (⭐⭐) — the canonical worked example: pull back the Euclidean metric via the polar-coordinate map; obtain $g = dr \otimes dr + r^2\, d\theta \otimes d\theta$; verify via the transformation rule ([[Def - Pullback of a Covariant Tensor Field]], [[Thm - Pullback Commutes with Tensor Product]], [[Thm - Transformation Rule for Tensor Components]]).

- [[Ex - The Kronecker Delta as a Mixed Tensor]] (⭐) — also relevant here as the prototype of a tensor field with chart-independent components, and as an example of the transformation rule's cancellation of Jacobian factors for the identity-as-$(1,1)$-tensor ([[Def - Tensor Field on a Manifold]], [[Thm - Transformation Rule for Tensor Components]]).
