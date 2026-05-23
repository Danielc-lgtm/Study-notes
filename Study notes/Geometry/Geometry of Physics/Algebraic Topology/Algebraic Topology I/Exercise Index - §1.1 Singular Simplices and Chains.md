---
type: exercise-index
subject: algebraic-topology
section: "1.1"
tags: [geometry, algebraic-topology]
---

## §1.1 Singular Simplices and Chains — Exercises

This section establishes the basic vocabulary of singular homology: simplices as continuous maps from the standard simplex, chains as formal sums, the boundary operator as the alternating face sum. The exercises here drill the foundational mechanics — what counts as a simplex (any continuous map, including degenerate ones), how to compute boundaries, and the verification that $\partial^2 = 0$ in low-dimensional cases. The single most important conceptual point is that a singular simplex is a *map*, not its image: constant maps are valid simplices, low-rank maps are valid simplices, and the chain complex absorbs all of them via the alternating-sign boundary structure. Mastery of these mechanics is prerequisite for every later computation.

- [[Ex - Singular Homology of a Point]] (⭐) — Compute $H_*(\{*\}; G)$ by enumerating the (single) singular simplex in each dimension and computing the alternating-sum boundaries. Drills the explicit chain-complex structure and the cancellation pattern $\sum (-1)^k$. ([[Def - Singular Simplex]], [[Def - The Boundary Operator]], [[Def - Singular Homology]])

- [[Ex - Computing H_n of S^n via Mayer-Vietoris]] (⭐⭐) — Compute $H_*(S^n; \mathbb{Z})$ inductively using Mayer–Vietoris on the cover by two open hemispheres. Drills the Mayer–Vietoris setup, the long exact sequence in special cases, and the connecting homomorphism. ([[Thm - Mayer-Vietoris for Singular Homology]], [[Thm - Singular Homology of the Sphere]], [[Thm - Homotopy Invariance of Singular Homology]])

- [[Ex - Computing the Homology of the Torus]] (⭐⭐) — Compute $H_*(T^2; \mathbb{Z})$ from the standard rectangle-with-identifications triangulation. Drills simplicial chain computations, fundamental-class construction, and the interplay between boundary identifications and orientation. ([[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces]], [[Def - Singular Homology]], [[Def - Euler Characteristic]])
