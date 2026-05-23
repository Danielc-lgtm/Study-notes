---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Affine Connection on a Vector Bundle"
  - "Def - Covariant Derivative along a Curve"
  - "Def - Christoffel Symbols"
tags: [geometry, riemannian-geometry, connections]
---

# Notation

$(M, \nabla)$ — a smooth manifold with an affine connection on $TM$ (or more generally a connection on a vector bundle $E \to M$). $\gamma : [a, b] \to M$ — a piecewise smooth curve from $p = \gamma(a)$ to $q = \gamma(b)$. $P_\gamma$ or $P_\gamma^{b \leftarrow a}$ — the **parallel transport operator** along $\gamma$ from $a$ to $b$, a linear map $T_pM \to T_qM$ (or more generally $E_p \to E_q$). $V(t)$ — the parallel transport at parameter $t$, with $V(a)$ the initial condition. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Axiom Motivation

The motivation for parallel transport is the original motivation for the entire chapter: **how do you compare tangent vectors at two different points of a manifold?** On $\mathbb{R}^n$ the comparison is free — both tangent spaces are canonically copies of $\mathbb{R}^n$ and you can just subtract. On a curved manifold the comparison requires data: you have to specify *how* you are going to move the vector from one point to the other.

The connection provides this. Given a curve $\gamma$ from $p$ to $q$, and given a vector $v \in T_pM$, declare that the vector "transported along $\gamma$" is the unique vector $V(t)$ along $\gamma$ that *does not change* — meaning $\nabla_t V = 0$. The natural requirement is: a vector that is being parallel-transported has zero covariant derivative. In components this is
$$
\dot V^k(t) + \Gamma^k_{ij}(\gamma(t))\,\dot\gamma^i(t)\,V^j(t) = 0,
$$
a first-order linear ODE in the components $V^k(t)$. By the standard ODE existence-uniqueness theorem (Picard-Lindelöf, on the maximal interval given by the linearity and continuity of the coefficients), this ODE has a unique solution for every initial condition $V(a) \in T_{\gamma(a)}M$, and the solution is defined on the entire parameter interval $[a, b]$ (linear ODEs do not blow up in finite time).

The resulting **parallel transport map** $P_\gamma : T_pM \to T_qM$ sends $v$ to the value $V(b)$ of the unique parallel section starting at $v$. It is **linear** because the parallel-transport ODE is linear and its solution depends linearly on the initial condition. It is **bijective** with inverse $P_{\gamma^{-1}}$ (parallel transport along the reverse curve $\gamma^{-1}(t) = \gamma(a + b - t)$), because parallel transport in the opposite direction undoes parallel transport in the original direction (running the ODE backward). So $P_\gamma$ is a linear isomorphism between the two tangent spaces.

**Why is parallel transport path-dependent?** On a curved manifold, the parallel-transport map $P_\gamma$ depends on the specific curve $\gamma$, not just on its endpoints $p, q$. This is the *defining feature* of a non-flat connection. The most vivid illustration is the round 2-sphere: parallel-transport a vector from the north pole down a meridian to the equator, then along the equator to a point 90° east, then back up another meridian to the north pole. The vector returns rotated by 90° — see [[Ex - Parallel Transport around a Geodesic Triangle on the Sphere]]. The same starting vector returns *unchanged* if you parallel-transport along a path that immediately retraces itself. The path-dependence is genuine, and the deviation from path-independence is exactly what the **curvature tensor** measures: around a small parallelogram with sides $\varepsilon X, \varepsilon Y$ at $p$, the parallel-transport holonomy is $\mathrm{id} - \varepsilon^2 R(X, Y) + O(\varepsilon^3)$, where $R(X, Y) : T_pM \to T_pM$ is the curvature operator.

**Why no other axioms?** The parallel-transport ODE $\nabla_t V = 0$ is the *minimal* condition that defines parallel transport — anything weaker (e.g., $V$ stays close to its initial value) is too weak to pick out a unique vector; anything stronger (e.g., $V$ is invariant under some symmetry group) requires extra structure. The ODE is what the abstract connection delivers, and the existence-uniqueness of solutions is what makes parallel transport a well-defined linear isomorphism. Once parallel transport is defined, it can be characterised in many equivalent ways — the "true name" below gives one such characterisation — but the *definition* is just "solution of the parallel-transport ODE".

**Why does linearity matter?** Parallel transport is linear: $P_\gamma(av + bw) = aP_\gamma v + bP_\gamma w$. This is what makes it useful — it means parallel transport extends from individual vectors to entire linear [[Def - Subspace|subspaces]], and from a single basis to all linear combinations. In a Riemannian manifold with metric-compatible connection ([[Def - Metric-Compatible Connection]]), parallel transport is also an *[[Def - Isometry|isometry]]*: $g(P_\gamma v, P_\gamma w) = g(v, w)$ ([[Thm - Parallel Transport is an Isometry for Metric-Compatible Connections]]). So lengths and angles are preserved along parallel transport — this is what makes the connection "metric-compatible" geometrically meaningful.

---

# The Definition

Let $(M, \nabla)$ be a smooth manifold with an affine connection on $TM$, and let $\gamma : [a, b] \to M$ be a smooth curve from $p = \gamma(a)$ to $q = \gamma(b)$. A vector field $V$ along $\gamma$ is called **parallel** (or **covariantly constant**) if its [[Def - Covariant Derivative along a Curve|covariant derivative]] vanishes:
$$
\nabla_t V \equiv 0 \quad \text{for all } t \in [a, b].
$$
In local coordinates this is the **parallel transport ODE**
$$
\dot V^k(t) + \Gamma^k_{ij}(\gamma(t))\,\dot\gamma^i(t)\,V^j(t) = 0,
$$
a system of linear first-order ODEs in the components $V^k(t)$.

The **parallel transport** of $v \in T_pM$ along $\gamma$ is the value $V(b) \in T_qM$ of the unique parallel vector field with initial condition $V(a) = v$. This defines the **parallel transport operator**
$$
P_\gamma = P_\gamma^{b \leftarrow a} : T_pM \to T_qM, \qquad v \mapsto V(b).
$$
By the existence-uniqueness theorem for linear ODEs, $P_\gamma$ is a **linear isomorphism**. Its inverse is parallel transport along the reverse curve: $(P_\gamma)^{-1} = P_{\gamma^{-1}}$ where $\gamma^{-1}(t) = \gamma(a + b - t)$.

**Composition.** Parallel transport is compatible with concatenation of curves: if $\gamma_1 : [a, b] \to M$ ends where $\gamma_2 : [b, c] \to M$ begins, and $\gamma_1 \cdot \gamma_2$ is the concatenation, then $P_{\gamma_1 \cdot \gamma_2} = P_{\gamma_2} \circ P_{\gamma_1}$.

**Generalisation to a vector bundle.** The same definition applies to any affine connection $\nabla$ on a vector bundle $E \to M$. Parallel transport along $\gamma$ is the linear isomorphism $P_\gamma : E_p \to E_q$ sending $v \in E_p$ to the value $V(b)$ of the unique parallel section of $\gamma^*E$ starting at $v$. In a local frame $(e_a)$ for $E$ with connection 1-forms $\omega^a{}_b$, the parallel-transport ODE is $\dot V^b + \omega^b{}_a(\dot\gamma(t))\,V^a = 0$.

**Piecewise smooth curves.** For piecewise smooth curves (curves with finitely many corners), parallel transport is defined by composition: parallel-transport along each smooth segment in turn. Equivalently, $P_\gamma$ is the time-ordered exponential of $-\int_a^b \omega(\dot\gamma)\,dt$ along the curve, formally $P_\gamma = \mathcal{T}\exp\bigl(-\int_a^b \omega(\dot\gamma)\,dt\bigr)$, the path-ordered exponential familiar from gauge theory.

---

# Relate to Other Fields / Compression

The compression: **parallel transport is the solution operator of the linear ODE $\nabla_t V = 0$, the equation declaring "$V$ does not change along $\gamma$".** It is the device that allows tangent vectors at different points to be compared, with the catch that the comparison depends on the path.

In **gauge theory**, parallel transport is called the **Wilson line** (in field theory) or the **holonomy** (in differential geometry). The closed-loop version — parallel transport around a closed curve back to the starting point — is the **Wilson loop** $W(\gamma) = \mathrm{tr}\,P_\gamma$, a fundamental gauge-invariant observable. In **lattice gauge theory** the path-ordered exponential is replaced by a product of group-valued **link variables** $U_{ij} \in G$ on each edge of a discrete lattice, and the discrete approximation of the curvature is the **plaquette variable** — the parallel-transport around the smallest loop. The connection between discrete and continuous parallel transport is the basis of how lattice computations approximate continuum gauge theory.

**True name:** The "true name" of parallel transport is **the horizontal lift of a curve to the total space of the bundle**. Given a connection on $E \to M$, the connection determines a **horizontal distribution** $H \subset TE$ — a subbundle of $TE$ everywhere complementary to the vertical distribution $V = \ker(d\pi)$. A curve $\tilde\gamma : [a, b] \to E$ in the total space is **horizontal** if its velocity lies in $H$. The **horizontal lift** of $\gamma$ starting at $v \in E_p$ is the unique horizontal curve $\tilde\gamma$ with $\tilde\gamma(a) = v$ and $\pi \circ \tilde\gamma = \gamma$. Parallel transport is then $P_\gamma(v) = \tilde\gamma(b)$. This perspective is the conceptual root of the **Ehresmann definition** of a connection: a connection is the data of a horizontal distribution, and parallel transport is the resulting "horizontal flow" along curves in $M$.

---

# Examples / Corollaries

**Example: parallel transport on Euclidean $\mathbb{R}^n$.** All Christoffel symbols vanish, so the parallel-transport ODE is just $\dot V^k = 0$, meaning the components are constant. Parallel transport is **trivial**: $P_\gamma v = v$ for *every* curve $\gamma$ and every $v$ — the same vector at every point. This is consistent with $\mathbb{R}^n$ having a canonical "comparison of tangent vectors at different points", and reflects the fact that the flat connection has zero curvature so parallel transport is path-independent.

**Example: parallel transport along a meridian on $S^2$.** Take the round sphere, and parallel-transport a vector along a meridian from the equator to the north pole. The meridian is a great circle (a geodesic), so its velocity vector is parallel along itself. Any tangent vector decomposes into a component along the meridian (parallel-transported as a multiple of $\dot\gamma$, which is parallel) and a component perpendicular to the meridian (parallel-transported as a multiple of the orthogonal direction, which is also parallel because rotating to follow the orthogonal direction is what an isometric rotation does). So parallel transport along the meridian preserves the angle of the vector to the meridian — the vector rotates with the geometry. Concretely, a vector pointing "east" at the equator becomes a vector pointing "east" at the north pole (after the natural identification by symmetry).

**Example: parallel transport along a circle of latitude on $S^2$.** A non-geodesic loop. Parallel-transport a vector around the circle of constant latitude $\theta_0$ for one full revolution. The resulting vector has rotated by an angle $2\pi(1 - \cos\theta_0)$. This is the **holonomy angle** of the loop. Note: a circle near the equator ($\theta_0$ near $\pi/2$, so $\cos\theta_0$ near $0$) has holonomy near $2\pi$ — almost no rotation. A circle near the pole ($\theta_0$ near $0$, $\cos\theta_0$ near $1$) has holonomy near $0$. The intermediate case is the source of the apparent rotation of the **Foucault pendulum** plane: the pendulum swing direction is parallel-transported along the Earth's daily latitude circle, and the rotation rate is $2\pi(1 - \cos\theta_0)/24\,\text{h}$.

**Example: parallel transport on a Lie group with bi-invariant metric.** On a Lie group $G$ with bi-invariant metric, the Levi-Civita connection has $\nabla_X Y = \tfrac{1}{2}[X, Y]$ on left-invariant fields. Parallel transport along a one-parameter [[Def - Subgroup|subgroup]] $\gamma(t) = \exp(tX)$ takes a left-invariant vector $Y$ at the identity to the left-invariant vector $\mathrm{Ad}_{\exp(tX/2)}(Y)$ at $\exp(tX)$. This is the special parallel-transport formula for compact Lie [[Def - Group|groups]] and is central to harmonic analysis on Lie groups.

**Non-example: "parallel" as "constant Cartesian components".** On a curved manifold there is no canonical identification of $T_pM$ with $T_qM$, so "constant Cartesian components" depends on a choice of chart and is not parallel transport. On $\mathbb{R}^n$ with the standard metric and Cartesian coordinates the two notions coincide, but this is special to the flat-metric-in-Cartesian-coordinates case.

**Non-example: "parallel" as "constant length".** Even on a Riemannian manifold with metric-compatible connection, parallel transport preserves length, but not every length-preserving transport is parallel transport. The Lie-derivative-based transport along the flow of a Killing field is length-preserving but generally not parallel — it differs from parallel transport by an antisymmetric infinitesimal rotation determined by the Killing field.

**Corollary (parallel transport is the only natural way to compare vectors).** Once a connection is fixed, parallel transport is the *canonical* way to compare a vector at $p$ with one at $q$. But it depends on a path. So there is no canonical comparison of $T_pM$ with $T_qM$ that depends only on the endpoints — that would require a connection with vanishing curvature on a simply connected region. The path-dependence of parallel transport is exactly the obstruction.

**Corollary ([[Def - Geodesic|geodesics]] are auto-parallel).** The defining equation of a geodesic is $\nabla_t\dot\gamma = 0$ — which says the velocity vector is parallel-transported along the curve itself. So a geodesic is a curve whose tangent vector is "auto-parallel": the parallel transport of $\dot\gamma(a)$ along $\gamma$ is exactly $\dot\gamma(t)$ for every $t$. This is the abstract statement of "a geodesic is a straight line" — the velocity does not change.

**Corollary (the holonomy group at a point).** Fix $p \in M$ and consider all piecewise smooth loops at $p$. The set of parallel-transport maps $\{P_\gamma : T_pM \to T_pM \mid \gamma \text{ a loop at } p\}$ forms a subgroup of $\mathrm{GL}(T_pM)$ called the **holonomy group** $\mathrm{Hol}(p, \nabla)$. For a metric-compatible connection it is a subgroup of $O(T_pM, g_p)$, and for a torsion-free metric-compatible connection (the Levi-Civita case) it is a subgroup of $\mathrm{SO}(T_pM, g_p)$ if $M$ is orientable. The **Ambrose-Singer theorem** says the Lie algebra of the holonomy group is spanned by the curvature operators $R(X, Y)$ at points reachable from $p$ by parallel transport. **Berger's classification** (1955) catalogues the possible irreducible holonomy groups of complete simply-connected Riemannian manifolds: $\mathrm{SO}(n)$ (generic), $U(n)$ (Kähler), $SU(n)$ (Calabi-Yau), $\mathrm{Sp}(n)$ and $\mathrm{Sp}(n)\cdot\mathrm{Sp}(1)$ (hyperkähler, quaternion-Kähler), $G_2$, $\mathrm{Spin}(7)$ — a finite list with each entry corresponding to a special geometric structure.

**Calibration check.** If you can perform the following three computations, you have understood parallel transport. (i) Verify by direct ODE solution that on Euclidean $\mathbb{R}^2$ in polar coordinates, parallel transport along a circle preserves Cartesian components (despite the polar components rotating). (ii) Compute the holonomy angle for parallel transport around a circle of latitude on the unit sphere, deriving the formula $2\pi(1 - \cos\theta_0)$. (iii) Show that for a connection with zero curvature on a simply-connected manifold, parallel transport depends only on the endpoints, not the path — by reducing to Stokes' theorem applied to the closed 1-form encoding parallel transport.

---

# Unlocked by This

> [!tip] Holonomy Groups and Berger's Classification *(from Differential Geometry / Riemannian Geometry)*
> The **holonomy group** $\mathrm{Hol}(p, \nabla)$ of a connection $\nabla$ at a point $p$ is the group of all parallel-transport maps along loops at $p$. For Levi-Civita connections it is a closed subgroup of $\mathrm{SO}(n)$, and **Berger's theorem** (1955) classifies the irreducible holonomy groups of complete simply-connected Riemannian manifolds: $\mathrm{SO}(n)$ (generic), $U(n)$ (Kähler), $SU(n)$ (Calabi-Yau), $\mathrm{Sp}(n)$, $\mathrm{Sp}(n)\mathrm{Sp}(1)$ (quaternion-Kähler), $G_2$, $\mathrm{Spin}(7)$. Each special holonomy corresponds to a special geometric structure with deep connections to string theory, mirror symmetry, and gauge theory. The **Ambrose-Singer theorem** identifies the Lie algebra of $\mathrm{Hol}$ with the span of curvature tensor values, completing the bridge from local curvature to global holonomy.

> [!tip] The Wilson Line and Lattice Gauge Theory *(from Gauge Theory and Mathematical Physics)*
> In gauge theory, parallel transport is called the **Wilson line** and the closed-loop version $W(\gamma) = \mathrm{tr}\,P_\gamma$ is the **Wilson loop**, a fundamental gauge-invariant observable. In **lattice gauge theory** the path-ordered exponential is approximated by a product of $G$-valued link variables, and the discrete plaquette variables approximate the curvature 2-form $F = dA + A \wedge A$. The Wilson-loop expectation value $\langle W(\gamma)\rangle$ encodes the confining vs. Coulomb-phase structure of the gauge theory (Wilson's area-law-vs-perimeter-law criterion for confinement), and is one of the most-studied observables in nonperturbative QCD.

> [!tip] The Geodesic Equation and the Exponential Map *(from Riemannian Geometry)*
> A **geodesic** is a curve along which the velocity is parallel-transported — $\nabla_t\dot\gamma = 0$. By the existence-uniqueness of the parallel-transport ODE, every initial velocity $v \in T_pM$ generates a unique geodesic $\gamma_v$ with $\gamma_v(0) = p$, $\dot\gamma_v(0) = v$, defined on a maximal interval. The **exponential map** $\exp_p : V \subseteq T_pM \to M$ sends $v$ to $\gamma_v(1)$ and is a local diffeomorphism around $0$; its inverse gives **normal coordinates** in which the metric is Euclidean at $p$ to first order. The full theory is the content of [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].
