---
type: theorem
subject: topology
prereqs:
  - "Def - Compact Space"
  - "Def - Separation Axioms"
  - "Def - Continuous Map"
tags: [analysis, topology, compactness, homeomorphism]
---

# Notation

$X, Y$ are topological spaces. $X$ is **compact** (see [[Def - Compact Space]]), $Y$ is **Hausdorff** (see [[Def - Separation Axioms]]). A map $f : X \to Y$ is a [[Def - Continuous Map|continuous]] function. $f$ is a **homeomorphism** if it is a continuous bijection with continuous inverse $f^{-1}$. A map $f$ is **closed** if $f(F)$ is closed in $Y$ for every closed $F \subseteq X$. The full registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Theorem.** Let $f : X \to Y$ be a continuous bijection. Suppose $X$ is **compact** and $Y$ is **Hausdorff**. Then $f$ is a **homeomorphism** — i.e., $f^{-1}$ is also continuous.

The proof is short: $f$ is automatically a *closed map* (the image of a closed subset of $X$ is compact in $X$ by [[Thm - Closed Subset of Compact is Compact]], hence compact in $Y$ by [[Thm - Continuous Image of a Compact Space]], hence closed in $Y$ by [[Thm - Compact Subset of Hausdorff is Closed]]). A continuous bijection that is also closed is a homeomorphism, because $f^{-1}$'s preimages of closed sets are exactly the images of closed sets under $f$.

---

# Motivation

The question this theorem answers is: *when is a continuous bijection automatically a homeomorphism*? In general, a continuous bijection need *not* be a homeomorphism. The standard counterexample is the unwinding map

$$f : [0, 2\pi) \to S^1, \quad f(t) = (\cos t, \sin t).$$

This is continuous (composition of continuous functions) and bijective (winds the half-open interval onto the circle exactly once). But $f^{-1} : S^1 \to [0, 2\pi)$ is *not* continuous: as $\theta \to 2\pi^-$ on the circle, the points $f(\theta)$ approach $f(0) = (1, 0)$, but $f^{-1}(f(\theta)) = \theta$ does not approach $f^{-1}(1, 0) = 0$. The issue: $[0, 2\pi)$ is *not compact* (missing the endpoint), so the compact-Hausdorff hypothesis pair is broken.

This counterexample is *exactly* what motivates the theorem. If one upgrades $[0, 2\pi)$ to $[0, 2\pi]$ (now compact) and identifies the endpoints (quotient by $0 \sim 2\pi$), the resulting map is a homeomorphism. The compactness hypothesis "closes the loop"; the Hausdorffness on the target side prevents pathologies in the image.

The pragmatic value of the theorem is enormous. It eliminates the need to verify continuity of the inverse in a vast class of identifications:

- Identifying a quotient of a compact space with another space: just need to check the map is a continuous bijection.
- Embedding theorems: a continuous bijection from a compact space to a Hausdorff space is automatically an embedding.
- Manifold theory: continuous bijections between compact manifolds are diffeomorphisms (once smoothness is added) provided the inverse is smooth, but continuity is automatic.
- Classification: when proving two compact Hausdorff spaces are homeomorphic, just exhibit any continuous bijection.

The theorem reveals the **rigidity of the compact-Hausdorff topology**. In the compact-Hausdorff world, every continuous bijection is a homeomorphism, every continuous map from compact-Hausdorff to Hausdorff is a closed map, and continuous bijections between compact Hausdorff spaces are automatically structure-preserving. This rigidity is what makes "compact + Hausdorff" the gold-standard hypothesis pair in topology.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f$ continuous bijection, $X$ compact, $Y$ Hausdorff".

The first disguised source is **$f$ is a quotient map from a compact space**. Property $B$: $X$ compact, $\sim$ an equivalence relation, $X/\sim$ a quotient space, and we want to identify $X/\sim$ with a known Hausdorff $Y$. The bridge: a continuous map $f : X/\sim \to Y$ inducing a bijection $X/\sim \cong Y$ is automatically a homeomorphism by this theorem (provided $X/\sim$ is compact, which it is as a continuous image of compact $X$). *Example:* $S^1 \cong [0, 1]/(0 \sim 1)$ is one of the most basic uses.

The second disguised source is **$f$ is a continuous bijection between two compact subsets of $\mathbb{R}^n$**. Property $B$: $X, Y$ both compact subsets of $\mathbb{R}^n$, with $\mathbb{R}^n$ Hausdorff. The bridge: $\mathbb{R}^n$ Hausdorff makes $Y$ Hausdorff, and the theorem applies. *Example:* every continuous bijection between compact subsets of Euclidean space is a homeomorphism — used constantly in topology of manifolds and CW complexes.

The third disguised source is **$f$ is the inclusion of a compact subspace into a Hausdorff space**, when one wants to compare topologies. Property $B$: $A \subseteq Y$ compact, $Y$ Hausdorff, and one has another topology $\tau$ on $A$ for which the inclusion $f : (A, \tau) \to Y$ is continuous. The bridge: if $(A, \tau)$ is compact (under $\tau$) and $f$ is bijective onto its image and continuous, then $\tau$ equals the subspace topology — a rigidity statement. *Example:* the compact-open topology on a function space is often the unique compact Hausdorff topology making evaluation continuous.

**Targets (Output Amplification)**

The conclusion is "$f$ is a homeomorphism".

Combine the conclusion with **a smooth structure**. Property $D$: $X, Y$ smooth manifolds, $f$ a smooth bijection. Amplified result $E$: $f$ is a diffeomorphism (given smooth inverse, which is automatic via inverse function theorem at each point if $df$ is everywhere invertible — but here we don't have differentiability of $f^{-1}$ for free; continuity is what we get from this theorem). *Example:* in algebraic geometry, a continuous bijection between compact complex varieties that is algebraic is automatically biholomorphic. This is a *much* stronger result, but the topological core is this theorem.

Combine the conclusion with **identification of structures via the homeomorphism**. Property $D$: the homeomorphism $f$. Amplified result $E$: $X$ and $Y$ have all the same topological invariants — Euler characteristic, fundamental group, homology, etc. *Example:* proving that all compact connected surfaces of genus $g$ are homeomorphic, once one exhibits a continuous bijection.

Combine the conclusion with **a sequence of identifications, transitively**. Property $D$: $X_0 \to X_1 \to X_2 \to \cdots$ a chain of continuous bijections between compact Hausdorff spaces. Amplified result $E$: all are mutually homeomorphic. *Example:* the classification of compact surfaces by genus, where each genus is exhibited as a compact Hausdorff space (the quotient of a polygon) and identifications are continuous bijections.

---

# Why Is It True

The theorem rests on the **closed-map property** of continuous maps from compact to Hausdorff. The argument has two pieces, each clean:

**Piece 1: $f$ is a closed map.** Let $F \subseteq X$ be closed. By [[Thm - Closed Subset of Compact is Compact]], $F$ is compact (closed subset of compact). By [[Thm - Continuous Image of a Compact Space]], $f(F) \subseteq Y$ is compact. By [[Thm - Compact Subset of Hausdorff is Closed]], $f(F)$ is closed in $Y$ (compact subset of Hausdorff). So $f$ sends closed sets to closed sets — $f$ is a closed map.

**Piece 2: A closed continuous bijection is a homeomorphism.** $f$ has an inverse $f^{-1} : Y \to X$ (bijectivity). To show $f^{-1}$ is continuous, check that preimages of closed sets under $f^{-1}$ are closed in $Y$. But $(f^{-1})^{-1}(F) = f(F)$ for $F \subseteq X$, so the preimage of a closed $F$ under $f^{-1}$ is $f(F)$, which is closed by Piece 1. Hence $f^{-1}$ is continuous, and $f$ is a homeomorphism.

The geometric picture: a continuous bijection is *almost* a homeomorphism — it preserves all the topology in one direction. The obstacle to being a full homeomorphism is that the *inverse* might fail to be continuous. The inverse failing to be continuous means: a closed set in $X$ has a non-closed image in $Y$ (some limit point is missed). Compactness of $X$ prevents this: closed sets in $X$ are compact, hence "small" enough that their images are also compact, hence closed in Hausdorff $Y$. So the compact-Hausdorff combination is exactly the structural condition that prevents the inverse from being discontinuous.

The role of Hausdorff on the *target*: it ensures that compact subsets of $Y$ are closed. Without Hausdorff, compact subsets of $Y$ need not be closed (in the cofinite topology, every set is compact, but most are not closed). So even though the image $f(F)$ is compact, it might fail to be closed in $Y$, breaking the closed-map property.

The role of compact on the *source*: it ensures closed subsets of $X$ are compact (every closed subset is the closure of itself, and closed-in-compact is compact). Without compactness of $X$, closed subsets of $X$ might not have compact images (e.g., $f : (0, 1) \to (0, 1)$ identity is a homeomorphism, but if we replaced $(0, 1)$ with $[0, 1)$ on the source and $S^1$ on the target via the unwinding map, the source not being compact breaks the closed-map property).

The combination is *tight* — both hypotheses are essential, and both work together via the chain "closed $\to$ compact $\to$ compact $\to$ closed".

---

# What Makes This Hard

The non-obvious step is the **closed-map chain**: closed $F \subseteq X$ → compact (by [[Thm - Closed Subset of Compact is Compact]]) → compact $f(F) \subseteq Y$ (by [[Thm - Continuous Image of a Compact Space]]) → closed $f(F) \subseteq Y$ (by [[Thm - Compact Subset of Hausdorff is Closed]]). Each step uses a different compactness theorem, and assembling the chain is the trick. The most common error is to forget one of the two hypotheses — to apply the theorem with non-compact $X$ (giving the $[0, 2\pi) \to S^1$ counterexample) or non-Hausdorff $Y$ (where compact images need not be closed). A second pitfall is to confuse "closed map" with "continuous map" — they are different conditions, and the closed-map condition is what gives continuity of $f^{-1}$.

---

# Rederivation Scaffold

**High-level strategy:**
Show $f$ is a closed map: closed in $X$ → compact in $X$ → compact in $Y$ → closed in $Y$. A closed continuous bijection has continuous inverse: preimage of closed under $f^{-1}$ is image of closed under $f$, which is closed.

**Subgoal decomposition:**

1. **Closed in $X$ ⇒ compact in $X$.** By [[Thm - Closed Subset of Compact is Compact]] applied to compact $X$.
   - *Hint:* Direct citation.

2. **Continuous image of compact is compact.** By [[Thm - Continuous Image of a Compact Space]] applied to $f$ continuous and the compact closed subset.

3. **Compact in Hausdorff $Y$ ⇒ closed in $Y$.** By [[Thm - Compact Subset of Hausdorff is Closed]] applied to Hausdorff $Y$.

4. **Hence $f$ is a closed map.** Combining 1–3.

5. **Closed continuous bijection ⇒ continuous inverse.** Preimages of closed under $f^{-1}$ are images of closed under $f$, which are closed by the closed-map property.

---

# Lemma Decomposition

> [!note]- Lemma 1: $f$ continuous, $X$ compact, $Y$ Hausdorff ⇒ $f$ is a closed map
> **Statement:** Let $f : X \to Y$ be continuous, $X$ compact, $Y$ Hausdorff. Then for every closed $F \subseteq X$, $f(F)$ is closed in $Y$.
>
> **Hint:** Closed $F$ in compact $X$ ⇒ $F$ compact; image $f(F)$ is compact (continuous image); compact in Hausdorff is closed.
>
> **Why needed:** It is the heart of the theorem.
>
> > [!note]- Full proof
> > Let $F \subseteq X$ be closed. By [[Thm - Closed Subset of Compact is Compact]], $F$ is compact (closed subset of compact $X$).
> >
> > By [[Thm - Continuous Image of a Compact Space]], $f(F) \subseteq Y$ is compact (continuous image of compact $F$).
> >
> > By [[Thm - Compact Subset of Hausdorff is Closed]], $f(F)$ is closed in $Y$ (compact subset of Hausdorff $Y$).
> >
> > So $f$ takes closed sets to closed sets, i.e., $f$ is a closed map.

> [!note]- Lemma 2: A closed continuous bijection has continuous inverse
> **Statement:** Let $f : X \to Y$ be a continuous bijection and a closed map. Then $f^{-1} : Y \to X$ is continuous.
>
> **Hint:** For continuity of $g = f^{-1}$, check preimages of closed sets are closed. $g^{-1}(F) = f(F)$.
>
> **Why needed:** It is the conclusion.
>
> > [!note]- Full proof
> > Let $g = f^{-1}$. We show preimages of closed sets under $g$ are closed in $Y$.
> >
> > For any closed $F \subseteq X$:
> > $$g^{-1}(F) = \{y \in Y : g(y) \in F\} = \{y \in Y : f^{-1}(y) \in F\} = \{y \in Y : y \in f(F)\} = f(F).$$
> > (Using bijectivity of $f$: $f^{-1}(y) \in F \iff y \in f(F)$.)
> >
> > By hypothesis $f$ is a closed map, so $f(F)$ is closed in $Y$. Hence $g^{-1}(F)$ is closed for every closed $F$, i.e., $g$ is continuous.

---

# Formal Proof

> [!note]- Complete formal proof
>
> Let $f : X \to Y$ be a continuous bijection with $X$ compact and $Y$ Hausdorff.
>
> By Lemma 1, $f$ is a closed map: $f(F)$ is closed in $Y$ for every closed $F \subseteq X$.
>
> By Lemma 2, $f^{-1} : Y \to X$ is continuous.
>
> Together with the continuity of $f$ and the bijectivity, $f$ is a homeomorphism. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**$S^1 \cong [0, 1]/(0 \sim 1)$.** Define $f : [0, 1]/(0 \sim 1) \to S^1$ by $f([t]) = (\cos 2\pi t, \sin 2\pi t)$. This is well-defined (because $f(0) = f(1)$), continuous (induced by a continuous map on $[0, 1]$ via the universal property of the quotient), and bijective. $[0, 1]/(0 \sim 1)$ is compact (quotient of compact). $S^1$ is Hausdorff (subspace of $\mathbb{R}^2$). By this theorem, $f$ is a homeomorphism. The application makes the abstract identification concrete and rigorous — no need to verify continuity of $f^{-1}$ explicitly.

**Why $[0, 2\pi) \to S^1$ fails.** The unwinding map is continuous and bijective, but $[0, 2\pi)$ is *not compact* (missing endpoint $2\pi$). By this theorem's contrapositive, the failure of homeomorphism implies one of the hypotheses fails — and indeed compactness of the source fails. This counterexample is the textbook illustration of why compactness is essential, and is the canonical motivator for the theorem.

**Classification of compact surfaces.** Every compact connected surface is homeomorphic to either the sphere $S^2$, a connected sum of tori $T^2 \# \cdots \# T^2$ (genus-$g$ orientable surface), or a connected sum of projective planes $\mathbb{RP}^2 \# \cdots \# \mathbb{RP}^2$ (non-orientable). The proof exhibits each topology type as a quotient of a polygon by edge identifications. The continuous bijection between the polygon-quotient and the standard surface representation is verified by hand; this theorem makes it a homeomorphism, completing the classification.

**Compact subgroups of Lie groups.** A compact subgroup of a Lie group $G$ is closed. Conversely, a closed bounded subgroup of $\mathrm{GL}_n(\mathbb{R})$ is compact (by [[Thm - Heine–Borel Theorem|Heine–Borel]]). The continuous bijection between an abstract compact group and its representation in some $\mathrm{GL}_n$ — if one exists — is automatically a homeomorphism by this theorem (since $\mathrm{GL}_n(\mathbb{R})$ is Hausdorff). This is the topological foundation of Peter–Weyl theory and the representation theory of compact groups.

---

# Bridges

- **[[Thm - Closed Subset of Compact is Compact]]** — supplies "closed in $X$ ⇒ compact in $X$".

- **[[Thm - Continuous Image of a Compact Space]]** — supplies "compact in $X$ + continuous $f$ ⇒ compact in $Y$".

- **[[Thm - Compact Subset of Hausdorff is Closed]]** — supplies "compact in Hausdorff $Y$ ⇒ closed in $Y$".

- **The closed-map property of continuous compact-to-Hausdorff maps** — explicitly stated, is one direction of the theorem.

- **The unwinding map $[0, 2\pi) \to S^1$** — the canonical counterexample showing both hypotheses are essential.

- **Quotient topology** — many concrete homeomorphisms arise as quotient maps from compact spaces. This theorem justifies "the quotient is the space we expect" once a continuous bijection is exhibited.

---

# Unlocked by This

> [!tip] **Classification of Compact Surfaces** *(from Algebraic Topology)*
> Every compact connected surface is homeomorphic to a specific model (sphere, genus-$g$ surface, or non-orientable surface). This theorem makes the polygon-edge-identification realizations homeomorphic to the surface models without further continuity verification.

> [!tip] **Peter–Weyl Theorem** *(from Representation Theory)*
> Every compact Hausdorff topological group has a faithful finite-dimensional unitary representation, and the matrix entries of all irreducible representations span a dense subspace of $C(G)$. This theorem is used at the level of continuous bijections to identify compact groups with subgroups of unitary groups.

> [!tip] **Cellular Approximation in CW Complexes** *(from Algebraic Topology)*
> Continuous maps between CW complexes can be approximated by cellular maps. The construction uses this theorem at each cell: continuous bijections between compact CW pairs are homeomorphisms, and the cellular replacement is built piece by piece.

> [!tip] **Stone Duality** *(from Category Theory)*
> The category of compact Hausdorff spaces is dual to a category of algebraic structures (commutative C*-algebras for Gelfand–Naimark, Stone Boolean algebras for Stone duality). The rigidity of compact Hausdorff topology (this theorem) is what makes the duality work: continuous bijections in one category correspond to isomorphisms in the dual.
