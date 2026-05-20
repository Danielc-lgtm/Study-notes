---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Mean Value Property for Holomorphic Functions"
  - "Thm - Cauchy–Riemann Equations"
tags: [analysis, complex-analysis]
---

# Notation

$f : D(a, r) \to \mathbb{C}$ holomorphic on the open disc. "Local maximum" of $|f|$ at $a$: $|f(z)| \leq |f(a)|$ for all $z \in D(a, r)$. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Motivation

The local maximum modulus principle says: a holomorphic function whose modulus attains a local maximum at an interior point of its domain must be *constant* on a neighbourhood of that point. There is no "interior maximum" for a non-constant holomorphic function.

The intuition: the mean value property says $|f(a)|$ equals the average of $|f|$ on surrounding circles, which is bounded above by the max on the circle. If $|f|$ has a max at $a$, the average equals the max, which forces $|f|$ to be *constant* on the circle. Then by varying the radius, $|f|$ is constant on a disc. By a CR argument, this forces $f$ itself to be constant.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ holomorphic on $D(a, r)$, $|f|$ has a local max at $a$".

The first disguised source is **$|f|$ has a local extremum** (min or max). Local minima are constants only if the minimum value is $0$ (else $1/f$ has a max). So a local min at $a$ with $f(a) \neq 0$ also forces $f$ constant.

The second disguised source is **$\operatorname{Re} f$ has a max at $a$**: then $g = e^f$ has $|g| = e^{\operatorname{Re} f}$ with a max, forcing $g$ constant, hence $f$ constant.

**Targets (Output Amplification)**

The conclusion is "$f$ is constant on $D(a, r)$".

Combine with **propagation to the whole domain.** Property $D$: $f$ holomorphic on a connected $D \supseteq D(a, r)$. The amplified result: by the identity theorem (or [[Thm - Constant on a Domain if Derivative is Zero]]), $f$ is constant on the whole $D$. This is the *global* maximum modulus principle.

---

# Why Is It True

By the mean value property at $a$:
$$|f(a)| = \left|\frac{1}{2\pi}\int_0^{2\pi} f(a + \rho e^{it})\,dt\right| \leq \frac{1}{2\pi}\int_0^{2\pi} |f(a + \rho e^{it})|\,dt \leq \max_t |f(a + \rho e^{it})| \leq |f(a)|$$
(the last by hypothesis: $|f(z)| \leq |f(a)|$ for $z$ in the disc). So all the inequalities are equalities. The second equality forces $|f(a + \rho e^{it})| = |f(a)|$ for all $t$ (any deviation would lower the average). The first equality forces the integrand to be a constant multiple of $|f(\cdot)|$ — actually, the integral equality condition from the triangle inequality (see [[Thm - ML Estimate]] proof) forces $\arg f(a + \rho e^{it})$ to be constant.

So $f$ is constant on each circle $|z - a| = \rho$ (constant modulus, constant argument). Since this holds for every $\rho \in (0, r)$, $f$ is constant on $D(a, r) \setminus \{a\}$, hence on $D(a, r)$ by continuity.

Alternative argument: $|f|$ constant on a disc + CR + $f$ holomorphic forces $f$ constant. This is because $|f|^2 = f\bar f$ constant means $f\bar f = c$ constant. If $c = 0$, $f \equiv 0$. If $c \neq 0$, $\bar f = c/f$ holomorphic. But $\bar f$ holomorphic + $f$ holomorphic forces both real and imaginary parts of $f$ harmonic; CR for both $f$ and $\bar f$ then forces $f$ constant.

---

# What Makes This Hard

The non-obvious step is the *equality case* analysis of the mean value inequality. The standard reasoning ("MVP gives $|f(a)| \leq $ max on circle") needs strengthening: equality in the integral inequality $|\int g| \leq \int |g|$ forces $\arg g$ constant. Once $|f|$ and $\arg f$ are both constant on a circle, the disc-version follows by varying the radius.

---

# Rederivation Scaffold

**High-level strategy:**
MVP + max hypothesis: chain of inequalities collapses to equalities, forcing $|f|$ constant on each surrounding circle. CR or further argument promotes $|f|$ constant to $f$ constant.

**Subgoal decomposition:**

1. **MVP + max hypothesis force $|f|$ constant on every circle $|z - a| = \rho$ for $\rho < r$.**

2. **Equality of arguments.** $\arg f$ constant on each circle (from equality in integral triangle inequality).

3. **$f$ constant on each circle.**

4. **$f$ constant on $D(a, r)$.** Discs are connected via radial parametrization.

---

# Lemma Decomposition

> [!note]- Lemma 1: $|f|$ constant on a disc forces $f$ constant
> **Statement:** If $f$ is holomorphic on $D(a, r)$ and $|f|$ is constant on $D(a, r)$, then $f$ is constant.
>
> **Hint:** If $|f| = c$ constant, $f\bar f = c^2$, so $\bar f$ is holomorphic (if $c \neq 0$); but $\bar f$ being holomorphic forces $f$ constant by CR.
>
> > [!note]- Full proof
> > If $c = 0$, $f \equiv 0$, constant. If $c > 0$: $\bar f = c^2/f$ is the quotient of holomorphic functions (since $f$ has no zeros — it has constant modulus $c > 0$), hence holomorphic. But $f$ holomorphic means $u, v$ satisfy CR ($u_x = v_y, u_y = -v_x$); $\bar f = u - iv$ holomorphic means $u, -v$ satisfy CR ($u_x = -v_y, u_y = v_x$). Combining: $u_x = v_y = -v_y \Rightarrow v_y = 0$, similarly $u_x = 0$; symmetric for $u_y, v_x$. All partials zero, so $f$ constant by [[Thm - Constant on a Domain if Derivative is Zero]]. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Assume $|f(z)| \leq |f(a)|$ for all $z \in D(a, r)$. By [[Thm - Mean Value Property for Holomorphic Functions]], for $0 < \rho < r$:
> $$|f(a)| = \left|\frac{1}{2\pi}\int_0^{2\pi}f(a + \rho e^{it})\,dt\right| \leq \frac{1}{2\pi}\int_0^{2\pi}|f(a + \rho e^{it})|\,dt \leq |f(a)|.$$
> All inequalities are equalities. The second equality forces $|f(a + \rho e^{it})| = |f(a)|$ for every $t$ (the integrand's average equals its sup only when the integrand is constant). So $|f|$ is constant (equal to $|f(a)|$) on every circle $|z - a| = \rho$ for $\rho \in (0, r)$, hence on the whole disc $D(a, r)$ (and at the centre by continuity).
>
> By Lemma 1, $f$ is constant on $D(a, r)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Maximum modulus for harmonic functions.** Real and imaginary parts of holomorphic functions are harmonic; the max modulus principle for $|f|$ has an analog for harmonic $u$: a harmonic $u$ with a local interior max is constant. The mean value property of harmonic functions provides the same argument.

**Schwarz lemma.** For $f : D(0, 1) \to D(0, 1)$ holomorphic with $f(0) = 0$: $|f(z)| \leq |z|$ and $|f'(0)| \leq 1$. Equality at any interior point forces $f$ to be a rotation. Proof uses max modulus applied to $f(z)/z$. This is a fundamental rigidity statement underlying conformal automorphisms.

---

# Bridges

- **[[Thm - Mean Value Property for Holomorphic Functions]]** — the direct source.

- **[[Thm - (Global) Maximum Modulus Principle]]** — propagation from local to global via connectedness.

- **[[Thm - Cauchy–Riemann Equations]]** — used in Lemma 1 to promote $|f|$ constant to $f$ constant.
