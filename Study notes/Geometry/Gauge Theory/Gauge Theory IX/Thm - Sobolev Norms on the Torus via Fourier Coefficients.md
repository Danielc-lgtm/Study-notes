---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Fourier Series of Smooth Functions on the Torus"
  - "Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order"
  - "Def - Sobolev Space of Sections"
  - "Thm - Cauchy-Schwarz Inequality"
tags: [geometry, gauge-theory, analysis, sobolev-spaces]
---

# Notation

Throughout, $T^n = \mathbb{R}^n / 2\pi\mathbb{Z}^n$ is the flat $n$-torus, carrying the flat Riemannian metric inherited from the Euclidean metric on $\mathbb{R}^n$ and, on the trivial bundle $T^n \times \mathbb{C}^r$, the trivial connection $\nabla = d$ (component-wise differentiation). We write $C^\infty(T^n) = C^\infty(T^n; \mathbb{C})$ for the smooth complex-valued functions; every statement below has a $\mathbb{C}^r$-valued version obtained by applying it in each of the $r$ components, and we suppress the target dimension when it is $1$.

For $u \in C^\infty(T^n)$ and a frequency $\xi \in \mathbb{Z}^n$, the **Fourier coefficient** is
$$\hat{u}(\xi) = (2\pi)^{-n} \int_{T^n} u(x)\, e^{-i\langle \xi, x\rangle}\, dx, \qquad \langle \xi, x\rangle = \sum_{j=1}^n \xi_j x_j,$$
as fixed on the definition page [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order]]. For an integer $k \in \mathbb{Z}$ the **Sobolev norm of order $k$** and the space $H_k$ are
$$\lVert u\rVert_k^2 = \sum_{\xi \in \mathbb{Z}^n} (1 + \lvert\xi\rvert^2)^k \, \lvert\hat{u}(\xi)\rvert^2, \qquad H_k(T^n) := \text{completion of } C^\infty(T^n) \text{ in } \lVert\cdot\rVert_k,$$
where $\lvert\xi\rvert^2 = \sum_{j=1}^n \xi_j^2$. That page identifies $H_k(T^n)$ with the **weighted sequence space**
$$\ell^2_k := \Big\{ c = (c_\xi)_{\xi \in \mathbb{Z}^n} : \lVert c\rVert_k^2 := \sum_\xi (1+\lvert\xi\rvert^2)^k \lvert c_\xi\rvert^2 < \infty\Big\},$$
a Hilbert space with inner product $(c, d)_k = \sum_\xi (1+\lvert\xi\rvert^2)^k \, c_\xi \overline{d_\xi}$; the Fourier-coefficient map $u \mapsto \hat{u}$ is the isometric isomorphism $H_k(T^n) \to \ell^2_k$, and on the dense subspace $C^\infty(T^n)$ it is the honest Fourier coefficient. The **$L^2$ pairing** is
$$\langle u, v\rangle = (2\pi)^n \sum_{\xi \in \mathbb{Z}^n} \hat{u}(\xi)\, \overline{\hat{v}(\xi)},$$
which on smooth functions agrees with $\int_{T^n} u\bar{v}\, dx$ (Parseval, restated in Step 0), is linear in $u$ and conjugate-linear in $v$, and extends to $H_k \times H_{-k} \to \mathbb{C}$.

The **Sobolev norm from the definition page** [[Def - Sobolev Space of Sections]] is, for $p = 2$ and $u \in C^\infty(T^n)$,
$$\lVert u\rVert_{W^{k,2}}^2 = \sum_{i=0}^{k} \lVert \nabla^i u\rVert_{L^2}^2, \qquad \nabla^i u \in \Gamma\big((T^*T^n)^{\otimes i}\big) \text{ the tensor of all } i\text{-th partial derivatives},$$
so that its pointwise norm in the flat metric is $\lvert \nabla^i u\rvert^2 = \sum_{j_1, \dots, j_i = 1}^n \lvert \partial_{j_1}\cdots\partial_{j_i} u\rvert^2$. We use standard multi-index notation: for $\alpha = (\alpha_1, \dots, \alpha_n) \in \mathbb{Z}_{\ge 0}^n$, $\lvert\alpha\rvert = \sum_j \alpha_j$, $\alpha! = \prod_j \alpha_j!$, $\partial^\alpha = \partial_1^{\alpha_1}\cdots\partial_n^{\alpha_n}$, and $\xi^\alpha = \prod_j \xi_j^{\alpha_j}$ so that $\xi^{2\alpha} = \prod_j \xi_j^{2\alpha_j} \ge 0$. A sequence $c = (c_\xi)$ is **rapidly decreasing** if $\sup_\xi (1+\lvert\xi\rvert)^N \lvert c_\xi\rvert < \infty$ for every $N \in \mathbb{Z}_{\ge 0}$.

> [!warning] Convention: the $L^2$ Sobolev scale, and the clash of notations
> This series builds every Sobolev space on the base $p = 2$, writing $H_k = W^{k,2}$ (Haydys's Remark 135 records that the literature also writes $L^2_k$, $H^k$, or $W^{k,2}$ for the same object, with the subscript and superscript conventions in conflict across texts). Haydys states his embedding, multiplication, and Rellich theorems for general $W^{k,p}$, $p > 1$; those general-$p$ statements are recorded as unproved context on the relevant pages of this chapter, and everything actually proved and used in the series is the $p = 2$ case. On the torus with the flat metric and trivial connection, $\lVert\cdot\rVert_{W^{k,2}}$ is the norm of [[Def - Sobolev Space of Sections]] and $\lVert\cdot\rVert_k$ is the Fourier weight norm above; the content of part (i) is that these two are equivalent, so that the abstractly-defined completion $W^{k,2}(T^n)$ and the concrete weighted sequence space $H_k(T^n)$ coincide.

---

# Statement

> **Theorem (Sobolev norms on the torus via Fourier coefficients).** Let $T^n = \mathbb{R}^n/2\pi\mathbb{Z}^n$ carry the flat metric and let all norms be as fixed above.
>
> **(i) (Identification of the norms.)** For every integer $k \ge 0$ and every $u \in C^\infty(T^n)$,
> $$\lVert u\rVert_{W^{k,2}}^2 = (2\pi)^n \sum_{\xi \in \mathbb{Z}^n}\Big(\sum_{i=0}^k \lvert\xi\rvert^{2i}\Big)\lvert\hat{u}(\xi)\rvert^2, \qquad 2^{-k/2}(2\pi)^{n/2}\,\lVert u\rVert_k \le \lVert u\rVert_{W^{k,2}} \le (2\pi)^{n/2}\,\lVert u\rVert_k .$$
> Hence $W^{k,2}(T^n) = H_k(T^n)$ with equivalent norms, for every integer $k \ge 0$.
>
> **(ii) (The Sobolev scale is nested, and its intersection is $C^\infty$.)** For integers $k \ge m$ one has $H_k(T^n) \subseteq H_m(T^n)$ with $\lVert u\rVert_m \le \lVert u\rVert_k$ for all $u \in H_k$. Moreover, as subsets of the coefficient sequences,
> $$\bigcap_{k \in \mathbb{Z}} H_k(T^n) = C^\infty(T^n),$$
> and the Fréchet topology defined by the family of norms $\{\lVert\cdot\rVert_k\}_{k \ge 0}$ on this intersection coincides with the usual $C^\infty$ topology of uniform convergence of all derivatives.
>
> **(iii) (Peetre's inequality.)** For all $\xi, \eta \in \mathbb{R}^n$ and every real $s \in \mathbb{R}$,
> $$(1 + \lvert\xi\rvert^2)^s \le 2^{\lvert s\rvert}\, (1 + \lvert\xi - \eta\rvert^2)^{\lvert s\rvert}\, (1 + \lvert\eta\rvert^2)^s .$$
>
> **(iv) (Duality.)** For every integer $k$, the $L^2$ pairing induces an isometric conjugate-linear isomorphism
> $$T : H_{-k}(T^n) \longrightarrow H_k(T^n)^*, \qquad T(u) = \langle\,\cdot\,, u\rangle,$$
> with $\lVert T(u)\rVert_{H_k^*} = (2\pi)^n \lVert u\rVert_{-k}$; equivalently, for every $u \in H_k(T^n)$,
> $$\lVert u\rVert_k = (2\pi)^{-n} \sup\big\{\, \lvert\langle u, \phi\rangle\rvert : \phi \in C^\infty(T^n),\ \lVert\phi\rVert_{-k} \le 1 \,\big\}.$$
>
> **(v) (Interpolation.)** For integers $r < t < s$ and every $\varepsilon > 0$ there is a constant $C_\varepsilon = C_\varepsilon(r, t, s) > 0$ with
> $$\lVert u\rVert_t \le \varepsilon\, \lVert u\rVert_s + C_\varepsilon\, \lVert u\rVert_r \qquad \text{for all } u \in H_s(T^n).$$

---

# Motivation

This page is where the Sobolev spaces of the whole chapter acquire a face one can compute with. On the definition page [[Def - Sobolev Space of Sections]] the space $W^{k,2}(T^n)$ is defined abstractly, as the completion of the smooth sections in a norm built from iterated covariant derivatives; on [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order]] a second family of spaces $H_k(T^n)$ is defined, as the completion of the smooth functions in a norm built from Fourier coefficients and the weight $(1+\lvert\xi\rvert^2)^k$. Two completions of the same dense space in two different norms are the same topological vector space precisely when the norms are equivalent, and part (i) proves exactly that. After it, "the Sobolev space of order $k$ on the torus" is unambiguously the weighted sequence space $\ell^2_k$, and every analytic question about it becomes a question about weighted sums over the integer lattice.

The importance of this reduction is that it makes the hard theorems of the chapter elementary on the torus. The Sobolev embedding theorem [[Thm - Sobolev Embedding Theorem]] and the Rellich compactness theorem [[Thm - Rellich Compactness Theorem]] are, on $T^n$, one-line consequences of the convergence of a lattice sum and the summability of Fourier tails; the multiplication theorem [[Thm - Sobolev Multiplication Theorem]] is the statement that a convolution of two weighted-$\ell^2$ sequences lands in a third weighted-$\ell^2$ space, and its engine is Peetre's inequality, part (iii). The bridge page [[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts]] then transports every torus result to an arbitrary compact manifold by charts and a partition of unity. In short: the entire local analysis of elliptic operators in gauge theory is anchored here, in the observation that on the torus the Sobolev scale is nothing but a one-parameter family of weighted sequence spaces, and the five parts of this theorem are the five structural facts about that family — how its norm relates to derivatives (i), how the members are nested (ii), how the weight behaves under a shift of frequency (iii), how each member is the dual of its mirror (iv), and how a middle norm is controlled by a large and a small one (v).

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis of the theorem is only that we work on the flat torus, so the interesting question is: which problems, not visibly about the torus, are in fact problems its five parts settle?

The first disguised source is **any completion of a smooth-function space in a translation-invariant norm**. Whenever a norm on $C^\infty(T^n)$ is built from constant-coefficient differential operators — the $W^{k,2}$ norm, but also norms weighted differently across derivative orders, or Besov-type norms — the Fourier transform diagonalises it, turning it into a weighted sum. The non-obvious bridge is that constant-coefficient differentiation becomes multiplication by a polynomial in $\xi$, so equivalence of two such norms reduces to the pointwise comparability of two polynomials, which is elementary. *Example problem:* show that the norm $\big(\sum_{i \le k}\lVert\Delta^{i}u\rVert_{L^2}^2\big)^{1/2}$ built from powers of the Laplacian $\Delta = -\sum\partial_j^2$ is equivalent to $\lVert\cdot\rVert_{2k}$, by comparing $\sum_{i\le k}\lvert\xi\rvert^{4i}$ with $(1+\lvert\xi\rvert^2)^{2k}$.

The second disguised source is **a bounded linear functional or a weak formulation on a Sobolev space**. Elliptic problems are routinely posed weakly: one seeks $u$ with $\langle u, L^*\phi\rangle$ prescribed for all test $\phi$, that is, one prescribes an element of a dual space. Part (iv) says that dual space is again a Sobolev space, of the opposite order, so a weak solution is an honest element of $H_{-k}$ rather than an abstract functional. The non-obvious point is that no distribution theory is needed: the dual of $H_k$ is realised concretely as $H_{-k}$, coefficient by coefficient. *Example problem:* given a smooth function $f$ and the requirement $\langle u, \phi\rangle = \int f\phi$ for all $\phi$, recognise the right-hand side as a functional on $H_k$ and read off its order.

The third disguised source is **an interpolation or absorption need inside an a priori estimate**. Estimates for elliptic operators are proved by bounding a middle-order norm and then absorbing the top-order part into the left-hand side; whenever one meets the phrase "the lower-order terms can be absorbed", one is invoking part (v). The non-obvious bridge is that the absorption is not a Banach-space abstraction but the pointwise scalar inequality $x^t \le \varepsilon x^s + C_\varepsilon x^r$ applied at each frequency. *Example problem:* in proving $\lVert u\rVert_2 \le C(\lVert \Delta u\rVert_0 + \lVert u\rVert_0)$, absorb an intermediate $\lVert u\rVert_1$ that appears in the cross-terms using $\lVert u\rVert_1 \le \varepsilon\lVert u\rVert_2 + C_\varepsilon\lVert u\rVert_0$.

**Targets (Output Amplification).** Combined with other ingredients, each part produces the working machinery of the chapter.

Combine part (i) with **the convergence of the lattice sum** [[Thm - Convergence of the Lattice Sum]]. Once the $W^{k,2}$ norm is the weighted-$\ell^2$ norm, the summability criterion $\sum_\xi(1+\lvert\xi\rvert^2)^{-t} < \infty \iff 2t > n$ turns Cauchy–Schwarz against the weight into a bound of a sup-norm by a Sobolev norm; the payoff is the Sobolev embedding theorem $H_k(T^n) \hookrightarrow C^r(T^n)$ for $k - r > n/2$. The extra ingredient is the single scalar sum, and the amplification is a genuine regularity statement.

Combine part (i) with **the finite-rank truncation of Fourier series**. The truncation $T_R u = \sum_{\lvert\xi\rvert \le R}\hat{u}(\xi)e^{i\langle\xi, x\rangle}$ has finite rank, and part (i) shows $\lVert u - T_R u\rVert_m^2 \le (1+R^2)^{m-k}\lVert u\rVert_k^2$ for $k > m$; the payoff is that the inclusion $H_k \hookrightarrow H_m$ is a norm limit of finite-rank operators, hence compact — the Rellich theorem. The extra ingredient is the elementary tail estimate, and the amplification is compactness.

Combine part (iii) with **Cauchy–Schwarz against a summable weight**. Peetre's inequality lets the weight $(1+\lvert\xi\rvert^2)^{k/2}$ of a product $\widehat{uv}(\xi) = \sum_\eta \hat{u}(\xi - \eta)\hat{v}(\eta)$ be split between the two factors; the payoff, after a summability check that consumes the excess regularity $k_1 + k_2 - k > n/2$, is that $H_{k_1}\cdot H_{k_2} \subseteq H_k$ — the multiplication theorem, and with it the group structure of the gauge group and the smoothness of the Seiberg–Witten map. The extra ingredient is one convolution estimate, and the amplification is that Sobolev spaces above the critical exponent are algebras.

---

# Why Is It True

Forget the five parts for a moment and hold one picture: the Fourier transform turns differentiation into multiplication. Integrating by parts on the torus, with no boundary terms because everything is periodic, gives $\widehat{\partial_j u}(\xi) = i\xi_j\, \hat{u}(\xi)$; iterating, $\widehat{\partial^\alpha u}(\xi) = (i\xi)^\alpha \hat{u}(\xi)$. So an operator that on the physical side is a derivative is, on the Fourier side, multiplication of the $\xi$-th coefficient by the number $(i\xi)^\alpha$. Parseval's identity then says the $L^2$ norm of a function is, up to the constant $(2\pi)^n$, the $\ell^2$ norm of its coefficients. Put these together: the $L^2$ norm of $\partial^\alpha u$ is the weighted $\ell^2$ norm of $\hat{u}$ with weight $\lvert\xi^\alpha\rvert^2 = \xi^{2\alpha}$. Summing over all derivatives of order at most $k$ produces a weight that is a polynomial in the $\xi_j^2$, and the only thing that matters about that polynomial is its size, which is comparable to $(1+\lvert\xi\rvert^2)^k$. This comparison is part (i), and it is the whole page in miniature.

> **The mechanism in one sentence:** on the torus the $k$-th Sobolev norm is the $L^2$ norm weighted by a polynomial of degree $2k$ in the frequency, and every one of the five parts is an elementary fact about the weight $(1+\lvert\xi\rvert^2)^k$ — its growth in $k$ (nesting), its behaviour under frequency shift (Peetre), its inverse (duality), and its logarithmic convexity in $k$ (interpolation).

Each remaining part is now transparent. Nesting (ii) is that raising the exponent $k$ of a number $\ge 1$ only increases it. The intersection over all $k$ being $C^\infty$ is the statement that a coefficient sequence lies in every weighted-$\ell^2$ space exactly when it decays faster than every power of $1/\lvert\xi\rvert$, and rapid decay of coefficients is exactly smoothness (this is the content of the Fourier page). Peetre (iii) is the single inequality $1 + \lvert\xi\rvert^2 \le 2(1+\lvert\xi-\eta\rvert^2)(1+\lvert\eta\rvert^2)$, which is the triangle inequality dressed up, raised to a power. Duality (iv) is that a weighted-$\ell^2$ space is a Hilbert space, so its dual is itself; pairing against the weight $(1+\lvert\xi\rvert^2)^k$ trades $H_k$ for $H_{-k}$. Interpolation (v) is the pointwise fact that a middle power of $x \ge 1$ is dominated by any small multiple of a high power plus a large multiple of a low power. The reason the theorem is true is that, on the torus, analysis becomes arithmetic of the weight.

---

# What Makes This Hard

The genuine difficulties are three, all easy to underestimate. First, in part (i) the two norms are *not* equal — the $W^{k,2}$ weight $\sum_{i\le k}\lvert\xi\rvert^{2i}$ and the Fourier weight $(1+\lvert\xi\rvert^2)^k$ are different polynomials, and the theorem is an equivalence with explicit constants; the constant $2^{-k/2}$ appearing in the lower bound is not a slip but the binomial-coefficient penalty $\binom{k}{\lfloor k/2\rfloor} \le 2^k$, and getting it right requires the multinomial identity that collapses the tensor norm $\lVert\nabla^i u\rVert_{L^2}^2$ to the clean weight $\lvert\xi\rvert^{2i}$. Second, in part (iv) the duality is *conjugate-linear* and carries the factor $(2\pi)^n$; the common error is to assert $H_k^* = H_{-k}$ without tracking either the complex conjugation forced by the sesquilinear pairing or the normalising constant hidden in the pairing's definition. Third, the Riesz representation used in part (iv) is on an *infinite-dimensional* weighted-$\ell^2$ space, and the vault's finite-dimensional Riesz theorem does not apply; one must prove directly, by evaluating a functional on the basis vectors and controlling the resulting sequence with the operator norm through a truncation argument, that every bounded functional is a pairing. Skipping any of these three leaves a proof that looks complete but is not.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Identify every Sobolev norm on the torus with a weighted $\ell^2$ norm of the Fourier coefficients, using that differentiation is multiplication by $i\xi$ (from the Fourier page) and Parseval. Then all five parts are elementary facts about the weight function $w_k(\xi) = (1+\lvert\xi\rvert^2)^k$: a polynomial comparison for (i), monotonicity in $k$ and rapid decay for (ii), a raised triangle inequality for (iii), Riesz on weighted $\ell^2$ for (iv), and a scalar Young inequality for (v).

**Subgoal decomposition:**

1. **Reduce $\lVert\nabla^i u\rVert_{L^2}^2$ to a clean weight.** Show $\lVert\nabla^i u\rVert_{L^2}^2 = (2\pi)^n\sum_\xi \lvert\xi\rvert^{2i}\lvert\hat{u}(\xi)\rvert^2$.
   - *Hint:* Parseval gives $\lVert\partial^\alpha u\rVert_{L^2}^2 = (2\pi)^n\sum_\xi \xi^{2\alpha}\lvert\hat{u}\rvert^2$; sum over ordered tuples of derivatives and apply the multinomial theorem $\sum_{\lvert\alpha\rvert = i}\frac{i!}{\alpha!}\xi^{2\alpha} = \lvert\xi\rvert^{2i}$.
   - *Why needed:* It is the exact evaluation of the $W^{k,2}$ norm on the Fourier side, and its clean form supplies the constants in part (i).

2. **Compare the two weights.** Show $\sum_{i=0}^k \lvert\xi\rvert^{2i} \le (1+\lvert\xi\rvert^2)^k \le 2^k \sum_{i=0}^k\lvert\xi\rvert^{2i}$.
   - *Hint:* Substitute $t = \lvert\xi\rvert^2$; the binomial theorem gives $(1+t)^k = \sum_i \binom{k}{i}t^i$ with $1 \le \binom{k}{i}\le 2^k$.
   - *Why needed:* Combined with subgoal 1 it is part (i).

3. **Nesting and intersection.** For $k \ge m$ use $(1+\lvert\xi\rvert^2)^m \le (1+\lvert\xi\rvert^2)^k$; for the intersection, show a sequence lies in every $\ell^2_k$ iff it is rapidly decreasing, and quote the Fourier page's bijection between rapidly decreasing sequences and $C^\infty$.
   - *Hint:* If $c \in \bigcap_k \ell^2_k$ then $\lvert c_\xi\rvert \le \lVert c\rVert_k (1+\lvert\xi\rvert^2)^{-k/2}$ for every $k$; conversely rapid decay makes each weighted sum converge by the lattice sum.
   - *Why needed:* It is part (ii).

4. **Peetre.** Prove the base inequality $1 + \lvert\xi\rvert^2 \le 2(1+\lvert\xi-\eta\rvert^2)(1+\lvert\eta\rvert^2)$, then raise to the power $\lvert s\rvert$ and handle the sign of $s$ by swapping $\xi$ and $\eta$.
   - *Hint:* $\lvert\xi\rvert^2 \le 2\lvert\xi-\eta\rvert^2 + 2\lvert\eta\rvert^2$ from $(a+b)^2 \le 2a^2 + 2b^2$.
   - *Why needed:* It is part (iii) and the workhorse of the multiplication theorem.

5. **Riesz on weighted $\ell^2$, then convert to the pairing.** Prove directly that every bounded functional on $\ell^2_k$ is $(\cdot, g)_k$ for a unique $g \in \ell^2_k$; then re-express $(\cdot, g)_k$ as $\langle\cdot, u\rangle$ with $\hat{u} = (2\pi)^{-n}w_k \hat{g}$, and track the norm.
   - *Hint:* Evaluate the functional on the basis vectors $e_\xi$; a truncation bounded by the operator norm shows the resulting sequence is in $\ell^2_k$.
   - *Why needed:* It is part (iv).

6. **Scalar interpolation.** Prove $x^{t-r} \le \delta x^{s-r} + C_\delta$ for $x \ge 1$, multiply by $x^r$, apply at $x = 1+\lvert\xi\rvert^2$, sum, and take square roots.
   - *Hint:* Maximise $x^a - \delta x^b$ ($0 < a < b$) over $x \ge 0$ by calculus to obtain $C_\delta$ explicitly.
   - *Why needed:* It is part (v).

---

# Lemma Decomposition

> [!note]- Lemma 1: The tensor norm of the $i$-th derivative is the weight $\lvert\xi\rvert^{2i}$
> **Statement:** For $u \in C^\infty(T^n)$ and any integer $i \ge 0$,
> $$\lVert\nabla^i u\rVert_{L^2}^2 = (2\pi)^n \sum_{\xi \in \mathbb{Z}^n} \lvert\xi\rvert^{2i}\, \lvert\hat{u}(\xi)\rvert^2.$$
>
> **Hint:** Compute $\lVert\partial^\alpha u\rVert_{L^2}^2$ by Parseval, then sum over the ordered $i$-tuples of coordinate directions and collect by multi-index using the multinomial theorem.
>
> **Why needed:** It evaluates the $W^{k,2}$ norm exactly on the Fourier side and, remarkably, produces the single clean weight $\lvert\xi\rvert^{2i}$ rather than a sum of monomials; this is what makes the constants in part (i) explicit.
>
> > [!note]- Full proof
> > We use two facts from [[Thm - Fourier Series of Smooth Functions on the Torus]], restated at the point of use.
> >
> > **Fact A (differentiation is multiplication by $i\xi$).** For $u \in C^\infty(T^n)$ and $1 \le j \le n$, $\widehat{\partial_j u}(\xi) = i\xi_j\, \hat{u}(\xi)$; iterating over the entries of a multi-index $\alpha$, $\widehat{\partial^\alpha u}(\xi) = (i\xi)^\alpha\, \hat{u}(\xi) = i^{\lvert\alpha\rvert}\xi^\alpha\, \hat{u}(\xi)$. (Both derivatives are again smooth, so their Fourier coefficients are defined and the identity is the one proved on the Fourier page by integration by parts, using periodicity to kill boundary terms.)
> >
> > **Fact B (Parseval).** For $v, w \in C^\infty(T^n)$, $\int_{T^n} v\bar{w}\, dx = (2\pi)^n\sum_\xi \hat{v}(\xi)\overline{\hat{w}(\xi)}$; in particular $\lVert v\rVert_{L^2}^2 = (2\pi)^n\sum_\xi \lvert\hat{v}(\xi)\rvert^2$.
> >
> > **Step 1: the $L^2$ norm of a single mixed partial.** Fix a multi-index $\alpha$ with $\lvert\alpha\rvert = i$. By Fact A, $\widehat{\partial^\alpha u}(\xi) = i^{\lvert\alpha\rvert}\xi^\alpha \hat{u}(\xi)$, so, since $\lvert i^{\lvert\alpha\rvert}\rvert = 1$ and $\xi^\alpha \in \mathbb{R}$,
> > $$\lVert\partial^\alpha u\rVert_{L^2}^2 = (2\pi)^n\sum_\xi \big\lvert i^{\lvert\alpha\rvert}\xi^\alpha \hat{u}(\xi)\big\rvert^2 = (2\pi)^n\sum_\xi \xi^{2\alpha}\, \lvert\hat{u}(\xi)\rvert^2 \qquad \text{(by Fact B applied to } v = \partial^\alpha u\text{, then Fact A).}$$
> >
> > **Step 2: sum over ordered tuples.** The pointwise squared norm of the tensor $\nabla^i u$ in the flat metric is $\lvert\nabla^i u\rvert^2 = \sum_{j_1, \dots, j_i = 1}^n \lvert\partial_{j_1}\cdots\partial_{j_i} u\rvert^2$, the sum running over all $n^i$ ordered $i$-tuples $(j_1, \dots, j_i)$. Integrating over $T^n$ and using Step 1 for each tuple (a tuple with $\alpha_p$ occurrences of the direction $p$ gives the multi-index $\alpha = (\alpha_1, \dots, \alpha_n)$),
> > $$\lVert\nabla^i u\rVert_{L^2}^2 = \sum_{j_1, \dots, j_i} \lVert\partial_{j_1}\cdots\partial_{j_i} u\rVert_{L^2}^2 = \sum_{\lvert\alpha\rvert = i} N(\alpha)\, \lVert\partial^\alpha u\rVert_{L^2}^2 \qquad \text{(grouping tuples by their multi-index),}$$
> > where $N(\alpha) = \tfrac{i!}{\alpha!}$ is the number of ordered $i$-tuples yielding $\alpha$ (a standard multinomial count: the number of ways to arrange $\alpha_1$ copies of $1$, $\dots$, $\alpha_n$ copies of $n$).
> >
> > **Step 3: collapse by the multinomial theorem.** Substituting Step 1 and interchanging the two finite-or-absolutely-convergent sums (the inner sum over $\xi$ is a sum of non-negative terms, so Tonelli's theorem for series permits the interchange),
> > $$\lVert\nabla^i u\rVert_{L^2}^2 = (2\pi)^n\sum_\xi\Big(\sum_{\lvert\alpha\rvert = i}\tfrac{i!}{\alpha!}\,\xi^{2\alpha}\Big)\lvert\hat{u}(\xi)\rvert^2 = (2\pi)^n\sum_\xi \big(\xi_1^2 + \cdots + \xi_n^2\big)^i\, \lvert\hat{u}(\xi)\rvert^2 = (2\pi)^n\sum_\xi \lvert\xi\rvert^{2i}\lvert\hat{u}(\xi)\rvert^2,$$
> > where the middle equality is the multinomial theorem $\big(\sum_{p} a_p\big)^i = \sum_{\lvert\alpha\rvert = i}\frac{i!}{\alpha!}\prod_p a_p^{\alpha_p}$ applied with $a_p = \xi_p^2$. This is the claim. $\blacksquare$

> [!note]- Lemma 2: Comparability of the two Sobolev weights
> **Statement:** For every integer $k \ge 0$ and every $\xi \in \mathbb{R}^n$,
> $$\sum_{i=0}^k \lvert\xi\rvert^{2i} \;\le\; (1 + \lvert\xi\rvert^2)^k \;\le\; 2^k \sum_{i=0}^k \lvert\xi\rvert^{2i}.$$
>
> **Hint:** Set $t = \lvert\xi\rvert^2 \ge 0$ and expand $(1+t)^k$ by the binomial theorem; the coefficients $\binom{k}{i}$ lie between $1$ and $2^k$.
>
> **Why needed:** It is the pointwise comparison of the $W^{k,2}$ weight (Lemma 1) with the Fourier weight, and it produces the constants $2^{-k/2}(2\pi)^{n/2}$ and $(2\pi)^{n/2}$ of part (i).
>
> > [!note]- Full proof
> > Put $t = \lvert\xi\rvert^2 \ge 0$. By the binomial theorem,
> > $$(1 + t)^k = \sum_{i=0}^k \binom{k}{i} t^i.$$
> >
> > **Lower bound.** Each binomial coefficient satisfies $\binom{k}{i} \ge 1$ (it is a positive integer for $0 \le i \le k$), and $t^i \ge 0$, so
> > $$(1+t)^k = \sum_{i=0}^k \binom{k}{i} t^i \;\ge\; \sum_{i=0}^k 1\cdot t^i = \sum_{i=0}^k t^i \qquad \text{(term-by-term, using } \binom{k}{i}\ge 1 \text{ and } t^i \ge 0\text{).}$$
> >
> > **Upper bound.** The binomial coefficients sum to $\sum_{i=0}^k\binom{k}{i} = 2^k$, so each satisfies $\binom{k}{i} \le 2^k$; hence
> > $$(1+t)^k = \sum_{i=0}^k \binom{k}{i} t^i \;\le\; \sum_{i=0}^k 2^k\, t^i = 2^k\sum_{i=0}^k t^i \qquad \text{(term-by-term, using } \binom{k}{i} \le 2^k \text{ and } t^i \ge 0\text{).}$$
> >
> > Substituting $t = \lvert\xi\rvert^2$ gives both inequalities. $\blacksquare$

> [!note]- Lemma 3: Riesz representation on a weighted sequence space
> **Statement:** Let $w = (w_\xi)_{\xi \in \mathbb{Z}^n}$ be strictly positive weights and $\ell^2_w = \{c : \lVert c\rVert_w^2 = \sum_\xi w_\xi\lvert c_\xi\rvert^2 < \infty\}$ the Hilbert space with inner product $(c, d)_w = \sum_\xi w_\xi\, c_\xi\overline{d_\xi}$. Then for every bounded linear functional $\Lambda : \ell^2_w \to \mathbb{C}$ there is a unique $g \in \ell^2_w$ with $\Lambda(c) = (c, g)_w$ for all $c$, and $\lVert g\rVert_w = \lVert\Lambda\rVert$ (the operator norm).
>
> **Hint:** Read off the candidate $g$ from the values of $\Lambda$ on the basis sequences $e_\xi$; a truncation argument bounds $\lVert g\rVert_w$ by $\lVert\Lambda\rVert$.
>
> **Why needed:** Part (iv) identifies $H_k^*$ with $H_{-k}$, and this identification is Riesz representation on $\ell^2_k$; the vault's [[Thm - Riesz Representation Theorem (Finite-Dimensional)|finite-dimensional Riesz theorem]] does not apply to the infinite-dimensional $\ell^2_k$, so the representation must be proved directly here.
>
> > [!note]- Full proof
> > Let $e_\xi \in \ell^2_w$ be the sequence with a $1$ in position $\xi$ and $0$ elsewhere; then $(e_\xi, e_\eta)_w = w_\xi\delta_{\xi\eta}$ and $\lVert e_\xi\rVert_w = w_\xi^{1/2}$. Write $A = \lVert\Lambda\rVert = \sup\{\lvert\Lambda(c)\rvert : \lVert c\rVert_w \le 1\} < \infty$.
> >
> > **Step 0 — finitely supported sequences are dense.** For $c \in \ell^2_w$ and a finite set $F \subset \mathbb{Z}^n$, let $c^F$ agree with $c$ on $F$ and vanish off $F$. Then $\lVert c - c^F\rVert_w^2 = \sum_{\xi \notin F} w_\xi\lvert c_\xi\rvert^2$, which is the tail of the convergent series $\sum_\xi w_\xi\lvert c_\xi\rvert^2$ and therefore tends to $0$ as $F$ increases to $\mathbb{Z}^n$; so the finitely supported sequences, that is, the linear span of $\{e_\xi\}$, are dense in $\ell^2_w$.
> >
> > **Step 1 — define the candidate.** Set $g_\xi := \overline{\Lambda(e_\xi)}\,/\, w_\xi$ for each $\xi$, and $g = (g_\xi)$. This is chosen so that if $\Lambda(\cdot) = (\cdot, g)_w$ held, then $\Lambda(e_\xi) = (e_\xi, g)_w = w_\xi \overline{g_\xi}$, consistent with the definition. We must show $g \in \ell^2_w$ and that the representation indeed holds.
> >
> > **Step 2 — $g \in \ell^2_w$ with $\lVert g\rVert_w \le A$.** Fix a finite $F$ and consider $g^F = \sum_{\xi \in F} g_\xi e_\xi \in \ell^2_w$. By linearity of $\Lambda$ and the definition of $g_\xi$,
> > $$\Lambda(g^F) = \sum_{\xi \in F} g_\xi\, \Lambda(e_\xi) = \sum_{\xi \in F} g_\xi\, w_\xi\overline{g_\xi} = \sum_{\xi \in F} w_\xi\lvert g_\xi\rvert^2 = \lVert g^F\rVert_w^2 \qquad \text{(definition of } g_\xi\text{, then of } \lVert\cdot\rVert_w\text{).}$$
> > On the other hand, boundedness of $\Lambda$ gives $\lvert\Lambda(g^F)\rvert \le A\,\lVert g^F\rVert_w$. Combining, $\lVert g^F\rVert_w^2 \le A\,\lVert g^F\rVert_w$, hence $\lVert g^F\rVert_w \le A$, that is $\sum_{\xi \in F} w_\xi\lvert g_\xi\rvert^2 \le A^2$. As this holds for every finite $F$, taking the supremum over $F$ gives $\lVert g\rVert_w^2 = \sum_\xi w_\xi\lvert g_\xi\rvert^2 \le A^2 < \infty$, so $g \in \ell^2_w$ and $\lVert g\rVert_w \le A$.
> >
> > **Step 3 — the representation holds.** Both $\Lambda$ and $c \mapsto (c, g)_w$ are bounded linear functionals on $\ell^2_w$ (the second because, by the Cauchy–Schwarz inequality in the inner product space $\ell^2_w$, $\lvert(c, g)_w\rvert \le \lVert c\rVert_w\lVert g\rVert_w$; restated: in any inner product space $\lvert(x, y)\rvert \le \lVert x\rVert\lVert y\rVert$, the content of [[Thm - Cauchy-Schwarz Inequality]]). On a basis sequence they agree: $(e_\xi, g)_w = w_\xi\overline{g_\xi} = \Lambda(e_\xi)$ by Step 1. By linearity they agree on the span of $\{e_\xi\}$, and by Step 0 that span is dense; two bounded functionals agreeing on a dense set are equal (their difference is bounded and vanishes on a dense set, hence is continuous and zero, hence zero everywhere). Therefore $\Lambda(c) = (c, g)_w$ for all $c \in \ell^2_w$.
> >
> > **Step 4 — norm equality and uniqueness.** From Step 3 and Cauchy–Schwarz, $\lvert\Lambda(c)\rvert = \lvert(c, g)_w\rvert \le \lVert c\rVert_w\lVert g\rVert_w$, so $A = \lVert\Lambda\rVert \le \lVert g\rVert_w$; with Step 2 this gives $\lVert\Lambda\rVert = \lVert g\rVert_w$. For uniqueness, if $(c, g)_w = (c, g')_w$ for all $c$, then taking $c = e_\xi$ gives $w_\xi\overline{g_\xi} = w_\xi\overline{g_\xi'}$, and since $w_\xi > 0$, $g_\xi = g_\xi'$ for every $\xi$, so $g = g'$. $\blacksquare$

> [!note]- Lemma 4: Scalar interpolation inequality
> **Statement:** Let $0 < a < b$ be reals. For every $\delta > 0$ there is a constant
> $$C_\delta = \frac{b - a}{b}\left(\frac{a}{\delta b}\right)^{a/(b-a)} > 0 \qquad \text{such that} \qquad x^a \le \delta\, x^b + C_\delta \quad \text{for all } x \ge 0.$$
> Consequently, for integers $r < t < s$ and every $\delta > 0$, $x^t \le \delta\, x^s + C'_\delta\, x^r$ for all $x \ge 1$, with $C'_\delta = C_\delta$ evaluated at $a = t - r$, $b = s - r$.
>
> **Hint:** Maximise $g(x) = x^a - \delta x^b$ over $x \ge 0$ by elementary calculus; its maximum value is $C_\delta$.
>
> **Why needed:** Applied at $x = 1+\lvert\xi\rvert^2$ and summed against $\lvert\hat{u}(\xi)\rvert^2$, it is part (v).
>
> > [!note]- Full proof
> > **Step 1 — the maximum of $g(x) = x^a - \delta x^b$.** The function $g$ is continuous on $[0, \infty)$ with $g(0) = 0$ and $g(x) \to -\infty$ as $x \to \infty$ (because $b > a > 0$, so the $-\delta x^b$ term dominates); and $g(x) > 0$ for small $x > 0$ (because $x^a$ dominates $\delta x^b$ near $0$, as $a < b$). Hence $g$ attains a positive maximum at an interior point $x_* > 0$. Differentiating,
> > $$g'(x) = a x^{a-1} - \delta b\, x^{b-1} = x^{a-1}\big(a - \delta b\, x^{b-a}\big),$$
> > which vanishes for $x > 0$ exactly when $x^{b-a} = a/(\delta b)$, that is at $x_* = \big(a/(\delta b)\big)^{1/(b-a)}$.
> >
> > **Step 2 — evaluate the maximum.** At $x_*$ we have $\delta x_*^{b-a} = a/b$, so
> > $$g(x_*) = x_*^a - \delta x_*^b = x_*^a\big(1 - \delta x_*^{b-a}\big) = x_*^a\Big(1 - \frac{a}{b}\Big) = \frac{b-a}{b}\,x_*^a = \frac{b-a}{b}\left(\frac{a}{\delta b}\right)^{a/(b-a)} =: C_\delta > 0.$$
> > Therefore $x^a - \delta x^b \le g(x_*) = C_\delta$ for all $x \ge 0$, that is $x^a \le \delta x^b + C_\delta$.
> >
> > **Step 3 — the shifted form.** Let $r < t < s$ be integers, $a = t - r > 0$, $b = s - r > 0$, so $a < b$. Step 2 gives $x^{t-r} \le \delta x^{s-r} + C'_\delta$ for $x \ge 0$, with $C'_\delta = \frac{b-a}{b}(a/(\delta b))^{a/(b-a)}$. For $x \ge 1$ we have $x^r > 0$, and multiplying through by $x^r$ (which preserves the inequality) gives
> > $$x^t = x^r\cdot x^{t-r} \le x^r\big(\delta x^{s-r} + C'_\delta\big) = \delta\, x^s + C'_\delta\, x^r,$$
> > as claimed. $\blacksquare$

> [!note]- Lemma 5: The intersection of all weighted $\ell^2$ spaces is the rapidly decreasing sequences
> **Statement:** A coefficient sequence $c = (c_\xi)_{\xi \in \mathbb{Z}^n}$ lies in $\bigcap_{k \in \mathbb{Z}} \ell^2_k$ if and only if it is rapidly decreasing, that is $\sup_\xi (1+\lvert\xi\rvert)^N\lvert c_\xi\rvert < \infty$ for every $N \ge 0$.
>
> **Hint:** One direction uses the pointwise bound $\lvert c_\xi\rvert \le \lVert c\rVert_k (1+\lvert\xi\rvert^2)^{-k/2}$; the other uses the convergence of the lattice sum.
>
> **Why needed:** Combined with the Fourier page's bijection between rapidly decreasing sequences and smooth functions, it is the set equality $\bigcap_k H_k = C^\infty$ of part (ii).
>
> > [!note]- Full proof
> > Since $\ell^2_k \subseteq \ell^2_m$ for $k \ge m$ (proved in part (ii), Step 1 below), the intersection over all integers equals the intersection over $k \ge 0$.
> >
> > **($\Rightarrow$) Membership in every $\ell^2_k$ forces rapid decrease.** Suppose $c \in \bigcap_{k\ge 0}\ell^2_k$. Fix $k$ and $\xi$. Since a single term of a series of non-negative terms is at most the whole sum,
> > $$(1+\lvert\xi\rvert^2)^k\lvert c_\xi\rvert^2 \le \sum_{\eta}(1+\lvert\eta\rvert^2)^k\lvert c_\eta\rvert^2 = \lVert c\rVert_k^2,$$
> > hence $\lvert c_\xi\rvert \le \lVert c\rVert_k\,(1+\lvert\xi\rvert^2)^{-k/2} \le \lVert c\rVert_k\,(1+\lvert\xi\rvert)^{-k}$ (using $(1+\lvert\xi\rvert^2)^{1/2} \ge (1+\lvert\xi\rvert)/\sqrt{2} \ge \tfrac12(1+\lvert\xi\rvert)$, so $(1+\lvert\xi\rvert^2)^{-k/2} \le 2^k(1+\lvert\xi\rvert)^{-k}$; absorbing the harmless factor $2^k$ into the constant). Given any $N$, take $k = N$: then $(1+\lvert\xi\rvert)^N\lvert c_\xi\rvert \le 2^N\lVert c\rVert_N < \infty$ uniformly in $\xi$. So $c$ is rapidly decreasing.
> >
> > **($\Leftarrow$) Rapid decrease forces membership in every $\ell^2_k$.** Suppose $c$ is rapidly decreasing and fix $k \ge 0$. Choose $N$ with $2N - 2k > n$, and use the rapid-decrease bound $\lvert c_\xi\rvert \le C_N(1+\lvert\xi\rvert)^{-N}$. Since $1+\lvert\xi\rvert^2 \le (1+\lvert\xi\rvert)^2$, we have $(1+\lvert\xi\rvert^2)^k \le (1+\lvert\xi\rvert)^{2k}$, so
> > $$\lVert c\rVert_k^2 = \sum_\xi (1+\lvert\xi\rvert^2)^k\lvert c_\xi\rvert^2 \le C_N^2\sum_\xi (1+\lvert\xi\rvert)^{2k - 2N} \le C_N^2\sum_\xi (1+\lvert\xi\rvert^2)^{k - N} < \infty,$$
> > where the last sum converges because $2(N - k) > n$, by [[Thm - Convergence of the Lattice Sum]] (restated: $\sum_{\xi\in\mathbb{Z}^n}(1+\lvert\xi\rvert^2)^{-t} < \infty$ if and only if $2t > n$), applied with $t = N - k$. Hence $c \in \ell^2_k$, and as $k$ was arbitrary, $c \in \bigcap_k \ell^2_k$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Throughout we use the isometric identification $u \mapsto \hat{u}$ of $H_k(T^n)$ with $\ell^2_k$ from [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order]], under which $\lVert u\rVert_k = \lVert\hat{u}\rVert_k$ and, for smooth $u$, $\hat{u}$ is the honest Fourier-coefficient sequence.
>
> **Step 0 — the two ingredients from the Fourier page.** From [[Thm - Fourier Series of Smooth Functions on the Torus]] we take, for $u \in C^\infty(T^n)$: (A) $\widehat{\partial^\alpha u}(\xi) = i^{\lvert\alpha\rvert}\xi^\alpha\hat{u}(\xi)$; (B) Parseval, $\lVert v\rVert_{L^2}^2 = (2\pi)^n\sum_\xi\lvert\hat{v}(\xi)\rvert^2$; and (C) the linear bijection $u \mapsto (\hat{u}(\xi))_\xi$ from $C^\infty(T^n)$ onto the rapidly decreasing sequences, with inverse the Fourier series. These are the only external inputs; everything else is Lemmas 1–5.
>
> **Part (i).** Let $k \ge 0$ be an integer and $u \in C^\infty(T^n)$. By the definition of the $W^{k,2}$ norm and Lemma 1,
> $$\lVert u\rVert_{W^{k,2}}^2 = \sum_{i=0}^k \lVert\nabla^i u\rVert_{L^2}^2 = \sum_{i=0}^k (2\pi)^n\sum_\xi\lvert\xi\rvert^{2i}\lvert\hat{u}(\xi)\rvert^2 = (2\pi)^n\sum_\xi\Big(\sum_{i=0}^k\lvert\xi\rvert^{2i}\Big)\lvert\hat{u}(\xi)\rvert^2 \quad \text{(Lemma 1, then interchange of two non-negative sums by Tonelli),}$$
> which is the displayed exact evaluation in the statement. Now apply Lemma 2 pointwise in $\xi$, with $t = \lvert\xi\rvert^2$: multiplying the double inequality $\sum_{i=0}^k\lvert\xi\rvert^{2i} \le (1+\lvert\xi\rvert^2)^k \le 2^k\sum_{i=0}^k\lvert\xi\rvert^{2i}$ by $(2\pi)^n\lvert\hat{u}(\xi)\rvert^2 \ge 0$ and summing over $\xi$,
> $$\lVert u\rVert_{W^{k,2}}^2 \le (2\pi)^n\sum_\xi(1+\lvert\xi\rvert^2)^k\lvert\hat{u}(\xi)\rvert^2 = (2\pi)^n\lVert u\rVert_k^2 \le 2^k\,\lVert u\rVert_{W^{k,2}}^2 \qquad \text{(Lemma 2 pointwise, then definition of } \lVert\cdot\rVert_k\text{).}$$
> Taking square roots in the left inequality gives $\lVert u\rVert_{W^{k,2}} \le (2\pi)^{n/2}\lVert u\rVert_k$; taking square roots in $(2\pi)^n\lVert u\rVert_k^2 \le 2^k\lVert u\rVert_{W^{k,2}}^2$ gives $(2\pi)^{n/2}\lVert u\rVert_k \le 2^{k/2}\lVert u\rVert_{W^{k,2}}$, that is $\lVert u\rVert_{W^{k,2}} \ge 2^{-k/2}(2\pi)^{n/2}\lVert u\rVert_k$. Thus
> $$2^{-k/2}(2\pi)^{n/2}\,\lVert u\rVert_k \le \lVert u\rVert_{W^{k,2}} \le (2\pi)^{n/2}\,\lVert u\rVert_k \qquad \text{for all } u \in C^\infty(T^n).$$
> The two norms are equivalent on the common dense space $C^\infty(T^n)$; two equivalent norms have identical Cauchy sequences and identical null sequences, so their completions coincide as topological vector spaces. Therefore $W^{k,2}(T^n) = H_k(T^n)$ with equivalent norms. This proves part (i).
>
> **Part (ii).** *Step 1 — nesting.* Let $k \ge m$ be integers. For every $\xi$, since $1 + \lvert\xi\rvert^2 \ge 1$ and $k \ge m$, raising a number $\ge 1$ to a larger power increases it: $(1+\lvert\xi\rvert^2)^m \le (1+\lvert\xi\rvert^2)^k$. Multiplying by $\lvert\hat{u}(\xi)\rvert^2 \ge 0$ and summing,
> $$\lVert u\rVert_m^2 = \sum_\xi(1+\lvert\xi\rvert^2)^m\lvert\hat{u}(\xi)\rvert^2 \le \sum_\xi(1+\lvert\xi\rvert^2)^k\lvert\hat{u}(\xi)\rvert^2 = \lVert u\rVert_k^2,$$
> so $\lVert u\rVert_m \le \lVert u\rVert_k$. In particular the identity on $C^\infty(T^n)$ is $\lVert\cdot\rVert_k$-to-$\lVert\cdot\rVert_m$ bounded, hence extends to a continuous injection $H_k \hookrightarrow H_m$; injectivity is clear from the sequence-space picture, where the map is the literal inclusion $\ell^2_k \subseteq \ell^2_m$ (a sequence with finite $\lVert\cdot\rVert_k$-norm has finite $\lVert\cdot\rVert_m$-norm by the same inequality).
>
> *Step 2 — the intersection is $C^\infty$.* By Lemma 5, a coefficient sequence lies in $\bigcap_{k\in\mathbb{Z}} H_k = \bigcap_{k\ge 0}\ell^2_k$ if and only if it is rapidly decreasing. By ingredient (C) of Step 0, the rapidly decreasing sequences are exactly the Fourier-coefficient sequences of smooth functions, and the Fourier series recovers the smooth function from its coefficients. Under the identifications, therefore, $\bigcap_{k}H_k(T^n) = C^\infty(T^n)$ as sets.
>
> *Step 3 — the topologies agree.* Write $u_j \to u$ meaning convergence of smooth functions. We show that $\lVert u_j - u\rVert_k \to 0$ for every $k \ge 0$ if and only if $\partial^\alpha u_j \to \partial^\alpha u$ uniformly for every multi-index $\alpha$ (the defining convergence of the $C^\infty$ topology). Set $w = u_j - u \in C^\infty(T^n)$.
> First, uniform convergence of derivatives implies $\lVert\cdot\rVert_k$-convergence: by part (i), $\lVert w\rVert_k \le 2^{k/2}(2\pi)^{-n/2}\lVert w\rVert_{W^{k,2}}$, and $\lVert w\rVert_{W^{k,2}}^2 = \sum_{i\le k}\lVert\nabla^i w\rVert_{L^2}^2 \le \mathrm{vol}(T^n)\sum_{i\le k}\lVert\nabla^i w\rVert_{C^0}^2$, so uniform smallness of the derivatives of $w$ up to order $k$ forces $\lVert w\rVert_k \to 0$.
> Conversely, suppose $\lVert w\rVert_k \to 0$ for every $k$. For a multi-index $\alpha$, the Fourier series of $\partial^\alpha w$ is $\sum_\xi (i\xi)^\alpha\hat{w}(\xi)e^{i\langle\xi,x\rangle}$ (ingredient (A)), so
> $$\sup_x\lvert\partial^\alpha w(x)\rvert \le \sum_\xi\lvert\xi^\alpha\rvert\,\lvert\hat{w}(\xi)\rvert \le \sum_\xi(1+\lvert\xi\rvert)^{\lvert\alpha\rvert}\lvert\hat{w}(\xi)\rvert,$$
> and by the Cauchy–Schwarz inequality (restated: $\lvert\sum a_\xi b_\xi\rvert \le (\sum\lvert a_\xi\rvert^2)^{1/2}(\sum\lvert b_\xi\rvert^2)^{1/2}$, the content of [[Thm - Cauchy-Schwarz Inequality]] for the inner product space of square-summable sequences), splitting the weight as $(1+\lvert\xi\rvert)^{\lvert\alpha\rvert} = (1+\lvert\xi\rvert^2)^{-M/2}\cdot (1+\lvert\xi\rvert)^{\lvert\alpha\rvert}(1+\lvert\xi\rvert^2)^{M/2}$ with an integer $M > \lvert\alpha\rvert + n/2$,
> $$\sup_x\lvert\partial^\alpha w(x)\rvert \le \Big(\sum_\xi (1+\lvert\xi\rvert)^{2\lvert\alpha\rvert}(1+\lvert\xi\rvert^2)^{-M}\Big)^{1/2}\Big(\sum_\xi(1+\lvert\xi\rvert^2)^{M}\lvert\hat{w}(\xi)\rvert^2\Big)^{1/2} = C_{\alpha,M}\,\lVert w\rVert_M ,$$
> where the first factor $C_{\alpha,M}$ is finite because $(1+\lvert\xi\rvert)^{2\lvert\alpha\rvert} \le (1+\lvert\xi\rvert^2)^{\lvert\alpha\rvert}$ makes it at most $\sum_\xi(1+\lvert\xi\rvert^2)^{\lvert\alpha\rvert - M}$, convergent by [[Thm - Convergence of the Lattice Sum]] since $2(M - \lvert\alpha\rvert) > n$. As $\lVert w\rVert_M \to 0$, we get $\sup_x\lvert\partial^\alpha w\rvert \to 0$. Hence the two topologies coincide. This proves part (ii).
>
> **Part (iii).** *Step 1 — the base inequality.* Fix $\xi, \eta \in \mathbb{R}^n$. From the elementary inequality $(a + b)^2 \le 2a^2 + 2b^2$ (which is $0 \le (a-b)^2$ rearranged) applied to the triangle inequality $\lvert\xi\rvert \le \lvert\xi - \eta\rvert + \lvert\eta\rvert$,
> $$\lvert\xi\rvert^2 \le \big(\lvert\xi-\eta\rvert + \lvert\eta\rvert\big)^2 \le 2\lvert\xi-\eta\rvert^2 + 2\lvert\eta\rvert^2 .$$
> Writing $a = \lvert\xi-\eta\rvert^2 \ge 0$ and $b = \lvert\eta\rvert^2 \ge 0$, and using $1 \le 2$ and $2ab \ge 0$,
> $$1 + \lvert\xi\rvert^2 \le 1 + 2a + 2b \le 2 + 2a + 2b + 2ab = 2(1 + a)(1 + b) = 2(1 + \lvert\xi-\eta\rvert^2)(1 + \lvert\eta\rvert^2).$$
>
> *Step 2 — the case $s \ge 0$.* All three factors $1+\lvert\xi\rvert^2$, $1+\lvert\xi-\eta\rvert^2$, $1+\lvert\eta\rvert^2$ are $\ge 1 > 0$, so raising the base inequality to the power $s \ge 0$ preserves it:
> $$(1+\lvert\xi\rvert^2)^s \le 2^s(1+\lvert\xi-\eta\rvert^2)^s(1+\lvert\eta\rvert^2)^s = 2^{\lvert s\rvert}(1+\lvert\xi-\eta\rvert^2)^{\lvert s\rvert}(1+\lvert\eta\rvert^2)^s \qquad (\text{since } s = \lvert s\rvert \ge 0).$$
>
> *Step 3 — the case $s < 0$.* Write $s = -t$ with $t > 0$, so $\lvert s\rvert = t$. Apply Step 1 with $\xi$ and $\eta$ interchanged (using $\lvert\eta - \xi\rvert = \lvert\xi - \eta\rvert$): $1 + \lvert\eta\rvert^2 \le 2(1+\lvert\xi-\eta\rvert^2)(1+\lvert\xi\rvert^2)$. Raising to the power $t > 0$,
> $$(1+\lvert\eta\rvert^2)^t \le 2^t(1+\lvert\xi-\eta\rvert^2)^t(1+\lvert\xi\rvert^2)^t.$$
> Dividing both sides by the positive quantity $(1+\lvert\eta\rvert^2)^t(1+\lvert\xi\rvert^2)^t$ gives
> $$(1+\lvert\xi\rvert^2)^{-t} \le 2^t(1+\lvert\xi-\eta\rvert^2)^t(1+\lvert\eta\rvert^2)^{-t},$$
> which, since $s = -t$ and $\lvert s\rvert = t$, is exactly $(1+\lvert\xi\rvert^2)^s \le 2^{\lvert s\rvert}(1+\lvert\xi-\eta\rvert^2)^{\lvert s\rvert}(1+\lvert\eta\rvert^2)^s$. Steps 2 and 3 exhaust the sign of $s$, proving part (iii).
>
> **Part (iv).** Fix an integer $k$. Recall the pairing $\langle u, \phi\rangle = (2\pi)^n\sum_\xi\hat{u}(\xi)\overline{\hat{\phi}(\xi)}$.
>
> *Step 1 — $T(u) = \langle\cdot, u\rangle$ is a bounded functional on $H_k$ with $\lVert T(u)\rVert_{H_k^*} \le (2\pi)^n\lVert u\rVert_{-k}$.* Let $u \in H_{-k}$, with coefficients $c = \hat{u} \in \ell^2_{-k}$, and $\phi \in H_k$, with coefficients $b = \hat{\phi} \in \ell^2_k$. Splitting the weight and applying Cauchy–Schwarz,
> $$\lvert\langle\phi, u\rangle\rvert = (2\pi)^n\Big\lvert\sum_\xi\hat{\phi}(\xi)\overline{\hat{u}(\xi)}\Big\rvert = (2\pi)^n\Big\lvert\sum_\xi\big((1+\lvert\xi\rvert^2)^{k/2}b_\xi\big)\big((1+\lvert\xi\rvert^2)^{-k/2}\overline{c_\xi}\big)\Big\rvert \le (2\pi)^n\lVert\phi\rVert_k\lVert u\rVert_{-k},$$
> where the inequality is [[Thm - Cauchy-Schwarz Inequality]] for square-summable sequences, the first factor being $(\sum(1+\lvert\xi\rvert^2)^k\lvert b_\xi\rvert^2)^{1/2} = \lVert\phi\rVert_k$ and the second $(\sum(1+\lvert\xi\rvert^2)^{-k}\lvert c_\xi\rvert^2)^{1/2} = \lVert u\rVert_{-k}$. Thus $T(u) := \langle\cdot, u\rangle$ is a bounded linear functional on $H_k$ (linear in the first slot $\phi$) with operator norm at most $(2\pi)^n\lVert u\rVert_{-k}$; and $u \mapsto T(u)$ is conjugate-linear because $u$ enters through $\overline{\hat{u}(\xi)}$.
>
> *Step 2 — $T$ is onto with $\lVert T(u)\rVert_{H_k^*} = (2\pi)^n\lVert u\rVert_{-k}$.* $H_k$ is (identified with) the weighted Hilbert space $\ell^2_k$, so by Lemma 3 every bounded linear functional $\Lambda$ on $H_k$ has the form $\Lambda(\phi) = (\hat{\phi}, g)_k = \sum_\xi(1+\lvert\xi\rvert^2)^k\hat{\phi}(\xi)\overline{g_\xi}$ for a unique $g \in \ell^2_k$, with $\lVert\Lambda\rVert = \lVert g\rVert_k$. Define $u \in H_{-k}$ by $\hat{u}(\xi) := (2\pi)^{-n}(1+\lvert\xi\rvert^2)^k g_\xi$. Then
> $$\lVert u\rVert_{-k}^2 = \sum_\xi(1+\lvert\xi\rvert^2)^{-k}\lvert\hat{u}(\xi)\rvert^2 = (2\pi)^{-2n}\sum_\xi(1+\lvert\xi\rvert^2)^{-k}(1+\lvert\xi\rvert^2)^{2k}\lvert g_\xi\rvert^2 = (2\pi)^{-2n}\lVert g\rVert_k^2 < \infty,$$
> so indeed $u \in H_{-k}$ and $\lVert u\rVert_{-k} = (2\pi)^{-n}\lVert g\rVert_k$. Moreover
> $$T(u)(\phi) = \langle\phi, u\rangle = (2\pi)^n\sum_\xi\hat{\phi}(\xi)\overline{\hat{u}(\xi)} = (2\pi)^n\sum_\xi\hat{\phi}(\xi)(2\pi)^{-n}(1+\lvert\xi\rvert^2)^k\overline{g_\xi} = \sum_\xi(1+\lvert\xi\rvert^2)^k\hat{\phi}(\xi)\overline{g_\xi} = \Lambda(\phi),$$
> so $T(u) = \Lambda$; hence $T$ is onto. Its norm is $\lVert T(u)\rVert_{H_k^*} = \lVert\Lambda\rVert = \lVert g\rVert_k = (2\pi)^n\lVert u\rVert_{-k}$, which also shows $T$ is injective (a nonzero $u$ has nonzero image) and, being onto, is a conjugate-linear isomorphism, isometric up to the factor $(2\pi)^n$.
>
> *Step 3 — the sup formula.* Let $u \in H_k$, $u \ne 0$. For every $\phi \in C^\infty(T^n)$ with $\lVert\phi\rVert_{-k} \le 1$, the bound of Step 1 (with the roles of the orders $k$ and $-k$ exchanged) gives $\lvert\langle u, \phi\rangle\rvert \le (2\pi)^n\lVert u\rVert_k\lVert\phi\rVert_{-k} \le (2\pi)^n\lVert u\rVert_k$, so the supremum is at most $(2\pi)^n\lVert u\rVert_k$. To see it is attained, first suppose $u \in C^\infty(T^n)$, so $\hat{u}$ is rapidly decreasing; define $\phi$ by $\hat{\phi}(\xi) := (1+\lvert\xi\rvert^2)^k\overline{\hat{u}(\xi)}$. The sequence $\hat{\phi}$ is rapidly decreasing (a polynomial weight times a rapidly decreasing sequence is rapidly decreasing), so by ingredient (C) of Step 0, $\phi \in C^\infty(T^n)$; and
> $$\lVert\phi\rVert_{-k}^2 = \sum_\xi(1+\lvert\xi\rvert^2)^{-k}\lvert\hat{\phi}(\xi)\rvert^2 = \sum_\xi(1+\lvert\xi\rvert^2)^{-k}(1+\lvert\xi\rvert^2)^{2k}\lvert\hat{u}(\xi)\rvert^2 = \sum_\xi(1+\lvert\xi\rvert^2)^k\lvert\hat{u}(\xi)\rvert^2 = \lVert u\rVert_k^2,$$
> while, using $\overline{\hat{\phi}(\xi)} = (1+\lvert\xi\rvert^2)^k\hat{u}(\xi)$,
> $$\langle u, \phi\rangle = (2\pi)^n\sum_\xi\hat{u}(\xi)\overline{\hat{\phi}(\xi)} = (2\pi)^n\sum_\xi(1+\lvert\xi\rvert^2)^k\lvert\hat{u}(\xi)\rvert^2 = (2\pi)^n\lVert u\rVert_k^2 .$$
> Normalising, $\psi := \phi/\lVert u\rVert_k$ satisfies $\lVert\psi\rVert_{-k} = 1$ and $\langle u, \psi\rangle = (2\pi)^n\lVert u\rVert_k$, so the supremum equals $(2\pi)^n\lVert u\rVert_k$ exactly. For general $u \in H_k$ the same conclusion follows because both sides of $\lVert u\rVert_k = (2\pi)^{-n}\sup\{\lvert\langle u,\phi\rangle\rvert : \phi \in C^\infty,\ \lVert\phi\rVert_{-k}\le 1\}$ are continuous in $u$ for the $\lVert\cdot\rVert_k$-norm (the left side trivially; the right side because $u \mapsto \langle u,\phi\rangle$ is $\lVert\cdot\rVert_k$-continuous uniformly over the unit ball of test functions, by Step 1) and agree on the dense set $C^\infty(T^n)$. This proves part (iv).
>
> **Part (v).** Let $r < t < s$ be integers and $\varepsilon > 0$. Apply Lemma 4 with $a = t - r$, $b = s - r$ and the parameter $\delta := \varepsilon^2$: for every $x \ge 1$,
> $$x^t \le \varepsilon^2\, x^s + C'_{\varepsilon^2}\, x^r, \qquad C'_{\varepsilon^2} = \frac{s-t}{s-r}\left(\frac{t-r}{\varepsilon^2(s-r)}\right)^{(t-r)/(s-t)} .$$
> Set $x = 1 + \lvert\xi\rvert^2 \ge 1$, multiply by $\lvert\hat{u}(\xi)\rvert^2 \ge 0$, and sum over $\xi$:
> $$\lVert u\rVert_t^2 = \sum_\xi(1+\lvert\xi\rvert^2)^t\lvert\hat{u}(\xi)\rvert^2 \le \varepsilon^2\sum_\xi(1+\lvert\xi\rvert^2)^s\lvert\hat{u}(\xi)\rvert^2 + C'_{\varepsilon^2}\sum_\xi(1+\lvert\xi\rvert^2)^r\lvert\hat{u}(\xi)\rvert^2 = \varepsilon^2\lVert u\rVert_s^2 + C'_{\varepsilon^2}\lVert u\rVert_r^2 .$$
> Taking square roots and using the elementary inequality $\sqrt{P + Q} \le \sqrt{P} + \sqrt{Q}$ for $P, Q \ge 0$,
> $$\lVert u\rVert_t \le \sqrt{\varepsilon^2\lVert u\rVert_s^2 + C'_{\varepsilon^2}\lVert u\rVert_r^2} \le \varepsilon\,\lVert u\rVert_s + C_\varepsilon\,\lVert u\rVert_r, \qquad C_\varepsilon := \sqrt{C'_{\varepsilon^2}} .$$
> The chain of estimates was derived for $u \in C^\infty(T^n)$; since every norm involved is continuous on $H_s$ (by nesting, part (ii), $H_s \subseteq H_t, H_r$, and the inequality is preserved under the $\lVert\cdot\rVert_s$-limits that define $H_s$), the inequality extends by density to all $u \in H_s(T^n)$. This proves part (v). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The heat semigroup as a smoothing operator (parabolic partial differential equations).** Consider the heat equation $\partial_\tau v = -\Delta v$ on $T^n$, whose solution from initial data $u$ is $v(\tau) = e^{-\tau\Delta}u$, acting on the Fourier side by $\widehat{v(\tau)}(\xi) = e^{-\tau\lvert\xi\rvert^2}\hat{u}(\xi)$. The theorem applies because the Sobolev norms are the weighted-$\ell^2$ norms of part (i), so one can ask how $\lVert v(\tau)\rVert_{k+j}$ compares to $\lVert u\rVert_k$: the factor $e^{-\tau\lvert\xi\rvert^2}(1+\lvert\xi\rvert^2)^{j/2}$ is bounded uniformly in $\xi$ for each $\tau > 0$, so $e^{-\tau\Delta}$ maps $H_k$ into $H_{k+j}$ for every $j$, that is, into $C^\infty$ by part (ii). The application is non-obvious because "the heat flow instantly smooths" is usually stated as a regularity theorem, whereas here it is the visible decay of one explicit multiplier against the polynomial weight.

**Spectral gaps and the Poincaré inequality (spectral geometry).** On $T^n$ the Laplacian $\Delta = -\sum\partial_j^2$ has eigenvalues $\lvert\xi\rvert^2$, and the mean-zero condition $\hat{u}(0) = 0$ removes the only frequency where the weight $\lvert\xi\rvert^2$ vanishes. The theorem applies because part (i) turns $\lVert\nabla u\rVert_{L^2}^2 = (2\pi)^n\sum_\xi\lvert\xi\rvert^2\lvert\hat{u}(\xi)\rvert^2$ and $\lVert u\rVert_{L^2}^2 = (2\pi)^n\sum_\xi\lvert\hat{u}(\xi)\rvert^2$ into sums one can compare term by term; for mean-zero $u$ every nonzero $\xi$ has $\lvert\xi\rvert \ge 1$, giving the Poincaré inequality $\lVert u\rVert_{L^2} \le \lVert\nabla u\rVert_{L^2}$. The non-obvious point is that the sharp constant is read straight off the smallest nonzero eigenvalue, which is exactly the smallest nonzero value of the weight.

**Weak solutions and the Lax–Milgram setting (functional analysis of elliptic problems).** A weak formulation of $\Delta u + u = f$ seeks $u$ with $\langle u, \phi\rangle_{H_1} = \langle f, \phi\rangle$ for all test $\phi$, that is, prescribes a functional on $H_1$. The theorem applies through part (iv): the right-hand side is an element of $H_{-1}$, and the bilinear form $\langle\cdot,\cdot\rangle_{H_1}$ is exactly the weighted inner product $(\cdot,\cdot)_1$, so the existence of $u$ is Riesz representation on $\ell^2_1$ — precisely Lemma 3. The application is non-obvious because the abstract Lax–Milgram theorem is usually invoked as a black box, whereas on the torus it degenerates into the concrete statement that a bounded functional on a weighted-$\ell^2$ space is a pairing, with the solution's coefficients written down explicitly.

---

# Bridges

- **[[Thm - Sobolev Embedding Theorem]]** — the immediate payoff of parts (i) and (iii)–(ii). On the torus one bounds $\sup_x\lvert\partial^\alpha u\rvert \le \sum_\xi\lvert\xi\rvert^{\lvert\alpha\rvert}\lvert\hat{u}(\xi)\rvert$ and applies Cauchy–Schwarz against the weight $(1+\lvert\xi\rvert^2)^{r-k}$; the leftover sum converges exactly when $2(k - r) > n$, which is the embedding $H_k \hookrightarrow C^r$. The construction is the same weight-splitting used in part (ii), Step 3, and it is the reason the strict inequality $k - r > n/2$ cannot be relaxed.

- **[[Thm - Rellich Compactness Theorem]]** — built from part (i) and the finite-rank truncations $T_R u = \sum_{\lvert\xi\rvert\le R}\hat{u}(\xi)e^{i\langle\xi,x\rangle}$. Part (i) makes $\lVert u - T_R u\rVert_m^2 = \sum_{\lvert\xi\rvert>R}(1+\lvert\xi\rvert^2)^m\lvert\hat{u}\rvert^2 \le (1+R^2)^{m-k}\lVert u\rVert_k^2$ for $k > m$, so $\lVert\iota - T_R\rVert_{H_k\to H_m}\le(1+R^2)^{(m-k)/2}\to 0$; the inclusion is a norm limit of finite-rank operators, hence compact.

- **[[Thm - Sobolev Multiplication Theorem]]** — powered by Peetre's inequality, part (iii). Writing $\widehat{uv}(\xi) = \sum_\eta\hat{u}(\xi-\eta)\hat{v}(\eta)$ and inserting the weight $(1+\lvert\xi\rvert^2)^{k/2}$, part (iii) with $s = k$ splits that weight between the two factors as $(1+\lvert\xi-\eta\rvert^2)^{k/2}$ and $(1+\lvert\eta\rvert^2)^{k/2}$; a Cauchy–Schwarz against a summable weight, whose summability consumes the excess regularity $k_1 + k_2 - k > n/2$, then closes the estimate $H_{k_1}\cdot H_{k_2}\subseteq H_k$.

- **[[Thm - Sobolev Spaces of Sections on a Compact Manifold via Charts]]** — the export mechanism. It patches the torus spaces $H_k(T^n)$ by a finite atlas and a partition of unity into $H_k(M; E)$ on any compact manifold, so that every "on a compact manifold" statement of the chapter reduces to its torus counterpart proved here; in particular the manifold duality and interpolation statements are transported from parts (iv) and (v).

---

# Unlocked by This

> [!tip] The Sobolev scale as a Hilbert scale *(from functional analysis)*
> Parts (i), (ii), and (iv) exhibit $\{H_k(T^n)\}_{k\in\mathbb{Z}}$ as a **Hilbert scale**: a family of Hilbert spaces indexed by a real parameter, nested, with $H_{-k}$ the dual of $H_k$ and the pairing between them, generated by the single positive self-adjoint operator $(1-\Delta)$ acting as multiplication by $(1+\lvert\xi\rvert^2)$ on the Fourier side. Interpolation, part (v), is the logarithmic convexity of the norms along the scale. This is the model on which the abstract theory of interpolation spaces is built.

> [!tip] Negative-order spaces without distribution theory *(from partial differential equations)*
> Part (iv) realises the dual $H_k^*$ concretely as $H_{-k}$, a space of ordinary coefficient sequences, so the elements of $H_{-k}$ for $k > 0$ — which one would otherwise introduce as distributions of order $k$ — are available in this chapter with no distribution theory at all. Every weak formulation of an elliptic equation on the torus lives inside this concrete duality, which is why the chapter can prove elliptic regularity by hand.
