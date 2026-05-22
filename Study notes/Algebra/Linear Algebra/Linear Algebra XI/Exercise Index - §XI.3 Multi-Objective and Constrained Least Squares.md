---
type: exercise-index
subject: linear-algebra
section: "XI.3"
tags: [algebra, linear-algebra, applied, optimization, constrained-optimization]
---

## §XI.3 Multi-Objective and Constrained Least Squares — Exercises

The exercises in this section drill the recognition of multi-objective and constrained LS structure in problems that don't *look* like LS at first glance. The recurring skill is *identifying* the LS objective and constraint matrices in problems stated with different terminology (regularization, constraints, target values, soft vs. hard requirements), then *solving* via the appropriate framework — stacking for multi-objective, KKT for constrained. These exercises bridge between the technical LS machinery and the practical optimization tasks of §XI.4.

- [[Ex - Tikhonov regularization is a multi-objective LS problem]] (⭐) — Verify that Tikhonov $\min \|Ax - b\|^2 + \lambda \|x\|^2$ is a single LS problem with stacked matrix $\binom{A}{\sqrt{\lambda} I}$ and stacked vector $\binom{b}{0}$. The conceptual move that unifies all regularized LS problems under one framework ([[Def - Regularized Least Squares]], [[Def - Multi-Objective Least Squares]], [[Thm - Existence and Uniqueness of Least Squares Solution]]).

- [[Ex - Portfolio optimization as constrained LS]] (⭐⭐) — Recognize the Markowitz mean-variance portfolio problem as a constrained LS problem with budget and target-return constraints; write the KKT system and derive the two-fund theorem from the linearity of the solution in the target return ([[Def - Constrained Least Squares]], [[Def - KKT System]], [[Thm - Constrained Least Squares via KKT System]]).

- [[Ex - Linear quadratic control via constrained LS]] (⭐⭐⭐) — Set up the LQR problem as a single large constrained LS problem on a stacked time-series variable, with dynamics as block-banded constraints; derive the linear state-feedback law from the linearity of the solution in the initial state ([[Def - Linear Quadratic Control]], [[Def - Constrained Least Squares]], [[Def - KKT System]], [[Thm - Constrained Least Squares via KKT System]]).
