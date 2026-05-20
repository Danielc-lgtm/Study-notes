---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
  - "Def - Subspace Topology"
tags: [analysis, topology]
---

# Notation

Let $\{X_\alpha\}_{\alpha \in A}$ be a family of topological spaces. The disjoint union is written $\bigsqcup_{\alpha \in A} X_\alpha$ or, for two spaces, $X \sqcup Y$. We use $\iota_\alpha : X_\alpha \hookrightarrow \bigsqcup_\beta X_\beta$ for the canonical inclusion. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Axiom Motivation

We are given a family of topological spaces $\{X_\alpha\}$ and want to combine them into a single space that holds them side-by-side, with no interaction. The set-theoretic operation is the disjoint union — take the points of every $X_\alpha$, tagging them by their index of origin so that copies of the same point in different factors are distinguished. The question is what topology to put on the resulting set.

The guiding principle, as with the product, is a universal property — but this time the *dual* one. The product was characterized by maps *into* it (a map $Z \to \prod_\alpha X_\alpha$ is determined by its coordinates, one map per factor). The disjoint union should be characterized by maps *out of* it: a map $f : \bigsqcup_\alpha X_\alpha \to Y$ should be specified by giving a map $f_\alpha : X_\alpha \to Y$ on each factor, with no compatibility requirement (since the factors are disjoint). And the topology on the disjoint union should make $f$ continuous if and only if each $f_\alpha$ is.

That requirement forces the topology in the opposite direction from the product. To make every $f_\alpha = f \circ \iota_\alpha$ continuous it is necessary that each $\iota_\alpha$ be continuous, so the topology must be at least fine enough that $\iota_\alpha^{-1}$ of every open in $\bigsqcup X_\alpha$ is open in $X_\alpha$. We could make the topology even finer, but the universal property prefers the *finest* topology making each $\iota_\alpha$ continuous: in this topology, a set $U \subseteq \bigsqcup X_\alpha$ is open exactly when $\iota_\alpha^{-1}(U)$ is open in $X_\alpha$ for every $\alpha$. Equivalently, an open set is a union of open subsets of the factors. This is the topology that is "as fine as possible" without breaking the continuity of inclusions, and it makes the universal property work cleanly.

Why does the asymmetry — *coarsest* for product, *finest* for disjoint union — make sense? Because the product is *built from the outside in*: the projections $\pi_\alpha$ go from the product to the factors, and you want them continuous, so the topology must be coarse enough not to make any $\pi_\alpha$ discontinuous. The disjoint union is *built from the inside out*: the inclusions $\iota_\alpha$ go from factors to the union, and you want them continuous, but you also want each $X_\alpha$ to embed as an *open* subspace — this requires the finest topology. The duality between "limit constructions" (coarsest, universal in) and "colimit constructions" (finest, universal out) is one of the central organizing principles of topology.

Strengthening or weakening the definition. If we made the topology coarser — say, only declare the union $\bigcup_\alpha X_\alpha$ open without insisting that each $X_\alpha \times \{\alpha\}$ be open — we would lose the property that each factor embeds as an open subspace, and the universal property would fail. If we made it finer — say, declare every singleton open — we get the discrete topology, which destroys the topology on each factor. The finest topology *making each inclusion continuous* is the unique sweet spot.

---

# The Definition

Let $\{X_\alpha\}_{\alpha \in A}$ be a family of topological spaces. The **disjoint union** (or **topological sum**) is the set

$$\bigsqcup_{\alpha \in A} X_\alpha = \bigcup_{\alpha \in A} X_\alpha \times \{\alpha\}$$

with the topology in which $U \subseteq \bigsqcup_\alpha X_\alpha$ is **open** if and only if $\iota_\alpha^{-1}(U) = \{x \in X_\alpha : (x, \alpha) \in U\}$ is open in $X_\alpha$ for every $\alpha \in A$.

Equivalently: the open sets are exactly the unions $\bigcup_\alpha U_\alpha \times \{\alpha\}$ where each $U_\alpha \subseteq X_\alpha$ is open. Equivalently again, this is the **finest topology** making every canonical inclusion $\iota_\alpha : X_\alpha \to \bigsqcup_\beta X_\beta$, $x \mapsto (x, \alpha)$, continuous.

In this topology, each $X_\alpha \times \{\alpha\}$ is **clopen** (both open and closed), and the inclusion $\iota_\alpha$ is a homeomorphism onto its image.

The **universal property** characterizes it: for any topological space $Y$ and any family of continuous maps $\{f_\alpha : X_\alpha \to Y\}$, there is a *unique* continuous map $f : \bigsqcup_\alpha X_\alpha \to Y$ with $f \circ \iota_\alpha = f_\alpha$, namely $f((x, \alpha)) = f_\alpha(x)$. Equivalently, $f : \bigsqcup_\alpha X_\alpha \to Y$ is continuous if and only if $f|_{X_\alpha \times \{\alpha\}}$ is continuous for every $\alpha$.

---

# Categorical Definition

The disjoint union is the **coproduct** in the category of topological spaces, dual to the product. A coproduct of a family $\{X_\alpha\}$ is an object $C$ with morphisms $\iota_\alpha : X_\alpha \to C$ such that for any object $Y$ and family of morphisms $\{f_\alpha : X_\alpha \to Y\}$, there is a unique morphism $f : C \to Y$ with $f \circ \iota_\alpha = f_\alpha$.

The set $\bigsqcup_\alpha X_\alpha$ with its topology and inclusions satisfies this universal property in topological spaces, and up to homeomorphism this characterizes it. Replacing "morphisms" with "continuous maps" and "object" with "topological space" recovers the concrete construction.

The general pattern: in any category, the coproduct is universal for *maps out*; the product is universal for *maps in*. In sets, the coproduct is set-theoretic disjoint union; in abelian groups, the direct sum (which coincides with the product for finite families but not infinite); in commutative rings, the tensor product. The topological case is the most straightforward — set-theoretic disjoint union with the natural topology.

---

# Relate to Other Fields / Compression

In **group theory**, the coproduct in the category of *groups* is the **free product** $G * H$, not the disjoint union of underlying sets — the coproduct depends sensitively on the category. In **abelian groups**, the coproduct is the direct sum $G \oplus H$, which coincides with the categorical product for finitely many factors but not for infinitely many: $\bigoplus_n A_n$ consists of *finitely supported* tuples, while $\prod_n A_n$ has no such restriction.

In **topology**, by contrast, the coproduct and product look very different even for two factors: $X \times Y$ versus $X \sqcup Y$. The disjoint union loses all topological connection between factors; the product preserves every coordinate's structure independently while binding them via the projection maps.

In **measure theory**, the disjoint union of measure spaces — $(\bigsqcup_\alpha X_\alpha, \bigsqcup_\alpha \mathcal{F}_\alpha, \mu = \sum_\alpha \mu_\alpha)$ — is the natural construction for combining measure spaces, and it is the measure-theoretic coproduct.

In **algebraic topology**, the disjoint union is what one uses to build CW complexes by attaching cells one at a time — each cell is a copy of a disk, and the CW complex is built by taking disjoint unions and identifying boundaries via attaching maps. The disjoint union is the *raw material*; attaching maps then glue parts together via quotients.

---

# Examples / Corollaries

**Is an instance — two real lines side by side.** $\mathbb{R} \sqcup \mathbb{R}$ has two connected components, each homeomorphic to $\mathbb{R}$, with no points in common. As a topological space it is *not* homeomorphic to $\mathbb{R}$ (which is connected) or to $\mathbb{R}^2$ (which is connected and 2-dimensional). It is homeomorphic to $\mathbb{R} \times \{0, 1\}$ with the discrete topology on $\{0, 1\}$ — a useful reformulation.

**Is an instance — the integers as a disjoint union of points.** $\mathbb{Z}$ with the discrete topology is the disjoint union $\bigsqcup_{n \in \mathbb{Z}} \{n\}$ of singleton spaces. Every subset is open. This is a special case where each factor is a one-point space.

**Is NOT an instance — the union of two overlapping intervals in $\mathbb{R}$.** The set $(0, 2) \cup (1, 3) \subseteq \mathbb{R}$ is *not* the disjoint union of $(0, 2)$ and $(1, 3)$ as topological spaces. In the disjoint union, the two intervals are clopen and disconnected; as subspaces of $\mathbb{R}$, they overlap in $(1, 2)$ and the union is connected. The disjoint union "remembers" the disjointness even if the factor spaces happen to share points abstractly.

**Corollary — connected components.** The connected components of $\bigsqcup_\alpha X_\alpha$ are exactly the connected components of the $X_\alpha$ (one per factor, if each $X_\alpha$ is connected, in which case the components are the $X_\alpha$ themselves). The disjoint union always has at least as many components as factors.

**Corollary — compactness and disjoint unions.** $\bigsqcup_\alpha X_\alpha$ is compact if and only if each $X_\alpha$ is compact *and* the index set $A$ is finite. The infinite disjoint union of nonempty spaces is never compact, because the family $\{X_\alpha \times \{\alpha\}\}_\alpha$ is an open cover with no finite subcover.

**Corollary — Hausdorff is preserved.** $\bigsqcup_\alpha X_\alpha$ is Hausdorff if and only if each $X_\alpha$ is. Two points in the same factor are separated within that factor; two points in different factors are separated by the clopen factors themselves.

**Calibration check.** Verify: (i) $\mathbb{R} \sqcup \mathbb{R}$ is not homeomorphic to $\mathbb{R}$ (count components); (ii) the map from $\mathbb{R} \sqcup \mathbb{R}$ to $\mathbb{R}$ sending both copies via $x \mapsto x$ is continuous and surjective but not injective — the universal property gives continuity, the disjointness gives non-injectivity; (iii) every continuous map $f : X \sqcup Y \to Z$ is determined by its restrictions $f|_X$ and $f|_Y$; (iv) if $X$ has $n$ connected components, $X$ is homeomorphic to the disjoint union of its components.

---

# Unlocked by This

> [!tip] Coproduct in Other Categories *(from Category Theory)*
> The disjoint union is the prototype of a **coproduct**. In abelian groups, the coproduct is the direct sum; in groups, the free product; in commutative rings, the tensor product. Recognizing the coproduct structure unifies these constructions as instances of the same universal property.

> [!tip] CW Complexes *(from Algebraic Topology)*
> A **CW complex** is built by attaching cells to a space via maps from the boundary of a disk. The construction takes disjoint unions of disks and identifies boundary points — disjoint union is the raw material, quotient by attaching maps gives the final space.
