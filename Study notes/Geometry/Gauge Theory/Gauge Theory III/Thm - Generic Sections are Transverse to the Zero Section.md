---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension"
  - "Thm - Regular Value Theorem on Manifolds"
  - "Thm - Existence of Smooth Partitions of Unity"
  - "Thm - Existence of Smooth Bump Functions"
  - "Def - Vector Bundle"
  - "Def - Local Frame"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth, compact, Hausdorff, second-countable manifold of dimension $m$, and $\pi\colon E\to M$ is a real [[Def - Vector Bundle|vector bundle]] of rank $r$; its fibre over $x\in M$ is $E_x=\pi^{-1}(x)$, a real vector space of dimension $r$, and $\Gamma(E)$ denotes the space of smooth sections $s\colon M\to E$ with $\pi\circ s=\operatorname{id}_M$. The **zero section** is the section $0_E\in\Gamma(E)$ with $0_E(x)=0_x$, the zero vector of $E_x$; by abuse of the same symbol we also write $0_E\subseteq E$ for its image $\{0_x:x\in M\}$, an embedded submanifold of $E$ diffeomorphic to $M$ under $\pi$. A **local frame** over an open set $U\subseteq M$ is an $r$-tuple $(e_1,\dots,e_r)$ of sections of $E|_U$ with $(e_1(y),\dots,e_r(y))$ a basis of $E_y$ for every $y\in U$; local frames exist over any trivialising open set by the definition of a vector bundle (see [[Def - Local Frame]]).

Given a section $s\in\Gamma(E)$ and a point $x$ with $s(x)=0_x$ (a **zero** of $s$), the **vertical derivative** of $s$ at $x$ is a linear map
$$D_xs\colon T_xM\longrightarrow E_x,$$
defined intrinsically in Lemma 1 below and computed, in any local trivialisation $\psi_U\colon E|_U\xrightarrow{\ \cong\ }U\times\mathbb R^r$ in which $s$ has principal part $\sigma\colon U\to\mathbb R^r$ (that is, $\psi_U(s(y))=(y,\sigma(y))$), by $D_xs=d\sigma_x$ under the identification $E_x\cong\mathbb R^r$ furnished by $\psi_U$. This map is well defined **only at zeros** of $s$; away from the zeros a vertical derivative requires the extra datum of a connection, which we do not use here.

We write $s\pitchfork 0_E$ and say $s$ is **transverse to the zero section** when, at every zero $x$ of $s$, the vertical derivative $D_xs$ is surjective. We write $Z(s)=\{x\in M:s(x)=0_x\}$ for the zero set. For a point $a=(a_1,\dots,a_N)\in\mathbb R^N$ and a fixed tuple of sections $s_1,\dots,s_N\in\Gamma(E)$ we write $s_a:=\sum_{i=1}^Na_is_i\in\Gamma(E)$, and $\lVert a\rVert$ for the Euclidean norm of $a$. "Almost every $a$" means: outside a subset of $\mathbb R^N$ of Lebesgue measure zero. The symbol $\operatorname{pr}_2\colon M\times\mathbb R^N\to\mathbb R^N$ is the projection $(x,a)\mapsto a$.

> [!warning] Convention: which side the two conventions for the vertical derivative sit on
> Some texts write the linearisation of a section at a zero as a map $T_xM\to E_x$ (the convention here) and others as the intrinsic derivative $ds_x\colon T_xM\to T_{0_x}E$ composed with the vertical projection; the two agree exactly, and Lemma 1 proves the coordinate formula $D_xs=d\sigma_x$ so that no picture is needed. There is no sign ambiguity. Transversality to the zero section is a property of the section alone; it does not depend on any metric, connection, or orientation.

The full symbol registry for the chapter is on the parent page [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]].

---

# Statement

> **Theorem (generic sections are transverse to the zero section).** Let $\pi\colon E\to M$ be a real vector bundle of rank $r$ over a compact manifold $M$ of dimension $m$.
>
> **(a) Finite spanning family.** There exist finitely many sections $s_1,\dots,s_N\in\Gamma(E)$ such that at every point $x\in M$ the vectors $s_1(x),\dots,s_N(x)$ span the fibre $E_x$.
>
> **(b) Genericity of transversality.** Assume in addition that $r\ge m$. With $s_1,\dots,s_N$ as in (a), for almost every $a\in\mathbb R^N$ the section $s_a=\sum_{i=1}^Na_is_i$ is transverse to the zero section: at each zero $x$ of $s_a$ the vertical derivative $D_xs_a\colon T_xM\to E_x$ is surjective.
>
> **(c) Consequences of transversality.** Suppose $r\ge m$ and $s_a$ is transverse to the zero section.
> - If $r>m$, then $s_a$ is nowhere vanishing; in particular $E$ admits a nowhere-vanishing section.
> - If $r=m$, then $s_a$ has only finitely many zeros, each **nondegenerate** in the sense that $D_xs_a\colon T_xM\to E_x$ is an isomorphism. When $M$ and $E$ are oriented, each zero $x$ carries a well-defined sign
> $$\epsilon(x)=\operatorname{sign}\det D_xs_a\in\{+1,-1\},$$
> the determinant taken with respect to positively oriented bases of $T_xM$ and of $E_x$.
>
> **(d) Relative version.** Let $K\subseteq M$ be closed and $s\in\Gamma(E)$ a section that is transverse to the zero section on an open neighbourhood of $K$; assume $r\ge m$. Then for every $\varepsilon>0$ there is a section $s'\in\Gamma(E)$ with $s'=s$ on a neighbourhood of $K$, with $s'$ transverse to the zero section on all of $M$, and with $\sup_M\lVert s'-s\rVert<\varepsilon$ (norm taken in any fixed fibre metric).

Parts (b)–(d) are stated under the standing hypothesis $r\ge m$, which is exactly the regime the classification theorems of this chapter require (an associated bundle $P\times_{SU(2)}\mathbb C^2$ has real rank $4$ over a base of dimension at most $4$; a complex line bundle over a surface has real rank $2$ over a base of dimension $2$). The reason for the hypothesis is that the proof of (b) applies the restricted Sard theorem to a projection whose source has dimension $m+N-r$ and whose target has dimension $N$, and the restricted theorem needs source dimension not exceeding target dimension, that is, $m\le r$.

**Scope remark (not used, not proved here).** For $r<m$ the same genericity conclusion in (b) still holds, but its proof requires the general Sard theorem for maps whose source dimension exceeds the target dimension; that theorem is proved in chapter X as a lemma of the Sard–Smale theorem and is never invoked in chapters I–VI. Nothing below depends on the case $r<m$.

---

# Motivation

Ask the most basic structural question one can ask about a vector bundle $E\to M$: does it have a section that is never zero? A nowhere-vanishing section is a trivialisation of a line's worth of the bundle, a first step towards splitting off a trivial summand, and — when the bundle is a frame bundle or an associated bundle — the difference between a bundle that is trivial and one that is not. The tangent bundle of the two-sphere has no nowhere-vanishing section; this is the hairy-ball theorem, and it is the reason $TS^2$ is nontrivial. So the existence of a nowhere-vanishing section is a genuine invariant, and we would like a systematic way to produce one when it exists and to detect the obstruction when it does not.

The naive approach — pick a section and hope it misses the zero section — fails, because a section can be tangent to the zero section, or vanish on a large set, in ways that are unstable and uninformative. What we want instead is a section in **general position**: one that meets the zero section as cleanly as the dimensions allow. If the bundle has rank $r$ and the base has dimension $m$, then a section is a map from an $m$-dimensional space into an $(m+r)$-dimensional total space, the zero section is an $m$-dimensional submanifold, and two submanifolds of a $(m+r)$-manifold of dimensions $m$ and $m$ generically meet in dimension $m+m-(m+r)=m-r$. When $r>m$ this "dimension" is negative, which is the geometry's way of saying that generically they do not meet at all — a generic section is nowhere zero. When $r=m$ they meet in dimension zero — a generic section vanishes at isolated points. The theorem makes "generic" precise and proves that the generic behaviour is the typical behaviour: almost every section in a suitable finite-parameter family is transverse to the zero section, and transversality forces exactly the dimension count above.

The technique that delivers this is one of the central devices of differential topology, the **parametric transversality argument** of Thom. One does not perturb a single section by hand; instead one assembles a finite-dimensional family $s_a=\sum a_is_i$ that is rich enough to move the section in every fibre direction, studies the single large map $(x,a)\mapsto s_a(x)$, and reads off from the Sard theorem — applied once, to a projection — that almost every parameter value gives a transverse section. The miracle is that a statement about "almost every section" (an infinite-dimensional space of perturbations) is proved by a measure-zero statement in a finite-dimensional parameter space. Everything downstream in this chapter — the triviality of $SU(2)$-bundles in low dimensions, the classification of line bundles over surfaces by their degree, the fact that every $SU(2)$-bundle over a four-manifold is trivial off a single point and hence built by clutching — rests on this one theorem.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypotheses are mild: a vector bundle over a compact manifold, with the rank at least the dimension. The skill is to recognise a problem that secretly presents such a bundle even when no bundle is named.

The first disguised source is **a principal bundle carrying a representation whose target space out-dimensions the base**. If $P\to M$ is a principal $G$-bundle and $\rho\colon G\to GL(V)$ a representation, the associated bundle $E=P\times_\rho V$ (see [[Def - Associated Bundle]]) is a vector bundle of rank $\dim_{\mathbb R}V$. When $\dim_{\mathbb R}V>\dim M$ the theorem's case $r>m$ applies and $E$ has a nowhere-vanishing section — which, for the right $G$ and $\rho$, is equivalent to triviality of $P$ itself. The non-obvious step is to pass from the principal bundle, which has no linear structure, to the associated vector bundle where "nowhere-vanishing section" makes sense and where a fibre metric can normalise it. *Example problem:* show that a principal $SU(2)$-bundle over a compact three-manifold is trivial by applying the theorem to $E=P\times_{SU(2)}\mathbb C^2$, of real rank $4>3$, obtaining a unit section and hence a section of $P$.

The second disguised source is **a closed surface bearing an oriented rank-two real bundle**, most often a complex line bundle read as a real bundle of rank two. Here $r=m=2$, so a generic section has finitely many nondegenerate zeros, each with a sign, and the signed count is a stable integer — the degree of the bundle. The bridge is the identification of a complex line bundle with an oriented real rank-two bundle (multiplication by $i$ orients each fibre), which converts a question about holomorphic-looking data into a transversality count. *Example problem:* compute the degree of a line bundle $L\to\Sigma$ over a closed oriented surface as the number of zeros of a generic section, counted with sign.

The third disguised source is **a manifold on which one seeks a vector field with isolated, generic zeros**, as in the computation of an Euler characteristic. Taking $E=TM$ gives $r=m=\dim M$, and a generic section — a generic vector field — has finitely many nondegenerate zeros with signs. The non-obvious recognition is that the tangent bundle is just one vector bundle among many, so the general transversality theorem specialises to produce exactly the vector fields that the Poincaré–Hopf theorem counts. *Example problem:* produce a vector field on a closed surface with isolated nondegenerate zeros whose signed sum is the Euler number, as the starting datum for [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf]].

**Targets (Output Amplification)**

The bare output is a transverse section; combined with other constructions it does a great deal.

Combine transversality with **the simple transitivity of $SU(2)$ on the unit sphere of $\mathbb C^2$**. When $r>m$ the theorem gives a nowhere-vanishing section of $E=P\times_{SU(2)}\mathbb C^2$; normalising it to unit length and using that $SU(2)$ acts simply transitively on the unit sphere $S^3\subseteq\mathbb C^2$ identifies $P$ with the unit sphere bundle and produces a section of $P$, hence a trivialisation. The payoff is the theorem that **every $SU(2)$-bundle over a compact manifold of dimension at most three is trivial**, proved on [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds]].

Combine transversality with **the homogeneity lemma and the clutching construction**. When $r=m=4$, a generic section of $E=P\times_{SU(2)}\mathbb C^2$ over a closed four-manifold has finitely many zeros; the [[Thm - Homogeneity Lemma for Connected Manifolds|homogeneity lemma]] gathers them into one coordinate disc, so $P$ is trivial off that disc, and the [[Thm - Clutching Construction for Bundles over a Closed Manifold|clutching construction]] then presents $P$ by a single map $S^3\to SU(2)$ whose degree is the Chern number. The payoff is the statement "**every $SU(2)$-bundle over a four-manifold is trivial off a point**", the geometric heart of the four-dimensional classification.

Combine transversality with **degree theory on the boundary circle**. For a line bundle over a surface, the signed zero count is turned, via clutching, into the winding number of a transition function, giving the **classification of $U(1)$-bundles over surfaces by an integer degree** (see [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class]]). The extra ingredient is the [[Thm - Winding Number of a Map from the Circle to U(1)|winding number]], and the payoff is that a single integer is a complete invariant.

---

# Why Is It True

Picture a section $s$ as the graph of a function over $M$ sitting inside the total space $E$, and the zero section as the "floor" $0_E$. A zero of $s$ is a point where the graph touches the floor. There are two ways the graph can touch the floor: it can **cross** it, cutting through cleanly, or it can **graze** it, staying tangent. Transversality is the statement that the graph only ever crosses, never grazes. At a crossing, the way the section climbs off the floor as you move in the base — that rate of climb, measured in the fibre directions, is the vertical derivative $D_xs$ — spans all the fibre directions; nothing is left tangent. That is precisely "$D_xs$ surjective".

Grazing is the exceptional, unstable behaviour, and the whole content of the theorem is that you can perturb it away, all of it at once, by a generic choice of coefficients. Here is the mechanism. Assemble enough sections $s_1,\dots,s_N$ that at every single point they already fill the fibre — that is part (a), and it is a soft partition-of-unity fact. Now the family $s_a=\sum a_is_i$ can push the value $s_a(x)$ in **any** fibre direction at $x$, just by nudging $a$. Form the one big map $F(x,a)=s_a(x)$. Because the $a$-directions alone already reach every fibre vector, $F$ crosses the floor transversally as a map of the enlarged domain $M\times\mathbb R^N$; its zero set $W=F^{-1}(0_E)$ is therefore a clean submanifold. The question "for which fixed $a$ is $s_a$ transverse?" becomes "for which $a$ is the graph $s_a$ transverse?", and unwinding the definitions shows this is exactly the question "for which $a$ is $a$ a regular value of the projection $W\to\mathbb R^N$?". Sard's theorem answers: almost every $a$.

> **The one-sentence mechanism:** enlarging the section to a parameter family that already fills every fibre turns "the section is transverse to the zero section" into "the parameter is a regular value of a projection", and Sard's theorem makes almost every parameter regular.

The dimension count that produces the corollaries is now automatic. Transversality says that at a zero the map $D_xs_a\colon T_xM\to E_x$ is onto. If $r>m$ there is no onto map from an $m$-dimensional space to an $r$-dimensional one, so there can be **no** zeros — the section is nowhere vanishing. If $r=m$ an onto map between equal dimensions is an isomorphism, so each zero is nondegenerate and, being nondegenerate, is isolated; compactness makes the isolated zeros finite in number, and orientations give each a sign.

---

# What Makes This Hard

The subtle point is that transversality of $s_a$ is a condition **at the zeros of $s_a$**, and the location of those zeros changes as $a$ changes — so one cannot fix a point and perturb. The parametric argument resolves this by never fixing a point: it studies the total zero set $W$ across all parameters at once and then projects. The single most common error is to confuse the transversality of the **big** map $F$ (which is easy, and holds because the parameter directions alone fill the fibre) with the transversality of the **individual** section $s_a$ for fixed $a$ (which is the conclusion, and holds only for almost every $a$); the bridge between the two is the identity "$a$ is a regular value of $\operatorname{pr}_2|_W$ if and only if $s_a\pitchfork 0_E$", and getting that identity right — in particular seeing why surjectivity of the parameter derivative is what lets you cancel it — is the crux. A second trap is the relative version (d): naively multiplying the perturbation by a cutoff fails on the collar where the cutoff transitions, because there the vertical derivative acquires an extra rank-one term from the differential of the cutoff; the fix is to keep the perturbation small so that transversality, being an open condition on a compact set, is not destroyed.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build a finite family of sections that spans every fibre (partition of unity). Form the total evaluation map $F(x,a)=s_a(x)$; because the parameter directions already surject onto each fibre, its zero set $W$ is a submanifold. Show that a fixed $a$ gives a transverse section exactly when $a$ is a regular value of the projection $W\to\mathbb R^N$, and invoke the restricted Sard theorem (legitimate because $r\ge m$ makes $\dim W\le N$). Read off the corollaries by counting dimensions, and prove the relative version by combining parametric transversality on the region where the cutoff is positive with the stability of transversality under small perturbations on the compact collar.

**Subgoal decomposition:**

1. **The vertical derivative and the meaning of transversality.** Define $D_xs$ intrinsically at a zero and prove the coordinate formula; prove $s\pitchfork 0_E$ if and only if $D_xs$ is surjective at every zero.
   - *Hint:* At a zero the tangent space of the total space splits canonically into the tangent to the zero section and the vertical space $\cong E_x$; project.
   - *Why needed:* Everything below is phrased in terms of $D_xs$; without well-definedness the statement is empty.

2. **A finite spanning family.** Produce $s_1,\dots,s_N$ spanning every fibre.
   - *Hint:* Local frames times bump functions, then compactness.
   - *Why needed:* It is part (a), and its spanning property is exactly what makes the parameter directions of $F$ surjective.

3. **The parametric map and the unwinding.** Show $W=F^{-1}(0_E)$ is a submanifold of dimension $m+N-r$, and that $a$ is a regular value of $\operatorname{pr}_2|_W$ if and only if $s_a\pitchfork 0_E$.
   - *Hint:* Work in a trivialisation: the principal part $\widehat F(x,a)=\sum a_i\sigma_i(x)$ has $0$ as a regular value because $\partial_a\widehat F$ already surjects; then chase the linear algebra of $\ker d\widehat F$ under the projection.
   - *Why needed:* It converts the analytic statement (a.e. section transverse) into a Sard statement about one projection.

4. **Stability of transversality near a compact set.** If $s\pitchfork 0_E$ near a compact $L$, then every section $C^1$-close to $s$ on $L$ has all its zeros in $L$ transverse.
   - *Hint:* Suppose not, extract a convergent sequence of bad zeros, and pass to the limit using that non-surjective matrices form a closed set.
   - *Why needed:* It is the device that makes the relative version (d) work across the cutoff collar.

---

# Lemma Decomposition

> [!note]- Lemma 1: The vertical derivative is well defined at a zero, and transversality means it is surjective
> **Statement:** Let $s\in\Gamma(E)$ and let $x$ be a zero of $s$. Then there is a canonical splitting $T_{0_x}E=T_{0_x}(0_E)\oplus V_x$ with $V_x=\ker(d\pi_{0_x})$ canonically isomorphic to $E_x$, and the map $D_xs:=\operatorname{pr}_{V_x}\circ ds_x\colon T_xM\to E_x$ is independent of all choices. In any local trivialisation with principal part $\sigma$ of $s$, one has $D_xs=d\sigma_x$ under $E_x\cong\mathbb R^r$. Finally, $s$ is transverse to the submanifold $0_E$ at $x$ if and only if $D_xs$ is surjective.
>
> **Hint:** The fibre is a vector space, so its tangent space at $0_x$ is canonically the fibre again; the zero section provides the complementary horizontal space.
>
> **Why needed:** It gives meaning to the vertical derivative and reduces "transverse to the zero section" to a rank condition that the rest of the proof manipulates.
>
> > [!note]- Full proof
> > **Step 0 — the canonical splitting.** The projection $\pi\colon E\to M$ is a submersion, so $V_x:=\ker(d\pi_{0_x})\subseteq T_{0_x}E$ has dimension $\dim T_{0_x}E-\dim T_xM=(m+r)-m=r$. The fibre $E_x=\pi^{-1}(x)$ is a smooth submanifold of $E$ (the preimage of the regular value $x$), an $r$-dimensional real vector space, and its tangent space at the point $0_x$ is contained in $V_x$ and has the same dimension $r$, so $T_{0_x}E_x=V_x$. Because $E_x$ is a vector space, there is a canonical isomorphism
> > $$\iota_x\colon E_x\xrightarrow{\ \cong\ }V_x,\qquad \iota_x(v)=\tfrac{d}{dt}\Big|_{t=0}(0_x+tv)=\tfrac{d}{dt}\Big|_{t=0}(tv),$$
> > which is the standard identification of a finite-dimensional vector space with its tangent space at any point. The zero section $0_E\colon M\to E$ satisfies $\pi\circ 0_E=\operatorname{id}_M$, so $d\pi_{0_x}\circ d(0_E)_x=\operatorname{id}_{T_xM}$; hence $d(0_E)_x\colon T_xM\to T_{0_x}E$ is injective and its image $T_{0_x}(0_E)$ meets $V_x=\ker d\pi_{0_x}$ only in $0$. By dimension count $\dim T_{0_x}(0_E)+\dim V_x=m+r=\dim T_{0_x}E$, so
> > $$T_{0_x}E=T_{0_x}(0_E)\oplus V_x.$$
> > Let $\operatorname{pr}_{V_x}\colon T_{0_x}E\to V_x$ be the projection with kernel $T_{0_x}(0_E)$, and set $D_xs:=\iota_x^{-1}\circ\operatorname{pr}_{V_x}\circ ds_x\colon T_xM\to E_x$. No choices entered: both summands of the splitting and $\iota_x$ are canonical.
> >
> > **Step 1 — the coordinate formula.** Fix a trivialisation $\psi_U\colon E|_U\to U\times\mathbb R^r$ over an open $U\ni x$, and write the section as $\psi_U\circ s=(\operatorname{id},\sigma)$ with $\sigma\colon U\to\mathbb R^r$ smooth. In these coordinates $E|_U\cong U\times\mathbb R^r$, the projection is $\pi(y,w)=y$, the zero section is $y\mapsto(y,0)$, and $0_x=(x,0)$. The identification $\iota_x$ carries $E_x\cong\mathbb R^r$ to $V_x=\{0\}\times\mathbb R^r=T_{(x,0)}(\{x\}\times\mathbb R^r)$, and the splitting is the standard $T_{(x,0)}(U\times\mathbb R^r)=T_xU\oplus\mathbb R^r$. Now $ds_x=(\operatorname{id},d\sigma_x)\colon T_xM\to T_xU\oplus\mathbb R^r$, and $\operatorname{pr}_{V_x}$ discards the first summand, so $\iota_x^{-1}\circ\operatorname{pr}_{V_x}\circ ds_x=d\sigma_x$. Thus $D_xs=d\sigma_x$ under $E_x\cong\mathbb R^r$, as claimed. (For a second trivialisation with principal part $\sigma'=g\,\sigma$, where $g\colon U'\to GL_r(\mathbb R)$ is the smooth transition, the product rule gives $d\sigma'_x=g(x)\,d\sigma_x+(dg_x)\,\sigma(x)$; since $x$ is a zero, $\sigma(x)=0$, so $d\sigma'_x=g(x)\,d\sigma_x$, which is exactly $d\sigma_x$ read through the fibre isomorphism $g(x)$. The two coordinate computations therefore describe the same intrinsic map, confirming independence of choices directly.)
> >
> > **Step 2 — transversality equals surjectivity.** By definition $s\pitchfork 0_E$ at the zero $x$ means $\operatorname{im}(ds_x)+T_{0_x}(0_E)=T_{0_x}E$. Using the splitting $T_{0_x}E=T_{0_x}(0_E)\oplus V_x$, add $T_{0_x}(0_E)$ to both sides and quotient: the condition holds if and only if $\operatorname{pr}_{V_x}\big(\operatorname{im}(ds_x)\big)=V_x$, that is, if and only if $\operatorname{pr}_{V_x}\circ ds_x$ is surjective onto $V_x$. Composing with the isomorphism $\iota_x^{-1}$ preserves surjectivity, so this is equivalent to $D_xs\colon T_xM\to E_x$ being surjective. Therefore $s$ is transverse to $0_E$ at $x$ if and only if $D_xs$ is surjective, and $s\pitchfork 0_E$ (transverse at every zero) if and only if $D_xs$ is surjective at every zero of $s$. $\blacksquare$

> [!note]- Lemma 2: A vector bundle over a compact manifold has a finite family of sections spanning every fibre
> **Statement:** Let $E\to M$ be a vector bundle of rank $r$ over a compact manifold $M$. There exist finitely many sections $s_1,\dots,s_N\in\Gamma(E)$ such that $\{s_1(x),\dots,s_N(x)\}$ spans $E_x$ for every $x\in M$.
>
> **Hint:** Around each point take a local frame, cut it off by a bump function, and use compactness to reduce to a finite cover.
>
> **Why needed:** This is part (a); its spanning property is precisely what makes the parameter derivative of the total map $F$ surjective in Lemma 3.
>
> > [!note]- Full proof
> > **Step 0 — local data.** Fix $x\in M$. By the definition of a vector bundle there is an open trivialising neighbourhood $U_x\ni x$ carrying a [[Def - Local Frame|local frame]] $(e_1^x,\dots,e_r^x)$, so that $(e_1^x(y),\dots,e_r^x(y))$ is a basis of $E_y$ for every $y\in U_x$.
> >
> > **Step 1 — cut off to global sections.** By the [[Thm - Existence of Smooth Bump Functions|existence of smooth bump functions]] — for a point $x$ in an open set $U_x$ there is $\chi_x\in C^\infty(M)$ with $0\le\chi_x\le1$, $\chi_x(x)=1$, and $\operatorname{supp}\chi_x\subseteq U_x$ compact — choose such a $\chi_x$. Define, for $j=1,\dots,r$, the global sections
> > $$\widetilde e_j^{\,x}(y):=\begin{cases}\chi_x(y)\,e_j^x(y),& y\in U_x,\\[2pt] 0_y,& y\notin\operatorname{supp}\chi_x,\end{cases}$$
> > which is smooth because the two definitions agree (both give $0_y$) on the overlap $U_x\setminus\operatorname{supp}\chi_x$. Let $W_x:=\{y\in M:\chi_x(y)>0\}$, an open set containing $x$ (since $\chi_x(x)=1>0$) and contained in $U_x$. For $y\in W_x$ the vectors $\widetilde e_j^{\,x}(y)=\chi_x(y)e_j^x(y)$ are the basis $(e_j^x(y))_j$ scaled by the positive number $\chi_x(y)$, hence themselves a basis of $E_y$; in particular they span $E_y$.
> >
> > **Step 2 — finiteness by compactness.** The family $\{W_x\}_{x\in M}$ is an open cover of the compact manifold $M$, so it has a finite subcover $W_{x_1},\dots,W_{x_k}$. Collect all the associated sections:
> > $$\{s_1,\dots,s_N\}:=\{\widetilde e_j^{\,x_\ell}:1\le \ell\le k,\ 1\le j\le r\},\qquad N=kr.$$
> > For any $y\in M$ there is $\ell$ with $y\in W_{x_\ell}$, and then $\widetilde e_1^{\,x_\ell}(y),\dots,\widetilde e_r^{\,x_\ell}(y)$ already span $E_y$ by Step 1. A fortiori the full collection $s_1(y),\dots,s_N(y)$ spans $E_y$. Since $y$ was arbitrary, the family spans every fibre. $\blacksquare$

> [!note]- Lemma 3: The parametric zero set is a submanifold, and regular values of its projection are transverse parameters
> **Statement:** Let $s_1,\dots,s_N\in\Gamma(E)$ span every fibre (Lemma 2), and define the smooth map $F\colon M\times\mathbb R^N\to E$ by $F(x,a)=s_a(x)=\sum_{i=1}^Na_is_i(x)\in E_x$. Then:
> - (i) $F$ is transverse to $0_E$; consequently $W:=F^{-1}(0_E)$ is an embedded submanifold of $M\times\mathbb R^N$ of dimension $m+N-r$.
> - (ii) For a fixed $a\in\mathbb R^N$, the parameter $a$ is a regular value of $\operatorname{pr}_2|_W\colon W\to\mathbb R^N$ if and only if $s_a$ is transverse to the zero section.
>
> **Hint:** In a trivialisation the principal part $\widehat F(x,a)=\sum a_i\sigma_i(x)$ has surjective $a$-derivative, so $0$ is a regular value; for (ii) chase which $\dot a$ lift into $\ker d\widehat F$.
>
> **Why needed:** It is the parametric-transversality core: it turns "$s_a$ transverse" into "$a$ regular value of one projection", the form on which Sard's theorem acts.
>
> > [!note]- Full proof
> > Throughout, $\dim(M\times\mathbb R^N)=m+N$ and $E$ has $\dim E=m+r$, so $0_E\subseteq E$ has codimension $r$.
> >
> > **Part (i) — $W$ is a submanifold of dimension $m+N-r$.** The claim is local over $M$: fix $x_0\in M$, a trivialising neighbourhood $U\ni x_0$ with $E|_U\cong U\times\mathbb R^r$, and write $\sigma_i\colon U\to\mathbb R^r$ for the principal part of $s_i$. In this trivialisation the zero section is $\{w=0\}$, and a point $(x,a)\in U\times\mathbb R^N$ lies in $W$ if and only if the principal part
> > $$\widehat F\colon U\times\mathbb R^N\to\mathbb R^r,\qquad \widehat F(x,a)=\sum_{i=1}^N a_i\,\sigma_i(x)$$
> > vanishes. We claim $0\in\mathbb R^r$ is a regular value of $\widehat F$. The differential at any $(x,a)$ acts on $(\dot x,\dot a)\in T_xU\times\mathbb R^N$ by
> > $$d\widehat F_{(x,a)}(\dot x,\dot a)=\underbrace{\Big(\textstyle\sum_i a_i\,d(\sigma_i)_x\Big)(\dot x)}_{\text{the }x\text{-derivative}}\;+\;\underbrace{\sum_i \dot a_i\,\sigma_i(x)}_{\text{the }a\text{-derivative}}\qquad\text{(product rule, }\widehat F\text{ linear in }a\text{)}.$$
> > Restricting to the $a$-directions ($\dot x=0$) gives the linear map $\dot a\mapsto\sum_i\dot a_i\sigma_i(x)$, whose image is the span of $\sigma_1(x),\dots,\sigma_N(x)$; by the spanning property of Lemma 2 (transported through the trivialisation, which is a fibrewise isomorphism) this span is all of $\mathbb R^r$. Hence $d\widehat F_{(x,a)}$ is surjective at every point of $U\times\mathbb R^N$, so in particular at every point of $\widehat F^{-1}(0)$; thus $0$ is a regular value. By the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] — if $y$ is a regular value of a smooth map $f\colon P\to Q$ between manifolds then $f^{-1}(y)$ is an embedded submanifold of $P$ with $\dim f^{-1}(y)=\dim P-\dim Q$ and $T_pf^{-1}(y)=\ker df_p$ — the set $W\cap(U\times\mathbb R^N)=\widehat F^{-1}(0)$ is an embedded submanifold of $U\times\mathbb R^N$ of dimension $(m+N)-r$, with tangent space $T_{(x,a)}W=\ker d\widehat F_{(x,a)}$. Because being an embedded submanifold is a local property and the local pieces are cut out consistently (the locus $F=0_E$ does not depend on the trivialisation, only the equation representing it does), $W$ is an embedded submanifold of $M\times\mathbb R^N$ of dimension $m+N-r$. This also shows $F\pitchfork 0_E$: surjectivity of the vertical part of $dF$ (the content of "$0$ regular for $\widehat F$") is transversality to the zero section by Lemma 1 applied to $F$ as a section of the pulled-back bundle over $M\times\mathbb R^N$.
> >
> > **Part (ii) — regular values are transverse parameters.** Fix $a$ and a point $(x,a)\in W$, so $x$ is a zero of $s_a$. Work in the trivialisation above; write
> > $$A:=d(\widehat{\sigma_a})_x=\sum_i a_i\,d(\sigma_i)_x\colon T_xM\to\mathbb R^r,\qquad B:=\Big(\dot a\mapsto\sum_i\dot a_i\,\sigma_i(x)\Big)\colon\mathbb R^N\to\mathbb R^r,$$
> > so that $d\widehat F_{(x,a)}(\dot x,\dot a)=A\dot x+B\dot a$, and $A=D_xs_a$ by the coordinate formula of Lemma 1 (recall $x$ is a zero, so the vertical derivative is $d(\widehat{\sigma_a})_x$). Note $B$ is surjective by Lemma 2.
> >
> > The differential of the projection $p:=\operatorname{pr}_2|_W$ at $(x,a)$ is the restriction of $(\dot x,\dot a)\mapsto\dot a$ to $T_{(x,a)}W=\ker d\widehat F_{(x,a)}=\{(\dot x,\dot a):A\dot x+B\dot a=0\}$. Thus $dp_{(x,a)}$ is surjective if and only if
> > $$\text{for every }\dot a\in\mathbb R^N\ \text{there is }\dot x\in T_xM\ \text{with }A\dot x+B\dot a=0,$$
> > that is, if and only if $\operatorname{im}B\subseteq\operatorname{im}A$ (for each $\dot a$ we need $-B\dot a\in\operatorname{im}A$). Since $B$ is surjective, $\operatorname{im}B=\mathbb R^r$, so this reads $\mathbb R^r\subseteq\operatorname{im}A$, i.e. $A=D_xs_a$ is surjective. Therefore:
> > $$dp_{(x,a)}\text{ surjective}\iff D_xs_a\text{ surjective}.$$
> > Now $a$ is a regular value of $p$ if and only if $dp_{(x,a)}$ is surjective at **every** $(x,a)\in W$ with this second coordinate $a$ — equivalently at every zero $x$ of $s_a$ — which by the displayed equivalence holds if and only if $D_xs_a$ is surjective at every zero of $s_a$, which by Lemma 1 is exactly $s_a\pitchfork 0_E$. (If $s_a$ has no zeros, then no $(x,a)\in W$ has that second coordinate, so $a$ is vacuously a regular value and $s_a$ is vacuously transverse; the equivalence still holds.) $\blacksquare$

> [!note]- Lemma 4: Transversality to the zero section is stable near a compact set
> **Statement:** Let $L\subseteq M$ be compact and let $s\in\Gamma(E)$ be transverse to the zero section on an open neighbourhood of $L$. Then there is a $\delta>0$ and a finite family of trivialisations covering $L$ such that: any section $s'\in\Gamma(E)$ whose principal parts satisfy $\sup_L\big(\lVert\widehat{s'}-\widehat{s}\rVert+\lVert d\widehat{s'}-d\widehat{s}\rVert\big)<\delta$ (measured in those trivialisations) has the property that every zero of $s'$ lying in $L$ is transverse, that is, $D_xs'$ is surjective there.
>
> **Hint:** Argue by contradiction: a sequence of bad sections with bad zeros in $L$ has a convergent subsequence of zeros; pass to the limit and use that the non-surjective linear maps form a closed set.
>
> **Why needed:** It is the device that makes the relative version (d) succeed across the collar of the cutoff, where a naive perturbation would spoil transversality.
>
> > [!note]- Full proof
> > **Step 0 — set-up.** Since $s\pitchfork 0_E$ on an open set $\Omega\supseteq L$ and $L$ is compact, cover $L$ by finitely many trivialising open sets $U_1,\dots,U_p$ with $\overline{U_\alpha}\subseteq\Omega$ compact; fix trivialisations over each and let $\widehat{s}$ denote the corresponding principal parts. For a section $t\in\Gamma(E)$ write $\lVert t\rVert_{C^1,L}:=\sup_{L}\big(\lVert\widehat{t}\rVert+\lVert d\widehat{t}\rVert\big)$ using these charts (finite because $L$ is compact and covered by the $U_\alpha$); this is a norm on the relevant restrictions, and different admissible choices are comparable on the compact $L$.
> >
> > **Step 1 — contradiction hypothesis.** Suppose the conclusion fails. Then for every $n\in\mathbb N$ there is a section $s^{(n)}$ with $\lVert s^{(n)}-s\rVert_{C^1,L}<1/n$ and a zero $x_n\in L$ of $s^{(n)}$ (so $s^{(n)}(x_n)=0_{x_n}$) at which $D_{x_n}s^{(n)}$ is **not** surjective.
> >
> > **Step 2 — extract a limit zero.** Since $L$ is compact, after passing to a subsequence we may assume $x_n\to x_*\in L$. Choose $\alpha$ with $x_*\in U_\alpha$; for $n$ large, $x_n\in U_\alpha$ as well, so we may compute in the fixed trivialisation over $U_\alpha$. Write $\widehat{s}$ and $\widehat{s^{(n)}}$ for the principal parts there. From $\lVert s^{(n)}-s\rVert_{C^1,L}\to0$ we have $\widehat{s^{(n)}}\to\widehat{s}$ and $d\widehat{s^{(n)}}\to d\widehat{s}$ uniformly on $\overline{U_\alpha}\cap L$. Because $\widehat{s^{(n)}}(x_n)=0$,
> > $$\lVert\widehat{s}(x_*)\rVert\le\lVert\widehat{s}(x_*)-\widehat{s}(x_n)\rVert+\lVert\widehat{s}(x_n)-\widehat{s^{(n)}}(x_n)\rVert+\underbrace{\lVert\widehat{s^{(n)}}(x_n)\rVert}_{=0}\longrightarrow0$$
> > (the first term by continuity of $\widehat{s}$ and $x_n\to x_*$, the second by uniform convergence), so $\widehat{s}(x_*)=0$: the point $x_*$ is a zero of $s$.
> >
> > **Step 3 — pass the rank condition to the limit.** At the zero $x_n$ of $s^{(n)}$ the vertical derivative is $D_{x_n}s^{(n)}=d(\widehat{s^{(n)}})_{x_n}$ (coordinate formula, Lemma 1), and by hypothesis this $r\times m$ matrix has rank $<r$. Now
> > $$d(\widehat{s^{(n)}})_{x_n}\longrightarrow d(\widehat{s})_{x_*}\qquad(n\to\infty),$$
> > because $d\widehat{s^{(n)}}\to d\widehat{s}$ uniformly and $x_n\to x_*$ with $d\widehat{s}$ continuous. The set of $r\times m$ matrices of rank $<r$ (equivalently, non-surjective linear maps $\mathbb R^m\to\mathbb R^r$) is closed, being the common zero locus of all $r\times r$ minors, each a continuous function of the entries. A limit of such matrices is therefore again of rank $<r$, so $d(\widehat{s})_{x_*}=D_{x_*}s$ is not surjective.
> >
> > **Step 4 — the contradiction.** But $x_*\in L\subseteq\Omega$ is a zero of $s$, and $s\pitchfork 0_E$ on $\Omega$, so $D_{x_*}s$ **is** surjective (Lemma 1). This contradicts Step 3. Hence the contradiction hypothesis is impossible: there exist $\delta>0$ and the finite family of trivialisations as claimed, for which every $C^1$-$\delta$-close section has all its zeros in $L$ transverse. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $E\to M$ be a real vector bundle of rank $r$ over a compact $m$-manifold $M$.
>
> **Part (a) — finite spanning family.** This is exactly Lemma 2: there exist $s_1,\dots,s_N\in\Gamma(E)$ spanning every fibre. Fix such a family for the remainder.
>
> **Part (b) — genericity, assuming $r\ge m$.** Form the parametric map $F(x,a)=s_a(x)$ of Lemma 3. By Lemma 3(i), $W:=F^{-1}(0_E)$ is an embedded submanifold of $M\times\mathbb R^N$ of dimension
> $$\dim W=m+N-r.$$
> Consider the smooth projection $p:=\operatorname{pr}_2|_W\colon W\to\mathbb R^N$. Its source dimension is $\dim W=m+N-r$ and its target dimension is $N$; the hypothesis $r\ge m$ gives $m-r\le0$, hence
> $$\dim W=N+(m-r)\le N.$$
> The source dimension does not exceed the target dimension, so the [[Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension|restricted Sard theorem]] applies — for a smooth map $f\colon P^p\to Q^q$ with $p\le q$, the set of critical values of $f$ has measure zero in $Q$; note $W$ is second countable (a submanifold of the second-countable $M\times\mathbb R^N$), so the countable-chart argument behind the theorem needs no compactness of the source. Therefore the set of critical values of $p$ has Lebesgue measure zero in $\mathbb R^N$, i.e. the regular values of $p$ form a set of full measure. By Lemma 3(ii), $a$ is a regular value of $p$ if and only if $s_a\pitchfork 0_E$. Combining, for almost every $a\in\mathbb R^N$ the section $s_a$ is transverse to the zero section. This proves (b).
>
> **Part (c) — consequences, assuming $r\ge m$ and $s_a\pitchfork 0_E$.**
>
> *Case $r>m$.* Suppose $s_a$ had a zero $x$. By transversality (Lemma 1) $D_xs_a\colon T_xM\to E_x$ would be surjective; but $\dim T_xM=m<r=\dim E_x$, and no linear map from an $m$-dimensional space onto an $r$-dimensional space exists when $m<r$. This contradiction shows $s_a$ has no zeros, i.e. $s_a$ is nowhere vanishing. Since almost every $a$ gives such a section (by (b), applied in the subcase $r>m$; concretely $\dim W=m+N-r<N$, so the restricted Sard theorem gives that the image $p(W)$ has measure zero and almost every $a\notin p(W)$, meaning $Z(s_a)=\varnothing$), the bundle $E$ admits a nowhere-vanishing section.
>
> *Case $r=m$.* Let $x$ be a zero of $s_a$. By transversality $D_xs_a\colon T_xM\to E_x$ is surjective, and since $\dim T_xM=m=r=\dim E_x$ a surjective linear map between spaces of equal dimension is an isomorphism; thus every zero is nondegenerate. We show the zeros are isolated. In a trivialisation near $x$ the principal part $\widehat{s_a}\colon U\to\mathbb R^m$ has $d(\widehat{s_a})_x=D_xs_a$ invertible, so by the [[Thm - The Inverse Function Theorem|inverse function theorem]] — a smooth map $\mathbb R^m\to\mathbb R^m$ whose differential at a point is invertible restricts to a diffeomorphism of a neighbourhood of that point onto a neighbourhood of its image — $\widehat{s_a}$ is a diffeomorphism from some open $V\ni x$ onto an open neighbourhood of $0\in\mathbb R^m$. A diffeomorphism is injective, so $x$ is the only point of $V$ with $\widehat{s_a}=0$; hence $x$ is an isolated zero. Thus $Z(s_a)$ is a discrete subset of $M$. It is also closed (the preimage of the closed submanifold $0_E$ under the continuous $s_a$), hence compact (closed in the compact $M$); a compact discrete set is finite. So $s_a$ has finitely many zeros, each nondegenerate.
>
> *The sign, when $M$ and $E$ are oriented.* At a zero $x$, choose a positively oriented basis $(v_1,\dots,v_m)$ of $T_xM$ and a positively oriented basis $(f_1,\dots,f_m)$ of $E_x$; the isomorphism $D_xs_a$ has a matrix in these bases, and we set $\epsilon(x)=\operatorname{sign}\det D_xs_a$. This is independent of the chosen positively oriented bases: replacing $(v_j)$ by another positively oriented basis multiplies the matrix on the right by a matrix of positive determinant, and replacing $(f_j)$ by another positively oriented basis multiplies it on the left by a matrix of positive determinant, so the sign of the determinant is unchanged. Hence $\epsilon(x)\in\{+1,-1\}$ is well defined. This proves (c).
>
> **Part (d) — relative version, assuming $r\ge m$.** Let $K\subseteq M$ be closed and $s\in\Gamma(E)$ transverse to the zero section on an open neighbourhood $\Omega\supseteq K$; let $\varepsilon>0$ and fix a smooth fibre metric on $E$ (built by a [[Thm - Existence of Smooth Partitions of Unity|partition of unity]] from local Euclidean structures), which supplies the norm $\lVert\cdot\rVert$.
>
> **Step 0 — nested neighbourhoods and a cutoff.** Choose open sets with
> $$K\subseteq V\subseteq\overline V\subseteq U_0\subseteq\overline{U_0}\subseteq\Omega,\qquad \overline{U_0}\ \text{compact},$$
> possible because $M$ is compact and $\Omega$ is open. By a partition of unity (equivalently a bump function, [[Thm - Existence of Smooth Bump Functions]]) choose $\rho\in C^\infty(M)$ with $0\le\rho\le1$, $\rho\equiv0$ on $\overline V$, and $\rho\equiv1$ on $M\setminus U_0$. Let $s_1,\dots,s_N$ be the spanning family of (a), and define the family
> $$s'_a:=s+\rho\sum_{i=1}^N a_is_i\in\Gamma(E),\qquad a\in\mathbb R^N.$$
> For every $a$, $s'_a=s$ on $\overline V\supseteq K$ (since $\rho=0$ there); this secures the "$s'=s$ near $K$" clause.
>
> **Step 1 — stability on the compact collar.** Apply Lemma 4 with $L:=\overline{U_0}$, compact and contained in $\Omega$ where $s\pitchfork 0_E$; it yields $\delta>0$ and a finite trivialising cover of $\overline{U_0}$ such that any section $C^1$-$\delta$-close to $s$ on $\overline{U_0}$ has every zero in $\overline{U_0}$ transverse. The difference $s'_a-s=\rho\sum_ia_is_i$ is, on the compact $\overline{U_0}$, bounded in the relevant $C^1$-norm by $C\lVert a\rVert$ for a constant $C$ depending only on $\rho$, the $s_i$, and the fixed charts (all smooth data on a compact set). Hence there is $\delta_1:=\delta/C>0$ such that for $\lVert a\rVert<\delta_1$ every zero of $s'_a$ in $\overline{U_0}$ is transverse.
>
> **Step 2 — parametric transversality off the collar.** On the open set $\Omega':=\{\rho>0\}=M\setminus\overline V$, the parameter derivative of the total map $(x,a)\mapsto s'_a(x)$ in the $a$-directions is $\dot a\mapsto\rho(x)\sum_i\dot a_is_i(x)$, which for $\rho(x)>0$ has image the span of $s_1(x),\dots,s_N(x)$, all of $E_x$ by (a). Thus the argument of Lemma 3, run over $\Omega'$ in place of $M$ with the shifted family $s'_a=s+\rho\,s_a$, shows: the parametric zero set $W':=\{(x,a)\in\Omega'\times\mathbb R^N:s'_a(x)=0_x\}$ is a submanifold of dimension $m+N-r\le N$, and $a$ is a regular value of $\operatorname{pr}_2|_{W'}$ if and only if every zero of $s'_a$ lying in $\Omega'$ is transverse. By the [[Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension|restricted Sard theorem]] (again $\dim W'\le N$ since $r\ge m$), the set $B\subseteq\mathbb R^N$ of parameters for which some zero of $s'_a$ in $\Omega'$ is non-transverse has measure zero.
>
> **Step 3 — choose the parameter and conclude.** The open ball $\{\lVert a\rVert<\delta_1\}$ has positive measure, so it is not contained in the measure-zero set $B$; pick $a$ with $\lVert a\rVert<\delta_1$ and $a\notin B$. For this $a$:
> - every zero of $s'_a$ in $\overline{U_0}$ is transverse (Step 1, as $\lVert a\rVert<\delta_1$);
> - every zero of $s'_a$ in $\Omega'=M\setminus\overline V$ is transverse (Step 2, as $a\notin B$).
> Since $M=\overline{U_0}\cup(M\setminus\overline V)$ — indeed $\overline V\subseteq U_0\subseteq\overline{U_0}$, so $M\setminus\overline{U_0}\subseteq M\setminus\overline V$ — every point of $M$, and in particular every zero of $s'_a$, lies in $\overline{U_0}$ or in $M\setminus\overline V$; in either case that zero is transverse. Therefore $s'_a\pitchfork 0_E$ on all of $M$. Finally, shrinking the choice if necessary so that $\lVert a\rVert$ is small enough that $\sup_M\lVert s'_a-s\rVert=\sup_M\big\lVert\rho\sum_ia_is_i\big\rVert\le\big(\sup_M\sum_i\lVert s_i\rVert\big)\lVert a\rVert_1<\varepsilon$, we obtain a section $s':=s'_a$ with all three required properties: $s'=s$ near $K$, $s'\pitchfork 0_E$ everywhere, and $\sup_M\lVert s'-s\rVert<\varepsilon$. This proves (d). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Vector fields and the Euler characteristic (differential topology).** Take $E=TM$ for a closed manifold $M$, so $r=m$. The theorem produces a vector field with finitely many nondegenerate zeros, each carrying a sign $\epsilon(x)=\operatorname{sign}\det D_xv$. The Poincaré–Hopf theorem asserts that $\sum_x\epsilon(x)=\chi(M)$ is independent of the generic field. Applying the present theorem is the necessary first step — it guarantees such a field exists at all — and the exercise is to run the construction on a specific surface (say the genus-two surface as a quotient of an octagon) and verify that the count is $2-2g$. The application is non-obvious because "generic vector field" is exactly a generic section, a fact obscured when one thinks of vector fields as a special species.

**Intersection numbers via defining sections (algebraic topology).** Let $Z\subseteq N$ be a closed submanifold of codimension $r$ in a compact manifold $N$, with a tubular neighbourhood whose normal bundle is $\nu\to Z$. A smooth map $f\colon M\to N$ can be pushed to be transverse to $Z$; near $Z$ the composite with the projection to the fibre of $\nu$ realises the transversality as transversality of a section of $f^*\nu$ to its zero section. The exercise is to phrase the transverse-preimage count $\#(f^{-1}(Z))$ with signs as the signed zero count of a generic section, and thereby see the intersection number as an instance of the theorem. This is non-obvious because it converts a statement about two submanifolds meeting into a statement about one section meeting a zero section.

**Genericity of Morse functions' gradients (dynamical systems).** For a Riemannian manifold $(M,g)$ and $f\in C^\infty(M)$, the gradient $\nabla f$ is a section of $TM$; its zeros are the critical points of $f$, and nondegeneracy of the zero (in the sense of this theorem, $D_x\nabla f$ invertible) is exactly nondegeneracy of the Hessian, i.e. $f$ being Morse at $x$. The exercise is to deduce, from the transversality theorem applied to $E=TM$, that a generic small perturbation of any function has only nondegenerate critical points. The subtlety is that the perturbations here should be of the function, not of an arbitrary section, so one restricts the family to gradients — a genuinely different parametrisation that the reader must check still fills the fibre directions.

---

# Bridges

- **[[Thm - Sard's Theorem when the Source Dimension does not Exceed the Target Dimension|Restricted Sard theorem]]** — the engine. The entire genericity statement (b) is the assertion that a certain projection $\operatorname{pr}_2|_W\colon W\to\mathbb R^N$ has almost every value regular; this is Sard's theorem, and the hypothesis $r\ge m$ is precisely what keeps $\dim W\le N$ so that the restricted (source-dimension-at-most-target) version suffices. The general case $r<m$ would call on the full Sard theorem of chapter X.

- **[[Thm - Regular Value Theorem on Manifolds|Regular value theorem]]** — supplies the submanifold. That the parametric zero set $W=F^{-1}(0_E)$ is a manifold at all comes from $0$ being a regular value of the principal part $\widehat F$; the parameter directions of $F$, made surjective by the spanning family, are what force regularity.

- **[[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|Classification of $SU(2)$-bundles]]** — the flagship consumer. In dimension at most three the corollary $r>m$ (with $E=P\times_{SU(2)}\mathbb C^2$ of rank four) gives a nowhere-vanishing section, hence triviality; in dimension four the corollary $r=m$ gives finitely many zeros, which the homogeneity lemma gathers into one disc so that clutching applies. Both directions of that classification quote this page directly.

- **[[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|Classification of line bundles over surfaces]]** — the rank-two consumer. A complex line bundle over a closed surface is an oriented real rank-two bundle with $r=m=2$; its generic section's signed zero count is the degree, and the relative version (d) is what lets one arrange the section to be a fixed nonzero constant outside a disc, ready for the winding-number computation.

- **[[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf]] and [[Def - Brouwer Degree of a Map|the Brouwer degree]]** — the historical companions. The signed count of nondegenerate zeros in the case $E=TM$ is the local index whose sum is the Euler characteristic; the same signed-counting principle, transported to maps between spheres, is the Brouwer degree. This theorem is the existence statement that both invariants presuppose: without a generic section (or map) there is nothing to count.

---

# Unlocked by This

> [!tip] Nowhere-vanishing sections from a rank bound *(from Differential Topology)*
> Whenever a real vector bundle over a compact manifold has rank strictly greater than the base dimension, it has a nowhere-vanishing section — a purely numerical criterion, with no computation of characteristic classes required. This is the quickest route to triviality statements in low dimensions and the reason the tangent bundle of an odd sphere, and every high-rank associated bundle over a low-dimensional base, splits off a trivial line.

> [!tip] Signed zero counts as stable invariants *(from Algebraic Topology)*
> In the balanced case $r=m$, the finite set of signed zeros of a generic section is the raw material of an integer invariant — the Euler number of the bundle — whose stability under change of generic section is proved later by a cobordism between zero sets. This page is where that raw material is first shown to exist and to be finite.
