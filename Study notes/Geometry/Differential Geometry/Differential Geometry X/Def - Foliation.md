---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Distribution on a Manifold"
  - "Def - Involutive Distribution"
  - "Def - Integral Manifold of a Distribution"
tags: [geometry, differential-geometry, frobenius, foliation]
---

# Notation

$M$ is a smooth $n$-manifold. A **foliation** is denoted by a calligraphic $\mathcal{F}$. Its members — the immersed submanifolds in the partition — are called the **leaves** and denoted $L, L', L_p$, etc.; $L_p$ is the leaf through $p$. The leaves have dimension $k$, the **dimension of the foliation**, and codimension $n - k$. A **flat chart for $\mathcal{F}$** is a smooth coordinate chart $(U, \varphi)$ with $\varphi(U) \subseteq \mathbb{R}^n$ a cube, such that each leaf $L \in \mathcal{F}$ intersects $U$ in either the empty set or a countable disjoint union of $k$-dimensional **slices** of the form $\{x^{k+1} = c^{k+1}, \dots, x^n = c^n\}$ for constants $c^{k+1}, \dots, c^n$.

---

# Axiom Motivation

The desideratum is to formalize the global geometric structure produced by an integrable distribution. We have a partition of $M$ into integral manifolds; we want a definition that captures exactly the regularity properties such a partition automatically has, in a way that does *not* require remembering which distribution it came from.

Three properties must hold for any such partition. **(i)** Each piece is a connected, nonempty, $k$-dimensional immersed submanifold (not necessarily embedded — recall the irrational line on the torus). **(ii)** The pieces are *disjoint*: any two distinct leaves do not meet, by the very notion of "partition." **(iii)** The pieces "fit together regularly" in the sense that in suitable local coordinates the partition looks just like a stack of parallel $k$-planes — there is a flat chart at every point. The third property is the most subtle and is what distinguishes a foliation from a general decomposition.

Without (iii), one could imagine a "partition" of $\mathbb{R}^3$ into curves that are pathologically arranged — say, curves that approach each other in a Cantor-like pattern, or that bend without regularity. The flat-chart requirement rules out such pathology by forcing the partition to be smoothly trivializable in every local neighborhood. It is the global analogue of the local-trivializability condition that makes a smooth bundle a smooth bundle.

Why insist that *countably many* slices of a flat chart can contain leaf-pieces? Because a single leaf — when it is dense in $M$, like the irrational-slope line on the torus — meets a flat chart in a *countable* family of slices (each pass through the chart is a slice, and the leaf passes through countably many times). If we required each leaf to meet a flat chart in a *single* slice, we would exclude the dense-leaf case, which is the standard non-embedded example we want to keep. The countable-union flexibility is what makes the definition handle both embedded and non-embedded leaves uniformly.

Why introduce foliations as a *separate* concept from integrable distributions, when they are equivalent via the global Frobenius theorem? Because the foliation viewpoint is the right one for many questions: it focuses on the partition rather than on the infinitesimal data. Many constructions are natural at the foliation level — leaf-wise integration, the holonomy groupoid, secondary characteristic classes, foliated cohomology. The distribution is the differential data; the foliation is the global integrated structure, and they have complementary uses.

A weaker definition — "a partition of $M$ into $k$-dimensional immersed submanifolds, with no regularity condition" — would let in pathological partitions and fail to recover the flat-chart structure. A stronger definition — "a partition with a *global* product structure $M \cong F \times B$" — would be far too restrictive (a foliated $T^2$ by lines of irrational slope cannot be globally a product, since the leaves are dense). The flat-chart requirement is the Goldilocks: locally trivial, globally permissive.

---

# The Definition

Let $M$ be a smooth $n$-manifold. A **foliation of [[Def - Dimension|dimension]] $k$** on $M$ is a collection $\mathcal{F}$ of disjoint, connected, nonempty, immersed $k$-dimensional submanifolds of $M$ (called the **leaves** of $\mathcal{F}$) such that:

**(i) Covering:** $\bigsqcup_{L \in \mathcal{F}} L = M$.

**(ii) Flat charts exist everywhere:** for every $p \in M$, there is a smooth coordinate chart $(U, \varphi)$ around $p$ with $\varphi(U)$ a cube in $\mathbb{R}^n$, such that each leaf $L \in \mathcal{F}$ meets $U$ in either the empty set or a countable union of $k$-dimensional **slices** $\{x \in U : x^{k+1} = c^{k+1}, \dots, x^n = c^n\}$ for constants $c^{k+1}, \dots, c^n$.

The number $n - k$ is the **codimension** of the foliation.

**Connection to involutive distributions (Global [[Thm - The Frobenius Theorem|Frobenius Theorem]]):** if $\mathcal{F}$ is a foliation, then the collection $\{T_pL : p \in M, L \ni p\}$ is an involutive distribution $D \subseteq TM$ — the **tangent distribution of $\mathcal{F}$**. Conversely, if $D$ is an involutive distribution, then the collection of maximal connected integral manifolds of $D$ is a foliation. This bijection between foliations and involutive distributions is the content of the [[Thm - The Frobenius Theorem|global Frobenius theorem]] (Lee, Theorem 19.21).

---

# Relate to Other Fields / Compression

**True name:** A foliation is *a smooth partition of $M$ by submanifolds, with a coherent local product structure.* The operational reading is: every point has a neighborhood $U \cong P \times T$ (a product of a $k$-disc $P$, the **plaque**, and an $(n-k)$-disc $T$, the **transversal**) such that each leaf meets $U$ in plaques $P \times \{*\}$. The global gluing of these local product structures is the content of the foliation.

**Compression to fiber bundles.** A fiber bundle with structure group $G$ has a global "fiber over base" decomposition. A foliation is a weaker structure: the local product structure is the same as for a fiber bundle, but the leaves can be wildly different in topology (compact and noncompact mixed, embedded and dense mixed), unlike fibers of a bundle which are all diffeomorphic. So foliations generalize bundle decompositions to allow for "wild" leaf structure.

**Compression to dynamical systems.** The orbits of a complete flow (or, more generally, of a smooth $\mathbb{R}^k$-action) on $M$ form a foliation (subject to some regularity). The leaves are orbits; the flat chart structure corresponds to "linearizing" the action locally via the canonical-form theorems for commuting flows. Many problems in dynamical systems — recurrent dynamics, ergodicity, hyperbolicity — are foliation problems in disguise.

**Compression to mechanics.** A holonomic constraint defines a foliation of configuration space — each leaf is a connected component of a constraint surface ($f_1 = c_1, \dots, f_r = c_r$). The leaves are *constant-energy surfaces* in Hamiltonian mechanics, *constant-action surfaces* in completely integrable systems, and so on. The leaves are precisely the surfaces along which the system can evolve.

---

# Examples / Corollaries

**Is an instance: parallel hyperplanes in $\mathbb{R}^n$.** The collection of affine $k$-planes $\{x^{k+1} = c^{k+1}, \dots, x^n = c^n\}$ as the constants vary is a foliation of $\mathbb{R}^n$, with the global Cartesian coordinates serving as a global flat chart. This is the "trivial" example, and Frobenius says every foliation looks locally like this.

**Is an instance: the fibers of a submersion.** If $F : M \to N$ is a smooth submersion, the family of fibers $\{F^{-1}(q) : q \in N\}$ is a foliation of $M$ of codimension $\dim N$. The flat charts come from the local-form theorem for submersions: in suitable coordinates, $F$ looks like the projection onto the last $\dim N$ coordinates, and the fibers become the slices.

**Is an instance: a foliation of $T^2$ by lines of fixed slope.** Take $T^2 = \mathbb{R}^2 / \mathbb{Z}^2$ and the rank-$1$ distribution spanned by $\partial_x + \alpha \partial_y$. For rational $\alpha = p/q$, the leaves are embedded closed curves (each line, after wrapping around the torus, closes up to a curve of slope $p/q$). For irrational $\alpha$, every leaf is dense — only immersed, not embedded. Both cases are foliations.

**Is an instance: the orbits of a free Lie [[Def - Group|group]] action.** If a Lie [[Def - Group|group]] $G$ acts smoothly and freely on $M$, the orbits $G \cdot p$ form a foliation of [[Def - Dimension|dimension]] $\dim G$. The flat chart structure comes from the existence of *local slices* (transversals to the action). When the action is not free, the orbit decomposition is a stratification, not a foliation.

**Is an instance: the Reeb foliation of $S^3$.** A celebrated foliation of $S^3$ by surfaces, with two "Reeb components" each diffeomorphic to a solid torus interior, and leaves that asymptote to the boundary torus. This is a $2$-dimensional foliation of a $3$-manifold; the leaves are non-compact non-embedded immersed surfaces. The Reeb foliation shows that even on compact manifolds the leaf structure can be exotic.

**Is NOT an instance: an arbitrary partition of $\mathbb{R}^n$ into $k$-dimensional submanifolds.** Without the flat-chart condition, such a partition can be pathological — leaves can accumulate on each other in non-product ways. The flat-chart condition is what rules out the pathologies.

**Is NOT an instance: the partition of $\mathbb{R}^2$ into the $x$-axis and concentric circles around the origin.** Each piece is a $1$-dimensional submanifold, the pieces are disjoint, and they cover $\mathbb{R}^2$. But there is no flat chart at any point of the $x$-axis: the leaf through such a point is a line, but the leaves arbitrarily close to it are circles, and no chart can put both into the slice format $\{x^2 = c\}$. So this is not a foliation. (It is a *singular* foliation, in a generalized sense — but not a foliation in the strict sense of this definition.)

**Corollary (uniqueness of leaves through a point).** Given a foliation $\mathcal{F}$ and a point $p \in M$, there is exactly one leaf $L_p \in \mathcal{F}$ containing $p$. By definition, $\mathcal{F}$ partitions $M$, so the leaf is unique.

**Corollary (the tangent distribution of a foliation is involutive).** From `Proposition 19.19` in Lee: the family $\{T_pL_p\}_{p \in M}$ of tangent spaces to leaves forms a smooth distribution, and the existence of integral manifolds (the leaves themselves) plus the necessity of involutivity yields bracket-closure.

**Corollary (the leaves of a foliation are weakly embedded).** By `Theorem 19.17` in Lee, every integral manifold of an involutive distribution is weakly embedded. Since the leaves of a foliation are integral manifolds, they are weakly embedded; in particular, every smooth map into a leaf, lifted from $M$, is smooth.

**Corollary (codimension-1 foliations and integrating factors).** A codimension-1 foliation on $M$ is locally given by $\ker \alpha$ for a $1$-form $\alpha$; involutivity (and hence the foliation structure) holds iff $\alpha \wedge d\alpha = 0$. When it does, $\alpha = \lambda \,df$ locally for some positive function $\lambda$ (an *integrating factor*) and some function $f$ — the leaves are the level sets of $f$.

**Calibration check.** If you have understood the definition you should be able to (i) verify the parallel-hyperplanes foliation of $\mathbb{R}^n$ satisfies the flat-chart property, (ii) explain why the concentric-circles-plus-$x$-axis decomposition of $\mathbb{R}^2$ is *not* a foliation, and (iii) state the bijective correspondence between foliations of $M$ and involutive distributions on $M$.

---

# Unlocked by This

> [!tip] **Holonomy of a foliation** *(from Foliation Theory)*
> Each leaf $L$ has a **holonomy group** at every point, capturing the "twist" the foliation experiences as you travel around a loop in $L$. Holonomy is the foliation-theoretic analogue of the fundamental group, and the holonomy groupoid is the right global invariant of a foliation. This unlocks the deep theory of foliations as developed by Reeb, Haefliger, and Connes.

> [!tip] **Characteristic classes of foliations** *(from Foliation Theory and Algebraic Topology)*
> Foliations have **secondary characteristic classes** — the Godbillon–Vey class, the Bott classes — living in the de Rham cohomology of $M$. These detect global obstructions to deforming the foliation, and the Godbillon–Vey class of the Reeb foliation is non-zero, showing it is *cobordism-non-trivial*. The Bott vanishing theorem and the Pontryagin classes of the normal bundle constrain which foliations can exist on which manifolds.

> [!tip] **Symplectic foliations and Poisson manifolds** *(from Geometric Mechanics)*
> A **Poisson manifold** is a manifold whose ring of smooth functions has a Lie bracket (the Poisson bracket) satisfying Leibniz. Every Poisson manifold has a canonical **symplectic foliation**: leaves are symplectic submanifolds, generally of varying dimension. This generalizes the symplectic foliation by orbits in a Lie–Poisson manifold $\mathfrak{g}^*$ — coadjoint orbits are the leaves, each with the Kirillov–Kostant–Souriau symplectic form.

> [!tip] **Noncommutative geometry** *(from Connes's Foliation Theory)*
> Connes's noncommutative geometry encodes a foliation $\mathcal{F}$ in a $C^*$-algebra — the **foliation algebra** $C^*(\mathcal{F})$ — whose representations capture the leaf space structure even when the leaf space $M/\mathcal{F}$ is pathological as a topological space (as for the irrational torus foliation). This is the gateway from foliations to noncommutative geometry.
