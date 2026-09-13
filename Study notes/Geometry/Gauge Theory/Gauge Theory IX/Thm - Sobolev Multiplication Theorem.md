---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Sobolev Norms on the Torus via Fourier Coefficients"
  - "Thm - Convergence of the Lattice Sum"
  - "Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts"
  - "Thm - Sobolev Embedding Theorem"
  - "Thm - Fourier Series of Smooth Functions on the Torus"
  - "Thm - Cauchy-Schwarz Inequality"
tags: [geometry, gauge-theory, analysis, sobolev-spaces]
---

# Notation

Throughout, $M$ is a smooth compact $n$-manifold (Hausdorff, second countable), and all Sobolev spaces are the $L^2$-based integer-order spaces of the series: $H_k(M;E) = W^{k,2}(M;E)$ for a real vector bundle $E \to M$ and $k \in \mathbb{Z}$, built by completing the smooth sections $\Gamma(E)$ in the chart norm of [[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts|the charts theorem]]. When the bundle is the trivial real line bundle we write $H_k(M)$ and speak of Sobolev *functions*. We write $\lVert\cdot\rVert_k$ for the $H_k$ norm (any of the mutually equivalent chart norms; a fixed choice is understood on each page).

The torus is $T^n = \mathbb{R}^n/2\pi\mathbb{Z}^n$ with the flat metric and trivial connection. For $u \in C^\infty(T^n;\mathbb{C})$ the Fourier coefficients are
$$\hat{u}(\xi) = (2\pi)^{-n}\int_{T^n} u(x)\,e^{-i\langle\xi,x\rangle}\,dx, \qquad \xi \in \mathbb{Z}^n,$$
and, following [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order|the torus definition]], the integer-order norm is
$$\lVert u\rVert_k^2 = \sum_{\xi\in\mathbb{Z}^n}(1+\lvert\xi\rvert^2)^k\,\lvert\hat{u}(\xi)\rvert^2, \qquad H_k(T^n) = W^{k,2}(T^n) \text{ with equivalent norms (charts theorem, part (i))}.$$
It is convenient to abbreviate the **Japanese bracket** $\langle\xi\rangle := (1+\lvert\xi\rvert^2)^{1/2} \ge 1$, so that $\lVert u\rVert_k^2 = \sum_\xi \langle\xi\rangle^{2k}\lvert\hat{u}(\xi)\rvert^2$; the $H_k$ norm is exactly the weighted $\ell^2$ norm of the coefficient sequence with weight $\langle\xi\rangle^{2k}$.

For sequences $a,b : \mathbb{Z}^n \to \mathbb{C}$ we write $\lVert a\rVert_{\ell^2}^2 = \sum_\xi\lvert a(\xi)\rvert^2$, $\lVert a\rVert_{\ell^1} = \sum_\xi\lvert a(\xi)\rvert$, and the (discrete) convolution
$$(a*b)(\xi) = \sum_{\eta\in\mathbb{Z}^n} a(\xi-\eta)\,b(\eta).$$
The $L^2$ pairing on $M$ is $(u,v)_{L^2} = \int_M \langle u,v\rangle_E\,\mathrm{vol}$ (fibre inner product integrated against the Riemannian volume form); for the trivial line bundle and real-valued functions this is $(u,v)_{L^2} = \int_M uv\,\mathrm{vol}$. Its extension to a perfect pairing $H_k(M;E)\times H_{-k}(M;E)\to\mathbb{R}$ is part (iv) of [[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts|the charts theorem]].

**Standing method.** Every estimate below is first proved for *smooth* sections, where the pointwise product is an ordinary smooth section and every series converges absolutely, and then extended to the completed Sobolev spaces by density and continuity (Lemma 4). This is the standing method of the chapter (group decision 2): all Sobolev estimates are $L^2$-based and are established on $\Gamma(E)$, then transported.

> [!warning] Convention: the general-$p$ statement is recorded, not proved
> Haydys's Theorem 136 (iv) is stated for $W^{k,p}(M;\mathbb{R})$ with any $p>1$: part (a), if $kp>n$ then $W^{k,p}(M;\mathbb{R})$ is an algebra; part (b), if $kp<n$ there is a bounded map $W^{k_1,p_1}\otimes W^{k_2,p_2}\to W^{k,p}$ provided $k_1-\tfrac{n}{p_1}+k_2-\tfrac{n}{p_2}\ge k-\tfrac np$. A complete proof of the general-$p$ multiplication and algebra statements is in M. E. Taylor, *Partial Differential Equations III*, §13.3 (Proposition 3.7 and its corollaries), and in R. Palais, *Foundations of Global Non-Linear Analysis*, §9. The series proves and uses only the case $p=2$, stated below; setting $p_1=p_2=p=2$ in Haydys's (iv)(b) recovers the exponent count $k_1+k_2-k\ge n/2$, which our part (b) sharpens to a strict inequality with the missing side conditions supplied.

> [!warning] Convention: correcting the printed side conditions of Theorem 136 (iv)(b)
> As printed, Haydys's Theorem 136 (iv)(b) reads "if $kp<n$, the map $W^{k_1,p_1}\otimes W^{k_2,p_2}\to W^{k,p}$ is bounded provided $k_1-\tfrac{n}{p_1}+k_2-\tfrac{n}{p_2}\ge k-\tfrac np$." Two hypotheses that the statement needs are missing (this is the item recorded in Appendix B of the content map): the target order may not exceed either source order, $k\le\min(k_1,k_2)$, and in the Hölder-critical borderline the inequality must be **strict**. Without $k\le\min(k_1,k_2)$ the claim is false — one cannot manufacture derivatives that neither factor has — and without strictness the endpoint fails, exactly as the endpoint $2k=n$ fails for the embedding into $C^0$ (see [[Ex - An Unbounded Function in W-1-2 of the Two-Torus]]). The corrected $L^2$ statement, proved in full below, is part (b): integers $k_1,k_2\ge k\ge0$ (so $k\le\min(k_1,k_2)$) with the *strict* inequality $k_1+k_2-k>\tfrac n2$. We adopt the corrected form.

---

# Statement

> **Theorem (Sobolev multiplication theorem).** Let $M$ be a compact $n$-manifold. Then pointwise multiplication of smooth sections extends to bounded bilinear maps of Sobolev spaces in each of the following regimes, with a constant $C$ depending only on $M$, the chosen norms, and the indices displayed.
>
> **(a) (Algebra property.)** If $2k>n$, then multiplication extends to a bounded bilinear map
> $$H_k(M) \times H_k(M) \longrightarrow H_k(M), \qquad \lVert uv\rVert_k \le C\,\lVert u\rVert_k\,\lVert v\rVert_k .$$
> Consequently $H_k(M)$, with the equivalent norm $\lVert\cdot\rVert_k' := C\lVert\cdot\rVert_k$, is a commutative unital Banach algebra (unit the constant function $1$).
>
> **(b) (Mixed orders and bundle-valued products.)** For integers $k_1,k_2\ge k\ge 0$ with the strict inequality
> $$k_1 + k_2 - k > \tfrac n2,$$
> multiplication extends to a bounded bilinear map $H_{k_1}(M)\times H_{k_2}(M)\to H_k(M)$, $\lVert uv\rVert_k\le C\lVert u\rVert_{k_1}\lVert v\rVert_{k_2}$. More generally, for any smooth bilinear bundle map $\beta : E_1\otimes E_2 \to E_3$ over $M$, the induced fibrewise product extends to a bounded bilinear map
> $$H_{k_1}(M;E_1) \times H_{k_2}(M;E_2) \longrightarrow H_k(M;E_3), \qquad \lVert \beta(u,v)\rVert_k \le C\,\lVert u\rVert_{k_1}\,\lVert v\rVert_{k_2}.$$
>
> **(c) (Multiplier property on the full scale.)** If $2k>n$, then for every integer $m$ with $\lvert m\rvert\le k$, multiplication by a fixed $H_k$ function is bounded on $H_m$: for $u\in H_k(M)$ and $v\in H_m(M)$ (real-valued),
> $$\lVert uv\rVert_m \le C\,\lVert u\rVert_k\,\lVert v\rVert_m .$$

The three parts are one phenomenon at three settings of the dials. Part (a) is the diagonal case $k_1=k_2=k$ of part (b): the hypothesis $2k>n$ is exactly $k_1+k_2-k = k > n/2$, and $k_1=k_2=k\ge k$ holds trivially, so (a) will be read off from (b). Part (c) extends the reach of an $H_k$ multiplier from the algebra $H_k$ down (and, by duality, up) the whole scale $H_m$, $\lvert m\rvert\le k$: for $m\ge0$ it is again an instance of (b), and for $m<0$ it is the transpose of the positive case across the perfect pairing. We record the one specialisation the four-manifold theory needs.

> **Corollary 1 (the Seiberg–Witten algebra).** Let $M$ be a compact $4$-manifold. Then $H_k(M)$ is a Banach algebra for every integer $k\ge 3$, and in particular $H_3(M)$ is; the borderline space $H_2(M)$ is **not** an algebra. In the notation of the source, $W^{k,2}(M^4)$ is an algebra for $k\ge3$.

The tie between the corollary and the theorem is the numerology $2k>n$ with $n=4$: this reads $k>2$, that is $k\ge3$ for integers, so part (a) applies exactly to $k\ge3$; at $k=2$ one has $2k=4=n$, the strict inequality fails, and $H_2(M^4)$ is genuinely not an algebra (proved in Step 7 below and drilled in [[Ex - W-3-2 is an Algebra in Dimension Four]]).

---

# Motivation

The question this theorem answers is blunt and practical: **if $u$ and $v$ are only as regular as their membership in a Sobolev space guarantees, is the pointwise product $uv$ a section of any Sobolev space at all, and if so which one?** For smooth sections the product is smooth and there is nothing to ask. But the whole reason Sobolev spaces were introduced — Dirichlet's principle, recalled on [[Def - Sobolev Space of Sections|the Sobolev definition page]] — is that the natural function spaces of geometry and analysis are *not* the smooth sections but their completions, and in a completion an element is a limit of smooth sections whose derivatives up to a fixed order are controlled in $L^2$ and nothing more. Multiplication is not continuous on $L^2$ (the product of two square-integrable functions need not be integrable), so the question has real content.

The gauge theory of the later chapters cannot proceed without an answer. The configuration space of Seiberg–Witten theory is built from Sobolev connections and Sobolev spinors, and the Seiberg–Witten map involves the quadratic term $\mu(\psi)$, the Clifford product $a\cdot\psi$ of a Sobolev $1$-form with a Sobolev spinor, and the gauge action $g^{-1}\nabla g$ — every one of these is a *pointwise product of two Sobolev sections*. For the map to be well defined between Banach spaces, and for the gauge group $\mathcal{G}^{k,2} = H_k(M;S^1)$ to be a topological group, one needs precisely that products of Sobolev sections land in Sobolev spaces with controlled norm. The multiplication theorem is the analytic licence for all of it.

The mechanism is best seen against the alternative that fails. One might hope to bound $\lVert uv\rVert_{L^2}$ by $\lVert u\rVert_{L^2}\lVert v\rVert_{L^2}$; this is false, because $L^2$ functions can be simultaneously large on the same small set. What rescues multiplication is *surplus regularity*. If $u$ and $v$ each have enough $L^2$-derivatives that the [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]] — for integers $k$ with $k-\tfrac n2>0$ the inclusion $H_k(M)\hookrightarrow C^0(M)$ is continuous — already forces them to be continuous, then the product is at least continuous and the only question is how many derivatives it keeps. The theorem says: **the product keeps the smaller of the two regularities, and the excess regularity $k_1+k_2-k$ beyond the target is what must pay the dimensional toll $n/2$.** Continuity of the factors ($2k_i>n$) is the sufficient-but-not-necessary caricature; the sharp statement (b) trades regularity between the factors, requiring only that their *combined* surplus over the target exceed $n/2$.

We assume the reader is at home with the Fourier description of Sobolev spaces on the torus — that $H_k$ norms are weighted $\ell^2$ norms of coefficient sequences, that differentiation is multiplication by $i\xi$, and that a compact manifold is finitely many pieces of a torus glued by smooth maps ([[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts|the charts theorem]]). The entire proof reduces, through that page, to an estimate about convolution of sequences on the lattice $\mathbb{Z}^n$.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of part (b) is a pair of Sobolev sections with a combined surplus $k_1+k_2-k>n/2$ over the target order. The skill is to recognise the many situations that hand you exactly this.

The first disguised source is **a factor that is smooth, or lies in $H_\ell$ for every $\ell$**. A smooth coefficient $\gamma$ — the components of a bilinear bundle map $\beta$ in a trivialisation, the coefficients of a differential operator, a fixed background field — belongs to $H_\ell(M)$ for every $\ell$, so multiplication by $\gamma$ meets the hypothesis of (b) with the free index $\ell$ taken as large as one likes: with target order $k$ and the smooth factor assigned order $k_1=\ell$, the surplus $\ell + k - k = \ell$ exceeds $n/2$ for $\ell$ large. Thus "multiply by a smooth thing" is always legal on every $H_k$, and this is why bundle-valued products reduce to scalar ones. *Example problem:* show that if $L$ is a differential operator of order $\ell$ with smooth coefficients on a compact $M$, then $L$ maps $H_{k+\ell}(M;E)$ boundedly into $H_k(M;F)$ — the coefficients are the smooth multipliers and the derivatives cost the orders, which is exactly [[Thm - Differential Operators are Bounded between Sobolev Spaces|the boundedness of differential operators]].

The second disguised source is **a factor known to be continuous by embedding**. If $2k_1>n$ then $u\in H_{k_1}(M)$ is continuous, so $\lVert u\rVert_{C^0}\le C\lVert u\rVert_{k_1}$; but the sharper input is that (b) then holds with target equal to the *other* factor's order, $k=k_2\le k_1$, because the surplus is $k_1+k_2-k_2 = k_1>n/2$. Recognising that a single factor above the embedding threshold already makes multiplication bounded on the scale up to its own order is the content of part (c). *Example problem:* on a compact $4$-manifold with $u\in H_3(M)$ (so $2\cdot3>4$, $u$ continuous), show $v\mapsto uv$ is bounded on $H_m(M)$ for every $\lvert m\rvert\le3$, which is precisely (c) and underlies the smoothness of the gauge action.

The third disguised source is **a quadratic or polynomial nonlinearity in a single Sobolev section above threshold**. If $2k>n$ and $u\in H_k(M)$, then $u^2, u^3, \dots$ and any convergent power series $f(u)$ lie in $H_k$, because $H_k$ is an algebra by (a). A nonlinearity that at first sight throws you out of the space in fact keeps you in it. *Example problem:* show that for $2k>n$ and $u\in H_k(M;\mathbb{R})$ the exponential $e^{iu}$ lies in $H_k(M;\mathbb{C})$ with $\lvert e^{iu}\rvert\equiv1$ — the algebra bound makes the power series $\sum (iu)^j/j!$ converge in $H_k$, which is [[Thm - Composition with Analytic Functions on the Sobolev Algebra|composition with analytic functions]] and the first step in giving $\mathcal{G}^{k}=H_k(M;S^1)$ a Banach-Lie-group structure.

**Targets (Output Amplification)**

The bare conclusion is a bound $\lVert uv\rVert_k\le C\lVert u\rVert_{k_1}\lVert v\rVert_{k_2}$. Combined with other facts it does the heavy lifting of the four-manifold theory.

Combine the algebra property (a) with **the exponential and the classification of $S^1$-valued maps**. Once $H_k(M)$ is a Banach algebra for $2k>n$, the entire functional calculus of entire functions is available in it, so $\mathcal{G}^{k} = \{g\in H_k(M;\mathbb{C}) : \lvert g\rvert\equiv1\}$ is a group under pointwise multiplication (the inverse of $g$ is $\bar g = g^{-1}$, again in $H_k$), and in fact a Banach Lie group modelled on $H_k(M;\mathbb{R})$. The extra ingredient is the smoothness of $u\mapsto e^{iu}$; the payoff is that the Sobolev gauge group of Chapter XI is a genuine Lie group acting smoothly on the Sobolev configuration space.

Combine the mixed bound (b) with **the mapping properties of an elliptic operator** to bootstrap regularity. In the Seiberg–Witten equations the nonlinear terms $a\cdot\psi$ and $\mu(\psi)$ are products handled by (b); once a solution is known to lie in some $H_k$ with $k$ above threshold, (b) places the nonlinearity in a space to which [[Thm - Elliptic Regularity and the Elliptic Estimate|elliptic regularity]] applies, raising $k$ by the order of the operator, and the loop repeats. The extra ingredient is the elliptic estimate; the payoff is that Sobolev solutions of the Seiberg–Witten equations are automatically smooth.

Combine (b) with **[[Thm - Rellich Compactness Theorem|Rellich compactness]]** in the compactness proof for the moduli space. A sequence of solutions bounded in a high $H_k$ has, by Rellich, a subsequence converging in a lower $H_m$; the multiplication theorem then controls the nonlinear terms along the subsequence (products of the convergent factors converge, because multiplication is continuous by (b)), so the limit again solves the equations. The extra ingredient is the compact embedding; the payoff is the compactness of the Seiberg–Witten moduli space that makes its signed count a well-defined invariant.

---

# Why Is It True

Forget the manifold and look at the torus, where a Sobolev norm is literally a weighted $\ell^2$ norm of Fourier coefficients and multiplication of functions is convolution of coefficients: $\widehat{uv} = \hat u * \hat v$. The whole theorem is a statement about how convolution interacts with the weight $\langle\xi\rangle^{2k} = (1+\lvert\xi\rvert^2)^k$.

Here is the mechanism in the cleanest case, where both factors are above the embedding threshold ($2k_1>n$ and $2k_2>n$). A function whose $H_{k_i}$ norm is finite has coefficients that decay fast enough to be *absolutely summable*: $\sum_\eta\lvert\hat u(\eta)\rvert<\infty$, by Cauchy–Schwarz against the weight $\langle\eta\rangle^{-k_i}$, whose square is summable exactly when $2k_i>n$ (this is the convergence dichotomy of [[Thm - Convergence of the Lattice Sum|the lattice-sum theorem]], that the weighted lattice sum converges precisely when twice the exponent exceeds the dimension). Absolute summability of the coefficients is the Fourier face of continuity. Now to bound $\langle\xi\rangle^k\lvert\widehat{uv}(\xi)\rvert$ one uses that the weight of a sum cannot be much bigger than the largest weight of the summands — $\langle\xi\rangle\le 2\max(\langle\xi-\eta\rangle,\langle\eta\rangle)$ — so the weight $\langle\xi\rangle^k$ lands on whichever of the two frequencies $\xi-\eta$ or $\eta$ is larger. That turns the weighted convolution into an ordinary convolution of an $\ell^2$ sequence (the weighted coefficients of one factor) with an $\ell^1$ sequence (the summable coefficients of the other), and convolution of $\ell^2$ with $\ell^1$ stays in $\ell^2$ with the product of the norms. The product therefore has finite $H_k$ norm.

> **The mechanism in one sentence: convolution smears the frequency mass, and the weight of the output frequency is carried by the larger input frequency, so the product inherits the smaller regularity provided the surplus $k_1+k_2-k$ over the target exceeds the dimensional threshold $n/2$ needed to make the leftover weight summable.**

The sharp statement (b) refines only the accounting. When neither factor is separately above threshold, one cannot afford to throw *all* the target weight onto one factor and ask the *other* to be summable on its own; instead one splits the leftover weight $k_1+k_2-k$ across the two factors according to which frequency is larger. On the region where $\eta$ is the smaller frequency the surplus attaches to $\eta$ and one asks $\sum_\eta\langle\eta\rangle^{-2(k_1+k_2-k)}<\infty$; on the complementary region it attaches to $\xi-\eta$ and one asks the same of that variable. Either way the summability condition is $2(k_1+k_2-k)>n$ — the hypothesis, verbatim, of the lattice sum. The dimension enters in exactly one place: whether the leftover weight is summable over the lattice.

---

# What Makes This Hard

The non-obvious step is the *weight-splitting inequality* $\langle\xi\rangle^k\le 2^k(\langle\xi-\eta\rangle^k+\langle\eta\rangle^k)$ together with the decision of how to distribute the surplus regularity $k_1+k_2-k$ between the two frequencies — done wrongly, one is left demanding that a single factor be above threshold and the sharp range of (b) is lost. The common error is to try to bound $\lVert uv\rVert_k$ by controlling $u$ and $v$ each in $H_k$ and hoping convolution behaves like multiplication of norms; it does not, because $\ell^2*\ell^2$ is not contained in $\ell^2$, and the correct pairing is $\ell^2 * \ell^1 \subset \ell^2$, which forces one factor's coefficients to be genuinely summable and hence forces the appearance of the dimensional threshold. A second trap is the endpoint: the estimate is false at $k_1+k_2-k = n/2$, so the strict inequality (missing from the printed source) is not a convenience but a necessity — the same failure that makes $H_{n/2}$ miss $C^0$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce to the torus through the charts theorem, where $H_k$ norms are weighted $\ell^2$ norms and multiplication is convolution. On the torus, dominate the target weight $\langle\xi\rangle^k$ by the larger of the two input weights, split the frequency lattice into the two regions "$\eta$ smaller" and "$\eta$ larger", place the full surplus $k_1+k_2-k$ on the smaller frequency in each region, and finish with Young's inequality $\ell^2*\ell^1\subset\ell^2$ and the lattice-sum convergence $\sum\langle\cdot\rangle^{-2(k_1+k_2-k)}<\infty$. Read off (a) as the diagonal case, get (c) for $m\ge0$ from (b) and for $m<0$ by duality across the perfect pairing, and globalise to $M$ by a partition of unity, extending everything from smooth sections by density.

**Subgoal decomposition:**

1. **Convolution of coefficients.** For smooth $u,v$ on $T^n$, establish $\widehat{uv}(\xi)=\sum_\eta\hat u(\xi-\eta)\hat v(\eta)$ with the series absolutely convergent.
   - *Hint:* Substitute the absolutely and uniformly convergent Fourier series (from the Fourier page) into the coefficient integral and integrate term by term.
   - *Why needed:* It is the sole translation of "multiply functions" into "convolve sequences".

2. **Weight splitting.** Prove $\langle\xi\rangle^k\le 2^k(\langle\xi-\eta\rangle^k+\langle\eta\rangle^k)$ for $k\ge0$, and the monotonicity that lets the surplus move to the smaller frequency.
   - *Hint:* $\lvert\xi\rvert\le 2\max(\lvert\xi-\eta\rvert,\lvert\eta\rvert)$ from the triangle inequality; then $\langle\xi\rangle\le2\max(\langle\xi-\eta\rangle,\langle\eta\rangle)$.
   - *Why needed:* It relocates the output weight onto an input frequency.

3. **Young for sequences.** Prove $\lVert a*b\rVert_{\ell^2}\le\lVert a\rVert_{\ell^2}\lVert b\rVert_{\ell^1}$.
   - *Hint:* Write $a*b = \sum_\eta b(\eta)\,\tau_\eta a$ (translates) and apply the triangle inequality in $\ell^2$.
   - *Why needed:* It is the one inequality that makes the convolution estimate close.

4. **Summable weight.** Prove that for $t>n/2$ and $b\in\ell^2$, the sequence $\langle\cdot\rangle^{-t}b$ is in $\ell^1$ with $\ell^1$ norm $\le (\sum\langle\eta\rangle^{-2t})^{1/2}\lVert b\rVert_{\ell^2}$.
   - *Hint:* Cauchy–Schwarz, then the lattice-sum theorem for the finiteness of $\sum\langle\eta\rangle^{-2t}$.
   - *Why needed:* This is where the dimensional threshold $k_1+k_2-k>n/2$ is spent.

5. **Assemble the torus estimate (b).** Combine 1–4 over the two regions.
   - *Hint:* On $\{\lvert\eta\rvert\le\lvert\xi-\eta\rvert\}$ the surplus goes to $\eta$; on the complement to $\xi-\eta$; each region is a convolution of an $\ell^2$ and an $\ell^1$ sequence.
   - *Why needed:* It is the theorem on the torus.

6. **Diagonal, multiplier, globalise, extend.** Read off (a); get (c) via duality; globalise by partition of unity; extend from smooth sections by density (Lemma 4).
   - *Hint:* $k_1=k_2=k$ for (a); $\langle uv,\phi\rangle = \langle v,u\phi\rangle$ for the $m<0$ case of (c).
   - *Why needed:* It delivers the stated theorem on $M$ in all three parts.

---

# Lemma Decomposition

> [!note]- Lemma 1: Weight-splitting inequality and surplus transfer
> **Statement:** Let $k\ge0$. For all $\xi,\eta\in\mathbb{Z}^n$,
> $$\langle\xi\rangle^k \le 2^k\big(\langle\xi-\eta\rangle^k + \langle\eta\rangle^k\big), \qquad \langle\xi\rangle := (1+\lvert\xi\rvert^2)^{1/2}.$$
> More precisely, $\langle\xi\rangle\le 2\langle\xi-\eta\rangle$ whenever $\lvert\eta\rvert\le\lvert\xi-\eta\rvert$, and $\langle\xi\rangle\le2\langle\eta\rangle$ whenever $\lvert\eta\rvert\ge\lvert\xi-\eta\rvert$. Finally, for any real $s\le0$: if $\langle\eta\rangle\le\langle\zeta\rangle$ then $\langle\zeta\rangle^s\le\langle\eta\rangle^s$.
>
> **Hint:** Use $\lvert\xi\rvert\le\lvert\xi-\eta\rvert+\lvert\eta\rvert\le 2\max(\lvert\xi-\eta\rvert,\lvert\eta\rvert)$ and that $t\mapsto t^s$ is nonincreasing on $[1,\infty)$ for $s\le0$.
>
> **Why needed:** It moves the output weight $\langle\xi\rangle^k$ onto whichever input frequency is larger, and lets the (nonpositive) surplus exponent be transferred to the smaller frequency in each region of the frequency lattice.
>
> > [!note]- Full proof
> > **Setup.** Write $\zeta := \xi-\eta$, so $\xi = \zeta+\eta$ and $\lvert\xi\rvert\le\lvert\zeta\rvert+\lvert\eta\rvert$ by the triangle inequality in $\mathbb{R}^n$. Hence $\lvert\xi\rvert\le 2\max(\lvert\zeta\rvert,\lvert\eta\rvert)$, because the sum of two nonnegative numbers is at most twice their maximum.
> >
> > **The two one-sided bounds.** Suppose first $\lvert\eta\rvert\le\lvert\zeta\rvert$, so $\max(\lvert\zeta\rvert,\lvert\eta\rvert)=\lvert\zeta\rvert$ and $\lvert\xi\rvert\le2\lvert\zeta\rvert$, giving $\lvert\xi\rvert^2\le4\lvert\zeta\rvert^2$. Then
> > $$\langle\xi\rangle^2 = 1+\lvert\xi\rvert^2 \le 1 + 4\lvert\zeta\rvert^2 \le 4(1+\lvert\zeta\rvert^2) = 4\langle\zeta\rangle^2 \qquad(\text{since } 1\le 4),$$
> > so $\langle\xi\rangle\le 2\langle\zeta\rangle$ (both sides nonnegative). Symmetrically, if $\lvert\eta\rvert\ge\lvert\zeta\rvert$ then $\langle\xi\rangle\le2\langle\eta\rangle$. These are the two displayed one-sided bounds.
> >
> > **The additive form.** In either case $\langle\xi\rangle\le 2\max(\langle\zeta\rangle,\langle\eta\rangle)$. Raising to the power $k\ge0$ (the map $t\mapsto t^k$ is nondecreasing on $[0,\infty)$),
> > $$\langle\xi\rangle^k \le 2^k\max(\langle\zeta\rangle,\langle\eta\rangle)^k = 2^k\max(\langle\zeta\rangle^k,\langle\eta\rangle^k) \le 2^k\big(\langle\zeta\rangle^k+\langle\eta\rangle^k\big),$$
> > the last step because a maximum of two nonnegative numbers is at most their sum. This is the claimed inequality with $\zeta=\xi-\eta$.
> >
> > **Monotonicity of nonpositive powers.** Let $s\le0$ and suppose $1\le\langle\eta\rangle\le\langle\zeta\rangle$. Writing $s=-\lvert s\rvert$, the function $t\mapsto t^{-\lvert s\rvert} = 1/t^{\lvert s\rvert}$ is nonincreasing on $[1,\infty)$ because $t^{\lvert s\rvert}$ is nondecreasing there; hence $\langle\zeta\rangle^{s}\le\langle\eta\rangle^{s}$. This is the surplus-transfer statement. $\blacksquare$

> [!note]- Lemma 2: Young's inequality for sequences ($\ell^2*\ell^1\subset\ell^2$)
> **Statement:** For sequences $a\in\ell^2(\mathbb{Z}^n)$ and $b\in\ell^1(\mathbb{Z}^n)$, the convolution $(a*b)(\xi)=\sum_\eta a(\xi-\eta)b(\eta)$ is defined for every $\xi$, belongs to $\ell^2(\mathbb{Z}^n)$, and
> $$\lVert a*b\rVert_{\ell^2}\le \lVert a\rVert_{\ell^2}\,\lVert b\rVert_{\ell^1}.$$
>
> **Hint:** View $a*b$ as the $\ell^2$-valued sum $\sum_\eta b(\eta)\,\tau_\eta a$ of translates $\tau_\eta a(\xi):=a(\xi-\eta)$, and apply the triangle inequality in $\ell^2$ together with the translation invariance $\lVert\tau_\eta a\rVert_{\ell^2}=\lVert a\rVert_{\ell^2}$.
>
> **Why needed:** It is the exact inequality that closes the convolution estimate; it forces one factor to be summable (in $\ell^1$), which is where the dimensional threshold is spent through Lemma 3.
>
> > [!note]- Full proof
> > **Reduction to nonnegative sequences.** Since $\lvert(a*b)(\xi)\rvert\le\sum_\eta\lvert a(\xi-\eta)\rvert\,\lvert b(\eta)\rvert = (\lvert a\rvert*\lvert b\rvert)(\xi)$, it suffices to prove the bound for the nonnegative sequences $\lvert a\rvert,\lvert b\rvert$; we therefore assume $a,b\ge0$ and prove $\lVert a*b\rVert_{\ell^2}\le\lVert a\rVert_{\ell^2}\lVert b\rVert_{\ell^1}$.
> >
> > **Translation invariance.** For each fixed $\eta$, the translate $\tau_\eta a$ defined by $(\tau_\eta a)(\xi)=a(\xi-\eta)$ has $\lVert\tau_\eta a\rVert_{\ell^2}^2 = \sum_\xi a(\xi-\eta)^2 = \sum_{\xi'}a(\xi')^2 = \lVert a\rVert_{\ell^2}^2$ (reindex $\xi'=\xi-\eta$; the lattice $\mathbb{Z}^n$ is invariant under the shift). Hence $\lVert\tau_\eta a\rVert_{\ell^2}=\lVert a\rVert_{\ell^2}$.
> >
> > **Triangle inequality in $\ell^2$.** By definition $a*b = \sum_{\eta} b(\eta)\,\tau_\eta a$ as sequences. For any finite subset $F\subset\mathbb{Z}^n$, the triangle inequality (Minkowski's inequality) in the Hilbert space $\ell^2(\mathbb{Z}^n)$ gives
> > $$\Big\lVert \sum_{\eta\in F} b(\eta)\,\tau_\eta a\Big\rVert_{\ell^2} \le \sum_{\eta\in F} b(\eta)\,\lVert\tau_\eta a\rVert_{\ell^2} = \Big(\sum_{\eta\in F} b(\eta)\Big)\lVert a\rVert_{\ell^2} \le \lVert b\rVert_{\ell^1}\,\lVert a\rVert_{\ell^2},$$
> > using translation invariance for the equality and $b\ge0$ for the last step.
> >
> > **Passage to the full sum.** The partial sums $s_F:=\sum_{\eta\in F}b(\eta)\tau_\eta a$ are monotone increasing in $F$ (all terms nonnegative), so for every $\xi$, $s_F(\xi)\uparrow (a*b)(\xi)$ as $F\uparrow\mathbb{Z}^n$. By the monotone convergence theorem for the counting measure on $\mathbb{Z}^n$ (equivalently, monotone limits of nonnegative partial sums), $\lVert s_F\rVert_{\ell^2}\uparrow\lVert a*b\rVert_{\ell^2}$. Since every $\lVert s_F\rVert_{\ell^2}\le\lVert a\rVert_{\ell^2}\lVert b\rVert_{\ell^1}$, the supremum obeys the same bound:
> > $$\lVert a*b\rVert_{\ell^2}\le\lVert a\rVert_{\ell^2}\,\lVert b\rVert_{\ell^1}<\infty.$$
> > In particular $a*b\in\ell^2$, so the convolution series converges (absolutely) for every $\xi$. $\blacksquare$

> [!note]- Lemma 3: Summable weight bound (where the dimension is spent)
> **Statement:** Let $t\in\mathbb{R}$ with $2t>n$, and set $S_t := \sum_{\eta\in\mathbb{Z}^n}\langle\eta\rangle^{-2t}$. Then $S_t<\infty$, and for every $b\in\ell^2(\mathbb{Z}^n)$ the sequence $c(\eta):=\langle\eta\rangle^{-t}\,b(\eta)$ lies in $\ell^1(\mathbb{Z}^n)$ with
> $$\lVert c\rVert_{\ell^1} = \sum_\eta \langle\eta\rangle^{-t}\lvert b(\eta)\rvert \le S_t^{1/2}\,\lVert b\rVert_{\ell^2}.$$
>
> **Hint:** Cauchy–Schwarz with the two factors $\langle\eta\rangle^{-t}$ and $\lvert b(\eta)\rvert$; finiteness of $S_t$ is the lattice-sum theorem.
>
> **Why needed:** It converts an $\ell^2$ sequence (weighted coefficients of a factor) into an $\ell^1$ sequence, at the exact cost $2t>n$; this is the only place the dimensional threshold enters, and $t = k_1+k_2-k$ is the surplus.
>
> > [!note]- Full proof
> > **Finiteness of $S_t$.** By [[Thm - Convergence of the Lattice Sum|the lattice-sum theorem]] — for $s\in\mathbb{R}$, $\sum_{\eta\in\mathbb{Z}^n}(1+\lvert\eta\rvert^2)^{-s}<\infty$ if and only if $2s>n$ — applied with $s=t$, the hypothesis $2t>n$ gives $S_t=\sum_\eta\langle\eta\rangle^{-2t}<\infty$.
> >
> > **Cauchy–Schwarz.** Write $\langle\eta\rangle^{-t}\lvert b(\eta)\rvert = \langle\eta\rangle^{-t}\cdot\lvert b(\eta)\rvert$ and apply the [[Thm - Cauchy-Schwarz Inequality|Cauchy–Schwarz inequality]] for the counting measure on $\mathbb{Z}^n$ (that is, in $\ell^2(\mathbb{Z}^n)$, $\sum\lvert f g\rvert\le(\sum\lvert f\rvert^2)^{1/2}(\sum\lvert g\rvert^2)^{1/2}$) with $f(\eta)=\langle\eta\rangle^{-t}$ and $g(\eta)=\lvert b(\eta)\rvert$:
> > $$\sum_\eta \langle\eta\rangle^{-t}\lvert b(\eta)\rvert \le \Big(\sum_\eta \langle\eta\rangle^{-2t}\Big)^{1/2}\Big(\sum_\eta \lvert b(\eta)\rvert^2\Big)^{1/2} = S_t^{1/2}\,\lVert b\rVert_{\ell^2}.$$
> > The right-hand side is finite because $S_t<\infty$ and $b\in\ell^2$; hence $c\in\ell^1$ with the stated bound. $\blacksquare$

> [!note]- Lemma 4: Continuous bilinear extension by density
> **Statement:** Let $X,Y,Z$ be normed spaces with $Z$ complete (Banach), let $X_0\subseteq X$ and $Y_0\subseteq Y$ be dense linear subspaces, and let $B_0 : X_0\times Y_0\to Z$ be bilinear with $\lVert B_0(x,y)\rVert_Z\le C\lVert x\rVert_X\lVert y\rVert_Y$ for all $x\in X_0$, $y\in Y_0$. Then $B_0$ extends uniquely to a bilinear map $B:X\times Y\to Z$ satisfying the same bound $\lVert B(x,y)\rVert_Z\le C\lVert x\rVert_X\lVert y\rVert_Y$; the extension is separately continuous, indeed jointly continuous.
>
> **Hint:** For $x\in X$, $y\in Y$ take sequences $x_j\to x$ in $X_0$, $y_j\to y$ in $Y_0$; show $(B_0(x_j,y_j))_j$ is Cauchy in $Z$ using the bilinear identity $B_0(x_j,y_j)-B_0(x_l,y_l)=B_0(x_j-x_l,y_j)+B_0(x_l,y_j-y_l)$.
>
> **Why needed:** Every estimate is proved for smooth sections; this lemma is what turns "bounded on the dense subspace $\Gamma(E)$" into "bounded on the completed Sobolev spaces".
>
> > [!note]- Full proof
> > **Cauchy property.** Fix $x\in X$, $y\in Y$ and choose $x_j\to x$ ($x_j\in X_0$), $y_j\to y$ ($y_j\in Y_0$); such sequences exist by density. Convergent sequences are bounded, so $\sup_j\lVert x_j\rVert_X=:P<\infty$ and $\sup_j\lVert y_j\rVert_Y=:Q<\infty$. Using bilinearity,
> > $$B_0(x_j,y_j)-B_0(x_l,y_l) = B_0(x_j-x_l,\,y_j) + B_0(x_l,\,y_j-y_l),$$
> > whence, by the bound on $B_0$,
> > $$\lVert B_0(x_j,y_j)-B_0(x_l,y_l)\rVert_Z \le C\lVert x_j-x_l\rVert_X\,Q + C\,P\,\lVert y_j-y_l\rVert_Y \xrightarrow[j,l\to\infty]{} 0,$$
> > since $(x_j),(y_j)$ are Cauchy. Thus $(B_0(x_j,y_j))_j$ is Cauchy in the complete space $Z$ and converges; define $B(x,y):=\lim_j B_0(x_j,y_j)$.
> >
> > **Independence of the sequences.** If $x_j'\to x$, $y_j'\to y$ are other approximating sequences, interleaving them with $(x_j),(y_j)$ produces one approximating sequence whose image must converge; hence the two limits agree, and $B(x,y)$ is well defined. On $X_0\times Y_0$ the constant sequences show $B=B_0$, so $B$ extends $B_0$.
> >
> > **Bound and bilinearity.** Passing to the limit in $\lVert B_0(x_j,y_j)\rVert_Z\le C\lVert x_j\rVert_X\lVert y_j\rVert_Y$ and using continuity of the norm gives $\lVert B(x,y)\rVert_Z\le C\lVert x\rVert_X\lVert y\rVert_Y$. Bilinearity passes to the limit because addition and scalar multiplication are continuous. Uniqueness: any continuous extension agrees with $B_0$ on the dense set $X_0\times Y_0$, hence with $B$ everywhere by continuity. $\blacksquare$

> [!note]- Lemma 5: Multiplication is convolution of Fourier coefficients
> **Statement:** For $u,v\in C^\infty(T^n;\mathbb{C})$ the product $uv$ is smooth and, for every $\xi\in\mathbb{Z}^n$,
> $$\widehat{uv}(\xi) = \sum_{\eta\in\mathbb{Z}^n}\hat u(\xi-\eta)\,\hat v(\eta) = (\hat u * \hat v)(\xi),$$
> the series converging absolutely.
>
> **Hint:** Substitute the uniformly and absolutely convergent Fourier series of $u$ and $v$ (from the Fourier page) into $\hat{uv}(\xi)=(2\pi)^{-n}\int_{T^n}uv\,e^{-i\langle\xi,x\rangle}dx$ and integrate term by term, using orthogonality of the characters.
>
> **Why needed:** It is the identity that translates the theorem from functions to sequences; the entire torus estimate is about the right-hand convolution.
>
> > [!note]- Full proof
> > **Absolute convergence of the factor series.** By [[Thm - Fourier Series of Smooth Functions on the Torus|the Fourier series theorem]], for smooth $u$ the coefficients decay rapidly, $\lvert\hat u(\xi)\rvert\le C_N\langle\xi\rangle^{-N}$ for every $N$, and the series $u(x)=\sum_\zeta\hat u(\zeta)e^{i\langle\zeta,x\rangle}$ converges absolutely and uniformly; likewise for $v$. In particular $\sum_\zeta\lvert\hat u(\zeta)\rvert<\infty$ and $\sum_\eta\lvert\hat v(\eta)\rvert<\infty$.
> >
> > **Term-by-term integration.** The product of the two uniformly convergent series,
> > $$u(x)v(x) = \sum_{\zeta,\eta}\hat u(\zeta)\hat v(\eta)\,e^{i\langle\zeta+\eta,x\rangle},$$
> > converges absolutely and uniformly on the compact torus, because $\sum_{\zeta,\eta}\lvert\hat u(\zeta)\rvert\lvert\hat v(\eta)\rvert = \big(\sum_\zeta\lvert\hat u(\zeta)\rvert\big)\big(\sum_\eta\lvert\hat v(\eta)\rvert\big)<\infty$. A uniformly convergent series may be integrated term by term against the bounded function $e^{-i\langle\xi,x\rangle}$, so
> > $$\widehat{uv}(\xi) = (2\pi)^{-n}\int_{T^n} u v\, e^{-i\langle\xi,x\rangle}\,dx = \sum_{\zeta,\eta}\hat u(\zeta)\hat v(\eta)\,(2\pi)^{-n}\int_{T^n} e^{i\langle\zeta+\eta-\xi,x\rangle}\,dx.$$
> >
> > **Orthogonality of characters.** For $m\in\mathbb{Z}^n$, $(2\pi)^{-n}\int_{T^n}e^{i\langle m,x\rangle}dx = 1$ if $m=0$ and $0$ otherwise (the coordinatewise integral $\int_0^{2\pi}e^{im_jx_j}dx_j$ vanishes unless $m_j=0$). Only the terms with $\zeta+\eta=\xi$, that is $\zeta=\xi-\eta$, survive:
> > $$\widehat{uv}(\xi) = \sum_{\eta}\hat u(\xi-\eta)\hat v(\eta).$$
> > The rearrangement into a sum over $\eta$ alone is legitimate because the double series is absolutely convergent. Smoothness of $uv$ is immediate (product of smooth functions). $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the theorem in the order (b) $\Rightarrow$ (a) $\Rightarrow$ (c), first on the torus for smooth functions, then globalising and extending by density; the corollary is Step 7.
>
> **Step 0 — preconditions and the standing reduction.** By [[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts|the charts theorem]], each $H_k(M;E)$ is the completion of $\Gamma(E)$ in a chart norm, $\Gamma(E)$ is dense in it (part (iii)), the norm on $T^n$ equals the weighted $\ell^2$ norm $\lVert w\rVert_k^2=\sum_\xi\langle\xi\rangle^{2k}\lvert\hat w(\xi)\rvert^2$ (part (i) with [[Thm - Sobolev Norms on the Torus via Fourier Coefficients|the torus identification]]), and the $L^2$ pairing extends to a perfect pairing $H_k\times H_{-k}\to\mathbb{R}$ (part (iv)). Since multiplication of smooth sections is bilinear and produces smooth sections, and $\Gamma$ is dense in each Sobolev space, it suffices by Lemma 4 to prove each stated *inequality on smooth sections*; the bounded bilinear extension then exists and is unique. We fix real-valued smooth $u,v$ (for the bundle-valued and complex cases see Step 6); on the torus we allow complex values, which only helps.
>
> ---
>
> **Part I — the torus estimate for (b).** *Claim.* For integers $k_1,k_2\ge k\ge0$ with $t:=k_1+k_2-k>\tfrac n2$ and all $u,v\in C^\infty(T^n;\mathbb{C})$,
> $$\lVert uv\rVert_k \le 2^{k+1}S_t^{1/2}\,\lVert u\rVert_{k_1}\lVert v\rVert_{k_2}, \qquad S_t=\sum_{\eta}\langle\eta\rangle^{-2t}<\infty.$$
>
> **Set up the weighted sequences.** Put
> $$a(\zeta):=\langle\zeta\rangle^{k_1}\lvert\hat u(\zeta)\rvert, \qquad b(\eta):=\langle\eta\rangle^{k_2}\lvert\hat v(\eta)\rvert,$$
> so that $a,b\ge0$ with $\lVert a\rVert_{\ell^2}=\lVert u\rVert_{k_1}$ and $\lVert b\rVert_{\ell^2}=\lVert v\rVert_{k_2}$ by definition of the $H_{k_1}, H_{k_2}$ norms. By Lemma 5 and the triangle inequality for the absolutely convergent series,
> $$\langle\xi\rangle^k\lvert\widehat{uv}(\xi)\rvert \le \langle\xi\rangle^k\sum_{\eta}\lvert\hat u(\xi-\eta)\rvert\,\lvert\hat v(\eta)\rvert = \sum_{\eta}\langle\xi\rangle^k\lvert\hat u(\xi-\eta)\rvert\,\lvert\hat v(\eta)\rvert. \tag{I.1}$$
>
> **Split the frequency lattice.** For fixed $\xi$ partition $\mathbb{Z}^n = A_\xi\sqcup B_\xi$ with
> $$A_\xi=\{\eta : \lvert\eta\rvert\le\lvert\xi-\eta\rvert\}, \qquad B_\xi=\{\eta : \lvert\eta\rvert>\lvert\xi-\eta\rvert\},$$
> so the sum in (I.1) is the sum over $A_\xi$ plus the sum over $B_\xi$.
>
> **Estimate on $A_\xi$ (surplus onto $\eta$).** For $\eta\in A_\xi$ we have $\lvert\eta\rvert\le\lvert\xi-\eta\rvert$, hence (Lemma 1) $\langle\xi\rangle^k\le 2^k\langle\xi-\eta\rangle^k$ and $\langle\eta\rangle\le\langle\xi-\eta\rangle$. Writing $\langle\xi-\eta\rangle^k=\langle\xi-\eta\rangle^{k_1}\langle\xi-\eta\rangle^{k-k_1}$ and using $k-k_1\le0$ with the monotonicity clause of Lemma 1 ($\langle\xi-\eta\rangle^{k-k_1}\le\langle\eta\rangle^{k-k_1}$),
> $$\langle\xi\rangle^k\lvert\hat u(\xi-\eta)\rvert \le 2^k\langle\xi-\eta\rangle^{k_1}\lvert\hat u(\xi-\eta)\rvert\cdot\langle\eta\rangle^{k-k_1} = 2^k\,a(\xi-\eta)\,\langle\eta\rangle^{k-k_1} \qquad(\text{definition of } a).$$
> Multiplying by $\lvert\hat v(\eta)\rvert = \langle\eta\rangle^{-k_2}b(\eta)$ and using $k-k_1-k_2 = -t$,
> $$\langle\xi\rangle^k\lvert\hat u(\xi-\eta)\rvert\lvert\hat v(\eta)\rvert \le 2^k\,a(\xi-\eta)\,\langle\eta\rangle^{-t}\,b(\eta) \qquad(\eta\in A_\xi). \tag{I.2}$$
> Summing over $\eta\in A_\xi$ and then dropping the restriction (all terms are nonnegative, so the sum over $A_\xi$ is at most the sum over $\mathbb{Z}^n$),
> $$\sum_{\eta\in A_\xi}\langle\xi\rangle^k\lvert\hat u(\xi-\eta)\rvert\lvert\hat v(\eta)\rvert \le 2^k\sum_{\eta}a(\xi-\eta)\,c(\eta) = 2^k\,(a*c)(\xi), \qquad c(\eta):=\langle\eta\rangle^{-t}b(\eta). \tag{I.3}$$
>
> **Estimate on $B_\xi$ (surplus onto $\xi-\eta$).** For $\eta\in B_\xi$ we have $\lvert\xi-\eta\rvert<\lvert\eta\rvert$, hence (Lemma 1) $\langle\xi\rangle^k\le2^k\langle\eta\rangle^k$ and $\langle\xi-\eta\rangle\le\langle\eta\rangle$. Writing $\langle\eta\rangle^k=\langle\eta\rangle^{k_2}\langle\eta\rangle^{k-k_2}$ and using $k-k_2\le0$ with $\langle\eta\rangle^{k-k_2}\le\langle\xi-\eta\rangle^{k-k_2}$ (Lemma 1 monotonicity, since $\langle\xi-\eta\rangle\le\langle\eta\rangle$),
> $$\langle\xi\rangle^k\lvert\hat v(\eta)\rvert \le 2^k\langle\eta\rangle^{k_2}\lvert\hat v(\eta)\rvert\cdot\langle\xi-\eta\rangle^{k-k_2} = 2^k\,b(\eta)\,\langle\xi-\eta\rangle^{k-k_2}.$$
> Multiplying by $\lvert\hat u(\xi-\eta)\rvert=\langle\xi-\eta\rangle^{-k_1}a(\xi-\eta)$ and using $k-k_2-k_1=-t$,
> $$\langle\xi\rangle^k\lvert\hat u(\xi-\eta)\rvert\lvert\hat v(\eta)\rvert \le 2^k\,\langle\xi-\eta\rangle^{-t}a(\xi-\eta)\,b(\eta) \qquad(\eta\in B_\xi). \tag{I.4}$$
> Summing over $\eta\in B_\xi$ and dropping the restriction,
> $$\sum_{\eta\in B_\xi}\langle\xi\rangle^k\lvert\hat u(\xi-\eta)\rvert\lvert\hat v(\eta)\rvert \le 2^k\sum_{\eta}d(\xi-\eta)\,b(\eta) = 2^k\,(d*b)(\xi), \qquad d(\zeta):=\langle\zeta\rangle^{-t}a(\zeta). \tag{I.5}$$
>
> **Combine and take $\ell^2$ norms.** Adding (I.3) and (I.5) into (I.1),
> $$\langle\xi\rangle^k\lvert\widehat{uv}(\xi)\rvert \le 2^k\big[(a*c)(\xi)+(d*b)(\xi)\big] \qquad\text{for every }\xi. \tag{I.6}$$
> Taking the $\ell^2(\mathbb{Z}^n)$ norm in $\xi$ and using the triangle inequality,
> $$\lVert uv\rVert_k = \big\lVert \langle\cdot\rangle^k\widehat{uv}\big\rVert_{\ell^2} \le 2^k\big(\lVert a*c\rVert_{\ell^2} + \lVert d*b\rVert_{\ell^2}\big) \qquad(\text{by (I.6) and monotonicity of the } \ell^2 \text{ norm}). \tag{I.7}$$
> Now $2t>n$, so by Lemma 3 the sequences $c=\langle\cdot\rangle^{-t}b$ and $d=\langle\cdot\rangle^{-t}a$ lie in $\ell^1$ with $\lVert c\rVert_{\ell^1}\le S_t^{1/2}\lVert b\rVert_{\ell^2}$ and $\lVert d\rVert_{\ell^1}\le S_t^{1/2}\lVert a\rVert_{\ell^2}$. Young's inequality (Lemma 2) then gives
> $$\lVert a*c\rVert_{\ell^2} \le \lVert a\rVert_{\ell^2}\lVert c\rVert_{\ell^1} \le S_t^{1/2}\lVert a\rVert_{\ell^2}\lVert b\rVert_{\ell^2}, \qquad \lVert d*b\rVert_{\ell^2} \le \lVert d\rVert_{\ell^1}\lVert b\rVert_{\ell^2} \le S_t^{1/2}\lVert a\rVert_{\ell^2}\lVert b\rVert_{\ell^2}.$$
> Substituting into (I.7) and recalling $\lVert a\rVert_{\ell^2}=\lVert u\rVert_{k_1}$, $\lVert b\rVert_{\ell^2}=\lVert v\rVert_{k_2}$,
> $$\lVert uv\rVert_k \le 2^{k+1}S_t^{1/2}\,\lVert u\rVert_{k_1}\lVert v\rVert_{k_2}.$$
> This proves the torus claim for (b). $\square$ (Part I)
>
> ---
>
> **Part II — the algebra property (a).** Take $k_1=k_2=k$ with $2k>n$. Then $k_1,k_2=k\ge k$ and $t=k_1+k_2-k=k>\tfrac n2$, so the hypotheses of Part I hold and, on the torus, $\lVert uv\rVert_k\le C\lVert u\rVert_k\lVert v\rVert_k$ with $C=2^{k+1}S_k^{1/2}$. (The globalisation to $M$ is Step 6.) For the algebraic structure, work on $M$: $H_k(M)$ is complete, being a Hilbert space ([[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts|charts theorem]] part (ii)). Multiplication on $\Gamma(M)$ is commutative and associative and has unit the constant function $1$ — which lies in $H_k(M)$ for every $k$ because $M$ is compact, so $1$ is smooth of bounded derivatives — and $1\cdot u=u$. Each of these identities holds for all smooth $u,v,w$ and each side is $\lVert\cdot\rVert_k$-continuous in every argument (by the bound just proved, multiplication is jointly continuous), so by density in $H_k(M)$ (Lemma 4) commutativity, associativity, and the unit law persist on $H_k(M)$. Renorming by $\lVert\cdot\rVert_k':=C\lVert\cdot\rVert_k$ (an equivalent norm) makes the bound submultiplicative, $\lVert uv\rVert_k'\le\lVert u\rVert_k'\lVert v\rVert_k'$: indeed $\lVert uv\rVert_k'=C\lVert uv\rVert_k\le C\cdot C\lVert u\rVert_k\lVert v\rVert_k=\lVert u\rVert_k'\lVert v\rVert_k'$. Hence $(H_k(M),\lVert\cdot\rVert_k')$ is a commutative unital Banach algebra. $\square$ (Part II)
>
> ---
>
> **Part III — the multiplier property (c).** Let $2k>n$ and $\lvert m\rvert\le k$; we bound $\lVert uv\rVert_m$ for real-valued $u\in\Gamma(M)$, $v\in\Gamma(M)$, working on $M$ (the estimate uses only the globalised (b) from Step 6 and the manifold duality).
>
> **Case $0\le m\le k$.** Apply the globalised part (b) with source orders $k_1:=k$ (for $u$) and $k_2:=m$ (for $v$) and target order $m$. The hypotheses hold: $k_1=k\ge m$ and $k_2=m\ge m$ (so $k_1,k_2\ge m$), and the surplus is $k_1+k_2-m = k+m-m = k>\tfrac n2$ (since $2k>n$). Hence
> $$\lVert uv\rVert_m \le C\,\lVert u\rVert_k\,\lVert v\rVert_m. \tag{III.1}$$
>
> **Case $-k\le m<0$.** Set $m':=-m$, so $0<m'\le k$. By the perfect pairing ([[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts|charts theorem]] part (iv)) the negative-order norm is the dual norm: there is a constant $c_0>0$ with
> $$\lVert w\rVert_m \le c_0\sup\big\{\lvert(w,\phi)_{L^2}\rvert : \phi\in\Gamma(M),\ \lVert\phi\rVert_{m'}\le1\big\} \tag{III.2}$$
> for all $w\in\Gamma(M)$ (the pairing $H_m\times H_{m'}\to\mathbb{R}$ is perfect and continuous). Take $w=uv$. For any smooth $\phi$, since pointwise multiplication of real functions is commutative and the pairing is the plain integral,
> $$(uv,\phi)_{L^2} = \int_M u\,v\,\phi\,\mathrm{vol} = \int_M v\,(u\phi)\,\mathrm{vol} = (v,\,u\phi)_{L^2}. \tag{III.3}$$
> Bound the right-hand side by the pairing inequality $\lvert(v,\psi)_{L^2}\rvert\le C\lVert v\rVert_m\lVert\psi\rVert_{m'}$ (charts theorem part (iv), with $\psi:=u\phi$ and orders $m,m'=-m$), then bound $\lVert u\phi\rVert_{m'}$ by the already-proved Case $0\le m'\le k$ (III.1) applied to the pair $(u,\phi)$ (legitimate: $2k>n$ and $0<m'\le k$):
> $$\lvert(uv,\phi)_{L^2}\rvert = \lvert(v,u\phi)_{L^2}\rvert \le C\lVert v\rVert_m\,\lVert u\phi\rVert_{m'} \le C\lVert v\rVert_m\cdot C\lVert u\rVert_k\lVert \phi\rVert_{m'}. \tag{III.4}$$
> For $\lVert\phi\rVert_{m'}\le1$ the right-hand side is $\le C^2\lVert u\rVert_k\lVert v\rVert_m$; taking the supremum over such $\phi$ and using (III.2),
> $$\lVert uv\rVert_m \le c_0 C^2\,\lVert u\rVert_k\,\lVert v\rVert_m.$$
> In both cases $\lVert uv\rVert_m\le C'\lVert u\rVert_k\lVert v\rVert_m$ on smooth functions; by Lemma 4 multiplication extends to a bounded bilinear map $H_k(M)\times H_m(M)\to H_m(M)$ with the same bound. $\square$ (Part III)
>
> ---
>
> **Part IV — globalisation to $M$ (Step 6).** We upgrade Part I from $T^n$ to $M$ and, at the same time, from scalar products to a smooth bilinear bundle map $\beta:E_1\otimes E_2\to E_3$; the scalar statement of (b) is the case $E_1=E_2=E_3=M\times\mathbb{R}$ with $\beta$ ordinary multiplication.
>
> **Chart data.** Fix a finite atlas $\kappa_i:U_i\to\kappa_i(U_i)\subset(-\pi,\pi)^n\subset T^n$ trivialising $E_1,E_2,E_3$, with a subordinate partition of unity $(\phi_i)$, as in the [[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts|charts theorem]]; the norm on $H_k(M;E_3)$ is equivalent to $\lVert w\rVert_{(k)}^2=\sum_i\lVert(\phi_i w)\circ\kappa_i^{-1}\rVert_{H_k(T^n;\mathbb{C}^{r_3})}^2$. For each $i$ choose $\psi_i\in C_c^\infty(U_i)$ with $\psi_i\equiv1$ on $\operatorname{supp}\phi_i$ (a smooth cutoff, [[Thm - Existence of Smooth Bump Functions|existence of bump functions]]); then $\phi_i = \phi_i\psi_i$, and because $\psi_i=1$ wherever $\phi_i\ne0$,
> $$\phi_i\,\beta(u,v) = \beta(\phi_i u,\ \psi_i v) \tag{IV.1}$$
> as sections of $E_3$ (both sides vanish off $\operatorname{supp}\phi_i$; on it, $\psi_i v=v$ and $\phi_i\beta(u,v)=\beta(\phi_i u,v)$ by bilinearity of $\beta$ in the first slot).
>
> **Transport to the torus.** In the trivialisations, $\beta$ has smooth coefficient functions $\gamma^{c}_{ab}\in C^\infty(U_i)$ with $\beta(s,t)_c=\sum_{a,b}\gamma^c_{ab}\,s_a t_b$ on $U_i$. Pushing (IV.1) forward by $\kappa_i$, the $c$-th component of $(\phi_i\beta(u,v))\circ\kappa_i^{-1}$ is the finite sum
> $$\sum_{a,b}\ (\gamma^c_{ab}\circ\kappa_i^{-1})\cdot\big[(\phi_i u)_a\circ\kappa_i^{-1}\big]\cdot\big[(\psi_i v)_b\circ\kappa_i^{-1}\big], \tag{IV.2}$$
> each summand a product of a fixed smooth compactly supported function on $T^n$ with two scalar functions on $T^n$.
>
> **Apply the scalar torus estimate and smooth multipliers.** By Part I on $T^n$ (target order $k$, source orders $k_1,k_2$), each scalar product $\big[(\phi_i u)_a\circ\kappa_i^{-1}\big]\big[(\psi_i v)_b\circ\kappa_i^{-1}\big]$ has $H_k(T^n)$ norm at most $C\lVert(\phi_i u)_a\circ\kappa_i^{-1}\rVert_{k_1}\lVert(\psi_i v)_b\circ\kappa_i^{-1}\rVert_{k_2}$. Multiplication by the fixed smooth function $\gamma^c_{ab}\circ\kappa_i^{-1}$ is bounded on $H_k(T^n)$ — this is itself an instance of Part I, with the smooth factor placed in $H_{k_1'}$ for $k_1'$ chosen so large that $k_1'+k-k=k_1'>\tfrac n2$, so that $\lVert\gamma w\rVert_k\le C\lVert\gamma\rVert_{k_1'}\lVert w\rVert_k$. Combining and summing the finitely many terms in (IV.2),
> $$\big\lVert(\phi_i\beta(u,v))\circ\kappa_i^{-1}\big\rVert_{H_k(T^n)} \le C_i\,\lVert(\phi_i u)\circ\kappa_i^{-1}\rVert_{H_{k_1}}\,\lVert(\psi_i v)\circ\kappa_i^{-1}\rVert_{H_{k_2}} \le C_i'\,\lVert u\rVert_{k_1}\,\lVert v\rVert_{k_2},$$
> the last inequality because $w\mapsto(\phi_i w)\circ\kappa_i^{-1}$ and $w\mapsto(\psi_i w)\circ\kappa_i^{-1}$ are bounded from $H_\ell(M;E)$ to $H_\ell(T^n;\mathbb{C}^r)$ (charts theorem: $\phi_i,\psi_i$ are smooth multipliers and localisation is bounded on every $H_\ell$).
>
> **Sum the charts.** Squaring, summing over the finitely many $i$, and taking the square root,
> $$\lVert\beta(u,v)\rVert_k \le C\,\lVert\beta(u,v)\rVert_{(k)} = C\Big(\sum_i\lVert(\phi_i\beta(u,v))\circ\kappa_i^{-1}\rVert_{H_k(T^n)}^2\Big)^{1/2} \le C''\,\lVert u\rVert_{k_1}\,\lVert v\rVert_{k_2},$$
> using the norm equivalence of the charts theorem. This proves the bound on smooth sections; by Lemma 4 the fibrewise product $\beta$ extends to a bounded bilinear map $H_{k_1}(M;E_1)\times H_{k_2}(M;E_2)\to H_k(M;E_3)$. Taking $\beta$ to be scalar multiplication gives the scalar statement of (b), and the diagonal case gives (a) on $M$. $\square$ (Part IV)
>
> ---
>
> **Step 7 — Corollary 1.** Let $n=4$. For an integer $k\ge3$ we have $2k\ge6>4=n$, so part (a) applies and $H_k(M)$ is a commutative unital Banach algebra; in particular $H_3(M^4)$ is. This is the positive statement of the corollary, and it is now proved.
>
> **The borderline $k=2$ is not an algebra.** For $k=2$ one has $2k=4=n$, so the strict inequality $2k>n$ fails and part (a) does not apply. The failure is genuine: there exists $u\in H_2(T^4)$ with $u^2\notin H_2(T^4)$, so no bound $\lVert u^2\rVert_2\le C\lVert u\rVert_2^2$ can hold. The witness is a function with a mild $\log\log$ singularity — precisely the borderline of the embedding $H_{n/2}\not\subset C^0$ studied in dimension two in [[Ex - An Unbounded Function in W-1-2 of the Two-Torus|the borderline exercise]] — scaled to dimension four; its explicit construction, together with the verification that $u\in H_2(T^4)$ while $u^2\notin H_2(T^4)$, is carried out in [[Ex - W-3-2 is an Algebra in Dimension Four]]. We do not reproduce that computation here; the positive statement $k\ge3$ is what the four-manifold theory uses, and it is fully proved above. $\square$ (Step 7)
>
> **Conclusion.** Parts I–IV establish (b) on $M$ for all admissible orders and bundle maps, hence (a) as the diagonal case and (c) as the multiplier case, each first on smooth sections and then on the completed Sobolev spaces by the density extension of Lemma 4; Step 7 records the four-dimensional corollary. Therefore pointwise multiplication extends to bounded bilinear maps in each stated regime, and $H_k(M)$ is a Banach algebra whenever $2k>n$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Nonlinear elliptic partial differential equations (fixed-point existence).** Consider a semilinear equation $\Delta u = f(u)$ on a compact manifold, where $f$ is a polynomial. To solve it by a fixed-point argument in $H_k$ one must know that $u\mapsto f(u)$ maps $H_k$ to $H_{k}$ (or $H_{k-2}$) boundedly; the multiplication theorem is exactly what guarantees $f(u)\in H_k$ when $2k>n$, so the nonlinearity does not leave the space. The application is non-obvious because the naive fear is that squaring a Sobolev function halves its regularity; the theorem says that above the embedding threshold it does not.

**Harmonic analysis and paraproducts.** The estimate $H^{s_1}\cdot H^{s_2}\subset H^s$ for $s\le\min(s_1,s_2)$, $s_1+s_2-s>n/2$, is the periodic model of the Kato–Ponce and paraproduct estimates that organise nonlinear terms in dispersive and fluid partial differential equations. A reader who has met Littlewood–Paley theory will recognise the two-region split of Part I as the crudest paraproduct decomposition (high-low versus low-high frequency interaction). The application is non-obvious because the sharp fractional-order theory looks far removed from a convolution of lattice coefficients, yet the mechanism is identical.

**Gauge theory: the Sobolev gauge group as a Lie group.** In Chapter XI one needs $\mathcal{G}^{k}=H_k(M;S^1)$ to be a Banach Lie group acting smoothly on Sobolev connections. The group operation is pointwise multiplication of $S^1$-valued Sobolev maps; part (a) (with $2k>n$) makes the product of two such maps again $H_k$, and the composition-with-analytic-functions theorem, itself built on (a), gives the exponential chart. The application is non-obvious because "the space of Sobolev maps into a manifold is a Banach manifold" is a statement one cannot even phrase without the algebra property first securing that products stay in the space.

---

# Bridges

- **From the Fourier picture to elliptic bootstrapping.** The multiplication theorem and [[Thm - Elliptic Regularity and the Elliptic Estimate|elliptic regularity]] form a self-reinforcing pair: given a solution of a nonlinear elliptic equation in some $H_k$ above threshold, multiplication places the nonlinear terms in a Sobolev space, elliptic regularity gains two orders, and multiplication again places the (now higher-regularity) nonlinear terms one step up. Iterating this bridge is the standard proof that Sobolev solutions of geometric equations are smooth. The construction is a loop: $u\in H_k \xrightarrow{\text{multiplication}} f(u)\in H_k \xrightarrow{\text{elliptic estimate}} u\in H_{k+2}$.

- **To the gauge group and its Lie algebra.** Part (a) makes $H_k(M;\mathbb{C})$ a Banach algebra; restricting to $\{\lvert g\rvert=1\}$ and using [[Thm - Composition with Analytic Functions on the Sobolev Algebra|composition with the exponential]] realises $\mathcal{G}^k=H_k(M;S^1)$ as a group with Lie algebra $H_k(M;i\mathbb{R})$. The bridge is concrete: the chart near $g_0\in\mathcal{G}^k$ is $\xi\mapsto g_0 e^{i\xi}$ for $\xi\in H_k(M;\mathbb{R})$, and the algebra bound is what makes this map and its inverse (a branch of $\log$ composed with $g_0^{-1}g$) smooth between Banach spaces.

- **To Rellich compactness in moduli problems.** Where [[Thm - Rellich Compactness Theorem|Rellich compactness]] extracts a convergent subsequence in a lower Sobolev norm, the multiplication theorem guarantees that the nonlinear terms evaluated along the subsequence converge in a still-lower norm, because multiplication is a continuous bilinear map. The two together are the analytic core of every compactness theorem for a gauge-theoretic moduli space: extract a limit (Rellich), then pass the equation to the limit (multiplication).

---

# Unlocked by This

> [!tip] The Sobolev Gauge Group *(from Gauge Theory XI)*
> With $2k>n$, part (a) makes $H_k(M;\mathbb{C})$ a Banach algebra, and the $S^1$-valued Sobolev maps $\mathcal{G}^k=H_k(M;S^1)$ form a group under pointwise multiplication with $g^{-1}=\bar g\in H_k$. Combined with **[[Thm - Composition with Analytic Functions on the Sobolev Algebra|composition with analytic functions]]** this gives $\mathcal{G}^k$ a Banach-Lie-group structure, the setting for the quotient of Sobolev connections by gauge in Seiberg–Witten theory.

> [!tip] Smoothness of the Seiberg–Witten Map *(from Gauge Theory XI)*
> The Seiberg–Witten map has quadratic terms $a\cdot\psi$ (Clifford product of a Sobolev $1$-form with a Sobolev spinor) and $\mu(\psi)$ (a quadratic map of the spinor). Part (b), in its bundle-valued form, makes each of these a bounded bilinear (hence smooth) map of Sobolev sections, so the whole Seiberg–Witten map is a smooth map between Banach manifolds — the precondition for the transversality and moduli-space theory that follows.
