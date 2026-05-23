---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Affine Connection on a Vector Bundle"
  - "Def - Riemannian Metric"
  - "Def - Metric-Compatible Connection"
  - "Def - Torsion Tensor"
  - "Def - Christoffel Symbols"
tags: [geometry, riemannian-geometry, connections]
---

# Notation

$(M, g)$ — a Riemannian (or semi-Riemannian) manifold. $\nabla$ or $\nabla^g$ — the Levi-Civita connection of $g$. $\Gamma^k_{ij}$ — its Christoffel symbols in a coordinate frame. $X, Y, Z$ — smooth vector fields. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Axiom Motivation

A generic affine connection on $TM$ has two strictly independent local invariants — its **torsion** $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y]$ and its **curvature** $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$ — and the connection comes with no relation at all to a metric $g$, even if a metric is around. On a Riemannian manifold there are infinitely many distinct connections on $TM$ (the space of connections is affine, modelled on $\Gamma(T^*M \otimes \mathrm{End}\,TM)$), and choosing one is *not* canonical from the connection axioms alone.

The Levi-Civita connection is the canonical choice forced by two additional structural conditions:

**Torsion-freeness:** $T \equiv 0$, equivalently $\nabla_X Y - \nabla_Y X = [X, Y]$, equivalently $\Gamma^k_{ij}$ is symmetric in $(i, j)$ in any coordinate frame. Geometrically, infinitesimal parallelograms close (see [[Def - Torsion Tensor]]). This is a structural / symmetry condition unrelated to the metric.

**Metric-compatibility:** $\nabla g = 0$, equivalently $Xg(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$, equivalently parallel transport is a linear isometry of tangent spaces (see [[Def - Metric-Compatible Connection]]). Geometrically, the connection respects the metric — lengths and angles are conserved under parallel transport. This is the condition that ties $\nabla$ to $g$.

The remarkable structural fact — content of the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem of Riemannian geometry]] — is that **these two conditions together uniquely determine $\nabla$ from $g$**. Neither alone suffices: there are torsion-free non-compatible connections (e.g., the flat connection on $\mathbb{R}^n$ with a non-Euclidean metric), and there are compatible non-torsion-free connections (e.g., Cartan-Schouten connections on Lie groups). The conjunction selects exactly one, and that one is the **Levi-Civita connection** $\nabla^g$.

**Why these two conditions?** The answer is a combination of geometric naturalness and algebraic miracle.

The geometric naturalness: each condition has a clean independent meaning. Torsion-freeness says "the connection is symmetric" — it does not introduce a preferred direction of rotation in infinitesimal parallelograms. Metric-compatibility says "the connection respects the metric" — it does not change inner products under parallel transport. Both are minimal symmetry conditions that one would impose without thinking, given a metric and the desire for a canonical connection.

The algebraic miracle: the two conditions together are *just enough* to determine $\nabla$. A smaller condition (e.g., torsion-free alone) is underdetermined — the difference of any two torsion-free connections is a symmetric tensor field, still a large affine space of solutions. A larger condition (e.g., torsion-free + metric-compatible + "second covariant derivatives commute on functions") would be inconsistent — curvature is genuinely there, and demanding it vanish forces flatness, which is a global topological constraint. The pair (torsion-free, metric-compatible) hits the sweet spot. The mechanical proof of uniqueness is the Koszul-formula derivation: cycle the metric-compatibility identity over $(X, Y, Z)$, add with appropriate signs, use torsion-freeness to convert the antisymmetric $\nabla$ differences into Lie brackets, and read off $2g(\nabla_X Y, Z)$ as an explicit expression in $g$ and Lie brackets. The factor of $2$ and the explicit closed form are the algebraic miracle — they say the conditions overdetermine the connection by exactly the right amount.

**Why is the Levi-Civita connection the "natural" one to choose?** Two reasons. Operationally: it gives the geodesic equation that matches the variational characterisation of "shortest path" — geodesics of $\nabla^g$ are critical points of the energy functional $E(\gamma) = \tfrac{1}{2}\int g(\dot\gamma, \dot\gamma)\,dt$, equivalently locally length-minimising curves modulo reparametrisation. Without metric-compatibility, geodesics of $\nabla$ have no length-minimising interpretation; without torsion-freeness, the first variation formula has extra torsion terms that spoil the variational picture. Structurally: it is the connection that makes the orthonormal frame bundle into a principal $O(n)$-bundle with a canonical connection — and this is the bridge to all of gauge theory on the tangent bundle.

**What about generalisations?** On a vector bundle other than $TM$, "torsion" does not make sense (it requires the special role of the tangent bundle, where the bundle equals the base's tangent bundle and the Lie bracket is available). So on a general vector bundle, the analogue of "Levi-Civita" is just a metric-compatible connection — which is not unique (the difference of two compatible connections is a skew tensor field). The uniqueness of the Levi-Civita connection is special to the tangent bundle; for general vector bundles one chooses a metric-compatible connection, and the choice is part of the data. This is the situation in gauge theory: a connection on a $G$-bundle is *not* uniquely determined by a $G$-invariant metric on the fibres.

---

# The Definition

Let $(M, g)$ be a Riemannian (or semi-Riemannian) manifold. The **Levi-Civita connection** of $g$ is the unique affine connection $\nabla = \nabla^g$ on $TM$ that is both:

1. **Torsion-free:** $\nabla_X Y - \nabla_Y X = [X, Y]$ for all $X, Y \in \mathfrak{X}(M)$ (see [[Def - Torsion Tensor]]).

2. **Metric-compatible:** $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ for all $X, Y, Z \in \mathfrak{X}(M)$ (see [[Def - Metric-Compatible Connection]]).

Existence and uniqueness are the content of the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem of Riemannian geometry]], proved via the [[Thm - Koszul Formula|Koszul formula]]:
$$
2g(\nabla_X Y, Z) = X g(Y, Z) + Y g(X, Z) - Z g(X, Y) + g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X).
$$

**In local coordinates,** the Levi-Civita Christoffel symbols are given by the **Christoffel formula**:
$$
\Gamma^k_{ij} = \tfrac{1}{2}\,g^{kl}\bigl(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}\bigr).
$$
This formula is symmetric in the lower indices $(i, j)$ — the torsion-free condition — and is derived from the Koszul formula by setting $X = \partial_i$, $Y = \partial_j$, $Z = \partial_l$ and using $[\partial_i, \partial_j] = 0$.

**Action on vector fields.** For $X = X^i\partial_i$, $Y = Y^j\partial_j$:
$$
(\nabla_X Y)^k = X^i\,\partial_i Y^k + \Gamma^k_{ij}\,X^i Y^j.
$$

**Action on covector fields and tensor fields.** By the [[Def - Induced Connection on Tensor Bundles|induced-connection rule]], $\nabla$ extends to all tensor bundles. For a 1-form $\alpha = \alpha_i\,dx^i$:
$$
(\nabla_X \alpha)_k = X^i\,\partial_i \alpha_k - \Gamma^j_{ik}\,X^i\,\alpha_j.
$$
For a $(0, 2)$-tensor $T = T_{ij}\,dx^i \otimes dx^j$:
$$
(\nabla_X T)_{kl} = X^i\,\partial_i T_{kl} - \Gamma^j_{ik}\,X^i\,T_{jl} - \Gamma^j_{il}\,X^i\,T_{kj}.
$$
Metric-compatibility takes the clean form $\nabla g = 0$, which in components is $\nabla_X g_{ij} = \partial_i g_{ij} - \Gamma^l_{ki}g_{lj} - \Gamma^l_{kj}g_{il} = 0$ — the **Ricci identity** for the metric, and the integrability condition that gives the Christoffel formula.

---

# Categorical / Structural Definition

The Levi-Civita connection has a clean categorical description as **the principal connection on the orthonormal frame bundle determined by the soldering form**.

Let $(M, g)$ be a Riemannian $n$-manifold. The **orthonormal frame bundle** $O(M, g) \to M$ is the principal $O(n)$-bundle whose fibre at $p$ consists of all orthonormal bases of $(T_pM, g_p)$. The **soldering form** $\theta$ on $O(M, g)$ is the canonical $\mathbb{R}^n$-valued 1-form that identifies $TM$ with $O(M, g) \times_{O(n)} \mathbb{R}^n$. A principal connection on $O(M, g)$ is an $\mathfrak{o}(n)$-valued 1-form $\omega$ on the total space, $O(n)$-equivariant and reducing to the Maurer-Cartan form on fibres.

The **Levi-Civita connection** is the unique principal connection on $O(M, g)$ whose torsion 2-form, defined by Cartan's first structural equation $d\theta + \omega \wedge \theta = \tau$, vanishes: $\tau \equiv 0$. The corresponding vector-bundle connection on $TM = O(M, g) \times_{O(n)} \mathbb{R}^n$ is the standard Levi-Civita connection.

This formulation has two virtues. First, it makes manifest the reduction of structure group from $\mathrm{GL}(n)$ (generic frame bundle) to $O(n)$ (orthonormal frame bundle): the principal connection naturally takes values in $\mathfrak{o}(n)$, the skew-symmetric matrices, which is exactly the antisymmetry $\omega^a{}_b + \omega^b{}_a = 0$ of the orthonormal-frame connection 1-forms. Second, it generalises straightforwardly: replace $O(n)$ by a Lie subgroup $H \subseteq O(n)$ (e.g., $U(n)$ for Kähler manifolds, $G_2$ for $G_2$-manifolds), and the analogous reduction selects a special connection compatible with the additional structure. This is the conceptual foundation of **special holonomy** in Riemannian geometry.

---

# Relate to Other Fields / Compression

The compression: **the Levi-Civita connection is the unique torsion-free metric-compatible connection on $(M, g)$ — and its Christoffel symbols are $\tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$.** It is the connection of choice for Riemannian and Lorentzian geometry, the connection that makes geodesics into length-minimising curves and parallel transport into an isometry.

In **general relativity**, the Levi-Civita connection of the Lorentzian spacetime metric $g_{\mu\nu}$ is the **gravitational connection**. Its Christoffel symbols $\Gamma^\lambda_{\mu\nu}$ play the role of "gravitational field components" — the geodesic equation $\ddot x^\lambda + \Gamma^\lambda_{\mu\nu}\dot x^\mu \dot x^\nu = 0$ is Newton's second law for a freely falling particle, with the right-hand side absent (no force) and the Christoffel correction encoding the gravitational attraction. The Riemann tensor of the Levi-Civita connection enters the Einstein field equations $R_{\mu\nu} - \tfrac{1}{2}R\,g_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ — the **Einstein equations** that determine the metric from the matter distribution.

In **gauge theory**, the Levi-Civita connection on $TM$ is the principal connection on the orthonormal frame bundle $O(M, g)$ with structure group $O(n)$, satisfying the *additional* torsion-free condition. For a general principal $G$-bundle the structure group $G$ does not have a "torsion" intrinsic to it; torsion is a feature specific to the tangent bundle via the soldering form. So the uniqueness of the Levi-Civita connection — the algebraic miracle of "exactly two conditions = exactly one connection" — is special to the tangent bundle setting and does not generalise to arbitrary principal bundles.

**True name:** The "true name" of the Levi-Civita connection is **the unique connection for which parallel transport is an isometry and infinitesimal parallelograms close**. The two formal conditions (torsion-free, metric-compatible) have these clean geometric meanings, and once they are understood, the entire abstract machinery of the Christoffel formula and the Koszul formula becomes "the computational consequence of these two demands".

---

# Examples / Corollaries

**Example: the Levi-Civita connection on Euclidean $\mathbb{R}^n$.** In Cartesian coordinates the metric is $g_{ij} = \delta_{ij}$ (constant), so all partial derivatives $\partial_k g_{ij} = 0$, and the Christoffel formula gives $\Gamma^k_{ij} \equiv 0$. The Levi-Civita connection is just the flat connection — the directional derivative.

**Example: the Levi-Civita connection on $S^2$.** The round metric is $g = d\theta^2 + \sin^2\theta\,d\varphi^2$, with components $g_{\theta\theta} = 1$, $g_{\varphi\varphi} = \sin^2\theta$. The Christoffel formula gives $\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta$, $\Gamma^\varphi_{\theta\varphi} = \Gamma^\varphi_{\varphi\theta} = \cot\theta$, all others zero. See [[Ex - Christoffel Symbols of the Round Metric on the Sphere]].

**Example: the Levi-Civita connection on the hyperbolic plane.** Upper-half-plane metric $g = (dx^2 + dy^2)/y^2$, with $g_{xx} = g_{yy} = 1/y^2$. The Christoffel formula gives $\Gamma^x_{xy} = \Gamma^x_{yx} = -1/y$, $\Gamma^y_{xx} = 1/y$, $\Gamma^y_{yy} = -1/y$. See [[Ex - Christoffel Symbols of the Hyperbolic Plane]].

**Example: the Levi-Civita connection on a Lie group with bi-invariant metric.** For a Lie group $G$ with a bi-invariant Riemannian metric (necessarily $\mathrm{Ad}$-invariant, possible iff $G$ is compact or abelian), the Levi-Civita connection on left-invariant vector fields takes the elegant form
$$
\nabla_X Y = \tfrac{1}{2}[X, Y].
$$
This follows from the Koszul formula plus the fact that left-invariant fields are constant under the metric ($X g(Y, Z) = 0$ for left-invariant $X, Y, Z$). The geodesics through the identity are the one-parameter subgroups $\exp(tX)$, and the Riemannian exponential map equals the Lie-group exponential of [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]].

**Example: the Levi-Civita connection on a submanifold.** If $S \hookrightarrow M$ is an embedded submanifold of a Riemannian manifold $(M, g)$ with induced metric $\iota^* g$, the Levi-Civita connection on $S$ is the **tangential projection** of $\nabla^M$:
$$
\nabla^S_X Y = (\nabla^M_X Y)^\top,
$$
where $(\cdot)^\top$ denotes orthogonal projection onto $T_p S \subseteq T_p M$. The normal part is the **second fundamental form** $II(X, Y) = (\nabla^M_X Y)^\perp$. This is the **Gauss formula**, and it makes the abstract Levi-Civita connection concrete: for a submanifold of $\mathbb{R}^N$, $\nabla^M$ is just the componentwise derivative, and $\nabla^S_X Y$ is its tangential projection. This is the original Levi-Civita construction (1917) and is the route used in [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

**Non-example: the Weitzenböck connection on a Lie group.** On a Lie group, declaring all left-invariant fields parallel gives the Weitzenböck connection — which is flat (curvature zero) but has torsion $T(X, Y) = -[X, Y]$ on left-invariant fields. This is not the Levi-Civita connection of any bi-invariant metric (the Levi-Civita has $\nabla_X Y = \tfrac{1}{2}[X, Y]$ and is *not* flat in general).

**Non-example: the flat connection on $\mathbb{R}^2$ with the non-Euclidean metric $g = e^{2x}(dx^2 + dy^2)$.** The flat connection (all $\Gamma = 0$) is torsion-free but *not* metric-compatible with this rescaled metric — so it is not the Levi-Civita connection of $g$. The Levi-Civita connection of $g$ has nonzero Christoffel symbols computed from the Christoffel formula.

**Corollary (uniqueness of the geodesic equation).** The geodesics of the Levi-Civita connection of $(M, g)$ are the unique unparametrised curves whose velocity is parallel along themselves: $\nabla^g_{\dot\gamma}\dot\gamma = 0$. In coordinates: $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$. By the existence-uniqueness theorem for second-order ODEs, given any $p \in M$ and $v \in T_pM$, there is a unique geodesic $\gamma_v$ with $\gamma_v(0) = p$, $\dot\gamma_v(0) = v$, defined on a maximal interval.

**Corollary (the variational characterisation of geodesics).** Geodesics of the Levi-Civita connection are critical points of the energy functional $E(\gamma) = \tfrac{1}{2}\int g(\dot\gamma, \dot\gamma)\,dt$ over smooth curves with fixed endpoints. They are also extrema of the length functional $L(\gamma) = \int |\dot\gamma|\,dt$, modulo reparametrisation. This is the **first variation formula**, and it works *only* for the Levi-Civita connection — for a non-metric-compatible or non-torsion-free connection, the geodesics are *not* the extrema of these functionals.

**Corollary (Killing fields and Killing's equation).** A vector field $K$ is a **Killing field** (the infinitesimal generator of a flow of isometries) if and only if $\mathcal{L}_K g = 0$. In terms of the Levi-Civita connection this is **Killing's equation** $\nabla_i K_j + \nabla_j K_i = 0$, where $K_i = g_{ij}K^j$. Killing fields give conserved quantities along geodesics: $g(\dot\gamma, K)$ is constant for any geodesic $\gamma$. This is the geometric basis of Noether's theorem for spacetime symmetries.

**Calibration check.** If you can perform the following four computations, you have understood the Levi-Civita connection. (i) Compute the Christoffel symbols of the round 2-sphere via the Christoffel formula and verify the great-circle geodesic equation. (ii) Show that the Levi-Civita connection on a Lie group with bi-invariant metric satisfies $\nabla_X Y = \tfrac{1}{2}[X, Y]$ on left-invariant fields, by applying the Koszul formula. (iii) Verify that the Levi-Civita Christoffel formula is manifestly symmetric in $(i, j)$, so the connection is torsion-free. (iv) Verify that the Christoffel formula satisfies the metric-compatibility condition $\partial_k g_{ij} - \Gamma_{kij} - \Gamma_{kji} = 0$ by direct substitution.

---

# Unlocked by This

> [!tip] The Geodesic Equation, Exponential Map, and Variational Theory *(from Riemannian Geometry)*
> The Levi-Civita connection delivers the **geodesic equation** $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$, the **exponential map** $\exp_p : T_pM \to M$ that sends $v$ to $\gamma_v(1)$, **normal coordinates** around any point (in which $g_{ij}(p) = \delta_{ij}$ and $\Gamma^k_{ij}(p) = 0$), and the **first and second variation formulas** for arc length. The full theory — Jacobi fields, conjugate points, the Morse index theorem, Hopf-Rinow completeness — is the content of [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

> [!tip] The Riemann Curvature Tensor and Curvature-to-Topology Theorems *(from Riemannian Geometry)*
> Curvature is defined via the Levi-Civita connection: $R(X, Y)Z := \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$. The **sectional curvature**, **Ricci tensor**, and **scalar curvature** are contractions of $R$, and the major curvature-to-topology theorems — **Bonnet-Myers** (positive Ricci implies compact, diameter bounded), **Cartan-Hadamard** (nonpositive sectional curvature implies universal cover diffeomorphic to $\mathbb{R}^n$), **Synge** (positive sectional curvature on even-dimensional orientable manifolds implies simply connected), **Gauss-Bonnet** for surfaces — all use the Levi-Civita connection essentially. The full theory is the content of [[Riemannian Geometry III — Riemann Curvature and Topology]].

> [!tip] Einstein's Field Equations *(from General Relativity)*
> In general relativity, the Levi-Civita connection of the Lorentzian spacetime metric is the gravitational connection, and the **Ricci tensor** $R_{\mu\nu}$ of this connection appears in the **Einstein field equations** $R_{\mu\nu} - \tfrac{1}{2}R\,g_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\,T_{\mu\nu}$. The contracted **second Bianchi identity** $\nabla_\mu(R^{\mu\nu} - \tfrac{1}{2}R\,g^{\mu\nu}) = 0$ — a consequence of metric-compatibility plus the structure of the curvature tensor — gives the **conservation law** $\nabla_\mu T^{\mu\nu} = 0$ for the matter energy-momentum, automatically. The full theory is in [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] Special Holonomy and Berger's Classification *(from Riemannian Geometry)*
> The holonomy group of the Levi-Civita connection of an irreducible simply-connected complete Riemannian manifold is one of the entries on Berger's list: $\mathrm{SO}(n)$ (generic), $U(n)$ (Kähler), $SU(n)$ (Calabi-Yau), $\mathrm{Sp}(n)$ (hyperkähler), $\mathrm{Sp}(n)\mathrm{Sp}(1)$ (quaternion-Kähler), $G_2$, $\mathrm{Spin}(7)$. Each special holonomy corresponds to a reduction of the orthonormal frame bundle's structure group and to additional parallel tensor fields on the manifold (e.g., the Kähler form for $U(n)$, a holomorphic volume form for $SU(n)$). These have profound connections to algebraic geometry, mirror symmetry, and string compactifications.
