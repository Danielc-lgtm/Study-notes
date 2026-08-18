---
type: definition
subject: geometry
prereqs:
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
  - "Def - First Homology, Characters, and Finite Fourier Analysis"
tags: [paper, zeta-functions, homology]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 6.3"
---

# Statement

> **Definition (Selberg $L$-function; Belyaev–Huseynli 6.3).** For a unitary character $\chi:H_1(X,\mathbb{Z})\to S^1$ and $\operatorname{Re}s>\delta$,
> $$L_X(s,\chi):=\prod_{\gamma\in\mathcal P_X}\prod_{k=0}^\infty\big(1-\chi([\gamma])\,e^{-(s+k)\ell_\gamma}\big),$$
> the [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent|Selberg zeta]] twisted by the one-dimensional representation $\chi$ (trivial $\chi\Rightarrow L_X=Z_X$); it continues meromorphically to $\mathbb{C}$.

**In one line.** The Selberg zeta with each geodesic weighted by a [[Def - First Homology, Characters, and Finite Fourier Analysis|character]] value — the geodesic analogue of a Dirichlet $L$-function, detecting how closed geodesics distribute across homology classes. Its log-expansion carries the character weight $\chi([\gamma])^m=\chi(m[\gamma])$, which regroups by homology (Cor 6.4) and Fourier-inverts to the [[Def - Mass in a Homology Class|homology-class masses]].

**Full treatment:** [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]].
