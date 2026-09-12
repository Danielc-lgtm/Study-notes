---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Rellich Compactness Theorem"
  - "Def - Sobolev Space of Sections"
  - "Def - Compact Operator"
  - "Def - Bump Function and Smooth Cutoff"
tags: [geometry, gauge-theory, sobolev-spaces, analysis]
---

# Problem Statement

Fix $n\ge1$ and work on $\mathbb R^n$ with its standard flat metric and Lebesgue measure. Let $\phi\in C_c^\infty(\mathbb R^n)$ be a fixed smooth bump function that is not identically zero and whose support is contained in the open ball $B_{1/2}(0)=\{x\in\mathbb R^n:|x|<\tfrac12\}$. Let $e_1=(1,0,\dots,0)\in\mathbb R^n$ be the first standard basis vector, and for each integer $j\ge0$ define the translate
$$u_j:\mathbb R^n\to\mathbb R,\qquad u_j(x):=\phi(x-je_1).$$

Prove the following three statements, and then answer the conceptual question.

1. **Uniform bound.** The sequence $(u_j)_{j\ge0}$ is bounded in $W^{1,2}(\mathbb R^n)$; in fact $\lVert u_j\rVert_{W^{1,2}}=\lVert\phi\rVert_{W^{1,2}}$ for every $j$.
2. **Exact separation.** For all integers $j\ne l$ the supports of $u_j$ and $u_l$ meet in a set of Lebesgue measure zero, and consequently
$$\lVert u_j-u_l\rVert_{L^2}=\sqrt2\,\lVert\phi\rVert_{L^2}\qquad(j\ne l).$$
3. **No convergent subsequence.** No subsequence of $(u_j)$ converges in $L^2(\mathbb R^n)$. Hence the inclusion $W^{1,2}(\mathbb R^n)\hookrightarrow L^2(\mathbb R^n)$ is **not** a [[Def - Compact Operator|compact operator]]: the Rellich compactness theorem is false on the non-compact domain $\mathbb R^n$.

**Conceptual question.** The proof of the [[Thm - Rellich Compactness Theorem|Rellich compactness theorem]] on a compact manifold reduces, chart by chart, to the torus $T^n$ and there approximates the inclusion $H_k(T^n)\hookrightarrow H_m(T^n)$ by finite-rank frequency truncations. Identify precisely the step of that proof that uses compactness of the base, and explain why the translate sequence $(u_j)$ is exactly the obstruction that step removes.

**Recall.**

The objects in play are the Sobolev space $W^{1,2}(\mathbb R^n)$ and its norm, a smooth compactly supported bump function, the notion of a compact operator, and the statement of the Rellich theorem whose hypotheses this exercise probes.

![[Def - Sobolev Space of Sections#The Definition]]

Concretely, on $\mathbb R^n$ the space $L^2(\mathbb R^n)$ is the completion of $C_c^\infty(\mathbb R^n)$ in the norm $\lVert u\rVert_{L^2}=\big(\int_{\mathbb R^n}|u|^2\,dx\big)^{1/2}$, a Hilbert space with inner product $\langle u,v\rangle_{L^2}=\int_{\mathbb R^n}uv\,dx$; and $W^{1,2}(\mathbb R^n)$ is the completion of $C_c^\infty(\mathbb R^n)$ in
$$\lVert u\rVert_{W^{1,2}}^2:=\lVert u\rVert_{L^2}^2+\sum_{i=1}^n\big\lVert\partial_i u\big\rVert_{L^2}^2=\int_{\mathbb R^n}|u|^2\,dx+\int_{\mathbb R^n}|\nabla u|^2\,dx,$$
where $\nabla u=(\partial_1u,\dots,\partial_nu)$ and $|\nabla u|^2=\sum_{i=1}^n|\partial_iu|^2$. Each $u_j=\phi(\cdot-je_1)$ lies in $C_c^\infty(\mathbb R^n)$, so it is a genuine element of $W^{1,2}(\mathbb R^n)$ with no completion subtlety.

![[Def - Compact Operator#The Definition]]

A bounded linear map $K:X\to Y$ between Banach spaces is **compact** if the image $K(B)$ of the unit ball $B=\{x:\lVert x\rVert_X\le1\}$ is relatively compact in $Y$; equivalently, every bounded sequence $(x_j)$ in $X$ has a subsequence $(x_{j_i})$ for which $(Kx_{j_i})$ converges in $Y$.

![[Thm - Rellich Compactness Theorem#Statement]]

The theorem's single standing hypothesis is that the base manifold is **compact**. This exercise shows the hypothesis cannot be dropped: on the non-compact domain $\mathbb R^n$ the conclusion fails outright.

---

# Convergent Strategy

**Problem class.** This is a *counterexample-construction* problem of the sharpest kind: we are handed a theorem — Rellich compactness — with one hypothesis (compactness of the base), and asked to certify that the hypothesis is essential by exhibiting a bounded sequence with no convergent subsequence once the hypothesis is removed. The deliverable is not a delicate estimate but a single explicit sequence together with a clean proof that it defeats compactness, followed by a diagnosis of *which line of the positive proof it breaks*.

**Assumption pattern.** The recognisable trigger is that compactness of an inclusion $X\hookrightarrow Y$ is *equivalent* to the statement "every bounded sequence has a $Y$-convergent subsequence", and the cheapest way to kill this is a sequence that is bounded in $X$ but **uniformly separated** in $Y$ — a sequence all of whose distinct pairs are the same fixed distance $\delta>0$ apart in $Y$. A uniformly separated sequence has no Cauchy subsequence, hence no convergent subsequence, so it certifies non-compactness immediately. On a non-compact domain the group of translations acts by isometries and offers such a sequence for free: translate one bump off to infinity in unit steps.

**Theorem routing.** The route is: (i) verify boundedness in $W^{1,2}$ using that translation $x\mapsto x-je_1$ is a *measure-preserving isometry of $\mathbb R^n$*, so it preserves every integral defining the norm; (ii) verify separation in $L^2$ using that the supports become disjoint (up to measure zero) once the bumps are far enough apart, which makes the cross term $\langle u_j,u_l\rangle_{L^2}$ vanish and turns $\lVert u_j-u_l\rVert_{L^2}^2$ into $\lVert u_j\rVert_{L^2}^2+\lVert u_l\rVert_{L^2}^2$ by the parallelogram-type expansion; (iii) conclude via the elementary fact that a sequence whose distinct terms are all a fixed positive distance apart has no Cauchy — hence no convergent — subsequence in the complete space $L^2$. Then read the positive proof of [[Thm - Rellich Compactness Theorem|Rellich]] backwards to locate the exact step this sequence sabotages.

**Key decision point.** Two decisions carry the argument. First, *choosing the support radius smaller than $\tfrac12$ rather than $1$*: bumps supported in $B_{1/2}(0)$ have, after integer translation along $e_1$, essentially disjoint supports for *every* pair $j\ne l$ (their support closures meet in at most a measure-zero set), which is what upgrades the separation identity from "eventually" to "for all $j\ne l$" and yields the clean constant $\sqrt2\,\lVert\phi\rVert_{L^2}$. Had we taken support in $B_1(0)$, adjacent bumps ($|j-l|=1$) would overlap and the cross term would not vanish. Second, *recognising that the obstruction is the escape of mass to infinity, not any loss of regularity*: the sequence is perfectly smooth and uniformly bounded in every $W^{k,2}$; what fails is that $\mathbb R^n$ has infinite volume and room for the mass to march away, and this is precisely the ingredient that the finite atlas (equivalently, the discreteness and finiteness of frequency shells on the torus) supplies in the positive proof.

---

# Legal Operations Used

This solution deploys the following operations; where the [[Gauge Theory IX — Sobolev Spaces, Elliptic Operators, and Elliptic Complexes|topic page]] numbers its Legal Operations, these are to be reconciled against that list.

1. **Certify non-compactness by a uniformly separated bounded sequence.** To show an inclusion $X\hookrightarrow Y$ is not compact, produce a sequence bounded in $X$ with $\lVert x_j-x_l\rVert_Y\ge\delta>0$ for all $j\ne l$; such a sequence has no $Y$-Cauchy subsequence, so the image of the unit ball is not relatively compact.

2. **Use translation as a measure-preserving isometry.** The map $\tau_a:u\mapsto u(\cdot-a)$ preserves $\int_{\mathbb R^n}|u|^2\,dx$ and each $\int_{\mathbb R^n}|\partial_iu|^2\,dx$ (change of variables with unit Jacobian, and $\partial_i(\tau_au)=\tau_a(\partial_iu)$), hence preserves the $L^2$ and $W^{1,2}$ norms.

3. **Kill a cross term by disjointness of supports.** If $\operatorname{supp}u\cap\operatorname{supp}v$ has measure zero then $\langle u,v\rangle_{L^2}=\int uv\,dx=0$, so $\lVert u-v\rVert_{L^2}^2=\lVert u\rVert_{L^2}^2+\lVert v\rVert_{L^2}^2$.

4. **Pass from "no Cauchy subsequence" to "no convergent subsequence" via completeness.** In the complete space $L^2(\mathbb R^n)$, every convergent sequence is Cauchy; a uniformly separated sequence has no Cauchy subsequence, hence none of its subsequences converges.

5. **Diagnose a proof by locating the step that fails.** Read the positive proof of Rellich and identify the exact use of compactness (finiteness of the frequency shell / finiteness of the atlas), then confirm the counterexample is the object that step is designed to exclude.

---

# Hints

> [!note]- Hint 1
> Compactness of an inclusion $X\hookrightarrow Y$ says every $X$-bounded sequence has a $Y$-convergent subsequence. To defeat it you do not need cleverness in the estimate; you need one bounded sequence whose distinct terms stay a fixed positive distance apart in $Y$. On $\mathbb R^n$, what natural family of isometries lets you make infinitely many disjoint copies of a single bump?

> [!note]- Hint 2
> Translation $x\mapsto x-je_1$ has Jacobian $1$ and commutes with each partial derivative, so it preserves $\int|u|^2$ and $\int|\nabla u|^2$. Deduce that $\lVert u_j\rVert_{W^{1,2}}=\lVert\phi\rVert_{W^{1,2}}$ for all $j$ — the sequence is not merely bounded, it has constant norm.

> [!note]- Hint 3
> Because $\operatorname{supp}\phi\subset B_{1/2}(0)$, the support of $u_j$ sits in $B_{1/2}(je_1)$. For $j\ne l$ the centres $je_1,le_1$ are at distance $|j-l|\ge1$, while the two balls have radii summing to $1$; so the supports meet in at most a single boundary point — a set of measure zero. What does that do to $\int u_ju_l\,dx$, and hence to $\lVert u_j-u_l\rVert_{L^2}^2$?

> [!note]- Hint 4
> With $\lVert u_j-u_l\rVert_{L^2}=\sqrt2\,\lVert\phi\rVert_{L^2}$ for all $j\ne l$ and $\lVert\phi\rVert_{L^2}>0$, any subsequence has all distinct terms exactly $\sqrt2\lVert\phi\rVert_{L^2}$ apart, so it cannot be Cauchy. Since $L^2$ is complete, non-Cauchy means non-convergent. For the conceptual question, ask where the positive proof uses that the frequency ball $\{|\xi|\le R\}\cap\mathbb Z^n$ is *finite* — and note that on $\mathbb R^n$ the frequencies form a continuum, so the corresponding truncation has infinite rank.

---

# Solution

The whole argument is the observation that on a non-compact domain the isometry group is large enough to spread a single bump into infinitely many disjoint, equinormed copies. Boundedness comes from translation invariance of the norm; separation comes from disjoint supports; the failure of compactness comes from the elementary fact that a uniformly separated sequence has no Cauchy subsequence. The diagnosis at the end pins the disappearance of compactness on the finiteness of the frequency shell in the torus proof — the imprint of compactness of the base.

**Step 1: The translates have constant $W^{1,2}$ norm, hence are bounded.**

Translation by $je_1$ is a measure-preserving isometry of $\mathbb R^n$ that commutes with differentiation, so it fixes each integral in the definition of the $W^{1,2}$ norm; therefore $\lVert u_j\rVert_{W^{1,2}}=\lVert\phi\rVert_{W^{1,2}}$ for all $j$.

> [!note]- Derivation
> Fix $j\ge0$ and write $u_j(x)=\phi(x-je_1)$. Two elementary facts about the translation $\tau_j:x\mapsto x-je_1$:
>
> - **It preserves the $L^2$ integral.** By the change of variables $y=x-je_1$, which is an affine bijection of $\mathbb R^n$ with Jacobian determinant $\det I=1$,
> $$\int_{\mathbb R^n}|u_j(x)|^2\,dx=\int_{\mathbb R^n}|\phi(x-je_1)|^2\,dx=\int_{\mathbb R^n}|\phi(y)|^2\,dy=\lVert\phi\rVert_{L^2}^2\qquad(\text{change of variables }y=x-je_1,\ dy=dx).$$
> - **It commutes with each partial derivative.** By the chain rule, for each $i\in\{1,\dots,n\}$,
> $$\partial_i u_j(x)=\partial_i\big[\phi(x-je_1)\big]=(\partial_i\phi)(x-je_1)\qquad(\text{chain rule; the inner map }x\mapsto x-je_1\text{ has derivative }I).$$
> Hence, by the same change of variables applied to $\partial_i\phi$,
> $$\int_{\mathbb R^n}|\partial_iu_j(x)|^2\,dx=\int_{\mathbb R^n}|(\partial_i\phi)(x-je_1)|^2\,dx=\int_{\mathbb R^n}|\partial_i\phi(y)|^2\,dy=\lVert\partial_i\phi\rVert_{L^2}^2\qquad(\text{change of variables }y=x-je_1).$$
>
> Summing over $i$ and adding the $L^2$ term,
> $$\lVert u_j\rVert_{W^{1,2}}^2=\lVert u_j\rVert_{L^2}^2+\sum_{i=1}^n\lVert\partial_iu_j\rVert_{L^2}^2=\lVert\phi\rVert_{L^2}^2+\sum_{i=1}^n\lVert\partial_i\phi\rVert_{L^2}^2=\lVert\phi\rVert_{W^{1,2}}^2\qquad(\text{by the two displayed identities}).$$
> Therefore $\lVert u_j\rVert_{W^{1,2}}=\lVert\phi\rVert_{W^{1,2}}$ for every $j\ge0$. In particular the sequence $(u_j)$ is bounded in $W^{1,2}(\mathbb R^n)$, with the uniform bound $\sup_j\lVert u_j\rVert_{W^{1,2}}=\lVert\phi\rVert_{W^{1,2}}<\infty$. This proves statement 1.

**Step 2: For $j\ne l$ the supports meet in measure zero, so the $L^2$ cross term vanishes.**

Because $\phi$ is supported in $B_{1/2}(0)$, the bumps $u_j$ live in disjoint balls up to boundary; the overlap has measure zero, killing $\langle u_j,u_l\rangle_{L^2}$.

> [!note]- Derivation
> Since $\operatorname{supp}\phi\subseteq B_{1/2}(0)$ and $u_j=\phi(\cdot-je_1)$, we have
> $$\operatorname{supp}u_j\subseteq B_{1/2}(je_1)=\{x\in\mathbb R^n:|x-je_1|<\tfrac12\}\qquad(\text{translating the support of }\phi\text{ by }je_1).$$
> Fix integers $j\ne l$. The centres $je_1$ and $le_1$ satisfy $|je_1-le_1|=|j-l|\,|e_1|=|j-l|\ge1$. If a point $x$ lay in both open balls, then by the triangle inequality
> $$|j-l|=|je_1-le_1|\le|je_1-x|+|x-le_1|<\tfrac12+\tfrac12=1\qquad(\text{triangle inequality; }x\in B_{1/2}(je_1)\cap B_{1/2}(le_1)),$$
> contradicting $|j-l|\ge1$. Hence the *open* balls $B_{1/2}(je_1)$ and $B_{1/2}(le_1)$ are disjoint, so
> $$\operatorname{supp}u_j\cap\operatorname{supp}u_l\subseteq B_{1/2}(je_1)\cap B_{1/2}(le_1)=\varnothing.$$
> (Even had we allowed the closed balls, their intersection when $|j-l|=1$ would be a single point, of Lebesgue measure zero, which is all the argument needs.) Consequently the product $u_j(x)u_l(x)$ vanishes for every $x$, and
> $$\langle u_j,u_l\rangle_{L^2}=\int_{\mathbb R^n}u_j(x)\,u_l(x)\,dx=0\qquad(\text{the integrand is identically }0\text{ off the empty overlap}).$$
> This is the vanishing cross term needed in Step 3.

**Step 3: The exact separation $\lVert u_j-u_l\rVert_{L^2}=\sqrt2\,\lVert\phi\rVert_{L^2}$.**

Expanding the squared $L^2$ norm and using the vanishing cross term of Step 2 together with the constant norm of Step 1 gives the separation identity.

> [!note]- Derivation
> Fix $j\ne l$. Since $L^2(\mathbb R^n)$ is an inner-product space, the squared norm of the difference expands as
> $$\lVert u_j-u_l\rVert_{L^2}^2=\langle u_j-u_l,\,u_j-u_l\rangle_{L^2}=\lVert u_j\rVert_{L^2}^2-2\langle u_j,u_l\rangle_{L^2}+\lVert u_l\rVert_{L^2}^2\qquad(\text{bilinearity and symmetry of }\langle\cdot,\cdot\rangle_{L^2}).$$
> By Step 2, $\langle u_j,u_l\rangle_{L^2}=0$; by Step 1 (its $L^2$ part), $\lVert u_j\rVert_{L^2}=\lVert u_l\rVert_{L^2}=\lVert\phi\rVert_{L^2}$. Substituting,
> $$\lVert u_j-u_l\rVert_{L^2}^2=\lVert\phi\rVert_{L^2}^2-0+\lVert\phi\rVert_{L^2}^2=2\,\lVert\phi\rVert_{L^2}^2\qquad(\text{by Step 2 and Step 1}).$$
> Taking the non-negative square root,
> $$\lVert u_j-u_l\rVert_{L^2}=\sqrt2\,\lVert\phi\rVert_{L^2}\qquad(j\ne l).$$
> Since $\phi$ is smooth and not identically zero, $\lVert\phi\rVert_{L^2}^2=\int|\phi|^2\,dx>0$ (a non-negative continuous integrand that is positive somewhere has positive integral), so the separation constant $\delta:=\sqrt2\,\lVert\phi\rVert_{L^2}$ is strictly positive. This proves statement 2.

**Step 4: No subsequence converges in $L^2$; Rellich fails on $\mathbb R^n$.**

A sequence all of whose distinct terms are the fixed distance $\delta>0$ apart has no Cauchy subsequence, and in the complete space $L^2$ this means no convergent subsequence; hence the bounded sequence $(u_j)$ witnesses the failure of compactness.

> [!note]- Derivation
> Let $(u_{j_i})_{i\ge0}$ be any subsequence, with $j_0<j_1<j_2<\cdots$ strictly increasing integers. For $i\ne i'$ the indices $j_i\ne j_{i'}$ are distinct, so by Step 3,
> $$\lVert u_{j_i}-u_{j_{i'}}\rVert_{L^2}=\sqrt2\,\lVert\phi\rVert_{L^2}=\delta>0\qquad(\text{Step 3 applied to the distinct pair }j_i\ne j_{i'}).$$
> A sequence is **Cauchy** only if for $\varepsilon=\delta/2>0$ there is $N$ with $\lVert u_{j_i}-u_{j_{i'}}\rVert_{L^2}<\delta/2$ for all $i,i'\ge N$; but every such distance equals $\delta$, and $\delta<\delta/2$ is false. Hence $(u_{j_i})$ is **not** Cauchy. Because $L^2(\mathbb R^n)$ is a [[Def - Cauchy Sequence and Complete Metric Space|complete metric space]] (it is defined as a completion), a convergent sequence is necessarily Cauchy; the contrapositive says a non-Cauchy sequence does not converge. Therefore no subsequence of $(u_j)$ converges in $L^2(\mathbb R^n)$.
>
> Now suppose, for contradiction, that the inclusion $\iota:W^{1,2}(\mathbb R^n)\hookrightarrow L^2(\mathbb R^n)$ were a [[Def - Compact Operator|compact operator]]. By Step 1 the sequence $(u_j)$ is bounded in $W^{1,2}(\mathbb R^n)$, so by the definition of compactness the sequence $(\iota u_j)=(u_j)$ would have a subsequence converging in $L^2(\mathbb R^n)$. This contradicts the previous paragraph. Therefore $\iota$ is not compact: **the Rellich compactness theorem fails on the non-compact domain $\mathbb R^n$.** This proves statement 3. $\blacksquare$

**Step 5: Which step of the torus proof uses compactness.**

The positive proof approximates the inclusion by finite-rank frequency truncations; that those truncations have *finite* rank is exactly the discreteness-and-finiteness of the frequency shell $\{|\xi|\le R\}$, and the reduction from a compact manifold to the torus uses a *finite* atlas — both are compactness. The translate sequence has bounded, non-concentrating frequency content but escaping spatial support, which is the phenomenon those finiteness steps exclude.

> [!note]- Diagnosis
> Recall the structure of the proof of the [[Thm - Rellich Compactness Theorem|Rellich compactness theorem]] on the torus $T^n=\mathbb R^n/2\pi\mathbb Z^n$. For $k>m$ one writes the inclusion $\iota:H_k(T^n)\hookrightarrow H_m(T^n)$ as the operator-norm limit of the finite-rank frequency truncations
> $$T_R u:=\sum_{\xi\in\mathbb Z^n,\ |\xi|\le R}\hat u(\xi)\,e^{i\langle\xi,x\rangle},\qquad\lVert\iota-T_R\rVert_{H_k\to H_m}\le(1+R^2)^{(m-k)/2}\xrightarrow[R\to\infty]{}0,$$
> and concludes that $\iota$ is compact because it is a norm-limit of finite-rank operators. **The load-bearing use of compactness is the word *finite* in "finite-rank".** Each $T_R$ has finite rank precisely because the frequency shell $\{\xi\in\mathbb Z^n:|\xi|\le R\}$ is a *finite* set: on a compact Riemannian manifold the Laplacian has discrete spectrum with finite-dimensional eigenspaces, and on the torus this is visible as the frequencies forming the *discrete* lattice $\mathbb Z^n$ with only finitely many points in any ball. Compactness enters a second time in the reduction from a general compact manifold to the torus: one covers the manifold by a *finite* atlas with a *finite* subordinate partition of unity, and the inclusion is a finite sum of bounded localisations composed with torus inclusions. Both "finite"s are the compactness hypothesis.
>
> On $\mathbb R^n$ neither finiteness survives. The Fourier transform is taken over the *continuous* frequency space $\mathbb R^n$, so the corresponding truncation $u\mapsto\int_{|\xi|\le R}\hat u(\xi)e^{i\langle\xi,x\rangle}\,d\xi$ has *infinite* rank — its range is the infinite-dimensional space of band-limited functions — and the norm-limit-of-finite-rank argument produces nothing. Correspondingly $\mathbb R^n$ admits no finite atlas. The translate sequence $(u_j)$ makes the failure concrete and shows *which* feature is missing: the sequence is uniformly bounded not only in $W^{1,2}$ but in every $W^{k,2}$, and its Fourier content does not concentrate at high frequency (translation only multiplies $\hat u_j(\xi)$ by the unimodular phase $e^{-ij\langle\xi,e_1\rangle}$, so $|\hat u_j|=|\hat\phi|$ is $j$-independent). What runs away is the *spatial support*: the mass $\lVert u_j\rVert_{L^2}^2=\lVert\phi\rVert_{L^2}^2$ sits in the ball $B_{1/2}(je_1)$ and marches off to spatial infinity. On a compact base the finite atlas confines all mass to a bounded region and forbids this escape; that confinement is exactly what the finite-rank truncation encodes on the Fourier side. In one sentence: **Rellich needs the frequency shell to be finite and the atlas to be finite, and both are the compactness of the base; the translates escape to spatial infinity precisely in the room that non-compactness provides.**

> [!warning] Illegal but tempting shortcut
> One is tempted to argue "$(u_j)$ converges to $0$ weakly in $L^2$ (indeed $\langle u_j,g\rangle_{L^2}\to0$ for every fixed $g\in L^2$, since the mass escapes any fixed compact set), and a weakly convergent sequence with no strong limit shows non-compactness." The *conclusion* is correct, but the parenthetical is a real theorem (that $u_j\rightharpoonup0$) requiring its own proof, and weak convergence to $0$ does not by itself contradict strong convergence of a subsequence unless one also knows the strong limit would have to be the weak limit $0$ while $\lVert u_j\rVert_{L^2}=\lVert\phi\rVert_{L^2}\not\to0$. That fuller argument is valid but strictly longer than the disjoint-support computation above, which needs no functional-analytic machinery beyond completeness. The direct route — uniform separation, no Cauchy subsequence — is both shorter and self-contained, so it is the one to use.

---

# Key Takeaways

**To prove an inclusion is not compact, exhibit a uniformly separated bounded sequence; the isometry group of the domain is the natural source of one.** The definition of a compact operator is "every bounded sequence has a convergent subsequence", and its cleanest negation is a bounded sequence whose distinct terms are all a fixed positive distance $\delta$ apart in the target. Such a sequence has no Cauchy subsequence, so — in a complete target — no convergent subsequence, and the operator fails to be compact. The recurring manufacturing recipe is to take one fixed element and move it by an infinite discrete family of *isometries of the domain that become "orthogonal" in the target*: on $\mathbb R^n$ these are the integer translations $\tau_{je_1}$, which preserve every Sobolev norm (Step 1) yet drive the supports apart until the $L^2$ inner products vanish (Step 2). The same template recurs whenever a symmetry group acts by isometries with wandering orbits — for instance dilations on scale-invariant spaces, or deck transformations on a non-compact cover — and is the standard way to see that Sobolev embeddings that *are* compact on compact manifolds degrade to merely continuous, non-compact embeddings on $\mathbb R^n$.

**Compactness of the base is not an incidental hypothesis of Rellich; it is the finiteness that the whole proof runs on.** It is worth internalising exactly where compactness is spent, because the same accounting governs every later application in this chapter. The positive proof spends compactness twice: once so that the frequency shell $\{|\xi|\le R\}\cap\mathbb Z^n$ is a *finite* set, making the truncations $T_R$ finite-rank and the inclusion a norm-limit of finite-rank operators; and once so that a general compact manifold is covered by a *finite* atlas, reducing to the torus by a finite sum of bounded pieces. Both finitenesses fail on $\mathbb R^n$, where frequencies form a continuum and no finite atlas exists. The diagnostic to carry away: when a theorem's proof approximates an operator by finite-rank pieces, *the compactness hypothesis is usually hiding in the word "finite"*, and removing it typically resurfaces as an escape of mass either to high frequency (loss of the finite shell) or to spatial infinity (loss of the finite atlas). Here the escape is spatial, which is why the counterexample is a translate rather than a highly oscillatory bump.

**The obstruction is escaping mass, not lost regularity — and recognising which failure mode is at work tells you how to repair the theorem.** The translate sequence is smooth and uniformly bounded in *every* $W^{k,2}(\mathbb R^n)$, so no amount of extra differentiability rescues compactness; the difficulty is purely that infinite-volume domains let a fixed lump of mass wander off to infinity while keeping its norm. This is exactly the diagnostic that motivates the standard repairs on $\mathbb R^n$: the Rellich–Kondrachov theorem is recovered by restricting to a *bounded* domain $\Omega$ (which reinstates finite volume and a compact closure), or by working in *weighted* Sobolev spaces whose weights penalise mass at infinity, or by imposing decay/tightness that prevents the escape. Each repair addresses the spatial-escape mode specifically. The companion exercise [[Ex - An Unbounded Function in W-1-2 of the Two-Torus]] isolates the *other* failure mode — the borderline $2k=n$ of the Sobolev embedding, where regularity, not compactness, is at stake even on a compact base — and reading the two together fixes in the mind the distinction between "the base is non-compact" and "the Sobolev index is critical" as two independent ways the clean theorems can break.
