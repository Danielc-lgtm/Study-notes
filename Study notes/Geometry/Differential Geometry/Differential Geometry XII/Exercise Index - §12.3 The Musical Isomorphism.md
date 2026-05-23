---
type: exercise-index
subject: differential-geometry
section: "12.3"
tags: [geometry, differential-geometry, riemannian-geometry]
---

## §12.3 The Musical Isomorphism — Exercises

This section's exercises drill the metric-induced canonical isomorphism between tangent and cotangent bundles, equivalently the operations of "raising and lowering indices" with the metric and its inverse. The central computational pattern is: given a metric $g_{ij}$ in coordinates, compute the inverse $g^{ij}$ by matrix inversion, and then apply $g^{ij}$ or $g_{ij}$ to raise or lower indices on a given vector or covector. The most common application is the gradient $\mathrm{grad}_g f = g^{ij}\partial_j f\, \partial_i$ — the *correct* manifold-intrinsic gradient, with the inverse-metric factor $g^{ij}$ that is invisible in Cartesian coordinates on Euclidean space but essential in any non-Cartesian system.

- [[Ex - Raising and Lowering Indices in Polar Coordinates]] (⭐⭐) — compute $g^{ij}$ in polar coordinates and use it to raise the index of the differential $df$ for a concrete $f$; verify via Cartesian conversion ([[Def - Musical Isomorphism (Flat and Sharp)]], [[Thm - Musical Isomorphism Identifies Tangent and Cotangent Bundles]])
- **Gradient and divergence in spherical coordinates** (⭐⭐, classical) — compute the Laplace–Beltrami operator $\Delta_g f$ for the Euclidean metric in spherical coordinates $(r, \theta, \varphi)$ on $\mathbb{R}^3$, and verify the formula $\Delta f = (1/r^2)\partial_r(r^2 \partial_r f) + (1/r^2 \sin\theta)\partial_\theta(\sin\theta\, \partial_\theta f) + (1/r^2\sin^2\theta)\partial_\varphi^2 f$. Uses [[Def - Musical Isomorphism (Flat and Sharp)]], [[Def - Riemannian Metric]].
- **The gradient of the standard coordinate function in any chart** (⭐) — for the metric $g$ in coordinates $x^i$, compute $\mathrm{grad}_g x^k = g^{kj}\partial_j$. Verify this agrees with $\partial_k$ when $g$ is the Euclidean metric in Cartesian coordinates. Uses [[Def - Musical Isomorphism (Flat and Sharp)]], [[Thm - Musical Isomorphism Identifies Tangent and Cotangent Bundles]].
- **Index gymnastics on the round sphere** (⭐⭐⭐, from Lee Problem 13-21) — for $f \in C^\infty(M)$ on a Riemannian manifold, prove that $\mathrm{grad}_g f$ at $p$ is orthogonal to the level set of $f$ through $p$, and that among unit tangent vectors, the directional derivative $v(f)$ is maximised in the direction of $\mathrm{grad}_g f$, with maximum value $|\mathrm{grad}_g f|_g$. Application: compute the geometry of level sets of "height functions" on the sphere. Uses [[Def - Musical Isomorphism (Flat and Sharp)]], [[Def - Riemannian Metric]].

Additional exercises from Lee Ch 13 Problems 13-21 (gradient as direction of steepest increase), 13-22 (the tangent and cotangent bundles are isomorphic — the result also holds *without* a metric, but the natural isomorphism requires one), 13-23 (smooth covector fields with prescribed zeros on $S^2$).
