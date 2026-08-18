---
type: theorem
subject: probability-geometry
prereqs:
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Thm - Prime Geodesic Theorem"
tags: [paper, brownian-loops, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Corollary 4.7"
---

# Statement

> **Corollary (finiteness; Belyaev–Huseynli 4.7).** For any Bernstein function $\phi$ in the paper, with spectral parameter $s=s(\phi)$ ($s=1$ for Brownian and $\alpha$-stable; $s=\frac12+\sqrt{\frac14+\kappa}$ for killing/shifted-stable with $\kappa\ge-\frac14$): if $s(\phi)>\delta$, then the total mass is finite,
> $$\sum_{\gamma\in\mathcal P_X}\sum_{m=1}^\infty\mu^\phi_X(C_X(\gamma^m))<\infty.$$

**In one line.** The total non-trivial-class mass is finite exactly when the loops' decay rate $s$ beats the geodesics' proliferation rate $\delta$ ([[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent|critical exponent]]); the threshold is sharp ($Z_X(s)\to0$ as $s\downarrow\delta$). Proof: reduce to $\sum_\gamma e^{-s\ell_\gamma}<\infty$, then integrate by parts against $N_X(R)\asymp e^{\delta R}/R$ ([[Thm - Prime Geodesic Theorem|prime geodesic theorem]]).

**Full treatment and proof:** [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4.2]].
