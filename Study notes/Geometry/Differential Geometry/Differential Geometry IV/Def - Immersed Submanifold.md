---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - Immersion, Submersion, and Embedding"
  - "Def - Embedded Submanifold"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold; $S \subseteq M$ is a subset. We will give $S$ its own topology and smooth structure, not necessarily the subspace topology from $M$. The inclusion $\iota : S \hookrightarrow M$ is then a smooth map, but possibly only an *immersion*, not an *embedding*. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

---

# Axiom Motivation

The [[Def - Embedded Submanifold|embedded submanifold]] notion is the clean one: subspace topology, unique smooth structure, slice charts. But for certain natural constructions — Lie subgroups, foliations, integral submanifolds of distributions, the image of a non-injective immersion's restriction to an injectivity neighbourhood — the natural object cannot be described in the embedded-submanifold framework, and a strict generalisation is needed.

The motivating example is the **irrational line on the torus**. For irrational $\alpha \in \mathbb{R}$, the map $\gamma : \mathbb{R} \to T^2 = S^1 \times S^1$ defined by $\gamma(t) = (e^{2\pi i t}, e^{2\pi i \alpha t})$ is a smooth injective immersion. Its image $S = \gamma(\mathbb{R})$ is *dense* in $T^2$ (by Weyl equidistribution or Dirichlet's approximation theorem). In the subspace topology from $T^2$, the image $S$ is not locally Euclidean — every neighbourhood of any point in $S$ contains infinitely many "wraps" of $\gamma$, which are not connected in $S$. So $S$ is not an embedded submanifold of $T^2$.

But $S$ is naturally a smooth $1$-manifold: it is the image of $\gamma$, and we can give it the topology and smooth structure that *makes $\gamma$ a diffeomorphism onto $S$*. This means $S$ has the topology of $\mathbb{R}$ (not the subspace topology from $T^2$), and a single global chart $\gamma^{-1} : S \to \mathbb{R}$. With this structure $S$ is a smooth $1$-manifold, the inclusion $\iota : S \hookrightarrow T^2$ is the composition $\gamma \circ \gamma^{-1}$ which is a smooth immersion, and we have all the differential-geometric structure we want — but the topology on $S$ is the *domain* topology pulled across by $\gamma$, not the subspace topology.

This is the immersed submanifold idea: **take a subset, equip it with its own topology and smooth structure, and require only that the inclusion into the ambient manifold be a smooth immersion**. The topology may differ from the subspace topology; this is the price of admitting examples like the irrational line on the torus.

What's preserved: tangent spaces, differentials, smoothness of compositions, the local-immersion-implies-locally-embedded property (every immersed submanifold is *locally* an embedded submanifold). What's lost: uniqueness of the topology and smooth structure. A given subset $S \subseteq M$ can admit *multiple* immersed-submanifold structures with different domain topologies — the figure-eight image set admits an immersed structure as the image of the standard figure-eight parametrisation $\beta$, but also other immersed structures coming from other parametrisations.

The condition that the inclusion be a smooth immersion (rather than merely a smooth map) is exactly what makes the tangent-space identification work. The differential $d\iota_p : T_p S \to T_p M$ must be injective so that $T_p S$ can be identified with a subspace of $T_p M$; otherwise the tangent-space inclusion would collapse some directions and the differential structure on $S$ would be incompatible with that on $M$.

What if we tried to drop the immersion condition? Then we'd admit "submanifolds" whose tangent spaces do not embed cleanly into the ambient tangent space — for instance the inclusion of the $x$-axis into $\mathbb{R}^2$ with the alternative smooth structure given by $t \mapsto t^3$. The map $t \mapsto (t^3, 0)$ is smooth and injective, but its derivative at $0$ is zero, so it is not an immersion; the "submanifold" structure on the $x$-axis it induces is incompatible with the ambient. We exclude such bad cases by requiring immersion.

What if we tried to strengthen by requiring the inclusion to be an *injection* (just on points, not on tangent vectors)? This is what "immersed submanifold" already encodes when we require $\iota$ to be injective. But injectivity on points alone is too weak — the inclusion of the cusped curve $\{y^3 = x^2\}$ via $t \mapsto (t^3, t^2)$ is injective on points but not an immersion at $t = 0$. We need both — immersion (tangent-space injectivity) and injectivity on points (set-level injectivity) — to get the clean notion. Some texts call the result an "injective immersion" rather than "immersed submanifold", because the latter is sometimes used more generally for non-injective immersions.

---

# The Definition

Let $M$ be a smooth manifold.

**Immersed submanifold.** A subset $S \subseteq M$ together with a choice of topology and smooth structure on $S$ is an **immersed submanifold** of $M$ if, with the given structure, $S$ is itself a smooth manifold and the inclusion map $\iota : S \hookrightarrow M$ is a smooth immersion.

Note that:
- The topology on $S$ need not be the subspace topology from $M$.
- The smooth structure on $S$ need not be unique — different immersed structures may exist on the same set.
- The inclusion is automatically injective (since $S \subseteq M$ as a set), but may fail to be a topological embedding (i.e., a homeomorphism onto its image in the subspace topology of $M$).

**Equivalent characterisation.** A set with topology and smooth structure $(S, \tau, \mathcal{A})$ is an immersed submanifold of $M$ if and only if it is the image of an injective smooth immersion $F : N \to M$ from some abstract smooth manifold $N$, equipped with the topology and smooth structure pushed forward by $F$ (declaring $F$ to be a homeomorphism, hence a diffeomorphism, onto $S$).

**Local embedding.** Every immersed submanifold is **locally embedded**: for each $p \in S$ there is a neighbourhood $U$ of $p$ in $S$ (in the domain topology of $S$) such that $\iota|_U : U \hookrightarrow M$ is a smooth embedding. So $S$ looks locally like an embedded submanifold, but globally may twist (figure-eight) or fold densely (irrational line on torus).

**Smooth structure given topology.** If a topology $\tau$ on $S$ is given making it an immersed submanifold of $M$, then the smooth structure on $S$ compatible with $\tau$ is unique.

**Weakly embedded submanifold.** An immersed submanifold $S \subseteq M$ is **weakly embedded** (or **initial**) if every smooth map $F : N \to M$ whose image lies in $S$ is automatically smooth as a map $F : N \to S$ (in the topology of $S$). Embedded submanifolds are weakly embedded; the figure-eight is not; the irrational line on the torus *is* weakly embedded despite not being embedded.

---

# Relate to Other Fields / Compression

The immersed-submanifold notion is the **strict generalisation** of embedded submanifold needed to capture examples that are smooth manifolds in their own right but whose topology disagrees with the ambient subspace topology. The relationship:

$$\text{embedded submanifold} \subset \text{immersed submanifold} \subset \text{image of a smooth immersion}$$

Each containment is strict: embedded ⊊ immersed (figure-eight, irrational line); and "image of an immersion" includes images of *non-injective* immersions (self-crossing curves), which are not considered submanifolds in our convention.

In **Lie theory**, immersed submanifolds are essential: Lie subgroups that are not closed (such as the irrational line as a subgroup of $T^2$) are immersed but not embedded. The closed-subgroup theorem identifies exactly when an immersed Lie subgroup is embedded — namely, when the subgroup is closed.

In **foliation theory**, the leaves of a foliation are immersed submanifolds — locally they are embedded (slice-like), but globally they can be dense or have non-trivial topology.

**True name:** the **true name** of "immersed submanifold" is **"image of an injective smooth immersion, with the pulled-back topology"**. This captures the operational content: you produce an immersed submanifold by exhibiting an injective immersion and pulling its domain's topology to the image. The "abstract" definition (a subset with topology and smooth structure making the inclusion an immersion) is logically primary but operationally derived from the image-of-immersion construction.

---

# Examples / Corollaries

**Is an instance — every embedded submanifold.** Every embedded submanifold is automatically an immersed submanifold, with the subspace topology and the inherited smooth structure. The immersion condition follows from the embedding condition.

**Is an instance — the figure-eight image set.** The image of $\beta(t) = (\sin 2t, \sin t)$ on $(-\pi, \pi) \to \mathbb{R}^2$, equipped with the topology and smooth structure making $\beta$ a diffeomorphism onto the image, is an immersed (but not embedded) submanifold of $\mathbb{R}^2$. The inclusion is a smooth injective immersion, but not a topological embedding because the subspace topology on the image has more open sets than the pulled-back topology. See [[Ex - The Figure-Eight Immersion]].

**Is an instance — the irrational line on the torus.** For irrational $\alpha$, the image of $\gamma(t) = (e^{2\pi i t}, e^{2\pi i \alpha t})$ on $\mathbb{R} \to T^2$ is an immersed submanifold of $T^2$ with the topology of $\mathbb{R}$. It is *dense* in $T^2$ and not locally closed, but as an immersed $1$-manifold it is diffeomorphic to $\mathbb{R}$. Remarkably, this is a *weakly embedded* immersed submanifold despite not being embedded.

**Is an instance — the image of an injective immersion of any manifold.** For any injective smooth immersion $F : N \to M$, the image $F(N) \subseteq M$ with the topology and smooth structure pushed forward by $F$ is an immersed submanifold of $M$, diffeomorphic to $N$ via $F$. This is the standard way of constructing immersed submanifolds.

**Is NOT an immersed submanifold structure — the figure-eight with the subspace topology.** If we equip the figure-eight image set with the subspace topology from $\mathbb{R}^2$, the resulting space is not a topological manifold (the crossing point has no Euclidean neighbourhood). So there is no smooth structure compatible with this topology making the inclusion an immersion. The valid immersed-submanifold structures come from parametrisations, which give different topologies.

**Is NOT an immersed submanifold structure — the $x$-axis with $\mathbb{R}$ via $t \mapsto t^3$.** The map $\phi : \mathbb{R} \to \mathbb{R}^2$, $\phi(t) = (t^3, 0)$, is smooth and injective, but not an immersion (derivative vanishes at $0$). So the smooth structure on the $x$-axis induced by $\phi^{-1}$ does not make the inclusion an immersion. The valid immersed structure on the $x$-axis comes from $t \mapsto (t, 0)$, giving the standard smooth structure.

**Corollary — image of an injective immersion is canonically an immersed submanifold.** Given $F : N \to M$ an injective smooth immersion, the image $F(N)$ has a unique topology and smooth structure as an immersed submanifold, namely the one making $F$ a diffeomorphism onto its image.

**Corollary — uniqueness of smooth structure given topology.** If two smooth structures on a set $S$ both make the inclusion into $M$ a smooth immersion *and* both induce the same topology on $S$, then the smooth structures agree. (The topology, however, can vary across different immersed-submanifold structures.)

**Corollary — locally embedded.** Every immersed submanifold $S \subseteq M$, around every point $p \in S$, has a neighbourhood $U \subseteq S$ (in the domain topology of $S$) on which the inclusion is a smooth embedding. So $S$ is "embedded near each point" — only the global topology can fail.

**Calibration check.** Verify that every embedded submanifold is immersed, but not conversely. Verify that the figure-eight image set is an immersed but not embedded submanifold of $\mathbb{R}^2$ — by exhibiting the topology that makes the parametrisation a diffeomorphism, and showing this topology differs from the subspace topology (in the subspace topology the crossing point is a limit of two sequences from the domain that do not have a common limit in the domain). Verify that the figure-eight image set is not weakly embedded by exhibiting a smooth map from $\mathbb{R}$ to $\mathbb{R}^2$ whose image lies in the figure-eight but which is not continuous as a map into the figure-eight with its immersed-submanifold topology.

---

# Unlocked by This

> [!tip] Lie Subgroups (non-closed) *(from [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie Theory]])*
> A subgroup $H$ of a Lie group $G$ that is also an immersed submanifold (compatibly with the group operations) is a **Lie subgroup**. Non-closed Lie subgroups — like the irrational line on the torus — are immersed but not embedded. The closed-subgroup theorem (Cartan) says closed subgroups are automatically embedded.

> [!tip] Leaves of Foliations *(from Differential Geometry / Dynamical Systems)*
> A **foliation** of $M$ is a decomposition of $M$ into disjoint immersed submanifolds (the leaves), locally diffeomorphic to a stack of parallel slices. The leaves are generically not embedded — they can be dense, as in the foliation of $T^2$ by lines of irrational slope. The Frobenius theorem in [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]] characterises when a distribution integrates to a foliation.

> [!tip] Integral Submanifolds of Distributions *(from Differential Geometry)*
> Given a smooth distribution $D \subseteq TM$ (a smooth choice of subspace $D_p \subseteq T_p M$ at each point), an **integral submanifold** of $D$ is an immersed submanifold $S$ with $T_p S = D_p$ at every $p$. Maximal integral submanifolds are the leaves of an associated foliation when $D$ is involutive.

> [!tip] Weakly Embedded vs Embedded *(from this topic)*
> The dichotomy between weakly embedded and merely immersed is precisely the dichotomy between "the smooth structure is unique even though the embedding fails" and "multiple smooth structures are possible". Lie subgroups are always weakly embedded, even when not embedded.
