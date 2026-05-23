---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - The Tangent Space"
  - "Def - The Differential of a Smooth Map"
  - "Def - Coordinate Tangent Vectors"
tags: [geometry, differential-geometry]
---

# Notation

A **smooth curve** in a manifold $M$ is a smooth map $\gamma : J \to M$ where $J \subseteq \mathbb{R}$ is an interval. We will primarily consider $J$ open and $t_{0}$ an interior point of $J$, with occasional boundary-point variants. The tangent space to $\mathbb{R}$ at any $t_{0}$ is 1-dimensional and has a canonical basis vector $d/dt|_{t_{0}}$ (rather than $\partial/\partial t|_{t_{0}}$, since the manifold is 1-dimensional). The full notation registry is on [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# Axiom Motivation

The motivation is immediate: a smooth curve $\gamma : J \to M$ traces out a path on the manifold, and at each instant $t_{0}$ it has an instantaneous **velocity** — a tangent vector at $\gamma(t_{0})$. The construction has to specify what this velocity is, formally, in terms of the chart/derivation machinery already in place.

The cleanest definition routes through the differential. The interval $J \subseteq \mathbb{R}$ is itself a 1-manifold; the tangent space $T_{t_{0}}\mathbb{R}$ is one-dimensional with canonical basis $d/dt|_{t_{0}}$ (the standard derivative operator at $t_{0}$). The curve $\gamma$ is a smooth map $J \to M$, so it has a differential $d\gamma_{t_{0}} : T_{t_{0}}\mathbb{R} \to T_{\gamma(t_{0})}M$. The velocity of $\gamma$ at $t_{0}$ is then *the image of the canonical basis vector under the differential*:
$$\gamma'(t_{0}) := d\gamma_{t_{0}}\left(\left.\frac{d}{dt}\right|_{t_{0}}\right).$$
This makes velocity a tangent vector to $M$ at $\gamma(t_{0})$ — exactly what we want. It is canonically defined (no chart needed in the formula) and uses only the differential machinery already developed.

Unwinding the definition: for $f \in C^{\infty}(M)$, the derivation $\gamma'(t_{0})$ acts by
$$\gamma'(t_{0})(f) = \left.\frac{d}{dt}\right|_{t_{0}} (f \circ \gamma) = (f \circ \gamma)'(t_{0}).$$
So $\gamma'(t_{0})$ is the derivation "rate of change of $f$ along $\gamma$ at time $t_{0}$". This matches the intuition that velocity tells you how fast functions change as you move along the curve.

Why is this the right definition? Because it satisfies three desiderata. (a) It reduces to the standard Euclidean velocity when $M = \mathbb{R}^{n}$: $\gamma'(t_{0})$ as a vector in $\mathbb{R}^{n}$ has components $(d\gamma^{i}/dt)(t_{0})$, the standard component-wise derivatives. (b) It is functorial in $\gamma$: a smooth map $F : M \to N$ pushes velocities forward correctly, $(F \circ \gamma)'(t_{0}) = dF_{\gamma(t_{0})}(\gamma'(t_{0}))$ — this is Lee's Proposition 3.24 and is a consequence of the chain rule applied to $d(F \circ \gamma)$. (c) Every tangent vector at every point arises as the velocity of *some* smooth curve — Lee's Proposition 3.23 — which makes velocity the surjective bridge between abstract tangent vectors and concrete curve-based intuition.

The definition is also independent of any chart. In a chart with coordinates $x^{i}$, the velocity is computed as the chart-components-rate-of-change:
$$\gamma'(t_{0}) = \frac{d\gamma^{i}}{dt}(t_{0})\,\left.\frac{\partial}{\partial x^{i}}\right|_{\gamma(t_{0})},$$
where $\hat\gamma(t) = (\gamma^{1}(t), \dots, \gamma^{n}(t))$ is the coordinate representative. So in a chart, "the velocity is the derivative of the coordinate components" — the formula you would use if you naively defined velocity in coordinates without abstract machinery. The abstract definition is what makes this formula chart-independent.

A reader could invent the definition as follows. Want to define "velocity of a curve at $t_{0}$" as a tangent vector at $\gamma(t_{0})$. Notice that $\gamma$ is a smooth map and the source $\mathbb{R}$ has a canonical tangent vector $d/dt|_{t_{0}}$ at every point. Push the canonical tangent vector forward through the differential. Done. The construction uses no chart and no calculation beyond the definition of the differential.

---

# The Definition

Let $M$ be a smooth manifold and $\gamma : J \to M$ a smooth curve, where $J \subseteq \mathbb{R}$ is an interval. For $t_{0} \in J$ (interior — or at an endpoint with the obvious one-sided modifications), the **velocity** of $\gamma$ at $t_{0}$ is the tangent vector
$$\gamma'(t_{0}) \;=\; d\gamma_{t_{0}}\left(\left.\frac{d}{dt}\right|_{t_{0}}\right) \;\in\; T_{\gamma(t_{0})}M,$$
where $d/dt|_{t_{0}} \in T_{t_{0}}\mathbb{R}$ is the canonical basis vector and $d\gamma_{t_{0}} : T_{t_{0}}\mathbb{R} \to T_{\gamma(t_{0})}M$ is the [[Def - The Differential of a Smooth Map|differential]] of $\gamma$ at $t_{0}$.

Equivalently, $\gamma'(t_{0})$ is the derivation at $\gamma(t_{0})$ defined by
$$\gamma'(t_{0})(f) \;=\; (f \circ \gamma)'(t_{0}) \quad \text{for } f \in C^{\infty}(M).$$

**Coordinate expression.** In a chart $(U, \varphi)$ around $\gamma(t_{0})$ with coordinates $x^{i}$, if $\hat\gamma = \varphi \circ \gamma = (\gamma^{1}, \dots, \gamma^{n})$, then
$$\gamma'(t_{0}) \;=\; \frac{d\gamma^{i}}{dt}(t_{0})\,\left.\frac{\partial}{\partial x^{i}}\right|_{\gamma(t_{0})}.$$
The components of $\gamma'(t_{0})$ in the coordinate basis are the derivatives of the coordinate component functions of $\gamma$.

**Common alternative notations.** $\dot\gamma(t_{0})$, $\frac{d\gamma}{dt}(t_{0})$, $\frac{d\gamma}{dt}\big|_{t = t_{0}}$. We standardize on $\gamma'(t_{0})$.

**Three foundational properties** (proved in [[Thm - Equivalence of Tangent Vector Definitions]] and surrounding propositions):

1. **Surjectivity of velocity.** For every $v \in T_{p}M$ there exists a smooth curve $\gamma$ with $\gamma(0) = p$ and $\gamma'(0) = v$. Proof: in a chart, take $\gamma(t) = \varphi^{-1}(\varphi(p) + tv)$ where $v$ is identified with its coordinate components.

2. **Velocity of a composite curve (Lee Proposition 3.24).** For a smooth map $F : M \to N$ and smooth curve $\gamma : J \to M$,
$$(F \circ \gamma)'(t_{0}) = dF_{\gamma(t_{0})}(\gamma'(t_{0})).$$

3. **Computing the differential via a curve (Lee Corollary 3.25).** For any smooth map $F : M \to N$, point $p \in M$, and tangent vector $v \in T_{p}M$,
$$dF_{p}(v) = (F \circ \gamma)'(0)$$
for any smooth curve $\gamma$ with $\gamma(0) = p$ and $\gamma'(0) = v$.

The last is the workhorse for *computing* differentials and the practical reason to know the curve definition of tangent vectors.

---

# Relate to Other Fields / Compression

In **classical mechanics**, the velocity of a particle moving on the configuration manifold $Q$ is precisely the tangent vector $\gamma'(t)$ at the instantaneous position $\gamma(t)$. The pair $(\gamma(t), \gamma'(t))$ lives in the tangent bundle $TQ$, and the Lagrangian $L : TQ \to \mathbb{R}$ assigns a number to each (position, velocity) pair. The Euler–Lagrange equations are second-order ODEs governing $\gamma$. This is the natural setting for Lagrangian mechanics, and it is where the tangent bundle was first physically motivated — the configuration of a mechanical system and its velocity belong together in $TQ$.

In **special relativity**, the **four-velocity** of a worldline $\gamma : J \to M$ (with $M$ Minkowski space) is the tangent vector $\gamma'(\tau)$ at the event $\gamma(\tau)$, where $\tau$ is proper time. The fact that proper time is the right parameter — i.e., that the four-velocity normalized by proper time has Minkowski norm $-1$ — is a non-trivial physical input from the [[Def - Inertial Frame and the Postulates of Special Relativity|postulates of special relativity]]. See [[Def - Four-Vector]].

**True name:** The velocity $\gamma'(t_{0})$ is "the derivation that differentiates functions along $\gamma$ at time $t_{0}$" — operationally, $\gamma'(t_{0})(f) = (f \circ \gamma)'(t_{0})$. This is the curve-picture realization of a tangent vector and is what you reach for in concrete computations. The functoriality property $(F \circ \gamma)'(t_{0}) = dF(\gamma'(t_{0}))$ is then a direct application of the one-variable chain rule.

In **Lie theory**, the **one-parameter subgroup** generated by an element $X$ of the Lie algebra $\mathfrak{g}$ of a Lie group $G$ is a smooth curve $\gamma : \mathbb{R} \to G$ with $\gamma(0) = e$, $\gamma'(0) = X$, and the group property $\gamma(s + t) = \gamma(s)\gamma(t)$. So the velocity at the identity uniquely determines a curve through $G$. The exponential map $\exp : \mathfrak{g} \to G$ is $\exp(X) = \gamma_{X}(1)$, and the entire Lie correspondence rests on the velocity construction. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

---

# Examples / Corollaries

**Velocity of a straight line in $\mathbb{R}^{n}$.** For $\gamma(t) = a + tv$, the coordinate components are $\gamma^{i}(t) = a^{i} + tv^{i}$, so $(d\gamma^{i}/dt)(t_{0}) = v^{i}$ for any $t_{0}$. Hence $\gamma'(t_{0}) = v^{i}\,\partial/\partial x^{i}|_{a + t_{0}v}$ — geometrically, $\gamma$ has constant velocity $v$ at every point of its trace, with $v$ identified with a tangent vector at the current position.

**Velocity of a coordinate curve.** Given a chart $(U, \varphi)$ with coordinates $x^{i}$ and a point $p \in U$, the $i$-th coordinate curve is $\gamma_{i}(t) = \varphi^{-1}(\varphi(p) + t\,e_{i})$. Its coordinate components are $\gamma_{i}^{j}(t) = \varphi^{j}(p) + t\,\delta^{j}_{i}$, so $(d\gamma_{i}^{j}/dt)(0) = \delta^{j}_{i}$ and $\gamma_{i}'(0) = \delta^{j}_{i}\,\partial/\partial x^{j}|_{p} = \partial/\partial x^{i}|_{p}$. So the coordinate tangent vector is the velocity of the corresponding coordinate curve. See [[Ex - Tangent Vectors as Velocities of Coordinate Curves]].

**Velocity of a circle in $\mathbb{R}^{2}$.** The curve $\gamma(t) = (\cos t, \sin t)$ traces the unit circle. Its velocity is $\gamma'(t) = -\sin t\,\partial/\partial x|_{\gamma(t)} + \cos t\,\partial/\partial y|_{\gamma(t)}$. At $t = 0$, $\gamma(0) = (1, 0)$ and $\gamma'(0) = \partial/\partial y|_{(1,0)}$ — the upward tangent to the circle.

**Velocity of a curve in $\mathrm{GL}(n)$ at the identity.** Take $\gamma(t) = I + tH$ for a matrix $H \in M_{n}(\mathbb{R})$. The coordinate components in $M_{n}(\mathbb{R})$ are $\gamma^{ij}(t) = \delta^{ij} + tH^{ij}$, so $(d\gamma^{ij}/dt)(0) = H^{ij}$, and $\gamma'(0) = H$ (identified with the corresponding element of $T_{I}\mathrm{GL}(n) \cong M_{n}(\mathbb{R})$). This is how matrices appear as tangent vectors at the identity of $\mathrm{GL}(n)$.

**Velocity of a 1-parameter family of rotations.** Let $R_{t} = e^{tA}$ for a skew-symmetric matrix $A$. The curve $\gamma : \mathbb{R} \to \mathrm{SO}(n)$, $t \mapsto R_{t}$ satisfies $\gamma(0) = I$. By the matrix-exponential expansion, $\gamma'(0) = A$. So the Lie algebra $\mathfrak{so}(n)$ consists of skew-symmetric matrices, identified with velocities of curves of rotations through the identity.

**Is NOT a tangent vector to $M$: $(d\gamma/dt)(t_{0})$ when $\gamma$ is a curve in $\mathbb{R}^{N}$ ambient to $M$ but $M$ is the level set of a function and the velocity is not in the kernel.** If $M = \{f = c\}$ and $\gamma : J \to \mathbb{R}^{N}$ is a curve with $\gamma(t) \in M$ for all $t$ but $\gamma(t_{0}) \in M$ only by chance, then $\gamma$ is not a curve *in* $M$ — it is a curve in $\mathbb{R}^{N}$ that happens to touch $M$. Its velocity at $t_{0}$ might not be tangent to $M$. The constraint that $\gamma$ lies *entirely* in $M$ (not just at one instant) is essential for the velocity to be a tangent vector to $M$. This is the operational content of "tangent vectors to a level set are killed by $df$": only curves staying in the level set produce velocities in $\ker df$.

**Corollary — every tangent vector is a velocity.** For any $v \in T_{p}M$, there is a smooth curve $\gamma : (-\varepsilon, \varepsilon) \to M$ with $\gamma(0) = p$ and $\gamma'(0) = v$. *Proof:* pick a chart $(U, \varphi)$ around $p$ and write $v = v^{i}\,\partial/\partial x^{i}|_{p}$ with components $v^{i}$. Define $\gamma(t) = \varphi^{-1}(\varphi(p) + tv)$ for $|t|$ small. Then $\gamma(0) = p$ and by the coordinate formula above, $\gamma'(0) = v^{i}\,\partial/\partial x^{i}|_{p} = v$. So the velocity construction is surjective onto $T_{p}M$. This is Lee's Proposition 3.23.

**Corollary — chain rule for velocities.** For a smooth map $F : M \to N$ and smooth curve $\gamma$ in $M$,
$$(F \circ \gamma)'(t_{0}) = dF_{\gamma(t_{0})}(\gamma'(t_{0})).$$
This is Lee's Proposition 3.24 and is a one-line application of the chain rule for differentials applied to the composition $F \circ \gamma$: $d(F \circ \gamma)_{t_{0}} = dF_{\gamma(t_{0})} \circ d\gamma_{t_{0}}$, so applying both sides to $d/dt|_{t_{0}}$ gives the equation. The corollary is the operational basis for [[Ex - Computing the Differential in Local Coordinates|computing dF via curves]].

**Calibration check.** Verify that the constant curve $\gamma(t) \equiv p$ has velocity $\gamma'(t) = 0 \in T_{p}M$ for every $t$. Verify that $\gamma(t) = (t^{2}, t)$ on $\mathbb{R}^{2}$ has velocity $\gamma'(0) = \partial/\partial y|_{(0,0)}$ (since $\gamma^{1\prime}(0) = 0$ and $\gamma^{2\prime}(0) = 1$). Verify that for $\gamma(t) = (\cos t, \sin t, t)$ on a cylinder $S^{1} \times \mathbb{R}$, the velocity at $t = 0$ is $\partial/\partial y|_{(1,0,0)} + \partial/\partial z|_{(1,0,0)}$. If you can also explain why the formula $\gamma'(t_{0}) = (d\gamma^{i}/dt)(t_{0})\,\partial/\partial x^{i}|_{\gamma(t_{0})}$ is chart-independent (i.e., why two different charts produce the same vector), you have understood the abstract definition.

---

# Unlocked by This

> [!tip] Integral Curves of a Vector Field *(from Differential Geometry)*
> An **integral curve** of a vector field $X$ on $M$ is a smooth curve $\gamma$ satisfying the ODE $\gamma'(t) = X_{\gamma(t)}$: the velocity of $\gamma$ at $t$ equals the value of $X$ at $\gamma(t)$. Local existence and uniqueness (via the multivariate ODE theorem) gives a **flow** of $X$. This is the foundational content of dynamical systems on manifolds. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]].

> [!tip] Geodesic *(from Riemannian Geometry)*
> On a [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds|Riemannian manifold]] $(M, g)$, a **geodesic** is a smooth curve whose velocity is parallel-transported along itself: $\nabla_{\gamma'}\gamma' = 0$. Equivalently, the geodesic equation $\ddot\gamma^{k} + \Gamma^{k}_{ij}\,\dot\gamma^{i}\dot\gamma^{j} = 0$ governs the local coordinate components. Geodesics are the analogue of straight lines on a curved manifold and are the trajectories of free particles in general relativity.

> [!tip] One-Parameter Subgroup *(from Lie Theory)*
> A **one-parameter subgroup** of a Lie group $G$ is a smooth group homomorphism $\gamma : \mathbb{R} \to G$. The velocity $\gamma'(0)$ uniquely determines $\gamma$, and the map $X \mapsto \gamma_{X}$ from the Lie algebra $\mathfrak{g} = T_{e}G$ to one-parameter subgroups is a bijection. This is the cornerstone of the relationship between Lie groups and Lie algebras. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

> [!tip] Four-Velocity in General Relativity *(from GR)*
> In **general relativity**, the worldline of a massive particle is a smooth curve $\gamma : J \to M$ in spacetime, parameterized by proper time so that $g(\gamma', \gamma') = -1$ (timelike normalization). The four-velocity $\gamma'(\tau)$ is a tangent vector at $\gamma(\tau)$ on which the spacetime metric acts to produce the proper-time interval. The geodesic equation $\nabla_{\gamma'}\gamma' = 0$ is then the equation of motion for a free-falling particle.
