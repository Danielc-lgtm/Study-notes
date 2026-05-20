---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
  - "Def - Locally Finite Family and Refinement"
  - "Def - Paracompact Space"
tags: [analysis, topology]
---

# Notation

$X$ is a topological space. The **support** of a continuous function $f : X \to \mathbb{R}$ is $\operatorname{supp}(f) = \overline{\{x \in X : f(x) \neq 0\}}$, the closure of the set where $f$ is nonzero. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Axiom Motivation

The motivating problem: take a global property of a space — a Riemannian metric, an integral, a connection, a vector field — that is "easy to define locally" and "hard to define globally". On a manifold, for instance, we know how to put a Euclidean inner product on each tangent space when we use a coordinate chart (it is just the standard $\mathbb{R}^n$ inner product). The question is how to glue these local choices into a single, smoothly varying Riemannian metric on the whole manifold, despite the fact that different charts disagree on overlaps.

The answer is to take a **weighted average** of the local choices, with the weights varying smoothly so that no single chart's choice dominates and the result is well-defined where multiple charts overlap. A **partition of unity** is exactly the data that supplies the weights: a family of continuous functions $\{\rho_\alpha\}$, each supported in one of the open sets of the cover, with $\sum_\alpha \rho_\alpha \equiv 1$ pointwise. The condition $\sum \rho_\alpha = 1$ ensures the weights are *normalized*, so the weighted average is a genuine average (a convex combination). The condition $\operatorname{supp}(\rho_\alpha) \subseteq U_\alpha$ ensures that the weight $\rho_\alpha$ is *local* to $U_\alpha$ — it contributes only where the local construction on $U_\alpha$ is defined.

The third condition is **local finiteness of the supports**: every point has a neighborhood in which only finitely many $\rho_\alpha$ are nonzero. This is essential. Without it, the sum $\sum_\alpha \rho_\alpha(x)$ might involve infinitely many nonzero terms at a single point $x$, and convergence becomes a problem. Local finiteness reduces the sum at every point to a *finite* sum, which is unambiguously defined and continuous. It also ensures that the weighted average $\sum_\alpha \rho_\alpha(x) \cdot (\text{local thing}_\alpha(x))$ has only finitely many nonzero terms, so it converges and inherits the smoothness of the $\rho_\alpha$ and the local things.

What makes this *the* right construction? The conditions are minimal. To average over local data on $\{U_\alpha\}$, you need: (a) a weight for each $U_\alpha$, supported in $U_\alpha$ — otherwise it does not respect the locality of the cover; (b) total weight $1$ — otherwise the average is not a convex combination; (c) only finitely many nonzero contributions at each point — otherwise convergence is uncertain. Each axiom is forced. The continuity (or smoothness) of $\rho_\alpha$ is needed to produce continuous (smooth) global objects from continuous (smooth) local ones.

**Subordination**: a partition of unity $\{\rho_\alpha\}$ is **subordinate to a cover** $\{U_\alpha\}$ if $\operatorname{supp}(\rho_\alpha) \subseteq U_\alpha$ for each $\alpha$. This means the indexing of the partition matches the indexing of the cover, so each weight comes "labeled" with the cover element it belongs to. A natural variant is to have the support inside *some* cover element, not necessarily $U_\alpha$ for the same $\alpha$ — this is subordination "up to refinement".

The existence theorem (Bredon Thm 12.8) says: every open cover of a paracompact Hausdorff space has a subordinate partition of unity. So paracompactness is the topological hypothesis under which partitions of unity exist. The proof has three steps: refine the cover to a locally finite one (paracompactness), shrink each cover element to a closed set still covering (using normality, which is implied by paracompact Hausdorff), apply Urysohn's lemma to get bump functions on each closed-open pair, then normalize.

For **smooth manifolds**, one wants $C^\infty$ partitions of unity, not just continuous ones. The existence is again guaranteed, using $C^\infty$ bump functions on $\mathbb{R}^n$ (e.g., $\exp(-1/(1 - |x|^2))$ on the open unit ball, $0$ outside) pulled back through coordinate charts. The local finiteness of the partition lets the sum converge in $C^\infty$.

---

# The Definition

Let $X$ be a topological space, and let $\{U_\alpha\}_{\alpha \in A}$ be an open cover of $X$.

A **partition of unity** subordinate to $\{U_\alpha\}$ is a family $\{\rho_\alpha\}_{\alpha \in A}$ of continuous functions $\rho_\alpha : X \to [0, 1]$ such that:

1. **Support condition.** $\operatorname{supp}(\rho_\alpha) \subseteq U_\alpha$ for every $\alpha \in A$.
2. **Local finiteness.** The collection $\{\operatorname{supp}(\rho_\alpha) : \alpha \in A\}$ is **locally finite** — every point has a neighborhood meeting only finitely many $\operatorname{supp}(\rho_\alpha)$.
3. **Sum to one.** $\sum_{\alpha \in A} \rho_\alpha(x) = 1$ for every $x \in X$. (The sum is well-defined and continuous because of local finiteness — at each point it is a finite sum.)

Sometimes the index set of the partition is allowed to differ from the cover's index set, with each $\rho_\beta$ supported in some $U_{\alpha(\beta)}$ (corresponding to a refinement). The version above is the *strictly subordinate* one.

For a **smooth manifold** $M$, a **smooth partition of unity** has each $\rho_\alpha$ smooth (rather than just continuous). The same definition applies with $\rho_\alpha \in C^\infty(M)$.

---

# Categorical Definition

There is no clean categorical characterization of partitions of unity, but they are central to **descent** in sheaf theory: a sheaf-theoretic local-to-global construction often requires a partition-of-unity argument to assemble local sections into a global one.

---

# Relate to Other Fields / Compression

In **differential geometry**, partitions of unity are *the* tool for converting local constructions into global ones. The construction of a **Riemannian metric**, a **vector field**, a **connection**, a **volume form**, or a **smooth function with prescribed local values** all proceed by: take a local construction on each chart; multiply by $\rho_\alpha$; sum. The result is smooth (or $C^k$) globally, with the local fidelity preserved on the supports.

In **PDE** and **variational analysis**, partitions of unity are used to **localize** the analysis of a PDE on a domain $\Omega$: decompose the test function space as $C^\infty_c(\Omega) = \bigoplus_\alpha \rho_\alpha \cdot C^\infty_c(U_\alpha)$, prove regularity locally on each $U_\alpha$, and glue. This is the standard technique in elliptic regularity theory.

In **measure theory** on locally compact Hausdorff spaces, partitions of unity (existing because LCH $\sigma$-compact implies paracompact) are used to define the **Riesz representation** of positive linear functionals: a functional $\Lambda : C_c(X) \to \mathbb{R}$ can be localized to each compact set $K$ by multiplying functions by a bump that is $1$ on $K$, and the partition assembles the local pieces into a global measure.

In **sheaf cohomology**, the **softness** of a sheaf (extension of sections from closed sets to neighborhoods, used in proving acyclicity) often relies on partitions of unity in the underlying space.

In **algebraic topology**, the **Mayer–Vietoris sequence** for sheaf cohomology uses partitions of unity to combine cohomology on each $U_\alpha$ into cohomology on the whole space.

---

# Examples / Corollaries

**Is an instance — $\mathbb{R}$ with the cover $\{(n - 1, n + 1) : n \in \mathbb{Z}\}$.** Define $\rho_n(x)$ to be a smooth bump function equal to $1$ on $[n - 1/2, n + 1/2]$, supported in $(n - 1, n + 1)$. Normalize: $\tilde\rho_n = \rho_n / \sum_m \rho_m$. The sum has only finitely many nonzero terms at each $x$ (locally finite cover), so $\sum_m \rho_m$ is smooth and positive, and $\{\tilde\rho_n\}$ is a smooth partition of unity subordinate to the cover.

**Is an instance — partition of unity from Urysohn.** On $\mathbb{R}^2$ with the cover $\{B(p, 1) : p \in \mathbb{Z}^2\}$, by paracompactness we get a locally finite refinement (any open neighborhood of an integer point is covered by at most $4$ balls in the cover). Apply Urysohn's lemma (using normality of $\mathbb{R}^2$) to each pair of (closed shrunken ball, complement of original ball) to get bumps, normalize.

**Is NOT an instance — the indicator function family on a partition.** $\{\mathbf{1}_{[n, n+1)}(x)\}$ for $n \in \mathbb{Z}$ is *not* a partition of unity, even though they sum to $1$ pointwise: the functions are not continuous. Continuity is essential — partition of unity is for smooth assembly, not for discrete partition.

**Is NOT an instance — the family $\rho_n(x) = 1/(1 + (x - n)^2)$.** These sum to a finite positive function (the sum is bounded and continuous), but they are not normalized to sum to $1$, and their supports are not contained in bounded sets — every $\rho_n$ is positive everywhere. Local finiteness fails: every point lies in the support of every $\rho_n$, so the sum has infinitely many nonzero terms. Not a partition of unity by any of the three axioms.

**Corollary — existence in paracompact Hausdorff.** Every open cover of a paracompact Hausdorff space has a subordinate partition of unity. See [[Thm - Paracompact Has Partitions of Unity]].

**Corollary — smooth partition of unity on a manifold.** Every open cover of a smooth manifold has a smooth partition of unity subordinate to it. The proof uses smooth bump functions on $\mathbb{R}^n$, pulled back through coordinate charts.

**Corollary — partition of unity gives convex combination.** Given local functions $f_\alpha : U_\alpha \to V$ (where $V$ is a convex subset of a vector space), the weighted sum $f(x) = \sum_\alpha \rho_\alpha(x) f_\alpha(x)$ (extended by $0$ outside the union of supports) is a well-defined continuous function on $X$ taking values in $V$ (since at each $x$, $f(x)$ is a finite convex combination of $f_\alpha(x)$ values).

**Calibration check.** Verify: (i) on $\mathbb{R}$ with the cover $\{(n - 1, n + 1)\}$, the family $\rho_n$ from the example is locally finite, supported correctly, sums to $1$; (ii) on a non-paracompact space like the long line, no subordinate partition of unity exists for an inconveniently chosen cover; (iii) for an open cover by a single open set $U = X$, the constant function $\rho \equiv 1$ is the trivial partition; (iv) a smooth partition of unity on a smooth manifold gives a Riemannian metric via $g(v, w) = \sum_\alpha \rho_\alpha g_\alpha(v, w)$ where $g_\alpha$ is the Euclidean inner product on chart $\alpha$.

---

# Unlocked by This

> [!tip] Riemannian Metrics on Manifolds *(from Differential Geometry)*
> A **Riemannian metric** on a smooth manifold $M$ is constructed by partition of unity: take local Euclidean inner products in coordinate charts and assemble them via $g = \sum_\alpha \rho_\alpha g_\alpha$. The existence of such metrics on every smooth manifold is the foundational fact of Riemannian geometry, and it depends entirely on the existence of partitions of unity, hence paracompactness.

> [!tip] Vector Bundle Constructions *(from Differential Geometry)*
> Connections, Hermitian metrics, and bundle morphisms on smooth vector bundles are all constructed by partition of unity arguments. Locally, on a trivializing chart, the construction is obvious; the partition glues globally.

> [!tip] Localization of Operators in PDE *(from Analysis)*
> A **pseudo-differential operator** on a manifold is defined via partition of unity: each chart has a local symbol; the global operator is $\sum_\alpha \rho_\alpha P_\alpha \rho_\alpha$ for chart-localized operators $P_\alpha$. Microlocal analysis runs on this framework.

> [!tip] Smooth Functions with Prescribed Local Data *(from Differential Geometry)*
> Given a smooth function $f_\alpha$ on each $U_\alpha$, a partition of unity produces a global smooth function $f = \sum_\alpha \rho_\alpha f_\alpha$ that locally averages the $f_\alpha$. This is one of the constant uses of the partition.
