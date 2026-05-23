---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Lie Group"
  - "Def - Lie Subgroup"
  - "Def - Homogeneous Space"
  - "Def - Smooth Manifold"
tags: [geometry, differential-geometry, lie-groups]
---

# Notation

$G$ is a Lie group; $H \leq G$ is a closed Lie subgroup (automatically closed by the closed subgroup theorem if assumed closed). $G/H$ denotes the set of left cosets $\{gH : g \in G\}$ with the quotient topology from $G$. The natural projection is $\pi : G \to G/H$, $\pi(g) = gH$. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

---

# Statement

> **Theorem ([[Def - Homogeneous Space|Homogeneous Space]] Manifold Structure; Lee Thm 21.17).** Let $G$ be a Lie [[Def - Group|group]] and $H \leq G$ a closed Lie subgroup. Then the [[Def - Coset|coset]] space $G/H$ (with the quotient topology) carries a unique smooth manifold structure of [[Def - Dimension|dimension]] $\dim G - \dim H$ such that:
>
> (a) the projection $\pi : G \to G/H$ is a smooth submersion, and
>
> (b) the natural left action of $G$ on $G/H$, $g \cdot (g'H) = (gg')H$, is a smooth action.
>
> Moreover, $\pi : G \to G/H$ is a **principal $H$-bundle**: the right action of $H$ on $G$ by right translation is smooth, free, and proper, and the orbit space is $G/H$.

> **Corollary.** Combined with [[Thm - Orbit-Stabilizer for Lie Group Actions|orbit-stabilizer]], every smooth transitive $G$-action on a smooth manifold $M$ realizes $M$ as a homogeneous space $G/G_p$ for any choice of basepoint $p$.

---

# Motivation

This theorem is the structural foundation of homogeneous-space theory: it says that for any Lie group $G$ and closed Lie subgroup $H$, the [[Def - Coset|coset]] space $G/H$ is automatically a smooth manifold, and the projection is automatically a submersion (in fact a principal $H$-bundle). Without this theorem, one would have to construct charts on $G/H$ by hand for each example — a tedious and error-prone process. With it, the construction is uniform, and the manifold structure on $G/H$ is determined by the smooth structure of $G$ and the closedness of $H$ alone.

The two key inputs are:

1. **The closed subgroup theorem** — provides the embedded Lie subgroup structure on $H$ from the closed-subgroup hypothesis.
2. **The quotient manifold theorem** (Lee Thm 21.10) — provides smooth manifold structure on the quotient of a smooth manifold by a free proper action of a Lie group.

The quotient manifold theorem applied to the right action of $H$ on $G$ (which is smooth by smoothness of multiplication, free by group axioms, and proper because $H$ is closed) gives the smooth structure on $G/H$. The submersion property and the principal-bundle structure follow from the quotient manifold theorem's general framework.

The structural payoff is **the principal bundle $H \hookrightarrow G \to G/H$**. This is a smooth fibre bundle with fibre $H$ and structure group $H$ acting by right multiplication. Principal bundles are the geometric foundation of gauge theory, and the simplest examples — $\mathrm{SO}(n) \hookrightarrow \mathrm{SO}(n+1) \to S^n$, $\mathrm{O}(k) \times \mathrm{O}(n-k) \hookrightarrow \mathrm{O}(n) \to \mathrm{Gr}_k(\mathbb{R}^n)$ — all come from this construction.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is a Lie group with a closed Lie subgroup.

The first source is **a Lie group $G$ with a defining smooth action on a manifold**. Property $B$ is "$G$ acts smoothly on $M$". The bridge is: pick a basepoint $p$, take the stabilizer $H = G_p$ (closed by continuity), invoke orbit-stabilizer to get $M = G \cdot p \cong G/H$. Then the homogeneous space theorem gives the manifold structure on $G/H$ directly, recovering the smooth structure on $M$ (or rather, on its orbits).

A second source is **a Lie group $G$ with a defining quotient construction**. Property $B$ is "we want to form $G/H$ for a closed $H \leq G$". The bridge: the theorem gives the smooth manifold structure on $G/H$ directly, without any need to construct charts by hand.

A third source is **an algebraic group quotient**. For algebraic groups (over $\mathbb{R}$ or $\mathbb{C}$), the analogue of this theorem is the **quotient by a closed algebraic subgroup**, giving the underlying variety of $G/H$ as an algebraic variety. Over $\mathbb{R}$, the underlying smooth manifold of the algebraic quotient is the Lie-theoretic $G/H$ from this theorem.

**Targets (Output Amplification)**

The conclusion is the smooth manifold structure on $G/H$ plus the principal bundle structure.

The first amplification is **invariant geometric objects on $G/H$ via $H$-equivariance at the basepoint**. A $G$-invariant Riemannian metric on $G/H$ is in bijection with an $H$-invariant inner product on the tangent space at $eH$, which is $\mathfrak{g}/\mathfrak{h}$. The isotropy representation $H \to \mathrm{GL}(\mathfrak{g}/\mathfrak{h})$ is what determines whether such an inner product exists (e.g., is $H$ compact? then yes, by averaging). This converts the geometry of $G/H$ to representation-theoretic questions about $H$.

A second amplification is **principal bundle and associated bundle constructions**. The principal $H$-bundle $G \to G/H$ has **associated bundles** for every linear representation $\rho : H \to \mathrm{GL}(V)$: the associated bundle is $G \times_\rho V = (G \times V)/H$ where $H$ acts diagonally. These are the universal examples of vector bundles on $G/H$, and the [[Def - Section of a Vector Bundle|sections]] are exactly the $H$-equivariant functions $G \to V$.

A third amplification is **dimension and topology of $G/H$**. The dimension is $\dim G - \dim H$ (read off the theorem). The fundamental group fits into a long exact sequence from the fibration $H \to G \to G/H$: $\cdots \to \pi_k(H) \to \pi_k(G) \to \pi_k(G/H) \to \pi_{k-1}(H) \to \cdots$. This is the principal tool for computing homotopy groups of homogeneous spaces.

---

# Why Is It True

The theorem is essentially a corollary of two prior theorems: the closed subgroup theorem (giving $H$ a Lie subgroup structure) and the quotient manifold theorem (Lee Thm 21.10 — giving smooth structure to quotients of manifolds by free proper Lie group actions).

**The bolded mechanism summary: the right action of $H$ on $G$ by right multiplication is smooth (multiplication is smooth), free (only $e \in H$ fixes any $g \in G$, by cancellation), and proper (because $H$ is closed; properness reduces to compactness of preimage maps, which uses closedness in a careful argument). The quotient manifold theorem applied to this action gives the smooth structure on $G/H$.**

The proof proceeds:

1. **Right action of $H$ on $G$ is smooth.** This is just smoothness of group multiplication restricted to $G \times H \subseteq G \times G$.

2. **Right action is free.** For $g \in G$ and $h \in H$ with $g h = g$, multiplying by $g^{-1}$ on the left gives $h = e$. So the stabilizer of any $g \in G$ under right $H$-action is $\{e\}$.

3. **Right action is proper.** The map $G \times H \to G \times G$, $(g, h) \mapsto (gh, g)$, must have compact preimages. This step uses closedness of $H$ (and is the main technical step in Lee's proof of the quotient manifold theorem).

4. **Quotient manifold theorem.** Apply Lee Thm 21.10 to the free proper smooth right action of $H$ on $G$. The quotient $G/H$ inherits a unique smooth manifold structure of dimension $\dim G - \dim H$ such that $\pi : G \to G/H$ is a smooth submersion.

5. **$G$-action on $G/H$ is smooth.** The left action of $G$ on $G/H$ is $g \cdot (g' H) = (gg') H$. This factors as $G \times G/H \xrightarrow{\mathrm{id} \times \pi^{-1}} G \times G \xrightarrow{m} G \xrightarrow{\pi} G/H$ — smooth by composition of smooth maps.

6. **Principal $H$-bundle.** By construction, $G$ is a free $H$-space and $G \to G/H$ is the orbit projection; combined with the smoothness of the right action and the quotient manifold structure, this is the definition of a principal $H$-bundle.

---

# What Makes This Hard

The proof rests on the **properness of the right $H$-action on $G$**, which is where closedness of $H$ enters in an essential way. Without closedness, properness fails — the irrational winding $\mathbb{R} \hookrightarrow T^2$ provides the classical counterexample: $\mathbb{R}$ acts on $T^2$ by translation along the line, but the action is *not* proper (orbits are dense), and the quotient $T^2/\mathbb{R}$ has the trivial topology.

The most common error is to underestimate this: thinking that "$G/H$ is a manifold for any Lie subgroup $H$". This is **false** — only for closed Lie [[Def - Subgroup|subgroups]]. The closed subgroup theorem and this homogeneous-space theorem together restrict attention to the right class of [[Def - Subgroup|subgroups]].

A second subtlety is the construction of the principal bundle structure. The fibres of $\pi : G \to G/H$ are exactly the right $H$-orbits, $\pi^{-1}(\bar g) = g H$ for any representative $g$ of $\bar g$. The right action of $H$ acts freely and transitively on each fibre, so each fibre is diffeomorphic to $H$.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Apply the quotient manifold theorem (Lee Thm 21.10) to the right action of $H$ on $G$. Verify the action is smooth (multiplication is smooth), free (group cancellation), and proper (uses closedness of $H$). The quotient $G/H$ inherits smooth structure, and the projection is a submersion. The left $G$-action on $G/H$ is smooth by composition.

**Subgoal decomposition:**

1. **Right $H$-action on $G$ is smooth.** $G \times H \to G$, $(g, h) \mapsto gh$, is smooth (restriction of group multiplication).
   - *Hint:* Smoothness of multiplication on $G$.

2. **Right action is free.** $gh = g \implies h = e$.
   - *Hint:* Left-cancel by $g^{-1}$.

3. **Right action is proper.** Use closedness of $H$.
   - *Hint:* For compact $K \subseteq G$, the set $\{(g, h) : g \in K, gh \in K\}$ has $h \in K^{-1} K$, which is closed (and bounded if $K$ is compact) ⟹ compact, using closedness of $H$.

4. **Quotient manifold theorem.** Apply Lee Thm 21.10 to get smooth structure on $G/H$ of dimension $\dim G - \dim H$ with smooth projection $\pi$.

5. **$G$-action on $G/H$ is smooth.** $g \cdot (g'H) = (gg')H$ factors through smooth maps.

6. **Principal bundle structure.** $G \to G/H$ is a principal $H$-bundle by construction.

---

# Lemma Decomposition

> [!note]- Lemma 1: Right $H$-action on $G$ is free
> **Statement:** For $g \in G$ and $h \in H$, $gh = g$ implies $h = e$.
>
> **Hint:** Left-multiply by $g^{-1}$.
>
> **Why needed:** Freeness is one of the three hypotheses of the quotient manifold theorem.
>
> > [!note]- Full proof
> > $gh = g \implies g^{-1} g h = g^{-1} g \implies h = e$. So the right action is free.

> [!note]- Lemma 2: Right $H$-action is proper when $H$ is closed
> **Statement:** The right action of $H$ on $G$ is proper: for any compact $K \subseteq G$, the set $H_K := \{h \in H : Kh \cap K \neq \emptyset\}$ is compact.
>
> **Hint:** $H_K = H \cap (K^{-1} \cdot K)$ where $K^{-1} \cdot K$ is the image of $K^{-1} \times K$ under multiplication. Compact subset of $G$ intersected with the closed set $H$ is compact.
>
> **Why needed:** Properness is the third hypothesis of the quotient manifold theorem.
>
> > [!note]- Full proof
> > $H_K = \{h \in H : \exists g_1, g_2 \in K \text{ with } g_1 h = g_2\} = \{h \in H : h \in K^{-1} K\} = H \cap (K^{-1} K)$. Now $K^{-1} K$ is the image of the continuous map $G \times G \to G$, $(g_1, g_2) \mapsto g_1^{-1} g_2$, applied to the compact set $K \times K$, hence is compact. $H$ is closed by hypothesis. So $H_K = H \cap (K^{-1}K)$ is the intersection of a closed set and a compact set, hence compact.

> [!note]- Lemma 3: The left $G$-action on $G/H$ is smooth
> **Statement:** The map $G \times G/H \to G/H$, $(g, g'H) \mapsto (gg')H$, is smooth.
>
> **Hint:** Composition of smooth maps; use that $\pi$ is a submersion to lift smoothness questions to $G$.
>
> **Why needed:** It is the second conclusion of the theorem (after the manifold structure on $G/H$).
>
> > [!note]- Full proof
> > Consider the map $f : G \times G \to G/H$, $(g, g') \mapsto (gg') H = \pi(gg')$, a composition of the smooth multiplication on $G$ and the smooth projection $\pi$. This descends through the right $H$-action on the second factor (which acts as $(g, g') \mapsto (g, g'h)$, sending $(gg')H$ to $(gg'h)H = (gg')H$ since $h H = H$) to give a smooth map $G \times (G/H) \to G/H$, which is the desired action. (Smoothness on the quotient is via the universal property of the quotient manifold structure on $G/H$.)

---

# Formal Proof

> [!note]- Complete formal proof
> Let $G$ be a Lie group, $H \leq G$ a closed Lie subgroup.
>
> **Step 0 (Smoothness of the right $H$-action on $G$).** The map $G \times H \to G$, $(g, h) \mapsto gh$, is the restriction of the smooth multiplication $G \times G \to G$.
>
> **Step 1 (Free action).** By Lemma 1, the right $H$-action on $G$ is free.
>
> **Step 2 (Proper action).** By Lemma 2, the right $H$-action on $G$ is proper.
>
> **Step 3 (Quotient manifold theorem).** Apply Lee Theorem 21.10 (quotient manifold theorem) to the free proper smooth right action of $H$ on $G$. The orbit space $G/H$ inherits a unique smooth manifold structure of dimension $\dim G - \dim H$ such that the orbit projection $\pi : G \to G/H$ is a smooth submersion. This is the smooth manifold structure of the homogeneous space.
>
> **Step 4 ($G$-action on $G/H$).** By Lemma 3, the left $G$-action $g \cdot (g'H) = (gg')H$ on $G/H$ is smooth.
>
> **Step 5 (Principal $H$-bundle).** By the quotient manifold theorem's structure: $\pi : G \to G/H$ is a smooth submersion, the right $H$-action on $G$ is free, smooth, and proper, and $G/H$ is the orbit space. Locally over each open $U \subseteq G/H$, $\pi^{-1}(U) \cong U \times H$ as smooth $H$-spaces. This is exactly the structure of a **principal $H$-bundle**.
>
> **Step 6 (Uniqueness).** Uniqueness of the smooth structure on $G/H$ such that $\pi$ is a submersion is part of the quotient manifold theorem (Lee Thm 4.29 plus the construction).
>
> Hence $G/H$ has a unique smooth manifold structure with the stated properties. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Geometric topology — computing $\pi_k$ of homogeneous spaces.** The principal-bundle structure $H \to G \to G/H$ gives a long exact sequence of [[Def - Homotopy|homotopy]] [[Def - Group|groups]]: $\cdots \to \pi_{k+1}(G/H) \to \pi_k(H) \to \pi_k(G) \to \pi_k(G/H) \to \pi_{k-1}(H) \to \cdots$. For $S^n = \mathrm{SO}(n+1)/\mathrm{SO}(n)$, this is used inductively to compute $\pi_k$ of spheres in low [[Def - Dimension|dimensions]], and to recognize $\pi_1(\mathrm{SO}(n)) = \mathbb{Z}/2$ for $n \geq 3$ (the topological origin of spinors).

**Algebraic geometry — flag manifolds as homogeneous spaces of $\mathrm{GL}(n, \mathbb{C})$.** The full flag manifold $\mathrm{Fl}(n) = \mathrm{GL}(n, \mathbb{C})/B$ where $B$ is the Borel subgroup of upper-triangular matrices, by orbit-stabilizer (the action on complete flags is transitive, stabilizer of the standard flag is $B$). The smooth manifold structure comes from this theorem; it is also a smooth projective algebraic variety, and the structure of the Bruhat decomposition is read off the structure of $G/B$ as a union of Schubert cells.

**Geometric mechanics — the cotangent bundle of a Lie group.** $T^* G$ has a natural Hamiltonian action of $G \times G$ (left and right translations), and the **moment map** for the left action sends $T^* G \to \mathfrak{g}^*$ via right translation to the identity. This is how a Lie group gives rise to a Hamiltonian phase space, and the **coadjoint orbits** in $\mathfrak{g}^*$ are the symplectic reductions of $T^* G$ by the right action — homogeneous spaces $G/G_\xi$ for stabilizers $G_\xi$ of coadjoint orbits.

---

# Bridges

- **[[Thm - The Closed Subgroup Theorem|The Closed Subgroup Theorem]]** — provides the embedded Lie subgroup structure on $H$ from closedness. Without it, "closed Lie subgroup" would be ambiguous and the homogeneous space theorem would not have a clean hypothesis. Together they say: closed subgroup ⟹ embedded Lie subgroup ⟹ smooth quotient.

- **[[Thm - Orbit-Stabilizer for Lie Group Actions|Smooth Orbit-Stabilizer]]** — the converse direction. Every smooth transitive $G$-action on $M$ realizes $M$ as $G/G_p$ for a closed stabilizer $G_p$. So the orbit-stabilizer theorem and the homogeneous-space theorem together identify the category of "manifolds with smooth transitive $G$-action" with the category of "closed Lie subgroups of $G$ modulo conjugation".

- **The quotient manifold theorem (Lee Thm 21.10)** — the general result: any free proper smooth Lie group action on a manifold has a smooth quotient. The homogeneous-space theorem is the special case where the manifold is $G$ and the action is right translation by $H$. The general quotient manifold theorem is the structural foundation for principal bundles, foliations, and quotient constructions in differential geometry.

- **Klein's Erlangen program** — the geometry of $G/H$ is the geometry preserved by the $G$-action. The homogeneous space theorem provides the smooth manifold backbone on which Klein's program builds the structural geometry.

---

# Unlocked by This

> [!tip] Principal Bundles *(from Gauge Theory)*
> The map $\pi : G \to G/H$ is the universal example of a **principal $H$-bundle**. Principal bundles are the geometric objects encoding gauge symmetries: a principal $H$-bundle $P \to B$ is locally trivial with fibre $H$, and $H$ acts smoothly, freely, and properly on $P$ on the right. Connections, curvature, and characteristic classes on $P$ are the basic data of gauge theory.

> [!tip] Associated Vector Bundles *(from Gauge Theory)*
> Every linear representation $\rho : H \to \mathrm{GL}(V)$ produces an associated vector bundle $G \times_\rho V = (G \times V)/H \to G/H$, where $H$ acts on $G \times V$ by $(g, v) \cdot h = (gh, \rho(h^{-1})v)$. Sections of this bundle are exactly $H$-equivariant functions $G \to V$ (functions $f$ with $f(gh) = \rho(h^{-1}) f(g)$). This is the universal way of producing vector bundles on $G/H$ — the **Borel construction**.

> [!tip] Reductive Homogeneous Spaces *(from Riemannian Geometry, Advanced)*
> A homogeneous space $G/H$ is **reductive** if there is an $\mathrm{Ad}(H)$-invariant complement to $\mathfrak{h}$ in $\mathfrak{g}$: $\mathfrak{g} = \mathfrak{h} \oplus \mathfrak{m}$ with $\mathrm{Ad}(H) \mathfrak{m} \subseteq \mathfrak{m}$. Reductive homogeneous spaces are the natural setting for invariant Riemannian metrics, connections, and geodesics — they include all compact Lie groups (with $H$ a maximal torus and $\mathfrak{m}$ the orthogonal complement under the Killing form), all symmetric spaces, and many other examples.

> [!tip] Symplectic Reduction *(from Geometric Mechanics)*
> When $G$ acts on a symplectic manifold $(M, \omega)$ by symplectomorphisms with moment map $\mu : M \to \mathfrak{g}^*$, the **Marsden–Weinstein quotient** $\mu^{-1}(0)/G$ is a symplectic manifold of dimension $\dim M - 2\dim G$, recovering the homogeneous-space construction in the symplectic setting. This is the geometric framework for symmetry reduction in Hamiltonian mechanics.
