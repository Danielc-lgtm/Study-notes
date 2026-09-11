---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Curvature of a Principal Connection"
  - "Def - Connection on a Principal Bundle"
  - "Def - Horizontal Subspace and Horizontal Lift"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
  - "Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms"
  - "Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions"
  - "Thm - Cartan's Magic Formula"
  - "Thm - Coordinate Expression for the Exterior Derivative"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a Lie group with Lie algebra $\mathfrak{g} = T_eG$, and $\pi : P \to M$ is a smooth principal $G$-bundle. Following the series convention, $G$ acts on $P$ on the **right**, $R_g(p) = p \cdot g$, and this action is free and transitive on the fibres. For $\xi \in \mathfrak{g}$ the **[[Def - Fundamental Vector Field of a Group Action|fundamental vector field]]** $\xi_P$ is the vector field on $P$ whose value at $p$ is
$$\xi_P(p) = \frac{d}{dt}\Big|_{t=0}\, p \cdot \exp(t\xi),$$
so $\xi_P$ points along the fibre; Bär writes $\bar{\xi}$ for the same object. The **vertical subspace** at $p$ is $V_p = \ker(d\pi_p) = \{\xi_P(p) : \xi \in \mathfrak{g}\}$, and the map $\xi \mapsto \xi_P(p)$ is a linear isomorphism $\mathfrak{g} \to V_p$ (freeness of the action).

A **[[Def - Connection on a Principal Bundle|connection]]** is a $\mathfrak{g}$-valued $1$-form $\omega \in \Omega^1(P; \mathfrak{g})$ satisfying, for all $g \in G$ and all $\xi \in \mathfrak{g}$,
$$\text{(1)}\quad R_g^*\omega = \operatorname{Ad}_{g^{-1}} \circ\, \omega, \qquad\qquad \text{(2)}\quad \omega(\xi_P) = \xi .$$
Property (1) is **$\operatorname{Ad}$-equivariance**; property (2) says $\omega$ reproduces the Lie-algebra label of every vertical vector. Here $\operatorname{Ad}_g = d_e(h \mapsto ghg^{-1}) : \mathfrak{g} \to \mathfrak{g}$ is the adjoint representation, and $\operatorname{ad}_\xi \eta = [\xi, \eta]$ is its differential. Haydys writes $a$ for $\omega$ and — misleadingly — calls property (1) "$G$-invariance"; the correct term is $\operatorname{Ad}$-equivariance, and we use it throughout.

The **[[Def - Horizontal Subspace and Horizontal Lift|horizontal subspace]]** is $H_p = \ker(\omega_p)$; it satisfies $T_pP = V_p \oplus H_p$, $\dim H_p = \dim M$, and $dR_g(H_p) = H_{pg}$ for all $g$. We write $\pi_H : T_pP \to H_p$ for the projection onto $H_p$ along $V_p$. A tangent vector or vector field is **horizontal** if it lies in $H$ (equivalently, is annihilated by $\omega$) and **vertical** if it lies in $V$.

The **[[Def - Curvature of a Principal Connection|curvature form]]** of $\omega$ is
$$\Omega \in \Omega^2(P; \mathfrak{g}), \qquad \Omega(X, Y) := d\omega\big(\pi_H(X),\, \pi_H(Y)\big),$$
the exterior derivative of $\omega$ evaluated only on horizontal parts. By construction $\Omega$ is **horizontal** (it vanishes as soon as one argument is vertical, since $\pi_H$ kills that argument).

For the **[[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|bracket of 𝔤-valued forms]]** we use the series convention: for $\alpha, \beta \in \Omega^1(P; \mathfrak{g})$,
$$[\alpha \wedge \beta](X, Y) = [\alpha(X), \beta(Y)] - [\alpha(Y), \beta(X)], \qquad\text{so}\qquad [\omega \wedge \omega](X, Y) = 2\,[\omega(X), \omega(Y)].$$

> [!warning] Convention: the factor $\tfrac12$, the bracket, and the matrix wedge
> Bär writes this bracket $[\omega, \omega]$; the series writes $[\omega \wedge \omega]$; they denote the same $2$-form. Because $[\omega \wedge \omega](X, Y) = 2[\omega(X), \omega(Y)]$ carries an intrinsic factor of $2$, the structure equation below carries the compensating $\tfrac12$. For a **matrix Lie group** ($G \subseteq GL_k$, so $\mathfrak{g} \subseteq \mathfrak{gl}_k$ and $[\zeta, \eta] = \zeta\eta - \eta\zeta$) one has $[A \wedge A] = 2\,A \wedge A$, where $A \wedge A$ is the wedge taken with matrix multiplication, $(A \wedge A)(X, Y) = A(X)A(Y) - A(Y)A(X)$ — this is the sibling identity proved on **[[Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms]]** part (d). Consequently $\tfrac12[A \wedge A] = A \wedge A$, and the structure equation reads $F = dA + A \wedge A$ **without** an explicit $\tfrac12$ (Haydys equation (18)), while the intrinsic form $F = dA + \tfrac12[A \wedge A]$ (Haydys equation (20)) holds for any Lie group. The two are the same equation.

> [!warning] Convention: the exterior-derivative normalisation
> We use the normalisation $d\omega(X, Y) = X\big(\omega(Y)\big) - Y\big(\omega(X)\big) - \omega([X, Y])$ for a $1$-form (Lee, Bär, and this series), with **no** $\tfrac{1}{k+1}$ prefactor. The explicit $\tfrac12$ in the structure equation is tied to this normalisation together with the factor $2$ in $[\omega \wedge \omega]$; a source that folds a $\tfrac12$ into either the exterior derivative or the bracket will display the same identity with the constant absorbed.

---

# Statement

> **Theorem (Structure equation for the curvature).** Let $P \to M$ be a principal $G$-bundle with connection form $\omega \in \Omega^1(P; \mathfrak{g})$ and curvature $\Omega(X, Y) = d\omega(\pi_H X, \pi_H Y)$. Then:
>
> **(a) (Structure equation.)** As $2$-forms on $P$,
> $$\Omega = d\omega + \tfrac12[\omega \wedge \omega].$$
>
> **(b) (Bracket of fundamental and horizontal fields.)** For every $\xi \in \mathfrak{g}$ and every horizontal vector field $Y$ on $P$, the Lie bracket $[\xi_P, Y]$ is horizontal.
>
> **(c) ($\operatorname{Ad}$-equivariance of the curvature.)** For every $g \in G$,
> $$R_g^*\Omega = \operatorname{Ad}_{g^{-1}} \circ\, \Omega.$$
>
> **(d) (Local form of the curvature.)** For a local section (local gauge) $s_\alpha : U_\alpha \to P$ with local connection form $A_\alpha := s_\alpha^*\omega \in \Omega^1(U_\alpha; \mathfrak{g})$, the local curvature form $F_\alpha := s_\alpha^*\Omega$ satisfies
> $$F_\alpha = dA_\alpha + \tfrac12[A_\alpha \wedge A_\alpha];$$
> for a matrix group this is $F_\alpha = dA_\alpha + A_\alpha \wedge A_\alpha$, and for an abelian group it is $F_\alpha = dA_\alpha$.
>
> **(e) ($d\omega + \tfrac12[\omega \wedge \omega]$ is basic and equivariant.)** The $\mathfrak{g}$-valued $2$-form $d\omega + \tfrac12[\omega \wedge \omega]$ is **basic** (it vanishes whenever one argument is vertical) and **$\operatorname{Ad}$-equivariant** ($R_g^*(d\omega + \tfrac12[\omega \wedge \omega]) = \operatorname{Ad}_{g^{-1}}(d\omega + \tfrac12[\omega \wedge \omega])$). Hence, by the descent theorem for basic equivariant forms, there is a unique $F_\omega \in \Omega^2(M; \operatorname{ad}P)$ with $\pi^* F_\omega = \Omega$.

Parts (b) and (e) are the two structural inputs; parts (a), (c), (d) are the working forms of the identity. Part (a) with the exterior-covariant-derivative language is written $\Omega = D^\omega\omega$ on the companion page **[[Def - Exterior Covariant Derivative on a Principal Bundle]]**.

---

# Motivation

The curvature of a principal connection has two faces, and this theorem is the bridge between them. Its first face is the *conceptual* definition, $\Omega(X, Y) = d\omega(\pi_H X, \pi_H Y)$: the curvature measures how far the horizontal distribution $H = \ker\omega$ is from being integrable, by feeding $d\omega$ only horizontal inputs. This definition makes the geometry transparent — curvature is the obstruction to the horizontal planes fitting together into surfaces — but it is nearly useless for computation, because the horizontal projection $\pi_H$ is an implicit, connection-dependent operation that is painful to write in coordinates.

Its second face is the *computational* formula, $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$: the curvature is the exterior derivative of the connection form corrected by a quadratic self-bracket. This face has no $\pi_H$ in it. It is a polynomial expression in $\omega$ and its first derivatives, and once pulled back by a local section it becomes the field strength $F = dA + \tfrac12[A \wedge A]$ that every physicist writes down and every calculation uses. The whole reason the principal-bundle formalism is worth its abstraction is that it turns the frame-dependent bookkeeping of [[Def - Curvature of a Vector-Bundle Connection|vector-bundle curvature]] into a single global object; the structure equation is what makes that object computable.

The theorem does more than identify the two faces. Part (b) — the bracket of a fundamental field with a horizontal field is again horizontal — is the technical fact that makes the whole comparison work, and it recurs in every subsequent computation on the total space. Part (c), the $\operatorname{Ad}$-equivariance of $\Omega$, together with part (e), its basicness, is exactly the pair of properties that lets the curvature *descend*: an $\operatorname{Ad}$-equivariant basic $\mathfrak{g}$-valued form on $P$ is the same data as a genuine two-form on the base with values in the adjoint bundle $\operatorname{ad}P$. Without (c) and (e) there would be no curvature *on $M$* at all, only a form upstairs on $P$; with them, we get $F_\omega \in \Omega^2(M; \operatorname{ad}P)$, the object that feeds Chern–Weil theory, the Bianchi identity, and the Yang–Mills equation.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of the theorem is only "a connection $\omega$ on a principal bundle". The interesting sources are the disguises under which a connection, and hence this identity, is handed to you.

The first disguised source is **a $G$-invariant horizontal distribution**. Suppose a problem gives you not a $1$-form but a smoothly varying family of subspaces $H_p \subset T_pP$ with $T_pP = V_p \oplus H_p$ and $dR_g(H_p) = H_{pg}$ — a "choice of horizontal directions" compatible with the group. By the correspondence between connection forms and invariant horizontal distributions (proved on the sibling page **[[Thm - Connection Forms Correspond to Invariant Horizontal Distributions]]**), this is the same data as a connection $\omega$, with $H = \ker\omega$. The bridge $B \Rightarrow A$ is that the projection-and-read-off construction turns the distribution into a $1$-form satisfying (1) and (2), after which the structure equation applies verbatim and tells you the curvature of the distribution. *Example problem:* on the [[Def - The Hopf Bundle|Hopf bundle]] $S^3 \to S^2$, the orthogonal complement $H_p = (\mathbb{C}p)^\perp$ of the fibre direction is such a distribution; the structure equation computes its curvature and shows it is nonzero, so the planes do not integrate to surfaces.

The second disguised source is **a covariant derivative on a vector bundle**. A [[Def - Connection on a Vector Bundle|connection]] $\nabla$ on a rank-$k$ vector bundle $E$ is not visibly a principal connection, but it determines one on the frame bundle $\operatorname{Fr}(E)$, a principal $GL_k$-bundle, with $e^*\omega = A(\nabla, e)$ for every local frame $e$ (the sibling theorem **[[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]]**). The bridge is this identification of frames with local sections. Applying part (d) in the matrix case then reproduces the [[Thm - Local Formula for the Curvature of a Connection|vector-bundle curvature formula]] $F = dA + A \wedge A$ of chapter II as a special case, so any question phrased about $\nabla$ can be answered by the principal-bundle structure equation. *Example problem:* recover the Riemann curvature two-forms of the Levi-Civita connection as the local curvature form of the induced connection on the orthonormal frame bundle.

The third disguised source is **a bare gauge potential from physics**. A physicist typically starts not with a global $\omega$ but with a $\mathfrak{g}$-valued $1$-form $A = A_\mu \, dx^\mu$ on a coordinate patch of spacetime — the gauge potential — and no bundle in sight. Any such $A$ is the local form $s^*\omega$ of a connection on the trivial bundle $U \times G$ for the identity section (sibling page **[[Def - Local Connection Form and Gauge Potential]]**). The bridge is that a single local $1$-form always trivially satisfies the (empty) overlap condition, so it is genuine connection data over $U$. Part (d) then manufactures the field strength $F = dA + \tfrac12[A \wedge A]$ directly, and its transformation law under a change of gauge is governed by the same computation. *Example problem:* given an $\mathfrak{su}(2)$ potential $A_\mu : \mathbb{R}^4 \to \mathfrak{su}(2)$, write the Yang–Mills field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + [A_\mu, A_\nu]$.

**Targets (Output Amplification)**

Combine the structure equation with **the exterior derivative and the graded Jacobi identity**. Differentiating $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ and using $d^2 = 0$ together with the graded Leibniz and Jacobi rules for the bracket (sibling **[[Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms]]**) produces the **Bianchi identity** $D^\omega\Omega = 0$, locally $dF_\alpha + [A_\alpha \wedge F_\alpha] = 0$ (sibling **[[Thm - Bianchi Identity for a Principal Connection]]**). The extra ingredient is the calculus of $\mathfrak{g}$-valued forms; the payoff is the universal identity that every curvature satisfies, the geometric conservation law behind the source-free Maxwell equations.

Combine the descended curvature $F_\omega$ from part (e) with an **$\operatorname{Ad}$-invariant polynomial** on $\mathfrak{g}$. Feeding $F_\omega$ into a symmetric invariant polynomial $f$ of degree $\ell$ produces a $2\ell$-form $f(F_\omega)$ on $M$; the structure equation and the Bianchi identity together prove this form closed and its cohomology class independent of the connection — this is the **[[Thm - Chern-Weil Theorem|Chern–Weil theorem]]**, the machine that turns curvature into the [[Def - Chern Classes|characteristic classes]] of chapter VI. The extra ingredient is invariance; the payoff is a bundle invariant computed from any connection.

Combine the local field strength $F_\alpha$ with **a metric and the Hodge star**. Contracting $F$ with an $\operatorname{Ad}$-invariant inner product on $\mathfrak{g}$ and integrating $|F|^2$ gives the Yang–Mills functional, whose Euler–Lagrange equation is $d^\omega \star F = 0$ (chapter VII, **[[Thm - Yang-Mills Equation from the Action Principle]]**). The extra ingredient is the metric; the payoff is the field equation of non-abelian gauge theory, for which the structure equation supplies the very definition of $F$ that is varied.

---

# Why Is It True

Both sides of the structure equation, $\Omega$ and $d\omega + \tfrac12[\omega \wedge \omega]$, are honest $2$-forms on $P$: at each point they are alternating bilinear maps $T_pP \times T_pP \to \mathfrak{g}$. To compare two alternating bilinear maps it is enough to compare them on pairs drawn from a spanning set, and the splitting $T_pP = V_p \oplus H_p$ gives us three kinds of pair: vertical–vertical, vertical–horizontal, horizontal–horizontal. On each kind the two sides agree for a reason that is visible without any computation once the arithmetic is done once.

**On two vertical vectors, $d\omega$ contributes $-[\xi, \eta]$ and $\tfrac12[\omega \wedge \omega]$ contributes $+[\xi, \eta]$, so the right-hand side cancels to zero — which is exactly $\Omega$, since $\Omega$ ignores vertical inputs.** The cancellation is the heart of the matter. Extend the two vertical vectors to fundamental fields $\xi_P, \eta_P$. Then $\omega(\xi_P) = \xi$ and $\omega(\eta_P) = \eta$ are *constant* functions, so their directional derivatives drop out of the invariant formula for $d\omega$, and what survives is $-\omega([\xi_P, \eta_P])$. The fundamental-field map is a Lie algebra homomorphism for a right action, so $[\xi_P, \eta_P] = [\xi, \eta]_P$ and $\omega([\xi_P, \eta_P]) = [\xi, \eta]$; hence $d\omega(\xi_P, \eta_P) = -[\xi, \eta]$. Meanwhile the bracket term is $\tfrac12 \cdot 2[\xi, \eta] = +[\xi, \eta]$. They annihilate, and the answer $0$ is what the horizontal projection forces $\Omega$ to give.

On a mixed pair — one vertical, one horizontal — both sides are simply zero. The bracket term dies because $\omega$ vanishes on the horizontal argument. And $d\omega$ dies because of the one genuinely non-trivial lemma, part (b): the bracket $[\xi_P, Y]$ of a fundamental field with a horizontal field is *again horizontal*, so $\omega([\xi_P, Y]) = 0$; the two directional-derivative terms in the invariant formula also vanish (one differentiates a constant, the other differentiates zero). This is why (b) is not a side remark but the load-bearing input.

On two horizontal vectors the bracket term vanishes (again $\omega$ kills horizontal inputs), and $\Omega(X, Y) = d\omega(\pi_H X, \pi_H Y) = d\omega(X, Y)$ because $X, Y$ are already horizontal, so $\pi_H$ does nothing. The two sides agree with no cancellation needed. So the structure equation is the single global statement that ties together three separate local facts, each forced by one of the two defining properties of a connection.

---

# What Makes This Hard

The step that is silently used in every textbook and is easy to get wrong is the identity $\omega([\xi_P, \eta_P]) = [\xi, \eta]$ in the vertical–vertical case: it depends on the fundamental-field map being a genuine Lie algebra **homomorphism** (for the right action of this series), whereas for a *left* action the same map is an **anti**-homomorphism and the sign flips, breaking the cancellation. The second subtlety is that the invariant formula for $d\omega$ requires extending the given tangent vectors to vector fields, and one must choose the *right* extensions — fundamental fields for vertical vectors, horizontal fields for horizontal ones — so that the directional-derivative terms can be evaluated; the value is extension-independent because $d\omega$ is tensorial, but the computation only becomes tractable for these choices. The third is part (b) itself: it is tempting to think brackets respect the horizontal–vertical splitting in general, but they do not — the bracket of two horizontal fields is generically *not* horizontal (that failure is the curvature), and only the mixed bracket $[\text{vertical}, \text{horizontal}]$ stays horizontal.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce part (a) to a pointwise check on the three pair-types allowed by $T_pP = V_p \oplus H_p$, evaluating $d\omega$ through the invariant formula $d\omega(X, Y) = X(\omega(Y)) - Y(\omega(X)) - \omega([X, Y])$ with fundamental extensions of vertical vectors and horizontal extensions of horizontal vectors. The only non-trivial inputs are two facts about brackets on $P$: the fundamental-field map is a bracket homomorphism (kills the vertical–vertical case), and $[\text{vertical}, \text{horizontal}]$ is horizontal (kills the mixed case). Parts (c), (e) then follow from the equivariance and basicness of $\omega$, and (d) by pulling everything back along a local section.

**Subgoal decomposition:**

1. **Establish $\mathcal{L}_{\xi_P}\omega = -[\xi, \omega]$.**
   - *Hint:* The flow of $\xi_P$ is $R_{\exp(t\xi)}$; pull $\omega$ back through it using equivariance (1), then differentiate at $t = 0$ using $\frac{d}{dt}\big|_0 \operatorname{Ad}_{\exp(-t\xi)} = -\operatorname{ad}_\xi$.
   - *Why needed:* It powers both part (b) and part (e).

2. **Prove part (b): $[\xi_P, Y]$ is horizontal.**
   - *Hint:* Show $\omega([\xi_P, Y]) = 0$ by expanding $\mathcal{L}_{\xi_P}(\omega(Y))$ with the Leibniz rule and using subgoal 1 with $\omega(Y) \equiv 0$.
   - *Why needed:* It is the vertical–horizontal case of the structure equation.

3. **Prove the homomorphism identity $\omega([\xi_P, \eta_P]) = [\xi, \eta]$.**
   - *Hint:* Combine $[\xi_P, \eta_P] = [\xi, \eta]_P$ (chapter I) with the defining property $\omega(\zeta_P) = \zeta$.
   - *Why needed:* It is the vertical–vertical case.

4. **Prove part (a) by the three-case check.**
   - *Hint:* Vertical–vertical uses subgoal 3 and the constancy of $\omega(\xi_P)$; mixed uses subgoal 2; horizontal–horizontal is immediate.
   - *Why needed:* It is the structure equation.

5. **Prove part (c): $R_g^*\Omega = \operatorname{Ad}_{g^{-1}}\Omega$.**
   - *Hint:* Show $dR_g$ preserves the splitting, hence commutes with $\pi_H$; then push the pullback through $d\omega$ using equivariance and $R_g^* d\omega = d(R_g^*\omega)$.
   - *Why needed:* It is one of the two descent conditions.

6. **Prove part (e) by Cartan's magic formula, and part (d) by pullback.**
   - *Hint:* For (e), contract $d\omega + \tfrac12[\omega \wedge \omega]$ with $\xi_P$ using $\mathcal{L}_K = d\iota_K + \iota_K d$; for (d), apply $s_\alpha^*$ to (a) using that pullback commutes with $d$ and with the bracket.
   - *Why needed:* (e) gives basicness (the second descent condition); (d) is the computational form.

---

# Lemma Decomposition

> [!note]- Lemma 1: The Lie derivative of the connection form along a fundamental field
> **Statement:** For every $\xi \in \mathfrak{g}$, $\mathcal{L}_{\xi_P}\omega = -[\xi, \omega]$, where $[\xi, \omega]$ is the $\mathfrak{g}$-valued $1$-form $X \mapsto [\xi, \omega(X)] = \operatorname{ad}_\xi(\omega(X))$.
>
> **Hint:** The flow of $\xi_P$ is right translation by $\exp(t\xi)$; use equivariance of $\omega$ and differentiate the resulting $\operatorname{Ad}$.
>
> **Why needed:** It is the engine of parts (b) and (e): it converts the geometric operation "Lie-drag $\omega$ along the fibre" into the algebraic operation "bracket with $\xi$".
>
> > [!note]- Full proof
> > **Set-up.** By the definition of the Lie derivative of a form via its generating flow, $\mathcal{L}_{\xi_P}\omega = \frac{d}{dt}\big|_{t=0} \Phi_t^*\omega$, where $\Phi_t$ is the flow of the vector field $\xi_P$.
> >
> > **Identify the flow.** For a right action, the flow of the fundamental field $\xi_P$ is right translation: $\Phi_t = R_{\exp(t\xi)}$. This is the corollary recorded on **[[Def - Fundamental Vector Field of a Group Action]]** — the integral curve of $\xi_P$ through $p$ is $t \mapsto p \cdot \exp(t\xi) = R_{\exp(t\xi)}(p)$, because $\frac{d}{dt}\, p\exp(t\xi) = \xi_P(p\exp(t\xi))$ by the one-parameter subgroup property of $\exp$.
> >
> > **Pull back using equivariance.** By the defining property (1) of a connection, applied with $g = \exp(t\xi)$ so that $g^{-1} = \exp(-t\xi)$,
> > $$\Phi_t^*\omega = R_{\exp(t\xi)}^*\,\omega = \operatorname{Ad}_{\exp(t\xi)^{-1}} \circ\, \omega = \operatorname{Ad}_{\exp(-t\xi)} \circ\, \omega \qquad\text{(by equivariance (1)).}$$
> > The right-hand side is, at each point and on each tangent vector $X$, the $\mathfrak{g}$-vector $\operatorname{Ad}_{\exp(-t\xi)}\big(\omega(X)\big)$.
> >
> > **Differentiate at $t = 0$.** Fix a tangent vector $X$ and write $v = \omega(X) \in \mathfrak{g}$, which does not depend on $t$. Then
> > $$(\mathcal{L}_{\xi_P}\omega)(X) = \frac{d}{dt}\Big|_{t=0} \operatorname{Ad}_{\exp(-t\xi)}(v) = \Big(\tfrac{d}{dt}\big|_{0}\operatorname{Ad}_{\exp(-t\xi)}\Big)(v) = -\operatorname{ad}_\xi(v) \qquad\text{(chain rule; }\tfrac{d}{dt}|_0\exp(-t\xi) = -\xi\text{).}$$
> > Here we used that the differential of the adjoint representation is $\operatorname{ad}$, that is, $\frac{d}{dt}\big|_{0}\operatorname{Ad}_{\exp(t\zeta)} = \operatorname{ad}_\zeta$ — the theorem **[[Thm - Ad is a Smooth Representation and its Differential is ad]]** — applied to the curve $t \mapsto \exp(-t\xi) = \exp(t(-\xi))$, i.e. with $\zeta = -\xi$, which gives $\operatorname{ad}_{-\xi} = -\operatorname{ad}_\xi$ and hence the sign.
> >
> > **Conclude.** Since $\operatorname{ad}_\xi(v) = [\xi, v] = [\xi, \omega(X)]$ for every $X$, we have $(\mathcal{L}_{\xi_P}\omega)(X) = -[\xi, \omega(X)]$, i.e. $\mathcal{L}_{\xi_P}\omega = -[\xi, \omega]$. $\blacksquare$

> [!note]- Lemma 2: The bracket of a fundamental field with a horizontal field is horizontal (part (b))
> **Statement:** Let $\xi \in \mathfrak{g}$ and let $Y$ be a horizontal vector field on $P$ (that is, $\omega(Y) = 0$ identically). Then $[\xi_P, Y]$ is horizontal, i.e. $\omega([\xi_P, Y]) = 0$.
>
> **Hint:** Apply the Leibniz rule for the Lie derivative to the pairing $\omega(Y)$ and use Lemma 1.
>
> **Why needed:** It is precisely the vertical–horizontal case of the structure equation and appears again in the Bianchi identity.
>
> > [!note]- Full proof
> > **Goal.** We must show the $\mathfrak{g}$-valued function $\omega([\xi_P, Y])$ is identically zero.
> >
> > **Rewrite the bracket as a Lie derivative.** By definition of the Lie derivative of a vector field, $[\xi_P, Y] = \mathcal{L}_{\xi_P} Y$. The Lie derivative obeys the Leibniz rule against the natural pairing of a $1$-form with a vector field: for any $1$-form $\alpha$ and vector field $Z$,
> > $$\mathcal{L}_{\xi_P}\big(\alpha(Z)\big) = (\mathcal{L}_{\xi_P}\alpha)(Z) + \alpha(\mathcal{L}_{\xi_P} Z).$$
> > Apply this with $\alpha = \omega$ and $Z = Y$ and solve for the term we want:
> > $$\omega(\mathcal{L}_{\xi_P} Y) = \mathcal{L}_{\xi_P}\big(\omega(Y)\big) - (\mathcal{L}_{\xi_P}\omega)(Y) \qquad\text{(Leibniz rule for }\mathcal{L}\text{).}$$
> >
> > **Kill the first term.** Since $Y$ is horizontal, $\omega(Y) = 0$ is the constant zero $\mathfrak{g}$-valued function, and the Lie derivative (directional derivative along $\xi_P$) of a constant function is zero: $\mathcal{L}_{\xi_P}\big(\omega(Y)\big) = 0$.
> >
> > **Kill the second term.** By Lemma 1, $\mathcal{L}_{\xi_P}\omega = -[\xi, \omega]$, so
> > $$(\mathcal{L}_{\xi_P}\omega)(Y) = -[\xi, \omega(Y)] = -[\xi, 0] = 0 \qquad\text{(by Lemma 1 and }\omega(Y) = 0\text{).}$$
> >
> > **Conclude.** Both terms vanish, so $\omega([\xi_P, Y]) = \omega(\mathcal{L}_{\xi_P} Y) = 0 - 0 = 0$. Since $H = \ker\omega$, the field $[\xi_P, Y]$ is horizontal. $\blacksquare$

> [!note]- Lemma 3: The homomorphism identity $\omega([\xi_P, \eta_P]) = [\xi, \eta]$
> **Statement:** For all $\xi, \eta \in \mathfrak{g}$, the fundamental fields satisfy $[\xi_P, \eta_P] = [\xi, \eta]_P$ and hence $\omega([\xi_P, \eta_P]) = [\xi, \eta]$.
>
> **Hint:** Use that $\xi \mapsto \xi_P$ is a Lie algebra homomorphism for the right action, then apply the defining property $\omega(\zeta_P) = \zeta$.
>
> **Why needed:** It is the vertical–vertical case of the structure equation; the sign here (homomorphism, not anti-homomorphism) is what makes the cancellation work.
>
> > [!note]- Full proof
> > **The bracket of fundamental fields.** For a smooth *right* action of $G$, the fundamental-field map $\mathfrak{g} \to \mathfrak{X}(P)$, $\zeta \mapsto \zeta_P$, is a Lie algebra homomorphism:
> > $$[\xi_P, \eta_P] = [\xi, \eta]_P \qquad\text{for all }\xi, \eta \in \mathfrak{g}.$$
> > This is the theorem **[[Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions]]**, whose proof identifies $\zeta_P$ with the push-forward of the left-invariant field $\tilde\zeta$ under each orbit map and uses that $\tilde\zeta$-related fields have related brackets. (For a *left* action the same map is an anti-homomorphism, $[\bar\xi, \bar\eta] = -\overline{[\xi, \eta]}$; the series' right-action convention is what gives the plus sign here.)
> >
> > **Apply the connection axiom.** The vector field $[\xi, \eta]_P$ is the fundamental field of the Lie-algebra element $[\xi, \eta] \in \mathfrak{g}$, so by the defining property (2) of a connection, $\omega\big([\xi, \eta]_P\big) = [\xi, \eta]$. Combining,
> > $$\omega([\xi_P, \eta_P]) = \omega([\xi, \eta]_P) = [\xi, \eta] \qquad\text{(homomorphism identity, then property (2)).} \qquad \blacksquare$$

> [!note]- Lemma 4: The right action preserves the horizontal–vertical splitting
> **Statement:** For every $g \in G$ and $p \in P$, the differential $dR_g : T_pP \to T_{pg}P$ satisfies $dR_g(V_p) = V_{pg}$ and $dR_g(H_p) = H_{pg}$; consequently $dR_g \circ \pi_H = \pi_H \circ dR_g$.
>
> **Hint:** Vertical vectors are killed by $d\pi$ and $\pi \circ R_g = \pi$; horizontal vectors are killed by $\omega$ and $\omega$ is equivariant.
>
> **Why needed:** It lets the horizontal projection commute past $R_g$ in the proof of part (c).
>
> > [!note]- Full proof
> > **Vertical directions.** Since the right action preserves fibres, $\pi \circ R_g = \pi$, so $d\pi_{pg} \circ dR_g = d\pi_p$. If $X \in V_p = \ker d\pi_p$ then $d\pi_{pg}(dR_g X) = d\pi_p(X) = 0$, so $dR_g X \in \ker d\pi_{pg} = V_{pg}$. Thus $dR_g(V_p) \subseteq V_{pg}$, and since $dR_g$ is a linear isomorphism (with inverse $dR_{g^{-1}}$) and $\dim V_p = \dim V_{pg} = \dim G$, we get $dR_g(V_p) = V_{pg}$.
> >
> > **Horizontal directions.** Let $X \in H_p = \ker\omega_p$. By equivariance (1),
> > $$\omega_{pg}(dR_g X) = (R_g^*\omega)_p(X) = \operatorname{Ad}_{g^{-1}}\big(\omega_p(X)\big) = \operatorname{Ad}_{g^{-1}}(0) = 0 \qquad\text{(by (1) and }X \in \ker\omega_p\text{),}$$
> > so $dR_g X \in \ker\omega_{pg} = H_{pg}$. Thus $dR_g(H_p) \subseteq H_{pg}$, and again by the isomorphism property and $\dim H_p = \dim H_{pg} = \dim M$ we get $dR_g(H_p) = H_{pg}$.
> >
> > **Commuting with the projection.** Since $dR_g$ carries $V_p$ onto $V_{pg}$ and $H_p$ onto $H_{pg}$, it carries the direct-sum decomposition $T_pP = V_p \oplus H_p$ onto $T_{pg}P = V_{pg} \oplus H_{pg}$ componentwise. Therefore $dR_g$ commutes with the projections onto the horizontal summand: for $X = X^V + X^H$ with $X^V \in V_p$, $X^H \in H_p$,
> > $$\pi_H(dR_g X) = \pi_H(dR_g X^V + dR_g X^H) = dR_g X^H = dR_g(\pi_H X),$$
> > using $dR_g X^V \in V_{pg}$ (killed by $\pi_H$) and $dR_g X^H \in H_{pg}$ (fixed by $\pi_H$). Hence $dR_g \circ \pi_H = \pi_H \circ dR_g$. $\blacksquare$

> [!note]- Lemma 5: Pullback commutes with the exterior derivative and the bracket of $\mathfrak{g}$-valued forms
> **Statement:** Let $f : N \to Q$ be a smooth map and $\alpha, \beta \in \Omega^1(Q; \mathfrak{g})$. Then $f^*(d\alpha) = d(f^*\alpha)$ and $f^*[\alpha \wedge \beta] = [f^*\alpha \wedge f^*\beta]$.
>
> **Hint:** The first is naturality of $d$ applied componentwise; the second is a direct expansion using $(f^*\alpha)(X) = \alpha(df\,X)$.
>
> **Why needed:** It converts the structure equation on $P$ into its local form on $U_\alpha$ under $s_\alpha^*$ (part (d)).
>
> > [!note]- Full proof
> > **Exterior derivative.** Choose a basis $(e_a)$ of $\mathfrak{g}$ and write $\alpha = \sum_a \alpha^a e_a$ with $\alpha^a \in \Omega^1(Q)$ ordinary real-valued forms. Then $d\alpha = \sum_a (d\alpha^a) e_a$ by the componentwise definition of $d$ on $\mathfrak{g}$-valued forms, and pullback acts componentwise, so
> > $$f^*(d\alpha) = \sum_a f^*(d\alpha^a)\, e_a = \sum_a d(f^*\alpha^a)\, e_a = d\Big(\sum_a (f^*\alpha^a) e_a\Big) = d(f^*\alpha),$$
> > where $f^*(d\alpha^a) = d(f^*\alpha^a)$ is the naturality of the ordinary exterior derivative, proved on **[[Thm - Pull-Back Commutes with the Exterior Derivative]]**. (This identity is used repeatedly below and in part (d).)
> >
> > **Bracket.** For tangent vectors $X, Y$ at a point of $N$, using $(f^*\alpha)(X) = \alpha(df\,X)$ and the definition of the bracket of $\mathfrak{g}$-valued $1$-forms,
> > $$\big(f^*[\alpha \wedge \beta]\big)(X, Y) = [\alpha \wedge \beta](df\,X, df\,Y) = [\alpha(df\,X), \beta(df\,Y)] - [\alpha(df\,Y), \beta(df\,X)]$$
> > $$= [(f^*\alpha)(X), (f^*\beta)(Y)] - [(f^*\alpha)(Y), (f^*\beta)(X)] = [f^*\alpha \wedge f^*\beta](X, Y) \qquad\text{(definitions of }f^*\text{ and of the bracket).}$$
> > Since $X, Y$ were arbitrary, $f^*[\alpha \wedge \beta] = [f^*\alpha \wedge f^*\beta]$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $P \to M$ be a principal $G$-bundle with connection $\omega$ and curvature $\Omega(X, Y) = d\omega(\pi_H X, \pi_H Y)$.
>
> **Step 0 — reduction of part (a) to a pointwise three-case check.** Both $\Omega$ and $d\omega + \tfrac12[\omega \wedge \omega]$ are elements of $\Omega^2(P; \mathfrak{g})$, hence at each $p \in P$ are alternating bilinear maps $T_pP \times T_pP \to \mathfrak{g}$. Two alternating bilinear maps that agree on every pair drawn from a spanning set of the vector space agree everywhere; since $T_pP = V_p \oplus H_p$, it suffices to prove the equality on the three pair-types $(X, Y)$ with $X, Y$ both vertical, both horizontal, or one of each. Moreover $d\omega$ is a tensor, so $d\omega(X_p, Y_p)$ depends only on the values $X_p, Y_p$ and may be computed by extending them to any convenient vector fields via the **invariant formula for the exterior derivative** (restated from **[[Thm - Coordinate Expression for the Exterior Derivative]]**, and valid verbatim for $\mathfrak{g}$-valued forms by applying it componentwise in a basis of $\mathfrak{g}$):
> $$d\omega(X, Y) = X\big(\omega(Y)\big) - Y\big(\omega(X)\big) - \omega([X, Y]),$$
> where $X(\omega(Y))$ denotes the directional derivative of the $\mathfrak{g}$-valued function $\omega(Y)$ along $X$. We extend every vertical vector to a fundamental field $\xi_P$ and every horizontal vector to a horizontal vector field (a horizontal vector always extends to a horizontal field, e.g. as the horizontal lift of a local vector field on $M$). We also record the abbreviation $\tfrac12[\omega \wedge \omega](X, Y) = [\omega(X), \omega(Y)]$, from $[\omega \wedge \omega](X, Y) = 2[\omega(X), \omega(Y)]$.
>
> **Part (a), Case 1 — both arguments vertical.** Take $X = \xi_P$, $Y = \eta_P$ for $\xi, \eta \in \mathfrak{g}$.
> - *Curvature side.* Fundamental fields are vertical, so $\pi_H(\xi_P) = \pi_H(\eta_P) = 0$ and $\Omega(\xi_P, \eta_P) = d\omega(0, 0) = 0$.
> - *Exterior-derivative side.* By property (2), $\omega(\xi_P) = \xi$ and $\omega(\eta_P) = \eta$ are constant $\mathfrak{g}$-valued functions, so their directional derivatives vanish: $\xi_P(\omega(\eta_P)) = \xi_P(\eta) = 0$ and $\eta_P(\omega(\xi_P)) = \eta_P(\xi) = 0$. By Lemma 3, $\omega([\xi_P, \eta_P]) = [\xi, \eta]$. Hence
> $$d\omega(\xi_P, \eta_P) = 0 - 0 - [\xi, \eta] = -[\xi, \eta] \qquad\text{(invariant formula; property (2); Lemma 3).}$$
> - *Bracket side.* $\tfrac12[\omega \wedge \omega](\xi_P, \eta_P) = [\omega(\xi_P), \omega(\eta_P)] = [\xi, \eta]$ (property (2)).
> - *Combine.* $d\omega(\xi_P, \eta_P) + \tfrac12[\omega \wedge \omega](\xi_P, \eta_P) = -[\xi, \eta] + [\xi, \eta] = 0 = \Omega(\xi_P, \eta_P)$. The two sides agree.
>
> **Part (a), Case 2 — both arguments horizontal.** Take $X, Y$ horizontal, so $\omega(X) = \omega(Y) = 0$.
> - *Bracket side.* $\tfrac12[\omega \wedge \omega](X, Y) = [\omega(X), \omega(Y)] = [0, 0] = 0$.
> - *Curvature side.* Since $X, Y$ are horizontal, $\pi_H X = X$ and $\pi_H Y = Y$, so $\Omega(X, Y) = d\omega(\pi_H X, \pi_H Y) = d\omega(X, Y)$.
> - *Combine.* $d\omega(X, Y) + \tfrac12[\omega \wedge \omega](X, Y) = d\omega(X, Y) + 0 = \Omega(X, Y)$. The two sides agree, with no computation of $d\omega$ required.
>
> **Part (a), Case 3 — one argument vertical, one horizontal.** Take $X = \xi_P$ vertical and $Y$ horizontal.
> - *Curvature side.* $\pi_H(\xi_P) = 0$, so $\Omega(\xi_P, Y) = d\omega(0, \pi_H Y) = 0$.
> - *Bracket side.* $\tfrac12[\omega \wedge \omega](\xi_P, Y) = [\omega(\xi_P), \omega(Y)] = [\xi, 0] = 0$.
> - *Exterior-derivative side.* We evaluate the invariant formula term by term. First, $\omega(Y) = 0$ ($Y$ horizontal), so $\xi_P(\omega(Y)) = \xi_P(0) = 0$. Second, $\omega(\xi_P) = \xi$ is constant, so $Y(\omega(\xi_P)) = Y(\xi) = 0$. Third, by Lemma 2 the field $[\xi_P, Y]$ is horizontal, so $\omega([\xi_P, Y]) = 0$. Hence
> $$d\omega(\xi_P, Y) = 0 - 0 - 0 = 0 \qquad\text{(invariant formula; }\omega(Y)=0\text{; property (2); Lemma 2).}$$
> - *Combine.* $d\omega(\xi_P, Y) + \tfrac12[\omega \wedge \omega](\xi_P, Y) = 0 + 0 = 0 = \Omega(\xi_P, Y)$. The two sides agree. (By antisymmetry of both $2$-forms, the case $X$ horizontal, $Y$ vertical follows: swapping arguments multiplies both sides by $-1$, and $-0 = 0$.)
>
> The three cases are exhaustive for pairs from $V_p \oplus H_p$, so by Step 0, $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ as $2$-forms on $P$. This proves **(a)**.
>
> **Part (b).** This is Lemma 2: for $\xi \in \mathfrak{g}$ and $Y$ horizontal, $[\xi_P, Y]$ is horizontal. $\checkmark$
>
> **Part (c) — $\operatorname{Ad}$-equivariance of $\Omega$.** Fix $g \in G$. For tangent vectors $X, Y$ at $p$,
> $$(R_g^*\Omega)(X, Y) = \Omega(dR_g X, dR_g Y) = d\omega\big(\pi_H(dR_g X), \pi_H(dR_g Y)\big) \qquad\text{(definitions of }R_g^*\text{ and }\Omega\text{)}$$
> $$= d\omega\big(dR_g(\pi_H X), dR_g(\pi_H Y)\big) \qquad\text{(Lemma 4: }\pi_H \circ dR_g = dR_g \circ \pi_H\text{)}$$
> $$= (R_g^* d\omega)(\pi_H X, \pi_H Y) \qquad\text{(definition of }R_g^*\text{ applied to the }2\text{-form }d\omega\text{).}$$
> Now $R_g^* d\omega = d(R_g^*\omega)$ (Lemma 5, first identity, with $f = R_g$), and $R_g^*\omega = \operatorname{Ad}_{g^{-1}} \circ \omega$ by equivariance (1), so
> $$R_g^* d\omega = d\big(\operatorname{Ad}_{g^{-1}} \circ \omega\big) = \operatorname{Ad}_{g^{-1}} \circ (d\omega),$$
> because $\operatorname{Ad}_{g^{-1}}$ is a fixed linear endomorphism of $\mathfrak{g}$ and $d$ acts componentwise, hence commutes with any fixed linear map. Therefore
> $$(R_g^*\Omega)(X, Y) = \operatorname{Ad}_{g^{-1}}\big(d\omega(\pi_H X, \pi_H Y)\big) = \operatorname{Ad}_{g^{-1}}\big(\Omega(X, Y)\big) \qquad\text{(definition of }\Omega\text{).}$$
> Since $X, Y$ were arbitrary, $R_g^*\Omega = \operatorname{Ad}_{g^{-1}} \circ \Omega$. This proves **(c)**.
>
> **Part (d) — local form.** Let $s_\alpha : U_\alpha \to P$ be a local section, $A_\alpha = s_\alpha^*\omega$, and $F_\alpha = s_\alpha^*\Omega$. Applying $s_\alpha^*$ to the structure equation (a) and using Lemma 5 (both identities, with $f = s_\alpha$),
> $$F_\alpha = s_\alpha^*\Omega = s_\alpha^*\Big(d\omega + \tfrac12[\omega \wedge \omega]\Big) = s_\alpha^*(d\omega) + \tfrac12\, s_\alpha^*[\omega \wedge \omega] = d(s_\alpha^*\omega) + \tfrac12[s_\alpha^*\omega \wedge s_\alpha^*\omega] = dA_\alpha + \tfrac12[A_\alpha \wedge A_\alpha].$$
> Every step is justified: linearity of pullback; $s_\alpha^*(d\omega) = d(s_\alpha^*\omega)$ and $s_\alpha^*[\omega \wedge \omega] = [s_\alpha^*\omega \wedge s_\alpha^*\omega]$ by Lemma 5; the definition $A_\alpha = s_\alpha^*\omega$. For a **matrix group**, $\tfrac12[A_\alpha \wedge A_\alpha] = A_\alpha \wedge A_\alpha$ (the identity $[A \wedge A] = 2A \wedge A$ of **[[Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms]]** part (d)), giving $F_\alpha = dA_\alpha + A_\alpha \wedge A_\alpha$; this is Haydys's local formula (18). For an **abelian group**, $[\zeta, \eta] = 0$ for all $\zeta, \eta \in \mathfrak{g}$, so $[A_\alpha \wedge A_\alpha] = 0$ and $F_\alpha = dA_\alpha$. This proves **(d)**.
>
> **Part (e) — basicness and equivariance of $d\omega + \tfrac12[\omega \wedge \omega]$.** We give the direct computation, independent of parts (a) and (c). Write $\Theta := d\omega + \tfrac12[\omega \wedge \omega]$.
>
> *Basicness.* A $2$-form is basic exactly when its contraction with every vertical vector vanishes; since every vertical vector is $\xi_P(p)$ for some $\xi$, it suffices to show $\iota_{\xi_P}\Theta = 0$ for all $\xi \in \mathfrak{g}$. By **Cartan's magic formula** $\mathcal{L}_K = d\,\iota_K + \iota_K\, d$ (restated from **[[Thm - Cartan's Magic Formula]]**), applied to $K = \xi_P$ and the $1$-form $\omega$,
> $$\iota_{\xi_P}(d\omega) = \mathcal{L}_{\xi_P}\omega - d\big(\iota_{\xi_P}\omega\big).$$
> Here $\iota_{\xi_P}\omega = \omega(\xi_P) = \xi$ is a constant $\mathfrak{g}$-valued function, so $d(\iota_{\xi_P}\omega) = d\xi = 0$; and $\mathcal{L}_{\xi_P}\omega = -[\xi, \omega]$ by Lemma 1. Hence
> $$\iota_{\xi_P}(d\omega) = -[\xi, \omega] \qquad\text{(Cartan's formula; property (2); Lemma 1).}$$
> For the bracket term, contract the $2$-form $[\omega \wedge \omega]$ with $\xi_P$: for any tangent vector $Z$,
> $$\big(\iota_{\xi_P}[\omega \wedge \omega]\big)(Z) = [\omega \wedge \omega](\xi_P, Z) = [\omega(\xi_P), \omega(Z)] - [\omega(Z), \omega(\xi_P)] = [\xi, \omega(Z)] + [\xi, \omega(Z)] = 2[\xi, \omega(Z)],$$
> using $\omega(\xi_P) = \xi$ and antisymmetry $[\omega(Z), \xi] = -[\xi, \omega(Z)]$ of the Lie bracket. Thus $\iota_{\xi_P}[\omega \wedge \omega] = 2[\xi, \omega]$, so $\iota_{\xi_P}\big(\tfrac12[\omega \wedge \omega]\big) = [\xi, \omega]$. Adding,
> $$\iota_{\xi_P}\Theta = \iota_{\xi_P}(d\omega) + \iota_{\xi_P}\big(\tfrac12[\omega \wedge \omega]\big) = -[\xi, \omega] + [\xi, \omega] = 0.$$
> Since this holds for every $\xi$, $\Theta$ vanishes whenever one argument is vertical, i.e. $\Theta$ is basic.
>
> *Equivariance.* Using Lemma 5 (with $f = R_g$), equivariance (1) of $\omega$, that $d$ and $\operatorname{Ad}_{g^{-1}}$ commute, and that $\operatorname{Ad}_{g^{-1}}$ is a Lie algebra automorphism (so $\operatorname{Ad}_{g^{-1}}[\zeta, \eta] = [\operatorname{Ad}_{g^{-1}}\zeta, \operatorname{Ad}_{g^{-1}}\eta]$, whence $[\operatorname{Ad}_{g^{-1}}\omega \wedge \operatorname{Ad}_{g^{-1}}\omega] = \operatorname{Ad}_{g^{-1}}[\omega \wedge \omega]$),
> $$R_g^*\Theta = d(R_g^*\omega) + \tfrac12[R_g^*\omega \wedge R_g^*\omega] = d(\operatorname{Ad}_{g^{-1}}\omega) + \tfrac12[\operatorname{Ad}_{g^{-1}}\omega \wedge \operatorname{Ad}_{g^{-1}}\omega] = \operatorname{Ad}_{g^{-1}}\big(d\omega + \tfrac12[\omega \wedge \omega]\big) = \operatorname{Ad}_{g^{-1}}\Theta.$$
> So $\Theta$ is $\operatorname{Ad}$-equivariant. (This re-derives part (c), since $\Theta = \Omega$ by (a).)
>
> *Descent.* By part (a), $\Theta = \Omega$, so $\Omega$ is basic and $\operatorname{Ad}$-equivariant. The descent theorem for basic equivariant forms — a basic $\operatorname{Ad}$-equivariant $V$-valued $q$-form on $P$ corresponds to a unique $q$-form on $M$ with values in the associated bundle $P \times_{\operatorname{Ad}} V$, via pullback by $\pi$ (**[[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space]]**) — applied with $V = \mathfrak{g}$ and the adjoint action yields a unique $F_\omega \in \Omega^2(M; \operatorname{ad}P)$ with $\pi^* F_\omega = \Omega$. This proves **(e)** and produces the curvature two-form on the base.
>
> All five parts are established. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Integrability of the horizontal distribution (differential topology).** Use the structure equation to prove that $\Omega = 0$ if and only if the horizontal distribution $H = \ker\omega$ is involutive, and combine this with the **[[Thm - The Frobenius Theorem|Frobenius theorem]]** to conclude that flatness is equivalent to $H$ being integrable — the horizontal planes tangent to a foliation. The theorem applies because part (a) shows that for horizontal fields $X, Y$ one has $\Omega(X, Y) = d\omega(X, Y) = -\omega([X, Y])$, so $\Omega$ is precisely the vertical part of $[X, Y]$. It is non-obvious because "curvature" and "integrability" are stated in unrelated languages — a $2$-form versus closure under bracket — and the structure equation is the identity that translates one into the other.

**The abelian Maxwell field (mathematical physics).** For $G = U(1)$, so $\mathfrak{g} = i\mathbb{R}$ abelian, the structure equation collapses to $\Omega = d\omega$ and locally $F = dA$; deduce that $F$ is a *closed* real $2$-form on $M$ and that the map $A \mapsto F$ is linear. The theorem applies because the bracket term vanishes identically for an abelian group. The subtlety is that closedness — which becomes the source-free half of Maxwell's equations, $dF = 0$ — is here a *consequence* of the structure equation and $d^2 = 0$, not an extra postulate; it is the geometric origin of magnetic-charge conservation.

**Chern–Weil closedness (algebraic topology via geometry).** For an $\operatorname{Ad}$-invariant polynomial $f$ of degree $\ell$, use the descended curvature $F_\omega$ from part (e) and the Bianchi identity (a target of this theorem) to show that $f(F_\omega)$ is a closed $2\ell$-form on $M$ whose de Rham class is independent of $\omega$. The theorem applies because part (e) is what produces the base-manifold form $F_\omega$ in the first place, and part (a) is what makes the Bianchi identity available. It is non-obvious because a topological invariant — a characteristic class — is being extracted from a differential-geometric object that depends on an arbitrary choice of connection.

---

# Bridges

- **The vector-bundle curvature formula as the $GL_k$ case.** The local formula (d), $F_\alpha = dA_\alpha + A_\alpha \wedge A_\alpha$ for a matrix group, is *identical* to the chapter II expression for the curvature of a covariant derivative in a local frame, **[[Thm - Local Formula for the Curvature of a Connection]]**. The construction that identifies them is the frame bundle: a connection $\nabla$ on $E$ becomes a principal connection $\omega$ on $\operatorname{Fr}(E)$ (a $GL_k$-bundle) with $e^*\omega = A(\nabla, e)$ for each local frame $e$ viewed as a local section; pulling $\Omega$ back by that section reproduces $F_\nabla = dA + A \wedge A$. Thus the abstract principal-bundle curvature specialises to the concrete matrix curvature, and every property proved here — equivariance, descent, the local formula — descends to the vector-bundle setting.

- **The Bianchi identity as the exterior derivative of the structure equation.** Differentiating $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ and simplifying with $d^2 = 0$ and the graded Leibniz rule for the bracket gives $d\Omega = [\Omega \wedge \omega] - \tfrac12[[\omega \wedge \omega]\wedge\omega]$, and the last term vanishes by the Jacobi identity for a $1$-form. The construction is entirely internal to the calculus of $\mathfrak{g}$-valued forms; the result is $D^\omega\Omega = 0$, locally $dF_\alpha + [A_\alpha \wedge F_\alpha] = 0$, on the sibling page **[[Thm - Bianchi Identity for a Principal Connection]]**. The structure equation is the definition of $F$ that gets differentiated; the Bianchi identity is what that derivative always is.

- **The transformation law for local curvature forms.** Part (c), the $\operatorname{Ad}$-equivariance of $\Omega$, is the total-space statement whose local shadow is the gauge transformation of $F_\alpha$: under a change of section $s_\beta = s_\alpha g_{\alpha\beta}$, the local curvature forms satisfy $F_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}} F_\alpha$ — with **no** inhomogeneous term, unlike the connection, because the curvature is horizontal. This is worked out on **[[Thm - Transformation of Local Connection and Curvature Forms]]**, where the vertical (pure-gauge) contribution is killed precisely because $\Omega$ vanishes on vertical vectors. The bridge is that equivariance upstairs is the reason the $[s_\alpha, F_\alpha]$ glue to a single global $F_\omega \in \Omega^2(M; \operatorname{ad}P)$.

- **The Yang–Mills field strength.** In chapter VII the object $F$ produced by part (d) is renamed the field strength and its norm integrated to form the Yang–Mills action; the definition **[[Def - The Yang-Mills Field Strength]]** is exactly $F = dA + \tfrac12[A \wedge A]$. The construction is to fix an $\operatorname{Ad}$-invariant inner product on $\mathfrak{g}$ and a metric on $M$; the structure equation supplies the field that is then varied to yield the equations of motion.

---

# Unlocked by This

> [!tip] Chern–Weil Theory *(from Algebraic Topology / Differential Geometry)*
> Because part (e) descends the curvature to $F_\omega \in \Omega^2(M; \operatorname{ad}P)$ and part (a) feeds the Bianchi identity, invariant polynomials in $F_\omega$ become closed forms with connection-independent cohomology classes — the [[Def - Chern Classes|characteristic classes]] of the bundle. See **[[Thm - Chern-Weil Theorem]]**.

> [!tip] Flat Connections and Monodromy *(from Gauge Theory V)*
> The structure equation shows $\Omega = 0$ is equivalent to the horizontal distribution being integrable, which by the Frobenius theorem produces horizontal foliations and, on a connected base, a **holonomy representation** of the fundamental group. This is the entry point to **[[Thm - Flat Connections and Monodromy Representations of the Fundamental Group]]**.
