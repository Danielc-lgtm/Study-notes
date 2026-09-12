---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension"
  - "Def - Set of Measure Zero on a Manifold"
  - "Def - Regular and Critical Points"
  - "Def - Smooth Map between Manifolds"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\gamma\colon\mathbb{R}\to\mathbb{R}^2$ be a **smooth** map. Prove:
$$\text{the image }\gamma(\mathbb{R})\subseteq\mathbb{R}^2\text{ has Lebesgue measure zero, and its interior is empty.}$$

In words: a single smooth curve can never fill up any two-dimensional region, however wildly it wanders. The map $\gamma$ is not assumed injective, not assumed an immersion, not assumed to have bounded speed; it is only required to be $C^\infty$. The curve may be dense in $\mathbb{R}^2$ (a line of irrational slope wound onto a torus and then lifted has dense image), yet its image still occupies zero area.

Then explain, in one paragraph, why the hypothesis of smoothness cannot be dropped: exhibit the contrast with **Peano's continuous space-filling curve**, a *continuous* surjection $[0,1]\to[0,1]^2$ whose image is the entire filled unit square, of area $1$.

This is the smallest instance of the general fact that a smooth map cannot raise dimension — the fact that, one dimension up, tells us that the critical values of a Yang–Mills or Seiberg–Witten section are negligible and that generic sections miss thin sets. Here $m=1<n=2$; the same argument gives the general statement for $m<n$.

**Recall.** The objects in play are a smooth map between manifolds, the critical points and critical values of such a map, the notion of a measure-zero subset of a manifold, and the one case of Sard's theorem the argument needs.

![[Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension#Statement]]

The clause we use is part (a): **if $m<n$ then the whole image $f(M)$ has measure zero and empty interior.** We restate it at the point of use.

![[Def - Set of Measure Zero on a Manifold#The Definition]]

For a subset of $\mathbb{R}^n$ this specialises to the familiar Euclidean notion: $A\subseteq\mathbb{R}^n$ has **Lebesgue measure zero** if for every $\delta>0$ there is a countable family of open cubes $\{Q_k\}_{k\in\mathbb{N}}$ with $A\subseteq\bigcup_k Q_k$ and $\sum_k\operatorname{vol}(Q_k)<\delta$.

![[Def - Regular and Critical Points#The Definition]]

A point $t$ in the domain of a smooth map $f\colon M^m\to N^n$ is a **critical point** if the differential $d f_t\colon T_tM\to T_{f(t)}N$ fails to be surjective; the image $f(t)$ of a critical point is a **critical value**. A point of $N$ that is not a critical value is a **regular value**. When $m<n$ the linear map $d f_t$ maps an $m$-dimensional space into an $n$-dimensional one, so its image has dimension at most $m<n$ and it can never be surjective — hence *every* point of the domain is critical, a fact the solution turns on.

---

# Convergent Strategy

**Problem class.** This is a *negligibility* problem: we are handed a set defined as the image of a map and must show it is small in the measure-theoretic sense. The universal move for "the image of a smooth map is small" is to recognise the image as a set of critical values and invoke [[Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension|Sard's theorem]]. The problem is deliberately the lowest-dimensional case so that the recognition step is transparent: because the source dimension is strictly below the target dimension, there is no work to do in locating the critical set — it is everything.

**Assumption pattern.** The single hypothesis that carries the whole argument is the strict inequality $m=1<2=n$ together with smoothness. Strictness is what forces every differential $d\gamma_t$ to be non-surjective: a linear map $\mathbb{R}\to\mathbb{R}^2$ has rank at most $1$, so its image is a proper subspace and it misses points. Smoothness (in fact $C^1$ would suffice) is what licenses Sard; drop it and Peano's curve is a counterexample. The recognisable trigger is "*image of a map from a lower-dimensional space*"; the reaction is "*that image is a set of critical values, hence measure zero by Sard*."

**Theorem routing.** The route is short and rigid. First, use the dimension count to prove every $t\in\mathbb{R}$ is a critical point, so $\gamma(\mathbb{R})$ equals the set of critical values of $\gamma$. Second, apply part (a) of [[Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension|Sard's theorem]] with $m=1$, $n=2$, $M=\mathbb{R}$, $N=\mathbb{R}^2$: the image of a smooth map from a $1$-manifold to a $2$-manifold has measure zero. Third, deduce empty interior from measure zero by the elementary fact that a non-empty open subset of $\mathbb{R}^2$ contains a ball of positive area and therefore cannot be null.

**Key decision point.** The one genuinely conceptual step is realising that "measure zero" and "smooth" are inseparable here, and that continuity alone gives nothing. A continuous curve *can* be a bijection-like surjection onto a square; the failure of Sard for merely continuous maps is not a technicality but the whole content of the Peano phenomenon. The decision, then, is to identify precisely which regularity is being spent — $C^1$, through the local Lipschitz estimate that underlies Sard — and to make the Peano contrast the explicit witness that it is spent, not free.

---

# Legal Operations Used

The topic page for §3.5 is assembled after these subpages; until then the operations are named descriptively, and the orchestrator will reconcile the numbering.

1. **Read an image as a set of critical values via a dimension count.** When a set is presented as $f(M)$ for a smooth $f\colon M^m\to N^n$ with $m<n$, observe that every differential has rank $\le m<n$, so every domain point is critical and $f(M)$ *is* the critical-value set. This is the operation that turns a raw image into an object Sard can act on.

2. **Apply the low-dimensional Sard theorem to conclude measure zero.** Invoke part (a) of [[Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension|Sard's theorem]]: for $m<n$ the image of a smooth map has measure zero in the target. The hypotheses to check are only smoothness and $m<n$, both immediate here.

3. **Pass from measure zero to empty interior.** Use the elementary Euclidean fact that a non-empty open set contains a cube of positive volume, so a set of measure zero can contain no non-empty open set; its interior is therefore empty.

4. **Certify the failure of a claim by a boundary counterexample.** To show that a hypothesis is load-bearing, produce an object satisfying the weaker hypothesis but violating the conclusion — here Peano's continuous surjection $[0,1]\to[0,1]^2$, which fills a set of area $1$.

---

# Hints

> [!note]- Hint 1
> You are asked to show that an *image* is small. The one theorem in this section that says "the image of a smooth map is small" is Sard's theorem, in the version for $m\le n$. What does Sard say about the *critical* values, and how large is the critical set when the source has dimension strictly below the target?

> [!note]- Hint 2
> Fix $t\in\mathbb{R}$ and look at the differential $d\gamma_t\colon\mathbb{R}\to\mathbb{R}^2$. It is a linear map from a $1$-dimensional space to a $2$-dimensional one. Can it possibly be surjective? If not, what does that make $t$, and what does that make $\gamma(t)$?

> [!note]- Hint 3
> Since every $t$ is a critical point, the set of critical values is the entire image $\gamma(\mathbb{R})$. Now apply part (a) of Sard's theorem with $m=1<n=2$: the image has measure zero. For the interior, ask what the area of a non-empty open set must be.

> [!note]- Hint 4
> Empty interior from measure zero: if $\gamma(\mathbb{R})$ had an interior point $p$, it would contain an open ball $B(p,r)$, whose Lebesgue measure is $\pi r^2>0$. A subset of a measure-zero set has measure zero, so $\pi r^2=0$ — impossible. For the Peano contrast, remember that Peano's map is only continuous, so Sard does not apply; the local Lipschitz estimate that powers Sard needs a derivative bound, which a merely continuous map does not supply.

---

# Solution

The proof is three moves long. Because the source dimension $1$ is strictly less than the target dimension $2$, the differential of $\gamma$ is nowhere surjective, so every point of $\mathbb{R}$ is a critical point and the image $\gamma(\mathbb{R})$ is exactly the set of critical values. Sard's theorem then says this set has measure zero, and a measure-zero set in $\mathbb{R}^2$ cannot contain an open ball, so its interior is empty. The final paragraph records why continuity alone would not do.

**Step 1: Every point of the domain is critical, so $\gamma(\mathbb{R})$ is the set of critical values.**

For each $t\in\mathbb{R}$ the differential $d\gamma_t\colon T_t\mathbb{R}\to T_{\gamma(t)}\mathbb{R}^2$ has rank at most $1<2$, hence is not surjective; so $t$ is a critical point and $\gamma(t)$ a critical value. Consequently the set of critical values equals $\gamma(\mathbb{R})$.

> [!note]- Derivation
> Fix $t\in\mathbb{R}$. The tangent space $T_t\mathbb{R}$ is one-dimensional and $T_{\gamma(t)}\mathbb{R}^2$ is two-dimensional, so the differential
> $$d\gamma_t\colon T_t\mathbb{R}\longrightarrow T_{\gamma(t)}\mathbb{R}^2$$
> is a linear map from a $1$-dimensional vector space to a $2$-dimensional one. Its image is a linear subspace of $T_{\gamma(t)}\mathbb{R}^2$ of dimension at most $\dim T_t\mathbb{R}=1$ (the rank of a linear map cannot exceed the dimension of its domain). A subspace of dimension at most $1$ is a proper subspace of the $2$-dimensional target, so
> $$\operatorname{im}(d\gamma_t)\subsetneq T_{\gamma(t)}\mathbb{R}^2\qquad\text{(rank}\le1<2\text{)},$$
> that is, $d\gamma_t$ is **not surjective**. By the definition of a [[Def - Regular and Critical Points|critical point]] — $t$ is critical exactly when $d\gamma_t$ fails to be surjective — every $t\in\mathbb{R}$ is a critical point of $\gamma$.
>
> Therefore the critical value set is
> $$\{\gamma(t):t\text{ a critical point}\}=\{\gamma(t):t\in\mathbb{R}\}=\gamma(\mathbb{R})\qquad\text{(every }t\text{ is critical, by the line above).}$$
> The raw image has been identified with a set of critical values, which is the object Sard's theorem controls.

**Step 2: The image has measure zero.**

Apply part (a) of Sard's theorem with $m=1$, $n=2$: the image of a smooth map from a $1$-manifold to a $2$-manifold has measure zero in the target.

> [!note]- Derivation
> We invoke the following, proved in full on its own page (we restate it at the point of use, as required):
>
> > **Theorem (Sard, source dimension $\le$ target dimension), part (a).** Let $f\colon M^m\to N^n$ be smooth with $m\le n$. Then the set of critical values of $f$ has measure zero in $N$; in particular, if $m<n$ then $f(M)$ has measure zero and empty interior.
>
> Here $M=\mathbb{R}$ is a smooth $1$-manifold, $N=\mathbb{R}^2$ is a smooth $2$-manifold, $\gamma$ is smooth by hypothesis, and $m=1<2=n$. All hypotheses of the theorem are met. By part (a) applied to $\gamma$,
> $$\gamma(\mathbb{R})\text{ has measure zero in }\mathbb{R}^2\qquad\text{(by [[Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension|Sard's theorem]], part (a), since }m=1<2=n\text{).}$$
> Equivalently, by Step 1 the critical-value set is all of $\gamma(\mathbb{R})$, and the first clause of the theorem — critical values have measure zero — gives the same conclusion. On $\mathbb{R}^2$ the manifold notion of [[Def - Set of Measure Zero on a Manifold|measure zero]] is exactly Lebesgue measure zero, since the single global chart is the identity: for every $\delta>0$ there are countably many open cubes $\{Q_k\}$ with $\gamma(\mathbb{R})\subseteq\bigcup_kQ_k$ and $\sum_k\operatorname{vol}(Q_k)<\delta$.

**Step 3: The interior is empty.**

A set of Lebesgue measure zero in $\mathbb{R}^2$ contains no non-empty open set, because a non-empty open set contains a ball of positive area. Hence $\gamma(\mathbb{R})$ has empty interior.

> [!note]- Derivation
> Suppose, for contradiction, that the interior of $\gamma(\mathbb{R})$ were non-empty; call the assumption **(⋆)**. Then there is a point $p\in\gamma(\mathbb{R})$ and a radius $r>0$ with the open ball
> $$B(p,r)=\{z\in\mathbb{R}^2:|z-p|<r\}\subseteq\gamma(\mathbb{R}).$$
> The ball $B(p,r)$ has strictly positive Lebesgue measure, $\operatorname{vol}(B(p,r))=\pi r^2>0$. But a subset of a measure-zero set has measure zero (monotonicity of outer measure: if $A\subseteq S$ and $S$ is covered by cubes of total volume $<\delta$, the same cubes cover $A$), and by Step 2 the set $\gamma(\mathbb{R})$ has measure zero; hence
> $$\pi r^2=\operatorname{vol}\big(B(p,r)\big)\le\operatorname{vol}\big(\gamma(\mathbb{R})\big)=0\qquad\text{(monotonicity of measure; Step 2).}$$
> This forces $\pi r^2=0$, contradicting $r>0$. The contradiction is between the positive area of the ball and the vanishing measure of the set that contains it; it refutes **(⋆)**. Therefore the interior of $\gamma(\mathbb{R})$ is empty.

> [!note]- Complete formal solution
> **Claim.** For every smooth map $\gamma\colon\mathbb{R}\to\mathbb{R}^2$, the image $\gamma(\mathbb{R})$ has Lebesgue measure zero and empty interior.
>
> *Proof.* We show, in order, that every domain point is critical, that the image is therefore null, and that a null set has empty interior.
>
> **Every point is critical.** Fix $t\in\mathbb{R}$. The differential $d\gamma_t\colon T_t\mathbb{R}\to T_{\gamma(t)}\mathbb{R}^2$ maps a $1$-dimensional space into a $2$-dimensional one, so $\operatorname{rank}(d\gamma_t)\le1<2$ and $d\gamma_t$ is not surjective. By the definition of a [[Def - Regular and Critical Points|critical point]], $t$ is critical; as $t$ was arbitrary, every point of $\mathbb{R}$ is critical, so the set of critical values of $\gamma$ is exactly $\gamma(\mathbb{R})$.
>
> **The image is null.** By [[Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension|Sard's theorem]] — for smooth $f\colon M^m\to N^n$ with $m\le n$ the critical values have measure zero, and if $m<n$ then $f(M)$ has measure zero — applied to the smooth map $\gamma$ with $m=1<2=n$, the image $\gamma(\mathbb{R})$ has measure zero in $\mathbb{R}^2$. Under the identity chart this is Lebesgue measure zero.
>
> **Empty interior.** If $\gamma(\mathbb{R})$ contained an interior point $p$, it would contain an open ball $B(p,r)$ with $r>0$, and then $\pi r^2=\operatorname{vol}(B(p,r))\le\operatorname{vol}(\gamma(\mathbb{R}))=0$ by monotonicity of Lebesgue measure, contradicting $r>0$. Hence $\gamma(\mathbb{R})$ has empty interior. $\blacksquare$
>
> **The general case.** The identical argument, verbatim with $m$ and $n$ in place of $1$ and $2$, shows that for any smooth $f\colon M^m\to N^n$ with $m<n$ the image $f(M)$ has measure zero and empty interior: the rank bound $\operatorname{rank}(df_t)\le m<n$ makes every point critical, and Sard finishes. This is precisely part (a) of the theorem, seen from the domain side.

> [!warning] Illegal but tempting: "continuity is enough"
> One might expect a curve to have negligible image just because it is one-dimensional, using only continuity. This is **false**. **Peano's space-filling curve** is a *continuous* surjection $P\colon[0,1]\to[0,1]^2$ (constructed as the uniform limit of the polygonal Hilbert-curve approximants; uniform convergence of continuous maps yields a continuous limit, and one checks the limit hits every point of the square). Its image is the entire filled unit square, of area $1$ and with non-empty interior. So the conclusion fails outright for continuous maps.
> The reason Sard does not apply is exactly the reason it is a theorem about *smooth* maps: its proof rests on a local Lipschitz estimate — on a compact cube $K$ in a chart, $|f(z)-f(w)|\le L\,|z-w|$ for some $L$ depending on $\sup_K|df|$ — which bounds how much a small cube can be stretched, and there is no such $L$ for a merely continuous map. The extra condition that *would* make the naive argument legal is $C^1$ regularity (a bounded derivative on compacta), which is all Sard needs and all we used. Peano's curve is nowhere differentiable in any usable sense, and that is why it escapes.

> [!note]- Independent check: the image is null without quoting Sard
> It is instructive to see the measure-zero conclusion directly, since the computation *is* the proof of Sard in this case and confirms Step 2 by hand. Cover $\mathbb{R}=\bigcup_{j\in\mathbb{Z}}[j,j+1]$. Fix one compact interval $I=[j,j+1]$. Since $\gamma$ is $C^1$ and $I$ is compact, $L:=\sup_{t\in I}|\gamma'(t)|<\infty$, and by the mean value inequality $|\gamma(t)-\gamma(t')|\le L\,|t-t'|$ for $t,t'\in I$. Partition $I$ into $N$ subintervals $I_1,\dots,I_N$ of length $1/N$. On each $I_i$ the image has diameter at most $L/N$, so it lies in a square $Q_i$ of side $L/N$, of area $(L/N)^2$. Then
> $$\gamma(I)\subseteq\bigcup_{i=1}^{N}Q_i,\qquad \sum_{i=1}^{N}\operatorname{vol}(Q_i)\le N\cdot\frac{L^2}{N^2}=\frac{L^2}{N}\xrightarrow[N\to\infty]{}0\qquad\text{(mean value estimate on each }I_i\text{).}$$
> Since the total covering area can be made smaller than any $\delta>0$, the set $\gamma(I)$ has measure zero. A countable union of measure-zero sets has measure zero, so $\gamma(\mathbb{R})=\bigcup_j\gamma([j,j+1])$ has measure zero — agreeing with Step 2. The estimate visibly uses the derivative bound $L$, which is exactly what continuity fails to provide.

---

# Key Takeaways

**"Image of a smooth map from lower dimension" is a trigger phrase, and the reaction is always Sard.** The reusable principle is that a smooth map can never increase dimension in the measure-theoretic sense: whenever a set is presented as $f(M)$ with $f$ smooth and $\dim M<\dim N$, its image is automatically negligible, because every point of the domain is critical and Sard's theorem drowns the critical values in a null set. The recognition is purely a dimension count — $\operatorname{rank}(df)\le\dim M<\dim N$ — and requires nothing about $f$ beyond smoothness. This is the diagnostic to carry away: do not try to understand the geometry of the image, count dimensions and quote Sard. The same reflex tells us that a smooth curve in a surface, a smooth surface in a $3$-manifold, or the boundary values of a smooth map on a lower-dimensional face all sweep out measure-zero, empty-interior sets — the ingredient that lets §3.5 speak of "generic" points avoiding thin obstructions and that, one dimension higher, underlies transversality and the definition of degree.

**Measure zero and empty interior are two faces of "thin", and the bridge between them is elementary and one-directional.** Measure zero is the stronger statement: it implies empty interior, because a non-empty open set contains a ball of positive area, and no positive-area set fits inside a null set. The converse fails — the fat Cantor set has empty interior yet positive measure — so one should always prove measure zero first and read off empty interior, never the reverse. The transferable diagnostic is that "cannot fill a region" splits into a measure claim (occupies zero area) and a topological claim (contains no open patch), and the measure claim is the one Sard delivers, with the topological claim following for free by the ball-of-positive-measure argument used in Step 3. Keeping the implication straight — measure zero $\Rightarrow$ empty interior, not the other way — prevents the common error of trying to certify negligibility from a purely topological hypothesis.

**Smoothness is not decorative: it is precisely the hypothesis that Sard spends, and Peano's curve is the receipt.** The single most important lesson is knowing *which* regularity a theorem consumes. Sard consumes a derivative bound, through the local Lipschitz estimate that lets a small domain cube map into a small target cube; strip that bound away and the conclusion collapses, as Peano's continuous surjection onto the square demonstrates in the starkest possible way. When reconstructing this proof after a gap, the anchor is the pair "$m<n$ makes every point critical" and "continuity is not enough — remember Peano." The broader pattern for spaced practice: whenever a theorem's conclusion feels like it should follow from a weaker hypothesis, look for the standard counterexample living at exactly that weaker level; its existence tells you precisely how much regularity the theorem is really using, and here it pins the cost of the result to $C^1$, no less and no more. This is the same accounting that later distinguishes topological from smooth four-manifolds, where a theorem true for smooth structures fails for merely topological ones.
