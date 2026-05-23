---
type: exercise-index
subject: differential-geometry
section: "9.4"
tags: [geometry, differential-geometry, riemannian, integration]
---

## §9.4 Integration on Riemannian Manifolds — Exercises

This section's exercises practice computation and application of the Riemannian volume form $\omega_g = \sqrt{\det g_{ij}}\,dx^1\wedge\cdots\wedge dx^n$ — the canonical volume form arising from the marriage of orientation and metric. The unifying skill is recognizing $\omega_g$ as the bridge between geometry (metric + orientation) and analysis (integration of functions), and using it to compute volumes, areas, and integral quantities on specific Riemannian manifolds. The exercises here range from explicit coordinate computations of volume to applications in physics, where the Lorentzian / Minkowski volume form $\sqrt{|\det g|}\,d^4x$ provides the integration measure for action functionals and conservation laws.

- [[Ex - Volume of the n-Sphere via the Volume Form]] (⭐⭐⭐) — Computes $\mathrm{vol}(S^n) = 2\pi^{(n+1)/2}/\Gamma((n+1)/2)$ via the Riemannian volume form in spherical coordinates and the Wallis integral. The closed-form answer is the iconic surface-area formula. ([[Def - Riemannian Volume Form]], [[Thm - Existence of the Riemannian Volume Form]], [[Thm - Change of Variables for Integration on Manifolds]])
- [[Ex - Maxwell's Equations as Two Form Equations on Minkowski Space]] (⭐⭐⭐) — Uses the Lorentzian volume form $\sqrt{|\det\eta|}\,d^4x = dt\,dx\,dy\,dz$ on Minkowski space implicitly through the Hodge star $\star$ in the construction of $d{\star}F$. Stokes applied to the 4-volume gives the integral charge conservation law. ([[Thm - Stokes' Theorem on Manifolds]], [[Def - Minkowski Space and the Metric]], [[Def - Differential k-Form on a Manifold]])
- [[Ex - The Round Metric on the Sphere via Restriction]] (⭐⭐) — *(from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]])* Establishes the round metric on $S^n$ via restriction from the Euclidean ambient space; the volume form of this metric agrees with the area form constructed by contraction in §9.1. ([[Def - Induced Metric on a Submanifold]], [[Def - Riemannian Volume Form]])
