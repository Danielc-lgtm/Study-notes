---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Linear Quadratic Control"
  - "Def - Constrained Least Squares"
  - "Def - KKT System"
tags: [algebra, linear-algebra, applied, control, optimization]
---

# Problem Statement

You are given a discrete-time linear dynamical system
$$x_{t+1} = A_t x_t + B_t u_t, \quad y_t = C_t x_t, \quad t = 1, \ldots, T,$$
with state $x_t \in \mathbb{R}^n$, input $u_t \in \mathbb{R}^m$, output $y_t \in \mathbb{R}^p$. The initial state $x_1 = x_{\text{init}}$ and desired final state $x_T = x_{\text{des}}$ are given. The cost is $J = J_{\text{output}} + \rho J_{\text{input}}$ with $J_{\text{output}} = \sum_t \|y_t\|^2$ and $J_{\text{input}} = \sum_t \|u_t\|^2$, and $\rho > 0$ trades input against output cost.

1. Set up the LQR problem $\min J$ s.t. dynamics + boundary conditions as a *single* large constrained LS problem on the stacked variable $z = (x_1, \ldots, x_T, u_1, \ldots, u_{T-1})$. Identify the matrices $\tilde{A}, \tilde{b}, \tilde{C}, \tilde{d}$.

2. Write the KKT system. Identify its *block-banded* sparsity pattern.

3. Show that the optimal initial input $\hat{u}_1$ is a *linear function* of the initial state $x_{\text{init}}$ (and final state $x_{\text{des}}$), giving the *linear state-feedback law*: $\hat{u}_1 = K x_{\text{init}}$ (when $x_{\text{des}} = 0$). Explain how to compute the gain matrix $K$.

4. Demonstrate the *control-estimation duality*: the LQR KKT system has the same block-banded structure as the Kalman state-estimation KKT system (see [[Ex - Kalman state estimation as constrained LS]]), with control inputs $u_t$ playing the role of process noise $w_t$, output objectives $\|y_t\|^2$ playing the role of measurement residuals $\|C_t x_t - y_t\|^2$.

**Recall:**

[[Def - Linear Quadratic Control|Linear quadratic control]] is constrained LS over a time-series variable; the dynamics is the constraint. The [[Def - KKT System|KKT system]] for $\min \|\tilde{A} z\|^2$ s.t. $\tilde{C} z = \tilde{d}$ has block structure with $\tilde{A}^T \tilde{A}$ on top-left, $\tilde{C}^T$ on top-right, $\tilde{C}$ on bottom-left, $0$ on bottom-right.

---

# Convergent Strategy

**Problem class:** This is a *time-series-constrained quadratic optimization* problem. The class is "minimize a quadratic in a stacked time-series variable subject to recursive linear constraints (the dynamics)." It is *the* paradigmatic problem of finite-horizon optimal control, and it reduces to constrained LS via the stacking trick that's central to §XI.3-§XI.4.

**Assumption pattern:** Given the time-invariant or time-varying dynamics matrices $A_t, B_t, C_t$, initial state $x_{\text{init}}$, desired final state $x_{\text{des}}$, time horizon $T$, cost weight $\rho > 0$. Three structural assumptions are needed for the KKT system to be well-posed: (i) the dynamics constraints are linearly independent (typically true if the inputs have nontrivial effect on the state); (ii) the columns of the stacked $\binom{\tilde{A}}{\tilde{C}}$ are linearly independent (true if the input matrices $B_t$ have full column rank or if the output observation provides enough information); (iii) the boundary conditions are *reachable* (the system can be driven from $x_{\text{init}}$ to $x_{\text{des}}$ in $T$ steps).

**Theorem routing:** Stack the variables into $z$. Identify $\tilde{A}, \tilde{b}$ for the cost objective and $\tilde{C}, \tilde{d}$ for the dynamics + boundary constraints. Apply [[Thm - Constrained Least Squares via KKT System]] to write down the KKT system and solve. Exploit the block-banded sparsity (each dynamics step couples only consecutive time blocks) to reduce solution cost from $O(T^3)$ to $O(T)$ via sparse linear algebra. The linearity of the solution in $x_{\text{init}}$ gives the state-feedback law $\hat{u}_1 = K x_{\text{init}}$.

**Key decision point:** The non-obvious step is the *stacking* — recognizing that the trajectory-level problem becomes a single high-dimensional LS problem on the stacked $z$. The stacking is mechanical but tedious; the payoff is unifying every LQR-type problem under one solver. The further insight — that the KKT matrix is *block-banded* — is what makes the solution practical for long time horizons (otherwise the $O(T^3)$ dense solve would be prohibitive).

---

# Legal Operations Used

1. **Build the KKT system for an equality-constrained problem.** (Operation 5 from the topic page.) The dynamics + boundary conditions are equality constraints; the cost is the LS objective. Stack into the KKT framework.

2. **Stack matrices to reduce a structured problem to LS.** (Operation 3.) Stacking the time-series variable converts the temporally indexed problem into a single big LS problem; the dynamics constraints become block-banded.

3. **Exploit sparsity in time-series LS problems.** (Operation 10.) The KKT matrix is block-banded; sparse-matrix algorithms (LU, QR with banded ordering) solve it in $O(T)$ flops instead of $O(T^3)$. The recursive Riccati equation is the algorithmic realization of this sparsity exploitation.

4. **Recognize linearity in the data.** (Targeted use of [[Thm - Constrained Least Squares via KKT System]] point 5.) The KKT solution is linear in $\tilde{d}$, hence in $x_{\text{init}}$ and $x_{\text{des}}$. This gives the state-feedback law: $\hat{u}_1 = K x_{\text{init}}$ (when $x_{\text{des}} = 0$).

---

# Hints

> [!note]- Hint 1
> Stack all states and inputs into one big vector: $z = (x_1, x_2, \ldots, x_T, u_1, u_2, \ldots, u_{T-1}) \in \mathbb{R}^{Tn + (T-1)m}$.

> [!note]- Hint 2
> The cost $J = \sum_t \|y_t\|^2 + \rho \sum_t \|u_t\|^2 = \sum_t \|C_t x_t\|^2 + \rho \sum_t \|u_t\|^2$ becomes $\|\tilde{A} z\|^2$ for the block-diagonal matrix
> $$\tilde{A} = \begin{pmatrix} C_1 & & & & & \\ & C_2 & & & & \\ & & \ddots & & & \\ & & & C_T & & \\ & & & & \sqrt{\rho} I_m & \\ & & & & & \ddots \\ & & & & & & \sqrt{\rho} I_m \end{pmatrix}.$$

> [!note]- Hint 3
> The dynamics $x_{t+1} = A_t x_t + B_t u_t$ becomes $-A_t x_t + x_{t+1} - B_t u_t = 0$. Stacking these for $t = 1, \ldots, T - 1$, plus the boundary conditions $x_1 = x_{\text{init}}$ and $x_T = x_{\text{des}}$, gives the constraint matrix $\tilde{C}$ — block-banded with bandwidth $n + m$.

> [!note]- Hint 4 (for state feedback)
> The KKT system right-hand side $\tilde{d}$ contains $x_{\text{init}}$ and $x_{\text{des}}$. Since the KKT solution is linear in $\tilde{d}$, in particular $\hat{u}_1$ is linear in $x_{\text{init}}$ (when $x_{\text{des}} = 0$). Solving the KKT system for $n$ specific initial conditions $x_{\text{init}} = e_1, \ldots, e_n$ and assembling the resulting $\hat{u}_1$ vectors as columns of a matrix gives the gain matrix $K$.

---

# Solution

The proof has four parts. Step 1 stacks the variables and identifies the constrained-LS structure. Step 2 writes the KKT system and analyzes its block-banded structure. Step 3 derives the state-feedback law via linearity in $x_{\text{init}}$. Step 4 explains the control-estimation duality.

**Step 1: Stack into a constrained LS problem.**

Let $z = (x_1, \ldots, x_T, u_1, \ldots, u_{T-1})$, of dimension $Tn + (T-1)m$. The cost objective is
$$J = \sum_{t=1}^T \|C_t x_t\|^2 + \rho \sum_{t=1}^{T-1} \|u_t\|^2.$$
Identify the LS form $J = \|\tilde{A} z\|^2$ with $\tilde{A}$ block-diagonal:
$$\tilde{A} = \begin{pmatrix} C_1 & & & & & & \\ & \ddots & & & & & \\ & & C_T & & & & \\ & & & \sqrt{\rho} I_m & & & \\ & & & & \ddots & & \\ & & & & & \sqrt{\rho} I_m \end{pmatrix},$$
where the first $T$ block-columns act on $x_1, \ldots, x_T$ via $C_t$ and the next $T - 1$ block-columns act on $u_1, \ldots, u_{T-1}$ via $\sqrt{\rho} I_m$. The right-hand side is $\tilde{b} = 0$.

The constraints — dynamics + boundary conditions — give

> [!note]- Derivation
> Stacking the constraints:
> - Dynamics $x_{t+1} - A_t x_t - B_t u_t = 0$ for $t = 1, \ldots, T - 1$: this gives $(T-1)n$ equations.
> - Initial state $x_1 = x_{\text{init}}$: $n$ equations.
> - Final state $x_T = x_{\text{des}}$: $n$ equations.
> Total: $(T+1)n$ equations.
>
> The constraint matrix $\tilde{C}$ has block structure: each dynamics block has $-A_t$ at column $x_t$, $I$ at column $x_{t+1}$, $-B_t$ at column $u_t$, zeros elsewhere. The boundary blocks have $I$ at columns $x_1$ and $x_T$ respectively. This makes $\tilde{C}$ block-banded with bandwidth $\max\{n, m\}$.
>
> The right-hand side $\tilde{d}$ has zeros for the dynamics constraints and $x_{\text{init}}, x_{\text{des}}$ for the boundary constraints.

**Step 2: KKT system and block-banded structure.**

The KKT system is
$$\begin{pmatrix} 2 \tilde{A}^T \tilde{A} & \tilde{C}^T \\ \tilde{C} & 0 \end{pmatrix} \begin{pmatrix} z \\ \nu \end{pmatrix} = \begin{pmatrix} 0 \\ \tilde{d} \end{pmatrix}.$$
The matrix $\tilde{A}^T \tilde{A}$ is *block diagonal* (since $\tilde{A}$ is) with blocks $C_t^T C_t$ on the state diagonals and $\rho I_m$ on the input diagonals. The matrix $\tilde{C}$ is *block-banded* with bandwidth $\max\{n, m\}$. Putting these together, the KKT matrix is *block-banded* with the same bandwidth.

> [!note]- Derivation
> The block-banded structure means: each block-row of the KKT matrix has nonzeros only in its own block and the immediately adjacent ones. For the standard ordering $(x_1, u_1, x_2, u_2, \ldots, x_T)$, the matrix has bandwidth $\max\{n, m\}$ — a "block-tridiagonal-like" structure.
>
> Sparse banded LU factorization solves the KKT system in $O(T (n + m)^2)$ flops — *linear* in the time horizon $T$. The naïve dense LU would cost $O(T^3 (n + m)^3)$, which is prohibitive for large $T$. The exploitation of block-banded sparsity is what makes LQR computationally tractable for long horizons.

**Step 3: Linear state-feedback law.**

The KKT system right-hand side is $(0, \tilde{d})^T$, with $\tilde{d}$ depending linearly on $x_{\text{init}}$ and $x_{\text{des}}$. The KKT matrix is fixed (doesn't depend on the boundary data). So the KKT solution $(z, \nu)$ is a linear function of $(x_{\text{init}}, x_{\text{des}})$. In particular, the *first input* $\hat{u}_1$ (extracted from $z$) is a linear function of $(x_{\text{init}}, x_{\text{des}})$:
$$\hat{u}_1 = K_1 x_{\text{init}} + K_2 x_{\text{des}}.$$
When $x_{\text{des}} = 0$, this becomes $\hat{u}_1 = K_1 x_{\text{init}}$ — the *state-feedback law* with gain matrix $K_1 \in \mathbb{R}^{m \times n}$.

> [!note]- Derivation
> To compute $K_1$: solve the KKT system for $n$ different initial conditions $x_{\text{init}} = e_1, \ldots, e_n$ (with $x_{\text{des}} = 0$). The resulting $\hat{u}_1^{(j)}$ from the $j$-th solve is the $j$-th column of $K_1$. Computational cost: factor the KKT matrix once ($O(T(n+m)^2)$ with sparsity), then $n$ back-substitutions ($n \cdot O(T(n+m))$). Total: $O(T (n+m)^2 + n T (n+m))$ — linear in $T$.
>
> Once $K_1$ is computed offline, real-time control becomes trivial: at each time step, measure the state $x_t$, compute $u_t = K_1 x_t$ via matrix-vector multiply ($O(nm)$ flops), apply. The whole online cost is one matrix-vector multiply per time step — instantaneous.

**Step 4: Control-estimation duality.**

The LQR KKT system has the *same block-banded structure* as the Kalman state-estimation KKT system (see [[Ex - Kalman state estimation as constrained LS]]). The substitutions: control inputs $u_t \leftrightarrow$ process noise $w_t$; output cost $\|C_t x_t\|^2 \leftrightarrow$ measurement residual $\|C_t x_t - y_t\|^2$. The roles of "objective" and "constraint" are swapped: in LQR, the dynamics is the constraint and the output cost is the objective; in Kalman, the dynamics is the constraint *and* the measurement residual is the objective. Both reduce to the same KKT system with block-banded structure.

> [!note]- Derivation
> Specifically, the LQR KKT matrix and the Kalman KKT matrix are *transposes* of each other (under appropriate identifications). This is the deep "duality" of optimal control and estimation: the optimal feedback law and the optimal estimator are computed by the same algorithm, just with different inputs. In the time-invariant infinite-horizon limit, the duality becomes exact: the LQR optimal-feedback gain is the *transpose* of the Kalman optimal-filter gain (with appropriate normalizations). This is the *separation principle* of LQG control.

> [!note]- Complete formal solution
> *Step 1:* Stack $z = (x_1, \ldots, x_T, u_1, \ldots, u_{T-1})$. The cost $J = \|\tilde{A} z\|^2$ with $\tilde{A}$ block-diagonal containing $C_1, \ldots, C_T$ on the state blocks and $\sqrt{\rho} I, \ldots, \sqrt{\rho} I$ on the input blocks. The constraints $\tilde{C} z = \tilde{d}$ encode the dynamics (block-banded with bandwidth $\max\{n, m\}$) and boundary conditions.
>
> *Step 2:* Apply [[Thm - Constrained Least Squares via KKT System]]. The KKT matrix $M$ inherits the block-banded structure of $\tilde{C}$ (since $\tilde{A}^T \tilde{A}$ is block-diagonal). Sparse banded LU solves $M (z, \nu)^T = (0, \tilde{d})^T$ in $O(T (n+m)^2)$ flops.
>
> *Step 3:* Since $\tilde{d}$ depends linearly on $(x_{\text{init}}, x_{\text{des}})$ and the KKT matrix is fixed, the solution $\hat{z}$ — in particular $\hat{u}_1$ — is linear in $(x_{\text{init}}, x_{\text{des}})$. Setting $x_{\text{des}} = 0$ gives $\hat{u}_1 = K x_{\text{init}}$ for a matrix $K$ computable by solving the KKT system at $n$ basis-vector initial conditions.
>
> *Step 4:* The control-estimation duality is the observation that the same block-banded KKT structure governs LQR and Kalman estimation, with control inputs and process noise playing dual roles. The separation principle of LQG is the limiting statement that the optimal stochastic LQR controller separates into "estimate the state via Kalman" + "apply LQR feedback to the estimate." $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to solve the LQR problem by *dynamic programming*: at each time step, compute the optimal value function $V_t(x)$ recursively backward from $V_T(x_T) = 0$, with $V_t(x) = \min_u \|C_t x\|^2 + \rho \|u\|^2 + V_{t+1}(A_t x + B_t u)$. This is the *Bellman equation* approach and gives the same answer, with the value function quadratic ($V_t(x) = x^T P_t x$) and the matrices $P_t$ satisfying a backward recursion (the *Riccati equation*). The Bellman approach is *equivalent* to the KKT approach we just did — both solve the same sparse linear system — but the Bellman approach hides the underlying constrained-LS structure. The KKT approach makes explicit that LQR is a single LS problem, unifying it with the rest of §XI.3-§XI.4.

---

# Key Takeaways

**Stacking converts trajectory-level optimization to a single LS problem.**

The most important conceptual move in this exercise is the stacking $z = (x_1, \ldots, x_T, u_1, \ldots, u_{T-1})$. A "control problem" that *looks* like it's about choosing a sequence of inputs becomes, after stacking, a single high-dimensional constrained LS problem. The dynamics constraints become block-banded; the cost becomes block-diagonal. Once stacked, all the §XI.3 machinery (KKT systems, sparse solvers, linearity in data) applies unchanged. The trigger for using this transformation: *any* trajectory-level quadratic optimization problem with linear dynamics and quadratic cost.

**The block-banded structure of the KKT matrix is what makes LQR computationally tractable.**

If the KKT matrix were dense (no sparsity), solving an LQR problem with $T = 100$ time steps would cost $O(T^3) = 10^6$ block operations — feasible but slow. With block-banded structure (each dynamics step couples only consecutive time blocks), sparse banded LU solves the same system in $O(T) = 100$ block operations — 4 orders of magnitude faster. The block-banded sparsity is *not* a coincidence; it is the algebraic shadow of the *Markov property* of the dynamics (current state depends only on previous state, not history). The recursive Riccati equation algorithm is exactly the sparse banded LU written in recursive form, and the same Markov-property sparsity underlies Kalman filtering and HMM forward-backward algorithms.

**Linear state feedback is the runtime simplification of a precomputed KKT solve.**

The most important practical takeaway is that *once the gain matrix $K$ is computed offline*, the online control law is just $u = Kx$ — a matrix-vector multiply. This is what makes LQR the most widely-deployed optimal-control framework in industry: design the controller offline (solve the KKT system once), then run it at high frequency (matrix-vector multiply per time step). The whole controller-design problem is solved once, and the controller becomes a stateless function. This is the *certainty-equivalence* principle at work: the optimal controller depends linearly on the state, with the dependence captured by a fixed precomputed matrix.

**Control and estimation are duals — same KKT structure, opposite interpretation.**

The deepest insight is that LQR and Kalman estimation are *dual problems*: same KKT structure, same sparsity, same algorithms, but with the roles of "input" and "output" swapped. The separation principle of LQG — that the optimal stochastic LQR controller separates into "estimate state via Kalman" + "apply LQR feedback to estimate" — is the deepest statement of this duality. The constrained-LS framework here is the unifying mathematical scaffold; everything in optimal control and filtering builds on it.

This exercise is the entry point to optimal control theory. Generalizations include: infinite-horizon LQR (Riccati equation), continuous-time LQR (Hamilton-Jacobi-Bellman PDE), stochastic LQG (separation principle), robust $H^\infty$ control (worst-case disturbances), and model predictive control (receding-horizon LQR with constraints). All build on the constrained-LS / KKT framework here.
