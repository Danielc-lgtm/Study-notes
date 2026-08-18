---
type: theorem
subject: probability
prereqs:
  - "Def - Poisson Point Process and the Loop Soup"
  - "Thm - Mass of a Free Homotopy Class"
tags: [paper, brownian-loops, point-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Proposition 3.8"
---

# Statement

> **Proposition (Poissonian structure; Belyaev–Huseynli 3.8).** Let $\mathcal L_c$ be the [[Def - Poisson Point Process and the Loop Soup|loop soup]] of intensity $c\,\mu^\phi_X$. For $\gamma\in\mathcal P_X$ and $m\ge1$, the number of loops of $\mathcal L_c$ in the free homotopy class $C_X(\gamma^m)$ (for jump processes, of marked loops) is a Poisson random variable of mean $c\,\mu^\phi_X(C_X(\gamma^m))$; and for finitely many pairwise-distinct classes these counts are jointly independent.

**In one line.** Each closed-form class-mass from §3.1 is the *mean* of a Poisson count of soup loops, and winding numbers around distinct handles are independent — so the loop soup gives distributions, not just expectations. Immediate from the Poisson-count and independent-scattering axioms, since distinct classes are disjoint.

**Full treatment:** [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.3]].
