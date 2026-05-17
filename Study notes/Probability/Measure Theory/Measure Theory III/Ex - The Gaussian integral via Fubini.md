---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Fubini-Tonelli Theorem"
  - "Def - Lebesgue Measure"
tags: [analysis, measure-theory, probability]
---

# Problem Statement

Prove the **Gaussian integral identity**
$$\int_{\mathbb{R}}e^{-x^2/2}\,dx=\sqrt{2\pi}$$
by computing $I^2$, where $I=\int_\mathbb{R}e^{-x^2/2}\,dx$, as a double integral over $\mathbb{R}^2$ via [[Thm - Fubini-Tonelli Theorem|Tonelli]] and a polar-coordinates change of variables. Deduce that $f(x)=(2\pi)^{-1/2}e^{-x^2/2}$ is a probability density (the standard Gaussian).

**Recall:**

[[Thm - Fubini-Tonelli Theorem|Tonelli]]: for $g\ge0$ on $\mathbb{R}\times\mathbb{R}$, $\int g\,d\lambda_2=\iint g\,dx\,dy$. The polar change of variables: $dx\,dy=r\,dr\,d\theta$.

---

# Convergent Strategy

**Problem class:** evaluating a one-dimensional integral with no elementary antiderivative — by *lifting it to a product*.

**Assumption pattern:** $e^{-x^2/2}$ has no elementary primitive, so $I$ resists direct evaluation. But $I^2=\big(\int e^{-x^2/2}dx\big)\big(\int e^{-y^2/2}dy\big)$ factors as a *product*, which [[Thm - Fubini-Tonelli Theorem|Tonelli]] reassembles into a single integral over $\mathbb{R}^2$ of $e^{-(x^2+y^2)/2}$ — and *that* has rotational symmetry, so polar coordinates trivialise it.

**Theorem routing:** $I^2\xrightarrow{\text{Tonelli}}\int_{\mathbb{R}^2}e^{-(x^2+y^2)/2}\xrightarrow{\text{polar}}\int_0^{2\pi}\int_0^\infty e^{-r^2/2}r\,dr\,d\theta$.

**Key decision point:** squaring to get a product, the move that unlocks the symmetry.

---

# Legal Operations Used

1. **Square the integral** to factor it into a product.
2. **Tonelli** to merge two iterated integrals into a double integral.
3. **Polar change of variables.**

---

# Hints

> [!note]- Hint 1
> $I^2=\big(\int e^{-x^2/2}dx\big)\big(\int e^{-y^2/2}dy\big)$. The integrand $e^{-x^2/2}\cdot e^{-y^2/2}\ge0$ — Tonelli applies with no integrability check.

> [!note]- Hint 2
> $e^{-x^2/2}e^{-y^2/2}=e^{-(x^2+y^2)/2}$ depends only on $r^2=x^2+y^2$. Switch to polar.

> [!note]- Hint 3
> $\int_0^\infty e^{-r^2/2}r\,dr=[-e^{-r^2/2}]_0^\infty=1$.

---

# Solution

**Step 1 — Square and merge.** $I=\int_\mathbb{R}e^{-x^2/2}\,dx>0$. Then
$$I^2=\Big(\int_\mathbb{R}e^{-x^2/2}dx\Big)\Big(\int_\mathbb{R}e^{-y^2/2}dy\Big)=\int_\mathbb{R}\Big(\int_\mathbb{R}e^{-x^2/2}e^{-y^2/2}\,dx\Big)dy.$$
The integrand $e^{-(x^2+y^2)/2}\ge0$ is Borel measurable, so by [[Thm - Fubini-Tonelli Theorem|Tonelli]] this iterated integral equals the double integral over $\mathbb{R}^2$:
$$I^2=\int_{\mathbb{R}^2}e^{-(x^2+y^2)/2}\,d\lambda_2(x,y).$$

**Step 2 — Polar coordinates.** The map $(r,\theta)\mapsto(r\cos\theta,r\sin\theta)$ from $(0,\infty)\times(0,2\pi)$ to $\mathbb{R}^2$ (minus a null half-line) has Jacobian $r$, so $d\lambda_2=r\,dr\,d\theta$. Since $x^2+y^2=r^2$,
$$I^2=\int_0^{2\pi}\!\!\int_0^\infty e^{-r^2/2}\,r\,dr\,d\theta=\Big(\int_0^{2\pi}d\theta\Big)\Big(\int_0^\infty e^{-r^2/2}r\,dr\Big)=2\pi\cdot\big[-e^{-r^2/2}\big]_0^\infty=2\pi\cdot 1.$$
Hence $I^2=2\pi$ and, since $I>0$, $I=\sqrt{2\pi}$.

**Step 3 — The Gaussian density.** Therefore $\int_\mathbb{R}(2\pi)^{-1/2}e^{-x^2/2}\,dx=1$, so $f(x)=(2\pi)^{-1/2}e^{-x^2/2}\ge0$ integrates to $1$: it is a [[Def - Absolute Continuity and Density|probability density]], the **standard Gaussian** $N(0,1)$.

> [!note]- Complete formal solution
> $I^2=\iint e^{-x^2/2}e^{-y^2/2}dx\,dy=\int_{\mathbb{R}^2}e^{-(x^2+y^2)/2}d\lambda_2$ by Tonelli (non-negative integrand). Polar coordinates ($d\lambda_2=r\,dr\,d\theta$, $x^2+y^2=r^2$) give $I^2=\int_0^{2\pi}d\theta\int_0^\infty e^{-r^2/2}r\,dr=2\pi\cdot1=2\pi$, so $I=\sqrt{2\pi}$. Hence $(2\pi)^{-1/2}e^{-x^2/2}$ is a probability density. $\blacksquare$

---

# Key Takeaways

**An intractable one-dimensional integral can become trivial when *squared and lifted to a product* — the square factors into a product, Tonelli merges it into one double integral, and a symmetry invisible in 1-D appears in 2-D.** $e^{-x^2/2}$ has no elementary antiderivative, but $e^{-(x^2+y^2)/2}$ is rotationally symmetric, and polar coordinates exploit exactly that. The trigger-reaction: "a 1-D integral resists direct attack, but $f(x)f(y)$ has a symmetry" → square it, apply Tonelli, change variables.

**This computation certifies the Gaussian density and is the gateway to the [[Thm - Central Limit Theorem|central limit theorem]].** The normalising constant $(2\pi)^{-1/2}$ is *what this exercise computes*; without it the Gaussian is not a probability measure. The same square-and-go-to-polar device evaluates all Gaussian moment integrals and is the reason the Gaussian — uniquely — is its own [[Def - Characteristic Function|Fourier transform]] up to scaling, the analytic fact underpinning the CLT.
