---
type: definition
subject: probability-geometry
prereqs:
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Dirichlet Form Loop Measure"
tags: [paper, brownian-loops, levy-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 2.8"
---

# Statement

> **Definition (subordinate Brownian loop measure; Belyaev–Huseynli Def. 2.8).** Fix a [[Def - Bernstein Function, Subordinator, and Subordination|Bernstein function]] $\phi$ and let $(\mathcal E^\phi,\mathcal F^\phi)$ be the subordinate [[Def - Dirichlet Form and its Operator and Semigroup|Dirichlet form]] on $L^2(X,\operatorname{vol}_g)$, with transition density $p^\phi(t,x,y)=\int_{[0,\infty)}p^E(s,x,y)\,\psi^\phi_t(ds)$ and bridge masses $p^\phi(t,x,y)$. The **rooted subordinate Brownian loop measure** is
> $$\mu^{*,\phi}_X := \int_0^\infty\frac{dt}{t}\int_X \mathbb{W}^{t,\phi}_{x\to x}\,d\operatorname{vol}_g(x),$$
> with pushforward $\mu^\phi_X$ to $C_X$.

**In one line.** The [[Def - Dirichlet Form Loop Measure|Dirichlet-form loop measure]] for the subordinate process $\phi(A)$ — i.e. loops of the process obtained by running the original one on the random clock with Laplace exponent $\phi$ (killed Brownian motion, $\alpha$-stable, …).

**Full treatment:** [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.4]].
