---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Def - Contour Integral"
  - "Thm - Cauchy's Theorem for a Disc"
  - "Thm - Goursat's Theorem (Cauchy for a Triangle)"
tags: [analysis, complex-analysis]
---

# Notation

$D = D(a, r)$ — an open disc; $f : D \to \mathbb{C}$ holomorphic; $w \in D$ with $|w - a| < \rho < r$. The integration contour is $|z - a| = \rho$, traversed counterclockwise once. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Statement

> **Theorem (Cauchy integral formula).** Let $D = D(a, r) \subseteq \mathbb{C}$ be an open disc and $f : D \to \mathbb{C}$ holomorphic. For every $w \in D$ and every $\rho$ with $|w - a| < \rho < r$:
> $$f(w) = \frac{1}{2\pi i} \oint_{|z - a| = \rho} \frac{f(z)}{z - w}\,dz,$$
> where the contour is traversed once counterclockwise. The value of $f$ at the interior point $w$ is recovered as a contour integral of $f$ along any surrounding circle.

---

# Motivation

The Cauchy integral formula (CIF) is *the* central formula of complex analysis. It reads:
$$f(w) = \frac{1}{2\pi i} \oint_{|z - a| = \rho} \frac{f(z)}{z - w}\,dz.$$
This expresses the value of $f$ at an interior point $w$ as a *contour integral* over a surrounding circle. The function's value at any interior point is *reproduced* from its values on the boundary — this is the **reproducing kernel** structure of holomorphic functions.

From CIF, the entire arsenal of complex analysis follows: differentiability of all orders ([[Thm - Higher Derivatives via CIF]]), the local power series expansion ([[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]), Liouville's theorem ([[Thm - Liouville's Theorem]]), the maximum modulus principle, the identity theorem. Every rigidity result of complex analysis traces back to CIF.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ holomorphic on $D(a, r)$, $w \in D(a, \rho), \rho < r$".

The first disguised source is **$f$ has a known power series at $a$**: then $f(w)$ can be computed term by term, but CIF is the cleanest universal formula — works for any holomorphic $f$, not just power series.

The second disguised source is **$f$ continuous on $\overline{D(a, \rho)}$, holomorphic on the open disc**: CIF extends (boundary values are recovered from a hypothesis of continuity to the boundary plus holomorphicity inside).

**Targets (Output Amplification)**

The conclusion is "$f(w) = \frac{1}{2\pi i}\oint f(z)/(z - w)\,dz$".

Combine with **the mean value property at the centre.** Property $D$: $w = a$ (centre). The amplified result: $f(a) = \frac{1}{2\pi}\int_0^{2\pi} f(a + re^{i\theta})\,d\theta$ — the **mean value property**. See [[Thm - Mean Value Property for Holomorphic Functions]].

Combine with **differentiation under the integral.** Property $D$: differentiate the integrand with respect to $w$. The amplified result: $f^{(n)}(w) = (n!/2\pi i)\oint f(z)/(z - w)^{n+1}\,dz$ — the higher-derivative formula. See [[Thm - Higher Derivatives via CIF]].

Combine with **Cauchy estimates.** Property $D$: a sup bound $M(r) = \sup_{|z-a|=r}|f|$. The amplified result: $|f^{(n)}(a)| \leq n!M(r)/r^n$. The engine of [[Thm - Liouville's Theorem|Liouville]].

---

# Why Is It True

The idea: $f(z)/(z - w)$ has a pole at $z = w$. To evaluate $\oint f(z)/(z - w)\,dz$, replace $f(z)$ by its average around $w$. Concretely, consider the function
$$g(z) := \frac{f(z) - f(w)}{z - w} \quad \text{for } z \neq w, \qquad g(w) := f'(w).$$
$g$ is continuous on $D$ (the limit as $z \to w$ exists and equals $f'(w)$) and holomorphic on $D \setminus \{w\}$. By the extended [[Thm - Goursat's Theorem (Cauchy for a Triangle)|Goursat]] (continuous + holomorphic-except-finite-points), $g$ has vanishing triangle integrals; on the star-shaped disc, $\oint g(z)\,dz = 0$. So
$$\oint \frac{f(z) - f(w)}{z - w}\,dz = 0, \quad \text{i.e.,} \quad \oint \frac{f(z)}{z - w}\,dz = f(w) \oint \frac{dz}{z - w}.$$
The second integral is computed directly: parametrize the circle, get $2\pi i$. So $\oint f(z)/(z - w)\,dz = 2\pi i f(w)$. Divide by $2\pi i$ to get CIF.

The alternative proof (Cambridge IB) uses the geometric series expansion: for $z$ on the circle $|z - a| = \rho$,
$$\frac{1}{z - w} = \frac{1}{(z - a)(1 - (w - a)/(z - a))} = \sum_{n=0}^\infty \frac{(w - a)^n}{(z - a)^{n+1}},$$
converging uniformly in $z$ on the circle. Multiplying by $f(z)$ and integrating term by term:
$$\oint \frac{f(z)}{z - w}\,dz = \sum_{n=0}^\infty (w - a)^n \oint \frac{f(z)}{(z - a)^{n+1}}\,dz.$$
The $n$-th integral evaluates (by the CIF itself, recursively, or by direct calculation) to $2\pi i f^{(n)}(a)/n!$. This gives the *power series expansion* of $f(w)$ in terms of the coefficients, and Lemma 2.3.1 in Cambridge handles it.

---

# What Makes This Hard

The non-obvious step is the introduction of the auxiliary function $g(z) = (f(z) - f(w))/(z - w)$, which "removes the singularity" at $w$ by extending continuously. This is a *removable singularity* argument, and the technical point is that $g$ is holomorphic on $D \setminus \{w\}$ and *continuous* at $w$ (extending by $f'(w)$). The extended Goursat for continuous-+-holomorphic-except-finite-points does the rest.

---

# Rederivation Scaffold

**High-level strategy:**
Build $g(z) = (f(z) - f(w))/(z - w)$, continuous on $D$ with $g(w) = f'(w)$, holomorphic on $D \setminus \{w\}$. Apply extended Goursat/Cauchy: $\oint g\,dz = 0$. Rearrange to extract $f(w)\oint dz/(z - w) = 2\pi i f(w)$.

**Subgoal decomposition:**

1. **Define $g(z) = (f(z) - f(w))/(z - w)$ with $g(w) = f'(w)$.** Check continuity at $w$ (use $f' (w)$ existence) and holomorphicity off $w$.

2. **Apply extended Cauchy.** $\oint g\,dz = 0$.

3. **Rearrange.** $\oint f(z)/(z - w)\,dz = f(w)\oint dz/(z - w)$.

4. **Compute $\oint dz/(z - w) = 2\pi i$.** Direct parametrization of the circle.

5. **Conclude.** $f(w) = (1/2\pi i)\oint f(z)/(z - w)\,dz$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Removable singularity at $w$
> **Statement:** Define $g(z) = (f(z) - f(w))/(z - w)$ for $z \neq w$, $g(w) = f'(w)$. Then $g$ is continuous on $D$ and holomorphic on $D \setminus \{w\}$.
>
> > [!note]- Full proof
> > For $z \neq w$, $g$ is the quotient of two holomorphic functions (with nonzero denominator), hence holomorphic. Continuity at $w$: $\lim_{z \to w} g(z) = \lim_{z \to w}(f(z) - f(w))/(z - w) = f'(w) = g(w)$. So $g$ is continuous at $w$. $\blacksquare$

> [!note]- Lemma 2: $\oint dz/(z - w) = 2\pi i$ for $w$ inside the contour
> **Statement:** For $w$ with $|w - a| < \rho$, $\oint_{|z - a| = \rho} dz/(z - w) = 2\pi i$.
>
> **Hint:** This is just the "winding number of the circle around $w$".
>
> > [!note]- Full proof
> > Compute directly. Parametrize $\gamma(t) = a + \rho e^{it}$, $t \in [0, 2\pi]$, so $\gamma'(t) = i\rho e^{it}$. Then
> > $$\oint \frac{dz}{z - w} = \int_0^{2\pi}\frac{i\rho e^{it}}{a + \rho e^{it} - w}\,dt.$$
> > Alternative cleaner argument: $1/(z - w) = 1/(z - a) \cdot 1/(1 - (w - a)/(z - a)) = \sum_{n=0}^\infty (w - a)^n/(z - a)^{n+1}$ uniformly convergent for $|z - a| = \rho > |w - a|$. Integrate term by term: $\oint (z - a)^{-(n+1)}\,dz = 2\pi i \delta_{n, 0}$ (only the $n = 0$ term survives). So $\oint dz/(z - w) = 2\pi i \cdot 1 = 2\pi i$.

---

# Formal Proof

> [!note]- Complete formal proof
> Define $g(z) := (f(z) - f(w))/(z - w)$ for $z \neq w$, $g(w) := f'(w)$. By Lemma 1, $g$ is continuous on $D$ and holomorphic on $D \setminus \{w\}$.
>
> The disc $D$ is star-shaped (Lemma 1 of [[Thm - Cauchy's Theorem for a Disc]]). Apply the extended Cauchy/Goursat theorem (Goursat's theorem for continuous functions holomorphic except at finite points, see [[Thm - Goursat's Theorem (Cauchy for a Triangle)]]): for any closed curve $\gamma$ in $D$ (in particular, the circle $|z - a| = \rho$):
> $$\oint_{|z - a| = \rho} g(z)\,dz = 0.$$
> Expanding $g$ for $z$ on the circle (where $z \neq w$):
> $$\oint \frac{f(z)}{z - w}\,dz - \oint \frac{f(w)}{z - w}\,dz = 0,$$
> hence
> $$\oint \frac{f(z)}{z - w}\,dz = f(w) \oint \frac{dz}{z - w} = f(w) \cdot 2\pi i$$
> by Lemma 2. Dividing by $2\pi i$:
> $$f(w) = \frac{1}{2\pi i}\oint_{|z - a| = \rho}\frac{f(z)}{z - w}\,dz. \quad \blacksquare$$

---

# Cross-Field Exercise Suggestions

**Evaluating real integrals.** Many real integrals like $\int_{-\infty}^\infty \cos x/(x^2 + 1)\,dx$ are evaluated by integrating $e^{iz}/(z^2 + 1)$ over a contour in the upper half-plane and using CIF at the pole $z = i$. The bridge from real to complex is via CIF.

**Sampling theorem / band-limited reconstruction.** In signal processing, a band-limited function (Fourier transform supported on $[-B, B]$) can be reconstructed from samples. This is a real-variable version of CIF: the function on a region is recovered from "boundary" data. The structural analogy is striking.

**Holomorphic functional calculus.** For a bounded operator $T$ with spectrum $\sigma(T)$, one defines $f(T) := \frac{1}{2\pi i}\oint_\gamma f(z)(zI - T)^{-1}\,dz$ for $f$ holomorphic on a neighbourhood of $\sigma(T)$. This is the *operator-valued* CIF — the basis of spectral theory.

---

# Bridges

- **[[Thm - Cauchy's Theorem for a Disc]]** — the input.

- **[[Thm - Higher Derivatives via CIF]]** — direct corollary.

- **[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]** — proved by expanding $1/(z - w)$ in geometric series in CIF.

- **[[Thm - Mean Value Property for Holomorphic Functions]]** — special case at the centre.

- **[[Thm - Liouville's Theorem]]** — proved by CIF + Cauchy estimates.
