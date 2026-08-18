---
type: theorem
subject: probability-geometry
prereqs:
  - "Def - Selberg L-Function"
  - "Def - Mass in a Homology Class"
tags: [paper, brownian-loops, homology, zeta-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 6.5"
---

# Statement

> **Theorem (Fourier expansion and inversion by homology class; Belyaev–Huseynli 6.5).** For $\operatorname{Re}s>\delta$ and every unitary character $\chi\in\widehat{H_1(X,\mathbb{Z})}$,
> $$-\log L_X(s,\chi)=\sum_{\beta\in H_1(X,\mathbb{Z})}\chi(\beta)\,\mu^\kappa_X(\beta),\qquad \mu^\kappa_X(\beta)=\int_{\widehat{H_1(X,\mathbb{Z})}}\big(-\log L_X(s,\chi)\big)\,\overline{\chi(\beta)}\,d\chi.$$

**In one line.** The [[Def - Selberg L-Function|Selberg L-function]] is the Fourier transform, over the character torus, of the [[Def - Mass in a Homology Class|homology-class masses]]; character orthogonality inverts it to extract the mass in any single class $\beta$. In the closed case the inversion is an integral over the Jacobian. Proof: regroup the $L$-function's log-expansion by homology, then integrate against $\overline{\chi(\beta)}$ using [[Def - First Homology, Characters, and Finite Fourier Analysis|character orthogonality]].

**Full treatment and proof:** [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]].
