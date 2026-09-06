---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Tensor Field on a Manifold"
  - "Def - Symmetric Tensor Field"
  - "Def - The Tangent Space"
  - "Def - Inner Product Space"
  - "Def - Bilinear Form"
tags: [geometry, differential-geometry, riemannian-geometry]
---

# Notation

Let $M$ be a smooth $n$-manifold. We write $g$ for a Riemannian metric. In local coordinates $x^i$ on a chart $U$, the components are $g_{ij}(x) = g_p(\partial_i, \partial_j)$, a smooth symmetric positive-definite matrix-valued function. The inverse matrix is $g^{ij}(x)$, defined by $g^{ij}g_{jk} = \delta^i_k$. The pair $(M, g)$ is a [[Def - Riemannian Manifold|Riemannian manifold]]. The length of a tangent vector $v \in T_pM$ is $|v|_g = \sqrt{g_p(v, v)}$, and the inner product on $T_pM$ is $\langle v, w\rangle_g = g_p(v, w)$. Full registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

---

# Axiom Motivation

The desideratum is simple: we want to install on a manifold the geometric notions of *length*, *angle*, and *distance*, which are absent from the bare smooth structure. We already know how to do this on a single vector space — an [[Def - Inner Product Space|inner product]] does the whole job. So the natural plan is: place an inner product in every tangent space $T_pM$, and require that it vary smoothly with $p$ so that the resulting structure is compatible with the calculus already in place. A Riemannian metric is precisely this. The three axioms — smoothness, symmetry, positive-definiteness — are not arbitrary; each one is forced by what the structure must do.

**Why a $(0,2)$-tensor field?** The geometric input we want is, at each $p$, a function $T_pM \times T_pM \to \mathbb{R}$ — taking two tangent vectors and producing a number, the inner product. That is a $\mathbb{R}$-bilinear map on a vector space, which is exactly a $(0,2)$-tensor on $T_pM$ ([[Def - Covariant Tensor on a Vector Space]]). Bundling these together as $p$ varies gives a section of the $(0,2)$-tensor bundle $T^{(0,2)}M = T^*M \otimes T^*M$ — a [[Def - Tensor Field on a Manifold|tensor field of type (0,2)]]. So the type "$(0,2)$-tensor field" is forced the instant we decide each $T_pM$ should carry a bilinear "inner-product-shaped" pairing.

**Why symmetric?** An inner product $\langle v, w \rangle = \langle w, v \rangle$ on a real vector space is symmetric — this is part of the standard definition. Geometrically, the symmetry says that "the angle from $v$ to $w$" equals "the angle from $w$ to $v$", which is what one means by an angle on an unoriented pair of vectors. If we dropped symmetry, we would have a general bilinear form, which is the sum of a symmetric part (an inner product candidate) and an antisymmetric part (a 2-form). The antisymmetric part records oriented area but cannot record length — $\omega(v, v) = 0$ for any antisymmetric $\omega$ — so it carries no information about $|v|$. Concretely, dropping symmetry would put symplectic-structure data on the tangent spaces instead of inner-product data, and the resulting object would not be a metric. Symmetry is what guarantees that the diagonal $g_p(v, v)$ is the right quantity to call "length-squared".

**Why positive-definite?** Positive-definiteness — $g_p(v, v) > 0$ for every nonzero $v$ — is what makes $|v|_g = \sqrt{g_p(v, v)}$ a well-defined non-negative number, with $|v|_g = 0$ if and only if $v = 0$. Drop positive-definiteness and you get a [[Def - Semi-Riemannian Metric and Signature|semi-Riemannian metric]], which is non-degenerate but indefinite; the diagonal $g_p(v, v)$ can be negative or zero on nonzero vectors, and the "length" of a vector is no longer a real number for every $v$. This is not a defect — it is exactly what one wants for relativistic spacetime, where the indefiniteness produces the light cone. But for the *Riemannian* setting where the goal is honest "distance and length", positive-definiteness is essential: it is what makes $g$ an inner product in the strict sense, what makes the [[Def - Length of a Curve and Riemannian Distance|Riemannian distance function]] a real-valued metric, and what makes the [[Thm - The Riemannian Distance Makes M a Metric Space|Riemannian-manifolds-are-metric-spaces]] theorem true. The whole point of the chapter's distinction between "Riemannian" and "semi-Riemannian" is the presence or absence of this single axiom.

A second way to see why positive-definiteness is essential: the existence proof for Riemannian metrics ([[Thm - Existence of Riemannian Metrics via Partitions of Unity]]) uses partitions of unity. The argument relies on the fact that a positive convex combination of positive-definite forms is positive-definite — this is geometrically the convexity of the set of inner products in the space of all $(0,2)$-tensors. The same argument *fails* for non-degenerate indefinite forms: a positive convex combination of two indefinite forms can be degenerate or change signature, so partitions of unity cannot patch local indefinite metrics into a global one. Positive-definiteness is exactly the property that makes the partition-of-unity construction work, which is why every smooth manifold admits a Riemannian metric but not every one admits a Lorentzian one (see [[Thm - A Lorentzian Manifold Need Not Exist on Every Smooth Manifold]]).

**Why smooth?** A "$(0,2)$-tensor field" on a manifold is by default a section of the tensor bundle — possibly only continuous. Smoothness — the components $g_{ij}(x)$ being $C^\infty$ in any (equivalently every) chart — is required so that the calculus we want to build on top of $g$ goes through. The musical isomorphism uses $g^{ij}$, the inverse matrix, which is smooth when $g_{ij}$ is smooth (and non-degenerate, which positive-definiteness guarantees pointwise). The gradient $\mathrm{grad}\, f = g^{ij}\partial_j f\, \partial_i$ involves derivatives. The Christoffel symbols $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$ — the entry point to all of [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|the Levi-Civita connection]] — involve first derivatives of $g_{ij}$. The Riemann curvature involves second derivatives. To have any of this, $g$ must be $C^\infty$. Dropping smoothness — for instance allowing $g_{ij}$ to be only $C^k$ — restricts how many derivatives of curvature one can take, and is a serious technical limitation; one routinely works in higher-regularity classes ($C^k$, $C^{k,\alpha}$, $W^{k,p}$) in PDE-flavored Riemannian geometry, but the default is full smoothness.

A useful forward reference: the [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|fundamental theorem of Riemannian geometry]] asserts the existence and uniqueness of a torsion-free metric-compatible connection. The uniqueness part — that *only one* such connection exists — uses each of the three axioms: symmetry of $g$ is needed for the Koszul formula's symmetrisation, positive-definiteness (more precisely non-degeneracy) is needed to "solve for" $\nabla_X Y$ from $g(\nabla_X Y, Z)$, and smoothness is needed for the resulting connection to be smooth. If you weaken any one axiom, the fundamental theorem fails or changes form. This is a good calibration check: the definition is tuned to make the theorem true.

---

# The Definition

> **Definition (Riemannian Metric).** Let $M$ be a smooth manifold. A **Riemannian metric** on $M$ is a smooth covariant $2$-tensor field $g \in \Gamma(T^*M \otimes T^*M)$ that is, at every point $p \in M$:
>
> (i) **symmetric**: $g_p(v, w) = g_p(w, v)$ for all $v, w \in T_pM$;
>
> (ii) **positive-definite**: $g_p(v, v) > 0$ for every nonzero $v \in T_pM$.

Equivalently, $g$ assigns to each $p \in M$ an [[Def - Inner Product Space|inner product]] $g_p$ on $T_pM$, with smooth dependence on $p$.

In local coordinates $(x^i)$ on a chart $U \subseteq M$, $g$ has the expression
$$
g = g_{ij}(x)\, dx^i \otimes dx^j = \tfrac{1}{2}\bigl(g_{ij}(x) + g_{ji}(x)\bigr) dx^i \otimes dx^j,
$$
where $g_{ij}(x) = g_p(\partial_i|_p, \partial_j|_p)$ is a smooth, symmetric, positive-definite matrix-valued function. By symmetry one also writes $g = g_{ij}\, dx^i\, dx^j$ with the convention that $dx^i\, dx^j$ denotes the symmetric product $\tfrac{1}{2}(dx^i \otimes dx^j + dx^j \otimes dx^i)$, so that
$$
g\bigl(\textstyle\sum_i a^i \partial_i,\ \sum_j b^j \partial_j\bigr) = g_{ij}\, a^i b^j.
$$

The **inverse metric** $g^{-1}$ is the $(2, 0)$-tensor field with components $g^{ij}(x)$, the matrix inverse of $g_{ij}(x)$, characterised by $g^{ij} g_{jk} = \delta^i_k$. Equivalently, $g^{-1}$ is the symmetric bilinear form on $T_p^*M$ corresponding to $g_p$ under the musical isomorphism (see [[Def - Musical Isomorphism (Flat and Sharp)]]).

A **Riemannian manifold** is a pair $(M, g)$ where $M$ is a smooth manifold and $g$ is a Riemannian metric on $M$; see [[Def - Riemannian Manifold]].

---

# Categorical / Structural Definition

A Riemannian metric is, structurally, a **fibre metric** on the tangent bundle $TM \to M$ — that is, a smooth choice of inner product on each fibre. More categorically, write $\mathrm{SymBil}^+(V)$ for the space of positive-definite symmetric bilinear forms on a real vector space $V$ (a convex open cone in $\mathrm{Sym}(V^* \otimes V^*)$). The smooth bundle $\mathrm{SymBil}^+(TM) \to M$ has fibre $\mathrm{SymBil}^+(T_pM)$ over $p$, and a Riemannian metric is precisely a smooth global section of this bundle. The convexity of each fibre is exactly what makes the [[Thm - Existence of Riemannian Metrics via Partitions of Unity|partition-of-unity construction]] of a global section possible.

From the perspective of vector bundles, a Riemannian metric is a special case of a **bundle metric** on a smooth real vector bundle $E \to M$ — a smooth section of $\mathrm{Sym}^2(E^*)$ that is fibrewise positive-definite. The same construction (cover, pull back the Euclidean metric on local trivialisations, partition-of-unity gluing) shows that *every* smooth real vector bundle over a paracompact base admits a bundle metric. The Riemannian metric is the case $E = TM$.

Yet another perspective: a Riemannian metric on $M$ is the same data as a **reduction of the structure [[Def - Group|group]]** of $TM$ from $GL(n, \mathbb{R})$ to the orthogonal group $O(n)$. The unreduced principal $GL(n, \mathbb{R})$-bundle is the frame bundle $F(M)$; reducing to $O(n)$ amounts to selecting at each point an *orthonormal* frame, equivalent to selecting an inner product on each tangent space. This perspective generalises: a [[Def - Lorentzian Manifold|Lorentzian metric]] is a reduction to $O(1, n-1)$, a complex structure is a reduction to $GL(n/2, \mathbb{C})$, a Hermitian metric is a reduction to $U(n/2)$, a symplectic structure is a reduction to $Sp(n)$, and so on. Each "extra geometric structure" on a manifold is a structure-group reduction of the frame bundle, and the Riemannian case is the most basic.

---

# Relate to Other Fields / Compression

This is the smooth-manifold version of "[[Def - Inner Product Space|inner product space]]", parametrised by a point of the manifold. Where linear algebra studies a single inner product on a single vector space, Riemannian geometry studies a smoothly varying family of inner products on the tangent spaces of $M$. Every theorem of inner-product linear algebra — Cauchy–Schwarz, Gram–Schmidt, the dual-space isomorphism, the spectral theorem for self-adjoint operators — applies pointwise at every $T_pM$. The new content is the smoothness of the variation in $p$ and the global geometric structures (length, distance, geodesics, curvature) that depend on derivatives of $g$.

The connection to [[Def - Bilinear Form|bilinear forms]]: a Riemannian metric is, pointwise, a positive-definite symmetric bilinear form on $T_pM$. The space of symmetric bilinear forms on a fixed $V$ is the symmetric square $\mathrm{Sym}^2(V^*)$, and the positive-definite ones form an open convex subset. A Riemannian metric is a smooth section of the bundle whose fibres are this open convex set.

The connection to physics: in continuum mechanics, the metric is the "first fundamental form" of the configuration space; in general relativity, the metric is the dynamical gravitational field; in fluid dynamics on a Riemannian manifold, the metric provides the inner product needed to define divergence and the Laplace–Beltrami operator that drives the Navier–Stokes equations.

**True name:** A Riemannian metric is *a smoothly varying inner product on tangent spaces*. The official "smooth, symmetric, positive-definite $(0,2)$-tensor field" is the right thing to write in a definition, but the operational picture is the inner-product-per-tangent-space picture: at every $p$ there is a real, honest inner product $\langle\cdot,\cdot\rangle_p$ on $T_pM$, varying smoothly with $p$, and *that* is what one computes with.

---

# Examples / Corollaries

**Is an instance — the Euclidean metric on $\mathbb{R}^n$.** The standard Euclidean metric is $\bar g = \sum_{i=1}^n dx^i \otimes dx^i$, with components $g_{ij} = \delta_{ij}$. It is smooth (constant), symmetric, and positive-definite ($\bar g_p(v, v) = \sum (v^i)^2 \geq 0$, zero iff $v = 0$). The induced inner product is the usual dot product, the induced norm is the usual Euclidean norm, and the induced distance is the usual Euclidean distance.

**Is an instance — the round metric on $S^n$.** The induced metric from the inclusion $S^n \hookrightarrow \mathbb{R}^{n+1}$ is the round metric $\mathring g$. In spherical coordinates on $S^2$, $\mathring g = d\theta^2 + \sin^2\theta\, d\varphi^2$ (see [[Ex - The Round Metric on the Sphere via Restriction]]). The factor $\sin^2\theta$ in the coordinate matrix is what makes the sphere *curved* — it is not the constant matrix.

**Is an instance — the hyperbolic metric on the upper half-plane.** On $\mathbb{H}^2 = \{(x, y) : y > 0\}$, the metric $g_{\mathbb{H}} = (dx^2 + dy^2)/y^2$ is smooth (the singular set $y = 0$ is excluded), symmetric, and positive-definite (proportional to the Euclidean metric by a positive scalar function); see [[Ex - The Hyperbolic Plane as a Riemannian Manifold]]. The hyperbolic plane is the prototypical constantly negatively-curved Riemannian manifold.

**Is an instance — the flat metric on a torus.** On $T^n = \mathbb{R}^n / \mathbb{Z}^n$, the quotient of the Euclidean metric is well-defined (the metric is translation-invariant, so it descends to the quotient) and gives the flat metric on $T^n$. As a Riemannian manifold, $T^n$ with this metric is *flat* — locally isometric to Euclidean space — even though it is topologically not $\mathbb{R}^n$.

**Is NOT an instance — the Minkowski metric on $\mathbb{R}^4$.** The Minkowski metric $\eta = dt^2 - dx^2 - dy^2 - dz^2$ on $\mathbb{R}^4$ is smooth and symmetric, but *not* positive-definite: $\eta_p(v, v) < 0$ for any spacelike vector, and $\eta_p(v, v) = 0$ for any null vector with $v \neq 0$. It is a [[Def - Semi-Riemannian Metric and Signature|semi-Riemannian metric]] of signature $(1, 3)$ — a [[Def - Lorentzian Manifold|Lorentzian metric]] — but not a Riemannian one. The geometry of $(\mathbb{R}^4, \eta)$ is [[Def - Minkowski Space and the Metric|Minkowski space]], the setting of [[Special Relativity I — Postulates and Lorentz Transformations|special relativity]].

**Is NOT an instance — a positive semi-definite but degenerate form.** The "metric" $g = dx^2$ on $\mathbb{R}^2$ (only the first coordinate contributes) is smooth and symmetric, but degenerate: $g(\partial_y, v) = 0$ for every $v$, so $\partial_y$ has zero "length" while being nonzero. This is not a Riemannian metric, nor even a semi-Riemannian one — it is a *degenerate* symmetric bilinear form. Such forms appear in the geometry of Carnot [[Def - Group|groups]] and sub-Riemannian geometry, where the metric is only defined on a [[Def - Subbundle|subbundle]] (a distribution), but they are not the subject of Riemannian or semi-Riemannian geometry.

**Corollary — every smooth manifold admits a Riemannian metric.** The proof via partition of unity is the content of [[Thm - Existence of Riemannian Metrics via Partitions of Unity]]. This is striking because *most* additional geometric structures are obstructed (a Lorentzian metric, an almost complex structure, an orientation, a non-vanishing vector field can all fail to exist on a given manifold). The Riemannian metric is the universally available one.

**Corollary — different Riemannian metrics on the same manifold can be genuinely different.** The same smooth $S^2$ carries the round metric and many distorted metrics (any smooth deformation), and they are *not* isometric in general — the round metric is rotationally symmetric and has constant curvature, while a distorted one is not and does not. The smooth structure determines the manifold *as a manifold*; the metric determines its *geometry*. This is the central insight of the chapter: smooth structure and metric structure are genuinely separate layers.

**Corollary — the metric raises and lowers indices.** Non-degeneracy (a consequence of positive-definiteness) means $g_{ij}$ has an inverse $g^{ij}$, and the musical [[Def - Isomorphism|isomorphisms]] $\flat : T_pM \to T_p^*M$ and $\sharp : T_p^*M \to T_pM$ are bijections defined by $X_i = g_{ij}X^j$ and $\omega^i = g^{ij}\omega_j$ (see [[Def - Musical Isomorphism (Flat and Sharp)]]). This is the formal mechanism for the index gymnastics universally used in tensor calculus.

**Calibration check.** If you have understood the definition, you should be able to verify each of the following. First, the metric $g = e^{2u(x)}(dx_1^2 + \cdots + dx_n^2)$ for any smooth $u : \mathbb{R}^n \to \mathbb{R}$ is a Riemannian metric on $\mathbb{R}^n$ (a *conformally flat* metric); positive-definiteness follows from the positivity of the conformal factor $e^{2u}$. Second, the metric tensor of the cylinder $\{(x, y, z) : x^2 + y^2 = 1\}$ in cylindrical coordinates $(\theta, z)$ is $d\theta^2 + dz^2$, the same as the Euclidean metric on $\mathbb{R}^2$ — the cylinder is flat. Third, if $g_1$ and $g_2$ are Riemannian metrics on $M$ and $t \in [0, 1]$, then $tg_1 + (1-t)g_2$ is again a Riemannian metric on $M$ (the convexity of the positive-definite cone).

---

# Unlocked by This

> [!tip] The Riemannian Distance Function *(from §12.2)*
> Given a Riemannian metric, every piecewise smooth curve $\gamma$ has a well-defined length $L_g(\gamma) = \int |\dot\gamma|_g\, dt$, and the [[Def - Length of a Curve and Riemannian Distance|Riemannian distance]] $d_g(p, q) = \inf L_g$ over piecewise smooth curves makes $M$ into a metric space. The smooth field of inner products has produced an honest metric, with topology coinciding with the manifold topology — the unification of point-set topology and differential geometry.

> [!tip] The Musical Isomorphism *(from §12.3)*
> The metric induces canonical isomorphisms $\flat : TM \to T^*M$ and $\sharp : T^*M \to TM$ ([[Def - Musical Isomorphism (Flat and Sharp)]]). With these, the gradient of a smooth function becomes a vector field rather than a covector field, and every tensor type can be converted to every other by raising and lowering indices.

> [!tip] The Levi-Civita Connection *(from Riemannian Geometry)*
> The single most important consequence of having a Riemannian (or semi-Riemannian) metric is the [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|fundamental theorem of Riemannian geometry]]: there is a unique torsion-free, metric-compatible connection $\nabla$ on $TM$, the **Levi-Civita connection**. From it come the **Christoffel symbols** $\Gamma^k_{ij}$, the **geodesic equation** $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$, parallel transport, the Riemann curvature tensor, sectional curvature, Ricci curvature, and the entire subsequent development of Riemannian geometry. The metric does not merely give length — it determines, uniquely and canonically, *how to differentiate vector fields along curves*, and the whole curvature theory is the unfolding of consequences of this single fact.

> [!tip] The Riemannian Volume Form *(from Differential Geometry IX)*
> On an oriented Riemannian manifold, the metric induces a canonical [[Def - Riemannian Volume Form|volume form]] $dV_g$ — locally $\sqrt{\det g_{ij}}\, dx^1 \wedge \cdots \wedge dx^n$. This is the form one integrates a function against, and it converts every Riemannian manifold into a measure space. The Euclidean volume form $dx^1 \wedge \cdots \wedge dx^n$ on $\mathbb{R}^n$ is the special case $g_{ij} = \delta_{ij}$.

> [!tip] Information Geometry *(from Applied Probability and Statistics)*
> A parametric family of probability distributions $\{p(x; \theta)\}_{\theta \in \Theta \subseteq \mathbb{R}^k}$ has a canonical Riemannian metric on $\Theta$, the **Fisher information metric** $g_{ij}(\theta) = \mathbb{E}_{p_\theta}[\partial_i \log p \cdot \partial_j \log p]$. This is the metric for which the Cramér–Rao bound and the asymptotic distribution of the maximum likelihood estimator are clean, and the study of statistical models as Riemannian manifolds is **information geometry** (Amari's program). The bridge: a Riemannian metric is exactly what makes "infinitesimal distinguishability" of probability distributions a quantitative notion.
