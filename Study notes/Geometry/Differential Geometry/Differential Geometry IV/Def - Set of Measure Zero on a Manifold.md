---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Coordinate Chart and Atlas"
  - "Def - Smooth Map between Manifolds"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold. A subset $A \subseteq \mathbb{R}^n$ has **Lebesgue measure zero** if for every $\delta > 0$, $A$ can be covered by a countable collection of open rectangles (equivalently, open balls or open cubes) whose total $n$-dimensional volume is less than $\delta$. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

---

# Axiom Motivation

A general smooth manifold $M$ carries no canonical measure or volume — a Riemannian metric is required to define one, and there is no canonical metric. So we cannot define "measure zero on $M$" by integrating a volume form (no volume form is available without extra structure) or by bounding the measure of $A$ (no measure is available). But [[Thm - Sard's Theorem|Sard's theorem]] says the critical values of a smooth map have measure zero in the codomain manifold, so *some* notion of measure zero on a manifold is essential.

The escape is that Lebesgue measure zero on $\mathbb{R}^n$ is **diffeomorphism-invariant** in a precise sense: a smooth map between open subsets of $\mathbb{R}^n$ (of the same [[Def - Dimension|dimension]]) sends measure-zero sets to measure-zero sets, because such a map is locally Lipschitz on compact sets, and Lipschitz maps preserve measure zero with at most a multiplicative bound on the covering volumes. This makes "measure zero" a property that transports across charts: if $\varphi(A \cap U)$ has measure zero in $\mathbb{R}^n$ for one chart $(U, \varphi)$, then the same is true in any compatible chart.

So we *define* "measure zero on a manifold" by demanding it in every chart: $A \subseteq M$ has measure zero iff $\varphi(A \cap U)$ has Lebesgue measure zero in $\mathbb{R}^n$ for every smooth chart $(U, \varphi)$ of $M$. The diffeomorphism invariance ensures this is well-posed; in practice, only one atlas needs to be checked.

The desiderata for this notion are clean:
1. **[[Def - Diffeomorphism|Diffeomorphism]] invariance.** Smooth maps between manifolds of the same dimension send measure-zero sets to measure-zero sets.
2. **Closure under countable unions.** A countable union of measure-zero sets has measure zero (just like in Euclidean space).
3. **Density of the complement.** The complement of a measure-zero set is dense in $M$ — measure-zero sets are "small enough that you can avoid them by perturbing".
4. **Submanifolds of positive codimension have measure zero.** A submanifold of dimension $k < n$ has measure zero in $M$ — strictly lower-dimensional pieces are negligible.

All four of these properties follow from the chart-based definition. The fourth is particularly important for Sard's theorem: critical points often form a positive-codimension subset (whose image will then have measure zero in the codomain).

What if we tried to use a chart-independent definition, like a positive Borel measure on $M$? This is possible (push forward Lebesgue measure under any chart), but it depends on the chart choice and is not canonical. The "measure zero" property *is* canonical, even though the measure itself is not — this is the largest piece of measure theory that survives without a metric.

What if we tried to demand the chart-based condition for only *one* chart at each point (rather than all charts)? This would also work, by diffeomorphism invariance: if it holds for one cover, it holds for all. Both formulations are equivalent. The "all charts" version is logically tidier; the "some chart cover" version is more efficient to verify.

---

# The Definition

Let $M$ be a smooth $n$-manifold.

**Set of measure zero.** A subset $A \subseteq M$ has **measure zero** (or is **negligible**) if for every smooth chart $(U, \varphi)$ of $M$, the Euclidean set
$$\varphi(A \cap U) \;\subseteq\; \mathbb{R}^n$$
has $n$-dimensional Lebesgue measure zero.

**Equivalent characterisation (one cover suffices).** $A \subseteq M$ has measure zero if and only if there exists *some* collection of smooth charts $\{(U_\alpha, \varphi_\alpha)\}_{\alpha \in I}$ whose domains cover $A$, such that $\varphi_\alpha(A \cap U_\alpha)$ has measure zero in $\mathbb{R}^n$ for each $\alpha$. (Once the property is verified for one cover, it holds for every chart, by diffeomorphism invariance.)

**Closure properties.**
1. **Countable union.** If $\{A_i\}_{i \in \mathbb{N}}$ are measure-zero subsets of $M$, then $\bigcup_i A_i$ is a measure-zero subset of $M$.
2. **Subset.** If $A \subseteq B$ and $B$ has measure zero in $M$, then $A$ has measure zero in $M$.
3. **Diffeomorphism preservation.** If $F : M \to N$ is a smooth map between manifolds of the same dimension and $A \subseteq M$ has measure zero, then $F(A) \subseteq N$ has measure zero. (More generally, $F$ can be replaced by a Lipschitz-on-compacts map.)
4. **Smooth image when domain dimension is smaller.** If $F : M \to N$ is smooth with $\dim M < \dim N$, then $F(M)$ has measure zero in $N$.

**Complement is dense.** If $A \subseteq M$ has measure zero, then $M \setminus A$ is dense in $M$ — every nonempty open subset of $M$ meets $M \setminus A$, because a nonempty open subset cannot itself have measure zero (using any chart, a nonempty Euclidean open set has positive Lebesgue measure).

---

# Relate to Other Fields / Compression

The notion of measure zero on a manifold is the **chart-independent shadow of Lebesgue measure zero** in Euclidean space. It is the largest piece of Lebesgue measure theory that does not require additional structure (a metric, a volume form, an explicit measure) to define.

**Comparison with full measure theory.** On a Riemannian manifold, one can define a full Borel measure (the Riemannian volume measure), under which "measure zero" coincides with the chart-based notion. But the chart-based notion is well-defined without any metric, while the full measure requires the metric. So the chart-based "measure zero" is a structure-light substitute for a full measure: it does not assign a number to subsets, but it does identify which sets are negligible.

The relationship to **first category / meagre sets** in topology: measure zero is a measure-theoretic notion of smallness; meagre is a topological notion (a countable union of nowhere-dense sets). They are independent — there exist measure-zero sets that are residual (the complement of a meagre set), and there exist meagre sets of positive measure. The two notions of "small" coexist and are sometimes called "fat" vs "thin" in different senses.

**True name:** the **true name** of "measure zero on a manifold" is **"negligible in every coordinate chart"** — that is, the set looks small from every Euclidean perspective. The chart-dependent verification is the operational meaning; the invariance under diffeomorphisms ensures the property is genuinely about $M$, not about a chosen chart.

---

# Examples / Corollaries

**Example — a single point.** A single point $\{p\} \subseteq M$ has measure zero: in any chart, it corresponds to a single point in $\mathbb{R}^n$, which has Lebesgue measure zero. More generally, any countable subset of $M$ has measure zero.

**Example — a submanifold of positive codimension.** Any embedded or immersed submanifold $S \subseteq M$ with $\dim S < \dim M$ has measure zero in $M$. To see this, cover $S$ by countably many slice charts $\{(U_i, \varphi_i)\}$ in which $S \cap U_i$ corresponds to a flat slice $\mathbb{R}^k \times \{0\}^{n-k}$ in $\varphi_i(U_i) \subseteq \mathbb{R}^n$. A flat slice of dimension $k < n$ has $n$-dimensional Lebesgue measure zero, so each $\varphi_i(S \cap U_i)$ has measure zero, hence $S$ has measure zero by the one-cover-suffices criterion.

**Example — the graph of a continuous function.** For $A \subseteq \mathbb{R}^{n-1}$ open and $f : A \to \mathbb{R}$ continuous, the graph $\Gamma(f) \subseteq \mathbb{R}^n$ has measure zero. (Proved by induction in Lee's Proposition 6.3.) So a graph in $\mathbb{R}^n$ — even a graph of a merely continuous function — is negligible. This is the engine of "submanifolds have measure zero".

**Example — a proper affine [[Def - Subspace|subspace]].** A proper affine subspace of $\mathbb{R}^n$ has measure zero (corollary of the graph result). So lines in $\mathbb{R}^2$, planes in $\mathbb{R}^3$, hyperplanes in $\mathbb{R}^n$ — all have measure zero in the appropriate ambient space.

**Example — critical values of a smooth map (Sard).** By [[Thm - Sard's Theorem|Sard's theorem]], the set of critical values of any smooth map $F : M \to N$ has measure zero in $N$. This is the most important application of the notion, and it makes "almost every value is regular" a precise statement.

**Is NOT a set of measure zero — a nonempty open subset.** Any nonempty open subset $U \subseteq M$ does not have measure zero: in any chart whose domain meets $U$, the image of $U$ contains a nonempty open subset of $\mathbb{R}^n$, which has positive Lebesgue measure. So "$M \setminus A$ is dense" follows from "$A$ has measure zero".

**Is NOT a set of measure zero — the Cantor set with positive measure.** The standard Cantor set in $[0,1]$ has measure zero. But there exist "fat Cantor sets" — closed, nowhere-dense subsets of $[0,1]$ with positive Lebesgue measure. These are NOT measure-zero sets, even though they are meagre (nowhere dense). Conversely, the rationals in $[0,1]$ have measure zero (countable) but are *dense* — they are not meagre. So the topological notion of "small" and the measure-theoretic notion of "small" disagree.

**Corollary — a smooth map between manifolds of equal dimension cannot map a positive-measure set to a measure-zero set "from the outside".** If $F : M \to N$ is smooth, $\dim M = \dim N$, and $A \subseteq M$ has positive measure (i.e., is not measure-zero), then $F(A)$ might still have measure zero (if $F$ collapses dimension somewhere), but this would only happen on critical sets — by Sard, such collapsing is rare.

**Corollary — Sard plus measure zero gives "almost every value is regular".** Since the critical values have measure zero, their complement (the regular values) is dense in $N$. The complement of a measure-zero set is always dense, so regular values can be picked arbitrarily close to any value.

**Calibration check.** Verify that any countable subset of $M$ has measure zero. Verify that the unit circle $S^1 \subseteq \mathbb{R}^2$ has measure zero in $\mathbb{R}^2$ (it is a $1$-submanifold of a $2$-manifold). Verify that the cone $\{z^2 = x^2 + y^2\} \subseteq \mathbb{R}^3$ has measure zero in $\mathbb{R}^3$ (it's a $2$-dimensional subset of a $3$-manifold, even though not a submanifold — but it is a finite union of graphs and a single point, all of which have measure zero). If you can also explain why "measure zero" does not require a metric on $M$ — that is, why the chart-based definition is intrinsic — you have understood the diffeomorphism-invariance content.

---

# Unlocked by This

> [!tip] Sard's Theorem *(from this topic)*
> [[Thm - Sard's Theorem|Sard's theorem]] is the central theorem about manifolds of measure-zero sets: the critical values of a smooth map form a set of measure zero. This is what makes regular values generic, transversality generic, and Morse functions generic — and it is the engine of the weak Whitney embedding theorem.

> [!tip] Almost Everywhere Properties *(from Geometric Measure Theory)*
> Whenever a property is shown to hold off a measure-zero set, we say it holds **almost everywhere**. On manifolds without a metric, this is the only well-defined "almost everywhere" notion. It is enough for many density / genericity arguments.

> [!tip] Volume Forms and Integration *(from [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]])*
> When $M$ is oriented and equipped with a volume form $\omega$ (a never-vanishing top-degree differential form), integrating a function against $\omega$ defines a positive measure on $M$ — the **volume measure**. The measure-zero sets of this measure coincide with the chart-based measure-zero sets, so the chart-based notion is the "skeleton" preserved as one adds structure.

> [!tip] Fubini's Theorem on Manifolds *(from Measure Theory)*
> Fubini's theorem and its analogues for product measures generalise to product manifolds, and the manifold notion of measure zero behaves correctly under the product (e.g., $A \times B$ has measure zero in $M \times N$ iff $A$ or $B$ does, almost surely). This is the framework for the slicing arguments behind Sard's theorem.
