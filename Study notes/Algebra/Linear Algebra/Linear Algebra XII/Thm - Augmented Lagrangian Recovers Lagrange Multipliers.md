---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Augmented Lagrangian Algorithm"
  - "Def - Constrained Nonlinear Least Squares"
tags: [algebra, linear-algebra, applied, optimization, convergence]
---

# Notation

Let $f : \mathbb{R}^n \to \mathbb{R}^m$ and $g : \mathbb{R}^n \to \mathbb{R}^p$ be continuously differentiable. The augmented Lagrangian is
$$L_\mu(x, z) = \|f(x)\|^2 + g(x)^T z + \mu \|g(x)\|^2.$$
The algorithm produces iterates $(x^{(k+1)}, z^{(k+1)})$ with $x^{(k+1)}$ minimizing $L_{\mu^{(k)}}(\cdot, z^{(k)})$ and $z^{(k+1)} = z^{(k)} + 2\mu^{(k)} g(x^{(k+1)})$. The full registry is on [[Linear Algebra XII — Applied III — Nonlinear Least Squares]].

---

# Statement

> **Theorem (Augmented Lagrangian iterate satisfies KKT stationarity).** Let $\tilde x$ be a (local) minimizer of $L_\mu(\cdot, z)$ over $x$, for some fixed $z \in \mathbb{R}^p$ and $\mu > 0$. Define
> $$\tilde z := z + 2 \mu \, g(\tilde x).$$
> Then the pair $(\tilde x, \tilde z)$ satisfies the KKT stationarity condition for the constrained problem $\min \|f(x)\|^2$ s.t. $g(x) = 0$:
> $$2 Df(\tilde x)^T f(\tilde x) + Dg(\tilde x)^T \tilde z = 0.$$
>
> **Corollary (algorithm produces stationary iterates).** Each pair $(x^{(k+1)}, z^{(k+1)})$ produced by the augmented Lagrangian algorithm satisfies the KKT stationarity condition exactly (modulo inner-loop tolerance).
>
> **Corollary (feasibility is the only obstacle).** The augmented Lagrangian algorithm terminates at a constrained KKT point as soon as $\|g(x^{(k+1)})\|$ falls below the required tolerance.

---

# Motivation

This is the structural fact that makes the augmented Lagrangian algorithm work. The penalty algorithm's flaw was that constraint enforcement required $\mu \to \infty$; this theorem says the augmented Lagrangian *avoids* that requirement by transferring the work of enforcing the KKT stationarity to the multiplier update.

The content is: at *every* outer iteration, the pair $(x^{(k+1)}, z^{(k+1)})$ satisfies the KKT stationarity condition $2 Df^T f + Dg^T z = 0$ exactly — not approximately, not in the limit, but exactly (modulo inner-loop tolerance, which can be made as small as we want by running Levenberg–Marquardt to a tight tolerance). So the only condition the algorithm has to drive to zero is the *feasibility* condition $g(x) = 0$, achieved by the geometric/linear convergence of $g(x^{(k)}) \to 0$ as $z^{(k)} \to \hat z$.

This is a deep structural fact, not a convergence rate claim. The rate of convergence (linear, with rate depending on $\mu$ and the constraint curvature) is a separate result. What *this* theorem says is that the algorithm is *iteratively consistent*: it does not waste iterations chasing KKT stationarity, because the update structure makes stationarity automatic.

The contrast with the penalty algorithm sharpens the point. Penalty algorithm: at each iterate, KKT stationarity holds with implicit multiplier $2\mu^{(k)} g(x^{(k+1)})$, but the implicit multiplier blows up as $\mu \to \infty$ in lockstep with $\|g\| \to 0$, so the inner subproblem is increasingly ill-conditioned. Augmented Lagrangian: KKT stationarity holds with explicit multiplier $z^{(k+1)}$, which converges to $\hat z$ at a *bounded* rate, decoupled from $\mu$.

---

# Sources and Targets

**Sources (Input Broadening).**

The first disguised source is **any method-of-multipliers algorithm in convex optimization**. The theorem's mechanism — that the inner optimality identifies a KKT-stationary pair $(\tilde x, \tilde z)$ with $\tilde z$ as the "next multiplier" — is the structural insight behind ADMM, dual decomposition, and proximal methods on dual problems. The non-obvious step is to recognize "augmented Lagrangian for NLS" as a special case of "method of multipliers for general convex problems with strong duality." *Example problem:* Prove convergence of the ADMM algorithm for $\min f(x) + g(y)$ s.t. $Ax + By = c$ by adapting this theorem.

The second disguised source is **interior-point methods for nonlinear programming**. IPOPT and similar solvers maintain an explicit Lagrange-multiplier estimate that is updated alongside the primal variable; the same KKT-identification structure applies, with the difference that the multiplier update is determined by the barrier function rather than a simple gradient-ascent rule. The non-obviousness: the same "identify the multiplier via the inner optimality, update it explicitly" pattern unifies augmented Lagrangian, interior-point, and SQP methods.

The third disguised source is **fixed-point iteration on the KKT system**. The pair $(x^{(k)}, z^{(k)})$ is approaching the fixed point $(\hat x, \hat z)$ of the KKT operator, and the augmented Lagrangian iteration is a *contraction* for that fixed point. The non-obvious step is to recognize that "minimize over $x$, then update $z$" is structurally a Gauss-Seidel-style fixed-point iteration on the saddle-point system. *Example problem:* Show that augmented Lagrangian convergence is governed by the spectrum of a particular linearized operator at the KKT point.

**Targets (Output Amplification).**

Combine the theorem with **the explicit feasibility-rate analysis**. The theorem says: each iterate is KKT-stationary; the algorithm terminates when feasibility holds. Combining with a feasibility-rate result ($\|g(x^{(k+1)})\| \leq \alpha^k \|g(x^{(1)})\|$ for some $\alpha < 1$, under stronger hypotheses) gives the full convergence rate: the algorithm achieves $\|g\| \leq \varepsilon$ in $O(\log(1/\varepsilon)/\log(1/\alpha))$ iterations. Compared to the penalty algorithm's $O(1/\varepsilon)$, this is exponentially faster.

Combine the theorem with **the inner-loop Levenberg–Marquardt's quadratic convergence**. Each inner Levenberg–Marquardt solve has its own quadratic local convergence (modulo trust-region adaptivity). Combined: the total number of inner Levenberg–Marquardt iterations across the entire augmented Lagrangian algorithm is $O(\text{outer iterations} \times \text{inner iterations per outer})$, with both factors small in practice. This explains why augmented Lagrangian achieves tight constraint satisfaction in a number of *total* Levenberg–Marquardt iterations that is orders of magnitude smaller than the penalty algorithm.

Combine the theorem with **the augmented Lagrangian's connection to ADMM**. ADMM applies the augmented Lagrangian idea to a *block-separable* problem $\min f(x) + g(y)$ s.t. $Ax + By = c$, alternating between $x$-minimization and $y$-minimization with the multiplier update between them. Each block-minimization step produces a partial KKT-stationary pair, and the alternation drives the joint feasibility to zero. ADMM inherits and parallelizes the KKT-identification structure proved here.

---

# Why Is It True

**The mechanism in one sentence: the optimality condition for the unconstrained augmented Lagrangian minimization is algebraically identical to the constrained KKT stationarity, with $z^{(k)} + 2\mu^{(k)} g(x^{(k+1)})$ playing the role of the Lagrange multiplier.**

The augmented Lagrangian's gradient with respect to $x$ is
$$\nabla_x L_\mu(x, z) = 2 Df(x)^T f(x) + Dg(x)^T z + 2 \mu \, Dg(x)^T g(x).$$
Grouping the $z$ and $g$ terms,
$$\nabla_x L_\mu(x, z) = 2 Df(x)^T f(x) + Dg(x)^T (z + 2 \mu g(x)).$$
At an inner-loop minimum $\tilde x$, this gradient is zero:
$$0 = 2 Df(\tilde x)^T f(\tilde x) + Dg(\tilde x)^T (z + 2 \mu g(\tilde x)).$$
Defining $\tilde z = z + 2\mu g(\tilde x)$, this reads
$$2 Df(\tilde x)^T f(\tilde x) + Dg(\tilde x)^T \tilde z = 0,$$
which is precisely the KKT stationarity condition for the *original* constrained problem.

That is the entire proof. The augmented Lagrangian was *designed* so that this rewriting works: the $z^T g$ term contributes $Dg^T z$ to the gradient, and the $\mu \|g\|^2$ term contributes $2 \mu Dg^T g$, and these two terms combine into $Dg^T (z + 2\mu g)$ — exactly the KKT-stationarity contribution with the updated multiplier.

The multiplier update $z \leftarrow z + 2 \mu g(x)$ is forced: it is the *unique* update rule that makes the inner-loop optimality coincide with the constrained KKT stationarity at $(x, z_\text{new})$. Any other update rule for $z$ would fail the algebraic identity.

This is why the augmented Lagrangian is "the right" generalization of the penalty algorithm: the multiplier update was not chosen by analogy with anything else; it was *derived* by demanding consistency between inner and outer optimality.

---

# What Makes This Hard

The theorem itself is a simple algebraic rearrangement once one sees the right grouping; the non-trivial step is *discovering* the augmented Lagrangian function and the matching multiplier-update rule simultaneously. Historically, Hestenes (1969) and Powell (1969) independently arrived at this combination after the penalty algorithm's failure was understood; neither presented the algebraic derivation as cleanly as it now appears. The common error in re-deriving the algorithm is to add only the multiplier term $z^T g$ (without the penalty $\mu \|g\|^2$), giving an algorithm that satisfies KKT stationarity exactly but lacks the inner-loop convexity that the $\mu \|g\|^2$ term provides — the algorithm is then unstable and may fail to have inner minimizers.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Compute the gradient of $L_\mu(x, z)$ with respect to $x$, [[Def - Group|group]] the constraint-related terms, identify the result with the KKT stationarity at the multiplier $z + 2\mu g(x)$.

**Subgoal decomposition:**

1. **Gradient of $L_\mu$ with respect to $x$.** Compute $\nabla_x L_\mu(x, z)$ using the chain rule on $\|f\|^2$, $g^T z$, and $\|g\|^2$.
   - *Hint:* $\nabla_x \|f\|^2 = 2 Df^T f$; $\nabla_x (g^T z) = Dg^T z$; $\nabla_x \|g\|^2 = 2 Dg^T g$. Sum these.
   - *Why needed:* The optimality condition is $\nabla_x L_\mu = 0$; we need its explicit form.

2. **[[Def - Group|Group]] constraint-related terms.** Combine $Dg^T z + 2\mu Dg^T g = Dg^T (z + 2\mu g)$.
   - *Hint:* Linearity of $Dg^T$ in the argument.
   - *Why needed:* Reveals the inner optimality as a KKT-shaped equation with an "updated multiplier."

3. **Identify with KKT stationarity.** The equation $2 Df^T f + Dg^T (z + 2\mu g) = 0$ is exactly the constrained KKT stationarity with multiplier $\tilde z = z + 2\mu g$.
   - *Hint:* Compare with the definition of constrained KKT stationarity at $(\tilde x, \tilde z)$.
   - *Why needed:* This is the theorem's conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Gradient of the augmented Lagrangian
> **Statement:** $\nabla_x L_\mu(x, z) = 2 Df(x)^T f(x) + Dg(x)^T z + 2\mu Dg(x)^T g(x)$.
>
> **Hint:** Chain rule applied to each of the three terms in $L_\mu = \|f\|^2 + g^T z + \mu \|g\|^2$.
>
> **Why needed:** The optimality condition at the inner minimum is $\nabla_x L_\mu = 0$; we need its explicit form to manipulate it.
>
> > [!note]- Full proof
> > Term by term:
> >
> > 1. $\nabla_x (f(x)^T f(x))$ — by the chain rule with $\phi(x) = f(x)^T f(x)$, we have $\nabla \phi = 2 Df^T f$. (One way to see this: $\phi(x) = \sum_i f_i(x)^2$, so $\partial \phi/\partial x_j = \sum_i 2 f_i \partial f_i/\partial x_j = 2 (Df^T f)_j$.)
> >
> > 2. $\nabla_x (g(x)^T z)$ — since $z$ is constant in $x$, and $g(x)^T z = \sum_i g_i(x) z_i$, we have $\partial/\partial x_j (g^T z) = \sum_i z_i \partial g_i/\partial x_j = (Dg^T z)_j$, so $\nabla_x (g^T z) = Dg^T z$.
> >
> > 3. $\nabla_x (g(x)^T g(x)) = 2 Dg^T g$ — same computation as term 1.
> >
> > Summing, $\nabla_x L_\mu = 2 Df^T f + Dg^T z + 2 \mu Dg^T g$.

> [!note]- Lemma 2: Grouping the constraint terms
> **Statement:** $Dg(x)^T z + 2\mu Dg(x)^T g(x) = Dg(x)^T (z + 2\mu g(x))$ for any vector $z$ and any $x$.
>
> **Hint:** $Dg(x)^T$ is a linear operator from $\mathbb{R}^p$ to $\mathbb{R}^n$, so it distributes over vector sums.
>
> **Why needed:** Reveals the KKT-stationarity structure of the optimality condition.
>
> > [!note]- Full proof
> > By linearity of the linear operator $Dg(x)^T : \mathbb{R}^p \to \mathbb{R}^n$ (or equivalently of matrix-vector multiplication), $Dg^T z + Dg^T (2\mu g) = Dg^T (z + 2\mu g)$.

> [!note]- Lemma 3: Optimality condition rewritten
> **Statement:** Setting $\nabla_x L_\mu(\tilde x, z) = 0$ and defining $\tilde z = z + 2\mu g(\tilde x)$ gives $2 Df(\tilde x)^T f(\tilde x) + Dg(\tilde x)^T \tilde z = 0$, the KKT stationarity at $(\tilde x, \tilde z)$.
>
> **Hint:** Combine Lemmas 1 and 2 and substitute the definition of $\tilde z$.
>
> **Why needed:** This is the theorem's conclusion.
>
> > [!note]- Full proof
> > By Lemma 1, $\nabla_x L_\mu(\tilde x, z) = 0$ becomes $2 Df(\tilde x)^T f(\tilde x) + Dg(\tilde x)^T z + 2\mu Dg(\tilde x)^T g(\tilde x) = 0$. By Lemma 2 the last two terms combine to $Dg(\tilde x)^T (z + 2\mu g(\tilde x)) = Dg(\tilde x)^T \tilde z$. Therefore $2 Df(\tilde x)^T f(\tilde x) + Dg(\tilde x)^T \tilde z = 0$, which is the constrained KKT stationarity at $(\tilde x, \tilde z)$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 1 — gradient of the augmented Lagrangian** (Lemma 1). For any $x, z, \mu$,
> $$\nabla_x L_\mu(x, z) = 2 Df(x)^T f(x) + Dg(x)^T z + 2\mu Dg(x)^T g(x).$$
>
> **Step 2 — at an inner minimum $\tilde x$, the gradient vanishes.** A local minimum of $L_\mu(\cdot, z)$ in the interior of the domain (no constraints on the minimization over $x$) satisfies $\nabla_x L_\mu(\tilde x, z) = 0$, so
> $$2 Df(\tilde x)^T f(\tilde x) + Dg(\tilde x)^T z + 2\mu Dg(\tilde x)^T g(\tilde x) = 0.$$
>
> **Step 3 — group constraint terms** (Lemma 2). The last two terms combine:
> $$Dg(\tilde x)^T z + 2\mu Dg(\tilde x)^T g(\tilde x) = Dg(\tilde x)^T (z + 2\mu g(\tilde x)).$$
>
> **Step 4 — identify the updated multiplier.** Define $\tilde z = z + 2\mu g(\tilde x)$. Substituting:
> $$2 Df(\tilde x)^T f(\tilde x) + Dg(\tilde x)^T \tilde z = 0.$$
> This is the KKT stationarity condition for the constrained problem $\min \|f(x)\|^2$ s.t. $g(x) = 0$ at the pair $(\tilde x, \tilde z)$.
>
> **Step 5 — apply to algorithm iterates.** In the augmented Lagrangian algorithm, $x^{(k+1)}$ is the inner minimizer with $z = z^{(k)}$, $\mu = \mu^{(k)}$; the multiplier update step sets $z^{(k+1)} = z^{(k)} + 2\mu^{(k)} g(x^{(k+1)})$ — exactly the $\tilde z$ formula. So each pair $(x^{(k+1)}, z^{(k+1)})$ satisfies the KKT stationarity condition.
>
> **Step 6 — corollary.** The algorithm terminates at a constrained KKT point as soon as $g(x^{(k+1)}) = 0$ (feasibility), because KKT stationarity is automatic at every iterate.
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**ADMM derivation (distributed optimization).** Specialize this theorem to the separable problem $\min \phi(x) + \psi(y)$ s.t. $Ax + By = c$, with augmented Lagrangian $L_\mu(x, y, z) = \phi(x) + \psi(y) + z^T(Ax + By - c) + \mu \|Ax + By - c\|^2$. The ADMM algorithm alternates $x$-minimization and $y$-minimization, with $z$ updated by the same rule $z \leftarrow z + 2\mu (Ax + By - c)$ as here. Adapting the theorem to ADMM gives partial-KKT-stationarity statements at each iterate. This is the standard derivation of ADMM convergence properties.

**Lagrangian duality for convex programming (convex optimization).** For convex $\phi$ and $g$, the Lagrangian dual $\phi^*(z) = \min_x \phi(x) + z^T g(x)$ has the property that $\phi^*(z) \leq \phi(\hat x)$ for any $z \geq 0$, with equality at the optimal multiplier (strong duality, under Slater's condition). The augmented Lagrangian's mechanism — that inner optimality coincides with KKT stationarity at an updated multiplier — is the *primal* perspective on the duality theory's dual gradient ascent.

**Newton's method on the KKT system (sequential quadratic programming).** A different approach is to apply Newton's method directly to the saddle-point KKT system $\{ 2Df^T f + Dg^T z = 0, \; g(x) = 0 \}$ in $(x, z)$ jointly. This is the SQP starting point. The augmented Lagrangian theorem can be used to *prove* that SQP and augmented Lagrangian produce the same iterates near the solution (for appropriate parameter choices), reconciling the two algorithmic families.

---

# Bridges

- **[[Thm - Convergence of Penalty Algorithm|Penalty algorithm convergence]]** — the corresponding penalty theorem says the implicit multiplier $2\mu^{(k)} g(x^{(k+1)})$ converges to $\hat z$ *in the limit* as $\mu \to \infty$. The augmented Lagrangian theorem here is the iterate-level analogue: the multiplier is correct *at each iterate* with $\mu$ moderate, because the multiplier is explicitly tracked rather than implicitly produced. The two theorems together explain why augmented Lagrangian dominates penalty in practice.

- **KKT necessary conditions for nonlinear programming** — the constrained KKT stationarity condition is itself a theorem (necessary conditions for a constrained minimum under LICQ); the augmented Lagrangian theorem says these necessary conditions are *iteratively satisfiable* by a particular algorithmic structure. The KKT conditions are the *target*; the augmented Lagrangian is one way to *reach* the target.

- **Dual gradient ascent in convex optimization** — for convex problems with strong duality, the multiplier update $z \leftarrow z + 2\mu g(\tilde x)$ is a *gradient ascent* step on the dual function $\phi(z) = \min_x L_\mu(x, z)$, with step size $2\mu$. The theorem here gives the corresponding statement on the primal side: the primal iterate is KKT-stationary at the dual ascent's current $z$. The augmented Lagrangian is the primal-dual viewpoint coherent.

- **Newton's method on the gradient of the Lagrangian** — Newton's method on the full KKT system would update both $x$ and $z$ simultaneously by solving a linear system involving the Hessian of the Lagrangian. The augmented Lagrangian decouples this: minimize $L_\mu$ over $x$ (using Levenberg–Marquardt, which is an *inexact* Newton's method on $\nabla_x L_\mu = 0$); update $z$ by a gradient step. The augmented Lagrangian's $\mu \|g\|^2$ term regularizes the inner $x$-minimization, eliminating the indefinite-Hessian difficulty that direct Newton on the KKT system faces.

---

# Unlocked by This

> [!tip] Saddle Point Theorems and Mini-Max Optimization *(from Game Theory / Optimization)*
> The KKT system is a *saddle point* of the Lagrangian (minimum in $x$, maximum in $z$), and the augmented Lagrangian's success in finding the saddle point illustrates a general principle: many minimax problems are best attacked by alternating minimization and maximization with appropriate regularization. This principle extends to **generative adversarial networks** (where a generator network minimizes and a discriminator network maximizes, with the analogue of $\mu \|g\|^2$ being various forms of gradient penalty), to **robust optimization** (minimize over $x$, maximize over uncertainty $w$, with augmented penalties stabilizing the iteration), and to **two-player zero-sum game-solving** in reinforcement learning. The structural insight is "regularization stabilizes minimax iteration."

> [!tip] Proximal Point Method *(from Convex Optimization)*
> The augmented Lagrangian update $z \leftarrow z + 2\mu g(\tilde x(z))$ is exactly the **proximal point method** applied to the dual function $\phi(z) = -\min_x L_0(x, z)$ (the negative of the ordinary Lagrangian dual). Proximal point: at each iterate, $z^{(k+1)} = \arg\min_z \big( \phi(z) + \tfrac{1}{2\eta} \|z - z^{(k)}\|^2 \big)$. The augmented-Lagrangian step with $\mu$ corresponds to proximal-point step size $\eta = 1/(2\mu)$. So the convergence theory of proximal point methods (geometric convergence under strong convexity, $O(1/k)$ in general) directly gives convergence rates for the augmented Lagrangian algorithm — without any new analysis.
