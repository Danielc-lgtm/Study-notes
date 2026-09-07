---
type: theorem
subject: gauge-theory
prereqs: ["Def - Dirac Bundle and Dirac Operator", "Def - Connection Laplacian"]
tags: [gauge-theory, weitzenbock-formula, dirac-operator]
---

# Prerequisite Concepts

- [[Def - Dirac Bundle and Dirac Operator]]
- [[Def - Connection Laplacian]]

# Statement

> [!theorem] Weitzenböck formula
> Let $D$ be the Dirac operator of a Dirac bundle $(E,c,\nabla)$. If $R^E$ is the connection curvature, then
> $$D^2=\nabla^*\nabla+\mathcal R,\qquad
> \mathcal R=\frac12\sum_{i,j}c(e^i)c(e^j)R^E_{e_i,e_j}.$$

# Motivation

The principal symbol already forces $D^2$ to have the same leading term as a Laplacian. The theorem identifies the complete lower-order error: curvature is the sole obstruction to “Dirac squared equals Laplacian.”

# Formal Proof

> [!proof]- Formal Proof
> Fix $x\in M$ and choose an orthonormal frame with $\nabla^{LC}_{e_i}e_j=0$ at $x$. Clifford compatibility gives
> $$D^2s=\sum_{i,j}c(e^i)c(e^j)\nabla_{e_i}\nabla_{e_j}s$$
> at $x$. The diagonal part is $-\sum_i\nabla_{e_i}\nabla_{e_i}s=(\nabla^*\nabla s)(x)$. Pair the $(i,j)$ and $(j,i)$ terms for $i\ne j$. Since the Clifford factors anticommute,
> $$\frac12\sum_{i\ne j}c(e^i)c(e^j)(\nabla_{e_i}\nabla_{e_j}-\nabla_{e_j}\nabla_{e_i})s
> =\frac12\sum_{i,j}c(e^i)c(e^j)R^E_{e_i,e_j}s.$$
> Here $[e_i,e_j](x)=0$ for the chosen normal frame, and the curvature definition supplies the displayed commutator. Both sides are intrinsic, so equality at every $x$ proves the formula.

# Consequences

For the untwisted spin Dirac operator, contraction of the spin curvature gives the Lichnerowicz formula $D^2=\nabla^*\nabla+\frac14\operatorname{scal}$. Twisting adds Clifford contraction of the twisting curvature. Positivity of the total zeroth-order term can force every harmonic spinor to vanish.

# Rederivation Scaffold

Choose a normal frame, separate diagonal and off-diagonal terms, and recognize the antisymmetrized second derivatives as curvature.

