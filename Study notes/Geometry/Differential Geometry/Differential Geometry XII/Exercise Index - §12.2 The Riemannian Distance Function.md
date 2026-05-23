---
type: exercise-index
subject: differential-geometry
section: "12.2"
tags: [geometry, differential-geometry, riemannian-geometry, topology]
---

## §12.2 The Riemannian Distance Function — Exercises

This section's exercises drill the metric-space structure on a Riemannian manifold and the comparison between Riemannian distance and Euclidean distance in coordinate charts. The decisive technical tool is the local-comparability lemma: on any compact subset of a chart, $g$ is bilipschitz-equivalent to the Euclidean metric, and this single fact converts manifold-distance statements into chart-distance statements. The exercises range from direct length computations (verifying basic length-formula manipulations) to the foundational topology-coincidence proof and applications to completeness.

- [[Ex - The Riemannian Distance Topology Coincides with the Manifold Topology]] (⭐⭐⭐) — the central foundational proof of §12.2, using the local-comparability lemma to pinch the two topologies together ([[Thm - The Riemannian Distance Makes M a Metric Space]], [[Def - Length of a Curve and Riemannian Distance]])
- **Distance on a punctured plane** (⭐⭐, from Lee Problem 13-11) — show that for $(\mathbb{R}^2 \setminus \{0\}, \bar g)$ there exist points $p, q$ such that no piecewise smooth curve achieves the infimum $d_g(p, q)$. (Hint: take points on opposite sides of the puncture; any curve must detour.) Demonstrates that the Riemannian distance is an infimum, not always a minimum — minimisers may not exist on incomplete manifolds. Uses [[Def - Length of a Curve and Riemannian Distance]], [[Thm - The Riemannian Distance Makes M a Metric Space]].
- **Length is independent of parametrisation** (⭐, from Lee Proposition 13.25) — for a piecewise smooth curve $\gamma : [a, b] \to M$ and a diffeomorphism $\varphi : [c, d] \to [a, b]$, prove $L_g(\gamma \circ \varphi) = L_g(\gamma)$. Direct application of change-of-variables in the length integral. Uses [[Def - Length of a Curve and Riemannian Distance]].
- **Length is preserved under isometries** (⭐, from Lee Exercise 13.24) — for an isometry $F : (M, g) \to (N, h)$ and a piecewise smooth curve $\gamma$ in $M$, prove $L_h(F \circ \gamma) = L_g(\gamma)$. (See also [[Ex - Isometries Send Geodesics to Geodesics]] for the consequence on geodesics.) Uses [[Def - Length of a Curve and Riemannian Distance]], [[Def - Isometry of Riemannian Manifolds]].

Additional exercises from Lee Ch 13 Problems 13-12 (isometry group of Euclidean space), 13-16 (completeness of one-dimensional metrics), and 13-17 (every connected manifold admits a complete Riemannian metric).
