---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection on a Principal Bundle"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Def - Pullback of a Differential Form on a Manifold"
  - "Def - The Maurer-Cartan Form"
  - "Def - Fundamental Vector Field of a Group Action"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a smooth principal $G$-bundle over a smooth manifold $M$, with $G$ a Lie group acting on the **right**, $R_g(p)=p\cdot g$, and Lie algebra $\mathfrak g=T_eG$. For $\xi\in\mathfrak g$ the **fundamental vector field** is $\xi_P(p)=\frac{d}{dt}\big|_{t=0}\,p\cdot\exp(t\xi)$ (the notation of [[Def - Fundamental Vector Field of a Group Action]]); the vectors $\{\xi_P(p):\xi\in\mathfrak g\}$ span the vertical subspace $V_p=\ker d_p\pi$. We write $\operatorname{Ad}_g\colon\mathfrak g\to\mathfrak g$ for the adjoint representation, $\operatorname{Ad}_gX=gXg^{-1}$ for matrix groups. A **connection** on $P$ is a $\mathfrak g$-valued one-form $\omega\in\Omega^1(P;\mathfrak g)$ satisfying the two conditions recalled in the box below; $\mathcal A(P)$ denotes the set of all connections. The left **Maurer–Cartan form** of $G$ is $\theta\in\Omega^1(G;\mathfrak g)$, $\theta_g=d_gL_{g^{-1}}\colon T_gG\to\mathfrak g$ (the notation of [[Def - The Maurer-Cartan Form]]); for matrix groups $\theta=g^{-1}\,dg$. For a smooth map $g\colon U\to G$ we write $g^*\theta\in\Omega^1(U;\mathfrak g)$ for its pullback, $(g^*\theta)_x(v)=\theta_{g(x)}(d_xg(v))$.

A **local section** of $P$ over an open set $U\subseteq M$ is a smooth map $s\colon U\to P$ with $\pi\circ s=\operatorname{id}_U$; equivalently (via [[Thm - Sections of a Principal Bundle and Triviality]]) a local trivialisation of $P$ over $U$. In gauge theory a local section is called a **local gauge**, and the choice of one is a choice of gauge. The pullback $s^*\colon\Omega^1(P;\mathfrak g)\to\Omega^1(U;\mathfrak g)$ acts componentwise on the $\mathfrak g$ factor and as the ordinary pullback of forms (the notation and properties of [[Def - Pullback of a Differential Form on a Manifold]]). We use coordinates $x=(x^1,\dots,x^n)$ on $U$ and write $\partial_\mu=\partial/\partial x^\mu$; Greek indices $\mu,\nu$ run over $1,\dots,n=\dim M$ and are summed when repeated. The full symbol registry for the chapter is on [[Gauge Theory IV — Connections and Curvature on Principal Bundles]].

> [!warning] Convention: naming of the connection form and its local representation
> Haydys writes $a$ for the connection form on $P$ and $A:=\sigma^*a$ for its local representation with respect to a section $\sigma$ (his D2.2.16), and occasionally writes $\operatorname{ad}$ where the series writes $\operatorname{Ad}$. Bär writes $\omega$ for the connection form and $\omega_\alpha:=s_\alpha^*\omega$ for the local forms attached to sections $s_\alpha$ (his D2.3.3). This series writes $\omega\in\Omega^1(P;\mathfrak g)$ for the global form on the total space and $A_s\in\Omega^1(U;\mathfrak g)$ (or $A_\alpha$ for a section $s_\alpha$) for the local form on the base; the letter $A$ is reserved for the base object, matching the physicists' gauge potential. Bär's connection conditions are stated as (1) $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\circ\,\omega$ and (2) $\omega(\xi_P)=\xi$; his printed text (2.3.1) misprints (1) as "$R_g^*=\operatorname{Ad}_{g^{-1}}\circ\omega$", dropping the $\omega$ on the left — the corrected form, with $\omega_{p\cdot g}(d R_g X)=\operatorname{Ad}_{g^{-1}}\!\big(\omega_p(X)\big)$, is what we use.

---

# Axiom Motivation

A connection $\omega$ is a one-form on the total space $P$, an object of dimension $\dim M+\dim G$. That is precisely where it must live: the defining conditions $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$ and $\omega(\xi_P)=\xi$ speak about the group action and the vertical directions, which exist only upstairs on $P$. But almost everything one wants to *compute* — a curvature, a Yang–Mills action, a coupling of a charged field to a gauge field, a Chern number — is an integral over the base $M$, and almost every explicit example is given by writing functions of the base coordinates $x^\mu$. A one-form on a high-dimensional total space, equivariant under a group we cannot draw, is not a convenient object to calculate with. We would like to bring the connection *down* to the base, into an ordinary $\mathfrak g$-valued one-form on an open subset $U\subseteq M$, without losing any information. The construction that does this is the pullback along a section, and the purpose of this page is to define that local object, to say exactly how much of the connection it remembers, and to record the two features of it that most often cause confusion.

The desideratum is sharp. We want a rule that takes a connection $\omega$ and a chosen local gauge $s\colon U\to P$ and returns a one-form on $U$, in such a way that (i) the rule is purely local and computable — it should be an ordinary pullback of forms, so that all of the machinery of exterior calculus on $U$ applies verbatim; (ii) no information is thrown away over $U$ — the connection $\omega$ on the whole of $P|_U=\pi^{-1}(U)$ should be *reconstructible* from the local form together with the trivialisation, so that working on the base is genuinely equivalent to working on the total space; and (iii) the object should be exactly the physicists' *gauge potential* $A_\mu$, so that the geometric theory and the field theory are the same theory. The single formula $A_s:=s^*\omega$ meets all three, and the reconstruction (proved below) is what makes precise that nothing is lost.

There is one price, and it is the whole subtlety of gauge theory: the local form depends on the section. A connection is one global object; but there is no canonical section of a principal bundle (a bundle with a canonical section is trivial), so there is no canonical way to bring $\omega$ down to $U$. Different gauges $s$ and $s'=s\cdot g$ produce different local forms $A_s$ and $A_{s'}$, related by the inhomogeneous transformation law of [[Thm - Transformation of Local Connection and Curvature Forms]]. This is not a defect of the definition; it is the reason the theory is called *gauge* theory. The reader should therefore hold two facts in tension from the start: over a fixed $U$ with a fixed gauge, $A_s$ is a perfectly ordinary $\mathfrak g$-valued one-form one can write in coordinates; but the assignment $U\mapsto A_s$ is *not* a global object on $M$, because there is no gauge-independent meaning to "$A_\mu(x)$" until a gauge is fixed.

What breaks if we drop each ingredient? If we drop the section and try to define a "local form" by an arbitrary linear-algebra recipe rather than by pullback, we lose reconstruction: only the pullback along a genuine section is compatible with the equivariance condition (1), and it is exactly that compatibility that lets us recover $\omega$ on the fibre directions (the calculation in the reconstruction proof uses (1) at the single step that handles the group directions). If we forget that $A_s$ is merely $\mathfrak g$-valued and treat it as though it were a section of the adjoint bundle $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$ — a global object on $M$ — we make a category error that produces wrong answers the moment we change gauge: the *difference* of two connections is $\operatorname{ad}P$-valued and global, but a single connection's local form is neither. And if we imagine the family $(A_{s_\alpha})_\alpha$ over a trivialising cover assembles into a global one-form on $M$, we contradict the transformation law: the forms differ on overlaps by $g_{\alpha\beta}^*\theta$, an inhomogeneous *pure-gauge* term that is generally nonzero, so they do not glue. A reader who has internalised these three failure modes has understood the definition, because each of them is a way of forgetting that the object carries a gauge in its very definition.

---

# The Definition

Let $\pi\colon P\to M$ be a principal $G$-bundle with a connection $\omega\in\mathcal A(P)$, and let $s\colon U\to P$ be a local gauge over an open set $U\subseteq M$.

> **Definition (local connection form).** The **local connection form** of $\omega$ with respect to the gauge $s$ is the pullback
> $$A_s\;:=\;s^*\omega\;\in\;\Omega^1(U;\mathfrak g),$$
> the $\mathfrak g$-valued one-form on $U$ whose value on $v\in T_xU$ is $(A_s)_x(v)=\omega_{s(x)}\big(d_xs(v)\big)$.

When several sections $s_\alpha$ over a cover $\{U_\alpha\}$ are in play we write $A_\alpha:=s_\alpha^*\omega$.

**The gauge potential in coordinates.** Fixing coordinates $x^\mu$ on $U$, expand $A_s$ in the coordinate coframe:
$$A_s\;=\;A_\mu\,dx^\mu,\qquad A_\mu\colon U\to\mathfrak g,\quad A_\mu(x)=(A_s)_x(\partial_\mu)\in\mathfrak g.$$
The $\mathfrak g$-valued functions $A_\mu$ are the **gauge potential** (or **gauge field**) of physics; $A=A_\mu\,dx^\mu$ is exactly the field the physicist writes down. In the abelian case $G=U(1)$ one has $\mathfrak g=i\mathbb R$, and writing $A_\mu=i\,\mathsf A_\mu$ with $\mathsf A_\mu\colon U\to\mathbb R$ recovers the electromagnetic vector potential $\mathsf A_\mu$ of classical electrodynamics; the local form of a $U(1)$-connection *is* the electromagnetic potential (this is developed in [[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang-Mills Theory]]).

**The associated local curvature form.** Once the curvature $\Omega\in\Omega^2(P;\mathfrak g)$ of $\omega$ is available (see [[Def - Curvature of a Principal Connection]]), the same pullback produces the **local curvature form**
$$F_s\;:=\;s^*\Omega\;\in\;\Omega^2(U;\mathfrak g),\qquad F_s\;=\;dA_s+\tfrac12[A_s\wedge A_s],$$
where $[\cdot\wedge\cdot]$ is the bracket of $\mathfrak g$-valued forms of [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]] and $\tfrac12[A_s\wedge A_s]=A_s\wedge A_s$ for matrix groups. The identity $F_s=dA_s+\tfrac12[A_s\wedge A_s]$ is the local structure equation, proved on [[Thm - Structure Equation for the Curvature]]; here it only names the object, and the full transformation theory of $A_s$ and $F_s$ is [[Thm - Transformation of Local Connection and Curvature Forms]].

**The frame-bundle case: local connection form equals connection matrix.** When $P=\operatorname{Fr}(E)$ is the frame bundle of a vector bundle $E\to M$ of rank $k$, a local frame $e=(e_1,\dots,e_k)$ of $E$ over $U$ is precisely a local section of $\operatorname{Fr}(E)$, and the group is $G=GL_k$ with $\mathfrak g=\mathfrak{gl}_k$. If $\omega$ is the connection on $\operatorname{Fr}(E)$ induced by a covariant derivative $\nabla$ on $E$, then the local connection form $e^*\omega$ coincides with the **connection matrix** $A(\nabla,e)\in\Omega^1(U;\mathfrak{gl}_k)$ defined by $\nabla e=e\cdot A(\nabla,e)$ in [[Def - Connection Matrix and Local Form of a Connection]]:
$$e^*\omega\;=\;A(\nabla,e).$$
This identification — that the principal-bundle local connection form of chapter IV *is* the connection matrix of chapter II — is the content of [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]] in §4.4, and we state it here only with a forward link. It is the reason the two chapters describe the same geometry: the local matrix $A$ of a linear connection and the gauge potential $A_s$ of a principal connection are the same one-form read in a frame.

---

# Categorical / Structural Definition

There is a clean structural reading. A local gauge $s\colon U\to P$ is the same datum as a trivialisation $\Phi\colon U\times G\xrightarrow{\ \sim\ }P|_U$, $\Phi(x,g)=s(x)\cdot g$, by [[Thm - Sections of a Principal Bundle and Triviality]]. Transporting $\omega$ through $\Phi$ gives a connection $\Phi^*\omega$ on the *trivial* bundle $U\times G\to U$, and the local form is the value of that trivial-bundle connection along the identity section: $A_s=(s_0^*\Phi^*\omega)$ where $s_0(x)=(x,e)$. In this sense $A_s$ is the *coordinate representation* of $\omega$ in the chart of $P|_U$ furnished by the gauge, exactly as the Christoffel symbols are the coordinate representation of the Levi-Civita connection in a coordinate chart. The pullback functor $s^*$ is what carries a form on the trivialised total space to its representative on the base; the whole content of the local theory is that $s^*$ is injective on connections restricted to $P|_U$ (this is the reconstruction below), so no structural information over $U$ is lost by passing to the representative.

The family $(A_\alpha)_\alpha$ over a trivialising cover is then best understood not as a global one-form but as a *cochain* for the transition data $(g_{\alpha\beta})$: it is a collection of local representatives whose failure to agree on overlaps is measured by the pure-gauge terms $g_{\alpha\beta}^*\theta$, and a connection is precisely a cochain glued by the affine cocycle rule $A_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha+g_{\alpha\beta}^*\theta$ (see [[Thm - Transformation of Local Connection and Curvature Forms]]). This is the principal-bundle analogue of describing a global object by local data and a compatibility law, and it is the point of view under which "a connection is a consistent choice of gauge potentials" is a precise statement rather than a slogan.

---

# Relate to Other Fields / Compression

**True name.** The operational meaning of $A_s$ is: *the connection written in a gauge*. Officially it is a pullback of a form on the total space; operationally it is the object one integrates, varies, and quantises, and every explicit connection in the literature — the electromagnetic potential $A_\mu\,dx^\mu$, the Yang–Mills field $A^a_\mu T_a\,dx^\mu$, the Christoffel symbols $\Gamma^j_{ik}\,dx^k$, the BPST instanton potential — is a local connection form for some principal connection. The three appearances are one construction:

- In **electromagnetism** ($G=U(1)$), $A_s$ is the vector potential; the gauge freedom $s\mapsto s\cdot e^{i\chi}$ produces $A_s\mapsto A_s+i\,d\chi$, which is the classical gauge transformation $\mathsf A_\mu\mapsto\mathsf A_\mu+\partial_\mu\chi$.
- In **Yang–Mills theory** ($G$ compact non-abelian), $A_s$ is the gauge field, and its inhomogeneous transformation law $A\mapsto\operatorname{Ad}_{g^{-1}}A+g^*\theta$ is precisely the non-abelian gauge transformation $A_\mu\mapsto g^{-1}A_\mu g+g^{-1}\partial_\mu g$ that couples the theory to itself.
- In **Riemannian geometry** ($G=GL_n$ or $O(n)$ on the frame bundle), $A_s$ is the matrix of connection one-forms, whose entries in a coordinate frame are the Christoffel symbols; this is the identification $e^*\omega=A(\nabla,e)$ recorded above and the bridge to [[Def - Christoffel Symbols]].

**Compression.** The single sentence "a connection restricted to a trivialising patch is a $\mathfrak g$-valued one-form on the patch, defined up to the pure-gauge action of the transition functions" contains the entire local theory. Everything downstream — Wilson lines, the Yang–Mills action, minimal coupling of charged matter, characteristic-class integrands — is written in terms of $A_s$ and made gauge-invariant by combining $A_s$ with the transformation law so that the pure-gauge term cancels. The curvature $F_s=dA_s+\tfrac12[A_s\wedge A_s]$ transforms *homogeneously* ($F_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha$, no additive term), which is why it, and not $A_s$, descends to a global object on $M$ — a section-valued two-form in $\operatorname{ad}P$.

---

# Examples / Corollaries

**Is an instance — the product connection has vanishing local form in the identity gauge.** On the trivial bundle $M\times G\to M$ take the product connection $\omega=\operatorname{pr}_2^*\theta$, where $\operatorname{pr}_2\colon M\times G\to G$ is the projection and $\theta$ the Maurer–Cartan form; this is a connection on $M\times G$ (both connection conditions are verified on the Examples of [[Def - Connection on a Principal Bundle]], using $R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta$ and $\theta(\xi_G)=\xi$). Let $s_0(m)=(m,e)$ be the identity gauge. Then
$$A_{s_0}=s_0^*\operatorname{pr}_2^*\theta=(\operatorname{pr}_2\circ s_0)^*\theta \qquad\text{(pullback is functorial: }(g\circ f)^*=f^*g^*\text{)}.$$
But $\operatorname{pr}_2\circ s_0\colon M\to G$, $m\mapsto e$, is the constant map to the identity, and the pullback of any form along a constant map is zero (its differential is zero). Hence
$$A_{s_0}=0.$$
Every clause checks: $s_0$ is a section since $\pi\circ s_0(m)=m$; the pullback is the composite pullback; the composite lands on a constant map; a constant map kills one-forms. The product connection is flat and, in the identity gauge, its potential is literally zero.

**Is an instance — a general gauge on the trivial bundle produces a pure-gauge potential.** On $M\times G$ with the same $\omega=\operatorname{pr}_2^*\theta$, take an arbitrary gauge $s(m)=(m,g(m))$ determined by a smooth $g\colon U\to G$. Then $\operatorname{pr}_2\circ s=g$, so
$$A_s=s^*\operatorname{pr}_2^*\theta=(\operatorname{pr}_2\circ s)^*\theta=g^*\theta \qquad\text{(functoriality of pullback, then }\operatorname{pr}_2\circ s=g\text{)}.$$
For matrix groups this reads $A_s=g^{-1}\,dg$. A local form of the shape $g^*\theta$ is called **pure gauge**: it is the potential of the flat product connection seen in a rotated gauge, and (consistently with the transformation law $A_{s\cdot g}=\operatorname{Ad}_{g^{-1}}A_{s_0}+g^*\theta$ of [[Thm - Transformation of Local Connection and Curvature Forms]], with $A_{s_0}=0$) it carries zero curvature: $F_s=d(g^*\theta)+\tfrac12[g^*\theta\wedge g^*\theta]=0$ by the Maurer–Cartan equation $d\theta+\tfrac12[\theta\wedge\theta]=0$ pulled back by $g$ (see [[Thm - The Maurer-Cartan Equation]]). This is the standing example the reader should keep: pure gauge means "gauge-equivalent to zero", and it looks like $g^{-1}dg$.

**Corollary (reconstruction of the connection from its local form).** The local form loses nothing over $U$: the connection is uniquely recovered from it. This is the uniqueness half of Bär's Example 2.3.6 (his T2.3.7), which we prove in full.

> [!note]- Corollary and its complete proof: $\omega$ over $U$ is determined by $A_s$
> **Statement.** Let $\omega\in\mathcal A(P)$ and let $s\colon U\to P$ be a local gauge with local form $A_s=s^*\omega$. For every $x\in U$, every $g\in G$, every $v\in T_xU$, and every $\xi\in\mathfrak g$,
> $$\omega_{s(x)\cdot g}\Big(d R_g\big(d_xs(v)\big)+\xi_P\big(s(x)g\big)\Big)\;=\;\operatorname{Ad}_{g^{-1}}\!\big((A_s)_x(v)\big)+\xi. \tag{$\ast$}$$
> Moreover every tangent vector of $P$ at the point $s(x)g$ is *uniquely* of the form $d R_g(d_xs(v))+\xi_P(s(x)g)$ with $v\in T_xU$ and $\xi\in\mathfrak g$. Consequently $A_s$ determines $\omega$ on all of $P|_U=\pi^{-1}(U)$, and a connection is uniquely determined by the family of its local forms over any trivialising cover.
> 
> **What is assumed and what is shown.** We are given a connection $\omega$, meaning (by [[Def - Connection on a Principal Bundle]]) a $\mathfrak g$-valued one-form with (1) $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$, i.e. $\omega_{p\cdot g}(dR_gX)=\operatorname{Ad}_{g^{-1}}(\omega_p(X))$ for all $p,g,X$, and (2) $\omega(\xi_P)=\xi$ for all $\xi\in\mathfrak g$. We must first show that every tangent vector at $s(x)g$ decomposes as claimed (Step 0), then evaluate $\omega$ on such a vector to get $(\ast)$ (Step 1), then read off uniqueness of the connection (Step 2).
>
> > [!note]- Full proof
> > **Step 0 — every tangent vector at $s(x)g$ has the stated form, uniquely.** By [[Thm - Sections of a Principal Bundle and Triviality]], the map
> > $$\Phi\colon U\times G\to P|_U,\qquad \Phi(x,g)=s(x)\cdot g$$
> > is a diffeomorphism (a section trivialises the bundle over its domain). Hence its differential $d\Phi_{(x,g)}\colon T_xU\oplus T_gG\to T_{s(x)g}P$ is a linear isomorphism. We compute $d\Phi_{(x,g)}$ on the two summands.
> >
> > **Base directions.** For $v\in T_xU$, choose a curve $x(t)$ in $U$ with $x(0)=x$, $\dot x(0)=v$, and hold the group argument fixed at $g$. Then $\Phi(x(t),g)=s(x(t))\cdot g=R_g\big(s(x(t))\big)$, so
> > $$d\Phi_{(x,g)}(v,0)=\frac{d}{dt}\Big|_{0}R_g\big(s(x(t))\big)=dR_g\big(d_xs(v)\big) \qquad\text{(chain rule, }R_g\text{ smooth).}$$
> >
> > **Group directions.** For $w\in T_gG$, write $\xi:=\theta_g(w)=d_gL_{g^{-1}}(w)\in\mathfrak g$ (the Maurer–Cartan form of [[Def - The Maurer-Cartan Form]]; $L_{g^{-1}}$ is a diffeomorphism, so $w\mapsto\xi$ is a linear isomorphism $T_gG\to\mathfrak g$ and $w=d_eL_g(\xi)$). Take the curve $g(t)=g\exp(t\xi)$, which has $g(0)=g$ and $\dot g(0)=\frac{d}{dt}\big|_0 g\exp(t\xi)=d_eL_g(\xi)=w$, and hold the base argument fixed at $x$. Then, using associativity of the right action $s(x)\cdot(g\exp(t\xi))=(s(x)g)\cdot\exp(t\xi)$,
> > $$d\Phi_{(x,g)}(0,w)=\frac{d}{dt}\Big|_0 s(x)\cdot\big(g\exp(t\xi)\big)=\frac{d}{dt}\Big|_0 (s(x)g)\cdot\exp(t\xi)=\xi_P\big(s(x)g\big) \qquad\text{(definition of the fundamental vector field }\xi_P\text{).}$$
> >
> > **Combine.** By linearity of the differential $d\Phi_{(x,g)}$,
> > $$d\Phi_{(x,g)}(v,w)=dR_g\big(d_xs(v)\big)+\xi_P\big(s(x)g\big),\qquad \xi=\theta_g(w). \tag{$\dagger$}$$
> > Since $\Phi$ is a diffeomorphism, $d\Phi_{(x,g)}$ is bijective; and since $(v,w)\mapsto(v,\xi=\theta_g(w))$ is a linear isomorphism of $T_xU\oplus T_gG$ onto $T_xU\oplus\mathfrak g$, formula $(\dagger)$ exhibits every vector of $T_{s(x)g}P$ exactly once as $dR_g(d_xs(v))+\xi_P(s(x)g)$ with $(v,\xi)\in T_xU\oplus\mathfrak g$. This proves the uniqueness of the decomposition.
> >
> > **Step 1 — evaluation of $\omega$ on the decomposed vector, proving $(\ast)$.** Fix $x,g,v,\xi$ and apply $\omega_{s(x)g}$ to the vector in $(\dagger)$. By linearity of $\omega_{s(x)g}$,
> > $$\omega_{s(x)g}\Big(dR_g\big(d_xs(v)\big)+\xi_P\big(s(x)g\big)\Big)=\omega_{s(x)g}\Big(dR_g\big(d_xs(v)\big)\Big)+\omega_{s(x)g}\Big(\xi_P\big(s(x)g\big)\Big). \tag{$\dagger\dagger$}$$
> > **Second term (vertical part).** By connection condition (2), $\omega(\xi_P)=\xi$ at every point, so
> > $$\omega_{s(x)g}\big(\xi_P(s(x)g)\big)=\xi \qquad\text{(connection condition (2)).}$$
> > **First term (equivariant transport).** Set $X:=d_xs(v)\in T_{s(x)}P$. By connection condition (1) in the form $\omega_{p\cdot g}(dR_gX)=\operatorname{Ad}_{g^{-1}}(\omega_p(X))$, taken at $p=s(x)$,
> > $$\omega_{s(x)g}\big(dR_g\,X\big)=\operatorname{Ad}_{g^{-1}}\!\big(\omega_{s(x)}(X)\big) \qquad\text{(connection condition (1)).}$$
> > Now $\omega_{s(x)}(X)=\omega_{s(x)}\big(d_xs(v)\big)=(s^*\omega)_x(v)=(A_s)_x(v)$ by the definition of the pullback $s^*\omega$ (see [[Def - Pullback of a Differential Form on a Manifold]]) and of $A_s$. Since $\operatorname{Ad}_{g^{-1}}\colon\mathfrak g\to\mathfrak g$ is linear, it commutes with this evaluation, giving
> > $$\omega_{s(x)g}\big(dR_g\,d_xs(v)\big)=\operatorname{Ad}_{g^{-1}}\!\big((A_s)_x(v)\big).$$
> > **Substitute into $(\dagger\dagger)$:**
> > $$\omega_{s(x)g}\Big(dR_g\big(d_xs(v)\big)+\xi_P\big(s(x)g\big)\Big)=\operatorname{Ad}_{g^{-1}}\!\big((A_s)_x(v)\big)+\xi,$$
> > which is exactly $(\ast)$.
> >
> > **Step 2 — uniqueness of the connection.** Every point of $P|_U$ is $s(x)\cdot g$ for a unique $(x,g)\in U\times G$ (because $\Phi$ is a bijection), and by Step 0 every tangent vector there is uniquely $dR_g(d_xs(v))+\xi_P(s(x)g)$. Formula $(\ast)$ writes the value of $\omega$ on that tangent vector using only $A_s$, the transition data $g$, and $\xi$. Hence the restriction $\omega|_{P|_U}$ is completely determined by $A_s$. If two connections $\omega,\omega'$ have equal local forms $s_\alpha^*\omega=s_\alpha^*\omega'$ for all sections of a trivialising cover $\{U_\alpha\}$, then by the previous sentence $\omega=\omega'$ on each $P|_{U_\alpha}$; since the $U_\alpha$ cover $M$, the $P|_{U_\alpha}$ cover $P$, so $\omega=\omega'$ on $P$.
> >
> > **Conclusion.** A connection $\omega$ is uniquely reconstructible over $U$ from its single local form $A_s$ via $(\ast)$, and globally from the family of its local forms; no information is lost in passing from $\omega$ to $A_s$. $\blacksquare$

**Is NOT a global one-form — the family $(A_\alpha)$.** Take the frame bundle $\operatorname{Fr}(TS^2)$ of the round sphere with its Levi-Civita connection and the two coordinate gauges $s_N,s_S$ coming from stereographic charts. The local forms $A_N=s_N^*\omega$ and $A_S=s_S^*\omega$ are perfectly good $\mathfrak{gl}_2$-valued one-forms on their respective domains, but on the overlap they differ by $A_S=\operatorname{Ad}_{g^{-1}}A_N+g^*\theta$ with $g=g_{NS}$ the change-of-frame, and the term $g^*\theta=g^{-1}dg$ is nonzero there. Two one-forms that disagree on an overlap do not patch to a global one-form. This is the concrete face of the calibration point that a single connection's local forms are *not* a global object: what patches is the curvature $F_\alpha$ (which transforms without the additive term) and the *difference* of two connections (which is $\operatorname{ad}P$-valued).

**Calibration check.** Three verifications the reader can carry out from the page alone. First, $A_s$ is $\mathfrak g$-valued, not $\operatorname{ad}P$-valued: it takes values in the fixed Lie algebra $\mathfrak g$, and its transformation under a change of gauge carries the inhomogeneous $g^*\theta$; a section of $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$ transforms homogeneously by $\operatorname{Ad}_{g^{-1}}$ alone, which $A_s$ does only when $g^*\theta=0$, e.g. for a locally constant $g$. Second, in the identity gauge on a trivial bundle the product connection gives $A_{s_0}=0$ (worked above), so "flat" and "pure gauge" and "$A=g^{-1}dg$ for some $g$" are the same local statement. Third, using $(\ast)$ with $g=e$ (so $\operatorname{Ad}_{e^{-1}}=\operatorname{id}$ and $R_e=\operatorname{id}$): $\omega_{s(x)}(d_xs(v)+\xi_P)=(A_s)_x(v)+\xi$, which says $A_s$ is exactly the "horizontal record" of $\omega$ read at the section, while the vertical part is always the tautological $\xi$ — a direct sanity check that $A_s$ captures the non-trivial part of the connection and nothing spurious.

---

# Unlocked by This

> [!tip] Gauge transformation of the potential *(from this chapter)*
> The local form is the input to [[Thm - Transformation of Local Connection and Curvature Forms]]: under a change of gauge $s\mapsto s\cdot g$ the potential transforms as $A\mapsto\operatorname{Ad}_{g^{-1}}A+g^*\theta$, while the curvature transforms homogeneously $F\mapsto\operatorname{Ad}_{g^{-1}}F$. Every gauge-invariance argument in the series runs through this pair of laws.

> [!tip] The Yang–Mills action *(from Gauge Theory VII)*
> **The Yang–Mills functional** $\tfrac12\int_M|F_s|^2$ is written in terms of the local curvature $F_s=dA_s+\tfrac12[A_s\wedge A_s]$ and made gauge-invariant by the homogeneous transformation of $F_s$; the gauge potential $A_s$ is the field over which one varies to obtain the Yang–Mills equations.

> [!tip] Minimal coupling of charged matter *(from Gauge Theory VII–VIII)*
> A section of an associated bundle is differentiated by $\nabla=d+\rho_*(A_s)$ in a local gauge, where $\rho_*$ is the differential of the matter field's representation; the gauge potential is what "covariantly connects" the field across the base, and this is the geometric content of minimal coupling and of the twisted Dirac operator.
