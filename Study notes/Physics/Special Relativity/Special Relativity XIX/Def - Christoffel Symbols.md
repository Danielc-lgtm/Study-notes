---
type: definition
subject: special-relativity
prereqs:
  - "Def - Arbitrary Coordinates and the Coordinate Basis"
  - "Def - The Covariant Derivative"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. Arbitrary coordinates $(x^\alpha)$ on flat spacetime, with coordinate basis $\vec{e}_\alpha$, metric components $g_{\alpha\beta} = \vec{e}_\alpha\cdot\vec{e}_\beta$ and inverse $g^{\alpha\beta}$ (see [[Def - Arbitrary Coordinates and the Coordinate Basis]]). The covariant derivative is $\boldsymbol{\nabla}$ (see [[Def - The Covariant Derivative]]). The connection coefficients are $\Gamma^\gamma{}_{\alpha\beta}$; $\partial_\alpha \equiv \partial/\partial x^\alpha$. Full registry on [[Special Relativity XIX — Fields on Spacetime and the Covariant Derivative]].

This is a compound page: it defines two interlocking notions — the **connection coefficients** of an arbitrary field of bases, and the **Christoffel symbols** (the connection coefficients of a metric's coordinate basis) — because the second is the first specialised, and the chapter needs both names.

> [!warning] Convention: flat-spacetime Christoffel symbols; signature-independent formula
> These are the Christoffel symbols of *flat* spacetime in curvilinear coordinates — the same objects as the manifold [[Riemannian Geometry I/Def - Christoffel Symbols|Christoffel symbols]] of [[Riemannian Geometry I — Connections and Covariant Differentiation]], but for a metric of zero curvature. The defining formula $\Gamma^\gamma{}_{\alpha\beta} = \tfrac12 g^{\gamma\mu}(\partial_\alpha g_{\mu\beta} + \partial_\beta g_{\alpha\mu} - \partial_\mu g_{\alpha\beta})$ is **signature-independent**: it contains one factor $g^{\gamma\mu}$ (upper) against three factors $g_{\cdots}$ (lower) in each term, and under a global sign flip of the metric the up-index inverse and the down-index components flip oppositely, so the value is unchanged. Gourgoulhon's mostly-plus arrays therefore give the *same* Christoffel symbols as our mostly-minus arrays.

---

# Axiom Motivation

The covariant derivative was defined abstractly — the tensor that captures the first-order variation of a field — but to compute with it we need its value on the basis vectors themselves, because everything else follows by the Leibniz rule. So ask the concrete question: how does the basis vector $\vec{e}_\alpha$ change as you move in the direction $\vec{e}_\beta$? The answer is some vector at each event, and a vector can be expanded on the basis. The coefficients of that expansion are, by definition, the connection coefficients: $\boldsymbol{\nabla}_{\vec{e}_\beta}\vec{e}_\alpha = \Gamma^\mu{}_{\alpha\beta}\vec{e}_\mu$. There is no choice here; this is simply the name for "the components of the rate of turning of the basis". It is the minimal data needed to compute any covariant derivative, because once you know how the basis turns, the product rule applied to $v^\alpha\vec{e}_\alpha$ gives $\nabla_\beta v^\alpha = \partial_\beta v^\alpha + \Gamma^\alpha{}_{\mu\beta}v^\mu$ and you are done.

Two facts about the connection coefficients are not optional once the basis is a *coordinate* basis built from a metric, and seeing why each is forced is the heart of the matter. The first is **symmetry in the lower indices**, $\Gamma^\gamma{}_{\alpha\beta} = \Gamma^\gamma{}_{\beta\alpha}$. This is equivalent to $\boldsymbol{\nabla}_{\vec{e}_\beta}\vec{e}_\alpha = \boldsymbol{\nabla}_{\vec{e}_\alpha}\vec{e}_\beta$, and it holds because the coordinate basis vectors are gradients of coordinates: moving along $\vec{e}_\beta$ and then $\vec{e}_\alpha$ reaches the same nearby event as moving along $\vec{e}_\alpha$ then $\vec{e}_\beta$ (coordinate increments commute), so the second-order displacement is symmetric. Were the basis a general field of bases (a tetrad, say) this would fail — the Lie bracket $[\vec{e}_\alpha,\vec{e}_\beta]$ would be nonzero, and the connection coefficients would carry an antisymmetric piece. Symmetry is therefore a gift of using a coordinate basis, and it is exactly the **torsion-free** condition.

The second forced fact is the explicit formula in terms of the metric, and it is forced by **metric compatibility** $\boldsymbol{\nabla}g = 0$. The flat metric is a constant tensor field, so $\nabla_\gamma g_{\alpha\beta} = 0$; writing this out with the lower-index covariant-derivative rule gives $\partial_\gamma g_{\alpha\beta} = \Gamma^\mu{}_{\alpha\gamma}g_{\mu\beta} + \Gamma^\mu{}_{\beta\gamma}g_{\alpha\mu}$. This is one equation relating the derivatives of the metric to the connection coefficients. The trick that solves for $\Gamma$ is the standard one: write the same equation three times with the indices $\alpha,\beta,\gamma$ cyclically permuted, add two and subtract one, and use the symmetry $\Gamma^\gamma{}_{\alpha\beta} = \Gamma^\gamma{}_{\beta\alpha}$ to collapse the result. Out drops $\Gamma^\gamma{}_{\alpha\beta} = \tfrac12 g^{\gamma\mu}(\partial_\alpha g_{\mu\beta} + \partial_\beta g_{\alpha\mu} - \partial_\mu g_{\alpha\beta})$. The point of the derivation is that *symmetry plus metric compatibility uniquely determine the connection coefficients from the metric* — there is exactly one symmetric connection compatible with $g$, and this formula is it. This is the content of the fundamental theorem of Riemannian geometry, and the reason the Christoffel symbols are not extra data but are computed from the metric.

What would go wrong with a nearby variant? If you dropped metric compatibility, the formula would be false — the connection coefficients would be independent of the metric, and there would be infinitely many connections. If you dropped symmetry, you would have torsion, and the formula would acquire antisymmetric correction terms (the contorsion). The specific combination $+\partial_\alpha g_{\mu\beta} + \partial_\beta g_{\alpha\mu} - \partial_\mu g_{\alpha\beta}$ — two plus, one minus, in that index pattern — is the unique one that the cyclic-permutation trick produces, and any other sign pattern fails to solve $\nabla g = 0$. Finally, the formula must be checked to reduce correctly: in inertial coordinates $g_{\alpha\beta} = \eta_{\alpha\beta}$ is constant, every $\partial g = 0$, and $\Gamma^\gamma{}_{\alpha\beta} = 0$ — confirming that the connection coefficients vanish exactly when the basis is constant.

The deepest motivation is the one that points forward. On flat spacetime the Christoffel symbols are nonzero in curvilinear coordinates but can be transformed to zero *everywhere at once* by returning to inertial coordinates — they encode the curvature of the *coordinate system*, not of the *spacetime*. The obstruction to transforming them all away is the Riemann curvature tensor, built from their first derivatives; on flat spacetime it vanishes. So the Christoffel symbols are the exact object whose nonvanishing distinguishes "I am using bad coordinates" (flat space, fictitious forces) from "spacetime is curved" (gravitation) — and that distinction is invisible to the Christoffel symbols themselves, visible only in their derivatives. This is why the same formula, the same symbols, serve in special relativity as a bookkeeping device for curvilinear coordinates and in general relativity as the gravitational field.

---

# The Definition

**Connection coefficients.** Given a field of bases $(\vec{e}_\alpha)$ on $\mathscr{E}$, the **connection coefficients** $\Gamma^\gamma{}_{\alpha\beta}$ relative to that frame are defined by expanding the covariant derivative of each basis vector along each basis vector on the basis itself:
$$\boldsymbol{\nabla}_{\vec{e}_\beta}\,\vec{e}_\alpha =: \Gamma^\mu{}_{\alpha\beta}\,\vec{e}_\mu.$$
They are $4^3 = 64$ scalar fields on $\mathscr{E}$. For the dual basis, $\boldsymbol{\nabla}_{\vec{e}_\beta}\,e^\alpha = -\Gamma^\alpha{}_{\mu\beta}\,e^\mu$.

**Christoffel symbols.** When $(\vec{e}_\alpha)$ is the **coordinate basis** of a coordinate system $(x^\alpha)$ and the metric components are $g_{\alpha\beta}$, the connection coefficients are symmetric in their lower indices,
$$\Gamma^\gamma{}_{\alpha\beta} = \Gamma^\gamma{}_{\beta\alpha}\qquad(\text{coordinate basis}),$$
and are given explicitly by the **Christoffel symbols**
$$\boxed{\;\Gamma^\gamma{}_{\alpha\beta} = \frac{1}{2}\,g^{\gamma\mu}\!\left(\frac{\partial g_{\mu\beta}}{\partial x^\alpha} + \frac{\partial g_{\alpha\mu}}{\partial x^\beta} - \frac{\partial g_{\alpha\beta}}{\partial x^\mu}\right).\;}$$
This formula is valid *only* for the components in a coordinate basis. In inertial (affine) coordinates $g_{\alpha\beta} = \eta_{\alpha\beta}$ is constant, so $\Gamma^\gamma{}_{\alpha\beta} = 0$.

**Spherical coordinates.** For $(x^\alpha) = (ct,r,\theta,\varphi)$ with $g_{\alpha\beta} = \mathrm{diag}(1,-1,-r^2,-r^2\sin^2\theta)$, the nonzero Christoffel symbols are
$$\Gamma^r{}_{\theta\theta} = -r, \qquad \Gamma^r{}_{\varphi\varphi} = -r\sin^2\theta, \qquad \Gamma^\theta{}_{r\theta} = \Gamma^\theta{}_{\theta r} = \frac{1}{r}, \qquad \Gamma^\theta{}_{\varphi\varphi} = -\cos\theta\sin\theta,$$
$$\Gamma^\varphi{}_{r\varphi} = \Gamma^\varphi{}_{\varphi r} = \frac{1}{r}, \qquad \Gamma^\varphi{}_{\theta\varphi} = \Gamma^\varphi{}_{\varphi\theta} = \frac{1}{\tan\theta} = \cot\theta,$$
all others zero. These involve only the spatial coordinates; the time part contributes nothing because $g_{(ct)(ct)} = 1$ is constant. They are identical to the Christoffel symbols of three-dimensional Euclidean space in spherical coordinates.

---

# Categorical / Structural Definition

The connection coefficients are the components, in a chosen frame, of an **affine connection** $\boldsymbol{\nabla}$ — equivalently the components of the connection $1$-forms $\omega^\gamma{}_\alpha = \Gamma^\gamma{}_{\alpha\beta}\,e^\beta$ of [[Riemannian Geometry I/Def - Connection 1-Forms (Cartan)|Cartan's formalism]]. They are *not* tensor components: under a change of frame they transform inhomogeneously, $\Gamma^\gamma{}_{\alpha\beta} \mapsto (\text{tensorial Jacobian terms}) + (\text{inhomogeneous second-derivative term})$, the inhomogeneous term being exactly what cancels the non-tensoriality of the partial derivative in $\nabla_\beta v^\alpha$. This is the precise sense in which "the connection is not a tensor but its variation makes the covariant derivative a tensor".

Among connections, the symmetric metric-compatible one is unique (the [[Riemannian Geometry I/Def - Levi-Civita Connection|Levi-Civita connection]]), and its connection coefficients in a coordinate basis are the Christoffel symbols. The two defining conditions are: **vanishing torsion** $T^\gamma{}_{\alpha\beta} := \Gamma^\gamma{}_{\alpha\beta} - \Gamma^\gamma{}_{\beta\alpha} = 0$ (see [[Riemannian Geometry I/Def - Torsion Tensor|torsion]]), and **metric compatibility** $\nabla_\gamma g_{\alpha\beta} = 0$ (see [[Riemannian Geometry I/Def - Metric-Compatible Connection|metric-compatible connection]]). The [[Riemannian Geometry I/Thm - Koszul Formula|Koszul formula]] is the coordinate-free statement of the Christoffel formula. The structural content: the Christoffel symbols are not free data but the unique solution to "symmetric and metric-compatible", which on flat spacetime happens to be transformable to zero.

---

# Relate to Other Fields / Compression

The Christoffel symbols are the **Levi-Civita connection coefficients of flat spacetime**, the same objects as the manifold [[Riemannian Geometry I/Def - Christoffel Symbols|Christoffel symbols]] for a metric of zero curvature. In three-dimensional vector calculus they are hidden inside the formulas for gradient, divergence, and Laplacian in curvilinear coordinates — the "$2/r$" and "$\cot\theta$" terms in spherical-coordinate operators are Christoffel symbols.

**True name:** the Christoffel symbols are *the fictitious forces* — centrifugal, Coriolis, and the geometric terms of curvilinear coordinates — the corrections that appear precisely because you have chosen non-inertial coordinates. They can always be set to zero at a point (and on flat spacetime, everywhere) by a change of coordinates, so a nonzero $\Gamma$ is never by itself a sign of gravity. Operationally: read off $g_{\alpha\beta}$, use $\Gamma^\gamma{}_{\alpha\beta} = \tfrac12 g^{\gamma\mu}(\partial_\alpha g_{\mu\beta}+\partial_\beta g_{\alpha\mu}-\partial_\mu g_{\alpha\beta})$, exploit diagonality of $g^{\gamma\mu}$ and the symmetry in $\alpha\beta$. The fact whose nonvanishing *does* signal gravity is the curvature, built from derivatives of $\Gamma$.

---

# Examples / Corollaries

**Is an instance — spherical Christoffel symbols.** As listed above, $\Gamma^r{}_{\theta\theta} = -r$, $\Gamma^\theta{}_{r\theta} = 1/r$, etc. Sample computation: $\Gamma^\theta{}_{r\theta} = \tfrac12 g^{\theta\theta}(\partial_r g_{\theta\theta} + \partial_\theta g_{r\theta} - \partial_\theta g_{r\theta}) = \tfrac12\cdot(-r^{-2})\cdot\partial_r(-r^2) = \tfrac12\cdot(-r^{-2})\cdot(-2r) = 1/r$. (The factor $g^{\theta\theta} = -1/r^2$ in mostly-minus and $\partial_r g_{\theta\theta} = \partial_r(-r^2) = -2r$ both carry the extra sign, and the two signs cancel — confirming the signature-independence.)

**Is an instance — rotating (Langevin) coordinates.** For the rotating metric the nonzero Christoffels include the centrifugal and Coriolis terms; for instance the geodesic equation in these coordinates produces $\ddot r - r\dot\varphi(\dot\varphi + 2\omega\dot t/c)\sin^2\theta - \dots$, the bracketed pieces being Christoffel symbols $\Gamma^r{}_{\varphi\varphi}$ and $\Gamma^r{}_{(ct)\varphi}$. These are the fictitious centrifugal and Coriolis forces of the rotating frame, present even though the spacetime is flat.

**Is an instance — inertial coordinates.** With $g_{\alpha\beta} = \eta_{\alpha\beta}$ every $\partial_\mu g_{\alpha\beta} = 0$, so $\Gamma^\gamma{}_{\alpha\beta} = 0$ identically. The covariant derivative reduces to the partial derivative — the elementary special-relativistic situation in which no connection is ever needed.

**Is NOT an instance — the connection coefficients of the orthonormal spherical frame.** For the tetrad $\vec{e}'_1 = \vec{e}_r$, $\vec{e}'_2 = r^{-1}\vec{e}_\theta$, $\vec{e}'_3 = (r\sin\theta)^{-1}\vec{e}_\varphi$ the connection coefficients (Ricci rotation coefficients) are *not* symmetric in their lower indices, and the metric formula $\tfrac12 g^{\gamma\mu}(\partial g + \partial g - \partial g)$ gives the *wrong* answer, because that formula's derivation assumed a coordinate basis. One must compute $\boldsymbol{\nabla}_{\vec{e}'_\beta}\vec{e}'_\alpha$ directly. This is the standard trap: the Christoffel formula is for coordinate bases only.

**Corollary — the Christoffels are not a tensor.** If they were, $\Gamma = 0$ in one coordinate system (inertial) would force $\Gamma = 0$ in all, contradicting their nonvanishing in spherical coordinates. Their inhomogeneous transformation law is exactly what is needed to make $\nabla_\beta v^\alpha$ tensorial.

**Corollary — the trace gives the divergence factor.** Contracting the formula on $\gamma$ and $\beta$ yields $\Gamma^\nu{}_{\mu\nu} = \tfrac12 g^{\rho\sigma}\partial_\mu g_{\rho\sigma} = \dfrac{1}{\sqrt{-\det g}}\,\partial_\mu\sqrt{-\det g}$, the quantity that produces the determinant form of the divergence — see [[Thm - Divergence of a Vector and Tensor Field]].

**Calibration check.** You should be able to (i) derive $\Gamma^\theta{}_{r\theta} = 1/r$ from the metric; (ii) state the two conditions (symmetry, metric compatibility) that make the Christoffel symbols the unique connection of $g$; and (iii) explain why $\Gamma \neq 0$ in spherical coordinates does not mean the space is curved, naming the object (Riemann tensor) that does detect curvature.

---

# Unlocked by This

> [!tip] The Geodesic Equation and Fictitious Forces *(from General Relativity)*
> The Christoffel symbols are the coefficients of the **geodesic equation** $\ddot{x}^\gamma + \Gamma^\gamma{}_{\alpha\beta}\dot{x}^\alpha\dot{x}^\beta = 0$. In rotating coordinates they *are* the centrifugal and Coriolis forces; in a gravitational field they are the gravitational force. The equivalence principle is the statement that gravity, like a centrifugal force, is a Christoffel symbol — locally removable by free fall. See [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

> [!tip] The Riemann Curvature Tensor *(from General Relativity)*
> Curvature is built from the *derivatives* of the Christoffel symbols: $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$. Although $\Gamma$ is not a tensor, this particular combination is, and it vanishes identically on flat spacetime — the invariant statement that the curvilinear coordinates' Christoffels can be transformed away. Its non-vanishing is the coordinate-free signature of gravitation. See [[Riemannian Geometry III — Riemann Curvature and Topology]] and [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] The Christoffel Symbols as the Gravitational Field *(from General Relativity)*
> In general relativity the metric $g_{\mu\nu}(x)$ is a dynamical field, and its Christoffel symbols — computed by the *identical* formula used here — are the components of the gravitational field; the geodesic equation with these symbols is the law of free fall, replacing Newton's $\ddot{\mathbf{x}} = -\nabla\Phi$. Where Newton has one potential $\Phi$, Einstein has ten metric components and forty Christoffel symbols, and the flat-spacetime calculation of this page is exactly how one computes them — only with a curved $g$.
