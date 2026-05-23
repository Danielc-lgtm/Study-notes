---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Riemannian Metric"
  - "Def - Smooth Map between Manifolds"
  - "Def - Metric Space"
tags: [geometry, differential-geometry, riemannian-geometry]
---

# Notation

Let $(M, g)$ be a Riemannian manifold (connected, for the distance discussion). A **piecewise smooth curve** on $M$ is a continuous map $\gamma : [a, b] \to M$ such that there exists a partition $a = t_0 < t_1 < \cdots < t_k = b$ with $\gamma|_{[t_{i-1}, t_i]}$ smooth for each $i$. The **velocity** of a smooth curve $\gamma$ at $t$ is $\dot\gamma(t) \in T_{\gamma(t)}M$, defined as $d\gamma_t(\partial_t) = \gamma_*(\partial_t)$. The **speed** is $|\dot\gamma(t)|_g = \sqrt{g_{\gamma(t)}(\dot\gamma, \dot\gamma)}$. We write $L_g(\gamma)$ for the length and $d_g(p, q)$ for the distance. Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

This is a compound page: it defines two interlocking notions — the length of a curve and the Riemannian distance function — because they are introduced together and the distance is defined as an infimum of lengths.

---

# Axiom Motivation

The whole point of installing a Riemannian metric is to be able to *measure*, and the two most basic measurements are the **length of a curve** and the **distance between two points**. The metric $g$ provides an inner product in every tangent space, which gives a norm $|v|_g = \sqrt{g_p(v, v)}$ on each $T_pM$. The norm of the velocity $\dot\gamma(t)$ is the *instantaneous speed* of the curve at parameter $t$, and integrating speed over the parameter gives the *total length* — this is precisely the construction of arc-length from elementary calculus, transported to the manifold setting.

**Why piecewise smooth curves rather than just smooth?** The reason is that the triangle inequality $d_g(p, r) \leq d_g(p, q) + d_g(q, r)$ requires being able to *concatenate* curves. Given a curve $\gamma_1$ from $p$ to $q$ and a curve $\gamma_2$ from $q$ to $r$, the concatenation $\gamma_1 \cdot \gamma_2$ has a corner at $q$ — it is continuous but not smooth there. If we restricted to smooth curves only, this concatenation would be excluded, and we would have to smooth out the corner at each step, ending up with an approximate triangle inequality (which suffices in the end but is awkward). Allowing piecewise smooth curves makes the concatenation immediate and the triangle inequality clean. Lee remarks on this explicitly: "This is one reason why it is important to define the distance function using piecewise smooth curves instead of just smooth ones."

**Why infimum and not minimum?** Because in general no minimising curve exists. Consider $M = \mathbb{R}^2 \setminus \{(0, 0)\}$ with the Euclidean metric. The distance from $(-1, 0)$ to $(1, 0)$ is $2$ — the infimum of lengths over all piecewise smooth curves avoiding the origin — but no such curve achieves the length $2$, because any curve from $(-1, 0)$ to $(1, 0)$ avoiding the origin must take a detour. The infimum is the only consistent definition. The question of when the infimum is achieved — by a *minimising geodesic* — is the content of the Hopf–Rinow theorem and belongs to Riemannian geometry, not this chapter.

**Why connected $M$?** If $M$ is not connected, then two points in different connected components cannot be joined by any continuous curve, let alone a piecewise smooth one. The infimum over an empty set is $+\infty$, which is not a real number, so $d_g$ as defined is not a real-valued metric. One can extend the definition to disconnected manifolds by defining the distance between different components to be $+\infty$ (giving an "extended metric"), or by working one component at a time. We assume connectedness throughout to avoid this technicality. Lee handles the disconnected case explicitly in the proof of the corollary that every smooth manifold is metrisable.

**Why the integral expression?** The length must be reparametrisation-invariant: if $\tilde\gamma = \gamma \circ \varphi$ for a smooth [[Def - Diffeomorphism|diffeomorphism]] $\varphi : [c, d] \to [a, b]$, then $L_g(\tilde\gamma) = L_g(\gamma)$. The integral $\int |\dot\gamma|_g\, dt$ has exactly this invariance, by the change-of-variables formula applied with $\varphi$. Any other natural expression (like $\int g(\dot\gamma, \dot\gamma)\, dt$, the *energy*) is *not* reparametrisation-invariant; the energy depends on the parametrisation and minimising it picks out a particular constant-speed parametrisation of the geodesic. Length is the right notion when one cares only about the path; energy is the right notion when one cares about the parametrisation as well, and is more convenient for variational calculations.

**Why the infimum gives a metric?** Three properties need to hold: $d_g \geq 0$, $d_g(p, p) = 0$, and the triangle inequality. The first two are immediate from the definition (constant curves have length zero). The triangle inequality follows from concatenation: any curve from $p$ to $q$ plus any curve from $q$ to $r$ gives a curve from $p$ to $r$ of total length equal to the sum of the pieces, so $d_g(p, r) \leq L(\gamma_1) + L(\gamma_2)$ for every $\gamma_1, \gamma_2$, and taking infima on the right gives $d_g(p, r) \leq d_g(p, q) + d_g(q, r)$. The non-trivial axiom is **positivity** — that $d_g(p, q) > 0$ for $p \neq q$ — and that requires the local-comparability argument of [[Thm - The Riemannian Distance Makes M a Metric Space]]. The fundamental obstruction would be a curve from $p$ to $q$ of length zero, which would require $|\dot\gamma| = 0$ everywhere; but this forces $\dot\gamma = 0$ identically (since the Riemannian metric is positive-definite), hence $\gamma$ is constant — contradicting $p \neq q$.

---

# The Definition

> **Definition (Length).** Let $(M, g)$ be a Riemannian manifold, and let $\gamma : [a, b] \to M$ be a piecewise smooth curve. The **length** of $\gamma$ with respect to $g$ is
> $$
> L_g(\gamma) \;=\; \int_a^b \bigl|\dot\gamma(t)\bigr|_g\, dt \;=\; \int_a^b \sqrt{g_{\gamma(t)}\bigl(\dot\gamma(t), \dot\gamma(t)\bigr)}\, dt.
> $$
> The integrand is continuous at all but finitely many points and bounded with one-sided limits, so the integral is well defined.

The length is **reparametrisation-invariant**: if $\tilde\gamma = \gamma \circ \varphi$ for a piecewise smooth [[Def - Diffeomorphism|diffeomorphism]] $\varphi$, then $L_g(\tilde\gamma) = L_g(\gamma)$.

In local coordinates $x^i$ on a chart containing the image of $\gamma$, writing $\gamma(t) = (x^1(t), \ldots, x^n(t))$,
$$
L_g(\gamma) \;=\; \int_a^b \sqrt{g_{ij}(x(t))\, \dot x^i(t)\, \dot x^j(t)}\, dt.
$$

> **Definition (Riemannian Distance).** Let $(M, g)$ be a connected Riemannian manifold. For $p, q \in M$, the **Riemannian distance** from $p$ to $q$ is
> $$
> d_g(p, q) \;=\; \inf\bigl\{L_g(\gamma) : \gamma \text{ a piecewise smooth curve from } p \text{ to } q\bigr\}.
> $$
> This is well defined: a piecewise smooth curve from $p$ to $q$ always exists since $M$ is path-connected.

By [[Thm - The Riemannian Distance Makes M a Metric Space]], $(M, d_g)$ is a [[Def - Metric Space|metric space]] whose induced topology coincides with the manifold topology.

---

# Relate to Other Fields / Compression

This is the smooth-manifold version of arc-length from elementary calculus and the curve-length theory of [[Multivariate Analysis I — Differentiation in Several Variables|multivariate analysis]]. In $\mathbb{R}^n$ with the Euclidean metric, $|\dot\gamma|_g = |\dot\gamma|_{\bar g} = \sqrt{\sum (\dot x^i)^2}$ is the usual Euclidean speed, and the length is $\int |\dot\gamma|\, dt$ — the standard arc-length. Riemannian distance in flat $\mathbb{R}^n$ is the Euclidean distance: any straight-line segment achieves the infimum (Problem 13-10 in Lee).

The connection to [[Def - Metric Space|metric spaces]]: the Riemannian distance turns $(M, g)$ into a metric space, joining the differential-geometric and point-set-topological pictures. Every smooth manifold becomes metrisable as a consequence (with any Riemannian metric chosen).

The connection to variational calculus: the length functional $L_g(\gamma)$ is the most basic *functional* one studies on manifolds, and its critical points are **geodesics**. Length minimisation is the variational characterisation of geodesics; the [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|Levi-Civita connection]] makes the geodesic equation explicit. The closely related **energy functional** $E(\gamma) = \tfrac{1}{2}\int g(\dot\gamma, \dot\gamma)\, dt$ is parametrisation-dependent but has nicer variational properties (its critical points are exactly the constant-speed geodesics, while critical points of $L$ are geodesics up to reparametrisation).

**True name:** Length is *the integral of speed over time*, and distance is *the infimum length of connecting paths*. The same definitions as in $\mathbb{R}^n$, transported faithfully to manifolds via the metric.

---

# Examples / Corollaries

**Is an instance — Euclidean arc length.** For $\gamma : [a, b] \to \mathbb{R}^n$ with the Euclidean metric, $L_{\bar g}(\gamma) = \int_a^b \sqrt{\sum (\dot\gamma^i)^2}\, dt$, the usual arc length. The Riemannian distance is the Euclidean distance: $d_{\bar g}(p, q) = |p - q|$, with the straight-line segment as a minimiser (proved in Problem 13-10 of Lee using calculus of variations: the straight line uniquely minimises length among curves with fixed endpoints in $\mathbb{R}^n$).

**Is an instance — great-circle arcs on the sphere.** On $(S^2, \mathring g)$, the distance between two points $p, q$ is the arc length of the great-circle arc connecting them, $d(p, q) = \arccos(p \cdot q)$ (in $\mathbb{R}^3$ inner product). Minimisers exist (great-circle arcs are [[Def - Geodesic|geodesics]]) and are unique except for antipodal pairs, where two distinct minimising great-circle arcs exist.

**Is an instance — the upper-half-plane.** On $(\mathbb{H}^2, g_{\mathbb{H}})$ with $g_{\mathbb{H}} = (dx^2 + dy^2)/y^2$, the [[Def - Geodesic|geodesics]] are vertical lines and circular arcs perpendicular to the $x$-axis. The distance between $(x_1, y_1)$ and $(x_2, y_2)$ has a closed form involving hyperbolic functions, and unlike the Euclidean case, the distance grows logarithmically with $y$-coordinate ratios.

**Is NOT an instance — straight-line "distance" without the metric.** In a general Riemannian manifold, there is no notion of "straight line" without choosing the Levi-Civita connection. Even on $\mathbb{R}^n$, the "straight line in coordinates" notion depends on the chart — in polar coordinates, the path $r =$ const is *not* a straight line in the Cartesian sense. The Riemannian distance is intrinsic and chart-independent; the calculation in any one chart should give a chart-invariant answer.

**Is NOT an instance — infimum achieved.** For $(M, g) = (\mathbb{R}^2 \setminus \{0\}, \bar g)$, the distance from $(-1, 0)$ to $(1, 0)$ is $2$ (the infimum), but no curve in $M$ achieves length $2$ — every curve must detour around the origin. The infimum is not a minimum here.

**Corollary — reparametrisation invariance.** $L_g(\gamma \circ \varphi) = L_g(\gamma)$ for any piecewise smooth reparametrisation $\varphi$. Proof: change of variables in the integral. This is the formal expression of the geometric fact that length is a property of the *image curve*, not of the way it is traced.

**Corollary — concatenation additivity.** If $\gamma$ is piecewise smooth on $[a, b]$ and $c \in (a, b)$, then $L_g(\gamma) = L_g(\gamma|_{[a, c]}) + L_g(\gamma|_{[c, b]})$. Proof: split the integral.

**Corollary — isometry invariance.** If $F : (M, g) \to (N, h)$ is a (local) Riemannian isometry, then $L_h(F \circ \gamma) = L_g(\gamma)$ for every piecewise smooth curve $\gamma$ in $M$ (Lee Exercise 13.24). Distances are preserved: $d_h(F(p), F(q)) = d_g(p, q)$ for global [[Def - Isometry|isometries]]. This is what justifies calling these maps "[[Def - Isometry|isometries]]" — the metric (in the metric-space sense) is preserved.

**Calibration check.** First, compute the length of the helix $\gamma(t) = (\cos t, \sin t, t)$ in $\mathbb{R}^3$ for $t \in [0, 2\pi]$. Expected: $L = \int_0^{2\pi}\sqrt{1 + 1}\, dt = 2\pi\sqrt 2$. Second, compute the length of the great-circle arc $\gamma(t) = (\cos t, \sin t, 0)$ for $t \in [0, \pi/2]$ on the unit sphere $S^2 \subseteq \mathbb{R}^3$. Expected: $L = \pi/2$ (it is a quarter of the equator). Third, on $\mathbb{H}^2$ with the upper-half-plane metric, compute the length of the vertical curve $\gamma(t) = (0, t)$ for $t \in [1, e]$. Expected: $L = \int_1^e (1/t)\, dt = 1$.

---

# Unlocked by This

> [!tip] $(M, d_g)$ is a Metric Space *(from §12.2)*
> The Riemannian distance turns any connected Riemannian manifold into an honest metric space; see [[Thm - The Riemannian Distance Makes M a Metric Space]]. The induced topology coincides with the manifold topology, and every concept of point-set metric topology — Cauchy sequences, completeness, total boundedness, Heine–Borel — becomes available.

> [!tip] Geodesics as Length Minimisers *(from Riemannian Geometry)*
> Critical points of the length functional (or of the related energy functional) are **geodesics** — curves $\gamma$ that locally minimise length. Geodesics generalise straight lines and are characterised by the **geodesic equation** $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$ involving the Christoffel symbols of the [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|Levi-Civita connection]].

> [!tip] Hopf–Rinow Theorem *(from Riemannian Geometry)*
> The **Hopf–Rinow theorem** is the central completeness/connectedness theorem of Riemannian geometry, asserting that for a connected Riemannian manifold the following are equivalent: (i) $(M, d_g)$ is a complete metric space; (ii) $M$ is geodesically complete (every geodesic extends to all parameter values); (iii) every closed bounded subset of $M$ is compact; (iv) for some $p$, $\exp_p$ is defined on all of $T_pM$. Moreover, if any of these hold, any two points are joined by a length-minimising geodesic. This is the bridge between the metric-space picture of distances and the differential picture of geodesics, and the foundational completeness theorem of the subject.

> [!tip] The Energy Functional *(from Calculus of Variations on Manifolds)*
> Closely related is the **energy functional** $E(\gamma) = \tfrac{1}{2}\int g(\dot\gamma, \dot\gamma)\, dt$, defined only up to parametrisation; its critical points are constant-speed geodesics. The energy is more convenient than length for variational arguments because it is differentiable in $\gamma$ (length involves a square root that misbehaves where $\dot\gamma = 0$). The Cauchy–Schwarz inequality $L(\gamma)^2 \leq 2(b - a)E(\gamma)$ links them, with equality iff $\gamma$ has constant speed.
