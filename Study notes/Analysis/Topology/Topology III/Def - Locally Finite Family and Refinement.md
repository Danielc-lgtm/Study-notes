---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Closure, Interior, and Boundary"
tags: [analysis, topology]
---

# Notation

$X$ is a topological space. A **collection** or **family** $\mathcal{U} = \{U_\alpha\}_{\alpha \in A}$ is an indexed family of subsets of $X$. We write $\mathcal{U} \succeq \mathcal{V}$ when $\mathcal{U}$ is a refinement of $\mathcal{V}$. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Axiom Motivation

Compactness gives access to a powerful tool: any open cover has a *finite* subcover. Finiteness is what allows you to assemble local data into global — combining finitely many pieces, you can take maxes, minima, sums, intersections without convergence concerns. But many spaces — non-compact manifolds, function spaces, infinite simplicial complexes — are not compact and the finiteness is not available. Local finiteness is the right generalization: rather than asking that the cover itself be finite, ask only that at every point the cover *looks* finite — only finitely many members touch any small enough neighborhood.

This is a much weaker condition. An open cover of $\mathbb{R}$ by intervals $(n - 1, n + 1)$ for $n \in \mathbb{Z}$ is locally finite: each point lies in at most two intervals, so a small enough neighborhood of any point meets only finitely many cover elements — yet the cover is countably infinite. Locally finite is the operational substitute for finite in non-compact settings: it gives you, locally, all the assembly power of finiteness, without forcing global finiteness.

The key payoff is that **locally finite unions interact well with closures**. If $\{F_\alpha\}$ is a locally finite family of closed sets, then $\bigcup_\alpha F_\alpha$ is closed (not just any union of closed sets is closed; this requires the locally-finite hypothesis). The intuition: near any point, only finitely many $F_\alpha$ are present, so the union locally equals a *finite* union of closed sets, which is closed. Globally, every limit point is captured. Without local finiteness, infinite unions of closed sets can spill open: $\bigcup_n [1/n, 1] = (0, 1]$, which is not closed.

Equivalently, the closure of a union equals the union of closures for locally finite families: $\overline{\bigcup_\alpha F_\alpha} = \bigcup_\alpha \overline{F_\alpha}$. This is *the* assembly principle: it says local-to-global construction works as expected. Without it, the closure of the union can be strictly larger than the union of closures, and gluing arguments break.

The second key notion is **refinement**: a cover $\mathcal{V}$ refines $\mathcal{U}$ if every $V \in \mathcal{V}$ is contained in some $U \in \mathcal{U}$. Refinement is the formalization of "make the pieces smaller". Given an open cover, the question is whether you can pass to a refinement with better properties — locally finite, made of small balls, with controlled supports. The interaction between local finiteness and refinement is the heart of paracompactness: a paracompact space is one where *every* open cover has a locally finite *open* refinement.

Compare with **closure-preserving** and **point-finite** families. A family is **point-finite** if each *point* lies in finitely many members; this is weaker than locally finite (each point has a neighborhood meeting finitely many). A family is **closure-preserving** if for every subfamily $\mathcal{F}' \subseteq \mathcal{F}$, $\overline{\bigcup_{F \in \mathcal{F}'} F} = \bigcup_{F \in \mathcal{F}'} \overline{F}$; this is weaker than locally finite. Local finiteness is the strongest of these natural conditions, and it is the one that combines best with paracompactness and partitions of unity.

Why not just demand finite covers? Because *non-compact spaces have no finite open covers*. A locally compact, non-compact space like $\mathbb{R}^n$ cannot be covered by finitely many *bounded* open sets (the cover would have bounded union), and yet most natural covers (by coordinate charts, by balls of bounded radius) are unbounded in cardinality. The construction needs to scale to non-compact spaces, and local finiteness is the scaling.

---

# The Definition

Let $X$ be a topological space, and let $\mathcal{U} = \{U_\alpha\}_{\alpha \in A}$ be a family (indexed collection) of subsets of $X$.

**Locally finite.** The family $\mathcal{U}$ is **locally finite** if every point $x \in X$ has a neighborhood $N$ meeting only finitely many members:

$$|\{\alpha \in A : N \cap U_\alpha \neq \emptyset\}| < \infty.$$

A locally finite family is *not* required to be a cover, nor required to consist of open sets; but in practice we apply the notion to open covers.

**Refinement.** Let $\mathcal{U} = \{U_\alpha\}_{\alpha \in A}$ and $\mathcal{V} = \{V_\beta\}_{\beta \in B}$ be two families of subsets of $X$. Then $\mathcal{V}$ is a **refinement** of $\mathcal{U}$, written $\mathcal{V} \succeq \mathcal{U}$, if every $V_\beta \in \mathcal{V}$ is contained in some $U_\alpha \in \mathcal{U}$:

$$\forall \beta \in B, \ \exists \alpha \in A : V_\beta \subseteq U_\alpha.$$

If $\mathcal{U}$ and $\mathcal{V}$ are both covers, the refinement need not have a bijection with $\mathcal{U}$ — the cardinalities can differ. An **open refinement** is a refinement consisting of open sets.

**Locally finite cover.** A **locally finite open cover** of $X$ is an open cover that is also locally finite.

These definitions extend to families of *subsets*, not just covers — a locally finite collection of closed sets, for instance, plays a role in the proof that paracompact implies normal.

---

# Relate to Other Fields / Compression

Local finiteness is closely related to **Čech cohomology** and **good covers** in algebraic topology. A **good cover** of a manifold is an open cover by sets such that every finite intersection is contractible (or empty); to compute Čech cohomology one wants the cover to be at least locally finite, so that the Čech complex has well-defined finite intersections at each level. The existence of good covers on paracompact manifolds (a key technical lemma in de Rham theory) uses local finiteness.

In **sheaf theory**, a **sheaf** $\mathcal{F}$ on a topological space is required to satisfy compatibility under restriction and gluing. The gluing axiom — sections on a cover that agree on overlaps glue to a global section — typically requires the cover to be locally finite (or at least that the index set be manageable) for the gluing to make sense without infinite-product convergence issues.

In **PDE** and **Riemannian geometry**, partitions of unity (which are inherently locally finite) are the standard tool for converting local results to global. Every gluing argument — Riemannian metric existence, smooth connection existence, integration of forms — uses the locally finite structure of a partition.

In **descriptive set theory**, a **$\sigma$-discrete** family is a countable union of discrete (hence locally finite) families. This refinement of local finiteness underlies the **Nagata–Smirnov metrization theorem** — a topological space is metrizable if and only if it is regular and has a $\sigma$-locally-finite base.

---

# Examples / Corollaries

**Is an instance — the cover of $\mathbb{R}$ by unit intervals.** The family $\{(n - 1, n + 1) : n \in \mathbb{Z}\}$ is a locally finite open cover of $\mathbb{R}$: every point lies in at most $2$ intervals, so a neighborhood of any point meets at most $4$ intervals. This is the prototype: countably infinite, locally finite, with bounded overlap.

**Is an instance — the cover of $\mathbb{R}^n$ by integer-translated cubes.** The family of closed unit cubes $\{[k_1, k_1 + 1] \times \cdots \times [k_n, k_n + 1] : (k_1, \dots, k_n) \in \mathbb{Z}^n\}$ is a locally finite cover by closed sets (and the union of their interiors is locally finite as an open family, with each point in at most $2^n$ cubes).

**Is NOT an instance — the cover of $(0, 1]$ by $(1/n, 1]$.** The family $\{(1/n, 1] : n \in \mathbb{N}\}$ is an open cover of $(0, 1]$. It is *not* locally finite at points near $0$: any neighborhood of $1/k$ meets all $(1/n, 1]$ for $n \geq k$, which is infinite. The point $0$ is not in $(0, 1]$, so the issue is on the open boundary.

**Is NOT an instance — the cover of $\mathbb{R}$ by $(-n, n)$.** The family $\{(-n, n) : n \in \mathbb{N}\}$ is an open cover of $\mathbb{R}$, but it is not locally finite: every point lies in all but finitely many of the $(-n, n)$, so every neighborhood meets infinitely many cover elements.

**Refinement example — $\mathbb{R}$.** The cover $\{(n - 1, n + 1)\}_{n \in \mathbb{Z}}$ is a refinement of $\{(-n, n)\}_{n \in \mathbb{N}}$ (every short interval is contained in a long interval), and it is locally finite. This is the standard move: given a non-locally-finite cover, find a locally finite refinement.

**Corollary — locally finite union of closed sets is closed.** If $\{F_\alpha\}$ is a locally finite family of closed sets, $\bigcup_\alpha F_\alpha$ is closed. Proof: let $x$ be a limit point of the union; some neighborhood $N$ of $x$ meets only finitely many $F_\alpha$, say $F_{\alpha_1}, \dots, F_{\alpha_k}$. The limit point $x$ is a limit point of $\bigcup_i F_{\alpha_i}$ (within $N$), which is a finite union of closed sets, hence closed, hence $x \in \bigcup_i F_{\alpha_i} \subseteq \bigcup_\alpha F_\alpha$.

**Corollary — closure of locally finite union.** For a locally finite family $\{A_\alpha\}$, $\overline{\bigcup_\alpha A_\alpha} = \bigcup_\alpha \overline{A_\alpha}$. (The same proof as above: closure is a local property, and locally the family is finite.)

**Corollary — every subfamily of a locally finite family is locally finite.** Trivially: if $N$ meets only finitely many of $\mathcal{U}$, it meets only finitely many of any sub-family.

**Corollary — finite subcovers of locally finite covers.** If $X$ is compact and $\mathcal{U}$ is a locally finite open cover, then $\mathcal{U}$ is in fact *finite*. Proof: each point has a neighborhood meeting finitely many cover elements; cover $X$ by such neighborhoods; pass to a finite subcover; the total cardinality of cover elements meeting these neighborhoods is finite.

**Calibration check.** Verify: (i) the cover $\{(n - 1, n + 1)\}$ of $\mathbb{R}$ is locally finite; (ii) the cover $\{(-n, n)\}$ is *not* locally finite; (iii) finiteness implies local finiteness (trivially); (iv) any open cover of a compact space has a locally finite refinement (in fact, a finite subcover); (v) any refinement of a locally finite cover need not be locally finite — a refinement can introduce more sets, breaking local finiteness.

---

# Unlocked by This

> [!tip] Paracompactness *(from this topic)*
> A Hausdorff space is **paracompact** if every open cover has a locally finite open refinement. This is the most flexible covering condition for non-compact spaces, and it is the cleanest sufficient condition for the existence of partitions of unity. See [[Def - Paracompact Space]].

> [!tip] Partition of Unity *(from this topic)*
> A **partition of unity** subordinate to a cover $\{U_\alpha\}$ requires its support family to be locally finite, so that the sum $\sum_\alpha \rho_\alpha$ converges pointwise (it is a *finite* sum at each point). See [[Def - Partition of Unity]].

> [!tip] Nagata–Smirnov Metrization *(from this topic)*
> The **Nagata–Smirnov theorem** characterizes metrizable spaces as regular spaces with a **$\sigma$-locally-finite base** — a countable union of locally finite bases. This is the general metrization theorem; Urysohn's is the second-countable special case.
