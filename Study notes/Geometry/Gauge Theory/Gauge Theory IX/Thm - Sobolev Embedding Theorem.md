---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts"
  - "Thm - Fourier Series of Smooth Functions on the Torus"
  - "Thm - Convergence of the Lattice Sum"
  - "Def - Sobolev Space of Sections"
  - "Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order"
tags: [geometry, gauge-theory, analysis, sobolev]
---

# Notation

Throughout, $M$ is a compact smooth $n$-manifold (smooth means $C^\infty$; manifolds in this series are Hausdorff and second countable) and $E\to M$ is a smooth real or complex [[Def - Vector Bundle|vector bundle]] of rank $q$; we write $\Gamma(E)$ for its smooth [[Def - Section of a Vector Bundle|sections]]. We fix, once and for all, a [[Def - Riemannian Metric|Riemannian metric]] $g$ on $M$, a fibre metric on $E$, and connections $\nabla^E$ on $E$ and $\nabla^M$ on $T^*M$; these induce connections on every tensor bundle $(T^*M)^{\otimes i}\otimes E$, so the iterated covariant derivative $\nabla^i u\in\Gamma\big((T^*M)^{\otimes i}\otimes E\big)$ of a section $u$ is defined.

The $L^2$-Sobolev norms and spaces are those of [[Def - Sobolev Space of Sections]]: for an integer $k\ge0$,
$$\|u\|_{W^{k,2}}^2=\sum_{i=0}^{k}\int_M|\nabla^i u|^2\,\mathrm{vol}_g,\qquad H_k(M;E):=\overline{\big(\Gamma(E),\ \|\cdot\|_{W^{k,2}}\big)},$$
the completion of $\Gamma(E)$ in that norm; $H_0=L^2$. By [[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts]] the same completion is obtained from a finite atlas $\kappa_i:U_i\to\kappa_i(U_i)\subset(-\pi,\pi)^n\subset T^n$ over which $E$ is trivialised, together with a subordinate [[Def - Partition of Unity on a Manifold|partition of unity]] $(\phi_i)$, through the chart norm $\|u\|_{(k)}^2=\sum_i\|(\phi_i u)\circ\kappa_i^{-1}\|_{H_k(T^n;\mathbb C^q)}^2$; the chart norm is equivalent to the connection norm for $k\ge0$ and extends the scale to all integers $k\in\mathbb Z$. We write $\|u\|_k$ for the $H_k(M;E)$ norm, understood up to this equivalence, and reserve $\|\cdot\|_k$ on the torus for the Fourier norm below. On the torus $T^n=\mathbb R^n/2\pi\mathbb Z^n$ with the flat metric and trivial connection, [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order]] fixes the Fourier coefficients $\hat u(\xi)=(2\pi)^{-n}\int_{T^n}u(x)\,e^{-i\langle\xi,x\rangle}\,dx$ for $\xi\in\mathbb Z^n$, and, for every integer $k$, the norm
$$\|u\|_k^2=\sum_{\xi\in\mathbb Z^n}(1+|\xi|^2)^k\,|\hat u(\xi)|^2,\qquad H_k(T^n;\mathbb C^q)=\overline{\big(C^\infty,\ \|\cdot\|_k\big)}.$$

The **uniform (Hölder-zero) scale** is that of [[Def - Sobolev Space of Sections|the Cʳ norm]]: for an integer $r\ge0$,
$$\|u\|_{C^r}=\sum_{i=0}^{r}\sup_{x\in M}\,|\nabla^i u(x)|,$$
and $C^r(M;E)$ is the space of $r$-times continuously differentiable sections with this norm; $\|u\|_{C^0}=\sup_M|u|$. On the torus $C^r(T^n;\mathbb C^q)$ carries the equivalent norm $\sum_{|\alpha|\le r}\sup_{T^n}|\partial^\alpha u|$, where $\alpha=(\alpha_1,\dots,\alpha_n)$ is a multi-index, $|\alpha|=\sum_j\alpha_j$, $\partial^\alpha=\partial_{x_1}^{\alpha_1}\cdots\partial_{x_n}^{\alpha_n}$, and $\xi^\alpha=\xi_1^{\alpha_1}\cdots\xi_n^{\alpha_n}$. The letter $C$ denotes a finite positive constant that may change from line to line and depends only on the fixed data $(M,E,g,\nabla^E,\nabla^M,\text{atlas},\phi_i)$ and on the integers $k,m,r$ — never on the section $u$.

> [!warning] Convention: which parameters we prove, and Haydys's general statement
> This series builds the entire Sobolev theory on $L^2$ (the case $p=2$), because that is all gauge theory over a compact base needs and because the $L^2$ scale is exactly the family of weighted $\ell^2$ spaces produced by Fourier series. Haydys states the embedding for all $W^{k,p}$ with $p>1$. We record his statement below as context and prove only the $p=2$ instances (which are the ones we use); nothing downstream depends on the general-$p$ statement.

---

# Statement

> **Sobolev Embedding Theorem.** Let $M$ be a compact $n$-manifold and $E\to M$ a vector bundle of rank $q$. Then:
>
> **(i) (Descending $L^2$-scale.)** For all integers $k\ge m$ one has $H_k(M;E)\subset H_m(M;E)$, and the inclusion is continuous: there is a constant $C=C(k,m)$ with
> $$\|u\|_m\le C\,\|u\|_k\qquad\text{for all }u\in H_k(M;E).$$
>
> **(ii) (Embedding into $C^r$.)** Let $k,r\ge0$ be integers with $k-\tfrac n2>r$. Then there is a continuous injection
> $$H_k(M;E)\hookrightarrow C^r(M;E):$$
> every element of $H_k(M;E)$ is represented by a unique $C^r$ section, and there is a constant $C=C(k,r)$ with $\|u\|_{C^r}\le C\,\|u\|_{H_k}$ for all $u\in H_k(M;E)$.
>
> **(iii) (Smoothness of the intersection.)** $\displaystyle\bigcap_{k\ge0}H_k(M;E)=C^\infty(M;E)$: a section that lies in $H_k$ for every integer $k\ge0$ is (represented by) a smooth section, and conversely every smooth section lies in every $H_k$.

The three parts feed one another: (i) says the finer spaces sit inside the coarser ones, (ii) trades $L^2$-derivatives for uniform derivatives once there is a strictly positive surplus $k-\tfrac n2-r>0$, and (iii) is (ii) read for every $r$ at once. We record the two dimension-four instances that Chapter XI leans on, and the general-$p$ statement, as companion results.

> **Corollary 1 (the dimension-four instances).** For $n=4$ the embedding $H_5(M;E)\hookrightarrow C^2(M;E)$ and the embedding $H_5(M;E)\hookrightarrow C^0(M;E)$ both hold and are continuous. In the notation of the source these read $W^{5,2}(M^4)\subset C^2(M^4)$ and $W^{5,2}(M^4)\subset C^0(M^4)$.

> [!note]- Recorded as context (not proved and not used in this series): the general $W^{k,p}$ embedding
> Haydys's Theorem 136 (i),(iii) reads, for a compact $n$-manifold $M$ and any $p>1$: the natural embedding $W^{k,p}(M;E)\subset W^{m,q}(M;E)$ is continuous provided $k-\tfrac np\ge m-\tfrac nq$ and $k\ge m$; and there is a continuous embedding $W^{k,p}(M;E)\subset C^r(M;E)$ provided $k-\tfrac np>r$, so that a section lying in $W^{k,p}$ for a fixed $p$ and all $k\ge0$ is smooth. A complete proof of the general-$p$ statement is in L. C. Evans, *Partial Differential Equations*, 2nd ed., §5.6 (Theorems 5.6.1–5.6.3 for the Gagliardo–Nirenberg–Sobolev and Morrey inequalities, Theorem 5.6.5 for the general case), and in R. A. Adams and J. J. F. Fournier, *Sobolev Spaces*, 2nd ed., Theorem 4.12. We do not prove the general-$p$ statement; setting $p=q=2$ recovers our parts (i)–(iii), which are proved in full below, and those are the only cases the series invokes.

---

# Motivation

The Sobolev spaces $H_k(M;E)$ are built to be complete, and completeness is bought at a price: an element of $H_k$ is not a function but an equivalence class of Cauchy sequences of smooth sections, and there is no reason on the face of it that such a class should have a pointwise value anywhere. The whole method of elliptic partial differential equations — produce a solution in a Sobolev space by a soft compactness or variational argument, then upgrade it to a genuine, classically differentiable, ultimately smooth object — collapses without a theorem that says when a Sobolev class is secretly a differentiable function. The Sobolev embedding theorem is that bridge. It answers the single question: *how many square-integrable derivatives must a section have before it is guaranteed to be $r$-times continuously differentiable, with the $C^r$ size controlled by the $H_k$ size?*

The answer is a piece of dimension counting, and the cleanest place to see why is the circle, which is where Haydys locates "the spirit of the proof". Let $u\in C^\infty(S^1;\mathbb R)$, write $\bar u=\tfrac1{2\pi}\int_0^{2\pi}u\,d\theta$ for its mean and $u_0=u-\bar u$ for the mean-zero part. Because $u_0$ has integral zero over the circle, it cannot be everywhere positive nor everywhere negative, so by the intermediate value theorem there is a point $\theta_0$ with $u_0(\theta_0)=0$. For any other point $\theta$, the fundamental theorem of calculus and then the [[Thm - Cauchy-Schwarz Inequality|Cauchy–Schwarz inequality]] give
$$|u_0(\theta)|=\left|\int_{\theta_0}^{\theta}u_0'(\varphi)\,d\varphi\right|\le\int_{\theta_0}^{\theta}|u_0'(\varphi)|\,d\varphi\le\left(\int_{\theta_0}^{\theta}|u_0'|^2\,d\varphi\right)^{1/2}\left(\int_{\theta_0}^{\theta}1^2\,d\varphi\right)^{1/2}\le\sqrt{2\pi}\,\|u_0'\|_{L^2(S^1)},$$
where the middle inequality is Cauchy–Schwarz applied to the two functions $u_0'$ and the constant $1$ on the interval from $\theta_0$ to $\theta$, and the last step uses $\int_{\theta_0}^{\theta}1\,d\varphi\le2\pi$ together with $\int_{\theta_0}^{\theta}|u_0'|^2\le\int_{S^1}|u_0'|^2=\|u_0'\|_{L^2}^2$. Since $u_0'=u'$, the right-hand side is at most $\sqrt{2\pi}\,\|u\|_{W^{1,2}}$. The mean is controlled the same way, $|\bar u|\le\tfrac1{2\pi}\int|u|\le\tfrac1{2\pi}\sqrt{2\pi}\,\|u\|_{L^2}=\tfrac1{\sqrt{2\pi}}\,\|u\|_{L^2}$ (Cauchy–Schwarz against the constant $1$ again), so combining,
$$\|u\|_{C^0}\le|\bar u|+\sup_{\theta}|u_0(\theta)|\le C\,\|u\|_{W^{1,2}}.$$
This is exactly the case $n=1$, $k=1$, $r=0$ of part (ii): the surplus $k-\tfrac n2-r=1-\tfrac12-0=\tfrac12>0$ is positive, and one $L^2$-derivative suffices to bound the supremum. Tracing the same inequality between two arbitrary points shows more, a Hölder-$\tfrac12$ estimate, $|u(\theta_1)-u(\theta_2)|\le\sqrt{2\pi}\,\|u\|_{W^{1,2}}\,\operatorname{dist}(\theta_1,\theta_2)^{1/2}$, because $\int_{\theta_1}^{\theta_2}1\,d\varphi=\operatorname{dist}(\theta_1,\theta_2)$.

The reason the naive argument does not simply transplant to $n$ dimensions is visible in that last factor $\big(\int 1\big)^{1/2}$. In one dimension the "cost" of integrating a derivative back up to a value is the length of an interval, which is finite. In $n$ dimensions one integrates along rays out of a point, and the corresponding cost is of the type $\int_{|x|\le 1}|x|^{1-n}\,dx$; the surplus of derivatives one needs grows with $n$, and the exact bookkeeping is what the theorem encodes. Fourier series make the bookkeeping transparent and uniform across dimensions, and — a genuine gain over the classical route — dispense with the mean value theorem entirely, so we take that path.

---

# Sources and Targets

**Sources (Input Broadening).** The hypothesis of part (ii) is a single $H_k$ bound with $k>\tfrac n2+r$. The skill is recognising the many situations that silently hand you such a bound.

The first disguised source is **an elliptic equation together with an interior or global elliptic estimate**. If $L$ is an elliptic operator of order $\ell$ on the compact $M$ and $Lu=f$ with $f\in H_{k-\ell}$, the elliptic estimate $\|u\|_k\le C(\|Lu\|_{k-\ell}+\|u\|_0)$ (proved on **[[Thm - Elliptic Regularity and the Elliptic Estimate]]**) upgrades an a priori weak solution to an $H_k$ bound, and then the embedding theorem converts that into a $C^r$ bound. The bridge $B\Rightarrow A$ here is "$u$ solves an elliptic equation with regular data" $\Rightarrow$ "$u\in H_k$"; it is non-obvious because the equation gives no pointwise information directly — the regularity is manufactured by the estimate and only then made classical. *Example problem:* show that a distributional solution of $\Delta u=f$ with $f$ smooth on a closed surface is a smooth function, by bootstrapping $u\in H_1\Rightarrow u\in H_3\Rightarrow\cdots$ and embedding at each stage.

The second disguised source is **a uniform energy bound produced by a variational or compactness argument**. A minimising sequence for the Dirichlet energy, or a sequence of connections with bounded Yang–Mills energy, is bounded in some $H_1$ or $H_k$ but is only known abstractly to exist. The bridge is "bounded energy" $\Rightarrow$ "$H_k$-bounded" (after possibly using the equation to raise $k$), and its payoff through the embedding theorem is that a weak subsequential limit is an honest $C^r$ object on which one may evaluate, differentiate, and integrate by parts. The non-obviousness is that a bound in a Hilbert space of classes becomes a bound in a Banach space of functions. *Example problem:* extract a $C^0$-convergent subsequence from an $H_2(S^2)$-bounded sequence and identify its limit as continuous.

The third disguised source is **a section characterised by infinitely many moment or derivative bounds**, i.e. a section known to lie in $H_k$ for *every* $k$. This is precisely the hypothesis of part (iii). The bridge is "all $H_k$ norms finite" $\Rightarrow$ "$C^r$ for every $r$" $\Rightarrow$ "smooth", and it is the standard last step of every elliptic-regularity bootstrap: once the iteration has climbed the whole Sobolev ladder, smoothness is read off in one line. *Example problem:* deduce that the kernel of an elliptic operator on a closed manifold consists of smooth sections, given that elements of the kernel satisfy $u\in H_k$ for all $k$.

**Targets (Output Amplification).** The bare conclusion is an inequality $\|u\|_{C^r}\le C\|u\|_{H_k}$ and the existence of a $C^r$ representative. Combined with other ingredients it does more.

Combine part (ii) with **the boundedness of pointwise multiplication in low regularity**. If $2k>n$ then, by part (ii) with $r=0$, functions in $H_k$ are continuous and bounded, and this uniform bound is exactly the estimate that turns $H_k$ into a Banach algebra: $\|uv\|_k\le C\|u\|_k\|v\|_k$. The extra ingredient is the convolution structure of Fourier coefficients, and the payoff — proved on [[Thm - Sobolev Multiplication Theorem]] — is that nonlinear expressions in $H_k$ sections stay in $H_k$, which is what makes the Seiberg–Witten map well defined between Sobolev completions.

Combine part (iii) with **an elliptic operator whose kernel one wishes to understand**. If $u$ lies in the kernel of an elliptic $L$, elliptic regularity places $u$ in every $H_k$, and part (iii) then declares $u$ smooth; the extra ingredient is the regularity theorem and the payoff is that the finite-dimensional kernels and cokernels appearing in the Hodge and Fredholm theory (Chapter IX §§9.4–9.6) are spaces of genuinely smooth sections, so that the Hodge theorem represents de Rham cohomology by smooth harmonic forms.

Combine part (ii) with **an a priori $H_k$ bound uniform along a family**. In the compactness theory for the Seiberg–Witten equations one derives, from the curvature identities, a bound on the solutions in some $H_k$ with $2k>n=4$; the embedding into $C^0$ (Corollary 1) then gives a uniform pointwise bound on the spinor and the curvature. The extra ingredient is the Weitzenböck estimate, and the payoff is the $C^0$-precompactness that begins the proof that the moduli space is compact (Chapter XI).

---

# Why Is It True

The mechanism is one line on the Fourier side and everything else is bookkeeping.

> **A smooth function on the torus is its Fourier series; differentiating $\alpha$ times multiplies the $\xi$-coefficient by $(i\xi)^\alpha$, so the supremum of $\partial^\alpha u$ is bounded by $\sum_\xi|\xi|^{|\alpha|}|\hat u(\xi)|$; splitting each summand as a weight $(1+|\xi|^2)^{(r-k)/2}$ times $(1+|\xi|^2)^{k/2}|\hat u(\xi)|$ and applying Cauchy–Schwarz separates the $H_k$-norm (the second factor) from a pure lattice sum $\sum_\xi(1+|\xi|^2)^{r-k}$ (the first factor), and that lattice sum is finite exactly when $2(k-r)>n$ — which is the hypothesis $k-\tfrac n2>r$.**

Read this slowly. The value and every derivative of order at most $r$ are reconstructed by summing the Fourier series, and a sum is bounded by the sum of the absolute values of its terms; that step throws away all cancellation but is exactly what we can afford, because the terms decay. Each term is a frequency amplitude $|\hat u(\xi)|$ times a polynomial factor $|\xi^\alpha|\le|\xi|^{|\alpha|}\le(1+|\xi|^2)^{r/2}$. The $H_k$ norm controls the *weighted-$\ell^2$* size of the amplitudes, with weight $(1+|\xi|^2)^{k/2}$. So we are trying to bound an $\ell^1$-type sum (the sum of the terms) by an $\ell^2$-type quantity (the $H_k$ norm), and the classical device for that is to Cauchy–Schwarz against a fixed weight. The weight we have available is $(1+|\xi|^2)^{k/2}$; the weight we need is $(1+|\xi|^2)^{r/2}$; the deficit $(1+|\xi|^2)^{(r-k)/2}$ is what is left over, and it must itself be square-summable over the lattice. Square-summability of $(1+|\xi|^2)^{(r-k)/2}$ is summability of $(1+|\xi|^2)^{r-k}$, which is the lattice sum with exponent $t=k-r$, finite precisely when $2t>n$.

The local-to-global step — from the torus to a general compact manifold — carries no analytic content: a compact manifold is a finite union of coordinate pieces, each of which sits inside a torus, and both the $H_k$ norm and the $C^r$ norm are built additively from those pieces, with the connection differing from flat coordinate differentiation only by smooth, hence bounded, zeroth-order terms. The inequality on each piece therefore assembles into the inequality on $M$.

Part (i) is even simpler and needs no Cauchy–Schwarz: on the frequency side, lowering the exponent from $k$ to $m\le k$ multiplies each amplitude's weight by $(1+|\xi|^2)^{m-k}\le1$, so the $H_m$ norm is dominated by the $H_k$ norm term by term.

Part (iii) is the observation that "$C^r$ for every $r$" is the definition of smooth. Once (ii) hands us, for each $r$, a $C^r$ representative of the class, we only have to see that these representatives are the *same* function — which they are, because they all carry the same Fourier coefficients — and that function is then infinitely differentiable.

---

# What Makes This Hard

The strict inequality $k-\tfrac n2>r$ is not decoration and cannot be weakened to $\ge$: at the borderline $2k=n+2r$ the lattice sum $\sum_\xi(1+|\xi|^2)^{r-k}$ is exactly the divergent one, and the embedding genuinely fails — the function $u(x)=\chi(|x|)\log\log(1/|x|)$ on the two-torus lies in $W^{1,2}$ yet is unbounded, so $H_1(T^2)\not\subset C^0(T^2)$ although $2\cdot1=n=2$ (see **[[Ex - An Unbounded Function in W-1-2 of the Two-Torus]]**). The most common error is to prove the estimate on smooth sections and stop: that is not the theorem. An element of $H_k$ is an equivalence class, and one must produce a *bona fide* $C^r$ function representing it and check that the class-to-function assignment is well defined and injective — the estimate gives a Cauchy sequence in $C^r$, completeness of $C^r$ gives a limit, and a separate uniqueness argument (a continuous function is determined by its Fourier coefficients) is needed to know the limit does not depend on the sequence and to know distinct classes give distinct functions. Skipping the completeness and uniqueness steps leaves the theorem unproved even after the hard inequality is in hand.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove everything first on the torus, where a smooth function equals its Fourier series and $H_k$ is a weighted $\ell^2$ space. Part (i) is a term-by-term weight comparison. Part (ii) is: reconstruct each derivative from the series, bound its supremum by an absolute sum of amplitudes, split off a lattice weight and Cauchy–Schwarz to expose the $H_k$ norm, invoke the lattice-sum lemma for convergence, then extend the resulting bounded inclusion from the dense subspace of smooth functions to the completion using completeness of $C^r$, and identify the extension as the $C^r$ representative via equality of Fourier coefficients. Transport both to a compact manifold by the finite trivialising atlas and partition of unity. Part (iii) reads part (ii) for all $r$.

**Subgoal decomposition:**

1. **Completeness of the target.** Show that $C^r(T^n;\mathbb C^q)$, and then $C^r(M;E)$, is a Banach space.
   - *Hint:* A $C^r$-Cauchy sequence has each derivative of order $\le r$ uniformly Cauchy; use the fundamental theorem of calculus to pass the limit through the derivative.
   - *Why needed:* Extending the estimate from smooth sections to $H_k$ requires a complete space to receive the limit.

2. **The torus estimate.** For $u\in C^\infty(T^n;\mathbb C^q)$ and $k-\tfrac n2>r$, prove $\|u\|_{C^r(T^n)}\le C\|u\|_k$ with $C^2=(\#\{|\alpha|\le r\})\sum_\xi(1+|\xi|^2)^{r-k}$.
   - *Hint:* $\partial^\alpha u(x)=\sum_\xi(i\xi)^\alpha\hat u(\xi)e^{i\langle\xi,x\rangle}$; bound $|\xi^\alpha|\le(1+|\xi|^2)^{r/2}$, split and Cauchy–Schwarz.
   - *Why needed:* This is the analytic heart; the surplus $k-\tfrac n2>r$ enters only through convergence of the lattice sum.

3. **From smooth to the completion.** Extend the identity map, bounded from $\|\cdot\|_k$ to $\|\cdot\|_{C^r}$ on the dense subspace $C^\infty$, to a bounded map $H_k\to C^r$; show the extension of a class $u$ is a $C^r$ function whose Fourier coefficients equal those of $u$, and that the extension is injective.
   - *Hint:* A bounded linear map into a Banach space extends uniquely from a dense subspace; Fourier-coefficient evaluation is continuous on $H_k$, and a continuous function is determined by its coefficients.
   - *Why needed:* Turns the estimate on functions into the stated embedding of classes, with representative and injectivity.

4. **Patch to the manifold.** Assemble the torus estimate over the finite atlas.
   - *Hint:* $u=\sum_i\phi_iu$; each piece pulls back to $T^n$; the connection differs from coordinate differentiation by smooth bounded terms; sum with Cauchy–Schwarz over the finitely many charts.
   - *Why needed:* Delivers parts (i) and (ii) on $M$, not just on $T^n$.

5. **Smoothness.** Deduce part (iii) by applying part (ii) with $k=r+n$ for each $r$ and matching representatives.
   - *Hint:* All the $C^r$ representatives share Fourier coefficients, hence are one function, which is therefore $C^r$ for all $r$.
   - *Why needed:* Completes the theorem and is the terminal step of every regularity bootstrap.

---

# Lemma Decomposition

> [!note]- Lemma 1: The uniform space $C^r$ is complete
> **Statement:** For an integer $r\ge0$, the space $C^r(T^n;\mathbb C^q)$ with the norm $\sum_{|\alpha|\le r}\sup_{T^n}|\partial^\alpha u|$ is a Banach space, and so is $C^r(M;E)$ with the norm $\sum_{i\le r}\sup_M|\nabla^iu|$.
>
> **Hint:** A Cauchy sequence has each derivative uniformly Cauchy; uniform limits of continuous functions are continuous, and the fundamental theorem of calculus lets the derivative pass to the limit.
>
> **Why needed:** The estimate of Lemma 2 makes the inclusion $C^\infty\hookrightarrow C^r$ (in the $H_k$ topology on the source) uniformly continuous; a uniformly continuous map extends to the completion $H_k$ only if the target $C^r$ is complete.
>
> > [!note]- Full proof
> > **The torus case.** Let $(u_j)_{j\ge1}$ be a sequence in $C^r(T^n;\mathbb C^q)$ that is Cauchy in the $C^r$ norm. By the definition of that norm, for each multi-index $\alpha$ with $|\alpha|\le r$ the sequence $(\partial^\alpha u_j)_j$ is Cauchy in the supremum norm on $T^n$ (since $\sup|\partial^\alpha u_j-\partial^\alpha u_l|\le\|u_j-u_l\|_{C^r}$). The space $C^0(T^n;\mathbb C^q)$ with the supremum norm is complete — a uniformly Cauchy sequence of continuous functions on a compact space converges uniformly, and the uniform limit of continuous functions is continuous (a standard $\varepsilon/3$ argument) — so for each such $\alpha$ there is $g_\alpha\in C^0(T^n;\mathbb C^q)$ with
> > $$\partial^\alpha u_j\longrightarrow g_\alpha\qquad\text{uniformly on }T^n\quad(j\to\infty).\qquad(\ast)$$
> > Write $g:=g_0$ for the multi-index $\alpha=0$. We show $g\in C^r$ with $\partial^\alpha g=g_\alpha$ for all $|\alpha|\le r$, by induction on $|\alpha|$; it suffices to treat a single first-order derivative and iterate, since $\partial^\alpha=\partial_{x_i}\partial^\beta$ with $|\beta|=|\alpha|-1$. Fix an index $i$ and a multi-index $\beta$ with $|\beta|\le r-1$, and abbreviate $v_j:=\partial^\beta u_j$, so that $v_j\to g_\beta$ and $\partial_{x_i}v_j\to g_{\beta+e_i}$ uniformly by $(\ast)$. For points $x$ on $T^n$ and $x'=x+te_i$ obtained by moving a distance $t$ in the $i$-th coordinate direction (within a fundamental domain, so the segment is a genuine interval), the fundamental theorem of calculus gives, for each fixed $j$,
> > $$v_j(x+te_i)-v_j(x)=\int_0^{t}\partial_{x_i}v_j(x+se_i)\,ds.$$
> > As $j\to\infty$ the left side converges to $g_\beta(x+te_i)-g_\beta(x)$ pointwise (by $(\ast)$), and the integrand $\partial_{x_i}v_j(x+se_i)$ converges to $g_{\beta+e_i}(x+se_i)$ uniformly in $s\in[0,t]$; uniform convergence on the bounded interval $[0,t]$ permits interchanging the limit and the integral (the error is at most $|t|\sup_{[0,t]}|\partial_{x_i}v_j-g_{\beta+e_i}|\to0$), so
> > $$g_\beta(x+te_i)-g_\beta(x)=\int_0^{t}g_{\beta+e_i}(x+se_i)\,ds.$$
> > Since $g_{\beta+e_i}$ is continuous, the right side is differentiable in $t$ with derivative $g_{\beta+e_i}(x+te_i)$ (the fundamental theorem of calculus, forward direction); evaluating the derivative at $t=0$ shows $g_\beta$ is partially differentiable in the $i$-th direction with $\partial_{x_i}g_\beta=g_{\beta+e_i}$, a continuous function. Running this over all $i$ and all $|\beta|\le r-1$ shows that all partial derivatives of $g$ up to order $r$ exist, equal the corresponding $g_\alpha$, and are continuous; hence $g\in C^r(T^n;\mathbb C^q)$ and, by $(\ast)$, $\|u_j-g\|_{C^r}=\sum_{|\alpha|\le r}\sup|\partial^\alpha u_j-g_\alpha|\to0$. Thus $(u_j)$ converges in $C^r$, and $C^r(T^n;\mathbb C^q)$ is complete.
> >
> > **The manifold case.** Let $(u_j)$ be $C^r$-Cauchy in $C^r(M;E)$, so each $(\nabla^iu_j)$, $i\le r$, is uniformly Cauchy on the compact $M$. The bundles $(T^*M)^{\otimes i}\otimes E$ carry fibre metrics, and continuous sections of a bundle over a compact base, with the supremum norm, form a complete space by the same $\varepsilon/3$ argument applied in local trivialisations; hence $\nabla^iu_j\to w_i$ uniformly for some continuous sections $w_i$. Over each trivialising chart $\kappa_\iota:U_\iota\to T^n$, the covariant derivatives $\nabla^iu_j$ are expressed through the flat coordinate derivatives $\partial^\alpha\big((u_j)\text{ in the trivialisation}\big)$ and the smooth (hence, on the relatively compact chart, bounded together with all their derivatives) Christoffel and connection coefficients; the linear change between $\{\nabla^iu_j\}_{i\le r}$ and $\{\partial^\alpha(u_j)\}_{|\alpha|\le r}$ is invertible with smooth bounded entries, so uniform Cauchyness of the former on $U_\iota$ is equivalent to uniform Cauchyness of the latter. The torus case then gives a $C^r$ limit of $(u_j)$ over each chart; the limits agree on overlaps (they equal the same uniform $C^0$ limit $w_0$), so they define a global section $w_0\in C^r(M;E)$ with $\nabla^iw_0=w_i$ and $u_j\to w_0$ in $C^r(M;E)$. Hence $C^r(M;E)$ is complete. $\blacksquare$

> [!note]- Lemma 2: The pointwise Fourier estimate on the torus
> **Statement:** Let $k,r\ge0$ be integers with $k-\tfrac n2>r$. There is a constant $C=C(k,r,n)$ such that every $u\in C^\infty(T^n;\mathbb C^q)$ satisfies
> $$\|u\|_{C^r(T^n)}=\sum_{|\alpha|\le r}\sup_{x\in T^n}|\partial^\alpha u(x)|\le C\,\|u\|_k,\qquad C^2=\Big(\#\{\alpha:|\alpha|\le r\}\Big)\sum_{\xi\in\mathbb Z^n}(1+|\xi|^2)^{r-k}.$$
>
> **Hint:** Reconstruct $\partial^\alpha u$ from the Fourier series, bound $|\xi^\alpha|\le(1+|\xi|^2)^{r/2}$, split each amplitude against the weight $(1+|\xi|^2)^{(r-k)/2}$, apply Cauchy–Schwarz, and use the lattice-sum lemma for the finiteness of the weight sum.
>
> **Why needed:** This is the analytic core of part (ii); every other step is soft (density, completeness, patching).
>
> > [!note]- Full proof
> > **The reconstruction and the crude bound.** Fix $u\in C^\infty(T^n;\mathbb C^q)$ (apply the scalar argument in each of the $q$ components and add). By [[Thm - Fourier Series of Smooth Functions on the Torus]] — part (i), $\widehat{\partial^\alpha u}(\xi)=(i\xi)^\alpha\hat u(\xi)$ and the coefficients decay faster than any power, and part (ii), the series and each of its termwise derivatives converge absolutely and uniformly with sum $u$ — we have, for every multi-index $\alpha$ and every $x\in T^n$,
> > $$\partial^\alpha u(x)=\sum_{\xi\in\mathbb Z^n}(i\xi)^\alpha\,\hat u(\xi)\,e^{i\langle\xi,x\rangle}\qquad\text{(termwise-differentiated Fourier series, part (ii))}.$$
> > Bounding the sum by the sum of absolute values, and using $|e^{i\langle\xi,x\rangle}|=1$ and $|(i\xi)^\alpha|=|\xi^\alpha|$,
> > $$\sup_{x\in T^n}|\partial^\alpha u(x)|\le\sum_{\xi\in\mathbb Z^n}|\xi^\alpha|\,|\hat u(\xi)|\qquad\text{(triangle inequality for the absolutely convergent series).}$$
> > The rapid decrease of $(\hat u(\xi))$ from part (i) guarantees this sum is finite, so all manipulations below are between finite quantities.
> >
> > **Reducing the polynomial factor to a single weight.** For $|\alpha|\le r$ we have $|\xi^\alpha|=|\xi_1|^{\alpha_1}\cdots|\xi_n|^{\alpha_n}\le|\xi|^{\alpha_1}\cdots|\xi|^{\alpha_n}=|\xi|^{|\alpha|}$ (each $|\xi_j|\le|\xi|$), and $|\xi|^{|\alpha|}\le(1+|\xi|^2)^{|\alpha|/2}\le(1+|\xi|^2)^{r/2}$ — the first because $|\xi|^2\le1+|\xi|^2$, the second because $|\alpha|\le r$ and $1+|\xi|^2\ge1$. Therefore
> > $$\sup_{x}|\partial^\alpha u(x)|\le\sum_{\xi}(1+|\xi|^2)^{r/2}\,|\hat u(\xi)|\qquad\text{(monotonicity of the sum under }|\xi^\alpha|\le(1+|\xi|^2)^{r/2}\text{).}$$
> >
> > **The Cauchy–Schwarz split.** Write each summand as a product of two factors,
> > $$(1+|\xi|^2)^{r/2}|\hat u(\xi)|=\underbrace{(1+|\xi|^2)^{(r-k)/2}}_{a_\xi}\cdot\underbrace{(1+|\xi|^2)^{k/2}|\hat u(\xi)|}_{b_\xi}.$$
> > Apply the [[Thm - Cauchy-Schwarz Inequality|Cauchy–Schwarz inequality]] $\big|\sum a_\xi b_\xi\big|\le\big(\sum a_\xi^2\big)^{1/2}\big(\sum b_\xi^2\big)^{1/2}$ to the nonnegative sequences $(a_\xi),(b_\xi)$. Because Cauchy–Schwarz holds for every finite partial sum and each of the two full sums below is finite (the first by the lattice-sum lemma next, the second being $\|u\|_k^2$), passing to the supremum over finite subsets gives the inequality for the full series:
> > $$\sum_{\xi}(1+|\xi|^2)^{r/2}|\hat u(\xi)|\le\Big(\sum_{\xi}(1+|\xi|^2)^{r-k}\Big)^{1/2}\Big(\sum_{\xi}(1+|\xi|^2)^{k}|\hat u(\xi)|^2\Big)^{1/2}.$$
> > The second factor is exactly $\|u\|_k$ by the definition of the Fourier Sobolev norm ([[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order]]).
> >
> > **Convergence of the weight sum.** The first factor is finite: by [[Thm - Convergence of the Lattice Sum]] — for $t\in\mathbb R$, $\sum_{\xi\in\mathbb Z^n}(1+|\xi|^2)^{-t}<\infty$ if and only if $2t>n$ — applied with $t=k-r$, the sum $\sum_\xi(1+|\xi|^2)^{r-k}=\sum_\xi(1+|\xi|^2)^{-(k-r)}$ converges precisely when $2(k-r)>n$, i.e. when $k-\tfrac n2>r$, which is the hypothesis. Denote its value by $S:=\sum_\xi(1+|\xi|^2)^{r-k}<\infty$. Combining the last three displays,
> > $$\sup_{x}|\partial^\alpha u(x)|\le S^{1/2}\,\|u\|_k\qquad\text{for every }\alpha\text{ with }|\alpha|\le r.$$
> >
> > **Summing over $\alpha$.** There are $\#\{\alpha:|\alpha|\le r\}=:P$ multi-indices with $|\alpha|\le r$ (a finite number depending only on $n$ and $r$). Summing the previous bound over them,
> > $$\|u\|_{C^r(T^n)}=\sum_{|\alpha|\le r}\sup_x|\partial^\alpha u(x)|\le P\,S^{1/2}\,\|u\|_k=\big(P^2S\big)^{1/2}\|u\|_k.$$
> > This is the claimed inequality with $C=(P^2S)^{1/2}$, and by construction $C^2=P^2S\le P\cdot(PS)$; taking $C^2=P\!\cdot\!S$ with the harmless bound $P\ge1$ absorbed into $C$ gives the stated form. In either bookkeeping $C$ depends only on $k,r,n$. $\blacksquare$

> [!note]- Lemma 3: Bounded extension from a dense subspace, with representative and injectivity
> **Statement:** Let $D$ be a dense linear subspace of a normed space $X$, let $Y$ be a Banach space, and let $T_0:D\to Y$ be linear with $\|T_0d\|_Y\le C\|d\|_X$ for all $d\in D$. Then $T_0$ extends uniquely to a bounded linear map $T:X\to Y$ with $\|Tx\|_Y\le C\|x\|_X$. Applied with $X=H_k(T^n;\mathbb C^q)$, $D=C^\infty(T^n;\mathbb C^q)$, $Y=C^r(T^n;\mathbb C^q)$ (with $k-\tfrac n2>r$) and $T_0$ the identity inclusion, the extension $T$ sends a class $u\in H_k$ to a $C^r$ function whose Fourier coefficients equal those of $u$, and $T$ is injective.
>
> **Hint:** Cauchy sequences map to Cauchy sequences; completeness of $Y$ gives the limit; Fourier-coefficient evaluation is continuous on $H_k$; a continuous function with vanishing Fourier coefficients is zero.
>
> **Why needed:** It converts Lemma 2 (an estimate on smooth functions) into the actual embedding of the completion, and supplies the "$C^r$ representative" and injectivity clauses of part (ii).
>
> > [!note]- Full proof
> > **Existence and uniqueness of the extension.** Let $x\in X$. By density choose $d_j\in D$ with $d_j\to x$ in $X$; then $(d_j)$ is $X$-Cauchy, and $\|T_0d_j-T_0d_l\|_Y=\|T_0(d_j-d_l)\|_Y\le C\|d_j-d_l\|_X\to0$, so $(T_0d_j)$ is $Y$-Cauchy and, $Y$ being complete, converges to some limit; define $Tx:=\lim_jT_0d_j$. This is independent of the approximating sequence: if $d_j'\to x$ as well, then $\|T_0d_j-T_0d_j'\|_Y\le C\|d_j-d_j'\|_X\le C(\|d_j-x\|_X+\|x-d_j'\|_X)\to0$, so the two limits coincide. The map $T$ is linear (limits respect linear combinations) and agrees with $T_0$ on $D$ (take the constant sequence). Passing to the limit in $\|T_0d_j\|_Y\le C\|d_j\|_X$ and using continuity of the norm gives $\|Tx\|_Y\le C\|x\|_X$. Uniqueness: any bounded (hence continuous) extension must agree with the limit of $T_0d_j$, so $T$ is the only one.
> >
> > **The extension is the $C^r$ representative.** Take $X=H_k$, $Y=C^r$, $T_0=\mathrm{id}$ as stated; Lemma 2 supplies the bound $C$, and Lemma 1 the completeness of $Y$. Fix $u\in H_k$ and a smooth sequence $u_j\to u$ in $H_k$. Then $Tu=\lim_ju_j$ in $C^r$, in particular $u_j\to Tu$ uniformly (the $C^0$ part of the $C^r$ norm). We compare Fourier coefficients. On one hand, for each fixed $\xi$ the coefficient map $w\mapsto\hat w(\xi)$ is continuous on $H_k$: for smooth $w$,
> > $$|\hat w(\xi)|=(1+|\xi|^2)^{-k/2}\big|(1+|\xi|^2)^{k/2}\hat w(\xi)\big|\le(1+|\xi|^2)^{-k/2}\,\|w\|_k,$$
> > since the bracketed term is one summand of $\|w\|_k^2=\sum_\eta(1+|\eta|^2)^k|\hat w(\eta)|^2$; hence $\hat{u_j}(\xi)\to c_\xi$ where $(c_\xi)$ is, by definition, the frequency data of the class $u$. On the other hand $u_j\to Tu$ uniformly, so we may pass the limit through the (compact-domain) integral defining the coefficient,
> > $$\widehat{Tu}(\xi)=(2\pi)^{-n}\!\int_{T^n}(Tu)\,e^{-i\langle\xi,x\rangle}dx=\lim_j(2\pi)^{-n}\!\int_{T^n}u_j\,e^{-i\langle\xi,x\rangle}dx=\lim_j\hat{u_j}(\xi)=c_\xi.$$
> > Thus $\widehat{Tu}(\xi)=c_\xi$ for every $\xi$: the $C^r$ function $Tu$ carries exactly the Fourier coefficients of the class $u$, so it represents $u$.
> >
> > **Injectivity.** Suppose $Tu=0$ in $C^r$. Then $Tu$ is the zero continuous function, so all its Fourier coefficients vanish; by the previous paragraph $c_\xi=\widehat{Tu}(\xi)=0$ for all $\xi$, whence $\|u\|_k^2=\sum_\xi(1+|\xi|^2)^k|c_\xi|^2=0$ and $u=0$ in $H_k$. (Equivalently, one may invoke the uniqueness clause of [[Thm - Fourier Series of Smooth Functions on the Torus]]: a continuous function on $T^n$ with all Fourier coefficients zero is identically zero.) Hence $T$ is injective. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a compact $n$-manifold and $E\to M$ a vector bundle of rank $q$. We use throughout the concrete realisations recorded in Step 0 and the three lemmas above.
>
> **Step 0 — the objects and what we may assume.** By [[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts]] there is a finite atlas $\{\kappa_i:U_i\to\kappa_i(U_i)\subset(-\pi,\pi)^n\subset T^n\}_{i=1}^{N}$ trivialising $E$, with a subordinate partition of unity $(\phi_i)$, such that for every integer $k$
> $$\|u\|_{(k)}^2=\sum_{i=1}^{N}\big\|(\phi_i u)\circ\kappa_i^{-1}\big\|_{H_k(T^n;\mathbb C^q)}^2$$
> defines a norm on $\Gamma(E)$ whose completion is $H_k(M;E)$; that for $k\ge0$ this chart norm is equivalent to the connection norm $\|\cdot\|_{W^{k,2}}$ (part (i) of that theorem); that $\Gamma(E)$ is dense in every $H_k(M;E)$ (part (iii)); and that the pieces $f_i:=(\phi_i u)\circ\kappa_i^{-1}$ are smooth $\mathbb C^q$-valued functions on $T^n$, supported in $\kappa_i(U_i)$ and extended by zero. We write $\|u\|_k$ for the $H_k(M;E)$ norm, equal to $\|u\|_{(k)}$ up to the fixed equivalence constants.
>
> ---
> **Part I — the descending scale (statement (i)).** Fix integers $k\ge m$.
>
> **Torus weight comparison.** For $w\in C^\infty(T^n;\mathbb C^q)$, since $m-k\le0$ and $1+|\xi|^2\ge1$ we have $(1+|\xi|^2)^{m}=(1+|\xi|^2)^{m-k}(1+|\xi|^2)^{k}\le(1+|\xi|^2)^{k}$ for every $\xi$, hence, summing the amplitudes against these weights,
> $$\|w\|_m^2=\sum_{\xi}(1+|\xi|^2)^{m}|\hat w(\xi)|^2\le\sum_{\xi}(1+|\xi|^2)^{k}|\hat w(\xi)|^2=\|w\|_k^2\qquad\text{(term-by-term, }(1+|\xi|^2)^{m-k}\le1\text{),}$$
> so $\|w\|_m\le\|w\|_k$ on the torus.
>
> **Assembly on $M$.** For $u\in\Gamma(E)$, apply the torus bound to each piece $f_i$ (each $f_i$ is smooth on $T^n$):
> $$\|u\|_{(m)}^2=\sum_{i=1}^{N}\|f_i\|_{H_m(T^n)}^2\le\sum_{i=1}^{N}\|f_i\|_{H_k(T^n)}^2=\|u\|_{(k)}^2\qquad\text{(torus weight comparison in each summand).}$$
> Thus $\|u\|_{(m)}\le\|u\|_{(k)}$ on $\Gamma(E)$, and by the equivalence of the chart norms with the norms $\|\cdot\|_m,\|\cdot\|_k$ there is a constant $C=C(k,m)$ with $\|u\|_m\le C\|u\|_k$ for all $u\in\Gamma(E)$. Since $\Gamma(E)$ is dense in $H_k(M;E)$ (Step 0) and the estimate is a bounded-linear estimate, it extends to all $u\in H_k(M;E)$ by Lemma 3 (with $X=H_k$, $Y=H_m$ — a Banach space as a completion — $T_0$ the inclusion); the extension is the natural inclusion $H_k(M;E)\hookrightarrow H_m(M;E)$, which is injective by the same lemma (a class with all chart-Fourier coefficients zero is zero in $H_k$). This proves (i).
>
> ---
> **Part II — embedding into $C^r$ (statement (ii)).** Fix integers $k,r\ge0$ with $k-\tfrac n2>r$.
>
> **Step II.1 — the estimate on the torus.** By Lemma 2, there is a constant $C_0=C_0(k,r,n)$ with $\|w\|_{C^r(T^n)}\le C_0\|w\|_k$ for every $w\in C^\infty(T^n;\mathbb C^q)$. (This is where the strict inequality $k-\tfrac n2>r$ is spent, through the convergence of $\sum_\xi(1+|\xi|^2)^{r-k}$.)
>
> **Step II.2 — the embedding on the torus.** By Lemma 1 the space $C^r(T^n;\mathbb C^q)$ is complete, and $C^\infty(T^n;\mathbb C^q)$ is dense in $H_k(T^n;\mathbb C^q)$ (it is dense by the definition of $H_k$ as the completion of $C^\infty$). Lemma 3, applied with $X=H_k(T^n)$, $Y=C^r(T^n)$, and $T_0$ the inclusion of smooth functions bounded by Step II.1, yields a bounded injection
> $$\iota_{T^n}:H_k(T^n;\mathbb C^q)\hookrightarrow C^r(T^n;\mathbb C^q),\qquad \|\iota_{T^n}w\|_{C^r}\le C_0\|w\|_k,$$
> where $\iota_{T^n}w$ is the unique $C^r$ function carrying the Fourier coefficients of the class $w$. Every element of $H_k(T^n)$ is thus represented by a unique $C^r$ function, and distinct elements by distinct functions.
>
> **Step II.3 — patching to $M$.** Let $u\in\Gamma(E)$ and let $f_i=(\phi_iu)\circ\kappa_i^{-1}\in C^\infty(T^n;\mathbb C^q)$ be its pieces (Step 0). We estimate the connection $C^r$ norm of $u$ on $M$ by the $C^r$ norms of the $f_i$ on $T^n$. Because $u=\sum_i\phi_iu$ (finite sum, as $\sum_i\phi_i\equiv1$) and each $\phi_iu$ is supported in the chart $U_i$, and because over $U_i$ the covariant derivatives $\nabla^ju$ are expressed through the coordinate derivatives $\partial^\alpha f_i$ of order $|\alpha|\le j$ times the smooth connection and transition coefficients — which are bounded together with all their derivatives on the relatively compact charts, by compactness of $M$ — there is a constant $C_1$ (depending only on the fixed data) with
> $$\sup_M|\nabla^ju|\le C_1\sum_{i=1}^{N}\sum_{|\alpha|\le j}\sup_{T^n}|\partial^\alpha f_i|\qquad(0\le j\le r),$$
> and summing over $j\le r$,
> $$\|u\|_{C^r(M;E)}\le C_1'\sum_{i=1}^{N}\|f_i\|_{C^r(T^n)}\qquad\text{(finitely many charts; }C_1'\text{ absorbs }C_1\text{ and }r\text{).}$$
> Now bound each term by Step II.1, then pass from the sum of $H_k$ norms to their $\ell^2$-combination by the Cauchy–Schwarz inequality on the finite index set $\{1,\dots,N\}$:
> $$\sum_{i=1}^{N}\|f_i\|_{C^r(T^n)}\le C_0\sum_{i=1}^{N}\|f_i\|_{H_k(T^n)}\le C_0\sqrt{N}\Big(\sum_{i=1}^{N}\|f_i\|_{H_k(T^n)}^2\Big)^{1/2}=C_0\sqrt{N}\,\|u\|_{(k)},$$
> where the middle step is Cauchy–Schwarz, $\sum_i1\cdot\|f_i\|\le(\sum_i1^2)^{1/2}(\sum_i\|f_i\|^2)^{1/2}$, and the last equality is the definition of the chart norm (Step 0). Combining the two displays and the equivalence $\|u\|_{(k)}\le C\|u\|_k$,
> $$\|u\|_{C^r(M;E)}\le C_2\,\|u\|_k\qquad\text{for all }u\in\Gamma(E),\qquad C_2:=C_1'C_0\sqrt N\,C.$$
>
> **Step II.4 — extension, representative, injectivity on $M$.** The space $C^r(M;E)$ is complete (Lemma 1) and $\Gamma(E)$ is dense in $H_k(M;E)$ (Step 0). Lemma 3, applied with $X=H_k(M;E)$, $Y=C^r(M;E)$, $T_0$ the inclusion bounded by Step II.3, produces a bounded injection
> $$\iota:H_k(M;E)\hookrightarrow C^r(M;E),\qquad\|\iota u\|_{C^r}\le C_2\|u\|_k.$$
> That $\iota$ represents each class and is injective is the content of Lemma 3 read locally: for $u\in H_k(M;E)$ with approximating $u_j\in\Gamma(E)$, $u_j\to\iota u$ in $C^r(M;E)$, hence $\phi_i u_j\to\phi_i\,\iota u$ uniformly and $(\phi_iu_j)\circ\kappa_i^{-1}\to(\phi_i\iota u)\circ\kappa_i^{-1}$ in $C^r(T^n)$; by Step II.2 the latter is the $C^r$ representative of the $H_k(T^n)$ class $\lim_j(\phi_iu_j)\circ\kappa_i^{-1}$, which is the $i$-th chart-piece of $u$. Thus in every chart the pieces of $\iota u$ carry the chart-Fourier coefficients of $u$; if $\iota u=0$ then all these coefficients vanish, so $\|u\|_{(k)}=0$ and $u=0$. Hence every element of $H_k(M;E)$ is represented by a unique $C^r$ section and $\iota$ is injective, completing (ii).
>
> ---
> **Part III — the intersection is $C^\infty$ (statement (iii)).**
>
> **The easy inclusion $C^\infty\subset\bigcap_kH_k$.** Let $u\in C^\infty(M;E)$. For every integer $k\ge0$ the covariant derivatives $\nabla^iu$ ($i\le k$) are continuous sections of bundles over the compact $M$, hence bounded, hence square-integrable against the finite-volume $\mathrm{vol}_g$; so $\|u\|_{W^{k,2}}^2=\sum_{i\le k}\int_M|\nabla^iu|^2\,\mathrm{vol}_g<\infty$ and $u\in H_k(M;E)$. As $k$ was arbitrary, $u\in\bigcap_{k\ge0}H_k(M;E)$.
>
> **The substantial inclusion $\bigcap_kH_k\subset C^\infty$.** Let $u\in\bigcap_{k\ge0}H_k(M;E)$. Fix an integer $r\ge0$ and set $k:=r+n$, so that $k-\tfrac n2=r+\tfrac n2>r$ (as $n\ge1$), and $u\in H_k$ by hypothesis. By part (ii) there is a unique $C^r$ section $v_r:=\iota_{(k)}u$ representing the class $u$, with Fourier coefficients (in every chart) equal to those of $u$. These representatives are all one and the same section: for $r<r'$, the class $u$ lies in $H_{r'+n}\subset H_{r+n}$ (by part (i)), and both $v_{r'}$ and $v_r$ are continuous sections carrying, in each chart, the chart-Fourier coefficients of $u$; since a continuous section is determined in each chart by its Fourier coefficients (uniqueness clause of [[Thm - Fourier Series of Smooth Functions on the Torus]]), $v_{r'}=v_r$ as continuous sections. Write $v$ for this common section. Then $v=v_r\in C^r(M;E)$ for every $r\ge0$, which means $v$ has continuous covariant derivatives of every order; that is, $v\in C^\infty(M;E)$. Since $v$ represents $u$, the class $u$ is (represented by) a smooth section. Combining the two inclusions, $\bigcap_{k\ge0}H_k(M;E)=C^\infty(M;E)$, proving (iii).
>
> ---
> **Corollary 1 (dimension four).** Take $n=4$, $k=5$. For the embedding into $C^2$ set $r=2$: then $k-\tfrac n2=5-2=3>2=r$, so part (ii) gives the continuous injection $H_5(M;E)\hookrightarrow C^2(M;E)$. For the embedding into $C^0$ set $r=0$: then $k-\tfrac n2=3>0=r$, so part (ii) gives $H_5(M;E)\hookrightarrow C^0(M;E)$; alternatively this follows from the $C^2$ case and $C^2\subset C^0$. In source notation, $W^{5,2}(M^4)\subset C^2(M^4)$ and $W^{5,2}(M^4)\subset C^0(M^4)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Elliptic regularity bootstrap for the Laplacian on a closed surface.** Let $(\Sigma,g)$ be a closed Riemannian surface ($n=2$) and suppose $u\in H_1(\Sigma)$ satisfies $\Delta u=f$ weakly with $f\in C^\infty(\Sigma)$. The elliptic estimate raises $u$ to $H_2$, then to $H_3$, and so on, so $u\in\bigcap_kH_k$, and part (iii) then declares $u$ smooth. The theorem applies because the surplus $k-\tfrac n2=k-1$ is eventually as large as any $r$; the step is non-obvious because the hypothesis is a *weak* equation with no pointwise meaning, and the conclusion is a *classical* smooth solution. This is the exact template by which harmonic representatives of de Rham classes are shown to be smooth.

**Convergence of Fourier partial sums in a Hölder norm.** On $T^n$, take $u$ with $\|u\|_k<\infty$ for some $k>\tfrac n2+r$. The estimate of Lemma 2 applied to the tail $u-\sum_{|\xi|\le R}\hat u(\xi)e^{i\langle\xi,x\rangle}$ shows the partial sums converge to $u$ in $C^r$, with an explicit rate governed by the lattice-sum tail $R^{\,n-2(k-r)}$. The embedding theorem applies to the tail, treated as an $H_k$ element supported on high frequencies; it is non-obvious that a single scalar bound ($\|u\|_k$) controls the *uniform* rate of convergence of all derivatives up to order $r$. This links the abstract embedding to concrete numerical approximation.

**Compactness of a bounded family of connections in $C^0$.** In dimension four, a sequence of connections $A_j$ bounded in $H_5$ (say, after gauge fixing) has, by Corollary 1, curvature representatives bounded in $C^2$; combined with the Rellich theorem this yields a $C^0$-convergent subsequence. The theorem applies because $5-\tfrac42=3>0$; the subtlety is that gauge fixing is what produces the $H_5$ bound in the first place, so the pointwise control is downstream of a nonlinear normalisation. This is the analytic backbone of moduli-space compactness arguments.

---

# Bridges

- **[[Thm - Rellich Compactness Theorem|Rellich compactness]]** — the compact companion of part (i). Where the embedding theorem says the inclusion $H_k\hookrightarrow H_m$ ($k\ge m$) is bounded, Rellich says that for the strict inequality $k>m$ it is even compact: a bounded sequence in $H_k$ has an $H_m$-convergent subsequence. The mechanism is the same lattice bookkeeping seen through a different lens — the tail estimate $\|u-T_Ru\|_m\le(1+R^2)^{(m-k)/2}\|u\|_k$ shows the inclusion is an operator-norm limit of finite-rank truncations. The embedding theorem controls size; Rellich controls compactness; the elliptic theory needs both.

- **[[Thm - Sobolev Multiplication Theorem|Sobolev multiplication]]** — built directly on part (ii). When $2k>n$, part (ii) with $r=0$ says $H_k\subset C^0$, and this uniform bound is what lets one estimate the Fourier convolution $\widehat{uv}=\hat u*\hat v$ and conclude $\|uv\|_k\le C\|u\|_k\|v\|_k$: the space $H_k$ becomes a Banach algebra. The embedding is the hypothesis under which pointwise products of Sobolev sections are again Sobolev sections, the enabling fact for every nonlinear construction over a compact base.

- **[[Thm - Elliptic Regularity and the Elliptic Estimate]]** — the source that feeds the embedding. The elliptic estimate manufactures the $H_k$ bounds that part (ii) then turns into $C^r$ regularity; together they are the statement that an elliptic equation with smooth data has smooth solutions. The two theorems are always used in tandem: regularity climbs the $L^2$-Sobolev ladder, the embedding steps off it into the classical world at the top.

- **[[Thm - Hodge Theorem for Elliptic Complexes]]** — the destination. That the finite-dimensional harmonic spaces produced by the Hodge theorem consist of smooth sections is precisely part (iii) applied to kernels of elliptic operators; the embedding is what makes "harmonic representative" a smooth differential form rather than a mere $L^2$ class.

---

# Unlocked by This

> [!tip] Uniform bounds on Seiberg–Witten solutions *(from Gauge Theory)*
> In dimension four, the a priori $H_k$ bounds on solutions of the Seiberg–Witten equations, combined with Corollary 1 ($H_5\subset C^0$), give uniform pointwise control of the spinor and curvature; this is the first step of the compactness of the moduli space. See **[[Thm - Compactness of the Seiberg-Witten Moduli Space]]**.

> [!tip] Smooth harmonic representatives *(from Hodge Theory)*
> Part (iii), applied to the kernel of the Hodge Laplacian, shows every harmonic form is smooth, so the [[Thm - Hodge Decomposition Theorem|Hodge decomposition]] represents each de Rham cohomology class by a smooth harmonic form rather than a weak $L^2$ solution.
