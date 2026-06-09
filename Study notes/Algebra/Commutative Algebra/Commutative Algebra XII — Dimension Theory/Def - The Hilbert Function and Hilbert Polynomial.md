---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Graded Ring and Graded Module"
  - "Def - Noetherian Ring"
  - "Def - Noetherian and Artinian Module"
  - "Def - Composition Series and Length"
  - "Def - Krull Dimension and Height"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A = \bigoplus_{n \geq 0} A_n$ be a [[Def - Graded Ring and Graded Module|graded ring]] that is [[Def - Noetherian Ring|Noetherian]], with $A_0$ **Artinian** and $A$ generated as an $A_0$-algebra by finitely many homogeneous elements $x_1, \dots, x_s$ with $x_i \in A_{k_i}$, $k_i > 0$. Let $M = \bigoplus_{n \geq 0} M_n \neq 0$ be a finitely generated graded $A$-module. We write $\ell(P)$ for the [[Def - Composition Series and Length|length]] of an $A_0$-module $P$ (the supremum of lengths of composition series; equal to $\dim_k P$ when $A_0 = k$ is a field). The objects defined here are: the **Hilbert function** $n \mapsto \ell(M_n)$, the **Poincaré series** $P(M,T) = \sum_n \ell(M_n)T^n$, and the **Hilbert polynomial** $\mathrm{HP}_M \in \mathbb{Q}[T]$. We write $d(M)$ for the order of the pole of $P(M,T)$ at $T = 1$. The full registry is on [[Commutative Algebra XII — Dimension Theory]].

This is a compound page: it defines four interlocking notions — the **Hilbert function**, the **Poincaré series**, the **Hilbert polynomial**, and the integer **$d(M)$** — because they are the same datum packaged four ways (a sequence, its generating function, the polynomial it eventually equals, and the degree of that polynomial), and none is usable without the others.

---

# Axiom Motivation

We want to attach to a graded module $M$ a *number* that measures its size and, ultimately, its dimension — and we want to extract that number from data we can actually compute. The raw data is the sequence of "sizes" of the graded pieces: in each degree $n$, the piece $M_n$ is a finite-length $A_0$-module, and its length $\ell(M_n)$ is a single non-negative integer. When $A_0 = k$ is a field and $M = A = k[X_1,\dots,X_s]$ is a polynomial ring, $M_n$ is the space of homogeneous polynomials of degree $n$ and $\ell(M_n) = \dim_k M_n = \binom{n+s-1}{s-1}$ — the number of monomials of degree $n$. The function $n \mapsto \ell(M_n)$ is the **Hilbert function**, and the entire theory is the study of its growth.

**Why count by length, and why the standing hypotheses.** For $\ell(M_n)$ to be a finite number we need each $M_n$ to have finite length as an $A_0$-module — and this is exactly what the hypothesis "$A_0$ Artinian, $A$ finitely generated over $A_0$, $M$ finitely generated over $A$" buys us. Finite generation of $M$ over the Noetherian ring $A$ makes each $M_n$ a finitely generated $A_0$-module; the Artinian hypothesis on $A_0$ then makes every finitely generated $A_0$-module both Noetherian and Artinian, hence of finite [[Def - Composition Series and Length|length]]. Drop "$A_0$ Artinian" and $\ell(M_n)$ can be infinite (take $A_0 = k[Y]$, where $A_0$ itself has infinite length over itself), and the whole counting scheme collapses. Length is the right size-measure rather than, say, number of generators, because length is *additive on short exact sequences* — and the entire machinery to come (Hilbert–Serre, the Hilbert polynomial) is built on splicing graded pieces into exact sequences and adding up lengths.

**Why package the function as a generating function.** A sequence of integers is hard to manipulate; its generating function is not. The **Poincaré series** $P(M,T) = \sum_{n \geq 0} \ell(M_n) T^n$ repackages the entire Hilbert function into a single power series, and the payoff is structural: multiplication by a generator $x_i \in A_{k_i}$ shifts degree by $k_i$, which on the generating-function side is multiplication by $T^{k_i}$. This turns the recursive structure of $M$ as an $A$-module into algebraic relations among power series, and the [[Thm - Hilbert-Serre and Rationality of the Poincare Series|Hilbert–Serre theorem]] cashes this in: $P(M,T)$ is a *rational function* with denominator $\prod_i (1 - T^{k_i})$. Rationality is the whole game — a rational function is determined by finitely many coefficients, so the infinitely many values $\ell(M_n)$ are encoded in a finite amount of data.

**Why a polynomial, and why only eventually.** A rational function $f(T)/\prod_i(1-T^{k_i})$ with all $k_i = 1$, i.e. $f(T)/(1-T)^d$, has Taylor coefficients that are *eventually* given by a polynomial in $n$ of degree $d - 1$. This is the **Hilbert polynomial** $\mathrm{HP}_M$: the unique polynomial with $\ell(M_n) = \mathrm{HP}_M(n)$ for all large $n$. Why "eventually" and not "always"? Because the numerator $f(T)$ contributes finitely many low-degree corrections — a few exceptional values $\ell(M_0), \ell(M_1), \dots$ where the module has not yet settled into its asymptotic growth. The polynomial sees only the asymptotics, which is exactly what we want: dimension is an asymptotic notion (how fast does the module grow?), insensitive to finitely many small-degree anomalies. The restriction to $k_i = 1$ (generators in degree one, the **standard graded** case) is what guarantees a genuine polynomial; with mixed degrees $k_i$ one gets a *quasi-polynomial* (a polynomial whose coefficients are periodic in $n$), as the nonstandard-grading example shows.

**Why $\mathrm{HP}_M$ lands in $\mathbb{Q}[T]$ but takes integer values.** The Hilbert polynomial is built from binomial coefficients $\binom{n+d-1}{d-1}$, which are integer-valued functions of the integer $n$ but, written as polynomials in $T$, have rational (non-integer) coefficients: $\binom{T+1}{2} = \tfrac{1}{2}T(T+1) = \tfrac12 T^2 + \tfrac12 T$. So $\mathrm{HP}_M \in \mathbb{Q}[T]$ in general, even though $\mathrm{HP}_M(n) \in \mathbb{Z}$ for all integers $n$. These are the **numerical polynomials** — the $\mathbb{Z}$-linear combinations of $\binom{T}{j}$ — and they are the natural home of every Hilbert polynomial. Demanding $\mathbb{Z}[T]$ would be wrong; the correct invariant is the value-pattern, not the coefficients.

**The punchline: $d(M)$ is the dimension.** All of this exists to define one integer. Let $d(M)$ be the order of the pole of $P(M,T)$ at $T = 1$ — equivalently $1 + \deg \mathrm{HP}_M$, equivalently the asymptotic growth rate of $\ell(M_n)$ (the function $\ell(M_n)$ grows like $n^{d(M)-1}$). For the associated graded ring of a Noetherian local ring this number turns out to *equal the Krull dimension* — that is the [[Thm - The Dimension Theorem for Noetherian Local Rings|dimension theorem]]. The Hilbert function is invented so that this single integer, read off the asymptotics of $\ell(M_n)$, is the dimension.

---

# The Definition

Let $A = \bigoplus_{n \geq 0} A_n$ be a Noetherian graded ring with $A_0$ Artinian, generated as an $A_0$-algebra by homogeneous $x_1,\dots,x_s$ with $x_i \in A_{k_i}$, $k_i > 0$. Let $M = \bigoplus_{n\geq 0} M_n \neq 0$ be a finitely generated graded $A$-module. Each $M_n$ is then a finite-length $A_0$-module.

## Hilbert function

The **Hilbert function** of $M$ is
$$H_M : \mathbb{Z}_{\geq 0} \to \mathbb{Z}_{\geq 0}, \qquad H_M(n) = \ell(M_n),$$
where $\ell$ is length over $A_0$ (equal to $\dim_k M_n$ when $A_0 = k$ is a field).

## Poincaré series

The **Poincaré series** (or Hilbert series) of $M$ is the formal power series
$$P(M, T) = \sum_{n=0}^{\infty} \ell(M_n)\, T^n \ \in\ \mathbb{Z}[[T]].$$

## The integer $d(M)$

By the [[Thm - Hilbert-Serre and Rationality of the Poincare Series|Hilbert–Serre theorem]], $P(M,T) = f(T) / \prod_{i=1}^s (1 - T^{k_i})$ for some $f \in \mathbb{Z}[T]$. The number $d(M)$ is the **order of the pole of this rational function at $T = 1$** (equivalently, the order of vanishing at $T=1$ of the denominator minus that of $f$). One always has $d(M) \geq 0$, with $d(M) = 0$ exactly when $\ell(M_n) = 0$ for all large $n$.

## Eventually-polynomial functions, and the Hilbert polynomial

A function $f : \mathbb{Z}_{\geq 0} \to \mathbb{Z}_{\geq 0}$ is **eventually a polynomial** if there exist $g \in \mathbb{Q}[T]$ and $n_0$ with $f(n) = g(n)$ for all $n \geq n_0$; the polynomial $g$ is then unique, and one defines $\deg f$, the leading coefficient, and the leading term of $f$ to be those of $g$.

When $k_1 = \cdots = k_s = 1$ (the **standard graded** case), the Hilbert function is eventually a polynomial: there is a unique
$$\mathrm{HP}_M \in \mathbb{Q}[T], \qquad \deg \mathrm{HP}_M = d(M) - 1,$$
with $\ell(M_n) = \mathrm{HP}_M(n)$ for all large $n$. This is the **Hilbert polynomial** of $M$. (Convention: $\deg 0 = -1$, so $d(M) = 0 \iff \mathrm{HP}_M = 0$.) In general $\mathrm{HP}_M \in \mathbb{Q}[T] \setminus \mathbb{Z}[T]$, but $\mathrm{HP}_M(\mathbb{Z}_{\geq 0}) \subseteq \mathbb{Z}_{\geq 0}$: it is a **numerical polynomial**.

---

# Categorical / Structural Definition

The Hilbert function is best understood as the **Euler characteristic / additive invariant attached to the Grothendieck group of finite-length graded modules.** Length is the universal additive function on finite-length $A_0$-modules: $\ell$ factors through the Grothendieck group $K_0(\text{f.l. } A_0\text{-mod}) \cong \mathbb{Z}$, and any short exact sequence $0 \to P' \to P \to P'' \to 0$ gives $\ell(P) = \ell(P') + \ell(P'')$. The Poincaré series is then the image of the class $[M] = \sum_n [M_n]T^n$ under the map to $\mathbb{Z}[[T]]$, and **Hilbert–Serre is the statement that the degree-shift action of the generators $x_i$ (multiplication by $T^{k_i}$) makes this class a rational function** — the same structural reason a finitely generated module over $\mathbb{Z}[T_1,\dots,T_s]$ has a finite free resolution, here read off in $K_0$. The additivity of $\ell$ on the exact sequences $0 \to K_n \to M_n \xrightarrow{x_s} M_{n+k_s} \to L_{n+k_s} \to 0$ is precisely what powers the induction in the Hilbert–Serre proof.

---

# Relate to Other Fields / Compression

**The cleanest compression: the Hilbert function is the "dimension of the space of degree-$n$ polynomials on a variety", and its growth rate is the dimension of the variety.** For a projective variety $X \subseteq \mathbb{P}^n$ with homogeneous coordinate ring $A = k[X_0,\dots,X_n]/I(X)$, the Hilbert function $\ell(A_n) = \dim_k A_n$ counts the linearly independent degree-$n$ functions on $X$. If $X$ is a curve this grows linearly, if a surface quadratically, and in general the degree of $\mathrm{HP}_X$ as a polynomial is exactly $\dim X$.

**True name:** the operational name of the Hilbert polynomial is **"$\mathrm{HP}_X(n) = \dfrac{\deg X}{(\dim X)!}\, n^{\dim X} + (\text{lower order})$": its degree is the dimension of $X$ and its leading coefficient encodes the degree of $X$.** This is what you read it for. The whole rational-function apparatus exists to extract these two geometric numbers — dimension (the degree of $\mathrm{HP}$) and degree (the normalized leading coefficient) — from the asymptotics of a count.

This is the algebraic geometer's analogue of the **Weyl law** in spectral geometry, where the number of Laplace eigenvalues below $\lambda$ grows like $C \lambda^{n/2}$ with the exponent recording the dimension of the manifold and the constant its volume. In both cases an asymptotic count of "modes" of bounded size has a leading term whose exponent is the dimension and whose constant is a volume/degree. The numerical-polynomial values also reappear as **Euler characteristics**: $\mathrm{HP}_X(n) = \chi(X, \mathcal{O}_X(n))$ for large $n$, tying the Hilbert polynomial to sheaf cohomology and Riemann–Roch.

---

# Examples / Corollaries

**Is an instance — the polynomial ring.** For $A = k[T_1,\dots,T_s]$ with the standard grading, $A_n$ is the space of homogeneous degree-$n$ polynomials, with $k$-basis the monomials of degree $n$. By stars and bars there are $\binom{n+s-1}{s-1}$ of them, so
$$\ell(A_n) = \binom{n+s-1}{s-1} = \frac{(n+s-1)(n+s-2)\cdots(n+1)}{(s-1)!},$$
a polynomial in $n$ of degree $s-1$ with leading coefficient $1/(s-1)!$. Thus $\mathrm{HP}_A(T) = \binom{T+s-1}{s-1}$, $d(A) = s$, and the Poincaré series is $P(A,T) = \sum_n \binom{n+s-1}{s-1}T^n = (1-T)^{-s}$, matching $d(A) = s$ as the pole order at $T=1$. Note $\dim A = s = d(A)$ — the dimension theorem in its cleanest instance.

**Is an instance — a hypersurface.** For $A = S/(f)$ with $S = k[X_0,\dots,X_n]$ and $f$ homogeneous of degree $e$, multiplication by $f$ is injective and gives the exact sequence $0 \to S(-e) \xrightarrow{f} S \to A \to 0$ of graded modules, so by additivity of length in each degree $\ell(A_n) = \ell(S_n) - \ell(S_{n-e})$. Hence $\mathrm{HP}_A(T) = \binom{T+n}{n} - \binom{T-e+n}{n}$, whose two leading terms $\tfrac{T^n}{n!}$ cancel, leaving a polynomial of degree $n-1$. So $\dim A = n$ as a ring (the projective variety has dimension $n-1$), exactly one less than the ambient $\dim S = n+1$: a single equation drops dimension by one, the Hilbert-function shadow of Krull's principal ideal theorem.

**Is NOT an instance — a nonstandard grading gives a quasi-polynomial, not a polynomial.** Grade $A = k[T_1, T_2]$ by $\deg' T_1 = 1$, $\deg' T_2 = 2$. Then $A_n$ has dimension $\#\{(e_1,e_2) : e_1 + 2e_2 = n\} = \lfloor n/2 \rfloor + 1$, which is $\tfrac{n}{2}+1$ for even $n$ and $\tfrac{n+1}{2}$ for odd $n$ — *not* a single polynomial in $n$, but a quasi-polynomial of period $2$. The Poincaré series is $P(A,T) = 1/\big((1-T)(1-T^2)\big)$, with $k_1 = 1, k_2 = 2$, so the denominator is not a pure power of $(1-T)$ and Proposition 13.9 (which needs all $k_i = 1$) does not apply. This is exactly why the *standard graded* hypothesis is in the definition of $\mathrm{HP}_M$.

**Is NOT an instance — without $A_0$ Artinian there is no Hilbert function.** Take $A = k[Y][X] = A_0[X]$ with $A_0 = k[Y]$ and $X$ in degree $1$. Then $A_1 = k[Y]\cdot X$ has infinite length over $A_0 = k[Y]$, so $\ell(A_1) = \infty$ and the Poincaré series is not even defined over $\mathbb{Z}[[T]]$. The Artinian hypothesis on $A_0$ is not cosmetic — it is what makes the entire construction finite.

**Calibration check.** Compute $\ell(A_n)$ for $A = k[X,Y]$ directly (it should be $n+1$, linear in $n$, so $d = 2$, $\mathrm{HP}_A = T+1$). Verify $\sum_n (n+1)T^n = (1-T)^{-2}$, confirming the pole at $T=1$ has order $2$. Check that $\mathrm{HP}_A = \binom{T+1}{1}\cdot\text{...}$, i.e. that $T+1$ is a numerical polynomial sending $\mathbb{Z}_{\geq 0}$ to $\mathbb{Z}_{\geq 0}$. Finally, confirm that $\deg \mathrm{HP}_A = d(A) - 1 = 1$, the relation that makes $d(A)$ the dimension.

---

# Unlocked by This

> [!tip] The Hilbert polynomial of a projective variety: dimension and degree *(from Algebraic Geometry)*
> For a projective variety $X \subseteq \mathbb{P}^N$ with homogeneous coordinate ring $A$, the Hilbert polynomial $\mathrm{HP}_X(n) = \dim_k A_n$ for large $n$ has **degree equal to $\dim X$** and leading coefficient $\dfrac{\deg X}{(\dim X)!}$, so a single polynomial reads off both the **dimension** and the **degree** of the variety. For $\mathbb{P}^d$ itself, $\mathrm{HP}(n) = \binom{n+d}{d}$, degree $d$, leading coefficient $1/d!$, degree $1$ — see [[Ex - The Hilbert polynomial of projective space]]. This is the computational gateway to intersection theory: degrees multiply under generic intersection (Bézout), and dimensions add up to the ambient dimension.

> [!tip] Euler characteristics and Riemann–Roch *(from Algebraic Geometry)*
> For large $n$ the Hilbert polynomial equals the **Euler characteristic** $\chi(X, \mathcal{O}_X(n)) = \sum_i (-1)^i \dim_k H^i(X, \mathcal{O}_X(n))$ of the twisting sheaf, because the higher cohomology vanishes for $n \gg 0$ (Serre vanishing). The constant term $\mathrm{HP}_X(0) = \chi(X, \mathcal{O}_X)$ is the **arithmetic genus** up to sign. This identifies the Hilbert polynomial with the right-hand side of the **Riemann–Roch theorem**, making the Hilbert function the elementary, length-counting shadow of sheaf cohomology.

> [!tip] Hilbert–Samuel multiplicity and singularities *(from Commutative Algebra / Singularity Theory)*
> Applied to the associated graded ring $G_{\mathfrak{m}}(A)$ of a local ring, the leading coefficient of the Hilbert–Samuel polynomial $\ell(A/\mathfrak{m}^n)$ (times $(d-1)!$) is the **multiplicity** $e(A)$, an integer measuring the severity of the singularity at the closed point: $e(A) = 1$ characterizes regular (smooth) points among nice rings, and higher multiplicity detects worse singularities. This is how the Hilbert function becomes a numerical invariant of singularities.
