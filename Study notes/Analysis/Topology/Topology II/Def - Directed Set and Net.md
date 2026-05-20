---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Neighbourhood and Neighbourhood Basis"
tags: [analysis, topology]
---

# Notation

Throughout, $D$ denotes a directed set, with elements written $\alpha, \beta, \gamma, \delta, \tau, \ldots$, and partial order $\leq$. The expression $\beta \geq \alpha$ means $\beta$ is "later" than $\alpha$ in $D$. A net is written $\Phi : D \to X$ or, suggestively, $\{x_\alpha\}_{\alpha \in D}$ where $x_\alpha = \Phi(\alpha)$. The set $\mathbb{N}$ of natural numbers, with its usual ordering, is the prototype directed set; a sequence is a net indexed by $\mathbb{N}$. For a point $x \in X$, $\mathcal{N}(x)$ denotes the set of all open neighbourhoods of $x$. The full registry of symbols is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Axiom Motivation

In a metric space, sequences are sufficient to detect all topological phenomena: a point $x$ is in the closure of $A$ if and only if some sequence in $A$ converges to $x$; a function $f$ is continuous at $x$ if and only if for every sequence $x_n \to x$, $f(x_n) \to f(x)$. The combinatorics of $\mathbb{N}$ — countable, linearly ordered, cofinal — exactly matches the combinatorics of the metric topology, where every point has a *countable* neighbourhood basis (the balls of radius $1/n$). In a general topological space this matching breaks down: there exist points $x \in \overline{A}$ with no sequence in $A$ converging to $x$, and there exist functions $f$ that preserve all sequential limits yet are not continuous. The pathology lies in having no countable neighbourhood basis — there are too many neighbourhoods to thread by an $\mathbb{N}$-indexed sequence.

The natural fix is to allow indexing by something larger than $\mathbb{N}$. What is the right replacement? Whatever it is, it must support the same operations we use on sequences: comparing two indices to see which is "later", taking pairs of indices and finding a common "later" index, and defining "eventually" via final segments of indices. The minimal structure that supports these operations is a **directed set**: a set $D$ with a partial order $\leq$ in which any two elements have an upper bound — given $\alpha, \beta \in D$, there is $\gamma \in D$ with $\gamma \geq \alpha$ and $\gamma \geq \beta$.

Why partial order rather than total order? Because the natural indexing in topology is not linear. The canonical example: the directed set of all open neighbourhoods of a point $x \in X$, ordered by *reverse inclusion* — $U \leq V$ iff $U \supseteq V$ (smaller neighbourhoods are "later"). This is a partial order: two neighbourhoods $U, V$ need not be nested either way, but their *intersection* $U \cap V$ is a smaller neighbourhood than either, providing an upper bound in the directed sense. This is the directed set we use to prove "$x \in \overline{A}$ iff some net in $A$ converges to $x$" — pick a point of $A$ in each smaller and smaller neighbourhood of $x$.

Why no upper bound requirement on infinite subsets — only finite (in fact, pairs)? Because the analogue of "eventually" only needs to talk about finite collections of preceding indices. To say "$\Phi$ is eventually in $U$" means "there is some $\alpha_0$ such that for all $\beta \geq \alpha_0$, $\Phi(\beta) \in U$". Combining "eventually in $U$" and "eventually in $V$" to get "eventually in $U \cap V$" requires finding a common $\alpha_0$ for the two thresholds; an upper bound of *two* elements suffices, and by induction of any finite collection. We never need to bound infinite sets — finite-pair bounds are exactly the right level of strictness.

So a **net** in $X$ is just a function $\Phi : D \to X$ from a directed set $D$ to $X$. Sequences are the special case $D = \mathbb{N}$. The directed sets that come up most often in topology are:

1. **$\mathbb{N}$** — recovering sequences. Useful for first-countable spaces.

2. **The neighbourhood filter at a point**, ordered by reverse inclusion. Used to prove $x \in \overline{A}$ via nets in $A$; the canonical "convergence" directed set.

3. **Finite subsets of an arbitrary set $S$**, ordered by inclusion. Used in summation: a "net of partial sums" indexed by finite subsets generalizes the idea of summing an uncountable family. The series $\sum_{i \in I} a_i$ converges iff the net of partial sums converges, which is a useful definition when $I$ is uncountable.

4. **Cofinal subsets of a directed set** — restricting a net to a smaller indexing.

5. **Products of two directed sets**, ordered componentwise. Used to combine two nets into one.

The notion of "eventually in" and "frequently in" recapitulates the sequential language: $\Phi$ is **eventually in $A$** if there exists $\alpha_0$ such that $\Phi(\beta) \in A$ for all $\beta \geq \alpha_0$, and **frequently in $A$** if for every $\alpha$ there exists $\beta \geq \alpha$ with $\Phi(\beta) \in A$. "Eventually" is the dual of "frequently in the complement": $\Phi$ is eventually in $A$ iff it is *not* frequently in $X \setminus A$. These are the key locutions for net convergence.

A pragmatic point: directed-set-based indexing makes everything that worked for sequences in metric spaces work in arbitrary spaces. The only price is that "subsequence" is too rigid a notion — we need [[Def - Subnet and Universal Net|subnets]], which generalize subsequences in a non-obvious way. But the basic apparatus — convergence, eventually/frequently, closure-via-nets, continuity-via-nets — translates *mutatis mutandis*.

---

# The Definition

Let $X$ be a topological space.

**Directed set.** A **directed set** is a set $D$ equipped with a partial order $\leq$ such that for any two elements $\alpha, \beta \in D$, there exists $\gamma \in D$ with $\gamma \geq \alpha$ and $\gamma \geq \beta$. Equivalently, every finite subset of $D$ has an upper bound (this follows by induction from the pairwise condition).

**Net.** A **net** in $X$ is a function $\Phi : D \to X$ from a directed set $D$ to $X$. We often denote the net by $\{x_\alpha\}_{\alpha \in D}$ where $x_\alpha = \Phi(\alpha)$.

**Sequence as a special case.** A **sequence** in $X$ is a net indexed by $D = \mathbb{N}$ with the usual ordering. So every sequence is a net, but not every net is a sequence.

**Eventually in / frequently in.** Let $\Phi : D \to X$ be a net and let $A \subseteq X$. We say $\Phi$ is:

- **eventually in $A$** if there exists $\alpha_0 \in D$ such that $\Phi(\beta) \in A$ for every $\beta \geq \alpha_0$;
- **frequently in $A$** if for every $\alpha \in D$ there exists $\beta \geq \alpha$ with $\Phi(\beta) \in A$.

These notions are duals: $\Phi$ is eventually in $A$ if and only if $\Phi$ is *not* frequently in $X \setminus A$.

---

# Relate to Other Fields / Compression

The directed-set structure is exactly the structure of a **filter base** — though in topology it is usually presented in the "net" form (functions out of a directed set) rather than the "filter" form (collections of subsets directed by reverse inclusion). The two formalisms are equivalent and used interchangeably depending on the author's preference. **Bourbaki and the French school** prefer filters; **Munkres, Bredon, and the American school** prefer nets. The translation: a net $\Phi : D \to X$ defines a filter $\mathcal{F}_\Phi = \{A \subseteq X : \Phi \text{ is eventually in } A\}$ on $X$; conversely, a filter on $X$ defines (via Tukey's theorem) a net up to subnet equivalence.

In **probability theory**, the analogue of a net is a *generalised sequence* indexed by a directed set, and the analogue of convergence is convergence of expectations along the directed indexing. Martingales are sequences (nets indexed by $\mathbb{N}$ or $\mathbb{R}_{\geq 0}$); martingale convergence theorems use the directed structure of the indexing. In **stochastic calculus**, one uses nets of partitions (refinement-ordered) to define stochastic integrals.

In **category theory**, the colimit of a functor from a *filtered category* is the categorical analogue of "limit of a net". A filtered category is a categorification of a directed set, and filtered colimits commute with finite limits in many settings (e.g. in the category of sets, or in any locally finitely presentable category).

In **order theory and lattice theory**, the structure of a directed set is studied for its own sake. Every poset has a *directed completion*, and the theory of continuous lattices (Scott topology) places directed sets at the center.

---

# Examples / Corollaries

**Is an instance — $D = \mathbb{N}$.** The natural numbers with their usual ordering form a directed set: given $m, n \in \mathbb{N}$, $\max(m, n)$ is an upper bound. A net indexed by $\mathbb{N}$ is exactly a sequence. Sequences are nets, but not vice versa.

**Is an instance — the neighbourhood filter at a point.** Let $X$ be a topological space and $x \in X$. The set $\mathcal{N}(x)$ of all open neighbourhoods of $x$, ordered by *reverse inclusion* ($U \leq V$ iff $U \supseteq V$), is a directed set: given $U, V \ni x$, their intersection $U \cap V$ is also an open neighbourhood of $x$, smaller than both, hence "later" in the order. This is the directed set used to prove the closure-via-nets characterisation: pick $\Phi(U)$ to be any element of $A \cap U$, and the resulting net $\Phi : \mathcal{N}(x) \to A$ converges to $x$.

**Is an instance — finite subsets of a set $S$, ordered by inclusion.** Given a set $S$ (say, an index set for a sum), the collection $\text{Fin}(S)$ of finite subsets is directed by inclusion: given two finite subsets $F_1, F_2 \subseteq S$, their union $F_1 \cup F_2$ is a finite subset containing both. A net indexed by $\text{Fin}(S)$ is exactly a "partial sum" pattern: for a family $\{a_s\}_{s \in S}$, the net $F \mapsto \sum_{s \in F} a_s$ is the natural directed-set generalisation of summation. The unordered series $\sum_{s \in S} a_s$ converges iff this net converges.

**Is an instance — products of directed sets.** If $D, D'$ are directed sets, so is $D \times D'$ with the componentwise order $(\alpha, \alpha') \leq (\beta, \beta')$ iff $\alpha \leq \beta$ and $\alpha' \leq \beta'$. The product directed set is used to combine two nets — given $\Phi : D \to X$ and $\Phi' : D' \to X$, the product directed set indexes a "joint" net.

**Is NOT an instance of a directed set — the integers $\mathbb{Z}$ with the *strict* order $<$.** The strict order is not reflexive, so it is not even a partial order. The correct notion is the non-strict order $\leq$.

**Is NOT an instance of a directed set — $\{a, b\}$ with $a$ and $b$ incomparable and no third element.** Here $\{a, b\}$ is a poset but $a, b$ have no common upper bound, so it is not directed. Any partial order with a maximal antichain that has no common upper bound fails directedness.

**Is NOT a "useful" directed set — a set with a maximum element $M$.** Such a poset is directed (the max is an upper bound for everything), but a net indexed by it is essentially trivial: once you reach $M$, the net is "constant from $M$ onward". Useful directed sets are those that "keep going" — have no maximum, so the net keeps being indexed at later and later stages.

**Corollary — every finite subset of a directed set has an upper bound.** By induction on the size: for the base case (one element), the element itself is an upper bound. For the inductive step, given $\alpha_1, \ldots, \alpha_n$, find an upper bound $\beta$ for $\alpha_1, \ldots, \alpha_{n-1}$ by hypothesis, then an upper bound $\gamma$ for $\beta$ and $\alpha_n$. Then $\gamma$ is an upper bound for all.

**Corollary — sequences are special nets, but the converse is false.** Every sequence is a net (indexed by $\mathbb{N}$), but in a non-first-countable space — say $\omega_1 + 1$ with the order topology — there exist nets (indexed by the neighbourhood filter of $\omega_1$) that have no sequential analogue.

**Corollary — the directed set of finite subsets of an uncountable set has uncountable cofinality.** A cofinal subset of $\text{Fin}(S)$ for uncountable $S$ must contain finite subsets exhausting $S$, and there are uncountably many. So nets indexed here cannot be reindexed to sequences when $S$ is uncountable — this is the technical reason for needing nets when working with the weak topology on an infinite-dimensional Banach space.

**Calibration check.** Verify that: (i) the directed set "finite subsets of $\mathbb{N}$ ordered by inclusion" is *not* a chain (the subsets $\{1\}$ and $\{2\}$ are incomparable); (ii) the directed set of "open neighbourhoods of $0 \in \mathbb{R}$" is order-isomorphic to the directed set of positive real numbers with $a \leq b$ meaning $a \geq b$, by mapping each $\varepsilon$-ball to $\varepsilon$; (iii) the directed set $\omega_1$ (the first uncountable ordinal) has *no* countable cofinal subset.

---

# Unlocked by This

> [!tip] **Net Convergence** *(this topic)*
> A net $\{x_\alpha\}$ converges to $x$ if it is eventually in every open neighbourhood of $x$. See [[Def - Net Convergence]]. This is the generalisation of sequential convergence to arbitrary topological spaces.

> [!tip] **Subnets and Universal Nets** *(this topic)*
> A "subnet" of a net is the analogue of a "subsequence", but defined more flexibly using a *final function* rather than a strictly increasing function. A net is **universal** if for every $A \subseteq X$ it is eventually in $A$ or eventually in $X \setminus A$. See [[Def - Subnet and Universal Net]]. Universal nets are the key technical tool for the compactness equivalence "every net has a convergent subnet".

> [!tip] **Filter Convergence** *(from Topology / Set Theory)*
> A **filter** on $X$ is a nonempty collection of subsets of $X$ closed under finite intersection and supersets, not containing $\emptyset$. Filter convergence is the alternative-but-equivalent formalism for what nets do: a filter converges to $x$ if every neighbourhood of $x$ is in the filter. The Tukey theorem establishes the equivalence between nets and filters.
