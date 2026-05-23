---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Function on a Manifold"
  - "Def - Support of a Function"
  - "Def - Locally Finite Family and Refinement"
  - "Def - Partition of Unity"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold. $\{U_\alpha\}_{\alpha \in A}$ is an open cover of $M$, indexed by a (possibly uncountable) set $A$. $\{\psi_\alpha\}_{\alpha \in A}$ denotes a smooth partition of unity subordinate to $\{U_\alpha\}$. The full registry is on [[Differential Geometry II — Smooth Maps and Partitions of Unity]].

---

# Axiom Motivation

The motivating problem is *globalization*. We have a smooth manifold $M$ and an open cover $\{U_\alpha\}$ — typically a cover by coordinate charts. On each $U_\alpha$, we know how to perform some construction: define a Riemannian metric (using the standard Euclidean inner product in chart coordinates), define a vector field (using a constant vector field in the chart), define a $k$-form (using a standard Euclidean form), build a smooth function with prescribed local data. The challenge is *gluing*: on overlaps $U_\alpha \cap U_\beta$, the constructions from the two charts will disagree (different charts give different Euclidean inner products at the same point of the manifold). We need a way to *blend* the conflicting local constructions into a single global one, smoothly varying across overlaps.

The blending mechanism is a **weighted average**. If $T_\alpha$ is the local construction on $U_\alpha$ and $\psi_\alpha : M \to [0, 1]$ is a weight function supported in $U_\alpha$, then the weighted average
$$T(p) = \sum_\alpha \psi_\alpha(p) T_\alpha(p)$$
makes sense at each point: it is a convex combination of the local objects $T_\alpha(p)$ at points $p$ in the supports. For the sum to be unambiguously defined, the weights must (i) be defined globally on $M$ (with $T_\alpha$ extended by zero outside $U_\alpha$), (ii) sum to $1$ at every point (so the result is a genuine convex combination, not just a weighted sum), and (iii) be locally finite (so the sum has only finitely many nonzero terms at each point, no convergence issues). For the result to be smooth, the weights must be smooth.

These three conditions — local support, summing to $1$, local finiteness — together with smoothness, are exactly the axioms of a smooth partition of unity. The construction is forced by the requirement that the weighted average produce a well-defined smooth global object.

*Why local support?* Without $\operatorname{supp}(\psi_\alpha) \subseteq U_\alpha$, the weight $\psi_\alpha$ could be nonzero at a point $p$ where $T_\alpha$ is not even defined (i.e. $p \notin U_\alpha$). The local support condition guarantees that $\psi_\alpha(p) T_\alpha(p)$ makes sense — when $\psi_\alpha(p) \neq 0$, $p$ is in $\operatorname{supp}(\psi_\alpha) \subseteq U_\alpha$, so $T_\alpha(p)$ is defined. We extend $\psi_\alpha T_\alpha$ by zero outside $U_\alpha$, with no discontinuity, because $\psi_\alpha \to 0$ on the boundary.

*Why sum to $1$?* Because we want a convex combination (a true average), not an arbitrary weighted sum. If $\sum_\alpha \psi_\alpha(p) = c(p) \neq 1$, then $\sum_\alpha \psi_\alpha(p) T_\alpha(p) = c(p) \cdot (\text{average})$, which is a *scaled* average, distorting the result. The normalization $\sum = 1$ is what makes the operation "the local construction at $p$ as seen from a mixture of charts".

*Why local finiteness?* Because at each point $p$, the sum $\sum_\alpha \psi_\alpha(p)$ is *defined* only when finitely many terms are nonzero (otherwise we have an issue of convergence in $\mathbb{R}$, and worse for the smoothness of the sum as a function on $M$). Local finiteness says every $p$ has a neighbourhood on which all but finitely many $\psi_\alpha$ vanish identically, so the sum reduces to a finite sum locally — both pointwise convergence and smoothness become automatic.

*Why smoothness of $\psi_\alpha$?* Because if the weights are merely continuous, the weighted average $\sum_\alpha \psi_\alpha T_\alpha$ is at best continuous. For smooth target objects (smooth functions, smooth metrics, smooth forms), we need smooth weights to preserve smoothness. This is the upgrade from the topological partition of unity to the smooth one — and the upgrade is non-trivial because not every paracompact Hausdorff space admits *smooth* partitions of unity (it requires a smooth structure with adequate bump functions).

**Bridge to the topological version.** The manifold-level definition is the [[Def - Partition of Unity|topological partition of unity]] with the *additional requirement* that each $\psi_\alpha$ is smooth (as a function on $M$ in the sense of [[Def - Smooth Function on a Manifold]]), not merely continuous. The three axioms (local support, local finiteness, sum to $1$) are unchanged. The existence theorem requires more: the topological version needs only paracompact Hausdorff, while the smooth version needs paracompact Hausdorff *plus* a supply of smooth bump functions (which a smooth manifold automatically has). The construction is parallel — refine the cover to be locally finite, build bumps on each cover element via Urysohn (topological) or via the $e^{-1/t}$-trick (smooth), sum, normalize — but in the smooth case the bumps are smooth.

The construction of the *smooth* bump functions uses the function $\psi_0(t) = e^{-1/t}$ for $t > 0$ — see [[Def - Bump Function and Smooth Cutoff]]. This is the entire reason the smooth partition of unity theorem is *separate* from the topological one: the smooth bumps require a $C^\infty$-but-not-analytic function, an explicit real-analysis input, while the topological bumps come from Urysohn (which is purely set-theoretic / topological).

---

# The Definition

Let $M$ be a smooth manifold and $\{U_\alpha\}_{\alpha \in A}$ an open cover of $M$. A **smooth partition of unity subordinate to $\{U_\alpha\}$** is a family of smooth functions $\{\psi_\alpha\}_{\alpha \in A}$, $\psi_\alpha \in C^\infty(M)$, with the following properties:

(1) $0 \leq \psi_\alpha(p) \leq 1$ for every $\alpha \in A$ and $p \in M$;
(2) $\operatorname{supp}(\psi_\alpha) \subseteq U_\alpha$ for every $\alpha \in A$;
(3) The family of supports $\{\operatorname{supp}(\psi_\alpha)\}_{\alpha \in A}$ is **locally finite**: every $p \in M$ has an open neighbourhood that meets only finitely many of the supports;
(4) $\sum_{\alpha \in A} \psi_\alpha(p) = 1$ for every $p \in M$.

Note that condition (4) is meaningful because of condition (3): at each $p$, only finitely many terms in the sum are nonzero, so the sum is a finite real number (well-defined). The sum is moreover a smooth function on $M$ because, locally near each $p$, it equals a finite sum of smooth functions — hence smooth.

The existence theorem [[Thm - Existence of Smooth Partitions of Unity]] guarantees that for *every* open cover of a smooth manifold, a smooth partition of unity subordinate to it exists. The proof reduces the cover to a countable locally finite refinement by regular coordinate balls, then builds bumps on each refinement element and normalizes.

**Bridge to the topological version (key).** This is the [[Def - Partition of Unity|topological partition of unity]] applied to the topological space underlying $M$, with the additional smoothness requirement on each $\psi_\alpha$. The topological version requires the $\psi_\alpha$ to be continuous; the manifold version requires them to be smooth. The smoothness is the only difference, but it is a real strengthening — the existence proof must use smooth bumps (built from $e^{-1/t}$), not just Urysohn bumps.

**Variants:** Some authors allow the partition of unity to be indexed by a different set than the cover, with each $\psi_\beta$ supported in *some* $U_{\alpha(\beta)}$ — this corresponds to a refinement. We use the "strictly subordinate" version (same index set, $\operatorname{supp}(\psi_\alpha) \subseteq U_\alpha$). The two definitions are equivalent for existence purposes.

---

# Categorical Definition

There is no clean categorical formulation of a partition of unity, but the construction is central to the descent theory of sheaves: a sheaf-theoretic local-to-global argument typically requires a partition-of-unity argument to assemble local sections into a global one. **Soft sheaves** (sheaves where every section extends from a closed subset to a global section) are exactly those for which partitions-of-unity-style assembly works; the sheaf of smooth functions $\mathcal{O}_M^\infty$ on a smooth manifold is soft.

In more sophisticated language: the existence of partitions of unity on $M$ is what makes the sheaf $\mathcal{O}_M^\infty$ acyclic for sheaf cohomology, and this is what allows the de Rham cohomology of $M$ (computed by $\mathcal{O}_M^\infty$-modules) to compute the actual cohomology of $M$ as a topological space (the de Rham theorem).

---

# Relate to Other Fields / Compression

A partition of unity is **a smoothly-varying choice of "which chart to use here"**. Each point $p$ lies in some subset of the $U_\alpha$, and the weights $\psi_\alpha(p)$ tell you how much to weight the chart $U_\alpha$'s opinion when constructing an object at $p$. Where $\psi_\alpha = 1$, you fully trust the chart $U_\alpha$; where $\psi_\alpha = 0$, you ignore it; where $0 < \psi_\alpha < 1$, you blend.

It is also **the smooth analogue of the topological partition of unity** — see the bridge above. In a paracompact Hausdorff space, the topological partition of unity exists (Urysohn-based); on a smooth manifold, the smooth partition of unity exists ($e^{-1/t}$-bump-based). The strengthening from topological to smooth is the addition of "smooth in the manifold sense", verifiable via charts.

It is also **the simplest example of a sheaf-theoretic gluing**: local objects on $U_\alpha$ glue to a global object via the partition-of-unity weights. In algebraic geometry, gluing is done by morphisms on overlaps that satisfy a cocycle condition (Čech-style); in smooth manifold theory, the existence of $C^\infty$ partitions of unity reduces gluing to a single weighted sum, dramatically simpler than the Čech machinery.

**True name:** *a partition of unity is a smooth choice of weights for blending local data*. The operational meaning is that whenever you have local objects $T_\alpha$ on each $U_\alpha$ and you want a global object, you can multiply each $T_\alpha$ by $\psi_\alpha$, extend by zero, and sum — and the result is global, smooth, and inherits whatever convex properties the $T_\alpha$ had (positivity, symmetry, bilinearity).

---

# Examples / Corollaries

**Is an instance: $\mathbb{R}$ with the cover $\{(n - 1, n + 1) : n \in \mathbb{Z}\}$.** Build a smooth bump $\rho_n$ supported in $(n - 1, n + 1)$, equal to $1$ on $[n - 1/2, n + 1/2]$. Then $\sum_n \rho_n$ is positive everywhere (every $x \in \mathbb{R}$ is in some $[n - 1/2, n + 1/2]$), and locally finite (each point is in at most a few intervals). Normalize: $\psi_n = \rho_n / \sum_m \rho_m$. The family $\{\psi_n\}$ is a smooth partition of unity subordinate to the cover.

**Is an instance: trivial partition of unity for the single-cover.** If $\{U\} = \{M\}$ — the trivial cover with one element — then $\psi \equiv 1$ is the constant function, satisfying all four axioms trivially. This is the degenerate but valid base case.

**Is an instance: partition of unity for a finite cover.** If $M$ is compact and $\{U_1, \ldots, U_k\}$ is a finite open cover, the partition of unity construction simplifies: no Zorn's lemma is needed for shrinking, the locally-finiteness is automatic. Build bumps $\rho_i$ supported in $U_i$ with $\sum_i \rho_i > 0$, normalize. See [[Ex - Smooth Partition of Unity Subordinate to a Cover]].

**Is an instance: partition of unity on $S^2$ via stereographic charts.** Cover $S^2$ by two stereographic charts $U_N = S^2 \setminus \{N\}$ and $U_S = S^2 \setminus \{S\}$. Build a smooth bump $\psi_N$ supported in $U_N$, equal to $1$ in a neighbourhood of the south pole, and similarly $\psi_S$ for the north pole. Adjust so $\psi_N + \psi_S \equiv 1$ — e.g., let $\psi_N = h(\text{latitude})$, $\psi_S = 1 - h(\text{latitude})$, where $h$ is a smooth cutoff.

**Is NOT an instance: the indicator functions of a partition.** The family $\{\chi_{U_\alpha}\}$ — characteristic functions of the cover elements — sums to *some* function (potentially $> 1$ on overlaps) and the functions are not continuous. Not a partition of unity by any of the axioms.

**Is NOT an instance: a continuous (not smooth) partition of unity on a smooth manifold.** The topological version exists on any paracompact Hausdorff space, but it is not "smooth" — the weights are merely continuous. For most differential-geometric constructions, smoothness of the weights is essential, since the goal is a smooth global object. On a smooth manifold, the topological partition is a weaker structure than the smooth one.

**Is NOT an instance: a partition of unity with non-locally-finite supports.** If we drop the local finiteness condition, the sum $\sum_\alpha \psi_\alpha$ might have infinitely many nonzero terms at a point, and convergence becomes an issue. The functions $\rho_n(x) = 1/(1 + (x - n)^2)$ have positive supports everywhere on $\mathbb{R}$ — every point is in every support — so local finiteness fails. Even after normalization to sum to $1$ pointwise, this is not a partition of unity in our sense.

**Corollary (existence, smooth case).** For any open cover of a smooth manifold, a smooth partition of unity subordinate to it exists. See [[Thm - Existence of Smooth Partitions of Unity]].

**Corollary (the sum is a finite sum at each point).** For any partition of unity $\{\psi_\alpha\}$ and any $p \in M$, the sum $\sum_\alpha \psi_\alpha(p) = 1$ has only finitely many nonzero terms, by local finiteness. So $1$ is the sum of finitely many (positive) values, all in $[0, 1]$.

**Corollary (convex combination of local data).** Given local objects $T_\alpha$ on each $U_\alpha$ (where the relevant "object" is in some vector space, or convex set, that admits weighted averages), the global $T = \sum_\alpha \psi_\alpha T_\alpha$ inherits whatever convex properties the $T_\alpha$ had. Positive-definite quadratic forms sum to positive-definite forms; symmetric tensors sum to symmetric tensors; nonzero vectors sum to potentially-zero vectors (so vector-field constructions need care).

**Calibration check.** Verify the following: (i) on $\mathbb{R}^2$ with the cover $\{B(p, 1) : p \in \mathbb{Z}^2\}$ (open balls of radius $1$ centred at integer lattice points), the cover is locally finite (any point of $\mathbb{R}^2$ lies in at most a bounded number of these balls), and a smooth partition of unity subordinate to it exists. (ii) For the trivial cover $\{M\}$, the constant function $\psi \equiv 1$ is a partition of unity. (iii) A partition of unity $\{\psi_\alpha\}$ extends each $\psi_\alpha$ (defined globally on $M$) to a function vanishing on $M \setminus \operatorname{supp}(\psi_\alpha)$ — the smoothness is preserved across this "boundary" because $\psi_\alpha \to 0$ smoothly. (iv) The bridge to the topological version: every smooth partition of unity is, in particular, a topological partition of unity (since smooth $\Rightarrow$ continuous).

---

# Unlocked by This

> [!tip] Globalization of Local Constructions *(from Differential Geometry)*
> Whenever a smooth object can be defined on each chart of a smooth manifold, a partition of unity provides a global smooth object. Riemannian metrics, connections, volume forms, sections of vector bundles — all are built this way. The most-used phrase in differential geometry is "by a partition of unity argument", and it refers to this construction. See [[Thm - Existence of Smooth Partitions of Unity]] for the existence and [[Thm - Smooth Extension Lemma]] for the canonical application.

> [!tip] Existence of Riemannian Metrics *(from Riemannian Geometry)*
> Every smooth manifold $M$ admits a Riemannian metric — a smoothly-varying inner product on each tangent space. The proof: take a partition of unity $\{\psi_\alpha\}$ subordinate to a chart cover $\{U_\alpha\}$; define local metrics $g_\alpha$ via the Euclidean inner product in chart coordinates; sum $g = \sum_\alpha \psi_\alpha g_\alpha$. The result is smooth and positive-definite (convex combination of positive-definite quadratic forms). See **Riemannian Geometry** (downstream) and [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds|DG XII]] for the existence proof.

> [!tip] Integration of Forms on Manifolds *(from Differential Geometry)*
> The integral of a top-degree differential form on an oriented manifold is defined via a partition of unity: $\int_M \omega = \sum_\alpha \int_{U_\alpha} \psi_\alpha \omega$, where each integral on the right is a Euclidean integral via the chart coordinates. Independence of the chart cover follows from the change-of-variables formula. See [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]].

> [!tip] Soft Sheaves and Acyclicity *(from Sheaf Theory)*
> The sheaf $\mathcal{O}_M^\infty$ of smooth functions on a manifold is **soft** because partitions of unity exist: any smooth section on a closed subset extends to a global smooth section. Softness implies that $\mathcal{O}_M^\infty$ is acyclic for sheaf cohomology, and this is the foundation for the de Rham theorem identifying de Rham cohomology with singular cohomology. See [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]].
