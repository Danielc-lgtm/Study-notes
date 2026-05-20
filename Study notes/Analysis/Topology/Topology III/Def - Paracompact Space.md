---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Separation Axioms"
  - "Def - Locally Finite Family and Refinement"
  - "Def - Compact Space"
tags: [analysis, topology]
---

# Notation

$X$ is a Hausdorff topological space. An **open cover** of $X$ is a family $\{U_\alpha\}_{\alpha \in A}$ of open subsets with $\bigcup_\alpha U_\alpha = X$. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Axiom Motivation

Compactness is the property that every open cover has a *finite* subcover. It is extraordinarily useful — it converts global problems into finite ones — but it is also extraordinarily restrictive. $\mathbb{R}^n$, smooth manifolds, infinite simplicial complexes, function spaces: most spaces of analytic interest are not compact. So if compactness is the only tool that gives us "finite subcovers", we are out of luck for non-compact spaces.

The fix is to find a weaker condition that still gives a usable form of finiteness. Paracompactness is the answer: a Hausdorff space is paracompact if every open cover has a *locally finite open refinement*. We drop "finite" but keep "locally finite", and we drop "subcover" but allow "refinement" — a cover by *smaller* opens, each contained in some original cover element. The trade is excellent: paracompactness covers many more spaces (all metric spaces, all smooth manifolds, all CW complexes), and it is *exactly* the condition that yields **partitions of unity**.

Why is locally finite the right replacement for finite? Because the operations one wants to do with covers — summing functions over the cover, intersecting sets in the cover, taking closures of unions — all behave well when the cover is locally finite. Locally, you have finitely many cover elements present; the operation at each point is a finite operation, so it converges. A *globally* infinite cover would cause infinite sums and unmanageable intersections; a *locally* finite cover hides this complexity from each individual point.

Why refinement rather than subcover? Because subcovers are too restrictive. Most non-compact spaces have nice covers (e.g., by small balls) that are not locally finite (the cover of $\mathbb{R}$ by all balls of radius $1$ is not locally finite — every point lies in continuum many balls), but they have locally finite *refinements* (e.g., by carefully chosen smaller balls). Refinement gives the flexibility to shrink and reindex cover elements to make local finiteness achievable.

The flexibility of paracompactness combines beautifully with the **Hausdorff axiom**. The combination paracompact + Hausdorff implies *normality* — between any two disjoint closed sets there are disjoint open separating sets. The proof uses local finiteness to combine pointwise separations into global ones: cover one closed set with locally-finite small open neighborhoods, each disjoint from a fixed point of the other closed set; the union (of opens) is open, the union (of closures, using local finiteness) is closed and disjoint, etc. So paracompact Hausdorff inherits all the goodies of normal spaces — Urysohn's lemma, Tietze extension, separating functions — plus the local-finite structure on top.

What is the cleanest sufficient condition for paracompactness? **Metric spaces are paracompact** (Stone's theorem, a hard result). **Locally compact $\sigma$-compact Hausdorff spaces are paracompact** (Bredon's Theorem 12.11; the proof uses an exhaustion by compact sets). **Smooth manifolds are paracompact** (by definition in most conventions, or because they are LCH and second countable, hence $\sigma$-compact). These are the standard sufficient conditions, and together they cover essentially every space encountered in analysis and geometry.

What is the cost of paracompactness? You exclude some pathological spaces — the **long line** (locally Euclidean but uncountable), spaces with too much "spreading" — but in practice you exclude almost nothing of analytic interest.

---

# The Definition

A topological space $X$ is **paracompact** if:

1. $X$ is **Hausdorff** ($T_2$);
2. Every open cover $\{U_\alpha\}_{\alpha \in A}$ of $X$ has a **locally finite open refinement**: a locally finite open cover $\{V_\beta\}_{\beta \in B}$ such that every $V_\beta$ is contained in some $U_\alpha$.

The Hausdorff hypothesis is built in by convention (Bredon's Definition 12.3); some authors define paracompactness without it and add Hausdorff separately. The combination paracompact + Hausdorff is what is genuinely useful, so we make it part of the definition.

Compactness implies paracompactness: a finite subcover *is* a locally finite open refinement (finite always implies locally finite).

A topological space $X$ is **$\sigma$-compact** if $X = \bigcup_{n=1}^\infty K_n$ for some sequence of compact sets $K_n$.

Closed subspaces of paracompact spaces are paracompact (Bredon's Proposition 12.4); arbitrary subspaces need not be. Products of paracompact spaces need not be paracompact (the product of the Sorgenfrey line with itself is a classical counterexample to product-preservation).

---

# Categorical Definition

There is no clean categorical characterization of paracompactness — it is a specific separation/covering condition rather than a universal property. However, paracompact Hausdorff spaces form the right category for **partitions of unity** and **sheaf-theoretic constructions** (since their gluing axioms work cleanly with locally finite covers).

---

# Relate to Other Fields / Compression

In **differential geometry**, a **smooth manifold** is typically defined to be Hausdorff, second countable, and locally Euclidean. The second countability plus local Euclideanness (hence local compactness) imply $\sigma$-compactness, hence paracompactness. So manifolds are automatically paracompact, and they automatically have smooth partitions of unity — which is the entire foundation of differential geometry on manifolds.

In **sheaf theory**, paracompactness is the hypothesis under which **soft sheaves are acyclic** and the **Čech cohomology** computed from a good cover converges to the sheaf cohomology. The paracompact Hausdorff assumption is the standard one in algebraic topology for these constructions to work.

In **algebraic topology**, the **fine cell structure** of a CW complex is locally finite (every point lies in finitely many cells in a small enough neighborhood), making CW complexes paracompact. Paracompactness is what allows the usual fixed-point-theory and cohomology constructions to proceed.

In **PDE** and **Riemannian geometry**, partitions of unity (existing because of paracompactness) are used to define Riemannian metrics, connections, smooth bump functions, and to localize the analysis of PDE to coordinate patches. Without paracompactness, these constructions fail.

The classical result that **every metric space is paracompact** is due to **A. H. Stone** (1948). The proof is nontrivial; it uses a maximal-element argument or a sequence of refinements. This implies that every metrizable space — every "topologically nice" space — automatically has partitions of unity.

---

# Examples / Corollaries

**Is an instance — every compact Hausdorff space.** A finite subcover *is* a locally finite open refinement.

**Is an instance — $\mathbb{R}^n$.** Locally compact Hausdorff and $\sigma$-compact (covered by closed balls of integer radii), hence paracompact by [[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]].

**Is an instance — every metric space.** By Stone's theorem; the proof is intricate but yields a sharp result.

**Is an instance — every smooth manifold.** By the standard definition (Hausdorff + second countable + locally Euclidean), manifolds are LCH and $\sigma$-compact, hence paracompact.

**Is an instance — every CW complex.** The cell structure provides a natural locally-finite open cover.

**Is NOT an instance — the long line.** The **long line** is locally Euclidean but uncountable; it cannot be covered by a locally finite collection of open intervals of bounded length (any such cover would force countability). This is the standard example of a Hausdorff locally Euclidean space that is *not* paracompact.

**Is NOT an instance — the Sorgenfrey plane.** The Sorgenfrey line (real line with half-open intervals $[a, b)$ as basic opens) is paracompact, but its product with itself, the Sorgenfrey plane, is not. This shows that products do not preserve paracompactness.

**Corollary — paracompact Hausdorff implies normal.** Between any two disjoint closed sets $F, G$ there are disjoint open neighborhoods. See [[Thm - Paracompact Implies Normal]]. Hence Urysohn's lemma and Tietze extension are available in paracompact Hausdorff spaces.

**Corollary — paracompact spaces have partitions of unity.** Every open cover of a paracompact Hausdorff space has a subordinate partition of unity. See [[Thm - Paracompact Has Partitions of Unity]]. This is the existence theorem that makes paracompactness the foundational hypothesis for differential geometry, sheaf theory, and integration on manifolds.

**Corollary — closed subspaces of paracompact are paracompact.** If $A \subseteq X$ is closed and $X$ is paracompact, then $A$ with the subspace topology is paracompact. The proof: cover $A$ by opens in $X$, extend the cover by $X \setminus A$, take a locally finite refinement, restrict to $A$.

**Calibration check.** Verify: (i) every compact Hausdorff space is paracompact; (ii) $\mathbb{R}^n$ is paracompact via $\sigma$-compactness; (iii) the long line is not paracompact; (iv) closed subspaces of paracompact spaces are paracompact; (v) products of paracompact spaces need not be paracompact (Sorgenfrey plane); (vi) every paracompact Hausdorff space is normal.

---

# Unlocked by This

> [!tip] Existence of Partitions of Unity *(from this topic)*
> The cornerstone application: paracompact Hausdorff spaces have **partitions of unity** subordinate to every open cover. See [[Thm - Paracompact Has Partitions of Unity]]. This is what powers every "local-to-global" construction in differential geometry.

> [!tip] Riemannian Metrics on Manifolds *(from Differential Geometry)*
> Every smooth manifold admits a Riemannian metric, constructed by a partition of unity argument: take local Euclidean inner products in coordinate charts and patch them together. The existence depends entirely on paracompactness.

> [!tip] Sheaf Cohomology *(from Algebraic Topology)*
> On a paracompact Hausdorff space, the Čech cohomology of a sheaf agrees with its derived-functor cohomology, and soft sheaves are acyclic. Paracompactness is the technical hypothesis that makes sheaf cohomology computable.

> [!tip] Normality and Function-Richness *(from this topic)*
> Paracompact Hausdorff spaces are normal, so all of Urysohn's lemma and Tietze extension are available. Combined with paracompactness, this yields the existence of partitions of unity.
