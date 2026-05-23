---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Atlas and Smooth Structure"
  - "Def - Coordinate Chart and Atlas"
  - "Def - Product Topology"
tags: [geometry, differential-geometry]
---

# Notation

Throughout, $M_1, \dots, M_k$ are smooth manifolds of dimensions $n_1, \dots, n_k$, with given smooth structures $\mathcal{A}_1, \dots, \mathcal{A}_k$. The Cartesian product $M_1 \times \cdots \times M_k$ is equipped with the [[Def - Product Topology|product topology]]. For full notation see [[Differential Geometry I — Smooth Manifolds and Atlases]].

---

# Statement

> **Theorem (Product of [[Def - Smooth Manifold|Smooth Manifolds]]; Lee Example 1.34).** Let $M_1, \dots, M_k$ be smooth manifolds of [[Def - Dimension|dimensions]] $n_1, \dots, n_k$. The product space $M_1 \times \cdots \times M_k$ with the product topology is a topological manifold of [[Def - Dimension|dimension]] $n_1 + \cdots + n_k$. Moreover, the **product atlas**
> $$\mathcal{A}_{\mathrm{prod}} = \{(U_{\alpha_1} \times \cdots \times U_{\alpha_k}, \, \varphi_{\alpha_1} \times \cdots \times \varphi_{\alpha_k}) : (U_{\alpha_i}, \varphi_{\alpha_i}) \in \mathcal{A}_i\}$$
> is a smooth atlas on $M_1 \times \cdots \times M_k$, determining the **product smooth structure**.

> **Corollary.** If $M_1, \dots, M_k, N$ are smooth manifolds and $N$ is a smooth manifold with boundary, then $M_1 \times \cdots \times M_k \times N$ is a smooth manifold with boundary, with $\partial(M_1 \times \cdots \times M_k \times N) = M_1 \times \cdots \times M_k \times \partial N$. (Lee Proposition 1.45.) Products of two or more manifolds with boundary are *not* in general smooth manifolds with boundary — they are smooth manifolds with corners (Lee Chapter 16).

---

# Motivation

A natural way to build new manifolds from old ones is via the Cartesian product: given $M_1$ and $M_2$, form $M_1 \times M_2$ as a set, equip it with the product topology, and ask whether this is again a manifold. The answer is yes, and the smooth structure is built from the smooth structures on the factors in the most direct way possible — the product of charts on the factors becomes a chart on the product. This theorem gives the construction and verifies it works.

The product manifold is the source of many of the most important examples: the $n$-torus $T^n = (S^1)^n$, the configuration space of a multi-particle system $\mathbb{R}^{3N}$, the phase space $M \times \mathbb{R}^n$ in mechanics, the cylinder $S^1 \times \mathbb{R}$ in physics, the double pendulum's configuration space $T^2 = S^1 \times S^1$. Each of these is "build up" the manifold dimension by combining lower-dimensional building blocks. The theorem says this construction works *uniformly* — the product topology, the product smooth structure, and the chain rule all conspire to make it well-defined.

The construction also has structural significance: it shows that the category $\mathbf{Man}^\infty$ of smooth manifolds has finite products, with the product manifold and product smooth structure as the categorical product. The projections $\pi_i : M_1 \times M_2 \to M_i$ are smooth maps, and any pair of smooth maps $f : N \to M_1$, $g : N \to M_2$ assembles into a unique smooth map $(f, g) : N \to M_1 \times M_2$ — this is the universal property of the product in $\mathbf{Man}^\infty$.

The corollary about manifolds with boundary is technically delicate: products of two boundary-bearing manifolds produce *corners*, not boundary, so the category $\mathbf{Man}^\infty_\partial$ of manifolds with boundary is *not* closed under products. To get a closed category, one must enlarge to manifolds with corners (Lee Chapter 16). The corollary is the maximally general statement that stays inside $\mathbf{Man}^\infty_\partial$.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "smooth manifolds $M_1, \dots, M_k$". The skill is recognizing when a space is naturally a product.

The first source is **a space described by independent coordinates**. The $n$-torus $T^n$ has $n$ "independent angle coordinates" $\theta_1, \dots, \theta_n \in S^1$ — it is *manifestly* a product. The configuration space of $n$ particles in $\mathbb{R}^3$, ignoring interactions, is $(\mathbb{R}^3)^n$ — a product. The product structure is read directly off the parametrization.

The second source is **a space that decomposes as a fibre bundle with trivial monodromy**. A fibre bundle $\pi : E \to B$ with fibre $F$ is locally a product (over any local trivialization of $B$); if the bundle is globally trivializable — meaning $E \cong B \times F$ — then $E$ is a product manifold. The non-trivial twist is that fibre bundles are usually *not* trivializable globally (the Möbius band is a $\mathbb{R}$-bundle over $S^1$ that is not trivial). When triviality holds, the product structure simplifies analysis enormously.

The third source is **a Lie group expressed as a semidirect product**. Many Lie groups have the form $G = H \rtimes K$, and topologically $G \cong H \times K$ — though the group structure twists this in a nontrivial way. The smooth manifold structure of $G$ inherits the product structure of $H \times K$, and this is the source of explicit charts on Lie groups.

The fourth source is **a tangent bundle with a trivialization**. The tangent bundle $TM$ of a smooth manifold $M$ is in general not a product (its non-triviality is measured by the Euler class and other characteristic classes), but for **parallelizable** manifolds — those admitting a global trivialization $TM \cong M \times \mathbb{R}^n$ — the tangent bundle is genuinely a product manifold. Examples: $\mathbb{R}^n$, every Lie group, $S^1$, $S^3$, $S^7$.

**Targets (Output Amplification)**

The first target: **the product topology + smooth structure makes calculus on the product well-defined**, with the projections being smooth and the universal property of the product holding. Smooth maps $f : N \to M_1 \times M_2$ correspond bijectively to pairs of smooth maps $(f_1, f_2)$ with $f_i = \pi_i \circ f : N \to M_i$. This is the categorical content.

The second target: **dimension of the product = sum of dimensions of the factors**. So a product manifold is "bigger" in dimension than its factors, in the additive sense. This propagates to formulas: the Euler characteristic of $T^n = (S^1)^n$ is $0^n$ (since $\chi(S^1) = 0$); the volume of a Riemannian product is the product of volumes; the de Rham cohomology of a product is the *Künneth tensor product* $H^*_{dR}(M \times N) \cong H^*_{dR}(M) \otimes H^*_{dR}(N)$ (a deep result in [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]]).

The third target: **the tangent space of a product is the product of tangent spaces**. $T_{(p, q)}(M \times N) \cong T_p M \times T_q N$ canonically. This is the basis of doing calculus on product manifolds: a tangent vector to $M \times N$ is a pair of tangent vectors. See [[Differential Geometry III — Tangent Vectors and the Differential|DG III]].

The fourth target: **the smooth functions on a product form a tensor product algebra**. $C^\infty(M \times N) \neq C^\infty(M) \otimes_\mathbb{R} C^\infty(N)$ in general (the tensor product is too small), but they coincide for compact $M$ and $N$ in the appropriate completion. The structure is the differentiable analogue of the algebraic Künneth formula.

---

# Why Is It True

The intuition is that the smooth structure on a product is the *cleanest possible* one: a chart on the product is just a product of charts on the factors, and a transition function on the product is a product of transition functions on the factors. Smoothness of the product of smooth functions follows from the chain rule, applied componentwise.

More precisely: the smoothness of a product map $\varphi_\beta \times \psi_\beta : U_\beta \times V_\beta \to \widehat{U}_\beta \times \widehat{V}_\beta$ between products of open subsets of Euclidean spaces is equivalent to smoothness of each factor separately. So the product chart $\varphi_\alpha \times \psi_\beta$ is automatically a homeomorphism, and the transition between two product charts factors as

$$(\varphi_{\alpha'} \times \psi_{\beta'}) \circ (\varphi_\alpha \times \psi_\beta)^{-1} = (\varphi_{\alpha'} \circ \varphi_\alpha^{-1}) \times (\psi_{\beta'} \circ \psi_\beta^{-1}),$$

a product of two smooth maps (the transition functions on each factor), hence smooth.

**The one-liner mechanism: smoothness of a product map factors into smoothness of each component, so the product atlas is smooth iff each factor atlas is.**

The Hausdorff and second-countability properties are inherited by finite products: Hausdorff is preserved under finite products (two points $(p, q), (p', q')$ are different iff $p \neq p'$ or $q \neq q'$; separate in the appropriate factor, take a product open neighbourhood), and second countability is preserved by finite products (the product of countable bases is a countable basis for the product topology). These are standard topological facts.

The locally Euclidean property follows from the product of charts: a chart on $M_i$ has image in $\mathbb{R}^{n_i}$, so the product of charts has image in $\mathbb{R}^{n_1 + \cdots + n_k}$, an open subset (the product of open subsets is open in the product topology, which coincides with the standard topology on $\mathbb{R}^{n_1+\cdots+n_k}$).

---

# What Makes This Hard

The theorem is not technically hard once the framework is in place — the proof is largely bookkeeping with the chain rule. The non-obvious aspect is the *failure* of the corresponding statement for manifolds with boundary: the product of two manifolds with boundary has *corners*, not boundary. This is the source of the subtle Lee Proposition 1.45, which states the most general version that stays inside the smooth-manifold-with-boundary category — at most one factor may have boundary.

Concretely: $[0, 1]^2$ has four corner points where two boundary edges meet at a right angle. Near a corner, the local model is the closed quadrant $\{x, y \geq 0\}$, not the half-plane $\{y \geq 0\}$. The corner is a *codimension-2* boundary phenomenon, and to handle it one needs the language of manifolds with corners (Lee Chapter 16). For elementary applications — the cylinder $S^1 \times [0, 1]$, the cone $\mathbb{R}^n \times [0, 1]$ — the corollary suffices.

The other common error is to assume that the product topology and the standard topology on $\mathbb{R}^{n_1+n_2}$ coincide for chart targets — they do, of course, but the verification (the product of open balls is open in the product topology, which has the same open sets as the standard topology) is sometimes glossed over.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Verify the three topological-manifold conditions for $M_1 \times \cdots \times M_k$, then verify the product atlas is smooth by computing the transition function as a product of transition functions on each factor.

**Subgoal decomposition:**

1. **Verify Hausdorff for $M_1 \times \cdots \times M_k$.** Two distinct points $(p_1, \dots, p_k), (q_1, \dots, q_k)$ differ in at least one coordinate; separate in that coordinate using Hausdorff on $M_i$ and take a product open set.
   - *Hint:* Hausdorff is preserved by finite products in general topology.
   - *Why needed:* One of the three conditions of topological manifold.

2. **Verify second countability.** Take a countable basis $\mathcal{B}_i$ for each $M_i$; the product $\{B_1 \times \cdots \times B_k : B_i \in \mathcal{B}_i\}$ is a countable basis for the product topology.
   - *Hint:* Finite product of countable sets is countable.
   - *Why needed:* The second topological-manifold condition.

3. **Verify locally Euclidean of dimension $n_1 + \cdots + n_k$.** Given $(p_1, \dots, p_k)$, take charts $(U_i, \varphi_i)$ on $M_i$ with $p_i \in U_i$; then $U_1 \times \cdots \times U_k$ is an open neighbourhood, and $\varphi_1 \times \cdots \times \varphi_k$ is a homeomorphism onto $\widehat{U}_1 \times \cdots \times \widehat{U}_k \subseteq \mathbb{R}^{n_1 + \cdots + n_k}$.
   - *Hint:* The product of [[Def - Homeomorphism|homeomorphisms]] is a homeomorphism between products.
   - *Why needed:* The locally Euclidean condition, with dimension $n_1 + \cdots + n_k$.

4. **Verify the product atlas is smooth.** Take two product charts $\varphi_\alpha = \varphi_{\alpha_1} \times \cdots \times \varphi_{\alpha_k}$ and $\varphi_\beta = \varphi_{\beta_1} \times \cdots \times \varphi_{\beta_k}$; compute the transition as $\varphi_\beta \circ \varphi_\alpha^{-1} = (\varphi_{\beta_1} \circ \varphi_{\alpha_1}^{-1}) \times \cdots \times (\varphi_{\beta_k} \circ \varphi_{\alpha_k}^{-1})$, a product of smooth maps.
   - *Hint:* A product of smooth maps between products of open subsets of Euclidean spaces is smooth iff each factor is.
   - *Why needed:* Smoothness of the product atlas is the smooth-manifold conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Hausdorff is preserved by finite products
> **Statement:** A finite product of Hausdorff topological spaces, with the product topology, is Hausdorff.
>
> **Hint:** Given two distinct points, find a coordinate where they differ and separate in that coordinate.
>
> **Why needed:** Establishes the Hausdorff condition for the product manifold.
>
> > [!note]- Full proof
> > Let $X_1, X_2$ be Hausdorff. For two distinct points $(p_1, p_2), (q_1, q_2) \in X_1 \times X_2$, either $p_1 \neq q_1$ or $p_2 \neq q_2$. WLOG $p_1 \neq q_1$. Find disjoint opens $U \ni p_1, V \ni q_1$ in $X_1$. Then $U \times X_2$ and $V \times X_2$ are disjoint opens in $X_1 \times X_2$ separating the two points. Induct on the number of factors.

> [!note]- Lemma 2: Second countability is preserved by finite products
> **Statement:** A finite product of second-countable topological spaces, with the product topology, is second-countable.
>
> **Hint:** The product of countable bases gives a countable basis for the product topology.
>
> **Why needed:** Establishes the second-countability condition for the product manifold.
>
> > [!note]- Full proof
> > Let $X_i$ have countable basis $\mathcal{B}_i$ for $i = 1, \dots, k$. Then $\mathcal{B} = \{B_1 \times \cdots \times B_k : B_i \in \mathcal{B}_i\}$ is a basis for the product topology on $X_1 \times \cdots \times X_k$ (definition of product topology), and $|\mathcal{B}| \leq |\mathcal{B}_1| \cdot \ldots \cdot |\mathcal{B}_k| \leq \aleph_0^k = \aleph_0$, so $\mathcal{B}$ is countable.

> [!note]- Lemma 3: Smoothness of a product map
> **Statement:** Let $f_1 : U_1 \to V_1, \ldots, f_k : U_k \to V_k$ be maps between open subsets of Euclidean spaces. Then $f_1 \times \cdots \times f_k : U_1 \times \cdots \times U_k \to V_1 \times \cdots \times V_k$ is smooth iff each $f_i$ is smooth.
>
> **Hint:** Partial derivatives of the product map are sums of partial derivatives of each factor; the conclusion follows from the definition of smoothness componentwise.
>
> **Why needed:** Reduces smoothness of the product transition function to smoothness of each factor's transition function.
>
> > [!note]- Full proof
> > Write $(x_1, \dots, x_k)$ for the variable on $U_1 \times \cdots \times U_k$ with $x_i \in U_i \subseteq \mathbb{R}^{n_i}$. The product map is $F(x_1, \dots, x_k) = (f_1(x_1), \dots, f_k(x_k))$. A partial derivative of $F$ in the $x_i^j$ direction (the $j$-th coordinate of the $i$-th factor) is
> > $$\frac{\partial F}{\partial x_i^j}(x_1, \dots, x_k) = \left(0, \dots, 0, \frac{\partial f_i}{\partial x_i^j}(x_i), 0, \dots, 0\right) \in V_1 \times \cdots \times V_k,$$
> > with the nonzero entry only in the $i$-th slot. Iterating, every higher-order partial derivative of $F$ corresponds to a derivative of exactly one of the $f_i$'s (mixed partials across factors are zero). So $F$ has all partials continuous iff each $f_i$ does — i.e., $F$ is smooth iff each $f_i$ is.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** The product space $M_1 \times \cdots \times M_k$ with the product topology is a topological manifold of dimension $n_1 + \cdots + n_k$, and the product atlas is a smooth atlas.
>
> *Proof.*
>
> **Step 0 — Topological manifold structure.** By Lemmas 1 and 2, $M_1 \times \cdots \times M_k$ is Hausdorff and second-countable. For locally Euclidean: given any point $(p_1, \dots, p_k) \in M_1 \times \cdots \times M_k$, choose for each $i$ a chart $(U_i, \varphi_i)$ on $M_i$ with $p_i \in U_i$. The product $U_1 \times \cdots \times U_k$ is open in the product topology (definition), and the product map $\varphi_1 \times \cdots \times \varphi_k : U_1 \times \cdots \times U_k \to \widehat{U}_1 \times \cdots \times \widehat{U}_k$ is a homeomorphism (product of [[Def - Homeomorphism|homeomorphisms]] is a homeomorphism between products). The image $\widehat{U}_1 \times \cdots \times \widehat{U}_k$ is an open subset of $\mathbb{R}^{n_1} \times \cdots \times \mathbb{R}^{n_k} = \mathbb{R}^{n_1 + \cdots + n_k}$. So the product chart is a chart of dimension $n_1 + \cdots + n_k$, and the product atlas covers $M_1 \times \cdots \times M_k$.
>
> **Step 1 — Smooth compatibility of product charts.** Let $\varphi_\alpha = \varphi_{\alpha_1} \times \cdots \times \varphi_{\alpha_k}$ and $\varphi_\beta = \varphi_{\beta_1} \times \cdots \times \varphi_{\beta_k}$ be two product charts with overlapping domains. On the overlap, the transition function is
> $$\varphi_\beta \circ \varphi_\alpha^{-1} = (\varphi_{\beta_1} \circ \varphi_{\alpha_1}^{-1}) \times \cdots \times (\varphi_{\beta_k} \circ \varphi_{\alpha_k}^{-1}),$$
> a product of transition functions on each factor. Each factor $\varphi_{\beta_i} \circ \varphi_{\alpha_i}^{-1}$ is smooth (since $(\mathcal{A}_i)$ is a smooth atlas on $M_i$). By Lemma 3, the product is smooth. By symmetry, the inverse is also smooth. So $\varphi_\alpha$ and $\varphi_\beta$ are smoothly compatible.
>
> **Step 2 — Smooth structure determination.** The product atlas $\mathcal{A}_{\mathrm{prod}}$ is a smooth atlas. By [[Thm - Smooth Structure from Maximal Atlas]], it is contained in a unique maximal smooth atlas, which is the **product smooth structure** on $M_1 \times \cdots \times M_k$. $\blacksquare$
>
> *Note on dimension.* By [[Thm - Invariance of Dimension]], the dimension is well-defined and equals $n_1 + \cdots + n_k$.

---

# Cross-Field Exercise Suggestions

**Algebraic topology — Künneth formula.** The de Rham cohomology of a product satisfies $H^*_{dR}(M \times N) \cong H^*_{dR}(M) \otimes H^*_{dR}(N)$ (Künneth theorem; see [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]]). This is a direct consequence of the product smooth structure and is the geometric reason that cohomological invariants of products multiply.

**Lie group theory — direct product of Lie [[Def - Group|groups]].** The product of two Lie [[Def - Group|groups]] is a Lie group (the group operations multiply componentwise), and topologically it is the product manifold. The Lie algebra of the product is the direct sum of the Lie algebras. This is the "free" construction in the category of Lie groups, and most concrete Lie groups are built from direct/semidirect products of simpler ones.

**Probability and measure theory — product measures.** The product topology on $M \times N$ supports a natural Borel structure $\mathcal{B}(M \times N) \cong \mathcal{B}(M) \otimes \mathcal{B}(N)$, and the product of two probability measures is a probability measure on the product. Probability spaces with smooth structure (e.g., random points on a manifold) inherit the product smooth structure.

**Differential equations — phase portraits and product systems.** A coupled ODE system on $M \times N$ corresponds to a vector field on the product, decomposable into the partial vector fields on each factor. When the system *uncouples* — the vector field is a direct sum — the trajectories are products of trajectories on each factor. This is the "diagonal" structure of decoupled systems and is the foundation of separation-of-variables techniques.

---

# Bridges

- **[[Def - Product Topology]]** — the topology on the product manifold is the product topology, the categorical product in $\mathbf{Top}$. The smooth structure refines this to a smooth manifold structure.

- **Tangent space of a product** ([[Differential Geometry III — Tangent Vectors and the Differential|DG III]]) — $T_{(p, q)}(M \times N) \cong T_p M \times T_q N$ canonically, with the isomorphism given by the differentials of the projections. This is the *infinitesimal* product structure, and the smooth structure on the tangent bundle of a product is itself a product of tangent bundles.

- **Künneth theorem for de Rham cohomology** ([[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]]) — the de Rham cohomology of $M \times N$ tensor-decomposes: $H^k(M \times N) \cong \bigoplus_{p+q = k} H^p(M) \otimes H^q(N)$. This is a deep consequence of the product structure and Stokes's theorem.

- **Whitney embedding theorem** (preview of [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]]) — every smooth $n$-manifold embeds into $\mathbb{R}^{2n}$, so in particular every product manifold embeds into a Euclidean space of dimension $\leq 2(n_1 + \cdots + n_k)$. The product structure is preserved by the embedding when the factors embed separately.

- **Lee Proposition 1.45 (products with boundary)** — the category $\mathbf{Man}^\infty_\partial$ of manifolds with boundary is not closed under products; one factor with boundary suffices, multiple factors with boundary produce corners. The corollary states the maximally general case. To allow more factors with boundary, one passes to manifolds with corners (Lee Chapter 16).

---

# Unlocked by This

> [!tip] Tori, Configuration Spaces, and Phase Spaces *(throughout the rest of differential geometry and physics)*
> The product manifold construction gives the $n$-torus $T^n$, the configuration space of $n$ particles in $\mathbb{R}^3$, the phase space $T^*M = M \times \mathbb{R}^n$ in a single chart (with the cotangent bundle structure), and countless other examples. These are the "building blocks" of geometric mechanics and field theory.

> [!tip] Categorical Product in $\mathbf{Man}^\infty$ *(from Category Theory of Manifolds)*
> The product smooth structure makes $\mathbf{Man}^\infty$ into a category with finite products. The universal property: a smooth map $f : N \to M_1 \times M_2$ is the same as a pair of smooth maps $(f_1, f_2)$ with $f_i = \pi_i \circ f$. This makes diagrammatic reasoning about manifolds (and constructions like fibre products, pullbacks) possible.

> [!tip] Fibre Bundles as Locally Trivial Products *(from [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle|DG VI]])*
> A **fibre bundle** $\pi : E \to B$ with fibre $F$ is "locally a product": every point of $B$ has a neighbourhood $U$ over which $\pi^{-1}(U) \cong U \times F$ as smooth manifolds. The global structure is the "twist" by which the local products are glued together (the transition functions). Vector bundles, principal bundles, and the tangent bundle are all instances of this picture.

> [!tip] Manifolds with Corners *(from Lee Chapter 16)*
> Products of multiple manifolds-with-boundary produce *corners*. The product $[0,1] \times [0,1]$ has four corner points, locally modelled on $\{(x,y) : x, y \geq 0\}$. The generalization to *manifolds with corners* enlarges the model class beyond $\mathbb{R}^n$ and $\mathbb{H}^n$ to include products like $\mathbb{R}^k \times \mathbb{H}^j_1 \times \cdots$, and is the right category for products of boundary-bearing manifolds.
