---
type: exercise-index
subject: multivariate-analysis
section: "4.3"
tags: [analysis, multivariate-analysis]
---

## §4.3 The Classical Integral Theorems — Exercises

The exercises of §4.3 drill the three classical integral theorems (Green, divergence, Kelvin-Stokes) as the unified Stokes statement in different ambient dimensions. Each exercise practices the same recipe: convert a boundary integral to an interior integral of the exterior derivative, choose a convenient parametrisation, and exploit surface-independence (a consequence of $d \circ d = 0$). The unifying observation: the classical integral theorems are all $\int_M d\omega = \int_{\partial M} \omega$ in different guises.

- [[Ex - Computing area with Green's theorem]] (⭐) — apply the area corollary $\operatorname{area}(\Omega) = \tfrac12\oint_{\partial\Omega}(x\,dy - y\,dx)$ to an ellipse and an astroid by pulling the $1$-form back along the boundary parametrization, watch the integrand collapse via the Pythagorean identity, and verify that the three equivalent forms of the area formula agree because they differ by the integral of an exact form around a closed curve ([[Thm - Green's Theorem]], [[Def - Pullback of a Differential Form]]).

- [[Ex - Flux through a closed surface]] (⭐⭐) — compute the outward flux of polynomial vector fields through a sphere, a ball's boundary, and a cube's boundary by converting each closed-surface integral to a volume integral of the divergence, and observe that the flux sees only $\operatorname{div} F$ — the rotational, divergence-free part of a field contributes nothing through any closed surface ([[Thm - The Divergence Theorem]], [[Def - The Exterior Derivative]]).

- [[Ex - Circulation of a vector field via Stokes' theorem]] (⭐⭐) — compute circulations of vector fields around the unit circle and a triangular space curve by replacing each line integral with the flux of the curl through the flattest spanning surface, then confirm surface-independence by recomputing one circulation over a hemisphere — the freedom to choose the surface is the integral shadow of $d\circ d = 0$ ([[Thm - The Kelvin-Stokes Theorem]], [[Def - The Exterior Derivative]], [[Def - Pullback of a Differential Form]]).
