# PAGE SPEC

- **Filename:** `Thm - Homology of a Point and of a Path-Connected Space.md`
- **Type:** theorem
- **Chapter:** Gauge Theory XII — Homotopy, Homology, Orientation, and Poincaré Duality  (folder `Gauge Theory XII/`)
- **Section:** §12.4 Singular Homology, Homotopy Invariance, and Excision

## Spec (from the manifest)

type: theorem; source items: T4.2.4(3), T4.2.8, I4.2.4; prereqs: [Def - Singular Homology with Coefficients, Def - Chain Complex and Its Homology, Def - Path-Connected Space]; statement: (i) $H_n(\{p\}; R) = R$ for $n = 0$ and $0$ for $n \ge 1$. (ii) For any space $X$, $H_0(X;R)$ is the free $R$-module on the set of path components of $X$; in particular $H_0(X;R) \cong R$ when $X$ is path connected, the isomorphism $\varepsilon : H_0(X;R) \to R$, $\sum \alpha_k x_k \mapsto \sum \alpha_k$, being the augmentation; proof: source: (i) full (Bär's computation: one simplex $\sigma_n$ per degree, $\partial \sigma_n = \sigma_{n-1}$ or $0$ according to the parity of $n$, so the complex is $0 \leftarrow R \xleftarrow{0} R \xleftarrow{1} R \xleftarrow{0} \cdots$), (ii) omitted; the page proves (ii) via the augmentation: $\varepsilon$ is surjective, its kernel is $\mathrm{im}\, \partial_1$ (a $0$-chain $\sum \alpha_k x_k$ with $\sum \alpha_k = 0$ is a boundary of a sum of paths from a fixed base point when $X$ is path connected), and the general case splits over path components (Ex in this section). Reference: Hatcher Prop. 2.6, 2.7. spec: Sources: connected manifolds are path connected; Targets: every Mayer–Vietoris computation of §12.5 starts from this page.
