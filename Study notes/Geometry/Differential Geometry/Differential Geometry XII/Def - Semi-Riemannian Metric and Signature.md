---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Tensor Field on a Manifold"
  - "Def - Symmetric Tensor Field"
  - "Def - Bilinear Form"
  - "Def - Symmetric and Alternating Bilinear Form"
  - "Def - Quadratic Form"
tags: [geometry, differential-geometry, pseudo-riemannian-geometry]
---

# Notation

Let $M$ be a smooth $n$-manifold and $g$ a semi-Riemannian (pseudo-Riemannian) metric on $M$. The **signature** of $g$ is the ordered pair $(p, q)$ of positive and negative eigenvalues of $g_p$ at any point — by Sylvester's law, independent of $p$ on each connected component, and required to be constant globally. We have $p + q = n$. The Riemannian case is signature $(n, 0)$; the Lorentzian case is signature $(1, n-1)$ (or, in the opposite convention, $(n-1, 1)$). Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

This is a compound page: it defines two interlocking notions — semi-Riemannian metric and signature — because they are introduced together and the signature is a fundamental invariant of a semi-Riemannian metric.

---

# Axiom Motivation

The Riemannian definition requires that $g$ be smooth, symmetric, and *positive-definite*. The semi-Riemannian definition relaxes positive-definiteness while keeping the other two properties and adds **non-degeneracy** as a replacement for the positivity that would otherwise fail. The motivation is twofold: a mathematical desire to broaden the class of metrics one studies, and a physical demand from special and general relativity for indefinite metrics with a causal structure.

**Why drop positive-definiteness?** Because the geometric content of [[Special Relativity I — Lorentz Transformations and Minkowski Space|special relativity]] requires it. The [[Def - Minkowski Space and the Metric|Minkowski metric]] $\eta = \mathrm{diag}(1, -1, -1, -1)$ is symmetric and non-degenerate but *not* positive-definite — a vector with $\eta(v, v) = 0$ need not be zero (a null vector), and there exist vectors with $\eta(v, v) < 0$ (spacelike vectors). The whole causal structure of spacetime — light cones, timelike-spacelike-null trichotomy, reversed triangle inequality for timelike vectors — comes from this indefiniteness. If we restricted to positive-definite metrics, we could not formulate the geometry of relativity.

**Why keep non-degeneracy?** Non-degeneracy — the condition that $g_p(v, w) = 0$ for all $w$ implies $v = 0$ — is what makes the metric *invertible* as a bilinear form, equivalently makes the [[Def - Musical Isomorphism (Flat and Sharp)|musical isomorphism]] $TM \to T^*M$ an honest isomorphism. Without non-degeneracy, there would be vectors "invisible" to $g$, the inverse metric $g^{ij}$ would not exist, raising and lowering indices would fail, and the Levi-Civita connection construction would break. Non-degeneracy is the minimal requirement that preserves all the structural machinery of Riemannian geometry while allowing indefinite signature.

**Why is signature well-defined?** A symmetric bilinear form on a finite-dimensional real vector space can always be diagonalised in some basis, with diagonal entries $\pm 1$ or $0$. By **Sylvester's law of inertia**, the numbers of $+1$s, $-1$s, and $0$s are basis-independent invariants of the form. For a *non-degenerate* form, there are no zeros, so the form is characterised by the pair $(p, q)$ — the number of positive and negative diagonal entries. This is the **signature**. Pointwise, the signature of $g_p$ is well-defined; on a connected manifold, it cannot jump (it is a locally constant function of $p$, hence constant on each connected component), so a smooth non-degenerate symmetric $(0, 2)$-tensor field on a connected manifold has a well-defined global signature.

**Why require signature constant globally?** On a connected manifold this is automatic — the eigenvalues of $g_p$ vary continuously in $p$ and never pass through zero (by non-degeneracy), so the signs are locally constant. On a disconnected manifold one could in principle have different signatures on different components, but for the definition to be useful (so that the manifold has a well-defined "type"), we require the signature to be uniform. This is a definitional convention rather than a forced one.

**Why the convention $p + q = n$?** This is just the dimension count — at every point, the bilinear form has $n$ eigenvalues counted with multiplicity, and they must be distributed between positive ($p$) and negative ($q$).

**Per-axiom failure analysis:**

(a) *Drop non-degeneracy.* Then $g_p$ may have a nontrivial **null space** at some $p$ — the set of vectors $v$ with $g_p(v, w) = 0$ for all $w$. The musical isomorphism is no longer an isomorphism, the inverse metric does not exist, and we are in the setting of **degenerate** metrics, which arises in sub-Riemannian geometry and the study of "lightlike" hypersurfaces in Lorentzian manifolds but is not what semi-Riemannian geometry studies.

(b) *Drop symmetry.* Then $g$ has a symmetric and an antisymmetric part. The antisymmetric part is a 2-form, useful for symplectic geometry but unrelated to a metric. Symmetry is essential to the metric being "inner-product-like".

(c) *Drop smoothness.* Then $g_{ij}(x)$ is only continuous, or $C^k$, and the Levi-Civita connection requires $g \in C^2$ to define curvature properly. Low-regularity (semi-)Riemannian metrics are studied in geometric PDE, but they are not the default setting.

(d) *Allow the signature to vary across $M$.* Pointwise the signature is well-defined; globally it must be locally constant (so constant on connected components). Allowing it to jump across components requires non-connectedness, and "the signature of $M$" is not well-defined in that case. For practical purposes we always take $M$ connected and the signature global.

---

# The Definition

> **Definition (Non-degenerate bilinear form on a vector space).** A symmetric bilinear form $b : V \times V \to \mathbb{R}$ on a finite-dimensional real vector space $V$ is **non-degenerate** if for every nonzero $v \in V$ there exists $w \in V$ with $b(v, w) \neq 0$. Equivalently, the map $V \to V^*$, $v \mapsto b(v, \cdot)$ is an isomorphism. Equivalently, $\det(b_{ij}) \neq 0$ in any basis.

> **Definition (Sylvester's law / Signature).** Let $b$ be a non-degenerate symmetric bilinear form on $V$. There exists a basis $(e_1, \ldots, e_n)$ of $V$ in which $b$ is diagonal with entries $\pm 1$:
> $$
> b_{ij} = \pm \delta_{ij}, \qquad b_{ii} = +1 \text{ for } i = 1, \ldots, p, \qquad b_{ii} = -1 \text{ for } i = p+1, \ldots, n.
> $$
> The pair $(p, q) = (p, n-p)$ is the **signature** of $b$ and is independent of the choice of basis.

> **Definition (Semi-Riemannian metric).** A **semi-Riemannian** (or **pseudo-Riemannian**) metric on a smooth manifold $M$ is a smooth symmetric $(0, 2)$-tensor field $g$ that is **non-degenerate** at every point — meaning $g_p$ is a non-degenerate symmetric bilinear form on $T_pM$ for every $p \in M$ — and whose **signature** $(p, q)$ is constant on $M$.

The pair $(M, g)$ is a **semi-Riemannian manifold** of signature $(p, q)$, with $p + q = \dim M$.

**Special cases:**
- $(n, 0)$ — a **Riemannian metric** ([[Def - Riemannian Metric]]).
- $(1, n-1)$ or $(n-1, 1)$ — a **Lorentzian metric** ([[Def - Lorentzian Manifold]]).
- $(p, q)$ with $p, q \geq 2$ — a metric of **mixed signature** (sometimes called **neutral** when $p = q$, used in twistor theory and 4-dimensional split-signature geometry).

In local coordinates,
$$
g = g_{ij}(x)\, dx^i \otimes dx^j, \qquad g_{ij}(x) \text{ smooth, symmetric, with constant signature } (p, q).
$$
The inverse metric $g^{ij}(x)$ is defined by $g^{ij}g_{jk} = \delta^i_k$; it exists pointwise by non-degeneracy and is smooth by Cramer's rule.

---

# Categorical / Structural Definition

A semi-Riemannian metric of signature $(p, q)$ on $M$ is equivalent to a reduction of the structure group of the tangent bundle $TM$ from $GL(n, \mathbb{R})$ to the **indefinite orthogonal group** $O(p, q)$ — the group of linear transformations of $\mathbb{R}^n$ preserving the standard form of signature $(p, q)$:
$$
O(p, q) = \{A \in GL(n, \mathbb{R}) : A^T \eta_{p,q} A = \eta_{p,q}\},
$$
where $\eta_{p,q} = \mathrm{diag}(1, \ldots, 1, -1, \ldots, -1)$ with $p$ ones and $q$ minus ones. Geometrically, this reduction selects at each point a **pseudo-orthonormal frame** — a basis $(e_1, \ldots, e_n)$ with $g(e_i, e_j) = \pm \delta_{ij}$ — and the indefinite orthogonal group is the change-of-frame group between such bases.

For $(p, q) = (n, 0)$, $O(n, 0) = O(n)$ is the usual orthogonal group — the Riemannian case. For $(p, q) = (1, n-1)$, $O(1, n-1)$ is the **Lorentz group** of dimension $n$, the isometry group of $n$-dimensional Minkowski space (with the time-direction-fixed origin). The classification of semi-Riemannian metrics by signature corresponds to the classification of orthogonal groups $O(p, q)$ of the same total dimension.

The bundle picture: a semi-Riemannian metric is a smooth section of the bundle whose fibre at $p$ is the space of non-degenerate symmetric bilinear forms on $T_pM$ of signature $(p, q)$. *Unlike* the Riemannian case, this fibre is not a convex set — it is a union of components (one per signature), and even within a fixed signature the set of metrics of that signature is not convex. This is why the partition-of-unity argument that works for Riemannian metrics ([[Thm - Existence of Riemannian Metrics via Partitions of Unity]]) *fails* for general signatures, and why the existence of, say, a Lorentzian metric is genuinely obstructed.

---

# Relate to Other Fields / Compression

This is the smooth-manifold version of an **indefinite inner product space** in linear algebra. Where a Riemannian metric assigns a positive-definite inner product to each tangent space, a semi-Riemannian metric assigns a non-degenerate symmetric bilinear form, possibly indefinite. All of the algebraic structure of inner-product spaces — the dual-space isomorphism, the orthogonal complement decomposition (with caveats for null subspaces), the symmetric eigendecomposition — has an indefinite analogue, with the wrinkles handled by tracking signs.

The Lorentzian case is the geometric setting of [[Special Relativity I — Lorentz Transformations and Minkowski Space|special relativity]] (when the metric is flat $\eta$) and **general relativity** (when the metric is a dynamical field $g_{\mu\nu}(x)$ obeying the Einstein equations). The notion of "spacetime" in modern physics *is* the notion of a four-dimensional Lorentzian manifold.

Higher-signature cases appear in:
- $(2, 2)$ — split-signature in twistor theory and self-dual geometry.
- $(p, q)$ with $p, q \geq 1$ — pseudo-Riemannian geometry, with applications to holonomy classification (Berger, Bryant).
- Indefinite Kähler geometry — complex manifolds with an indefinite Hermitian metric, used in twistor theory and the study of supergravity backgrounds.

**True name:** A semi-Riemannian metric is *a smoothly varying non-degenerate symmetric bilinear form on tangent spaces*. The signature is the discrete invariant that classifies it up to local pointwise equivalence; the smoothness and connectivity ensure the signature is global.

---

# Examples / Corollaries

**Is an instance — any Riemannian metric.** A positive-definite metric is in particular non-degenerate, so every [[Def - Riemannian Metric|Riemannian metric]] is a semi-Riemannian metric of signature $(n, 0)$. The Riemannian case is the "all-positive" extreme of the semi-Riemannian classification.

**Is an instance — the Minkowski metric $\eta$ on $\mathbb{R}^4$.** With $\eta = \mathrm{diag}(1, -1, -1, -1)$ in Lee's convention, $\eta$ is smooth, symmetric, and non-degenerate ($\det\eta = -1 \neq 0$), with constant signature $(1, 3)$. It is a Lorentzian metric on $\mathbb{R}^4$ — the simplest example, and the model for all Lorentzian geometry; see [[Def - Minkowski Space and the Metric]] and [[Ex - Minkowski Space as the Flat Lorentzian Manifold]].

**Is an instance — Lorentzian metrics on a smooth manifold with a nowhere-vanishing vector field.** Given a Riemannian metric $g_R$ on $M$ and a nowhere-vanishing vector field $X$ on $M$ (this exists, for example, on every odd-dimensional sphere and on every Lie group), the bilinear form $g_L = g_R - 2\, X^\flat \otimes X^\flat / g_R(X, X)$ is a Lorentzian metric. The construction works because subtracting twice the "$X$-projection" of $g_R$ flips the sign on the $X$-direction. This is the standard existence construction for Lorentzian metrics: they exist iff the manifold admits a nowhere-vanishing line field (a slightly weaker condition).

**Is an instance — a metric of signature $(2, 2)$ on $\mathbb{R}^4$.** $g = dx_1^2 + dx_2^2 - dx_3^2 - dx_4^2$ is smooth, symmetric, non-degenerate, with signature $(2, 2)$. This is the **neutral signature** (or **split signature**), used in twistor theory.

**Is NOT an instance — a positive semi-definite metric.** $g = dx^2$ on $\mathbb{R}^2$ (only the $x$-direction contributes) is smooth, symmetric, positive semi-definite, but *degenerate*: $g(\partial_y, v) = 0$ for every $v$. The signature is undefined for degenerate forms (Sylvester gives $(1, 0, 1)$ — one positive, one negative, one zero — but degenerate forms are excluded from the semi-Riemannian definition).

**Is NOT an instance — a non-symmetric bilinear form.** A non-degenerate antisymmetric 2-form $\omega$ — for example a [[Def - Closed and Exact Forms|symplectic form]] $\omega = dp \wedge dq$ on $\mathbb{R}^{2n}$ — is non-degenerate but not symmetric. It is *not* a metric in the semi-Riemannian sense; it gives a symplectic structure rather than an inner product. The signature concept does not apply.

**Corollary — the signature is invariant under isometries.** If $F : (M, g) \to (N, h)$ is a (semi-)Riemannian isometry, then $g$ and $h$ have the same signature. This is because the pullback $F^*h = g$ preserves signature pointwise (isometries are pointwise isomorphisms of inner-product spaces).

**Corollary — every signature is achievable on $\mathbb{R}^n$.** For any $(p, q)$ with $p + q = n$, the constant metric $\sum_{i=1}^p dx_i^2 - \sum_{i=p+1}^n dx_i^2$ is a flat semi-Riemannian metric of signature $(p, q)$ on $\mathbb{R}^n$. So locally, every signature is realisable; the global question of whether a given smooth manifold admits a metric of a given signature is more delicate ([[Thm - A Lorentzian Manifold Need Not Exist on Every Smooth Manifold]]).

**Calibration check.** First, identify the signature of $g = -dt^2 + dx^2 + dy^2 + dz^2$ on $\mathbb{R}^4$ (the "mostly plus" convention). Expected: $(3, 1)$ — three positive eigenvalues (the spatial directions), one negative (the time direction). Second, verify that $g = dxdy + dydx$ on $\mathbb{R}^2$ (in coordinates $(x, y)$) is non-degenerate and find its signature. Compute: the matrix is $g_{ij} = \bigl(\begin{smallmatrix} 0 & 1 \\ 1 & 0\end{smallmatrix}\bigr)$, with eigenvalues $\pm 1$, so signature $(1, 1)$. Third, on the 2-dimensional Lorentzian plane $\mathbb{R}^{1,1}$ with $g = dt^2 - dx^2$, identify the null vectors. Expected: vectors of the form $(\pm a, a)$ for $a \in \mathbb{R}$, lying on the two lines $t = \pm x$.

---

# Unlocked by This

> [!tip] Lorentzian Manifolds and General Relativity *(from General Relativity)*
> The signature-$(1, n-1)$ case is the [[Def - Lorentzian Manifold|Lorentzian manifold]], the geometric setting of relativistic physics. The four-dimensional Lorentzian manifold is **spacetime**, and the Einstein field equations $R_{\mu\nu} - \tfrac{1}{2}R\, g_{\mu\nu} = 8\pi G\, T_{\mu\nu}$ govern its dynamics. Most of physics, from the geodesic motion of test particles to gravitational waves, lives in this signature.

> [!tip] The Fundamental Theorem of (Semi-)Riemannian Geometry *(from Riemannian Geometry)*
> The [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|fundamental theorem]] holds in the semi-Riemannian case: every semi-Riemannian metric uniquely determines a torsion-free metric-compatible connection (the **Levi-Civita connection**). This connection, its curvature, and the resulting curvature tensors (Riemann, Ricci, scalar) generalise verbatim from Riemannian to semi-Riemannian. The proofs use non-degeneracy of $g$, not positive-definiteness, so they carry over.

> [!tip] Signature Restrictions on Existence *(from Topology of Manifolds)*
> While Riemannian metrics exist on every smooth manifold, Lorentzian metrics do not. The obstruction is the existence of a nowhere-vanishing line field, and equivalent obstructions are formulated in terms of Euler characteristic, Stiefel–Whitney classes, and (for closed manifolds) integral characteristic numbers. The general topology-of-manifolds question "which signatures does $M$ admit?" is the subject of substantial research.

> [!tip] Holonomy and Berger's Classification *(from Riemannian Holonomy Theory)*
> The **holonomy group** of a (semi-)Riemannian metric is the group generated by parallel transport along closed loops. **Berger's classification** lists the possible holonomy groups of irreducible non-symmetric Riemannian metrics — $O(n)$, $U(n/2)$, $SU(n/2)$, $Sp(n/4) \cdot Sp(1)$, $Sp(n/4)$, $G_2$, $\mathrm{Spin}(7)$ — and the corresponding rich geometric structures (Kähler, Calabi–Yau, hyperkähler, quaternionic-Kähler, $G_2$, $\mathrm{Spin}(7)$ manifolds). The signature-indefinite analogue is also classified (Berger, Bryant, etc.) and includes the holonomy structures relevant to supergravity.
