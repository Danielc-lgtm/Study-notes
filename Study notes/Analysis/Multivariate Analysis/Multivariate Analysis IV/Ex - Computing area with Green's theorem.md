---
type: exercise
subject: multivariate-analysis
difficulty: "⭐"
prereqs:
  - "Thm - Green's Theorem"
  - "Def - Pullback of a Differential Form"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

1. Use the Green's-theorem area formula $\operatorname{area}(\Omega) = \tfrac12\oint_{\partial\Omega}(x\,dy - y\,dx)$ to compute the area enclosed by the ellipse parametrized by $\gamma(t) = (a\cos t,\ b\sin t)$, $t \in [0, 2\pi]$, with $a, b > 0$.
2. Use the same formula to compute the area enclosed by the astroid $\gamma(t) = (\cos^3 t,\ \sin^3 t)$, $t \in [0, 2\pi]$.
3. Verify, for the ellipse, that the alternative forms of the area formula — $\oint x\,dy$ and $-\oint y\,dx$ — give the same answer.

**Recall:**

![[Thm - Green's Theorem#Statement]]

The relevant consequence of [[Thm - Green's Theorem|Green's theorem]] is the **area corollary**: for a compact planar region $\Omega$ with piecewise-$C^1$ boundary traversed counterclockwise,
$$\operatorname{area}(\Omega) = \oint_{\partial\Omega} x\,dy = -\oint_{\partial\Omega} y\,dx = \frac{1}{2}\oint_{\partial\Omega}(x\,dy - y\,dx).$$
To evaluate $\oint_{\partial\Omega}$ along a parametrized curve $\gamma(t)$, [[Def - Pullback of a Differential Form|pull the form back]]: $x\,dy - y\,dx$ becomes $[\gamma_1(t)\gamma_2'(t) - \gamma_2(t)\gamma_1'(t)]\,dt$.

---

# Convergent Strategy

**Problem class.** A *routine application* problem: one theorem (the area corollary of Green's theorem), applied directly. The [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]] strategy records that area is best computed as a boundary integral when the boundary has a clean parametrization.

**Assumption pattern.** Each region is presented by a clean parametrization of its closed boundary curve. The recognizable feature: the region itself (an ellipse's interior, an astroid's interior) is awkward to integrate over directly, but its boundary is a single smooth curve with an explicit formula.

**Theorem routing.** The area corollary converts $\operatorname{area}(\Omega) = \iint_\Omega 1\,dA$ (a double integral) into $\tfrac12\oint_{\partial\Omega}(x\,dy - y\,dx)$ (a line integral). Pull the $1$-form back along $\gamma$ and integrate in $t$ from $0$ to $2\pi$.

**Key decision point.** The only decision is which version of the formula to use — $\oint x\,dy$, $-\oint y\,dx$, or the symmetric average — and the answer is: whichever makes the integrand simplest. Part 3 confirms they all agree, which is the content of Green's theorem (their difference is $\oint d(xy) = 0$ around a closed curve). The other thing to check is orientation: the parametrizations here are counterclockwise, so the formula applies with a $+$ sign.

---

# Legal Operations Used

1. **Apply the general Stokes theorem (here its Green's-theorem area corollary)** — converting the area to a boundary integral.
2. **Pull a form back along a parametrization** — converting $\oint_{\partial\Omega}(x\,dy - y\,dx)$ into an ordinary integral in $t$.

---

# Hints

> [!note]- Hint 1
> For the ellipse, substitute $x = a\cos t$, $y = b\sin t$ into $x\,dy - y\,dx$. Compute $dy = b\cos t\,dt$ and $dx = -a\sin t\,dt$, then form $x\,dy - y\,dx$ as an expression in $t\,dt$.

> [!note]- Hint 2
> For the astroid, the same substitution: $x = \cos^3 t$, $y = \sin^3 t$. Compute $dx$ and $dy$ by the chain rule, then $x\,dy - y\,dx$. The resulting integrand simplifies using $\cos^2 t + \sin^2 t = 1$.

> [!note]- Hint 3
> For the ellipse with $\oint x\,dy$ alone: this is $\int_0^{2\pi}(a\cos t)(b\cos t)\,dt = ab\int_0^{2\pi}\cos^2 t\,dt$. Recall $\int_0^{2\pi}\cos^2 t\,dt = \pi$.

> [!note]- Hint 4
> The three versions of the formula must agree because their pairwise differences are $\oint d(xy)$, the integral of an exact form around a closed curve, which is zero by Green's theorem (or the Fundamental Theorem of Calculus).

---

# Solution

The area corollary turns each area into a one-variable integral over $[0, 2\pi]$. The pullback of $x\,dy - y\,dx$ along $\gamma$ does all the work.

**Step 1: area of the ellipse.**

$$\operatorname{area} = \frac{1}{2}\oint(x\,dy - y\,dx) = \frac{1}{2}\int_0^{2\pi} ab\,dt = \pi ab.$$

> [!note]- Derivation
> Along $\gamma(t) = (a\cos t, b\sin t)$: $x = a\cos t$, $y = b\sin t$, so
> $$dx = -a\sin t\,dt, \qquad dy = b\cos t\,dt.$$
> Form the pulled-back integrand:
> $$x\,dy - y\,dx = (a\cos t)(b\cos t\,dt) - (b\sin t)(-a\sin t\,dt) = ab\cos^2 t\,dt + ab\sin^2 t\,dt = ab\,dt.$$
> The $1$-form pulls back to the constant $ab\,dt$ — the cross-term structure of $x\,dy - y\,dx$ collapses via $\cos^2 + \sin^2 = 1$. Hence
> $$\operatorname{area} = \frac{1}{2}\int_0^{2\pi} ab\,dt = \frac{1}{2}\cdot ab\cdot 2\pi = \pi ab.$$
> For $a = b = r$ this is $\pi r^2$, the area of a disk — a sanity check. The parametrization runs counterclockwise (as $t$ increases the point sweeps counterclockwise), so the area corollary applies with a $+$ sign and the answer is positive.

**Step 2: area of the astroid.**

$$\operatorname{area} = \frac{1}{2}\int_0^{2\pi} 3\cos^2 t\sin^2 t\,dt = \frac{3\pi}{8}.$$

> [!note]- Derivation
> Along $\gamma(t) = (\cos^3 t, \sin^3 t)$: by the chain rule,
> $$dx = 3\cos^2 t\cdot(-\sin t)\,dt = -3\cos^2 t\sin t\,dt, \qquad dy = 3\sin^2 t\cos t\,dt.$$
> Form the integrand:
> $$x\,dy - y\,dx = \cos^3 t\cdot(3\sin^2 t\cos t)\,dt - \sin^3 t\cdot(-3\cos^2 t\sin t)\,dt$$
> $$= 3\cos^4 t\sin^2 t\,dt + 3\sin^4 t\cos^2 t\,dt = 3\cos^2 t\sin^2 t\,(\cos^2 t + \sin^2 t)\,dt = 3\cos^2 t\sin^2 t\,dt.$$
> So
> $$\operatorname{area} = \frac{1}{2}\int_0^{2\pi} 3\cos^2 t\sin^2 t\,dt.$$
> Evaluate the integral: $\cos^2 t\sin^2 t = \tfrac14\sin^2(2t) = \tfrac18(1 - \cos 4t)$. Hence $\int_0^{2\pi}\cos^2 t\sin^2 t\,dt = \tfrac18\int_0^{2\pi}(1 - \cos 4t)\,dt = \tfrac18\cdot 2\pi = \tfrac{\pi}{4}$. Therefore
> $$\operatorname{area} = \frac{1}{2}\cdot 3\cdot\frac{\pi}{4} = \frac{3\pi}{8}.$$
> The astroid encloses area $3\pi/8$ — smaller than the unit disk's $\pi$, as the inward-cusped shape should be.

**Step 3: the three forms of the formula agree (ellipse).**

$$\oint x\,dy = \pi ab, \qquad -\oint y\,dx = \pi ab, \qquad \frac{1}{2}\oint(x\,dy - y\,dx) = \pi ab.$$

> [!note]- Derivation
> *Using $\oint x\,dy$.* From Step 1, $x\,dy = (a\cos t)(b\cos t\,dt) = ab\cos^2 t\,dt$, so $\oint x\,dy = ab\int_0^{2\pi}\cos^2 t\,dt = ab\cdot\pi = \pi ab$.
>
> *Using $-\oint y\,dx$.* From Step 1, $y\,dx = (b\sin t)(-a\sin t\,dt) = -ab\sin^2 t\,dt$, so $-\oint y\,dx = ab\int_0^{2\pi}\sin^2 t\,dt = ab\cdot\pi = \pi ab$.
>
> *The symmetric form* gave $\pi ab$ in Step 1. All three agree.
>
> *Why they must agree.* The difference between $\oint x\,dy$ and $-\oint y\,dx$ is $\oint(x\,dy + y\,dx) = \oint d(xy)$, since $d(xy) = x\,dy + y\,dx$. The form $d(xy)$ is *exact*, and the integral of an exact $1$-form around a *closed* curve is zero (by Green's theorem, or directly: $\oint d(xy) = [xy]$ evaluated around a closed loop $= 0$). So $\oint x\,dy = -\oint y\,dx$, and the symmetric formula $\tfrac12\oint(x\,dy - y\,dx)$ is their common value. The three forms are not three different formulas — they are one formula, with the freedom to add or subtract the exact form $\tfrac12 d(xy)$, which contributes nothing around a closed curve.

> [!note]- Complete formal solution
> **Ellipse.** $\gamma(t) = (a\cos t, b\sin t)$ gives $x\,dy - y\,dx = ab(\cos^2 t + \sin^2 t)\,dt = ab\,dt$, so $\operatorname{area} = \tfrac12\int_0^{2\pi} ab\,dt = \pi ab$.
>
> **Astroid.** $\gamma(t) = (\cos^3 t, \sin^3 t)$ gives $x\,dy - y\,dx = 3\cos^2 t\sin^2 t\,dt$, so $\operatorname{area} = \tfrac12\int_0^{2\pi} 3\cos^2 t\sin^2 t\,dt = \tfrac32\cdot\tfrac{\pi}{4} = \tfrac{3\pi}{8}$.
>
> **Agreement.** $\oint x\,dy = ab\int_0^{2\pi}\cos^2 t\,dt = \pi ab$ and $-\oint y\,dx = ab\int_0^{2\pi}\sin^2 t\,dt = \pi ab$; both equal the symmetric value, since their difference is $\oint d(xy) = 0$. $\blacksquare$

---

# Key Takeaways

**Area is a boundary integral — compute it by walking the boundary, not by filling the region.** The area corollary of Green's theorem turns the two-dimensional $\iint_\Omega 1\,dA$ into the one-dimensional $\tfrac12\oint_{\partial\Omega}(x\,dy - y\,dx)$, and the practical payoff is enormous whenever the region is awkward but its boundary is cleanly parametrized — which is the typical situation. An ellipse's interior is described by an inequality; its boundary is a single smooth curve. An astroid's interior is a strange cusped region; its boundary is one parametrized loop. In every such case, the area corollary moves the entire computation onto the boundary, where a parametrization reduces it to a one-variable integral. The trigger to internalize: *given a closed parametrized curve and asked for the area it encloses, never set up a double integral — pull $x\,dy - y\,dx$ back along the curve and integrate.* This is the principle behind the shoelace formula for polygons and the planimeter, and it generalizes to the volume formula $\operatorname{vol}(\Omega) = \tfrac1n\int_{\partial\Omega}(x\cdot\nu)\,dS$ from the divergence theorem.

**The freedom to add an exact form is the freedom to pick the simplest integrand.** The three versions of the area formula — $\oint x\,dy$, $-\oint y\,dx$, and their average — are all correct because they differ by $\oint d(xy)$, the integral of an exact form around a closed curve, which is zero. This is a small instance of a pervasive principle: whenever you integrate a closed form around a closed curve (or, more generally, over a boundary), you may freely add any exact form without changing the answer, because exact forms have zero period. The practical use is to *choose the representative that makes the integrand simplest*. For the ellipse, $x\,dy$ alone was as easy as the symmetric form; for other curves one version may collapse and another may not. The general lesson, carried forward to [[Ex - Circulation of a vector field via Stokes' theorem]] and to de Rham cohomology: when integrating over a cycle, you are really integrating a *cohomology class*, and you may replace the form by any other in its class — pick the convenient one.

**Trigonometric pullbacks collapse via the Pythagorean identity — expect the cross-terms to cancel.** In both the ellipse and the astroid, the pulled-back integrand $x\,dy - y\,dx$ started as a sum of two trigonometric products and collapsed dramatically: to the constant $ab\,dt$ for the ellipse, to $3\cos^2 t\sin^2 t\,dt$ for the astroid, each time because a factor $\cos^2 t + \sin^2 t$ appeared and equalled $1$. This is not luck — the combination $x\,dy - y\,dx$ is, up to scale, the angular form $d\theta$ met in [[Ex - Pulling back a differential form]] and [[Ex - A closed form that is not exact]], and it is *built* to interact cleanly with circular and radial parametrizations. When pulling $x\,dy - y\,dx$ back along any curve given in terms of $\cos t$ and $\sin t$, expect a Pythagorean cancellation to simplify the integrand substantially before you integrate; if it does not, recheck the algebra.
