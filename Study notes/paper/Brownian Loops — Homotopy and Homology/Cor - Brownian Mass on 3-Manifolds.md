---
type: theorem
subject: probability-geometry
prereqs:
  - "Thm - Mass of Subordinate Loops on 3-Manifolds"
tags: [paper, brownian-loops, hyperbolic-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Corollary 7.3"
---

# Statement

> **Corollary (Brownian mass, 3-manifolds; Belyaev–Huseynli 7.3).** For pure Brownian motion on a geometrically finite hyperbolic 3-manifold, $\gamma\in\mathcal P_X$, $m\ge1$ (complex length $L_\gamma=\ell_\gamma+i\theta_\gamma$),
> $$\mu_X(C_X(\gamma^m))=\frac1m\cdot\frac{1}{|e^{mL_\gamma}-1|^2}=\frac{e^{-m\ell_\gamma}}{2m(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma))}=\frac1m\Big[(e^{m\ell_\gamma}-1)^2+4e^{m\ell_\gamma}\sin^2\frac{m\theta_\gamma}{2}\Big]^{-1}.$$

**In one line.** The 3-manifold analogue of the surface formula $\frac1m\frac{1}{e^{m\ell_\gamma}-1}$, with the *square* $|e^{mL_\gamma}-1|^2$ replacing $e^{m\ell_\gamma}-1$ (the extra dimension) and the holonomy angle $\theta_\gamma$ entering through $\cos(m\theta_\gamma)$; reduces to $(e^{m\ell_\gamma}-1)^{-2}/m$ when $\theta_\gamma=0$. Proof: [[Thm - Mass of Subordinate Loops on 3-Manifolds|Theorem 7.2]] with $V_\phi=ds/s$ and the Gaussian-type integral.

**Full treatment and gap-free proof:** [[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7.2]].
