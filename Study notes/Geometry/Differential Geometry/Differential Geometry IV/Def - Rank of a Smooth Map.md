---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Map between Manifolds"
  - "Def - The Differential of a Smooth Map"
  - "Def - The Tangent Space"
  - "Def - Rank of a Linear Map"
tags: [geometry, differential-geometry]
---

# Notation

Let $F : M \to N$ be a smooth map between smooth manifolds with $\dim M = m$ and $\dim N = n$. At each $p \in M$, the **differential** of $F$ at $p$ is the linear map $dF_p : T_p M \to T_{F(p)} N$ between tangent spaces; see [[Def - The Differential of a Smooth Map]]. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

In any pair of smooth coordinate charts $(U, \varphi)$ around $p$ and $(V, \psi)$ around $F(p)$, the coordinate representation $\hat F = \psi \circ F \circ \varphi^{-1}$ is a smooth map between open subsets of Euclidean space, and the Jacobian matrix $J\hat F(\varphi(p)) = \big[\partial \hat F^i / \partial x^j\big]$ represents $dF_p$ with respect to the bases $\{\partial/\partial x^j|_p\}$ of $T_p M$ and $\{\partial/\partial y^i|_{F(p)}\}$ of $T_{F(p)} N$.

---

# Axiom Motivation

The single most important fact about a smooth map between manifolds is its **first-order behaviour at a point**, packaged in the differential $dF_p$. But $dF_p$ is itself a linear map between vector spaces, and the question we want to ask of a linear map is: what is its rank? A linear map of rank $r$ between vector spaces of [[Def - Dimension|dimensions]] $m$ and $n$ behaves, after a change of basis on both sides, exactly like the standard projection-inclusion $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^r, 0, \dots, 0)$ — its rank is its only invariant. So the rank of $dF_p$ is the natural starting point for any local question about $F$.

The desiderata for the notion of "rank at a point" of a smooth map are sharp. First, it should be the *linear* rank of $dF_p$, so that we inherit all the linear-algebra machinery (rank–nullity, the dimension of the image, the dimension of the kernel) and convert it into geometric statements about $F$. Second, it should be *coordinate-independent* — choosing different charts around $p$ and $F(p)$ must not change the answer. Third, it should be *locally testable* — computable from the Jacobian of the coordinate representation in any single chart, without needing to inspect $F$'s global behaviour.

Why the *rank* and not something else, like the determinant or some other invariant of $dF_p$? Because for non-square $dF_p$ (which is the typical case when $m \neq n$) the determinant is undefined, while rank is well-defined for any linear map between any two finite-dimensional vector spaces. And rank captures *exactly* the information needed for the rank theorem and its corollaries: rank equals $m$ iff $dF_p$ is injective (immersion), rank equals $n$ iff $dF_p$ is surjective (submersion), and rank equals $\min(m,n)$ iff $dF_p$ has maximal possible rank. These three conditions are exactly the conditions of the chapter.

The coordinate independence is automatic once the differential is recognised as a linear map between tangent spaces (which are intrinsic, coordinate-free objects): the rank of a linear map is the dimension of its image, an intrinsic invariant. The Jacobian matrix changes when coordinates change (the new Jacobian is the old one multiplied by the change-of-basis matrices on both sides), but rank is unchanged under multiplication by invertible matrices on either side — exactly because a change of basis is invertible. So "the rank of the Jacobian" gives a well-defined number, which is what we *call* the rank of $F$ at $p$.

What if we tried to demand more — for instance, that the rank also be constant on a neighbourhood, or that it be globally constant? Both of these are stronger and useful conditions, but they belong to derived notions ("constant rank near $p$", "constant rank map"). The pointwise notion is the base case; everything else is built from it. What about *less*? One could imagine only tracking whether $dF_p$ is invertible (a single bit), but this discards the dimension information that drives the entire theory; for instance, the difference between an immersion ($\mathrm{rank} = m$) and a submersion ($\mathrm{rank} = n$) is invisible at this resolution when $m \neq n$, yet these are geometrically opposite conditions.

---

# The Definition

Let $F : M \to N$ be a smooth map between smooth manifolds, and let $p \in M$.

**Rank at a point.** The **rank** of $F$ at $p$, written $\mathrm{rank}\, F|_p$ or $\mathrm{rank}\, dF_p$, is the rank of the linear map $dF_p : T_p M \to T_{F(p)} N$ — equivalently, the dimension of $\mathrm{im}\, dF_p$, or the rank of the Jacobian matrix $J\hat F(\varphi(p))$ in any pair of smooth coordinate charts $(U,\varphi)$ around $p$ and $(V,\psi)$ around $F(p)$.

The rank satisfies $0 \leq \mathrm{rank}\, F|_p \leq \min(\dim M, \dim N)$.

**Constant rank.** The map $F$ has **constant rank** $r$ on an open subset $U \subseteq M$ if $\mathrm{rank}\, F|_p = r$ for every $p \in U$. We say $F$ is a **constant-rank map** if it has constant rank on $M$.

**Maximal rank.** The map $F$ has **maximal rank at $p$** if $\mathrm{rank}\, F|_p = \min(\dim M, \dim N)$. The set $\{p \in M : F$ has maximal rank at $p\}$ is open in $M$.

**Lower semicontinuity.** The function $p \mapsto \mathrm{rank}\, F|_p$ is **lower semicontinuous**: for every $r$, the set $\{p : \mathrm{rank}\, F|_p \geq r\}$ is open in $M$. So rank can only "jump up" in the limit, never down — and the set of maximal-rank points is open.

---

# Relate to Other Fields / Compression

The rank of a smooth map at a point is **the linear rank applied to the linear approximation**. It is the manifold-level packaging of the [[Def - Rank of a Linear Map|linear rank]]: the rank of a linear map $L : V \to W$ between finite-dimensional vector spaces is $\dim \mathrm{im}\, L$, and the rank of a smooth map at $p$ is the rank of the differential $dF_p$ — itself a linear map between tangent spaces. The coordinate Jacobian is the matrix of this linear map; rank-of-Jacobian computations carry over verbatim.

The compression with [[Multivariate Analysis I — Differentiation in Several Variables|multivariable analysis]] is exact: for $F : U \to \mathbb{R}^n$ with $U \subseteq \mathbb{R}^m$ open, the rank of $F$ at $p$ in the manifold sense (using the chart $U$ as a single chart for $\mathbb{R}^m$) is the rank of the Jacobian matrix $DF(p) = [\partial F^i / \partial x^j(p)]$ in the analysis sense. So all the linear-algebra-of-Jacobian content from multivariable analysis transfers directly. The manifold setting just packages this intrinsically — the rank is a number attached to the *map and the point*, not to a chosen coordinate system.

**True name:** the rank of a smooth map at $p$ is the **dimension of the local image** of $F$ in any sufficiently small neighbourhood of $p$, at first order. More precisely, by the [[Thm - The Rank Theorem|rank theorem]], if $F$ has constant rank $r$ near $p$, then the image $F(U)$ for $U$ a small enough neighbourhood of $p$ is, in suitable coordinates, an $r$-dimensional flat slice — so rank is literally the dimension of where $F$ is going, locally.

---

# Examples / Corollaries

**Example — a constant map.** A constant map $F : M \to N$ (sending all of $M$ to a single point $q \in N$) has $dF_p = 0$ at every $p$, so $\mathrm{rank}\, F \equiv 0$. The map has constant rank zero, and the rank theorem says it is "locally trivial" — in any chart, it is the zero linear map.

**Example — a diffeomorphism.** A diffeomorphism $F : M \to N$ between manifolds of the same dimension has $dF_p$ a linear isomorphism at every point, so $\mathrm{rank}\, F|_p = \dim M = \dim N$ everywhere. It has constant maximal rank.

**Example — the squaring map $z \mapsto z^2$ on $\mathbb{C}$.** Viewing $\mathbb{C}$ as $\mathbb{R}^2$, the map $F(x, y) = (x^2 - y^2, 2xy)$ has Jacobian $\begin{pmatrix} 2x & -2y \\ 2y & 2x \end{pmatrix}$, with determinant $4(x^2 + y^2)$. So $\mathrm{rank}\, F = 2$ everywhere except at the origin, where $\mathrm{rank}\, F = 0$. The rank drops at the origin; this is exactly where the squaring map has its critical point.

**Example — a projection $\mathbb{R}^{m+n} \to \mathbb{R}^n$.** The standard projection $\pi(x^1, \dots, x^{m+n}) = (x^{m+1}, \dots, x^{m+n})$ has Jacobian $[0_{n \times m} \mid I_n]$, which has rank $n$ everywhere. This is a constant-rank map of rank $n$ — and an example of a submersion ($\mathrm{rank} = \dim N$).

**Example — a graph map.** Given $g : U \to \mathbb{R}^k$ smooth on $U \subseteq \mathbb{R}^d$ open, the graph map $G(x) = (x, g(x))$ from $U$ to $\mathbb{R}^d \times \mathbb{R}^k$ has Jacobian $\begin{pmatrix} I_d \\ Dg(x) \end{pmatrix}$, which has rank $d$ everywhere (the top block is the identity). This is a constant-rank map of rank $d$ — an immersion ($\mathrm{rank} = \dim M$).

**Is NOT a constant-rank map — the squaring map above.** The squaring map $z \mapsto z^2$ on $\mathbb{C}$ has rank $2$ away from the origin and rank $0$ at the origin. So it is not constant-rank globally — its rank drops at a single point. By lower semicontinuity, the rank-drop point is "isolated upward": the set $\{p : \mathrm{rank} \geq 2\}$ is open (it is $\mathbb{C} \setminus \{0\}$).

**Corollary — rank is preserved by composition with [[Def - Diffeomorphism|diffeomorphisms]].** If $\Psi : M \to M$ and $\Phi : N \to N$ are diffeomorphisms (or even local diffeomorphisms at the relevant points), then $\mathrm{rank}\,(\Phi \circ F \circ \Psi)|_p = \mathrm{rank}\, F|_{\Psi(p)}$. This is the chain rule plus the fact that composing with a linear isomorphism preserves rank. In particular, rank is independent of the choice of coordinate charts — which is what makes the definition well-defined.

**Corollary — the set of maximal-rank points is open.** If $\mathrm{rank}\, F|_p = \min(m,n)$, then by lower semicontinuity $\mathrm{rank}\, F|_q \geq \min(m,n)$ in a neighbourhood of $p$ — but rank cannot exceed $\min(m,n)$, so equality holds in the neighbourhood. The immersion points (when $m \leq n$) form an open set; the submersion points (when $m \geq n$) form an open set; the maximal-rank points always form an open set.

**Calibration check.** Verify that the differential $df_p : T_p M \to T_{f(p)}\mathbb{R} \cong \mathbb{R}$ of a smooth scalar function $f : M \to \mathbb{R}$ has rank either $0$ (when $df_p = 0$, a critical point of $f$) or $1$ (when $df_p \neq 0$, a regular point). Verify that the inclusion $\iota : S^n \hookrightarrow \mathbb{R}^{n+1}$ has rank $n$ at every point (it is an immersion). Verify that the squaring map $z \mapsto z^2$ on $\mathbb{C}$ has rank $2$ away from the origin and rank $0$ at the origin, and that the origin is its only critical point.

---

# Unlocked by This

> [!tip] The Rank Theorem *(from this topic)*
> When a smooth map has **constant** rank on an open set, the [[Thm - The Rank Theorem|rank theorem]] gives a *local normal form*: smooth coordinates on source and target in which the map is the linear projection-inclusion $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^r, 0, \dots, 0)$. So rank is literally the only local invariant of a constant-rank smooth map.

> [!tip] Immersion, Submersion, and Embedding *(from this topic)*
> The two extreme cases of maximal rank are the most important: maximal rank $= \dim M$ is the [[Def - Immersion, Submersion, and Embedding|immersion]] condition (injective differential), and maximal rank $= \dim N$ is the [[Def - Immersion, Submersion, and Embedding|submersion]] condition (surjective differential). Each extreme has its own dedicated local normal form theorem ([[Thm - Local Immersion Theorem]] and [[Thm - Local Submersion Theorem]]).

> [!tip] Critical and Regular Points *(from this topic)*
> A point $p$ where $\mathrm{rank}\, F|_p$ is not maximal is a **critical point**; otherwise it is a **regular point**. For a smooth map $\Phi : M \to N$ a value $c \in N$ is a regular value if every point of $\Phi^{-1}(c)$ is regular (and *automatically* a regular value if $\Phi^{-1}(c) = \varnothing$), and then by the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] the level set $\Phi^{-1}(c)$ is an embedded submanifold. See [[Def - Regular and Critical Points]].

> [!tip] Sard's Theorem and Genericity *(from this topic)*
> [[Thm - Sard's Theorem|Sard's theorem]] says the set of critical values of a smooth map has measure zero — equivalently, *almost every* value is a regular value. The rank-dropping behaviour is generic-zero-measure; ordinary smooth maps generically have maximal rank, and constructions requiring regular values can always find one.
