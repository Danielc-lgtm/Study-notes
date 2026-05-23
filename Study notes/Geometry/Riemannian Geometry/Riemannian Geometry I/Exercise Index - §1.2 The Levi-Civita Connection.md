---
type: exercise-index
subject: riemannian-geometry
section: "1.2"
tags: [geometry, riemannian-geometry, connections, levi-civita]
---

## §1.2 The Levi-Civita Connection — Exercises

The exercises of §1.2 drill the construction and computation of the [[Def - Levi-Civita Connection|Levi-Civita connection]] on concrete Riemannian manifolds via the [[Def - Christoffel Symbols|Christoffel formula]]. The three exercises systematically work through three canonical metrics: the round 2-sphere (constant positive curvature), the hyperbolic plane (constant negative curvature), and the polar-coordinate Euclidean plane (flat — illustrating that nonzero Christoffels do not imply curvature). Each entry below names the exercise, summarises the technique it practices in one line, and lists in parentheses every definition and theorem invoked in that exercise's solution.

- [[Ex - Christoffel Symbols of the Round Metric on the Sphere]] (⭐⭐) — apply the Christoffel formula to the diagonal metric $g = d\theta^2 + \sin^2\theta\,d\varphi^2$; only $\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta$ and $\Gamma^\varphi_{\theta\varphi} = \cot\theta$ are nonzero; verify the equator is a geodesic ([[Def - Christoffel Symbols]], [[Def - Riemannian Metric]], [[Def - Levi-Civita Connection]])
- [[Ex - Christoffel Symbols of the Hyperbolic Plane]] (⭐⭐) — apply the Christoffel formula to the conformally flat hyperbolic metric $g = (dx^2 + dy^2)/y^2$; get $\Gamma^x_{xy} = -1/y$, $\Gamma^y_{xx} = 1/y$, $\Gamma^y_{yy} = -1/y$; verify vertical lines and circles centred on $\partial\mathbb{H}^2$ are geodesics ([[Def - Christoffel Symbols]], [[Def - Riemannian Metric]], [[Def - Levi-Civita Connection]])
- [[Ex - The Levi-Civita Connection of Polar Coordinates]] (⭐) — apply the Christoffel formula to the polar form $g = dr^2 + r^2 d\theta^2$ of the Euclidean metric; verify by direct curvature computation that the connection is flat despite nonzero Christoffels — the canonical demonstration of "$\Gamma$ is not a tensor" ([[Def - Christoffel Symbols]], [[Def - Levi-Civita Connection]], [[Def - Curvature 2-Forms (Cartan)]])
