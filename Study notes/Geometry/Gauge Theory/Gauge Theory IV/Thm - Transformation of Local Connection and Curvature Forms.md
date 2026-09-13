---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Local Connection Form and Gauge Potential"
  - "Def - The Maurer-Cartan Form"
  - "Def - Transition Functions and the Cocycle Condition"
  - "Thm - Pull-Back Commutes with the Exterior Derivative"
  - "Def - Curvature of a Principal Connection"
  - "Def - Connection on a Principal Bundle"
  - "Thm - Structure Equation for the Curvature"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a smooth principal $G$-bundle over a smooth manifold $M$, with $G$ a Lie group acting on the **right**, $R_g(p)=p\cdot g$, and Lie algebra $\mathfrak g=T_eG$. For $\xi\in\mathfrak g$ the **fundamental vector field** is $\xi_P(p)=\frac{d}{dt}\big|_{t=0}\,p\cdot\exp(t\xi)$ (the notation of [[Def - Fundamental Vector Field of a Group Action]]); the vectors $\{\xi_P(p):\xi\in\mathfrak g\}$ span the **vertical subspace** $V_p=\ker d_p\pi\subseteq T_pP$. We write $\operatorname{Ad}_g\colon\mathfrak g\to\mathfrak g$ for the adjoint representation, $\operatorname{Ad}_gX=gXg^{-1}$ for matrix groups, and $\operatorname{Ad}_{g^{-1}}=(\operatorname{Ad}_g)^{-1}$.

A **connection** on $P$ (see [[Def - Connection on a Principal Bundle]]) is a $\mathfrak g$-valued one-form $\omega\in\Omega^1(P;\mathfrak g)$ satisfying
$$\text{(1)}\quad R_g^*\omega=\operatorname{Ad}_{g^{-1}}\circ\,\omega\ \ \forall g\in G, \qquad\text{i.e. } \omega_{p\cdot g}\big(dR_g\,X\big)=\operatorname{Ad}_{g^{-1}}\!\big(\omega_p(X)\big);\qquad \text{(2)}\quad \omega(\xi_P)=\xi\ \ \forall\xi\in\mathfrak g.$$
We write $\mathcal A(P)$ for the set of all connections. Its **horizontal subspace** at $p$ is $H_p=\ker\omega_p$, with $T_pP=H_p\oplus V_p$, and $\pi_H\colon T_pP\to H_p$ is the horizontal projection along $V_p$ (the notation of [[Def - Horizontal Subspace and Horizontal Lift]]). The **curvature** of $\omega$ is $\Omega\in\Omega^2(P;\mathfrak g)$, $\Omega(X,Y)=d\omega(\pi_HX,\pi_HY)$ (see [[Def - Curvature of a Principal Connection]]).

The left **Maurer–Cartan form** of $G$ is $\theta\in\Omega^1(G;\mathfrak g)$, $\theta_g=d_gL_{g^{-1}}\colon T_gG\to\mathfrak g$ (the notation of [[Def - The Maurer-Cartan Form]]); for matrix groups $\theta=g^{-1}\,dg$. For a smooth map $g\colon U\to G$, $g^*\theta\in\Omega^1(U;\mathfrak g)$ is its pullback, $(g^*\theta)_x(v)=\theta_{g(x)}\big(d_xg(v)\big)$; for matrix groups $g^*\theta=g^{-1}\,dg$.

A **local gauge** (local section) of $P$ over an open set $U\subseteq M$ is a smooth $s\colon U\to P$ with $\pi\circ s=\operatorname{id}_U$. Given a cover $\{U_\alpha\}$ of $M$ trivialising $P$ and local gauges $s_\alpha\colon U_\alpha\to P$, the **transition functions** are the unique maps $g_{\alpha\beta}\colon U_{\alpha\beta}\to G$ on $U_{\alpha\beta}:=U_\alpha\cap U_\beta$ with
$$s_\beta=s_\alpha\cdot g_{\alpha\beta}\quad\text{on }U_{\alpha\beta},$$
and they satisfy the cocycle condition $g_{\alpha\beta}g_{\beta\gamma}=g_{\alpha\gamma}$, $g_{\alpha\alpha}=e$ (the notation of [[Def - Transition Functions and the Cocycle Condition]]). The **local connection forms** and **local curvature forms** are
$$A_\alpha:=s_\alpha^*\omega\in\Omega^1(U_\alpha;\mathfrak g),\qquad F_\alpha:=s_\alpha^*\Omega\in\Omega^2(U_\alpha;\mathfrak g),$$
in the notation of [[Def - Local Connection Form and Gauge Potential]]; by the local structure equation, $F_\alpha=dA_\alpha+\tfrac12[A_\alpha\wedge A_\alpha]$. Here $[\cdot\wedge\cdot]$ is the bracket of $\mathfrak g$-valued forms of [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]], with $\tfrac12[A\wedge A]=A\wedge A$ for matrix groups. The **adjoint bundle** is $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$, the associated bundle for the adjoint representation, whose points are equivalence classes $[p,X]$ under $[p\cdot g,\operatorname{Ad}_{g^{-1}}X]=[p,X]$ (see [[Def - Adjoint Bundles ad P and Ad P]]); $\Omega^k(M;\operatorname{ad}P)=\Gamma(\Lambda^kT^*M\otimes\operatorname{ad}P)$. The full symbol registry is on [[Gauge Theory IV — Connections and Curvature on Principal Bundles]].

> [!warning] Convention: the pure-gauge term and the two source presentations
> The intrinsic form of the inhomogeneous term below is $g_{\alpha\beta}^*\theta$. Bär (T2.3.6, his equations (2.2)/(2.3)) writes it as $d\big(g_{\alpha\beta}(u_0)^{-1}g_{\alpha\beta}\big)\big|_{u_0}$; these are equal, because $g_{\alpha\beta}(u_0)^{-1}g_{\alpha\beta}=L_{g_{\alpha\beta}(u_0)^{-1}}\circ g_{\alpha\beta}$, whose differential at $u_0$ is $d_{g_{\alpha\beta}(u_0)}L_{g_{\alpha\beta}(u_0)^{-1}}\circ d_{u_0}g_{\alpha\beta}=\theta_{g_{\alpha\beta}(u_0)}\circ d_{u_0}g_{\alpha\beta}=(g_{\alpha\beta}^*\theta)_{u_0}$, and it lands in $T_eG=\mathfrak g$. We state the theorem in the $g_{\alpha\beta}^*\theta$ form throughout. Haydys (D2.2.16, T2.2.5 Step 3) writes $a$ for the connection form and $A$ for its local representation, and works on the frame bundle with $G=GL_k$, where the law reads $A_\beta=g_{\alpha\beta}^{-1}A_\alpha g_{\alpha\beta}+g_{\alpha\beta}^{-1}\,dg_{\alpha\beta}$ (his (14)); this is the matrix specialisation of part (a). Bär's D2.3.1 misprints connection condition (1) as "$R_g^*=\operatorname{Ad}_{g^{-1}}\circ\omega$", dropping the $\omega$ on the left; the corrected form is the one displayed above.

---

# Statement

> **Theorem (transformation and gluing of local connection and curvature forms).** Let $\pi\colon P\to M$ be a principal $G$-bundle, let $\omega\in\mathcal A(P)$ be a connection with curvature $\Omega$, and let $s_\alpha\colon U_\alpha\to P$, $s_\beta\colon U_\beta\to P$ be local gauges with transition function $g_{\alpha\beta}\colon U_{\alpha\beta}\to G$, so $s_\beta=s_\alpha\cdot g_{\alpha\beta}$ on $U_{\alpha\beta}$. Write $A_\alpha=s_\alpha^*\omega$, $A_\beta=s_\beta^*\omega$, $F_\alpha=s_\alpha^*\Omega$, $F_\beta=s_\beta^*\Omega$.
>
> **(a) Transformation of the connection form.** On $U_{\alpha\beta}$,
> $$A_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha+g_{\alpha\beta}^*\theta,$$
> which for a matrix group $G$ reads $A_\beta=g_{\alpha\beta}^{-1}A_\alpha g_{\alpha\beta}+g_{\alpha\beta}^{-1}\,dg_{\alpha\beta}$.
>
> **(b) Reconstruction from local data.** Conversely, let $\{U_\alpha\}$ be a cover trivialising $P$ with transition functions $g_{\alpha\beta}$, and let $(A_\alpha)_\alpha$, $A_\alpha\in\Omega^1(U_\alpha;\mathfrak g)$, be a family satisfying the law in (a) on every overlap $U_{\alpha\beta}$. Then there is a **unique** connection $\omega\in\mathcal A(P)$ with $s_\alpha^*\omega=A_\alpha$ for all $\alpha$.
>
> **(c) Transformation of the curvature and gluing.** On $U_{\alpha\beta}$,
> $$F_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha$$
> with **no inhomogeneous term**. Consequently the locally defined sections $[s_\alpha,F_\alpha]$ of $\Lambda^2T^*M\otimes\operatorname{ad}P$ agree on overlaps and glue to a single global form $F=F_\omega\in\Omega^2(M;\operatorname{ad}P)$, which equals the descended curvature $\overline\Omega$ of [[Def - Curvature of a Principal Connection]] (the unique form with $[s_\alpha,\overline\Omega|_{U_\alpha}]=[s_\alpha,F_\alpha]$). If $G$ is abelian, then $\operatorname{Ad}$ is trivial, $F_\beta=F_\alpha$, and the $F_\alpha$ glue to a genuine $\mathfrak g$-valued global two-form $F\in\Omega^2(M;\mathfrak g)$.

---

# Motivation

A connection lives on the total space $P$, but every computation and every explicit example lives on the base $M$: one writes a gauge potential $A_\mu(x)\,dx^\mu$ in coordinates, integrates a curvature over a surface in $M$, varies an action functional on $M$. The bridge between the two is the local form $A_\alpha=s_\alpha^*\omega$, produced by pulling $\omega$ back along a chosen gauge. The one fact that then governs the entire theory is that this bridge is not canonical: there is no preferred gauge on a nontrivial bundle, so the *same* connection produces *different* local forms in different gauges. This theorem is the exact accounting of that ambiguity. Part (a) says precisely how the local form changes when the gauge changes, part (b) says that this change law is the *only* constraint — any family obeying it is the local data of one and only one honest global connection — and part (c) says that although the connection form transforms inhomogeneously, the curvature form transforms homogeneously and therefore assembles into a genuine global object on $M$.

The importance is threefold. First, part (a) is the mathematical content of the phrase "gauge transformation": in electromagnetism it is $\mathsf A_\mu\mapsto\mathsf A_\mu+\partial_\mu\chi$, in Yang–Mills theory it is $A_\mu\mapsto g^{-1}A_\mu g+g^{-1}\partial_\mu g$, and in Riemannian geometry it is the change-of-frame law for the connection matrix; all three are the single formula $A_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha+g_{\alpha\beta}^*\theta$. Second, part (b) is what lets one *build* connections and bundles from local pieces: this is how connections are constructed in practice (patch by patch, then glued), and it is the point at which the cocycle description of a principal bundle becomes a cocycle description of a connection on it. Third, part (c) is the reason curvature, and not the potential, is the carrier of geometric and topological information: because $F$ descends to a global $\operatorname{ad}P$-valued two-form, one can integrate invariant polynomials of it over $M$ and obtain gauge-invariant numbers — the characteristic classes of Chern–Weil theory. Without the homogeneous transformation law of (c) there would be no Chern number, no instanton number, no topological classification of bundles by curvature integrals.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is mild — a connection and two gauges related by a transition function — so the real source question is: when does a problem secretly present two gauges of one connection, so that part (a) or (c) applies even though no principal bundle is named?

The first disguised source is **a change of local frame in a vector bundle with a covariant derivative**. If $E\to M$ carries a connection $\nabla$ and $e,e'$ are two local frames on an overlap, related by $e'=e\cdot g$ with $g\colon U\to GL_k$, then the connection matrices $A(\nabla,e)$ and $A(\nabla,e')$ are exactly the local connection forms of the induced connection on the frame bundle $\operatorname{Fr}(E)$ in the two gauges $e,e'$, and the theorem's part (a) is the frame-change law $A(\nabla,e')=g^{-1}A(\nabla,e)g+g^{-1}dg$. The bridge $B\Rightarrow A$ is the identification $e^*\omega=A(\nabla,e)$ of [[Def - Local Connection Form and Gauge Potential]]; recognising that "two frames of the same bundle" is "two gauges of the same principal connection" turns a linear-algebra change-of-basis calculation into an instance of the theorem. *Example problem:* deduce the transformation law of the Christoffel symbols under a change of coordinates by realising the two coordinate frames as two gauges of the Levi-Civita connection on $\operatorname{Fr}(TM)$.

The second disguised source is **a physicist's field configuration written in two gauges**. Suppose one is handed a gauge potential $A_\mu$ and a "gauge-transformed" potential $A_\mu'$ said to describe the same physics, together with the group element $g(x)$ implementing the transformation. This is precisely a connection presented in two gauges over a single patch (with $g_{\alpha\beta}$ replaced by the gauge transformation $g$), and part (a) is the statement that $A'=\operatorname{Ad}_{g^{-1}}A+g^*\theta$. The bridge is that a gauge transformation of a trivial bundle is the special case $U_\alpha=U_\beta=U$, $s_\beta=s_\alpha\cdot g$; the theorem's overlap law and the physicist's gauge transformation are the same equation read with different intent. *Example problem:* verify that the field strength $F_{\mu\nu}$ of a Yang–Mills potential is gauge-covariant, i.e. transforms by conjugation with no additive term, directly from part (c).

The third disguised source is **local data for a bundle-with-connection assembled from charts**. Whenever one specifies a geometry patch by patch — a $\mathfrak g$-valued one-form on each chart of an atlas, together with transition functions — the question "does this local data come from a global connection?" is answered by part (b): it does, uniquely, precisely when the forms obey the law of part (a) on overlaps. The bridge $B\Rightarrow A$ is that the cocycle $(g_{\alpha\beta})$ already defines the bundle $P$ (by [[Thm - Principal Bundles are Classified by Cocycles]]), and the compatibility law promotes a local potential to a global connection. *Example problem:* construct the monopole connection on the Hopf bundle $S^3\to S^2$ by giving $A_N$ and $A_S$ on the two hemispheres and checking $A_S=A_N+g_{NS}^*\theta$ on the equatorial overlap.

**Targets (Output Amplification)**

Combine part (c) with **an $\operatorname{Ad}$-invariant polynomial $f$ on $\mathfrak g$**. Because $F$ is a global $\operatorname{ad}P$-valued two-form and $f$ is $\operatorname{Ad}$-invariant, the scalar form $f(F)\in\Omega^{2k}(M)$ is a well-defined global real form on $M$; the extra ingredient is the invariance $f(\operatorname{Ad}_gX_1,\dots)=f(X_1,\dots)$, which absorbs exactly the conjugation $\operatorname{Ad}_{g_{\alpha\beta}^{-1}}$ of the transition law. The payoff is the entire construction of characteristic classes: $f(F)$ is closed and its de Rham class is independent of the connection, giving the Chern, Pontryagin, and Euler classes ([[Thm - Chern-Weil Theorem]]). This is non-obvious because it converts a purely local invariance of a polynomial into a global topological invariant of the bundle.

Combine part (b) with **a partition of unity and the affine structure of $\mathcal A(P)$**. Given the reconstruction of a connection from compatible local data, one may build a connection on *any* bundle by choosing arbitrary local potentials, gluing them with a partition of unity, and correcting the failure of the naive average to satisfy the cocycle law by the homogeneous transformation of the correction terms; the extra ingredient is that the difference of two connections is a global $\operatorname{ad}P$-valued one-form ([[Thm - Existence of Connections on Principal Bundles]]). The payoff is the existence of connections on every principal bundle and the description of $\mathcal A(P)$ as an affine space over $\Omega^1(M;\operatorname{ad}P)$, which is the arena for the Yang–Mills and Seiberg–Witten variational problems.

Combine part (a) with **the group of gauge transformations $\mathcal G(P)=\Gamma(\operatorname{Ad}P)$**. Reading the transition function $g_{\alpha\beta}$ instead as a bundle automorphism over a fixed chart turns the overlap law into the action of the gauge group on the space of connections, $A\mapsto\operatorname{Ad}_{g^{-1}}A+g^*\theta$; the extra ingredient is the identification of vertical automorphisms of $P$ with sections of $\operatorname{Ad}P$ ([[Def - Gauge Transformation]]). The payoff is the quotient $\mathcal A(P)/\mathcal G(P)$, the true configuration space of a gauge theory, whose geometry (reducible connections, the based gauge group, the orbit structure) drives the topology of moduli spaces in chapters XI and XIII.

---

# Why Is It True

Forget the formulas and picture the total space $P$ over an overlap $U_{\alpha\beta}$ as $U_{\alpha\beta}\times G$. A gauge $s_\alpha$ is a "floor" — a copy of the base sitting at group-height $e$ — and the second gauge $s_\beta=s_\alpha\cdot g_{\alpha\beta}$ is the same base pushed up the fibre to group-height $g_{\alpha\beta}(x)$, a height that varies as $x$ moves. When we pull the connection $\omega$ back along $s_\beta$ we are reading $\omega$ along this raised, tilted floor rather than along the original one. The velocity of a point moving in the raised floor decomposes into two pieces: the old base velocity, carried up the fibre by the right translation $R_{g_{\alpha\beta}}$, and a *purely vertical* velocity coming from the fact that the height $g_{\alpha\beta}(x)$ is itself changing as $x$ moves. This is exactly the content of the differential-of-the-action-map lemma (Lemma 1 below): a tangent vector to the raised floor is $dR_{g_{\alpha\beta}}(\text{old})+\big(\text{rate of change of }g_{\alpha\beta}\big)_P$.

Now apply $\omega$ to this decomposed velocity. On the transported-base piece, condition (1) — the equivariance $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$ — replaces the transport by a conjugation, producing $\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha$. On the vertical piece, condition (2) — $\omega(\xi_P)=\xi$ — reads off the group-velocity itself, which is precisely $g_{\alpha\beta}^*\theta$, the rate at which $g_{\alpha\beta}$ turns measured in the Lie algebra. The two pieces are the two terms of part (a). The inhomogeneous term is not an algebraic accident; it is the connection reporting the vertical motion that changing the gauge forces on us.

> **Mechanism.** Moving the reference gauge along the fibre by $g_{\alpha\beta}$ conjugates the connection by $\operatorname{Ad}_{g_{\alpha\beta}^{-1}}$ (from equivariance) and adds the pure-gauge term $g_{\alpha\beta}^*\theta$ (from the vertical velocity that the varying group-height creates); the curvature carries no such term because it is horizontal, so it annihilates that vertical velocity outright.

Part (c) is the same picture with one decisive difference. The curvature $\Omega(X,Y)=d\omega(\pi_HX,\pi_HY)$ is *horizontal*: it vanishes the moment either argument has a vertical component, because $\pi_H$ deletes vertical parts. So when we pull $\Omega$ back along the raised floor, the vertical velocity — the very thing that produced the inhomogeneous term for $A$ — is killed on sight. Only the transported-base piece survives, and equivariance of $\Omega$ ($R_g^*\Omega=\operatorname{Ad}_{g^{-1}}\Omega$) turns its transport into a pure conjugation. The result is the homogeneous law $F_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha$, and a homogeneously transforming family is exactly what glues into a section of the associated bundle $\operatorname{ad}P$. The whole distinction between "gauge potential (does not descend)" and "field strength (descends)" is the distinction between "$\omega$ sees vertical vectors" and "$\Omega$ does not".

---

# What Makes This Hard

The one genuinely non-obvious step is Lemma 1, the differential of the right-action map $\hat R\colon P\times G\to P$: one must see that varying the group argument produces a *fundamental* vector $\big(\theta_g(w)\big)_P(pg)$, with the Maurer–Cartan form appearing precisely because a tangent vector $w\in T_gG$ must be left-translated back to the identity before it names a Lie-algebra element. Skipping this and differentiating "naively" is the common error; it produces the right first term but mangles the second, losing the fact that it is vertical. The second subtlety is that part (c)'s "no inhomogeneous term" rests entirely on the *horizontality* of $\Omega$, not on any special property of $\Omega$ as a closed form: a reader who tries to prove (c) by pulling back $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$ and cancelling terms algebraically can do it, but will miss why the cancellation is forced and will not see the clean structural reason. The third trap, in part (b), is to conflate *existence* of a connection with the correct local form (which requires a genuine construction over each patch) with *uniqueness* (which is the reconstruction identity); the two are separate obligations and both must be discharged.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Express the second gauge as $s_\beta=\hat R\circ(s_\alpha,g_{\alpha\beta})$ and differentiate using the action-map lemma; apply $\omega$ and use conditions (1),(2) to read off part (a). For part (c) do the same to $\Omega$ and use that $\Omega$ is horizontal (so the vertical term dies) together with the equivariance of $\Omega$. For part (b), build a connection over each patch from the given local form and glue the patches using the uniqueness of the reconstruction and the law of part (a).

**Subgoal decomposition:**

1. **Differential of the action map (Lemma 1).** Show $d\hat R_{(p,g)}(v,w)=dR_g(v)+\big(\theta_g(w)\big)_P(p\cdot g)$.
   - *Hint:* Differentiate along the two coordinate directions separately: hold $g$ fixed to get $dR_g(v)$; hold $p$ fixed and take the curve $g\exp(t\theta_g(w))$ to get the fundamental vector.
   - *Why needed:* It is the exact decomposition of a velocity in the raised gauge into a transported-horizontal part and a vertical part; part (a) and part (c) both differentiate $s_\beta$ through it.

2. **Reconstruction over a single patch (Lemma 2).** Show that over a trivialising $U$ with gauge $s$, every $A\in\Omega^1(U;\mathfrak g)$ is the local form of a unique connection $\omega_A$ on $P|_U$.
   - *Hint:* Transport the "product connection plus potential" $\operatorname{pr}_2^*\theta+\operatorname{Ad}_{(\cdot)^{-1}}\pi^*A$ through the trivialisation $\Phi(x,g)=s(x)g$; check conditions (1),(2); uniqueness is the reconstruction identity of [[Def - Local Connection Form and Gauge Potential]].
   - *Why needed:* Part (b) glues these patchwise connections; without existence-and-uniqueness over one patch there is nothing to glue.

3. **Part (a).** Differentiate $s_\beta=\hat R\circ(s_\alpha,g_{\alpha\beta})$ via Lemma 1, apply $\omega$, use (1) on the transported term and (2) on the vertical term.
   - *Hint:* The vertical term's Lie-algebra value is $\theta_{g_{\alpha\beta}}(dg_{\alpha\beta})=g_{\alpha\beta}^*\theta$.
   - *Why needed:* It is the theorem's first claim and the input to (b).

4. **Part (c).** Differentiate $s_\beta$ the same way, apply $\Omega$, and use horizontality of $\Omega$ to kill every term containing the vertical piece; convert the surviving transported term by $R_g^*\Omega=\operatorname{Ad}_{g^{-1}}\Omega$.
   - *Hint:* A two-form that vanishes on vertical vectors kills the vertical summand in each slot, including the cross terms.
   - *Why needed:* It is the homogeneous law; the gluing follows from it by the definition of $\operatorname{ad}P$.

5. **Part (b) and the gluing in (c).** Build $\omega^{(\alpha)}$ on each $P|_{U_\alpha}$ by Lemma 2; show $\omega^{(\alpha)}=\omega^{(\beta)}$ on overlaps using part (a) for $\omega^{(\beta)}$, the given cocycle law, and uniqueness; for (c) use $[s_\beta,F_\beta]=[s_\alpha,F_\alpha]$ from the $\operatorname{ad}P$ relation.
   - *Hint:* Two connections with equal local forms on a patch are equal there.
   - *Why needed:* It upgrades local data to a global connection and local curvatures to a global $\operatorname{ad}P$-valued form.

---

# Lemma Decomposition

> [!note]- Lemma 1: Differential of the right-action map
> **Statement:** Let $\hat R\colon P\times G\to P$, $\hat R(p,g)=p\cdot g$, be the action map. For $p\in P$, $g\in G$, $v\in T_pP$, $w\in T_gG$,
> $$d\hat R_{(p,g)}(v,w)=dR_g(v)+\big(\theta_g(w)\big)_P(p\cdot g),$$
> where $R_g\colon P\to P$ is right translation by $g$, $\theta_g(w)=d_gL_{g^{-1}}(w)\in\mathfrak g$, and $(\,\cdot\,)_P$ is the fundamental vector field.
>
> **Hint:** Split $(v,w)=(v,0)+(0,w)$; the first summand holds the group argument fixed, the second holds the base argument fixed and is computed with the curve $g\exp(t\theta_g(w))$.
>
> **Why needed:** It is the exact velocity decomposition in a moving gauge, applied in parts (a) and (c) to $s_\beta=\hat R\circ(s_\alpha,g_{\alpha\beta})$; the fundamental vector it produces is what conditions (2) and horizontality act on.
>
> > [!note]- Full proof
> > **What is assumed and what is shown.** We assume $\hat R$ is the smooth right action, so $\hat R(p,g)=p\cdot g$, $R_g=\hat R(\cdot,g)$, and $\hat R(p,\cdot)$ is the orbit map $g\mapsto p\cdot g$. We must compute the differential $d\hat R_{(p,g)}\colon T_pP\oplus T_gG\to T_{p\cdot g}P$ on an arbitrary $(v,w)$. By linearity of the differential it suffices to evaluate it on $(v,0)$ and $(0,w)$ and add.
> >
> > **Step 1 — the base direction $(v,0)$.** Choose a curve $p(t)$ in $P$ with $p(0)=p$, $\dot p(0)=v$, and hold the group argument fixed at $g$. Then $t\mapsto(p(t),g)$ is a curve in $P\times G$ through $(p,g)$ with velocity $(v,0)$, and $\hat R(p(t),g)=p(t)\cdot g=R_g\big(p(t)\big)$. Hence
> > $$d\hat R_{(p,g)}(v,0)=\frac{d}{dt}\Big|_{0}R_g\big(p(t)\big)=dR_g\big(\dot p(0)\big)=dR_g(v) \qquad\text{(chain rule; }R_g\text{ smooth).}$$
> >
> > **Step 2 — the group direction $(0,w)$.** Set $\xi:=\theta_g(w)=d_gL_{g^{-1}}(w)\in\mathfrak g$. Take the curve $g(t):=g\exp(t\xi)=L_g\big(\exp(t\xi)\big)$ in $G$; then $g(0)=g$ and
> > $$\dot g(0)=\frac{d}{dt}\Big|_0 L_g\big(\exp(t\xi)\big)=d_eL_g\Big(\tfrac{d}{dt}\big|_0\exp(t\xi)\Big)=d_eL_g(\xi)=d_eL_g\big(d_gL_{g^{-1}}(w)\big)=w \qquad\text{(}\exp'(0)=\operatorname{id},\ L_g\circ L_{g^{-1}}=\operatorname{id}_G\text{),}$$
> > so $t\mapsto(p,g(t))$ has velocity $(0,w)$ at $t=0$. Holding the base argument fixed at $p$,
> > $$\hat R\big(p,g(t)\big)=p\cdot\big(g\exp(t\xi)\big)=(p\cdot g)\cdot\exp(t\xi) \qquad\text{(associativity of the right action).}$$
> > Differentiating,
> > $$d\hat R_{(p,g)}(0,w)=\frac{d}{dt}\Big|_0(p\cdot g)\cdot\exp(t\xi)=\xi_P(p\cdot g)=\big(\theta_g(w)\big)_P(p\cdot g) \qquad\text{(definition of the fundamental vector field }\xi_P\text{).}$$
> >
> > **Step 3 — combine.** By linearity of $d\hat R_{(p,g)}$ and $(v,w)=(v,0)+(0,w)$,
> > $$d\hat R_{(p,g)}(v,w)=d\hat R_{(p,g)}(v,0)+d\hat R_{(p,g)}(0,w)=dR_g(v)+\big(\theta_g(w)\big)_P(p\cdot g).$$
> > **Conclusion.** The differential of the action map splits a velocity into its right-transported base part and the vertical fundamental vector named by the Maurer–Cartan value of the group velocity. $\blacksquare$

> [!note]- Lemma 2: Existence and uniqueness of a connection with prescribed local form over a patch
> **Statement:** Let $U\subseteq M$ be open and trivialising, with gauge $s\colon U\to P$ and induced trivialisation $\Phi\colon U\times G\to P|_U$, $\Phi(x,g)=s(x)\cdot g$. For every $A\in\Omega^1(U;\mathfrak g)$ there is a **unique** connection $\omega_A\in\mathcal A(P|_U)$ with $s^*\omega_A=A$. Explicitly, in the trivialisation,
> $$\Phi^*\omega_A=\operatorname{Ad}_{\operatorname{pr}_2^{-1}}\!\big(\operatorname{pr}_1^*A\big)+\operatorname{pr}_2^*\theta,$$
> where $\operatorname{pr}_1\colon U\times G\to U$, $\operatorname{pr}_2\colon U\times G\to G$ are the projections and $\operatorname{Ad}_{\operatorname{pr}_2^{-1}}$ means $\operatorname{Ad}_{g^{-1}}$ at the point $(x,g)$.
>
> **Hint:** Verify conditions (1),(2) for $\Phi^*\omega_A$ directly on $U\times G$ using $R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta$ and $\theta(\xi_{U\times G})=\xi$; then $s^*\omega_A=A$ because pulling back along the identity section kills $\operatorname{pr}_2^*\theta$ and leaves $\operatorname{Ad}_eA=A$. Uniqueness is the reconstruction identity.
>
> **Why needed:** Part (b) constructs the global connection by building one on each patch and gluing; this lemma supplies both the patchwise connection and the uniqueness that makes the glue unambiguous.
>
> > [!note]- Full proof
> > **What is assumed and what is shown.** By [[Thm - Sections of a Principal Bundle and Triviality]] a gauge $s$ over $U$ gives a $G$-equivariant diffeomorphism $\Phi\colon U\times G\to P|_U$, $\Phi(x,g)=s(x)\cdot g$, intertwining the right $G$-action on $U\times G$, $(x,g)\cdot h=(x,gh)$, with that on $P|_U$. We must produce a connection on $P|_U$ with local form $A$ and show it is the only one. It is equivalent, transporting through the diffeomorphism $\Phi$, to produce a connection $\eta:=\Phi^*\omega_A$ on the trivial bundle $U\times G\to U$ with $s_0^*\eta=A$, where $s_0(x)=(x,e)$ is the identity gauge (note $\Phi\circ s_0=s$, so $s^*\omega_A=s_0^*\Phi^*\omega_A=s_0^*\eta$).
> >
> > **Step 0 — the candidate is a well-defined $\mathfrak g$-valued one-form.** Define
> > $$\eta:=\operatorname{Ad}_{\operatorname{pr}_2^{-1}}\!\big(\operatorname{pr}_1^*A\big)+\operatorname{pr}_2^*\theta\in\Omega^1(U\times G;\mathfrak g),$$
> > i.e. $\eta_{(x,g)}(v,w)=\operatorname{Ad}_{g^{-1}}\!\big(A_x(v)\big)+\theta_g(w)$ for $(v,w)\in T_xU\oplus T_gG$. Each summand is smooth in $(x,g)$ ($A$, $\theta$, and $g\mapsto\operatorname{Ad}_{g^{-1}}$ are smooth), so $\eta\in\Omega^1(U\times G;\mathfrak g)$.
> >
> > **Step 1 — condition (2).** The fundamental vector field of $\xi\in\mathfrak g$ on $U\times G$ is $\xi_{U\times G}(x,g)=\frac{d}{dt}\big|_0(x,g\exp t\xi)=(0,d_eL_g\xi)$, a purely vertical vector. Since $\operatorname{pr}_1^*A$ annihilates vectors with zero $U$-component,
> > $$\eta\big(\xi_{U\times G}\big)=\operatorname{Ad}_{g^{-1}}\!\big(A_x(0)\big)+\theta_g\big(d_eL_g\xi\big)=0+\theta_g\big(d_eL_g\xi\big) \qquad\text{(}\operatorname{pr}_1^*A\text{ kills the vertical vector).}$$
> > Now $\theta_g\big(d_eL_g\xi\big)=d_gL_{g^{-1}}\big(d_eL_g\xi\big)=d_e\big(L_{g^{-1}}\circ L_g\big)(\xi)=\xi$ (by $L_{g^{-1}}\circ L_g=\operatorname{id}_G$), so $\eta(\xi_{U\times G})=\xi$. Condition (2) holds.
> >
> > **Step 2 — condition (1).** Right translation by $h$ is $R_h(x,g)=(x,gh)$, so $\operatorname{pr}_1\circ R_h=\operatorname{pr}_1$ and $\operatorname{pr}_2\circ R_h=R_h^G\circ\operatorname{pr}_2$ with $R_h^G$ right translation on $G$. Pulling back each summand:
> > $$R_h^*\big(\operatorname{pr}_1^*A\big)=(\operatorname{pr}_1\circ R_h)^*A=\operatorname{pr}_1^*A \qquad\text{(}\operatorname{pr}_1\circ R_h=\operatorname{pr}_1\text{),}$$
> > and, using $R_h^{G*}\theta=\operatorname{Ad}_{h^{-1}}\theta$ (equivariance of the Maurer–Cartan form, [[Def - The Maurer-Cartan Form]]),
> > $$R_h^*\big(\operatorname{pr}_2^*\theta\big)=\operatorname{pr}_2^*\big(R_h^{G*}\theta\big)=\operatorname{pr}_2^*\big(\operatorname{Ad}_{h^{-1}}\theta\big)=\operatorname{Ad}_{h^{-1}}\operatorname{pr}_2^*\theta \qquad\text{(}\operatorname{pr}_2\circ R_h=R_h^G\circ\operatorname{pr}_2\text{).}$$
> > For the conjugation factor, at the point $R_h(x,g)=(x,gh)$ the coefficient $\operatorname{Ad}_{\operatorname{pr}_2^{-1}}$ is $\operatorname{Ad}_{(gh)^{-1}}=\operatorname{Ad}_{h^{-1}}\operatorname{Ad}_{g^{-1}}$, whence
> > $$R_h^*\Big(\operatorname{Ad}_{\operatorname{pr}_2^{-1}}\operatorname{pr}_1^*A\Big)=\operatorname{Ad}_{h^{-1}}\operatorname{Ad}_{g^{-1}}\operatorname{pr}_1^*A=\operatorname{Ad}_{h^{-1}}\Big(\operatorname{Ad}_{\operatorname{pr}_2^{-1}}\operatorname{pr}_1^*A\Big) \qquad\text{(}\operatorname{Ad}\text{ is a homomorphism).}$$
> > Adding the two pulled-back summands, $R_h^*\eta=\operatorname{Ad}_{h^{-1}}\eta$. Condition (1) holds.
> >
> > **Step 3 — the local form.** With $s_0(x)=(x,e)$, we have $\operatorname{pr}_1\circ s_0=\operatorname{id}_U$ and $\operatorname{pr}_2\circ s_0\equiv e$ the constant map. A constant map has zero differential, so $s_0^*\operatorname{pr}_2^*\theta=(\operatorname{pr}_2\circ s_0)^*\theta=0$; and $s_0^*\operatorname{Ad}_{\operatorname{pr}_2^{-1}}\operatorname{pr}_1^*A=\operatorname{Ad}_{e^{-1}}A=A$ (evaluating the coefficient along $g=e$, where $\operatorname{Ad}_e=\operatorname{id}$). Hence
> > $$s^*\omega_A=s_0^*\eta=A+0=A.$$
> > Thus $\omega_A:=(\Phi^{-1})^*\eta$ is a connection on $P|_U$ with $s^*\omega_A=A$, proving existence.
> >
> > **Step 4 — uniqueness.** Suppose $\omega,\omega'\in\mathcal A(P|_U)$ both satisfy $s^*\omega=s^*\omega'=A$. By the reconstruction identity of [[Def - Local Connection Form and Gauge Potential]] — every tangent vector at $s(x)\cdot g$ is uniquely $dR_g\big(d_xs(v)\big)+\zeta_P\big(s(x)g\big)$ with $(v,\zeta)\in T_xU\oplus\mathfrak g$, and any connection $\varpi$ takes on it the value $\varpi_{s(x)g}\big(dR_g(d_xs(v))+\zeta_P\big)=\operatorname{Ad}_{g^{-1}}\!\big((s^*\varpi)_x(v)\big)+\zeta$ — the restriction of a connection to $P|_U$ is determined by its local form. Applying this to $\omega$ and $\omega'$, both give $\operatorname{Ad}_{g^{-1}}\!\big(A_x(v)\big)+\zeta$ on the same vector, so $\omega=\omega'$ on $P|_U$.
> > **Conclusion.** Over a trivialising patch, the assignment $A\mapsto\omega_A$ is a bijection between $\Omega^1(U;\mathfrak g)$ and connections on $P|_U$; in particular a prescribed local form determines a connection uniquely. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix the data of the theorem: $\omega\in\mathcal A(P)$ with curvature $\Omega$, and gauges $s_\alpha,s_\beta$ with $s_\beta=s_\alpha\cdot g_{\alpha\beta}$ on $U_{\alpha\beta}$. Abbreviate $g:=g_{\alpha\beta}$, and for a point $u_0\in U_{\alpha\beta}$ write $g_0:=g(u_0)\in G$.
>
> **Step 0 — the map $s_\beta$ as a composite and its differential.** On $U_{\alpha\beta}$ the identity $s_\beta=s_\alpha\cdot g$ reads $s_\beta=\hat R\circ\Psi$ with $\Psi\colon U_{\alpha\beta}\to P\times G$, $\Psi(u)=\big(s_\alpha(u),g(u)\big)$, and $\hat R$ the action map. Fix $u_0$ and $v\in T_{u_0}U_{\alpha\beta}$. By the chain rule and $d_{u_0}\Psi(v)=\big(d_{u_0}s_\alpha(v),\,d_{u_0}g(v)\big)$,
> $$d_{u_0}s_\beta(v)=d\hat R_{(s_\alpha(u_0),g_0)}\big(d_{u_0}s_\alpha(v),\,d_{u_0}g(v)\big)=dR_{g_0}\big(d_{u_0}s_\alpha(v)\big)+\big(\theta_{g_0}(d_{u_0}g(v))\big)_P\big(s_\beta(u_0)\big) \qquad\text{(Lemma 1, at }(s_\alpha(u_0),g_0)\text{).}$$
> Write $\xi(v):=\theta_{g_0}\big(d_{u_0}g(v)\big)=(g^*\theta)_{u_0}(v)\in\mathfrak g$ for the Lie-algebra value of the second (vertical) summand; note $s_\beta(u_0)=s_\alpha(u_0)\cdot g_0$. Thus
> $$d_{u_0}s_\beta(v)=dR_{g_0}\big(d_{u_0}s_\alpha(v)\big)+\xi(v)_P\big(s_\beta(u_0)\big). \tag{$\star$}$$
>
> **Part (a) — transformation of the connection form.** Apply $\omega_{s_\beta(u_0)}$ to $(\star)$ and use its linearity:
> $$A_\beta|_{u_0}(v)=\omega_{s_\beta(u_0)}\big(d_{u_0}s_\beta(v)\big)=\omega_{s_\beta(u_0)}\Big(dR_{g_0}\big(d_{u_0}s_\alpha(v)\big)\Big)+\omega_{s_\beta(u_0)}\Big(\xi(v)_P\big(s_\beta(u_0)\big)\Big) \qquad\text{(definition }A_\beta=s_\beta^*\omega\text{; (}\star\text{); linearity).}$$
> For the first term, set $X:=d_{u_0}s_\alpha(v)\in T_{s_\alpha(u_0)}P$ and use connection condition (1) in the form $\omega_{p\cdot g_0}(dR_{g_0}X)=\operatorname{Ad}_{g_0^{-1}}\!\big(\omega_p(X)\big)$ at $p=s_\alpha(u_0)$:
> $$\omega_{s_\beta(u_0)}\big(dR_{g_0}X\big)=\operatorname{Ad}_{g_0^{-1}}\!\big(\omega_{s_\alpha(u_0)}(X)\big)=\operatorname{Ad}_{g_0^{-1}}\!\big(A_\alpha|_{u_0}(v)\big) \qquad\text{(condition (1); }\omega_{s_\alpha(u_0)}(d_{u_0}s_\alpha(v))=A_\alpha|_{u_0}(v)\text{).}$$
> For the second term, $\xi(v)_P$ is the fundamental vector field of $\xi(v)\in\mathfrak g$, so condition (2) gives
> $$\omega_{s_\beta(u_0)}\Big(\xi(v)_P\big(s_\beta(u_0)\big)\Big)=\xi(v)=(g^*\theta)_{u_0}(v) \qquad\text{(condition (2); definition of }\xi(v)\text{).}$$
> Adding the two terms, for every $u_0\in U_{\alpha\beta}$ and $v$,
> $$A_\beta|_{u_0}(v)=\operatorname{Ad}_{g_0^{-1}}\!\big(A_\alpha|_{u_0}(v)\big)+(g^*\theta)_{u_0}(v),\qquad\text{i.e.}\qquad A_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha+g_{\alpha\beta}^*\theta.$$
> For a matrix group $\operatorname{Ad}_{g^{-1}}X=g^{-1}Xg$ and $g^*\theta=g^{-1}dg$, giving $A_\beta=g_{\alpha\beta}^{-1}A_\alpha g_{\alpha\beta}+g_{\alpha\beta}^{-1}dg_{\alpha\beta}$. This proves (a).
>
> **Part (c) — transformation of the curvature.** Fix $u_0$ and $v_1,v_2\in T_{u_0}U_{\alpha\beta}$. Using $(\star)$ for each argument and writing $X_i:=dR_{g_0}\big(d_{u_0}s_\alpha(v_i)\big)$ (a transported vector) and $W_i:=\xi(v_i)_P\big(s_\beta(u_0)\big)$ (a vertical vector),
> $$F_\beta|_{u_0}(v_1,v_2)=\Omega_{s_\beta(u_0)}\big(d_{u_0}s_\beta(v_1),\,d_{u_0}s_\beta(v_2)\big)=\Omega_{s_\beta(u_0)}\big(X_1+W_1,\,X_2+W_2\big) \qquad\text{(definition }F_\beta=s_\beta^*\Omega\text{; (}\star\text{)).}$$
> Expand by bilinearity into four terms. By [[Def - Curvature of a Principal Connection]] the curvature is **horizontal**: $\Omega(Y,Z)=d\omega(\pi_HY,\pi_HZ)=0$ whenever $Y$ or $Z$ is vertical, because $\pi_H$ annihilates vertical vectors. Each $W_i$ is vertical (a fundamental vector), so the three terms $\Omega(X_1,W_2)$, $\Omega(W_1,X_2)$, $\Omega(W_1,W_2)$ all vanish, leaving
> $$F_\beta|_{u_0}(v_1,v_2)=\Omega_{s_\beta(u_0)}\big(X_1,X_2\big)=\Omega_{s_\alpha(u_0)\cdot g_0}\Big(dR_{g_0}d_{u_0}s_\alpha(v_1),\,dR_{g_0}d_{u_0}s_\alpha(v_2)\Big) \qquad\text{(horizontality of }\Omega\text{ kills the }W_i\text{ terms).}$$
> Now use the equivariance of the curvature $R_g^*\Omega=\operatorname{Ad}_{g^{-1}}\circ\Omega$, proved on [[Thm - Structure Equation for the Curvature]] (namely $\big(R_{g_0}^*\Omega\big)(Y_1,Y_2)=\operatorname{Ad}_{g_0^{-1}}\Omega(Y_1,Y_2)$), at $p=s_\alpha(u_0)$ with $Y_i=d_{u_0}s_\alpha(v_i)$:
> $$\Omega_{s_\alpha(u_0)g_0}\big(dR_{g_0}Y_1,dR_{g_0}Y_2\big)=\big(R_{g_0}^*\Omega\big)_{s_\alpha(u_0)}(Y_1,Y_2)=\operatorname{Ad}_{g_0^{-1}}\Omega_{s_\alpha(u_0)}(Y_1,Y_2)=\operatorname{Ad}_{g_0^{-1}}\!\big(F_\alpha|_{u_0}(v_1,v_2)\big) \qquad\text{(equivariance of }\Omega\text{; }F_\alpha=s_\alpha^*\Omega\text{).}$$
> Therefore $F_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha$ on $U_{\alpha\beta}$, with no additive term. This proves the transformation law in (c).
>
> **Part (c), gluing.** Define, on each $U_\alpha$, the local $\Lambda^2T^*M\otimes\operatorname{ad}P$-valued object $\sigma_\alpha:=[s_\alpha,F_\alpha]$, meaning $\sigma_\alpha(v_1,v_2):=\big[s_\alpha,\,F_\alpha(v_1,v_2)\big]\in\operatorname{ad}P$. On $U_{\alpha\beta}$, using $s_\beta=s_\alpha g_{\alpha\beta}$, the just-proved law $F_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha$, and the defining relation $[p\cdot g,\operatorname{Ad}_{g^{-1}}X]=[p,X]$ of $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$ (see [[Def - Adjoint Bundles ad P and Ad P]]),
> $$\sigma_\beta(v_1,v_2)=\big[s_\beta,F_\beta(v_1,v_2)\big]=\big[s_\alpha g_{\alpha\beta},\,\operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha(v_1,v_2)\big]=\big[s_\alpha,F_\alpha(v_1,v_2)\big]=\sigma_\alpha(v_1,v_2).$$
> Hence the $\sigma_\alpha$ agree on all overlaps and define a single global $F=F_\omega\in\Omega^2(M;\operatorname{ad}P)$ with $F|_{U_\alpha}=[s_\alpha,F_\alpha]$. By [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space]], the horizontal $\operatorname{Ad}$-equivariant form $\Omega$ corresponds to a unique $\overline\Omega\in\Omega^2(M;\operatorname{ad}P)$ characterised by $\pi^*$-compatibility, equivalently by $\overline\Omega|_{U_\alpha}=[s_\alpha,s_\alpha^*\Omega]=[s_\alpha,F_\alpha]$; since $F$ has the same local description, $F=\overline\Omega$, the descended curvature of [[Def - Curvature of a Principal Connection]]. If $G$ is abelian then $\operatorname{Ad}_g=\operatorname{id}_{\mathfrak g}$ for all $g$, so $F_\beta=F_\alpha$ on overlaps and the $F_\alpha$ themselves glue to a global $\mathfrak g$-valued form $F\in\Omega^2(M;\mathfrak g)$ (equivalently $\operatorname{ad}P=M\times\mathfrak g$ is trivial). This proves (c).
>
> **Part (b) — reconstruction from local data.** We are given a trivialising cover $\{U_\alpha\}$ with transition functions $g_{\alpha\beta}$ (defining $P$ up to isomorphism by [[Thm - Principal Bundles are Classified by Cocycles]]) and forms $A_\alpha\in\Omega^1(U_\alpha;\mathfrak g)$ with
> $$A_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha+g_{\alpha\beta}^*\theta\quad\text{on every }U_{\alpha\beta}. \tag{$\dagger$}$$
>
> *Existence.* By Lemma 2, for each $\alpha$ there is a unique connection $\omega^{(\alpha)}\in\mathcal A(P|_{U_\alpha})$ with $s_\alpha^*\omega^{(\alpha)}=A_\alpha$. We claim $\omega^{(\alpha)}=\omega^{(\beta)}$ on $P|_{U_{\alpha\beta}}$. Indeed, $\omega^{(\beta)}$ is a genuine connection on $P|_{U_\beta}\supseteq P|_{U_{\alpha\beta}}$, and both gauges $s_\alpha,s_\beta$ are defined on $U_{\alpha\beta}$ with $s_\beta=s_\alpha g_{\alpha\beta}$; so part (a), applied to the connection $\omega^{(\beta)}$ over $U_{\alpha\beta}$, gives
> $$s_\beta^*\omega^{(\beta)}=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}\big(s_\alpha^*\omega^{(\beta)}\big)+g_{\alpha\beta}^*\theta \qquad\text{(part (a) for }\omega^{(\beta)}\text{).}$$
> The left side is $A_\beta$ (as $s_\beta^*\omega^{(\beta)}=A_\beta$ by construction). Comparing with the hypothesis $(\dagger)$, $A_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha+g_{\alpha\beta}^*\theta$, and subtracting the common $g_{\alpha\beta}^*\theta$ and applying the invertible linear map $\operatorname{Ad}_{g_{\alpha\beta}}$,
> $$s_\alpha^*\omega^{(\beta)}=A_\alpha=s_\alpha^*\omega^{(\alpha)} \qquad\text{(cancel }g_{\alpha\beta}^*\theta\text{; apply }\operatorname{Ad}_{g_{\alpha\beta}}\text{ to both sides).}$$
> Thus $\omega^{(\alpha)}$ and $\omega^{(\beta)}$ are two connections on the trivialising patch $U_{\alpha\beta}$ (with gauge $s_\alpha$) having the same local form $A_\alpha$; by the uniqueness clause of Lemma 2 they coincide on $P|_{U_{\alpha\beta}}$. Since the $P|_{U_\alpha}$ cover $P$ and the $\omega^{(\alpha)}$ agree on all overlaps, they patch to a single one-form $\omega\in\Omega^1(P;\mathfrak g)$ with $\omega|_{P|_{U_\alpha}}=\omega^{(\alpha)}$. Conditions (1) and (2) hold pointwise, and each point of $P$ lies in some $P|_{U_\alpha}$ where $\omega=\omega^{(\alpha)}$ is a connection, so $\omega\in\mathcal A(P)$; and $s_\alpha^*\omega=s_\alpha^*\omega^{(\alpha)}=A_\alpha$.
>
> *Uniqueness.* If $\omega,\omega'\in\mathcal A(P)$ both satisfy $s_\alpha^*\omega=s_\alpha^*\omega'=A_\alpha$ for all $\alpha$, then on each trivialising patch $U_\alpha$ they have equal local forms, so by the uniqueness clause of Lemma 2 they agree on $P|_{U_\alpha}$; as these cover $P$, $\omega=\omega'$. This proves (b).
>
> **Consistency remark.** The hypothesis $(\dagger)$ is not over-determined on triple overlaps: substituting $g_{\alpha\gamma}=g_{\alpha\beta}g_{\beta\gamma}$ into the law and using the Maurer–Cartan product rule $(g_{\alpha\beta}g_{\beta\gamma})^*\theta=\operatorname{Ad}_{g_{\beta\gamma}^{-1}}\big(g_{\alpha\beta}^*\theta\big)+g_{\beta\gamma}^*\theta$ (Corollary of [[Def - The Maurer-Cartan Form]]) shows that $(\dagger)$ on $U_{\alpha\beta}$ and on $U_{\beta\gamma}$ imply $(\dagger)$ on $U_{\alpha\gamma}$, so the cocycle of transformation laws is self-consistent. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry: transformation of Christoffel symbols.** On a manifold $M$ with the Levi-Civita connection $\nabla$, take two coordinate charts with coordinate frames $e=(\partial_1,\dots,\partial_n)$ and $e'=(\partial_1',\dots,\partial_n')$, related on the overlap by the Jacobian $g=\big(\partial x^i/\partial x'^j\big)\colon U\to GL_n$. The Christoffel symbols are the entries of the connection matrices $A(\nabla,e)$ and $A(\nabla,e')$, which are the local connection forms $e^*\omega$ and $e'^*\omega$ of the induced connection on $\operatorname{Fr}(TM)$. The theorem applies because a change of coordinate frame is a change of gauge; its part (a) reproduces the classical inhomogeneous transformation law of the $\Gamma^i_{jk}$, whose inhomogeneous term $g^{-1}dg$ is exactly what makes $\Gamma$ not a tensor. This is non-obvious because the $\Gamma$'s are usually introduced by a coordinate formula with a mysterious second-derivative term; the theorem explains that term as the Maurer–Cartan pure-gauge contribution.

**Electromagnetism: gauge invariance of the field strength.** A $U(1)$-connection over spacetime is an electromagnetic potential $A=iA_\mu dx^\mu$; a gauge transformation is a map $g=e^{i\chi}\colon U\to U(1)$, and part (a) gives $A\mapsto A+i\,d\chi$, the classical gauge freedom $A_\mu\mapsto A_\mu+\partial_\mu\chi$. Part (c) then gives $F\mapsto F$ (since $U(1)$ is abelian), which is the statement that the electromagnetic field strength $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ is gauge-invariant. The theorem applies because "gauge transformation" is "change of gauge over one patch"; it is non-obvious that the abelian case of a general non-abelian gluing law is precisely the observable/unobservable split of classical electrodynamics.

**Algebraic topology: obstruction to a global gauge.** A principal bundle admits a global section (equivalently is trivial) iff it admits a global gauge, and part (b) says a connection is global data glued from local potentials by the transformation law. Ask when a family of local potentials on the two hemispheres of $S^2$ glues to a connection on a nontrivial $U(1)$-bundle: the transition function $g_{NS}\colon S^1\to U(1)$ on the equator has a winding number, and the failure of a *single* global potential to exist is measured by $\oint_{S^1}g_{NS}^*\theta=2\pi i\cdot(\text{winding})$. The theorem applies because part (b) turns the existence question into a cocycle-compatibility question; the interest is that the very inhomogeneous term $g^*\theta$ that obstructs a global potential integrates to the first Chern number, connecting the local transformation law to a global topological invariant.

---

# Bridges

- **[[Thm - Gauge Transformation Law for Connection 1-Forms]]** (Riemannian Geometry I). This is the frame-bundle, matrix-group case of part (a). For a covariant derivative on a vector bundle $E$, a change of local frame $e'=e\cdot g$ transforms the connection matrix by $A(\nabla,e')=g^{-1}A(\nabla,e)g+g^{-1}dg$. Under the identification $e^*\omega=A(\nabla,e)$ of [[Def - Local Connection Form and Gauge Potential]], the frames $e,e'$ are gauges of the induced connection on $\operatorname{Fr}(E)$ with $G=GL_k$, and the Cartan law becomes the $\operatorname{Ad}_{g^{-1}}A+g^*\theta$ of part (a) with $\operatorname{Ad}_{g^{-1}}X=g^{-1}Xg$ and $g^*\theta=g^{-1}dg$. Haydys derives exactly this in Step 3 of his Theorem 46, differentiating $e'=eg$ through the action map; our Lemma 1 is his Step 1.

- **[[Def - Curvature of a Principal Connection]]** — the source of the horizontality that drives part (c). The curvature is $\Omega(X,Y)=d\omega(\pi_HX,\pi_HY)$, and the single fact that $\pi_H$ deletes vertical vectors is what removes the inhomogeneous term from the curvature's transformation law, in contrast to the connection form, which reads vertical vectors by condition (2). The descended global form $\overline\Omega\in\Omega^2(M;\operatorname{ad}P)$ named there is the $F=F_\omega$ this theorem constructs by gluing.

- **[[Thm - Structure Equation for the Curvature]]** — supplies the equivariance $R_g^*\Omega=\operatorname{Ad}_{g^{-1}}\Omega$ used in part (c), and the local structure equation $F_\alpha=dA_\alpha+\tfrac12[A_\alpha\wedge A_\alpha]$ that defines the local curvature forms this theorem transforms. Combining the two, one may re-derive part (c) purely algebraically by pulling $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$ back along $s_\beta$ and using part (a); the horizontality argument here is the conceptual reason that computation must come out homogeneous.

- **[[Thm - Chern-Weil Theorem]]** (Gauge Theory VI) — the principal consumer of part (c). Because $F$ descends to a global $\operatorname{ad}P$-valued two-form and $\operatorname{Ad}$-invariant polynomials absorb the conjugation $\operatorname{Ad}_{g_{\alpha\beta}^{-1}}$, the scalar forms $f(F)$ are globally defined, closed, and independent of the connection up to exact forms; this is the mechanism by which curvature integrals become characteristic numbers.

---

# Unlocked by This

> [!tip] The affine space of connections *(from this chapter)*
> Part (a) shows that the difference of two connections' local forms transforms homogeneously ($A_\beta-A_\beta'=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}(A_\alpha-A_\alpha')$, since the $g^*\theta$ terms cancel), so it glues to a global element of $\Omega^1(M;\operatorname{ad}P)$. This is the starting point of [[Thm - Existence of Connections on Principal Bundles]]: $\mathcal A(P)$ is an affine space modelled on $\Omega^1(M;\operatorname{ad}P)$.

> [!tip] The Yang–Mills configuration space *(from Gauge Theory VII)*
> Reading part (a) with $g_{\alpha\beta}$ a bundle automorphism gives the gauge-group action $A\mapsto\operatorname{Ad}_{g^{-1}}A+g^*\theta$ on the space of connections; the quotient by this action is the configuration space over which the Yang–Mills functional is defined, and the homogeneous law of part (c) is what makes the functional gauge-invariant.
