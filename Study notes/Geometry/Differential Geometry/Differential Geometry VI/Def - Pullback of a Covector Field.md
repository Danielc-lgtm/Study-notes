---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Covector Field and Differential 1-Form"
  - "Def - The Differential of a Smooth Map"
  - "Def - Smooth Map between Manifolds"
  - "Def - Dual Map"
tags: [geometry, differential-geometry, pullback, naturality]
---

# Notation

$F : M \to N$ is a smooth map between smooth manifolds. $\omega \in \Omega^1(N)$ is a covector field (1-form) on $N$. The pullback is denoted $F^*\omega \in \Omega^1(M)$, with $F^*\omega \in $ the space of 1-forms on $M$. At a point $p \in M$, $(F^*\omega)_p$ is a covector at $p$, paired with tangent vectors at $p$. The differential $dF_p : T_pM \to T_{F(p)}N$ is the bundle differential at $p$ (see [[Def - The Differential of a Smooth Map]]).

---

# Axiom Motivation

The pullback of a covector field exists because **covectors are evaluable, and the natural way to transport them along a smooth map is by precomposition with the differential**. The construction is forced by the operational signature of covectors and tangent vectors, and is the structural reason covector fields enjoy a universal naturality that vector fields lack.

Begin with the pointwise picture. At $p \in M$, we have the tangent space $T_pM$ and its differential $dF_p : T_pM \to T_{F(p)}N$. At $q = F(p) \in N$, we have the cotangent space $T_q^*N$. A covector $\omega_q \in T_q^*N$ is a linear functional on $T_qN$. We want to define a covector at $p$ — that is, a linear functional on $T_pM$ — out of these data.

The natural construction: given $\omega_q$ and $dF_p$, the composition $\omega_q \circ dF_p : T_pM \to T_qN \to \mathbb{R}$ is a linear functional on $T_pM$, i.e., an element of $T_p^*M$. This is the **dual map** of $dF_p$ in the sense of [[Def - Dual Map]] applied to $\omega_q$: $(dF_p)^*(\omega_q) = \omega_q \circ dF_p \in T_p^*M$. So we define $(F^*\omega)_p := \omega_{F(p)} \circ dF_p$.

This definition has three remarkable features.

**First, it works for arbitrary smooth $F$.** No invertibility, no diffeomorphism — just smoothness suffices, because the construction only needs $dF_p$ (which exists for any smooth $F$) and the pointwise evaluation of $\omega$ at $F(p)$. This is unlike the pushforward of vector fields, which requires $F$ to be a diffeomorphism.

**Second, the construction is contravariant.** $F^*$ goes from forms on $N$ (the target of $F$) to forms on $M$ (the source). This is the opposite direction from $F$ itself. The contravariance is structural: it comes from the dual-map structure of $(dF_p)^*$, which reverses arrows.

**Third, the pullback is natural in the strongest sense.** $(F \circ G)^* = G^* \circ F^*$ for composable smooth maps, $\mathrm{id}_M^* = \mathrm{id}_{\Omega^1(M)}$, and pullback commutes with the differential operator: $F^*(dg) = d(g \circ F) = d(F^*g)$ for any $g \in C^\infty(N)$. This naturality is what makes the theory of differential forms a *functor* on the category of smooth manifolds, and it is what makes de Rham cohomology a topological invariant.

What is forced by demanding $(F^*\omega)_p$ be **linear** in $v$? Linearity is automatic from $(F^*\omega)_p(v) = \omega_{F(p)}(dF_p(v))$: $dF_p$ is linear in $v$, $\omega_{F(p)}$ is linear in its argument, so the composition is linear in $v$.

What is forced by demanding $F^*\omega$ be **smooth** as a 1-form on $M$? Smoothness follows from the smoothness of $F$ (which makes $dF$ smooth on $TM$) and the smoothness of $\omega$ (which makes $\omega \circ F$ smooth as a section of $T^*N$ pulled back to $M$). Explicitly in coordinates: if $\omega = \omega_j \, dy^j$ on $N$ and $F$ has coordinate expression $y^j = F^j(x)$, then $F^*\omega = \omega_j(F(x)) \cdot (\partial F^j / \partial x^i) dx^i$, with smooth coefficients on $M$.

What is forced by demanding pullback **respect the differential operator**? The identity $F^*(dg) = d(F^*g)$ is forced by the chain rule: $(F^*(dg))_p(v) = dg_{F(p)}(dF_p(v)) = dF_p(v)(g) = v(g \circ F) = d(g \circ F)_p(v)$ — the third equality uses the duality definition of $dg$, the fourth uses the chain rule for derivations. So naturality with $d$ is *automatic*, not separately imposed.

What if we **strengthened** by demanding $F$ be a diffeomorphism? Then we could also pull back vector fields, using $F^{-1}$ — but the pullback of covectors works without this. Strengthening would lose the universal applicability.

What if we **weakened** by allowing $\omega$ to be merely continuous? Then $F^*\omega$ would be continuous but not smooth. The smooth-pullback is the special case for the smooth-forms theory.

What if we **weakened** the linearity-on-fibres of $dF_p$ — that is, if $F$ were not smooth, so $dF_p$ didn't exist? Then pullback would not be defined at all. The existence of the differential of $F$ is what makes pullback possible, and smoothness of $F$ is what makes the differential exist.

---

# The Definition

Let $F : M \to N$ be a smooth map between smooth manifolds, and let $\omega \in \Omega^1(N)$ be a smooth 1-form (covector field) on $N$. The **pullback** of $\omega$ by $F$ is the 1-form $F^*\omega \in \Omega^1(M)$ defined pointwise by
$$(F^*\omega)_p (v) := \omega_{F(p)}\bigl( dF_p(v) \bigr) \qquad \text{for every } p \in M \text{ and every } v \in T_pM,$$
where $dF_p : T_pM \to T_{F(p)}N$ is the differential of $F$ at $p$ (see [[Def - The Differential of a Smooth Map]]).

Equivalently, $(F^*\omega)_p = \omega_{F(p)} \circ dF_p \in T_p^*M$, the composition of $dF_p$ with $\omega_{F(p)}$.

**Coordinate expression.** In charts $(U, x^i)$ on $M$ and $(V, y^j)$ on $N$ with $F(U) \subseteq V$, write $F$ in coordinates as $y^j = F^j(x^1, \dots, x^m)$ (where $m = \dim M$, $n = \dim N$) and $\omega = \omega_j \, dy^j$ on $V$. Then on $U$,
$$F^*\omega = \omega_j(F(x)) \cdot \frac{\partial F^j}{\partial x^i} \, dx^i.$$
The coefficient of $dx^i$ is the pullback of the coefficient $\omega_j$ composed with $F$ (giving $\omega_j(F(x))$, a smooth function on $U$) times the Jacobian $\partial F^j / \partial x^i$.

**Pullback on functions.** For a smooth function $g \in C^\infty(N)$ (a 0-form), the pullback is the composition $F^*g := g \circ F \in C^\infty(M)$. This is consistent with the 1-form pullback formula via $F^*(dg) = d(F^*g)$ — see [[Thm - Pullback Commutes with d for 1-Forms]].

**Properties.**

- **$\mathbb{R}$-linearity:** $F^*(\omega + \eta) = F^*\omega + F^*\eta$ and $F^*(c\omega) = c F^*\omega$ for $c \in \mathbb{R}$.
- **$C^\infty$-multiplicativity:** $F^*(g \omega) = (g \circ F) \cdot F^*\omega = (F^*g) \cdot F^*\omega$ for $g \in C^\infty(N)$.
- **Functoriality:** $(G \circ F)^* = F^* \circ G^*$ for composable smooth maps $F : M \to N$, $G : N \to P$, and $\mathrm{id}_M^* = \mathrm{id}_{\Omega^1(M)}$.
- **Naturality with $d$:** $F^*(dg) = d(F^*g) = d(g \circ F)$ for $g \in C^\infty(N)$.

The pullback **does not** require $F$ to be a diffeomorphism, an immersion, an embedding, or anything other than smooth. This is the structural feature distinguishing covector fields (which pull back universally) from vector fields (which can be pushed forward only along diffeomorphisms).

---

# Relate to Other Fields / Compression

The pullback of a covector field is the **dual operation to the pushforward of a tangent vector**. Pointwise, the differential $dF_p : T_pM \to T_qN$ is a linear map. Its dual (in the sense of [[Def - Dual Map]]) is $(dF_p)^* : T_q^*N \to T_p^*M$, reversing the direction. The pullback of covector fields is the pointwise application of this dual map to the value of $\omega$ at each point.

The pullback is also a **morphism in the category of smooth manifolds**, viewed contravariantly. The assignment $F \mapsto F^*$ is the contravariant functor $\Omega^1 : \mathbf{Man}^\mathrm{op} \to \mathbf{Mod}$ from the (opposite of the) category of smooth manifolds to the category of modules (or even chain complexes, when one includes the de Rham differential). The functoriality $(G \circ F)^* = F^* \circ G^*$ is exactly the contravariant-functor axiom.

**True name:** the true name of $F^*\omega$ is "**$\omega$ composed with the differential of $F$**", or equivalently "**the covector field obtained by pulling tangent vectors at $p$ forward via $dF_p$ and evaluating $\omega$ at $F(p)$**". The operational signature: $F^*\omega$ takes a tangent vector $v$ at $p \in M$, pushes it to $dF_p(v) \in T_{F(p)}N$, and then evaluates $\omega_{F(p)}$ on that pushed vector. The verbiage "pull-back" is appropriate because the *covector field* is being pulled from $N$ to $M$, even though the *tangent vector* is being pushed.

A useful slogan: **vector fields are intrinsic to a point — they cannot be transported along non-invertible maps; covector fields are evaluators — they are transported by composition with the differential**. This is the formal source of the asymmetry between $TM$ and $T^*M$ from the perspective of category theory: $TM$ is *covariant* (functorial in the same direction as $F$), while $T^*M$ at the level of sections is *contravariant*.

In **physics**, pullback is the natural operation for restricting a field on a "big" space to a "smaller" space. The electromagnetic 4-potential $A$ on Minkowski space pulls back to any worldline (a smooth map $\gamma : \mathbb{R} \to \mathbb{R}^4$), giving the worldline's experienced potential $\gamma^*A$. The pullback to a surface (a smooth $f : \Sigma \to \mathbb{R}^4$) gives the surface's induced 1-form. This is the canonical way to compute fluxes and work integrals.

---

# Examples / Corollaries

**Is an instance — pullback of $dy$ by $F : \mathbb{R} \to \mathbb{R}^2$, $F(t) = (t, t^2)$.** $F^* dy = (\partial F^2/\partial t) dt = 2t \, dt$. Verifying via the definition: $F^*dy_t(v) = dy_{F(t)}(dF_t(v)) = dy_{(t, t^2)}(v, 2tv) = 2tv$. So $(F^*dy)_t = 2t \, dt$ as expected.

**Is an instance — pullback by the inclusion of a submanifold.** Let $\iota : S \hookrightarrow M$ be a smooth embedding of a submanifold. For $\omega \in \Omega^1(M)$, the pullback $\iota^*\omega \in \Omega^1(S)$ is the **restriction** of $\omega$ to $S$ — for $v \in T_pS \subseteq T_pM$, $(\iota^*\omega)_p(v) = \omega_p(v)$. Restriction is a special case of pullback.

**Is an instance — pullback of $dr$ by polar-to-Cartesian.** Define $F : (0, \infty) \times (0, 2\pi) \to \mathbb{R}^2$ by $F(r, \theta) = (r\cos\theta, r\sin\theta)$. On Cartesian $\mathbb{R}^2$, the 1-form $dx = $ standard differential. The pullback $F^*(dx) = \cos\theta \, dr - r \sin\theta \, d\theta$ — using $x = r\cos\theta$, $\partial x/\partial r = \cos\theta$, $\partial x/\partial \theta = -r\sin\theta$. Similarly $F^*(dy) = \sin\theta \, dr + r \cos\theta \, d\theta$.

**Is an instance — pullback of $d\theta$ on $S^1$ by the squaring map.** Let $F : S^1 \to S^1$, $F(e^{i\theta}) = e^{2i\theta}$ (the squaring map, which has degree $2$). Then $F^*(d\theta) = 2 d\theta$ — the pullback covers $S^1$ "twice", and the integral over $S^1$ doubles accordingly: $\int_{S^1} F^*(d\theta) = 2 \int_{S^1} d\theta$.

**Is NOT a pullback that respects $d$ — pullback by a non-smooth map.** If $F$ is only continuous, then $dF$ doesn't exist as a bundle homomorphism, and the formula $F^*\omega = \omega \circ dF$ does not give a well-defined 1-form. Smoothness of $F$ is essential.

**Is NOT analogous to pushforward — pullback always works.** Pushforward of vector fields requires $F$ to be a diffeomorphism. For example, with $F : \mathbb{R} \to \mathbb{R}$, $F(x) = x^2$, the vector field $X = \partial/\partial x$ does not push forward to a well-defined vector field on $\mathbb{R}$, because $F(-1) = F(1) = 1$ and $dF_{-1}(\partial/\partial x) = -2 \partial/\partial x \neq 2 \partial/\partial x = dF_1(\partial/\partial x)$ — two candidates at $y = 1$. But the pullback of a 1-form $\omega$ on $\mathbb{R}$ always works: $F^*\omega = \omega(x^2) \cdot 2x \, dx$.

**Corollary — pullback of an exact form is exact.** If $\omega = df$ for $f \in C^\infty(N)$, then $F^*\omega = F^*(df) = d(F^*f) = d(f \circ F)$ — exact, with the pullback function $f \circ F$ as its potential. So pullback preserves exactness.

**Corollary — pullback of a closed form is closed.** If $d\omega = 0$ on $N$, then $d(F^*\omega) = F^*(d\omega) = 0$ on $M$. So pullback preserves closedness. This makes pullback descend to a map on de Rham cohomology, $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$.

**Corollary — pullback of the canonical 1-form on $T^*Q$.** The canonical 1-form $\theta$ on $T^*Q$ has a universal property: it is the unique 1-form such that for every $\alpha \in \Omega^1(Q)$, $\alpha^*\theta = \alpha$ where $\alpha : Q \to T^*Q$ is the section corresponding to $\alpha$. This characterizes $\theta$ up to a sign convention.

**Corollary — pullback commutes with restriction.** If $\omega \in \Omega^1(N)$ and $U \subseteq N$ is open with $F : M \to N$ and $F^{-1}(U) \subseteq M$, then $F^*(\omega|_U) = (F^*\omega)|_{F^{-1}(U)}$. Pullback is local.

**Calibration check.** Compute $F^*(dy)$ for $F : \mathbb{R}^2 \to \mathbb{R}^2$, $F(x, y) = (x + y, xy)$, directly using the coordinate formula. Verify that $F^*(d(x + y)) = dx + dy$ on the source. Verify $F^*(dg) = d(F^*g)$ for a specific function $g$ and a specific map $F$.

---

# Unlocked by This

> [!tip] Pullback of Higher Forms *(from Differential Geometry VIII)*
> The pullback extends to all degrees: $F^* : \Omega^k(N) \to \Omega^k(M)$ for any $k \geq 0$, defined via the alternating-multilinear pairing. For $\omega \in \Omega^k(N)$, $(F^*\omega)_p(v_1, \dots, v_k) := \omega_{F(p)}(dF_p(v_1), \dots, dF_p(v_k))$. The pullback respects the wedge product ($F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$) and the exterior derivative ($F^*(d\omega) = d(F^*\omega)$), making $F^*$ a chain map of the de Rham complex.

> [!tip] de Rham Cohomology Functoriality *(from Algebraic Topology)*
> Since pullback commutes with the exterior derivative, it descends to a map $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$ on de Rham cohomology. This is the structural source of de Rham cohomology being a *contravariant functor* from smooth manifolds to graded vector spaces. The de Rham theorem then identifies $H^k_{dR}$ with singular cohomology, giving the functoriality content of "manifolds have topological invariants".

> [!tip] Yang–Mills Theory and Gauge Pullback *(from Gauge Theory)*
> In gauge theory, the **connection 1-form** on a principal bundle pulls back via gauge transformations and via local sections. The pullback of a connection by a local section gives a Lie-algebra-valued 1-form on the base — the local "gauge field" of physics. Yang–Mills equations are equations on the curvature 2-form of a connection, and pullback by local trivializations relates the global field to local "potentials" and "gauges".

> [!tip] Variational Principles and the Action Integral *(from Geometric Mechanics)*
> The action $S[\gamma] = \int_\gamma L \, dt$ in mechanics is the pullback of the Lagrangian 1-form along a path $\gamma : [a, b] \to TQ$. Varying the path $\gamma$ and computing $\delta S = 0$ gives the Euler–Lagrange equations. The pullback formalism makes the entire variational principle a coordinate-free calculus on path spaces.
