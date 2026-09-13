---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Set of Measure Zero on a Manifold"
  - "Def - Regular and Critical Points"
  - "Def - Smooth Map between Manifolds"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ and $N$ are smooth manifolds in the sense fixed for this series — smooth ($C^\infty$), Hausdorff, and second countable — of [[Def - Dimension|dimensions]] $m = \dim M$ and $n = \dim N$, and $f\colon M \to N$ is a [[Def - Smooth Map between Manifolds|smooth map]]. At a point $p \in M$ the differential $d f_p\colon T_p M \to T_{f(p)} N$ is the induced linear map on [[Def - Tangent Space|tangent spaces]]. A point $p \in M$ is a [[Def - Regular and Critical Points|regular point]] of $f$ when $d f_p$ is surjective, and a **critical point** otherwise; a point $c \in N$ is a [[Def - Regular and Critical Points|regular value]] when every point of the preimage $f^{-1}(c) = \{p \in M : f(p) = c\}$ is a regular point (in particular when $f^{-1}(c) = \varnothing$), and a **critical value** otherwise. We write $\operatorname{Crit}(f) = \{p \in M : d f_p \text{ not surjective}\}$ for the set of critical points, so that the set of critical values is exactly the image $f(\operatorname{Crit}(f)) \subseteq N$.

A subset $A \subseteq \mathbb{R}^k$ has **Lebesgue measure zero** when for every $\delta > 0$ it admits a countable cover by open cubes whose total $k$-dimensional volume is less than $\delta$; a subset $A \subseteq N$ has [[Def - Set of Measure Zero on a Manifold|measure zero on the manifold]] when $\psi(A \cap V) \subseteq \mathbb{R}^n$ has Lebesgue measure zero for every smooth chart $(V, \psi)$ of $N$, a condition that need only be checked on the domains of a single atlas because it is diffeomorphism invariant. For a linear map $T$ we write $\lVert T \rVert$ for its operator norm, and for $h \in \mathbb{R}^k$ we write $\lvert h \rvert$ for the Euclidean norm; $\operatorname{vol}_k$ denotes $k$-dimensional Lebesgue volume. The full notation registry for this chapter lives on [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]].

> [!warning] Convention: this is the restricted Sard theorem
> This page proves Sard's theorem **only in the case $m \le n$** (source dimension not exceeding target dimension), which is the only case chapters I–VI of this series use, and the substance of the proof is genuinely elementary — the first-order Taylor estimate together with a cube count, with no measure-theoretic machinery beyond countable subadditivity of Lebesgue volume. **The full Sard theorem, which allows $m > n$ and controls the higher critical strata by an induction on the order of vanishing of the derivatives, is a different and much harder statement; it is proved in full in chapter X as a lemma feeding the Sard–Smale theorem, and it is not invoked anywhere before that chapter.** Nothing on this page depends on the general theorem.

---

# Statement

> **Theorem (Sard, the case $m \le n$).** Let $f\colon M^m \to N^n$ be a smooth map between smooth manifolds with $m \le n$. Then the set of critical values of $f$ — that is, $f(\operatorname{Crit}(f))$ — has measure zero in $N$. In particular:
> - **(a)** if $m < n$, then every point of $M$ is a critical point, and the image $f(M)$ has measure zero in $N$ and hence has empty interior;
> - **(b)** if $m = n$, then the set of regular values of $f$ is dense in $N$;
> - **(c)** if $M$ is compact and $c \in N$ is a regular value of $f$, then the preimage $f^{-1}(c)$ is a finite set.

---

# Motivation

The classification theorems that close this chapter — that every principal $SU(2)$-bundle over a manifold of dimension at most three is trivial, that a principal $U(1)$-bundle over a surface is determined by one integer, that a line bundle over a compact base is pulled back from projective space — all rest on the same manoeuvre: perturb a section a little so that it meets the zero section cleanly, and read off a finite, signed set of zeros. That manoeuvre is the transversality theorem of the next page, and transversality is powered by a single analytic fact, that the values a smooth map can hit "badly" are negligible. This is Sard's theorem. Degree theory needs the same fact — the degree is computed at a regular value, and one has to know regular values exist — and so does the hairy-ball theorem. Sard's theorem is the one piece of hard analysis standing under the soft topology of this chapter.

The vault's differential-geometry pages state Sard's theorem in full generality but leave it unproved, and a chapter that proves everything it uses cannot lean on that. The escape is that the general theorem is only needed here in the tractable range $m \le n$. When the source is no larger than the target there is no room for the derivative to drop rank in a way that hides critical values behind a curtain of higher-order flatness: for $m < n$ the image is already too thin to fill anything, and for $m = n$ a single first-order Taylor estimate on a cube does the whole job. We prove exactly that restricted statement, note explicitly that the general one belongs to chapter X, and thereby keep the classification arguments self-contained.

The statement has three faces worth separating. Face (a), for $m < n$, is the intuition that a curve cannot fill a plane and a surface cannot fill a solid: a lower-dimensional domain has a negligible image. Face (b), for $m = n$, is the useful existence statement — one can always find a value over which the map is a local diffeomorphism at every preimage point. Face (c) is the finiteness that makes counting possible: over a good value of a map from a compact source of equal dimension, the fibre is a finite set, which is what lets the degree be an integer and lets a generic section have finitely many zeros.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is mild — any smooth $f$ with $m \le n$ — so the useful question is which problems secretly present such a map.

The first disguised source is **a section of a vector bundle presented as a map into its total space, or as a map into a fibre**. When one perturbs a section $s$ of a rank-$r$ bundle $E \to M$ by a finite-parameter family $s_a = \sum_i a_i s_i$, the assignment $a \mapsto s_a(x)$ and the parametrised zero-locus map are smooth maps whose critical values one must avoid; the bridge $B \Rightarrow A$ is that the parameter map from the zero manifold to the parameter space $\mathbb{R}^N$ is a smooth map of manifolds, and one only ever needs it where the source dimension is at most $N$. This is precisely the input to [[Thm - Generic Sections are Transverse to the Zero Section|the generic-sections theorem]]. *Example problem:* show that a rank-$r$ bundle over a compact $m$-manifold with $r > m$ has a nowhere-vanishing section, by making the parametric section map miss the (measure-zero) bad parameters.

The second disguised source is **a smoothly parametrised family of maps whose "good" members are wanted**, for instance a family $f_t\colon M \to N$ and the search for a $t$ making $f_t$ transverse to a fixed submanifold. The bridge is that transversality of $f_t$ to a submanifold is the regularity of a value of an auxiliary projection built from the family, so Sard supplies almost every $t$. *Example problem:* given a smooth homotopy $H\colon M \times [0,1] \to N$ between two maps, find a level $t$ at which $H(\cdot, t)$ has a prescribed regular value, used to compare degrees across a homotopy.

The third disguised source is **a concrete polynomial or trigonometric map given by formulas**, where one wants to know that its image or its critical image is thin. The bridge is simply that such a map is smooth and one checks the dimensions; the non-obvious part is recognising that "this map cannot be onto" or "almost every value is attained transversally" is a Sard statement rather than an algebraic one. *Example problem:* show that the map $q \mapsto q^k$ on the unit quaternions ($S^3 \to S^3$, so $m = n = 3$) has a regular value, so that its [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|Brouwer degree]] can be computed by counting a finite fibre.

**Targets (Output Amplification).** The bare conclusion is "critical values are negligible". Combined with other ingredients it produces the working tools of the chapter.

Combine the conclusion with **the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]]**. Sard gives a regular value $c$; the regular value theorem then makes $f^{-1}(c)$ an embedded submanifold of the expected dimension $m - n$ (empty when $m < n$, a finite set when $m = n$). The amplified result $E$ is the existence of clean level sets and clean zero sets: this is the mechanism behind generic transversality and hence behind every "perturb until it is nice" argument on the following pages.

Combine the conclusion (face (c)) with **an orientation on $M$ and $N$ and the change-of-variables formula**. Over a regular value $c$ of a map between closed oriented equidimensional manifolds the fibre is finite, and summing the local signs $\operatorname{sign} \det d f_p$ over $p \in f^{-1}(c)$ produces an integer; that this integer is independent of $c$ and homotopy invariant is [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the Brouwer degree theorem]], whose proof begins exactly by invoking face (c) here to know the sum is finite.

Combine the conclusion with **a rank count against the dimension of the source**. If $r > m$ a rank-$r$ bundle has a nowhere-vanishing section, because the section's image inside the $r$-dimensional fibre directions is, in the parametric picture, the image of a map from too small a source to be onto. The amplified result is the [[Thm - Hairy Ball Theorem|hairy-ball theorem]] and its relatives, and, downstream, the triviality of $SU(2)$-bundles below dimension four.

---

# Why Is It True

Forget charts for a moment and picture a smooth map $g$ from an $n$-cube of side $\delta$ into $\mathbb{R}^n$, and suppose the cube contains a point $x$ where the derivative $d g_x$ has rank less than $n$. Rank less than $n$ means the linear image $d g_x(\mathbb{R}^n)$ is a proper subspace, so it sits inside a hyperplane $H_x$ through the origin. To first order, then, $g$ pushes the whole cube into the flat affine slice $g(x) + H_x$: writing $g(x + h) = g(x) + d g_x h + (\text{error})$, the leading term $d g_x h$ never leaves $H_x$, and the error is smaller than any fixed multiple of $\lvert h \rvert$ once $\delta$ is small. So the image of the cube is squeezed into a thin slab straddling an $(n-1)$-dimensional plane — its thickness is not of order $\delta$ but of order $\varepsilon(\delta)\,\delta$ with $\varepsilon(\delta) \to 0$, while its extent along the plane is only of order $\delta$.

Now count. A cube of side $s$ splits into about $(s/\delta)^n$ subcubes of side $\delta$. The bad subcubes (those meeting the critical set) each map into a slab of volume of order $\delta^{n-1} \cdot \varepsilon(\delta)\delta = \varepsilon(\delta)\,\delta^n$; there are at most $(s/\delta)^n$ of them; so the total volume covering the critical image is of order $(s/\delta)^n \cdot \varepsilon(\delta)\delta^n = \varepsilon(\delta)\,s^n$, which tends to $0$ as $\delta \to 0$. The extra factor $\varepsilon(\delta)$, and nothing else, is what makes the total shrink to nothing.

> **The mechanism in one sentence: rank deficiency flattens each small cube's image against a hyperplane, so the image is thinner than a full cube by a factor $\varepsilon(\delta) \to 0$, and that factor survives the cube count to force total measure zero.**

The case $m < n$ is even softer and needs no rank hypothesis at all: the domain simply has fewer than $n$ dimensions, so a compact piece of it, thickened into $\mathbb{R}^n$ by holding the extra coordinates fixed, is a flat slab of measure zero to begin with, and a smooth map cannot inflate a measure-zero set (a smooth map is locally Lipschitz, and Lipschitz maps enlarge covering volumes by at most a fixed constant). The single unifying idea is that when the source is not too big, its critical image is trapped in something whose volume we can drive to zero.

---

# What Makes This Hard

The one genuinely delicate step is that the slab's thickness is controlled by $\varepsilon(\delta)\,\delta$ rather than $\delta$: it is the *first-order* accuracy of the linear approximation, uniform over the compact cube, that supplies the vanishing factor $\varepsilon(\delta)$, and without it the count would only bound the critical image by a set of volume of order $s^n$, which is useless. The common error is to believe one needs Taylor's theorem to second order (and hence $C^2$, or even a bound on second derivatives); in fact only $C^1$ is used, through the uniform continuity of the first derivative on a compact set, and getting the estimate from the mean value inequality applied to $h \mapsto g(x+h) - d g_x h$ rather than from a second-order remainder is what keeps the hypotheses honest. A second subtlety is bookkeeping: measure zero is a chart-local notion, and one must reduce the manifold statement to countably many Euclidean pieces before the Euclidean estimate can be applied, using second countability to keep the collection countable so that countable subadditivity is available.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce to a smooth map between open subsets of Euclidean space by covering source and target with countably many charts, since measure zero is chart-detected and countably additive. In Euclidean space split on $m < n$ versus $m = n$. For $m < n$, thicken the domain to full dimension and use that smooth maps preserve measure zero. For $m = n$, chop a cube into subcubes and use the first-order Taylor estimate to trap each bad subcube's image in a thin slab, then count. Finally read off (a), (b), (c).

**Subgoal decomposition:**

1. **Euclidean measure-zero preservation (equal dimension).** Show a $C^1$ map $g\colon U \to \mathbb{R}^n$ with $U \subseteq \mathbb{R}^n$ open sends measure-zero sets to measure-zero sets.
   - *Hint:* Cover $U$ by compact cubes; on a slightly larger cube $g$ is Lipschitz, and an $L$-Lipschitz map turns a cube of side $s$ into a set of diameter $\le L\sqrt{n}\,s$, so covering volume grows by at most a fixed constant.
   - *Why needed:* It is the engine for the $m < n$ case and expresses "smooth maps do not inflate negligible sets".

2. **Lower-dimensional image is negligible ($m < n$).** Show a $C^1$ map $g\colon U \to \mathbb{R}^n$ with $U \subseteq \mathbb{R}^m$ open and $m < n$ has $g(U)$ of measure zero.
   - *Hint:* Extend to $G(x, z) = g(x)$ on $U \times \mathbb{R}^{n-m}$; then $g(K) = G(K \times \{0\})$ and $K \times \{0\}$ is a flat slab of measure zero; apply subgoal 1.
   - *Why needed:* It is exactly part (a) in local form.

3. **Rank-deficient critical image is negligible ($m = n$).** Show a $C^1$ map $g\colon U \to \mathbb{R}^n$ with $U \subseteq \mathbb{R}^n$ open has $g(\{x : \det d g_x = 0\})$ of measure zero.
   - *Hint:* On a cube of side $s$ cut into $r^n$ subcubes of side $\delta = s/r$; on a bad subcube containing $x$, the image lies within $\varepsilon(\delta)\sqrt{n}\,\delta$ of the hyperplane $g(x) + \operatorname{im}(d g_x)$ and within diameter $L\sqrt{n}\,\delta$; the slab has volume $\le C\varepsilon(\delta)\delta^n$; there are $\le r^n$ bad subcubes.
   - *Why needed:* It is the substantive equal-dimensional case, hence the heart of (b).

4. **Localisation.** Show the manifold statement follows from subgoals 2 and 3 by covering $M$ and $N$ with countably many charts and using countable additivity of measure zero.
   - *Hint:* On the overlap piece $U_i \cap f^{-1}(V_j)$ the coordinate representation $\hat f_{ij}$ has the same critical points as $f$, and its critical values are $\psi_j$ of the critical values of $f$ there.
   - *Why needed:* Measure zero on a manifold is defined chart by chart; without the reduction the Euclidean estimates cannot be applied.

5. **Finiteness of a regular fibre from a compact source ($m = n$).** Show that if $c$ is a regular value and $M$ is compact then $f^{-1}(c)$ is finite.
   - *Hint:* At a regular preimage point $d f_p$ is an isomorphism, so $f$ is a local diffeomorphism there and the point is isolated in the fibre; a closed discrete subset of a compact space is finite.
   - *Why needed:* It is part (c), the finiteness that makes counting arguments (degree, signed zeros) possible.

---

# Lemma Decomposition

> [!note]- Lemma 1: A $C^1$ map between open subsets of $\mathbb{R}^n$ preserves Lebesgue measure zero
> **Statement:** Let $U \subseteq \mathbb{R}^n$ be open and $g\colon U \to \mathbb{R}^n$ be $C^1$. If $A \subseteq U$ has Lebesgue measure zero, then $g(A) \subseteq \mathbb{R}^n$ has Lebesgue measure zero.
>
> **Hint:** Exhaust $U$ by compact cubes; on each, $g$ is Lipschitz by the mean value inequality; a Lipschitz map multiplies covering volumes by a fixed constant.
>
> **Why needed:** It is the tool that pushes the flat slab of the $m < n$ case forward without inflating it (Lemma 2), and it packages "smooth maps do not enlarge negligible sets".
>
> > [!note]- Full proof
> > **Set-up and reduction to a compact cube.** Since $U$ is open it is a countable union $U = \bigcup_{k \in \mathbb{N}} K_k$ of closed cubes $K_k$ with $K_k \subseteq U$ (take, for instance, all dyadic cubes contained in $U$; there are countably many and they cover $U$ because every point of an open set has a small dyadic cube around it inside $U$). Then $A = \bigcup_k (A \cap K_k)$, and $g(A) = \bigcup_k g(A \cap K_k)$. A countable union of measure-zero sets has measure zero — given $\delta > 0$, cover the $k$-th set by cubes of total volume less than $\delta / 2^{k+1}$ and take the union of these covers, of total volume less than $\delta$ — so it suffices to show each $g(A \cap K_k)$ has measure zero.
> >
> > **A Lipschitz constant on an enlargement.** Fix $k$. Because $K_k$ is compact and contained in the open set $U$, there is a closed cube $K_k'$, concentric with $K_k$ and slightly larger, with $K_k \subseteq (K_k')^\circ \subseteq K_k' \subseteq U$; let $\rho = \operatorname{dist}(K_k, \partial K_k') > 0$. The set $K_k'$ is compact and convex and $d g$ is continuous, so $L := \sup_{\xi \in K_k'} \lVert d g_\xi \rVert$ is finite. By the [[Thm - The Mean Value Inequality|vector mean value inequality]] — *for a differentiable map on a convex set with $\lVert d g \rVert \le L$ throughout, $\lvert g(x) - g(y) \rvert \le L\,\lvert x - y \rvert$ for all $x, y$ in the set* — the restriction $g|_{K_k'}$ is $L$-Lipschitz.
> >
> > **Covering the image.** Let $\delta > 0$. Since $A \cap K_k$ has measure zero, cover it by countably many open cubes $\{Q_j\}_{j}$ of side $s_j$ with total volume $\sum_j s_j^{\,n} < \delta$, and, by subdividing any cube of side $\ge \rho/\sqrt{n}$ into smaller cubes (which changes neither the union nor the total volume), arrange that every $Q_j$ has diameter $\sqrt{n}\, s_j < \rho$. Discard those $Q_j$ that do not meet $K_k$; a retained $Q_j$ meets $K_k$ and has diameter less than $\rho = \operatorname{dist}(K_k, \partial K_k')$, so $Q_j \subseteq K_k'$. Hence $A \cap K_k \subseteq \bigcup_j (Q_j \cap K_k')$ with every retained $Q_j \subseteq K_k'$.
> >
> > **The volume bound.** For a retained $Q_j$, the set $g(Q_j)$ has diameter at most $L \cdot \operatorname{diam}(Q_j) = L\sqrt{n}\, s_j$ (as $g|_{K_k'}$ is $L$-Lipschitz and $Q_j \subseteq K_k'$), so it is contained in a cube of side $L\sqrt{n}\, s_j$, of volume $(L\sqrt{n})^n s_j^{\,n}$. Therefore
> > $$g(A \cap K_k) \subseteq \bigcup_j g(Q_j), \qquad \sum_j \operatorname{vol}_n\big(g(Q_j)\big) \le (L\sqrt{n})^n \sum_j s_j^{\,n} < (L\sqrt{n})^n\, \delta \qquad \text{(by the diameter bound and } \sum_j s_j^{\,n} < \delta\text{)}.$$
> > Since $\delta > 0$ was arbitrary and $(L\sqrt{n})^n$ is a fixed constant, $g(A \cap K_k)$ is covered by cubes of arbitrarily small total volume, so it has measure zero. Taking the countable union over $k$, $g(A)$ has measure zero. $\blacksquare$

> [!note]- Lemma 2: A $C^1$ map from a lower-dimensional Euclidean domain has negligible image
> **Statement:** Let $U \subseteq \mathbb{R}^m$ be open, let $m < n$, and let $g\colon U \to \mathbb{R}^n$ be $C^1$. Then $g(U)$ has Lebesgue measure zero in $\mathbb{R}^n$.
>
> **Hint:** Thicken $g$ to a map on an open subset of $\mathbb{R}^n$ by ignoring the new coordinates, so that $g(U)$ becomes the image of a flat measure-zero slab; then quote Lemma 1.
>
> **Why needed:** It is part (a) of the theorem in local Euclidean form — the statement that a lower-dimensional domain cannot fill any open set.
>
> > [!note]- Full proof
> > **The trivial thickening.** Define $G\colon U \times \mathbb{R}^{n-m} \to \mathbb{R}^n$ by $G(x, z) = g(x)$; here $U \times \mathbb{R}^{n-m}$ is an open subset of $\mathbb{R}^m \times \mathbb{R}^{n-m} = \mathbb{R}^n$. Its differential $d G_{(x,z)}(\eta, \zeta) = d g_x(\eta)$ is continuous in $(x, z)$, so $G$ is $C^1$ as a map between open subsets of $\mathbb{R}^n$.
> >
> > **Reduction to a cube.** Since $U$ is open it is a countable union of closed cubes $K \subseteq U$; as $g(U) = \bigcup_K g(K)$ and countable unions of measure-zero sets are measure zero, it suffices to prove each $g(K)$ has measure zero.
> >
> > **The slab is negligible.** Fix such a cube $K \subseteq \mathbb{R}^m$ and consider $K \times \{0\} \subseteq \mathbb{R}^n$. Choose an open box $K'' \subseteq \mathbb{R}^m$ with $K \subseteq K''$ and $\operatorname{vol}_m(K'') \le 2\,\operatorname{vol}_m(K)$. For each $\eta > 0$ the open box $K'' \times (-\eta, \eta)^{\,n-m}$ contains $K \times \{0\}$ and has volume
> > $$\operatorname{vol}_n\big(K'' \times (-\eta, \eta)^{\,n-m}\big) = \operatorname{vol}_m(K'') \cdot (2\eta)^{\,n-m} \xrightarrow[\;\eta \to 0^+\;]{} 0 \qquad \text{(since } n - m \ge 1\text{)},$$
> > so $K \times \{0\}$ is covered by a single open box of arbitrarily small volume and hence has Lebesgue measure zero in $\mathbb{R}^n$.
> >
> > **Push forward.** By Lemma 1 applied to the $C^1$ map $G$ between open subsets of $\mathbb{R}^n$ and the measure-zero set $K \times \{0\}$, the image $G(K \times \{0\})$ has measure zero. But $G(K \times \{0\}) = \{g(x) : x \in K\} = g(K)$. Hence $g(K)$ has measure zero, and taking the countable union over the cubes $K$, so does $g(U)$. $\blacksquare$

> [!note]- Lemma 3: The critical image of an equidimensional $C^1$ map is negligible
> **Statement:** Let $U \subseteq \mathbb{R}^n$ be open and $g\colon U \to \mathbb{R}^n$ be $C^1$. Write $C = \{x \in U : \det d g_x = 0\}$ for its set of critical points (points where the rank of $d g_x$ is less than $n$). Then $g(C)$ has Lebesgue measure zero in $\mathbb{R}^n$.
>
> **Hint:** On a subcube of side $\delta$ containing a critical point, the image lies in a slab of thickness $\sim \varepsilon(\delta)\delta$ against a hyperplane and of extent $\sim \delta$; count the $\le (s/\delta)^n$ bad subcubes of a cube of side $s$.
>
> **Why needed:** It is the substantive equal-dimensional case, from which parts (b) and the $m = n$ half of the main statement follow.
>
> > [!note]- Full proof
> > **Reduction to a cube.** As $U$ is a countable union of closed cubes $K \subseteq U$ and $g(C) = \bigcup_K g(C \cap K)$, and countable unions of measure-zero sets are measure zero, it suffices to fix one closed cube $K \subseteq U$ of side $s$ and show $g(C \cap K)$ has measure zero.
> >
> > **Two uniform constants on an enlargement.** Choose a closed cube $K'$ concentric with $K$ with $K \subseteq (K')^\circ \subseteq K' \subseteq U$. Since $K'$ is compact and $d g$ is continuous, $L := \sup_{\xi \in K'} \lVert d g_\xi \rVert < \infty$, and $d g$ is uniformly continuous on $K'$; let
> > $$\omega(\rho) := \sup\{\lVert d g_a - d g_b \rVert : a, b \in K',\ \lvert a - b \rvert \le \rho\}, \qquad \omega(\rho) \xrightarrow[\;\rho \to 0^+\;]{} 0 \qquad \text{(uniform continuity of } d g \text{ on the compact } K'\text{).}$$
> >
> > **The first-order estimate.** Let $x \in K'$ and $h \in \mathbb{R}^n$ with the segment from $x$ to $x + h$ inside $K'$. Apply the [[Thm - The Mean Value Inequality|vector mean value inequality]] — *$\lvert \phi(x+h) - \phi(x) \rvert \le \big(\sup_{t \in [0,1]} \lVert d\phi_{x+th} \rVert\big)\lvert h \rvert$* — to the auxiliary map $\phi(y) = g(y) - d g_x(y)$, whose differential is $d\phi_y = d g_y - d g_x$. Since $d\phi_{x+th} = d g_{x+th} - d g_x$ has norm at most $\omega(\lvert h \rvert)$ for $t \in [0,1]$ (as $\lvert (x+th) - x \rvert = t\lvert h \rvert \le \lvert h \rvert$ and both points lie in $K'$),
> > $$\big\lvert g(x+h) - g(x) - d g_x\, h \big\rvert = \lvert \phi(x+h) - \phi(x) \rvert \le \omega(\lvert h \rvert)\,\lvert h \rvert \qquad \text{(mean value inequality applied to } \phi\text{).} \tag{$\ast$}$$
> >
> > **The slab around a critical subcube.** Subdivide $K$ into $r^n$ closed subcubes of side $\delta = s/r$; each has diameter $\sqrt{n}\,\delta$, and for $r$ large enough every subcube lies in $K'$. Let $Q$ be a subcube that contains a critical point $x \in C \cap K$; so $\operatorname{rank}(d g_x) < n$, and $\operatorname{im}(d g_x)$ is a proper subspace of $\mathbb{R}^n$, hence contained in some hyperplane through the origin with a chosen unit normal $u_x$, so that $\langle d g_x\, h, u_x\rangle = 0$ for every $h$. For any point $x + h \in Q$ we have $\lvert h \rvert \le \sqrt{n}\,\delta$, and:
> > $$\big\lvert \langle g(x+h) - g(x),\, u_x\rangle \big\rvert = \big\lvert \langle g(x+h) - g(x) - d g_x h,\, u_x\rangle \big\rvert \le \big\lvert g(x+h) - g(x) - d g_x h \big\rvert \le \omega(\sqrt{n}\,\delta)\,\sqrt{n}\,\delta$$
> > (first equality since $\langle d g_x h, u_x\rangle = 0$; first inequality since $\lvert u_x \rvert = 1$ and Cauchy–Schwarz; second by $(\ast)$ with $\lvert h \rvert \le \sqrt{n}\,\delta$), and
> > $$\big\lvert g(x+h) - g(x) \big\rvert \le L\,\lvert h \rvert \le L\sqrt{n}\,\delta \qquad \text{(mean value inequality, } \lVert d g \rVert \le L \text{ on } K'\text{).}$$
> > Writing $\varepsilon(\delta) := \omega(\sqrt{n}\,\delta) \to 0$ as $\delta \to 0$, the first display says $g(Q)$ lies within perpendicular distance $\varepsilon(\delta)\sqrt{n}\,\delta$ of the affine hyperplane $g(x) + \{u_x\}^\perp$, and the second says $g(Q)$ lies within total distance $L\sqrt{n}\,\delta$ of $g(x)$. Hence $g(Q)$ is contained in a rectangular box with one edge of length $2\varepsilon(\delta)\sqrt{n}\,\delta$ (along $u_x$) and the other $n-1$ edges of length $2L\sqrt{n}\,\delta$, of volume
> > $$\operatorname{vol}_n\big(g(Q)\big) \le \big(2\varepsilon(\delta)\sqrt{n}\,\delta\big)\big(2L\sqrt{n}\,\delta\big)^{n-1} = C\,\varepsilon(\delta)\,\delta^{\,n}, \qquad C := 2\sqrt{n}\,(2L\sqrt{n})^{\,n-1}.$$
> >
> > **The count.** There are at most $r^n$ subcubes in all, hence at most $r^n$ bad ones, and $C \cap K$ is contained in the union of the bad subcubes. Therefore
> > $$g(C \cap K) \subseteq \bigcup_{\text{bad } Q} g(Q), \qquad \sum_{\text{bad } Q} \operatorname{vol}_n\big(g(Q)\big) \le r^n \cdot C\,\varepsilon(\delta)\,\delta^{\,n} = r^n \cdot C\,\varepsilon(\delta)\Big(\tfrac{s}{r}\Big)^{\!n} = C\,s^n\,\varepsilon(\delta) \qquad (\delta = s/r).$$
> > As $r \to \infty$ we have $\delta = s/r \to 0$, so $\varepsilon(\delta) \to 0$ and the total covering volume $C s^n \varepsilon(\delta) \to 0$. Enlarging each covering box by an arbitrarily small amount makes the cover one by *open* boxes of still-arbitrarily-small total volume, so $g(C \cap K)$ has Lebesgue measure zero. Taking the countable union over the cubes $K$, $g(C)$ has measure zero. $\blacksquare$

> [!note]- Lemma 4: Localisation — reduction of the manifold statement to Euclidean charts
> **Statement:** Let $f\colon M^m \to N^n$ be smooth. Suppose that for every pair of charts $(U, \varphi)$ of $M$ and $(V, \psi)$ of $N$ with $f(U) \cap V \ne \varnothing$, the coordinate representation $\hat f = \psi \circ f \circ \varphi^{-1}$, defined on the open set $\varphi(U \cap f^{-1}(V)) \subseteq \mathbb{R}^m$, has critical image of Lebesgue measure zero in $\mathbb{R}^n$. Then $f(\operatorname{Crit}(f))$ has measure zero in $N$.
>
> **Hint:** Cover $M$ and $N$ by countably many charts (second countability); a point is critical for $f$ iff it is critical for the local representation; assemble by countable additivity.
>
> **Why needed:** Measure zero on a manifold is defined chart by chart, so the Euclidean Lemmas 2 and 3 only bite after this reduction.
>
> > [!note]- Full proof
> > **Countable atlases.** Because $M$ and $N$ are second countable, each is covered by a countable collection of charts: $M = \bigcup_{i \in \mathbb{N}} U_i$ with charts $\varphi_i\colon U_i \to \mathbb{R}^m$, and $N = \bigcup_{j \in \mathbb{N}} V_j$ with charts $\psi_j\colon V_j \to \mathbb{R}^n$. (A second countable manifold has a countable basis; each basis element inside a chart domain gives a chart, and countably many of them cover.)
> >
> > **Criticality is chart-local.** For indices $i, j$ let $W_{ij} = U_i \cap f^{-1}(V_j)$, an open subset of $M$, and let $\hat f_{ij} = \psi_j \circ f \circ \varphi_i^{-1}$ on $\varphi_i(W_{ij})$. Since $\varphi_i$ and $\psi_j$ are diffeomorphisms, the chain rule gives $d(\hat f_{ij})_{\varphi_i(p)} = d(\psi_j)_{f(p)} \circ d f_p \circ d(\varphi_i^{-1})_{\varphi_i(p)}$, a composition of $d f_p$ with two linear isomorphisms; hence $d(\hat f_{ij})_{\varphi_i(p)}$ is surjective if and only if $d f_p$ is surjective. So $p \in W_{ij}$ is a critical point of $f$ exactly when $\varphi_i(p)$ is a critical point of $\hat f_{ij}$.
> >
> > **Assembling the critical values.** Let $c \in f(\operatorname{Crit}(f))$, say $c = f(p)$ with $d f_p$ not surjective. Pick $i$ with $p \in U_i$ and $j$ with $c \in V_j$; then $p \in W_{ij}$, and by the previous paragraph $\varphi_i(p)$ is a critical point of $\hat f_{ij}$, so $\psi_j(c) = \hat f_{ij}(\varphi_i(p))$ is a critical value of $\hat f_{ij}$. Thus, for each fixed $j$,
> > $$\psi_j\big(f(\operatorname{Crit}(f)) \cap V_j\big) \subseteq \bigcup_{i \in \mathbb{N}} \big(\text{critical image of } \hat f_{ij}\big).$$
> > By hypothesis every set on the right has Lebesgue measure zero, and the union is countable, so the left side has Lebesgue measure zero in $\mathbb{R}^n$. This holds for every $j$, and $\{(V_j, \psi_j)\}$ is an atlas of $N$, so by the one-cover-suffices criterion for [[Def - Set of Measure Zero on a Manifold|measure zero on a manifold]], $f(\operatorname{Crit}(f))$ has measure zero in $N$. $\blacksquare$

> [!note]- Lemma 5: A regular fibre of a map from a compact equidimensional source is finite
> **Statement:** Let $f\colon M^m \to N^n$ be smooth with $m = n$, let $M$ be compact, and let $c \in N$ be a regular value. Then $f^{-1}(c)$ is a finite set.
>
> **Hint:** At a regular preimage point the differential is an isomorphism, so $f$ is a local diffeomorphism and the point is isolated; a closed discrete subset of a compact space is finite.
>
> **Why needed:** It is part (c), the finiteness underlying every counting argument (degree, signed zeros) in this chapter.
>
> > [!note]- Full proof
> > **Each preimage point is isolated in the fibre.** Let $p \in f^{-1}(c)$. Since $c$ is regular, $d f_p\colon T_p M \to T_c N$ is surjective; as $\dim T_p M = m = n = \dim T_c N$, a surjective linear map between spaces of equal dimension is an isomorphism, so $d f_p$ has full rank $n$. Rank is lower semicontinuous, so $f$ has rank $n$ on a neighbourhood of $p$, i.e. it has constant rank $n = m = n$ there; by the [[Thm - The Rank Theorem|rank theorem]] — *a smooth map of constant rank $r$ near $p$ is, in suitable centred charts, the linear model $(x^1, \dots, x^r, \dots, x^m) \mapsto (x^1, \dots, x^r, 0, \dots, 0)$; when $r = m = n$ this model is a coordinate identity, so $f$ is a diffeomorphism from a neighbourhood of $p$ onto a neighbourhood of $c$*. In particular $f$ is injective on a neighbourhood $O_p$ of $p$, so $O_p \cap f^{-1}(c) = \{p\}$: the point $p$ is isolated in $f^{-1}(c)$. Hence $f^{-1}(c)$ is discrete.
> >
> > **A closed discrete subset of a compact space is finite.** The fibre $f^{-1}(c)$ is closed in $M$, being the preimage of the closed set $\{c\}$ under the continuous map $f$ (points are closed since $N$ is Hausdorff). A closed subset of the compact space $M$ is compact, so $f^{-1}(c)$ is compact. The sets $\{O_p \cap f^{-1}(c) : p \in f^{-1}(c)\} = \{\{p\}\}$ form an open cover of $f^{-1}(c)$ (in its subspace topology) by singletons; a finite subcover exists by compactness, which is possible only if $f^{-1}(c)$ is itself finite. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f\colon M^m \to N^n$ be smooth with $m \le n$.
>
> **Step 0 — the objects are well-posed.** The set of critical values is $f(\operatorname{Crit}(f))$ by definition: $c$ is a critical value exactly when some $p \in f^{-1}(c)$ has $d f_p$ not surjective, i.e. $c \in f(\operatorname{Crit}(f))$. Measure zero in $N$ is a chart-independent notion by the diffeomorphism invariance recorded on [[Def - Set of Measure Zero on a Manifold|the measure-zero page]], so the assertion "$f(\operatorname{Crit}(f))$ has measure zero" is meaningful and may be checked on any single atlas.
>
> **Step 1 — reduce to Euclidean charts.** By Lemma 4 it suffices to show that for every chart pair the coordinate representation $\hat f_{ij} = \psi_j \circ f \circ \varphi_i^{-1}$, a smooth map from an open subset of $\mathbb{R}^m$ to $\mathbb{R}^n$ with $m \le n$, has critical image of Lebesgue measure zero. Fix such a $\hat f_{ij}$ and call it $g\colon U \to \mathbb{R}^n$, $U \subseteq \mathbb{R}^m$ open. We split on the dimension comparison.
>
> **Step 2 — the case $m < n$.** Here no $d g_x$ can be surjective (its rank is at most $m < n$), so every point of $U$ is critical and the critical image is all of $g(U)$. By Lemma 2, $g(U)$ has Lebesgue measure zero. Thus the critical image of $g$ is measure zero.
>
> **Step 3 — the case $m = n$.** Here the critical set of $g$ is $C = \{x \in U : \det d g_x = 0\}$, and by Lemma 3 the critical image $g(C)$ has Lebesgue measure zero.
>
> **Step 4 — conclude the main statement.** In either case ($m < n$ via Step 2, $m = n$ via Step 3) every coordinate representation has critical image of measure zero, so by Lemma 4 the set $f(\operatorname{Crit}(f))$ of critical values has measure zero in $N$. This is the main assertion.
>
> **Step 5 — part (a), the case $m < n$.** When $m < n$, every $p \in M$ has $d f_p$ of rank at most $m < n$, hence not surjective, so every point of $M$ is a critical point and $f(\operatorname{Crit}(f)) = f(M)$. By Step 4 (equivalently, by Lemma 2 applied in each chart and Lemma 4), $f(M)$ has measure zero in $N$. Finally $f(M)$ has empty interior: were some nonempty open $W \subseteq N$ contained in $f(M)$, then in a chart $\psi(W \cap V)$ would be a nonempty open subset of $\mathbb{R}^n$, which contains a cube of positive Lebesgue volume and therefore cannot be covered by cubes of arbitrarily small total volume — contradicting that $f(M)$, hence $W$, has measure zero. So $f(M)$ has empty interior.
>
> **Step 6 — part (b), the case $m = n$.** The set of critical values $f(\operatorname{Crit}(f))$ has measure zero by Step 4, and the set of regular values is its complement $N \setminus f(\operatorname{Crit}(f))$. Let $W \subseteq N$ be any nonempty open set; choose a chart $(V, \psi)$ with $W \cap V \ne \varnothing$, so $\psi(W \cap V)$ is a nonempty open subset of $\mathbb{R}^n$ and contains a cube of positive volume, whence $\psi(W \cap V)$ does not have measure zero. Therefore $W \cap V$ is not contained in the measure-zero set $f(\operatorname{Crit}(f))$, so $W$ meets $N \setminus f(\operatorname{Crit}(f))$. As $W$ was an arbitrary nonempty open set, the regular values are dense in $N$.
>
> **Step 7 — part (c), a compact source and a regular value.** Assume $M$ compact and $c$ a regular value; recall $m \le n$. If $m < n$, then by Step 5 every point of $M$ is critical, so a regular value $c$ can have no critical (hence no) preimage point: $f^{-1}(c) = \varnothing$, which is finite. If $m = n$, then $f^{-1}(c)$ is finite by Lemma 5. In both cases $f^{-1}(c)$ is finite.
>
> Combining Steps 4–7, the set of critical values of $f$ has measure zero in $N$, and (a), (b), (c) hold. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Nonlinear analysis: solvability of an underdetermined system.** Consider a smooth map $F\colon \mathbb{R}^m \to \mathbb{R}^n$ with $m < n$ given by explicit formulas, and ask whether the equation $F(x) = b$ can be solved for a *generic* right-hand side $b$. The theorem applies because $m < n$ forces $F(\mathbb{R}^m)$ to have measure zero and empty interior, so for almost every $b$ — indeed for a dense open set of $b$ — the system has *no* solution. This is non-obvious because a naive count of equations versus unknowns says nothing about which right-hand sides are attainable; the measure-zero conclusion is what turns "too few unknowns" into "almost no attainable targets".

**Numerical continuation and homotopy methods.** In path-following algorithms one deforms an easy system into a hard one along a homotopy $H\colon \mathbb{R}^n \times [0,1] \to \mathbb{R}^n$ and follows the solution curve $H^{-1}(0)$. The theorem (in the parametrised form that feeds the [[Thm - Generic Sections are Transverse to the Zero Section|transversality theorem]]) guarantees that for almost every choice of starting data $0$ is a regular value, so the solution set is a clean one-dimensional manifold with no bifurcations, and the algorithm can march along it. The theorem applies because criticality of the augmented map is a measure-zero event in the auxiliary parameter; it is non-obvious because it converts a global guarantee ("the path never gets stuck") into a local generic condition on the derivative.

**Statistical geometry: a smooth curve of parameters cannot be dense in a model.** In information geometry a one-parameter family of probability distributions is a smooth curve $t \mapsto p_t$ in an $n$-dimensional statistical manifold with $n \ge 2$. The theorem, with $m = 1 < n$, shows the image of the curve has measure zero and empty interior, so a single smooth parameter can never sweep out an open region of models. This is non-obvious because a curve can be made to pass close to any finite list of target distributions, tempting one to think it is "essentially onto"; the measure-zero conclusion draws the sharp line between approximation and coverage.

---

# Bridges

- **The regular value theorem.** The natural partner of Sard's theorem is [[Thm - Regular Value Theorem on Manifolds|the regular value theorem]]: Sard produces a value $c$ over which $f$ is a submersion at every preimage point, and the regular value theorem then upgrades that value into geometry, presenting $f^{-1}(c)$ as an embedded submanifold of dimension $m - n$ with tangent space $\ker d f_p$ at each $p$. Used together they are the usual route from an arbitrary smooth map to a clean submanifold: choose a regular value by Sard, cut with the regular value theorem. When $m = n$ the "submanifold" is a discrete set, and part (c) of the present page supplies its finiteness over a compact source.

- **Generic sections and transversality.** [[Thm - Generic Sections are Transverse to the Zero Section|The generic-sections theorem]] is built directly on this page. One assembles a section into a finite-parameter family $s_a = \sum_i a_i s_i$, forms the smooth map $(x, a) \mapsto s_a(x)$ into the total space, and applies Sard to the projection from the (smooth) common zero locus down to the parameter space $\mathbb{R}^N$; the source of that projection has dimension $m + N - r \le N$ in the relevant rank-$r$ case, so the restricted theorem of this page — source dimension not exceeding target dimension — is exactly what applies, and almost every parameter $a$ makes $s_a$ transverse to the zero section.

- **The Brouwer degree.** [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|The degree theorem]] uses this page twice: face (b) supplies a regular value at which to compute the degree, and face (c) makes the fibre over that value finite, so that the signed count $\sum_{p \in f^{-1}(c)} \operatorname{sign} \det d f_p$ is a genuine finite integer. The homotopy invariance of the degree is then a separate argument, but the very definition-by-counting is licensed here.

- **The hairy-ball theorem and low-dimensional bundle triviality.** [[Thm - Hairy Ball Theorem|The hairy-ball theorem]] and the triviality statements of §3.6 exploit face (a) in the rank count "fibre rank exceeds base dimension implies a nowhere-vanishing section": in the parametric picture a section that must vanish would give an onto map from a source of dimension below the fibre dimension, which face (a) forbids. This is the mechanism by which an $SU(2)$-bundle over a manifold of dimension at most three, whose associated $\mathbb{C}^2$-bundle has real fibre rank four, acquires a global unit section and hence a trivialisation.

---

# Unlocked by This

> [!tip] Transversality as genericity *(from Differential Topology)*
> Once critical values are known to be negligible, "transverse" becomes synonymous with "generic": a property that holds after an arbitrarily small perturbation and on a dense set of parameters. This reframes existence questions ("is there a nowhere-zero section?", "can these submanifolds be made to meet cleanly?") as measure-zero-avoidance questions, the organising idea of the next two pages. See **Thm - Generic Sections are Transverse to the Zero Section**.

> [!tip] Sard–Smale in infinite dimensions *(from Global Analysis)*
> The finite-dimensional theorem of this page is the model for its Banach-manifold analogue, the Sard–Smale theorem, which underlies the transversality theory of moduli spaces in gauge theory. There the "source dimension" is replaced by the finite index of a Fredholm map, and the general Sard theorem for $m > n$ enters as a lemma; both are proved in chapter X. See **Gauge Theory X — Fredholm Maps, Transversality, and Degree**.
