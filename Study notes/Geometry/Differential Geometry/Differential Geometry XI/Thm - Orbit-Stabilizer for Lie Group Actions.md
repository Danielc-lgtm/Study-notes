---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Lie Group"
  - "Def - Smooth Action of a Lie Group"
  - "Def - Homogeneous Space"
  - "Def - Equivariant Map"
tags: [geometry, differential-geometry, lie-groups]
---

# Notation

$G$ is a Lie group; $M$ is a smooth manifold with a transitive smooth left action of $G$. For $p \in M$, $G_p$ is the stabilizer, a closed Lie subgroup. The orbit map at $p$ is $\theta^{(p)} : G \to M$, $\theta^{(p)}(g) = g \cdot p$. The quotient $G/G_p$ has the smooth manifold structure from [[Thm - Homogeneous Space is a Smooth Manifold]]. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

---

# Statement

> **Theorem (Smooth Orbit-Stabilizer).** Let $G$ be a Lie [[Def - Group|group]] acting smoothly and transitively on a smooth manifold $M$. For any $p \in M$, the orbit map $\theta^{(p)} : G \to M$, $g \mapsto g \cdot p$, factors uniquely through the quotient $\pi : G \to G/G_p$ to give a $G$-equivariant [[Def - Diffeomorphism|diffeomorphism]]
>
> $$\bar\theta^{(p)} : G/G_p \xrightarrow{\;\sim\;} M.$$

> **Corollary (dimension equation).** $\dim M = \dim G - \dim G_p$.

---

# Motivation

This is the smooth-manifold analogue of the classical orbit-stabilizer theorem from finite [[Thm - Orbit-Stabiliser Theorem|group theory]]: for a finite [[Def - Group|group]] $G$ acting transitively on a finite set $X$, $|X| = |G|/|G_p|$. The smooth version replaces "$|.|$" with "$\dim$" and "$=$" with "diffeomorphism" — converting an arithmetic identity into a manifold-theoretic one.

The structural content is that **every homogeneous space is of the form $G/G_p$**. So the classification of homogeneous spaces of $G$ reduces to the classification of closed Lie [[Def - Subgroup|subgroups]] of $G$. Combined with the closed subgroup theorem and the homogeneous-space construction, this makes the theory of homogeneous spaces purely algebraic: given $G$, list its closed [[Def - Subgroup|subgroups]] $H$, form quotients $G/H$, and you have all homogeneous spaces of $G$ (up to $G$-equivariant diffeomorphism, and up to conjugation of $H$, which corresponds to changing basepoint in $M$).

The corollary $\dim M = \dim G - \dim G_p$ is the smooth version of $|X| = |G|/|G_p|$, and it is the workhorse for dimension counts: knowing the [[Def - Dimension|dimensions]] of $G$ and the stabilizer, one reads off the dimension of the homogeneous space. Examples: $\dim S^n = \dim \mathrm{SO}(n+1) - \dim \mathrm{SO}(n) = n$, $\dim \mathrm{Gr}_k(\mathbb{R}^n) = \dim \mathrm{O}(n) - \dim(\mathrm{O}(k) \times \mathrm{O}(n-k)) = k(n-k)$.

The theorem is the bridge between abstract orbit-stabilizer (purely combinatorial) and the smooth manifold-theoretic version (which provides the diffeomorphism structure, not just the dimension count).

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is a transitive smooth Lie group action.

The first source is **a familiar manifold with a recognizable group of symmetries**. Property $B$ is "$M$ has a natural transitive symmetry group $G$". The bridge is to compute the stabilizer of a basepoint $p \in M$ and conclude $M \cong G/G_p$. This is how spheres, projective spaces, Grassmannians, flag manifolds, hyperbolic spaces, etc., are realized as homogeneous spaces.

A second source is **an inhomogeneous problem with an underlying symmetry**. Property $B$ is "a problem on $M$ is hard because $M$ is complicated, but $M$ has lots of symmetry". The bridge: realize $M = G/H$, transfer the problem to $G$ where it can be solved using the group structure, then descend back to $M$. This is how differential operators on $S^n$ are computed (using harmonic analysis on $\mathrm{SO}(n+1)$), and how representations of compact Lie groups are constructed (Borel–Weil on flag manifolds).

A third source is **a quotient construction $G/H$ for closed $H \leq G$**, viewed from the other direction. Property $B$ is "we have $G$ and a closed subgroup $H$". The bridge: $G/H$ is a homogeneous space (Lee Thm 21.17), and the orbit-stabilizer theorem identifies it as the orbit of a basepoint under any extension of the $G$-action to a manifold.

**Targets (Output Amplification)**

The conclusion is an equivariant diffeomorphism $G/G_p \cong M$ plus the dimension equation.

The first amplification is **invariant geometry on $M$ from $H$-equivariant data**. Once $M \cong G/H$ is established, every $G$-invariant geometric object on $M$ — Riemannian metric, connection, differential operator — corresponds to an $H$-invariant linear-algebraic object on $T_p M \cong \mathfrak{g}/\mathfrak{h}$ (the tangent space at the basepoint), where $H$ acts via the isotropy representation $H \to \mathrm{GL}(\mathfrak{g}/\mathfrak{h})$. This converts global geometry into linear-representation theory of $H$.

A second amplification is **dimension computation**. For Grassmannians, flag manifolds, Stiefel manifolds, etc., the dimension is read off from the dimensions of the relevant matrix groups via orbit-stabilizer. For instance, the Stiefel manifold $V_k(\mathbb{R}^n)$ of orthonormal $k$-frames in $\mathbb{R}^n$ is $\mathrm{O}(n)/\mathrm{O}(n - k)$, of dimension $\binom{n}{2} - \binom{n-k}{2} = k(2n - k - 1)/2$.

A third amplification is **classification of group actions**. The equivariant rank theorem says every equivariant smooth map between homogeneous spaces is determined (up to a finite set of choices) by the corresponding map of stabilizers. So $G$-equivariant smooth maps $G/H \to G/K$ are essentially elements of $K \backslash G / H$ (the double-coset space) with appropriate stabilizer constraints — combinatorial data.

A fourth amplification is **the dimension equation for fibrations**. Combining orbit-stabilizer with the quotient manifold theorem, $G \to G/H$ is a principal $H$-bundle, with $\dim G = \dim(G/H) + \dim H$. This is the basic fibration $H \hookrightarrow G \to G/H$ from which many topological invariants of $G$ are computed.

---

# Why Is It True

The proof has three ingredients: (i) the orbit map $\theta^{(p)}$ has constant rank by the equivariant rank theorem; (ii) by transitivity, the orbit map is surjective; (iii) the level sets of $\theta^{(p)}$ are left [[Def - Coset|cosets]] of $G_p$, so $\theta^{(p)}$ descends to a continuous bijection $G/G_p \to M$, which is then a diffeomorphism by the constant-rank theorem and properness.

**The bolded mechanism summary: an equivariant smooth map from a homogeneous space has constant rank, and a surjective constant-rank map factors through its quotient by the stabilizer to give a diffeomorphism — applied to the orbit map, this gives $G/G_p \cong M$.**

Step by step:

1. **Constant rank.** $\theta^{(p)} : G \to M$ is $G$-equivariant (with $G$ acting on itself by left translation, and on $M$ by the given action: $\theta^{(p)}(hg) = (hg) \cdot p = h \cdot (g \cdot p) = h \cdot \theta^{(p)}(g)$). The action on $G$ is transitive (any $g_1$ can be sent to any $g_2$ by $L_{g_2 g_1^{-1}}$). By the equivariant rank theorem (Lee Thm 7.25), $\theta^{(p)}$ has constant rank.

2. **Rank equals $\dim M$.** Since $\theta^{(p)}$ is surjective (by transitivity of the $G$-action on $M$) and has constant rank, the rank equals $\dim M$ (Lee Thm 4.14 — a smooth map of constant rank $\leq \dim$-target whose image has full measure has rank equal to $\dim$-target).

3. **Quotient.** The level sets $(\theta^{(p)})^{-1}(\{q\})$ are precisely the left [[Def - Coset|cosets]] of $G_p$: indeed, $\theta^{(p)}(g) = q$ iff $g \cdot p = q$, and choosing one such $g_0$, every other $g$ with $g \cdot p = q$ satisfies $g = g_0 h$ for $h \in G_p$, i.e., $g \in g_0 G_p$. So $\theta^{(p)}$ descends through $\pi : G \to G/G_p$ to a continuous bijection $\bar\theta^{(p)} : G/G_p \to M$.

4. **Smoothness and inverse.** $\bar\theta^{(p)}$ is smooth (since the action map $\theta$ is smooth) and injective (by step 3). By the rank theorem applied to $\theta^{(p)}$, $\theta^{(p)}$ is locally a submersion (since rank = $\dim M$); hence $\bar\theta^{(p)} : G/G_p \to M$ is a local diffeomorphism. A bijective local diffeomorphism is a diffeomorphism.

For the equivariance of $\bar\theta^{(p)}$: $\bar\theta^{(p)}(g \cdot \bar g) = g \bar g \cdot p = g \cdot (\bar g \cdot p) = g \cdot \bar\theta^{(p)}(\bar g)$.

---

# What Makes This Hard

The proof is structurally clean but uses several non-trivial ingredients in sequence: the equivariant rank theorem (which needs equivariance, transitivity of source action), the rank theorem itself (for the factorization), and the quotient manifold theorem (for the smooth structure on $G/G_p$). Each is non-trivial, and the orbit-stabilizer theorem is the combination.

The most common error is to forget that the **stabilizer $G_p$ must be closed** for $G/G_p$ to have a smooth manifold structure. Closedness follows automatically from continuity of the action ($G_p = \theta^{(p)})^{-1}(\{p\})$ is closed), but it must be invoked at the right moment.

A second subtlety: the theorem says $G/G_p \cong M$ **for any choice of basepoint $p$**, but different basepoints give different stabilizers. The stabilizers of any two points in the same orbit are **conjugate**: $G_{g \cdot p} = g G_p g^{-1}$. So the isomorphism class of $G/G_p$ is independent of $p$, but the specific subgroup is not. This is a smooth-manifold version of "the stabilizers of different points in the same orbit are conjugate", a fact from abstract group theory.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
The orbit map $\theta^{(p)} : G \to M$ is equivariant for the left translation action of $G$ on itself and the given action on $M$. By the equivariant rank theorem, it has constant rank, which equals $\dim M$ by transitivity. The level sets are left cosets of $G_p$, so the map factors through $G/G_p$ giving a smooth bijection. The constant-rank theorem upgrades this to a diffeomorphism.

**Subgoal decomposition:**

1. **$\theta^{(p)}$ is equivariant.** Verify $\theta^{(p)}(hg) = h \cdot \theta^{(p)}(g)$.
   - *Hint:* $\theta^{(p)}(hg) = (hg) \cdot p = h \cdot (g \cdot p) = h \cdot \theta^{(p)}(g)$, by the action axiom $g_1 \cdot (g_2 \cdot p) = (g_1 g_2) \cdot p$.

2. **Constant rank.** Apply the equivariant rank theorem.
   - *Hint:* $G$ acts transitively on itself by left translation; orbit map is equivariant; conclude constant rank.

3. **Rank equals $\dim M$.** $\theta^{(p)}$ is surjective (by transitivity on $M$); a smooth surjective map of constant rank between smooth manifolds has rank equal to $\dim M$.

4. **Factorization through quotient.** $\theta^{(p)}(g_1) = \theta^{(p)}(g_2)$ iff $g_1 \cdot p = g_2 \cdot p$ iff $g_2^{-1} g_1 \in G_p$ iff $g_1, g_2$ are in the same left coset of $G_p$. So $\theta^{(p)}$ is constant on left cosets, hence descends to $\bar\theta^{(p)} : G/G_p \to M$.

5. **$\bar\theta^{(p)}$ is a diffeomorphism.** Bijective; smooth (by smoothness of the quotient and the action); locally a diffeomorphism by the rank theorem; conclude.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\theta^{(p)}$ is equivariant
> **Statement:** $\theta^{(p)} : G \to M$ is equivariant for left translation action of $G$ on $G$ and the given action on $M$.
>
> **Hint:** Direct from the action axiom.
>
> **Why needed:** It is the condition for applying the equivariant rank theorem.
>
> > [!note]- Full proof
> > For $h, g \in G$: $\theta^{(p)}(hg) = (hg) \cdot p = h \cdot (g \cdot p) = h \cdot \theta^{(p)}(g)$, using compatibility of the action.

> [!note]- Lemma 2: $\theta^{(p)}$ has constant rank
> **Statement:** $\theta^{(p)}$ has constant rank, equal to $\mathrm{rank}(d\theta^{(p)}_e)$.
>
> **Hint:** Apply the equivariant rank theorem (Lee Thm 7.25): equivariant + transitive source action ⟹ constant rank.
>
> **Why needed:** Constant rank lets the rank theorem upgrade the orbit map factorization to a diffeomorphism.
>
> > [!note]- Full proof
> > $G$ acts on itself by left translation, which is transitive. By Lemma 1, $\theta^{(p)}$ is equivariant. By the equivariant rank theorem (Lee Thm 7.25), $\theta^{(p)}$ has constant rank.

> [!note]- Lemma 3: Rank equals $\dim M$
> **Statement:** $\mathrm{rank}(\theta^{(p)}) = \dim M$.
>
> **Hint:** Surjectivity + constant rank.
>
> **Why needed:** It identifies $\theta^{(p)}$ as a submersion onto $M$, hence locally invertible after quotienting by the kernel of the differential — which is the tangent space to the stabilizer.
>
> > [!note]- Full proof
> > By transitivity, $\theta^{(p)}$ is surjective. A smooth surjective map of constant rank between manifolds has rank equal to the dimension of the target (otherwise the image has zero measure, contradicting surjectivity). Hence $\mathrm{rank}(\theta^{(p)}) = \dim M$.

> [!note]- Lemma 4: Level sets are left cosets of $G_p$
> **Statement:** For $g \in G$, $(\theta^{(p)})^{-1}(\theta^{(p)}(g)) = g G_p$.
>
> **Hint:** $\theta^{(p)}(g_1) = \theta^{(p)}(g_2)$ iff $g_1 \cdot p = g_2 \cdot p$ iff $g_2^{-1} g_1 \in G_p$.
>
> **Why needed:** Identifies the fibres of $\theta^{(p)}$ as cosets of $G_p$, allowing factorization through $G/G_p$.
>
> > [!note]- Full proof
> > $g_1 \cdot p = g_2 \cdot p$ iff $g_2^{-1} g_1 \cdot p = p$ (acting by $g_2^{-1}$) iff $g_2^{-1} g_1 \in G_p$ iff $g_1 \in g_2 G_p$. So the level sets are left cosets.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $G$ act smoothly and transitively on $M$, and let $p \in M$. Define the orbit map $\theta^{(p)} : G \to M$, $\theta^{(p)}(g) = g \cdot p$.
>
> **Step 0 (Well-posedness).** $G_p = (\theta^{(p)})^{-1}(\{p\})$ is closed in $G$ (preimage of a point under a continuous map), hence is an embedded Lie subgroup of $G$ by [[Thm - The Closed Subgroup Theorem|the closed subgroup theorem]]. The quotient $G/G_p$ is a smooth manifold of dimension $\dim G - \dim G_p$ by [[Thm - Homogeneous Space is a Smooth Manifold]], with smooth projection $\pi : G \to G/G_p$.
>
> **Step 1 (Equivariance).** By Lemma 1, $\theta^{(p)}$ is equivariant for left-translation on $G$ and the given action on $M$.
>
> **Step 2 (Constant rank).** By Lemma 2 (equivariant rank theorem applied to the transitive left action of $G$ on itself), $\theta^{(p)}$ has constant rank. By Lemma 3, the rank equals $\dim M$.
>
> **Step 3 (Factorization).** By Lemma 4, the fibres of $\theta^{(p)}$ are left cosets of $G_p$. So $\theta^{(p)}$ is constant on each coset and descends to a unique smooth map $\bar\theta^{(p)} : G/G_p \to M$ satisfying $\bar\theta^{(p)} \circ \pi = \theta^{(p)}$.
>
> **Step 4 (Bijection).** $\bar\theta^{(p)}$ is **injective** by Lemma 4 (distinct cosets have distinct images). $\bar\theta^{(p)}$ is **surjective** because $\theta^{(p)}$ is surjective (by transitivity of the $G$-action on $M$).
>
> **Step 5 ([[Def - Diffeomorphism|Diffeomorphism]]).** $\bar\theta^{(p)}$ is a smooth bijection. By the rank theorem applied to $\theta^{(p)}$ (which has rank $\dim M$), $\theta^{(p)}$ is locally a submersion onto $M$. After quotienting by the kernel of the differential (= cosets of $G_p$), $\bar\theta^{(p)}$ becomes a local diffeomorphism. A bijective local diffeomorphism is a diffeomorphism.
>
> **Step 6 (Equivariance of $\bar\theta^{(p)}$).** For $g \in G$ and $\bar g \in G/G_p$, $\bar\theta^{(p)}(g \cdot \bar g) = \bar\theta^{(p)}([g \bar g]) = (g\bar g) \cdot p = g \cdot (\bar g \cdot p) = g \cdot \bar\theta^{(p)}(\bar g)$. So $\bar\theta^{(p)}$ is $G$-equivariant.
>
> Hence $\bar\theta^{(p)} : G/G_p \to M$ is a $G$-equivariant diffeomorphism. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Differential topology — spheres as homogeneous spaces.** $S^n = \mathrm{SO}(n+1)/\mathrm{SO}(n)$ via the natural action of $\mathrm{SO}(n+1)$ on $\mathbb{R}^{n+1}$ restricted to $S^n$. See [[Ex - S^2 as a Homogeneous Space of SO(3)]] for the $n = 2$ case. The dimension equation $\dim S^n = \dim \mathrm{SO}(n+1) - \dim \mathrm{SO}(n) = \binom{n+1}{2} - \binom{n}{2} = n$ provides an immediate sanity check.

**Grassmannians as homogeneous spaces.** $\mathrm{Gr}_k(\mathbb{R}^n) = \mathrm{O}(n)/(\mathrm{O}(k) \times \mathrm{O}(n - k))$, since $\mathrm{O}(n)$ acts transitively on $k$-planes in $\mathbb{R}^n$ and the stabilizer of a fixed $k$-plane decomposes into rotations within and orthogonal to that plane. [[Def - Dimension|Dimension]]: $\binom{n}{2} - \binom{k}{2} - \binom{n-k}{2} = k(n-k)$.

**Geometric mechanics — coadjoint orbits as symplectic manifolds.** For any Lie group $G$, the coadjoint orbits in $\mathfrak{g}^*$ (orbits under the action $\mathrm{Ad}^* : G \to \mathrm{GL}(\mathfrak{g}^*)$) are homogeneous spaces $G/G_\xi$ for the stabilizer $G_\xi$ of a covector $\xi \in \mathfrak{g}^*$. By the orbit-stabilizer theorem they are smooth manifolds; the Kirillov–Kostant–Souriau construction equips them with a canonical symplectic structure, making them the natural setting for geometric quantization. For $G = \mathrm{SU}(2)$, the coadjoint orbits in $\mathfrak{su}(2)^* \cong \mathbb{R}^3$ are spheres centered at the origin — Bohr's quantization of angular momentum, geometrically.

---

# Bridges

- **[[Thm - Orbit-Stabiliser Theorem|Orbit-stabilizer (finite groups)]]** — the discrete analogue: for $G$ acting on a finite set $X$ transitively, $|X| = |G|/|G_p|$. The smooth orbit-stabilizer theorem is the manifold version of this counting argument, with cardinality replaced by dimension.

- **[[Thm - Homogeneous Space is a Smooth Manifold]]** — the converse direction: every coset space $G/H$ for closed $H$ is a smooth manifold with a transitive $G$-action. Together with orbit-stabilizer, this gives the equivalence "homogeneous space $\Leftrightarrow$ coset space".

- **The equivariant rank theorem** (Lee Thm 7.25): for any equivariant map between $G$-manifolds with transitive $G$-action on the source, the rank is constant. This is the structural tool used in the proof.

- **Klein's Erlangen program** — a geometry is, in Klein's sense, a homogeneous space $G/H$ together with the invariants of the $G$-action. Orbit-stabilizer says every classical geometry (Euclidean, spherical, hyperbolic, projective) is of this form for an appropriate $G$ and $H$. The structural unity of classical geometries comes from the fact that they all arise as orbits of Lie group actions on familiar spaces.

---

# Unlocked by This

> [!tip] Symmetric Spaces *(from Riemannian Geometry, Advanced)*
> A **symmetric space** is a homogeneous space $G/H$ where $H$ is the fixed-point set of an involution of $G$. The orbit-stabilizer theorem is the structural tool that produces every symmetric space as a coset space, and the involution structure on $G$ gives the symmetric space its bi-invariant Riemannian metric. Classification: Cartan (1926).

> [!tip] Borel–Weil Theorem *(from Representation Theory)*
> For a compact connected Lie group $G$ with maximal torus $T$, the **flag manifold** $G/T$ is a homogeneous space (via orbit-stabilizer) and a complex projective variety. The **Borel–Weil theorem** identifies the irreducible $G$-representations with spaces of holomorphic sections of certain $G$-equivariant line bundles on $G/T$, providing a geometric construction of all irreducible representations.

> [!tip] Principal Bundle Structure *(from Gauge Theory)*
> The map $G \to G/H$ is a **principal $H$-bundle** for any closed Lie subgroup $H \leq G$ (Lee Thm 21.17). This is the universal example of a principal bundle: the bundle is "$G$ as a Lie group", the structure group is "$H$ as a Lie subgroup", and the base is "the homogeneous space $G/H$". Principal bundles are the geometric framework of gauge theory, and the simplest principal bundles arise as $G \to G/H$.

> [!tip] Quotient Manifold Theorem *(from Lie Groups, Advanced)*
> The **quotient manifold theorem** (Lee Thm 21.10): if $G$ acts smoothly, **freely**, and **properly** on a manifold $M$, then $M/G$ is a smooth manifold of dimension $\dim M - \dim G$. The orbit-stabilizer theorem applied to a transitive action is a special case; in the general case, the quotient is no longer a single orbit, and the dimension counts orbits rather than points.
