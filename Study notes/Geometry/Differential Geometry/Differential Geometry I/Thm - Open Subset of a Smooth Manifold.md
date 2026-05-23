---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Atlas and Smooth Structure"
  - "Def - Coordinate Chart and Atlas"
  - "Def - Subspace Topology"
tags: [geometry, differential-geometry]
---

# Notation

Throughout, $M$ is a smooth $n$-manifold with smooth structure $\mathcal{A}$, and $U \subseteq M$ is an open subset. The [[Def - Subspace Topology|subspace topology]] on $U$ is the one inherited from $M$. For full notation see [[Differential Geometry I — Smooth Manifolds and Atlases]].

---

# Statement

> **Theorem (Open Submanifold; Lee Example 1.26).** Let $M$ be a smooth $n$-manifold with smooth structure $\mathcal{A}$, and let $U \subseteq M$ be an open subset (with the subspace topology). Then $U$ inherits a natural smooth $n$-manifold structure, with smooth atlas
> $$\mathcal{A}_U = \{(V, \varphi|_V) : (V, \varphi) \in \mathcal{A} \text{ with } V \subseteq U\}.$$
> Endowed with this smooth structure, $U$ is called an **open submanifold** of $M$.

The conclusion is that $\mathcal{A}_U$ is a smooth atlas (its charts cover $U$, and any two are smoothly compatible), so by [[Thm - Smooth Structure from Maximal Atlas]] it determines a unique smooth structure on $U$. Equivalently, one may take the atlas of *all* charts of $M$ restricted to their intersection with $U$:
$$\mathcal{A}_U' = \{(V \cap U, \varphi|_{V \cap U}) : (V, \varphi) \in \mathcal{A}\}.$$
These two atlases determine the same smooth structure (Lee discussion before Proposition 1.17).

---

# Motivation

After defining smooth manifolds and verifying that finite products are smooth, we need a third construction: open subsets. The motivation is everywhere: $\mathrm{GL}(n, \mathbb{R})$ is the open subset of $M(n, \mathbb{R})$ where the determinant is nonzero, the upper half-plane $\{y > 0\} \subseteq \mathbb{R}^2$ is an open subset of $\mathbb{R}^2$, the orientation-preserving subgroup $\mathrm{GL}^+(n) = \{A : \det A > 0\}$ is open in $\mathrm{GL}(n)$, the complement of any closed subset of a manifold is open and inherits a smooth structure. The theorem says: all these inherit smooth manifold structures, and the inheritance is *canonical* — the same dimension, charts from the ambient manifold simply restricted.

This is the most natural construction one could hope for: an open subset is *locally* the same as the ambient manifold, so its smooth structure should be locally inherited from the ambient one. The theorem makes this precise.

The construction is also crucial structurally. The category of smooth manifolds is large; the open-subset construction is one of the few canonical ways to produce new smooth manifolds inside a given one. Combined with the **regular value theorem** ([[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]]), which gives smooth manifolds as level sets of smooth maps, and the product construction ([[Thm - Product of Smooth Manifolds is a Smooth Manifold]]), it generates essentially all the elementary examples of smooth manifolds.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a smooth manifold $M$ and an open subset $U \subseteq M$." The skill is recognizing when a subset is open in a smooth manifold.

The first source is **a subset defined by a strict inequality involving a continuous function**. If $f : M \to \mathbb{R}$ is continuous and $c \in \mathbb{R}$, then $\{p : f(p) > c\}, \{p : f(p) < c\}$ are open subsets of $M$. The most important instance: $\mathrm{GL}(n, \mathbb{R}) = \{A \in M(n, \mathbb{R}) : \det A \neq 0\}$ is the preimage of $\mathbb{R} \setminus \{0\}$ under the continuous determinant function — an open subset of $M(n, \mathbb{R}) \cong \mathbb{R}^{n^2}$. This is the source for matrix Lie groups: $\mathrm{GL}(n)$ is automatic; $\mathrm{SL}(n)$, $\mathrm{O}(n)$, $\mathrm{SU}(n)$ are *not* open but are submanifolds (via the regular value theorem).

The second source is **the complement of a closed subset**. If $K \subseteq M$ is closed, then $M \setminus K$ is open. This is the source for the *punctured manifold* $M \setminus \{p\}$ (closed singleton), the *complement of an embedded curve*, the *complement of a singular set* in an algebraic variety.

The third source is **a chart domain itself**. Every coordinate domain $U$ of a chart $(U, \varphi) \in \mathcal{A}$ is open by definition, and is therefore a smooth submanifold. This is a tautology, but a useful one: it lets us treat any chart domain as a smooth manifold in its own right and reduce questions about $M$ near a point to questions about an open subset of $\mathbb{R}^n$.

The fourth source is **the interior of a manifold with boundary**. By [[Def - Smooth Manifold with Boundary]], the interior $\operatorname{Int} M = M \setminus \partial M$ is an open subset of $M$ (the boundary is closed), and inherits a smooth structure as an open submanifold. The interior is a smooth manifold *without* boundary.

The fifth source is **a finite intersection of open sets**. Any finite intersection of open subsets is open. So the locus where multiple continuous inequalities hold simultaneously — $\{f_1 > 0\} \cap \{f_2 > 0\}$ — is open. This is used to define explicit open submanifolds with multiple constraints.

**Targets (Output Amplification)**

The first target: **an open submanifold inherits all local-property structure of the ambient manifold**. A function $f : U \to \mathbb{R}$ is smooth iff its extension by zero or its restriction from a smooth function on $M$ is smooth on $M$. Smooth vector fields on $U$ extend (locally) to smooth vector fields on $M$. The dimension of $U$ equals the dimension of $M$. *Local* differential geometry on $U$ is identical to local differential geometry on $M$.

The second target: **embeddings of open submanifolds**. The inclusion $\iota : U \hookrightarrow M$ is a smooth map ([[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]]), and is actually a *smooth embedding* — it is a smooth immersion (the differential is injective) and a homeomorphism onto its image (since the image is $U$ itself, with the subspace topology). The differential $d\iota_p : T_p U \to T_p M$ is an isomorphism for every $p \in U$, identifying $T_p U$ with $T_p M$.

The third target: **smooth structure preserved by restriction**. Anything defined globally on $M$ — Riemannian metric, vector field, differential form, smooth function — restricts to a corresponding object on $U$. This is the *restriction* operation, and it commutes with the smooth structure.

The fourth target: **smooth maps from open submanifolds**. A smooth map $f : M \to N$ restricts to a smooth map $f|_U : U \to N$. Conversely, a smooth map $g : U \to N$ does *not* extend canonically to a smooth map on all of $M$, in general — this is precisely the obstruction studied via *partitions of unity* in [[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]] (Whitney extension, smooth extension lemma).

---

# Why Is It True

The intuition is that smoothness is a *local* property: a smooth atlas is determined by its behaviour near each point, and restricting to an open subset preserves this local behaviour. The proof is largely bookkeeping.

For the Hausdorff and second-countability conditions: both are inherited by subspaces in general topology. A subspace of a Hausdorff space is Hausdorff (intersect the separating open sets with the subspace); a subspace of a second-countable space is second-countable (intersect a countable basis with the subspace).

For the locally Euclidean condition: given $p \in U$, choose a chart $(V, \varphi)$ on $M$ with $p \in V$. Since $U$ is open and $p \in V \cap U$, the intersection $V \cap U$ is open in $M$ (intersection of opens). Restricting $\varphi$ to $V \cap U$ gives a chart $(V \cap U, \varphi|_{V \cap U})$ on $U$ with image $\varphi(V \cap U) \subseteq \varphi(V)$, an open subset of $\mathbb{R}^n$. This chart has dimension $n$ (the same as $M$), so $U$ is locally Euclidean of dimension $n$.

For smooth compatibility: the transition between two restricted charts is just the restriction of the transition between the original charts, hence smooth on the (open) restricted domain. Concretely, if $(V_\alpha, \varphi_\alpha), (V_\beta, \varphi_\beta) \in \mathcal{A}$ and we form the restricted charts $(V_\alpha \cap U, \varphi_\alpha|_{V_\alpha \cap U}), (V_\beta \cap U, \varphi_\beta|_{V_\beta \cap U})$ on $U$, the transition between them is

$$\varphi_\beta|_{V_\beta \cap U} \circ (\varphi_\alpha|_{V_\alpha \cap U})^{-1} = \varphi_\beta \circ \varphi_\alpha^{-1}|_{\varphi_\alpha(V_\alpha \cap V_\beta \cap U)},$$

a restriction of the smooth ambient transition function to an open subset, hence smooth.

**The one-liner mechanism: smoothness of a function is a local property, so restricting a smooth atlas to an open subset preserves smooth compatibility.**

---

# What Makes This Hard

This theorem is one of the easiest in the chapter — the proof is largely tautological. The non-obvious point is that the same dimension $n$ is preserved: an open submanifold of an $n$-manifold is again an $n$-manifold, *not* a lower-dimensional manifold even though it is a "smaller" set. The local Euclidean structure with the same model space $\mathbb{R}^n$ is what fixes the dimension.

The other subtlety: an open submanifold is *not* a submanifold in the more general sense of [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]] — that would be an embedded submanifold of *lower* dimension, like a curve in $\mathbb{R}^2$ or a surface in $\mathbb{R}^3$. The two senses of "submanifold" are different: the open-submanifold sense (same dimension, open subset) and the embedded-submanifold sense (lower dimension, locally a level set). The terminology can be confusing; we always say "open submanifold" or "embedded submanifold" explicitly when there is danger of confusion.

The most common error is to assume the closed-subset version: a closed subset of a smooth manifold is *not* in general a smooth manifold. The closed interval $[0, 1] \subseteq \mathbb{R}$ is not a smooth 1-manifold (it has boundary), and the boundary $\partial \mathbb{B}^n = S^{n-1}$ inside $\mathbb{R}^n$ is a lower-dimensional submanifold, not an open submanifold. Inheritance of smooth structure works for *open* subsets, not closed ones.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Verify the three topological-manifold conditions for $U$ with the subspace topology, then verify the restricted atlas is smooth. Each step is short and uses subspace-topology inheritance plus the obvious restriction.

**Subgoal decomposition:**

1. **Verify Hausdorff for $U$.** Two distinct points in $U$ are distinct in $M$; separate by disjoint opens in $M$ (Hausdorff property), then intersect with $U$ to get disjoint opens in $U$.
   - *Hint:* Hausdorff is preserved by subspaces.
   - *Why needed:* First condition of topological manifold.

2. **Verify second countability for $U$.** A countable basis $\mathcal{B}$ for $M$ gives a countable basis $\mathcal{B}_U = \{B \cap U : B \in \mathcal{B}\}$ for the subspace topology on $U$.
   - *Hint:* Second countability is preserved by subspaces.
   - *Why needed:* Second condition.

3. **Verify locally Euclidean of dimension $n$ for $U$.** Given $p \in U$, take a chart $(V, \varphi) \in \mathcal{A}$ with $p \in V$; restrict to $(V \cap U, \varphi|_{V \cap U})$, a chart on $U$ of dimension $n$.
   - *Hint:* Restrictions of homeomorphisms to open subsets are homeomorphisms.
   - *Why needed:* Locally Euclidean condition.

4. **Verify smooth compatibility.** The transition between two restricted charts is the restriction of the transition between the original charts, hence smooth on the open restricted domain.
   - *Hint:* Smoothness is a local property; restriction to an open subset preserves smoothness.
   - *Why needed:* Smoothness of the atlas $\mathcal{A}_U$.

5. **Apply [[Thm - Smooth Structure from Maximal Atlas]] to conclude $\mathcal{A}_U$ determines a unique smooth structure on $U$, making $U$ a smooth $n$-manifold.**
   - *Hint:* Once we have a smooth atlas, the maximal-atlas theorem produces the smooth structure.
   - *Why needed:* This is the conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Hausdorff and second countability are preserved by subspaces
> **Statement:** Let $X$ be a topological space with a subspace $Y \subseteq X$. If $X$ is Hausdorff, then $Y$ (with subspace topology) is Hausdorff. If $X$ is second-countable, then $Y$ is second-countable.
>
> **Hint:** Subspace topology pulls back open sets and bases.
>
> **Why needed:** Establishes Hausdorff + second countability for the open submanifold.
>
> > [!note]- Full proof
> > *Hausdorff:* Given $p \neq q$ in $Y$, find disjoint $U_X, V_X$ open in $X$ with $p \in U_X, q \in V_X$. Then $U_X \cap Y, V_X \cap Y$ are open in $Y$, disjoint, and contain $p, q$.
> >
> > *Second countability:* Let $\mathcal{B}$ be a countable basis for $X$. Then $\mathcal{B}|_Y = \{B \cap Y : B \in \mathcal{B}\}$ is a countable collection. To check it's a basis: any open $V \subseteq Y$ equals $V_X \cap Y$ for some $V_X$ open in $X$, and $V_X = \bigcup_i B_i$ for some $B_i \in \mathcal{B}$, so $V = \bigcup_i (B_i \cap Y)$.

> [!note]- Lemma 2: Restriction of a chart to an open subset is a chart
> **Statement:** Let $(V, \varphi)$ be a chart on $M$ and let $W \subseteq V$ be open. Then $(W, \varphi|_W)$ is a chart on $M$ (and on any open subset $U \subseteq M$ containing $W$).
>
> **Hint:** Restrictions of homeomorphisms to open subsets are homeomorphisms onto open subsets.
>
> **Why needed:** Provides charts on the open submanifold by restricting ambient charts.
>
> > [!note]- Full proof
> > $W$ is open in $M$ (since $W$ is open in $V$ and $V$ is open in $M$). $\varphi|_W : W \to \varphi(W)$ is continuous (restriction of $\varphi$) and a bijection onto $\varphi(W)$; its inverse $\varphi^{-1}|_{\varphi(W)} : \varphi(W) \to W$ is continuous (restriction of $\varphi^{-1}$). The image $\varphi(W) = \varphi|_W (W)$ is open in $\mathbb{R}^n$ because $\varphi$ is a homeomorphism (which is an open map onto its image) and $W$ is open. So $(W, \varphi|_W)$ is a chart.

> [!note]- Lemma 3: Transition functions restrict smoothly
> **Statement:** Let $(V_\alpha, \varphi_\alpha), (V_\beta, \varphi_\beta)$ be smoothly compatible charts on $M$, and let $W_\alpha \subseteq V_\alpha, W_\beta \subseteq V_\beta$ be open. Then the restricted charts $(W_\alpha, \varphi_\alpha|_{W_\alpha}), (W_\beta, \varphi_\beta|_{W_\beta})$ are smoothly compatible.
>
> **Hint:** The transition function between restricted charts is the restriction of the original transition function to the smaller open set.
>
> **Why needed:** Establishes smoothness of the restricted atlas $\mathcal{A}_U$.
>
> > [!note]- Full proof
> > The transition $\varphi_\beta|_{W_\beta} \circ (\varphi_\alpha|_{W_\alpha})^{-1}$ is defined on $\varphi_\alpha(W_\alpha \cap W_\beta)$ and equals $\varphi_\beta \circ \varphi_\alpha^{-1}$ restricted to that open set. Since $\varphi_\beta \circ \varphi_\alpha^{-1}$ is smooth on $\varphi_\alpha(V_\alpha \cap V_\beta) \supseteq \varphi_\alpha(W_\alpha \cap W_\beta)$, its restriction is smooth. Similarly the inverse transition is smooth.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $M$ be a smooth $n$-manifold and $U \subseteq M$ open. Then $U$ inherits a smooth $n$-manifold structure from $M$.
>
> *Proof.*
>
> **Step 0 — Topological structure.** $U$ with the subspace topology is a topological space. By Lemma 1, $U$ inherits Hausdorff and second countability from $M$.
>
> **Step 1 — Locally Euclidean of dimension $n$.** Let $p \in U$. Choose a chart $(V, \varphi) \in \mathcal{A}$ with $p \in V$. Then $V \cap U$ is open in $M$ (intersection of opens), hence open in $U$ (definition of subspace topology). By Lemma 2, $(V \cap U, \varphi|_{V \cap U})$ is a chart of $M$ (and of $U$), with image $\varphi(V \cap U) \subseteq \varphi(V)$ an open subset of $\mathbb{R}^n$. So $p$ has a neighbourhood in $U$ homeomorphic to an open subset of $\mathbb{R}^n$, and $U$ is locally Euclidean of dimension $n$.
>
> **Step 2 — $U$ is a topological $n$-manifold.** Combining Steps 0 and 1, $U$ is Hausdorff, second-countable, and locally Euclidean of dimension $n$ — a topological $n$-manifold.
>
> **Step 3 — Construct the smooth atlas $\mathcal{A}_U$.** Define
> $$\mathcal{A}_U = \{(V, \varphi|_V) : (V, \varphi) \in \mathcal{A}, V \subseteq U\}.$$
> By Step 1, every point of $U$ is in the domain of some chart of $\mathcal{A}_U$, so the charts of $\mathcal{A}_U$ cover $U$. Equivalently (and more symmetrically), one can take
> $$\mathcal{A}_U' = \{(V \cap U, \varphi|_{V \cap U}) : (V, \varphi) \in \mathcal{A}\},$$
> which is also a covering family of charts; these two atlases determine the same smooth structure (compatibility check is identical).
>
> **Step 4 — Smooth compatibility of $\mathcal{A}_U$.** Let $(V_\alpha, \varphi_\alpha|_{V_\alpha}), (V_\beta, \varphi_\beta|_{V_\beta}) \in \mathcal{A}_U$ (with $V_\alpha, V_\beta \subseteq U$, both open in $M$). By Lemma 3 (with $W_\alpha = V_\alpha, W_\beta = V_\beta$, both already open in $M$), the restricted charts are smoothly compatible since $(V_\alpha, \varphi_\alpha)$ and $(V_\beta, \varphi_\beta)$ are smoothly compatible in $\mathcal{A}$.
>
> **Step 5 — Smooth structure determination.** $\mathcal{A}_U$ is a smooth atlas on $U$. By [[Thm - Smooth Structure from Maximal Atlas]], it is contained in a unique maximal smooth atlas, which is the smooth structure on $U$. Thus $U$ is a smooth $n$-manifold. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Topology — every open subset of a manifold is locally connected.** A topological manifold is locally connected (every point has a basis of connected neighbourhoods — the coordinate balls); this property is preserved by open subsets. Hence open submanifolds are locally connected, which simplifies many connectivity arguments.

**Algebraic topology — homotopy invariance.** An open submanifold $U \subseteq M$ has its own homotopy type, generally different from $M$. Computing $\pi_k(U)$ and $H_k(U)$ versus $\pi_k(M)$ and $H_k(M)$ is a standard exercise in algebraic topology. The inclusion $U \hookrightarrow M$ induces maps on these invariants, and the *long exact sequence* relating $U$, $M$, and $M \setminus U$ (excision, Mayer–Vietoris) computes them.

**Matrix Lie groups — concrete open submanifolds.** $\mathrm{GL}(n, \mathbb{R}), \mathrm{GL}(n, \mathbb{C})$, the *upper-triangular invertible matrices*, the *positive-determinant block-diagonal matrices*, the *unitary matrices in a specific maximal torus* — all are open submanifolds of larger linear groups. Computing the dimension of each and the relationship to the regular value theorem ([[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]]) is a basic Lie-theory exercise.

**Algebraic geometry — open subvarieties.** An algebraic variety $X$ has open subvarieties (complements of closed subvarieties), and these inherit the variety structure. The same construction — restrict the structure sheaf to the open set — works for schemes. The open-submanifold theorem in differential geometry is the differential-geometric counterpart of this purely algebraic construction.

---

# Bridges

- **[[Def - Subspace Topology]]** — the open submanifold inherits the subspace topology, the canonical topology on a subset of a topological space. The smooth structure refines this to a smooth manifold structure.

- **[[Ex - The General Linear Group is a Smooth Manifold]]** — the standard application: $\mathrm{GL}(n, \mathbb{R}) \subseteq M(n, \mathbb{R}) \cong \mathbb{R}^{n^2}$ is open (the determinant is continuous and nonzero exactly on $\mathrm{GL}$), so $\mathrm{GL}$ is a smooth $n^2$-manifold by this theorem. This is the source of essentially all matrix Lie groups as smooth manifolds.

- **Embedded submanifold vs. open submanifold** ([[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]]) — two different senses of "submanifold". Open submanifolds preserve dimension; embedded submanifolds typically decrease dimension. The terminology can collide; we always disambiguate.

- **Interior of a manifold with boundary** ([[Def - Smooth Manifold with Boundary]]) — $\operatorname{Int} M = M \setminus \partial M$ is an open subset of a manifold-with-boundary, hence a smooth manifold without boundary by this theorem.

- **Whitney extension and partition of unity** ([[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]]) — a smooth function on an open subset $U \subseteq M$ does *not* automatically extend to a smooth function on $M$; the obstruction is precisely the boundary behaviour as $U$ approaches the closure. Partitions of unity provide the technical tool to overcome this, glueing local smooth functions into global ones.

---

# Unlocked by This

> [!tip] $\mathrm{GL}(n, \mathbb{R})$ and Matrix Lie Groups *(from [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]])*
> The general linear group $\mathrm{GL}(n, \mathbb{R})$ — the prototype matrix Lie group — gets its smooth manifold structure as an open subset of $M(n, \mathbb{R}) \cong \mathbb{R}^{n^2}$. From this single example, the entire theory of matrix Lie groups (orthogonal, unitary, symplectic, special linear) follows by applying the regular value theorem to identify them as submanifolds.

> [!tip] Local Versus Global Properties on Manifolds *(throughout the rest of differential geometry)*
> The open-submanifold theorem encodes a profound principle: many properties of a smooth manifold are *local* — depending only on small open neighbourhoods of each point. Smoothness, dimension, tangent space, vector fields, differential forms are all local. *Global* properties — orientability, topology, integrability of distributions, existence of nowhere-zero vector fields — are obstructions to local-to-global extension, and are precisely the deep content of differential geometry.

> [!tip] Sheaves of Smooth Functions on Open Sets *(from Algebraic Geometry and Differential Geometry)*
> The assignment $U \mapsto C^\infty(U)$ for open $U \subseteq M$ defines the *structure sheaf* $C^\infty_M$ — a contravariant functor from the category of open subsets of $M$ to $\mathbb{R}$-algebras, with restriction maps as morphisms. The open-submanifold theorem is the differential-geometric content of "the structure sheaf restricts to any open subset" — a purely sheaf-theoretic principle.

> [!tip] Open Cover of a Manifold *(for Partitions of Unity in [[Differential Geometry II — Smooth Maps and Partitions of Unity|DG II]])*
> Every smooth manifold has an open cover by smooth coordinate balls (in fact, by precompact regular coordinate balls — Lee Proposition 1.19). Each member of the cover is itself an open submanifold (by this theorem), and the open-submanifold structure is exactly what makes partition-of-unity arguments work: we glue smooth functions defined on open submanifolds together to produce a global smooth function on $M$.
