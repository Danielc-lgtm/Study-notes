---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - Immersion, Submersion, and Embedding"
  - "Def - Subspace Topology"
  - "Def - Coordinate Chart and Atlas"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold (without boundary, by our standing convention from [[Differential Geometry I — Smooth Manifolds and Atlases]]). $S \subseteq M$ is a subset that we wish to give the structure of a smooth manifold. A **smooth chart** on $M$ is a pair $(U, \varphi)$ with $U \subseteq M$ open and $\varphi : U \to \mathbb{R}^n$ a homeomorphism onto an open subset of $\mathbb{R}^n$, all compatible with the smooth structure of $M$. A **$k$-slice** of an open set $\varphi(U) \subseteq \mathbb{R}^n$ is a subset of the form $\{x \in \varphi(U) : x^{k+1} = c^{k+1}, \dots, x^n = c^n\}$ for some constants. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

---

# Axiom Motivation

We want a precise notion of "a smooth $k$-dimensional submanifold sitting inside an $n$-manifold". The desiderata: it should generalise [[Def - Submanifold of Euclidean Space|the Euclidean-submanifold theory]] from $\mathbb{R}^n$-ambient to general-manifold-ambient; it should give a well-defined smooth structure on $S$ (so that "submanifold" is an unambiguous notion); it should make the inclusion $\iota : S \hookrightarrow M$ a smooth map automatically; and it should produce the standard examples — the sphere inside $\mathbb{R}^{n+1}$, a great circle inside the sphere, a Lie group inside $\mathrm{GL}(n)$ — without forcing the embedding to be given as part of the data.

The naive try is: "$S$ is a smooth manifold and the inclusion $\iota$ is smooth". This is too weak. It does not pin down the topology of $S$ (we could give $S$ any topology making the inclusion continuous), and consequently does not pin down the smooth structure. The figure-eight image set illustrates the danger: as a subset of $\mathbb{R}^2$ it inherits the subspace topology and is not a manifold (it has a singular crossing), but it can be parametrised by an open interval, which puts a *different* topology on the same set, under which it *is* a manifold. So "subset that is a manifold" is ambiguous about which topology is meant.

The fix is to *demand the subspace topology*. An **embedded submanifold** is required to be a smooth manifold *in the subspace topology* — the topology inherited from $M$. Then there is no ambiguity: the topology is determined by the ambient manifold, and (as we will see in the corollaries below) the smooth structure compatible with this topology is unique. The figure-eight image set, with the subspace topology, fails to be a manifold (the crossing point has no Euclidean neighbourhood), so it is correctly excluded.

The second piece of the definition is that the inclusion $\iota : S \hookrightarrow M$ should be a **smooth embedding** — a smooth immersion that is also a topological embedding. The topological-embedding part is automatic from "subspace topology" (the inclusion is then a homeomorphism onto its image, trivially). The immersion part is the substantive requirement: it ensures the smooth structure on $S$ is *compatible* with that of $M$, in the sense that smooth functions on $M$ restrict to smooth functions on $S$, and tangent vectors to $S$ embed into tangent vectors to $M$ via $d\iota_p$.

What if we tried to weaken the immersion condition? Then we might admit a "submanifold" whose smooth structure does not match the ambient — for instance, the $x$-axis in $\mathbb{R}^2$ with its standard smooth structure is fine (the inclusion is an immersion), but with the alternative smooth structure given by the chart $t \mapsto t^3$ (where $t$ is the standard coordinate), the inclusion is no longer an immersion (its derivative at $0$ is zero) — yet the subspace topology is the same. The immersion condition rules out such mismatched smooth structures.

What if we tried to *strengthen* the definition — for instance, by demanding $S$ be closed in $M$ (giving "properly embedded")? Then we exclude open submanifolds like the open unit ball in $\mathbb{R}^n$, which is naturally an $n$-dimensional embedded submanifold (the inclusion is a smooth open immersion). Closedness is a useful extra hypothesis when needed but should not be built in.

The most operational characterisation of embedded submanifold is the **local $k$-slice condition**: every point of $S$ is contained in a coordinate chart of $M$ in which $S$ is locally a flat slice $\{x^{k+1} = \dots = x^n = 0\}$. This is what makes computations possible: the slice charts of $M$ restrict to coordinate charts of $S$, and the smooth structures match automatically. The equivalence between "satisfies the local slice condition" and "is an embedded submanifold" is a theorem ([[Thm - The Rank Theorem|the rank theorem]] is one route in its proof), but the slice condition is what people actually check.

---

# The Definition

Let $M$ be a smooth $n$-manifold.

**Embedded submanifold (primary definition).** A subset $S \subseteq M$ is a **$k$-dimensional embedded submanifold** of $M$ if there exists a smooth manifold structure on $S$ (consisting of a topology and a smooth atlas) such that:
1. The topology on $S$ is the **subspace topology** inherited from $M$;
2. With this smooth structure, the inclusion map $\iota : S \hookrightarrow M$ is a smooth embedding (a smooth immersion that is also a topological embedding).

The integer $k$ is the **dimension** of $S$ (necessarily $0 \leq k \leq n$), and $n - k$ is its **codimension**. An embedded $1$-codimensional submanifold is an **embedded hypersurface**.

**Local slice criterion (equivalent characterisation).** A subset $S \subseteq M$ is an embedded $k$-dimensional submanifold of $M$ if and only if it satisfies the **local $k$-slice condition**: for every $p \in S$ there is a smooth chart $(U, \varphi)$ of $M$ with $p \in U$ such that
$$\varphi(S \cap U) = \varphi(U) \cap (\mathbb{R}^k \times \{0\}^{n-k}).$$
A chart $(U, \varphi)$ for which $\varphi(S \cap U)$ is a $k$-slice of $\varphi(U)$ is called a **slice chart** for $S$ in $M$.

**Properly embedded.** An embedded submanifold $S \subseteq M$ is **properly embedded** if the inclusion $\iota : S \hookrightarrow M$ is a proper map (preimages of compact sets are compact). Equivalently, $S$ is closed in $M$.

**Uniqueness.** The smooth manifold structure on $S$ making it an embedded submanifold is unique: any two such structures coincide.

**Equivalence to regular level sets.** Every embedded submanifold is *locally* a regular level set of a smooth submersion ([[Thm - Regular Value Theorem on Manifolds]]); conversely every regular level set is an embedded submanifold. So the local descriptions are interchangeable.

---

# Categorical / Structural Definition

In the category $\mathbf{SmoothMan}$ of smooth manifolds and smooth maps, an embedded submanifold $S \subseteq M$ is a **subobject** in the precise sense that the inclusion $\iota : S \hookrightarrow M$ is a monomorphism (injective on points) and *also* satisfies the universal property characterising the inherited structure: a map $F : N \to M$ that happens to land in $S$ is smooth as a map into $M$ if and only if it is smooth as a map into $S$ (since $S$ has the subspace topology and inherited smooth structure). This is the manifold-level statement of the topological "restricting the codomain" property: for embedded submanifolds, restricting the codomain preserves smoothness automatically.

**Sheaf-theoretic content.** The local-slice characterisation says an embedded submanifold is a subset that, locally, looks like the inclusion $\mathbb{R}^k \hookrightarrow \mathbb{R}^n$ as the first $k$ coordinates of $\mathbb{R}^n$. This is the structural content: the geometry of $S$ inside $M$ is locally trivial — it is a coordinate subspace inclusion in suitable charts — and only the global topology distinguishes one embedded submanifold from another. The sheaf of smooth functions on $S$ is the restriction of the sheaf of smooth functions on $M$ to subsets of $S$ (modulo the standard subtlety that not every smooth function on $S$ extends globally; see the extension lemma for functions on submanifolds).

---

# Relate to Other Fields / Compression

An embedded submanifold of $M$ is **the abstract version of a [[Def - Submanifold of Euclidean Space|Euclidean submanifold]] with general-manifold ambient instead of $\mathbb{R}^n$**. When $M = \mathbb{R}^n$ the definitions coincide: the local-slice characterisation is exactly the chart/straightening definition of a Euclidean submanifold. The four equivalent characterisations from the Euclidean case (chart, implicit, parametric, graphical) all carry over to the manifold case, with the same proofs in local coordinates.

In topology, an embedded submanifold is the smooth-category analogue of a **topological embedding** with locally Euclidean image. The added smooth structure is what allows differential calculus on $S$: tangent vectors, derivatives, vector fields, forms.

In algebraic geometry, the analogue is a **smooth subvariety** — a subset cut out by polynomials whose Jacobian has maximal rank at every point of the subset. The local-slice condition is replaced by "locally cut out by polynomials with a regularity condition", and the resulting object is a smooth variety in the algebraic-geometric sense.

**True name:** the **true name** of "embedded submanifold" is **"satisfies the local $k$-slice condition"**. This is the operational characterisation: when handed a subset $S \subseteq M$ and asked whether it is an embedded submanifold, you check whether around each point there is a chart of $M$ in which $S$ is locally a coordinate slice. The "smooth manifold structure" definition is logically primary but operationally derived; the slice characterisation is what you compute with.

---

# Examples / Corollaries

**Is an instance — open submanifolds.** Any open subset $U \subseteq M$ is an embedded submanifold of $M$ of codimension $0$. The inclusion is trivially a smooth embedding, and the local slice condition is satisfied by any chart contained in $U$. The smooth structure on $U$ is the restriction of $M$'s smooth structure.

**Is an instance — the sphere $S^n \subseteq \mathbb{R}^{n+1}$.** By [[Ex - The Sphere as a Level Set]], $S^n$ is a regular level set of $f(x) = |x|^2 - 1$ on $\mathbb{R}^{n+1}$, hence (by [[Thm - Regular Value Theorem on Manifolds]]) an embedded $n$-dimensional submanifold. The subspace topology coincides with the standard topology on the sphere, and the smooth structure agrees with the one defined via stereographic projection.

**Is an instance — graphs of smooth maps.** For $g \in C^\infty(M, N)$ between smooth manifolds, the graph $\Gamma(g) = \{(p, g(p)) : p \in M\} \subseteq M \times N$ is an embedded submanifold of $M \times N$, diffeomorphic to $M$. The inclusion $M \to \Gamma(g)$ given by $p \mapsto (p, g(p))$ is a smooth embedding (its inverse is the projection $\Gamma(g) \to M$).

**Is an instance — the orthogonal group $\mathrm{O}(n) \subseteq \mathrm{GL}(n,\mathbb{R})$.** By [[Ex - The Orthogonal Group as a Regular Level Set]], $\mathrm{O}(n)$ is a regular level set of $\Phi(A) = A^T A$ valued in symmetric matrices, hence an embedded submanifold of dimension $n(n-1)/2$. Being closed in $\mathrm{GL}(n)$ (and even in $\mathrm{Mat}_n$), it is properly embedded.

**Is an instance — the identity element of a Lie group.** A single point in a smooth manifold is a $0$-dimensional embedded submanifold (trivially: the local slice condition is satisfied with $k = 0$ and the slice being the origin in any chart).

**Is NOT an embedded submanifold — the figure-eight curve.** The image $S = \{(\sin 2t, \sin t) : t \in (-\pi, \pi)\} \subseteq \mathbb{R}^2$ is not an embedded submanifold of $\mathbb{R}^2$: in the subspace topology, the crossing point $(0,0)$ has no neighbourhood homeomorphic to an open interval (any neighbourhood contains four "branches" meeting at the crossing). So the local-slice condition fails at the crossing. It *is* an immersed submanifold, with its own topology pulled back from the parametrisation (see [[Def - Immersed Submanifold]]).

**Is NOT an embedded submanifold — the dense line on the torus.** For irrational $\alpha$, the line $\{(e^{2\pi i t}, e^{2\pi i \alpha t}) : t \in \mathbb{R}\} \subseteq T^2$ is dense in the torus. In the subspace topology, it is not locally Euclidean (every neighbourhood of any point contains pieces of infinitely many "wraps" of the line). So it is not embedded, though it is immersed.

**Is NOT an embedded submanifold — a set with a corner.** The set $S = \{(x, y) : y = |x|\} \subseteq \mathbb{R}^2$ has a corner at the origin: in the subspace topology, no neighbourhood of the origin in $S$ is homeomorphic to an open interval and *also* smoothly compatible with $\mathbb{R}^2$. So $S$ is not an embedded $1$-submanifold (it can be made into a topological $1$-manifold via the homeomorphism $\mathbb{R} \to S$, $t \mapsto (t, |t|)$, but the inclusion of this manifold into $\mathbb{R}^2$ is not smooth at the origin).

**Corollary — uniqueness of smooth structure.** If $S \subseteq M$ is an embedded submanifold, the smooth structure making it so is unique. *Proof sketch:* given two such structures, the identity map between them is smooth in both directions (by restricting the codomain of the inclusion), so it is a diffeomorphism.

**Corollary — closed embedded ⟺ properly embedded.** An embedded submanifold $S$ is properly embedded if and only if it is closed in $M$.

**Corollary — compact embedded submanifolds are properly embedded.** Any compact embedded submanifold is automatically closed (compact subsets of Hausdorff spaces are closed) and hence properly embedded.

**Calibration check.** Verify that any single point of $M$ is a $0$-dimensional embedded submanifold. Verify that $S^1 \subseteq S^2$ as the equator is an embedded $1$-dimensional submanifold (find a slice chart at any point). Verify that the local-slice condition fails for the figure-eight at the crossing point (no chart of $\mathbb{R}^2$ can flatten the four branches onto a coordinate axis simultaneously). If you can also show that the open submanifold $\mathbb{R} \setminus \{0\}$ of $\mathbb{R}$ is *not* connected (so not every embedded submanifold is connected), you have understood that connectedness is not part of the definition.

---

# Unlocked by This

> [!tip] The Tangent Space as a Subspace *(from this topic)*
> Every embedded submanifold $S \subseteq M$ has, at each $p \in S$, a [[Def - Tangent Space of a Submanifold|tangent space]] $T_p S$ that sits canonically as a linear subspace of $T_p M$ — the image of the differential $d\iota_p$ of the inclusion. This is what makes "the tangent space of the sphere" or "the tangent space of $\mathrm{O}(n)$ at the identity" a well-defined subspace of an ambient tangent space.

> [!tip] Manifolds with Boundary as Submanifolds *(from Differential Geometry)*
> The boundary $\partial M$ of a smooth manifold with boundary is a properly embedded codimension-$1$ submanifold of $M$ (without boundary). This generalises: any submanifold of $M$ whose closure has a smooth boundary inherits a "submanifold with boundary" structure.

> [!tip] Lie Subgroups *(from [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie Theory]])*
> An **(embedded) Lie subgroup** of a Lie group $G$ is a subgroup that is also an embedded submanifold. The Closed Subgroup Theorem says: every closed subgroup of a Lie group is automatically an embedded Lie subgroup. This is the source of the classification of matrix Lie groups.

> [!tip] Submanifolds and Integration *(from Differential Geometry IX)*
> Once $S$ is known to be an embedded $k$-submanifold, differential $k$-forms can be integrated over it — this is the setting for Stokes's theorem on manifolds, developed in [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]].
