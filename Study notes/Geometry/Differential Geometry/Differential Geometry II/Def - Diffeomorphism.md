---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - Homeomorphism"
tags: [geometry, differential-geometry]
---

# Notation

$M$ and $N$ denote smooth manifolds. $F : M \to N$ is a map. We write $M \approx N$ to mean $M$ and $N$ are diffeomorphic. The set of diffeomorphisms $M \to M$ forms a group under composition denoted $\operatorname{Diff}(M)$. The full registry is on [[Differential Geometry II — Smooth Maps and Partitions of Unity]].

---

# Axiom Motivation

In every category, two objects are considered "the same" when there is an isomorphism between them. For sets, the isomorphisms are bijections; for groups, the isomorphisms are bijective homomorphisms; for topological spaces, the isomorphisms are homeomorphisms. The natural question for smooth manifolds: what should an isomorphism be?

The smooth-manifold structure on a topological space $M$ consists of a maximal smooth atlas (see [[Def - Smooth Atlas and Smooth Structure]]). An isomorphism of smooth manifolds should preserve both the topology and the smooth structure. So it should be:

(1) A bijection (set isomorphism).
(2) A homeomorphism (topological isomorphism).
(3) Compatible with the smooth structures, in a sense that makes the two atlases interchangeable.

The first two requirements are familiar. The third is the new content. The clean formulation is that both $F : M \to N$ and $F^{-1} : N \to M$ should be smooth in the sense of [[Def - Smooth Map between Manifolds]]. We take this as the definition.

*Why both directions?* Because smoothness is not a symmetric condition: a smooth bijection need not have a smooth inverse, as the standard example $F : \mathbb{R} \to \mathbb{R}$, $F(x) = x^3$ illustrates. $F$ is smooth, bijective, with continuous inverse $F^{-1}(y) = y^{1/3}$. The inverse is not differentiable at $0$ (its first derivative blows up), let alone smooth. So if we only demanded $F$ smooth + bijective, we would identify manifolds that are *not* really isomorphic as smooth structures — $\mathbb{R}$ with two different smooth structures might falsely become "isomorphic". (In fact, $\mathbb{R}$ has only one smooth structure up to diffeomorphism, but verifying this requires the two-sided definition.)

*What goes wrong with a smooth bijection whose inverse fails smoothness?* The differential $dF_p$ may fail to be invertible at some point $p$ (in the case $F(x) = x^3$, $dF_0 = 0$). At such a point, the inverse function theorem fails, and $F^{-1}$ has nowhere to find its smoothness. The condition "$F^{-1}$ is smooth" is logically independent of "$F$ is smooth" — it is a separate demand and must be stated explicitly.

*Why not demand only that the differential is everywhere invertible?* This is a sufficient condition for the inverse to be smooth (by the inverse function theorem locally), provided $F$ is also bijective. So "smooth bijection with invertible differential everywhere" $\Leftrightarrow$ "diffeomorphism", and the two are equivalent characterizations. The advantage of demanding "$F^{-1}$ smooth" directly is that it makes the symmetry between $F$ and $F^{-1}$ manifest and avoids the need for the inverse function theorem to verify the definition. The differential-based characterization belongs to [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]] where the inverse function theorem on manifolds is developed.

*Why is this the right notion of equivalence?* Two diffeomorphic manifolds are interchangeable as smooth structures — they have isomorphic $C^\infty$ algebras, isomorphic tangent bundles, identical differential-topological invariants. Any smooth-structure question about one has a corresponding answer for the other. By contrast, a homeomorphism of smooth manifolds may not preserve smooth structures (consider exotic $\mathbb{R}^4$'s, which are homeomorphic but not diffeomorphic to standard $\mathbb{R}^4$). So diffeomorphism is strictly finer than homeomorphism, and it is the correct equivalence relation for the smooth category.

---

# The Definition

Let $M$ and $N$ be smooth manifolds. A map $F : M \to N$ is a **diffeomorphism** if

(1) $F$ is smooth;
(2) $F$ is bijective;
(3) $F^{-1} : N \to M$ is smooth.

Two manifolds $M$ and $N$ are **diffeomorphic**, written $M \approx N$, if there exists a diffeomorphism $F : M \to N$.

The set of diffeomorphisms $M \to M$ — *the diffeomorphism group* — is denoted $\operatorname{Diff}(M)$. Under composition it is a group with identity $\operatorname{id}_M$; for any $M$ of positive dimension, $\operatorname{Diff}(M)$ is an infinite-dimensional non-abelian group of central importance in geometry, topology, and physics (it is the symmetry group of $M$ as a smooth object, and the gauge group of general relativity is its restriction to spacetime).

**Equivalent characterization (Lee Proposition 2.15 / DG IV):** $F$ is a diffeomorphism if and only if $F$ is a smooth bijection whose differential $dF_p : T_p M \to T_{F(p)} N$ is invertible at every $p \in M$. The forward direction is straightforward; the reverse direction uses the inverse function theorem applied at every point. This characterization belongs more naturally to [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]].

---

# Categorical Definition

A diffeomorphism is precisely an **isomorphism in the category $\mathbf{Man}^\infty$** of smooth manifolds and smooth maps. The categorical definition of isomorphism — an arrow with a two-sided inverse — unfolds, in this category, to (1) the arrow $F$ is smooth, (2) it has an inverse, and (3) the inverse is also smooth.

The forgetful functor $\mathbf{Man}^\infty \to \mathbf{Top}$ sends a diffeomorphism to a homeomorphism, but is *not* full: there exist homeomorphisms between smooth manifolds that are not diffeomorphisms. The most spectacular instance is the existence of **exotic smooth structures on $\mathbb{R}^4$** (Donaldson–Freedman, 1984): there are uncountably many smooth manifold structures on the topological space $\mathbb{R}^4$, no two of which are diffeomorphic, but all of which are homeomorphic to standard $\mathbb{R}^4$. Even more startling: **Milnor's exotic spheres** (1956) — the topological $7$-sphere admits exactly $28$ distinct smooth structures up to orientation-preserving diffeomorphism. The category $\mathbf{Man}^\infty$ has strictly more isomorphism classes than $\mathbf{Top}$ restricted to manifold spaces.

The **diffeomorphism group** $\operatorname{Diff}(M)$ is the automorphism group of $M$ in $\mathbf{Man}^\infty$. It carries no natural finite-dimensional smooth structure (it is genuinely infinite-dimensional), but it is a Fréchet manifold and a topological group.

---

# Relate to Other Fields / Compression

A diffeomorphism is **the smooth-category analogue of a homeomorphism**: just as homeomorphisms are the isomorphisms of topological spaces, diffeomorphisms are the isomorphisms of smooth manifolds. The structural pattern *"isomorphism = bijective morphism in both directions"* recurs across categories: group isomorphism (bijective homomorphism with bijective-homomorphism inverse), linear isomorphism (bijective linear map with bijective-linear inverse), homeomorphism (bijective continuous with bijective-continuous inverse). The "in both directions" clause is automatic in some categories (linear algebra over a field, where the inverse of a bijective linear map is automatically linear) and not in others (smooth manifolds, where the inverse of a smooth bijection may not be smooth).

A diffeomorphism is also **a change of coordinates** on a manifold. The chart maps themselves are diffeomorphisms from $U \subseteq M$ to $\widetilde U \subseteq \mathbb{R}^m$, and the transition maps are diffeomorphisms between Euclidean open sets. So the smooth-atlas structure on $M$ can be viewed as a covering of $M$ by patches, with diffeomorphisms specifying how the patches glue together.

**True name:** *a diffeomorphism is "two manifolds, indistinguishable as smooth objects"*. The official definition is symmetric — smooth bijection with smooth inverse — but the operational meaning is that everything you could ever ask about $M$ as a smooth manifold has the same answer for $N$, and vice versa. The diffeomorphism gives the explicit translation between the two languages.

---

# Examples / Corollaries

**Is an instance: $\mathbb{R}^n \approx B^n$, the open unit ball.** The map $F : B^n \to \mathbb{R}^n$, $F(x) = x/\sqrt{1 - |x|^2}$, with inverse $G(y) = y/\sqrt{1 + |y|^2}$, is a diffeomorphism. Both maps are smooth (rational functions of smooth functions with non-vanishing denominators), and they are inverse to each other (straightforward calculation). So the open ball is diffeomorphic to all of $\mathbb{R}^n$ — open balls and $\mathbb{R}^n$ are not distinguished by smooth geometry.

**Is an instance: a chart map.** Every smooth chart $\varphi : U \to \widetilde U$ is a diffeomorphism (where $\widetilde U \subseteq \mathbb{R}^m$ has its standard smooth structure). The coordinate representation in the chart pair $((U, \varphi), (\widetilde U, \operatorname{id}))$ is the identity, manifestly smooth in both directions.

**Is an instance: stereographic projection.** The stereographic projection from the north pole $\sigma_N : S^n \setminus \{N\} \to \mathbb{R}^n$ is a diffeomorphism. The map and its inverse are explicit rational functions and are both smooth.

**Is an instance: rotation of the sphere.** Any element $R \in \operatorname{SO}(n+1)$ acts on $S^n \subseteq \mathbb{R}^{n+1}$ by restriction, giving a diffeomorphism $S^n \to S^n$. The smoothness of $R$ as a linear map of $\mathbb{R}^{n+1}$ restricts to smoothness on $S^n$; its inverse $R^{-1}$ is also in $\operatorname{SO}(n+1)$, hence also smooth. So $\operatorname{SO}(n+1)$ embeds in $\operatorname{Diff}(S^n)$.

**Is NOT an instance: $F : \mathbb{R} \to \mathbb{R}$, $F(x) = x^3$.** This is smooth and bijective, with continuous inverse $F^{-1}(y) = y^{1/3}$. But the inverse is **not smooth** at $0$ — its derivative $\tfrac{1}{3} y^{-2/3}$ blows up. So $F$ is *not* a diffeomorphism, even though it is a "smooth homeomorphism" in the loose sense. *This non-example is the standard reminder that smooth bijection $\not\Rightarrow$ diffeomorphism.* The failure can be diagnosed: $dF_0 = 0$, so the differential is not invertible at $0$.

**Is NOT an instance: a homeomorphism between manifolds with different smooth structures.** Take $\mathbb{R}$ with its standard smooth structure $\mathcal{A}_1$ and with the smooth structure $\mathcal{A}_2$ in which the chart is $x \mapsto x^3$ (Lee Example 1.23). The identity map $(\mathbb{R}, \mathcal{A}_1) \to (\mathbb{R}, \mathcal{A}_2)$ is a homeomorphism but *not* a diffeomorphism: in $\mathcal{A}_2$, the function $x^{1/3}$ is smooth (since the chart $x \mapsto x^3$ pulls it back to $x$), but the identity sends this smooth function to itself in $\mathcal{A}_1$, where $x^{1/3}$ is *not* smooth at $0$. However, the map $F : (\mathbb{R}, \mathcal{A}_1) \to (\mathbb{R}, \mathcal{A}_2)$, $F(x) = x^{1/3}$, *is* a diffeomorphism — its coordinate representation in the chart pair (identity on $\mathcal{A}_1$, $x \mapsto x^3$ on $\mathcal{A}_2$) is the identity. So the two smooth structures on $\mathbb{R}$ are diffeomorphic, even though the identity is not the diffeomorphism between them.

**Corollary (composition of diffeomorphisms).** The composition of two diffeomorphisms is a diffeomorphism. Both the map and its inverse are smooth (compositions of smooth maps).

**Corollary (diffeomorphic is an equivalence relation).** $M \approx M$ (the identity), $M \approx N \Rightarrow N \approx M$ (inverse), $M \approx N \approx P \Rightarrow M \approx P$ (composition). This is Lee's Proposition 2.15(e).

**Corollary (diffeomorphism invariance of dimension).** If $F : M \to N$ is a diffeomorphism, then $\dim M = \dim N$. Proof: pick $p \in M$, charts $(U, \varphi)$ around $p$ and $(V, \psi)$ around $F(p)$; the coordinate representation $\widehat F = \psi \circ F \circ \varphi^{-1}$ is a diffeomorphism between open subsets of $\mathbb{R}^m$ and $\mathbb{R}^n$, and an elementary result (Brouwer's invariance of dimension, or simply that a $C^1$ diffeomorphism preserves dimension via the Jacobian) forces $m = n$.

**Corollary (restriction).** The restriction of a diffeomorphism to an open submanifold is a diffeomorphism onto its image.

**Calibration check.** Verify the following: (i) the map $F(x) = x^3$ on $\mathbb{R}$ (standard smooth structure on both sides) is a smooth bijection but not a diffeomorphism — exhibit the obstruction. (ii) Stereographic projection $S^2 \setminus \{N\} \to \mathbb{R}^2$ is a diffeomorphism — write down the inverse and check both directions are smooth. (iii) $\mathbb{R}^2$ and $\mathbb{R}^3$ are not diffeomorphic (invoke dimension). (iv) Two open intervals $(a, b)$ and $(c, d)$ in $\mathbb{R}$ are always diffeomorphic — exhibit a diffeomorphism (e.g., the unique affine map).

---

# Unlocked by This

> [!tip] Exotic Smooth Structures *(from Differential Topology)*
> Different smooth structures on the same topological manifold can be non-diffeomorphic. Milnor's discovery (1956) of $28$ distinct smooth structures on $S^7$, and Donaldson–Freedman's discovery (1984) of *uncountably many* smooth structures on $\mathbb{R}^4$, are central results of low-dimensional topology. The classification of smooth structures up to diffeomorphism is one of the deepest projects in geometric topology.

> [!tip] The Diffeomorphism Group $\operatorname{Diff}(M)$ *(from Geometry / Physics)*
> $\operatorname{Diff}(M)$ is the symmetry group of $M$ as a smooth object. In general relativity, the diffeomorphism group of spacetime is the gauge group of the theory — physical fields are equivalence classes under the action of $\operatorname{Diff}(M)$. The infinite-dimensional structure of $\operatorname{Diff}(M)$ is studied via its Lie algebra of smooth vector fields (see [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket|DG V]]).

> [!tip] Local Diffeomorphism and the Inverse Function Theorem *(from Differential Geometry)*
> A smooth map $F : M \to N$ is a **local diffeomorphism at $p$** if it restricts to a diffeomorphism on some open neighbourhood of $p$. The inverse function theorem on manifolds states that $F$ is a local diffeomorphism at $p$ if and only if $dF_p$ is invertible. This is developed in [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]].

> [!tip] Mapping Class Group *(from Algebraic Topology)*
> The **mapping class group** $\operatorname{MCG}(M) = \pi_0(\operatorname{Diff}(M))$ is the group of diffeomorphisms modulo smooth isotopy. For a closed orientable surface of genus $g$, $\operatorname{MCG}$ is a discrete group whose structure is the central topic of low-dimensional topology and the theory of moduli spaces of Riemann surfaces.
