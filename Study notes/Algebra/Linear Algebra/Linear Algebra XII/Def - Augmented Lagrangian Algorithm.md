---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Constrained Nonlinear Least Squares"
  - "Def - Penalty Algorithm"
  - "Def - Levenberg-Marquardt Algorithm"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation

Throughout, $f : \mathbb{R}^n \to \mathbb{R}^m$ is the residual map, $g : \mathbb{R}^n \to \mathbb{R}^p$ the equality-constraint map, and we wish to solve $\min \|f(x)\|^2$ subject to $g(x) = 0$. The **Lagrange multiplier** estimate at iteration $k$ is $z^{(k)} \in \mathbb{R}^p$, and the **penalty parameter** is $\mu^{(k)} > 0$. The **Lagrangian** is $L(x, z) = \|f(x)\|^2 + g(x)^T z$. The **augmented Lagrangian** with penalty $\mu$ is
$$L_\mu(x, z) = L(x, z) + \mu \|g(x)\|^2 = \|f(x)\|^2 + g(x)^T z + \mu \|g(x)\|^2.$$
The full symbol registry is on [[Linear Algebra XII — Applied III — Nonlinear Least Squares]].

---

# Axiom Motivation

The [[Def - Penalty Algorithm|penalty algorithm]] succeeds in spirit but fails in practice because driving $\mu$ to infinity ill-conditions the inner subproblem. The diagnosis is sharp: at the constrained optimum, the KKT stationarity is
$$2 Df(\hat x)^T f(\hat x) + Dg(\hat x)^T \hat z = 0,$$
involving a *finite* Lagrange multiplier $\hat z$. The penalty algorithm enforces this approximately by setting $2 \mu^{(k)} g(x^{(k+1)}) \approx \hat z$ — that is, the role of $\hat z$ is played by $2 \mu^{(k)} g(x^{(k+1)})$. For $\hat z$ of finite magnitude and $g(x^{(k+1)}) \to 0$, the product $2 \mu^{(k)} g(x^{(k+1)})$ stays finite — but only if $\mu^{(k)} \to \infty$ exactly fast enough to compensate the shrinking of $g$. This is the source of the ill-conditioning: we are using $\mu$ to manufacture a Lagrange-multiplier-like quantity that is *inherent to the problem* and could in principle be tracked directly.

The fix is to **track the Lagrange multiplier directly**. Maintain a running estimate $z^{(k)}$ of $\hat z$, and modify the inner subproblem so that, at the inner optimum, the *correct* KKT-like condition holds with the *current* multiplier estimate. Specifically, define the **augmented Lagrangian**
$$L_\mu(x, z) = \|f(x)\|^2 + g(x)^T z + \mu \|g(x)\|^2,$$
and at each outer iteration *minimize $L_{\mu^{(k)}}(x, z^{(k)})$ over $x$* for the current values of $\mu^{(k)}$ and $z^{(k)}$. Then update $z^{(k+1)}$ to track the multiplier.

The motivation for the augmented Lagrangian is twofold.

**First**, $L_\mu(x, z) = L(x, z) + \mu \|g(x)\|^2$ is just the Lagrangian augmented by the penalty term — hence the name. It interpolates between two extremes: $\mu = 0$ gives the ordinary Lagrangian (whose saddle points are the KKT solutions but which is unsuitable for direct minimization), and $z = 0$ gives the pure penalty objective $\|f\|^2 + \mu \|g\|^2$. The full $L_\mu(x, z)$ is suitable for minimization (the $\mu \|g\|^2$ term makes the problem convex in $x$ near the solution) *and* tracks the Lagrange multiplier (the $z$ term ensures the inner KKT condition involves a finite multiplier).

**Second**, the augmented Lagrangian admits an exact identity (Boyd Eq 18.8):
$$L_\mu(x, z) = \|f(x)\|^2 + \mu \|g(x) + z/(2\mu)\|^2 - \mu \|z/(2\mu)\|^2,$$
where the last term is a constant in $x$. So minimizing $L_\mu(x, z)$ over $x$ is *exactly* minimizing $\|f(x)\|^2 + \mu \|g(x) + z/(2\mu)\|^2$, which is the squared norm of the stacked residual $h(x) = (f(x), \sqrt{\mu}(g(x) + z/(2\mu)))$. This is again an unconstrained nonlinear LS problem, solvable by Levenberg–Marquardt — *with the same conditioning as the penalty algorithm's inner subproblem at penalty parameter $\mu$*. The augmented Lagrangian *does not* change the inner subproblem's conditioning at fixed $\mu$; what it changes is the *requirement that $\mu \to \infty$*. By tracking the multiplier directly, $\mu$ can stay moderate, so the inner subproblem stays well-conditioned.

How to update $z$? The right rule is suggested by the KKT structure itself. The inner-loop optimality condition for the augmented Lagrangian is
$$0 = 2 Df(\tilde x)^T f(\tilde x) + Dg(\tilde x)^T \tilde z, \quad \text{where} \quad \tilde z := z + 2 \mu g(\tilde x).$$
Compare this to the constrained KKT stationarity: it is exactly the same equation, but with $\tilde z$ playing the role of the Lagrange multiplier. So **the inner-loop minimum satisfies the KKT stationarity condition exactly, with multiplier $z + 2\mu g(x)$**. If we *update* the multiplier estimate by
$$z^{(k+1)} = z^{(k)} + 2 \mu^{(k)} g(x^{(k+1)}),$$
then $z^{(k+1)}$ is the value of $\tilde z$ at the inner-loop minimum — and this is the value that makes the KKT condition hold at $x^{(k+1)}$. So as the algorithm proceeds, the pair $(x^{(k+1)}, z^{(k+1)})$ exactly satisfies the KKT *stationarity*, and the only obstacle to optimality is the *feasibility* condition $g(x) = 0$, which the iteration drives down.

This is the deepest single observation of the chapter: **the multiplier update $z \leftarrow z + 2\mu g(x)$ is exactly the rule that makes each inner-loop minimum simultaneously satisfy the KKT stationarity condition with the updated multiplier estimate.** It is also (and this is one and the same fact) **gradient ascent on the Lagrangian dual function** $\phi(z) = \min_x L_\mu(x, z)$. The reason: by Danskin's theorem (envelope theorem), $\partial \phi / \partial z = g(\tilde x(z))$ where $\tilde x(z)$ is the minimizer of $L_\mu$ at $z$. So the multiplier update is a step of size $2\mu$ in the gradient direction of $\phi$. The $\mu$ in the multiplier update plays the role of *step size* in dual gradient ascent — too small a step is slow, too large a step is unstable, and the moderate $\mu$ that the algorithm keeps is the right balance.

The growth rule for $\mu$ is similarly elegant. Update $\mu$ only when the constraint residual fails to decrease fast enough: if $\|g(x^{(k+1)})\| < 0.25 \|g(x^{(k)})\|$ (the constraint shrunk by a factor of 4), keep $\mu^{(k+1)} = \mu^{(k)}$ — the current $\mu$ is sufficient. Otherwise double it: $\mu^{(k+1)} = 2 \mu^{(k)}$. This rule keeps $\mu$ as small as possible while ensuring constraint progress, which keeps the inner subproblem as well-conditioned as possible.

**Why this works where pure penalty fails.** The pure penalty algorithm uses $\mu$ to manufacture the multiplier role; the augmented Lagrangian tracks the multiplier separately. So the augmented Lagrangian achieves constraint enforcement with $\mu$ *moderate* — typically $\mu^{(k)}$ stabilizes at $O(1)$ or $O(10)$ rather than $O(10^{12})$. The inner Levenberg–Marquardt subproblems remain well-conditioned, and the algorithm achieves tight constraint satisfaction without the numerical breakdown of the pure penalty method.

---

# The Definition

The **augmented Lagrangian algorithm** for $\min \|f(x)\|^2$ s.t. $g(x) = 0$ generates iterates $x^{(2)}, x^{(3)}, \ldots$ and Lagrange multiplier estimates $z^{(2)}, z^{(3)}, \ldots$ from a starting point $x^{(1)}$ by minimizing the augmented Lagrangian over $x$ for the current $(z, \mu)$, then updating $z$ to drive feasibility and (conditionally) growing $\mu$.

> **Algorithm 19.2 (Augmented Lagrangian).** Given $f, g$, $x^{(1)}$. Set $z^{(1)} = 0$ and $\mu^{(1)} = 1$.
> For $k = 1, 2, \ldots, k_\max$:
> 1. *Solve unconstrained subproblem.* Set $x^{(k+1)}$ as the (approximate) minimizer of
> $$\|f(x)\|^2 + \mu^{(k)} \, \big\| g(x) + z^{(k)}/(2\mu^{(k)}) \big\|^2,$$
> using [[Def - Levenberg-Marquardt Algorithm|Levenberg–Marquardt]], starting from $x^{(k)}$.
> 2. *Update multiplier:* $z^{(k+1)} = z^{(k)} + 2 \mu^{(k)} \, g(x^{(k+1)})$.
> 3. *Conditionally update penalty:*
> $$\mu^{(k+1)} = \begin{cases} \mu^{(k)} & \text{if } \|g(x^{(k+1)})\| < 0.25\, \|g(x^{(k)})\|, \\ 2\, \mu^{(k)} & \text{otherwise.} \end{cases}$$

Terminate early when $\|g(x^{(k)})\|$ is below a desired tolerance.

**The key identity** (Boyd Eq 18.8): for any $z$ and $\mu > 0$,
$$L_\mu(x, z) = \|f(x)\|^2 + g(x)^T z + \mu \|g(x)\|^2 = \|f(x)\|^2 + \mu \|g(x) + z/(2\mu)\|^2 - \mu \|z/(2\mu)\|^2.$$
The last term is a constant in $x$, so minimizing $L_\mu(x, z)$ over $x$ at fixed $(z, \mu)$ is equivalent to minimizing
$$\|f(x)\|^2 + \mu \|g(x) + z/(2\mu)\|^2,$$
which is the unconstrained nonlinear LS problem solved by Levenberg–Marquardt in step 1.

**The KKT identity**: at the inner-loop minimum $\tilde x = x^{(k+1)}$, the optimality condition for the augmented subproblem is
$$2 Df(\tilde x)^T f(\tilde x) + Dg(\tilde x)^T (z^{(k)} + 2 \mu^{(k)} g(\tilde x)) = 0.$$
This is *exactly* the KKT stationarity condition for the constrained problem, with multiplier $z^{(k+1)} = z^{(k)} + 2\mu^{(k)} g(\tilde x)$. So the multiplier update in step 2 is precisely the rule that makes each pair $(x^{(k+1)}, z^{(k+1)})$ exactly satisfy the KKT stationarity condition. This is the result formalized in [[Thm - Augmented Lagrangian Recovers Lagrange Multipliers]].

**Initial conditions.** The standard initialization $z^{(1)} = 0$ makes the first outer iteration coincide with one step of the penalty algorithm at $\mu = 1$. Subsequent iterations diverge from pure penalty as the multiplier estimate accumulates.

---

# Relate to Other Fields / Compression

The augmented Lagrangian algorithm is also known as the **method of multipliers** (Hestenes 1969, Powell 1969 — the algorithm's two independent inventors). It is the conceptual ancestor of:

- **ADMM** (Alternating Direction Method of Multipliers): a variant for problems with separable structure $\min f(x) + g(y)$ s.t. $Ax + By = c$. ADMM alternates between minimization in $x$ and $y$, with the augmented Lagrangian multiplier update between them. It is the algorithm of choice for large-scale distributed optimization (consensus problems, regularized inverse problems, statistical learning at scale).
- **Sequential Quadratic Programming (SQP)**: at each iterate, SQP forms a quadratic-program subproblem whose KKT conditions match a Newton step on the constrained problem. The augmented Lagrangian's $\mu \|g\|^2$ term plays the role of *Hessian regularization* in SQP, ensuring the QP is convex.
- **Interior Point methods for nonlinear programming**: IPOPT, KNITRO, and related solvers combine a barrier-style treatment of inequality constraints with an augmented-Lagrangian-style treatment of equality constraints. The equality-only special case of these solvers is essentially the algorithm of this page.

From the angle of **convex optimization**, the augmented Lagrangian is the **proximal point method** applied to the dual problem. For convex problems with strong duality, the dual function $\phi(z) = \min_x L(x, z)$ is concave, and the augmented Lagrangian's multiplier update $z \leftarrow z + 2\mu g(\tilde x(z))$ is a gradient ascent step on $\phi$ with step size $2\mu$. The $\mu \|g\|^2$ term in $L_\mu$ converts the *gradient* ascent into a *proximal* gradient ascent, which has stability advantages (it converges for any positive step size, not just sufficiently small ones).

**True name.** The operational characterization of the augmented Lagrangian algorithm is: *alternate between (i) minimizing the augmented Lagrangian over $x$ for fixed multiplier $z$, and (ii) updating $z$ by gradient ascent on the dual, with the penalty $\mu$ controlling the dual step size and providing stability.* This characterization is precise and reveals the algorithm's place in the broader primal-dual landscape of nonlinear optimization.

---

# Examples / Corollaries

**Example 1 (Boyd two-variable nonlinear).** With $f(x_1, x_2) = (x_1 + e^{-x_2}, x_1^2 + 2 x_2 + 1)$ and $g(x_1, x_2) = x_1 + x_1^3 + x_2 + x_2^2$, the constrained minimum is $\hat x = (0, 0)$ with $\hat z = -2$. Starting from $x^{(1)} = (0.5, -0.5)$, $z^{(1)} = 0$, $\mu^{(1)} = 1$, the algorithm proceeds:
- Iteration 1: $x^{(2)} \approx (-0.04, 0.05)$, $z^{(2)} = -0.893$, $\mu^{(2)} = 2$ (constraint shrunk but not by factor 4).
- Iteration 2: $x^{(3)}$ closer to zero, $z^{(3)} = -1.569$, $\mu^{(3)} = 4$.
- Iteration 3: $x^{(4)}$ even closer, $z^{(4)} = -1.898$, $\mu^{(4)} = 4$ (constraint progress now adequate; $\mu$ stops growing).
- After 6 iterations, $z^{(6)} = -1.994 \approx \hat z = -2$, constraint $\|g\|$ is $\sim 10^{-6}$, $\mu$ remains at $4$.

Compare to pure penalty on the same problem: $\mu$ doubles at every iteration, reaching $32$ after 6 iterations, and constraint enforcement is looser despite the larger penalty. (See [[Ex - Penalty method on a quadratic with linear constraint]].)

**Example 2 (nonlinear control).** The car-steering problem of Boyd §19.4 with $N = 50$ time steps gives an augmented Lagrangian instance with hundreds of variables (states $x_2, \ldots, x_{N-1}$ and inputs $u_1, \ldots, u_N$) and hundreds of constraints (one per dynamics step). The augmented Lagrangian algorithm with sparsity-exploiting Levenberg–Marquardt inner solves converges in a handful of outer iterations to a feasible optimal trajectory.

**Example 3 ($z^{(1)} = 0$ makes the first iteration coincide with penalty).** With $z^{(1)} = 0$, the augmented Lagrangian objective in iteration 1 is exactly $\|f(x)\|^2 + \mu^{(1)} \|g(x)\|^2$ — the same as the penalty algorithm's first subproblem. The methods diverge from iteration 2 onward, as the multiplier estimate $z^{(2)} = 2\mu^{(1)} g(x^{(2)})$ enters the iteration-2 subproblem.

**Non-example 1 (constant $z^{(k)} \equiv 0$ is just the penalty algorithm).** If the multiplier update step is omitted (or implemented as $z^{(k+1)} = z^{(k)}$ always), the algorithm reduces to the penalty algorithm, inheriting its ill-conditioning. The multiplier update is essential.

**Non-example 2 (very small $\mu$ is unstable).** With $\mu^{(k)}$ very small, the multiplier update $z^{(k+1)} = z^{(k)} + 2\mu^{(k)} g$ takes tiny steps in $z$, and the algorithm converges slowly even though each inner subproblem is well-conditioned. The trade-off — moderate $\mu$ for moderate step size, moderate conditioning — is what the chapter's heuristic balances.

**Corollary (stationarity at each iterate).** As shown above, each pair $(x^{(k+1)}, z^{(k+1)})$ produced by the algorithm satisfies the KKT stationarity condition exactly (modulo inner-loop tolerance). The only condition the algorithm must drive to zero is the feasibility $g(x) = 0$. (See [[Thm - Augmented Lagrangian Recovers Lagrange Multipliers]].)

**Corollary (rate of multiplier convergence).** If the algorithm converges with $\mu^{(k)}$ bounded, then $z^{(k)} \to \hat z$ at a *linear* rate determined by the eigenvalues of the constraint Jacobian: $\|z^{(k+1)} - \hat z\| \leq \alpha \|z^{(k)} - \hat z\|$ with $\alpha < 1$ provided $\mu$ is large enough relative to the constraint curvature. The rate $\alpha$ improves as $\mu$ grows but the per-iteration cost stays the same — hence the heuristic of doubling $\mu$ only when constraint progress is slow.

**Calibration check.** A reader should: (i) write down the augmented Lagrangian for $\min (x - 1)^2 + (y - 1)^2$ s.t. $x + y = 1$ and verify by direct calculation that the algorithm with $z^{(1)} = 0$, $\mu^{(1)} = 1$ produces $x^{(2)} = y^{(2)} = 2/5$, $z^{(2)} = -2/5$ (using the multiplier update); (ii) check that after several iterations the multiplier converges to $\hat z = -1$ and the iterate to $(1/2, 1/2)$ *with $\mu$ staying at moderate values*; (iii) explain in one sentence why the pure penalty algorithm would need $\mu$ to grow without bound to achieve the same tolerance.

---

# Unlocked by This

> [!tip] ADMM (Alternating Direction Method of Multipliers) *(from Convex Optimization)*
> For problems with the separable structure $\min f(x) + h(y)$ s.t. $Ax + By = c$, **ADMM** alternates between minimization in $x$ (with $y, z$ fixed), minimization in $y$ (with $x, z$ fixed), and the augmented Lagrangian multiplier update. The decomposition decouples large problems into smaller subproblems that can be solved in parallel — making ADMM the algorithm of choice for distributed convex optimization at the scale of large machine learning, statistical inference, and consensus problems. ADMM specializes the augmented Lagrangian to the separable case and exploits the structure to gain parallelism.

> [!tip] Sequential Quadratic Programming *(from Optimization)*
> **SQP** is the direct generalization of Newton's method to constrained optimization. At each iterate, it forms the *quadratic program*
> $$\min \tfrac12 p^T H p + g^T p \quad \text{s.t.} \quad Dg(x^{(k)}) p + g(x^{(k)}) \leq 0,$$
> where $H$ is the Hessian of the Lagrangian (or an approximation) and $g$ its gradient. The QP solution gives the next step. For equality-only constraints, SQP coincides with Newton's method on the KKT system, with the augmented Lagrangian's $\mu \|g\|^2$ term playing the role of Hessian regularization to ensure the QP is convex. SQP and augmented Lagrangian are the two main families of practical NLP codes — SNOPT is the SQP exemplar, while LANCELOT is augmented Lagrangian.

> [!tip] Method of Multipliers for Convex Programming *(from Convex Optimization)*
> For *convex* objectives with strong duality, the augmented Lagrangian algorithm becomes the **method of multipliers** with global convergence guarantees. The dual function $\phi(z) = \min_x L(x, z)$ is concave, and the algorithm performs proximal gradient ascent on $\phi$. For strongly convex objectives, the rate of convergence on $z$ is linear with rate $1/(1 + 2\mu/\sigma)$ where $\sigma$ is the strong-convexity modulus — so growing $\mu$ accelerates convergence (until inner-subproblem cost becomes prohibitive). This is the foundation of many algorithms in convex programming, including dual decomposition and proximal point methods.
