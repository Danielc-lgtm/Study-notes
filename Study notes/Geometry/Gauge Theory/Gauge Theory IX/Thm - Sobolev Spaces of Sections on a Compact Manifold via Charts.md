---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Sobolev Norms on the Torus via Fourier Coefficients"
  - "Thm - Sobolev Norms are Independent of the Metric and Connections up to Equivalence"
  - "Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order"
  - "Def - Sobolev Space of Sections"
  - "Def - Partition of Unity on a Manifold"
  - "Thm - Existence of Smooth Partitions of Unity"
  - "Def - Local Trivialization"
  - "Def - Section of a Vector Bundle"
tags: [geometry, gauge-theory, analysis, sobolev-spaces]
---

# Notation

Throughout, $M$ is a smooth, compact, Hausdorff, second-countable $n$-manifold without boundary, and $E \to M$ is a smooth [[Def - Vector Bundle|vector bundle]] of rank $r$ over $M$. We write $\Gamma(E)$ for the space of smooth [[Def - Section of a Vector Bundle|sections]] of $E$; since $M$ is compact every smooth section is automatically compactly supported. We take $E$ to be a real bundle, so that a fibre is $\mathbb{R}^r$; the complex case is identical after replacing $\mathbb{R}^r$ by $\mathbb{C}^r = \mathbb{R}^{2r}$, and we say so once where it matters. We fix once and for all a [[Def - Riemannian Metric|Riemannian metric]] $g$ on $M$, a fibre metric $h$ on $E$, and a [[Def - Connection on a Vector Bundle|connection]] $\nabla^E$ on $E$ together with the Levi-Civita connection $\nabla^M$ on $T^*M$; these data define the connection Sobolev norm $\lVert\cdot\rVert_{W^{k,2}}$ of [[Def - Sobolev Space of Sections]], and by [[Thm - Sobolev Norms are Independent of the Metric and Connections up to Equivalence]] a different choice changes that norm only up to a bounded factor in each direction.

**The torus and its Sobolev scale.** We write $T^n := \mathbb{R}^n / 2\pi\mathbb{Z}^n$ for the flat $n$-torus, and we regard the open cube $(-\pi,\pi)^n$ as an open subset of $T^n$ through the quotient map, so that a function on $(-\pi,\pi)^n$ with compact support extends by zero to a smooth function on all of $T^n$. For $w \in C^\infty(T^n;\mathbb{C})$ the Fourier coefficients are $\hat w(\xi) := (2\pi)^{-n}\int_{T^n} w(x)\,e^{-i\langle\xi,x\rangle}\,dx$, indexed by $\xi \in \mathbb{Z}^n$, and for every integer $k$ the torus Sobolev norm is
$$\lVert w\rVert_k^2 := \sum_{\xi\in\mathbb{Z}^n}(1+|\xi|^2)^k\,|\hat w(\xi)|^2,$$
with $H_k(T^n;\mathbb{C})$ the completion of $C^\infty(T^n;\mathbb{C})$ in $\lVert\cdot\rVert_k$; these are the objects of [[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order]]. For $\mathbb{C}^r$-valued data $w = (w^1,\dots,w^r)$ we set $\lVert w\rVert_{H_k(T^n;\mathbb{C}^r)}^2 := \sum_{a=1}^r\lVert w^a\rVert_k^2$, and $H_k(T^n;\mathbb{C}^r) := \bigoplus_{a=1}^r H_k(T^n;\mathbb{C})$. The bilinear-in-the-first-slot torus pairing is $\langle w, \varphi\rangle_{T^n} := (2\pi)^n\sum_{\xi} \hat w(\xi)\,\overline{\hat\varphi(\xi)}$, which for smooth $w,\varphi$ equals $\int_{T^n}\langle w,\varphi\rangle_{\mathbb{C}^r}\,dx$ by Parseval.

**The atlas, the trivialisations, the partition of unity.** By compactness we may and do fix a *finite* atlas: charts $\kappa_i : U_i \to \kappa_i(U_i) \subset (-\pi,\pi)^n \subset T^n$ for $i = 1,\dots,N$, with $M = \bigcup_i U_i$, over each of which $E$ is [[Def - Local Trivialization|trivialised]] by a smooth [[Def - Local Frame|local frame]] $e^{(i)} = (e^{(i)}_1,\dots,e^{(i)}_r)$, giving a fibrewise identification $E|_{U_i} \cong U_i \times \mathbb{R}^r$. We fix a smooth [[Def - Partition of Unity on a Manifold|partition of unity]] $(\phi_i)_{i=1}^N$ subordinate to $(U_i)$, so $\phi_i \in C^\infty(M)$, $0 \le \phi_i \le 1$, $\operatorname{supp}\phi_i \subset U_i$ compact, and $\sum_i \phi_i \equiv 1$; such a family exists by [[Thm - Existence of Smooth Partitions of Unity]]. The whole package — metric, fibre metric, connections, atlas, trivialisations, partition of unity — will be called the *data* and denoted $\mathcal{D}$.

**The localised section and the chart norm.** For $u \in \Gamma(E)$ the product $\phi_i u \in \Gamma(E)$ is supported in $U_i$; reading it in the frame $e^{(i)}$ gives an $\mathbb{R}^r$-valued function on $U_i$, and transporting through the chart yields
$$u_i := (\phi_i u)\circ\kappa_i^{-1} \in C^\infty\big(\kappa_i(U_i);\mathbb{R}^r\big), \qquad\text{extended by zero to } C^\infty(T^n;\mathbb{R}^r)\subset C^\infty(T^n;\mathbb{C}^r).$$
The extension is smooth because $\operatorname{supp}(\phi_i u)$ is a compact subset of $U_i$, so $u_i$ has compact support inside the open cube $\kappa_i(U_i)$. The *chart norm* of order $k \in \mathbb{Z}$ attached to $\mathcal{D}$ is
$$\lVert u\rVert_{(k)}^2 := \sum_{i=1}^N \big\lVert u_i\big\rVert_{H_k(T^n;\mathbb{C}^r)}^2, \qquad u \in \Gamma(E).$$
The map $R_i : u \mapsto u_i$ is the *localisation operator* of the $i$-th chart. When two data packages appear we decorate the second with a prime: $\mathcal{D}'$, $\kappa_i'$, $\phi_j'$, $u_j' = (\phi_j' u)\circ\kappa_j'^{-1}$, $\lVert\cdot\rVert'_{(k)}$.

**The manifold $L^2$ pairing.** For $u,v \in \Gamma(E)$ we write $(u,v)_{L^2} := \int_M \langle u,v\rangle_h\,\mathrm{vol}_g$, the real pairing built from the fibre metric $h$ and the [[Def - Riemannian Metric|Riemannian]] volume form $\mathrm{vol}_g$. The associated norm is $\lVert u\rVert_{L^2} = (u,u)_{L^2}^{1/2}$, which is $\lVert u\rVert_{W^{0,2}}$.

> [!warning] Convention: $L^2$-based scale only
> Following the series design (group decision 2), every Sobolev space in this chapter is built on $p = 2$: we write $H_k(M;E) := W^{k,2}(M;E)$ for $k \ge 0$ and extend the scale to negative $k$ by the duality proved below. Haydys, *Introduction to Gauge Theory*, Theorem 136, records the general-$p$ statements $W^{k,p}(M;E)$; those are context and are not proved or used here. The identification of the abstract completion $L^2$ with the Lebesgue space $L^2(M;E)$ (Riesz–Fischer together with the density of smooth sections, e.g. Folland, *Real Analysis*, Theorem 6.6 and Proposition 8.17) is likewise recorded and not used: every estimate below is proved for *smooth* sections and extended by continuity, so no measure theory intervenes.

---

# Statement

> **Theorem (Sobolev spaces of sections on a compact manifold via charts).** Let $M$ be a compact $n$-manifold, $E \to M$ a real vector bundle of rank $r$, and $\mathcal{D}$ a data package (finite atlas $\kappa_i : U_i \to \kappa_i(U_i)\subset(-\pi,\pi)^n\subset T^n$ trivialising $E$, subordinate partition of unity $(\phi_i)$, metrics, connections) as in the Notation. For $k \in \mathbb{Z}$ define $\lVert u\rVert_{(k)}^2 = \sum_i \lVert (\phi_i u)\circ\kappa_i^{-1}\rVert_{H_k(T^n;\mathbb{C}^r)}^2$ on $\Gamma(E)$. Then:
>
> **(i) Agreement with the connection norm for $k \ge 0$.** For each integer $k \ge 0$ there are constants $0 < c_k \le C_k$, depending on $\mathcal{D}$, with
> $$c_k\,\lVert u\rVert_{W^{k,2}} \;\le\; \lVert u\rVert_{(k)} \;\le\; C_k\,\lVert u\rVert_{W^{k,2}} \qquad\text{for all } u \in \Gamma(E).$$
>
> **(ii) Independence of the data; the space $H_k(M;E)$.** For every integer $k$, the chart norms $\lVert\cdot\rVert_{(k)}$ and $\lVert\cdot\rVert'_{(k)}$ built from two data packages $\mathcal{D}, \mathcal{D}'$ are equivalent on $\Gamma(E)$. Consequently the completion
> $$H_k(M;E) := \overline{\big(\Gamma(E),\ \lVert\cdot\rVert_{(k)}\big)}$$
> is a topological vector space independent of $\mathcal{D}$, and it is *Hilbertable*: each $\lVert\cdot\rVert_{(k)}$ is the norm of an inner product, so $H_k(M;E)$ carries a compatible Hilbert-space structure (canonical only up to the equivalence). For $k \ge 0$ one has $H_k(M;E) = W^{k,2}(M;E)$ with equivalent norms.
>
> **(iii) Density and the descending scale.** $\Gamma(E)$ is dense in $H_k(M;E)$ for every $k$; and for integers $k \ge m$ the inclusion $\Gamma(E) \hookrightarrow \Gamma(E)$ extends to a continuous injection $H_k(M;E) \hookrightarrow H_m(M;E)$ with $\lVert u\rVert_{(m)} \le C\,\lVert u\rVert_{(k)}$.
>
> **(iv) Duality: a perfect pairing.** The $L^2$ pairing $(\,\cdot\,,\,\cdot\,)_{L^2} : \Gamma(E)\times\Gamma(E) \to \mathbb{R}$ extends, for every integer $k$, to a continuous bilinear pairing
> $$(\,\cdot\,,\,\cdot\,) : H_k(M;E) \times H_{-k}(M;E) \longrightarrow \mathbb{R}, \qquad |(u,v)| \le C\,\lVert u\rVert_{(k)}\,\lVert v\rVert_{(-k)},$$
> which is *perfect*: the induced map $v \mapsto (\,\cdot\,,v)$ is a topological isomorphism $H_{-k}(M;E) \xrightarrow{\ \cong\ } \big(H_k(M;E)\big)^*$ onto the continuous dual.
>
> **(v) Bounded multipliers and bundle maps.** For every integer $k$, multiplication by a smooth function $f \in C^\infty(M)$ is bounded $H_k(M;E) \to H_k(M;E)$; more generally, a smooth bundle map $\Psi : E \to F$ (a smooth section of $\operatorname{Hom}(E,F)$) induces a bounded operator $H_k(M;E) \to H_k(M;F)$.
>
> **(vi) Interpolation.** For integers $r < t < s$ and every $\varepsilon > 0$ there is a constant $C_\varepsilon$ with $\lVert u\rVert_{(t)} \le \varepsilon\,\lVert u\rVert_{(s)} + C_\varepsilon\,\lVert u\rVert_{(r)}$ for all $u \in H_s(M;E)$.

The construction and its verification follow Lawson and Michelsohn, *Spin Geometry*, III.§5 (the discussion after Definition 5.1), and Wells, *Differential Analysis on Complex Manifolds*, Chapter IV §1.

---

# Motivation

The previous four pages of this section built a complete, computable Sobolev theory, but only on one very special space: the flat torus $T^n$, where the [[Thm - Fourier Series of Smooth Functions on the Torus|Fourier transform]] turns differentiation into multiplication by $i\xi$ and turns the Sobolev norm into a weighted $\ell^2$ norm on the lattice $\mathbb{Z}^n$. Everything one wants — the exact size of each derivative, the [[Thm - Sobolev Norms on the Torus via Fourier Coefficients|equivalence of the Fourier norm with the raw derivative norm]], the negative-order spaces, the duality, the interpolation inequality — is transparent there because it is arithmetic on a sequence. But gauge theory does not take place on a torus. It takes place on the total space of sections of a bundle over a compact four-manifold, and we need the full analytic apparatus there: the [[Thm - Sobolev Embedding Theorem|embedding into continuous sections]], the [[Thm - Rellich Compactness Theorem|Rellich compactness]] of the inclusions, [[Thm - Elliptic Regularity and the Elliptic Estimate|elliptic regularity]], the [[Thm - Elliptic Operators on Closed Manifolds are Fredholm|Fredholm property]]. This page is the single bridge that carries the entire torus theory across to that setting.

The question it answers is exactly this: *how should one even define $W^{k,2}(M;E)$ so that the torus results transfer, and does the definition depend on the arbitrary choices one is forced to make?* There are two candidate definitions, and the whole content of the theorem is that they agree. The first is intrinsic: differentiate a section $k$ times with a fixed connection, measure each derivative in $L^2$ against a fixed metric, and add up. This is the definition of [[Def - Sobolev Space of Sections]], and it is manifestly geometric, but it is useless for negative orders and it hides the Fourier machinery. The second is extrinsic and computational: chop a section into finitely many pieces by a partition of unity, flatten each piece onto the torus through a chart, and add up the torus norms. This is the chart norm $\lVert\cdot\rVert_{(k)}$; it inherits *every* torus theorem for free but appears to depend on a mountain of arbitrary choices — which charts, which frames, which bump functions.

Part (i) says the two definitions give the same topology for $k \ge 0$, so the geometric object and the computable object coincide. Part (ii) says the computable object does not remember the choices. Together they let us *define* the negative-order spaces $H_{-k}(M;E)$ — which have no derivative-counting description at all — by transport from the torus, and part (iv) identifies them as the duals of the positive-order spaces, exactly as on the torus. From this page onward, every statement of the form "on a compact manifold, such-and-such Sobolev estimate holds" is proved by cutting the section into chart pieces, invoking the corresponding torus statement on each piece, and reassembling; the reassembly is always bounded because the only maps involved — multiplication by a bump function and composition with a transition diffeomorphism — are smooth, and this theorem records once and for all that smooth maps act boundedly on every $H_k$.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is a compact manifold with a bundle, an atlas, and a partition of unity. The interesting question is which analytic problems secretly present themselves in this form.

The first disguised source is **any elliptic boundary-free problem posed on a closed manifold**. A problem given as "find a section $u$ minimising $\int_M |\nabla u|^2 + \dots$" or "solve $Lu = f$ for an [[Def - Elliptic Differential Operator and Principal Symbol|elliptic operator]] $L$" does not mention Sobolev spaces at all, yet the only function spaces in which such problems are well posed are the $H_k(M;E)$ built here; the bridge $B \Rightarrow A$ is that the variational or PDE formulation forces one to complete $\Gamma(E)$ in a derivative norm, and this theorem certifies that the completion is intrinsic. *Example problem:* the Dirichlet-type energy $E(u) = \tfrac12\int_M |\nabla u|^2\,\mathrm{vol}$ has no minimiser in $C^2$ (minimising sequences need not converge in the $C^2$ norm), but it has one in $H_1(M;E)$ precisely because that space is complete and, by part (iv), reflexive.

The second disguised source is **a family of sections whose Fourier tails one can control chart by chart**. Whenever one has, on each chart, a uniform bound on the high-frequency Fourier mass of the localised pieces $u_i$, part (ii) turns those local bounds into a global $H_k$ bound; the bridge is that the global norm is, by definition, the sum of the local torus norms. *Example problem:* to show a sequence of connections has an $H_k$-bounded subsequence, one bounds each $(\phi_i A)\circ\kappa_i^{-1}$ in $H_k(T^n)$ using the torus theory and sums — this is the first step of every compactness argument in the chapter.

The third disguised source is **a nonlinear map between section spaces built from pointwise operations**, such as the [[Thm - Sobolev Multiplication Theorem|multiplication]] appearing in the Seiberg–Witten map $\psi \mapsto \psi\otimes\psi^*$. Such maps are defined fibrewise and so are smooth bundle maps in disguise; part (v) certifies that the algebraic operations they are built from act boundedly on each $H_k$. The bridge $B \Rightarrow A$ is that a fibrewise-polynomial operation is a smooth bundle map, hence a bounded multiplier once the multiplication theorem supplies the bilinear estimate. *Example problem:* the quadratic term of the Seiberg–Witten equations is bounded $H_k \to H_k$ for $2k > n$ by combining part (v) here with the algebra property of $H_k$.

**Targets (Output Amplification).** The bare conclusion is an intrinsic, self-dual scale of Hilbert spaces with bounded multipliers. Combined with other ingredients it produces the working theorems of the chapter.

Combine the theorem with **the torus embedding $H_k(T^n) \hookrightarrow C^r(T^n)$**. Parts (i)–(iii) reduce the [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]] on $M$ to its torus statement chart by chart: the extra ingredient is the finite-atlas decomposition, and the payoff is the continuous inclusion $H_k(M;E) \hookrightarrow C^r(M;E)$ for $k - n/2 > r$, from which the smoothness of solutions of elliptic equations ultimately follows.

Combine the theorem with **the finite-rank truncation of the identity on the torus**. Part (ii) writes the inclusion $H_k(M;E) \hookrightarrow H_m(M;E)$ as a finite sum of transported torus inclusions; the extra ingredient is that on the torus the inclusion is a norm-limit of finite-rank operators, and the payoff is the [[Thm - Rellich Compactness Theorem|Rellich compactness theorem]] on $M$, the engine of every moduli-space compactness result.

Combine the theorem with **an elliptic operator and its formal adjoint**. Part (iv), the perfect pairing, is what lets an [[Def - Elliptic Differential Operator and Principal Symbol|elliptic operator]] be studied through its adjoint on the negative-order spaces: the extra ingredient is the integration-by-parts identity $(Lu,\phi) = (u, L^*\phi)$, and the payoff is that $L : H_{k+\ell}(M;E) \to H_k(M;F)$ has a well-defined [[Def - Fredholm Operator and Index|adjoint]] and a Fredholm theory. Without the duality of this page the negative-order half of the elliptic package could not even be stated.

---

# Why Is It True

Strip away the bundle and the derivatives and look at what a compact manifold *is* to a Sobolev norm. A partition of unity writes any section as a finite sum $u = \sum_i \phi_i u$ of pieces, each living in a single coordinate patch; a chart flattens each patch onto a piece of the torus. So a section on $M$ is nothing but a finite tuple of compactly supported functions on $T^n$, glued along overlaps. The gluing is done by exactly two kinds of map: multiplying by a smooth bump function (when we cut with $\phi_i$ or recombine), and composing with a smooth transition diffeomorphism $\kappa_i\circ\kappa_j^{-1}$ (when we compare the description in one chart with the description in another). The single fact that makes the whole transfer work is that *these two operations are bounded on every torus Sobolev space, of every order, positive or negative*.

> A compact manifold is finitely many pieces of a torus glued by smooth maps, and a Sobolev norm sees a smooth map only as a bounded operator; so every torus estimate survives the gluing, uniformly, because there are only finitely many pieces.

That the two gluing operations are bounded is itself two clean facts. Multiplication by a smooth $\phi$ is bounded because differentiating $\phi u$ spreads at most the derivatives of $u$ around by the Leibniz rule (for $k \ge 0$), and because multiplication is self-adjoint under the $L^2$ pairing, so the negative-order bound is the positive-order bound read through the [[Thm - Sobolev Norms on the Torus via Fourier Coefficients|duality]]. Composition with a diffeomorphism $\psi$ is bounded because the chain rule expresses the derivatives of $u\circ\psi$ as bounded combinations of the derivatives of $u$ pulled back (for $k \ge 0$), and because the change-of-variables formula turns the pairing with $u\circ\psi$ into a pairing with a transported test function (for $k < 0$). Everything else on the page — that the definition ignores the choices, that the spaces are dual, that smooth bundle maps are bounded — is bookkeeping built on those two facts and the finiteness of the atlas.

The one genuinely non-formal point is the duality (iv), and its mechanism is worth isolating. To recover the representing section $v$ of a functional on $H_k(M;E)$, one localises the functional to each chart, represents it there by a torus element $g_i \in H_{-k}(T^n)$ using the torus duality, and spreads the $g_i$ back onto $M$. The spreading must undo the localisation exactly, and $\sum_i \phi_i u = u$ is *not* enough for that, because localising and then spreading naively reproduces $\sum_i \phi_i^2 u$, not $u$. The repair is to spread with the *renormalised* weights $\theta_i = \phi_i / \sum_j \phi_j^2$, whose denominator is smooth and strictly positive because at every point some $\phi_j$ is positive; then $\sum_i \theta_i \phi_i = 1$ and the spreading is a genuine inverse of the localisation. This little renormalisation is the entire subtlety of the perfect-pairing statement.

---

# What Makes This Hard

The non-obvious step is the negative-order theory. For $k \ge 0$ everything reduces to the Leibniz and chain rules on smooth functions, but $H_{-k}(M;E)$ has no derivative-counting definition; it exists only as a completion transported from the torus, and its multiplier and composition bounds must be obtained *by duality*, taking the adjoint of the corresponding positive-order operator with respect to the $L^2$ pairing. The common error is to try to bound $\lVert \phi u\rVert_{(-k)}$ or $\lVert u\circ\psi\rVert_{(-k)}$ directly with a Leibniz-type estimate, which is meaningless for a distributional element; one must instead pass to the transposed operator and use its already-proved positive-order bound. The second trap is the perfect-pairing statement, where localising and spreading with the raw partition of unity reproduces $\sum_i \phi_i^2 u$ rather than $u$: the fix is the renormalisation $\theta_i = \phi_i/\sum_j \phi_j^2$, and forgetting it produces a "duality isomorphism" that is off by a bounded but non-identity factor and so fails to be canonical.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove two atomic boundedness facts on the torus — multiplication by a smooth function and composition with a diffeomorphism are bounded on every $H_k(T^n)$, positive and negative order — then observe that the localisation and spreading operators between $\Gamma(E)$ and finitely many copies of $C^\infty(T^n;\mathbb{C}^r)$ are built solely from those two operations. Every clause of the theorem is then a finite-sum manipulation of these bounded operators, with the single extra idea (the renormalised partition of unity) needed only for the duality.

**Subgoal decomposition:**

1. **Multiplication is bounded on $H_k(T^n)$, all $k$.**
   - *Hint:* For $k \ge 0$ use the Leibniz rule and the equivalence of the torus Fourier norm with the derivative norm; for $k < 0$ take the adjoint under the pairing and reduce to the case $-k > 0$.
   - *Why needed:* Cutting with $\phi_i$ and recombining is multiplication by a smooth function; every part of the proof uses it.

2. **Composition with a diffeomorphism is bounded on $H_k(T^n)$, all $k$.**
   - *Hint:* For $k \ge 0$ apply the chain rule and change of variables; for $k < 0$ dualise against the transposed map $\varphi \mapsto |\det D\psi^{-1}|\,(\varphi\circ\psi^{-1})$.
   - *Why needed:* Comparing the description of a section in two overlapping charts is composition with the transition map.

3. **Localisation and spreading operators are bounded, and spreading inverts localisation.**
   - *Hint:* $R_i u = (\phi_i u)\circ\kappa_i^{-1}$ and $S_i w = \theta_i\,\Phi_i(w)$ with $\theta_i = \phi_i/\sum_j\phi_j^2$; boundedness is Subgoals 1–2, and $\sum_i S_i R_i = \mathrm{id}$ because $\sum_i \theta_i\phi_i = 1$.
   - *Why needed:* These operators are the passage between the manifold and the torus; every clause is phrased through them.

4. **Assemble parts (i)–(vi).** Equivalence with the connection norm from the chain rule and the [[Thm - Sobolev Norms are Independent of the Metric and Connections up to Equivalence|equivalence theorem]]; independence of the data, density, the descending inclusion, boundedness of bundle maps, and interpolation from Subgoals 1–3 and the torus statements; the perfect pairing from the torus duality, the renormalised spreading, and the transport of the pairing.
   - *Hint:* Every "on $M$" statement is $\sum_i$ (a torus statement applied to $R_i u$), bounded because $N$ is finite.
   - *Why needed:* This is the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: Multiplication by a smooth function is bounded on every torus Sobolev space
> **Statement:** Let $\phi \in C^\infty(T^n;\mathbb{C})$ and $k \in \mathbb{Z}$. Then there is a constant $C = C(\phi,k)$ with $\lVert \phi w\rVert_k \le C\,\lVert w\rVert_k$ for all $w \in C^\infty(T^n;\mathbb{C})$; hence multiplication by $\phi$ extends to a bounded operator on $H_k(T^n;\mathbb{C})$, and componentwise to a bounded operator on $H_k(T^n;\mathbb{C}^r)$ (multiplication by a smooth matrix-valued function likewise).
>
> **Hint:** Positive order by the Leibniz rule and the [[Thm - Sobolev Norms on the Torus via Fourier Coefficients|torus norm equivalence]]; negative order by taking the adjoint of multiplication under the $L^2$ pairing.
>
> **Why needed:** Cutting a section with $\phi_i$, recombining with $\theta_i$, and applying a smooth bundle map all reduce to this bound; it is used in every subsequent lemma and in parts (i), (ii), (iv), (v).
>
> > [!note]- Full proof
> > We prove the scalar statement; the $\mathbb{C}^r$ and matrix versions follow by summing over the finitely many components.
> >
> > **Case $k \ge 0$.** By part (i) of [[Thm - Sobolev Norms on the Torus via Fourier Coefficients]] — for an integer $k \ge 0$ and $w \in C^\infty(T^n)$ the Fourier norm and the flat derivative norm are equivalent, $c_k\lVert w\rVert_k \le \big(\sum_{|\alpha|\le k}\lVert\partial^\alpha w\rVert_{L^2}^2\big)^{1/2} \le C_k\lVert w\rVert_k$ — it suffices to bound the flat derivative norm of $\phi w$. By the Leibniz rule, for every multi-index $\alpha$ with $|\alpha| \le k$,
> > $$\partial^\alpha(\phi w) = \sum_{\beta \le \alpha}\binom{\alpha}{\beta}(\partial^{\alpha-\beta}\phi)(\partial^\beta w) \qquad\text{(Leibniz rule for iterated partial derivatives).}$$
> > Taking $L^2(T^n)$ norms and using the triangle inequality together with $\lVert(\partial^{\alpha-\beta}\phi)\,\partial^\beta w\rVert_{L^2} \le \lVert\partial^{\alpha-\beta}\phi\rVert_{C^0}\,\lVert\partial^\beta w\rVert_{L^2}$ (a smooth function on the compact torus is bounded, so $\lVert\partial^{\alpha-\beta}\phi\rVert_{C^0} < \infty$),
> > $$\lVert\partial^\alpha(\phi w)\rVert_{L^2} \le \sum_{\beta\le\alpha}\binom{\alpha}{\beta}\lVert\partial^{\alpha-\beta}\phi\rVert_{C^0}\,\lVert\partial^\beta w\rVert_{L^2} \le C'\!\!\sum_{|\beta|\le k}\lVert\partial^\beta w\rVert_{L^2} \qquad\text{(triangle inequality; boundedness of the derivatives of }\phi\text{),}$$
> > with $C'$ the finite maximum of the $\binom{\alpha}{\beta}\lVert\partial^{\alpha-\beta}\phi\rVert_{C^0}$ over the finitely many $\beta\le\alpha$, $|\alpha|\le k$. Summing the squares over $|\alpha|\le k$ and applying the norm equivalence at both ends gives $\lVert\phi w\rVert_k \le C\lVert w\rVert_k$.
> >
> > **Case $k < 0$.** Write $k = -m$ with $m > 0$. Part (iv) of [[Thm - Sobolev Norms on the Torus via Fourier Coefficients]] gives the duality characterisation of the norm: for $w \in C^\infty(T^n)$,
> > $$\lVert w\rVert_{-m} = \sup\Big\{\tfrac{1}{(2\pi)^n}\,|\langle w,\varphi\rangle_{T^n}| : \varphi\in C^\infty(T^n),\ \lVert\varphi\rVert_{m}\le 1\Big\}.$$
> > For smooth $\phi,w,\varphi$ the pairing satisfies the adjoint identity
> > $$\langle \phi w, \varphi\rangle_{T^n} = \int_{T^n}(\phi w)\,\overline{\varphi}\,dx = \int_{T^n} w\,\overline{\bar\phi\,\varphi}\,dx = \langle w, \bar\phi\,\varphi\rangle_{T^n} \qquad\text{(Parseval writes the pairing as an integral; }\phi\overline{\varphi} = \overline{\bar\phi\varphi}\text{).}$$
> > Hence
> > $$\lVert \phi w\rVert_{-m} = \sup_{\lVert\varphi\rVert_m\le 1}\tfrac{1}{(2\pi)^n}|\langle w,\bar\phi\varphi\rangle_{T^n}| \le \sup_{\lVert\varphi\rVert_m\le 1}\lVert w\rVert_{-m}\,\lVert\bar\phi\varphi\rVert_m \qquad\text{(pairing bound }|\langle w,\eta\rangle_{T^n}|\le(2\pi)^n\lVert w\rVert_{-m}\lVert\eta\rVert_m\text{ from the torus definition).}$$
> > By the case $k = m \ge 0$ already proved, applied to the smooth multiplier $\bar\phi$, we have $\lVert\bar\phi\varphi\rVert_m \le C\lVert\varphi\rVert_m \le C$ whenever $\lVert\varphi\rVert_m \le 1$. Therefore $\lVert\phi w\rVert_{-m} \le C\lVert w\rVert_{-m}$. In both cases the bound is uniform over smooth $w$, so multiplication by $\phi$ extends by continuity to a bounded operator on the completion $H_k(T^n)$. $\blacksquare$

> [!note]- Lemma 2: Composition with a diffeomorphism is bounded on every torus Sobolev space
> **Statement:** Let $V, V' \subset (-\pi,\pi)^n$ be open and $\psi : V \to V'$ a diffeomorphism, and let $k \in \mathbb{Z}$. There is a constant $C = C(\psi,k)$ such that for every $w \in C^\infty(T^n;\mathbb{C})$ with $\operatorname{supp} w \subset V'$ compact, the function $w\circ\psi$ (extended by zero to $T^n$) satisfies $\lVert w\circ\psi\rVert_k \le C\,\lVert w\rVert_k$.
>
> **Hint:** Positive order by the chain rule and the change-of-variables formula; negative order by dualising against the transposed pullback $\varphi \mapsto |\det D\psi^{-1}|\,(\varphi\circ\psi^{-1})$.
>
> **Why needed:** Comparing the two chart descriptions of a section is composition with the transition diffeomorphism $\kappa_i\circ\kappa_j^{-1}$; it drives the independence-of-data statement and the duality.
>
> > [!note]- Full proof
> > Since $\operatorname{supp} w$ is a compact subset of the open set $V'$ and $\psi$ is a diffeomorphism, $\operatorname{supp}(w\circ\psi) = \psi^{-1}(\operatorname{supp} w)$ is a compact subset of $V \subset (-\pi,\pi)^n$, so $w\circ\psi$ extends by zero to a smooth function on $T^n$; all integrals below are over the compact set $\overline{V}$ where the integrands are supported.
> >
> > **Case $k \ge 0$: the $L^2$ change of variables.** For $k = 0$, part (iii) (Parseval) of [[Thm - Fourier Series of Smooth Functions on the Torus]] gives $\lVert\cdot\rVert_0 = (2\pi)^{-n/2}\lVert\cdot\rVert_{L^2}$, and the change of variables $x = \psi^{-1}(y)$ (Jacobian factor $|\det D\psi^{-1}(y)|$, a positive smooth function bounded on the compact $\operatorname{supp} w$) yields
> > $$\lVert w\circ\psi\rVert_{L^2}^2 = \int_V |w(\psi(x))|^2\,dx = \int_{V'} |w(y)|^2\,|\det D\psi^{-1}(y)|\,dy \le \big(\sup_{V'}|\det D\psi^{-1}|\big)\,\lVert w\rVert_{L^2}^2 \qquad\text{(change of variables; boundedness of the Jacobian).}$$
> >
> > **Case $k \ge 0$: higher derivatives by the chain rule.** By part (i) of [[Thm - Sobolev Norms on the Torus via Fourier Coefficients]] it suffices to bound $\sum_{|\alpha|\le k}\lVert\partial^\alpha(w\circ\psi)\rVert_{L^2}$. The multivariate chain rule (Faà di Bruno) expresses each such derivative as
> > $$\partial^\alpha(w\circ\psi) = \sum_{1\le|\beta|\le|\alpha|} c_{\alpha\beta}\cdot\big((\partial^\beta w)\circ\psi\big), \qquad |\alpha|\le k, \qquad\text{(chain rule),}$$
> > where each coefficient $c_{\alpha\beta}$ is a universal polynomial in the partial derivatives of the components of $\psi$ up to order $k$, hence smooth and bounded on the compact $\overline{V}$. Taking $L^2$ norms and using the $k=0$ change-of-variables bound on each $\partial^\beta w$,
> > $$\lVert\partial^\alpha(w\circ\psi)\rVert_{L^2} \le \sum_{1\le|\beta|\le k}\lVert c_{\alpha\beta}\rVert_{C^0}\,\lVert(\partial^\beta w)\circ\psi\rVert_{L^2} \le C''\!\!\sum_{|\beta|\le k}\lVert\partial^\beta w\rVert_{L^2} \qquad\text{(triangle inequality; }k=0\text{ bound applied to }\partial^\beta w\text{).}$$
> > Summing squares over $|\alpha|\le k$ and using the norm equivalence at both ends gives $\lVert w\circ\psi\rVert_k \le C\lVert w\rVert_k$.
> >
> > **Case $k < 0$: duality against the transposed map.** Write $k = -m$, $m > 0$. For smooth $w$ (supported in $V'$) and smooth test $\varphi$, change variables $y = \psi(x)$ in the pairing:
> > $$\langle w\circ\psi, \varphi\rangle_{T^n} = \int_{V} w(\psi(x))\,\overline{\varphi(x)}\,dx = \int_{V'} w(y)\,\overline{\varphi(\psi^{-1}(y))}\,|\det D\psi^{-1}(y)|\,dy = \langle w, T\varphi\rangle_{T^n},$$
> > $$\text{where}\qquad T\varphi := |\det D\psi^{-1}|\cdot(\varphi\circ\psi^{-1}) \qquad\text{(change of variables; the real Jacobian factor moves onto the conjugated slot).}$$
> > The operator $T$ is the composition of two operators already controlled: composition with the diffeomorphism $\psi^{-1} : V' \to V$ (bounded on $H_m(T^n)$ by the case $m \ge 0$ of *this* lemma, applied to $\psi^{-1}$), followed by multiplication by the smooth function $|\det D\psi^{-1}|$ (bounded on $H_m(T^n)$ by **Lemma 1**). Hence $\lVert T\varphi\rVert_m \le C_T\lVert\varphi\rVert_m$. Using the duality characterisation of the norm from part (iv) of [[Thm - Sobolev Norms on the Torus via Fourier Coefficients]],
> > $$\lVert w\circ\psi\rVert_{-m} = \sup_{\lVert\varphi\rVert_m\le 1}\tfrac{1}{(2\pi)^n}|\langle w\circ\psi,\varphi\rangle_{T^n}| = \sup_{\lVert\varphi\rVert_m\le 1}\tfrac{1}{(2\pi)^n}|\langle w, T\varphi\rangle_{T^n}| \le \sup_{\lVert\varphi\rVert_m\le 1}\lVert w\rVert_{-m}\,\lVert T\varphi\rVert_m \le C_T\,\lVert w\rVert_{-m}.$$
> > (The first inequality is the pairing bound from the torus definition; the last is $\lVert T\varphi\rVert_m \le C_T$ for $\lVert\varphi\rVert_m\le 1$.) The bound is uniform in smooth $w$, so composition extends by continuity to a bounded operator on the relevant subspace of $H_{-m}(T^n)$. $\blacksquare$

> [!note]- Lemma 3: The localisation and spreading operators are bounded, and spreading inverts localisation
> **Statement:** Set $\sigma := \sum_{j=1}^N \phi_j^2 \in C^\infty(M)$ and $\theta_i := \phi_i/\sigma$. Then: (a) $\sigma > 0$ everywhere and $\theta_i \in C^\infty(M)$ with $\operatorname{supp}\theta_i \subset U_i$ and $\sum_i \theta_i\phi_i \equiv 1$. Define, for $w \in C^\infty(T^n;\mathbb{C}^r)$, the *spreading* section $S_i w := \theta_i\cdot\Phi_i(w) \in \Gamma(E)$, where $\Phi_i(w)$ is the section of $E|_{U_i}$ whose frame components are $w\circ\kappa_i$ (extended by zero using $\theta_i$). Then (b) for every $k$, the localisation operators $R_i : (\Gamma(E),\lVert\cdot\rVert_{(k)}) \to H_k(T^n;\mathbb{C}^r)$, $R_i u = (\phi_i u)\circ\kappa_i^{-1}$, are bounded with $\lVert R_i u\rVert_{H_k} \le \lVert u\rVert_{(k)}$, and the spreading operators $S_i : H_k(T^n;\mathbb{C}^r) \to (\Gamma(E),\lVert\cdot\rVert_{(k)})$ are bounded; and (c) $\sum_{i=1}^N S_i R_i = \mathrm{id}$ on $\Gamma(E)$.
>
> **Hint:** Boundedness is Lemmas 1–2 applied to the transition maps and bump functions; the resolution of the identity is the identity $\sum_i\theta_i\phi_i = 1$.
>
> **Why needed:** Every clause of the theorem is phrased through $R_i$ and $S_i$; part (ii) is their boundedness, part (iv) uses $\sum S_i R_i = \mathrm{id}$.
>
> > [!note]- Full proof
> > **(a) The renormalisation is smooth and positive.** At each $x \in M$ we have $\sum_j \phi_j(x) = 1$, so some $\phi_j(x) > 0$, whence $\sigma(x) = \sum_j\phi_j(x)^2 > 0$; thus $\sigma$ is a strictly positive smooth function and $\theta_i = \phi_i/\sigma \in C^\infty(M)$. Since $\operatorname{supp}\theta_i = \operatorname{supp}\phi_i \subset U_i$, the section $S_i w = \theta_i\Phi_i(w)$ extends by zero to a global smooth section. Finally $\sum_i\theta_i\phi_i = \sum_i \phi_i^2/\sigma = \sigma/\sigma = 1$.
> >
> > **(b) Boundedness of $R_i$.** By definition $\lVert u\rVert_{(k)}^2 = \sum_{j}\lVert R_j u\rVert_{H_k}^2 \ge \lVert R_i u\rVert_{H_k}^2$, so $\lVert R_i u\rVert_{H_k} \le \lVert u\rVert_{(k)}$.
> >
> > **Boundedness of $S_i$.** We must bound $\lVert S_i w\rVert_{(k)}^2 = \sum_j\lVert R_j(S_i w)\rVert_{H_k}^2$. Fix $j$. The section $\phi_j\cdot S_i w = \phi_j\theta_i\Phi_i(w)$ is supported in $U_i\cap U_j$, and reading it in the $j$-th frame and transporting through $\kappa_j$ gives
> > $$R_j(S_i w) = \big(\phi_j\theta_i\,\Phi_i(w)\big)\circ\kappa_j^{-1} = M_{ij}\cdot\Big[(\rho_{ij})\cdot\big(w\circ(\kappa_i\circ\kappa_j^{-1})\big)\Big],$$
> > where $\rho_{ij} := (\phi_j\theta_i)\circ\kappa_j^{-1} \in C^\infty(T^n)$ is a smooth bump supported in $\kappa_j(U_i\cap U_j)$, $M_{ij} \in C^\infty(T^n;\mathrm{GL}_r)$ is the (smooth, matrix-valued) frame-change $e^{(i)} \mapsto e^{(j)}$ transported through $\kappa_j$, and $\kappa_i\circ\kappa_j^{-1}$ is the transition diffeomorphism between open subsets of $(-\pi,\pi)^n$. The bracketed factor is $w$ composed with the transition diffeomorphism, bounded on $H_k(T^n;\mathbb{C}^r)$ by **Lemma 2**; multiplication by the smooth bump $\rho_{ij}$ and by the smooth matrix $M_{ij}$ are bounded on $H_k(T^n;\mathbb{C}^r)$ by **Lemma 1**. Hence $\lVert R_j(S_i w)\rVert_{H_k} \le C_{ij}\lVert w\rVert_{H_k}$, and summing the finitely many squares,
> > $$\lVert S_i w\rVert_{(k)}^2 = \sum_{j=1}^N\lVert R_j(S_i w)\rVert_{H_k}^2 \le \Big(\sum_{j=1}^N C_{ij}^2\Big)\lVert w\rVert_{H_k}^2 \qquad\text{(finiteness of the atlas).}$$
> >
> > **(c) Resolution of the identity.** For $u \in \Gamma(E)$, by construction $\Phi_i(R_i u) = \Phi_i\big((\phi_i u)\circ\kappa_i^{-1}\big) = \phi_i u$ (transporting through $\kappa_i$ and back is the identity on $U_i$), so $S_i R_i u = \theta_i\Phi_i(R_i u) = \theta_i\phi_i u$. Summing and using (a),
> > $$\sum_{i=1}^N S_i R_i u = \sum_{i=1}^N \theta_i\phi_i u = \Big(\sum_{i=1}^N\theta_i\phi_i\Big)u = u. \qquad \blacksquare$$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix a data package $\mathcal{D}$ as in the Notation, and let $R_i, S_i, \theta_i, \sigma$ be as in Lemma 3.
>
> **Step 0 — $\lVert\cdot\rVert_{(k)}$ is a Hilbert norm on $\Gamma(E)$.** The inner product $\langle u,v\rangle_{(k)} := \sum_{i=1}^N \langle R_i u, R_i v\rangle_{H_k}$ is a finite sum of the (Hilbert) torus inner products, hence a genuine inner product, and $\lVert u\rVert_{(k)}^2 = \langle u,u\rangle_{(k)}$. It is positive definite: if $\lVert u\rVert_{(k)} = 0$ then $R_i u = 0$, i.e. $\phi_i u = 0$, for every $i$, so $u = \sum_i \phi_i u = 0$ (partition of unity). Thus $(\Gamma(E),\lVert\cdot\rVert_{(k)})$ is a pre-Hilbert space and its completion $H_k(M;E)$ is a Hilbert space in which $\Gamma(E)$ is dense *by construction of the completion*; this is the first assertion of part (iii).
>
> **Step 1 — part (i): agreement with the connection norm for $k \ge 0$.** Fix an integer $k \ge 0$. We prove the two inequalities.
>
> *Upper bound $\lVert u\rVert_{(k)} \le C_k\lVert u\rVert_{W^{k,2}}$.* Fix $i$. By part (i) of [[Thm - Sobolev Norms on the Torus via Fourier Coefficients]], $\lVert R_i u\rVert_{H_k} \le C\,\big(\sum_{|\alpha|\le k}\lVert\partial^\alpha(R_i u)\rVert_{L^2(T^n)}^2\big)^{1/2}$. In the chart $\kappa_i$ with the frame $e^{(i)}$, the flat coordinate derivatives $\partial^\alpha$ of the transported components are, by the chain rule and the fact that the connection $\nabla^E$ differs from the flat coordinate differentiation by the smooth zero-order Christoffel term $\Gamma^{(i)} \in C^\infty(U_i;\operatorname{End}(\mathbb{R}^r)\otimes T^*U_i)$ of the frame, expressible as
> $$\partial^\alpha(R_i u) = \sum_{|\beta|\le|\alpha|} B^{(i)}_{\alpha\beta}\cdot\big((\nabla^\beta(\phi_i u))\circ\kappa_i^{-1}\big) \qquad\text{(chain rule; }\nabla^E = d + \Gamma^{(i)}\text{ in the frame),}$$
> where $\nabla^\beta$ denotes the $|\beta|$-th iterated covariant derivative and the $B^{(i)}_{\alpha\beta}$ are smooth and bounded on the compact $\operatorname{supp}\phi_i$. By the Leibniz rule for $\nabla$, each $\nabla^\beta(\phi_i u)$ is a bounded combination of $\nabla^\gamma u$, $|\gamma|\le|\beta|\le k$, with coefficients built from the bounded derivatives of $\phi_i$. Taking $L^2$ norms (the change of variables from $\kappa_i(U_i)$ to $U_i$ contributes the bounded volume density) and summing,
> $$\lVert R_i u\rVert_{H_k} \le C\sum_{|\gamma|\le k}\lVert\nabla^\gamma u\rVert_{L^2(M)} \le C'\,\lVert u\rVert_{W^{k,2}} \qquad\text{(Leibniz rule; boundedness of }\phi_i, B^{(i)}, \text{ and the density on the compact chart).}$$
> Squaring and summing over the finitely many $i$ gives $\lVert u\rVert_{(k)} \le C_k\lVert u\rVert_{W^{k,2}}$.
>
> *Lower bound $c_k\lVert u\rVert_{W^{k,2}} \le \lVert u\rVert_{(k)}$.* Since $\sum_i\phi_i = 1$ we have $\nabla^\gamma u = \sum_i \nabla^\gamma(\phi_i u)$ for every $|\gamma|\le k$. Fix $i$ and $\gamma$. On $U_i$, expressing $\nabla$ through $d$ in the frame as above and inverting the previous relation, $\nabla^\gamma(\phi_i u)$ is a bounded combination of the flat derivatives $\partial^\alpha(R_i u)$, $|\alpha|\le|\gamma|\le k$, with smooth bounded coefficients supported in $\operatorname{supp}\phi_i$; taking $L^2$ norms and reversing the change of variables,
> $$\lVert\nabla^\gamma(\phi_i u)\rVert_{L^2(M)} \le C\sum_{|\alpha|\le k}\lVert\partial^\alpha(R_i u)\rVert_{L^2(T^n)} \le C'\,\lVert R_i u\rVert_{H_k} \qquad\text{(chain rule; part (i) of the torus theorem).}$$
> Hence, by the triangle inequality over the finite atlas, $\lVert\nabla^\gamma u\rVert_{L^2} \le \sum_i\lVert\nabla^\gamma(\phi_i u)\rVert_{L^2} \le C\sum_i\lVert R_i u\rVert_{H_k} \le C\sqrt{N}\,\lVert u\rVert_{(k)}$ (Cauchy–Schwarz on the finite sum). Squaring, summing over $|\gamma|\le k$, gives $\lVert u\rVert_{W^{k,2}} \le c_k^{-1}\lVert u\rVert_{(k)}$. This proves part (i), and with it $H_k(M;E) = W^{k,2}(M;E)$ with equivalent norms for $k \ge 0$, part of (ii).
>
> **Step 2 — part (ii): independence of the data.** Let $\mathcal{D}, \mathcal{D}'$ be two data packages with operators $R_i, S_i$ and $R_j', S_j'$. For $u \in \Gamma(E)$, using $\sum_i S_i R_i = \mathrm{id}$ (Lemma 3(c)) for the unprimed data,
> $$R_j' u = R_j'\Big(\sum_{i=1}^N S_i R_i u\Big) = \sum_{i=1}^N (R_j' S_i)(R_i u) \qquad\text{(linearity of }R_j'\text{).}$$
> Each composite $R_j' S_i : H_k(T^n;\mathbb{C}^r) \to H_k(T^n;\mathbb{C}^r)$ is, exactly as in the proof of Lemma 3(b) but with the transition $\kappa_i \circ (\kappa_j')^{-1}$, the frame-change matrix, and the bump $(\phi_j'\theta_i)\circ(\kappa_j')^{-1}$, a composition of a diffeomorphism-composition (**Lemma 2**) and smooth multiplications (**Lemma 1**), hence bounded: $\lVert R_j' S_i w\rVert_{H_k} \le C_{ij}\lVert w\rVert_{H_k}$. Therefore
> $$\lVert R_j' u\rVert_{H_k} \le \sum_{i=1}^N C_{ij}\,\lVert R_i u\rVert_{H_k} \le \Big(\sum_i C_{ij}^2\Big)^{1/2}\lVert u\rVert_{(k)} \qquad\text{(triangle inequality, then Cauchy–Schwarz on the finite sum),}$$
> and squaring and summing over $j$ gives $\lVert u\rVert'_{(k)} \le C\lVert u\rVert_{(k)}$. Exchanging the roles of $\mathcal{D}$ and $\mathcal{D}'$ gives the reverse inequality. Thus the two norms are equivalent, the completion $H_k(M;E)$ is independent of the data as a topological vector space, and by Step 0 it is Hilbertable. This completes part (ii).
>
> **Step 3 — part (iii): density and the descending inclusion.** Density of $\Gamma(E)$ was noted in Step 0. For the inclusion, let $k \ge m$ be integers. By part (ii) of [[Thm - Sobolev Norms on the Torus via Fourier Coefficients]] — for $k \ge m$ one has $\lVert w\rVert_m \le \lVert w\rVert_k$ on the torus, because $(1+|\xi|^2)^m \le (1+|\xi|^2)^k$ termwise — we have $\lVert R_i u\rVert_{H_m} \le \lVert R_i u\rVert_{H_k}$ for each $i$. Summing the squares over the finite atlas,
> $$\lVert u\rVert_{(m)}^2 = \sum_i\lVert R_i u\rVert_{H_m}^2 \le \sum_i\lVert R_i u\rVert_{H_k}^2 = \lVert u\rVert_{(k)}^2 \qquad\text{(termwise monotonicity of the torus weights).}$$
> Hence the identity on $\Gamma(E)$ is bounded from $\lVert\cdot\rVert_{(k)}$ to $\lVert\cdot\rVert_{(m)}$ and extends to a continuous linear map $H_k(M;E) \to H_m(M;E)$. It is injective: if $u_j \to u$ in $H_k$ and $u_j \to 0$ in $H_m$, then choosing a diagonal subsequence and using that both limits agree with the common limit on the dense smooth sections forces $u = 0$ (a Cauchy sequence of smooth sections that converges to $0$ in the weaker norm $\lVert\cdot\rVert_{(m)}$ has all its localisations $R_i u_j$ converging to $0$ in $H_m(T^n)$, and since $H_k(T^n) \hookrightarrow H_m(T^n)$ is injective on the torus, the $H_k$-limit of $R_i u_j$ is also $0$; summing over $i$ gives $u = 0$ in $H_k$). This proves part (iii).
>
> **Step 4 — part (v): bounded multipliers and bundle maps.** Let $\Psi : E \to F$ be a smooth bundle map, i.e. a smooth section of $\operatorname{Hom}(E,F)$; take a common finite atlas trivialising both $E$ and $F$, with partition of unity $(\phi_i)$ and localisations $R_i^E, R_i^F$. For $u \in \Gamma(E)$, in the $i$-th chart $\Psi u$ is read as multiplication of the components of $u$ by the smooth matrix-valued function $\Psi_i := \Psi$ expressed in the frames, so
> $$R_i^F(\Psi u) = (\phi_i\,\Psi u)\circ\kappa_i^{-1} = \widetilde\Psi_i \cdot R_i^E u, \qquad \widetilde\Psi_i := \Psi_i\circ\kappa_i^{-1} \in C^\infty(T^n;\operatorname{Hom}(\mathbb{R}^r,\mathbb{R}^{r'})),$$
> because $\phi_i$ commutes with the fibrewise map $\Psi$. By **Lemma 1** (matrix version) multiplication by the smooth matrix $\widetilde\Psi_i$ is bounded on $H_k(T^n;\mathbb{C}^r)$, so $\lVert R_i^F(\Psi u)\rVert_{H_k} \le C_i\lVert R_i^E u\rVert_{H_k}$; squaring and summing over the finite atlas, $\lVert\Psi u\rVert_{(k)} \le C\lVert u\rVert_{(k)}$. Taking $F = E$ and $\Psi = f\cdot\mathrm{id}_E$ gives the multiplication-by-$f$ statement. By density (part (iii)) the operator extends boundedly to $H_k(M;E) \to H_k(M;F)$. This proves part (v).
>
> **Step 5 — part (iv): the perfect pairing.** Fix an integer $k$; write the two orders as $k$ and $-k$.
>
> *The pairing extends and is bounded.* For $u, v \in \Gamma(E)$ we first rewrite the $L^2$ pairing chartwise. Using $\sum_i\theta_i\phi_i = 1$ (Lemma 3(a)) and the pointwise identity $\langle\phi_i u, w\rangle_h = \langle u,\phi_i w\rangle_h$ (the real scalar $\phi_i$ is self-adjoint),
> $$(u,v)_{L^2} = \int_M \Big\langle\sum_i\theta_i\phi_i u,\ v\Big\rangle_h\mathrm{vol}_g = \sum_{i=1}^N \int_M \langle \phi_i u,\ \theta_i v\rangle_h\,\mathrm{vol}_g \qquad\text{(resolution of the identity; }\phi_i\text{ self-adjoint).}$$
> The $i$-th summand is supported in $U_i$; transporting through $\kappa_i$ and the frame, it becomes a torus pairing of $R_i u = (\phi_i u)\circ\kappa_i^{-1}$ against the transported section, weighted by the smooth positive volume density $J_i > 0$ and the smooth positive-definite fibre-metric matrix $h_i$ read in the frame:
> $$\int_M\langle\phi_i u,\theta_i v\rangle_h\,\mathrm{vol}_g = \int_{T^n}\big(R_i u\big)^{\!\top} h_i\,J_i\,\big((\theta_i v)\circ\kappa_i^{-1}\big)\,dx = \big\langle R_i u,\ G_i\big\rangle_{T^n}, \quad G_i := \tfrac{1}{(2\pi)^n}\,h_i J_i\,\big((\theta_i v)\circ\kappa_i^{-1}\big),$$
> where $G_i \in C^\infty(T^n;\mathbb{R}^r)$ (the matrix factors $h_i J_i$ are smooth and bounded, so $G_i$ is $(\theta_i v)\circ\kappa_i^{-1}$ multiplied by a smooth matrix, i.e. bounded in $H_{-k}(T^n;\mathbb{C}^r)$ by **Lemma 1**). Applying the torus pairing bound $|\langle R_i u, G_i\rangle_{T^n}| \le (2\pi)^n\lVert R_i u\rVert_{H_k}\lVert G_i\rVert_{H_{-k}}$ and then the boundedness $\lVert G_i\rVert_{H_{-k}} \le C\lVert(\theta_i v)\circ\kappa_i^{-1}\rVert_{H_{-k}} \le C'\lVert v\rVert_{(-k)}$ (the last step is the boundedness of $R_i^{\theta}v := (\theta_i v)\circ\kappa_i^{-1}$, which is $R_i S_i'$-type and bounded by Lemma 3(b) applied with the weight $\theta_i$),
> $$|(u,v)_{L^2}| \le \sum_{i=1}^N|\langle R_i u,G_i\rangle_{T^n}| \le C\sum_{i=1}^N\lVert R_i u\rVert_{H_k}\,\lVert v\rVert_{(-k)} \le C\sqrt{N}\,\lVert u\rVert_{(k)}\,\lVert v\rVert_{(-k)} \qquad\text{(Cauchy–Schwarz on the finite sum).}$$
> Thus the pairing is bounded for smooth sections and, by density (part (iii)) in both slots, extends to a continuous bilinear pairing $H_k(M;E)\times H_{-k}(M;E) \to \mathbb{R}$ with the stated bound. Call the induced map $\iota : H_{-k}(M;E) \to (H_k(M;E))^*$, $\iota(v) = (\,\cdot\,,v)$.
>
> *$\iota$ is injective.* If $\iota(v) = 0$, then $(u,v) = 0$ for all $u \in \Gamma(E)$. Localising, $\langle R_i u, G_i\rangle_{T^n} = 0$ for all smooth $u$ and each $i$ (choose $u$ supported in a single $U_i$); by the perfect pairing on the torus (part (iv) of [[Thm - Sobolev Norms on the Torus via Fourier Coefficients]], which gives $\lVert G_i\rVert_{H_{-k}} = \sup_{w}|\langle w,G_i\rangle_{T^n}|/((2\pi)^n\lVert w\rVert_k)$) we get $G_i = 0$, hence $(\theta_i v)\circ\kappa_i^{-1} = 0$, hence $\theta_i v = 0$ for all $i$, hence $v = \sum_i\theta_i\phi_i v = 0$. So $\iota$ is injective.
>
> *$\iota$ is surjective.* Let $\Lambda \in (H_k(M;E))^*$. For each $i$ define a functional on the torus space by spreading first: $\mu_i : H_k(T^n;\mathbb{C}^r) \to \mathbb{R}$, $\mu_i(w) := \Lambda(S_i w)$, which is bounded because $S_i$ is bounded (Lemma 3(b)) and $\Lambda$ is bounded. By the torus duality (part (iv) of the torus theorem, componentwise), there is a unique $g_i \in H_{-k}(T^n;\mathbb{C}^r)$ with
> $$\mu_i(w) = \langle w, g_i\rangle_{T^n} \qquad\text{for all } w \in H_k(T^n;\mathbb{C}^r), \qquad \lVert g_i\rVert_{H_{-k}} \le C\lVert\mu_i\rVert.$$
> Now reverse the transport: define $v_i \in H_{-k}(E|_{U_i})$ by requiring its transported representative to be $(v_i)\circ\kappa_i^{-1} = (2\pi)^n\,J_i^{-1}h_i^{-\top}g_i$ — a smooth-matrix multiple of $g_i$, hence in $H_{-k}$ by **Lemma 1** and pulled back by $\kappa_i$ via **Lemma 2** — and set $v := \sum_{i=1}^N \phi_i v_i \in H_{-k}(M;E)$ (each $\phi_i v_i$ is a bounded multiplier applied to a transported $H_{-k}$ element, by part (v)). By the very choice of $J_i^{-1}h_i^{-\top}$, the chartwise pairing computation of the boundedness step runs in reverse: for $u \in \Gamma(E)$,
> $$(u,v)_{L^2} = \sum_{i=1}^N(u,\phi_i v_i)_{L^2} = \sum_{i=1}^N(\phi_i u, v_i)_{L^2} = \sum_{i=1}^N\langle R_i u, g_i\rangle_{T^n} = \sum_{i=1}^N\mu_i(R_i u) = \sum_{i=1}^N\Lambda(S_i R_i u) = \Lambda\Big(\sum_i S_i R_i u\Big) = \Lambda(u),$$
> where the third equality is the chartwise transport (the factors $J_i, h_i$ cancel by construction), the fifth is $\mu_i = \Lambda\circ S_i$, and the last is $\sum_i S_i R_i = \mathrm{id}$ (Lemma 3(c)). Both $\iota(v)$ and $\Lambda$ are continuous and agree on the dense subspace $\Gamma(E)$, so $\iota(v) = \Lambda$ on all of $H_k(M;E)$. Hence $\iota$ is surjective. Being a bounded linear bijection between the Hilbertable — in particular Banach — spaces $H_{-k}(M;E)$ and $(H_k(M;E))^*$, $\iota$ is a topological isomorphism (its inverse is bounded because a bounded bijection of Banach spaces is open). This proves part (iv). The identification with the abstract dual is compatible with the case $k \ge 0$, where the $L^2$ pairing is the genuine integral pairing; thus the negative-order spaces $H_{-k}(M;E)$ are, by definition and by this identification, the duals of the positive-order spaces.
>
> **Step 6 — part (vi): interpolation.** Let $r < t < s$ be integers and $\varepsilon > 0$. By part (v) of [[Thm - Sobolev Norms on the Torus via Fourier Coefficients]] — for integers $r < t < s$ and every $\varepsilon > 0$ there is $C_\varepsilon$ with $\lVert w\rVert_t \le \varepsilon\lVert w\rVert_s + C_\varepsilon\lVert w\rVert_r$ on the torus (this follows from the pointwise weight inequality $(1+|\xi|^2)^t \le \varepsilon(1+|\xi|^2)^s + C_\varepsilon(1+|\xi|^2)^r$) — apply the estimate to each $R_i u$ and sum. Using $\lVert a+b\rVert_{\ell^2} \le \lVert a\rVert_{\ell^2}+\lVert b\rVert_{\ell^2}$ over the finite index $i$,
> $$\lVert u\rVert_{(t)} = \Big(\sum_i\lVert R_i u\rVert_{H_t}^2\Big)^{1/2} \le \Big(\sum_i\big(\varepsilon\lVert R_i u\rVert_{H_s}+C_\varepsilon\lVert R_i u\rVert_{H_r}\big)^2\Big)^{1/2} \le \varepsilon\lVert u\rVert_{(s)} + C_\varepsilon\lVert u\rVert_{(r)} \qquad\text{(torus interpolation; triangle inequality in }\ell^2\text{).}$$
> This proves part (vi).
>
> **Conclusion.** All six parts are established: the chart norm agrees with the connection norm for $k \ge 0$ (Step 1), is independent of the data and Hilbertable (Steps 0, 2), has dense smooth sections and continuous descending inclusions (Step 3), a perfect $L^2$ duality (Step 5), bounded smooth multipliers and bundle maps (Step 4), and the torus interpolation inequality (Step 6). Therefore $H_k(M;E)$ is a well-defined intrinsic Hilbertable Sobolev scale on the compact manifold, into which every torus estimate transports through the finite atlas. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Elliptic PDE on a closed surface.** On a closed Riemann surface $\Sigma$ with a metric, consider the scalar equation $\Delta u = f$ for the Laplace–Beltrami operator. To even pose the equation weakly one completes $C^\infty(\Sigma)$ in the $H_1$ norm, and this theorem certifies that the completion is independent of the coordinate charts one uses to write $\Delta$ locally; the exercise is to show that the weak formulation $(\nabla u,\nabla\varphi)_{L^2} = -(f,\varphi)_{L^2}$ for all $\varphi \in H_1$ is well posed precisely because of the perfect pairing $H_1 \times H_{-1} \to \mathbb{R}$ of part (iv). The application is non-obvious because the equation never mentions charts, yet its solvability rests on the chart-independence proved here.

**Bootstrapping the regularity of a gauge field.** Given a connection $A$ on a bundle over a closed four-manifold that is known only to be $H_1$ and to satisfy an elliptic equation weakly, one improves its regularity one Sobolev order at a time. Each improvement step multiplies $A$ by cutoffs and transition data and reads it in charts; part (v) (bounded multipliers) and part (iii) (the descending scale) are exactly what make each step bounded and the limit smooth by part (iii)'s corollary $\bigcap_k H_k = C^\infty$. The exercise is to identify, in a single bootstrapping step, every place where "multiply by a smooth cutoff" or "compare two charts" is invoked and to certify boundedness by citing this page.

**Fredholm theory of an abstract elliptic operator.** For an [[Def - Elliptic Differential Operator and Principal Symbol|elliptic operator]] $L$ of order $\ell$ one studies $L : H_{k+\ell}(M;E) \to H_k(M;F)$ together with its adjoint on the dual spaces. The exercise is to show, using only parts (iii) and (iv), that the formal adjoint $L^*$ acting on smooth sections extends to the negative-order spaces and that the pairing identity $(Lu,\phi) = (u,L^*\phi)$ persists on the completions; the non-obvious point is that this makes sense at all for negative $k$, and it does only because $H_{-k}$ is the dual of $H_k$ by this theorem.

---

# Bridges

- **From the torus to every later compactness statement.** The [[Thm - Rellich Compactness Theorem|Rellich theorem]] on $M$ is obtained by writing the inclusion $H_k(M;E)\hookrightarrow H_m(M;E)$ as $\sum_i (\text{extension by zero})\circ(\text{torus inclusion})\circ R_i$ with the operators of this page; each factor is bounded here, and the middle factor is compact on the torus, so the whole is compact by the ideal property of compact operators. The bridge is the chart decomposition: it turns a global compactness question into finitely many torus questions.

- **From the perfect pairing to elliptic adjoints.** Part (iv) is what gives an elliptic operator a genuine adjoint on the negative-order spaces. Writing $L : H_{k+\ell}(M;E)\to H_k(M;F)$, its transpose under the pairings of this page is the extension of the formal adjoint $L^*$, and the Fredholm alternative for $L$ is stated through $\operatorname{coker} L \cong \ker L^*$ using precisely the identification $H_{-k}(M;F)\cong (H_k(M;F))^*$ proved here.

- **From bounded bundle maps to the nonlinear gauge theory.** The Seiberg–Witten and Yang–Mills equations are built from fibrewise-algebraic operations — Clifford multiplication, the quadratic term $\psi\otimes\psi^*$, the curvature nonlinearity. Part (v) certifies that the linear pieces of these operations are bounded on every $H_k(M;E)$, and combined with the [[Thm - Sobolev Multiplication Theorem|multiplication theorem]] this is what lets one set up the equations as smooth maps between Sobolev completions of section spaces.

---

# Unlocked by This

> [!tip] Elliptic Estimates on Closed Manifolds *(from Global Analysis)*
> Once $H_k(M;E)$ is intrinsic and self-dual, the local elliptic estimate on the torus patches to the global estimate $\lVert u\rVert_{(k+\ell)} \le C(\lVert Lu\rVert_{(k)} + \lVert u\rVert_{(k)})$ for an elliptic operator $L$ of order $\ell$, by the same $\sum_i R_i$ decomposition used throughout this page. See **Thm - Elliptic Regularity and the Elliptic Estimate**.

> [!tip] The Configuration Space of Gauge Theory *(from Gauge Theory)*
> The space of connections modulo gauge, and the space of pairs (connection, spinor), are modelled on the Sobolev completions built here; the group of $H_{k}$ gauge transformations acts smoothly because it is a Banach Lie group built from the Sobolev algebra, whose boundedness properties trace back to parts (v) and to the multiplication theorem. See **Def - Seiberg-Witten Moduli Space**.
