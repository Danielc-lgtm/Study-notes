---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Rouché's Theorem"
  - "Thm - Argument Principle"
tags: [analysis, complex-analysis, algebra]
---

# Notation

$p(z) = z^n + a_{n-1}z^{n-1} + \ldots + a_1 z + a_0$ is a monic polynomial of degree $n \geq 1$, with complex coefficients. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Motivation

The **Fundamental Theorem of Algebra (FTA)** states: every nonconstant polynomial with complex coefficients has at least one complex root. Equivalently, a degree-$n$ polynomial has exactly $n$ roots in $\mathbb{C}$, counted with multiplicity. Equivalently, $\mathbb{C}$ is algebraically closed.

This is one of the most important theorems in mathematics, with proofs in many flavors (algebraic, topological, complex-analytic, real-analytic). The complex-analytic proof via Rouché's theorem is short, clean, and illustrates the power of contour integration.

The key insight: a polynomial $z^n + a_{n-1}z^{n-1} + \ldots + a_0$ is *approximately equal to $z^n$* when $|z|$ is large — the lower-order terms become negligible. Since $z^n$ has $n$ roots (an $n$-fold zero at $0$) in any disc $|z| < R$ around the origin, Rouché's theorem forces the polynomial to also have $n$ roots in such a disc, provided $R$ is large enough that the lower-order terms are dominated.

---

# Sources and Targets

**Sources (Input Broadening)**

**Any nonconstant polynomial with complex coefficients.** Property $B$: $p(z) = a_n z^n + a_{n-1}z^{n-1} + \ldots + a_0$ with $a_n \neq 0$. Bridge: divide by $a_n$ to get monic; FTA applies to the monic version.

**Polynomials with real coefficients.** Property $B$: $a_i \in \mathbb{R}$. Bridge: FTA still applies; the roots are complex conjugate pairs (since $\overline{p(z)} = p(\bar z)$ for real-coefficient $p$).

**Companion matrices of linear ODEs.** Property $B$: looking for eigenvalues of an $n \times n$ matrix. Bridge: eigenvalues are roots of the characteristic polynomial $\det(zI - A)$, a degree-$n$ polynomial. FTA gives existence of $n$ eigenvalues in $\mathbb{C}$.

**Targets (Output Amplification)**

Combine with **algebraic closure of $\mathbb{C}$.** Amplified result: every polynomial factors as $p(z) = a_n\prod_{k=1}^n(z - z_k)$. Used extensively in factoring, partial fractions, and root analysis.

Combine with **the structure of $\mathbb{C}[x]/(p(x))$.** Property $D$: $p$ is a degree-$n$ polynomial. Amplified result $E$: $\mathbb{C}[x]/(p) \cong \mathbb{C}^n$ (if $p$ has distinct roots) or a sum of Jordan-block-like rings (general case). Used in algebra and commutative algebra.

Combine with **spectral theorem for normal operators.** Property $D$: $A$ a normal $n \times n$ matrix. Amplified result $E$: $A$ has $n$ eigenvalues (by FTA) and is unitarily diagonalizable (by orthogonal eigenvectors). The spectral theorem rests on FTA giving the eigenvalues.

---

# Why Is It True

The intuition is that a polynomial is "asymptotically equal to its leading term": as $|z| \to \infty$, $p(z)/z^n \to 1$. So for large $|z|$, $p(z)$ behaves like $z^n$, which has $n$ roots (all at $0$). Rouché formalizes this: on a large enough circle, the difference $|p(z) - z^n|$ is dominated by $|z^n|$, so $p$ has the same root count as $z^n$ inside the circle.

Why this works geometrically: as $z$ traces a large circle, $p(z)$ traces a curve that winds around $0$ the same number of times as $z^n$ does — namely $n$ times. The argument principle says this winding number equals the zero count.

The result is sharp: a polynomial of degree $n$ has *exactly* $n$ roots, not more and not fewer. The "exactly $n$" comes from counting with multiplicity (a double root counts twice).

---

# What Makes This Hard

The non-obvious step is **choosing $R$ large enough**: explicitly, $R$ must satisfy $R^n > |a_{n-1}|R^{n-1} + \ldots + |a_0|$, which holds for $R$ larger than $\max(1, |a_0| + \ldots + |a_{n-1}|)$ (a crude bound). The main pedagogical point is that *any sufficiently large $R$* works — Rouché only requires the inequality to hold on the boundary, not throughout the disc.

A common confusion: students sometimes think the polynomial needs more conditions (real coefficients, leading coefficient $1$). FTA works for any nonconstant polynomial over $\mathbb{C}$.

---

# Rederivation Scaffold

**High-level strategy:**
On a large circle $|z| = R$, the polynomial $p(z)$ is dominated by its leading term $z^n$. By Rouché, $p$ and $z^n$ have the same number of zeros inside $|z| < R$. $z^n$ has $n$ zeros at $0$ (counted with multiplicity); so does $p$.

**Subgoal decomposition:**

1. **Estimate $|p(z) - z^n|$ on a large circle.** $|p(z) - z^n| = |a_{n-1}z^{n-1} + \ldots + a_0| \leq |a_{n-1}|R^{n-1} + \ldots + |a_0|$ on $|z| = R$.

2. **Choose $R$ large enough.** Need $|a_{n-1}|R^{n-1} + \ldots + |a_0| < R^n$, equivalently $|a_{n-1}|/R + |a_{n-2}|/R^2 + \ldots + |a_0|/R^n < 1$. For $R \geq |a_{n-1}| + |a_{n-2}| + \ldots + |a_0| + 1$, this is at most $|a_{n-1}|/R + \ldots + |a_0|/R^n \leq (|a_{n-1}| + \ldots + |a_0|)/R < 1$.

3. **Apply Rouché's theorem.** With $f = z^n, g = p$: $|f - g| < |f|$ on $|z| = R$. So $N(p, |z| < R) = N(z^n, |z| < R) = n$.

4. **Conclude.** $p$ has $n$ zeros in $|z| < R$, hence in $\mathbb{C}$ (any zero of $p$ must be in some disc, and we've covered them).

---

# Formal Proof

> [!note]- Complete formal proof
> Let $p(z) = z^n + a_{n-1}z^{n-1} + \ldots + a_0$ be a monic polynomial of degree $n \geq 1$ (the leading coefficient $1$ is no loss of generality; divide if needed).
>
> Choose $R > 0$ such that $R > 1 + |a_{n-1}| + |a_{n-2}| + \ldots + |a_0|$.
>
> On the circle $|z| = R$:
> $$|p(z) - z^n| = |a_{n-1}z^{n-1} + \ldots + a_0| \leq |a_{n-1}|R^{n-1} + \ldots + |a_0|$$
> $$\leq (|a_{n-1}| + |a_{n-2}| + \ldots + |a_0|) R^{n-1} < (R - 1) R^{n-1} < R^n = |z^n|.$$
>
> So $|p(z) - z^n| < |z^n|$ on $|z| = R$. By [[Thm - Rouché's Theorem|Rouché's theorem]], $p$ and $z^n$ have the same number of zeros in $|z| < R$.
>
> $z^n$ has a single zero at $z = 0$ with multiplicity $n$, so $N(z^n, |z| < R) = n$.
>
> Therefore $N(p, |z| < R) = n$. Since this holds for *every* sufficiently large $R$, and any zero of $p$ lies in some sufficiently large disc, the polynomial $p$ has exactly $n$ zeros in $\mathbb{C}$, counted with multiplicity. $\blacksquare$
>
> **Corollary (algebraic closure).** $\mathbb{C}$ is algebraically closed: every polynomial of degree $\geq 1$ over $\mathbb{C}$ has a root in $\mathbb{C}$.

---

# Cross-Field Exercise Suggestions

**Eigenvalue existence for $n \times n$ matrices.** Apply FTA to $\det(\lambda I - A)$, a degree-$n$ polynomial in $\lambda$. Conclude that $A$ has exactly $n$ eigenvalues in $\mathbb{C}$, counted with algebraic multiplicity. This is the existence theorem for spectra of finite-dimensional operators.

**Stability of polynomial perturbations.** A polynomial close to a known stable one (all roots in left half-plane) is also stable (by Rouché applied on the boundary of the right half-plane). This is the source of *robust stability* in control theory.

**Locating zeros of polynomials.** Combine FTA (giving $n$ zeros total) with Rouché on smaller circles to localize zeros to specific regions. Example: $p(z) = z^5 + 3z + 1$. On $|z| = 1$, $|p - 3z| = |z^5 + 1| \leq 2 < 3 = |3z|$, so by Rouché $p$ has the same zero count as $3z$ in $|z| < 1$, namely $1$. So one zero in $|z| < 1$, four zeros in $|z| > 1$.

---

# Bridges

- **[[Thm - Rouché's Theorem]]** — the engine of the proof.

- **[[Thm - Argument Principle]]** — underlies Rouché.

- **[[Thm - Liouville's Theorem]]** (in CA II) — an alternative proof of FTA via Liouville.

---

# Unlocked by This

> [!tip] Spectral Theorem *(from Linear Algebra)*
> The existence of eigenvalues is a direct consequence of FTA applied to the characteristic polynomial. From there, the **spectral theorem** for normal operators (diagonalizability via unitary transforms) and the **Jordan normal form** (general matrices) build on FTA.

> [!tip] Algebraic Closure of $\mathbb{C}$ *(from Algebra)*
> $\mathbb{C}$ is the algebraic closure of $\mathbb{R}$ (smallest algebraically closed field containing $\mathbb{R}$). This is a foundational fact in algebra, abstract field theory, and Galois theory.
