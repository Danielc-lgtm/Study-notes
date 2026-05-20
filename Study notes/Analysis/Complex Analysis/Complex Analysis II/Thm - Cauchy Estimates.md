---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Higher Derivatives via CIF"
  - "Thm - ML Estimate"
tags: [analysis, complex-analysis]
---

# Notation

$f : D(a, R) \to \mathbb{C}$ holomorphic; $M(r) = \sup_{|z - a| = r}|f(z)|$; $n \geq 0$ integer. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Motivation

The Cauchy estimates bound the Taylor coefficients of a holomorphic function by the sup-norm on a surrounding circle:
$$|f^{(n)}(a)| \leq \frac{n! M(r)}{r^n}.$$
This is the universal *quantitative* tool in complex analysis. It converts "boundedness of $f$ on a circle" into "boundedness of derivatives at the centre", and it has *no analog* in real analysis (a bounded $C^1$ function can have arbitrarily large derivative). The Cauchy estimates are the engine of [[Thm - Liouville's Theorem|Liouville]] (let $r \to \infty$), of [[Ex - Cauchy estimates bound polynomial degree|polynomial-degree bounds]] (polynomial growth $\Rightarrow$ polynomial), and of many compactness theorems for normal families.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ holomorphic on $D(a, R)$, $M(r) = \sup_{|z-a| = r}|f| < \infty$".

The first disguised source is **$f$ entire with growth $|f(z)| \leq A|z|^k$**: then $M(r) \leq A r^k$, and Cauchy estimates give $|f^{(n)}(a)| \leq A n! r^{k - n}$, which goes to $0$ as $r \to \infty$ for $n > k$. So $f^{(n)}(a) = 0$ for $n > k$, hence $f$ is a polynomial of degree $\leq k$.

The second disguised source is **$f$ continuous on $\overline{D(a, r)}$, holomorphic inside**: $M(r)$ is finite (compact + continuous), and the estimate applies. Useful when $f$ extends continuously to a closed disc.

**Targets (Output Amplification)**

The conclusion is "$|f^{(n)}(a)| \leq n! M(r)/r^n$".

Combine with **$r \to \infty$ for entire $f$.** Property $D$: $M$ uniform. The amplified result: derivative bounds shrink, eventually to zero — [[Thm - Liouville's Theorem]].

Combine with **the Taylor coefficient formula.** Property $D$: $c_n = f^{(n)}(a)/n!$. The amplified result: $|c_n| \leq M(r)/r^n$ — the radius of convergence bound.

Combine with **compactness/normal families.** Property $D$: a family $\{f_\alpha\}$ uniformly bounded on a circle. The amplified result: their derivatives are uniformly bounded — leading to Montel's theorem on normal families.

---

# Why Is It True

By [[Thm - Higher Derivatives via CIF]]:
$$f^{(n)}(a) = \frac{n!}{2\pi i}\oint_{|z - a| = r}\frac{f(z)}{(z - a)^{n+1}}\,dz.$$
On the circle $|z - a| = r$, $|z - a| = r$ exactly, so $|f(z)/(z - a)^{n+1}| \leq M(r)/r^{n+1}$. By [[Thm - ML Estimate]]:
$$|f^{(n)}(a)| \leq \frac{n!}{2\pi} \cdot \frac{M(r)}{r^{n+1}} \cdot 2\pi r = \frac{n! M(r)}{r^n}.$$
That is the entire argument. Two applications of ML, applied to the higher-derivative CIF.

---

# What Makes This Hard

Nothing genuinely hard — a direct application of ML to the higher-derivative CIF. The cleverness lies in *how* the estimates are used: letting $r \to \infty$ for Liouville, letting $r$ be chosen as a function of the growth rate for polynomial bounds, etc.

---

# Rederivation Scaffold

**High-level strategy:**
Apply ML to the higher-derivative CIF integrand on the circle.

---

# Lemma Decomposition

(No lemmas needed.)

---

# Formal Proof

> [!note]- Complete formal proof
> By [[Thm - Higher Derivatives via CIF]]:
> $$f^{(n)}(a) = \frac{n!}{2\pi i}\oint_{|z - a| = r}\frac{f(z)}{(z - a)^{n+1}}\,dz.$$
> The integrand on the circle has modulus $\leq M(r)/r^{n+1}$ (since $|z - a| = r$ on the circle and $|f(z)| \leq M(r)$). The length of the circle is $2\pi r$. By [[Thm - ML Estimate]]:
> $$|f^{(n)}(a)| \leq \frac{n!}{2\pi} \cdot \frac{M(r)}{r^{n+1}} \cdot 2\pi r = \frac{n!M(r)}{r^n}. \quad \blacksquare$$

---

# Cross-Field Exercise Suggestions

**Liouville.** $M(r) \leq M$ uniform; $|f'(a)| \leq M/r \to 0$ as $r \to \infty$; hence $f' \equiv 0$. See [[Thm - Liouville's Theorem]].

**Polynomial degree from polynomial growth.** $M(r) \leq Ar^k$ for $|z|$ large; $|f^{(n)}(a)| \leq An!r^{k - n}$; for $n > k$, this $\to 0$ as $r \to \infty$, so $f^{(n)}(a) = 0$. So $f$ is a polynomial of degree $\leq k$. See [[Ex - Cauchy estimates bound polynomial degree]].

**Normal families and Montel.** If $\{f_\alpha\}$ is a uniformly bounded family of holomorphic functions on a domain, Cauchy estimates give uniform bounds on derivatives; by Arzela–Ascoli, $\{f_\alpha\}$ is precompact in the topology of uniform convergence on compacts. This is *Montel's theorem*, the basis of conformal mapping arguments in CA IV.

---

# Bridges

- **[[Thm - Higher Derivatives via CIF]]** — the source of the integral representation.

- **[[Thm - ML Estimate]]** — the bounding tool.

- **[[Thm - Liouville's Theorem]]** — direct application.

- **[[Thm - Fundamental Theorem of Algebra]]** — direct via Liouville.
