---
type: theorem
subject: topology
prereqs:
  - "Def - Nowhere Dense and Meager"
  - "Def - Cauchy Sequence and Complete Metric Space"
  - "Def - Locally Compact Space"
tags: [analysis, topology, baire, category]
---

# Notation

$X$ a topological space. $\{A_n\}$ a countable family of subsets of $X$. "First category" / "meager" / "second category" / "residual" defined on the parent topic page and in [[Def - Nowhere Dense and Meager]]. $B_r(x)$ open ball of radius $r$ around $x$ (in a metric space). The full registry is on the topic page.

---

# Motivation

The Baire category theorem is the canonical *structural existence* theorem of topology. It does not produce a specific point with a specific property; it produces, in a complete metric space (or locally compact Hausdorff space), a *generic* element — one in the complement of any countable union of "small" (nowhere dense) sets. The statement is short, the proof is one shrinking-ball construction, and the applications are vast.

The intuition: a "small" (nowhere dense) set is topologically thin — every nonempty open set contains a sub-open set disjoint from it. The countable union of thin sets is still thin, and the Baire theorem says: the whole space is not such a union. In particular, the complement of a meager set is nonempty — usually dense.

This is the engine behind every "generic" argument: the generic continuous function is nowhere differentiable; the generic Banach space operator has nontrivial spectrum; the generic dynamical system has dense periodic orbits or some other strong property. In each case, the "bad" set is meager, and the Baire theorem produces a witness for the "good" property.

In functional analysis, Baire is the foundation of three cornerstone theorems: Banach-Steinhaus (uniform boundedness from pointwise boundedness), open mapping (surjective continuous linear maps are open), and closed graph (closed graphs imply continuity). Each application writes the "bad" set as a countable union of nowhere dense sets and applies Baire.

---

# Statement

Let $X$ be either a **complete metric space** or a **locally compact Hausdorff space**. Then:

1. **Open subsets are second category.** The union of a countable family of nowhere dense subsets of $X$ has empty interior. Equivalently, every nonempty open subset of $X$ is not meager.

2. **Residual sets are dense (contrapositive).** The intersection of countably many dense open subsets of $X$ is dense.

The two formulations are contrapositives of each other and capture the same theorem.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "complete metric space or LCH space". Both classes are large:

**Every Banach space (and $\ell^p, L^p, C(K)$).** Property $B$: a normed vector space whose Cauchy sequences converge. The bridge: a Banach space is complete by definition. *Example:* $C[0, 1]$, the space of continuous functions on $[0, 1]$ with the supremum norm, is a Banach space; Baire applies. This is the setting for [[Ex - A continuous nowhere differentiable function exists]].

**Every closed subspace of a complete metric space.** Property $B$: closed subsets inherit completeness. *Example:* the closed unit ball of a Banach space, the orthonormal basis of a Hilbert space — all are complete metric subspaces.

**Locally compact Hausdorff spaces.** Property $B$: every point has a compact neighborhood, and the space is Hausdorff. *Example:* every locally compact group (including all Lie groups), every locally Euclidean manifold, $\mathbb{R}^n$ itself.

**Polish spaces.** Property $B$: separable, completely metrizable. The bridge: $X$ admits a *complete* metric (even if the given one isn't complete). *Example:* $\mathbb{R}$, $[0, 1]$, $\mathbb{R}^n$, the Cantor set, the Baire space $\mathbb{N}^\mathbb{N}$.

**Targets (Output Amplification)**

The conclusion "residual sets are dense" amplifies in many directions:

Combine with **a continuous function or operator.** Property $D$: a continuous map on the space whose "bad" behavior is meager. The amplified result $E$: the "good" behavior is dense, in fact residual. *Example:* Banach-Steinhaus — pointwise boundedness of a family of operators (good behavior on a residual set) implies uniform boundedness ([[Thm - Banach–Steinhaus and Open Mapping (Application of Baire)]]).

Combine with **an explicit dense set of approximating elements.** Property $D$: a countable dense set of "simple" functions, polynomials, etc. The amplified result $E$: generic elements have properties unattainable by the dense subset alone. *Example:* the generic continuous function is nowhere differentiable, even though the dense polynomials are smooth.

Combine with **fixed-point theorems.** Property $D$: a continuous self-map with some genericity property. The amplified result $E$: most self-maps have fixed points, or specific orbits — generic dynamical systems exhibit predictable behavior.

---

# Why Is It True

The proof is a single explicit construction: a shrinking sequence of nested open sets whose centers form a Cauchy sequence converging to a witness point.

Take a countable family $\{A_n\}$ of nowhere dense subsets and any nonempty open set $U \subseteq X$. We want to find a point in $U$ not in any $A_n$, i.e., in $U \setminus \bigcup A_n$.

Start with $V_0 := U$. Since $A_0$ is nowhere dense, $\overline{A_0}$ has empty interior, so $U \setminus \overline{A_0}$ is a nonempty open set. Choose $V_1 \subseteq U \setminus \overline{A_0}$ open and nonempty, with $\overline{V_1}$ "small" — in the metric case, $V_1$ is a ball of small radius; in the LCH case, $V_1$ has compact closure.

Inductively: having $V_n$, since $A_n$ is nowhere dense, $V_n \setminus \overline{A_n}$ is open and nonempty. Choose $V_{n+1} \subseteq V_n \setminus \overline{A_n}$ open, with $\overline{V_{n+1}} \subseteq V_n$ and $\overline{V_{n+1}}$ small.

**Metric case:** Choose $V_{n+1}$ as a ball with radius $< 2^{-n}$. Then the centers $x_n$ of $V_n$ form a Cauchy sequence (any two centers $x_m, x_n$ with $m, n \geq k$ are in $V_k$, of diameter $< 2 \cdot 2^{-k}$). By completeness, $x_n \to x$ for some $x \in X$. Since $\overline{V_n} \subseteq V_{n-1}$ and the chain is nested, $x \in \overline{V_n}$ for all $n$, hence $x \notin A_n$ (since $V_n \cap A_n = \emptyset$... wait, $V_{n+1}$ avoids $\overline{A_n}$ which contains $A_n$). So $x \in U \setminus \bigcup A_n$.

**LCH case:** Choose $V_n$ with compact closure $\overline{V_n}$. The chain $\overline{V_1} \supseteq \overline{V_2} \supseteq \dots$ is a decreasing chain of nonempty compacts, which has nonempty intersection (any decreasing chain of compacts in a Hausdorff space has the finite intersection property of any finite subfamily, hence by compactness of $\overline{V_1}$, the full intersection is nonempty). Pick $x$ in the intersection; same argument as before.

The reason to expect this: completeness (or local compactness) gives an "all the way down" mechanism — a shrinking-ball construction converges, or a nested-compact-set construction has nonempty intersection. The proof is essentially Cantor's nested-interval lemma generalized to complete metric spaces and LCH spaces.

---

# What Makes This Hard

The non-obvious step is *recognizing the shrinking-ball construction*. Beginners often think Baire is non-constructive (it produces a point that is generic but not specified), but the construction is explicit: at each step, choose a shrinking ball avoiding the next bad set. The most common error is forgetting to ensure the *closures* are nested ($\overline{V_{n+1}} \subseteq V_n$, not just $V_{n+1} \subseteq V_n$) — without this, the limit might fall outside the chain.

---

# Rederivation Scaffold

**High-level strategy:**
Inductively construct nested nonempty open sets $V_n$ with $\overline{V_n} \subseteq V_{n-1}$ and $V_n$ avoiding $A_n$. Use completeness (or local compactness) to extract a limit point in $\bigcap V_n$.

**Subgoal decomposition:**

1. **Induction setup.** $V_0 := U$ (given nonempty open). $V_{n+1}$ chosen nonempty open with $\overline{V_{n+1}} \subseteq V_n \setminus \overline{A_n}$. Use that $A_n$ nowhere dense $\Leftrightarrow$ $V_n \setminus \overline{A_n}$ is nonempty open.
   - *Hint:* Use regularity of complete metric / LCH spaces to find such $V_{n+1}$.

2. **Extract limit point.** In metric case: choose $V_n$ as a ball of radius $< 2^{-n}$; centers Cauchy, complete metric gives limit. In LCH case: choose $V_n$ with compact closure; nested compacts have nonempty intersection.

3. **Verify witness.** The limit point $x \in \overline{V_n}$ for every $n$, hence $x \notin A_n$ (since $\overline{V_{n+1}}$ avoids $A_n$). So $x \in U \setminus \bigcup A_n$.

---

# Lemma Decomposition

> [!note]- Lemma 1: A nowhere dense set's closure has empty interior
> **Statement:** $A$ is nowhere dense iff $\overline{A}$ has empty interior iff every nonempty open set contains a nonempty open set disjoint from $\overline{A}$.
>
> **Hint:** Definition.
>
> **Why needed:** Provides the open set to descend into at each step.
>
> > [!note]- Full proof
> > Direct from the definition: $\operatorname{int}(\overline{A}) = \emptyset$ iff $X \setminus \overline{A}$ is dense, iff every nonempty open set meets $X \setminus \overline{A}$, iff every nonempty open set contains a nonempty open subset disjoint from $\overline{A}$.

> [!note]- Lemma 2: Inductively shrinking balls in complete metric spaces
> **Statement:** Let $X$ be complete metric. Given nested decreasing nonempty open sets $V_n$ with $\overline{V_n} \subseteq V_{n-1}$ and $\operatorname{diam}(V_n) \to 0$, the intersection $\bigcap V_n$ is a single point.
>
> **Hint:** Centers form a Cauchy sequence.
>
> **Why needed:** Provides the witness in the metric case.
>
> > [!note]- Full proof
> > Choose $x_n \in V_n$ for each $n$. For $m, n \geq k$, $x_m, x_n \in V_k$, so $d(x_m, x_n) \leq \operatorname{diam}(V_k) \to 0$. Hence $(x_n)$ is Cauchy. By completeness, $x_n \to x \in X$. For each $k$, $x_n \in V_k$ for $n \geq k$, so $x \in \overline{V_k} \subseteq V_{k-1}$. So $x \in \bigcap V_n$. Uniqueness: if $y \in \bigcap V_n$ too, then $d(x, y) \leq \operatorname{diam}(V_k) \to 0$, so $x = y$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X$ be either complete metric or locally compact Hausdorff, $U \subseteq X$ open nonempty, $\{A_n\}_{n \geq 0}$ nowhere dense subsets of $X$.
>
> **Inductive construction.** Set $V_0 := U$. Given $V_n$ open nonempty, since $A_n$ is nowhere dense, $V_n \setminus \overline{A_n}$ is open and nonempty (Lemma 1 applied to the open set $V_n$). In the metric case: choose $x_{n+1} \in V_n \setminus \overline{A_n}$ and $r_{n+1} < 2^{-(n+1)}$ small enough that $B_{2 r_{n+1}}(x_{n+1}) \subseteq V_n \setminus \overline{A_n}$; set $V_{n+1} := B_{r_{n+1}}(x_{n+1})$. Then $\overline{V_{n+1}} \subseteq B_{2 r_{n+1}}(x_{n+1}) \subseteq V_n \setminus \overline{A_n}$.
>
> In the LCH case: choose a point in $V_n \setminus \overline{A_n}$; by local compactness, it has a relatively compact neighborhood $W$ with $\overline{W} \subseteq V_n \setminus \overline{A_n}$; set $V_{n+1} := W$.
>
> **Limit extraction.**
>
> *Metric case (Lemma 2):* the centers $(x_n)$ form a Cauchy sequence with $d(x_m, x_n) < r_{\min(m,n)}$ for $m, n$ large. By completeness, $x_n \to x \in X$. The point $x$ lies in $\overline{V_n}$ for every $n$.
>
> *LCH case:* $\overline{V_1} \supseteq \overline{V_2} \supseteq \cdots$ is a decreasing chain of nonempty compact sets in $\overline{V_1}$. By compactness (or the finite intersection property), $\bigcap \overline{V_n} \neq \emptyset$. Choose $x$ in the intersection.
>
> **Verify witness.** For each $n$, $x \in \overline{V_{n+1}} \subseteq V_n \setminus \overline{A_n}$, so $x \notin A_n$. Hence $x \in U \setminus \bigcup_n A_n$, so $U$ is not a subset of $\bigcup_n A_n$. Since $U$ was arbitrary, $\bigcup_n A_n$ has empty interior. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Continuity points of pointwise limits.** If $f_n : X \to \mathbb{R}$ are continuous and $f = \lim f_n$ pointwise, the discontinuity set of $f$ is meager. So $f$ is continuous on a dense $G_\delta$. See [[Ex - Pointwise limit of continuous functions has dense continuity set]] (Bredon's Corollary 17.4).

**Existence of transcendental numbers.** The algebraic numbers in $\mathbb{R}$ are countable (the polynomials are countable; each has finitely many roots). So the algebraic numbers are meager in $\mathbb{R}$. Hence the irrational/transcendental numbers form a residual set in $\mathbb{R}$, in particular nonempty (this is silly for $\mathbb{R}$ since algebraic numbers have measure zero, but the same argument in a Banach space proves the genericity of "transcendental" basis elements).

**The space of homeomorphisms.** $\operatorname{Homeo}(M)$ for a compact manifold $M$ is a Baire space (in the compact-open topology). A residual set of homeomorphisms have generic dynamical properties (e.g., topological transitivity, or no preserved metrics).

**Liouville numbers as residual.** Liouville numbers (real numbers approximable too well by rationals) form a residual set in $\mathbb{R}$, even though they have measure zero. Baire-generic ≠ measure-generic.

---

# Bridges

- **[[Def - Nowhere Dense and Meager]]** — the size notions used.

- **[[Def - Cauchy Sequence and Complete Metric Space]]** — the completeness hypothesis in the metric case.

- **[[Def - Locally Compact Space]]** — the alternative LCH hypothesis.

- **[[Thm - Banach–Steinhaus and Open Mapping (Application of Baire)]]** — the cornerstone applications in functional analysis.

---

# Unlocked by This

> [!tip] Banach-Steinhaus (Uniform Boundedness) *(from Functional Analysis)*
> A family of bounded linear operators on a Banach space that is **pointwise bounded** is **uniformly bounded**. The proof: the set $\{x : \sup \|T_n x\| > k\}$ for each $k$ is closed and meager if the family is pointwise bounded; by Baire, its union (where pointwise unboundedness occurs) is meager — but it's all of $X$ if the family is not uniformly bounded. Contradiction.

> [!tip] Open Mapping Theorem *(from Functional Analysis)*
> A surjective continuous linear map between Banach spaces is **open** — i.e., maps open sets to open sets. Proof uses Baire: $T(X)$ is a countable union of $nT(B_1)$, so one of these has nonempty interior, which translates to openness of $T$.

> [!tip] Closed Graph Theorem *(from Functional Analysis)*
> A linear map between Banach spaces with closed graph is continuous. Proof: apply the open mapping theorem to the projection from the graph to one of the spaces.

> [!tip] Existence of Nowhere Differentiable Functions *(from Real Analysis)*
> Bredon's Corollary 17.6 (and [[Ex - A continuous nowhere differentiable function exists]]): in $C[0, 1]$, the set of nowhere differentiable functions is residual. Baire produces existence; Weierstrass produces an explicit example.
