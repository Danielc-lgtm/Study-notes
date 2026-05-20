---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Continuous Map"
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis]
---

# Notation

$[a, b] \subseteq \mathbb{R}$ is a closed bounded real interval; $\gamma : [a, b] \to \mathbb{C}$ is a curve. The image $\gamma^* = \gamma([a, b]) \subseteq \mathbb{C}$ is the **trace** of $\gamma$; $\gamma$ itself is the *parametrization*. The derivative $\gamma'(t) \in \mathbb{C}$ is the one-variable derivative of a complex-valued function of a real variable: if $\gamma(t) = x(t) + iy(t)$, then $\gamma'(t) = x'(t) + iy'(t)$. Full notation registry on [[Complex Analysis I — Basic Notions]].

---

# Axiom Motivation

We need a notion of "path in the plane" precise enough to support two things: (a) integration along the path — needed for contour integration in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]] — and (b) the notion of "joining two points" used in path-connectedness of a [[Def - Domain in the Complex Plane|domain]]. These two demands pull in opposite directions, and the layered definition — *curve*, *$C^1$ curve*, *piecewise $C^1$ curve* — reflects the compromise.

For path-connectedness, we want the *weakest* notion: continuity is enough. Any two points joined by *any* continuous path lie in the same connected component, and weakening the regularity here would make the theory of domains less useful. So a *curve* is just a continuous map $\gamma : [a, b] \to \mathbb{C}$. No smoothness, no special structure — just a continuous deformation from one point to another. This is the right notion for *topology*.

For *integration* — $\int_\gamma f\,dz := \int_a^b f(\gamma(t)) \gamma'(t)\,dt$ — we need $\gamma'(t)$ to exist almost everywhere, and at least continuously where it does. The minimum requirement is *piecewise $C^1$*: the interval $[a, b]$ partitions into finitely many subintervals on each of which $\gamma$ is $C^1$, allowing finitely many "corner" points where the tangent jumps. This admits all the curves one wants to integrate over — line segments, circles, polygonal paths, boundaries of triangles — while remaining flexible enough to concatenate paths without breaking the regularity. A pure $C^1$ curve (continuously differentiable everywhere on $[a, b]$) is the cleanest case, but the corner points of, say, a triangle boundary force us to weaken to piecewise.

Why insist that the derivative be *continuous* on each piece, not just exist? Because the integration formula $\int_a^b f(\gamma(t)) \gamma'(t)\,dt$ uses $\gamma'$ as an integrand, and the cleanest theory (Riemann integration) is for continuous functions. Continuity also forbids pathological cases — derivatives that exist everywhere but are unbounded, for instance — without ruling out anything one actually wants to integrate over.

The choice of *closed bounded interval* $[a, b]$ as the parameter space is essential: it makes the trace $\gamma^*$ compact (the continuous image of a compact set), so suprema of $|f|$ on the path exist and the integral makes sense. An open or unbounded parameter interval would force one to treat improper integrals, which is a separate complication best avoided at the basic level.

Finally, we keep *parametrization* and *trace* separate. The same subset of $\mathbb{C}$ can be parametrized by many different curves — going faster or slower, going forwards or backwards — and the contour integral depends on the parametrization (specifically, its orientation). Reparametrizations that preserve orientation give the same integral; reversing orientation negates it. So the curve is not just its image, and we keep the function $\gamma$ as the primary object.

---

# The Definition

**Curve.** A **curve** in $\mathbb{C}$ is a continuous map
$$\gamma : [a, b] \to \mathbb{C}, \qquad [a, b] \subseteq \mathbb{R}$$
where $[a, b]$ is a closed bounded interval. Its **trace** is $\gamma^* := \gamma([a, b])$.

**$C^1$ curve.** A curve $\gamma : [a, b] \to \mathbb{C}$ is **$C^1$ (continuously differentiable)** if its derivative $\gamma'(t)$ exists and is continuous on $[a, b]$, where at the endpoints $a, b$ the derivative is taken as a one-sided limit.

**Piecewise $C^1$ curve.** A curve $\gamma : [a, b] \to \mathbb{C}$ is **piecewise $C^1$** if there is a partition $a = t_0 < t_1 < \ldots < t_n = b$ such that $\gamma|_{[t_{i-1}, t_i]}$ is $C^1$ for each $i = 1, \ldots, n$.

**Closed curve.** A curve is **closed** if $\gamma(a) = \gamma(b)$.

**Simple curve.** A curve is **simple** if it is injective on $[a, b)$ — equivalently, the curve does not cross itself except possibly at the endpoints (a simple closed curve has $\gamma(a) = \gamma(b)$ but is otherwise injective).

**Arc length.** For a $C^1$ curve, $L(\gamma) := \int_a^b |\gamma'(t)|\,dt$ — the **length** of the curve.

---

# Relate to Other Fields / Compression

In **differential topology**, a curve is a smooth map from a 1-manifold (the interval $[a, b]$) into a 2-manifold ($\mathbb{C} \cong \mathbb{R}^2$). The $C^1$ regularity is the minimum for the curve to have a well-defined tangent vector at every point.

In **measure theory**, a piecewise $C^1$ curve has finite arc length (by the integral formula), so its trace is a *rectifiable* set — one for which length is well-defined. This is the analytic precondition for line integrals to converge.

In **algebraic topology**, a curve $\gamma : [0, 1] \to X$ is a **path** in $X$. The homotopy classes of closed paths form the fundamental group $\pi_1(X, x_0)$. The complex-analytic notion is identical to the topological path, except that for analysis one needs piecewise regularity to integrate.

---

# Examples / Corollaries

**Is an instance — the line segment.** $\gamma(t) = (1-t)z_1 + tz_2$ for $t \in [0, 1]$, $z_1, z_2 \in \mathbb{C}$. $C^1$ everywhere with $\gamma'(t) = z_2 - z_1$. Length $|z_2 - z_1|$. The simplest path.

**Is an instance — the unit circle.** $\gamma(t) = e^{it}$ for $t \in [0, 2\pi]$. $C^1$ everywhere with $\gamma'(t) = ie^{it}$. Closed (since $\gamma(0) = 1 = \gamma(2\pi)$) and simple (no self-intersections inside $[0, 2\pi)$). Length $2\pi$.

**Is an instance — the boundary of a triangle.** Concatenate three line segments. Piecewise $C^1$ but not $C^1$ (corners where the tangent jumps). Closed and simple. Length the sum of the three side lengths.

**Is NOT an instance of a $C^1$ curve, but IS piecewise $C^1$ — the unit square boundary.** Four line segments concatenated. Corners at the four vertices where the tangent jumps. Common contour for elementary problems.

**Is NOT an instance — a "curve" defined on an open interval.** Restricting the parameter to $(0, 1)$ makes the trace non-compact and breaks the integration theory. Always parametrize over a *closed* interval.

**Calibration check.** Verify that the curve $\gamma(t) = e^{2\pi it}$ for $t \in [0, 1]$ is a simple closed $C^1$ curve, with $\gamma'(t) = 2\pi i e^{2\pi it}$ and length $2\pi$; and that the figure-eight $\gamma(t) = \sin(2t)(\cos t, \sin t)$ is closed but *not* simple (self-intersection at the centre). If you can also see that the "circle traversed twice" $\gamma(t) = e^{2it}$ on $[0, 2\pi]$ is closed but *not* simple (every point hit twice except the starting point), you have understood the distinction.

---

# Unlocked by This

> [!tip] Contour Integrals *(from this topic)*
> The piecewise $C^1$ regularity is exactly what is needed to define [[Def - Contour Integral|contour integrals]] $\int_\gamma f\,dz = \int_a^b f(\gamma(t))\gamma'(t)\,dt$ as Riemann integrals. The entire machinery of [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]] — Cauchy's theorem, the integral formula, the residue theorem — is built on this notion.

> [!tip] Winding Number *(from CA III)*
> For a closed curve $\gamma$ not passing through $0$, the **winding number** $I(\gamma; 0) = \frac{1}{2\pi i}\int_\gamma dz/z$ counts the number of times $\gamma$ wraps around the origin. It is the key topological invariant of a closed curve in a multiply connected domain.
