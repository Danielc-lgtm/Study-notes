---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Jacobi Field"
  - "Def - Geodesic"
  - "Def - The Riemannian Exponential Map"
tags: [geometry, riemannian-geometry, conjugate-points, jacobi-fields]
---

# Notation

$(M, g)$ a Riemannian manifold, $\gamma : I \to M$ a [[Def - Geodesic|geodesic]] with $p = \gamma(0)$. $J$ denotes a [[Def - Jacobi Field|Jacobi field]] along $\gamma$, satisfying $J'' + R(J, T)T = 0$ with $T = \dot\gamma$. $\exp_p$ is the [[Def - The Riemannian Exponential Map|Riemannian exponential map]]. The Riemann curvature operator on the orthogonal complement $T^\perp \subseteq T_{\gamma(t)} M$ is the linear map $w \mapsto R(w, T)T$. The full registry is on [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

---

# Axiom Motivation

The motivating question is: **where along a geodesic does the local Riemannian theory break down, and what is the precise geometric content of that breakdown?** The local theory works inside a region where the exponential map is a [[Def - Diffeomorphism|diffeomorphism]] — there we have normal coordinates, a smooth distance function, and a guarantee that [[Def - Geodesic|geodesics]] minimise. The *boundary* of this region is the **conjugate locus**, and conjugate points are the parameters at which the locus is hit.

Two equivalent characterisations of conjugate points exist, and the connection between them is the central content of the theory.

**The exponential-map characterisation.** $\exp_p$ is a local diffeomorphism near $v \in T_pM$ iff $d(\exp_p)_v : T_pM \to T_{\exp_p(v)}M$ is invertible. So the *failure* of $\exp_p$ to be a local diffeomorphism is exactly the kernel of $d(\exp_p)_v$: a nonzero $w \in T_pM$ with $d(\exp_p)_v(w) = 0$. We then say $\exp_p(v)$ is **conjugate to $p$** along $\gamma_v$, with multiplicity equal to $\dim \ker d(\exp_p)_v$.

**The Jacobi-field characterisation.** As we showed in [[Def - Jacobi Field]], the Jacobi field along $\gamma_v$ with $J(0) = 0$ and $J'(0) = w$ is exactly $J(t) = d(\exp_p)_{tv}(tw)$. So $d(\exp_p)_{v}(w) = J(1) = 0$ iff there is a nonzero Jacobi field along $\gamma_v$ vanishing at $0$ *and* at $1$. The conjugate point $\gamma_v(1)$ is therefore the place "where a one-parameter family of geodesics through $p$ comes back together to first order".

These are the same condition, and the dictionary between them is one of the key technical achievements of the theory. The Jacobi-field side is *computable*: you solve a linear ODE. The exponential-map side is *geometric*: you read off the failure of $\exp_p$ to be a diffeomorphism.

**Why this matters.** The conjugate locus is the boundary of the region where:

1. Geodesics from $p$ are uniquely characterised by their endpoint (within the injectivity radius, $\exp_p$ is injective).
2. Geodesics from $p$ are *length-minimising* (the second variation of length is positive-definite below the first conjugate point, fails to be at the conjugate point, and is negative beyond it; see [[Thm - Second Variation of Arc Length]] and [[Def - The Index Form]]).
3. Normal coordinates exist (defined via the inverse of $\exp_p$, which only exists where $\exp_p$ is a diffeomorphism).
4. The distance function $d_g(p, \cdot)$ is smooth.

So conjugate points are not a curiosity — they are the place where the local Riemannian theory hands off to the global theory. Below the first conjugate point, everything is regular and matches the Euclidean intuition. At and beyond conjugate points, all of these regularity properties fail, and the global structure of the manifold (topology, curvature integrals) starts to play a role.

**Why the multiplicity matters.** The multiplicity of a conjugate point is the [[Def - Dimension|dimension]] of the kernel of $d(\exp_p)_v$, or equivalently the dimension of the space of Jacobi fields along $\gamma_v$ vanishing at $0$ and $1$. On the round sphere $S^n$ of radius $1$, the antipode is conjugate to any point with multiplicity $n - 1$ — *every* direction tangent to a great circle through $p$ at $-p$ is a Jacobi-field direction that returns to zero. This high multiplicity is exactly why $\exp_p$ on the sphere collapses an entire sphere of radius $\pi$ in $T_pS^n$ to a single point.

A subtler design choice is the **directionality of "conjugate"**. The definition is symmetric: $q$ is conjugate to $p$ along $\gamma$ iff $p$ is conjugate to $q$ along the reverse geodesic. This is because the Jacobi equation is preserved under $t \mapsto -t$ (with appropriate adjustment of $J'$), and "a Jacobi field vanishing at both endpoints" is symmetric in the two endpoints. So conjugate-pair is a symmetric relation, and "the conjugate locus of $p$" is well-defined as a subset of $M$ (not a directed structure).

**The eigenvalue link.** When the curvature operator $R(\cdot, T)T : T^\perp \to T^\perp$ has eigenvalues $\lambda_1(t), \ldots, \lambda_{n-1}(t)$ along the geodesic, the Jacobi equation in a parallel-transported basis becomes a decoupled system of $n-1$ scalar Sturm–Liouville equations $f_i'' + \lambda_i(t) f_i = 0$. **A conjugate point appears at the first $t_0 > 0$ at which any of these scalar equations has a non-trivial solution vanishing at both $0$ and $t_0$**, and the multiplicity is the number of equations whose solutions vanish simultaneously. *Positive eigenvalues force focusing*, with the time-to-conjugate point bounded by $\pi / \sqrt{\lambda_{\max}}$ via Sturm comparison; *non-positive eigenvalues forbid conjugate points entirely*, since the corresponding Sturm equation $f'' + \lambda f = 0$ with $\lambda \leq 0$ has no zero between $0$ and $\infty$. This eigenvalue/conjugate-point dictionary is the technical heart of all comparison theorems and the source of the curvature-to-topology bounds (Bonnet–Myers, Cartan–Hadamard) developed in [[Riemannian Geometry III — Riemann Curvature and Topology]].

---

# The Definition

Let $\gamma : [0, T] \to M$ be a geodesic on a Riemannian manifold. The points $p := \gamma(0)$ and $q := \gamma(t_0)$ (for some $t_0 \in (0, T]$) are **conjugate along $\gamma$** if there exists a non-zero [[Def - Jacobi Field|Jacobi field]] $J$ along $\gamma$ with $J(0) = 0$ and $J(t_0) = 0$.

The **multiplicity** of the conjugate pair is the dimension of the space of such Jacobi fields:
$$\mathrm{mult}_{\gamma}(p, q) := \dim\{J \text{ Jacobi along } \gamma : J(0) = J(t_0) = 0\}.$$

**Equivalent characterisation via the exponential map.** Writing $v = \dot\gamma(0)$ and $\gamma = \gamma_v$, the points $p$ and $q = \gamma_v(t_0)$ are conjugate along $\gamma_v$ if and only if $d(\exp_p)_{t_0 v} : T_{t_0 v}(T_pM) \to T_{\gamma_v(t_0)} M$ is not invertible. The multiplicity equals $\dim \ker d(\exp_p)_{t_0 v}$.

**Equivalent characterisation via the index form.** Restricting to *normal* variations along the unit-speed reparametrisation of $\gamma$, $p$ and $q$ are conjugate iff the [[Def - The Index Form|index form]] $I$ on the space of normal variation fields along $\gamma|_{[0, t_0]}$ vanishing at the endpoints has non-trivial kernel.

**Conjugate locus.** The **conjugate locus** of $p$ in $M$ is the set of all points $q \in M$ that are conjugate to $p$ along *some* geodesic $\gamma$ from $p$ to $q$. The **cut locus** of $p$ (a related but distinct notion) is the set of points at which a minimising geodesic from $p$ stops being unique-and-minimising; the cut locus is contained in (and often equals) the closure of the conjugate locus.

---

# Relate to Other Fields / Compression

**True name:** **a parameter value at which the linearisation of the geodesic flow becomes degenerate**. In dynamical-systems language, the linearised flow along $\gamma$ has a vanishing solution that returns to a transversal — a "focal point" of the geodesic flow. The Riemannian-geometry name is "conjugate point"; the symplectic-geometry name (which generalises beyond geodesic flow) is "Maslov point" or "focal point".

**Conjugate points are eigenvalues of the curvature operator translated into time.** In the simplest setting — geodesic in a space of *constant* sectional curvature $K$ — the Jacobi equation on a normal field becomes $f'' + Kf = 0$. For $K > 0$ the solution with $f(0) = 0$ is $\sin(\sqrt K t)/\sqrt K$, vanishing at $t = \pi / \sqrt K$ — the **first conjugate distance**. For $K = 0$ the solution is $t$, never vanishing — no conjugate points. For $K < 0$ the solution is $\sinh(\sqrt{|K|} t)/\sqrt{|K|}$, never vanishing — no conjugate points. So:
- *Positive curvature gives conjugate points at distance $\pi/\sqrt K$.*
- *Zero or negative curvature: no conjugate points.*

For varying curvature, Sturm comparison says: if $K \geq K_0 > 0$ everywhere along $\gamma$, then a conjugate point appears no later than $\pi/\sqrt{K_0}$ (the **Bonnet–Myers diameter bound**). If $K \leq 0$ along $\gamma$, no conjugate point appears (the **Cartan–Hadamard non-conjugate-point theorem**).

**Conjugate points trigger the failure of length-minimisation.** By the [[Thm - Second Variation of Arc Length|second variation of arc length]], the geodesic $\gamma$ from $p$ to $q$ minimises length iff the index form $I$ is positive-semidefinite on normal variations vanishing at the endpoints. The kernel of $I$ on this space is exactly the space of Jacobi fields vanishing at both endpoints. So:
- *Below the first conjugate point*: $I > 0$, $\gamma$ minimises strictly.
- *At the first conjugate point*: $I \geq 0$ with kernel, $\gamma$ minimises but not strictly.
- *Past the first conjugate point*: $I$ has a negative direction, $\gamma$ is *not* a local minimiser.

This is the **Morse index theorem**: the index of $I$ equals the number of interior conjugate points counted with multiplicity.

---

# Examples / Corollaries

**Is an instance: the antipode of $p$ on the round sphere $S^n$.** On the unit sphere with the round metric, $K = 1$ everywhere. Along any unit-speed geodesic from $p$, the Jacobi equation on a normal field is $f'' + f = 0$, with the solution $f(t) = \sin t$ vanishing at $t = \pi$. So the antipode $-p$ is conjugate to $p$ along *every* geodesic through $p$, at parameter $\pi$. The multiplicity is $n - 1$ — *every* direction in $T^\perp$ supports a vanishing Jacobi field. See [[Ex - Conjugate Points on the Round Sphere are Antipodal]].

**Is an instance: equatorial conjugate points on an oblate ellipsoid.** On an ellipsoid with axes $a \geq b > 0$ (oblate, like Earth), a geodesic along the equator (the longer axis) has a conjugate point not at the antipode but slightly earlier, because the equatorial circle has higher Gaussian curvature than the average. This non-trivial example shows conjugate points depend on the geometry along the specific geodesic, not on a global average curvature.

**Is an instance: in Euclidean space, no conjugate points exist.** With $R = 0$ identically, the Jacobi equation is $f'' = 0$ with linear solutions $at + b$. The only solution with $f(0) = 0$ is $f(t) = at$, which only vanishes at $t = 0$. So no conjugate points exist along any Euclidean geodesic. Consistent with: $\exp_p$ on $\mathbb{R}^n$ is the identity, always a diffeomorphism.

**Is an instance: in hyperbolic space, no conjugate points exist.** With $K = -1$, the Jacobi equation is $f'' - f = 0$ with hyperbolic solutions; the one vanishing at $0$ is $\sinh t$, never vanishing for $t > 0$. So $\exp_p : T_p\mathbb{H}^n \to \mathbb{H}^n$ is a diffeomorphism (Cartan–Hadamard).

**Is an instance: conjugate points on a Lie [[Def - Group|group]] with bi-invariant metric.** For a one-parameter [[Def - Subgroup|subgroup]] $\gamma(t) = \exp(tX)$, conjugate points along $\gamma$ are at parameters $t_k = 2\pi k / |\lambda|$ where $i\lambda$ is a nonzero imaginary eigenvalue of $\mathrm{ad}_X$ on $\mathfrak g$ (purely imaginary eigenvalues correspond to compact directions). For $SU(2) \cong S^3$, $\mathrm{ad}_X$ on $\mathfrak{su}(2)$ has eigenvalues $\pm i|X|$, giving conjugate points at $t = \pi/|X|$ — consistent with $S^3$ being the round sphere of curvature $1$.

**Is NOT an instance: a cut point that is not a conjugate point.** On a flat torus $T^2 = \mathbb{R}^2 / \mathbb{Z}^2$ with the standard flat metric, $K = 0$, so no conjugate points exist along any geodesic. But the geodesic from the origin to the point $(0, 0)$ via wrapping around once is a "shortest" geodesic that ceases to be minimising past the halfway point — this is a **cut point** (where minimisers cease to be unique-and-minimising) without being a conjugate point. So the cut locus is generally larger than the conjugate locus.

**Is NOT an instance: a parameter where the Jacobi field is nonzero.** Most parameters $t$ along a geodesic are *not* conjugate to the starting point: the Jacobi field with $J(0) = 0$ is nonzero generically. Conjugate points are *exceptional* — they form a discrete subset of the parameter range (by analyticity of solutions to linear ODEs).

**Corollary (conjugate points are isolated).** Along a fixed geodesic $\gamma$, the parameters at which conjugate points occur form a discrete subset of $(0, \infty)$. *Calibration check:* solutions of a second-order linear ODE with nonconstant coefficients have isolated zeros (otherwise by analyticity they would be identically zero on a connected interval).

**Corollary (positivity-of-curvature forces conjugate points).** If the sectional curvature on a unit-speed geodesic $\gamma$ satisfies $K \geq K_0 > 0$ for all 2-planes containing $\dot\gamma$, then $\gamma(t)$ is conjugate to $\gamma(0)$ for some $t \leq \pi/\sqrt{K_0}$. *Calibration check:* this is Sturm comparison applied to the Jacobi equation, comparing $f'' + K_0 f = 0$ (which has zero at $t = \pi/\sqrt{K_0}$) with $f'' + Kf = 0$ where $K \geq K_0$ — the larger coefficient forces an earlier zero. This is the seed of [[Riemannian Geometry III — Riemann Curvature and Topology|Bonnet–Myers]].

**Corollary (non-positive curvature ⟹ no conjugate points).** If sectional curvature $K \leq 0$ on $M$ along $\gamma$, then $\gamma$ has no conjugate points. *Calibration check:* Sturm comparison the other way, against $f'' = 0$.

**Calibration check.** If you can verify (a) that on $S^n$ the antipode is conjugate with multiplicity $n - 1$, (b) that conjugate points correspond exactly to singular values of the linearised exponential map, and (c) that positive curvature forces conjugate points while non-positive curvature forbids them — then you have understood the definition.

---

# Unlocked by This

> [!tip] The Morse Index Theorem *(from Riemannian Geometry / Variational Calculus)*
> The number of conjugate points strictly inside a geodesic $\gamma|_{[0, T]}$, counted with multiplicity, equals the index of the [[Def - The Index Form|index form]] $I$ on the space of normal variations vanishing at the endpoints — i.e., the dimension of a maximal subspace on which $I$ is negative-definite. This is the **Morse Index Theorem** and is the variational core of the theory of geodesics. It is the prototype for the Morse theory of harmonic maps, Yang–Mills connections, and the Seiberg–Witten equations.

> [!tip] **Comparison Geometry and the Bonnet–Myers Diameter Bound** *(from Riemannian Geometry)*
> Positive lower bound on sectional curvature forces conjugate points within a bounded distance, which forces every geodesic to fail to minimise beyond that distance, which (by Hopf–Rinow) forces the manifold to have bounded diameter. **Bonnet–Myers**: if $\mathrm{Ric} \geq (n-1) K_0 g$ with $K_0 > 0$ and $M$ is complete, then $M$ is compact with diameter $\leq \pi/\sqrt{K_0}$ and finite fundamental group. The whole chain is conjugate-point-based; see [[Riemannian Geometry III — Riemann Curvature and Topology]].

> [!tip] **The Cut Locus** *(from Metric Geometry)*
> The conjugate locus is contained in the cut locus, but the latter can be larger. The **cut locus** of $p$ is the set of points at which some minimising geodesic from $p$ stops being uniquely-minimising (whether by encountering a conjugate point or by another minimising geodesic catching up). On the flat torus, the cut locus exists but the conjugate locus is empty. The cut locus controls the smoothness of the distance function $d_g(p, \cdot)$ globally and is the boundary of the **normal neighbourhood** in which the manifold "looks like its tangent space".
