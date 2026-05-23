---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Vector Bundle"
  - "Def - Local Frame"
  - "Def - Subspace"
  - "Def - Embedded Submanifold"
tags: [geometry, differential-geometry, bundles, subbundle]
---

# Notation

$\pi : E \to M$ is a smooth vector bundle of rank $k$ over a smooth manifold $M$. The candidate subbundle is denoted $D \subseteq E$, with $D_p := D \cap E_p$ the fibre of $D$ over $p$. The dimension of $D_p$ is denoted $m$, the **rank** of the subbundle, with $0 \leq m \leq k$.

---

# Axiom Motivation

A subbundle is the bundle counterpart of a vector subspace, made to vary smoothly with $p$. The motivating examples are direct: the kernel of a constant-rank bundle homomorphism, the span of a nonvanishing vector field, the kernel of a 1-form on tangent vectors — all are families of [[Def - Subspace|subspaces]] parametrized by $M$, and all deserve to be regarded as bundles in their own right.

The defining condition has three parts, each forced by what we mean by "subbundle".

First, $D$ should be a subset of $E$, and at each point $p$, $D_p = D \cap E_p$ should be a linear subspace of $E_p$. Without this, $D$ would not even be a "family of subspaces"; the fibrewise inclusion is the basic structural condition.

Second, the **[[Def - Dimension|dimension]] $m$ of $D_p$ should be constant** as $p$ varies. This is the crucial condition. A family of subspaces of varying dimension does exist as a set, but it does not have a bundle structure: at points where the dimension jumps, no local trivialization with a fixed model fibre exists. The constant-rank condition is exactly what makes $D$ locally trivial in the bundle sense. As a non-example, consider the "bundle" whose fibre at $p \in \mathbb{R}$ is the line $\mathbb{R} \subseteq \mathbb{R}^2$ when $p \neq 0$ and the whole $\mathbb{R}^2$ when $p = 0$ — this is a family of subspaces of $\mathbb{R}^2$, but not a subbundle, because the rank jumps.

Third, $D$ should be an **embedded submanifold** of $E$ (the total space) — not just a subset, but one carrying a compatible smooth structure inherited from $E$. This is what makes $D$ a smooth manifold in its own right, with the inclusion $D \hookrightarrow E$ a smooth embedding. The constant-rank condition together with the local-frame criterion (below) is what guarantees this submanifold structure exists.

What is forced by demanding **constant rank** $m$ rather than merely "linear subspace at each point"? Local triviality of $D$ as a bundle requires a constant model fibre $\mathbb{R}^m$. Without constant rank, the local-trivialization condition cannot be satisfied near points where the dimension changes — there is no [[Def - Diffeomorphism|diffeomorphism]] with $U \times \mathbb{R}^m$ for any single $m$. The constant-rank condition is the bundle-theoretic embodiment of "smoothness of subspace structure".

What is forced by demanding $D$ is an **embedded submanifold** of $E$? An embedded submanifold has the subspace topology and a compatible smooth structure. Without this, $D$ might be an *immersed* submanifold — locally a submanifold but globally tangled — and the bundle structure on $D$ might not be well-behaved at the global level. The embedded condition is what makes the geometry of $D$ inside $E$ clean.

What is forced by demanding **$D$ is itself a smooth vector bundle** under the restricted projection $\pi|_D : D \to M$? This is the conclusion the definition packages: once the constant-rank and embedded-submanifold conditions are satisfied, the local-frame criterion ([[Thm - Local Frames Span Sections]] applied to local sections that span $D$) certifies $D$ is a smooth vector bundle. The definition is essentially saying: "$D$ is a subset of $E$ whose fibrewise restriction gives a bundle".

What if we **strengthened** to demand $D$ is a *full* subbundle ($D_p = E_p$ for all $p$)? Then $D = E$, and the subbundle concept collapses. The interesting case is $0 < m < k$.

What if we **weakened** by allowing varying-dimension subspaces? Then we have a **family of linear subspaces** but not a subbundle. Such families arise (e.g., the kernel of a bundle homomorphism of nonconstant rank), and one can study them, but they do not have the clean vector-bundle structure of subbundles. The Frobenius theorem on involutive distributions is precisely the constant-rank case where things work.

The local-frame criterion is the technical heart of the definition and gives a working diagnostic. It says: $D \subseteq E$ is a subbundle if and only if each point of $M$ has a neighbourhood $U$ on which there exist smooth local sections $\sigma_1, \dots, \sigma_m$ of $E$ such that $\sigma_1(q), \dots, \sigma_m(q)$ is a basis of $D_q$ for every $q \in U$. So a subbundle is "a family of subspaces locally spanned by smooth sections" — a clean and verifiable condition.

---

# The Definition

Let $\pi : E \to M$ be a smooth vector bundle of rank $k$. A **smooth subbundle** of $E$ of rank $m$ (with $0 \leq m \leq k$) is a subset $D \subseteq E$ satisfying:

1. **Subspace condition:** for every $p \in M$, the fibre $D_p := D \cap E_p$ is a linear subspace of $E_p$ of dimension exactly $m$ (independent of $p$).
2. **Embedded submanifold condition:** $D$ is an embedded submanifold of $E$ (in the sense of [[Def - Embedded Submanifold]]).
3. **Bundle condition:** the restricted projection $\pi|_D : D \to M$, together with the vector-space structure inherited fibrewise from $E$, makes $D$ a smooth vector bundle of rank $m$ over $M$.

Condition (3) is in fact a consequence of (1) and (2) together with smoothness in the bundle theory sense; the three conditions are usually stated together for clarity.

**Local-frame criterion** ([[Thm - Local Frames Span Sections]] adapted): $D \subseteq E$ is a smooth subbundle of rank $m$ if and only if every point $p \in M$ has an open neighbourhood $U$ on which there exist smooth local sections $\sigma_1, \dots, \sigma_m \in \Gamma(U, E)$ such that $\sigma_1(q), \dots, \sigma_m(q)$ is a basis of $D_q$ for every $q \in U$. Such a tuple $(\sigma_1, \dots, \sigma_m)$ is called a **local frame for $D$**.

A bundle homomorphism $F : E \to E'$ over $M$ of **constant rank** $r$ (the rank of each $F_p : E_p \to E'_p$ is $r$, independent of $p$) has $\ker F = \bigsqcup_p \ker F_p$ as a smooth subbundle of $E$ of rank $k - r$, and $\mathrm{im} F = \bigsqcup_p \mathrm{im} F_p$ as a smooth subbundle of $E'$ of rank $r$. The constant-rank hypothesis is essential — without it, the kernel and image are families of subspaces of varying dimension, not subbundles.

---

# Relate to Other Fields / Compression

A subbundle is **the bundle counterpart of a vector subspace**, varying smoothly with $p$. The analogy with linear algebra is exact: every subspace $W \subseteq V$ of a vector space corresponds, at each fibre, to a subspace $D_p \subseteq E_p$, and the constant-rank condition is the smooth-bundle version of "fixed dimension" for subspaces.

A subbundle is also a **family of linear subspaces parametrized by $M$**, locally spanned by smooth sections. The local-frame criterion makes this precise: a subbundle is "a family of subspaces such that local bases exist smoothly".

**True name:** the true name of a subbundle is "**a constant-rank family of linear subspaces, smoothly varying with the base point**". The operational diagnostic is the local-frame criterion: if you can produce locally-defined smooth sections that span each fibre of $D$, then $D$ is a subbundle.

A useful slogan: **subbundles are detected by local frames**. Whenever you suspect a family of subspaces is a subbundle, the proof strategy is to construct local frames; the proof of non-subbundleness is to show that local frames cannot exist (typically because the rank changes).

In the theory of [[Def - Distribution on a Manifold|distributions]] on a manifold (a distribution is a subbundle of $TM$), the Frobenius theorem characterizes which distributions are *integrable* — that is, when they arise as tangent spaces to a foliation. The constant-rank condition is essential there; without it, even the concept of integrability would not make sense.

---

# Examples / Corollaries

**Is an instance — the span of a nonvanishing vector field.** If $X$ is a nowhere-vanishing smooth vector field on $M$, then $D := \{c X_p : p \in M, c \in \mathbb{R}\} \subseteq TM$ is a smooth rank-$1$ subbundle of $TM$. Locally, $X$ itself is a local frame for $D$. The "nowhere-vanishing" condition is precisely what guarantees rank constancy.

**Is an instance — the kernel of a constant-rank bundle homomorphism.** If $F : E \to E'$ is a smooth bundle homomorphism over $M$ with $\mathrm{rank}(F_p) = r$ constant in $p$, then $\ker F \subseteq E$ is a smooth subbundle of rank $k - r$. The proof uses the constant-rank hypothesis to construct local frames for $\ker F$ via a basis-completion argument.

**Is an instance — the tangent bundle of a submanifold.** If $S \subseteq M$ is an embedded submanifold, the tangent bundle $TS$ embeds into $TM|_S$ as a smooth subbundle, identifying $T_pS$ with a linear subspace of $T_pM$ at each $p \in S$. The rank of this subbundle is $\dim S$.

**Is an instance — the trivial bundle of rank 0.** The "zero subbundle" $\{0_p\}_{p \in M} \subseteq E$ is a rank-$0$ subbundle, isomorphic to $M$ itself via the zero section. It is the trivial example.

**Is an instance — the full bundle as a subbundle of itself.** $E$ is a rank-$k$ subbundle of itself.

**Is NOT a subbundle — a varying-rank family.** Consider $M = \mathbb{R}$, $E = \mathbb{R} \times \mathbb{R}^2$, and $D_p =$ the line spanned by $(1, p)$ when $p \neq 0$, $D_0 = \{0\}$. The dimension drops at $p = 0$, so $D$ is not a subbundle. Even though $D$ is a smooth family of subspaces away from $0$, the rank-jump destroys local triviality near the origin.

**Is NOT a subbundle — a discontinuous family.** Take $E = \mathbb{R} \times \mathbb{R}^2$ and $D_p = \mathbb{R} \times \{0\}$ for $p \leq 0$, $D_p = \{0\} \times \mathbb{R}$ for $p > 0$. Same rank everywhere, but the assignment $p \mapsto D_p$ is not continuous (the subspace flips abruptly at $0$). No local sections can span $D$ near $0$, so the local-frame criterion fails.

**Is NOT a subbundle — the kernel of a bundle homomorphism of varying rank.** Define $F : \mathbb{R}^2 \to \mathbb{R}^2$ (as a bundle homomorphism over $\mathbb{R}$) by $F_p(v) = p \cdot v$. The kernel is $\{0\}$ when $p \neq 0$ and all of $\mathbb{R}^2$ when $p = 0$. Rank-jump, so $\ker F$ is not a subbundle.

**Corollary — every subbundle has a complementary subbundle locally.** If $D \subseteq E$ is a smooth rank-$m$ subbundle, then locally there exists a complementary rank-$(k - m)$ subbundle $D'$ with $E|_U = D|_U \oplus D'|_U$. The construction uses the [[Def - Direct Sum|direct sum]] of vector spaces fibrewise; the complement is unique up to choice, and global existence of a complement requires the bundle to be split (a topological condition).

**Corollary — the quotient bundle exists.** Given a smooth subbundle $D \subseteq E$, the **quotient bundle** $E/D$ exists, with fibre $(E/D)_p = E_p / D_p$ — a vector space of dimension $k - m$. The bundle structure on $E/D$ comes from the local triviality of $D$ and $E$ and the constant-rank condition. Sections of $E/D$ over $M$ correspond to sections of $E$ modulo sections of $D$.

**Corollary — direct sums of subbundles.** If $D_1, D_2 \subseteq E$ are subbundles with $D_1 \cap D_2 = 0$ fibrewise (so $D_{1,p} \cap D_{2,p} = \{0\}$ for all $p$), then $D_1 \oplus D_2 \subseteq E$ — defined fibrewise as $D_{1,p} + D_{2,p}$ — is a smooth subbundle of rank $\dim D_1 + \dim D_2$. This is the bundle counterpart of internal direct sum of subspaces.

**Calibration check.** Verify that the span of a nonvanishing vector field is a rank-$1$ subbundle of $TM$ by constructing the local frame explicitly. Verify that the rank-jump non-example above is *not* a subbundle by showing the local-frame criterion fails at the jump point. Convince yourself that constant rank is essential by considering what happens to local trivializations near a rank-jump.

---

# Unlocked by This

> [!tip] Distribution on a Manifold *(from Differential Geometry X)*
> A **distribution** of rank $m$ on $M$ is precisely a smooth rank-$m$ subbundle of the tangent bundle $TM$. Distributions encode "fields of $m$-planes" in $TM$, and the **Frobenius theorem** characterizes when a distribution is *integrable* — that is, when it arises as tangent spaces to a foliation of $M$ by $m$-dimensional submanifolds. Integrable distributions are exactly the **involutive** ones (closed under Lie bracket), and the theorem is the bridge between local linear-algebra (subbundles) and global submanifold theory.

> [!tip] Splitting of a Vector Bundle *(from Bundle Theory)*
> A bundle $E$ **splits** into a direct sum of subbundles $E = D_1 \oplus D_2$ when each $E_p$ admits a corresponding subspace decomposition smoothly varying in $p$. The Whitney sum is the universal splitting construction. Splittings are obstructed: not every short exact sequence of bundles $0 \to D \to E \to E/D \to 0$ splits, and the obstruction is a characteristic class. For complex bundles, the splitting principle is a powerful technique in algebraic topology.

> [!tip] Tangent and Normal Bundles of an Immersion *(from Riemannian Geometry)*
> For a submanifold $S \subseteq M$ with a Riemannian metric on $M$, the tangent bundle $TM|_S$ splits as $TS \oplus NS$, where $TS$ is the tangent subbundle (tangent to $S$) and $NS$ is the **normal bundle** (orthogonal complement of $TS$ in $TM|_S$). This decomposition is the foundation of submanifold geometry: second fundamental forms, principal curvatures, Gauss and Codazzi equations all live in terms of the splitting $TM|_S = TS \oplus NS$.
