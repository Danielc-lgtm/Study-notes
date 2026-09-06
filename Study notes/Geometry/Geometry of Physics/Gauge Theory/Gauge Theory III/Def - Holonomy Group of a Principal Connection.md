---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Parallel Transport of a Principal Connection"
tags: [gauge-theory, holonomy]
---

# The Definition

> [!definition] Holonomy
> Fix $p\in P_x$. For every piecewise-smooth loop $\gamma$ based at $x$, there is a unique element $h_\gamma\in G$ with
> $$\operatorname{PT}_\gamma(p)=p h_\gamma.$$
> The **holonomy group** is
> $$\operatorname{Hol}_p(\omega)=\{h_\gamma:\gamma\text{ is a loop at }x\}\subset G.$$

Concatenation and reversal show this is a subgroup. Replacing $p$ by $pg$ conjugates it:
$$\operatorname{Hol}_{pg}(\omega)=g^{-1}\operatorname{Hol}_p(\omega)g.$$
Thus only its conjugacy class is independent of the chosen point in the fibre.

# Restricted Holonomy

Loops homotopic to the constant loop generate the restricted holonomy group $\operatorname{Hol}^0_p$. Curvature governs this connected local part; topology can contribute additional components. In particular, a flat connection has trivial restricted holonomy but may have nontrivial full holonomy.

# Gauge Behaviour

A gauge transformation maps transport by endpoint conjugation. At a based loop, holonomy is conjugated by the gauge value at the base point. Conjugation-invariant functions such as traces in representations are therefore gauge-invariant Wilson loops.
