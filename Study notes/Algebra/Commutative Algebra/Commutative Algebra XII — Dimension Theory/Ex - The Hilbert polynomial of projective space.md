---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - The Hilbert Function and Hilbert Polynomial"
  - "Thm - The Hilbert Polynomial"
  - "Thm - Hilbert-Serre and Rationality of the Poincare Series"
  - "Def - Graded Ring and Graded Module"
  - "Def - Composition Series and Length"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $k$ be a field and $S = k[T_0, T_1, \dots, T_n]$ the standard-graded polynomial ring in $n+1$ variables, the homogeneous coordinate ring of projective space $\mathbb{P}^n_k$. Compute its Hilbert function, Hilbert polynomial, and Poincaré series, and identify the degree and leading coefficient.

Concretely, prove:

1. The graded piece $S_d$ (homogeneous polynomials of degree $d$) has dimension $\dim_k S_d = \binom{n+d}{n}$, so the Hilbert function is $H_S(d) = \binom{n+d}{n}$.
2. This is already a polynomial in $d$ for *all* $d \geq 0$, so the **Hilbert polynomial** is
$$\mathrm{HP}_S(T) = \binom{T+n}{n} = \frac{(T+n)(T+n-1)\cdots(T+1)}{n!},$$
of degree $n$ with leading coefficient $1/n!$.
3. The **Poincaré series** is $P(S, T) = \dfrac{1}{(1-T)^{n+1}}$, with a pole of order $n+1$ at $T=1$, so $d(S) = n+1 = \dim S$.

Interpret: $\deg \mathrm{HP}_S = n = \dim \mathbb{P}^n$ and the leading coefficient $1/n! = \deg(\mathbb{P}^n)/(\dim \mathbb{P}^n)!$ records $\deg \mathbb{P}^n = 1$.

**Recall:**

The objects in play are the Hilbert function, Hilbert polynomial, Poincaré series, and the integer $d(M)$.

![[Def - The Hilbert Function and Hilbert Polynomial#Hilbert function]]

![[Def - The Hilbert Function and Hilbert Polynomial#Poincaré series]]

For $S = k[T_0,\dots,T_n]$ standard graded, $S_d$ is the $k$-vector space of homogeneous degree-$d$ polynomials, with basis the monomials $T_0^{e_0}\cdots T_n^{e_n}$, $\sum e_i = d$. The **stars and bars** count of such monomials — the number of ways to write $d$ as an ordered sum of $n+1$ non-negative integers — is $\binom{d + (n+1) - 1}{(n+1)-1} = \binom{n+d}{n}$.

![[Thm - The Hilbert Polynomial#Statement]]

The key fact about **numerical polynomials**: $\binom{T+n}{n}$ is a polynomial in $T$ of degree $n$ with rational (non-integer) coefficients that nonetheless sends $\mathbb{Z}_{\geq 0}$ to $\mathbb{Z}_{\geq 0}$; its leading coefficient is $1/n!$.

---

# Convergent Strategy

**Problem class.** This is a *direct computation* of a structured invariant — the model example for the entire theory of Hilbert functions, exactly the worked Example 13.8 of the lectures. There is no clever trick to discover; the discipline is to compute three packagings of the same datum (the dimension count $\dim_k S_d$, its generating function, and the polynomial it equals) and to read off the two geometric numbers — *dimension* (the degree of $\mathrm{HP}$) and *degree* (the normalized leading coefficient). The value of the exercise is calibration: every later Hilbert-function computation (hypersurfaces, projective varieties) is a perturbation of this one.

**Assumption pattern.** The hypotheses "standard grading ($k_i = 1$ for all generators), $A_0 = k$ a field, finitely many variables" are exactly the conditions under which the [[Thm - The Hilbert Polynomial|Hilbert polynomial exists as a genuine polynomial]]. The standard grading is the recognisable trigger: it forces the Poincaré-series denominator to be a pure power $(1-T)^{n+1}$ rather than a product of mixed cyclotomic-type factors, which is what makes the Hilbert function eventually (here, always) a polynomial rather than a quasi-polynomial. With $A_0 = k$ a field, length equals $k$-dimension, so $\ell(S_d) = \dim_k S_d$ is a plain monomial count.

**Theorem routing.** The route is: (i) count monomials by stars and bars to get $\dim_k S_d = \binom{n+d}{n}$; (ii) observe this is a polynomial in $d$ of degree $n$, so it *is* its own Hilbert polynomial $\mathrm{HP}_S(T) = \binom{T+n}{n}$ (uniqueness of the eventually-equal polynomial); (iii) sum the generating function $\sum_d \binom{n+d}{n} T^d$ using the binomial series for $(1-T)^{-(n+1)}$, confirming $P(S,T) = (1-T)^{-(n+1)}$ and that the pole order $d(S) = n+1$ matches $1 + \deg \mathrm{HP}_S = n+1$, consistent with $\dim S = n+1$. The leading-coefficient computation reads $\deg \mathbb{P}^n = 1$.

**Key decision point.** The one conceptual move is *not confusing the two dimensions*: the ring $S = k[T_0,\dots,T_n]$ has Krull dimension $n+1$ (it is affine $(n+1)$-space as a ring), but the *projective* variety $\mathbb{P}^n$ it coordinatizes has dimension $n$, and it is the **degree of the Hilbert polynomial** ($n$), not the pole order of the Poincaré series ($n+1$), that equals $\dim \mathbb{P}^n$. The off-by-one — $\deg \mathrm{HP} = d(S) - 1$ — is exactly the passage from the affine cone (dimension $n+1$) to the projective variety (dimension $n$), the cone being one dimension larger than its projectivization. Keeping straight which number is which is the whole subtlety.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XII — Dimension Theory#Legal Operations|the topic page's Legal Operations]]:

1. **Count a graded piece by a monomial basis.** $\dim_k S_d$ equals the number of degree-$d$ monomials, computed by stars and bars.

2. **Recognise an everywhere-polynomial Hilbert function.** When $\dim_k S_d$ is already a polynomial in $d$ for all $d$, that polynomial *is* the Hilbert polynomial (by uniqueness).

3. **Sum a Hilbert function into a Poincaré series.** Use the binomial series $\sum_d \binom{n+d}{n} T^d = (1-T)^{-(n+1)}$.

4. **Read the pole order as $d(S)$ and relate it to $\deg \mathrm{HP}$.** The order of the pole at $T = 1$ is $d(S) = 1 + \deg \mathrm{HP}_S$.

5. **Extract dimension and degree from $\mathrm{HP}$.** $\deg \mathrm{HP} = \dim \mathbb{P}^n$ and the leading coefficient times $(\dim)!$ is $\deg \mathbb{P}^n$.

---

# Hints

> [!note]- Hint 1
> Start with $\dim_k S_d$: this is the number of monomials $T_0^{e_0}\cdots T_n^{e_n}$ of total degree $d$, i.e. the number of solutions in non-negative integers to $e_0 + \cdots + e_n = d$. What standard counting formula gives this?

> [!note]- Hint 2
> Stars and bars: distributing $d$ identical units among $n+1$ slots gives $\binom{d + (n+1) - 1}{(n+1) - 1} = \binom{n+d}{n}$. So $H_S(d) = \binom{n+d}{n}$. Now: is this already a polynomial in $d$? If so, what is its degree?

> [!note]- Hint 3
> $\binom{n+d}{n} = \frac{(d+n)(d+n-1)\cdots(d+1)}{n!}$ is a polynomial in $d$ of degree $n$, valid for *all* $d \geq 0$ — so it equals its own Hilbert polynomial $\mathrm{HP}_S(T) = \binom{T+n}{n}$. The leading coefficient is $1/n!$. For the Poincaré series, recall the binomial series $(1-T)^{-m} = \sum_{d \geq 0} \binom{d+m-1}{m-1} T^d$.

> [!note]- Hint 4
> With $m = n+1$: $\sum_d \binom{n+d}{n} T^d = (1-T)^{-(n+1)}$, so $P(S,T) = (1-T)^{-(n+1)}$, a pole of order $n+1$ at $T=1$. Thus $d(S) = n+1 = \dim S = \deg \mathrm{HP}_S + 1$. Be careful: $\deg \mathrm{HP}_S = n$ is the dimension of *projective* space $\mathbb{P}^n$, while $n+1$ is the Krull dimension of the *ring* (the affine cone).

---

# Solution

The computation has three movements: count the monomials in each degree, recognise the count as a polynomial (the Hilbert polynomial), and sum the generating function (the Poincaré series). Each is mechanical; the interpretation at the end — degree $n$ is $\dim \mathbb{P}^n$, leading coefficient $1/n!$ is $\deg \mathbb{P}^n = 1$ — is the point.

**Step 1: $\dim_k S_d = \binom{n+d}{n}$.**

The degree-$d$ part $S_d$ has $k$-basis the monomials of degree $d$, counted by stars and bars.

> [!note]- Derivation
> $S_d$ is the $k$-vector space of homogeneous polynomials of degree $d$ in $T_0,\dots,T_n$, with $k$-basis the monomials
> $$T_0^{e_0} T_1^{e_1} \cdots T_n^{e_n}, \qquad e_i \geq 0, \quad e_0 + e_1 + \cdots + e_n = d.$$
> Counting these is the **stars and bars** problem: the number of ways to write $d$ as an ordered sum of $n+1$ non-negative integers is the number of ways to place $n$ dividing bars among $d + n$ positions,
> $$\#\{(e_0,\dots,e_n) : e_i \geq 0,\ \textstyle\sum e_i = d\} = \binom{d + n}{n} = \binom{n+d}{n}.$$
> Since $A_0 = k$ is a field, length equals dimension, so the Hilbert function is
> $$H_S(d) = \ell(S_d) = \dim_k S_d = \binom{n+d}{n}.$$

**Step 2: The Hilbert polynomial is $\mathrm{HP}_S(T) = \binom{T+n}{n}$, of degree $n$.**

The count $\binom{n+d}{n}$ is already a degree-$n$ polynomial in $d$, valid for all $d \geq 0$, so it is the Hilbert polynomial.

> [!note]- Derivation
> Expand the binomial coefficient as a polynomial in $d$:
> $$\binom{n+d}{n} = \frac{(d+n)(d+n-1)\cdots(d+1)}{n!}.$$
> The numerator is a product of $n$ linear factors in $d$, so this is a polynomial in $d$ of degree $n$, with leading term $\dfrac{d^n}{n!}$. It agrees with $H_S(d)$ for *every* $d \geq 0$ (not merely large $d$). By the uniqueness of the eventually-equal polynomial in the definition of the [[Def - The Hilbert Function and Hilbert Polynomial|Hilbert polynomial]],
> $$\mathrm{HP}_S(T) = \binom{T+n}{n} = \frac{(T+n)(T+n-1)\cdots(T+1)}{n!},$$
> of degree $n$ with leading coefficient $\dfrac{1}{n!}$. Note $\mathrm{HP}_S \in \mathbb{Q}[T] \setminus \mathbb{Z}[T]$ in general (e.g. for $n = 1$, $\mathrm{HP}_S = T + 1$, integer coefficients; for $n = 2$, $\mathrm{HP}_S = \tfrac12 T^2 + \tfrac32 T + 1$, rational coefficients) yet it is a **numerical polynomial**: $\mathrm{HP}_S(d) \in \mathbb{Z}_{\geq 0}$ for all $d \geq 0$.

**Step 3: The Poincaré series is $P(S,T) = (1-T)^{-(n+1)}$, pole order $n+1$.**

Summing the Hilbert function via the binomial series gives a pole of order $n+1$ at $T = 1$.

> [!note]- Derivation
> Using the negative binomial series $(1-T)^{-m} = \sum_{d \geq 0} \binom{d+m-1}{m-1} T^d$ with $m = n+1$:
> $$P(S, T) = \sum_{d \geq 0} \dim_k S_d \, T^d = \sum_{d \geq 0} \binom{n+d}{n} T^d = \frac{1}{(1-T)^{n+1}}.$$
> Equivalently, $S = k[T_0,\dots,T_n]$ is the tensor product / "product" of $n+1$ copies of the degree-$1$-generated ring $k[T_i]$, each with Poincaré series $\sum_{e \geq 0} T^e = (1-T)^{-1}$, and Poincaré series multiply, giving $(1-T)^{-(n+1)}$. This matches the form predicted by [[Thm - Hilbert-Serre and Rationality of the Poincare Series|Hilbert–Serre]]: a rational function with denominator $\prod_{i=0}^n (1 - T^{k_i}) = (1-T)^{n+1}$ (all $k_i = 1$). The numerator $f(T) = 1$ does not vanish at $T = 1$, so the pole at $T = 1$ has order exactly
> $$d(S) = n + 1.$$

**Step 4: Read off the geometry — dimension $n$, degree $1$.**

The degree of $\mathrm{HP}_S$ is $\dim \mathbb{P}^n = n$; the leading coefficient encodes $\deg \mathbb{P}^n = 1$.

> [!note]- Derivation
> The general dictionary (from [[Def - The Hilbert Function and Hilbert Polynomial|the Hilbert-polynomial definition]]): for a projective variety $X \subseteq \mathbb{P}^N$ with homogeneous coordinate ring $A$,
> $$\deg \mathrm{HP}_X = \dim X, \qquad (\text{leading coefficient of } \mathrm{HP}_X) = \frac{\deg X}{(\dim X)!}.$$
> Here $X = \mathbb{P}^n$ with coordinate ring $S$, so $\deg \mathrm{HP}_S = n$ gives $\dim \mathbb{P}^n = n$ — as it must — and the leading coefficient $1/n!$ gives
> $$\deg \mathbb{P}^n = n! \cdot \frac{1}{n!} = 1.$$
> Consistency check with the ring: $\deg \mathrm{HP}_S = n = d(S) - 1 = (n+1) - 1$, and $d(S) = n+1 = \dim S$ is the Krull dimension of the polynomial ring (the affine cone over $\mathbb{P}^n$, one dimension larger than $\mathbb{P}^n$). $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** For $S = k[T_0,\dots,T_n]$ standard graded: $H_S(d) = \binom{n+d}{n}$, $\mathrm{HP}_S(T) = \binom{T+n}{n}$ (degree $n$, leading coefficient $1/n!$), and $P(S,T) = (1-T)^{-(n+1)}$ (pole order $n+1$).
>
> The monomials $T_0^{e_0}\cdots T_n^{e_n}$ with $\sum e_i = d$ form a $k$-basis of $S_d$; by stars and bars there are $\binom{d+n}{n} = \binom{n+d}{n}$ of them, so $H_S(d) = \dim_k S_d = \binom{n+d}{n}$. This is a degree-$n$ polynomial $\binom{T+n}{n} = (T+n)\cdots(T+1)/n!$ in $d$ for all $d \geq 0$, hence equals $\mathrm{HP}_S$, with leading coefficient $1/n!$. Summing, $P(S,T) = \sum_d \binom{n+d}{n}T^d = (1-T)^{-(n+1)}$ by the binomial series, a pole of order $n+1$ at $T=1$, so $d(S) = n+1 = \dim S$. Finally $\deg \mathrm{HP}_S = n = \dim\mathbb{P}^n$ and $n! \cdot (1/n!) = 1 = \deg \mathbb{P}^n$. $\blacksquare$

---

# Key Takeaways

**The Hilbert polynomial reads off two geometric numbers at once — dimension is its degree, degree is its normalized leading coefficient.** This is the operational meaning of the entire Hilbert-function apparatus, and $\mathbb{P}^n$ is the calibrating example. For *any* projective variety $X \subseteq \mathbb{P}^N$, the single polynomial $\mathrm{HP}_X(d) = \dim_k A_d$ (for large $d$) has $\deg \mathrm{HP}_X = \dim X$ and leading coefficient $\frac{\deg X}{(\dim X)!}$. So from one count — "how many independent forms of degree $d$ are there on $X$, asymptotically?" — you extract both the dimension and the degree of $X$. For $\mathbb{P}^n$ the answer is degree $n$, leading coefficient $1/n!$, hence dimension $n$ and degree $1$ (projective space is the unique variety of its dimension and degree). The lesson for spaced practice: when you meet a graded ring, compute its Hilbert function, recognise it as a polynomial, and immediately decode dimension (the degree) and degree (the leading coefficient $\times$ factorial) — these two numbers are the gateway to **bold plain text — intersection theory**, where degrees multiply under generic intersection (Bézout) and dimensions add to the ambient dimension.

**Mind the off-by-one between the cone and the projective variety: $\dim S = \deg \mathrm{HP}_S + 1$.** The polynomial ring $S = k[T_0,\dots,T_n]$ has *Krull* dimension $n+1$ (it is the coordinate ring of the affine cone $\mathbb{A}^{n+1}$ over $\mathbb{P}^n$), but the *Hilbert polynomial* has degree $n$, the dimension of $\mathbb{P}^n$ itself. The relation $\dim S = d(S) = 1 + \deg \mathrm{HP}_S$ is the algebra of "the affine cone over a projective variety is one dimension larger than the variety," because the cone includes the extra scaling direction collapsed in projectivization. This is exactly why the pole order of the Poincaré series ($n+1$, the cone/ring dimension) differs by one from the degree of the Hilbert polynomial ($n$, the projective dimension). Confusing these two is the most common error in the subject; the discipline is to remember that **the Poincaré series sees the cone, the Hilbert polynomial sees the projective variety.**

**Stars and bars, the binomial series, and Hilbert–Serre are three views of the same identity $\sum_d \binom{n+d}{n}T^d = (1-T)^{-(n+1)}$.** The computation knits together three pieces of machinery into one identity. *Combinatorially*, $\binom{n+d}{n}$ counts degree-$d$ monomials (stars and bars). *Analytically*, the negative binomial series $(1-T)^{-(n+1)} = \sum_d \binom{n+d}{n}T^d$ is the generating function. *Structurally*, [[Thm - Hilbert-Serre and Rationality of the Poincare Series|Hilbert–Serre]] guarantees the rational form with denominator $(1-T)^{n+1}$ because $S$ is generated by $n+1$ degree-one elements, and the pole order equals the number of generators in the cleanest (regular) case. The reusable insight: a standard-graded ring built from $m$ degree-one generators with no relations has Poincaré series $(1-T)^{-m}$ exactly, and relations only *lower* the pole order. This is why a hypersurface $S/(f)$ with $\deg f = e$ has Poincaré series $\frac{1 - T^e}{(1-T)^{n+1}} = \frac{1+T+\cdots+T^{e-1}}{(1-T)^n}$, pole order $n$ — one less — the Hilbert-function shadow of **bold plain text — Krull's principal ideal theorem**: one equation drops dimension by one (see [[Ex - Krull's principal ideal theorem and hypersurfaces]]).

**The Hilbert polynomial is the elementary, length-counting shadow of sheaf cohomology and Riemann–Roch.** Although this exercise computes everything by hand, the result connects to deep geometry: for large $d$, $\mathrm{HP}_X(d) = \chi(X, \mathcal{O}_X(d))$, the **bold plain text — Euler characteristic** of the twisting sheaf, because higher cohomology vanishes for $d \gg 0$ (Serre vanishing). For $\mathbb{P}^n$, $\binom{n+d}{n} = \dim_k H^0(\mathbb{P}^n, \mathcal{O}(d)) = \chi(\mathbb{P}^n, \mathcal{O}(d))$, the dimension of the space of global degree-$d$ forms. So the naive monomial count of Step 1 is secretly computing a cohomological invariant, and the polynomiality of $\mathrm{HP}$ is the elementary face of the **bold plain text — Riemann–Roch theorem**. This is the through-line that makes the Hilbert function worth defining: it is the computable, combinatorial entry point to the analytic theory of line bundles and their global sections, with $\mathbb{P}^n$ as the worked base case from which all of projective geometry is bootstrapped.
