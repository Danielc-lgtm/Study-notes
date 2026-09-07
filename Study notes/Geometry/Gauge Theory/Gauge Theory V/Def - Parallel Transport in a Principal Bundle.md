---
type: definition
subject: gauge-theory
prereqs:
  - "Thm - Existence and Uniqueness of Horizontal Lifts"
  - "Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles"
  - "Def - Parallel Transport"
  - "Def - Covariant Derivative along a Curve"
  - "Thm - Pull-Back of Connections and Curvature"
tags: [geometry, gauge-theory]
---

# Notation

This is a compound page: it defines three interlocking notions — parallel transport $\Gamma_c$ in a principal bundle, a parallel section of an associated bundle along a curve, and parallel transport $PT_c$ in an associated vector bundle — because they are one construction seen through three lenses, and separating them would hide the fact that the linear parallel transport of a vector, the transport of a whole frame, and the transport of a point of the principal bundle are all governed by a single horizontal lift.

Throughout, $\pi\colon P\to M$ is a smooth [[Def - Principal G-Bundle|principal $G$-bundle]] over a smooth manifold $M$, with $G$ acting on the **right**: $R_g(p)=p\cdot g$ for $p\in P$, $g\in G$. For $m\in M$ the fibre is $P_m:=\pi^{-1}(m)$, and the action is free and transitive on each fibre, so each $P_m$ is a right $G$-torsor. We fix a [[Def - Connection on a Principal Bundle|connection]] $\omega\in\Omega^1(P;\mathfrak g)$, where $\mathfrak g=T_eG$ is the Lie algebra; its [[Def - Horizontal Subspace and Horizontal Lift|horizontal subspace]] at $p$ is $H_p:=\ker\omega_p\subset T_pP$, a $G$-invariant complement of the vertical tangent space $V_p:=\ker d\pi_p$, so that $T_pP=H_p\oplus V_p$ and $dR_g(H_p)=H_{pg}$.

A **curve** is a piecewise smooth map $c\colon I\to M$ on a compact interval $I=[t_0,t_1]\subset\mathbb R$; $\dot c(t)\in T_{c(t)}M$ is its velocity. A curve $\tilde c\colon I\to P$ is a **lift** of $c$ if $\pi\circ\tilde c=c$, and a **horizontal lift** if in addition $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ for all $t$; a lift is uniquely determined by an initial point $\tilde c(t_0)=p\in P_{c(t_0)}$ ([[Thm - Existence and Uniqueness of Horizontal Lifts|existence and uniqueness of horizontal lifts]], restated at the point of use below).

Given a [[Def - Representation of a Lie Group|representation]] $\rho\colon G\to GL(V)$ on a finite-dimensional real or complex vector space $V$, with differential $\rho_*\colon\mathfrak g\to\mathfrak{gl}(V)$, the [[Def - Associated Bundle|associated vector bundle]] is $E=P\times_\rho V:=(P\times V)/G$, where $G$ acts by $(p,v)\cdot g=(p\cdot g,\rho(g)^{-1}v)$; the class of $(p,v)$ is written $[p,v]$, so the defining relation is $[p\cdot g,\ \rho(g)^{-1}v]=[p,v]$ for all $g\in G$. The fibre $E_m=\pi_E^{-1}(m)$ is a vector space, and for each fixed $p\in P_m$ the map $V\to E_m$, $v\mapsto[p,v]$, is a linear isomorphism. We write $\nabla=\nabla^\omega$ for the connection that $\omega$ [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|induces]] on $E$, and $\tfrac{\nabla}{dt}$ for the [[Def - Covariant Derivative along a Curve|covariant derivative along a curve]] $c$ that $\nabla$ determines on sections of $E$ over $c$ (that is, on sections of the pulled-back bundle $c^*E$).

> [!warning] Convention: names for parallel transport
> The literature writes this object in several ways. Bär writes $\Gamma(c)\colon P_{c(t_0)}\to P_{c(t_1)}$ for the principal-bundle map; Haydys writes $PT_\gamma\colon E_{\gamma(0)}\to E_{\gamma(1)}$ for the induced map on a vector bundle and defines only the vector-bundle version directly (leaving the principal case to the reader, Haydys Remark 103). **This series writes $\Gamma_c$ for parallel transport in the principal bundle $P$ and $PT_c$ for the induced parallel transport in an associated vector bundle $E$.** The object on a vector bundle $E=TM$ is exactly the [[Def - Parallel Transport|parallel transport of Riemannian geometry]] already defined in the vault; the present page recovers that as the special case $P=\operatorname{Fr}(TM)$, $\rho=\text{standard}$.

> [!warning] Convention: a typographical slip in Haydys
> On p. 32 Haydys trivialises $\gamma^*E$ and writes the pulled-back connection as $\tfrac{d}{dt}+B(t)\,dt$ with $B\colon[0,1]\to M_k(\mathbb R)$, then writes the parallel-transport equation as $\dot s+A(t)s(t)=0$. The two letters denote the same matrix-valued function: $A=B$. We write the connection matrix as $\mathcal A(t)$ throughout and use $\dot s+\mathcal A(t)s=0$, so that $A$ is never overloaded against the gauge potential $A_\alpha=s_\alpha^*\omega$ of the local sections.

---

# Axiom Motivation

A connection on a bundle exists to answer one question the bundle by itself cannot: given a point of the fibre $P_{c(t_0)}$ over the start of a curve, which point of the fibre $P_{c(t_1)}$ over the end is "the same point, carried along $c$"? The fibres $P_{c(t_0)}$ and $P_{c(t_1)}$ are abstractly isomorphic — both are right $G$-torsors — but there is no *canonical* isomorphism between them until extra data is supplied, because a bundle is only *locally* a product and the global identification of fibres is precisely what a nontrivial bundle refuses to give for free. Parallel transport is the identification the connection supplies, curve by curve. The definition must therefore do three things: produce, for each curve, an honest map between the end fibres; make that map respect the group action (so that it also transports every associated object — vectors, frames, spinors — coherently); and reduce, in the flat product case, to the naive "do nothing" identification, so that the construction genuinely generalises the elementary notion of keeping a vector constant.

The naive candidate is to pick a local trivialisation $P|_U\cong U\times G$ and declare that $(c(t_0),g)$ transports to $(c(t_1),g)$ — carry the second coordinate unchanged. The desideratum this fails is **independence of the trivialisation**: over the overlap of two charts the second coordinates differ by the transition function $g_{\alpha\beta}(c(t))$, which varies along the curve, so "keep the second coordinate fixed" says different things in different charts and is not a property of $P$ at all. What is needed is a rule for moving through $P$ that is intrinsic — expressible without reference to any chart. The connection provides exactly such a rule by singling out, at each point $p\in P$, the horizontal subspace $H_p\subset T_pP$: the directions in which one moves "without turning inside the fibre". Requiring the lift $\tilde c$ of $c$ to be everywhere horizontal, $\dot{\tilde c}(t)\in H_{\tilde c(t)}$, is a chart-free condition, and it determines $\tilde c$ uniquely once its starting point is fixed. Setting $\Gamma_c(p):=\tilde c(t_1)$ is then forced: it is the only map to $P_{c(t_1)}$ built from horizontality alone.

Consider dropping the horizontality clause and asking only that $\tilde c$ be *some* lift with $\tilde c(t_0)=p$. Then $\tilde c(t_1)$ can be any point of $P_{c(t_1)}$ whatsoever — write $\tilde c(t)=(c(t),h(t))$ in a chart and $h(t_1)$ is entirely free — so $\Gamma_c$ would not be defined at all. Horizontality is the clause that pins the fibre coordinate down: it converts the freedom in $h$ into a first-order ordinary differential equation, $\dot h(t)=-dR_{h(t)}\big(A_\alpha(\dot c(t))\big)$ in Bär's local form, whose solution through a given initial value is unique. Weaken the clause to "$\dot{\tilde c}(t)\in H_{\tilde c(t)}$ at $t=t_0$ only" and the same collapse occurs immediately after the initial instant. The horizontality must hold at every $t$; that is what makes the whole curve, and hence the endpoint map, deterministic.

Consider next dropping the requirement that the base curve be at least piecewise differentiable. Parallel transport is the endpoint value of the solution of an ordinary differential equation driven by $\dot c(t)$; if $\dot c$ does not exist, the equation has no right-hand side and there is nothing to solve. This is not a technicality that a cleverer definition could remove: a merely continuous curve carries no infinitesimal direction of travel, and the connection is a device for penalising motion in the fibre *per unit of base-direction travelled*. The concrete failure is exhibited on a nowhere-differentiable path in the Examples section. The lesson is that parallel transport is genuinely a differential-geometric object, tied to velocities, and the natural domain of curves is the piecewise smooth ones (the corners are harmless: one transports across each smooth arc and composes, and independence of the subdivision is part of the existence theorem).

Finally, why insist that the transport respect the $G$-action? Because the entire payoff of working on the principal bundle rather than on one associated bundle at a time is that a single horizontal lift transports *every* associated object at once. If $\Gamma_c$ commutes with the right action, $\Gamma_c(p\cdot g)=\Gamma_c(p)\cdot g$, then it descends to a well-defined map on each associated bundle $E=P\times_\rho V$ by $[p,v]\mapsto[\Gamma_c(p),v]$, and this map is automatically linear and — when $\rho$ preserves an inner product — automatically an isometry, with no further work. Drop equivariance and the induced map on $E$ would depend on which representative $(p,v)$ of a class $[p,v]$ one chose, and would fail to be well defined. Equivariance is not an optional decoration; it is the property that makes "parallel transport in $P$" and "parallel transport in every $E$" the same theorem. It is guaranteed by the connection's defining $G$-invariance of $H$, and the existence theorem records it in the clause "$\tilde c\cdot g$ is the horizontal lift through $p\cdot g$". A reader who wanted only these desiderata — a chart-free, deterministic, velocity-driven, action-respecting rule for identifying fibres along a curve — would be driven to exactly the horizontal-lift definition below.

---

# The Definition

Fix, once and for all, the connection $\omega$ on $\pi\colon P\to M$ and a curve $c\colon[t_0,t_1]\to M$. The construction rests on the following theorem, whose complete proof is on its own page; we restate it because every clause below invokes it.

> [!note] Restatement — existence and uniqueness of horizontal lifts
> **[[Thm - Existence and Uniqueness of Horizontal Lifts|Theorem]].** For any piecewise smooth curve $c\colon I\to M$, any $t_0\in I$, and any $p\in P_{c(t_0)}$, there is a unique piecewise smooth curve $\tilde c\colon I\to P$ with (i) $\pi\circ\tilde c=c$, (ii) $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ for all $t$, and (iii) $\tilde c(t_0)=p$. It is defined on all of $I$. Moreover, for every $g\in G$, the horizontal lift of $c$ through $p\cdot g$ is $\tilde c\cdot g:=R_g\circ\tilde c$.

## Parallel transport in the principal bundle

> **Definition (parallel transport, principal form).** Let $c\colon[t_0,t_1]\to M$ be piecewise smooth. The **parallel transport along $c$** determined by $\omega$ is the map
> $$\Gamma_c\colon P_{c(t_0)}\longrightarrow P_{c(t_1)},\qquad \Gamma_c(p):=\tilde c(t_1),$$
> where $\tilde c$ is the unique horizontal lift of $c$ with $\tilde c(t_0)=p$.

The map is well defined because the horizontal lift exists, is unique, and is defined on the whole interval (existence-uniqueness theorem, all three clauses). It is $G$-**equivariant**:
$$\Gamma_c(p\cdot g)=\Gamma_c(p)\cdot g\qquad\text{for all }p\in P_{c(t_0)},\ g\in G,$$
because the horizontal lift through $p\cdot g$ is $\tilde c\cdot g$ (last clause of the theorem), whose endpoint is $\tilde c(t_1)\cdot g=\Gamma_c(p)\cdot g$ (definition of $\tilde c\cdot g=R_g\circ\tilde c$). Since a $G$-equivariant map between right $G$-torsors is automatically a bijection — fixing any $p_0\in P_{c(t_0)}$ and $q_0:=\Gamma_c(p_0)$, every element of $P_{c(t_0)}$ is $p_0\cdot g$ for a unique $g$, and $\Gamma_c(p_0\cdot g)=q_0\cdot g$ ranges bijectively over $P_{c(t_1)}$ — the map $\Gamma_c$ is a bijection, indeed a diffeomorphism, as its smoothness follows from smooth dependence of the lift on the initial condition.

## Parallel sections along a curve in an associated bundle

Let $E=P\times_\rho V$ be an associated vector bundle and $\tilde c$ the horizontal lift of $c$ through a chosen $p\in P_{c(t_0)}$.

> **Definition (parallel section along $c$).** For a fixed $v\in V$, the section of $E$ along $c$ given by
> $$s_v\colon[t_0,t_1]\to E,\qquad s_v(t):=[\tilde c(t),v]\in E_{c(t)},$$
> is called the **parallel section of $E$ along $c$ with value $v$ in the frame $\tilde c$**. More generally, a section $s$ of $E$ along $c$ (that is, a section of $c^*E$) is **parallel along $c$** if $\tfrac{\nabla}{dt}s\equiv0$, where $\nabla=\nabla^\omega$ is the induced connection and $\tfrac{\nabla}{dt}$ its covariant derivative along $c$.

The two clauses of this definition — "$s_v(t)=[\tilde c(t),v]$" and "$\tfrac{\nabla}{dt}s=0$" — describe the *same* sections; that this is so is the content of the next result, which we prove in full because the whole page turns on it.

> [!note]- Corollary (Bär, Remark 2.6.3): the parallel sections are exactly the covariantly constant ones
> **Statement.** A section $s$ of $E$ along $c$ satisfies $\tfrac{\nabla}{dt}s\equiv0$ if and only if there is a fixed $v\in V$ with $s(t)=[\tilde c(t),v]$ for all $t$, where $\tilde c$ is a horizontal lift of $c$. In particular every $s_v$ is parallel, and the parallel sections along $c$ form a vector space isomorphic to $V$ via $v\mapsto s_v$.
>
> > [!note]- Full proof
> > **What we assume and what we must show.** We are given the connection $\nabla=\nabla^\omega$ on $E=P\times_\rho V$ induced by $\omega$, and a horizontal lift $\tilde c$ of $c$. We must prove the two implications, "$s(t)=[\tilde c(t),v]\Rightarrow\tfrac{\nabla}{dt}s=0$" and "$\tfrac{\nabla}{dt}s=0\Rightarrow s(t)=[\tilde c(t),v]$ for some fixed $v$", and then read off the vector-space statement.
> >
> > **Step 0 — the local formula for $\tfrac{\nabla}{dt}$ along a lift.** We first record the formula for the induced covariant derivative, restated from its own page.
> >
> > > [!note] Restatement — the induced covariant derivative
> > > **[[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|Theorem]] (local form).** For a smooth lift $\hat c$ of $c$ to $P$ and a smooth map $v\colon[t_0,t_1]\to V$, the section $\sigma(t):=[\hat c(t),v(t)]$ of $E$ along $c$ has
> > > $$\frac{\nabla}{dt}\sigma(t)=\Big[\hat c(t),\ \dot v(t)+\rho_*\big(\omega_{\hat c(t)}(\dot{\hat c}(t))\big)\,v(t)\Big].$$
> >
> > (The formula is the along-a-curve specialisation of $\nabla_X[p,v]=[p,\partial_X v+\rho_*(p^*\omega(X))v]$; Bär's printed version writes $\omega_{\tilde c(t)}(\dot s_\alpha(t))$ for the correction term, a slip for $\omega_{\tilde c(t)}(\dot{\tilde c}(t))$, which we use here.)
> >
> > **Direction 1 ($\Rightarrow$): $s(t)=[\tilde c(t),v]$ with $v$ constant is parallel.** Take $\hat c:=\tilde c$ the horizontal lift and $v(t):=v$ constant in the formula of Step 0. Then $\dot v(t)=0$ (since $v$ is constant), and $\omega_{\tilde c(t)}(\dot{\tilde c}(t))=0$ (since $\tilde c$ is horizontal, $\dot{\tilde c}(t)\in H_{\tilde c(t)}=\ker\omega_{\tilde c(t)}$). Substituting,
> > $$\frac{\nabla}{dt}s(t)=\big[\tilde c(t),\ 0+\rho_*(0)\,v\big]=[\tilde c(t),0]=0_{E_{c(t)}}\qquad\text{(both correction terms vanish; }\rho_*(0)=0\text{ is linear).}$$
> > Hence $s_v$ is parallel, for every $v\in V$.
> >
> > **Direction 2 ($\Leftarrow$): a parallel section has the form $[\tilde c(t),v]$ with $v$ constant.** Let $s$ be any section of $E$ along $c$ with $\tfrac{\nabla}{dt}s\equiv0$. Because $\tilde c(t)\in P_{c(t)}$ is a point of the fibre and $w\mapsto[\tilde c(t),w]$ is a linear isomorphism $V\to E_{c(t)}$ (definition of the associated bundle), there is a *unique* smooth curve $v\colon[t_0,t_1]\to V$ with
> > $$s(t)=[\tilde c(t),v(t)]\qquad\text{for all }t\qquad\text{(read the fibre coordinate of }s\text{ in the frame }\tilde c\text{).}$$
> > Smoothness of $v$ holds because $\tilde c$ is smooth and the identification is a smooth family of linear isomorphisms. Applying Step 0 with $\hat c=\tilde c$ (horizontal, so the correction term $\rho_*(\omega_{\tilde c}(\dot{\tilde c}))$ vanishes as in Direction 1),
> > $$0=\frac{\nabla}{dt}s(t)=[\tilde c(t),\dot v(t)]\qquad\text{(hypothesis }\tfrac{\nabla}{dt}s=0\text{; Step 0 with the correction term }=0\text{).}$$
> > Since $w\mapsto[\tilde c(t),w]$ is injective and sends $\dot v(t)$ to $0$, we conclude $\dot v(t)=0$ for all $t$, so $v$ is constant, say $v(t)\equiv v_0\in V$. Therefore $s(t)=[\tilde c(t),v_0]=s_{v_0}(t)$, of the claimed form.
> >
> > **Conclusion.** The two directions show that the parallel sections along $c$ are exactly the maps $s_v$, $v\in V$. The assignment $v\mapsto s_v$ is linear ($s_{av+bw}=a\,s_v+b\,s_w$ because $[\tilde c(t),av+bw]=a[\tilde c(t),v]+b[\tilde c(t),w]$ in the vector space $E_{c(t)}$) and injective (if $s_v\equiv0$ then $[\tilde c(t_0),v]=0$, so $v=0$ by injectivity of the frame map), hence a linear isomorphism onto the space of parallel sections; the latter is therefore a vector space of dimension $\dim V$. $\blacksquare$

## Parallel transport in an associated vector bundle

> **Definition (parallel transport, associated form).** The **parallel transport in $E=P\times_\rho V$ along $c$** is the map
> $$PT_c\colon E_{c(t_0)}\longrightarrow E_{c(t_1)},\qquad PT_c\big([p,v]\big):=[\Gamma_c(p),v],\qquad p\in P_{c(t_0)},\ v\in V.$$
> Equivalently, $PT_c(e)=s(t_1)$, where $s$ is the unique parallel section of $E$ along $c$ with $s(t_0)=e$.

> [!note]- Corollary: $PT_c$ is a well-defined linear isomorphism, and the two descriptions agree
> **Statement.** The map $PT_c$ is (i) well defined, independent of the representative $(p,v)$ chosen for a class $[p,v]$; (ii) a linear isomorphism $E_{c(t_0)}\to E_{c(t_1)}$; and (iii) equal to the endpoint map of the parallel section, $PT_c([p,v])=s_v(t_1)$ where $s_v$ is the parallel section along $c$ with $s_v(t_0)=[p,v]$.
>
> > [!note]- Full proof
> > **Assumptions and goal.** We use only the equivariance $\Gamma_c(p\cdot g)=\Gamma_c(p)\cdot g$ (proved above) and the associated-bundle relation $[p\cdot g,\rho(g)^{-1}v]=[p,v]$. We must establish the three clauses.
> >
> > **(i) Well-definedness.** Two pairs represent the same class exactly when they differ by the $G$-action: $[p',v']=[p,v]$ iff $p'=p\cdot g$ and $v'=\rho(g)^{-1}v$ for some $g\in G$. Compute the two candidate values:
> > $$PT_c([p\cdot g,\rho(g)^{-1}v])=[\Gamma_c(p\cdot g),\ \rho(g)^{-1}v]=[\Gamma_c(p)\cdot g,\ \rho(g)^{-1}v]\qquad\text{(definition of }PT_c\text{; equivariance of }\Gamma_c\text{)}$$
> > $$=[\Gamma_c(p),\ v]=PT_c([p,v])\qquad\text{(associated-bundle relation with }q=\Gamma_c(p),\ [q\cdot g,\rho(g)^{-1}v]=[q,v]\text{).}$$
> > So the value does not depend on the representative: $PT_c$ is well defined.
> >
> > **(ii) Linearity and bijectivity.** Fix a single $p_0\in P_{c(t_0)}$ and set $q_0:=\Gamma_c(p_0)\in P_{c(t_1)}$. The maps
> > $$\iota_0\colon V\to E_{c(t_0)},\ v\mapsto[p_0,v],\qquad \iota_1\colon V\to E_{c(t_1)},\ v\mapsto[q_0,v]$$
> > are linear isomorphisms (definition of the associated bundle: fixing a point of the fibre trivialises it). Every $e\in E_{c(t_0)}$ is $[p_0,v]$ for a unique $v=\iota_0^{-1}(e)$, and by definition $PT_c([p_0,v])=[\Gamma_c(p_0),v]=[q_0,v]=\iota_1(v)$. Hence
> > $$PT_c=\iota_1\circ\iota_0^{-1}\colon E_{c(t_0)}\to E_{c(t_1)}\qquad\text{(both sides send }[p_0,v]\mapsto[q_0,v]\text{).}$$
> > A composite of linear isomorphisms is a linear isomorphism, so $PT_c$ is one, with inverse $\iota_0\circ\iota_1^{-1}$.
> >
> > **(iii) Agreement with the parallel section.** Let $\tilde c$ be the horizontal lift with $\tilde c(t_0)=p$, so $\Gamma_c(p)=\tilde c(t_1)$, and let $s_v(t)=[\tilde c(t),v]$ be the parallel section through $[p,v]$ (its value at $t_0$ is $[\tilde c(t_0),v]=[p,v]$, and it is parallel by Direction 1 of the previous corollary). Then
> > $$s_v(t_1)=[\tilde c(t_1),v]=[\Gamma_c(p),v]=PT_c([p,v])\qquad\text{(definition of }s_v\text{; }\tilde c(t_1)=\Gamma_c(p)\text{; definition of }PT_c\text{).}$$
> > Uniqueness of the parallel section with a given initial value is the previous corollary's isomorphism $v\mapsto s_v$. Therefore $PT_c$ is the endpoint map of parallel sections. $\blacksquare$

## Equivalence with the direct ordinary-differential-equation definition

Haydys defines parallel transport on a vector bundle $E$ with connection $\nabla$ without any principal bundle: pull $\nabla$ back to $c^*E$, trivialise $c^*E\cong V\times[t_0,t_1]$ (legitimate because $c^*E$ is a bundle over the contractible interval, hence trivial — see the restatement below), write $c^*\nabla=\tfrac{d}{dt}+\mathcal A(t)$ with $\mathcal A\colon[t_0,t_1]\to\operatorname{End}(V)$ continuous, and declare $s$ parallel along $c$ iff, viewed as $s\colon[t_0,t_1]\to V$, it solves the linear ordinary differential equation
$$\dot s(t)+\mathcal A(t)\,s(t)=0.$$
His $PT_\gamma\colon E_{c(t_0)}\to E_{c(t_1)}$ is $s_0\mapsto s(t_1)$ for the solution $s$ with $s(t_0)=s_0$.

> [!note] Restatement — a bundle over an interval is trivial
> **[[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|Theorem]], clause (c).** Every principal (or vector) bundle over a contractible manifold, in particular over the interval $[t_0,t_1]$, is trivial. Consequently $c^*E$ admits a global frame, in which $c^*\nabla$ takes the form $\tfrac{d}{dt}+\mathcal A(t)$.

> [!note]- Corollary: Haydys's definition and the horizontal-lift definition coincide
> **Statement.** For an associated vector bundle $E=P\times_\rho V$ with induced connection $\nabla=\nabla^\omega$, a section $s$ of $E$ along $c$ is parallel in Haydys's sense (solves $\dot s+\mathcal A s=0$ in a global frame of $c^*E$) if and only if it is parallel in the horizontal-lift sense ($\tfrac{\nabla}{dt}s=0$). Consequently $PT_\gamma=PT_c$ as maps $E_{c(t_0)}\to E_{c(t_1)}$.
>
> > [!note]- Full proof
> > **Goal.** We show that both notions of "parallel" are the single condition $\tfrac{\nabla}{dt}s=0$, so they coincide and their endpoint maps agree.
> >
> > **Step 1 — Haydys's equation is $\tfrac{\nabla}{dt}s=0$ written in a frame.** Choose a global frame $(f_1,\dots,f_k)$ of $c^*E$ (it exists by the restatement above; $k=\dim V$). Writing $s(t)=\sum_i s^i(t)f_i(t)$ with coordinate vector $s(t)=(s^i(t))\in V$, the covariant derivative along $c$ is, by the definition of the connection matrix $\mathcal A$ of $c^*\nabla$ in this frame,
> > $$\frac{\nabla}{dt}s(t)=\sum_i\dot s^i(t)f_i(t)+\sum_i s^i(t)\,\frac{\nabla}{dt}f_i(t)=\Big(\dot s(t)+\mathcal A(t)s(t)\Big)\ \text{in the frame }(f_i)\qquad\text{(Leibniz rule for }\tfrac{\nabla}{dt}\text{; }\tfrac{\nabla}{dt}f_i=\textstyle\sum_j\mathcal A^{j}{}_i f_j\text{).}$$
> > Here the Leibniz rule for the covariant derivative along a curve, $\tfrac{\nabla}{dt}(fs)=\dot f\,s+f\tfrac{\nabla}{dt}s$, is the defining property of $\tfrac{\nabla}{dt}$ ([[Def - Covariant Derivative along a Curve|covariant derivative along a curve]]). Since the frame is a basis at each $t$, the bundle-valued expression $\tfrac{\nabla}{dt}s$ vanishes if and only if its coordinate vector $\dot s+\mathcal A s$ vanishes. Thus
> > $$\tfrac{\nabla}{dt}s\equiv0\iff\dot s+\mathcal A s\equiv0\qquad\text{(a vector is zero iff its coordinates in a basis are zero).}$$
> > This is precisely the equality of the horizontal-lift notion of parallel (left side) with Haydys's notion (right side).
> >
> > **Step 2 — the endpoint maps agree.** Both $PT_\gamma$ and $PT_c$ send $s_0\in E_{c(t_0)}$ to $s(t_1)$, where $s$ is *the* section along $c$ with $s(t_0)=s_0$ and $\tfrac{\nabla}{dt}s=0$ — unique by the existence-uniqueness theorem for the linear equation $\dot s+\mathcal A s=0$ (a linear ordinary differential equation with continuous coefficients has a unique solution on all of $[t_0,t_1]$ for each initial value). By Step 1 the two definitions single out the same $s$, so they assign the same $s(t_1)$. Hence $PT_\gamma=PT_c$. $\blacksquare$

---

# Categorical / Structural Definition

Parallel transport organises into a functor, and this is the cleanest way to see what kind of object it is. Let the **piecewise smooth path groupoid** $\Pi^{\mathrm{ps}}(M)$ have as objects the points of $M$ and as morphisms $m\to m'$ the piecewise smooth curves from $m$ to $m'$, composed by concatenation $c_2*c_1$ (first $c_1$, then $c_2$). (Strictly this is a category rather than a groupoid unless one quotients by reparametrisation and inserts formal inverses; the reparametrisation-invariance and the inverse $\Gamma_{c^{-1}}=\Gamma_c^{-1}$ that upgrade it to a groupoid are proved on [[Thm - Properties of Parallel Transport|the properties page]] and we do not presuppose them here.) Let $\mathbf{Tor}_G$ be the category whose objects are right $G$-torsors and whose morphisms are $G$-equivariant maps.

Then a connection $\omega$ on $P$ determines a functor
$$\mathcal T_\omega\colon\Pi^{\mathrm{ps}}(M)\longrightarrow\mathbf{Tor}_G,\qquad \mathcal T_\omega(m)=P_m,\qquad \mathcal T_\omega(c)=\Gamma_c,$$
sending each point to its fibre (a right $G$-torsor) and each curve to its parallel transport (a $G$-equivariant map of torsors, hence an isomorphism). Functoriality is the statement $\Gamma_{c_2*c_1}=\Gamma_{c_2}\circ\Gamma_{c_1}$ and $\Gamma_{\text{constant}}=\operatorname{id}$, again the content of the properties page; equivariance of each $\Gamma_c$ is proved above and is what lands the morphism in $\mathbf{Tor}_G$ rather than merely in $\mathbf{Set}$. Post-composing with the "associate a representation" functor $-\times_\rho V\colon\mathbf{Tor}_G\to\mathbf{Vect}$ (a torsor $Q$ goes to the vector space $Q\times_\rho V$, an equivariant map goes to the induced linear map) produces the vector-bundle transport: $PT_c$ is $\mathcal T_\omega(c)\times_\rho V$. In this language the three notions of the page are one functor read through two composed functors, and the linearity of $PT_c$ is not a computation but the automatic fact that a functor into $\mathbf{Vect}$ sends isomorphisms to linear isomorphisms. This is the structural meaning of "a single horizontal lift transports everything at once": there is one functor $\mathcal T_\omega$, and every associated transport is its image under an associating functor.

---

# Relate to Other Fields / Compression

**True name.** Officially, $\Gamma_c$ is defined by lifting horizontally and reading the endpoint. Operationally, parallel transport *is the solution operator of the transport ordinary differential equation*: on a matrix group $G\subset GL(n;\mathbb K)$ or on a vector bundle it is $s(t_1)$ where $\dot s+\mathcal A(t)s=0$, and this operator has the closed form of a [[Def - Path-Ordered Exponential|path-ordered exponential]] $\mathcal P\exp\!\big(-\!\int_c A_\alpha\big)$. So the true name of parallel transport is "the connection integrated along the curve", with the ordering of the integration mattering exactly to the extent that the connection fails to commute with itself along $c$ — which is the extent to which the [[Def - Curvature of a Principal Connection|curvature]] is nonzero. The elementary picture of "sliding a vector along, keeping it as constant as the geometry allows" is faithful, provided "constant" is read as "annihilated by the covariant derivative", not "unchanged in some chart".

In physics this operator is the **Wilson line**: in a gauge theory with gauge group $G$ and gauge potential $A$, the transport of a charged field along a path $c$ is $\mathcal P\exp\!\big(-\!\int_c A\big)$, and the trace of the transport around a closed loop is the **Wilson loop**, the basic gauge-invariant observable. The Aharonov–Bohm effect is the statement that this loop transport can be nontrivial even where the field strength $F$ vanishes pointwise, because the transport sees the potential's integral, not only its curl; on a non-simply-connected region that integral need not be zero. This is the same phenomenon that makes flat connections carry nontrivial [[Def - Holonomy Group of a Connection|holonomy]].

The construction compresses several apparently separate transports into one. The [[Def - Parallel Transport|parallel transport of Riemannian geometry]] is the case $P=\operatorname{Fr}(TM)$, $\rho=$ standard; the transport of the frame bundle is a moving frame all of whose vectors are parallel (verified below); the transport of a spinor field (chapter VIII) is the case of the spin representation; the transport of a section of $\operatorname{End}E$ used in gauge theory is the case of the adjoint representation. All are $PT_c$ for one and the same $\Gamma_c$. The monodromy of a covering space is the discrete-group shadow of this: a covering $\tilde M\to M$ is a principal bundle with discrete structure group, its unique connection is flat, and its parallel transport along a loop is the deck transformation the loop induces — the bridge that chapter V's flat-connection theory makes precise.

---

# Examples / Corollaries

**Is an instance — the product connection.** Let $P=M\times G$ with the projection $\pi(m,g)=m$ and the right action $(m,g)\cdot g'=(m,gg')$, carrying the **product connection** $\omega=\operatorname{pr}_G^*\theta$, where $\theta$ is the left [[Def - The Maurer-Cartan Form|Maurer–Cartan form]] on $G$ and $\operatorname{pr}_G\colon M\times G\to G$ is the projection. We verify $\Gamma_c(m,g)=(c(t_1),g)$ clause by clause. At $(m,g)$ a tangent vector is a pair $(u,w)$ with $u\in T_mM$, $w\in T_gG$, and $\omega_{(m,g)}(u,w)=\theta_g(w)$ (definition of $\operatorname{pr}_G^*\theta$). Since $\theta_g\colon T_gG\to\mathfrak g$ is a linear isomorphism, $\omega_{(m,g)}(u,w)=0$ iff $w=0$, so the horizontal subspace is $H_{(m,g)}=T_mM\times\{0\}$. A lift of $c$ through $(c(t_0),g_0)$ has the form $\tilde c(t)=(c(t),h(t))$ with $h(t_0)=g_0$; its velocity is $\dot{\tilde c}(t)=(\dot c(t),\dot h(t))$, which is horizontal iff $\dot h(t)=0$, that is iff $h$ is constant $=g_0$. Hence $\tilde c(t)=(c(t),g_0)$ and $\Gamma_c(c(t_0),g_0)=\tilde c(t_1)=(c(t_1),g_0)$, as claimed: the product connection carries the fibre coordinate along unchanged, recovering the naive transport that a *single* global trivialisation makes available.

**Is an instance — the flat $U(1)$-line bundle over the circle, with holonomy $e^{-2\pi ia}$.** Let $E=S^1\times\mathbb C$ be the trivial Hermitian line bundle over the circle $S^1=\{e^{i\theta}:\theta\in\mathbb R/2\pi\mathbb Z\}$, with connection $\nabla=d+A$ where $A=ia\,d\theta$ for a real constant $a$ (this is the $U(1)$-connection whose principal form lives on $S^1\times U(1)$). Take the loop $c(\theta)=e^{i\theta}$, $\theta\in[0,2\pi]$, based at $1$. A section $s\colon[0,2\pi]\to\mathbb C$ is parallel along $c$ iff $\tfrac{\nabla}{d\theta}s=\dot s+A(\dot c)s=0$; here $\dot c=\partial_\theta$ and $A(\partial_\theta)=ia$, so the transport equation is
$$\dot s(\theta)+ia\,s(\theta)=0\qquad\text{(the connection matrix along }c\text{ is }\mathcal A(\theta)=ia\text{, constant).}$$
Its solution with $s(0)=s_0$ is $s(\theta)=e^{-ia\theta}s_0$ (verify: $\dot s=-ia\,e^{-ia\theta}s_0=-ia\,s$). Therefore
$$PT_c(s_0)=s(2\pi)=e^{-2\pi ia}s_0,$$
so parallel transport once around the circle is multiplication by $e^{-2\pi ia}$. When $a\in\mathbb Z$ this is the identity and the connection's transport is trivial around the loop; for $a\notin\mathbb Z$ it is a nontrivial rotation of the fibre even though the curvature $F=dA=0$ vanishes identically — the circle is not simply connected, so a flat connection can still transport nontrivially. This is the same number that reappears in chapter II's exercise on this bundle and that the [[Def - Holonomy Group of a Connection|holonomy group]] records as $\{e^{-2\pi ika}:k\in\mathbb Z\}$.

**Is an instance — the frame bundle: a horizontal lift is a parallel frame.** Let $E\to M$ be a rank-$n$ real vector bundle, $P=\operatorname{Fr}(E)$ its [[Def - Frame Bundle of a Vector Bundle|frame bundle]] (whose fibre over $m$ is the set of ordered bases of $E_m$, a right $GL_n(\mathbb R)$-torsor), and $\rho$ the standard representation of $GL_n(\mathbb R)$ on $\mathbb R^n$, so that $E\cong\operatorname{Fr}(E)\times_\rho\mathbb R^n$. A point of the fibre is a frame $\tilde c(t)=(b_1(t),\dots,b_n(t))$, an ordered basis of $E_{c(t)}$, and under the associated-bundle identification the $i$-th vector is $b_i(t)=[\tilde c(t),e_i]$ for the standard basis vector $e_i\in\mathbb R^n$. By the corollary of the previous section, $[\tilde c(t),e_i]$ is a parallel section of $E$ along $c$ if and only if $\tilde c$ is horizontal; applying this for each $i$ shows that $\tilde c$ is a horizontal lift **if and only if every $b_i$ is a parallel section of $E$ along $c$**. Thus parallel transport of a frame is exactly the transport of each of its vectors, and the horizontal lift is "the frame carried parallelly". This is Bär's Example 2.6.1 and it is the bridge to Riemannian geometry: for $E=TM$ with the Levi-Civita connection, $\Gamma_c$ on $\operatorname{Fr}(TM)$ is the transport of tangent frames, and its associated $PT_c$ on $TM$ is the classical [[Def - Parallel Transport|parallel transport]].

**Corollary — a constant curve gives the identity.** If $c\equiv m$ is constant, its horizontal lift through any $p\in P_m$ is the constant curve $\tilde c\equiv p$ (a constant curve has velocity $0\in H_p$, so it is horizontal, and it is the unique such lift). Hence $\Gamma_c(p)=\tilde c(t_1)=p$ and $\Gamma_c=\operatorname{id}_{P_m}$; likewise $PT_c=\operatorname{id}_{E_m}$. This is the base case of every functoriality statement and the sanity check that "transport along no motion changes nothing".

> [!note]- Corollary — parallel transport in a Euclidean or Hermitian bundle is an isometry
> **Statement.** Suppose $E=P\times_\rho V$ carries a fibre metric induced by a $G$-invariant inner product $\langle\cdot,\cdot\rangle_V$ on $V$ (equivalently, $\rho$ takes values in $O(V)$ for the real case or $U(V)$ for the complex case, so that $\nabla$ is a metric, respectively Hermitian, connection). Then for every piecewise smooth curve $c$, the parallel transport $PT_c\colon E_{c(t_0)}\to E_{c(t_1)}$ is a linear isometry.
>
> > [!note]- Full proof
> > **Goal.** With $\langle[p,v],[p,w]\rangle_{E_m}:=\langle v,w\rangle_V$ the induced fibre metric, we must show $\langle PT_c(e),PT_c(e')\rangle=\langle e,e'\rangle$ for all $e,e'\in E_{c(t_0)}$.
> >
> > **Step 0 — the fibre metric is well defined.** For a class $[p,v]$ and another representative $[p\cdot g,\rho(g)^{-1}v]$ of the same element, $\langle\rho(g)^{-1}v,\rho(g)^{-1}w\rangle_V=\langle v,w\rangle_V$ because $\rho(g)^{-1}\in O(V)$ (or $U(V)$) preserves the inner product ($G$-invariance of $\langle\cdot,\cdot\rangle_V$). So the formula depends only on the classes.
> >
> > **Step 1 — read both vectors in one frame.** Fix $p_0\in P_{c(t_0)}$, write $e=[p_0,v]$ and $e'=[p_0,w]$ with $v=\iota_0^{-1}(e)$, $w=\iota_0^{-1}(e')$, and set $q_0:=\Gamma_c(p_0)$. Then $PT_c(e)=[q_0,v]$ and $PT_c(e')=[q_0,w]$ (definition of $PT_c$; the representative $p_0$ transports to $q_0$).
> >
> > **Step 2 — compare inner products.** Using the definition of the fibre metric at $c(t_0)$ and at $c(t_1)$,
> > $$\langle PT_c(e),PT_c(e')\rangle_{E_{c(t_1)}}=\langle[q_0,v],[q_0,w]\rangle=\langle v,w\rangle_V=\langle[p_0,v],[p_0,w]\rangle=\langle e,e'\rangle_{E_{c(t_0)}}\qquad\text{(fibre-metric formula at both ends).}$$
> > The middle equality is just $\langle v,w\rangle_V$ read twice, once in the frame $q_0$ and once in the frame $p_0$. Hence $PT_c$ preserves the inner product; being also a linear isomorphism (proved above), it is a linear isometry. $\blacksquare$
>
> An equivalent, purely differential proof runs through the metric-connection identity $\tfrac{d}{dt}\langle s_1,s_2\rangle=\langle\tfrac{\nabla}{dt}s_1,s_2\rangle+\langle s_1,\tfrac{\nabla}{dt}s_2\rangle$: if $s_1,s_2$ are parallel then the right side vanishes, so $\langle s_1(t),s_2(t)\rangle$ is constant, and evaluating at $t_0$ and $t_1$ gives the isometry. For the tangent bundle this is exactly the vault's [[Thm - Parallel Transport is an Isometry for Metric-Compatible Connections|theorem that parallel transport is an isometry for metric-compatible connections]]; the corollary above is its statement for a general associated Euclidean or Hermitian bundle, obtained from equivariance rather than from the metric-compatibility identity. The special cases used in chapter V's holonomy are: $\rho$ orthogonal gives $PT_c\in O(E_m)$, $\rho$ unitary gives $PT_c\in U(E_m)$, and $\rho$ complex-linear gives $PT_c$ complex-linear.

**Is NOT an instance — a nowhere-differentiable base curve.** Parallel transport requires a piecewise smooth (in particular, almost-everywhere differentiable with an integrable velocity) base curve. Consider the map $c\colon[0,1]\to\mathbb R$, $c(t)=\sum_{n\ge0}2^{-n}\cos(3^n\pi t)$ (a Weierstrass function), continuous but nowhere differentiable. There is no velocity $\dot c(t)$ at any $t$, so the horizontality condition $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ has no meaning: the lift ordinary differential equation $\dot h(t)=-dR_{h(t)}(A_\alpha(\dot c(t)))$ has no right-hand side to integrate, because $A_\alpha(\dot c(t))$ is undefined. Parallel transport along $c$ is therefore not defined at all — not merely hard to compute. (One can define transport along continuous curves of bounded variation by a limiting or Riemann–Stieltjes procedure, but that is a genuine extension of the notion, requiring $c$ to have finite length; the bare continuity of the Weierstrass path is not enough, and this is why the definition fixes the class of curves as the piecewise smooth ones.)

**Calibration check.** First, transport along a constant curve is the identity (verified above), so the functor $\mathcal T_\omega$ sends the identity morphism at $m$ to the identity of $P_m$ — the minimal consistency requirement. Second, on the product bundle $M\times G$ with the product connection, $\Gamma_c(m,g)=(c(t_1),g)$ depends only on the endpoint, not on the path $c$, because that connection is flat; this is the calibration that nontrivial path-dependence of $\Gamma_c$ (as in the flat circle bundle above, where the loop transport $e^{-2\pi ia}$ differs from the identity) is a curvature-or-topology phenomenon, absent exactly when the transport reduces to the naive one. Third, in the flat circle example the transport around the reversed loop $c^{-1}(\theta)=e^{-i\theta}$ solves $\dot s-ia\,s=0$, giving $s(2\pi)=e^{+2\pi ia}s_0=(PT_c)^{-1}s_0$, confirming that transport along the reversed curve is the inverse — a check that $\Gamma_c$ really is a torsor isomorphism and not merely a map.

---

# Unlocked by This

> [!tip] Holonomy group *(from Gauge Theory V)*
> Restricting parallel transport to loops based at a point $m$ and reading each $\Gamma_c$ as right multiplication by a group element defines the [[Def - Holonomy Group of a Connection|holonomy group]] $\operatorname{Hol}_p(\omega)\subset G$: the subgroup of all $g$ with $\Gamma_c(p)=p\cdot g$ for some loop $c$. The linear-isometry corollary above is what forces $\operatorname{Hol}$ into $O(k)$ or $U(k)$ for metric and Hermitian connections.

> [!tip] Path-ordered exponential *(from Gauge Theory V)*
> On a matrix structure group the transport equation $\dot s+\mathcal A(t)s=0$ is solved in closed form by the [[Def - Path-Ordered Exponential|path-ordered exponential]] $\mathcal P\exp\!\big(-\!\int_c A_\alpha\big)$, the Dyson series whose noncommutativity is exactly the ordering that curvature obstructs.

> [!tip] Flat connections and monodromy *(from Gauge Theory V)*
> When the curvature vanishes, parallel transport depends only on the homotopy class of the curve, and $[c]\mapsto\operatorname{hol}(c)$ becomes the **monodromy representation** $\pi_1(M)\to G$ — the bridge, via [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the monodromy correspondence]], between flat connections and representations of the fundamental group.

> [!tip] Properties of parallel transport *(from Gauge Theory V)*
> Concatenation $\Gamma_{c_2*c_1}=\Gamma_{c_2}\circ\Gamma_{c_1}$, reparametrisation invariance, the inverse under orientation reversal, and commutation with the right action are collected and proved on [[Thm - Properties of Parallel Transport|the properties page]]; they are what promote the path category into a groupoid and the assignment $\mathcal T_\omega$ into a genuine functor.
