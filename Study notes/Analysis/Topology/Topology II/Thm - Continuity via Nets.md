---
type: theorem
subject: topology
prereqs:
  - "Def - Continuous Map"
  - "Def - Directed Set and Net"
  - "Def - Net Convergence"
  - "Def - Topological Space"
tags: [analysis, topology, nets, continuity]
---

# Notation

$X, Y$ are [[Def - Topological Space|topological spaces]] and $f : X \to Y$ a function. A **net** in $X$ is a function $\Phi : D \to X$ from a [[Def - Directed Set and Net|directed set]] $D$ to $X$, written $\{x_\alpha\}$. The net **converges to** $x$, written $x_\alpha \to x$, if for every neighborhood $U$ of $x$ there is $\alpha_0$ with $x_\alpha \in U$ for $\alpha \geq \alpha_0$ (see [[Def - Net Convergence]]). The full registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Theorem.** A function $f : X \to Y$ between topological spaces is **continuous** (see [[Def - Continuous Map]]) if and only if for every net $\{x_\alpha\}$ in $X$ converging to $x \in X$, the image net $\{f(x_\alpha)\}$ in $Y$ converges to $f(x)$.

This is the abstract-topology generalization of the metric-space "continuous iff sequentially continuous". In a first-countable space (like a metric space) sequences suffice; in general topological spaces, nets are essential.

---

# Motivation

Continuity in topological spaces is defined as "preimages of open sets are open". This is the *right* definition — categorically clean, base-of-topology-friendly — but it can feel disconnected from the intuitive picture of "$f$ sends nearby points to nearby points". In metric spaces, the latter is captured by sequences: $f$ continuous if and only if $x_n \to x$ implies $f(x_n) \to f(x)$. The question this theorem answers is: *what is the analog of "sequentially continuous" in arbitrary topological spaces*?

The answer is **net-continuous**: preserve all net limits. The forward direction (continuous implies net-preserving) is straightforward — preimages of neighborhoods of $f(x)$ are neighborhoods of $x$, in which the net is eventually. The reverse direction is the substantive one: if $f$ preserves nets, then $f$ is continuous in the open-set sense. The proof constructs, for any non-continuity witness (an open $V \subseteq Y$ with $f^{-1}(V)$ not open), a net witnessing the failure: a net in $X \setminus f^{-1}(V)$ converging to a point of $f^{-1}(V)$, whose image is in $Y \setminus V$ but should converge to $f(x) \in V$.

The value of the theorem is operational. To prove a function is continuous, one can either show preimages of opens are open, or show net preservation. The net method is often more direct, because it expresses continuity in *terms of the limiting behavior*, which is what one usually wants to use anyway. In analysis, "$f(\lim x_n) = \lim f(x_n)$" is the operational meaning of continuity — net preservation is the topology-wide form.

This theorem also reveals *why* sequential continuity fails to characterize continuity in general spaces. The forward direction works for sequences (sequences are nets), but the reverse direction requires the canonical net constructed from the *non-continuity witness*, and this net is indexed by neighborhoods of $x$, which may have arbitrary cardinality. In a first-countable space, the construction collapses to a sequence and sequential continuity suffices. Without first countability, nets are essential.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f$ is continuous".

The first disguised source is **$f$ is given by a formula** — polynomial, rational, exponential, etc. in concrete spaces. Property $B$: $f$ is built from continuous operations. The bridge: continuity is preserved by composition (this theorem makes this manifest — preserving nets composes), products, sums, and limits. *Example:* every elementary function on $\mathbb{R}^n$ is continuous via this argument, and the net characterization lets one extend this routinely to weak topologies and other coarser settings.

The second disguised source is **$f$ is the restriction of a continuous function**. Property $B$: $f = g|_A$ for $g$ continuous on a larger space. The bridge: restrictions of continuous functions are continuous in the subspace topology. *Example:* the inclusion of a closed subset into $\mathbb{R}^n$ is continuous; restricting a smooth function on $\mathbb{R}^n$ to a manifold is continuous.

The third disguised source is **$f$ is the extension by limits of a function on a dense subset $A$**. Property $B$: $A$ is dense in $X$ and $f|_A$ is determined; $f$ is defined elsewhere by net-limits. The bridge: this theorem and the closure-via-nets theorem make extension by continuity work — every $x \in X = \overline{A}$ has a net in $A$ converging to it, and $f(x)$ must equal $\lim f(x_\alpha)$. Provided the net limit is independent of the net (this requires uniqueness, hence Hausdorff target), $f$ extends uniquely. *Example:* the Fourier transform on Schwartz functions extends to $L^2$ by density; the integral on simple functions extends to measurable functions by limits.

**Targets (Output Amplification)**

The conclusion is "$f$ preserves net limits".

Combine the conclusion with **a uniqueness argument**. Property $D$: $Y$ is Hausdorff. Amplified result $E$: continuous functions on $X$ are determined by their values on any dense subset $A \subseteq X$ — if $f|_A = g|_A$, then $f = g$. The bridge: every $x \in X$ has a net in $A$ converging to $x$ ([[Thm - Closure via Nets]] applied to $\overline{A} = X$); the image nets under $f, g$ are equal (since $f = g$ on $A$); by uniqueness of net limits in Hausdorff (see [[Thm - Hausdorff Iff Unique Net Limits]]), $f(x) = g(x)$. *Example:* this is the foundation of every "extension by continuity" argument.

Combine the conclusion with **a closed-graph or sequentially-continuous argument**. Property $D$: $X$ first-countable. Amplified result $E$: continuity is determined by sequential limits alone, recovering the metric-space characterization. *Example:* in $\mathbb{R}^n$, every continuity proof can be done with sequences alone; the net version simplifies to sequences without loss.

Combine the conclusion with **the composition $f \circ g$**. Property $D$: $g$ is also a net-preserving function. Amplified result $E$: the composition $f \circ g$ preserves nets — a net $x_\alpha \to x$ gives $g(x_\alpha) \to g(x)$ (continuity of $g$), then $f(g(x_\alpha)) \to f(g(x))$ (continuity of $f$). Hence $f \circ g$ is continuous by this theorem. *Example:* compositions of continuous functions are continuous, manifestly via net-preservation.

---

# Why Is It True

The forward direction (**continuous implies net-preserving**) is structural. Suppose $f$ is continuous, $x_\alpha \to x$ in $X$, and $V$ is a neighborhood of $f(x)$ in $Y$. Then $f^{-1}(V)$ is a neighborhood of $x$ in $X$ (preimage of open is open under continuity, and $f(x) \in V$ means $x \in f^{-1}(V)$, with $f^{-1}(V)$ open). By convergence of the net, $x_\alpha \in f^{-1}(V)$ eventually, hence $f(x_\alpha) \in V$ eventually. As $V$ was arbitrary, $f(x_\alpha) \to f(x)$.

The reverse direction (**net-preserving implies continuous**) is the substantive one. Suppose $f$ is *not* continuous — there is an open $V \subseteq Y$ with $f^{-1}(V)$ not open. So there is a point $x \in f^{-1}(V)$ that is *not* in the interior of $f^{-1}(V)$ — equivalently, *every* open neighborhood of $x$ contains a point *outside* $f^{-1}(V)$, i.e., a point $z$ with $f(z) \notin V$.

We construct a net witnessing the failure of net-preservation:

- *Index by neighborhoods of $x$*, ordered by reverse inclusion (same as in [[Thm - Closure via Nets]]).
- *At each $U$*, pick $x_U \in U$ with $f(x_U) \notin V$. This is possible by the failure of $x$ to be in the interior.
- The net $x_U \to x$ (same convergence argument as canonical-net for closure).
- But $f(x_U) \notin V$ for every $U$, and $f(x) \in V$. So $f(x_U) \not\to f(x)$: the image net is *never* in $V$, but $V$ is a neighborhood of $f(x)$.

So $f$ does not preserve this particular net. Contrapositively, if $f$ preserves every net, $f$ is continuous.

The geometric picture: failure of continuity at $x$ means *some neighborhood $V$ of $f(x)$ has a preimage that fails to contain a neighborhood of $x$*. So every neighborhood of $x$ "leaks" — has points whose image escapes $V$. By picking these leaking points systematically across a directed family of shrinking neighborhoods of $x$, one builds a net that approaches $x$ but whose images never reach $V$, breaking continuity.

The reverse direction is *exactly* the canonical-net construction of [[Thm - Closure via Nets]], applied to the set $A = X \setminus f^{-1}(V)$ (whose image escapes $V$). The fact that $x$ is in $\overline{A}$ — every neighborhood of $x$ meets $A$ — is the negation of "$f^{-1}(V)$ is open at $x$", and the canonical net in $A$ converging to $x$ witnesses the failure.

Why does this fail for sequences in non-first-countable spaces? Because the canonical net is indexed by *all* neighborhoods of $x$, which has the cardinality of the neighborhood basis. In a first-countable space, a countable basis lets the net collapse to a sequence and sequential continuity suffices. Without first countability, sequences may not exhaust the basis, and the canonical net argument requires the full directed-set generality.

---

# What Makes This Hard

The non-obvious step is the **reverse direction's canonical-net construction**: when $f$ fails to be continuous, one indexes by neighborhoods of the failure point $x$ and picks points whose images escape the offending open set $V$. The most common error is to attempt the reverse direction with sequences in non-first-countable spaces, where the canonical sequence may not exist; one then mistakenly concludes "sequential continuity equals continuity", which is false in general. A second common error is to conflate the index of the net with the value: the net is indexed by *neighborhoods of $x$*, not by points, but its *values* are points in $X$ — keeping these straight is essential.

---

# Rederivation Scaffold

**High-level strategy:**
Forward: preimage of a neighborhood of $f(x)$ is a neighborhood of $x$; net is eventually in the preimage, image is eventually in the neighborhood.
Reverse (contrapositive): if $f^{-1}(V)$ is not open at $x$, build a canonical net of points outside $f^{-1}(V)$ converging to $x$; the image net is outside $V$, contradicting net preservation since $f(x) \in V$.

**Subgoal decomposition:**

1. **(Forward, $\Rightarrow$) Continuity implies net preservation.** Net $x_\alpha \to x$; $V$ neighborhood of $f(x)$ in $Y$; $f^{-1}(V)$ is a neighborhood of $x$ in $X$; net eventually in $f^{-1}(V)$; image eventually in $V$.
   - *Hint:* Preimages of opens are open under continuity.

2. **(Reverse, $\Leftarrow$, contrapositive) Discontinuity implies a non-preserved net.** Suppose $f$ is not continuous: $V \subseteq Y$ open with $f^{-1}(V)$ not open. So there is $x \in f^{-1}(V)$ not in the interior of $f^{-1}(V)$.
   - *Hint:* "Not open" means some point is in the set but not in its interior.

3. **Every neighborhood of $x$ contains a point outside $f^{-1}(V)$.** By failure of interior.
   - *Hint:* Standard reformulation.
   - *Why needed:* Gives the points to put into the canonical net.

4. **Construct the canonical net.** $D = \mathcal{N}_x$ open neighborhoods of $x$, reverse inclusion ordering; pick $x_U \in U$ with $f(x_U) \notin V$ for each $U$.
   - *Hint:* Same construction as [[Thm - Closure via Nets]] but with the side condition $f(x_U) \notin V$.

5. **Verify $x_U \to x$.** By the canonical-net convergence argument.

6. **Verify $f(x_U) \not\to f(x)$.** Image is *never* in $V$, but $V$ is a neighborhood of $f(x)$, so net is not eventually in $V$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Continuity is equivalent to preimages of open neighborhoods being open neighborhoods
> **Statement:** $f : X \to Y$ is continuous iff for every $x \in X$ and every open neighborhood $V$ of $f(x)$, $f^{-1}(V)$ is an open neighborhood of $x$.
>
> **Hint:** Continuity = preimages of opens are open; restrict to neighborhoods of a chosen point.
>
> **Why needed:** It is what makes the forward direction immediate.
>
> > [!note]- Full proof
> > If $f$ is continuous, $V \subseteq Y$ open means $f^{-1}(V) \subseteq X$ open. If $f(x) \in V$, then $x \in f^{-1}(V)$, so $f^{-1}(V)$ is an open set containing $x$, i.e., an open neighborhood.
> >
> > Conversely, if preimages of open neighborhoods are open neighborhoods, then for any open $V \subseteq Y$, every $x \in f^{-1}(V)$ has $f^{-1}(V)$ as an open neighborhood, so $f^{-1}(V)$ is open (as it is a neighborhood of each of its points).

> [!note]- Lemma 2: Failure of continuity at $x$ produces a canonical "bad" net
> **Statement:** Let $V \subseteq Y$ be open with $f^{-1}(V)$ not open, and let $x \in f^{-1}(V)$ not be in the interior. Then there is a net $\{x_U\}$ in $X \setminus f^{-1}(V)$ converging to $x$, with $f(x_U) \notin V$ for all $U$.
>
> **Hint:** Index by neighborhoods of $x$, pick a point of $U \setminus f^{-1}(V)$ for each.
>
> **Why needed:** It is the contradiction-producing net.
>
> > [!note]- Full proof
> > $x \in f^{-1}(V)$ not in the interior means every open neighborhood of $x$ contains a point outside $f^{-1}(V)$. Index $D = \mathcal{N}_x$ by reverse inclusion. For each $U \in D$, pick $x_U \in U \setminus f^{-1}(V)$ (nonempty by hypothesis). Then $f(x_U) \notin V$ (definition of $f^{-1}(V)$).
> >
> > Convergence $x_U \to x$: for any neighborhood $W$ of $x$, indices $U \geq W$ (i.e., $U \subseteq W$) give $x_U \in U \subseteq W$. So the net is eventually in $W$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> ($\Rightarrow$) Suppose $f : X \to Y$ is continuous, and let $\{x_\alpha\}_{\alpha \in D}$ be a net in $X$ with $x_\alpha \to x$. Let $V$ be a neighborhood of $f(x)$ in $Y$; we may assume $V$ is open. By Lemma 1, $f^{-1}(V)$ is an open neighborhood of $x$. By convergence, there is $\alpha_0 \in D$ with $x_\alpha \in f^{-1}(V)$ for all $\alpha \geq \alpha_0$. Hence $f(x_\alpha) \in V$ for all $\alpha \geq \alpha_0$. As $V$ was arbitrary, $f(x_\alpha) \to f(x)$.
>
> ($\Leftarrow$, contrapositive) Suppose $f$ is not continuous. By Lemma 1, there is an open $V \subseteq Y$ and a point $x \in f^{-1}(V)$ such that $f^{-1}(V)$ is not a neighborhood of $x$ — i.e., $x$ is in $f^{-1}(V)$ but not in its interior.
>
> By Lemma 2, there is a net $\{x_U\}_{U \in \mathcal{N}_x}$ in $X$ converging to $x$ with $f(x_U) \notin V$ for all $U$. Since $V$ is an open neighborhood of $f(x)$ (because $x \in f^{-1}(V)$), the image net $\{f(x_U)\}$ is *never* in $V$, hence not eventually in $V$, so $f(x_U) \not\to f(x)$.
>
> So $f$ does not preserve net convergence at $x$. Contrapositively, if $f$ preserves all net convergence, $f$ is continuous. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Continuous extension to closure.** Let $A$ be dense in $X$, $f : A \to Y$ continuous with $Y$ Hausdorff, and suppose for every net $\{a_\alpha\}$ in $A$ converging to $x \in X$, the image net $\{f(a_\alpha)\}$ converges in $Y$ to a value depending only on $x$. Define $\tilde f(x) = \lim_\alpha f(a_\alpha)$. Then $\tilde f$ is continuous on $X$, and $\tilde f|_A = f$. The proof uses this theorem in both directions: forward to verify $\tilde f$ is well-defined, and reverse (via Lemma 2) to verify continuity. This is the universal "extension by density" argument in functional analysis.

**Distributional continuity via test-function nets.** A distribution $T \in \mathcal{D}'(\mathbb{R}^n)$ is continuous on the space of test functions $\mathcal{D}(\mathbb{R}^n)$, which is *not* first-countable (it has a complicated inductive-limit topology). So "sequentially continuous" is not enough — net-continuous is the right characterization. The Hahn–Banach style construction of distributions uses the net version of this theorem, building distributions as limits of nets of approximating functionals.

**The weak topology and weak-net continuity.** A function $f : V \to \mathbb{R}$ on a normed space $V$ is weak-continuous (continuous from the weak topology to $\mathbb{R}$) if and only if it preserves weak net convergence. The weak topology is rarely first-countable, so sequential weak continuity does not suffice. This theorem in the weak setting is the foundation of the calculus of variations: lower semicontinuity in the weak topology is exactly preservation of weak nets, and this is what makes minimization arguments work.

---

# Bridges

- **[[Thm - Closure via Nets]]** — the foundation. The proof of the reverse direction of this theorem is essentially the canonical-net construction of closure-via-nets, applied to the set $X \setminus f^{-1}(V)$. The two theorems together are the net characterization of basic topology.

- **[[Thm - Hausdorff Iff Unique Net Limits]]** — Hausdorffness of $Y$ makes "$\lim f(x_\alpha) = f(x)$" unambiguous, which is the operational form of continuity in analysis.

- **[[Def - First and Second Countable]]** — in first-countable $X$, nets reduce to sequences and "continuous = net-continuous = sequentially continuous". This is the metric-space special case.

- **[[Def - Continuous Map]]** — the open-set definition this theorem characterizes via nets.

- **Sequential continuity and the failure thereof.** In non-first-countable spaces, sequential continuity does *not* imply continuity. The standard counterexample is the **co-countable topology**: the topology on an uncountable set where opens are sets with countable complement (or empty). Sequences converge only when eventually constant, so every function is sequentially continuous, but not every function is continuous. This is the canonical illustration of why nets are necessary.

---

# Unlocked by This

> [!tip] **Weak Topologies in Functional Analysis** *(from Functional Analysis)*
> The **weak topology** on a normed space $V$ is the coarsest topology making all $\varphi \in V^*$ continuous. Functions on $V$ that are weak-continuous (i.e., preserve weak nets) are exactly the ones that can be expressed in terms of the dual. This theorem makes the net characterization the standard tool.

> [!tip] **Topological Vector Spaces and Distributions** *(from Functional Analysis)*
> The space of test functions $\mathcal{D}(\mathbb{R}^n)$ has an inductive-limit topology, not first-countable. Distributions are linear functionals continuous in this topology — i.e., net-continuous. The Schwartz space $\mathcal{S}(\mathbb{R}^n)$ is metrizable, but $\mathcal{D}(\mathbb{R}^n)$ is not, so the net theorem is essential.

> [!tip] **Categorical Continuity in Limits and Colimits** *(from Category Theory)*
> A functor is **continuous** if it preserves limits — categorical limits, which in topological categories include net-limit-like constructions. The continuity-via-nets theorem is the topological prototype of this categorical pattern: a structure-preserving map is one that preserves the limit operation.
