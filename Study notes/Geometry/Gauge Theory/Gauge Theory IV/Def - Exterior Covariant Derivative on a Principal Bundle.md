---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Horizontal Subspace and Horizontal Lift"
  - "Def - Equivariant and Basic Forms on a Principal Bundle"
  - "Def - Curvature of a Principal Connection"
  - "Def - Connection on a Principal Bundle"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
  - "Def - Representation of a Lie Algebra"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a principal $G$-bundle with a smooth right action $R_g(p)=p\cdot g$, and $\omega\in\Omega^1(P;\mathfrak g)$ is a fixed **[[Def - Connection on a Principal Bundle|connection form]]**: a $\mathfrak g$-valued $1$-form on the total space satisfying $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$ and $\omega(\xi_P)=\xi$, where $\mathfrak g=T_eG$ is the Lie algebra and $\xi_P$ is the **[[Def - Fundamental Vector Field of a Group Action|fundamental vector field]]** of $\xi\in\mathfrak g$, defined by $\xi_P(p)=\tfrac{d}{dt}\big|_{t=0}\,p\cdot\exp(t\xi)$. All actions on principal bundles are on the right, following the series convention.

At each $p\in P$ we have the **vertical subspace** $V_p:=\ker d\pi_p=\{\xi_P(p):\xi\in\mathfrak g\}$ (the tangent space to the fibre; the two descriptions agree by [[Def - Equivariant and Basic Forms on a Principal Bundle]]) and the **[[Def - Horizontal Subspace and Horizontal Lift|horizontal subspace]]** $H_p:=\ker\omega_p$. The connection axioms give the $G$-invariant splitting $T_pP=H_p\oplus V_p$ with $dR_g(H_p)=H_{pg}$; the **horizontal projection** $\pi_H\colon T_pP\to H_p$ is the projection onto $H_p$ along $V_p$, and $\pi_V:=\operatorname{id}-\pi_H$ is the vertical projection. A tangent vector $X$ is called horizontal if $\pi_H X=X$ (equivalently $\omega(X)=0$) and vertical if $\pi_H X=0$.

We work with $V$-valued differential forms $\Omega^p(P;V)=\Gamma(\Lambda^pT^*P)\otimes V$ for a fixed finite-dimensional real or complex vector space $V$ carrying a **[[Def - Representation of a Lie Algebra|representation]]** $\rho\colon G\to GL(V)$ with differential $\rho_*=d_e\rho\colon\mathfrak g\to\operatorname{End}(V)$, a Lie algebra homomorphism ($\rho_*[\xi,\eta]=[\rho_*\xi,\rho_*\eta]=\rho_*\xi\,\rho_*\eta-\rho_*\eta\,\rho_*\xi$). Recall from [[Def - Equivariant and Basic Forms on a Principal Bundle]] that $\alpha\in\Omega^p(P;V)$ is:

- **horizontal** if $\alpha(X_0,\dots,X_{p-1})=0$ whenever any $X_i$ is vertical;
- **equivariant of type $\rho$** if $R_g^*\alpha=\rho(g^{-1})\alpha$ for all $g\in G$;
- **basic** if it is both horizontal and equivariant.

We write $\Omega^p_{\mathrm{hor}}(P;V)$, $\Omega^p(P;V)^G_\rho$, and $\Omega^p_{\mathrm{bas}}(P;V)^G_\rho$ for these three subspaces. The **[[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|basic-forms correspondence]]** identifies $\Omega^p_{\mathrm{bas}}(P;V)^G_\rho$ with $\Omega^p(M;E)$, where $E=P\times_\rho V$ is the associated bundle; for $\rho=\operatorname{Ad}$ on $V=\mathfrak g$ this is the [[Def - Adjoint Bundles ad P and Ad P|adjoint bundle]] $\operatorname{ad}P$.

The exterior derivative $d$ acts on $V$-valued forms componentwise (in any basis of $V$); its defining first-order property on a $1$-form is the invariant formula
$$d\beta(X,Y)=X\,\beta(Y)-Y\,\beta(X)-\beta([X,Y]),$$
which is Bär's convention (no $1/(k+1)$ prefactor) and is proved from the coordinate expression on [[Thm - Coordinate Expression for the Exterior Derivative]]. We use the interior product $\iota_X$, the Lie derivative $\mathcal L_X$, and **[[Thm - Cartan's Magic Formula|Cartan's magic formula]]** $\mathcal L_X=d\,\iota_X+\iota_X\,d$, with the convention $(\iota_X\gamma)(X_1,\dots,X_{p-1})=\gamma(X,X_1,\dots,X_{p-1})$.

**The wedge-action of $\mathfrak g$-valued forms on $V$-valued forms.** From [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]], the bilinear map $\mathfrak g\times V\to V$, $(\xi,v)\mapsto\rho_*(\xi)v$, extends to a wedge product: for $\eta\in\Omega^1(P;\mathfrak g)$ and $\alpha\in\Omega^p(P;V)$,
$$\big(\rho_*(\eta)\wedge\alpha\big)(X_0,\dots,X_p):=\sum_{i=0}^{p}(-1)^i\,\rho_*\big(\eta(X_i)\big)\,\alpha(X_0,\dots,\widehat{X_i},\dots,X_p),$$
the hat denoting omission; for $p=0$ this reads $(\rho_*(\eta)\wedge f)(X_0)=\rho_*(\eta(X_0))f$, Haydys's $\eta\cdot f$. The bracket of $\mathfrak g$-valued forms $[\alpha\wedge\beta]$ uses the Lie bracket in place of $\rho_*$; for $1$-forms, $[\alpha\wedge\beta](X,Y)=[\alpha(X),\beta(Y)]-[\alpha(Y),\beta(X)]$, so $[\omega\wedge\omega](X,Y)=2[\omega(X),\omega(Y)]$.

The full symbol registry for the chapter is on **Gauge Theory IV — Connections and Curvature on Principal Bundles**.

> [!warning] Convention: three names for one operator
> Bär defines the curvature by $\Omega(X,Y):=d\omega(\pi_H X,\pi_H Y)$ (Def. 2.4.1) without naming the underlying operator; Haydys writes $d^{\nabla_a}$ for the exterior covariant derivative of the *induced* connection $\nabla_a$ on $\operatorname{ad}P$ (Proposition 53); Kobayashi–Nomizu write $D$ for the operator on $P$ itself. The series writes $D^\omega$ for the operator $(d\,\cdot)\circ\pi_H$ on forms upstairs on $P$, and reserves $d^\nabla$ for the exterior covariant derivative of a connection on a vector bundle over $M$ (chapter II). That the two agree under the basic-forms correspondence is the theorem [[Thm - Exterior Covariant Derivatives on P and on Associated Bundles Agree]]; here we develop $D^\omega$ intrinsically on $P$.

---

# Axiom Motivation

The ordinary exterior derivative $d$ is the one canonical first-order operator on differential forms, but on a principal bundle it does not respect the geometry that a connection provides. Two problems arise, and the exterior covariant derivative is the minimal repair of both.

The first problem is that $d$ does not preserve horizontality. If $\alpha$ is a horizontal $V$-valued form on $P$ — one that "lives on the base", vanishing on vertical directions — then $d\alpha$ need not be horizontal: differentiating in a fibre direction generally produces a form that no longer vanishes on the fibre. Concretely, the connection form $\omega$ itself is *not* horizontal (it is $\xi$ on $\xi_P$), and $d\omega$ has both horizontal and vertical content; the vertical content is exactly what obstructs $d\omega$ from descending to the base. We want an operator that always lands in horizontal forms, because horizontal equivariant forms are precisely the forms that descend to the associated bundle over $M$, by the [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|basic-forms correspondence]]. The one honest way to force a form to be horizontal is to feed its arguments through the horizontal projection $\pi_H$ before evaluating. This is the whole idea: **compose $d$ with $\pi_H$**.

The second problem is a compatibility demand. The whole point of a connection is to differentiate sections of associated bundles covariantly; the covariant derivative $\nabla=\nabla^\omega$ on $E=P\times_\rho V$ (constructed in [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles]]) and its exterior extension $d^\nabla$ live downstairs on $M$. We want an operator upstairs on $P$ that is the exact mirror of $d^\nabla$ under the correspondence $\Omega^\bullet(M;E)\cong\Omega^\bullet_{\mathrm{bas}}(P;V)^G_\rho$, so that identities proved on one side transfer verbatim to the other. The operator $(d\,\cdot)\circ\pi_H$ turns out to do this too, once we check it maps basic forms to basic forms. So the same construction answers both desiderata at once, which is a strong sign it is the right one.

There is exactly one design choice, and it is forced. Why project the arguments of $d\alpha$ rather than, say, project $\alpha$ first and then differentiate, or subtract off the vertical part of $d\alpha$ some other way? Because we need three things simultaneously: the operator must be $\mathbb R$-linear and first order (so it should be built from $d$); it must always output a horizontal form (so a projection must be applied *after* $d$, since $d$ can create vertical content); and on forms already pulled up from the base it must reduce to the de Rham $d$ (so no extra correction term may be inserted by hand). The bare composite $D^\omega\alpha:=(d\alpha)\circ\pi_H$ is the unique operator meeting all three: horizontality is built in, first-orderness is inherited from $d$, and on a pulled-back form $\pi^*\beta$ — which is horizontal and whose exterior derivative $d\pi^*\beta=\pi^*d\beta$ is already horizontal — the projection changes nothing, so $D^\omega\pi^*\beta=\pi^*d\beta$ (verified in the Examples).

What would go wrong if we dropped the projection and used $d$ alone? Then the curvature could not be written as $D^\omega\omega$: the object $d\omega$ is not horizontal, does not descend to the base, and does not equal the curvature. The projection is precisely what discards the fibre-direction bracket term. Indeed, the defining formula of the [[Def - Curvature of a Principal Connection|curvature]], $\Omega(X,Y)=d\omega(\pi_H X,\pi_H Y)$, *is* $D^\omega$ applied to $\omega$; the exterior covariant derivative is the operator of which curvature is the first instance. And what would go wrong if we projected but forgot to check equivariance? We would land in horizontal forms that do not descend, because descent to a bundle over $M$ requires both horizontality and equivariance of type $\rho$; the theorem below shows the projection preserves equivariance for free, so no separate hypothesis is needed. Once these checks are in place the definition is not arbitrary — it is the horizontal shadow of $d$, and every property we want follows from that one description.

---

# The Definition

Let $\pi\colon P\to M$ be a principal $G$-bundle with connection form $\omega$, horizontal projection $\pi_H$, and let $V$ be a vector space (carrying a representation $\rho$ of $G$ when equivariance is at issue). The **exterior covariant derivative** associated with $\omega$ is the operator
$$D^\omega\colon\Omega^p(P;V)\longrightarrow\Omega^{p+1}(P;V),\qquad (D^\omega\alpha)(X_0,\dots,X_p):=d\alpha\big(\pi_H X_0,\dots,\pi_H X_p\big),$$
for tangent vectors $X_0,\dots,X_p\in T_pP$; equivalently $D^\omega\alpha=(d\alpha)\circ\pi_H$, meaning "apply $d$, then restrict to horizontal parts of all arguments". For a $0$-form (a $V$-valued function) $f$ this reads $(D^\omega f)(X)=df(\pi_H X)$.

This formula does define a genuine element of $\Omega^{p+1}(P;V)$. The horizontal projection $\pi_H\colon T_pP\to T_pP$ is a smooth bundle endomorphism (it is the projection onto the smooth horizontal distribution $H=\ker\omega$ along the smooth vertical distribution, both varying smoothly with $p$ by [[Def - Horizontal Subspace and Horizontal Lift]]), and $d\alpha\in\Omega^{p+1}(P;V)$ is a smooth alternating $V$-valued form; precomposing each of the $p+1$ arguments of the multilinear alternating map $d\alpha_p$ with the single linear map $(\pi_H)_p$ produces again a multilinear alternating map, whose dependence on $p$ is smooth because $d\alpha$ and $\pi_H$ are. Hence $D^\omega\alpha$ is a smooth $V$-valued $(p+1)$-form, and $D^\omega\colon\Omega^p(P;V)\to\Omega^{p+1}(P;V)$ is well defined.

The operator is $\mathbb R$-linear (indeed $\mathbb C$-linear when $V$ is complex) because $d$ and $\pi_H$ are. It is first order and satisfies a Leibniz rule against ordinary forms on $M$ pulled up to $P$ (established below). By construction $D^\omega\alpha$ is horizontal: if any $X_i$ is vertical then $\pi_H X_i=0$ and the value is $0$.

**Equivalent description (Bär's curvature form).** The curvature of $\omega$ is the special value $\Omega=D^\omega\omega$, since $\Omega(X,Y)=d\omega(\pi_H X,\pi_H Y)$ is exactly $(D^\omega\omega)(X,Y)$; see [[Def - Curvature of a Principal Connection]].

**Equivalent description on basic forms (the tensorial formula).** If $\alpha$ is basic and equivariant of type $\rho$, then $D^\omega\alpha=d\alpha+\rho_*(\omega)\wedge\alpha$; this second form makes the first-order operator visibly a "corrected exterior derivative" and is what one computes with in a local gauge. The equivalence of the two descriptions on basic forms is proved in the Examples / Corollaries section below.

---

# Categorical / Structural Definition

Structurally, $D^\omega$ is the composite
$$\Omega^p(P;V)\xrightarrow{\;d\;}\Omega^{p+1}(P;V)\xrightarrow{\;\pi_H^\ast\;}\Omega^{p+1}_{\mathrm{hor}}(P;V),$$
where $\pi_H^\ast\gamma:=\gamma\circ\pi_H$ (each argument projected) is the projection of the space of all forms onto the horizontal ones. Three structural facts organise everything on this page. First, $\pi_H^\ast$ is idempotent and its image is $\Omega^\bullet_{\mathrm{hor}}(P;V)$; a horizontal form is a fixed point of $\pi_H^\ast$, and a horizontal form is determined by its values on horizontal vector fields alone (expand each argument as $\pi_H X_i+\pi_V X_i$ and drop the vertical terms). Second, the invariant splitting $dR_g\circ\pi_H=\pi_H\circ dR_g$ (the $G$-invariance of the horizontal distribution) makes $\pi_H^\ast$ commute with the $G$-action, so $D^\omega$ restricts to an operator on the $G$-equivariant complex. Third, on the subcomplex of basic forms of type $\rho$ — which the [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|basic-forms correspondence]] identifies with $\Omega^\bullet(M;E)$, $E=P\times_\rho V$ — the operator $D^\omega$ is *exactly* the exterior covariant derivative $d^{\nabla^\omega}$ of the induced connection on $E$ (this identification is the content of [[Thm - Exterior Covariant Derivatives on P and on Associated Bundles Agree]]).

Thus $D^\omega$ is not a differential of a cochain complex in the naïve sense: it fails $D^\omega\circ D^\omega=0$, and its square measures curvature (Corollary 5). The right structural slogan is that $(\Omega^\bullet_{\mathrm{bas}}(P;V)^G_\rho,\,D^\omega)$ is the pullback to $P$ of the twisted de Rham operator $(\Omega^\bullet(M;E),\,d^{\nabla^\omega})$ of a connection whose curvature is $\rho_*(\Omega)$; it is a genuine complex precisely when that curvature vanishes.

---

# Relate to Other Fields / Compression

The exterior covariant derivative on $P$ is the principal-bundle avatar of an operator the reader has already met over the base. On a vector bundle $E\to M$ with connection $\nabla$, the [[Def - Exterior Covariant Derivative on a Vector Bundle|exterior covariant derivative]] $d^\nabla\colon\Omega^p(M;E)\to\Omega^{p+1}(M;E)$ is defined by the Leibniz rule $d^\nabla(\beta\otimes s)=d\beta\otimes s+(-1)^p\beta\wedge\nabla s$, and its square is the curvature: $d^\nabla\circ d^\nabla=F_\nabla\wedge(\,\cdot\,)$. Every one of those facts has a mirror here — the tensorial formula $D^\omega\alpha=d\alpha+\rho_*(\omega)\wedge\alpha$ is the Leibniz rule read on $P$, and $D^\omega\circ D^\omega=\rho_*(\Omega)\wedge(\,\cdot\,)$ is the curvature-squared identity read on $P$. The two agree object for object under the basic-forms correspondence, which is why one never has to prove the same identity twice.

**True name.** The operational content of $D^\omega$ is *"differentiate, then throw away the fibre-direction"*. Everything the fibre "knows" is coordinatised by $\mathfrak g$ through the connection, and the exterior covariant derivative is the part of $d$ that is invisible to that coordinatisation: it is the exterior derivative as felt along the horizontal distribution. This is why $D^\omega$ on a function is the horizontal part of $df$, why $D^\omega\omega$ is the curvature (the horizontal part of $d\omega$, the failure of the horizontal distribution to be integrable), and why $D^\omega$ reduces to plain $d$ on forms that are already pulled up from the base.

In gauge theory this operator is the covariant exterior derivative of the Yang–Mills field: local field strengths $F_\alpha=dA_\alpha+\tfrac12[A_\alpha\wedge A_\alpha]$ and their Bianchi identity $D^\omega\Omega=0$ (proved on [[Thm - Bianchi Identity for a Principal Connection]]) are both statements about $D^\omega$. In Riemannian geometry, applied to the frame bundle with $\rho$ the standard representation, $D^\omega$ recovers the covariant exterior derivative of the tangent bundle and the second Bianchi identity of the curvature tensor.

---

# Examples / Corollaries

We first prove the structural corollaries — that $D^\omega$ preserves basicness, that curvature is $D^\omega\omega$, the tensorial formula, and the curvature-squared identity — and then verify a concrete instance, a concrete non-instance, and the calibration checks. Every corollary is proved on this page at the full proof standard.

## Corollary 1 — $D^\omega$ maps equivariant forms to basic equivariant forms

**Statement.** If $\alpha\in\Omega^p(P;V)$ is equivariant of type $\rho$, then $D^\omega\alpha$ is basic and equivariant of type $\rho$. In particular $D^\omega\colon\Omega^p_{\mathrm{bas}}(P;V)^G_\rho\to\Omega^{p+1}_{\mathrm{bas}}(P;V)^G_\rho$.

> [!note]- Proof of Corollary 1
> We must show two things: $D^\omega\alpha$ is horizontal, and $D^\omega\alpha$ is equivariant of type $\rho$. Note the hypothesis is only equivariance — horizontality of $\alpha$ is not assumed here.
>
> **Horizontality.** If any argument $X_i$ is vertical, then $\pi_H X_i=0$, so $(D^\omega\alpha)(X_0,\dots,X_p)=d\alpha(\pi_H X_0,\dots,\pi_H X_p)=0$ because one entry of $d\alpha$ is the zero vector and $d\alpha$ is multilinear. Hence $D^\omega\alpha$ vanishes whenever an argument is vertical, i.e. it is horizontal (by the definition of horizontal in Notation).
>
> **Equivariance.** Fix $g\in G$ and tangent vectors $X_0,\dots,X_p\in T_pP$. Two facts enter: the horizontal distribution is $G$-invariant, so $dR_g\circ\pi_H=\pi_H\circ dR_g$ (from [[Def - Horizontal Subspace and Horizontal Lift]]), and pullback commutes with the exterior derivative, $R_g^*d=dR_g^*$ (from [[Thm - Pull-Back Commutes with the Exterior Derivative]]). We compute, writing $dR_g$ for the differential of $R_g$ at the relevant point:
> $$\big(R_g^*D^\omega\alpha\big)(X_0,\dots,X_p)=(D^\omega\alpha)_{pg}\big(dR_gX_0,\dots,dR_gX_p\big)\qquad\text{(definition of the pullback }R_g^*\text{)}$$
> $$=d\alpha_{pg}\big(\pi_H\,dR_gX_0,\dots,\pi_H\,dR_gX_p\big)\qquad\text{(definition of }D^\omega\text{)}$$
> $$=d\alpha_{pg}\big(dR_g\,\pi_HX_0,\dots,dR_g\,\pi_HX_p\big)\qquad\text{(since }dR_g\circ\pi_H=\pi_H\circ dR_g\text{, the horizontal distribution being }G\text{-invariant: }dR_g(H_p)=H_{pg}\text{)}$$
> $$=\big(R_g^*(d\alpha)\big)\big(\pi_HX_0,\dots,\pi_HX_p\big)\qquad\text{(definition of the pullback }R_g^*(d\alpha)\text{)}$$
> $$=\big(d(R_g^*\alpha)\big)\big(\pi_HX_0,\dots,\pi_HX_p\big)\qquad\text{(since }R_g^*d=dR_g^*\text{, pullback commuting with }d\text{, applied componentwise to the }V\text{-valued form)}$$
> $$=\big(d(\rho(g^{-1})\alpha)\big)\big(\pi_HX_0,\dots,\pi_HX_p\big)\qquad\text{(equivariance of }\alpha\text{: }R_g^*\alpha=\rho(g^{-1})\alpha\text{)}$$
> $$=\rho(g^{-1})\,d\alpha\big(\pi_HX_0,\dots,\pi_HX_p\big)\qquad\text{(since }\rho(g^{-1})\in GL(V)\text{ is a constant linear map, it commutes with }d\text{, which acts componentwise)}$$
> $$=\rho(g^{-1})\,(D^\omega\alpha)(X_0,\dots,X_p)\qquad\text{(definition of }D^\omega\text{).}$$
> Therefore $R_g^*D^\omega\alpha=\rho(g^{-1})\,D^\omega\alpha$ for every $g$, which is equivariance of type $\rho$. Together with horizontality, $D^\omega\alpha$ is basic. $\blacksquare$

## Corollary 2 — Curvature is the exterior covariant derivative of the connection form

**Statement.** $\Omega=D^\omega\omega$, where $\Omega\in\Omega^2(P;\mathfrak g)$ is the [[Def - Curvature of a Principal Connection|curvature form]] of $\omega$.

> [!note]- Proof of Corollary 2
> This is a restatement of the definition of curvature. By [[Def - Curvature of a Principal Connection]], $\Omega(X,Y)=d\omega(\pi_HX,\pi_HY)$ for all $X,Y\in T_pP$. The right-hand side is exactly $(D^\omega\omega)(X,Y)$ by the definition of $D^\omega$ applied to the $\mathfrak g$-valued $1$-form $\alpha=\omega$ (with $V=\mathfrak g$). Hence $\Omega=D^\omega\omega$. $\blacksquare$
>
> The connection form $\omega$ is equivariant of type $\operatorname{Ad}$ (its axiom $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$), so Corollary 1 confirms that $\Omega=D^\omega\omega$ is basic and equivariant of type $\operatorname{Ad}$, consistent with its descent to $\Omega^2(M;\operatorname{ad}P)$.

## Corollary 3 — The tensorial formula

**Statement.** If $\alpha\in\Omega^p(P;V)$ is basic and equivariant of type $\rho$, then
$$D^\omega\alpha=d\alpha+\rho_*(\omega)\wedge\alpha.$$

> [!note]- Proof of Corollary 3
> **What is assumed and what must be shown.** We assume $\alpha$ is horizontal and $R_g^*\alpha=\rho(g^{-1})\alpha$. We must show the two $V$-valued $(p+1)$-forms $D^\omega\alpha$ and $d\alpha+\rho_*(\omega)\wedge\alpha$ are equal. Write $\Psi:=d\alpha+\rho_*(\omega)\wedge\alpha$ for the right-hand side. The strategy is: (Step 0) reduce equality of two horizontal forms to their values on horizontal tuples; (Step 1) $D^\omega\alpha$ is horizontal; (Step 2) $\Psi$ is horizontal — this is the substantial step and is where both hypotheses on $\alpha$ are used; (Step 3) the two agree on horizontal tuples.
>
> **Step 0 — a horizontal form is determined by its values on horizontal vectors.** Let $\beta$ be any horizontal $(p+1)$-form. For arbitrary $Y_0,\dots,Y_p$ write each $Y_i=\pi_HY_i+\pi_VY_i$ and expand $\beta(Y_0,\dots,Y_p)$ multilinearly; every resulting term containing at least one vertical entry $\pi_VY_i$ vanishes because $\beta$ is horizontal, leaving $\beta(Y_0,\dots,Y_p)=\beta(\pi_HY_0,\dots,\pi_HY_p)$. Hence two horizontal $(p+1)$-forms are equal if and only if they agree on all-horizontal tuples.
>
> **Step 1 — $D^\omega\alpha$ is horizontal.** Immediate from the definition: if any $X_i$ is vertical then $\pi_HX_i=0$ and $(D^\omega\alpha)(X_0,\dots,X_p)=d\alpha(\pi_HX_0,\dots,\pi_HX_p)=0$.
>
> **Step 2 — $\Psi=d\alpha+\rho_*(\omega)\wedge\alpha$ is horizontal.** Since vertical vectors at $p$ are exactly the values $\xi_P(p)$ of fundamental fields ($V_p=\{\xi_P(p):\xi\in\mathfrak g\}$, from [[Def - Equivariant and Basic Forms on a Principal Bundle]]) and $\Psi$ is an antisymmetric $(p+1)$-form, it suffices to show $\Psi(\xi_P,X_1,\dots,X_p)=0$ at $p$ for every $\xi\in\mathfrak g$ and arbitrary tangent vectors $X_1,\dots,X_p$; antisymmetry then gives vanishing whenever any argument is vertical. We extend the vertical vector to the fundamental field $\xi_P$ and the others to arbitrary vector fields $X_1,\dots,X_p$ (permissible, as a form is tensorial: its value at $p$ depends only on the vectors at $p$).
>
> *The $d\alpha$ term, via Cartan's formula.* By [[Thm - Cartan's Magic Formula|Cartan's magic formula]] $\mathcal L_{\xi_P}=d\,\iota_{\xi_P}+\iota_{\xi_P}\,d$ (applied componentwise to the $V$-valued form $\alpha$),
> $$\iota_{\xi_P}\,d\alpha=\mathcal L_{\xi_P}\alpha-d\big(\iota_{\xi_P}\alpha\big).$$
> Now $\iota_{\xi_P}\alpha=0$: for any $X_1,\dots,X_{p-1}$, $(\iota_{\xi_P}\alpha)(X_1,\dots,X_{p-1})=\alpha(\xi_P,X_1,\dots,X_{p-1})=0$ because $\alpha$ is horizontal and $\xi_P$ is vertical (hypothesis: $\alpha$ horizontal). Hence $d(\iota_{\xi_P}\alpha)=0$, and $\iota_{\xi_P}d\alpha=\mathcal L_{\xi_P}\alpha$. Next we evaluate the Lie derivative using the flow of $\xi_P$, which is $R_{\exp(t\xi)}$ (from [[Def - Fundamental Vector Field of a Group Action]]):
> $$\mathcal L_{\xi_P}\alpha=\frac{d}{dt}\Big|_{t=0}R_{\exp(t\xi)}^*\alpha=\frac{d}{dt}\Big|_{t=0}\rho\big(\exp(t\xi)^{-1}\big)\alpha\qquad\text{(equivariance: }R_g^*\alpha=\rho(g^{-1})\alpha\text{, with }g=\exp(t\xi)\text{)}$$
> $$=\frac{d}{dt}\Big|_{t=0}\exp\big(-t\,\rho_*(\xi)\big)\alpha=-\rho_*(\xi)\,\alpha\qquad\text{(since }\rho\circ\exp=\exp\circ\rho_*\text{, so }\rho(\exp(-t\xi))=\exp(-t\rho_*(\xi))\text{, differentiated at }t=0\text{).}$$
> Reading off the interior product, $d\alpha(\xi_P,X_1,\dots,X_p)=(\iota_{\xi_P}d\alpha)(X_1,\dots,X_p)=-\rho_*(\xi)\,\alpha(X_1,\dots,X_p)$.
>
> *The wedge term.* Using the wedge-action formula from Notation with $\eta=\omega$ and first argument $X_0=\xi_P$,
> $$\big(\rho_*(\omega)\wedge\alpha\big)(\xi_P,X_1,\dots,X_p)=\rho_*\big(\omega(\xi_P)\big)\,\alpha(X_1,\dots,X_p)+\sum_{i=1}^{p}(-1)^i\rho_*\big(\omega(X_i)\big)\,\alpha(\xi_P,X_1,\dots,\widehat{X_i},\dots,X_p).$$
> In the sum, each term contains the factor $\alpha(\xi_P,\dots)=0$ (again $\alpha$ horizontal, $\xi_P$ vertical), so the sum vanishes. In the first term $\omega(\xi_P)=\xi$ (connection axiom), giving $\rho_*(\xi)\,\alpha(X_1,\dots,X_p)$.
>
> *Combining.* Adding the two evaluations,
> $$\Psi(\xi_P,X_1,\dots,X_p)=-\rho_*(\xi)\,\alpha(X_1,\dots,X_p)+\rho_*(\xi)\,\alpha(X_1,\dots,X_p)=0.$$
> Thus $\Psi$ vanishes whenever an argument is vertical, i.e. $\Psi$ is horizontal.
>
> **Step 3 — agreement on horizontal tuples.** Let $X_0,\dots,X_p$ all be horizontal, so $\pi_HX_i=X_i$ and $\omega(X_i)=0$ (horizontal means $\ker\omega$). Then
> $$(D^\omega\alpha)(X_0,\dots,X_p)=d\alpha(\pi_HX_0,\dots,\pi_HX_p)=d\alpha(X_0,\dots,X_p),$$
> while
> $$\Psi(X_0,\dots,X_p)=d\alpha(X_0,\dots,X_p)+\sum_{i=0}^{p}(-1)^i\rho_*\big(\underbrace{\omega(X_i)}_{=0}\big)\,\alpha(\dots)=d\alpha(X_0,\dots,X_p).$$
> So $D^\omega\alpha$ and $\Psi$ agree on horizontal tuples.
>
> **Conclusion.** $D^\omega\alpha$ (Step 1) and $\Psi$ (Step 2) are both horizontal and agree on horizontal tuples (Step 3); by Step 0 they are equal. Therefore $D^\omega\alpha=d\alpha+\rho_*(\omega)\wedge\alpha$. $\blacksquare$

## Corollary 4 — The exterior covariant derivative of the curvature

**Statement.** $D^\omega\Omega=d\Omega+[\omega\wedge\Omega]$.

> [!note]- Proof of Corollary 4
> The curvature $\Omega$ is basic and equivariant of type $\operatorname{Ad}$ (Corollary 2), so we may apply the tensorial formula (Corollary 3) with $\rho=\operatorname{Ad}$, whose differential is $\rho_*=\operatorname{ad}$, i.e. $\operatorname{ad}(\xi)\eta=[\xi,\eta]$ (from [[Thm - Ad is a Smooth Representation and its Differential is ad]]). This gives
> $$D^\omega\Omega=d\Omega+\operatorname{ad}(\omega)\wedge\Omega\qquad\text{(tensorial formula, Corollary 3, }\rho=\operatorname{Ad}\text{).}$$
> It remains to identify $\operatorname{ad}(\omega)\wedge\Omega$ with the bracket $[\omega\wedge\Omega]$ of $\mathfrak g$-valued forms. We compute both sides on an arbitrary triple $(X,Y,Z)$ of tangent vectors and check they agree. On the one hand, the wedge-action formula from Notation with $\rho_*=\operatorname{ad}$, the $1$-form $\eta=\omega$, and the $2$-form $\alpha=\Omega$ (so $p=2$, arguments $(X_0,X_1,X_2)=(X,Y,Z)$) gives
> $$\big(\operatorname{ad}(\omega)\wedge\Omega\big)(X,Y,Z)=\operatorname{ad}\!\big(\omega(X)\big)\Omega(Y,Z)-\operatorname{ad}\!\big(\omega(Y)\big)\Omega(X,Z)+\operatorname{ad}\!\big(\omega(Z)\big)\Omega(X,Y)\qquad\text{(wedge-action formula, three terms }i=0,1,2\text{)}$$
> $$=\big[\omega(X),\Omega(Y,Z)\big]-\big[\omega(Y),\Omega(X,Z)\big]+\big[\omega(Z),\Omega(X,Y)\big]\qquad\text{(since }\operatorname{ad}(\xi)\eta=[\xi,\eta]\text{, from [[Thm - Ad is a Smooth Representation and its Differential is ad]]).}$$
> On the other hand, the bracket of a $\mathfrak g$-valued $1$-form with a $\mathfrak g$-valued $2$-form, by the shuffle convention of [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]], is
> $$[\omega\wedge\Omega](X,Y,Z)=\sum_{i=0}^{2}(-1)^i\big[\omega(X_i),\Omega(X_0,\dots,\widehat{X_i},\dots,X_2)\big]=\big[\omega(X),\Omega(Y,Z)\big]-\big[\omega(Y),\Omega(X,Z)\big]+\big[\omega(Z),\Omega(X,Y)\big].$$
> The two displayed expressions are identical term by term, so $\big(\operatorname{ad}(\omega)\wedge\Omega\big)(X,Y,Z)=[\omega\wedge\Omega](X,Y,Z)$ for every $(X,Y,Z)$. Hence $\operatorname{ad}(\omega)\wedge\Omega=[\omega\wedge\Omega]$, and $D^\omega\Omega=d\Omega+[\omega\wedge\Omega]$. $\blacksquare$
>
> This is a formula, not yet the Bianchi identity: the assertion that this quantity *vanishes*, $D^\omega\Omega=0$, is the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]], proved on its own page.

## Corollary 5 (non-example) — $D^\omega$ is not a differential

**Statement.** For $\alpha$ basic and equivariant of type $\rho$,
$$D^\omega\big(D^\omega\alpha\big)=\rho_*(\Omega)\wedge\alpha.$$
In particular $D^\omega\circ D^\omega\ne 0$ in general: unlike the de Rham $d$, the exterior covariant derivative does not square to zero, and its square is multiplication by the curvature $\rho_*(\Omega)$. It squares to zero exactly when $\rho_*(\Omega)$ acts as zero — for instance when $\omega$ is flat ($\Omega=0$) or when $\rho$ is the trivial representation ($\rho_*=0$).

> [!note]- Proof of Corollary 5
> Write $B:=\rho_*(\omega)\in\Omega^1(P;\operatorname{End}V)$, the $\operatorname{End}(V)$-valued $1$-form $B(X)=\rho_*(\omega(X))$; then the wedge-action $\rho_*(\omega)\wedge(\,\cdot\,)$ is the evaluation-wedge $B\wedge(\,\cdot\,)$ with the bilinear map $\operatorname{End}(V)\times V\to V$. By the tensorial formula (Corollary 3), for any basic equivariant $\alpha$ of type $\rho$,
> $$D^\omega\alpha=d\alpha+B\wedge\alpha.$$
> By Corollary 1, $D^\omega\alpha$ is again basic and equivariant of type $\rho$, so the tensorial formula applies to it as well:
> $$D^\omega(D^\omega\alpha)=d\big(D^\omega\alpha\big)+B\wedge\big(D^\omega\alpha\big)=d(d\alpha+B\wedge\alpha)+B\wedge(d\alpha+B\wedge\alpha).$$
> We expand the four resulting terms.
>
> **The $dd\alpha$ term.** $d(d\alpha)=0$ by [[Thm - d-Squared-is-Zero]] (applied componentwise to the $V$-valued form).
>
> **The $d(B\wedge\alpha)$ term.** The evaluation-wedge obeys the graded Leibniz rule $d(B\wedge\alpha)=dB\wedge\alpha+(-1)^{\deg B}B\wedge d\alpha=dB\wedge\alpha-B\wedge d\alpha$ (from [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]], graded Leibniz for the wedge-action; here $\deg B=1$). Moreover $dB=d(\rho_*\omega)=\rho_*(d\omega)$, since $\rho_*\in\operatorname{Hom}(\mathfrak g,\operatorname{End}V)$ is a fixed linear map and $d$ acts componentwise, so $d\circ\rho_*=\rho_*\circ d$. Hence $d(B\wedge\alpha)=\rho_*(d\omega)\wedge\alpha-B\wedge d\alpha$.
>
> **Combining.** Substituting,
> $$D^\omega(D^\omega\alpha)=\underbrace{dd\alpha}_{=0}+\big(\rho_*(d\omega)\wedge\alpha-B\wedge d\alpha\big)+B\wedge d\alpha+B\wedge(B\wedge\alpha)=\rho_*(d\omega)\wedge\alpha+B\wedge(B\wedge\alpha),$$
> the two $B\wedge d\alpha$ terms cancelling.
>
> **Identifying $B\wedge(B\wedge\alpha)$.** The evaluation-wedge is associative with the composition-wedge of $\operatorname{End}(V)$-valued forms — because the composite maps $\operatorname{End}(V)\times\operatorname{End}(V)\times V\to V$ agree ($T_1(T_2 v)=(T_1T_2)v$, associativity of matrix multiplication) — so $B\wedge(B\wedge\alpha)=(B\wedge B)\wedge\alpha$, where $(B\wedge B)$ is the $\operatorname{End}(V)$-valued $2$-form with $(B\wedge B)(X,Y)=B(X)B(Y)-B(Y)B(X)$. Now for each $X,Y$,
> $$(B\wedge B)(X,Y)=\rho_*(\omega(X))\,\rho_*(\omega(Y))-\rho_*(\omega(Y))\,\rho_*(\omega(X))=\rho_*\big([\omega(X),\omega(Y)]\big)\qquad\text{(}\rho_*\text{ is a Lie algebra homomorphism)}$$
> $$=\tfrac12\,\rho_*\big([\omega\wedge\omega](X,Y)\big)\qquad\text{(since }[\omega\wedge\omega](X,Y)=2[\omega(X),\omega(Y)]\text{).}$$
> Hence $B\wedge B=\rho_*\!\big(\tfrac12[\omega\wedge\omega]\big)$ and $B\wedge(B\wedge\alpha)=\rho_*\!\big(\tfrac12[\omega\wedge\omega]\big)\wedge\alpha$.
>
> **Conclusion.** Using the [[Thm - Structure Equation for the Curvature|structure equation]] $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$ and the linearity of $\rho_*$,
> $$D^\omega(D^\omega\alpha)=\rho_*(d\omega)\wedge\alpha+\rho_*\!\big(\tfrac12[\omega\wedge\omega]\big)\wedge\alpha=\rho_*\!\big(d\omega+\tfrac12[\omega\wedge\omega]\big)\wedge\alpha=\rho_*(\Omega)\wedge\alpha.$$
> Therefore $D^\omega\circ D^\omega=\rho_*(\Omega)\wedge(\,\cdot\,)$ on basic equivariant forms of type $\rho$, which vanishes identically if and only if $\rho_*(\Omega)$ acts as zero. $\blacksquare$

## Verified instance — the product connection on $M\times G$

Let $P=M\times G$ with $\pi=\operatorname{pr}_1$ the projection to $M$ and the right action $(m,h)\cdot g=(m,hg)$, carrying the **product connection** $\omega=\operatorname{pr}_2^*\theta$, where $\theta\in\Omega^1(G;\mathfrak g)$ is the [[Def - The Maurer-Cartan Form|Maurer–Cartan form]] and $\operatorname{pr}_2\colon M\times G\to G$ is the second projection. We claim that on this bundle $D^\omega$ acts as the ordinary de Rham $d$ once a basic form is read through the identity section — precisely, the induced exterior covariant derivative on the associated bundle is the trivial (flat) $d$.

We verify this clause by clause. First, $\omega=\operatorname{pr}_2^*\theta$ is a connection: this is checked on **Ex - The Product Connection on a Trivial Bundle and Pure Gauge Potentials**, and its horizontal distribution is $H_{(m,g)}=T_mM\times\{0\}$ (from [[Def - Horizontal Subspace and Horizontal Lift]]), so $\pi_H$ is projection onto the $M$-direction. Second, $\omega$ is flat: by the [[Thm - The Maurer-Cartan Equation|Maurer–Cartan equation]] $d\theta+\tfrac12[\theta\wedge\theta]=0$, pulling back by $\operatorname{pr}_2$ gives $d\omega+\tfrac12[\omega\wedge\omega]=\operatorname{pr}_2^*\!\big(d\theta+\tfrac12[\theta\wedge\theta]\big)=0$, so $\Omega=d\omega+\tfrac12[\omega\wedge\omega]=0$ by the structure equation. Third, take the identity section $s_0\colon M\to M\times G$, $m\mapsto(m,e)$. Its gauge potential is
$$A_{s_0}=s_0^*\omega=s_0^*\operatorname{pr}_2^*\theta=(\operatorname{pr}_2\circ s_0)^*\theta=(\text{constant map to }e)^*\theta=0,$$
since a constant map pulls every form back to zero. Now let $\alpha$ be basic and equivariant of type $\rho$, corresponding under the [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|basic-forms correspondence]] to $\alpha_0:=s_0^*\alpha\in\Omega^p(M;V)$. Pulling the tensorial formula back by $s_0$ and using $s_0^*\omega=A_{s_0}=0$,
$$s_0^*\big(D^\omega\alpha\big)=s_0^*\big(d\alpha+\rho_*(\omega)\wedge\alpha\big)=d(s_0^*\alpha)+\rho_*(s_0^*\omega)\wedge s_0^*\alpha=d\alpha_0+\rho_*(0)\wedge\alpha_0=d\alpha_0,$$
where $s_0^*d=ds_0^*$ is [[Thm - Pull-Back Commutes with the Exterior Derivative]]. Thus, read in the identity gauge, $D^\omega$ is exactly the de Rham $d$; equivalently, the induced connection on the associated bundle $M\times V$ is the flat product connection whose $d^\nabla$ is $d$. This is consistent with Corollary 5: $\Omega=0$ forces $D^\omega\circ D^\omega=\rho_*(\Omega)\wedge(\,\cdot\,)=0$, so on this bundle $D^\omega$ really is a differential.

## Calibration check

Two quick verifications the reader can carry out from the definition alone. **First, $D^\omega$ on functions is the horizontal part of $d$.** For $f\in\Omega^0(P;V)=C^\infty(P;V)$, the definition with $p=0$ gives $(D^\omega f)(X)=df(\pi_HX)$, so $D^\omega f=df\circ\pi_H$ is exactly the restriction of the differential $df$ to horizontal directions — the horizontal part of $df$. **Second, $D^\omega\pi^*\beta=\pi^*d\beta$ for $\beta\in\Omega^p(M;V)$.** The pulled-back form $\pi^*\beta$ is horizontal (it vanishes on vertical vectors, since $d\pi$ kills them) and $G$-invariant, hence basic of type the trivial representation ($\rho$ trivial, $\rho_*=0$). By the tensorial formula, $D^\omega\pi^*\beta=d(\pi^*\beta)+\rho_*(\omega)\wedge\pi^*\beta=d\pi^*\beta+0=\pi^*d\beta$, the last equality by [[Thm - Pull-Back Commutes with the Exterior Derivative]]. These two checks show that $D^\omega$ genuinely extends the de Rham derivative — it is $d$ along the horizontal distribution and reduces to $d$ on everything pulled up from the base — and that the whole novelty of the operator is concentrated in the curvature correction $\rho_*(\omega)\wedge(\,\cdot\,)$ that appears for non-trivial representations.

---

# Unlocked by This

> [!tip] The Bianchi identity *(from Gauge Theory IV)*
> The statement $D^\omega\Omega=0$ — equivalently $d\Omega=[\Omega\wedge\omega]$ on $P$ and $dF_\alpha+[A_\alpha\wedge F_\alpha]=0$ locally — is the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]], the single most-used consequence of this operator. Corollary 4, $D^\omega\Omega=d\Omega+[\omega\wedge\Omega]$, is its computational form; the vanishing is proved there.

> [!tip] Agreement with the covariant derivative on associated bundles *(from Gauge Theory IV)*
> Under the basic-forms correspondence $\Omega^\bullet(M;P\times_\rho V)\cong\Omega^\bullet_{\mathrm{bas}}(P;V)^G_\rho$, the operator $D^\omega$ corresponds to the exterior covariant derivative $d^{\nabla^\omega}$ of the induced connection on the associated bundle; this is [[Thm - Exterior Covariant Derivatives on P and on Associated Bundles Agree]]. Every identity on this page thereby transfers to the vector bundle downstairs, and conversely.

> [!tip] Chern–Weil theory *(from Gauge Theory VI)*
> The closedness of characteristic forms is a corollary of $D^\omega\Omega=0$: an invariant polynomial evaluated on the curvature is a closed form on $M$ because the exterior covariant derivative annihilates the curvature. The exterior covariant derivative is the operator that makes the **Chern–Weil homomorphism** land in de Rham cohomology.

> [!tip] The Yang–Mills equation *(from Gauge Theory VII)*
> The second-order field equation $d^{\nabla}\!\star F=0$ pairs the exterior covariant derivative with the Hodge star; together with the Bianchi identity $d^\nabla F=0$ it is the exact analogue of the source-free Maxwell equations, of which the abelian case is literally electrodynamics.
