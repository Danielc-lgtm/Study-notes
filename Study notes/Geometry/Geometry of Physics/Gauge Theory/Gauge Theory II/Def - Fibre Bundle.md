---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Vector Bundle"
  - "Def - Lie Group"
  - "Def - Smooth Action of a Lie Group"
tags: [geometry, gauge-theory, fibre-bundles]
---

# Notation

A fibre bundle is data $(E, M, \pi, F, G)$ where $E$ is the **total space**, $M$ the **base**, $\pi : E \to M$ the **projection**, $F$ the **typical fibre** (a smooth manifold, possibly non-linear), and $G$ a **structure group** (a Lie group, see [[Def - Lie Group]]) acting smoothly on $F$. Local trivializations are written $\Phi_U : \pi^{-1}(U) \to U \times F$; transition functions $c_{VU} : U \cap V \to G$ act on $F$ by diffeomorphisms. The fibre over $p \in M$ is $\pi^{-1}(p)$ and is diffeomorphic to $F$. See [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]] for the full registry.

---

# Axiom Motivation

The structure we are trying to axiomatize is **a smoothly varying family of manifolds, parametrized by a base manifold**. Think of it as the geometric expansion of the idea of a vector bundle (where each fibre was a *vector space*) to allow each fibre to be an arbitrary manifold. Why would one want this generalization? Because in geometry there are many natural families of fibres that are not vector spaces: the unit tangent vectors at each point of a Riemannian manifold form a sphere $S^{n-1}$ (not a vector space — adding two unit vectors and getting another unit vector makes no sense); the set of all orthonormal frames at a point is a copy of $O(n)$ (a Lie group, not a vector space); the projective tangent spaces are $\mathbb{RP}^{n-1}$. None of these fit the vector-bundle framework, but all are bundles in the broader sense, and they share the essential features of vector bundles: local triviality, transition functions, sections, gauge symmetry. The fibre-bundle definition is the minimum amount of structure that retains those features without insisting that the fibre be linear.

Why **local triviality**? A bundle is supposed to be a smoothly varying family — and "smooth" only has meaning for things that locally look like Euclidean space. The local-triviality axiom $\pi^{-1}(U) \cong U \times F$ is what makes "smooth section", "smooth varying fibre", and "smooth bundle morphism" definable in the first place. Without local triviality we have only a set-theoretic family of fibres; with it, we have an honest smooth manifold $E$ of dimension $\dim M + \dim F$, with the local product structure providing local coordinates. If we drop local triviality but keep the fibre-by-fibre structure, we get a notion sometimes called a **fibred manifold**, which is much weaker and admits pathological examples (e.g., fibres of varying topology, jumping rank, etc.). Local triviality rules these out and is what guarantees the bundle is "a smooth family in any reasonable sense."

Why a **structure group $G$** at all, and not just "any diffeomorphism of $F$ on overlaps"? Two reasons. First, the set $\mathrm{Diff}(F)$ of all diffeomorphisms of $F$ is typically infinite-dimensional and not a Lie group, so the data of a bundle without restricting transition functions to a Lie subgroup is not amenable to differential-geometric analysis. Restricting to a finite-dimensional Lie group $G \leq \mathrm{Diff}(F)$ gives us a Lie algebra of infinitesimal symmetries, hence connection forms, curvature forms, characteristic classes, and gauge transformations. Second, the structure group is *additional geometric data* attached to the bundle — it records which kind of symmetry the fibres have. A real rank-$k$ vector bundle has structure group $\mathrm{GL}(k, \mathbb{R})$; an *oriented* one reduces to $\mathrm{GL}^+(k, \mathbb{R})$; a *Riemannian* one reduces to $\mathrm{O}(k)$; an *oriented Riemannian* one to $\mathrm{SO}(k)$. Each reduction is geometric structure, and the structure group records which. If we strengthened the structure-group axiom to demand $G = \{e\}$, we would only have trivial bundles; if we weakened it to allow all of $\mathrm{Diff}(F)$, we would have no useful theory. The Lie-subgroup-of-$\mathrm{Diff}(F)$ formulation hits the sweet spot.

Why the **cocycle condition** $c_{\alpha\gamma} = c_{\alpha\beta} \circ c_{\beta\gamma}$ on triple overlaps, with $c_{\alpha\alpha} = \mathrm{id}$? This is the consistency condition: two trivializations on $U_\alpha$ and $U_\gamma$ can be compared either directly (via $c_{\alpha\gamma}$) or through an intermediate trivialization on $U_\beta$ (via $c_{\alpha\beta} \circ c_{\beta\gamma}$), and the two routes must agree. Without it, the trivializations are inconsistent and the total space $E$ cannot be globally assembled. The cocycle condition is *not* a free axiom: it is forced by the requirement that we are gluing one and the same total space $E$. If we drop it we no longer have a bundle — we have inconsistent local data. If we strengthen it (e.g., demand $c_{\alpha\beta} = \mathrm{id}$ everywhere), we get only trivial bundles.

A fibre-bundle definition that omitted the structure group $G$ — keeping only $E, M, \pi, F$ and demanding the transition functions be diffeomorphisms — would be much weaker. The structure group is precisely the data that turns the bundle into a *gauge field*: connections take values in $\mathfrak{g}$, gauge transformations are $G$-valued maps on the base, and characteristic classes are pulled back from $H^*(BG)$. Without specifying $G$, none of this works. Conversely, *specifying* a smaller $G$ for an existing bundle is a **reduction of structure group**, a separate (and obstructed) geometric question.

---

# The Definition

A **fibre bundle** with structure group $G$ consists of:

1. A smooth manifold $E$ (the **total space**),
2. A smooth manifold $M$ (the **base space**),
3. A smooth surjective submersion $\pi : E \to M$ (the **projection**),
4. A smooth manifold $F$ (the **typical fibre**),
5. A Lie group $G$ together with a smooth left action $G \times F \to F$ (the **structure group** and its action on the fibre),

such that there exists an open cover $\{U_\alpha\}$ of $M$ together with diffeomorphisms (**local trivializations**)
$$\Phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times F$$
satisfying $\mathrm{pr}_1 \circ \Phi_\alpha = \pi$, and such that on each overlap $U_\alpha \cap U_\beta \neq \emptyset$ the composition
$$\Phi_\alpha \circ \Phi_\beta^{-1} : (U_\alpha \cap U_\beta) \times F \to (U_\alpha \cap U_\beta) \times F$$
has the form $(p, y) \mapsto (p, c_{\alpha\beta}(p) \cdot y)$ for a smooth **transition function** $c_{\alpha\beta} : U_\alpha \cap U_\beta \to G$. The transition functions satisfy
$$c_{\alpha\alpha}(p) = e, \qquad c_{\alpha\beta}(p) = c_{\beta\alpha}(p)^{-1}, \qquad c_{\alpha\gamma}(p) = c_{\alpha\beta}(p) \cdot c_{\beta\gamma}(p)$$
on overlaps $U_\alpha \cap U_\beta \cap U_\gamma$ (the **cocycle condition**).

A **local section** of $\pi$ over an open $U \subseteq M$ is a smooth map $s : U \to E$ with $\pi \circ s = \mathrm{id}_U$. A **global section** is a local section with $U = M$. The bundle is **trivial** if there exists a global trivialization $\Phi : E \to M \times F$ (equivalently, transition functions can be chosen to be identically $e$).

---

# Relate to Other Fields / Compression

A fibre bundle is **a vector bundle with the linearity dropped from the fibre**. Specifically: a real rank-$k$ vector bundle (in the sense of [[Def - Vector Bundle]]) is a fibre bundle with $F = \mathbb{R}^k$ and $G = \mathrm{GL}(k, \mathbb{R})$ acting by matrix multiplication. Dropping the demand $F = \mathbb{R}^k$ gives the more general fibre bundle, with any smooth manifold $F$. The reverse direction — recovering vector bundles as a *case* — is the associated-bundle construction $E = P \times_G \mathbb{R}^k$ once a principal bundle $P$ is in hand.

A fibre bundle is also **a covering space when $F$ is discrete**: covering spaces of $M$ are precisely fibre bundles with discrete fibre and discrete structure group (a subgroup of the symmetric group of $F$). The connected double cover of a non-orientable manifold is the prototypical example: $F = \{+, -\}$, $G = \mathbb{Z}/2$. The covering-space theory of [[Algebraic Topology II — Fundamental Group and Covering Spaces|Algebraic Topology II]] is the fibre-bundle theory of this chapter, restricted to discrete fibres.

**True name:** A fibre bundle is **a free local product structure with consistent gluing**. The operational content is: locally $E$ looks like $U \times F$ (the trivializations), and the consistency of the local pictures is encoded by transition functions in a Lie group (the gluing data). This dual presentation — local pictures plus gluing — is the working definition for almost every construction in the theory.

---

# Examples / Corollaries

**Is an instance: the trivial bundle $E = M \times F$.** Take $\pi$ to be the projection onto $M$. The single global trivialization $\Phi = \mathrm{id}$ shows the bundle is trivial; the structure group can be taken to be the trivial group $\{e\}$.

**Is an instance: the unit tangent bundle $T_0 M$ of a Riemannian manifold.** For $M$ Riemannian, $T_0 M$ has fibre $S^{n-1}$ (the unit sphere in each tangent space), structure group $\mathrm{O}(n)$ (or $\mathrm{SO}(n)$ if oriented), and local trivializations from orthonormal frame fields. This is a fibre bundle but *not* a vector bundle, since the fibre $S^{n-1}$ is not a vector space.

**Is an instance: the Möbius strip as a real line bundle over $S^1$.** $E$ is the open Möbius band, $M = S^1$, $F = \mathbb{R}$, $G = \mathbb{Z}/2 = \{\pm 1\} \subset \mathrm{GL}(1, \mathbb{R})$. The transition function on the two-piece overlap is $\pm 1$, with the sign change on one piece making the bundle nontrivial. This is a vector bundle (rank 1) and also a fibre bundle; the structure group is the discrete $\mathbb{Z}/2$ rather than the full $\mathrm{GL}(1, \mathbb{R})$.

**Is an instance: a covering space.** A connected $n$-sheeted covering $p : \tilde M \to M$ is a fibre bundle with $F = \{1, 2, \ldots, n\}$ discrete and $G$ a transitive subgroup of $S_n$. The transition functions, being valued in a discrete group, are locally constant.

**Is an instance: the Hopf bundle $S^3 \to S^2$.** Total space $E = S^3 \subset \mathbb{C}^2$, base $M = S^2 = \mathbb{CP}^1$, fibre $F = S^1$, structure group $G = U(1)$. The projection sends $(z_0, z_1)$ to $[z_0 : z_1] \in \mathbb{CP}^1$. The transition function on the standard two-patch overlap of $S^2$ is $z/|z| = e^{i\phi}$ — a nontrivial map $U \cap V \to U(1)$.

**Is NOT an instance: the cone $\mathrm{Cone}(M) = (M \times [0, 1]) / (M \times \{0\})$.** The "fibre" over the apex degenerates to a single point, violating local triviality (and in fact violating the demand that $\pi$ be a submersion at the apex). The cone is not a fibre bundle; it is a quotient that destroys the bundle structure at one point.

**Is NOT an instance: a singular foliation with leaves of varying dimension.** If the leaves of a partition of $M$ have different dimensions at different points (e.g., a 2-dimensional leaf collapsing to a 1-dimensional leaf along a subset), the partition does not arise from a fibre bundle: the local-triviality axiom forces $\pi^{-1}(p) \cong F$ with a *fixed* $F$, hence a single dimension. The example: $\mathbb{R}^2$ partitioned into the line $x = 0$ and circles $x = r > 0$ around the origin is not a fibre bundle structure.

**Corollary (the total space is a smooth manifold of dimension $\dim M + \dim F$).** The local triviality $\pi^{-1}(U_\alpha) \cong U_\alpha \times F$ provides charts on $E$ via product charts on $U_\alpha \times F$, with smooth transition functions on overlaps inherited from the smoothness of $c_{\alpha\beta}$ and the smooth $G$-action.

**Corollary (a section exists locally over any trivializing patch).** Over $U_\alpha$, pick any $y_0 \in F$ and define $s : U_\alpha \to E$ by $s(p) = \Phi_\alpha^{-1}(p, y_0)$. This is smooth and satisfies $\pi \circ s = \mathrm{id}$. Global sections need not exist.

**Corollary (the bundle is trivial if and only if there is a global trivialization, equivalently if the transition functions can be normalized to $c_{\alpha\beta} \equiv e$ on all overlaps).** A global section of a principal bundle is equivalent to triviality; a global section of a general fibre bundle does not imply triviality (e.g., the zero section of any vector bundle exists).

**Calibration check.** If you understand the definition you should be able to (i) construct the Möbius bundle from its two-patch transition function and verify the cocycle condition; (ii) identify the structure group of the unit tangent bundle of an orientable Riemannian $n$-manifold as $\mathrm{SO}(n)$; (iii) verify that the trivial bundle has structure group reducible to $\{e\}$.

---

# Unlocked by This

> [!tip] Principal $G$-Bundle *(from Gauge Theory)*
> When the typical fibre $F$ coincides with the structure group $G$ itself, and the transition functions act on $F = G$ by *left* translation, the fibre bundle becomes a **principal $G$-bundle**. This is the universal object from which all other bundles with structure group $G$ are recovered by the associated-bundle construction. See [[Def - Principal G-Bundle]] for the formal definition and [[Gauge Theory III — Connections in Principal and Associated Bundles]] for the connection theory.

> [!tip] Associated Bundle *(from Gauge Theory)*
> Given a principal $G$-bundle $P$ and any smooth $G$-action on a manifold $F$, the associated bundle $P \times_G F$ is a fibre bundle with fibre $F$ and the same structure group. Every fibre bundle with structure group $G$ is an associated bundle of its frame bundle. See [[Def - Associated Bundle]].

> [!tip] Classifying Space $BG$ *(from Algebraic Topology)*
> The classification of fibre bundles with structure group $G$ over a base $M$ (up to isomorphism) reduces to the homotopy classification of maps $M \to BG$, where $BG$ is the **classifying space** of $G$ and $EG \to BG$ is the universal principal $G$-bundle. The cohomology $H^*(BG)$ is the home of all characteristic classes of $G$-bundles. This is the bridge from differential geometry to homotopy theory.
