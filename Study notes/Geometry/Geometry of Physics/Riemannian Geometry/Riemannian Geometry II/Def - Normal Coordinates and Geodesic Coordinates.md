---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - The Riemannian Exponential Map"
  - "Def - Geodesic"
  - "Def - Riemannian Metric"
tags: [geometry, riemannian-geometry, coordinates]
---

# Notation

$(M, g)$ a Riemannian manifold, $p \in M$, and $(e_1, \ldots, e_n)$ an orthonormal basis of $T_pM$ with respect to $g_p$. We write $B_r(0) \subseteq T_pM$ for the Euclidean ball of radius $r$ around the origin and $B_r(p) \subseteq M$ for the metric ball of radius $r$ around $p$. The full registry is at [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]]. **This is a compound page: it defines two interlocking notions — normal coordinates and geodesic polar coordinates — because the polar version is the natural completion of the Cartesian version and the most-used global tool is built from both.**

---

# Axiom Motivation

The motivation is a sharper version of the question that motivated the [[Def - The Riemannian Exponential Map|exponential map]]: **once we have $\exp_p$ as a local [[Def - Diffeomorphism|diffeomorphism]] near $p$, what is the most useful chart we can build from it?** The bare exponential gives a smooth map $T_pM \to M$ near the origin; to turn this into a coordinate chart we need to identify $T_pM$ with $\mathbb{R}^n$.

The natural way is to pick an *orthonormal* basis $(e_1, \ldots, e_n)$ for $T_pM$. The choice of basis matters: with an orthonormal basis the resulting chart will have the property $g_{ij}(p) = \delta_{ij}$, the metric at the centre point is Euclidean — exactly what we want for a coordinate system "centred on Euclidean". With a non-orthonormal basis the metric at $p$ would be some other symmetric positive-definite matrix, and computations would be needlessly cluttered.

The structural payoff is this: in normal coordinates centred at $p$, **the Christoffel symbols all vanish at $p$**:
$$\Gamma^k_{ij}(p) = 0 \quad\text{for all } i, j, k.$$
This is the most useful single property of normal coordinates. The proof is short: the [[Def - Geodesic|geodesics]] through $p$ have the form $\gamma_v(t) = (tv^1, \ldots, tv^n)$ in normal coordinates (because $\exp_p(tv)$ is literally the geodesic point with coordinates $tv$). Substituting into the geodesic equation $\ddot x^k + \Gamma^k_{ij}\dot x^i \dot x^j = 0$ at $t = 0$ gives $\Gamma^k_{ij}(p) v^i v^j = 0$ for *every* $v \in T_pM$, so by symmetry $\Gamma^k_{(ij)}(p) = 0$; the Levi-Civita Christoffel symbols are already symmetric in $(i, j)$, so $\Gamma^k_{ij}(p) = 0$.

From this, $\partial_k g_{ij}(p) = 0$ follows by the Christoffel formula $\Gamma^k_{ij} = \tfrac12 g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$, which is invertible: a symmetric cyclic combination of $\partial g$ equals zero iff all the $\partial g$ vanish (algebra exercise). So normal coordinates achieve, at the centre point:

1. $g_{ij}(p) = \delta_{ij}$ — metric is Euclidean,
2. $\partial_k g_{ij}(p) = 0$ — first-order corrections vanish,
3. $\Gamma^k_{ij}(p) = 0$ — connection vanishes at $p$.

This is the maximum cancellation possible. **The second-order coefficient** $\partial^2_{kl} g_{ij}(p)$, however, **cannot be made to vanish** in any choice of coordinates — and this non-vanishing is *exactly the curvature tensor at $p$*:
$$\partial^2_{kl} g_{ij}(p) = -\tfrac{1}{3}\bigl(R_{ikjl}(p) + R_{iljk}(p)\bigr).$$
So normal coordinates expose the curvature as the leading obstruction to "being Euclidean". Every pointwise tensorial identity in Riemannian geometry can be checked in normal coordinates, where the metric is Euclidean to first order and the only contribution is from this curvature term.

Why these *specific* cancellations and no more? It is a counting argument. A coordinate change near $p$ has $n^2$ free parameters at first order (the Jacobian) and $n^2(n+1)/2$ free parameters at second order (the Hessian terms). The metric has $n(n+1)/2$ independent components at each order. So first-order cancellation of $g$ needs $n(n+1)/2$ constraints and has $n^2$ degrees of freedom — solvable with extra freedom $n(n-1)/2$ left over (this is the rotation freedom, the choice of orthonormal frame). Second-order cancellation of $\partial g$ needs $n^2(n+1)/2$ constraints (one $\partial_k g_{ij}$ for each $(i, j, k)$) and has $n^2(n+1)/2$ second-order degrees of freedom — solvable but with no freedom left over (a *unique* second-order coordinate change cancels $\partial g$). Third-order cancellation of $\partial^2 g$ would need $n^2(n+1)^2/4$ constraints and has only $n^2(n+1)(n+2)/6$ third-order degrees of freedom — *over-determined* in general, and the obstruction is the curvature tensor. So the first two cancellations are coordinate artefacts; the third is genuine geometry.

A subtler design question is whether to use **Cartesian normal coordinates** or **geodesic polar coordinates**. Cartesian normal coordinates are smooth, including at the origin; they are the basic chart. Geodesic polar coordinates $(r, \omega) \in (0, \mathrm{inj}_g(p)) \times S^{n-1}$ are *singular* at $r = 0$ (just like polar coordinates on $\mathbb{R}^2$), but they have the spectacular property of [[Thm - The Gauss Lemma|the Gauss lemma]]: the metric in polar coordinates has the form
$$g = dr^2 + h_{\alpha\beta}(r, \omega)\, d\omega^\alpha d\omega^\beta,$$
with *no* cross term between $dr$ and $d\omega$. This is the *exact* analogue of $dr^2 + r^2 d\Omega^2$ on Euclidean space, with the Euclidean angular metric $r^2 d\Omega^2$ replaced by a Riemannian-corrected version $h_{\alpha\beta}\, d\omega^\alpha d\omega^\beta$. The polar form is what makes geodesics minimising near $p$: the length of any curve is at least the change in $r$, with equality only for radial geodesics.

So we keep both forms. Cartesian normal coordinates are the right setting for *pointwise* computations involving $g$, $\Gamma$, $R$ at the origin. Geodesic polar coordinates are the right setting for *radial* computations involving distance, length-minimisation, and the local geometry of geodesic spheres.

---

# The Definition

Let $(M, g)$ be a Riemannian manifold, $p \in M$, and $\mathrm{inj}_g(p)$ the injectivity radius at $p$. Fix an orthonormal basis $(e_1, \ldots, e_n)$ of $(T_pM, g_p)$, and let $E : \mathbb{R}^n \to T_pM$ be the linear isomorphism $E(x^1, \ldots, x^n) = x^i e_i$.

**(Cartesian) normal coordinates** at $p$ adapted to $(e_1, \ldots, e_n)$ are the coordinate map
$$\varphi := E^{-1} \circ \exp_p^{-1} : U \to \tilde U \subseteq \mathbb{R}^n,$$
defined on the open neighbourhood $U := \exp_p(E(B_{\mathrm{inj}_g(p)}(0))) \subseteq M$. The image $\tilde U$ is the Euclidean ball $B_{\mathrm{inj}_g(p)}(0) \subseteq \mathbb{R}^n$.

In these coordinates, the metric satisfies
$$g_{ij}(p) = \delta_{ij}, \qquad \partial_k g_{ij}(p) = 0, \qquad \Gamma^k_{ij}(p) = 0,$$
where the derivatives and Christoffel symbols are evaluated at $p$ (which corresponds to $x = 0 \in \mathbb{R}^n$). The radial geodesics through $p$ are precisely $\gamma_v(t) = (tv^1, \ldots, tv^n)$ for $v = v^i e_i \in T_pM$.

**Geodesic polar coordinates** at $p$ are the coordinates $(r, \omega) \in (0, \mathrm{inj}_g(p)) \times S^{n-1}$ defined by
$$(r, \omega) \mapsto \exp_p(r \cdot E(\omega)),$$
where $S^{n-1} \subseteq \mathbb{R}^n$ is the unit sphere. In these coordinates, by the [[Thm - The Gauss Lemma|Gauss lemma]], the metric has the form
$$g = dr^2 + h_{\alpha\beta}(r, \omega)\, d\omega^\alpha d\omega^\beta,$$
with no $dr\, d\omega$ cross terms. The radial coordinate $r$ equals the Riemannian distance $d_g(p, \cdot)$, so $r$ is the distance function from $p$ (smooth on $U \setminus \{p\}$).

---

# Relate to Other Fields / Compression

**True name:** **the coordinates in which the manifold is "as Euclidean as possible at one point"**. Operationally, normal coordinates are the chart you use whenever you want to do a Taylor expansion of a geometric quantity at $p$: at the origin the metric is the identity, the Christoffel symbols vanish, and the only non-trivial contribution at order $r^2$ is the curvature. Geodesic polar coordinates are the version adapted to *radial* questions — the distance function, geodesic spheres, length-minimisation of radial geodesics.

**Cartan's principle for general gauge theories.** In gauge theory, you can always choose a gauge (locally) in which the gauge potential $A$ vanishes at one point — the "synchronous gauge". The connection's failure to vanish in a neighbourhood is the curvature $F = dA + A \wedge A$. Normal coordinates are the special case of this principle for the Levi-Civita connection: you can always set $A = \Gamma = 0$ at one point, and the residual non-vanishing in a neighbourhood is the Riemann curvature. See [[Riemannian Geometry I — Connections and Covariant Differentiation]] and [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

**The equivalence principle in general relativity.** Einstein's equivalence principle — locally, gravity can be transformed away by a change to a freely-falling reference frame — is the physicist's name for the existence of normal coordinates. In a Lorentzian normal coordinate chart at $p$, the metric is Minkowski at $p$ and the Christoffel symbols (the gravitational "force") vanish at $p$. The non-vanishing curvature at order $r^2$ is the **tidal force**, the genuine, coordinate-invariant gravitational effect. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Examples / Corollaries

**Is an instance: Euclidean space $\mathbb{R}^n$.** Cartesian normal coordinates centred at any $p \in \mathbb{R}^n$ are just translated Cartesian coordinates $x \mapsto x - p$. The metric is exactly $\delta_{ij}$ everywhere, Christoffels vanish everywhere, and the second-order coefficient of the metric is zero — consistent with zero curvature. Polar normal coordinates are standard polar (or spherical) coordinates.

**Is an instance: the sphere $S^2$.** At the north pole with standard charts, geodesic polar coordinates are $(\theta, \varphi)$ with $\theta$ the colatitude (which equals the arc length from the pole) and $\varphi$ the azimuthal angle. The metric is $d\theta^2 + \sin^2\theta\, d\varphi^2$. Compare to the Euclidean polar metric $dr^2 + r^2 d\varphi^2$: the angular factor $\sin^2\theta$ replaces $\theta^2$, and the Taylor expansion $\sin\theta = \theta - \theta^3/6 + \ldots$ gives $\sin^2\theta = \theta^2 - \theta^4/3 + \ldots$ The second-order deviation from Euclidean is $-\theta^4/3 \cdot d\varphi^2$, which encodes Gaussian curvature $K = +1$. The geodesic polar form is the natural chart.

**Is an instance: hyperbolic plane $\mathbb{H}^2$.** Geodesic polar coordinates at any point have the metric $dr^2 + \sinh^2 r\, d\varphi^2$. The angular factor $\sinh^2 r = r^2 + r^4/3 + \ldots$ has the opposite sign at order $r^4$ from the sphere, encoding $K = -1$. Note that $\sinh r$ grows exponentially with $r$, so geodesic spheres in $\mathbb{H}^2$ have circumference $2\pi \sinh r$, growing exponentially — much faster than Euclidean $2\pi r$.

**Is NOT an instance: arbitrary coordinates centred at $p$.** A general chart centred at $p \in M$ will have $g_{ij}(p)$ some arbitrary symmetric positive-definite matrix, and $\Gamma^k_{ij}(p)$ generally nonzero. So "$\partial_k g_{ij}(p) = 0$" and "$\Gamma^k_{ij}(p) = 0$" are very specific properties of normal coordinates, not general features of any chart. For example, on $\mathbb{R}^2$ with the standard Euclidean metric, the chart $(u, v) := (x + xy, y)$ has $\partial_u g_{uv}(0) = 1 \neq 0$ — Euclidean space has zero curvature, but in non-normal coordinates the first derivatives of $g$ can still be nonzero.

**Is NOT an instance: a chart where $g_{ij}(p) = \delta_{ij}$ but $\partial_k g_{ij}(p) \neq 0$.** Just orthonormalising the basis at $p$ ensures (1) but not (2). E.g., on the sphere $S^2$ with stereographic coordinates from the south pole, at the north pole $g_{ij}$ may have a particular form, but $\partial_k g_{ij}$ will generally not vanish — to *also* kill the first derivatives one must use the exponential-map construction.

**Corollary (geodesics through $p$ are coordinate rays).** In normal coordinates at $p$, the geodesic $\gamma_v$ with $\gamma_v(0) = p, \dot\gamma_v(0) = v$ is given by $\gamma_v(t) = (tv^1, \ldots, tv^n)$ for $|tv| < \mathrm{inj}_g(p)$. *Calibration check:* this follows immediately from the definition $\exp_p(tv) = \gamma_v(t)$ and the identification of normal coordinates with the inverse of $\exp_p$.

**Corollary (the radial distance is exactly $r$).** Within the geodesic polar chart (i.e., within the injectivity radius), the Riemannian distance from $p$ to the point with polar coordinates $(r, \omega)$ is exactly $r$. *Calibration check:* the radial curve $t \mapsto (t, \omega)$ has velocity $\partial_r$, length $\int_0^r 1\, dt = r$, and by [[Thm - The Gauss Lemma|Gauss's lemma]] this is the unique length-minimiser between the endpoints.

**Corollary (Taylor expansion of the metric).** In normal coordinates,
$$g_{ij}(x) = \delta_{ij} - \tfrac{1}{3} R_{ikjl}(p)\, x^k x^l + O(|x|^3),$$
exhibiting the curvature tensor as the second-order Taylor coefficient. *Calibration check:* this is the cleanest statement of the geometric content of curvature; it says that "how much $g$ deviates from Euclidean" is *exactly* the Riemann tensor.

**Calibration check.** If you can verify (a) that on the sphere of radius $1$ the geodesic polar metric at the north pole is $d\theta^2 + \sin^2\theta\, d\varphi^2$, (b) that this expands to $d\theta^2 + \theta^2 d\varphi^2 - \tfrac{\theta^4}{3} d\varphi^2 + O(\theta^6)$ consistent with curvature $K = 1$, and (c) that you understand why $\partial_k g_{ij}(p) = 0$ in normal coordinates is equivalent to $\Gamma^k_{ij}(p) = 0$ — then you have understood the definition.

---

# Unlocked by This

> [!tip] Curvature as the Second Taylor Coefficient *(from Riemannian Geometry)*
> The formula $g_{ij}(x) = \delta_{ij} - \tfrac{1}{3} R_{ikjl}(p) x^k x^l + O(|x|^3)$ in normal coordinates is the *operational definition* of the Riemann curvature tensor: it is "the failure of the metric to be Euclidean to second order in geodesic distance". Every theorem about Riemannian curvature (Bianchi identities, Ricci tensor symmetries, comparison theorems) is, at its root, a statement about this Taylor coefficient. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

> [!tip] The Equivalence Principle in General Relativity *(from General Relativity)*
> In a Lorentzian normal-coordinate chart at $p$, the metric is Minkowski at $p$ and Christoffel symbols vanish at $p$ — *gravity is locally trivialised*. The non-vanishing curvature at order $r^2$ is the **tidal force**, the genuine gravitational effect. This is Einstein's equivalence principle: "locally, no experiment can distinguish gravity from acceleration." See [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] **Harmonic and Normal Coordinates in PDE Theory** *(from Geometric Analysis)*
> Normal coordinates are smooth but not analytic in general, and the curvature tensor is the obstruction. Refined coordinate systems — **harmonic coordinates** (where the coordinate functions satisfy $\Delta x^i = 0$) — are more useful for PDE analysis on manifolds: regularity of the metric tensor in harmonic coordinates is tied to regularity of the Ricci tensor, used in compactness results for Einstein manifolds (Anderson, Cheeger–Naber). Normal coordinates are the warm-up.
