---
type: definition
subject: probability-geometry
prereqs:
  - "Def - First Homology, Characters, and Finite Fourier Analysis"
  - "Thm - Mass of a Free Homotopy Class"
tags: [paper, brownian-loops, homology]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 6.1"
---

# Statement

> **Definition (mass in a homology class; Belyaev–Huseynli 6.1).** For $\beta\in H_1(X,\mathbb{Z})$ and $s=\frac12+\sqrt{\frac14+\kappa}$, $\operatorname{Re}s>\delta$,
> $$\mu^\kappa_X(\beta):=\sum_{\substack{\gamma\in\mathcal P_X,\,m\ge1\\ m[\gamma]=\beta}}\mu^\kappa_X(C_X(\gamma^m))=\sum_{\substack{\gamma,m\\ m[\gamma]=\beta}}\frac1m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}.$$

**In one line.** The killed loop mass grouped by [[Def - First Homology, Characters, and Finite Fourier Analysis|homology]] (net winding) rather than free homotopy — a coarser partition, summing infinitely many homotopy classes per $\beta$. Detected via Selberg $L$-functions and recovered by [[Thm - Fourier Inversion by Homology Class|Fourier inversion]] over the character torus.

**Full treatment:** [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]].
