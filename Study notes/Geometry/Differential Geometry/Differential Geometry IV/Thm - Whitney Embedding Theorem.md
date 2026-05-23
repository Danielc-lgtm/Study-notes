---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Immersion, Submersion, and Embedding"
  - "Def - Embedded Submanifold"
  - "Def - Partition of Unity"
  - "Thm - Sard's Theorem"
  - "Thm - Existence of Smooth Bump Functions"
  - "Def - Compact Space"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold (without boundary, by our convention). A **smooth embedding** $F : M \to \mathbb{R}^N$ is a smooth immersion that is a homeomorphism onto its image (with the subspace topology from $\mathbb{R}^N$). The embedding is **proper** if preimages of compact sets are compact; equivalently the image is closed in $\mathbb{R}^N$. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

---

# Statement

> **Theorem (Weak Whitney Embedding Theorem).** Every smooth $n$-manifold (without boundary) admits a proper smooth embedding into $\mathbb{R}^{2n+1}$.

> **Theorem (Compact case).** Every compact smooth $n$-manifold admits a smooth embedding into $\mathbb{R}^{2n+1}$.

> **Theorem (Strong Whitney Embedding Theorem).** For $n \geq 1$, every smooth $n$-manifold admits a smooth embedding into $\mathbb{R}^{2n}$.

> **Theorem (Whitney Immersion Theorem).** Every smooth $n$-manifold admits a smooth immersion into $\mathbb{R}^{2n}$.

The weak theorem is the version we prove here (the easier "$2n+1$" bound); the strong theorem requires more sophisticated algebraic-topological techniques.

---

# Motivation

This theorem **justifies the picture of manifolds as subsets of Euclidean space**. Before Whitney's 1936 proof, it was unclear whether the abstract definition of a smooth manifold (Hausdorff, second-countable, locally Euclidean with smooth transition functions) was strictly more general than "smooth submanifold of $\mathbb{R}^N$" — i.e., whether there were abstract manifolds that could not be embedded in any Euclidean space. Whitney showed there are not: every smooth manifold sits as a properly embedded submanifold of some $\mathbb{R}^N$, and in fact of $\mathbb{R}^{2n+1}$ for an $n$-manifold.

This means the abstract smooth-manifold theory and the Euclidean-submanifold theory describe the same class of objects. The two viewpoints differ only in what they emphasise: the abstract definition makes differential-geometric properties (smoothness of transition maps, partition of unity) front and centre, freeing the geometry from any chosen embedding; the embedded viewpoint makes computations concrete by sitting inside a known ambient space. Whitney's theorem is the bridge.

Why specifically $\mathbb{R}^{2n+1}$? The dimension $2n+1$ has a natural interpretation: a smooth embedding $F : M \to \mathbb{R}^N$ is determined by the data of $N$ smooth functions $F^1, \dots, F^N : M \to \mathbb{R}$, subject to two conditions — *injectivity of $F$* (a condition on pairs of points) and *injectivity of $dF_p$* (a condition on tangent vectors). Each condition is "generic-codimension $n$": failure of injectivity at a point pair is a codimension-$2n$ condition in $M \times M \setminus \Delta$, and failure of immersion at a point is a codimension-$n$ condition. So the "bad set" for both conditions has dimension at most $2n$, and to generically avoid the bad set you need $N > 2n$, i.e., $N \geq 2n + 1$. The proof makes this counting argument precise via Sard's theorem.

The strong theorem ($\mathbb{R}^{2n}$) requires deeper tools — Whitney came back to it in 1944 with additional techniques (the "Whitney trick" for resolving self-intersections, which works for $n \geq 2$). For $n = 1$ the strong theorem says every $1$-manifold embeds in $\mathbb{R}^2$, which is true (the only connected $1$-manifolds without boundary are $\mathbb{R}$ and $S^1$, and both sit in $\mathbb{R}^2$). The strong theorem is not always optimal: Wall showed every $3$-manifold embeds in $\mathbb{R}^5$ (not just $\mathbb{R}^6$). The "best" embedding dimension is a deep topological invariant of $M$.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$M$ is a smooth manifold" — already very broad. The skill is identifying the kind of structure on $M$ that the proof actually leverages.

The first disguised source is **a smooth atlas with compact closures.** Property $B$: $M$ admits a smooth atlas with countably many coordinate balls whose closures are compact. By Hausdorff + second-countable, every smooth manifold has this property — it is the foundation of partition of unity arguments. The proof of Whitney's theorem assembles local coordinate embeddings (from charts) into a global embedding using partitions of unity, and this requires the countable-cover structure.

The second disguised source is **an exhaustion function.** Property $B$: $M$ admits a smooth proper function $f : M \to [0, \infty)$ (an *exhaustion function*). Every smooth manifold admits one (constructed via partition of unity). The proof of the non-compact case of Whitney's theorem uses the exhaustion function to control the embedding at infinity, ensuring properness.

The third disguised source is **a finite chart cover for compact manifolds.** Property $B$: $M$ is compact, so it admits a finite atlas. In this case the proof simplifies dramatically — no exhaustion or countable assembly is needed; one just concatenates finitely many local coordinate embeddings with partition-of-unity weights.

**Targets (Output Amplification)**

The conclusion is "$M$ embeds properly in $\mathbb{R}^{2n+1}$".

Combine with **the goal of doing geometry on $M$ concretely.** Property $D$: you want to develop a theory of curvature, geodesics, volume on $M$. The amplified result $E$: with $M$ realised as a submanifold of $\mathbb{R}^{2n+1}$, the standard inner product on $\mathbb{R}^{2n+1}$ restricts to a Riemannian metric on $M$ (the **first fundamental form**); all of submanifold differential geometry transfers via the embedding. So Whitney provides a *constructive* way to put a Riemannian metric on $M$ (though typically not the most natural one).

Combine with **the goal of doing computation.** Property $D$: you want to specify a smooth function or vector field on $M$ explicitly. The amplified result $E$: with $M \subset \mathbb{R}^{2n+1}$, smooth functions on $M$ can be specified as restrictions of polynomials on $\mathbb{R}^{2n+1}$; vector fields as restrictions of vector fields on $\mathbb{R}^{2n+1}$ (suitably tangent to $M$). This is the computational content of Whitney: the abstract objects on $M$ acquire concrete polynomial / coordinate descriptions via the embedding.

Combine with **the question of intrinsic vs. extrinsic differential geometry.** Property $D$: you want to know whether a property of $M$ is *intrinsic* (depending only on $M$'s smooth structure) or *extrinsic* (depending on the embedding). The amplified result $E$: Whitney shows that *every* property can be made extrinsic (by realising $M$ via some embedding), but the question of which properties are *invariant* under change of embedding is the foundation of intrinsic differential geometry. Curvature in the embedded sense (a property of the embedding) versus the intrinsic Gaussian curvature (a property of $M$) is the canonical distinction.

---

# Why Is It True

The proof has two distinct shapes depending on whether $M$ is compact or not. We focus on the compact case for cleanness.

**The bolded one-liner mechanism summary for the compact case: partition $M$ by finitely many charts, weight each chart's coordinate functions by a bump function localised to the chart, and concatenate everything into a single map to $\mathbb{R}^{nm + m}$; the bump functions force injectivity and the coordinate maps force immersion, while the chart-bump packaging keeps everything smooth. Then use Sard repeatedly to project down to $\mathbb{R}^{2n+1}$.**

Here is the compact-case construction.

**Step A (cover $M$ with regular coordinate balls).** Since $M$ is compact, choose finitely many smooth charts $(U_1, \varphi_1), \dots, (U_m, \varphi_m)$ such that the $U_i$ cover $M$. By shrinking, arrange that each $U_i$ contains a smaller coordinate ball $V_i$ on which the coordinate map's image $\varphi_i(V_i)$ is also a ball, and the $V_i$ still cover $M$.

**Step B (cutoff functions).** For each $i$, by [[Thm - Existence of Smooth Bump Functions|the smooth bump function existence theorem]], let $\rho_i : M \to [0, 1]$ be a smooth function that is $1$ on $\bar V_i$ and supported in $U_i$.

**Step C (assembled map).** Define $F : M \to \mathbb{R}^{nm + m}$ by
$$F(p) = (\rho_1(p) \varphi_1(p), \dots, \rho_m(p) \varphi_m(p), \rho_1(p), \dots, \rho_m(p)),$$
where $\rho_i(p) \varphi_i(p)$ is understood to be zero outside $U_i$ (since $\rho_i$ vanishes there). This is a smooth map from $M$ to $\mathbb{R}^{nm + m}$.

**Step D (verify injectivity).** Suppose $F(p) = F(q)$. Then $\rho_i(p) = \rho_i(q)$ for all $i$. Since the $V_i$ cover $M$, some $\rho_i$ equals $1$ at $p$ — and hence at $q$, forcing $q \in U_i$ (where $\rho_i$ is supported). In this $U_i$, the coordinate components give $\varphi_i(p) = \varphi_i(q)$ (since $\rho_i(p) = \rho_i(q) = 1$); since $\varphi_i$ is a [[Def - Homeomorphism|homeomorphism]], $p = q$.

**Step E (verify immersion).** At any $p \in V_i$, $\rho_i$ equals $1$ in a neighbourhood of $p$, so $d(\rho_i \varphi_i)_p = d\varphi_{i\,p}$, which is a coordinate map's differential and is injective. The corresponding components of $dF_p$ are therefore injective. (In fact $dF_p$ is injective on the $n$-dimensional tangent space $T_p M$ because $d(\rho_i \varphi_i)_p$ already is.)

**Step F (compact case: $F$ is an embedding).** $F$ is a smooth injective immersion. Since $M$ is compact, $F$ is automatically a smooth embedding (compact-domain injective immersion is an embedding by [[Def - Immersion, Submersion, and Embedding|Lee's Proposition 4.22(c)]]).

**Step G (dimension reduction via Sard).** $F$ embeds $M$ in $\mathbb{R}^{nm + m}$, but we want to embed in $\mathbb{R}^{2n+1}$. Apply Sard repeatedly: at each step, project from $\mathbb{R}^{N}$ to $\mathbb{R}^{N-1}$ along a direction $v$. The "bad" directions — those for which the projection fails to be injective or an immersion — form a set of dimension at most $2n$ in $\mathbb{RP}^{N-1}$ (the projective space of directions), which has dimension $N - 1$. As long as $N - 1 > 2n$, i.e., $N > 2n + 1$, Sard guarantees a "good" direction exists. Repeat until $N = 2n + 1$.

The non-compact case is similar but uses an exhaustion function to control the embedding at infinity. The exhaustion function ensures the embedding into $\mathbb{R}^{N+1}$ (with the exhaustion function as the extra coordinate) is *proper*; the dimension reduction then preserves properness because the projections are along "horizontal" directions.

**Why is Sard the engine?** The proof reduces the existence of a "good" embedding direction to a measure-zero / density argument: for each $v \in \mathbb{RP}^{N-1}$, the projection $\pi_v$ fails to be an immersion or fails injectivity on a set of $v$'s that has measure zero in $\mathbb{RP}^{N-1}$ (by Sard applied to the natural maps from $TM \setminus 0$ and $M \times M \setminus \Delta$ to $\mathbb{RP}^{N-1}$). The complement is dense, so a good $v$ exists. This is the **density-of-good-directions** application of Sard.

---

# What Makes This Hard

The non-obvious step is **Step G**, the dimension reduction via Sard. Most students follow the construction of the embedding in $\mathbb{R}^{nm + m}$ without difficulty (it is partition-of-unity bookkeeping), but the projection-by-Sard step is more subtle. The key insight is to identify the "bad set" of projection directions: a direction $v$ is bad if either (a) $v$ is the difference of two image points (projection collapses two points) or (b) $v$ is parallel to a tangent vector (projection collapses an immersion direction). Both bad sets are images of smooth maps from spaces of dimension $\leq 2n$, hence by Sard have measure zero in $\mathbb{RP}^{N-1}$ as long as $\dim \mathbb{RP}^{N-1} = N - 1 > 2n$. The most common error is forgetting either condition (a) or (b), and missing the requirement $N - 1 > 2n$ (i.e., $N > 2n + 1$, so the final $N$ is $2n + 1$).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof of the compact case.**

**High-level strategy:**
For compact $M$, cover by finitely many regular coordinate balls. Build cutoff functions concentrated on smaller balls. Assemble an embedding into $\mathbb{R}^{nm + m}$ using the cutoffs and the coordinate maps. Then project down dimension by dimension using Sard, at each step finding a projection direction avoiding the "bad set" (projection directions that kill injectivity or immersion). Stop when $N = 2n + 1$, since for $N - 1 \leq 2n$ the bad set may have positive measure.

**Subgoal decomposition:**

1. **Finite cover.** Cover $M$ by finitely many regular coordinate balls $V_1, \dots, V_m$ with closures contained in larger balls $U_i$. (Compactness gives finiteness; the size discrepancy gives room for cutoffs.)
   - *Hint:* A regular coordinate ball is one whose coordinate map's image is a Euclidean ball.

2. **Cutoff functions.** For each $i$, let $\rho_i : M \to [0,1]$ be smooth, equal to $1$ on $\bar V_i$, supported in $U_i$.
   - *Hint:* Use the smooth bump function existence theorem.

3. **Assembled map.** Define $F(p) = (\rho_i(p) \varphi_i(p), \rho_i(p))_{i = 1, \dots, m} \in \mathbb{R}^{nm + m}$ where $\rho_i(p) \varphi_i(p) := 0$ outside $U_i$.
   - *Hint:* Each coordinate "$\rho_i \varphi_i$" is smooth because $\rho_i$ kills the discontinuity outside its support.

4. **Verify injectivity.** Two points $p, q \in M$ with $F(p) = F(q)$: pick $i$ with $\rho_i(p) = 1$ (possible since $\{V_i\}$ covers $M$); then $\rho_i(q) = 1$ too, so $q \in V_i \subseteq U_i$; the corresponding coordinate equation gives $\varphi_i(p) = \varphi_i(q)$, so $p = q$ by chart injectivity.
   - *Hint:* The "second batch" of coordinates (just $\rho_i$'s) provides the chart-detection.

5. **Verify immersion.** At any $p \in V_i$, $\rho_i \equiv 1$ near $p$, so $d(\rho_i \varphi_i)_p = d\varphi_{i\,p}$, injective by chart immersion.
   - *Hint:* On $V_i$, the cutoff is constant equal to $1$.

6. **Compact embedding.** $F$ is an injective smooth immersion from a compact manifold, hence a smooth embedding (Proposition 4.22(c)).
   - *Hint:* Compact-domain criterion.

7. **Reduce dimension via Sard.** From $F : M \to \mathbb{R}^N$ embedding ($N = nm + m$, large), apply iterated projection. At each step from $\mathbb{R}^N$ to $\mathbb{R}^{N-1}$:
   - The bad set of directions $v \in \mathbb{RP}^{N-1}$ where the projection $\pi_v$ fails injectivity is the image of $M \times M \setminus \Delta \to \mathbb{RP}^{N-1}$, $(p, q) \mapsto [F(p) - F(q)]$. Domain has dimension $2n$.
   - The bad set where $\pi_v$ fails to be an immersion is the image of $TM \setminus 0 \to \mathbb{RP}^{N-1}$, $(p, w) \mapsto [dF_p(w)]$. Domain has dimension $2n$.
   - By Sard (specifically Corollary 6.11 of Lee for low-dimensional sources), both bad sets have measure zero in $\mathbb{RP}^{N-1}$ as long as $\dim \mathbb{RP}^{N-1} = N - 1 > 2n$.
   - Hence good directions are dense; pick one and project. Resulting embedding is in $\mathbb{R}^{N-1}$.
   - Iterate until $N = 2n + 1$.
   - *Hint:* At $N = 2n + 1$, the bad set has dimension $2n = N - 1 = \dim \mathbb{RP}^{N-1}$, so Sard does not give it measure zero. Stop the iteration here.

---

# Lemma Decomposition

> [!note]- Lemma 1: Projection along a direction avoids injectivity-failure for generic directions
> **Statement:** Let $M \subseteq \mathbb{R}^N$ be a smooth embedded $n$-submanifold with $N > 2n + 1$. For a dense set of vectors $v \in \mathbb{R}^N \setminus \mathbb{R}^{N-1}$ (where $\mathbb{R}^{N-1}$ is identified with a hyperplane), the projection $\pi_v : M \to \mathbb{R}^{N-1}$ along $v$ is injective.
>
> **Hint:** $\pi_v$ fails injectivity iff $v$ is parallel to $p - q$ for some $p \neq q \in M$. The image of $(p, q) \mapsto [p - q]$ in $\mathbb{RP}^{N-1}$ has measure zero by Sard.
>
> **Why needed:** It is one of the two bad-set conditions in the Sard-based dimension reduction.
>
> > [!note]- Full proof
> > Consider the smooth map
> > $$\sigma : M \times M \setminus \Delta \to \mathbb{RP}^{N-1}, \quad \sigma(p, q) = [p - q],$$
> > where $\Delta = \{(p, p)\}$ is the diagonal and the bracket denotes the equivalence class in projective space. The domain has dimension $2n$; the codomain has dimension $N - 1$. Since $N > 2n + 1$, $N - 1 > 2n$, so by Sard's theorem (specifically Corollary 6.11), the image $\sigma(M \times M \setminus \Delta)$ has measure zero in $\mathbb{RP}^{N-1}$.
> >
> > For $v \notin \sigma(M \times M \setminus \Delta)$, we have $[v] \neq [p - q]$ for all distinct $p, q \in M$ — that is, $v$ is not parallel to $p - q$. So $\pi_v(p) \neq \pi_v(q)$, i.e., $\pi_v|_M$ is injective. The set of good $v$ is the complement of a measure-zero set, hence dense.

> [!note]- Lemma 2: Projection preserves immersion for generic directions
> **Statement:** Let $M \subseteq \mathbb{R}^N$ be a smooth embedded $n$-submanifold with $N > 2n + 1$. For a dense set of $v \in \mathbb{R}^N \setminus \mathbb{R}^{N-1}$, the projection $\pi_v : M \to \mathbb{R}^{N-1}$ is an immersion (i.e., $d(\pi_v)_p$ is injective on $T_p M$ at every $p$).
>
> **Hint:** $\pi_v|_M$ fails to be an immersion at $p$ iff some nonzero tangent vector $w \in T_p M$ is parallel to $v$. The image of $(p, w) \mapsto [w]$ in $\mathbb{RP}^{N-1}$ has measure zero.
>
> **Why needed:** It is the second bad-set condition in the Sard-based dimension reduction.
>
> > [!note]- Full proof
> > Consider the smooth map
> > $$\tau : TM \setminus M_0 \to \mathbb{RP}^{N-1}, \quad \tau(p, w) = [w],$$
> > where $M_0 = \{(p, 0) : p \in M\}$ is the zero section. The domain $TM \setminus M_0$ has dimension $2n$ (the tangent bundle of an $n$-manifold has dimension $2n$); the codomain $\mathbb{RP}^{N-1}$ has dimension $N - 1 > 2n$. By Sard's theorem, $\tau(TM \setminus M_0)$ has measure zero in $\mathbb{RP}^{N-1}$.
> >
> > For $v \notin \tau(TM \setminus M_0)$, we have $[v] \neq [w]$ for all nonzero $w \in T_p M$ and all $p$ — that is, $v$ is not parallel to any nonzero tangent vector of $M$. The differential $d\pi_v$ on $T_p M$ has kernel exactly the [[Def - Subspace|subspace]] of $T_p M$ parallel to $v$; this is $\{0\}$ by the genericity of $v$, so $d\pi_v|_{T_p M}$ is injective. Hence $\pi_v|_M$ is an immersion. The set of good $v$ is dense.

---

# Formal Proof

> [!note]- Complete formal proof (compact case)
> Let $M$ be a compact smooth $n$-manifold. We construct a smooth embedding $F : M \to \mathbb{R}^{2n+1}$.
>
> **Step 0 (initial embedding into a large Euclidean space).** Since $M$ is compact, choose finitely many smooth charts $(U_i, \varphi_i)$, $i = 1, \dots, m$, with $\varphi_i(U_i) \subseteq \mathbb{R}^n$ open, such that the $U_i$ cover $M$. For each $i$, choose a smooth open set $V_i$ with $\bar V_i \subseteq U_i$ such that the $V_i$ still cover $M$ (compactness allows this — shrink each $U_i$ slightly). For each $i$, let $\rho_i : M \to [0,1]$ be a smooth function equal to $1$ on $\bar V_i$ and supported in $U_i$ (by the [[Thm - Existence of Smooth Bump Functions|smooth bump function existence theorem]]).
>
> Define $F_0 : M \to \mathbb{R}^{nm + m}$ by
> $$F_0(p) = (\rho_1(p) \varphi_1(p), \dots, \rho_m(p) \varphi_m(p),\, \rho_1(p), \dots, \rho_m(p)),$$
> with $\rho_i(p) \varphi_i(p) := 0$ when $p \notin U_i$. Each component is smooth (because $\rho_i$ kills the discontinuity outside its support).
>
> *$F_0$ is injective.* If $F_0(p) = F_0(q)$, then $\rho_i(p) = \rho_i(q)$ for all $i$. The $V_i$ cover $M$, so $p \in V_j$ for some $j$, hence $\rho_j(p) = 1$, hence $\rho_j(q) = 1$, hence $q \in \mathrm{supp}\, \rho_j \subseteq U_j$ — in fact $q \in V_j$ (otherwise $\rho_j(q) < 1$). The coordinate component gives $\varphi_j(p) = \rho_j(p)\varphi_j(p) = \rho_j(q) \varphi_j(q) = \varphi_j(q)$, and $\varphi_j$ is injective on $U_j$, so $p = q$.
>
> *$F_0$ is an immersion.* At $p \in V_i$, $\rho_i$ is constantly $1$ on a neighbourhood, so $d(\rho_i \varphi_i)_p = d\varphi_{i\,p}$ is injective (chart differentials are [[Def - Isomorphism|isomorphisms]]). Hence $dF_{0,p}$ is injective.
>
> *$F_0$ is an embedding.* Injective smooth immersion from compact $M$ to Hausdorff $\mathbb{R}^{nm + m}$ is automatically a smooth embedding.
>
> **Step 1 (iterated projection via Sard).** Set $F = F_0$ and $N = nm + m$. While $N > 2n + 1$:
>
> By Lemmas 1 and 2, the set of "bad" projection directions in $\mathbb{RP}^{N-1}$ — those for which projection fails injectivity or fails to be an immersion — is the union of two measure-zero sets, hence measure zero (as long as $N - 1 > 2n$, which holds since $N > 2n + 1$). The set of good directions is dense.
>
> Pick a good direction $v \in \mathbb{R}^N \setminus \mathbb{R}^{N-1}$. The projection $\pi_v : F(M) \to \mathbb{R}^{N-1}$ along $v$ is a smooth injective immersion. Composing $F$ with $\pi_v$ gives a smooth injective immersion $\pi_v \circ F : M \to \mathbb{R}^{N-1}$.
>
> Set $F := \pi_v \circ F$, $N := N - 1$. Repeat.
>
> **Step 2 (termination).** The iteration terminates when $N = 2n + 1$ (we cannot iterate further since at $N = 2n + 1$ we would have $N - 1 = 2n$, equal to the dimension of the bad-set domains, so Sard does not give measure zero). The resulting $F$ is a smooth injective immersion $M \to \mathbb{R}^{2n+1}$ from a compact manifold, hence a smooth embedding.
>
> $\qquad\blacksquare$
>
> The non-compact case is similar but uses an exhaustion function as one of the embedding coordinates to ensure properness; the projection step preserves properness because the projections are "horizontal" (do not involve the exhaustion-function direction).

---

# Cross-Field Exercise Suggestions

**Riemannian metric existence.** Once $M$ is embedded in $\mathbb{R}^{2n+1}$ via Whitney, the standard inner product on $\mathbb{R}^{2n+1}$ restricts to give a Riemannian metric on $M$. So every smooth manifold admits a Riemannian metric — and the Whitney embedding provides one. This is the existence half of "every smooth manifold is Riemannian". The other approach uses partitions of unity directly on $M$ without embedding.

**Topological invariants from embeddings.** Many topological invariants of $M$ — characteristic classes, Euler characteristic, signature — have descriptions in terms of intersections of $M$ with itself in some embedding, or in terms of the normal bundle to the embedding. The Whitney embedding theorem ensures the embedding exists; the topological theory uses the existence to define the invariants.

**Computational topology.** In computational topology, manifolds are represented as simplicial complexes embedded in $\mathbb{R}^N$ for $N$ small. Whitney's theorem gives a theoretical bound on the necessary $N$ (namely $2n + 1$ for smooth $n$-manifolds), guiding choice of data structures and algorithms.

**The h-cobordism theorem and high-dimensional topology.** Smale's $h$-cobordism theorem (every simply connected $h$-cobordism is trivial in [[Def - Dimension|dimensions]] $\geq 5$) was proved using Whitney's trick for resolving self-intersections of embeddings — a refinement of the techniques behind the strong Whitney embedding theorem ($\mathbb{R}^{2n}$). The classification of simply connected high-dimensional manifolds rests on this.

---

# Bridges

- **[[Thm - Sard's Theorem|Sard's Theorem]]** — the engine. Whitney's theorem's proof is a Sard-style argument: iterated projection with Sard guaranteeing good projection directions at each step. The relationship is exact: Whitney is a consequence of Sard applied to the natural maps $M \times M \to \mathbb{RP}^{N-1}$ and $TM \to \mathbb{RP}^{N-1}$.

- **[[Def - Embedded Submanifold|Embedded Submanifold]]** — the output. The conclusion of Whitney's theorem is that $M$ is realised as an embedded submanifold of $\mathbb{R}^{2n+1}$. So Whitney is the existence theorem for the parametric representation of any smooth manifold.

- **[[Def - Immersion, Submersion, and Embedding|Smooth Embedding]]** — the structural content. The theorem produces a smooth embedding, which is the strongest form of immersion (it includes the topological-embedding condition).

- **[[Def - Compact Space|Compactness]]** — the simplifying hypothesis. For compact $M$ the proof is cleaner: no exhaustion function needed; the partition of unity is finite; the dimension reduction step works directly.

- **[[Def - Partition of Unity|Partition of Unity]]** — the technical tool. The construction of the assembled embedding uses cutoff functions (one for each chart in the cover), which form a partition of unity (after normalisation). This is the standard way of going from local to global smooth structure.

- **Whitney's later work and the strong theorem.** The strong Whitney theorem ($\mathbb{R}^{2n}$ for $n \geq 1$) requires more delicate analysis (the "Whitney trick" for cancelling double points), and is not derivable from Sard alone.

- **Nash embedding theorem** — the metric refinement. Whitney embeds smoothly; **Nash** embeds *isometrically*: any Riemannian manifold embeds isometrically into some $\mathbb{R}^N$ (with $N$ depending on dimension and regularity class). Nash's $N$ is larger than Whitney's, reflecting the additional metric constraint.

---

# Unlocked by This

> [!tip] Existence of Riemannian Metric *(from Riemannian Geometry)*
> Once $M$ is embedded in $\mathbb{R}^N$, the Euclidean inner product restricts to a Riemannian metric on $M$. So every smooth manifold admits a Riemannian metric (existence-by-Whitney). The alternative existence proof (partition of unity) does not need embedding, but Whitney's gives a *concrete* metric.

> [!tip] Characteristic Classes via Normal Bundle *(from Algebraic Topology)*
> An embedding of $M$ in $\mathbb{R}^N$ gives a **normal bundle** $\nu_M = (TM)^\perp$, a real vector bundle of rank $N - n$ over $M$. The characteristic classes of $\nu_M$ — Stiefel–Whitney, Pontryagin, Chern (for complex bundles) — are topological invariants of the embedded $M$, and they encode deep topological information about $M$ itself.

> [!tip] Cobordism and the Pontryagin–Thom Construction *(from Algebraic Topology)*
> The **Pontryagin–Thom construction** realises cobordism classes as preimages of regular values of maps from spheres into Thom spaces of universal bundles. Whitney's embedding theorem ensures that any compact manifold has the required embedding into a sphere (or its universal Thom space), which is the setup for the construction.

> [!tip] Smooth Surgery and Handle Decompositions *(from Differential Topology)*
> Smooth surgery — cutting out a tubular neighbourhood of an embedded sphere and gluing in a complementary handle — is the key operation in classifying high-dimensional manifolds. Whitney's embedding theorem ensures the necessary embedded spheres exist (in suitable manifolds), and Whitney's trick for resolving self-intersections is the key technical tool.

> [!tip] Nash's Isometric Embedding Theorem *(from Riemannian Geometry)*
> Nash strengthens Whitney to the **isometric** embedding: any Riemannian $n$-manifold embeds isometrically into $\mathbb{R}^N$ for $N$ depending on $n$ and the smoothness class (e.g., $N = n(3n+11)/2$ for smooth embeddings of compact manifolds). This realises any abstract Riemannian manifold as a "concrete" submanifold of Euclidean space with the inherited metric matching the abstract one.
