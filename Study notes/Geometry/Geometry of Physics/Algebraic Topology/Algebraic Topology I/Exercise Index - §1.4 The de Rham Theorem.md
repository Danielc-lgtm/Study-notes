---
type: exercise-index
subject: algebraic-topology
section: "1.4"
tags: [geometry, algebraic-topology, de-rham]
---

## §1.4 The de Rham Theorem — Exercises

This section establishes the [[Thm - The de Rham Theorem (Full Proof)|de Rham theorem]]: on a smooth manifold, de Rham cohomology and singular cohomology with real coefficients agree, via the integration pairing $\int_c \omega$. The exercises drill the well-definedness of the pairing (using Stokes's theorem), the explicit computation of the pairing in the simplest non-trivial case ($S^1$), and the interpretation of pairings as identifying dual basis elements. The single most important conceptual point is that the integration pairing is the bridge between smooth and topological invariants: every topological quantity computable by integration of forms (Betti number, Euler characteristic, winding number, Chern number) is a de Rham pairing in disguise. Mastery of this section enables the cross-field applications (gauge theory, complex geometry, mathematical physics) that follow.

- [[Ex - The Pairing Integral over a Simplex of a Form is a Chain-Homotopy Invariant]] (⭐⭐) — Show that $\int_c \omega$ depends only on $[\omega] \in H^p_{dR}$ and $[c] \in H_p$, via two applications of Stokes's theorem. Drills the well-definedness of the de Rham homomorphism, the dual roles of "closed" and "boundary" under integration, and the foundational identity $\int_{\partial \alpha} \beta = \int_\alpha d\beta$. ([[Def - de Rham Cohomology]], [[Def - Singular Homology]], [[Thm - Stokes' Theorem on Manifolds]])

- [[Ex - The de Rham Pairing for H^1 of S^1]] (⭐⭐) — Compute $\int_\gamma d\theta = 2\pi$ for the canonical loop $\gamma$ on $S^1$ and the angular form $d\theta$. Drills the de Rham pairing in the minimal non-trivial case, identifies the dual basis element $[d\theta]/(2\pi)$, and connects the computation to winding numbers and the $2\pi$-normalisation throughout physics. ([[Def - de Rham Cohomology]], [[Def - Singular Homology]], [[Thm - The de Rham Theorem (Full Proof)]], [[Thm - Singular Homology of the Sphere]])

- [[Ex - Euler Characteristic of a Closed Orientable Surface is 2 - 2g]] (⭐⭐) — Verify $\chi(\Sigma_g) = 2 - 2g$ from Betti numbers and from a triangulation, connecting the topological invariant $\chi$ to a smooth-form computation (via Gauss–Bonnet, the curvature integral equals $\chi$). Drills the cell-count method, the cross-checking of two computations, and the de Rham-theorem-mediated identification of smooth and topological invariants. ([[Def - Euler Characteristic]], [[Def - Betti Numbers]], [[Thm - Euler Characteristic via Alternating Betti Numbers]])
