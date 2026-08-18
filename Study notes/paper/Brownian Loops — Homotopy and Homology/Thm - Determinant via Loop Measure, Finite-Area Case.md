---
type: theorem
subject: spectral-geometry
prereqs:
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Thm - Selberg Zeta Identity for the Total Loop Mass"
tags: [paper, brownian-loops, zeta-functions, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 5.7"
---

# Statement

> **Theorem (renormalised determinant via loop measure, finite-area case; Belyaev–Huseynli 5.7).** For a geometrically finite hyperbolic surface of finite area with $n_C$ cusps and Euler characteristic $\chi$, and $\kappa\ge0$, $s=\frac12+\sqrt{\frac14+\kappa}>1$,
> $$-\log{\det}_0(\Delta_X+\kappa)=F\kappa-M+\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\mu^\kappa_X(C_X(\gamma^m))-D_X(s),$$
> and dividing out the simple zero at $s=1$, the $\kappa\to0^+$ limit gives $\log{\det}_0\Delta_X=\log C_X+\log Z_X'(1)$ ($M,F,D_X,C_X$ as in Borthwick–Judge–Perry).

**In one line.** The cusped-surface analogue of [[Thm - Determinant as Renormalised Loop Mass|Theorem 5.1]]: the renormalised ($0$-)[[Def - Zeta-Regularised Determinant of the Laplacian|determinant]] equals a killed loop mass plus explicit cusp corrections, with the same $\log\kappa$/simple-zero cancellation. Proof: substitute the [[Thm - Selberg Zeta Identity for the Total Loop Mass|Selberg identity]] into the Borthwick–Judge–Perry formula and take $\kappa\to0$.

**Full treatment and gap-free proof:** [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5.2]].
