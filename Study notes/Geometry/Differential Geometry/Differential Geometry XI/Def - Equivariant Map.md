---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Lie Group"
  - "Def - Smooth Action of a Lie Group"
  - "Def - Smooth Map between Manifolds"
tags: [geometry, differential-geometry, lie-groups]
---

# Notation

$G$ is a Lie group; $M, N$ are smooth manifolds carrying smooth actions of $G$. We write $g \cdot p$ for the action on $M$ and $g \cdot q$ for the action on $N$ (left actions; with the obvious modifications for right). An equivariant map is denoted $F : M \to N$. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

---

# Axiom Motivation

When two manifolds $M$ and $N$ carry smooth actions of the same Lie group $G$, the natural maps between them are those that **respect** the $G$-actions — sending a $G$-symmetry of $M$ to the corresponding $G$-symmetry of $N$. An equivariant map is precisely this: a smooth map $F : M \to N$ such that $F(g \cdot p) = g \cdot F(p)$ for all $g, p$.

Why this condition? It is the manifold-theoretic version of "homomorphism of $G$-sets": the morphisms in the category of $G$-spaces. Without it, $F$ is just a smooth map of manifolds with no relationship to the $G$-actions; with it, $F$ becomes a "$G$-equivariant" smooth map, intertwining the two actions.

The most important structural consequence is **constant rank**. If $F : M \to N$ is equivariant and $G$ acts transitively on $M$, then $F$ has constant rank — equal to the rank of $dF$ at any one point. The proof is by equivariance: $F \circ \theta_g = \phi_g \circ F$ where $\theta_g, \phi_g$ are the actions of $g$ on $M, N$ respectively. Differentiating at $p$ gives $dF_{g \cdot p} \circ d(\theta_g)_p = d(\phi_g)_{F(p)} \circ dF_p$. Since $\theta_g$ and $\phi_g$ are diffeomorphisms, their differentials are isomorphisms, so the rank of $dF_{g \cdot p}$ equals the rank of $dF_p$. Transitivity then means any two points are connected by such a $g$, so the rank is constant.

This is the **equivariant rank theorem** (Lee Thm 7.25), and it is what makes equivariant maps so tractable: constant rank unlocks the [[Thm - The Rank Theorem|rank theorem]] (Lee Thm 4.12) — $F$ factors locally as a submersion followed by an immersion. So equivariant maps automatically have all the nice local structure of constant-rank maps without any extra assumption.

Why **two** actions of $G$ rather than one? Equivariance is intrinsically a comparison: we need $G$ to act on both $M$ and $N$, and we compare how $F$ intertwines the two actions. The actions can be different (transitive vs non-transitive, with different stabilizers); equivariance imposes no constraint other than that the same $G$ act on both.

What if we **drop equivariance** and just consider arbitrary smooth maps $M \to N$ between $G$-manifolds? Then we lose the constant-rank theorem and most of the structural payoff. The smooth maps $M \to N$ form a vast space; the equivariant ones form a small, structured subset that is the source of orbit-stabilizer, homogeneous-space identification, and equivariant bundle theory.

What if we **strengthen** by requiring $F$ to be a diffeomorphism? Then we get the notion of **$G$-equivariant diffeomorphism**, the right notion of isomorphism in the category of $G$-spaces. Examples include the orbit-map diffeomorphism $G/G_p \to G \cdot p$ for a smooth action.

The summary: equivariance is the condition that morphisms in the category of $G$-spaces should respect both the smooth-manifold and the $G$-action structure. It is the joint condition.

---

# The Definition

Let $G$ be a Lie group, and let $M, N$ be smooth manifolds equipped with smooth left $G$-actions $\theta : G \times M \to M$ and $\phi : G \times N \to N$.

A smooth map $F : M \to N$ is **equivariant** (or **$G$-equivariant**) if it commutes with the two actions:

$$F(g \cdot p) = g \cdot F(p) \qquad \text{for all } g \in G, \; p \in M.$$

In diagrammatic form, $F \circ \theta_g = \phi_g \circ F$ for every $g \in G$, i.e., the following square commutes for each $g$:

$$
\begin{array}{ccc}
M & \xrightarrow{F} & N \\
\theta_g \downarrow & & \downarrow \phi_g \\
M & \xrightarrow{F} & N
\end{array}
$$

For right actions, the analogous condition is $F(p \cdot g) = F(p) \cdot g$.

The smooth maps form a category $G\text{-}\mathbf{Man}$ whose objects are $G$-manifolds and whose morphisms are equivariant smooth maps. An equivariant diffeomorphism is the corresponding notion of isomorphism.

The **equivariant rank theorem** (Lee Thm 7.25): if $F : M \to N$ is equivariant and $G$ acts transitively on $M$, then $F$ has constant rank. As a consequence, by the [[Thm - The Rank Theorem|rank theorem]]:

- If $\mathrm{rank}(dF) = \dim N$ everywhere (and $G$ is transitive on $M$), then $F$ is a smooth submersion;
- If $\mathrm{rank}(dF) = \dim M$ everywhere, then $F$ is a smooth immersion;
- If additionally $F$ is injective and a topological embedding, then $F$ is a smooth embedding.

---

# Relate to Other Fields / Compression

An equivariant map is the **morphism in the category of $G$-spaces**: a smooth map intertwining two $G$-actions. It is the simultaneous smooth-and-$G$-respecting version of the notion of morphism, the manifold-theoretic counterpart of "homomorphism of $G$-modules" or "$G$-equivariant function" in representation theory.

From the abstract group-action side, equivariance is just the standard "morphism of $G$-sets" condition $F(g \cdot p) = g \cdot F(p)$. From the smooth-manifold side, the smoothness condition makes the manifold structure interact with the action. Both are inherited.

**True name:** An equivariant map is **a smooth map that descends to the orbit spaces**: if $F : M \to N$ is equivariant, it induces a unique smooth map $\bar F : M/G \to N/G$ on orbit spaces (when these are manifolds, which they are under freeness + properness). Equivariant maps are the smooth maps that "see only the orbit structure" — they treat each orbit of $M$ as a single object mapping to an orbit of $N$.

---

# Examples / Corollaries

**Is an instance: the orbit map.** For a smooth left action of $G$ on $M$ and $p \in M$, the orbit map $\theta^{(p)} : G \to M$, $g \mapsto g \cdot p$, is $G$-equivariant when $G$ acts on itself by left translation: $\theta^{(p)}(hg) = (hg) \cdot p = h \cdot (g \cdot p) = h \cdot \theta^{(p)}(g)$. Since the action of $G$ on itself by left translation is transitive, $\theta^{(p)}$ has constant rank by the equivariant rank theorem.

**Is an instance: a Lie group homomorphism.** A Lie group homomorphism $F : G \to H$ is $G$-equivariant when $G$ acts on itself by left translation and on $H$ via $F$ followed by left translation: $F(gg') = F(g) F(g')$ is exactly the equivariance condition. The constant-rank fact for Lie group homomorphisms (Lee Thm 7.5) is a special case of the equivariant rank theorem.

**Is an instance: the projection $\pi : \mathbb{R}^{n+1} \setminus \{0\} \to \mathbb{RP}^n$.** Under the natural action of $\mathbb{R}^\times$ on $\mathbb{R}^{n+1} \setminus \{0\}$ by scalar multiplication, and the trivial action on $\mathbb{RP}^n$, the projection $\pi(v) = [v]$ is equivariant ($\pi(\lambda v) = [\lambda v] = [v] = \pi(v) = \lambda \cdot \pi(v)$ where the last "$\lambda \cdot$" is the trivial action). It is a smooth submersion (by the equivariant rank theorem applied to a transitive action).

**Is an instance: the determinant $\det : \mathrm{GL}(n) \to \mathbb{R}^\times$.** Equivariant when $\mathrm{GL}(n)$ acts on itself by left translation and on $\mathbb{R}^\times$ via the determinant: $\det(AB) = \det(A) \det(B)$. The induced action of $\mathrm{GL}(n)$ on $\mathbb{R}^\times$ is $A \cdot t = \det(A) t$.

**Is NOT an instance: a map that breaks equivariance.** Take $F : \mathbb{R}^n \to \mathbb{R}^n$, $F(v) = v + e_1$ (translation by the first basis vector). This is smooth, and the natural action of $\mathrm{SO}(n)$ on $\mathbb{R}^n$ acts on both source and target. But $F(A v) = Av + e_1 \neq A(v + e_1) = A v + A e_1$ unless $A e_1 = e_1$, which happens only for $A$ in the stabilizer of $e_1$ in $\mathrm{SO}(n)$. So $F$ is *not* $\mathrm{SO}(n)$-equivariant (it is only $\mathrm{SO}(n)_{e_1}$-equivariant).

**Is NOT an instance: smooth bijection of two $G$-spaces with different actions.** Two manifolds may be diffeomorphic as smooth manifolds yet not isomorphic as $G$-spaces. For instance, $G = \mathbb{Z}/2$ acting on $S^1$ either trivially or by $z \mapsto z^{-1}$ gives two different $G$-structures on $S^1$; the identity map is *not* $G$-equivariant for these distinct actions.

**Corollary (constant rank).** Equivariant + transitive $G$-action on source ⟹ constant rank (Lee Thm 7.25).

**Corollary (image is a $G$-orbit).** If $F : M \to N$ is equivariant with $M$ a single $G$-orbit, then $F(M)$ is a single $G$-orbit in $N$. *Proof:* take $p \in M$; $F(M) = F(G \cdot p) = G \cdot F(p)$.

**Corollary (kernel of equivariant action).** If $F : G \to \mathrm{Diff}(M)$ is the homomorphism corresponding to an action, then $\ker F$ is a closed normal Lie subgroup of $G$ (closed by continuity, normal because it is the kernel of a homomorphism). The action descends to a faithful action of $G/\ker F$ on $M$. So every non-faithful action canonically factors through a faithful one.

**Corollary (induced map on orbit spaces).** If $F : M \to N$ is equivariant and the orbit spaces $M/G$, $N/G$ are smooth manifolds (e.g., the actions are free and proper), then $F$ descends to a smooth map $\bar F : M/G \to N/G$ on orbit spaces.

**Calibration check.** If you can (i) verify the orbit map is equivariant when $G$ acts on itself by left translation; (ii) state and apply the equivariant rank theorem; and (iii) explain why a Lie group homomorphism is automatically equivariant under appropriate left actions — you have understood the definition correctly.

---

# Unlocked by This

> [!tip] Equivariant Rank Theorem *(from this chapter)*
> An equivariant smooth map with transitive $G$-action on the source has **constant rank** (Lee Thm 7.25). This is the principal structural property of equivariant maps; it unlocks the [[Thm - The Rank Theorem|rank theorem]] and allows one to read off whether $F$ is an immersion, submersion, or embedding from a single-point calculation.

> [!tip] Equivariant Cohomology *(from Algebraic Topology, Advanced)*
> When $G$ acts on $M$, the **equivariant cohomology** $H^*_G(M)$ is defined as $H^*((M \times EG)/G)$ where $EG$ is a contractible $G$-space. Equivariant maps $F : M \to N$ induce pullbacks on equivariant cohomology, just as ordinary smooth maps do on ordinary cohomology. Equivariant cohomology is the principal tool for computing topology of fixed-point sets via localization theorems (Atiyah–Bott, Berline–Vergne).

> [!tip] Equivariant Bundles *(from Gauge Theory)*
> An **equivariant bundle** is a fibre bundle $E \to M$ over a $G$-manifold $M$ with a $G$-action on $E$ covering the action on $M$. Equivariant sections, equivariant connections, and equivariant characteristic classes are the natural objects in gauge theory and equivariant K-theory.
