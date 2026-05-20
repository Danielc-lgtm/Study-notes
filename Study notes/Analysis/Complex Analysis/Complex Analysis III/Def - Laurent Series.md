---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Power Series and Radius of Convergence"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Notation

Throughout, $a \in \mathbb{C}$ is the centre of the expansion, $c_n \in \mathbb{C}$ are coefficients indexed by $n \in \mathbb{Z}$ (both positive and negative), and $A(a; r, R) = \{z : r < |z - a| < R\}$ denotes an annulus with inner radius $r \geq 0$ and outer radius $R \leq \infty$. We write $\sum_{n=-\infty}^\infty c_n (z - a)^n$ for a Laurent series; the **principal part** is the sum over $n < 0$ and the **regular** (or **holomorphic**) part is the sum over $n \geq 0$. The full registry lives on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Axiom Motivation

A power series $\sum_{n \geq 0} c_n (z - a)^n$ represents a function holomorphic on a disc, and conversely every function holomorphic on a disc has a power series expansion (Taylor's theorem for holomorphic functions). The natural question: what is the analogous object for a function holomorphic on a *punctured disc* or, more generally, on an *annulus*?

The obstruction is that a function holomorphic on the punctured disc $D(a, R) \setminus \{a\}$ may blow up at $a$ — think of $1/(z - a)$ or $e^{1/(z-a)}$ — and a series in nonnegative powers of $(z - a)$ cannot represent such a function, because every term vanishes (or stays bounded) as $z \to a$. We need *negative* powers of $(z - a)$ in the expansion, because $(z - a)^{-k}$ blows up as $z \to a$ with the right rate.

So the natural generalization of a power series is a *two-sided* series $\sum_{n=-\infty}^\infty c_n (z - a)^n$, with both positive and negative powers allowed. The convergence question becomes: when does such a series converge? The nonnegative-power part $\sum_{n \geq 0} c_n (z - a)^n$ has a radius of convergence $R$ — converges on $\{|z - a| < R\}$ by the standard root-test theorem. The negative-power part $\sum_{n \geq 1} c_{-n}(z - a)^{-n}$ is, substituting $u = 1/(z - a)$, the power series $\sum_{n \geq 1} c_{-n} u^n$ in $u$, which has its own radius of convergence $1/r$ — and converges for $|u| < 1/r$, i.e. $|z - a| > r$.

So the natural domain of convergence is the *intersection*: an annulus $A(a; r, R)$ with $r < R$. On this annulus, both halves of the series converge, and they sum to a well-defined holomorphic function. Outside the annulus, at least one half diverges. This is the geometric heart of the Laurent series: a power series converges on a disc, a Laurent series converges on an annulus.

What would break with a different definition? Allowing both positive and negative powers is forced: we need positive powers for the holomorphic-on-the-disc part, negative powers for the blow-up-at-the-centre part. Allowing only finitely many negative powers (a *meromorphic* series with a pole) would handle poles but not essential singularities. Allowing infinitely many positive powers and only finitely many negative is exactly the meromorphic case — a useful sub-case but not general enough. The two-sided unbounded series is the unique object capturing all isolated singularities and annular domains.

A subtle point: the *uniqueness* of the expansion requires the centre $a$ to be fixed and the annulus to be specified. The same function may have *different* Laurent expansions around different centres, or even around the same centre but on different annuli. For instance, $1/(z(z - 1))$ has one Laurent expansion on $0 < |z| < 1$ and another on $1 < |z|$ — both around $a = 0$, both valid, but different series.

---

# The Definition

A **Laurent series** centred at $a \in \mathbb{C}$ is a formal sum
$$\sum_{n=-\infty}^\infty c_n (z - a)^n$$
where $c_n \in \mathbb{C}$ for every $n \in \mathbb{Z}$. The **principal part** at $a$ is
$$\sum_{n=1}^\infty c_{-n}(z - a)^{-n},$$
the sum of negative-power terms. The **regular part** (also called the **holomorphic part**) is
$$\sum_{n=0}^\infty c_n(z - a)^n,$$
the sum of nonnegative-power terms.

**Convergence.** The Laurent series **converges** at $z \neq a$ if both the principal part and the regular part converge at $z$. The natural domain of convergence is an annulus $A(a; r, R)$ with
$$\frac{1}{R} = \limsup_{n \to \infty} |c_n|^{1/n}, \qquad r = \limsup_{n \to \infty} |c_{-n}|^{1/n}.$$
On any closed sub-annulus $A(a; r', R') \subseteq A(a; r, R)$ with $r < r' < R' < R$, the series converges absolutely and uniformly.

**Sum.** The sum of a Laurent series on its annulus of convergence is a holomorphic function. The coefficients can be recovered from the sum by
$$c_n = \frac{1}{2\pi i}\oint_{|z - a| = \rho} \frac{f(z)}{(z - a)^{n+1}}\,dz, \qquad n \in \mathbb{Z},$$
where $\rho$ is any radius in $(r, R)$ (the integral is independent of $\rho$ within the annulus, by Cauchy's theorem applied to the holomorphic-on-the-annulus integrand).

---

# Relate to Other Fields / Compression

A Laurent series is the **complex analog of a formal Laurent series** in algebra: an element of the ring $\mathbb{C}((z - a))$, defined as the field of fractions of the power series ring $\mathbb{C}[[z - a]]$. Algebraically, $\mathbb{C}((z - a))$ consists of formal sums with finitely many negative powers; complex-analytically, Laurent series may have infinitely many. The algebraic version is the meromorphic case; the analytic version includes essential singularities.

A Laurent series is also a **Fourier series in disguise**. Substituting $z = a + \rho e^{i\theta}$ for fixed $\rho$ in the annulus, a Laurent series becomes $\sum c_n \rho^n e^{in\theta}$ — a Fourier series in $\theta$ with coefficients $c_n \rho^n$. The Laurent coefficient formula $c_n = (2\pi i)^{-1}\oint f(z)(z - a)^{-n-1}\,dz$ is, after this substitution, the standard Fourier coefficient integral $c_n = (2\pi)^{-1}\int_0^{2\pi} f(a + \rho e^{i\theta}) e^{-in\theta}\,\rho^{-n}\,d\theta$. So Laurent series unify the theories of complex-analytic singularities and harmonic-analytic Fourier expansions on a circle.

In **algebraic geometry**, Laurent series are the local picture near a singular point of a curve: the **complete local ring** at a point on a smooth curve is $\mathbb{C}[[t]]$ (power series), and the **Laurent expansion at a point** is in the fraction field $\mathbb{C}((t))$. Residues, defined via Laurent coefficients, are intrinsic invariants of differential forms on the curve.

---

# Examples / Corollaries

**Is an instance — geometric series.** For $|z| < 1$, $\frac{1}{1 - z} = \sum_{n=0}^\infty z^n$ — a power series, hence trivially a Laurent series with $c_n = 0$ for $n < 0$. For $|z| > 1$, the same function expands differently: $\frac{1}{1 - z} = -\frac{1}{z}\cdot\frac{1}{1 - 1/z} = -\sum_{n=1}^\infty z^{-n}$, a Laurent series with only negative-power terms. *Same function, two different Laurent expansions on two different annuli.*

**Is an instance — $e^z/z$ around $z = 0$.** Since $e^z = \sum_{n=0}^\infty z^n/n!$, we have $e^z/z = \sum_{n=0}^\infty z^{n-1}/n! = 1/z + 1 + z/2! + z^2/3! + \ldots$, valid on $0 < |z| < \infty$. The principal part is just $1/z$ (one negative-power term), so this function has a *simple pole* at $0$, and the residue (the coefficient of $1/z$) is $1$.

**Is an instance — $e^{1/z}$ around $z = 0$.** Since $e^w = \sum_{n=0}^\infty w^n/n!$, substituting $w = 1/z$ gives $e^{1/z} = \sum_{n=0}^\infty z^{-n}/n!$, valid on $0 < |z| < \infty$. Infinitely many negative-power terms, so this function has an *essential singularity* at $0$. The residue (the coefficient of $1/z$) is $1$ (from the $n = 1$ term).

**Is NOT an instance — a series with both centre points.** A "Laurent series" of the form $\sum c_n (z - a)^n + \sum d_n (z - b)^n$ with $a \neq b$ is not a single Laurent series; it is a sum of two Laurent series with different centres. The Laurent expansion requires a single centre, and the annulus of convergence is centred at that centre.

**Calibration check — uniqueness on a fixed annulus.** On a *fixed* annulus $A(a; r, R)$, the Laurent expansion of a holomorphic function is unique. Two different expansions on the same annulus would, by the coefficient formula, give different values of the integral $\oint f(z)(z - a)^{-n-1}\,dz$ — contradiction. So the *function plus the annulus* determine the coefficients.

**Calibration check — convergence on an annulus.** For $1 < |z| < 2$, the function $\frac{1}{(z - 1)(z - 2)} = \frac{1}{z - 2} - \frac{1}{z - 1}$ has the Laurent expansion (around $a = 0$): $\frac{1}{z - 2} = -\frac{1}{2}\cdot\frac{1}{1 - z/2} = -\frac{1}{2}\sum_{n=0}^\infty (z/2)^n$ (valid for $|z| < 2$) and $-\frac{1}{z - 1} = -\frac{1}{z}\cdot\frac{1}{1 - 1/z} = -\sum_{n=1}^\infty z^{-n}$ (valid for $|z| > 1$). Adding, the full Laurent expansion has both positive and negative power terms.

**Corollary — Taylor as a special case.** A power series (no negative-power terms) is a Laurent series whose principal part is zero. The annulus of convergence is $A(a; 0, R)$ — a punctured disc — but since the principal part is zero, the expansion extends to the full disc $D(a, R)$.

---

# Unlocked by This

> [!tip] Laurent Series Theorem and Existence of Expansions *(from §3.3)*
> [[Thm - Laurent Series Theorem|Existence:]] every function holomorphic on an annulus has a unique Laurent expansion. This is the foundational theorem of singularity analysis.

> [!tip] Classification of Isolated Singularities *(from §3.3)*
> The structure of the negative-power part of the Laurent expansion at an isolated singularity classifies the singularity: zero negative terms = [[Def - Removable Singularity, Pole, Essential Singularity|removable]]; finitely many = pole; infinitely many = essential.

> [!tip] Residue *(from §3.3)*
> The [[Def - Residue|residue]] of $f$ at $a$ is the single Laurent coefficient $c_{-1}$. Of all the Laurent coefficients, this is the one that survives integration around a small circle: $\oint f\,dz = 2\pi i c_{-1}$.
