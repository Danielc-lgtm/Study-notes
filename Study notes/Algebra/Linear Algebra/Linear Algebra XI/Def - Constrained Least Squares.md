---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Least Squares Problem"
  - "Def - Multi-Objective Least Squares"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation

In a constrained LS problem, $A$ is an $m \times n$ matrix (the objective matrix), $b$ an $m$-vector (objective right-hand side), $C$ a $p \times n$ matrix (constraint matrix), $d$ a $p$-vector (constraint right-hand side). The variable is $x \in \mathbb{R}^n$. A vector $x$ is *feasible* if $Cx = d$. The Lagrange multipliers (or *dual variables*) form a $p$-vector $\nu$. The associated *KKT system* is the augmented linear system from [[Def - KKT System]].

The number of constraints satisfies $p \leq n$ (no more constraints than variables; otherwise the constraint system is over-determined and generically infeasible). Existence and uniqueness require: (i) rows of $C$ are linearly independent; (ii) the stacked matrix $\binom{A}{C}$ has linearly independent columns.

---

# Axiom Motivation

Many problems ask for a least squares fit, *but with hard constraints*. Maybe the parameters must sum to 1 (portfolio allocation), or the predicted trajectory must hit a specific waypoint (control problem), or the inferred state must satisfy a dynamics equation (state estimation). The constraints are *not negotiable*: any candidate $x$ that violates them is unacceptable, no matter how small the LS objective.

The naive approach — add the constraints as soft penalties via multi-objective LS, $\min \|Ax - b\|^2 + \lambda \|Cx - d\|^2$ with large $\lambda$ — produces a solution that *approximately* satisfies the constraints. For any finite $\lambda$, $Cx \neq d$ in general; pushing $\lambda \to \infty$ recovers exact satisfaction but with numerical conditioning issues (the stacked matrix has a huge ratio of row scales).

The principled formulation imposes the constraints *exactly*:
$$\min_x \|Ax - b\|^2 \quad \text{subject to} \quad Cx = d.$$
The feasible set is the *affine [[Def - Subspace|subspace]]* $\{x : Cx = d\}$, which is non-empty iff the constraint system has at least one solution (which it does iff the rows of $C$ are linearly independent — the standard assumption — or, more generally, iff $d$ lies in the range of $C$). On this feasible set, we minimize the LS objective.

Geometrically: we are finding the point in $\mathrm{col}(A)$ closest to $b$ that comes from an $x$ in the feasible affine [[Def - Subspace|subspace]]. The unconstrained LS finds the closest point in $\mathrm{col}(A)$ overall; the constrained version requires that $x$ also lie in a specified affine subspace.

The deep observation is that this constrained problem reduces to a *single linear system*, just larger than the unconstrained case. The Lagrange multiplier method gives the *KKT optimality conditions*:
- *Stationarity*: $\nabla_x L = 2 A^T(Ax - b) + C^T \nu = 0$, i.e., $2 A^T A x + C^T \nu = 2 A^T b$. This is the *generalized normal equation*: the gradient of the objective is balanced by the gradients of the constraints (weighted by the multipliers $\nu$).
- *Feasibility*: $Cx = d$.

Stacking these as a block matrix equation gives the KKT system:
$$\begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix} \begin{pmatrix} x \\ \nu \end{pmatrix} = \begin{pmatrix} 2 A^T b \\ d \end{pmatrix}.$$
This is an $(n + p) \times (n + p)$ square linear system. Under the conditions (i) and (ii) above, the matrix is invertible, and there is a unique $(x, \nu)$ solution. The $\nu$ part is often not interesting in itself (it is the "shadow price" of the constraint, useful in sensitivity analysis), but it is *necessary* to extract — without solving for $\nu$, we cannot identify $x$.

Three motivating routes lead to the same formulation:

(i) *Lagrange multipliers*. The above derivation. This is the standard approach in constrained smooth optimization, and the multipliers $\nu$ have natural interpretation as shadow prices.

(ii) *Limit of multi-objective LS*. As the weight $\lambda$ on the constraint objective $\|Cx - d\|^2$ tends to infinity, the multi-objective LS solution converges to the constrained LS solution. The $\nu$ vector is, in this limit, $\nu = \lim_{\lambda \to \infty} 2\lambda (Cx(\lambda) - d)$ — a finite limit because the constraint violation $Cx(\lambda) - d$ vanishes at rate $1/\lambda$.

(iii) *Projection onto the feasible affine subspace, restricted to the column space*. The constrained LS solution is the orthogonal projection of $b$ onto the column space of $A$ restricted to the affine subspace $\{x : Cx = d\}$. This is a generalization of the orthogonal-projection interpretation of unconstrained LS.

The further special cases are illuminating:

*No constraints ($p = 0$):* the KKT system reduces to $2 A^T A x = 2 A^T b$, i.e., the ordinary normal equations.

*Zero objective ($A = 0, b = 0$):* the KKT system becomes $C^T \nu = 0, Cx = d$, which (with $C$ having linearly independent rows) gives the *least-norm* solution. But this requires regularization-like content; usually we set $A = I, b = 0$ giving $\min \|x\|^2$ s.t. $Cx = d$, with solution $\hat{x} = C^T(CC^T)^{-1} d = C^\dagger d$ — the [[Def - Pseudoinverse|pseudoinverse]] of the wide matrix $C$.

*Equality-constraint regression*: when the data-fitting problem has natural side constraints (e.g., the regression coefficient sum to a known value, or the model interpolates exactly at specific points), constrained LS provides the exact framework. This is far more elegant than ad-hoc adjustments after unconstrained fitting.

The reader has now invented the constrained-LS framework. The next definition formalizes the KKT system, the theorem characterizes its solvability, and the §XI.4 applications (portfolio, LQR, Kalman) all instantiate this framework.

---

# The Definition

> **Definition (Constrained Least Squares).** Given an $m \times n$ matrix $A$, an $m$-vector $b$, a $p \times n$ matrix $C$ (with $p \leq n$), and a $p$-vector $d$, the *constrained least squares problem* (or *linearly equality-constrained LS*) is
> $$\min_{x \in \mathbb{R}^n} \|Ax - b\|^2 \quad \text{subject to} \quad Cx = d.$$
> A vector $x$ is *feasible* if $Cx = d$. An *optimal point* (or *solution*) is a feasible $x$ with $\|Ax - b\|^2 \leq \|A\tilde{x} - b\|^2$ for all feasible $\tilde{x}$.
>
> The problem has a unique solution if and only if:
> 1. The rows of $C$ are linearly independent (the constraint system is non-redundant and consistent), *and*
> 2. The stacked matrix $\binom{A}{C}$ has linearly independent columns (no nonzero $x$ is simultaneously a "free direction" for the objective and feasible for the constraint).
>
> Under these conditions, the solution $\hat{x}$ is obtained by solving the *KKT system* (see [[Def - KKT System]]):
> $$\begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix} \begin{pmatrix} x \\ \nu \end{pmatrix} = \begin{pmatrix} 2 A^T b \\ d \end{pmatrix},$$
> where $\nu \in \mathbb{R}^p$ is the vector of Lagrange multipliers for the constraints.

---

# Relate to Other Fields / Compression

**True name:** constrained LS is *orthogonal projection of $b$ onto a constrained subspace*. Where unconstrained LS projects $b$ onto $\mathrm{col}(A)$, constrained LS projects onto $A \cdot \{x : Cx = d\}$ — the image under $A$ of the feasible affine subspace. The Lagrange multipliers $\nu$ are the linear combinations of $\nabla(C_i^T x - d_i)$ that, added to $\nabla_x \|Ax - b\|^2$, give zero — the geometric condition for stationarity on the feasible set.

This is the same construction as:
- **Equality-constrained quadratic programming**: the simplest case of QP, where constrained LS is a special case (the quadratic objective $\|Ax - b\|^2$ is a particular form of general convex quadratic $x^T P x + q^T x$).
- **Galerkin methods with essential boundary conditions**: in finite-element analysis, "essential" boundary conditions (Dirichlet) are imposed as constraints rather than as soft penalties. The resulting linear system is a constrained-LS-like KKT system.
- **Lagrange Multipliers in Multivariate Calculus**: the smooth-optimization generalization, where the constraint $g(x) = 0$ may be nonlinear. The first-order condition $\nabla f = \nu \nabla g$ (in our notation) is the KKT stationarity equation. See [[Def - The Total Derivative and Differentiability]].
- **Method of Substitution**: in some special cases (e.g., when $C$ has a "selector" form), one can substitute the constraint into the objective and reduce to an unconstrained LS in fewer variables. This is the equality-constraint elimination technique and is the basis of variable-elimination approaches in LP solvers.

---

# Examples / Corollaries

*Example 1 (least-norm problem).* When $A = I, b = 0$, the constrained LS problem becomes $\min \|x\|^2$ s.t. $Cx = d$ — the *least-norm problem*. Solution: $\hat{x} = C^T(CC^T)^{-1} d = C^\dagger d$, the [[Def - Pseudoinverse|pseudoinverse]] formula for wide matrices with linearly independent rows. See [[Def - Pseudoinverse]].

*Example 2 (spline fitting with continuity constraints).* Fit two cubic polynomials $p(x), q(x)$ to a dataset, with the constraint that $p(a) = q(a)$ and $p'(a) = q'(a)$ (continuity and smoothness at the join point $a$). This is constrained LS with $p = 2$ scalar constraints. The result is a piecewise-cubic *spline*. Generalizing to many pieces gives the standard cubic-spline interpolation/fitting.

*Example 3 (portfolio optimization).* Given a return matrix $R \in \mathbb{R}^{T \times n}$ and a target return $\rho$, find allocation weights $w$ minimizing the realized risk $\|Rw - \rho \mathbf{1}\|^2$ subject to budget constraint $\mathbf{1}^T w = 1$ and target-return constraint $\mu^T w = \rho$. The constraint matrix is $C = \binom{\mathbf{1}^T}{\mu^T}$ (a $2 \times n$ matrix), with $d = \binom{1}{\rho}$. See [[Ex - Portfolio optimization as constrained LS]].

*Example 4 (LQR control).* Choosing a control trajectory $u_1, \ldots, u_{T-1}$ for a linear dynamical system, with constraints $x_{t+1} = A_t x_t + B_t u_t$ (dynamics) and $x_1 = x_{\text{init}}, x_T = x_{\text{des}}$ (boundary conditions), and minimizing a quadratic cost. The dynamics equations and boundary conditions are *all* linear equality constraints, making this a single large constrained LS problem. See [[Ex - Linear quadratic control via constrained LS]].

*Example 5 (NOT a constrained LS — inequality constraints).* The portfolio problem with $w \geq 0$ (no short selling) is *not* a constrained LS problem; it has inequality constraints. The KKT framework still applies but now includes complementary slackness conditions, and the problem is a quadratic program (QP) rather than a linear system. Specialized QP solvers (active-set, interior-point) are needed.

**Calibration check.** Verify: (i) when $C$ is empty ($p = 0$), the KKT system reduces to the unconstrained normal equations $2 A^T A x = 2 A^T b$; (ii) when $A$ is empty ($m = 0$), we have a *least-norm problem* $\min \|x\|^2$ s.t. $Cx = d$ with solution $\hat{x} = C^\dagger d$; (iii) the KKT system has $n + p$ unknowns and $n + p$ equations (square), and the solution $\hat{x}$ exists and is unique iff the KKT matrix is invertible.

---

# Unlocked by This

> [!tip] Quadratic Programming *(from Optimization)*
> Constrained LS is the simplest case of **quadratic programming (QP)**: minimize a convex quadratic $\frac{1}{2} x^T P x + q^T x$ subject to equality and/or inequality linear constraints. The equality-only case (here) admits closed-form KKT solutions; adding inequality constraints requires iterative active-set or interior-point methods. The pattern transfers: KKT optimality conditions stay the same, with additional complementary-slackness conditions for inequalities.

> [!tip] Convex Optimization *(from Convex Analysis)*
> Constrained LS is a baby example of the broader **convex optimization** framework. The unifying principle: any convex objective with linear equality and/or inequality constraints has a KKT-type characterization of optimality, and well-developed numerical methods (interior point, ADMM) solve such problems efficiently. The constrained-LS solution is the unique point where the gradient of the objective lies in the *negative cone* of the constraint normals — a geometric statement that generalizes the linear-algebraic KKT system.

> [!tip] Lagrangian Mechanics *(from Classical Mechanics)*
> Lagrange multipliers in constrained LS are the linear-algebraic shadow of Lagrange multipliers in **classical mechanics**, where they enforce holonomic constraints on the motion of mechanical systems. The constraint forces (mathematical Lagrange multipliers) are the forces the constraints exert on the system to keep it on the constraint manifold. The same conceptual unification: stationarity of an action functional, subject to constraints, gives optimality + feasibility + multipliers.
