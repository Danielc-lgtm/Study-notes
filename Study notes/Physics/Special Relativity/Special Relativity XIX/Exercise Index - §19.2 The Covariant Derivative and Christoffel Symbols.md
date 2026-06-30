---
type: exercise-index
subject: special-relativity
section: "19.2"
tags: [physics, special-relativity]
---

## §19.2 The Covariant Derivative and Christoffel Symbols — Exercises

The exercises of §19.2 are the computational and conceptual core of the chapter. The headline drill is computing Christoffel symbols from a metric via $\Gamma^\gamma{}_{\alpha\beta} = \tfrac12 g^{\gamma\mu}(\partial_\alpha g_{\mu\beta}+\partial_\beta g_{\alpha\mu}-\partial_\mu g_{\alpha\beta})$, exploiting diagonality and the lower-index symmetry to keep the bookkeeping short. Alongside it sit two calibration checks on the central claim that $\boldsymbol{\nabla}$, not $\partial$, is the geometrically correct derivative: that the metric is covariantly constant ($\boldsymbol{\nabla}g = 0$, trivial here because $g$ is constant, but the defining condition of the connection in general relativity), and that the divergence in curvilinear coordinates collapses to the determinant formula $\frac{1}{\sqrt{-\det g}}\partial_\mu(\sqrt{-\det g}\,v^\mu)$, with constant-component fields nevertheless having nonzero divergence and constant fields in curvilinear clothes having zero. The capstone connects the Christoffel symbols to physics: in rotating coordinates they *are* the centrifugal and Coriolis forces, fictitious because the curvature is zero — the flat-space rehearsal for gravity. Throughout, the unifying discipline is separating geometry (the tensors, the curvature) from coordinate artefact (the nonzero Christoffels of curvilinear coordinates).

- [[Ex - Christoffel symbols of spherical coordinates]] (⭐⭐) — invert the diagonal spherical metric and compute all nonzero Christoffel symbols ($\Gamma^r{}_{\theta\theta}=-r$, $\Gamma^\theta{}_{r\theta}=1/r$, $\cot\theta$, …), confirm they are purely spatial and identical to Euclidean $\mathbb{R}^3$, and verify the signature-independence of the result ([[Def - Christoffel Symbols]], [[Def - Arbitrary Coordinates and the Coordinate Basis]]).

- [[Ex - The covariant derivative of the metric is zero]] (⭐⭐) — prove $\boldsymbol{\nabla}g = 0$ both conceptually (constant tensor) and by substituting the Christoffel formula so the connection terms reassemble $\partial g$, check the component $\nabla_r g_{\theta\theta} = 0$ in spherical coordinates, deduce that index-raising commutes with $\boldsymbol{\nabla}$, and contrast the trivial flat-space role with the defining role in general relativity ([[Def - The Covariant Derivative]], [[Def - Christoffel Symbols]]).

- [[Ex - Divergence in curvilinear coordinates via the metric determinant]] (⭐⭐) — derive the spherical divergence operator from $\sqrt{-\det g} = r^2\sin\theta$, compute $\boldsymbol{\nabla}\!\cdot\vec{e}_r = 2/r$ both by the determinant formula and the Christoffel trace, and confirm $\boldsymbol{\nabla}\!\cdot\vec{e}_x = 0$ for the constant Cartesian field despite its position-dependent components ([[Thm - Divergence of a Vector and Tensor Field]], [[Def - Christoffel Symbols]]).

- [[Ex - Christoffel symbols and fictitious forces in rotating coordinates]] (⭐⭐⭐) — compute the Cartesian-rotating metric and its Christoffel symbols, identify the centrifugal ($\Gamma^i{}_{tt}$) and Coriolis ($\Gamma^i{}_{tj}$) symbols, recover the Newtonian rotating-frame accelerations $\ddot{x} = \omega^2 x + 2\omega\dot y$ from the slow-motion geodesic equation, and confirm the forces are fictitious by the vanishing of the Riemann tensor ([[Def - Christoffel Symbols]], [[Def - The Covariant Derivative]]).
