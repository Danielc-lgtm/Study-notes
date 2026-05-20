---
type: definition
subject: topology
prereqs:
  - "Def - Metric Space"
  - "Def - Open and Closed Sets in a Metric Space"
tags: [analysis, topology]
---

# Notation

Throughout, $X$ is a fixed set carrying two candidate metrics $d_1$ and $d_2$. We write $\tau_{d_i}$ for the topology induced by $d_i$, i.e. the collection of sets that are open in the sense of $d_i$. For $x \in X$ and $\varepsilon > 0$, $B_\varepsilon^{(i)}(x) = \{y : d_i(x, y) < \varepsilon\}$ is the open ball with respect to $d_i$. We write $\text{id}_X : (X, d_1) \to (X, d_2)$ for the identity map on $X$ regarded as a function between the two metric spaces. We use $L \leq M$ for constants. For the full registry of symbols see [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Axiom Motivation

We have just learned that the topology induced by a metric — the collection of open sets — does not depend on the actual numerical values of the metric, only on the *family* of balls. So two metrics that look numerically very different can still give the same notion of "open" and hence the same notion of "continuous function". The question becomes: when are two metrics on the same set "the same" for analytic purposes?

To answer this, we must first ask *which* purposes we are willing to identify metrics across. The right framework is to ask: for which purposes does the metric data feed in? Three answers, in increasing order of restrictiveness.

The most basic purpose of a metric is to define *continuity* and *open sets*. From this point of view, two metrics are equivalent if and only if they generate the same open sets — the same topology. This is the loosest notion, and it is called **topological equivalence**. The intuition: $d_1$ and $d_2$ are topologically equivalent if every "small ball" in one metric contains a "small ball" in the other, *but the relationship between the sizes need not be uniform*. Each point may need its own conversion ratio between the two metrics.

The next purpose is to define *uniform* continuity — that is, a single $\delta$ that works for all $x$ given $\varepsilon$. This is more restrictive: it asks that the conversion ratio between $d_1$ and $d_2$ be uniform across the space. This gives the notion of **uniform equivalence**: there exist functions $\varphi_1, \varphi_2 : (0, \infty) \to (0, \infty)$ with $\varphi_i(\varepsilon) \to 0$ as $\varepsilon \to 0$, such that $d_1(x, y) < \varphi_1(\varepsilon) \Rightarrow d_2(x, y) < \varepsilon$ and vice versa, for *all* $x, y$.

The strongest commonly used purpose is to compare metrics up to a constant: there exist constants $0 < c \leq C < \infty$ with $c\, d_1(x, y) \leq d_2(x, y) \leq C\, d_1(x, y)$ for all $x, y$. This is **strong equivalence** (also called **Lipschitz equivalence** or *bi-Lipschitz equivalence*). The metrics differ at most by a multiplicative factor, uniformly. This is the natural notion in many parts of analysis — for instance, when we say $\ell^1$, $\ell^2$, $\ell^\infty$ are equivalent on $\mathbb{R}^n$ we usually mean strongly equivalent.

The three notions are nested: strong $\Rightarrow$ uniform $\Rightarrow$ topological, and none of the reverse implications holds in general. On a bounded space the gap between uniform and topological can vanish, and on a compact space the gap between strong and topological can vanish, but in general they are genuinely distinct.

Now ask: *why is topological equivalence the right base notion*? Because almost every theorem in analysis that depends only on continuity — characterizations of compactness via covers, properties of continuous functions, the open-mapping principle — uses only the topology. A theorem about *Lipschitz* functions or *uniformly continuous* functions would need the stronger notions; but continuity alone, the most basic property, depends only on the topology. So the equivalence-class of metrics generating the same topology is the natural unit of identification.

There is also a cleaner formulation: $d_1$ and $d_2$ are topologically equivalent if and only if the identity map $\text{id}_X : (X, d_1) \to (X, d_2)$ is a **homeomorphism** — a continuous bijection with continuous inverse. The "if" is automatic; the "only if" uses that continuity of $\text{id}_X$ means preimages of $d_2$-open sets are $d_1$-open. Topological equivalence is exactly the failure of any topological distinction between the two metrics, in this principled sense. Once we have this formulation, the right level of abstraction for the entire theory becomes clear: we should be working with topological spaces, not metric spaces, and a metric is just one *presentation* of a topology.

The phenomenon is reminiscent of the choice of basis in linear algebra: many different bases can give the same vector space, and we identify them via change-of-basis matrices. Many different metrics can give the same topological space, and we identify them via equivalence relations like the three above. The "platonic" object is the topology; the metric is a particular *representation* of it, and equivalences of metric are change-of-representation maps.

A useful trick for *generating* equivalent metrics is the bounded transformation $d \mapsto d / (1 + d)$. If $d$ is any metric, then $d'(x, y) = d(x, y) / (1 + d(x, y))$ is also a metric (a small calculation using $\frac{a+b}{1+a+b} \leq \frac{a}{1+a} + \frac{b}{1+b}$ for $a, b \geq 0$), and it is bounded by 1. The metrics $d$ and $d'$ are topologically equivalent: a $d$-small ball is a $d'$-small ball and vice versa, because the function $t \mapsto t/(1+t)$ is a strictly increasing bijection $[0, \infty) \to [0, 1)$. So any metric can be replaced by a bounded one without changing the topology. This is useful for putting metrics on countable products of metric spaces (where uniformity of the metric is otherwise hard to ensure).

---

# The Definition

Let $X$ be a set and let $d_1, d_2$ be metrics on $X$.

**Topological equivalence.** The metrics $d_1$ and $d_2$ are **topologically equivalent** if they induce the same topology on $X$:
$$\tau_{d_1} = \tau_{d_2}.$$
Equivalently, the identity map $\text{id}_X : (X, d_1) \to (X, d_2)$ is a homeomorphism: it is continuous and its inverse is continuous. Equivalently again, for every $x \in X$ and every $\varepsilon > 0$, there exists $\delta > 0$ such that $B_\delta^{(1)}(x) \subseteq B_\varepsilon^{(2)}(x)$, and the symmetric statement with the roles of $1$ and $2$ swapped.

**Uniform equivalence.** The metrics $d_1$ and $d_2$ are **uniformly equivalent** if for every $\varepsilon > 0$ there exists $\delta > 0$ such that
$$d_1(x, y) < \delta \implies d_2(x, y) < \varepsilon \qquad \text{for all } x, y \in X,$$
and the symmetric statement with the roles of $1$ and $2$ swapped. Equivalently, the identity map $\text{id}_X : (X, d_1) \to (X, d_2)$ and its inverse are both **uniformly continuous**.

**Strong (Lipschitz, bi-Lipschitz) equivalence.** The metrics $d_1$ and $d_2$ are **strongly equivalent** if there exist constants $0 < c \leq C < \infty$ such that
$$c \cdot d_1(x, y) \leq d_2(x, y) \leq C \cdot d_1(x, y) \qquad \text{for all } x, y \in X.$$

**Hierarchy.** Strong equivalence implies uniform equivalence (take $\delta = \varepsilon/C$); uniform equivalence implies topological equivalence (the $\varepsilon$–$\delta$ condition restricted to fixed $x$ gives the ball-containment condition).

---

# Relate to Other Fields / Compression

Topological equivalence is the **isomorphism relation** in the category of metric spaces *forgetting down to topology*: a presentation by a metric is one choice of structure refining the topology. The notion is exactly analogous to the way two norms $\lVert \cdot \rVert_1$ and $\lVert \cdot \rVert_2$ on a vector space $V$ are called **equivalent norms** if there exist constants $c, C$ with $c \lVert v \rVert_1 \leq \lVert v \rVert_2 \leq C \lVert v \rVert_1$. On *finite-dimensional* $V$ every pair of norms is equivalent (this is a theorem: the unit sphere is compact in the norm topology, so the continuous function $v \mapsto \lVert v \rVert_2 / \lVert v \rVert_1$ attains a positive minimum and a finite maximum). On infinite-dimensional $V$ — for example the space of continuous functions on $[0, 1]$ — there are inequivalent norms, and the $L^p$ versus $L^\infty$ comparison below is the prototype.

In **functional analysis**, the equivalence of all norms on $\mathbb{R}^n$ is the reason finite-dimensional analysis is "topologically trivial" — there is only one reasonable topology on $\mathbb{R}^n$ as a vector space. In infinite dimensions, the multiplicity of inequivalent topologies (norm topology, weak topology, weak-$*$ topology) is the source of much of the richness of the subject.

In **Riemannian geometry**, two Riemannian metrics $g_1, g_2$ on a manifold $M$ are called **conformally equivalent** if $g_2 = e^{2f} g_1$ for some smooth function $f$. The induced distance functions are *not* metric-equivalent in our sense in general, but they share the same set of angle-preserving maps and the same Cauchy–Riemann structure (in dimension 2). The notion of equivalence shifts depending on what one wants to identify.

The truncation trick $d \mapsto d/(1+d)$ is the engine behind constructing the **Polish space** topology on countable products of metric spaces: if $(X_n, d_n)$ are metric spaces, the metric $d((x_n), (y_n)) = \sum_n 2^{-n} d_n(x_n, y_n)/(1 + d_n(x_n, y_n))$ on $\prod_n X_n$ is well-defined precisely because the truncations are bounded. This is how the product topology on countably many factors gets a metric, when each factor is metrizable.

---

# Examples / Corollaries

**Is an instance of strong (hence all three) equivalence — $\ell^1, \ell^2, \ell^\infty$ on $\mathbb{R}^n$.** Define
$$d_1(x, y) = \sum_{i=1}^n |x_i - y_i|, \quad d_2(x, y) = \sqrt{\sum_{i=1}^n |x_i - y_i|^2}, \quad d_\infty(x, y) = \max_i |x_i - y_i|.$$
The chain of inequalities
$$d_\infty(x, y) \leq d_2(x, y) \leq d_1(x, y) \leq n\, d_\infty(x, y), \qquad d_2(x, y) \leq \sqrt{n}\, d_\infty(x, y)$$
shows that each pair is strongly equivalent with explicit constants. The right-most inequality $d_1 \leq n\, d_\infty$ has constant $n$ — depending on dimension — but for fixed $n$ this is fine: a constant is a constant. The geometric pictures of the unit balls — diamond ($d_1$), Euclidean disc ($d_2$), square ($d_\infty$) — are dramatically different, but they nest within constant factors of each other, so the topologies coincide.

**Is an instance of strong equivalence — the truncated metric $d' = d/(1+d)$ versus $d$.** Take any metric $d$ on $X$. We have $d'(x, y) = d(x, y)/(1 + d(x, y))$. The map $t \mapsto t/(1 + t)$ is strictly increasing on $[0, \infty)$ with image $[0, 1)$, so it is a bijection $[0, \infty) \to [0, 1)$ and $d'$ is a metric (the triangle inequality follows from the concavity of $t \mapsto t/(1+t)$). On any *bounded* subset $\{d(x, y) \leq R\}$, we have $1/(1 + R) \leq d'/d \leq 1$, so $d'$ and $d$ are strongly equivalent on bounded sets — and topologically equivalent globally. The truncation reduces an unbounded metric to a bounded one with the same topology, a key trick.

**Is an instance of topological equivalence that is NOT uniform equivalence — $d$ and $d^2$ on $\mathbb{R}$.** Take $d(x, y) = |x - y|$ and $d'(x, y) = |x - y|^2$ — wait: $d'$ is not actually a metric (triangle fails, see [[Def - Metric Space]]). Take instead $d$ and $d'(x, y) = \min(d(x, y), 1)$: the truncated Euclidean metric. These are topologically equivalent (small balls are the same) and uniformly equivalent (both metrics agree for distance $< 1$). For a genuine non-uniform example, consider $\mathbb{R}$ with $d_1(x, y) = |x - y|$ and $d_2(x, y) = |\arctan(x) - \arctan(y)|$. Both induce the standard topology on $\mathbb{R}$ (the arctan is a homeomorphism $\mathbb{R} \to (-\pi/2, \pi/2)$), so they are topologically equivalent. They are *not* uniformly equivalent: with $x_n = n, y_n = n + 1$, we have $d_1(x_n, y_n) = 1$ for all $n$, while $d_2(x_n, y_n) = |\arctan(n+1) - \arctan(n)| \to 0$. So $d_2$ "sees less and less" of the distances far from the origin, while $d_1$ does not. No uniform $\delta$–$\varepsilon$ comparison can hold.

**Is NOT an instance — the discrete metric and the standard metric on $\mathbb{R}$ are not topologically equivalent.** In the discrete metric every singleton $\{x\}$ is open; in the standard metric singletons are not open. So the topologies differ. Equivalently: the identity map $\mathbb{R}_\text{standard} \to \mathbb{R}_\text{discrete}$ is *not* continuous, because the preimage of $\{0\}$ (open in the discrete topology) is $\{0\}$ (not open in the standard topology).

**Is NOT an instance — the sup metric and the $L^1$ metric on $C[0, 1]$ are not topologically equivalent.** Consider $f_n(t) = $ "thin tall spike" of height $1$ and width $1/n$, supported near $t = 0$. Then $d_\infty(f_n, 0) = 1$ for all $n$ (the spike has height 1), but $d_1(f_n, 0) = \int |f_n| = 1/(2n) \to 0$. So $f_n \to 0$ in the $L^1$ metric but not in the sup metric. If the two metrics were topologically equivalent, convergence in one would imply convergence in the other — see [[Ex - Sup metric versus L1 metric on C01]]. This example is the prototype of "different metrics on a function space give genuinely different topologies", and it is the reason functional analysis needs to choose a metric carefully for each problem.

**Corollary — the identity map is the test.** $d_1 \sim_{\text{top}} d_2$ if and only if both $\text{id}_X : (X, d_1) \to (X, d_2)$ and $\text{id}_X : (X, d_2) \to (X, d_1)$ are continuous (which is to say, the identity is a homeomorphism). One direction is enough to *fail* equivalence: if $\text{id}_X$ is not continuous in one direction, the metrics are not topologically equivalent.

**Corollary — strong equivalence is more than topological equivalence carries.** Strong equivalence preserves uniform-continuity-class, Lipschitz-class, and Cauchy-sequence-class (the same sequences are Cauchy in both metrics). Topological equivalence preserves only continuity-class — which sequences converge, and to what — but not the rate. So a Cauchy sequence in one metric may fail to be Cauchy in a merely topologically equivalent metric. Example: $\mathbb{R}$ with the Euclidean metric is complete, but $\mathbb{R}$ with the topologically equivalent metric $d'(x, y) = |\arctan(x) - \arctan(y)|$ is *not* complete (the sequence $x_n = n$ is Cauchy in $d'$ but does not converge). Completeness depends on the metric, not just the topology.

**Corollary — finite-dimensional norm equivalence.** All norms on $\mathbb{R}^n$ are strongly equivalent (and hence topologically equivalent). This is a theorem rather than a triviality: the unit sphere $\{v : \lVert v \rVert_1 = 1\}$ is compact (closed and bounded in any norm), so the continuous function $v \mapsto \lVert v \rVert_2$ attains its max and min there, which are the constants $C, c$ of the strong equivalence. The result fails in infinite dimensions, where there are inequivalent norms even on the same space.

**Calibration check.** Verify that the three metrics $\ell^1, \ell^2, \ell^\infty$ on $\mathbb{R}^2$ are pairwise strongly equivalent by writing down the explicit constants for each pair. Verify that the metric $d(x, y) = \min(|x - y|, 1)$ on $\mathbb{R}$ is topologically equivalent to the Euclidean metric (think about what "small balls" look like). Verify that on $C[0, 1]$, a continuous function vanishing nowhere is "far from $0$" in the sup metric but the integral metric depends on the integral. If you can also explain why "the identity map is a homeomorphism" is the most natural characterization of topological equivalence, you have understood every clause.

---

# Unlocked by This

> [!tip] **Topological Invariance** *(from this topic)*
> Once we have a notion of when two metrics give the same topology, we can speak of properties that depend only on the topology: connectedness, compactness, separability, the number of connected components. Each of these is invariant under topological equivalence. See [[Def - Topological Space]] and [[Def - Homeomorphism]].

> [!tip] **Norm Equivalence and Banach Spaces** *(from Functional Analysis)*
> A **norm** $\lVert \cdot \rVert$ on a vector space $V$ induces a metric $d(v, w) = \lVert v - w \rVert$. Two norms are *equivalent* if their induced metrics are strongly equivalent. On finite-dimensional $V$, all norms are equivalent; on infinite-dimensional $V$, there are inequivalent norms, and the choice of norm determines whether the space is complete (a **Banach space**) or not.

> [!tip] **Polish Spaces and Borel Hierarchy** *(from Descriptive Set Theory and Probability)*
> A **Polish space** is a topological space that is separable and admits a complete metric — but not every metric inducing the topology is complete. The notion of topological equivalence is exactly what is needed to formulate this: "admits a complete metric" is a property of the topology, not of any particular metric. Polish spaces are the natural setting for advanced probability theory (regular conditional distributions, weak convergence on Polish spaces).

> [!tip] **Bi-Lipschitz Equivalence and Metric Geometry** *(from Geometric Group Theory)*
> The notion of strong (bi-Lipschitz) equivalence is fundamental in **metric geometry** and **geometric group theory**: the **quasi-isometry** relation between metric spaces is a relaxation of bi-Lipschitz equivalence in which the constants are allowed an additive slack. Cayley graphs of finitely generated groups are well-defined only up to quasi-isometry — the choice of generating set changes the metric, but only by a quasi-isometry — and many group-theoretic invariants (growth rate, hyperbolicity) are quasi-isometry invariants.
