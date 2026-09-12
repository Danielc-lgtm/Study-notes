---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Sobolev Multiplication Theorem"
  - "Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order"
  - "Thm - Convergence of the Lattice Sum"
  - "Thm - Sobolev Norms on the Torus via Fourier Coefficients"
tags: [geometry, gauge-theory, sobolev-spaces, analysis]
---

# Problem Statement

Work on the flat four-torus $T^4=\mathbb R^4/2\pi\mathbb Z^4$, so $n:=\dim T^4=4$. For $k\in\mathbb Z$ let $H_k(T^4)$ denote the Sobolev space of integer order $k$, with norm
$$\lVert u\rVert_k^2=\sum_{\xi\in\mathbb Z^4}\langle\xi\rangle^{2k}\,|\hat u(\xi)|^2,\qquad\langle\xi\rangle:=(1+|\xi|^2)^{1/2},\qquad\hat u(\xi)=(2\pi)^{-4}\!\int_{T^4}u(x)\,e^{-i\langle\xi,x\rangle}\,dx.$$

Establish the following. This is the four-dimensional instance ("Corollary 1: $W^{k,2}(M^4)$ is an algebra for $k\ge3$") of the [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]] that the Seiberg–Witten construction of chapter XI relies on.

1. **Numerology.** Verify that the pair $(k,n)=(3,4)$ satisfies the algebra threshold $2k>n$ of the multiplication theorem, that $(k,n)=(2,4)$ sits exactly at the borderline $2k=n$, and record what each says about $H_k(T^4)$.
2. **The algebra estimate with an explicit constant.** Prove that for all $u,v\in H_3(T^4)$ the pointwise product lies in $H_3(T^4)$ and
$$\lVert uv\rVert_3\ \le\ C\,\lVert u\rVert_3\,\lVert v\rVert_3,\qquad C=16\,\Lambda^{1/2},\quad \Lambda:=\sum_{\xi\in\mathbb Z^4}\langle\xi\rangle^{-6}=\sum_{\xi\in\mathbb Z^4}(1+|\xi|^2)^{-3}<\infty,$$
so that $H_3(T^4)$, after renorming by $C$, is a Banach algebra. Exhibit *where in the proof the numerology $2\cdot3>4$ is spent*.
3. **The borderline is genuinely not an algebra.** Exhibit an explicit $u\in H_2(T^4)$ whose square $u^2$ does **not** lie in $H_2(T^4)$. Hence $H_2(T^4)$ is not closed under multiplication: the threshold $2k>n$ in Part 2 cannot be relaxed to $2k=n$.

**Recall.**

The objects in play are the Sobolev spaces $H_k(T^4)$ and their Fourier description, the multiplication theorem whose four-dimensional corollary this drills, and the lattice-sum convergence criterion that supplies the finite constant.

![[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order#The Definition]]

We use throughout that for smooth (or $L^2$) functions $u,v$ on $T^4$ the Fourier coefficients of a product are the convolution of the coefficients,
$$\widehat{uv}(\xi)=\sum_{\eta\in\mathbb Z^4}\hat u(\xi-\eta)\,\hat v(\eta)\qquad(\xi\in\mathbb Z^4),$$
which follows by multiplying the two Fourier series and collecting the coefficient of $e^{i\langle\xi,x\rangle}$; the series manipulation is justified in [[Thm - Fourier Series of Smooth Functions on the Torus]] for smooth factors and, for $u\in L^2$, by absolute convergence of the convolution (Cauchy–Schwarz, since $\hat u\in\ell^2(\mathbb Z^4)$).

![[Thm - Sobolev Multiplication Theorem#Statement]]

![[Thm - Convergence of the Lattice Sum#Statement]]

We also use Peetre's inequality in the elementary form derived on [[Thm - Sobolev Norms on the Torus via Fourier Coefficients|the Fourier-norms page]]; the exact constant we need is re-derived from scratch in Step 2 below to keep the constant $C$ explicit.

> [!warning] Convention: which form of the threshold, and a corrected side condition
> Haydys's Theorem 136(iv)(a) states the algebra property as "$kp>n\Rightarrow W^{k,p}(M)$ is an algebra"; with $p=2$ this is $2k>n$, the form used here. Haydys's clause (iv)(b) for products of *different* orders $W^{k_1,p_1}\otimes W^{k_2,p_2}\to W^{k,p}$ omits the side conditions $k\le\min(k_1,k_2)$ and the *strict* inequality in the borderline count; the corrected statement, with $k\le\min(k_1,k_2)$ and $k_1+k_2-k>\tfrac n2$, is the one recorded on [[Thm - Sobolev Multiplication Theorem|the multiplication page]]. Part 2 uses only case (a), $k_1=k_2=k=3$, $2k=6>4=n$, for which no side-condition subtlety arises.

---

# Convergent Strategy

**Problem class.** This is a two-sided calibration exercise on a single inequality: first a *positive* estimate ($H_3$ closes under products, with a named constant), then a *sharpness* construction (the estimate fails at the borderline $H_2$). The value of doing both is that the numerology $2k>n$ is not a black box — the same lattice sum $\sum\langle\xi\rangle^{-6}$ that must converge for the constant to be finite is the sum that *diverges* one step down, and watching the exponent cross the convergence threshold $2k=n$ is the whole content.

**Assumption pattern.** The recognisable trigger for "is this Sobolev space an algebra?" is the comparison $2k$ versus $n$. Above threshold ($2k>n$) the space embeds in $C^0$ and products behave; at or below threshold products can leave the space. The mechanical signature is a *convolution of Fourier coefficients weighted by $\langle\xi\rangle^{2k}$*, controlled by splitting the weight onto the two factors (Peetre) and paying for the leftover with a lattice sum $\sum\langle\xi\rangle^{-2k}$ that converges exactly when $2k>n$.

**Theorem routing.** For Part 2 the route is: pass to Fourier coefficients; write $\langle\xi\rangle^{3}\widehat{uv}(\xi)$ as a convolution; split the weight $\langle\xi\rangle^3\lesssim\langle\xi-\eta\rangle^3+\langle\eta\rangle^3$ (Peetre, explicit constant $8$); bound each of the two resulting sums by [Young's inequality for sequences $\ell^2*\ell^1\subseteq\ell^2$], where the $\ell^1$ factor is finite *because* $\sum\langle\eta\rangle^{-6}=\Lambda<\infty$ — the invocation of [[Thm - Convergence of the Lattice Sum]] with $2t=6>4=n$. For Part 3 the route is: build $u$ by prescribing radially decaying Fourier coefficients tuned to the borderline, with a logarithmic factor placing $u$ just inside $H_2$; then bound $\widehat{u^2}(\xi)=\sum_\eta\hat u(\xi-\eta)\hat u(\eta)$ from below by restricting the (positive) convolution to low frequencies $|\eta|\le|\xi|/2$, where the partial sum $\sum_{|\eta|\le|\xi|/2}\hat u(\eta)$ grows like a power of $\log|\xi|$; the resulting lower bound on $\lVert u^2\rVert_2^2$ is a divergent lattice sum.

**Key decision point.** Two decisions are decisive. In Part 2, *keeping the constant explicit* forces the honest bookkeeping: the only non-elementary input is $\Lambda=\sum\langle\xi\rangle^{-6}<\infty$, and isolating it exposes that the algebra property *is* the convergence of that sum. In Part 3, the delicate choice is the *logarithmic exponent* $\beta$ in $\hat u(\xi)=\langle\xi\rangle^{-4}\big(\log(2+|\xi|)\big)^{-\beta}$: it must be large enough ($2\beta>1$) that $u\in H_2$, yet small enough ($4\beta\le3$, and strictly $4\beta<3$ for a clean divergence) that the low-frequency mass $\sum_{|\eta|\le R}\hat u(\eta)$ still grows like $(\log R)^{1-\beta}$ fast enough to push $u^2$ out of $H_2$. The window $\tfrac12<\beta<\tfrac34$ is exactly the borderline being pried open; we take $\beta=\tfrac23$.

---

# Legal Operations Used

Where the [[Gauge Theory IX — Sobolev Spaces, Elliptic Operators, and Elliptic Complexes|topic page]] numbers its Legal Operations, these are to be reconciled against that list.

1. **Pass a product to the convolution of Fourier coefficients.** Replace $\lVert uv\rVert_k$ by the weighted $\ell^2$ norm of $\widehat{uv}=\hat u*\hat v$.

2. **Split a Japanese-bracket weight across a sum (Peetre).** Use $\langle\xi\rangle^{s}\le C_s(\langle\xi-\eta\rangle^{s}+\langle\eta\rangle^{s})$, derived from $\langle\xi\rangle^2\le2(\langle\xi-\eta\rangle^2+\langle\eta\rangle^2)$, to move the weight onto the two convolution factors.

3. **Bound a convolution by Young's inequality $\ell^2*\ell^1\subseteq\ell^2$.** $\lVert a*b\rVert_{\ell^2}\le\lVert a\rVert_{\ell^2}\lVert b\rVert_{\ell^1}$, proved by writing $a*b=\sum_\eta b(\eta)\tau_\eta a$ and using translation invariance of $\lVert\cdot\rVert_{\ell^2}$.

4. **Turn an $\ell^1$ norm into a norm times a lattice sum by Cauchy–Schwarz.** $\sum_\eta|\hat v(\eta)|=\sum_\eta\langle\eta\rangle^{-k}\langle\eta\rangle^{k}|\hat v(\eta)|\le\Lambda^{1/2}\lVert v\rVert_k$, finite exactly when $2k>n$ ([[Thm - Convergence of the Lattice Sum]]).

5. **Construct a boundary-case function by prescribing radial Fourier coefficients.** Choose $\hat u(\xi)=\langle\xi\rangle^{-2a}\ell(\xi)^{-\beta}$ with $\ell(\xi)=\log(2+|\xi|)$ and tune $(a,\beta)$ against the two shell-sum thresholds.

6. **Lower-bound a positive convolution by restricting its range.** Since $\hat u\ge0$, $\widehat{u^2}(\xi)=\sum_\eta\hat u(\xi-\eta)\hat u(\eta)\ge\sum_{|\eta|\le|\xi|/2}\hat u(\xi-\eta)\hat u(\eta)$, then bound $\hat u(\xi-\eta)$ below uniformly on the restricted range.

7. **Count lattice points in a ball by cube-packing.** $\tfrac{\pi^2}2(\rho-1)^4\le\#\{\eta\in\mathbb Z^4:|\eta|\le\rho\}\le\tfrac{\pi^2}2(\rho+1)^4$, from the unit cubes centred at lattice points.

---

# Hints

> [!note]- Hint 1
> For Part 2, everything happens on the Fourier side: $\lVert uv\rVert_3^2=\sum_\xi\langle\xi\rangle^6|\widehat{uv}(\xi)|^2$ and $\widehat{uv}=\hat u*\hat v$. The obstacle is that the weight $\langle\xi\rangle^3$ sits on the *output* frequency $\xi$, not on the summation variable. Find an inequality that redistributes $\langle\xi\rangle^3$ onto $\langle\xi-\eta\rangle^3$ and $\langle\eta\rangle^3$.

> [!note]- Hint 2
> From $|\xi|^2\le(|\xi-\eta|+|\eta|)^2\le2|\xi-\eta|^2+2|\eta|^2$ deduce $\langle\xi\rangle^2\le2(\langle\xi-\eta\rangle^2+\langle\eta\rangle^2)\le4\max(\langle\xi-\eta\rangle^2,\langle\eta\rangle^2)$, hence $\langle\xi\rangle^3\le8(\langle\xi-\eta\rangle^3+\langle\eta\rangle^3)$. Split the convolution into two sums accordingly. Each is a convolution of one weighted factor with one *bare* factor; bound it by $\lVert\,\cdot\,\rVert_{\ell^2}\,\lVert\,\cdot\,\rVert_{\ell^1}$.

> [!note]- Hint 3
> The bare factor's $\ell^1$ norm is $\sum_\eta|\hat v(\eta)|$. Insert $1=\langle\eta\rangle^{-3}\langle\eta\rangle^{3}$ and apply Cauchy–Schwarz: $\sum_\eta|\hat v(\eta)|\le(\sum_\eta\langle\eta\rangle^{-6})^{1/2}\lVert v\rVert_3=\Lambda^{1/2}\lVert v\rVert_3$. The finiteness of $\Lambda=\sum_{\eta\in\mathbb Z^4}\langle\eta\rangle^{-6}$ is where $2\cdot3=6>4$ is spent — this is the lattice-sum criterion with $2t=6>n=4$.

> [!note]- Hint 4
> For Part 3, set $\hat u(\xi)=\langle\xi\rangle^{-4}\big(\log(2+|\xi|)\big)^{-2/3}$ (real, even in $\xi$, so $u$ is real). Check $u\in H_2$: the shell sum for $\lVert u\rVert_2^2$ behaves like $\sum_R R^{-1}(\log R)^{-4/3}$, which converges. For the failure, use $\hat u\ge0$ and restrict $\widehat{u^2}(\xi)=\sum_\eta\hat u(\xi-\eta)\hat u(\eta)$ to $|\eta|\le|\xi|/2$: there $\hat u(\xi-\eta)\gtrsim|\xi|^{-4}(\log|\xi|)^{-2/3}$, and $\sum_{|\eta|\le|\xi|/2}\hat u(\eta)\gtrsim(\log|\xi|)^{1/3}$. Conclude that $\lVert u^2\rVert_2^2\gtrsim\sum_\xi|\xi|^{-4}(\log|\xi|)^{-2/3}=\infty$.

---

# Solution

The exercise is the numerology $2k>n$ made mechanical. In Part 2 the weight $\langle\xi\rangle^{2k}$ on a product is redistributed onto the factors by Peetre, and the leftover is paid for by the lattice sum $\Lambda=\sum\langle\xi\rangle^{-2k}$, which is finite exactly when $2k>n$; the constant is $C=16\Lambda^{1/2}$. In Part 3 we drop to $2k=n$, where that very sum diverges, and we exploit the divergence to build a function whose square escapes $H_2$: a radial coefficient with a critical power and a fractional logarithm sits inside $H_2$, yet its low-frequency self-convolution accumulates a logarithmic factor that a genuine algebra could not tolerate.

## Part 1 — Numerology

**The threshold $2k$ versus $n=4$.** For $(k,n)=(3,4)$: $2k=6>4=n$, so case (a) of the multiplication theorem applies and $H_3(T^4)$ is a Banach algebra (after renorming). For $(k,n)=(2,4)$: $2k=4=n$, the exact borderline; case (a) requires the *strict* inequality $2k>n$ and therefore does **not** apply, and Part 3 shows the conclusion genuinely fails. Equivalently, in terms of the Sobolev embedding into $C^0$, which holds when $k-\tfrac n2>0$: $H_3(T^4)\hookrightarrow C^0$ since $3-2=1>0$, while $H_2(T^4)\not\hookrightarrow C^0$ since $2-2=0$ is not $>0$. The algebra property and the $C^0$ embedding cross the same threshold $2k=n$, and $H_2(T^4)$ fails both.

## Part 2 — $H_3(T^4)$ is a Banach algebra, with $C=16\Lambda^{1/2}$

We prove $\lVert uv\rVert_3\le 16\Lambda^{1/2}\lVert u\rVert_3\lVert v\rVert_3$ for all $u,v\in H_3(T^4)$, where $\Lambda=\sum_{\xi\in\mathbb Z^4}\langle\xi\rangle^{-6}$. It suffices to prove the estimate for $u,v\in C^\infty(T^4)$: these are dense in $H_3$ (by definition $H_3$ is their completion), the bilinear map $(u,v)\mapsto uv$ then extends by continuity, and both sides are continuous in the $H_3$ norms. We do the smooth case.

**Step 0: The finite constant $\Lambda$ exists.**

The number $\Lambda=\sum_{\xi\in\mathbb Z^4}\langle\xi\rangle^{-6}$ is finite because $6>4$.

> [!note]- Derivation
> By the [[Thm - Convergence of the Lattice Sum|lattice-sum convergence theorem]], $\sum_{\xi\in\mathbb Z^n}(1+|\xi|^2)^{-t}<\infty$ if and only if $2t>n$. Here $n=4$ and $t=3$, and $2t=6>4=n$, so
> $$\Lambda:=\sum_{\xi\in\mathbb Z^4}\langle\xi\rangle^{-6}=\sum_{\xi\in\mathbb Z^4}(1+|\xi|^2)^{-3}<\infty\qquad(\text{lattice-sum theorem, }2t=6>4=n).$$
> **This is the one and only place the numerology $2\cdot3>4$ is used.** Every other step of Part 2 is an identity or an elementary inequality valid for any $k$; the algebra property lives entirely in the finiteness of this single sum.

**Step 1: Peetre's weight splitting with explicit constant $8$.**

For all $\xi,\eta\in\mathbb Z^4$, $\langle\xi\rangle^3\le8\big(\langle\xi-\eta\rangle^3+\langle\eta\rangle^3\big)$.

> [!note]- Derivation
> Write $\langle\zeta\rangle^2=1+|\zeta|^2$. By the triangle inequality $|\xi|\le|\xi-\eta|+|\eta|$ and the elementary bound $(a+b)^2\le2a^2+2b^2$,
> $$|\xi|^2\le(|\xi-\eta|+|\eta|)^2\le2|\xi-\eta|^2+2|\eta|^2\qquad(\text{triangle inequality; }(a+b)^2\le2a^2+2b^2).$$
> Adding $1$ to both sides, and using $1\le4$ to bound the constant term,
> $$\langle\xi\rangle^2=1+|\xi|^2\le1+2|\xi-\eta|^2+2|\eta|^2\le4+2|\xi-\eta|^2+2|\eta|^2=2(1+|\xi-\eta|^2)+2(1+|\eta|^2)=2\big(\langle\xi-\eta\rangle^2+\langle\eta\rangle^2\big)\qquad(\text{previous line; }1\le4).$$
> Since $\langle\xi-\eta\rangle^2+\langle\eta\rangle^2\le2\max(\langle\xi-\eta\rangle^2,\langle\eta\rangle^2)$, we get $\langle\xi\rangle^2\le4\max(\langle\xi-\eta\rangle^2,\langle\eta\rangle^2)$, hence
> $$\langle\xi\rangle^3=(\langle\xi\rangle^2)^{3/2}\le4^{3/2}\max(\langle\xi-\eta\rangle^2,\langle\eta\rangle^2)^{3/2}=8\,\max(\langle\xi-\eta\rangle^3,\langle\eta\rangle^3)\le8\big(\langle\xi-\eta\rangle^3+\langle\eta\rangle^3\big)$$
> $$(\text{raise to the power }3/2;\ 4^{3/2}=8;\ \max\le\text{sum for non-negative terms}).$$
> This is the claimed inequality with the explicit constant $8$.

**Step 2: Young's inequality for sequences, $\ell^2*\ell^1\subseteq\ell^2$.**

For sequences $a\in\ell^2(\mathbb Z^4)$ and $b\in\ell^1(\mathbb Z^4)$, the convolution $a*b$ lies in $\ell^2$ with $\lVert a*b\rVert_{\ell^2}\le\lVert a\rVert_{\ell^2}\lVert b\rVert_{\ell^1}$.

> [!note]- Derivation
> Write $(a*b)(\xi)=\sum_{\eta}a(\xi-\eta)b(\eta)=\sum_\eta b(\eta)\,(\tau_\eta a)(\xi)$, where $(\tau_\eta a)(\xi):=a(\xi-\eta)$ is the translate of $a$. Translation is an isometry of $\ell^2(\mathbb Z^4)$, since re-indexing gives $\lVert\tau_\eta a\rVert_{\ell^2}^2=\sum_\xi|a(\xi-\eta)|^2=\sum_\zeta|a(\zeta)|^2=\lVert a\rVert_{\ell^2}^2$. Therefore, by the triangle inequality for the $\ell^2$ norm applied to the (absolutely convergent) sum $\sum_\eta b(\eta)\tau_\eta a$,
> $$\lVert a*b\rVert_{\ell^2}=\Big\lVert\sum_\eta b(\eta)\,\tau_\eta a\Big\rVert_{\ell^2}\le\sum_\eta|b(\eta)|\,\lVert\tau_\eta a\rVert_{\ell^2}=\Big(\sum_\eta|b(\eta)|\Big)\lVert a\rVert_{\ell^2}=\lVert b\rVert_{\ell^1}\lVert a\rVert_{\ell^2}$$
> $$(\text{triangle inequality in }\ell^2;\ \tau_\eta\text{ an isometry};\ \text{definition of }\lVert b\rVert_{\ell^1}).$$
> (The interchange is legitimate: $\sum_\eta|b(\eta)|\lVert\tau_\eta a\rVert_{\ell^2}=\lVert b\rVert_{\ell^1}\lVert a\rVert_{\ell^2}<\infty$, so the vector-valued series converges absolutely in $\ell^2$.)

**Step 3: Assemble the estimate.**

Splitting the weight (Step 1) and applying Young with the lattice-sum bound (Steps 0, 2) gives $\lVert uv\rVert_3\le16\Lambda^{1/2}\lVert u\rVert_3\lVert v\rVert_3$.

> [!note]- Derivation
> Let $u,v\in C^\infty(T^4)$. By the convolution identity $\widehat{uv}(\xi)=\sum_\eta\hat u(\xi-\eta)\hat v(\eta)$ and the triangle inequality (all following bounds use $|\hat u|,|\hat v|\ge0$),
> $$\langle\xi\rangle^3|\widehat{uv}(\xi)|\le\sum_\eta\langle\xi\rangle^3|\hat u(\xi-\eta)|\,|\hat v(\eta)|\le8\sum_\eta\big(\langle\xi-\eta\rangle^3+\langle\eta\rangle^3\big)|\hat u(\xi-\eta)|\,|\hat v(\eta)|\qquad(\text{convolution identity; Step 1}).$$
> Split into two non-negative sums, $\langle\xi\rangle^3|\widehat{uv}(\xi)|\le8\big(S_1(\xi)+S_2(\xi)\big)$, with
> $$S_1(\xi)=\sum_\eta\big(\langle\xi-\eta\rangle^3|\hat u(\xi-\eta)|\big)\,|\hat v(\eta)|=(a_1*b_1)(\xi),\qquad a_1(\zeta)=\langle\zeta\rangle^3|\hat u(\zeta)|,\ b_1(\eta)=|\hat v(\eta)|,$$
> $$S_2(\xi)=\sum_\eta|\hat u(\xi-\eta)|\,\big(\langle\eta\rangle^3|\hat v(\eta)|\big)=(a_2*b_2)(\xi),\qquad a_2(\zeta)=|\hat u(\zeta)|,\ b_2(\eta)=\langle\eta\rangle^3|\hat v(\eta)|.$$
> **The two $\ell^2$ factors are Sobolev norms:** $\lVert a_1\rVert_{\ell^2}=\big(\sum_\zeta\langle\zeta\rangle^6|\hat u(\zeta)|^2\big)^{1/2}=\lVert u\rVert_3$ and, likewise, $\lVert b_2\rVert_{\ell^2}=\lVert v\rVert_3$.
>
> **The two $\ell^1$ factors are controlled by $\Lambda$.** Inserting $1=\langle\eta\rangle^{-3}\langle\eta\rangle^{3}$ and applying the Cauchy–Schwarz inequality in $\ell^2(\mathbb Z^4)$,
> $$\lVert b_1\rVert_{\ell^1}=\sum_\eta|\hat v(\eta)|=\sum_\eta\langle\eta\rangle^{-3}\big(\langle\eta\rangle^3|\hat v(\eta)|\big)\le\Big(\sum_\eta\langle\eta\rangle^{-6}\Big)^{1/2}\Big(\sum_\eta\langle\eta\rangle^6|\hat v(\eta)|^2\Big)^{1/2}=\Lambda^{1/2}\lVert v\rVert_3$$
> $$(\text{Cauchy–Schwarz};\ \Lambda<\infty\text{ by Step 0}),$$
> and by the identical computation $\lVert a_2\rVert_{\ell^1}=\sum_\eta|\hat u(\eta)|\le\Lambda^{1/2}\lVert u\rVert_3$.
>
> **Young's inequality (Step 2) applied to each sum:**
> $$\lVert S_1\rVert_{\ell^2}=\lVert a_1*b_1\rVert_{\ell^2}\le\lVert a_1\rVert_{\ell^2}\lVert b_1\rVert_{\ell^1}\le\lVert u\rVert_3\cdot\Lambda^{1/2}\lVert v\rVert_3,$$
> $$\lVert S_2\rVert_{\ell^2}=\lVert a_2*b_2\rVert_{\ell^2}\le\lVert a_2\rVert_{\ell^1}\lVert b_2\rVert_{\ell^2}\le\Lambda^{1/2}\lVert u\rVert_3\cdot\lVert v\rVert_3\qquad(\text{Step 2, in the two orderings}).$$
> **Combine.** Taking the $\ell^2(\mathbb Z^4)$ norm of the pointwise bound $\langle\xi\rangle^3|\widehat{uv}(\xi)|\le8(S_1(\xi)+S_2(\xi))$ (monotone for non-negative sequences) and using the triangle inequality,
> $$\lVert uv\rVert_3=\big\lVert\,\langle\cdot\rangle^3\widehat{uv}\,\big\rVert_{\ell^2}\le8\big(\lVert S_1\rVert_{\ell^2}+\lVert S_2\rVert_{\ell^2}\big)\le8\big(2\Lambda^{1/2}\lVert u\rVert_3\lVert v\rVert_3\big)=16\,\Lambda^{1/2}\lVert u\rVert_3\lVert v\rVert_3.$$
> In particular $\widehat{uv}\in\langle\cdot\rangle^{-3}\ell^2$, i.e. $uv\in H_3(T^4)$, and $\lVert uv\rVert_3\le C\lVert u\rVert_3\lVert v\rVert_3$ with $C=16\Lambda^{1/2}$. By density of $C^\infty(T^4)$ in $H_3(T^4)$ the estimate extends to all $u,v\in H_3(T^4)$.

**Renorming to a Banach algebra.** Define the equivalent norm $\lVert u\rVert':=C\lVert u\rVert_3$. Then $\lVert uv\rVert'=C\lVert uv\rVert_3\le C\cdot C\lVert u\rVert_3\lVert v\rVert_3=(C\lVert u\rVert_3)(C\lVert v\rVert_3)=\lVert u\rVert'\lVert v\rVert'$, so $(H_3(T^4),\lVert\cdot\rVert')$ is a Banach algebra (it is complete, being $H_3$ with an equivalent norm, and the norm is submultiplicative). This completes Part 2.

## Part 3 — $H_2(T^4)$ is not an algebra

We construct $u\in H_2(T^4)$ with $u^2\notin H_2(T^4)$. Throughout write $\ell(\xi):=\log(2+|\xi|)$ and set
$$\hat u(\xi):=\langle\xi\rangle^{-4}\,\ell(\xi)^{-2/3}=(1+|\xi|^2)^{-2}\big(\log(2+|\xi|)\big)^{-2/3}\ \ge0,\qquad u:=\sum_{\xi\in\mathbb Z^4}\hat u(\xi)\,e^{i\langle\xi,x\rangle}.$$
The coefficients are real and depend only on $|\xi|$, so $\hat u(-\xi)=\hat u(\xi)=\overline{\hat u(\xi)}$ and $u$ is real-valued. We use the crude lattice counts of Step A repeatedly.

**Step A: Crude lattice-point counts in $\mathbb Z^4$.**

For $\rho\ge1$, $\tfrac{\pi^2}{2}(\rho-1)^4\le\#\{\eta\in\mathbb Z^4:|\eta|\le\rho\}\le\tfrac{\pi^2}{2}(\rho+1)^4$; consequently the dyadic shell $A_j:=\{\eta\in\mathbb Z^4:2^j\le|\eta|<2^{j+1}\}$ has $\#A_j\ge 3\pi^2\,16^{j}$ for every integer $j\ge3$.

> [!note]- Derivation
> To each $\eta\in\mathbb Z^4$ attach the unit cube $Q_\eta:=\eta+(-\tfrac12,\tfrac12]^4$; these are disjoint and tile $\mathbb R^4$, each of Lebesgue volume $1$. Any $x\in Q_\eta$ has $|x-\eta|\le\tfrac12\sqrt4=1$ (half the diagonal of a unit cube).
>
> *Lower count.* If $|x|\le\rho-1$, its nearest lattice point $\eta$ (so $x\in Q_\eta$) satisfies $|\eta|\le|x|+1\le\rho$; hence $\{|x|\le\rho-1\}\subseteq\bigcup_{|\eta|\le\rho}Q_\eta$, and comparing volumes (the volume of the unit ball in $\mathbb R^4$ is $\tfrac{\pi^2}2$),
> $$\tfrac{\pi^2}2(\rho-1)^4=\operatorname{vol}\{|x|\le\rho-1\}\le\#\{|\eta|\le\rho\}\cdot1\qquad(\text{disjoint unit cubes cover the ball}).$$
> *Upper count.* If $|\eta|\le\rho$ then $Q_\eta\subseteq\{|x|\le\rho+1\}$, so $\bigcup_{|\eta|\le\rho}Q_\eta\subseteq\{|x|\le\rho+1\}$ and $\#\{|\eta|\le\rho\}\le\operatorname{vol}\{|x|\le\rho+1\}=\tfrac{\pi^2}2(\rho+1)^4$.
>
> *Dyadic shell.* For $j\ge3$ (so $2^j\ge8$),
> $$\#A_j=\#\{|\eta|<2^{j+1}\}-\#\{|\eta|<2^j\}\ge\#\{|\eta|\le 2^{j+1}-1\}-\#\{|\eta|\le2^j\}\ge\tfrac{\pi^2}2\big((2^{j+1}-2)^4-(2^j+1)^4\big).$$
> Since $2^{j+1}-2=2(2^j-1)\ge2\cdot\tfrac78 2^j=\tfrac74 2^j$ and $2^j+1\le\tfrac98 2^j$ (both using $2^j\ge8$),
> $$(2^{j+1}-2)^4-(2^j+1)^4\ge\Big(\big(\tfrac74\big)^4-\big(\tfrac98\big)^4\Big)16^{j}\ge(9.38-1.61)\,16^j\ge7\cdot16^{j},$$
> so $\#A_j\ge\tfrac{\pi^2}2\cdot7\cdot16^j\ge3\pi^2\,16^{j}$, as claimed. (The constants are deliberately crude; only the growth rate $16^j$ matters.)

**Step B: $u\in H_2(T^4)$.**

The weighted coefficient sum $\lVert u\rVert_2^2=\sum_\xi\langle\xi\rangle^4|\hat u(\xi)|^2$ converges.

> [!note]- Derivation
> With $\hat u(\xi)=\langle\xi\rangle^{-4}\ell(\xi)^{-2/3}$,
> $$\lVert u\rVert_2^2=\sum_{\xi\in\mathbb Z^4}\langle\xi\rangle^4\,\langle\xi\rangle^{-8}\,\ell(\xi)^{-4/3}=\sum_{\xi\in\mathbb Z^4}\langle\xi\rangle^{-4}\,\ell(\xi)^{-4/3}.$$
> Group the lattice into dyadic shells $A_j$ ($j\ge0$), together with the finite set $\{|\xi|<1\}$ (which contributes a finite amount). On $A_j$ we have $\langle\xi\rangle^{-4}=(1+|\xi|^2)^{-2}\le(|\xi|^2)^{-2}\le(4^j)^{-2}=16^{-j}$ and $\ell(\xi)=\log(2+|\xi|)\ge\log(2+2^j)\ge j\log2$ (for $j\ge1$). Using also the upper count $\#A_j\le\#\{|\eta|\le2^{j+1}\}\le\tfrac{\pi^2}2(2^{j+1}+1)^4\le C_0\,16^{j}$,
> $$\sum_{\xi\in A_j}\langle\xi\rangle^{-4}\ell(\xi)^{-4/3}\le C_0\,16^{j}\cdot16^{-j}\cdot(j\log2)^{-4/3}=C_0(\log2)^{-4/3}\,j^{-4/3}\qquad(j\ge1).$$
> Therefore $\lVert u\rVert_2^2\le(\text{finite}) + C_1\sum_{j\ge1}j^{-4/3}<\infty$, since $\tfrac43>1$. Hence $u\in H_2(T^4)$; in particular $u\in H_0=L^2(T^4)$, so $u^2\in L^1(T^4)$ and $\widehat{u^2}=\hat u*\hat u$ with the convolution absolutely convergent (Cauchy–Schwarz, $\hat u\in\ell^2$).

**Step C: A lower bound on the low-frequency mass, $\sum_{|\eta|\le R}\hat u(\eta)\gtrsim(\log R)^{1/3}$.**

For $R\ge16$, $\displaystyle\sum_{\eta\in\mathbb Z^4,\ |\eta|\le R}\hat u(\eta)\ \ge\ c_1\,(\log R)^{1/3}$ for a constant $c_1>0$.

> [!note]- Derivation
> Sum over dyadic shells $A_j$ with $2^{j+1}\le R$, i.e. $3\le j\le J$ where $J:=\lfloor\log_2 R\rfloor-1$. On $A_j$,
> $$\hat u(\eta)=\langle\eta\rangle^{-4}\ell(\eta)^{-2/3}\ge\big(1+4^{j+1}\big)^{-2}\big(\log(2+2^{j+1})\big)^{-2/3}\ge\big(2\cdot4^{j+1}\big)^{-2}\big((j+2)\log2\big)^{-2/3}$$
> using $1+4^{j+1}\le2\cdot4^{j+1}$ and $2+2^{j+1}\le2^{j+2}$ so $\log(2+2^{j+1})\le(j+2)\log2$. Thus $\hat u(\eta)\ge\tfrac1{4}16^{-(j+1)}(\log2)^{-2/3}(j+2)^{-2/3}$ on $A_j$. Multiplying by the shell count $\#A_j\ge3\pi^2 16^j$ (Step A),
> $$\sum_{\eta\in A_j}\hat u(\eta)\ge3\pi^2\,16^{j}\cdot\tfrac14\,16^{-(j+1)}(\log2)^{-2/3}(j+2)^{-2/3}=\frac{3\pi^2}{64}(\log2)^{-2/3}\,(j+2)^{-2/3}=:c_0\,(j+2)^{-2/3}.$$
> Summing over $3\le j\le J$ and comparing with an integral,
> $$\sum_{|\eta|\le R}\hat u(\eta)\ge c_0\sum_{j=3}^{J}(j+2)^{-2/3}\ge c_0\int_3^{J+1}(t+2)^{-2/3}\,dt=3c_0\big((J+3)^{1/3}-5^{1/3}\big)\ge c_1\,J^{1/3}\qquad(\text{integral comparison, }-\tfrac23>-1).$$
> Finally $J=\lfloor\log_2 R\rfloor-1\ge\tfrac12\log_2 R\ge c_2\log R$ for $R\ge16$, so $\sum_{|\eta|\le R}\hat u(\eta)\ge c_1'(\log R)^{1/3}$. (Note the exponent $1-\beta=1-\tfrac23=\tfrac13$ predicted by the strategy.)

**Step D: A lower bound on $\widehat{u^2}(\xi)$ for large $\xi$.**

For $|\xi|=R\ge16$, $\displaystyle\widehat{u^2}(\xi)\ \ge\ c_3\,R^{-4}\,(\log R)^{-1/3}$.

> [!note]- Derivation
> Because $\hat u\ge0$, restricting the convolution to $|\eta|\le R/2$ only decreases it:
> $$\widehat{u^2}(\xi)=\sum_{\eta\in\mathbb Z^4}\hat u(\xi-\eta)\hat u(\eta)\ \ge\ \sum_{|\eta|\le R/2}\hat u(\xi-\eta)\,\hat u(\eta)\qquad(\text{all terms non-negative}).$$
> On the range $|\eta|\le R/2$ we have $|\xi-\eta|\le|\xi|+|\eta|\le\tfrac32 R$, so $\langle\xi-\eta\rangle^2=1+|\xi-\eta|^2\le1+\tfrac94R^2\le3R^2$ (for $R\ge2$), and $\log(2+|\xi-\eta|)\le\log(2+\tfrac32R)\le\log((2+R)^2)=2\,\ell(\xi)\le4\log R$ (for $R\ge2$, using $2+\tfrac32R\le(2+R)^2$ and $2+R\le R^2$). Hence uniformly on the range,
> $$\hat u(\xi-\eta)=\langle\xi-\eta\rangle^{-4}\big(\log(2+|\xi-\eta|)\big)^{-2/3}\ge(3R^2)^{-2}(4\log R)^{-2/3}=\frac{1}{9\cdot4^{2/3}}\,R^{-4}(\log R)^{-2/3}\qquad(\text{the two bounds above}).$$
> Therefore, with Step C,
> $$\widehat{u^2}(\xi)\ge\frac{R^{-4}(\log R)^{-2/3}}{9\cdot4^{2/3}}\sum_{|\eta|\le R/2}\hat u(\eta)\ge\frac{R^{-4}(\log R)^{-2/3}}{9\cdot4^{2/3}}\cdot c_1'\big(\log(R/2)\big)^{1/3}\ge c_3\,R^{-4}(\log R)^{-1/3}$$
> for $R\ge16$, using $\log(R/2)\ge\tfrac12\log R$ for $R\ge4$ and absorbing constants into $c_3>0$.

**Step E: $\lVert u^2\rVert_2^2=\infty$, hence $u^2\notin H_2(T^4)$.**

The lower bound of Step D makes the weighted coefficient sum for $u^2$ diverge.

> [!note]- Derivation
> Using $\langle\xi\rangle^4\ge|\xi|^4=R^4$ and Step D, for the dyadic shells $A_j$ with $2^j\ge16$ (i.e. $j\ge4$),
> $$\lVert u^2\rVert_2^2=\sum_{\xi\in\mathbb Z^4}\langle\xi\rangle^4|\widehat{u^2}(\xi)|^2\ge\sum_{j\ge4}\sum_{\xi\in A_j}|\xi|^4\,\big(c_3|\xi|^{-4}(\log|\xi|)^{-1/3}\big)^2=c_3^2\sum_{j\ge4}\sum_{\xi\in A_j}|\xi|^{-4}(\log|\xi|)^{-2/3}.$$
> On $A_j$: $|\xi|^{-4}\ge(2^{j+1})^{-4}=16^{-(j+1)}$ and, since $-\tfrac23<0$, $(\log|\xi|)^{-2/3}\ge\big(\log2^{j+1}\big)^{-2/3}=((j+1)\log2)^{-2/3}$. With $\#A_j\ge3\pi^2 16^j$ (Step A),
> $$\sum_{\xi\in A_j}|\xi|^{-4}(\log|\xi|)^{-2/3}\ge3\pi^2\,16^{j}\cdot16^{-(j+1)}\cdot((j+1)\log2)^{-2/3}=\frac{3\pi^2}{16}(\log2)^{-2/3}\,(j+1)^{-2/3}=:c_4\,(j+1)^{-2/3}.$$
> Therefore
> $$\lVert u^2\rVert_2^2\ge c_3^2\,c_4\sum_{j\ge4}(j+1)^{-2/3}=+\infty\qquad(\text{the exponent }\tfrac23<1,\text{ so the series diverges}).$$
> Since $H_2(T^4)=\{f\in L^2(T^4):\sum_\xi\langle\xi\rangle^4|\hat f(\xi)|^2<\infty\}$ and $u^2\in L^1(T^4)$ has Fourier coefficients $\widehat{u^2}=\hat u*\hat u$ with $\sum_\xi\langle\xi\rangle^4|\widehat{u^2}(\xi)|^2=\infty$, the square $u^2$ is **not** an element of $H_2(T^4)$. Hence $H_2(T^4)$ is not closed under pointwise multiplication, so it is not an algebra: the strict threshold $2k>n$ of Part 2 cannot be weakened to $2k=n$. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** On $T^4$: (a) $\lVert uv\rVert_3\le16\Lambda^{1/2}\lVert u\rVert_3\lVert v\rVert_3$ with $\Lambda=\sum_{\xi\in\mathbb Z^4}(1+|\xi|^2)^{-3}<\infty$, so $H_3(T^4)$ is a Banach algebra after renorming; (b) $H_2(T^4)$ is not an algebra.
>
> **(a)** By the [[Thm - Convergence of the Lattice Sum|lattice-sum theorem]], $\Lambda<\infty$ because $2\cdot3=6>4$. For $u,v\in C^\infty(T^4)$ write $\widehat{uv}=\hat u*\hat v$. From $\langle\xi\rangle^2\le2(\langle\xi-\eta\rangle^2+\langle\eta\rangle^2)\le4\max(\langle\xi-\eta\rangle^2,\langle\eta\rangle^2)$ one gets $\langle\xi\rangle^3\le8(\langle\xi-\eta\rangle^3+\langle\eta\rangle^3)$. Hence $\langle\xi\rangle^3|\widehat{uv}(\xi)|\le8(S_1(\xi)+S_2(\xi))$ with $S_1=a_1*b_1$, $a_1(\zeta)=\langle\zeta\rangle^3|\hat u(\zeta)|$, $b_1=|\hat v|$, and $S_2=a_2*b_2$ symmetrically. By Cauchy–Schwarz, $\lVert|\hat v|\rVert_{\ell^1}\le\Lambda^{1/2}\lVert v\rVert_3$ and $\lVert|\hat u|\rVert_{\ell^1}\le\Lambda^{1/2}\lVert u\rVert_3$; and $\lVert a_1\rVert_{\ell^2}=\lVert u\rVert_3$, $\lVert b_2\rVert_{\ell^2}=\lVert v\rVert_3$. By Young ($\lVert a*b\rVert_{\ell^2}\le\lVert a\rVert_{\ell^2}\lVert b\rVert_{\ell^1}$), $\lVert S_1\rVert_{\ell^2},\lVert S_2\rVert_{\ell^2}\le\Lambda^{1/2}\lVert u\rVert_3\lVert v\rVert_3$, so $\lVert uv\rVert_3\le8(\lVert S_1\rVert+\lVert S_2\rVert)_{\ell^2}\le16\Lambda^{1/2}\lVert u\rVert_3\lVert v\rVert_3$. Density of $C^\infty$ in $H_3$ extends this; $\lVert\cdot\rVert':=16\Lambda^{1/2}\lVert\cdot\rVert_3$ is submultiplicative.
>
> **(b)** Let $\hat u(\xi)=(1+|\xi|^2)^{-2}(\log(2+|\xi|))^{-2/3}\ge0$ (even, so $u$ real). Then $\lVert u\rVert_2^2=\sum\langle\xi\rangle^{-4}(\log(2+|\xi|))^{-4/3}<\infty$ by dyadic-shell comparison with $\sum_j j^{-4/3}$, so $u\in H_2\subset L^2$ and $\widehat{u^2}=\hat u*\hat u$. Using the cube-packing counts $\#\{|\eta|\le\rho\}\ge\tfrac{\pi^2}2(\rho-1)^4$ (so $\#A_j\ge3\pi^2 16^j$ on dyadic shells for $j\ge3$), one gets $\sum_{|\eta|\le R/2}\hat u(\eta)\ge c(\log R)^{1/3}$; restricting the positive convolution $\widehat{u^2}(\xi)\ge\sum_{|\eta|\le R/2}\hat u(\xi-\eta)\hat u(\eta)$ and bounding $\hat u(\xi-\eta)\ge c'R^{-4}(\log R)^{-2/3}$ on that range gives $\widehat{u^2}(\xi)\ge c_3R^{-4}(\log R)^{-1/3}$ for $|\xi|=R\ge16$. Then $\lVert u^2\rVert_2^2\ge c_3^2\sum_{|\xi|\ge16}|\xi|^{-4}(\log|\xi|)^{-2/3}\ge c_4\sum_j (j+1)^{-2/3}=\infty$. So $u^2\notin H_2(T^4)$, and $H_2(T^4)$ is not an algebra. $\blacksquare$

> [!warning] Illegal but tempting: "unbounded implies not-an-algebra"
> A shorter-looking route is: "the companion exercise [[Ex - An Unbounded Function in W-1-2 of the Two-Torus]] scaled up gives an unbounded $u\in H_2(T^4)$; an unbounded function cannot generate an algebra, contradiction." This is **not** a proof. Unboundedness of $u$ does not by itself imply $u^2\notin H_2$: membership in $H_2$ is a statement about $L^2$-control of two derivatives, not about pointwise boundedness, and there exist unbounded functions whose squares are perfectly regular. The honest obstruction is the *logarithmic accumulation* in the self-convolution $\widehat{u^2}=\hat u*\hat u$ at the critical decay rate, which is exactly what Steps C–E compute. The correct relationship to the companion exercise is *analogy of mechanism*, not implication: both live at the critical index $2k=n$ (there $k=1,n=2$; here $k=2,n=4$), and in both the borderline lattice sum $\sum\langle\xi\rangle^{-n}$ diverges logarithmically — that shared divergence is what breaks the $C^0$ embedding there and the algebra property here. To use the companion result legitimately one would still have to run an argument like Steps C–E; there is no shortcut through "unbounded".
>
> **Independent sanity check on the exponent window.** With $\hat u(\xi)=\langle\xi\rangle^{-4}\ell(\xi)^{-\beta}$: the shell sum for $\lVert u\rVert_2^2$ is $\sum_j j^{-2\beta}$, finite iff $2\beta>1$; the shell sum forcing $\lVert u^2\rVert_2^2=\infty$ is $\sum_j j^{-(4\beta-2)}$, divergent iff $4\beta-2\le1$, i.e. $\beta\le\tfrac34$. The admissible window is $\tfrac12<\beta\le\tfrac34$, and our choice $\beta=\tfrac23$ sits strictly inside it ($2\beta=\tfrac43>1$ and $4\beta-2=\tfrac23<1$), so both the membership and the divergence hold with room to spare. Had we naively taken $\beta=1$ (the shape the spec suggests as a *type*), one would find $4\beta-2=2>1$ and the square would in fact land back in $H_2$ — the reason the fractional exponent is not cosmetic.

---

# Key Takeaways

**Whether a Sobolev space is an algebra is decided by one lattice sum, and the threshold $2k>n$ is precisely its convergence.** The entire positive proof (Part 2) is elementary manipulation — Peetre's weight-splitting and Young's inequality — except for a single non-trivial input: that $\Lambda=\sum_{\xi\in\mathbb Z^n}\langle\xi\rangle^{-2k}$ is finite, which by the [[Thm - Convergence of the Lattice Sum|lattice-sum theorem]] happens exactly when $2k>n$. So "$H_k$ is a Banach algebra" and "$\sum\langle\xi\rangle^{-2k}<\infty$" are, in this proof, the same statement, and the constant $C=16\Lambda^{1/2}$ wears the sum on its sleeve. The transferable diagnostic: whenever you must bound the product of two functions in a norm defined by a frequency weight $w(\xi)$, the move is to split $w(\xi)\lesssim w(\xi-\eta)+w(\eta)$, apply $\ell^2*\ell^1\subseteq\ell^2$, and read off the surviving weight $\sum w(\eta)^{-1}$ as the quantity that must converge. This is the mechanism behind every "$H^s$ is an algebra for $s>n/2$" statement and behind the smoothness of the Seiberg–Witten map, where products of the spinor and connection fields must stay in the same Sobolev class for the equations to make sense.

**The borderline $2k=n$ fails, and the failure is a logarithmic accumulation in the self-convolution, not a pointwise pathology.** Part 3 is a lesson in how sharp thresholds actually break. Dropping from $2k>n$ to $2k=n$ turns the convergent sum $\Lambda$ into a divergent one, and the construction converts that divergence into a concrete function: a critically-decaying radial coefficient with a fractional-logarithmic correction sits *inside* $H_2$, but its low-frequency self-convolution $\widehat{u^2}(\xi)=\sum_\eta\hat u(\xi-\eta)\hat u(\eta)$ picks up a factor $(\log|\xi|)^{1/3}$ from summing $\hat u$ over the ball $|\eta|\le|\xi|/2$, and that extra logarithm is exactly enough to send $\lVert u^2\rVert_2$ to infinity. The trigger to recognise in the wild: at a *critical* Sobolev index, do not trust an algebra property; probe it with a radial coefficient carrying a $\log$ correction and compute the self-convolution's low-high interaction. The same $\log$-tuning technique produces the critical Sobolev embedding counterexamples, the borderline cases of the Gagliardo–Nirenberg inequalities, and the failure of $H^{n/2}\hookrightarrow L^\infty$.

**Keeping constants explicit is a discipline that exposes where a hypothesis is spent.** It would have been faster in Part 2 to invoke the multiplication theorem as a black box, but writing $C=16\Lambda^{1/2}$ forces the sum $\Lambda$ into the open, and once it is in the open the role of the numerology is unmissable: Step 0 is the *only* place $2\cdot3>4$ appears, and every other line is index-independent. This is why the exercise pairs the explicit constant with the sharpness construction — the same object, $\sum\langle\xi\rangle^{-2k}$, is finite in Part 2 (with $k=3$) and infinite in Part 3 (with $k=2$), and seeing it change status as $2k$ crosses $n=4$ is the whole point. When you return to this after months, reconstruct it from the single question "for which $k$ does $\sum_{\xi\in\mathbb Z^4}(1+|\xi|^2)^{-k}$ converge?" — the answer $k>2$, i.e. $2k>4=n$, regenerates both halves. The companion drill [[Ex - The Lattice Sum Converges iff 2t Exceeds n]] isolates that convergence criterion on its own, and [[Ex - An Unbounded Function in W-1-2 of the Two-Torus]] shows the same critical index breaking the $C^0$ embedding rather than the algebra property.
