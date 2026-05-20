---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
  - "Def - Closure, Interior, and Boundary"
  - "Def - Directed Set and Net"
  - "Def - Net Convergence"
  - "Def - Subnet and Universal Net"
tags: [analysis, topology]
---

# Notation

Throughout, $X$ is a topological space. A **cover** of $X$ is a collection $\mathcal{U} = \{U_\alpha\}_{\alpha \in A}$ of subsets with $X = \bigcup_\alpha U_\alpha$; it is an **open cover** if every $U_\alpha$ is open. A **subcover** is a sub-collection $\{U_\alpha\}_{\alpha \in A'}$, $A' \subseteq A$, that is still a cover; a **finite subcover** has $A'$ finite. A collection of sets has the **finite intersection property** (FIP) if every finite subcollection has nonempty intersection. The notation $K \subseteq X$ usually denotes a compact subset. The full registry of symbols is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Axiom Motivation

The intuition we want to capture is "topological finiteness" — a space that, while possibly infinite as a set, behaves *finitely* in some structural sense relevant to analysis. The motivating examples are the closed intervals $[a, b]$ and closed balls $\overline{B}(x, r) \subset \mathbb{R}^n$: they are infinite point-sets, but they are *small* in a useful way. On $[0, 1]$, every continuous real function attains its maximum and minimum (extreme value theorem); every sequence has a convergent subsequence (Bolzano–Weierstrass); every continuous function is uniformly continuous; every open cover has a finite subcover (Heine–Borel). These four properties express a single underlying notion of "smallness", and we want to axiomatize it.

The chosen definition is "every open cover has a finite subcover". To see why this is the right level, think about what would fail without compactness. In $\mathbb{R}$ (not compact), the open cover $\{(-n, n) : n \in \mathbb{N}\}$ has no finite subcover — no finitely many intervals can exhaust all of $\mathbb{R}$. In $(0, 1)$ (not compact), the open cover $\{(1/n, 1) : n \in \mathbb{N}\}$ has no finite subcover — finitely many of these intervals can never reach down to $0$. These two failure modes — *escape to infinity* and *escape to the boundary* — are exactly what compactness rules out. A compact space is one where these escape mechanisms are eliminated *uniformly* across all open covers, simultaneously.

The seeming oddness of the definition — it is about *covers*, not about *points or sequences* — is what makes it powerful. By requiring control over arbitrary open covers, we get a property that propagates beautifully under continuous maps: the preimage of an open cover under a continuous function is an open cover, so a finite subcover pulls back, giving continuity-of-compactness. And by stating in terms of opens, compactness is intrinsic to the topology — no metric, no countability, no algebraic structure required.

But the open-cover definition is hard to *use* directly. So we develop two equivalent formulations. First, by taking complements, "every open cover has a finite subcover" translates to "every collection of closed sets with the finite intersection property has nonempty total intersection" — the **FIP formulation**. This is the form that converts the *covering* picture (which is about exhaustion) to the *intersection* picture (which is about existence of a common point). It is the form you use to prove Tychonoff's theorem (the product of compact spaces is compact) and to prove existence theorems via "there is a point in every closed set in this family".

Second, by passing to nets, we get the **net subnet formulation**: $X$ is compact iff every net in $X$ has a convergent subnet. This is the form that captures what compactness *does* in analysis. When you have a sequence and want to extract a convergent subsequence (the Bolzano–Weierstrass move), what you are really using is the net-subnet form of compactness. In metric (or more generally first-countable) spaces this specializes to "every sequence has a convergent subsequence", which is *sequential compactness*. In general spaces, sequential compactness and compactness are different (see [[Def - Sequentially Compact Space]]) — but the net-subnet form is always equivalent to compactness, no matter the space. This is why nets were invented: to give a *fully general* "subsequence-style" characterisation of compactness.

The proof of the equivalence is non-trivial — it uses the existence of universal subnets ([[Thm - Every Net Has a Universal Subnet]]), which itself uses Zorn's lemma. The chain (open cover) ⇒ (universal nets converge) ⇒ (every net has a convergent subnet) ⇒ (FIP) ⇒ (open cover) closes the loop. This is why all three definitions are "fundamental" — there is no single one that is obviously the "real" definition; they are three equivalent perspectives, each useful in different contexts.

What does compactness buy? The two most important consequences: the **extreme value theorem** (continuous real-valued functions on compact spaces attain their max and min) and the **closed-map property** (continuous maps from compact to Hausdorff spaces are closed, hence continuous bijections between such are homeomorphisms). The first underlies every existence proof for minimisers in calculus of variations, optimal control, statistical estimation, and analysis. The second is the engine of every "quotient space is homeomorphic to so-and-so" argument in topology. Almost every existence result in analysis routes through compactness somewhere.

A point about *which compactness to use when*. If you are proving something has a finite covering structure — say, that a function is uniformly continuous on a space — use the open-cover form. If you are proving existence of a fixed point or a common point of some closed sets, use FIP. If you are extracting a subsequence and passing to a limit (the dominant pattern in analysis), use the net-subnet form. The three forms are not redundant; they are calibrated for different purposes, and fluency requires knowing all three.

A warning: in $\mathbb{R}^n$, the Heine–Borel theorem makes compactness checkable as "closed and bounded", and most students learn compactness this way. But Heine–Borel is *specific to finite-dimensional normed spaces*. In infinite-dimensional Banach spaces, the closed unit ball is bounded but *not* compact — this is **F. Riesz's theorem**. So mistaking "closed and bounded" for compactness is the most expensive error in functional analysis. The abstract definitions (open cover, FIP, net subnet) survive in all settings; "closed and bounded" survives only in finite dimensions.

---

# The Definition

Let $X$ be a topological space.

**Compact space (open-cover formulation).** $X$ is **compact** if every open cover of $X$ has a finite subcover. That is, whenever $X = \bigcup_{\alpha \in A} U_\alpha$ with each $U_\alpha$ open, there exists a finite subset $A' \subseteq A$ with $X = \bigcup_{\alpha \in A'} U_\alpha$.

**Equivalent formulations.** The following are equivalent for a topological space $X$:

1. Every open cover of $X$ has a finite subcover (open-cover compactness).
2. Every collection of closed subsets of $X$ with the **finite intersection property** has nonempty total intersection.
3. Every net in $X$ has a convergent subnet.
4. Every universal net in $X$ converges.

The equivalence (1) ⇔ (2) is immediate by taking complements. The equivalences (3) ⇔ (4) ⇔ (1) use the existence of universal subnets and Zorn's lemma; see [[Thm - Every Net Has a Universal Subnet]] and the proof in §7.14 of Bredon.

**Compact subset.** A subset $K \subseteq X$ is **compact** if $K$ is compact as a topological space with the subspace topology. Equivalently, every cover of $K$ by open subsets of $X$ has a finite subcover.

---

# Relate to Other Fields / Compression

The "true name" of compactness in **analysis** is the net-subnet form: every net has a convergent subnet, and in metric spaces, every sequence has a convergent subsequence (Bolzano–Weierstrass). This is what you actually deploy when proving existence theorems — minimisers, fixed points, eigenvectors, MLE. The open-cover form is what you deploy when proving properties that require *uniformity* (uniform continuity, partition of unity, Lebesgue number lemma).

In **algebraic geometry**, the analogue of compactness is **properness**: a morphism of schemes $f : X \to Y$ is proper if it is separated, of finite type, and universally closed. The motivating example is "compactness over a point" — a scheme over $\operatorname{Spec} k$ is proper iff it is "complete", the algebraic-geometric notion of being compact. Projective varieties are proper; affine varieties (other than points) are not.

In **probability and measure theory**, the relevant compactness is **tightness**: a family of probability measures on a complete separable metric space is tight if for every $\varepsilon > 0$ there is a compact $K$ with $\mu(K) > 1 - \varepsilon$ for every $\mu$ in the family. **Prokhorov's theorem** says tight families are precompact in the weak topology. The mechanism is the same as topological compactness — no "escape of mass to infinity".

In **functional analysis**, the **Banach–Alaoglu theorem** is the keystone compactness result: the closed unit ball of the dual of a normed space is compact in the weak-$*$ topology. The proof uses Tychonoff (product of compacts is compact) on a product of intervals indexed by the original space. This is the source of every "extract a weakly convergent subsequence" argument in PDE, calculus of variations, and stochastic analysis.

In **logic**, the **compactness theorem** of first-order logic — a set of first-order sentences is satisfiable iff every finite subset is — is a literal compactness statement about the Stone space of complete theories. The bridge between topological and logical compactness is mediated by ultrafilters / universal nets.

---

# Examples / Corollaries

**Is an instance — the unit interval $[0, 1]$.** The proof: let $\mathcal{U}$ be an open cover of $[0, 1]$, and consider $S = \{s \in [0, 1] : [0, s] \text{ has a finite subcover from } \mathcal{U}\}$. Then $S$ is nonempty ($0 \in S$, covered by any single open containing $0$), bounded above by $1$. Let $b = \sup S$. Show $b \in S$ (continuity: pick an open $U \in \mathcal{U}$ containing $b$; $U$ contains $[a, b]$ for some $a < b$; add $U$ to the finite cover of $[0, a]$). Show $b = 1$ (if $b < 1$, the same open $U$ extends the cover slightly past $b$, contradicting maximality of $b$). See [[Ex - The unit interval is compact]].

**Is an instance — the $n$-sphere $S^n$.** $S^n$ is a closed bounded subset of $\mathbb{R}^{n+1}$, hence compact by Heine–Borel. More intrinsically, $S^n$ is a continuous image of $[0, 1]^n$ under a suitable map, and continuous images of compact spaces are compact.

**Is an instance — finite topological spaces.** Any finite topological space $X = \{x_1, \ldots, x_n\}$ is compact: an open cover already consists of finitely many sets, so it is its own finite subcover. (This works regardless of the topology.)

**Is an instance — any set with the cofinite topology.** In the cofinite topology on a set $X$, the open sets are $\emptyset$ and complements of finite sets. Given an open cover $\mathcal{U}$, pick any $U \in \mathcal{U}$. Then $X \setminus U$ is finite, and each of its points is covered by some element of $\mathcal{U}$; together with $U$, finitely many of these elements form a finite subcover. So *every* set with the cofinite topology is compact. Note this includes uncountable sets like $\mathbb{R}$ — but the cofinite topology on $\mathbb{R}$ is much coarser than the standard topology, so this doesn't conflict with $\mathbb{R}$ being non-compact in the usual topology.

**Is NOT an instance — $\mathbb{R}$ in the standard topology.** The open cover $\{(-n, n) : n \in \mathbb{N}\}$ has no finite subcover. Alternatively, the sequence $x_n = n$ has no convergent subsequence (any subsequence diverges to $\infty$), failing the sequential form of compactness.

**Is NOT an instance — the open interval $(0, 1)$.** The cover $\{(1/n, 1) : n \in \mathbb{N}\}$ has no finite subcover (any finite sub-collection has a smallest $1/n$, missing $(0, 1/n)$). Alternatively, the sequence $x_n = 1/n$ has no convergent subsequence in $(0, 1)$ — every subsequence converges to $0$, which is not in $(0, 1)$.

**Is NOT an instance — an infinite discrete space.** $\mathbb{N}$ with the discrete topology: the open cover $\{\{n\} : n \in \mathbb{N}\}$ has no finite subcover. More dramatically, every singleton is open, so any partition by singletons is an open cover. This is the prototype of "non-compact discrete".

**Is NOT an instance — the closed unit ball in an infinite-dimensional Banach space.** F. Riesz's theorem: the closed unit ball of a normed space is compact iff the space is finite-dimensional. So the unit ball of $\ell^2$, $L^2[0, 1]$, $C[0, 1]$, etc., is closed and bounded but NOT compact. The failure mode is the standard orthonormal basis $\{e_n\}$ in $\ell^2$, which has no convergent subsequence (any two $e_n, e_m$ are at distance $\sqrt{2}$). This is the *escape to orthogonal directions* — analogous to escape to infinity, but using up dimensions.

**Corollary — continuous image of compact is compact.** If $f : X \to Y$ is continuous and $X$ is compact, then $f(X)$ is compact. Proof: pull back an open cover of $f(X)$ via $f$ to get an open cover of $X$; extract a finite subcover by compactness of $X$; push forward to get a finite subcover of $f(X)$. See [[Thm - Continuous Image of a Compact Space]].

**Corollary — closed subset of compact is compact.** If $X$ is compact and $A \subseteq X$ is closed, then $A$ is compact. Proof: take an open cover of $A$ (by opens of $X$); throw in $X \setminus A$ (open since $A$ is closed) to get an open cover of $X$; extract a finite subcover; restrict back to $A$.

**Corollary — compact subset of Hausdorff is closed.** If $X$ is Hausdorff and $A \subseteq X$ is compact, then $A$ is closed. Proof: take $x \notin A$. For each $a \in A$, by Hausdorff there are disjoint opens $U_a \ni a, V_a \ni x$. The $U_a$ cover $A$; extract a finite subcover $U_{a_1}, \ldots, U_{a_n}$; let $V = V_{a_1} \cap \ldots \cap V_{a_n}$. Then $V$ is an open neighbourhood of $x$ disjoint from $A$. Hence $X \setminus A$ is open, so $A$ is closed.

**Corollary — extreme value theorem.** If $X$ is compact and $f : X \to \mathbb{R}$ is continuous, then $f$ attains its maximum and minimum. Proof: $f(X)$ is compact in $\mathbb{R}$ (continuous image of compact), hence closed and bounded by Heine–Borel, hence contains $\sup f(X)$ and $\inf f(X)$.

**Calibration check.** Three equivalent definitions of compactness in mind, verify that: (i) $[0, 1]^n$ is compact via Tychonoff (product of compacts is compact — needs Topology III), giving Heine–Borel; (ii) the FIP formulation is what you use to prove Tychonoff; (iii) the net-subnet form is what you use to extract a weakly convergent subsequence in functional analysis. Each formulation is calibrated for a class of arguments.

---

# Unlocked by This

> [!tip] **Heine–Borel Theorem** *(this topic)*
> A subset of $\mathbb{R}^n$ is compact if and only if it is closed and bounded. See [[Thm - Heine–Borel Theorem]]. This collapses the abstract compactness machinery to a calculable hand-check in $\mathbb{R}^n$, but be aware: it fails in infinite-dimensional spaces.

> [!tip] **Tychonoff's Theorem** *(from Topology III)*
> The arbitrary product of compact spaces is compact, in the product topology. **Tychonoff's theorem** is equivalent to the Axiom of Choice and is the foundational compactness result in topology. See [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

> [!tip] **Banach–Alaoglu** *(from Functional Analysis)*
> The closed unit ball of the dual $V^*$ of a normed space $V$ is compact in the weak-$*$ topology. Proof: embed the ball in the compact product $\prod_x [-\|x\|, \|x\|]$ (one factor per $x \in V$); apply Tychonoff. This is *the* compactness result in functional analysis.

> [!tip] **Prokhorov's Theorem** *(from Probability)*
> A family of probability measures on a complete separable metric space is precompact in the weak topology iff it is **tight** — for every $\varepsilon$ there is a compact $K$ such that every measure assigns mass $> 1 - \varepsilon$ to $K$. See [[Thm - Prokhorov's Theorem]]. The probabilistic instance of compactness.
