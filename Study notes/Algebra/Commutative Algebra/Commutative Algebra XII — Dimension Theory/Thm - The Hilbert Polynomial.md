---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - The Hilbert Function and Hilbert Polynomial"
  - "Thm - Hilbert-Serre and Rationality of the Poincare Series"
  - "Def - Graded Ring and Graded Module"
  - "Def - Composition Series and Length"
tags: [algebra, commutative-algebra]
---

# Notation

All rings commutative with $1$. Let $A = \bigoplus_{n\geq 0}A_n$ be a Noetherian [[Def - Graded Ring and Graded Module|graded ring]] with $A_0$ Artinian, generated as an $A_0$-algebra by $s$ homogeneous elements **of degree one** ($k_1 = \cdots = k_s = 1$, the *standard graded* case). Let $M = \bigoplus_n M_n \neq 0$ be a finitely generated graded $A$-module, $\ell$ the [[Def - Composition Series and Length|length]] over $A_0$, $d = d(M)$ the order of the pole of the [[Def - The Hilbert Function and Hilbert Polynomial|Poincaré series]] $P(M,T)$ at $T=1$. We use the convention $\binom{n}{-1} = 0$ for $n \geq 0$ and $\binom{-1}{-1} = 1$, and $\deg 0 = -1$. The full registry is on [[Commutative Algebra XII — Dimension Theory]].

---

# Statement

> **Theorem (Hilbert polynomial).** Let $A$ be a standard graded Noetherian ring (generators in degree one) with $A_0$ Artinian, and $M \neq 0$ a finitely generated graded $A$-module with $d = d(M)$. Then there is a **unique** polynomial $\mathrm{HP}_M \in \mathbb{Q}[T]$ of degree $d - 1$ such that
> $$\ell(M_n) = \mathrm{HP}_M(n) \qquad \text{for all sufficiently large } n.$$
> The leading coefficient of $\mathrm{HP}_M$ is $f(1)/(d-1)!$, where $P(M,T) = f(T)/(1-T)^d$ with $f(1) \neq 0$. The polynomial $\mathrm{HP}_M$ is **numerical**: $\mathrm{HP}_M(\mathbb{Z}) \subseteq \mathbb{Z}$, though in general $\mathrm{HP}_M \notin \mathbb{Z}[T]$.

The associated **Hilbert–Samuel** statement (proved by the same mechanism, summing the Hilbert function — Lemma 3 below): the partial-sum function $n \mapsto \ell(M_0) + \cdots + \ell(M_{n-1}) = \ell\big(\bigoplus_{j<n}M_j\big)$ is eventually a polynomial of degree $d$, one higher.

---

# Motivation

[[Thm - Hilbert-Serre and Rationality of the Poincare Series|Hilbert–Serre]] tells you the Poincaré series is rational; this theorem cashes that rationality into a concrete, computable polynomial. The point is that "rational function" is still an analytic object, whereas "$\ell(M_n) = \mathrm{HP}_M(n)$ for large $n$" is a finite recipe: once you know the finitely many coefficients of $\mathrm{HP}_M$, you know the Hilbert function for all large $n$, and you can read its *degree* and *leading coefficient* directly. Those two numbers are the geometric payload — degree gives dimension, leading coefficient gives multiplicity/degree of the variety — so the Hilbert polynomial is the form in which the Hilbert function becomes a geometric invariant.

The restriction to standard grading (all generators in degree one) is what upgrades "rational" to "polynomial". With mixed degrees the denominator is $\prod(1-T^{k_i})$, whose partial-fraction expansion at the various roots of unity produces a *quasi-polynomial* — a polynomial with periodic coefficients — not a genuine polynomial. The degree-one hypothesis collapses the denominator to a pure power $(1-T)^d$, all poles sit at $T=1$, and the expansion is a single polynomial. This is why projective varieties (whose coordinate rings are standard graded) have honest Hilbert polynomials, while weighted projective spaces only have Hilbert quasi-polynomials.

The theorem also explains the curious fact that $\mathrm{HP}_M$ has rational, non-integer coefficients yet takes integer values. The Hilbert function counts lengths, so $\ell(M_n) \in \mathbb{Z}$; but the natural basis for the polynomials that express it is not $\{1, T, T^2,\dots\}$ but the binomial polynomials $\{\binom{T}{j}\}$, in which the coefficients *are* integers. The theorem is most honestly stated as "$\mathrm{HP}_M$ is an integer combination of binomial coefficients", and its rational $T$-coefficients are an artifact of insisting on the monomial basis.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "standard graded $A$, finitely generated graded $M$". The disguised sources are about recognizing standard gradings.

The first disguised source is **a homogeneous quotient of a polynomial ring**, $A = k[X_0,\dots,X_n]/I$ with $I$ homogeneous. The property $B$ is "$A$ is generated in degree one over a field". Since the $X_i$ have degree one, $B$ implies the standard-graded hypothesis, and $\mathrm{HP}_A$ exists. *Example problem:* the Hilbert polynomial of a projective variety, read for dimension and degree.

The second disguised source is **the associated graded ring with the $\mathfrak{m}$-adic filtration**, $G_{\mathfrak{m}}(A) = \bigoplus \mathfrak{m}^n/\mathfrak{m}^{n+1}$. The property $B$ is "$(A,\mathfrak{m})$ Noetherian local". Then $G_{\mathfrak{m}}(A)$ is generated in degree one by the images of generators of $\mathfrak{m}$ — automatically standard graded — so the **Hilbert–Samuel polynomial** $n \mapsto \ell(A/\mathfrak{m}^n)$ exists, of degree $d = \dim A$. The non-obviousness: a local ring with no grading at all produces a standard graded ring and hence a Hilbert polynomial. *Example problem:* compute $\dim A$ as $\deg$ of the Hilbert–Samuel polynomial.

The third disguised source is **a graded module given by generators and relations of degree one**. The property $B$ is "$M$ has a presentation $A^a \to A^b \to M \to 0$ by graded maps of degree zero". Then $M$ is standard-graded-compatible, and $\mathrm{HP}_M$ is computable from the presentation. *Example problem:* compute the Hilbert polynomial of $S/(f,g)$ for a regular sequence $f,g$ by the inclusion–exclusion $\mathrm{HP} = \mathrm{HP}_S - \mathrm{HP}_{S(-\deg f)} - \mathrm{HP}_{S(-\deg g)} + \mathrm{HP}_{S(-\deg f - \deg g)}$.

**Targets (Output Amplification)**

The conclusion is "$\ell(M_n) = \mathrm{HP}_M(n)$ for large $n$, $\deg \mathrm{HP}_M = d - 1$".

Combine $\deg \mathrm{HP}_M = d - 1$ with **the dimension theorem** to compute Krull dimensions. The additional input $D$ is "$M = A/\mathfrak{m}^n$-filtration data, i.e. $G_{\mathfrak{m}}(A)$"; then $d = \dim A$. The result $E$ is that the Krull dimension is computed by polynomial interpolation of a length sequence — a finite, mechanical computation replacing the search over chains of primes. Non-obvious because dimension is defined by chains but computed by counting.

Combine the leading coefficient $f(1)/(d-1)!$ with **a degree-$e$ hypersurface section** to compute geometric degree. The additional input $D$ is "$M = A$ for a projective variety $X$"; then $(d-1)! \times (\text{leading coefficient}) = \deg X$, the number of points in which $X$ meets a generic linear space of complementary dimension. The result $E$ is Bézout-type degree counting. Non-obvious because a single rational number extracted from asymptotic growth equals an intersection number.

Combine the *additivity of $\mathrm{HP}$ along short exact sequences* with **a known submodule** to compute by inclusion–exclusion. The additional input $D$ is "$0 \to M' \to M \to M'' \to 0$"; then $\mathrm{HP}_M = \mathrm{HP}_{M'} + \mathrm{HP}_{M''}$. The result $E$ is that Hilbert polynomials add, so one computes complicated $\mathrm{HP}$ by decomposing into known pieces. Non-obvious in the strength it provides: the whole apparatus of free resolutions becomes a tool for Hilbert-polynomial computation.

---

# Why Is It True

The mechanism is the **binomial expansion of $(1-T)^{-d}$**: the negative-power binomial series has coefficients that *are* a polynomial in the index, of degree exactly $d-1$, and a polynomial numerator $f(T)$ just takes a finite integer combination of shifts of this polynomial — still a polynomial, with leading coefficient scaled by $f(1)$.

Concretely, by [[Thm - Hilbert-Serre and Rationality of the Poincare Series|Hilbert–Serre]] in the standard-graded case, $P(M,T) = f(T)/(1-T)^d$ with $f \in \mathbb{Z}[T]$, $f(1) \neq 0$ (else cancel a factor of $(1-T)$ and lower $d$). Now expand the denominator:
$$(1-T)^{-d} = \sum_{j \geq 0}\binom{j+d-1}{j}T^j = \sum_{j\geq 0} b_j T^j, \qquad b_j = \binom{j+d-1}{d-1}.$$
The crucial fact is that $b_j = \binom{j+d-1}{d-1} = \frac{(j+d-1)(j+d-2)\cdots(j+1)}{(d-1)!}$ is a polynomial in $j$ of degree $d-1$ with leading coefficient $1/(d-1)!$. Multiplying by $f(T) = \sum_{i} a_i T^i$, the coefficient of $T^n$ in $P(M,T)$ is
$$\ell(M_n) = \sum_i a_i\, b_{n-i} = \sum_i a_i \binom{n-i+d-1}{d-1}.$$
For $n \geq \deg f$ every $b_{n-i}$ is given by the polynomial formula (no edge corrections), so $\ell(M_n)$ is a finite sum of polynomials in $n$ — hence a polynomial $\mathrm{HP}_M(n)$. Its degree is $d-1$ (each summand has degree $d-1$ and they cannot all cancel, because the leading coefficients sum to $\frac{1}{(d-1)!}\sum_i a_i = \frac{f(1)}{(d-1)!} \neq 0$). That non-cancellation — the leading coefficient is $f(1)/(d-1)! \neq 0$ — is exactly why $f(1) \neq 0$ was arranged.

**The one-line mechanism: $(1-T)^{-d}$ has coefficients $\binom{n+d-1}{d-1}$, a degree-$(d-1)$ polynomial in $n$; multiplying by the numerator $f$ shifts and combines these into another degree-$(d-1)$ polynomial whose leading coefficient is $f(1)/(d-1)!$, nonzero precisely because $f(1) \neq 0$.**

Uniqueness is automatic: two polynomials agreeing at infinitely many integers (all large $n$) are equal. Integer-valuedness is because $\ell(M_n) \in \mathbb{Z}$ for the infinitely many large $n$, and a numerical polynomial is determined by its values.

---

# What Makes This Hard

The non-obvious step is recognizing that $\binom{n+d-1}{d-1}$ is a *polynomial* in $n$ (degree $d-1$, leading coefficient $1/(d-1)!$) — students often see it as "just a binomial coefficient" and miss that it is the engine producing the polynomial. The second subtlety is the role of $f(1) \neq 0$: it is what guarantees the leading terms do not cancel, so $\deg \mathrm{HP}_M = d-1$ exactly rather than less; one must remember to cancel all factors of $(1-T)$ from $P$ first so that $f(1) \neq 0$ genuinely holds. The most common error is to expect $\mathrm{HP}_M \in \mathbb{Z}[T]$ and be confused by the $\tfrac{1}{2}$ in examples like $\tfrac12 T(T+1)$ — the resolution is that the natural coefficients live in the binomial basis, not the monomial basis.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Write $P(M,T) = f(T)/(1-T)^d$ with $f(1)\neq 0$ via Hilbert–Serre. Expand $(1-T)^{-d}$ as $\sum_j \binom{j+d-1}{d-1}T^j$, note these coefficients are a degree-$(d-1)$ polynomial in $j$, multiply by $f$, and read off that $\ell(M_n)$ is eventually a polynomial of degree $d-1$ with leading coefficient $f(1)/(d-1)!$.

**Subgoal decomposition:**

1. **Normalize the rational form.** Get $P(M,T) = f(T)/(1-T)^d$ with $f \in \mathbb{Z}[T]$ and $f(1) \neq 0$.
   - *Hint:* Hilbert–Serre gives the rational form; cancel all $(1-T)$ factors so $f(1)\neq 0$, defining $d$.
   - *Why needed:* $f(1)\neq 0$ is what makes the eventual degree exactly $d-1$.

2. **Expand the denominator.** Show $(1-T)^{-d} = \sum_j \binom{j+d-1}{d-1}T^j$ and that $\binom{j+d-1}{d-1}$ is a polynomial in $j$ of degree $d-1$, leading coefficient $1/(d-1)!$.
   - *Hint:* Negative binomial series; the falling-factorial form exhibits the polynomial.
   - *Why needed:* It supplies the polynomial that $\ell(M_n)$ will turn out to equal.

3. **Multiply and extract the coefficient.** Show $\ell(M_n) = \sum_i a_i \binom{n-i+d-1}{d-1}$ for $n \geq \deg f$, a polynomial of degree $d-1$ with leading coefficient $f(1)/(d-1)!$.
   - *Hint:* Coefficient of $T^n$ in $f(T)(1-T)^{-d}$; for $n\geq\deg f$ no boundary corrections; sum leading coefficients $= \frac{\sum a_i}{(d-1)!} = \frac{f(1)}{(d-1)!}$.
   - *Why needed:* It is the conclusion — eventual polynomiality, degree, leading coefficient.

4. **Uniqueness and integrality.** Conclude $\mathrm{HP}_M$ is unique and numerical.
   - *Hint:* Agreement at infinitely many points forces equality; integer values at large $n$ give a numerical polynomial.
   - *Why needed:* Completes the "unique numerical polynomial" claim.

---

# Lemma Decomposition

> [!note]- Lemma 1: The negative binomial coefficient is a polynomial
> **Statement:** For fixed $d \geq 1$, the function $j \mapsto \binom{j+d-1}{d-1}$ is a polynomial in $j$ of degree $d-1$ with leading coefficient $1/(d-1)!$, and $(1-T)^{-d} = \sum_{j\geq 0}\binom{j+d-1}{d-1}T^j$.
>
> **Hint:** $\binom{j+d-1}{d-1} = \frac{(j+d-1)(j+d-2)\cdots(j+1)}{(d-1)!}$, a product of $d-1$ linear factors in $j$.
>
> **Why needed:** This is the source of the polynomial; everything else is bookkeeping around it.
>
> > [!note]- Full proof
> > The generalized binomial theorem gives $(1-T)^{-d} = \sum_{j\geq 0}\binom{-d}{j}(-T)^j = \sum_j \binom{j+d-1}{j}T^j$, and $\binom{j+d-1}{j} = \binom{j+d-1}{d-1}$. Writing it out,
> > $$\binom{j+d-1}{d-1} = \frac{(j+d-1)!}{(d-1)!\,j!} = \frac{(j+1)(j+2)\cdots(j+d-1)}{(d-1)!},$$
> > a product of $d-1$ monic linear polynomials in $j$ divided by $(d-1)!$. This is a polynomial in $j$ of degree $d-1$; its leading term is $j^{d-1}/(d-1)!$, so the leading coefficient is $1/(d-1)!$.

> [!note]- Lemma 2: A finite shift-combination of a degree-$e$ polynomial is degree-$e$ unless leading coefficients cancel
> **Statement:** If $p(n)$ has degree $e$ and leading coefficient $c$, then $\sum_i a_i\, p(n - i)$ (finite sum) has degree $\leq e$, with degree exactly $e$ and leading coefficient $c\sum_i a_i$ provided $\sum_i a_i \neq 0$.
>
> **Hint:** Each shift $p(n-i)$ has the same leading term $cn^e$; the lower terms can differ but the top term is $c(\sum a_i)n^e$.
>
> **Why needed:** Applied with $p(n) = \binom{n+d-1}{d-1}$ and $a_i$ the coefficients of $f$, it gives degree $d-1$ and leading coefficient $f(1)/(d-1)!$.
>
> > [!note]- Full proof
> > Write $p(n) = cn^e + (\text{lower})$. Then $p(n-i) = c(n-i)^e + (\text{lower}) = cn^e + (\text{lower in } n)$, since $(n-i)^e = n^e - ein^{e-1} + \cdots$ has the same leading term $cn^e$. Hence $\sum_i a_i p(n-i) = c\big(\sum_i a_i\big)n^e + (\text{terms of degree} < e)$. If $\sum_i a_i \neq 0$ this is degree exactly $e$ with leading coefficient $c\sum_i a_i$; otherwise the top terms cancel and the degree drops. With $a_i$ the coefficients of $f$, $\sum_i a_i = f(1)$.

> [!note]- Lemma 3: Hilbert–Samuel — summing raises the degree by one
> **Statement:** If $g : \mathbb{Z}_{\geq 0} \to \mathbb{Q}$ is eventually a polynomial of degree $e$, then $G(n) = \sum_{k=0}^{n-1}g(k)$ is eventually a polynomial of degree $e+1$, with leading coefficient $(\text{leading coeff of }g)/(e+1)$.
>
> **Hint:** $\sum_{k=0}^{n-1}k^e$ is a polynomial in $n$ of degree $e+1$ (Faulhaber); extend by linearity.
>
> **Why needed:** It promotes "$\ell(\mathfrak{m}^n/\mathfrak{m}^{n+1})$ is polynomial of degree $d-1$" to "$\ell(A/\mathfrak{m}^n)$ is polynomial of degree $d$" — the Hilbert–Samuel statement used in the dimension theorem.
>
> > [!note]- Full proof
> > For a single power, $\sum_{k=0}^{n-1}k^e$ is a polynomial in $n$ of degree $e+1$ with leading coefficient $\frac{1}{e+1}$ (Faulhaber's formula / the integral approximation $\int_0^n x^e\,dx = \frac{n^{e+1}}{e+1}$ made exact). By linearity, if $g(k) = c k^e + (\text{lower})$ for $k \geq n_0$, then $G(n) = \sum_{k<n_0}g(k) + \sum_{k=n_0}^{n-1}g(k)$; the first sum is a constant and the second is, up to a constant, $c\sum_{k=0}^{n-1}k^e + (\text{lower degree sums})$, a polynomial of degree $e+1$ with leading coefficient $c/(e+1)$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — normalize.** By [[Thm - Hilbert-Serre and Rationality of the Poincare Series|Hilbert–Serre]] with all $k_i = 1$, $P(M,T) = g(T)/(1-T)^s$ for some $g \in \mathbb{Z}[T]$. Cancel every common factor of $(1-T)$ to write $P(M,T) = f(T)/(1-T)^d$ with $f(1) \neq 0$; this defines $d = d(M)$, the pole order at $T=1$.
>
> **Step 1 — expand.** By **Lemma 1**, $(1-T)^{-d} = \sum_{j\geq 0} b_j T^j$ with $b_j = \binom{j+d-1}{d-1}$ a polynomial in $j$ of degree $d-1$ and leading coefficient $1/(d-1)!$.
>
> **Step 2 — multiply.** Write $f(T) = \sum_{i=0}^{\deg f} a_i T^i$, $a_i \in \mathbb{Z}$. The coefficient of $T^n$ in $P(M,T) = f(T)(1-T)^{-d}$ is
> $$\ell(M_n) = \sum_{i=0}^{\deg f} a_i\, b_{n-i} = \sum_{i=0}^{\deg f} a_i \binom{n-i+d-1}{d-1}.$$
> For $n \geq \deg f$, every index $n-i \geq 0$, so each $b_{n-i}$ is given by the polynomial formula of Lemma 1 with no edge correction.
>
> **Step 3 — it is a polynomial of the right degree.** By **Lemma 2** applied to $p(n) = b_n = \binom{n+d-1}{d-1}$ (degree $d-1$, leading coefficient $\frac{1}{(d-1)!}$) and the coefficients $a_i$, the function $n \mapsto \sum_i a_i b_{n-i}$ is, for $n \geq \deg f$, a polynomial $\mathrm{HP}_M(n)$ of degree $d-1$ with leading coefficient
> $$\frac{1}{(d-1)!}\sum_i a_i = \frac{f(1)}{(d-1)!} \neq 0.$$
>
> **Step 4 — uniqueness and integrality.** Two polynomials agreeing at all large integers $n$ agree everywhere, so $\mathrm{HP}_M$ is unique. Since $\ell(M_n) \in \mathbb{Z}_{\geq 0}$ for the infinitely many large $n$, $\mathrm{HP}_M$ takes integer values on $\mathbb{Z}$ — it is a numerical polynomial, an integer combination of $\binom{T}{j}$, though typically $\mathrm{HP}_M \notin \mathbb{Z}[T]$.
>
> **Hilbert–Samuel addendum.** Applying **Lemma 3** to $g(n) = \ell(M_n)$ (degree $d-1$), the partial sums $\sum_{k<n}\ell(M_k)$ are eventually a polynomial of degree $d$. In the local case with $M = G_{\mathfrak{m}}(A)$, this is $\ell(A/\mathfrak{m}^n)$, eventually polynomial of degree $d(G_{\mathfrak{m}}(A))$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Faulhaber's formula and sums of powers.** The Hilbert–Samuel half of this theorem is, stripped of algebra, the statement that $\sum_{k=0}^{n-1}\binom{k+d-1}{d-1} = \binom{n+d-1}{d}$ — a hockey-stick identity — and more generally that summing a degree-$e$ polynomial gives a degree-$(e+1)$ one. This is exactly the content of Faulhaber's formulas for $\sum k^e$. The application is non-obvious because a theorem about graded modules reduces, at its combinatorial core, to elementary sum-of-powers identities.

**Asymptotics of coefficients of rational generating functions.** In analytic combinatorics, the coefficients of a rational generating function with a pole of order $d$ at its dominant singularity grow polynomially of degree $d-1$ (when the dominant singularity is at a positive real point). The Hilbert polynomial theorem is the special case where the only singularity is at $T=1$ of order $d$; the same partial-fraction mechanism governs the asymptotics of any rational generating function. The bridge: "pole order $\to$ polynomial growth degree" is a general principle of which this is the cleanest instance.

**Ehrhart's theorem for lattice polytopes.** For a lattice polytope $P$ of dimension $d$, the lattice-point count $L_P(n) = |nP \cap \mathbb{Z}^N|$ is eventually (in fact always, for lattice $P$) a polynomial in $n$ of degree $d$, the Ehrhart polynomial, with leading coefficient $\operatorname{vol}(P)$. This is the Hilbert polynomial of the semigroup ring of the cone over $P$, and Ehrhart reciprocity mirrors Serre duality. The application is non-obvious because counting lattice points in dilated polytopes is geometric, yet it is governed by the same eventual-polynomiality theorem.

---

# Bridges

- **[[Thm - Hilbert-Serre and Rationality of the Poincare Series|Hilbert–Serre]]** — the input. Hilbert–Serre gives the rational form $f(T)/(1-T)^d$; this theorem extracts the eventual polynomial by binomial expansion. The two are a matched pair: rationality (the algebraic finiteness) and polynomiality (its numerical consequence). Without the standard-graded hypothesis here, one gets only a quasi-polynomial.

- **[[Thm - The Dimension Theorem for Noetherian Local Rings|The dimension theorem]]** — the application. Applied to $G_{\mathfrak{m}}(A)$, the Hilbert–Samuel polynomial $\ell(A/\mathfrak{m}^n)$ has degree $d(G_{\mathfrak{m}}(A))$, and the dimension theorem proves this equals $\dim A$. So this theorem provides the *degree* that the dimension theorem identifies with Krull dimension.

- **[[Def - The Hilbert Function and Hilbert Polynomial|The Hilbert function]]** — the definitional home. This theorem is the existence-and-uniqueness statement that makes "the Hilbert polynomial" a well-defined object; the definition page records what it is, this page proves it exists with the claimed degree and leading coefficient.

- **Numerical polynomials and the binomial basis** — the algebraic framework. The theorem's natural statement is that $\mathrm{HP}_M = \sum_j c_j \binom{T}{j}$ with $c_j \in \mathbb{Z}$; the $\binom{T}{j}$ are a $\mathbb{Z}$-basis for integer-valued polynomials, and the finite-difference operator $\Delta f(n) = f(n+1)-f(n)$ acts on them as a shift. This is the discrete-calculus structure underlying every Hilbert-function computation.

---

# Unlocked by This

> [!tip] Dimension and degree of a projective variety *(from Algebraic Geometry)*
> For a projective variety $X \subseteq \mathbb{P}^N$ with coordinate ring $A$, this theorem produces $\mathrm{HP}_X(n) = \dim_k A_n$ for large $n$, a polynomial whose **degree is $\dim X$** and whose **leading coefficient times $(\dim X)!$ is $\deg X$** — the number of points where $X$ meets a generic linear subspace of complementary dimension. So a single polynomial, computed by interpolating a length sequence, simultaneously yields the two most basic projective invariants. This is the computational foundation of classical projective geometry and the input to Bézout's theorem.

> [!tip] Hilbert–Samuel multiplicity and the local degree *(from Commutative Algebra)*
> The Hilbert–Samuel polynomial $\ell(A/\mathfrak{q}^n)$ for an $\mathfrak{m}$-primary ideal $\mathfrak{q}$ has degree $d = \dim A$ and leading coefficient $e(\mathfrak{q})/d!$, where the integer $e(\mathfrak{q})$ is the **multiplicity** — the local intersection number of the system of parameters generating $\mathfrak{q}$. Multiplicity one (for the maximal ideal, in a nice ring) characterizes **regular local rings**, i.e. smooth points; higher multiplicity quantifies the singularity. This is how the Hilbert polynomial becomes a numerical measure of how singular a point is.
