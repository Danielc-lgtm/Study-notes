---
type: theorem
subject: probability-geometry
prereqs:
  - "Thm - Homotopy Decomposition for 3-Manifolds"
  - "Lemma - Collapsing the Time Integral of the Subordinate Kernel"
tags: [paper, brownian-loops, hyperbolic-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 7.2"
---

# Statement

> **Theorem (subordinate mass, 3-manifolds; Belyaev–Huseynli 7.2).** For a Bernstein $\phi$, $\gamma\in\mathcal P_X$, $m\ge1$ (complex length $L=mL_\gamma=m\ell_\gamma+im\theta_\gamma$),
> $$\mu^\phi_X(C_X(\gamma^m))=2\pi\,\frac{e^{m\ell_\gamma}\ell_\gamma}{|e^{L}-1|^2}\int_{(0,\infty)}\frac{2s\,e^{-s}}{(4\pi s)^{3/2}}\,e^{-(m\ell_\gamma)^2/4s}\,V_\phi(ds).$$

**In one line.** [[Thm - Homotopy Decomposition for 3-Manifolds|Theorem 7.1]] evaluated via the explicit $\mathbb{H}^3$ heat kernel (whose strip integral the paper *derives itself*, unlike the surface case) and [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]]. The complex length enters through $|e^{L}-1|^2=2e^{m\ell_\gamma}(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma))$.

**Full treatment and gap-free strip-integral derivation:** [[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7.2]].
