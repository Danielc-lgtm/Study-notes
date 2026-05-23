---
type: exercise-index
subject: differential-geometry
section: "12.4"
tags: [geometry, differential-geometry, lorentzian-geometry, pseudo-riemannian-geometry]
---

## §12.4 Semi-Riemannian and Lorentzian Manifolds — Exercises

This section's exercises drill the geometry of indefinite metrics, with special attention to the Lorentzian signature $(1, n-1)$ and its physical realisation as Minkowski space and curved spacetimes. The decisive new feature is the **causal classification** of tangent vectors into timelike, spacelike, and null — a trichotomy absent from Riemannian geometry. The exercises range from the basic identification of Minkowski space as a Lorentzian manifold (the bridge from special relativity to differential geometry) to the structural consequences of [[Def - Isometry|isometries]] on indefinite metrics, including the preservation of [[Def - Geodesic|geodesics]] and causal classification.

- [[Ex - Minkowski Space as the Flat Lorentzian Manifold]] (⭐⭐) — verify that $(\mathbb{R}^4, \eta)$ with $\eta = dt^2 - dx^2 - dy^2 - dz^2$ is a Lorentzian manifold; identify the isometry [[Def - Group|group]] as the Poincaré [[Def - Group|group]] $O(1, 3) \ltimes \mathbb{R}^{1, 3}$; bridge to [[Special Relativity I — Lorentz Transformations and Minkowski Space]] ([[Def - Lorentzian Manifold]], [[Def - Semi-Riemannian Metric and Signature]], [[Def - The Lorentz Group]], [[Def - Isometry of Riemannian Manifolds]])
- [[Ex - Isometries Send Geodesics to Geodesics]] (⭐⭐) — prove that Riemannian (or Lorentzian) [[Def - Isometry|isometries]] preserve [[Def - Geodesic|geodesics]], via the length-preservation argument or via the Levi-Civita connection ([[Def - Isometry of Riemannian Manifolds]], [[Def - Length of a Curve and Riemannian Distance]], [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)]])
- **Classify all causal vectors in a 2-D Lorentzian plane** (⭐, classical) — for $(\mathbb{R}^2, dt^2 - dx^2)$, identify the sets of timelike, spacelike, and null vectors at the origin, and verify that the null vectors form two lines through the origin (the $t = \pm x$ light cone in 2D). Uses [[Def - Causal Classification of Tangent Vectors]], [[Def - Lorentzian Manifold]].
- **Identify the signature of $g = dxdy + dydx$** (⭐, classical) — for the bilinear form on $\mathbb{R}^2$ given by $g = dxdy + dydx$ (with matrix $\bigl(\begin{smallmatrix}0 & 1 \\ 1 & 0\end{smallmatrix}\bigr)$), find a basis in which it diagonalises to $\mathrm{diag}(+1, -1)$, and conclude the signature is $(1, 1)$ — neutral signature in [[Def - Dimension|dimension]] 2, equivalent to the 2D Lorentzian metric $dt^2 - dx^2$ up to a change of variables. Uses [[Def - Semi-Riemannian Metric and Signature]].
- **Hairy ball: $S^2$ has no Lorentzian metric** (⭐⭐, from [[Thm - A Lorentzian Manifold Need Not Exist on Every Smooth Manifold]]) — show that the existence of a Lorentzian metric on a smooth manifold $M$ implies the existence of a nowhere-vanishing line field on $M$, and that $S^2$ admits no such line field (via the Euler characteristic $\chi(S^2) = 2 \neq 0$). Uses [[Def - Lorentzian Manifold]], [[Thm - A Lorentzian Manifold Need Not Exist on Every Smooth Manifold]].

Additional exercises drawing on Lorentzian geometry: classify the geodesics in Schwarzschild spacetime; verify the Schwarzschild metric satisfies the vacuum Einstein equations $R_{\mu\nu} = 0$; compute the Christoffel symbols of the FRW metric in cosmic-time coordinates. These belong to a future Riemannian Geometry I or General Relativity I topic but are forward-bridge problems.
