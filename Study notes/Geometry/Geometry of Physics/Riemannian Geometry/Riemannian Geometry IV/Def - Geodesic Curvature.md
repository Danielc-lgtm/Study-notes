---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - First Fundamental Form"
  - "Def - Embedded Submanifold"
tags: [geometry, riemannian-geometry, surfaces, geodesics, intrinsic-curvature]
---

# Notation

Let $M \subset \mathbb{R}^3$ be an oriented regular surface with unit normal $N$, and let $C$ be a smooth curve on $M$ parametrised by arc length $s$, with unit tangent $T(s) = d\mathbf{x}/ds \in T_{\gamma(s)}M$. The intrinsic (covariant) derivative of a tangent field $X$ along $C$ is $\nabla X/ds$. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Axiom Motivation

The desideratum is to measure **how much a curve on $M$ fails to be a [[Def - Geodesic|geodesic]]** — using only intrinsic data (data accessible to an inhabitant of $M$ without leaving the surface). The full curvature vector $\kappa\mathbf{n} = dT/ds$ of $C$ as a space curve in $\mathbb{R}^3$ contains *too much* information: it includes the normal-to-$M$ component, which is the second-fundamental-form data and is extrinsic. Stripping out this normal component leaves the **tangential component** of $dT/ds$ — and this is what an inhabitant of $M$ can measure: it is how the tangent direction turns *within the surface*, relative to parallel transport.

**Why is the normal component the wrong thing for "geodesic-ness"?** A geodesic on $M$ is a curve that an inhabitant of $M$ perceives as "straight" — its tangent direction does not turn at all within the surface. But the same curve, viewed in $\mathbb{R}^3$, may still curve out of the tangent plane (Meusnier's theorem) — that is, $\langle dT/ds, N\rangle = \mathrm{II}(T, T)$ can be nonzero. The classic example: any great circle on $S^2$ is a geodesic (an inhabitant of $S^2$ perceives it as straight), but as a space curve it has curvature $1/a$ in $\mathbb{R}^3$ — that curvature is purely normal, all of it goes into $\mathrm{II}(T, T)$. So "curving in $\mathbb{R}^3$" and "curving on $M$" are different things; the former is the full $dT/ds$, the latter is the tangential projection.

**Why "tangential projection of $dT/ds$"?** The decomposition $dT/ds = (dT/ds)_{\text{tang}} + (dT/ds)_{\text{norm}}$ is a unique orthogonal decomposition because the tangent plane $T_pM$ and the normal line $\mathbb{R}\cdot N(p)$ are orthogonal complements in $\mathbb{R}^3$. The normal projection is $\langle dT/ds, N\rangle N = \mathrm{II}(T, T)N$, an extrinsic quantity. The tangential projection $\nabla T/ds := dT/ds - \mathrm{II}(T, T)N$ is what remains, and it is intrinsic because it equals the Levi-Civita covariant derivative of $T$ along $C$, computed in terms of the metric alone.

**Why is this intrinsic?** The Christoffel-symbol formula for $\nabla T/ds$ in coordinates,
$$
\left(\frac{\nabla T}{ds}\right)^\gamma = \frac{dT^\gamma}{ds} + \Gamma^\gamma_{\alpha\beta}T^\alpha\frac{du^\beta}{ds},
$$
involves only the Christoffel symbols $\Gamma^\gamma_{\alpha\beta}$, which are computed from the metric $g_{\alpha\beta}$ alone via (8.32). Hence $\nabla T/ds$ depends only on $\mathrm{I}$ and is intrinsic. This is a direct consequence of the [[Thm - Theorema Egregium of Gauss|intrinsic nature of the Levi-Civita connection]].

**The forced form of the definition.** Given that we want an intrinsic measure of "how much a curve bends on $M$", the only natural choice is the magnitude of $\nabla T/ds$ — equivalently the magnitude of the tangential projection of the ambient curvature vector. There is essentially no other intrinsic scalar that measures the bending of a unit-tangent curve: lengths and angles only give arc length, and arc length is not "bending". So the geodesic curvature $\kappa_g = |\nabla T/ds|$ is uniquely determined as the right intrinsic curvature of a curve on a surface.

A forward reference: in the **Gauss–Bonnet theorem with boundary**, $\int_{\partial M}\kappa_g\, ds$ appears as the boundary contribution to the topological identity, and it encodes the "turning rate" of the tangent direction relative to parallel transport along the boundary curve. This is consistent: the geodesic curvature *is* the rate at which the unit tangent turns within the tangent plane, hence the rate at which it fails to be parallel-transported, hence the rate at which $C$ fails to be a geodesic.

---

# The Definition

> **Definition (Geodesic Curvature).** Let $M \subset \mathbb{R}^3$ be an oriented regular surface and $C$ a smooth curve on $M$ parametrised by arc length, with unit tangent $T$. The **geodesic curvature vector** of $C$ at the point $\gamma(s)$ is
> $$
> \vec\kappa_g(s) := \frac{\nabla T}{ds} = \frac{dT}{ds} - \left\langle\frac{dT}{ds}, N\right\rangle N,
> $$
> the tangential projection (to $T_{\gamma(s)}M$) of the ambient acceleration $dT/ds$. The **geodesic curvature** (scalar) is the magnitude
> $$
> \kappa_g(s) := \left|\frac{\nabla T}{ds}\right|_\mathrm{I}.
> $$

Equivalently, in local coordinates with $\gamma(s) = \mathbf{x}(u(s), v(s))$,
$$
\left(\frac{\nabla T}{ds}\right)^\gamma = \frac{d^2u^\gamma}{ds^2} + \Gamma^\gamma_{\alpha\beta}\frac{du^\alpha}{ds}\frac{du^\beta}{ds},
$$
where $\Gamma^\gamma_{\alpha\beta} = \tfrac{1}{2}g^{\gamma\tau}(\partial_\beta g_{\alpha\tau} + \partial_\alpha g_{\beta\tau} - \partial_\tau g_{\alpha\beta})$ are the Christoffel symbols of the [[Def - First Fundamental Form|first fundamental form]] $g_{\alpha\beta}$.

**Decomposition of the ambient curvature vector.** For any curve $C$ on $M$, the ambient curvature vector $\kappa \mathbf{n} = dT/ds$ decomposes uniquely as
$$
\kappa \mathbf{n} = \vec\kappa_g + \mathrm{II}(T, T)\, N,
$$
the geodesic-curvature vector (tangential, intrinsic) plus the normal-curvature scalar times $N$ (extrinsic). Taking magnitudes,
$$
\kappa^2 = \kappa_g^2 + \mathrm{II}(T, T)^2,
$$
a Pythagorean identity.

**Signed geodesic curvature on an oriented surface.** On an oriented surface $M$, with $T$ the unit tangent and $T^\perp$ the unique unit tangent vector with $\{T, T^\perp, N\}$ positively oriented in $\mathbb{R}^3$, the geodesic curvature has a sign:
$$
\kappa_g = \left\langle\frac{\nabla T}{ds}, T^\perp\right\rangle.
$$
Positive $\kappa_g$ means the curve turns left (relative to the orientation); negative means right.

**Characterisation of [[Def - Geodesic|geodesics]].** A smooth curve $C$ on $M$ (parametrised by arc length) is a [[Def - Geodesic|geodesic]] iff $\kappa_g \equiv 0$, iff $\nabla T/ds \equiv 0$ (the tangent is parallel-transported along $C$).

---

# Relate to Other Fields / Compression

The geodesic curvature is the **intrinsic counterpart** of the ambient curvature of a space curve. Where $\kappa$ measures how a curve in $\mathbb{R}^3$ deviates from a straight line in $\mathbb{R}^3$, $\kappa_g$ measures how a curve on $M$ deviates from a geodesic on $M$. The decomposition $\kappa^2 = \kappa_g^2 + \kappa_n^2$ (with $\kappa_n = \mathrm{II}(T, T)$ the normal curvature) precisely separates the two — bending within the surface (intrinsic) and bending out of the surface (extrinsic).

In **classical mechanics** on a surface (a particle constrained to move on $M$ with no external forces), the **principle of least action** forces the trajectory to be a geodesic — i.e., $\kappa_g = 0$ — because any tangential component of acceleration would correspond to a tangential force, but the only forces present are the normal constraint forces. So a freely moving particle on a constraint surface follows geodesics, with $\kappa_g$ measuring departure from free motion.

In **optics**, a light ray confined to a curved waveguide follows a geodesic (Fermat's principle); $\kappa_g$ along an arbitrary path measures how much that path deviates from the principle of least time.

In **PDE on manifolds**, the **geodesic flow** on the unit tangent bundle is the Hamiltonian flow of the kinetic energy $H = \tfrac{1}{2}|p|^2_g$, and $\kappa_g$ along an arbitrary curve gives a measure of the "geodesic deviation" relevant to **Anosov flows** and **ergodic theory** of geodesic flows on negatively curved surfaces.

**True name:** The geodesic curvature is *the rate at which the tangent direction turns within the tangent plane relative to parallel transport*. The official "tangential projection of $dT/ds$" is the right formal definition, but the operational picture is the rotational rate of $T$ as seen by parallel-transport bookkeeping: if you parallel-transport $T(0)$ along $C$ and compare to $T(s)$, the angle between them grows at rate $\kappa_g$. This makes the **Gauss–Bonnet** boundary integral $\int_{\partial M}\kappa_g\, ds$ feel obvious: it is the total turning angle of the tangent relative to parallel transport, exactly the holonomy of the bounding loop.

---

# Examples / Corollaries

**Is an instance — the equator of $S^2$.** Take $C$ to be the equator of the unit sphere. The unit tangent is $T = -\sin\varphi\, \mathbf{e}_x + \cos\varphi\, \mathbf{e}_y$ (using $\varphi$ as the longitude / arc-length parameter, since $a = 1$). Then $dT/ds = -\cos\varphi\,\mathbf{e}_x - \sin\varphi\,\mathbf{e}_y = -\mathbf{x}$, where $\mathbf{x}$ is the position vector on $S^2$. The unit normal at points of the equator is $N = \mathbf{x}$ (outward), so $\langle dT/ds, N\rangle = -1$ — the normal curvature is $-1$ (consistent with $\kappa = 1/a = 1$, $\kappa_n = -1$ Frankel-convention). The tangential projection is $dT/ds - \langle dT/ds, N\rangle N = -\mathbf{x} + \mathbf{x} = 0$. So $\kappa_g = 0$: the equator is a geodesic of $S^2$, as expected for a great circle.

**Is an instance — a parallel (circle of latitude) on $S^2$.** Take $C$ to be the circle of latitude $\theta = \theta_0$ on $S^2$, parametrised by $\varphi \in [0, 2\pi]$. Arc length is $s = a\sin\theta_0 \cdot \varphi$. The tangent vector to $C$ in $\mathbb{R}^3$ is $T = (-\sin\varphi, \cos\varphi, 0)$. Then $dT/d\varphi = (-\cos\varphi, -\sin\varphi, 0)$ and $dT/ds = (1/(a\sin\theta_0))dT/d\varphi$. The unit normal at points of the parallel is $N = (\sin\theta_0\cos\varphi, \sin\theta_0\sin\varphi, \cos\theta_0)$. One computes $\langle dT/ds, N\rangle = -\sin\theta_0/(a\sin\theta_0) = -1/a$, so the tangential part is $\vec\kappa_g = (-\cos\varphi, -\sin\varphi, 0)/(a\sin\theta_0) - (-1/a)(\sin\theta_0\cos\varphi, \sin\theta_0\sin\varphi, \cos\theta_0)$. After simplification, $|\vec\kappa_g| = \cos\theta_0/(a\sin\theta_0) = \cot\theta_0/a$. So $\kappa_g = \cot\theta_0/a$, which vanishes only at the equator $\theta_0 = \pi/2$ — the only parallel that is a geodesic.

**Is an instance — a straight line in the plane.** $dT/ds = 0$, so $\nabla T/ds = 0$, $\kappa_g = 0$. Straight lines are the geodesics of the plane.

**Is an instance — a circle of radius $r$ in the plane.** $dT/ds = -\hat r/r$ (radial direction inward), $N = \mathbf{e}_z$ (vertical, since we are in the $xy$-plane), so $\langle dT/ds, N\rangle = 0$. The tangential projection is the full $dT/ds$, so $\kappa_g = 1/r$ — same as the ambient curvature, since $\kappa_n = 0$ for a plane curve in the $xy$-plane.

**Is NOT an instance — the magnitude of $dT/ds$.** A common confusion is $\kappa = |dT/ds|$ versus $\kappa_g = |\nabla T/ds|$. The first is the *ambient* curvature in $\mathbb{R}^3$; the second is *intrinsic*. They agree only when the normal curvature $\mathrm{II}(T, T) = 0$, i.e., when $T$ is an asymptotic direction. **Counterexample:** A great circle on $S^2$ has $\kappa = 1/a$ and $\kappa_g = 0$ — these are very different numbers.

**Is NOT an instance — a parametrisation by non-arc-length.** The formula $\kappa_g = |\nabla T/ds|$ requires $C$ to be parametrised by arc length so that $T$ is the unit tangent. For a general parametrisation $\gamma(t)$, one must first compute the unit tangent $T = \dot\gamma/|\dot\gamma|$ and then $\nabla T/ds = (\nabla T/dt)/|\dot\gamma|$ — there is a Jacobian factor. Forgetting this gives wrong answers.

**Corollary — the angle of parallel transport equals the integrated geodesic curvature.** If $X(s)$ is a vector parallel-transported along $C$ and $\theta(s) = \angle(T(s), X(s))$ is the angle from the tangent to $X$, then $\kappa_g = |d\theta/ds|$ (Frankel problem 8.7(2)). So $\int_C \kappa_g\, ds$ is the total angle by which $T$ rotates relative to parallel transport along $C$. This is the surface-level precursor of holonomy = $\int K\, dA$ on a disc (see [[Ex - Holonomy around a Spherical Cap is the Solid Angle]]).

**Corollary — geodesic curvature is intrinsic.** Since $\nabla T/ds$ is defined entirely by the Christoffel symbols of the metric, $\kappa_g$ depends only on the first fundamental form. Two surfaces that are locally isometric (a plane and a cylinder, say) have curves with the same $\kappa_g$ when corresponding curves are taken — even though their ambient curvatures $\kappa$ in $\mathbb{R}^3$ may differ. This is a special case of the broader intrinsicity of the Levi-Civita connection.

**Calibration check.** If you have understood the definition, you should be able to: (i) verify that the geodesic curvature of a parallel of latitude $\theta_0$ on the unit sphere is $\cot\theta_0$, and check that this vanishes at the equator (the only latitude that is a geodesic); (ii) compute that for a curve on the cylinder $\mathbf{x}(u, v) = (a\cos u, a\sin u, v)$ parametrised as a helix $u = \omega s, v = \mu s$ with $a^2\omega^2 + \mu^2 = 1$, the geodesic curvature is zero — every helix on the cylinder is a geodesic (consistent with the cylinder being isometric to the plane, where straight lines wrap into helices); (iii) confirm the Pythagorean identity $\kappa^2 = \kappa_g^2 + \kappa_n^2$ on the example of a parallel of $S^2$, where $\kappa = 1/(a\sin\theta_0)$ (the curvature of a circle of radius $a\sin\theta_0$ in space), $\kappa_g = \cot\theta_0/a$, $\kappa_n = -1/a$.

---

# Unlocked by This

> [!tip] Geodesics on Surfaces *(from §4.4)*
> A geodesic is precisely a curve with $\kappa_g \equiv 0$ — the tangent is parallel-transported along itself, the "intrinsically straight" curves on $M$. The geodesic equation $\ddot u^\gamma + \Gamma^\gamma_{\alpha\beta}\dot u^\alpha\dot u^\beta = 0$ is the equation $\nabla T/ds = 0$ written out in components. See [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]] for the abstract treatment.

> [!tip] Parallel Transport and Holonomy *(from §4.4)*
> A tangent vector field $X$ along $C$ is **parallel-transported** if $\nabla X/ds = 0$. Around a closed loop on $M$, parallel transport returns $X$ to a rotated version of itself; the rotation angle is the **holonomy**, equal to $\int_D K\, dA$ for any disc $D$ with boundary $\partial D = C$ (the surface-level **Ambrose–Singer theorem**). The geodesic curvature is the *infinitesimal* turning rate that integrates to the holonomy angle.

> [!tip] Gauss–Bonnet with Boundary *(from §4.3)*
> The boundary-corrected Gauss–Bonnet formula reads
> $$
> \int_M K\, dA + \int_{\partial M}\kappa_g\, ds + \sum_i (\pi - \alpha_i) = 2\pi\chi(M),
> $$
> where the $\alpha_i$ are exterior angles at corners. The geodesic-curvature term is the natural boundary contribution, ensuring the formula holds for surfaces with boundary (e.g., a hemisphere, where the equator boundary integral is zero since the equator is a geodesic, $\kappa_g = 0$).
