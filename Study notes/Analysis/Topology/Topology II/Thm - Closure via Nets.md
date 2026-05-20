---
type: theorem
subject: topology
prereqs:
  - "Def - Directed Set and Net"
  - "Def - Net Convergence"
  - "Def - Closure, Interior, and Boundary"
  - "Def - Topological Space"
tags: [analysis, topology, nets, closure]
---

# Notation

$X$ is a [[Def - Topological Space|topological space]], $A \subseteq X$ a subset, $\overline{A}$ the [[Def - Closure, Interior, and Boundary|closure]] of $A$. A **net** in $A$ is a function $\Phi : D \to A$ from a [[Def - Directed Set and Net|directed set]] $D$ into $A$. The net **converges to** $x \in X$, written $x_\alpha \to x$, if for every neighborhood $U$ of $x$ there is $\alpha_0 \in D$ with $x_\alpha \in U$ for all $\alpha \geq \alpha_0$ (see [[Def - Net Convergence]]). The full registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Theorem.** Let $X$ be a topological space, $A \subseteq X$. Then $x \in \overline{A}$ if and only if there exists a net $\{x_\alpha\}_{\alpha \in D}$ with $x_\alpha \in A$ for all $\alpha$ and $x_\alpha \to x$.

In a [[Def - First and Second Countable|first-countable]] space (e.g., a metric space), one can replace "net" by "sequence". In a general topological space, the sequence version is *false*: closures can contain points not reachable by any sequence (the canonical example is $\omega_1$ in the order topology, where the supremum is in the closure of $[0, \omega_1)$ but no sequence in $[0, \omega_1)$ converges to it).

---

# Motivation

In a metric space, every concept can be phrased in terms of sequences: $x \in \overline{A}$ if and only if a sequence in $A$ converges to $x$; $f$ is continuous if and only if it preserves sequential limits; compactness equals sequential compactness. These sequential characterizations are what make metric topology so usable — sequences are easy to construct, manipulate, and visualize.

In a general topological space, *these characterizations fail*. There exist spaces with points in closures unreachable by any sequence; functions that preserve every sequential limit but are not continuous; compact spaces that are not sequentially compact. The reason: sequences are indexed by $\mathbb{N}$, which is rigid and countable, but a neighborhood basis at a point in a general space can have *higher cardinality* — there is no way to "exhaust" the basis with a sequence.

The cure is to *replace $\mathbb{N}$ with an arbitrary directed set*. A net is a function from a directed set to $X$; convergence is the same eventual-in-every-neighborhood condition. With this generalization, every sequential theorem of metric topology restores in full generality: closure equals net-limits (this theorem), continuity equals net-preservation ([[Thm - Continuity via Nets]]), compactness equals convergent-subnet-existence (in [[Def - Compact Space]]'s third formulation), Hausdorff equals unique-net-limits ([[Thm - Hausdorff Iff Unique Net Limits]]).

This theorem is the foundational one — it makes nets *useful* by characterizing closure operationally. From "closure" one can derive "boundary", "interior", "open", "closed" — every basic point-set notion. So once closure has a net characterization, all the basic notions do, and the entire metric intuition transfers to abstract spaces.

The reason the theorem is *true* is structural: a point $x$ is in the closure of $A$ if and only if every neighborhood of $x$ meets $A$. To produce a net converging to $x$, *index by neighborhoods* (or a basis of them) ordered by reverse inclusion, and pick one point of $A \cap U$ for each neighborhood $U$. This is the canonical construction, and it makes the equivalence almost mechanical.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$x \in \overline{A}$".

The first disguised source is **$A$ is dense in $X$**. Property $B$: $\overline{A} = X$. The bridge: every point of $X$ is in $\overline{A}$, so this theorem applies universally. *Example:* $\mathbb{Q}$ is dense in $\mathbb{R}$, so every real is a limit of a sequence (in this case, a sequence, since $\mathbb{R}$ is metric) of rationals — the standard $a$-adic, decimal, continued fraction expansions. More generally, smooth functions are dense in $L^p$, polynomials in $C[0, 1]$, etc. — every density theorem becomes a "net of approximations exists" theorem via this.

The second disguised source is **$x$ is a limit point of $A$**. Property $B$: every neighborhood of $x$ meets $A \setminus \{x\}$. The bridge: closure equals $A \cup \{$limit points$\}$, so a limit point is in the closure. *Example:* the irrationals have $0$ as a limit point, hence a (net or, here, sequence) of irrationals converges to $0$.

The third disguised source is **$A$ has $x$ as a boundary point, weak limit, distributional limit, or measure-theoretic boundary**. Property $B$: $x$ is reached by $A$ in any of these weaker senses. The bridge: most "limit" notions in functional analysis (weak convergence, distributional convergence, measure-theoretic almost-everywhere) are topological convergence on suitable function spaces, where this theorem applies. *Example:* a sequence converges weakly in a Banach space if and only if it converges in the weak topology, which is metrizable on bounded sets of separable spaces (so sequences suffice) but in general requires nets.

**Targets (Output Amplification)**

The conclusion is "$x$ is the limit of a net in $A$".

Combine the conclusion with **the continuity of a function $f$**. Property $D$: $f$ is continuous. Amplified result $E$: $f(x)$ is the limit of the image net $f(x_\alpha) \in f(A)$, hence $f(x) \in \overline{f(A)}$. This is the standard "$f$ extends to closure" argument: from a net in $A$ converging to $x$, the image net converges to $f(x)$, so $f$'s behavior at $x$ is forced by its behavior on $A$. *Example:* if $f|_A$ is determined and $A$ is dense, then $f$ on $X$ is determined (assuming the target is Hausdorff).

Combine the conclusion with **a topological vector space and net approximation by a dense subspace**. Property $D$: a dense subspace $V_0 \subseteq V$ in a topological vector space. Amplified result $E$: bounded linear maps on $V_0$ extend uniquely to $V$ (BLT — bounded linear transformation — theorem). The bridge: the net of $V_0$-approximations to any $v \in V$ has its $f$-image converging by continuity, and the limit is the extension. *Example:* the Fourier transform is defined first on Schwartz functions and extended to $L^2$ by density and continuity.

Combine the conclusion with **the compactness of $\overline{A}$**. Property $D$: $\overline{A}$ is compact in $X$. Amplified result $E$: every net in $A$ has a convergent subnet, with limit in $\overline{A}$. This combines the net-characterization of closure with the net-characterization of compactness. *Example:* in functional analysis, if $A$ is a bounded set in a reflexive Banach space, then $\overline{A}$ is weakly compact (Eberlein–Šmulian), and every net in $A$ has a weakly convergent subnet.

---

# Why Is It True

The proof has two directions, both straightforward once the canonical net is identified.

**($\Leftarrow$) If a net in $A$ converges to $x$, then $x \in \overline{A}$.** Suppose $\{x_\alpha\}_{\alpha \in D}$ is a net in $A$ converging to $x$. For every neighborhood $U$ of $x$, the net is eventually in $U$, so there is some $\alpha$ with $x_\alpha \in U$. But $x_\alpha \in A$, so $A \cap U \neq \emptyset$. Since every neighborhood of $x$ meets $A$, $x$ is in $\overline{A}$ by the standard characterization of closure.

**($\Rightarrow$) If $x \in \overline{A}$, construct a net in $A$ converging to $x$.** This is the substantive direction, and it uses a canonical construction: *index the net by neighborhoods of $x$*.

- Let $D = \mathcal{N}_x$, the set of open neighborhoods of $x$, ordered by reverse inclusion: $U \leq V$ iff $U \supseteq V$ (smaller-or-equal in our partial order means *larger* as a set). Equivalently, $U \geq V$ iff $U \subseteq V$.
- This is a directed set: given $U_1, U_2$, the intersection $U_1 \cap U_2$ is an open neighborhood of $x$ (open sets closed under finite intersection, both contain $x$), and $U_1 \cap U_2 \geq U_1, U_2$ in the order.
- For each $U \in D$, since $x \in \overline{A}$, $A \cap U \neq \emptyset$. Choose $x_U \in A \cap U$ (Axiom of Choice).
- This defines a net $\{x_U\}_{U \in D}$ in $A$.
- *Convergence to $x$:* given any neighborhood $W$ of $x$, $W \in D$. For any $U \geq W$, $U \subseteq W$, so $x_U \in U \subseteq W$. Hence the net is eventually in $W$. So $x_U \to x$.

The construction is sometimes called the "**canonical net**" or "**net of neighborhoods**". It is the prototype for every net construction in topology: directed sets indexed by some structural information about a point or a property (neighborhoods, finite subsets, finite covers), with reverse-inclusion-like ordering, and a value chosen using the hypothesis. This pattern recurs throughout: the net witnessing non-Hausdorff in [[Thm - Hausdorff Iff Unique Net Limits]], the net constructed for compactness arguments, the FIP-based net in [[Def - Compact Space|compactness equivalences]].

The reason the construction *works* is that the reverse-inclusion ordering captures "shrinking towards $x$": as the index $U$ grows in the partial order, $U$ shrinks as a set towards $x$. So the net values $x_U \in U$ are forced into ever-smaller neighborhoods of $x$, which is precisely what convergence demands.

Why does this fail for sequences in general? Because the indexing $D$ — all open neighborhoods of $x$ — can have arbitrary cardinality. In a metric space, the countable neighborhood basis $\{B_{1/n}(x)\}_{n \in \mathbb{N}}$ suffices, and the net collapses to a sequence. In non-first-countable spaces, no countable basis exists, and the directed-set generalization is essential.

---

# What Makes This Hard

The non-obvious step is constructing the **canonical net indexed by neighborhoods of $x$ ordered by reverse inclusion**. Beginners often try to use a *fixed* index set (e.g., $\mathbb{N}$) and find it impossible in non-first-countable spaces. The most common error is to forget that the order is *reverse* inclusion — that "larger in the directed set" means "smaller as a set" — which inverts the direction of convergence. A second pitfall is forgetting the Axiom of Choice: choosing $x_U \in A \cap U$ for each of possibly uncountably many $U$ requires AC, and this is a real (mild) use of choice baked into general-topology net arguments.

---

# Rederivation Scaffold

**High-level strategy:**
The reverse direction is immediate: a net eventually in any neighborhood meets $A$ in each, so $x \in \overline{A}$ by the closure characterization. The forward direction is the canonical construction: index by neighborhoods of $x$, reverse-inclusion-ordered; pick a point of $A \cap U$ for each; verify convergence.

**Subgoal decomposition:**

1. **(Reverse, $\Leftarrow$) A net in $A$ converging to $x$ forces $x \in \overline{A}$.** For any neighborhood $U$ of $x$, the net is eventually in $U$, so $A \cap U \neq \emptyset$.
   - *Hint:* The closure of $A$ is the set of points every neighborhood of which meets $A$.
   - *Why needed:* The easy direction.

2. **(Forward, $\Rightarrow$) Index by neighborhoods of $x$.** $D = \mathcal{N}_x$ open neighborhoods of $x$, ordered by $U \geq V \iff U \subseteq V$. Verify this is directed.
   - *Hint:* Intersection of two open neighborhoods is an open neighborhood.

3. **Choose net values.** For each $U \in D$, pick $x_U \in A \cap U$ (nonempty by $x \in \overline{A}$).
   - *Hint:* Axiom of Choice.
   - *Why needed:* This is the canonical net.

4. **Verify convergence $x_U \to x$.** For any neighborhood $W$ of $x$, all indices $U \geq W$ (i.e., $U \subseteq W$) have $x_U \in U \subseteq W$, so the net is eventually in $W$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Open neighborhoods of $x$ ordered by reverse inclusion form a directed set
> **Statement:** Let $\mathcal{N}_x$ be the set of open neighborhoods of $x \in X$, with $U \geq V \iff U \subseteq V$. Then $(\mathcal{N}_x, \geq)$ is a directed set.
>
> **Hint:** Upper bound of $U, V$ is $U \cap V$.
>
> **Why needed:** It is the index set for the canonical net.
>
> > [!note]- Full proof
> > Reflexivity and transitivity of $\geq$ follow from those of $\subseteq$. For directedness: given $U_1, U_2 \in \mathcal{N}_x$, $U_1 \cap U_2$ is open (open sets closed under finite intersection) and contains $x$ (both $U_1$ and $U_2$ do). So $U_1 \cap U_2 \in \mathcal{N}_x$, and $U_1 \cap U_2 \subseteq U_1, U_2$ in the set inclusion order, which translates to $U_1 \cap U_2 \geq U_1, U_2$ in the directed-set order.

> [!note]- Lemma 2: The closure characterization — $x \in \overline{A}$ iff every neighborhood of $x$ meets $A$
> **Statement:** For any $A \subseteq X$ and $x \in X$, $x \in \overline{A}$ if and only if every open neighborhood of $x$ has nonempty intersection with $A$.
>
> **Hint:** $\overline{A}$ is the set of points $x$ such that $x$ is in every closed set containing $A$, equivalently $x$ is not in any open set disjoint from $A$.
>
> **Why needed:** It is the standard fact connecting closure to neighborhoods, used in both directions.
>
> > [!note]- Full proof
> > $x \notin \overline{A}$ means $x$ is in the complement of $\overline{A}$, which is open (since $\overline{A}$ is closed). So there is an open neighborhood $U$ of $x$ with $U \subseteq X \setminus \overline{A} \subseteq X \setminus A$, i.e., $U \cap A = \emptyset$.
> >
> > Contrapositively: $x \in \overline{A}$ iff no open neighborhood of $x$ is disjoint from $A$, i.e., every open neighborhood of $x$ has nonempty intersection with $A$.

> [!note]- Lemma 3: The canonical net $x_U \in A \cap U$ converges to $x$
> **Statement:** Let $x \in \overline{A}$, $D = \mathcal{N}_x$ ordered by reverse inclusion, and pick $x_U \in A \cap U$ for each $U \in D$. Then $x_U \to x$.
>
> **Hint:** Indices $\geq W$ have $x_U \in U \subseteq W$.
>
> **Why needed:** This is the forward direction of the theorem.
>
> > [!note]- Full proof
> > Fix any neighborhood $W$ of $x$. $W$ contains an open neighborhood $W' \subseteq W$ of $x$ (by definition of neighborhood), and $W' \in \mathcal{N}_x = D$. For any $U \in D$ with $U \geq W'$, by definition of the order $U \subseteq W'$, so $x_U \in A \cap U \subseteq U \subseteq W' \subseteq W$. So the net is eventually in $W$. Since $W$ was arbitrary, $x_U \to x$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> ($\Leftarrow$) Suppose $\{x_\alpha\}_{\alpha \in D}$ is a net in $A$ with $x_\alpha \to x$. Let $U$ be any open neighborhood of $x$. By convergence, there is $\alpha_0 \in D$ with $x_\alpha \in U$ for all $\alpha \geq \alpha_0$. Choose any such $\alpha$; then $x_\alpha \in U$ and $x_\alpha \in A$, so $A \cap U \neq \emptyset$. As $U$ was arbitrary, by Lemma 2, $x \in \overline{A}$.
>
> ($\Rightarrow$) Suppose $x \in \overline{A}$. By Lemma 1, $D = \mathcal{N}_x$ with reverse-inclusion ordering is a directed set. For each $U \in D$, Lemma 2 gives $A \cap U \neq \emptyset$; choose $x_U \in A \cap U$ (Axiom of Choice). This defines a net $\{x_U\}_{U \in D}$ in $A$, which by Lemma 3 converges to $x$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Density of $\mathbb{Q}$ in $\mathbb{R}$ via nets.** $\mathbb{R}$ is metric, hence first-countable, so the net characterization reduces to the sequential one. The decimal-expansion sequence $q_n$ for any $r \in \mathbb{R}$ is a net (indexed by $\mathbb{N}$) in $\mathbb{Q}$ converging to $r$. This gives by this theorem $r \in \overline{\mathbb{Q}} = \mathbb{R}$. The application is the trivial case, but it shows the net theorem reduces to the familiar density argument in metric spaces.

**A closure not reached by any sequence: $\omega_1$ in the ordinal space.** Let $X = [0, \omega_1]$ with the order topology, $A = [0, \omega_1)$ (everything below $\omega_1$). Then $\omega_1 \in \overline{A}$ (every neighborhood of $\omega_1$ in the order topology contains an interval $(\alpha, \omega_1]$ for some $\alpha < \omega_1$, which meets $A$). But *no sequence* in $A$ converges to $\omega_1$: any sequence $\{\alpha_n\}$ in $[0, \omega_1)$ has a countable supremum $\sup_n \alpha_n < \omega_1$ (the supremum of countably many countable ordinals is countable), so the sequence is eventually in $[0, \sup_n \alpha_n]$, which is a *closed* set in $[0, \omega_1]$ not containing $\omega_1$. The *net* of all ordinals in $[0, \omega_1)$ ordered by themselves *does* converge to $\omega_1$, witnessing closure as the theorem promises. This is the canonical counterexample showing sequences are insufficient.

**Cauchy sequences and completeness.** In a metric space, $x \in \overline{A}$ if and only if a sequence in $A$ converges to $x$. The completeness of a metric space is the statement that *every Cauchy sequence converges* — equivalently, every "Cauchy-like net of approximations" has a limit. In the abstract topological setting (e.g., uniform spaces), one uses *Cauchy nets* and the net characterization of closure to define completeness. This generalizes Cauchy completeness from metric spaces to uniform spaces, the proper home for the concept.

---

# Bridges

- **[[Thm - Continuity via Nets]]** — the companion theorem characterizing continuity. Together: closure (this theorem) and continuity (the companion) give the complete net-theoretic restatement of topology, lifting the metric intuition to arbitrary spaces.

- **[[Thm - Hausdorff Iff Unique Net Limits]]** — Hausdorffness in net language: if every convergent net has a unique limit, then $X$ is Hausdorff. Combined with this theorem, in a Hausdorff space the net characterization of closure has the bonus that the limit is unique — making "the limit of a net in $A$" a well-defined notion.

- **[[Def - First and Second Countable]]** — when $X$ is first-countable, nets can be replaced by sequences in this theorem and its companions. This is what makes metric-space topology "sequential" and powers the standard sequential characterizations.

- **The closure characterization via net-limits is the bridge from metric topology to general topology.** Every sequential argument in metric topology (continuity, closure, compactness, completeness) becomes a net argument in general topology, with the canonical neighborhood-indexed net as the universal substitute for sequences.

---

# Unlocked by This

> [!tip] **Continuity via Nets** *(Companion Theorem)*
> $f$ is continuous if and only if $f$ preserves net convergence. The proof uses this theorem: $x \in \overline{A}$ has a net in $A$ converging to $x$; continuity sends it to a net in $f(A)$ converging to $f(x)$; hence $f(x) \in \overline{f(A)}$, which is the topological definition of continuity in terms of preimages of closed sets.

> [!tip] **Compactness via Convergent Subnets** *(from Topology II)*
> $X$ is compact iff every net in $X$ has a convergent subnet. The proof uses the FIP characterization of compactness, the canonical-net construction (much like this theorem), and the existence of universal subnets ([[Thm - Every Net Has a Universal Subnet]]).

> [!tip] **Weak Compactness in Functional Analysis** *(from Functional Analysis)*
> The weak compactness of bounded sets in reflexive Banach spaces, and the [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Banach–Alaoglu theorem]] for weak-$*$ compactness of the dual unit ball, are net-theoretic compactness statements proved using the net characterization of closure. The "weak limit of a net of approximations" is precisely the net construction of this theorem applied to the weak topology.
