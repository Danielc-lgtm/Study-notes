---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle"
  - "Def - Connection on a Principal Bundle"
  - "Def - Curvature of a Principal Connection"
  - "Thm - Pull-Back Commutes with the Exterior Derivative"
  - "Thm - Structure Equation for the Curvature"
  - "Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space"
  - "Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles"
  - "Def - Fundamental Vector Field of a Group Action"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
  - "Def - Associated Bundle"
  - "Def - Adjoint Bundles ad P and Ad P"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a Lie group with Lie algebra $\mathfrak{g} = T_e G$, and $\pi\colon P \to M$ is a smooth principal $G$-bundle over a smooth manifold $M$. The group acts on the **right**, $R_g(p) = p \cdot g$, and the fundamental vector field of $X \in \mathfrak{g}$ is $X_P(p) = \frac{d}{dt}\big|_{t=0}\, p \cdot \exp(tX)$; this is the standing convention of the series, and it is the object recorded on **[[Def - Fundamental Vector Field of a Group Action]]**. We write $\operatorname{Ad}_g = d_e(h \mapsto ghg^{-1})\colon \mathfrak{g} \to \mathfrak{g}$ for the adjoint representation, so that for a matrix group $\operatorname{Ad}_g X = gXg^{-1}$.

A **connection** on $P$ is a $\mathfrak{g}$-valued one-form $\omega \in \Omega^1(P; \mathfrak{g})$ satisfying the two defining conditions recorded on **[[Def - Connection on a Principal Bundle]]**:

1. $R_g^* \omega = \operatorname{Ad}_{g^{-1}} \omega$ for every $g \in G$ (equivariance);
2. $\omega(X_P) = X$ for every $X \in \mathfrak{g}$ (reproduction of fundamental fields).

Its **curvature** is $\Omega = d\omega + \tfrac12[\omega \wedge \omega] \in \Omega^2(P; \mathfrak{g})$, the structure-equation form of **[[Def - Curvature of a Principal Connection]]**; $\Omega$ is horizontal and $\operatorname{Ad}$-equivariant, hence **basic**, and descends to a unique two-form $F_\omega \in \Omega^2(M; \operatorname{ad} P)$ on the base with $\pi^* F_\omega = \Omega$. Here $\operatorname{ad} P = P \times_{\operatorname{Ad}} \mathfrak{g}$ is the **adjoint bundle** of **[[Def - Adjoint Bundles ad P and Ad P]]**. Given a local section $s_\alpha\colon U_\alpha \to P$ over an open set $U_\alpha \subseteq M$, the **local connection form** and **local curvature form** are
$$A_\alpha := s_\alpha^* \omega \in \Omega^1(U_\alpha; \mathfrak{g}), \qquad F_\alpha := s_\alpha^* \Omega \in \Omega^2(U_\alpha; \mathfrak{g}),$$
and $F_\alpha = dA_\alpha + \tfrac12[A_\alpha \wedge A_\alpha]$ (the local structure equation).

The bracket $[\alpha \wedge \beta]$ of $\mathfrak{g}$-valued forms is the one fixed on **[[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]]**: on decomposable forms $\alpha = a \otimes \xi$ and $\beta = b \otimes \eta$ (with $a, b$ scalar forms and $\xi, \eta \in \mathfrak{g}$) it is $[\alpha \wedge \beta] = (a \wedge b) \otimes [\xi, \eta]$, extended bilinearly; for one-forms this gives $[\omega \wedge \omega](Y, Z) = 2[\omega(Y), \omega(Z)]$, which is why the structure equation carries the factor $\tfrac12$.

Now let $f\colon N \to M$ be a smooth map from a second manifold $N$. The **pull-back bundle** is
$$f^*P := \{(p, n) \in P \times N \mid f(n) = \pi(p)\},$$
a submanifold of $P \times N$; the projection $\varpi\colon f^*P \to N$, $(p, n) \mapsto n$, makes it a principal $G$-bundle over $N$ with the action $(p, n) \cdot g = (p \cdot g, n)$, and the **canonical map**
$$\hat f\colon f^*P \to P, \qquad \hat f(p, n) = p$$
is smooth, $G$-equivariant ($\hat f(q \cdot g) = \hat f(q) \cdot g$, i.e. $\hat f \circ R_g = R_g \circ \hat f$), and covers $f$ in the sense that $\pi \circ \hat f = f \circ \varpi$. Restricted to any fibre $\varpi^{-1}(n) = P_{f(n)} \times \{n\}$, the map $\hat f$ is a diffeomorphism onto $P_{f(n)}$. All of this is the content of **[[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle]]**, specialised to a principal bundle; we take it as given.

For a smooth map $\phi\colon S \to T$ and a form $\eta$ on $T$ we write $\phi^*\eta$ for its **pull-back**, the operation of **[[Def - Pullback of a Differential Form on a Manifold]]**; it is $\mathbb{R}$-linear, commutes with the wedge product ($\phi^*(a \wedge b) = \phi^*a \wedge \phi^*b$, by **[[Thm - Wedge Product Properties]]**), is functorial ($(\psi \circ \phi)^* = \phi^* \circ \psi^*$), and commutes with the exterior derivative ($\phi^* d\eta = d\phi^*\eta$, the content of **[[Thm - Pull-Back Commutes with the Exterior Derivative]]**). For a $\mathfrak{g}$-valued form $\eta = \sum_i \eta_i \otimes \xi_i$ (with $\xi_i$ a fixed basis of $\mathfrak{g}$) the pull-back acts componentwise, $\phi^*\eta = \sum_i (\phi^*\eta_i) \otimes \xi_i$, and every one of these properties passes to the $\mathfrak{g}$-valued case componentwise.

> [!warning] Convention: the two sources place the $P$-factor on opposite sides
> Haydys (Introduction to Gauge Theory, §2.2.4) writes $f^*P = \{(p,n) \in P \times N : f(n) = \pi(p)\}$ with the canonical map $\hat f(p,n) = p$, and states the result as "$f^*A := \hat f^* A$ is a connection on $f^*P$ and $F_{f^*A} = f^* F_A$", where his $A$ is our connection form $\omega$ and his $F_A$ is our descended curvature $F_\omega$. Bär (§2.5, Remark 2.5.7) instead writes the pull-back as a submanifold of $N \times P$ and uses $\operatorname{pr}_2$ for the projection onto the $P$-factor, so that his $\operatorname{pr}_2$ is exactly our $\hat f$. The two conventions differ only by the order of the two factors; we adopt Haydys's ordering. Every displayed identity below is stated for $\hat f$ and is Bär's identity with $\operatorname{pr}_2$ substituted for $\hat f$.

> [!warning] Convention: Haydys leaves the proof as an exercise; Bär proves it inside the naturality argument
> Haydys states the theorem (his Proposition 56) with the words "whose proof is left as an exercise". Bär proves the connection half and the local-form half in the course of establishing the naturality of characteristic classes (his Remark 2.5.7). We prove all four parts in full; part (d) and the global identity $F_{f^*\omega} = f^* F_\omega$ under the identification $\operatorname{ad}(f^*P) = f^* \operatorname{ad} P$ are proved here from scratch (they follow the account in Kobayashi–Nomizu, *Foundations of Differential Geometry* I, Proposition II.6.2), as neither source writes them out.

---

# Statement

> **Theorem (pull-back of connections and curvature).** Let $\pi\colon P \to M$ be a principal $G$-bundle, let $f\colon N \to M$ be smooth, and let $\hat f\colon f^*P \to P$ and $\varpi\colon f^*P \to N$ be the canonical map and the projection of the pull-back bundle. Let $\omega \in \Omega^1(P; \mathfrak{g})$ be a connection on $P$ with curvature $\Omega \in \Omega^2(P; \mathfrak{g})$ and descended curvature $F_\omega \in \Omega^2(M; \operatorname{ad} P)$. Then:
>
> **(a)** The $\mathfrak{g}$-valued one-form $f^*\omega := \hat f^*\omega \in \Omega^1(f^*P; \mathfrak{g})$ is a connection on $f^*P$.
>
> **(b)** The curvature of $f^*\omega$ on the total space is $\Omega_{f^*\omega} = \hat f^*\Omega$. Under the canonical bundle isomorphism $\operatorname{ad}(f^*P) \cong f^* \operatorname{ad} P$, the descended curvature satisfies
> $$F_{f^*\omega} = f^* F_\omega \in \Omega^2\big(N; f^*\operatorname{ad}P\big).$$
>
> **(c)** Let $\{U_\alpha\}$ be a trivialising cover of $M$ with local sections $s_\alpha\colon U_\alpha \to P$, and set $V_\alpha := f^{-1}(U_\alpha)$ and $s'_\alpha := \hat f^{-1} \circ s_\alpha \circ f\colon V_\alpha \to f^*P$ (the local section $n \mapsto (s_\alpha(f(n)), n)$). Writing $A_\alpha = s_\alpha^*\omega$, $F_\alpha = s_\alpha^*\Omega$ for the local forms of $\omega$ and $A'_\alpha = (s'_\alpha)^*(f^*\omega)$, $F'_\alpha = (s'_\alpha)^*\Omega_{f^*\omega}$ for those of $f^*\omega$, one has
> $$A'_\alpha = f^* A_\alpha, \qquad F'_\alpha = f^* F_\alpha.$$
>
> **(d)** Let $\rho\colon G \to GL(V)$ be a representation. Under the canonical vector-bundle isomorphism $f^*(P \times_\rho V) \cong (f^*P) \times_\rho V$, the covariant derivative on $(f^*P) \times_\rho V$ induced by the connection $f^*\omega$ coincides with the pull-back connection $f^*\nabla^\omega$ of the covariant derivative $\nabla^\omega$ induced on $P \times_\rho V$ by $\omega$.

The four parts are one statement read at four altitudes: (a) on the total space $f^*P$, (b) both on the total space and on the base $N$, (c) in local gauges, and (d) on every associated vector bundle at once. Part (a) is the assertion that pulling a connection back through the canonical map produces a connection; the remaining parts say that curvature, its local representatives, and the induced covariant derivatives all pull back by the same rule, with no correction terms.

---

# Motivation

A connection is data attached to a specific principal bundle over a specific base. The moment one wants to *transport* a bundle-and-connection from one base to another — to restrict a gauge field on $M$ to a submanifold, to a curve, or to compare fields over $M$ with fields over a space that maps into $M$ — one is pulling the bundle back along a map $f\colon N \to M$. The question this theorem answers is whether the connection comes along for free, and whether its curvature is computed downstairs before or after the pull-back with the same answer.

The importance is that it makes the assignment "bundle-with-connection $\mapsto$ its curvature" *natural* in the base. Two constructions in the series rest on exactly this naturality. The first is the naturality of characteristic classes in **Gauge Theory VI**: a Chern-Weil form is a polynomial in the curvature, and to prove that a characteristic class pulls back correctly, $c(f^*P) = f^* c(P)$, one needs precisely that the curvature of the pulled-back connection is the pull-back of the curvature, so that the polynomial evaluated upstairs and pulled back equals the polynomial evaluated on the pulled-back curvature. The second is the restriction of a connection to a curve in **Gauge Theory V**: parallel transport along a path $\gamma\colon [0,1] \to M$ is governed by the pulled-back connection $\gamma^*\omega$ on $\gamma^*P$, an ordinary linear ordinary differential equation, and this theorem is what guarantees $\gamma^*\omega$ really is a connection so that the transport is well posed.

The heart of the matter is that the pull-back is performed through the *canonical equivariant map* $\hat f$, not through $f$ itself — $f$ maps $N$ to $M$, but the connection lives on the total space, and it is $\hat f\colon f^*P \to P$ that carries the total space of the pulled-back bundle to the total space of the original. Every clause of the proof is a statement about how $\hat f$ interacts with the group action, with fundamental vector fields, and with the exterior derivative; because $\hat f$ is $G$-equivariant and covers $f$, all three interactions are exactly the ones the two defining conditions of a connection require.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is a connection on $P$ together with a smooth map $f$; the skill is recognising when a problem is secretly of this form.

The first disguised source is **a submanifold or an embedding**. Whenever one restricts a gauge field to a submanifold $\iota\colon N \hookrightarrow M$, one is pulling back along the inclusion, and $\iota^*P = P|_N$ is the restricted bundle. The bridge $B \Rightarrow A$ is that an embedding is in particular a smooth map, so the theorem applies verbatim; the payoff is that the restricted field is automatically a connection with restricted curvature, so one never re-checks the two defining axioms on the smaller base. *Example problem:* restrict the standard connection on the Hopf bundle $S^{2n+1} \to \mathbb{CP}^n$ to a projective line $\iota\colon \mathbb{CP}^1 \hookrightarrow \mathbb{CP}^n$ and identify the result with the standard connection on $S^3 \to \mathbb{CP}^1$.

The second disguised source is **a curve or a homotopy**. A path $\gamma\colon [0,1] \to M$ and a homotopy $H\colon [0,1] \times [0,1] \to M$ are both smooth maps into the base, and pulling a connection back along them turns the connection into data on an interval or a square. The bridge is again that these are smooth maps; the non-obvious payoff is that parallel transport and its homotopy invariance become statements about a connection on a low-dimensional, contractible or nearly contractible, pull-back bundle, where every bundle is trivial and the connection is a single $\mathfrak{g}$-valued one-form. *Example problem:* set up the parallel-transport equation along $\gamma$ as the horizontal-lift equation for $\gamma^*\omega$ on $\gamma^*P \cong [0,1] \times G$.

The third disguised source is **a change of parameters or a covering map**. If $q\colon \tilde M \to M$ is a covering (or any submersion used to reparametrise), a connection downstairs pulls back to one upstairs. The bridge is that a covering is a smooth map with the additional feature that $\hat q$ is a local diffeomorphism, so the pulled-back curvature is locally isomorphic to the original; the payoff is that one may compute a curvature integral or a holonomy on a convenient cover and descend. *Example problem:* compute the holonomy of a flat connection by pulling it back to the universal cover, where it becomes trivialisable.

**Targets (Output Amplification).** The bare conclusion is that connections and curvatures pull back with no correction; combined with other ingredients it does much more.

Combine the conclusion with **an invariant polynomial** $\lambda$ on $\mathfrak{g}$. Since the Chern-Weil form is $\lambda(F_\omega) \in \Omega^{2k}(M)$ and $F_{f^*\omega} = f^* F_\omega$, we get $\lambda(F_{f^*\omega}) = \lambda(f^* F_\omega) = f^* \lambda(F_\omega)$, because $\lambda$ is applied pointwise and commutes with pull-back. The extra ingredient is the invariance of $\lambda$ (so that the form descends) and the closedness of Chern-Weil forms; the payoff is the naturality identity $c_\lambda(f^*P) = f^* c_\lambda(P)$ in de Rham cohomology, the backbone of characteristic-class theory.

Combine the conclusion with **the affine structure of the space of connections**. Two connections on $P$ differ by an $\operatorname{ad}P$-valued one-form $b$; pulling back sends $\omega \mapsto \hat f^*\omega$ and $b \mapsto f^*b$ linearly, so pull-back is an affine map $\mathcal{A}(P) \to \mathcal{A}(f^*P)$. The extra ingredient is that $\mathcal{A}(P)$ is affine over $\Omega^1(M; \operatorname{ad}P)$; the payoff is that a homotopy of connections downstairs pulls back to a homotopy upstairs, which is exactly the transgression argument that proves characteristic classes are independent of the connection.

Combine the conclusion with **flatness**. If $\Omega = 0$ then $\Omega_{f^*\omega} = \hat f^*\Omega = 0$, so the pull-back of a flat connection is flat. The extra ingredient is the equivalence of flatness with local triviality; the payoff is that flatness is a homotopy-invariant, monodromy-representation phenomenon, developed in **Gauge Theory V**, where pulling back along paths converts a flat connection into a representation of the fundamental group.

---

# Why Is It True

Strip away the formalism and picture the canonical map $\hat f\colon f^*P \to P$. It sends the fibre of $f^*P$ over $n \in N$ diffeomorphically onto the fibre of $P$ over $f(n)$, and it does so *compatibly with the group action*: sliding a point by $g$ upstairs and then applying $\hat f$ is the same as applying $\hat f$ and then sliding by $g$. A connection is nothing but a rule, invariant under the group, for reading off "how much of a tangent vector points along the fibre", expressed as an element of $\mathfrak{g}$. Because $\hat f$ is a fibrewise diffeomorphism that respects the action, it carries the fibre directions of $f^*P$ onto the fibre directions of $P$ and the group action of $f^*P$ onto that of $P$; so the rule $\omega$ upstairs, read through $\hat f$, is again a group-invariant rule that reproduces fundamental fields. That is the whole of part (a).

**A connection pulls back to a connection because the canonical map is a fibrewise, action-preserving diffeomorphism, and the two defining conditions of a connection are exactly the conditions preserved by such a map.**

For the curvature, the mechanism is even shorter. Curvature is built from the connection by two operations — the exterior derivative and the Lie bracket of forms — and both operations are *natural*: they commute with pull-back. So computing the curvature and then pulling back is the same as pulling back and then computing the curvature; there is no room for a correction term because neither $d$ nor the bracket produces one. The absence of any inhomogeneous term is not a small miracle but the reflection of the fact that pull-back is a homomorphism for the full differential-graded structure in which curvature is defined.

The smallest concrete case makes this vivid. Take $G = U(1)$, abelian, so $\mathfrak{g} = i\mathbb{R}$, brackets vanish, and $\Omega = d\omega$; the descended curvature $F_\omega$ is an ordinary $i\mathbb{R}$-valued two-form on $M$ because $\operatorname{ad}P$ is the trivial bundle $\underline{i\mathbb{R}}$. Then $F_{f^*\omega} = f^* F_\omega$ is the plainest possible naturality statement: the field strength of the pulled-back electromagnetic potential is the pull-back of the field strength, $f^*(dA) = d(f^*A)$, which is just the commutation of $d$ with pull-back written for a physicist. Everything the theorem adds over this case is the bookkeeping that makes the non-abelian correction terms cancel, and they cancel for the same reason: the bracket, like $d$, is natural.

---

# What Makes This Hard

The one genuinely non-obvious point is that the pull-back is taken through $\hat f$ and not through $f$: the connection lives on the total space $P$, so "pulling it back" means using the map between total spaces, $\hat f\colon f^*P \to P$, and part (c)'s local formulas involve $f$ only because the local sections $s'_\alpha$ are built so that $\hat f \circ s'_\alpha = s_\alpha \circ f$. A common error is to try to write $f^*\omega$ using $f$ directly, which is type-incorrect, or to forget that the local section of $f^*P$ that makes $A'_\alpha = f^*A_\alpha$ true is the specific section $n \mapsto (s_\alpha(f(n)), n)$ and not some arbitrary local section. The second subtlety is the identification $\operatorname{ad}(f^*P) \cong f^*\operatorname{ad}P$ in part (b): the descended curvatures $F_{f^*\omega}$ and $f^*F_\omega$ are sections of two *a priori* different bundles, and the equation between them is meaningful only after one fixes the canonical isomorphism between those bundles, which must itself be checked to be well defined.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Establish three naturality facts about the canonical map $\hat f$ — that it sends fundamental fields to fundamental fields, that the bracket of $\mathfrak{g}$-valued forms is natural under pull-back, and that pull-back and the associated-bundle functor commute — and then feed them into the two defining conditions of a connection and into the structure equation. Each of the four parts is a short substitution once these facts are in hand.

**Subgoal decomposition:**

1. **Fundamental fields transform correctly.** Show $d\hat f(X_{f^*P}) = X_P \circ \hat f$ for every $X \in \mathfrak{g}$.
   - *Hint:* Differentiate the equivariance identity $\hat f(q \cdot \exp tX) = \hat f(q) \cdot \exp tX$ at $t = 0$.
   - *Why needed:* It is exactly what verifies defining condition (2) for $\hat f^*\omega$.

2. **The bracket is natural.** Show $\phi^*[\alpha \wedge \beta] = [\phi^*\alpha \wedge \phi^*\beta]$ for any smooth $\phi$ and $\mathfrak{g}$-valued forms $\alpha, \beta$.
   - *Hint:* Reduce to decomposable forms $a \otimes \xi$ and use that pull-back commutes with the wedge product and fixes the constant $[\xi, \eta]$.
   - *Why needed:* It is the only missing ingredient in the curvature computation, alongside the naturality of $d$.

3. **Part (a): $\hat f^*\omega$ is a connection.** Verify equivariance and reproduction of fundamental fields.
   - *Hint:* For equivariance use $\hat f \circ R_g = R_g \circ \hat f$ and functoriality of pull-back; for the fundamental-field condition use Subgoal 1.
   - *Why needed:* It is part (a) and the precondition for all the rest.

4. **Part (b) on the total space: $\Omega_{f^*\omega} = \hat f^*\Omega$.** Apply the structure equation to $f^*\omega$ and pull the structure equation of $\omega$ back.
   - *Hint:* Use the naturality of $d$ (the external theorem **[[Thm - Pull-Back Commutes with the Exterior Derivative]]**) and of the bracket (Subgoal 2).
   - *Why needed:* It is the total-space half of (b) and the input to (c).

5. **The associated-bundle functor commutes with pull-back.** Construct the canonical isomorphism $\Phi_\rho\colon (f^*P) \times_\rho V \to f^*(P \times_\rho V)$ and check it is a well-defined vector-bundle isomorphism.
   - *Hint:* Send $[(p, n), v]$ to $(n, [p, v])$ and check independence of the representative using the action.
   - *Why needed:* It gives meaning to the identifications in (b) and (d).

6. **Part (c): local forms.** Compute $A'_\alpha = (s'_\alpha)^*\hat f^*\omega$ and $F'_\alpha = (s'_\alpha)^*\hat f^*\Omega$ using $\hat f \circ s'_\alpha = s_\alpha \circ f$ and functoriality.
   - *Hint:* $(s'_\alpha)^*\hat f^* = (\hat f \circ s'_\alpha)^* = (s_\alpha \circ f)^* = f^* s_\alpha^*$.
   - *Why needed:* It is part (c) and, via the local characterisation of the descended curvature, the route to the global identity in (b).

7. **Part (b) on the base and Part (d).** Deduce $F_{f^*\omega} = f^*F_\omega$ from (c) and the local characterisation of the descent, and deduce the equality of induced connections in (d) from the local connection matrices.
   - *Hint:* Both descended curvatures and both connections are pinned down by their local representatives, which agree by (c).
   - *Why needed:* These are the remaining global statements.

---

# Lemma Decomposition

> [!note]- Lemma 1: The canonical map carries fundamental fields to fundamental fields
> **Statement:** For every $X \in \mathfrak{g}$ and every $q \in f^*P$, $\; d\hat f_q\big(X_{f^*P}(q)\big) = X_P\big(\hat f(q)\big)$. Equivalently, $\hat f$ intertwines the fundamental vector fields: $d\hat f \circ X_{f^*P} = X_P \circ \hat f$.
>
> **Hint:** Differentiate the equivariance of $\hat f$ along the one-parameter subgroup $t \mapsto \exp(tX)$.
>
> **Why needed:** It is exactly the identity that verifies the second defining condition of a connection for $\hat f^*\omega$; the whole difference between a general one-form and a connection form lives on the fundamental fields.
>
> > [!note]- Full proof
> > Fix $X \in \mathfrak{g}$ and $q \in f^*P$. By the definition of the fundamental vector field (**[[Def - Fundamental Vector Field of a Group Action]]**, right-action convention), the curve $t \mapsto q \cdot \exp(tX)$ has velocity $X_{f^*P}(q)$ at $t = 0$. Since $\hat f$ is $G$-equivariant, $\hat f(q \cdot \exp(tX)) = \hat f(q) \cdot \exp(tX)$ for all $t$ (by $G$-equivariance of the canonical map, part of **[[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle]]**). Differentiating both sides at $t = 0$ and using the chain rule on the left,
> > $$d\hat f_q\big(X_{f^*P}(q)\big) = \frac{d}{dt}\Big|_{t=0} \hat f\big(q \cdot \exp(tX)\big) = \frac{d}{dt}\Big|_{t=0} \hat f(q) \cdot \exp(tX) = X_P\big(\hat f(q)\big),$$
> > where the first equality is the definition of the differential applied to the velocity of $t \mapsto q\cdot\exp(tX)$ (whose value at $0$ is $X_{f^*P}(q)$), the second is $G$-equivariance, and the third is again the definition of the fundamental vector field, now for the right action on $P$ at the point $\hat f(q)$. As $q$ was arbitrary, $d\hat f \circ X_{f^*P} = X_P \circ \hat f$. $\;\blacksquare$

> [!note]- Lemma 2: The bracket of Lie-algebra-valued forms is natural under pull-back
> **Statement:** Let $\phi\colon S \to T$ be smooth and $\alpha \in \Omega^p(T; \mathfrak{g})$, $\beta \in \Omega^q(T; \mathfrak{g})$. Then $\phi^*[\alpha \wedge \beta] = [\phi^*\alpha \wedge \phi^*\beta]$ in $\Omega^{p+q}(S; \mathfrak{g})$.
>
> **Hint:** Reduce to decomposable forms $\alpha = a \otimes \xi$, $\beta = b \otimes \eta$ and use that scalar pull-back commutes with the wedge product and does nothing to the constant vector $[\xi, \eta] \in \mathfrak{g}$.
>
> **Why needed:** Curvature is $d\omega + \tfrac12[\omega \wedge \omega]$; to pull curvature back through $\hat f$ we need both that $d$ is natural (an external theorem) and that the bracket is natural (this lemma). Without it the non-abelian term would not manifestly pull back.
>
> > [!note]- Full proof
> > Fix a basis $(\xi_1, \dots, \xi_r)$ of $\mathfrak{g}$. Every $\mathfrak{g}$-valued form is a finite sum of decomposable forms $a \otimes \xi_i$ with $a$ a scalar form, and both sides of the claimed identity are $\mathbb{R}$-bilinear in $(\alpha, \beta)$; so it suffices to prove the identity for decomposables $\alpha = a \otimes \xi$ and $\beta = b \otimes \eta$ with $a \in \Omega^p(T)$, $b \in \Omega^q(T)$, $\xi, \eta \in \mathfrak{g}$.
> >
> > **Compute the left-hand side.** By the definition of the bracket on decomposable forms (**[[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]]**), $[\alpha \wedge \beta] = (a \wedge b) \otimes [\xi, \eta]$. Applying $\phi^*$, which acts on a $\mathfrak{g}$-valued form componentwise and fixes the constant vector $[\xi, \eta]$,
> > $$\phi^*[\alpha \wedge \beta] = \phi^*(a \wedge b) \otimes [\xi, \eta] = (\phi^*a \wedge \phi^*b) \otimes [\xi, \eta],$$
> > where the second equality uses that scalar pull-back commutes with the wedge product (**[[Thm - Wedge Product Properties]]**).
> >
> > **Compute the right-hand side.** The pull-backs are $\phi^*\alpha = (\phi^*a) \otimes \xi$ and $\phi^*\beta = (\phi^*b) \otimes \eta$ (componentwise action of pull-back). By the definition of the bracket applied to these decomposable forms,
> > $$[\phi^*\alpha \wedge \phi^*\beta] = (\phi^*a \wedge \phi^*b) \otimes [\xi, \eta].$$
> >
> > **Conclude.** The two expressions are identical. By bilinearity the identity extends to all $\alpha, \beta$. $\;\blacksquare$

> [!note]- Lemma 3: The associated-bundle construction commutes with pull-back
> **Statement:** Let $\rho\colon G \to GL(V)$ be a representation and $f\colon N \to M$ smooth. The map
> $$\Phi_\rho\colon (f^*P) \times_\rho V \longrightarrow f^*(P \times_\rho V), \qquad \big[(p, n),\, v\big] \longmapsto \big(n,\, [p, v]\big)$$
> is a well-defined isomorphism of vector bundles over $N$. In particular, taking $\rho = \operatorname{Ad}$ and $V = \mathfrak{g}$, it restricts to a canonical isomorphism $\operatorname{ad}(f^*P) = (f^*P) \times_{\operatorname{Ad}} \mathfrak{g} \cong f^*(P \times_{\operatorname{Ad}} \mathfrak{g}) = f^*\operatorname{ad}P$.
>
> **Hint:** Check independence of the equivalence-class representative using the defining relation of the associated bundle, then check it is a fibrewise linear isomorphism and smooth in a local trivialisation.
>
> **Why needed:** The descended curvatures in part (b) and the two induced connections in part (d) live on the two bundles $\operatorname{ad}(f^*P)$ and $f^*\operatorname{ad}P$ (respectively on $(f^*P) \times_\rho V$ and $f^*(P \times_\rho V)$); the identities of (b) and (d) are meaningful only through this isomorphism.
>
> > [!note]- Full proof
> > Recall (**[[Def - Associated Bundle]]**) that $(f^*P) \times_\rho V$ is the quotient of $(f^*P) \times V$ by the relation $(q \cdot g, v) \sim (q, \rho(g)v)$, with class denoted $[q, v]$, and that $f^*(P \times_\rho V) = \{(n, w) \in N \times (P \times_\rho V) : f(n) = \pi_E(w)\}$ where $\pi_E\colon P \times_\rho V \to M$ is the associated-bundle projection (**[[Def - Operations on Vector Bundles and Pull-Back Bundles|pull-back of a vector bundle]]**).
> >
> > **Well-definedness (Step 0).** We must check $\Phi_\rho$ is independent of the representative of the class $[(p, n), v]$. A general representative of the same class is $((p, n) \cdot g,\, \rho(g)^{-1}v) = ((p \cdot g, n),\, \rho(g)^{-1}v)$ for $g \in G$ (the action on $f^*P$ is $(p, n) \cdot g = (p \cdot g, n)$). Its image is
> > $$\big(n,\, [p \cdot g,\, \rho(g)^{-1}v]\big) = \big(n,\, [p, v]\big),$$
> > because $[p \cdot g, \rho(g)^{-1}v] = [p, v]$ by the defining relation of $P \times_\rho V$. So the image does not depend on the representative, and $\Phi_\rho$ is a well-defined map. Its target lands in $f^*(P \times_\rho V)$ because $\pi_E([p, v]) = \pi(p) = f(n)$ (using $(p, n) \in f^*P$, so $\pi(p) = f(n)$), which is exactly the fibre-product condition.
> >
> > **Fibrewise linear isomorphism.** Fix $n \in N$. The fibre of $(f^*P) \times_\rho V$ over $n$ is $\varpi^{-1}(n) \times_\rho V = (P_{f(n)} \times \{n\}) \times_\rho V \cong P_{f(n)} \times_\rho V = (P \times_\rho V)_{f(n)}$, and the fibre of $f^*(P \times_\rho V)$ over $n$ is $\{n\} \times (P \times_\rho V)_{f(n)} \cong (P \times_\rho V)_{f(n)}$. Under these identifications $\Phi_\rho$ is the identity on $(P \times_\rho V)_{f(n)}$: it sends $[(p, n), v] \mapsto [p, v]$, using that $\hat f$ restricts to the fibre diffeomorphism $(p, n) \mapsto p$. A representative-preserving bijection between two vector spaces that carries the vector-space structure (the class operations $[q, v] + [q, v'] = [q, v + v']$ and $c[q, v] = [q, cv]$ are defined by the same formula on both sides) is a linear isomorphism. Hence $\Phi_\rho$ is a fibrewise linear isomorphism.
> >
> > **Smoothness.** Over a trivialising set $U_\alpha$ with section $s_\alpha$, the bundle $P \times_\rho V$ is trivialised by $(u, v) \mapsto [s_\alpha(u), v]$, and $(f^*P) \times_\rho V$ over $V_\alpha = f^{-1}(U_\alpha)$ is trivialised by $(n, v) \mapsto [s'_\alpha(n), v]$ with $s'_\alpha(n) = (s_\alpha(f(n)), n)$. In these trivialisations $\Phi_\rho$ reads $(n, v) \mapsto (n, v)$, since $\Phi_\rho[s'_\alpha(n), v] = (n, [s_\alpha(f(n)), v])$ and $[s_\alpha(f(n)), v]$ is the point of $f^*(P\times_\rho V)$ over $n$ with trivialisation coordinate $v$. The identity is smooth, so $\Phi_\rho$ is a smooth bundle isomorphism with smooth inverse. $\;\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix the connection $\omega$ on $P$, the smooth map $f\colon N \to M$, the canonical map $\hat f\colon f^*P \to P$, and the projection $\varpi\colon f^*P \to N$, all as in the Notation. Set $f^*\omega := \hat f^*\omega \in \Omega^1(f^*P; \mathfrak{g})$.
>
> **Part (a): $f^*\omega$ is a connection on $f^*P$.**
>
> **Verify condition (1) (equivariance).** Fix $g \in G$. Using functoriality of pull-back and the equivariance $\hat f \circ R_g = R_g \circ \hat f$ of the canonical map (**[[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle]]**),
> $$R_g^*(f^*\omega) = R_g^*\hat f^*\omega = (\hat f \circ R_g)^*\omega = (R_g \circ \hat f)^*\omega = \hat f^* R_g^*\omega \qquad \text{(functoriality } (\psi\circ\phi)^* = \phi^*\psi^* \text{, twice).}$$
> Now apply the equivariance of $\omega$ (condition (1) of **[[Def - Connection on a Principal Bundle]]**), namely $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$, and the fact that $\hat f^*$ commutes with the fixed linear map $\operatorname{Ad}_{g^{-1}}$ on $\mathfrak{g}$ (pull-back acts componentwise):
> $$\hat f^* R_g^*\omega = \hat f^*\big(\operatorname{Ad}_{g^{-1}}\omega\big) = \operatorname{Ad}_{g^{-1}}\big(\hat f^*\omega\big) = \operatorname{Ad}_{g^{-1}}(f^*\omega) \qquad \text{(equivariance of } \omega \text{; componentwise pull-back).}$$
> Combining the two displays, $R_g^*(f^*\omega) = \operatorname{Ad}_{g^{-1}}(f^*\omega)$, which is condition (1) for $f^*\omega$.
>
> **Verify condition (2) (fundamental fields).** Fix $X \in \mathfrak{g}$ and a point $q \in f^*P$. By the definition of pull-back of a one-form and Lemma 1,
> $$(f^*\omega)_q\big(X_{f^*P}(q)\big) = \omega_{\hat f(q)}\big(d\hat f_q(X_{f^*P}(q))\big) = \omega_{\hat f(q)}\big(X_P(\hat f(q))\big) = X \qquad \text{(definition of } \hat f^*\omega \text{; Lemma 1; condition (2) for } \omega\text{),}$$
> the last equality being condition (2) of **[[Def - Connection on a Principal Bundle]]** for $\omega$ at the point $\hat f(q)$. As $q$ was arbitrary, $(f^*\omega)(X_{f^*P}) = X$, which is condition (2) for $f^*\omega$. Both conditions hold, so $f^*\omega$ is a connection on $f^*P$. This proves (a).
>
> **Part (b), total space: $\Omega_{f^*\omega} = \hat f^*\Omega$.**
>
> **Apply the structure equation upstairs and pull it back.** By part (a), $f^*\omega$ is a connection, so by the structure equation (**[[Thm - Structure Equation for the Curvature]]**, which states that the curvature of any connection $\eta$ equals $d\eta + \tfrac12[\eta \wedge \eta]$) its curvature is
> $$\Omega_{f^*\omega} = d(f^*\omega) + \tfrac12[f^*\omega \wedge f^*\omega] = d\hat f^*\omega + \tfrac12[\hat f^*\omega \wedge \hat f^*\omega].$$
> Now use the naturality of $d$ (**[[Thm - Pull-Back Commutes with the Exterior Derivative]]**: $\hat f^* d\omega = d\hat f^*\omega$, applied componentwise to the $\mathfrak{g}$-valued $\omega$) and the naturality of the bracket (Lemma 2 with $\phi = \hat f$, $\alpha = \beta = \omega$):
> $$\Omega_{f^*\omega} = \hat f^* d\omega + \tfrac12 \hat f^*[\omega \wedge \omega] = \hat f^*\big(d\omega + \tfrac12[\omega \wedge \omega]\big) = \hat f^*\Omega \qquad \text{(naturality of } d \text{; Lemma 2; } \mathbb{R}\text{-linearity of } \hat f^* \text{; structure equation for } \omega\text{),}$$
> where the last equality is the structure equation $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ for $\omega$ itself (**[[Def - Curvature of a Principal Connection]]**). This proves the total-space identity.
>
> **Part (c): local forms.**
>
> **Set up the pulled-back sections.** Let $\{U_\alpha\}$ trivialise $M$ with sections $s_\alpha\colon U_\alpha \to P$, put $V_\alpha = f^{-1}(U_\alpha)$, and define $s'_\alpha\colon V_\alpha \to f^*P$ by $s'_\alpha(n) = (s_\alpha(f(n)), n)$. This is a smooth local section of $f^*P$: it lands in $f^*P$ because $\pi(s_\alpha(f(n))) = f(n)$, and $\varpi(s'_\alpha(n)) = n$. Moreover, by construction,
> $$\hat f \circ s'_\alpha = s_\alpha \circ f, \qquad \text{since } \hat f(s'_\alpha(n)) = \hat f(s_\alpha(f(n)), n) = s_\alpha(f(n)) = (s_\alpha \circ f)(n).$$
> This is the meaning of the formula $s'_\alpha = \hat f^{-1} \circ s_\alpha \circ f$ in the statement: $\hat f^{-1}$ is the fibrewise inverse, and it selects the unique preimage of $s_\alpha(f(n))$ in the fibre over $n$.
>
> **Pull back the connection form.** Using functoriality and $\hat f \circ s'_\alpha = s_\alpha \circ f$,
> $$A'_\alpha = (s'_\alpha)^*(f^*\omega) = (s'_\alpha)^*\hat f^*\omega = (\hat f \circ s'_\alpha)^*\omega = (s_\alpha \circ f)^*\omega = f^*(s_\alpha^*\omega) = f^* A_\alpha \qquad \text{(functoriality of pull-back, twice; definition of } A_\alpha\text{).}$$
>
> **Pull back the curvature form.** By the total-space identity of part (b), $\Omega_{f^*\omega} = \hat f^*\Omega$, so by the same computation
> $$F'_\alpha = (s'_\alpha)^*\Omega_{f^*\omega} = (s'_\alpha)^*\hat f^*\Omega = (s_\alpha \circ f)^*\Omega = f^*(s_\alpha^*\Omega) = f^* F_\alpha \qquad \text{(part (b); functoriality; definition of } F_\alpha\text{).}$$
> This proves (c). As an internal consistency check, both sides satisfy the local structure equation: $F'_\alpha = f^*F_\alpha = f^*\big(dA_\alpha + \tfrac12[A_\alpha \wedge A_\alpha]\big) = d(f^*A_\alpha) + \tfrac12[f^*A_\alpha \wedge f^*A_\alpha] = dA'_\alpha + \tfrac12[A'_\alpha \wedge A'_\alpha]$, using the naturality of $d$ and Lemma 2 once more.
>
> **Part (b), base: $F_{f^*\omega} = f^*F_\omega$ under $\operatorname{ad}(f^*P) \cong f^*\operatorname{ad}P$.**
>
> **Use the local characterisation of the descended curvature.** By **[[Def - Curvature of a Principal Connection]]** together with **[[Thm - Transformation of Local Connection and Curvature Forms]]**, the descended curvature $F_\omega \in \Omega^2(M; \operatorname{ad}P)$ is the unique global $\operatorname{ad}P$-valued two-form whose representative in the local trivialisation determined by $s_\alpha$ is the local curvature form $F_\alpha$; concretely $F_\omega|_{U_\alpha} = [s_\alpha, F_\alpha]$, meaning the section $u \mapsto [s_\alpha(u), F_\alpha(u)]$ of $\Lambda^2 T^*M \otimes \operatorname{ad}P$. This local-representative description is exactly the correspondence between basic equivariant $\mathfrak{g}$-valued forms on the total space and $\operatorname{ad}P$-valued forms on the base recorded in **[[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space]]**, applied to the basic equivariant form $\Omega$.
>
> Applying the same description on $N$ to the connection $f^*\omega$ (whose local curvature forms are the $F'_\alpha$ relative to the sections $s'_\alpha$), the descended curvature $F_{f^*\omega} \in \Omega^2(N; \operatorname{ad}(f^*P))$ has local representative $F_{f^*\omega}|_{V_\alpha} = [s'_\alpha, F'_\alpha]$.
>
> **Compare through $\Phi_{\operatorname{Ad}}$.** On the other side, the pull-back form $f^*F_\omega \in \Omega^2(N; f^*\operatorname{ad}P)$ has, over $V_\alpha$, the local representative obtained by pulling back the representative $[s_\alpha, F_\alpha]$ of $F_\omega$; concretely $(f^*F_\omega)(n) = \big(n, F_\omega(f(n))\big)$, whose trivialisation coordinate over $V_\alpha$ is $f^*F_\alpha$. Transporting $F_{f^*\omega}$ to $f^*\operatorname{ad}P$ by the canonical isomorphism $\Phi_{\operatorname{Ad}}\colon \operatorname{ad}(f^*P) \to f^*\operatorname{ad}P$ of Lemma 3, the class $[s'_\alpha, F'_\alpha]$ is sent, by the formula $\Phi_{\operatorname{Ad}}[(p, n), v] = (n, [p, v])$, to the element of $f^*\operatorname{ad}P$ with trivialisation coordinate $F'_\alpha$ over $V_\alpha$. Since $F'_\alpha = f^*F_\alpha$ by part (c), the two global two-forms $\Phi_{\operatorname{Ad}} \circ F_{f^*\omega}$ and $f^*F_\omega$ have the same trivialisation coordinate in every chart $V_\alpha$ of an open cover of $N$, hence are equal. Under the identification $\operatorname{ad}(f^*P) = f^*\operatorname{ad}P$ this reads
> $$F_{f^*\omega} = f^* F_\omega.$$
> This completes part (b).
>
> **Part (d): induced covariant derivatives.**
>
> Fix a representation $\rho\colon G \to GL(V)$ with differential $\rho_* = d_e\rho\colon \mathfrak{g} \to \operatorname{End}(V)$. Write $E = P \times_\rho V$ and $\nabla^\omega$ for the covariant derivative it inherits from $\omega$; write $E' = (f^*P) \times_\rho V$ and $\nabla^{f^*\omega}$ for the covariant derivative it inherits from $f^*\omega$. By Lemma 3, $\Phi_\rho\colon E' \to f^*E$ is a canonical vector-bundle isomorphism, and we identify $E'$ with $f^*E$ through it.
>
> **Read off the local connection matrix of $\nabla^{f^*\omega}$.** By **[[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles]]**, for a local section $p$ of a principal bundle and $v\colon U \to V$ the induced covariant derivative satisfies $\nabla_Y[p, v] = [p, \partial_Y v + \rho_*(p^*\omega(Y))\,v]$; equivalently, in the local frame of $E$ furnished by $p$, the connection matrix is $\rho_*(p^*\omega) \in \Omega^1(U; \operatorname{End}V)$. Applied to $E'$ with the section $p = s'_\alpha$, and using $A'_\alpha = (s'_\alpha)^*(f^*\omega) = f^*A_\alpha$ from part (c) together with the componentwise commutation $\rho_* \circ f^* = f^* \circ \rho_*$ (the fixed linear map $\rho_*$ commutes with pull-back), the connection matrix of $\nabla^{f^*\omega}$ in the frame $s'_\alpha$ is
> $$\rho_*(A'_\alpha) = \rho_*(f^*A_\alpha) = f^*\big(\rho_*(A_\alpha)\big).$$
>
> **Read off the local connection matrix of the pull-back connection $f^*\nabla^\omega$.** Recall the construction of the pull-back of a vector-bundle connection. In the frame of $E$ over $U_\alpha$ given by $s_\alpha$ (with a fixed basis of $V$), $\nabla^\omega$ has connection matrix $\rho_*(A_\alpha) =: B_\alpha \in \Omega^1(U_\alpha; \operatorname{End}V)$; under a change of frame $e' = e\,h$ these transform by $B'_\alpha = h^{-1}B_\alpha h + h^{-1}dh$ (**[[Def - Connection Matrix and Local Form of a Connection]]**). Pulling back through $f$ turns this into $f^*B'_\alpha = (f^*h)^{-1}(f^*B_\alpha)(f^*h) + (f^*h)^{-1}d(f^*h)$, using $f^*(h^{-1}dh) = (f^*h)^{-1}\,d(f^*h)$ (naturality of $d$). Hence the collection $\{f^*B_\alpha\}$ satisfies the connection-matrix transformation law relative to the pulled-back frames $f^*e$ of $f^*E$, and therefore defines a unique connection on $f^*E$ — this is by definition the **pull-back connection** $f^*\nabla^\omega$; its connection matrix in the frame $\Phi_\rho \circ (\text{frame from } s'_\alpha) = f^*(\text{frame from } s_\alpha)$ is $f^*B_\alpha = f^*(\rho_*(A_\alpha))$.
>
> **Compare.** Under $\Phi_\rho$ the frame of $E'$ coming from $s'_\alpha$ is carried to the pulled-back frame $f^*(\text{frame from } s_\alpha)$ of $f^*E$: indeed for a basis vector $v_i \in V$, $\Phi_\rho[s'_\alpha, v_i] = (n, [s_\alpha(f(n)), v_i])$, which is the pull-back $f^*[s_\alpha, v_i]$. In this common frame both $\nabla^{f^*\omega}$ and $f^*\nabla^\omega$ have the same connection matrix $f^*(\rho_*(A_\alpha))$. Two connections on the same vector bundle with equal connection matrices in a common local frame over an open cover are equal (a connection is determined by its connection matrices, **[[Def - Connection Matrix and Local Form of a Connection]]**). Therefore $\nabla^{f^*\omega} = f^*\nabla^\omega$ under the identification $\Phi_\rho$. This proves (d).
>
> **Conclusion.** The pull-back one-form $f^*\omega = \hat f^*\omega$ is a connection on $f^*P$ (a); its curvature is $\hat f^*\Omega$ on the total space and $f^*F_\omega$ on the base under the canonical identification $\operatorname{ad}(f^*P) = f^*\operatorname{ad}P$ (b); its local connection and curvature forms are $f^*A_\alpha$ and $f^*F_\alpha$ (c); and the covariant derivatives it induces on associated bundles are the pull-backs of the covariant derivatives induced downstairs (d). Every one of these identities is the naturality of a single operation — the group action, the exterior derivative, the bracket, or the associated-bundle functor — under the canonical equivariant map $\hat f$. $\;\blacksquare$

---

# Cross-Field Exercise Suggestions

**Restriction to a projective line (complex geometry).** Let $\iota\colon \mathbb{CP}^1 \hookrightarrow \mathbb{CP}^n$ be the inclusion of a projective line and $\omega$ the standard connection on the Hopf bundle $S^{2n+1} \to \mathbb{CP}^n$. The theorem gives that $\iota^*\omega$ is the standard connection on the restricted bundle $\iota^*(S^{2n+1}) \cong S^3 \to \mathbb{CP}^1$, and $F_{\iota^*\omega} = \iota^* F_\omega$. This is non-obvious because the restricted total space is a genuine three-sphere, not a subset of $S^{2n+1}$ one can see directly; the theorem produces the connection abstractly and then part (c) lets one compute its local form by pulling back the known local form on $\mathbb{CP}^n$, which is the route by which one recovers $\int_{\mathbb{CP}^1} c_1 = -1$ downstairs.

**Parallel transport along a path (dynamical systems).** For a piecewise-smooth path $\gamma\colon [0, 1] \to M$, the pull-back $\gamma^*\omega$ on $\gamma^*P$ is a connection by part (a), and because $[0,1]$ is contractible $\gamma^*P$ is trivial, so $\gamma^*\omega$ is a single $\mathfrak{g}$-valued one-form $a(t)\,dt$. The horizontal-lift equation becomes the linear ordinary differential equation $\dot g(t) = -a(t) g(t)$ in $G$, whose solution is the parallel transport. The theorem is what licenses treating transport as an ordinary differential equation on the interval; the non-obvious content is that the curvature of $\gamma^*\omega$ vanishes for dimension reasons, so transport is path-ordered-exponential and never sees a two-form.

**Naturality of the first Chern class (algebraic topology).** For a Hermitian line bundle $L \to M$ with a unitary connection, the first Chern form is $\tfrac{i}{2\pi} F_\omega$, an ordinary closed two-form since $U(1)$ is abelian. Given $f\colon N \to M$, part (b) gives $F_{f^*\omega} = f^*F_\omega$, hence $c_1(f^*L) = f^* c_1(L)$ in de Rham cohomology. The application is non-obvious because the Chern class is usually introduced topologically, via classifying maps or clutching functions, and this theorem shows the differential-geometric representative is natural without invoking any of that machinery — the entire proof of naturality collapses to $f^*d = df^*$ and Lemma 2.

---

# Bridges

- **Naturality of characteristic classes (Gauge Theory VI).** A characteristic class is the de Rham class of $\lambda(F_\omega)$ for an $\operatorname{Ad}$-invariant polynomial $\lambda$ of degree $k$. Given $f\colon N \to M$, one builds $f^*P$, equips it with $f^*\omega$, computes its curvature $F_{f^*\omega} = f^*F_\omega$ by part (b), and then $\lambda(F_{f^*\omega}) = \lambda(f^*F_\omega) = f^*\lambda(F_\omega)$ because $\lambda$ is applied pointwise and pull-back is an algebra homomorphism on forms. Passing to cohomology yields $c_\lambda(f^*P) = f^*c_\lambda(P)$. The construction is entirely this theorem followed by the observation that invariant polynomials commute with pull-back; nothing else enters.

- **Restriction of connections to curves and holonomy (Gauge Theory V).** The horizontal lift of a path, the definition of parallel transport, and the holonomy group are all built by pulling the connection back along paths $\gamma$ and loops. Part (a) guarantees $\gamma^*\omega$ is a connection so that the lift exists and is unique; part (b) guarantees that the curvature seen along the path is $\gamma^*F_\omega$, which is how the Ambrose-Singer description of holonomy in terms of curvature is set up. The bridge is that transport, an object about the total space over an interval, is exactly the pulled-back connection theory of this page specialised to $N = [0,1]$.

- **The affine map on connection spaces (Gauge Theory IV-V).** Because pull-back is $\mathbb{R}$-linear and sends the difference $\omega - \omega' \in \Omega^1(M; \operatorname{ad}P)$ of two connections to $f^*(\omega - \omega') \in \Omega^1(N; \operatorname{ad}(f^*P))$, the assignment $\omega \mapsto f^*\omega$ is an affine map from $\mathcal{A}(P)$ to $\mathcal{A}(f^*P)$ over the linear map $f^*$ on the model spaces. This is the mechanism behind transgression: a straight-line homotopy $\omega_t = \omega_0 + t(\omega_1 - \omega_0)$ downstairs pulls back to a straight-line homotopy upstairs, so the Chern-Simons transgression form and the connection-independence of characteristic classes transport verbatim to $f^*P$.

- **The gauge-transformation law is a pull-back identity (Gauge Theory IV).** The transformation $A_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha + g_{\alpha\beta}^*\theta$ of local connection forms on **[[Thm - Transformation of Local Connection and Curvature Forms]]** is, at bottom, another instance of pulling forms back through maps into the total space (the transition sections $s_\beta = s_\alpha g_{\alpha\beta}$). The present theorem and that one are the two faces of "how local data transforms": one under a change of base, the other under a change of section.

---

# Unlocked by This

> [!tip] Naturality of the Chern-Weil homomorphism *(from Chern-Weil theory)*
> Once curvature is known to pull back with no correction, the Chern-Weil map $\lambda \mapsto [\lambda(F_\omega)]$ is a natural transformation: it commutes with pull-back of bundles. This is the input to the theorem that characteristic classes are homotopy invariants of the base and depend only on the isomorphism class of the bundle. See **Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional**.

> [!tip] Connections on restricted and induced bundles *(from bundle theory)*
> Combining part (a) with the structure-group reduction and extension operations, one obtains connections on every bundle built from $P$ by a smooth base map together with a homomorphism of structure groups; in particular the restriction of a spin or spin-$c$ connection to a submanifold, used in **Gauge Theory VIII** and **Gauge Theory XI**, is an instance of this page's construction.
