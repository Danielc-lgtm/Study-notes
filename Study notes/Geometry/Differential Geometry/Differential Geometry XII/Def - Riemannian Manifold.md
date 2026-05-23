---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Riemannian Metric"
tags: [geometry, differential-geometry, riemannian-geometry]
---

# Notation

$(M, g)$ — a Riemannian manifold: $M$ is a smooth $n$-manifold (Hausdorff, second-countable), $g$ is a [[Def - Riemannian Metric|Riemannian metric]] on $M$. The dimension $n$ is the dimension of $M$ as a smooth manifold. Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

---

# Axiom Motivation

The need for this definition is purely terminological: once we have decided to study geometry on manifolds, we want a name for "a smooth manifold together with a chosen Riemannian metric". The pair $(M, g)$ is more than just $M$: every geometric quantity — length, angle, distance, curvature, geodesic — depends on $g$ as well as on $M$. To talk about isometries, to define geodesics, to compute curvature, the metric is part of the object, not auxiliary data.

The decision to bundle $M$ and $g$ into one object is the same decision one makes in linear algebra when one writes "inner product space $(V, \langle\cdot,\cdot\rangle)$" rather than "vector space $V$ with an inner product $\langle\cdot,\cdot\rangle$": the inner product is part of the structure being studied, not external to it. A *vector space isomorphism* preserves only the linear structure; an *inner product space isomorphism* (linear isometry) preserves both linear structure and inner product, and is a more restrictive notion. Similarly, *a diffeomorphism* of smooth manifolds preserves only the smooth structure, while a [[Def - Isometry of Riemannian Manifolds|Riemannian isometry]] preserves the metric as well — and the round sphere and the ellipsoid, while diffeomorphic as smooth manifolds, are not isometric as Riemannian manifolds.

There is no question of which axioms to impose — the data is exactly $(M, g)$ with $M$ a smooth manifold and $g$ a Riemannian metric — but the conceptual move is to commit to the metric as part of the structure rather than as external choice.

---

# The Definition

> **Definition (Riemannian Manifold).** A **Riemannian manifold** is a pair $(M, g)$, where $M$ is a smooth manifold (Hausdorff, second-countable) and $g$ is a [[Def - Riemannian Metric|Riemannian metric]] on $M$.

The dimension of $(M, g)$ is the dimension of $M$ as a smooth manifold. By abuse of language one often refers to "the Riemannian manifold $M$" when the metric is clear from context, but strictly speaking the object is the pair.

**Subobjects:** A **Riemannian submanifold** of $(M, g)$ is a pair $(S, \iota^* g)$ where $S \subseteq M$ is an immersed or embedded submanifold and $\iota^* g$ is the [[Def - Induced Metric on a Submanifold|induced metric]] obtained by pulling back $g$ along the inclusion $\iota : S \hookrightarrow M$.

**Morphisms:** A **smooth map of Riemannian manifolds** is a smooth map $F : (M, g) \to (N, h)$, where smoothness is in the manifold sense. The map is a **Riemannian isometry** if $F$ is a diffeomorphism with $F^*h = g$; see [[Def - Isometry of Riemannian Manifolds]]. The isometries form a group $\mathrm{Isom}(M, g)$.

**Completeness:** A Riemannian manifold $(M, g)$ is **complete** (or **metrically complete**) if the [[Def - Length of a Curve and Riemannian Distance|Riemannian distance]] $d_g$ makes $(M, d_g)$ a complete metric space — every Cauchy sequence converges. Equivalently (Hopf–Rinow) — but this is the content of Riemannian Geometry, not this chapter — $M$ is **geodesically complete**: every geodesic extends to all parameter values.

---

# Categorical / Structural Definition

Riemannian manifolds form a category $\mathbf{Riem}$: objects are pairs $(M, g)$, morphisms are smooth maps preserving the metric only when they are isometries; alternatively, one can take morphisms to be **smooth Riemannian submersions** (smooth maps whose differential, restricted to the orthogonal complement of the kernel at each point, is a linear isometry onto the tangent space of the target) or **smooth Riemannian immersions** (smooth immersions whose differential, restricted to its image, is a linear isometry — equivalently, $F^*h = g$ for an immersion $F$). The category of Riemannian manifolds is best regarded as a *higher-structured* version of $\mathbf{Smooth}$: the underlying smooth manifold is a forgetful image, and an inner-product structure is the "extra" data.

From the bundle perspective, a Riemannian manifold is a smooth manifold equipped with a chosen $O(n)$-reduction of its frame bundle — see the categorical section of [[Def - Riemannian Metric]] for this perspective.

---

# Relate to Other Fields / Compression

A Riemannian manifold is *the geometric object* that differential geometry studies; it is the manifold version of "Euclidean space", parametrised by an arbitrary smooth manifold rather than $\mathbb{R}^n$. Where Euclidean geometry studies $(\mathbb{R}^n, \bar g)$ with $\bar g$ the standard inner product, Riemannian geometry studies $(M, g)$ with $M$ any smooth manifold and $g$ any positive-definite inner product field. The flat Euclidean case is the case $M = \mathbb{R}^n$, $g = \bar g$.

The analogue in physics: in [[Special Relativity I — Lorentz Transformations and Minkowski Space|special relativity]], the object is $(\mathbb{R}^4, \eta)$ — a flat *Lorentzian* manifold. In general relativity, the object is $(M, g)$ with $M$ a four-dimensional smooth manifold and $g$ a Lorentzian metric. The structural type "manifold + metric" is shared with Riemannian geometry; the difference is the signature of $g$ — positive-definite for Riemannian, $(1, 3)$ for relativistic.

**True name:** A Riemannian manifold is *a smooth space carrying enough geometric data to do all of differential geometry*. The minimum data needed for length, distance, angle, gradient, divergence, Laplacian, geodesics, and curvature is a smoothly varying inner product on tangent spaces, and the Riemannian manifold is the object packaging exactly this.

---

# Examples / Corollaries

**Is an instance — Euclidean space $(\mathbb{R}^n, \bar g)$.** With the standard Euclidean metric $\bar g = \sum (dx^i)^2$. This is the prototypical Riemannian manifold, the flat case. Every other Riemannian manifold is, at each point, locally modelled on the Euclidean structure of the tangent space (with the metric serving as the inner product there).

**Is an instance — the round sphere $(S^n, \mathring g)$.** With the induced metric from $\mathbb{R}^{n+1}$. The simplest *curved* Riemannian manifold: positive constant sectional curvature, finite total volume, compact, with isometry group $O(n+1)$.

**Is an instance — the hyperbolic plane $(\mathbb{H}^2, g_{\mathbb{H}})$.** Either as the upper half-plane $\{y > 0\} \subseteq \mathbb{R}^2$ with $g_{\mathbb{H}} = (dx^2 + dy^2)/y^2$, or as the Poincaré disk model. Constant negative sectional curvature, non-compact, with isometry group $\mathrm{PSL}(2, \mathbb{R})$.

**Is an instance — the flat torus $(T^n, g_{\mathrm{flat}})$.** With the quotient metric from $\mathbb{R}^n / \mathbb{Z}^n$. Compact, flat (zero curvature everywhere), genuinely non-trivial topologically — it cannot be isometrically embedded into Euclidean $\mathbb{R}^n$ even though it is locally flat (the Nash embedding theorem requires higher-dimensional ambient space).

**Is an instance — a Lie group with a left-invariant metric.** Any [[Def - Lie Group|Lie group]] $G$ becomes a Riemannian manifold by choosing an inner product on $\mathfrak{g} = T_e G$ and translating it. If the inner product is $\mathrm{Ad}$-invariant (e.g., on compact $G$), the resulting metric is bi-invariant and has remarkable symmetry properties.

**Is NOT an instance — Minkowski space $(\mathbb{R}^4, \eta)$.** Although $\mathbb{R}^4$ is a smooth manifold and $\eta$ is a smooth symmetric $(0,2)$-tensor field, $\eta$ is not positive-definite, so $(\mathbb{R}^4, \eta)$ is *not* a Riemannian manifold. It is a [[Def - Lorentzian Manifold|Lorentzian manifold]] — a different category. The distinction is the signature of $g$, and it matters: Minkowski space has a causal structure (light cones, timelike/spacelike trichotomy) that no Riemannian manifold has.

**Is NOT an instance — $\mathbb{R}^n$ with no metric specified.** The bare smooth manifold $\mathbb{R}^n$ is not a Riemannian manifold; to make it one, you must *choose* a Riemannian metric. The default Euclidean choice is so natural that it is often suppressed, but the data of a Riemannian manifold is "manifold + metric", and a manifold without a chosen metric is not yet a Riemannian manifold.

**Corollary — every smooth manifold becomes a Riemannian manifold by choice of metric.** By [[Thm - Existence of Riemannian Metrics via Partitions of Unity]], a Riemannian metric always exists. The choice is non-canonical (many metrics work), but at least one always does.

**Corollary — Riemannian submanifolds are Riemannian manifolds.** Any submanifold $S \subseteq M$ of a Riemannian manifold inherits a Riemannian structure via the induced metric ([[Def - Induced Metric on a Submanifold]]). The category of Riemannian manifolds is closed under taking immersed/embedded submanifolds.

**Calibration check.** First, identify which of the following are Riemannian manifolds in the strict sense: (i) $\mathbb{R}^n$ with the Euclidean metric — yes; (ii) $S^2$ with the induced metric — yes; (iii) $S^2$ with no metric specified — no, just a smooth manifold; (iv) $\mathbb{R}^4$ with the Minkowski metric — no, Lorentzian not Riemannian; (v) the cylinder $S^1 \times \mathbb{R}$ with the product metric — yes. Second, observe that the same smooth $S^2$ admits both the round metric *and* the metric inherited from an embedding as a non-round ellipsoid; these are different Riemannian manifolds with the same underlying smooth manifold. Third, verify that a Riemannian product $(M_1 \times M_2, g_1 \oplus g_2)$ is again a Riemannian manifold, with $(g_1 \oplus g_2)((v_1, v_2), (w_1, w_2)) = g_1(v_1, w_1) + g_2(v_2, w_2)$.

---

# Unlocked by This

> [!tip] All of Riemannian Geometry *(from Riemannian Geometry)*
> Once we have committed to "manifold + metric" as the basic object of study, every subsequent construction of Riemannian geometry — geodesics, curvature, exponential map, comparison theorems, Hodge theory, harmonic maps, Ricci flow — is the unfolding of consequences of this single piece of data. The structural significance of "Riemannian manifold" is therefore not in the definition (which is trivial) but in the commitment: this is the object, and everything we will build sits on top of it.

> [!tip] General Relativity — Lorentzian Manifolds in Place of Riemannian *(from General Relativity)*
> Replacing "Riemannian metric" by "Lorentzian metric" in the definition gives a **Lorentzian manifold** $(M, g)$, the geometric object of general relativity. The same formal structure — manifold + metric — but with a different signature, and the consequences differ fundamentally: a causal structure, a distinction between time and space, the Einstein field equations governing the dynamics of $g$ itself. The conceptual parallelism between Riemannian and Lorentzian geometry is one of the most powerful unifying frames in modern differential geometry.
