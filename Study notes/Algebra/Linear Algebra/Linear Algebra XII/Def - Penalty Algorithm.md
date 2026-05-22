---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Constrained Nonlinear Least Squares"
  - "Def - Levenberg-Marquardt Algorithm"
  - "Def - Nonlinear Least Squares Problem"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation

Throughout, $f : \mathbb{R}^n \to \mathbb{R}^m$ is the residual map and $g : \mathbb{R}^n \to \mathbb{R}^p$ the equality-constraint map of the [[Def - Constrained Nonlinear Least Squares|constrained nonlinear LS problem]] $\min \|f(x)\|^2$ subject to $g(x) = 0$. The **penalty parameter** at iteration $k$ is denoted $\mu^{(k)} > 0$. The full symbol registry is on [[Linear Algebra XII — Applied III — Nonlinear Least Squares]].

---

# Axiom Motivation

We have a [[Def - Constrained Nonlinear Least Squares|constrained nonlinear least squares problem]] and a working algorithm — [[Def - Levenberg-Marquardt Algorithm|Levenberg–Marquardt]] — for the *unconstrained* case. The cleanest possible way to make the constraint disappear is to convert it into an additional residual.

The constraint $g(x) = 0$ says: at the solution, $\|g(x)\|^2$ should be zero. So suppose we add $\mu \|g(x)\|^2$ to the objective, where $\mu > 0$ is a parameter. The new objective is
$$\phi_\mu(x) = \|f(x)\|^2 + \mu \|g(x)\|^2.$$
For very large $\mu$, any $x$ with $g(x) \neq 0$ has a hugely inflated objective, so the minimizer is forced toward feasibility — toward $g(x) = 0$. In the limit $\mu \to \infty$, the minimizer of $\phi_\mu$ should converge to the solution of the original constrained problem.

This is a clean idea, and it works in principle. The composite objective is itself a sum of squares — it equals $\|h_\mu(x)\|^2$ where $h_\mu(x) = (f(x), \sqrt\mu \, g(x))$ is the stacked residual map — so Levenberg–Marquardt applied to $h_\mu$ minimizes it. Then increase $\mu$ and repeat with the previous solution as the warm-start, and continue until $\|g(x)\|$ is small enough to call the constraint satisfied. That is the **penalty algorithm**.

So why is there a *second* constrained algorithm in this chapter ([[Def - Augmented Lagrangian Algorithm|the augmented Lagrangian]]) that is harder to derive but used in practice instead? Because the penalty algorithm has a fundamental numerical problem.

To enforce the constraint to a tight tolerance — say, $\|g(\hat x)\| < 10^{-6}$ — we need $\mu$ to be very large, perhaps $10^{10}$ or more. At that scale, the stacked residual $h_\mu(x) = (f(x), \sqrt\mu \, g(x))$ has *two blocks of vastly different scale*: the original residuals $f_i(x)$ have magnitudes $\sim 1$, but the penalty residuals $\sqrt\mu \, g_j(x)$ have magnitudes $\sim 10^5 \, g_j(x)$. The Jacobian $Dh_\mu$ has the same block structure — top $m$ rows from $Df$, bottom $p$ rows scaled by $\sqrt\mu$. The condition number of the inner linear LS subproblem scales with $\sqrt\mu$, so by the time $\mu$ has grown large enough to enforce the constraint, the inner Levenberg–Marquardt subproblems are *catastrophically ill-conditioned*: the linear-LS solves return inaccurate steps, the algorithm stalls, and even with double-precision arithmetic the constraint cannot be driven below $\sim 10^{-8}$.

This is a real practical problem, not a theoretical concern. The penalty algorithm cannot achieve tight constraint satisfaction without losing accuracy on the objective and stalling. The constraint and the objective are in numerical tension: as $\mu$ grows, the algorithm focuses ever more exclusively on the constraint and loses sight of the objective.

Why include the penalty algorithm in the textbook if it has this flaw? Three reasons. First, it is the *natural first guess* — anyone presented with a constrained problem and an unconstrained solver would invent it within minutes — and understanding why it underperforms is a precondition for appreciating the augmented Lagrangian fix. Second, the penalty algorithm is *pedagogically clean*: there is one outer-loop parameter to track ($\mu$), one heuristic for updating it (double per iteration), and one algorithm in the inner loop (Levenberg–Marquardt). Third, the penalty algorithm is the *limiting case* of the augmented Lagrangian when the multiplier estimate is set to zero ($z^{(k)} \equiv 0$); recognizing this connection makes the augmented Lagrangian seem like an "obvious extension" rather than a separate invention.

The update rule for $\mu$ is similarly the simplest possible: **double per iteration**. Start with $\mu^{(1)} = 1$, set $\mu^{(k+1)} = 2 \mu^{(k)}$, and stop when $\|g(x^{(k)})\|$ is small enough. This rule has no adaptivity — unlike Levenberg–Marquardt's adaptive $\lambda$, which responds to step success or failure — and so the penalty algorithm has fewer parameters to tune but also fewer levers to pull. Sophisticated penalty methods adapt $\mu$ based on constraint-residual progress, but the basic version is just geometric growth.

Two implementation notes. First, **warm-start the inner Levenberg–Marquardt at the previous outer iterate**: the change in objective from iteration $k$ to $k+1$ is small (only $\mu$ changed), so the previous solution is a good starting point. Without warm-starting, the algorithm wastes iterations re-discovering progress already made. Second, **terminate the inner Levenberg–Marquardt early**: at moderate $\mu$ there is no need to solve the inner problem to high accuracy because the outer problem will change $\mu$ next iteration anyway. The standard rule is to run a few Levenberg–Marquardt iterations per outer step, just enough to make meaningful progress.

---

# The Definition

The **penalty algorithm** for the [[Def - Constrained Nonlinear Least Squares|constrained nonlinear least squares problem]] $\min \|f(x)\|^2$ s.t. $g(x) = 0$ generates iterates $x^{(2)}, x^{(3)}, \ldots$ from a starting point $x^{(1)}$ by minimizing a sequence of unconstrained penalized objectives.

> **Algorithm 19.1 (Penalty algorithm).** Given $f, g$, $x^{(1)}$. Set $\mu^{(1)} = 1$.
> For $k = 1, 2, \ldots, k_\max$:
> 1. *Solve unconstrained subproblem.* Set $x^{(k+1)}$ as the (approximate) minimizer of
> $$\|f(x)\|^2 + \mu^{(k)} \|g(x)\|^2,$$
> using [[Def - Levenberg-Marquardt Algorithm|Levenberg–Marquardt]], starting from $x^{(k)}$.
> 2. *Increase penalty:* $\mu^{(k+1)} = 2 \mu^{(k)}$.

Terminate early when $\|g(x^{(k)})\|$ is below a desired tolerance (the constraint is approximately satisfied).

**The inner subproblem as a stacked nonlinear LS problem.** The composite objective $\|f(x)\|^2 + \mu^{(k)} \|g(x)\|^2$ is the squared norm of the stacked residual
$$h_{\mu^{(k)}}(x) = \begin{pmatrix} f(x) \\ \sqrt{\mu^{(k)}}\, g(x) \end{pmatrix} \in \mathbb{R}^{m + p}.$$
So step 1 is exactly the unconstrained nonlinear LS problem $\min \|h_{\mu^{(k)}}(x)\|^2$, solved by Levenberg–Marquardt with Jacobian
$$Dh_{\mu^{(k)}}(x) = \begin{pmatrix} Df(x) \\ \sqrt{\mu^{(k)}}\, Dg(x) \end{pmatrix}.$$

**Implicit Lagrange multiplier estimate.** At the inner-loop minimum $x^{(k+1)}$, the optimality condition of the unconstrained subproblem reads
$$2 Df(x^{(k+1)})^T f(x^{(k+1)}) + 2 \mu^{(k)} Dg(x^{(k+1)})^T g(x^{(k+1)}) = 0.$$
Comparing with the constrained KKT stationarity $2 Df^T f + Dg^T \hat z = 0$, we see that the penalty algorithm *implicitly* uses the multiplier estimate
$$z^{(k+1)} := 2 \mu^{(k)} g(x^{(k+1)}).$$
This is a quantity the user can read off from the iterates; it converges to the true Lagrange multiplier $\hat z$ as $k \to \infty$ (see [[Thm - Convergence of Penalty Algorithm]]).

**Drawback: ill-conditioning.** The condition number of $Dh_{\mu^{(k)}}^T Dh_{\mu^{(k)}}$ scales like $\mu^{(k)}$ as $\mu^{(k)} \to \infty$. Inner Levenberg–Marquardt accuracy degrades correspondingly; in IEEE double precision the practical ceiling is $\mu \sim 10^{12}$. This is the structural flaw that motivates the [[Def - Augmented Lagrangian Algorithm|augmented Lagrangian algorithm]].

---

# Relate to Other Fields / Compression

The penalty algorithm is the simplest member of the **exterior penalty method** family in nonlinear programming. "Exterior" refers to the fact that the iterates are generally *infeasible* — $g(x^{(k)}) \neq 0$ — and approach feasibility from outside the constraint set as $\mu \to \infty$. There is a parallel family of **interior penalty methods** (also called **barrier methods**), where the penalty is constructed to keep iterates strictly inside an inequality-constrained feasible region; **interior point methods** for linear and convex programming are a refinement of this idea.

The penalty algorithm is a **homotopy method**: it traces a continuous family of unconstrained problems parametrized by $\mu$, with the constrained problem as the $\mu \to \infty$ endpoint. The homotopy is followed approximately by warm-starting each new subproblem at the previous solution. More sophisticated homotopy methods would solve a continuous ODE describing how the optimizer changes with $\mu$, but the discrete penalty algorithm is much simpler and often sufficient.

From the angle of **statistics / regularization**, the penalty $\mu \|g(x)\|^2$ added to $\|f(x)\|^2$ is structurally identical to **Tikhonov regularization** with $g(x)$ as the "regularization residual." In this view, the penalty algorithm interprets the equality constraint as "the regularization term we want to drive to zero." The hyperparameter sweep over $\mu$ that regularization theory uses to balance fit and regularization is here used to drive regularization to dominate fit — pushing $\|g\|^2$ all the way to zero.

**True name.** The operational characterization of the penalty algorithm is: *replace the constrained problem by an unconstrained problem with the squared constraint added as a penalty, and drive the penalty weight to infinity.* The compactness of this statement makes the idea irresistible to anyone seeing constrained optimization for the first time; the chapter's emphasis on the augmented Lagrangian as the better alternative is the lesson that the obvious idea is not the right one.

---

# Examples / Corollaries

**Example 1 (quadratic objective, linear constraint).** Minimize $(x_1 - 1)^2 + (x_2 - 1)^2$ subject to $x_1 + x_2 = 1$. The penalty objective is $(x_1 - 1)^2 + (x_2 - 1)^2 + \mu (x_1 + x_2 - 1)^2$. Setting partial derivatives to zero gives a $2 \times 2$ linear system whose solution is
$$x_1 = x_2 = \frac{2 + \mu}{2 + 4\mu}.$$
As $\mu \to \infty$, $x_1 = x_2 \to 1/4 + 1/4 = 1/2$, the constrained optimum. The implicit multiplier $z = 2\mu(x_1 + x_2 - 1) = 2\mu \cdot \frac{-1}{1 + 2\mu} = \frac{-2\mu}{1 + 2\mu} \to -1$, the true Lagrange multiplier. (See [[Ex - Penalty method on a quadratic with linear constraint]].)

**Example 2 (Boyd two-variable nonlinear).** The example in Boyd §19.3 with $f(x_1, x_2) = (x_1 + e^{-x_2}, x_1^2 + 2 x_2 + 1)$ and $g(x_1, x_2) = x_1 + x_1^3 + x_2 + x_2^2$. The penalty algorithm started at $(0.5, -0.5)$ with $\mu^{(1)} = 1$ doubles $\mu$ at each iteration. After six outer iterations, $\mu^{(6)} = 32$ and the iterate is close to the solution $\hat x = (0, 0)$, but constraint enforcement is loose. Compare with the augmented Lagrangian's $\mu$ remaining at $4$ throughout and achieving much tighter constraint satisfaction (see [[Def - Augmented Lagrangian Algorithm]]).

**Example 3 (warm-starting matters).** Without warm-starting (each inner LM run started from a generic initial point), the penalty algorithm spends $\Omega(k)$ iterations per outer step even when the iterate barely changes between $\mu^{(k)}$ and $\mu^{(k+1)}$. With warm-starting (each inner LM started from the previous outer-iterate solution), 1–3 inner iterations suffice. The total iteration count drops by a factor of 5–10 in typical applications.

**Non-example 1 (small $\mu$ does not enforce the constraint).** Setting $\mu = 1$ and stopping makes the constraint contribute $\|g(x)\|^2$ to the objective with weight $1$ — barely more than the original residuals. The unconstrained minimizer of $\|f\|^2 + \|g\|^2$ is generally *not* feasible. The penalty algorithm requires the *outer loop* (growing $\mu$); a single inner LM run with finite $\mu$ does not solve the constrained problem.

**Non-example 2 (large initial $\mu$ defeats the algorithm).** Starting with $\mu^{(1)} = 10^{12}$ immediately puts the inner LM subproblem in the ill-conditioned regime, and the algorithm cannot make accurate progress. The geometric growth $\mu^{(1)} = 1, \mu^{(2)} = 2, \ldots$ is essential precisely because it allows the algorithm to gain accuracy at small $\mu$ first, then refine.

**Corollary (limit point is a constrained stationary point).** Under suitable regularity, if $x^{(k)} \to \hat x$ and $\mu^{(k)} \to \infty$, then $\hat x$ satisfies the constrained KKT stationarity condition with multiplier $\hat z = \lim 2 \mu^{(k)} g(x^{(k+1)})$, and $g(\hat x) = 0$. *Proof sketch:* the inner optimality condition rearranges to $2 Df^T f + Dg^T (2\mu g) = 0$, and the bracketed quantity is $z^{(k+1)}$; taking limits gives the KKT condition. The full statement appears as [[Thm - Convergence of Penalty Algorithm]].

**Calibration check.** A reader who has understood the penalty algorithm should: (i) write down the explicit stacked-residual Jacobian for $f(x_1, x_2) = (x_1 - 1, x_2 - 1)$ and $g(x_1, x_2) = x_1 + x_2 - 1$ with $\mu = 100$; (ii) compute the condition number of $Dh^T Dh$ for that example and observe it scales linearly in $\mu$; (iii) explain in one sentence why driving $\mu$ to $10^{16}$ is hopeless even in exact arithmetic if the inner LM has to converge.

---

# Unlocked by This

> [!tip] Barrier Methods and Interior Point Algorithms *(from Convex Optimization)*
> The penalty algorithm's "exterior" approach has a parallel "interior" version: for inequality constraints $h_j(x) \leq 0$, add the **logarithmic barrier** $-t \sum_j \log(-h_j(x))$ to the objective. As $t \to 0$, the modified problem's solution approaches the inequality-constrained optimum, but iterates remain *strictly feasible* throughout. This is the **interior point method**, the workhorse of modern convex programming (linear, quadratic, semidefinite programs). The connection to penalty: both methods convert constraints into a continuous family of unconstrained problems indexed by a homotopy parameter, with the constrained solution as a limit.

> [!tip] Augmented Lagrangian as Penalty Plus Multiplier *(from Optimization)*
> The penalty algorithm's flaw — requiring $\mu \to \infty$ for constraint satisfaction — is fixed by *also* tracking the Lagrange multiplier estimate. The [[Def - Augmented Lagrangian Algorithm|augmented Lagrangian algorithm]] adds $z^T g(x)$ to the penalty objective, where $z$ is updated to converge to the true Lagrange multiplier. This single addition keeps $\mu$ bounded and the inner subproblems well-conditioned. The conceptual lesson: *if you absorb the part of the constraint that "wants" the multiplier into a separate update, the penalty term only has to handle the residual.*
