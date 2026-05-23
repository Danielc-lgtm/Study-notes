---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Map between Manifolds"
  - "Def - The Differential of a Smooth Map"
  - "Def - Rank of a Smooth Map"
  - "Def - Homeomorphism"
  - "Def - Subspace Topology"
tags: [geometry, differential-geometry]
---

# Notation

Throughout, $F : M \to N$ is a smooth map between smooth manifolds, with $\dim M = m$ and $\dim N = n$. The differential at $p$ is $dF_p : T_p M \to T_{F(p)} N$ ([[Def - The Differential of a Smooth Map]]). The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

This is a compound page: it defines three interlocking notions — **immersion**, **submersion**, and **(smooth) embedding** — because they form a strict hierarchy (embeddings are immersions with an extra topological condition) and none is fully usable without comparison to the others. The single underlying parameter is the rank of $dF_p$.

---

# Axiom Motivation

The differential $dF_p$ at a point is a linear map between finite-dimensional vector spaces, so it can be either injective, surjective, both (an isomorphism), or neither. These four cases correspond to four geometric types of behaviour for $F$ near $p$, and the local-normal-form theorems of this chapter ([[Thm - The Rank Theorem|the rank theorem]] and its specialisations) say *the local behaviour of $F$ near $p$ is determined entirely by which of these four cases $dF_p$ falls into*. Naming these cases is therefore essential — they are the categories the local theory is built around.

**Why "immersion" for $dF_p$ injective.** The picture is that $F$ "immerses" $M$ into $N$ — like dipping a curve into a higher-dimensional space, the image is locally an $m$-dimensional piece of $N$. This requires $m \leq n$, since an injective linear map can exist only when the source has dimension no greater than the target. Injectivity of the *differential* (not of $F$ itself) is the right condition because injectivity at the linear level is exactly what prevents the image from collapsing dimensionally — by the [[Thm - Local Immersion Theorem|local immersion theorem]], an immersion is locally the standard inclusion of $\mathbb{R}^m$ into $\mathbb{R}^n$. Note that immersion is a *local* condition: every immersion is locally injective (as a map), but globally an immersion may not be injective. The classic example is a smooth curve in the plane that crosses itself — at the crossing point the curve is not injective as a map, but its derivative is non-zero everywhere, so it is an immersion.

**Why "submersion" for $dF_p$ surjective.** Here $F$ "submerses" or "submerges" $M$ into $N$ — the image of any neighbourhood of $p$ fills out a neighbourhood of $F(p)$ in $N$ (by the [[Thm - Local Submersion Theorem|local submersion theorem]]; locally $F$ looks like a coordinate projection). This requires $m \geq n$. Submersions are how "quotient" maps appear in smooth geometry: the fibres are the level sets, and the base is the image. Every smooth submersion is an [[Thm - Submersions are Open Maps|open map]], so a surjective submersion is a smooth quotient map. The condition is on the differential, not on $F$ itself, because surjectivity at the linear level is exactly what gives the [[Thm - The Implicit Function Theorem|implicit function theorem]] room to apply.

**Why "embedding" needs a separate definition.** An immersion's image, with the subspace topology from $N$, may not be homeomorphic to $M$. The figure-eight curve $\beta(t) = (\sin 2t, \sin t)$, $t \in (-\pi, \pi)$, is an injective immersion whose image is *not* homeomorphic to $(-\pi, \pi)$ in the subspace topology: in the subspace topology of $\mathbb{R}^2$, the crossing point $(0,0)$ is a limit of two distinct sequences $t_n \to \pi$ and $t_n \to -\pi$, but in the domain $(-\pi, \pi)$ those sequences have no common limit. So the parametrisation is injective but not a homeomorphism onto its image. An **embedding** is the strengthening that fixes this: it demands the immersion be a homeomorphism onto its image. The point is that without this extra topological condition, "submanifold" would not have a clean notion of subspace topology, and theorems like the slice criterion would fail.

What if we tried to drop the immersion condition from "embedding"? Then we would have a topological embedding that need not be smooth in the way we want — for instance the map $\gamma(t) = (t^3, 0)$ from $\mathbb{R}$ to $\mathbb{R}^2$ is a topological embedding (a homeomorphism onto its image, the $x$-axis) and smooth as a map, but its derivative at $0$ is zero, so it is not an immersion. Its image is fine as a submanifold (the $x$-axis), but the *map* $\gamma$ is not the right kind: the smooth structure on the image inherited via $\gamma$ disagrees with the embedded-submanifold smooth structure. So "smooth embedding" demands both ingredients — smooth immersion *and* topological embedding — to ensure the image is a clean smooth submanifold and the map is a diffeomorphism onto it.

What if we tried to *strengthen* the submersion condition (by requiring constant rank rather than just pointwise surjectivity)? It turns out you don't need to: pointwise surjectivity in a neighbourhood already implies constant rank in that neighbourhood, by the upper bound $\mathrm{rank}\, dF_p \leq n$ and lower semicontinuity from [[Def - Rank of a Smooth Map]]. The local definitions are stable, and constant rank is automatic for immersions and submersions in the open neighbourhood where they hold.

---

# The Definition

Let $F : M \to N$ be a smooth map between smooth manifolds, $m = \dim M$, $n = \dim N$.

**Immersion.** $F$ is an **immersion at $p$** if $dF_p : T_p M \to T_{F(p)} N$ is **injective** (equivalently, $\mathrm{rank}\, dF_p = m$, which requires $m \leq n$). $F$ is a **smooth immersion** if it is an immersion at every point of $M$.

**Submersion.** $F$ is a **submersion at $p$** if $dF_p : T_p M \to T_{F(p)} N$ is **surjective** (equivalently, $\mathrm{rank}\, dF_p = n$, which requires $m \geq n$). $F$ is a **smooth submersion** if it is a submersion at every point of $M$.

**Smooth embedding.** $F$ is a **smooth embedding** if $F$ is a smooth immersion that is also a **topological embedding** — that is, a homeomorphism from $M$ onto its image $F(M)$ equipped with the [[Def - Subspace Topology|subspace topology]] inherited from $N$. Equivalently, $F$ is an injective smooth immersion such that $F : M \to F(M)$ has a continuous inverse for the subspace topology on $F(M)$.

**Local diffeomorphism.** $F$ is a **local diffeomorphism at $p$** if $dF_p$ is a linear isomorphism (equivalently, both an immersion and a submersion at $p$, which forces $m = n$). By the [[Thm - The Inverse Function Theorem|inverse function theorem]], this is equivalent to the existence of an open neighbourhood $U$ of $p$ such that $F|_U : U \to F(U)$ is a [[Def - Diffeomorphism|diffeomorphism]] onto an open subset of $N$.

**Sufficient criteria for embedding.** Suppose $F : M \to N$ is an injective smooth immersion. If any of the following holds, then $F$ is a smooth embedding:
1. $F$ is an open or closed map;
2. $F$ is a proper map (preimages of compact sets are compact);
3. $M$ is compact.

The compact case is the most commonly used: any injective smooth immersion from a compact manifold is automatically an embedding.

---

# Categorical Definition

In the category $\mathbf{SmoothMan}$ of smooth manifolds and smooth maps, **immersions** and **submersions** are the structural analogues, respectively, of monomorphisms and epimorphisms in algebra — but with the caveat that they are defined infinitesimally (on tangent spaces), not categorically (on maps).

More cleanly: the differential functor $dF_p : T_p M \to T_{F(p)} N$ lives in the category of finite-dimensional vector spaces, where injectivity and surjectivity have the usual categorical meanings. **Immersion** is "injectivity in the tangent category"; **submersion** is "surjectivity in the tangent category". This is what makes them so natural — they are the conditions on $F$ for which the differential is, respectively, a monomorphism or epimorphism in $\mathbf{Vect}$.

**Embedding as a strictly stronger condition.** A smooth embedding is an immersion plus the topological condition of being a homeomorphism onto its image. The added topology pins down the image as a subspace of $N$ (in the subspace topology), which makes the image a well-defined embedded submanifold. Without this, the image could carry multiple topologies, none of them canonical. The categorical content: the image of a smooth embedding is an embedded submanifold, and the inclusion of an embedded submanifold is itself a smooth embedding (canonical and unique).

**The submersion / quotient analogy.** A surjective smooth submersion plays the role of a quotient map in $\mathbf{SmoothMan}$: it has the universal property that a map $F : N \to P$ is smooth if and only if its composition with the submersion is smooth (a manifold-level analogue of the quotient topology's characteristic property). This is why "quotient manifold theorems" (Lie group actions producing homogeneous spaces, fibre bundles, etc.) are organised around submersions.

---

# Relate to Other Fields / Compression

The triple **(immersion, submersion, embedding)** is the manifold version of the analysis triple **(injective derivative, surjective derivative, locally a graph)** in [[Multivariate Analysis II — Inverse and Implicit Function Theorems]]. In Euclidean space, a smooth map $F : U \to \mathbb{R}^n$ from an open $U \subseteq \mathbb{R}^m$ has:
- $DF_p$ injective ⟺ $F$ is an immersion at $p$;
- $DF_p$ surjective ⟺ $F$ is a submersion at $p$;
- $F$ injective with closed image ⟹ $F$ is a topological embedding.

So the manifold definitions are the Euclidean ones promoted to chart-independent statements via the differential.

The relationship to [[Def - Submanifold of Euclidean Space|submanifolds of Euclidean space]] is direct: a subset $S \subseteq \mathbb{R}^n$ is an embedded submanifold (in the Euclidean sense) iff it is locally the image of a smooth embedding $V \to \mathbb{R}^n$ from an open $V \subseteq \mathbb{R}^d$. The manifold theory in this topic generalises this to the case where the ambient space is itself a manifold rather than $\mathbb{R}^n$.

**True name (for immersion):** the **true name** of "immersion" is **"locally an embedding"** — by the [[Thm - Local Immersion Theorem|local immersion theorem]], every immersion is locally a smooth embedding (i.e., for every $p \in M$ there is a neighbourhood $U$ of $p$ such that $F|_U$ is a smooth embedding). So an immersion is the local-without-global version of an embedding.

**True name (for submersion):** the **true name** of "submersion" is **"admits smooth local sections everywhere"**. The [[Thm - Local Submersion Theorem|local submersion theorem]] says that for every $p \in M$ and every neighbourhood of $F(p)$ in $N$, there is a smooth right-inverse of $F$ defined on a smaller neighbourhood. This is the operational content; surjectivity of the differential is the check.

**True name (for embedding):** the **true name** of "smooth embedding" is **"diffeomorphism onto an embedded submanifold"**. By the inverse-image-of-embedding construction ([[Def - Embedded Submanifold]]), the image of a smooth embedding is an embedded submanifold, and the embedding is itself a diffeomorphism onto this image.

---

# Examples / Corollaries

**Is an immersion: the inclusion $\iota : S^n \hookrightarrow \mathbb{R}^{n+1}$.** Its differential at any point $p \in S^n$ is the inclusion of the tangent space $T_p S^n \cong \{v \in \mathbb{R}^{n+1} : v \cdot p = 0\}$ into $\mathbb{R}^{n+1}$, which is injective. Since $S^n$ is compact, it is also an embedding by the compact-domain criterion.

**Is an immersion but not an embedding: the figure-eight curve.** The map $\beta : (-\pi, \pi) \to \mathbb{R}^2$, $\beta(t) = (\sin 2t, \sin t)$, is an injective smooth immersion (its velocity $\beta'(t) = (2\cos 2t, \cos t)$ never vanishes). But its image in the subspace topology from $\mathbb{R}^2$ is *not* homeomorphic to $(-\pi, \pi)$: the sequences $t_n = -\pi + 1/n$ and $s_n = \pi - 1/n$ both have images converging to $(0,0)$ in $\mathbb{R}^2$, while in $(-\pi, \pi)$ they converge to opposite ends and have no common limit. So $\beta$ is an injective immersion that is *not* an embedding. See [[Ex - The Figure-Eight Immersion]] for the full analysis.

**Is a submersion: the projection $\pi : \mathbb{R}^{m+n} \to \mathbb{R}^n$, $\pi(x, y) = y$.** Its differential is the constant linear map $(v, w) \mapsto w$, which is surjective. So $\pi$ is a smooth submersion at every point. The fibres $\pi^{-1}(y) = \mathbb{R}^m \times \{y\}$ are all diffeomorphic copies of $\mathbb{R}^m$.

**Is a submersion: the Hopf map $h : S^3 \to S^2$.** Viewing $S^3 \subseteq \mathbb{C}^2$ and $S^2 \cong \mathbb{CP}^1$, the map $h(z, w) = [z : w]$ is a smooth submersion with fibres the great circles $\{(\lambda z, \lambda w) : |\lambda| = 1\}$. See [[Ex - The Hopf Map is a Submersion]].

**Is a smooth embedding: the inclusion of a closed submanifold.** If $S \subseteq M$ is an [[Def - Embedded Submanifold|embedded submanifold]] (so $S$ already has the subspace topology), the inclusion $\iota : S \hookrightarrow M$ is, by definition, a smooth embedding. This is the canonical example.

**Is a local diffeomorphism but not a global one: the covering map $\mathbb{R} \to S^1$, $t \mapsto e^{2\pi i t}$.** At every $t \in \mathbb{R}$, the differential is multiplication by $2\pi i e^{2\pi i t}$, which is non-zero, hence a linear isomorphism — so this is a local diffeomorphism (in fact a smooth covering map). It is not globally injective, and certainly not an embedding, because it wraps $\mathbb{R}$ around the circle infinitely many times.

**Is NOT an immersion: the cusp parametrisation $t \mapsto (t^3, t^2)$.** This map's derivative at $t = 0$ is $(3t^2, 2t)|_{t=0} = (0, 0)$, which is zero — not injective. Away from $0$ the derivative is non-zero, so it is an immersion away from $0$. The image is the cusped curve $\{y^3 = x^2\}$, which has a non-smooth cusp at the origin: this is the geometric meaning of the rank dropping at $t = 0$.

**Is NOT a submersion: the inclusion $\iota : S^n \hookrightarrow \mathbb{R}^{n+1}$.** Its differential at any $p$ has image $T_p S^n$, which is $n$-dimensional inside the $(n+1)$-dimensional $T_p \mathbb{R}^{n+1}$ — so the differential is not surjective. Inclusions of strictly lower-dimensional submanifolds are never submersions; they are immersions.

**Corollary — immersions are open maps onto the appropriate target dimension only when $m = n$.** If $F : M \to N$ is an immersion with $\dim M < \dim N$, then $F$ is *not* an open map: $F(M)$ has dimension $\dim M < \dim N$, so it cannot contain any open subset of $N$. Immersions are open maps iff they are also submersions iff $m = n$ iff they are local diffeomorphisms.

**Corollary — submersions are surjective on neighbourhoods.** If $F : M \to N$ is a submersion at $p$, then for every neighbourhood $U$ of $p$ in $M$, the image $F(U)$ is a neighbourhood of $F(p)$ in $N$. This is the [[Thm - Submersions are Open Maps|open mapping]] property and is the geometric content of "submersions admit local sections".

**Calibration check.** Verify that any local diffeomorphism is both an immersion and a submersion (and conversely, an immersion plus submersion equals local diffeomorphism, forcing $m = n$). Verify the projection $T M \to M$ in the tangent bundle is a smooth submersion (its differential is essentially the projection in the local trivialisation). Verify that the antipodal map $S^n \to S^n$ is a diffeomorphism (hence both immersion and embedding), and that any composition of immersions is an immersion (and similarly for submersions and embeddings).

---

# Unlocked by This

> [!tip] The Rank Theorem and its Specialisations *(from this topic)*
> The [[Thm - The Rank Theorem|rank theorem]] is the unified statement covering both immersions ([[Thm - Local Immersion Theorem]]) and submersions ([[Thm - Local Submersion Theorem]]): a constant-rank smooth map has a coordinate normal form. Immersions and submersions are the two extreme rank conditions, and each has its own normal form theorem; the unified one covers them both plus everything in between.

> [!tip] Embedded Submanifolds *(from this topic)*
> The image of a smooth embedding is an [[Def - Embedded Submanifold|embedded submanifold]] of the target; conversely every embedded submanifold appears this way. The dictionary "embedding ↔ embedded submanifold" is the foundation of the entire submanifold theory.

> [!tip] Smooth Covering Maps *(from Differential Topology)*
> A **smooth covering map** $\pi : \tilde M \to M$ is a surjective local diffeomorphism that is also a topological covering map. Smooth covering maps are simultaneously immersions, submersions, and local diffeomorphisms; they are the smooth-category analogue of the topological covering theory.

> [!tip] Lie Subgroups *(from [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie Theory]])*
> A subgroup $H$ of a Lie group $G$ that is also a smooth immersed (resp. embedded) submanifold is a **Lie subgroup** (resp. **closed Lie subgroup**). The closed Lie subgroup theorem says closed subgroups are automatically embedded; non-closed Lie subgroups exist (e.g., the irrational line on the torus) and are immersed but not embedded.

> [!tip] Fibre Bundles *(from Algebraic Topology)*
> A surjective submersion with locally trivial fibres is a **fibre bundle**. The Hopf fibration $S^3 \to S^2$ is the simplest nontrivial example. Bundles are how higher-dimensional manifolds are built from lower-dimensional ones with global twists, and they organise the theory of vector bundles, principal bundles, and gauge theory.
