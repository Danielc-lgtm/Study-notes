---
type: definition
subject: probability-geometry
prereqs:
  - "Def - Dirichlet Form and its Operator and Semigroup"
  - "Def - Brownian Loop Measure"
tags: [paper, brownian-loops, dirichlet-forms]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 2.2"
---

# Statement

> **Definition (Dirichlet-form loop measure; Belyaev–Huseynli Def. 2.2).** Let $(\mathcal E,\mathcal F)$ be a regular symmetric [[Def - Dirichlet Form and its Operator and Semigroup|Dirichlet form]] on $L^2(X,\operatorname{vol}_g)$ with transition density $p^E(t,x,y)$ and bridge measures $\mathbb{W}^{t,E}_{x\to y}$ (on càdlàg paths $D([0,t];X)$, mass $p^E(t,x,y)$). The **parametrised loop measure** on $C^*_X$ is the σ-finite measure
> $$\mu^{*,E}_X := \int_0^\infty\frac{dt}{t}\int_X \mathbb{W}^{t,E}_{x\to x}\,d\operatorname{vol}_g(x),$$
> invariant under the circular time-shift; its pushforward to $C_X$ is the **loop measure** $\mu^E_X$. Total mass $\int_0^\infty\frac1t\int_X p^E(t,x,x)\,d\operatorname{vol}_g(x)\,dt$.

**In one line.** The Brownian loop measure with Brownian motion replaced by *any* symmetric Markov process coming from a Dirichlet form (Le Jan's construction) — the abstraction that lets killed and jump processes be handled by the same formulas. Restriction still holds.

**Full treatment:** [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.2]].
