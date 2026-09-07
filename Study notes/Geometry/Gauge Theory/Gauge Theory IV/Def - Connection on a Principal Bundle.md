---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Fundamental Vector Field of a Group Action"
  - "Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
  - "Def - Equivariant and Basic Forms on a Principal Bundle"
  - "Def - The Maurer-Cartan Form"
  - "Def - Adjoint Bundles ad P and Ad P"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a smooth **[[Def - Principal G-Bundle|principal G-bundle]]**: a smooth manifold $P$ carrying a smooth free right action of a Lie group $G$, written $R_g(p)=p\cdot g$, whose orbits are exactly the fibres of $\pi$ and which is locally trivial. The action being free and fibre-transitive means each fibre $P_b=\pi^{-1}(b)$ is a single orbit and the **orbit map** $\ell_p\colon G\to P$, $\ell_p(a)=p\cdot a$, is a diffeomorphism onto the fibre through $p$.

We write $\mathfrak g=T_eG$ for the Lie algebra of $G$, with the bracket of left-invariant vector fields; for a matrix group this is the commutator $[\,X,Y]=XY-YX$. The **group adjoint** is $\operatorname{Ad}_g=d_e(a\mapsto gag^{-1})\colon\mathfrak g\to\mathfrak g$, a Lie-algebra automorphism, and for a matrix group $\operatorname{Ad}_g X=gXg^{-1}$; the **algebra adjoint** is $\operatorname{ad}_X Y=[\,X,Y]$. These are two different maps and we never abbreviate one as the other. The relevant translations are recorded on [[Def - Left and Right Translations and Conjugation on a Lie Group|the page on translations and conjugation on a Lie group]].

For each $\xi\in\mathfrak g$ the **[[Def - Fundamental Vector Field of a Group Action|fundamental vector field]]** of $\xi$ on $P$ is
$$\xi_P(p):=\frac{d}{dt}\Big|_{t=0}\,p\cdot\exp(t\xi)=d_e\ell_p(\xi)\in T_pP,$$
the velocity of the orbit through $p$ in the direction $\xi$. Because the action is free, at each $p$ the linear map $\xi\mapsto\xi_P(p)$ is injective with image the **vertical subspace**
$$V_pP:=\ker(d\pi_p)=\{\xi_P(p):\xi\in\mathfrak g\},$$
so $\xi\mapsto\xi_P(p)$ is a linear isomorphism $\mathfrak g\xrightarrow{\ \sim\ }V_pP$; every vector tangent to a fibre is $\xi_P(p)$ for exactly one $\xi\in\mathfrak g$. The map $\xi\mapsto\xi_P$ is moreover a homomorphism from $\mathfrak g$ into the vector fields on $P$, as established on [[Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions|the fundamental-field homomorphism page]]. A tangent vector is called **vertical** if it lies in $V_pP$; the collection $VP=\bigsqcup_p V_pP=\ker d\pi$ is the **vertical bundle**.

We work with **[[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|𝔤-valued differential forms]]**: $\Omega^1(P;\mathfrak g)=\Gamma(T^*P\otimes\mathfrak g)$ is the space of smooth $1$-forms on $P$ with values in $\mathfrak g$. For a smooth map $\varphi$ and a $\mathfrak g$-valued form $\alpha$, the pullback $\varphi^*\alpha$ is taken component-by-component, and for a fixed linear map $L\colon\mathfrak g\to\mathfrak g$ we write $L\alpha$ for the form $(L\alpha)(v)=L(\alpha(v))$; a fixed $L$ commutes with pullback, $\varphi^*(L\alpha)=L(\varphi^*\alpha)$, because $L$ does not depend on the point.

The **[[Def - The Maurer-Cartan Form|Maurer–Cartan form]]** of $G$ is $\theta\in\Omega^1(G;\mathfrak g)$, $\theta_g=d_gL_{g^{-1}}\colon T_gG\to\mathfrak g$; for a matrix group $\theta=g^{-1}\,dg$. Two of its properties are used below and proved on its page: it satisfies $\theta(\widetilde\xi)=\xi$ for the left-invariant field $\widetilde\xi(g)=d_eL_g(\xi)$, and it transforms under right translation by $R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta$.

The **[[Def - Adjoint Bundles ad P and Ad P|adjoint bundle]]** is $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$, the vector bundle over $M$ associated with $P$ through the adjoint representation $\operatorname{Ad}\colon G\to GL(\mathfrak g)$. A form is **[[Def - Equivariant and Basic Forms on a Principal Bundle|equivariant]]** (of adjoint type) if $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$, and **basic** if it vanishes whenever one argument is vertical.

> [!warning] Convention: connection form and the group adjoint
> Two source conventions must be reconciled. First, Bär's Definition 2.3.1 prints condition 1 as "$R_g^*=\operatorname{Ad}_{g^{-1}}\circ\omega$": the symbol $\omega$ has dropped off the left-hand side. The intended and correct statement is $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$, an equality of $\mathfrak g$-valued $1$-forms on $P$; we use this corrected form throughout. Second, Haydys writes $a$ for the connection form and, more consequentially, writes $\operatorname{ad}_g$ for what we and Bär call $\operatorname{Ad}_g$ (the group adjoint), reserving no separate symbol for the group adjoint. In this series $\operatorname{Ad}_g$ is always the group adjoint $d_e(a\mapsto gag^{-1})$ and $\operatorname{ad}_X$ is always the algebra adjoint $[\,X,\cdot\,]$; a reader translating from Haydys should read every $\operatorname{ad}_g$ (subscript a group element) there as $\operatorname{Ad}_g$ here.

---

# Axiom Motivation

We are handed a principal bundle $\pi\colon P\to M$ and we want to differentiate: to compare values of a section over nearby points of $M$, to transport data along a curve, to build a covariant derivative on every bundle associated with $P$. On a vector bundle this is done by a **[[Def - Connection on a Vector Bundle|covariant derivative]]** $\nabla$, a rule for differentiating sections that obeys the Leibniz law. A principal bundle has no linear structure in its fibres — the fibres are group orbits, not vector spaces — so there is nothing to add and no Leibniz law to impose directly. We must find the right substitute, and the point of this definition is that the substitute is forced.

The forcing comes from a structural asymmetry between the two kinds of directions in $P$. The **vertical** directions, those tangent to the fibres, are already fully understood: the fundamental-field isomorphism $\xi\mapsto\xi_P(p)$ identifies $V_pP$ with the fixed vector space $\mathfrak g$, canonically and at every point. What is missing is a notion of **horizontal**: at each $p$ a complement $H_p$ to $V_pP$ inside $T_pP$, telling us which infinitesimal motions "go somewhere new in $M$" rather than "slide along the fibre." A choice of such complements is exactly a way to lift a tangent vector on $M$ to a canonical tangent vector on $P$, hence a way to transport and to differentiate. The whole content of a connection is a compatible, group-respecting choice of horizontal directions.

There are two equivalent ways to package the datum. One is to give the distribution $H=\{H_p\}$ directly. The other, which is what we take as the primary definition, is to give the $\mathfrak g$-valued $1$-form $\omega$ that measures the vertical part of a tangent vector, read off in $\mathfrak g$ through the fundamental-field identification. If $v\in T_pP$ decomposes as (horizontal part) $+$ (vertical part), and the vertical part equals $\xi_P(p)$ for a unique $\xi\in\mathfrak g$, then $\omega_p(v):=\xi$. Its kernel is then the horizontal distribution, $H_p=\ker\omega_p$, and the two packagings carry the same information. The form is the more convenient object because it is an ordinary differential form, on which the exterior derivative, pullback, and the bracket of $\mathfrak g$-valued forms all act; the distribution is the more geometric object. We can now read off exactly which two conditions the form must satisfy.

The first condition is that $\omega$ genuinely reads off the vertical part in $\mathfrak g$, which means it must act as the identity on vertical vectors after the fundamental-field identification:
$$\omega(\xi_P)=\xi\qquad\text{for all }\xi\in\mathfrak g.$$
This is a **normalisation**: it fixes $\omega$ completely on the vertical subspace and forces $\omega_p|_{V_pP}\colon V_pP\to\mathfrak g$ to be the inverse of $\xi\mapsto\xi_P(p)$, in particular an isomorphism, so that $\ker\omega_p$ is a genuine complement to $V_pP$ of dimension $\dim M$.

**What breaks if we drop the normalisation (2).** Without it the zero form $\omega=0$ would qualify, since it trivially satisfies the equivariance condition below ($R_g^*0=0=\operatorname{Ad}_{g^{-1}}0$). But $\ker 0=T_pP$ is not a complement to the vertical subspace; it defines no horizontal directions and no lift. The normalisation is precisely what excludes this degenerate case, and it is the reason the set of connections is **not** a vector space: the natural candidate for a zero element already fails to be a connection. A second reading of the same point: an object satisfying only equivariance is a general $\mathfrak g$-valued equivariant $1$-form, of which there are many that carry no horizontal information; clause (2) selects, among these, the ones that split off the vertical part exactly.

The second condition is that the choice must respect the group. The group $G$ acts on $P$ by $R_g$, hence on tangent vectors by $dR_g$ and on forms by pullback; a construction on $P$ is only geometrically meaningful — only descends to statements about $M$ — if it is equivariant. The correct equivariance for a connection form is
$$R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega\qquad\text{for all }g\in G,$$
that is, moving a vector by $dR_g$ and then applying $\omega$ is the same as applying $\omega$ first and then rotating the answer in $\mathfrak g$ by $\operatorname{Ad}_{g^{-1}}$.

**What breaks if we drop the equivariance (1).** Using a partition of unity one can choose, at each point of $P$, *some* complement $H_p$ to $V_pP$, smoothly but with no relation between $H_p$ and $H_{p\cdot g}$; the associated form (vanishing on $H$, inverse of $\xi\mapsto\xi_P$ on the vertical) then satisfies (2) but not (1). The horizontal lift such a form defines does not commute with the group action, so parallel transport around the fibre is inconsistent, and — the decisive failure — the curvature and the connection's local data do not glue to global objects on $M$. A concrete witness appears among the examples below: on $M\times SU(2)$ the form $\operatorname{pr}_2^*\theta+\pi^*\alpha$ with $\alpha\neq 0$ satisfies (2) but violates (1), and is exactly the kind of non-equivariant complement just described.

Finally, one might ask why the equivariance is $\operatorname{Ad}_{g^{-1}}$ and not, say, $\operatorname{Ad}_g$. This is not a free choice: it is forced by clause (2) together with how $dR_g$ moves vertical vectors, and the two clauses are consistent for exactly this factor and inconsistent for $\operatorname{Ad}_g$. That computation is the corollary proved below. The reader who has followed the last four paragraphs has, in effect, invented the definition: encode an equivariant horizontal complement as a $\mathfrak g$-valued $1$-form, normalise it on the vertical directions, and require it to intertwine the group action with the adjoint action on $\mathfrak g$.

---

# The Definition

Let $\pi\colon P\to M$ be a principal $G$-bundle. A **connection form** (or **principal connection**, or simply a **connection**) on $P$ is a $\mathfrak g$-valued $1$-form
$$\omega\in\Omega^1(P;\mathfrak g)$$
satisfying the two conditions:

1. **Equivariance (adjoint type).** For every $g\in G$,
$$R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega,$$
an equality of $\mathfrak g$-valued $1$-forms on $P$; equivalently, for every $p\in P$ and $v\in T_pP$, $\ \omega_{p\cdot g}(dR_g\,v)=\operatorname{Ad}_{g^{-1}}\big(\omega_p(v)\big)$.

2. **Normalisation on the vertical.** For every $\xi\in\mathfrak g$,
$$\omega(\xi_P)=\xi,$$
that is, $\omega_p(\xi_P(p))=\xi$ for all $p\in P$; since every vertical vector is $\xi_P(p)$ for a unique $\xi$, this determines $\omega$ on the vertical subspace $V_pP$ and identifies $\omega_p|_{V_pP}$ with the inverse of $\xi\mapsto\xi_P(p)$.

The **space of connections** on $P$ is
$$\mathcal A(P):=\{\omega\in\Omega^1(P;\mathfrak g):\omega\text{ satisfies }(1)\text{ and }(2)\},$$
denoted $\mathcal C(P)$ by Bär. It is **not a vector space**: the zero form fails condition (2) (it sends every $\xi_P$ to $0\neq\xi$), so $0\notin\mathcal A(P)$. It is instead an affine space modelled on $\Omega^1(M;\operatorname{ad}P)$ — the difference of two connections is a basic equivariant $\mathfrak g$-valued $1$-form and so descends to an $\operatorname{ad}P$-valued $1$-form on $M$, and conversely every such form added to a connection gives a connection. That $\mathcal A(P)$ is non-empty and affine is the content of the **[[Thm - Existence of Connections on Principal Bundles|existence theorem]]**; the difference statement is verified in the corollary below and again there.

The horizontal packaging of the same datum is $H_p:=\ker\omega_p$, developed on [[Def - Horizontal Subspace and Horizontal Lift|the horizontal-subspace page]]; the equivalence of the two packagings is [[Thm - Connection Forms Correspond to Invariant Horizontal Distributions|the correspondence theorem]].

---

# Categorical / Structural Definition

The definition has a clean reading as the splitting of a short exact sequence of vector bundles over $P$, equivariant for the group. The vertical bundle $VP=\ker d\pi$ is canonically trivialised,
$$P\times\mathfrak g\xrightarrow{\ \sim\ }VP,\qquad (p,\xi)\longmapsto\xi_P(p),$$
because the action is free. The differential of $\pi$ gives a surjection $d\pi\colon TP\to\pi^*TM$ onto the pullback bundle $\pi^*TM$ (whose fibre at $p$ is $T_{\pi(p)}M$), with kernel exactly $VP$. Thus there is a short exact sequence of vector bundles over $P$,
$$0\longrightarrow VP\longrightarrow TP\xrightarrow{\ d\pi\ }\pi^*TM\longrightarrow 0.$$
The group $G$ acts on all three bundles: on $TP$ by $dR_g$, on $VP$ by restriction (equivalently on $P\times\mathfrak g$ by $(p,\xi)\mapsto(p\cdot g,\operatorname{Ad}_{g^{-1}}\xi)$, matching the fundamental-field transformation proved in the corollary below), and on $\pi^*TM$ by the identity on $T_{\pi(p)}M$ over the moved base point.

A **connection is a $G$-equivariant left splitting** of this sequence: a bundle map $\lambda\colon TP\to VP\cong P\times\mathfrak g$ restricting to the identity on $VP$ and intertwining the $G$-actions. Post-composing with the projection $P\times\mathfrak g\to\mathfrak g$ turns $\lambda$ into a $\mathfrak g$-valued $1$-form; that this form is our $\omega$ is exactly clauses (1) and (2): "restricts to the identity on $VP$" is the normalisation (2), and "intertwines the $G$-actions" is the equivariance (1) with $G$ acting on the target $\mathfrak g$ by $\operatorname{Ad}$. Dually, a connection is a $G$-equivariant right splitting $\sigma\colon\pi^*TM\to TP$ with $d\pi\circ\sigma=\operatorname{id}$; its image is the horizontal distribution $H=\ker\omega$ and $\sigma$ is the horizontal lift. The two splittings determine each other by $\lambda=\operatorname{id}-\sigma\circ d\pi$, so a connection is one datum with three faces: the form, the horizontal distribution, and the lift. This is the sense in which "a connection is a compatible choice of horizontal directions" is not a metaphor but a splitting in the category of $G$-equivariant vector bundles over $P$.

---

# Relate to Other Fields / Compression

**True name.** The official definition is a $\mathfrak g$-valued $1$-form with two clauses, but the operational object is a *field of horizontal complements, equivariant under the group*. Everything one does with a connection — lift a vector, transport a section, measure curvature — is done through $H=\ker\omega$ and the lift; the form is bookkeeping that makes the exterior calculus available. This is why the same connection appears in three guises (form, distribution, lift) and why the sign and factor conventions all live in how $\omega$ interacts with $\theta$ and the bracket rather than in the geometry itself.

**Relation to vector-bundle connections.** A covariant derivative $\nabla$ on a vector bundle $E\to M$ and a principal connection $\omega$ on its **[[Def - Frame Bundle of a Vector Bundle|frame bundle]]** $\operatorname{Fr}(E)$ are the same datum in two languages: $e^*\omega$ is the connection matrix $A(\nabla,e)$ for every local frame $e$, and the correspondence $\nabla\leftrightarrow\omega$ is a bijection. More generally, for any representation $\rho\colon G\to GL(V)$ a principal connection $\omega$ on $P$ induces a covariant derivative on the associated bundle $P\times_\rho V$, the connection form entering through its differential $\rho_*\colon\mathfrak g\to\operatorname{End}(V)$ so that a $\mathfrak g$-valued $\omega$ becomes $\operatorname{End}(V)$-valued when it acts on $V$. These are the two halves of the equivalence proved on [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle|the frame-bundle theorem]] and [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|the associated-bundle theorem]]; the point of moving to the principal bundle is that **one** connection $\omega$ simultaneously differentiates every associated bundle, whereas $\nabla$ lives on one $E$ at a time.

**The physicists' gauge potential.** Choosing a local section $s\colon U\to P$ (a *local gauge*) and pulling back, $A_s:=s^*\omega\in\Omega^1(U;\mathfrak g)$, gives the gauge potential $A=A_\mu\,dx^\mu$ of physics; the connection is the geometric object of which the vector potential of electromagnetism and the gauge fields of Yang–Mills theory are local coordinate expressions. This is developed on [[Def - Local Connection Form and Gauge Potential|the local-connection-form page]]. The freedom to change $s$ is the gauge freedom, and the way $A_s$ changes is governed by the Maurer–Cartan form $\theta$.

**Compression across the vault.** The pattern "differentiate by choosing an equivariant horizontal complement to a canonical vertical" is the principal-bundle instance of a recurring construction: an Ehresmann connection on a general fibre bundle chooses a horizontal complement without any equivariance; a Cartan connection adds a coframing; a covariant derivative is the associated-bundle shadow. In each case the vertical directions are given and the connection supplies the horizontal ones.

---

# Examples / Corollaries

**Corollary — the two conditions are consistent, and $\operatorname{Ad}_{g^{-1}}$ is forced.** *We claim that a form can satisfy (1) and (2) simultaneously, and that replacing $\operatorname{Ad}_{g^{-1}}$ by $\operatorname{Ad}_g$ in (1) would be incompatible with (2).* The whole point is a single identity about how $dR_g$ moves a vertical vector.

> [!note]- Proof of the corollary (with the fundamental-field transformation proved inline)
> **Step 0 — the fundamental-field transformation law.** We first show
> $$dR_g\big(\xi_P(p)\big)=\big(\operatorname{Ad}_{g^{-1}}\xi\big)_P(p\cdot g)\qquad\text{for all }p\in P,\ g\in G,\ \xi\in\mathfrak g.\tag{$\ast$}$$
> Recall the orbit map $\ell_p\colon G\to P$, $\ell_p(a)=p\cdot a$, so that $\xi_P(p)=d_e\ell_p(\xi)$ (definition of the fundamental field). Compute the composite $R_g\circ\ell_p$ on a group element $a$:
> $$(R_g\circ\ell_p)(a)=p\cdot a\cdot g=p\cdot g\cdot(g^{-1}a g)=\ell_{p\cdot g}\big(C_{g^{-1}}(a)\big)\qquad\text{(associativity of the action; }C_{g^{-1}}(a):=g^{-1}ag\text{),}$$
> so $R_g\circ\ell_p=\ell_{p\cdot g}\circ C_{g^{-1}}$ as maps $G\to P$. Differentiating at $a=e$ (chain rule), and using $C_{g^{-1}}(e)=e$ so that $d_eC_{g^{-1}}\colon\mathfrak g\to\mathfrak g$,
> $$dR_g\circ d_e\ell_p=d_e\ell_{p\cdot g}\circ d_eC_{g^{-1}}\qquad\text{(chain rule applied to both sides).}$$
> By the very definition of the group adjoint, $d_eC_{g^{-1}}=\operatorname{Ad}_{g^{-1}}$ (the adjoint is the differential at $e$ of conjugation, here by $g^{-1}$). Applying both sides to $\xi\in\mathfrak g$ and using $d_e\ell_q(\eta)=\eta_P(q)$ for any $q$,
> $$dR_g\big(\xi_P(p)\big)=d_e\ell_{p\cdot g}\big(\operatorname{Ad}_{g^{-1}}\xi\big)=\big(\operatorname{Ad}_{g^{-1}}\xi\big)_P(p\cdot g),$$
> which is $(\ast)$. (For a matrix group this is Bär's one-line computation $dR_g(dL_pX)=\tfrac{d}{dt}\big|_0\,p\exp(tX)g=\tfrac{d}{dt}\big|_0\,pg\,g^{-1}\exp(tX)g=dL_{pg}(\operatorname{Ad}_{g^{-1}}X)$.)
>
> **Consistency.** Suppose $\omega$ satisfies (2). Evaluate its equivariance requirement on a vertical vector $\xi_P(p)$. On one hand, if $\omega$ satisfies (1) then
> $$\omega_{p\cdot g}\big(dR_g\,\xi_P(p)\big)=\operatorname{Ad}_{g^{-1}}\big(\omega_p(\xi_P(p))\big)=\operatorname{Ad}_{g^{-1}}\xi\qquad\text{(by (1), then by (2)).}$$
> On the other hand, using $(\ast)$ and then (2) at the point $p\cdot g$,
> $$\omega_{p\cdot g}\big(dR_g\,\xi_P(p)\big)=\omega_{p\cdot g}\big((\operatorname{Ad}_{g^{-1}}\xi)_P(p\cdot g)\big)=\operatorname{Ad}_{g^{-1}}\xi\qquad\text{(by }(\ast)\text{, then by (2) with }\operatorname{Ad}_{g^{-1}}\xi\in\mathfrak g\text{).}$$
> The two computations agree: on vertical vectors, the equivariance demanded by (1) is *automatically* the value forced by $(\ast)$ and (2). Hence (1) and (2) impose no contradiction on the vertical subspace, and on the horizontal complement (1) is a free equivariance requirement that any $G$-invariant choice of complement satisfies; a form satisfying both exists (the [[Thm - Existence of Connections on Principal Bundles|existence theorem]] constructs one).
>
> **Why $\operatorname{Ad}_g$ would fail.** Suppose instead we demanded $R_g^*\omega=\operatorname{Ad}_g\,\omega$ together with (2). Repeating the vertical computation, (2) and $(\ast)$ still force
> $$\omega_{p\cdot g}\big(dR_g\,\xi_P(p)\big)=\operatorname{Ad}_{g^{-1}}\xi\qquad\text{(by }(\ast)\text{ and (2), independent of which equivariance we posit),}$$
> whereas the hypothetical equivariance would require this to equal $\operatorname{Ad}_g\big(\omega_p(\xi_P(p))\big)=\operatorname{Ad}_g\xi$. Thus we would need $\operatorname{Ad}_{g^{-1}}\xi=\operatorname{Ad}_g\xi$ for all $\xi\in\mathfrak g$ and all $g\in G$, i.e. $\operatorname{Ad}_{g^2}=\operatorname{id}$ for every $g$. This fails already for $G=SU(2)$: taking $g=\exp(\tfrac{\pi}{2}X)$ for a nonzero $X\in\mathfrak{su}(2)$ makes $\operatorname{Ad}_{g^2}=\operatorname{Ad}_{\exp(\pi X)}\neq\operatorname{id}$ (the adjoint action of $SU(2)$ on $\mathfrak{su}(2)\cong\mathbb R^3$ is rotation by twice the angle, nontrivial here). Naming the contradiction: the assumption $R_g^*\omega=\operatorname{Ad}_g\omega$ contradicts the forced value $(\ast)$ on the vertical vector $\xi_P(p)$. Therefore $\operatorname{Ad}_{g^{-1}}$, not $\operatorname{Ad}_g$, is the only equivariance compatible with the normalisation. $\blacksquare$

**Is an instance — the product connection $\operatorname{pr}_2^*\theta$ on $M\times G$.** Let $P=M\times G$ be the trivial bundle with $\pi=\operatorname{pr}_1$ and right action $(m,g)\cdot h=(m,gh)$, so $\operatorname{pr}_2\colon M\times G\to G$ is the second projection. Set
$$\omega:=\operatorname{pr}_2^*\theta\in\Omega^1(M\times G;\mathfrak g),$$
the pullback of the Maurer–Cartan form. We verify both clauses.

> [!note]- Verification of the product connection, clause by clause
> **The fundamental field.** For $\xi\in\mathfrak g$,
> $$\xi_P(m,g)=\frac{d}{dt}\Big|_{0}(m,g\exp(t\xi))=\Big(0_m,\ \tfrac{d}{dt}\big|_0 g\exp(t\xi)\Big)=\big(0_m,\ \widetilde\xi(g)\big)\qquad\text{(the action fixes the }M\text{-factor; }\widetilde\xi(g)=d_eL_g(\xi)\text{),}$$
> where $\widetilde\xi$ is the left-invariant field. Hence $d\operatorname{pr}_2\big(\xi_P(m,g)\big)=\widetilde\xi(g)$.
>
> **Clause (2).** For any $\xi$,
> $$\omega\big(\xi_P(m,g)\big)=(\operatorname{pr}_2^*\theta)\big(\xi_P(m,g)\big)=\theta_g\big(d\operatorname{pr}_2\,\xi_P(m,g)\big)=\theta_g\big(\widetilde\xi(g)\big)=\xi\qquad\text{(definition of pullback; previous line; then }\theta(\widetilde\xi)=\xi\text{).}$$
> So $\omega(\xi_P)=\xi$. $\checkmark$
>
> **Clause (1).** The right action commutes with the second projection, $\operatorname{pr}_2\circ R_h=R_h^G\circ\operatorname{pr}_2$ (where $R_h^G$ is right translation on $G$), because $(m,g)\cdot h=(m,gh)$. Therefore
> $$R_h^*\omega=R_h^*\operatorname{pr}_2^*\theta=\operatorname{pr}_2^*\big((R_h^G)^*\theta\big)=\operatorname{pr}_2^*\big(\operatorname{Ad}_{h^{-1}}\theta\big)=\operatorname{Ad}_{h^{-1}}\big(\operatorname{pr}_2^*\theta\big)=\operatorname{Ad}_{h^{-1}}\omega,$$
> where the second equality is functoriality of pullback, the third is the Maurer–Cartan transformation law $(R_h^G)^*\theta=\operatorname{Ad}_{h^{-1}}\theta$, and the fourth is that the fixed linear map $\operatorname{Ad}_{h^{-1}}$ commutes with pullback. So $R_h^*\omega=\operatorname{Ad}_{h^{-1}}\omega$. $\checkmark$
>
> Both clauses hold, so $\operatorname{pr}_2^*\theta\in\mathcal A(M\times G)$. Its horizontal distribution is $H_{(m,g)}=\ker\omega_{(m,g)}=T_mM\times\{0\}$ (the vectors with no $G$-component), the "flat" horizontal directions; this is the product (or canonical flat) connection.

**Is an instance — the standard connection on the Hopf bundle.** On the Hopf fibration $S^{2n+1}\to\mathbb{CP}^n$ with $G=U(1)$, $\mathfrak u(1)=i\mathbb R$, and fundamental field $v(z)=iz$ of $i\in\mathfrak u(1)$, the form $a_z(u)=\langle v(z),u\rangle\,i$ (with $\langle\cdot,\cdot\rangle$ the real inner product of $\mathbb R^{2n+2}$) is a connection; it is verified clause by clause, and shown to be the unique connection with $\ker a=v^\perp$, on [[Thm - The Standard Connection on the Hopf Bundle|the Hopf-connection page]]. The key simplification is that $U(1)$ is abelian, so $\operatorname{Ad}\equiv\operatorname{id}$ and clause (1) reduces to ordinary invariance $R_h^*a=a$, which holds because $U(1)$ acts by isometries.

**Is NOT an instance in general — $\operatorname{pr}_2^*\theta+\pi^*\alpha$.** On $M\times G$ take
$$\omega_\alpha:=\operatorname{pr}_2^*\theta+\pi^*\alpha,\qquad \alpha\in\Omega^1(M;\mathfrak g),\ \pi=\operatorname{pr}_1.$$
This satisfies (2) for every $\alpha$, but satisfies (1) — hence is a connection — **if and only if** $\alpha$ takes values pointwise in the $\operatorname{Ad}$-invariant part of $\mathfrak g$, that is, in the centre $\mathfrak z(\mathfrak g)$.

> [!note]- Verification of the non-example, both clauses and the two cases
> **Clause (2) always holds.** The form $\pi^*\alpha$ is basic: for a vertical vector $\xi_P(m,g)=(0_m,\widetilde\xi(g))$ we have $d\pi\,\xi_P=d\operatorname{pr}_1(0_m,\widetilde\xi(g))=0$, so $(\pi^*\alpha)(\xi_P)=\alpha(d\pi\,\xi_P)=0$. Hence
> $$\omega_\alpha(\xi_P)=(\operatorname{pr}_2^*\theta)(\xi_P)+(\pi^*\alpha)(\xi_P)=\xi+0=\xi\qquad\text{(clause (2) for }\operatorname{pr}_2^*\theta\text{ shown above; }\pi^*\alpha\text{ basic).}$$
> So (2) holds for every $\alpha$. $\checkmark$
>
> **Clause (1) is a condition on $\alpha$.** The base projection is unchanged by the action, $\pi\circ R_h=\pi$, so $R_h^*\pi^*\alpha=\pi^*\alpha$. Combining with the product-connection computation,
> $$R_h^*\omega_\alpha=R_h^*\operatorname{pr}_2^*\theta+R_h^*\pi^*\alpha=\operatorname{Ad}_{h^{-1}}\operatorname{pr}_2^*\theta+\pi^*\alpha\qquad\text{(clause (1) for }\operatorname{pr}_2^*\theta\text{; }R_h^*\pi^*\alpha=\pi^*\alpha\text{).}$$
> The requirement $R_h^*\omega_\alpha=\operatorname{Ad}_{h^{-1}}\omega_\alpha=\operatorname{Ad}_{h^{-1}}\operatorname{pr}_2^*\theta+\operatorname{Ad}_{h^{-1}}\pi^*\alpha$ therefore reduces, after cancelling the common $\operatorname{Ad}_{h^{-1}}\operatorname{pr}_2^*\theta$, to
> $$\pi^*\alpha=\operatorname{Ad}_{h^{-1}}\pi^*\alpha\quad\text{for all }h\in G,\qquad\text{i.e.}\qquad\operatorname{Ad}_{h^{-1}}\big(\alpha_m(v)\big)=\alpha_m(v)\ \ \text{for all }h\in G,\ m\in M,\ v\in T_mM.$$
> That is, every value $\alpha_m(v)$ must be fixed by $\operatorname{Ad}_h$ for all $h$. For $G$ connected, differentiating $h\mapsto\operatorname{Ad}_h(\alpha_m(v))$ at $e$ shows this is equivalent to $[\,X,\alpha_m(v)]=\operatorname{ad}_X(\alpha_m(v))=0$ for all $X\in\mathfrak g$, i.e. $\alpha_m(v)\in\mathfrak z(\mathfrak g)$, the centre of the Lie algebra.
>
> **Case 1: $G$ abelian.** Then $\operatorname{Ad}_h=\operatorname{id}$ for all $h$ and $\mathfrak z(\mathfrak g)=\mathfrak g$, so the condition is vacuous: **every** $\alpha\in\Omega^1(M;\mathfrak g)$ gives a connection. This recovers the fact that on a trivial bundle with abelian $G$ the connections form the affine space $\operatorname{pr}_2^*\theta+\pi^*\Omega^1(M;\mathfrak g)$.
>
> **Case 2: $G=SU(2)$.** Then $\mathfrak g=\mathfrak{su}(2)$ has trivial centre, $\mathfrak z(\mathfrak{su}(2))=\{0\}$ (it is simple), so the condition forces $\alpha_m(v)=0$ for all $m,v$, i.e. $\alpha=0$. Only $\alpha=0$ gives a connection of this form; any $\alpha\neq 0$ is a $\mathfrak g$-valued $1$-form satisfying (2) but violating (1), the promised concrete non-equivariant complement. $\checkmark$
>
> The dividing line is exactly $\operatorname{Ad}$-invariance, which is why clause (1) is not decorative: for non-abelian $G$ it genuinely restricts the candidate forms.

**Calibration check.** Three quick verifications the reader can run from the definitions on this page. First, **restricted to a fibre, $\omega$ is the Maurer–Cartan form.** For the orbit diffeomorphism $\ell_p\colon G\to P_{\pi(p)}$, $\ell_p(a)=p\cdot a$, and a tangent vector $\widetilde\eta(a)=d_eL_a(\eta)$ at $a\in G$, one has $d\ell_p(\widetilde\eta(a))=\tfrac{d}{dt}\big|_0\,p\cdot a\exp(t\eta)=\eta_P(p\cdot a)$, so $\ell_p^*\omega$ evaluated there is $\omega_{p\cdot a}(\eta_P(p\cdot a))=\eta=\theta_a(\widetilde\eta(a))$ (by clause (2), then $\theta(\widetilde\eta)=\eta$); hence $\ell_p^*\omega=\theta$, using only the normalisation. Second, **the difference of two connections vanishes on vertical vectors.** If $\omega,\omega'\in\mathcal A(P)$ then $(\omega-\omega')(\xi_P(p))=\xi-\xi=0$ for every $\xi$ (clause (2) for each), and since every vertical vector is some $\xi_P(p)$, the difference $\omega-\omega'$ is horizontal; together with the fact that it is equivariant (subtract clause (1) for each) this is why $\omega-\omega'$ is basic and descends to $\Omega^1(M;\operatorname{ad}P)$. Third, **for abelian $G$ clause (1) is ordinary invariance:** $\operatorname{Ad}_{g^{-1}}=\operatorname{id}$, so (1) reads $R_g^*\omega=\omega$; understanding why the product connection then has $R_g^*\operatorname{pr}_2^*\theta=\operatorname{pr}_2^*\theta$ recovers that $\theta$ on an abelian group is bi-invariant.

---

# Unlocked by This

> [!tip] Horizontal subspace and horizontal lift *(from this chapter)*
> With $\omega$ in hand, $H_p=\ker\omega_p$ is a $G$-invariant complement to the vertical subspace, and every tangent vector on $M$ has a unique **[[Def - Horizontal Subspace and Horizontal Lift|horizontal lift]]** to $P$. This is the machine that transports and differentiates; the correspondence between forms and invariant distributions is [[Thm - Connection Forms Correspond to Invariant Horizontal Distributions|the correspondence theorem]].

> [!tip] Curvature and the structure equation *(from this chapter)*
> The failure of the horizontal distribution to be integrable is measured by the **[[Def - Curvature of a Principal Connection|curvature]]** $\Omega$, computed from $\omega$ by the structure equation $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$ ([[Thm - Structure Equation for the Curvature|structure equation theorem]]). A connection is the input; its curvature is the first invariant one reads off.

> [!tip] Gauge potentials and gauge transformations *(from Gauge Theory V and VII)*
> The local form $A_s=s^*\omega$ is the gauge potential; changing the local section changes $A_s$ by a Maurer–Cartan term, and the automorphisms of $P$ act on $\mathcal A(P)$ as the **gauge group**. The affine structure of $\mathcal A(P)$, established here, is the arena in which the Yang–Mills functional is minimised.
