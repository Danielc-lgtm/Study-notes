---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Riemannian Metric"
  - "Thm - Fundamental Theorem of Riemannian Geometry (Statement)"
  - "Def - Vector Field on a Manifold"
tags: [geometry, riemannian-geometry, geodesics]
---

# Notation

$(M, g)$ is a smooth Riemannian (or semi-Riemannian) manifold and $\nabla$ its [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|Levi-Civita connection]]. For a smooth curve $\gamma : I \to M$ on an open interval $I \subseteq \mathbb{R}$, the **velocity** $\dot\gamma(t) \in T_{\gamma(t)}M$ is a vector field *along* $\gamma$; the operator $\nabla_{\dot\gamma}$ takes vector fields along $\gamma$ to vector fields along $\gamma$ (the *induced connection*). In a chart $(x^1, \ldots, x^n)$ we write $\gamma(t) = (\gamma^1(t), \ldots, \gamma^n(t))$ and $\dot\gamma^k = d\gamma^k/dt$, and the Christoffel symbols of $g$ are $\Gamma^k_{ij} = \tfrac12 g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$. See [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]] for the full registry.

---

# Axiom Motivation

The question is: **what should "straight line" mean on a curved manifold?** A straight line in $\mathbb{R}^n$ has two equivalent characterisations, and once we move to a manifold these two split apart, forcing us to pick which one we will keep.

The first characterisation is *kinematic*: a straight line is a curve with zero acceleration, $\ddot\gamma = 0$. In Euclidean space this is unambiguous because $\ddot\gamma(t)$ lives in $\mathbb{R}^n$ — there is a single ambient vector space in which to compare the velocity at time $t$ to the velocity at time $t + h$. On a general manifold this comparison is meaningless: $\dot\gamma(t)$ lives in $T_{\gamma(t)}M$, $\dot\gamma(t+h)$ lives in $T_{\gamma(t+h)}M$, and these are different vector spaces. Without extra data we cannot subtract them, so we cannot form $\ddot\gamma$. *This is exactly the gap the Levi-Civita connection fills*: it gives a canonical way to compare vectors in nearby tangent spaces (parallel transport), and through that, a covariant derivative $\nabla_{\dot\gamma}\dot\gamma$ that *does* live in $T_{\gamma(t)}M$. The kinematic definition becomes: $\gamma$ is a geodesic if $\nabla_{\dot\gamma}\dot\gamma = 0$.

The second characterisation is *variational*: a straight line minimises distance between two points. On a Riemannian manifold this also generalises: define the length of a curve by $L(\gamma) = \int |\dot\gamma|\, dt$, and look for minimisers. The catch is that "minimiser between two points" is a global condition with boundary data, while the kinematic version is a local ODE with initial data. They will turn out to agree (the first variation formula shows critical points of length are constant-speed geodesics, and minimisers locally exist by the existence-and-uniqueness theorem), but as *definitions* they have very different structures.

The convention is to take the kinematic definition as primary, for three reasons. First, **locality**: $\nabla_{\dot\gamma}\dot\gamma = 0$ is a local condition, computable at each $t$ from the metric and the curve; the variational definition compares the curve globally to other curves and requires more setup. Second, **uniqueness from initial data**: by the [[Thm - Existence and Uniqueness of Geodesics|ODE existence theorem]] there is a unique geodesic with given $(p, v) \in TM$ at $t = 0$, exactly the data that determines a straight line in Euclidean space; minimisation between fixed endpoints is a less natural data type. Third, **uniformity across signatures**: the kinematic definition works *verbatim* in Lorentzian signature, where lengths can be zero (null) or imaginary, and "minimising the length" makes much less sense. Geodesics in general relativity are defined by the kinematic equation.

Why **not** simply $\ddot\gamma = 0$ in coordinates? Because that equation is *not coordinate-invariant*. Under a change of coordinate $x^i = x^i(\tilde x)$, the ordinary second derivative $\ddot\gamma^k$ transforms with extra Jacobian terms involving $\partial^2 x^k / \partial \tilde x^i \partial \tilde x^j$; the equation $\ddot\gamma^k = 0$ would hold only in *one* chart. The coordinate version of the covariant equation, $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i \dot\gamma^j = 0$, has precisely the extra term needed to cancel the Jacobian contributions of $\ddot\gamma^k$ under coordinate change. *This is the content of the Christoffel-symbol correction*: it is what is needed to make "zero acceleration" coordinate-invariant. In coordinates centred at a single point such that $\Gamma^k_{ij}(p) = 0$ (normal coordinates), the two equations coincide at $p$, which is one way to see that the correction term is genuinely a coordinate artefact.

A subtler design choice is the **parametrisation**. Metric-compatibility of $\nabla$ immediately gives
$$\frac{d}{dt} g(\dot\gamma, \dot\gamma) = 2 g(\nabla_{\dot\gamma}\dot\gamma, \dot\gamma) = 0,$$
so $|\dot\gamma|$ is constant along a geodesic. This is *not* an extra requirement — it is forced by the definition. So a geodesic comes with a *natural parametrisation* up to affine reparametrisation $t \mapsto at + b$; we cannot reparametrise a geodesic to non-constant speed without breaking the geodesic equation. By contrast, "shortest-path" curves can be parametrised by anything, since length is reparametrisation-invariant. The kinematic definition thus *includes* a parametrisation choice as a non-trivial output — the geodesic is not just an unparametrised curve but an unparametrised curve plus a constant-speed parametrisation.

The relaxation worth flagging: there is a weaker notion of **pre-geodesic**, a curve whose *image* is the image of some geodesic but whose parametrisation may not be constant-speed — equivalent to $\nabla_{\dot\gamma}\dot\gamma$ being parallel to $\dot\gamma$ rather than zero. Pre-geodesics arise naturally in conformal geometry (the geodesic equation is *not* conformally invariant, but pre-geodesic equations are partially so) and in the theory of null geodesics in general relativity (where the "length" is zero so a natural parametrisation requires a separate choice). Standard practice is to use "geodesic" for the parametrised version and add "pre-" only when the parametrisation distinction matters.

---

# The Definition

A **geodesic** on a Riemannian (or semi-Riemannian) manifold $(M, g)$ is a smooth curve $\gamma : I \to M$ on an open interval $I \subseteq \mathbb{R}$ satisfying
$$\nabla_{\dot\gamma}\dot\gamma = 0$$
along the entire curve, where $\nabla$ is the Levi-Civita connection of $g$.

**Coordinate form.** In a chart $(U, x^1, \ldots, x^n)$ with $\gamma(I) \subseteq U$, writing $\gamma(t) = (\gamma^1(t), \ldots, \gamma^n(t))$, the geodesic equation becomes the system of nonlinear ODEs
$$\ddot\gamma^k + \Gamma^k_{ij}(\gamma(t))\, \dot\gamma^i\, \dot\gamma^j = 0, \qquad k = 1, \ldots, n.$$

**Speed is constant.** Metric compatibility of $\nabla$ forces $|\dot\gamma|^2 = g(\dot\gamma, \dot\gamma)$ to be constant along $\gamma$. The geodesic is therefore *automatically* parametrised at constant speed; the parameter $t$ is called an **affine parameter** (unique up to affine rescaling $t \mapsto at + b$).

A **maximal geodesic** is one whose domain $I$ cannot be extended to a larger open interval. The manifold is **geodesically complete** if every maximal geodesic has $I = \mathbb{R}$.

---

# Relate to Other Fields / Compression

**A geodesic is an integral curve of the geodesic vector field on $TM$.** Lift the second-order ODE on $M$ to a first-order ODE on $TM$ by setting $u = (x, v)$ with $v = \dot x$, then the system becomes
$$\frac{d}{dt}(x, v) = (v, -\Gamma^k_{ij}(x) v^i v^j\, \partial_k),$$
which is a smooth vector field $G$ on $TM$, the **geodesic vector field**. A curve $\gamma$ on $M$ is a geodesic iff its tangent lift $t \mapsto (\gamma(t), \dot\gamma(t)) \in TM$ is an integral curve of $G$. This converts every theorem about geodesics into a theorem about the dynamical system on $TM$ generated by $G$. The flow of $G$ is the **geodesic flow** $\phi_t : TM \to TM$, and the [[Def - The Riemannian Exponential Map|exponential map]] is its time-$1$ map composed with projection: $\exp_p(v) = \pi(\phi_1(v))$.

**A geodesic is a self-parallel curve.** Equivalently, $\gamma$ is a geodesic iff $\dot\gamma(t)$ is the parallel transport of $\dot\gamma(0)$ along $\gamma$. This is the most geometric formulation: the velocity stays "the same vector" (modulo parallel transport) all along the curve. It is also the formulation that survives in non-Riemannian connection settings (affine connections, gauge theory) where there is no metric to use.

**True name:** **a curve with zero covariant acceleration**, or equivalently, **a curve whose velocity is its own parallel transport**. The minimisation property — that geodesics locally minimise length — is a *theorem*, not the definition, and it requires extra hypotheses (local enough; no conjugate points; etc.) to be true globally. When you need to compute, identify, or characterise a geodesic, you use the covariant-acceleration form; when you need to understand *why* the geodesic is interesting, you appeal to the variational principle. Both viewpoints are essential, but the covariant-acceleration form is operational.

---

# Examples / Corollaries

**Is an instance: straight lines in $\mathbb{R}^n$.** With the Euclidean metric $g = \delta_{ij}$, all $\Gamma^k_{ij}$ vanish, so the geodesic equation reduces to $\ddot\gamma^k = 0$. Solutions are $\gamma(t) = p + tv$ — the affinely-parametrised straight lines. This recovers the elementary case and shows the geodesic equation is the right generalisation.

**Is an instance: great circles on $S^n$.** On the unit sphere $S^n \subseteq \mathbb{R}^{n+1}$ with the induced metric, the geodesics are precisely the great circles parametrised at constant speed. This is the content of [[Ex - Great Circles are the Geodesics of the Sphere]] and is the simplest non-trivial example. The shortest geodesic between $p$ and a non-antipodal $q$ is the *shorter* of the two great-circle arcs.

**Is an instance: vertical lines and semicircles in the hyperbolic plane.** In the upper half-plane $\mathbb{H}^2 = \{(x, y) : y > 0\}$ with $ds^2 = (dx^2 + dy^2)/y^2$, the geodesics are the vertical lines $x = \mathrm{const}$ and the semicircles whose centres lie on the $x$-axis. See [[Ex - Geodesics of the Hyperbolic Plane]] for the integration.

**Is an instance: one-parameter [[Def - Subgroup|subgroups]] of a Lie [[Def - Group|group]] with bi-invariant metric.** On a Lie group $G$ with a bi-invariant Riemannian metric, the geodesics through the identity are exactly the one-parameter subgroups $t \mapsto \exp(tX)$ for $X \in \mathfrak{g}$. The Riemannian exponential map then coincides with the [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie-group exponential]]. This is the cleanest case where the abstract geodesic ODE has an algebraically simple solution.

**Is an instance: helices on a flat cylinder.** The cylinder $S^1 \times \mathbb{R} \subseteq \mathbb{R}^3$ with the induced flat metric has, as geodesics, the straight lines on its universal cover $\mathbb{R}^2$ projected down — meridians (vertical), circles of latitude (horizontal), and helices winding around. This shows that geodesics need not be globally length-minimising: a helix winding many times around the cylinder is much longer than the direct geodesic between the same endpoints.

**Is an instance: free-falling test particles in general relativity.** In a Lorentzian spacetime $(M, g)$ with signature $(-,+,+,+)$, the worldline of a free-falling massive particle is a timelike geodesic ($g(\dot\gamma, \dot\gamma) < 0$), and the worldline of a light ray is a null geodesic ($g(\dot\gamma, \dot\gamma) = 0$). The geodesic equation $\nabla_{\dot\gamma}\dot\gamma = 0$ is the equation of motion. The Schwarzschild geodesics give the classical tests of GR.

**Is NOT an instance: a great circle traversed at non-constant speed.** The image of the equator on $S^2$ can be parametrised in many ways, e.g. $\gamma(t) = (\cos(t^2), \sin(t^2), 0)$. As an image-curve this is a geodesic, but as a parametrised curve the equation $\nabla_{\dot\gamma}\dot\gamma = 0$ fails — $\dot\gamma$ does not have constant length. The repair is to *reparametrise* by arc length: $\tilde\gamma(s) = (\cos s, \sin s, 0)$. This non-example illustrates that the geodesic equation includes a parametrisation choice and is sensitive to it.

**Is NOT an instance: the boundary of a triangle on a sphere.** The sides are individually geodesic arcs, but the full closed curve has corners — kinks where two geodesics meet at an angle. At a corner the velocity is discontinuous, so $\dot\gamma$ is not even defined, let alone parallel-transported. Piecewise-geodesic curves with corners are an important class but are *not* geodesics in the strict sense; the second variation formula on the index form picks up boundary terms at corners.

**Corollary (constant speed).** $g(\dot\gamma, \dot\gamma)$ is constant along every geodesic. *Calibration check:* take the derivative; $\frac{d}{dt} g(\dot\gamma, \dot\gamma) = 2 g(\nabla_{\dot\gamma}\dot\gamma, \dot\gamma) = 0$ since $\nabla_{\dot\gamma}\dot\gamma = 0$. This uses metric compatibility *and* the geodesic equation; either alone is insufficient.

**Corollary (affine reparametrisation).** If $\gamma$ is a geodesic and $t = as + b$ for $a, b \in \mathbb{R}$, $a \neq 0$, then $\tilde\gamma(s) := \gamma(as + b)$ is also a geodesic. *Calibration check:* compute $\dot{\tilde\gamma} = a\dot\gamma$, then $\nabla_{\dot{\tilde\gamma}}\dot{\tilde\gamma} = a^2 \nabla_{\dot\gamma}\dot\gamma = 0$. So the affine group acts on the set of geodesics, and a geodesic determines a parametrisation only *up to* affine reparametrisation.

**Corollary ([[Def - Isometry|isometries]] map geodesics to geodesics).** If $\varphi : (M, g) \to (N, h)$ is an isometry and $\gamma$ is a geodesic of $g$, then $\varphi \circ \gamma$ is a geodesic of $h$. *Calibration check:* isometries preserve the Levi-Civita connection (uniqueness of the Levi-Civita connection forces this), so they preserve the geodesic equation. This is the basis for the uniqueness trick used to identify geodesics on symmetric spaces — see [[Ex - Great Circles are the Geodesics of the Sphere]].

**Calibration check.** If you can verify (a) that straight lines in $\mathbb{R}^n$ satisfy the geodesic equation, (b) that constant-speed parametrisation is *forced* by the equation rather than an extra assumption, and (c) that the equation in coordinates contains the Christoffel-symbol correction needed for coordinate invariance, then you have understood the definition.

---

# Unlocked by This

> [!tip] The Geodesic Flow on the Tangent Bundle *(from Riemannian Geometry / Dynamical Systems)*
> The geodesic equation, lifted to $TM$, is a first-order autonomous ODE generated by the **geodesic vector field** $G$. Its flow $\phi_t : TM \to TM$ is the **geodesic flow**; on the unit tangent bundle $SM$ it preserves the Sasaki metric and the canonical volume (Liouville form), making it a measure-preserving dynamical system. The geodesic flow on a compact manifold of negative curvature is one of the most-studied examples of a hyperbolic (Anosov) dynamical system — it is *ergodic*, *mixing*, and a model case for the entire theory of chaotic conservative dynamics.

> [!tip] Geodesics in General Relativity *(from General Relativity)*
> In a Lorentzian spacetime $(M, g)$, the same equation $\nabla_{\dot\gamma}\dot\gamma = 0$ defines geodesics. **Timelike geodesics** (where $g(\dot\gamma, \dot\gamma) < 0$) are the worldlines of free-falling massive particles; **null geodesics** ($g(\dot\gamma, \dot\gamma) = 0$) are the worldlines of light rays. The geodesic equation is the equation of motion of free fall — gravity is *not* a force, it is the geometry of spacetime. This is the equivalence principle, made mathematically precise. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] **Sub-Riemannian Geodesics** *(from Sub-Riemannian Geometry)*
> Replace "all of $T_pM$" by a smooth horizontal subbundle $\mathcal{H} \subseteq TM$ — a distribution. A **sub-Riemannian geodesic** is the shortest path among curves whose velocity always lies in $\mathcal{H}$. The geodesic equation is no longer a second-order ODE on $M$ but a constrained Hamiltonian system on $T^*M$, and the resulting geodesics can do surprising things — in the Heisenberg group, the geodesic between two non-horizontal points spirals. Sub-Riemannian geometry is the natural mathematical setting for nonholonomic mechanics (a car or bicycle's wheels are constrained), and the geodesic equation here is the abstract version of the constrained Lagrangian formulation.
