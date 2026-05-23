---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Penalty Algorithm"
  - "Def - Constrained Nonlinear Least Squares"
tags: [algebra, linear-algebra, applied, optimization, convergence]
---

# Notation

Let $f : \mathbb{R}^n \to \mathbb{R}^m$ and $g : \mathbb{R}^n \to \mathbb{R}^p$ be continuously differentiable. The constrained problem is $\min \|f(x)\|^2$ s.t. $g(x) = 0$. The **penalty algorithm** iterates are $x^{(k+1)} \in \arg\min \|f(x)\|^2 + \mu^{(k)} \|g(x)\|^2$ with $\mu^{(k)} \to \infty$. The full registry is on [[Linear Algebra XII — Applied III — Nonlinear Least Squares]].

---

# Statement

> **Theorem (Convergence of the penalty algorithm).** Let $\hat x$ be an isolated solution of $\min \|f(x)\|^2$ s.t. $g(x) = 0$ with Lagrange multiplier $\hat z$, and assume:
> 1. $f, g$ are $C^1$ near $\hat x$;
> 2. $Dg(\hat x)$ has full row rank (LICQ holds);
> 3. The second-order sufficient conditions for $\hat x$ to be an isolated minimum hold.
>
> Let $\mu^{(k)} \to \infty$ and assume that each penalty subproblem $\min \|f(x)\|^2 + \mu^{(k)} \|g(x)\|^2$ has a global minimizer $x^{(k+1)}$ near $\hat x$. Then as $k \to \infty$,
> $$x^{(k+1)} \to \hat x, \qquad 2\, \mu^{(k)}\, g(x^{(k+1)}) \to \hat z, \qquad \|g(x^{(k+1)})\| \to 0.$$
>
> Furthermore, the **rate of convergence** of $\|g(x^{(k+1)})\|$ is $O(1/\mu^{(k)})$, and the corresponding rate of $x^{(k+1)} \to \hat x$ is $O(1/\mu^{(k)})$ in directions transverse to the constraint surface.

---

# Motivation

The penalty algorithm converts the constrained problem into a sequence of unconstrained subproblems with weights $\mu^{(k)} \to \infty$. The theorem says this conversion *works*: the iterates converge to the constrained optimum, and the implicit multiplier $2 \mu^{(k)} g(x^{(k+1)})$ converges to the true Lagrange multiplier $\hat z$. So the penalty algorithm is theoretically correct.

The reason this is not obviously true is that as $\mu \to \infty$, the penalty subproblem becomes increasingly singular: the Hessian of the penalty objective acquires large eigenvalues in the constraint-normal directions while remaining bounded in constraint-tangent directions, producing an anisotropic landscape with condition number growing as $\mu$. The theorem says that despite this singular limit, the *minimizer* of the subproblem behaves well and approaches the constrained minimum at a quantifiable rate.

The convergence rate $O(1/\mu^{(k)})$ is the precise statement of the algorithm's *practical flaw*: to achieve $\|g\| < \varepsilon$, you need $\mu \sim 1/\varepsilon$. For tight tolerances $\varepsilon \sim 10^{-8}$, this is $\mu \sim 10^8$, well into the ill-conditioned regime. So while the algorithm *converges* to any desired tolerance, the inner subproblems become *unsolvable* at the values of $\mu$ required — which is exactly the practical motivation for the augmented Lagrangian replacement.

---

# Sources and Targets

**Sources (Input Broadening).**

The first disguised source is **any constrained NLS problem where you have an unconstrained NLS solver available but no constrained solver**. The penalty algorithm requires only Levenberg–Marquardt and the ability to evaluate $g$; no Lagrange-multiplier infrastructure is needed. The non-obvious step is recognizing that this minimal toolkit suffices for a (theoretically) convergent constrained algorithm. *Example problem:* Implement a constrained-NLS solver from scratch with only an LM library and the ability to evaluate $g$ — use the penalty algorithm, verify with this theorem.

The second disguised source is **a regularization sweep on a constrained problem**. Sometimes you want to solve the constrained problem for a range of regularization weights $\lambda$, with the constraint $g(x) = 0$ enforced for each. Re-running the constrained solve at each $\lambda$ is expensive; instead, formulate as $\min \|f(x; \lambda)\|^2 + \mu \|g(x)\|^2$ and sweep both $\lambda$ and $\mu$ jointly. This theorem says that for any fixed $\lambda$, as $\mu \to \infty$ the constraint is enforced. *Example problem:* Solve a regularized Tikhonov problem with hard constraints by combining the penalty algorithm with the regularization sweep.

The third disguised source is **constrained least-squares model fitting with linearity assumptions failing**. If your problem is a small perturbation of a linear constrained LS problem (e.g., a near-linear model with mild nonlinearities), the penalty algorithm started at the linear solution converges rapidly: the penalty $\mu \|g\|^2$ provides a "homotopy" from the linear approximation toward the true constrained nonlinear solution. *Example problem:* A near-linear regression with $\|\theta\| = 1$ constraint, solved by penalty starting from the linear-LS solution projected onto the constraint sphere.

**Targets (Output Amplification).**

Combine the conclusion with **the implicit multiplier estimate**. The theorem identifies $2\mu^{(k)} g(x^{(k+1)})$ as the implicit Lagrange multiplier estimate, and this quantity converges to $\hat z$. So even though the penalty algorithm does not maintain $z$ explicitly, the user can read off the Lagrange multiplier as a byproduct of the iteration. The non-obviousness: many engineering applications care about the multiplier (it has interpretation as a "shadow price" in economics, a "constraint force" in mechanics, a "reaction force" in robotics) and the penalty algorithm produces it for free if you know where to look.

Combine the conclusion with **the conditioning bound**. The convergence rate $\|g\| = O(1/\mu)$ combined with the condition-number scaling $\kappa(Dh^T Dh) = O(\mu)$ tells you the *combined* error budget: at $\mu \sim 10^k$, you have $\|g\| \sim 10^{-k}$ but the inner solve has accuracy $\sim 10^{-(16-k)}$ in double precision. The product is $\sim 10^{-16}$, so the *practical* achievable constraint tolerance in double precision is $\sim 10^{-8}$. The non-obvious combination: you can predict the floor on achievable constraint accuracy from the conditioning analysis alone.

Combine the conclusion with **the augmented Lagrangian's superiority**. The theorem's $O(1/\mu)$ rate is the *baseline* against which the augmented Lagrangian is measured. The augmented Lagrangian achieves *linear* convergence of $\|g\|$ to zero with $\mu$ kept moderate — exponentially faster than the penalty algorithm's $O(1/\mu)$ at the cost of an additional multiplier update. The non-obvious takeaway: the theorem says the penalty algorithm is the *worst possible* convergent algorithm for constrained NLS, useful pedagogically but not practically.

---

# Why Is It True

**The mechanism in one sentence: the penalty objective's first-order optimality condition is exactly the constrained KKT stationarity with the implicit multiplier $z = 2\mu g(x)$, and the feasibility condition $g(x) = 0$ is forced in the limit by the requirement that the implicit multiplier remain bounded.**

At the inner-loop minimum $x^{(k+1)}$, the gradient of the penalized objective is zero:
$$0 = \nabla_x \big( \|f(x^{(k+1)})\|^2 + \mu^{(k)} \|g(x^{(k+1)})\|^2 \big) = 2 Df(x^{(k+1)})^T f(x^{(k+1)}) + 2 \mu^{(k)} Dg(x^{(k+1)})^T g(x^{(k+1)}).$$
Defining $z^{(k+1)} := 2 \mu^{(k)} g(x^{(k+1)})$, this rewrites as
$$2 Df(x^{(k+1)})^T f(x^{(k+1)}) + Dg(x^{(k+1)})^T z^{(k+1)} = 0,$$
which is *exactly* the constrained KKT stationarity at $(x^{(k+1)}, z^{(k+1)})$.

So every inner-loop minimum satisfies the KKT stationarity *exactly* with the implicit multiplier $z^{(k+1)}$. The only thing missing is feasibility $g(x^{(k+1)}) = 0$, and this is what the outer loop drives. As $\mu^{(k)} \to \infty$, for the multiplier $z^{(k+1)} = 2\mu^{(k)} g(x^{(k+1)})$ to *not* blow up, $g(x^{(k+1)})$ must shrink at rate $1/\mu^{(k)}$. This is the mechanism of feasibility: not because the algorithm "tries to satisfy the constraint," but because the implicit-multiplier rate $2\mu g$ cannot remain bounded otherwise, and that boundedness is what every other algorithmic guarantee depends on.

The contrast with augmented Lagrangian: there, $z$ is updated explicitly to converge to $\hat z$, so the multiplier role is decoupled from $\mu$. The penalty algorithm couples them, hence the conditioning problem.

---

# What Makes This Hard

The proof has three subtleties. **First**, the assertion that the inner subproblem has a minimizer near $\hat x$ for each $\mu^{(k)}$ requires the second-order sufficient conditions at $\hat x$ — without them, the penalized problem might have minimizers far from $\hat x$ at finite $\mu$. **Second**, identifying the limit of $2\mu^{(k)} g(x^{(k+1)})$ as $\hat z$ requires the LICQ (full row rank of $Dg(\hat x)$) — without LICQ the multiplier is not even uniquely defined, and the limit could fail to exist. **Third**, the rate $\|g\| = O(1/\mu)$ requires a careful Taylor expansion at the constrained optimum and is not automatic from the convergence statement; it depends on the curvature of the constraint surface and the magnitude of the residual at $\hat x$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show (i) the inner subproblem's optimality condition is exactly KKT stationarity with the implicit multiplier $2\mu g$; (ii) along the iterates, the implicit multiplier remains bounded by the LICQ; (iii) boundedness of the implicit multiplier forces $\|g\| \to 0$ at rate $1/\mu$; (iv) limits exist and satisfy the constrained KKT.

**Subgoal decomposition:**

1. **Inner KKT identification.** The gradient of $\|f\|^2 + \mu \|g\|^2$ at $x^{(k+1)}$ is zero, which rearranges to the constrained KKT stationarity at $(x^{(k+1)}, z^{(k+1)})$ with $z^{(k+1)} = 2\mu^{(k)} g(x^{(k+1)})$.
   - *Hint:* Expand the gradient by the chain rule on the squared norms.
   - *Why needed:* This is the algebraic fact that makes the penalty algorithm an instance of "approximate constrained optimization."

2. **Boundedness of $\{z^{(k)}\}$.** The sequence $z^{(k+1)} = 2\mu^{(k)} g(x^{(k+1)})$ is bounded.
   - *Hint:* Use the LICQ at $\hat x$ to invert (the relevant part of) $Dg^T$ and bound $z$ in terms of the bounded $Df^T f$ via the KKT stationarity.
   - *Why needed:* Without boundedness, the implicit multiplier could escape to infinity and the rate-$1/\mu$ feasibility would fail.

3. **Feasibility rate.** $\|g(x^{(k+1)})\| = O(1/\mu^{(k)})$ follows directly from $z^{(k+1)} = 2\mu^{(k)} g$ and the bound on $z^{(k+1)}$.
   - *Hint:* Just rearrange: $\|g\| = \|z\|/(2\mu)$.
   - *Why needed:* Quantifies the rate at which the constraint is approached.

4. **Limit point is feasible and KKT-stationary.** Any limit point $\hat x$ of $\{x^{(k+1)}\}$ satisfies $g(\hat x) = 0$ (from feasibility rate) and the KKT stationarity (passing to limits in the KKT identification with $z^{(k+1)} \to \hat z$).
   - *Hint:* Continuity of $f, g, Df, Dg$ and boundedness of $\{z^{(k)}\}$ allow extraction of a convergent subsequence.
   - *Why needed:* Identifies the limit as a constrained optimum.

5. **Uniqueness from isolated minimum hypothesis.** If $\hat x$ is the unique solution in a neighborhood (second-order sufficient condition), then the entire sequence converges to $\hat x$, not just a subsequence.
   - *Hint:* Argue by contradiction: if not, there would be a different limit point also satisfying constrained KKT, contradicting isolation.
   - *Why needed:* Strengthens "limit point" to "limit."

---

# Lemma Decomposition

> [!note]- Lemma 1: Inner KKT identification
> **Statement:** At the inner-loop minimum $x^{(k+1)}$ of $\|f(x)\|^2 + \mu^{(k)} \|g(x)\|^2$, defining $z^{(k+1)} := 2 \mu^{(k)} g(x^{(k+1)})$,
> $$2 Df(x^{(k+1)})^T f(x^{(k+1)}) + Dg(x^{(k+1)})^T z^{(k+1)} = 0.$$
>
> **Hint:** Compute the gradient of the penalty objective using the chain rule on $\|f\|^2 = f^T f$ and $\|g\|^2 = g^T g$.
>
> **Why needed:** This is the structural fact that the penalty algorithm's inner minimum is *already* a stationary point of the constrained problem, with the implicit multiplier $z^{(k+1)}$.
>
> > [!note]- Full proof
> > The objective is $\phi_\mu(x) = f(x)^T f(x) + \mu g(x)^T g(x)$. Its gradient is
> > $$\nabla \phi_\mu(x) = 2 Df(x)^T f(x) + 2 \mu Dg(x)^T g(x).$$
> > At an interior minimum $x^{(k+1)}$, $\nabla \phi_{\mu^{(k)}}(x^{(k+1)}) = 0$. Substituting $z^{(k+1)} = 2 \mu^{(k)} g(x^{(k+1)})$ gives
> > $$2 Df(x^{(k+1)})^T f(x^{(k+1)}) + Dg(x^{(k+1)})^T z^{(k+1)} = 0,$$
> > the constrained KKT stationarity at $(x^{(k+1)}, z^{(k+1)})$.

> [!note]- Lemma 2: Boundedness of the multiplier sequence
> **Statement:** Under the hypotheses of the theorem, the sequence $z^{(k+1)} = 2\mu^{(k)} g(x^{(k+1)})$ is bounded.
>
> **Hint:** From the KKT stationarity, $Dg^T z = -2 Df^T f$, so $z$ is determined (modulo nullspace of $Dg^T$) by the bounded right-hand side; LICQ ensures $Dg^T$ has trivial nullspace on the relevant [[Def - Subspace|subspace]].
>
> **Why needed:** Boundedness allows extraction of a convergent subsequence in the next lemma, and gives the $O(1/\mu)$ feasibility rate as a corollary.
>
> > [!note]- Full proof
> > By LICQ, $Dg(\hat x)$ has rank $p$, so $Dg(\hat x)^T : \mathbb{R}^p \to \mathbb{R}^n$ is injective. By continuity, $Dg(x)^T$ is injective for $x$ in some neighborhood $U$ of $\hat x$, with a uniform lower bound on its smallest singular value: $\|Dg(x)^T z\| \geq c \|z\|$ for some $c > 0$ and all $x \in U$, $z \in \mathbb{R}^p$.
> >
> > Assume $x^{(k+1)} \in U$ for all large enough $k$ (this is a consequence of the algorithm being well-defined and the inner subproblems having minimizers near $\hat x$; formally, this is part of the second-order sufficient condition hypothesis). Then from Lemma 1,
> > $$\|Dg(x^{(k+1)})^T z^{(k+1)}\| = 2 \|Df(x^{(k+1)})^T f(x^{(k+1)})\|.$$
> > The right-hand side is bounded (continuous $Df, f$ on a compact set near $\hat x$). The left-hand side is at least $c \|z^{(k+1)}\|$. So $\|z^{(k+1)}\| \leq 2 \|Df^T f\| / c$, bounded.

> [!note]- Lemma 3: Feasibility rate $\|g\| = O(1/\mu)$
> **Statement:** $\|g(x^{(k+1)})\| \leq C/\mu^{(k)}$ for some constant $C$ depending on the problem and the neighborhood.
>
> **Hint:** Direct consequence of Lemma 2 and the definition of $z^{(k+1)}$.
>
> **Why needed:** This is the quantitative rate at which feasibility is approached.
>
> > [!note]- Full proof
> > By Lemma 2, $\|z^{(k+1)}\| \leq M$ for some constant $M$. By definition $z^{(k+1)} = 2 \mu^{(k)} g(x^{(k+1)})$, so
> > $$\|g(x^{(k+1)})\| = \frac{\|z^{(k+1)}\|}{2 \mu^{(k)}} \leq \frac{M}{2 \mu^{(k)}}.$$
> > Set $C = M/2$.

> [!note]- Lemma 4: Limit point satisfies constrained KKT
> **Statement:** Any convergent subsequence $x^{(k_j)} \to \bar x$ (with corresponding $z^{(k_j)} \to \bar z$) satisfies $g(\bar x) = 0$ and the KKT stationarity $2 Df(\bar x)^T f(\bar x) + Dg(\bar x)^T \bar z = 0$.
>
> **Hint:** Pass to limits in Lemma 1 and Lemma 3 along the subsequence.
>
> **Why needed:** Identifies the limit as a constrained KKT point.
>
> > [!note]- Full proof
> > Boundedness of $\{z^{(k)}\}$ by Lemma 2 means we may extract a convergent subsequence $z^{(k_j)} \to \bar z$, refining if necessary so that $x^{(k_j)} \to \bar x$ also.
> >
> > From Lemma 3, $\|g(x^{(k_j)})\| \to 0$ as $k_j \to \infty$, so by continuity $g(\bar x) = 0$. So $\bar x$ is feasible.
> >
> > From Lemma 1 along the subsequence,
> > $$2 Df(x^{(k_j+1)})^T f(x^{(k_j+1)}) + Dg(x^{(k_j+1)})^T z^{(k_j+1)} = 0$$
> > for each $j$. Passing to the limit using continuity of $f, g, Df, Dg$:
> > $$2 Df(\bar x)^T f(\bar x) + Dg(\bar x)^T \bar z = 0.$$
> > So $(\bar x, \bar z)$ satisfies the constrained KKT system.

> [!note]- Lemma 5: Full-sequence convergence
> **Statement:** If $\hat x$ is an isolated constrained minimum (second-order sufficient condition holds), then the entire sequence $x^{(k)} \to \hat x$ and $z^{(k)} \to \hat z$.
>
> **Hint:** Argue by contradiction: every convergent subsequence has the same limit $\hat x$ (since $\hat x$ is the unique KKT point in the neighborhood). Boundedness of $\{(x^{(k)}, z^{(k)})\}$ and uniqueness of limit points implies convergence of the full sequence.
>
> **Why needed:** Strengthens subsequential convergence to full-sequence convergence.
>
> > [!note]- Full proof
> > By the second-order sufficient condition at $\hat x$, there is a neighborhood $V$ of $\hat x$ in which $\hat x$ is the unique constrained KKT point. The inner subproblems have minimizers near $\hat x$ (by the same condition), so $x^{(k+1)} \in V$ for all large $k$.
> >
> > Any convergent subsequence of $\{x^{(k+1)}\}$ has limit point in $V$ satisfying the constrained KKT (Lemma 4), hence equal to $\hat x$. So $\hat x$ is the *unique* limit point of the bounded sequence $\{x^{(k+1)}\}$, which implies $x^{(k+1)} \to \hat x$.
> >
> > Similarly, by LICQ at $\hat x$, the multiplier $\hat z$ corresponding to $\hat x$ is unique, so $z^{(k+1)} \to \hat z$.

---

# Formal Proof

> [!note]- Complete formal proof
> Assume the hypotheses: $\hat x$ is an isolated constrained minimum with LICQ ($Dg(\hat x)$ full row rank) and second-order sufficient condition; $f, g \in C^1$ near $\hat x$; $\mu^{(k)} \to \infty$; inner subproblems have minimizers $x^{(k+1)}$ near $\hat x$.
>
> **Step 0 — inner minimizers are well-defined.** The second-order sufficient condition at $\hat x$ guarantees that for each $\mu^{(k)}$ large enough, the penalty objective $\|f\|^2 + \mu^{(k)} \|g\|^2$ has a local minimizer $x^{(k+1)}$ in a fixed neighborhood of $\hat x$ (by the implicit function theorem applied to the optimality equations).
>
> **Step 1 — implicit KKT** (Lemma 1). At each $x^{(k+1)}$, defining $z^{(k+1)} = 2\mu^{(k)} g(x^{(k+1)})$, the KKT stationarity $2 Df(x^{(k+1)})^T f(x^{(k+1)}) + Dg(x^{(k+1)})^T z^{(k+1)} = 0$ holds.
>
> **Step 2 — boundedness** (Lemma 2). LICQ and the KKT stationarity bound $\|z^{(k+1)}\|$ uniformly.
>
> **Step 3 — feasibility rate** (Lemma 3). $\|g(x^{(k+1)})\| = \|z^{(k+1)}\|/(2\mu^{(k)}) = O(1/\mu^{(k)}) \to 0$.
>
> **Step 4 — subsequential KKT** (Lemma 4). Any convergent subsequence has a limit point $(\bar x, \bar z)$ with $g(\bar x) = 0$ and KKT stationarity.
>
> **Step 5 — full convergence** (Lemma 5). The isolated-minimum hypothesis upgrades subsequential to full convergence: $x^{(k+1)} \to \hat x$ and $z^{(k+1)} \to \hat z$.
>
> **Step 6 — rate.** Step 3 gives $\|g\| = O(1/\mu)$, which is the announced rate. For the $x^{(k+1)} \to \hat x$ rate transverse to the constraint, expand in the direction of $Dg^T$: a first-order Taylor expansion shows the transverse error in $x^{(k+1)}$ is $O(\|g\|) = O(1/\mu^{(k)})$.
>
> Combining Steps 1–6 gives the theorem. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Exterior penalty methods in linear programming (operations research).** Apply the same penalty idea to the *linear* program $\min c^T x$ s.t. $Ax = b$, $x \geq 0$, using $\mu \|Ax - b\|^2$ as the equality penalty and $\mu \max(0, -x)^2$ as the inequality penalty. The resulting algorithm converges to the LP optimum as $\mu \to \infty$, and the same $O(1/\mu)$ rate holds. This was a competitor to the simplex method before interior-point methods superseded it.

**Quadratic penalty for engineering optimization (structural design).** Truss optimization (minimize weight subject to stress constraints) is often solved by the penalty method, where the constraint penalty represents "stress safety margin violation." The convergence theorem here applies, and the $O(1/\mu)$ rate translates to the design's feasibility tolerance — a designer can predict how much $\mu$ to use to achieve a given safety margin.

**Lagrangian relaxation of integer programs (combinatorial optimization).** Drop integrality constraints by adding penalty terms — for example, $\mu \sum_i x_i(1 - x_i)^2$ to encourage $x_i \in \{0, 1\}$. As $\mu \to \infty$, solutions converge to integer feasibility. This is the penalty algorithm applied to a non-convex problem; the convergence theorem still holds locally but global optimality is not guaranteed. The technique is the basis of *quadratic unconstrained binary optimization* (QUBO) formulations used in quantum annealing.

---

# Bridges

- **Tikhonov regularization** — the inner subproblem $\min \|f(x)\|^2 + \mu \|g(x)\|^2$ is *exactly* Tikhonov-regularized LS with regularization term $\mu \|g(x)\|^2$. The convergence theorem here is, structurally, the statement that Tikhonov regularization parameter $\to \infty$ drives the regularization residual to zero — a basic result in linear inverse-problem theory generalized to the nonlinear setting.

- **[[Thm - Augmented Lagrangian Recovers Lagrange Multipliers|Augmented Lagrangian recovery]]** — the corresponding theorem for the augmented Lagrangian algorithm says the implicit multiplier $z^{(k+1)}$ satisfies KKT stationarity *exactly* at each iterate (not just in the limit), because the multiplier is tracked explicitly. The augmented Lagrangian theorem is the *iterate-level* analogue of this *limit-level* theorem.

- **Asymptotic equivalence of penalty and barrier methods** — for inequality constraints $g(x) \leq 0$, the **barrier method** adds $-\sum_i \log(-g_i(x))$ to the objective and drives the barrier coefficient to zero (rather than the penalty to infinity). The penalty and barrier methods give the same *limit* (the constrained optimum) at the same *rate* ($O(1/\mu)$ where $\mu$ is the relevant parameter), but the iteration paths differ — penalty approaches from outside the feasible region, barrier from inside. Both are convergent; both have conditioning issues at extreme parameter values; both are superseded by augmented Lagrangian / interior-point methods.

---

# Unlocked by This

> [!tip] Convergence of Penalty Methods for PDEs *(from Numerical PDEs)*
> When solving PDEs with Dirichlet boundary conditions, the **penalty method for boundary conditions** adds $\mu \int_{\partial \Omega} (u - g)^2$ to the variational formulation, enforcing $u = g$ on $\partial \Omega$ as $\mu \to \infty$. The discretized problem is a constrained nonlinear LS (or linear LS in linear cases), and this theorem governs the rate at which the boundary condition is satisfied: $\|u - g\|_{L^2(\partial \Omega)} = O(1/\mu)$. Combined with discretization error analysis, this gives the total error in penalty-enforced FEM solutions. The same theorem applies, in form, to *Nitsche's method* (a variational form of weak boundary-condition enforcement) where the conditioning is improved.

> [!tip] Sequential Penalty Methods for QP *(from Quadratic Programming)*
> When the objective and constraints are both quadratic / linear, the penalty method's subproblems are linear systems and the convergence rate $O(1/\mu)$ is recoverable in closed form. This gives an explicit comparison between penalty methods and active-set / interior-point methods for quadratic programming. Modern QP solvers do *not* use penalty methods (they use active set or interior point), but the analysis is instructive for understanding why.
