---
type: exercise-index
subject: linear-algebra
section: "XII.2"
tags: [algebra, linear-algebra, applied, optimization, constrained]
---

## §XII.2 Constrained Nonlinear Least Squares — Exercises

This section's exercises drill the algorithmic content of Boyd Chapter 19: solving the [[Def - Constrained Nonlinear Least Squares|equality-constrained nonlinear least squares problem]] $\min \|f(x)\|^2$ s.t. $g(x) = 0$ via outer-loop methods that convert the constrained problem into a sequence of unconstrained subproblems. The first exercise applies the [[Def - Penalty Algorithm|penalty algorithm]] to a problem so simple — quadratic objective with linear equality constraint — that every iterate, every multiplier estimate, and every constraint residual can be computed in closed form, providing a transparent verification of the $O(1/\mu)$ convergence rate predicted by [[Thm - Convergence of Penalty Algorithm]]. The second exercise scales up to a flagship application: **nonlinear optimal control** of a car steering between prescribed initial and final states, solved by the [[Def - Augmented Lagrangian Algorithm|augmented Lagrangian algorithm]] via direct transcription. The two together span the spectrum from "transparent baseline" to "production-scale application," illustrating why the augmented Lagrangian (not the penalty algorithm) is the workhorse of practical constrained nonlinear LS.

- [[Ex - Penalty method on a quadratic with linear constraint]] (⭐) — closed-form penalty-algorithm iterates on $\min \|x - (1,1)\|^2$ s.t. $x_1 + x_2 = 1$, verifying the $\|g\| = 1/(1 + 2\mu) = O(1/\mu)$ rate explicitly ([[Def - Penalty Algorithm]], [[Def - Constrained Nonlinear Least Squares]], [[Thm - Convergence of Penalty Algorithm]], [[Def - Constrained Least Squares]], [[Def - KKT System]])
- [[Ex - Nonlinear control with augmented Lagrangian]] (⭐⭐⭐) — direct-transcription formulation of car-steering optimal control with nonlinear dynamics constraints, solved by the augmented Lagrangian algorithm with sparsity-exploiting LM inner solves ([[Def - Augmented Lagrangian Algorithm]], [[Def - Constrained Nonlinear Least Squares]], [[Def - Levenberg-Marquardt Algorithm]], [[Thm - Augmented Lagrangian Recovers Lagrange Multipliers]])
