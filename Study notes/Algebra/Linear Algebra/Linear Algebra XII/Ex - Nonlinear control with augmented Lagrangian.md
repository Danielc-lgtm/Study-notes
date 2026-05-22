---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Augmented Lagrangian Algorithm"
  - "Def - Constrained Nonlinear Least Squares"
  - "Def - Levenberg-Marquardt Algorithm"
  - "Thm - Augmented Lagrangian Recovers Lagrange Multipliers"
tags: [algebra, linear-algebra, applied, optimal-control]
---

# Problem Statement

Consider the discrete-time nonlinear dynamical system describing a car with position $p = (p_1, p_2)$, orientation angle $\theta$, speed $s$, and steering angle $\phi$:
$$x_{k+1} = f(x_k, u_k), \quad k = 1, \ldots, N-1,$$
where $x_k = (p_1(k), p_2(k), \theta(k)) \in \mathbb{R}^3$ is the state, $u_k = (s(k), \phi(k)) \in \mathbb{R}^2$ is the control input, and
$$f(x_k, u_k) = x_k + h (u_k)_1 \begin{pmatrix} \cos(x_k)_3 \\ \sin(x_k)_3 \\ \tan(u_k)_2 / L \end{pmatrix},$$
with $h$ the time step and $L$ the car's wheelbase.

The **nonlinear optimal control problem** is:
$$\min_{u_1, \ldots, u_N, \; x_2, \ldots, x_N} \sum_{k=1}^N \|u_k\|^2 + \gamma \sum_{k=1}^{N-1} \|u_{k+1} - u_k\|^2$$
subject to
$$x_2 = f(0, u_1), \quad x_{k+1} = f(x_k, u_k) \;\; (k = 2, \ldots, N-1), \quad x^\text{final} = f(x_N, u_N).$$

(The initial state is $x_1 = 0$; the final state $x^\text{final}$ is prescribed.)

**(a)** Identify the variable $\xi$, the residual map $r(\xi)$, the constraint map $c(\xi)$, and the dimensions of each, in the form of an equality-constrained nonlinear LS problem $\min \|r(\xi)\|^2$ s.t. $c(\xi) = 0$.

**(b)** Set up the augmented Lagrangian iteration. Specifically, write down the inner-loop nonlinear LS subproblem $\min \|h_{\mu, z}(\xi)\|^2$ that needs to be solved at each outer iteration, and the multiplier update rule.

**(c)** Explain in two paragraphs why the augmented Lagrangian — not the penalty algorithm — is the appropriate tool for this problem, especially for long horizons $N$.

**Recall:**

The problem is an equality-constrained nonlinear least squares problem.

![[Def - Constrained Nonlinear Least Squares#The Definition]]

![[Def - Augmented Lagrangian Algorithm#The Definition]]

The dynamics $x_{k+1} - f(x_k, u_k) = 0$ are *nonlinear* in the state $x_k$ and input $u_k$ (because of the $\cos, \sin, \tan$ in $f$), so they must be enforced as nonlinear equality constraints.

By [[Thm - Augmented Lagrangian Recovers Lagrange Multipliers]], each iterate produced by the augmented Lagrangian algorithm satisfies the KKT stationarity condition for the constrained problem; the algorithm needs only to drive the constraint $c = 0$ to satisfy feasibility.

---

# Convergent Strategy

**Problem class.** This is a **direct transcription** (or "direct multiple shooting") instance of nonlinear optimal control: the state and input trajectories are unrolled into a single vector of unknowns, the dynamics are enforced as equality constraints, and the boundary conditions are part of the constraint set. The recipe of [[Linear Algebra XII — Applied III — Nonlinear Least Squares#Problem-Solving Strategy|the topic page's strategy]] applies directly: equality constraints, nonlinear, use augmented Lagrangian wrapped around Levenberg–Marquardt.

**Assumption pattern.** Three signals identify the recognizable instance. (i) The objective is a *sum of squares* of inputs and input-differences — a smoothness penalty on the control trajectory. (ii) The constraints are *nonlinear equalities* — the dynamics. (iii) The initial and final states are prescribed; everything in between is free. This is the canonical form of **finite-horizon optimal control** for nonlinear systems, and direct transcription is the standard discretization.

**Theorem routing.** The route splits into three parts. *Setup* (part a): collect the unknowns $(u_1, \ldots, u_N, x_2, \ldots, x_N)$ into a single vector $\xi$, the objective $\sum \|u\|^2 + \gamma \sum \|u_{k+1} - u_k\|^2$ as $\|r(\xi)\|^2$ for a residual map $r$ built from $u$'s and $u$-differences, the constraints $x_{k+1} - f(x_k, u_k) = 0$ as a single constraint map $c(\xi)$. *Inner solve* (part b): apply LM to the augmented Lagrangian subproblem $\min \|r(\xi)\|^2 + \mu \|c(\xi) + z/(2\mu)\|^2$ at the current $(z, \mu)$. *Outer update* (part b): set $z \leftarrow z + 2\mu c(\xi)$, grow $\mu$ if constraint progress is slow.

**Key decision point.** The non-obvious decision is *how to organize the variable $\xi$*. The natural choices are: (i) put all states first, then all inputs ($\xi = (x_2, \ldots, x_N, u_1, \ldots, u_N)$), (ii) interleave by time step ($\xi = (u_1, x_2, u_2, x_3, \ldots, u_N, x_N)$), (iii) eliminate the states by "shooting" — express each $x_{k+1}$ recursively from $x_1, u_1, \ldots, u_k$ and treat only $u$'s as unknowns. The right choice for *direct transcription* is the time-step-interleaved variant (ii), because the constraint Jacobian $Dc$ then has a *band-diagonal* structure (each constraint $c_k = x_{k+1} - f(x_k, u_k)$ involves only adjacent time steps), and the inner LM linear-LS solves can exploit this sparsity for $O(N)$ rather than $O(N^3)$ cost per iteration. Choice (iii), "single shooting," eliminates the constraints but produces a heavily nonlinear unconstrained problem that is poorly conditioned for long $N$ — the chain of compositions $f \circ f \circ \cdots$ amplifies small errors exponentially. Direct transcription's larger but *better-conditioned* problem wins for moderate to long $N$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra XII — Applied III — Nonlinear Least Squares#Legal Operations|the topic page's Legal Operations]]:

1. **Convert an equality constraint into a quadratic penalty** (operation 7), in the augmented form. The constraint $c(\xi) = 0$ is converted into the penalty term $\mu \|c(\xi) + z/(2\mu)\|^2$ inside the augmented Lagrangian.

2. **Estimate a Lagrange multiplier by the augmented Lagrangian update** (operation 8). After each inner LM solve, update $z^{(k+1)} = z^{(k)} + 2\mu^{(k)} c(\xi^{(k+1)})$ to track the multiplier.

3. **Group state and control variables together as a single block** (operation 9). The unknowns are concatenated into a single vector $\xi$ that LM treats as a generic vector of optimization variables.

4. **Linearize the residual at the current iterate** (operation 1). Each inner LM subproblem linearizes both $r$ and $c$ at the current iterate to produce a linear LS problem.

5. **Regularize the step by adding a trust-region penalty** (operation 2). The inner LM uses the trust-region $\lambda^{(k)} \|\xi - \xi^{(k)}\|^2$ to keep steps bounded.

---

# Hints

> [!note]- Hint 1
> Collect the unknowns: $\xi = (u_1, \ldots, u_N, x_2, \ldots, x_N) \in \mathbb{R}^{2N + 3(N-1)}$. For Boyd's setup with $N = 50$, this is a vector of about $250$ unknowns.

> [!note]- Hint 2
> The residual map for the *objective* has two blocks: $r^u_k = u_k$ for $k = 1, \ldots, N$ (with squared norm $\sum \|u_k\|^2$) and $r^\Delta_k = \sqrt\gamma (u_{k+1} - u_k)$ for $k = 1, \ldots, N-1$ (with squared norm $\gamma \sum \|u_{k+1} - u_k\|^2$). Total residual dimension: $2N + 2(N-1)$.

> [!note]- Hint 3
> The constraint map $c$ has one block per dynamics step: $c_k(\xi) = x_{k+1} - f(x_k, u_k)$ for $k = 1, \ldots, N$, with $x_1 = 0$ given and $x_{N+1} = x^\text{final}$ also given. Total constraint dimension: $3N$ (one constraint per time step in $\mathbb{R}^3$).

> [!note]- Hint 4
> The inner-loop augmented Lagrangian subproblem is to minimize over $\xi$:
> $$\|r(\xi)\|^2 + \mu^{(k)} \|c(\xi) + z^{(k)}/(2\mu^{(k)})\|^2.$$
> This is itself a nonlinear LS problem (in $\xi$), solved by LM. Note the residual and constraint maps are stacked: the LM iteration sees the combined map $h_{\mu, z}(\xi) = (r(\xi), \sqrt\mu (c(\xi) + z/(2\mu)))$.

> [!note]- Hint 5
> The Jacobian $Dc$ is band-diagonal because $c_k$ involves only $x_k$, $u_k$, $x_{k+1}$. Each block row of $Dc$ is sparse: it has nonzeros only for the three blocks of variables $(u_k, x_k, x_{k+1})$. Sparse linear algebra solves the inner LM system in $O(N)$ rather than $O(N^3)$ flops, making long horizons feasible.

---

# Solution

The plan is to organize the variables and constraints, formulate the augmented Lagrangian subproblem and update, and discuss why augmented Lagrangian beats penalty for long horizons.

**Step 1: Variable, residual, and constraint maps.**

Unknowns: $\xi = (u_1, \ldots, u_N, x_2, \ldots, x_N)$, with $u_k \in \mathbb{R}^2$ and $x_k \in \mathbb{R}^3$. So $\xi \in \mathbb{R}^{2N + 3(N-1)}$.

Residual map for the *objective*:
- Input-size residuals: $r^u_k(\xi) = u_k$ for $k = 1, \ldots, N$.
- Input-difference residuals: $r^\Delta_k(\xi) = \sqrt\gamma (u_{k+1} - u_k)$ for $k = 1, \ldots, N-1$.
- Combined $r(\xi)$ has dimension $2N + 2(N-1) = 4N - 2$.

Constraint map: $c_k(\xi) = x_{k+1} - f(x_k, u_k)$ for $k = 1, \ldots, N$, with $x_1 = 0$ and $x_{N+1} = x^\text{final}$ given. So $c(\xi)$ has dimension $3N$.

> [!note]- Derivation
> Boyd's problem statement (Equation 19.12 of §19.4) groups the unknowns as the inputs $u_1, \ldots, u_N$ and the intermediate states $x_2, \ldots, x_N$. The initial state $x_1 = 0$ and the final state $x^\text{final}$ are given, not optimized over.
>
> The objective is $\sum_{k=1}^N \|u_k\|^2 + \gamma \sum_{k=1}^{N-1} \|u_{k+1} - u_k\|^2$. To match the form $\|r(\xi)\|^2$, we identify each $\|u_k\|^2$ with the squared norm of a 2-vector residual $r^u_k = u_k$ and each $\gamma \|u_{k+1} - u_k\|^2$ with the squared norm of $r^\Delta_k = \sqrt\gamma (u_{k+1} - u_k)$. Stacking gives the full residual map $r : \mathbb{R}^{2N + 3(N-1)} \to \mathbb{R}^{4N - 2}$.
>
> The constraints are: $x_2 = f(0, u_1)$ (initial), $x_{k+1} = f(x_k, u_k)$ for $k = 2, \ldots, N-1$ (intermediate), and $x^\text{final} = f(x_N, u_N)$ (terminal). Rewriting as $c_k(\xi) = 0$:
> - $c_1(\xi) = x_2 - f(0, u_1)$,
> - $c_k(\xi) = x_{k+1} - f(x_k, u_k)$ for $k = 2, \ldots, N-1$,
> - $c_N(\xi) = x^\text{final} - f(x_N, u_N)$.
>
> Each $c_k$ is a vector in $\mathbb{R}^3$, so the total constraint map $c : \mathbb{R}^{2N + 3(N-1)} \to \mathbb{R}^{3N}$.
>
> For $N = 50$: $\xi$ has $\sim 250$ dimensions, $r$ has $\sim 200$, $c$ has $150$. The combined $h$ map has $\sim 350$ components.

**Step 2: Augmented Lagrangian iteration.**

The inner-loop nonlinear LS subproblem at outer iteration $k$ is
$$\min_\xi \quad \|r(\xi)\|^2 + \mu^{(k)} \big\|c(\xi) + z^{(k)}/(2\mu^{(k)})\big\|^2,$$
solved by Levenberg–Marquardt applied to the stacked residual
$$h_{\mu^{(k)}, z^{(k)}}(\xi) = \begin{pmatrix} r(\xi) \\ \sqrt{\mu^{(k)}}\, c(\xi) + z^{(k)}/(2\sqrt{\mu^{(k)}}) \end{pmatrix}.$$
(Algebraically equivalent to $\sqrt{\mu^{(k)}}(c(\xi) + z^{(k)}/(2\mu^{(k)}))$ as the second block.)

The outer-loop updates are:
- Multiplier: $z^{(k+1)} = z^{(k)} + 2 \mu^{(k)} c(\xi^{(k+1)})$.
- Penalty: $\mu^{(k+1)} = \mu^{(k)}$ if $\|c(\xi^{(k+1)})\| < 0.25 \|c(\xi^{(k)})\|$, else $2 \mu^{(k)}$.

Initialize: $\xi^{(1)}$ arbitrary (Boyd uses random $u$'s and $x = 0$), $z^{(1)} = 0$, $\mu^{(1)} = 1$.

> [!note]- Derivation
> The augmented Lagrangian is
> $$L_\mu(\xi, z) = \|r(\xi)\|^2 + c(\xi)^T z + \mu \|c(\xi)\|^2.$$
> Using the [[Def - Augmented Lagrangian Algorithm#The Definition|key identity]],
> $$L_\mu(\xi, z) = \|r(\xi)\|^2 + \mu \|c(\xi) + z/(2\mu)\|^2 - \mu \|z/(2\mu)\|^2,$$
> where the last term is constant in $\xi$. Minimizing $L_\mu$ over $\xi$ at fixed $(z, \mu)$ is therefore equivalent to minimizing the first two terms, which is the inner-loop nonlinear LS problem above.
>
> The stacked form $h_{\mu, z}(\xi) = (r(\xi), \sqrt\mu (c(\xi) + z/(2\mu)))$ has squared norm $\|h\|^2 = \|r\|^2 + \mu \|c + z/(2\mu)\|^2$, matching the inner subproblem. LM applied to $h$ minimizes this.
>
> The Jacobian $Dh$ has the corresponding block structure:
> $$Dh(\xi) = \begin{pmatrix} Dr(\xi) \\ \sqrt\mu \, Dc(\xi) \end{pmatrix}.$$
> The constraint Jacobian $Dc$ is band-diagonal (each $c_k$ involves only $x_k, u_k, x_{k+1}$), which is exploited by sparse LM implementations.
>
> The multiplier update $z^{(k+1)} = z^{(k)} + 2\mu^{(k)} c(\xi^{(k+1)})$ is the standard augmented Lagrangian rule, equivalent to dual gradient ascent on the Lagrangian dual.
>
> The penalty update keeps $\mu$ moderate when the constraint is shrinking fast (no need to grow $\mu$) and doubles $\mu$ when progress is slow (constraint not shrinking fast enough).

**Step 3: Why augmented Lagrangian, not penalty.**

For long horizons (large $N$), the augmented Lagrangian is dramatically preferable to the penalty algorithm for two reasons.

> [!note]- Derivation
> **Reason 1: Conditioning.** The penalty algorithm requires $\mu \to \infty$ to enforce the dynamics constraints. The condition number of the inner LM subproblem scales linearly in $\mu$, so by the time $\mu = 10^{12}$ (the value needed to enforce dynamics to $10^{-6}$ tolerance, by [[Thm - Convergence of Penalty Algorithm]] $\|c\| = O(1/\mu)$), the inner subproblem has condition number $\sim 10^{12}$ — at the edge of what double precision can handle reliably. For long $N$ ($N = 50$ or $N = 200$), the constraint Jacobian $Dc$ itself has condition number that grows with $N$ (because the dynamics map composed many times amplifies errors), so the *effective* condition number of the penalty inner solve at large $\mu$ exceeds machine epsilon. The algorithm stalls. The augmented Lagrangian keeps $\mu$ moderate (typically $O(10)$), so the inner subproblem stays well-conditioned even for long horizons.
>
> **Reason 2: Iteration count.** The penalty algorithm's outer-loop convergence is $\|c\| = O(1/\mu^{(k)}) = O(1/2^k)$ (since $\mu$ doubles each outer iteration). To achieve $\|c\| = 10^{-8}$, you need $k \sim 27$ outer iterations. The augmented Lagrangian's convergence on $\|c\|$ is *linear* with rate determined by the constraint curvature and $\mu$, and in practice $\|c\|$ shrinks by a factor of $4$–$10$ per outer iteration — so $k \sim 5$–$10$ outer iterations achieve $\|c\| = 10^{-8}$. Combined with the better conditioning, augmented Lagrangian achieves a target tolerance with $\sim 5\times$ fewer total LM iterations than the penalty algorithm.
>
> For Boyd's $N = 50$ car-steering problem, the augmented Lagrangian completes in $\sim 6$ outer iterations and $\sim 140$ total LM iterations; the penalty algorithm requires $\sim 12$ outer iterations and $\sim 150$ total LM iterations *but* with much larger residuals at termination (constraint violation $\sim 10^{-3}$ vs $\sim 10^{-7}$ for augmented Lagrangian; see Boyd Figure 19.4). The augmented Lagrangian is the clear winner.

> [!note]- Complete formal solution
> **(a) Setup.** $\xi = (u_1, \ldots, u_N, x_2, \ldots, x_N) \in \mathbb{R}^{2N + 3(N-1)}$. The residual map $r$ has blocks $r^u_k = u_k$ (size $2$, $k = 1, \ldots, N$) and $r^\Delta_k = \sqrt\gamma(u_{k+1} - u_k)$ (size $2$, $k = 1, \ldots, N-1$), total dimension $4N - 2$. The constraint map $c$ has blocks $c_k = x_{k+1} - f(x_k, u_k)$ (size $3$, $k = 1, \ldots, N$, with $x_1 = 0$ and $x_{N+1} = x^\text{final}$), total dimension $3N$.
>
> **(b) Augmented Lagrangian iteration.** Initialize $\xi^{(1)}$, $z^{(1)} = 0$, $\mu^{(1)} = 1$. At each outer iteration $k$, minimize $\|r(\xi)\|^2 + \mu^{(k)} \|c(\xi) + z^{(k)}/(2\mu^{(k)})\|^2$ over $\xi$ using Levenberg–Marquardt (starting from $\xi^{(k)}$) to obtain $\xi^{(k+1)}$. Then update $z^{(k+1)} = z^{(k)} + 2\mu^{(k)} c(\xi^{(k+1)})$ and $\mu^{(k+1)} = \mu^{(k)}$ if $\|c(\xi^{(k+1)})\| < 0.25 \|c(\xi^{(k)})\|$, else $\mu^{(k+1)} = 2\mu^{(k)}$. Stop when $\|c(\xi^{(k)})\|$ is below tolerance.
>
> **(c) Why augmented Lagrangian.** For long $N$, the penalty algorithm's required $\mu \to \infty$ makes the inner LM subproblem catastrophically ill-conditioned (condition number $\sim \mu \cdot \kappa(Dc)$, both growing with $N$). The augmented Lagrangian keeps $\mu$ moderate by tracking the multiplier $z$ explicitly, achieving constraint enforcement to $10^{-7}$ tolerance with $\mu = O(10)$ — well within double-precision conditioning. Additionally, the augmented Lagrangian's outer-loop convergence is linear in iteration count, requiring $\sim 5$–$10$ outer iterations vs $\sim 30$ for penalty, for the same tolerance. The combined effect is a $\sim 5\times$ reduction in total LM iterations *and* substantially tighter constraint satisfaction. $\blacksquare$

> [!warning] Illegal but tempting alternative — single shooting
> An alternative is **single shooting**: eliminate the states by composition. Express $x_2 = f(0, u_1)$, $x_3 = f(x_2, u_2) = f(f(0, u_1), u_2)$, etc., and treat the problem as an unconstrained minimization in $(u_1, \ldots, u_N)$ alone, with the terminal constraint $x^\text{final} = f(x_N, u_N)$ as a single equality. This has *fewer unknowns* ($2N$ instead of $5N$) and *no intermediate constraints*. Why not do it?
>
> Because the composition $f^N$ is exponentially sensitive to early $u$'s for nonlinear dynamics. The Jacobian of $x_N$ with respect to $u_1$ involves the product of all intermediate Jacobians $\prod_{k=1}^{N-1} \partial f/\partial x \cdot \partial f/\partial u$, which has eigenvalues growing or shrinking exponentially in $N$ (the Lyapunov spectrum). For chaotic or stiff systems, this Jacobian becomes numerically degenerate by $N \sim 10$.
>
> Direct transcription's *larger but better-conditioned* problem wins for nontrivial $N$. The band-diagonal $Dc$ replaces the exponentially-amplified composition product with a sequence of well-scaled local Jacobians, and sparse linear algebra exploits the structure. This is why **all modern optimal-control codes** (CasADi, GPOPS-II, ACADO, IPOPT-based pipelines) use direct transcription with augmented Lagrangian or interior-point solvers, not single shooting.

---

# Key Takeaways

**Direct transcription converts trajectory optimization into a structured nonlinear LS problem.** This exercise drills the master pattern of modern numerical optimal control: don't try to be clever by eliminating states (single shooting) or by using continuous-time machinery (indirect methods via Pontryagin); just discretize, write everything as unknowns, write the dynamics as equality constraints, and let the augmented Lagrangian solve the resulting structured problem. The "magic" is that the constraint Jacobian is band-diagonal — sparsity emerges naturally from the time-stepping structure of dynamics. Sparse linear algebra inside LM then makes the inner solve $O(N)$ in iteration cost, so trajectories of length $N = 1000$ are solvable on a laptop in seconds. The trigger to reach for this machinery is straightforward: any time you have a nonlinear dynamical system, boundary conditions, and a cost on the trajectory — pose it as constrained NLS via direct transcription. The legal operation 9 "group state and control variables together as a single block" is the technical maneuver; the algorithmic infrastructure does the rest.

**Augmented Lagrangian's superiority over penalty is most dramatic for long-horizon problems.** The conditioning argument generalizes: any time the constraint structure has its own intrinsic condition number that grows with problem size — long-horizon dynamics, fine-grid PDE constraints, network-flow problems with many nodes — multiplying by a large $\mu$ pushes the inner subproblem into numerical breakdown. The penalty algorithm cannot escape this; the augmented Lagrangian can, by transferring the constraint-enforcement work from $\mu$ to the explicit multiplier. The general principle: *whenever the constraint magnitude has its own intrinsic conditioning issue, you need the multiplier separately to avoid coupling it to the penalty scale.* This is why the augmented Lagrangian, not the penalty algorithm, is the foundation of every production nonlinear-programming code.

**Sparse linear algebra is what makes large-scale nonlinear optimization feasible.** This exercise's $N = 50$ problem has ~250 unknowns and ~150 constraints, with a constraint Jacobian containing only $\sim 5 \cdot 150 = 750$ nonzeros out of $250 \cdot 150 = 37500$ entries (about 2% density). For $N = 1000$, the unknowns are 5000 and the nonzeros are $\sim 15000$ — still about 2% density. Naive (dense) linear solves cost $O(N^3)$ in this regime; sparse solves cost $O(N)$ (because the band structure means each band-elimination step is $O(\text{bandwidth})$ regardless of $N$). The factor of $N^2$ saving is what turns a 1-day trajectory optimization into a 1-second one. The takeaway for any large-scale nonlinear LS: identify the sparsity structure of $Dr$ and $Dc$, use a linear solver that exploits it (sparse Cholesky, sparse QR, conjugate gradient with preconditioner), and the inner-loop cost scales with the number of nonzeros, not the number of variables. Off-the-shelf libraries (Ceres Solver, Ipopt, CasADi) implement this; the user supplies the sparse Jacobian via callback.
