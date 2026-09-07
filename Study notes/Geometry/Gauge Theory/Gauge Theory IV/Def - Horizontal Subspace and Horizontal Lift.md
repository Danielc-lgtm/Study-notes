---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection on a Principal Bundle"
  - "Def - Principal G-Bundle"
  - "Def - Fundamental Vector Field of a Group Action"
  - "Def - Distribution on a Manifold"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a smooth **[[Def - Principal G-Bundle|principal G-bundle]]** over a smooth manifold $M$, with $G$ a Lie group acting on $P$ smoothly, freely, and on the **right**: $R_g(p)=p\cdot g$. We write $\mathfrak g=T_eG$ for the Lie algebra, $x=\pi(p)$ for the image of a point, and $P_x=\pi^{-1}(x)$ for the fibre over $x$. The dimensions are related by $\dim P=\dim M+\dim G$, because a principal bundle is locally $U\times G$ over the base.

For $\xi\in\mathfrak g$ the **[[Def - Fundamental Vector Field of a Group Action|fundamental vector field]]** is
$$\xi_P(p):=\frac{d}{dt}\Big|_{t=0}\,p\cdot\exp(t\xi)\in T_pP,$$
the velocity of the orbit through $p$ in the direction $\xi$. Because the action is free, at each $p$ the linear map $\xi\mapsto\xi_P(p)$ is injective, and its image is the **vertical subspace**
$$V_pP:=\ker(d\pi_p)=\{\xi_P(p):\xi\in\mathfrak g\}=T_p(P_x),$$
the tangent space to the fibre. Since $\dim V_pP=\dim\mathfrak g=\dim G$, the map $\xi\mapsto\xi_P(p)$ is a linear isomorphism $\mathfrak g\xrightarrow{\ \sim\ }V_pP$: every vector tangent to a fibre is $\xi_P(p)$ for exactly one $\xi\in\mathfrak g$. A tangent vector $v\in T_pP$ is called **vertical** if $v\in V_pP$, equivalently $d\pi_p(v)=0$. The projection is fibre-preserving, $\pi\circ R_g=\pi$, and right translation $R_g\colon P\to P$ is a diffeomorphism, so $dR_g$ is a linear isomorphism at every point.

A **[[Def - Connection on a Principal Bundle|connection 1-form]]** on $P$ is a $\mathfrak g$-valued $1$-form $\omega\in\Omega^1(P;\mathfrak g)$ satisfying the two axioms

> [!note] Recall — the connection axioms
> A form $\omega\in\Omega^1(P;\mathfrak g)$ is a **connection $1$-form** if and only if
> 1. **($\operatorname{Ad}$-equivariance)** $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$ for all $g\in G$, that is $\omega_{p\cdot g}(dR_g\,v)=\operatorname{Ad}_{g^{-1}}\big(\omega_p(v)\big)$ for every $v\in T_pP$;
> 2. **(normalisation)** $\omega(\xi_P)=\xi$ for all $\xi\in\mathfrak g$, that is $\omega_p(\xi_P(p))=\xi$.
>
> Axiom (2) forces $\omega_p|_{V_pP}\colon V_pP\to\mathfrak g$ to be the inverse of the fundamental-field isomorphism $\xi\mapsto\xi_P(p)$; this fact is used at almost every step below. The full page is [[Def - Connection on a Principal Bundle]].

The notation of this page is $H_p$ for the horizontal subspace, $\pi_H$ and $\pi_V$ for the horizontal and vertical projections, $\tilde v$ for the horizontal lift of a vector $v$, and $\tilde X$ for the horizontal lift of a vector field $X$. The symbol $\operatorname{Ad}_g$ is always the group adjoint $d_e(a\mapsto gag^{-1})$; for matrix groups $\operatorname{Ad}_gX=gXg^{-1}$.

> [!note] This is a compound page
> It defines five interlocking notions — the horizontal subspace $H_p$, the horizontal and vertical projections $\pi_H,\pi_V$, the horizontal lift $\tilde v$ of a tangent vector, the horizontal lift $\tilde X$ of a vector field, and the horizontal lift of a curve — because they are one geometric idea seen from five angles: a connection form splits every tangent space into a horizontal and a vertical piece, and everything else is the bookkeeping of that single splitting. The corollaries of Bär's Theorem 2.3.4 (the splitting is direct, is $G$-invariant, and projects isomorphically to the base) are proved on the page, and so is the bracket identity $[\tilde X,\tilde Y]-\widetilde{[X,Y]}\in VP$ that foreshadows curvature.

---

# Axiom Motivation

A connection form $\omega$ is, by axiom (2), a device that reads off the vertical part of a tangent vector as an element of $\mathfrak g$. The vertical directions were never the problem: the fundamental-field isomorphism $\xi\mapsto\xi_P(p)$ already identifies $V_pP$ with the fixed vector space $\mathfrak g$, canonically and at every point. What a connection *adds* is the missing half of the picture — a notion of which tangent vectors point "horizontally", transverse to the fibre, so that a motion in the base can be lifted to a canonical motion upstairs. The horizontal subspace is the object that carries exactly this added information, and the definition that follows is the only one that could.

The desideratum is a rule assigning to each $p\in P$ a linear complement $H_p$ to $V_pP$ inside $T_pP$, so that $T_pP=H_p\oplus V_pP$ and every tangent vector splits uniquely into a horizontal and a vertical part. We want three further things of this complement, each of which turns out to be automatic once the definition is made correctly. First, $H_p$ should vary smoothly with $p$, so that lifting is a smooth operation. Second, the family $\{H_p\}$ should respect the group action, $dR_g(H_p)=H_{p\cdot g}$, so that the horizontal lift of a base vector does not depend on which point of the fibre we lift it to in an inconsistent way — this is what will let the local data descend to the base. Third, $H_p$ should project isomorphically onto $T_xM$ under $d\pi_p$, so that each base vector has exactly one horizontal lift at each $p$.

There is exactly one candidate that meets these desiderata and requires no new choice beyond $\omega$ itself: the kernel of $\omega_p$. The reason is that $\omega_p$ is, by construction, the linear map that returns the vertical part; a vector is "purely horizontal" precisely when it has no vertical part, that is when $\omega_p(v)=0$. So we are not free to *invent* the horizontal subspace once $\omega$ is fixed — it is forced to be $H_p=\ker\omega_p$, and the three desiderata are then theorems (proved in the Examples/Corollaries section), not additional axioms.

What would break if we tried to define horizontality by some other rule? Two failures are instructive. If we dropped the normalisation axiom (2) from $\omega$ — say $\omega=0$ — then "$\ker\omega_p$" would be all of $T_pP$, which is not a complement to $V_pP$ and defines no horizontal directions at all; the normalisation is exactly what guarantees $\omega_p$ restricts to an isomorphism on $V_pP$ and hence that its kernel is a genuine complement of the correct dimension $\dim M$. If we dropped the equivariance axiom (1) we could still form $\ker\omega_p$ and get a smooth complement, but the family $\{H_p\}$ would fail $dR_g(H_p)=H_{p\cdot g}$; the horizontal lift would then depend on the point in the fibre in a way the group could not correct, parallel transport around the fibre would be inconsistent, and — the decisive consequence — the curvature would not descend to a form on $M$. Each clause of the connection axioms is therefore visible here as a property the horizontal splitting must have; a reader who has understood why a connection is a vertical-part operator can reconstruct the definition $H_p:=\ker\omega_p$ and predict every corollary below.

---

# The Definition

Let $\pi\colon P\to M$ be a principal $G$-bundle with a connection $1$-form $\omega\in\Omega^1(P;\mathfrak g)$.

**Horizontal subspace.** For $p\in P$, the **horizontal subspace** at $p$ is the kernel of $\omega_p$,
$$H_p:=\ker\omega_p=\{v\in T_pP:\omega_p(v)=0\}\subset T_pP.$$
The family $H=\{H_p\}_{p\in P}$ is the **horizontal distribution**; it is a smooth rank-$(\dim M)$ [[Def - Distribution on a Manifold|distribution]] on $P$, as the corollaries below establish. A tangent vector $v$ is called **horizontal** if $v\in H_p$.

**Horizontal and vertical projections.** By the direct-sum corollary $T_pP=H_p\oplus V_pP$ proved below, every $v\in T_pP$ decomposes uniquely as $v=v_H+v_V$ with $v_H\in H_p$ and $v_V\in V_pP$. The two components are given in closed form by the connection: the vertical part is the fundamental field of $\omega_p(v)$, and the horizontal part is what remains,
$$\pi_V(v):=\big(\omega_p(v)\big)_P(p)\in V_pP,\qquad \pi_H(v):=v-\big(\omega_p(v)\big)_P(p)\in H_p.$$
These are the **vertical projection** $\pi_V\colon T_pP\to V_pP$ and the **horizontal projection** $\pi_H\colon T_pP\to H_p$; they are complementary linear projections, $\pi_H+\pi_V=\operatorname{id}$, $\pi_H^2=\pi_H$, $\pi_V^2=\pi_V$, and they depend smoothly on $p$ because $\omega$ is smooth and $\zeta\mapsto\zeta_P$ carries smooth $\mathfrak g$-valued functions to smooth vector fields.

**Horizontal lift of a tangent vector.** For $x=\pi(p)$ and a tangent vector $v\in T_xM$, the **horizontal lift** of $v$ to $p$ is the unique horizontal vector $\tilde v\in H_p$ with $d\pi_p(\tilde v)=v$,
$$\tilde v:=\big(d\pi_p|_{H_p}\big)^{-1}(v)\in H_p,$$
which exists and is unique because $d\pi_p|_{H_p}\colon H_p\to T_xM$ is an isomorphism (corollary below). When the point $p$ must be named we write $\tilde v^{\,p}$; otherwise $p$ is understood from context.

**Horizontal lift of a vector field.** For a vector field $X\in\Gamma(TM)$ on the base, the **horizontal lift** $\tilde X\in\Gamma(TP)$ is the vector field on the total space whose value at $p$ is the horizontal lift of $X_{\pi(p)}$ to $p$,
$$\tilde X(p):=\widetilde{X_{\pi(p)}}\in H_p,\qquad\text{so}\qquad \tilde X(p)\in H_p\quad\text{and}\quad d\pi_p\big(\tilde X(p)\big)=X_{\pi(p)}.$$
Equivalently, $\tilde X$ is the unique **horizontal** vector field on $P$ that is **[[Def - F-Related Vector Fields|π-related]]** to $X$. Its smoothness and this uniqueness are proved below.

**Horizontal lift of a curve.** For a smooth curve $c\colon[a,b]\to M$ and a point $p_0\in\pi^{-1}(c(a))$, a **horizontal lift** of $c$ through $p_0$ is a smooth curve $\tilde c\colon[a,b]\to P$ with
$$\pi\circ\tilde c=c,\qquad \tilde c(a)=p_0,\qquad \dot{\tilde c}(t)\in H_{\tilde c(t)}\ \text{ for all }t,$$
the last condition being $\omega\big(\dot{\tilde c}(t)\big)=0$. Here we record only the definition; the existence and uniqueness of the horizontal lift of a curve is the parallel-transport theorem, proved in **Gauge Theory V** (it is a first-order ordinary differential equation for the fibre coordinate, solved by the flow of the horizontal lift of $\dot c$).

---

# Categorical / Structural Definition

The horizontal distribution is the image of a **$G$-equivariant splitting** of a short exact sequence of vector bundles over $P$. The differential of $\pi$ and the fundamental-field map assemble into the exact sequence
$$0\longrightarrow VP\longrightarrow TP\xrightarrow{\ d\pi\ }\pi^*TM\longrightarrow 0,$$
where $VP=\ker d\pi$ is the vertical bundle and $\pi^*TM$ is the pullback of $TM$, whose fibre at $p$ is $T_{\pi(p)}M$. A connection is exactly a splitting of this sequence — a bundle map $\sigma\colon\pi^*TM\to TP$ with $d\pi\circ\sigma=\operatorname{id}$ — that is invariant under the group, $dR_g\circ\sigma=\sigma\circ (\text{pullback of }dR_g)$. Given the connection form $\omega$, the splitting is the horizontal lift, $\sigma_p(v)=\tilde v$, and its image is the horizontal subspace, $\sigma_p(T_{\pi(p)}M)=H_p$. The projection $\pi_H\colon TP\to TP$ onto the image of $\sigma$ (with kernel $VP$) is the horizontal projection, and $\pi_V=\operatorname{id}-\pi_H$ recovers $\omega$ through $\omega_p(v)=\big((\text{fundamental-field iso})^{-1}\circ\pi_V\big)(v)$. In this language the equivalence "connection form $\leftrightarrow$ invariant horizontal distribution" is the statement that a $G$-equivariant splitting is the same datum as its image; it is proved in full on **[[Thm - Connection Forms Correspond to Invariant Horizontal Distributions]]**.

---

# Relate to Other Fields / Compression

The horizontal lift is the principal-bundle form of a single idea that recurs across geometry: *a connection is a rule for lifting motion in the base to motion in the total space, transverse to the fibres.* In the theory of a **[[Def - Connection on a Vector Bundle|vector-bundle connection]]** $\nabla$, the same idea appears as the covariant derivative: a section is "constant in the direction $X$" when $\nabla_X s=0$, and the horizontal lift of a curve on the frame bundle is exactly the moving frame that stays parallel. The precise dictionary — that the horizontal lift of a curve in $\operatorname{Fr}(E)$ is the frame whose columns are parallel — is one of the identifications proved in §4.4 and made fully explicit on the frame-bundle correspondence theorem. In Riemannian geometry, the horizontal lift of the Levi-Civita connection on the orthonormal frame bundle is the construction behind the development of curves and the rolling-without-slipping picture of parallel transport.

**True name.** Operationally, the horizontal subspace is *the graph, over the base directions, of the choice of how to move without changing the internal (gauge) coordinate.* Fix a local trivialisation $P|_U\cong U\times G$ with connection potential $A\in\Omega^1(U;\mathfrak g)$ (the local form $s^*\omega$ of a section $s$). In these coordinates a tangent vector at $(x,g)$ is a pair $(v,w)\in T_xU\oplus T_gG$, and one computes $\omega_{(x,g)}(v,w)=\operatorname{Ad}_{g^{-1}}\big(A_x(v)\big)+\theta_g(w)$, where $\theta$ is the [[Def - The Maurer-Cartan Form|Maurer–Cartan form]]. The horizontal condition $\omega=0$ then reads $w=-dL_g\big(\operatorname{Ad}_{g^{-1}}A_x(v)\big)$, exhibiting $H_{(x,g)}$ as the graph $\{(v,w(v)):v\in T_xU\}$ of a linear map $T_xU\to T_gG$. So "horizontal" is not "no motion in $G$"; it is "the specific motion in $G$ dictated by the potential $A$ as one moves in the base." This is the sense in which a connection is a rule, and the potential $A$ is that rule written in a gauge.

---

# Examples / Corollaries

We first prove, at full rigour, the five structural corollaries of the definition — these are Bär's Theorem 2.3.4 — then the properties of the horizontal lift of a vector field, then the bracket identity that foreshadows curvature, and finally an example and a non-example. Every claim is verified on the page.

> [!note]- Corollary 1: $\omega_p|_{V_pP}\colon V_pP\to\mathfrak g$ is a linear isomorphism.
> **Claim.** The restriction of $\omega_p$ to the vertical subspace $V_pP$ is a linear isomorphism onto $\mathfrak g$.
>
> **Proof.** We must show $\omega_p|_{V_pP}$ is linear, injective, and surjective. Linearity is inherited from $\omega_p$, which is a linear map $T_pP\to\mathfrak g$. **Identify the vertical subspace via fundamental fields.** By the fundamental-field isomorphism recalled in the Notation, every $v\in V_pP$ is $v=\xi_P(p)$ for a unique $\xi\in\mathfrak g$, and the map $\Phi_p\colon\mathfrak g\to V_pP$, $\Phi_p(\xi)=\xi_P(p)$, is a linear isomorphism (injective because the action is free, surjective onto $V_pP$ by definition of $V_pP$, and of matching dimension $\dim\mathfrak g=\dim V_pP$). **Compose with $\omega_p$.** For any $\xi\in\mathfrak g$,
> $$\big(\omega_p|_{V_pP}\circ\Phi_p\big)(\xi)=\omega_p\big(\xi_P(p)\big)=\xi\qquad\text{(by the normalisation axiom (2)).}$$
> Thus $\omega_p|_{V_pP}\circ\Phi_p=\operatorname{id}_{\mathfrak g}$. Since $\Phi_p$ is an isomorphism, $\omega_p|_{V_pP}=\Phi_p^{-1}$ is its inverse, hence itself a linear isomorphism $V_pP\to\mathfrak g$. **Conclusion.** $\omega_p|_{V_pP}$ is a linear isomorphism, and it is exactly the inverse of $\xi\mapsto\xi_P(p)$. $\blacksquare$

> [!note]- Corollary 2: $T_pP=H_p\oplus V_pP$ (the splitting is direct).
> **Claim.** For every $p\in P$, the tangent space decomposes as an internal direct sum $T_pP=H_p\oplus V_pP$ of the horizontal and vertical subspaces.
>
> **Proof.** We show $H_p\cap V_pP=\{0\}$ and $H_p+V_pP=T_pP$; together these are the definition of an internal direct sum. **Trivial intersection.** Let $v\in H_p\cap V_pP$. Then $\omega_p(v)=0$ because $v\in H_p=\ker\omega_p$, and $v\in V_pP$. But $\omega_p|_{V_pP}$ is injective (by Corollary 1), and it sends $v$ to $0=\omega_p(0)$; injectivity gives $v=0$. Hence $H_p\cap V_pP=\{0\}$. **Spanning.** Let $v\in T_pP$ be arbitrary and set $\xi:=\omega_p(v)\in\mathfrak g$. Define $v_V:=\xi_P(p)\in V_pP$ and $v_H:=v-v_V$. Then
> $$\omega_p(v_H)=\omega_p(v)-\omega_p\big(\xi_P(p)\big)=\xi-\xi=0\qquad\text{(by linearity of }\omega_p\text{ and the normalisation axiom (2)),}$$
> so $v_H\in\ker\omega_p=H_p$. Therefore $v=v_H+v_V$ with $v_H\in H_p$ and $v_V\in V_pP$, proving $H_p+V_pP=T_pP$. **Conclusion.** The intersection is trivial and the sum is everything, so $T_pP=H_p\oplus V_pP$. The decomposition $v=v_H+v_V$ constructed here is exactly $v=\pi_H(v)+\pi_V(v)$ of the definition, since $v_V=\big(\omega_p(v)\big)_P(p)=\pi_V(v)$. $\blacksquare$

> [!note]- Corollary 3: $\dim H_p=\dim M$, and $H$ is a smooth rank-$(\dim M)$ distribution.
> **Claim.** $\dim H_p=\dim M$ for every $p$, and the assignment $p\mapsto H_p$ is a smooth distribution on $P$.
>
> **Proof.** **Dimension count.** By Corollary 2 the sum $T_pP=H_p\oplus V_pP$ is direct, so
> $$\dim H_p=\dim T_pP-\dim V_pP=\dim P-\dim\mathfrak g\qquad\text{(direct-sum dimension formula; }\dim V_pP=\dim\mathfrak g\text{ by Corollary 1),}$$
> and since $\dim P=\dim M+\dim G=\dim M+\dim\mathfrak g$ (a principal bundle is locally $U\times G$), this equals $\dim H_p=\dim M$. **Smoothness.** The horizontal projection $\pi_H(v)=v-\big(\omega(v)\big)_P$ is a smooth bundle endomorphism of $TP$ of constant rank $\dim M$ (its image is $H_p$ at each point, of constant dimension just computed), because $\omega$ is a smooth $1$-form and $\zeta\mapsto\zeta_P$ is smooth. A constant-rank smooth bundle endomorphism has smooth image, so $H=\operatorname{im}\pi_H$ is a smooth subbundle of $TP$, that is a smooth distribution of rank $\dim M$ in the sense of [[Def - Distribution on a Manifold]]. **Conclusion.** $\dim H_p=\dim M$ and $H$ is a smooth rank-$(\dim M)$ distribution on $P$. $\blacksquare$

> [!note]- Corollary 4: $dR_g(H_p)=H_{p\cdot g}$ (the horizontal distribution is $G$-invariant).
> **Claim.** For all $p\in P$ and $g\in G$, the differential of right translation maps the horizontal subspace at $p$ isomorphically onto the horizontal subspace at $p\cdot g$.
>
> **Proof.** **Containment $dR_g(H_p)\subseteq H_{p\cdot g}$.** Let $v\in H_p$, so $\omega_p(v)=0$. Then
> $$\omega_{p\cdot g}\big(dR_g\,v\big)=\big(R_g^*\omega\big)_p(v)=\operatorname{Ad}_{g^{-1}}\big(\omega_p(v)\big)=\operatorname{Ad}_{g^{-1}}(0)=0\qquad\text{(definition of pullback; then }\operatorname{Ad}\text{-equivariance axiom (1); then }v\in\ker\omega_p\text{),}$$
> so $dR_g\,v\in\ker\omega_{p\cdot g}=H_{p\cdot g}$. This proves $dR_g(H_p)\subseteq H_{p\cdot g}$. **Upgrade to equality.** The map $dR_g\colon T_pP\to T_{p\cdot g}P$ is a linear isomorphism, because $R_g$ is a diffeomorphism of $P$. Its restriction $dR_g|_{H_p}\colon H_p\to H_{p\cdot g}$ is therefore injective, and by Corollary 3, $\dim H_p=\dim M=\dim H_{p\cdot g}$. An injective linear map between spaces of equal finite dimension is surjective, so $dR_g(H_p)=H_{p\cdot g}$. **Conclusion.** Right translation permutes the horizontal subspaces exactly as it permutes the points, $dR_g(H_p)=H_{p\cdot g}$; this is the $G$-invariance of the horizontal distribution. $\blacksquare$

> [!note]- Corollary 5: $d\pi_p|_{H_p}\colon H_p\to T_{\pi(p)}M$ is a linear isomorphism.
> **Claim.** The differential of $\pi$, restricted to the horizontal subspace, is a linear isomorphism onto the tangent space of the base.
>
> **Proof.** Write $x=\pi(p)$. **Injectivity.** Let $v\in H_p$ with $d\pi_p(v)=0$. Then $v\in\ker d\pi_p=V_pP$ (definition of the vertical subspace), so $v\in H_p\cap V_pP=\{0\}$ by Corollary 2, giving $v=0$. Hence $d\pi_p|_{H_p}$ is injective. **Dimension match and surjectivity.** By Corollary 3, $\dim H_p=\dim M=\dim T_xM$. An injective linear map between spaces of equal finite dimension is an isomorphism, so $d\pi_p|_{H_p}\colon H_p\to T_xM$ is bijective. (Equivalently: $\pi$ is a submersion, so $d\pi_p\colon T_pP\to T_xM$ is surjective with kernel $V_pP$; restricting to the complement $H_p$ of the kernel gives an isomorphism.) **Conclusion.** $d\pi_p|_{H_p}$ is a linear isomorphism $H_p\xrightarrow{\ \sim\ }T_xM$, which is precisely what makes the horizontal lift $\tilde v=(d\pi_p|_{H_p})^{-1}(v)$ well defined and unique. $\blacksquare$

With Corollary 5 in hand, the horizontal lift of a tangent vector is well defined. We now verify that the horizontal lift of a vector field is a genuine smooth vector field with the three properties listed in the definition.

> [!note]- Corollary 6: $\tilde X$ is a well-defined smooth vector field, and is the unique horizontal field $\pi$-related to $X$.
> **Claim.** For $X\in\Gamma(TM)$, the pointwise horizontal lift $\tilde X(p):=\widetilde{X_{\pi(p)}}$ is a smooth vector field on $P$; it is horizontal and $\pi$-related to $X$; and it is the only vector field on $P$ with these two properties.
>
> **Proof.** **Construct a smooth reference lift.** Because $\pi$ is a submersion, there is a smooth vector field $Y\in\Gamma(TP)$ with $d\pi_p(Y(p))=X_{\pi(p)}$ for all $p$ (a vector field $\pi$-related to $X$, not necessarily horizontal): in a local trivialisation $P|_U\cong U\times G$ take $Y=(X,0)$, and patch such local choices with a partition of unity subordinate to a trivialising cover; the patched field still satisfies $d\pi(Y)=X\circ\pi$ because $d\pi$ is linear and $\sum\rho_\alpha=1$. **Project to the horizontal.** Set $\tilde X:=\pi_H(Y)=Y-\big(\omega(Y)\big)_P$. This is smooth, because $Y$ is smooth, $\omega(Y)$ is a smooth $\mathfrak g$-valued function on $P$, and $\zeta\mapsto\zeta_P$ maps smooth $\mathfrak g$-valued functions to smooth vector fields. It is horizontal, $\omega(\tilde X)=\omega(Y)-\omega\big((\omega(Y))_P\big)=\omega(Y)-\omega(Y)=0$ (by the normalisation axiom (2) applied to the $\mathfrak g$-valued function $\omega(Y)$). And it is $\pi$-related to $X$:
> $$d\pi\big(\tilde X\big)=d\pi(Y)-d\pi\big((\omega(Y))_P\big)=X\circ\pi-0=X\circ\pi\qquad\text{(fundamental fields are vertical, }d\pi(\zeta_P)=0\text{).}$$
> **Match with the pointwise definition.** At each $p$, $\tilde X(p)$ is horizontal and satisfies $d\pi_p(\tilde X(p))=X_{\pi(p)}$, so $\tilde X(p)=(d\pi_p|_{H_p})^{-1}(X_{\pi(p)})=\widetilde{X_{\pi(p)}}$ by the uniqueness in Corollary 5. Thus the smooth field just built agrees with the pointwise horizontal lift; in particular the pointwise definition is smooth. **Uniqueness.** If $Z$ is any horizontal vector field $\pi$-related to $X$, then at each $p$ the vector $Z(p)\in H_p$ satisfies $d\pi_p(Z(p))=X_{\pi(p)}$, so $Z(p)=(d\pi_p|_{H_p})^{-1}(X_{\pi(p)})=\tilde X(p)$ by Corollary 5; hence $Z=\tilde X$. **Conclusion.** $\tilde X$ is a smooth vector field, horizontal and $\pi$-related to $X$, and it is the unique field with those two properties. $\blacksquare$

> [!note]- Corollary 7: $\tilde X$ is $G$-invariant, and $\widetilde{fX}=(f\circ\pi)\,\tilde X$ for $f\in C^\infty(M)$; the lift is $\mathbb R$-linear in $X$.
> **Claim.** (i) $dR_g\big(\tilde X(p)\big)=\tilde X(p\cdot g)$ for all $p,g$ — equivalently $(R_g)_*\tilde X=\tilde X$, the field $\tilde X$ is $G$-invariant. (ii) For $f\in C^\infty(M)$, $\widetilde{fX}=(f\circ\pi)\,\tilde X$. (iii) $\widetilde{X+Y}=\tilde X+\tilde Y$ and $\widetilde{aX}=a\,\tilde X$ for $a\in\mathbb R$.
>
> **Proof of (i).** We show $dR_g\big(\tilde X(p)\big)$ is the horizontal lift of $X_{\pi(p\cdot g)}$ at $p\cdot g$, hence equals $\tilde X(p\cdot g)$ by the uniqueness in Corollary 5. **It is horizontal.** $\tilde X(p)\in H_p$, so $dR_g\big(\tilde X(p)\big)\in dR_g(H_p)=H_{p\cdot g}$ (by Corollary 4). **It projects to the right vector.** Using $\pi\circ R_g=\pi$,
> $$d\pi_{p\cdot g}\big(dR_g\,\tilde X(p)\big)=d(\pi\circ R_g)_p\big(\tilde X(p)\big)=d\pi_p\big(\tilde X(p)\big)=X_{\pi(p)}=X_{\pi(p\cdot g)}\qquad\text{(chain rule; then }\pi\circ R_g=\pi\text{; then Corollary 6; then }\pi(p\cdot g)=\pi(p)\text{).}$$
> Being horizontal at $p\cdot g$ and projecting to $X_{\pi(p\cdot g)}$, the vector $dR_g\big(\tilde X(p)\big)$ equals $\widetilde{X_{\pi(p\cdot g)}}=\tilde X(p\cdot g)$ by Corollary 5. This proves (i).
>
> **Proof of (ii).** The field $(f\circ\pi)\,\tilde X$ is horizontal, since $\big((f\circ\pi)\tilde X\big)(p)=f(\pi(p))\,\tilde X(p)$ is a scalar multiple of the horizontal vector $\tilde X(p)\in H_p$ and $H_p$ is a linear subspace. Its projection is
> $$d\pi_p\big(f(\pi(p))\,\tilde X(p)\big)=f(\pi(p))\,d\pi_p\big(\tilde X(p)\big)=f(\pi(p))\,X_{\pi(p)}=(fX)_{\pi(p)}\qquad\text{(linearity of }d\pi_p\text{; then Corollary 6; then definition of }fX\text{).}$$
> A horizontal field projecting to $fX$ is the horizontal lift $\widetilde{fX}$ by the uniqueness in Corollary 6, so $\widetilde{fX}=(f\circ\pi)\,\tilde X$.
>
> **Proof of (iii).** At each $p$ the horizontal lift is $(d\pi_p|_{H_p})^{-1}$ applied to the value of the base field, and $(d\pi_p|_{H_p})^{-1}$ is a linear map (the inverse of a linear isomorphism, Corollary 5). Hence $\widetilde{(X+Y)}(p)=(d\pi_p|_{H_p})^{-1}(X_{\pi(p)}+Y_{\pi(p)})=\tilde X(p)+\tilde Y(p)$ and $\widetilde{aX}(p)=a\,\tilde X(p)$. **Conclusion.** The horizontal lift of vector fields is $\mathbb R$-linear, is $C^\infty(M)$-homogeneous through pullback (clause (ii)), and produces $G$-invariant fields (clause (i)). $\blacksquare$

The next corollary is the one this whole page is built toward. It says that the horizontal lift *almost* commutes with the Lie bracket — the failure to commute is a vertical vector field, and that vertical failure is precisely the curvature of the connection. It is the mechanism behind the structure equation of §4.3, previewed here because it needs nothing beyond the splitting.

> [!note]- Corollary 8 (foreshadowing curvature): $[\tilde X,\tilde Y]-\widetilde{[X,Y]}$ is vertical.
> **Claim.** For vector fields $X,Y\in\Gamma(TM)$, the vector field $[\tilde X,\tilde Y]-\widetilde{[X,Y]}$ on $P$ is vertical, that is $[\tilde X,\tilde Y]-\widetilde{[X,Y]}\in\Gamma(VP)$; equivalently, the horizontal part of $[\tilde X,\tilde Y]$ is $\widetilde{[X,Y]}$, and $\pi_H\big([\tilde X,\tilde Y]\big)=\widetilde{[X,Y]}$.
>
> **Proof.** We show $d\pi\big([\tilde X,\tilde Y]-\widetilde{[X,Y]}\big)=0$, which is exactly the assertion that the field lies in $\ker d\pi=VP$. **Both terms are $\pi$-related to $[X,Y]$.** By Corollary 6, $\tilde X$ is $\pi$-related to $X$ and $\tilde Y$ is $\pi$-related to $Y$. By the **naturality of the Lie bracket under smooth maps** — if $\tilde X\sim_\pi X$ and $\tilde Y\sim_\pi Y$ then $[\tilde X,\tilde Y]\sim_\pi[X,Y]$, which is part (f) of [[Thm - Lie Bracket Properties]], proved there from the characterisation $\tilde X(h\circ\pi)=(Xh)\circ\pi$ of [[Def - F-Related Vector Fields|π-relatedness]] applied twice — we get
> $$d\pi\big([\tilde X,\tilde Y]\big)=[X,Y]\circ\pi\qquad\text{(naturality of the bracket, [[Thm - Lie Bracket Properties]]).}$$
> On the other hand, $\widetilde{[X,Y]}$ is by Corollary 6 the horizontal field $\pi$-related to $[X,Y]$, so directly
> $$d\pi\big(\widetilde{[X,Y]}\big)=[X,Y]\circ\pi\qquad\text{(Corollary 6, $\pi$-relatedness of the lift).}$$
> **Subtract.** By linearity of $d\pi$,
> $$d\pi\big([\tilde X,\tilde Y]-\widetilde{[X,Y]}\big)=[X,Y]\circ\pi-[X,Y]\circ\pi=0,$$
> so $[\tilde X,\tilde Y]-\widetilde{[X,Y]}\in\ker d\pi=VP$ is vertical. **Identify the horizontal parts.** Since $\widetilde{[X,Y]}$ is horizontal, the equation $[\tilde X,\tilde Y]=\widetilde{[X,Y]}+(\text{vertical})$ is the decomposition of $[\tilde X,\tilde Y]$ into $H\oplus VP$ (Corollary 2), so $\pi_H\big([\tilde X,\tilde Y]\big)=\widetilde{[X,Y]}$ and $\pi_V\big([\tilde X,\tilde Y]\big)=[\tilde X,\tilde Y]-\widetilde{[X,Y]}$. **Conclusion.** The bracket of horizontal lifts fails to be the lift of the bracket only by a vertical vector field. Reading that vertical vector off in $\mathfrak g$ through $\omega$ gives $\omega\big([\tilde X,\tilde Y]\big)$; the curvature is, up to sign, exactly this quantity, since $\Omega(\tilde X,\tilde Y)=-\omega\big([\tilde X,\tilde Y]\big)$ (the vertical part of the bracket of horizontal lifts), as the structure-equation page **[[Def - Curvature of a Principal Connection]]** makes precise. The horizontal distribution is thus involutive — closed under the bracket — if and only if the curvature vanishes. $\blacksquare$

**Is an instance — the product connection on a trivial bundle.** Let $P=M\times G$ with $\pi=\operatorname{pr}_1$ the projection to $M$ and the right action $R_h(m,g)=(m,g\cdot h)$, and equip it with the **product connection** $\omega=\operatorname{pr}_2^*\theta$, where $\theta\in\Omega^1(G;\mathfrak g)$ is the [[Def - The Maurer-Cartan Form|Maurer–Cartan form]], $\theta_g=dL_{g^{-1}}\colon T_gG\to\mathfrak g$. We verify $H_{(m,g)}=T_mM\times\{0\}$ clause by clause. A tangent vector at $(m,g)$ is a pair $(v,w)\in T_mM\oplus T_gG$, and
$$\omega_{(m,g)}(v,w)=\big(\operatorname{pr}_2^*\theta\big)_{(m,g)}(v,w)=\theta_g\big(d\,\!\operatorname{pr}_2(v,w)\big)=\theta_g(w)\qquad\text{(definition of pullback; }d\,\!\operatorname{pr}_2(v,w)=w\text{).}$$
Therefore $(v,w)\in H_{(m,g)}=\ker\omega_{(m,g)}$ if and only if $\theta_g(w)=0$; but $\theta_g=dL_{g^{-1}}$ is a linear isomorphism $T_gG\to\mathfrak g$ (left translation is a diffeomorphism), so $\theta_g(w)=0$ if and only if $w=0$. Hence
$$H_{(m,g)}=\{(v,0):v\in T_mM\}=T_mM\times\{0\},$$
as claimed. This is consistent with every corollary: the vertical subspace is $V_{(m,g)}P=\{0\}\times T_gG$, the sum $T_mM\times\{0\}\ \oplus\ \{0\}\times T_gG$ is direct and equals $T_{(m,g)}(M\times G)$ (Corollary 2), $\dim H_{(m,g)}=\dim M$ (Corollary 3), and $d\pi_{(m,g)}(v,0)=v$ shows $d\pi|_H$ is an isomorphism onto $T_mM$ (Corollary 5). The horizontal lift of a vector field $X$ on $M$ is $\tilde X=(X,0)$, and since $[(X,0),(Y,0)]=([X,Y],0)=\widetilde{[X,Y]}$, the vertical defect of Corollary 8 vanishes identically — consistent with the product connection being flat, its curvature zero.

**Is NOT an instance — the horizontal distribution of the Hopf connection is not integrable.** Horizontality of a distribution does not make it a foliation. On the Hopf bundle $S^3\to S^2$ with structure group $U(1)$ and the standard connection $a_p(Y)=i\langle Y,p\cdot i\rangle$ of **[[Thm - The Standard Connection on the Hopf Bundle]]**, the horizontal distribution $H_p=\ker a_p=(p\cdot i)^\perp$ is a smooth rank-$2$ distribution on the three-manifold $S^3$ — everything Corollaries 1–5 promise — yet it is **not involutive**: there are horizontal vector fields $v_2,v_3$ on $S^3$ with $[v_2,v_3]=-2v_1$, and $v_1$ is the vertical fundamental field of $i$, so $[v_2,v_3]\notin H$. By the **[[Thm - The Frobenius Theorem|Frobenius theorem]]** — a distribution is integrable if and only if it is involutive — $H$ is not integrable: no surface in $S^3$ has $H$ as its tangent planes. This is precisely Corollary 8 with a nonzero vertical defect, and it is the geometric content of the Hopf connection having nonzero curvature; the computation is carried out in **[[Ex - The Horizontal Distribution of the Hopf Connection is Not Integrable]]**. The lesson is that "horizontal" is a pointwise linear-algebra notion, while "integrable" is a bracket-closure notion, and a connection is flat exactly when the two coincide.

**Calibration check.** Three verifications a reader should be able to carry out from the page alone. First, that $\pi_H$ and $\pi_V$ are complementary projections: $\pi_H+\pi_V=\operatorname{id}$ is immediate from their definitions, and $\pi_V^2(v)=\big(\omega(\pi_V v)\big)_P=\big(\omega((\omega(v))_P)\big)_P=(\omega(v))_P=\pi_V(v)$ using the normalisation axiom (2), so $\pi_V^2=\pi_V$ and hence $\pi_H^2=\pi_H$. Second, that the horizontal lift of a coordinate field in a local trivialisation is $\tilde{\partial_k}=\partial_k-\big(\operatorname{Ad}_{g^{-1}}A(\partial_k)\big)_P$ in the $U\times G$ coordinates with potential $A$ — obtained by solving $\omega(\partial_k,w)=\operatorname{Ad}_{g^{-1}}A(\partial_k)+\theta_g(w)=0$ for the vertical correction $w$, exactly the graph description of the True name section. Third, that for the product connection $[\tilde X,\tilde Y]=\widetilde{[X,Y]}$ exactly (no vertical defect), which recovers flatness and matches the general fact that $\omega\big([\tilde X,\tilde Y]\big)=0$ when the curvature is zero.

---

# Unlocked by This

> [!tip] Connection ↔ invariant horizontal distribution *(from Gauge Theory IV)*
> Corollaries 2, 3, and 4 show that the kernel of a connection form is a smooth $G$-invariant distribution complementary to the vertical bundle. The converse — that every such distribution is $\ker\omega$ for a unique connection form — makes "connection" and "invariant horizontal distribution" two names for one datum. This equivalence is proved on **[[Thm - Connection Forms Correspond to Invariant Horizontal Distributions]]**, whose inverse map sends a distribution $H$ to the form vanishing on $H$ and inverting $\xi\mapsto\xi_P$ on the vertical.

> [!tip] Curvature as the vertical defect of the bracket *(from Gauge Theory IV)*
> Corollary 8 is the seed of curvature: $\Omega(\tilde X,\tilde Y)=-\omega\big([\tilde X,\tilde Y]\big)$ measures exactly the vertical part of the bracket of horizontal lifts, and the connection is flat if and only if $H$ is involutive. This is developed on **[[Def - Curvature of a Principal Connection]]** and turned into the structure equation $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$ on **[[Thm - Structure Equation for the Curvature]]**.

> [!tip] Parallel transport and holonomy *(from Gauge Theory V)*
> The horizontal lift of a curve, defined here, is solved for existence and uniqueness in **Gauge Theory V**: each curve in the base and each starting point in the fibre determine a unique horizontal lift, and its endpoint defines parallel transport. Comparing the lift of a loop's start and end points gives the holonomy group, the global invariant of the connection.

> [!tip] Exterior covariant derivative *(from Gauge Theory IV)*
> The horizontal projection $\pi_H$ is the ingredient of the exterior covariant derivative $D^\omega\alpha:=(d\alpha)\circ\pi_H$, which restricts the exterior derivative to horizontal arguments and is the principal-bundle form of the covariant derivative on associated vector bundles. See **[[Def - Exterior Covariant Derivative on a Principal Bundle]]**.
