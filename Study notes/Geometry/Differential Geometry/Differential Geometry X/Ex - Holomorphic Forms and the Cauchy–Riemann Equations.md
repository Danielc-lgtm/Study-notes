---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Closed and Exact Forms"
  - "Thm - Cauchy's Integral Theorem via Stokes"
tags: [geometry, differential-geometry, complex-analysis, cauchy-riemann]
---

# Problem Statement

Consider the complex plane $\mathbb{C}$ identified with $\mathbb{R}^2$ via $z = x + iy$, and a complex-valued $C^1$ function $f : U \to \mathbb{C}$ on an open set $U$. Decompose $f = a(x, y) + i\,b(x, y)$ with $a, b$ real $C^1$ functions on $U$.

**(a)** Compute the exterior derivative $d(f(z)\,dz)$ in terms of the partial derivatives of $a$ and $b$.

**(b)** Show that $d(f(z)\,dz) = 0$ on $U$ if and only if $a$ and $b$ satisfy the **Cauchy–Riemann equations**
$$\frac{\partial a}{\partial x} = \frac{\partial b}{\partial y}, \qquad \frac{\partial a}{\partial y} = -\frac{\partial b}{\partial x}.$$

**(c)** Re-derive the same result using the **Wirtinger derivatives** $\partial/\partial z$ and $\partial/\partial\bar z$, showing that $d(f(z)\,dz) = (\partial f/\partial\bar z)\,d\bar z\wedge dz$, hence closedness of $f(z)\,dz$ is equivalent to $\partial f/\partial\bar z = 0$.

**(d)** Verify with two concrete examples: (i) $f(z) = z^2 = (x^2 - y^2) + i(2xy)$ is holomorphic, so $d(z^2\,dz) = 0$. (ii) $f(z) = \bar z = x - iy$ is not holomorphic, so $d(\bar z\,dz) \neq 0$; compute it explicitly.

**Recall:**

The objects in play are complex-valued differential forms on $\mathbb{R}^2 \cong \mathbb{C}$, the exterior derivative on such forms, and the Cauchy–Riemann equations.

![[Def - Exterior Derivative on a Manifold#The Definition]]

The exterior derivative is $\mathbb{C}$-linear and extends to complex-valued forms by acting on real and imaginary parts separately. So for $f = a + ib$ and a real $1$-form $\omega$, $d(f\omega) = d(a\omega) + i\,d(b\omega) = (da + i\,db)\wedge\omega + (a + ib)\,d\omega$ by the graded Leibniz rule.

The complex-valued $1$-forms $dz = dx + i\,dy$ and $d\bar z = dx - i\,dy$ on $\mathbb{C} \cong \mathbb{R}^2$ form a basis (over $\mathbb{C}$) for complex-valued $1$-forms at each point. The wedge products are $dz\wedge dz = 0 = d\bar z\wedge d\bar z$ and $dz\wedge d\bar z = -2i\,dx\wedge dy$. Any complex-valued $1$-form decomposes as $p(z, \bar z)\,dz + q(z, \bar z)\,d\bar z$.

The **Wirtinger derivatives** are defined by
$$\frac{\partial}{\partial z} = \tfrac{1}{2}\left(\frac{\partial}{\partial x} - i\frac{\partial}{\partial y}\right), \qquad \frac{\partial}{\partial\bar z} = \tfrac{1}{2}\left(\frac{\partial}{\partial x} + i\frac{\partial}{\partial y}\right),$$
chosen so that $\partial z/\partial z = 1$, $\partial z/\partial\bar z = 0$, $\partial\bar z/\partial z = 0$, $\partial\bar z/\partial\bar z = 1$. They give $df = (\partial f/\partial z)\,dz + (\partial f/\partial\bar z)\,d\bar z$ in the $(dz, d\bar z)$ basis.

The **Cauchy–Riemann equations** $\partial a/\partial x = \partial b/\partial y$, $\partial a/\partial y = -\partial b/\partial x$ are the standard analytic conditions for a $C^1$ function $f = a + ib$ to be holomorphic ([[Thm - Cauchy–Riemann Equations]]).

---

# Convergent Strategy

**Problem class.** This is a *prove the equivalence of two characterizations of a structural condition* problem. The structural condition is "holomorphy" / "$f\,dz$ is closed" / "Cauchy–Riemann"; the exercise shows these three characterizations are literally the same equation in different notations. It is the prelude to [[Thm - Cauchy's Integral Theorem via Stokes]] which then plugs the closedness into Stokes to recover Cauchy's integral theorem.

**Assumption pattern.** The single hypothesis is "$f$ is $C^1$" — minimal smoothness, just enough for $d(f\,dz)$ to be defined. The exercise then derives the equivalence between three formulations: the *vector-calculus* one (Cauchy–Riemann equations on $a$, $b$), the *form-language* one ($d(f\,dz) = 0$), and the *Wirtinger* one ($\partial f/\partial\bar z = 0$). The first is in terms of the real coordinates $(x, y)$; the second uses complex-valued forms but real partial derivatives; the third uses the natural complex coordinates $(z, \bar z)$. All three are the same equation.

**Theorem routing.** No named theorem is invoked. The route is computational: (i) compute $df$ in the $(dx, dy)$ basis, (ii) apply the graded Leibniz rule to $d(f\,dz) = df\wedge dz$ (noting $d(dz) = 0$ by $d^2 = 0$), (iii) collect coefficients of $dx\wedge dy$ and identify Cauchy–Riemann, (iv) repeat in the $(dz, d\bar z)$ basis and identify $\partial f/\partial\bar z$, (v) check the two concrete examples.

**Key decision point.** The single non-obvious step is recognizing that the *coefficient* of $d\bar z\wedge dz$ in $d(f\,dz)$ is the Wirtinger derivative $\partial f/\partial\bar z$, and that this Wirtinger derivative encodes both real and imaginary Cauchy–Riemann equations in one complex equation. The alternative — staying in $(x, y)$ coordinates and writing two separate equations — works but obscures the unified structure. A reader who sees the Wirtinger derivative as "the operator that kills holomorphic functions" gains a powerful unifying perspective; without this recognition, the Cauchy–Riemann equations remain two unrelated equations.

---

# Legal Operations Used

This solution deploys the following legal operations:

1. **Apply the graded Leibniz rule for $d$** (a foundational rule from [[Def - Exterior Derivative on a Manifold]]). For complex-valued forms: $d(f\omega) = df\wedge\omega + f\,d\omega$ with $f$ a complex-valued function. The trigger is the need to compute $d$ of a product of a complex-valued function and a $1$-form.

2. **Use $d^2 = 0$** to kill the term $d(dz) = 0$ in $d(f\,dz)$. The trigger is the appearance of an iterated derivative; the resolution is that any closed form ($dz$ is exact, hence closed) is annihilated by $d$.

3. **Compute wedges in the complex basis $(dz, d\bar z)$.** The non-trivial identities are $dz\wedge dz = 0$, $d\bar z\wedge d\bar z = 0$, and $dz\wedge d\bar z = -2i\,dx\wedge dy$. Use them to simplify $df\wedge dz$.

4. **Convert between $(x, y)$ and $(z, \bar z)$ coordinates** via $dx = (dz + d\bar z)/2$, $dy = (dz - d\bar z)/(2i)$, $\partial/\partial z = \tfrac{1}{2}(\partial/\partial x - i\partial/\partial y)$, $\partial/\partial\bar z = \tfrac{1}{2}(\partial/\partial x + i\partial/\partial y)$. The trigger is wanting to express the same object in two equivalent bases.

---

# Hints

> [!note]- Hint 1
> Use the graded Leibniz rule and $d(dz) = 0$ (which is $d^2$ applied to $z$, since $dz$ is exact). So $d(f\,dz) = df\wedge dz$.

> [!note]- Hint 2
> Write $df = (\partial f/\partial x)\,dx + (\partial f/\partial y)\,dy$ and then expand $df\wedge dz = df\wedge(dx + i\,dy)$. Collect the coefficient of $dx\wedge dy$.

> [!note]- Hint 3
> For part (b), set the coefficient of $dx\wedge dy$ in $d(f\,dz)$ equal to zero. This gives one complex equation, which is two real equations — the Cauchy–Riemann equations on $a, b$.

> [!note]- Hint 4
> For part (c), use the alternative basis $(dz, d\bar z)$. Write $df = (\partial f/\partial z)\,dz + (\partial f/\partial\bar z)\,d\bar z$ (verify this is consistent with the $(dx, dy)$ form). Then $df\wedge dz$ has only the $d\bar z\wedge dz$ term because $dz\wedge dz = 0$.

> [!note]- Hint 5
> For part (d)(ii), use $f(z) = \bar z = x - iy$. Then $df = dx - i\,dy = d\bar z$. So $d(\bar z\,dz) = d\bar z\wedge dz = -dz\wedge d\bar z = 2i\,dx\wedge dy \neq 0$. Confirm via the Wirtinger calculation: $\partial\bar z/\partial\bar z = 1 \neq 0$, so $\bar z$ is not holomorphic.

---

# Solution

The proof breaks into three steps. Step 1 computes $d(f\,dz)$ in the real coordinate basis $(dx, dy)$ and reads off the coefficient of $dx\wedge dy$ as a combination of Cauchy–Riemann expressions. Step 2 repeats in the complex basis $(dz, d\bar z)$ and identifies the coefficient as the Wirtinger derivative $\partial f/\partial\bar z$. Step 3 verifies the two example computations.

**Step 1: $d(f\,dz)$ in real coordinates.**

By the graded Leibniz rule and $d(dz) = 0$,
$$d(f\,dz) = df\wedge dz = [(\partial f/\partial x)\,dx + (\partial f/\partial y)\,dy]\wedge[dx + i\,dy].$$
Expanding the wedge,
$$d(f\,dz) = i(\partial f/\partial x)\,dx\wedge dy + (\partial f/\partial y)\,dy\wedge dx = [i(\partial f/\partial x) - (\partial f/\partial y)]\,dx\wedge dy.$$
Substituting $f = a + ib$ gives the coefficient
$$i(\partial f/\partial x) - (\partial f/\partial y) = i(\partial a/\partial x + i\partial b/\partial x) - (\partial a/\partial y + i\partial b/\partial y) = -(\partial a/\partial y + \partial b/\partial x) + i(\partial a/\partial x - \partial b/\partial y).$$

> [!note]- Derivation
> Compute $df = (\partial a/\partial x + i\partial b/\partial x)\,dx + (\partial a/\partial y + i\partial b/\partial y)\,dy$. Now wedge with $dz = dx + i\,dy$:
> $$df\wedge dz = (a_x + ib_x)\,dx\wedge dz + (a_y + ib_y)\,dy\wedge dz.$$
> $dx\wedge dz = dx\wedge(dx + i\,dy) = 0 + i\,dx\wedge dy = i\,dx\wedge dy$.
> $dy\wedge dz = dy\wedge(dx + i\,dy) = dy\wedge dx + 0 = -dx\wedge dy$.
>
> Substituting,
> $$df\wedge dz = i(a_x + ib_x)\,dx\wedge dy - (a_y + ib_y)\,dx\wedge dy = [i(a_x + ib_x) - (a_y + ib_y)]\,dx\wedge dy.$$
> Expanding the bracketed coefficient:
> $$i(a_x + ib_x) - (a_y + ib_y) = (ia_x - b_x) - (a_y + ib_y) = -(b_x + a_y) + i(a_x - b_y).$$
> So $d(f\,dz) = [-(b_x + a_y) + i(a_x - b_y)]\,dx\wedge dy$, where subscripts denote partial derivatives.

**Step 2: Closedness $\iff$ Cauchy–Riemann (part b).**

The coefficient of $dx\wedge dy$ in $d(f\,dz)$ is $-(b_x + a_y) + i(a_x - b_y)$. This is zero if and only if both
$$a_x = b_y \quad\text{and}\quad a_y = -b_x,$$
which are the Cauchy–Riemann equations. Hence $d(f\,dz) = 0 \iff f$ holomorphic.

> [!note]- Derivation
> A complex number $u + iv = 0$ iff $u = 0$ and $v = 0$. Apply to the coefficient:
> $$-(b_x + a_y) = 0 \;\text{and}\; a_x - b_y = 0,$$
> i.e.
> $$a_x = b_y \;\text{(the first Cauchy–Riemann equation)}\;\text{and}\;a_y = -b_x \;\text{(the second).}$$
> Conversely, if both hold then the coefficient is zero, so $d(f\,dz) = 0$.

**Step 3: $d(f\,dz)$ in the Wirtinger basis $(dz, d\bar z)$ (part c).**

Write $df = (\partial f/\partial z)\,dz + (\partial f/\partial\bar z)\,d\bar z$ — this is the change-of-basis formula for $df$ in the $(dz, d\bar z)$ basis. Then
$$d(f\,dz) = df\wedge dz = (\partial f/\partial z)(dz\wedge dz) + (\partial f/\partial\bar z)(d\bar z\wedge dz) = (\partial f/\partial\bar z)(d\bar z\wedge dz),$$
using $dz\wedge dz = 0$. So $d(f\,dz) = 0 \iff \partial f/\partial\bar z = 0$.

> [!note]- Derivation
> The basis identity $df = (\partial f/\partial z)\,dz + (\partial f/\partial\bar z)\,d\bar z$ follows from solving $dz = dx + i\,dy$, $d\bar z = dx - i\,dy$ for $dx, dy$ — giving $dx = (dz + d\bar z)/2$, $dy = (dz - d\bar z)/(2i) = -i(dz - d\bar z)/2$ — and substituting into $df = f_x\,dx + f_y\,dy$:
> $$df = f_x\cdot(dz + d\bar z)/2 + f_y\cdot(-i)(dz - d\bar z)/2 = \tfrac{1}{2}(f_x - if_y)\,dz + \tfrac{1}{2}(f_x + if_y)\,d\bar z = (\partial f/\partial z)\,dz + (\partial f/\partial\bar z)\,d\bar z.$$
>
> Now wedge with $dz$:
> $$df\wedge dz = (\partial f/\partial z)(dz\wedge dz) + (\partial f/\partial\bar z)(d\bar z\wedge dz).$$
> The first term vanishes since $dz\wedge dz = 0$. The second term is $(\partial f/\partial\bar z)(d\bar z\wedge dz)$.
>
> Sanity check: $d\bar z\wedge dz = -dz\wedge d\bar z = -(-2i\,dx\wedge dy) = 2i\,dx\wedge dy$. So $d(f\,dz) = (\partial f/\partial\bar z)\cdot 2i\,dx\wedge dy$. Compare to Step 1: the coefficient of $dx\wedge dy$ there was $-(b_x + a_y) + i(a_x - b_y)$. Compute $\partial f/\partial\bar z = \tfrac{1}{2}(f_x + if_y) = \tfrac{1}{2}((a_x + ib_x) + i(a_y + ib_y)) = \tfrac{1}{2}((a_x - b_y) + i(a_y + b_x))$. Multiplying by $2i$: $2i\cdot\partial f/\partial\bar z = i((a_x - b_y) + i(a_y + b_x)) = i(a_x - b_y) - (a_y + b_x)$, which matches the coefficient in Step 1. The two formulations agree.

**Step 4: Concrete examples (part d).**

*Example (i): $f(z) = z^2$.* In real coordinates, $z^2 = (x + iy)^2 = (x^2 - y^2) + i(2xy)$, so $a = x^2 - y^2$, $b = 2xy$. Then $a_x = 2x$, $b_y = 2x$ (so $a_x = b_y$ ✓), and $a_y = -2y$, $b_x = 2y$, so $a_y = -b_x$ ✓. Both Cauchy–Riemann equations are satisfied; $f$ is holomorphic; $d(z^2\,dz) = 0$.

In the Wirtinger calculation: $\partial f/\partial\bar z = \tfrac{1}{2}(f_x + if_y)$, $f_x = 2x + i\cdot 2y = 2(x + iy) = 2z$, $f_y = -2y + i\cdot 2x = 2i(x + iy) = 2iz$. Then $\partial f/\partial\bar z = \tfrac{1}{2}(2z + i\cdot 2iz) = \tfrac{1}{2}(2z - 2z) = 0$. So $f$ is holomorphic and $d(z^2\,dz) = 0$.

*Example (ii): $f(z) = \bar z$.* In real coordinates, $\bar z = x - iy$, so $a = x$, $b = -y$. Then $a_x = 1$, $b_y = -1$, so $a_x \neq b_y$. Cauchy–Riemann fails; $f$ is not holomorphic; $d(\bar z\,dz) \neq 0$.

Compute explicitly: $d\bar z = dx - i\,dy$, so $d(\bar z\,dz) = d\bar z\wedge dz = -dz\wedge d\bar z = -(- 2i\,dx\wedge dy) = 2i\,dx\wedge dy$. Confirming via Wirtinger: $\partial\bar z/\partial\bar z = 1$, so $d(\bar z\,dz) = 1\cdot d\bar z\wedge dz = 2i\,dx\wedge dy$. Matches.

> [!note]- Derivation
> For $f(z) = z^2$: differentiating directly, $f'(z) = 2z$, and a holomorphic function (with a complex derivative everywhere) automatically satisfies Cauchy–Riemann. Alternatively, the Wirtinger computation: $z^2$ as a function of $(z, \bar z)$ is independent of $\bar z$, so $\partial(z^2)/\partial\bar z = 0$ by definition of the Wirtinger derivative. So $d(z^2\,dz) = 0$.
>
> For $f(z) = \bar z$: this is the prototypical *anti*-holomorphic function. As a function of $(z, \bar z)$ it is $\bar z$ — depending *only* on $\bar z$ — so $\partial\bar z/\partial z = 0$ but $\partial\bar z/\partial\bar z = 1$. The exterior derivative $d\bar z = dx - i\,dy$ is precisely the basis $1$-form for $d\bar z$, so $d(\bar z\,dz) = d\bar z\wedge dz = -dz\wedge d\bar z = 2i\,dx\wedge dy$, a nowhere-vanishing $2$-form on $\mathbb{R}^2$.

> [!note]- Complete formal solution
> *(a)* Compute $d(f\,dz) = df\wedge dz$ (using $d^2 = 0$ to kill $d(dz)$). In real coordinates, $df = (\partial f/\partial x)\,dx + (\partial f/\partial y)\,dy = (a_x + ib_x)\,dx + (a_y + ib_y)\,dy$. Wedging with $dz = dx + i\,dy$ and using $dx\wedge dx = 0 = dy\wedge dy$ and $dy\wedge dx = -dx\wedge dy$,
> $$d(f\,dz) = [i(a_x + ib_x) - (a_y + ib_y)]\,dx\wedge dy = [-(b_x + a_y) + i(a_x - b_y)]\,dx\wedge dy.$$
>
> *(b)* The coefficient $-(b_x + a_y) + i(a_x - b_y)$ vanishes iff both $a_x = b_y$ and $a_y = -b_x$, i.e. iff the Cauchy–Riemann equations hold.
>
> *(c)* In the complex basis $(dz, d\bar z)$, $df = (\partial f/\partial z)\,dz + (\partial f/\partial\bar z)\,d\bar z$. Wedging with $dz$ and using $dz\wedge dz = 0$,
> $$d(f\,dz) = (\partial f/\partial\bar z)\,d\bar z\wedge dz.$$
> Closedness is equivalent to $\partial f/\partial\bar z = 0$, the Wirtinger form of the Cauchy–Riemann equations.
>
> *(d)*
>
> (i) $f = z^2$: as a function of $(z, \bar z)$, $f$ depends only on $z$, so $\partial f/\partial\bar z = 0$. Hence $d(z^2\,dz) = 0$. In real coordinates: $f = (x^2 - y^2) + i(2xy)$, $a = x^2 - y^2$, $b = 2xy$, with $a_x = 2x = b_y$ and $a_y = -2y = -b_x$. Cauchy–Riemann satisfied.
>
> (ii) $f = \bar z$: $\partial\bar z/\partial\bar z = 1$, so $d(\bar z\,dz) = 1\cdot d\bar z\wedge dz = 2i\,dx\wedge dy \neq 0$. In real coordinates: $a = x$, $b = -y$, with $a_x = 1$ but $b_y = -1$, violating the first Cauchy–Riemann equation. $\blacksquare$

> [!note]- Sanity check via independent route
> Verify by direct power-series argument: a holomorphic function has a convergent Taylor series $f(z) = \sum c_n(z - z_0)^n$ in any disc, and each $z^n$ is independent of $\bar z$, so $\partial f/\partial\bar z = 0$ for any holomorphic $f$. Conversely, $\partial f/\partial\bar z = 0$ on $U$ implies (by Wirtinger calculus or by the equivalent Cauchy–Riemann + smoothness implication) that $f$ admits a convergent Taylor expansion locally. So all three characterizations of holomorphy — $f\,dz$ closed, $\partial f/\partial\bar z = 0$, Cauchy–Riemann — agree with the power-series definition. The form-language characterization is the most useful for proving theorems via Stokes; the Cauchy–Riemann form is the most useful for computational verification; the Wirtinger form is the most useful for keeping track of the bidegree structure.

---

# Key Takeaways

**The Cauchy–Riemann equations are literally the closedness condition $d(f\,dz) = 0$ — there is no analytic miracle.** The classical statement of the Cauchy–Riemann equations as "the necessary and sufficient conditions for complex differentiability" treats them as a remarkable analytic fact requiring proof. The form-language perspective reveals them as a wedge-product computation: $df\wedge dz = (\partial f/\partial\bar z)\,d\bar z\wedge dz$, so $d(f\,dz) = 0$ iff $\partial f/\partial\bar z = 0$. Once you internalize that $\partial f/\partial\bar z = \tfrac{1}{2}(\partial a/\partial x - \partial b/\partial y) + i\tfrac{1}{2}(\partial a/\partial y + \partial b/\partial x)$, the two Cauchy–Riemann equations are just the two parts of "the coefficient of $d\bar z\wedge dz$ in $d(f\,dz)$ is zero." This is the highest-density compression of the Cauchy–Riemann equations: one form-language equation containing both real Cauchy–Riemann equations. The reusable principle: whenever a problem involves the Cauchy–Riemann equations in the classical guise, recasting them as "the form $f\,dz$ is closed" usually leads to a much cleaner proof — especially when the proof uses Stokes's theorem.

**Wirtinger calculus gives the right coordinates for complex analysis.** The Wirtinger derivatives $\partial/\partial z$ and $\partial/\partial\bar z$ are the natural derivatives in the complex coordinate system $(z, \bar z)$ on $\mathbb{C}$. They are defined precisely so that $\partial z/\partial z = 1$, $\partial z/\partial\bar z = 0$, etc., making the complex variables "behave like independent coordinates" even though $\bar z = \overline{z}$ is determined by $z$. The benefit is that complex differentiation becomes the partial derivative $\partial/\partial z$ with all expressions treating $\bar z$ as independent. Holomorphic functions are characterized by "no $\bar z$-dependence" ($\partial f/\partial\bar z = 0$); antiholomorphic functions by "no $z$-dependence" ($\partial f/\partial z = 0$). This split is unavailable in real-variable calculus, and it underlies the rich bigraded structure of complex differential geometry (the bidegree decomposition of forms into $(p, q)$-forms). On a complex manifold of [[Def - Dimension|dimension]] $n$, this decomposition splits the de Rham complex into the **Dolbeault complex** indexed by $(p, q)$, leading to the Hodge numbers $h^{p,q}$ — the master invariants of complex manifolds. The transferable insight: when working in complex geometry, always prefer the $(z, \bar z)$ coordinates over $(x, y)$; the algebra is cleaner and the geometric content (holomorphic vs antiholomorphic, $(p, q)$-bidegree) is automatic.

**$f(z) = \bar z$ is the prototypical non-holomorphic function — and $d(\bar z\,dz) = 2i\,dV$ is a quantitative measure of its non-holomorphy.** The example $f = \bar z$ illustrates the geometric meaning of failure of Cauchy–Riemann: the form $\bar z\,dz$ has exterior derivative $d\bar z\wedge dz = 2i\,dx\wedge dy$ — a constant nonzero $2$-form proportional to the area form. So $\bar z$ is "maximally non-holomorphic" in the sense that its non-holomorphy contributes uniformly across the plane. By contrast, a holomorphic function like $z^2$ has $d(z^2\,dz) = 0$ identically — zero contribution to non-holomorphy. The general lesson: $\partial f/\partial\bar z$ measures "how anti-holomorphic" $f$ is at each point. The integral $\int_D|\partial f/\partial\bar z|^2\,dV$ is the famous **Dirichlet energy** for the anti-holomorphic part, and minimizing it (subject to boundary conditions) is exactly the Cauchy problem of finding the "best" holomorphic approximation to $f$. This connects to **harmonic analysis** (the imaginary part of $-2i\partial f/\partial\bar z = i(\partial/\partial z - \partial/\partial\bar z)\bar f = i\Delta_{1/2}(\bar f)$ where $\Delta_{1/2}$ is the fractional Laplacian), to the **Cauchy problem for $\bar\partial$**, and to the construction of the **Bergman kernel** projecting onto holomorphic functions.

**Cauchy's integral theorem is now visible as Stokes plus the Cauchy–Riemann equations rephrased as closedness.** Once you have established the equivalence "$f$ holomorphic $\iff d(f\,dz) = 0$", Cauchy's integral theorem $\oint_\gamma f\,dz = 0$ for $\gamma$ bounding a $2$-chain follows immediately from Stokes: $\oint_\gamma f\,dz = \int_D d(f\,dz) = 0$. The full proof is two lines: the equivalence (this exercise) and Stokes ([[Thm - Stokes' Theorem on Manifolds]]). This is the [[Thm - Cauchy's Integral Theorem via Stokes|companion theorem to this exercise]], and it is the entry point to the whole of complex analysis. The takeaway: Cauchy's theorem is not a separate analytic insight — it is the special case of Stokes for a closed $1$-form on a $2$-manifold. Internalize the closedness perspective and the rest of Cauchy theory (the integral formula, the [[Def - Residue|residue]] theorem, Liouville's theorem, the maximum principle) unfolds as a sequence of Stokes-plus-algebra arguments.
