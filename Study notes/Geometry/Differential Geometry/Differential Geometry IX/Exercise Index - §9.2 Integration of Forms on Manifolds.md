---
type: exercise-index
subject: differential-geometry
section: "9.2"
tags: [geometry, differential-geometry, integration]
---

## §9.2 Integration of Forms on Manifolds — Exercises

This section's exercises practice the chart-by-chart definition of the manifold integral and the practical "integration over a parametrization" technique. The unifying skill is recognizing that to compute $\int_M\omega$, one parametrizes (or covers) $M$, pulls back the form, and reduces to a multivariable Riemann integral on Euclidean space. The exercises here range from straightforward (sphere area, with a clean spherical parametrization) to involved (the $n$-sphere via Wallis integrals). The change-of-variables theorem and the orientation-preservation check are running themes.

- [[Ex - Computing the Integral of a 2-Form on the Sphere]] (⭐⭐) — Computes $\int_{S^2}\omega = 4\pi$ where $\omega$ is the area form, via the spherical parametrization $F(\varphi, \theta)$ and the pullback $F^*\omega = \sin\varphi\,d\varphi\wedge d\theta$. ([[Def - Integral of a Compactly Supported Form on a Manifold]], [[Def - Pullback of a Differential Form on a Manifold]], [[Thm - Change of Variables for Integration on Manifolds]])
- [[Ex - Volume of the n-Sphere via the Volume Form]] (⭐⭐⭐) — Generalizes the 2-sphere computation to $S^n$ in higher-dimensional spherical coordinates, with the volume form $\sin^{n-1}\varphi_1\cdots\sin\varphi_{n-1}\,d\varphi_1\cdots d\theta$ and the closed-form answer $\mathrm{vol}(S^n) = 2\pi^{(n+1)/2}/\Gamma((n+1)/2)$. ([[Def - Riemannian Volume Form]], [[Thm - Existence of the Riemannian Volume Form]], [[Thm - Change of Variables for Integration on Manifolds]])
- [[Ex - The Round Metric on the Sphere via Restriction]] (⭐⭐) — *(from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]])* Shows the round metric on $S^n$ is the induced metric from the Euclidean ambient space, with the area form arising naturally from this construction. ([[Def - Induced Metric on a Submanifold]], [[Def - Riemannian Volume Form]])
