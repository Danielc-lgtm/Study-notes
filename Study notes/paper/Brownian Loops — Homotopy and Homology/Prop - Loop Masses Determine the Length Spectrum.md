---
type: theorem
subject: probability-geometry
prereqs:
  - "Def - Marked Length Spectrum"
  - "Thm - Mass of a Free Homotopy Class"
tags: [paper, brownian-loops, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Proposition 3.11"
---

# Statement

> **Proposition (loop masses determine length; Belyaev–Huseynli 3.11).** For every $\gamma\in\mathcal P_X$,
> $$\ell_\gamma=\log\!\Big(1+\frac{1}{\mu_X(C_X(\gamma))}\Big).$$
> For $\phi(\lambda)=\lambda+\kappa$ with $\kappa\ge-\frac14$, the killed mass $\mu^\kappa_X(C_X(\gamma))$ is strictly decreasing in $\ell_\gamma$, hence also determines it. In either case the loop masses determine the [[Def - Marked Length Spectrum|marked length spectrum]].

**In one line.** Invert the closed-form mass $\mu_X(C_X(\gamma))=1/(e^{\ell_\gamma}-1)$ to read the geodesic length off the loop mass; the killed masses are injective in $\ell_\gamma$ too (log-derivative $<0$). Feeds [[Cor - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]].

**Full treatment and proof:** [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.4]].
