---
type: theorem
subject: multivariate-analysis
prereqs: []
tags: [analysis, multivariate-analysis, fixed-point]
---

# Notation

$(X, d)$ is a **metric space**: a set $X$ with a distance function $d : X \times X \to [0,\infty)$ satisfying $d(x,y) = 0 \iff x = y$, symmetry, and the triangle inequality. The space is **complete** if every Cauchy sequence — one whose terms eventually get arbitrarily close to each other — converges to a point of $X$. A map $T : X \to X$ is a **contraction** with constant $r$ if $d(Tx, Ty) \leq r\, d(x,y)$ for all $x, y$, with $r < 1$ fixed. A **fixed point** of $T$ is a point $x$ with $Tx = x$, and $T^k$ denotes the $k$-fold composition $T \circ \cdots \circ T$. The full registry is on [[Multivariate Analysis II — Inverse and Implicit Function Theorems]].

---

# Statement

> **Contraction mapping principle (Banach fixed-point theorem).** Let $(X, d)$ be a non-empty complete metric space and $T : X \to X$ a contraction: there is a constant $r < 1$ with
> $$d(Tx, Ty) \leq r\, d(x,y) \qquad \text{for all } x, y \in X.$$
> Then $T$ has **exactly one** fixed point $x^* \in X$. Moreover, for *every* starting point $x_0 \in X$, the sequence of iterates $x_k = T^k x_0$ converges to $x^*$, with the explicit error bound
> $$d(x_k, x^*) \leq \frac{r^k}{1 - r}\, d(x_0, x_1).$$

---

# Motivation

A vast number of mathematical problems take the form "solve the equation $\Phi(x) = 0$" — and most such equations have no closed-form solution. What do you do when you cannot write the answer down? The contraction mapping principle is the most important single answer to that question: it is a *machine for proving an equation has a solution*, and for *computing the solution by iteration*, without ever needing a formula.

The trick is a change of viewpoint. Instead of solving $\Phi(x) = 0$ directly, algebraically rearrange it into the form $Tx = x$ — the solution is now a *fixed point* of $T$ rather than a zero of $\Phi$. (For instance, $\Phi(x) = 0$ might rearrange to $x = x - \Phi(x) =: Tx$.) Now ask: why would $T$ have a fixed point? Imagine iterating $T$: pick any $x_0$, form $x_1 = Tx_0$, $x_2 = Tx_1$, and so on. If $T$ *shrinks distances* — if applying $T$ always brings points closer together — then the successive iterates crowd ever more tightly, the gaps between them shrink geometrically, and the sequence has nowhere to go but to converge. Its limit, being unmoved by the further application of $T$, is a fixed point.

That is the entire idea, and its power lies in how *cheap* the hypothesis is. You do not need to know anything about the solution; you need only check one inequality — that $T$ is a contraction — and the theorem hands you existence, uniqueness, *and* a convergent algorithm with a computable error bound. It is the engine underneath the [[Thm - The Inverse Function Theorem|inverse function theorem]] (which solves $f(x) = y$ for $x$), underneath the Picard existence theorem for differential equations (which solves an integral equation for the trajectory), and underneath Newton's method. Whenever this topic — or much of analysis — proves that something *exists* by solving an equation, the contraction mapping principle is doing the work.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$T$ is a contraction on a complete space". The skill is recognizing contractions in disguise.

The first disguised source is **a map whose derivative is uniformly small.** Property $B$: $T : U \to U$ is $C^1$ on a convex set with $\lVert DT\rVert \leq r < 1$ everywhere. The bridge is the mean value inequality (see [[Thm - The Mean Value Inequality]]): a bound on the derivative integrates to a bound on the increment, $|Tx - Ty| \leq r|x - y|$. So a *differential* smallness condition produces the *global* contraction property. The non-obviousness: contraction is a statement about all pairs of points, yet it follows from a pointwise bound on a derivative. *Example:* in the proof of the inverse function theorem, the auxiliary map $x \mapsto y - \varphi(x)$ is shown to be a contraction precisely by making $\lVert D\varphi\rVert \leq \tfrac12$.

The second disguised source is **an integral operator with a short time interval or small kernel.** Property $B$: $T$ is the operator $(Ty)(t) = y_0 + \int_{t_0}^t F(s, y(s))\,ds$ on continuous functions, where $F$ is Lipschitz in $y$. The bridge: the integral over a short interval $[t_0, t_0 + T]$ multiplies the Lipschitz constant by the small length $T$, making $T \cdot L < 1$. The non-obviousness: the "points" of the metric space are now *functions*, and the contraction lives in the supremum metric. *Example:* the Picard–Lindelöf existence theorem for ordinary differential equations.

The third disguised source is **a self-map of a complete space that strictly decreases a "potential" comparably to the distance moved.** Property $B$: less obvious settings — projections onto convex sets, averaging operators, the Bellman operator of dynamic programming — turn out to be contractions in an appropriate metric. The bridge is identifying the right complete metric in which the shrinkage is visible. *Example:* the Bellman operator in dynamic programming is a contraction in the supremum norm with constant the discount factor, which is why value iteration converges.

**Targets (Output Amplification)**

The conclusion is "$T$ has a unique fixed point, reached by iteration".

Combine the conclusion with **a parameter on which $T$ depends continuously.** Property $D$: $T = T_\lambda$ varies continuously (or smoothly) with a parameter $\lambda$, with a *uniform* contraction constant. The amplified result $E$: the fixed point $x^*(\lambda)$ depends continuously (or smoothly) on $\lambda$ — a *parametrized* existence statement. This is exactly the mechanism by which the inverse and implicit functions inherit the smoothness of the data: the solution of a contraction problem is as regular as the problem.

Combine the conclusion with **the explicit geometric error bound.** Property $D$: the bound $d(x_k, x^*) \leq \frac{r^k}{1-r}d(x_0, x_1)$. The amplified result $E$: not just *existence* but a *certified algorithm* — you can compute the solution to any prescribed accuracy and know in advance how many iterations are needed. This converts a pure existence theorem into a numerical method.

Combine the conclusion with **a small perturbation of the map.** Property $D$: $\tilde T$ is uniformly close to a contraction $T$. The amplified result $E$: $\tilde T$, if still a contraction, has a fixed point close to that of $T$ — fixed points are *stable* under perturbation. This is the basis of structural-stability and continuation arguments.

---

# Why Is It True

Watch the iterates and the proof writes itself. Start anywhere at $x_0$, and let $x_1 = Tx_0$, $x_2 = Tx_1$, and so on. The first step moves you a distance $d(x_0, x_1)$. The next step is the *image* of that step under $T$, and $T$ shrinks distances by the factor $r$, so $d(x_1, x_2) \leq r\, d(x_0, x_1)$. The step after that is shrunk again: $d(x_2, x_3) \leq r\, d(x_1, x_2) \leq r^2 d(x_0, x_1)$. In general the $k$-th step has length at most $r^k d(x_0, x_1)$. The steps form a *geometric sequence*, and a geometric sequence with ratio $r < 1$ has a *finite total length*: $\sum_k r^k d(x_0,x_1) = \frac{d(x_0,x_1)}{1-r} < \infty$.

A sequence whose steps have finite total length cannot wander off — its terms eventually huddle together, because the tail of a convergent series is small. That is precisely the Cauchy property. And here is where *completeness* enters, doing the one job no contraction estimate can do: a Cauchy sequence has terms that *want* to converge, but it needs the space to actually *contain* a limit point for them to converge to. Completeness is the guarantee that the limit exists *in $X$*. (On the incomplete space $\mathbb{Q}$, the contraction $x \mapsto x/2 + 1/x$ has iterates Cauchy and crowding toward $\sqrt 2$ — but $\sqrt 2 \notin \mathbb{Q}$, so there is no fixed point. The hypothesis is not decorative.)

Once the iterates converge to a limit $x^*$, that limit is a fixed point: applying $T$ to the relation $x_{k+1} = Tx_k$ and letting $k \to \infty$, the left side tends to $x^*$ and the right side tends to $Tx^*$ (a contraction is continuous), so $x^* = Tx^*$.

Uniqueness is the easiest part and the most striking. Suppose $x^*$ and $y^*$ were *two* fixed points. Then $d(x^*, y^*) = d(Tx^*, Ty^*) \leq r\, d(x^*, y^*)$. A non-negative number that is at most $r$ times itself, with $r < 1$, must be zero. So $x^* = y^*$. The contraction property does not merely *permit* a unique fixed point — it *forbids* two, because two distinct fixed points would be a pair of points that $T$ fails to bring closer, contradicting that $T$ brings every pair closer.

So one should expect the theorem because a distance-shrinking map leaves its iterates no room to do anything but converge, and convergence with shrinkage forces the limit to be a fixed point — the unique one, since the shrinkage collapses any two candidates together.

---

# What Makes This Hard

The conceptual difficulty is recognizing that the *hard part is supplied by completeness, not by the contraction estimate*: the contraction inequality alone proves the iterates are Cauchy, but it is completeness that converts "Cauchy" into "convergent to a point of $X$", and forgetting this is the most common gap — the theorem is genuinely false on incomplete spaces. A second subtlety, important in applications, is that the metric space is often a space of *functions* with the supremum metric, so the "point" $x^*$ being constructed is itself a function and one must verify $T$ maps the chosen function space into itself before checking the contraction estimate.

---

# Rederivation Scaffold

**High-level strategy:**
Iterate $T$ from any starting point. Bound consecutive gaps by a geometric sequence using the contraction property. Sum the geometric series to show the iterates are Cauchy; invoke completeness for a limit; continuity of $T$ makes the limit a fixed point; the contraction property makes it unique.

**Subgoal decomposition:**

1. **Bound consecutive gaps geometrically.** Show $d(x_k, x_{k+1}) \leq r^k d(x_0, x_1)$.
   - *Hint:* Induct: $d(x_{k+1}, x_{k+2}) = d(Tx_k, Tx_{k+1}) \leq r\, d(x_k, x_{k+1})$.
   - *Why needed:* It converts the iteration into a geometric sequence of step lengths.

2. **Show the iterates are Cauchy.** Bound $d(x_k, x_{k+m})$ by a geometric tail.
   - *Hint:* Triangle inequality: $d(x_k, x_{k+m}) \leq \sum_{i=0}^{m-1}d(x_{k+i}, x_{k+i+1}) \leq d(x_0,x_1)\sum_{i\geq k}r^i = \frac{r^k}{1-r}d(x_0,x_1)$.
   - *Why needed:* A Cauchy sequence is the input completeness needs.

3. **Produce the limit.** Invoke completeness: the Cauchy sequence converges to some $x^* \in X$.
   - *Hint:* This is the *definition* of completeness; it is the only place that hypothesis is used.
   - *Why needed:* Without it the iterates crowd toward a "hole" not in $X$.

4. **Show the limit is a fixed point.** Pass to the limit in $x_{k+1} = Tx_k$.
   - *Hint:* $T$ is continuous (contractions are Lipschitz), so $Tx_k \to Tx^*$; also $x_{k+1} \to x^*$.
   - *Why needed:* It establishes existence.

5. **Show uniqueness.** If $Tx^* = x^*$ and $Ty^* = y^*$, then $d(x^*,y^*) \leq r\,d(x^*,y^*)$ forces $d = 0$.
   - *Hint:* A non-negative number $\leq r$ times itself, $r < 1$, is zero.
   - *Why needed:* It completes the statement and yields the error bound by letting $m \to \infty$ in step 2.

---

# Lemma Decomposition

> [!note]- Lemma 1: The iterates form a Cauchy sequence
> **Statement:** With $x_k = T^k x_0$, for all $k$ and $m$, $d(x_k, x_{k+m}) \leq \frac{r^k}{1-r}d(x_0, x_1)$. Hence $(x_k)$ is Cauchy.
>
> **Hint:** First bound a single gap $d(x_j, x_{j+1}) \leq r^j d(x_0,x_1)$ by induction, then chain gaps with the triangle inequality and sum the geometric series.
>
> **Why needed:** It is the heart of the proof — everything except the existence of a limit and uniqueness.
>
> > [!note]- Full proof
> > *Single gap.* By induction on $j$: the base $j = 0$ is trivial, and $d(x_{j+1}, x_{j+2}) = d(Tx_j, Tx_{j+1}) \leq r\,d(x_j, x_{j+1}) \leq r\cdot r^j d(x_0,x_1) = r^{j+1}d(x_0,x_1)$.
> >
> > *Chained gaps.* By the triangle inequality,
> > $$d(x_k, x_{k+m}) \leq \sum_{i=0}^{m-1}d(x_{k+i}, x_{k+i+1}) \leq \sum_{i=0}^{m-1}r^{k+i}d(x_0,x_1) = r^k d(x_0,x_1)\sum_{i=0}^{m-1}r^i.$$
> > Since $r < 1$, $\sum_{i=0}^{m-1}r^i \leq \sum_{i=0}^\infty r^i = \frac{1}{1-r}$, giving $d(x_k, x_{k+m}) \leq \frac{r^k}{1-r}d(x_0,x_1)$.
> >
> > *Cauchy.* As $k \to \infty$, $r^k \to 0$, so the bound tends to $0$ uniformly in $m$; hence for any $\varepsilon > 0$ there is $K$ with $d(x_k, x_{k+m}) < \varepsilon$ for all $k \geq K$ and all $m$. That is the Cauchy property.

> [!note]- Lemma 2: A contraction is continuous
> **Statement:** A contraction $T$ is (Lipschitz) continuous: $x_k \to x$ implies $Tx_k \to Tx$.
>
> **Hint:** Apply the contraction inequality directly.
>
> **Why needed:** It lets the limit be passed through $T$ in the relation $x_{k+1} = Tx_k$, which is what makes the limit a fixed point.
>
> > [!note]- Full proof
> > If $x_k \to x$, then $d(Tx_k, Tx) \leq r\, d(x_k, x) \to 0$, so $Tx_k \to Tx$. (Any Lipschitz map is continuous; a contraction is Lipschitz with constant $r < 1$.)

---

# Formal Proof

> [!note]- Complete formal proof
> Let $(X, d)$ be non-empty and complete, $T : X \to X$ with $d(Tx, Ty) \leq r\,d(x,y)$, $r < 1$. Pick any $x_0 \in X$ and set $x_k = T^k x_0$.
>
> **Existence.** By Lemma 1, $(x_k)$ is a Cauchy sequence. Since $X$ is complete, it converges to some $x^* \in X$. By Lemma 2, $T$ is continuous, so $Tx_k \to Tx^*$. But $Tx_k = x_{k+1} \to x^*$ as well. A sequence has a unique limit, so $Tx^* = x^*$: $x^*$ is a fixed point.
>
> **Uniqueness.** Suppose $x^*$ and $y^*$ are both fixed points. Then
> $$d(x^*, y^*) = d(Tx^*, Ty^*) \leq r\, d(x^*, y^*).$$
> Hence $(1 - r)\,d(x^*, y^*) \leq 0$. Since $1 - r > 0$ and $d \geq 0$, this forces $d(x^*, y^*) = 0$, so $x^* = y^*$.
>
> **Error bound.** In Lemma 1's inequality $d(x_k, x_{k+m}) \leq \frac{r^k}{1-r}d(x_0,x_1)$, let $m \to \infty$. Since $x_{k+m} \to x^*$ and $d$ is continuous, the left side tends to $d(x_k, x^*)$, giving
> $$d(x_k, x^*) \leq \frac{r^k}{1-r}\,d(x_0, x_1).$$
> So the iterates from any starting point converge to $x^*$ geometrically. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Existence of solutions to differential equations.** Recast the initial value problem $y' = F(t,y)$, $y(t_0) = y_0$ as the integral equation $y(t) = y_0 + \int_{t_0}^t F(s,y(s))\,ds$. The right-hand side is an operator $T$ on continuous functions; if $F$ is Lipschitz in $y$, then on a short enough time interval $T$ is a contraction in the supremum metric, and its fixed point is the solution. The application is nonobvious because the "points" are functions and the contraction lives in an infinite-dimensional space — yet the theorem applies verbatim. This is the Picard–Lindelöf theorem.

**Newton's method and fast root-finding.** Newton's iteration $x_{k+1} = x_k - f(x_k)/f'(x_k)$ is the iteration of a map $N$ whose fixed points are the roots of $f$. Near a simple root $N$ is a contraction — in fact $N'$ vanishes at the root — so the convergence is not merely geometric but *quadratic*. The application battle-tests the principle: the contraction property explains *why* Newton's method converges, and the vanishing derivative explains why it converges so fast.

**Dynamic programming and the Bellman equation.** In an infinite-horizon decision problem with discount factor $\beta < 1$, the optimal value function solves the Bellman equation $V = TV$, where $T$ is the Bellman operator. $T$ is a contraction in the supremum norm with constant $\beta$, so the value function exists, is unique, and is computed by *value iteration* — iterating $T$ from any guess. The application is out-of-distribution because the fixed point is an entire optimal policy, and the discount factor *is* the contraction constant.

---

# Bridges

- **[[Thm - The Inverse Function Theorem]]** — the principal client. The inverse function theorem is proved by solving $f(x) = y$ for $x$, rewritten as the fixed-point problem $x = x + (y - f(x))$ (after normalizing the derivative); the contraction estimate comes from the derivative being close to the identity.

- **[[Thm - The Implicit Function Theorem]]** — a corollary of the inverse function theorem, hence ultimately of this principle. The implicit function $g$ is the fixed point of a contraction depending on the free parameter $x$, and its smoothness is the parametrized-fixed-point amplification.

- **[[Thm - The Mean Value Inequality]]** — the standard supplier of contractions. A bound $\lVert DT\rVert \leq r < 1$ on a convex set integrates, via the mean value inequality, to the contraction estimate $|Tx - Ty| \leq r|x-y|$.

- **The Picard–Lindelöf theorem** — the existence-and-uniqueness theorem for ordinary differential equations, which is this principle applied to an integral operator on a function space.

---

# Unlocked by This

> [!tip] Existence and Uniqueness for ODEs *(from Dynamical Systems)*
> Recasting an initial value problem as an integral equation makes the solution a fixed point of a contraction on a function space — this is the **Picard–Lindelöf theorem**, the foundational existence-and-uniqueness result for ordinary differential equations and the starting point of dynamical systems.

> [!tip] The Stable Manifold Theorem *(from Dynamical Systems)*
> Near a hyperbolic fixed point of a dynamical system, the stable and unstable manifolds are constructed as fixed points of contraction operators on spaces of curves — a more elaborate application of the same principle, central to the qualitative theory of dynamical systems.
