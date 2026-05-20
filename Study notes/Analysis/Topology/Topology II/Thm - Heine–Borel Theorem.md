---
type: theorem
subject: topology
prereqs:
  - "Def - Compact Space"
  - "Def - Separation Axioms"
  - "Def - Metric Space"
tags: [analysis, topology, compactness, metric]
---

# Notation

$\mathbb{R}^n$ is Euclidean $n$-space with the standard Euclidean topology (equivalently, the metric topology). A subset $A \subseteq \mathbb{R}^n$ is **bounded** if $A \subseteq B_R(0)$ for some $R > 0$. The closure $\overline{A}$, interior $\mathrm{int}(A)$, and boundary are defined in the standard topological sense (see [[Def - Closure, Interior, and Boundary]]). $A$ is **compact** if every open cover has a finite subcover (see [[Def - Compact Space]]). The full registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Heine–Borel Theorem.** A subset $A \subseteq \mathbb{R}^n$ is **compact** if and only if $A$ is **closed and bounded**.

The theorem is a workhorse: it reduces the abstract "every open cover has a finite subcover" to two hand-checkable conditions in Euclidean space. The forward direction (compact ⇒ closed and bounded) holds in every Hausdorff metric space. The reverse direction (closed and bounded ⇒ compact) is *specific to $\mathbb{R}^n$* (and more generally finite-dimensional normed spaces) — it *fails* in infinite-dimensional spaces, as F. Riesz showed.

---

# Motivation

Compactness in the abstract is a complicated property: open-cover finitization, FIP for closed sets, convergent-subnet existence. None of these are easy to verify directly for a concrete subset of $\mathbb{R}^n$. The question this theorem answers is: *what is the cheapest checkable characterization of compactness in Euclidean space*?

The answer is "closed and bounded". Bounded is trivial — checkable by computing a single sup. Closed is also concrete — checkable by examining boundary points or by verifying $A = \overline{A}$. So compactness in $\mathbb{R}^n$ is reduced to two hand-computations.

This is enormously powerful because *every concrete compact set encountered in calculus and elementary analysis is in $\mathbb{R}^n$*: closed intervals $[a, b]$, closed disks, closed boxes, spheres, level sets of smooth functions on compact domains. All are closed and bounded; all are therefore compact; therefore the Extreme Value Theorem applies, sequences have convergent subsequences (Bolzano–Weierstrass), continuous functions attain extrema, etc. The entire toolkit of compactness in calculus is unlocked by this single theorem.

The *failure* of the theorem in infinite dimensions is equally important. In an infinite-dimensional normed space (e.g., $\ell^2$, $L^2$, $C[0, 1]$), the closed unit ball is closed and bounded but *not* compact. This is **F. Riesz's theorem**, and it is the reason functional analysis works the way it does. The cure is to either restrict to finite-dimensional subspaces (where Heine–Borel survives), or to *change the topology* (weak topologies, where the closed unit ball *is* compact by Banach–Alaoglu in the dual). The fact that the closed unit ball in $\ell^2$ is non-compact is the *signature feature* of infinite-dimensional analysis — every difference between finite and infinite dimensions descends to this.

The proof of Heine–Borel itself is a tour of the compactness toolbox: compactness of $[0, 1]$ (by direct argument from the supremum definition of compactness or by repeated bisection); Tychonoff finite product giving compactness of cubes $[-N, N]^n$; closed-in-compact giving compactness of any closed bounded subset; compactness in metric spaces gives bounded (covering by unit balls, extract a finite subcover); compactness in Hausdorff gives closed. The theorem is the assembly of these pieces.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$A \subseteq \mathbb{R}^n$".

The first disguised source is **$A$ is a level set of a continuous proper function**. Property $B$: $A = f^{-1}(\{c\})$ for $f : \mathbb{R}^n \to \mathbb{R}$ continuous with $f^{-1}(K)$ bounded for every bounded $K \subseteq \mathbb{R}$. The bridge: level sets of continuous functions are closed (preimage of $\{c\}$ which is closed); properness gives boundedness. *Example:* the sphere $S^{n-1} = \{x : \lVert x \rVert = 1\}$ as the level set of $\lVert \cdot \rVert$, hence closed and bounded, hence compact.

The second disguised source is **$A$ is the image of a continuous function from a compact source**. Property $B$: $A = f(K)$ with $K$ compact, $f : K \to \mathbb{R}^n$ continuous. The bridge: continuous images of compact are compact (by [[Thm - Continuous Image of a Compact Space]]), and compact in $\mathbb{R}^n$ is closed and bounded by this theorem. *Example:* the image of a continuous loop $\gamma : [0, 1] \to \mathbb{R}^n$ is closed and bounded.

The third disguised source is **$A$ is a closed subset of a known compact** in $\mathbb{R}^n$. Property $B$: $A \subseteq B$, $B$ compact in $\mathbb{R}^n$ (e.g., $B = [-N, N]^n$). The bridge: closed subsets of compact are compact (by [[Thm - Closed Subset of Compact is Compact]]). *Example:* the Cantor set as a closed subset of $[0, 1]$, hence compact.

**Targets (Output Amplification)**

The conclusion is "$A$ is compact iff closed and bounded".

Combine the conclusion with **a continuous real-valued function on $A$**. Property $D$: $f : A \to \mathbb{R}$ continuous. Amplified result $E$: $f$ attains its maximum and minimum on $A$ (Extreme Value Theorem). The bridge: by this theorem $A$ compact; by [[Thm - Continuous Image of a Compact Space]] $f(A) \subseteq \mathbb{R}$ compact; by this theorem applied in $\mathbb{R}$, $f(A)$ is closed and bounded, hence has max and min attained.

Combine the conclusion with **a sequence in $A$**. Property $D$: $\{x_k\}_{k \in \mathbb{N}}$ in $A$. Amplified result $E$: $\{x_k\}$ has a convergent subsequence in $A$ (Bolzano–Weierstrass). The bridge: compact metric spaces are sequentially compact, and the limit is in $A$ since $A$ is closed. *Example:* every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence — a fundamental tool in real analysis.

Combine the conclusion with **an infinite-dimensional ambient space**. Property $D$: working in a Banach space $V$ instead of $\mathbb{R}^n$. Amplified result $E$: **Heine–Borel fails** — closed bounded subsets need not be compact. The bridge: F. Riesz's theorem — in $V$ infinite-dimensional, the closed unit ball is non-compact, and one must use weak compactness or other replacements. *Example:* this is *the* defining contrast between finite-dimensional and infinite-dimensional functional analysis — every infinite-dim phenomenon (Banach–Alaoglu, weak compactness, Rellich–Kondrachov) comes from working around the failure of Heine–Borel.

Combine the conclusion with **the assertion of a global extremum existence**. Property $D$: a continuous functional $J : A \to \mathbb{R}$ on a closed bounded $A \subseteq \mathbb{R}^n$. Amplified result $E$: $J$ has a global minimizer and maximizer. *Example:* every constrained optimization problem in finite dimensions with continuous objective and closed bounded constraint set has a solution. This is the bedrock of finite-dimensional optimization.

---

# Why Is It True

The theorem is the assembly of several pieces from compactness theory. Each piece has its own intuition; the assembly is by composition.

**Compact ⇒ bounded (forward, first half).** A compact set in a metric space is bounded because the open cover $\{B_k(x_0)\}_{k \in \mathbb{N}}$ (balls of radius $k$ around a fixed point $x_0$) has a finite subcover, so the set is contained in some ball $B_N(x_0)$ — bounded.

**Compact ⇒ closed (forward, second half).** $\mathbb{R}^n$ is Hausdorff (metric), so by [[Thm - Compact Subset of Hausdorff is Closed]], every compact subset is closed.

**Closed and bounded ⇒ compact (reverse).** This is the substantive direction, with three steps:

1. **$[0, 1]$ is compact.** Direct argument: let $\{U_i\}$ be an open cover and $S = \{s \in [0, 1] : [0, s] \text{ has a finite subcover}\}$. Show $S$ is an interval $[0, b]$, then $b = 1$ by an open-cover argument at $b$. (Bredon 7.9.)

2. **$[-N, N]^n$ is compact.** By the finite-product case of Tychonoff (Bredon 8.4–8.5): the product of finitely many compacts is compact. Iterating, $[-N, N]^n$ is compact for any $n$.

3. **Closed bounded $A$ is compact.** A bounded $A$ is contained in some $[-N, N]^n$. A closed subset of a compact is compact (by [[Thm - Closed Subset of Compact is Compact]]). Hence $A$ is compact.

The geometric picture: compactness in $\mathbb{R}^n$ is "geometric finiteness in a metric sense". Closed prevents escape via limit points; bounded prevents escape to infinity. Together they prevent every escape mechanism from a compact-friendly to a compact-hostile state. In infinite dimensions, "bounded" is too weak to prevent escape — the orthonormal basis $\{e_n\}$ in $\ell^2$ has unit norm (bounded) and the points are mutually at distance $\sqrt{2}$, so no subsequence converges; the escape is into "infinitely many independent directions", a possibility that does not exist in finite dimensions.

The reason the proof of $[0, 1]$ compact works: $[0, 1]$ is *connected* and *bounded*, with a least upper bound property. The supremum argument exploits both: connectedness ensures the set $S$ is an interval, the LUB property gives the sup, and the open cover lets one push past the sup to derive $b = 1$. The compactness of $[0, 1]$ is in this sense a packed-in consequence of the *completeness* of $\mathbb{R}$.

---

# What Makes This Hard

The non-obvious step is not in the *individual* compactness arguments — each is short and clean — but in *assembling the chain* in the right order: $[0, 1]$ compact (direct), then $[-N, N]^n$ compact (Tychonoff finite case), then closed-in-compact gives the general closed bounded case. The most common error is to try to prove "closed and bounded ⇒ compact" directly via an open-cover argument, which works in $[0, 1]$ but is needlessly complicated in $\mathbb{R}^n$. A second pitfall is to forget that *the converse fails in infinite dimensions* — closed bounded is *not* compact in $\ell^2, L^2, C[0, 1]$, and forgetting this is the most expensive error in functional analysis.

---

# Rederivation Scaffold

**High-level strategy:**
Compact ⇒ bounded: cover by nested balls, finite subcover gives a single bounding ball.
Compact ⇒ closed: $\mathbb{R}^n$ is Hausdorff metric, so [[Thm - Compact Subset of Hausdorff is Closed]] applies.
Closed bounded ⇒ compact: $[0, 1]$ compact (direct) → $[-N, N]^n$ compact (Tychonoff finite) → closed subset of compact is compact.

**Subgoal decomposition:**

1. **(Forward) Compact ⇒ bounded.** Cover by $\{B_k(0)\}_{k \in \mathbb{N}}$ (open balls of radius $k$); finite subcover gives boundedness.
   - *Hint:* The largest $k$ in the finite subcover bounds $A$.

2. **(Forward) Compact ⇒ closed.** $\mathbb{R}^n$ Hausdorff metric, apply [[Thm - Compact Subset of Hausdorff is Closed]].
   - *Hint:* Direct citation of the theorem.

3. **(Reverse) $[0, 1]$ is compact.** Direct argument via the supremum of "$[0, s]$ has a finite subcover".
   - *Hint:* Bredon 7.9. The connectedness of $[0, 1]$ and LUB of $\mathbb{R}$ are the inputs.

4. **(Reverse) $[-N, N]^n$ is compact.** Tychonoff finite product case.
   - *Hint:* Bredon 8.4–8.5. The finite product result is independent of choice.

5. **(Reverse) Closed bounded ⇒ compact.** $A \subseteq [-N, N]^n$ for some $N$ (by boundedness); $A$ is closed in $\mathbb{R}^n$, hence closed in $[-N, N]^n$ (subspace topology); closed in compact is compact by [[Thm - Closed Subset of Compact is Compact]].
   - *Hint:* Combine boundedness, closedness, and Tychonoff.

---

# Lemma Decomposition

> [!note]- Lemma 1: A compact subset of a metric space is bounded
> **Statement:** Let $(X, d)$ be a metric space and $A \subseteq X$ compact. Then $A$ is bounded: $A \subseteq B_R(x_0)$ for some $x_0 \in X, R > 0$.
>
> **Hint:** Cover $X$ by $\{B_k(x_0)\}_{k \in \mathbb{N}}$ and use compactness.
>
> **Why needed:** It is the "compact ⇒ bounded" direction.
>
> > [!note]- Full proof
> > Fix any $x_0 \in X$. The open balls $\{B_k(x_0)\}_{k \in \mathbb{N}}$ cover $X$ (every point has finite distance from $x_0$, so lies in some ball of integer radius). In particular they cover $A$. By compactness, extract a finite subcover: $A \subseteq B_{k_1}(x_0) \cup \cdots \cup B_{k_m}(x_0) \subseteq B_K(x_0)$ where $K = \max(k_1, \ldots, k_m)$. So $A$ is bounded.

> [!note]- Lemma 2: $[0, 1]$ is compact
> **Statement:** The closed interval $[0, 1]$ with the standard topology is compact.
>
> **Hint:** Let $\{U_i\}$ be an open cover and $S = \{s \in [0, 1] : [0, s] \text{ has a finite subcover from } \{U_i\}\}$. Show $\sup S = 1$ and is in $S$.
>
> **Why needed:** It is the base case for the reverse direction.
>
> > [!note]- Full proof
> > Let $\{U_i\}_{i \in I}$ be an open cover of $[0, 1]$. Set $S = \{s \in [0, 1] : [0, s] \text{ has a finite subcover from } \{U_i\}\}$. Then $0 \in S$ ($[0, 0] = \{0\}$ is covered by any $U_i \ni 0$, taking just that one), so $S$ is nonempty and bounded above by $1$. Let $b = \sup S$.
> >
> > *Claim: $b \in S$.* Choose $U_{i_0} \ni b$ (some open in the cover); $U_{i_0}$ contains an interval $(b - \epsilon, b + \epsilon) \cap [0, 1]$. Then $b - \epsilon/2 < b$, so by definition of $\sup$, there is $s \in S$ with $s > b - \epsilon/2$. The finite subcover for $[0, s]$, together with $U_{i_0}$, covers $[0, b]$ (the gap $[s, b]$ is inside $U_{i_0}$). So $b \in S$.
> >
> > *Claim: $b = 1$.* Suppose $b < 1$. With $U_{i_0}$ as above, $(b, b + \epsilon) \cap [0, 1]$ is nonempty (since $b < 1$ and $b + \epsilon$ could exceed 1, but the intersection still contains points $b' \in (b, \min(1, b + \epsilon))$). The finite subcover for $[0, b]$ plus $U_{i_0}$ covers $[0, b']$, so $b' \in S$, contradicting $b = \sup S$.
> >
> > So $b = 1$ and $b \in S$, i.e., $[0, 1]$ has a finite subcover from $\{U_i\}$.

> [!note]- Lemma 3: A closed bounded subset of $\mathbb{R}^n$ is contained in some compact cube
> **Statement:** Let $A \subseteq \mathbb{R}^n$ be bounded. Then there is $N > 0$ with $A \subseteq [-N, N]^n$, and $[-N, N]^n$ is compact (finite product of compact intervals).
>
> **Hint:** Boundedness gives some bounding box; products of compacts are compact (Bredon 8.5).
>
> **Why needed:** It puts $A$ inside a known-compact superset.
>
> > [!note]- Full proof
> > Boundedness of $A$ means $A \subseteq B_R(0)$ for some $R$. Inside any ball $B_R(0)$ in $\mathbb{R}^n$, every coordinate is bounded by $R$ in absolute value. So $A \subseteq [-R, R]^n =: [-N, N]^n$ with $N = R$.
> >
> > By Lemma 2, $[-N, N]$ is compact (homeomorphic to $[0, 1]$ via the affine map). By Tychonoff for finite products (Bredon 8.5), $[-N, N]^n$ is compact.

---

# Formal Proof

> [!note]- Complete formal proof
>
> Let $A \subseteq \mathbb{R}^n$.
>
> **($\Rightarrow$) Compact ⇒ closed and bounded.**
>
> *Bounded:* By Lemma 1 ($\mathbb{R}^n$ is a metric space), $A$ is bounded.
>
> *Closed:* $\mathbb{R}^n$ is Hausdorff (as a metric space, any two distinct points have disjoint balls). By [[Thm - Compact Subset of Hausdorff is Closed]], $A$ is closed.
>
> **($\Leftarrow$) Closed and bounded ⇒ compact.**
>
> By Lemma 3, $A \subseteq [-N, N]^n$ for some $N > 0$, and $[-N, N]^n$ is compact.
>
> $A$ is closed in $\mathbb{R}^n$ by hypothesis. Since $[-N, N]^n \subseteq \mathbb{R}^n$ has the subspace topology, $A$ is closed in $[-N, N]^n$ as well (intersection of a closed set in $\mathbb{R}^n$ with $[-N, N]^n$ is closed in the subspace).
>
> By [[Thm - Closed Subset of Compact is Compact]], the closed subset $A$ of the compact $[-N, N]^n$ is compact.
>
> So $A$ compact $\iff$ $A$ closed and bounded. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Extreme Value Theorem on bounded closed regions.** Let $f : K \to \mathbb{R}$ be continuous on a closed bounded $K \subseteq \mathbb{R}^n$. By this theorem, $K$ is compact. By [[Thm - Continuous Image of a Compact Space]], $f(K)$ is compact in $\mathbb{R}$. By this theorem in dimension 1, $f(K)$ is closed and bounded, hence has a maximum and minimum, both attained. The application is the foundational result of finite-dimensional optimization.

**Bolzano–Weierstrass via Heine–Borel.** A bounded sequence $\{x_n\}$ in $\mathbb{R}^n$ takes values in some compact $[-N, N]^n$. A compact metric space is sequentially compact (by the equivalence in [[Def - Compact Space]] applied in first-countable settings), so $\{x_n\}$ has a convergent subsequence. The application is the classical sequential characterization of compactness in $\mathbb{R}^n$.

**F. Riesz's failure of Heine–Borel.** In an infinite-dimensional Banach space, the closed unit ball is closed and bounded but *not* compact. Proof sketch: by F. Riesz's lemma, one can construct a sequence $\{x_n\}$ with $\lVert x_n \rVert = 1$ and $\lVert x_n - x_m \rVert \geq 1/2$ for $n \neq m$. Such a sequence has no convergent subsequence (the points are mutually $\geq 1/2$ apart), so the unit ball is not sequentially compact, hence not compact (in a metric space). The application is *the* defining contrast between finite-dim and infinite-dim functional analysis.

**The Mountain Pass Theorem and compactness conditions.** In infinite-dim variational problems, the Heine–Borel-style compactness fails, and one must impose **Palais–Smale conditions** (every Palais–Smale sequence has a convergent subsequence) to restore compactness for critical-point theory. This is the engineering workaround for Heine–Borel's failure, used throughout PDE and calculus of variations.

---

# Bridges

- **[[Thm - Closed Subset of Compact is Compact]]** — half of the proof. Closed subsets of $[-N, N]^n$ are compact, which (with Tychonoff finite product) gives closed bounded ⇒ compact.

- **[[Thm - Compact Subset of Hausdorff is Closed]]** — the other half (compact ⇒ closed in $\mathbb{R}^n$, since $\mathbb{R}^n$ is Hausdorff).

- **[[Thm - Continuous Image of a Compact Space]]** — combines with Heine–Borel to give the Extreme Value Theorem in $\mathbb{R}^n$.

- **Tychonoff's finite product theorem** — gives compactness of $[-N, N]^n$ from compactness of $[-N, N]$. The arbitrary-index Tychonoff theorem (in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]) requires the Axiom of Choice; the finite-product version does not.

- **F. Riesz's theorem** — the limit of Heine–Borel. In infinite-dim normed spaces, closed bounded ≠ compact; the closed unit ball is not compact. This is the defining feature of infinite-dim analysis.

- **Bolzano–Weierstrass** — sequential compactness in $\mathbb{R}^n$. Equivalent to Heine–Borel via the first-countability of metric spaces.

- **Banach–Alaoglu** — the *workaround* for the failure of Heine–Borel in infinite-dim. The closed unit ball of $V^*$ is *weak-$*$ compact* even when not norm-compact. This is the "right" compactness theorem for infinite-dim duals.

---

# Unlocked by This

> [!tip] **Extreme Value Theorem** *(from Real Analysis)*
> Continuous functions on closed bounded subsets of $\mathbb{R}^n$ attain their maximum and minimum.

> [!tip] **Bolzano–Weierstrass Theorem** *(from Real Analysis)*
> Every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence.

> [!tip] **F. Riesz's Theorem on Infinite-Dim Unit Balls** *(from Functional Analysis)*
> In an infinite-dim normed space, the closed unit ball is not compact. This is the limit of Heine–Borel — the failure of the natural finite-dim analog forces the development of weak topologies and infinite-dim compactness substitutes.

> [!tip] **Banach–Alaoglu Theorem** *(from Functional Analysis)*
> The closed unit ball of the dual $V^*$ of a normed space $V$ is **weak-$*$ compact**. The replacement for Heine–Borel in infinite-dim, achieved by changing the topology to weak-$*$. The proof uses Tychonoff's theorem in the full (arbitrary-index) form.

> [!tip] **Compactness in PDE and the Direct Method** *(from PDE Theory)*
> The direct method of the calculus of variations extracts minimizers from minimizing sequences via compactness. In infinite-dim function spaces, this requires weak compactness (Banach–Alaoglu, Rellich–Kondrachov) since Heine–Borel fails. Every successful PDE existence proof navigates the failure of Heine–Borel in infinite dimensions.
