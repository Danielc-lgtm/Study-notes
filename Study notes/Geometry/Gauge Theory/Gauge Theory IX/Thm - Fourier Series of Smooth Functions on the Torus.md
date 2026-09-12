---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order"
  - "Thm - Cauchy-Schwarz Inequality"
tags: [geometry, gauge-theory, analysis]
---

# Notation

Throughout, $n\ge1$ is a fixed integer and $T^n=\mathbb R^n/2\pi\mathbb Z^n$ is the **flat $n$-torus**, the quotient of $\mathbb R^n$ by the lattice $2\pi\mathbb Z^n$, carried with the flat Riemannian metric it inherits from the Euclidean metric on $\mathbb R^n$. A smooth complex-valued function on $T^n$ is the same thing as a smooth function $u\colon\mathbb R^n\to\mathbb C$ that is $2\pi$-periodic in every coordinate, $u(x+2\pi e_j)=u(x)$ for each standard basis vector $e_j$; we write $C^\infty(T^n;\mathbb C)$ for the space of these. Integration over $T^n$ means integration of a periodic function over one period cell, which we take to be $[-\pi,\pi]^n$; thus $\int_{T^n}f\,dx:=\int_{[-\pi,\pi]^n}f(x)\,dx$ and $\operatorname{vol}(T^n)=(2\pi)^n$.

For $\xi=(\xi_1,\dots,\xi_n)\in\mathbb Z^n$ and $x\in\mathbb R^n$ we write $\langle\xi,x\rangle=\sum_{j=1}^n\xi_jx_j$ for the standard pairing, and $|\xi|=\big(\sum_j\xi_j^2\big)^{1/2}$ for the Euclidean norm. The **Fourier coefficient** of $u\in C^\infty(T^n;\mathbb C)$ at frequency $\xi\in\mathbb Z^n$ is
$$
\hat u(\xi):=(2\pi)^{-n}\int_{T^n}u(x)\,e^{-i\langle\xi,x\rangle}\,dx ,
$$
exactly as on the parent page [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order]]. The character $e_\xi(x):=e^{i\langle\xi,x\rangle}$ is a smooth $2\pi$-periodic function of modulus one. The formal series $\sum_{\xi\in\mathbb Z^n}\hat u(\xi)\,e^{i\langle\xi,x\rangle}$ is the **Fourier series** of $u$.

We use standard multi-index notation: for $\alpha=(\alpha_1,\dots,\alpha_n)\in\mathbb Z_{\ge0}^n$ we set $|\alpha|=\sum_j\alpha_j$, $\partial^\alpha=\partial_1^{\alpha_1}\cdots\partial_n^{\alpha_n}$ (where $\partial_j=\partial/\partial x_j$), and $\xi^\alpha=\xi_1^{\alpha_1}\cdots\xi_n^{\alpha_n}$. The uniform norm of a continuous function is $\lVert f\rVert_{C^0}=\sup_{x\in T^n}|f(x)|$, and $\lVert f\rVert_{C^r}=\sum_{|\alpha|\le r}\lVert\partial^\alpha f\rVert_{C^0}$. The $L^2$ norm is $\lVert u\rVert_{L^2}^2=\int_{T^n}|u|^2\,dx$. Following the parent page, for $k\in\mathbb Z$ the Sobolev norm is $\lVert u\rVert_k^2=\sum_{\xi\in\mathbb Z^n}(1+|\xi|^2)^k\,|\hat u(\xi)|^2$; in particular $\lVert u\rVert_0^2=\sum_{\xi}|\hat u(\xi)|^2$.

A sequence $c=(c_\xi)_{\xi\in\mathbb Z^n}$ of complex numbers is **rapidly decreasing** if for every $N\in\mathbb Z_{\ge0}$ there is a constant $C_N<\infty$ with $|c_\xi|\le C_N(1+|\xi|)^{-N}$ for all $\xi\in\mathbb Z^n$; equivalently, $\sup_\xi(1+|\xi|)^N|c_\xi|<\infty$ for every $N$. We write $\mathscr S(\mathbb Z^n)$ for the set of rapidly decreasing sequences, a complex vector space under coordinatewise operations. The **convolution** of two continuous functions $f,w$ on $T^n$ is $(f*w)(x):=(2\pi)^{-n}\int_{T^n}f(y)\,w(x-y)\,dy$.

> [!warning] Convention: period and placement of the factor $2\pi$
> This series works on the $2\pi$-periodic torus $T^n=\mathbb R^n/2\pi\mathbb Z^n$ with $\hat u(\xi)=(2\pi)^{-n}\int u\,e^{-i\langle\xi,x\rangle}\,dx$, so that the reconstruction series carries no prefactor and Parseval carries a single factor $(2\pi)^n$. Many texts (Stein–Shakarchi, *Fourier Analysis*, Ch. 2–3) work one variable at a time on $[-\pi,\pi]$ with the same normalisation; others (Folland, *Real Analysis*, §8.3) use the unit-period torus $\mathbb R^n/\mathbb Z^n$ with characters $e^{2\pi i\langle\xi,x\rangle}$ and coefficients $\int u\,e^{-2\pi i\langle\xi,x\rangle}\,dx$ carrying no prefactor at all. To convert a unit-period statement to ours, rescale $x\mapsto x/2\pi$: the frequency lattice is unchanged, the derivative $\partial_j$ picks up a factor $2\pi$, and the volume changes by $(2\pi)^n$. All four assertions below are convention-independent once the prefactors are tracked; we state them in the series convention throughout.

---

# Statement

> **Theorem (Fourier series of a smooth function on the torus).** Let $u,v\in C^\infty(T^n;\mathbb C)$ and write $\hat u(\xi)=(2\pi)^{-n}\int_{T^n}u\,e^{-i\langle\xi,x\rangle}\,dx$ for $\xi\in\mathbb Z^n$. Then:
>
> **(i) (Differentiation is multiplication; rapid decrease.)** For every $j\in\{1,\dots,n\}$ and every $\xi\in\mathbb Z^n$,
> $$\widehat{\partial_j u}(\xi)=i\,\xi_j\,\hat u(\xi),\qquad\text{and more generally}\qquad \widehat{\partial^\alpha u}(\xi)=(i\xi)^\alpha\,\hat u(\xi)=i^{|\alpha|}\xi^\alpha\,\hat u(\xi)$$
> for every multi-index $\alpha$. Consequently, for every $N\in\mathbb Z_{\ge0}$ there is a constant $C_N<\infty$, depending only on $N$, $n$, and finitely many $C^0$ norms of derivatives of $u$, with $|\hat u(\xi)|\le C_N(1+|\xi|)^{-N}$ for all $\xi\in\mathbb Z^n$; that is, $(\hat u(\xi))_\xi\in\mathscr S(\mathbb Z^n)$.
>
> **(ii) (Uniform reconstruction with all derivatives.)** The Fourier series $\sum_{\xi\in\mathbb Z^n}\hat u(\xi)\,e^{i\langle\xi,x\rangle}$ converges absolutely and uniformly on $T^n$, as does the series $\sum_{\xi}(i\xi)^\alpha\hat u(\xi)\,e^{i\langle\xi,x\rangle}$ obtained by differentiating it term by term with any $\partial^\alpha$; its sum is a smooth function, and that sum is $u$:
> $$u(x)=\sum_{\xi\in\mathbb Z^n}\hat u(\xi)\,e^{i\langle\xi,x\rangle}\qquad\text{for every }x\in T^n,\qquad \partial^\alpha u(x)=\sum_{\xi\in\mathbb Z^n}(i\xi)^\alpha\hat u(\xi)\,e^{i\langle\xi,x\rangle}.$$
>
> **(iii) (Parseval.)** The inner products in physical space and in frequency space agree up to the volume factor:
> $$\int_{T^n}u(x)\,\overline{v(x)}\,dx=(2\pi)^n\sum_{\xi\in\mathbb Z^n}\hat u(\xi)\,\overline{\hat v(\xi)};$$
> in particular $\lVert u\rVert_{L^2}^2=(2\pi)^n\sum_\xi|\hat u(\xi)|^2=(2\pi)^n\lVert u\rVert_0^2$.
>
> **(iv) (The coefficient map is a bijection onto $\mathscr S$.)** The map $\mathcal F\colon C^\infty(T^n;\mathbb C)\to\mathscr S(\mathbb Z^n)$, $\mathcal F(u)=(\hat u(\xi))_\xi$, is a linear bijection. Its inverse sends a rapidly decreasing sequence $(c_\xi)_\xi$ to the smooth function $\sum_\xi c_\xi\,e^{i\langle\xi,x\rangle}$.

---

# Motivation

This page is the analytic bedrock of the entire chapter. Everything that follows — the identification of the Sobolev spaces $H_k(T^n)$ with weighted sequence spaces, the Sobolev embedding and Rellich compactness theorems, the elliptic estimate for constant-coefficient operators, the Friedrichs mollifier, and through the charts theorem every "on a compact manifold" statement of §9.2–§9.6 — is, at bottom, a statement about how fast the Fourier coefficients of a function decay. Before any of those can be stated cleanly we need the one theorem that turns analysis on the torus into arithmetic on the lattice $\mathbb Z^n$: the dictionary between a smooth function and its sequence of Fourier coefficients.

The question the theorem answers is the most basic one imaginable. A smooth periodic function $u$ produces a sequence of numbers $\hat u(\xi)$. Two things could go wrong with treating that sequence as a faithful copy of $u$. First, the sequence might lose information — different functions might have the same coefficients, so that reading off $\hat u$ would be like reading a blurred photograph. Second, even if no information is lost, we might not be able to rebuild $u$ from $\hat u$ in any usable way — the series $\sum_\xi\hat u(\xi)e_\xi$ might diverge, or converge only in some weak averaged sense that does not let us evaluate $u$ at a point or differentiate it. The theorem says that for *smooth* $u$ neither failure occurs: the coefficients decay faster than any power of $|\xi|$, the series converges uniformly together with all of its termwise derivatives, and its sum is exactly $u$. Smoothness of the function is precisely coded as rapid decay of the coefficients, and the code is a perfect two-way dictionary — part (iv) makes this literal by exhibiting $\mathcal F$ as a bijection onto the rapidly decreasing sequences.

The mechanism behind all of this is a single identity, part (i): under $\mathcal F$, the differential operator $\partial_j$ becomes multiplication by $i\xi_j$. Differentiation, the most analytic of operations, becomes an algebraic operation on the coefficient side — a multiplication by a polynomial in $\xi$. This is why "$u$ has $N$ bounded derivatives" translates into "$\hat u(\xi)$ decays like $|\xi|^{-N}$", and why the whole Sobolev theory of the chapter, which measures functions by counting derivatives in $L^2$, becomes on the torus the theory of weighted $\ell^2$ spaces with the weight $(1+|\xi|^2)^k$. Every difficulty about differential operators is, after Fourier transform, a difficulty about multiplication operators, and multiplication operators are transparent.

The one place where genuine work is required is the claim that the dictionary loses nothing — that a continuous function whose coefficients all vanish is identically zero. This is the injectivity of the Fourier transform, and it cannot be evaded by any formal manipulation, because summing the Fourier series naively runs into the fact that the partial sums (the Dirichlet kernel) do not converge nicely. The resolution, due to Fejér, is to average the partial sums: the Cesàro means converge, and their kernel — the Fejér kernel — is a genuine approximate identity, non-negative and concentrating its mass at the origin. That averaging is the technical heart of the proof, isolated below as Lemmas 2–4.

The one-dimensional shadow of the entire chapter appears already in Haydys's *Introduction to Gauge Theory*, Remark 138: for $u\in C^\infty(S^1;\mathbb R)$ with mean $\bar u$ and mean-zero part $u_0=u-\bar u$, the mean value theorem furnishes a point $\theta_0$ with $u_0(\theta_0)=0$, and then $|u_0(\theta)|=\big|\int_{\theta_0}^\theta u_0'\big|\le\big(\int|u_0'|^2\big)^{1/2}\big(\int 1\big)^{1/2}\le\sqrt{2\pi}\,\lVert u\rVert_{W^{1,2}}$ by the Cauchy–Schwarz inequality, whence $W^{1,2}(S^1)\subset C^0(S^1)$. That estimate is the germ of the Sobolev embedding theorem, and the present page provides the Fourier-analytic foundation on $T^n$ from which the embedding, in every dimension and to every order, will be read off in [[Thm - Sobolev Embedding Theorem]] as a decay-and-summation statement about $\hat u$.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is that $u$ is smooth on the torus. The skill is recognising when a problem secretly hands you a function on the torus, or hands you the coefficient data instead of the function.

The first disguised source is **a smooth function on $\mathbb R^n$ that is periodic under some lattice $\Lambda$**, whether or not the periodicity is advertised. Any $\Lambda$-periodic smooth function is a function on the torus $\mathbb R^n/\Lambda$, and a linear change of coordinates carrying $\Lambda$ to $2\pi\mathbb Z^n$ brings the theorem to bear. The non-obvious bridge is that the lattice need not be rectangular: a function periodic under an oblique lattice (as arise for a flat metric that is not the product metric, or for a complex torus $\mathbb C/(\mathbb Z+\tau\mathbb Z)$) is still governed by this theorem after the coordinate change, with the frequency lattice replaced by the dual lattice $\Lambda^*$. *Example problem:* show that a doubly periodic entire-like smooth function on $\mathbb C$ with a prescribed lattice of periods is determined by, and reconstructible from, its coefficients indexed by the dual lattice.

The second disguised source is **a differential equation with constant coefficients on the torus**, or on any domain where the solution is known to be periodic. If $Pu=f$ with $P=\sum_{|\alpha|\le\ell}a_\alpha\partial^\alpha$ having constant coefficients, then part (i) turns the equation into $\big(\sum_\alpha a_\alpha(i\xi)^\alpha\big)\hat u(\xi)=\hat f(\xi)$, an algebraic equation solved coefficientwise. The bridge is that the smoothness of $u$ needed to apply part (i) is often *not* assumed but *proved* afterward: one solves for $\hat u(\xi)=\hat f(\xi)/p(i\xi)$, checks rapid decrease of the quotient, and invokes part (iv) to conclude that a smooth solution exists. This is exactly the constant-coefficient elliptic estimate of [[Thm - Elliptic Estimate for Constant-Coefficient Operators on the Torus]]. *Example problem:* solve $(-\Delta+1)u=f$ on $T^n$ for smooth $f$ and show the solution is smooth, by exhibiting $\hat u(\xi)=\hat f(\xi)/(|\xi|^2+1)$ and checking rapid decrease.

The third disguised source is **a sequence presented as data, with no function in sight**. Any rapidly decreasing sequence $(c_\xi)$ — for instance the spectral data of a diagonalised operator, or a prescribed multiplier — is, by part (iv), the coefficient sequence of a unique smooth function, and questions about the sequence become questions about that function and vice versa. The non-obvious step is to *pass to the function*: convolution of sequences corresponds to multiplication of functions, multiplication by the weight $(1+|\xi|^2)^{k}$ corresponds to the action of $(1-\Delta)^k$, and a sequence-theoretic estimate becomes a Sobolev estimate. *Example problem:* given a rapidly decreasing multiplier $(m_\xi)$, show that the operator $u\mapsto\sum_\xi m_\xi\hat u(\xi)e_\xi$ is smoothing, by realising $(m_\xi)$ as $\hat g$ for a smooth $g$ and identifying the operator with convolution by $g$.

**Targets (Output Amplification).** The theorem's four parts are ingredients that combine with almost everything downstream.

Combine part (i) with **the definition of the Sobolev norm** $\lVert u\rVert_k^2=\sum_\xi(1+|\xi|^2)^k|\hat u(\xi)|^2$ and the elementary comparison $\sum_{|\alpha|\le k}|\xi^\alpha|^2\asymp(1+|\xi|^2)^k$: the result is the identification $W^{k,2}(T^n)=H_k(T^n)$ with equivalent norms, the content of [[Thm - Sobolev Norms on the Torus via Fourier Coefficients]]. The extra ingredient is only bookkeeping with monomials; the payoff is that the entire Sobolev scale on the torus becomes a family of weighted $\ell^2$ spaces.

Combine parts (i)–(ii) with **the convergence of a lattice sum** $\sum_\xi(1+|\xi|)^{-s}<\infty$ for $s>n$ (Lemma 1 below): the result is that $H_k(T^n)\hookrightarrow C^r(T^n)$ whenever $k-\tfrac n2>r$, the Sobolev embedding theorem, because $\sum_\xi|\xi^\alpha||\hat u(\xi)|$ can be split by the Cauchy–Schwarz inequality into a convergent weight sum times $\lVert u\rVert_k$. The extra ingredient is the dimension count in the lattice sum; the payoff is uniform control of $r$ derivatives from $k$ derivatives in $L^2$.

Combine part (iii) with **the completeness of $\ell^2$**: the result is that the completion $H_0(T^n)$ is isometrically (up to the factor $(2\pi)^{n/2}$) the space $\ell^2(\mathbb Z^n)$, so that $L^2(T^n)$ has $\{(2\pi)^{-n/2}e_\xi\}_{\xi}$ as an orthonormal basis. The extra ingredient is the Riesz–Fischer completeness of $\ell^2$; the payoff is a concrete orthonormal basis diagonalising every constant-coefficient operator, which is the starting point for the spectral analysis used throughout §9.3–§9.6.

As the manifest records, the targets of this page are, quite literally, *every page of the chapter*: no later result on the torus, and hence — through [[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts]] — no later result on a compact manifold, is proved without it.

---

# Why Is It True

Picture the character $e_\xi(x)=e^{i\langle\xi,x\rangle}$ as a pure oscillation of frequency $\xi$. Applying $\partial_j$ multiplies it by $i\xi_j$; this is the whole of part (i), read on a single character, and it extends to $u$ because the Fourier coefficient is an integral against $e_{-\xi}$ and integration by parts moves the derivative onto the character with no boundary term to pay — the torus is closed, so periodicity swallows the boundary. Once differentiation is multiplication by $i\xi$, a function that can be differentiated $N$ times with bounded result must have coefficients that survive multiplication by $|\xi|^N$ and stay bounded, which forces $|\hat u(\xi)|\lesssim|\xi|^{-N}$: **smoothness of the function is decay of the coefficients, and each derivative buys one power of decay.**

Rapid decay is exactly what a series needs to converge robustly. If the coefficients die faster than any power of $|\xi|$, then the majorant $\sum_\xi|\hat u(\xi)|(1+|\xi|)^{|\alpha|}$ is summable for every $\alpha$, because the leftover weight $(1+|\xi|)^{|\alpha|-N}$ is summable over the lattice once $N$ exceeds $|\alpha|+n$. The Weierstrass comparison test then makes the Fourier series, and every one of its termwise-differentiated cousins, converge uniformly, and a uniformly convergent series of smooth functions whose derivatives also converge uniformly is itself smooth with the expected derivatives. So the sum $S=\sum_\xi\hat u(\xi)e_\xi$ is a bona fide smooth function; the only question left is whether $S=u$.

That last question is the one place where oscillation could hide something. It is settled by observing that $S$ and $u$ have the *same* Fourier coefficients — termwise integration of the uniformly convergent series for $S$ against $e_{-\xi}$ recovers $\hat u(\xi)$ by the orthogonality of characters — and then invoking the fact that a continuous function on the torus is determined by its coefficients. The reason nothing is lost is Fejér's: although the sharp partial sums of the Fourier series (the Dirichlet kernel) oscillate too wildly to converge for a merely continuous function, their *averages* converge, because the averaged kernel $K_N$ is non-negative and piles all of its unit mass into a shrinking neighbourhood of the origin. Convolving a continuous function with such a kernel reproduces the function in the limit — this is what "approximate identity" means — while the convolution is visibly a trigonometric polynomial built from the coefficients. If all coefficients vanish, every such average is zero, so the function, being their uniform limit, is zero. **The Fejér average is the device that lets us reconstruct a continuous function from its coefficients even though the naive partial sums fail, and it is why the coefficient dictionary is faithful.**

Parseval and the bijection are then bookkeeping on top of reconstruction: integrate the uniformly convergent expansion of $u$ against $\bar v$ and use orthogonality to get part (iii), and run the convergence argument backward — a rapidly decreasing sequence yields, by the same M-test, a smooth function whose coefficients are the given sequence — to get part (iv).

---

# What Makes This Hard

The genuinely non-trivial step is the uniqueness lemma: a continuous function on $T^n$ with all Fourier coefficients zero must vanish. Everything else in the theorem is either integration by parts (part i) or an application of the Weierstrass M-test once decay is known (parts ii and iv); a beginner who tries to prove uniqueness by simply summing the Fourier series discovers that the partial sums — convolution with the Dirichlet kernel, which changes sign and has $L^1$ norm growing like $\log N$ — need not converge for a merely continuous function, so no direct summation argument closes the gap. The correct move, easy to miss, is to average the partial sums and work with the Fejér kernel, whose non-negativity and mass concentration make it an approximate identity where the Dirichlet kernel is not.

The second place to slip is justifying the two interchanges of sum and integral (in identifying $\hat S=\hat u$, and in deriving Parseval): both are legitimate only because the relevant series converges *uniformly* on the finite-measure space $T^n$, and the proof must say so rather than manipulate infinite sums formally. A related trap in the multidimensional case is to assert that $K_N(x)=\prod_jF_N(x_j)$ tends to zero pointwise off the origin; it does not, because if one coordinate stays near zero the corresponding factor stays large. What is true, and what the approximate-identity argument actually uses, is that the *mass* of $K_N$ off any neighbourhood of the origin tends to zero, and the honest proof estimates $\int_{|y|\ge\delta}K_N$ rather than $\sup_{|y|\ge\delta}K_N$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Establish the differentiation identity by integration by parts and read off rapid decay. Use rapid decay plus a convergent lattice sum to run the Weierstrass M-test, producing a smooth sum $S$ of the Fourier series; identify $\hat S=\hat u$ by termwise integration and conclude $S=u$ from a uniqueness lemma proved with the Fejér kernel. Parseval and the bijection then follow by the same interchange and the same M-test run backward.

**Subgoal decomposition:**

1. **Differentiation is multiplication by $i\xi$.** Prove $\widehat{\partial_ju}(\xi)=i\xi_j\hat u(\xi)$, iterate to $\widehat{\partial^\alpha u}=(i\xi)^\alpha\hat u$, and deduce $|\hat u(\xi)|\le C_N(1+|\xi|)^{-N}$.
   - *Hint:* Integrate by parts in $x_j$ over one period; the boundary term cancels by $2\pi$-periodicity. Bound $|\xi^\alpha||\hat u(\xi)|\le\lVert\partial^\alpha u\rVert_{C^0}$ and compare $(1+|\xi|)^N$ with $\sum_{|\alpha|\le N}|\xi^\alpha|$.
   - *Why needed:* Rapid decay is the fuel for every convergence argument below.

2. **A lattice sum converges.** Show $\sum_{\xi\in\mathbb Z^n}(1+|\xi|)^{-s}<\infty$ for $s>n$.
   - *Hint:* Count lattice points in the spherical shell $\{m\le|\xi|<m+1\}$ by comparing disjoint unit cubes with an annulus; the count is $\lesssim(1+m)^{n-1}$.
   - *Why needed:* It is the summable majorant that powers the M-test in subgoals 3 and 6.

3. **The series and its derivatives converge uniformly to a smooth $S$.** Show $\sum_\xi(i\xi)^\alpha\hat u(\xi)e_\xi$ converges absolutely and uniformly for every $\alpha$, and that the sum $S$ is smooth with $\partial^\alpha S$ equal to that series.
   - *Hint:* Majorise by $C_N\sum_\xi(1+|\xi|)^{|\alpha|-N}$ with $N=|\alpha|+n+1$ and apply the M-test; upgrade to smoothness by the differentiation-of-uniformly-convergent-series lemma.
   - *Why needed:* It produces an honest smooth candidate $S$ for the sum of the Fourier series.

4. **The Fejér kernel is an approximate identity.** Show $K_N(x)=\prod_jF_N(x_j)\ge0$, has total mass one, concentrates near the origin, and hence $K_N*w\to w$ uniformly for continuous $w$.
   - *Hint:* Use the closed form $F_N(t)=\frac1{N+1}\big(\frac{\sin((N+1)t/2)}{\sin(t/2)}\big)^2$ and the bound $\int_{|y|\ge\delta}K_N\to0$; split $K_N*w-w$ into a near part and a far part.
   - *Why needed:* It is the reconstruction device that makes the coefficient dictionary faithful.

5. **Uniqueness.** Show that a continuous $w$ on $T^n$ with $\hat w\equiv0$ is $w\equiv0$.
   - *Hint:* $K_N*w$ is a trigonometric polynomial whose coefficients are multiples of $\hat w(\xi)$, hence identically zero; but $K_N*w\to w$ uniformly.
   - *Why needed:* It closes the identification $S=u$ and gives injectivity in part (iv).

6. **Assemble (ii)–(iv).** Identify $\hat S=\hat u$ by termwise integration, conclude $S=u$; integrate $u$'s expansion against $\bar v$ for Parseval; run subgoal 3 backward for surjectivity.
   - *Hint:* Every interchange of $\sum$ and $\int$ is licensed by uniform convergence; orthogonality of characters kills all but one term.
   - *Why needed:* These are the four stated conclusions.

---

# Lemma Decomposition

> [!note]- Lemma 1: A lattice power sum converges precisely beyond the dimension
> **Statement:** For real $s$, the sum $\sum_{\xi\in\mathbb Z^n}(1+|\xi|)^{-s}$ is finite if $s>n$. Moreover there is a constant $A_{n}<\infty$ with $\#\{\xi\in\mathbb Z^n:m\le|\xi|<m+1\}\le A_n(1+m)^{n-1}$ for every integer $m\ge0$.
>
> **Hint:** Attach to each lattice point a unit cube; disjoint cubes centred in a shell fit inside a slightly fattened annulus, so their number is bounded by the annulus volume.
>
> **Why needed:** It is the summable majorant behind the Weierstrass M-test in Lemma 6 and in the Formal Proof, and it is the dimension count that later yields the Sobolev embedding theorem.
>
> > [!note]- Full proof
> > **Set-up of the shell count.** Fix an integer $m\ge0$ and let $S_m=\{\xi\in\mathbb Z^n:m\le|\xi|<m+1\}$. To each $\xi\in\mathbb Z^n$ associate the half-open unit cube $Q_\xi=\xi+[-\tfrac12,\tfrac12)^n$. Distinct lattice points give disjoint cubes (they tile $\mathbb R^n$), and each cube has Lebesgue volume $1$. For $x\in Q_\xi$ we have $|x-\xi|\le\tfrac12\sqrt n$ (the longest vector in $[-\tfrac12,\tfrac12)^n$ has length $\tfrac12\sqrt n$), so by the triangle inequality every $x\in Q_\xi$ with $\xi\in S_m$ satisfies
> > $$m-\tfrac12\sqrt n\le|\xi|-\tfrac12\sqrt n\le|x|\le|\xi|+\tfrac12\sqrt n<m+1+\tfrac12\sqrt n\qquad\text{(triangle inequality, }|x-\xi|\le\tfrac12\sqrt n\text{).}$$
> > Hence the disjoint union $\bigsqcup_{\xi\in S_m}Q_\xi$ is contained in the annulus $A_m=\{x\in\mathbb R^n:(m-\tfrac12\sqrt n)_+\le|x|<m+1+\tfrac12\sqrt n\}$, where $(\cdot)_+$ denotes the non-negative part.
> >
> > **Counting by volume.** Since the cubes are disjoint and each has volume $1$,
> > $$\#S_m=\operatorname{vol}\Big(\bigsqcup_{\xi\in S_m}Q_\xi\Big)\le\operatorname{vol}(A_m)\qquad\text{(disjoint unit cubes inside }A_m\text{).}$$
> > Writing $\omega_n$ for the volume of the Euclidean unit ball, $\operatorname{vol}(A_m)=\omega_n\big[(m+1+\tfrac12\sqrt n)^n-(m-\tfrac12\sqrt n)_+^n\big]$. Put $b=m+1+\tfrac12\sqrt n$ and $a=(m-\tfrac12\sqrt n)_+$, so $0\le b-a\le 1+\sqrt n$. By the mean value theorem applied to $t\mapsto t^n$ on $[a,b]$, there is $c\in[a,b]$ with $b^n-a^n=nc^{n-1}(b-a)\le n\,b^{n-1}(b-a)\le n(1+\sqrt n)\,b^{n-1}$ (since $c\le b$ and $b-a\le1+\sqrt n$). As $b=m+1+\tfrac12\sqrt n\le(1+\sqrt n)(1+m)$, we obtain $b^{n-1}\le(1+\sqrt n)^{n-1}(1+m)^{n-1}$, and therefore
> > $$\#S_m\le\omega_n\,n(1+\sqrt n)^{n}(1+m)^{n-1}=:A_n(1+m)^{n-1}\qquad\text{(mean value theorem; }b\le(1+\sqrt n)(1+m)\text{),}$$
> > which is the claimed shell bound, valid for every $m\ge0$.
> >
> > **Summation.** Every $\xi\in\mathbb Z^n$ lies in exactly one shell $S_m$ with $m=\lfloor|\xi|\rfloor$, and there $1+|\xi|\ge1+m$, so $(1+|\xi|)^{-s}\le(1+m)^{-s}$ for $s\ge0$. Grouping the sum by shells and using the shell bound,
> > $$\sum_{\xi\in\mathbb Z^n}(1+|\xi|)^{-s}=\sum_{m=0}^\infty\sum_{\xi\in S_m}(1+|\xi|)^{-s}\le\sum_{m=0}^\infty\#S_m\,(1+m)^{-s}\le A_n\sum_{m=0}^\infty(1+m)^{n-1-s}\qquad\text{(shell bound; monotone weight).}$$
> > The final series is $A_n\sum_{m=0}^\infty(1+m)^{-(s-n+1)}$, a $p$-series with exponent $p=s-n+1$, which converges if and only if $p>1$, that is $s>n$. Therefore $\sum_\xi(1+|\xi|)^{-s}<\infty$ whenever $s>n$. $\blacksquare$

> [!note]- Lemma 2: The one-variable Fejér kernel is non-negative with unit mass and vanishing tails
> **Statement:** For $N\ge0$ define $F_N(t)=\sum_{j=-N}^{N}\big(1-\tfrac{|j|}{N+1}\big)e^{ijt}$ for $t\in\mathbb R$. Then $F_N$ is real, $2\pi$-periodic, and
> $$F_N(t)=\frac1{N+1}\left(\frac{\sin\!\big((N+1)t/2\big)}{\sin(t/2)}\right)^2\ge0,\qquad \frac1{2\pi}\int_{-\pi}^{\pi}F_N(t)\,dt=1,$$
> and for every $\delta\in(0,\pi]$, $\displaystyle\sup_{\delta\le|t|\le\pi}F_N(t)\le\frac1{(N+1)\sin^2(\delta/2)}$.
>
> **Hint:** $F_N$ is the average of the Dirichlet kernels $D_m(t)=\sum_{|j|\le m}e^{ijt}=\frac{\sin((m+\frac12)t)}{\sin(t/2)}$; telescope $\sum_{m=0}^ND_m$ using $2\sin(t/2)\sin((m+\tfrac12)t)=\cos(mt)-\cos((m+1)t)$.
>
> **Why needed:** These three properties — sign, mass, tail — are exactly the hypotheses that make $K_N$ an approximate identity in Lemma 3.
>
> > [!note]- Full proof
> > **The Dirichlet kernel in closed form.** For an integer $m\ge0$ set $D_m(t)=\sum_{j=-m}^{m}e^{ijt}$. For $t\notin2\pi\mathbb Z$ this is a geometric sum: multiplying $D_m(t)$ by $e^{it/2}-e^{-it/2}=2i\sin(t/2)$ telescopes the terms, giving $2i\sin(t/2)D_m(t)=e^{i(m+\frac12)t}-e^{-i(m+\frac12)t}=2i\sin\!\big((m+\tfrac12)t\big)$, hence
> > $$D_m(t)=\frac{\sin\!\big((m+\tfrac12)t\big)}{\sin(t/2)}\qquad(t\notin2\pi\mathbb Z),\qquad D_m(t)=2m+1\ \ (t\in2\pi\mathbb Z)\qquad\text{(geometric sum).}$$
> >
> > **Averaging: the Cesàro means.** By definition $F_N=\frac1{N+1}\sum_{m=0}^ND_m$. Interchanging the two finite sums and collecting the coefficient of $e^{ijt}$, the character $e^{ijt}$ with $|j|\le N$ occurs in $D_m$ exactly for $m\ge|j|$, that is for $N-|j|+1$ values of $m$, so its coefficient in $F_N$ is $\frac{N-|j|+1}{N+1}=1-\frac{|j|}{N+1}$; characters with $|j|>N$ do not occur. This is the stated defining sum, and it shows $F_N$ is a real trigonometric polynomial (the coefficients are real and symmetric in $j$).
> >
> > **Closed form and non-negativity.** Sum the closed forms of the $D_m$ using the product-to-sum identity $2\sin(t/2)\sin\!\big((m+\tfrac12)t\big)=\cos(mt)-\cos\big((m+1)t\big)$: for $t\notin2\pi\mathbb Z$,
> > $$2\sin(t/2)\sum_{m=0}^{N}\sin\!\big((m+\tfrac12)t\big)=\sum_{m=0}^N\big[\cos(mt)-\cos((m+1)t)\big]=1-\cos\big((N+1)t\big)=2\sin^2\!\big((N+1)t/2\big)$$
> > by telescoping and the identity $1-\cos\theta=2\sin^2(\theta/2)$. Dividing by $2\sin(t/2)$ gives $\sum_{m=0}^N\sin((m+\tfrac12)t)=\dfrac{\sin^2((N+1)t/2)}{\sin(t/2)}$, and therefore
> > $$F_N(t)=\frac1{N+1}\sum_{m=0}^ND_m(t)=\frac1{N+1}\cdot\frac1{\sin(t/2)}\sum_{m=0}^N\sin\!\big((m+\tfrac12)t\big)=\frac1{N+1}\left(\frac{\sin((N+1)t/2)}{\sin(t/2)}\right)^2$$
> > for $t\notin2\pi\mathbb Z$; both sides extend continuously to $t\in2\pi\mathbb Z$ with value $N+1$, so the identity holds for all $t$. The right-hand side is a non-negative constant times a square, so $F_N\ge0$.
> >
> > **Unit mass.** Integrating the defining sum term by term over $[-\pi,\pi]$ and using $\frac1{2\pi}\int_{-\pi}^\pi e^{ijt}\,dt=\delta_{j,0}$ (which holds because for $j\ne0$, $\int_{-\pi}^\pi e^{ijt}\,dt=\big[\tfrac{e^{ijt}}{ij}\big]_{-\pi}^\pi=\tfrac{e^{ij\pi}-e^{-ij\pi}}{ij}=\tfrac{2i\sin(j\pi)}{ij}=0$), only the $j=0$ term with coefficient $1-\tfrac0{N+1}=1$ survives:
> > $$\frac1{2\pi}\int_{-\pi}^\pi F_N(t)\,dt=\sum_{j=-N}^N\Big(1-\tfrac{|j|}{N+1}\Big)\,\frac1{2\pi}\int_{-\pi}^\pi e^{ijt}\,dt=1\qquad\text{(orthogonality of characters).}$$
> > (The interchange of the finite sum and the integral is trivial, the sum being finite.)
> >
> > **Tail bound.** Fix $\delta\in(0,\pi]$ and let $\delta\le|t|\le\pi$. Then $|t|/2\in[\delta/2,\pi/2]$, and since $\sin$ is increasing on $[0,\pi/2]$ we have $\sin(|t|/2)\ge\sin(\delta/2)>0$, hence $\sin^2(t/2)\ge\sin^2(\delta/2)$. Using $\sin^2((N+1)t/2)\le1$ in the closed form,
> > $$F_N(t)=\frac1{N+1}\cdot\frac{\sin^2((N+1)t/2)}{\sin^2(t/2)}\le\frac1{N+1}\cdot\frac1{\sin^2(\delta/2)}\qquad(\delta\le|t|\le\pi),$$
> > which is the stated bound and tends to $0$ as $N\to\infty$ for each fixed $\delta$. $\blacksquare$

> [!note]- Lemma 3: The product Fejér kernel is an approximate identity on the torus
> **Statement:** Define $K_N(x)=\prod_{j=1}^n F_N(x_j)$ for $x\in T^n$. Then $K_N\ge0$, $(2\pi)^{-n}\int_{T^n}K_N(y)\,dy=1$, and for every $\delta>0$, $\int_{\{y\in T^n:\,|y|\ge\delta\}}K_N(y)\,dy\to0$ as $N\to\infty$. Consequently, for every continuous $w\colon T^n\to\mathbb C$ the convolutions $K_N*w$ converge to $w$ uniformly on $T^n$.
>
> **Hint:** Non-negativity and mass are the one-variable facts multiplied; for the tails, note $|y|\ge\delta$ forces some $|y_j|\ge\delta/\sqrt n$ and integrate that one factor using Lemma 2. For the convergence split $K_N*w-w$ into $|y|<\delta$ and $|y|\ge\delta$.
>
> **Why needed:** It is the reconstruction engine: it turns "same coefficients" into "same function" in Lemma 4.
>
> > [!note]- Full proof
> > **Non-negativity and mass.** Each factor $F_N(x_j)\ge0$ by Lemma 2, so $K_N=\prod_jF_N(x_j)\ge0$. By Fubini's theorem on the product period cell $[-\pi,\pi]^n$ (the integrand is continuous, hence integrable) and the one-variable unit-mass identity of Lemma 2,
> > $$(2\pi)^{-n}\int_{T^n}K_N(y)\,dy=\prod_{j=1}^n\Big((2\pi)^{-1}\int_{-\pi}^\pi F_N(y_j)\,dy_j\Big)=\prod_{j=1}^n 1=1\qquad\text{(Fubini; Lemma 2, unit mass).}$$
> >
> > **Tail estimate.** Fix $\delta>0$. If $|y|\ge\delta$ then $\max_j|y_j|\ge\delta/\sqrt n$ (since $|y|\le\sqrt n\max_j|y_j|$), so at least one coordinate satisfies $|y_j|\ge\delta/\sqrt n$; writing $\delta'=\delta/\sqrt n$, the region $\{|y|\ge\delta\}$ is contained in $\bigcup_{j=1}^n\{|y_j|\ge\delta'\}$. Hence, using $K_N\ge0$ and the union bound,
> > $$\int_{\{|y|\ge\delta\}}K_N\,dy\le\sum_{j=1}^n\int_{\{|y_j|\ge\delta'\}}K_N(y)\,dy\qquad\text{(subadditivity over a cover; }K_N\ge0\text{).}$$
> > For a fixed $j$, factor the integral by Fubini: the $y_j$-integral runs over $\{\delta'\le|y_j|\le\pi\}$ and the remaining coordinates give factors $\int_{-\pi}^\pi F_N=2\pi$ each, so
> > $$\int_{\{|y_j|\ge\delta'\}}K_N(y)\,dy=\Big(\int_{\delta'\le|t|\le\pi}F_N(t)\,dt\Big)(2\pi)^{n-1}\le(2\pi)\sup_{\delta'\le|t|\le\pi}F_N(t)\,(2\pi)^{n-1}\le\frac{(2\pi)^n}{(N+1)\sin^2(\delta'/2)}$$
> > by Lemma 2's tail bound and $\int_{\delta'\le|t|\le\pi}F_N\le2\pi\sup_{\delta'\le|t|\le\pi}F_N$. Summing over $j$,
> > $$\int_{\{|y|\ge\delta\}}K_N\,dy\le\frac{n(2\pi)^n}{(N+1)\sin^2(\delta'/2)}\xrightarrow[N\to\infty]{}0\qquad(\delta'=\delta/\sqrt n\text{ fixed}).$$
> >
> > **Uniform convergence of $K_N*w$.** Let $w$ be continuous on $T^n$, hence bounded, $\lVert w\rVert_{C^0}=:M<\infty$, and uniformly continuous ($T^n$ is compact). Because $(2\pi)^{-n}\int K_N=1$ we may write, for every $x$,
> > $$(K_N*w)(x)-w(x)=(2\pi)^{-n}\int_{T^n}K_N(y)\big[w(x-y)-w(x)\big]\,dy\qquad\text{(unit mass: }w(x)=(2\pi)^{-n}\!\int K_N(y)w(x)\,dy\text{).}$$
> > Fix $\varepsilon>0$. By uniform continuity choose $\delta>0$ so that $|w(x-y)-w(x)|<\varepsilon$ whenever $|y|<\delta$, for all $x$. Split the integral at $|y|=\delta$. On the near region, using $K_N\ge0$ and unit mass,
> > $$(2\pi)^{-n}\int_{|y|<\delta}K_N(y)\,|w(x-y)-w(x)|\,dy\le\varepsilon\,(2\pi)^{-n}\int_{T^n}K_N=\varepsilon\qquad\text{(uniform continuity; }K_N\ge0\text{).}$$
> > On the far region, bounding $|w(x-y)-w(x)|\le2M$ and using the tail estimate,
> > $$(2\pi)^{-n}\int_{|y|\ge\delta}K_N(y)\,|w(x-y)-w(x)|\,dy\le 2M\,(2\pi)^{-n}\int_{|y|\ge\delta}K_N\le\frac{2Mn}{(N+1)\sin^2(\delta/(2\sqrt n))}.$$
> > The right-hand side is independent of $x$ and tends to $0$; choose $N_0$ so that it is below $\varepsilon$ for $N\ge N_0$. Then $\sup_x|(K_N*w)(x)-w(x)|\le2\varepsilon$ for $N\ge N_0$. As $\varepsilon>0$ was arbitrary, $K_N*w\to w$ uniformly. $\blacksquare$

> [!note]- Lemma 4: A continuous function with vanishing Fourier coefficients is zero
> **Statement:** If $w\colon T^n\to\mathbb C$ is continuous and $\hat w(\xi)=0$ for every $\xi\in\mathbb Z^n$, then $w\equiv0$.
>
> **Hint:** Compute $K_N*w$: it is a finite trigonometric polynomial whose coefficient at $\xi$ is a scalar multiple of $\hat w(\xi)$, hence zero; but $K_N*w\to w$ uniformly.
>
> **Why needed:** It is the injectivity of the coefficient dictionary, used to conclude $S=u$ in part (ii) and to prove part (iv).
>
> > [!note]- Full proof
> > **The convolution is a trigonometric polynomial in the coefficients.** Write $K_N(y)=\sum_{\xi}c^{(N)}_\xi\,e^{i\langle\xi,y\rangle}$, where, by the product structure and Lemma 2, $c^{(N)}_\xi=\prod_{j=1}^n\big(1-\tfrac{|\xi_j|}{N+1}\big)$ for $\xi$ with $\max_j|\xi_j|\le N$ and $c^{(N)}_\xi=0$ otherwise; this is a finite sum. Then for each $x\in T^n$,
> > $$(K_N*w)(x)=(2\pi)^{-n}\int_{T^n}K_N(y)\,w(x-y)\,dy=\sum_\xi c^{(N)}_\xi\,(2\pi)^{-n}\int_{T^n}e^{i\langle\xi,y\rangle}\,w(x-y)\,dy\qquad\text{(finite sum, linearity).}$$
> > Substituting $z=x-y$ (a measure-preserving translation on $T^n$, so the domain remains one period cell) gives $\int_{T^n}e^{i\langle\xi,y\rangle}w(x-y)\,dy=\int_{T^n}e^{i\langle\xi,x-z\rangle}w(z)\,dz=e^{i\langle\xi,x\rangle}\int_{T^n}e^{-i\langle\xi,z\rangle}w(z)\,dz=(2\pi)^n\,e^{i\langle\xi,x\rangle}\,\hat w(\xi)$, by the definition of $\hat w(\xi)$. Therefore
> > $$(K_N*w)(x)=\sum_\xi c^{(N)}_\xi\,\hat w(\xi)\,e^{i\langle\xi,x\rangle}\qquad\text{(change of variables }z=x-y\text{; definition of }\hat w\text{).}$$
> >
> > **Conclusion.** By hypothesis $\hat w(\xi)=0$ for all $\xi$, so every coefficient $c^{(N)}_\xi\hat w(\xi)$ vanishes and $K_N*w\equiv0$ for every $N$. On the other hand $w$ is continuous, so by Lemma 3 the sequence $K_N*w$ converges to $w$ uniformly. A sequence that is identically zero converges uniformly to $0$, and uniform limits are unique, so $w\equiv0$. $\blacksquare$

> [!note]- Lemma 5: Differentiation of a uniformly convergent series of smooth functions
> **Statement:** Let $(g_N)_{N\ge0}$ be smooth functions on $T^n$ such that $g_N\to S$ pointwise on $T^n$ and, for some $j$, $\partial_j g_N\to h$ uniformly on $T^n$ with $h$ continuous. Then $\partial_j S$ exists everywhere, is continuous, and equals $h$.
>
> **Hint:** Integrate $\partial_j g_N$ along a coordinate segment (fundamental theorem of calculus), pass the uniform limit inside the integral, then differentiate the resulting integral of a continuous function.
>
> **Why needed:** It upgrades the uniform convergence produced by the M-test in the Formal Proof from "the sum is continuous" to "the sum is smooth with the expected derivatives".
>
> > [!note]- Full proof
> > **An integral identity for each partial sum.** Fix a point $x\in T^n$, represented by $x\in\mathbb R^n$, and consider the coordinate segment $s\mapsto x+se_j$. By the fundamental theorem of calculus, applied to the smooth function $s\mapsto g_N(x+se_j)$ whose derivative is $(\partial_jg_N)(x+se_j)$,
> > $$g_N(x+te_j)-g_N(x)=\int_0^t(\partial_j g_N)(x+se_j)\,ds\qquad(t\in\mathbb R)\qquad\text{(fundamental theorem of calculus).}$$
> > **Passing to the limit.** As $N\to\infty$, the left-hand side converges to $S(x+te_j)-S(x)$ by the pointwise convergence $g_N\to S$. On the right-hand side, $(\partial_jg_N)(x+se_j)\to h(x+se_j)$ uniformly in $s\in[0,t]$, and a uniformly convergent sequence may be integrated term by term over the bounded interval $[0,t]$ (the error is bounded by $|t|\sup_s|\partial_jg_N-h|\to0$). Hence
> > $$S(x+te_j)-S(x)=\int_0^t h(x+se_j)\,ds\qquad\text{(pointwise limit on the left; uniform convergence on the right).}$$
> > **Differentiating.** The right-hand side is the integral of the continuous function $s\mapsto h(x+se_j)$, so by the fundamental theorem of calculus it is differentiable in $t$ with derivative $h(x+te_j)$; at $t=0$ this reads $(\partial_j S)(x)=h(x)$. Since $x$ was arbitrary and $h$ is continuous, $\partial_jS$ exists everywhere and equals the continuous function $h$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $u,v\in C^\infty(T^n;\mathbb C)$. We prove the four parts in order, each building on the previous.
>
> **Step 0 — preliminaries and well-posedness.** For every $\xi\in\mathbb Z^n$ the integral defining $\hat u(\xi)$ is the integral of a continuous function over the compact set $T^n$, hence finite; so the coefficient sequence $(\hat u(\xi))_\xi$ is well defined. We record the **orthogonality of characters**, used repeatedly: for $\zeta\in\mathbb Z^n$,
> $$(2\pi)^{-n}\int_{T^n}e^{i\langle\zeta,x\rangle}\,dx=\prod_{j=1}^n\Big((2\pi)^{-1}\int_{-\pi}^\pi e^{i\zeta_j x_j}\,dx_j\Big)=\prod_{j=1}^n\delta_{\zeta_j,0}=\delta_{\zeta,0},$$
> by Fubini and the one-variable computation $\int_{-\pi}^\pi e^{i\zeta_jx_j}\,dx_j=0$ for $\zeta_j\ne0$ (established inside Lemma 2) and $=2\pi$ for $\zeta_j=0$.
>
> **Part (i) — differentiation is multiplication by $i\xi$, and rapid decrease.**
>
> **Integration by parts with no boundary term.** Fix $j$ and $\xi$. Because $u$ and the character are smooth and $2\pi$-periodic, Fubini's theorem lets us integrate first in the variable $x_j$ over one period $[-\pi,\pi]$:
> $$\widehat{\partial_j u}(\xi)=(2\pi)^{-n}\int_{T^n}(\partial_j u)(x)\,e^{-i\langle\xi,x\rangle}\,dx=(2\pi)^{-n}\int_{[-\pi,\pi]^{n-1}}\!\Big(\int_{-\pi}^\pi(\partial_j u)\,e^{-i\langle\xi,x\rangle}\,dx_j\Big)dx'\qquad\text{(Fubini; }x'\text{ the other variables).}$$
> Integrating the inner integral by parts in $x_j$, with $e^{-i\langle\xi,x\rangle}$ differentiated to $-i\xi_j\,e^{-i\langle\xi,x\rangle}$,
> $$\int_{-\pi}^\pi(\partial_j u)\,e^{-i\langle\xi,x\rangle}\,dx_j=\Big[u\,e^{-i\langle\xi,x\rangle}\Big]_{x_j=-\pi}^{x_j=\pi}-\int_{-\pi}^\pi u\cdot(-i\xi_j)\,e^{-i\langle\xi,x\rangle}\,dx_j=i\xi_j\int_{-\pi}^\pi u\,e^{-i\langle\xi,x\rangle}\,dx_j,$$
> where **the boundary term vanishes by $2\pi$-periodicity**: both $u$ and $e^{-i\langle\xi,x\rangle}$ take equal values at $x_j=-\pi$ and $x_j=\pi$ (for the character, $e^{-i\xi_j\pi}=e^{i\xi_j\pi}$ since $\xi_j\in\mathbb Z$), so the bracket is zero. Reassembling by Fubini gives $\widehat{\partial_j u}(\xi)=i\xi_j\,\hat u(\xi)$. Iterating the identity once for each factor of $\partial^\alpha=\partial_1^{\alpha_1}\cdots\partial_n^{\alpha_n}$ (each application is licensed by the smoothness and periodicity of the intermediate derivatives) yields $\widehat{\partial^\alpha u}(\xi)=(i\xi)^\alpha\hat u(\xi)=i^{|\alpha|}\xi^\alpha\hat u(\xi)$.
>
> **From the identity to rapid decrease.** Taking absolute values and using $|e^{-i\langle\xi,x\rangle}|=1$ together with $\operatorname{vol}(T^n)=(2\pi)^n$,
> $$|\xi^\alpha|\,|\hat u(\xi)|=|\widehat{\partial^\alpha u}(\xi)|\le(2\pi)^{-n}\int_{T^n}|\partial^\alpha u|\,dx\le\lVert\partial^\alpha u\rVert_{C^0}\qquad(\text{triangle inequality for integrals; }(2\pi)^{-n}\!\int_{T^n}1=1).$$
> Now fix $N\in\mathbb Z_{\ge0}$. We compare the radial weight with monomials: from $|\xi|\le\sqrt n\max_j|\xi_j|$ we get, for each $0\le k\le N$, $|\xi|^k\le n^{k/2}\max_j|\xi_j|^k\le n^{k/2}\sum_{|\alpha|=k}|\xi^\alpha|$, and hence by the binomial theorem
> $$(1+|\xi|)^N=\sum_{k=0}^N\binom Nk|\xi|^k\le\sum_{k=0}^N\binom Nk n^{k/2}\sum_{|\alpha|=k}|\xi^\alpha|\le B_{N,n}\sum_{|\alpha|\le N}|\xi^\alpha|,\qquad B_{N,n}:=\max_{0\le k\le N}\binom Nk n^{k/2}.$$
> Multiplying the coefficient bound by these weights,
> $$(1+|\xi|)^N|\hat u(\xi)|\le B_{N,n}\sum_{|\alpha|\le N}|\xi^\alpha|\,|\hat u(\xi)|\le B_{N,n}\sum_{|\alpha|\le N}\lVert\partial^\alpha u\rVert_{C^0}=:C_N\qquad\text{(monomial comparison; coefficient bound),}$$
> with $C_N<\infty$ because $u$ is smooth on the compact $T^n$, so all its derivatives are bounded. Thus $|\hat u(\xi)|\le C_N(1+|\xi|)^{-N}$ for every $N$ and every $\xi$, i.e. $(\hat u(\xi))_\xi\in\mathscr S(\mathbb Z^n)$. This proves part (i).
>
> **Part (ii) — uniform reconstruction with all derivatives.**
>
> **The termwise-differentiated series converges uniformly.** Fix a multi-index $\alpha$ and consider the series $\sum_\xi(i\xi)^\alpha\hat u(\xi)\,e^{i\langle\xi,x\rangle}$. Its general term has modulus $|\xi^\alpha|\,|\hat u(\xi)|\le|\xi|^{|\alpha|}|\hat u(\xi)|\le(1+|\xi|)^{|\alpha|}|\hat u(\xi)|$, and applying the rapid-decrease bound of part (i) with $N=|\alpha|+n+1$,
> $$|\xi^\alpha|\,|\hat u(\xi)|\le(1+|\xi|)^{|\alpha|}\cdot C_N(1+|\xi|)^{-(|\alpha|+n+1)}=C_N(1+|\xi|)^{-(n+1)}\qquad(\text{part (i), }N=|\alpha|+n+1).$$
> The majorant $\sum_\xi C_N(1+|\xi|)^{-(n+1)}$ is finite by **Lemma 1** (which states $\sum_\xi(1+|\xi|)^{-s}<\infty$ for $s>n$, here $s=n+1>n$). By the Weierstrass M-test, the series $\sum_\xi(i\xi)^\alpha\hat u(\xi)e^{i\langle\xi,x\rangle}$ converges absolutely and uniformly on $T^n$; the case $\alpha=0$ is the Fourier series itself.
>
> **The sum is smooth.** Let $S(x)=\sum_\xi\hat u(\xi)e^{i\langle\xi,x\rangle}$ (the $\alpha=0$ case), a uniform limit of continuous partial sums, hence continuous. Enumerate the lattice so that the partial sums $g_M=\sum_{\max_j|\xi_j|\le M}\hat u(\xi)e^{i\langle\xi,x\rangle}$ are smooth; then $g_M\to S$ uniformly, and for each $j$, $\partial_j g_M=\sum_{\max_k|\xi_k|\le M}(i\xi_j)\hat u(\xi)e^{i\langle\xi,x\rangle}\to h_j:=\sum_\xi(i\xi_j)\hat u(\xi)e^{i\langle\xi,x\rangle}$ uniformly, with $h_j$ continuous (again a uniform limit). By **Lemma 5**, $S$ is differentiable with $\partial_jS=h_j$ continuous. Applying Lemma 5 repeatedly — the same argument with $S$ replaced by $\partial^\beta S$ and $g_M$ by $\partial^\beta g_M$, each of which converges uniformly by the M-test above — shows $S\in C^\infty(T^n)$ with $\partial^\alpha S=\sum_\xi(i\xi)^\alpha\hat u(\xi)e^{i\langle\xi,x\rangle}$ for every $\alpha$.
>
> **The sum equals $u$.** We show $S$ and $u$ have the same Fourier coefficients. For fixed $\xi$,
> $$\hat S(\xi)=(2\pi)^{-n}\int_{T^n}S(x)e^{-i\langle\xi,x\rangle}\,dx=(2\pi)^{-n}\int_{T^n}\Big(\sum_\eta\hat u(\eta)e^{i\langle\eta,x\rangle}\Big)e^{-i\langle\xi,x\rangle}\,dx=\sum_\eta\hat u(\eta)\,(2\pi)^{-n}\int_{T^n}e^{i\langle\eta-\xi,x\rangle}\,dx,$$
> where the interchange of sum and integral is justified because the series for $S$ converges **uniformly** on the finite-measure space $T^n$, so integration against the bounded function $e^{-i\langle\xi,x\rangle}$ commutes with the sum (the partial sums converge uniformly, and $\int_{T^n}$ of a uniform limit is the limit of the integrals). By the orthogonality of Step 0, $(2\pi)^{-n}\int_{T^n}e^{i\langle\eta-\xi,x\rangle}dx=\delta_{\eta,\xi}$, so only $\eta=\xi$ survives and $\hat S(\xi)=\hat u(\xi)$. Therefore $S-u$ is continuous with $\widehat{S-u}(\xi)=0$ for all $\xi$, and by **Lemma 4** (uniqueness), $S-u\equiv0$, that is $S=u$. Together with the smoothness and the termwise-derivative formula just proved, this is part (ii).
>
> **Part (iii) — Parseval.** By part (ii), $u(x)=\sum_\xi\hat u(\xi)e^{i\langle\xi,x\rangle}$ with the series converging uniformly. Multiply by the bounded continuous function $\overline{v(x)}$ and integrate; uniform convergence again licenses the interchange of sum and integral:
> $$\int_{T^n}u\,\overline v\,dx=\sum_\xi\hat u(\xi)\int_{T^n}e^{i\langle\xi,x\rangle}\,\overline{v(x)}\,dx\qquad\text{(uniform convergence of the }u\text{-series; }\overline v\text{ bounded).}$$
> For the inner integral, conjugate the definition of $\hat v(\xi)$: $\int_{T^n}e^{i\langle\xi,x\rangle}\overline{v(x)}\,dx=\overline{\int_{T^n}e^{-i\langle\xi,x\rangle}v(x)\,dx}=\overline{(2\pi)^n\hat v(\xi)}=(2\pi)^n\overline{\hat v(\xi)}$. Substituting,
> $$\int_{T^n}u\,\overline v\,dx=(2\pi)^n\sum_\xi\hat u(\xi)\,\overline{\hat v(\xi)}.$$
> The series on the right converges absolutely: by the [[Thm - Cauchy-Schwarz Inequality|Cauchy–Schwarz inequality]] — which states that in any inner product space $|\langle a,b\rangle|\le\lVert a\rVert\,\lVert b\rVert$, so that for finitely many non-negative reals $p_1,\dots,p_m,q_1,\dots,q_m$ one has $\sum_k p_kq_k\le(\sum_k p_k^2)^{1/2}(\sum_k q_k^2)^{1/2}$ on $\mathbb R^m$ with the standard inner product — applied with $p_\xi=|\hat u(\xi)|$, $q_\xi=|\hat v(\xi)|$ over any finite subset $F\subset\mathbb Z^n$,
> $$\sum_{\xi\in F}|\hat u(\xi)|\,|\hat v(\xi)|\le\Big(\sum_{\xi\in F}|\hat u(\xi)|^2\Big)^{1/2}\Big(\sum_{\xi\in F}|\hat v(\xi)|^2\Big)^{1/2}\le\Big(\sum_\xi|\hat u(\xi)|^2\Big)^{1/2}\Big(\sum_\xi|\hat v(\xi)|^2\Big)^{1/2}<\infty,$$
> the last two sums being finite by the rapid decrease of part (i) and Lemma 1 (with $s=2(n+1)>n$ after using $|\hat u(\xi)|\le C_{n+1}(1+|\xi|)^{-(n+1)}$). Taking the supremum over finite $F$ shows the double sum converges absolutely, so the manipulation is valid. Setting $v=u$ gives $\lVert u\rVert_{L^2}^2=\int_{T^n}|u|^2\,dx=(2\pi)^n\sum_\xi|\hat u(\xi)|^2=(2\pi)^n\lVert u\rVert_0^2$. This is part (iii).
>
> **Part (iv) — the coefficient map is a bijection onto $\mathscr S$.** The map $\mathcal F(u)=(\hat u(\xi))_\xi$ takes values in $\mathscr S(\mathbb Z^n)$ by part (i), and it is linear because $u\mapsto\hat u(\xi)$ is an integral, hence linear, for each fixed $\xi$.
>
> *Injectivity.* If $\mathcal F(u)=0$ then $u$ is continuous with all Fourier coefficients zero, so $u\equiv0$ by **Lemma 4**. (Equivalently, by part (ii), $u=\sum_\xi 0\cdot e_\xi=0$.)
>
> *Surjectivity and the inverse.* Let $(c_\xi)_\xi\in\mathscr S(\mathbb Z^n)$ be a rapidly decreasing sequence, so $|c_\xi|\le C_N(1+|\xi|)^{-N}$ for every $N$. Define $w(x)=\sum_\xi c_\xi\,e^{i\langle\xi,x\rangle}$. Exactly the argument of part (ii) — the M-test with majorant $C_N(1+|\xi|)^{-(n+1)}$ for each termwise-differentiated series, and Lemma 5 to upgrade to smoothness — shows that $w$ and all its termwise-differentiated series converge uniformly and that $w\in C^\infty(T^n)$. Its Fourier coefficients are, by termwise integration (justified by uniform convergence) and the orthogonality of Step 0,
> $$\hat w(\zeta)=(2\pi)^{-n}\int_{T^n}\Big(\sum_\xi c_\xi e^{i\langle\xi,x\rangle}\Big)e^{-i\langle\zeta,x\rangle}\,dx=\sum_\xi c_\xi\,(2\pi)^{-n}\int_{T^n}e^{i\langle\xi-\zeta,x\rangle}\,dx=\sum_\xi c_\xi\,\delta_{\xi,\zeta}=c_\zeta.$$
> Thus $\mathcal F(w)=(c_\xi)_\xi$, so $\mathcal F$ is surjective, and the assignment $(c_\xi)_\xi\mapsto\sum_\xi c_\xi e^{i\langle\xi,x\rangle}=w$ is a two-sided inverse: it recovers $w$ from $\mathcal F(w)$ (this is part (ii)) and produces from any $(c_\xi)$ a smooth function with those coefficients (just shown). Hence $\mathcal F$ is a linear bijection $C^\infty(T^n;\mathbb C)\to\mathscr S(\mathbb Z^n)$ with the stated inverse.
>
> Combining parts (i)–(iv) completes the proof. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Heat flow on a compact quotient and instantaneous smoothing.** Consider the heat equation $\partial_t u=\Delta u$ on $T^n$ with continuous initial data $u_0$ whose coefficients need not decay rapidly. Writing $u(t,\cdot)=\sum_\xi e^{-|\xi|^2t}\hat u_0(\xi)e_\xi$, the exponential factor $e^{-|\xi|^2t}$ makes the coefficient sequence rapidly decreasing for every $t>0$, so part (iv) shows $u(t,\cdot)$ is smooth however rough $u_0$ was. The theorem applies because the heat semigroup acts as a rapidly decreasing multiplier; it is non-obvious because instantaneous smoothing is invisible in physical space and transparent only through the coefficient dictionary. This is the model for the smoothing estimates that recur in the Seiberg–Witten flow arguments of chapter XI.

**Lattice sums and Epstein zeta functions in statistical mechanics.** The convergence threshold $\sum_\xi(1+|\xi|)^{-s}<\infty\iff s>n$ from Lemma 1 is exactly the abscissa of convergence of the Epstein zeta function $\sum_{\xi\ne0}|\xi|^{-2s}$ attached to the lattice $\mathbb Z^n$, which controls the low-temperature expansion of a lattice gas and the Casimir energy of a field on $T^n$. The theorem's decay bookkeeping is the tool that decides which such sums converge; the point that is easy to get wrong is the shell count, where a naive ball-count worsens the exponent by one.

**Multiplier operators and pseudodifferential calculus.** A sequence $(m_\xi)$ of at-most-polynomial growth defines an operator $T_m u=\sum_\xi m_\xi\hat u(\xi)e_\xi$; by part (i) a constant-coefficient differential operator is the case $m_\xi=p(i\xi)$ for a polynomial $p$, and part (iv) shows $T_m$ maps $C^\infty$ to $C^\infty$ whenever $(m_\xi)$ has polynomial growth (because it maps $\mathscr S$ to $\mathscr S$). Recognising a translation-invariant operator as a Fourier multiplier is the non-obvious first step, and it is the toy model of the symbol calculus that [[Def - Elliptic Differential Operator and Principal Symbol]] builds on the torus and then transports to manifolds.

---

# Bridges

- **[[Thm - Sobolev Norms on the Torus via Fourier Coefficients]]** — the immediate sequel. Part (i) of the present theorem turns the derivative count in the Sobolev norm into multiplication by monomials $\xi^\alpha$ on the coefficient side, and part (iii) turns each $L^2$ norm into a weighted sum $\sum_\xi\xi^{2\alpha}|\hat u(\xi)|^2$. Summing over $|\alpha|\le k$ and comparing $\sum_{|\alpha|\le k}\xi^{2\alpha}$ with $(1+|\xi|^2)^k$ (an elementary polynomial inequality) gives the norm equivalence $W^{k,2}(T^n)=H_k(T^n)$; the whole Sobolev scale on the torus is thereby realised as weighted $\ell^2$ spaces.

- **[[Thm - Sobolev Embedding Theorem]]** — reads off from parts (i)–(ii) and Lemma 1. For $u\in C^\infty(T^n)$ and $|\alpha|\le r$, the bound $\sup|\partial^\alpha u|\le\sum_\xi|\xi^\alpha||\hat u(\xi)|$ (from the uniform reconstruction of $\partial^\alpha u$ in part (ii)) is split by the Cauchy–Schwarz inequality into $\big(\sum_\xi(1+|\xi|^2)^{r-k}\big)^{1/2}\lVert u\rVert_k$, and the weight sum converges by Lemma 1 exactly when $2(k-r)>n$; the estimate on smooth functions then extends to the completion, giving $H_k\hookrightarrow C^r$ for $k-\tfrac n2>r$.

- **[[Thm - Elliptic Estimate for Constant-Coefficient Operators on the Torus]]** — uses part (i) to diagonalise. A constant-coefficient operator $P=\sum_{|\alpha|=\ell}A_\alpha\partial^\alpha$ acts on coefficients by $\widehat{Pu}(\xi)=\sigma(i\xi)\hat u(\xi)$, where $\sigma$ is the symbol; ellipticity means $\sigma(\xi)$ is invertible with $\lVert\sigma(\xi)^{-1}\rVert\lesssim|\xi|^{-\ell}$, so $|\hat u(\xi)|\lesssim|\xi|^{-\ell}|\widehat{Pu}(\xi)|$, which is the elliptic estimate weight by weight. The present theorem is what makes "act on coefficients" legitimate.

- **[[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts]]** — the bridge to geometry. A compact manifold is finitely many chart images inside a torus glued by smooth transition maps; the charts theorem transports every torus statement above to sections of a bundle over a compact manifold, so that Fourier analysis on $T^n$ becomes, through it, the analytic engine of the entire chapter. Parseval and the coefficient bijection are the facts it transports first.

---

# Unlocked by This

> [!tip] Orthonormal basis of $L^2(T^n)$ *(from Functional Analysis)*
> Part (iii) says the characters are orthogonal in $L^2(T^n)$ with $\langle e_\xi,e_\eta\rangle_{L^2}=(2\pi)^n\delta_{\xi,\eta}$, and part (ii) says their finite combinations (trigonometric polynomials) are uniformly, hence $L^2$-, dense in $C^\infty(T^n)$, which is $L^2$-dense in $L^2(T^n)$. Therefore $\{(2\pi)^{-n/2}e_\xi\}_{\xi\in\mathbb Z^n}$ is an orthonormal basis of the Hilbert space $L^2(T^n)$, and $\mathcal F$ extends to a unitary $L^2(T^n)\to\ell^2(\mathbb Z^n)$ up to the constant $(2\pi)^{n/2}$. See **Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order** for the completed spaces.

> [!tip] Poisson summation and theta functions *(from Analytic Number Theory)*
> Once smooth functions are known to equal their Fourier series pointwise (part ii), applying the identity to a periodised Schwartz function yields the Poisson summation formula $\sum_{m\in\mathbb Z^n}f(m)=\sum_{\xi\in\mathbb Z^n}\hat f(\xi)$, from which the modular transformation law of the Jacobi theta function follows. The rapid decrease of part (i) is exactly what makes both sides absolutely convergent.
