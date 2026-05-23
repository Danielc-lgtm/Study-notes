---
type: exercise-index
subject: differential-geometry
section: "12.1"
tags: [geometry, differential-geometry, riemannian-geometry]
---

## §12.1 Riemannian Metrics — Exercises

This section's exercises drill the construction and verification of Riemannian metrics. The standard pattern is to take a manifold presented as a parametrised submanifold of Euclidean space (or some other ambient Riemannian manifold) and compute the induced metric by pulling back the ambient inner product along the parametrisation. The reusable technique is the Gram-matrix formula $g_{ij} = \langle \partial_i X, \partial_j X\rangle$ for the matrix of the induced metric in coordinates, which handles essentially every concrete example one encounters. The companion verification problems check the three defining properties — smoothness, symmetry, positive-definiteness — of candidate tensor fields, with the conformally-rescaled hyperbolic metric being the most important non-Euclidean example.

- [[Ex - The Round Metric on the Sphere via Restriction]] (⭐⭐) — induced metric via parametrisation; Gram-matrix computation for the standard 2-sphere ([[Def - Induced Metric on a Submanifold]], [[Def - Riemannian Metric]])
- [[Ex - The Hyperbolic Plane as a Riemannian Manifold]] (⭐⭐) — conformal rescaling of the Euclidean metric; positive-definiteness via the positive conformal factor $1/y^2$ ([[Def - Riemannian Metric]], [[Def - Riemannian Manifold]])
- **Induced metric on a cylinder is flat** (⭐⭐, from Lee Example 13.18(c)) — show that the cylinder $\{x^2 + y^2 = 1\}$ in $\mathbb{R}^3$ has induced metric $d\theta^2 + dz^2$, locally isometric to Euclidean $\mathbb{R}^2$, illustrating that "extrinsic curvature" (the cylinder is bent in $\mathbb{R}^3$) is distinct from "intrinsic curvature" (the cylinder's intrinsic geometry is flat). Uses [[Def - Induced Metric on a Submanifold]], [[Def - Riemannian Metric]].
- **Induced metric on a graph of a smooth function** (⭐⭐, from Lee Example 13.17) — for $f : U \subseteq \mathbb{R}^n \to \mathbb{R}$ smooth, the graph $\{(x, f(x))\} \subseteq \mathbb{R}^{n+1}$ inherits the metric $\sum (dx^i)^2 + df^2 = (\delta_{ij} + \partial_i f\, \partial_j f) dx^i dx^j$. Generalises to first fundamental forms of parametrised surfaces. Uses [[Def - Induced Metric on a Submanifold]].

Additional exercises drilling these patterns are found in Lee Ch 13 Problems 13-1, 13-4, 13-8, 13-20, and in do Carmo's *Riemannian Geometry* problem sets.
