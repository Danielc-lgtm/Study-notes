---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts"
  - "Def - Compact Operator"
  - "Thm - Basic Properties of Compact Operators"
  - "Thm - Convergence of the Lattice Sum"
tags: [geometry, gauge-theory, analysis]
---

# Notation

Throughout, $M$ is a compact smooth manifold of dimension $n$, and $E \to M$ is a smooth [[Def - Vector Bundle|vector bundle]] of rank $r$. We work with the $L^2$-based Sobolev spaces $H_k(M; E) := W^{k,2}(M; E)$ of [[Def - Section of a Vector Bundle|sections]] of $E$, indexed by an integer $k \in \mathbb{Z}$; these are the Hilbertable spaces constructed on [[Def - Sobolev Space of Sections|the definition page]] for $k \ge 0$ and extended to all integers, and identified with a chart-and-Fourier model on [[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts|the charts page]]. Their norm is written $\lVert \cdot \rVert_k$, or $\lVert \cdot \rVert_{H_k}$ where the space must be named. For $k \ge 0$ the norm agrees, up to equivalence, with the connection norm $\lVert u \rVert_{W^{k,2}}^2 = \sum_{i=0}^k \int_M |\nabla^i u|^2 \, \mathrm{vol}$, where $\nabla^i u$ is the $i$-th iterated covariant derivative computed from a fixed Riemannian metric on $M$ and connections on $E$ and $T^*M$; by [[Thm - Sobolev Norms are Independent of the Metric and Connections up to Equivalence|the norm-equivalence theorem]] the resulting topology does not depend on these choices, so we suppress them.

The model space is the flat torus $T^n := \mathbb{R}^n / 2\pi \mathbb{Z}^n$. For a smooth function $u \in C^\infty(T^n; \mathbb{C}^r)$ the Fourier coefficients are $\hat u(\xi) := (2\pi)^{-n} \int_{T^n} u(x) e^{-i \langle \xi, x \rangle} \, dx$, indexed by $\xi \in \mathbb{Z}^n$, where $\langle \xi, x \rangle = \sum_{j=1}^n \xi_j x_j$ and $|\xi|^2 = \sum_j \xi_j^2$. On the torus the Sobolev norm of integer order $k$ is $\lVert u \rVert_k^2 = \sum_{\xi \in \mathbb{Z}^n} (1 + |\xi|^2)^k \, |\hat u(\xi)|^2$, and $H_k(T^n; \mathbb{C}^r)$ is the completion of $C^\infty(T^n; \mathbb{C}^r)$ in this norm, identified with the weighted sequence space $\{(c_\xi)_{\xi \in \mathbb{Z}^n} : \sum_\xi (1 + |\xi|^2)^k |c_\xi|^2 < \infty\}$; all of this is set up on [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order|the Fourier-space definition page]] and [[Thm - Sobolev Norms on the Torus via Fourier Coefficients|the torus-norm theorem]].

A bounded linear map $K : X \to Y$ between Banach spaces is a [[Def - Compact Operator|compact operator]] if the image $K(B)$ of the closed unit ball $B \subseteq X$ is relatively compact in $Y$; equivalently, since $Y$ is complete, if $K(B)$ is [[Def - Totally Bounded Metric Space|totally bounded]]; equivalently, every bounded sequence $(x_j)$ in $X$ has a subsequence $(x_{j_l})$ for which $(K x_{j_l})$ converges in $Y$. The inclusion (or embedding) $\iota_{k,m} : H_k \hookrightarrow H_m$, $k \ge m$, is the linear map that regards an element of the finer space $H_k$ as an element of the coarser space $H_m$; that it is well defined and bounded is part of [[Thm - Sobolev Embedding Theorem|the Sobolev embedding theorem]] and is re-established below.

> [!warning] Convention: general integrability exponent
> Haydys states the compactness result in the full Rellich–Kondrachov generality (his Theorem 136(ii), equation (137)): for a compact manifold $M$ of dimension $n$, the embedding $j : W^{k,p}(M; E) \hookrightarrow W^{m,q}(M; E)$ is a compact operator provided
> $$k - \tfrac{n}{p} > m - \tfrac{n}{q} \qquad \text{and} \qquad k > m .$$
> Following the series' design decision to prove everything for the Hilbertian exponent $p = q = 2$, we take $q = p = 2$, where the condition $k - \tfrac{n}{2} > m - \tfrac{n}{2}$ reduces to the single inequality $k > m$. The general-$p$ statement is recorded here as unproved context; a complete proof is in L. C. Evans, *Partial Differential Equations*, 2nd ed., §5.7 Theorem 1 (Rellich–Kondrachov), and R. A. Adams and J. J. F. Fournier, *Sobolev Spaces*, 2nd ed., Theorem 6.3. Every statement below uses only the case $p = q = 2$.

---

# Statement

> **Rellich compactness theorem.** Let $M$ be a compact smooth manifold, $E \to M$ a smooth vector bundle, and let $k > m$ be integers. Then the inclusion
> $$\iota_{k,m} : H_k(M; E) \hookrightarrow H_m(M; E)$$
> is a compact operator. Equivalently: every sequence $(u_j)_{j \in \mathbb{N}}$ that is bounded in $H_k(M; E)$ has a subsequence that converges in $H_m(M; E)$.

The archetype, $k = 1$, $m = 0$, reads: on a compact manifold, a sequence of sections whose $L^2$ norms and first covariant derivatives are uniformly $L^2$-bounded has an $L^2$-convergent subsequence. This is the compactness that the identity map on an infinite-dimensional Hilbert space conspicuously lacks, recovered by paying one derivative.

---

# Motivation

The whole analytic apparatus of gauge theory rests on turning bounds into convergent subsequences. One proves an *a priori* estimate — a bound on some Sobolev norm of a family of connections or spinors, obtained from an energy inequality, an elliptic estimate, or the equations themselves — and then wants to extract a limit that is again a solution. A bound alone does not give a limit: the closed unit ball of an infinite-dimensional Hilbert space is not compact, so a bounded sequence need not have any convergent subsequence at all. The Rellich theorem is precisely the device that repairs this, at the cost of one unit of regularity: a set bounded in the *finer* space $H_k$ is not merely bounded but *relatively compact* in the *coarser* space $H_m$. One trades a little smoothness for compactness, and compactness is what produces the limit.

This is the reason the theorem is invoked at two decisive points later in the series. It gives the finite-dimensionality of the kernel of an elliptic operator on a closed manifold — the seed of the whole Fredholm theory, hence of the index and of the Hodge theorem — because the elliptic estimate turns an $L^2$-bounded family of solutions into an $H_k$-bounded family, and Rellich then forces the unit ball of the kernel to be compact, which for a normed space means finite-dimensional. And it gives the compactness of the Seiberg–Witten moduli space: a sequence of solutions is bootstrapped, after gauge fixing, to a uniform bound in a high Sobolev norm, and Rellich extracts a subsequence converging in a lower norm, whose limit solves the equations by continuity.

Haydys states the result as part (ii) of his omnibus Theorem 136, and remarks that a full proof lies beyond his notes; he does record, in his Remark 138, the "spirit of the proof" in the one case $M = S^1$. There the argument runs through classical hard analysis: for $u \in C^\infty(S^1)$ one uses the mean value theorem to find a point where the mean-adjusted function vanishes, then Cauchy–Schwarz to obtain a Hölder-$\tfrac12$ modulus of continuity $|u(\theta_1) - u(\theta_2)| \le \sqrt{2\pi} \, \lVert u \rVert_{W^{1,2}} \, \mathrm{dist}(\theta_1, \theta_2)^{1/2}$, so that a $W^{1,2}$-bounded sequence is uniformly bounded and equicontinuous, and the **Arzelà–Ascoli theorem** delivers a uniformly convergent subsequence. We do not take this route. The Arzelà–Ascoli theorem is *not used anywhere on this page*: the Fourier construction of the Sobolev spaces makes a cleaner and dimension-independent argument available, in which the embedding is exhibited directly as a norm-limit of finite-rank operators. The reader who wants Haydys's classical $S^1$ argument in full will find it worked out as [[Ex - Sobolev Embedding on the Circle by Hand|the exercise reproducing Remark 138]]; here we prove the compactness in every dimension at once, and by a mechanism that we can point at.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of the theorem is only that a family of sections is bounded in $H_k(M; E)$; the skill is to recognise the many disguises in which such a bound arrives.

The first disguised source is **an a priori energy bound from a variational problem**. In the direct method of the calculus of variations one shows a functional is coercive, meaning its sublevel sets are bounded in some $H_k$; a minimising sequence therefore satisfies exactly the boundedness hypothesis. The non-obvious bridge is that coercivity — a statement purely about the *size* of the functional — hands one the compactness hypothesis for free, after which Rellich produces the convergent subsequence whose limit is the sought minimiser. *Example problem:* recover Dirichlet's principle, the motivating problem of [[Def - Sobolev Space of Sections|the whole chapter]] — minimise $E(u) = \tfrac12 \int_\Omega |\nabla u|^2$ subject to boundary data — by showing a minimising sequence is bounded in $H_1$ and extracting an $H_0 = L^2$-convergent subsequence.

The second disguised source is **an elliptic estimate applied to a family of solutions**. If $L$ is an elliptic operator of order $\ell$ and one already controls $\lVert u_j \rVert_{L^2}$ and $\lVert L u_j \rVert_{H_{k-\ell}}$, then [[Thm - Elliptic Regularity and the Elliptic Estimate|the elliptic estimate]], $\lVert u \rVert_{H_k} \le C(\lVert L u \rVert_{H_{k-\ell}} + \lVert u \rVert_{L^2})$, upgrades these to a bound on $\lVert u_j \rVert_{H_k}$. The bridge is that ellipticity converts a bound on the *output* of the operator, plus a weak bound on the section, into a bound on the *full* $H_k$ norm — precisely the input Rellich wants. *Example problem:* show that a sequence of harmonic sections with bounded $L^2$ norms is precompact in $C^0$, by first bounding them in every $H_k$ and then embedding.

The third disguised source is **a bound in a strictly stronger norm**. A family bounded in $C^\ell(M; E)$ with $\ell \ge k$, or in $H_{k'}(M; E)$ with $k' \ge k$, is a fortiori bounded in $H_k$: for the continuous inclusions $C^\ell \hookrightarrow H_k$ (integrate the pointwise bound over the compact $M$, whose total volume is finite) and $H_{k'} \hookrightarrow H_k$ (the embedding of part (i) of [[Thm - Sobolev Embedding Theorem|the Sobolev embedding theorem]]). The bridge is the routine but easily forgotten point that one may *land* a bound in $H_{k}$ from above, applying Rellich with $m$ any integer below $k$. *Example problem:* given a sequence bounded in $H_{k+5}$, obtain a subsequence converging in $H_{k+4}$, $H_{k+3}$, …, and in particular in $C^{k}$ once the embedding of the limit into $C^k$ applies.

**Targets (Output Amplification)**

The bare conclusion is that a bounded sequence has a convergent subsequence. Combined with one further ingredient each, it produces the structural theorems of the chapter.

Combine Rellich with **the elliptic estimate and the fact that a normed space with compact unit ball is finite-dimensional (Riesz's lemma)**. On the kernel of an elliptic operator $L$, the equation $Lu = 0$ makes the elliptic estimate read $\lVert u \rVert_{H_k} \le C \lVert u \rVert_{L^2}$, so the $H_k$ and $L^2$ norms are equivalent on $\ker L$; the $H_k$ unit ball of $\ker L$ is $L^2$-bounded, hence $L^2$-precompact by Rellich, hence $H_k$-precompact by the norm equivalence, hence $\ker L$ is finite-dimensional. This is the load-bearing step of [[Thm - Elliptic Operators on Closed Manifolds are Fredholm|the Fredholm property of elliptic operators]], and through it of the index theory and the [[Thm - Hodge Theorem for Elliptic Complexes|Hodge theorem]].

Combine Rellich with **continuity of a nonlinear map and a gauge-fixing bootstrap**. In [[Thm - Compactness of the Seiberg-Witten Moduli Space|the compactness of the Seiberg–Witten moduli space]], a sequence of solutions is put, by gauge transformations, into a form uniformly bounded in a high Sobolev norm $H_{k+1}$; Rellich then extracts a subsequence converging in $H_k$, and the continuity of the Seiberg–Witten map in the $H_k$ topology guarantees that the limit again solves the equations. The extra ingredient beyond Rellich is the pair (uniform high-norm bound, continuity of the equations), and the payoff is a compact moduli space — the finiteness on which the Seiberg–Witten invariants are defined.

Combine Rellich with **weak lower semicontinuity of a functional**. If $F$ is coercive and lower semicontinuous with respect to $H_m$-convergence, a minimising sequence is $H_k$-bounded (coercivity), has an $H_m$-convergent subsequence (Rellich), and the limit has $F$-value no larger than the infimum (lower semicontinuity), so it is a minimiser. The extra ingredient is lower semicontinuity, and the payoff is the existence half of the direct method — the general form of the Dirichlet principle that opened the chapter.

---

# Why Is It True

Forget the manifold for a moment and picture the torus, where a section is nothing but its list of Fourier coefficients $(\hat u(\xi))_{\xi \in \mathbb{Z}^n}$, and the two Sobolev norms are two ways of weighting that list: $\lVert u \rVert_k^2 = \sum_\xi (1 + |\xi|^2)^k |\hat u(\xi)|^2$ and $\lVert u \rVert_m^2 = \sum_\xi (1 + |\xi|^2)^m |\hat u(\xi)|^2$. Because $k > m$, the finer weight $(1 + |\xi|^2)^k$ is *much larger than* the coarser weight $(1 + |\xi|^2)^m$ at high frequency, and the ratio $(1 + |\xi|^2)^{m-k}$ tends to zero as $|\xi| \to \infty$. This single fact is the engine of the theorem.

Take a set of sections bounded in $H_k$, say $\lVert u \rVert_k \le 1$. The $H_m$-mass of $u$ carried by the high frequencies $|\xi| > R$ is
$$\sum_{|\xi| > R} (1 + |\xi|^2)^m |\hat u(\xi)|^2 = \sum_{|\xi| > R} (1 + |\xi|^2)^{m-k} \, (1 + |\xi|^2)^k |\hat u(\xi)|^2 \le (1 + R^2)^{m-k} \sum_{|\xi| > R} (1 + |\xi|^2)^k |\hat u(\xi)|^2 \le (1 + R^2)^{m-k},$$
because on the tail the ratio $(1 + |\xi|^2)^{m-k}$ never exceeds its value $(1 + R^2)^{m-k}$ at the innermost shell. The bound $(1 + R^2)^{m-k}$ is *the same for every $u$ in the set* and goes to zero as $R \to \infty$. So the entire bounded set has *uniformly negligible high-frequency tails* when measured in $H_m$. What survives, the low-frequency part $|\xi| \le R$, lives in a finite-dimensional space — there are only finitely many lattice points in a ball — and a bounded subset of a finite-dimensional space is precompact. A set that is, to within an error tending uniformly to zero, contained in a precompact set is itself precompact. That is the whole theorem on the torus.

> **The mechanism in one sentence:** a set bounded in $H_k$ has uniformly small Fourier tails when measured in the weaker norm $H_m$, so truncating to the finitely many low frequencies is a finite-rank operation whose error tends to zero uniformly, and the inclusion is therefore an operator-norm limit of finite-rank operators, hence compact.

Passing to a compact manifold changes nothing essential. A compact manifold is finitely many chart-pieces of a torus glued by smooth maps, and Sobolev norms only ever see a smooth map as a bounded operator; so the manifold inclusion factors through finitely many torus inclusions sandwiched between bounded localisation and reassembly maps, and compactness survives the sandwich because the compact operators form an ideal — bounded maps on either side of a compact map leave it compact.

---

# What Makes This Hard

The one genuinely non-obvious move is to see that "small uniform tails plus finite-dimensional trunk" *is* precompactness, and to encode it operator-theoretically as a norm-limit of finite-rank maps rather than fumbling with an explicit diagonal extraction. The common error is to confuse the two Sobolev norms in the tail estimate — the ratio that must decay is $(1 + |\xi|^2)^{m-k}$ with $m - k < 0$, and writing it upside down (as though the finer norm were the weaker one) collapses the argument. The second trap is at the manifold step: one must use *one and the same* atlas and partition of unity to compute both the $H_k$ and the $H_m$ norms, so that the localisation of a bounded $H_k$ sequence is a bounded $H_k$ sequence of torus functions whose torus limits reassemble to an $H_m$ limit on $M$; mixing two different sets of chart data breaks the reassembly. Everything else is bookkeeping.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove it first on the torus by writing the inclusion as an operator-norm limit of the frequency-truncation operators $T_R$, each of which is finite-rank hence compact, and invoke the closedness of the compact operators. Then transport to a compact manifold by localising through a fixed finite atlas and partition of unity, extracting a common convergent subsequence on each of the finitely many torus charts, and reassembling using the completeness of the target space.

**Subgoal decomposition:**

1. **Tail estimate on the torus.** For $k > m$ and the truncation $T_R u = \sum_{|\xi| \le R} \hat u(\xi) e^{i \langle \xi, x \rangle}$, show $\lVert u - T_R u \rVert_m \le (1 + R^2)^{(m-k)/2} \lVert u \rVert_k$, so that $\lVert \iota_{k,m} - T_R \rVert \le (1 + R^2)^{(m-k)/2} \to 0$.
   - *Hint:* Split the $H_m$ norm of $u - T_R u$ over $|\xi| > R$, factor out the ratio of weights $(1 + |\xi|^2)^{m-k}$, and bound it by its value at $|\xi| = R$ using that $m - k < 0$.
   - *Why needed:* This is the quantitative statement that high frequencies carry uniformly little $H_m$-mass; it makes the inclusion a limit of the $T_R$.

2. **Truncations are finite-rank.** Show each $T_R$ maps into the finite-dimensional space spanned by the exponentials with $|\xi| \le R$, hence is a compact operator.
   - *Hint:* The number of lattice points $\xi \in \mathbb{Z}^n$ with $|\xi| \le R$ is finite; a bounded operator with finite-dimensional image is compact.
   - *Why needed:* It supplies the compact operators whose limit is the inclusion.

3. **Torus Rellich.** Conclude that the torus inclusion $H_k(T^n; \mathbb{C}^r) \hookrightarrow H_m(T^n; \mathbb{C}^r)$ is compact.
   - *Hint:* A norm-limit of compact operators is compact.
   - *Why needed:* It is the base case that the manifold argument reduces to.

4. **Localisation and reassembly on $M$.** Fix an atlas and partition of unity; localise a bounded $H_k(M; E)$ sequence to bounded $H_k(T^n; \mathbb{C}^r)$ sequences on each chart, extract a common $H_m$-convergent subsequence by Subgoal 3, and reassemble.
   - *Hint:* The $H_l(M; E)$ norm is equivalent to the sum over charts of the torus $H_l$ norms of the localised pieces, for *every* integer $l$, using one fixed choice of data; a Cauchy sequence in the complete space $H_m(M; E)$ converges.
   - *Why needed:* It transports the torus theorem to the manifold and closes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: high-frequency tail estimate for the truncation on the torus
> **Statement:** Let $k > m$ be integers and let $r \ge 1$. For $R \ge 0$ define the frequency-truncation operator on $H_k(T^n; \mathbb{C}^r)$ by $T_R u := \sum_{\xi \in \mathbb{Z}^n,\, |\xi| \le R} \hat u(\xi) \, e^{i \langle \xi, x \rangle}$. Then for every $u \in H_k(T^n; \mathbb{C}^r)$,
> $$\lVert u - T_R u \rVert_m^2 \le (1 + R^2)^{m-k} \, \lVert u \rVert_k^2 ,$$
> and consequently the inclusion $\iota := \iota_{k,m} : H_k(T^n; \mathbb{C}^r) \to H_m(T^n; \mathbb{C}^r)$ and the truncations satisfy the operator-norm bound $\lVert \iota - T_R \rVert_{H_k \to H_m} \le (1 + R^2)^{(m-k)/2}$.
>
> **Hint:** In the sequence model an element of $H_k$ is its coefficient list $(\hat u(\xi))$; $u - T_R u$ has the same coefficients for $|\xi| > R$ and zero for $|\xi| \le R$. Factor the coarse weight $(1 + |\xi|^2)^m$ as $(1 + |\xi|^2)^{m-k}$ times the fine weight $(1 + |\xi|^2)^k$ and bound the ratio.
>
> **Why needed:** It is the quantitative core: it exhibits the inclusion as an operator-norm limit of the $T_R$, converting the qualitative "small tails" into a bound that goes to zero uniformly over the unit ball.
>
> > [!note]- Full proof
> > **Setup.** By [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order|the definition of the integer-order Sobolev spaces]] and [[Thm - Sobolev Norms on the Torus via Fourier Coefficients|the torus-norm theorem]], the map $u \mapsto (\hat u(\xi))_{\xi \in \mathbb{Z}^n}$ is an isometric isomorphism of $H_l(T^n; \mathbb{C}^r)$ onto the weighted sequence space with $\lVert u \rVert_l^2 = \sum_\xi (1 + |\xi|^2)^l |\hat u(\xi)|^2$, for every integer $l$. The operator $T_R$ acts on coefficients by $\widehat{T_R u}(\xi) = \hat u(\xi)$ for $|\xi| \le R$ and $\widehat{T_R u}(\xi) = 0$ for $|\xi| > R$; this is well defined on all of $H_k$ because it only deletes coefficients, so $\lVert T_R u \rVert_k^2 = \sum_{|\xi| \le R} (1 + |\xi|^2)^k |\hat u(\xi)|^2 \le \lVert u \rVert_k^2$.
> >
> > **Compute the residual norm.** The residual $u - T_R u$ has coefficients $\hat u(\xi)$ for $|\xi| > R$ and $0$ otherwise, so
> > $$\lVert u - T_R u \rVert_m^2 = \sum_{|\xi| > R} (1 + |\xi|^2)^m \, |\hat u(\xi)|^2 \qquad \text{(definition of the } H_m \text{ norm in coefficients).}$$
> >
> > **Insert the fine weight.** Writing $(1 + |\xi|^2)^m = (1 + |\xi|^2)^{m-k} (1 + |\xi|^2)^k$ (a factorisation of positive reals, valid termwise),
> > $$\lVert u - T_R u \rVert_m^2 = \sum_{|\xi| > R} (1 + |\xi|^2)^{m-k} \, (1 + |\xi|^2)^k \, |\hat u(\xi)|^2 \qquad \text{(splitting the exponent } m = (m-k) + k\text{).}$$
> >
> > **Bound the ratio on the tail.** For $|\xi| > R$ we have $1 + |\xi|^2 > 1 + R^2 \ge 1$, and since the exponent $m - k$ is a *negative* integer (because $k > m$), the function $t \mapsto t^{m-k}$ is strictly decreasing on $[1, \infty)$; hence $(1 + |\xi|^2)^{m-k} \le (1 + R^2)^{m-k}$ for every $\xi$ with $|\xi| > R$. Substituting this uniform bound and pulling the constant out of the sum,
> > $$\lVert u - T_R u \rVert_m^2 \le (1 + R^2)^{m-k} \sum_{|\xi| > R} (1 + |\xi|^2)^k \, |\hat u(\xi)|^2 \qquad \text{(the tail ratio is at most } (1+R^2)^{m-k}\text{).}$$
> >
> > **Discard the frequency restriction.** The remaining sum is over $|\xi| > R$ only, and every term is non-negative, so it is at most the full sum:
> > $$\sum_{|\xi| > R} (1 + |\xi|^2)^k \, |\hat u(\xi)|^2 \le \sum_{\xi \in \mathbb{Z}^n} (1 + |\xi|^2)^k \, |\hat u(\xi)|^2 = \lVert u \rVert_k^2 \qquad \text{(enlarging the index set of a sum of non-negative terms).}$$
> > Combining the last two displays gives $\lVert u - T_R u \rVert_m^2 \le (1 + R^2)^{m-k} \lVert u \rVert_k^2$, the claimed estimate.
> >
> > **Read off the operator norm.** For every $u \in H_k$, $\lVert (\iota - T_R) u \rVert_m = \lVert u - T_R u \rVert_m \le (1 + R^2)^{(m-k)/2} \lVert u \rVert_k$ (take square roots; here $\iota u$ and $u$ are the same element viewed in $H_m$). Taking the supremum over $\lVert u \rVert_k \le 1$ gives $\lVert \iota - T_R \rVert_{H_k \to H_m} \le (1 + R^2)^{(m-k)/2}$. This is the bound asserted. $\blacksquare$

> [!note]- Lemma 2: the truncations are finite-rank, hence compact
> **Statement:** For each $R \ge 0$ the operator $T_R : H_k(T^n; \mathbb{C}^r) \to H_m(T^n; \mathbb{C}^r)$ of Lemma 1 is bounded and has finite-dimensional image; its rank is at most $r \cdot \#\{\xi \in \mathbb{Z}^n : |\xi| \le R\} < \infty$. Consequently $T_R$ is a compact operator.
>
> **Hint:** The image of $T_R$ consists of trigonometric polynomials supported on the frequencies $|\xi| \le R$; there are only finitely many such frequencies. A bounded operator whose range is finite-dimensional is compact.
>
> **Why needed:** It supplies the compact operators of which the inclusion is the limit; the finiteness is where the lattice-counting content of the theorem enters.
>
> > [!note]- Full proof
> > **Boundedness.** For any $u \in H_k$, by the computation in Lemma 1 the coefficients of $T_R u$ are a subset of those of $u$, so $\lVert T_R u \rVert_m^2 = \sum_{|\xi| \le R} (1 + |\xi|^2)^m |\hat u(\xi)|^2 \le \sum_{|\xi| \le R} (1 + |\xi|^2)^k |\hat u(\xi)|^2 \le \lVert u \rVert_k^2$ (since $(1 + |\xi|^2)^{m-k} \le 1$ as $m - k < 0$ and $1 + |\xi|^2 \ge 1$). Thus $T_R$ is bounded with $\lVert T_R \rVert_{H_k \to H_m} \le 1$.
> >
> > **The index set is finite.** The set $\Lambda_R := \{\xi \in \mathbb{Z}^n : |\xi| \le R\}$ is the intersection of the lattice $\mathbb{Z}^n$ with the closed ball of radius $R$; it is finite because it is a discrete set inside a bounded set. Quantitatively, by [[Thm - Convergence of the Lattice Sum|the lattice-sum theorem]] — which establishes, en route to its tail estimate, the shell count $\#\{\xi \in \mathbb{Z}^n : R' \le |\xi| < R' + 1\} \le C_n (1 + R')^{n-1}$ — summing over the shells $R' = 0, 1, \dots, \lceil R \rceil$ gives $\#\Lambda_R \le C_n' (1 + R)^n$, in particular a finite number.
> >
> > **The range is finite-dimensional.** Every $T_R u = \sum_{\xi \in \Lambda_R} \hat u(\xi) e^{i \langle \xi, x \rangle}$ lies in the complex-linear span
> > $$V_R := \operatorname{span}_{\mathbb{C}} \{ e_a \, e^{i \langle \xi, x \rangle} : \xi \in \Lambda_R,\ a = 1, \dots, r \} ,$$
> > where $e_1, \dots, e_r$ is the standard basis of $\mathbb{C}^r$; this space has dimension at most $r \cdot \#\Lambda_R < \infty$. Hence $\operatorname{rank} T_R = \dim T_R(H_k) \le \dim V_R < \infty$.
> >
> > **Finite rank implies compact.** A bounded linear operator with finite-dimensional image is compact: this is verified as one of the standing examples on [[Def - Compact Operator|the compact-operator definition page]]. Concretely, the image under $T_R$ of the unit ball of $H_k$ is a bounded subset of the finite-dimensional space $V_R$ (bounded because $\lVert T_R \rVert \le 1$), and a bounded subset of a finite-dimensional normed space is relatively compact by [[Thm - Heine–Borel Theorem|the Heine–Borel theorem]]. Therefore $T_R$ is a compact operator. $\blacksquare$

> [!note]- Lemma 3: the inclusion on the torus is compact
> **Statement:** For integers $k > m$ and any $r \ge 1$, the inclusion $\iota_{k,m} : H_k(T^n; \mathbb{C}^r) \hookrightarrow H_m(T^n; \mathbb{C}^r)$ is a compact operator.
>
> **Hint:** By Lemma 1 the inclusion is the operator-norm limit of the $T_R$ as $R \to \infty$; by Lemma 2 each $T_R$ is compact; the compact operators are closed in the operator norm.
>
> **Why needed:** This is the base case of the theorem — the whole manifold statement will be reduced to it.
>
> > [!note]- Full proof
> > **The inclusion is bounded.** For every $u \in H_k$, $\lVert u \rVert_m^2 = \sum_\xi (1 + |\xi|^2)^m |\hat u(\xi)|^2 \le \sum_\xi (1 + |\xi|^2)^k |\hat u(\xi)|^2 = \lVert u \rVert_k^2$, because $(1 + |\xi|^2)^{m-k} \le 1$ for every $\xi$ (as $m - k < 0$ and $1 + |\xi|^2 \ge 1$). So $\iota_{k,m}$ is bounded with norm at most $1$, and in particular is a bona fide bounded operator to which the compact-operator machinery applies.
> >
> > **Approximate by finite-rank operators.** By Lemma 1, $\lVert \iota_{k,m} - T_R \rVert_{H_k \to H_m} \le (1 + R^2)^{(m-k)/2}$. Since $m - k < 0$, the exponent $(m-k)/2$ is negative, so $(1 + R^2)^{(m-k)/2} \to 0$ as $R \to \infty$. Therefore $T_R \to \iota_{k,m}$ in the operator norm of $\mathcal{B}(H_k, H_m)$.
> >
> > **Invoke closedness of the compact operators.** By Lemma 2 each $T_R$ is compact. By part (i) of [[Thm - Basic Properties of Compact Operators|the basic properties of compact operators]] — the compact operators form a *closed* linear subspace of the bounded operators $H_k \to H_m$ in the operator norm — an operator-norm limit of compact operators is compact. Since $\iota_{k,m}$ is such a limit, $\iota_{k,m}$ is compact.
> >
> > **Conclusion.** The inclusion $H_k(T^n; \mathbb{C}^r) \hookrightarrow H_m(T^n; \mathbb{C}^r)$ is a compact operator. $\blacksquare$

> [!note]- Lemma 4: localisation identity and completeness on a compact manifold
> **Statement:** Let $M$ be a compact $n$-manifold and $E \to M$ a vector bundle of rank $r$. There exist a finite atlas of charts $\kappa_i : U_i \to \kappa_i(U_i) \subseteq (-\pi, \pi)^n \subseteq T^n$ ($i = 1, \dots, N$) over which $E$ is trivialised, and a subordinate partition of unity $(\phi_i)_{i=1}^N$, such that for **every** integer $l$ the localisation maps
> $$L_l^i : H_l(M; E) \to H_l(T^n; \mathbb{C}^r), \qquad u \mapsto (\phi_i u) \circ \kappa_i^{-1} \ \text{(extended by zero)},$$
> are bounded, and there are constants $0 < c_l \le C_l$ with
> $$c_l^2 \, \lVert u \rVert_{H_l(M;E)}^2 \ \le \ \sum_{i=1}^N \lVert L_l^i u \rVert_{H_l(T^n; \mathbb{C}^r)}^2 \ \le \ C_l^2 \, \lVert u \rVert_{H_l(M;E)}^2 \qquad (u \in H_l(M; E)).$$
> Moreover $H_l(M; E)$ is a complete normed space for every integer $l$.
>
> **Hint:** This is the content of the charts construction: the manifold Sobolev norm *is* (up to equivalence, independently of the chosen data) the sum over charts of the torus Sobolev norms of the localised pieces. Completeness is built into the definition of $H_l$ as a completion.
>
> **Why needed:** It lets a bounded $H_k(M; E)$ sequence be localised into bounded $H_k(T^n; \mathbb{C}^r)$ sequences on each of finitely many charts, and lets a Cauchy sequence in $H_m(M; E)$ be summoned to a limit.
>
> > [!note]- Full proof
> > **Existence of the data.** Since $M$ is compact it admits a finite atlas of charts $\kappa_i : U_i \to \kappa_i(U_i) \subseteq (-\pi, \pi)^n$ over which $E$ is trivialised — the cube $(-\pi, \pi)^n$ embeds as a coordinate patch of $T^n = \mathbb{R}^n / 2\pi\mathbb{Z}^n$, so a function supported in $\kappa_i(U_i)$ extends by zero to a smooth function on $T^n$. A subordinate [[Def - Partition of Unity on a Manifold|partition of unity]] $(\phi_i)_{i=1}^N$ with $\operatorname{supp} \phi_i \subseteq U_i$ and $\sum_i \phi_i \equiv 1$ exists by [[Thm - Existence of Smooth Partitions of Unity|the existence theorem for partitions of unity]]. Fix these once and for all.
> >
> > **The localisation identity and boundedness of $L_l^i$.** By construction on [[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts|the charts page]], the norm on $H_l(M; E)$ is defined, for every integer $l$, by $\lVert u \rVert_l^2 := \sum_{i=1}^N \lVert (\phi_i u) \circ \kappa_i^{-1} \rVert_{H_l(T^n; \mathbb{C}^r)}^2 = \sum_i \lVert L_l^i u \rVert_{H_l(T^n)}^2$, and part (ii) of that page proves that any two admissible choices of atlas and partition of unity give equivalent norms. Taking the fixed data as the *defining* data, the displayed inequalities hold with $c_l = C_l = 1$; taking any other admissible data, they hold with the equivalence constants of that page. In either reading each $L_l^i$ is bounded, since $\lVert L_l^i u \rVert_{H_l(T^n)}^2 \le \sum_j \lVert L_l^j u \rVert_{H_l(T^n)}^2 \le C_l^2 \lVert u \rVert_{H_l(M;E)}^2$.
> >
> > **Completeness.** By the same page, $H_l(M; E)$ is defined as the completion of $\Gamma(E)$ in the norm $\lVert \cdot \rVert_l$; a completion of a normed space is, by construction, a complete normed space (indeed a Hilbertable space, the norm coming from an inner product). Hence $H_l(M; E)$ is complete for every integer $l$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a compact smooth $n$-manifold, $E \to M$ a vector bundle of rank $r$, and $k > m$ integers. We must show that the inclusion $\iota_{k,m} : H_k(M; E) \hookrightarrow H_m(M; E)$ is a compact operator; by the sequential characterisation of compactness on [[Def - Compact Operator|the compact-operator definition page]] (valid because the target $H_m(M; E)$ is complete, by Lemma 4), it is equivalent to show that every sequence bounded in $H_k(M; E)$ has a subsequence converging in $H_m(M; E)$, and we prove the theorem in this form.
>
> **Step 0 — the inclusion is a bounded linear operator.** Fix the atlas $(\kappa_i)_{i=1}^N$ and partition of unity $(\phi_i)_{i=1}^N$ of Lemma 4, and let $L_l^i$ denote the associated localisation maps. For $u \in H_k(M; E)$, using the localisation identity (Lemma 4) at both orders together with the torus norm comparison $\lVert w \rVert_{H_m(T^n)} \le \lVert w \rVert_{H_k(T^n)}$ (established in Lemma 3, Step "the inclusion is bounded"),
> $$\lVert u \rVert_{H_m(M;E)}^2 \le \tfrac{1}{c_m^2} \sum_{i=1}^N \lVert L_m^i u \rVert_{H_m(T^n)}^2 \le \tfrac{1}{c_m^2} \sum_{i=1}^N \lVert L_k^i u \rVert_{H_k(T^n)}^2 \le \tfrac{C_k^2}{c_m^2} \lVert u \rVert_{H_k(M;E)}^2 ,$$
> where the first inequality is the lower bound of Lemma 4 at order $m$, the second is the torus comparison applied to $w = L^i u = (\phi_i u) \circ \kappa_i^{-1}$ (the same section viewed at the two orders), and the third is the upper bound of Lemma 4 at order $k$. Thus $\iota_{k,m}$ is bounded, with $\lVert \iota_{k,m} \rVert \le C_k / c_m$. Linearity is immediate. The spaces $H_k(M; E)$ and $H_m(M; E)$ are complete (Lemma 4), so the compact-operator framework applies.
>
> **Step 1 — the base case on the torus.** By Lemma 3, for every integer pair $k > m$ and every $r \ge 1$ the torus inclusion $H_k(T^n; \mathbb{C}^r) \hookrightarrow H_m(T^n; \mathbb{C}^r)$ is compact; in particular every sequence bounded in $H_k(T^n; \mathbb{C}^r)$ has a subsequence converging in $H_m(T^n; \mathbb{C}^r)$.
>
> **Step 2 — localise a bounded sequence on $M$.** Let $(u_j)_{j \in \mathbb{N}}$ be a sequence with $\lVert u_j \rVert_{H_k(M;E)} \le C_0$ for all $j$. For each chart index $i \in \{1, \dots, N\}$, the localised sequence $(L_k^i u_j)_j$ lies in $H_k(T^n; \mathbb{C}^r)$ and is bounded there: by the upper bound of Lemma 4 at order $k$,
> $$\lVert L_k^i u_j \rVert_{H_k(T^n)}^2 \le \sum_{i'=1}^N \lVert L_k^{i'} u_j \rVert_{H_k(T^n)}^2 \le C_k^2 \, \lVert u_j \rVert_{H_k(M;E)}^2 \le C_k^2 C_0^2 \qquad (\text{Lemma 4; boundedness of } (u_j)) .$$
>
> **Step 3 — extract one subsequence that works on every chart.** There are only finitely many chart indices, $i = 1, \dots, N$. Apply Step 1 to the bounded sequence $(L_k^1 u_j)_j$ to obtain a subsequence along which it converges in $H_m(T^n; \mathbb{C}^r)$; from that subsequence apply Step 1 to $(L_k^2 u_j)_j$ to refine to a further subsequence along which the second localisation also converges in $H_m$; continue through $i = 3, \dots, N$. After these $N$ successive refinements we have a single subsequence — relabel it $(u_j)_j$ — along which, for **every** $i \in \{1, \dots, N\}$, the localised sequence $(L_m^i u_j)_j$ converges in $H_m(T^n; \mathbb{C}^r)$ (here $L_m^i u_j$ is the element $L_k^i u_j$ viewed in the larger space $H_m$; the inclusion $H_k(T^n) \hookrightarrow H_m(T^n)$ carries the $H_m$-convergent subsequence produced by Step 1). In particular each $(L_m^i u_j)_j$ is Cauchy in $H_m(T^n; \mathbb{C}^r)$.
>
> **Step 4 — reassemble to a Cauchy sequence on $M$.** For any two indices $j, j'$, the lower bound of Lemma 4 at order $m$, applied to $u_j - u_{j'}$, gives
> $$\lVert u_j - u_{j'} \rVert_{H_m(M;E)}^2 \le \tfrac{1}{c_m^2} \sum_{i=1}^N \lVert L_m^i(u_j - u_{j'}) \rVert_{H_m(T^n)}^2 = \tfrac{1}{c_m^2} \sum_{i=1}^N \lVert L_m^i u_j - L_m^i u_{j'} \rVert_{H_m(T^n)}^2 ,$$
> using the linearity of $L_m^i$. Fix $\varepsilon > 0$. Since each of the finitely many sequences $(L_m^i u_j)_j$ is Cauchy in $H_m(T^n; \mathbb{C}^r)$ (Step 3), choose $J$ so large that $\lVert L_m^i u_j - L_m^i u_{j'} \rVert_{H_m(T^n)}^2 < c_m^2 \varepsilon / N$ for all $j, j' \ge J$ and all $i = 1, \dots, N$ (take the maximum of the finitely many thresholds). Then for $j, j' \ge J$,
> $$\lVert u_j - u_{j'} \rVert_{H_m(M;E)}^2 \le \tfrac{1}{c_m^2} \cdot N \cdot \tfrac{c_m^2 \varepsilon}{N} = \varepsilon \qquad (\text{summing the } N \text{ chart estimates}).$$
> Hence $(u_j)_j$ is a Cauchy sequence in $H_m(M; E)$.
>
> **Step 5 — conclude.** The space $H_m(M; E)$ is complete (Lemma 4), so the Cauchy sequence $(u_j)_j$ converges to some $u \in H_m(M; E)$. We have therefore extracted, from an arbitrary $H_k(M; E)$-bounded sequence, a subsequence convergent in $H_m(M; E)$. By the sequential characterisation of compact operators between Banach spaces (target complete), the inclusion $\iota_{k,m} : H_k(M; E) \hookrightarrow H_m(M; E)$ is a compact operator. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Spectral theory of the Laplacian on a closed manifold.** Consider the Hodge Laplacian $\Delta$ acting on functions on a closed Riemannian manifold $M$, and its associated quadratic form (the Dirichlet energy) on $H_1(M)$. Rellich applies because the inclusion $H_1(M) \hookrightarrow H_0(M) = L^2(M)$ is compact, and this is exactly the hypothesis that makes the inverse of $\Delta + 1$ a compact self-adjoint operator on $L^2$; the spectral theorem for compact operators then yields a discrete spectrum $0 = \lambda_0 \le \lambda_1 \le \cdots \to \infty$ with an $L^2$-orthonormal basis of smooth eigenfunctions. It is non-obvious that a purely qualitative compactness input produces the *discreteness* and *accumulation only at infinity* of the spectrum — the entire structure of the eigenvalue problem is downstream of Rellich.

**The direct method for a nonlinear elliptic equation.** Take a semilinear energy $F(u) = \int_M \big( \tfrac12 |\nabla u|^2 + G(u) \big) \, \mathrm{vol}$ on $H_1(M)$ with $G$ bounded below and of subcritical growth. Coercivity gives a minimising sequence bounded in $H_1$; Rellich extracts a subsequence converging in $L^2$; the subcritical growth makes the lower-order term $\int G(u)$ continuous along it, while the gradient term is weakly lower semicontinuous. The Euler–Lagrange equation of the minimiser is the elliptic partial differential equation one wanted to solve. The application is non-obvious because the *compactness* Rellich provides is what converts a bound into an actual solution — without it the minimising sequence could disperse.

**Compact embeddings and the Fredholm alternative in scattering-free settings.** In a linear boundary-value or eigenvalue problem posed on a compact manifold, one writes the operator as "invertible principal part plus lower-order perturbation" and observes that the perturbation, factoring through a compact Sobolev embedding, is a compact operator; the Fredholm alternative — existence-implies-uniqueness dichotomies — then follows from Riesz–Schauder theory. Recognising that a *lower-order* term is automatically *compact* (it gains no derivatives but the embedding it factors through does the work) is the non-obvious move, and it is Rellich that certifies the compactness.

---

# Bridges

- **From bounds to the Fredholm property.** The single most important consequence: on a closed manifold, [[Thm - Elliptic Operators on Closed Manifolds are Fredholm|an elliptic operator is Fredholm]]. The construction takes the elliptic estimate $\lVert u \rVert_{H_k} \le C(\lVert L u \rVert_{H_{k-\ell}} + \lVert u \rVert_{L^2})$ and restricts it to the kernel, where $L u = 0$ collapses it to $\lVert u \rVert_{H_k} \le C \lVert u \rVert_{L^2}$. The $H_k$-unit ball of $\ker L$ is then $L^2$-bounded, so Rellich makes it $L^2$-precompact, so (by the reversed inequality on the kernel) $H_k$-precompact; a normed space whose unit ball is precompact is finite-dimensional. Compactness of the cokernel and closedness of the range follow along the same lines. This is where Rellich earns its place in the series.

- **From the torus to every compact manifold.** The proof itself is a bridge between two constructions of the Sobolev spaces: the frequency-space picture on the torus, where compactness is transparent (small tails, finite trunk), and the chart-and-partition picture on a general compact manifold, established on [[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts|the charts page]]. The localisation identity of Lemma 4 is the seam along which the torus theorem is glued to the manifold. Every "on a compact manifold" analytic statement in the chapter is transported by this same seam.

- **To the compactness of moduli spaces.** In gauge theory the sections one bounds are connections and spinors, and the bound is obtained by a bootstrap: the equations plus the elliptic estimate raise a weak bound to a bound in a high Sobolev norm, after which Rellich extracts a convergent subsequence in a slightly lower norm. This is the skeleton of [[Thm - Compactness of the Seiberg-Witten Moduli Space|the compactness of the Seiberg–Witten moduli space]]; the continuity of the equations in the lower norm promotes the limit to a solution. The bridge is the pairing of Rellich with an operator-continuity statement.

- **To the Hodge theorem.** [[Thm - Hodge Theorem for Elliptic Complexes|The Hodge decomposition]] rests on the finite-dimensionality of harmonic spaces and the closedness of the images of $d$ and $d^*$; both are consequences of the Fredholm property, and hence, one step further back, of Rellich. The chain "Rellich $\Rightarrow$ elliptic operators are Fredholm $\Rightarrow$ Hodge" is the analytic backbone that lets a topological invariant (de Rham cohomology) be represented by a unique harmonic form.

---

# Unlocked by This

> [!tip] Discreteness of the Laplace spectrum *(from Spectral Geometry)*
> Because the inclusion $H_1(M) \hookrightarrow L^2(M)$ is compact on a closed manifold, the resolvent $(\Delta + 1)^{-1}$ is a compact self-adjoint operator on $L^2(M)$, and the spectral theorem for compact operators gives a discrete spectrum with eigenvalues accumulating only at infinity and smooth eigenfunctions forming an orthonormal basis. This is the analytic foundation of **heat-kernel asymptotics** and of **Weyl's law** on the growth of eigenvalues.

> [!tip] The Fredholm property and the index *(from Elliptic Theory)*
> Rellich is the compactness that makes an elliptic operator on a closed manifold Fredholm, so that its **index** $\dim \ker L - \dim \operatorname{coker} L$ is a well-defined integer, stable under continuous deformation. This integer is the object computed by the **Atiyah–Singer index theorem** and is the deformation invariant on which the dimension counts of gauge-theoretic moduli spaces rest.
