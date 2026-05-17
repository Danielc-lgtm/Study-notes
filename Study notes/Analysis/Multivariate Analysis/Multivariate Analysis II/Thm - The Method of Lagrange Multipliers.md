---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - Critical Point, Hessian, and Definiteness"
  - "Def - Directional Derivative and the Gradient"
  - "Thm - First-Order Optimality Condition"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open; $f, g_1, \dots, g_k \in C^1(U, \mathbb{R})$. The **constraint set** is
$$M = \{x \in U : g_1(x) = \dots = g_k(x) = 0\}.$$
The **gradient** $\nabla g_j(x)$ is the column vector of partials of $g_j$. A point of $M$ is **regular** if the gradients $\nabla g_1, \dots, \nabla g_k$ are linearly independent there. The numbers $\lambda_1, \dots, \lambda_k$ are **Lagrange multipliers**, and $\lambda_0$ is the multiplier on $f$ itself. The **Lagrangian** is $L(x,\lambda) = f(x) - \sum_j\lambda_j g_j(x)$. The full registry is on [[Multivariate Analysis II — Inverse and Implicit Function Theorems]].

---

# Statement

> **Method of Lagrange multipliers.** Let $U \subseteq \mathbb{R}^n$ be open, $f, g_1, \dots, g_k \in C^1(U, \mathbb{R})$, and let
> $$M = \{x \in U : g_1(x) = \dots = g_k(x) = 0\}.$$
> Suppose $f|_M$ has a local extremum at $x_0 \in M$ — meaning $f(x) \geq f(x_0)$ (or $\leq$) for all $x \in M$ in some ball $B_r(x_0)$. Then there exist real numbers $\lambda_0, \lambda_1, \dots, \lambda_k$, **not all zero**, with
> $$\lambda_0 \nabla f(x_0) + \lambda_1 \nabla g_1(x_0) + \dots + \lambda_k \nabla g_k(x_0) = 0.$$
> Equivalently: the vectors $\nabla f(x_0), \nabla g_1(x_0), \dots, \nabla g_k(x_0)$ are **linearly dependent**.
>
> **Regular case.** If, in addition, $\nabla g_1(x_0), \dots, \nabla g_k(x_0)$ are linearly independent (the point $x_0$ is **regular** for the constraints), then necessarily $\lambda_0 \neq 0$, so one may normalize $\lambda_0 = 1$ and obtain
> $$\nabla f(x_0) = \sum_{j=1}^k \lambda_j \nabla g_j(x_0).$$
> Equivalently, $(x_0, \lambda)$ is a critical point of the Lagrangian $L(x,\lambda) = f(x) - \sum_j\lambda_j g_j(x)$: every partial $\partial_{x_i} L$ and $\partial_{\lambda_j} L$ vanishes.

---

# Motivation

The [[Thm - First-Order Optimality Condition|first-order condition]] $\nabla f = 0$ finds extrema over an *open* set. But the optimization problems that actually arise are almost never over open sets. You want the hottest point on a sphere, the cheapest production plan on a budget constraint, the geodesic on a surface, the closest point of a curve to the origin. In every case the search is over a set $M$ cut out by equations, and on such a set $\nabla f = 0$ is simply the wrong condition.

To see why, walk around the unit circle $x^2 + y^2 = 1$ trying to maximise $f(x,y) = x$. The maximum is at $(1,0)$. But $\nabla f = (1,0)$ there — it is nonzero, indeed it is nonzero *everywhere*. So $\nabla f = 0$ would find no candidates at all and miss the answer entirely. The first-order condition fails because it asks $f$ to be flat in *every* direction, but on the circle you are not allowed to move in every direction — only along the circle. The right demand is that $f$ be flat *in the directions you are allowed to move*, the directions tangent to $M$.

That is the whole idea. At a constrained extremum, the gradient $\nabla f$ — which points in the direction of steepest ascent of $f$ — must have *no component along the constraint set*, or you could increase $f$ by sliding along $M$. So $\nabla f$ must be entirely *perpendicular* to $M$. And the perpendicular space to $M = \{g_j = 0\}$ is spanned by the constraint gradients $\nabla g_j$, because each $\nabla g_j$ points perpendicular to its own level set $\{g_j = \text{const}\}$. Hence $\nabla f$ must be a linear combination of the $\nabla g_j$ — which is exactly the conclusion. The multipliers $\lambda_j$ are the coefficients of that combination, and they carry real meaning: $\lambda_j$ measures how much the optimal value of $f$ would change if the $j$-th constraint were relaxed — its *shadow price*.

The general statement carries an extra subtlety, the multiplier $\lambda_0$ on $f$ itself. In the well-behaved (regular) case $\lambda_0$ can be taken to be $1$ and the conclusion is the clean $\nabla f = \sum\lambda_j\nabla g_j$. But where the constraint gradients are themselves dependent — at corners, cusps, self-crossings of $M$ — the method can fail to constrain $f$ at all, and the honest statement allows $\lambda_0 = 0$. Knowing this failure mode is essential, and it is treated carefully below.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f|_M$ has a local extremum at $x_0$, with $M$ a $C^1$ constraint set". The skill is recognizing constrained extrema.

The first disguised source is **the global extremum of a continuous function on a compact constraint set.** Property $B$: $f$ is continuous on a compact $M$ (a sphere, a torus, a closed level set). The bridge: Weierstrass guarantees the global extremum on $M$ exists; it is in particular a local extremum of $f|_M$, so this theorem applies. The non-obviousness is that you need not assume an extremum — compactness of the constraint set produces one. *Example:* extremising a linear functional on the sphere, which produces the largest and smallest eigenvalues of a quadratic form (see [[Ex - The spectral theorem via constrained optimization]]).

The second disguised source is **a tangency condition between two surfaces.** Property $B$: the level set $\{f = c\}$ and the constraint set $\{g = 0\}$ are tangent at $x_0$. The bridge: at a constrained extremum the value $c = f(x_0)$ is the extreme value, and $\{f = c\}$ touches $M$ without crossing — tangentially — so their normals align, $\nabla f \parallel \nabla g$. This is the geometric face of the theorem. *Example:* finding the point of an ellipse closest to a line — the extremal contour of "distance" is tangent to the ellipse.

The third disguised source is **a constrained minimization that has been penalized.** Property $B$: $x_0$ minimises $f$ on $M$, and one studies the penalized functions $f_\varepsilon(x) = f(x) + \tfrac{1}{2\varepsilon}\sum g_j(x)^2$ on a fixed ball. The bridge: the minimizers $x_\varepsilon$ of $f_\varepsilon$ are *unconstrained* interior extrema, so $\nabla f_\varepsilon(x_\varepsilon) = 0$ by the [[Thm - First-Order Optimality Condition|first-order condition]]; letting $\varepsilon \to 0$ pushes $x_\varepsilon \to x_0$ and the relation $\nabla f_\varepsilon = 0$ limits to the Lagrange relation. This *is* the proof, and recognizing it shows that constrained problems are limits of unconstrained ones. *Example:* the penalty and augmented-Lagrangian methods of numerical optimization.

**Targets (Output Amplification)**

The conclusion is "$\nabla f(x_0)$ lies in the span of the constraint gradients".

Combine the conclusion with **the constraints $g_j(x_0) = 0$ themselves.** Property $D$: the point $x_0$ also satisfies the $k$ constraint equations. The amplified result $E$: a closed system of $n + k$ equations in the $n + k$ unknowns $(x, \lambda)$ — the $n$ stationarity equations $\nabla f = \sum\lambda_j\nabla g_j$ plus the $k$ constraints — whose solutions are the complete candidate list. The combination is what makes the method *operational*: it produces a solvable system, not just a geometric statement.

Combine the conclusion with **compactness of $M$ and a check of non-regular points.** Property $D$: $M$ is compact and you have separately listed its non-regular points. The amplified result $E$: the global constrained extremum is found by evaluating $f$ on the finite list = (Lagrange solutions) $\cup$ (non-regular points). The non-obviousness, stressed throughout this topic, is that the Lagrange equations alone are *incomplete* — the non-regular points are invisible to them and must be added by hand.

Combine the conclusion with **the second derivative of $f$ along the constraint set.** Property $D$: the Hessian of the Lagrangian, restricted to the tangent space $T_{x_0}M$. The amplified result $E$: a second-order test for constrained problems — the bordered-Hessian criterion — which classifies the Lagrange candidate as a constrained minimum, maximum, or saddle, exactly as the [[Thm - Second-Order Optimality Conditions|unconstrained second-order test]] does for critical points.

---

# Why Is It True

There are two complementary intuitions; both are worth carrying.

The **geometric** intuition: imagine standing on the constraint set $M$ and trying to climb $f$. You may only move along $M$. If, at your current point, the gradient $\nabla f$ has *any* component tangent to $M$, then sliding a little in that tangent direction increases $f$ — you are not at a maximum. So at a maximum (or minimum) the gradient $\nabla f$ must have *zero tangential component*: it must be entirely perpendicular to $M$. Now, what is the perpendicular space to $M$? The set $M$ is the common zero set of the $g_j$, and the gradient $\nabla g_j$ always points perpendicular to the level set of $g_j$ — that is the fundamental geometric fact about gradients. The perpendicular space to $M$ at $x_0$ is therefore spanned by $\nabla g_1, \dots, \nabla g_k$ (in the regular case, where these are independent, this span is exactly the $k$-dimensional normal space). For $\nabla f$ to lie in that perpendicular space is for it to be a linear combination $\sum\lambda_j\nabla g_j$. That is the theorem.

The **penalization** intuition, which is also the actual proof: a constrained problem is the limit of unconstrained ones. Instead of forbidding points off $M$, *punish* them — minimise $f_\varepsilon(x) = f(x) + \tfrac{1}{2\varepsilon}\sum_j g_j(x)^2$, which adds a steeply rising cost for violating the constraints, the steepness controlled by $1/\varepsilon$. As $\varepsilon \to 0$ the penalty becomes infinitely steep, the punished minimizer is squeezed onto $M$, and in the limit it must be the constrained minimizer $x_0$. But each $f_\varepsilon$ is being minimised over an open set with *no* constraint, so the ordinary [[Thm - First-Order Optimality Condition|first-order condition]] applies: $\nabla f_\varepsilon = \nabla f + \tfrac{1}{\varepsilon}\sum_j g_j\nabla g_j = 0$. Rename $\lambda_j^\varepsilon = -g_j(x_\varepsilon)/\varepsilon$; the equation reads $\nabla f(x_\varepsilon) = \sum_j\lambda_j^\varepsilon\nabla g_j(x_\varepsilon)$. As $\varepsilon \to 0$ this relation passes to the limit — after normalizing the coefficient vector $(\lambda_0, \dots, \lambda_k)$ to unit length and extracting a convergent subsequence, which is legal because the unit sphere in $\mathbb{R}^{k+1}$ is compact — and produces $\lambda_0\nabla f(x_0) + \sum\lambda_j\nabla g_j(x_0) = 0$. The normalization is exactly why the conclusion comes with a multiplier $\lambda_0$ on $f$ and why the multiplier vector is only determined up to scale.

The penalization picture also explains the $\lambda_0$ subtlety honestly. The limiting multiplier vector is a *unit* vector in $\mathbb{R}^{k+1}$, so it is nonzero — but nothing forces its first coordinate $\lambda_0$ to survive. If at $x_0$ the constraint gradients are linearly dependent, the limit can collapse onto a relation $\sum_j\lambda_j\nabla g_j = 0$ among the constraint gradients alone, with $\lambda_0 = 0$, saying nothing about $f$. That is the non-regular failure mode, built into the theorem's structure.

---

# What Makes This Hard

The non-obvious step is the **normalization and compactness argument**: the multiplier vector must be rescaled to unit length so that a convergent subsequence can be extracted from the unit sphere as $\varepsilon \to 0$, and it is this rescaling that produces the symmetric statement with a multiplier $\lambda_0$ on $f$ itself. The most common error is to *use the clean form $\nabla f = \sum\lambda_j\nabla g_j$ at a non-regular point* — where the constraint gradients are dependent, $\lambda_0$ may be forced to $0$ and the method silently misses the extremum; a second frequent slip is to treat the Lagrange equations as the *complete* candidate list and forget to check the non-regular points of $M$ separately.

---

# Rederivation Scaffold

**High-level strategy:**
Replace the constrained problem by penalized unconstrained problems $f_\varepsilon = f + \tfrac{1}{2\varepsilon}\sum g_j^2$. Minimise each over a fixed ball; the minimizers converge to $x_0$. Apply the unconstrained first-order condition to each, normalize the resulting multiplier vector to the unit sphere, and pass to a convergent subsequence.

**Subgoal decomposition:**

1. **Reduce to a strict minimum.** Replace $f$ by $f(x) + |x - x_0|^2$ so that $x_0$ is the *unique* (strict) local minimizer on $M$ near $x_0$.
   - *Hint:* Adding $|x-x_0|^2$ does not change $\nabla f$ at $x_0$ and makes the minimum strict, which is needed for the convergence in step 3.
   - *Why needed:* Strictness guarantees the penalized minimizers cannot accumulate anywhere but $x_0$.

2. **Penalize and minimise.** For $\varepsilon > 0$, let $x_\varepsilon$ minimise $f_\varepsilon = f + \tfrac{1}{2\varepsilon}\sum g_j^2$ over the compact ball $\overline{B_r(x_0)}$.
   - *Hint:* Weierstrass gives a minimizer; the penalty term punishes constraint violation.
   - *Why needed:* $x_\varepsilon$ is an *unconstrained* extremum, so the easy first-order condition applies to it.

3. **Show $x_\varepsilon \to x_0$.** As $\varepsilon \to 0$, the minimizers converge to $x_0$.
   - *Hint:* From $f_\varepsilon(x_\varepsilon) \leq f_\varepsilon(x_0) = f(x_0)$ deduce $\sum g_j(x_\varepsilon)^2 \leq 2\varepsilon f(x_0) \to 0$, so any accumulation point lies in $M$; strictness from step 1 forces it to be $x_0$.
   - *Why needed:* It anchors the limiting relation at the right point.

4. **Apply the first-order condition and normalize.** Eventually $x_\varepsilon$ is interior, so $\nabla f_\varepsilon(x_\varepsilon) = 0$, giving a dependence among $\nabla f, \nabla g_j$ at $x_\varepsilon$; record it as a *unit* coefficient vector $\lambda^\varepsilon \in S^k$.
   - *Hint:* $\nabla f_\varepsilon = \nabla f + \tfrac1\varepsilon\sum g_j\nabla g_j$; the coefficients $(1, g_1/\varepsilon, \dots, g_k/\varepsilon)$ give a dependence — divide by their norm.
   - *Why needed:* Normalizing puts the coefficient vectors on the compact sphere $S^k$.

5. **Pass to the limit.** Extract a convergent subsequence $\lambda^\varepsilon \to \lambda \in S^k$ and let $\varepsilon \to 0$ in the dependence relation.
   - *Hint:* $S^k$ is compact, so a convergent subsequence exists; gradients are continuous, so the relation survives the limit.
   - *Why needed:* It yields $\lambda_0\nabla f(x_0) + \sum\lambda_j\nabla g_j(x_0) = 0$ with $\lambda \neq 0$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The penalized minimizers converge to the constrained minimizer
> **Statement:** Assume $x_0$ is a strict local minimizer of $f$ on $M \cap \overline{B_r(x_0)}$. Let $x_\varepsilon$ minimise $f_\varepsilon = f + \tfrac{1}{2\varepsilon}\sum g_j^2$ over $\overline{B_r(x_0)}$. Then $x_\varepsilon \to x_0$ as $\varepsilon \to 0$.
>
> **Hint:** Use $f_\varepsilon(x_\varepsilon) \leq f_\varepsilon(x_0) = f(x_0)$ to bound the constraint violation, and strictness to pin the accumulation point.
>
> **Why needed:** It guarantees the limiting Lagrange relation is anchored at the correct point $x_0$.
>
> > [!note]- Full proof
> > By minimality, $f_\varepsilon(x_\varepsilon) \leq f_\varepsilon(x_0)$. Since $x_0 \in M$, all $g_j(x_0) = 0$, so $f_\varepsilon(x_0) = f(x_0)$. Hence
> > $$f(x_\varepsilon) + \tfrac{1}{2\varepsilon}\sum_j g_j(x_\varepsilon)^2 \leq f(x_0).$$
> > As $f$ is continuous on the compact ball it is bounded below, so $\sum_j g_j(x_\varepsilon)^2 \leq 2\varepsilon\big(f(x_0) - \inf f\big) \to 0$. Now $\{x_\varepsilon\}$ lies in the compact ball, so any sequence $\varepsilon_\ell \to 0$ has $x_{\varepsilon_\ell}$ accumulating at some $\bar x$; by the bound just shown $g_j(\bar x) = 0$ for all $j$, so $\bar x \in M \cap \overline{B_r(x_0)}$. Moreover $f(\bar x) \leq \liminf f(x_{\varepsilon_\ell}) \leq \liminf f_{\varepsilon_\ell}(x_{\varepsilon_\ell}) \leq f(x_0)$, and since $x_0$ is the *strict* minimizer on $M \cap \overline{B_r(x_0)}$, this forces $\bar x = x_0$. Every accumulation point is $x_0$, and the sequence is bounded, so $x_\varepsilon \to x_0$.

> [!note]- Lemma 2: A bounded sequence of unit vectors has a convergent subsequence
> **Statement:** Any sequence on the unit sphere $S^k = \{\lambda \in \mathbb{R}^{k+1} : |\lambda| = 1\}$ has a subsequence converging to a point of $S^k$.
>
> **Hint:** $S^k$ is closed and bounded in $\mathbb{R}^{k+1}$, hence compact.
>
> **Why needed:** It legitimizes passing the normalized multiplier relation to the limit, and guarantees the limiting multiplier vector is nonzero (it is a *unit* vector).
>
> > [!note]- Full proof
> > $S^k$ is bounded (every point has norm $1$) and closed (it is the preimage of $\{1\}$ under the continuous map $\lambda \mapsto |\lambda|$). By the Heine–Borel theorem a closed bounded subset of $\mathbb{R}^{k+1}$ is compact, and in a compact metric space every sequence has a convergent subsequence with limit in the set. So a subsequence of any sequence in $S^k$ converges to some $\lambda \in S^k$; in particular $|\lambda| = 1 \neq 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> Assume $f|_M$ has a local minimum at $x_0$ (replace $f$ by $-f$ for a maximum). Choose $r > 0$ with $\overline{B_r(x_0)} \subseteq U$.
>
> **Step 0 — make the minimum strict.** Replace $f$ by $\tilde f(x) = f(x) + |x - x_0|^2$. Then $\nabla\tilde f(x_0) = \nabla f(x_0)$ (the added term has zero gradient at $x_0$), and $x_0$ is now a *strict* local minimizer of $\tilde f|_M$. Proving the relation for $\tilde f$ proves it for $f$. Rename $\tilde f$ as $f$.
>
> **Step 1 — penalize.** For $\varepsilon > 0$ define $f_\varepsilon(x) = f(x) + \tfrac{1}{2\varepsilon}\sum_{j=1}^k g_j(x)^2$ on $\overline{B_r(x_0)}$. By the Weierstrass theorem $f_\varepsilon$ attains a minimum at some $x_\varepsilon \in \overline{B_r(x_0)}$.
>
> **Step 2 — convergence.** By Lemma 1, $x_\varepsilon \to x_0$ as $\varepsilon \to 0$. In particular, for $\varepsilon$ small enough $x_\varepsilon$ lies in the open ball $B_r(x_0)$, hence is an *interior* minimizer of $f_\varepsilon$.
>
> **Step 3 — first-order condition.** Being an interior minimizer of the $C^1$ function $f_\varepsilon$, $x_\varepsilon$ satisfies $\nabla f_\varepsilon(x_\varepsilon) = 0$ by the [[Thm - First-Order Optimality Condition|first-order optimality condition]]. Since $\nabla(g_j^2) = 2g_j\nabla g_j$,
> $$0 = \nabla f_\varepsilon(x_\varepsilon) = \nabla f(x_\varepsilon) + \frac{1}{\varepsilon}\sum_{j=1}^k g_j(x_\varepsilon)\,\nabla g_j(x_\varepsilon).$$
> Thus the $k+1$ vectors $\nabla f(x_\varepsilon), \nabla g_1(x_\varepsilon), \dots, \nabla g_k(x_\varepsilon)$ are linearly dependent: the coefficient vector
> $$\mu^\varepsilon = \Big(1, \tfrac{g_1(x_\varepsilon)}{\varepsilon}, \dots, \tfrac{g_k(x_\varepsilon)}{\varepsilon}\Big) \in \mathbb{R}^{k+1}$$
> is nonzero (its first entry is $1$) and gives $\mu^\varepsilon_0\nabla f(x_\varepsilon) + \sum_j\mu^\varepsilon_j\nabla g_j(x_\varepsilon) = 0$. Normalize: set $\lambda^\varepsilon = \mu^\varepsilon/|\mu^\varepsilon| \in S^k$, so that
> $$\lambda^\varepsilon_0\,\nabla f(x_\varepsilon) + \sum_{j=1}^k\lambda^\varepsilon_j\,\nabla g_j(x_\varepsilon) = 0, \qquad |\lambda^\varepsilon| = 1. \tag{$\dagger$}$$
>
> **Step 4 — pass to the limit.** By Lemma 2, along a subsequence $\varepsilon_\ell \to 0$ the unit vectors $\lambda^{\varepsilon_\ell}$ converge to some $\lambda \in S^k$, so $\lambda \neq 0$. Since $x_{\varepsilon_\ell} \to x_0$ and the gradients $\nabla f, \nabla g_j$ are continuous, taking the limit of ($\dagger$) along this subsequence gives
> $$\lambda_0\,\nabla f(x_0) + \sum_{j=1}^k\lambda_j\,\nabla g_j(x_0) = 0, \qquad (\lambda_0, \dots, \lambda_k) \neq 0.$$
> This is the general statement.
>
> **Regular case.** Suppose $\nabla g_1(x_0), \dots, \nabla g_k(x_0)$ are linearly independent. If $\lambda_0 = 0$ the relation would read $\sum_j\lambda_j\nabla g_j(x_0) = 0$ with the $\lambda_j$ not all zero, contradicting independence. So $\lambda_0 \neq 0$; dividing through by $\lambda_0$ and renaming gives $\nabla f(x_0) = \sum_j\lambda_j\nabla g_j(x_0)$. Setting all partials of $L(x,\lambda) = f - \sum_j\lambda_j g_j$ to zero recovers exactly this equation ($\partial_{x_i}L = 0$) together with the constraints ($\partial_{\lambda_j}L = -g_j = 0$). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Thermodynamics and the principle of maximum entropy.** The equilibrium distribution of a physical system maximises entropy $S$ subject to constraints fixing the total probability and the mean energy. The Lagrange multiplier on the energy constraint is, up to a constant, the *inverse temperature* $\beta = 1/kT$, and the multiplier-derived stationarity equation produces the Boltzmann distribution $e^{-\beta E}$. The application is nonobvious because a multiplier — an abstract algebraic coefficient — turns out to be a measurable physical quantity, temperature.

**The spectral theorem.** Extremising the quadratic form $\langle x, Ax\rangle$ on the unit sphere $\{|x|^2 = 1\}$ produces, via this theorem, the equation $Ax = \lambda x$ — the multiplier $\lambda$ *is* the eigenvalue. Iterating on successive orthogonal complements builds an orthonormal eigenbasis. The application is striking because a theorem of linear algebra falls out of an analysis optimization; this is exactly [[Ex - The spectral theorem via constrained optimization]].

**Economics — utility maximization and shadow prices.** A consumer maximises utility $u(x)$ subject to a budget constraint $p\cdot x = w$. The multiplier on the budget constraint is the *marginal utility of wealth*: it measures exactly how much extra utility one more unit of budget would buy. The application is out-of-distribution because the multiplier, an artefact of the method, is the central economic quantity — a shadow price — and the entire theory of duality in optimization is the systematic study of these multipliers.

---

# Bridges

- **[[Thm - First-Order Optimality Condition]]** — the unconstrained special case ($k = 0$) and the engine of the proof. The penalized problems are unconstrained, and Lagrange's theorem is this first-order condition pushed to a limit.

- **[[Def - The Tangent Space to a Submanifold]]** and **[[Def - Submanifold of Euclidean Space]]** — the geometric home of the theorem. When the constraint set $M$ is a regular submanifold, the Lagrange condition says exactly $\nabla f(x_0) \perp T_{x_0}M$: the gradient is normal to the constraint manifold. This reframing generalizes the method to optimization on abstract manifolds.

- **[[Thm - The Implicit Function Theorem]]** — the alternative proof route. Where the constraints are regular, the implicit function theorem locally writes $M$ as a graph, reducing the constrained problem to an *unconstrained* one in the graph coordinates; differentiating and applying the first-order condition recovers the Lagrange relation.

- **The Karush–Kuhn–Tucker conditions** — the generalization to inequality constraints $g_j \leq 0$. The stationarity equation $\nabla f = \sum\lambda_j\nabla g_j$ survives, augmented by sign conditions on the multipliers and complementary slackness; this is the cornerstone of constrained optimization.

---

# Unlocked by This

> [!tip] Duality and Convex Optimization *(from Optimization Theory)*
> The Lagrangian $L(x,\lambda)$ has a *dual* problem — maximise over $\lambda$ the minimum over $x$. For convex problems strong duality holds: the primal and dual optimal values coincide, and the optimal multipliers are the **shadow prices**. The entire theory of convex duality grows from the Lagrangian introduced here.

> [!tip] Geodesics and the Calculus of Variations *(from Differential Geometry)*
> Constrained optimization over an infinite-dimensional space of curves — minimise length subject to lying on a surface — produces the **geodesic equation** by an infinite-dimensional analogue of this theorem. The multipliers become the *normal force* keeping the curve on the surface.
