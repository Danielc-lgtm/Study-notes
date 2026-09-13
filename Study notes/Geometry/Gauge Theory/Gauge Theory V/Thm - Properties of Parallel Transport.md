---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Parallel Transport in a Principal Bundle"
  - "Def - Euclidean Vector Bundle and Metric Connection"
  - "Thm - Existence and Uniqueness of Horizontal Lifts"
tags: [geometry, gauge-theory]
---

# Notation

This page collects the structural properties of parallel transport determined by a principal connection. We use throughout the standing conventions of the series: **Lie groups act on principal bundles on the right**, $R_g(p)=p\cdot g$; $\Gamma(E)$ denotes smooth sections; a curve means a piecewise smooth map from a compact interval.

Throughout, $\pi\colon P\to M$ is a smooth [[Def - Connection on a Principal Bundle|principal $G$-bundle]] over a smooth manifold $M$, with $G$ a Lie group acting on the right, and $\omega\in\Omega^1(P;\mathfrak g)$ is a fixed [[Def - Connection on a Principal Bundle|connection]], where $\mathfrak g=T_eG$ is the Lie algebra. Its [[Def - Horizontal Subspace and Horizontal Lift|horizontal subspace]] at $p\in P$ is $H_p:=\ker\omega_p\subset T_pP$, a $G$-invariant complement of the vertical space $V_p:=\ker d\pi_p$: at each point $T_pP=H_p\oplus V_p$, and the invariance is the identity
$$dR_g(H_p)=H_{p\cdot g}\qquad\text{for all }p\in P,\ g\in G,$$
which we invoke by name as the **$G$-invariance of the horizontal distribution**. For $m\in M$ the fibre $P_m:=\pi^{-1}(m)$ is a right $G$-torsor: the action of $G$ on $P_m$ is free and transitive.

A **curve** is a piecewise smooth map $c\colon[t_0,t_1]\to M$; its velocity $\dot c(t)\in T_{c(t)}M$ exists off the finitely many corners. A curve $\tilde c\colon[t_0,t_1]\to P$ is a **lift** of $c$ if $\pi\circ\tilde c=c$, and a **horizontal lift** if in addition $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ wherever the velocity exists. By [[Thm - Existence and Uniqueness of Horizontal Lifts|the existence and uniqueness of horizontal lifts]] (restated in the Statement), a horizontal lift exists on the whole interval and is uniquely determined by its initial point $\tilde c(t_0)=p$.

The [[Def - Parallel Transport in a Principal Bundle|parallel transport along $c$]] is the map
$$\Gamma_c\colon P_{c(t_0)}\longrightarrow P_{c(t_1)},\qquad \Gamma_c(p):=\tilde c(t_1),$$
where $\tilde c$ is the horizontal lift of $c$ with $\tilde c(t_0)=p$. Given a [[Def - Representation of a Lie Group|representation]] $\rho\colon G\to GL(V)$ on a finite-dimensional real or complex vector space $V$, the [[Def - Associated Bundle|associated vector bundle]] is $E=P\times_\rho V=(P\times V)/G$ with $(p,v)\cdot g=(p\cdot g,\rho(g)^{-1}v)$, classes written $[p,v]$ (so $[p\cdot g,\rho(g)^{-1}v]=[p,v]$), and the [[Def - Parallel Transport in a Principal Bundle|induced parallel transport]] on $E$ is
$$PT_c\colon E_{c(t_0)}\longrightarrow E_{c(t_1)},\qquad PT_c\big([p,v]\big):=[\Gamma_c(p),v].$$
For each fixed $p\in P_m$ the map $\iota_p\colon V\to E_m$, $v\mapsto[p,v]$, is a linear isomorphism (definition of the associated bundle). We write $k=\dim_{\mathbb R}E_m$ for the real rank of $E$; for a complex bundle of complex rank $m$ we have $k=2m$.

A **reparametrisation** of $[t_0,t_1]$ is a piecewise smooth homeomorphism $\phi\colon[a,b]\to[t_0,t_1]$ whose derivative is nowhere zero on each smooth piece; it is **orientation-preserving** if $\dot\phi>0$ (so $\phi(a)=t_0$, $\phi(b)=t_1$) and **orientation-reversing** if $\dot\phi<0$ (so $\phi(a)=t_1$, $\phi(b)=t_0$). For a curve $c_1\colon[t_0,t_1]\to M$ and $c_2\colon[t_1,t_2]\to M$ with $c_1(t_1)=c_2(t_1)$, the **concatenation** $c_2*c_1\colon[t_0,t_2]\to M$ is the piecewise smooth curve equal to $c_1$ on $[t_0,t_1]$ and to $c_2$ on $[t_1,t_2]$ (first $c_1$, then $c_2$).

> [!warning] Convention: names for parallel transport, and the two sources
> Bär writes $\Gamma(c)\colon P_{c(t_0)}\to P_{c(t_1)}$ for the principal-bundle map and states properties (1)–(5) below in his Remark 2.6.5; his Remark 2.6.6 is our property (7). Haydys writes $PT_\gamma$ for the induced map on a vector bundle and states the isometry/unitary/complex-linear content as his Exercise 102. **This series writes $\Gamma_c$ on $P$ and $PT_c$ on the associated bundle $E$.** Where Haydys writes $\operatorname{Hol}(\nabla)\subset U(k/2)$ for a complex Hermitian bundle, the $k$ is the real rank, so $U(k/2)=U(m)$ with $m$ the complex rank; we write $U(m)$ and note the identification.

---

# Statement

> **Theorem (Properties of parallel transport).** Let $\omega$ be a connection on the principal $G$-bundle $\pi\colon P\to M$, and let all curves below be piecewise smooth. Parallel transport has the following properties.
> 1. **(Constant curve.)** If $c\equiv m$ is constant, then $\Gamma_c=\operatorname{id}_{P_m}$.
> 2. **(Orientation-preserving reparametrisation.)** If $c'=c\circ\phi$ with $\phi$ an orientation-preserving reparametrisation, then $\Gamma_{c'}=\Gamma_c$.
> 3. **(Orientation reversal.)** If $c'=c\circ\phi$ with $\phi$ an orientation-reversing reparametrisation, then $\Gamma_{c'}=\Gamma_c^{-1}$. In particular $\Gamma_c$ is a diffeomorphism $P_{c(t_0)}\to P_{c(t_1)}$.
> 4. **(Concatenation.)** For composable curves $c_1\colon[t_0,t_1]\to M$ and $c_2\colon[t_1,t_2]\to M$ with $c_1(t_1)=c_2(t_1)$, $\Gamma_{c_2*c_1}=\Gamma_{c_2}\circ\Gamma_{c_1}$.
> 5. **(Equivariance.)** For every $g\in G$, $\Gamma_c\circ R_g=R_g\circ\Gamma_c$, that is, $\Gamma_c(p\cdot g)=\Gamma_c(p)\cdot g$.
> 6. **(Associated vector bundle.)** For an associated bundle $E=P\times_\rho V$, the induced parallel transport $PT_c\colon E_{c(t_0)}\to E_{c(t_1)}$ is a linear isomorphism. If $\rho$ preserves an inner product on $V$ — equivalently, if $\nabla=\nabla^\omega$ is a metric connection (real case) or a Hermitian connection (complex case) — then $PT_c$ is a linear isometry; choosing an orthonormal basis of $E_{c(t_0)}$ and its parallel transport as an orthonormal basis of $E_{c(t_1)}$, $PT_c$ is represented by a matrix in $O(k)$ (real case) or $U(m)$ (complex Hermitian case, $k=2m$). If $V$ is complex and $\rho$ is complex-linear, then $PT_c$ is complex-linear, represented by a matrix in $GL_m(\mathbb C)$.
> 7. **(Path dependence.)** $\Gamma_c$ depends on the curve $c$, not only on its endpoints. Explicitly, there exist connections and pairs of curves with the same endpoints whose parallel transports differ; equivalently, for a closed curve $c$ one has $\Gamma_c\ne\operatorname{id}$ in general. This failure is governed by the [[Def - Curvature of a Principal Connection|curvature]] and by the topology of $M$.

Properties (1)–(5) are the structural identities that make parallel transport a functor from the path category of $M$ to $G$-torsors; property (6) transports them to every associated bundle; property (7) records that the functor is genuinely non-trivial.

---

# Motivation

Parallel transport is only useful because it composes. A connection assigns to each curve an isomorphism of fibres; if these isomorphisms did not fit together — if transport along a reparametrised curve gave a different answer, if transporting along $c_1$ and then along $c_2$ were unrelated to transporting along the joined curve, if reversing a curve did not undo it — then "transport" would be a name for an unstructured collection of maps and none of the theory built on it (holonomy, the monodromy of flat connections, the free action of the reduced gauge group) could get started. This theorem is the verification that the isomorphisms do fit together, in exactly the way one would demand: transport ignores how fast the curve is traced (2), reverses under reversal (3), composes under concatenation (4), and intertwines the group action (5), reducing to the identity on a curve that does not move (1). In categorical language, properties (1)–(4) say that the assignment $c\mapsto\Gamma_c$ is a functor from the groupoid of piecewise smooth paths in $M$ (points as objects, curves up to reparametrisation as morphisms, reversal as inverse) into the category of right $G$-torsors, and property (5) says the functor lands in *equivariant* maps of torsors rather than mere maps of sets.

The importance of property (5) deserves separate emphasis, because it is the reason one works on the principal bundle at all. A single horizontal lift transports not one object but every object associated to $P$ — a tangent vector, a whole frame, a spinor, a section of an endomorphism bundle — all at once and coherently, precisely because $\Gamma_c$ commutes with the structure group. Property (6) cashes this out: because $\Gamma_c$ is equivariant, the induced map $PT_c$ on any associated vector bundle is automatically linear, and when the representation preserves an inner product it is automatically an isometry. No separate computation on each associated bundle is required; the linearity and the isometry are consequences of the equivariance of one map upstairs. This is the mechanism by which the holonomy of a metric connection is forced into the orthogonal group and the holonomy of a Hermitian connection into the unitary group — the fact that turns curvature into a constraint on which groups can arise as holonomy, and ultimately into the Ambrose–Singer theorem and the reduction theory of connections.

Property (7) is the counterweight. Having proved that transport is beautifully structured, one must not conclude that it is trivial. Transport around a loop is, in general, *not* the identity, and two paths with the same endpoints need not give the same isomorphism. This path dependence is the entire content of the subject: it is what the [[Def - Holonomy Group of a Connection|holonomy group]] measures, what the [[Def - Curvature of a Principal Connection|curvature]] generates infinitesimally, and what the Aharonov–Bohm effect detects physically. The theorem thus draws the exact line between what is automatic (the algebra of composition) and what is substantive (the geometry of non-closure).

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's hypotheses are minimal — a connection and a piecewise smooth curve — so the "source" question is: which problems secretly present a parallel transport whose properties can then be exploited, and which properties of a curve or a connection unlock which conclusions?

The first disguised source is **a linear ordinary differential equation with a curve of coefficients**. On a matrix structure group or a vector bundle, transport is the solution operator of $\dot s+\mathcal A(t)s=0$, so any first-order linear system $\dot s=B(t)s$ is a parallel transport for the connection with local form $\mathcal A=-B$. The bridge $B\Rightarrow A$ is: "this evolution operator is $PT_c$", after which properties (2)–(4) become the reparametrisation invariance, the reversibility, and the multiplicativity of the solution operator, and property (6) becomes the statement that the solution operator of a skew-Hermitian system is unitary. *Example problem:* show that the time-ordered evolution operator $U(t_1,t_0)$ of a Schrödinger equation $i\hbar\dot\psi=H(t)\psi$ with Hermitian $H(t)$ is unitary and satisfies $U(t_2,t_0)=U(t_2,t_1)U(t_1,t_0)$ — this is properties (6) and (4) for the connection $\mathcal A=iH/\hbar$ on the trivial Hermitian bundle over the time interval.

The second disguised source is **a connection whose representation preserves extra structure**. Whenever the structure group is a subgroup of the isometry, unitary, or complex-linear group of the model fibre — an $O(k)$-, $U(m)$-, or $GL_m(\mathbb C)$-connection — property (6) applies without one having to notice the connection "is metric". The bridge is that a reduction of the structure group *is* an invariant inner product or complex structure on the associated bundle preserved by the connection. *Example problem:* deduce that parallel transport for the Levi-Civita connection preserves the Riemannian metric on $TM$, directly from the fact that its structure group reduces to $O(n)$, without recomputing $\tfrac{d}{dt}\langle s_1,s_2\rangle$.

The third disguised source is **a covering space, read as a flat discrete-group bundle**. A covering $\tilde M\to M$ is a principal bundle with discrete structure group and a unique (flat) connection whose horizontal lifts are the path lifts; its parallel transport along a loop is the deck transformation the loop induces. Properties (4) and (5) then reproduce the fact that path lifting is a groupoid morphism and that the monodromy action is a group action. The bridge $B\Rightarrow A$ is "a covering is a bundle with a connection whose transport is path lifting". *Example problem:* show that lifting loops in $S^1$ to $\mathbb R$ gives a homomorphism $\pi_1(S^1)\to\mathbb Z$ using property (4); this is the covering-space shadow of concatenation of parallel transports.

**Targets (Output Amplification)**

Combine properties (4) and (3) with **restriction to loops based at a point** and one obtains that the [[Def - Holonomy Group of a Connection|holonomy]] $\operatorname{Hol}_p(\omega)=\{g:\Gamma_c(p)=p\cdot g\ \text{for some loop }c\}$ is a subgroup of $G$: concatenation gives closure under multiplication, reversal gives closure under inverses, and the constant loop gives the identity. The extra ingredient is the group $G$ acting on the fibre; the payoff is that holonomy is not a mere set of maps but a group, the foundation of the entire holonomy classification.

Combine property (6) with **a metric or Hermitian reduction of the structure group** and one obtains the containment $\operatorname{Hol}(\nabla)\subset O(k)$ (metric case) and $\operatorname{Hol}(\nabla)\subset U(m)$ (Hermitian case), and $\operatorname{Hol}(\nabla)\subset GL_m(\mathbb C)$ for a complex connection. The extra ingredient is the choice of a basis of the fibre identifying the isometry group with a matrix group; the payoff is Haydys's Exercise 102 and the first constraint theorem on holonomy groups, from which the local reduction theory proceeds.

Combine property (7) with **the abelian holonomy formula and Stokes' theorem** and one obtains that the non-closure of transport around a small loop is, to leading order, the flux of the curvature through the loop: $\Gamma_c\approx\operatorname{id}-\int_S F$. The extra ingredient is the [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|abelian holonomy computation]] (and its non-abelian refinement); the payoff is the identification of curvature as infinitesimal holonomy, the geometric meaning of the field strength $F_{\mu\nu}$ in gauge theory.

---

# Why Is It True

Every one of properties (1)–(5) is a restatement of a single fact: **a horizontal lift stays a horizontal lift under the operations one performs on curves, so parallel transport inherits whatever those operations do to endpoints.** Reparametrise the base curve and the lift reparametrises with it — because horizontality is a condition on the *direction* of the velocity, not its magnitude, and reparametrising only rescales the velocity, which cannot leave the linear subspace $H$. Reverse the curve and the lift reverses, now starting from the old endpoint, so transport reverses. Concatenate two curves and glue the two horizontal lifts at the shared point — the glued curve is horizontal on each piece and projects correctly, so by uniqueness it *is* the horizontal lift of the joined curve, and its endpoint is the composite. Translate the starting point by $g$ and, because the horizontal distribution is $G$-invariant, the whole lift translates by $g$, so transport commutes with the action. In each case one does not compute transport; one recognises that a manipulated horizontal lift is again the horizontal lift of the manipulated curve, and reads off the endpoint. Uniqueness of horizontal lifts is the engine that turns "is a horizontal lift" into "is the horizontal lift", and hence into an equality of transports.

Property (6) is the same recognition pushed through the associated-bundle construction. Fix one point $p_0$ of the starting fibre; it determines a linear frame $\iota_{p_0}\colon V\to E_{c(t_0)}$, and its transport $q_0=\Gamma_c(p_0)$ determines a linear frame $\iota_{q_0}\colon V\to E_{c(t_1)}$. In these two frames, $PT_c$ *is the identity of $V$*: it sends $[p_0,v]$ to $[q_0,v]$. So $PT_c=\iota_{q_0}\circ\iota_{p_0}^{-1}$ is a composite of two linear isomorphisms, hence linear; and if $V$ carries a $\rho$-invariant inner product, both frames are "orthonormal" for the induced fibre metrics, so the map that is the identity of $V$ in these frames is an isometry. Linearity and the isometry are not computed; they are visible the instant one writes transport in a transported frame.

> **The whole theorem is one sentence: parallel transport is the endpoint of a horizontal lift, and a horizontal lift is preserved by reparametrisation, reversal, concatenation, and the group action — so transport inherits exactly the endpoint behaviour of those operations.**

Property (7) is true because horizontality is a genuinely non-integrable constraint: the horizontal subspaces do not in general fit together into the tangent spaces of a family of surfaces, so a lift that goes out and comes back along a loop need not return to where it started in the fibre. The precise measure of this failure is the curvature $F=d\omega+\tfrac12[\omega\wedge\omega]$; where it is non-zero, small loops already have non-trivial transport, and even where it vanishes, a topologically non-trivial loop can transport non-trivially (the flat circle bundle below). The one place transport depends only on endpoints is a flat connection on a simply connected base.

---

# What Makes This Hard

There is little computation; the difficulty is entirely in the discipline of the horizontal-lift argument. The non-obvious step is that reparametrisation and reversal preserve horizontality *because $H$ is a linear subspace closed under scalar multiplication* — including multiplication by the negative scalar $\dot\phi<0$ of an orientation-reversing $\phi$; a reader who pictures horizontality as "pointing forward along the curve" will wrongly expect reversal to break it. The common error in property (4) is to forget that uniqueness of horizontal lifts must be invoked to identify the glued curve with *the* lift of the concatenation: gluing produces *a* horizontal lift, and only uniqueness upgrades "a" to "the". The common error in property (6) is to try to prove the isometry by differentiating $\langle s_1,s_2\rangle$ and juggling connection terms, when the equivariant-frame argument makes it immediate; the differential proof works but hides why the result is forced. Finally, property (7) must be stated carefully: transport depends on the curve, but by property (2) it depends only on the *unparametrised, oriented* curve, so the honest statement of path dependence is that it depends on the oriented curve up to reparametrisation, and this dependence is non-trivial.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For (1)–(5), never compute a transport; instead manufacture, from the horizontal lift $\tilde c$ of $c$, a curve that is manifestly a horizontal lift of the manipulated curve $c'$, check its initial point, and invoke uniqueness to conclude it is *the* lift of $c'$; read off the endpoint. For (6), write $PT_c$ in a transported frame, where it becomes the identity of the model fibre. For (7), exhibit one flat connection on a non-simply-connected base whose loop transport is not the identity.

**Subgoal decomposition:**

1. **Reparametrisation lemma.** Show that if $\tilde c$ is a horizontal lift of $c$ then $\tilde c\circ\phi$ is a horizontal lift of $c\circ\phi$, for any reparametrisation $\phi$.
   - *Hint:* Chain rule gives $\dot{(\tilde c\circ\phi)}(t)=\dot\phi(t)\,\dot{\tilde c}(\phi(t))$; use that $H$ is a linear subspace.
   - *Why needed:* Properties (2) and (3) are this lemma plus a check of the initial point.

2. **Right-translation lemma.** Show that $R_g\circ\tilde c$ is the horizontal lift of $c$ through $p\cdot g$.
   - *Hint:* $\pi\circ R_g=\pi$; velocity is $dR_g(\dot{\tilde c})$; use $G$-invariance $dR_g(H_p)=H_{p\cdot g}$.
   - *Why needed:* Property (5), and the bijectivity of $\Gamma_c$ that upgrades (3) to "diffeomorphism".

3. **Concatenation lemma.** Show that gluing the horizontal lift of $c_1$ to the horizontal lift of $c_2$ started at $\Gamma_{c_1}(p)$ gives the horizontal lift of $c_2*c_1$ through $p$.
   - *Hint:* The glued curve is continuous (endpoints match), horizontal on each piece, and projects to $c_2*c_1$; invoke uniqueness.
   - *Why needed:* Property (4).

4. **Transported-frame lemma.** Show $PT_c=\iota_{q_0}\circ\iota_{p_0}^{-1}$ with $q_0=\Gamma_c(p_0)$, and that a $\rho$-invariant inner product makes both frames isometries.
   - *Hint:* $PT_c([p_0,v])=[q_0,v]=\iota_{q_0}(v)$ and $[p_0,v]=\iota_{p_0}(v)$.
   - *Why needed:* Property (6): linearity, isometry, complex-linearity all read off this factorisation.

5. **A non-trivial loop.** Compute transport once around the flat circle bundle with connection $ia\,d\theta$.
   - *Hint:* Solve $\dot s+ia\,s=0$ on $[0,2\pi]$.
   - *Why needed:* Property (7): a loop (equal endpoints) with transport $e^{-2\pi ia}\ne\operatorname{id}$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Reparametrisation preserves horizontal lifts
> **Statement:** Let $\tilde c\colon[t_0,t_1]\to P$ be a horizontal lift of $c\colon[t_0,t_1]\to M$, and let $\phi\colon[a,b]\to[t_0,t_1]$ be a piecewise smooth reparametrisation (orientation-preserving or reversing). Then $\tilde c\circ\phi$ is a horizontal lift of $c\circ\phi$.
>
> **Hint:** By the chain rule the velocity of $\tilde c\circ\phi$ is a scalar multiple of the velocity of $\tilde c$; a linear subspace absorbs scalar multiples of any sign.
>
> **Why needed:** It is the single computational fact behind properties (2) and (3); combined with a check of the initial point it gives both.
>
> > [!note]- Full proof
> > **What we assume and show.** We are given that $\tilde c$ is a horizontal lift, so $\pi\circ\tilde c=c$ and $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ off the corners of $\tilde c$. We must show $\tilde c\circ\phi$ is a lift of $c\circ\phi$ and is horizontal.
> >
> > **It is a lift.** Composing with $\pi$,
> > $$\pi\circ(\tilde c\circ\phi)=(\pi\circ\tilde c)\circ\phi=c\circ\phi\qquad\text{(since }\pi\circ\tilde c=c\text{).}$$
> > So $\tilde c\circ\phi$ projects to $c\circ\phi$; being a composite of piecewise smooth maps it is piecewise smooth.
> >
> > **It is horizontal.** Fix a point $t\in[a,b]$ that is not a corner of $\phi$ and where $\phi(t)$ is not a corner of $\tilde c$ (all but finitely many $t$). By the chain rule,
> > $$\frac{d}{dt}\big(\tilde c\circ\phi\big)(t)=\dot\phi(t)\,\dot{\tilde c}(\phi(t))\qquad\text{(chain rule; }\dot\phi(t)\in\mathbb R\text{ is a scalar).}$$
> > Now $\dot{\tilde c}(\phi(t))\in H_{\tilde c(\phi(t))}$ (horizontality of $\tilde c$ at the point $\phi(t)$), and $H_{\tilde c(\phi(t))}=H_{(\tilde c\circ\phi)(t)}$ is a **linear subspace** of the tangent space (a connection's horizontal subspaces are $\ker\omega$, a linear subspace). A linear subspace is closed under multiplication by any scalar, including the possibly negative $\dot\phi(t)$; hence
> > $$\dot\phi(t)\,\dot{\tilde c}(\phi(t))\in H_{(\tilde c\circ\phi)(t)}\qquad\text{(a linear subspace absorbs scalar multiples, of either sign).}$$
> > Therefore $\tfrac{d}{dt}(\tilde c\circ\phi)(t)\in H_{(\tilde c\circ\phi)(t)}$ off the finitely many exceptional points, so $\tilde c\circ\phi$ is horizontal. Hence $\tilde c\circ\phi$ is a horizontal lift of $c\circ\phi$. $\blacksquare$

> [!note]- Lemma 2: The right-translate of a horizontal lift is the horizontal lift through the translated point
> **Statement:** Let $\tilde c$ be the horizontal lift of $c$ with $\tilde c(t_0)=p$, and let $g\in G$. Then $R_g\circ\tilde c$ (that is, $t\mapsto\tilde c(t)\cdot g$) is the horizontal lift of $c$ with initial point $p\cdot g$.
>
> **Hint:** Check the three defining clauses of a horizontal lift for $R_g\circ\tilde c$, using $\pi\circ R_g=\pi$ and the $G$-invariance $dR_g(H_p)=H_{p\cdot g}$.
>
> **Why needed:** It gives the equivariance (property 5) directly, and the bijectivity of $\Gamma_c$ needed to call it a diffeomorphism in property (3).
>
> > [!note]- Full proof
> > **What we assume and show.** We assume $\tilde c$ is horizontal with $\tilde c(t_0)=p$, and that the connection's horizontal distribution is $G$-invariant, $dR_g(H_q)=H_{q\cdot g}$ for all $q,g$. We show $R_g\circ\tilde c$ satisfies the three clauses defining the horizontal lift of $c$ through $p\cdot g$; uniqueness then identifies it as that lift.
> >
> > **Clause (i): it projects to $c$.** Since $R_g$ preserves fibres, $\pi\circ R_g=\pi$, so
> > $$\pi\circ(R_g\circ\tilde c)=(\pi\circ R_g)\circ\tilde c=\pi\circ\tilde c=c\qquad\text{(}\pi(q\cdot g)=\pi(q)\text{ as the action is along fibres).}$$
> >
> > **Clause (ii): it is horizontal.** Off the corners of $\tilde c$, the chain rule gives $\tfrac{d}{dt}(R_g\circ\tilde c)(t)=dR_g\big(\dot{\tilde c}(t)\big)$. Since $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ (horizontality of $\tilde c$),
> > $$dR_g\big(\dot{\tilde c}(t)\big)\in dR_g\big(H_{\tilde c(t)}\big)=H_{\tilde c(t)\cdot g}=H_{(R_g\circ\tilde c)(t)}\qquad\text{(}G\text{-invariance of the horizontal distribution).}$$
> > So $R_g\circ\tilde c$ is horizontal.
> >
> > **Clause (iii): its initial point.** $(R_g\circ\tilde c)(t_0)=\tilde c(t_0)\cdot g=p\cdot g$ (definition of $R_g$; $\tilde c(t_0)=p$).
> >
> > **Conclusion.** $R_g\circ\tilde c$ is a horizontal lift of $c$ with initial point $p\cdot g$. By the uniqueness clause of [[Thm - Existence and Uniqueness of Horizontal Lifts|the existence and uniqueness of horizontal lifts]], it is *the* horizontal lift of $c$ through $p\cdot g$. $\blacksquare$

> [!note]- Lemma 3: Horizontal lifts glue under concatenation
> **Statement:** Let $c_1\colon[t_0,t_1]\to M$ and $c_2\colon[t_1,t_2]\to M$ be composable, $c_1(t_1)=c_2(t_1)$. Let $\tilde c_1$ be the horizontal lift of $c_1$ through $p$, and $\tilde c_2$ the horizontal lift of $c_2$ through $\tilde c_1(t_1)$. Then the curve $\tilde c\colon[t_0,t_2]\to P$ equal to $\tilde c_1$ on $[t_0,t_1]$ and to $\tilde c_2$ on $[t_1,t_2]$ is the horizontal lift of $c_2*c_1$ through $p$.
>
> **Hint:** The glue is continuous because $\tilde c_1(t_1)=\tilde c_2(t_1)$ by construction; it is horizontal on each smooth piece; invoke uniqueness for piecewise smooth curves.
>
> **Why needed:** It is property (4).
>
> > [!note]- Full proof
> > **What we assume and show.** We assume $\tilde c_1$ is horizontal over $c_1$ with $\tilde c_1(t_0)=p$, and $\tilde c_2$ is horizontal over $c_2$ with $\tilde c_2(t_1)=\tilde c_1(t_1)$. We must show the glued curve $\tilde c$ is well defined, is a horizontal lift of $c_2*c_1$, and starts at $p$.
> >
> > **Well-defined and continuous.** The two pieces agree at the shared point $t_1$: $\tilde c_1(t_1)=\tilde c_2(t_1)$ by the choice of $\tilde c_2$'s initial point. Hence $\tilde c$ is a single continuous, piecewise smooth map $[t_0,t_2]\to P$.
> >
> > **It is a lift of $c_2*c_1$.** On $[t_0,t_1]$, $\pi\circ\tilde c=\pi\circ\tilde c_1=c_1=(c_2*c_1)|_{[t_0,t_1]}$; on $[t_1,t_2]$, $\pi\circ\tilde c=\pi\circ\tilde c_2=c_2=(c_2*c_1)|_{[t_1,t_2]}$. So $\pi\circ\tilde c=c_2*c_1$ (definition of the concatenation as $c_1$ then $c_2$).
> >
> > **It is horizontal.** On the interior of $[t_0,t_1]$ its velocity is $\dot{\tilde c_1}\in H$; on the interior of $[t_1,t_2]$ its velocity is $\dot{\tilde c_2}\in H$; the point $t_1$ is one of the finitely many corners at which horizontality is not required. Hence $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ off the corners.
> >
> > **Its initial point.** $\tilde c(t_0)=\tilde c_1(t_0)=p$.
> >
> > **Conclusion.** $\tilde c$ is a horizontal lift of $c_2*c_1$ with initial point $p$; by the uniqueness clause of [[Thm - Existence and Uniqueness of Horizontal Lifts|the existence and uniqueness of horizontal lifts]] (which admits piecewise smooth curves), it is the horizontal lift of $c_2*c_1$ through $p$. $\blacksquare$

> [!note]- Lemma 4: Parallel transport is the identity of the fibre read in a transported frame
> **Statement:** Let $E=P\times_\rho V$ and fix $p_0\in P_{c(t_0)}$, $q_0:=\Gamma_c(p_0)\in P_{c(t_1)}$. With the linear frames $\iota_{p_0}\colon V\to E_{c(t_0)}$, $v\mapsto[p_0,v]$, and $\iota_{q_0}\colon V\to E_{c(t_1)}$, $v\mapsto[q_0,v]$, one has
> $$PT_c=\iota_{q_0}\circ\iota_{p_0}^{-1}.$$
> Consequently $PT_c$ is a linear isomorphism. If moreover $V$ carries a $\rho$-invariant inner product $\langle\cdot,\cdot\rangle_V$ and $E$ its induced fibre metric, then $PT_c$ is a linear isometry; if $V$ is complex and $\rho$ is complex-linear, then $PT_c$ is complex-linear.
>
> **Hint:** $PT_c([p_0,v])=[\Gamma_c(p_0),v]=[q_0,v]$; both $\iota_{p_0},\iota_{q_0}$ are linear isomorphisms by definition of the associated bundle.
>
> **Why needed:** It is the whole of property (6).
>
> > [!note]- Full proof
> > **What we assume and show.** We use only the definition $PT_c([p,v])=[\Gamma_c(p),v]$ and the fact that $\iota_p\colon v\mapsto[p,v]$ is a linear isomorphism $V\to E_{\pi(p)}$ for each $p$ (definition of the associated vector bundle). We prove the factorisation and its three consequences.
> >
> > **The factorisation.** Every $e\in E_{c(t_0)}$ is $e=[p_0,v]=\iota_{p_0}(v)$ for the unique $v=\iota_{p_0}^{-1}(e)\in V$. By the definition of $PT_c$ and $q_0=\Gamma_c(p_0)$,
> > $$PT_c(e)=PT_c([p_0,v])=[\Gamma_c(p_0),v]=[q_0,v]=\iota_{q_0}(v)=\iota_{q_0}\big(\iota_{p_0}^{-1}(e)\big)\qquad\text{(definition of }PT_c\text{; }q_0=\Gamma_c(p_0)\text{).}$$
> > Since $e$ was arbitrary, $PT_c=\iota_{q_0}\circ\iota_{p_0}^{-1}$.
> >
> > **Linear isomorphism.** $\iota_{p_0}^{-1}$ and $\iota_{q_0}$ are linear isomorphisms (inverses and instances of the frame maps), so their composite $PT_c$ is a linear isomorphism.
> >
> > **Isometry.** Suppose $\langle\cdot,\cdot\rangle_V$ is $\rho$-invariant, meaning $\langle\rho(g)v,\rho(g)w\rangle_V=\langle v,w\rangle_V$ for all $g\in G$, $v,w\in V$; the induced fibre metric is $\langle[p,v],[p,w]\rangle_{E}:=\langle v,w\rangle_V$, which is well defined precisely because of $\rho$-invariance (for another representative $[p\cdot g,\rho(g)^{-1}v]$ one gets $\langle\rho(g)^{-1}v,\rho(g)^{-1}w\rangle_V=\langle v,w\rangle_V$). Then for $e=\iota_{p_0}(v)$, $e'=\iota_{p_0}(w)$,
> > $$\langle PT_c(e),PT_c(e')\rangle_{E_{c(t_1)}}=\langle[q_0,v],[q_0,w]\rangle=\langle v,w\rangle_V=\langle[p_0,v],[p_0,w]\rangle=\langle e,e'\rangle_{E_{c(t_0)}}\qquad\text{(fibre-metric formula at both ends).}$$
> > So $PT_c$ preserves the inner product; being a linear isomorphism, it is a linear isometry.
> >
> > **Complex-linearity.** If $V$ is a complex vector space and $\rho\colon G\to GL_{\mathbb C}(V)$ is complex-linear, then each $\iota_p\colon V\to E_{\pi(p)}$ is a complex-linear isomorphism for the complex structure the associated bundle inherits from $V$, hence so is $PT_c=\iota_{q_0}\circ\iota_{p_0}^{-1}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\omega$ be the fixed connection on $\pi\colon P\to M$, and $\tilde c$ always denote the horizontal lift of the curve under discussion through the stated initial point. We prove the seven properties in turn; each uses [[Thm - Existence and Uniqueness of Horizontal Lifts|the existence and uniqueness of horizontal lifts]], restated here for reference.
>
> > [!note] Restatement — existence and uniqueness of horizontal lifts
> > For any piecewise smooth $c\colon I\to M$, any $t_0\in I$, and any $p\in P_{c(t_0)}$, there is a unique piecewise smooth $\tilde c\colon I\to P$ with $\pi\circ\tilde c=c$, $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ off its corners, and $\tilde c(t_0)=p$; it is defined on all of $I$, and for every $g\in G$ the curve $\tilde c\cdot g$ is the horizontal lift through $p\cdot g$.
>
> **Property (1): a constant curve gives the identity.** Let $c\equiv m$ on $[t_0,t_1]$ and $p\in P_m$. The constant curve $\tilde c\equiv p$ satisfies $\pi\circ\tilde c\equiv m=c$, has velocity $\dot{\tilde c}\equiv0$, and $0\in H_p$ because $H_p$ is a linear subspace (so it contains the zero vector); its initial point is $p$. Hence $\tilde c\equiv p$ is a horizontal lift of $c$ through $p$, and by uniqueness it is *the* horizontal lift. Therefore
> $$\Gamma_c(p)=\tilde c(t_1)=p\qquad\text{(the lift is the constant curve at }p\text{),}$$
> for every $p\in P_m$, so $\Gamma_c=\operatorname{id}_{P_m}$.
>
> **Property (2): orientation-preserving reparametrisation.** Let $c'=c\circ\phi$ with $\phi\colon[a,b]\to[t_0,t_1]$ orientation-preserving, so $\phi(a)=t_0$ and $\phi(b)=t_1$. Fix $p\in P_{c(t_0)}=P_{c'(a)}$ and let $\tilde c$ be the horizontal lift of $c$ through $p$. By **Lemma 1**, $\tilde c':=\tilde c\circ\phi$ is a horizontal lift of $c'$; its initial point is
> $$\tilde c'(a)=\tilde c(\phi(a))=\tilde c(t_0)=p\qquad\text{(}\phi(a)=t_0\text{, orientation-preserving).}$$
> By uniqueness, $\tilde c'$ is *the* horizontal lift of $c'$ through $p$. Its endpoint is
> $$\Gamma_{c'}(p)=\tilde c'(b)=\tilde c(\phi(b))=\tilde c(t_1)=\Gamma_c(p)\qquad\text{(}\phi(b)=t_1\text{).}$$
> As $p$ was arbitrary, $\Gamma_{c'}=\Gamma_c$.
>
> **Property (3): orientation reversal.** Let $c'=c\circ\phi$ with $\phi\colon[a,b]\to[t_0,t_1]$ orientation-reversing, so $\phi(a)=t_1$ and $\phi(b)=t_0$; note $c'$ runs from $c(t_1)$ to $c(t_0)$. Fix $p\in P_{c(t_0)}$ and let $\tilde c$ be the horizontal lift of $c$ through $p$, so $\Gamma_c(p)=\tilde c(t_1)$. By **Lemma 1**, $\tilde c':=\tilde c\circ\phi$ is a horizontal lift of $c'$; its initial point is
> $$\tilde c'(a)=\tilde c(\phi(a))=\tilde c(t_1)=\Gamma_c(p)\qquad\text{(}\phi(a)=t_1\text{, orientation-reversing).}$$
> By uniqueness $\tilde c'$ is the horizontal lift of $c'$ through $\Gamma_c(p)$, and its endpoint is
> $$\Gamma_{c'}\big(\Gamma_c(p)\big)=\tilde c'(b)=\tilde c(\phi(b))=\tilde c(t_0)=p\qquad\text{(}\phi(b)=t_0\text{).}$$
> Since $p\in P_{c(t_0)}$ was arbitrary, $\Gamma_{c'}\circ\Gamma_c=\operatorname{id}_{P_{c(t_0)}}$. The map $\Gamma_c$ is a bijection (it is $G$-equivariant between $G$-torsors by property (5), proved below independently of this, and an equivariant map of torsors is a bijection); composing the identity $\Gamma_{c'}\circ\Gamma_c=\operatorname{id}$ on the right with $\Gamma_c^{-1}$ gives
> $$\Gamma_{c'}=\Gamma_c^{-1}.$$
> **Diffeomorphism.** $\Gamma_c$ is smooth by the smooth dependence of solutions of the horizontal-lift ordinary differential equation on their initial conditions, and its inverse $\Gamma_c^{-1}=\Gamma_{c'}$ is again a parallel transport, hence also smooth by the same theorem. A smooth bijection with smooth inverse is a diffeomorphism, so $\Gamma_c\colon P_{c(t_0)}\to P_{c(t_1)}$ is a diffeomorphism.
>
> **Property (4): concatenation.** Let $c_1\colon[t_0,t_1]\to M$, $c_2\colon[t_1,t_2]\to M$ be composable, $c_1(t_1)=c_2(t_1)$, and fix $p\in P_{c_1(t_0)}$. Let $\tilde c_1$ be the horizontal lift of $c_1$ through $p$, so $\tilde c_1(t_1)=\Gamma_{c_1}(p)$, and let $\tilde c_2$ be the horizontal lift of $c_2$ through $\tilde c_1(t_1)=\Gamma_{c_1}(p)$, so $\tilde c_2(t_2)=\Gamma_{c_2}\big(\Gamma_{c_1}(p)\big)$. By **Lemma 3**, the glued curve $\tilde c$ is the horizontal lift of $c_2*c_1$ through $p$, so
> $$\Gamma_{c_2*c_1}(p)=\tilde c(t_2)=\tilde c_2(t_2)=\Gamma_{c_2}\big(\Gamma_{c_1}(p)\big)\qquad\text{(Lemma 3; the second piece of the glue is }\tilde c_2\text{).}$$
> As $p$ was arbitrary, $\Gamma_{c_2*c_1}=\Gamma_{c_2}\circ\Gamma_{c_1}$.
>
> **Property (5): equivariance.** Fix $p\in P_{c(t_0)}$ and $g\in G$, and let $\tilde c$ be the horizontal lift of $c$ through $p$. By **Lemma 2**, $R_g\circ\tilde c=\tilde c\cdot g$ is the horizontal lift of $c$ through $p\cdot g$. Evaluating at $t_1$,
> $$\Gamma_c(p\cdot g)=(\tilde c\cdot g)(t_1)=\tilde c(t_1)\cdot g=\Gamma_c(p)\cdot g\qquad\text{(Lemma 2; }R_g\text{ evaluated at the endpoint).}$$
> Thus $\Gamma_c(p\cdot g)=\Gamma_c(p)\cdot g$, that is $\Gamma_c\circ R_g=R_g\circ\Gamma_c$. (This is the equivariance invoked in property (3); it is proved here from the $G$-invariance of the horizontal distribution alone, so there is no circularity.)
>
> **Property (6): the associated vector bundle.** Let $E=P\times_\rho V$. By **Lemma 4**, fixing $p_0\in P_{c(t_0)}$ and $q_0=\Gamma_c(p_0)$, the induced parallel transport factors as $PT_c=\iota_{q_0}\circ\iota_{p_0}^{-1}$, a composite of linear isomorphisms; hence $PT_c$ is a **linear isomorphism**. If $\rho$ preserves an inner product on $V$ — equivalently, if the induced connection $\nabla=\nabla^\omega$ is a metric connection (for a Euclidean $V$) or a Hermitian connection (for a Hermitian $V$), which is the case exactly when the structure group reduces to $O(V)$ or $U(V)$ — then by Lemma 4, $PT_c$ is a **linear isometry**. Choosing an orthonormal basis $(f_i)$ of $E_{c(t_0)}$, its image $(PT_c f_i)$ is an orthonormal basis of $E_{c(t_1)}$ (an isometry sends orthonormal bases to orthonormal bases), and in these two bases $PT_c$ is represented by the identity matrix; more usefully, transporting a *fixed* reference orthonormal frame along $c$ and comparing with a chosen orthonormal frame at the endpoint represents $PT_c$ by a matrix in $O(k)$ (real, $k=\dim_{\mathbb R}E_m$) or $U(m)$ (complex Hermitian, $k=2m$). If $V$ is complex and $\rho$ is complex-linear, Lemma 4 gives that $PT_c$ is **complex-linear**, represented by a matrix in $GL_m(\mathbb C)$. These are exactly the three implications of Haydys's Exercise 102; the further conclusions $\operatorname{Hol}\subset O(k)$, $\operatorname{Hol}\subset U(m)$, $\operatorname{Hol}\subset GL_m(\mathbb C)$ follow by restricting to loops and are recorded on [[Def - Holonomy Group of a Connection|the holonomy page]].
>
> **Property (7): path dependence.** We exhibit a connection and a curve with equal endpoints whose transport is not the identity. Take the trivial Hermitian line bundle $E=S^1\times\mathbb C$ over the circle $S^1=\{e^{i\theta}:\theta\in\mathbb R/2\pi\mathbb Z\}$, with the $U(1)$-connection $\nabla=d+ia\,d\theta$ for a fixed real constant $a\notin\mathbb Z$ (its principal form lives on $S^1\times U(1)$). Consider the loop $c(\theta)=e^{i\theta}$, $\theta\in[0,2\pi]$, which has equal endpoints $c(0)=c(2\pi)=1$. A section $s\colon[0,2\pi]\to\mathbb C$ is parallel along $c$ iff $\dot s(\theta)+ia\,s(\theta)=0$ (the connection matrix along $c$ is the constant $\mathcal A=ia$), whose solution with $s(0)=s_0$ is $s(\theta)=e^{-ia\theta}s_0$ (verify: $\dot s=-ia\,e^{-ia\theta}s_0=-ia\,s$). Hence
> $$PT_c(s_0)=s(2\pi)=e^{-2\pi ia}s_0,\qquad\text{so}\qquad PT_c=e^{-2\pi ia}\cdot\operatorname{id}\ne\operatorname{id}\quad(a\notin\mathbb Z).$$
> But transport along the **constant** curve at the base point $1$, which has the *same* endpoints as $c$, is $\operatorname{id}$ by property (1). Two curves with equal endpoints therefore give different transports: $\Gamma_c$ genuinely depends on the curve, not only on its endpoints. Equivalently, for the closed curve $c$ we have $\Gamma_c\ne\operatorname{id}$. That this occurs even though the curvature $F=d(ia\,d\theta)=0$ vanishes shows the dependence is topological here (the circle is not simply connected); on the [[Ex - Parallel Transport in the Hopf Bundle along a Great Circle|Hopf connection]], where $F\ne0$, transport around a great circle is $-\operatorname{id}$, and the general link between non-closure and curvature is made quantitative by [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy theorem]].
>
> This completes the proof of all seven properties. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Time-ordered evolution in quantum mechanics.** The Schrödinger equation $i\hbar\,\dot\psi(t)=H(t)\psi(t)$ with a time-dependent Hermitian Hamiltonian $H(t)$ is the parallel-transport equation $\dot\psi+\mathcal A(t)\psi=0$ for the connection $\mathcal A=iH/\hbar$ on the trivial Hermitian bundle over the time axis. Property (4) is the group law $U(t_2,t_0)=U(t_2,t_1)U(t_1,t_0)$ of the evolution operator, property (6) is its unitarity (because $iH/\hbar$ is skew-Hermitian, so $\mathcal A$ preserves the Hermitian inner product), and property (3) is the reversibility $U(t_0,t_1)=U(t_1,t_0)^{-1}$. The theorem applies because the evolution operator *is* a parallel transport; the non-obvious part is recognising the abstract structure in a piece of physics usually derived by hand, and seeing that unitarity is a corollary of equivariance rather than a separate calculation.

**The monodromy of a linear ordinary differential equation on the punctured plane.** For a linear system $\dot y=B(z)y$ with $B$ holomorphic on $\mathbb C\setminus\{0\}$, analytic continuation of a fundamental solution once around the origin multiplies it by a fixed monodromy matrix. This is parallel transport for the flat connection $d-B\,dz$ on the trivial bundle over the punctured plane, and property (4) shows the monodromy is a representation of $\pi_1(\mathbb C\setminus\{0\})=\mathbb Z$, while property (7) is the statement that the monodromy can be non-trivial. The theorem applies because the flat connection depends only on homotopy classes of loops (a fact proved from properties (2)–(4) plus flatness); the subtlety is that although the connection is flat, the base is not simply connected, so transport is path-dependent exactly in the way property (7) allows.

**Berry's phase in adiabatic quantum mechanics.** Slowly varying the parameters of a Hamiltonian around a loop in parameter space transports an eigenstate back to itself up to a phase, the Berry phase, which is the holonomy of the Berry connection on the eigenline bundle over parameter space. Property (6) forces this holonomy into $U(1)$ (the eigenline is a Hermitian line bundle and the Berry connection is Hermitian), and property (7) is precisely the observation that the phase is generally non-zero and depends on the loop, being the integral of the Berry curvature. The theorem applies because the adiabatic transport of the eigenstate is parallel transport for a genuine connection; the point of interest is that the holonomy being a *phase* rather than an arbitrary complex number is property (6), not an accident.

---

# Bridges

- **Holonomy as a group.** Restricting parallel transport to loops based at $m$ and writing $\Gamma_c(p)=p\cdot\operatorname{hol}_p(c)$ defines the [[Def - Holonomy Group of a Connection|holonomy group]] $\operatorname{Hol}_p(\omega)\subset G$. Properties (1), (3), (4) are exactly the three group axioms for this set: the constant loop gives the identity element, orientation reversal gives inverses, and concatenation gives the product. This is the construction that turns the present structural theorem into the starting point of holonomy theory; the group is well defined up to conjugacy as the base point moves, again by properties (4) and (5).

- **Curvature as infinitesimal holonomy.** Property (7) says transport around a loop is non-trivial; the quantitative refinement expands the transport of a small loop bounding a surface $S$ as $\Gamma_c=\operatorname{id}-\int_S F+O(\text{area}^{3/2})$, so the curvature is the density of holonomy per unit area. The bridge is built by writing transport as a [[Def - Path-Ordered Exponential|path-ordered exponential]], expanding to second order, and applying Stokes' theorem to the leading term; the abelian case is [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy theorem]] and shows $\Gamma_c=\exp(-\int_S F)$ exactly.

- **The classical parallel transport of Riemannian geometry.** For $P=\operatorname{Fr}(TM)$ the frame bundle and $\rho$ the standard representation, $E=TM$ and $PT_c$ is the [[Def - Parallel Transport|parallel transport]] of the Levi-Civita connection. Property (6) with the metric reduction to $O(n)$ recovers the vault's [[Thm - Parallel Transport is an Isometry for Metric-Compatible Connections|theorem that parallel transport is an isometry for metric-compatible connections]]: the present proof derives it from equivariance of $\Gamma_c$ on the principal bundle rather than from the metric-compatibility identity, and the two agree because the $O(n)$-reduction of the frame bundle *is* the metric compatibility of the connection.

- **Monodromy of flat connections.** When $F=0$, properties (2)–(4) combine with a homotopy-invariance argument to show that $\Gamma_c$ depends only on the homotopy class of $c$ relative to its endpoints, so $[c]\mapsto\operatorname{hol}_p(c)$ becomes the monodromy representation $\pi_1(M,m)\to G$. Property (4) is what makes it a homomorphism (up to the ordering convention on the path product); this is the entry point to [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the correspondence between flat connections and representations of the fundamental group]].

---

# Unlocked by This

> [!tip] Holonomy group *(from Gauge Theory V)*
> The three properties (1), (3), (4) are precisely the identity, inverse, and product axioms, so the set of holonomies of loops is a subgroup [[Def - Holonomy Group of a Connection|$\operatorname{Hol}_p(\omega)\subset G$]]. Property (6) then constrains it: metric connections have holonomy in $O(k)$, Hermitian connections in $U(m)$, complex connections in $GL_m(\mathbb C)$.

> [!tip] Wilson lines and Wilson loops *(from Yang–Mills theory, Gauge Theory VII)*
> The trace of parallel transport around a closed loop, $\operatorname{tr}\Gamma_c$, is the **Wilson loop**, the basic gauge-invariant observable of a gauge theory. Property (5) is why it is gauge invariant, property (4) is why Wilson loops multiply under joining of loops, and property (7) is why they are non-trivial and can detect the field strength.
