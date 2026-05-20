---
type: definition
subject: topology
prereqs:
  - "Def - Metric Space"
  - "Def - Cauchy Sequence and Complete Metric Space"
tags: [analysis, topology]
---

# Notation

$(X, d)$ is a metric space. $B_\varepsilon(x) = \{y \in X : d(x, y) < \varepsilon\}$ is the open $\varepsilon$-ball about $x$. An **$\varepsilon$-net** for $X$ is a subset $F \subseteq X$ such that every point of $X$ is within distance $\varepsilon$ of some point of $F$; equivalently, the $\varepsilon$-balls about points of $F$ cover $X$. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Axiom Motivation

The motivation is to find the right notion of "topologically small" for a metric space. Boundedness — the property that $X$ has finite diameter — looks like the obvious candidate, but it turns out to be too weak. In Euclidean space $\mathbb{R}^n$, bounded sets are exactly the ones with compact closure (this is Heine–Borel), but in infinite-dimensional Banach spaces, bounded sets can be very far from compact: the closed unit ball of an infinite-dimensional Hilbert space, for instance, contains an orthonormal sequence $\{e_n\}$ with $\lVert e_n - e_m\rVert = \sqrt{2}$ for $n \neq m$, so no subsequence is Cauchy, and the ball is not sequentially compact. Boundedness alone does not capture compactness.

The fix is to ask for a quantitative form of "finiteness at every scale". A subset $X$ should be totally bounded if, for every $\varepsilon > 0$, the space can be covered by a *finite* number of $\varepsilon$-balls. The cover is allowed to depend on $\varepsilon$ — smaller $\varepsilon$ needs more balls — but for each scale the number is finite. This is much stronger than boundedness: an infinite-dimensional unit ball is bounded but cannot be covered by finitely many $1/2$-balls (the orthonormal sequence shows that any two distinct points must be in different balls, so you need at least one ball per orthonormal vector).

Total boundedness is exactly the right hypothesis for compactness in metric spaces, in conjunction with completeness. The equivalence "compact = complete + totally bounded" (the central theorem of §9) decomposes compactness into a topological condition (every Cauchy converges) and a geometric condition (finite $\varepsilon$-nets). The topological condition says limits exist; the geometric condition says the space is "finite at every resolution". Together they give compactness.

Why is "$\varepsilon$-net" the right finiteness condition, and not some weaker version? Because $\varepsilon$-nets bound the *cardinality at scale $\varepsilon$*, which is exactly what is needed to extract convergent subsequences. The standard proof of compactness from total boundedness uses a diagonal argument: a sequence has infinitely many points in some $1$-ball, so it has an infinite subsequence in that ball; then infinitely many of those in some $1/2$-ball, so a subsequence; iterate. The diagonal subsequence is Cauchy because at every scale it is eventually confined to a small ball. If we only had "bounded" instead of "totally bounded", the iteration would not work — the bounded condition gives no information about smaller scales.

Why allow the $\varepsilon$-net to depend on $\varepsilon$? Because demanding a *single* finite cover at all scales would reduce to "finite", which is far too strong. The Hilbert cube $[0, 1]^\mathbb{N}$ is totally bounded (and even compact!), but it is uncountable; what makes it tractable is that for each $\varepsilon$, finitely many $\varepsilon$-balls suffice, even though the total cardinality is large.

Total boundedness is also the right finiteness for **uniform continuity** arguments: a uniformly continuous function on a totally bounded space has bounded image, and a Cauchy sequence in the domain pushes forward to a Cauchy sequence in the codomain.

---

# The Definition

A metric space $(X, d)$ is **totally bounded** if for every $\varepsilon > 0$ there exists a finite set $\{x_1, \dots, x_n\} \subseteq X$ (a **finite $\varepsilon$-net**) such that

$$X = \bigcup_{i=1}^n B_\varepsilon(x_i).$$

Equivalently, for every $\varepsilon > 0$ there is a finite cover of $X$ by sets of diameter at most $2\varepsilon$ (or, after a $2\times$ rescaling, of diameter at most $\varepsilon$).

A subset $A \subseteq X$ is totally bounded if it is totally bounded as a metric space with the inherited metric — equivalently, if for every $\varepsilon > 0$ there is a finite set $\{x_1, \dots, x_n\} \subseteq X$ with $A \subseteq \bigcup_i B_\varepsilon(x_i)$ (note: the centers can be chosen anywhere in $X$, not necessarily in $A$; the two formulations differ by at most a factor of $2$).

Equivalent characterization via sequences: $X$ is totally bounded if and only if every sequence in $X$ has a **Cauchy subsequence**. (Without completeness, the Cauchy subsequence need not converge.)

---

# Relate to Other Fields / Compression

Total boundedness is the metric incarnation of a more general notion: **precompactness** (or **relative compactness**) in a uniform space. A subset of a uniform space is precompact if its closure is compact; in complete metric spaces this is equivalent to being totally bounded. The interplay "totally bounded + complete = compact" is metric-space shorthand for "precompact + closed in a complete space = compact".

In **functional analysis**, the **Arzelà–Ascoli theorem** characterizes totally bounded subsets of $C(K)$ (continuous functions on a compact $K$ with sup norm) as the **equicontinuous bounded** families. This is the canonical bridge: total boundedness in a function space is captured by an equicontinuity-plus-boundedness condition, not by mere boundedness. The same idea underlies the **Rellich–Kondrachov compactness theorem** for Sobolev embeddings.

In **dynamical systems**, the **topological entropy** of a continuous map on a compact metric space is defined via the rate at which finite $\varepsilon$-nets distinguish trajectories — entropy is the asymptotic exponent of the minimal $\varepsilon$-net size for the iterated dynamics. Total boundedness is the static version of this; entropy is the dynamic version.

In **information theory and statistics**, the **metric entropy** $H(\varepsilon)$ of a metric space is $\log$ of the minimal size of a finite $\varepsilon$-net — a quantitative measure of total boundedness. Sample complexity bounds for learning algorithms are expressed via metric entropy of the hypothesis class, and the **Dudley entropy integral** estimates Gaussian process suprema via $\int \sqrt{H(\varepsilon)}\, d\varepsilon$.

---

# Examples / Corollaries

**Is an instance — closed bounded subset of $\mathbb{R}^n$.** By Heine–Borel, closed bounded subsets of $\mathbb{R}^n$ are compact, hence totally bounded. Explicitly, the cube $[-N, N]^n$ admits a finite $\varepsilon$-net for any $\varepsilon$: partition it into cubes of side length $\varepsilon/\sqrt{n}$, of which there are $(2N\sqrt{n}/\varepsilon)^n$.

**Is an instance — the Hilbert cube $[0, 1]^\mathbb{N}$ with the metric $d(x, y) = \sum_n |x_n - y_n|/2^n$.** For each $\varepsilon$, truncate at coordinate $N$ where $\sum_{n > N} 1/2^n < \varepsilon/2$, and use an $\varepsilon/2$-net for $[0, 1]^N$ (finite!). The product of the truncated net with arbitrary tails gives a finite $\varepsilon$-net for the cube. Hence the Hilbert cube is totally bounded (and being complete in this metric, it is compact).

**Is NOT an instance — the unit ball of an infinite-dimensional Hilbert space.** Take an orthonormal basis $\{e_n\}_{n \in \mathbb{N}}$. The closed unit ball contains all $e_n$, with $\lVert e_n - e_m\rVert = \sqrt{2}$ for $n \neq m$. Any $\sqrt{2}/2$-ball can contain at most one $e_n$, so a finite $\sqrt{2}/2$-net would need infinitely many balls — contradiction. So the unit ball is bounded but not totally bounded. By F. Riesz's theorem, this is true in *every* infinite-dimensional normed space.

**Is NOT an instance — $\mathbb{R}$ with the usual metric.** $\mathbb{R}$ is unbounded, hence not totally bounded. But its subsets are: every bounded subset of $\mathbb{R}$ is totally bounded.

**Is an instance — the rationals in $[0, 1]$.** As a subset of $\mathbb{R}$ they are totally bounded (just as $[0, 1]$ is), but they are not complete (the irrationals are missing), so they are not compact. This shows that total boundedness alone is not enough for compactness — completeness is the additional ingredient.

**Corollary — total bounded implies separable.** A totally bounded metric space is separable: for each $n$, take a finite $1/n$-net $F_n$; the union $F = \bigcup_n F_n$ is countable and dense. So total boundedness rules out spaces of size larger than continuum, and is incompatible with non-separability.

**Corollary — total bounded implies bounded, not conversely.** Every totally bounded space is bounded (a finite $1$-net gives diameter at most $2 + \max_i d(x_i, x_j)$). The converse fails by the infinite-dimensional unit ball example.

**Corollary — every sequence has a Cauchy subsequence.** This is the sequential characterization. Given a sequence $\{x_n\}$, cover $X$ by finitely many $1$-balls; one contains infinitely many $x_n$, extract a subsequence in that ball; among that subsequence, finitely many $1/2$-balls cover, extract again; continue, and diagonalize.

**Calibration check.** Verify: (i) the rationals in $\mathbb{Q} \cap [0, 1]$ are totally bounded as a subset of $\mathbb{R}$; (ii) $\ell^2$ (square-summable sequences) restricted to the unit ball is *not* totally bounded (by the orthonormal sequence argument); (iii) the set $\{x \in \ell^2 : |x_n| \leq 1/n\}$ (a "shrinking-coordinate" box) *is* totally bounded — it has finite $\varepsilon$-nets via truncation, just like the Hilbert cube; (iv) a finite metric space is trivially totally bounded.

---

# Unlocked by This

> [!tip] Compactness in Metric Spaces *(from this topic)*
> The equivalence **compact = complete + totally bounded** decomposes the metric notion of compactness into a topological/limit condition (completeness) and a geometric/scale condition (total boundedness). See [[Thm - Compactness in Metric Spaces (Three Equivalents)]].

> [!tip] Arzelà–Ascoli Theorem *(from Functional Analysis)*
> In $C(K)$ for $K$ compact metric, the totally bounded subsets are exactly the **equicontinuous, pointwise bounded** families. This is the workhorse compactness criterion in function space analysis — see [[Thm - Arzelà–Ascoli Theorem]].

> [!tip] Metric Entropy and Statistical Learning *(from Statistics)*
> The minimal size of an $\varepsilon$-net of a hypothesis class controls its **VC dimension** and **Rademacher complexity**, hence the sample complexity of PAC learning. Metric entropy $\log N(\varepsilon)$ is the quantitative form of total boundedness — see **Dudley's entropy integral**.
