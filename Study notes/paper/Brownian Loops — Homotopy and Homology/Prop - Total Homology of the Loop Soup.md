---
type: theorem
subject: probability-geometry
prereqs:
  - "Def - Poisson Point Process and the Loop Soup"
  - "Thm - Fourier Inversion by Homology Class"
tags: [paper, brownian-loops, homology, point-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Proposition 6.7"
---

# Statement

> **Proposition (distribution of the loop soup's total homology; Belyaev–Huseynli 6.7).** Let $\mathcal L_\lambda$ be the [[Def - Poisson Point Process and the Loop Soup|loop soup]] of intensity $\lambda$, and $\beta(\lambda)=\sum_{\eta\in\mathcal L^*_\lambda}[\eta]\in H_1(X,\mathbb{Z})$ the total homology of its non-contractible, non-cusp-peripheral loops (a finite sum). Then for every unitary character $\chi$,
> $$\mathbb E\big[\chi(\beta(\lambda))\big]=\Big(\frac{Z_X(s)}{L_X(s,\chi)}\Big)^{\lambda},\qquad \mathbb P\big(\beta(\lambda)=\beta\big)=Z_X(s)^\lambda\!\int_{\widehat{H_1(X,\mathbb{Z})}}\!L_X(s,\chi)^{-\lambda}\,\overline{\chi(\beta)}\,d\chi.$$

**In one line.** The characteristic function of the loop soup's net homology is a ratio of [[Def - Selberg L-Function|Selberg L-function]] to zeta, raised to the intensity; Fourier-inverting gives the probability of each total-homology value. Proof: the Poisson exponential (Campbell) formula turns $\mathbb E[\chi(\beta(\lambda))]$ into $\exp(\lambda\int(\chi([\eta])-1)\,d\mu^\kappa_X)$, evaluated by the $L$-function and zeta identities; then [[Def - First Homology, Characters, and Finite Fourier Analysis|character orthogonality]] inverts.

**Full treatment and proof:** [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]].
