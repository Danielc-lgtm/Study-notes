---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Neighbourhood and Neighbourhood Basis"
  - "Def - Directed Set and Net"
tags: [analysis, topology]
---

# Notation

Throughout, $X$ is a topological space, $D$ is a directed set, and $\Phi : D \to X$ is a net, written $\{x_\alpha\}_{\alpha \in D}$ where $x_\alpha = \Phi(\alpha)$. The expression $x_\alpha \to x$ means $\Phi$ converges to $x$. The set of open neighbourhoods of $x$ is $\mathcal{N}(x)$. The notation $\beta \geq \alpha$ in $D$ means $\beta$ is later (or equal) than $\alpha$. The full registry of symbols is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Axiom Motivation

We have built up the apparatus: [[Def - Directed Set and Net|directed sets and nets]] generalize $\mathbb{N}$ and sequences to indexing structures rich enough to thread the neighbourhood filter of every point in an arbitrary topological space. The next step is to import the definition of convergence — and ideally to do so in such a way that the metric-space intuition for "sequence convergence" is *literally* the special case of the new definition.

In metric space $X$ with metric $d$, a sequence $x_n \to x$ means: for every $\varepsilon > 0$, there exists $N$ such that $d(x_n, x) < \varepsilon$ for all $n \geq N$. Reading this carefully: the threshold $N$ depends on $\varepsilon$, and beyond $N$ the sequence stays inside the $\varepsilon$-ball around $x$. In topological language: for every open neighbourhood $U$ of $x$, there exists $N$ such that $x_n \in U$ for all $n \geq N$. The $\varepsilon$-balls form a neighbourhood basis at $x$, so the metric condition is a basis-restricted version of the general topological condition.

For a general net $\Phi : D \to X$, we want the same shape of statement: $\Phi$ converges to $x$ iff for every open neighbourhood $U$ of $x$ there exists an index $\alpha_0 \in D$ such that $\Phi(\beta) \in U$ for every $\beta \geq \alpha_0$. In the language of "eventually in" from the previous page: **$\Phi$ converges to $x$ iff $\Phi$ is eventually in every neighbourhood of $x$**. The threshold $\alpha_0$ depends on the neighbourhood $U$, and beyond $\alpha_0$ the net stays inside $U$. When $D = \mathbb{N}$ this is sequential convergence, so the new definition is a strict generalisation.

Why is this the *right* definition rather than some alternative? Several things to rule out. We could ask "eventually in every set $A$ such that $x \in A$" — but this is too strong (the singleton $\{x\}$ is such a set, and being eventually in $\{x\}$ would mean the net is eventually equal to $x$). We could ask "eventually in some open set containing $x$" — but this is too weak (every net is eventually in $X$ itself, so this would be trivially satisfied). The open neighbourhood basis at $x$ is the *exact* level of refinement — strong enough to give a meaningful notion of "closeness", weak enough to be achievable. The dual condition — being "frequently in" every neighbourhood — gives a weaker notion called "having $x$ as a *cluster point*"; we will encounter this distinction with subnets.

Now to see why nets, and not sequences, are *necessary*. In a metric space, the closure of $A$ is the set of limits of sequences in $A$. In a general topological space this fails: there exist points in $\overline{A}$ to which no sequence in $A$ converges. The pathological example is the *ordinal space* $\omega_1 + 1$ — the set of ordinals up to and including the first uncountable ordinal $\omega_1$, with the order topology. The point $\omega_1$ is in the closure of $[0, \omega_1)$ (every open neighbourhood of $\omega_1$ contains arbitrarily large countable ordinals), but no sequence in $[0, \omega_1)$ converges to $\omega_1$ — every sequence has a countable supremum, strictly less than $\omega_1$. With nets (indexed by neighbourhoods of $\omega_1$, ordered by reverse inclusion), we can detect $\omega_1$ as a limit: pick a countable ordinal in each neighbourhood. The net works; no sequence does.

The same story plays out for continuity. In a metric space, $f$ is continuous at $x$ iff $f$ preserves all sequential limits at $x$. In a general space, sequential continuity is *strictly weaker* than continuity, and the gap is closed exactly by replacing sequences with nets. The result "$f$ is continuous iff it preserves all net limits" is the natural topological generalisation, and it works in every space. See [[Thm - Continuity via Nets]] and [[Thm - Closure via Nets]].

A subtle point: in a *Hausdorff* space, a net has at most one limit, and we can speak of "the limit of $\Phi$" with no ambiguity. In a non-Hausdorff space, a net can converge to multiple points. The standard example is the cofinite topology on $\mathbb{N}$: the sequence $x_n = n$ is eventually in every cofinite set (eventually it dodges every fixed finite set), so it converges to *every* element of $\mathbb{N}$. This is the failure mode of non-Hausdorff, and explains why Hausdorff is the minimum sane separation axiom for analysis. The equivalence "Hausdorff iff unique net limits" is one of the deepest justifications for the Hausdorff axiom (see [[Thm - Hausdorff Iff Unique Net Limits]]).

A final motivating observation. Net convergence in $\mathbb{R}$ for an "alternating" net works *differently* from an alternating sequence. In a sequence $x_n = (-1)^n$, the directed set $\mathbb{N}$ is *linearly ordered*, so the requirement "eventually in any neighbourhood of $+1$" forces $x_n$ to *avoid* $-1$ from some point onward, which it doesn't, so the sequence doesn't converge. But for a net indexed by a *partially ordered* directed set with, say, two non-comparable branches, one could construct a net that converges to $+1$ along one branch and $-1$ along the other — and the directed-set requirement forces *consistency* (the upper bound has to be in both neighbourhoods, hence in their intersection, hence near both $+1$ and $-1$, impossible in Hausdorff). So nets enforce a kind of "joint consistency" that sequences cannot. This is the subtle technical content of net convergence.

---

# The Definition

Let $X$ be a topological space and $\Phi : D \to X$ a net.

**Convergence.** The net $\Phi$ **converges to $x \in X$** if for every open neighbourhood $U$ of $x$, $\Phi$ is eventually in $U$ — that is, there exists $\alpha_0 \in D$ such that $\Phi(\beta) \in U$ for every $\beta \geq \alpha_0$. We write $x_\alpha \to x$ or $\Phi \to x$ or $\lim_{\alpha} x_\alpha = x$ (in Hausdorff spaces where the limit is unique).

**Equivalent basis formulation.** Equivalently, $\Phi \to x$ if and only if $\Phi$ is eventually in every basic open neighbourhood of $x$ — for any neighbourhood basis $\mathcal{B}_x$ of $x$, $\Phi \to x$ iff for every $B \in \mathcal{B}_x$ there exists $\alpha_0$ with $\Phi(\beta) \in B$ for all $\beta \geq \alpha_0$.

**Limit point / cluster point.** The point $x$ is a **cluster point** of $\Phi$ (also called an "accumulation point" of $\Phi$) if $\Phi$ is *frequently* in every neighbourhood of $x$ — for every $U \in \mathcal{N}(x)$ and every $\alpha \in D$ there exists $\beta \geq \alpha$ with $\Phi(\beta) \in U$. Equivalently, $\Phi$ has $x$ as a cluster point iff some subnet of $\Phi$ converges to $x$ — the standard **net-cluster-point–subnet correspondence**.

**Sequence convergence as a special case.** When $D = \mathbb{N}$, the definition specializes to: $\{x_n\}$ converges to $x$ iff for every neighbourhood $U$ of $x$, there exists $N$ such that $x_n \in U$ for all $n \geq N$. This recovers the metric-space definition exactly.

---

# Relate to Other Fields / Compression

Net convergence is the topology-side mirror of **filter convergence**: a filter $\mathcal{F}$ on $X$ converges to $x$ iff every neighbourhood of $x$ is in $\mathcal{F}$, and the net-to-filter correspondence translates each into the other. The two formalisms are equivalent, and which one to use is a matter of taste. Bourbaki uses filters; Bredon and most American textbooks use nets.

In **probability**, convergence of random variables and convergence of distributions are both special cases of net (or sequence) convergence in appropriate topological spaces. The four standard probabilistic convergence modes — almost sure, in probability, in $L^p$, in distribution — correspond to convergence of *sequences* of random variables in spaces with different topologies: pointwise convergence (a.s.), convergence in measure (in probability), $L^p$ norm convergence, and weak convergence of measures (in distribution).

In **functional analysis**, *weak convergence* in a Banach space and *weak-$*$ convergence* in the dual are nets — indexed not by $\mathbb{N}$ but by the directed set of finite subsets of the dual (or predual), ordered by inclusion. The need for nets is what motivates the entire formalism: in infinite-dimensional spaces, weak topologies are *not* first-countable, so sequential convergence is insufficient to detect everything.

In **category theory**, the colimit of a filtered diagram is the categorical analogue of "limit of a net". The same directed-set indexing structure controls both, and filtered colimits commute with finite limits in many categories.

---

# Examples / Corollaries

**Is an instance — a sequence in $\mathbb{R}$.** $x_n = 1/n$ in $\mathbb{R}$ converges to $0$: for any $\varepsilon$-ball around $0$, eventually $1/n < \varepsilon$. This is the prototypical sequence convergence.

**Is an instance — the "neighbourhood-indexed" net at a closure point.** Let $A \subseteq X$ and $x \in \overline{A}$. Index $\Phi$ by $\mathcal{N}(x)$ ordered by reverse inclusion, and for each $U \in \mathcal{N}(x)$ pick $\Phi(U) \in U \cap A$ (which exists because $x \in \overline{A}$). Then $\Phi \to x$: for any neighbourhood $V$ of $x$, take $\alpha_0 = V$; then $\beta \geq V$ in the directed set means $\beta \subseteq V$, so $\Phi(\beta) \in \beta \cap A \subseteq V$. This is the canonical construction of a net converging to a closure point, and is the heart of the proof of [[Thm - Closure via Nets]].

**Is an instance — a net of partial sums.** For an uncountable family $\{a_s\}_{s \in S}$ of real numbers, define $\Phi : \text{Fin}(S) \to \mathbb{R}$ by $\Phi(F) = \sum_{s \in F} a_s$. The net $\Phi$ converges to $L$ iff for every $\varepsilon > 0$ there exists a finite $F_0$ such that $|L - \sum_{s \in F} a_s| < \varepsilon$ for every finite $F \supseteq F_0$. This is the canonical notion of "unordered sum" for uncountable families, and is *stricter* than the sequential sum: it converges iff the family is absolutely summable, i.e., $\sum |a_s| < \infty$ with at most countably many nonzero $a_s$.

**Is an instance of converging to multiple points — non-Hausdorff.** In the cofinite topology on $\mathbb{N}$, the sequence $x_n = n$ converges to every point of $\mathbb{N}$. Reason: a neighbourhood of any $m \in \mathbb{N}$ is a cofinite set, missing only finitely many elements. Eventually (after $n > \max(\text{missing elements})$), $x_n$ is in the neighbourhood. So $x_n \to m$ for every $m$. This is the failure of uniqueness of limits, and the failure mode of non-Hausdorff.

**Is NOT a convergent net — an "oscillating" sequence in $\mathbb{R}$.** $x_n = (-1)^n$ does *not* converge to any point of $\mathbb{R}$: for any candidate limit $L$, the neighbourhood $(L - 0.5, L + 0.5)$ excludes either $1$ or $-1$ (or both), and the sequence keeps hitting both values, so it is never eventually inside the neighbourhood. It has *cluster points* $+1$ and $-1$ — frequently in every neighbourhood — but no actual limit.

**Is NOT a convergent net — a sequence with a divergent subsequence.** Take $x_n = n$ in $\mathbb{R}$. The neighbourhood $(0, 10)$ of any candidate limit $L \in (0, 10)$ is exited eventually as $n$ grows, so the sequence does not converge.

**Corollary — a sequence in a discrete space converges iff eventually constant.** In the discrete topology, each $\{x\}$ is open, so "eventually in $\{x\}$" means $x_n = x$ for all large $n$. The convergence demand for *every* neighbourhood includes the singleton, so the sequence must eventually be constant.

**Corollary — constant nets converge.** If $\Phi(\alpha) = x$ for all $\alpha$, then $\Phi$ is eventually in every neighbourhood of $x$ (in fact, always), so $\Phi \to x$. Useful trivially, but also as a degenerate case in proofs.

**Corollary — convergence is preserved under composition with continuous functions.** If $f : X \to Y$ is continuous and $x_\alpha \to x$ in $X$, then $f(x_\alpha) \to f(x)$ in $Y$. (Take a neighbourhood $V$ of $f(x)$; then $f^{-1}(V)$ is a neighbourhood of $x$, and $\Phi$ is eventually in $f^{-1}(V)$ by hypothesis, so $f \circ \Phi$ is eventually in $V$.) This is one direction of [[Thm - Continuity via Nets]] — the other (preservation of net convergence implies continuity) is the substantive content.

**Calibration check — a subsequence of a sequence is a subnet.** If $\{x_n\}$ is a sequence in $X$ and $\{x_{n_k}\}$ is a subsequence (with $n_1 < n_2 < \ldots$), then $\{x_{n_k}\}$ is a subnet in the sense of [[Def - Subnet and Universal Net]], with the final function $h : \mathbb{N} \to \mathbb{N}$ given by $h(k) = n_k$. So "subnet generalises subsequence". The converse is what is *not* true — a subnet of a sequence need not be a subsequence.

---

# Unlocked by This

> [!tip] **Closure-via-Nets and Continuity-via-Nets** *(this topic)*
> Two foundational theorems: $x \in \overline{A}$ iff some net in $A$ converges to $x$ ([[Thm - Closure via Nets]]); $f$ is continuous iff $f$ preserves all net limits ([[Thm - Continuity via Nets]]). These are the natural net-level analogues of the metric-space sequential characterizations.

> [!tip] **Net Characterisation of Compactness** *(this topic)*
> A topological space $X$ is compact iff every net in $X$ has a convergent subnet. See [[Def - Compact Space]] and [[Thm - Every Net Has a Universal Subnet]]. This is the "true name" of compactness — the equivalent formulation that captures what compactness actually does in analysis.

> [!tip] **Banach–Alaoglu and Weak Topologies** *(from Functional Analysis)*
> The closed unit ball of the dual of a normed space is weak-$*$ compact, by Banach–Alaoglu. The proof essentially uses net convergence: the unit ball is closed in a product of compact intervals (Tychonoff), and the product topology is generated by neighbourhoods that match the directed-set indexing of nets. Sequence-level reasoning fails here; nets are essential.
