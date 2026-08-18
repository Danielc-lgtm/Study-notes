---
type: theorem
subject: spectral-geometry
prereqs:
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Thm - Selberg Zeta Identity for the Total Loop Mass"
tags: [paper, brownian-loops, zeta-functions, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 5.1"
---

# Statement

> **Theorem (determinant as renormalised loop mass, compact case; Belyaev–Huseynli 5.1).** For a closed hyperbolic surface $X$, the [[Def - Zeta-Regularised Determinant of the Laplacian|zeta-regularised determinant]] $\det_\zeta\Delta$ (zero mode excluded) equals a renormalised total Brownian loop mass. In the killing case ($\phi=\lambda+\kappa$, $\kappa\to0^+$) this reduces cleanly to
> $$\log\det_\zeta\Delta=\operatorname{Area}(X)\,E+\log Z_X'(1),\qquad E=\frac{1}{4\pi}\big(4\zeta_R'(-1)-\frac12+\log2\pi\big),$$
> the classical D'Hoker–Phong formula. (Brownian and $\alpha$-stable cases use a geometric renormalisation subtracting the long-geodesic tail $\widetilde{\mathrm{Li}}(e^R)$ predicted by the refined prime geodesic theorem.)

**In one line.** The infinite total loop mass of a finite-area surface is renormalised to the finite spectral invariant $\det_\zeta\Delta$; the mechanism is a $\log\kappa$ divergence cancelling against the simple zero of the [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent|Selberg zeta]] at $s=1$. This finite value is the normalising constant of §6's probability measure.

**Full treatment and gap-free killing-limit proof:** [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5.1]].
