---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Nonlinear Least Squares Problem"
  - "Def - Gauss-Newton Algorithm"
  - "Def - Least Squares Problem"
  - "Def - Regularized Least Squares"
  - "Def - Partial Derivatives and the Jacobian Matrix"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation

Throughout, $f : \mathbb{R}^n \to \mathbb{R}^m$ is a differentiable nonlinear residual map with Jacobian $Df(x)$. The iterates are $x^{(1)}, x^{(2)}, \ldots$ and the **trust parameter** at iteration $k$ is denoted $\lambda^{(k)} > 0$. The identity matrix of size $n$ is $I$. The full symbol registry is on [[Linear Algebra XII — Applied III — Nonlinear Least Squares]]. See [[Def - Gauss-Newton Algorithm]] for the algorithm this modifies.

---

# Axiom Motivation

[[Def - Gauss-Newton Algorithm|Gauss–Newton]] has two failure modes:

**Failure mode 1: divergence.** When $x^{(k)}$ is far from a residual minimum, the Taylor approximation $\hat f(x; x^{(k)}) \approx f(x)$ is only valid locally, but the Gauss–Newton step computes the *global* minimizer of $\|\hat f(x; x^{(k)})\|^2$. If that minimizer is far from $x^{(k)}$, the step jumps into a region where the approximation does not hold, and the new iterate's true objective $\|f(x^{(k+1)})\|^2$ can be *larger* than $\|f(x^{(k)})\|^2$. Iterating can produce a sequence whose true objective grows without bound. The standard counterexample is the sigmoid from $x^{(1)} = 1.15$, where Newton diverges.

**Failure mode 2: rank deficiency.** If $Df(x^{(k)})$ has linearly dependent columns at some iterate, the matrix $Df^T Df$ is singular, and the Gauss–Newton update formula is undefined. The algorithm stops with an error.

We want a single modification that fixes both failure modes without changing what the algorithm does when both are well-behaved. The idea is to replace the *unconstrained* linear least squares subproblem
$$\min_x \; \|\hat f(x; x^{(k)})\|^2$$
by a *regularized* version that penalizes large steps:
$$\min_x \; \|\hat f(x; x^{(k)})\|^2 + \lambda^{(k)} \|x - x^{(k)}\|^2,$$
where $\lambda^{(k)} > 0$ is a parameter we will adapt. This is a [[Def - Regularized Least Squares|regularized least squares]] problem in $x$ (also called Tikhonov regularization or ridge regression), and it has a closed-form solution computable in the same way as the Gauss–Newton subproblem.

Why does this single modification fix *both* failure modes simultaneously?

For failure mode 1 (divergence): the term $\lambda^{(k)} \|x - x^{(k)}\|^2$ penalizes large steps. When $\lambda^{(k)}$ is large, the optimal $x$ is close to $x^{(k)}$, and the algorithm behaves like **gradient descent** on $\|f\|^2$ (the gradient direction is $-Df^T f$, and a small step in that direction is what the regularized problem returns). When $\lambda^{(k)}$ is small (or zero), the algorithm recovers Gauss–Newton. So the algorithm interpolates between gradient descent (safe, slow) and Gauss–Newton (bold, fast) — exactly the right behavior. The interpretation is **trust-region**: $\lambda^{(k)}$ controls how far we trust the affine approximation, hence how large a step we are willing to take.

For failure mode 2 (rank deficiency): the normal equations of the regularized subproblem are
$$(Df^T Df + \lambda^{(k)} I) \, x = Df^T (Df \, x^{(k)} - f(x^{(k)})) + \lambda^{(k)} x^{(k)}.$$
The matrix $Df^T Df + \lambda^{(k)} I$ is *always* invertible for $\lambda^{(k)} > 0$, regardless of whether $Df$ has full column rank. (The matrix is symmetric positive definite: $v^T (Df^T Df + \lambda I) v = \|Df v\|^2 + \lambda \|v\|^2 \geq \lambda \|v\|^2 > 0$ for $v \neq 0$.) So the algorithm never stops with an error.

Both failure modes fixed by one stroke. The price is that we now have a parameter $\lambda^{(k)}$ to choose at each iteration. How?

The natural rule, due to Marquardt, is **adapt $\lambda^{(k)}$ based on whether each step succeeds**. Compute the tentative iterate $x^{(k+1)}$ with the current $\lambda^{(k)}$. Evaluate the true objective $\|f(x^{(k+1)})\|^2$. If it is smaller than $\|f(x^{(k)})\|^2$ — the step succeeded — accept the iterate and *shrink* $\lambda$ (be bolder next time): $\lambda^{(k+1)} = 0.8 \, \lambda^{(k)}$. If the true objective did *not* decrease — the step failed, the linear approximation was untrustworthy — reject the step, set $x^{(k+1)} = x^{(k)}$, and *grow* $\lambda$ (be more cautious): $\lambda^{(k+1)} = 2 \lambda^{(k)}$. Repeat. The specific factors $0.8$ and $2$ are not magic; any pair with the geometric ratio between $1$ and $\infty$ works, and Boyd takes these as standard.

This adaptive rule is what makes Levenberg–Marquardt **robust**. The user does not have to choose $\lambda$; the algorithm chooses it automatically based on the local geometry. A run might start with $\lambda^{(1)} = 1$, grow $\lambda$ to $\sim 10$ in early iterations when the linearization is poor, then shrink it to $\sim 10^{-3}$ as the algorithm closes in on a solution and Gauss–Newton-like behavior is desired. The full quadratic convergence of Newton is recovered in the final phase, while the early phase is dominated by the cautious gradient-descent-like steps.

The single modification — add $\lambda^{(k)} \|x - x^{(k)}\|^2$ to the subproblem and adapt $\lambda^{(k)}$ — turns Gauss–Newton from a fragile algorithm requiring an excellent starting point into a robust workhorse. This is why Levenberg–Marquardt, not Gauss–Newton, is the production-quality algorithm for nonlinear least squares. It is the algorithm in MINPACK, in `scipy.optimize.leastsq`, in MATLAB's `lsqnonlin`, and in every nonlinear-fitting package in widespread use.

---

# The Definition

The **Levenberg–Marquardt algorithm** is the iterative procedure that, given a differentiable residual map $f : \mathbb{R}^n \to \mathbb{R}^m$, a starting point $x^{(1)}$, and an initial trust parameter $\lambda^{(1)} > 0$, generates iterates $x^{(2)}, x^{(3)}, \ldots$ by minimizing the regularized linearized objective

$$\min_x \; \|\hat f(x; x^{(k)})\|^2 + \lambda^{(k)} \|x - x^{(k)}\|^2,$$

where $\hat f(x; x^{(k)}) = f(x^{(k)}) + Df(x^{(k)})(x - x^{(k)})$ is the Taylor affine approximation. The minimizer is given in closed form by

$$x^{(k+1)} = x^{(k)} - \big( Df(x^{(k)})^T Df(x^{(k)}) + \lambda^{(k)} I \big)^{-1} Df(x^{(k)})^T f(x^{(k)}).$$

The trust parameter $\lambda^{(k)}$ is updated by an acceptance rule based on the change in true objective:

> **Algorithm 18.3 (Levenberg–Marquardt).** Given $f$, $x^{(1)}$, $\lambda^{(1)} > 0$, $k_\max$.
> For $k = 1, 2, \ldots, k_\max$:
> 1. *Linearize.* Compute $f(x^{(k)})$ and the Jacobian $Df(x^{(k)})$.
> 2. *Tentative iterate.* Set $x^{(k+1)}$ as the minimizer of $\|\hat f(x; x^{(k)})\|^2 + \lambda^{(k)} \|x - x^{(k)}\|^2$.
> 3. *Acceptance test.*
>    - If $\|f(x^{(k+1)})\|^2 < \|f(x^{(k)})\|^2$: *accept*, set $\lambda^{(k+1)} = 0.8 \, \lambda^{(k)}$.
>    - Otherwise: *reject*, set $x^{(k+1)} = x^{(k)}$ and $\lambda^{(k+1)} = 2 \, \lambda^{(k)}$.

Terminate early when $\|f(x^{(k)})\|^2$ is small, or when the optimality residual $\|2 Df(x^{(k)})^T f(x^{(k)})\|$ is small, or when iterates stop moving.

**The matrix $Df^T Df + \lambda^{(k)} I$ is always invertible for $\lambda^{(k)} > 0$.** This is the structural reason the algorithm never fails. The proof is one line: for $\lambda > 0$, $v^T(Df^T Df + \lambda I)v = \|Df v\|^2 + \lambda \|v\|^2 \geq \lambda \|v\|^2 > 0$ for $v \neq 0$, so the matrix is symmetric positive definite, hence invertible.

**Equivalent formulation as a stacked linear LS problem.** The regularized subproblem is equivalent to the *unregularized* linear least squares problem
$$\min_x \; \left\| \begin{pmatrix} Df(x^{(k)}) \\ \sqrt{\lambda^{(k)}} \, I \end{pmatrix} (x - x^{(k)}) + \begin{pmatrix} f(x^{(k)}) \\ 0 \end{pmatrix} \right\|^2.$$
This is useful in practice: one can solve the inner problem by [[Thm - Least Squares via QR Factorization|QR factorization]] of the stacked matrix, which is numerically more stable than forming $Df^T Df$ and adding $\lambda I$.

**Special case $n = 1$.** For $f : \mathbb{R} \to \mathbb{R}$, the Levenberg–Marquardt update simplifies to
$$x^{(k+1)} = x^{(k)} - \frac{f'(x^{(k)})}{\lambda^{(k)} + (f'(x^{(k)}))^2} f(x^{(k)}).$$
For $\lambda^{(k)} = 0$ this is Newton's method. For $f'(x^{(k)}) = 0$, the Levenberg–Marquardt step is still well-defined (the denominator is $\lambda^{(k)} > 0$), whereas Newton's step would be undefined.

---

# Relate to Other Fields / Compression

**Levenberg–Marquardt is the trust-region instantiation of Gauss–Newton.** General **trust-region methods** for unconstrained optimization solve a sequence of *constrained* subproblems: at each iterate, build a quadratic model $m^{(k)}(p)$ of the objective and find $p^*$ minimizing $m^{(k)}$ subject to $\|p\| \leq \Delta^{(k)}$. The radius $\Delta^{(k)}$ is updated based on the ratio of actual to predicted decrease. Levenberg–Marquardt is precisely the trust-region method whose quadratic model is the Gauss–Newton model ($m^{(k)}(p) = \|f(x^{(k)}) + Df(x^{(k)}) p\|^2$) and whose trust constraint is enforced via the Lagrange multiplier $\lambda^{(k)}$ that is dual to the radius constraint $\|p\| \leq \Delta^{(k)}$. The trust-region theory is the unifying frame; Levenberg–Marquardt is its most successful instance.

**Levenberg–Marquardt is regularized Gauss–Newton with adaptive regularization.** The inner subproblem is identical to ridge regression / [[Def - Regularized Least Squares|Tikhonov regularization]] applied to the Gauss–Newton linear subproblem, with regularization parameter $\lambda^{(k)}$. The outer adaptive rule for $\lambda^{(k)}$ — shrink on success, grow on failure — is what distinguishes Levenberg–Marquardt from "Tikhonov-regularized Gauss–Newton with fixed $\lambda$"; the adaptivity is the source of robustness.

**Levenberg–Marquardt blends Gauss–Newton with gradient descent.** Write the Levenberg–Marquardt step as $p^{(k)} = -(Df^T Df + \lambda I)^{-1} Df^T f$. For $\lambda \to 0$, $p^{(k)} \to -(Df^T Df)^{-1} Df^T f$, the Gauss–Newton step. For $\lambda \to \infty$, $p^{(k)} \approx -\frac{1}{\lambda} Df^T f$, a small step in the direction of the negative gradient — *gradient descent with step size $1/\lambda$*. So Levenberg–Marquardt is a *continuous interpolation* between these two algorithms, with $\lambda$ as the interpolation parameter. The trust-region framework explains why this is the right interpolation: $\lambda$ is dual to the trust radius.

**True name.** The operational characterization of Levenberg–Marquardt is: *Gauss–Newton with a trust-region penalty on the step size, where the penalty parameter is adapted based on whether each step decreases the true objective.* This is what makes it robust where Gauss–Newton is fragile, and what makes it the default algorithm for nonlinear least squares.

---

# Examples / Corollaries

**Example 1 (Levenberg–Marquardt fixes the divergent sigmoid).** With $f(x) = \tanh(x)$ and starting point $x^{(1)} = 1.15$, Newton diverges. Levenberg–Marquardt with $\lambda^{(1)} = 1$ converges. The mechanism: at iteration 1, the Newton step would jump to $\approx -1.32$, far from $x^{(1)}$; Levenberg–Marquardt with $\lambda = 1$ shrinks this to a much smaller step that *does* decrease the objective. Subsequent iterations shrink $\lambda$ (since steps succeed) and the algorithm picks up Newton-like quadratic convergence near $\hat x = 0$. (See [[Ex - Levenberg-Marquardt outperforms Gauss-Newton on a hard problem]].)

**Example 2 (rank-deficient Jacobian).** With $f(x_1, x_2) = (x_1 - x_2, x_1 - x_2)$ and any $\lambda > 0$, the Levenberg–Marquardt subproblem has Jacobian $Df = \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}$, hence $Df^T Df + \lambda I = \begin{pmatrix} 2 + \lambda & -2 \\ -2 & 2 + \lambda \end{pmatrix}$, which is invertible with determinant $(2 + \lambda)^2 - 4 = 4\lambda + \lambda^2 > 0$. The algorithm proceeds without error, whereas Gauss–Newton would terminate immediately.

**Example 3 (trust parameter adaptation traces).** In the equilibrium-prices example (Boyd §18.3, Figure 18.8), $\lambda^{(k)}$ starts at $1$, oscillates between $0.8$ and $2$ in early iterations as steps are accepted and rejected alternately, and finally decreases monotonically to $\sim 10^{-3}$ as the algorithm converges and Newton-like behavior dominates. This trace is the standard diagnostic: a $\lambda^{(k)}$ that stabilizes at a small value means the algorithm is in fast-convergence regime; a $\lambda^{(k)}$ that keeps growing means the algorithm is struggling.

**Non-example 1 ($\lambda^{(k)} \equiv 0$ is just Gauss–Newton).** Setting $\lambda^{(k)} = 0$ at every iteration disables the trust-region modification and recovers Gauss–Newton — failing to address either of its failure modes. The adaptivity is essential; a fixed $\lambda$ defeats the point.

**Non-example 2 (extremely large $\lambda$ degenerates to bare gradient descent).** Setting $\lambda^{(k)}$ to a huge constant gives, to leading order, $x^{(k+1)} \approx x^{(k)} - \frac{1}{\lambda} Df^T f$ — gradient descent with a tiny step size. This is safe (it decreases the objective every step) but extraordinarily slow. The point of Levenberg–Marquardt is precisely to *not* be stuck in this regime; the adaptive shrinkage of $\lambda$ when steps succeed is what allows the algorithm to escape into fast Newton-like convergence.

**Corollary (Newton's method specialization).** For $\lambda^{(k)} = 0$ and $m = n$, Levenberg–Marquardt is Newton's method on $f(x) = 0$. So Newton's method is the doubly-degenerate (no regularization, square system) special case of Levenberg–Marquardt.

**Corollary (regularization makes the inner system always solvable).** For any $\lambda^{(k)} > 0$, the inner regularized normal equations $(Df^T Df + \lambda^{(k)} I) p = -Df^T f$ have a unique solution $p$. This holds even if $Df$ is rank-deficient, even if $m < n$ (underdetermined), even if the columns of $Df$ are nearly linearly dependent. *Proof:* $Df^T Df + \lambda I$ is symmetric positive definite, hence invertible.

**Calibration check.** A reader who has understood Levenberg–Marquardt should: (i) write down the explicit update for $f(x) = x^2 - 2$ at $x^{(1)} = 1$ with $\lambda^{(1)} = 1$, and observe it differs from Newton's update; (ii) verify that for the rank-deficient Jacobian of Non-example 1 above, the inner system *is* solvable for $\lambda = 1$ and unsolvable for $\lambda = 0$; (iii) explain why "set $\lambda^{(k)} = 0$ once we are near the solution" recovers Newton-like quadratic convergence.

---

# Unlocked by This

> [!tip] Trust Region Methods *(from Optimization)*
> **Trust region methods** for general unconstrained optimization $\min \phi(x)$ build a quadratic model $m^{(k)}(p) = \phi(x^{(k)}) + g^{(k)T} p + \tfrac{1}{2} p^T B^{(k)} p$ at each iterate (with $B^{(k)}$ some symmetric approximation of the Hessian) and minimize $m^{(k)}$ subject to $\|p\| \leq \Delta^{(k)}$. The radius $\Delta^{(k)}$ is updated by the ratio of actual to predicted decrease — exactly analogous to the Levenberg–Marquardt $\lambda$-adaptation. Trust-region theory provides global convergence guarantees that Levenberg–Marquardt inherits in the LS setting. Algorithms like Steihaug's truncated CG, the dogleg method, and Powell's algorithm are different choices of how to (approximately) solve the trust-region subproblem efficiently — Levenberg–Marquardt's exact subproblem solution is the gold standard for least-squares-structured $B^{(k)} = Df^T Df$.

> [!tip] Damped Newton and Cubic Regularization *(from Numerical Optimization)*
> The Levenberg–Marquardt modification of Newton's method has many descendants. **Damped Newton** uses $x^{(k+1)} = x^{(k)} - \alpha^{(k)} H^{-1} g$ with line search on $\alpha^{(k)}$ rather than the regularization parameter $\lambda$. **Cubic regularization** (Nesterov–Polyak) adds a cubic term $\tfrac{\sigma}{3} \|p\|^3$ to the quadratic model, providing strong global convergence guarantees and a natural extension to saddle-point avoidance. The common theme: *the Newton step is too aggressive when the model is inaccurate, and a regularization-based correction makes the algorithm robust without sacrificing local quadratic convergence*.

> [!tip] Levenberg–Marquardt for Inverse Problems *(from Numerical Analysis)*
> In **ill-posed inverse problems** — recovering an image from blurry measurements, recovering subsurface parameters from seismic data — the forward model is a nonlinear map $F$ from parameters $x$ to predictions $y$, and the inverse problem $F(x) = y_\text{meas}$ has many near-solutions or is sensitive to noise. Levenberg–Marquardt with $\lambda$ playing the role of *Tikhonov regularization parameter* on the inverse problem (not just on the step) is the standard algorithm. The connection is direct: each LM iteration is *itself* a Tikhonov-regularized linearization, so running LM on a noisy inverse problem implicitly regularizes the inversion. The L-curve criterion and Morozov discrepancy principle for choosing $\lambda$ in linear Tikhonov regularization extend to LM with little change.
