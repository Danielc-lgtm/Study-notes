---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Cauchy Integral Formula"
  - "Thm - Higher Derivatives via CIF"
  - "Def - Power Series and Radius of Convergence"
tags: [analysis, complex-analysis]
---

# Notation

$f : D(a, R) \to \mathbb{C}$ holomorphic; $c_n = f^{(n)}(a)/n!$. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Statement

> **Theorem (holomorphic functions are analytic).** Let $f : D(a, R) \to \mathbb{C}$ be holomorphic on the open disc $D(a, R)$. Then $f$ has a convergent power series expansion centred at $a$ on the entire disc:
> $$f(z) = \sum_{n=0}^\infty c_n (z - a)^n, \qquad z \in D(a, R),$$
> with coefficients $c_n = f^{(n)}(a)/n!$ given by Taylor's formula and equivalently by the Cauchy integral formula
> $$c_n = \frac{1}{2\pi i}\oint_{|z - a| = r}\frac{f(z)}{(z - a)^{n+1}}\,dz \quad \text{for any } 0 < r < R.$$
> Combined with the converse from CA I, this gives the equivalence: a function is holomorphic on $D(a, R)$ if and only if it is given by a convergent power series on $D(a, R)$.

---

# Motivation

The structural theorem of complex analysis: **every holomorphic function on a disc is given by a convergent power series**, with coefficients $c_n = f^{(n)}(a)/n!$. Combined with the converse from [[Complex Analysis I — Basic Notions]] ([[Thm - Power Series is Holomorphic with Termwise Derivative]]: every power series is holomorphic on its disc), this gives the central equivalence:
$$\text{holomorphic on a disc} \quad \Longleftrightarrow \quad \text{convergent power series on that disc}.$$
Holomorphic and analytic are the *same thing* in complex analysis (in stark contrast to real analysis, where $C^\infty \neq $ analytic).

This theorem is the engine of every rigidity result: identity theorem, principle of isolated zeros, factorization at zeros, Schwarz lemma. All rely on the local power-series structure.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ holomorphic on $D(a, R)$".

**Targets (Output Amplification)**

The conclusion is "$f(z) = \sum c_n (z - a)^n$ converging on $D(a, R)$".

Combine with **the identity theorem.** Property $D$: $f$ vanishes on a set with an accumulation point. The amplified result: all $c_n = 0$, hence $f \equiv 0$ locally, and by connectedness globally. See [[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]].

Combine with **the principle of isolated zeros.** Property $D$: $f(w) = 0$ for some interior $w$. The amplified result: at $w$, $f(z) = (z - w)^k g(z)$ with $g(w) \neq 0$, so $w$ is an isolated zero. See [[Thm - Principle of Isolated Zeros]].

Combine with **the residue theorem (in CA III).** Property $D$: $f$ has a Laurent series at an isolated singularity. The amplified result: residues classify the behaviour near the singularity. The local power series is the engine.

---

# Why Is It True

Start with CIF: $f(w) = (1/2\pi i)\oint_{|z - a| = r} f(z)/(z - w)\,dz$ for $|w - a| < r < R$. Expand $1/(z - w)$ as a geometric series in $(w - a)$:
$$\frac{1}{z - w} = \frac{1}{(z - a)(1 - (w - a)/(z - a))} = \sum_{n=0}^\infty \frac{(w - a)^n}{(z - a)^{n+1}},$$
uniformly convergent for $z$ on the circle $|z - a| = r$ (since $|(w - a)/(z - a)| = |w - a|/r < 1$).

Substituting and integrating term by term (justified by uniform convergence):
$$f(w) = \frac{1}{2\pi i}\oint f(z) \sum_{n=0}^\infty \frac{(w - a)^n}{(z - a)^{n+1}}\,dz = \sum_{n=0}^\infty (w - a)^n \cdot \frac{1}{2\pi i}\oint\frac{f(z)}{(z - a)^{n+1}}\,dz.$$
The integrand of the $n$-th coefficient is precisely the integrand of $f^{(n)}(a)/n!$ from the higher-derivative CIF, so each coefficient equals $f^{(n)}(a)/n! = c_n$. Hence
$$f(w) = \sum_{n=0}^\infty c_n (w - a)^n, \quad c_n = f^{(n)}(a)/n!.$$

The convergence is on the whole disc $D(a, R)$: for any $w$ with $|w - a| < R$, take $r$ with $|w - a| < r < R$, and the argument applies. Equivalently, the radius of convergence is at least $R$.

The depth of the result: it is *not* obvious that a holomorphic function should locally be a power series. In real analysis, the analogous statement is false. The complex setting works because complex differentiability is a much stronger condition (a single complex derivative implies infinitely many, and they assemble into a convergent series).

---

# What Makes This Hard

The non-obvious step is the *geometric series expansion* of $1/(z - w)$ around $(w - a)$ — a clever rewriting that converts CIF into a power series. The technical detail is justifying *term-by-term integration*, which uses uniform convergence on the circle. The most common error is to confuse "Taylor series" (which always exists for $C^\infty$ functions) with "convergent power series equal to $f$" (which requires complex differentiability).

---

# Rederivation Scaffold

**High-level strategy:**
Start with CIF. Expand $1/(z - w)$ as a geometric series in $(w - a)/(z - a)$. Integrate term by term to get the power series with $c_n = f^{(n)}(a)/n!$.

**Subgoal decomposition:**

1. **CIF at $w$.** $f(w) = (1/2\pi i)\oint f(z)/(z - w)\,dz$.

2. **Geometric series expansion.** $1/(z - w) = \sum (w - a)^n/(z - a)^{n+1}$, uniformly convergent on the circle.

3. **Integrate term by term.** $f(w) = \sum (w - a)^n \cdot (1/2\pi i)\oint f(z)/(z - a)^{n+1}\,dz$.

4. **Identify coefficients.** $c_n = (1/2\pi i)\oint f(z)/(z - a)^{n+1}\,dz = f^{(n)}(a)/n!$ by [[Thm - Higher Derivatives via CIF]].

5. **Radius.** Series converges on $D(a, R)$ since the argument works for any $|w - a| < r < R$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Geometric series expansion of $1/(z - w)$
> **Statement:** For $|w - a| < |z - a|$:
> $$\frac{1}{z - w} = \sum_{n=0}^\infty \frac{(w - a)^n}{(z - a)^{n+1}}.$$
>
> > [!note]- Full proof
> > $1/(z - w) = 1/((z - a) - (w - a)) = (1/(z - a))/(1 - (w - a)/(z - a))$. By the geometric series for $1/(1 - q) = \sum q^n$ with $q = (w - a)/(z - a)$ (and $|q| < 1$), the series converges to $1/(1 - q)$, giving the formula. $\blacksquare$

> [!note]- Lemma 2: Uniform convergence on a circle
> **Statement:** For $|w - a| < r$, the series in Lemma 1 converges uniformly for $z$ on the circle $|z - a| = r$.
>
> > [!note]- Full proof
> > On the circle, $|q| = |w - a|/r < 1$ constant. So the series $\sum q^n/(z - a)$ is bounded by $\sum |q|^n/r = 1/(r(1 - |q|))$, summable. Weierstrass $M$-test gives uniform convergence. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix $w \in D(a, R)$. Choose $r$ with $|w - a| < r < R$. By [[Thm - Cauchy Integral Formula]]:
> $$f(w) = \frac{1}{2\pi i}\oint_{|z - a| = r}\frac{f(z)}{z - w}\,dz.$$
> By Lemma 1, $1/(z - w) = \sum_n (w - a)^n/(z - a)^{n+1}$ for $|w - a| < |z - a|$ (the entire circle). By Lemma 2, the series converges uniformly in $z$ on the circle.
>
> Multiply by $f(z)/(2\pi i)$ and integrate term by term:
> $$f(w) = \sum_{n=0}^\infty (w - a)^n \cdot \underbrace{\frac{1}{2\pi i}\oint_{|z - a| = r}\frac{f(z)}{(z - a)^{n+1}}\,dz}_{= f^{(n)}(a)/n! \text{ by } [[Thm - Higher Derivatives via CIF]]} = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(w - a)^n.$$
>
> Since $w$ was arbitrary in $D(a, R)$, the power series converges on the whole disc. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Holomorphic = analytic, in stark contrast to $C^\infty$ vs analytic in real analysis.** The real exponential $e^{-1/x^2}$ (extended by $0$ at $0$) is $C^\infty$ but its Taylor series at $0$ is identically zero, so the series does not equal the function. In complex analysis, this cannot happen: holomorphic $\Rightarrow$ analytic. The lesson: complex differentiability is *vastly* stronger than real differentiability.

**Radius of convergence equals distance to nearest singularity.** A holomorphic $f$ on $\mathbb{C}$ except for some singularities has a Taylor series at any point $a$ with radius equal to the distance from $a$ to the nearest singularity. So the *geometric* placement of singularities determines the *analytic* radius of convergence — a beautiful structural fact.

---

# Bridges

- **[[Thm - Cauchy Integral Formula]]** — the source.

- **[[Thm - Higher Derivatives via CIF]]** — gives the coefficient formula.

- **[[Thm - Identity Theorem for Power Series]]** — gives uniqueness of the local representation.

- **[[Thm - Principle of Isolated Zeros]]** — direct consequence.

- **[[Thm - Identity Theorem (Uniqueness of Analytic Continuation)]]** — uses this and isolated zeros.
