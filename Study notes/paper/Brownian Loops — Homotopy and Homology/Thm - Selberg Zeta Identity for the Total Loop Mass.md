---
type: theorem
subject: probability-geometry
prereqs:
  - "Lemma - Selberg Zeta Criterion"
tags: [paper, brownian-loops, zeta-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Corollary 4.3"
---

# Statement

> **Corollary (Selberg zeta identity; Belyaev–Huseynli 4.3).** For $\kappa\ge-\frac14$ with $s=\frac12+\sqrt{\frac14+\kappa}>\delta$,
> $$\sum_{\gamma\in\mathcal P_X}\sum_{m=1}^\infty\mu^\kappa_X(C_X(\gamma^m))=-\log Z_X\!\Big(\frac12+\sqrt{\frac14+\kappa}\Big).$$
> In particular, the total Brownian loop mass ($\kappa=0$, $s=1$) is $-\log Z_X(1)$.

**In one line.** The summed loop mass over all homotopy classes *is* a value of the [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent|Selberg zeta function]] — the paper's bridge from random loops to spectral geometry; finite for infinite-area surfaces ($\delta<1$), divergent for finite-area ones ($\delta=1$). Immediate from the [[Lemma - Selberg Zeta Criterion|Selberg zeta criterion]] with $C=1$.

**Full treatment:** [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4.1.1]].
