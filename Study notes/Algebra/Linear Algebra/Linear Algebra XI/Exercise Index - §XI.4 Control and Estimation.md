---
type: exercise-index
subject: linear-algebra
section: "XI.4"
tags: [algebra, linear-algebra, applied, control, estimation, kalman-filter]
---

## §XI.4 Control and Estimation — Exercises

The exercises in this section drill the three applications of constrained LS that close out Boyd's textbook: *portfolio optimization* (constrained LS in finance), *linear quadratic control* (constrained LS in dynamical systems), and *Kalman state estimation* (constrained LS in estimation). The recurring insight is that these three apparently disparate fields share *one* mathematical framework: minimize a quadratic objective subject to linear equality constraints, solve via the KKT system. The block-banded sparsity of the time-series problems (LQR, Kalman) makes them computationally tractable for long horizons; the linearity of solutions in the boundary / target data gives the structural theorems (two-fund theorem, linear state feedback, control-estimation duality).

- [[Ex - Portfolio optimization as constrained LS]] (⭐⭐) — Markowitz mean-variance portfolio optimization as constrained LS with budget and target-return constraints. The KKT system is small ($n + 2$ equations); the two-fund theorem follows from linearity in the target return ([[Def - Constrained Least Squares]], [[Def - KKT System]], [[Thm - Constrained Least Squares via KKT System]]).

- [[Ex - Linear quadratic control via constrained LS]] (⭐⭐⭐) — Set up LQR as a large constrained LS problem on a stacked time-series variable. The KKT matrix is block-banded; sparse LU solves in $O(T)$ flops. Linearity in the initial state gives the linear state-feedback law ([[Def - Linear Quadratic Control]], [[Def - Constrained Least Squares]], [[Def - KKT System]], [[Thm - Constrained Least Squares via KKT System]]).

- [[Ex - Kalman state estimation as constrained LS]] (⭐⭐⭐) — Set up the batch Kalman filter as a constrained LS problem. The KKT system has the same block-banded structure as LQR — *control-estimation duality*. The recursive Kalman filter is the sparse banded LU written sequentially. Validation on held-out measurements chooses the regularization parameter $\lambda$ ([[Def - Linear Quadratic State Estimation]], [[Def - Constrained Least Squares]], [[Def - KKT System]], [[Def - Validation (Training and Test Error)]], [[Thm - Constrained Least Squares via KKT System]]).
