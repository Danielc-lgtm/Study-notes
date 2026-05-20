---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Primitive (Antiderivative)"
  - "Thm - Existence of a Primitive iff Closed Integrals Vanish"
  - "Thm - Fundamental Theorem of Contour Integration"
  - "Def - Contour Integral"
tags: [analysis, complex-analysis]
---

# Problem Statement

The function $f(z) = 1/z$ is holomorphic on $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$. Use this function to make the equivalence "primitive exists $\iff$ all closed-loop integrals vanish" concrete:

1. Compute $\displaystyle \oint_{|z|=1} \frac{dz}{z}$ directly by parametrising the unit circle, and conclude that $f$ has *no primitive* on $\mathbb{C}^\times$.

2. On the *slit plane* $\Omega = \mathbb{C} \setminus (-\infty, 0]$, exhibit an explicit holomorphic primitive of $f$ — namely a branch of $\log z$ — and verify $F'(z) = 1/z$ directly.

3. Verify the equivalence in this concrete case: for any closed piecewise $C^1$ curve $\gamma$ contained in $\Omega$, $\oint_\gamma dz/z = 0$ via the [[Thm - Fundamental Theorem of Contour Integration|fundamental theorem]]. Show by example that, although $1/z$ has *no* primitive on $\mathbb{C}^\times$, it has *local* primitives at every point of $\mathbb{C}^\times$ — there is no obstruction locally; the obstruction is global.

**Recall:**

![[Def - Primitive (Antiderivative)#The Definition]]

![[Thm - Existence of a Primitive iff Closed Integrals Vanish#Statement]]

![[Thm - Fundamental Theorem of Contour Integration#Statement]]

The **principal branch** of the logarithm is $\log z := \log|z| + i\arg z$ where $\arg z$ is taken in $(-\pi, \pi]$. This is well-defined and continuous on the slit plane $\Omega = \mathbb{C} \setminus (-\infty, 0]$, and discontinuous across the negative real axis (where $\arg$ jumps from $\pi$ to $-\pi$). Its complex derivative on $\Omega$ is $1/z$ — a standard computation from the Cauchy–Riemann equations (or from inverting $z = e^w$ near a point with $\arg z \in (-\pi, \pi)$).

A **closed piecewise $C^1$ curve** in a domain $U$ is a continuous map $\gamma : [a, b] \to U$ that is $C^1$ on finitely many subintervals partitioning $[a, b]$, with $\gamma(a) = \gamma(b)$.

---

# Convergent Strategy

**Problem class.** This is a *worked example* of the equivalence theorem: take a concrete function whose closed-loop behaviour is computable in two different ways and exhibit both sides of the iff. The problem class is "verify a theorem in a concrete instance to expose the mechanism" — particularly useful when the theorem packages two implications that are non-trivial in opposite directions. Here the forward direction (primitive $\Rightarrow$ closed integral vanishes) is the [[Thm - Fundamental Theorem of Contour Integration|fundamental theorem]], a one-line consequence of the chain rule; the converse (closed integrals vanish $\Rightarrow$ primitive exists) is the genuine content of the [[Thm - Existence of a Primitive iff Closed Integrals Vanish|existence theorem]].

**Assumption pattern.** The exercise hinges on a topological switch: $\mathbb{C}^\times$ contains a non-trivial closed loop (the unit circle around $0$), while the slit plane $\Omega = \mathbb{C} \setminus (-\infty, 0]$ does *not* — the slit obstructs any loop from winding around $0$. The signature is "remove a one-dimensional set from $\mathbb{C}^\times$ to kill the topological obstruction" — the slit plane is *simply connected*, which forces every closed loop to be contractible and hence (by Cauchy's theorem, downstream) to give a vanishing integral for any holomorphic $f$.

**Theorem routing.** The route has three independent threads, one for each part of the problem. (a) Direct computation: parametrise the unit circle as $\gamma(t) = e^{it}$, $t \in [0, 2\pi]$; then $\oint_{|z|=1} dz/z = \int_0^{2\pi} (e^{-it})(ie^{it})\,dt = 2\pi i$. By the [[Thm - Existence of a Primitive iff Closed Integrals Vanish|existence theorem]] in the contrapositive form, a non-vanishing closed integral forbids a primitive on $\mathbb{C}^\times$. (b) Construction: define $F(z) = \log|z| + i\arg z$ on $\Omega$ with $\arg \in (-\pi, \pi)$; compute $F'(z) = 1/z$ by Cauchy–Riemann or by inverting $z = e^w$. (c) Verification: for any closed $\gamma$ in $\Omega$, $\oint_\gamma dz/z = F(\gamma(b)) - F(\gamma(a)) = 0$ since $\gamma(a) = \gamma(b)$ — the [[Thm - Fundamental Theorem of Contour Integration|fundamental theorem]] in the simplest form.

**Key decision point.** The crux is *which slit to cut*. To get a simply connected domain containing the punctured plane minus a one-dimensional set, we must remove a curve from $0$ to $\infty$ — any continuous curve will do, but a *ray* is the simplest, and the negative real axis gives a logarithm whose imaginary part is the *principal* argument $\arg \in (-\pi, \pi)$, the most familiar choice. Cutting along the positive real axis instead would give $\arg \in (0, 2\pi)$, a non-principal branch. Cutting along a spiral is technically valid but produces an unworkable formula. The decision "ray from $0$ to $\infty$" is what makes the branch usable; the decision "negative real axis" is convention.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Complex Analysis II — Cauchy's Theorem and its Consequences#Legal Operations|the topic page's Legal Operations]]:

1. **Compute a contour integral by direct parametrisation.** The unit circle $|z| = 1$ has the standard parametrisation $\gamma(t) = e^{it}$, $t \in [0, 2\pi]$. Substituting into $\int_a^b f(\gamma(t))\gamma'(t)\,dt$ converts the contour integral into an ordinary integral over a real interval. This is the universal first move when no other tool applies, and the one move every later technique reduces to in principle.

2. **Apply the fundamental theorem of contour integration to a closed curve** (operation related to the [[Thm - Fundamental Theorem of Contour Integration|FT]]). When a primitive $F$ is available on a domain containing the curve $\gamma$, $\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a))$; for closed $\gamma$ this is $0$. This is the cleanest way to compute or rule out a closed-loop integral, when a primitive can be exhibited.

3. **Use the existence theorem in contrapositive** ([[Thm - Existence of a Primitive iff Closed Integrals Vanish|operation]]). If a single closed integral $\oint_\gamma f\,dz \neq 0$, then *no* primitive of $f$ on the domain of $\gamma$ exists. One non-vanishing example suffices to rule out existence — a much more efficient way of *disproving* primitive existence than trying every conceivable candidate.

---

# Hints

> [!note]- Hint 1
> For the unit-circle integral: parametrise $z = e^{it}$, $dz = ie^{it}\,dt$, and $1/z = e^{-it}$. Substitute and integrate.

> [!note]- Hint 2
> A non-vanishing closed integral immediately rules out a global primitive: if $F$ were a primitive on $\mathbb{C}^\times$, the fundamental theorem would give $\oint dz/z = F(\gamma(2\pi)) - F(\gamma(0)) = F(1) - F(1) = 0$, contradicting Step 1.

> [!note]- Hint 3
> On the slit plane $\Omega = \mathbb{C} \setminus (-\infty, 0]$, every $z \in \Omega$ has a unique $\arg z \in (-\pi, \pi)$. Define $F(z) = \log|z| + i\arg z$, where $\log|z|$ is the real logarithm of the modulus. Check $F$ is continuous (because $\arg$ is continuous on $\Omega$), and compute $F'$ via Cauchy–Riemann or by inverting $z = e^F$.

> [!note]- Hint 4
> For any closed curve $\gamma$ in $\Omega$, the fundamental theorem gives $\oint_\gamma dz/z = F(\gamma(b)) - F(\gamma(a)) = 0$. This is the *forward* direction of the equivalence theorem applied in the explicit case of $f = 1/z$ on the slit plane.

> [!note]- Hint 5
> For "local primitives exist at every point of $\mathbb{C}^\times$": every point of $\mathbb{C}^\times$ has an open disc neighbourhood contained in a slit plane (rotate the slit if necessary to avoid the point). On that disc, the local branch of $\log$ is a primitive of $1/z$. The obstruction is *not* at any point; it is in the global homotopy class of the unit circle around $0$.

---

# Solution

The plan is to expose both directions of the equivalence theorem on the single function $f(z) = 1/z$. Step 1 computes the unit-circle integral by direct parametrisation, getting $2\pi i$ and ruling out a primitive on $\mathbb{C}^\times$ in the contrapositive. Step 2 constructs an explicit primitive on the simply connected slit plane $\Omega$ and verifies $F' = 1/z$. Step 3 reuses $F$ to verify, via the fundamental theorem, that every closed-loop integral on $\Omega$ vanishes — and exhibits a *local* primitive at every point of $\mathbb{C}^\times$, showing the obstruction is purely topological.

**Step 1: $\oint_{|z|=1} dz/z = 2\pi i$, hence $1/z$ has no primitive on $\mathbb{C}^\times$.**

Parametrising the positively oriented unit circle gives $\oint_{|z|=1} dz/z = 2\pi i$. Because this is nonzero, the existence theorem rules out a primitive on $\mathbb{C}^\times$.

> [!note]- Derivation
> Parametrise $\gamma(t) = e^{it}$ for $t \in [0, 2\pi]$; this is a $C^1$ map onto the positively oriented unit circle with $\gamma(0) = \gamma(2\pi) = 1$, so it is a closed curve. Compute $\gamma'(t) = ie^{it}$ and $1/\gamma(t) = e^{-it}$, so by [[Def - Contour Integral|the definition of the contour integral]]:
> $$\oint_{|z|=1} \frac{dz}{z} \;=\; \int_0^{2\pi} \frac{1}{e^{it}} \cdot ie^{it}\,dt \;=\; \int_0^{2\pi} i\,dt \;=\; i \cdot 2\pi \;=\; 2\pi i.$$
>
> Now apply [[Thm - Existence of a Primitive iff Closed Integrals Vanish|the existence theorem]] in *contrapositive*: if $f$ had a primitive on the domain $\mathbb{C}^\times$ containing the curve, then by the [[Thm - Fundamental Theorem of Contour Integration|fundamental theorem]], $\oint_{|z|=1} dz/z = F(\gamma(2\pi)) - F(\gamma(0)) = F(1) - F(1) = 0$. But the integral equals $2\pi i \neq 0$, so no such $F$ exists. The function $f(z) = 1/z$ has *no* primitive on $\mathbb{C}^\times$.

**Step 2: On the slit plane $\Omega = \mathbb{C} \setminus (-\infty, 0]$, $F(z) = \log|z| + i\arg z$ is a primitive of $1/z$.**

Define $F : \Omega \to \mathbb{C}$ by $F(z) := \log|z| + i\arg z$ with $\arg z \in (-\pi, \pi)$. Then $F$ is holomorphic on $\Omega$ with $F'(z) = 1/z$.

> [!note]- Derivation
> *Continuity and well-definedness.* For $z \in \Omega$, both $|z| > 0$ (since $z \neq 0$) and $\arg z \in (-\pi, \pi)$ (the open interval avoiding the negative real axis) are well-defined and continuous functions of $z$ — the standard "principal" argument fails to be continuous only on $(-\infty, 0)$, which we have removed. So $F$ is continuous on $\Omega$.
>
> *Identification $F(z) = \log z$ as a branch.* The function $F$ satisfies $e^{F(z)} = e^{\log|z| + i\arg z} = |z|\, e^{i\arg z} = z$ (the polar form). So $F$ is *a* branch of the logarithm — one continuous solution to $e^w = z$ on $\Omega$.
>
> *Holomorphicity and derivative.* Write $z = x + iy$ with $z \in \Omega$. Then $|z| = \sqrt{x^2 + y^2}$ and $\arg z = \arctan(y/x)$ when $x > 0$ (with a piecewise extension when $x \leq 0, y \neq 0$, but locally any branch of $\arctan$ adapted to the quadrant works smoothly). Set $u(x, y) = \tfrac{1}{2}\log(x^2 + y^2)$ and $v(x, y) = \arg z$, so $F = u + iv$. Then
> $$u_x = \frac{x}{x^2 + y^2}, \qquad u_y = \frac{y}{x^2 + y^2}, \qquad v_x = \frac{-y}{x^2 + y^2}, \qquad v_y = \frac{x}{x^2 + y^2},$$
> the last two computed by differentiating $\arctan(y/x)$ in $x$ and $y$ respectively (and verifying the same formulas hold for any local branch of $\arg$ avoiding the slit). The Cauchy–Riemann equations $u_x = v_y$ and $u_y = -v_x$ hold (both yield $x/(x^2+y^2)$ for the first and $y/(x^2+y^2)$ for the second). So $F$ is holomorphic with
> $$F'(z) \;=\; u_x + iv_x \;=\; \frac{x}{x^2 + y^2} + i\,\frac{-y}{x^2 + y^2} \;=\; \frac{x - iy}{x^2 + y^2} \;=\; \frac{\bar z}{|z|^2} \;=\; \frac{1}{z}.$$
>
> *Alternative derivation by inverse function.* The function $z = e^w$ is entire and holomorphic with $dz/dw = e^w = z \neq 0$ everywhere. On a neighbourhood of any point of $\Omega$, $F$ is the local inverse of $e^w$ restricted to a horizontal strip $\{|\operatorname{Im} w| < \pi\}$, so by the inverse function theorem (in its complex form) $F$ is holomorphic with $F'(z) = 1/(dz/dw)|_{w = F(z)} = 1/e^{F(z)} = 1/z$.
>
> Either route: $F$ is a primitive of $f(z) = 1/z$ on $\Omega$.

**Step 3: Verification of the equivalence on $\Omega$, and local primitives at every point of $\mathbb{C}^\times$.**

For every closed piecewise $C^1$ curve $\gamma$ in $\Omega$, $\oint_\gamma dz/z = 0$ — a one-line consequence of the fundamental theorem. And at every point of $\mathbb{C}^\times$ there is a local branch of $\log$ defined on a small disc around that point.

> [!note]- Derivation
> *Closed-loop vanishing on $\Omega$.* Let $\gamma : [a, b] \to \Omega$ be a closed piecewise $C^1$ curve, $\gamma(a) = \gamma(b)$. By the [[Thm - Fundamental Theorem of Contour Integration|fundamental theorem]] applied to the primitive $F$ on $\Omega$:
> $$\oint_\gamma \frac{dz}{z} \;=\; F(\gamma(b)) - F(\gamma(a)) \;=\; F(\gamma(a)) - F(\gamma(a)) \;=\; 0.$$
> Every closed loop in $\Omega$ has vanishing integral against $1/z$. This is the *forward* direction of the [[Thm - Existence of a Primitive iff Closed Integrals Vanish|equivalence theorem]] for $1/z$ on $\Omega$.
>
> *Local primitives at every point of $\mathbb{C}^\times$.* Fix $z_0 \in \mathbb{C}^\times$. Choose an angle $\theta_0$ with $\arg z_0 \neq \theta_0 + \pi$, i.e., $z_0$ does not lie on the ray from $0$ in direction $\theta_0 + \pi$. Let $L_{\theta_0} := \{re^{i(\theta_0 + \pi)} : r \geq 0\}$ be that ray, and let $\Omega_{\theta_0} := \mathbb{C} \setminus L_{\theta_0}$ be the corresponding slit plane — open, simply connected, and containing $z_0$. On $\Omega_{\theta_0}$, the branch of $\log$ with $\arg \in (\theta_0 - \pi, \theta_0 + \pi)$ is holomorphic with derivative $1/z$ (by the same argument as Step 2, with the slit and $\arg$-range rotated). Restricting to a small disc $D(z_0, \varepsilon) \subseteq \Omega_{\theta_0}$ gives a *local primitive* of $1/z$ at $z_0$.
>
> So every point of $\mathbb{C}^\times$ has a neighbourhood on which $1/z$ has a primitive — local primitives always exist. The obstruction to a *global* primitive on $\mathbb{C}^\times$ is not at any single point; it lives in the global homotopy class of the unit circle around $0$, which $\mathbb{C}^\times$ admits but no slit plane does.

> [!note]- Complete formal solution
> *(a) Direct computation.* Parametrise the unit circle by $\gamma(t) = e^{it}$, $t \in [0, 2\pi]$; then $\gamma'(t) = ie^{it}$ and
> $$\oint_{|z|=1} \frac{dz}{z} \;=\; \int_0^{2\pi} e^{-it}\cdot ie^{it}\,dt \;=\; \int_0^{2\pi} i\,dt \;=\; 2\pi i \;\neq\; 0.$$
> By [[Thm - Existence of a Primitive iff Closed Integrals Vanish|the existence theorem]] contrapositively, $1/z$ has no primitive on $\mathbb{C}^\times$.
>
> *(b) Construction of a primitive on $\Omega$.* On $\Omega := \mathbb{C} \setminus (-\infty, 0]$, set $F(z) := \log|z| + i\arg z$ with $\arg z \in (-\pi, \pi)$. Then $F$ satisfies $e^{F(z)} = z$ (so $F$ is a branch of $\log$); writing $F = u + iv$ with $u = \tfrac{1}{2}\log(x^2 + y^2)$ and $v = \arg z$, one verifies the Cauchy–Riemann equations and computes $F'(z) = u_x + iv_x = (x - iy)/(x^2 + y^2) = 1/z$.
>
> *(c) Verification of vanishing on $\Omega$.* For any closed curve $\gamma$ in $\Omega$, the [[Thm - Fundamental Theorem of Contour Integration|fundamental theorem]] gives $\oint_\gamma dz/z = F(\gamma(b)) - F(\gamma(a)) = 0$. Hence $1/z$ has a primitive on $\Omega$ and (consistently) all closed-loop integrals on $\Omega$ vanish.
>
> *(d) Local primitives at every point of $\mathbb{C}^\times$.* For $z_0 \in \mathbb{C}^\times$, rotate the slit to a ray not passing through $z_0$; the corresponding branch of $\log$ is a primitive of $1/z$ on a slit-plane neighbourhood of $z_0$, hence on a small disc around $z_0$. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> A natural impulse is to "define $F(z) = \log z$ on $\mathbb{C}^\times$ by picking any value of $\arg z$ at each point." This *fails* because $\arg z$ cannot be chosen continuously on $\mathbb{C}^\times$: any continuous selection on a small punctured disc around $0$ extends along a loop and is forced to increase by $2\pi$ each time the loop goes around $0$ — incompatible with the loop closing. The continuous selection problem has no global solution; this is the topological content of $\pi_1(\mathbb{C}^\times) = \mathbb{Z}$. The repair is exactly the slit: removing a ray from $0$ to $\infty$ disconnects the loops around $0$ from the homotopy class of constants, and $\arg z$ becomes continuously selectable.

---

# Key Takeaways

**The equivalence theorem reads in two directions, and each direction is its own technique.**

The [[Thm - Existence of a Primitive iff Closed Integrals Vanish|existence theorem]] is, on the surface, a single biconditional: $f$ has a primitive on $U$ if and only if every closed-loop integral of $f$ on $U$ vanishes. Operationally, however, the two directions function as *different* tools. The forward direction (primitive $\Rightarrow$ closed integrals vanish) is the [[Thm - Fundamental Theorem of Contour Integration|fundamental theorem]] and is *easy*: one line of chain rule. It is used to *compute* a closed-loop integral when a primitive is known — and to *rule out* primitives by exhibiting a non-vanishing integral (the contrapositive). The converse direction (closed integrals vanish $\Rightarrow$ primitive exists) is the genuinely analytic content: it constructs the primitive as an integral $F(z) = \int_a^z f\,dw$ along an arbitrary path, with well-definedness exactly because all closed loops give zero. The construction is the engine behind Cauchy's theorem on star-shaped domains. Whenever one encounters a primitive-existence problem, the first question is *which direction of the equivalence theorem is doing the work*: are we exhibiting a primitive to conclude closed integrals vanish, or are we computing a single closed integral to rule out primitives? The two strategies look identical at the level of the theorem statement but at the level of *technique* are mirror images.

**Global obstructions to primitives are topological, not local.**

The example $f(z) = 1/z$ on $\mathbb{C}^\times$ is the simplest non-trivial example of the *topological* nature of primitive existence in complex analysis. Locally, $1/z$ has a primitive at every point — every point of $\mathbb{C}^\times$ sits in a slit plane where $\log$ exists as an honest holomorphic function. The failure is global: the loop around the origin produces a *monodromy* — a $2\pi i$ shift in $\log z$ as we go once around — and no continuous global selection of $\arg z$ on $\mathbb{C}^\times$ exists. The general phenomenon is that primitive existence depends on $\pi_1$ of the domain: for *simply connected* $U$ (i.e., $\pi_1(U) = 0$), every holomorphic $f$ on $U$ has a global primitive (this is Cauchy's theorem); for $U$ with non-trivial $\pi_1$, primitives may fail to exist, and the obstruction lives in the integral $\oint_\gamma f\,dz$ as $\gamma$ runs over a basis of homotopy classes. Recognising "is the domain simply connected?" as the first question whenever primitive existence is asked is the most reusable diagnostic in this region of the subject — and it generalises seamlessly into de Rham cohomology and the residue theorem of [[Complex Analysis III — Winding, Laurent, Residues|CA III]].

**One non-vanishing closed integral is enough to rule out a primitive.**

The contrapositive use of the existence theorem is one of the *most efficient* moves in complex analysis. To rule out the existence of a primitive on a domain $U$ for a function $f$, one does not need to argue exhaustively that "no candidate $F$ works"; instead, exhibit a *single* closed curve $\gamma$ in $U$ with $\oint_\gamma f\,dz \neq 0$. The unit circle around $0$ does this for $1/z$ on $\mathbb{C}^\times$ in one line. The same trigger applies in many other settings: $\oint_{|z|=1} \bar z\,dz = 2\pi i$ rules out a primitive of $\bar z$ anywhere $\bar z$ is *not* holomorphic (which is everywhere — but the contour-integral test gives a clean obstruction even when other holomorphic tests do not apply); $\oint_\gamma \omega \neq 0$ rules out exactness of a 1-form $\omega$. The reusable diagnostic is: *whenever you are asked "does this function have a primitive on $U$?", first try to find a closed loop in $U$ around a singularity or a topological hole and compute the integral; non-vanishing answers the question in the negative immediately.*

**The slit plane is the universal repair for the punctured plane.**

The construction of a primitive for $1/z$ on the slit plane $\Omega = \mathbb{C} \setminus (-\infty, 0]$ exhibits the standard repair strategy for handling singularities: replace a non-simply-connected domain by a simply connected sub-domain that avoids the topological obstruction. The slit plane is the universal example — it removes a one-dimensional "branch cut" from $0$ to $\infty$, exactly enough to disconnect the homotopy class of loops winding around $0$. The choice of slit is somewhat arbitrary (any continuous curve from $0$ to $\infty$ would do), but the negative real axis is conventional because it makes $\arg z \in (-\pi, \pi)$ the *principal* argument and gives the principal branch of $\log z$. Once one has internalised that "any slit from $0$ to $\infty$ produces a slit plane on which $\log z$ is a primitive of $1/z$," similar moves transfer to other multi-valued functions: $\sqrt{z}$ on the slit plane, $z^\alpha$ for non-integer $\alpha$ on the slit plane, and more elaborate branch-cut constructions for $\sqrt{z^2 - 1}$ or $\log((1-z)/(1+z))$. The pattern is identical: *identify the branch points; cut between them so the resulting domain is simply connected; choose a branch on that domain*. See also [[Ex - Verifying Cauchy on a triangle in C minus 0]] for a closely related use of the slit plane.
