---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Constrained Least Squares"
  - "Def - Normal Equations"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation

For the constrained LS problem $\min \|Ax - b\|^2$ subject to $Cx = d$, the KKT system involves: the *primal* variable $x \in \mathbb{R}^n$, the *dual* variable (Lagrange multipliers) $\nu \in \mathbb{R}^p$, the *KKT matrix*
$$M = \begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix} \in \mathbb{R}^{(n+p) \times (n+p)},$$
and the *KKT right-hand side* $r = \binom{2 A^T b}{d} \in \mathbb{R}^{n + p}$. The KKT system is $M \binom{x}{\nu} = r$.

The Lagrangian function is $L(x, \nu) = \|Ax - b\|^2 + \nu^T (Cx - d)$. The KKT system arises as the stationarity conditions $\nabla_x L = 0$ and $\nabla_\nu L = 0$.

---

# Axiom Motivation

When we want to minimize $\|Ax - b\|^2$ subject to the constraint $Cx = d$, we need a notion of "optimality on a constrained set." The unconstrained case has a clean condition: gradient of the objective equals zero. The constrained case requires a generalization, because on the boundary of (or inside) the feasible set, the gradient need not vanish — it can point in any direction *transverse* to the feasible set, since moving in such directions would violate the constraint.

The Lagrange-multiplier insight is that at a constrained optimum, the gradient of the objective is in the span of the gradients of the constraints. Specifically, $\nabla_x \|Ax - b\|^2 = -\sum_{i} \nu_i \nabla(C_i^T x - d_i) = -C^T \nu$ for some vector of multipliers $\nu$. This is a *linear-algebraic condition* on the gradient: it lies in the row space of $C$, with the multipliers $\nu$ being the coefficients.

Together with the feasibility condition $Cx = d$, this gives a square system: $(n + p)$ unknowns ($x$ and $\nu$) and $(n + p)$ equations (the $n$ stationarity equations and the $p$ feasibility equations). This is the *KKT system*.

The derivation is mechanical:
- The Lagrangian is $L(x, \nu) = \|Ax - b\|^2 + \nu^T(Cx - d)$.
- Stationarity: $\nabla_x L = 2 A^T(Ax - b) + C^T \nu = 0$, giving $2 A^T A x + C^T \nu = 2 A^T b$.
- Feasibility (equivalently $\nabla_\nu L = 0$): $Cx - d = 0$, giving $Cx = d$.

Stack these in block form:
$$\begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix} \begin{pmatrix} x \\ \nu \end{pmatrix} = \begin{pmatrix} 2 A^T b \\ d \end{pmatrix}.$$

The structure is illuminating. The top-left block $2 A^T A$ is the Gram matrix of the objective — what would be the normal equations in the unconstrained case. The bottom-right block is zero, reflecting that the constraint has no "self-interaction" (it is purely affine). The off-diagonal blocks $C^T$ and $C$ encode the *coupling* between the objective and the constraint: the constraint normals (rows of $C$) interact with the objective via the multipliers.

The bottom-right zero block has an important consequence: the KKT matrix is *not* positive definite (in general — only positive semidefinite). It has a *saddle-point* structure, with the objective hessian and the constraint giving conflicting signs. The KKT matrix is invertible — but it is not symmetric positive definite, and solving the KKT system requires methods (LU, LDLT, or specialized saddle-point solvers) that do not rely on positive definiteness.

The two assumptions ensuring invertibility — rows of $C$ linearly independent, and stacked $\binom{A}{C}$ with linearly independent columns — together imply the KKT matrix is *non-singular*. Without them, multiple LS minimizers or unsolvable constraint systems make the unique-solution claim fail.

The further structural insight: the KKT system has the form of a *block 2x2* linear system, and there are efficient solution techniques exploiting this. The Schur-complement approach eliminates $\nu$ first:
- From the bottom block, $\nu = (CC^T)^{-1}(d - $ (whatever depends on $x$));
- Substituting into the top block gives a smaller system for $x$ alone.

This is equivalent to the QR-based algorithm in Boyd §16.3 (algorithm 16.2). The total cost is $O((m + p) n^2)$ flops, dominated by the QR factorization of the stacked $(m + p) \times n$ matrix $\binom{A}{C}$.

For *sparse* problems (LQR, Kalman) where $A$ and $C$ have block-banded structure, the KKT matrix is block-banded too, and the cost can be reduced from $O(T^3)$ to $O(T)$ via sparse LU or specialized recursive algorithms. The recursive Kalman filter and the LQR backward sweep are both sparse-KKT solvers in disguise.

---

# The Definition

> **Definition (KKT System).** For the constrained LS problem $\min \|Ax - b\|^2$ subject to $Cx = d$ (with $A$ an $m \times n$ matrix, $b$ an $m$-vector, $C$ a $p \times n$ matrix, $d$ a $p$-vector), the *KKT system* is the $(n + p) \times (n + p)$ linear system
> $$\begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix} \begin{pmatrix} x \\ \nu \end{pmatrix} = \begin{pmatrix} 2 A^T b \\ d \end{pmatrix},$$
> where $\nu \in \mathbb{R}^p$ is the vector of *Lagrange multipliers* (or *dual variables*).
>
> The $(n + p) \times (n + p)$ coefficient matrix is called the *KKT matrix* and is invertible iff (i) the rows of $C$ are linearly independent, and (ii) the stacked matrix $\binom{A}{C}$ has linearly independent columns. Under these conditions, the unique solution $(x, \nu)$ has $x$ equal to the constrained LS minimizer.
>
> The name *KKT* honors William Karush, Harold Kuhn, and Albert Tucker, who derived these optimality conditions for general (non-quadratic) constrained optimization.

---

# Relate to Other Fields / Compression

**True name:** the KKT system is the *linear-algebraic form of constrained-optimization stationarity*. The top block (stationarity) says "the gradient of the objective is in the row space of $C$"; the bottom block (feasibility) says "$x$ satisfies the constraint." For quadratic-objective + linear-constraint problems, both blocks are linear in $(x, \nu)$, and the combined system is a *square* linear system.

This is the same construction as:
- **Lagrange Multipliers in Smooth Optimization**: when the objective $f(x)$ and constraint $g(x) = 0$ are smooth (not necessarily quadratic/linear), the same stationarity condition $\nabla f = -\sum \nu_i \nabla g_i$ holds, but the resulting equations are *nonlinear* and require iterative solution.
- **Karush-Kuhn-Tucker Conditions** in nonlinear programming: with inequality constraints $h(x) \leq 0$, the KKT conditions add complementary slackness ($\nu_i h_i(x) = 0$) and sign constraints ($\nu_i \geq 0$). The equality-only case here is a special case.
- **Saddle-Point Problems**: the KKT system arises naturally in mixed finite-element formulations of PDEs (Stokes equations, mixed elasticity, Lagrange-multiplier penalty methods), where the velocity-pressure pair plays the role of $(x, \nu)$ and the saddle-point structure makes naive iterative solvers diverge — specialized solvers (Uzawa, augmented Lagrangian) are needed.
- **Primal-Dual Pairs in Linear Programming**: the LP primal $\min c^T x$ s.t. $Ax = b, x \geq 0$ has a dual $\max b^T \nu$ s.t. $A^T \nu \leq c$, and the KKT conditions $A^T \nu + s = c, s \cdot x = 0, x \geq 0, s \geq 0$ couple the primal and dual variables. This is the LP analog of our quadratic case.

---

# Examples / Corollaries

*Example 1 (KKT for a budget-constrained portfolio).* Minimize $\|Rw - \rho \mathbf{1}\|^2$ subject to $\mathbf{1}^T w = 1$. The KKT system is
$$\begin{pmatrix} 2 R^T R & \mathbf{1} \\ \mathbf{1}^T & 0 \end{pmatrix} \begin{pmatrix} w \\ \nu \end{pmatrix} = \begin{pmatrix} 2 \rho R^T \mathbf{1} \\ 1 \end{pmatrix}.$$
The single scalar multiplier $\nu$ has interpretation as the marginal change in optimal risk per unit relaxation of the budget constraint — the "shadow price" of the budget. See [[Ex - Portfolio optimization as constrained LS]].

*Example 2 (KKT for least-norm).* Minimize $\|x\|^2$ subject to $Cx = d$ (with $C$ having linearly independent rows). The KKT system is
$$\begin{pmatrix} 2 I & C^T \\ C & 0 \end{pmatrix} \begin{pmatrix} x \\ \nu \end{pmatrix} = \begin{pmatrix} 0 \\ d \end{pmatrix}.$$
From the top block, $x = -\frac{1}{2} C^T \nu$. Substituting into the bottom block: $-\frac{1}{2} CC^T \nu = d$, so $\nu = -2(CC^T)^{-1} d$. Then $x = C^T(CC^T)^{-1} d = C^\dagger d$ — the classical least-norm formula via the wide-matrix [[Def - Pseudoinverse|pseudoinverse]].

*Example 3 (KKT for LQR).* For the linear quadratic control problem with $T$ time steps, the variable $z = (x_1, \ldots, x_T, u_1, \ldots, u_{T-1})$ has [[Def - Dimension|dimension]] $Tn + (T-1)m$, and the constraint matrix $C$ (encoding dynamics + boundary conditions) has block-banded structure with bandwidth $\max\{n, m\}$. The KKT matrix is also block-banded; sparse LU factorization solves it in $O(T)$ flops. See [[Ex - Linear quadratic control via constrained LS]].

*Example 4 (KKT non-invertibility — redundant constraints).* If two rows of $C$ are identical (or one is a linear combination of others), the constraint system is redundant: any $x$ satisfying the independent constraints satisfies the redundant ones. The corresponding $\nu$ is not uniquely determined (the multipliers can absorb the redundancy in different ways), and the KKT matrix is singular. The fix is to drop redundant constraints to reduce $C$ to having linearly independent rows.

*Example 5 (KKT non-invertibility — uncoupled objective and constraint).* If $C = 0$ (no constraint) but we still write the KKT system formally, the bottom row says $\nu$ is arbitrary (multiplied by zero), so the KKT matrix has a kernel and is non-invertible. In this case, the constraint contributes no information and the problem reduces to unconstrained LS.

**Calibration check.** Verify: (i) the KKT system is $(n + p) \times (n + p)$ — square, ready for direct solution; (ii) the KKT matrix is *symmetric* (the $(C^T, C)$ off-diagonal blocks are transposes of each other and the $2 A^T A$ block is symmetric) but *not* positive definite (the $0$ block in the bottom-right makes it indefinite); (iii) the multipliers $\nu$ have a *sensitivity* interpretation: $\partial (\text{optimal value})/\partial d = \nu^T$, the rate at which the optimal LS objective changes when the constraint right-hand side $d$ is perturbed.

---

# Unlocked by This

> [!tip] KKT Conditions for General Convex Optimization *(from Optimization Theory)*
> The full **KKT conditions** for convex optimization with inequality constraints generalize the linear KKT system here. For $\min f(x)$ subject to $g_i(x) \leq 0$, the conditions are: (i) stationarity $\nabla f + \sum \mu_i \nabla g_i + \sum \nu_j \nabla h_j = 0$, (ii) primal feasibility $g_i(x) \leq 0, h_j(x) = 0$, (iii) dual feasibility $\mu_i \geq 0$, (iv) complementary slackness $\mu_i g_i(x) = 0$. For convex $f, g_i$, the KKT conditions are sufficient for global optimality. Modern interior-point methods (used in CPLEX, Gurobi, MOSEK) solve these conditions iteratively for large-scale convex problems.

> [!tip] Saddle-Point Problems in PDEs *(from Numerical Analysis)*
> The block-2x2 KKT structure $\begin{pmatrix} A & B^T \\ B & 0 \end{pmatrix}$ appears in **mixed finite-element methods** for elliptic PDEs (Stokes, mixed elasticity, Darcy flow). The $A$ block encodes a self-adjoint operator (often the Laplacian) and the $B$ block encodes the constraint (often $\nabla \cdot u = 0$ for incompressibility). The saddle-point structure requires *inf-sup stable* (LBB) discretizations to ensure well-posedness, and specialized iterative solvers (Schur complement, augmented Lagrangian) to solve efficiently. This is a direct extension of the constrained-LS KKT framework to infinite dimensions.

> [!tip] Mean-Variance Portfolio Theory *(from Math Finance)*
> The Markowitz portfolio problem is a constrained LS problem solved via KKT; the multipliers have a financial interpretation as *shadow prices* of constraints. The shadow price of the budget constraint is the marginal value of an additional dollar; the shadow price of the target-return constraint is the marginal cost of an additional unit of required return. This is the **two-fund theorem** in operation: solving the KKT system parametrically in the target return $\rho$ shows that all efficient portfolios are affine combinations of two anchoring portfolios.
