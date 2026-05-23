---
type: exercise-index
subject: algebraic-topology
section: "1.2"
tags: [geometry, algebraic-topology]
---

## §1.2 The Singular Homology Functor — Exercises

This section establishes singular homology as a covariant functor $\mathbf{Top} \to \mathbf{Ab}$, the central organising fact of the chapter. The exercises drill functoriality (continuous maps induce homology homomorphisms), homotopy invariance (homotopic maps induce equal maps on homology), and the long-exact-sequence machinery (Mayer–Vietoris) that propagates local data to global computations. The single most important conceptual point is that homology is a *homotopy invariant*: the underlying topology suffices, and the smooth structure (if present) leaves no extra fingerprint. Mastery of this section enables the explicit computations of §1.3 and the de Rham comparison of §1.4.

- [[Ex - Computing H_n of S^n via Mayer-Vietoris]] (⭐⭐) — Compute $H_*(S^n; \mathbb{Z})$ inductively by Mayer–Vietoris on the cover by two open hemispheres, using homotopy invariance to identify the intersection with $S^{n-1}$. Drills the functoriality (inclusions induce homology maps), Mayer–Vietoris setup, and the homotopy-invariance step. ([[Thm - Mayer-Vietoris for Singular Homology]], [[Thm - Homotopy Invariance of Singular Homology]], [[Thm - Singular Homology of the Sphere]])

- [[Ex - Singular Homology of a Point]] (⭐) — Compute $H_*(\{*\}; G)$ as the base case of homotopy invariance: any contractible space has the same homology by [[Thm - Homotopy Invariance of Singular Homology]]. Drills the functoriality of constant maps and the chain-complex structure of a point. ([[Def - Singular Homology]], [[Def - The Boundary Operator]])

- [[Ex - Computing H_* of the Torus]] (⭐⭐) — Compute $H_*(T^2; \mathbb{Z})$ from the polygon triangulation. Drills the simplicial-to-singular equivalence (so simplicial homology computes the topological invariant) and the construction of the fundamental class $[T^2]$ as a generator of $H_2(T^2; \mathbb{Z}) = \mathbb{Z}$. ([[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces]], [[Def - Singular Homology]], [[Def - Euler Characteristic]])
