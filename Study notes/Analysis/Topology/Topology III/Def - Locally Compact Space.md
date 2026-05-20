---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Compact Space"
  - "Def - Neighbourhood and Neighbourhood Basis"
  - "Def - Separation Axioms"
tags: [analysis, topology]
---

# Notation

$X$ is a topological space. A **neighborhood** of $x \in X$ is a set $N$ containing an open set containing $x$; we do not require $N$ itself to be open. A neighborhood basis at $x$ is a family $\mathcal{B}_x$ of neighborhoods of $x$ such that every neighborhood of $x$ contains some member of $\mathcal{B}_x$. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Axiom Motivation

Compactness is one of the most useful properties a topological space can have, but in practice most spaces of interest are *not* compact. Euclidean space $\mathbb{R}^n$, smooth manifolds, function spaces — these are typically non-compact, and yet we want to bring compactness arguments to bear on them. **Local compactness** is the answer: the requirement that compactness be available *locally*, even when the space as a whole fails to be compact.

The motivating examples are $\mathbb{R}^n$ and its open subsets. $\mathbb{R}^n$ is not compact (it is unbounded), but every point has a compact neighborhood — a closed ball around the point is compact (by Heine–Borel). This local availability of compactness is what makes the analysis of $\mathbb{R}^n$ tractable: locally, you have a compact set to work with, and you can use compactness arguments on small enough scales. The hypothesis to capture this — "every point has a compact neighborhood" — is the simplest possible local version of compactness, and it turns out to be exactly the right hypothesis for an enormous amount of analysis.

Why "every point has a compact neighborhood" and not "every neighborhood contains a compact one"? In *Hausdorff* spaces these are equivalent: if $x$ has compact neighborhood $K$ and $U$ is any neighborhood of $x$, then $K \cap U$ contains an open neighborhood $V$ of $x$ with $\overline{V} \subseteq K \cap U$ (by regularity of $K$ as a compact Hausdorff space restricted to a neighborhood); $\overline{V}$ is closed in compact $K$ hence compact, and lies in $U$. But in non-Hausdorff spaces the two conditions can differ, and the "every neighborhood contains a compact one" condition is sometimes called **strong local compactness**. In analysis we almost always work in Hausdorff settings, so the distinction collapses.

What does local compactness buy you? Three crucial things. First, the **one-point compactification** $X^+ = X \cup \{\infty\}$ exists for any LCH space, embedding $X$ as an open dense subset of a compact Hausdorff space. This is the "minimal" compactification and is the standard tool for converting non-compact problems into compact ones. Second, **completely regular** — every LCH space is completely regular, so there are enough continuous functions for separation arguments (proved by Urysohn on the compact $K^+$ and restricting). Third, **Radon measures** — the **Riesz representation theorem** identifies positive linear functionals on $C_c(X)$ for LCH $X$ with Radon measures, the natural measure-theoretic objects on $X$. The whole theory of integration on non-compact spaces flows from local compactness.

The standard non-examples are infinite-dimensional Banach spaces. These are not locally compact: the closed unit ball is bounded but not compact (containing infinite orthonormal sequences), and no smaller ball can be compact either (scaling and translation). F. Riesz's theorem says: a normed space is locally compact if and only if it is finite-dimensional. This is one of the most important dichotomies in functional analysis — finite-dimensional spaces support compactness arguments locally; infinite-dimensional spaces do not.

What would happen if we *required* compactness globally? We would exclude $\mathbb{R}^n$, smooth manifolds, sequence spaces — almost every space of analytic interest. What would happen if we *weakened* local compactness — say, asked only that every point has a *bounded* neighborhood, or a neighborhood that is *closed*? Closed bounded subsets of infinite-dimensional Banach spaces are bounded and closed but not compact, so the weakened hypothesis would not give us the compactness arguments we need. Local compactness is the minimum.

---

# The Definition

A topological space $X$ is **locally compact** if every point $x \in X$ has a **compact neighborhood**: a neighborhood $K$ of $x$ such that $K$ is compact (as a subspace of $X$). Note: $K$ itself need not be open, but it must contain an open set containing $x$.

In a **Hausdorff** space, local compactness is equivalent to: every point $x$ has a neighborhood basis consisting of compact neighborhoods. (Bredon's Theorem 11.2: if $X$ is locally compact Hausdorff, then every neighborhood of every point contains a compact neighborhood of that point.)

The acronym **LCH** stands for **Locally Compact Hausdorff**, the combination that is the standard setting for most of measure theory, harmonic analysis, and the theory of topological groups. LCH spaces are completely regular (see **LCH implies completely regular**).

A subspace $A \subseteq X$ is **locally closed** if every point $a \in A$ has an open neighborhood $V_a$ in $X$ such that $V_a \cap A$ is closed in $V_a$. Equivalently, $A = C \cap U$ for some closed $C$ and open $U$ in $X$. Locally closed subspaces of locally compact Hausdorff spaces are again locally compact Hausdorff — this is the standard inheritance theorem.

A space is **$\sigma$-compact** if it is a countable union of compact sets. $\sigma$-compactness is a global countability condition that combines well with local compactness — see [[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]].

---

# Categorical Definition

Local compactness does not have a categorical universal-property characterization in the same clean sense as the product or coproduct. However, the **category of locally compact Hausdorff spaces with proper continuous maps** is the natural setting in which compactification functors (one-point, Stone–Čech) become well-behaved adjoint functors. The one-point compactification $(\cdot)^+$ is a functor from LCH spaces with proper maps to compact Hausdorff spaces with continuous maps, with the universal property that proper maps into LCH spaces lift to maps of one-point compactifications fixing $\infty$.

---

# Relate to Other Fields / Compression

In **measure theory**, the natural setting for **Radon measures** is locally compact Hausdorff spaces. The Riesz representation theorem says: positive linear functionals on $C_c(X)$ (continuous compactly supported real-valued functions on $X$) correspond bijectively to Radon measures on $X$. Local compactness ensures that $C_c(X)$ is rich enough — every point has a compactly supported bump function — and Hausdorff ensures the measure is uniquely determined.

In **harmonic analysis** and **representation theory**, the natural objects are **locally compact topological groups**. The Haar measure (a translation-invariant Radon measure) exists for any LC group; the Fourier transform on $\mathbb{R}^n$, the Peter–Weyl theorem for compact groups, and the Plancherel formula for non-compact groups all sit in this framework. The hypothesis of local compactness on the group is what gives integration its translation invariance and compactness arguments for representations.

In **algebraic topology**, a space $X$ is locally compact Hausdorff if and only if its **one-point compactification** $X^+$ is compact Hausdorff. Many topological invariants (cohomology with compact supports, Borel–Moore homology, dualities) are naturally defined via $X^+$ and so implicitly use local compactness.

In **functional analysis**, F. Riesz's theorem says a normed vector space is locally compact if and only if it is finite-dimensional. Infinite-dimensional Banach spaces are *never* locally compact. The replacement is the **weak topology** (for which the unit ball is weakly compact by Banach–Alaoglu in the dual), not local compactness in the norm topology.

---

# Examples / Corollaries

**Is an instance — $\mathbb{R}^n$.** Every point has a closed ball as compact neighborhood (by Heine–Borel). $\mathbb{R}^n$ is the prototype LCH space.

**Is an instance — every compact Hausdorff space.** The whole space is a compact neighborhood of every point.

**Is an instance — every smooth manifold.** A smooth manifold is locally homeomorphic to $\mathbb{R}^n$, which is locally compact, so by inheritance smooth manifolds are locally compact. Together with Hausdorffness (axiomatic for manifolds), this makes manifolds LCH, the basic setting for differential geometry.

**Is an instance — open subsets of $\mathbb{R}^n$.** An open $U \subseteq \mathbb{R}^n$ is locally compact: at each $x \in U$, a small enough closed ball is contained in $U$ and compact.

**Is an instance — locally finite simplicial complexes.** A simplicial complex where every vertex is in finitely many simplices is locally compact: a neighborhood of any point is contained in a finite union of compact simplices.

**Is NOT an instance — $\mathbb{Q}$ with the subspace topology from $\mathbb{R}$.** Every neighborhood of a rational $q$ contains a small interval $(q - \varepsilon, q + \varepsilon) \cap \mathbb{Q}$, which is not compact: it has irrational limit points whose absence breaks completeness, hence (with total boundedness) compactness. So $\mathbb{Q}$ is *not* locally compact. This is the canonical example showing that local compactness can fail in apparently "small" spaces.

**Is NOT an instance — infinite-dimensional Banach spaces.** F. Riesz: an infinite-dimensional normed space has no compact neighborhood of $0$ (and by translation, no compact neighborhood of any point). Sequence spaces $\ell^p$, function spaces $L^p$ (for infinite measure space), $C([0, 1])$ — all fail to be locally compact in the norm topology. This is one of the most important non-examples; it is the reason functional analysis develops weak topologies as a substitute.

**Is NOT an instance — the long line.** The **long line** $L$ — the order topology on $[0, \omega_1) \times [0, 1)$ with lexicographic order — is locally compact at most points but fails paracompactness, so it does not embed nicely in compact spaces.

**Corollary — locally compact Hausdorff implies completely regular.** This is **LCH implies completely regular**. The argument: separate locally via compactness, use the normality of the compact neighborhood, restrict back.

**Corollary — products of locally compact spaces.** A finite product of locally compact spaces is locally compact (the product of compact neighborhoods is a compact neighborhood). An infinite product of locally compact spaces is *almost never* locally compact, because basic open sets in the product topology have cofinitely many full factors, which are typically non-compact. Exception: a product of locally compact spaces where all but finitely many factors are compact is locally compact.

**Corollary — open subspaces and closed subspaces.** Open and closed subspaces of LCH spaces are LCH (locally closed in general). The inheritance theorem: locally closed subspaces of LCH spaces are LCH, and conversely every LCH space embeds as a locally closed subspace of a compact Hausdorff space (namely $X \hookrightarrow X^+$ as an open subspace).

**Calibration check.** Verify: (i) $\mathbb{R}^n$ is locally compact (use closed balls); (ii) $\mathbb{Q}$ is not locally compact (use that closed rational intervals are not compact); (iii) $\ell^2$ is not locally compact (use the orthonormal sequence in the unit ball); (iv) the open interval $(0, 1)$ is locally compact (small closed sub-intervals are compact); (v) the one-point compactification $(\mathbb{R}^n)^+ \cong S^n$ is compact Hausdorff (stereographic projection).

---

# Unlocked by This

> [!tip] One-Point Compactification *(from this topic)*
> Every LCH space $X$ has a **one-point compactification** $X^+ = X \cup \{\infty\}$, a compact Hausdorff space in which $X$ embeds as an open subset with single-point complement. See [[Thm - One-Point Compactification]]. The basic example: $(\mathbb{R}^n)^+ \cong S^n$ via stereographic projection.

> [!tip] Radon Measures and Riesz Representation *(from Measure Theory)*
> On an LCH space $X$, positive linear functionals on $C_c(X)$ correspond to **Radon measures** via $\Lambda f = \int f\, d\mu$. The supply of compactly supported continuous functions, guaranteed by local compactness and Urysohn (on the compactification), is what makes the correspondence work.

> [!tip] Haar Measure on Locally Compact Groups *(from Harmonic Analysis)*
> A **locally compact topological group** admits a **Haar measure**: a translation-invariant Radon measure, unique up to scaling. Local compactness is essential — it is the topological hypothesis under which the measure is constructible. This is the foundation of abstract harmonic analysis.

> [!tip] Paracompactness from σ-Compactness *(from this topic)*
> An LCH space that is also **$\sigma$-compact** (a countable union of compact sets) is paracompact. This is the standard route by which smooth manifolds (LCH + second countable, hence $\sigma$-compact) acquire partitions of unity. See [[Thm - Locally Compact σ-Compact Hausdorff is Paracompact]].
