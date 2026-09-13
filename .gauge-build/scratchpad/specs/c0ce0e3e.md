# PAGE SPEC

- **Filename:** `Thm - Poincare-Lefschetz Duality for Manifolds with Boundary.md`
- **Type:** theorem
- **Chapter:** Gauge Theory XII — Homotopy, Homology, Orientation, and Poincaré Duality  (folder `Gauge Theory XII/`)
- **Section:** §12.8 Orientations, the Fundamental Class, and Poincaré Duality

## Spec (from the manifest)

type: theorem; source items: (Hatcher Thm 3.43; needed for `Thm - Cobordism Invariance of the Signature` in chapter XIII, i.e. for I5.3.4); prereqs: [Thm - Poincare Duality, Thm - Relative Fundamental Class of a Compact Manifold with Boundary, Def - Cap Product, Thm - Long Exact Sequence of a Pair in Singular Homology]; statement: Let $W$ be a compact $R$-oriented $n$-manifold with collared boundary $\partial W$ (e.g. smooth). Then cap product with $[W, \partial W]$ gives isomorphisms $H^k(W, \partial W; R) \to H_{n-k}(W;R)$ and $H^k(W;R) \to H_{n-k}(W, \partial W; R)$, and these fit into a commutative ladder (up to sign) between the long exact sequence of the pair $(W, \partial W)$ in cohomology and that in homology, with the vertical map $H^k(\partial W) \to H_{n-1-k}(\partial W)$ being Poincaré duality of the closed manifold $\partial W$; proof: source: none; the page follows Hatcher Thm 3.43 (pp. 253–254): with $M := W \setminus \partial W$ and the collar, $H^k(W, \partial W) \cong H^k_c(M)$ and $H_{n-k}(W) \cong H_{n-k}(M)$, and the first isomorphism is the non-compact Poincaré duality (B); the second isomorphism follows from the first, the ladder, and the five lemma (once the ladder is shown to commute up to sign, which is the naturality of cap products and the boundary formula of `Def - Cap Product`). Reference: Hatcher Thm 3.43. spec: Targets: chapter XIII's `Thm - Cobordism Invariance of the Signature` (the Lagrangian-subspace argument).
