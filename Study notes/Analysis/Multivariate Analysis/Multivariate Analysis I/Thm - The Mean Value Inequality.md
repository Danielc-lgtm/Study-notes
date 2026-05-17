---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - The Total Derivative and Differentiability"
  - "Def - Directional Derivative and the Gradient"
  - "Thm - The Chain Rule"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open; $f : U \to \mathbb{R}^m$; $x_\circ, x, y \in U$; $h \in \mathbb{R}^n$. The total derivative is $Df_\xi : \mathbb{R}^n \to \mathbb{R}^m$ (see [[Def - The Total Derivative and Differentiability]]); $\|Df_\xi\|$ is its operator norm, the smallest constant with $|Df_\xi(v)| \le \|Df_\xi\|\,|v|$. The segment from $x$ to $y$ is $\{(1-t)x + ty : t\in[0,1]\}$; a set is **convex** if it contains the segment between any two of its points. The directional derivative is $\partial_h f$ (see [[Def - Directional Derivative and the Gradient]]). The full symbol registry is on [[Multivariate Analysis I — Differentiation in Several Variables]].

---

# Statement

> **The Mean Value Theorem and Inequality.**
>
> *(Scalar mean value equality.)* Let $U \subseteq \mathbb{R}^n$ be open and $f : U \to \mathbb{R}$ differentiable. If $x_\circ$ and $x_\circ + h$ lie in $U$ together with the whole segment joining them, then there exists $t \in (0,1)$ such that, with $\xi = x_\circ + th$,
> $$f(x_\circ + h) - f(x_\circ) = Df_\xi(h) = \partial_h f(\xi).$$
>
> *(Vector mean value inequality.)* Let $f : U \to \mathbb{R}^m$ be differentiable and let the segment from $x$ to $y$ lie in $U$. Then
> $$|f(x) - f(y)| \;\le\; \Big(\sup_{\xi \in [x,y]} \|Df_\xi\|\Big)\,|x - y|.$$
> In particular, if $U$ is convex and $\|Df_\xi\| \le M$ for all $\xi \in U$, then $f$ is **$M$-Lipschitz**: $|f(x) - f(y)| \le M|x-y|$ for all $x, y \in U$. Two corollaries: a $C^1$ map is **locally Lipschitz**; and if $Df \equiv 0$ on an open *connected* set, then $f$ is **constant**.

---

# Motivation

The one-variable mean value theorem says $f(b) - f(a) = f'(\xi)(b - a)$ for some intermediate $\xi$: the increment of $f$ is captured *exactly* by the derivative at a single well-chosen point. It is the bridge from the derivative back to the function — derivatives are local, increments are global, and the mean value theorem is what connects them. Almost every estimate in one-variable analysis routes through it. The question this topic must answer is: what survives in several variables?

The answer comes in two halves, and the split is itself the lesson. For a *scalar-valued* function the theorem survives intact, as an exact equality, because the proof restricts $f$ to the segment from $x_\circ$ to $x_\circ + h$ — producing a one-variable function — and applies the one-variable theorem. There is one scalar function, one intermediate point.

For a *vector-valued* function the exact equality is genuinely **lost**, and no amount of cleverness recovers it. Applying the scalar result to each component is no help: each component $f_j$ supplies its own intermediate point $\xi_j$, and there is in general no single $\xi$ serving all $m$ components at once. The starkest witness is a closed curve: $\gamma(t) = (\cos 2\pi t, \sin 2\pi t)$ returns to its start, so $\gamma(1) - \gamma(0) = 0$, while the velocity $\gamma'(t)$ is never zero — no intermediate point can make $0 = \gamma'(\xi)\cdot 1$. A mean value *equality* for vector outputs is simply false.

What survives — and it is enough — is the **inequality**: the size of the increment is bounded by the largest size of the derivative along the segment, times the distance. The inequality survives precisely because it is one-sided. An upper bound does not need a single magic point; it only needs to dominate every component simultaneously, and a supremum does that. This is a recurring phenomenon in analysis: when an exact identity fails in a more general setting, the salvageable remnant is the corresponding inequality, and the inequality is usually all the applications ever needed. Dieudonné built his treatise on the inequality alone, discarding the equality as a luxury.

The inequality is the workhorse. It converts knowledge of the *derivative* into knowledge of the *function*: bound $Df$ and you have bounded how fast $f$ can change. From it: a function with bounded derivative is Lipschitz; a $C^1$ function is locally Lipschitz (the derivative, being continuous, is bounded on small balls); and — taking the bound to be zero — a function with vanishing derivative on a connected set is constant. That last corollary is the multivariate "$f' = 0 \Rightarrow f$ constant", and it is the basis of every uniqueness argument that says "two solutions with the same derivative agree".

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition for the inequality is "$f$ differentiable, with $\|Df\|$ bounded by $M$ along the relevant segment".

The first disguised source is **$f$ is $C^1$ on a set whose closure is compact**. The property $B$ is "$f \in C^1(U)$ and we work inside a compact $K \subseteq U$". The bridge is that $Df$ is continuous (this is what $C^1$ means, via [[Thm - Continuous Partials Imply Differentiability]]), and a continuous function on a compact set is bounded — so $\sup_K\|Df\| < \infty$ automatically. The implication is nonobvious in that "is the derivative bounded?" is silently answered by compactness. *Example problem:* show any $C^1$ map is Lipschitz on every closed ball inside its domain.

The second disguised source is **$f$ has a derivative given by an explicit formula one can bound by hand**. The property $B$ is "$Jf$ is an explicit matrix expression". The bridge is direct estimation of the operator norm from the entries. *Example problem:* show a contraction-type map $|Df| \le \tfrac12$ everywhere is genuinely a contraction in the metric sense.

The third disguised source is **$Df \equiv 0$**. The property $B$ is "the derivative vanishes identically on $U$". The bridge is the inequality with $M = 0$. The nonobvious payoff is the *constancy* corollary, and the subtlety that it needs $U$ connected. *Example problem:* two antiderivatives of the same vector field on a connected domain differ by a constant.

**Targets (Output Amplification)**

The conclusion is the bound $|f(x) - f(y)| \le M|x-y|$.

Combine the conclusion with **a contraction constant $M < 1$**. If $f : U \to U$ satisfies $\|Df\| \le M < 1$ on a convex $U$, the inequality makes $f$ a contraction, $|f(x)-f(y)| \le M|x-y|$ with $M < 1$. The further result $E$ is that the contraction mapping principle applies, so $f$ has a unique fixed point. This is the engine of the inverse function theorem (**Multivariate Analysis II**), and the combination is nonobvious because a derivative bound is being converted into the metric hypothesis of a fixed-point theorem.

Combine the conclusion with **the completeness of $\mathbb{R}^m$**. If a sequence $x_k$ is Cauchy and $f$ has bounded derivative, then $f(x_k)$ is Cauchy too ($|f(x_k) - f(x_\ell)| \le M|x_k - x_\ell|$), hence convergent. The further result $E$ is that bounded-derivative maps preserve Cauchy sequences and convergence — the basis of stability and continuous-dependence arguments.

Combine the conclusion with **bound $M = 0$ on a connected domain**. The further result $E$ is the constancy theorem, and through it every *uniqueness* statement of the form "two objects with the same derivative coincide": uniqueness of antiderivatives, of solutions to differential equations with matching data, of harmonic functions with matching gradient. The combination is the most-used target of all.

---

# Why Is It True

Take the two halves separately, because they are true for different reasons.

**The scalar equality.** The idea is the universal move of the topic: a multivariate problem along a straight path is a one-variable problem. The increment $f(x_\circ + h) - f(x_\circ)$ only involves the values of $f$ on the segment joining the two endpoints. So forget the rest of the domain and look only at the segment. Parametrise it by $\varphi(t) = f(x_\circ + th)$, $t \in [0,1]$ — an honest function of one real variable. The increment of $f$ is $\varphi(1) - \varphi(0)$, and the one-variable mean value theorem says this equals $\varphi'(t)$ for some intermediate $t$. The chain rule computes $\varphi'(t) = Df_{x_\circ + th}(h)$. So the multivariate equality is the one-variable equality wearing a coordinate disguise: there *is* a single intermediate point because there is a single scalar function $\varphi$ on the segment.

**Why the equality fails for vectors, and the inequality is what is left.** Run the same argument on a vector-valued $f$: each component $f_j$ gives a one-variable function $\varphi_j$, and the one-variable theorem gives each $\varphi_j$ its own intermediate point. To get a *vector* equality you would need all $m$ of these intermediate points to coincide, and nothing forces that. The closed curve $\gamma(t) = (\cos 2\pi t, \sin 2\pi t)$ shows the failure is real, not a defect of the argument: $\gamma$ returns to its start so the increment is zero, but the velocity is never zero, so no intermediate point can reproduce the increment as $\gamma'(\xi)$.

The inequality survives because an *upper bound* does not need a single point. Here is the picture. The increment $f(x) - f(y)$ is, by the fundamental theorem of calculus applied along the segment, the integral of the velocity $Df$ along the path: $f(x) - f(y) = \int_0^1 Df_{(1-t)y + tx}(x - y)\,dt$. An integral of a vector-valued thing has norm at most the integral of the norms — the triangle inequality for integrals. Each $|Df_\xi(x-y)|$ is at most $\|Df_\xi\|\,|x-y| \le M|x-y|$. Integrating the constant bound $M|x-y|$ over $t \in [0,1]$ gives exactly $M|x-y|$. So $|f(x) - f(y)| \le M|x-y|$. Notice what made this work: the inequality $|\int| \le \int|\cdot|$ is exactly the place where the requirement of "one magic point" is dropped. We never asked for a $\xi$ achieving the increment; we only asked for a $\xi$-independent bound, and the supremum supplies one.

**Why convexity matters.** Both arguments parametrise the *straight segment* from $y$ to $x$ and integrate along it. If that segment leaves the domain, there is no function to integrate — $f$ is not even defined off $U$. Convexity is exactly the guarantee that the segment stays inside. On a non-convex domain the bound can fail outright: on a slit plane a function can have a tiny bounded derivative everywhere yet take very different values on the two lips of the slit, because the only paths connecting them are long. The straight segment is not optional; it is the path the proof integrates over.

---

# What Makes This Hard

The conceptual difficulty is not the proof but knowing **which form is legal**: for a vector-valued function the mean value *equality* is false, and the temptation to apply it componentwise — collecting a single intermediate point — is the standard error, because each component supplies its own point and they need not agree. The non-obvious structural fact is that the inequality survives exactly because it is one-sided: replacing "achieve the increment at a point" by "bound the increment by a supremum" is what removes the need for a common point. A second frequent slip is forgetting the **convexity** (or segment-containment) hypothesis: the proof integrates along the straight segment, so on a non-convex domain the conclusion can be false, and the salvage is to chain the inequality along a polygonal path, picking up the path length instead of $|x-y|$.

---

# Rederivation Scaffold

**High-level strategy:**
Restrict $f$ to the straight segment between the two points, turning the problem one-dimensional. For a scalar $f$, apply the one-variable mean value theorem to get an equality. For a vector $f$, write the increment as the integral of $Df$ along the segment (fundamental theorem of calculus) and bound the integral by the integral of the norm.

**Subgoal decomposition:**

1. **Parametrise the segment.** Set $\varphi(t) = f((1-t)y + tx)$ for $t \in [0,1]$, a function $[0,1] \to \mathbb{R}^m$.
   - *Hint:* The segment lies in $U$ by convexity (or hypothesis), so $\varphi$ is defined.
   - *Why needed:* It converts the multivariate increment into a one-variable problem.

2. **Differentiate via the chain rule.** Show $\varphi'(t) = Df_{(1-t)y+tx}(x - y)$.
   - *Hint:* $\varphi = f\circ\gamma$ with $\gamma(t) = (1-t)y + tx$, $\gamma'(t) = x - y$; apply [[Thm - The Chain Rule]].
   - *Why needed:* It expresses the segment-velocity through the total derivative.

3. **Scalar case — one-variable mean value theorem.** For $m = 1$, get $t\in(0,1)$ with $\varphi(1) - \varphi(0) = \varphi'(t)$.
   - *Hint:* This is the one-variable mean value theorem applied to $\varphi$.
   - *Why needed:* It yields the exact scalar equality $f(x) - f(y) = Df_\xi(x-y)$.

4. **Vector case — integrate and bound.** For general $m$, write $f(x) - f(y) = \int_0^1\varphi'(t)\,dt$ and bound by $\int_0^1|\varphi'(t)|\,dt \le M|x-y|$.
   - *Hint:* Fundamental theorem of calculus, then $|\int| \le \int|\cdot|$, then $|\varphi'(t)| = |Df_\xi(x-y)| \le \|Df_\xi\|\,|x-y| \le M|x-y|$.
   - *Why needed:* It yields the inequality, the only form valid for vector outputs.

5. **Corollaries.** Local Lipschitz: on a small ball $\overline{B}$, $Df$ is continuous hence bounded; the ball is convex, apply the inequality. Constancy: $M = 0$ gives $f$ constant on every ball; connectedness propagates this across $U$.
   - *Hint:* For constancy, the set $\{f = f(x_\circ)\}$ is open and closed in connected $U$.
   - *Why needed:* These are the standard applications and they use the topological hypotheses essentially.

---

# Lemma Decomposition

> [!note]- Lemma 1: Restriction to the segment and its derivative
> **Statement:** Let the segment from $y$ to $x$ lie in $U$ and $f$ be differentiable on $U$. Then $\varphi(t) = f((1-t)y + tx)$ is differentiable on $[0,1]$ with $\varphi'(t) = Df_{(1-t)y+tx}(x-y)$.
>
> **Hint:** $\varphi = f\circ\gamma$ with $\gamma$ the affine parametrisation; apply the chain rule.
>
> **Why needed:** It is the reduction to one variable that both halves of the theorem rest on.
>
> > [!note]- Full proof
> > Let $\gamma : [0,1] \to U$, $\gamma(t) = (1-t)y + tx = y + t(x-y)$, an affine curve; it lands in $U$ because the segment lies in $U$. Its derivative is the constant velocity $\gamma'(t) = x - y$. By [[Thm - The Chain Rule]], the composite $\varphi = f\circ\gamma$ is differentiable with $\varphi'(t) = Df_{\gamma(t)}\big(\gamma'(t)\big) = Df_{(1-t)y+tx}(x-y)$.

> [!note]- Lemma 2: The increment as an integral of the derivative
> **Statement:** For differentiable $f$ with the segment from $y$ to $x$ in $U$, $f(x) - f(y) = \displaystyle\int_0^1 Df_{(1-t)y+tx}(x-y)\,dt$.
>
> **Hint:** Apply the fundamental theorem of calculus to $\varphi$ componentwise.
>
> **Why needed:** It is the exact representation of the increment that the vector inequality bounds.
>
> > [!note]- Full proof
> > By Lemma 1, $\varphi(t) = f((1-t)y+tx)$ is differentiable with the stated $\varphi'$; assume $f \in C^1$ so $\varphi'$ is continuous and the fundamental theorem of calculus applies to each component $\varphi_j$: $\varphi_j(1) - \varphi_j(0) = \int_0^1\varphi_j'(t)\,dt$. Assembling the $m$ components, $\varphi(1) - \varphi(0) = \int_0^1\varphi'(t)\,dt$. Since $\varphi(1) = f(x)$, $\varphi(0) = f(y)$, and $\varphi'(t) = Df_{(1-t)y+tx}(x-y)$, this is the claim.

> [!note]- Lemma 3: Norm of a vector integral is bounded by the integral of the norm
> **Statement:** For continuous $u : [0,1] \to \mathbb{R}^m$, $\big|\int_0^1 u(t)\,dt\big| \le \int_0^1|u(t)|\,dt$.
>
> **Hint:** Let $w = \int_0^1 u\,dt$; bound $|w|^2 = w\cdot\int u\,dt = \int (w\cdot u)\,dt$ using Cauchy–Schwarz.
>
> **Why needed:** It is the precise step where the demand for a single intermediate point is dropped — it turns the exact integral representation into a bound.
>
> > [!note]- Full proof
> > Let $w = \int_0^1 u(t)\,dt \in \mathbb{R}^m$. If $w = 0$ the inequality is trivial. Otherwise, $|w|^2 = w\cdot w = w\cdot\int_0^1 u(t)\,dt = \int_0^1 (w\cdot u(t))\,dt$, by linearity of the integral and of the dot product. By Cauchy–Schwarz, $w\cdot u(t) \le |w|\,|u(t)|$, so $|w|^2 \le \int_0^1 |w|\,|u(t)|\,dt = |w|\int_0^1|u(t)|\,dt$. Dividing by $|w| > 0$ gives $|w| \le \int_0^1|u(t)|\,dt$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Scalar equality.** Let $f : U \to \mathbb{R}$ be differentiable and let the segment from $x_\circ$ to $x_\circ + h$ lie in $U$. By Lemma 1, $\varphi(t) = f(x_\circ + th)$ is differentiable on $[0,1]$ with $\varphi'(t) = Df_{x_\circ+th}(h)$. By the one-variable mean value theorem there is $t\in(0,1)$ with $\varphi(1) - \varphi(0) = \varphi'(t)$, i.e. $f(x_\circ + h) - f(x_\circ) = Df_{x_\circ+th}(h) = \partial_h f(\xi)$ with $\xi = x_\circ + th$.
>
> **Vector inequality.** Let $f : U \to \mathbb{R}^m$ be differentiable with the segment from $y$ to $x$ in $U$, and put $M = \sup_{\xi\in[x,y]}\|Df_\xi\|$. By Lemma 2,
> $$f(x) - f(y) = \int_0^1 Df_{(1-t)y+tx}(x-y)\,dt.$$
> Set $u(t) = Df_{(1-t)y+tx}(x-y)$. By Lemma 3,
> $$|f(x)-f(y)| = \Big|\int_0^1 u(t)\,dt\Big| \le \int_0^1|u(t)|\,dt.$$
> For each $t$, the point $\xi_t = (1-t)y+tx$ lies on the segment, so $|u(t)| = |Df_{\xi_t}(x-y)| \le \|Df_{\xi_t}\|\,|x-y| \le M\,|x-y|$. Integrating the constant bound,
> $$|f(x)-f(y)| \le \int_0^1 M|x-y|\,dt = M\,|x-y|.$$
> If $U$ is convex and $\|Df\| \le M$ on all of $U$, every segment lies in $U$ and the bound holds for all $x, y \in U$: $f$ is $M$-Lipschitz.
>
> **Corollary — locally Lipschitz.** Let $f \in C^1(U)$ and $x_\circ \in U$. Choose $\delta > 0$ with $\overline{B}(x_\circ,\delta)\subseteq U$. The ball is convex and compact, $Df$ is continuous, so $M := \sup_{\overline{B}}\|Df\| < \infty$; by the inequality $f$ is $M$-Lipschitz on $B(x_\circ,\delta)$. Since $x_\circ$ was arbitrary, $f$ is locally Lipschitz.
>
> **Corollary — constancy.** Suppose $Df \equiv 0$ on an open connected $U$. Fix $x_\circ \in U$ and let $A = \{x\in U : f(x) = f(x_\circ)\}$. $A$ is non-empty ($x_\circ\in A$). $A$ is closed in $U$ by continuity of $f$. $A$ is open: for $x\in A$, take a ball $B(x,\delta)\subseteq U$; it is convex and $\|Df\| = 0$ on it, so the inequality with $M = 0$ gives $f(y) = f(x) = f(x_\circ)$ for every $y\in B(x,\delta)$, hence $B(x,\delta)\subseteq A$. A non-empty subset of the connected set $U$ that is both open and closed equals $U$, so $f \equiv f(x_\circ)$ on $U$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Uniqueness for differential equations.** If two solutions of an initial value problem have the same derivative structure, their difference has vanishing derivative on a connected interval, so by the constancy corollary it is constant — and zero at the initial time, hence zero throughout. The application is nonobvious because uniqueness looks like it needs Grönwall's inequality, while in the simplest cases it is just "$Df = 0 \Rightarrow f$ constant".

**Contraction estimates for fixed-point iteration.** A map with $\|Df\| \le M < 1$ on a convex set is, by the inequality, a contraction in the metric sense; the contraction mapping principle then gives a unique fixed point. The application is the technical core of the inverse function theorem, and it is nonobvious in that a *derivative* bound is being upgraded to a *metric* contraction hypothesis.

**Conservative vector fields.** Two scalar potentials with the same gradient differ by a constant on a connected domain — this is the constancy corollary, and it is why a potential is determined up to an additive constant. The application is nonobvious because "the potential is unique up to a constant" sounds like a separate fact rather than a one-line consequence of the mean value inequality.

**Stability of numerical schemes.** A numerical step map with bounded derivative does not amplify errors faster than its Lipschitz constant; iterating, the global error is controlled. The mean value inequality is the per-step estimate, and the application is out-of-distribution in that "stability" sounds algorithmic while it reduces to a derivative bound.

---

# Bridges

- **The one-variable mean value theorem** — the special case $n = m = 1$, and the engine of the scalar half (it is applied to the restriction $\varphi$). The multivariate scalar equality is the one-variable theorem transported along a segment by the chain rule.

- **[[Thm - The Chain Rule|The Chain Rule]]** — the tool that computes the segment-velocity $\varphi'(t) = Df_{x_\circ+th}(h)$. Without it the restriction-to-a-line technique would not get off the ground.

- **The fundamental theorem of calculus** — the alternative engine, used in the vector half: the increment is the integral of the derivative along the segment, and the inequality follows from $|\int|\le\int|\cdot|$.

- **The contraction mapping principle** — a downstream consumer. The inequality with $M < 1$ produces the contraction hypothesis that the fixed-point theorem requires; this is the link to the inverse function theorem of **Multivariate Analysis II**.

- **Closed curves and the failure of the equality** — the unit circle $\gamma(t) = (\cos2\pi t, \sin2\pi t)$ is the standard certificate that the vector mean value *equality* is false: zero increment, never-zero velocity. It marks the precise boundary of what the theorem can claim.

---

# Unlocked by This

> [!tip] The Contraction Mapping Principle and the Inverse Function Theorem *(from Multivariate Analysis II)*
> A map with $\|Df\| \le M < 1$ on a convex set is a metric contraction by the inequality, so the **contraction mapping principle** gives it a unique fixed point. This is the analytic core of the **inverse function theorem**: a $C^1$ map with invertible derivative is locally invertible.

> [!tip] Grönwall's Inequality and Well-Posedness *(from Differential Equations)*
> The mean value inequality is the linear, one-step special case of **Grönwall's inequality**, the estimate that controls how fast solutions of differential equations can separate. It underlies the theorems on existence, uniqueness, and continuous dependence on initial data.
