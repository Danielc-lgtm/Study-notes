---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
  - "Def - Product Topology"
  - "Def - Separation Axioms"
tags: [analysis, topology, group, topological-group]
---

# Notation

$G$ a topological group, $e$ or $1$ the identity. $\mu : G \times G \to G$ the multiplication, $\iota : G \to G$ the inversion. $L_g(h) = gh$ left translation by $g$; $R_g(h) = hg^{-1}$ right translation by $g$ (Bredon's convention, so $R_e = 1_G$). For subsets $A, B \subseteq G$: $AB = \{ab : a \in A, b \in B\}$, $A^{-1} = \{a^{-1} : a \in A\}$. A subset $A$ is **symmetric** if $A = A^{-1}$. The full registry is on the topic page.

---

# Axiom Motivation

A topological group is a single object wearing two hats: it is a *space* (with continuity) and a *group* (with multiplication and inversion). The axioms demand that these two structures *cooperate* — the algebraic operations must be continuous as maps of topological spaces. This is the right thing to demand: without continuity of multiplication and inversion, the algebra and the topology would be irrelevant to one another, and the combined object would have no more structure than its pieces. With continuity, the topology becomes *homogeneous* (every point looks like every other, via translation) and the algebra becomes *robust* (small perturbations of group elements multiply to small perturbations of products).

Why insist on *joint* continuity of multiplication $\mu : G \times G \to G$ — continuity as a map on the product space $G \times G$ — rather than just separate continuity in each variable? Because separate continuity is much weaker: a multiplication continuous in each variable separately could fail to be continuous in both at once, and we would lose almost all useful properties. The product topology on $G \times G$ is the right object, and joint continuity at $(g, h)$ means: for every open $W \ni gh$, there are opens $U \ni g, V \ni h$ with $UV \subseteq W$.

Continuity of inversion $\iota : G \to G$ is a separate axiom: it does not follow from joint continuity of multiplication (the inversion in $\operatorname{GL}_n(\mathbb{R})$, given by Cramer's rule, requires its own argument). In some references, the two axioms can be combined: "the map $(g, h) \mapsto gh^{-1}$ is continuous" implies both, since $\iota = (g, h) \mapsto gh^{-1}$ specialized to $g = e$, and $\mu$ recovers from this by first inverting the second argument and then applying. Bredon keeps them separate for clarity.

Why does Bredon require Hausdorff as part of the definition? In some textbooks, "topological group" means just (continuous multiplication + continuous inversion + group structure), and Hausdorff is a separate (often automatic) hypothesis. Bredon includes Hausdorff because most useful theorems require it, and excluding non-Hausdorff cases simplifies the statements. Importantly, if the topological group is $T_0$ (every two distinct points distinguishable by some open set), then it is automatically Hausdorff by homogeneity: translate the separating open sets. So requiring Hausdorff is essentially requiring $T_0$, which is the minimal separation axiom.

If we *weaken* by dropping continuity of inversion, we get a "topological semigroup with identity"; if we *weaken* by dropping joint continuity of multiplication, we get a much less structured object where the algebra and the topology don't interact. If we *strengthen* by requiring multiplication and inversion to be smooth (and $G$ to be a manifold), we get a **Lie group** — the central object of differential geometry and continuous symmetry.

The most important consequence of the axioms: **translations are homeomorphisms**. For each $g$, $L_g$ is continuous (being multiplication by $g$, which is continuous in the second variable as a corollary of joint continuity), and its inverse $L_{g^{-1}}$ is also continuous. So $L_g$ is a homeomorphism. Translation by $g$ maps neighborhoods of $h$ to neighborhoods of $gh$, so the topology near $h$ is identical to the topology near $gh$ — the topological group is **homogeneous**.

---

# The Definition

A **topological group** is a triple $(G, \tau, \mu)$ consisting of:

1. A set $G$;
2. A topology $\tau$ on $G$ making $(G, \tau)$ a **Hausdorff** topological space;
3. A group structure on $G$ — i.e., an associative binary operation $\mu : G \times G \to G$, $(g, h) \mapsto gh$, with identity $e$ and inverses $g \mapsto g^{-1}$;

such that:

- **Multiplication is continuous:** $\mu : G \times G \to G$ is continuous as a map from the product space $G \times G$ (with product topology) to $G$.
- **Inversion is continuous:** $\iota : G \to G$, $g \mapsto g^{-1}$, is continuous.

---

# Relate to Other Fields / Compression

A topological group is the **group object in the category of topological spaces**: an internal group structure in $\mathbf{Top}$, in the sense of categorical group objects. The same notion specialized to other categories yields Lie groups (smooth manifolds + smooth multiplication), algebraic groups (varieties + regular multiplication), topological monoids (drop inversion), and so on. In each case, the universal definition is: "an object equipped with multiplication and inversion morphisms satisfying the group axioms diagrammatically".

The continuity of multiplication and inversion expresses the same idea in **topological algebra**: every algebraic operation should be continuous if the algebraic object also carries a topology. Topological rings, topological vector spaces, topological fields are defined analogously, each by requiring continuity of the relevant algebraic operations.

In **harmonic analysis**, the right level of generality is a **locally compact** topological group, on which a left-translation-invariant measure (Haar measure) exists uniquely up to scaling. This unifies the Fourier transform on $\mathbb{R}^n$, on $S^1$ (Fourier series), and on compact groups (representation theory) under a single framework.

---

# Examples and Corollaries

**Is an instance — $(\mathbb{R}^n, +)$.** $\mathbb{R}^n$ under addition with the standard topology is the prototype abelian topological group. Multiplication $(x, y) \mapsto x + y$ is continuous (sum of continuous coordinate functions), inversion $x \mapsto -x$ is continuous (negation). The same applies to $(\mathbb{Z}, +), (\mathbb{Q}, +), (\mathbb{C}, +)$.

**Is an instance — $(S^1, \cdot)$.** The unit circle in $\mathbb{C}$ under complex multiplication: $S^1 = \{z \in \mathbb{C} : |z| = 1\}$. Equivalently $S^1 = \mathbb{R}/\mathbb{Z}$ (quotient of additive reals by integers), with multiplication addition modulo $1$. Compact abelian topological group, the source of Fourier series.

**Is an instance — $\operatorname{GL}_n(\mathbb{R})$.** The general linear group of invertible $n \times n$ real matrices, as an open subset of $\mathbb{R}^{n^2}$ (complement of the zero set of the polynomial $\det$). Multiplication is polynomial, hence continuous; inversion is rational (Cramer's rule), with nonvanishing denominator $\det$ on this domain, hence continuous. A topological group of dimension $n^2$. The subgroups $\operatorname{SL}_n, \operatorname{O}(n), \operatorname{SO}(n), \operatorname{U}(n), \operatorname{SU}(n)$ are all closed subgroups, hence topological groups under the subspace topology.

**Is an instance — discrete groups.** Any group $G$ with the discrete topology is a topological group: multiplication and inversion are automatically continuous (every map from a discrete space is). $(\mathbb{Z}, +), (\mathbb{Z}/n\mathbb{Z}, +), S_n$ (symmetric group), free groups — all are topological groups with the discrete topology.

**Is NOT an instance — multiplication on $\mathbb{R}$.** $(\mathbb{R}, \cdot)$ is not a group at all: $0$ has no multiplicative inverse. But $(\mathbb{R} \setminus \{0\}, \cdot)$ is a topological group (multiplicative reals).

**Is NOT an instance of Hausdorff — $\mathbb{R}/\mathbb{Q}$.** The quotient $\mathbb{R}/\mathbb{Q}$ is an abelian group with indiscrete topology (see [[Ex - A quotient with trivial topology]]); not Hausdorff. By Bredon's definition, not a topological group. (Some authors would still call it a topological group.)

**Corollary — topological groups are homogeneous.** For any $g, h \in G$, the translation $L_{hg^{-1}}$ is a homeomorphism sending $g$ to $h$. So the local topology at every point is the same: the topology of $G$ is determined entirely by neighborhoods of $e$ (see [[Thm - Translations are Homeomorphisms]]).

**Corollary — open subgroups are closed.** If $H \leq G$ is an open subgroup, its complement $G \setminus H$ is a union of (open) cosets $gH$, hence open. So $H$ is closed.

**Corollary — topological groups are completely regular.** This follows from regularity ([[Thm - Topological Group is Regular]]) plus the existence of enough continuous real-valued functions (Urysohn-style arguments). Hence topological groups are highly separable spaces.

**Calibration check.** Verify: $\operatorname{O}(n)$ is a closed bounded subset of $\mathbb{R}^{n^2}$ (cut out by polynomial equations $AA^T = I$, hence closed; entries bounded by $1$, hence bounded), hence compact. Verify $\operatorname{SL}_n(\mathbb{R})$ is a closed subgroup of $\operatorname{GL}_n(\mathbb{R})$ but is *not* compact (it's a closed subset of $\mathbb{R}^{n^2}$ that's unbounded). Verify that $S^1$ and $\operatorname{SO}(2)$ are isomorphic as topological groups (see [[Ex - S1 and SO(2) are homeomorphic as topological groups]]).

---

# Unlocked by This

> [!tip] Lie Group *(from Differential Geometry)*
> A **Lie group** is a topological group that is also a smooth manifold, with multiplication and inversion smooth maps. The Lie algebra is the tangent space at $e$, and the exponential map provides a chart from a neighborhood of $0$ in the Lie algebra to a neighborhood of $e$. All classical matrix groups are Lie groups.

> [!tip] Haar Measure *(from Measure Theory)*
> Every **locally compact** topological group admits a unique-up-to-scaling left-translation-invariant Radon measure, the **Haar measure**. This is the foundation of harmonic analysis on groups: Fourier transform on $\mathbb{R}^n$, $S^1$, $\mathbb{Z}^n$, and noncommutative groups all unify under Haar.

> [!tip] Pontryagin Duality *(from Harmonic Analysis)*
> For locally compact abelian groups, the dual $\hat{G} := \operatorname{Hom}(G, S^1)$ of continuous homomorphisms to the circle is itself a locally compact abelian group, and the double-dual map $G \to \hat{\hat{G}}$ is an isomorphism. This is **Pontryagin duality**, the generalization of the Fourier transform.
