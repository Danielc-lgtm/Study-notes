---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection on a Principal Bundle"
  - "Def - Horizontal Subspace and Horizontal Lift"
  - "Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space"
  - "Def - Adjoint Bundles ad P and Ad P"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a Lie group with Lie algebra $\mathfrak{g} = T_eG$, and $\pi\colon P \to M$ is a smooth principal $G$-bundle over a smooth manifold $M$, with the group acting on the **right**, $R_g(p) = p\cdot g$. For $\xi \in \mathfrak{g}$ the **fundamental vector field** on $P$ is $\xi_P(p) = \frac{d}{dt}\big|_{t=0}\, p\cdot\exp(t\xi)$; it is vertical, meaning $d\pi(\xi_P) = 0$, and the assignment $\xi \mapsto \xi_P(p)$ is a linear isomorphism from $\mathfrak{g}$ onto the vertical subspace $V_p = \ker d\pi_p = T_p(P_{\pi(p)})$ (see [[Def - Fundamental Vector Field of a Group Action]]).

We fix a **connection** $\omega \in \Omega^1(P; \mathfrak{g})$ on $P$, that is (see [[Def - Connection on a Principal Bundle]]) a $\mathfrak{g}$-valued $1$-form satisfying

$$\omega(\xi_P) = \xi \quad \text{for all } \xi \in \mathfrak{g}, \qquad\qquad R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega \quad \text{for all } g \in G. \tag{C1, C2}$$

Here $\operatorname{Ad}\colon G \to GL(\mathfrak{g})$ is the adjoint representation, $\operatorname{Ad}_g = d_e(h \mapsto ghg^{-1})$, so that for a matrix group $\operatorname{Ad}_gX = gXg^{-1}$; its differential is $\operatorname{ad}_\xi = [\xi, \cdot\,]$ (see [[Thm - Ad is a Smooth Representation and its Differential is ad]]). The connection determines at each $p \in P$ the **horizontal subspace** $H_p := \ker\omega_p$, and one has the direct-sum splitting $T_pP = H_p \oplus V_p$ with $dR_g(H_p) = H_{pg}$ for all $g$ (see [[Def - Horizontal Subspace and Horizontal Lift]]). We write $\pi_H\colon T_pP \to H_p$ for the projection onto the horizontal summand along $V_p$, and $\pi_V = \operatorname{id} - \pi_H\colon T_pP \to V_p$ for the vertical projection. The **horizontal lift** of a vector field $X$ on $M$ is the unique horizontal $G$-invariant vector field $\tilde X$ on $P$ with $d\pi(\tilde X) = X\circ\pi$.

We use the **bracket of $\mathfrak{g}$-valued forms** of [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]]: for $\alpha, \beta \in \Omega^1(P; \mathfrak{g})$,

$$[\alpha \wedge \beta](X, Y) = [\alpha(X), \beta(Y)] - [\alpha(Y), \beta(X)], \qquad\text{so in particular}\qquad [\omega \wedge \omega](X, Y) = 2\,[\omega(X), \omega(Y)]. \tag{$\ast$}$$

For a matrix Lie algebra this bracket is $[\alpha \wedge \beta] = \alpha \wedge \beta + \beta \wedge \alpha$ on $1$-forms, and $\tfrac12[\omega \wedge \omega] = \omega \wedge \omega$; the factor $\tfrac12$ below is exactly what compensates the factor $2$ in $(\ast)$. The exterior derivative $d$ acts on a $\mathfrak{g}$-valued form componentwise (fix any basis of $\mathfrak{g}$), and we use throughout the invariant formula for the exterior derivative of a $1$-form,

$$d\alpha(X, Y) = X\big(\alpha(Y)\big) - Y\big(\alpha(X)\big) - \alpha([X, Y]) \tag{$d$-formula}$$

for vector fields $X, Y$ (see [[Thm - Coordinate Expression for the Exterior Derivative]]; for a $\mathfrak{g}$-valued form it holds in each component).

Symbols introduced on this page: the **curvature form** $\Omega \in \Omega^2(P; \mathfrak{g})$ on the total space; the **local curvature forms** $F_\alpha \in \Omega^2(U_\alpha; \mathfrak{g})$; the **curvature** $F_\omega \in \Omega^2(M; \operatorname{ad}P)$ on the base; and, when $G$ is abelian, the scalar-type curvature $F \in \Omega^2(M; \mathfrak{g})$. The bundle $\operatorname{ad}P = P\times_{\operatorname{Ad}}\mathfrak{g}$ is the vector bundle associated to $P$ by the adjoint representation (see [[Def - Adjoint Bundles ad P and Ad P]]).

> [!warning] Convention: three names for one object across the two sources
> Haydys writes the connection form as $a$, its curvature on the total space as $\hat F_A := da + \tfrac12[a\wedge a]$, and the descended curvature on $M$ as $F_a \in \Omega^2(M; \operatorname{ad}P)$, calling both the total-space and the base object "the curvature form". Bär writes the connection form as $\omega$, the total-space curvature as $\Omega \in \Omega^2(P; \mathfrak{g})$, the local forms as $\Omega_\alpha := s_\alpha^*\Omega$, and the base curvature as $\bar\Omega \in \Omega^2(M; P\times_{\operatorname{Ad}}\mathfrak{g})$. **This series fixes the notation** $\Omega \in \Omega^2(P; \mathfrak{g})$ for the total-space form, $F_\alpha := s_\alpha^*\Omega \in \Omega^2(U_\alpha; \mathfrak{g})$ for the local forms, and $F_\omega \in \Omega^2(M; \operatorname{ad}P)$ for the descended curvature (Bär's $\bar\Omega$, Haydys's $F_a$). One-line dictionary: $\Omega = \hat F_A$, $F_\omega = F_a = \bar\Omega$, $F_\alpha = \Omega_\alpha = A$-pullback.

> [!warning] Convention: Haydys's "$G$-invariant" means "$\operatorname{Ad}$-equivariant"
> In stating that $da + \tfrac12[a\wedge a]$ descends, Haydys writes that the form is "$G$-invariant". What is required, and what he verifies, is $\operatorname{Ad}$-equivariance $R_g^*(da+\tfrac12[a\wedge a]) = \operatorname{Ad}_{g^{-1}}(da+\tfrac12[a\wedge a])$, which is the type-$\operatorname{Ad}$ transformation, not literal invariance $R_g^*(\cdot) = (\cdot)$. We use the precise term **equivariant** below. (Bär's connection definition prints a related slip, "$R_g^* = \operatorname{Ad}_{g^{-1}}\circ\omega$" for the correct $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\circ\,\omega$; we use the corrected form throughout.)

**This is a compound page.** It defines four interlocking notions — the curvature form $\Omega$ on the total space, its local representatives $F_\alpha$, the curvature $F_\omega$ that lives on the base with values in $\operatorname{ad}P$, and the scalar-valued curvature $F$ available only in the abelian case — because they are one geometric object seen in four coordinate systems, and separating them into four pages would sever the descent argument that is the entire content of the definition.

---

# Axiom Motivation

We already possess a curvature for connections on **vector** bundles: for a covariant derivative $\nabla$ on $E \to M$ the curvature $F_\nabla(X, Y)s = \nabla_X\nabla_Y s - \nabla_Y\nabla_X s - \nabla_{[X,Y]}s$ is a $2$-form on $M$ with values in $\operatorname{End}E$, measuring the failure of second covariant derivatives to commute (see [[Def - Curvature of a Vector-Bundle Connection]]). A principal connection carries no sections to differentiate; it is a distribution of horizontal subspaces $H_p = \ker\omega_p$, one in each tangent space $T_pP$, invariant under the group and complementary to the fibre directions. The question that forces the definition upon us is therefore the geometric shadow of the vector-bundle question: **when do the horizontal subspaces fit together into a foliation, and if they do not, by how much do they fail?** A vector transported horizontally around a small closed loop in $M$ returns rotated; the infinitesimal generator of that rotation is what we must capture. Equivalently, the horizontal distribution $H$ is integrable — tangent to a family of submanifolds — precisely when the Lie bracket of two horizontal vector fields is again horizontal; the curvature will be exactly the vertical part of that bracket, and it vanishes if and only if $H$ integrates to horizontal leaves.

The first desideratum is that the curvature be a genuine object **on the base $M$**, not merely on the total space $P$. The connection $\omega$ itself does not descend: it is $\operatorname{Ad}$-equivariant but not horizontal, since $\omega(\xi_P) = \xi \ne 0$ on vertical directions. So the naive candidate cannot simply be $\omega$. The exterior derivative $d\omega$ is the natural next candidate, because for a vector-bundle connection the local curvature is $dA + \tfrac12[A\wedge A]$ and $dA$ is its leading term. But $d\omega$ alone is not horizontal when $G$ is non-abelian. Testing it on two vertical vectors, using $(d\text{-formula})$, the constancy $\omega(\xi_P) = \xi$, and the bracket relation $[\xi_P, \eta_P] = [\xi,\eta]_P$ for fundamental fields (see [[Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions]]), one finds

$$d\omega(\xi_P, \eta_P) = \xi_P(\omega(\eta_P)) - \eta_P(\omega(\xi_P)) - \omega([\xi_P, \eta_P]) = 0 - 0 - \omega([\xi,\eta]_P) = -[\xi, \eta],$$

which is nonzero whenever $[\xi, \eta] \ne 0$. A form that is nonzero on pairs of vertical vectors cannot be the pullback of anything on $M$. So $d\omega$ by itself is disqualified for non-abelian structure groups; it must be corrected.

There are exactly two ways to enforce horizontality, and they turn out to give the same form. The first, Bär's, is to **project onto the horizontal before differentiating**: set $\Omega(X, Y) := d\omega(\pi_H X, \pi_H Y)$, which is horizontal by fiat, since $\pi_H$ annihilates vertical vectors. The second, Haydys's, is to **add the algebraic correction $\tfrac12[\omega\wedge\omega]$**, which on two vertical vectors evaluates to $\tfrac12[\omega\wedge\omega](\xi_P, \eta_P) = [\omega(\xi_P), \omega(\eta_P)] = [\xi, \eta]$ by $(\ast)$, exactly cancelling the offending $-[\xi, \eta]$ above. That the projection and the correction agree — $d\omega(\pi_H\,\cdot, \pi_H\,\cdot) = d\omega + \tfrac12[\omega\wedge\omega]$ — is the content of the structure equation, [[Thm - Structure Equation for the Curvature]], stated below and proved on its own page. The definition is thus not arbitrary: the $\tfrac12[\omega\wedge\omega]$ term is the unique quadratic correction that makes $d\omega$ horizontal, and the coefficient $\tfrac12$ is forced by the factor $2$ in $(\ast)$.

Per-clause failure analysis. **Drop the horizontal projection (or the bracket correction) and keep only $d\omega$:** the resulting form is not horizontal for non-abelian $G$, by the computation above, hence does not descend to $M$, and the curvature would remain trapped on the total space. For abelian $G$ the bracket vanishes identically, $d\omega$ is already horizontal, and $\Omega = d\omega$ — this is the whole of Maxwell's electromagnetism, where the curvature of a $U(1)$-connection is the field strength $F = dA$. **Drop the requirement that the connection be $\operatorname{Ad}$-equivariant (C2):** then $\Omega$ would still be horizontal but would fail $R_g^*\Omega = \operatorname{Ad}_{g^{-1}}\Omega$, and the descent through the correspondence between basic equivariant forms on $P$ and $\operatorname{ad}P$-valued forms on $M$ (see [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space]]) would break; there would be a horizontal $2$-form on $P$, but no $2$-form on $M$. **Insist on landing in $\Omega^2(M; \mathfrak{g})$ rather than $\Omega^2(M; \operatorname{ad}P)$:** this is possible only for abelian $G$, where $\operatorname{Ad}$ is trivial and $\operatorname{ad}P = M\times\mathfrak{g}$ is the trivial bundle; for non-abelian $G$ the fibrewise identification of $\mathfrak{g}$ over different points of $M$ is twisted by the transition functions, and forgetting that twist would produce a quantity that changes under a change of local section — not a well-defined form on $M$. The correct target is a $2$-form valued in the associated bundle $\operatorname{ad}P$, and this is what distinguishes principal curvature from ordinary scalar-valued $2$-forms.

A reader who has internalised these three failures can reconstruct the definition: differentiate the connection, force horizontality (equivalently, add $\tfrac12[\omega\wedge\omega]$), read off equivariance, and descend to an $\operatorname{ad}P$-valued form on the base, which collapses to a scalar $\mathfrak{g}$-valued closed form exactly when the group is abelian.

---

# The Definition

Let $\pi\colon P \to M$ be a principal $G$-bundle with connection $\omega \in \Omega^1(P; \mathfrak{g})$, and let $\pi_H\colon T_pP \to H_p$ be the horizontal projection determined by $\omega$.

**The curvature form on the total space (primary form).** The **curvature form** of $\omega$ is the $\mathfrak{g}$-valued $2$-form $\Omega \in \Omega^2(P; \mathfrak{g})$ defined by

$$\Omega(X, Y) := d\omega\big(\pi_H(X), \pi_H(Y)\big), \qquad X, Y \in T_pP.$$

From this form all the others are derived. Two facts are immediate from the definition.

- **$\Omega$ is horizontal:** if either argument is vertical, then $\pi_H$ sends it to $0$, so $\Omega(X, Y) = 0$. In particular $\Omega$ vanishes on every pair containing a fundamental vector field.
- **$\Omega$ agrees with $d\omega$ on horizontal vectors:** if $X, Y \in H_p$ then $\pi_H X = X$, $\pi_H Y = Y$, so $\Omega(X, Y) = d\omega(X, Y)$.

**The structure equation (secondary description).** The projected form has a closed algebraic expression that never mentions $\pi_H$: with the bracket $(\ast)$,

$$\boxed{\;\Omega = d\omega + \tfrac12[\omega \wedge \omega]\;}\qquad\text{(for a matrix group, } \Omega = d\omega + \omega\wedge\omega\text{).}$$

This equality — that the geometrically defined $d\omega(\pi_H\,\cdot, \pi_H\,\cdot)$ equals the algebraically defined $d\omega + \tfrac12[\omega\wedge\omega]$ — is the **structure equation** and is proved in full on [[Thm - Structure Equation for the Curvature]]:

> **Theorem (structure equation).** For a connection $\omega$ on a principal $G$-bundle, $d\omega(\pi_HX, \pi_HY) = \big(d\omega + \tfrac12[\omega\wedge\omega]\big)(X, Y)$ for all $X, Y$; equivalently $\Omega = d\omega + \tfrac12[\omega\wedge\omega]$.

We use this identity below to compute $\Omega$ in examples and to descend it to the base; the descent, however, does not depend on it, as the direct proof of equivariance shows.

**$\Omega$ is $\operatorname{Ad}$-equivariant.** The curvature form transforms under the right action exactly as the connection does:

$$R_g^*\Omega = \operatorname{Ad}_{g^{-1}}\circ\,\Omega \qquad \text{for all } g \in G.$$

> [!note]- Proof that $R_g^*\Omega = \operatorname{Ad}_{g^{-1}}\Omega$
> We must show, for every $g \in G$ and all $X, Y \in T_pP$, that $\Omega(dR_g X, dR_g Y) = \operatorname{Ad}_{g^{-1}}\Omega(X, Y)$.
>
> **Step 0 — the horizontal projection commutes with $dR_g$.** The right translation $R_g\colon P \to P$ maps the fibre $P_{\pi(p)}$ to itself, hence carries vertical vectors to vertical vectors: $dR_g(V_p) = V_{pg}$. By the equivariance of the horizontal distribution, $dR_g(H_p) = H_{pg}$ (this is a property of the horizontal subspaces recorded in [[Def - Horizontal Subspace and Horizontal Lift]], where $dR_g(H_p) = H_{pg}$ is proved from clause (C2)). Since $dR_g$ preserves both summands of $T_pP = H_p \oplus V_p$ and sends them to the two summands of $T_{pg}P = H_{pg} \oplus V_{pg}$, it commutes with the projections onto the horizontal summand:
> $$\pi_H \circ dR_g = dR_g \circ \pi_H \qquad\text{(since } dR_g \text{ maps } H_p \to H_{pg},\ V_p \to V_{pg}\text{).}$$
>
> **Step 1 — pull $d\omega$ through $R_g$.** Exterior differentiation commutes with pullback, so $R_g^*(d\omega) = d(R_g^*\omega)$. By the connection axiom (C2), $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$, where $\operatorname{Ad}_{g^{-1}}\colon \mathfrak{g} \to \mathfrak{g}$ is a fixed (point-independent) linear map. A fixed linear map applied to the values of a form commutes with $d$, because $d$ acts componentwise in any basis. Hence
> $$R_g^*(d\omega) = d\big(\operatorname{Ad}_{g^{-1}}\omega\big) = \operatorname{Ad}_{g^{-1}}\,d\omega \qquad\text{(by (C2), then } \operatorname{Ad}_{g^{-1}} \text{ constant, hence commuting with } d\text{).}$$
>
> **Step 2 — assemble.** For all $X, Y \in T_pP$,
> $$(R_g^*\Omega)(X, Y) = \Omega(dR_gX, dR_gY) = d\omega\big(\pi_H dR_g X,\ \pi_H dR_g Y\big) \qquad\text{(definition of } \Omega \text{ at } pg\text{)}$$
> $$= d\omega\big(dR_g\,\pi_H X,\ dR_g\,\pi_H Y\big) \qquad\text{(by Step 0)}$$
> $$= (R_g^*d\omega)\big(\pi_H X, \pi_H Y\big) = \operatorname{Ad}_{g^{-1}}\,d\omega\big(\pi_H X, \pi_H Y\big) \qquad\text{(by Step 1)}$$
> $$= \operatorname{Ad}_{g^{-1}}\,\Omega(X, Y) \qquad\text{(definition of } \Omega \text{ at } p\text{).}$$
>
> **Conclusion.** Therefore $R_g^*\Omega = \operatorname{Ad}_{g^{-1}}\circ\,\Omega$, so $\Omega$ is $\operatorname{Ad}$-equivariant. $\blacksquare$

Combined with horizontality, this says $\Omega$ is a **basic** (horizontal) and **$\operatorname{Ad}$-equivariant** $\mathfrak{g}$-valued $2$-form on $P$; equivalently, $\Omega \in \Omega^2_{\mathrm{bas}}(P; \mathfrak{g})^G$.

**The curvature on the base.** By the correspondence between bundle-valued forms on the base and basic equivariant forms on the total space, restated here:

> **Theorem (basic equivariant forms descend).** For a representation $\rho\colon G \to GL(V)$, pullback along $\pi$ gives a linear isomorphism $\Omega^q(M; P\times_\rho V) \xrightarrow{\ \sim\ } \Omega^q_{\mathrm{bas}}(P; V)^G$ onto the space of horizontal, $\rho$-equivariant $V$-valued $q$-forms on $P$; a base form $\bar\beta$ corresponds to the total-space form $\pi^*\bar\beta$, and conversely every basic equivariant form is $\pi^*$ of a unique base form (see [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space]]).

Applying this with $\rho = \operatorname{Ad}$ and $V = \mathfrak{g}$, so that $P\times_{\operatorname{Ad}}\mathfrak{g} = \operatorname{ad}P$, the basic equivariant form $\Omega$ is $\pi^*$ of a unique form on $M$: there exists a unique

$$F_\omega \in \Omega^2(M; \operatorname{ad}P) \qquad\text{with}\qquad \pi^*F_\omega = \Omega.$$

This $F_\omega$ is **the curvature** of the connection $\omega$; it is Bär's $\bar\Omega$ and Haydys's $F_a$. It is a genuine $2$-form on the base manifold $M$, valued in the vector bundle $\operatorname{ad}P$.

**Local curvature forms.** Choose a trivialising cover $\{U_\alpha\}$ of $M$ with local sections $s_\alpha\colon U_\alpha \to P|_{U_\alpha}$ (local gauges; see [[Def - Local Connection Form and Gauge Potential]]), and let $A_\alpha := s_\alpha^*\omega \in \Omega^1(U_\alpha; \mathfrak{g})$ be the local connection forms. The **local curvature forms** are the pullbacks of $\Omega$:

$$F_\alpha := s_\alpha^*\Omega \in \Omega^2(U_\alpha; \mathfrak{g}).$$

Pulling the structure equation back along $s_\alpha$ and using that pullback commutes with $d$ (see [[Thm - Pull-Back Commutes with the Exterior Derivative]]) and with the bracket (which is defined componentwise), we obtain the local form of the structure equation,

$$F_\alpha = s_\alpha^*\big(d\omega + \tfrac12[\omega\wedge\omega]\big) = d(s_\alpha^*\omega) + \tfrac12[s_\alpha^*\omega \wedge s_\alpha^*\omega] = dA_\alpha + \tfrac12[A_\alpha \wedge A_\alpha]$$

(and $F_\alpha = dA_\alpha + A_\alpha\wedge A_\alpha$ for a matrix group). Under a change of gauge $s_\beta = s_\alpha\cdot g_{\alpha\beta}$ with transition function $g_{\alpha\beta}\colon U_\alpha\cap U_\beta \to G$, the local curvature forms transform by conjugation with **no inhomogeneous term**,

$$F_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha,$$

as proved on [[Thm - Transformation of Local Connection and Curvature Forms]] (contrast the connection forms, which pick up the pure-gauge term $g_{\alpha\beta}^*\theta$). This homogeneous transformation is precisely the compatibility that lets the local pieces $[s_\alpha, F_\alpha]$ assemble into the global section $F_\omega$: in the trivialisation of $\operatorname{ad}P$ induced by $s_\alpha$ over $U_\alpha$,

$$F_\omega\big|_{U_\alpha}(X, Y) = [\,s_\alpha,\ F_\alpha(X, Y)\,], \qquad X, Y \in T_uM.$$

That the right-hand sides agree on overlaps is checked in the Examples section below.

**The abelian case.** If $G$ is abelian, then $\operatorname{Ad}_g = \operatorname{id}_{\mathfrak{g}}$ for all $g$, so $[\,\cdot\,,\cdot\,] \equiv 0$ and the structure equation collapses to $\Omega = d\omega$; the local forms satisfy $F_\alpha = dA_\alpha$ and, by $F_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha = F_\alpha$, agree on all overlaps. Moreover $\operatorname{ad}P = P\times_{\operatorname{Ad}}\mathfrak{g} = M\times\mathfrak{g}$ is the trivial bundle. The $F_\alpha$ therefore glue directly to a single $\mathfrak{g}$-valued $2$-form on $M$,

$$F \in \Omega^2(M; \mathfrak{g}), \qquad F|_{U_\alpha} = dA_\alpha,$$

identified with $F_\omega$ under $\operatorname{ad}P = M\times\mathfrak{g}$. This is the field strength of gauge theory in the abelian ($U(1)$, electromagnetic) case.

---

# Categorical / Structural Definition

Curvature has no universal-property definition, but it has two clean structural characterisations, each independent of the local data and each illuminating a different aspect of the object.

**Curvature as the vertical part of the bracket of horizontal lifts.** For horizontal vector fields the curvature reads off how far their Lie bracket fails to be horizontal. If $\tilde X, \tilde Y$ are horizontal (for instance the horizontal lifts of vector fields on $M$), then

$$\Omega(\tilde X, \tilde Y) = -\,\omega\big([\tilde X, \tilde Y]\big).$$

> [!note]- Proof that $\Omega(\tilde X, \tilde Y) = -\omega([\tilde X, \tilde Y])$ for horizontal $\tilde X, \tilde Y$
> **Goal.** Show that on horizontal vector fields $\tilde X, \tilde Y$ the curvature equals minus $\omega$ of their bracket.
>
> **Reduce to $d\omega$.** Since $\tilde X, \tilde Y$ are horizontal, $\pi_H\tilde X = \tilde X$ and $\pi_H\tilde Y = \tilde Y$, so by the definition of $\Omega$,
> $$\Omega(\tilde X, \tilde Y) = d\omega(\tilde X, \tilde Y) \qquad\text{(definition of } \Omega \text{; } \tilde X, \tilde Y \text{ horizontal).}$$
>
> **Apply the invariant formula.** By $(d\text{-formula})$ applied to the $\mathfrak{g}$-valued $1$-form $\omega$,
> $$d\omega(\tilde X, \tilde Y) = \tilde X\big(\omega(\tilde Y)\big) - \tilde Y\big(\omega(\tilde X)\big) - \omega\big([\tilde X, \tilde Y]\big) \qquad\text{(by the } d\text{-formula).}$$
> Because $\tilde X, \tilde Y$ are horizontal, $\omega(\tilde X) = 0$ and $\omega(\tilde Y) = 0$ identically, so both derivative terms vanish:
> $$d\omega(\tilde X, \tilde Y) = 0 - 0 - \omega([\tilde X, \tilde Y]) = -\omega([\tilde X, \tilde Y]) \qquad\text{(since } \omega(\tilde X) = \omega(\tilde Y) = 0\text{).}$$
>
> **Conclusion.** Combining, $\Omega(\tilde X, \tilde Y) = -\omega([\tilde X, \tilde Y])$. Since $\omega$ restricted to the vertical subspace is the inverse of $\xi \mapsto \xi_P$, the quantity $-\omega([\tilde X, \tilde Y])$ reads off, as an element of $\mathfrak{g}$, minus the vertical component of the bracket $[\tilde X, \tilde Y]$; that is, $\Omega$ is the vertical part of the bracket of horizontal lifts. $\blacksquare$

This is the structural heart of the object: the horizontal distribution $H = \ker\omega$ is **involutive** (closed under Lie bracket) if and only if $\omega([\tilde X, \tilde Y]) = 0$ for all horizontal $\tilde X, \tilde Y$, that is, if and only if $\Omega = 0$. By the Frobenius theorem, involutivity is equivalent to integrability, so **the curvature is the exact obstruction to the horizontal distribution being tangent to a foliation of $P$** (this equivalence is drilled in [[Ex - The Curvature is the Obstruction to Integrability of the Horizontal Distribution]]). A connection with $\Omega = 0$ is called flat, and flatness means the horizontal subspaces knit together into leaves.

**Curvature as the exterior covariant derivative of the connection.** The horizontal-projection definition $\Omega(X, Y) = d\omega(\pi_HX, \pi_HY)$ is the special case, applied to the connection form itself, of the exterior covariant derivative $D^\omega\alpha := (d\alpha)\circ\pi_H$ acting on $\mathfrak{g}$-valued forms on $P$. In that language

$$\Omega = D^\omega\omega,$$

exhibiting curvature as "the horizontal part of the derivative of the connection" (see [[Def - Exterior Covariant Derivative on a Principal Bundle]]). The two characterisations are the same statement read forwards and backwards: $D^\omega\omega$ differentiates and then horizontalises, and on horizontal arguments the derivative $d\omega$ is $-\omega\circ[\,\cdot\,,\cdot\,]$.

---

# Relate to Other Fields / Compression

**True name.** Operationally, the curvature of a principal connection is *the vertical part of the Lie bracket of horizontal lifts*: $\Omega(\tilde X, \tilde Y) = -\omega([\tilde X, \tilde Y])$. Every computation in gauge theory that involves curvature ultimately cashes out as this statement — that transporting horizontally along the coordinate directions $X$ and then $Y$, versus $Y$ then $X$, differs by a vertical (fibre) displacement, and $\Omega$ names that displacement as an element of $\mathfrak{g}$ (or, after descent, of $\operatorname{ad}P$). The official definition $\Omega = d\omega + \tfrac12[\omega\wedge\omega]$ is the coordinate-friendly avatar of this operational content.

**Relation to the vector-bundle curvature.** Under the frame-bundle and associated-bundle correspondences, principal curvature specialises exactly to the curvature $F_\nabla$ of [[Def - Curvature of a Vector-Bundle Connection]]. If $E = P\times_\rho V$ is associated to $P$ by a representation $\rho$, and $\nabla^\omega$ is the induced covariant derivative on $E$, then the curvature of $\nabla^\omega$ is $\rho_*(F_\omega) \in \Omega^2(M; \operatorname{End}E)$, where $\rho_*$ is the differential of $\rho$; locally $F_{\nabla^\omega} = \rho_*(F_\alpha)$. For the standard representation on the frame bundle this recovers the local formula $F = dA + A\wedge A$ of [[Thm - Local Formula for the Curvature of a Connection]]; the principal picture is the source of which the vector-bundle picture is the $GL_k$ (or $\rho$-associated) image. The choice of target bundle is the visible difference: vector-bundle curvature is $\operatorname{End}E$-valued, principal curvature is $\operatorname{ad}P$-valued, and the two are matched by $\rho_* \colon \operatorname{ad}P \to \operatorname{End}E$.

**Relation to physics.** For $G = U(1)$, abelian, the curvature $F = dA \in \Omega^2(M; \mathfrak{u}(1)) = \Omega^2(M; i\mathbb{R})$ is the electromagnetic field strength; the connection form $A$ is the electromagnetic potential, $dF = 0$ (a special case of the Bianchi identity) recovers the homogeneous Maxwell equations, and $\tfrac{i}{2\pi}[F]$ is the first Chern class of the associated line bundle. For $G = SU(2)$ or $SU(3)$, non-abelian, $F_\alpha = dA_\alpha + A_\alpha\wedge A_\alpha$ with $A_\alpha$ the Yang–Mills gauge potential and $F_\alpha$ the field strength; the extra quadratic term $A\wedge A$ is precisely the non-abelian self-interaction of the gauge field. The single formula $\Omega = d\omega + \tfrac12[\omega\wedge\omega]$ therefore contains both electromagnetism (bracket term absent) and the strong and weak interactions (bracket term present).

**Compression.** The whole definition is one slogan: *curvature is the failure of horizontality to be closed under bracket, differentiated once and descended to the base.* The four objects on this page are the same failure recorded on the total space ($\Omega$), in a local gauge ($F_\alpha$), globally on the base ($F_\omega$), and — when the group is commutative so the twist disappears — as an ordinary closed $2$-form ($F$).

---

# Examples / Corollaries

**Is an instance — the product (flat) connection on $M\times G$.** On the trivial bundle $P = M\times G$ take the product connection $\omega = \operatorname{pr}_2^*\theta$, the pullback of the (left) Maurer–Cartan form $\theta \in \Omega^1(G; \mathfrak{g})$ under the projection $\operatorname{pr}_2\colon M\times G \to G$ (this is a connection; see [[Def - The Maurer-Cartan Form]] and the verification in [[Ex - The Product Connection on a Trivial Bundle and Pure Gauge Potentials]]). Its curvature vanishes:

$$\Omega = d\omega + \tfrac12[\omega\wedge\omega] = \operatorname{pr}_2^*\Big(d\theta + \tfrac12[\theta\wedge\theta]\Big) = \operatorname{pr}_2^*(0) = 0,$$

where the second equality uses that pullback commutes with $d$ and with the bracket, and the third is the **Maurer–Cartan equation** $d\theta + \tfrac12[\theta\wedge\theta] = 0$ (proved on [[Thm - The Maurer-Cartan Equation]]). Hence $F_\omega = 0$ and the connection is flat, consistent with the True-name reading: the horizontal subspaces $H_{(m,g)} = T_mM\times\{0\}$ are the tangent spaces to the leaves $M\times\{g\}$, which do foliate $M\times G$, so their brackets are horizontal and $\Omega = 0$.

**Is an instance — the standard connection on the Hopf bundle (nonzero curvature).** On the Hopf bundle $S^3 \to S^2$ (the case $n = 1$ of $S^{2n+1}\to\mathbb{CP}^n$), with $G = U(1)$, $\mathfrak{u}(1) = i\mathbb{R}$, the standard connection form is $a = (-x_1\,dx_0 + x_0\,dx_1 - x_3\,dx_2 + x_2\,dx_3)\,i$ in the coordinates of $\mathbb{R}^4 \supset S^3$ (see [[Thm - The Standard Connection on the Hopf Bundle]]). Since $U(1)$ is abelian the bracket term drops and $\Omega = da$; computing the exterior derivative,

$$\Omega = da = 2\,(dx_0\wedge dx_1 + dx_2\wedge dx_3)\,i \ \ne\ 0,$$

so the Hopf connection has nonvanishing curvature; its descent $F_\omega$ is a nonzero closed $2$-form on $S^2$ with $\int_{S^2}F_\omega = 2\pi i$. The full computation, including the verification $\Omega(ip, Y) = 0$ on vertical vectors and the identification $F_\omega = 2\,\mathrm{vol}_{S^2_{1/2}}\,i$, is carried out in [[Ex - Curvature of the Standard Hopf Connection]]. This example is the geometric origin of the nontriviality of the Hopf bundle: a flat connection on it would force $\int_{S^2}F_\omega = 0$, which fails.

**Is NOT an instance — $d\omega$ alone (for non-abelian $G$).** The bare exterior derivative $d\omega$ is not a candidate curvature for non-abelian structure groups, because it is not horizontal, hence does not descend to $M$. We verify the failure clause by clause on a pair of vertical vectors $\xi_P, \eta_P$ with $[\xi, \eta] \ne 0$ (possible whenever $\mathfrak{g}$ is non-abelian, for example $\mathfrak{g} = \mathfrak{su}(2)$ with $\xi, \eta$ two of the Pauli generators):

$$d\omega(\xi_P, \eta_P) = \xi_P\big(\omega(\eta_P)\big) - \eta_P\big(\omega(\xi_P)\big) - \omega\big([\xi_P, \eta_P]\big) \qquad\text{(by the } d\text{-formula).}$$

Now $\omega(\eta_P) = \eta$ and $\omega(\xi_P) = \xi$ are constant $\mathfrak{g}$-valued functions on $P$ (connection axiom (C1)), so the first two terms are derivatives of constants and vanish. For the third, $[\xi_P, \eta_P] = [\xi, \eta]_P$ (the fundamental-field map is a Lie algebra homomorphism for right actions, [[Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions]]), so $\omega([\xi_P, \eta_P]) = \omega([\xi, \eta]_P) = [\xi, \eta]$ by (C1). Hence

$$d\omega(\xi_P, \eta_P) = 0 - 0 - [\xi, \eta] = -[\xi, \eta] \ \ne\ 0.$$

A form that is nonzero on two vertical vectors cannot be $\pi^*$ of any form on $M$, so $d\omega$ is disqualified. The curvature repairs exactly this, since the correction contributes $\tfrac12[\omega\wedge\omega](\xi_P, \eta_P) = [\omega(\xi_P), \omega(\eta_P)] = [\xi, \eta]$ by $(\ast)$, giving $\Omega(\xi_P, \eta_P) = -[\xi, \eta] + [\xi, \eta] = 0$, in agreement with the horizontality of $\Omega$. For abelian $G$ the two terms are separately zero and $d\omega$ is already horizontal, which is why $\Omega = d\omega$ in the abelian case.

**Corollary — the local pieces glue.** The formula $F_\omega|_{U_\alpha}(X, Y) = [s_\alpha, F_\alpha(X, Y)]$ is well defined, i.e. independent of $\alpha$ on overlaps.

> [!note]- Proof that $[s_\alpha, F_\alpha]$ and $[s_\beta, F_\beta]$ agree on $U_\alpha\cap U_\beta$
> **Goal.** Show $[s_\alpha, F_\alpha(X, Y)] = [s_\beta, F_\beta(X, Y)]$ as elements of the fibre $(\operatorname{ad}P)_u = (P\times_{\operatorname{Ad}}\mathfrak{g})_u$, for $u \in U_\alpha\cap U_\beta$ and $X, Y \in T_uM$.
>
> **Recall the equivalence relation on $\operatorname{ad}P$.** An element of $P\times_{\operatorname{Ad}}\mathfrak{g}$ is an equivalence class $[p, \xi]$ under $(p\cdot g,\ \operatorname{Ad}_{g^{-1}}\xi) \sim (p, \xi)$ for $g \in G$ (see [[Def - Adjoint Bundles ad P and Ad P]]).
>
> **Substitute the transition law for the sections and for the curvature.** By definition of the transition function, $s_\beta = s_\alpha\cdot g_{\alpha\beta}$, and by the homogeneous transformation of local curvature forms (restated: $F_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha$, from [[Thm - Transformation of Local Connection and Curvature Forms]]),
> $$[s_\beta,\ F_\beta(X, Y)] = \big[\,s_\alpha\cdot g_{\alpha\beta},\ \operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha(X, Y)\,\big] \qquad\text{(by } s_\beta = s_\alpha g_{\alpha\beta} \text{ and } F_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha\text{).}$$
> **Apply the equivalence relation.** With $p = s_\alpha(u)$, $g = g_{\alpha\beta}(u)$, $\xi = F_\alpha(X, Y)$, the pair $(p\cdot g,\ \operatorname{Ad}_{g^{-1}}\xi)$ represents the same class as $(p, \xi)$:
> $$\big[\,s_\alpha\cdot g_{\alpha\beta},\ \operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha(X, Y)\,\big] = [\,s_\alpha,\ F_\alpha(X, Y)\,] \qquad\text{(by the defining relation of } \operatorname{ad}P\text{).}$$
>
> **Conclusion.** The two local expressions coincide on the overlap, so they patch to a single global section $F_\omega \in \Omega^2(M; \operatorname{ad}P)$; this is exactly Bär's construction of $\bar\Omega$, and it agrees with the $F_\omega$ obtained by descent, since both restrict to $[s_\alpha, F_\alpha]$ over $U_\alpha$. $\blacksquare$

**Corollary — the abelian curvature is a globally defined scalar-type form.** If $G$ is abelian then $F_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha = F_\alpha$ on every overlap, so the local forms $F_\alpha \in \Omega^2(U_\alpha; \mathfrak{g})$ agree wherever two charts meet and therefore define a single global $F \in \Omega^2(M; \mathfrak{g})$; under $\operatorname{ad}P = M\times\mathfrak{g}$ this $F$ is $F_\omega$. This is the precise sense in which "abelian gauge fields are ordinary $\mathfrak{g}$-valued $2$-forms".

**Calibration check.** First, $\Omega$ vanishes if either argument is vertical: this is immediate from the definition $\Omega(X, Y) = d\omega(\pi_HX, \pi_HY)$ since $\pi_H$ kills vertical vectors — verify it against the non-example, where $d\omega(\xi_P, \eta_P) = -[\xi, \eta]$ but $\Omega(\xi_P, \eta_P) = 0$. Second, $F_\omega$ is a $2$-form on the base $M$ valued in the vector bundle $\operatorname{ad}P$, not in the fixed vector space $\mathfrak{g}$ — the two coincide only when $G$ is abelian and $\operatorname{ad}P = M\times\mathfrak{g}$ is trivial; if you find yourself writing $F_\omega \in \Omega^2(M; \mathfrak{g})$ for a non-abelian group you have dropped the twist by the transition functions. Third, check the coefficient: for a matrix group $\tfrac12[\omega\wedge\omega] = \omega\wedge\omega$, so the structure equation reads $\Omega = d\omega + \omega\wedge\omega$, and on two vertical fundamental fields $(\omega\wedge\omega)(\xi_P, \eta_P) = \omega(\xi_P)\omega(\eta_P) - \omega(\eta_P)\omega(\xi_P) = \xi\eta - \eta\xi = [\xi, \eta]$, again cancelling $d\omega(\xi_P, \eta_P) = -[\xi, \eta]$ — the factor $\tfrac12$ and the matrix wedge $\omega\wedge\omega$ describe the same correction.

---

# Unlocked by This

> [!tip] Structure equation and the local field strength *(from Gauge Theory IV)*
> With curvature defined, the identity $\Omega = d\omega + \tfrac12[\omega\wedge\omega]$ and its local form $F_\alpha = dA_\alpha + \tfrac12[A_\alpha\wedge A_\alpha]$ become available (see [[Thm - Structure Equation for the Curvature]]); this is the formula every subsequent computation of curvature uses.

> [!tip] The Bianchi identity *(from Gauge Theory IV)*
> Differentiating the structure equation yields $d^{\nabla_\omega}F_\omega = 0$, the Bianchi identity, the universal constraint every curvature satisfies (see [[Thm - Bianchi Identity for a Principal Connection]]); for abelian $G$ it is $dF = 0$, the homogeneous Maxwell equations.

> [!tip] Chern–Weil theory and characteristic classes *(from Gauge Theory VI)*
> Feeding the curvature into an $\operatorname{Ad}$-invariant polynomial produces closed forms on $M$ whose de Rham classes are independent of the connection — the **Chern and Pontryagin classes**. Curvature is the analytic input to every characteristic number, including the instanton number $\int_M c_2(P)$.

> [!tip] Yang–Mills theory and instantons *(from Gauge Theory VII)*
> The **Yang–Mills functional** $\mathcal{YM}(\omega) = \tfrac12\int_M |F_\omega|^2$ measures the size of the curvature; its critical points are the Yang–Mills connections, and the absolute minima in a fixed topological sector are the (anti-)self-dual connections, the **instantons** at the heart of Donaldson theory.
