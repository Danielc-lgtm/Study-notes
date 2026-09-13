---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order"
tags: [geometry, gauge-theory, analysis, sobolev-spaces]
---

# Notation

Throughout, $n\in\mathbb N$ with $n\ge1$ is the dimension of the integer lattice $\mathbb Z^n\subset\mathbb R^n$, and $\xi=(\xi_1,\dots,\xi_n)\in\mathbb Z^n$ denotes a lattice point. We write $|\xi|:=\big(\sum_{j=1}^n\xi_j^2\big)^{1/2}$ for the Euclidean norm and $|\xi|_\infty:=\max_{1\le j\le n}|\xi_j|$ for the supremum norm; both are used, and the elementary comparison $|\xi|_\infty\le|\xi|\le\sqrt n\,|\xi|_\infty$ between them is the workhorse of the proof. The parameter $t\in\mathbb R$ is a fixed real exponent, and $R\ge1$ is a real radius. The weight appearing in the sum is $(1+|\xi|^2)^{-t}$; this is exactly the weight $(1+|\xi|^2)^{k}$ that defines the Sobolev norm $\lVert u\rVert_k^2=\sum_{\xi\in\mathbb Z^n}(1+|\xi|^2)^k|\hat u(\xi)|^2$ on the torus, evaluated at $k=-t$ against the constant sequence, so this lemma is precisely the summability threshold of the [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order|torus Sobolev weights]].

Because $\mathbb Z^n$ carries no canonical ordering, the symbol $\sum_{\xi\in\mathbb Z^n}a_\xi$ for a family of nonnegative reals $a_\xi\ge0$ means the **unordered sum**
$$\sum_{\xi\in\mathbb Z^n}a_\xi\ :=\ \sup\Big\{\textstyle\sum_{\xi\in F}a_\xi\ :\ F\subseteq\mathbb Z^n\ \text{finite}\Big\}\ \in\ [0,+\infty],$$
the supremum of all finite partial sums. We say the sum **converges**, and write $\sum_{\xi}a_\xi<\infty$, when this supremum is finite. Two standing facts about unordered sums of nonnegative terms are used and are recorded here as Lemma 0 with proof: the value is unchanged by any grouping of the index set into disjoint blocks, and it is the limit of the partial sums along any increasing sequence of finite sets exhausting $\mathbb Z^n$.

We use the Landau-style shorthand $a_m\asymp b_m$ to mean that there are constants $0<c\le C<\infty$, depending only on $n$ and $t$, with $c\,b_m\le a_m\le C\,b_m$ for all $m$ in the stated range; every such $\asymp$ in this page is discharged into an explicit two-sided inequality with named constants, never left as an assertion.

The symbol $\#S$ denotes the cardinality of a finite set $S$. All logarithms and powers are real; for $x>0$ and $s\in\mathbb R$, $x^s:=\exp(s\log x)$, and $x\mapsto x^s$ is strictly decreasing when $s<0$ and strictly increasing when $s>0$ — the monotonicity direction we invoke by name at each use.

---

# Statement

> **Lemma (Convergence of the Lattice Sum).** Let $n\ge1$ and $t\in\mathbb R$. Then:
> $$\sum_{\xi\in\mathbb Z^n}(1+|\xi|^2)^{-t}\ <\ \infty\qquad\text{if and only if}\qquad 2t>n.$$
> Moreover, when $2t>n$ there is a constant $C_{n,t}<\infty$, depending only on $n$ and $t$, such that the tail satisfies
> $$\sum_{\substack{\xi\in\mathbb Z^n\\ |\xi|\ge R}}(1+|\xi|^2)^{-t}\ \le\ C_{n,t}\,R^{\,n-2t}\qquad\text{for every }R\ge1.$$

The two displayed statements are proved together: the shell decomposition that establishes the convergence dichotomy produces the tail bound as its quantitative refinement, and the exponent $n-2t$ in the tail is negative precisely because $2t>n$, so the tail tends to zero as $R\to\infty$ at the polynomial rate $R^{n-2t}$.

---

# Motivation

Every quantitative statement about Sobolev spaces on the flat torus $T^n=\mathbb R^n/2\pi\mathbb Z^n$ rests on being able to decide when a weighted sum over the frequency lattice $\mathbb Z^n$ is finite, and on controlling how fast its tail decays. The [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order|Sobolev norm]] of a function is the weighted $\ell^2$ norm $\lVert u\rVert_k^2=\sum_\xi(1+|\xi|^2)^k|\hat u(\xi)|^2$ of its Fourier coefficients, and the recurring analytic move — in the Sobolev embedding theorem, in the Rellich compactness theorem, in the Sobolev multiplication theorem — is a Cauchy–Schwarz splitting that peels a factor of the pure weight $(1+|\xi|^2)^{-t}$ off the sum and asks that what remains be summable. Whether that residual sum converges, and how large its tail is, is the single arithmetic fact this page settles once and for all so that the four theorems downstream may invoke it by name rather than re-deriving it.

The question is genuinely a question, and the answer is genuinely a threshold, not a triviality. Fix the exponent $t$ and ask: is $\sum_{\xi\in\mathbb Z^n}(1+|\xi|^2)^{-t}$ finite? In dimension one the sum is $\sum_{m\in\mathbb Z}(1+m^2)^{-t}$, which converges for $t>\tfrac12$ and diverges for $t\le\tfrac12$ — the familiar $p$-series threshold, since $(1+m^2)^{-t}\asymp m^{-2t}$ and $\sum m^{-2t}$ converges exactly when $2t>1$. What happens in higher dimension is that the number of lattice points at radius about $m$ grows like $m^{n-1}$, so the effective number of terms of size $m^{-2t}$ is not one but $m^{n-1}$; the sum behaves like $\sum_m m^{n-1}\cdot m^{-2t}=\sum_m m^{n-1-2t}$, and this converges exactly when $n-1-2t<-1$, that is, when $2t>n$. The whole content of the lemma is this counting: **in dimension $n$ the lattice has $n$ dimensions' worth of points to sum over, so the weight must decay faster than the $n$-dimensional volume grows.** The threshold $2t=n$ is exactly the balance point, and — as the borderline is delicate — the lemma is careful to land on the strict side.

We prove the lemma by dimension counting on the lattice directly, with no appeal to measure theory or to the theory of improper multiple integrals. The one continuous ingredient is the elementary one-variable integral comparison for a decreasing function, which we prove from scratch below. This keeps the page self-contained: a reader who knows only the definition of an unordered sum of nonnegative terms and the fundamental theorem of calculus can check every line.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is a single real inequality, $2t>n$, so the interesting question is which apparently different problems are secretly this one.

The first disguised source is **any question of the form "is this weighted $\ell^2$ Fourier series in a Sobolev space?"**. A formal series $\sum_\xi c_\xi e^{i\langle\xi,x\rangle}$ on the torus lies in the negative-order space $H_{-s}(T^n)$ if and only if $\sum_\xi(1+|\xi|^2)^{-s}|c_\xi|^2<\infty$. When the coefficients are of unit size, $|c_\xi|\equiv1$ — the case of the Dirac comb $\sum_\xi e^{i\langle\xi,x\rangle}$ — the membership condition is exactly $\sum_\xi(1+|\xi|^2)^{-s}<\infty$, which is this lemma with $t=s$. The non-obvious bridge is that a distributional object of unit-modulus coefficients is placed on the Sobolev scale purely by the lattice sum: the Dirac comb lies in $H_{-s}$ precisely when $2s>n$, so its Sobolev order is any number strictly below $-n/2$. *Example problem:* show that the periodic Dirac comb on $T^n$ belongs to $H_k(T^n)$ if and only if $2k<-n$, a fact recorded on the [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order|definition page]].

The second disguised source is **a Cauchy–Schwarz estimate that must dominate a supremum or a convolution by an $L^2$ Sobolev norm**. Whenever one bounds a pointwise quantity $\sum_\xi w(\xi)|\hat u(\xi)|$ by splitting $w(\xi)=w(\xi)(1+|\xi|^2)^{-k/2}\cdot(1+|\xi|^2)^{k/2}$ and applying Cauchy–Schwarz, the price is a factor $\big(\sum_\xi w(\xi)^2(1+|\xi|^2)^{-k}\big)^{1/2}$ that must be finite. For the [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]] one takes $w(\xi)=|\xi|^{r}$ with $r$ the number of derivatives, and the residual sum is $\sum_\xi(1+|\xi|^2)^{r-k}$, finite by this lemma exactly when $2(k-r)>n$. The bridge is that the differentiation order $r$ and the Sobolev order $k$ enter only through the difference $k-r$, which is the effective exponent $t=k-r$ fed into the lemma. *Example problem:* determine the least integer $k$ for which every $u\in H_k(T^4)$ has a continuous representative — the answer $k\ge3$ is $2(k-0)>4$.

The third disguised source is **the eigenvalue-counting or spectral-zeta question for the flat Laplacian**. On $T^n$ the operator $1-\Delta$ has eigenfunctions $e^{i\langle\xi,x\rangle}$ with eigenvalues $1+|\xi|^2$, each of multiplicity one. Hence $\sum_\xi(1+|\xi|^2)^{-t}$ is the trace $\operatorname{tr}(1-\Delta)^{-t}$, the value at $t$ of the spectral zeta function of $1-\Delta$. Any question about the finiteness of such a trace — whether a heat or resolvent operator is trace-class, whether a Green's kernel is square-integrable — is this lemma applied to the eigenvalue sequence. The bridge is Weyl's law: the number of eigenvalues below $\lambda$ grows like $\lambda^{n/2}$, which is the same $n$-dimensional count the lattice performs here. *Example problem:* show that the resolvent $(1-\Delta)^{-t}$ on $T^n$ is a Hilbert–Schmidt operator if and only if $2t>n/2$ (apply the lemma to the squared weight).

**Targets (Output Amplification).** This is a technical lemma, and its targets are the four theorems of the chapter that consume it; each combination pairs the lemma with a Cauchy–Schwarz or tail argument to reach a functional-analytic conclusion.

Combined with **a Cauchy–Schwarz splitting of the sup norm**, the convergence half gives the [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]]: for $u\in C^\infty(T^n)$ and $|\alpha|\le r$, one has $\sup|\partial^\alpha u|\le\sum_\xi|\xi|^{|\alpha|}|\hat u(\xi)|\le\big(\sum_\xi(1+|\xi|^2)^{r-k}\big)^{1/2}\lVert u\rVert_k$, and the residual sum converges by this lemma precisely when $2(k-r)>n$, so $k$ derivatives in $L^2$ control $r$ derivatives uniformly. The extra ingredient is the completeness of $C^r(T^n)$, and the payoff is that Sobolev functions of high enough order are genuinely differentiable.

Combined with **the observation that the frequency-truncation operators are finite-rank**, the tail estimate gives the [[Thm - Rellich Compactness Theorem|Rellich compactness theorem]]: the truncation $T_Ru:=\sum_{|\xi|\le R}\hat u(\xi)e^{i\langle\xi,x\rangle}$ satisfies $\lVert u-T_Ru\rVert_m^2=\sum_{|\xi|>R}(1+|\xi|^2)^m|\hat u(\xi)|^2\le(1+R^2)^{m-k}\lVert u\rVert_k^2$ for $k>m$, so the inclusion $H_k\hookrightarrow H_m$ is a norm limit of finite-rank operators and hence compact. Here the lemma is used in the sharper form that a bounded set in $H_k$ has *uniformly small* $H_m$-tails; the payoff is that bounded sequences in the higher space have $H_m$-convergent subsequences.

Combined with **Peetre's inequality and a convolution splitting**, the convergence half gives the [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]]: after Peetre's splitting of the weight, the product estimate $\lVert uv\rVert_k\le C\lVert u\rVert_{k_1}\lVert v\rVert_{k_2}$ reduces to the summability of a weight $\sum_\eta(1+|\eta|^2)^{-(k_1+k_2-k)}$, finite by this lemma exactly when $2(k_1+k_2-k)>n$. The extra ingredient is Young's inequality for sequences; the payoff is that Sobolev spaces of high enough order are Banach algebras, the fact that makes the gauge group a Lie group in later chapters.

---

# Why Is It True

Picture the lattice $\mathbb Z^n$ organised into concentric shells. Put in shell number $m$ all the points whose supremum norm equals $m$, that is, the points on the boundary of the integer cube of side $2m$. The number of such points is the surface count of that cube: it grows like $m^{n-1}$, the number of ways to fill $n-1$ free coordinates once one coordinate has been pinned to the maximum. Every point in shell $m$ has Euclidean norm comparable to $m$ — between $m$ and $\sqrt n\,m$ — so the weight $(1+|\xi|^2)^{-t}$ is comparable to $m^{-2t}$ on the whole shell. The total contribution of shell $m$ is therefore comparable to $m^{n-1}\cdot m^{-2t}=m^{n-1-2t}$, and summing over shells turns the lattice sum into the one-dimensional series $\sum_{m\ge1}m^{n-1-2t}$.

**A sum over an $n$-dimensional lattice with weight $(1+|\xi|^2)^{-t}$ is, up to constants, the one-dimensional $p$-series $\sum_m m^{n-1-2t}$, because the lattice has $\asymp m^{n-1}$ points at radius $m$; the sum converges exactly when $n-1-2t<-1$, i.e. when $2t>n$.** The threshold is the point at which the polynomial growth $m^{n-1}$ of the shell count is exactly cancelled by the decay $m^{-2t}$ down to the borderline $m^{-1}$, whose sum is the harmonic series and just barely diverges; pushing $t$ up past $n/2$ tips the exponent below $-1$ and the geometric-like decay wins.

The tail estimate is the same picture read quantitatively. The points with $|\xi|\ge R$ live in shells numbered $m\gtrsim R$, and the tail of the majorising series $\sum_{m\ge R}m^{n-1-2t}$ is governed by its first surviving term times a geometric factor, giving $\asymp R^{n-2t}$ — the shell radius $R$ raised to the effective exponent $n-2t$. Nothing subtler than "count the points, weigh each shell, sum a $p$-series" is at work; the lemma is dimension counting made precise.

---

# What Makes This Hard

The only genuine difficulty is landing on the correct side of the borderline $2t=n$ with an honest two-sided estimate, rather than a one-sided comparison that silently loses the exact threshold. A comparison that only bounds the shell count above proves convergence for $2t>n$ but says nothing about divergence for $2t\le n$; one must produce a matching *lower* bound on the number of lattice points per shell to close the "only if" direction, and it is easy to write a lower bound that degrades near $m=1$ or that carries a constant tending to zero with $n$. The second trap is the interchange of summation orders: the passage from the sum over $\xi\in\mathbb Z^n$ to the iterated sum over shells is legitimate only because every term is nonnegative, and a reader who imports habits from conditionally convergent series will worry about an ordering that in fact does not exist here — which is why we fix the meaning of the unordered sum in the Notation and prove the grouping principle as Lemma 0.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Decompose $\mathbb Z^n$ into supremum-norm shells $S_m=\{|\xi|_\infty=m\}$. Count each shell two-sidedly, $\#S_m\asymp m^{n-1}$. Bound the weight two-sidedly on each shell, $(1+|\xi|^2)^{-t}\asymp m^{-2t}$ for $t>0$. Multiply and sum to reduce the lattice sum to the $p$-series $\sum_m m^{n-1-2t}$, whose threshold is $2t>n$; read the tail of the same majorant to get the $R^{n-2t}$ bound.

**Subgoal decomposition:**

1. **Legitimise the shell grouping.** Show that an unordered sum of nonnegative terms may be computed by grouping the index set into the disjoint shells and summing the block sums, and equals the limit along any exhaustion.
   - *Hint:* The unordered sum is a supremum of finite partial sums; every finite set is contained in a ball $\{|\xi|_\infty\le K\}$, and every ball is a union of finitely many finite sets.
   - *Why needed:* Without it the passage $\sum_\xi=\sum_m\sum_{S_m}$ is unjustified, and the whole reduction is circular.

2. **Count a shell.** Prove $2n\,m^{n-1}\le\#S_m\le 2n\,3^{\,n-1}m^{n-1}$ for $m\ge1$.
   - *Hint:* $S_m$ is the set of lattice points in the cube $\{|\xi|_\infty\le m\}$ minus those in $\{|\xi|_\infty\le m-1\}$, so $\#S_m=(2m+1)^n-(2m-1)^n$; factor $a^n-b^n$.
   - *Why needed:* The upper count drives convergence and the tail; the lower count drives divergence.

3. **Weigh a shell.** For $t>0$ and $\xi\in S_m$ with $m\ge1$, prove $m^{-2t}\ge(1+|\xi|^2)^{-t}\ge(2n)^{-t}m^{-2t}$.
   - *Hint:* $|\xi|_\infty\le|\xi|\le\sqrt n\,|\xi|_\infty$ gives $m^2\le 1+|\xi|^2\le 2n\,m^2$; raise to the power $-t<0$, reversing inequalities.
   - *Why needed:* It converts the geometric weight into a pure power of the shell index $m$.

4. **Sum the majorant $p$-series and its tail.** Prove $\sum_{m\ge1}m^{-p}<\infty\iff p>1$, and for $p>1$ and integers $M\ge1$, $\sum_{m\ge M}m^{-p}\le\frac{p}{p-1}M^{1-p}$.
   - *Hint:* Integral comparison for the decreasing function $x^{-p}$; compute $\int_M^\infty x^{-p}\,dx=\frac{M^{1-p}}{p-1}$ by the fundamental theorem of calculus.
   - *Why needed:* Steps 2–3 reduce the lattice sum to this series with $p=2t-n+1$; convergence and the tail both come from here.

5. **Assemble and handle $t\le0$ separately.** Combine Steps 1–4 for $t>0$; dispose of $t\le0$ by noting the terms do not tend to zero.
   - *Hint:* For $t\le0$, $(1+|\xi|^2)^{-t}\ge1$ for all $\xi$, so the sum over the infinite lattice is $+\infty$, consistent with $2t\le0<n$.
   - *Why needed:* The dichotomy must be proved for all real $t$, and Steps 2–4 assumed $t>0$ to control the direction of the power inequalities.

---

# Lemma Decomposition

> [!note]- Lemma 0: An unordered sum of nonnegative terms may be grouped and exhausted freely
> **Statement:** Let $(a_\xi)_{\xi\in\mathbb Z^n}$ with $a_\xi\ge0$, and let $\sum_\xi a_\xi=\sup\{\sum_{\xi\in F}a_\xi:F\subseteq\mathbb Z^n\text{ finite}\}\in[0,\infty]$. (a) If $\mathbb Z^n=\bigsqcup_{m\ge0}B_m$ is a partition into disjoint sets $B_m$, then $\sum_\xi a_\xi=\sum_{m\ge0}\big(\sum_{\xi\in B_m}a_\xi\big)$, where each inner sum is itself an unordered sum. (b) If $F_1\subseteq F_2\subseteq\cdots$ are finite with $\bigcup_j F_j=\mathbb Z^n$, then $\sum_\xi a_\xi=\lim_{j\to\infty}\sum_{\xi\in F_j}a_\xi$ (a limit in $[0,\infty]$).
>
> **Hint:** Every finite subset meets only finitely many blocks $B_m$ and is contained in some $F_j$; use the defining supremum in both directions.
>
> **Why needed:** It licenses the reduction $\sum_{\xi\in\mathbb Z^n}=\sum_{m}\sum_{\xi\in S_m}$ over shells, which is the first step of the formal proof.
>
> > [!note]- Full proof
> > Write $S:=\sum_\xi a_\xi\in[0,\infty]$.
> >
> > **Part (b) first.** The partial sums $s_j:=\sum_{\xi\in F_j}a_\xi$ are nondecreasing in $j$ (each $F_{j+1}\supseteq F_j$ adds nonnegative terms), so $\lim_j s_j=\sup_j s_j$ exists in $[0,\infty]$. Since each $F_j$ is a finite subset, $s_j\le S$ by the definition of $S$ as a supremum over all finite subsets; taking the limit, $\sup_j s_j\le S$. Conversely, let $F\subseteq\mathbb Z^n$ be any finite set; since $F$ is finite and $\bigcup_j F_j=\mathbb Z^n$, and the $F_j$ increase, there is a single $j$ with $F\subseteq F_j$ (choose for each $\xi\in F$ an index $j_\xi$ with $\xi\in F_{j_\xi}$, and take $j=\max_{\xi\in F}j_\xi$, finite because $F$ is finite). Then $\sum_{\xi\in F}a_\xi\le s_j\le\sup_j s_j$. Taking the supremum over $F$ gives $S\le\sup_j s_j$. The two inequalities give $S=\sup_j s_j=\lim_j s_j$.
> >
> > **Part (a).** For each $m$ write $T_m:=\sum_{\xi\in B_m}a_\xi\in[0,\infty]$. First we show $\sum_{m\ge0}T_m\le S$. Fix $M$ and a finite set $G_m\subseteq B_m$ for each $m\le M$. The union $G:=\bigcup_{m\le M}G_m$ is finite and, because the $B_m$ are disjoint, $\sum_{m\le M}\sum_{\xi\in G_m}a_\xi=\sum_{\xi\in G}a_\xi\le S$. Taking the supremum over each finite $G_m\subseteq B_m$ independently (legitimate since the left side is a finite sum of the independent inner suprema) gives $\sum_{m\le M}T_m\le S$; letting $M\to\infty$ gives $\sum_{m\ge0}T_m\le S$. For the reverse inequality, let $F\subseteq\mathbb Z^n$ be finite. Because the $B_m$ partition $\mathbb Z^n$, $F$ splits as the disjoint union of the sets $F\cap B_m$, and only finitely many of these are nonempty, say for $m$ in a finite set $I$. Then $\sum_{\xi\in F}a_\xi=\sum_{m\in I}\sum_{\xi\in F\cap B_m}a_\xi\le\sum_{m\in I}T_m\le\sum_{m\ge0}T_m$, using $\sum_{\xi\in F\cap B_m}a_\xi\le T_m$ (a finite subsum of the block is at most the block's supremum). Taking the supremum over finite $F$ gives $S\le\sum_{m\ge0}T_m$. Therefore $S=\sum_{m\ge0}T_m$.

> [!note]- Lemma 1: Two-sided count of a supremum-norm shell
> **Statement:** For an integer $m\ge1$, let $S_m:=\{\xi\in\mathbb Z^n:|\xi|_\infty=m\}$. Then
> $$\#S_m=(2m+1)^n-(2m-1)^n,\qquad\text{and}\qquad 2n\,m^{n-1}\ \le\ \#S_m\ \le\ 2n\,3^{\,n-1}\,m^{n-1}.$$
>
> **Hint:** The closed cube $\{|\xi|_\infty\le m\}$ contains exactly $(2m+1)^n$ lattice points; $S_m$ is the difference of two such cubes. Factor $a^n-b^n$ with $a=2m+1$, $b=2m-1$.
>
> **Why needed:** The lower bound forces divergence at and below the threshold; the upper bound forces convergence above it and yields the tail estimate.
>
> > [!note]- Full proof
> > **The exact count.** A lattice point $\xi$ satisfies $|\xi|_\infty\le m$ if and only if each coordinate satisfies $-m\le\xi_j\le m$, and there are exactly $2m+1$ integers in $[-m,m]$; since the coordinates are chosen independently, the closed cube $\{|\xi|_\infty\le m\}$ contains exactly $(2m+1)^n$ lattice points. Likewise $\{|\xi|_\infty\le m-1\}$ contains $(2(m-1)+1)^n=(2m-1)^n$ points. Now $\{|\xi|_\infty=m\}=\{|\xi|_\infty\le m\}\setminus\{|\xi|_\infty\le m-1\}$, a set difference of nested finite sets, so $\#S_m=(2m+1)^n-(2m-1)^n$.
> >
> > **Factoring the difference.** Set $a:=2m+1$ and $b:=2m-1$, so $a>b>0$ (as $m\ge1$) and $a-b=2$. The algebraic identity $a^n-b^n=(a-b)\sum_{i=0}^{n-1}a^{\,n-1-i}b^{\,i}$ gives
> > $$\#S_m=2\sum_{i=0}^{n-1}a^{\,n-1-i}b^{\,i}.$$
> > The sum has exactly $n$ terms. Each term $a^{\,n-1-i}b^{\,i}$ is a product of $n-1$ factors, each of which is either $a$ or $b$ with $b\le a$; hence every term lies between $b^{\,n-1}$ and $a^{\,n-1}$:
> > $$b^{\,n-1}\ \le\ a^{\,n-1-i}b^{\,i}\ \le\ a^{\,n-1}\qquad(0\le i\le n-1).$$
> > Summing the $n$ terms and multiplying by $2$,
> > $$2n\,b^{\,n-1}\ \le\ \#S_m\ \le\ 2n\,a^{\,n-1}.$$
> >
> > **Discharging the constants.** For $m\ge1$ we have $b=2m-1\ge m$ (since $2m-1\ge m\iff m\ge1$) and $a=2m+1\le 3m$ (since $2m+1\le 3m\iff m\ge1$). Substituting $b\ge m$ into the lower bound and $a\le 3m$ into the upper bound,
> > $$2n\,m^{\,n-1}\ \le\ 2n\,b^{\,n-1}\ \le\ \#S_m\ \le\ 2n\,a^{\,n-1}\ \le\ 2n\,(3m)^{\,n-1}=2n\,3^{\,n-1}m^{\,n-1}.$$
> > This is the claimed two-sided bound. (The lower bound uses $b^{n-1}\ge m^{n-1}$, valid because $b\ge m\ge0$ and $x\mapsto x^{n-1}$ is nondecreasing on $[0,\infty)$; the upper bound uses $a^{n-1}\le(3m)^{n-1}$ for the same reason.)

> [!note]- Lemma 2: Two-sided bound on the weight over a shell
> **Statement:** Let $t>0$. For every integer $m\ge1$ and every $\xi\in S_m$ (that is, $|\xi|_\infty=m$),
> $$(2n)^{-t}\,m^{-2t}\ \le\ (1+|\xi|^2)^{-t}\ \le\ m^{-2t}.$$
>
> **Hint:** From $|\xi|_\infty\le|\xi|\le\sqrt n\,|\xi|_\infty$ get $m^2\le 1+|\xi|^2\le 2n\,m^2$, then raise to the power $-t$, which reverses inequalities because $-t<0$.
>
> **Why needed:** It replaces the geometric weight by a pure power of the shell index, so that Lemma 1's count can be summed as a $p$-series.
>
> > [!note]- Full proof
> > **Comparison of the two norms.** For any $\xi\in\mathbb R^n$, since $|\xi|^2=\sum_{j=1}^n\xi_j^2$ and each $\xi_j^2\le|\xi|_\infty^2$ while at least one $\xi_j^2$ equals $|\xi|_\infty^2$, we have $|\xi|_\infty^2\le|\xi|^2\le n\,|\xi|_\infty^2$; equivalently $|\xi|_\infty\le|\xi|\le\sqrt n\,|\xi|_\infty$. For $\xi\in S_m$ this reads $m^2\le|\xi|^2\le n\,m^2$.
> >
> > **Bounding the weight.** Adding $1$, and using $m\ge1$ to control the additive constant,
> > $$m^2\ \le\ 1+|\xi|^2,\qquad 1+|\xi|^2\ \le\ 1+n\,m^2\ \le\ n\,m^2+n\,m^2\ =\ 2n\,m^2,$$
> > where the middle step $1\le n\,m^2$ holds because $n\ge1$ and $m\ge1$. Thus
> > $$m^2\ \le\ 1+|\xi|^2\ \le\ 2n\,m^2.$$
> >
> > **Raising to the power $-t$.** The map $x\mapsto x^{-t}$ is strictly decreasing on $(0,\infty)$ because $-t<0$, so applying it to the chain above reverses the inequalities:
> > $$(2n\,m^2)^{-t}\ \le\ (1+|\xi|^2)^{-t}\ \le\ (m^2)^{-t}.$$
> > Since $(2n\,m^2)^{-t}=(2n)^{-t}m^{-2t}$ and $(m^2)^{-t}=m^{-2t}$, this is exactly the claimed bound $(2n)^{-t}m^{-2t}\le(1+|\xi|^2)^{-t}\le m^{-2t}$.

> [!note]- Lemma 3: Integral comparison, the $p$-series threshold, and its tail
> **Statement:** Let $p\in\mathbb R$. (a) $\sum_{m\ge1}m^{-p}<\infty$ if and only if $p>1$. (b) If $p>1$ then for every integer $M\ge1$,
> $$\sum_{m\ge M}m^{-p}\ \le\ \frac{p}{\,p-1\,}\,M^{\,1-p}.$$
>
> **Hint:** For $x\in[m,m+1]$, monotonicity of $x^{-p}$ gives $(m+1)^{-p}\le x^{-p}\le m^{-p}$; integrate over unit intervals and telescope. Compute $\int_M^\infty x^{-p}\,dx=\frac{M^{1-p}}{p-1}$ for $p>1$ by the fundamental theorem of calculus.
>
> **Why needed:** Lemmas 1–2 reduce the lattice sum to $\sum_m m^{n-1-2t}$, i.e. to this series with $p=2t-n+1$; part (a) gives the dichotomy and part (b) gives the tail rate.
>
> > [!note]- Full proof
> > Assume first $p>0$, so that $f(x):=x^{-p}$ is continuous, positive, and strictly decreasing on $[1,\infty)$; the cases $p\le0$ are settled at the end.
> >
> > **The one-step integral comparison.** Fix an integer $m\ge1$. For $x\in[m,m+1]$ monotonicity of $f$ gives $f(m+1)\le f(x)\le f(m)$, and integrating over the unit interval $[m,m+1]$ (whose length is $1$) preserves these inequalities:
> > $$(m+1)^{-p}\ \le\ \int_m^{m+1}x^{-p}\,dx\ \le\ m^{-p}.\tag{$\ast$}$$
> >
> > **Summing the upper half.** Summing the left inequality in $(\ast)$ over $m=M,M+1,\dots,K-1$ and using additivity of the integral over adjacent intervals,
> > $$\sum_{m=M+1}^{K}m^{-p}=\sum_{m=M}^{K-1}(m+1)^{-p}\ \le\ \sum_{m=M}^{K-1}\int_m^{m+1}x^{-p}\,dx=\int_M^{K}x^{-p}\,dx.$$
> > Summing the right inequality in $(\ast)$ over $m=M,\dots,K-1$ gives, likewise,
> > $$\int_M^{K}x^{-p}\,dx=\sum_{m=M}^{K-1}\int_m^{m+1}x^{-p}\,dx\ \le\ \sum_{m=M}^{K-1}m^{-p}.$$
> > Combining, for all integers $K>M\ge1$,
> > $$\int_M^{K}x^{-p}\,dx\ \le\ \sum_{m=M}^{K-1}m^{-p}\ \le\ \ m^{-p}\Big|_{m=M}+\int_M^{K}x^{-p}\,dx,\tag{$\ast\ast$}$$
> > where the right-hand form adds back the single term $M^{-p}$ to pass from $\sum_{m=M+1}^{K}$ to $\sum_{m=M}^{K-1}$; explicitly $\sum_{m=M}^{K-1}m^{-p}=M^{-p}+\sum_{m=M+1}^{K-1}m^{-p}\le M^{-p}+\int_M^{K}x^{-p}\,dx$.
> >
> > **Evaluating the integral.** For $p\ne1$ the function $x\mapsto\frac{x^{1-p}}{1-p}$ is an antiderivative of $x^{-p}$, so by the fundamental theorem of calculus $\int_M^{K}x^{-p}\,dx=\frac{K^{1-p}-M^{1-p}}{1-p}$. For $p=1$, $\int_M^{K}x^{-1}\,dx=\log K-\log M$.
> >
> > **Part (a), convergence for $p>1$.** Let $p>1$, so $1-p<0$ and $K^{1-p}\to0$ as $K\to\infty$. Then $\int_M^{K}x^{-p}\,dx\to\frac{-M^{1-p}}{1-p}=\frac{M^{1-p}}{p-1}$, a finite limit. By the right inequality of $(\ast\ast)$ with $M=1$, the partial sums $\sum_{m=1}^{K-1}m^{-p}\le 1+\int_1^{K}x^{-p}\,dx\le 1+\frac{1}{p-1}$ are bounded above; being nondecreasing, they converge, so $\sum_{m\ge1}m^{-p}<\infty$.
> >
> > **Part (a), divergence for $p\le1$.** If $0<p\le1$, use the left inequality of $(\ast\ast)$ with $M=1$: $\sum_{m=1}^{K-1}m^{-p}\ge\int_1^{K}x^{-p}\,dx$. For $p=1$ this integral is $\log K\to\infty$; for $0<p<1$ it is $\frac{K^{1-p}-1}{1-p}\to\infty$ because $1-p>0$. In either case the partial sums are unbounded, so $\sum_{m\ge1}m^{-p}=\infty$. If $p\le0$, then $m^{-p}\ge1$ for every $m\ge1$, so the partial sums exceed $K-1\to\infty$ and again the series diverges. Thus $\sum_{m\ge1}m^{-p}<\infty$ if and only if $p>1$.
> >
> > **Part (b), the tail bound.** Let $p>1$ and $M\ge1$. Letting $K\to\infty$ in the right inequality of $(\ast\ast)$ (the partial sums increase to the tail, and the integral increases to its finite limit),
> > $$\sum_{m\ge M}m^{-p}\ \le\ M^{-p}+\int_M^{\infty}x^{-p}\,dx\ =\ M^{-p}+\frac{M^{1-p}}{p-1}.$$
> > Since $M\ge1$ we have $M^{-p}=M^{1-p}\cdot M^{-1}\le M^{1-p}$, hence
> > $$\sum_{m\ge M}m^{-p}\ \le\ M^{1-p}\Big(1+\frac{1}{p-1}\Big)=\frac{p}{\,p-1\,}\,M^{1-p}.$$
> > This is the claimed tail estimate.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $n\ge1$ and $t\in\mathbb R$. We must prove the dichotomy $\sum_{\xi\in\mathbb Z^n}(1+|\xi|^2)^{-t}<\infty\iff 2t>n$, and the tail bound for $2t>n$. All terms $(1+|\xi|^2)^{-t}$ are positive, so every sum below is an unordered sum of nonnegative terms in the sense fixed in the Notation.
>
> **Step 0 — the degenerate range $t\le0$.** Suppose $t\le0$. Then $-t\ge0$, and since $1+|\xi|^2\ge1$ for every $\xi\in\mathbb Z^n$, the increasing map $x\mapsto x^{-t}$ (nondecreasing because $-t\ge0$) gives $(1+|\xi|^2)^{-t}\ge 1^{-t}=1$ for every $\xi$. The lattice $\mathbb Z^n$ is infinite, so for every $N$ there is a finite set $F$ with $\#F\ge N$, whence $\sum_{\xi\in F}(1+|\xi|^2)^{-t}\ge\#F\ge N$; the supremum over finite $F$ is therefore $+\infty$, and the sum diverges. On the other hand $2t\le0<n$ (as $n\ge1$), so the condition "$2t>n$" is false. Hence the equivalence "$\text{sum finite}\iff 2t>n$" holds vacuously on this range: both sides are false. It remains to treat $t>0$, which we assume from now on.
>
> **Step 1 — reduction to a sum over shells.** Partition the lattice by supremum norm: $\mathbb Z^n=\{0\}\sqcup\bigsqcup_{m\ge1}S_m$ with $S_m=\{\xi:|\xi|_\infty=m\}$, a disjoint partition because every nonzero $\xi$ has a unique value $|\xi|_\infty=m\ge1$ and the only point with $|\xi|_\infty=0$ is $\xi=0$. By the grouping principle (Lemma 0(a)), applied to the nonnegative family $a_\xi=(1+|\xi|^2)^{-t}$,
> $$\sum_{\xi\in\mathbb Z^n}(1+|\xi|^2)^{-t}=\underbrace{(1+0)^{-t}}_{=\,1}+\sum_{m\ge1}\Sigma_m,\qquad\text{where }\ \Sigma_m:=\sum_{\xi\in S_m}(1+|\xi|^2)^{-t}.\tag{1}$$
> The constant first term $1$ is finite and affects neither convergence nor the tail (which starts at $|\xi|\ge R\ge1$, hence excludes $\xi=0$), so the dichotomy and the tail are governed entirely by $\sum_{m\ge1}\Sigma_m$.
>
> **Step 2 — two-sided estimate of each shell sum.** Fix $m\ge1$. Each $\xi\in S_m$ contributes a weight controlled by Lemma 2 (valid since $t>0$): $(2n)^{-t}m^{-2t}\le(1+|\xi|^2)^{-t}\le m^{-2t}$. Summing this over the $\#S_m$ points of $S_m$,
> $$(2n)^{-t}m^{-2t}\,\#S_m\ \le\ \Sigma_m\ \le\ m^{-2t}\,\#S_m.$$
> Now insert Lemma 1's count $2n\,m^{n-1}\le\#S_m\le 2n\,3^{n-1}m^{n-1}$. Using the lower count in the lower bound and the upper count in the upper bound,
> $$\underbrace{(2n)^{1-t}}_{=:\,c_1}\,m^{\,n-1-2t}\ \le\ \Sigma_m\ \le\ \underbrace{2n\,3^{\,n-1}}_{=:\,c_2}\,m^{\,n-1-2t}\qquad(m\ge1),\tag{2}$$
> where $c_1=(2n)^{-t}\cdot 2n=(2n)^{1-t}>0$ and $c_2=2n\,3^{n-1}<\infty$ depend only on $n$ and $t$. Thus $\Sigma_m\asymp m^{\,n-1-2t}$ with the explicit constants $c_1,c_2$.
>
> **Step 3 — the convergence dichotomy.** Set $p:=2t-n+1$, so that the exponent in (2) is $n-1-2t=-p$. By Lemma 0(b) applied to the nonnegative shell contributions (equivalently, monotone summation of a nonnegative series), $\sum_{m\ge1}\Sigma_m$ and $\sum_{m\ge1}m^{-p}$ are simultaneously finite or infinite by the comparison (2): if $\sum_m m^{-p}<\infty$ then $\sum_m\Sigma_m\le c_2\sum_m m^{-p}<\infty$, and if $\sum_m m^{-p}=\infty$ then $\sum_m\Sigma_m\ge c_1\sum_m m^{-p}=\infty$. By Lemma 3(a),
> $$\sum_{m\ge1}m^{-p}<\infty\iff p>1\iff 2t-n+1>1\iff 2t>n.$$
> Combining with (1): $\sum_{\xi}(1+|\xi|^2)^{-t}<\infty\iff\sum_m\Sigma_m<\infty\iff 2t>n$. This proves the equivalence for $t>0$, and with Step 0 for all real $t$.
>
> **Step 4 — the tail estimate for $2t>n$.** Assume now $2t>n$, so $p=2t-n+1>1$, and let $R\ge1$. We bound $\sum_{|\xi|\ge R}(1+|\xi|^2)^{-t}$.
>
> *Locating the far points in high shells.* If $|\xi|\ge R$ then, by $|\xi|\le\sqrt n\,|\xi|_\infty$ (the comparison of norms from Lemma 2's proof), $|\xi|_\infty\ge|\xi|/\sqrt n\ge R/\sqrt n$. Hence, writing $M:=\lceil R/\sqrt n\rceil$ for the least integer $\ge R/\sqrt n$ (and $M\ge1$ since $R\ge1$),
> $$\{\xi:|\xi|\ge R\}\ \subseteq\ \{\xi:|\xi|_\infty\ge R/\sqrt n\}\ =\ \bigsqcup_{m\ge M}S_m.$$
> *Summing the tail.* Because all terms are nonnegative, enlarging the index set only increases the sum (Lemma 0(a) with the extra blocks contributing nonnegative amounts), so
> $$\sum_{|\xi|\ge R}(1+|\xi|^2)^{-t}\ \le\ \sum_{m\ge M}\Sigma_m\ \overset{(2)}{\le}\ c_2\sum_{m\ge M}m^{-p}\ \overset{\text{Lemma 3(b)}}{\le}\ c_2\cdot\frac{p}{\,p-1\,}\,M^{\,1-p}.$$
> *Converting the exponent.* Here $1-p=n-2t<0$, and $M\ge R/\sqrt n$; since the exponent is negative and $x\mapsto x^{1-p}$ is decreasing,
> $$M^{\,1-p}\ \le\ \Big(\frac{R}{\sqrt n}\Big)^{1-p}=(\sqrt n)^{\,p-1}R^{\,1-p}=(\sqrt n)^{\,2t-n}\,R^{\,n-2t}.$$
> *Collecting constants.* Combining the last two displays,
> $$\sum_{|\xi|\ge R}(1+|\xi|^2)^{-t}\ \le\ \underbrace{c_2\cdot\frac{p}{\,p-1\,}\cdot(\sqrt n)^{\,2t-n}}_{=:\,C_{n,t}}\ R^{\,n-2t}\qquad(R\ge1),$$
> with $C_{n,t}=2n\,3^{n-1}\cdot\frac{2t-n+1}{\,2t-n\,}\cdot n^{\,(2t-n)/2}<\infty$ depending only on $n$ and $t$ (finite because $2t-n>0$). This is the claimed tail bound.
>
> **Conclusion.** For every real $t$ the sum $\sum_{\xi\in\mathbb Z^n}(1+|\xi|^2)^{-t}$ is finite if and only if $2t>n$ (Steps 0–3), and in that case its tail beyond radius $R\ge1$ is at most $C_{n,t}R^{n-2t}$ (Step 4). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Number theory — the Epstein zeta function and lattice point counting.** The sum $\sum_{\xi\ne0}|\xi|^{-2s}$ is the Epstein zeta function of the standard lattice, and the present lemma (with the harmless replacement of $|\xi|^2$ by $1+|\xi|^2$, which changes only the behaviour near the origin) shows it converges exactly for $2s>n$, i.e. $\operatorname{Re}(2s)>n$ for the analytic continuation's abscissa. The theorem applies because the Epstein zeta is precisely a lattice sum of a radial power weight; the non-obvious part is that the convergence abscissa is dictated by the dimension alone, not by the finer arithmetic of the lattice, which is exactly what the shell count isolates. This is the entry point to the Gauss circle problem, where one asks for the *error* in $\#\{|\xi|\le R\}\approx\omega_n R^n$ rather than merely its order.

**Statistical mechanics — the Bose gas and Bose–Einstein condensation.** The occupation sum for an ideal Bose gas in a box with periodic boundary conditions is $\sum_{\xi\in\mathbb Z^n}\big(e^{\beta(|\xi|^2-\mu)}-1\big)^{-1}$, and near the critical chemical potential $\mu\to0^-$ the small-frequency behaviour of each term is $\sim(\beta(|\xi|^2-\mu))^{-1}$, so the question of whether the total particle number stays finite as $\mu\to0$ is the question of whether $\sum_\xi|\xi|^{-2}$ converges — the lemma with $t=1$. The theorem applies because the mode sum is a lattice sum of an inverse-power weight; the payoff, non-obvious physically, is that a macroscopic condensate can form only when $2t=2\le n$ fails to hold, i.e. only in dimension $n\ge3$, recovering the textbook fact that there is no Bose–Einstein condensation in one or two dimensions.

**Numerical analysis — spectral accuracy of Fourier truncation.** When a smooth periodic function is approximated by truncating its Fourier series at radius $R$, the squared $H_m$ error is $\sum_{|\xi|>R}(1+|\xi|^2)^m|\hat u(\xi)|^2$; if $u\in H_k$ with $k>m$, one factors $(1+|\xi|^2)^m=(1+|\xi|^2)^{-(k-m)}\cdot(1+|\xi|^2)^k$ and the tail estimate of this lemma with $t=k-m$ bounds the error by $C R^{-2(k-m)}\lVert u\rVert_k^2$. The theorem applies because the truncation error is literally a lattice tail; the non-obvious payoff is the rate of spectral convergence, $R^{-(k-m)}$ in norm, whose exponent is the number of extra derivatives — the quantitative form of the Rellich estimate.

---

# Bridges

- **From the lattice sum to the Sobolev embedding theorem.** The embedding $H_k(T^n)\hookrightarrow C^r(T^n)$ for $k-r>n/2$ is built by writing, for a smooth periodic function and a derivative index $|\alpha|\le r$, the sup-norm bound $\sup|\partial^\alpha u|\le\sum_\xi|\xi|^{|\alpha|}|\hat u(\xi)|$ (each derivative multiplies the Fourier coefficient by $(i\xi)^\alpha$, and the series converges absolutely), then splitting the summand as $|\xi|^{|\alpha|}=|\xi|^{|\alpha|}(1+|\xi|^2)^{-k/2}\cdot(1+|\xi|^2)^{k/2}$ and applying Cauchy–Schwarz. The residual weight is $\sum_\xi|\xi|^{2|\alpha|}(1+|\xi|^2)^{-k}\le\sum_\xi(1+|\xi|^2)^{r-k}$, which the convergence half of this lemma renders finite exactly when $2(k-r)>n$. The lemma is the whole reason the embedding has the exponent it does. See [[Thm - Sobolev Embedding Theorem]].

- **From the tail estimate to the Rellich compactness theorem.** To show the inclusion $H_k(T^n)\hookrightarrow H_m(T^n)$ with $k>m$ is compact, one approximates it in operator norm by the finite-rank frequency truncations $T_R$. The error is controlled by the crude weight tail $\lVert u-T_Ru\rVert_m^2=\sum_{|\xi|>R}(1+|\xi|^2)^m|\hat u(\xi)|^2\le(1+R^2)^{m-k}\lVert u\rVert_k^2$, which needs only the monotonicity of the weight rather than the full lattice sum; but the sharper quantitative form of Rellich, and the corresponding statements for non-integer orders and for the manifold case, use the tail estimate of this lemma to make the smallness of the far frequencies uniform over bounded families. See [[Thm - Rellich Compactness Theorem]].

- **From the lattice sum to the Sobolev multiplication theorem.** The product of two periodic functions has Fourier coefficients given by the convolution $\widehat{uv}(\xi)=\sum_\eta\hat u(\xi-\eta)\hat v(\eta)$. Estimating the weighted $\ell^2$ norm of this convolution by Peetre's inequality and Cauchy–Schwarz produces, as the decisive factor, a summable weight $\big(\sum_\eta(1+|\eta|^2)^{-(k_1+k_2-k)}\big)^{1/2}$; this lemma makes that factor finite precisely under the multiplication theorem's hypothesis $2(k_1+k_2-k)>n$. The convergence threshold of the lattice sum is what turns the convolution bound into an algebra property. See [[Thm - Sobolev Multiplication Theorem]].

- **From the lattice sum to the Sobolev scale itself.** The comparison $m^2\le 1+|\xi|^2\le 2n\,m^2$ used in Lemma 2, together with the elementary inequality $\sum_{|\alpha|\le k}\xi^{2\alpha}\asymp(1+|\xi|^2)^k$, is the arithmetic backbone of the identification $W^{k,2}(T^n)=H_k(T^n)$ on the [[Thm - Sobolev Norms on the Torus via Fourier Coefficients|Fourier characterisation of Sobolev norms]]. The same two-sided weight control that this page uses to sum a series is what makes the two definitions of the Sobolev norm equivalent.

---

# Unlocked by This

> [!tip] The Dirac comb on the Sobolev scale *(from Distribution Theory)*
> The periodic Dirac comb $\sum_{\xi\in\mathbb Z^n}e^{i\langle\xi,x\rangle}$ has all Fourier coefficients equal to $1$, so its formal $H_k$ norm is $\big(\sum_\xi(1+|\xi|^2)^k\big)^{1/2}$; by this lemma with $t=-k$ it is finite exactly when $2k<-n$. Thus the comb is a distribution of every negative order strictly below $-n/2$, and no better — the precise placement of the sharpest singular periodic object on the Sobolev scale. See [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order]].

> [!note] Exercise Index — §9.2 Sobolev Embedding, Rellich Compactness, and Multiplication
> This lemma is drilled directly in **[[Ex - The Lattice Sum Converges iff 2t Exceeds n]]**, and used throughout the section's other exercises.
> [[Exercise Index - §9.2 Sobolev Embedding, Rellich Compactness, and Multiplication]]
