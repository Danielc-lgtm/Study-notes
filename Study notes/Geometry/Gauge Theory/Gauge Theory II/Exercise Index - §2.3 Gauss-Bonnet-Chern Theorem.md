---
type: exercise-index
subject: gauge-theory
section: "2.3"
tags: [geometry, gauge-theory, gauss-bonnet, characteristic-classes]
---

## §2.3 Gauss-Bonnet-Chern Theorem — Exercises

This section drills the **Gauss-Bonnet theorem** in its two flavors: the classical Gauss-Bonnet for surfaces (Chern's intrinsic proof) and the higher-dimensional Gauss-Bonnet-Chern theorem using the Pfaffian of the curvature 2-form. The exercises verify the theorem on specific manifolds — flat and curved tori, complex projective spaces — and exhibit how the **topological invariant** $\chi(M)$ is computable as a **geometric integral** of curvature. The recurring techniques are: choosing convenient metrics for explicit computation, exploiting symmetries to reduce the integral, and using the multiplicative property of Chern classes / the Pfaffian polynomial to convert curvature data into topological numbers.

- [[Ex - Gauss-Bonnet for the Torus]] (⭐⭐) — Two-way verification of $\chi(T^2) = 0$: directly from the flat metric ($K \equiv 0$), and from the donut surface in $\mathbb{R}^3$ via explicit fundamental forms, where positive curvature on the outer rim and negative curvature on the inner rim cancel exactly ([[Thm - Gauss-Bonnet for Closed Surfaces (Chern's Proof)]], [[Def - Riemannian Metric]], [[Def - Riemannian Volume Form]])

- [[Ex - Computing the Euler Class of the Tangent Bundle of CP^n]] (⭐⭐⭐) — Two-method computation of $\int_{\mathbb{CP}^n} e(T\mathbb{CP}^n) = n+1$: CW-decomposition of $\mathbb{CP}^n$ (one cell per even dimension), and Chern-class formula via the Euler sequence $(0 \to \mathcal{O} \to \mathcal{O}(1)^{n+1} \to T\mathbb{CP}^n \to 0)$ ([[Thm - Gauss-Bonnet-Chern Theorem]], [[Def - The Euler Class of a Real Oriented Vector Bundle]], [[Def - The Hopf Bundle]])

- [[Ex - The Tangent Bundle of S^2 from the SO(3) Hopf Fibration]] (⭐⭐) — Nontriviality of $TS^2$ from $\chi(S^2) = 2$ via Gauss-Bonnet; the simplest case of "no global section because Euler characteristic is nonzero" ([[Thm - Gauss-Bonnet for Closed Surfaces (Chern's Proof)]], [[Def - Orthonormal Frame Bundle]])
