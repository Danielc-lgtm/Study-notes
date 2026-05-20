---
type: definition
subject: topology
prereqs:
  - "Def - Topological Group"
  - "Def - Subspace Topology"
  - "Def - Continuous Map"
tags: [analysis, topology, group, topological-group]
---

# Notation

$G, G'$ topological groups; $H \leq G$ a subgroup. $f : G \to G'$ a homomorphism. An action of $G$ on a space $X$ is denoted $g \cdot x$ or $g(x)$. $G(x) = \{g \cdot x : g \in G\}$ is the orbit; $G_x = \{g \in G : g \cdot x = x\}$ is the isotropy subgroup. The full registry is on the topic page.

---

# Axiom Motivation

Once a topological group $G$ is defined, three natural derived notions arise. First, a *subgroup* that is closed under the topology — a sub-object inheriting both the algebraic and topological structure. Second, a *map between topological groups* that respects both structures — a morphism in the category of topological groups. Third, an *action of $G$ on a topological space $X$* — a continuous group homomorphism from $G$ into the homeomorphism group of $X$, but viewed as a single continuous map $G \times X \to X$.

For each of these, the axiom is "respect both structures". A topological subgroup is a subgroup (algebra) carrying the subspace topology (topology); a continuous homomorphism is a group homomorphism (algebra) that is also continuous (topology); a continuous action is a group action (algebra) that is continuous as a map of topological spaces (topology). The pattern is universal: every algebraic/topological notion has a topological-group version obtained by requiring continuity of the relevant operations.

The subspace topology is the right choice for subgroups: it ensures that the inclusion $H \hookrightarrow G$ is continuous (any other choice would either be discontinuous or strictly coarser), and it is the unique topology making this true with the minimum extra structure. Importantly, $H$ might not be closed in $G$ (e.g., $\mathbb{Q} \leq \mathbb{R}$ is a subgroup but not closed). The *closure* of a subgroup is itself a subgroup (see [[Thm - Closure of a Subgroup is a Subgroup]]), so closed subgroups are a natural special case.

For homomorphisms, "continuous" is the natural addition. The kernel of a continuous homomorphism is a closed normal subgroup (preimage of $\{e\}$ under a continuous map to a Hausdorff space), and the first isomorphism theorem of group theory has a topological refinement: if $\varphi : G \to G'$ is a continuous open surjection with kernel $K$, then $G/K \cong G'$ as topological groups. The kernel-image factorization persists with topological structure.

For actions, the right notion is **continuous action**: the map $G \times X \to X$ is jointly continuous. This is stronger than each $g$ acting by a homeomorphism (which would be "separate continuity" of the action). Joint continuity ensures that the orbit map $g \mapsto g \cdot x$ is continuous for each $x$, that the isotropy subgroups are closed, and that the orbit space $X/G$ inherits a quotient topology with reasonable properties. When $G$ is compact and the action is continuous, the orbit map $G/G_x \to G(x)$ is a homeomorphism (Proposition 15.14 in Bredon — compact + Hausdorff continuous bijection upgrade).

The three notions interact: a continuous action of $G$ on $X$ is equivalent to a continuous homomorphism $G \to \operatorname{Homeo}(X)$ when $\operatorname{Homeo}(X)$ carries the compact-open topology (under reasonable hypotheses on $X$).

---

# The Definition

**Topological subgroup.** A **topological subgroup** of a topological group $G$ is a subset $H \subseteq G$ which is:

1. A subgroup of $G$ in the algebraic sense: closed under multiplication and inversion, containing $e$;
2. Equipped with the subspace topology inherited from $G$.

The subspace topology makes $H$ itself a topological group: multiplication and inversion in $H$ are restrictions of those in $G$, hence continuous.

A subgroup $H$ is **closed** if it is closed as a subset of $G$; **normal** if $gHg^{-1} = H$ for all $g \in G$ (the algebraic notion).

**Continuous homomorphism.** A **continuous homomorphism** between topological groups $G$ and $G'$ is a map $f : G \to G'$ that is:

1. A group homomorphism: $f(gh) = f(g)f(h)$ for all $g, h$ (which forces $f(e) = e'$ and $f(g^{-1}) = f(g)^{-1}$);
2. Continuous as a map of topological spaces.

A **topological group isomorphism** is a continuous homomorphism that is also a homeomorphism (equivalently, a continuous group isomorphism whose inverse is continuous).

**Continuous action.** A **continuous (left) action** of a topological group $G$ on a topological space $X$ is a continuous map
$$\alpha : G \times X \to X, \quad (g, x) \mapsto g \cdot x$$
satisfying the group action axioms:

1. $(gh) \cdot x = g \cdot (h \cdot x)$ for all $g, h \in G, x \in X$;
2. $e \cdot x = x$ for all $x \in X$.

For $x \in X$, the **orbit** of $x$ is $G(x) = G \cdot x = \{g \cdot x : g \in G\} \subseteq X$. The **isotropy** (or **stabilizer**) of $x$ is $G_x = \{g \in G : g \cdot x = x\} \leq G$. The action is **transitive** if there is a single orbit (i.e., $G(x) = X$ for one, hence every, $x$). The action is **effective** (or **faithful**) if $g \cdot x = x$ for every $x$ implies $g = e$.

**Quotient group.** If $H \trianglelefteq G$ is a closed normal subgroup, the **quotient group** $G/H$ (left cosets $gH$) with the quotient topology induced by $\pi : G \to G/H$ is a topological group (Proposition 15.12 in Bredon). The projection $\pi$ is continuous and open.

---

# Relate to Other Fields / Compression

The triple (subgroup, homomorphism, action) is the standard package in any group-theoretic context. In abstract category theory: subgroups are subobjects, homomorphisms are morphisms, actions are functors $G \to \mathbf{Top}$ when $G$ is treated as a one-object category. The topological-group versions are the same notions in the category of topological groups.

In **representation theory**, a continuous action of $G$ on a vector space $V$ is a **continuous representation** of $G$ — a continuous homomorphism $G \to \operatorname{GL}(V)$. The classification of irreducible continuous representations is the central problem (solved for compact groups by the Peter-Weyl theorem).

In **homogeneous space theory**, the quotient $G/H$ for a closed subgroup $H$ is a **homogeneous space**: $G$ acts transitively on it by left multiplication. Every transitive $G$-action arises this way (up to equivalence), so $G/H$ parametrize the transitive $G$-spaces.

---

# Examples and Corollaries

**Is an instance — $\operatorname{SO}(n) \leq \operatorname{O}(n) \leq \operatorname{GL}_n(\mathbb{R})$.** Each is a closed subgroup of the next, with the subspace topology. $\operatorname{O}(n)$ is closed in $\operatorname{GL}_n(\mathbb{R})$ (cut out by polynomial equations $AA^T = I$); $\operatorname{SO}(n)$ is closed in $\operatorname{O}(n)$ (cut out by $\det A = 1$).

**Is an instance — continuous homomorphism $\det : \operatorname{GL}_n(\mathbb{R}) \to \mathbb{R}^\times$.** The determinant is a continuous homomorphism (polynomial expression). Its kernel is $\operatorname{SL}_n(\mathbb{R})$ (closed normal subgroup). The first isomorphism theorem gives $\operatorname{GL}_n(\mathbb{R}) / \operatorname{SL}_n(\mathbb{R}) \cong \mathbb{R}^\times$ as topological groups.

**Is an instance — $\operatorname{O}(n)$ acting on $S^{n-1}$.** The standard orthogonal action $\operatorname{O}(n) \times S^{n-1} \to S^{n-1}$, $(A, x) \mapsto Ax$, is continuous (matrix-vector multiplication is polynomial). The action is transitive (any unit vector can be mapped to any other) with isotropy $\operatorname{O}(n-1)$ at $(0, \dots, 0, 1)$. So $\operatorname{O}(n)/\operatorname{O}(n-1) \cong S^{n-1}$ as a homogeneous space (Proposition 15.14 with $G$ compact).

**Is an instance — $\mathbb{Z}$ acting on $\mathbb{R}$ by translation.** $\mathbb{Z} \times \mathbb{R} \to \mathbb{R}$, $(n, x) \mapsto x + n$, is continuous. Orbits are $\mathbb{Z}$-cosets; the orbit space is $\mathbb{R}/\mathbb{Z} \cong S^1$.

**Is NOT an instance of a closed subgroup — $\mathbb{Q} \leq \mathbb{R}$.** $\mathbb{Q}$ is a topological subgroup of $\mathbb{R}$ (algebraic subgroup with subspace topology), but it is *not* closed in $\mathbb{R}$ — its closure is all of $\mathbb{R}$. So topological subgroups need not be closed.

**Is NOT an instance of a continuous homomorphism — a non-measurable additive function.** A function $f : \mathbb{R} \to \mathbb{R}$ with $f(x + y) = f(x) + f(y)$ but not continuous exists (using the axiom of choice, via a Hamel basis). It is an algebraic homomorphism but not a topological one. Continuous homomorphisms $\mathbb{R} \to \mathbb{R}$ are exactly $x \mapsto cx$ for $c \in \mathbb{R}$.

**Corollary — kernels of continuous homomorphisms are closed normal subgroups.** $\ker f = f^{-1}(\{e'\})$, the preimage of a closed set (singleton in Hausdorff) under a continuous map, is closed. Normality is the standard algebraic fact.

**Corollary — orbits of compact group actions are closed.** If $G$ is compact and acts continuously on Hausdorff $X$, the orbit map $g \mapsto g \cdot x$ from $G$ to $X$ has image $G(x)$, which is the continuous image of a compact space, hence compact, hence closed in the Hausdorff $X$.

**Corollary — homogeneous space structure.** If $G$ is compact and acts transitively on Hausdorff $X$ with isotropy $G_x$ at $x$, then $G/G_x \cong X$ via $gG_x \mapsto g \cdot x$ (continuous bijection from compact to Hausdorff, hence homeomorphism by [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]]). This is Bredon's Proposition 15.14.

**Calibration check.** Verify: $\operatorname{O}(n)/\operatorname{O}(n-1) \cong S^{n-1}$, $\operatorname{U}(n)/\operatorname{U}(n-1) \cong S^{2n-1}$, $\operatorname{Sp}(n)/\operatorname{Sp}(n-1) \cong S^{4n-1}$ (each via the homogeneous space identification at the standard north pole). Verify the Stiefel manifold $V_{n,k}$ of orthonormal $k$-frames in $\mathbb{R}^n$ is $\operatorname{O}(n)/\operatorname{O}(n-k)$.

---

# Unlocked by This

> [!tip] Homogeneous Space *(from Differential Geometry)*
> A **homogeneous space** for a topological group $G$ is a space $X$ with a transitive $G$-action. Every homogeneous space is of the form $G/H$ for $H$ the isotropy of a point. Spheres, projective spaces, Grassmannians, and Stiefel manifolds are all homogeneous spaces.

> [!tip] Principal Bundle *(from Differential Geometry)*
> A **principal $G$-bundle** is a fiber bundle $P \to B$ with a free continuous $G$-action on $P$ whose orbits are exactly the fibers. The classifying space $BG$ parameterizes principal $G$-bundles up to homotopy; this is the topological foundation of gauge theory.

> [!tip] Continuous Representation *(from Representation Theory)*
> A **continuous representation** of $G$ on a topological vector space $V$ is a continuous homomorphism $G \to \operatorname{GL}(V)$. For compact $G$, every continuous representation decomposes into irreducibles, all finite-dimensional (Peter-Weyl). For noncompact $G$, the theory is much richer.
