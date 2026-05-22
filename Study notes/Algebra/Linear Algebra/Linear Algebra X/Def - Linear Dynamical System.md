---
type: definition
subject: linear-algebra
prereqs:
tags: [algebra, linear-algebra, applied, dynamics]
---

# Notation

Throughout, $x_t \in \mathbb R^n$ is the **state** at discrete time $t = 1, 2, 3, \dots$ The **dynamics matrix** $A_t \in \mathbb R^{n \times n}$ governs the update from time $t$ to time $t + 1$. In the time-invariant case $A_t = A$ is constant. Inputs are $m$-vectors $u_t$ and offsets are $n$-vectors $c_t$; the **input matrix** is $B_t \in \mathbb R^{n \times m}$.

This is a compound page: it defines four interlocking notions — the **state and state trajectory**, the **dynamics matrix and update equation**, the **input form** of the dynamics, and the **time-invariant** and **$K$-Markov** specialisations — because they form the natural unit of "what a linear dynamical system is".

---

# Axiom Motivation

The desideratum is to model a system that evolves over discrete time, with the next state determined by the current state in a particularly simple way: linearly. Many real-world phenomena update by a recurrence — the demographic profile of a country next year is a function of this year's, the share prices tomorrow are a function of today's, the position and velocity of a mechanical system one millisecond later are a function of now's — and in a wide range of cases the dependence is approximately linear or can be made linear by appropriate state augmentation.

The first design choice is: **what counts as the "state"?** The state $x_t$ is the variable that, by definition, contains all the information about the past needed to predict the future. If the next-step rule depends only on $x_t$ — not on $x_{t-1}$, $x_{t-2}$, $\dots$ — then $x_t$ deserves to be called the state. This is the Markov property. If the next step depends on multiple previous values, the state has been chosen too small, and one expands it: a $K$-Markov system with $x_{t+1} = A_1 x_t + \cdots + A_K x_{t-K+1}$ is equivalent to a standard Markov system in the augmented state $z_t = (x_t, x_{t-1}, \dots, x_{t-K+1})$, which has dimension $nK$. This is the principle that *Markovianity is achieved by choosing a large enough state*.

The second design choice is **linearity**: $x_{t+1} = A x_t$ (or $A_t x_t$ if the dynamics matrix can vary). Why linear? Linear dynamics are the simplest non-trivial dependence one can write, and they capture an astonishing variety of phenomena: any system whose update is differentiable can be linearised near an equilibrium (giving local validity), any system whose update is affine becomes linear after a coordinate change to centre on the fixed point, and many phenomena are exactly linear (population dynamics with fixed birth/death rates, electrical circuits with linear components, financial portfolios with deterministic returns). The full theory of *eigenvalues* and *invariant subspaces* of $A$ becomes the theory of long-time behaviour: trajectories decay or grow exponentially according to the eigenvalues of $A$, with rate $|\lambda|^t$.

The third design choice is whether to include **inputs and offsets**. The basic form $x_{t+1} = A x_t$ describes a *closed* system with no external forcing. Adding $B u_t$ accommodates external inputs — control signals, exogenous shocks, immigration in a population model. Adding $c_t$ accommodates time-varying offsets, like seasonal trends. The most general form is $x_{t+1} = A_t x_t + B_t u_t + c_t$, but in many applications the time-invariant form $x_{t+1} = A x_t + B u_t$ is sufficient.

**Why discrete time and not continuous?** This is a modelling choice. Continuous-time linear systems $\dot x = A x$ are also well-studied, with similar structural theory (eigenvalues of $A$ control behaviour, but now $\operatorname{Re}(\lambda)$ rather than $|\lambda|$ matters). Boyd works in discrete time because: (i) most applied modelling proceeds in time steps (years for population, days for portfolios, milliseconds for engineering controllers); (ii) computer simulations are naturally discrete; (iii) continuous-time can be reduced to discrete by sampling and the Euler method, $x_{t+1} = x_t + h \dot x_t = (I + h A) x_t$ for small step size $h$. So discrete time is more practical without sacrificing generality.

**What goes wrong with nearby variants?** **Non-linear dynamics** $x_{t+1} = f(x_t)$ for general $f$: this is the general setting of dynamical systems, but loses the algebraic tractability — the long-time behaviour can be chaotic, with no clean characterisation. The linear case is special in that everything follows from the eigenvalues/eigenvectors of $A$. **Higher-order rules without state augmentation** ($K$-Markov with $K > 1$): these *can* be reduced to standard Markov via state augmentation, so they are not genuinely new, just a notational variant. **Time-varying dynamics matrix $A_t$**: this generalises the time-invariant case but loses much of the spectral theory; analysis is much harder, and most practical models stay in the time-invariant regime.

**Why is the state called the "state"?** Because it captures the *current state of the system* in the sense that knowing $x_t$ alone — not the past — suffices to predict $x_{t+1}, x_{t+2}, \dots$. This is the operational meaning of "state" in physics, computer science, and control theory: the minimal information needed to specify "where the system is" right now.

---

# The Definition

**Linear dynamical system.** A **linear dynamical system** in $\mathbb R^n$ is a sequence $x_1, x_2, x_3, \dots$ of $n$-vectors — the **state trajectory** — evolving according to the recurrence
$$
x_{t+1} = A_t x_t, \quad t = 1, 2, 3, \dots,
$$
where each $A_t \in \mathbb R^{n \times n}$ is the **dynamics matrix** at time $t$. The vector $x_t$ is the **state** at time $t$; it contains all the information needed to determine $x_{t+1}, x_{t+2}, \dots$.

**Time-invariant case.** When $A_t = A$ does not depend on $t$, the system is **time-invariant**:
$$x_{t+1} = A x_t,$$
and iterating gives $x_{t + \ell} = A^\ell x_t$ for any $\ell \geq 0$. This is also called a **Markov model** or **first-order autoregressive model** in different fields.

**Linear dynamical system with input.** A more general form includes external inputs $u_t \in \mathbb R^m$ and offsets $c_t \in \mathbb R^n$:
$$x_{t+1} = A_t x_t + B_t u_t + c_t,$$
with input matrix $B_t \in \mathbb R^{n \times m}$. The trajectory is determined by the initial state $x_1$ together with the input and offset sequences $u_1, u_2, \dots$ and $c_1, c_2, \dots$. For the time-invariant case, repeated substitution gives the explicit formula
$$
x_{t + \ell} = A^\ell x_t + \sum_{j = 0}^{\ell - 1} A^{\ell - 1 - j} B u_{t + j} + \sum_{j = 0}^{\ell - 1} A^{\ell - 1 - j} c_{t + j}.
$$
The first term is the **free response** (the response without inputs), and the second and third are the **forced response** (the response due to inputs and offsets).

**$K$-Markov model.** A $K$-th order linear recurrence is
$$
x_{t+1} = A_1 x_t + A_2 x_{t-1} + \cdots + A_K x_{t - K + 1}, \quad t \geq K.
$$
This is equivalent to a standard linear dynamical system in the augmented state $z_t = (x_t, x_{t-1}, \dots, x_{t-K+1}) \in \mathbb R^{nK}$, with dynamics matrix
$$
\tilde A = \begin{pmatrix} A_1 & A_2 & \cdots & A_K \\ I_n & 0 & \cdots & 0 \\ 0 & I_n & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & I_n \end{pmatrix} \in \mathbb R^{nK \times nK}.
$$
The first block-row implements the $K$-Markov recurrence; the lower block-rows simply shift the past states along.

**Equilibrium.** For the time-invariant system $x_{t+1} = A x_t + c$ (with constant offset), an **equilibrium point** is a vector $z$ with $z = A z + c$, equivalently $(I - A) z = c$. Starting from $x_1 = z$ keeps the state at $z$ for all $t$.

---

# Relate to Other Fields / Compression

A linear dynamical system is the **discrete-time linear time-invariant (LTI) system** of control theory and signal processing. The continuous-time analogue is the differential equation $\dot x = A x + B u$, with the same algebraic structure (matrix exponentials replace matrix powers).

A linear dynamical system without input is exactly a **Markov chain on a continuous state space with deterministic transitions** — equivalently, an iterated linear map, the most basic discrete dynamical system. Replacing $A$ by a stochastic matrix (columns nonneg, summing to $1$) gives a probabilistic Markov chain on a finite state space, and the iterations of $A$ describe the evolution of probability distributions.

In statistics, the autoregressive AR($K$) model is a $K$-Markov linear dynamical system, used for time series forecasting. In econometrics, vector autoregression (VAR) models extend this to vector-valued time series. The state-augmentation trick converts AR($K$) into AR($1$) in a higher-dimensional state space, which is the standard analytical move.

In numerical analysis, discretising a continuous-time ODE $\dot x = f(x)$ by the **Euler method** gives $x_{t+1} = x_t + h f(x_t)$; if $f$ is linear or has been linearised, this is a linear dynamical system. The conditions for stability of the Euler discretisation — eigenvalues of the discrete map inside the unit disk — translate to conditions on the step size $h$.

**True name:** A linear dynamical system is *iterated multiplication by a matrix*, plus possibly inputs and offsets. The long-time behaviour is *entirely controlled by the spectrum of $A$*: trajectories decay exponentially if all eigenvalues satisfy $|\lambda| < 1$, blow up if any $|\lambda| > 1$, and exhibit polynomial-growth subtleties on the boundary $|\lambda| = 1$.

---

# Examples / Corollaries

**Is an instance — Boyd's population dynamics.** The age-distribution vector $x_t \in \mathbb R^{100}$ (with $(x_t)_i$ the number of $(i-1)$-year-olds in year $t$) evolves by $x_{t+1} = A x_t$, with $A$ a sparse matrix: the first row contains the birth rates $b_i$, the sub-diagonal entries $1 - d_i$ encode aging plus survival, and all other entries are zero. Iterating $A$ projects the demographic profile forward in time.

**Is an instance — Boyd's epidemic dynamics.** The $4$-vector $x_t$ tracks the fractions of the population that are susceptible, infected, recovered, and deceased. With transition probabilities given (each susceptible has $5\%$ chance of becoming infected each day, each infected has $1\%$ chance of dying, $10\%$ chance of becoming immune, $4\%$ chance of returning to susceptible), the model is $x_{t+1} = A x_t$ for an explicit $4 \times 4$ matrix.

**Is an instance — mass-on-a-spring (Euler discretisation).** Newton's law $m\ddot x = F$ with viscous damping $-\eta \dot x$ and applied force $f$ becomes, after Euler discretisation with time step $h$, the linear dynamical system $\begin{pmatrix} x_{k+1} \\ v_{k+1} \end{pmatrix} = \begin{pmatrix} 1 & h \\ 0 & 1 - h \eta/m \end{pmatrix}\begin{pmatrix} x_k \\ v_k \end{pmatrix} + \begin{pmatrix} 0 \\ h/m \end{pmatrix} f_k$. The state is $(x, v)$ — position and velocity — and the input is the applied force.

**Is an instance — supply-chain dynamics.** With $n$ warehouses connected by $m$ transportation links, the deviation $x_t$ from target inventory levels updates by $x_{t+1} = x_t + A^{\text{sc}} f_t + p_t - s_t$, where $A^{\text{sc}}$ is the incidence matrix of the transportation network, $f_t$ is the vector of link flows, $p_t$ is purchases, $s_t$ is sales. This is a linear dynamical system with $A = I$ (the inventory persists) and inputs $(f_t, p_t)$ with offset $-s_t$.

**Is an instance — Fibonacci sequence as a $2$-Markov model.** The Fibonacci recurrence $y_{t+1} = y_t + y_{t-1}$ is a $2$-Markov model, reducible to a standard linear dynamical system in the state $z_t = (y_t, y_{t-1})$ with dynamics matrix $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$. The eigenvalues are the golden ratio $\phi \approx 1.618$ and its conjugate $1 - \phi \approx -0.618$, and the closed-form $y_t = (\phi^t - (1-\phi)^t)/\sqrt 5$ (Binet's formula) follows directly from the eigendecomposition.

**Is NOT an instance — chaotic dynamics.** The logistic map $x_{t+1} = r x_t (1 - x_t)$ is *not* a linear dynamical system (it is quadratic in the state). For $r = 4$ it exhibits chaos: trajectories are sensitive to initial conditions and never settle. Linear systems cannot be chaotic — their long-time behaviour is exponential decay, exponential growth, or oscillation, none of which is chaotic.

**Is NOT an instance — sequence without finite state.** A sequence $y_t = y_{t-1} + y_{t-2} + y_{t-3} + \cdots + y_1$ — the sum of all previous values — does *not* have a finite-dimensional Markov state, because the number of values needed to predict the next grows with $t$. However, this *can* be made into a linear dynamical system by introducing the auxiliary state $s_t = \sum_{i \leq t} y_i$ (the running sum), giving a $2$-dimensional state.

**Corollary — explicit trajectory in the time-invariant case.** For $x_{t+1} = A x_t$, $x_{t + \ell} = A^\ell x_t$, and the entire future is determined by $x_t$ and powers of $A$. The matrix power can be computed via diagonalisation when $A$ has $n$ linearly independent eigenvectors: $A = V \Lambda V^{-1}$ gives $A^\ell = V \Lambda^\ell V^{-1}$, reducing the matrix power to the much easier diagonal power.

**Corollary — equilibrium characterisation.** For $x_{t+1} = A x_t + c$, equilibria solve $(I - A) z = c$. The solution exists for all $c$ iff $I - A$ is invertible, iff $A$ has no eigenvalue equal to $1$. When $I - A$ is singular, equilibria exist only for special $c$ (in the range of $I - A$).

**Corollary — linearity of trajectories in initial state.** The map from $x_1$ to $x_T$ is linear: $x_T = A^{T-1} x_1$ for a closed system, or affine in the presence of inputs and offsets. This linearity is what makes superposition and sensitivity analysis tractable for linear dynamical systems and intractable for non-linear ones.

**Calibration check.** Verify that for $A = I$ (the identity), the state is constant: $x_{t+1} = x_t$, so $x_t = x_1$ for all $t$. Verify that for the cyclic permutation matrix $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}$ in $\mathbb R^3$, iterating cycles the entries of $x_t$ by $A^3 = I$, so the trajectory is periodic with period $3$. Verify that for $A = \begin{pmatrix} 0.5 & 0 \\ 0 & 0.5 \end{pmatrix}$, every trajectory decays to $0$ exponentially.

---

# Unlocked by This

> [!tip] Eigenvalues and Stability of Discrete Dynamical Systems *(from Linear Algebra V and Dynamical Systems)*
> The long-time behaviour of a linear dynamical system $x_{t+1} = A x_t$ is entirely controlled by the **eigenvalues** of $A$: trajectories decay to zero if all $|\lambda| < 1$, blow up if any $|\lambda| > 1$, and the boundary $|\lambda| = 1$ gives oscillatory or polynomially-growing behaviour. The full spectral story is in [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

> [!tip] Markov Chains and Stochastic Matrices *(from Probability)*
> When the dynamics matrix $A$ is a *stochastic matrix* (entries nonneg, columns sum to $1$), the linear dynamical system describes the evolution of a probability distribution over a finite state space — a **Markov chain**. The stationary distribution is an eigenvector of $A$ with eigenvalue $1$, and mixing time is controlled by the second-largest eigenvalue magnitude.

> [!tip] Control Theory and Linear Quadratic Regulator (LQR) *(from Optimization)*
> A linear dynamical system with input $u_t$ is the basic object of **linear control theory**. The **Linear Quadratic Regulator** problem — choose $u_t$ to minimise a quadratic cost subject to the dynamics — has an exact closed-form solution as a state-feedback law $u_t = K x_t$, where $K$ is computed from the **Riccati equation**. This is the foundation of optimal control and appears in [[Linear Algebra XI — Applied II — Least Squares|Boyd Ch 17]].
