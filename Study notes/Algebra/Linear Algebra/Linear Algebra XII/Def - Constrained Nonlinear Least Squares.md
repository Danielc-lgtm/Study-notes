---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Nonlinear Least Squares Problem"
  - "Def - Constrained Least Squares"
  - "Def - KKT System"
  - "Def - Partial Derivatives and the Jacobian Matrix"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation

Throughout, $f : \mathbb{R}^n \to \mathbb{R}^m$ is the differentiable **residual** map and $g : \mathbb{R}^n \to \mathbb{R}^p$ is the differentiable **equality-constraint** map. The Jacobians are $Df(x)$ ($m \times n$) and $Dg(x)$ ($p \times n$). The variable $x \in \mathbb{R}^n$ is **feasible** if $g(x) = 0$. The **Lagrange multiplier** is denoted $z \in \mathbb{R}^p$; one component per constraint. The **Lagrangian** is $L(x, z) = \|f(x)\|^2 + g(x)^T z$. The full symbol registry is on [[Linear Algebra XII — Applied III — Nonlinear Least Squares]].

---

# Axiom Motivation

The [[Def - Nonlinear Least Squares Problem|unconstrained nonlinear least squares problem]] minimizes $\|f(x)\|^2$ over all $x$. Suppose now we additionally require $x$ to satisfy a nonlinear equation $g(x) = 0$. The constrained problem is fundamentally different in three ways.

**First**, the search space is now a $(n-p)$-dimensional surface (assuming the constraint Jacobian $Dg$ has full row rank), not a full open subset of $\mathbb{R}^n$. The geometry is that of a *manifold* inside $\mathbb{R}^n$; the unconstrained minimum of $\|f\|^2$ is generally not on this surface, so the constrained minimum is determined by the interplay of objective gradient and constraint normal.

**Second**, the first-order optimality conditions change. For the unconstrained problem the condition was simply $\nabla \|f\|^2 = 0$. For the constrained problem, the **method of Lagrange multipliers** says: at a constrained minimum $\hat x$, the gradient of the objective is a *linear combination of the constraint gradients*. That is,
$$2 Df(\hat x)^T f(\hat x) = -Dg(\hat x)^T \hat z$$
for some vector $\hat z \in \mathbb{R}^p$. Geometrically: the gradient of the objective is perpendicular to the constraint surface — equivalently, parallel to the normal [[Def - Subspace|subspace]] spanned by the rows of $Dg$. The coefficients $\hat z_i$ are the **Lagrange multipliers**, with one per constraint. The combined system $g(\hat x) = 0$ and $2 Df^T f + Dg^T \hat z = 0$ is the **KKT (Karush–Kuhn–Tucker) system** for equality constraints; it generalizes the linear KKT system of [[Def - Constrained Least Squares|equality-constrained linear LS]] from [[Linear Algebra XI — Applied II — Least Squares|Topic XI]] to the nonlinear setting.

**Third**, there is no analogue of the normal equations. For the linear case $\min \|Ax - b\|^2$ s.t. $Cx = d$, the KKT system is a *linear* system of size $(n + p) \times (n + p)$ that can be solved in one step. For the nonlinear case, the KKT system is *nonlinear* in $x$ and $z$ jointly, and we must iterate.

The natural question: can we just apply Levenberg–Marquardt to the entire KKT system, treating $(x, z)$ as the joint unknown? In principle yes — this is what **sequential quadratic programming** (SQP) does — but the resulting algorithm has subtleties (the KKT system is a saddle point, not a minimum, so the algorithm must handle indefinite Hessians; and the multiplier $z$ has no obvious initialization). A more conceptually direct approach is to *convert the constrained problem into a sequence of unconstrained problems*, each of which Levenberg–Marquardt can solve directly. That is the strategy of the two algorithms in this section.

The **penalty algorithm** adds $\mu \|g(x)\|^2$ to the objective with $\mu \to \infty$, enforcing the constraint by making violations expensive. The **augmented Lagrangian algorithm** adds both the penalty $\mu \|g(x)\|^2$ *and* a Lagrange-multiplier term $z^T g(x)$ — and updates $z$ across outer iterations to track the true Lagrange multiplier. Both algorithms produce a sequence of unconstrained subproblems, each solvable by Levenberg–Marquardt, with constraint enforcement emerging from the outer-loop dynamics.

Why have *two* algorithms when we could just present the better one? Because the penalty algorithm is conceptually transparent — it converts constraints into a single composite objective in the most obvious way — and it exhibits the precise failure mode (ill-conditioning at large $\mu$) that the augmented Lagrangian repairs. Understanding the penalty algorithm makes the design of the augmented Lagrangian inevitable.

The constraint Jacobian $Dg(\hat x)$ is required to have **full row rank** at the constrained minimum for the Lagrange multiplier $\hat z$ to be unique (the **linear independence constraint qualification**, LICQ). If the constraints are linearly dependent at $\hat x$ — for instance, two constraints coincide — the multiplier is not uniquely determined and the standard KKT theory does not apply. In practical applications one ensures LICQ by formulating the constraints with care.

Why **only equality constraints**, not inequalities? Inequality constraints $g_i(x) \leq 0$ introduce two new ingredients: *active sets* (which constraints are tight at the minimum) and *complementary slackness* ($z_i \geq 0$ with $z_i = 0$ if $g_i(\hat x) < 0$, $g_i(\hat x) = 0$ if $z_i > 0$). The algorithms in this chapter handle equalities only. For inequality-constrained nonlinear LS, the standard tools are **sequential quadratic programming** (SQP) and **interior point methods** — both generalize the equality-only algorithms here.

---

# The Definition

The **equality-constrained nonlinear least squares problem** with residual map $f : \mathbb{R}^n \to \mathbb{R}^m$ and constraint map $g : \mathbb{R}^n \to \mathbb{R}^p$ is the optimization problem

$$\min_{x \in \mathbb{R}^n} \; \|f(x)\|^2 \quad \text{subject to} \quad g(x) = 0.$$

A point $x$ is **feasible** if $g(x) = 0$. A **solution** is a feasible local minimizer: a point $\hat x$ with $g(\hat x) = 0$ and $\|f(\hat x)\|^2 \leq \|f(x)\|^2$ for all feasible $x$ in a neighborhood of $\hat x$.

The **Lagrangian** is the scalar function
$$L(x, z) = \|f(x)\|^2 + g(x)^T z = \|f(x)\|^2 + \sum_{i=1}^p z_i g_i(x),$$
where $z \in \mathbb{R}^p$ is the **Lagrange multiplier vector**.

The **first-order optimality conditions** (KKT conditions for equality-constrained problems) at a solution $\hat x$ are: there exists a Lagrange multiplier $\hat z \in \mathbb{R}^p$ such that
$$\text{(stationarity)} \quad 2\, Df(\hat x)^T f(\hat x) + Dg(\hat x)^T \hat z = 0,$$
$$\text{(feasibility)} \quad g(\hat x) = 0.$$

These conditions are necessary at a solution provided the **linear independence constraint qualification (LICQ)** holds: the rows of $Dg(\hat x)$ are linearly independent (equivalently, $Dg(\hat x)$ has full row rank $p$, requiring $p \leq n$). The conditions are not sufficient: stationary points include saddle points and local maxima.

**Linear special case.** When $f(x) = Ax - b$ and $g(x) = Cx - d$ are affine, the problem reduces to the linear [[Def - Constrained Least Squares|equality-constrained least squares]] of [[Linear Algebra XI — Applied II — Least Squares|Topic XI]], with closed-form solution via the [[Def - KKT System|KKT system]]
$$\begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix} \begin{pmatrix} \hat x \\ \hat z \end{pmatrix} = \begin{pmatrix} 2 A^T b \\ d \end{pmatrix}.$$

**Nonlinear case.** When $f$ or $g$ is nonlinear, no closed-form solution exists. The two standard heuristic algorithms — [[Def - Penalty Algorithm|the penalty algorithm]] and [[Def - Augmented Lagrangian Algorithm|the augmented Lagrangian algorithm]] — solve the constrained problem by converting it into a sequence of unconstrained nonlinear least squares subproblems, each handled by [[Def - Levenberg-Marquardt Algorithm|Levenberg–Marquardt]].

---

# Relate to Other Fields / Compression

The equality-constrained nonlinear LS problem is the natural generalization of [[Def - Constrained Least Squares|linear equality-constrained LS]] obtained by allowing both the objective and the constraints to be nonlinear in $x$. The structural parallel is exact: in both cases the first-order conditions are gradient stationarity plus feasibility, the Lagrange multipliers play the role of "the cost of enforcing each constraint," and the linear case is the one-step computable specialization.

From the angle of **constrained optimization theory**, this is a special case of the **general nonlinear program** (NLP)
$$\min \phi(x) \quad \text{s.t.} \quad g_i(x) = 0, \quad h_j(x) \leq 0.$$
Our problem has $\phi(x) = \|f(x)\|^2$, equality constraints $g_i$, and no inequality constraints. The KKT conditions for the general NLP include complementary slackness for the inequalities; for the equality-only case they reduce to the conditions stated above.

From the angle of **mechanical equilibrium and physics**, equality-constrained optimization arises naturally whenever a system minimizes an energy subject to conservation laws (mass, momentum, energy) or geometric constraints (rigid-body constraints, contact). The constraints encode "what physics insists must hold," and the Lagrange multipliers are the *forces* that enforce those constraints. In a rigid body simulation, the constraint $g_i(x) = 0$ might say "the distance between particles $a$ and $b$ is fixed," and the multiplier $z_i$ is the constraint force along that bond.

From the angle of **statistical estimation**, equality constraints often encode known structural relationships among parameters: a probability vector summing to 1, a covariance matrix being positive definite, a model parameter satisfying a physical law. Constrained maximum likelihood is exactly the application of these algorithms to statistical models with structural constraints.

**True name.** The operational characterization of the constrained nonlinear LS problem is: *the joint $(x, z)$ that satisfies both the KKT stationarity and the feasibility condition.* The "minimize subject to" framing is the problem statement; the KKT-system characterization is the working definition that every algorithm in the chapter tracks.

---

# Examples / Corollaries

**Example 1 (parameter estimation with a normalization constraint).** Fit a probabilistic model parametrized by $\theta = (\theta_1, \ldots, \theta_p)$ with the constraint $\sum_i \theta_i = 1$ (a probability simplex constraint). The residuals come from the model fit; the constraint $g(\theta) = \mathbf{1}^T \theta - 1 = 0$ is linear (so this is technically a linearly-constrained nonlinear LS problem and Levenberg–Marquardt handles it directly without an outer loop).

**Example 2 (nonlinear control).** Steer a car from initial state $x_1 = (0, 0, 0)$ to final state $x_N = (1, 0, 0)$ over $N$ time steps. The variables are the input sequence $u_1, \ldots, u_{N-1}$ and the intermediate states $x_2, \ldots, x_{N-1}$. The residual is the control cost $\sum_k \|u_k\|^2 + \gamma \|u_{k+1} - u_k\|^2$ (smoothness penalty). The constraints are the dynamics $x_{k+1} - f(x_k, u_k) = 0$ for each $k$ — *nonlinear* in $x_k$ and $u_k$. The constrained NLS problem is solved by the augmented Lagrangian algorithm. (See [[Ex - Nonlinear control with augmented Lagrangian]].)

**Example 3 (equilibrium with conservation).** Find a chemical equilibrium where species concentrations $c_i$ minimize a free energy $\phi(c)$ subject to conservation $A c = b$ (atom-balance equations). With $\phi(c) = c^T \log c$ (nonlinear), constraints linear. Algorithm: penalty or augmented Lagrangian, with each inner subproblem solved by Levenberg–Marquardt.

**Non-example 1 (no constraint).** If $g$ is absent ($p = 0$), the problem is the unconstrained nonlinear LS of [[Def - Nonlinear Least Squares Problem]] and the algorithms of this section are not needed.

**Non-example 2 (linear in everything).** If $f, g$ are both affine, the closed-form KKT-system solution from [[Linear Algebra XI — Applied II — Least Squares|Topic XI]] applies and no iteration is needed. The algorithms here are designed for the truly nonlinear setting.

**Non-example 3 (inequality constraints).** If the constraints are $g(x) \leq 0$ rather than $g(x) = 0$, the KKT conditions include complementary slackness and the algorithms of this chapter do not directly apply. **Sequential quadratic programming** or **interior point methods** are the right tools.

**Corollary (Lagrangian gradient).** The gradient of the Lagrangian with respect to $x$ is
$$\nabla_x L(x, z) = 2 Df(x)^T f(x) + Dg(x)^T z.$$
The KKT stationarity condition is exactly $\nabla_x L(\hat x, \hat z) = 0$.

**Corollary (Lagrangian Hessian).** The Hessian of the Lagrangian with respect to $x$ is
$$\nabla_{xx}^2 L(x, z) = 2 Df^T Df + 2 \sum_i f_i \nabla^2 f_i + \sum_j z_j \nabla^2 g_j.$$
The Gauss–Newton-like approximation of this Hessian uses $2 Df^T Df$ alone, ignoring both the residual curvature term and the constraint curvature term. The augmented Lagrangian's $2\mu Dg^T Dg$ term adds an approximation of *part* of the constraint contribution.

**Calibration check.** A reader who has understood the definition should: (i) write down the KKT system for $\min (x_1 - 1)^2 + (x_2 - 1)^2$ s.t. $x_1 + x_2 = 1$ and solve it (should get $\hat x = (1/2, 1/2)$, $\hat z = -1$); (ii) identify that with the constraint $x_1^2 + x_2^2 = 1$ (nonlinear) the problem requires iteration; (iii) explain why the constraint $g_1(x) = g_2(x)$ (the two constraints coincide) violates LICQ and forces the multiplier to be non-unique.

---

# Unlocked by This

> [!tip] Optimal Control via Direct Transcription *(from Control Theory)*
> Continuous-time optimal control problems $\min \int_0^T \ell(x(t), u(t))\, dt$ subject to $\dot x = f(x, u)$, $x(0) = x_0$, $x(T) = x_T$ are discretized in time and recast as **equality-constrained nonlinear LS** with the discretized dynamics as the constraints. This is **direct transcription** (or "direct collocation," "direct multiple shooting"), the workhorse of modern numerical optimal control. The augmented Lagrangian algorithm solves these problems; sparse linear algebra exploits the band-diagonal structure of the constraint Jacobian to keep the iteration cost linear in the time horizon $N$. Trajectory optimization for rockets, manipulators, and autonomous vehicles is done this way every day.

> [!tip] Variational Methods with Constraints *(from Calculus of Variations)*
> Many problems in physics and engineering ask for a function $u : \Omega \to \mathbb{R}$ minimizing a functional $\int \mathcal{L}(u, \nabla u)$ subject to $u = u_0$ on $\partial \Omega$ (boundary conditions) or $\int u = c$ (integral constraints). Discretization on a mesh converts these into finite-dimensional constrained nonlinear LS problems, and the same algorithms apply. The continuous Lagrange multiplier is identified, after discretization, with a vector of multipliers — one per constraint imposed by the discretization. This connects the chapter's algorithms to the **finite element method** for nonlinear PDEs with constraints.

> [!tip] Nonlinear Programming Solvers *(from Optimization)*
> The two main families of modern NLP solvers are **interior point methods** (IPOPT, KNITRO) and **sequential quadratic programming** (SNOPT). Both are direct generalizations of the equality-constrained algorithms here. IPOPT adds a logarithmic barrier on inequality constraints and uses Newton's method on the barrier-augmented Lagrangian; SNOPT linearizes constraints at each iterate and solves a quadratic program. The equality-only augmented Lagrangian algorithm is the conceptual ancestor of both, and remains competitive for problems where it applies directly.
