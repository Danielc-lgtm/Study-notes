---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Riemannian Metric"
  - "Def - The Tangent Space"
  - "Def - Cotangent Space and Cotangent Bundle"
  - "Def - Dual Space"
tags: [geometry, differential-geometry, riemannian-geometry]
---

# Notation

Let $(M, g)$ be a Riemannian manifold. The musical isomorphisms are written:

- $\flat : TM \to T^*M$ (flat) — "lowering an index";
- $\sharp : T^*M \to TM$ (sharp) — "raising an index";

with $X^\flat = \flat(X) = g(X, \cdot)$ for a vector $X$ and $\omega^\sharp = \sharp(\omega)$ for a covector $\omega$. In components, $X_i = g_{ij}X^j$ and $\omega^i = g^{ij}\omega_j$. The two are inverse to each other: $(X^\flat)^\sharp = X$ and $(\omega^\sharp)^\flat = \omega$.

The **gradient** of a smooth function $f \in C^\infty(M)$ is $\mathrm{grad}_g f = (df)^\sharp$, a vector field on $M$. The symbols $\flat$ and $\sharp$ are the musical symbols for "flat" (lower the pitch by a semitone) and "sharp" (raise the pitch); mnemonically, $\flat$ lowers an index and $\sharp$ raises it. Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

This is a compound page: it defines two interlocking notions — the flat map and the sharp map — because they are introduced together and inverse to each other.

---

# Axiom Motivation

Without a metric, the tangent bundle $TM$ and the cotangent bundle $T^*M$ are genuinely different objects. They are dual to each other, in the precise sense that $T_p^*M = (T_pM)^*$ — the cotangent space at a point is the algebraic dual of the tangent space at that point. But there is no *canonical* isomorphism between a vector space and its dual: choosing one requires choosing some bilinear pairing, which is extra structure not present in the bare tangent-bundle data.

A Riemannian metric *is* such a bilinear pairing: at each $p$, $g_p$ is a non-degenerate symmetric bilinear form $T_pM \times T_pM \to \mathbb{R}$, and any non-degenerate bilinear form provides a canonical isomorphism between a finite-dimensional vector space and its dual. So a Riemannian metric *is* the data needed to canonically identify $TM$ with $T^*M$.

**The desideratum:** install a canonical isomorphism $TM \cong T^*M$ on a Riemannian manifold, smoothly varying with the base point, in such a way that all the "natural" tensor operations of vector calculus (gradient, divergence, etc.) become available.

**Why $g(v, \cdot)$ and not some other formula?** The cleanest way to associate a covector to a vector via $g$ is to send $v$ to the linear functional $w \mapsto g(v, w)$ — "take the inner product with $v$". This is well-defined for any bilinear form $g$ and is linear in $v$. The map $v \mapsto g(v, \cdot)$ is the *only* natural construction one can write using $g$ and the abstract category-theoretic structure. Any other formula would either ignore $g$ (and be metric-independent) or use $g$ in a more complicated way (and be equivalent up to constants).

**Why is it an isomorphism (not just a homomorphism)?** Non-degeneracy. For a positive-definite (or any non-degenerate) symmetric bilinear form, the map $v \mapsto g(v, \cdot)$ has trivial kernel: if $g(v, w) = 0$ for every $w$, then in particular $g(v, v) = 0$, so $v = 0$ (using positive-definiteness, or just non-degeneracy). A linear map between equal-dimensional vector spaces with trivial kernel is an isomorphism. So $\flat : T_pM \to T_p^*M$ is a vector space isomorphism at every $p$, and assembling these gives a smooth bundle isomorphism $\flat : TM \to T^*M$.

**Why is the inverse computed by $g^{ij}$?** In coordinates, $\flat$ acts as the matrix $g_{ij}$: $X_i = g_{ij}X^j$. The inverse map $\sharp$ acts as the inverse matrix $g^{ij}$: $\omega^i = g^{ij}\omega_j$. This is pure linear algebra — the inverse of a linear map represented by a matrix is represented by the inverse matrix — and the entire content of "raising indices" is matrix inversion.

**Why is this the right way to define the gradient?** In elementary multivariable calculus, the gradient of $f$ on $\mathbb{R}^n$ is "the vector of partial derivatives" $\nabla f = (\partial_1 f, \ldots, \partial_n f)$. This depends on the choice of coordinates — under a coordinate change, the gradient transforms covariantly (like a covector), not contravariantly (like a vector). What is intrinsic is $df = \partial_i f\, dx^i$, the **differential** of $f$, which is a covector field on any smooth manifold. To get a *vector* field (which is what the elementary calculus "gradient" looks like in Cartesian coordinates), we raise the index of $df$ using the metric: $\mathrm{grad}_g f = (df)^\sharp = g^{ij}\partial_j f\, \partial_i$. This is the *correct* manifold-intrinsic notion of gradient, and it agrees with the elementary calculus version exactly when $g = \delta_{ij}$ — that is, in Cartesian coordinates on Euclidean space. In any other coordinates, the inverse metric $g^{ij}$ enters and the formula changes (in polar coordinates on $\mathbb{R}^2$, the gradient has a factor of $1/r^2$ in its $\theta$-component).

**Per-axiom failure analysis.** This is really a single-axiom definition (the non-degeneracy of $g$), but two interpretations:

(a) *Drop positive-definiteness, keep non-degeneracy.* For a semi-Riemannian metric of signature $(p, q)$ with $p + q = n$, $p, q \geq 0$ (see [[Def - Semi-Riemannian Metric and Signature]]), the musical isomorphism still works because $g$ is non-degenerate by hypothesis. The construction is identical, and "raising/lowering indices" on a Lorentzian manifold proceeds with the indefinite metric $\eta_{\mu\nu}$ and its inverse $\eta^{\mu\nu}$. In Minkowski space the inverse metric is $\eta^{\mu\nu} = \mathrm{diag}(1, -1, -1, -1)$ — the same matrix as $\eta_{\mu\nu}$, since $\eta^2 = I$ for this particular form. So raising and lowering swap signs on spacelike components: $v^i = -v_i$ for $i \neq 0$.

(b) *Drop non-degeneracy.* Then the map $v \mapsto g(v, \cdot)$ has a nontrivial kernel, and is not an isomorphism. The construction breaks. This is why one requires non-degeneracy of the metric (positive-definite implies non-degenerate, but the reverse is the relevant requirement).

---

# The Definition

> **Definition (Flat map).** Let $(M, g)$ be a Riemannian manifold (or more generally semi-Riemannian, with $g$ non-degenerate). The **flat map** $\flat : TM \to T^*M$ is the smooth bundle homomorphism defined fibrewise by
> $$
> \flat_p(v) = v^\flat \;:=\; g_p(v, \cdot) \in T_p^*M.
> $$
> Explicitly, $v^\flat(w) = g_p(v, w)$ for all $w \in T_pM$.

In local coordinates $x^i$ with $v = v^i \partial_i \in T_pM$,
$$
v^\flat = v_j\, dx^j, \qquad \text{where} \qquad v_j = g_{ij} v^i.
$$
The operation $v^i \mapsto v_j$ is called **lowering the index** (note the index position drops from upper to lower).

> **Definition (Sharp map).** The **sharp map** $\sharp : T^*M \to TM$ is the inverse of $\flat$. Explicitly, for a covector $\omega \in T_p^*M$, $\omega^\sharp$ is the unique vector $v \in T_pM$ such that $g_p(v, w) = \omega(w)$ for every $w \in T_pM$.

In local coordinates with $\omega = \omega_j\, dx^j$,
$$
\omega^\sharp = \omega^i\, \partial_i, \qquad \text{where} \qquad \omega^i = g^{ij}\omega_j,
$$
with $g^{ij}$ the inverse matrix of $g_{ij}$. The operation $\omega_j \mapsto \omega^i$ is called **raising the index**.

The two maps are mutually inverse: $(v^\flat)^\sharp = v$ and $(\omega^\sharp)^\flat = \omega$. Together they identify $TM$ and $T^*M$ as smoothly isomorphic vector bundles — but the identification depends on the metric $g$, and a different $g$ gives a different identification.

> **Definition (Gradient).** For a smooth function $f \in C^\infty(M)$ on a Riemannian manifold, the **gradient** of $f$ is the vector field
> $$
> \mathrm{grad}_g f \;:=\; (df)^\sharp,
> $$
> the metric dual of the differential $df$. In local coordinates, $(\mathrm{grad}_g f)^i = g^{ij}\partial_j f$, so
> $$
> \mathrm{grad}_g f = g^{ij}\, \partial_j f\, \partial_i.
> $$

The gradient is characterised by the invariant equation $g(\mathrm{grad}_g f, X) = X(f) = df(X)$ for every vector field $X$.

---

# Categorical / Structural Definition

Structurally, $\flat$ is the bundle map induced by the metric tensor $g$ viewed as a section of $T^*M \otimes T^*M$. Pointwise, $g_p$ defines a linear map $T_pM \to T_p^*M$ via $v \mapsto g_p(v, \cdot)$; smoothing in $p$ gives the bundle map $\flat : TM \to T^*M$.

Equivalently, in terms of categorical adjunction: the cotangent space $T_p^*M = (T_pM)^*$ is the dual space, and a non-degenerate symmetric bilinear form $g_p$ on a finite-dimensional vector space $V$ provides a *canonical isomorphism* $V \cong V^*$ via $v \mapsto g_p(v, \cdot)$. The musical isomorphism is this construction parametrised by the point of $M$.

From the perspective of vector bundle [[Def - Isomorphism|isomorphisms]]: the metric $g$ is a smooth section of $\mathrm{Sym}^2(T^*M)$ that is fibrewise non-degenerate, hence determines a bundle isomorphism $TM \cong T^*M$. Equivalently, the metric gives a fibrewise inner product, and the inner product gives the Riesz isomorphism between $T_pM$ and its dual.

A categorical subtlety: the musical isomorphism is *not* a natural transformation in any functorial sense, because there is no canonical metric on a manifold. The choice of $g$ is part of the structure, and the isomorphism depends on it. This is in contrast to the canonical isomorphism $V \cong V^{**}$ between a vector space and its double dual, which is natural with no extra data.

---

# Relate to Other Fields / Compression

This is the smooth-manifold version of the **Riesz representation theorem** for inner-product spaces: in any finite-dimensional inner-product space $(V, \langle\cdot,\cdot\rangle)$, every linear functional $\omega \in V^*$ can be uniquely represented as $\omega(w) = \langle v, w\rangle$ for some $v \in V$. The map $v \mapsto \langle v, \cdot\rangle$ is the canonical isomorphism $V \to V^*$, and its inverse is the Riesz isomorphism $\omega \mapsto v_\omega$. The musical isomorphism is exactly this Riesz isomorphism parametrised by points of the manifold.

In physics, "raising and lowering indices" is the bread-and-butter of tensor calculus. A vector $V^\mu$ has its index raised; lowering it gives a covector $V_\mu = g_{\mu\nu}V^\nu$. The same index "represents" the same geometric object in two forms, and one switches freely between them. This is true on any (pseudo-)Riemannian manifold; in [[Special Relativity I — Postulates and Lorentz Transformations|special relativity]] one raises and lowers with the Minkowski metric $\eta$, and the components flip signs in the spacelike entries.

In functional analysis, the dual-space identification on a Hilbert space (the Riesz representation theorem) is the infinite-dimensional analogue of this construction.

**True name:** The musical isomorphism is *the Riesz isomorphism, parametrised by the point of the manifold and smoothly varying*. Every formula involving "raising or lowering an index" is the matrix expression of this map and its inverse.

---

# Examples / Corollaries

**Is an instance — Euclidean $\mathbb{R}^n$ in Cartesian coordinates.** With $g_{ij} = \delta_{ij}$, the flat map is the identity matrix: $v_i = v^i$. So in Cartesian coordinates on Euclidean space, the components of a vector and its dual covector are numerically identical — this is why elementary calculus does not bother to distinguish them, and why "the gradient is the vector of partial derivatives" *happens* to be correct in Cartesian coordinates. The catch: in any other coordinate system, the metric is not $\delta_{ij}$ and the components do differ.

**Is an instance — Euclidean $\mathbb{R}^2$ in polar coordinates.** With $g = dr^2 + r^2 d\theta^2$, the metric matrix is $g_{ij} = \mathrm{diag}(1, r^2)$ and its inverse is $g^{ij} = \mathrm{diag}(1, 1/r^2)$. For a vector $v = v^r \partial_r + v^\theta \partial_\theta$, lowering gives $v_r = v^r$ and $v_\theta = r^2 v^\theta$. For a covector $\omega = \omega_r\, dr + \omega_\theta\, d\theta$, raising gives $\omega^r = \omega_r$ and $\omega^\theta = \omega_\theta / r^2$. The gradient of $f$ is $\mathrm{grad}\, f = \partial_r f\, \partial_r + (1/r^2)\partial_\theta f\, \partial_\theta$; see [[Ex - Raising and Lowering Indices in Polar Coordinates]].

**Is an instance — Minkowski space.** With $\eta_{\mu\nu} = \mathrm{diag}(1, -1, -1, -1)$, the inverse is $\eta^{\mu\nu} = \mathrm{diag}(1, -1, -1, -1)$ (same matrix). For a four-vector $X^\mu = (X^0, X^1, X^2, X^3)$, the lowered version is $X_\mu = (X^0, -X^1, -X^2, -X^3)$ — sign flips on the spatial components. This is the index gymnastics universal in relativistic physics; see [[Def - Minkowski Space and the Metric]].

**Is NOT an instance — naively identifying $TM$ with $T^*M$ via $\partial_i \leftrightarrow dx^i$.** In a chart, the basis $\partial_i$ of $T_pM$ and the basis $dx^i$ of $T_p^*M$ are *dual bases*: $dx^i(\partial_j) = \delta^i_j$. They look like they should be identified by $\partial_i \mapsto dx^i$, but this identification is only equal to $\flat$ when $g_{ij} = \delta_{ij}$ — when the metric is the standard Euclidean one in this chart. For any other metric (including the Euclidean metric in non-Cartesian coordinates), the musical isomorphism mixes basis vectors. This is the canonical pitfall of working in coordinates.

**Corollary — the gradient of the standard coordinate function $x^k$.** $df = dx^k$, so $(dx^k)^\sharp = g^{kj}\partial_j$. In particular on Euclidean $\mathbb{R}^n$ with Cartesian coordinates, $\mathrm{grad}\, x^k = \partial_k$ — the gradient of the $k$th coordinate is the $k$th coordinate vector. In polar coordinates on $\mathbb{R}^2$, $\mathrm{grad}\, r = \partial_r$ (since $g^{rr} = 1$) but $\mathrm{grad}\, \theta = (1/r^2)\partial_\theta$ (since $g^{\theta\theta} = 1/r^2$).

**Corollary — the gradient is orthogonal to level sets.** For $f \in C^\infty(M)$, if $\gamma : I \to M$ is a curve with $f \circ \gamma =$ const (so $\gamma$ lies in a level set of $f$), then $0 = (f \circ \gamma)'(t) = df(\dot\gamma) = g(\mathrm{grad}\, f, \dot\gamma)$. So $\mathrm{grad}\, f$ is $g$-orthogonal to every tangent vector to a level set, hence to the level set itself.

**Corollary — the gradient points in the direction of steepest increase.** Among unit tangent vectors $v \in T_pM$ with $g_p(v, v) = 1$, the directional derivative $v(f) = g(\mathrm{grad}\, f, v)$ is maximised when $v$ is the unit vector in the direction of $\mathrm{grad}\, f$, and the maximum value is $|\mathrm{grad}\, f|_g$.

**Calibration check.** First, verify that for the Euclidean metric on $\mathbb{R}^2$ in Cartesian coordinates, $X^\flat = X^1 dx + X^2 dy$ for $X = X^1\partial_x + X^2\partial_y$ — the components are unchanged, only the basis labels flip. Second, on the sphere $(S^2, \mathring g)$ with $\mathring g = d\theta^2 + \sin^2\theta\, d\varphi^2$, compute the gradient of $f(\theta, \varphi) = \cos\theta$ (the "$z$-coordinate" function). Expected: $\mathrm{grad}\, f = -\sin\theta\, \partial_\theta$, with no $\partial_\varphi$ component because $\partial_\varphi f = 0$. Third, on the upper-half-plane $\mathbb{H}^2$ with $g = (dx^2 + dy^2)/y^2$, the inverse metric is $g^{ij} = y^2 \delta^{ij}$; compute the gradient of $f(x, y) = y$. Expected: $\mathrm{grad}\, f = y^2 \partial_y$ — note the factor of $y^2$, which is the inverse metric coefficient.

---

# Unlocked by This

> [!tip] The Laplace–Beltrami Operator *(from Riemannian Geometry and Harmonic Analysis)*
> Combined with the divergence (which uses both the metric and the Riemannian volume form), the gradient gives the **Laplace–Beltrami operator** $\Delta_g f = \mathrm{div}(\mathrm{grad}_g f)$ on a Riemannian manifold — a second-order elliptic differential operator that generalises the Euclidean Laplacian $\sum \partial_i^2 f$. Its eigenvalues and eigenfunctions encode geometric information about $(M, g)$: the **spectral geometry** of Riemannian manifolds (Kac's question "can you hear the shape of a drum?") and the harmonic analysis of Lie groups and homogeneous spaces are built on this operator.

> [!tip] The Hodge Star Operator *(from Hodge Theory and de Rham Cohomology)*
> The metric extends from vectors and covectors to all degrees of differential forms via the induced inner product on $\Lambda^k T^*M$, and combined with the [[Def - Riemannian Volume Form|Riemannian volume form]] gives the **Hodge star** $\star : \Omega^k(M) \to \Omega^{n-k}(M)$. From it: the codifferential $\delta = (-1)^{...}\star d \star$ adjoint to $d$, the Hodge Laplacian $\Delta = d\delta + \delta d$, and the Hodge decomposition $\Omega^k = \mathrm{im}\, d \oplus \mathrm{im}\, \delta \oplus \ker \Delta$. Harmonic forms (in $\ker \Delta$) represent de Rham cohomology classes uniquely.

> [!tip] Tensor Algebra — Raising and Lowering on Higher-Rank Tensors *(from Tensor Calculus)*
> Applied tensor-by-tensor, the musical isomorphism allows index manipulation on any tensor. The Riemann curvature tensor $R^l{}_{ijk}$ can be lowered to $R_{lijk} = g_{lm}R^m{}_{ijk}$; the Ricci tensor $\mathrm{Ric}_{ij}$ can be raised to $\mathrm{Ric}^{ij} = g^{ik}g^{jl}\mathrm{Ric}_{kl}$. Every component formula in Riemannian and Lorentzian geometry passes through index manipulation via the metric, and the musical isomorphism is the formal mechanism.

> [!tip] The Stress–Energy Tensor in General Relativity *(from General Relativity)*
> The matter stress–energy tensor $T_{\mu\nu}$ on the right-hand side of Einstein's field equations $G_{\mu\nu} = 8\pi G\, T_{\mu\nu}$ can be raised to $T^{\mu\nu}$ or mixed to $T^\mu{}_\nu$, depending on context. The conservation law $\nabla^\mu T_{\mu\nu} = 0$ uses the inverse metric $g^{\mu\nu}$. All of this index gymnastics is the musical isomorphism applied to a particular tensor.
