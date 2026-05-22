---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Constrained Least Squares"
  - "Def - KKT System"
tags: [algebra, linear-algebra, applied, control]
---

# Notation

A discrete-time linear dynamical system has *state* $x_t \in \mathbb{R}^n$, *input* $u_t \in \mathbb{R}^m$, and *output* $y_t \in \mathbb{R}^p$ at time step $t = 1, 2, \ldots, T$. The dynamics is $x_{t+1} = A_t x_t + B_t u_t$, with output $y_t = C_t x_t$. The matrices $A_t, B_t, C_t$ are *time-varying* in general (in the *time-invariant* case they are $A, B, C$ independent of $t$). The *time horizon* is $T$.

The *initial state constraint* $x_1 = x_{\text{init}}$ and (optionally) *final state constraint* $x_T = x_{\text{des}}$ are part of the LQ control problem.

The cost function is $J = J_{\text{output}} + \rho J_{\text{input}}$ where $J_{\text{output}} = \sum_t \|y_t\|^2$ and $J_{\text{input}} = \sum_t \|u_t\|^2$. The parameter $\rho > 0$ trades input cost against output deviation.

---

# Axiom Motivation

Suppose you have a system you can influence by feeding it inputs $u_t$ at each time step. The system responds via a linear dynamics rule $x_{t+1} = A_t x_t + B_t u_t$, and you observe a (linear function of the) state $y_t = C_t x_t$. Both the state $x_t$ and the output $y_t$ represent *deviations* from some target operating condition — you want them small, ideally zero.

The question is: how do you choose the input trajectory $u_1, \ldots, u_{T-1}$ over $T$ time steps?

Three competing concerns shape the answer.

(i) *Output deviation must be small.* The output measures how far from target you are; we want $\|y_t\|^2$ summed over $t$ to be small. Call this $J_{\text{output}} = \sum_t \|y_t\|^2$.

(ii) *Input effort must be small.* Inputs cost something — fuel, energy, wear, money. Even if you could drive the output to zero by huge inputs, the cost of doing so makes this undesirable. Call the input cost $J_{\text{input}} = \sum_t \|u_t\|^2$.

(iii) *The dynamics must be obeyed.* The system follows $x_{t+1} = A_t x_t + B_t u_t$ exactly; there is no way around this constraint. The dynamics must be enforced as a hard constraint, not as a soft objective.

The natural formulation is then:
$$\min J_{\text{output}} + \rho J_{\text{input}} \quad \text{subject to dynamics and boundary conditions},$$
where $\rho > 0$ weights the input cost against the output deviation. As $\rho$ varies, we trace out a *Pareto frontier* of (input cost, output deviation) pairs; the choice of $\rho$ depends on the application.

The remarkable observation is that *this is constrained LS*. Stack all the state and input variables into one big vector
$$z = (x_1, x_2, \ldots, x_T, u_1, u_2, \ldots, u_{T-1}) \in \mathbb{R}^{Tn + (T-1)m}.$$
The output cost $J_{\text{output}} + \rho J_{\text{input}}$ is a quadratic function of $z$ — specifically, $\|\tilde{A} z\|^2$ for a particular sparse matrix $\tilde{A}$ assembled from the $C_t$'s (on the state blocks) and $\sqrt{\rho}$ times identity blocks (on the input blocks). The dynamics constraints $x_{t+1} = A_t x_t + B_t u_t$ are linear in $z$ — they can be written as $\tilde{C} z = \tilde{d}$ for a particular sparse matrix $\tilde{C}$ and zero vector $\tilde{d}$. The initial and final state constraints add additional rows to $\tilde{C}$ and $\tilde{d}$.

The whole LQ control problem is then a single constrained LS problem:
$$\min \|\tilde{A} z\|^2 \quad \text{subject to} \quad \tilde{C} z = \tilde{d}.$$
This is exactly the form handled by §XI.3. The KKT system has dimension roughly $T(n + m + p)$ — large, but with a *block-banded* sparsity pattern (only adjacent time blocks couple). Sparse-matrix methods reduce the solve cost from the dense $O(T^3)$ to $O(T)$. The recursive *Riccati equation* algorithm — the standard control-theoretic algorithm for LQ control — is *exactly* this sparse-KKT solver written in recursive form.

The deeper insight is that the *solution is linear in the boundary data $x_{\text{init}}, x_{\text{des}}$*. Since the KKT system is linear in $\tilde{d}$, and $\tilde{d}$ depends linearly on $x_{\text{init}}, x_{\text{des}}$, the solution $z$ — and in particular the first input $u_1$ — is a linear function of the initial state. This gives the *state feedback law*: $u_1 = K x_1$ for some matrix $K$, computed by precomputing the KKT solve for $n$ different initial states ($x_{\text{init}} = e_1, \ldots, e_n$).

Linear state feedback control is the *practical* recipe. Once you have $K$, control becomes trivial: at each time step, measure $x_t$, compute $u_t = K x_t$, apply it. The matrix $K$ is computed offline once; the runtime operation is just a matrix-vector multiply. This is why LQ control is the most widely-deployed optimal-control framework in industrial applications.

Three further extensions deserve mention:

(i) *Tracking*. Replace $y_t$ in $J_{\text{output}}$ with $y_t - y_t^{\text{des}}$, where $y_t^{\text{des}}$ is a desired output trajectory. The setup is unchanged; only the right-hand side $\tilde{b}$ becomes nonzero.

(ii) *Time-weighted cost*. Replace $\|y_t\|^2$ in $J_{\text{output}}$ with $w_t \|y_t\|^2$ for weights $w_t > 0$. Exponential weighting $w_t = \theta^t$ gives a discounted-cost LQR; useful for emphasizing later (or earlier) outputs.

(iii) *Way-point constraints*. Adding $y_\tau = y^{\text{wp}}$ as a hard constraint at a specific time $\tau$ enforces a *waypoint*: the trajectory must pass through a designated point. This is common in vehicle control (drone must visit specific positions).

The reader has now invented LQR; the recursive Riccati equation is the efficient solver, but conceptually LQR is just constrained LS over a time-series variable.

---

# The Definition

> **Definition (Linear Quadratic Control).** Given a linear dynamical system
> $$x_{t+1} = A_t x_t + B_t u_t, \quad y_t = C_t x_t, \quad t = 1, \ldots, T,$$
> with given initial state $x_1 = x_{\text{init}}$ and (optionally) desired final state $x_T = x_{\text{des}}$, the *linear quadratic control problem* (or *LQR* — linear quadratic regulator) is to choose the input trajectory $u_1, \ldots, u_{T-1}$ and the resulting state trajectory $x_1, \ldots, x_T$ to minimize
> $$J = J_{\text{output}} + \rho J_{\text{input}} = \sum_{t=1}^T \|y_t\|^2 + \rho \sum_{t=1}^{T-1} \|u_t\|^2,$$
> subject to the dynamics constraints and the boundary conditions, where $\rho > 0$ trades input effort against output deviation.
>
> *Reformulation as constrained LS:* stacking $z = (x_1, \ldots, x_T, u_1, \ldots, u_{T-1})$, the problem becomes
> $$\min \|\tilde{A} z\|^2 \quad \text{subject to} \quad \tilde{C} z = \tilde{d},$$
> where $\tilde{A}, \tilde{C}, \tilde{d}$ are specific sparse matrices/vectors. The solution is obtained by solving the corresponding KKT system, which exploits sparsity to run in $O(T(m + p + n)(m + n)^2)$ flops.
>
> *Linear state feedback*: since the solution $u_1$ is a linear function of $x_{\text{init}}$, we have $u_1 = K x_{\text{init}}$ for some matrix $K$ (the *state feedback gain matrix*), which can be precomputed and applied recursively.

---

# Relate to Other Fields / Compression

**True name:** LQ control is *constrained LS over a time-series variable*. The "control" framing emphasizes the temporal sequencing and the choice of inputs, but the underlying optimization is the same KKT-solve we have been studying. The recursive Riccati equation, the famous result of optimal control theory, is the *sparse solver* for this particular KKT system.

This is the same construction as:
- **Calculus of Variations**: in continuous time, the LQ control problem becomes minimizing $\int_0^T (y^T y + \rho u^T u) dt$ subject to $\dot{x} = A x + B u$ with given $x(0)$. The Euler-Lagrange equations of this variational problem are the continuous-time Riccati equation, and the solution gives a state-feedback law $u = K x$ for a time-varying gain $K(t)$.
- **Hamilton-Jacobi-Bellman Equations**: the dynamic programming approach to LQ control writes a value function $V(x, t)$ satisfying the HJB equation. For LQ problems, $V$ is quadratic in $x$ and the HJB equation reduces to the Riccati equation for its coefficient matrix.
- **Pontryagin's Maximum Principle**: the general continuous-time optimal control framework, of which LQR is the linear-quadratic special case. The costates (adjoint variables) play the role of Lagrange multipliers.
- **Model Predictive Control (MPC)**: a practical extension of LQR where the control problem is re-solved at each time step over a receding horizon. The KKT-solve structure of LQR is the inner-loop computation of MPC.

---

# Examples / Corollaries

*Example 1 (the trivial open-loop case).* If $\rho = \infty$ (no input allowed, $u_t = 0$ for all $t$), the state evolves freely as $x_{t+1} = A_t x_t$ from the initial condition, and $J_{\text{output}} = \sum \|C_t x_t\|^2$ is fixed. There is no optimization; we just observe the open-loop response.

*Example 2 (the trivial perfect-control case).* If $\rho = 0$ (input is free), we can drive the state to any desired trajectory the dynamics allows. If the boundary condition $x_T = x_{\text{des}}$ is reachable, we can also satisfy it. The output cost $J_{\text{output}}$ can typically be driven to zero (or to a residual reflecting unreachable states).

*Example 3 (LQR for a mass on a frictionless surface).* For a unit mass with state $x_t = (\text{position}_t, \text{velocity}_t)$ and input $u_t = $ force, the dynamics $x_{t+1} = \begin{pmatrix} 1 & \Delta t \\ 0 & 1 \end{pmatrix} x_t + \begin{pmatrix} 0 \\ \Delta t \end{pmatrix} u_t$ is linear. With initial condition $x_1 = (1, 0)$ (position 1, velocity 0) and desired final $x_T = (0, 0)$ (rest at origin), the LQR problem finds the input trajectory that brings the mass home with minimum input energy. The optimal solution is a *bang-bang* approximation: large negative input early to decelerate, large positive input late to stop at origin.

*Example 4 (tracking a step input).* For a system with desired output trajectory $y_t^{\text{des}} = 1$ for all $t$ (step setpoint), the tracking LQR problem $\min \sum \|y_t - 1\|^2 + \rho \sum \|u_t\|^2$ finds the input that drives $y_t$ to 1 as quickly as possible without using excessive input. The transient response (how fast $y_t$ reaches 1 and how much it overshoots) depends on $\rho$.

*Example 5 (NOT LQ control — nonlinear dynamics).* If the dynamics is nonlinear, $x_{t+1} = f(x_t, u_t)$, the problem is no longer LQR. Around an operating point one can linearize and apply LQR (giving a local controller); for global optimization, nonlinear MPC or model-based RL is required. The framework of [[Linear Algebra XII — Applied III — Nonlinear Least Squares]] handles such generalizations.

**Calibration check.** Verify: (i) the LQR problem reduces to ordinary LS in the limit $T = 1$ (just one step, no dynamics propagation); (ii) the KKT system is block-banded with bandwidth $\max\{n, m\}$, allowing $O(T)$ solution by sparse LU; (iii) the linear-state-feedback gain $K$ is *independent* of $x_{\text{init}}$ (the linearity in initial state translates to a fixed feedback rule); (iv) for large $\rho$, the LQR solution has small $u$ (and $x$ takes longer to reach desired); for small $\rho$, $u$ is large and the state reaches desired quickly.

---

# Unlocked by This

> [!tip] Linear Quadratic Gaussian (LQG) *(from Stochastic Control)*
> Adding Gaussian process noise to the dynamics ($x_{t+1} = A_t x_t + B_t u_t + w_t$ with $w_t \sim \mathcal{N}(0, Q)$) and Gaussian measurement noise ($y_t = C_t x_t + v_t$ with $v_t \sim \mathcal{N}(0, R)$) gives the **LQG problem**. The separation principle says the optimal control can be computed in two steps: (i) estimate the state using a Kalman filter (the dual of LQR), (ii) apply the LQR feedback to the estimated state. This decouples estimation from control and is the *certainty equivalence* principle of stochastic optimal control.

> [!tip] Algebraic Riccati Equation *(from Optimal Control)*
> In the infinite-horizon limit $T \to \infty$ for time-invariant LQR, the state-feedback gain $K$ stabilizes and the value-function matrix $P$ satisfies the **algebraic Riccati equation** (ARE)
> $$P = A^T P A - A^T P B (R + B^T P B)^{-1} B^T P A + Q.$$
> The solution $P$ can be found by iteratively solving the time-varying Riccati equation to convergence, or directly by Schur-decomposition methods. The ARE is the cornerstone of modern control theory and unlocks $H^\infty$ control, robust control, and adaptive control.

> [!tip] Model Predictive Control *(from Industrial Control)*
> **Model predictive control (MPC)** solves the LQR problem in a *receding horizon* fashion: at each time step, plan over the next $T$ time steps, apply only the first input, then re-plan from the new state. MPC handles input/state constraints (which LQR ignores in basic form) and is the workhorse of modern process control in chemical plants, refineries, and electric grids. The inner-loop solve at each time step is a KKT-style constrained quadratic problem — exactly the structure of this section.
