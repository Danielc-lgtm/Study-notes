---
type: exercise-index
subject: linear-algebra
section: "XII.1"
tags: [algebra, linear-algebra, applied, optimization]
---

## §XII.1 Nonlinear Least Squares — Exercises

This section's exercises drill the core algorithmic content of Boyd Chapter 18: solving the [[Def - Nonlinear Least Squares Problem|nonlinear least squares problem]] $\min \|f(x)\|^2$ by linearize-and-iterate methods. The three exercises are arranged to expose the unifying *linearize-and-solve-linear-LS* pattern in three different regimes. Exercise 1 applies bare [[Def - Gauss-Newton Algorithm|Gauss–Newton]] (= Newton's method, since $m = n$) to a small economics equilibrium problem, observing quadratic convergence in the late phase but also the basic algorithm's fragility. Exercise 2 is the canonical comparison: a function (the $\tanh$ sigmoid) where Newton diverges and [[Def - Levenberg-Marquardt Algorithm|Levenberg–Marquardt]]'s trust-parameter adaptation rescues convergence — the cleanest demonstration of why LM, not Gauss–Newton, is the production-quality algorithm. Exercise 3 is the master application of nonlinear LS to *classification*: replace the non-differentiable $\operatorname{sign}$ function by the smooth sigmoid $\phi(u) = \tanh(u)$ and apply LM to fit a classifier, recovering the structural pattern that links nonlinear LS to logistic regression and the neural-network family.

- [[Ex - Solving a system of nonlinear equations with Gauss-Newton]] (⭐⭐) — Newton's method on a square nonlinear system $f(p) = 0$ for two-commodity supply-demand equilibrium; quadratic local convergence and the rank-deficiency failure mode ([[Def - Gauss-Newton Algorithm]], [[Thm - Local Convergence of Gauss-Newton]], [[Def - Partial Derivatives and the Jacobian Matrix]])
- [[Ex - Levenberg-Marquardt outperforms Gauss-Newton on a hard problem]] (⭐⭐) — direct comparison of Newton's divergence from $x^{(1)} = 1.15$ against LM's convergence, exposing the trust-region mechanism via the $\lambda^{(k)}$ trajectory ([[Def - Gauss-Newton Algorithm]], [[Def - Levenberg-Marquardt Algorithm]], [[Def - Nonlinear Least Squares Problem]])
- [[Ex - Logistic regression as nonlinear least squares classification]] (⭐⭐) — sigmoid replacement of $\operatorname{sign}$ converts Boolean classification into a smooth nonlinear LS problem solvable by LM; recovers the structure of logistic regression ([[Def - Nonlinear Least Squares Problem]], [[Def - Levenberg-Marquardt Algorithm]], [[Def - Least Squares Classifier]], [[Def - Regularized Least Squares]])
