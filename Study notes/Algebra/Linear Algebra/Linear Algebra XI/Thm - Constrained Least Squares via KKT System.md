---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Constrained Least Squares"
  - "Def - KKT System"
tags: [algebra, linear-algebra, applied, optimization, constrained-optimization]
---

# Notation

$A$ is an $m \times n$ matrix (objective), $b$ an $m$-vector, $C$ a $p \times n$ matrix (constraint), $d$ a $p$-vector. The variable is $x \in \mathbb{R}^n$; the Lagrange multipliers are $\nu \in \mathbb{R}^p$. The KKT matrix is the $(n + p) \times (n + p)$ block matrix from [[Def - KKT System]].

---

# Statement

> **Theorem (Constrained Least Squares via KKT System).** Consider the constrained LS problem
> $$\min_x \|Ax - b\|^2 \quad \text{subject to} \quad Cx = d.$$
> 1. *Existence and uniqueness*: This problem has a unique solution if and only if:
>    (i) The rows of $C$ are linearly independent (the constraint system is consistent and non-redundant), and
>    (ii) The stacked matrix $\binom{A}{C}$ has linearly independent columns (no nonzero $x$ is simultaneously a "free direction" for the objective and feasible for the constraint).
> 2. *KKT system*: Under conditions (i)-(ii), the unique solution $\hat{x}$ is obtained from the KKT system
> $$\begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix} \begin{pmatrix} x \\ \nu \end{pmatrix} = \begin{pmatrix} 2 A^T b \\ d \end{pmatrix},$$
> where $\nu \in \mathbb{R}^p$ is the vector of Lagrange multipliers.
> 3. *Direct algorithm*: Solving the KKT system by forming the Gram matrix $A^T A$ and using QR factorization on the KKT matrix costs
> $$m n^2 + 2 (n + p)^3 \quad \text{flops}.$$
> 4. *QR-based algorithm*: Solving the KKT system via QR factorizations of $\binom{A}{C}$ and an auxiliary matrix (Boyd Algorithm 16.2) costs
> $$2 (m + p) n^2 + 2 n p^2 \quad \text{flops},$$
> which is the more efficient method when $m \gg n + p$.
> 5. *Linearity in data*: The solution $\hat{x}$ is a linear function of $b$ and $d$.

---

# Motivation

This theorem unifies all the constrained-LS applications in §XI.4 (portfolio, LQR, Kalman) under one solution method: solve a single linear system whose matrix is the KKT matrix and whose right-hand side combines the objective data and the constraint data. The existence-uniqueness conditions (i)-(ii) are easy to check in practice, and the algorithm is a direct extension of QR-based unconstrained LS.

The role of the theorem: it bridges the constrained-LS *problem statement* (often presented as a portfolio, control, or estimation problem in disguise) to the *solver* (a structured linear system, solvable in known time). The deep meta-content is that *every* equality-constrained quadratic problem can be solved by *one* method — solving its KKT system — and applications differ only in what the matrices $A, C$ encode.

The conditions (i)-(ii) deserve careful explanation. Condition (i) — linear independence of $C$'s rows — says the constraint system is consistent and non-redundant. If two rows of $C$ are linearly dependent (one is a scalar multiple of the other), one constraint is redundant; we can drop it without changing the feasible set. If $d$ doesn't satisfy the same linear relation as the rows of $C$, the constraint system is infeasible; no solution exists at all.

Condition (ii) — linear independence of columns of $\binom{A}{C}$ — is the *joint* version of the linear-independence assumption for unconstrained LS. It says: there is no nonzero direction $x$ that *both* lies in the kernel of $A$ (so the objective is flat in that direction) *and* lies in the kernel of $C$ (so the constraint is satisfied in that direction). If such a direction existed, the LS minimum would not be unique: we could move along $x$ without changing the objective or violating the constraint.

The conditions are not equivalent to the individual matrices having full rank; in particular, $A$ itself can have linearly *dependent* columns, as long as the stacked matrix recovers full rank.

---

# Sources and Targets

**Sources (input broadening)**

The theorem applies to any equality-constrained quadratic problem. The non-obvious bridges:

*Source 1: Portfolio optimization.* The Markowitz problem $\min \|Rw - \rho \mathbf{1}\|^2$ s.t. $\mathbf{1}^T w = 1, \mu^T w = \rho$ is constrained LS with $A = R, b = \rho \mathbf{1}, C = \binom{\mathbf{1}^T}{\mu^T}, d = \binom{1}{\rho}$. The conditions (i)-(ii) are easily verified: rows of $C$ are independent as long as $\mu \neq c \mathbf{1}$ for any scalar $c$ (i.e., not all assets have the same mean return), and the joint rank condition usually holds.

*Source 2: LQR control.* Stacking states and inputs into $z$ and writing the dynamics as $\tilde{C} z = \tilde{d}$, the LQR problem becomes constrained LS with a large block-banded $\tilde{C}$. Condition (i) holds because the dynamics constraints are independent (each step has its own equation); condition (ii) holds because the input matrices $B_t$ have full column rank (otherwise the input has no effect).

*Source 3: Kalman state estimation.* Same KKT structure as LQR; the constraint is again dynamics. Both conditions (i) and (ii) typically hold; the multipliers play the role of *innovations* in the recursive form.

*Source 4: Constrained polynomial interpolation.* Fit a polynomial that interpolates exactly at specified points while minimizing some norm. The interpolation conditions are linear constraints; the norm is the LS objective. Condition (i) holds if the interpolation nodes are distinct (rows of $C$ are independent Vandermonde rows); (ii) holds if the polynomial space is rich enough.

*Source 5: Equality-constrained ridge regression.* Add a Tikhonov term $\lambda \|x\|^2$ to a constrained LS problem: $\min \|Ax - b\|^2 + \lambda \|x\|^2$ s.t. $Cx = d$. This is constrained LS with stacked objective matrix $\binom{A}{\sqrt{\lambda} I}$. Condition (ii) is *automatically* satisfied (the stacked $\binom{A}{\sqrt{\lambda} I; C}$ has the $\sqrt{\lambda} I$ block ensuring column rank), making regularized constrained LS always well-posed.

**Targets (output amplification)**

The theorem gives a unique solution + an algorithm. Non-obvious uses:

*Target 1 (linear state feedback).* In LQR, the solution $\hat{u}_1$ is a linear function of the initial state $x_{\text{init}}$, so $\hat{u}_1 = K x_{\text{init}}$ for some matrix $K$ (the state-feedback gain). Computing $K$ requires solving the KKT system for $n$ different initial conditions ($x_{\text{init}} = e_1, \ldots, e_n$); the QR factorization is computed once and reused. *Example use*: real-time control of a system with $n$-dimensional state: precompute $K$, then at each time step compute $u = K x$ with a single matrix-vector multiply.

*Target 2 (efficient frontier and two-fund theorem).* In portfolio optimization, sweep the target return $\rho$ to trace the Pareto-optimal frontier. The solution at each $\rho$ involves the same KKT matrix (only $d$ changes), so the factorization is reused. Moreover, the *two-fund theorem* says all efficient portfolios are affine combinations of any two of them — a structural consequence of the linearity in $d$. *Example use*: tracing 100 points on the efficient frontier with one KKT factorization and 100 back-substitutions.

*Target 3 (sensitivity analysis via Lagrange multipliers).* The multipliers $\hat{\nu}$ have an interpretation as the *shadow prices* of the constraints: $\partial \text{(optimal value)}/\partial d_i = \hat{\nu}_i$. *Example use*: in portfolio optimization, the budget multiplier tells you the marginal value of an additional dollar to invest; the target-return multiplier tells you the marginal cost of an additional unit of required return.

*Target 4 (sparse KKT for time-series problems).* For LQR and Kalman with $T$ time steps, the KKT matrix is block-banded, and sparse-matrix LU factorization solves it in $O(T)$ flops instead of the dense $O(T^3)$. The recursive Riccati equation and the recursive Kalman filter are both sparse-KKT solvers in disguise. *Example use*: real-time MPC with $T = 100$ time steps: KKT solve in microseconds via sparse methods.

---

# Why Is It True

**The mechanism in one sentence: stationarity ($\nabla_x L = 0$, where $L$ is the Lagrangian) gives the top block of the KKT system; feasibility ($Cx = d$) gives the bottom block; together they are a square linear system whose invertibility is the precise content of conditions (i)-(ii).**

The full derivation:

*Lagrangian and KKT system.* Form the Lagrangian $L(x, \nu) = \|Ax - b\|^2 + \nu^T(Cx - d)$. Stationarity: $\nabla_x L = 2 A^T(Ax - b) + C^T \nu = 0$, giving $2 A^T A x + C^T \nu = 2 A^T b$. Feasibility: $Cx = d$. Stacking these gives the KKT system.

*Invertibility of the KKT matrix.* The KKT matrix is invertible under conditions (i) and (ii). The proof has two directions:
- *Necessity*: if the KKT matrix is singular, then there is a nonzero $(\bar{x}, \bar{\nu})$ in its kernel. From the top block, $2 A^T A \bar{x} + C^T \bar{\nu} = 0$; from the bottom, $C \bar{x} = 0$. Multiplying the top block on the left by $\bar{x}^T$: $2 \|A \bar{x}\|^2 + \bar{x}^T C^T \bar{\nu} = 2 \|A \bar{x}\|^2 + (C \bar{x})^T \bar{\nu} = 2 \|A \bar{x}\|^2 + 0 = 2 \|A \bar{x}\|^2 = 0$. So $A \bar{x} = 0$. Combined with $C \bar{x} = 0$, we have $\binom{A}{C} \bar{x} = 0$. If $\bar{x} \neq 0$, condition (ii) is violated. If $\bar{x} = 0$, then $C^T \bar{\nu} = 0$ by the top block; if $\bar{\nu} \neq 0$, condition (i) is violated. So at least one of (i), (ii) fails.
- *Sufficiency*: conversely, if both conditions hold, the KKT matrix is invertible — the argument is essentially the reverse of the above.

*Uniqueness and the closed-form formula.* Given invertibility, the KKT system has a unique solution $(x, \nu)$. The $x$ part is the unique LS minimizer. The closed-form formula
$$\hat{x} = (\text{first } n \text{ components of}) \, M^{-1} \binom{2 A^T b}{d}$$
shows $\hat{x}$ is a linear function of $b$ and $d$.

*Linearity in data.* The closed-form formula is linear in $(b, d)$: $\hat{x} = M_{xb} b + M_{xd} d$ where $M_{xb}, M_{xd}$ are the appropriate sub-blocks of $M^{-1}$. This is what makes precomputed feedback control and other linear-in-data techniques possible.

The deeper structural fact: the KKT system has a *saddle-point* structure (positive definite top-left block, zero bottom-right block), and saddle-point linear systems are a well-studied area of numerical linear algebra with specialized solvers (Schur complement, augmented Lagrangian, Uzawa iteration). The structure is the same in PDE-discretization problems (mixed FE, Stokes flow), where the same algorithmic ideas apply.

---

# What Makes This Hard

The hard step for first-time readers is the *direct verification of optimality* (Boyd's "completing the square" argument). The Lagrange-multiplier derivation gives the KKT system as a *necessary* condition; showing it is *sufficient* (i.e., any KKT solution is the LS minimizer, not just a stationary point) requires a direct argument. The completing-the-square computation is mechanical but requires careful tracking of which terms cancel.

A secondary difficulty is *checking the assumptions in practice*. Conditions (i) and (ii) are easy to state but their verification can be subtle, especially in time-series problems where $C$ has block-banded structure. The "rows of $C$ are linearly independent" condition often fails due to redundant constraints in a poorly-formulated problem — e.g., specifying the same constraint twice, or specifying both endpoint values for an initial-value problem.

A third difficulty: the *interpretation of the multipliers $\nu$*. They are not "extra unknowns" introduced for mathematical convenience; they encode the *sensitivity* of the optimal value to constraint perturbations. Students often discard the $\nu$ values once they have $x$; in fact, the multipliers are often the most informative output.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Form the Lagrangian, derive the KKT optimality system, prove invertibility of the KKT matrix under conditions (i)-(ii), and verify by completing the square that the KKT solution is the constrained LS minimizer.

**Subgoal decomposition:**

1. **Lagrangian derivation.** Form $L(x, \nu) = \|Ax - b\|^2 + \nu^T(Cx - d)$ and derive the stationarity conditions $\nabla_x L = 0, \nabla_\nu L = 0$.
   - *Hint:* $\nabla_x L = 2 A^T(Ax - b) + C^T \nu$. Setting to zero gives the top block.
   - *Why needed:* This is the textbook derivation of the necessary conditions.

2. **Invertibility of the KKT matrix.** Show that the $(n + p) \times (n + p)$ KKT matrix is invertible iff conditions (i) and (ii) hold.
   - *Hint:* If $M (\bar{x}, \bar{\nu})^T = 0$, multiply top block on left by $\bar{x}^T$ and use $C \bar{x} = 0$ to derive $\|A \bar{x}\|^2 = 0$, hence $A \bar{x} = 0$.
   - *Why needed:* Establishes existence-uniqueness.

3. **Direct verification.** Show that the KKT solution actually minimizes $\|Ax - b\|^2$ on the feasible set (not just being a stationary point).
   - *Hint:* Completing the square: $\|Ax - b\|^2 = \|A(x - \hat{x}) + (A\hat{x} - b)\|^2 = \|A(x - \hat{x})\|^2 + \|A\hat{x} - b\|^2 + 2(x - \hat{x})^T A^T(A\hat{x} - b)$. The cross term equals $-(x - \hat{x})^T C^T \nu = 0$ (using $C(x - \hat{x}) = 0$ for feasible $x$).
   - *Why needed:* Verifies that the necessary KKT conditions are also sufficient.

4. **Closed-form and algorithm.** Invert the KKT matrix to get the explicit formula; describe the two algorithms (direct via Gram + QR on KKT matrix; QR-based via the stacked matrix $\binom{A}{C}$ and an auxiliary QR).
   - *Hint:* Boyd algorithms 16.1 and 16.2.
   - *Why needed:* Connects the theorem to computational practice.

---

# Lemma Decomposition

> [!note]- Lemma 1: Stationarity of the Lagrangian gives the KKT system.
> **Statement:** Define the Lagrangian $L(x, \nu) = \|Ax - b\|^2 + \nu^T(Cx - d)$. If $(\hat{x}, \hat{\nu})$ is a stationary point of $L$ (i.e., $\nabla L = 0$), then $(\hat{x}, \hat{\nu})$ satisfies the KKT system.
>
> **Hint:** Compute $\nabla_x L$ and $\nabla_\nu L$ separately. Stack into a matrix equation.
>
> **Why needed:** Establishes the KKT system as the linear-algebraic form of the optimality conditions.
>
> > [!note]- Full proof
> > $L(x, \nu) = x^T A^T A x - 2 b^T A x + b^T b + \nu^T C x - \nu^T d$. Then $\nabla_x L = 2 A^T A x - 2 A^T b + C^T \nu$ and $\nabla_\nu L = Cx - d$. Setting both to zero:
> > - $2 A^T A \hat{x} + C^T \hat{\nu} = 2 A^T b$,
> > - $C \hat{x} = d$.
> > Stacking as a block-matrix equation gives the KKT system.

> [!note]- Lemma 2: KKT matrix invertibility ⟺ conditions (i)-(ii).
> **Statement:** The KKT matrix $M = \begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix}$ is invertible iff (i) rows of $C$ are linearly independent and (ii) columns of $\binom{A}{C}$ are linearly independent.
>
> **Hint:** Both directions of the iff are needed. Forward: assume $M$ is singular and derive a violation of (i) or (ii). Backward: assume (i) and (ii) and show $M$ is invertible by direct kernel argument.
>
> **Why needed:** This is the existence-uniqueness criterion.
>
> > [!note]- Full proof
> > $(\Rightarrow)$ Suppose $M$ has a nonzero kernel element $(\bar{x}, \bar{\nu})$. The top block gives $2 A^T A \bar{x} + C^T \bar{\nu} = 0$. Multiply on the left by $\bar{x}^T$: $2 \bar{x}^T A^T A \bar{x} + \bar{x}^T C^T \bar{\nu} = 0$, i.e., $2 \|A \bar{x}\|^2 + (C \bar{x})^T \bar{\nu} = 0$. The bottom block gives $C \bar{x} = 0$, so the cross term vanishes: $2 \|A \bar{x}\|^2 = 0$, hence $A \bar{x} = 0$. Combined with $C \bar{x} = 0$, we have $\binom{A}{C} \bar{x} = 0$. If $\bar{x} \neq 0$, condition (ii) fails. If $\bar{x} = 0$, the top block becomes $C^T \bar{\nu} = 0$; if $\bar{\nu} \neq 0$, condition (i) fails. So at least one of (i), (ii) is violated.
> >
> > $(\Leftarrow)$ Suppose (i) and (ii) hold and $(\bar{x}, \bar{\nu}) \in \ker M$. By the argument above, $A \bar{x} = 0$ and $C \bar{x} = 0$. By (ii), $\bar{x} = 0$. Substituting into the top block: $C^T \bar{\nu} = 0$. By (i) (linear independence of rows of $C$ ⟺ linear independence of columns of $C^T$), $\bar{\nu} = 0$. So $\ker M = \{0\}$, hence $M$ is invertible.

> [!note]- Lemma 3: Direct verification — the KKT solution minimizes the LS objective on the feasible set.
> **Statement:** Let $(\hat{x}, \hat{\nu})$ be the solution of the KKT system. For any $x$ with $Cx = d$, $\|Ax - b\|^2 \geq \|A\hat{x} - b\|^2$, with equality iff $A x = A \hat{x}$.
>
> **Hint:** Complete the square. Write $\|Ax - b\|^2 = \|A(x - \hat{x}) + (A\hat{x} - b)\|^2$, expand, and use the KKT optimality + feasibility to show the cross term vanishes.
>
> **Why needed:** Shows the KKT conditions are sufficient (any KKT solution is a minimizer), completing the existence-uniqueness theorem.
>
> > [!note]- Full proof
> > $\|Ax - b\|^2 = \|A(x - \hat{x}) + (A\hat{x} - b)\|^2 = \|A(x - \hat{x})\|^2 + \|A\hat{x} - b\|^2 + 2(A(x - \hat{x}))^T(A\hat{x} - b)$.
> >
> > The cross term: $2(A(x - \hat{x}))^T(A\hat{x} - b) = 2(x - \hat{x})^T A^T(A\hat{x} - b)$. From the top block of the KKT system, $2 A^T(A\hat{x} - b) = -C^T \hat{\nu}$, so the cross term equals $-(x - \hat{x})^T C^T \hat{\nu} = -(C(x - \hat{x}))^T \hat{\nu}$. Since both $x$ and $\hat{x}$ are feasible, $Cx = C\hat{x} = d$, so $C(x - \hat{x}) = 0$, and the cross term vanishes.
> >
> > Hence $\|Ax - b\|^2 = \|A(x - \hat{x})\|^2 + \|A\hat{x} - b\|^2 \geq \|A\hat{x} - b\|^2$, with equality iff $\|A(x - \hat{x})\|^2 = 0$, i.e., $A x = A \hat{x}$.

> [!note]- Lemma 4: Complexity of the QR-based algorithm.
> **Statement:** The QR-based algorithm (Boyd Algorithm 16.2) for solving the KKT system has cost $2(m + p)n^2 + 2 n p^2$ flops, dominated by $2(m + p) n^2$ when $n \geq p$.
>
> **Hint:** The algorithm involves QR factorization of the $(m + p) \times n$ stacked matrix $\binom{A}{C}$ and an auxiliary QR of $Q_2^T$. Count each step's cost.
>
> **Why needed:** Establishes computational efficiency, especially for time-series problems where the simple Gram-method cost would be cubic in the time horizon.
>
> > [!note]- Full proof
> > See Boyd §16.3 for the detailed algorithm. The steps are:
> > 1. QR factorization of $\binom{A}{C}$ (an $(m + p) \times n$ matrix): cost $2 (m + p) n^2$.
> > 2. QR factorization of an auxiliary $p \times n$ matrix $Q_2^T$: cost $2 n p^2$.
> > 3. Several matrix-vector products and triangular solves: $O((m + p) n + p^2)$, lower order.
> > Total: $2 (m + p) n^2 + 2 n p^2$ flops.

---

# Formal Proof

> [!note]- Complete formal proof
> *Step 0 (Existence preliminary).* If the constraint $Cx = d$ has no solution (because $d$ is not in the range of $C$), the constrained problem is infeasible and has no minimizer. We assume feasibility, which under condition (i) is guaranteed for any $d$.
>
> *Step 1: Lagrangian and KKT.* By Lemma 1, any stationary point of the Lagrangian $L(x, \nu) = \|Ax - b\|^2 + \nu^T(Cx - d)$ satisfies the KKT system.
>
> *Step 2: Invertibility.* By Lemma 2, under conditions (i)-(ii), the KKT matrix is invertible, so the KKT system has a unique solution $(\hat{x}, \hat{\nu})$.
>
> *Step 3: KKT solution is the constrained LS minimizer.* By Lemma 3, $\hat{x}$ minimizes $\|Ax - b\|^2$ over all feasible $x$ (i.e., $x$ with $Cx = d$).
>
> *Step 4: Uniqueness.* By Lemma 3, $\|Ax - b\|^2 = \|A\hat{x} - b\|^2$ implies $A x = A \hat{x}$, i.e., $A(x - \hat{x}) = 0$. Combined with $C(x - \hat{x}) = 0$ (both $x$ and $\hat{x}$ feasible), we have $\binom{A}{C}(x - \hat{x}) = 0$. By condition (ii), $x - \hat{x} = 0$, hence $x = \hat{x}$. So the minimizer is unique.
>
> *Step 5: Complexity and algorithm.* By Lemma 4, the QR-based algorithm has cost $2(m + p) n^2 + 2 n p^2$ flops. The direct (Gram-matrix-based) algorithm has cost $m n^2 + 2 (n + p)^3$ flops, dominated by $(n + p)^3$ when $m \ll n + p$.
>
> *Step 6: Linearity in data.* From the KKT system, $\hat{x} = (\text{first } n \text{ components of}) \, M^{-1} \binom{2 A^T b}{d}$. This is a linear function of $b$ and $d$.

---

# Cross-Field Exercise Suggestions

*Suggestion 1 (Calculus of Variations — Euler-Lagrange equations):* In the continuous-time generalization of LQR, the Lagrangian becomes a functional and the KKT system becomes a system of PDEs (the Euler-Lagrange equations). Apply this theorem to derive the discrete-time Riccati equation as the recursive form of the KKT solver, and recognize the continuous-time Riccati ODE as its limit.

*Suggestion 2 (Stochastic Control — Kalman duality):* The LQR and Kalman problems are duals: same KKT structure with $u \leftrightarrow w$ (input ↔ process noise) and a swap of objective vs. constraint roles. Apply this theorem to verify the duality at the matrix level and to derive the **separation principle** of LQG control.

*Suggestion 3 (Game Theory — Nash equilibria of quadratic games):* In a two-player game where player $i$ minimizes $\|A_i x - b_i\|^2$ over their variable $x_i$ subject to coupling constraints, the Nash equilibrium is characterized by a coupled KKT system. Apply this theorem to verify existence and uniqueness of Nash equilibria in quadratic games, and to derive equilibrium-finding algorithms.

---

# Bridges

- **[[Def - KKT System]]** — The KKT system is the central computational object of constrained LS. This theorem provides the existence-uniqueness conditions and the algorithms for solving it.

- **[[Thm - Least Squares via QR Factorization]]** — The QR-based algorithm for unconstrained LS extends directly to constrained LS (Boyd Algorithm 16.2). The constrained version applies QR to the *stacked* matrix $\binom{A}{C}$ rather than to $A$ alone. The conceptual unification: constrained LS is unconstrained LS on an augmented problem.

- **[[Def - Constrained Least Squares]]** — The problem definition. This theorem provides the solution.

- **Lagrange Multipliers in Smooth Optimization** — In the more general case of constrained smooth optimization (objective and constraints not necessarily quadratic / linear), the KKT optimality conditions still hold but become nonlinear, requiring iterative solution (Newton's method, sequential quadratic programming). The quadratic-objective + linear-constraint case here is the *baby example* that introduces the framework.

- **Saddle-Point Problems in Mixed Finite Elements** — The KKT matrix structure $\begin{pmatrix} A & B^T \\ B & 0 \end{pmatrix}$ appears in mixed-FE discretizations of PDEs (Stokes equations, mixed elasticity). The conditions for well-posedness (inf-sup / LBB) generalize conditions (i)-(ii); specialized iterative solvers (Schur complement, Uzawa, augmented Lagrangian) generalize the algorithms.

---

# Unlocked by This

> [!tip] Sequential Quadratic Programming *(from Nonlinear Programming)*
> The KKT-system solver for *equality-constrained* quadratic problems is the inner-loop of **sequential quadratic programming (SQP)**: iteratively linearize the constraints and quadratize the objective, then solve the resulting equality-constrained QP. SQP is one of the most powerful methods for general nonlinear-constrained optimization, and its theoretical foundation is the equality-constrained QP solver from this theorem.

> [!tip] Interior-Point Methods *(from Optimization)*
> For inequality-constrained problems $\min \|Ax - b\|^2$ s.t. $g(x) \leq 0$, **interior-point methods** solve a sequence of equality-constrained problems with logarithmic-barrier objectives. Each barrier subproblem is solved by KKT-system methods. Modern interior-point solvers (Mosek, Gurobi, CPLEX) for large-scale convex optimization are built on these foundations.

> [!tip] Optimal Control Theory *(from Control Engineering)*
> The discrete-time LQR derived here generalizes to:
> - **Continuous-time LQR**: KKT becomes the Hamilton-Jacobi-Bellman PDE.
> - **Stochastic LQR** (LQG): combine with Kalman filter; separation principle holds.
> - **Robust LQR** ($H^\infty$ control): allow worst-case disturbances; KKT becomes a saddle-point problem.
> - **Adaptive LQR**: identify the system online while controlling; combines system ID with KKT-based control.
> The constrained-LS KKT framework is the algorithmic kernel of all these.
