---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Structure Equation for the Curvature"
  - "Def - Exterior Covariant Derivative on a Principal Bundle"
  - "Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms"
  - "Thm - Exterior Covariant Derivatives on P and on Associated Bundles Agree"
  - "Def - Curvature of a Principal Connection"
  - "Def - Connection on a Principal Bundle"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P \to M$ is a smooth principal $G$-bundle over a smooth manifold $M$, with $G$ a Lie group acting on the **right**, $R_g(p) = p \cdot g$. The Lie algebra is $\mathfrak{g} = T_e G$, with bracket $[\cdot,\cdot]$; for a matrix group this is the commutator, and $\operatorname{Ad}_g X = gXg^{-1}$. For $\xi \in \mathfrak{g}$ the [[Def - Fundamental Vector Field of a Group Action|fundamental vector field]] is $\xi_P(p) = \tfrac{d}{dt}\big|_{t=0}\, p \cdot \exp(t\xi)$; a tangent vector is **vertical** when it is tangent to a fibre, that is when it lies in $V_p = \ker d\pi_p = \{\xi_P(p) : \xi \in \mathfrak{g}\}$.

A **[[Def - Connection on a Principal Bundle|connection form]]** is a form $\omega \in \Omega^1(P; \mathfrak{g})$ with $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$ and $\omega(\xi_P) = \xi$ for all $\xi \in \mathfrak{g}$; the associated **horizontal subspace** is $H_p = \ker\omega_p$, and $\pi_H\colon T_pP \to H_p$ is the projection along the splitting $T_pP = H_p \oplus V_p$ (see [[Def - Horizontal Subspace and Horizontal Lift]]). A vector or vector field is **horizontal** when it lies in $H$; equivalently, when $\omega$ annihilates it. The **[[Def - Curvature of a Principal Connection|curvature form]]** is $\Omega \in \Omega^2(P; \mathfrak{g})$, defined by $\Omega(X,Y) = d\omega(\pi_H X, \pi_H Y)$; it is horizontal ($\Omega(X,Y) = 0$ as soon as $X$ or $Y$ is vertical) and $\operatorname{Ad}$-equivariant, $R_g^*\Omega = \operatorname{Ad}_{g^{-1}}\Omega$.

For $\mathfrak{g}$-valued forms $\alpha \in \Omega^p(P; \mathfrak{g})$ and $\beta \in \Omega^q(P; \mathfrak{g})$ we write $[\alpha \wedge \beta] \in \Omega^{p+q}(P; \mathfrak{g})$ for their **[[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|bracket]]**, fixed on decomposables by $[a\otimes\xi \wedge b\otimes\eta] = (a\wedge b)\otimes[\xi,\eta]$; for two $1$-forms $\eta,\varphi$ this gives
$$[\eta \wedge \varphi](X,Y) = [\eta(X),\varphi(Y)] - [\eta(Y),\varphi(X)], \qquad\text{so}\qquad [\omega \wedge \omega](X,Y) = 2[\omega(X),\omega(Y)].$$
The exterior derivative $d$ acts componentwise on $\mathfrak{g}$-valued forms after fixing a basis of $\mathfrak{g}$, so $d^2 = 0$ and the graded Leibniz rule hold as for scalar forms. A local section $s_\alpha\colon U_\alpha \to P$ produces the **[[Def - Local Connection Form and Gauge Potential|local connection form]]** $A_\alpha = s_\alpha^*\omega \in \Omega^1(U_\alpha; \mathfrak{g})$ and the **local curvature form** $F_\alpha = s_\alpha^*\Omega \in \Omega^2(U_\alpha; \mathfrak{g})$. The bundle $\operatorname{ad}P = P \times_{\operatorname{Ad}} \mathfrak{g}$ is the [[Def - Adjoint Bundles ad P and Ad P|adjoint bundle]]; the curvature descends to $F_\omega \in \Omega^2(M; \operatorname{ad}P)$, and $\nabla_\omega$ denotes the covariant derivative that $\omega$ [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|induces]] on $\operatorname{ad}P$, with exterior covariant derivative $d^{\nabla_\omega}$. The operator $D^\omega$ is the [[Def - Exterior Covariant Derivative on a Principal Bundle|exterior covariant derivative on the total space]], $D^\omega\alpha := (d\alpha)\circ\pi_H$, so that $(D^\omega\alpha)(X_1,\dots) = d\alpha(\pi_H X_1, \dots)$.

> [!warning] Convention: the factor of $\tfrac12$ and the matrix form
> This series uses the Lie-bracket normalisation $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ ([[Thm - Structure Equation for the Curvature|structure equation]]). For a matrix group, $[A \wedge A] = 2\,A \wedge A$ (the wedge here multiplies matrix entries), so the same object reads $\Omega = d\omega + \omega \wedge \omega$ with no $\tfrac12$; this is why Haydys writes the structure equation both ways. In the local Bianchi identity below, the matrix form of $[A_\alpha \wedge F_\alpha]$ is $A_\alpha \wedge F_\alpha - F_\alpha \wedge A_\alpha$, obtained from the graded identity $[\alpha \wedge \beta] = \alpha\wedge\beta - (-1)^{pq}\beta\wedge\alpha$ with $p=1$, $q=2$.

> [!warning] Convention: Haydys's notation $\hat{F}_A$
> Haydys writes $a$ for the connection form on $P$ and $\hat{F}_A := \pi^*F_A = dA + \tfrac12[A \wedge A]$ for the curvature pulled up to $P$, and states the Bianchi identity in the form (55): $d\hat{F}_A = [\hat{F}_A \wedge A]$. Under the identifications $\hat{F}_A = \Omega$ and $A = \omega$, this is exactly part (b) below, read as a statement on $P$. Haydys's proof of the local identity asserts the graded sign rule $[\vartheta,\eta] = -[\eta,\vartheta]$ (for $\vartheta$ a $2$-form and $\eta$ a $1$-form) and the Jacobi step $[A \wedge [A \wedge A]] = 0$ without deriving them; we supply both from [[Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms|the algebra of Lie-algebra-valued forms]].

---

# Statement

> **Theorem (Bianchi identity).** Let $\pi\colon P \to M$ be a principal $G$-bundle with connection form $\omega \in \Omega^1(P; \mathfrak{g})$, curvature form $\Omega \in \Omega^2(P; \mathfrak{g})$, and exterior covariant derivative $D^\omega$. Then:
>
> **(a)** $D^\omega\Omega = 0$; equivalently, $d\Omega(X_1, X_2, X_3) = 0$ whenever $X_1, X_2, X_3$ are horizontal tangent vectors.
>
> **(b)** On $P$, the curvature satisfies
> $$d\Omega = [\Omega \wedge \omega].$$
>
> **(c)** For every local section $s_\alpha\colon U_\alpha \to P$, with $A_\alpha = s_\alpha^*\omega$ and $F_\alpha = s_\alpha^*\Omega$,
> $$dF_\alpha + [A_\alpha \wedge F_\alpha] = 0;$$
> equivalently, the descended curvature $F_\omega \in \Omega^2(M; \operatorname{ad}P)$ is annihilated by the exterior covariant derivative of the induced connection on $\operatorname{ad}P$:
> $$d^{\nabla_\omega} F_\omega = 0.$$
>
> **(d)** If $G$ is abelian, then $\Omega = d\omega$, so $d\Omega = 0$; the local forms satisfy $F_\beta = F_\alpha$ on overlaps and glue to a single closed form $F \in \Omega^2(M; \mathfrak{g})$, $dF = 0$.

---

# Motivation

The curvature $\Omega$ of a connection is not an arbitrary $\mathfrak{g}$-valued $2$-form on $P$: it is *derived* from the connection $\omega$ through the [[Thm - Structure Equation for the Curvature|structure equation]] $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$. Whenever an object is built from another by applying $d$, the identity $d \circ d = 0$ leaves a fingerprint on it — a first-order differential identity that the derived object must obey no matter what the underlying data are. The Bianchi identity is precisely that fingerprint for curvature. It is the statement that curvature, though it can be any horizontal equivariant $2$-form pointwise, is constrained *differentially*: its exterior covariant derivative vanishes identically.

This constraint is what makes gauge theory work. Two of the most important constructions downstream depend on it directly. First, in [[Thm - Chern-Weil Theorem|Chern–Weil theory]] one feeds the curvature into an $\operatorname{Ad}$-invariant polynomial $p$ to build differential forms $p(F_\omega)$ on the base; these represent characteristic classes precisely because they are *closed*, and the proof that $d\,p(F_\omega) = 0$ is nothing but the Bianchi identity combined with the invariance of $p$. Without Bianchi there would be no characteristic classes and no topological invariants of bundles built from connections. Second, in [[Def - Yang-Mills Lagrangian and Action Functional|Yang–Mills theory]] the field equation obtained by varying the action is $d^A \star F = 0$; its silent companion, the identity $d^A F = 0$ that holds for *every* connection without any equation of motion, is the Bianchi identity. In the abelian case these two equations are exactly the two halves of Maxwell's equations — the inhomogeneous half from the action principle, and the homogeneous half ($dF = 0$: Faraday's law and the absence of magnetic monopoles) from Bianchi.

The mechanism can be named in one line, and the whole page is an unpacking of it: **the exterior derivative of a structure equation is a Jacobi identity.** Applying $d$ to $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ annihilates the $d\omega$ term (by $d^2 = 0$) and turns the bracket term, through the graded Leibniz and antisymmetry rules, into an expression whose obstruction to vanishing is exactly $[\omega \wedge [\omega \wedge \omega]]$ — and that vanishes by the Jacobi identity of $\mathfrak{g}$.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is mild — any connection on any principal bundle satisfies the identity — so the useful question is which problems secretly present a connection or a structure equation, so that Bianchi becomes available.

The first disguised source is **a linear connection on a vector bundle**. A connection $\nabla$ on a rank-$k$ vector bundle $E \to M$ has, in a local frame, a connection matrix $A \in \Omega^1(U; \mathfrak{gl}_k)$ and curvature $F_\nabla = dA + A \wedge A$ ([[Thm - Local Formula for the Curvature of a Connection|local curvature formula]]). This is the $G = GL_k$ case of the present theorem: $\nabla$ corresponds to a connection on the [[Def - Frame Bundle of a Vector Bundle|frame bundle]] $\operatorname{Fr}(E)$, and the Bianchi identity descends to $d^\nabla F_\nabla = 0$, the differential Bianchi identity for $E$. The non-obvious bridge is that a connection presented purely in linear-algebra terms, with no bundle group in sight, already carries the full principal-bundle identity. *Example problem:* show that the endomorphism-valued $2$-form $F_\nabla$ of any linear connection satisfies $d^\nabla F_\nabla = 0$, and read off the second Bianchi identity of Riemannian geometry as the special case of the Levi-Civita connection.

The second disguised source is **a $\mathfrak{g}$-valued $1$-form together with its "field strength", even off a bundle**. Given any $A \in \Omega^1(U; \mathfrak{g})$ on an open set, form $F := dA + \tfrac12[A \wedge A]$. Purely algebraically — with no connection axioms used at all — one has $dF + [A \wedge F] = 0$, because the computation in part (c) below uses only the graded bracket identities. So the moment a problem writes down a potential $A$ and its curvature $F$, the Bianchi identity is present as an algebraic fact. The non-obvious point is that the identity is *not* a consequence of the equivariance or verticality axioms of a connection; those axioms are what let it descend to the base, but the identity itself is algebra. *Example problem:* verify $dF + [A \wedge F] = 0$ for a pure-gauge potential $A = g^{-1}dg$ (where $F = 0$) and confirm consistency.

The third disguised source is **a flat connection, or more generally the Maurer–Cartan setting**. The [[Thm - The Maurer-Cartan Equation|Maurer–Cartan equation]] $d\theta + \tfrac12[\theta \wedge \theta] = 0$ says the Maurer–Cartan form $\theta$ has zero curvature; a [[Def - Flat Connection|flat connection]] is one with $\Omega = 0$. For such data the Bianchi identity is vacuous as a constraint on $\Omega$, but the *same* algebraic engine — $d$ applied to a structure equation, killed by Jacobi — is what proves the Maurer–Cartan equation is consistent and what governs the integrability of flat connections. The non-obvious bridge is recognising a "zero curvature condition" as a specialisation of the structure equation, so that Bianchi's algebra is what one differentiates against. *Example problem:* differentiate the flatness condition $F = dA + \tfrac12[A \wedge A] = 0$ and confirm that the result is automatically satisfied, i.e. flatness imposes no further differential constraint beyond itself.

**Targets (Output Amplification)**

The bare conclusion $d^{\nabla_\omega}F_\omega = 0$ is a single differential identity. Combined with other ingredients it produces the central theorems of the subject.

Combine Bianchi with **an $\operatorname{Ad}$-invariant polynomial $p$ on $\mathfrak{g}$**. Invariance gives an infinitesimal identity $\sum_j p(X_1, \dots, [\xi, X_j], \dots, X_k) = 0$; feeding curvature into $p$ and differentiating, every term of $d\,p(F_\omega)$ is of the form $p(F_\omega, \dots, d^{\nabla_\omega}F_\omega, \dots, F_\omega)$, which vanishes by Bianchi. The payoff $E$ is that $p(F_\omega)$ is a closed form, hence defines a de Rham class independent of the connection — this is the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]] and the origin of all characteristic classes.

Combine Bianchi with **the Yang–Mills equation and the Hodge star**. The variational equation $d^{\nabla_\omega}\star F_\omega = 0$ is the "dynamical" half; Bianchi $d^{\nabla_\omega}F_\omega = 0$ is the "kinematic" half that holds for free. Together they say that for a [[Def - Self-Dual and Anti-Self-Dual Connections|(anti-)self-dual connection]] $\star F_\omega = \pm F_\omega$, the Yang–Mills equation is automatic: applying $d^{\nabla_\omega}$ to $\star F_\omega = \pm F_\omega$ and using Bianchi gives $d^{\nabla_\omega}\star F_\omega = \pm d^{\nabla_\omega}F_\omega = 0$. The payoff is [[Thm - Self-Dual Connections are Yang-Mills|instantons are Yang–Mills]], the entry point to Donaldson theory.

Combine Bianchi with **the abelian case and integration over cycles**. For $G = U(1)$ the identity reads $dF = 0$ with $F \in \Omega^2(M; i\mathbb{R})$, so $F$ is a closed $2$-form; by Stokes its periods over $2$-cycles are homotopy invariants of the bundle. The payoff is the [[Thm - First Chern Class of a Line Bundle from Curvature|first Chern class]] $c_1 = [\tfrac{i}{2\pi}F]$ and, on a closed surface, an integer-valued degree — the electromagnetic flux quantisation and the classification of line bundles by curvature.

---

# Why Is It True

Set the formulas aside and look at the two pictures the proof lives in.

The first picture is Bär's, and it is the shortest. Curvature is *born horizontal*: $\Omega(X,Y) = d\omega(\pi_H X, \pi_H Y)$ only ever sees the horizontal parts of its arguments, and it vanishes the instant one of them is vertical. Now ask what happens when we exterior-differentiate. Using the structure equation, $d\Omega = \tfrac12 d[\omega \wedge \omega]$, because the $d\omega$ term dies under a second $d$. The form $\eta = [\omega \wedge \omega]$ is even more sharply horizontal than $\Omega$: since $\eta(X,Y) = 2[\omega(X), \omega(Y)]$, it vanishes as soon as *either* argument is horizontal, because $\omega$ annihilates horizontal vectors. The invariant formula for the exterior derivative writes $d\eta$ on a triple of vector fields as a sum of directional derivatives of $\eta$ evaluated on pairs, plus $\eta$ evaluated on brackets. On a triple of horizontal fields, every one of those evaluations feeds $\eta$ at least one horizontal argument, so every term is zero. Thus $d\Omega$ vanishes on horizontal triples, which is exactly $D^\omega\Omega = 0$.

> **The curvature is a horizontal form, and horizontality is preserved under the exterior covariant derivative — because $d$ of a form that vanishes whenever one argument is horizontal again vanishes on horizontal triples, once the $d\omega$ term has been removed by $d^2 = 0$.**

The second picture is Haydys's, and it explains *why the bracket term $[\omega \wedge \Omega]$ appears* rather than a bare $d\Omega = 0$. Differentiate the structure equation as pure algebra of $\mathfrak{g}$-valued forms. The term $d(d\omega) = 0$. The term $\tfrac12 d[\omega \wedge \omega]$ opens by the graded Leibniz rule into two copies of $[d\omega \wedge \omega]$, giving $d\Omega = [d\omega \wedge \omega]$. Substituting $d\omega = \Omega - \tfrac12[\omega \wedge \omega]$ turns this into $[\Omega \wedge \omega]$ plus a leftover triple bracket $-\tfrac12[[\omega \wedge \omega] \wedge \omega]$ — and this leftover is precisely $[\omega \wedge [\omega \wedge \omega]]$ up to sign, which the Jacobi identity of $\mathfrak{g}$ sends to zero. The Jacobi identity is where the non-abelianness of $G$ lives, and it is exactly what has to hold for the structure equation to be differentiable into a clean identity. When $G$ is abelian all brackets vanish, so the triple bracket is zero because each of its Lie brackets is, and $d\Omega = 0$ on the nose. The two pictures agree because the tensorial formula for $D^\omega$ reads $D^\omega\Omega = d\Omega + [\omega \wedge \Omega]$, and part (b)'s $d\Omega = [\Omega \wedge \omega] = -[\omega \wedge \Omega]$ makes this vanish — Bär's horizontal statement (a) and Haydys's algebraic statement (b) are two faces of the same fact.

---

# What Makes This Hard

The single most common error is to believe the identity says $d\Omega = 0$. It does not: on $P$ one has $d\Omega = [\Omega \wedge \omega]$, and $d\Omega$ vanishes only on *horizontal* triples, or after passing to the exterior *covariant* derivative $D^\omega$ or $d^{\nabla_\omega}$. The bare $d\Omega = 0$ holds only in the abelian case. The second difficulty is entirely a matter of graded sign bookkeeping: the bracket $[\cdot \wedge \cdot]$ of $\mathfrak{g}$-valued forms is *graded*-antisymmetric, $[\alpha \wedge \beta] = -(-1)^{pq}[\beta \wedge \alpha]$, so $[\omega \wedge \omega] \neq 0$ for a $1$-form $\omega$ (it equals $2[\omega(X),\omega(Y)]$ on arguments), and the signs in the Leibniz and Jacobi rules must be tracked exactly or the cancellation fails. The third subtlety is conceptual: the local identity $dF_\alpha + [A_\alpha \wedge F_\alpha] = 0$ is pure algebra of forms, true for any $A_\alpha$ whatsoever, whereas its interpretation as $d^{\nabla_\omega}F_\omega = 0$ on the base requires the connection axioms so that the pieces glue into a global object — separating the algebra from the geometry is where care is needed.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Differentiate the structure equation $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$. The $d\omega$ term dies by $d^2 = 0$, leaving $d\Omega = \tfrac12 d[\omega \wedge \omega]$. Prove the horizontal statement (a) directly, by observing that $[\omega \wedge \omega]$ vanishes whenever an argument is horizontal and feeding this into the invariant formula for $d$ of a $2$-form. Prove the algebraic statement (b) by expanding $\tfrac12 d[\omega \wedge \omega]$ with the graded Leibniz rule and reducing the leftover triple bracket by Jacobi. Get (c) by pulling back along a local section, or by transcribing the same algebra with $A_\alpha$ in place of $\omega$. Get (d) by setting all brackets to zero.

**Subgoal decomposition:**

1. **Invariant formula for $d$ of a $2$-form.** Establish that for $\eta \in \Omega^2(P; \mathfrak{g})$ and vector fields $X_1, X_2, X_3$,
   $$d\eta(X_1,X_2,X_3) = X_1\,\eta(X_2,X_3) - X_2\,\eta(X_1,X_3) + X_3\,\eta(X_1,X_2) - \eta([X_1,X_2],X_3) + \eta([X_1,X_3],X_2) - \eta([X_2,X_3],X_1).$$
   - *Hint:* Both sides are tensorial (function-linear) in each $X_i$; check the identity on coordinate fields, where all brackets vanish, against the coordinate expression of $d$.
   - *Why needed:* It is the tool that turns "$\eta$ vanishes on horizontal arguments" into "$d\eta$ vanishes on horizontal triples" for part (a).

2. **Horizontal vanishing of $[\omega \wedge \omega]$ and its derivative.** Show $\eta := [\omega \wedge \omega]$ vanishes whenever one argument is horizontal, and that $d\eta$ vanishes on every triple of horizontal vectors.
   - *Hint:* $\eta(X,Y) = 2[\omega(X),\omega(Y)]$ and $\omega$ kills horizontal vectors; apply subgoal 1 to horizontal extensions.
   - *Why needed:* This is part (a) once combined with $d\Omega = \tfrac12 d\eta$.

3. **Graded reduction of $d[\omega \wedge \omega]$.** Show $d[\omega \wedge \omega] = 2[d\omega \wedge \omega]$ and $[[\omega \wedge \omega] \wedge \omega] = 0$.
   - *Hint:* Graded Leibniz plus graded antisymmetry for the first; graded Jacobi ($[\omega \wedge [\omega \wedge \omega]] = 0$) plus antisymmetry for the second.
   - *Why needed:* These are the two algebraic facts that produce part (b) from the structure equation.

4. **Assemble (b), then (c), then (d).** Combine subgoals into $d\Omega = [\Omega \wedge \omega]$; pull back / re-run for the local identity; specialise to abelian $G$.
   - *Hint:* For (c) substitute $A_\alpha, F_\alpha$ for $\omega, \Omega$ and use $F_\alpha = dA_\alpha + \tfrac12[A_\alpha \wedge A_\alpha]$; identify the result with $d^{\nabla_\omega}F_\omega$ via the agreement of $D^\omega$ and $d^{\nabla_\omega}$.
   - *Why needed:* Delivers the four stated forms of the identity.

---

# Lemma Decomposition

> [!note]- Lemma 1: Invariant formula for the exterior derivative of a 2-form
> **Statement:** Let $\eta \in \Omega^2(P; \mathfrak{g})$ and let $X_1, X_2, X_3$ be smooth vector fields on $P$. Then
> $$d\eta(X_1,X_2,X_3) = X_1\,\eta(X_2,X_3) - X_2\,\eta(X_1,X_3) + X_3\,\eta(X_1,X_2) - \eta([X_1,X_2],X_3) + \eta([X_1,X_3],X_2) - \eta([X_2,X_3],X_1),$$
> where $X_i\,\eta(X_j,X_k)$ denotes the directional derivative of the $\mathfrak{g}$-valued function $\eta(X_j,X_k)$ along $X_i$.
>
> **Hint:** Both sides are alternating and $C^\infty(P)$-linear in each $X_i$, hence tensorial; evaluate on coordinate vector fields, where the brackets drop out, and match the coordinate expression of $d$.
>
> **Why needed:** It converts the horizontal-vanishing of $[\omega \wedge \omega]$ into the horizontal-vanishing of its exterior derivative, which is part (a).
>
> > [!note]- Full proof
> > Because $d$, evaluation, and the Lie bracket of fields all act componentwise on $\mathfrak{g}$-valued forms once a basis $(e_a)$ of $\mathfrak{g}$ is fixed (writing $\eta = \sum_a \eta^a e_a$ with $\eta^a$ scalar $2$-forms), it suffices to prove the identity for a scalar $2$-form $\eta$; the $\mathfrak{g}$-valued case follows by summing $e_a$ times the scalar identity for $\eta^a$. Denote the right-hand side by $R(X_1,X_2,X_3)$.
> >
> > **Step 1 — $R$ is alternating.** Interchanging $X_1$ and $X_2$ sends the derivative part $X_1\eta(X_2,X_3) - X_2\eta(X_1,X_3) + X_3\eta(X_1,X_2)$ to $X_2\eta(X_1,X_3) - X_1\eta(X_2,X_3) + X_3\eta(X_2,X_1)$, which is its negative (using $\eta(X_2,X_1) = -\eta(X_1,X_2)$), and sends the bracket part to its negative by the same antisymmetry of $\eta$ together with $[X_2,X_1] = -[X_1,X_2]$. The transpositions $(X_1 X_3)$ and $(X_2 X_3)$ are handled identically. Hence $R$ is alternating in its three arguments.
> >
> > **Step 2 — $R$ is $C^\infty(P)$-linear in $X_1$.** Fix $f \in C^\infty(P)$ and replace $X_1$ by $fX_1$. In the derivative terms,
> > $$(fX_1)\,\eta(X_2,X_3) = f\,X_1\eta(X_2,X_3), \qquad X_2\,\eta(fX_1,X_3) = X_2\big(f\,\eta(X_1,X_3)\big) = (X_2 f)\,\eta(X_1,X_3) + f\,X_2\eta(X_1,X_3),$$
> > and likewise $X_3\,\eta(fX_1,X_2) = (X_3 f)\,\eta(X_1,X_2) + f\,X_3\eta(X_1,X_2)$ (by the Leibniz rule for directional derivatives and $C^\infty$-bilinearity of $\eta$). In the bracket terms, the Leibniz identity for the Lie bracket, $[fX_1, X_j] = f[X_1,X_j] - (X_j f)X_1$, gives
> > $$-\eta([fX_1,X_2],X_3) = -f\,\eta([X_1,X_2],X_3) + (X_2 f)\,\eta(X_1,X_3), \qquad \eta([fX_1,X_3],X_2) = f\,\eta([X_1,X_3],X_2) - (X_3 f)\,\eta(X_1,X_2),$$
> > while the term $-\eta([X_2,X_3],fX_1) = -f\,\eta([X_2,X_3],X_1)$ is already homogeneous. Adding all six, the undifferentiated-$f$ contributions reproduce $f\,R(X_1,X_2,X_3)$, and the four terms carrying $X_2 f$ and $X_3 f$ cancel in the two pairs
> > $$\big[-(X_2 f)\eta(X_1,X_3)\big] + \big[+(X_2 f)\eta(X_1,X_3)\big] = 0, \qquad \big[+(X_3 f)\eta(X_1,X_2)\big] + \big[-(X_3 f)\eta(X_1,X_2)\big] = 0.$$
> > Hence $R(fX_1,X_2,X_3) = f\,R(X_1,X_2,X_3)$. By Step 1, linearity in $X_1$ propagates to each argument, so $R$ is $C^\infty(P)$-multilinear.
> >
> > **Step 3 — reduce to coordinates and match.** The left-hand side $d\eta$ is a genuine $3$-form, hence $C^\infty(P)$-multilinear and alternating; by Steps 1–2 so is $R$. Two tensors that agree on a local frame agree everywhere, so it suffices to evaluate both on coordinate vector fields $\partial_a, \partial_b, \partial_c$ of a chart, for which $[\partial_a, \partial_b] = 0$. All three bracket terms of $R$ then vanish, leaving
> > $$R(\partial_a, \partial_b, \partial_c) = \partial_a\,\eta_{bc} - \partial_b\,\eta_{ac} + \partial_c\,\eta_{ab}, \qquad \eta_{ij} := \eta(\partial_i, \partial_j).$$
> > Writing $\eta = \sum_{i<j}\eta_{ij}\,dx^i \wedge dx^j$, the [[Thm - Coordinate Expression for the Exterior Derivative|coordinate expression of the exterior derivative]] gives $d\eta = \sum_{i<j}\sum_k \partial_k \eta_{ij}\,dx^k \wedge dx^i \wedge dx^j$, and evaluating on $(\partial_a,\partial_b,\partial_c)$ with $a<b<c$ yields exactly $\partial_a\eta_{bc} - \partial_b\eta_{ac} + \partial_c\eta_{ab}$. Thus $d\eta(\partial_a,\partial_b,\partial_c) = R(\partial_a,\partial_b,\partial_c)$ on coordinate fields, and by multilinearity $d\eta = R$ everywhere. $\blacksquare$

> [!note]- Lemma 2: The form $[\omega \wedge \omega]$ and its derivative vanish on horizontal arguments
> **Statement:** Let $\omega$ be a connection form and set $\eta := [\omega \wedge \omega] \in \Omega^2(P; \mathfrak{g})$. Then (i) $\eta(X,Y) = 0$ whenever $X$ or $Y$ is a horizontal vector, and (ii) $d\eta(X_1,X_2,X_3) = 0$ whenever $X_1, X_2, X_3$ are all horizontal.
>
> **Hint:** For (i), $\eta(X,Y) = 2[\omega(X),\omega(Y)]$ and $\omega$ annihilates horizontal vectors ($H = \ker\omega$). For (ii), extend to horizontal vector fields and apply Lemma 1: every term feeds $\eta$ a horizontal argument.
>
> **Why needed:** Together with $d\Omega = \tfrac12 d\eta$ (from the structure equation and $d^2 = 0$) this is part (a).
>
> > [!note]- Full proof
> > **(i)** By the bracket convention for $\mathfrak{g}$-valued $1$-forms, $\eta(X,Y) = [\omega \wedge \omega](X,Y) = [\omega(X),\omega(Y)] - [\omega(Y),\omega(X)] = 2[\omega(X),\omega(Y)]$ (the two summands are equal by antisymmetry of the Lie bracket). If $X$ is horizontal then $X \in H_p = \ker\omega_p$, so $\omega(X) = 0$ and hence $[\omega(X),\omega(Y)] = 0$; the same holds if $Y$ is horizontal. Therefore $\eta(X,Y) = 0$ whenever either argument is horizontal.
> >
> > **(ii)** Let $v_1, v_2, v_3 \in H_p$ be horizontal tangent vectors at a point $p$. Since $d\eta$ is a $3$-form, its value $d\eta(v_1,v_2,v_3)$ depends only on the tangent vectors, not on any extension; choose horizontal vector-field extensions $X_1, X_2, X_3$ (for instance the [[Def - Horizontal Subspace and Horizontal Lift|horizontal lifts]] of extensions of $d\pi(v_i)$, which are horizontal at every point). By Lemma 1,
> > $$d\eta(X_1,X_2,X_3) = X_1\,\eta(X_2,X_3) - X_2\,\eta(X_1,X_3) + X_3\,\eta(X_1,X_2) - \eta([X_1,X_2],X_3) + \eta([X_1,X_3],X_2) - \eta([X_2,X_3],X_1).$$
> > In each of the three derivative terms, the argument pair of $\eta$ consists of two horizontal fields, so by (i) the function $\eta(X_j,X_k)$ is identically zero on $P$, whence its directional derivative $X_i\,\eta(X_j,X_k)$ is zero (the derivative of the zero function). In each of the three bracket terms, the *second* slot of $\eta$ is one of the horizontal fields $X_1, X_2, X_3$, so by (i) the term vanishes regardless of whether the bracket $[X_i,X_j]$ is horizontal. All six terms are zero, so $d\eta(v_1,v_2,v_3) = d\eta(X_1,X_2,X_3) = 0$. $\blacksquare$

> [!note]- Lemma 3: Graded reduction of $d[\beta \wedge \beta]$ for a $\mathfrak{g}$-valued $1$-form
> **Statement:** Let $\beta$ be any $\mathfrak{g}$-valued $1$-form, on the total space $P$ or on an open subset $U \subseteq M$. Then $d[\beta \wedge \beta] = 2[d\beta \wedge \beta]$ and $[[\beta \wedge \beta] \wedge \beta] = 0$. In particular both identities hold for the connection form $\omega$ on $P$ and for a local connection form $A_\alpha = s_\alpha^*\omega$ on $U_\alpha$, since the proof uses only the graded algebra of $\mathfrak{g}$-valued forms and no property special to a connection.
>
> **Hint:** Apply the graded Leibniz rule then graded antisymmetry for the first identity; for the second use the graded Jacobi identity $[\beta \wedge [\beta \wedge \beta]] = 0$ (valid for every $\mathfrak{g}$-valued $1$-form) and one graded antisymmetry.
>
> **Why needed:** These are the two algebraic inputs that turn the differentiated structure equation into part (b) and clear the leftover triple bracket; the same two identities, applied to $A_\alpha$, drive the local computation in part (c).
>
> > [!note]- Full proof
> > We use the identities proved on [[Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms|the algebra of Lie-algebra-valued forms]], which are established there for arbitrary $\mathfrak{g}$-valued forms $\mu \in \Omega^p$, $\nu \in \Omega^q$ (all $\mathfrak{g}$-valued):
> > $$[\mu \wedge \nu] = -(-1)^{pq}[\nu \wedge \mu] \quad\text{(graded antisymmetry)}, \qquad d[\mu \wedge \nu] = [d\mu \wedge \nu] + (-1)^p[\mu \wedge d\nu] \quad\text{(graded Leibniz)},$$
> > and, for any $\mathfrak{g}$-valued $1$-form $\beta$, the graded Jacobi consequence $[\beta \wedge [\beta \wedge \beta]] = 0$. Since none of these three inputs uses any property of $\beta$ beyond its being a $\mathfrak{g}$-valued $1$-form, the conclusions below hold verbatim for $\omega$ and for $A_\alpha$.
> >
> > **First identity.** Applying the graded Leibniz rule with $\mu = \nu = \beta$, so $p = 1$,
> > $$d[\beta \wedge \beta] = [d\beta \wedge \beta] + (-1)^1[\beta \wedge d\beta] = [d\beta \wedge \beta] - [\beta \wedge d\beta] \qquad\text{(graded Leibniz, } p = 1\text{).}$$
> > Now $[\beta \wedge d\beta]$ has $\beta$ of degree $1$ and $d\beta$ of degree $2$; graded antisymmetry with $p = 1$, $q = 2$ gives
> > $$[\beta \wedge d\beta] = -(-1)^{1\cdot 2}[d\beta \wedge \beta] = -[d\beta \wedge \beta] \qquad\text{(graded antisymmetry, } (-1)^{2} = 1\text{).}$$
> > Substituting, $d[\beta \wedge \beta] = [d\beta \wedge \beta] - (-[d\beta \wedge \beta]) = 2[d\beta \wedge \beta]$.
> >
> > **Second identity.** In $[[\beta \wedge \beta] \wedge \beta]$ the first factor $[\beta \wedge \beta]$ has degree $2$ and the second factor $\beta$ has degree $1$; graded antisymmetry with $p = 2$, $q = 1$ gives
> > $$[[\beta \wedge \beta] \wedge \beta] = -(-1)^{2\cdot 1}[\beta \wedge [\beta \wedge \beta]] = -[\beta \wedge [\beta \wedge \beta]] \qquad\text{(graded antisymmetry, } (-1)^{2} = 1\text{).}$$
> > By the graded Jacobi consequence for a $1$-form, $[\beta \wedge [\beta \wedge \beta]] = 0$, hence $[[\beta \wedge \beta] \wedge \beta] = 0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\pi\colon P \to M$ be a principal $G$-bundle with connection form $\omega$ and curvature $\Omega$.
>
> **Step 0 — the differentiated structure equation.** By the [[Thm - Structure Equation for the Curvature|structure equation]], $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$. Applying $d$ and using $d(d\omega) = 0$ ([[Thm - d-Squared-is-Zero|d ∘ d = 0]], componentwise on $\mathfrak{g}$-valued forms),
> $$d\Omega = d(d\omega) + \tfrac12\,d[\omega \wedge \omega] = \tfrac12\,d[\omega \wedge \omega]. \tag{$\ast$}$$
> This single equation feeds all four parts.
>
> **Part (a) — $D^\omega\Omega = 0$.** By definition of the [[Def - Exterior Covariant Derivative on a Principal Bundle|exterior covariant derivative on the total space]], $(D^\omega\Omega)(X_1,X_2,X_3) = d\Omega(\pi_H X_1, \pi_H X_2, \pi_H X_3)$, so $D^\omega\Omega = 0$ is equivalent to the vanishing of $d\Omega$ on every triple of horizontal vectors. Let $X_1, X_2, X_3$ be horizontal. By $(\ast)$, $d\Omega(X_1,X_2,X_3) = \tfrac12\,d[\omega \wedge \omega](X_1,X_2,X_3)$, and by Lemma 2(ii) the right-hand side is $0$. Hence $d\Omega$ vanishes on horizontal triples, i.e. $D^\omega\Omega = 0$.
>
> **Part (b) — $d\Omega = [\Omega \wedge \omega]$ on $P$.** Starting from $(\ast)$ and applying the first identity of Lemma 3,
> $$d\Omega = \tfrac12\,d[\omega \wedge \omega] = \tfrac12 \cdot 2[d\omega \wedge \omega] = [d\omega \wedge \omega] \qquad\text{(Lemma 3, first identity).}$$
> Substitute $d\omega = \Omega - \tfrac12[\omega \wedge \omega]$ (the structure equation, rearranged) into this. By $\mathbb{R}$-bilinearity of the bracket of $\mathfrak{g}$-valued forms,
> $$d\Omega = \big[\big(\Omega - \tfrac12[\omega \wedge \omega]\big) \wedge \omega\big] = [\Omega \wedge \omega] - \tfrac12[[\omega \wedge \omega] \wedge \omega] \qquad\text{(bilinearity of } [\cdot \wedge \cdot]\text{).}$$
> The second term vanishes by the second identity of Lemma 3, $[[\omega \wedge \omega] \wedge \omega] = 0$. Therefore $d\Omega = [\Omega \wedge \omega]$.
>
> *Consistency with (a).* The tensorial formula for $D^\omega$ on the $\operatorname{Ad}$-type form $\Omega$ reads $D^\omega\Omega = d\Omega + [\omega \wedge \Omega]$ (proved on [[Def - Exterior Covariant Derivative on a Principal Bundle|the exterior covariant derivative page]]). By graded antisymmetry, $[\Omega \wedge \omega] = -(-1)^{2\cdot 1}[\omega \wedge \Omega] = -[\omega \wedge \Omega]$, so part (b) gives $D^\omega\Omega = [\Omega \wedge \omega] + [\omega \wedge \Omega] = 0$, recovering part (a). The two statements are the horizontal face and the algebraic face of one identity.
>
> **Part (c) — the local identity $dF_\alpha + [A_\alpha \wedge F_\alpha] = 0$.** Fix a local section $s_\alpha\colon U_\alpha \to P$ and set $A_\alpha = s_\alpha^*\omega$, $F_\alpha = s_\alpha^*\Omega$. Pulling the structure equation back along $s_\alpha$ and using that pull-back commutes with $d$ and with the bracket (both act componentwise) gives $F_\alpha = dA_\alpha + \tfrac12[A_\alpha \wedge A_\alpha]$ ([[Thm - Structure Equation for the Curvature|local structure equation]]). We now compute the local exterior covariant derivative of $F_\alpha$ directly:
> $$dF_\alpha + [A_\alpha \wedge F_\alpha] = d\Big(dA_\alpha + \tfrac12[A_\alpha \wedge A_\alpha]\Big) + \Big[A_\alpha \wedge \big(dA_\alpha + \tfrac12[A_\alpha \wedge A_\alpha]\big)\Big] \qquad\text{(substituting } F_\alpha\text{).}$$
> Expand each piece. First, $d\big(dA_\alpha + \tfrac12[A_\alpha \wedge A_\alpha]\big) = \tfrac12\,d[A_\alpha \wedge A_\alpha] = [dA_\alpha \wedge A_\alpha]$, using $d(dA_\alpha) = 0$ and Lemma 3's first identity applied to the $1$-form $A_\alpha$. Second, by bilinearity of the bracket,
> $$\big[A_\alpha \wedge (dA_\alpha + \tfrac12[A_\alpha \wedge A_\alpha])\big] = [A_\alpha \wedge dA_\alpha] + \tfrac12[A_\alpha \wedge [A_\alpha \wedge A_\alpha]] \qquad\text{(bilinearity).}$$
> The last term $\tfrac12[A_\alpha \wedge [A_\alpha \wedge A_\alpha]]$ vanishes by the graded Jacobi consequence for the $1$-form $A_\alpha$ ([[Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms|graded Jacobi]]). Collecting the two surviving terms,
> $$dF_\alpha + [A_\alpha \wedge F_\alpha] = [dA_\alpha \wedge A_\alpha] + [A_\alpha \wedge dA_\alpha].$$
> By graded antisymmetry with $p = 2$ (for $dA_\alpha$) and $q = 1$ (for $A_\alpha$), $[dA_\alpha \wedge A_\alpha] = -(-1)^{2}[A_\alpha \wedge dA_\alpha] = -[A_\alpha \wedge dA_\alpha]$, so the two terms cancel:
> $$dF_\alpha + [A_\alpha \wedge F_\alpha] = -[A_\alpha \wedge dA_\alpha] + [A_\alpha \wedge dA_\alpha] = 0.$$
> This proves the local identity. (Haydys's Proposition 53 records exactly this computation but leaves the graded sign rule and the Jacobi step as assertions; Lemma 3 and the graded-Jacobi theorem supply both.)
>
> **From local to global.** The local $2$-forms $[s_\alpha, F_\alpha]$ glue, by the [[Thm - Transformation of Local Connection and Curvature Forms|transformation law]] $F_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}F_\alpha$, into the single descended curvature $F_\omega \in \Omega^2(M; \operatorname{ad}P)$. The connection $\omega$ [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|induces]] the covariant derivative $\nabla_\omega$ on $\operatorname{ad}P = P \times_{\operatorname{Ad}}\mathfrak{g}$, whose exterior covariant derivative is, in the local trivialisation given by $s_\alpha$, the operator $d + [A_\alpha \wedge \,\cdot\,]$ (this is the statement of [[Thm - Exterior Covariant Derivatives on P and on Associated Bundles Agree|the agreement of the two exterior covariant derivatives]], specialised to the adjoint representation, whose differential is $\operatorname{ad}$ and for which $\operatorname{ad}(A_\alpha) \wedge F_\alpha = [A_\alpha \wedge F_\alpha]$). Hence the local expression of $d^{\nabla_\omega}F_\omega$ on $U_\alpha$ is $dF_\alpha + [A_\alpha \wedge F_\alpha]$, which we have just shown is $0$. As this holds on every $U_\alpha$ of a cover, $d^{\nabla_\omega}F_\omega = 0$ globally. The same theorem identifies $D^\omega\Omega$ with $\pi^*(d^{\nabla_\omega}F_\omega)$, so parts (a) and (c) are the upstairs and downstairs versions of one statement.
>
> **Part (d) — the abelian case.** Suppose $G$ is abelian. Then $\mathfrak{g}$ is abelian, so every Lie bracket $[\xi,\eta]$ vanishes, and hence $[\omega \wedge \omega] = 0$ (its value $2[\omega(X),\omega(Y)]$ is identically zero). The structure equation collapses to $\Omega = d\omega$, and therefore $d\Omega = d(d\omega) = 0$ by $d^2 = 0$ — no horizontal restriction is needed. Locally $F_\alpha = dA_\alpha$, and the transformation law degenerates ($\operatorname{Ad}$ is trivial) to $F_\beta = F_\alpha$ on every overlap, so the $F_\alpha$ are the restrictions of one global form $F \in \Omega^2(M; \mathfrak{g})$ with $F|_{U_\alpha} = dA_\alpha$; then $dF|_{U_\alpha} = d(dA_\alpha) = 0$ on each chart, hence $dF = 0$. The abelian curvature is a closed $\mathfrak{g}$-valued $2$-form on the base.
>
> Combining Parts (a)–(d), the Bianchi identity holds in all four stated forms. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The second Bianchi identity of Riemannian geometry.** Take $E = TM$ with the Levi-Civita connection, whose frame bundle is the orthonormal frame bundle with structure group $O(n)$. The principal Bianchi identity $d^{\nabla_\omega}F_\omega = 0$ becomes, in a coordinate frame, the classical second Bianchi identity $\nabla_a R_{bcde} + \nabla_b R_{cade} + \nabla_c R_{abde} = 0$ for the Riemann tensor. The application is non-obvious because the Riemannian identity is usually derived by brute-force manipulation of Christoffel symbols, whereas here it is a one-line corollary of $d$ applied to a structure equation; the exercise is to translate the coordinate-free $d^{\nabla}F = 0$ into the index form and confirm the two agree.

**Homogeneous Maxwell equations from a $U(1)$ connection.** Model electromagnetism as a connection on a principal $U(1)$-bundle, with curvature the field strength $F \in \Omega^2(M; i\mathbb{R})$. Part (d) gives $dF = 0$ with no equation of motion invoked, and in components on Minkowski space this is precisely $\partial_{[\mu}F_{\nu\rho]} = 0$, that is Faraday's law of induction together with the statement that there are no magnetic monopoles. The application is instructive because it shows that half of Maxwell's equations are not dynamical laws at all but a geometric identity forced by the existence of a potential $A$ with $F = dA$; the exercise is to extract the two vector-calculus equations from $dF = 0$.

**Instantons solve Yang–Mills for free.** On a closed oriented Riemannian $4$-manifold, a connection with $\star F_\omega = \pm F_\omega$ is (anti-)self-dual. Applying $d^{\nabla_\omega}$ to this equation and using Bianchi $d^{\nabla_\omega}F_\omega = 0$ yields $d^{\nabla_\omega}\star F_\omega = 0$, the Yang–Mills equation. The application is non-obvious because it means one never has to solve the second-order Yang–Mills equation directly for instantons — the first-order (anti-)self-duality condition plus the identity on this page does it — and this is the observation on which the entire theory of the [[Thm - Donaldson Diagonalisation Theorem|Donaldson invariants]] is built. The exercise is to carry out the two-line deduction and identify precisely where Bianchi is used.

---

# Bridges

- **Chern–Weil closedness.** For an $\operatorname{Ad}$-invariant polynomial $p$ of degree $k$, differentiate the base form $p(F_\omega, \dots, F_\omega)$. The Leibniz rule spreads $d$ over the $k$ slots, each term becoming $p(F_\omega, \dots, d^{\nabla_\omega}F_\omega, \dots, F_\omega)$ with one slot differentiated; every such term is zero by the Bianchi identity of this page, so $d\,p(F_\omega) = 0$. This is the closedness half of the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]]; the invariance of $p$ is what lets the mixed connection-form contributions cancel, and Bianchi is what kills the curvature-derivative contributions.

- **The exterior covariant derivative squares to curvature, not zero.** On an associated bundle, $d^{\nabla_\omega} \circ d^{\nabla_\omega} = [F_\omega \wedge \,\cdot\,]$ (or $\rho_*(F_\omega)\wedge$ in a general representation), which is *not* zero for a curved connection. The Bianchi identity is the statement that this same operator, applied to $F_\omega$ itself, does give zero — the curvature is in the "kernel" of its own iterated covariant derivative. This is the exact analogue, one degree up, of the vector-bundle identity in [[Def - Exterior Covariant Derivative on a Vector Bundle|the exterior covariant derivative on a vector bundle]].

- **The Maurer–Cartan equation as zero-curvature Bianchi.** The product connection $\operatorname{pr}_2^*\theta$ on $M \times G$ is flat, $\Omega = 0$, because $\theta$ satisfies the [[Thm - The Maurer-Cartan Equation|Maurer–Cartan equation]] $d\theta + \tfrac12[\theta \wedge \theta] = 0$. That equation is the structure equation with curvature set to zero, and differentiating it reproduces the same graded-Jacobi cancellation that powers the Bianchi identity; flat connections are exactly the connections whose potentials solve Maurer–Cartan locally, and Bianchi is the consistency condition that makes this solvable.

- **Local field-strength algebra.** The identity $dF + [A \wedge F] = 0$ holds for *any* $\mathfrak{g}$-valued $1$-form $A$ with $F = dA + \tfrac12[A \wedge A]$, whether or not $A$ is the local form of a connection. This is the bridge to the physics literature, where the Bianchi identity is written $\sum_{\text{cyc}} D_\lambda F_{\mu\nu} = 0$ with $D_\lambda F_{\mu\nu} = \partial_\lambda F_{\mu\nu} + [A_\lambda, F_{\mu\nu}]$; the coordinate identity is the component form of this page's part (c), and its proof is the same graded-Jacobi cancellation transcribed into indices.

---

# Unlocked by This

> [!tip] Closed characteristic forms *(from Chern–Weil Theory)*
> Because $d^{\nabla_\omega}F_\omega = 0$, every $\operatorname{Ad}$-invariant polynomial in the curvature produces a closed form on the base, and hence a de Rham cohomology class independent of the connection. This is the foundation of **[[Thm - Chern-Weil Theorem|Chern–Weil theory]]** and of the Chern, Pontryagin, and Euler classes.

> [!tip] The homogeneous Yang–Mills half *(from Yang–Mills Theory)*
> The Bianchi identity is the equation $d^A F = 0$ that every connection satisfies without any variational principle, standing opposite the field equation $d^A \star F = 0$. Their interplay makes **[[Thm - Self-Dual Connections are Yang-Mills|self-dual connections automatically Yang–Mills]]** and underlies instanton theory.
