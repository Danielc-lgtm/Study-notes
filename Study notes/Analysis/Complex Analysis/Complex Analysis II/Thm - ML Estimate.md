---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Contour Integral"
  - "Def - Curve and C1 Curve"
tags: [analysis, complex-analysis]
---

# Notation

$\gamma : [a, b] \to \mathbb{C}$ a piecewise $C^1$ curve; $f$ continuous on the trace $\gamma^*$; $M = \sup_{z \in \gamma^*} |f(z)|$; $L = L(\gamma) = \int_a^b |\gamma'(t)|\,dt$. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Statement

> **Theorem (ML estimate).** Let $\gamma : [a, b] \to \mathbb{C}$ be a piecewise $C^1$ curve with trace $\gamma^*$ and length $L = L(\gamma) = \int_a^b |\gamma'(t)|\,dt$, and let $f$ be continuous on $\gamma^*$ with $M = \sup_{z \in \gamma^*}|f(z)| < \infty$. Then
> $$\left|\int_\gamma f(z)\,dz\right| \leq M\, L.$$

---

# Motivation

The ML estimate is the universal *bound* on contour integrals. It says: $|\int_\gamma f\,dz|$ cannot exceed $M$ (a bound on $|f|$ on the path) times $L$ (the length of the path). This is the single most-used tool for bounding contour integrals, especially when proving an integral is small (e.g., a limit goes to zero).

The mnemonic "ML" stands for "Modulus times Length". Despite its simplicity, it is the engine of countless arguments: the proof of Liouville's theorem (bounding $|f'(a)|$ by $M/r$ via CIF + ML), the proof of Cauchy estimates, and the limit arguments in Cauchy's theorem and CIF.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ continuous on $\gamma^*$, $|f| \leq M$ on $\gamma^*$".

The first disguised source is **$|f|$ bounded by a function $g$ on the trace** with explicit $g$: take $M = \sup g$ on the relevant region. Used when $f = h_1/h_2$ and bounds on each component give a bound on $f$.

The second disguised source is **a sequence of paths $\gamma_n$ with $L(\gamma_n) \to 0$**: then $|\int_{\gamma_n} f\,dz| \leq M L(\gamma_n) \to 0$ for any continuous $f$ bounded near the limit. Useful for "shrinking contour" arguments.

The third disguised source is **a path approaching infinity with $|f(z)| \to 0$ on it**: e.g., $\gamma_R$ = quarter circle of radius $R$, $|f(z)| \leq C/R^2$. Then $|\int_{\gamma_R} f\,dz| \leq (C/R^2)(R\pi/2) \to 0$. Crucial in computing real integrals via half-plane contours.

**Targets (Output Amplification)**

The conclusion is "$|\int_\gamma f\,dz| \leq ML$".

Combine with **a parameterized family.** Property $D$: $f$ depends on a parameter, and we want uniform bounds. The amplified result: uniform bounds on the integral.

Combine with **a limit argument.** Property $D$: we want to show $\int_{\gamma_n} f\,dz \to 0$. The amplified result: enough to show $M_n L_n \to 0$ for $M_n = \sup_{\gamma_n^*} |f|, L_n = L(\gamma_n)$.

---

# Why Is It True

The triangle inequality, in integral form. $|\int_a^b g(t)\,dt| \leq \int_a^b |g(t)|\,dt$ for $g : [a, b] \to \mathbb{C}$ continuous — the integral of a complex-valued function is bounded by the integral of its modulus. Apply this to $g(t) = f(\gamma(t))\gamma'(t)$:
$$\left|\int_\gamma f\,dz\right| = \left|\int_a^b f(\gamma(t))\gamma'(t)\,dt\right| \leq \int_a^b |f(\gamma(t))| |\gamma'(t)|\,dt \leq M \int_a^b |\gamma'(t)|\,dt = M L.$$
That is the entire argument. The first inequality is the integral triangle inequality; the second is the pointwise bound $|f(\gamma(t))| \leq M$.

The integral triangle inequality itself has a short proof: let $\theta = \arg(\int g)$; then $\int g = e^{i\theta}|\int g|$, so $|\int g| = e^{-i\theta}\int g = \int e^{-i\theta} g = \int \operatorname{Re}(e^{-i\theta} g) \leq \int |g|$, since the integrand on the left equals the real part on the right (the integral is real), and $\operatorname{Re}(e^{-i\theta} g) \leq |e^{-i\theta} g| = |g|$.

---

# What Makes This Hard

There is essentially no difficulty in the *proof* — it is two applications of the triangle inequality. The skill is in *choosing $M$ and $L$* cleverly: an $M$ that is too loose (overestimating $|f|$) or an $L$ that is too long (because of poor path choice) gives a weak bound. In limit arguments, picking the right path so $ML \to 0$ is the entire art.

---

# Rederivation Scaffold

**High-level strategy:**
Apply the integral triangle inequality $|\int g| \leq \int |g|$. Apply the pointwise bound $|f(\gamma(t))| \leq M$. Pull out the constant $M$.

**Subgoal decomposition:**

1. **Integral triangle inequality.**
   - *Hint:* let $\theta = \arg(\int g)$, multiply by $e^{-i\theta}$ to make the integral real, use $\operatorname{Re}(z) \leq |z|$.
   - *Why needed:* the basic inequality.

2. **Apply to $g = f \circ \gamma \cdot \gamma'$ and bound $|f(\gamma(t))| \leq M$.**
   - *Why needed:* delivers the conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Integral triangle inequality
> **Statement:** For $g : [a, b] \to \mathbb{C}$ continuous: $|\int_a^b g(t)\,dt| \leq \int_a^b |g(t)|\,dt$.
>
> **Hint:** Multiply by an appropriate phase to make the integral real and positive, then use $\operatorname{Re}(z) \leq |z|$.
>
> > [!note]- Full proof
> > If $\int g = 0$, trivial. Otherwise let $I = \int g \neq 0$ and $\theta = \arg(I)$, so $I = e^{i\theta}|I|$. Then
> > $$|I| = e^{-i\theta}I = e^{-i\theta}\int g = \int e^{-i\theta}g = \int \operatorname{Re}(e^{-i\theta}g)$$
> > (the last equality because the left side is real, so the imaginary part of the right side is zero). Since $\operatorname{Re}(e^{-i\theta}g) \leq |e^{-i\theta}g| = |g|$ pointwise, $|I| \leq \int |g|$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Assume $\gamma$ is $C^1$ (the piecewise case follows by additivity). By Lemma 1:
> $$\left|\int_\gamma f\,dz\right| = \left|\int_a^b f(\gamma(t))\gamma'(t)\,dt\right| \leq \int_a^b |f(\gamma(t))\gamma'(t)|\,dt = \int_a^b |f(\gamma(t))|\,|\gamma'(t)|\,dt.$$
> Using $|f(\gamma(t))| \leq M$ on the trace:
> $$\leq M \int_a^b |\gamma'(t)|\,dt = ML. \quad \blacksquare$$

---

# Cross-Field Exercise Suggestions

**Bounding integrals on large circles.** For an entire function $f$ with $|f(z)| \leq C|z|^k$ as $|z| \to \infty$, the integral $\oint_{|z|=R} f(z)/z^n\,dz$ has $|f/z^n| \leq CR^k/R^n = CR^{k-n}$ on the circle of radius $R$, length $2\pi R$. ML gives the bound $2\pi C R^{k-n+1}$, which goes to zero as $R \to \infty$ if $k - n + 1 < 0$, i.e., $n > k + 1$.

**Estimating Cauchy coefficients.** From the higher-derivative CIF, $|f^{(n)}(a)| \leq \frac{n!}{2\pi} \cdot \frac{M(r)}{r^{n+1}} \cdot 2\pi r = \frac{n!M(r)}{r^n}$ — the Cauchy estimates. The ML is the single tool applied to the integral $f^{(n)}(a) = \frac{n!}{2\pi i}\int_{|z-a|=r} f(z)/(z-a)^{n+1}\,dz$.

**Bounds in stochastic calculus.** In Itô calculus, isometry-type bounds on stochastic integrals are the probabilistic analog of ML — they bound an integral by an integral of squared moduli.

---

# Bridges

- **[[Def - Contour Integral]]** — the object being bounded.

- **[[Thm - Cauchy Estimates]]** — the direct application of ML to higher-derivative CIF.

- **[[Thm - Liouville's Theorem]]** — proved by Cauchy estimates with $r \to \infty$, ultimately via ML.

- **[[Thm - Cauchy Integral Formula]]** — the proof uses ML on shrinking circles to pass to the limit.
