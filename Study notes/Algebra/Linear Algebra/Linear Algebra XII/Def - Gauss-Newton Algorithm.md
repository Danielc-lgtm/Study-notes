---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Nonlinear Least Squares Problem"
  - "Def - Least Squares Problem"
  - "Def - Normal Equations"
  - "Def - Partial Derivatives and the Jacobian Matrix"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation

Throughout, $f : \mathbb{R}^n \to \mathbb{R}^m$ is a differentiable nonlinear residual map, with Jacobian $Df(x)$ of size $m \times n$. The iterates of an iterative algorithm are written $x^{(1)}, x^{(2)}, \ldots$, with $x^{(1)}$ called the **starting point** and $x^{(k)}$ the **$k$th iterate**. The full symbol registry is on [[Linear Algebra XII — Applied III — Nonlinear Least Squares]]. See [[Def - Nonlinear Least Squares Problem]] for the underlying optimization problem.

---

# Axiom Motivation

We want to minimize $\|f(x)\|^2$ for a nonlinear $f$. The optimality condition $Df(\hat x)^T f(\hat x) = 0$ is a nonlinear system in $n$ unknowns; there is no closed-form solver. So we must iterate, and at each iterate we must take *some* step — but which?

The cleanest idea is the following. At the current iterate $x^{(k)}$, the residual $f$ is *approximately* affine: the Taylor expansion
$$f(x) \approx \hat f(x; x^{(k)}) := f(x^{(k)}) + Df(x^{(k)})(x - x^{(k)})$$
is valid to first order in $x - x^{(k)}$. So *for points $x$ near $x^{(k)}$*, the original problem $\min \|f(x)\|^2$ is approximately the problem $\min \|\hat f(x; x^{(k)})\|^2$ — and *this* is a **linear** least squares problem, because $\hat f$ is affine in $x$. We know how to solve linear least squares exactly, in one step, via the [[Def - Normal Equations|normal equations]]. So set $x^{(k+1)}$ to be the exact minimizer of the linear subproblem, and hope that $\hat f \approx f$ stays valid long enough for $x^{(k+1)}$ to be closer to the true solution than $x^{(k)}$ was.

This is the entire idea. The algorithm is constructed by taking the most basic thing one can do — replace the nonlinear function by its tangent affine approximation — and applying it at every iterate. Every other algorithm in this chapter is a refinement.

Now: what makes this idea reasonable enough to be implementable, and what makes it unreasonable enough to need fixing? Two questions.

The first is whether the inner linear least squares subproblem is well-posed. The normal equations $(Df^T Df) x = Df^T b$ for the subproblem are uniquely solvable exactly when $Df$ has linearly independent columns — equivalently, when $Df^T Df$ is invertible. So Gauss–Newton requires the Jacobian to have full column rank at the current iterate. This is the *required structural assumption* for the algorithm to make sense. If the Jacobian is rank-deficient, $Df^T Df$ is singular and the algorithm stops with an error. (Levenberg–Marquardt fixes this by adding $\lambda I$.)

The second question is whether Gauss–Newton is a good algorithm — whether $x^{(k+1)}$ is actually closer to the solution than $x^{(k)}$. This is *not guaranteed*. The approximation $f(x) \approx \hat f(x; x^{(k)})$ is only valid for $x$ near $x^{(k)}$. The Gauss–Newton step can jump arbitrarily far if the linear subproblem's minimizer is far from $x^{(k)}$, and in that case there is no reason to expect the new iterate to be better than the old. The standard pathological example (Boyd Figure 18.3) is the sigmoid $f(x) = (e^x - e^{-x})/(e^x + e^{-x})$ from starting point $x^{(1)} = 1.15$, where Gauss–Newton (= Newton's method for $m = n = 1$) diverges. This is the *failure mode* that motivates Levenberg–Marquardt.

The Gauss–Newton step, when it works, has a deep interpretation that justifies why "just linearize and solve LS" succeeds at all. The full Hessian of $\|f(x)\|^2$ is $2 Df^T Df + 2 \sum_i f_i \nabla^2 f_i$, and Newton's method for minimizing $\|f\|^2$ would use the full Hessian. Gauss–Newton **drops the second term** — the curvature contribution weighted by the residuals — and uses $Df^T Df$ alone as approximate Hessian. The dropped term is zero exactly when $f(\hat x) = 0$ at the minimum (each $f_i$ vanishes there), so for zero-residual problems Gauss–Newton is *Newton's method itself*, inheriting Newton's quadratic local convergence. For problems with large residuals at the minimum, the dropped term is not zero and Gauss–Newton is only an approximation of Newton; convergence degrades to linear. So Gauss–Newton is "Newton-fast at zero-residual minima, gradient-descent-slow at large-residual minima."

Why specifically use $Df^T Df$ instead of the full Hessian? Because $Df^T Df$ is *free* — it costs no extra derivatives beyond the Jacobian $Df$ that we already need for the gradient $2 Df^T f$. The full second-derivative Hessian would require $n^2 m$ second-derivative evaluations of the $m$ component functions, prohibitively expensive in most applications. Gauss–Newton trades a small accuracy loss (when residuals are large at the minimum) for a large computational saving. This trade-off is fundamental to the chapter.

Finally, the special case $m = n$: the Jacobian is square, $Df^T Df$ is invertible iff $Df$ is invertible, and the Gauss–Newton step simplifies to $x^{(k+1)} = x^{(k)} - Df(x^{(k)})^{-1} f(x^{(k)})$, which is exactly **Newton's method** for solving the nonlinear system $f(x) = 0$. So Newton's root-finding method is the Gauss–Newton specialization to $m = n$.

---

# The Definition

The **Gauss–Newton algorithm** is the iterative procedure that, given a differentiable residual map $f : \mathbb{R}^n \to \mathbb{R}^m$ and a starting point $x^{(1)}$, generates iterates $x^{(2)}, x^{(3)}, \ldots$ by

$$x^{(k+1)} = x^{(k)} - \big( Df(x^{(k)})^T Df(x^{(k)}) \big)^{-1} Df(x^{(k)})^T f(x^{(k)}),$$

provided the Jacobian $Df(x^{(k)})$ has linearly independent columns (so that $Df^T Df$ is invertible). Equivalently, $x^{(k+1)}$ is the minimizer of the linearized objective $\|\hat f(x; x^{(k)})\|^2 = \|f(x^{(k)}) + Df(x^{(k)})(x - x^{(k)})\|^2$, computed by the [[Def - Normal Equations|normal equations]] of that linear least squares subproblem.

**Algorithm in pseudocode:**

> **Algorithm 18.1 (Basic Gauss–Newton).** Given $f$, $x^{(1)}$, $k_\max$. For $k = 1, 2, \ldots, k_\max$:
> 1. *Linearize.* Compute $f(x^{(k)})$ and the Jacobian $Df(x^{(k)})$.
> 2. *Solve linear least squares.* Set $x^{(k+1)} = x^{(k)} - (Df^T Df)^{-1} Df^T f$, all evaluated at $x^{(k)}$.
>
> Terminate early if $\|f(x^{(k)})\|$ is small enough, or if $\|x^{(k+1)} - x^{(k)}\|$ is small. Terminate with an error if $Df(x^{(k)})$ has linearly dependent columns.

The algorithm stops at the optimality condition $Df^T f = 0$, since $x^{(k+1)} = x^{(k)}$ holds if and only if $Df(x^{(k)})^T f(x^{(k)}) = 0$.

**Special case $m = n$ (Newton's method).** When the residual is square ($m = n$), $Df$ is square and the update simplifies to
$$x^{(k+1)} = x^{(k)} - Df(x^{(k)})^{-1} f(x^{(k)}),$$
which is **Newton's method** for solving the nonlinear equation $f(x) = 0$. The line "Gauss–Newton with $m = n$ = Newton's method" is one of the most important identifications in the chapter.

---

# Relate to Other Fields / Compression

**Gauss–Newton is Newton's method with the curvature term dropped.** The full Newton step on $\phi(x) = \|f(x)\|^2$ uses the Hessian $\nabla^2 \phi(x) = 2 Df(x)^T Df(x) + 2 \sum_i f_i(x) \nabla^2 f_i(x)$. Gauss–Newton replaces this by $2 Df^T Df$, dropping the second-derivative sum. The dropped term is the **curvature contribution** to the Hessian — weighted by the current residuals — and vanishes at zero-residual minima. So Gauss–Newton coincides with Newton at zero-residual minima and deviates from Newton in proportion to the residuals.

**Gauss–Newton is one step of Newton's method on the nonlinear gradient equations.** Set $g(x) = Df(x)^T f(x)$, the gradient up to a factor of 2. Newton's method on $g(x) = 0$ would update by $x^{(k+1)} = x^{(k)} - Dg(x^{(k)})^{-1} g(x^{(k)})$, with $Dg(x) = Df^T Df + \sum_i f_i \nabla^2 f_i$ — the full Hessian. Gauss–Newton applies Newton's method using only the first term of $Dg$, which is the Jacobian's "self-product" structure.

**Gauss–Newton is the natural quasi-Newton method on a sum of squares.** Quasi-Newton methods (BFGS, DFP, L-BFGS) approximate the Hessian using only gradient information; Gauss–Newton is the "build the approximation analytically out of $Df$" version, exploiting the sum-of-squares structure that quasi-Newton methods cannot. When the problem is *not* a sum of squares, Gauss–Newton has no analogue and one falls back to quasi-Newton.

**Gauss–Newton is iteratively reweighted least squares with weights set to one.** In Boyd Exercise 18.3, when the residual has the form $f_i(x) = \phi_i(a_i^T x - b_i)$, the Jacobian becomes $Df(x) = \operatorname{diag}(d) A$ with $d_i = \phi_i'(r_i)$, and the Gauss–Newton subproblem is a *weighted* linear least squares problem with weights $d_i$ that change each iteration. This is the **iteratively reweighted least squares (IRLS)** algorithm — one of the standard algorithms for generalized linear models. So Gauss–Newton specializes to IRLS in this common case.

**True name.** The operational characterization of Gauss–Newton is: *use the Jacobian self-product $Df^T Df$ in place of the true Hessian, and iterate Newton's update*. This characterization makes precise the algorithm's domain of validity (zero-residual or small-residual problems) and its computational savings (no second derivatives needed). The textbook description "linearize and solve linear LS" is the implementation-level view; the Hessian-approximation view is the structural one.

---

# Examples / Corollaries

**Example 1 (Newton for $n = 1$).** For $f : \mathbb{R} \to \mathbb{R}$, the Gauss–Newton (= Newton) update is
$$x^{(k+1)} = x^{(k)} - f(x^{(k)})/f'(x^{(k)}),$$
the familiar scalar Newton iteration. Quadratic convergence near a simple zero $\hat x$ of $f$ is the classical theorem.

**Example 2 (root of $x^2 - 2$).** With $f(x) = x^2 - 2$, $f'(x) = 2x$, starting from $x^{(1)} = 1$, the Newton iteration is $x^{(k+1)} = x^{(k)} - (x^{(k)2} - 2)/(2 x^{(k)}) = (x^{(k)} + 2/x^{(k)})/2$. The first few iterates: $1 \to 1.5 \to 1.4167 \to 1.4142156... \to \sqrt 2$, showing the doubling of correct digits per step (quadratic convergence) once near the root.

**Example 3 (linear least squares as a degenerate case).** If $f(x) = Ax - b$ is affine, then $Df(x) = A$ is constant, and Gauss–Newton from any starting point gives
$$x^{(2)} = x^{(1)} - (A^T A)^{-1} A^T (A x^{(1)} - b) = (A^T A)^{-1} A^T b,$$
the exact linear least squares solution in *one step*. So nonlinear methods reduce to linear methods on linear problems.

**Non-example 1 (rank-deficient Jacobian).** Take $f(x_1, x_2) = (x_1 - x_2, x_1 - x_2)$ at $x = (0, 0)$. The Jacobian is $\begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}$, which has rank $1$. Then $Df^T Df = \begin{pmatrix} 2 & -2 \\ -2 & 2 \end{pmatrix}$ is singular, and the Gauss–Newton step is *undefined*. The algorithm terminates with an error here. This is the rank-deficiency failure mode that Levenberg–Marquardt repairs.

**Non-example 2 (divergent iteration on the sigmoid).** With $f(x) = (e^x - e^{-x})/(e^x + e^{-x})$ (the $\tanh$ function), the unique zero is $\hat x = 0$. From $x^{(1)} = 1.15$, the Newton update is
$$x^{(2)} = x^{(1)} - f(x^{(1)})/f'(x^{(1)}) = 1.15 - \frac{0.818}{0.331} \approx -1.32,$$
which is *further* from zero than $1.15$. Iterating produces $-1.32 \to 1.71 \to -2.5 \to \cdots$, diverging exponentially. The cause: the Taylor approximation of $\tanh$ at $x = 1.15$ extrapolates to a zero far from the true zero, and the algorithm chases the bad extrapolation. (Compare: from $x^{(1)} = 0.95$, the algorithm converges quickly. The basin of attraction is small.)

**Corollary (one-step exactness on affine residuals).** If $f$ is affine, $f(x) = Ax + c$ with $A$ full column rank, then Gauss–Newton converges in one iteration from any starting point. *Proof:* The Jacobian is the constant $A$, the affine approximation $\hat f(x; x^{(k)})$ equals $f(x)$ identically, so the linearized subproblem *is* the original problem; one iteration solves it.

**Corollary (zero-residual local fixed point).** If $f(\hat x) = 0$ and $Df(\hat x)$ has full column rank, then $\hat x$ is a fixed point of Gauss–Newton: starting at $x^{(k)} = \hat x$ gives $x^{(k+1)} = \hat x$ by the formula. Combined with the convergence theorem ([[Thm - Local Convergence of Gauss-Newton]]), this shows that Gauss–Newton is locally consistent at zero-residual minima.

**Calibration check.** A reader who has understood Gauss–Newton should be able to: (i) write down the explicit Gauss–Newton update for $f(x_1, x_2) = (x_1^2 + x_2^2 - 1, x_1 - x_2)$ at $x^{(1)} = (1, 0)$ and compute $x^{(2)}$; (ii) recognize that this is exactly Newton's method on $f(x) = 0$ since $m = n = 2$; (iii) explain in one sentence why the algorithm would terminate with an error if the Jacobian were $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.

---

# Unlocked by This

> [!tip] Iteratively Reweighted Least Squares *(from Statistics)*
> The form $f_i(x) = \phi_i(a_i^T x - b_i)$ — a scalar nonlinearity composed with an affine map — appears throughout statistical estimation. Gauss–Newton on this form is **iteratively reweighted least squares (IRLS)**: each iteration is a *weighted* linear least squares problem with weights $d_i = \phi'_i(r_i)$ computed at the current residuals. IRLS is the standard algorithm for fitting **generalized linear models** (Poisson regression, logistic regression with the standard log-likelihood loss, robust regression with Huber loss). Recognizing IRLS as a special case of Gauss–Newton unlocks the connection between linear LS, weighted linear LS, and the entire GLM toolkit.

> [!tip] Quasi-Newton Methods *(from Optimization)*
> **Quasi-Newton methods** (BFGS, L-BFGS, DFP) maintain an approximation $H^{(k)}$ to the Hessian, updated each iteration using only gradient evaluations. Gauss–Newton is the special analytic instance for sum-of-squares objectives, with $H = Df^T Df$ obtained directly from the Jacobian. The general theory of quasi-Newton — Sherman–Morrison rank-one updates, secant conditions, BFGS as the optimal "minimum-change" symmetric positive-definite update — generalizes Gauss–Newton to arbitrary smooth objectives. L-BFGS, which stores only a few past gradient pairs, is the algorithm of choice when even the Gauss–Newton matrix is too large to form.
