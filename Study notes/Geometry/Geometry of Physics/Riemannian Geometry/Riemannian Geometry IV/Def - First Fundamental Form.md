---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Embedded Submanifold"
  - "Def - Tangent Space of a Submanifold"
  - "Def - Riemannian Metric"
  - "Def - Induced Metric on a Submanifold"
tags: [geometry, riemannian-geometry, surfaces, metric]
---

# Notation

Let $M \subset \mathbb{R}^3$ be an oriented regular $2$-dimensional submanifold (a regular surface), thought of locally as the image $M = F(U)$ of a parametrisation $F : U \subset \mathbb{R}^2 \to \mathbb{R}^3$ with $F_*$ of rank $2$. We write $(u, v) = (u^1, u^2)$ for local coordinates on $U$, $\mathbf{x}(u, v) = F(u, v)$ for the position vector, and $\mathbf{x}_\alpha = \partial \mathbf{x}/\partial u^\alpha$ ($\alpha = 1, 2$) for the coordinate tangent vectors. The Euclidean inner product on $\mathbb{R}^3$ is $\langle\cdot,\cdot\rangle$. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Axiom Motivation

The desideratum is to install on a surface in $\mathbb{R}^3$ the geometric notions one already has for curves in space — length, angle between intersecting curves, area of regions — using *only the surface itself*, not the ambient $3$-space. A surface inhabitant, say a two-dimensional creature crawling along $M$, can measure each of these with a tape measure stretched along the surface; the question is what mathematical structure on $M$ encodes everything they can measure. The answer is a single symmetric, positive-definite, smooth bilinear form on each tangent space — exactly an [[Def - Inner Product Space|inner product]] varying smoothly with the point — and this is what we call the first fundamental form.

**Why a bilinear form, not just a quadratic form?** A quadratic form $Q : T_pM \to \mathbb{R}$, $v \mapsto |v|^2$, suffices to compute lengths of vectors. But to compute *angles between vectors* — which a surface inhabitant certainly needs — we need a *bilinear* form $\langle\cdot,\cdot\rangle$ from which $|v|^2 = \langle v, v\rangle$ and the cosine of the angle between $u, v$ is $\langle u, v\rangle/|u||v|$. Bilinearity and symmetry are forced by what an inner product *is*. Without bilinearity, the parallelogram law fails and one cannot reconstruct angles from lengths. Without symmetry, the angle from $u$ to $v$ would differ from the angle from $v$ to $u$, which is geometrically absurd.

**Why positive-definite?** The length of a nonzero tangent vector must be a strictly positive real number — otherwise the metric structure degenerates and there are tangent directions in which "nothing happens", which contradicts the surface being a regular $2$-submanifold (every nonzero $v \in T_pM$ should have $|v| > 0$). Positive-definiteness of $\mathrm{I}$ at $p$ follows from positive-definiteness of the Euclidean inner product on $\mathbb{R}^3$ restricted to the $2$-plane $T_pM$: the restriction of a positive-definite form to any subspace is positive-definite. If we dropped positive-definiteness — allowing a tangent vector with $|v|^2 \leq 0$ — we would no longer be doing Riemannian geometry; we would be in the realm of [[Def - Lorentzian Manifold|Lorentzian manifolds]] like Minkowski space, where the light-cone structure replaces honest distance.

**Why smoothness in $p$?** The components $g_{\alpha\beta}(u) = \langle\mathbf{x}_\alpha(u), \mathbf{x}_\beta(u)\rangle$ are smooth functions on $U$ because $\mathbf{x}$ is smooth and the Euclidean inner product is bilinear. Smoothness is needed downstream: the Christoffel symbols (which involve first derivatives of $g_{\alpha\beta}$), the Riemann curvature (which involves second derivatives), and the geodesic equation (with both) all require enough derivatives of $g$. Anything less than $C^2$ would break the formula $K = R_{1212}/\det g$ of the Theorema Egregium, so $C^\infty$ is the natural setting and we lose nothing by demanding it.

**The forced form of the definition.** The above three requirements — bilinear-symmetric, positive-definite, smooth — uniquely characterise a Riemannian metric on $M$, and *the* natural such metric on a surface in $\mathbb{R}^3$ is the **restriction of the Euclidean inner product** to tangent spaces. There is essentially no choice once one wishes the metric to be compatible with how curves in $M$ inherit length from curves in $\mathbb{R}^3$. The first fundamental form is the [[Def - Induced Metric on a Submanifold|induced metric]] applied to the case of a $2$-submanifold of $\mathbb{R}^3$, with one important feature: in this concrete embedded setting one can compute the components $g_{\alpha\beta}$ explicitly as inner products $\langle\mathbf{x}_\alpha, \mathbf{x}_\beta\rangle$ of the coordinate derivative vectors. This explicit formula is what makes the surface case the computational laboratory for all of Riemannian geometry.

A forward reference: the [[Thm - Theorema Egregium of Gauss|Theorema Egregium]] depends crucially on the first fundamental form being defined intrinsically — that is, that lengths and angles on $M$ depend only on $g_{\alpha\beta}$ and not on how $M$ sits in $\mathbb{R}^3$. If the metric were somehow defined to use the ambient embedding directly (rather than its restriction to $T_pM$), Theorema Egregium would be vacuous. The strict separation of "intrinsic data" ($g_{\alpha\beta}$) from "extrinsic data" (the second fundamental form, see [[Def - Second Fundamental Form]]) is precisely what makes the theorem possible.

---

# The Definition

> **Definition (First Fundamental Form).** Let $M \subset \mathbb{R}^3$ be a regular surface and $p \in M$. The **first fundamental form** at $p$ is the bilinear form $\mathrm{I}_p : T_pM \times T_pM \to \mathbb{R}$ obtained by restricting the Euclidean inner product to $T_pM \subset \mathbb{R}^3$:
> $$
> \mathrm{I}_p(X, Y) := \langle X, Y\rangle_{\mathbb{R}^3}, \quad X, Y \in T_pM.
> $$
> The family $\{\mathrm{I}_p\}_{p \in M}$ assembles into a smooth, symmetric, positive-definite $(0,2)$-tensor field on $M$ — the [[Def - Riemannian Metric|Riemannian metric]] $g$ induced from $\mathbb{R}^3$.

In a local parametrisation $\mathbf{x}(u, v)$ with coordinate tangents $\mathbf{x}_\alpha = \partial \mathbf{x}/\partial u^\alpha$, the components are
$$
g_{\alpha\beta}(u, v) = \langle\mathbf{x}_\alpha, \mathbf{x}_\beta\rangle,
$$
and the form is
$$
\mathrm{I} = g_{\alpha\beta}\, du^\alpha\, du^\beta.
$$
In Gauss's classical notation (which omits indices),
$$
\mathrm{I} = E\, du^2 + 2F\, du\, dv + G\, dv^2,
\qquad E = g_{11},\;\; F = g_{12} = g_{21},\;\; G = g_{22}.
$$
The matrix $\bigl(\begin{smallmatrix} E & F \\ F & G \end{smallmatrix}\bigr)$ is the Gram matrix of $(\mathbf{x}_u, \mathbf{x}_v)$, and its determinant $EG - F^2 = |\mathbf{x}_u \times \mathbf{x}_v|^2$ is strictly positive by the regularity assumption ($F_*$ has rank $2$).

The induced **arc length** of a curve $\gamma(t) = \mathbf{x}(u(t), v(t))$ on $M$ is
$$
L(\gamma) = \int_a^b \sqrt{g_{\alpha\beta}(u(t))\dot u^\alpha(t)\dot u^\beta(t)}\, dt = \int_a^b\sqrt{E\dot u^2 + 2F\dot u\dot v + G\dot v^2}\, dt.
$$
The **angle** between two intersecting curves with tangents $X, Y$ at $p$ is $\cos\theta = \mathrm{I}_p(X, Y)/\sqrt{\mathrm{I}_p(X,X)\mathrm{I}_p(Y,Y)}$. The **area** of a region $D \subset U$ is $\mathrm{Area}(D) = \iint_D\sqrt{EG - F^2}\, du\, dv = \iint_D\sqrt{\det g_{\alpha\beta}}\, du\, dv$.

---

# Categorical / Structural Definition

Structurally, the first fundamental form is the **pullback** of the Euclidean metric along the inclusion $\iota : M \hookrightarrow \mathbb{R}^3$:
$$
\mathrm{I} = \iota^*\bar g_{\mathbb{R}^3},
$$
where $\bar g_{\mathbb{R}^3} = \sum_{i=1}^3 dx^i \otimes dx^i$ is the standard Euclidean metric on $\mathbb{R}^3$. Pullback by an immersion sends a symmetric positive-definite tensor to a symmetric positive-definite tensor on the source (because $\iota_*$ is injective on tangent spaces), and that pullback is the canonical induced metric.

This is the special case of the general [[Def - Induced Metric on a Submanifold|induced metric on a submanifold]] applied to a $2$-submanifold of $(\mathbb{R}^3, \bar g)$. The same construction gives an induced metric on any submanifold of any Riemannian manifold: pull the ambient metric back along the inclusion. The richness of surface theory comes from working out the consequences of this single pullback in painstaking detail.

A functorial way to package the data: the assignment $M \mapsto (M, \iota^*\bar g)$ is a functor from the category of regular surfaces (with smooth maps preserving the embedding) to the category of Riemannian $2$-manifolds. The Theorema Egregium says certain invariants — notably $K$ — *factor through this functor*: they depend only on the Riemannian-manifold image, not on the embedded-surface preimage.

---

# Relate to Other Fields / Compression

The first fundamental form is **the metric tensor of the induced Riemannian structure** — it is the same object as a [[Def - Riemannian Metric|Riemannian metric]] $g$ on the abstract manifold $M$, with the historical name "first fundamental form" surviving from Gauss's 1827 work and now used almost exclusively in surface theory.

In **linear algebra**, $\mathrm{I}_p$ at a fixed point $p$ is just an inner product on a real two-dimensional vector space $T_pM$ — i.e., a positive-definite symmetric bilinear form. The choice of basis $(\mathbf{x}_u, \mathbf{x}_v)$ gives the Gram matrix $\bigl(\begin{smallmatrix}E&F\\F&G\end{smallmatrix}\bigr)$. Gram–Schmidt at each $p$ would produce an orthonormal frame, but in general such a frame cannot be chosen smoothly globally — the obstruction is precisely the **non-vanishing** of the Euler characteristic / parallelisability of $M$.

In **differential topology**, the first fundamental form is the simplest piece of "geometric data" on a manifold: it converts a smooth manifold into a metric space (length, distance), and from this distance topology one recovers the original manifold topology ([[Thm - The Riemannian Distance Makes M a Metric Space]]).

**True name:** The first fundamental form is *the inner product that an inhabitant of $M$ uses*. The official "restriction of the Euclidean inner product" is the right formal definition, but the operational picture is "the geometric data needed to measure lengths, angles, and areas without leaving the surface". Whenever Theorema Egregium or any other intrinsic argument is invoked, this is the relevant picture: $\mathrm{I}$ encodes exactly what a two-dimensional being can know.

---

# Examples / Corollaries

**Is an instance — the plane $\mathbb{R}^2$.** With the obvious parametrisation $\mathbf{x}(u, v) = (u, v, 0)$, $\mathbf{x}_u = (1, 0, 0)$, $\mathbf{x}_v = (0, 1, 0)$, so $E = G = 1$, $F = 0$, and $\mathrm{I} = du^2 + dv^2$. This is the standard flat metric; arc length $L = \int\sqrt{\dot u^2 + \dot v^2}\, dt$ is the usual Euclidean length.

**Is an instance — the sphere of radius $a$.** With spherical parametrisation $\mathbf{x}(\theta, \varphi) = (a\sin\theta\cos\varphi, a\sin\theta\sin\varphi, a\cos\theta)$, one computes $E = a^2$, $F = 0$, $G = a^2\sin^2\theta$, so $\mathrm{I} = a^2(d\theta^2 + \sin^2\theta\, d\varphi^2)$. The infinitesimal Pythagorean rule visible in this expression — $ds = a\, d\theta$ along meridians and $a\sin\theta\, d\varphi$ along parallels — is the geometry of the round metric. See [[Ex - Gauss Curvature of the Sphere of Radius R is 1 over R Squared]].

**Is an instance — the cylinder.** With $\mathbf{x}(u, v) = (a\cos u, a\sin u, v)$, $\mathbf{x}_u = (-a\sin u, a\cos u, 0)$, $\mathbf{x}_v = (0, 0, 1)$, so $E = a^2$, $F = 0$, $G = 1$, $\mathrm{I} = a^2\, du^2 + dv^2$. After the change of variable $\tilde u = au$, the metric becomes $d\tilde u^2 + dv^2$ — *flat Euclidean*. So the cylinder is locally isometric to the plane, and Gauss's theorem then forces $K_{\text{cylinder}} = 0$.

**Is an instance — the hyperbolic plane $\mathbb{H}^2$.** Although there is no isometric embedding of the full $\mathbb{H}^2$ in $\mathbb{R}^3$ (Hilbert's theorem), the upper half-plane $\{(x, y) : y > 0\}$ with $\mathrm{I} = (dx^2 + dy^2)/y^2$ is a complete Riemannian $2$-manifold of constant curvature $K = -1$. The first fundamental form makes sense for an *abstract* surface even when no embedding exists.

**Is NOT an instance — a degenerate parametrisation.** If $F : U \to \mathbb{R}^3$ has $F_*$ of rank $1$ at some point (e.g., the "north pole" in spherical coordinates where $\mathbf{x}_\varphi = 0$), then $EG - F^2 = 0$ there, and the matrix $g_{\alpha\beta}$ is degenerate. This is not a counterexample to the *form* being a first fundamental form — it just means the parametrisation breaks down at this point. The first fundamental form exists at every point of the regular surface $M$ (e.g., on the sphere itself, including the poles); only the *coordinate representation* in spherical coordinates fails there.

**Is NOT an instance — a Lorentzian "metric".** The form $du^2 - dv^2$ on $\mathbb{R}^2$ is symmetric and non-degenerate but *not* positive-definite (timelike vectors have $\mathrm{I} < 0$). This is a Lorentzian metric of signature $(1,1)$, not a Riemannian metric, and not a first fundamental form of any surface in *Euclidean* $\mathbb{R}^3$ (though it is the induced metric of a surface in *Minkowski* $\mathbb{R}^{1,2}$).

**Corollary — locally isometric surfaces have the same intrinsic geometry.** If two surfaces have parametrisations giving the same matrix $g_{\alpha\beta}(u, v)$ as a function of coordinates, then they are locally isometric: any curve on one is mapped to a curve of equal length on the other, and every intrinsic invariant (length, angle, area, Gauss curvature) agrees. The plane and cylinder example above is the classic case.

**Corollary — the area form is $dA = \sqrt{EG - F^2}\, du\wedge dv$.** This is the unique top form compatible with the orientation and the metric, equal to $\sqrt{\det g_{\alpha\beta}}\, du\wedge dv$ in any local coordinates. Integration of functions on $M$ uses this form: $\int_M f\, dA = \iint_U f(u, v)\sqrt{EG - F^2}\, du\, dv$.

**Calibration check.** If you have understood the definition, you should be able to verify each of the following. First, that the first fundamental form of the unit sphere in spherical coordinates is $d\theta^2 + \sin^2\theta\, d\varphi^2$, and from this compute the equatorial circumference $\int_0^{2\pi}1\, d\varphi = 2\pi$ (at $\theta = \pi/2$). Second, that a flat torus $\mathbb{R}^2/\mathbb{Z}^2$ — which is *not* isometrically embeddable in $\mathbb{R}^3$ — has first fundamental form $du^2 + dv^2$ in the obvious coordinates, the same as the plane, so the plane and the flat torus are locally isometric (a fact obscured by the fact that the standard "donut" embedding has a *different*, non-flat induced metric). Third, that under a change of parameter $u = u(\tilde u, \tilde v)$, $v = v(\tilde u, \tilde v)$, the metric components transform tensorially as $\tilde g_{\alpha\beta} = (\partial u^\gamma/\partial \tilde u^\alpha)(\partial u^\delta/\partial \tilde u^\beta)g_{\gamma\delta}$.

---

# Unlocked by This

> [!tip] The Second Fundamental Form *(from §4.1)*
> The first fundamental form encodes intrinsic geometry but says nothing about how $M$ curves inside $\mathbb{R}^3$. The extrinsic data is captured by the [[Def - Second Fundamental Form|second fundamental form]] $\mathrm{II}_p(X, Y) = -\langle dN(X), Y\rangle$, which measures how the unit normal $N$ rotates as one moves on the surface. Together $(\mathrm{I}, \mathrm{II})$ determine $M$ up to rigid motion (Bonnet's fundamental theorem of surface theory).

> [!tip] The Riemannian Volume Form *(from Differential Geometry IX)*
> On an oriented Riemannian manifold of any dimension, the metric induces a canonical [[Def - Riemannian Volume Form|volume form]] $dV_g = \sqrt{\det g_{ij}}\, dx^1 \wedge\cdots\wedge dx^n$. The surface area element $dA = \sqrt{EG - F^2}\, du\wedge dv$ is the case $n = 2$. This converts every Riemannian manifold into a measure space, and integrals of functions $\int_M f\, dV_g$ are well-defined.

> [!tip] Geodesics on Surfaces *(from §4.4 and Riemannian Geometry II)*
> The arc-length functional $L(\gamma) = \int\sqrt{g_{\alpha\beta}\dot u^\alpha\dot u^\beta}\, dt$, whose Euler–Lagrange equations are the [[Def - Geodesic|geodesic equation]] $\ddot u^\gamma + \Gamma^\gamma_{\alpha\beta}\dot u^\alpha\dot u^\beta = 0$, is built entirely from $\mathrm{I}$. So geodesics on a surface are determined by the first fundamental form alone — an intrinsic notion — and a flat plane bent into a cylinder has straight lines mapping to helices, with both being geodesics in their respective intrinsic geometries.
