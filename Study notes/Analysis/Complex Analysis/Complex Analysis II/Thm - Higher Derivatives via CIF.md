---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Cauchy Integral Formula"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Notation

$f : D(a, R) \to \mathbb{C}$ holomorphic; $w \in D(a, \rho)$ with $\rho < R$; $n \geq 0$ integer. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Motivation

The Cauchy integral formula expresses $f(w)$ as a contour integral over a surrounding circle. Differentiating both sides with respect to $w$ — under the integral sign — gives an integral representation for $f'(w)$, $f''(w)$, and all higher derivatives. The result:
$$f^{(n)}(w) = \frac{n!}{2\pi i}\oint_{|z - a| = \rho}\frac{f(z)}{(z - w)^{n+1}}\,dz.$$
The remarkable structural consequence: every holomorphic function is *automatically* infinitely differentiable. There is no "$C^1$ but not $C^2$" phenomenon in complex analysis — once a single complex derivative exists on an open set, all derivatives exist on the same set.

This *miracle of complex differentiability* has no counterpart in real analysis. The integral formula is the engine: it shows that derivatives are "smoother" than the function itself only seems to require.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ holomorphic on $D(a, R)$".

**Targets (Output Amplification)**

The conclusion is "$f^{(n)}$ exists and is given by the integral formula".

Combine with **Cauchy estimates.** Property $D$: a sup bound $M(\rho)$. The amplified result: $|f^{(n)}(a)| \leq n! M(\rho)/\rho^n$. The base of Liouville and Cauchy estimates.

Combine with **the Taylor coefficient formula.** Property $D$: $c_n = f^{(n)}(a)/n!$. The amplified result: $c_n = (1/2\pi i)\oint f(z)/(z - a)^{n+1}\,dz$. The integral representation of Taylor coefficients.

---

# Why Is It True

Differentiate the CIF under the integral sign. The integrand $f(z)/(z - w)$ is holomorphic in $w$ (for $z$ on the circle, $w$ inside the disc); the partial derivative $\partial/\partial w[1/(z - w)] = 1/(z - w)^2$. Justifying the interchange of differentiation and integration requires uniform convergence of the difference quotient on compact subsets — which holds because $z$ varies over a compact circle and $w$ is bounded away from the circle (in the smaller disc $D(a, \rho)$ inside $D(a, r)$ for some $\rho < r$).

Iterating: $f''(w) = (d/dw)[1/2\pi i \oint f(z)/(z - w)^2\,dz] = (1/2\pi i)\oint 2 f(z)/(z - w)^3\,dz = (2!/2\pi i)\oint f(z)/(z - w)^3\,dz$. By induction, the $n$-th derivative is $(n!/2\pi i)\oint f(z)/(z - w)^{n+1}\,dz$.

The deeper observation: differentiability of the integrand in $w$ propagates to differentiability of the integral. Since the integrand is *infinitely* differentiable in $w$, so is the integral.

---

# What Makes This Hard

The non-obvious technical step is *justifying* the interchange of derivative and integral. The rigorous argument uses uniform convergence of difference quotients on compact subsets of the disc, plus continuity of $\partial/\partial w[1/(z - w)] = 1/(z - w)^2$ in $(z, w)$ — both standard tools. The common error is to treat the interchange as obvious; it requires the underlying *uniform* control.

---

# Rederivation Scaffold

**High-level strategy:**
Differentiate the CIF integrand $1/(z - w)$ with respect to $w$, justify the interchange (uniform convergence on compacts), iterate.

**Subgoal decomposition:**

1. **$\partial/\partial w[1/(z - w)] = 1/(z - w)^2$.** Direct calculus.

2. **Interchange differentiation and integration.** Use uniform convergence of difference quotients on compact subsets.

3. **Result: $f'(w) = (1/2\pi i)\oint f(z)/(z - w)^2\,dz$.**

4. **Iterate.** $(d/dw)[1/(z - w)^n] = n/(z - w)^{n+1}$. After $n$ iterations, factor of $n!$ accumulates.

---

# Lemma Decomposition

> [!note]- Lemma 1: Differentiation under the integral
> **Statement:** Let $\phi : [a, b] \times D \to \mathbb{C}$ be continuous, with $\partial\phi/\partial z$ continuous on $[a, b] \times D$. Then $g(z) = \int_a^b \phi(t, z)\,dt$ is holomorphic on $D$ with $g'(z) = \int_a^b (\partial\phi/\partial z)(t, z)\,dt$.
>
> **Hint:** This is Theorem 2.5.4 in Cambridge (holomorphic dependence on a parameter), with the derivative formula confirmed by uniform convergence.
>
> > [!note]- Full proof
> > Sketch: by Morera's theorem, the function $g(z) = \int_a^b \phi(t, z)\,dt$ is holomorphic (vanishing triangle integrals, by Fubini swap with Cauchy on $\phi(t, \cdot)$). The derivative formula follows from differentiating under the integral sign, justified by uniform convergence of difference quotients on compact subsets — both $(\phi(t, z + h) - \phi(t, z))/h$ converges uniformly in $t$ to $\partial \phi/\partial z(t, z)$ when $z$ stays in a compact subset of $D$. Full proof in [[Thm - Holomorphic Dependence on a Parameter]].

---

# Formal Proof

> [!note]- Complete formal proof
> By [[Thm - Cauchy Integral Formula]], $f(w) = (1/2\pi i)\oint_{|z - a| = \rho} f(z)/(z - w)\,dz$ for $|w - a| < \rho$.
>
> The integrand $\phi(z, w) = f(z)/(z - w)$ for $z$ on the circle and $w \in D(a, \rho)$ is continuous in $(z, w)$ (the denominator is bounded away from zero: $|z - w| \geq \rho - |w - a| > 0$). Its partial in $w$ is $f(z)/(z - w)^2$, also continuous on the same domain.
>
> By Lemma 1 (or Theorem 2.5.4 in Cambridge), $f$ is holomorphic in $w$ on $D(a, \rho)$ with
> $$f'(w) = \frac{1}{2\pi i}\oint \frac{f(z)}{(z - w)^2}\,dz.$$
> Inductively: $f''(w) = (1/2\pi i)\oint \partial/\partial w[f(z)/(z - w)^2]\,dz = (1/2\pi i)\oint 2f(z)/(z - w)^3\,dz = (2!/2\pi i)\oint f(z)/(z - w)^3\,dz$.
>
> By induction, the $n$-th derivative is $(n!/2\pi i)\oint f(z)/(z - w)^{n+1}\,dz$. $\blacksquare$
>
> **Corollary: $f \in C^\infty$.** Holomorphic $\Rightarrow$ derivatives of all orders exist $\Rightarrow$ $f$ is $C^\infty$ as a function of $(x, y)$.

---

# Cross-Field Exercise Suggestions

**Boot-strapping regularity.** A "regularity theorem" in PDE says that solutions to certain equations are smoother than the equation requires. The complex case is the cleanest example: $f$ complex differentiable once $\Rightarrow$ $f \in C^\infty$ (and analytic).

**Iterating the integral formula.** The recursive structure $f^{(n)}(w) = (n!/2\pi i)\oint f(z)/(z - w)^{n+1}\,dz$ has analogues in operator theory: the resolvent $(zI - T)^{-n-1}$ for an operator $T$ has a similar contour integral characterization, used in spectral theory.

---

# Bridges

- **[[Thm - Cauchy Integral Formula]]** — the direct parent.

- **[[Thm - Cauchy Estimates]]** — direct consequence: ML applied to the higher-derivative formula.

- **[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]** — the deeper result that uses the higher-derivative formula to give the Taylor coefficients explicitly.

- **[[Thm - Holomorphic Dependence on a Parameter]]** — the differentiation-under-the-integral lemma.
