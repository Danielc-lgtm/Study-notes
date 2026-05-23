---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Volume Form"
  - "Def - Riemannian Metric"
  - "Def - Differential k-Form on a Manifold"
tags: [geometry, differential-geometry, riemannian, volume-form, integration]
---

# Notation

Throughout, $(M, g)$ is an oriented Riemannian $n$-manifold ($n \geq 1$), possibly with boundary. The Riemannian metric $g$ assigns to each $p \in M$ a positive-definite symmetric bilinear form $g_p$ on $T_pM$ (see [[Def - Riemannian Metric]]). In a coordinate chart, the components of $g$ are $g_{ij} = g(\partial_i, \partial_j)$, an $n \times n$ symmetric positive-definite matrix at each point. $\det(g_{ij})$ is its determinant, always positive by positive-definiteness. An **oriented orthonormal frame** is a tuple of vector fields $(E_1, \ldots, E_n)$ on an open set $U \subseteq M$ with $g(E_i, E_j) = \delta_{ij}$ and $(E_1|_p, \ldots, E_n|_p)$ positively oriented for every $p \in U$. The dual coframe is $(\varepsilon^1, \ldots, \varepsilon^n)$ with $\varepsilon^i(E_j) = \delta^i_j$. The full notation registry is at [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

---

# Axiom Motivation

A Riemannian metric gives every tangent space an *inner product*, and inner products give every parallelepiped an unsigned volume — the determinant of the Gram matrix of its edges, square-rooted. With orientation in hand, this unsigned volume becomes signed, and the signed-volume measurer is a top-form. The Riemannian volume form is the *canonical* top-form forced by the metric and the orientation.

Here is the construction in three layers.

**Layer 1: orthonormal frames have unit volume.** At each $p \in M$, the oriented Riemannian inner product on $T_pM$ singles out a class of "preferred" bases — the *oriented orthonormal* ones. By analogy with $\mathbb{R}^n$, the volume of the unit cube (spanned by an orthonormal frame) should be $1$. So we *demand* that the volume form $\omega_g$ at $p$ satisfy
$$\omega_g(E_1, \ldots, E_n) = 1$$
on every oriented orthonormal basis. This is a one-parameter family of top-covectors, except that the condition pins down the parameter: given the value on one basis, the value on every other basis is determined by the alternating-multilinear property. So at each point there is a *unique* such $\omega_g(p)$.

**Layer 2: the unique top-covector exists and is computable in any basis.** Given any basis $(E_1, \ldots, E_n)$ of $T_pM$ (not necessarily orthonormal), what is $\omega_g(E_1, \ldots, E_n)$? Let $(F_1, \ldots, F_n)$ be an oriented orthonormal basis. Then $E_i = a^j_iF_j$ for some matrix $A = (a^j_i)$. By the transformation rule of $n$-covectors, $\omega_g(E_1, \ldots, E_n) = \det A \cdot \omega_g(F_1, \ldots, F_n) = \det A$. And the Gram matrix of the $E_i$'s is $g(E_i, E_j) = a^k_i a^\ell_j g(F_k, F_\ell) = a^k_i a^\ell_j \delta_{k\ell} = \sum_k a^k_i a^k_j = (A^TA)_{ij}$, so $\det g_{ij} = \det(A^TA) = (\det A)^2$. Hence $|\omega_g(E_1, \ldots, E_n)| = \sqrt{\det g_{ij}}$, with sign positive iff the $E_i$ basis is positively oriented.

**Layer 3: in coordinates, $\omega_g = \sqrt{\det g_{ij}}\,dx^1\wedge\cdots\wedge dx^n$.** In an oriented coordinate chart, the coordinate frame $(\partial_1, \ldots, \partial_n)$ is positively oriented and has Gram matrix $g_{ij}$. By layer 2, $\omega_g(\partial_1, \ldots, \partial_n) = \sqrt{\det g_{ij}}$. So
$$\omega_g = \sqrt{\det g_{ij}}\,dx^1\wedge\cdots\wedge dx^n.$$
This is the famous formula. It expresses $\omega_g$ entirely in terms of metric components and coordinate differentials, and is the computable form.

**Why "Riemannian" rather than just "metric"?** The construction uses positive-definiteness in only one place: the determinant $\det g_{ij}$ must be positive, so $\sqrt{\det g_{ij}}$ is real. On a *semi-Riemannian* manifold (signature $(p, q)$, with $\det g_{ij}$ of sign $(-1)^q$), the formula needs an absolute value: $\omega_g = \sqrt{|\det g_{ij}|}\,dx^1\wedge\cdots\wedge dx^n$. This is the semi-Riemannian / Lorentzian volume form and is used on Minkowski space, in general relativity, and in [[#Examples / Corollaries|the Maxwell exercise of this topic]].

**Per-axiom failure analysis: what if we drop the orientation?** Without orientation, the formula $\sqrt{\det g_{ij}}\,dx^1\wedge\cdots\wedge dx^n$ depends on the chart (a chart with negative Jacobian would give the form with the opposite sign). Without orientation, only the *density* $|\omega_g|$ is canonical, not the form. See [[Def - Density on a Manifold]] for how to integrate on non-orientable Riemannian manifolds.

**What if we drop the orthonormality condition $\omega_g(E_1, \ldots, E_n) = 1$ on orthonormal frames?** We get a non-unique form. Any nonzero scalar multiple of $\omega_g$ would work as "a volume form compatible with the orientation"; the orthonormality condition fixes the scale to match Euclidean intuition.

**What if we instead use the volume form of *Lebesgue measure*?** In any single chart, $\sqrt{\det g_{ij}}\,dx^1\cdots dx^n$ *is* the Radon–Nikodým density of the Riemannian measure with respect to Lebesgue measure. So these are the same object, viewed from different sides: the Riemannian volume form on the form side, the Riemannian volume measure (or density) on the measure side. The bridge is the manifold integration definition.

---

# The Definition

Let $(M, g)$ be an oriented Riemannian manifold of [[Def - Dimension|dimension]] $n \geq 1$, possibly with boundary.

**Riemannian volume form.** The **Riemannian volume form** $\omega_g \in \Omega^n(M)$ is the unique positively-oriented smooth $n$-form on $M$ satisfying
$$\omega_g(E_1, \ldots, E_n) = 1$$
for every local oriented orthonormal frame $(E_1, \ldots, E_n)$.

**Coordinate formula.** In any oriented smooth chart $(U, \varphi)$ with coordinates $x^1, \ldots, x^n$ and metric components $g_{ij} = g(\partial_i, \partial_j)$,
$$\omega_g = \sqrt{\det(g_{ij})}\,dx^1\wedge\cdots\wedge dx^n.$$

**Equivalent formulation via dual coframe.** If $(E_1, \ldots, E_n)$ is an oriented orthonormal frame on $U$ with dual coframe $(\varepsilon^1, \ldots, \varepsilon^n)$, then
$$\omega_g = \varepsilon^1\wedge\cdots\wedge\varepsilon^n \qquad\text{on } U.$$

**Integration of functions.** For a compactly supported function $f \in C^\infty_c(M)$, define the **Riemannian integral**
$$\int_M f\,dV_g := \int_M f\omega_g.$$
The right-hand side is the integral of a compactly supported top-form, defined as in [[Def - Integral of a Compactly Supported Form on a Manifold]].

**Volume of a region.** For a compact subset $K \subseteq M$ (with measure-zero boundary), the **Riemannian volume**
$$\mathrm{vol}_g(K) := \int_K\omega_g \geq 0.$$
Always non-negative, since $\omega_g$ is positively oriented and the integration cone is well-behaved.

**Existence and uniqueness ([[Thm - Existence of the Riemannian Volume Form|theorem]]).** Every oriented Riemannian manifold has a unique Riemannian volume form, smooth, nowhere-vanishing.

**Semi-Riemannian generalization.** For a semi-Riemannian (e.g. Lorentzian) manifold of signature $(p, q)$ with $\det g_{ij}$ having sign $(-1)^q$ in some convention, the volume form is
$$\omega_g = \sqrt{|\det g_{ij}|}\,dx^1\wedge\cdots\wedge dx^n.$$
On Minkowski space $(\mathbb{R}^4, \eta)$ with $\eta = \mathrm{diag}(-1, 1, 1, 1)$, $|\det\eta| = 1$, so $\omega_\eta = dt\wedge dx\wedge dy\wedge dz$. This is used in the Maxwell exercise.

---

# Categorical / Structural Definition

The Riemannian volume form is the **canonical section of the orientation line bundle $\Lambda^n(T^*M)$ determined by the Riemannian metric and orientation**. More structurally: a Riemannian metric reduces the structure [[Def - Group|group]] of $TM$ from $\mathrm{GL}(n, \mathbb{R})$ to $\mathrm{O}(n)$; an orientation further reduces it to $\mathrm{SO}(n)$; and $\mathrm{SO}(n)$ has a canonical homomorphism $\det : \mathrm{SO}(n) \to \{1\}$ (the trivial map, since $\det = 1$ on $\mathrm{SO}(n)$). The associated bundle $\Lambda^n(T^*M)$ becomes the trivial line bundle, and the constant section $1$ corresponds to the Riemannian volume form.

In the **Hodge star** language: on an oriented Riemannian $n$-manifold, the Hodge star $\star : \Omega^k \to \Omega^{n-k}$ is defined by $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle_g\,\omega_g$. The volume form $\omega_g$ enters this formula as the "natural normalization" — it is the Hodge dual of the constant function $1$: $\omega_g = \star 1$.

**Conformal rescaling.** Under $g \mapsto \widetilde g = e^{2\phi}g$ for a smooth $\phi$, the metric components scale by $e^{2\phi}$, so $\det\widetilde g_{ij} = e^{2n\phi}\det g_{ij}$, and $\omega_{\widetilde g} = e^{n\phi}\omega_g$. This is the conformal scaling law of the volume form — the foundation of conformal geometry.

---

# Relate to Other Fields / Compression

The Riemannian volume form is the **bridge between geometry (metric + orientation) and analysis (integration of functions)** on a manifold. Without a metric, integration of functions is undefined. With a metric and an orientation, $\omega_g$ provides a canonical volume form, and "integrate $f$ over $M$" means "integrate $f\omega_g$" — recovering all the analytic machinery: $L^p$ spaces, Sobolev spaces, weak derivatives, the Laplace–Beltrami operator $\Delta_g$, the heat kernel, the spectral theorem.

In **classical mechanics on a Riemannian manifold**, $\omega_g$ is the natural measure on configuration space, and integrals like the kinetic energy functional $\int_M\tfrac{1}{2}|\dot q|_g^2\,\omega_g$ make sense. On a Lie group with a bi-invariant metric, $\omega_g$ is also (up to scale) the Haar volume form, unifying integration of functions on the group with the structure-group integration of representation theory.

In **information geometry**, the Fisher information metric on a statistical manifold $\{p_\theta\}$ produces a volume form $\omega_g$ that is invariant under reparametrization. The induced measure is **Jeffreys's prior** — the natural noninformative Bayesian prior, derived from the geometric structure of the parameter space.

**True name:** The Riemannian volume form is the unique positively-oriented top-form that assigns volume $1$ to every oriented orthonormal frame, or equivalently $\omega_g = \sqrt{\det g_{ij}}\,dx^1\wedge\cdots\wedge dx^n$ in oriented coordinates. This is the operational form; it is the *only* construction one needs in practice.

---

# Examples / Corollaries

**Is an instance — the Euclidean volume form on $\mathbb{R}^n$.** With the standard Euclidean metric ($g_{ij} = \delta_{ij}$, $\det g_{ij} = 1$), $\omega_g = dx^1\wedge\cdots\wedge dx^n$. The Riemannian integral of a function is the ordinary multiple Riemann integral.

**Is an instance — polar coordinates on $\mathbb{R}^2$.** In polar coordinates $(r, \theta)$, the Euclidean metric has components $g_{rr} = 1$, $g_{\theta\theta} = r^2$, $g_{r\theta} = 0$, so $\det g_{ij} = r^2$ and $\omega_g = r\,dr\wedge d\theta$. This is the familiar "extra factor of $r$" in $\int_0^{2\pi}\int_0^Rf(r,\theta)\,r\,dr\,d\theta$.

**Is an instance — the round metric on $S^n$.** In spherical coordinates $(\varphi_1, \ldots, \varphi_{n-1}, \theta)$ on $S^n$ (Hopf-style charts), the round metric gives $\omega_g = \sin^{n-1}\varphi_1\cdots\sin\varphi_{n-1}\,d\varphi_1\wedge\cdots\wedge d\varphi_{n-1}\wedge d\theta$. Integration gives the volume of $S^n$ in closed form: $\mathrm{vol}(S^n) = 2\pi^{(n+1)/2}/\Gamma\!\big(\tfrac{n+1}{2}\big)$. This is the exercise [[Ex - Volume of the n-Sphere via the Volume Form]].

**Is an instance — the Minkowski "volume" form $dt\wedge dx\wedge dy\wedge dz$.** Lorentzian metric $\eta = \mathrm{diag}(-1, 1, 1, 1)$, $|\det\eta| = 1$, $\omega_\eta = dt\wedge dx\wedge dy\wedge dz$. Used in relativistic field theory: integration of Lagrangian densities, Hodge star of forms (e.g. $\star F$ for the Faraday 2-form in Maxwell theory).

**Is an instance — the hyperbolic plane $\mathbb{H}^2$.** With metric $g = y^{-2}(dx^2 + dy^2)$ in the upper half-plane model, $g_{ij} = y^{-2}\delta_{ij}$, $\det g_{ij} = y^{-4}$, $\omega_g = y^{-2}\,dx\wedge dy$. The hyperbolic area is $\int_M y^{-2}\,dx\,dy$, infinite for the full $\mathbb{H}^2$ but useful for compact regions (e.g. the modular fundamental domain has hyperbolic area $\pi/3$).

**Is an instance — the Fubini–Study volume on $\mathbb{CP}^n$.** With the Fubini–Study Kähler metric, the volume form is $\omega^n_{FS}/n!$ where $\omega_{FS}$ is the Kähler 2-form. The total volume of $\mathbb{CP}^n$ is $\pi^n/n!$ in the natural normalization.

**Is NOT an instance — a top-form without the metric.** A top-form on a Riemannian manifold need not be $\omega_g$ or even proportional to it. For example, on $\mathbb{R}^2$, the form $x\,dx\wedge dy$ is a top-form but is not the Riemannian volume form (it vanishes on the $y$-axis and is not normalized to give $1$ on orthonormal frames). The Riemannian volume form is the canonical normalization fixed by the metric.

**Is NOT an instance — on a non-orientable Riemannian manifold.** The Möbius strip with a metric admits a *density* $|\omega_g|$ but no *form* $\omega_g$. The non-orientability prevents the existence of the form; only the density survives.

**Corollary — local [[Def - Isometry|isometries]] pull back the volume form.** If $F : (M, g_M) \to (N, g_N)$ is a local isometry of oriented Riemannian manifolds, then $F^*\omega_{g_N} = \omega_{g_M}$. In particular, the volume of $M$ equals the volume of $F(M)$ counted with multiplicity. This is the form-side statement of "[[Def - Isometry|isometries]] preserve volume".

**Corollary — conformal rescaling.** Under $g \mapsto e^{2\phi}g$, the volume form scales as $\omega_g \mapsto e^{n\phi}\omega_g$. The volume of a compact region $K$ scales as $\mathrm{vol}_{\widetilde g}(K) = \int_K e^{n\phi}\omega_g$. This is the conformal-invariance-or-lack-thereof discussion of integrals.

**Corollary — the volume form is closed but generally not exact.** $d\omega_g = 0$ automatically (top-forms are closed on an $n$-manifold). But on a compact orientable closed $M$, $\int_M\omega_g = \mathrm{vol}(M) > 0$, so by Stokes (if $\omega_g$ were exact, $\omega_g = d\eta$, then $\int_M\omega_g = \int_{\partial M}\eta = 0$, contradiction), $\omega_g$ is *not exact*. Hence $\omega_g$ represents a nonzero class in $H^n_{dR}(M)$.

**Calibration check.** Verify that on Euclidean $\mathbb{R}^n$, $\omega_g = dx^1\wedge\cdots\wedge dx^n$; that in polar coordinates on $\mathbb{R}^2$, $\omega_g = r\,dr\wedge d\theta$ (recovering the Jacobian); that on $S^2$ with the round metric, $\omega_g = \sin\varphi\,d\varphi\wedge d\theta$ giving area $4\pi$; and that the volume form on a compact orientable manifold without boundary is closed but not exact (it represents a nonzero cohomology class). If you can also explain why a conformal change $g \to e^{2\phi}g$ scales $\omega_g$ by $e^{n\phi}$, you have understood the basic computational machinery.

---

# Unlocked by This

> [!tip] Laplace–Beltrami Operator *(from Differential Geometry / Spectral Theory)*
> Using $\omega_g$ to integrate functions, the **Laplace–Beltrami operator** $\Delta_g$ on functions is the unique self-adjoint operator (with respect to the $L^2(\omega_g)$ inner product) coinciding with the Euclidean Laplacian on the model $\mathbb{R}^n$. In coordinates: $\Delta_g f = \tfrac{1}{\sqrt{\det g}}\partial_i\big(\sqrt{\det g}\,g^{ij}\partial_j f\big)$. The $\sqrt{\det g}$ factors come from $\omega_g$.

> [!tip] Hodge Star and Hodge Decomposition *(from Differential Geometry / Hodge Theory)*
> The Hodge star $\star : \Omega^k \to \Omega^{n-k}$ on an oriented Riemannian manifold satisfies $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle_g\omega_g$. Used to define the codifferential $\delta$, the Hodge Laplacian $\Delta = d\delta + \delta d$, and the **Hodge decomposition** $\Omega^k(M) = \mathcal{H}^k \oplus d\Omega^{k-1} \oplus \delta\Omega^{k+1}$ on a closed manifold.

> [!tip] Lebesgue Measure on a Manifold *(from Measure Theory)*
> The Riemannian volume form induces a canonical Borel measure $\mu_g$ on $M$ via $\mu_g(A) := \int_A\omega_g$. This measure is locally equivalent to [[Def - Lebesgue Measure|Lebesgue measure]] in any chart, with Radon–Nikodým derivative $\sqrt{\det g}$. It is the bridge to measure-theoretic integration on manifolds.

> [!tip] Riemannian Heat Kernel *(from PDE / Differential Geometry)*
> The heat equation $\partial_t u = \Delta_g u$ on $M$ has a fundamental solution $K_g(t; x, y)$, the **heat kernel**, satisfying $\int_M K_g(t; x, y)f(y)\,\omega_g(y) = (e^{t\Delta_g}f)(x)$. Its short-time asymptotics encode the Riemann curvature of $M$ — the Minakshisundaram–Pleijel expansion, foundational for index theory.

> [!tip] Jeffreys Prior and Information Geometry *(from Bayesian Statistics)*
> On a statistical manifold $\{p_\theta\}$ with the Fisher metric $g_{ij}(\theta)$, **Jeffreys's prior** is $\pi(\theta)\,d\theta = \sqrt{\det g_{ij}(\theta)}\,d\theta = \omega_g$. This is the unique reparametrization-invariant noninformative prior, fundamental to objective Bayesian inference.
