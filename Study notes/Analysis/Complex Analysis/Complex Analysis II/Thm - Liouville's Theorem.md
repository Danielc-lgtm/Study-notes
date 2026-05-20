---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Thm - Cauchy Integral Formula"
  - "Thm - Cauchy Estimates"
tags: [analysis, complex-analysis]
---

# Notation

$f : \mathbb{C} \to \mathbb{C}$ entire (holomorphic on all of $\mathbb{C}$), bounded ($|f(z)| \leq M$ for some $M$). Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Statement

> **Theorem (Liouville).** Every bounded entire function is constant. That is, if $f : \mathbb{C} \to \mathbb{C}$ is holomorphic on all of $\mathbb{C}$ and there exists $M > 0$ with $|f(z)| \leq M$ for every $z \in \mathbb{C}$, then $f$ is constant.

---

# Motivation

Liouville's theorem is the prototype rigidity statement of complex analysis: **the only bounded entire functions are constants**. Compare with real analysis, where $\sin x$ is bounded, smooth, and certainly not constant. The complex setting is *rigid* in a way the real one is not.

Liouville is the cleanest application of Cauchy estimates: bound $|f|$ by $M$ on every circle, conclude $|f'(a)| \leq M/r$ for every $r > 0$, let $r \to \infty$ to get $f' \equiv 0$, conclude $f$ is constant by [[Thm - Constant on a Domain if Derivative is Zero]] (on the connected $\mathbb{C}$).

From Liouville, the [[Thm - Fundamental Theorem of Algebra|fundamental theorem of algebra]] follows immediately: if $p(z)$ is a non-constant polynomial without roots, $1/p(z)$ is bounded entire, hence constant — contradiction.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ entire and bounded".

The first disguised source is **a non-constant polynomial $p(z)$, applied to $1/p$**: if $p$ has no roots, $1/p$ is entire; if $|p(z)| \to \infty$ as $|z| \to \infty$, $1/p$ is bounded entire (bounded inside a large disc by continuity, bounded outside by $1/|p|$). Liouville forces $1/p$ constant, contradicting $p$ non-constant.

The second disguised source is **a holomorphic $f : \mathbb{C} \to \mathbb{C}$ with growth $|f(z)| = O(\log|z|)$ as $|z| \to \infty$**: more generally, polynomial growth implies $f$ is a polynomial; logarithmic-or-slower growth forces $f$ constant.

The third disguised source is **a bounded harmonic function on $\mathbb{R}^2$**: by constructing a harmonic conjugate (exists globally on simply connected $\mathbb{R}^2$) and exponentiating, $e^f$ is bounded entire. Liouville gives $e^f$ constant, hence $f$ constant. See [[Ex - Liouville for harmonic functions]].

**Targets (Output Amplification)**

The conclusion is "$f$ is constant".

Combine with **a value at one point.** Property $D$: $f(0)$ or $f(z_0)$. The amplified result: $f \equiv f(z_0)$ identifies the constant.

Combine with **a hypothesis ruling out the constant.** Property $D$: $f$ non-constant by some other property. The amplified result: contradiction with the boundedness; conclusion is that the function must be unbounded — e.g., polynomials of positive degree.

---

# Why Is It True

Cauchy estimates give $|f'(a)| \leq M(r)/r \leq M/r$ for any $a \in \mathbb{C}$ and any $r > 0$. Letting $r \to \infty$: $|f'(a)| \leq 0$, i.e., $f'(a) = 0$.

So $f' \equiv 0$ on $\mathbb{C}$. By [[Thm - Constant on a Domain if Derivative is Zero]] on the connected $\mathbb{C}$, $f$ is constant.

The deep observation: the bound $M(r)/r$ on $|f'|$ shrinks with $r$, but for a bounded function $M(r) \leq M$ is uniform in $r$. So the bound goes to $0$ — and $|f'(a)|$ does not depend on $r$, so it must equal $0$.

---

# What Makes This Hard

The non-obvious step is the realization that Cauchy estimates *force* $f'$ to be zero by letting the radius grow without bound — possible *only because $f$ is entire* (defined on all $\mathbb{C}$). For a function defined only on a bounded disc, $r$ is constrained, and the bound does not vanish. The error to avoid is to apply Liouville to bounded holomorphic functions on a disc — they need not be constant ($f(z) = z$ is bounded on the unit disc and not constant!).

---

# Rederivation Scaffold

**High-level strategy:**
Cauchy estimates: $|f'(a)| \leq M(r)/r$ for every $r > 0$. With $M(r) \leq M$ uniformly (boundedness), the bound $\to 0$ as $r \to \infty$. So $f' \equiv 0$. Apply [[Thm - Constant on a Domain if Derivative is Zero]].

**Subgoal decomposition:**

1. **Bound $|f'(a)| \leq M/r$ for every $r > 0$.** By [[Thm - Cauchy Estimates]] with $M(r) = \sup_{|z - a| = r} |f| \leq M$.
2. **Let $r \to \infty$.** $|f'(a)| \to 0$, hence $f'(a) = 0$.
3. **Apply constancy.** $f' \equiv 0$ on connected $\mathbb{C}$ implies $f$ constant.

---

# Lemma Decomposition

(No lemmas needed beyond Cauchy estimates.)

---

# Formal Proof

> [!note]- Complete formal proof
> Let $|f(z)| \leq M$ on $\mathbb{C}$. Fix $a \in \mathbb{C}$. By [[Thm - Cauchy Estimates]] applied to the disc $D(a, r)$ for any $r > 0$:
> $$|f'(a)| \leq \frac{M(r)}{r} \leq \frac{M}{r}.$$
> Letting $r \to \infty$: $|f'(a)| = 0$. Since $a$ was arbitrary, $f' \equiv 0$ on $\mathbb{C}$. By [[Thm - Constant on a Domain if Derivative is Zero]], $f$ is constant on the connected $\mathbb{C}$. $\blacksquare$
>
> **Alternative direct proof via CIF.** For $|w| < R$:
> $$f(w) - f(0) = \frac{1}{2\pi i}\oint_{|z|=R}f(z)\left[\frac{1}{z - w} - \frac{1}{z}\right]\,dz = \frac{w}{2\pi i}\oint_{|z|=R}\frac{f(z)}{z(z - w)}\,dz.$$
> By ML: $|f(w) - f(0)| \leq |w|/(2\pi) \cdot 2\pi R \cdot M/(R(R - |w|)) = |w| M/(R - |w|) \to 0$ as $R \to \infty$. So $f(w) = f(0)$ for all $w$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**FTA via Liouville.** See [[Thm - Fundamental Theorem of Algebra]]: every non-constant polynomial has a complex root. Application of Liouville to $1/p$.

**Harmonic Liouville.** A bounded harmonic function on $\mathbb{R}^2$ is constant. The proof uses Liouville applied to $e^{f}$ where $f = u + iv$ is built from the harmonic conjugate. See [[Ex - Liouville for harmonic functions]].

**Sub-polynomial growth means constant.** If $|f(z)| \leq A|z|^\alpha$ for $|z|$ large, with $\alpha < 1$, then $f$ is constant. Generalization: $\alpha < n$ implies $f$ is a polynomial of degree $< n$. See [[Ex - Cauchy estimates bound polynomial degree]].

---

# Bridges

- **[[Thm - Cauchy Estimates]]** — the direct tool.

- **[[Thm - Fundamental Theorem of Algebra]]** — direct consequence.

- **[[Thm - Constant on a Domain if Derivative is Zero]]** — the finishing step.

- **[[Thm - Cauchy Integral Formula]]** — the deeper source (Cauchy estimates derive from CIF).
