---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Affine Connection on a Vector Bundle"
  - "Def - Christoffel Symbols"
tags: [geometry, riemannian-geometry, connections]
---

# Notation

$(M, \nabla)$ — a smooth manifold with an affine connection on $TM$ (or more generally an affine connection on a vector bundle $E \to M$). $\gamma : I \to M$ — a smooth curve from an open interval $I \subseteq \mathbb{R}$ into $M$, with velocity $\dot\gamma(t) \in T_{\gamma(t)}M$. $V : I \to TM$ — a **vector field along $\gamma$**, meaning a smooth map with $V(t) \in T_{\gamma(t)}M$ for each $t$; equivalently a section of the pulled-back bundle $\gamma^*TM$. $\nabla_t V$ or $DV/dt$ — the covariant derivative of $V$ along $\gamma$, again a vector field along $\gamma$. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Axiom Motivation

We have $\nabla_X Y$ defined when both $X$ and $Y$ are smooth vector fields on $M$. But there are situations where this is more than we have: a curve $\gamma$ has a velocity $\dot\gamma$ that lives only at the points on the curve, and we may want to differentiate a vector field that is also defined only along the curve. Examples: the velocity of a curve $\dot\gamma$ itself; the rate of change of a particle's spin angular momentum along its worldline; the parallel transport of a vector along a path. None of these are vector fields on $M$ — they are vector fields *along the curve* $\gamma$, which is a strictly weaker object.

What we need is an operator $\nabla_t$ that takes a vector field $V$ along $\gamma$ and produces another vector field along $\gamma$, with the natural properties: $\mathbb{R}$-linearity, the Leibniz rule for products with functions of $t$, and consistency with the connection $\nabla$ on $M$ when $V$ extends to a global vector field. The third property pins down what $\nabla_t$ must do: if $V(t) = \tilde V(\gamma(t))$ for some smooth $\tilde V \in \mathfrak{X}(M)$, then $\nabla_t V$ should equal $\nabla_{\dot\gamma}\tilde V$ at $\gamma(t)$. This is well-defined because $\nabla_{\dot\gamma(t)}\tilde V$ at $\gamma(t)$ depends only on $\dot\gamma(t)$ (by $C^\infty$-linearity in $X$) and on the value of $\tilde V$ in a neighbourhood of $\gamma(t)$ — and in fact only on the values along $\gamma$ near $t$.

The existence-uniqueness of $\nabla_t$ is the assertion that this prescription extends consistently to *all* vector fields along $\gamma$, not just those that come from extensions. This is non-trivial because not every vector field along $\gamma$ extends globally — if $\gamma$ has self-intersections, the values of $V$ at the same point of $M$ for different parameter values $t_1, t_2$ can differ, so no global vector field could produce $V$. The proof of existence-uniqueness is by working locally: in any coordinate chart, write $V(t) = V^i(t)\partial_i|_{\gamma(t)}$ for smooth functions $V^i$, and *define*
$$
(\nabla_t V)^k = \dot V^k(t) + \Gamma^k_{ij}(\gamma(t))\,\dot\gamma^i(t)\,V^j(t).
$$
The first term is the ordinary derivative of the components; the second is the **Christoffel correction** that compensates for the rotation of the coordinate frame along the curve. This formula is independent of the choice of chart (because the inhomogeneous parts of the Christoffel transformation cancel the inhomogeneous part of the component differentiation, as in the static covariant-derivative case), and it satisfies all the desired properties.

**Why is the Christoffel correction needed?** In Cartesian coordinates on $\mathbb{R}^n$ with the flat connection, all $\Gamma^k_{ij} = 0$ and $\nabla_t V$ reduces to just $\dot V$ — componentwise differentiation of the components. This is the prototype. Once the manifold is curved (or we use non-Cartesian coordinates on $\mathbb{R}^n$), the coordinate basis vectors $\partial_i$ themselves rotate along the curve, and "componentwise differentiation" no longer captures the intrinsic rate of change. The Christoffel correction subtracts off the rotation rate of the basis, leaving the intrinsic rate of change of $V$. Concretely on $\mathbb{R}^2$ in polar coordinates, a vector with constant Cartesian components — for instance, the constant vector $(1, 0)$ pointing east — has *changing* polar components as you move around a circle, yet its covariant derivative is zero. The Christoffel terms in the polar formula precisely cancel the apparent change in polar components.

**The setting generalises immediately to a vector bundle.** For an affine connection on a general vector bundle $E \to M$, "vector field along $\gamma$" becomes "section of $\gamma^*E$" (i.e., a smooth assignment $V(t) \in E_{\gamma(t)}$), and the covariant derivative $\nabla_t V$ is defined by the same prescription:
$$
(\nabla_t V)^a = \dot V^a + \omega^a{}_b(\dot\gamma(t))\,V^b
$$
in a local frame $(e_b)$ for $E$, with $\omega^a{}_b$ the connection 1-forms. The special case $E = TM$ recovers the formula above with $\omega^k{}_j(\partial_i) = \Gamma^k_{ij}$.

The covariant derivative along a curve is the conceptual *minimum* needed to make sense of "parallel transport" and "geodesic": a curve $V$ along $\gamma$ is **parallel** if $\nabla_t V \equiv 0$, and a curve $\gamma$ is a **geodesic** if its velocity $\dot\gamma$ is parallel along itself, i.e., $\nabla_t \dot\gamma \equiv 0$. Both are linear-ODE conditions in coordinates, with existence-uniqueness following from the ODE theorem.

---

# The Definition

Let $(M, \nabla)$ be a smooth manifold with an affine connection on $TM$, and let $\gamma : I \to M$ be a smooth curve. A **smooth vector field along $\gamma$** is a smooth map $V : I \to TM$ with $V(t) \in T_{\gamma(t)}M$ for every $t \in I$. The set of smooth vector fields along $\gamma$ is denoted $\mathfrak{X}(\gamma)$ and is a $C^\infty(I)$-module.

The **covariant derivative along $\gamma$** is the unique $\mathbb{R}$-linear operator
$$
\nabla_t : \mathfrak{X}(\gamma) \to \mathfrak{X}(\gamma), \qquad V \mapsto \nabla_t V
$$
satisfying

1. **Leibniz rule.** $\nabla_t(fV) = f' V + f\,\nabla_t V$ for $f \in C^\infty(I)$.

2. **Extensibility.** If $V$ extends to a vector field $\tilde V$ on a neighbourhood of $\gamma(I)$ (i.e., $V(t) = \tilde V(\gamma(t))$), then $\nabla_t V(t) = (\nabla_{\dot\gamma(t)}\tilde V)(\gamma(t))$.

Existence and uniqueness are established by the local coordinate expression: in a chart $(x^i)$ around $\gamma(t)$ with coordinate functions $\gamma^i(t) = x^i(\gamma(t))$ and $V(t) = V^j(t)\,\partial_j|_{\gamma(t)}$,
$$
(\nabla_t V)(t) = \bigl[\dot V^k(t) + \Gamma^k_{ij}(\gamma(t))\,\dot\gamma^i(t)\,V^j(t)\bigr]\,\partial_k|_{\gamma(t)}.
$$
This formula is independent of the chart and satisfies the two axioms; conversely, both axioms together force exactly this formula.

The same definition applies to a vector field along $\gamma$ valued in an arbitrary vector bundle $E \to M$ equipped with a connection $\nabla$: in a local frame $(e_a)$ for $E$ with $V(t) = V^a(t)\,e_a|_{\gamma(t)}$,
$$
(\nabla_t V)(t) = \bigl[\dot V^b(t) + \omega^b{}_a(\dot\gamma(t))\,V^a(t)\bigr]\,e_b|_{\gamma(t)}.
$$

---

# Relate to Other Fields / Compression

The compression: **the covariant derivative along a curve is the directional derivative of $V$ in the direction of $\dot\gamma$, with the Christoffel correction needed to compensate for the rotation of the coordinate frame along $\gamma$.** It is what makes "the velocity of a particle changes in this way along its worldline" a coordinate-independent statement.

In **physics**, $\nabla_t V$ is the **proper-time derivative** of a vector quantity carried by a particle. For a relativistic particle moving along a worldline $\gamma(\tau)$ with proper time $\tau$, the rate of change of the particle's four-velocity in its instantaneous rest frame is $\nabla_\tau \dot\gamma$ — and the equation $\nabla_\tau \dot\gamma = 0$ for an unaccelerated particle is the **geodesic equation** of general relativity. The equivalent statement in special relativity (flat spacetime, no $\Gamma$) is "the four-velocity has constant Cartesian components", i.e., the worldline is a straight line. The generalisation to GR is precisely the inclusion of the $\Gamma$ correction — gravitational forces enter as the Christoffel symbols of the spacetime metric.

**True name:** The "true name" of the covariant derivative along a curve is **the time-derivative in the parallel-transport frame**. Given a parallel frame along $\gamma$ — a frame $E_a(t)$ along $\gamma$ with $\nabla_t E_a = 0$ — every vector field $V = V^a E_a$ along $\gamma$ satisfies $\nabla_t V = \dot V^a E_a$, just componentwise differentiation. So in a parallel frame, the covariant derivative looks exactly like the ordinary derivative — no Christoffel correction at all. The Christoffel correction in a generic frame is *precisely* the deviation of the frame from being parallel. Operationally: to compute $\nabla_t V$ at $t_0$, parallel-transport a frame from $t_0$ along $\gamma$, take the ordinary derivative of the components of $V$ in that frame at $t_0$.

---

# Examples / Corollaries

**Example: covariant derivative in Cartesian coordinates on $\mathbb{R}^n$.** All Christoffel symbols vanish, so $\nabla_t V = \dot V$ — ordinary componentwise differentiation. This is the flat-space prototype.

**Example: the velocity of a curve in polar coordinates.** On $\mathbb{R}^2$ with polar coordinates, take $\gamma(t) = (r(t), \theta(t))$ with velocity $\dot\gamma = \dot r\,\partial_r + \dot\theta\,\partial_\theta$. Then $\nabla_t\dot\gamma$ has components $(\ddot r - r\dot\theta^2, \ddot\theta + (2/r)\dot r\dot\theta)$, using $\Gamma^r_{\theta\theta} = -r$ and $\Gamma^\theta_{r\theta} = 1/r$. The geodesic equation $\nabla_t\dot\gamma = 0$ then gives $\ddot r = r\dot\theta^2$ and $\ddot\theta = -(2/r)\dot r\dot\theta$ — and these are precisely the equations for a straight line in polar coordinates, which one can verify by checking that $r = a/\cos(\theta - \theta_0)$ (a line in polar form) satisfies them.

**Example: parallel transport of a vector around a circle of latitude on $S^2$.** Take $S^2$ with the round metric and parallel-transport a vector around a circle of constant latitude $\theta = \theta_0$. The parallel-transport ODE is $\nabla_t V = 0$ along $\gamma(\varphi) = (\theta_0, \varphi)$ — see [[Ex - Parallel Transport around a Geodesic Triangle on the Sphere]] for the worked computation, which gives a rotation by the angle $2\pi(1 - \cos\theta_0)$ around one full circuit. (This is the geometric phase of Foucault's pendulum: the apparent rotation of the pendulum's plane is parallel transport of its swing direction along the latitude circle.)

**Non-example: $\nabla_t V$ along a curve in a frame that is not parallel.** Naively differentiating the components of $V$ in a generic frame (not the coordinate frame, not orthonormal, not parallel) does not give $\nabla_t V$ — the connection 1-forms in that frame contribute additional Christoffel-type corrections. The cleanest computational frames are the coordinate frame (where $\Gamma^k_{ij}$ are the Christoffel symbols), the orthonormal frame (where the connection 1-forms are antisymmetric and the metric-compatibility is automatic), and the parallel frame along $\gamma$ (where the covariant derivative is just componentwise differentiation).

**Corollary (the covariant derivative satisfies the Leibniz rule for inner products of metric-compatible connections).** If $\nabla$ is metric-compatible and $V, W$ are vector fields along $\gamma$, then
$$
\frac{d}{dt}g_{\gamma(t)}(V(t), W(t)) = g_{\gamma(t)}(\nabla_t V, W) + g_{\gamma(t)}(V, \nabla_t W).
$$
This is the integrated form of metric-compatibility, and it is the basis for proving that parallel transport is an isometry ([[Thm - Parallel Transport is an Isometry for Metric-Compatible Connections]]).

**Corollary (geodesics have constant speed for metric-compatible connections).** If $\gamma$ is a geodesic ($\nabla_t \dot\gamma = 0$) and $\nabla$ is metric-compatible, then by the previous corollary $\frac{d}{dt}g(\dot\gamma, \dot\gamma) = 2g(\nabla_t\dot\gamma, \dot\gamma) = 0$, so $|\dot\gamma|^2$ is constant along the geodesic. This is the geometric content of "geodesics are constant-speed straight lines": the velocity has constant magnitude along the curve. For a non-metric-compatible connection (e.g., Weitzenböck on a Lie group with non-bi-invariant metric), this fails.

**Calibration check.** If you can perform the following three computations, you have understood the covariant derivative along a curve. (i) Compute $\nabla_t\dot\gamma$ for the curve $\gamma(t) = (R\cos t, R\sin t)$ on Euclidean $\mathbb{R}^2$ in Cartesian coordinates (answer: $\nabla_t\dot\gamma = -R(\cos t, \sin t)$, the centripetal acceleration), and verify that the same answer comes out in polar coordinates after applying the Christoffel correction. (ii) Verify that the velocity of a great circle on $S^2$ is parallel along itself (i.e., great circles are geodesics) using the Christoffel symbols. (iii) Solve the parallel-transport ODE along the equator of $S^2$ and verify that a vector returns unchanged after a full circuit — and contrast with the rotated result for parallel transport along a non-geodesic circle of constant latitude.

---

# Unlocked by This

> [!tip] Parallel Transport, Geodesics, and Holonomy *(from Riemannian Geometry)*
> The covariant derivative along a curve is the prerequisite for defining [[Def - Parallel Transport|parallel transport]] (the solution of $\nabla_t V = 0$ with given initial value) and **geodesics** (the solution of $\nabla_t\dot\gamma = 0$, equivalently $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$). Parallel transport around a closed loop produces a **holonomy** transformation in $\mathrm{GL}(T_pM)$ — a subgroup of $O(T_pM)$ for metric-compatible connections — whose Lie algebra is controlled by curvature via the **Ambrose-Singer theorem**. The full theory of holonomy groups and **Berger's classification** of irreducible Riemannian holonomy is one of the deeper results of modern differential geometry.

> [!tip] Geodesic Equation and Variational Principles *(from Riemannian Geometry)*
> The condition $\nabla_t\dot\gamma = 0$ has a beautiful variational characterisation: geodesics are critical points of the energy functional $E(\gamma) = \tfrac{1}{2}\int g(\dot\gamma, \dot\gamma)\,dt$, or equivalently critical points of the length functional $L(\gamma) = \int |\dot\gamma|\,dt$ (modulo reparametrisation). This is the **first variation formula**, and it links the connection-theoretic and variational pictures of "shortest path". The **second variation formula** then governs the local minimum vs. saddle-point structure of geodesics and is the input to the **Bonnet-Myers** and **Morse index** theorems. Full development in [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].
