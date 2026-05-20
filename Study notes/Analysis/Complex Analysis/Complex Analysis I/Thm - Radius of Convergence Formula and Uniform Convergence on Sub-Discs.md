---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Power Series and Radius of Convergence"
tags: [analysis, complex-analysis]
---

# Notation

$\sum_{n=0}^\infty c_n (z - a)^n$ — a power series with centre $a \in \mathbb{C}$ and coefficients $\{c_n\} \subseteq \mathbb{C}$. $R = 1/\limsup_{n\to\infty} |c_n|^{1/n}$ — the **radius of convergence**, in $[0, \infty]$ with the conventions $1/0 = \infty, 1/\infty = 0$. $\overline{D(a, r)} = \{z : |z - a| \leq r\}$ — closed disc. Full registry on [[Complex Analysis I — Basic Notions]].

---

# Motivation

A power series $\sum c_n (z - a)^n$ is a formal object — a sequence of coefficients — and we want to interpret it as a function. The first question: where does the series *converge*? The radius of convergence formula answers this *quantitatively* via the coefficient growth, and the uniform convergence statement says *how strongly* it converges on each closed subdisc.

Uniform convergence is essential because it makes the limit function $f(z) = \sum c_n (z - a)^n$ a continuous function — in fact, holomorphic, as [[Thm - Power Series is Holomorphic with Termwise Derivative]] shows. The uniform convergence on closed subdiscs (not on the whole open disc) is the natural compromise: the series may not converge uniformly all the way to the boundary, but it does so on any closed disc strictly inside.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "a power series with coefficient sequence $\{c_n\}$".

The first disguised source is **explicit coefficient formulas**: $c_n = 1/n!$, $c_n = 1$, $c_n = n!$, $c_n = 1/n$. The skill is computing $\limsup |c_n|^{1/n}$ from these — using Stirling for $n!$, or recognizing common limits.

The second disguised source is **functions defined by integrals or sums depending on a parameter**, where the Taylor coefficients are integrals or series of integrals. The theorem then gives a quantitative estimate of where the power series converges. *Example:* the gamma function has a Taylor series whose coefficients involve the Riemann zeta function; the radius is determined by the spacing of the poles.

**Targets (Output Amplification)**

The conclusion is "absolute convergence on $D(a, R)$ + uniform convergence on closed sub-discs + divergence outside $\overline{D(a, R)}$".

Combine with **termwise differentiation/integration.** Property $D$: we want $f'(z)$ or $\int f$. The amplified result: differentiate/integrate term by term, with the same radius of convergence. This is the engine of [[Thm - Power Series is Holomorphic with Termwise Derivative]].

Combine with **the Weierstrass test for limits.** Property $D$: $f$ is a uniform limit of $f_n$ on compact subsets of the disc. The amplified result: properties preserved under uniform-on-compacts limits transfer from $f_n$ to $f$ — continuity, holomorphicity (via Morera), zeros (via Hurwitz). The uniform-on-closed-subdiscs convergence is exactly *uniform on compact subsets of the open disc*.

---

# Why Is It True

The root test says $\sum a_n$ converges absolutely if $\limsup |a_n|^{1/n} < 1$, diverges if $> 1$. Applied to $a_n = c_n (z - a)^n$, we get $|a_n|^{1/n} = |c_n|^{1/n} |z - a|$, so the convergence/divergence threshold is $\limsup |c_n|^{1/n} \cdot |z - a| < 1$ vs. $> 1$, i.e., $|z - a| < R = 1/\limsup |c_n|^{1/n}$ vs. $> R$.

The uniform convergence on $\overline{D(a, r)}$ for $r < R$ is the **Weierstrass $M$-test**: bound each term $|c_n (z - a)^n| \leq |c_n| r^n =: M_n$ on the closed sub-disc. Then $\sum M_n$ converges (because $r < R$ gives $\limsup |c_n r^n|^{1/n} = r/R < 1$, so root test gives absolute convergence of $\sum |c_n| r^n$). The Weierstrass test then gives uniform convergence on $\overline{D(a, r)}$.

The whole argument is the *standard* root test analysis, with the geometric content that the natural shape of the convergence region is a disc (because the constraint involves only $|z - a|$).

---

# What Makes This Hard

The non-obvious step is *which* test to apply: root test (universal, using $\limsup$) or ratio test (limited to cases where $\lim |c_n/c_{n+1}|$ exists). The root test is universally applicable but harder to compute; the ratio test is easier but does not apply to series like $\sum 2^{n^2} z^n$ where the ratio oscillates. The error is to apply the ratio test where it does not converge and conclude divergence — when in fact the root test would give convergence.

---

# Rederivation Scaffold

**High-level strategy:**
Apply the root test pointwise to determine $R$. Apply the Weierstrass $M$-test on closed sub-discs with $M_n = |c_n| r^n$ to upgrade to uniform convergence.

**Subgoal decomposition:**

1. **Absolute convergence on $|z - a| < R$.**
   - *Hint:* root test: $\limsup |c_n (z - a)^n|^{1/n} = |z - a|/R < 1$.
   - *Why needed:* establishes convergence inside.

2. **Divergence on $|z - a| > R$.**
   - *Hint:* root test: $\limsup |c_n (z - a)^n|^{1/n} = |z - a|/R > 1$, so $|c_n (z - a)^n| \not\to 0$.
   - *Why needed:* establishes divergence outside.

3. **Uniform convergence on $\overline{D(a, r)}$ for $r < R$.**
   - *Hint:* Weierstrass $M$-test with $M_n = |c_n| r^n$; $\sum M_n < \infty$ by step 1 at $z = a + r$.
   - *Why needed:* upgrades pointwise to uniform.

---

# Lemma Decomposition

> [!note]- Lemma 1: Root test for power series
> **Statement:** For $z \in \mathbb{C}$ with $z \neq a$, $\sum c_n (z - a)^n$ converges absolutely if $|z - a| < R$ and diverges if $|z - a| > R$, where $R = 1/\limsup |c_n|^{1/n}$.
>
> **Hint:** $|c_n (z - a)^n|^{1/n} = |c_n|^{1/n} |z - a|$; apply the root test.
>
> **Why needed:** Establishes the disc of convergence.
>
> > [!note]- Full proof
> > Set $L = \limsup |c_n|^{1/n}$. Then $\limsup |c_n (z - a)^n|^{1/n} = L |z - a|$. By the root test for series of complex numbers: absolute convergence if $L|z - a| < 1$, divergence if $L|z - a| > 1$. The condition $L|z - a| < 1$ is $|z - a| < 1/L = R$ (with the convention $1/0 = \infty$ if $L = 0$, $1/\infty = 0$ if $L = \infty$). $\blacksquare$

> [!note]- Lemma 2: Weierstrass $M$-test
> **Statement:** If $\sum f_n$ is a series of functions on a set $S$ and $|f_n(z)| \leq M_n$ for all $z \in S$ with $\sum M_n < \infty$, then $\sum f_n$ converges uniformly on $S$.
>
> **Hint:** Tails of the partial sums are uniformly bounded by tails of $\sum M_n$, which are small.
>
> **Why needed:** Upgrades pointwise to uniform.
>
> > [!note]- Full proof
> > Let $S_N(z) = \sum_{n=0}^N f_n(z)$ and $S(z) = \lim S_N(z)$ (which exists for each $z$ by comparison with $\sum M_n$). For $M, N$ with $N > M$: $|S_N(z) - S_M(z)| \leq \sum_{n = M+1}^N |f_n(z)| \leq \sum_{n=M+1}^N M_n$. The right side is independent of $z$ and goes to $0$ as $M \to \infty$ (Cauchy criterion for $\sum M_n$). So $\sup_z |S(z) - S_M(z)| \to 0$ as $M \to \infty$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $L = \limsup_{n \to \infty} |c_n|^{1/n}$ and $R = 1/L$ (with conventions).
>
> **Convergence on $|z - a| < R$.** Take $z$ with $|z - a| = \rho < R$. Then $L\rho < 1$. By definition of $\limsup$, for any $\varepsilon > 0$ with $L + \varepsilon < 1/\rho$, there is $N$ such that $|c_n|^{1/n} < L + \varepsilon$ for $n \geq N$, i.e., $|c_n| < (L + \varepsilon)^n$. Then $|c_n (z - a)^n| < ((L + \varepsilon)\rho)^n$, and the geometric series $\sum ((L+\varepsilon)\rho)^n$ converges since $(L + \varepsilon)\rho < 1$. By comparison, $\sum |c_n (z - a)^n|$ converges, i.e., $\sum c_n (z - a)^n$ converges absolutely.
>
> **Divergence on $|z - a| > R$.** Take $z$ with $|z - a| = \rho > R$, so $L\rho > 1$. By definition of $\limsup$, there is a subsequence $n_k$ with $|c_{n_k}|^{1/n_k} > 1/\rho - \varepsilon$ for $\varepsilon$ small enough that $(1/\rho - \varepsilon)\rho > 1$ does *not* hold — actually, $|c_{n_k}|^{1/n_k} \to L > 1/\rho$ along some subsequence, so $|c_{n_k}| \rho^{n_k}$ does not go to $0$, and the series diverges (term does not go to zero).
>
> **Uniform convergence on $\overline{D(a, r)}$ for $0 < r < R$.** Set $M_n = |c_n| r^n$. By the absolute convergence at $z = a + r$ (which has $|z - a| = r < R$), $\sum M_n < \infty$. For $z \in \overline{D(a, r)}$, $|c_n (z - a)^n| \leq |c_n| r^n = M_n$. By the Weierstrass $M$-test (Lemma 2), $\sum c_n (z - a)^n$ converges uniformly on $\overline{D(a, r)}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Power series of generating functions.** In **combinatorics**, generating functions $\sum a_n z^n$ for counting sequences have radii of convergence reflecting the growth rate of $a_n$. Catalan numbers $C_n \sim 4^n/n^{3/2}$ give $R = 1/4$, while $a_n = n!$ gives $R = 0$ (the series is a formal object, not a function).

**Spectral radius in operator theory.** For a bounded linear operator $T$ on a Banach space, the resolvent $(zI - T)^{-1}$ has a power series expansion $\sum T^n/z^{n+1}$ valid for $|z| > $ the spectral radius. The spectral radius is exactly $\limsup \lVert T^n\rVert^{1/n}$ — same formula, in operator norms.

**Radius limited by nearest singularity.** A function holomorphic on a region with singularities has a power series at any interior point whose radius is exactly the distance to the *nearest singularity*. This is a stronger statement (proved with CIF in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]]) that gives geometric meaning to the radius formula.

---

# Bridges

- **[[Thm - Power Series is Holomorphic with Termwise Derivative]]** — the next theorem: power series are not just convergent but holomorphic, with termwise derivative. Builds on the uniform-convergence statement.

- **[[Thm - Identity Theorem for Power Series]]** — uses the analytic structure (power series determined by coefficients) to prove uniqueness on the disc.

- **[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]** — the converse direction in CA II: every holomorphic function locally *is* a power series with the radius given by this formula.
