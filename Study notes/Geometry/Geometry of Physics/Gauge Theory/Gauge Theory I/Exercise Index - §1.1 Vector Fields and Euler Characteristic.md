---
type: exercise-index
subject: gauge-theory
section: "1.1"
tags: [geometry, gauge-theory, topology]
---

## §1.1 Vector Fields and Euler Characteristic — Exercises

This section drills the central theorem of §1.1, the [[Thm - Poincare-Hopf Theorem|Poincaré-Hopf theorem]] $\sum j_v(p) = \chi(M)$, together with its primary consequence the [[Thm - Hairy Ball Theorem|Hairy Ball Theorem]]. The exercises develop the basic technique for computing vector-field indices in two dimensions (rotation count around a small circle), then verify Poincaré-Hopf for explicit fields on $S^2$ summing to $\chi(S^2) = 2$, and finally show by explicit construction that odd-dimensional spheres admit nowhere-zero tangent fields — completing Euler's iff statement. The first exercise is a basic calibration of the index calculation; the second drills the constructive existence direction (Stiefel field); the supplementary cross-link to the DG VI Möbius-bundle exercise shows the analogous *non-trivial-bundle* obstruction for line bundles, which is the topological precursor to the Chern-class machinery in §1.4.

- [[Ex - Index of the Source-Sink Vector Field on the Sphere]] (⭐) — Direct rotation count for $\partial/\partial\theta$ on $S^2$ giving indices $+1$ at each pole, summing to $\chi(S^2) = 2$; constructs a single-zero field of index $+2$ via stereographic projection ([[Def - Index of a Vector Field at a Zero]], [[Thm - Poincare-Hopf Theorem]])
- [[Ex - Stiefel Vector Field on the Odd Sphere is Nowhere-Zero]] (⭐⭐) — Explicit construction $v(x) = (-x_2, x_1, -x_4, x_3, \dots)$ on $S^{2k+1}$ via pairing coordinates and applying $90°$ rotation; verifies tangency and unit length, concluding $\chi(S^{2k+1}) = 0$ ([[Thm - Hairy Ball Theorem]], [[Thm - Poincare-Hopf Theorem]])
- [[Ex - The Möbius Bundle is Nontrivial]] (⭐⭐⭐) — *Supplementary, from [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]].* Constructs the rank-$1$ Möbius bundle $E \to S^1$ and shows via orientability that $E$ is not isomorphic to $S^1 \times \mathbb{R}$. This is the simplest non-trivial real line bundle and the topological precursor to the [[Def - The Dirac Monopole Bundle|Dirac monopole bundle]] in §1.4 — both are "bundles without global sections", with the latter being the complex / hermitian / $U(1)$ analogue ([[Def - Vector Bundle]], [[Def - Transition Function of a Vector Bundle]])
