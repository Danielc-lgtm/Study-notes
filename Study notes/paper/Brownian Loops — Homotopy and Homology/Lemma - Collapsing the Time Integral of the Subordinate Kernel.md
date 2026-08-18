---
type: lemma
subject: probability
prereqs:
  - "Def - Weighted Potential Measure"
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Thm - Fubini-Tonelli Theorem"
tags: [paper, brownian-loops]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Lemma 2.11"
---

# Statement

> **Lemma (Belyaev–Huseynli 2.11).** For all $x,y\in X$,
> $$\int_0^\infty \frac{dt}{t}\,p^\phi(t,x,y) \;=\; \int_{(0,\infty)} p^E(s,x,y)\,V_\phi(ds),$$
> where $p^\phi$ is the [[Def - Subordinate Brownian Loop Measure|subordinate]] heat kernel, $p^E$ the original one, and $V_\phi$ the [[Def - Weighted Potential Measure|weighted potential measure]].

**In one line.** Integrating the subordinate kernel against the scale-invariant duration weight equals integrating the *original* kernel against $V_\phi$ — the identity that collapses every loop-mass double integral (over duration $t$ and subordination time $s$) into a single $s$-integral. Proof is one application of [[Thm - Fubini-Tonelli Theorem|Tonelli]] plus the definition of $V_\phi$.

**Full treatment and gap-free proof:** [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.4]].
