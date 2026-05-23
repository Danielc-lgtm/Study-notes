---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - The Wedge Product on a Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - The Differential of a Smooth Map"
  - "Def - Pullback of a Covariant Tensor Field"
tags: [geometry, differential-geometry]
---

# Notation

$F : M \to N$ is a smooth map between smooth manifolds with $\dim M = m$ and $\dim N = n$. $dF_p : T_pM \to T_{F(p)}N$ is the differential of $F$ at $p$. Forms on $N$ are $\omega, \eta \in \Omega^k(N)$; their pullbacks are $F^*\omega, F^*\eta \in \Omega^k(M)$. The Jacobian matrix of $F$ in charts $(U, x^i)$ on $M$ and $(V, y^j)$ on $N$ is $DF = (\partial F^j/\partial x^i)$. In a chart $(V, y^j)$ on $N$ a $k$-form is $\omega = \sum'_J \omega_J(y)\,dy^J$ with $J$ increasing. The full registry is on [[Differential Geometry VIII — Differential Forms]].

---

# Axiom Motivation

The motivation is the same as in [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem|MA IV]] but with one essential structural addition for the manifold setting: **pullback is the only natural functorial operation between forms on different manifolds, and crucially it works for every smooth map, with no diffeomorphism hypothesis.** This is the structural advantage of forms over vector fields, and the reason differential geometry is built on forms.

**Why pullback at all?** Because we have differential forms on different manifolds, connected by smooth maps, and we want to relate them. The natural question is: given $F : M \to N$ and a form $\omega$ on $N$, can we produce a form on $M$? The answer is yes, by a canonical construction that requires no choices.

The construction is forced by what forms eat. A $k$-form on $N$ at $F(p)$ eats $k$ tangent vectors at $F(p) \in N$; tangent vectors at $p \in M$ are sent forward by $dF_p$ to tangent vectors at $F(p) \in N$. So the natural way to evaluate the form-on-$N$ using tangent-vectors-from-$M$ is to push the vectors forward by $dF_p$ first, then feed the result to $\omega$. This gives the formula
$$(F^*\omega)_p(v_1, \dots, v_k) = \omega_{F(p)}(dF_p \cdot v_1, \dots, dF_p \cdot v_k).$$
Notice the direction reversal: the form moves *from $N$ to $M$* — the opposite direction of the map $F$. This is *forced* by the structure of forms-as-machines-eating-vectors. The reason is that a form is a co-vector (more precisely, an alternating multi-co-vector), and co-vectors are dual to vectors, so they transform contravariantly: vectors go forward, co-vectors come back.

**Why does this work for *every* smooth $F$, not just diffeomorphisms?** Because the construction only ever uses $dF_p$ to *push vectors forward*, which works universally — every smooth map has a well-defined differential at every point. It never requires pushing forms forward (which would need $F$ to be invertible to know which preimage's information to use), nor pulling vectors back (which would also need invertibility).

By contrast, **a vector field on $M$ cannot generally be pushed forward to a vector field on $N$**: if $F$ collapses two points $p_1 \neq p_2$ of $M$ to one point of $N$, and the vector field has different values $X_{p_1} \neq X_{p_2}$, there is no canonical way to combine $dF_{p_1}(X_{p_1})$ and $dF_{p_2}(X_{p_2})$ into a single value at $F(p_1) = F(p_2)$. The pushforward of a vector field is only defined when $F$ is a diffeomorphism. This asymmetry — pullback for forms is universal, pushforward for vectors is restricted — is the *primary reason* differential geometry is built on forms rather than vector fields when global computation matters. **Whenever you can phrase a question in terms of forms and pullback, do so.**

**What breaks if we tried to define a "pushforward of forms"?** Consider the projection $F : \mathbb{R}^2 \to \mathbb{R}$ along the second coordinate, $F(x, y) = x$. The $1$-form $dy$ on $\mathbb{R}^2$ has no sensible "pushforward" to $\mathbb{R}$: the fibres $F^{-1}(x_0)$ are vertical lines on which $dy$ takes different values at different heights, and there is no canonical scalar at $x_0 \in \mathbb{R}$. The opposite direction — $dy$ on $\mathbb{R}$ pulled back to $\mathbb{R}^2$ — doesn't apply (there is no $dy$ on $\mathbb{R}$), but pulling back $dx$ on $\mathbb{R}$ to $\mathbb{R}^2$ gives $dx$ on $\mathbb{R}^2$, which is well-defined.

**What about the algebraic properties?** They are all forced by the pointwise definition. The pullback is $\mathbb{R}$-linear (because evaluation of forms is linear). It commutes with wedge products ($F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$) because the wedge is built from the determinant, and the determinant respects composition with the linear map $dF_p$. It is contravariant ($(F \circ G)^* = G^* \circ F^*$) because the differential of a composite is a composite of differentials in the appropriate order. It commutes with the exterior derivative ($F^*d = dF^*$) — this is a non-trivial theorem ([[Thm - Pullback Commutes with d for Forms on Manifolds]]), but follows from the uniqueness of $d$ once one checks that $F^* \circ d$ satisfies the four defining axioms.

**Why insist on the manifold setting if the local formula reduces to MA IV's?** Because the manifold setting unifies "change of coordinates" with "evaluation on a parametrized submanifold" with "pullback along an embedding": all three are instances of the single operation $F^*$. In particular, every coordinate computation on a manifold is a pullback computation — pullback along the chart map. Recognizing this unifies a lot of vector calculus.

---

# The Definition

Let $F : M \to N$ be a smooth map between smooth manifolds. The **pullback** of a differential $k$-form $\omega \in \Omega^k(N)$ along $F$ is the differential $k$-form $F^*\omega \in \Omega^k(M)$ defined by
$$(F^*\omega)_p(v_1, \dots, v_k) = \omega_{F(p)}\!\big(dF_p(v_1), \dots, dF_p(v_k)\big)$$
for all $p \in M$ and $v_1, \dots, v_k \in T_pM$.

**On $0$-forms.** For $f \in \Omega^0(N) = C^\infty(N)$, $F^*f = f \circ F \in C^\infty(M)$. This is the only sensible definition since $0$-forms eat no vectors.

**On coordinate $1$-forms.** For $F : M \to N$ in coordinates $(V, y^j)$ on $N$ and $(U, x^i)$ on $M$, write $F^j = y^j \circ F$ for the components of $F$. Then
$$F^*(dy^j) = d(F^j) = dF^j = \sum_{i=1}^m \frac{\partial F^j}{\partial x^i}\,dx^i.$$
This is the chain rule packaged as a pullback identity.

**On general $k$-forms.** For $\omega = \sum'_J \omega_J(y)\,dy^J$ with $J = (j_1, \dots, j_k)$ increasing,
$$F^*\omega = \sum'_J (\omega_J \circ F)\,(F^*dy^{j_1}) \wedge \cdots \wedge (F^*dy^{j_k}) = \sum'_J(\omega_J \circ F)\,dF^{j_1} \wedge \cdots \wedge dF^{j_k}.$$
Each $dF^{j_i}$ is expanded via the chain rule, and the wedges are simplified.

**Key properties.** The pullback satisfies, for all smooth $F : M \to N$, $G : L \to M$, and forms $\omega \in \Omega^k(N), \eta \in \Omega^\ell(N)$:

1. **$\mathbb{R}$-linearity:** $F^*(\omega + \eta) = F^*\omega + F^*\eta$, $F^*(c\omega) = c\,F^*\omega$.
2. **Wedge homomorphism:** $F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$.
3. **Contravariant composition:** $(F \circ G)^*\omega = G^*(F^*\omega)$.
4. **Naturality with $d$:** $F^*(d\omega) = d(F^*\omega)$. (See [[Thm - Pullback Commutes with d for Forms on Manifolds]].)
5. **Top-degree Jacobian formula:** If $\dim M = \dim N = n$ and $\omega = u\,dy^1 \wedge \cdots \wedge dy^n$ near $F(p)$, then in local coordinates near $p$,
$$F^*(u\,dy^1 \wedge \cdots \wedge dy^n) = (u \circ F)\,(\det DF)\,dx^1 \wedge \cdots \wedge dx^n,$$
where $DF$ is the Jacobian matrix in the chosen charts. This is Lee Proposition 14.20.
6. **Defined for every smooth $F$:** no diffeomorphism hypothesis is needed; the construction works universally.

**Universal property.** The pullback is the unique linear operator $F^* : \Omega^\bullet(N) \to \Omega^\bullet(M)$ such that it agrees with composition on functions ($F^*f = f \circ F$ for $f \in \Omega^0$), preserves wedge products, and is functorial. Uniqueness lets one *recognize* $F^*$ in disguise: any operator satisfying the universal property must be the pullback.

**Pushforward vs. pullback.** The pullback is the *only* universal functorial operation between forms on different manifolds. There is *no* universal "pushforward of forms" along a smooth map. (When $F$ is a diffeomorphism, one *can* define $F_* = (F^{-1})^*$ from forms on $M$ to forms on $N$, but this requires $F$ to be invertible.) This asymmetry favors forms over vector fields for global manifold computations.

---

# Categorical Definition

The pullback is what makes the calculus of differential forms a **contravariant functor** from the category of smooth manifolds (objects: smooth manifolds; morphisms: smooth maps) to the category of differential graded algebras (or, for fixed $k$, to graded-commutative algebras). The functor sends:
- a smooth manifold $M$ to its DGA of forms $(\Omega^\bullet(M), \wedge, d)$;
- a smooth map $F : M \to N$ to the *backward* DGA homomorphism $F^* : \Omega^\bullet(N) \to \Omega^\bullet(M)$.

Contravariance is encoded in property 3: $(F \circ G)^* = G^* \circ F^*$, the order reversal.

Properties 1 and 2 say the pullback respects the algebra structure (it is a graded algebra homomorphism). Property 4 says it respects the differential. So the pullback is a homomorphism of differential graded algebras.

Because the pullback respects $d$, it descends to cohomology: $F^*$ sends closed forms to closed forms (since $F^*(d\omega) = d(F^*\omega)$) and exact forms to exact forms (since $F^*(d\eta) = d(F^*\eta)$). Therefore $F^*$ induces a linear map on de Rham cohomology, $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$, and $H^k_{dR}$ is a **contravariant functor** from smooth manifolds to vector spaces (in fact to graded-commutative algebras when all $k$ are bundled together).

The functoriality of $H^k_{dR}$ is a powerful tool. For instance, if $F : M \to N$ is a diffeomorphism, $F^*$ is an isomorphism on cohomology, so $H^k_{dR}(M) \cong H^k_{dR}(N)$ as vector spaces. More remarkably, **homotopic maps induce the same map on cohomology** (the homotopy invariance of de Rham cohomology, proved using the Poincaré lemma machinery in [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]]), so $F^* = G^*$ on $H^k_{dR}$ whenever $F$ and $G$ are smoothly homotopic.

---

# Relate to Other Fields / Compression

**The pullback is the change-of-variables formula promoted from a theorem to an operation.** In MA III the change-of-variables formula is proved as a substantial theorem about Riemann integrals: $\int_\Omega f = \int_O (f \circ F) |\det DF|$. In the calculus of forms, this becomes a one-line algebraic identity courtesy of property 5: $F^*(u\,dy^1 \wedge \cdots \wedge dy^n) = (u \circ F)(\det DF)\,dx^1 \wedge \cdots \wedge dx^n$ — the Jacobian determinant is *produced automatically* by the wedge product, with no additional theorem invoked. The only residue is the sign: the form-integral uses $\det DF$, not $|\det DF|$, which is why integration of forms requires orientation. See [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]].

**Bridge to MA IV.** The manifold pullback restricts in any chart to the [[Def - Pullback of a Differential Form|MA IV pullback]] on Euclidean space. The MA IV theory is the local model; the manifold theory is the global packaging, with the new feature being that pullback along an arbitrary smooth map (e.g., the inclusion of a submanifold, the parametrization of an embedded surface, the projection in a fibre bundle) is meaningful, not just pullback along diffeomorphisms or coordinate changes.

**True name:** The pullback is "evaluate the form at the image, after pushing the tangent vectors forward via $dF$." The operational form is: see a smooth map and a form on the target, write $F^*\omega$, and use the chain rule.

A trigger-reaction pattern: **see "compute a form in new coordinates" / "evaluate a form on a parametrized submanifold" / "transform a form between frames" → think "pullback"**. All of these are instances of $F^*$ for an appropriate $F$. In particular: a change of chart $(U, x^i) \to (\tilde U, \tilde x^j)$ is a pullback along the inverse transition map; an integration over a parametrized $k$-submanifold is the pullback of the integrand to the parameter domain; a gauge transformation in physics is a pullback along the gauge map.

**Bridge to tensor fields (DG VII).** The pullback of a $k$-form is a special case of the [[Def - Pullback of a Covariant Tensor Field|pullback of a covariant tensor field]], restricted to the alternating subbundle. The whole apparatus of tensor pullback applies; the new feature for forms is the commutation $F^*d = dF^*$, which has no analogue for general tensor fields (there is no canonical chart-independent $d$ on tensor fields without choosing a connection).

**Bridge to gauge theory.** In gauge theory the connection $1$-form $A$ on a principal bundle transforms by pullback under a gauge transformation $g : M \to G$: $A \mapsto g^{-1}\,A\,g + g^{-1}\,dg$. Both terms involve pullbacks (the second is a Maurer–Cartan-type pullback of the Cartan form on $G$). The whole framework of gauge invariance is the framework of pullback-equivariance.

**Bridge to algebraic geometry.** In algebraic geometry the pullback of differential forms along a morphism of schemes is the analogous construction with Kähler differentials. The de Rham complex of an algebraic variety is then pullback-functorial in the same way, and **algebraic de Rham cohomology** is the analytic-input-free analogue of $H^k_{dR}$. The whole structure of the form-side machinery transports.

---

# Examples / Corollaries

**Is an instance — pulling back $dy$ along the identity in polar coordinates.** Let $F : \mathbb{R}^2 \to \mathbb{R}^2$ be $F(r, \theta) = (r\cos\theta, r\sin\theta)$, viewed as an expression for the same point in two coordinate systems. Then $F^*dx = d(r\cos\theta) = \cos\theta\,dr - r\sin\theta\,d\theta$ and $F^*dy = d(r\sin\theta) = \sin\theta\,dr + r\cos\theta\,d\theta$. Wedging,
$$F^*(dx \wedge dy) = (\cos\theta\,dr - r\sin\theta\,d\theta) \wedge (\sin\theta\,dr + r\cos\theta\,d\theta) = r\,dr \wedge d\theta.$$
The coefficient $r$ is precisely the polar Jacobian $\det DF = r\cos^2\theta + r\sin^2\theta = r$. The change-of-variables identity $dx\,dy = r\,dr\,d\theta$ is the top-degree pullback identity.

**Is an instance — pullback along an inclusion.** Let $\iota : S^2 \hookrightarrow \mathbb{R}^3$ be the inclusion of the unit sphere. The $2$-form $\omega = x\,dy \wedge dz + y\,dz \wedge dx + z\,dx \wedge dy$ on $\mathbb{R}^3$ pulls back to a $2$-form $\iota^*\omega$ on $S^2$, which is in fact the round volume form. The pullback formula (using the parametrization $\iota = (\sin\phi\cos\theta, \sin\phi\sin\theta, \cos\phi)$ for spherical coordinates) gives $\iota^*\omega = \sin\phi\,d\phi \wedge d\theta$, the area element of $S^2$. See Lee Problem 14-6.

**Is an instance — pullback along a curve.** Let $\gamma : [a, b] \to M$ be a smooth curve and $\omega$ a $1$-form on $M$. Then $\gamma^*\omega$ is a $1$-form on $[a, b]$, specifically $\gamma^*\omega = \omega_\gamma(\dot\gamma)\,dt$ where $\dot\gamma$ is the velocity. The line integral $\int_\gamma\omega = \int_a^b \gamma^*\omega$ is, by this identity, an honest integral over $[a, b]$.

**Is NOT an instance — pushing a form forward along a non-invertible map.** The projection $F : \mathbb{R}^2 \to \mathbb{R}$, $F(x, y) = x$, is smooth but not injective. The $1$-form $\omega = y\,dx + x\,dy$ on $\mathbb{R}^2$ has no sensible "pushforward" to $\mathbb{R}$: along a fibre $F^{-1}(x_0) = \{(x_0, y) : y \in \mathbb{R}\}$, the form $\omega$ takes infinitely many different "values" (different functions of $y$), with no canonical choice. The natural operation in this direction is the *pullback* of forms on $\mathbb{R}$ to $\mathbb{R}^2$, which is well-defined: $F^*(dx) = dx$ on $\mathbb{R}^2$.

**Is NOT an instance — pulling back a vector field.** Vector fields cannot be pulled back, only pushed forward, and even then only along diffeomorphisms (or along surjective submersions in special cases). The asymmetry "pullback for forms is always defined; pushforward for vectors is restricted" is the structural fact this definition makes precise.

**Corollary — pullback under a constant map.** If $F : M \to N$ is the constant map $F(p) = q_0$ for all $p$, then $dF_p = 0$, so $(F^*\omega)_p(v_1, \dots, v_k) = \omega_{q_0}(0, \dots, 0) = 0$ for $k \geq 1$, and $F^*\omega = 0$. On $0$-forms (functions), $F^*f = f \circ F = f(q_0)$, the constant function. So constant maps kill all positive-degree forms — the pullback "sees" only the value of a $0$-form at one point.

**Corollary — pullback when the source has lower dimension.** If $\dim M < k$, then $\Omega^k(M) = 0$, and $F^*\omega = 0$ trivially for any $\omega \in \Omega^k(N)$. For example, the volume form $dx \wedge dy \wedge dz$ on $\mathbb{R}^3$ pulls back to zero along any smooth curve $\gamma : \mathbb{R} \to \mathbb{R}^3$, regardless of how the curve is parametrized.

**Corollary — composition law.** If $F : M \to N$ and $G : N \to P$ are smooth maps, then $(G \circ F)^* = F^* \circ G^*$ on forms. Compositions of pullbacks compose in the reverse order — pure contravariance.

**Calibration check.** Verify $F^*(dx + dy) = du + dv$ for $F : \mathbb{R}^2 \to \mathbb{R}^2$, $F(u, v) = (u, v)$; compute $F^*(x\,dy)$ for $F(u, v) = (u^2, v)$ (answer: $u^2\,dv$); confirm that $F^*(dx \wedge dy) = (\det DF)\,du \wedge dv$ for any smooth $F : \mathbb{R}^2 \to \mathbb{R}^2$; check that the pullback of the volume form on $\mathbb{R}^3$ to a parametrized curve $\gamma : \mathbb{R} \to \mathbb{R}^3$ is zero. If you can also explain why pullback reverses composition while vector pushforward (where defined) does not, you have understood contravariance.

---

# Unlocked by This

> [!tip] Naturality of $d$ and de Rham Functoriality *(this chapter)*
> Because $F^*$ commutes with $d$, every smooth map $F : M \to N$ induces a map on de Rham cohomology, $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$. Moreover homotopic maps induce equal cohomology maps. Read [[Thm - Pullback Commutes with d for Forms on Manifolds]].

> [!tip] Change of Variables Formula *(from Integration on Manifolds)*
> The pullback of a top-degree form picks up the determinant of the Jacobian: $F^*(u\,dy^1 \wedge \cdots \wedge dy^n) = (u\circ F)(\det DF)\,dx^1 \wedge \cdots \wedge dx^n$. The change-of-variables formula for integration on manifolds, $\int_M F^*\omega = \int_N \omega$ when $F$ is an orientation-preserving diffeomorphism, follows. See [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

> [!tip] Gauge Transformations *(from Gauge Theory / Electromagnetism)*
> Pullback is the mathematical content of a **change of gauge** or a **change of frame**. In gauge theory the connection $1$-form and curvature $2$-form transform by pullback under a gauge transformation $g : M \to G$; physically meaningful quantities are exactly those invariant under all such pullbacks — a continuation of the principle that forms exist to make constructions coordinate-free.

> [!tip] Cotangent Functor and the Cotangent Bundle *(from DG VI)*
> The pullback of forms is the section-level shadow of the **cotangent functor**: a smooth map $F : M \to N$ induces a bundle map $T^*N|_F \to T^*M$ in the *opposite* direction. The cotangent bundle is contravariant in a way that the tangent bundle (which is covariant) is not, and this asymmetry is the bundle-level statement of "forms can be pulled back universally; vectors cannot be pushed forward universally."

> [!tip] Maurer–Cartan Form on a Lie Group *(from Differential Geometry XI)*
> On a Lie group $G$ with Lie algebra $\mathfrak{g}$, the **Maurer–Cartan form** $\theta \in \Omega^1(G; \mathfrak{g})$ is defined by $\theta_g(v) = (dL_{g^{-1}})_g(v)$, the left-translation of $v$ back to $T_e G = \mathfrak{g}$. The whole theory of left-invariant differential forms on $G$ is the theory of pullbacks of $\theta$ under group multiplication and its derivatives, and the Maurer–Cartan equation $d\theta + \tfrac12[\theta, \theta] = 0$ is the structure equation of $G$. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].
