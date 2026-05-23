---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Closed and Exact Forms"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Thm - The Poincaré Lemma on a Star-Shaped Region"
tags: [geometry, differential-geometry, complex-analysis, cauchy]
---

# Notation

The setting is the complex plane $\mathbb{C}$ identified with $\mathbb{R}^2$ via $z = x + iy$, with coordinates $(x, y)$ and the corresponding complex-valued $1$-forms $dz = dx + i\,dy$ and $d\bar z = dx - i\,dy$. The wedge product of these is $dz\wedge d\bar z = -2i\,dx\wedge dy$. The **Wirtinger derivatives** are
$$\frac{\partial}{\partial z} = \tfrac{1}{2}\left(\frac{\partial}{\partial x} - i\frac{\partial}{\partial y}\right), \qquad \frac{\partial}{\partial\bar z} = \tfrac{1}{2}\left(\frac{\partial}{\partial x} + i\frac{\partial}{\partial y}\right),$$
chosen so that on holomorphic test functions $\partial z/\partial z = 1$, $\partial z/\partial\bar z = 0$, $\partial\bar z/\partial z = 0$, $\partial\bar z/\partial\bar z = 1$.

A complex-valued function $f : U \to \mathbb{C}$ on an open set $U \subseteq \mathbb{C}$ decomposes as $f(z, \bar z) = a(x, y) + i\,b(x, y)$ with $a, b$ real-valued. We allow complex-valued differential forms: $f\,dz$ is a complex-valued $1$-form, exterior derivative and wedge product extending $\mathbb{C}$-linearly. A **holomorphic** (complex-analytic) function on $U$ is one satisfying $\partial f/\partial\bar z = 0$ in $U$, equivalently the [[Thm - Cauchy–Riemann Equations|Cauchy–Riemann equations]] $\partial a/\partial x = \partial b/\partial y$ and $\partial a/\partial y = -\partial b/\partial x$.

$\gamma : [0, 1] \to U$ is a piecewise-smooth closed curve in $U$, and $\oint_\gamma f\,dz$ is the contour integral $\int_\gamma f\,dz$. The contour is **homologically trivial** in $U$ if it bounds a $2$-chain in $U$. A domain $U$ is **simply connected** if every closed loop in $U$ is contractible; equivalently (in the plane), every closed curve in $U$ bounds a $2$-chain in $U$.

The full notation registry for this topic is on [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]].

---

# Statement

> **Theorem (Cauchy's Integral Theorem via Stokes).** Let $U \subseteq \mathbb{C}$ be open and $f : U \to \mathbb{C}$ a holomorphic function. Then the complex-valued $1$-form $f(z)\,dz$ on $U$ is **closed**: $d(f(z)\,dz) = 0$. In particular, by Stokes's theorem, for every compact oriented $2$-chain $D \subseteq U$ with boundary $\partial D = \gamma$,
> $$\oint_\gamma f(z)\,dz = \int_D d(f(z)\,dz) = 0.$$

> **Corollary (Classical Cauchy's Integral Theorem).** If $U$ is simply connected and $f$ is holomorphic on $U$, then $\oint_\gamma f(z)\,dz = 0$ for every closed contour $\gamma$ in $U$.

> **Converse (Holomorphy as closedness of $f(z)\,dz$).** Conversely, if $f$ is $C^1$ on $U$ and $f(z)\,dz$ is closed, then $f$ is holomorphic. So holomorphy and the closedness of $f(z)\,dz$ are *equivalent* conditions on a $C^1$ function — and the Cauchy–Riemann equations $\partial f/\partial\bar z = 0$ are the literal coefficient computation of $d(f(z)\,dz) = 0$.

The corollary follows because in a simply connected domain every closed curve bounds an oriented $2$-chain; the equivalence "holomorphic $\iff$ $f(z)\,dz$ closed" is the statement Stokes converts $\oint = 0$ into.

---

# Motivation

Cauchy's integral theorem is the foundational result of complex analysis — the source from which the Cauchy integral formula, [[Def - Residue|residue]] theorem, identity theorem, maximum principle, and every other major theorem of analytic-function theory ultimately derive. Its original proof in complex-analysis textbooks involves Goursat-style triangle arguments and careful $\varepsilon$-$\delta$ estimates, and the result looks like an analytic miracle: an integral that vanishes for reasons not obvious from any computation.

The form-language proof reveals what is actually happening. The complex-valued $1$-form $f(z)\,dz$ on $\mathbb{R}^2 \cong \mathbb{C}$ has its exterior derivative computable by the standard rules: $d(f(z)\,dz) = df\wedge dz$. Expanding $df = (\partial f/\partial z)\,dz + (\partial f/\partial\bar z)\,d\bar z$ and using $dz\wedge dz = 0$, we get $d(f\,dz) = (\partial f/\partial\bar z)\,d\bar z\wedge dz$. This is zero if and only if $\partial f/\partial\bar z = 0$ — which is *exactly* the Cauchy–Riemann equations. So holomorphy and closedness of $f(z)\,dz$ are *the same condition*, written in two notations. The "analytic miracle" of Cauchy's theorem is now a corollary of two facts: (i) the Cauchy–Riemann equations rephrased as $d(f\,dz) = 0$, and (ii) Stokes's theorem $\oint_\gamma\omega = \int_D d\omega$ for a closed contour bounding a $2$-chain in $U$.

This recasting is a paradigm shift in two ways. First, it embeds complex analysis in the de Rham complex of $\mathbb{R}^2$: holomorphic functions are nothing but "smooth complex-valued $0$-forms such that the natural $1$-form $f\,dz$ is closed." Second, it generalizes immediately to **Riemann surfaces** — any $1$-dimensional complex manifold — where the same de Rham machinery (forms, $d$, Stokes) reproduces the whole of one-dimensional complex analysis without any new tools. The Cauchy integral theorem becomes a special case of a far broader pattern: "closed form on simply connected manifold $\implies$ integrals over closed cycles vanish."

The motivational payoff is that one no longer needs separate proofs for each Cauchy-style theorem in complex analysis: every one of them is Stokes plus some form-level identity. Cauchy's integral formula will turn out to be Stokes plus the [[Def - Residue|residue]] computation at the pole; the residue theorem will be Stokes for forms with isolated singularities; the holomorphic functional calculus on operators will be Stokes applied to operator-valued forms. The form-language perspective unifies what classical complex analysis presents as a sequence of distinct theorems.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis "the $1$-form $f(z)\,dz$ is closed on $U$" is unfamiliar in classical complex-analysis language but trivial to verify in many contexts.

The most common source is **a function $f$ that is given as holomorphic**. Property $B$: "$f$ is complex-analytic (or has a convergent power-series expansion, or is conformal, or satisfies the Cauchy–Riemann equations explicitly)." The bridge: each of these conditions is equivalent to $\partial f/\partial\bar z = 0$, which is the coefficient of $d(f\,dz)$. So a holomorphic $f$ produces a closed $1$-form. The implication is non-obvious only because the four-or-five equivalent characterizations of holomorphy are usually proved as a separate package in complex-analysis courses; once you see them as different views of $d(f\,dz) = 0$, the equivalences are tautological.

A second source is **a $C^1$ function $f$ satisfying the Cauchy–Riemann equations**. Property $B$: "$f$ is real-differentiable with $\partial a/\partial x = \partial b/\partial y$, $\partial a/\partial y = -\partial b/\partial x$." The bridge: these are the real and imaginary parts of $\partial f/\partial\bar z = 0$. So the Cauchy–Riemann equations *are* the closedness condition for $f\,dz$. The historical fact is that the Cauchy–Riemann equations were discovered before exterior calculus was invented; the form-language reframing makes the equations look natural rather than miraculous.

A third source is **a primitive (potential) $F$ for $f$**. Property $B$: "there is a holomorphic $F$ on $U$ with $F'(z) = f(z)$." The bridge: then $f(z)\,dz = dF$ (as complex-valued forms, where $dF = F'(z)\,dz$ because $F$ is holomorphic so $\partial F/\partial\bar z = 0$), which is exact, hence closed. The implication is "exact $\implies$ closed", which is $d^2 = 0$. The trigger in problems: whenever a problem hands you a holomorphic antiderivative, $f(z)\,dz$ is exact and any contour integral over a closed curve vanishes by Stokes (even without simple-connectedness, because the form is *exact* not just closed).

A fourth source is **a meromorphic function in a region avoiding the poles**. Property $B$: "$f$ is meromorphic on $U$ with poles at isolated points $z_1, \dots, z_k$, and $\gamma$ lies in $U \setminus \{z_1, \dots, z_k\}$." The bridge: $f$ is holomorphic on $U \setminus \{z_1, \dots, z_k\}$, so $f(z)\,dz$ is closed there. The contour integral $\oint_\gamma f\,dz$ depends only on the winding numbers around the poles, by the residue theorem. The implication is the gateway to the **residue calculus** and the [[Thm - Cauchy Integral Formula|Cauchy Integral Formula]] in [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

**Targets (Output Amplification)**

The conclusion $\oint_\gamma f\,dz = 0$ is the entry-point to every other Cauchy-style result.

The most powerful combination is **Stokes-with-closed-form gives a primitive**. Take the conclusion $\oint_\gamma f(z)\,dz = 0$ for every closed contour $\gamma$ in a simply connected $U$ (property $C$). Combine with property $D$: pick a base point $z_0 \in U$ and define $F(z) := \int_{z_0}^z f(w)\,dw$ along any path in $U$. By the conclusion, the integral is path-independent (any two paths differ by a closed loop, around which the integral is zero), so $F$ is well-defined. The result $E$ is that *every* holomorphic function on a simply connected domain admits a holomorphic antiderivative — the **existence of a holomorphic primitive**. The combination is nonobvious because the conclusion is about closed integrals while the result is about the existence of a function; the bridge is path-independence.

A second combination is **Cauchy plus winding number gives the residue formula**. Take the conclusion for a function $f$ holomorphic on $U \setminus \{z_0\}$ with a simple pole at $z_0$ inside $\gamma$ (property $C$): the integral $\oint_\gamma f\,dz$ around a closed contour enclosing $z_0$. Combine with property $D$: the local expansion $f(z) = c/(z - z_0) + g(z)$ with $g$ holomorphic. The integral of the holomorphic part vanishes by Cauchy's theorem; the integral of the polar part is $c\oint_\gamma dz/(z - z_0) = 2\pi i c$ (a standard winding-number computation). The result $E$ is the **residue formula** $\oint_\gamma f\,dz = 2\pi i\,\mathrm{Res}_{z_0}(f)\cdot n(\gamma, z_0)$, where $n(\gamma, z_0)$ is the winding number. This is the foundational tool of contour integration in calculus.

A third combination is **Cauchy plus a Cauchy kernel gives the integral formula**. Take the conclusion applied to $g(z) = f(z)/(z - z_0)$ on a region with a small circle around $z_0$ removed (property $C$). Combine with property $D$: the singularity at $z_0$ is a simple pole with residue $f(z_0)$. Then $\oint_\gamma f(z)/(z - z_0)\,dz = 2\pi i\,f(z_0)$ — the **Cauchy integral formula**. This combination underlies every $L^\infty$/$L^2$ estimate of holomorphic functions, the proof that holomorphic functions are smooth (in fact analytic), the maximum modulus principle, and the resolution of Liouville's theorem (bounded entire functions are constant).

A fourth combination is **Cauchy plus deformation gives homotopy invariance**. Take the conclusion as the statement "the integral of $f\,dz$ over a closed contour vanishes" (property $C$). Combine with property $D$: two closed contours $\gamma_0$ and $\gamma_1$ in $U$ that are homotopic in $U$ with $\gamma_1 - \gamma_0 = \partial D$. Then $\oint_{\gamma_1}f\,dz - \oint_{\gamma_0}f\,dz = \int_D d(f\,dz) = 0$. The result $E$ is that contour integrals of $f\,dz$ depend only on the *homology class* of the contour — the **homotopy invariance** of contour integrals, which is the path-independence of Cauchy theory restated for cycles. This is exactly [[Thm - Homotopy Invariance of de Rham Cohomology]] applied to the complex-valued $1$-form $f\,dz$.

---

# Why Is It True

**The mechanism in one line: the Cauchy–Riemann equations are literally the closedness condition $d(f(z)\,dz) = 0$, and Stokes's theorem then turns the closed-form identity into the contour-integral identity.**

The setup is the simplest one can imagine. On the complex plane $\mathbb{C} \cong \mathbb{R}^2$, write the standard coordinates as $(x, y)$ or equivalently $(z, \bar z)$ via $z = x + iy$, $\bar z = x - iy$. The complex-valued $1$-forms $dz = dx + i\,dy$ and $d\bar z = dx - i\,dy$ are a basis for the complex $1$-forms at each point, and any complex-valued $1$-form is a combination $p(z, \bar z)\,dz + q(z, \bar z)\,d\bar z$.

Now consider the special $1$-form $\omega = f(z)\,dz$ — a *pure* $dz$ form, with no $d\bar z$ piece. Its exterior derivative is computed by Leibniz and the standard rules. We get
$$d\omega = df\wedge dz = \left(\frac{\partial f}{\partial z}\,dz + \frac{\partial f}{\partial\bar z}\,d\bar z\right)\wedge dz = \frac{\partial f}{\partial\bar z}\,d\bar z\wedge dz,$$
using $dz\wedge dz = 0$. So $d\omega = 0$ if and only if $\partial f/\partial\bar z = 0$. This is the Cauchy–Riemann equations, repackaged: the real and imaginary parts of $\partial f/\partial\bar z = 0$ are exactly the two classical Cauchy–Riemann equations.

So holomorphy of $f$ and closedness of $f\,dz$ are literally the same condition, with the only difference being notational. In particular, every holomorphic $f$ gives a closed $1$-form $f\,dz$.

Stokes's theorem now finishes the argument. For a closed contour $\gamma$ bounding a $2$-chain $D$ in $U$,
$$\oint_\gamma f\,dz = \int_{\partial D}f\,dz = \int_D d(f\,dz) = \int_D 0 = 0.$$

That's the whole proof. Three lines, including the definition of $d(f\,dz)$. The classical Goursat-triangle / open-disc / star-shaped-domain proofs of Cauchy's theorem are all elaborate substitutes for the single observation "Stokes's theorem on a closed $1$-form vanishes when the contour bounds a $2$-chain inside the domain."

Why this is *deeper* than the classical proofs: it makes precise that "Cauchy's theorem" is not a theorem about complex functions specifically — it is Stokes's theorem in disguise, with the holomorphy condition playing the role of "the $1$-form is closed." The classical statement "$f$ holomorphic implies $\oint_\gamma f\,dz = 0$" becomes the structurally cleaner "$f\,dz$ closed implies $\oint_\gamma f\,dz = \int d(f\,dz) = 0$ for $\gamma$ bounding a $2$-chain." The latter is true *by definition of $d$*. The former is a corollary.

---

# What Makes This Hard

The conceptual obstacle is the unfamiliarity of complex-valued differential forms. Most readers first see $f(z)\,dz$ as "an integrand for a contour integral" rather than as a genuine $1$-form on $\mathbb{R}^2 \cong \mathbb{C}$ with $\mathbb{C}$-valued coefficient — i.e., as a section of the complexified cotangent bundle $T^*\mathbb{R}^2\otimes\mathbb{C}$. Without this perspective, the equation $d(f\,dz) = (\partial f/\partial\bar z)\,d\bar z\wedge dz$ is opaque. The computational obstacle is the wedge-product algebra: one must remember $dz\wedge dz = 0$, $d\bar z\wedge dz = -dz\wedge d\bar z$, and that $\partial/\partial\bar z$ is defined so that $\partial z/\partial\bar z = 0$. None of these is hard individually, but together they trip readers who have not internalized the form-language version of complex calculus.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Compute $d(f(z)\,dz)$ using the Wirtinger basis $(dz, d\bar z)$ on $\mathbb{C} \cong \mathbb{R}^2$, observe that the result is $(\partial f/\partial\bar z)\,d\bar z\wedge dz$, recognize $\partial f/\partial\bar z = 0$ as the Cauchy–Riemann equations / holomorphy condition, and apply Stokes.

**Subgoal decomposition:**

1. **Set up the complex $1$-form algebra.** Verify the identities $dz\wedge dz = 0$, $d\bar z\wedge d\bar z = 0$, and $dz\wedge d\bar z = -2i\,dx\wedge dy$. Express $df$ in the $(dz, d\bar z)$ basis using the Wirtinger derivatives.
   - *Hint:* Substitute $dz = dx + i\,dy$, $d\bar z = dx - i\,dy$ into each wedge.
   - *Why needed:* The whole computation is in the $(dz, d\bar z)$ basis, which is the natural basis for complex forms.

2. **Compute $d(f\,dz)$.** Apply $d$ using the graded Leibniz rule: $d(f\,dz) = df\wedge dz$ (because $d(dz) = 0$).
   - *Hint:* The $dz\wedge dz$ term in $df\wedge dz$ vanishes; only the $d\bar z\wedge dz$ term survives.
   - *Why needed:* This produces the explicit coefficient $\partial f/\partial\bar z$.

3. **Identify holomorphy.** Recognize $\partial f/\partial\bar z = 0$ as the Cauchy–Riemann equations / holomorphy condition.
   - *Hint:* Write $f = a + ib$ and unpack $\partial f/\partial\bar z = \tfrac{1}{2}(\partial f/\partial x + i\partial f/\partial y) = \tfrac{1}{2}((\partial a/\partial x - \partial b/\partial y) + i(\partial b/\partial x + \partial a/\partial y))$. Setting real and imaginary parts to zero gives the two Cauchy–Riemann equations.
   - *Why needed:* This makes the equivalence "$f$ holomorphic $\iff$ $f\,dz$ closed" explicit.

4. **Apply Stokes.** For $\gamma = \partial D$ in $U$, write $\oint_\gamma f\,dz = \int_D d(f\,dz) = 0$.
   - *Hint:* Stokes's theorem $\int_{\partial D}\omega = \int_D d\omega$ applied to $\omega = f\,dz$.
   - *Why needed:* This delivers the contour-integral statement of Cauchy's theorem.

5. **(Simple connectivity for the classical form.)** A simply connected domain has the property that every closed curve bounds a $2$-chain in the domain; together with Step 4, this gives the classical statement.
   - *Hint:* In $\mathbb{R}^2$, simple connectivity is equivalent to "every closed curve bounds an oriented $2$-chain." On a general manifold the relevant property is "the curve is null-homologous."
   - *Why needed:* Reduces the form-language statement to the textbook complex-analysis statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: The Wirtinger-basis wedge identities
> **Statement:** $dz\wedge dz = 0$, $d\bar z\wedge d\bar z = 0$, $dz\wedge d\bar z = -2i\,dx\wedge dy$, and $df = (\partial f/\partial z)\,dz + (\partial f/\partial\bar z)\,d\bar z$ for any $C^1$ function $f$.
>
> **Hint:** Substitute $dz = dx + i\,dy$ and $d\bar z = dx - i\,dy$ directly into each wedge expression. For the $df$ formula, invert the linear change of basis from $(dx, dy)$ to $(dz, d\bar z)$.
>
> **Why needed:** The whole proof of Cauchy's theorem is one wedge computation; without these basis identities the computation can't be done.
>
> > [!note]- Full proof
> > *Wedge identities.* Expand $dz \wedge dz = (dx + i\,dy)\wedge(dx + i\,dy) = dx\wedge dx + i(dx\wedge dy + dy\wedge dx) - dy\wedge dy = 0 + i(dx\wedge dy - dx\wedge dy) + 0 = 0$, using $dx\wedge dx = 0 = dy\wedge dy$ and $dy\wedge dx = -dx\wedge dy$.
> >
> > Similarly $d\bar z\wedge d\bar z = 0$. For the cross product, $dz\wedge d\bar z = (dx + i\,dy)\wedge(dx - i\,dy) = dx\wedge dx - i\,dx\wedge dy + i\,dy\wedge dx + dy\wedge dy = 0 - i\,dx\wedge dy - i\,dx\wedge dy + 0 = -2i\,dx\wedge dy$.
> >
> > *$df$ in the $(dz, d\bar z)$ basis.* From $dz = dx + i\,dy$ and $d\bar z = dx - i\,dy$, solve $dx = (dz + d\bar z)/2$ and $dy = (dz - d\bar z)/(2i)$. Then $df = (\partial f/\partial x)\,dx + (\partial f/\partial y)\,dy = (\partial f/\partial x)(dz + d\bar z)/2 + (\partial f/\partial y)(dz - d\bar z)/(2i)$.
> >
> > Grouping the coefficient of $dz$: $(\partial f/\partial x)/2 + (\partial f/\partial y)/(2i) = (\partial f/\partial x)/2 - i(\partial f/\partial y)/2 = (\partial/\partial z) f$ by definition.
> >
> > Grouping the coefficient of $d\bar z$: $(\partial f/\partial x)/2 - (\partial f/\partial y)/(2i) = (\partial f/\partial x)/2 + i(\partial f/\partial y)/2 = (\partial/\partial\bar z)f$.
> >
> > Hence $df = (\partial f/\partial z)\,dz + (\partial f/\partial\bar z)\,d\bar z$, as claimed.

> [!note]- Lemma 2: $d(f\,dz) = (\partial f/\partial\bar z)\,d\bar z\wedge dz$
> **Statement:** For any $C^1$ function $f$ on an open set $U \subseteq \mathbb{C}$, $d(f(z)\,dz) = (\partial f/\partial\bar z)\,d\bar z\wedge dz$.
>
> **Hint:** Apply $d$ as a graded antiderivation: $d(f\,dz) = df\wedge dz + f\,d(dz) = df\wedge dz$ since $d^2 = 0$ gives $d(dz) = 0$. Use Lemma 1 to expand $df$, and observe $dz\wedge dz = 0$.
>
> **Why needed:** This is the central computation showing closedness of $f\,dz$ is exactly the Cauchy–Riemann condition.
>
> > [!note]- Full proof
> > By the graded Leibniz rule, $d(f\,dz) = df\wedge dz - f\wedge d(dz)$. Since $d^2 = 0$ applied to the coordinate function $z$ gives $d(dz) = 0$, the second term vanishes. By Lemma 1, $df = (\partial f/\partial z)\,dz + (\partial f/\partial\bar z)\,d\bar z$. Substituting,
> > $$d(f\,dz) = \left[(\partial f/\partial z)\,dz + (\partial f/\partial\bar z)\,d\bar z\right]\wedge dz = (\partial f/\partial z)\,(dz\wedge dz) + (\partial f/\partial\bar z)\,d\bar z\wedge dz.$$
> > The first term vanishes by $dz\wedge dz = 0$ (Lemma 1). The remaining term is $(\partial f/\partial\bar z)\,d\bar z\wedge dz$, as claimed.

> [!note]- Lemma 3: $\partial f/\partial\bar z = 0$ is the Cauchy–Riemann equations
> **Statement:** For a $C^1$ function $f = a + ib$ on an open set in $\mathbb{C}$, the equation $\partial f/\partial\bar z = 0$ holds if and only if the real and imaginary parts satisfy the [[Thm - Cauchy–Riemann Equations|Cauchy–Riemann equations]]: $\partial a/\partial x = \partial b/\partial y$ and $\partial a/\partial y = -\partial b/\partial x$.
>
> **Hint:** Unpack $\partial f/\partial\bar z = \tfrac{1}{2}(\partial f/\partial x + i\,\partial f/\partial y)$ and substitute $f = a + ib$. Separate the real and imaginary parts.
>
> **Why needed:** Establishes that the closedness of $f\,dz$ is *exactly* the holomorphy condition, no more no less.
>
> > [!note]- Full proof
> > $$\frac{\partial f}{\partial\bar z} = \tfrac{1}{2}\left(\frac{\partial f}{\partial x} + i\,\frac{\partial f}{\partial y}\right) = \tfrac{1}{2}\left[\left(\frac{\partial a}{\partial x} + i\frac{\partial b}{\partial x}\right) + i\left(\frac{\partial a}{\partial y} + i\frac{\partial b}{\partial y}\right)\right] = \tfrac{1}{2}\left[\left(\frac{\partial a}{\partial x} - \frac{\partial b}{\partial y}\right) + i\left(\frac{\partial b}{\partial x} + \frac{\partial a}{\partial y}\right)\right].$$
> > Setting this to zero requires both the real and imaginary parts to vanish:
> > $$\frac{\partial a}{\partial x} = \frac{\partial b}{\partial y}, \qquad \frac{\partial a}{\partial y} = -\frac{\partial b}{\partial x}.$$
> > These are the classical Cauchy–Riemann equations.

---

# Formal Proof

> [!note]- Complete formal proof
> *Theorem.* Let $f : U \to \mathbb{C}$ be holomorphic on an open set $U \subseteq \mathbb{C}$, and let $D \subseteq U$ be a compact oriented $2$-chain with boundary $\partial D = \gamma$ a piecewise-smooth closed contour. Then $\oint_\gamma f(z)\,dz = 0$.
>
> *Proof.* The $1$-form $\omega = f(z)\,dz$ is a smooth complex-valued $1$-form on $U$ (smooth because $f$ is $C^1$, indeed $C^\infty$ since holomorphic functions are smooth). By Lemma 2, $d\omega = (\partial f/\partial\bar z)\,d\bar z\wedge dz$. By Lemma 3, the assumption $f$ is holomorphic gives $\partial f/\partial\bar z = 0$ on $U$, so $d\omega = 0$ throughout $U$. The $1$-form $\omega$ is closed on $U$.
>
> By Stokes's theorem ([[Thm - Stokes' Theorem on Manifolds]]) applied to the compact oriented $2$-chain $D$ and the smooth complex-valued $1$-form $\omega$,
> $$\oint_\gamma\omega = \int_{\partial D}\omega = \int_D d\omega = \int_D 0 = 0.$$
> The complex-valued Stokes's theorem is the usual one applied to the real and imaginary parts of $\omega$ separately. $\qquad\blacksquare$
>
> *Corollary.* If $U$ is simply connected and $f$ is holomorphic on $U$, then $\oint_\gamma f(z)\,dz = 0$ for every closed contour $\gamma$ in $U$.
>
> *Proof.* In a simply connected planar domain, every closed contour bounds an oriented $2$-chain in the domain. Apply the theorem with $D$ this $2$-chain. $\qquad\blacksquare$
>
> *Converse.* If $f$ is $C^1$ on $U$ and $f(z)\,dz$ is closed on $U$, then $f$ is holomorphic.
>
> *Proof.* By Lemma 2, closedness of $f\,dz$ means $(\partial f/\partial\bar z)\,d\bar z\wedge dz = 0$, hence $\partial f/\partial\bar z = 0$ everywhere on $U$. By Lemma 3, this is the Cauchy–Riemann equations, which is the definition of holomorphy for a $C^1$ function. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemann surfaces: holomorphic forms.** On a Riemann surface $X$ (a $1$-dimensional complex manifold), a **holomorphic $1$-form** is a smooth $\mathbb{C}$-valued $1$-form of type $(1, 0)$ (i.e. proportional to $dz$ in each holomorphic chart, with no $d\bar z$ component) that is closed. The theorem above generalizes verbatim: every closed contour bounding a $2$-chain on $X$ gives a vanishing contour integral. On a *compact* Riemann surface of genus $g$, the space of holomorphic $1$-forms is $g$-dimensional — and this single fact is the gateway into the Riemann–Roch theorem and the Abel–Jacobi map. Each holomorphic $1$-form is a "Cauchy-theorem object", and the dimensionality is set by the topology. See **Algebraic Topology I — [[Def - Singular Homology|Singular Homology]] and [[Thm - The de Rham Theorem (Statement)|the de Rham Theorem]]** for the genus formula.

**Several complex variables: Dolbeault cohomology.** In $\mathbb{C}^n$ with coordinates $(z^1, \dots, z^n)$, decompose the exterior derivative as $d = \partial + \bar\partial$, where $\partial$ raises the $dz$-degree and $\bar\partial$ raises the $d\bar z$-degree. A function $f$ is holomorphic if and only if $\bar\partial f = 0$, i.e. all $\partial f/\partial\bar z^i = 0$. The generalization of "$f\,dz$ is closed" is "the $(n, 0)$-form $f\,dz^1\wedge\cdots\wedge dz^n$ is $\bar\partial$-closed", and the corresponding cohomology theory is **Dolbeault cohomology** $H^{p,q}_{\bar\partial}(M)$ — the bigraded analogue of de Rham. The full theory underlies the Hodge decomposition on Kähler manifolds and the modern algebraic geometry of complex projective varieties.

**Linear functional analysis: holomorphic functional calculus.** For a bounded operator $T$ on a Banach space and a holomorphic function $f$ on a neighborhood of $\sigma(T)$ (the spectrum), define $f(T) := (2\pi i)^{-1}\oint_\gamma f(z)(zI - T)^{-1}\,dz$ for a contour $\gamma$ enclosing $\sigma(T)$. The fact that this definition is independent of the contour (any two homologous contours give the same $f(T)$) is **Cauchy's theorem in the operator-valued setting**: the form $f(z)(zI - T)^{-1}\,dz$ is operator-valued but its computation behaves identically. This gives the **holomorphic functional calculus** — a powerful tool in spectral theory and operator algebras.

**General relativity: Petrov classification and Weyl scalars.** In general relativity, the Weyl tensor $C_{abcd}$ on a Lorentzian $4$-manifold is decomposed into five complex Weyl scalars $\Psi_0, \dots, \Psi_4$ via contraction with a null tetrad. The closedness of certain complex Weyl-tensor-valued $2$-forms — the *Bianchi identity* in spinor form — generalizes Cauchy's integral theorem to spinor analysis on spacetime. Petrov classification of gravitational fields uses this structure to classify possible asymptotic behaviors of solutions to the Einstein equations.

---

# Bridges

- **[[Thm - Stokes' Theorem on Manifolds]]** — Cauchy's theorem is one specific consequence of Stokes's theorem, namely the special case for the complex-valued $1$-form $f\,dz$ on a $2$-manifold. The Cauchy–Riemann equations are the closedness condition for this form. Stokes converts the closed-form identity into the contour-integral identity. This bridge collapses what looks like an analytic miracle into a one-line consequence of the fundamental theorem of calculus generalized to forms.

- **[[Thm - Cauchy's Theorem for Simply Connected Domains]]** — The classical complex-analysis statement of Cauchy's theorem, proved by Goursat-style approximation and exhaustion. The form-language proof above is a much shorter alternative. The two proofs prove the same theorem but illuminate it differently: the classical proof shows the result holds even for very irregular $f$ (only continuous with the integral round triangles vanishing), and is the foundational result of the [[Complex Analysis II — Cauchy's Theorem and its Consequences|Cauchy theory]]; the form-language proof shows the structural reason — closedness in de Rham.

- **[[Thm - Cauchy–Riemann Equations]]** — The Cauchy–Riemann equations are the *literal* coefficient computation of $d(f(z)\,dz) = 0$. The form-language perspective reveals them as a closedness condition rather than as an analytic curiosity. They are the simplest case of the **Dolbeault closedness** condition $\bar\partial f = 0$ on a complex manifold.

- **[[Thm - The Poincaré Lemma on a Star-Shaped Region]]** — Cauchy's theorem combined with the Poincaré lemma gives the existence of a *primitive* (antiderivative) for any holomorphic function on a simply connected domain. The Poincaré lemma says every closed form on a star-shaped (more generally contractible) domain is exact; applied to $f\,dz$ on a simply connected $U$, it produces $F$ with $dF = f\,dz$, i.e. a holomorphic primitive. This is the bridge from "contour integrals vanish" to "antiderivatives exist", which is the source of the [[Complex Analysis II — Cauchy's Theorem and its Consequences|Cauchy integral formula]] in the classical theory.

- **[[Def - Closed and Exact Forms]]** — In the form-language, "Cauchy's theorem" is "$f\,dz$ is closed iff $f$ is holomorphic, and closed forms have vanishing periods on null-homologous cycles." The richness of complex analysis on multiply-connected domains (the punctured plane, the annulus, doubly-periodic functions) is precisely the failure of "closed implies exact" in non-simply-connected domains — i.e., the non-triviality of $H^1_{dR}$.

---

# Unlocked by This

> [!tip] Residue Theorem *(from Complex Analysis)*
> Cauchy's theorem via Stokes immediately generalizes to functions with isolated singularities. The form $f(z)\,dz$ for $f$ meromorphic with simple poles at $z_1, \dots, z_k$ is closed on $U \setminus \{z_1, \dots, z_k\}$, but not on $U$. The integral around a small circle enclosing $z_j$ is $2\pi i\,\mathrm{Res}_{z_j}(f)$, and Cauchy's theorem applied to $U$ minus small discs around the poles gives the **residue formula** $\oint_\gamma f\,dz = 2\pi i\sum_j n(\gamma, z_j)\,\mathrm{Res}_{z_j}(f)$. This is the workhorse of contour integration in real analysis; see [[Complex Analysis III — Winding, Laurent, Residues]].

> [!tip] Dolbeault Cohomology and Hodge Theory on Complex Manifolds *(from Complex Geometry)*
> The form $f(z)\,dz$ on $\mathbb{C}$ is a $(1, 0)$-form, and "closed" decomposes into $\partial$-closed plus $\bar\partial$-closed. On a complex manifold of higher dimension, the analogous decomposition $d = \partial + \bar\partial$ gives rise to two new cohomology theories — **Dolbeault cohomology** $H^{p,q}_{\bar\partial}(M)$ — that combine to produce de Rham cohomology via the Hodge decomposition. On Kähler manifolds the Hodge decomposition $H^k_{dR}(M; \mathbb{C}) = \bigoplus_{p+q=k} H^{p,q}_{\bar\partial}(M)$ pins down the bigraded structure that distinguishes complex from real geometry. This is the field of **Hodge theory on complex manifolds**, central to modern algebraic geometry and string theory; see **Algebraic Topology I — Singular Homology and the de Rham Theorem** for the de Rham side and **Hodge Theory I — Harmonic Forms and the Hodge Decomposition** for the Kähler/Hodge side.

> [!tip] Holomorphic Functional Calculus *(from Operator Theory)*
> The Cauchy integral formula for a holomorphic function applied to a bounded operator $T$ with resolvent $(zI - T)^{-1}$ gives $f(T) = (2\pi i)^{-1}\oint_\gamma f(z)(zI - T)^{-1}\,dz$, and Cauchy's theorem in operator-valued form proves the calculus is well-defined (depends only on $f$ near $\sigma(T)$, not on $\gamma$). This is the **holomorphic functional calculus**, foundational to spectral theory of unbounded operators (functional calculus for self-adjoint operators) and to the theory of $C^*$-algebras and von Neumann algebras.
