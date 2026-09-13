---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Exterior Covariant Derivative on a Principal Bundle"
  - "Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space"
  - "Def - Exterior Covariant Derivative on a Vector Bundle"
  - "Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles"
  - "Thm - Sections of an Associated Bundle are Equivariant Functions"
  - "Def - Curvature of a Principal Connection"
  - "Thm - Pull-Back Commutes with the Exterior Derivative"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a principal $G$-bundle over a smooth manifold $M$, with a fixed **[[Def - Connection on a Principal Bundle|connection form]]** $\omega\in\Omega^1(P;\mathfrak g)$ (a $\mathfrak g$-valued $1$-form on the total space with $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$ and $\omega(\xi_P)=\xi$ for all $g\in G$, $\xi\in\mathfrak g$). Here $\mathfrak g=T_eG$ is the Lie algebra of $G$, $R_g(p)=p\cdot g$ is the right action, and $\xi_P(p)=\frac{d}{dt}\big|_{t=0}\,p\cdot\exp(t\xi)$ is the **[[Def - Fundamental Vector Field of a Group Action|fundamental vector field]]** of $\xi\in\mathfrak g$. At each $p\in P$ the tangent space splits $T_pP=H_p\oplus V_p$ into the horizontal subspace $H_p=\ker\omega_p$ and the vertical subspace $V_p=\ker d\pi_p=\{\xi_P(p):\xi\in\mathfrak g\}$; the **[[Def - Horizontal Subspace and Horizontal Lift|horizontal projection]]** $\pi_H\colon T_pP\to H_p$ is the projection onto $H_p$ along $V_p$.

We fix a representation $\rho\colon G\to GL(V)$ on a finite-dimensional real or complex vector space $V$, with differential the Lie-algebra representation $\rho_*:=d_e\rho\colon\mathfrak g\to\operatorname{End}(V)$ (a [[Def - Representation of a Lie Algebra|Lie-algebra homomorphism]], $\rho_*[\xi,\eta]=[\rho_*\xi,\rho_*\eta]$). The **[[Def - Associated Bundle|associated vector bundle]]** is $E:=P\times_\rho V=(P\times V)/G$, whose fibre over $m=\pi(p)$ carries the linear isomorphism
$$\ell_p\colon V\xrightarrow{\ \sim\ }E_{\pi(p)},\qquad \ell_p(v):=[p,v],\qquad \ell_{pg}=\ell_p\circ\rho(g).$$
We write $\nabla=\nabla^\omega$ for the **[[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|connection induced]]** on $E$ by $\omega$, and $\operatorname{ad}P:=P\times_{\operatorname{Ad}}\mathfrak g$ for the **[[Def - Adjoint Bundles ad P and Ad P|adjoint bundle]]** (the case $V=\mathfrak g$, $\rho=\operatorname{Ad}$, $\rho_*=\operatorname{ad}$).

For a fixed vector space $W$ we write $\Omega^q(N;W)=\Gamma(\Lambda^qT^*N)\otimes W$ for the $W$-valued $q$-forms on a manifold $N$, and for a vector bundle $F\to M$ we write $\Omega^q(M;F)=\Gamma(\Lambda^qT^*M\otimes F)$ for the $F$-valued $q$-forms. A $V$-valued form $\phi\in\Omega^q(P;V)$ is **equivariant of type $\rho$** if $R_g^*\phi=\rho(g^{-1})\phi$ for all $g$, and **basic** if $\phi(X_1,\dots,X_q)=0$ whenever one $X_i$ is vertical; the space of basic equivariant forms is $\Omega^q_{\mathrm{bas}}(P;V)^G$. The **exterior covariant derivatives** in play are

- $D^\omega\colon\Omega^q(P;V)\to\Omega^{q+1}(P;V)$, $D^\omega\phi:=(d\phi)\circ\pi_H$, i.e. $(D^\omega\phi)(X_0,\dots,X_q)=d\phi(\pi_HX_0,\dots,\pi_HX_q)$, the **[[Def - Exterior Covariant Derivative on a Principal Bundle|exterior covariant derivative on the total space]]**; and
- $d^\nabla\colon\Omega^q(M;E)\to\Omega^{q+1}(M;E)$, the **[[Def - Exterior Covariant Derivative on a Vector Bundle|exterior covariant derivative]]** of the vector-bundle connection $\nabla=\nabla^\omega$, determined by $d^\nabla|_{\Omega^0}=\nabla$ and the graded Leibniz rule $d^\nabla(\eta\wedge\alpha)=d\eta\wedge\alpha+(-1)^q\eta\wedge d^\nabla\alpha$ for $\eta\in\Omega^q(M)$, $\alpha\in\Omega^\bullet(M;E)$.

For a $\mathfrak g$-valued $1$-form $\beta$ and a $V$-valued $q$-form $\phi$ on the same manifold, $\rho_*(\beta)\wedge\phi$ is the $V$-valued $(q+1)$-form obtained by applying the linear map $\rho_*$ to the values of $\beta$ and then wedging through the action $\operatorname{End}(V)\otimes V\to V$; explicitly
$$(\rho_*(\beta)\wedge\phi)(X_0,\dots,X_q)=\sum_{i=0}^{q}(-1)^i\,\rho_*\!\big(\beta(X_i)\big)\,\phi(X_0,\dots,\widehat{X_i},\dots,X_q),$$
with the standard convention (from [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]]); for a $0$-form $\phi=v$ this is just $\rho_*(\beta)\,v$, and for $\rho=\operatorname{Ad}$ one has $\operatorname{ad}(\beta)\wedge\phi=[\beta\wedge\phi]$.

> [!warning] Convention: Haydys' notation
> Haydys (§2.2) writes $a$ for the connection form (our $\omega$), $a\cdot\hat s$ for our $\rho_*(\omega)\,\hat s$, $K_\xi$ for our $\xi_P$, and $d^{\nabla_a}$ for the exterior covariant derivative of the induced connection $\nabla_a$ on $\operatorname{ad}P$ (our $d^{\nabla_\omega}$); he also says "$G$-invariant" where we say "equivariant of type $\rho$". Equation (47) of Haydys, $\pi^*\nabla s=d\hat s+a\cdot\hat s$, is in our notation $\pi^*(\nabla s)=d\hat s+\rho_*(\omega)\,\hat s$, and Proposition 53's operator $d^{\nabla_a}$ is our $D^\omega$ read on $\operatorname{ad}P$-valued forms. The two sign-free descriptions of the same operator are the subject of this page.

---

# Statement

> **Theorem (the two exterior covariant derivatives agree).** Let $\pi\colon P\to M$ be a principal $G$-bundle with connection form $\omega\in\Omega^1(P;\mathfrak g)$, let $\rho\colon G\to GL(V)$ be a representation with differential $\rho_*\colon\mathfrak g\to\operatorname{End}(V)$, let $E=P\times_\rho V$ be the associated vector bundle, and let $\nabla=\nabla^\omega$ be the connection induced on $E$ by $\omega$. Let
> $$\Phi\colon \Omega^q(M;E)\xrightarrow{\ \sim\ }\Omega^q_{\mathrm{bas}}(P;V)^G,\qquad \Phi(\alpha)=\hat\alpha,\quad \hat\alpha_p(\hat v_1,\dots,\hat v_q)=\ell_p^{-1}\!\big(\alpha_{\pi(p)}(d\pi\,\hat v_1,\dots,d\pi\,\hat v_q)\big),$$
> be the [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|basic-forms correspondence]]. Then, for every $q\ge 0$, the diagram
> $$
> \begin{array}{ccc}
> \Omega^q(M;E) & \xrightarrow{\ d^\nabla\ } & \Omega^{q+1}(M;E)\\[2pt]
> {\scriptstyle\Phi}\big\downarrow{\scriptstyle\wr} & & {\scriptstyle\wr}\big\downarrow{\scriptstyle\Phi}\\[2pt]
> \Omega^q_{\mathrm{bas}}(P;V)^G & \xrightarrow{\ D^\omega\ } & \Omega^{q+1}_{\mathrm{bas}}(P;V)^G
> \end{array}
> $$
> commutes; that is,
> $$\Phi(d^\nabla\alpha)=D^\omega(\Phi\alpha),\qquad\text{equivalently}\qquad \widehat{d^\nabla\alpha}=D^\omega\hat\alpha,\qquad\text{for all }\alpha\in\Omega^q(M;E).$$

> **Corollary (local formula).** In any local gauge $s\colon U\to P$ with gauge potential $A:=s^*\omega\in\Omega^1(U;\mathfrak g)$ and induced trivialisation $E|_U\cong U\times V$, $[s(m),v]\leftrightarrow(m,v)$, the exterior covariant derivative is
> $$d^\nabla=d+\rho_*(A)\wedge\qquad\text{on }\Omega^\bullet(U;V);$$
> that is, if $\alpha=[s,\phi]$ with $\phi\in\Omega^q(U;V)$ then $d^\nabla\alpha=[s,\,d\phi+\rho_*(A)\wedge\phi]$.

> **Corollary (Bianchi in two guises).** Taking $\rho=\operatorname{Ad}$, $V=\mathfrak g$, $E=\operatorname{ad}P$: the base curvature $F_\omega\in\Omega^2(M;\operatorname{ad}P)$ corresponds under $\Phi$ to the total-space curvature $\Omega\in\Omega^2(P;\mathfrak g)$, and consequently
> $$\Phi\big(d^{\nabla_\omega}F_\omega\big)=D^\omega\Omega,\qquad\text{locally}\qquad d^{\nabla_\omega}F_\omega=dF_A+[A\wedge F_A].$$
> Hence the identity $D^\omega\Omega=0$ on $P$ and the identity $d^{\nabla_\omega}F_\omega=0$ (equivalently $dF_A+[A\wedge F_A]=0$) on $M$ are the same statement read on the two sides of $\Phi$. (Their common truth is the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]], proved on its own page; this theorem supplies only the translation.)

---

# Motivation

A connection can be described in two languages that look nothing alike. Downstairs on the base $M$ it appears as a covariant derivative $\nabla$ on the associated vector bundle $E=P\times_\rho V$, extended to $E$-valued forms as the exterior covariant derivative $d^\nabla$ by the Leibniz rule — this is the language of chapter II, the language a physicist uses when writing $D_\mu\phi=\partial_\mu\phi+\rho_*(A_\mu)\phi$ for a matter field. Upstairs on the total space $P$ the same connection appears as a $\mathfrak g$-valued form $\omega$, and the natural differentiation of equivariant tensorial forms is $D^\omega=(d\,\cdot)\circ\pi_H$, "differentiate and keep the horizontal part" — this is the language in which the curvature is $\Omega=D^\omega\omega$ and the Bianchi identity is the transparent $D^\omega\Omega=0$. The two descriptions are joined by one dictionary, the basic-forms correspondence $\Phi$, which turns an $E$-valued $q$-form on $M$ into a basic equivariant $V$-valued $q$-form on $P$. The question this page answers is whether $\Phi$ is compatible with differentiation: does the ordinary-looking $d^\nabla$ downstairs correspond, under $\Phi$, to the horizontal-projection operator $D^\omega$ upstairs?

The answer is yes, and its importance is that it lets every computation be done on whichever side is easier and then transported for free to the other. The clearest instance is the Bianchi identity. On $P$ it has a one-line conceptual proof: $D^\omega\Omega$ is $d\Omega$ evaluated on horizontal vectors, and a short bracket computation shows this vanishes. On $M$ the same identity reads $dF_A+[A\wedge F_A]=0$, an inhomogeneous-looking coordinate identity for the field strength; proving it directly downstairs is a graded-bracket calculation with a Jacobi step. This theorem says the two are literally the same statement pushed through $\Phi$, so the clean proof upstairs *is* a proof of the messy identity downstairs. The same mechanism will let Chern–Weil forms, built upstairs from $\Omega$, be recognised as closed forms downstairs, and will identify the curvature $F_{\nabla^\omega}$ of the induced connection with $\rho_*(F_\omega)$. In short, the theorem is the reason the principal-bundle and vector-bundle formalisms never diverge: they are two coordinate systems on one operator.

---

# Sources and Targets

**Sources (Input Broadening).** The hypothesis of the theorem is mild — a principal connection $\omega$ and a representation $\rho$ — so the skill is to recognise when a problem secretly supplies them.

The first disguised source is **a bare covariant derivative $\nabla$ on a vector bundle $E\to M$, with no principal bundle named.** Every rank-$k$ vector bundle is the associated bundle $E\cong\operatorname{Fr}(E)\times_{\mathrm{std}}\mathbb R^k$ of its frame bundle for the standard representation of $GL_k$ (this is [[Thm - Vector Bundles are Associated to Their Frame Bundles|the frame-bundle identification]]), and by [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle|the previous theorem]] the connection $\nabla$ is $e^*\omega=A(\nabla,e)$ for a unique principal connection $\omega$ on $\operatorname{Fr}(E)$. So a problem that only mentions $\nabla$ already meets the hypothesis with $P=\operatorname{Fr}(E)$ and $\rho$ the standard representation; the bridge is that the frame bundle is always available even when unmentioned. *Example problem:* show that the covariant exterior derivative of the Riemann curvature tensor, viewed as an $\operatorname{End}(TM)$-valued $2$-form, is computed by $D^\omega$ on the orthonormal frame bundle and thereby satisfies the second Bianchi identity.

The second disguised source is **a single principal connection together with the whole tower of representations of $G$.** One $\omega$ is simultaneously a connection on every associated bundle $E=P\times_\rho V$, $E^*=P\times_{\rho^*}V^*$, $\operatorname{End}E=P\times_{\rho\otimes\rho^*}\operatorname{End}V$, $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$, and every tensor and symmetric power. The non-obvious bridge is that all of these covariant derivatives are the *same* operator $D^\omega$ upstairs, merely read through different representations; a fact proved once on $P$ therefore holds on all associated bundles at once. *Example problem:* deduce that the induced covariant derivative is compatible with every $G$-equivariant tensor operation (contraction, pairing $E^*\otimes E\to\underline{\mathbb R}$) in one stroke, because such operations are $\rho$-morphisms and $D^\omega$ is representation-independent.

The third disguised source is **a gauge potential $A\in\Omega^1(U;\mathfrak g)$ handed over in coordinates, with no global bundle in sight** — the physicist's starting datum. Such an $A$ is the local form $s^*\omega$ of a connection for the section $s$ (by [[Thm - Transformation of Local Connection and Curvature Forms|the reconstruction of a connection from its local forms]]), so the local-formula corollary $d^\nabla=d+\rho_*(A)\wedge$ applies and computes covariant exterior derivatives of matter fields and of the field strength directly from $A$. The bridge is that a locally given potential always determines a local connection, and the theorem's local formula is then exactly the covariant derivative one wants. *Example problem:* compute the covariant divergence of an $SU(2)$ field strength $F$ from a coordinate potential $A_\mu$ and identify the Yang–Mills equation's Bianchi companion.

**Targets (Output Amplification).**

Combine the theorem with **the horizontal Bianchi identity $D^\omega\Omega=0$** proved on $P$. Because $F_\omega\leftrightarrow\Omega$ under $\Phi$, the theorem transports $D^\omega\Omega=0$ into $d^{\nabla_\omega}F_\omega=0$, that is $dF_A+[A\wedge F_A]=0$ locally. The extra ingredient is the one-line horizontal computation upstairs; the payoff is the field-strength Bianchi identity downstairs, obtained without any graded-bracket bookkeeping on the base. This is exactly how [[Thm - Bianchi Identity for a Principal Connection|the Bianchi identity page]] delivers its local form.

Combine the theorem with **the curvature-squared identity $d^\nabla\circ d^\nabla=F_\nabla\wedge(\,\cdot\,)$** for vector-bundle connections (from [[Thm - Existence of the Curvature Form|the existence of the curvature form]]) and the parallel identity $D^\omega\circ D^\omega=\rho_*(\Omega)\wedge(\,\cdot\,)$ upstairs. Since $\Phi$ intertwines $d^\nabla$ with $D^\omega$, it intertwines their squares, and the two curvature operators match: $F_{\nabla^\omega}=\rho_*(F_\omega)$ in $\Omega^2(M;\operatorname{End}E)$. The extra ingredient is the curvature-squared identity on each side; the payoff is the identification of the induced connection's curvature (Haydys' Proposition 52).

Combine the theorem with **an $\operatorname{Ad}$-invariant polynomial $f$ on $\mathfrak g$** (Chern–Weil theory, chapter VI). The characteristic form $f(\Omega)$ is built upstairs and is basic, hence descends to $f(F_\omega)$ on $M$; the theorem's compatibility of $D^\omega$ with $\Phi$ turns the horizontal identity $D^\omega\Omega=0$ into $df(F_\omega)=0$, the closedness of the characteristic form. The extra ingredient is invariance of $f$; the payoff is that characteristic classes are well defined in de Rham cohomology.

---

# Why Is It True

Two operators are equal when they are built by the same recipe from the same seed. Here the seed is the connection — read as $\nabla$ downstairs and as $\omega$ upstairs — and the recipe on both sides is: "act by the connection on degree zero, then extend to all degrees by the graded Leibniz rule over scalar forms." Downstairs, $d^\nabla$ is *defined* this way: it is $\nabla$ on sections and satisfies $d^\nabla(\eta\wedge\alpha)=d\eta\wedge\alpha+(-1)^{|\eta|}\eta\wedge d^\nabla\alpha$ for scalar forms $\eta$ on $M$. Upstairs, the same is true of $D^\omega$ once one notes two facts: on functions it is $\nabla$ read through the correspondence (this is exactly Haydys' equation (47)), and it satisfies the graded Leibniz rule against forms $\pi^*\eta$ pulled up from $M$. The dictionary $\Phi$ carries scalar forms $\eta$ on $M$ to their pullbacks $\pi^*\eta$ on $P$ and respects wedging, so it carries the downstairs recipe to the upstairs recipe verbatim. Two operators that agree on the generators (sections, and scalar forms) and obey the same product rule must agree everywhere they are defined.

**In one sentence: $d^\nabla$ and $D^\omega$ are both the unique extension of the connection to forms by the graded Leibniz rule over scalar forms, and $\Phi$ is an isomorphism of the two module-with-connection structures, so it intertwines the two extensions.**

The only place where the identity is not pure formalism is the base case in degree zero. There it says: the covariant derivative $\nabla s$ of a section, read upstairs, equals the horizontal part of the ordinary derivative of the equivariant lift $\hat s$ corrected by the connection. Concretely $D^\omega\hat s=d\hat s+\rho_*(\omega)\hat s$, and this equals $\widehat{\nabla s}$ precisely because the induced connection was *defined* by (47) to make it so. Once degree zero is pinned down by (47), every higher degree is forced by the Leibniz rule, and the theorem is the statement that nothing goes wrong in the forcing.

---

# What Makes This Hard

The difficulty is conceptual, not computational. The two operators are given by descriptions that share no symbols: $D^\omega$ is "apply $d$ then project onto horizontal directions", a projection with no visible connection term, while $d^\nabla$ is "extend $\nabla$ by an algebraic Leibniz rule", with the connection term explicit. The bridge is the tensorial formula $D^\omega\alpha=d\alpha+\rho_*(\omega)\wedge\alpha$ for basic equivariant $\alpha$, which rewrites the projection as a corrected exterior derivative; without it, the two sides cannot even be compared term by term. The second trap is the module structure: $\Phi$ does *not* intertwine $d^\nabla$ with $D^\omega$ by carrying a scalar form $\eta$ to itself — it carries $\eta$ to its pullback $\pi^*\eta$, and one must check that $\Phi(\eta\wedge\alpha)=\pi^*\eta\wedge\hat\alpha$ and that $D^\omega$ is a graded derivation over pulled-back forms with the *same* signs as $d^\nabla$ over $\eta$. The common error is to verify the base case (which is just (47)) and declare victory, forgetting that the Leibniz-rule compatibility of $\Phi$ and of $D^\omega$ against $\pi^*\eta$ is what actually propagates the base case to all degrees.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show that $\Phi$ intertwines the two module structures (it sends $\eta\wedge\alpha$ to $\pi^*\eta\wedge\hat\alpha$), that $D^\omega$ is a graded derivation over pulled-back forms with the same signs as $d^\nabla$ over base forms, and that the two operators agree in degree zero (this is (47)). Then every $E$-valued form is locally a sum $\sum\eta^a\wedge s_a$ of scalar forms wedged with frame sections, and a single Leibniz computation, using the three facts, verifies the identity on each such term; locality of the operators extends it globally.

**Subgoal decomposition:**

1. **Module compatibility of $\Phi$.** Prove $\Phi(\eta\wedge\alpha)=\pi^*\eta\wedge\Phi(\alpha)$ for $\eta\in\Omega^k(M)$, $\alpha\in\Omega^q(M;E)$.
   - *Hint:* Use $\hat\alpha_p=\ell_p^{-1}\circ(\pi^*\alpha)_p$ and that $\pi^*$ respects wedge products, and that the linear map $\ell_p^{-1}$ passes through wedging by a scalar form.
   - *Why needed:* It is what turns "$d^\nabla$ is a derivation over $\Omega^\bullet(M)$" into "$D^\omega$ is a derivation over $\pi^*\Omega^\bullet(M)$" under $\Phi$.

2. **$D^\omega$ is a derivation over pulled-back forms.** Prove $D^\omega(\pi^*\eta\wedge\phi)=\pi^*(d\eta)\wedge\phi+(-1)^k\pi^*\eta\wedge D^\omega\phi$ for $\eta\in\Omega^k(M)$, $\phi\in\Omega^q_{\mathrm{bas}}(P;V)^G$.
   - *Hint:* Apply the tensorial formula $D^\omega=d+\rho_*(\omega)\wedge$ on basic equivariant forms, use $d\pi^*\eta=\pi^*d\eta$, and move the scalar $k$-form $\pi^*\eta$ past the $1$-form $\rho_*(\omega)$ with the Koszul sign $(-1)^k$.
   - *Why needed:* It is the upstairs Leibniz rule, matched sign-for-sign to the downstairs one.

3. **Degree-zero base case.** Prove $\Phi(d^\nabla s)=D^\omega(\Phi s)$ for $s\in\Gamma(E)$.
   - *Hint:* $d^\nabla s=\nabla s$ and $\Phi(\nabla s)=d\hat s+\rho_*(\omega)\hat s$ by (47); $D^\omega\hat s=d\hat s+\rho_*(\omega)\hat s$ by the tensorial formula (verify it directly on horizontal and vertical vectors).
   - *Why needed:* This is the only non-formal input; everything else propagates it.

4. **Locality and local generation.** Prove that $d^\nabla$ (hence $\Phi\circ d^\nabla$) and $D^\omega\circ\Phi$ are local operators, and that every $\alpha\in\Omega^q(M;E)$ is, over the domain of a local frame, a finite sum $\sum_a\eta^a\wedge s_a$ with $\eta^a\in\Omega^q(U)$ and $s_a\in\Gamma(E|_U)$.
   - *Hint:* A connection is local by a bump-function argument; a local frame of $E$ over a trivialising set gives the decomposition.
   - *Why needed:* It reduces the global identity to the single-term identity handled by subgoals 1–3.

---

# Lemma Decomposition

> [!note]- Lemma 1: The correspondence $\Phi$ is a morphism of $\Omega^\bullet(M)$-modules
> **Statement:** For $\eta\in\Omega^k(M)$ and $\alpha\in\Omega^q(M;E)$,
> $$\Phi(\eta\wedge\alpha)=\pi^*\eta\wedge\Phi(\alpha),\qquad\text{i.e.}\qquad \widehat{\eta\wedge\alpha}=\pi^*\eta\wedge\hat\alpha.$$
>
> **Hint:** Write $\hat\alpha_p=\ell_p^{-1}\circ(\pi^*\alpha)_p$, use that pullback of scalar-times-bundle forms respects the wedge, and that a fixed linear map commutes with wedging by a scalar form.
>
> **Why needed:** It is the module-compatibility that lets the graded Leibniz rule for $d^\nabla$ over $\Omega^\bullet(M)$ translate into the graded Leibniz rule for $D^\omega$ over $\pi^*\Omega^\bullet(M)$ once $\Phi$ is applied.
>
> > [!note]- Full proof
> > We use the defining characterisation of $\Phi$ from the [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|basic-forms theorem]]: for $\beta\in\Omega^r(M;E)$, its lift $\hat\beta\in\Omega^r_{\mathrm{bas}}(P;V)^G$ is the unique basic equivariant form with
> > $$\ell_p\big(\hat\beta_p(\hat v_1,\dots,\hat v_r)\big)=\beta_{\pi(p)}(d\pi\,\hat v_1,\dots,d\pi\,\hat v_r)\qquad\text{for all }p\in P,\ \hat v_i\in T_pP,$$
> > equivalently $\hat\beta_p=\ell_p^{-1}\circ(\pi^*\beta)_p$, where $\pi^*\beta\in\Omega^r(P;\pi^*E)$ is the ordinary pullback and $(\pi^*\beta)_p(\hat v_\bullet)=\beta_{\pi(p)}(d\pi\,\hat v_\bullet)\in E_{\pi(p)}$. Uniqueness holds because $\ell_p\colon V\to E_{\pi(p)}$ is a linear isomorphism, so $\hat\beta_p$ is determined pointwise.
> >
> > **Pullback respects the wedge.** The exterior pullback is multiplicative, by [[Thm - Pull-Back Commutes with the Exterior Derivative|the pullback theorem]] (which covers $W$-valued forms for a fixed vector space $W$ as well as scalar forms): for the scalar form $\eta$ and the $E$-valued form $\alpha$,
> > $$\pi^*(\eta\wedge\alpha)=\pi^*\eta\wedge\pi^*\alpha\qquad\text{(multiplicativity of the pullback).}$$
> > Here $\pi^*\eta\in\Omega^k(P)$ is scalar and $\pi^*\alpha\in\Omega^q(P;\pi^*E)$ is $E$-valued, and the wedge is the scalar-times-bundle wedge, taken pointwise in $E_{\pi(p)}$.
> >
> > **A fixed linear map passes through a scalar wedge.** Fix $p$. For any scalar $k$-form $\mu$ and any $E_{\pi(p)}$-valued $q$-covector $\gamma$ on $T_pP$, and any linear map $L\colon E_{\pi(p)}\to V$, the definition of the scalar-times-vector wedge gives, for $\hat v_0,\dots,\hat v_{k+q-1}\in T_pP$,
> > $$L\big((\mu\wedge\gamma)(\hat v_0,\dots)\big)=L\!\left(\tfrac{1}{k!\,q!}\sum_{\sigma}\operatorname{sgn}(\sigma)\,\mu(\hat v_{\sigma(0)},\dots)\,\gamma(\hat v_{\sigma(k)},\dots)\right)=\tfrac{1}{k!\,q!}\sum_{\sigma}\operatorname{sgn}(\sigma)\,\mu(\hat v_{\sigma(0)},\dots)\,L\big(\gamma(\hat v_{\sigma(k)},\dots)\big),$$
> > the last equality because $L$ is linear and $\mu(\hat v_{\sigma(0)},\dots)$ is a scalar. Thus $L\big(\mu\wedge\gamma\big)=\mu\wedge(L\circ\gamma)$. Applying this with $L=\ell_p^{-1}$, $\mu=(\pi^*\eta)_p$, $\gamma=(\pi^*\alpha)_p$:
> > $$\ell_p^{-1}\big((\pi^*\eta\wedge\pi^*\alpha)_p\big)=(\pi^*\eta)_p\wedge\ell_p^{-1}\big((\pi^*\alpha)_p\big)=(\pi^*\eta)_p\wedge\hat\alpha_p=(\pi^*\eta\wedge\hat\alpha)_p.$$
> >
> > **Combine.** Using $\widehat{\eta\wedge\alpha}_p=\ell_p^{-1}\circ(\pi^*(\eta\wedge\alpha))_p$ and the two displays,
> > $$\widehat{\eta\wedge\alpha}_p=\ell_p^{-1}\big((\pi^*\eta\wedge\pi^*\alpha)_p\big)=(\pi^*\eta\wedge\hat\alpha)_p\qquad\text{(multiplicativity of }\pi^*\text{, then the scalar-wedge identity).}$$
> > Since this holds at every $p$, $\widehat{\eta\wedge\alpha}=\pi^*\eta\wedge\hat\alpha$. Finally $\pi^*\eta\wedge\hat\alpha$ is indeed basic (a wedge with the basic form $\pi^*\eta$, which vanishes on vertical vectors since $d\pi$ does) and equivariant of type $\rho$ (as $R_g^*\pi^*\eta=\pi^*\eta$ because $\pi\circ R_g=\pi$, and $R_g^*\hat\alpha=\rho(g^{-1})\hat\alpha$, the scalar factor commuting with $\rho(g^{-1})$), so it lies in $\Omega^{k+q}_{\mathrm{bas}}(P;V)^G$ and the equality is an equality there. $\blacksquare$

> [!note]- Lemma 2: $D^\omega$ is a graded derivation over pulled-back forms
> **Statement:** For $\eta\in\Omega^k(M)$ and $\phi\in\Omega^q_{\mathrm{bas}}(P;V)^G$,
> $$D^\omega(\pi^*\eta\wedge\phi)=\pi^*(d\eta)\wedge\phi+(-1)^k\,\pi^*\eta\wedge D^\omega\phi.$$
>
> **Hint:** Apply the tensorial formula $D^\omega=d+\rho_*(\omega)\wedge$ valid on basic equivariant forms; use $d\pi^*\eta=\pi^*d\eta$ and move $\pi^*\eta$ past the $1$-form $\rho_*(\omega)$ with the Koszul sign.
>
> **Why needed:** It is the upstairs Leibniz rule, matched sign-for-sign to the downstairs Leibniz rule for $d^\nabla$; it is what carries the base case up through the degrees.
>
> > [!note]- Full proof
> > First, $\pi^*\eta\wedge\phi\in\Omega^{k+q}_{\mathrm{bas}}(P;V)^G$: it is basic because $\pi^*\eta$ is (it vanishes on vertical vectors, $d\pi$ killing them), and equivariant of type $\rho$ because $R_g^*(\pi^*\eta\wedge\phi)=\pi^*\eta\wedge\rho(g^{-1})\phi=\rho(g^{-1})(\pi^*\eta\wedge\phi)$, the scalar $\pi^*\eta$ commuting with $\rho(g^{-1})$. So the **tensorial formula** for the exterior covariant derivative of a basic equivariant form (proved on [[Def - Exterior Covariant Derivative on a Principal Bundle|the definition page]] as its Corollary "$D^\omega\alpha=d\alpha+\rho_*(\omega)\wedge\alpha$ for basic equivariant $\alpha$") applies both to $\phi$ and to $\pi^*\eta\wedge\phi$:
> > $$D^\omega(\pi^*\eta\wedge\phi)=d(\pi^*\eta\wedge\phi)+\rho_*(\omega)\wedge(\pi^*\eta\wedge\phi)\qquad\text{(tensorial formula applied to }\pi^*\eta\wedge\phi\text{).}$$
> >
> > **First term — ordinary Leibniz for $d$.** Since $\pi^*\eta$ is a scalar $k$-form and $\phi$ is $V$-valued,
> > $$d(\pi^*\eta\wedge\phi)=d(\pi^*\eta)\wedge\phi+(-1)^k\,\pi^*\eta\wedge d\phi\qquad\text{(graded Leibniz rule for the exterior derivative on }V\text{-valued forms)}$$
> > $$=\pi^*(d\eta)\wedge\phi+(-1)^k\,\pi^*\eta\wedge d\phi\qquad\text{(since }d\pi^*\eta=\pi^*d\eta\text{, pullback commuting with }d\text{).}$$
> >
> > The identity $d\pi^*\eta=\pi^*d\eta$ used here is [[Thm - Pull-Back Commutes with the Exterior Derivative|the pullback theorem]].
> >
> > **Second term — move the scalar form past $\rho_*(\omega)$.** The form $\rho_*(\omega)$ is $\operatorname{End}(V)$-valued of degree $1$ and $\pi^*\eta$ is scalar of degree $k$; a scalar form commutes with any vector- or endomorphism-valued form up to the Koszul sign, so
> > $$\rho_*(\omega)\wedge\pi^*\eta\wedge\phi=(-1)^{1\cdot k}\,\pi^*\eta\wedge\rho_*(\omega)\wedge\phi=(-1)^k\,\pi^*\eta\wedge\big(\rho_*(\omega)\wedge\phi\big)\qquad\text{(graded commutativity of the scalar factor }\pi^*\eta\text{).}$$
> >
> > **Combine.** Adding the two contributions,
> > $$D^\omega(\pi^*\eta\wedge\phi)=\pi^*(d\eta)\wedge\phi+(-1)^k\,\pi^*\eta\wedge d\phi+(-1)^k\,\pi^*\eta\wedge\big(\rho_*(\omega)\wedge\phi\big)$$
> > $$=\pi^*(d\eta)\wedge\phi+(-1)^k\,\pi^*\eta\wedge\big(d\phi+\rho_*(\omega)\wedge\phi\big)\qquad\text{(factoring the common }(-1)^k\pi^*\eta\wedge\text{)}$$
> > $$=\pi^*(d\eta)\wedge\phi+(-1)^k\,\pi^*\eta\wedge D^\omega\phi\qquad\text{(tensorial formula applied to }\phi\text{).}$$
> > This is the claimed rule. $\blacksquare$

> [!note]- Lemma 3: The operators agree in degree zero
> **Statement:** For every section $s\in\Gamma(E)=\Omega^0(M;E)$, with equivariant lift $\hat s=\Phi(s)\in C^\infty(P;V)^G$,
> $$\Phi(d^\nabla s)=D^\omega(\Phi s),\qquad\text{both equal to}\qquad d\hat s+\rho_*(\omega)\,\hat s.$$
>
> **Hint:** $d^\nabla s=\nabla s$; use (47) for the left side and the tensorial formula (verified directly on horizontal and vertical vectors) for the right.
>
> **Why needed:** This is the sole non-formal input of the theorem; the higher degrees are forced from it by Lemmas 1 and 2.
>
> > [!note]- Full proof
> > By the $q=0$ case of the basic-forms correspondence, $\Phi(s)=\hat s$ is the equivariant function attached to the section $s$ by [[Thm - Sections of an Associated Bundle are Equivariant Functions|the sections-as-equivariant-functions theorem]]: it is the unique $\hat s\in C^\infty(P;V)$ with $s(\pi(p))=[p,\hat s(p)]=\ell_p(\hat s(p))$, and it satisfies $\hat s(p\cdot g)=\rho(g^{-1})\hat s(p)$.
> >
> > **Left side.** In degree zero the vector-bundle exterior covariant derivative is the connection itself, $d^\nabla s=\nabla s$ (a defining property from [[Def - Exterior Covariant Derivative on a Vector Bundle]], $d^\nabla|_{\Omega^0}=\nabla$). The defining property (Haydys' equation (47)) of the [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|induced connection]] $\nabla=\nabla^\omega$ is precisely that $\pi^*(\nabla s)$ corresponds under $\Phi$ to $d\hat s+\rho_*(\omega)\hat s$, i.e.
> > $$\Phi(d^\nabla s)=\Phi(\nabla s)=\widehat{\nabla s}=d\hat s+\rho_*(\omega)\,\hat s\qquad\text{(by (47), the defining equation of }\nabla^\omega\text{).}$$
> >
> > **Right side.** We show directly that $D^\omega\hat s=d\hat s+\rho_*(\omega)\hat s$ (this is the $q=0$ case of the tensorial formula). By definition $D^\omega\hat s=(d\hat s)\circ\pi_H$, so both sides are $V$-valued $1$-forms on $P$; since $T_pP=H_p\oplus V_p$, it suffices to check equality on horizontal and on vertical vectors.
> >
> > On a horizontal vector $X\in H_p$ we have $\pi_H X=X$ and $\omega(X)=0$, so
> > $$(D^\omega\hat s)(X)=d\hat s(\pi_H X)=d\hat s(X),\qquad (d\hat s+\rho_*(\omega)\hat s)(X)=d\hat s(X)+\rho_*(\omega(X))\hat s=d\hat s(X)+0,$$
> > and the two agree.
> >
> > On a vertical vector $\xi_P(p)\in V_p$ (for $\xi\in\mathfrak g$) we have $\pi_H\xi_P=0$, so $(D^\omega\hat s)(\xi_P)=d\hat s(0)=0$. For the other side, differentiate the equivariance relation along the flow $t\mapsto p\cdot\exp(t\xi)$ of $\xi_P$:
> > $$d\hat s\big(\xi_P(p)\big)=\frac{d}{dt}\Big|_{0}\hat s\big(p\cdot\exp(t\xi)\big)=\frac{d}{dt}\Big|_{0}\rho\big(\exp(-t\xi)\big)\hat s(p)=-\rho_*(\xi)\,\hat s(p)\qquad\text{(chain rule; }\tfrac{d}{dt}\big|_0\rho(\exp(-t\xi))=-\rho_*(\xi)\text{),}$$
> > while $\rho_*(\omega(\xi_P(p)))\hat s(p)=\rho_*(\xi)\hat s(p)$ (by the connection axiom $\omega(\xi_P)=\xi$). Hence
> > $$(d\hat s+\rho_*(\omega)\hat s)(\xi_P(p))=-\rho_*(\xi)\hat s(p)+\rho_*(\xi)\hat s(p)=0=(D^\omega\hat s)(\xi_P(p)).$$
> > The two $1$-forms agree on $H_p$ and on $V_p$, hence on all of $T_pP$; therefore $D^\omega\hat s=d\hat s+\rho_*(\omega)\hat s$.
> >
> > **Conclusion.** Both sides equal $d\hat s+\rho_*(\omega)\hat s$, so $\Phi(d^\nabla s)=D^\omega(\Phi s)$. $\blacksquare$

> [!note]- Lemma 4: The operators are local, and every form is locally a sum of scalar-form times section
> **Statement:** (a) The connection $\nabla$, hence $d^\nabla$, is a local operator: if $\alpha\in\Omega^q(M;E)$ vanishes on an open set $U$, then $d^\nabla\alpha$ vanishes on $U$; equivalently $d^\nabla\alpha|_U$ depends only on $\alpha|_U$. The same holds for $D^\omega$ and for $\Phi$. (b) Over the domain $U$ of any local frame $(s_1,\dots,s_r)$ of $E$, every $\alpha\in\Omega^q(M;E)$ is a finite sum $\alpha|_U=\sum_{a=1}^r\eta^a\wedge s_a$ with uniquely determined $\eta^a\in\Omega^q(U)$.
>
> **Hint:** For locality use a bump function equal to $1$ near a point and supported in $U$; for (b) expand $\alpha$ in the frame.
>
> **Why needed:** Locality reduces the global identity to a neighbourhood of each point; the decomposition reduces it to single terms $\eta\wedge s$, which Lemmas 1–3 handle.
>
> > [!note]- Full proof
> > **(a) Locality of $\nabla$ and $d^\nabla$.** Let $\alpha\in\Omega^q(M;E)$ vanish on the open set $U$, and fix $m\in U$. Choose a [[Thm - Existence of Smooth Bump Functions|smooth bump function]] $\chi\in C^\infty(M)$ with $\chi\equiv 1$ on a neighbourhood $W\ni m$, $W\subset U$, and $\operatorname{supp}\chi\subset U$. Then $\chi\,\alpha=0$ on all of $M$ (it is $0$ outside $\operatorname{supp}\chi\subset U$, and $0$ on $U$ because $\alpha|_U=0$). Applying $d^\nabla$ and the graded Leibniz rule (with $\chi$ a $0$-form),
> > $$0=d^\nabla(\chi\,\alpha)=d\chi\wedge\alpha+\chi\,d^\nabla\alpha\qquad\text{(graded Leibniz rule for }d^\nabla\text{).}$$
> > Evaluate at $m$: since $\chi\equiv 1$ on $W$, we have $d\chi_m=0$ and $\chi(m)=1$, so $0=0+d^\nabla\alpha|_m$, i.e. $d^\nabla\alpha|_m=0$. As $m\in U$ was arbitrary, $d^\nabla\alpha|_U=0$. Applying this to a difference $\alpha-\alpha'$ shows $d^\nabla\alpha|_U$ depends only on $\alpha|_U$. The operator $D^\omega=(d\,\cdot)\circ\pi_H$ is built from the exterior derivative $d$ (local, by the same bump-function argument on $P$) and the pointwise projection $\pi_H$, hence is local; and $\Phi$ is defined pointwise ($\hat\alpha_p$ depends only on $\alpha_{\pi(p)}$), hence local.
> >
> > **(b) Local decomposition.** Let $(s_1,\dots,s_r)$ be a smooth frame of $E$ over $U$ (a family of sections with $(s_1(m),\dots,s_r(m))$ a basis of $E_m$ for each $m\in U$; such a frame exists on any set over which $E$ is trivial). At each $m\in U$ the covector part of $\alpha_m\in\Lambda^qT^*_mM\otimes E_m$ expands uniquely in this basis: there are unique $\eta^a_m\in\Lambda^qT^*_mM$ with $\alpha_m=\sum_a\eta^a_m\otimes s_a(m)$. The coefficients $\eta^a$ are smooth because they are obtained from $\alpha$ and the dual frame $(s^1,\dots,s^r)$ of $E^*$ by the smooth pairing $\eta^a=\langle s^a,\alpha\rangle$ (contraction of the $E^*$-section $s^a$ against the $E$-valued form $\alpha$). Writing $\eta^a\wedge s_a:=\eta^a\otimes s_a$, we obtain $\alpha|_U=\sum_{a=1}^r\eta^a\wedge s_a$ with $\eta^a\in\Omega^q(U)$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\pi\colon P\to M$, $\omega$, $\rho$, $V$, $E=P\times_\rho V$, $\nabla=\nabla^\omega$, $D^\omega$, $d^\nabla$, and $\Phi$ be as in the Statement. We prove $\Phi(d^\nabla\alpha)=D^\omega(\Phi\alpha)$ for all $\alpha\in\Omega^q(M;E)$, all $q\ge 0$, then the two corollaries.
>
> **Step 0 — the identity is well-posed.** By the [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|basic-forms theorem]], $\Phi\colon\Omega^q(M;E)\to\Omega^q_{\mathrm{bas}}(P;V)^G$ is a bijection for every $q$. By Corollary 1 of [[Def - Exterior Covariant Derivative on a Principal Bundle|the exterior-covariant-derivative page]], $D^\omega$ maps $\Omega^q_{\mathrm{bas}}(P;V)^G$ into $\Omega^{q+1}_{\mathrm{bas}}(P;V)^G$. Thus both $\Phi(d^\nabla\alpha)$ and $D^\omega(\Phi\alpha)$ are elements of $\Omega^{q+1}_{\mathrm{bas}}(P;V)^G$, and comparing them is meaningful.
>
> **Step 1 — reduction to local monomials.** Fix $\alpha\in\Omega^q(M;E)$ and a point $m\in M$. Choose a set $U\ni m$ over which $E$ is trivial and pick a smooth frame $(s_1,\dots,s_r)$ of $E|_U$. By Lemma 4(b), $\alpha|_U=\sum_{a=1}^r\eta^a\wedge s_a$ with $\eta^a\in\Omega^q(U)$. Both maps $\alpha\mapsto\Phi(d^\nabla\alpha)$ and $\alpha\mapsto D^\omega(\Phi\alpha)$ are local by Lemma 4(a) (each of $d^\nabla$, $D^\omega$, $\Phi$ is local, and compositions of local operators are local), so their values over $\pi^{-1}(U)$ depend only on $\alpha|_U$. It therefore suffices to prove
> $$\Phi\big(d^\nabla(\eta\wedge s)\big)=D^\omega\big(\Phi(\eta\wedge s)\big)\qquad\text{for }\eta\in\Omega^q(U),\ s\in\Gamma(E|_U),$$
> and then sum over the $r$ terms; the identity over $\pi^{-1}(U)$ follows, and as $m$ was arbitrary the identity holds on all of $P$. (All operators restrict to $U$ and $\pi^{-1}(U)$ compatibly, again by locality.)
>
> **Step 2 — the single-term computation.** Let $\eta\in\Omega^q(U)$ and $s\in\Gamma(E|_U)$, and write $\hat s=\Phi(s)$. Using the graded Leibniz rule for $d^\nabla$ (from [[Def - Exterior Covariant Derivative on a Vector Bundle]]) with the scalar $q$-form $\eta$ and the section $s$,
> $$d^\nabla(\eta\wedge s)=d\eta\wedge s+(-1)^q\,\eta\wedge d^\nabla s\qquad\text{(graded Leibniz rule for }d^\nabla\text{; }d^\nabla s=\nabla s\text{).}$$
> Apply $\Phi$ and use its $\mathbb R$-linearity together with Lemma 1 (module compatibility), applied to the $(q+1)$-form $d\eta$ wedged with $s$ and to the $q$-form $\eta$ wedged with $\nabla s$:
> $$\Phi\big(d^\nabla(\eta\wedge s)\big)=\Phi(d\eta\wedge s)+(-1)^q\,\Phi(\eta\wedge\nabla s)=\pi^*(d\eta)\wedge\hat s+(-1)^q\,\pi^*\eta\wedge\Phi(\nabla s)\qquad\text{(Lemma 1, twice).}$$
> By Lemma 3 (the degree-zero base case), $\Phi(\nabla s)=\Phi(d^\nabla s)=D^\omega(\Phi s)=D^\omega\hat s$. Substituting,
> $$\Phi\big(d^\nabla(\eta\wedge s)\big)=\pi^*(d\eta)\wedge\hat s+(-1)^q\,\pi^*\eta\wedge D^\omega\hat s\qquad\text{(Lemma 3).}$$
> Now apply Lemma 2 (the derivation rule for $D^\omega$ over pulled-back forms) with $k=q$ and $\phi=\hat s\in\Omega^0_{\mathrm{bas}}(P;V)^G$:
> $$\pi^*(d\eta)\wedge\hat s+(-1)^q\,\pi^*\eta\wedge D^\omega\hat s=D^\omega\big(\pi^*\eta\wedge\hat s\big)\qquad\text{(Lemma 2, read right-to-left).}$$
> Finally, by Lemma 1 again, $\pi^*\eta\wedge\hat s=\Phi(\eta\wedge s)$. Combining the last three displays,
> $$\Phi\big(d^\nabla(\eta\wedge s)\big)=D^\omega\big(\pi^*\eta\wedge\hat s\big)=D^\omega\big(\Phi(\eta\wedge s)\big),$$
> which is the single-term identity. Summing over the frame terms (Step 1) proves $\Phi(d^\nabla\alpha)=D^\omega(\Phi\alpha)$ for all $\alpha$ and all $q$. This is the commuting square.
>
> **Step 3 — the local formula $d^\nabla=d+\rho_*(A)\wedge$.** Let $s\colon U\to P$ be a local gauge with $A=s^*\omega\in\Omega^1(U;\mathfrak g)$, and let $\alpha\in\Omega^q(U;E)$ be written $\alpha=[s,\phi]$ with $\phi\in\Omega^q(U;V)$, meaning $\alpha_m(v_\bullet)=\ell_{s(m)}(\phi_m(v_\bullet))=[s(m),\phi_m(v_\bullet)]$. First, $\phi=s^*\hat\alpha$: for $v_i\in T_mU$, taking $p=s(m)$ and lifts $\hat v_i=ds\,v_i$ (so $d\pi\,\hat v_i=d(\pi\circ s)\,v_i=v_i$ since $\pi\circ s=\operatorname{id}_U$),
> $$\ell_{s(m)}\big(\hat\alpha_{s(m)}(ds\,v_\bullet)\big)=\alpha_m(d\pi\,ds\,v_\bullet)=\alpha_m(v_\bullet)=\ell_{s(m)}\big(\phi_m(v_\bullet)\big)\qquad\text{(definition of }\hat\alpha\text{; then }\alpha=[s,\phi]\text{),}$$
> and applying the isomorphism $\ell_{s(m)}^{-1}$ gives $\phi_m=(s^*\hat\alpha)_m$. The same relation applied to $d^\nabla\alpha$ shows its local representative in the gauge $s$ is $s^*\widehat{d^\nabla\alpha}$. Now compute, using Step 2 ($\widehat{d^\nabla\alpha}=D^\omega\hat\alpha$) and the tensorial formula:
> $$s^*\widehat{d^\nabla\alpha}=s^*\big(D^\omega\hat\alpha\big)=s^*\big(d\hat\alpha+\rho_*(\omega)\wedge\hat\alpha\big)\qquad\text{(Step 2; then the tensorial formula for the basic equivariant }\hat\alpha\text{)}$$
> $$=s^*(d\hat\alpha)+s^*\big(\rho_*(\omega)\wedge\hat\alpha\big)=d(s^*\hat\alpha)+\rho_*(s^*\omega)\wedge s^*\hat\alpha\qquad\text{(}s^*d=ds^*\text{ and }s^*\text{ respects the wedge, by the pullback theorem; }s^*\text{ commutes with the fixed linear map }\rho_*\text{)}$$
> $$=d\phi+\rho_*(A)\wedge\phi\qquad\text{(since }s^*\hat\alpha=\phi\text{ and }s^*\omega=A\text{).}$$
> Hence $d^\nabla\alpha=[s,\,d\phi+\rho_*(A)\wedge\phi]$, i.e. $d^\nabla=d+\rho_*(A)\wedge$ in the gauge $s$. This is the local-formula corollary.
>
> **Step 4 — the adjoint case and the two Bianchi identities.** Take $\rho=\operatorname{Ad}\colon G\to GL(\mathfrak g)$, $V=\mathfrak g$, $\rho_*=\operatorname{ad}$, so $E=\operatorname{ad}P$. By the [[Def - Curvature of a Principal Connection|definition of the base curvature]], $F_\omega\in\Omega^2(M;\operatorname{ad}P)$ is the unique form with $\pi^*F_\omega$ corresponding to $\Omega\in\Omega^2(P;\mathfrak g)$ under $\Phi$; that is, $\Phi(F_\omega)=\Omega$. Applying the commuting square (Step 2) with $q=2$,
> $$\Phi\big(d^{\nabla_\omega}F_\omega\big)=D^\omega\big(\Phi F_\omega\big)=D^\omega\Omega\qquad\text{(Step 2, }\rho=\operatorname{Ad}\text{; then }\Phi F_\omega=\Omega\text{).}$$
> Locally, by Step 3 with $\rho_*=\operatorname{ad}$ and $\operatorname{ad}(A)\wedge F_A=[A\wedge F_A]$ (the definition of the bracket of $\mathfrak g$-valued forms, [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]]), the local representative of $d^{\nabla_\omega}F_\omega$ is
> $$d F_A+\operatorname{ad}(A)\wedge F_A=dF_A+[A\wedge F_A],\qquad F_A=s^*\Omega=dA+\tfrac12[A\wedge A].$$
> Therefore the total-space identity $D^\omega\Omega=0$ holds if and only if the base identity $d^{\nabla_\omega}F_\omega=0$ holds (they correspond under the bijection $\Phi$), if and only if $dF_A+[A\wedge F_A]=0$ in every gauge. This is the two-guises corollary; the common vanishing is the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]], established there and not used here. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry: the second Bianchi identity as a horizontal shadow.** On a Riemannian manifold $(M,g)$ take $P=\operatorname{Fr}_{O(n)}(TM)$ the orthonormal frame bundle, $\omega$ the Levi-Civita connection form, and $\rho$ the standard representation of $O(n)$ on $\mathbb R^n$, so $E=TM$. The theorem identifies the covariant exterior derivative $d^{\nabla^{\mathrm{LC}}}$ of the curvature tensor $R\in\Omega^2(M;\operatorname{End}TM)$ with $D^\omega$ upstairs, and the horizontal Bianchi identity $D^\omega\Omega=0$ becomes the second Bianchi identity $d^{\nabla}R=0$, i.e. $\nabla_{[a}R_{bc]de}=0$. This is a genuinely different context because the input is a metric, not a bundle, and the payoff is that the classical tensor identity is the descent of a one-line horizontal statement.

**Mathematical physics: covariant conservation of the Yang–Mills current.** For a matter field $\phi$ that is a section of $E=P\times_\rho V$ and a Lagrangian coupling it to the gauge field, the field equations produce a current $J\in\Omega^{n-1}(M;\operatorname{ad}P)$. The theorem's local formula $d^\nabla=d+\rho_*(A)\wedge$ turns "covariant conservation $d^\nabla{\star}F=J$ and $d^\nabla J=0$" into computations one can do with the coordinate potential $A_\mu$ alone. The application is non-obvious because it lets a physicist who never leaves a single chart nonetheless compute a globally correct covariant derivative, since the local formula is the shadow of the global operator.

**Complex geometry: the Chern connection and $\bar\partial$.** On a holomorphic Hermitian line bundle $L\to X$ with its Chern connection, $P$ is the associated $U(1)$-bundle and $\rho=\varrho_1$ the weight-one representation. The theorem identifies $d^\nabla$ on $L$-valued forms with $D^\omega$ on $S^1$-equivariant $\mathbb C$-valued forms upstairs; splitting into types recovers the $(0,1)$-part as $\bar\partial$ and the curvature $F_\omega$ as the first Chern form $\tfrac{i}{2\pi}F$. The context is different because the base carries a complex structure, and the theorem is what guarantees that the intrinsic $D^\omega$ and the coordinate $\bar\partial+\partial$ description agree.

---

# Bridges

- **[[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|The induced connection]]** — the degree-zero half. That theorem constructs $\nabla^\omega$ and proves equation (47), which is exactly the base case (Lemma 3) of the present theorem. The present theorem is its extension from sections to forms of all degrees: it says the induced connection's *exterior* covariant derivative is again nothing but $D^\omega$, so no new construction is needed above degree zero.

- **[[Def - Exterior Covariant Derivative on a Principal Bundle|The exterior covariant derivative on the total space]]** — the object being compared. Here $D^\omega=(d\,\cdot)\circ\pi_H$ is the operator on $P$. Its tensorial formula $D^\omega\alpha=d\alpha+\rho_*(\omega)\wedge\alpha$ on basic equivariant forms, and its preservation of basicness (Corollary 1 there), are the two facts that make the comparison possible; without the tensorial formula the projection description and the Leibniz description could not be matched term by term.

- **[[Def - Curvature of a Principal Connection|The base curvature and the total-space curvature]]** — the case $\rho=\operatorname{Ad}$, $q=2$, relating $F_\omega\in\Omega^2(M;\operatorname{ad}P)$ and $\Omega\in\Omega^2(P;\mathfrak g)$. The definition of $F_\omega$ *is* the statement $\Phi(F_\omega)=\Omega$; feeding this into the commuting square is what makes $d^{\nabla_\omega}F_\omega$ and $D^\omega\Omega$ the same object, and thereby unifies the two forms of the Bianchi identity.

- **[[Thm - Bianchi Identity for a Principal Connection|The Bianchi identity]]** — the principal consumer. It proves $D^\omega\Omega=0$ by a horizontal computation on $P$ and then invokes the present theorem to conclude $d^{\nabla_\omega}F_\omega=0$, that is $dF_A+[A\wedge F_A]=0$, on $M$. The present theorem is listed among its prerequisites for exactly this reason and must therefore stand on its own, never citing the Bianchi identity.

- **[[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle|The frame-bundle correspondence]]** — the reverse translation for vector bundles. Together with the present theorem it shows that the passage $\nabla\leftrightarrow\omega$ between a vector-bundle connection and the associated principal connection intertwines *all* the derived operators — covariant derivative, exterior covariant derivative, and curvature — so the two calculus frameworks are interchangeable at every level.

---

# Unlocked by This

> [!tip] Naturality of characteristic forms *(from Chern–Weil theory, chapter VI)*
> Because $D^\omega$ intertwines with $d^\nabla$ and with the base de Rham $d$ on invariant polynomials of the curvature, the Chern–Weil forms $f(F_\omega)$ are closed and their cohomology classes are connection-independent. The present theorem is the compatibility that lets the closedness computed upstairs from $D^\omega\Omega=0$ descend to $df(F_\omega)=0$ on the base. See **Thm - Chern-Weil Theorem**.

> [!tip] Coupling of gauge fields to matter *(from Yang–Mills theory, chapter VII)*
> The local formula $d^\nabla=d+\rho_*(A)\wedge$ is the minimal-coupling prescription $\partial\mapsto\partial+\rho_*(A)$ for a matter field in the representation $\rho$; the theorem certifies that this coordinate recipe is the honest covariant derivative of a global connection on the associated bundle. See **Def - The Yang-Mills Functional**.
