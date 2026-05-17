---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - Critical Point, Hessian, and Definiteness"
  - "Def - Directional Derivative and the Gradient"
  - "Def - Partial Derivatives and the Jacobian Matrix"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open and $f : U \to \mathbb{R}$ is real-valued. A point $x_0 \in U$ is a **local maximum** if $f(x) \leq f(x_0)$ for all $x$ in some ball $B_r(x_0)$, a **local minimum** if $f(x) \geq f(x_0)$ on such a ball, and a **local extremum** if it is one or the other. The maximum or minimum is **strict** (or **isolated**) if the inequality is strict for $x \neq x_0$. The **gradient** is $\nabla f(x) = (\partial_1 f(x), \dots, \partial_n f(x))^T$, $e_i$ is the $i$-th standard basis vector, and a **critical point** is one where $\nabla f = 0$. The full registry is on [[Multivariate Analysis II — Inverse and Implicit Function Theorems]].

---

# Statement

> **First-order optimality condition.** Let $U \subseteq \mathbb{R}^n$ be open and $f : U \to \mathbb{R}$. If $f$ is differentiable at an interior point $x_0 \in U$ and has a local extremum at $x_0$, then
> $$\nabla f(x_0) = 0,$$
> that is, $\partial_i f(x_0) = 0$ for every $i \in \{1, \dots, n\}$ — equivalently, the total derivative $Df_{x_0}$ is the zero map and $x_0$ is a [[Def - Critical Point, Hessian, and Definiteness|critical point]] of $f$.

---

# Motivation

In one variable, the search for the maximum of $f$ begins by solving $f'(x) = 0$. The reason this is the right move is sharp: if $f'(x_0) \neq 0$, then $f$ is strictly monotone through $x_0$, so $x_0$ is beaten on one side and beats the other — it cannot be an extremum. The extrema are trapped among the finitely many roots of $f'$, plus the endpoints.

This theorem is the multivariable version, and it answers the question: in $\mathbb{R}^n$, what equation traps the extrema? The naive guess — set each partial derivative to zero — turns out to be exactly right, but it deserves an argument, because in several variables "the function is not monotone here" is no longer a single statement; the function could be climbing in one direction and falling in another. The theorem says that at a genuine extremum *every* direction must be first-order flat, and the clean way to encode that is $\nabla f(x_0) = 0$.

The value of the theorem is that it converts an optimization problem — find the largest value of $f$, a search over a continuum — into an *algebra problem*: solve the system of $n$ equations $\partial_1 f = \dots = \partial_n f = 0$. The solutions are the only candidates, and there are usually only finitely many. The word **interior** in the statement is not a technicality to be glossed: the conclusion can fail at boundary points, and recognizing this is what forces the separate treatment of boundaries (and, downstream, the method of [[Thm - The Method of Lagrange Multipliers|Lagrange multipliers]] for extrema on constraint sets).

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f$ has an interior local extremum at $x_0$ and is differentiable there". The skill is recognizing situations that supply this without saying the word "extremum".

The first disguised source is **a global extremum of a continuous function on a compact set, located in the interior.** Property $B$: $f$ is continuous on a compact $K$, and the point $x_0$ achieving $\max_K f$ happens to lie in the interior of $K$. The bridge: by the Weierstrass theorem the global maximum *exists*, and a global maximum is in particular a local one; if it is interior, the theorem applies. The non-obviousness is that you do not need to assume an extremum — compactness *manufactures* one for you. *Example:* to find the largest value of $f$ on a closed ball, the candidates are the interior critical points (this theorem) together with the boundary points (handled by Lagrange multipliers).

The second disguised source is **a point where one function dominates or is dominated by another, with equality.** Property $B$: $g(x) \leq f(x)$ everywhere, with $g(x_0) = f(x_0)$, and both are differentiable. The bridge: the difference $f - g$ has a local minimum (value $0$) at $x_0$, so $\nabla(f-g)(x_0) = 0$, hence $\nabla f(x_0) = \nabla g(x_0)$ — two graphs that touch tangentially have equal gradients. This is the principle behind tangency arguments and behind the proof of [[Thm - The Method of Lagrange Multipliers|Lagrange's theorem]] via penalization. *Example:* showing that a supporting hyperplane of a convex function touches the graph with matching slope.

The third disguised source is **a fixed point of a gradient flow or the limit of a descent algorithm.** Property $B$: $x_0$ is a point that a gradient-descent iteration $x_{k+1} = x_k - t\nabla f(x_k)$ has converged to. The bridge: a limit of gradient descent with $\nabla f$ continuous must have $\nabla f(x_0) = 0$, so it is a critical point and a *candidate* extremum. *Example:* in optimization and machine learning, the output of a descent method is certified only as a critical point — this theorem is the converse caution.

**Targets (Output Amplification)**

The conclusion is "$\nabla f(x_0) = 0$" — $x_0$ is a critical point.

Combine the conclusion with **the second-order Taylor expansion.** Property $D$: $f$ is $C^2$, so near $x_0$ one has $f(x_0+h) = f(x_0) + \nabla f(x_0)\cdot h + \tfrac12 h^T Hf(x_0) h + o(|h|^2)$. With $\nabla f(x_0) = 0$ from this theorem, the first-order term *vanishes*, and the local behaviour of $f$ is governed entirely by the quadratic form $h^T Hf(x_0) h$. The amplified result $E$ is the entire [[Thm - Second-Order Optimality Conditions|second-order test]]: it is meaningful *only at critical points*, and this theorem is what certifies the first-order term is gone.

Combine the conclusion with **the finiteness of the solution set of a polynomial system.** Property $D$: $f$ is a polynomial, so $\nabla f = 0$ is a polynomial system; generically it has finitely many solutions. The amplified result $E$: the extrema of a polynomial $f$ on an open set form a *finite* explicit list, computable by algebra. The non-obvious payoff is that an analytic optimization problem becomes a finite algebraic one.

Combine the conclusion with **compactness of the domain.** Property $D$: $f$ is continuous on a compact set $K$. The amplified result $E$: the global maximum and minimum of $f$ are *guaranteed to exist* and to lie in the finite candidate list = (interior critical points from this theorem) $\cup$ (boundary candidates). Comparing $f$ on this finite list *solves* the optimization problem completely. This is the routine that every compact-domain optimization follows.

---

# Why Is It True

Picture the surface $z = f(x)$ above $\mathbb{R}^n$, and suppose $x_0$ is a local minimum — the surface has a valley bottom at $x_0$. Now slice the surface with the vertical plane containing the $x_i$-axis. The slice is the graph of the one-variable function $t \mapsto f(x_0 + t e_i)$, and because $x_0$ is a valley bottom of the whole surface, it is in particular a valley bottom of every slice. But for a one-variable function, a differentiable function cannot have a valley bottom in the interior with a nonzero derivative — a nonzero derivative means the function is sloping, so it is lower on one side. So the slice's derivative at $t = 0$ is zero. That derivative is exactly the partial derivative $\partial_i f(x_0)$. Doing this for every coordinate axis $i$ kills every partial, and $\nabla f(x_0) = 0$.

The single idea is **reduction to one variable by slicing**. An extremum in $\mathbb{R}^n$ is, when restricted to any line through $x_0$, an extremum in one variable — extremality is inherited by restriction, because "lower than all nearby points in $\mathbb{R}^n$" certainly implies "lower than all nearby points on this line". So the multivariable statement is just the one-variable statement applied $n$ times, once per coordinate direction. There is genuinely nothing more to it: the theorem looks like a several-variable fact but it is the one-variable fact wearing $n$ hats.

It is worth being clear about *why interior* is needed. The one-variable fact "extremum implies zero derivative" itself needs an interior point — at an endpoint of an interval, a minimum can have nonzero (one-sided) derivative, as $f(t) = t$ on $[0,1]$ shows at $t = 0$. The slicing argument inherits this: you need to be able to move a *little in both directions* along each axis and stay in the domain, and that is exactly what "interior point of the open set $U$" guarantees.

One should expect the theorem to be true because optimization is fundamentally about *exhausting the first-order freedom*. At a non-critical point you have a direction — the gradient direction — in which $f$ provably increases and the opposite in which it provably decreases; you are not yet at an extremum because you have somewhere to go. Only when the gradient vanishes is all first-order freedom spent. The theorem is the formal statement that an extremum is a place where you have run out of downhill.

---

# What Makes This Hard

The theorem itself is not hard — the difficulty is entirely in *not over-trusting it*. The non-obvious content is what the theorem does *not* say: it gives a necessary, not sufficient, condition, so a critical point may be a saddle; and it requires the extremum to be **interior**, so on a domain with boundary the extremum may sit on the boundary with $\nabla f \neq 0$. The most common error is to solve $\nabla f = 0$, find the candidates, and forget either to classify them (a critical point need not be an extremum) or to separately search the boundary (where this theorem is silent).

---

# Rederivation Scaffold

**High-level strategy:**
Restrict $f$ to each coordinate line through $x_0$, obtaining $n$ one-variable functions. Each inherits the extremum at the base point. Apply the one-variable interior-extremum theorem to each, killing one partial derivative at a time.

**Subgoal decomposition:**

1. **Reduce to one variable.** For each $i$, define $\varphi_i(t) = f(x_0 + t e_i)$ on a small interval around $t = 0$.
   - *Hint:* $x_0$ is interior to the open set $U$, so $x_0 + te_i \in U$ for $|t|$ small, and $\varphi_i$ is well-defined and differentiable with $\varphi_i'(0) = \partial_i f(x_0)$.
   - *Why needed:* It converts the $n$-variable problem into $n$ one-variable problems.

2. **Transfer the extremum.** Show $\varphi_i$ has a local extremum at $t = 0$.
   - *Hint:* If $f(x) \geq f(x_0)$ for $x$ near $x_0$ in $\mathbb{R}^n$, then in particular $f(x_0 + te_i) \geq f(x_0)$, i.e. $\varphi_i(t) \geq \varphi_i(0)$.
   - *Why needed:* Extremality must be inherited by the slice for the one-variable theorem to apply.

3. **Apply the one-variable result.** Conclude $\varphi_i'(0) = 0$ for each $i$.
   - *Hint:* A differentiable one-variable function with an interior local extremum has vanishing derivative there — examine the one-sided difference quotients, which have opposite-signed limits.
   - *Why needed:* $\varphi_i'(0) = \partial_i f(x_0)$, so this kills the $i$-th partial.

4. **Assemble.** All partials vanish, so $\nabla f(x_0) = 0$.
   - *Hint:* The gradient is the vector of partials.
   - *Why needed:* It is the statement of the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: A differentiable one-variable function has zero derivative at an interior extremum
> **Statement:** If $\varphi : (-\delta, \delta) \to \mathbb{R}$ is differentiable and has a local extremum at $0$, then $\varphi'(0) = 0$.
>
> **Hint:** Examine the difference quotient $(\varphi(h) - \varphi(0))/h$ as $h \to 0^+$ and as $h \to 0^-$ separately; the sign of the numerator is fixed but the sign of the denominator flips.
>
> **Why needed:** It is the one-variable engine; the whole proof is this lemma applied along each axis.
>
> > [!note]- Full proof
> > Suppose $0$ is a local minimum, so $\varphi(h) \geq \varphi(0)$ for $|h|$ small. For $h > 0$ small, $\frac{\varphi(h)-\varphi(0)}{h} \geq 0$, and letting $h \to 0^+$ gives $\varphi'(0) \geq 0$. For $h < 0$ small, $\frac{\varphi(h)-\varphi(0)}{h} \leq 0$ (non-negative numerator, negative denominator), and letting $h \to 0^-$ gives $\varphi'(0) \leq 0$. Since $\varphi$ is differentiable, the two one-sided limits both equal $\varphi'(0)$, so $\varphi'(0) \geq 0$ and $\varphi'(0) \leq 0$, forcing $\varphi'(0) = 0$. The local-maximum case is identical with inequalities reversed (or apply the result to $-\varphi$).

> [!note]- Lemma 2: The slice derivative is the partial derivative
> **Statement:** If $f$ is differentiable at $x_0$ and $\varphi_i(t) = f(x_0 + te_i)$, then $\varphi_i$ is differentiable at $0$ with $\varphi_i'(0) = \partial_i f(x_0)$.
>
> **Hint:** This is the definition of the partial derivative $\partial_i f$, read as the derivative of $f$ along the $i$-th coordinate line.
>
> **Why needed:** It identifies what Lemma 1 produces ($\varphi_i'(0) = 0$) with the quantity the theorem is about ($\partial_i f(x_0) = 0$).
>
> > [!note]- Full proof
> > By definition, $\partial_i f(x_0) = \lim_{t\to 0} \frac{f(x_0 + te_i) - f(x_0)}{t} = \lim_{t\to 0}\frac{\varphi_i(t) - \varphi_i(0)}{t}$, which is precisely $\varphi_i'(0)$. (Differentiability of $f$ at $x_0$ guarantees this limit exists; in fact mere existence of the partial derivative suffices for this lemma. The composition $t \mapsto x_0 + te_i$ is well-defined into $U$ for small $t$ because $U$ is open and $x_0 \in U$.)

---

# Formal Proof

> [!note]- Complete formal proof
> Let $x_0 \in U$ be an interior local extremum of $f$, with $f$ differentiable at $x_0$. Without loss of generality assume it is a local minimum (otherwise replace $f$ by $-f$). Fix $i \in \{1, \dots, n\}$.
>
> Since $U$ is open and $x_0 \in U$, there is $\delta > 0$ with $B_\delta(x_0) \subseteq U$; in particular $x_0 + te_i \in U$ for $|t| < \delta$. Define
> $$\varphi_i : (-\delta, \delta) \to \mathbb{R}, \qquad \varphi_i(t) = f(x_0 + te_i).$$
> By Lemma 2, $\varphi_i$ is differentiable at $0$ with $\varphi_i'(0) = \partial_i f(x_0)$.
>
> Because $x_0$ is a local minimum of $f$, there is $r > 0$ with $f(x) \geq f(x_0)$ for all $x \in B_r(x_0)$. For $|t| < \min(\delta, r)$ the point $x_0 + te_i$ lies in $B_r(x_0)$, so
> $$\varphi_i(t) = f(x_0 + te_i) \geq f(x_0) = \varphi_i(0).$$
> Thus $\varphi_i$ has a local minimum at $0$. By Lemma 1, $\varphi_i'(0) = 0$, hence $\partial_i f(x_0) = 0$.
>
> Since $i$ was arbitrary, $\partial_i f(x_0) = 0$ for all $i \in \{1, \dots, n\}$, that is, $\nabla f(x_0) = 0$. Equivalently the total derivative $Df_{x_0}$, whose matrix is the row $\nabla f(x_0)^T$, is the zero map, so $x_0$ is a critical point of $f$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Best approximation and orthogonality.** To find the point of a subspace $V \subseteq \mathbb{R}^n$ closest to a given $b$, minimise $f(v) = |b - v|^2$ over $V$. Parametrizing $V$ and setting the gradient to zero yields exactly the *normal equations* — the condition that the residual $b - v$ is orthogonal to $V$. The application is nonobvious because a purely geometric fact (orthogonal projection) emerges as a first-order optimality condition; the gradient vanishing *is* the orthogonality.

**Equilibria of physical systems.** A mechanical system rests at an equilibrium of its potential energy $V$, and equilibria are exactly the critical points $\nabla V = 0$. This theorem is the statement that a system at rest experiences no net force — force being $-\nabla V$. It battle-tests the theorem in a setting where "extremum" is replaced by "equilibrium" and the gradient is a physical force field.

**Maximum likelihood estimation.** The maximum-likelihood estimate of a parameter $\theta$ maximises the log-likelihood $\ell(\theta)$, and the theorem says the estimate satisfies the *score equation* $\nabla\ell(\hat\theta) = 0$. The application is out-of-distribution because the "function" is built from random data, yet the first-order condition is the workhorse derivation of nearly every estimator in statistics.

---

# Bridges

- **[[Thm - Second-Order Optimality Conditions]]** — the direct sequel. This theorem produces the candidate list (critical points); the second-order conditions classify each candidate using the Hessian. The two are always used together.

- **[[Thm - The Method of Lagrange Multipliers]]** — the generalization to constrained domains. When the extremum lies on a constraint surface rather than in an open set, $\nabla f = 0$ is replaced by $\nabla f \in \operatorname{span}\{\nabla g_j\}$. Lagrange's theorem reduces *to* this theorem: it is this first-order condition for the penalized or restricted function.

- **The one-variable interior extremum theorem (Fermat's theorem)** — the special case $n = 1$, and literally the engine of the proof. The multivariable statement is the one-variable statement applied along each coordinate axis.

- **[[Def - Critical Point, Hessian, and Definiteness]]** — this theorem is the reason the notion of "critical point" is defined: critical points are exactly the candidates for interior extrema.

---

# Unlocked by This

> [!tip] Gradient Descent and First-Order Methods *(from Optimization)*
> Because extrema satisfy $\nabla f = 0$, one searches for them by *flowing against the gradient*: the iteration $x_{k+1} = x_k - t\nabla f(x_k)$ decreases $f$ and its fixed points are exactly the critical points. **Gradient descent** and its many refinements are the algorithmic counterpart of this theorem.
