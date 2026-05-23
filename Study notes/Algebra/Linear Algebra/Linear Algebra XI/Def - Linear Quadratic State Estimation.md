---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Constrained Least Squares"
  - "Def - KKT System"
  - "Def - Linear Quadratic Control"
tags: [algebra, linear-algebra, applied, estimation, kalman-filter]
---

# Notation

A discrete-time linear dynamical system has state $x_t \in \mathbb{R}^n$, *process noise* $w_t \in \mathbb{R}^m$, and *measurement noise* $v_t \in \mathbb{R}^p$. The dynamics is $x_{t+1} = A_t x_t + B_t w_t$ and the measurement is $y_t = C_t x_t + v_t$. The matrices $A_t, B_t, C_t$ are known. The measurements $y_1, \ldots, y_T$ are observed; the state trajectory $x_1, \ldots, x_T$ is to be estimated.

The cost function has *primary objective* $J_{\text{meas}} = \sum_t \|y_t - C_t x_t\|^2 = \sum_t \|v_t\|^2$ (measurement residual) and *secondary objective* $J_{\text{proc}} = \sum_t \|w_t\|^2$ (process noise). The regularization parameter $\lambda > 0$ trades trust in measurements (small $\lambda$) against trust in the model (large $\lambda$).

---

# Axiom Motivation

You have a system whose state $x_t$ evolves over time according to known but *noisy* dynamics, and you observe noisy linear measurements $y_t$ of that state. The question is: given the measurement sequence $y_1, \ldots, y_T$, can you estimate the underlying state sequence $x_1, \ldots, x_T$?

This is the *state estimation* problem, and it is the dual of the LQ control problem: in control, you *choose* the inputs to drive the state somewhere; in estimation, you *observe* measurements to figure out what the state has been doing.

Three concerns shape the formulation.

(i) *The measurements should be consistent with the state estimate.* If the true measurement is $y_t = C_t x_t + v_t$ for small noise $v_t$, then the estimated state $\hat{x}_t$ should satisfy $\|y_t - C_t \hat{x}_t\|^2$ small. Call this $J_{\text{meas}} = \sum_t \|y_t - C_t x_t\|^2$.

(ii) *The state trajectory should be consistent with the dynamics.* The state evolves according to $x_{t+1} = A_t x_t + B_t w_t$, with $w_t$ a process-noise vector that we expect to be small. Our state estimate $\hat{x}_t$ should evolve according to (approximately) the same rule, with small implied process noise $\hat{w}_t = (x_{t+1} - A_t x_t)$. Call this $J_{\text{proc}} = \sum_t \|w_t\|^2$.

(iii) *We do not know the noise sequences.* Only the matrices $A_t, B_t, C_t$ and the measurements $y_t$ are observed. The noises $w_t, v_t$ are unknown.

The natural formulation is to *choose* the state trajectory $x_1, \ldots, x_T$ and the process-noise sequence $w_1, \ldots, w_{T-1}$ that *minimize* the weighted sum of the two cost terms, subject to the dynamics constraint:
$$\min J_{\text{meas}} + \lambda J_{\text{proc}} \quad \text{subject to} \quad x_{t+1} = A_t x_t + B_t w_t \text{ for all } t.$$

The role of $\lambda$ is similar to in LQ control: it trades the two objectives. Small $\lambda$ trusts the measurements (the state is estimated to fit measurements closely, possibly at the cost of jumpy dynamics); large $\lambda$ trusts the dynamics (the state evolves smoothly according to the model, possibly at the cost of fitting measurements poorly). The right $\lambda$ depends on the noise levels.

The astonishing observation is that *this is the same constrained LS problem as LQR*, just with a different interpretation of what is given and what is being estimated. Stack $z = (x_1, \ldots, x_T, w_1, \ldots, w_{T-1})$. The cost $J_{\text{meas}} + \lambda J_{\text{proc}}$ is a quadratic function of $z$ — specifically, $\|\tilde{A} z - \tilde{b}\|^2$ for a particular sparse $\tilde{A}$ (with $C_t$ blocks for measurement residuals and $\sqrt{\lambda}$ identity blocks for process noise) and right-hand side $\tilde{b}$ (with measurements $y_t$ in the appropriate slots, zeros elsewhere). The dynamics constraints are linear in $z$: $\tilde{C} z = 0$.

The KKT system has *block-banded* structure (each dynamics constraint couples only adjacent time blocks), and the sparse solve runs in $O(T)$ flops. This is the *batch Kalman filter* — the entire state trajectory estimated at once by solving one large sparse linear system.

The recursive *Kalman filter* algorithm — far more famous than the batch form — is the same algorithm written sequentially. Process measurements one at a time, updating the estimate after each. The recursive form has the advantage that it can run *online* (no need to store all measurements; just maintain a running state estimate and its covariance). It also gives explicit *Kalman gain* matrices that have natural interpretation as the relative weights of measurement vs. prior.

The Bayesian / probabilistic interpretation is exact: under Gaussian process and measurement noise, the LS-based state estimate equals the posterior mean of the state given the measurements. This is the conditional-expectation form of the Kalman filter, derived in stochastic-processes textbooks. The connection to this chapter: under Gaussian assumptions, *the MAP and posterior-mean estimators coincide* (both being the posterior mode of a Gaussian), and both equal the constrained-LS solution. The batch Kalman filter and the recursive Kalman filter agree exactly; the difference is computational order, not result.

Two extensions deserve mention:

(i) *Known initial state*: add $x_1 = x_1^{\text{known}}$ as an additional equality constraint.

(ii) *Missing measurements*: if not all $y_t$ are observed, restrict $J_{\text{meas}}$ to the observed time indices. The variables for unobserved $y_t$ effectively become free (or, equivalently, treated with infinite measurement noise — large $\lambda^{-1}$). The estimated $\hat{x}_t$ at the missing times is determined entirely by neighboring observations through the dynamics.

The reader has now invented the Kalman filter. The recursive form is the computational implementation; the batch form is the constrained-LS understanding.

---

# The Definition

> **Definition (Linear Quadratic State Estimation, Kalman Filter).** Given a linear dynamical system
> $$x_{t+1} = A_t x_t + B_t w_t, \quad y_t = C_t x_t + v_t, \quad t = 1, \ldots, T,$$
> with known matrices $A_t, B_t, C_t$ and observed measurements $y_1, \ldots, y_T$, the *linear quadratic state estimation problem* (or *Kalman filtering problem*, in its batch LS form) is to find the state sequence $x_1, \ldots, x_T$ and process-noise sequence $w_1, \ldots, w_{T-1}$ that minimize
> $$J = J_{\text{meas}} + \lambda J_{\text{proc}} = \sum_{t=1}^T \|y_t - C_t x_t\|^2 + \lambda \sum_{t=1}^{T-1} \|w_t\|^2,$$
> subject to the dynamics constraints, where $\lambda > 0$ trades trust in measurements (small $\lambda$) against trust in the model (large $\lambda$).
>
> *Reformulation as constrained LS:* stacking $z = (x_1, \ldots, x_T, w_1, \ldots, w_{T-1})$, the problem becomes
> $$\min \|\tilde{A} z - \tilde{b}\|^2 \quad \text{subject to} \quad \tilde{C} z = 0,$$
> for specific sparse matrices $\tilde{A}, \tilde{C}$ and a measurement vector $\tilde{b}$. The block-banded sparsity allows solution in $O(T(m + p + n)(m + n)^2)$ flops via sparse KKT methods.
>
> *Recursive form*: when measurements arrive sequentially, the same problem can be solved recursively by maintaining an *a priori* estimate $\hat{x}_{t|t-1}$ and updating to the *a posteriori* estimate $\hat{x}_{t|t}$ via the Kalman gain
> $$\hat{x}_{t|t} = \hat{x}_{t|t-1} + K_t (y_t - C_t \hat{x}_{t|t-1}),$$
> where $K_t$ is computed from the (recursively maintained) covariance matrix and the noise parameters. The recursive form coincides exactly with the batch solution.

---

# Relate to Other Fields / Compression

**True name:** linear quadratic state estimation is *constrained LS on a time-series variable, with dynamics as constraint and measurement consistency as objective*. It is the *dual* of LQ control: same KKT structure, opposite interpretation (observe vs. choose, estimate vs. drive). The Kalman filter is the recursive sparse solver.

This is the same construction as:
- **Bayesian Filtering**: in the probabilistic framework with Gaussian noises, the posterior $p(x_{1:T} | y_{1:T})$ is Gaussian, and the Kalman filter computes its mean. The recursive Bayes-rule update of the posterior coincides with the recursive Kalman update.
- **Particle Filtering** (Sequential Monte Carlo): the non-Gaussian / nonlinear generalization, where the posterior is represented by samples ("particles") and updated by importance sampling. Reduces to Kalman filtering in the linear-Gaussian case.
- **HMM Forward-Backward Algorithm** (hidden Markov models): the discrete-state analog of Kalman filtering, where the state space is finite rather than continuous. Both are sparse-graph inference algorithms with the same structural pattern (forward pass + backward pass on a chain).
- **Smoothing Splines** (statistics): fit a smooth function to noisy observations by minimizing $\sum \|f(t_i) - y_i\|^2 + \lambda \int |f''|^2$. The continuous-state version of Kalman filtering for a smooth-trajectory prior.

---

# Examples / Corollaries

*Example 1 (constant-velocity tracking).* For a mass moving in 1D with state $x_t = (\text{position}_t, \text{velocity}_t)$ and dynamics $x_{t+1} = \begin{pmatrix} 1 & \Delta t \\ 0 & 1 \end{pmatrix} x_t + B w_t$ (with $B$ governing how the noise drives the state), and measurements $y_t =$ position $+ v_t$, the Kalman filter recovers smoothed position and velocity estimates from noisy position measurements. The choice of $\lambda$ controls how much smoothing is applied.

*Example 2 (2D position tracking with noisy radar).* The example in Boyd §17.3.1 has a 4D state (2D position + 2D velocity), 2D measurements (noisy position), and shows the filtered trajectory $\hat{x}_t$ as $\lambda$ varies. For $\lambda = 1$, the filter trusts measurements too much (jumpy); for $\lambda = 10^5$, it trusts the dynamics too much (over-smoothed); the right value (around $\lambda = 10^3$) gives a smooth trajectory close to the true path.

*Example 3 (the dual of LQR).* Compare the LQR problem $\min \sum \|y_t\|^2 + \rho \sum \|u_t\|^2$ s.t. $x_{t+1} = A_t x_t + B_t u_t, x_1 = x_{\text{init}}$ with the estimation problem $\min \sum \|y_t - C_t x_t\|^2 + \lambda \sum \|w_t\|^2$ s.t. $x_{t+1} = A_t x_t + B_t w_t$. They have identical KKT structure, with the substitution $u_t \leftrightarrow w_t$ (control input ↔ process noise) and a swap of which residuals are in the objective vs. constraint. This is the *control/estimation duality*.

*Example 4 (NOT a Kalman filter — nonlinear dynamics).* If $x_{t+1} = f(x_t, w_t)$ is nonlinear, the Kalman filter (which is LS-based and assumes linear dynamics) does not directly apply. The *extended Kalman filter* (EKF) linearizes the dynamics around the current estimate and applies KF locally; the *unscented Kalman filter* (UKF) uses deterministic sampling. For severely nonlinear or non-Gaussian problems, particle filters are needed.

*Example 5 ([[Def - Validation (Training and Test Error)|validation]] for $\lambda$).* In the missing-measurement variant, randomly remove some measurements, run the Kalman filter on the remaining ones for a range of $\lambda$, and compare the filter's *prediction* of the missing measurements against their actual values. This gives a held-out evaluation procedure for choosing $\lambda$, analogous to cross-[[Def - Validation (Training and Test Error)|validation]] in regression. Boyd §17.3.3 demonstrates this on the 2D tracking example.

**Calibration check.** Verify: (i) for a noise-free linear system with full measurements ($v_t = 0, w_t = 0$), the Kalman filter recovers the true state exactly (the KKT system gives zero objective at the true trajectory, which is the unique feasible point); (ii) as $\lambda \to \infty$, the estimated state evolves according to the noise-free dynamics from the best-fit initial condition; (iii) as $\lambda \to 0^+$, the estimated state ignores the dynamics and at each step is the least-norm fit to that step's measurements.

---

# Unlocked by This

> [!tip] Kalman-Bucy Filter *(from Stochastic Control)*
> The continuous-time analog of the Kalman filter is the **Kalman-Bucy filter**, governing state estimation for a continuous-time linear stochastic system $dx = A x \, dt + B \, dW$, $y = C x \, dt + dV$ (with $W, V$ Brownian motions). The estimate satisfies a stochastic differential equation, and the conditional covariance satisfies the *matrix Riccati ODE*. Derivations use stochastic calculus (Itô's formula), but the result is the continuous analog of the discrete-time Kalman update.

> [!tip] Separation Principle in LQG *(from Optimal Control)*
> The **separation principle** of LQG control states that the optimal controller for a stochastic LQ system with noisy measurements *separates* into two stages: (i) estimate the state via Kalman filter, (ii) apply the LQR feedback to the estimated state. This decouples estimation from control and is the foundation of *certainty equivalence* in stochastic optimal control. It is a deep theorem with profound practical consequences: design the filter and controller independently and they combine to be optimal.

> [!tip] Bayesian Networks and Graphical Models *(from Probabilistic ML)*
> The Kalman filter is a special case of inference in a *Gaussian-linear chain graphical model*. The graphical structure (state at time $t$ depends only on state at $t-1$ and the measurement at $t$) makes the inference tractable via belief propagation along the chain. The same algorithmic pattern (forward-backward) handles HMMs (discrete states), MRFs (general graphs), and more. Modern probabilistic programming languages (Stan, PyMC) automate this for arbitrary models.

> [!tip] State-Space Models in Time-Series Econometrics *(from Econometrics)*
> Macroeconomic and financial time series are often modeled as state-space models, where unobserved latent factors (the "state") generate observed economic variables. The Kalman filter estimates these latent factors. Famous examples include the *dynamic factor models* (Stock-Watson), *trend-cycle decompositions* (Beveridge-Nelson), and *real-time business-cycle indicators* (Aruoba-Diebold-Scotti).
