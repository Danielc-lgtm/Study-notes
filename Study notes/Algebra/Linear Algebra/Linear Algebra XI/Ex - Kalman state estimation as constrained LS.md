---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Linear Quadratic State Estimation"
  - "Def - Constrained Least Squares"
  - "Def - KKT System"
tags: [algebra, linear-algebra, applied, estimation, kalman-filter]
---

# Problem Statement

You are given a linear dynamical system
$$x_{t+1} = A_t x_t + B_t w_t, \quad y_t = C_t x_t + v_t, \quad t = 1, \ldots, T,$$
with state $x_t \in \mathbb{R}^n$, process noise $w_t \in \mathbb{R}^m$, measurement $y_t \in \mathbb{R}^p$, measurement noise $v_t \in \mathbb{R}^p$. The matrices $A_t, B_t, C_t$ are known. The measurements $y_1, \ldots, y_T$ are observed; the state sequence $x_1, \ldots, x_T$ and process-noise sequence $w_1, \ldots, w_{T-1}$ are to be *estimated*.

Set up the *batch* Kalman state-estimation problem as a single large constrained LS problem:
$$\min_{x_1, \ldots, x_T, w_1, \ldots, w_{T-1}} \sum_{t=1}^T \|y_t - C_t x_t\|^2 + \lambda \sum_{t=1}^{T-1} \|w_t\|^2 \quad \text{subject to} \quad x_{t+1} = A_t x_t + B_t w_t,$$
where $\lambda > 0$ trades trust in measurements (small $\lambda$) against trust in the model (large $\lambda$).

1. Stack the variables into $z$ and identify the constrained LS matrices $\tilde{A}, \tilde{b}, \tilde{C}, \tilde{d}$.
2. Write the KKT system. Verify the block-banded sparsity structure (same as LQR — control-estimation duality).
3. Verify that as $\lambda \to \infty$, the estimated state trajectory satisfies the noise-free dynamics and minimizes measurement residuals (essentially fits the best initial condition).
4. Use validation on held-out measurements to choose $\lambda$: remove some measurements, run Kalman with the rest, and compare the filter's *prediction* of the held-out measurements against the actual ones. Sweep $\lambda$ to find the value that minimizes test prediction error.

**Recall:**

[[Def - Linear Quadratic State Estimation|Linear quadratic state estimation]] is constrained LS on a time-series variable, where the dynamics is the constraint and the measurement consistency + process-noise smallness is the objective. The KKT system has the same block-banded structure as LQR — *control-estimation duality* (see [[Ex - Linear quadratic control via constrained LS]]).

[[Def - Validation (Training and Test Error)|Validation]] on held-out measurements is the standard method for choosing $\lambda$.

---

# Convergent Strategy

**Problem class:** This is *time-series-constrained quadratic estimation* — the *dual* of LQR (which is time-series-constrained quadratic *control*). The same KKT structure applies; the interpretations differ. The class is "estimate a latent state trajectory from noisy linear observations by minimizing measurement residual + process-noise smallness, subject to dynamics."

**Assumption pattern:** Given measurements $y_1, \ldots, y_T$ and system matrices $A_t, B_t, C_t$. Three assumptions are needed: (i) the measurements have positive informativeness (the matrices $C_t$ are not zero, so we can extract some information from each $y_t$); (ii) the dynamics constraints are linearly independent (true if $B_t$ has full column rank for at least most $t$); (iii) the joint problem is identifiable (each state $x_t$ is connected to at least one measurement, or to a state that is, through the dynamics).

**Theorem routing:** Stack the variables into $z = (x_1, \ldots, x_T, w_1, \ldots, w_{T-1})$. Identify the LS objective as $J = \|\tilde{A} z - \tilde{b}\|^2$ with $\tilde{A}$ containing $C_t$ blocks for the measurement terms and $\sqrt{\lambda} I$ blocks for the process-noise terms, and $\tilde{b}$ containing the measurements $y_t$. The dynamics constraints $\tilde{C} z = 0$ are block-banded (same as LQR). Apply [[Thm - Constrained Least Squares via KKT System]] to write the KKT system; exploit sparsity to solve in $O(T)$ flops.

**Key decision point:** The non-obvious step is the *role of the regularization parameter $\lambda$*. In LQR, $\rho$ was the input cost; here, $\lambda$ is the trust in the dynamics model relative to the measurements. Small $\lambda$ means we trust the measurements (low penalty on $\|w_t\|$, so the dynamics can be violated through "process noise"); large $\lambda$ means we trust the model (high penalty on $\|w_t\|$, so process noise is small and the trajectory closely follows the noise-free dynamics). The right $\lambda$ depends on the actual noise levels, chosen by validation.

---

# Legal Operations Used

1. **Build the KKT system for an equality-constrained problem.** (Operation 5 from the topic page.) The dynamics is the constraint. The cost combines measurement consistency and process-noise smallness.

2. **Stack matrices to reduce a structured problem to LS.** (Operation 3.) Stacking the time-series variable converts the temporally indexed problem into a single big LS problem.

3. **Exploit sparsity in time-series LS problems.** (Operation 10.) The KKT matrix is block-banded; sparse banded LU solves in $O(T)$ flops. The recursive Kalman filter is exactly this sparse solver, written sequentially to process measurements one at a time.

4. **Split-and-validate to choose a regularization parameter.** (Operation 9.) Remove some measurements, run the estimator on the rest, predict the held-out measurements, choose $\lambda$ to minimize prediction error.

---

# Hints

> [!note]- Hint 1
> Stack $z = (x_1, x_2, \ldots, x_T, w_1, w_2, \ldots, w_{T-1})$. The objective is $J = J_{\text{meas}} + \lambda J_{\text{proc}}$.

> [!note]- Hint 2
> $J_{\text{meas}} = \sum_t \|y_t - C_t x_t\|^2$ is a sum of squared norms of *measurement residuals* — it has the LS form with $C_t$ blocks acting on $x_t$ and $-y_t$ on the right-hand side.

> [!note]- Hint 3
> $J_{\text{proc}} = \sum_t \|w_t\|^2$ is a sum of squared norms of process noises — it has the LS form with $\sqrt{\lambda} I$ blocks acting on $w_t$ and zero on the right-hand side.

> [!note]- Hint 4 (for duality)
> Compare with the LQR KKT system from [[Ex - Linear quadratic control via constrained LS]]: same block-banded structure, with control inputs $u_t$ ↔ process noise $w_t$, output cost $\|C_t x_t\|^2$ ↔ measurement residual $\|C_t x_t - y_t\|^2$. This is the *control-estimation duality*.

---

# Solution

The proof has four parts. Step 1 stacks the variables into the constrained LS framework. Step 2 writes the KKT system and identifies the block-banded sparsity. Step 3 examines the $\lambda \to \infty$ limit. Step 4 demonstrates validation for choosing $\lambda$.

**Step 1: Set up the constrained LS problem.**

Let $z = (x_1, x_2, \ldots, x_T, w_1, w_2, \ldots, w_{T-1})$, of [[Def - Dimension|dimension]] $Tn + (T-1)m$. The cost is
$$J = \sum_{t=1}^T \|y_t - C_t x_t\|^2 + \lambda \sum_{t=1}^{T-1} \|w_t\|^2.$$
This has LS form $J = \|\tilde{A} z - \tilde{b}\|^2$ with:

> [!note]- Derivation
> $\tilde{A}$ is block-diagonal:
> $$\tilde{A} = \begin{pmatrix} C_1 & & & & & & \\ & \ddots & & & & & \\ & & C_T & & & & \\ & & & \sqrt{\lambda} I_m & & & \\ & & & & \ddots & & \\ & & & & & \sqrt{\lambda} I_m \end{pmatrix},$$
> with $C_1, \ldots, C_T$ on the state blocks and $\sqrt{\lambda} I_m$ on the process-noise blocks.
>
> $\tilde{b}$ has measurements on the state blocks and zeros on the process-noise blocks:
> $$\tilde{b} = (y_1, y_2, \ldots, y_T, 0, 0, \ldots, 0).$$
>
> The dynamics constraints $x_{t+1} = A_t x_t + B_t w_t$ become $\tilde{C} z = 0$ with $\tilde{C}$ block-banded: each row has $-A_t$ at column $x_t$, $I$ at column $x_{t+1}$, $-B_t$ at column $w_t$, zeros elsewhere. The right-hand side $\tilde{d} = 0$.

**Step 2: KKT system and block-banded sparsity.**

The KKT system is
$$\begin{pmatrix} 2 \tilde{A}^T \tilde{A} & \tilde{C}^T \\ \tilde{C} & 0 \end{pmatrix} \begin{pmatrix} z \\ \nu \end{pmatrix} = \begin{pmatrix} 2 \tilde{A}^T \tilde{b} \\ 0 \end{pmatrix}.$$

> [!note]- Derivation
> $\tilde{A}^T \tilde{A}$ is block-diagonal with $C_t^T C_t$ on the state blocks and $\lambda I_m$ on the noise blocks. $\tilde{A}^T \tilde{b}$ has $C_t^T y_t$ on the state blocks and zeros on the noise blocks.
>
> The KKT matrix has block-banded structure inherited from $\tilde{C}$: bandwidth $\max\{n, m\}$. Sparse banded LU solves in $O(T(n + m + p)(n + m)^2)$ flops — *linear* in $T$.
>
> The *recursive Kalman filter* is exactly this sparse banded LU written sequentially: process the measurements one at a time, maintaining an estimate $\hat{x}_{t|t-1}$ (a priori, before measurement) and $\hat{x}_{t|t}$ (a posteriori, after measurement). The Kalman gain $K_t$ encodes how much the new measurement updates the prior estimate; it is computed from the (recursively maintained) covariance matrix.

**Step 3: $\lambda \to \infty$ limit.**

As $\lambda \to \infty$, the penalty on process noise $\|w_t\|^2$ dominates, forcing $w_t \to 0$. The constraint $x_{t+1} = A_t x_t$ (with $w_t = 0$) becomes the *noise-free* dynamics. The state trajectory is then *determined* by the initial state $x_1$, evolving deterministically: $x_t = A_{t-1} A_{t-2} \cdots A_1 x_1$. The remaining problem is choosing $x_1$ to minimize the measurement residual sum:
$$\hat{x}_1 = \arg\min_{x_1} \sum_t \|y_t - C_t A_{t-1} \cdots A_1 x_1\|^2.$$
This is an ordinary LS problem in $x_1$ — fit the best initial condition to the observed measurements assuming deterministic dynamics.

> [!note]- Derivation
> The limit $\lambda \to \infty$ is the *high-trust-in-model* regime: the estimated trajectory follows the dynamics exactly, with no process noise; the measurement residuals are minimized over the single remaining degree of freedom (the initial condition). This is the appropriate limit when measurement noise is large relative to actual process noise.
>
> The opposite limit $\lambda \to 0^+$ is the *low-trust-in-model* regime: the dynamics is essentially ignored, and each $x_t$ is estimated independently from the corresponding $y_t$ (when $C_t$ is invertible). This is appropriate when measurement noise is small but the model is unreliable.

**Step 4: [[Def - Validation (Training and Test Error)|Validation]] for choosing $\lambda$.**

Randomly remove $\sim 20\%$ of the measurements (the held-out set $\mathcal{H}$). Run the Kalman filter on the remaining $80\%$ ($\mathcal{T}$) with various $\lambda$ values. For each $\lambda$, the filter produces a state estimate $\hat{x}_t(\lambda)$, from which we can *predict* the held-out measurements:
$$\hat{y}_t = C_t \hat{x}_t(\lambda), \quad t \in \mathcal{H}.$$
The *test prediction RMS error* is
$$\mathrm{RMS}_{\text{test}}(\lambda) = \sqrt{\frac{1}{|\mathcal{H}|} \sum_{t \in \mathcal{H}} \|y_t - \hat{y}_t\|^2}.$$
Sweep $\lambda$ over a logarithmic grid; choose $\lambda^*$ minimizing $\mathrm{RMS}_{\text{test}}$.

> [!note]- Derivation
> Boyd's example in §17.3.3 demonstrates this. For a 4D linear dynamical system with 2D measurements and 100 time steps, $\lambda$ swept over $[10^{-3}, 10^5]$:
> - Small $\lambda$ ($< 1$): the filter trusts measurements too much; the estimated trajectory is jittery and follows measurement noise. Training RMS small (fits training measurements well), but test RMS large (does not predict held-out measurements).
> - Large $\lambda$ ($> 10^4$): the filter trusts the dynamics too much; the estimated trajectory is over-smoothed. Training RMS large (cannot fit measurements due to model constraint), test RMS also large.
> - Intermediate $\lambda$ ($\approx 10^3$ in this example): the filter balances measurement trust and model trust. Both training and test RMS are small.
>
> The optimal $\lambda^* \approx 10^3$ gives a good estimate of the true state trajectory, recoverable by either batch KKT solve or recursive Kalman filter.

> [!note]- Complete formal solution
> *Step 1:* Stack $z = (x_1, \ldots, x_T, w_1, \ldots, w_{T-1})$. The cost is $J = \|\tilde{A} z - \tilde{b}\|^2$ with $\tilde{A}$ block-diagonal (containing $C_t$ on state blocks and $\sqrt{\lambda} I$ on noise blocks) and $\tilde{b} = (y_1, \ldots, y_T, 0, \ldots, 0)$. The dynamics constraints are $\tilde{C} z = 0$ with $\tilde{C}$ block-banded (bandwidth $\max\{n, m\}$).
>
> *Step 2:* Apply [[Thm - Constrained Least Squares via KKT System]]. The KKT matrix has block-banded structure inherited from $\tilde{C}$. Sparse banded LU solves it in $O(T)$ flops. The recursive Kalman filter is exactly this sparse solver written sequentially.
>
> *Step 3:* As $\lambda \to \infty$, the process-noise penalty dominates, forcing $w_t \to 0$. The state trajectory becomes deterministic via the noise-free dynamics, parametrized by the initial condition $x_1$, which is fit by LS to the measurements.
>
> *Step 4:* Choose $\lambda$ by validation: hold out $\sim 20\%$ of measurements, run the filter on the rest, compare predicted vs. actual held-out measurements. The $\lambda^*$ minimizing test prediction error is the optimal choice; typical values are in $[10^2, 10^4]$ for problems with moderate noise levels.
>
> The whole framework — batch constrained LS, KKT system, sparse banded LU, validation — is the same as for LQR (control-estimation duality), just with different interpretations of the matrices. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to *invert each measurement equation directly*: at each $t$, compute $\hat{x}_t = C_t^+ y_t$ (the LS fit to the single measurement). This is the $\lambda \to 0^+$ limit and gives noisy, jittery state estimates that violate the dynamics. The Kalman filter's improvement is that it *combines* the measurement with the prior estimate from the dynamics, *smoothing* the noise. The illegal alternative ignores the dynamics; the legal approach uses the dynamics constraint to combine information across time.

---

# Key Takeaways

**The recursive Kalman filter is the sparse banded LU of the batch KKT system, written sequentially.**

The connection between the batch constrained-LS formulation and the recursive Kalman filter is deep but exact. The batch formulation gives a sparse linear system whose solution is the entire state trajectory; the recursive filter processes measurements one at a time, maintaining a running state estimate and its covariance. These are *the same algorithm*, just at different levels of abstraction. The batch view emphasizes the *constrained LS structure*; the recursive view emphasizes the *streaming computation*. Both perspectives illuminate the algorithm: the batch view connects it to LQR (duality), Markowitz portfolio (constrained LS), and general optimization theory; the recursive view connects it to Bayesian filtering, hidden Markov models, and online learning.

**Control and estimation are KKT-dual problems — same algorithm, swapped interpretations.**

The deepest unification of §XI.4 is that LQR (Boyd §17.2) and Kalman state estimation (Boyd §17.3) have the *same* sparse banded KKT structure, with control inputs $u_t$ and process noise $w_t$ playing dual roles, and output cost and measurement residual swapping objective/constraint placement. This duality is the foundation of LQG (Linear Quadratic Gaussian) control, which combines LQR + Kalman: estimate the state via Kalman, apply LQR feedback to the estimate. The *separation principle* says this is optimal — you can design the estimator and controller independently and combine them. The shared KKT framework is the mathematical basis of this principle.

**[[Def - Validation (Training and Test Error)|Validation]] for $\lambda$ uses held-out measurements as proxy for unknown future data.**

The Kalman filter's regularization parameter $\lambda$ trades measurement-trust against model-trust. There is no a priori "right" value; it depends on the actual (unknown) noise levels. The validation procedure — hold out some measurements, run filter on the rest, compare predictions to actual measurements — directly estimates the *generalization error* of the filter. This is the *same validation principle* as in [[Def - Validation (Training and Test Error)|cross-validation for regression]] and the *same trigger-reaction pattern*: when a model has a free hyperparameter, choose it by validation against held-out data. The trigger: *any* free hyperparameter; the reaction: validate.

This exercise is the entry point to a vast and deep field: state estimation in linear systems, Kalman filtering, Bayesian filtering, particle filtering, and more. Generalizations include: continuous-time Kalman-Bucy filter, nonlinear extended Kalman filter (EKF), unscented Kalman filter (UKF), and particle filters for non-Gaussian / nonlinear systems. All build on the constrained-LS / KKT framework here, with various approximations to handle non-Gaussianity or nonlinearity. The deepest theoretical connection is to **Bayesian Networks** and graphical-model inference: the Kalman filter is the special case of inference in a *Gaussian-linear chain graphical model*, and the recursive forward-backward algorithm generalizes to general probabilistic graphical models.
