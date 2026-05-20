---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis]
---

# Notation

$\{c_n\}_{n=0}^\infty \subseteq \mathbb{C}$ is a sequence of complex coefficients; $a \in \mathbb{C}$ is the centre. The power series is $\sum_{n=0}^\infty c_n (z - a)^n$, evaluated at points $z \in \mathbb{C}$. The radius of convergence is $R \in [0, \infty]$ with $1/0 = \infty, 1/\infty = 0$. We write $\limsup_{n\to\infty} a_n$ for the largest accumulation point of $\{a_n\}$ — equivalently $\inf_N \sup_{n \geq N} a_n$. Full registry on [[Complex Analysis I — Basic Notions]].

---

# Axiom Motivation

A power series $\sum c_n (z - a)^n$ is a *formal* algebraic object — a sequence of complex coefficients — that we want to interpret as a *function* on some subset of $\mathbb{C}$. The basic question is: for which $z$ does the series converge? The answer turns out to be remarkably clean: the set of convergence is a disc centred at $a$.

Why a *disc*? Think about what determines convergence: by the root test, $\sum c_n (z - a)^n$ converges absolutely if $\limsup |c_n (z - a)^n|^{1/n} < 1$, i.e., $|z - a| \cdot \limsup |c_n|^{1/n} < 1$. So the convergence condition depends *only* on $|z - a|$ — the modulus, not the argument. Sets defined by a constraint on the modulus alone are discs (or their complements). This is the source of the disc shape: it is the *natural geometric shape adapted to a condition on modulus*.

The **radius** is then $R = 1/\limsup |c_n|^{1/n}$, the threshold at which the convergence/divergence dichotomy switches. Inside the open disc $|z - a| < R$ the series converges absolutely; outside the closed disc $|z - a| > R$ it diverges. On the boundary circle $|z - a| = R$ the behaviour is genuinely indeterminate — depends on the specific series — and we do not include it in the convergence guarantee.

Why use $\limsup$ rather than $\lim$? Because $|c_n|^{1/n}$ need not converge — it can oscillate. The $\limsup$ always exists (as a value in $[0, \infty]$) and the formula $R = 1/\limsup |c_n|^{1/n}$ then gives the sharp convergence threshold. If the limit happens to exist, $\limsup$ equals it and the formula simplifies. The ratio test $R = \lim |c_n / c_{n+1}|$ also gives the radius when the ratio limit exists, but it does not always — the root test is the universal tool.

The choice of $\limsup$ over $\liminf$ in the formula has a clean reason: $\limsup$ gives the *largest* coefficient growth rate, and the convergence threshold is determined by the worst-case (largest) growth. Beyond $1/\limsup$, even the worst coefficients send the series to infinity; below it, even the worst are dominated.

Convention on the conventions: $\limsup |c_n|^{1/n} = 0$ means coefficients decay arbitrarily fast, so the series converges everywhere — $R = \infty$ ("the convention $1/0 = \infty$"). $\limsup |c_n|^{1/n} = \infty$ means coefficients grow arbitrarily fast, so the series converges only at $z = a$ — $R = 0$ ("the convention $1/\infty = 0$"). These conventions are not arbitrary: they extend the formula to all coefficient sequences without forcing case-splits.

The deep payoff: a power series $f(z) = \sum c_n (z - a)^n$ with $R > 0$ defines a *holomorphic function* on $D(a, R)$, and conversely every holomorphic function on $D(a, R)$ is a power series with this radius (proved in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]]). So power series and holomorphic functions are *the same thing* in disguise, and the radius of convergence is the *natural distance to the nearest singularity*.

---

# The Definition

**Power series.** A **power series** centred at $a \in \mathbb{C}$ is a formal expression
$$\sum_{n=0}^\infty c_n (z - a)^n, \qquad \{c_n\}_{n=0}^\infty \subseteq \mathbb{C}, \quad a \in \mathbb{C}.$$

**Radius of convergence.** The **radius of convergence** is
$$R := \frac{1}{\limsup_{n\to\infty} |c_n|^{1/n}} \in [0, \infty],$$
with the conventions $1/0 = \infty$ and $1/\infty = 0$. Equivalently, $R = \sup\{r \geq 0 : |c_n| r^n \to 0\}$.

**Disc of convergence.** The open disc $D(a, R) = \{z : |z - a| < R\}$ (empty if $R = 0$; all of $\mathbb{C}$ if $R = \infty$) is the **disc of convergence**. On $D(a, R)$ the series converges absolutely; for $|z - a| > R$ it diverges. Behaviour on the circle $|z - a| = R$ is undetermined.

When $R > 0$, the series defines a function $f : D(a, R) \to \mathbb{C}$ by $f(z) := \sum c_n (z - a)^n$.

---

# Relate to Other Fields / Compression

In **real analysis**, the same definition gives the radius of convergence of a real power series. The decisive difference is the *geometry* of the convergence set: in the complex case it is an open disc; in the real case it is an open interval $(a - R, a + R)$. This is because $\mathbb{R}$ has only the one-dimensional notion of "near $a$", while $\mathbb{C}$ has the two-dimensional notion.

In **functional analysis**, the radius of convergence is the inverse of the *spectral radius* of an operator — given a bounded operator $T$ on a Banach space, the series $\sum T^n z^n / n!$ defines $e^{zT}$ for $|z| < $ something, related to the spectral radius. The convergence is the same root-test convergence, transported to operator norms.

In **algebraic geometry**, the formal power series ring $\mathbb{C}[[z - a]]$ is the completion of $\mathbb{C}[z]$ at the maximal ideal $(z - a)$. Power series with positive radius of convergence form a subring — the convergent power series ring — which is the ring of germs of holomorphic functions at $a$.

---

# Examples / Corollaries

**Is an instance — the geometric series.** $\sum z^n$, centre $a = 0$, coefficients all $1$. Then $\limsup |c_n|^{1/n} = 1$, so $R = 1$. Converges on the open unit disc with sum $1/(1 - z)$; diverges on the circle $|z| = 1$ (each term has modulus $1$, fails the divergence test).

**Is an instance — the exponential series.** $\sum z^n/n!$, centre $a = 0$, $c_n = 1/n!$. Stirling gives $|c_n|^{1/n} \sim 1/n \cdot e \to 0$, so $\limsup = 0$ and $R = \infty$. Converges everywhere, defining $\exp(z)$.

**Is an instance — the factorial series.** $\sum n! z^n$, $c_n = n!$. Then $|c_n|^{1/n} = (n!)^{1/n} \to \infty$, so $R = 0$. Converges only at $z = 0$ — a degenerate "function" defined only at one point.

**Is an instance — $\sum z^n/n^2$.** $c_n = 1/n^2$. Then $|c_n|^{1/n} = 1/n^{2/n} \to 1$, so $R = 1$. Converges on $|z| < 1$. On $|z| = 1$ converges absolutely (since $\sum 1/n^2 < \infty$) — boundary behaviour can be benign.

**Is an instance — $\sum z^n/n$.** $c_n = 1/n$. Then $|c_n|^{1/n} = 1/n^{1/n} \to 1$, so $R = 1$. On $|z| = 1$: at $z = 1$ the series is the harmonic series, divergent; at $z = -1$ it is the alternating harmonic series, conditionally convergent. So boundary behaviour can vary point-by-point.

**Is NOT an instance of "convergent on a closed set" — power series convergence is open.** The convergence region is the *open* disc, and the boundary behaviour is genuinely a separate question (Abel's theorem and others address it). One cannot promote convergence on the open disc to convergence on the closed disc without further analysis.

**Corollary — radius is determined by coefficients alone.** The geometric set of convergence depends only on the sequence $\{c_n\}$, not on the function the series represents. (Two distinct series with the same radius may have very different boundary behaviour.)

**Corollary — the ratio test gives the radius when applicable.** If $\lim |c_n/c_{n+1}| = R$ exists in $[0, \infty]$, then this is the radius of convergence. Proof: $|c_{n+1}/c_n| \to 1/R$, so $|c_{n+1} z^{n+1}/(c_n z^n)| = |z| \cdot |c_{n+1}/c_n| \to |z|/R$, ratio test gives convergence for $|z| < R$ and divergence for $|z| > R$.

**Calibration check.** Compute the radii: $\sum n z^n$ ($R = 1$, since $n^{1/n} \to 1$); $\sum 2^n z^n$ ($R = 1/2$); $\sum z^{n!}$ ($R = 1$, sparse series). Verify by the formula and by considering convergence at $z = R - \varepsilon$ and $z = R + \varepsilon$. See [[Ex - Computing radii of convergence]].

---

# Unlocked by This

> [!tip] Holomorphicity of Power Series *(from this topic)*
> A power series with positive radius defines a holomorphic function on its open disc, with derivative given by termwise differentiation. See [[Thm - Power Series is Holomorphic with Termwise Derivative]] and [[Thm - Radius of Convergence Formula and Uniform Convergence on Sub-Discs]].

> [!tip] Analytic = Holomorphic *(from CA II)*
> The remarkable converse — every holomorphic function on a disc is a power series — is proved in [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]] via the Cauchy integral formula. The two notions are equivalent.

> [!tip] Laurent Series *(from CA III)*
> For functions holomorphic on an annulus $r < |z - a| < R$, allowing *negative* powers gives the **Laurent series** $\sum_{n=-\infty}^\infty c_n (z - a)^n$ — the natural extension allowing isolated singularities.
