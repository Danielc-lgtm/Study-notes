---
type: definition
subject: special-relativity
prereqs:
  - "Def - Tensors on Minkowski Space"
  - "Def - Metric Duality and Index Manipulation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. Spacetime $\mathscr{E}$ is an affine space; $E$ is its vector space of displacements; events are points $M \in \mathscr{E}$. A coordinate system is written $(x^\alpha) = (x^0,x^1,x^2,x^3)$, a second one $(x'^\alpha)$; Greek indices run $0,\dots,3$, Latin $1,2,3$, with the Einstein summation convention. The coordinate basis is $\vec{e}_\alpha(M)$, its dual basis $e^\alpha$, and the metric components in it are $g_{\alpha\beta} = \vec{e}_\alpha\cdot\vec{e}_\beta$. Full registry on [[Special Relativity XIX — Fields on Spacetime and the Covariant Derivative]].

This is a compound page: it defines three interlocking notions — the **arbitrary coordinate system**, the **coordinate (natural) basis** it induces, and the **components of the metric tensor** in that basis — because they are introduced together and none is fully usable without the others.

> [!warning] Convention: Gourgoulhon uses mostly-plus
> The source uses $\eta = \mathrm{diag}(-1,+1,+1,+1)$, so every metric-component array below has been sign-flipped to mostly-minus. With signature $(1,3)$ the determinant $\det g$ is negative, and the volume factor $\sqrt{-\det g}$ is real and signature-independent in four dimensions.

---

# Axiom Motivation

Until now, a coordinate system on spacetime has meant something very restrictive: an origin event together with a pseudo-orthonormal basis $(\vec{e}_\alpha)$, in which the metric is the constant array $\eta = \mathrm{diag}(1,-1,-1,-1)$ at every event. These are the inertial coordinates, the coordinates of an inertial observer. The desideratum here is to *loosen* this — to allow any reasonable relabelling of events — because the physics forces it. A rotating observer, a uniformly accelerated observer, an observer using spherical coordinates: each describes spacetime with coordinates that are not affine, and we need the mathematical apparatus to handle them. The question is exactly how much freedom to allow, and what structure survives.

The natural answer is: allow any smooth, invertible relabelling. A coordinate system should be a map $\Phi : \mathscr{E} \to \mathbb{R}^4$ assigning to each event four numbers, and the only requirements are that it be injective (distinct events get distinct labels), that its image be an open set, and that both $\Phi$ and $\Phi^{-1}$ be differentiable — a *diffeomorphism* onto its image. Differentiability is the crucial axiom: it is what lets calculus survive the relabelling. Drop it, and a "coordinate system" could be any wild bijection of $\mathbb{R}^4$ with itself, under which the notion of a smooth field, a derivative, or a tangent vector would be meaningless; the chain rule — the engine of every transformation law in the chapter — would have nothing to act on. Drop injectivity, and two distinct events would carry the same label, so a field could not be a function of the coordinates at all. The diffeomorphism requirement is the minimal structure under which the geometry of spacetime can be expressed in the new labels without loss.

Granted arbitrary coordinates, the next thing we need is a *basis* at each event, because vectors and tensors are expressed in components relative to a basis. Inertial coordinates came with a ready-made constant basis; arbitrary coordinates do not, so we must manufacture one. The right construction is forced by what a basis vector should *mean*: $\vec{e}_\alpha$ should be the direction in which the coordinate $x^\alpha$ increases. Concretely, hold all coordinates fixed except $x^\alpha$, increment $x^\alpha$ by an infinitesimal amount, and the resulting displacement vector — divided by the increment — is $\vec{e}_\alpha$. This is the only definition that makes the coordinate basis reduce to the affine basis when the coordinates happen to be affine, and it is the only one for which the displacement between two infinitesimally separated events decomposes cleanly as $\overrightarrow{MM'} = \mathrm{d}x^\alpha\,\vec{e}_\alpha$. Any other choice would break this decomposition and force the chain rule to carry correction terms everywhere.

The decisive new feature, the one that motivates the entire rest of the chapter, is that this coordinate basis is generally *not orthonormal and not constant*. In inertial coordinates $\vec{e}_\alpha\cdot\vec{e}_\beta = \eta_{\alpha\beta}$ at every event; in spherical coordinates $\vec{e}_\theta\cdot\vec{e}_\theta = -r^2$, which varies with position and is not $\pm 1$; in rotating coordinates the basis even fails to be orthogonal, picking up cross terms $\vec{e}_{ct}\cdot\vec{e}_\varphi \neq 0$. So the components of the metric, $g_{\alpha\beta}(M) = \vec{e}_\alpha(M)\cdot\vec{e}_\beta(M)$, become *functions of the event*. This is not because the geometry has changed — the spacetime is still flat Minkowski space, the metric is still the same bilinear form — but because the yardsticks (the basis vectors) we are measuring with now vary from place to place. A position-dependent $g_{\alpha\beta}$ is precisely what will force the introduction of the covariant derivative: the ordinary partial derivative of a field's components will no longer be a tensor, because it cannot tell apart a real change in the field from a change in the position-dependent basis.

One must resist the temptation to read "position-dependent metric" as "curved spacetime". It is not. Curvature is a property of the geometry — the failure to find *any* coordinates making $g_{\alpha\beta} = \eta_{\alpha\beta}$ everywhere — and it is detected by second derivatives of the metric assembled into the Riemann tensor. A position-dependent $g_{\alpha\beta}$ that arises merely from curvilinear coordinates on flat space has zero Riemann tensor, and inertial coordinates restoring $g_{\alpha\beta} = \eta_{\alpha\beta}$ always exist. The whole pedagogical value of this chapter is that it exhibits the full machinery of position-dependent metrics, coordinate bases, and connections in a setting where you can always check your work by transforming back to inertial coordinates — a luxury that disappears the moment the spacetime is genuinely curved.

---

# The Definition

**Arbitrary coordinate system.** A *coordinate system on $\mathscr{E}$* is a mapping
$$\Phi : \mathscr{E} \longrightarrow \mathbb{R}^4, \qquad M \longmapsto (x^0, x^1, x^2, x^3),$$
that is injective (hence bijective onto its image $\Phi(\mathscr{E})$) and such that both $\Phi$ and $\Phi^{-1}$ are differentiable; one says $\Phi$ is a **diffeomorphism** between $\mathscr{E}$ and $\Phi(\mathscr{E})$. The coordinates need not be affine: spherical, null, Rindler, and rotating coordinates are all admissible.

**Coordinate basis (natural basis).** Let $(x^\alpha)$ be a coordinate system. At an event $M$ with coordinates $(x^0,x^1,x^2,x^3)$, and for each $\alpha$, let $M_\alpha$ be the event obtained by incrementing only $x^\alpha$ by an infinitesimal $\mathrm{d}x^\alpha$. The vector $\vec{e}_\alpha(M) \in E$ is defined by
$$\overrightarrow{MM_\alpha} = \mathrm{d}x^\alpha\,\vec{e}_\alpha(M) \quad(\text{no sum}), \qquad\text{equivalently}\qquad \overrightarrow{MM'} = \mathrm{d}x^\alpha\,\vec{e}_\alpha(M)$$
for any event $M'$ infinitesimally near $M$ with coordinates $(x^\alpha + \mathrm{d}x^\alpha)$. The four vectors $(\vec{e}_\alpha(M))$ form a basis of $E$ at every $M$, the **coordinate basis** (or **natural basis**) associated with $(x^\alpha)$. In differential-geometry notation $\vec{e}_\alpha = \partial/\partial x^\alpha$. Under a second coordinate system $(x'^\alpha)$ the bases are related by
$$\vec{e}_\alpha(M) = \frac{\partial x'^\beta}{\partial x^\alpha}\,\vec{e}'_\beta(M).$$
The **dual basis** $(e^\alpha)$ satisfies $\langle e^\alpha, \vec{e}_\beta\rangle = \delta^\alpha{}_\beta$ and equals the gradients of the coordinates, $e^\alpha = \boldsymbol{\nabla}x^\alpha = \mathbf{d}x^\alpha$.

**Components of the metric tensor.** In the coordinate basis the components of the metric tensor $g$ are
$$g_{\alpha\beta}(M) = \vec{e}_\alpha(M)\cdot\vec{e}_\beta(M),$$
a symmetric matrix that is in general a function of the event $M$. Under a change of coordinates they transform as the components of a type $(0,2)$ tensor,
$$g_{\alpha\beta}(M) = \frac{\partial x'^\mu}{\partial x^\alpha}\,\frac{\partial x'^\nu}{\partial x^\beta}\,g'_{\mu\nu}(M).$$
The inverse matrix is denoted $g^{\alpha\beta}$, with $g^{\alpha\mu}g_{\mu\beta} = \delta^\alpha{}_\beta$, and the determinant $\det g$ of $(g_{\alpha\beta})$ is negative (signature $(1,3)$), so $\sqrt{-\det g}$ is real.

---

# Categorical / Structural Definition

A coordinate system is a *chart* in the sense of the theory of smooth manifolds: a diffeomorphism from (an open subset of) the manifold to an open subset of $\mathbb{R}^4$. The affine structure of Minkowski space makes the maximal atlas especially simple — the whole space is covered by a single chart in inertial coordinates — but the chapter deliberately works with arbitrary charts to develop the tools that a genuinely curved spacetime, which admits *no* global inertial chart, will require.

The coordinate basis is the image, at each event, of the standard basis of $\mathbb{R}^4$ under the inverse chart's derivative: $\vec{e}_\alpha(M) = (D\Phi^{-1})_{\Phi(M)}(\partial_\alpha)$, where $\partial_\alpha$ is the $\alpha$-th coordinate vector of $\mathbb{R}^4$. The change-of-basis law $\vec{e}_\alpha = (\partial x'^\beta/\partial x^\alpha)\vec{e}'_\beta$ is then just the chain rule for the composite of two inverse charts. This identifies the coordinate basis with the pushforward of the coordinate frame, and the metric components with the pullback of the metric tensor along the chart — the two operations being adjoint, which is why upper-index objects transform by the Jacobian and lower-index objects by its inverse-transpose. The functorial content is that a change of coordinates acts on the whole tensor algebra at each event by the corresponding linear isomorphism, with one Jacobian factor per contravariant index and one inverse-Jacobian factor per covariant index — the transformation law that *defines* what a tensor field is.

---

# Relate to Other Fields / Compression

This is the special-relativistic instance of the general apparatus of **charts and coordinate frames** on a smooth manifold (see [[Differential Geometry VIII — Differential Forms]] for the form-theoretic side and [[Riemannian Geometry I — Connections and Covariant Differentiation]] for the metric side). The construction "coordinate $\Rightarrow$ natural basis $\partial/\partial x^\alpha$ $\Rightarrow$ metric components $g_{\alpha\beta}$" is verbatim the manifold construction; the only specialisation is that the manifold is flat affine spacetime, so a global chart with $g_{\alpha\beta} = \eta_{\alpha\beta}$ exists.

**True name:** the coordinate basis is *the directions in which the coordinates increase*, and the metric components are *the dot products of those directions*. Operationally, you never compute $\vec{e}_\alpha$ from its definition; you read it off the coordinate change, $\vec{e}_\alpha = (\partial x'^\beta/\partial x^\alpha)\vec{e}'_\beta$, and then $g_{\alpha\beta} = J^{\mathsf T}\eta J$ with $J$ the Jacobian to inertial coordinates. The single most useful fact is that a position-dependent $g_{\alpha\beta}$ does **not** mean curvature — it may be flat space in curvilinear clothes.

---

# Examples / Corollaries

**Is an instance — spherical coordinates.** From inertial coordinates $(x'^\alpha) = (ct,x,y,z)$ define $(x^\alpha) = (ct,r,\theta,\varphi)$ by $x = r\sin\theta\cos\varphi$, $y = r\sin\theta\sin\varphi$, $z = r\cos\theta$. The Jacobian $\partial x'^\beta/\partial x^\alpha$ gives the coordinate basis vectors $\vec{e}_r = \sin\theta\cos\varphi\,\vec{e}_x + \sin\theta\sin\varphi\,\vec{e}_y + \cos\theta\,\vec{e}_z$, and so on, and the metric components come out to
$$g_{\alpha\beta} = \mathrm{diag}\!\left(1,\,-1,\,-r^2,\,-r^2\sin^2\theta\right).$$
The basis is orthogonal (off-diagonal $g_{\alpha\beta} = 0$) but *not* orthonormal: $g_{\theta\theta} = -r^2 \neq -1$. The coordinates are singular on the timelike plane $x=y=0$ (where $r=0$ or $\sin\theta=0$).

**Is an instance — rotating (Langevin) coordinates.** For a uniformly rotating observer the spherical coordinates $(ct,r,\theta,\varphi)$ are related to the inertial spherical ones $(ct',r',\theta',\varphi')$ by $t'=t$, $r'=r$, $\theta'=\theta$, $\varphi' = \varphi + \omega t$. The Jacobian carries the off-diagonal entry $\partial\varphi'/\partial(ct) = \omega/c$, and the metric becomes
$$g_{\alpha\beta} = \begin{pmatrix} 1 - \omega^2 r^2\sin^2\theta & 0 & 0 & -\omega r^2\sin^2\theta \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -r^2 & 0 \\ -\omega r^2\sin^2\theta & 0 & 0 & -r^2\sin^2\theta \end{pmatrix}.$$
The cross term $g_{(ct)\varphi} = -\omega r^2\sin^2\theta$ and the position-dependent $g_{(ct)(ct)} = 1 - \omega^2 r^2\sin^2\theta$ appear, yet this is *nothing but* the Minkowski metric expressed in rotating coordinates — the "Langevin metric" is not a new metric. (Verifying that its Riemann tensor vanishes is a calibration of the claim that this is still flat space.)

**Is an instance — null coordinates.** From the spherical $(ct,r,\theta,\varphi)$ set $u := ct-r$, $v := ct+r$. The coordinate basis vectors $\vec{e}_u = \tfrac12(\vec{e}_{ct}-\vec{e}_r)$ and $\vec{e}_v = \tfrac12(\vec{e}_{ct}+\vec{e}_r)$ are *null*: $g_{uu} = g_{vv} = 0$. The metric is $g_{\alpha\beta}$ with $g_{uv} = g_{vu} = \tfrac12$, $g_{\theta\theta} = -r^2$, $g_{\varphi\varphi} = -r^2\sin^2\theta$, and the rest zero — a basis built of two null vectors and two spacelike ones, with no timelike basis vector at all. It is not obvious from this array that the signature is still $(1,3)$, which is the point: signature is a property of the form, not of any one basis.

**Is NOT an instance — the orthonormal spherical frame.** The vectors $\vec{e}'_0 = \vec{e}_{ct}$, $\vec{e}'_1 = \vec{e}_r$, $\vec{e}'_2 = r^{-1}\vec{e}_\theta$, $\vec{e}'_3 = (r\sin\theta)^{-1}\vec{e}_\varphi$ form a perfectly good orthonormal basis at each event — a *tetrad* — but they are **not** a coordinate basis: there is no coordinate system whose natural basis they are. (One can prove this: a coordinate basis must have $[\vec{e}'_\alpha,\vec{e}'_\beta] = 0$, but these have nonzero Lie brackets.) This is the standard example separating "field of bases" (moving frame) from "coordinate basis".

**Corollary — the metric components are not constant in general.** In spherical coordinates $\partial g_{\theta\theta}/\partial r = -2r \neq 0$. This is the trigger for the failure of the naive partial derivative to be tensorial, and hence for the covariant derivative — see [[Def - The Covariant Derivative]].

**Corollary — the dual basis is the gradients of the coordinates.** Because $\langle\mathbf{d}x^\alpha,\overrightarrow{MM'}\rangle = \mathrm{d}x^\alpha = \langle\mathbf{d}x^\alpha, \mathrm{d}x^\beta\vec{e}_\beta\rangle$, one reads off $\langle e^\alpha,\vec{e}_\beta\rangle = \delta^\alpha{}_\beta$ with $e^\alpha = \mathbf{d}x^\alpha = \boldsymbol{\nabla}x^\alpha$. So the gradients of the four coordinate functions are exactly the dual basis of the coordinate basis.

**Calibration check.** You should be able to (i) write the Jacobian of the spherical coordinate change and recover $g_{\theta\theta} = -r^2$; (ii) state why a position-dependent $g_{\alpha\beta}$ does not imply curvature, and name the test (vanishing Riemann tensor); and (iii) explain why the orthonormal spherical frame is a field of bases but not a coordinate basis (zero Lie bracket fails).

---

# Unlocked by This

> [!tip] Charts, Atlases, and Manifolds *(from Differential Geometry)*
> The diffeomorphism $\Phi$ is a **chart**, and the requirement that overlapping charts be smoothly related is the definition of a **smooth manifold**. Flat spacetime is the trivial case (one global chart), but the apparatus developed here — coordinate bases, transformation laws, position-dependent metric components — is exactly what a curved spacetime, which admits no global inertial chart, requires.

> [!tip] The Tangent Space and the Vector-as-Operator Definition *(from Differential Geometry)*
> The identification $\vec{e}_\alpha = \partial/\partial x^\alpha$ is the gateway to the intrinsic definition of a tangent vector as a **derivation on scalar fields**: a vector at $M$ is a directional-derivative operator, and the coordinate vectors $\partial/\partial x^\alpha$ are a basis for the tangent space $T_M\mathscr{E}$. On the affine space this is optional (vectors are honest displacements), but on a general manifold it is the only available definition.

> [!tip] The Metric as a Field, and the Road to Curvature *(from General Relativity)*
> Allowing $g_{\alpha\beta}$ to depend on position is the first half of the step to gravitation; the second half is letting that dependence be *irremovable*. In general relativity $g_{\mu\nu}(x)$ is a dynamical field, and the obstruction to transforming it to $\eta_{\mu\nu}$ everywhere — the second derivatives that cannot be killed — is the **Riemann curvature tensor**. The position-dependent metrics of this page all have zero curvature; the same formalism with nonzero curvature is general relativity. See [[General Relativity I — Einstein's Equations and Schwarzschild]].
