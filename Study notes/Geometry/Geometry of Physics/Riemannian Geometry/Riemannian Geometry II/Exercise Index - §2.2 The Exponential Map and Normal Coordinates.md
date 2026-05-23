---
type: exercise-index
subject: riemannian-geometry
section: "2.2"
tags: [geometry, riemannian-geometry, exponential-map, normal-coordinates, exercise-index]
---

## §2.2 The Exponential Map and Normal Coordinates — Exercises

This section drills the computational and conceptual machinery of the exponential map and its associated coordinate systems. The unifying principle is that **the exponential map is the bridge between the linear (tangent space) and the curved (manifold)**, and that its differential is computed by *Jacobi fields*. Singular points of $\exp_p$ correspond to conjugate points; the *injectivity radius* of $p$ is the largest radius on which $\exp_p$ is a [[Def - Diffeomorphism|diffeomorphism]], and it equals the first conjugate distance for many natural examples. Normal coordinates are the resulting Riemannian-Taylor coordinate system in which the metric is Euclidean at the centre point and the curvature appears as the second-order obstruction. The exercises here are all computational verifications of these structures on the sphere — the simplest non-trivial concrete example.

- [[Ex - The Exponential Map on a Sphere is a Local Diffeomorphism]] (⭐⭐) — explicit computation of $\exp_p$ on $S^n$ via great circles, identification of the diffeomorphism range $\{|v| < \pi\}$ and the conjugate-singular sphere $\{|v| = \pi\}$ ([[Def - The Riemannian Exponential Map]], [[Def - Geodesic]], [[Thm - The Inverse Function Theorem]], [[Ex - Great Circles are the Geodesics of the Sphere]])

- [[Ex - Jacobi Fields on a Sphere are Sinusoidal]] (⭐⭐) — reduction of the Jacobi equation on $S^n$ to the scalar ODE $f'' + f = 0$, deriving the explicit form $J(t) = \sin(t)e(t)$ along great circles ([[Def - Jacobi Field]], [[Ex - Great Circles are the Geodesics of the Sphere]], [[Thm - Jacobi Equation and Conjugate Points]])

- [[Ex - Conjugate Points on the Round Sphere are Antipodal]] (⭐⭐) — using the sinusoidal Jacobi-field formula to identify the conjugate locus of $S^n$ as the periodic returns $\{k\pi : k \in \mathbb{Z}^+\}$, each with multiplicity $n - 1$ ([[Def - Conjugate Point]], [[Def - Jacobi Field]], [[Ex - Jacobi Fields on a Sphere are Sinusoidal]], [[Thm - Jacobi Equation and Conjugate Points]])
