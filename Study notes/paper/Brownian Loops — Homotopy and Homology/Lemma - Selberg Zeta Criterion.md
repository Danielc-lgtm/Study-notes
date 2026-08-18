---
type: lemma
subject: probability-geometry
prereqs:
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Def - The Loop-Length Integral"
tags: [paper, brownian-loops, zeta-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Lemma 4.2"
---

# Statement

> **Lemma (Selberg zeta criterion; Belyaev–Huseynli 4.2).** Suppose there are constants $C>0$ and real $s>\delta$, independent of $L$, with
> $$\frac{L}{2\sinh(L/2)}\,I_\phi(L)=C\cdot\frac{e^{(1-s)L}}{e^{L}-1}\qquad(L>0),$$
> where $I_\phi$ is the [[Def - The Loop-Length Integral|loop-length integral]]. Then
> $$\sum_{\gamma\in\mathcal P_X}\sum_{m=1}^\infty\mu^\phi_X(C_X(\gamma^m))=-C\log Z_X(s).$$

**In one line.** Whenever a process's class-mass has the standard "$e^{(1-s)L}/(e^L-1)$" shape, its total mass over all homotopy classes is $-C\log$ of the [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent|Selberg zeta]] at $s$ — the master identity of §4. Proof: substitute the shape, sum over $\gamma,m$, recognise the log-expansion of $Z_X$.

**Full treatment and proof:** [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4.1]].
