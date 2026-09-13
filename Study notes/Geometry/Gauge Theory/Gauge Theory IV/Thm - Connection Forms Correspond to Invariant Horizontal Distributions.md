---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Connection on a Principal Bundle"
  - "Def - Horizontal Subspace and Horizontal Lift"
  - "Def - Distribution on a Manifold"
  - "Def - Fundamental Vector Field of a Group Action"
  - "Def - Principal G-Bundle"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a smooth **[[Def - Principal G-Bundle|principal G-bundle]]**: a smooth manifold $P$ carrying a smooth free right action of a Lie group $G$, written $R_g(p)=p\cdot g$, whose orbits are exactly the fibres of $\pi$ and which is locally trivial. We write $m:=\dim M$ and, for the Lie group, $\dim G=\dim\mathfrak g$, so that $\dim P=m+\dim G$; the fibre $P_b=\pi^{-1}(b)$ is a single orbit, of dimension $\dim G$.

We write $\mathfrak g=T_eG$ for the **Lie algebra** of $G$, with the bracket of left-invariant vector fields; for a matrix group this is the commutator. The **group adjoint** is $\operatorname{Ad}_g=d_e(a\mapsto gag^{-1})\colon\mathfrak g\to\mathfrak g$; for a matrix group $\operatorname{Ad}_g X=gXg^{-1}$. It is always the group adjoint (a subscript that is a group element), never the algebra adjoint $\operatorname{ad}_X=[\,X,\cdot\,]$; the two are kept distinct on every page of this series.

For each $\xi\in\mathfrak g$ the **[[Def - Fundamental Vector Field of a Group Action|fundamental vector field]]** of $\xi$ on $P$ is
$$\xi_P(p):=\frac{d}{dt}\Big|_{t=0}\,p\cdot\exp(t\xi)=d_e\ell_p(\xi)\in T_pP,$$
where $\ell_p\colon G\to P$, $\ell_p(a)=p\cdot a$, is the **orbit map** (a diffeomorphism onto the fibre through $p$, because the action is free and fibre-transitive). Because the action is free, at each $p$ the linear map
$$\iota_p\colon\mathfrak g\longrightarrow T_pP,\qquad \iota_p(\xi):=\xi_P(p),$$
is injective with image the **vertical subspace**
$$V_pP:=\ker(d\pi_p)=\{\xi_P(p):\xi\in\mathfrak g\},$$
so $\iota_p$ is a linear isomorphism $\mathfrak g\xrightarrow{\ \sim\ }V_pP$; every vector tangent to a fibre is $\xi_P(p)$ for exactly one $\xi\in\mathfrak g$. We abbreviate $V_p:=V_pP$ and write $VP=\bigsqcup_p V_pP=\ker d\pi$ for the **vertical bundle**, a smooth subbundle of $TP$ of rank $\dim G$. A tangent vector is **vertical** if it lies in $V_pP$.

A **[[Def - Connection on a Principal Bundle|connection form]]** (principal connection) on $P$ is a $\mathfrak g$-valued $1$-form $\omega\in\Omega^1(P;\mathfrak g)$ satisfying two conditions, restated in full at the point of use below:

> [!note]- The two connection-form conditions (restated from the connection-form page)
> ![[Def - Connection on a Principal Bundle#The Definition]]

The set of all connection forms is $\mathcal A(P)$. A **[[Def - Distribution on a Manifold|distribution]]** on $P$ is a smooth subbundle $H\subset TP$; equivalently, each point has a neighbourhood on which $H$ is spanned by finitely many pointwise-independent smooth vector fields (a **local frame** of $H$). We write $H_p$ for the fibre of $H$ at $p$.

> [!warning] Convention: notation and the two directions of the correspondence
> Bär (Definition 2.3.2, Remark 2.3.4) writes the tangent space to the fibre as $T_pP_{\pi(p)}$; we write $V_pP$ for the same space, and call $H_p=\ker\omega_p$ the horizontal subspace exactly as he does. Bär's Remark 2.3.4 proves only the map $\omega\mapsto H$ half of the statement below — that $\ker\omega$ is a smooth invariant complement to the vertical bundle. The converse half, that every smooth invariant complement arises from a unique connection form, is the content of `conventions.md` ("equivalently a $G$-invariant horizontal distribution $H=\ker\omega$") and is written out here in full; the combined statement is Kobayashi–Nomizu I, Proposition II.1.1. Haydys writes $a$ for the connection form; the correspondence is identical.

---

# Statement

> **Theorem (connection forms as invariant horizontal distributions).** Let $\pi\colon P\to M$ be a principal $G$-bundle, with vertical bundle $VP=\ker d\pi$ and fundamental-field isomorphisms $\iota_p\colon\mathfrak g\xrightarrow{\sim}V_pP$, $\iota_p(\xi)=\xi_P(p)$. Call a smooth distribution $H\subset TP$ a **connection distribution** if it satisfies both:
> 1. **Complementarity.** $T_pP=H_p\oplus V_pP$ for every $p\in P$ (hence $H$ has rank $m=\dim M$);
> 2. **Invariance.** $dR_g(H_p)=H_{p\cdot g}$ for all $p\in P$ and $g\in G$.
>
> Then the map
> $$\Phi\colon\mathcal A(P)\longrightarrow\{\text{connection distributions}\},\qquad \Phi(\omega):=\ker\omega=\{\,v\in TP:\omega(v)=0\,\},$$
> is a bijection. Its inverse is the map $\Psi$ that sends a connection distribution $H$ to the $1$-form $\omega_H\in\Omega^1(P;\mathfrak g)$ determined by
> $$\omega_H(v):=\iota_p^{-1}(v_V)\qquad\text{for }v\in T_pP,\text{ where }v=v_H+v_V\text{ is the unique decomposition with }v_H\in H_p,\ v_V\in V_pP;$$
> equivalently, $\omega_H$ vanishes on $H$ and equals $\iota_p^{-1}$ on $V_pP$. In words: a connection form and a smooth, group-invariant field of horizontal complements to the fibres are the same datum, and the form is recovered from the field as "project onto the vertical part, then read it off in $\mathfrak g$ through $\iota_p^{-1}$."

---

# Motivation

A connection on a principal bundle was defined in [[Def - Connection on a Principal Bundle|two clauses on a differential form]], and the definition warned that a connection has three faces: the form $\omega$, the horizontal distribution $H$, and the horizontal lift. This theorem is the rigorous statement that the first two faces carry *exactly the same information* — that passing from $\omega$ to $\ker\omega$ loses nothing and can always be undone. Without it, "the horizontal distribution of a connection" and "the connection form" would be two objects that happen to travel together; with it, they are one object seen from two sides, and one is free to work with whichever is convenient for the task at hand.

The distinction matters because the two faces are good for different things. The form $\omega$ is an ordinary differential form: the exterior derivative $d$, pullback $s^*$, and the [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|bracket of $\mathfrak g$-valued forms]] all act on it, which is what makes the [[Thm - Structure Equation for the Curvature|structure equation]] $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$ and every local computation possible. The distribution $H$ is the geometric object: it is what one integrates to transport a point along a curve, and it is the thing whose failure to be integrable *is* the curvature. Many constructions are cleanest stated for $H$ (parallel transport, holonomy, the Frobenius criterion for flatness) and then computed through $\omega$. The theorem licenses moving back and forth at will.

It also settles which distributions are admissible. One might try to build a connection by simply choosing, at each point, a complement to the vertical subspace. The theorem says such a choice is a connection **if and only if** it is smooth and $G$-invariant; the invariance is not optional decoration but the precise condition that makes the choice descend to geometry on the base $M$. This is the same content that made $\mathcal A(P)$ fail to be a vector space and made clause (1) of the connection definition indispensable, now stated on the geometric side.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem's literal input on the left is a connection form; on the right, a smooth invariant complement. The skill is recognising, in a problem that mentions neither, that one of the two is secretly present.

The first disguised source is **a distinguished sub-bundle of $TP$ produced by geometry rather than by a connection**. Whenever a principal bundle carries extra structure — a $G$-invariant Riemannian metric, an integrable foliation transverse to the fibres, a reduction of the structure group — that structure often hands you a smooth field of complements to the vertical subspace for free. The bridge $B\Rightarrow A$ is: check that the field is $G$-invariant (condition 2) and transverse to the fibres (condition 1); the theorem then converts it into a genuine connection form with no further work. *Example problem:* on a bundle equipped with a $G$-invariant metric, take $H_p:=(V_pP)^\perp$, the orthogonal complement of the vertical subspace; invariance of the metric gives invariance of $H$, and the theorem produces the associated connection (this is how the Hopf connection arises from the round metric on the sphere).

The second disguised source is **a horizontal lift, or a rule for parallel transport, specified directly**. If a problem tells you how to lift each tangent vector on $M$ to $P$ — a linear right inverse $\sigma_p\colon T_{\pi(p)}M\to T_pP$ of $d\pi_p$, varying smoothly and equivariantly — then $H_p:=\operatorname{im}\sigma_p$ is a connection distribution, and the theorem yields the connection form whose horizontal lift $\sigma$ is. The bridge is that "an equivariant smooth right splitting of $d\pi$" is literally condition (1)+(2). *Example problem:* given a smooth family of parallel-transport operators along all curves, differentiate to recover the horizontal lift, hence the distribution, hence $\omega$.

The third disguised source is **an invariant $\mathfrak g$-valued $1$-form that is only known to be normalised on the vertical subspace, with its equivariance in doubt**. Rather than verify clause (1) of the connection definition directly, one can pass to $\ker\omega$ and check the single geometric condition $dR_g(\ker\omega_p)=\ker\omega_{pg}$, which is sometimes far easier to see (for instance when $\ker\omega$ is cut out by an invariant construction). The bridge runs $A\Leftarrow$(this theorem)$\Leftarrow$(invariance of $\ker\omega$): an invariant kernel forces the form to be equivariant. *Example problem:* on the trivial bundle $M\times G$, show $\operatorname{pr}_2^*\theta$ is a connection by exhibiting its horizontal distribution $T_mM\times\{0\}$ as manifestly invariant, sidestepping the pullback computation of clause (1).

**Targets (Output Amplification).** The bare output is a bijection; combined with other facts it becomes a working tool.

Combine the bijection with **the Frobenius theorem**. A connection distribution $H$ is a smooth distribution, so one may ask whether it is integrable. The extra ingredient is [[Thm - The Frobenius Theorem|Frobenius's integrability criterion]]: $H$ is integrable if and only if $\Gamma(H)$ is closed under the Lie bracket. The payoff is a geometric characterisation of *flat* connections — the ones with zero curvature — as exactly those whose horizontal distribution is a foliation of $P$ transverse to the fibres, which is the starting point of the holonomy description of flat bundles. This is non-obvious because "curvature" is defined analytically through $d\omega$ and only the correspondence turns it into a statement about integrating a plane field.

Combine the bijection with **the affine structure of $\mathcal A(P)$**. The [[Thm - Existence of Connections on Principal Bundles|existence theorem]] says $\mathcal A(P)$ is a non-empty affine space modelled on $\Omega^1(M;\operatorname{ad}P)$. Transporting this across $\Phi$ gives the corresponding statement for distributions: the connection distributions form an affine space in the sense that any two differ by an $\operatorname{ad}P$-valued $1$-form on the base, read as a bundle map $H\to VP$. The payoff is that "average two connections with a partition of unity" — the construction that proves connections exist — is legitimate precisely because both the analytic and the geometric side are affine.

Combine the bijection with **a right splitting of $d\pi$**, i.e. the horizontal lift. Because $\Phi$ identifies $\omega$ with $H=\ker\omega$, and $H_p$ maps isomorphically to $T_{\pi(p)}M$ under $d\pi_p$ (complementarity plus $\ker d\pi_p=V_pP$), every tangent vector on $M$ acquires a unique horizontal lift to each point of the fibre. The extra ingredient is the identity $d\pi_p|_{H_p}\colon H_p\xrightarrow{\sim}T_{\pi(p)}M$; the payoff is the whole apparatus of parallel transport and holonomy in the next chapter, all of which is phrased through the lift and therefore rests on this correspondence.

---

# Why Is It True

Strip away the formalism and the statement is nearly a tautology about complements. At each point $p$ the tangent space $T_pP$ has a *canonically given* piece, the vertical subspace $V_pP$, and that piece is canonically labelled by $\mathfrak g$ through the isomorphism $\iota_p(\xi)=\xi_P(p)$. To specify a connection is to specify the *missing* piece: a complement $H_p$. Once a complement is chosen, any tangent vector $v$ splits uniquely into a horizontal part (in $H_p$) and a vertical part (in $V_pP$), and the vertical part, being in $V_pP$, has a name in $\mathfrak g$. The form $\omega$ is nothing but the operation "throw away the horizontal part, keep the vertical part, read its name": $\omega(v)=\iota_p^{-1}(v_V)$. The distribution and the form are therefore two encodings of the single choice of complement, and translating between them is just the linear algebra of direct-sum decompositions.

**A connection is a choice of horizontal complement compatible with the group; the connection form is that choice's vertical projection, read off in $\mathfrak g$.**

Two things must be checked for the tautology to be a theorem rather than a slogan, and they are exactly the two non-tautological conditions in the statement. First, the choice of complement must be *smooth* in $p$ — otherwise $\omega$ is not a differential form, only a discontinuous field of covectors. Smoothness passes back and forth because $\omega$ smooth means $\ker\omega$ is a smooth subbundle (kernel of a constant-rank bundle map), and $H$ smooth means the vertical projection along $H$ is a smooth bundle map (in a smooth frame adapted to $H\oplus VP$). Second, the choice must be *$G$-invariant*: the complement over $p\cdot g$ must be the $dR_g$-image of the complement over $p$. On the form side this is precisely clause (1), the equivariance $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$; the translation between "invariant complement" and "equivariant form" is driven by the one identity that says how $dR_g$ moves a vertical vector, namely $dR_g(\xi_P(p))=(\operatorname{Ad}_{g^{-1}}\xi)_P(p\cdot g)$. That identity is the hinge: it says the group moves vertical directions by rotating their $\mathfrak g$-labels through $\operatorname{Ad}_{g^{-1}}$, which is exactly the rotation clause (1) demands of $\omega$.

---

# What Makes This Hard

The conceptual content is easy linear algebra; the two places a proof can go wrong are both about *smoothness*, not about the pointwise bijection. Going from a distribution $H$ to a form $\omega_H$, one must show $\omega_H$ is smooth, and the pointwise formula "read off the vertical part in $\mathfrak g$" does not make this visible — the honest argument builds a single smooth local frame of $TP$ by concatenating a smooth frame of $H$ with the global smooth frame $\{(\xi^a)_P\}$ of $VP$, and reads the vertical coordinates off in that frame, where they are manifestly smooth. Going the other way, one must know that $\ker\omega$ is a smooth *subbundle* of constant rank, which requires observing that $\omega_p\colon T_pP\to\mathfrak g$ is surjective at every $p$ (clause (2) makes it onto), so its kernel has constant rank $m$ and is smooth. The second common error is to prove the invariance clause for $\omega_H$ by manipulating the form directly and forgetting that it rests entirely on the fundamental-field transformation law $dR_g(\xi_P(p))=(\operatorname{Ad}_{g^{-1}}\xi)_P(p\cdot g)$; without that identity the $\operatorname{Ad}_{g^{-1}}$ in clause (1) appears from nowhere.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build the two maps $\Phi(\omega)=\ker\omega$ and $\Psi(H)=\omega_H$, show each lands where claimed (a connection form has a smooth invariant complementary kernel; an invariant smooth complement gives a smooth form satisfying both clauses), then show the two composites are the identity by unwinding the definitions against clause (2). The one external identity used is the fundamental-field transformation law; everything else is direct-sum linear algebra done smoothly.

**Subgoal decomposition:**

1. **The fundamental-field transformation law.** Prove $dR_g(\xi_P(p))=(\operatorname{Ad}_{g^{-1}}\xi)_P(p\cdot g)$.
   - *Hint:* Write $R_g\circ\ell_p=\ell_{p\cdot g}\circ C_{g^{-1}}$ where $C_{g^{-1}}(a)=g^{-1}ag$, differentiate at $e$, and use $d_eC_{g^{-1}}=\operatorname{Ad}_{g^{-1}}$.
   - *Why needed:* It is the sole engine that turns geometric invariance of $H$ into the $\operatorname{Ad}_{g^{-1}}$-equivariance of $\omega_H$, and conversely.

2. **$\Phi$ lands in connection distributions ($\ker\omega$ is smooth, complementary, invariant).** For $\omega\in\mathcal A(P)$, show $\ker\omega$ is a smooth rank-$m$ subbundle with $T_pP=\ker\omega_p\oplus V_pP$ and $dR_g(\ker\omega_p)=\ker\omega_{pg}$.
   - *Hint:* Surjectivity of $\omega_p$ (clause (2)) gives constant rank, hence a smooth kernel bundle; complementarity from $\omega_p|_{V_pP}$ being an isomorphism; invariance from clause (1) applied to a vector in the kernel.
   - *Why needed:* This is the forward half of the bijection (Bär's Remark 2.3.4).

3. **$\Psi$ produces a smooth form.** For a connection distribution $H$, show the pointwise formula $\omega_H(v)=\iota_p^{-1}(v_V)$ defines a smooth $\mathfrak g$-valued $1$-form.
   - *Hint:* Concatenate a smooth local frame of $H$ with the global smooth frame $\{(\xi^a)_P\}$ of $VP$ to get a smooth frame of $TP$; the vertical coordinates in that frame are smooth.
   - *Why needed:* Without smoothness $\omega_H$ is not a differential form and $\Psi$ is not defined.

4. **$\omega_H$ satisfies clauses (2) and (1).** Show $\omega_H(\xi_P)=\xi$ and $R_g^*\omega_H=\operatorname{Ad}_{g^{-1}}\omega_H$.
   - *Hint:* Clause (2) is immediate from the decomposition of a vertical vector; clause (1) uses invariance of $H$, subgoal 1, and uniqueness of the decomposition at $p\cdot g$.
   - *Why needed:* It is the backward half: $\omega_H\in\mathcal A(P)$.

5. **Mutual inverse.** Show $\ker\omega_H=H$ and $\omega_{\ker\omega}=\omega$.
   - *Hint:* $\ker\omega_H=\{v:v_V=0\}=H$ by construction; for the other, decompose $v$ along $\ker\omega$ and use clause (2) for $\omega$ to see $\omega(v)$ equals the $\mathfrak g$-label of $v_V$.
   - *Why needed:* It upgrades "two well-defined maps" to "a bijection with the stated inverse".

---

# Lemma Decomposition

> [!note]- Lemma 1: Fundamental-field transformation law
> **Statement:** For every $p\in P$, $g\in G$, and $\xi\in\mathfrak g$,
> $$dR_g\big(\xi_P(p)\big)=\big(\operatorname{Ad}_{g^{-1}}\xi\big)_P(p\cdot g).$$
>
> **Hint:** Express both fundamental fields through orbit maps and factor the right action through conjugation.
>
> **Why needed:** It is the single identity linking the geometric group action on vertical vectors to the algebraic $\operatorname{Ad}_{g^{-1}}$, used in both directions of the correspondence.
>
> > [!note]- Full proof
> > Recall the orbit map $\ell_q\colon G\to P$, $\ell_q(a)=q\cdot a$, and that $\eta_P(q)=d_e\ell_q(\eta)$ for every $q\in P$ and $\eta\in\mathfrak g$ (definition of the fundamental field). Write $C_{g^{-1}}\colon G\to G$, $C_{g^{-1}}(a)=g^{-1}ag$, for conjugation by $g^{-1}$.
> >
> > **Factor the right action through conjugation.** For every $a\in G$,
> > $$(R_g\circ\ell_p)(a)=p\cdot a\cdot g=p\cdot g\cdot(g^{-1}ag)=\ell_{p\cdot g}\big(C_{g^{-1}}(a)\big)\qquad\text{(associativity of the right action; definition of }C_{g^{-1}}\text{),}$$
> > so $R_g\circ\ell_p=\ell_{p\cdot g}\circ C_{g^{-1}}$ as smooth maps $G\to P$.
> >
> > **Differentiate at the identity.** Since $C_{g^{-1}}(e)=e$, the differential $d_eC_{g^{-1}}$ maps $\mathfrak g=T_eG$ to $\mathfrak g=T_eG$, and the chain rule applied to both sides at $a=e$ gives
> > $$dR_g\circ d_e\ell_p=d_e\ell_{p\cdot g}\circ d_eC_{g^{-1}}\qquad\text{(chain rule on }R_g\circ\ell_p=\ell_{p\cdot g}\circ C_{g^{-1}}\text{).}$$
> > By the definition of the group adjoint, $d_eC_{g^{-1}}=\operatorname{Ad}_{g^{-1}}$ (the adjoint is the differential at $e$ of conjugation, here by $g^{-1}$).
> >
> > **Read off the identity.** Apply both sides to $\xi\in\mathfrak g$ and use $d_e\ell_q(\eta)=\eta_P(q)$ at $q=p$ on the left and at $q=p\cdot g$ on the right:
> > $$dR_g\big(\xi_P(p)\big)=d_e\ell_{p\cdot g}\big(\operatorname{Ad}_{g^{-1}}\xi\big)=\big(\operatorname{Ad}_{g^{-1}}\xi\big)_P(p\cdot g).$$
> > Therefore the law holds. (For a matrix group this is the one-line computation $dR_g(dL_pX)=\tfrac{d}{dt}\big|_0\,p\exp(tX)g=\tfrac{d}{dt}\big|_0\,pg\,g^{-1}\exp(tX)g=dL_{pg}(\operatorname{Ad}_{g^{-1}}X)$.) $\blacksquare$

> [!note]- Lemma 2: The kernel of a connection form is a smooth invariant complement to the vertical bundle
> **Statement:** Let $\omega\in\mathcal A(P)$. Then $H:=\ker\omega=\{v\in TP:\omega(v)=0\}$ is a smooth distribution on $P$ of rank $m=\dim M$ with $T_pP=H_p\oplus V_pP$ for every $p$ and $dR_g(H_p)=H_{p\cdot g}$ for every $p,g$; that is, $H$ is a connection distribution.
>
> **Hint:** Clause (2) makes $\omega_p$ surjective; use the constant-rank kernel of a bundle map for smoothness, the isomorphism $\omega_p|_{V_pP}$ for complementarity, and clause (1) for invariance.
>
> **Why needed:** It is the forward direction $\Phi(\omega)\in\{\text{connection distributions}\}$ (Bär, Remark 2.3.4).
>
> > [!note]- Full proof
> > **Step 0 — $\omega$ is a surjective bundle map of constant rank.** The form $\omega$ is a smooth bundle map $\bar\omega\colon TP\to P\times\mathfrak g$ over $P$, $\bar\omega(v)=(p,\omega_p(v))$ for $v\in T_pP$. By clause (2), for every $\eta\in\mathfrak g$ we have $\omega_p(\eta_P(p))=\eta$, so $\omega_p\colon T_pP\to\mathfrak g$ is **surjective** at every $p$. A bundle map with fibrewise-surjective values has constant rank $\dim\mathfrak g$; hence its kernel $\ker\bar\omega$ is a smooth subbundle of $TP$ of rank $\dim P-\dim\mathfrak g=(m+\dim G)-\dim G=m$ (constant-rank theorem for vector-bundle morphisms). Thus $H=\ker\omega$ is a smooth distribution of rank $m$.
> >
> > **Step 1 — complementarity $T_pP=H_p\oplus V_pP$.** Fix $p$. First, $H_p\cap V_pP=\{0\}$: if $v\in V_pP$ then $v=\eta_P(p)$ for a unique $\eta\in\mathfrak g$ (fundamental-field isomorphism $\iota_p$), and $v\in H_p=\ker\omega_p$ forces $0=\omega_p(v)=\omega_p(\eta_P(p))=\eta$ (clause (2)), so $v=0_P(p)=0$. Second, $H_p+V_pP=T_pP$: for any $v\in T_pP$ set $\eta:=\omega_p(v)\in\mathfrak g$ and write
> > $$v=\big(v-\eta_P(p)\big)+\eta_P(p);$$
> > the second summand lies in $V_pP$, and the first lies in $H_p$ because
> > $$\omega_p\big(v-\eta_P(p)\big)=\omega_p(v)-\omega_p(\eta_P(p))=\eta-\eta=0\qquad\text{(linearity of }\omega_p\text{; clause (2) at }\eta\text{).}$$
> > Since the two subspaces meet only in $0$ and span $T_pP$, the sum is direct: $T_pP=H_p\oplus V_pP$. (Dimension check: $\dim H_p+\dim V_pP=m+\dim G=\dim T_pP$, consistent.)
> >
> > **Step 2 — invariance $dR_g(H_p)=H_{p\cdot g}$.** Let $v\in H_p$, so $\omega_p(v)=0$. Then
> > $$\omega_{p\cdot g}\big(dR_g\,v\big)=(R_g^*\omega)_p(v)=\operatorname{Ad}_{g^{-1}}\big(\omega_p(v)\big)=\operatorname{Ad}_{g^{-1}}(0)=0\qquad\text{(definition of }R_g^*\text{; clause (1); }v\in\ker\omega_p\text{),}$$
> > so $dR_g\,v\in\ker\omega_{p\cdot g}=H_{p\cdot g}$; that is, $dR_g(H_p)\subseteq H_{p\cdot g}$. Because $dR_g\colon T_pP\to T_{p\cdot g}P$ is a linear isomorphism (with inverse $dR_{g^{-1}}$) and $\dim H_p=m=\dim H_{p\cdot g}$ by Step 0, the inclusion of equal-dimensional subspaces is an equality: $dR_g(H_p)=H_{p\cdot g}$.
> >
> > Steps 0–2 show $H=\ker\omega$ is a smooth rank-$m$ distribution satisfying complementarity and invariance, i.e. a connection distribution. $\blacksquare$

> [!note]- Lemma 3: The vertical-projection form of a connection distribution is smooth
> **Statement:** Let $H\subset TP$ be a connection distribution. For $v\in T_pP$ let $v=v_H+v_V$ be its unique decomposition with $v_H\in H_p$, $v_V\in V_pP$, and define $\omega_H(v):=\iota_p^{-1}(v_V)\in\mathfrak g$. Then $\omega_H$ is a smooth $\mathfrak g$-valued $1$-form on $P$.
>
> **Hint:** Build one smooth local frame of $TP$ adapted to the splitting $H\oplus VP$; the map $v\mapsto v_V$ and then $\iota_p^{-1}$ are smooth in that frame.
>
> **Why needed:** Smoothness is exactly what makes $\Psi(H)=\omega_H$ an element of $\Omega^1(P;\mathfrak g)$; the pointwise formula alone does not give it.
>
> > [!note]- Full proof
> > **Step 0 — the vertical bundle has a global smooth frame.** Fix a basis $(\xi^1,\dots,\xi^r)$ of $\mathfrak g$, where $r=\dim G$. The fundamental fields $\sigma_a:=(\xi^a)_P$ are smooth vector fields on $P$ (the map $(p,\xi)\mapsto\xi_P(p)$ is smooth, being the differential of the smooth action), and at each $p$ the values $\sigma_1(p),\dots,\sigma_r(p)$ are the images $\iota_p(\xi^a)$ of a basis under the isomorphism $\iota_p$, hence a basis of $V_pP$. So $(\sigma_1,\dots,\sigma_r)$ is a global smooth frame of $VP$.
> >
> > **Step 1 — a smooth frame of $TP$ adapted to the splitting.** Fix $p_0\in P$. Since $H$ is a smooth distribution of rank $m$, there is an open neighbourhood $U\ni p_0$ and smooth vector fields $h_1,\dots,h_m$ on $U$ with $h_1(p),\dots,h_m(p)$ a basis of $H_p$ for every $p\in U$ (a local frame of $H$). By complementarity $T_pP=H_p\oplus V_pP$, the concatenation
> > $$\big(h_1,\dots,h_m,\ \sigma_1,\dots,\sigma_r\big)$$
> > is, at each $p\in U$, a basis of $T_pP$; being made of smooth vector fields, it is a smooth local frame of $TP$ on $U$.
> >
> > **Step 2 — the vertical projection and $\omega_H$ are smooth on $U$.** Write any smooth vector field $Y$ on $U$ in this frame:
> > $$Y=\sum_{i=1}^{m}f^i\,h_i+\sum_{a=1}^{r}b^a\,\sigma_a,$$
> > with $f^i,b^a\in C^\infty(U)$ the (smooth) coordinate functions of $Y$ relative to the smooth frame. By uniqueness of the direct-sum decomposition, at each $p$ the horizontal part of $Y(p)$ is $\sum_i f^i(p)h_i(p)\in H_p$ and the vertical part is
> > $$Y(p)_V=\sum_{a=1}^{r}b^a(p)\,\sigma_a(p)=\sum_{a=1}^{r}b^a(p)\,(\xi^a)_P(p)=\iota_p\!\Big(\sum_{a=1}^{r}b^a(p)\,\xi^a\Big).$$
> > Applying $\iota_p^{-1}$,
> > $$\omega_H(Y)(p)=\iota_p^{-1}\big(Y(p)_V\big)=\sum_{a=1}^{r}b^a(p)\,\xi^a,$$
> > a $\mathfrak g$-valued function whose coordinates in the fixed basis $(\xi^a)$ are the smooth functions $b^a$. Hence $\omega_H(Y)$ is smooth on $U$ for every smooth $Y$. As $C^\infty$-linearity of $v\mapsto\iota_p^{-1}(v_V)$ in $v$ is clear from the linearity of the projection and of $\iota_p^{-1}$, and smoothness has been shown in a neighbourhood of the arbitrary point $p_0$, the assignment $\omega_H$ is a smooth $\mathfrak g$-valued $1$-form on $P$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\pi\colon P\to M$ be a principal $G$-bundle. We must show that $\Phi(\omega)=\ker\omega$ maps connection forms to connection distributions, that $\Psi(H)=\omega_H$ maps connection distributions to connection forms, and that $\Phi$ and $\Psi$ are mutually inverse; this establishes that $\Phi$ is a bijection with inverse $\Psi$.
>
> **Step 0 — both target sets are well-posed.** On the left, $\mathcal A(P)$ is the set of $\omega\in\Omega^1(P;\mathfrak g)$ satisfying clauses (1) and (2). On the right, a *connection distribution* is a smooth subbundle $H\subset TP$ with $T_pP=H_p\oplus V_pP$ for all $p$ (complementarity) and $dR_g(H_p)=H_{p\cdot g}$ for all $p,g$ (invariance); complementarity forces $\operatorname{rank}H=\dim T_pP-\dim V_pP=(m+\dim G)-\dim G=m$. For a connection distribution $H$ the rule $\omega_H(v)=\iota_p^{-1}(v_V)$ is well-defined at each point: the decomposition $v=v_H+v_V$ is unique because the sum $H_p\oplus V_pP$ is direct, and $\iota_p^{-1}$ is a genuine map because $\iota_p\colon\mathfrak g\to V_pP$ is an isomorphism (the action is free).
>
> **Step 1 — $\Phi$ lands in connection distributions.** Let $\omega\in\mathcal A(P)$. By **Lemma 2**, $H=\ker\omega$ is a smooth rank-$m$ distribution with $T_pP=H_p\oplus V_pP$ (complementarity) and $dR_g(H_p)=H_{p\cdot g}$ (invariance). Hence $\Phi(\omega)=\ker\omega$ is a connection distribution.
>
> **Step 2 — $\Psi$ is defined and lands in connection forms.** Let $H$ be a connection distribution. By **Lemma 3**, $\omega_H$ is a smooth element of $\Omega^1(P;\mathfrak g)$, so $\Psi(H)=\omega_H$ is defined. We verify the two clauses.
>
> **Clause (2), normalisation on the vertical.** Fix $\xi\in\mathfrak g$ and $p\in P$. The vector $v=\xi_P(p)$ lies in $V_pP$, so its unique decomposition has $v_H=0$ and $v_V=\xi_P(p)=\iota_p(\xi)$. Therefore
> $$\omega_H\big(\xi_P(p)\big)=\iota_p^{-1}\big(\iota_p(\xi)\big)=\xi\qquad\text{(definition of }\omega_H\text{; }v_V=\iota_p(\xi)\text{),}$$
> which is clause (2).
>
> **Clause (1), equivariance.** Fix $g\in G$, $p\in P$, and $v\in T_pP$, and write the unique decomposition $v=v_H+\xi_P(p)$ with $v_H\in H_p$ and $\xi:=\omega_H(v)=\iota_p^{-1}(v_V)\in\mathfrak g$, so $v_V=\xi_P(p)$. Push forward by $dR_g$:
> $$dR_g\,v=dR_g\,v_H+dR_g\big(\xi_P(p)\big)=dR_g\,v_H+\big(\operatorname{Ad}_{g^{-1}}\xi\big)_P(p\cdot g)\qquad\text{(linearity of }dR_g\text{; }\textbf{Lemma 1}\text{).}$$
> Now $dR_g\,v_H\in H_{p\cdot g}$ by the **invariance** of $H$ ($dR_g(H_p)=H_{p\cdot g}$), and $(\operatorname{Ad}_{g^{-1}}\xi)_P(p\cdot g)\in V_{p\cdot g}P$ is vertical. Thus the displayed line *is* the unique horizontal–vertical decomposition of $dR_g\,v$ at the point $p\cdot g$, with vertical part $(\operatorname{Ad}_{g^{-1}}\xi)_P(p\cdot g)=\iota_{p\cdot g}(\operatorname{Ad}_{g^{-1}}\xi)$. Reading off the vertical label,
> $$(R_g^*\omega_H)_p(v)=\omega_{H,\,p\cdot g}\big(dR_g\,v\big)=\iota_{p\cdot g}^{-1}\Big(\iota_{p\cdot g}(\operatorname{Ad}_{g^{-1}}\xi)\Big)=\operatorname{Ad}_{g^{-1}}\xi=\operatorname{Ad}_{g^{-1}}\big(\omega_{H,\,p}(v)\big),$$
> using the definition of $R_g^*$, the definition of $\omega_H$ at $p\cdot g$, and $\xi=\omega_{H,p}(v)$. As $p$ and $v$ were arbitrary, $R_g^*\omega_H=\operatorname{Ad}_{g^{-1}}\omega_H$, which is clause (1). Hence $\omega_H\in\mathcal A(P)$.
>
> **Step 3 — $\Phi\circ\Psi=\operatorname{id}$.** Let $H$ be a connection distribution and $\omega_H=\Psi(H)$. For $v\in T_pP$ with decomposition $v=v_H+v_V$,
> $$\omega_H(v)=0\iff \iota_p^{-1}(v_V)=0\iff v_V=0\iff v=v_H\in H_p\qquad\text{(definition of }\omega_H\text{; }\iota_p\text{ injective; uniqueness of the decomposition).}$$
> Therefore $\ker\omega_{H,p}=H_p$ for every $p$, i.e. $\Phi(\Psi(H))=\ker\omega_H=H$.
>
> **Step 4 — $\Psi\circ\Phi=\operatorname{id}$.** Let $\omega\in\mathcal A(P)$, put $H=\Phi(\omega)=\ker\omega$ (a connection distribution by Step 1), and form $\omega_H=\Psi(H)$. Fix $p$ and $v\in T_pP$, and let $v=v_H+v_V$ be the decomposition relative to this **same** $H=\ker\omega$, with $v_V=\iota_p(\eta)=\eta_P(p)$ where $\eta:=\iota_p^{-1}(v_V)$. Then on one hand $\omega_H(v)=\eta$ by definition of $\omega_H$. On the other hand, applying $\omega$ to the decomposition,
> $$\omega(v)=\omega(v_H)+\omega(\eta_P(p))=0+\eta=\eta\qquad\text{(}v_H\in H_p=\ker\omega\text{; clause (2) for }\omega\text{ at }\eta\text{).}$$
> Hence $\omega_H(v)=\eta=\omega(v)$ for all $p,v$, i.e. $\Psi(\Phi(\omega))=\omega_H=\omega$.
>
> **Conclusion.** Steps 1 and 2 show $\Phi$ and $\Psi$ are well-defined maps between $\mathcal A(P)$ and the set of connection distributions; Steps 3 and 4 show $\Phi\circ\Psi=\operatorname{id}$ and $\Psi\circ\Phi=\operatorname{id}$. Therefore $\Phi\colon\omega\mapsto\ker\omega$ is a bijection with inverse $\Psi\colon H\mapsto\omega_H$, and connection forms correspond exactly to smooth $G$-invariant horizontal distributions. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian submersions and the horizontal distribution of a metric.** Let $\pi\colon(P,g_P)\to(M,g_M)$ be a Riemannian submersion with a free isometric $G$-action whose orbits are the fibres. The orthogonal complement $H_p:=(V_pP)^{\perp}$ of the vertical subspace is smooth (orthogonal complement of a smooth subbundle with respect to a smooth metric) and $G$-invariant (the $G$-action is by isometries, so it preserves orthogonality). The theorem then produces a connection form $\omega_H$ whose horizontal distribution is the metric complement. The application is non-obvious because the input mentions no differential form at all — only a metric — yet a canonical connection falls out; this is exactly the mechanism behind the Levi-Civita connection viewed on the orthonormal frame bundle and behind the standard connection on the Hopf bundle.

**Ehresmann connections on general fibre bundles.** For a fibre bundle $F\to E\xrightarrow{\pi}M$ without a group action, an Ehresmann connection is defined directly as a smooth complement $H_p$ to the vertical bundle $\ker d\pi$, with no invariance condition available. Comparing with this theorem isolates precisely what the principal structure adds: the extra clause (2) invariance, which is what lets the connection be encoded by a single $\mathfrak g$-valued form rather than by the raw distribution. The exercise is to state which parts of the correspondence survive without a group (the pointwise splitting and the vertical projection) and which do not (the $\operatorname{Ad}_{g^{-1}}$-equivariance and the $\mathfrak g$-valued form), sharpening one's sense of the role of equivariance.

**Distributions and integrability, via Frobenius.** Take a connection distribution $H$ and ask when it is integrable. By [[Thm - The Frobenius Theorem|Frobenius's theorem]], $H$ is integrable if and only if $[\Gamma(H),\Gamma(H)]\subseteq\Gamma(H)$, and one computes that the obstruction is the vertical part of $[\tilde X,\tilde Y]$ for horizontal lifts, which the [[Def - Curvature of a Principal Connection|curvature]] measures. The exercise — build an explicit non-integrable connection distribution (the horizontal distribution of the Hopf connection on $S^3\to S^2$, where two horizontal fields have vertical bracket) and confirm through the correspondence that its connection form has nonzero curvature — ties the geometric side of this theorem to the analytic definition of curvature, and shows the two views of a connection meeting on a concrete example.

---

# Bridges

- **[[Def - Connection on a Principal Bundle|Connection on a principal bundle]]** — the form side. That page defines $\omega$ by clauses (1) and (2) and lists the horizontal distribution $H=\ker\omega$ as one of a connection's three faces; the present theorem is the proof that the "form" face and the "distribution" face determine each other, so that the language may be switched freely. The corollary on that page (the fundamental-field transformation law, and the consistency of the two clauses) supplies the same identity used here as Lemma 1.

- **[[Def - Horizontal Subspace and Horizontal Lift|Horizontal subspace and horizontal lift]]** — the distribution side. There $H_p=\ker\omega_p$ is introduced from a given $\omega$, and the horizontal lift $\tilde v\in H_p$ of $v\in T_{\pi(p)}M$ is built from the isomorphism $d\pi_p|_{H_p}\colon H_p\xrightarrow{\sim}T_{\pi(p)}M$. The present theorem guarantees that *every* smooth invariant complement, however it is produced, is the horizontal subspace of a genuine connection, so the lift construction applies to distributions specified without reference to any form.

- **[[Thm - Existence of Connections on Principal Bundles|Existence of connections]]** — the same content on the geometric side. That theorem builds a connection form by patching product connections with a partition of unity; through $\Phi$ this reads as patching the flat complements $T_mM\times\{0\}$ into a smooth invariant distribution, and the affine structure of $\mathcal A(P)$ transports to the connection distributions. The correspondence is what makes "there exists an invariant complement" and "there exists a connection form" interchangeable statements.

- **[[Thm - The Frobenius Theorem|The Frobenius theorem]]** — the integrability partner. Once a connection is a smooth distribution, Frobenius decides when it is a foliation; a connection distribution is integrable exactly when its curvature vanishes, which is the geometric picture of a flat connection. The bridge is that a purely analytic object (the curvature $2$-form) governs a purely geometric question (integrating a plane field), and the correspondence theorem is the translation dictionary between them.

- **[[Def - Distribution on a Manifold|Distribution on a manifold]]** — the ambient notion. The right-hand objects of the bijection are ordinary smooth distributions (subbundles of $TP$) carrying two extra properties. Recognising a connection as a special distribution places gauge theory inside the general theory of plane fields on manifolds and makes the tools of that theory — frames, defining forms, integrability — available to connections.

---

# Unlocked by This

> [!tip] Flat connections as foliations *(from this chapter and Gauge Theory V)*
> Because a connection is now a smooth invariant distribution, one may ask when it is integrable. The [[Def - Curvature of a Principal Connection|curvature]] is the obstruction, and a flat connection ($\Omega=0$) is exactly one whose horizontal distribution foliates $P$ transversely to the fibres. This is the geometric foundation of the holonomy classification of flat bundles developed in the next chapter.

> [!tip] Building connections from geometry *(from Riemannian geometry)*
> Any $G$-invariant smooth field of complements to the fibres — an orthogonal complement for an invariant metric, the image of an equivariant horizontal lift, a reduction-of-structure-group splitting — is now known to be a connection. One constructs connections geometrically and reads off $\omega$, rather than writing down a $\mathfrak g$-valued form and checking two clauses by hand.
