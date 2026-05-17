---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Differential Form"
  - "Def - The Exterior Derivative"
  - "Def - Pullback of a Differential Form"
  - "Thm - The General Stokes Theorem"
  - "Thm - The Poincaré Lemma"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

On the punctured plane $U = \mathbb{R}^2\setminus\{0\}$, consider the **angular form**
$$\omega = \frac{x\,dy - y\,dx}{x^2 + y^2}.$$

1. Show that $\omega$ is **closed**: $d\omega = 0$ on all of $U$.
2. Compute the integral of $\omega$ around the unit circle, $\int_{S^1}\omega$, where $S^1$ is parametrized counterclockwise by $\gamma(t) = (\cos t, \sin t)$, $t \in [0, 2\pi]$.
3. Conclude that $\omega$ is **not exact** on $U$ — there is no smooth function $f$ on $U$ with $df = \omega$ — and explain why this does not contradict the [[Thm - The Poincaré Lemma|Poincaré lemma]].
4. Explain in what precise sense $\omega$ "is" the differential $d\theta$ of the angle, and why the angle is not a globally defined function on $U$.

**Recall:**

A form is **closed** if $d\omega = 0$ and **exact** if $\omega = d f$ for some $f$. By $d\circ d = 0$, every exact form is closed.

![[Thm - The Poincaré Lemma#Statement]]

The [[Thm - The Poincaré Lemma|Poincaré lemma]] gives the converse — closed implies exact — but *only on a contractible domain*. The punctured plane is not contractible.

![[Thm - The General Stokes Theorem#Statement]]

The key consequence of [[Thm - The General Stokes Theorem|Stokes' theorem]] used here: an exact $1$-form integrates to zero around any closed curve, because if $\omega = df$ then $\int_{\partial M}\omega = \int_M d(df) = 0$.

---

# Convergent Strategy

**Problem class.** A *structural / topological* problem: not "compute an integral" but "decide whether a form is exact", and the answer is negative. The [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]] strategy records that exactness is a two-step question — first closedness, then the topology of the domain — and this exercise is the canonical case where closedness holds but the topology obstructs.

**Assumption pattern.** The form is defined on a domain *with a hole* — the puncture at the origin. The recognizable signal that closedness will *not* be enough: the domain is not contractible. The hole is exactly where the obstruction to exactness will live.

**Theorem routing.** Part 1 is a direct computation of $d\omega$. Part 2 is a direct line integral. Part 3 is the contrapositive of a Stokes corollary: *exact $\Rightarrow$ zero period*, so *nonzero period $\Rightarrow$ not exact*. The nonzero number $2\pi$ from part 2, plugged into this contrapositive, is the entire proof of non-exactness.

**Key decision point.** The crux is realizing that computing $d\omega = 0$ does *not* settle exactness, and that the decisive computation is instead the *period* $\int_{S^1}\omega$. A reader who stops at "$d\omega = 0$, so by Poincaré $\omega = df$" has made exactly the error this exercise exists to expose: the Poincaré lemma's hypothesis — contractibility — fails on $U$, so closedness alone is worthless. The period integral is the meter that detects the hole.

---

# Legal Operations Used

1. **Compute $d$ of a form and watch for simplification** — part 1, verifying closedness.
2. **Pull a form back along a parametrization** — part 2, pulling $\omega$ back along $\gamma$ to compute the line integral.
3. **Test a form for closedness, then exactness** — the whole exercise is this two-step test, with the second step decided by the period.
4. **Apply Stokes' theorem (its corollary: exact forms have zero period)** — part 3, the contrapositive that converts the nonzero period into non-exactness.

---

# Hints

> [!note]- Hint 1
> For part 1, write $\omega = P\,dx + Q\,dy$ with $P = -y/(x^2+y^2)$ and $Q = x/(x^2+y^2)$. Closedness of a $1$-form means $\partial_x Q = \partial_y P$. Compute both partials with the quotient rule and compare.

> [!note]- Hint 2
> For part 2, pull $\omega$ back along $\gamma(t) = (\cos t, \sin t)$. On the unit circle, $x^2 + y^2 = 1$, so the denominator is just $1$. Compute $\gamma^*(x\,dy - y\,dx)$ — you should get a strikingly simple expression in $t$.

> [!note]- Hint 3
> For part 3, suppose for contradiction $\omega = df$. Then $\int_{S^1}\omega = \int_{S^1} df$. The unit circle is a *closed* curve (no boundary). What does Stokes' theorem — or directly the Fundamental Theorem of Calculus — say about $\int_{S^1} df$ for a closed curve?

> [!note]- Hint 4
> For part 4, in polar coordinates $x = r\cos\theta$, $y = r\sin\theta$, compute $d\theta$ by writing $\theta = \arctan(y/x)$ and differentiating — you will recover $\omega$ exactly. But $\theta$ itself is only defined up to adding multiples of $2\pi$: going once around the origin, $\theta$ increases by $2\pi$. So $d\theta$ is a perfectly good single-valued $1$-form even though $\theta$ is multi-valued.

---

# Solution

The form is closed everywhere on the punctured plane, but its integral around a loop encircling the puncture is $2\pi \neq 0$. Since an exact form has zero period around every loop, $\omega$ cannot be exact. The hole at the origin is the entire obstruction.

**Step 1: $\omega$ is closed.**

$$d\omega = 0 \quad\text{on all of } U = \mathbb{R}^2\setminus\{0\}.$$

> [!note]- Derivation
> Write $\omega = P\,dx + Q\,dy$ with
> $$P = \frac{-y}{x^2+y^2}, \qquad Q = \frac{x}{x^2+y^2}.$$
> A $1$-form $P\,dx + Q\,dy$ is closed exactly when $\partial_x Q = \partial_y P$ (this is $d\omega = (\partial_x Q - \partial_y P)\,dx\wedge dy = 0$).
>
> Compute $\partial_x Q$ by the quotient rule:
> $$\partial_x Q = \frac{1\cdot(x^2+y^2) - x\cdot 2x}{(x^2+y^2)^2} = \frac{y^2 - x^2}{(x^2+y^2)^2}.$$
> Compute $\partial_y P$:
> $$\partial_y P = \frac{-1\cdot(x^2+y^2) - (-y)\cdot 2y}{(x^2+y^2)^2} = \frac{-(x^2+y^2) + 2y^2}{(x^2+y^2)^2} = \frac{y^2 - x^2}{(x^2+y^2)^2}.$$
> The two are equal at every point of $U$. Hence $\partial_x Q - \partial_y P = 0$, so $d\omega = 0$: the form is closed throughout the punctured plane. (At the origin everything is undefined — but the origin is *not* in $U$, which is the whole point.)

**Step 2: the period $\int_{S^1}\omega = 2\pi$.**

$$\int_{S^1}\omega = \int_0^{2\pi} 1\;dt = 2\pi.$$

> [!note]- Derivation
> Parametrize the unit circle by $\gamma(t) = (\cos t, \sin t)$, $t \in [0, 2\pi]$, so $x = \cos t$, $y = \sin t$, and $x^2 + y^2 = 1$ identically on the circle.
>
> Pull $\omega$ back along $\gamma$. The numerator $x\,dy - y\,dx$ pulls back to
> $$\gamma^*(x\,dy - y\,dx) = \cos t\,d(\sin t) - \sin t\,d(\cos t) = \cos t\cdot\cos t\,dt - \sin t\cdot(-\sin t)\,dt = (\cos^2 t + \sin^2 t)\,dt = dt.$$
> The denominator $x^2 + y^2$ pulls back to $1$. Hence $\gamma^*\omega = dt$, and
> $$\int_{S^1}\omega = \int_0^{2\pi}\gamma^*\omega = \int_0^{2\pi} dt = 2\pi.$$
> The period of $\omega$ around a loop encircling the origin once, counterclockwise, is exactly $2\pi$. This number is the *winding number* of the loop times $2\pi$ — it counts how many times the curve goes around the puncture.

**Step 3: $\omega$ is not exact.**

The period $\int_{S^1}\omega = 2\pi \neq 0$ certifies that $\omega$ is **not exact** on $U$.

> [!note]- Derivation
> Suppose, for contradiction, that $\omega$ were exact: $\omega = df$ for some smooth $f : U \to \mathbb{R}$.
>
> The unit circle $S^1$ is a closed curve — it has no boundary, $\partial S^1 = \emptyset$. By the Fundamental Theorem of Calculus for line integrals (equivalently, [[Thm - The General Stokes Theorem|Stokes' theorem]] in dimension one), the integral of an exact $1$-form $df$ around any closed curve $\gamma$ is
> $$\int_\gamma df = f(\gamma(\text{end})) - f(\gamma(\text{start})) = 0,$$
> since for a closed curve the start and end points coincide. So *if* $\omega = df$, then $\int_{S^1}\omega = \int_{S^1} df = 0$.
>
> But Step 2 showed $\int_{S^1}\omega = 2\pi \neq 0$. Contradiction. Therefore no such $f$ exists: $\omega$ is **not exact** on $U$.
>
> *Why no contradiction with the Poincaré lemma.* The [[Thm - The Poincaré Lemma|Poincaré lemma]] says closed $\Rightarrow$ exact — but *only on a contractible domain*. The punctured plane $U = \mathbb{R}^2\setminus\{0\}$ is **not contractible**: it has a hole, and a loop around the hole cannot be shrunk to a point within $U$. So the lemma's hypothesis fails, and the lemma simply does not apply. There is no contradiction — $\omega$ is a closed form on a non-contractible domain, exactly the situation the lemma does not cover. On any *contractible* piece of $U$ — say the right half-plane $\{x > 0\}$ — the lemma *does* apply, and there $\omega$ *is* exact (a local primitive exists). What fails is the *gluing* of these local primitives into a global one, and the period $2\pi$ measures the failure.

**Step 4: $\omega$ is $d\theta$, and the angle is multi-valued.**

In polar coordinates, $\omega = d\theta$ where $\theta$ is the angular coordinate; the form $d\theta$ is single-valued and smooth on $U$, but $\theta$ itself is defined only modulo $2\pi$.

> [!note]- Derivation
> Introduce polar coordinates $x = r\cos\theta$, $y = r\sin\theta$. On the region where it is defined, the angle satisfies $\theta = \arctan(y/x)$ (with the appropriate branch). Differentiate:
> $$d\theta = \frac{\partial\theta}{\partial x}\,dx + \frac{\partial\theta}{\partial y}\,dy.$$
> With $\theta = \arctan(y/x)$, the chain rule gives $\partial_x\theta = \dfrac{1}{1+(y/x)^2}\cdot\big(-\dfrac{y}{x^2}\big) = \dfrac{-y}{x^2+y^2}$ and $\partial_y\theta = \dfrac{1}{1+(y/x)^2}\cdot\dfrac{1}{x} = \dfrac{x}{x^2+y^2}$. Hence
> $$d\theta = \frac{-y\,dx + x\,dy}{x^2+y^2} = \omega.$$
> So $\omega$ *is* the form $d\theta$ — the differential of the angle.
>
> Here is the subtlety. The *form* $d\theta$ is perfectly well-defined and smooth on all of $U$: the formula $(-y\,dx + x\,dy)/(x^2+y^2)$ has no ambiguity. But the *function* $\theta$ is not single-valued. As you travel once counterclockwise around the origin, the angle increases continuously from $\theta_0$ to $\theta_0 + 2\pi$ — it does not return to its starting value. There is no way to assign a single number $\theta(x,y)$ to every point of $U$ continuously; any attempt has a "jump" along some ray (a branch cut). The angle is well-defined only *modulo $2\pi$*, or only on a contractible sub-region.
>
> This is the precise resolution of the apparent paradox. "$\omega = d\theta$" looks like it exhibits $\omega$ as exact, with primitive $\theta$. But $\theta$ is not a function on $U$ — it is a *multi-valued* function, equivalently a function on the universal cover of $U$. The period $\int_{S^1}\omega = \int_{S^1} d\theta = 2\pi$ is exactly the total increase in the angle around one loop, the amount by which the multi-valued $\theta$ fails to be single-valued. The form is exact "locally" (where a branch of $\theta$ can be chosen) but not "globally" (where no consistent branch exists), and $2\pi$ is the size of the inconsistency.

> [!note]- Complete formal solution
> **Closed.** With $P = -y/(x^2+y^2)$, $Q = x/(x^2+y^2)$, the quotient rule gives $\partial_x Q = \partial_y P = (y^2-x^2)/(x^2+y^2)^2$, so $d\omega = (\partial_x Q - \partial_y P)\,dx\wedge dy = 0$ on $U$.
>
> **Period.** Along $\gamma(t) = (\cos t, \sin t)$, $x^2+y^2 = 1$ and $\gamma^*(x\,dy-y\,dx) = (\cos^2 t + \sin^2 t)\,dt = dt$, so $\int_{S^1}\omega = \int_0^{2\pi} dt = 2\pi$.
>
> **Not exact.** If $\omega = df$ then $\int_{S^1}\omega = \int_{S^1} df = 0$ since $S^1$ is closed; this contradicts $\int_{S^1}\omega = 2\pi$. So $\omega$ is not exact. No contradiction with the Poincaré lemma, whose contractibility hypothesis fails on the punctured plane.
>
> **Identification with $d\theta$.** In polar coordinates $\omega = d\theta$, but $\theta$ is multi-valued (increases by $2\pi$ per loop), so it is not a global primitive; the period $2\pi$ is exactly the monodromy of the angle. $\blacksquare$

---

# Key Takeaways

**Closedness is necessary for exactness but never sufficient on a domain with holes — the period is the decider.** The single most important lesson of this exercise, and a standing warning for the whole topic, is that "I computed $d\omega = 0$, therefore $\omega = df$" is a *fallacy* whenever the domain is not contractible. The Poincaré lemma's conclusion is hostage to its hypothesis. The correct procedure for deciding exactness on a domain with holes is two-step: first verify closedness (necessary, cheap), then compute the *periods* — the integrals of $\omega$ around loops encircling each hole. An exact form has every period zero, because Stokes makes $\int_{\text{loop}} df = 0$; so a single nonzero period is a complete, rigorous certificate of non-exactness. Whenever a problem asks "is this field conservative" or "does this form have a potential" and the domain has a puncture, a missing axis, or any hole, do not stop at $d\omega = 0$ — integrate around the hole.

**The angular form is the minimal model of a topological obstruction, and recognizing it is half the battle.** The form $(-y\,dx + x\,dy)/(x^2+y^2)$ — equivalently $d\theta$, equivalently, up to scale, the form $-y\,dx + x\,dy$ met in [[Ex - Pulling back a differential form]] — is *the* example of a closed-but-not-exact form, the generator of $H^1_{\mathrm{dR}}(\mathbb{R}^2\setminus\{0\})$. It encodes one hole, one obstruction, one number ($2\pi$). Any problem involving a planar field that blows up at a point, a domain with a removed point or removed axis, a winding number, or a multi-valued "angle"-like potential, is this example in disguise. The trigger to internalize: a denominator $x^2+y^2$ vanishing at an excluded point is the fingerprint of the angular form, and its presence signals that exactness will fail and the period will be a nonzero multiple of $2\pi$. Recognizing the angular form behind a disguised problem immediately tells you the answer is "not exact, period $2\pi k$".

**Local exactness versus global exactness — the gap is the shape of the domain, and that gap is de Rham cohomology.** This exercise dramatizes the difference between "exact near every point" and "exact on the whole domain". The form $\omega$ *is* exact on every contractible piece of $U$ — on the right half-plane, $\theta = \arctan(y/x)$ is a genuine primitive — but the local primitives, the local branches of the angle, cannot be glued into one global function, because going around the hole the branches disagree by $2\pi$. The Poincaré lemma is precisely the statement that the local obstruction always vanishes; the global obstruction is what survives, and it is a finite-dimensional invariant — here one-dimensional, generated by $[\omega]$ — called the first de Rham cohomology group. This is the cleanest finite model of a pervasive phenomenon: locally consistent data (local primitives, local sections, local coordinate descriptions) may fail to assemble into a global object, and the failure is measured by a cohomology class. The period integral $2\pi$ is the cost of going global; it is zero exactly when the local-to-global passage is free, and its nonvanishing is a hard, computable obstruction — the prototype every later cohomological obstruction is modeled on.
