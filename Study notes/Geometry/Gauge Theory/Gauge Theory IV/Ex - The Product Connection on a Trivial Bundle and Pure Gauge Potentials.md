---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Connection on a Principal Bundle"
  - "Def - Local Connection Form and Gauge Potential"
  - "Def - The Maurer-Cartan Form"
  - "Def - Fundamental Vector Field of a Group Action"
  - "Thm - Existence of Connections on Principal Bundles"
  - "Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space"
  - "Thm - Transformation of Local Connection and Curvature Forms"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M$ be a smooth manifold, let $G$ be a Lie group with Lie algebra $\mathfrak{g}=T_eG$, and consider the **trivial principal $G$-bundle**
$$P=M\times G\xrightarrow{\ \pi\ }M,\qquad \pi(m,g)=m,$$
on which $G$ acts on the right by right translation in the second factor, $R_h(m,g)=(m,gh)$. Let $\operatorname{pr}_1\colon M\times G\to M$ and $\operatorname{pr}_2\colon M\times G\to G$ be the two projections, and let $\theta\in\Omega^1(G;\mathfrak{g})$ be the (left) **Maurer–Cartan form**, $\theta_g=d_gL_{g^{-1}}\colon T_gG\to\mathfrak{g}$; for a matrix group $\theta=g^{-1}\,dg$.

Prove the following three statements.

1. **The product connection is a connection.** The $\mathfrak{g}$-valued $1$-form
$$\omega_0:=\operatorname{pr}_2^{\,*}\theta\in\Omega^1(M\times G;\mathfrak{g})$$
is a connection $1$-form on $P=M\times G$: it satisfies the equivariance condition $R_h^{\,*}\omega_0=\operatorname{Ad}_{h^{-1}}\omega_0$ for all $h\in G$ and the reproduction condition $\omega_0(\xi_P)=\xi$ for all $\xi\in\mathfrak{g}$, where $\xi_P$ is the fundamental vector field of $\xi$.

2. **Its gauge potential in a translated section is pure gauge.** For any smooth map $g\colon M\to G$, the map
$$s\colon M\to M\times G,\qquad s(m)=(m,g(m)),$$
is a smooth global section, and its local connection form (gauge potential) is
$$A_s:=s^{*}\omega_0=g^{*}\theta\in\Omega^1(M;\mathfrak{g}),$$
which for a matrix group reads $A_s=g^{-1}\,dg$. In particular the identity section $s_0(m)=(m,e)$ has $A_{s_0}=0$, and a section obtained from it by the fibrewise translation $g$ acquires exactly the pure-gauge term $g^{*}\theta$.

3. **Every connection on the trivial bundle is the product connection plus a base form.** For every connection $\omega$ on $M\times G$ there is a unique $\mathfrak{g}$-valued $1$-form $\alpha\in\Omega^1(M;\mathfrak{g})$ on the base with
$$\omega=\operatorname{pr}_2^{\,*}\theta+\widehat{\alpha},\qquad \widehat{\alpha}_{(m,g)}:=\operatorname{Ad}_{g^{-1}}\bigl((\operatorname{pr}_1^{\,*}\alpha)_{(m,g)}\bigr),$$
where $\widehat{\alpha}$ is the horizontal $\operatorname{Ad}$-equivariant "lift" of $\alpha$; concretely $\alpha=s_0^{*}\omega$ is the gauge potential of $\omega$ in the identity section. Thus the affine space of connections on $M\times G$ is $\operatorname{pr}_2^{\,*}\theta+\Omega^1(M;\mathfrak{g})$, an affine space modelled on $\Omega^1(M;\mathfrak{g})$.

**Recall:**

The objects in play are a principal bundle and its right action, the two defining conditions of a connection $1$-form, the fundamental vector field of a Lie-algebra element, the Maurer–Cartan form of $G$, the local connection form (gauge potential) of a connection in a chosen section, and the affine structure of the space of connections.

![[Def - Connection on a Principal Bundle#The Definition]]

A **[[Def - Connection on a Principal Bundle|connection 1-form]]** on a principal $G$-bundle $P\to M$ is a form $\omega\in\Omega^1(P;\mathfrak{g})$ satisfying, for all $h\in G$ and all $\xi\in\mathfrak{g}$,
$$\text{(1)}\quad R_h^{\,*}\omega=\operatorname{Ad}_{h^{-1}}\omega,\qquad\qquad \text{(2)}\quad \omega(\xi_P)=\xi.$$
Condition (1) is $\operatorname{Ad}$-equivariance under the right action; condition (2) says that $\omega$ reproduces the Lie-algebra element generating each vertical direction.

![[Def - Fundamental Vector Field of a Group Action#The Definition]]

The **[[Def - Fundamental Vector Field of a Group Action|fundamental vector field]]** of $\xi\in\mathfrak{g}$ on a right $G$-space $P$ is $\xi_P(p)=\frac{d}{dt}\big|_{t=0}\,p\cdot\exp(t\xi)$. On $P=M\times G$ the point $p=(m,g)$ moves along $t\mapsto(m,g\exp(t\xi))$, so $\xi_P(m,g)=\bigl(0_m,\,d_eL_g(\xi)\bigr)$ — it is vertical (its $\operatorname{pr}_1$-component vanishes) and its $G$-component is the left-translate of $\xi$ to $g$.

![[Def - The Maurer-Cartan Form#The Definition]]

The **[[Def - The Maurer-Cartan Form|Maurer–Cartan form]]** $\theta\in\Omega^1(G;\mathfrak{g})$ is $\theta_g=d_gL_{g^{-1}}\colon T_gG\to T_eG=\mathfrak{g}$. It is left-invariant, $L_h^{\,*}\theta=\theta$, and transforms under right translation by
$$R_h^{\,*}\theta=\operatorname{Ad}_{h^{-1}}\theta\qquad(h\in G).$$
On a left-invariant vector field $\widetilde{\xi}$ (the one with $\widetilde{\xi}(g)=d_eL_g(\xi)$) it returns the constant $\theta(\widetilde{\xi})=\xi$. For a matrix group $\theta=g^{-1}\,dg$, meaning $\theta_g(v)=g^{-1}v$ for $v\in T_gG\subset\operatorname{Mat}(n\times n)$.

![[Def - Local Connection Form and Gauge Potential#The Definition]]

The **[[Def - Local Connection Form and Gauge Potential|local connection form]]** (or **gauge potential**) of a connection $\omega$ in a local section $s\colon U\to P$ is the pullback $A_s:=s^{*}\omega\in\Omega^1(U;\mathfrak{g})$, defined by $A_s(v)=\omega(d s(v))$.

![[Thm - Existence of Connections on Principal Bundles#Statement]]

The relevant part of the **[[Thm - Existence of Connections on Principal Bundles|affine-space theorem]]** is: the set $\mathcal{A}(P)$ of connections on a principal $G$-bundle $P\to M$ is a non-empty affine space modelled on $\Omega^1(M;\operatorname{ad}P)$; the difference $\omega-\omega'$ of two connections is a horizontal $\operatorname{Ad}$-equivariant $\mathfrak{g}$-valued $1$-form, hence corresponds to a unique base form $b\in\Omega^1(M;\operatorname{ad}P)$, and conversely adding the lift of any such $b$ to a connection yields a connection. Here $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak{g}$ is the adjoint bundle.

The correspondence between base forms and horizontal equivariant forms on the total space is the content of **[[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|the basic-forms theorem]]**: a form $\beta\in\Omega^q(M;P\times_\rho V)$ corresponds bijectively to a form $\widehat{\beta}\in\Omega^q(P;V)$ that is *horizontal* ($\widehat{\beta}$ vanishes when any argument is vertical) and *$\rho$-equivariant* ($R_h^{\,*}\widehat{\beta}=\rho(h^{-1})\widehat{\beta}$), via $\beta_{\pi(p)}=[\,p,\widehat{\beta}_p\,]$; for the adjoint representation $\rho=\operatorname{Ad}$ this reads $R_h^{\,*}\widehat{\beta}=\operatorname{Ad}_{h^{-1}}\widehat{\beta}$.

---

# Convergent Strategy

**Problem class.** This is a *verification-and-parametrisation* drill: three short computations that together turn the trivial bundle into the concrete model on which every later local formula is calibrated. Part 1 checks two defining conditions against a given candidate; part 2 pulls a form back along a section; part 3 parametrises an entire affine space by identifying its origin (the product connection) and its model vector space ($\Omega^1(M;\mathfrak{g})$). The whole point is that on $M\times G$ the general principal-bundle machinery becomes explicit and hand-computable, so this is the example one returns to whenever a sign or a transformation law is in doubt.

**Assumption pattern.** The single structural fact that makes every part work is that $\theta$ is the *left*-invariant Maurer–Cartan form, whose two properties — $R_h^{\,*}\theta=\operatorname{Ad}_{h^{-1}}\theta$ and $\theta(\widetilde{\xi})=\xi$ on left-invariant fields — are exactly the two defining conditions of a connection, transported to $G$. Recognising "the vertical directions of $M\times G$ are a copy of $G$, and $\theta$ already reads off the generating Lie-algebra element there" is the whole insight. The recognisable trigger for part 3 is that we want to describe *all* connections and we already possess *one* distinguished connection together with a theorem saying the connections form an affine space; the move is always "fix the distinguished point, then identify the model vector space".

**Theorem routing.** Part 1 routes through the two properties of **[[Def - The Maurer-Cartan Form|the Maurer–Cartan form]]** and the naturality of pullback under the commuting squares $\operatorname{pr}_2\circ R_h=R_h\circ\operatorname{pr}_2$ and $\operatorname{pr}_2\circ\text{(fundamental flow)}$. Part 2 is a one-line pullback identity $s^{*}\operatorname{pr}_2^{\,*}\theta=(\operatorname{pr}_2\circ s)^{*}\theta=g^{*}\theta$, using $\operatorname{pr}_2\circ s=g$. Part 3 routes through **[[Thm - Existence of Connections on Principal Bundles|the affine-space theorem]]** and **[[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|the basic-forms theorem]]**, plus the triviality $\operatorname{ad}(M\times G)\cong M\times\mathfrak{g}$ coming from the global identity section $s_0$.

**Key decision point.** The one genuinely non-obvious step is the *shape of the lift* in part 3. The naïve guess $\omega=\operatorname{pr}_2^{\,*}\theta+\operatorname{pr}_1^{\,*}\alpha$ is *wrong* for non-abelian $G$: $\operatorname{pr}_1^{\,*}\alpha$ is horizontal but not $\operatorname{Ad}$-equivariant, so the sum fails condition (1) unless $\alpha$ happens to be pointwise $\operatorname{Ad}$-invariant (automatic when $G$ is abelian, forcing $\alpha=0$ for, say, $G=SU(2)$). The correct lift carries a compensating $\operatorname{Ad}_{g^{-1}}$ factor: $\widehat{\alpha}_{(m,g)}=\operatorname{Ad}_{g^{-1}}(\operatorname{pr}_1^{\,*}\alpha)_{(m,g)}$. Deciding to insert that twist — and understanding that it is exactly what the basic-forms correspondence demands — is the crux of the parametrisation.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory IV — Connections and Curvature on Principal Bundles#Legal Operations|the topic page's Legal Operations]]; where the topic page is not yet assembled, each is named descriptively.

1. **Pull a connection or its defining conditions back through a bundle map.** Both defining conditions of a connection are checked by pulling $\theta$ back along $\operatorname{pr}_2$ and using that $\operatorname{pr}_2$ intertwines the actions: $\operatorname{pr}_2\circ R_h=R_h\circ\operatorname{pr}_2$ turns condition (1) for $\omega_0$ into condition (1) for $\theta$.

2. **Compute a gauge potential as a composite pullback.** The gauge potential $s^{*}\omega_0$ is evaluated by collapsing $s^{*}\operatorname{pr}_2^{\,*}=(\operatorname{pr}_2\circ s)^{*}$, reducing an apparently bundle-level computation to a pullback on the base.

3. **Recognise the fundamental vector field of a product bundle explicitly.** On $M\times G$ the fundamental field $\xi_P(m,g)=(0,d_eL_g\xi)$ is written out in coordinates, so that condition (2) becomes the Maurer–Cartan reproduction property $\theta(\widetilde{\xi})=\xi$.

4. **Parametrise an affine space by a chosen origin plus its model vector space.** Given one connection $\operatorname{pr}_2^{\,*}\theta$ and the affine-space theorem, every connection is written as origin-plus-difference, and the difference is identified with a base form.

5. **Trivialise the adjoint bundle via a global section.** The global identity section $s_0$ makes $\operatorname{ad}(M\times G)\cong M\times\mathfrak{g}$, so that $\Omega^1(M;\operatorname{ad}P)\cong\Omega^1(M;\mathfrak{g})$ and the model vector space of the affine space becomes ordinary $\mathfrak{g}$-valued forms.

---

# Hints

> [!note]- Hint 1
> For part 1 you must verify two things about $\omega_0=\operatorname{pr}_2^{\,*}\theta$: equivariance $R_h^{\,*}\omega_0=\operatorname{Ad}_{h^{-1}}\omega_0$, and $\omega_0(\xi_P)=\xi$. Do not compute anything on $M\times G$ directly; instead push everything down to $G$ using $\operatorname{pr}_2$. What is $\operatorname{pr}_2\circ R_h$ as a map $M\times G\to G$? And where does the fundamental vector field $\xi_P(m,g)$ go under $d\operatorname{pr}_2$?

> [!note]- Hint 2
> The two properties of the Maurer–Cartan form you need are stated on [[Def - The Maurer-Cartan Form|its page]]: $R_h^{\,*}\theta=\operatorname{Ad}_{h^{-1}}\theta$ on $G$, and $\theta(\widetilde{\xi})=\xi$ where $\widetilde{\xi}$ is the left-invariant field extending $\xi$. Notice that $d\operatorname{pr}_2$ sends $\xi_P(m,g)=(0,d_eL_g\xi)$ to $d_eL_g\xi=\widetilde{\xi}(g)$ — exactly the left-invariant field on which $\theta$ returns $\xi$.

> [!note]- Hint 3
> Part 2 is a single line. The section is $s=(\operatorname{id}_M,g)\colon M\to M\times G$, so $\operatorname{pr}_2\circ s=g\colon M\to G$. Now use functoriality of pullback, $s^{*}\operatorname{pr}_2^{\,*}=(\operatorname{pr}_2\circ s)^{*}$.

> [!note]- Hint 4
> For part 3, invoke [[Thm - Existence of Connections on Principal Bundles|the affine-space theorem]]: any connection $\omega$ has $\omega-\omega_0$ a *horizontal, $\operatorname{Ad}$-equivariant* $\mathfrak{g}$-valued $1$-form, corresponding to a base form. Do **not** guess $\omega=\omega_0+\operatorname{pr}_1^{\,*}\alpha$: check whether $\operatorname{pr}_1^{\,*}\alpha$ is $\operatorname{Ad}$-equivariant. It is not, unless $G$ is abelian. What factor must you insert so that $R_h^{\,*}(\text{lift})=\operatorname{Ad}_{h^{-1}}(\text{lift})$?

> [!note]- Hint 5
> The corrected lift is $\widehat{\alpha}_{(m,g)}=\operatorname{Ad}_{g^{-1}}(\operatorname{pr}_1^{\,*}\alpha)_{(m,g)}$. Verify $R_h^{\,*}\widehat{\alpha}=\operatorname{Ad}_{h^{-1}}\widehat{\alpha}$ using $\operatorname{Ad}_{(gh)^{-1}}=\operatorname{Ad}_{h^{-1}}\operatorname{Ad}_{g^{-1}}$, and check $\widehat{\alpha}$ is horizontal because $\operatorname{pr}_1$ kills vertical vectors. Recover $\alpha$ from $\omega$ by pulling back along the identity section: $\alpha=s_0^{*}\omega$.

---

# Solution

The three parts are one idea seen three times: on $M\times G$ the vertical directions are literally a copy of $G$, and the Maurer–Cartan form $\theta$ is the connection that reads off the generating Lie-algebra element there. Part 1 verifies that $\operatorname{pr}_2^{\,*}\theta$ satisfies the two axioms because $\theta$ does; part 2 pulls it back through a translated section and finds the pure-gauge term $g^{*}\theta$; part 3 uses the affine-space theorem to see that the only freedom in a connection on $M\times G$ is a $\mathfrak{g}$-valued $1$-form on the base, lifted with the equivariance-restoring twist $\operatorname{Ad}_{g^{-1}}$.

**Step 1: The fundamental vector field on $M\times G$, written out.**

For $\xi\in\mathfrak{g}$ the fundamental vector field is $\xi_P(m,g)=(0_m,\ d_eL_g(\xi))$, vertical and equal to the left-invariant field $\widetilde{\xi}$ in the $G$-slot.

> [!note]- Derivation
> By the definition of the fundamental vector field, $\xi_P(m,g)=\frac{d}{dt}\big|_{t=0}\,(m,g)\cdot\exp(t\xi)$. The right action is right translation in the second factor, so
> $$(m,g)\cdot\exp(t\xi)=(m,\,g\exp(t\xi))\qquad\text{(definition of the right action on }M\times G\text{)}.$$
> Differentiating each component at $t=0$: the first component is the constant $m$, contributing $0_m\in T_mM$; the second is the curve $t\mapsto g\exp(t\xi)=L_g(\exp(t\xi))$ in $G$, whose velocity at $t=0$ is
> $$\tfrac{d}{dt}\big|_{0}L_g(\exp(t\xi))=d_eL_g\bigl(\tfrac{d}{dt}\big|_0\exp(t\xi)\bigr)=d_eL_g(\xi)\qquad\text{(chain rule; }\tfrac{d}{dt}\big|_0\exp(t\xi)=\xi\text{)}.$$
> Here $\widetilde{\xi}(g):=d_eL_g(\xi)$ is by definition the value at $g$ of the left-invariant vector field $\widetilde{\xi}$ extending $\xi\in\mathfrak{g}=T_eG$. Hence
> $$\xi_P(m,g)=\bigl(0_m,\ \widetilde{\xi}(g)\bigr).$$
> In particular $d\operatorname{pr}_2\bigl(\xi_P(m,g)\bigr)=\widetilde{\xi}(g)$, since $\operatorname{pr}_2$ forgets the first component.

**Step 2: The product form $\omega_0=\operatorname{pr}_2^{\,*}\theta$ satisfies the reproduction condition (2).**

For every $\xi\in\mathfrak{g}$, $\omega_0(\xi_P)=\xi$.

> [!note]- Derivation
> We evaluate $\omega_0$ on the fundamental field at an arbitrary point $(m,g)$:
> $$\omega_0\bigl(\xi_P(m,g)\bigr)=(\operatorname{pr}_2^{\,*}\theta)\bigl(\xi_P(m,g)\bigr)=\theta_g\bigl(d\operatorname{pr}_2(\xi_P(m,g))\bigr)\qquad\text{(definition of pullback of a }1\text{-form)}.$$
> By Step 1, $d\operatorname{pr}_2(\xi_P(m,g))=\widetilde{\xi}(g)$, so
> $$\omega_0\bigl(\xi_P(m,g)\bigr)=\theta_g\bigl(\widetilde{\xi}(g)\bigr)=\xi\qquad\text{(by the reproduction property }\theta(\widetilde{\xi})=\xi\text{ of the Maurer–Cartan form).}$$
> Since $(m,g)$ was arbitrary, $\omega_0(\xi_P)=\xi$. This is condition (2). For a matrix group the same reads $\theta_g(\widetilde{\xi}(g))=g^{-1}\,(g\xi)=\xi$, using $\widetilde{\xi}(g)=g\xi$ and $\theta_g(v)=g^{-1}v$.

**Step 3: $\omega_0$ satisfies the equivariance condition (1).**

For every $h\in G$, $R_h^{\,*}\omega_0=\operatorname{Ad}_{h^{-1}}\omega_0$.

> [!note]- Derivation
> The right translation on $M\times G$ is $R_h(m,g)=(m,gh)$, and it commutes with $\operatorname{pr}_2$ in the sense that the right translation $R_h^{G}$ on $G$ satisfies
> $$\operatorname{pr}_2\circ R_h=R_h^{G}\circ\operatorname{pr}_2\qquad\text{(both send }(m,g)\mapsto gh\text{)}.$$
> Therefore, by functoriality of pullback ($(\phi\circ\psi)^{*}=\psi^{*}\phi^{*}$),
> $$R_h^{\,*}\omega_0=R_h^{\,*}\operatorname{pr}_2^{\,*}\theta=(\operatorname{pr}_2\circ R_h)^{*}\theta=(R_h^{G}\circ\operatorname{pr}_2)^{*}\theta=\operatorname{pr}_2^{\,*}\bigl((R_h^{G})^{*}\theta\bigr)\qquad\text{(functoriality of pullback).}$$
> By the right-translation property of the Maurer–Cartan form, $(R_h^{G})^{*}\theta=\operatorname{Ad}_{h^{-1}}\theta$, and $\operatorname{Ad}_{h^{-1}}$ is a fixed linear endomorphism of $\mathfrak{g}$ that commutes with pullback of $\mathfrak{g}$-valued forms (pullback acts on the form part, $\operatorname{Ad}_{h^{-1}}$ on the $\mathfrak{g}$-value part). Hence
> $$R_h^{\,*}\omega_0=\operatorname{pr}_2^{\,*}\bigl(\operatorname{Ad}_{h^{-1}}\theta\bigr)=\operatorname{Ad}_{h^{-1}}\operatorname{pr}_2^{\,*}\theta=\operatorname{Ad}_{h^{-1}}\omega_0.$$
> This is condition (1). Steps 2 and 3 together show $\omega_0$ is a connection $1$-form, proving part 1.

**Step 4: The gauge potential of $\omega_0$ in the section $s=(\operatorname{id}_M,g)$ is $g^{*}\theta$.**

For $s(m)=(m,g(m))$, $A_s=s^{*}\omega_0=g^{*}\theta$.

> [!note]- Derivation
> The map $s=(\operatorname{id}_M,g)\colon M\to M\times G$ is smooth (both components are), and $\pi\circ s=\operatorname{pr}_1\circ(\operatorname{id}_M,g)=\operatorname{id}_M$, so $s$ is a global section. Its second projection is
> $$\operatorname{pr}_2\circ s=\operatorname{pr}_2\circ(\operatorname{id}_M,g)=g\colon M\to G.$$
> Therefore, again by functoriality of pullback,
> $$A_s=s^{*}\omega_0=s^{*}\operatorname{pr}_2^{\,*}\theta=(\operatorname{pr}_2\circ s)^{*}\theta=g^{*}\theta\qquad\text{(definition of the gauge potential; functoriality).}$$
> For a matrix group $g^{*}\theta=g^{-1}\,dg$ (the pullback of $\theta=g^{-1}dg$ along the map $g$, in the abuse of notation where $g$ denotes both the section-defining map and the coordinate). Taking $g\equiv e$ constant gives the identity section $s_0(m)=(m,e)$ with $A_{s_0}=e^{*}\theta=0$, because $de=0$. Thus the identity section carries the zero potential, and translating it fibrewise by $g$ adds precisely the *pure-gauge* term $g^{*}\theta$. This is the trivial-bundle instance of the general transformation law $A_{s'}=\operatorname{Ad}_{g^{-1}}A_s+g^{*}\theta$ with $A_s=0$: see [[Thm - Transformation of Local Connection and Curvature Forms|the transformation theorem]]. This proves part 2.

**Step 5: The lift $\widehat{\alpha}$ of a base form is horizontal and $\operatorname{Ad}$-equivariant.**

For $\alpha\in\Omega^1(M;\mathfrak{g})$ set $\widehat{\alpha}_{(m,g)}=\operatorname{Ad}_{g^{-1}}(\operatorname{pr}_1^{\,*}\alpha)_{(m,g)}$. Then $\widehat{\alpha}$ vanishes on vertical vectors and satisfies $R_h^{\,*}\widehat{\alpha}=\operatorname{Ad}_{h^{-1}}\widehat{\alpha}$.

> [!note]- Derivation
> *Horizontality.* A vertical vector at $(m,g)$ has the form $(0_m,w)$ with $w\in T_gG$. Then $d\operatorname{pr}_1(0_m,w)=0_m$, so $(\operatorname{pr}_1^{\,*}\alpha)_{(m,g)}(0_m,w)=\alpha_m(d\operatorname{pr}_1(0_m,w))=\alpha_m(0_m)=0$, and applying the fixed linear map $\operatorname{Ad}_{g^{-1}}$ leaves it $0$. Hence $\widehat{\alpha}$ kills all vertical vectors; it is horizontal.
>
> *Equivariance.* Fix $h\in G$ and a tangent vector $v\in T_{(m,g)}(M\times G)$. Since $R_h(m,g)=(m,gh)$ and $\operatorname{pr}_1\circ R_h=\operatorname{pr}_1$,
> $$(R_h^{\,*}\widehat{\alpha})_{(m,g)}(v)=\widehat{\alpha}_{(m,gh)}(dR_h\,v)=\operatorname{Ad}_{(gh)^{-1}}\bigl((\operatorname{pr}_1^{\,*}\alpha)_{(m,gh)}(dR_h\,v)\bigr)\qquad\text{(definition of }\widehat{\alpha}\text{).}$$
> Because $\operatorname{pr}_1\circ R_h=\operatorname{pr}_1$, functoriality gives $R_h^{\,*}\operatorname{pr}_1^{\,*}\alpha=\operatorname{pr}_1^{\,*}\alpha$, that is $(\operatorname{pr}_1^{\,*}\alpha)_{(m,gh)}(dR_h\,v)=(\operatorname{pr}_1^{\,*}\alpha)_{(m,g)}(v)$. Using also $\operatorname{Ad}_{(gh)^{-1}}=\operatorname{Ad}_{h^{-1}g^{-1}}=\operatorname{Ad}_{h^{-1}}\operatorname{Ad}_{g^{-1}}$ (the adjoint representation is a homomorphism),
> $$(R_h^{\,*}\widehat{\alpha})_{(m,g)}(v)=\operatorname{Ad}_{h^{-1}}\operatorname{Ad}_{g^{-1}}\bigl((\operatorname{pr}_1^{\,*}\alpha)_{(m,g)}(v)\bigr)=\operatorname{Ad}_{h^{-1}}\bigl(\widehat{\alpha}_{(m,g)}(v)\bigr).$$
> Since $v$ and $(m,g)$ were arbitrary, $R_h^{\,*}\widehat{\alpha}=\operatorname{Ad}_{h^{-1}}\widehat{\alpha}$. Thus $\widehat{\alpha}$ is a horizontal $\operatorname{Ad}$-equivariant form. Its pullback by the identity section recovers $\alpha$: $s_0^{*}\widehat{\alpha}$ has value at $m$ equal to $\operatorname{Ad}_{e^{-1}}(\alpha_m)=\alpha_m$ (using $g=e$ on the image of $s_0$), so $s_0^{*}\widehat{\alpha}=\alpha$.

> [!warning] Illegal but tempting route: the untwisted lift $\operatorname{pr}_1^{\,*}\alpha$
> It is tempting to write $\omega=\operatorname{pr}_2^{\,*}\theta+\operatorname{pr}_1^{\,*}\alpha$. The form $\operatorname{pr}_1^{\,*}\alpha$ is horizontal, but it is $\operatorname{Ad}$-equivariant only if $\operatorname{Ad}_{h^{-1}}\alpha=\alpha$ for all $h$, i.e. only if $\alpha$ takes values in the $\operatorname{Ad}$-invariants of $\mathfrak{g}$. For abelian $G$ (for instance $G=U(1)$) the adjoint action is trivial and $\operatorname{pr}_1^{\,*}\alpha=\widehat{\alpha}$, so the untwisted lift is legal and every connection is honestly $\operatorname{pr}_2^{\,*}\theta+\operatorname{pr}_1^{\,*}\alpha$. For non-abelian $G$ (for instance $G=SU(2)$, whose adjoint action has no nonzero invariants) the untwisted $\operatorname{pr}_2^{\,*}\theta+\operatorname{pr}_1^{\,*}\alpha$ is a connection only when $\alpha=0$. The extra condition that makes the untwisted route legal is thus *pointwise $\operatorname{Ad}$-invariance of $\alpha$*; the twist $\operatorname{Ad}_{g^{-1}}$ removes that condition.

**Step 6: Every connection on $M\times G$ is $\operatorname{pr}_2^{\,*}\theta+\widehat{\alpha}$ for a unique $\alpha$.**

For each connection $\omega$ there is a unique $\alpha\in\Omega^1(M;\mathfrak{g})$ with $\omega=\operatorname{pr}_2^{\,*}\theta+\widehat{\alpha}$, namely $\alpha=s_0^{*}\omega$.

> [!note]- Derivation
> By part 1, $\omega_0=\operatorname{pr}_2^{\,*}\theta$ is a connection, so $\mathcal{A}(M\times G)\neq\varnothing$. By [[Thm - Existence of Connections on Principal Bundles|the affine-space theorem]], the difference $\tau:=\omega-\omega_0$ of the two connections is a *horizontal, $\operatorname{Ad}$-equivariant* $\mathfrak{g}$-valued $1$-form on $M\times G$: horizontal because both connections agree on vertical vectors (each returns $\xi$ on $\xi_P$, so their difference is $0$ there), and $\operatorname{Ad}$-equivariant because $R_h^{\,*}\tau=R_h^{\,*}\omega-R_h^{\,*}\omega_0=\operatorname{Ad}_{h^{-1}}\omega-\operatorname{Ad}_{h^{-1}}\omega_0=\operatorname{Ad}_{h^{-1}}\tau$ (condition (1) for each of $\omega,\omega_0$).
>
> By [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|the basic-forms theorem]], such a $\tau$ corresponds to a unique base form $b\in\Omega^1(M;\operatorname{ad}P)$ with $\tau=\widehat{b}$. The trivial bundle has a global section $s_0$, which trivialises the adjoint bundle: $\operatorname{ad}(M\times G)=(M\times G)\times_{\operatorname{Ad}}\mathfrak{g}\cong M\times\mathfrak{g}$ by $[\,(m,g),\xi\,]\mapsto(m,\operatorname{Ad}_g\xi)$, an isomorphism of vector bundles because $s_0$ has trivial transition functions. Under it $\Omega^1(M;\operatorname{ad}P)\cong\Omega^1(M;\mathfrak{g})$, and $b$ becomes $\alpha:=s_0^{*}\tau=s_0^{*}(\omega-\omega_0)=s_0^{*}\omega-0=s_0^{*}\omega$ (using $s_0^{*}\omega_0=A_{s_0}=0$ from Step 4). By Step 5 the horizontal $\operatorname{Ad}$-equivariant form with $s_0^{*}(\cdot)=\alpha$ is exactly $\widehat{\alpha}$, and the correspondence is a bijection, so $\tau=\widehat{\alpha}$. Therefore
> $$\omega=\operatorname{pr}_2^{\,*}\theta+\widehat{\alpha},\qquad\alpha=s_0^{*}\omega,$$
> with $\alpha$ unique. Conversely, for any $\alpha\in\Omega^1(M;\mathfrak{g})$ the form $\operatorname{pr}_2^{\,*}\theta+\widehat{\alpha}$ is a connection: adding a horizontal $\operatorname{Ad}$-equivariant form to a connection preserves both defining conditions (horizontality means the reproduction condition (2) is untouched, and Step 5 gives the equivariance (1)). Hence $\mathcal{A}(M\times G)=\operatorname{pr}_2^{\,*}\theta+\{\widehat{\alpha}:\alpha\in\Omega^1(M;\mathfrak{g})\}$ is an affine space modelled on $\Omega^1(M;\mathfrak{g})$, proving part 3.

> [!note]- Complete formal solution
> **Claim.** On the trivial bundle $P=M\times G\to M$: (1) $\omega_0=\operatorname{pr}_2^{\,*}\theta$ is a connection; (2) the section $s=(\operatorname{id}_M,g)$ has gauge potential $A_s=g^{*}\theta$; (3) every connection is $\operatorname{pr}_2^{\,*}\theta+\widehat{\alpha}$ for a unique $\alpha\in\Omega^1(M;\mathfrak{g})$, where $\widehat{\alpha}_{(m,g)}=\operatorname{Ad}_{g^{-1}}(\operatorname{pr}_1^{\,*}\alpha)_{(m,g)}$.
>
> *Part 1.* The fundamental field is $\xi_P(m,g)=\frac{d}{dt}\big|_0(m,g\exp(t\xi))=(0,\,d_eL_g\xi)=(0,\widetilde{\xi}(g))$, so $d\operatorname{pr}_2(\xi_P(m,g))=\widetilde{\xi}(g)$. Hence $\omega_0(\xi_P(m,g))=\theta_g(\widetilde{\xi}(g))=\xi$ by the reproduction property $\theta(\widetilde{\xi})=\xi$; this is condition (2). For equivariance, $\operatorname{pr}_2\circ R_h=R_h^{G}\circ\operatorname{pr}_2$ gives $R_h^{\,*}\omega_0=\operatorname{pr}_2^{\,*}((R_h^{G})^{*}\theta)=\operatorname{pr}_2^{\,*}(\operatorname{Ad}_{h^{-1}}\theta)=\operatorname{Ad}_{h^{-1}}\omega_0$, condition (1). So $\omega_0$ is a connection.
>
> *Part 2.* $s=(\operatorname{id}_M,g)$ is a section since $\pi\circ s=\operatorname{id}_M$, and $\operatorname{pr}_2\circ s=g$, so $A_s=s^{*}\operatorname{pr}_2^{\,*}\theta=(\operatorname{pr}_2\circ s)^{*}\theta=g^{*}\theta$ (matrix form $g^{-1}dg$). The identity section $s_0$ has $A_{s_0}=e^{*}\theta=0$; translating by $g$ adds the pure-gauge $g^{*}\theta$.
>
> *Part 3.* Given a connection $\omega$, the form $\tau=\omega-\omega_0$ is horizontal (both connections return $\xi$ on $\xi_P$) and $\operatorname{Ad}$-equivariant ($R_h^{\,*}\tau=\operatorname{Ad}_{h^{-1}}\tau$, from condition (1) for each). By the affine-space and basic-forms theorems it equals $\widehat{b}$ for a unique $b\in\Omega^1(M;\operatorname{ad}P)$; the global section $s_0$ trivialises $\operatorname{ad}P\cong M\times\mathfrak{g}$, turning $b$ into $\alpha:=s_0^{*}\tau=s_0^{*}\omega$. Direct computation (Step 5) shows $\widehat{\alpha}$ is horizontal and $\operatorname{Ad}$-equivariant with $s_0^{*}\widehat{\alpha}=\alpha$, so $\tau=\widehat{\alpha}$ and $\omega=\operatorname{pr}_2^{\,*}\theta+\widehat{\alpha}$. Conversely every such sum is a connection. Uniqueness of $\alpha$ is uniqueness in the basic-forms correspondence. $\blacksquare$

---

# Key Takeaways

**The trivial bundle is the calculation you calibrate every local formula against, and its distinguished connection has zero potential in the identity gauge.** The product connection $\operatorname{pr}_2^{\,*}\theta$ is the unique connection on $M\times G$ whose horizontal subspace at $(m,g)$ is $T_mM\times\{0\}$ — the "obvious" flat splitting — and in the identity section $s_0(m)=(m,e)$ its gauge potential is exactly $0$. Whenever a computation on a general bundle is done in a local trivialisation, one is silently comparing to this model: a gauge potential $A_s$ is the failure of the chosen section to be horizontal for the given connection, measured against the flat product connection of the trivialisation. The trigger to return here is any doubt about a sign or a transformation law involving $\theta$; the reliable move is to re-derive it on $M\times G$, where $\xi_P(m,g)=(0,\widetilde{\xi}(g))$ and $\theta(\widetilde{\xi})=\xi$ make everything explicit. This is also why "pure gauge" means "$g^{*}\theta$": a potential is pure gauge precisely when it is the gauge potential of the *flat* product connection in some section, i.e. obtained from $0$ by a fibrewise translation.

**"Every connection is a fixed one plus a base form" is the shape of the entire theory of connections, and the trivial bundle is where the model vector space becomes concrete.** The set of connections is never a vector space — the zero form fails the reproduction condition (2) — but it is always an affine space over $\Omega^1(M;\operatorname{ad}P)$. The reusable principle is: *to describe all connections, fix one and identify the difference space.* On $M\times G$ the difference space $\Omega^1(M;\operatorname{ad}P)$ collapses to ordinary $\mathfrak{g}$-valued forms $\Omega^1(M;\mathfrak{g})$ because the global identity section trivialises the adjoint bundle. This is the first instance of a pattern that governs the whole subject: gauge fields on a trivial bundle are literally $\mathfrak{g}$-valued $1$-forms $\alpha$ on spacetime — the physicists' "$A_\mu$" — and the general curved-bundle theory is the statement that these forms are glued across charts by the transformation law $A_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha+g_{\alpha\beta}^{*}\theta$, whose homogeneous part is exactly the $\operatorname{Ad}_{g^{-1}}$ twist that appears already in the lift $\widehat{\alpha}$.

**The compensating $\operatorname{Ad}_{g^{-1}}$ twist is not a technicality but the exact content of "equivariance", and it disappears precisely for abelian groups.** The instinct to lift a base form $\alpha$ to $\operatorname{pr}_1^{\,*}\alpha$ fails because $\operatorname{pr}_1^{\,*}\alpha$ is constant along the fibre while a connection must rotate by $\operatorname{Ad}_{h^{-1}}$ as one moves along the fibre by $h$. The correct lift $\widehat{\alpha}_{(m,g)}=\operatorname{Ad}_{g^{-1}}(\operatorname{pr}_1^{\,*}\alpha)_{(m,g)}$ builds that rotation in. The diagnostic worth internalising: *whenever an object on the base must be transported to the total space of a principal bundle and stay equivariant, expect an $\operatorname{Ad}_{g^{-1}}$ (or $\rho(g^{-1})$) factor*, and expect it to vanish exactly when the relevant representation is trivial — which for the adjoint representation means $G$ abelian. This is why the abelian case ($U(1)$ electromagnetism) is so much simpler than the non-abelian case ($SU(2)$, $SU(3)$ Yang–Mills): for $U(1)$ the gauge potential is a genuine global-looking $i\mathbb{R}$-valued form up to the additive $g^{*}\theta$, whereas for $SU(2)$ the conjugation is unavoidable and connections genuinely mix the Lie-algebra directions. Companion exercises: [[Ex - Connection Forms of the Hopf Connection in the Two Local Sections]] carries out the abelian version on a *non-trivial* $U(1)$-bundle, where two such trivial-looking potentials fail to agree by exactly a pure-gauge term; [[Ex - Curvature of a Connection on a Trivial Bundle and the Abelian Case]] computes what curvature this affine family produces.
