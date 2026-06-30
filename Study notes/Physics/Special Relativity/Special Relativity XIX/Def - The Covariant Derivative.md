---
type: definition
subject: special-relativity
prereqs:
  - "Def - Arbitrary Coordinates and the Coordinate Basis"
  - "Def - Tensors on Minkowski Space"
  - "Def - Christoffel Symbols"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. $\mathscr{E}$ is flat spacetime, $E$ its vector space of displacements, with arbitrary coordinates $(x^\alpha)$ and coordinate basis $\vec{e}_\alpha = \partial/\partial x^\alpha$ (see [[Def - Arbitrary Coordinates and the Coordinate Basis]]). A tensor field of type $(k,\ell)$ is a smooth map $\boldsymbol{T} : \mathscr{E} \to \mathscr{T}_{(k,\ell)}(E)$ assigning a tensor to each event; $(0,0)$ is a scalar field, $(1,0)$ a vector field. The covariant derivative is $\boldsymbol{\nabla}$, with components $\nabla_\beta v^\alpha$, $\nabla_\beta\omega_\alpha$; the connection coefficients are $\Gamma^\gamma{}_{\alpha\beta}$. Full registry on [[Special Relativity XIX — Fields on Spacetime and the Covariant Derivative]].

> [!warning] Convention: this is the flat-spacetime covariant derivative
> The operator defined here is the covariant derivative of *flat* Minkowski spacetime in arbitrary coordinates. It is the **same operator** as the manifold covariant derivative of [[Riemannian Geometry I — Connections and Covariant Differentiation]], specialised to a spacetime whose curvature vanishes — but it is a distinct page from the manifold treatment; bridge between them, do not merge them. Gourgoulhon's source uses mostly-plus signature, which affects only the explicit metric arrays, not the structure of $\boldsymbol{\nabla}$.

---

# Axiom Motivation

Once the coordinates are arbitrary, the basis vectors $\vec{e}_\alpha(M)$ vary from event to event, and this innocuous fact breaks the naive notion of "the derivative of a vector field". Here is the failure in its sharpest form. Take the vector field $\vec{v} = \vec{e}_r$ in spherical coordinates: its components in the coordinate basis are $v^\alpha = (0,1,0,0)$, a *constant* tuple, so the array of partial derivatives $\partial_\beta v^\alpha$ is identically zero. Yet $\vec{e}_r$ obviously points in different directions at different places — it is a *radial* vector, swinging around as you orbit the origin — so the field genuinely changes, and any honest derivative must register that change. The partial derivative does not, because it sees only the components and is blind to the turning of the basis. We need a derivative that sees both.

The desideratum, stated abstractly, is a derivative that takes a tensor field of type $(k,\ell)$ and returns a tensor field — so that it can appear in physical laws, which must be tensorial — and that reduces to the partial derivative when the basis is constant (inertial coordinates), since there the partial derivative *is* correct. The construction that achieves this is forced by what "variation of $\boldsymbol{T}$" should mean. Between two infinitesimally close events $M$ and $M'$, the variation $\mathrm{d}\boldsymbol{T} = \boldsymbol{T}(M') - \boldsymbol{T}(M)$ is, to first order, linear in the displacement $\overrightarrow{MM'} = \mathrm{d}\vec{x}$. A linear map sending the displacement vector $\mathrm{d}\vec{x}$ to the variation $\mathrm{d}\boldsymbol{T}$ is exactly a tensor with one extra covariant slot — the slot that eats $\mathrm{d}\vec{x}$. So the covariant derivative $\boldsymbol{\nabla}\boldsymbol{T}$ is *defined* to be that tensor: $\mathrm{d}\boldsymbol{T} = \boldsymbol{\nabla}_{\mathrm{d}\vec{x}}\boldsymbol{T}$, a tensor of type $(k,\ell+1)$.

Why this definition and not a nearby variant? The key constraints are three, and each excludes an alternative. First, $\boldsymbol{\nabla}$ must obey the **Leibniz rule** with respect to the tensor product, $\boldsymbol{\nabla}_{\vec v}(A\otimes B) = \boldsymbol{\nabla}_{\vec v}A\otimes B + A\otimes\boldsymbol{\nabla}_{\vec v}B$, because differentiation of a product of fields must distribute — drop this and $\boldsymbol{\nabla}$ would not be a derivation, and the component formula for a vector ($v^\alpha\vec{e}_\alpha$) could not be derived from the product rule applied to components-times-basis. Second, $\boldsymbol{\nabla}$ must **commute with contraction**: taking a trace of a tensor and then differentiating must equal differentiating and then tracing, $\boldsymbol{\nabla}(C^p_q\boldsymbol{T}) = C^p_q(\boldsymbol{\nabla}\boldsymbol{T})$ — drop this and the derivative of a scalar built by contracting (like $\omega_\alpha v^\alpha$) would not equal the naive product rule, and the lower-index sign in $\nabla_\beta\omega_\alpha = \partial_\beta\omega_\alpha - \Gamma^\mu{}_{\alpha\beta}\omega_\mu$ could not be forced. Third, on a scalar field $\boldsymbol{\nabla}f$ must be the ordinary **gradient**, the linear form with components $\partial f/\partial x^\alpha$ — because a scalar has no basis-dependence to correct, so its variation is unambiguous, and $\boldsymbol{\nabla}$ must agree with calculus there. These three constraints, together with linearity in $\mathrm{d}\vec{x}$, pin down $\boldsymbol{\nabla}$ uniquely once a basis (hence the connection coefficients) is given.

There is a fourth property, special to the metric and not part of the bare definition, that elevates this particular $\boldsymbol{\nabla}$ to *the* connection of spacetime: **metric compatibility**, $\boldsymbol{\nabla}g = 0$. On flat spacetime it holds for a trivial reason — the metric $g$ is a fixed type $(0,2)$ tensor, the *same* bilinear form at every event, hence a constant tensor field, and the covariant derivative of a constant tensor field is zero. The significance is enormous and worth dwelling on. Metric compatibility says that lengths and angles do not change under covariant differentiation, so $\boldsymbol{\nabla}$ commutes with raising and lowering indices; combined with the symmetry of the connection coefficients (torsion-freeness, automatic for a coordinate basis), it makes $\boldsymbol{\nabla}$ the *unique* Levi-Civita connection of $g$. And it is the property that, transplanted to a curved spacetime where $g = g_{\mu\nu}(x)$ is genuinely position-dependent, *defines* the connection of general relativity. The flat case is the one where $\boldsymbol{\nabla}g = 0$ is trivial; the curved case is the one where it is a substantive condition determining the Christoffel symbols from the metric. Everything else is identical.

Finally, the definition must be checked against the failure that motivated it. For the field $\vec{v} = \vec{e}_r$ with constant components, the covariant derivative is *not* zero: the connection term $\Gamma^\alpha{}_{\mu\beta}v^\mu$ supplies the missing information about the turning of the basis, and one computes (for instance) $\nabla_\theta v^\theta = 1/r \neq 0$, registering exactly the swing of the radial direction. The naive partial derivative gave zero; the covariant derivative gives the right, nonzero, tensorial answer. That is the whole justification of the construction.

---

# The Definition

Let $\boldsymbol{T}$ be a tensor field of type $(k,\ell)$ on $\mathscr{E}$. Its **covariant derivative** $\boldsymbol{\nabla}\boldsymbol{T}$ is the tensor field of type $(k,\ell+1)$ such that, for two infinitesimally close events $M$ and $M'$ with $\overrightarrow{MM'} = \mathrm{d}\vec{x}$,
$$\mathrm{d}\boldsymbol{T} := \boldsymbol{T}(M') - \boldsymbol{T}(M) = \boldsymbol{\nabla}_{\mathrm{d}\vec{x}}\,\boldsymbol{T},$$
where the **covariant derivative along a vector** $\vec{v}$ is the contraction of $\boldsymbol{\nabla}\boldsymbol{T}$ on its last (new) slot with $\vec{v}$:
$$\boldsymbol{\nabla}_{\vec v}\,\boldsymbol{T} := \boldsymbol{\nabla}\boldsymbol{T}(\,\cdot,\dots,\cdot,\vec{v}\,).$$
The components are written $\nabla_\beta T^{\alpha_1\cdots\alpha_k}{}_{\beta_1\cdots\beta_\ell}$ (the new index $\beta$ on the left), with $(\boldsymbol{\nabla}_{\vec v}\boldsymbol{T})^{\cdots}{}_{\cdots} = v^\mu\,\nabla_\mu T^{\cdots}{}_{\cdots}$.

**Defining properties.** The covariant derivative is the unique operator satisfying:

1. On a scalar field $f$, $\boldsymbol{\nabla}f$ is the **gradient**, the $1$-form with $\nabla_\alpha f = \dfrac{\partial f}{\partial x^\alpha}$ (metric-independent).
2. **Leibniz rule** for $\otimes$: $\quad\boldsymbol{\nabla}_{\vec v}(A\otimes B) = \boldsymbol{\nabla}_{\vec v}A\otimes B + A\otimes\boldsymbol{\nabla}_{\vec v}B$, and in particular $\boldsymbol{\nabla}_{\vec v}(fB) = (\boldsymbol{\nabla}_{\vec v}f)\,B + f\,\boldsymbol{\nabla}_{\vec v}B$.
3. **Commutes with contraction**: $\quad\boldsymbol{\nabla}(C^p_q\boldsymbol{T}) = C^p_q(\boldsymbol{\nabla}\boldsymbol{T})$.

**Component formula.** In any coordinate basis, with connection coefficients $\Gamma^\gamma{}_{\alpha\beta}$ (see [[Def - Christoffel Symbols]]),
$$\boxed{\;\nabla_\beta v^\alpha = \frac{\partial v^\alpha}{\partial x^\beta} + \Gamma^\alpha{}_{\mu\beta}\,v^\mu\;}\qquad\text{and}\qquad\boxed{\;\nabla_\beta \omega_\alpha = \frac{\partial \omega_\alpha}{\partial x^\beta} - \Gamma^\mu{}_{\alpha\beta}\,\omega_\mu\;}$$
for a vector field $\vec{v}$ and a $1$-form $\omega$, and for a general type $(k,\ell)$ field one $+\Gamma$ term per contravariant index and one $-\Gamma$ term per covariant index:
$$\nabla_\rho T^{\alpha_1\cdots\alpha_k}{}_{\beta_1\cdots\beta_\ell} = \frac{\partial T^{\alpha_1\cdots\alpha_k}{}_{\beta_1\cdots\beta_\ell}}{\partial x^\rho} + \sum_{p=1}^{k}\Gamma^{\alpha_p}{}_{\mu\rho}\,T^{\alpha_1\cdots\mu\cdots\alpha_k}{}_{\beta_1\cdots\beta_\ell} - \sum_{q=1}^{\ell}\Gamma^{\mu}{}_{\beta_q\rho}\,T^{\alpha_1\cdots\alpha_k}{}_{\beta_1\cdots\mu\cdots\beta_\ell}.$$

**Metric compatibility.** Because the flat metric is a constant tensor field,
$$\boldsymbol{\nabla}g = 0, \qquad\text{equivalently}\qquad \nabla_\gamma g_{\alpha\beta} = 0,$$
which, with the symmetry $\Gamma^\gamma{}_{\alpha\beta} = \Gamma^\gamma{}_{\beta\alpha}$, makes $\boldsymbol{\nabla}$ the unique torsion-free metric connection (the Levi-Civita connection). In inertial (affine) coordinates the basis is constant, $\Gamma^\gamma{}_{\alpha\beta} = 0$, and $\nabla_\rho T^{\cdots}{}_{\cdots} = \partial_\rho T^{\cdots}{}_{\cdots}$.

**Absolute derivative along a worldline.** For a vector field $\vec{v}$ and a timelike worldline $\mathscr{L}$ with four-velocity $\vec{u}$ and proper time $t$, the rate of change of $\vec{v}$ along $\mathscr{L}$ is $\dfrac{\mathrm{d}\vec{v}}{\mathrm{d}t} = c\,\boldsymbol{\nabla}_{\vec u}\,\vec{v}$ (the absolute derivative).

---

# Categorical / Structural Definition

In the language of vector bundles, the covariant derivative is a **connection** on the tangent bundle $TE$ (and, by the Leibniz and contraction rules, on all the tensor bundles built from it): an $\mathbb{R}$-linear map $\boldsymbol{\nabla} : \Gamma(TE) \to \Gamma(T^*E\otimes TE)$ satisfying $\boldsymbol{\nabla}(f\vec{v}) = \mathrm{d}f\otimes\vec{v} + f\boldsymbol{\nabla}\vec{v}$. The defining properties above are precisely the axioms of a connection extended to the full tensor algebra: $\mathbb{R}$-linearity, the Leibniz product rule (which is the connection axiom), and commutation with contraction (which is what extends the bundle connection canonically to dual and tensor bundles). See [[Riemannian Geometry I/Def - Affine Connection on a Vector Bundle|affine connection on a vector bundle]] and [[Riemannian Geometry I/Def - Induced Connection on Tensor Bundles|the induced connection on tensor bundles]].

Among all connections, two extra conditions select a unique one: **metric compatibility** $\boldsymbol{\nabla}g = 0$ (the connection preserves the metric, so parallel transport is an isometry) and **vanishing torsion** $\Gamma^\gamma{}_{\alpha\beta} = \Gamma^\gamma{}_{\beta\alpha}$ (the symmetric part is the only part, equivalently $\boldsymbol{\nabla}_{\vec u}\vec{v} - \boldsymbol{\nabla}_{\vec v}\vec{u} = [\vec{u},\vec{v}]$). The [[Riemannian Geometry I/Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem of Riemannian geometry]] guarantees existence and uniqueness, and the [[Riemannian Geometry I/Thm - Koszul Formula|Koszul formula]] writes the connection in terms of the metric — on flat spacetime in a coordinate basis it reduces to the Christoffel formula. The structural punchline is that the covariant derivative of this chapter is *the* [[Riemannian Geometry I/Def - Levi-Civita Connection|Levi-Civita connection]], computed for a metric that is flat.

---

# Relate to Other Fields / Compression

This is the **Levi-Civita connection of flat spacetime**, identical in every formula to the connection of [[Riemannian Geometry I — Connections and Covariant Differentiation]] and of [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]], evaluated on a metric of zero curvature. The construction "variation linear in the displacement $\Rightarrow$ extra covariant slot $\Rightarrow$ tensor" is the connection in its purest form.

**True name:** the covariant derivative is *the partial derivative plus a correction for the turning of the basis*, the correction being $\pm\Gamma$ per index. Operationally you never use the abstract limit; you use the component formula $\nabla_\beta v^\alpha = \partial_\beta v^\alpha + \Gamma^\alpha{}_{\mu\beta}v^\mu$, with the sign mnemonic "$+$ for up, $-$ for down, derivation index last on $\Gamma$". The single highest-leverage fact is $\boldsymbol{\nabla}g = 0$: it lets the metric pass freely through $\boldsymbol{\nabla}$, so raising and lowering indices commutes with covariant differentiation, and it is the equation that becomes the *definition* of the connection in curved spacetime.

---

# Examples / Corollaries

**Is an instance — the gradient of a scalar.** For $f$ a scalar field, $\boldsymbol{\nabla}f$ has no Christoffel correction (a scalar has no index to dress), so $\nabla_\alpha f = \partial f/\partial x^\alpha$ in *every* coordinate system. This is why the gradient was definable in [[Def - Arbitrary Coordinates and the Coordinate Basis]] before any connection: scalar fields differentiate trivially.

**Is an instance — a vector field with constant components.** Take $\vec{v} = \vec{e}_r$ in spherical coordinates, $v^\alpha = (0,1,0,0)$. Then $\partial_\beta v^\alpha = 0$, but $\nabla_\beta v^\alpha = \Gamma^\alpha{}_{r\beta}$, and using $\Gamma^\theta{}_{r\theta} = 1/r$, $\Gamma^\varphi{}_{r\varphi} = 1/r$ one finds $\nabla_\theta v^\theta = 1/r$ and $\nabla_\varphi v^\varphi = 1/r$. So $\boldsymbol{\nabla}\vec{e}_r \neq 0$: the covariant derivative correctly reports that the radial field changes, even though its components do not. This is the canonical demonstration that $\boldsymbol{\nabla} \neq \partial$.

**Is an instance — a constant inertial field in curvilinear coordinates.** Take $\vec{w} = \vec{e}_x$ (a genuinely constant field on flat space) expressed in spherical coordinates, where its components are the non-constant $w^\alpha = (0,\,\sin\theta\cos\varphi,\,\cos\theta\cos\varphi/r,\,-\sin\varphi/(r\sin\theta))$. Here $\partial_\beta w^\alpha \neq 0$ — the components vary — yet $\nabla_\beta w^\alpha = 0$ once the Christoffel terms are added, because $\vec{e}_x$ really is constant. This is the mirror image of the previous example: constant field, varying components, zero covariant derivative.

**Is NOT an instance — the naive partial-derivative array $\partial_\beta v^\alpha$.** The array $\partial_\beta v^\alpha$ is *not* the covariant derivative and is *not* a tensor: under a change of coordinates it acquires an inhomogeneous second-derivative term $v^\mu\,\partial_\beta\partial_\mu x'^\gamma\,(\partial x^\alpha/\partial x'^\gamma)$, so its value depends on the coordinate system in a way no tensor's does. Only the combination $\partial_\beta v^\alpha + \Gamma^\alpha{}_{\mu\beta}v^\mu$ transforms correctly — the inhomogeneous term of $\partial_\beta v^\alpha$ exactly cancels the inhomogeneous transformation of $\Gamma$.

**Corollary — $\boldsymbol{\nabla}$ commutes with raising and lowering indices.** From $\boldsymbol{\nabla}g = 0$ and the Leibniz rule, $\nabla_\mu(g_{\alpha\beta}v^\beta) = g_{\alpha\beta}\nabla_\mu v^\beta$, so $\nabla_\mu v_\alpha = g_{\alpha\beta}\nabla_\mu v^\beta$. The covariant derivative of the lowered vector is the lowered covariant derivative; one may move indices in and out of $\boldsymbol{\nabla}$ at will.

**Corollary — in inertial coordinates $\boldsymbol{\nabla}$ is $\partial$.** With $\Gamma = 0$, $\nabla_\rho T^{\cdots}{}_{\cdots} = \partial_\rho T^{\cdots}{}_{\cdots}$. So all the elaborate index machinery collapses to ordinary partial differentiation the moment one returns to an inertial frame — the sanity check available on flat spacetime and unavailable on a curved one.

**Calibration check.** You should be able to (i) write $\nabla_\beta v^\alpha$ and $\nabla_\beta\omega_\alpha$ with the correct signs; (ii) compute $\nabla_\theta v^\theta = 1/r$ for $\vec{v} = \vec{e}_r$ and explain why the partial derivative gave zero; and (iii) explain in one sentence why $\boldsymbol{\nabla}g = 0$ is trivial on flat spacetime but substantive in general relativity.

---

# Unlocked by This

> [!tip] The Connection on a Manifold and Parallel Transport *(from Differential Geometry)*
> The covariant derivative defines **parallel transport**: a vector is parallel-transported along a curve if its covariant derivative along the curve vanishes, $\boldsymbol{\nabla}_{\vec u}\vec{v} = 0$. On flat spacetime parallel transport is path-independent (a vector returns to itself around any loop); the path-*dependence* of parallel transport on a curved manifold is the holonomy, measured by the curvature. See [[Riemannian Geometry I/Def - Parallel Transport|parallel transport]].

> [!tip] The Geodesic Equation *(from General Relativity)*
> A worldline is a **geodesic** — the relativistic straight line, the path of free fall — when its tangent is parallel-transported along itself, $\boldsymbol{\nabla}_{\vec u}\vec{u} = 0$, which in components is $\ddot{x}^\gamma + \Gamma^\gamma{}_{\alpha\beta}\dot{x}^\alpha\dot{x}^\beta = 0$. On flat spacetime in inertial coordinates this is $\ddot{x}^\gamma = 0$ (straight lines); in rotating coordinates the Christoffels reproduce centrifugal and Coriolis terms; in a curved spacetime the same equation with a curved metric is the law of gravitation. See [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

> [!tip] The Covariant Derivative of General Relativity *(from General Relativity)*
> This is the decisive unlock. Promote the constant metric $\eta_{\mu\nu}$ to a dynamical field $g_{\mu\nu}(x)$ obeying the Einstein equations, and **every formula on this page survives unchanged**: $\boldsymbol{\nabla}$ is still defined by $\boldsymbol{\nabla}g = 0$ plus torsion-freeness, the Christoffels are still $\tfrac12 g^{\gamma\mu}(\partial g + \partial g - \partial g)$, and matter still moves on geodesics $\boldsymbol{\nabla}_{\vec u}\vec{u} = 0$. The one new thing is curvature, $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma\Gamma - \Gamma\Gamma$, which is zero here and nonzero there. The covariant derivative is thus the load-bearing object common to special and general relativity, and the step between them is the step from a flat metric to a curved one. See [[General Relativity I — Einstein's Equations and Schwarzschild]].
