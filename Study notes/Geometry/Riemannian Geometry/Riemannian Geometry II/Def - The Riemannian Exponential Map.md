---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Geodesic"
  - "Thm - Existence and Uniqueness of Geodesics"
  - "Def - The Tangent Bundle"
tags: [geometry, riemannian-geometry, exponential-map]
---

# Notation

$(M, g)$ is a smooth Riemannian (or semi-Riemannian) manifold, $p \in M$ a point, and $T_pM$ the tangent space at $p$ identified canonically with $T_0(T_pM)$ (the tangent space to the vector space $T_pM$ at the origin). For $v \in T_pM$, $\gamma_v$ denotes the unique maximal [[Def - Geodesic|geodesic]] with $\gamma_v(0) = p$ and $\dot\gamma_v(0) = v$; its domain is some maximal open interval $I_v \ni 0$. The shorthand $|v| := \sqrt{g_p(v,v)}$ is the Riemannian norm of $v$. The full notation registry is on [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

---

# Axiom Motivation

The motivating question is **how do we put a coordinate system on a Riemannian manifold that is adapted to the metric, in the same sense that Cartesian coordinates on $\mathbb{R}^n$ are adapted to the Euclidean metric?** Arbitrary charts are arbitrary: the metric components $g_{ij}$ in some random chart look complicated, and statements like "the metric is approximately Euclidean near $p$" make no sense in that chart unless we know what "approximately" refers to.

The natural strategy is: from each point $p$, fire off geodesics in every direction, and use the resulting curves as "radial coordinates". This is the idea Gauss used for surfaces (geodesic polar coordinates) and that Riemann generalised. The data we need is, for each $v \in T_pM$, a curve $\gamma_v$ starting at $p$ with initial velocity $v$. By the [[Thm - Existence and Uniqueness of Geodesics|existence and uniqueness theorem]] we have this curve, on *some* interval around $0$. The exponential map is then defined by $\exp_p(v) := \gamma_v(1)$ — "follow the geodesic in direction $v$ for unit time".

Why "unit time" rather than some other normalisation? The choice is forced by the **homogeneity** of the geodesic equation. Reparametrising the geodesic $\gamma_v$ as $\tilde\gamma(s) = \gamma_v(s/c)$ gives a curve with initial velocity $v/c$; computing $\nabla_{\dot{\tilde\gamma}}\dot{\tilde\gamma}$ shows this is still a geodesic, so $\tilde\gamma = \gamma_{v/c}$. Equivalently, $\gamma_{tv}(s) = \gamma_v(ts)$ — speed and time-of-arrival are interchangeable. So evaluating $\gamma_v$ at time $1$ is the same as evaluating $\gamma_{tv}$ at time $1/t$, which is the same as evaluating the unit-speed geodesic at time $|v|$. The unit-time choice makes $\exp_p$ a function of $v$ alone (not of speed and time separately), and the homogeneity ensures the map respects the linear structure of $T_pM$ to leading order — its derivative at $0$ is the *identity* on $T_pM$.

The reason this matters is that it makes the [[Thm - The Inverse Function Theorem|inverse function theorem]] apply: a smooth map between manifolds whose differential at a point is invertible is a local diffeomorphism there. Since $d(\exp_p)_0 = \mathrm{id}_{T_pM}$, the exponential map is a local diffeomorphism near $0 \in T_pM$ onto some neighbourhood of $p$ in $M$. Composing the *inverse* with a choice of orthonormal basis $(e_1, \ldots, e_n)$ for $T_pM$ then gives a chart on a neighbourhood of $p$ — **normal coordinates** — in which the metric is *Euclidean at the origin*, $g_{ij}(p) = \delta_{ij}$, and *its first-order derivatives also vanish*, $\partial_k g_{ij}(p) = 0$ (equivalently $\Gamma^k_{ij}(p) = 0$). These two cancellations are exactly the cancellations that would happen for a Taylor expansion of the *Euclidean* metric in Cartesian coordinates, so normal coordinates are the Riemannian-geometric analogue of Cartesian coordinates: as Euclidean as possible at one point.

What does the domain $V_p \subseteq T_pM$ of $\exp_p$ look like? It is the set of $v \in T_pM$ for which the geodesic $\gamma_v$ extends to parameter $1$. By the homogeneity, if $v \in V_p$ then so is $tv$ for all $t \in [0, 1]$ — so $V_p$ is **star-shaped** around the origin. The manifold is **geodesically complete** at $p$ iff $V_p = T_pM$; this is one of the equivalent conditions in [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]].

A subtler design choice is whether to define $\exp_p$ from a tangent vector or from a unit tangent vector plus a distance. The unit-vector-plus-distance version $\widetilde{\exp}_p(\omega, r) := \gamma_{\omega/|\omega|}(r)$ has the advantage of writing the geodesic in terms of "direction and travel distance", which feels more geometric. But it is *less smooth*: the dependence on $\omega$ is singular at $\omega = 0$. The tangent-vector version $\exp_p(v) = \gamma_v(1)$ is smooth on all of $V_p$ including the origin, and the two are related by $\exp_p(v) = \widetilde{\exp}_p(v/|v|, |v|)$. Standard practice is to use the tangent-vector version as primary and the polar version only when working in geodesic polar coordinates.

A natural relaxation is to ask **why "exponential" and not just "Riemannian map" or some other name**. The reason is *historical agreement with Lie theory*: on a [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie group]] $G$ with a bi-invariant Riemannian metric, the Riemannian exponential at the identity literally equals the Lie group exponential, $\exp_e(X) = \exp(X)$ for $X \in \mathfrak{g}$, because the geodesics through $e$ are the one-parameter subgroups $t \mapsto \exp(tX)$. So the name "exponential map" is justified by this coincidence in the most symmetric setting — and it transfers to the general case as a piece of suggestive notation. The name should not, however, be taken to suggest any kind of *exponentiation* of vectors; the map is genuinely geometric.

---

# The Definition

Let $(M, g)$ be a Riemannian (or semi-Riemannian) manifold and $p \in M$. The **exponential map at $p$** is the smooth map
$$\exp_p : V_p \to M, \qquad \exp_p(v) := \gamma_v(1),$$
where $V_p \subseteq T_pM$ is the (open, star-shaped) set of tangent vectors $v$ at $p$ for which the maximal geodesic $\gamma_v$ with $\gamma_v(0) = p, \dot\gamma_v(0) = v$ is defined at least on the interval $[0, 1]$.

**Homogeneity.** For any $v \in T_pM$ and $t \in \mathbb{R}$ with $tv \in V_p$, $\exp_p(tv) = \gamma_v(t)$. Equivalently, the ray $t \mapsto tv$ in $T_pM$ is sent to the geodesic $\gamma_v$ in $M$.

**Differential at the origin.** Identifying $T_0(T_pM) = T_pM$ in the canonical way, $d(\exp_p)_0 : T_pM \to T_pM$ is the identity map.

By the [[Thm - The Inverse Function Theorem|inverse function theorem]], $\exp_p$ is therefore a local diffeomorphism from some open neighbourhood of $0 \in T_pM$ onto an open neighbourhood of $p$ in $M$. The supremum of $r > 0$ such that $\exp_p|_{B_g(0, r)}$ is a diffeomorphism onto its image is called the **injectivity radius** at $p$, denoted $\mathrm{inj}_g(p)$.

---

# Categorical / Structural Definition

The exponential map is most naturally thought of as one piece of a single object: the **geodesic flow** $\phi : I \subseteq TM \times \mathbb{R} \to TM$, which is the flow of the geodesic vector field $G$ on the tangent bundle. The geodesic vector field $G$ is determined by $g$ alone (it generates the geodesics in the manner described in [[Def - Geodesic]]), and its flow exists by ODE theory on the open subset $I = \{(v, t) : \gamma_v\text{ exists at parameter }t\}$ of $TM \times \mathbb{R}$.

The exponential map at $p$ is then the composition
$$T_pM \supseteq V_p \hookrightarrow TM \xrightarrow{\phi_1} TM \xrightarrow{\pi} M,$$
where $\phi_1$ is the time-$1$ flow map and $\pi$ is the bundle projection. So the data of "exp at every point simultaneously" is the data of the time-$1$ geodesic flow followed by projection — a single map $\mathrm{Exp} : V \subseteq TM \to M$, $\mathrm{Exp}(v) = \pi(\phi_1(v))$, of which each $\exp_p$ is the restriction to a fibre.

The structural payoff is that *every* property of $\exp_p$ is a property of the geodesic flow: smoothness of $\exp_p$ in $p$ (as well as in $v$) follows from smoothness of $\phi$, equivariance of $\exp_p$ under isometries follows from equivariance of $G$ under isometries, and the Hamiltonian-mechanical interpretation in [[Def - Hamiltonian Flow of the Kinetic Energy]] becomes available because $\phi$ is also (after Legendre transform) the Hamiltonian flow of $H = \tfrac12 |p|^2_{g^{-1}}$ on $T^*M$.

---

# Relate to Other Fields / Compression

**True name:** **the map that sends a tangent vector to the endpoint of the unit-time geodesic it generates**. This is what you reach for in computations: to compute $\exp_p$, parametrise the geodesics through $p$ and evaluate them at $t = 1$.

**The exponential map identifies $\exp_p$ on a Lie group with bi-invariant metric with the Lie-group exponential.** This is the connection to [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]]: $\exp_e(X) = \exp(X)$ for $X \in \mathfrak{g}$. On a Lie group with only a left-invariant metric the two disagree.

**Approximating the metric on $M$ by the metric on $T_pM$.** Through $\exp_p$, the Riemannian metric $g$ on (a neighbourhood of $p$ in) $M$ pulls back to a Riemannian metric $\exp_p^* g$ on (a neighbourhood of $0$ in) $T_pM$. At the origin, this pulled-back metric equals the Euclidean metric induced by $g_p$ on the vector space $T_pM$, and its first derivatives vanish. The second-order Taylor coefficient — the leading non-trivial term in the deviation from Euclidean — is the **curvature tensor at $p$**. So the exponential map is the device that converts curvature into a concrete coordinate computation: see [[Def - Normal Coordinates and Geodesic Coordinates]].

---

# Examples / Corollaries

**Is an instance: Euclidean space.** On $(\mathbb{R}^n, \delta)$ with $p$ the origin, all geodesics are straight lines $\gamma_v(t) = tv$, so $\exp_0(v) = v$. The exponential map is the identity $T_0\mathbb{R}^n = \mathbb{R}^n \to \mathbb{R}^n$. The injectivity radius is infinite. Normal coordinates here are just Cartesian coordinates.

**Is an instance: the sphere $S^n$.** At $p \in S^n$, $\exp_p$ takes $v \in T_pS^n$ to the point at angular distance $|v|$ from $p$ along the great circle in the direction $v/|v|$. Explicitly: $\exp_p(v) = \cos(|v|) p + \sin(|v|) v/|v|$ for $v \neq 0$ (and $\exp_p(0) = p$), embedding $S^n \subseteq \mathbb{R}^{n+1}$ and identifying $T_pS^n$ with the orthogonal complement of $p$. This is a diffeomorphism from the open ball of radius $\pi$ in $T_pS^n$ onto $S^n \setminus \{-p\}$; the entire boundary sphere of radius $\pi$ is collapsed to the antipodal point. Injectivity radius is $\pi$.

**Is an instance: the hyperbolic plane $\mathbb{H}^2$.** Using the disk model with $p$ the origin, $\exp_0$ takes $v$ to $\tanh(|v|/2) \cdot v/|v|$ (in disk coordinates). It is a diffeomorphism $T_0\mathbb{H}^2 \to \mathbb{H}^2$ — the *open* disk — and injectivity radius is infinite. This illustrates the Cartan–Hadamard theorem: on a complete simply-connected manifold of non-positive sectional curvature, $\exp_p$ is a diffeomorphism $T_pM \to M$ for every $p$.

**Is an instance: a torus $T^n = \mathbb{R}^n / \mathbb{Z}^n$.** Locally flat, so each $\exp_p : T_pT^n \to T^n$ is the quotient map $\mathbb{R}^n \to T^n$ composed with translation. Globally not injective: $\exp_p$ wraps $T_pT^n$ around $T^n$ infinitely many times. Injectivity radius is $1/2$ (the half-period).

**Is an instance: a cylinder $S^1 \times \mathbb{R}$.** Flat, so $\exp_p$ is, in local coordinates, the identity, but globally not injective because of the wrap-around in the $S^1$ direction. Injectivity radius is $\pi$ (half the circumference of the $S^1$ factor).

**Is NOT an instance: the open unit ball $B^n \subset \mathbb{R}^n$ with the Euclidean metric.** This is not geodesically complete, so $\exp_p$ is defined only on a proper subset $V_p \subsetneq T_pB^n$ — geodesics in the radial direction "run off" the boundary in finite time. The domain $V_p$ is the open polytope of $v$'s such that $p + v \in B^n$. This shows the necessity of restricting to $V_p$ in the definition.

**Is NOT an instance: the cone with a vertex.** A flat cone (e.g., the surface $z = \sqrt{x^2 + y^2}$ in $\mathbb{R}^3$) is a manifold away from the apex, and on the smooth part $\exp_p$ is a perfectly good local diffeomorphism. But geodesics through the apex have no well-defined extension — the apex is a *cone singularity*, and the exponential map there does not exist as a smooth map. This illustrates the necessity of smoothness of the metric for the existence theorem to work.

**Corollary (homogeneity of $\exp_p$).** $\exp_p(tv) = \gamma_v(t)$ for all $v \in T_pM$ and $t \in \mathbb{R}$ such that $tv \in V_p$. *Calibration check:* by the reparametrisation invariance of the geodesic equation, $\gamma_{tv}(s) = \gamma_v(ts)$; setting $s = 1$ gives $\exp_p(tv) = \gamma_{tv}(1) = \gamma_v(t)$.

**Corollary ($d(\exp_p)_0 = \mathrm{id}$).** *Calibration check:* compute $d(\exp_p)_0(v) = \frac{d}{dt}\big|_{t=0} \exp_p(tv) = \frac{d}{dt}\big|_{t=0} \gamma_v(t) = \dot\gamma_v(0) = v$.

**Corollary ($\exp_p$ is a local diffeomorphism at $0$).** Immediate from the inverse function theorem, since $d(\exp_p)_0 = \mathrm{id}$ is invertible. The largest radius $r > 0$ for which $\exp_p|_{B_g(0, r)}$ is a diffeomorphism onto its image is the injectivity radius $\mathrm{inj}_g(p)$.

**Corollary (Gauss lemma is hidden here).** Even where $\exp_p$ is a diffeomorphism, the pulled-back metric $\exp_p^* g$ on $T_pM$ is not the Euclidean one. But the [[Thm - The Gauss Lemma|Gauss lemma]] says it agrees with Euclidean *in one direction*: radial lines through $0$ in $T_pM$ are perpendicular (under $\exp_p^* g$) to the geodesic spheres $\{|v| = r\}$, exactly as for Euclidean.

**Calibration check.** If you can verify (a) that on Euclidean space the exponential map at the origin is the identity, (b) that on the sphere the exponential at any point is a diffeomorphism from the open ball of radius $\pi$ onto the complement of the antipodal point, and (c) that $d(\exp_p)_0 = \mathrm{id}$ follows immediately from $\dot\gamma_v(0) = v$ — then you have understood the definition.

---

# Unlocked by This

> [!tip] Normal Coordinates *(from Riemannian Geometry)*
> Composing $\exp_p^{-1}$ with an orthonormal basis on $T_pM$ produces **normal coordinates** at $p$: a chart in which $g_{ij}(p) = \delta_{ij}$ and $\Gamma^k_{ij}(p) = 0$. These are the "Taylor-expanded coordinates" of Riemannian geometry, allowing every pointwise computation to be done as if the manifold were Euclidean at $p$. See [[Def - Normal Coordinates and Geodesic Coordinates]].

> [!tip] The Injectivity Radius *(from Riemannian Geometry)*
> The injectivity radius $\mathrm{inj}_g(p)$ is the largest $r$ such that $\exp_p|_{B(0, r)}$ is a diffeomorphism. The function $p \mapsto \mathrm{inj}_g(p)$ is continuous, and its global infimum $\mathrm{inj}(M)$ is a fundamental invariant — on compact manifolds it is positive, and curvature bounds give Klingenberg-type lower bounds on $\mathrm{inj}(M)$. The injectivity radius governs the scale at which the manifold "looks Euclidean".

> [!tip] **Comparison Geometry** *(from Riemannian Geometry)*
> The exponential map is the device through which *curvature bounds* turn into *geometric statements*. Rauch's comparison theorem says: if $K \leq K_0$ on $M$, then $|d(\exp_p)_v(w)| \geq$ the corresponding norm on the model space of constant curvature $K_0$. From here flow the Toponogov triangle theorem, the Bonnet–Myers diameter bound, Cartan–Hadamard, the volume comparison theorems, and the entire industry of *curvature controls geometry* results. See [[Riemannian Geometry III — Riemann Curvature and Topology]].
