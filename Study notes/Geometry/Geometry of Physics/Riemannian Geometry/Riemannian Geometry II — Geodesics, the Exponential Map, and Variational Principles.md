---
type: topic
subject: riemannian-geometry
chapter: "10.1-10.2"
title: "Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles"
tags: [geometry, riemannian-geometry, geodesics, variational-calculus, hamiltonian-mechanics]
---

# Notation Registry

Throughout this topic $(M, g)$ is a smooth Riemannian manifold of dimension $n$, with the [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|Levi-Civita connection]] $\nabla$ uniquely determined by $g$. Almost every result we state has a Lorentzian counterpart (e.g. timelike geodesics in general relativity); see [[General Relativity I — Einstein's Equations and Schwarzschild]] for the sign nuances. **Standing convention:** unless we say otherwise, geodesics are parametrised at constant speed (the natural parametrisation produced by the geodesic equation), and the metric is positive-definite. Curves are smooth or piecewise smooth as appropriate; the regularity will be made explicit only when it matters.

- $\gamma : I \to M$ — a curve in $M$, with velocity $\dot\gamma(t) \in T_{\gamma(t)}M$
- $\nabla_{\dot\gamma}\dot\gamma$ — covariant acceleration along $\gamma$, computed using the Levi-Civita connection
- $\Gamma^k_{ij}$ — Christoffel symbols of $g$ in a chart; $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$
- $\exp_p : V_p \subseteq T_pM \to M$ — the **Riemannian exponential map** at $p$, sending $v \in T_pM$ to $\gamma_v(1)$ where $\gamma_v$ is the unique geodesic with $\gamma_v(0) = p$, $\dot\gamma_v(0) = v$
- $V_p \subseteq T_pM$ — the maximal star-shaped neighbourhood of $0$ on which $\exp_p$ is defined
- $L(\gamma) = \int_a^b |\dot\gamma|\, dt$ — the **length functional**
- $E(\gamma) = \tfrac{1}{2}\int_a^b g(\dot\gamma, \dot\gamma)\, dt$ — the **energy functional**
- $J(t)$ — a **Jacobi field** along a geodesic $\gamma$, satisfying $J'' + R(J, \dot\gamma)\dot\gamma = 0$ where $J' := \nabla_{\dot\gamma} J$ and $J'' := \nabla_{\dot\gamma}\nabla_{\dot\gamma} J$
- $R(X, Y)Z$ — the Riemann curvature tensor (see [[Riemannian Geometry III — Riemann Curvature and Topology]])
- $I(V, W) = \int_0^L \bigl(g(V', W') - g(R(V, T)T, W)\bigr)\, dt$ — the **index form** on variations $V, W$ along a unit-speed geodesic with tangent $T$
- Conjugate points: $q$ is **conjugate** to $p$ along $\gamma$ if a nonzero Jacobi field along $\gamma$ vanishes at both endpoints
- $T^*M$ — cotangent bundle, the natural phase space; $\theta = p_i\, dq^i$ — canonical 1-form; $\omega = -d\theta = dq^i \wedge dp_i$ — canonical symplectic form
- $H : T^*M \to \mathbb{R}$ — a Hamiltonian, e.g. the **kinetic-energy Hamiltonian** $H = \tfrac{1}{2}g^{ij}p_i p_j$
- $X_H$ — Hamiltonian vector field, defined by $\iota_{X_H}\omega = dH$
- $\delta$ — variation operator; $\delta q$ a virtual displacement (Lagrangian language)
- $L(q, \dot q, t)$ — a Lagrangian on $TM \times \mathbb{R}$; canonical example $L = T - V$
- $p_i = \partial L / \partial \dot q^i$ — conjugate momenta
- $d\rho = \sqrt{2(E - V(q))}\, ds$ — the **Jacobi metric** on the configuration space at fixed total energy $E$

---

# Motivation

Here is the entire topic in one sentence: **a geodesic is what becomes of "straight line" once you take the metric seriously**. Once you have a [[Def - Riemannian Metric|Riemannian metric]] and its [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|Levi-Civita connection]], you can ask the most basic question of geometry: which curves go straight? In Euclidean space a straight line is a curve whose velocity does not change. On a manifold "velocity" lives in different tangent spaces at different times, and the only way to compare them is parallel transport along the curve. A **geodesic** is therefore a curve whose velocity is parallel-transported along itself,
$$\nabla_{\dot\gamma}\dot\gamma = 0,$$
the cleanest possible equation expressing "no acceleration". In coordinates this becomes a system of second-order nonlinear ODEs, and the existence theorem for ODEs hands us, for free, a geodesic through each point in each direction.

That ODE system has an enormous payoff. It produces the **exponential map** $\exp_p : T_pM \to M$, which takes a tangent vector at $p$ and follows the geodesic in that direction for unit time. Near $0$ this map is a local [[Def - Diffeomorphism|diffeomorphism]], and its inverse gives the most precious coordinate system on a Riemannian manifold — **normal coordinates** — in which the metric looks Euclidean at the origin and the Christoffel symbols vanish there. Normal coordinates are the geometric analogue of taking a Taylor expansion: they let you treat curvature as the *correction* to a Euclidean local picture, which is exactly how all curvature theorems are proved.

The second story of this chapter is **variational**. A geodesic turns out to be a critical point of two natural functionals on curves with fixed endpoints — the **length** $L(\gamma) = \int |\dot\gamma|\, dt$ and the **energy** $E(\gamma) = \tfrac{1}{2}\int g(\dot\gamma, \dot\gamma)\, dt$. The first variation of either gives back the geodesic equation, which is one explanation for *why* the geodesic equation is the right notion of "straight": [[Def - Geodesic|geodesics]] are locally length-minimising. The second variation gives a quadratic form on variations, the **index form** $I(V, V) = \int g(V', V') - g(R(V, T)T, V)$, and through the eigenvalues of $R(\cdot, T)T$ this brings the curvature tensor directly into the variational story. Vanishing second variation in a direction means a nearby curve has the same length to first order, and the kernel — directions of vanishing second variation — is exactly the space of **Jacobi fields**. A Jacobi field is a variation of $\gamma$ through nearby geodesics; conjugate points along $\gamma$ are precisely the parameters at which a Jacobi field returns to zero. So the local geometry of geodesics, the second-order calculus of variations, and the eigenvalues of the curvature tensor are three views of one object.

The third story is **mechanics**. The geodesic equation is Hamilton's principle for the Lagrangian $L = \tfrac{1}{2}g_{ij}\dot q^i \dot q^j$ on the tangent bundle, and on the cotangent bundle this becomes Hamilton's equations for the kinetic-energy Hamiltonian $H = \tfrac{1}{2}g^{ij}p_i p_j$. Geodesic flow on $T^*M$ is the simplest non-trivial Hamiltonian system. More striking is **Jacobi's principle of least action**: a particle moving in a potential $V$ on $M$ traces a geodesic of the *conformally modified* metric $\tilde g = 2(E - V)\, g$, where $E$ is the conserved total energy. So *every* mechanical trajectory in a potential is a geodesic for some metric — classical mechanics dissolves into Riemannian geometry. This is the bridge by which the variational tradition (Maupertuis, Euler, Lagrange, Jacobi) meets the geometric one (Gauss, Riemann, Levi-Civita), and it is the framework all subsequent work in [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]] and [[General Relativity I — Einstein's Equations and Schwarzschild]] builds on.

**This chapter assumes you have absorbed [[Riemannian Geometry I — Connections and Covariant Differentiation]]** — in particular, you should be comfortable with covariant derivatives $\nabla_X Y$, the Levi-Civita connection, Christoffel symbols, and parallel transport. You should also have the smooth-manifold machinery of [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket|DG V]] (flows of vector fields) and [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]] (the Lie-group exponential, with which the Riemannian one shares its name and its idea), and you should be willing to use the ODE existence and uniqueness theorem freely.

---

# Concept Map

## §2.1 The Geodesic Equation

- **[[Def - Geodesic]]**
	- A **geodesic** is a smooth curve $\gamma : I \to M$ satisfying $\nabla_{\dot\gamma}\dot\gamma = 0$ — its velocity is parallel-transported along itself, so it has zero covariant acceleration. In coordinates this reads $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i \dot\gamma^j = 0$. Metric compatibility immediately forces $|\dot\gamma|$ constant, so geodesics carry a *natural parametrisation* up to affine reparametrisation. Examples: straight lines in $\mathbb{R}^n$, great circles on $S^n$, vertical lines and semicircles meeting the boundary perpendicularly in the [[Ex - Geodesics of the Hyperbolic Plane|hyperbolic plane]].

- **[[Thm - Existence and Uniqueness of Geodesics]]**
	- For every $p \in M$ and $v \in T_pM$ there is a unique maximal geodesic $\gamma_v$ with $\gamma_v(0) = p$ and $\dot\gamma_v(0) = v$. The proof is just the Picard–Lindelöf theorem applied to the geodesic ODE, lifted to the tangent bundle. The domain may be a proper subinterval of $\mathbb{R}$; when every maximal geodesic is defined on all of $\mathbb{R}$ we say $M$ is **geodesically complete**. Affine rescaling gives the homogeneity property $\gamma_{cv}(t) = \gamma_v(ct)$, used everywhere later.

- **[[Ex - Great Circles are the Geodesics of the Sphere]]** (⭐)
	- Verify directly from $\nabla_{\dot\gamma}\dot\gamma = 0$ that great circles on $S^n \subset \mathbb{R}^{n+1}$ are geodesics, and that nothing else is. The cleanest argument uses the second fundamental form of the embedding to reduce to "the covariant acceleration is the tangential part of the ambient acceleration".

- **[[Ex - Geodesics of the Hyperbolic Plane]]** (⭐⭐)
	- Show in the upper half-plane model $\mathbb{H}^2 = \{(x, y) : y > 0\}$ with $ds^2 = (dx^2 + dy^2)/y^2$ that the geodesics are vertical lines and semicircles meeting the $x$-axis orthogonally. Uses [[Riemannian Geometry I — Connections and Covariant Differentiation|Cartan structure equations]] to find $\Gamma^k_{ij}$ and then integrates the geodesic equation.

> [!tip] Unlocked: Sub-Riemannian Geodesics *(from Sub-Riemannian Geometry)*
> Replace "all of $T_pM$" by a smooth horizontal distribution $\mathcal{H} \subseteq TM$, and ask for the shortest horizontal curve. The geodesic equation becomes a Hamiltonian system on $T^*M$ with constraints (a presymplectic problem), and the resulting **sub-Riemannian geodesics** can do things normal geodesics cannot — for example, in the Heisenberg group the geodesic between two points often *spirals*. The theory is the geometric core of Carnot–Carathéodory geometry and of the geometry of nonholonomic mechanical systems.

> [!note] Exercise Index — §2.1
> [[Exercise Index - §2.1 The Geodesic Equation]]

## §2.2 The Exponential Map and Normal Coordinates

- **[[Def - The Riemannian Exponential Map]]**
	- For $p \in M$, the exponential map $\exp_p : V_p \subseteq T_pM \to M$ is $\exp_p(v) = \gamma_v(1)$, where $\gamma_v$ is the geodesic with $\gamma_v(0) = p$ and $\dot\gamma_v(0) = v$. The domain $V_p$ is the star-shaped subset of $T_pM$ on which the unit-time geodesic exists. The differential at the origin $d(\exp_p)_0 : T_0(T_pM) = T_pM \to T_pM$ is the identity, so by the [[Thm - The Inverse Function Theorem|inverse function theorem]] $\exp_p$ is a local diffeomorphism near $0$. The name and the linearisation match the Lie-group exponential of [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]], and on a Lie group with bi-invariant metric the two literally coincide.

- **[[Def - Normal Coordinates and Geodesic Coordinates]]**
	- **Normal coordinates** at $p$ are the coordinates produced by composing $\exp_p^{-1}$ with a choice of orthonormal frame at $p$. They satisfy $g_{ij}(p) = \delta_{ij}$ and $\partial_k g_{ij}(p) = 0$ (equivalently $\Gamma^k_{ij}(p) = 0$). These are the "Riemannian Taylor coordinates" — the metric is Euclidean at $p$ and the first deviation is order $r^2$, controlled by curvature. **Geodesic polar coordinates** are the polar version, $(r, \omega)$ on $T_pM \setminus 0$ pushed forward.

- **[[Thm - The Gauss Lemma]]**
	- Radial geodesics through $p$ are orthogonal to the **geodesic spheres** $\exp_p(\{v : |v| = r\})$. Equivalently, $d(\exp_p)_v$ preserves orthogonality between the radial direction $v$ and its orthogonal complement in $T_pM$. The lemma is the statement that geodesics are the *shortest* path locally — once you know radial = orthogonal to spheres, a length computation in polar coordinates gives the local minimisation property.

- **[[Def - Geodesic Completeness]]**
	- $(M, g)$ is **geodesically complete** if every maximal geodesic is defined for all $t \in \mathbb{R}$ — equivalently, $\exp_p$ is defined on all of $T_pM$ for some (equivalently every) $p$. The open unit ball $B^n \subset \mathbb{R}^n$ with the Euclidean metric is *not* complete (geodesics run off the boundary); the same set with the hyperbolic Poincaré metric *is* complete. Completeness is the geometric content the next theorem turns into other properties.

- **[[Thm - Hopf-Rinow Theorem (Statement)]]**
	- For a connected Riemannian manifold $(M, g)$, the following are equivalent: (a) $(M, g)$ is geodesically complete; (b) $(M, d_g)$ is complete as a metric space; (c) every closed bounded set is compact. Furthermore, under any of these, every pair of points is joined by a length-minimising geodesic. The theorem is the bridge between the analytic (ODE-completeness), metric, and topological (Heine–Borel) facets of "completeness".

- **[[Ex - The Exponential Map on a Sphere is a Local Diffeomorphism]]** (⭐⭐)
	- Compute $\exp_p$ on $S^2$ explicitly: it wraps a ray $tv$ into the great circle of length $t$. Show it is a diffeomorphism on the open ball of radius $\pi$ in $T_pS^2$ and fails at the antipode (where it crushes the whole sphere of radius $\pi$ to a point). This is the cleanest concrete illustration of "exp is a local diffeo near $0$ but not globally injective".

> [!tip] Unlocked: CAT(k) Spaces *(from Metric Geometry)*
> The Gauss lemma's local-minimisation conclusion generalises massively: a **CAT(k) space** is a geodesic metric space in which triangles are at least as thin as in the model space of constant curvature $k$ (the sphere, the plane, or the hyperbolic plane). The exponential map and Gauss lemma are the synthetic origin of these comparison conditions, and CAT(k) geometry is the natural setting for non-smooth comparison geometry — singular spaces, buildings, asymptotic cones, the moduli space of trees.

> [!note] Exercise Index — §2.2
> [[Exercise Index - §2.2 The Exponential Map and Normal Coordinates]]

## §2.3 Variational Principles and Jacobi Fields

- **[[Def - Length and Energy Functionals]]**
	- The **length** $L(\gamma) = \int_a^b |\dot\gamma|\, dt$ is reparametrisation-invariant; the **energy** $E(\gamma) = \tfrac{1}{2}\int_a^b g(\dot\gamma, \dot\gamma)\, dt$ is not, but is differentiable at constant-speed curves and easier to vary. Cauchy–Schwarz forces $L(\gamma)^2 \leq 2(b-a)\, E(\gamma)$ with equality exactly for constant-speed parametrisations, so a curve minimising $E$ among fixed-endpoint curves automatically minimises $L$ and is constant-speed. The energy is the "right" functional for variational arguments; geodesics are its critical points without the reparametrisation ambiguity.

- **[[Thm - First Variation of Arc Length]]**
	- For a smooth variation $\gamma_s$ of a unit-speed curve $\gamma = \gamma_0$ with variation field $V = \partial_s \gamma_s|_{s=0}$, fixing endpoints,
	$$\frac{d}{ds}\bigg|_{s=0} L(\gamma_s) = -\int_a^b g(V, \nabla_T T)\, dt + \bigl[g(V, T)\bigr]_a^b.$$
	With fixed endpoints, criticality is therefore $\nabla_T T = 0$ — exactly the geodesic equation. So **a curve extremises length if and only if it is a geodesic (up to reparametrisation)**.

- **[[Thm - Second Variation of Arc Length]]**
	- For a fixed-endpoint variation $\gamma_s$ of a unit-speed geodesic $\gamma$ with normal variation field $V \perp T$,
	$$\frac{d^2}{ds^2}\bigg|_{s=0} L(\gamma_s) = \int_a^b \bigl(g(V', V') - g(R(V, T)T, V)\bigr)\, dt = I(V, V).$$
	The bilinear form $I$ on normal variations is the **index form**, and its sign determines whether $\gamma$ is a local minimum, saddle, or maximum of length. Positive curvature contributes a *negative* term (geodesics tend to come together — second variation becomes negative beyond conjugate points), and negative curvature contributes a positive term (geodesics minimise globally — Cartan–Hadamard).

- **[[Def - Jacobi Field]]**
	- A **Jacobi field** along a geodesic $\gamma$ is a smooth vector field $J$ along $\gamma$ satisfying the **Jacobi equation** $J'' + R(J, T)T = 0$, where $T = \dot\gamma$ and $J' = \nabla_T J$. Equivalently, $J$ arises as the variation field of $\gamma$ through a one-parameter family of geodesics. Jacobi fields form a $2n$-dimensional vector space, parametrised by $(J(0), J'(0)) \in T_pM \times T_pM$. They are the *kernel of the index form* among normal variations vanishing at the endpoints, and they govern the differential of the exponential map.

- **[[Def - Conjugate Point]]**
	- Two points $p, q$ on a geodesic $\gamma$ are **conjugate along $\gamma$** if there is a nonzero Jacobi field $J$ along $\gamma$ with $J(p) = J(q) = 0$. The conjugate locus controls the failure of $\exp_p$ to be injective: $\exp_p$ is a local diffeomorphism near $v$ exactly when $\exp_p(v)$ is not conjugate to $p$ along $\gamma_v$. On the round sphere $S^n$ of radius $1$, $p$ is conjugate to its antipode along every geodesic (and only there); on a flat or non-positively-curved manifold, there are no conjugate points at all.

- **[[Def - The Index Form]]**
	- For piecewise-smooth normal variation fields $V, W$ along a unit-speed geodesic $\gamma$ vanishing at the endpoints,
	$$I(V, W) := \int_a^b \bigl(g(V', W') - g(R(V, T)T, W)\bigr)\, dt.$$
	$I$ is symmetric, its kernel on the vanishing-at-endpoints [[Def - Subspace|subspace]] is the space of Jacobi fields vanishing at the endpoints (zero exactly when the endpoints are not conjugate), and its **index** ([[Def - Dimension|dimension]] of a maximal subspace on which $I$ is negative-definite) counts the conjugate points strictly inside the geodesic — this is the **Morse index theorem**.

- **[[Thm - Jacobi Equation and Conjugate Points]]**
	- The Jacobi field $J$ along $\gamma_v$ with $J(0) = 0$ and $J'(0) = w$ is precisely $J(t) = d(\exp_p)_{tv}(tw)$. Consequently, $\exp_p$ fails to be a local diffeomorphism at $v$ if and only if there is a nonzero Jacobi field along $\gamma_v$ vanishing at $0$ and at $1$ — i.e. if and only if $\exp_p(v)$ is conjugate to $p$. Positive sectional curvature bounds force conjugate points to appear within bounded distance; the eigenvalues of $R(\cdot, T)T$ on $T^\perp$ are *exactly* the rates of focusing.

- **[[Ex - Jacobi Fields on a Sphere are Sinusoidal]]** (⭐⭐)
	- On the unit sphere $S^n$, show that for a unit-speed geodesic the Jacobi equation along $T^\perp$ reduces to $f'' + f = 0$, so normal Jacobi fields are linear combinations of $\sin t$ and $\cos t$. Derives directly the existence of conjugate points at $t = \pi$ — the antipode.

- **[[Ex - Conjugate Points on the Round Sphere are Antipodal]]** (⭐⭐)
	- Using the sinusoidal Jacobi fields above, prove that the conjugate points of $p \in S^n$ along any geodesic are exactly the antipode $-p$ (with multiplicity $n - 1$) and its periodic images. Compare to the [[Ex - The Exponential Map on a Sphere is a Local Diffeomorphism|failure of $\exp_p$ at radius $\pi$]].

- **[[Ex - Computing the Index Form for a Pole-to-Pole Geodesic on S^2]]** (⭐⭐⭐)
	- For a pole-to-pole great-circle arc on $S^2$ (parameter $0 \leq t \leq \pi$), evaluate $I(V, V)$ on test variations $V(t) = f(t)\, e_\perp(t)$ with $f(0) = f(\pi) = 0$. Show by an integration by parts and the curvature identity $K = 1$ that $I(V, V) = \int_0^\pi (f'^2 - f^2)\, dt$, and that this is *zero* on the Jacobi-field test function $f(t) = \sin t$ — exhibiting both the loss of length-minimisation and the conjugate-point obstruction concretely.

> [!tip] Unlocked: Comparison Geometry *(from Riemannian Geometry)*
> Once you have Jacobi fields and the index form, **Rauch's comparison theorem** is two pages away: it bounds the "size" of a Jacobi field on $M$ in terms of its behaviour on a model space of constant sectional curvature. From Rauch flow the Toponogov triangle theorem, the Bonnet–Myers diameter bound, the Cartan–Hadamard theorem, and the entire industry of curvature-to-topology results in **comparison geometry** — the chapter that follows in [[Riemannian Geometry III — Riemann Curvature and Topology]] is the start of that program.

> [!tip] Unlocked: Mountain-Pass and Minimax Theorems *(from Variational Calculus / PDE)*
> The index form is the Hessian of the length functional at a geodesic, and it generalises wholesale to other variational problems (harmonic maps, minimal surfaces, Yang–Mills). When the Hessian has nontrivial negative index, the critical point is a saddle, and **mountain-pass / minimax theorems** (Ljusternik–Schnirelmann, Palais–Smale) use the index to count critical points of higher Morse index. This is the geometric origin of the Morse theory eventually used to prove the existence of closed geodesics on any closed Riemannian manifold.

> [!note] Exercise Index — §2.3
> [[Exercise Index - §2.3 Variational Principles and Jacobi Fields]]

## §2.4 Hamilton's Principle in Mechanics

- **[[Def - Hamiltonian Flow of the Kinetic Energy]]**
	- The **kinetic-energy Hamiltonian** on $T^*M$ is $H(q, p) = \tfrac{1}{2}g^{ij}(q)\, p_i\, p_j$. The associated Hamiltonian vector field $X_H$, defined by $\iota_{X_H}\omega = dH$ with $\omega = dq^i \wedge dp_i$, generates **geodesic flow**: projecting an integral curve of $X_H$ to $M$ gives a geodesic of $g$ parametrised by arc length. This is the cleanest possible formulation — the entire geodesic equation is contained in the one Hamiltonian $\tfrac{1}{2}|p|^2_{g^{-1}}$.

- **[[Thm - Hamilton's Principle Gives the Geodesic Equation]]**
	- For curves $q : [a, b] \to M$ with fixed endpoints, the critical points of the action $\int_a^b L\, dt$ for the Lagrangian $L(q, \dot q) = \tfrac{1}{2}g_{ij}(q)\, \dot q^i \dot q^j$ are precisely the geodesics. Equivalently, the Euler–Lagrange equations $\frac{d}{dt}\frac{\partial L}{\partial \dot q^i} = \frac{\partial L}{\partial q^i}$ reduce to $\ddot q^k + \Gamma^k_{ij}\dot q^i \dot q^j = 0$. The Legendre transform $p_i = \partial L / \partial \dot q^i = g_{ij}\dot q^j$ converts this to the Hamiltonian system on $T^*M$ with $H = \tfrac{1}{2}g^{ij}p_i p_j$.

- **[[Ex - Pendulum as a Geodesic in a Conformally Modified Metric (Jacobi)]]** (⭐⭐⭐)
	- For a particle of unit mass on a configuration manifold $(M, g)$ moving in a potential $V(q)$ with total energy $E$, show by Jacobi's principle of least action that its trajectory is a geodesic of the **Jacobi metric** $\tilde g = 2(E - V(q))\, g$ on the region $\{V < E\}$. Apply to the simple pendulum: the configuration space is $S^1$, the energy is $E = \tfrac{1}{2}\dot\theta^2 + (1 - \cos\theta)$, and the Jacobi metric is $\tilde g = 2(E - 1 + \cos\theta)\, d\theta^2$ — periodic motions correspond to closed geodesics of $\tilde g$.

> [!tip] Unlocked: Ricci Flow as a Geometric Heat Equation *(from Riemannian Geometry)*
> The geodesic equation is the "free particle" on $M$, the simplest non-trivial Hamiltonian flow. **Ricci flow** $\partial_t g_{ij} = -2 R_{ij}$ is what you get when you let the *metric itself* evolve by a Hamiltonian-like dissipative dynamics — the Lagrangian is now the integral of scalar curvature (Hilbert's action), and Ricci flow is its gradient flow up to a diffeomorphism term. The whole circle of ideas in this chapter is what makes Perelman's resolution of the Poincaré conjecture sit in the language it sits in.

> [!note] Exercise Index — §2.4
> [[Exercise Index - §2.4 Hamilton's Principle in Mechanics]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The exercises of this chapter fall into a small number of recurring patterns. The first is **identification of geodesics**: given an explicit metric (the sphere, hyperbolic space, a surface of revolution, the Schwarzschild metric), find the geodesics — either by solving the ODE directly or by using a symmetry (Killing vector, conservation law) to integrate it. The second is **computing the exponential map and its differential**, and from this **deciding whether the exponential is a local diffeomorphism on a region of $T_pM$**. The third is **deciding whether a curve is length-minimising** between two given points — typically by checking conjugate points and using the second variation. The fourth is **finding the Jacobi fields along a given geodesic**, which on a homogeneous space (sphere, hyperbolic space) reduces to a constant-coefficient ODE. The fifth is **converting a mechanical problem to a geodesic problem via Jacobi's principle**, or conversely **reading off the dynamics of a Lagrangian/Hamiltonian system from the geometry of the configuration manifold**. These five targets — identify geodesics, compute $\exp$, decide minimisation, find Jacobi fields, convert mechanics ↔ geometry — recur because each is a way of pinning down the local geometry: once you know the geodesics and the Jacobi fields, you know the local exponential map and the second variation, and curvature is determined by Jacobi field behaviour.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **An explicit metric on a familiar manifold** (sphere, hyperbolic space, surface of revolution, warped product) routes through coordinate computation of Christoffel symbols and integration of the geodesic ODE. **A symmetry of the metric** — most usefully a Killing vector field — gives a conserved quantity $g(\dot\gamma, X)$ along geodesics, often enough to reduce the geodesic ODE to quadrature. **A point and a tangent vector**, by [[Thm - Existence and Uniqueness of Geodesics|existence and uniqueness]], produces a unique maximal geodesic — exploiting *uniqueness* is the trick behind "isometries send geodesics to geodesics" and behind reflection arguments in symmetric spaces. **A curvature bound** (sectional curvature $\geq K_0$ or $\leq K_0$) controls the Jacobi field equation through Sturm comparison, giving global statements about conjugate points and length-minimisation. **A potential $V$ and an energy level $E$** convert via Jacobi's principle into a Riemannian metric on the configuration space, transferring mechanical questions to geometric ones. The recurring move is to route from one of these sources to one of the targets above: an explicit metric routes through Christoffel symbols and ODE integration to "identify the geodesics"; a Killing vector routes through conservation to "integrate the geodesic ODE"; a curvature bound routes through the index form to "decide minimisation"; an energy level routes through Jacobi's principle to "identify periodic motions as closed geodesics".

---

# Legal Operations

These are the moves almost every exercise in this topic is assembled from. When stuck, scan the list and try each.

**Legal operations:**

1. **Write down the geodesic equation in coordinates.** From the metric components $g_{ij}$ compute $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$ and assemble $\ddot x^k + \Gamma^k_{ij}\dot x^i \dot x^j = 0$. *Trigger:* the metric is given by explicit components in a chart. *Pattern:* compute $g^{ij}$ first, then each $\Gamma^k_{ij}$ that does not vanish by symmetry; the resulting ODE system is often integrable because of zero entries.

2. **Use a Killing vector to produce a conserved quantity.** If $X$ is a [[Def - Vector Field on a Manifold|vector field]] whose flow preserves $g$ (a **Killing field**), then $g(\dot\gamma, X)$ is conserved along every geodesic $\gamma$. *Trigger:* the metric has a continuous symmetry — a rotational, translational, or boost invariance. *Pattern:* identify $X$ by inspection, write down $g(\dot\gamma, X) = \mathrm{const}$, and use it to reduce the system to one fewer ODE. This is how one integrates the geodesic equations on the sphere, on Schwarzschild, on Kerr.

3. **Exploit uniqueness to identify a geodesic.** A curve $\gamma$ is the unique geodesic with $\gamma(0) = p$ and $\dot\gamma(0) = v$. So if you can exhibit *any* curve through $p$ with velocity $v$ at $p$ and zero covariant acceleration, that curve *is* the geodesic. *Trigger:* the candidate is a fixed locus of an [[Def - Isometry|isometry]], an integral curve of a Killing field, or a smooth curve whose covariant acceleration is computable. *Pattern:* "find an isometry $\varphi$ fixing $p$ and $v$; then $\varphi \circ \gamma$ is also a geodesic with the same initial data, so $\varphi \circ \gamma = \gamma$; the only curves fixed by $\varphi$ are $\ldots$ which must therefore be the geodesic". This is how great circles are identified on the sphere.

4. **Compute the exponential map via the geodesic flow.** $\exp_p(v) = \gamma_v(1)$, so if you have explicit geodesics you have $\exp_p$. *Trigger:* you have parametrised the geodesics through $p$ explicitly. *Pattern:* re-parametrise the geodesic by $t \mapsto t\, v / |v|$ in terms of $v \in T_pM$, evaluate at $1$, read off the map. On Lie [[Def - Group|groups]] with bi-invariant metric the Riemannian exponential equals the Lie-group exponential, and this is the shortcut.

5. **Use normal coordinates to kill first-order terms.** In normal coordinates at $p$, $g_{ij}(p) = \delta_{ij}$ and $\partial_k g_{ij}(p) = 0$, so $\Gamma^k_{ij}(p) = 0$. Any calculation involving "the value of a covariant derivative at $p$" becomes the value of an ordinary derivative. *Trigger:* you need a local first-order identity at one point. *Pattern:* "work in normal coordinates at $p$; then $\Gamma^k_{ij}(p) = 0$, so at $p$ ordinary differentiation equals covariant differentiation". Use this to compute curvature components at a point, or to verify tensor identities pointwise.

6. **Apply the first variation formula to a critical curve.** A critical point of length (or energy) with fixed endpoints satisfies $\nabla_{\dot\gamma}\dot\gamma = 0$. *Trigger:* the problem is set up as "show that the critical curves of [some functional] are geodesics" or "deduce that minimisers of length are geodesics". *Pattern:* set up the variation $\gamma_s$, compute $\frac{d}{ds}\big|_0 L$ via integration by parts, read off the Euler–Lagrange equation.

7. **Apply the second variation formula to test minimisation.** A geodesic $\gamma$ is a local length-minimiser only if the index form $I(V, V) \geq 0$ for all normal variations $V$ vanishing at the endpoints. *Trigger:* the question is "is $\gamma$ minimising?" or "what is the maximum length over which $\gamma$ minimises?". *Pattern:* evaluate $I$ on suitable test functions; a single $V$ with $I(V, V) < 0$ proves non-minimisation; vanishing $I(V, V) = 0$ on a non-trivial $V$ signals a conjugate point.

8. **Solve the Jacobi equation along $\gamma$.** Parallel-transport an orthonormal frame along $\gamma$, expand $J(t) = \sum f^i(t) e_i(t)$, and the Jacobi equation becomes the linear ODE system $f''^i + R^i{}_j(t) f^j = 0$ where $R^i{}_j = g(R(e_j, T)T, e_i)$. *Trigger:* you need to compute or characterise Jacobi fields. *Pattern:* parallel transport reduces the equation to an ODE with time-dependent coefficient matrix; in constant-curvature spaces the matrix is constant and solutions are explicitly trigonometric, hyperbolic, or linear.

9. **Convert a Hamiltonian system to a geodesic flow via Jacobi.** Given a Lagrangian $L = T - V$ on a Riemannian configuration manifold $(M, g)$ at fixed energy $E$, replace $g$ by the **Jacobi metric** $\tilde g = 2(E - V(q))\, g$ on $\{V < E\}$. Trajectories become geodesics of $\tilde g$. *Trigger:* a classical mechanics problem at fixed energy. *Pattern:* this is how periodic orbits become closed geodesics, how chaotic dynamics translates into ergodicity of geodesic flow, and how billiards on a flat table become broken geodesics.

10. **Pass between $TM$ and $T^*M$ via the Legendre transform.** The map $\dot q \mapsto p = g_{ij}\dot q^j$ is a diffeomorphism between $TM$ and $T^*M$ (for any Riemannian metric); under it the Lagrangian $L = \tfrac{1}{2}|\dot q|^2$ corresponds to the Hamiltonian $H = \tfrac{1}{2}|p|^2_{g^{-1}} = \tfrac{1}{2}g^{ij}p_i p_j$. *Trigger:* you have a problem on one side of the Legendre transform and want to use a tool natural on the other side. *Pattern:* use $T^*M$ when you want the symplectic geometry (Poisson brackets, action–angle variables, KAM); use $TM$ when you want the variational principle directly.

**Illegal but tempting operations:**

> [!warning] 1. Treating the exponential map as globally a diffeomorphism
> $\exp_p$ is a local diffeomorphism near $0$, but in general not globally. On the round $S^2$, $\exp_p$ is a diffeomorphism on the open ball of radius $\pi$ in $T_p S^2$ but collapses the entire boundary sphere of radius $\pi$ to the single antipodal point. The local diffeomorphism property fails exactly at *conjugate points*: $\exp_p$ is a local diffeo at $v$ iff $\gamma_v(1)$ is not conjugate to $p$ along $\gamma_v$. The repair is to work either inside the **injectivity radius** $\mathrm{inj}(p) = \sup\{r : \exp_p|_{B(0,r)}\text{ is a diffeomorphism}\}$, or to use [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]] (existence of minimising geodesics) without claiming uniqueness.

> [!warning] 2. Inferring "no conjugate points $\implies$ length-minimising"
> Lack of conjugate points along $\gamma$ ensures $\gamma$ is a *local* minimum of length, but not a global one. The standard counterexample is the flat cylinder $S^1 \times \mathbb{R}$: a geodesic that winds around the cylinder several times never has conjugate points (the metric is locally flat) but is not length-minimising — a shorter geodesic exists between the same endpoints. The repair: global minimisation requires both no conjugate points and "the geodesic is the shortest among all curves in its [[Def - Homotopy|homotopy]] class", which is a global topological condition.

> [!warning] 3. Confusing $\nabla_{\dot\gamma}\dot\gamma = 0$ with $\ddot\gamma = 0$
> "Constant velocity" in $\mathbb{R}^n$ means $\ddot\gamma = 0$, the ordinary second derivative. On a manifold $\ddot\gamma$ alone is not even well-defined — it would live in some ambient space — and the right notion is $\nabla_{\dot\gamma}\dot\gamma = 0$, the *covariant* acceleration. In coordinates the difference is the Christoffel-symbol correction $\Gamma^k_{ij}\dot\gamma^i \dot\gamma^j$, which is genuinely necessary. The repair: in normal coordinates at a single point, $\Gamma^k_{ij}(p) = 0$ and the two notions coincide *at that point*, which is why normal coordinates are useful for pointwise verifications.

> [!warning] 4. Varying $L$ instead of $E$ in the second variation
> The length $L(\gamma) = \int |\dot\gamma|\, dt$ is reparametrisation-invariant, so its Hessian has a degenerate direction (reparametrisation of $\gamma$). Computing the second variation of $L$ naively produces a singular form. The repair: use the energy $E(\gamma) = \tfrac{1}{2}\int |\dot\gamma|^2\, dt$ at *constant-speed parametrisations*; the energy's second variation gives the clean index form $I$. The Cauchy–Schwarz relation $L^2 \leq 2(b-a)E$ then transfers minimisation results between the two.

> [!warning] 5. Identifying the Lie exponential and the Riemannian exponential on a general Lie group
> On a Lie group $G$ with *bi-invariant* metric, the Riemannian and Lie exponentials at the identity agree, and the geodesics through $e$ are one-parameter [[Def - Subgroup|subgroups]]. But on a Lie group with only a left-invariant metric (e.g. left-invariant metrics on $SL(2,\mathbb{R})$), the geodesics are *not* one-parameter subgroups, and the two exponentials disagree. The repair: bi-invariance is the precise condition — a Lie group admits a bi-invariant metric iff it is the product of an abelian group and a compact group.

---

# Problem-Solving Strategy

The problems in this topic are almost all of one of the five types named in Sources and Targets above, and recognising which type — fast — is most of the battle.

If the problem **gives an explicit metric and asks for the geodesics**, the routine is mechanical: compute $g^{ij}$, compute the Christoffel symbols, write down $\ddot x^k + \Gamma^k_{ij}\dot x^i \dot x^j = 0$, and then look for *symmetries* to integrate. A continuous symmetry of $g$ (a Killing vector field $X$) gives the conserved quantity $g(\dot\gamma, X)$, which is one of the first-order conservation laws Noether's theorem produces from the Hamiltonian formulation. With enough symmetries the second-order system reduces to quadrature: on the sphere, rotational symmetry plus energy conservation gives two conservation laws and integrates the geodesic equation completely; on Schwarzschild, time translation plus rotational invariance give two, plus the trivial energy conservation gives three, enough to reduce the four-dimensional spatial geodesic equation to a one-variable problem.

The cheap *uniqueness* trick is worth its own paragraph. The geodesic with $\gamma(0) = p$ and $\dot\gamma(0) = v$ is unique. So if there is an isometry $\varphi$ fixing $p$ and $v$, then $\varphi(\gamma(t))$ is also a geodesic with the same initial conditions, hence equals $\gamma(t)$. This means $\gamma$ lies in the fixed set of $\varphi$. On the round sphere $S^2$, the reflection across the plane through $p$ and $v$ is an isometry fixing $p$ and $v$; the fixed set is the great circle through $p$ tangent to $v$; uniqueness forces the geodesic to be that great circle, no ODE solving required. The hyperbolic plane, Schwarzschild, surfaces of revolution — most of the cases people actually compute — yield to this trick.

If the problem **asks whether a geodesic is length-minimising**, the routine is to look for conjugate points. The geodesic minimises strictly up to the first conjugate point, fails to minimise locally past it. To find conjugate points solve the Jacobi equation. On a space of *constant* sectional curvature $K$, the Jacobi equation along $T^\perp$ becomes the constant-coefficient ODE $f'' + Kf = 0$, whose solutions are sinusoidal (sphere), linear (flat), or hyperbolic (hyperbolic space); the first conjugate point is at $t = \pi/\sqrt K$, infinity, or infinity respectively. This recovers all the basic comparison statements (Bonnet–Myers bound, Cartan–Hadamard) by direct ODE comparison.

If the problem **comes from mechanics** — a Lagrangian or Hamiltonian system — the routine is Jacobi's principle: fix the total energy $E$, replace the metric $g$ on the configuration space by the **Jacobi metric** $\tilde g = 2(E - V(q))\, g$ on the classically-allowed region $\{V < E\}$, and now the trajectories are geodesics of $\tilde g$. Periodic motions correspond to closed geodesics, and ergodicity of the dynamics translates into ergodicity of the geodesic flow. The Schwarzschild light-bending calculation, the deduction of Kepler orbits as conic sections, and the small-amplitude pendulum's harmonic period all fall out of this conversion.

If the problem **asks for the differential of the exponential**, the routine is Jacobi fields: $d(\exp_p)_{tv}(tw) = J(t)$, where $J$ is the Jacobi field along $\gamma_v$ with $J(0) = 0$ and $J'(0) = w$. So the linearisation of $\exp_p$ at any point is computed by solving the Jacobi ODE with appropriate initial data — and the singular locus of $\exp_p$ is exactly the conjugate locus. This is the only way to compute $d\exp_p$ in any concrete case where you cannot read it off by symmetry.

A meta-strategy threads all of this together: **the local geometry of a Riemannian manifold is encoded in three layers — the metric $g$, the geodesics $\gamma_v$, and the Jacobi fields $J$ — and each layer differentiates the previous**. The metric is zeroth-order data; geodesics are the first-order dynamical content (one integration of the connection); Jacobi fields are the second-order content (one further linearisation), and the eigenvalues of the curvature operator on $T^\perp$ are exactly the *coefficients* of the Jacobi equation. So every question about local Riemannian geometry can be re-asked at the level of geodesics or Jacobi fields, and conversion between layers is the standard pattern of proof.

---

# Most Reusable Properties

- **[[Thm - Existence and Uniqueness of Geodesics|Existence and uniqueness of geodesics]]** — Given $(p, v) \in TM$, there is a unique maximal geodesic $\gamma_v$ with these initial conditions. This is the workhorse: it underlies the *definition* of the exponential map (which sends $v$ to $\gamma_v(1)$), the geodesic flow on $TM$, the global characterisation of completeness, and the uniqueness arguments that identify geodesics through symmetry. Reach for it whenever you have a candidate geodesic and want to argue it is *the* geodesic, and whenever you need to know that the dynamical system on $TM$ generated by the geodesic vector field is well-posed.

- **[[Thm - The Gauss Lemma|The Gauss Lemma]]** — Radial geodesics through $p$ are orthogonal to geodesic spheres. The reusable content is that in geodesic polar coordinates the metric has the form $dr^2 + h(r, \omega)$ — no cross term between $dr$ and $d\omega$ — so the radial direction is *metrically* orthogonal to the spherical directions, not just transversal. This is what makes radial geodesics locally length-minimising and what makes the Riemannian distance function smooth inside the injectivity radius. Reach for it whenever you need to estimate distances near a point.

- **[[Thm - First Variation of Arc Length|First Variation]]** — A curve extremises length (with fixed endpoints) iff it is a geodesic. This is the variational *characterisation* of geodesics, and it is the bridge between the ODE definition and Hamilton's principle. The reusable use is to *recognise* a geodesic problem in a context where no metric is overtly named: any "find the shortest path" or "find the critical points of $\int \cdots$" problem on a manifold with a quadratic-in-velocities integrand routes through the first variation.

- **[[Thm - Jacobi Equation and Conjugate Points|Jacobi field equation $J'' + R(J, T)T = 0$]]** — A second-order linear ODE for vector fields along $\gamma$, with the curvature tensor as coefficient. The reusable use is that it converts *curvature bounds* into *bounds on conjugate-point distance*: positive sectional curvature $K \geq K_0 > 0$ forces conjugate points within distance $\pi/\sqrt{K_0}$ (Bonnet–Myers diameter bound), and non-positive sectional curvature implies no conjugate points (Cartan–Hadamard). Reach for it whenever a curvature hypothesis appears alongside a question about geodesics' global behaviour.

- **[[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]]** — On a connected Riemannian manifold, geodesic completeness ⟺ metric completeness ⟺ every closed bounded set is compact, and any of these implies every pair of points is joined by a minimising geodesic. Reach for it whenever you need the *existence* of a minimising geodesic — the theorem makes this completely free on any complete manifold. Compactness implies completeness, so on compact manifolds minimising geodesics always exist; this is why all examples in introductory treatments work.

---

# Bridges

1. **General relativity** — A Lorentzian spacetime is a [[Def - Lorentzian Manifold|manifold]] $(M, g)$ with a non-degenerate metric of signature $(-, +, +, +)$. The Levi-Civita connection of $g$ exists and is unique (the [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|fundamental theorem]] holds in any signature), and a **geodesic** of $g$ is again $\nabla_{\dot\gamma}\dot\gamma = 0$. Timelike geodesics are the worldlines of free-falling massive particles; null geodesics are the worldlines of light. Einstein's equations $R_{\mu\nu} - \tfrac12 R\, g_{\mu\nu} = 8\pi T_{\mu\nu}$ determine the metric from the matter content, and then *every* free-fall trajectory in the resulting spacetime is a geodesic of this metric. So the geodesic-equation machinery of this chapter is the entire kinematic content of GR; [[General Relativity I — Einstein's Equations and Schwarzschild]] develops this, and the Schwarzschild geodesic equations are the classical tests (perihelion precession of Mercury, gravitational light bending) of the theory.

2. **Hamiltonian mechanics on $T^*M$** — The geodesic flow is the Hamiltonian flow of $H = \tfrac{1}{2}g^{ij}p_i p_j$ on $T^*M$ with its canonical symplectic structure $\omega = dq^i \wedge dp_i$. This is the simplest non-trivial Hamiltonian system: free motion on a Riemannian manifold. Every conservative mechanical system $L = T - V$ on a configuration manifold $M$ becomes, after Legendre transform, a Hamiltonian on $T^*M$ with $H = T + V$; and via Jacobi's principle, the trajectories at fixed energy $E$ are geodesics of the conformally rescaled Jacobi metric $\tilde g = 2(E - V)\, g$ — i.e. the *same* kind of geodesic flow, but with a different metric. The full symplectic machinery (Poisson brackets, action–angle variables, KAM theory, integrability) developed in [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]] specialises to give powerful global structure theorems for geodesic flow.

3. **The fundamental group and the Bonnet–Myers diameter bound** — When the Ricci curvature of $(M, g)$ is bounded below by a positive constant, the second variation formula and Jacobi field analysis force every geodesic of length $\geq \pi/\sqrt{(n-1)K_0/n}$ to have a conjugate point — so no such geodesic can minimise. By [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]] this means $M$ has bounded diameter, hence is compact. Combined with the lifting of geodesics to the universal cover and applying the diameter bound there, we get **Myers' theorem**: a complete Riemannian manifold with positive Ricci curvature has finite fundamental group $\pi_1(M)$. This is one of the cleanest curvature-to-topology theorems and is developed fully in [[Riemannian Geometry III — Riemann Curvature and Topology]] and [[Algebraic Topology II — Fundamental Group and Covering Spaces]] — the bridge is variational, through Jacobi fields and the index form.

4. **Existence and uniqueness via the contraction mapping principle** — The geodesic ODE $\ddot x^k + \Gamma^k_{ij}\dot x^i \dot x^j = 0$ is a second-order autonomous ODE with smooth coefficients (if $g$ is smooth) — but more importantly, lifted to $TM$ via the substitution $(x, v) \mapsto (v, -\Gamma^k_{ij}(x)v^i v^j)$, it becomes a first-order ODE on the tangent bundle: the **geodesic vector field**. Picard–Lindelöf (i.e., the [[Thm - The Contraction Mapping Principle|contraction mapping principle]] applied to the Volterra integral form) gives short-time existence and uniqueness for any smooth initial condition. This is the abstract reason every Riemannian manifold has lots of geodesics — it is just ODE theory applied carefully. The same machinery, lifted to *parallel transport* (a linear ODE on $TM$), gives the Levi-Civita connection's parallel transport map as discussed in [[Riemannian Geometry I — Connections and Covariant Differentiation]].

5. **The inverse function theorem and normal coordinates** — The differential of $\exp_p$ at $0 \in T_pM$ is the identity map on $T_pM$ — this is immediate from the homogeneity $\gamma_{tv}(s) = \gamma_v(st)$ of the geodesic ODE. By the [[Thm - The Inverse Function Theorem|inverse function theorem]] $\exp_p$ is a local diffeomorphism onto a neighbourhood of $p$. Composing the inverse with a choice of orthonormal basis at $T_pM$ produces normal coordinates: a chart in which $g_{ij}(p) = \delta_{ij}$ and $\Gamma^k_{ij}(p) = 0$. The construction is one application of the inverse function theorem and is the source of every pointwise computation in Riemannian geometry — the equivalence principle in general relativity is literally the physicist's statement of the existence of normal coordinates.

---

# Insights

**The unifying frame: a Riemannian manifold is studied by its geodesics, its exponential map, and its Jacobi fields — three layers of the same calculus**. The metric $g$ is a piece of static data: an inner product on each tangent space, varying smoothly. The geodesics are the *integrated* content: paths on $M$ that locally minimise length. The exponential map packages all the geodesics through one point into a single smooth map $\exp_p : T_pM \to M$, and the Jacobi fields measure how the exponential map differentiates — they are the variations of $\gamma_v$ along nearby geodesics. The remarkable thing is that the eigenvalues of the curvature operator $R(\cdot, T)T$ on $T^\perp$ — a purely algebraic object built from the metric — are exactly the *coefficients* of the Jacobi equation, so curvature bounds translate immediately into ODE comparison statements and from there into global geometric and topological conclusions (Bonnet–Myers, Cartan–Hadamard, Synge). The story of this topic is the unfolding of this dictionary: data → integrated paths → variations → curvature → topology.

**The true name of "geodesic" is "constant-velocity curve"**, not "shortest path". The shortest-path definition is what most students meet first, but it has two defects: it requires endpoints and a global hypothesis (lengths defined and compared), and it does not say *what* the geodesic is, only that it minimises. The covariant-acceleration definition $\nabla_{\dot\gamma}\dot\gamma = 0$ is a local ODE, requires no boundary conditions, and gives a unique geodesic for every initial $(p, v)$ via ODE theory. The connection between them is the first variation formula: critical points of length are exactly constant-velocity geodesics. So the operational definition is the dynamical one, and "shortest path" is a *theorem* (with the additional hypothesis of "shorter than nearby paths"), not the definition.

**Conjugate points are the place where the local geodesic story fails**. Within the injectivity radius, $\exp_p$ is a diffeomorphism, normal coordinates work, geodesics minimise. The *boundary* of the region where this all works is the conjugate locus, and beyond it everything is more subtle: $\exp_p$ may not be injective (multiple geodesics between the same points), local minimisation fails (the second variation can be made negative), and the metric distance function $d_g(p, \cdot)$ stops being smooth. So conjugate points are not a curiosity — they are the place the entire local Riemannian theory hands off to the global theory. Variations vanishing at conjugate points (i.e., Jacobi fields between conjugate points) are the precise mathematical object that signals the transition, and the **Morse index theorem** (the index of $I$ equals the number of conjugate points strictly inside the geodesic) makes the count exact.

**A trigger-reaction pattern: see "geodesic" → think "ODE on $TM$"**. Whenever a problem mentions geodesics, your first move is to lift to the tangent bundle and view the geodesic equation as a first-order ODE on $TM$: the **geodesic vector field**. From there, "existence and uniqueness" is Picard–Lindelöf, "completeness" is "the vector field is complete" (its flow is defined for all time), the "geodesic flow" $\phi_t : TM \to TM$ is the time-$t$ flow of this vector field, and the **exponential map** is $\exp_p(v) = \pi(\phi_1(v))$, where $\pi : TM \to M$ is the projection. Every theorem about geodesics is, under this conversion, a theorem about a dynamical system on $TM$ — and this is the viewpoint that makes geodesic flow the simplest non-trivial example in dynamical systems, the natural target of KAM theory, ergodic theory, and the theory of hyperbolic systems.

**A trigger-reaction pattern: see "mechanical system with potential $V$ at fixed energy $E$" → convert to a geodesic problem via Jacobi's principle**. The Jacobi metric $\tilde g = 2(E - V(q))\, g$ on the classically-allowed region converts trajectories into geodesics — periodic orbits become closed geodesics, the question of integrability becomes the question of integrability of the geodesic flow, and the Bonnet–Myers bound applied to $\tilde g$ produces global statements about classical mechanical systems. The pendulum example in [[Ex - Pendulum as a Geodesic in a Conformally Modified Metric (Jacobi)]] is the simplest concrete case; for the Kepler problem the Jacobi metric on $\mathbb{R}^3 \setminus \{0\}$ has a remarkable extra symmetry (Runge–Lenz vector), and the integrability of Kepler is a special property of *that* metric.

**The exponential map is the bridge between the linear and the curved**. A tangent space $T_pM$ is a linear object — a vector space — on which all the apparatus of linear algebra works. A manifold $M$ is curved and intrinsically non-linear. The exponential map $\exp_p : T_pM \to M$ converts linear questions at $T_pM$ into curved questions on $M$: e.g., "what does the metric $g$ pulled back to $T_pM$ via $\exp_p$ look like?" — answer, in normal coordinates, $g_{ij}(0) = \delta_{ij}$, $\partial_k g_{ij}(0) = 0$, and the $r^2$ Taylor coefficient is the curvature tensor. So the exponential map gives a Taylor-series-like expansion of the curved metric around any point, with curvature appearing as the leading non-trivial correction. This is the technical heart of "the equivalence principle": you can locally set up coordinates in which gravity (a non-trivial connection) disappears at one point.
