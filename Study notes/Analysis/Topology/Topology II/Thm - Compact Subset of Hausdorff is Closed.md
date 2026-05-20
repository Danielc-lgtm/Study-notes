---
type: theorem
subject: topology
prereqs:
  - "Def - Compact Space"
  - "Def - Separation Axioms"
  - "Def - Topological Space"
tags: [analysis, topology, compactness, separation]
---

# Notation

$X$ is a [[Def - Topological Space|topological space]], $A \subseteq X$ a subset, both equipped with the appropriate topology ($X$ its own, $A$ the [[Def - Subspace Topology|subspace topology]]). $A$ is **compact** (see [[Def - Compact Space]]) if every open cover has a finite subcover. $X$ is **Hausdorff** ([[Def - Separation Axioms|T₂]]) if any two distinct points have disjoint open neighborhoods. The full registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Theorem.** Let $X$ be a Hausdorff topological space and $A \subseteq X$ a compact subset. Then $A$ is **closed** in $X$.

The proof exhibits the complement of $A$ as open: for each $x \in X \setminus A$, separate $x$ from every point of $A$ using Hausdorff, extract a finite subcover of $A$ via compactness, intersect the finitely many opens around $x$ to get a neighborhood of $x$ disjoint from $A$.

---

# Motivation

In a general topological space, compactness is *not* a closure-implying condition. In the cofinite topology on $\mathbb{N}$, every subset is compact (every open cover has all but finitely many of $\mathbb{N}$ in one open set, plus the rest in finitely many opens), but the only closed sets are finite sets and $\mathbb{N}$ itself. So most compact subsets are not closed. The Hausdorff hypothesis is what makes compactness imply closure.

The question this theorem answers is: *when can compactness automatically upgrade to closure*? The answer is precisely Hausdorffness. The mechanism is structural: Hausdorff means we can separate any external point from any internal point by disjoint opens; compactness lets us finitize the separation; the result is a single open neighborhood of the external point disjoint from the entire compact set, making the complement open.

The geometric picture: in a Hausdorff space, compactness is "geometric finiteness" — the set is "small enough" that it can be sealed off by a single open neighborhood around any external point. Without Hausdorff, points and compact sets can be "topologically entangled" — every neighborhood of one point meets every neighborhood of another — and the separation fails.

The pragmatic value: this theorem is one of the two "automatic upgrades" of compactness, the other being the closed-map property of continuous maps from compact to Hausdorff ([[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]]). Together they make "compact + Hausdorff" the gold-standard pair of hypotheses in topology. Every compact subset of a Hausdorff space is automatically closed, hence carries all the structural niceness of closed sets — limits in it stay in it, it is a "rigid" subobject.

This theorem also underlies the closed-graph theorem in functional analysis and the embedding theorems in algebraic geometry (where "proper morphism" — the algebraic analog of "compact in Hausdorff" — gives a closed image automatically). The general principle: compactness + Hausdorff = "honest closed subset", with all the implications that brings.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$X$ Hausdorff, $A \subseteq X$ compact".

The first disguised source is **$X$ is a metric space**. Property $B$: $X$ has a metric. The bridge: every metric space is Hausdorff (disjoint open balls separate distinct points). *Example:* every compact subset of $\mathbb{R}^n$ is closed — the standard fact, proven via this theorem.

The second disguised source is **$X$ is locally compact Hausdorff**, or more generally has any standard separation property. Property $B$: $X$ has a strong separation property implying Hausdorff. The bridge: locally compact Hausdorff is a special case of Hausdorff. *Example:* every compact subset of a Lie group (a locally compact Hausdorff topological group) is closed.

The third disguised source is **$A$ is the continuous image of a compact space**. Property $B$: $A = f(K)$ with $K$ compact, $f$ continuous. The bridge: $A$ is compact by [[Thm - Continuous Image of a Compact Space]], hence (in a Hausdorff target) closed by this theorem. *Example:* the image of a continuous loop $\gamma : S^1 \to X$ in a Hausdorff space $X$ is a closed compact subset.

**Targets (Output Amplification)**

The conclusion is "$A$ is closed in $X$".

Combine the conclusion with **a continuous bijection $f : K \to A$ from a compact source**. Property $D$: $K$ compact, $f$ continuous bijection. Amplified result $E$: $f$ is a closed map (the image of any closed subset of $K$ is compact by [[Thm - Closed Subset of Compact is Compact]] and [[Thm - Continuous Image of a Compact Space]], hence closed by this theorem). Hence $f^{-1}$ is continuous and $f$ is a homeomorphism. This is [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism|the homeomorphism criterion]].

Combine the conclusion with **a sequence (or net) of points $\{a_n\} \subseteq A$ converging in $X$**. Property $D$: $a_n \to x$ in $X$. Amplified result $E$: $x \in A$. The bridge: closure-via-nets and the closedness of $A$ from this theorem. *Example:* limits of points in a compact subset of a Hausdorff space stay in the compact subset — a basic but essential closure property used throughout analysis.

Combine the conclusion with **the intersection of $A$ with another closed set $B$**. Property $D$: $B$ closed in $X$. Amplified result $E$: $A \cap B$ is closed in $A$ and in $X$, and compact (closed subset of compact $A$, see [[Thm - Closed Subset of Compact is Compact]]). *Example:* the intersection of a compact set with a closed set is compact — used in extracting compact subdomains for analysis.

---

# Why Is It True

The intuition: in a Hausdorff space, every point outside the compact set $A$ can be "sealed off" from $A$ by a single open neighborhood — and "sealed off" is exactly what makes the complement of $A$ open, hence $A$ closed.

The mechanism is *Hausdorff at every point, compactness for finiteness*:

1. Fix $x \in X \setminus A$. We want to find an open neighborhood of $x$ disjoint from $A$.

2. For each $a \in A$, since $x \neq a$ and $X$ is Hausdorff, choose disjoint opens $U_a \ni x$ and $V_a \ni a$.

3. The family $\{V_a\}_{a \in A}$ is an open cover of $A$ (since each $a$ is in $V_a$).

4. By compactness of $A$, extract a finite subcover $\{V_{a_1}, \ldots, V_{a_n}\}$ — so $A \subseteq V_{a_1} \cup \cdots \cup V_{a_n}$.

5. The corresponding intersection $U = U_{a_1} \cap \cdots \cap U_{a_n}$ is open (finite intersection of opens), contains $x$ (each $U_{a_i}$ does), and is disjoint from $V_{a_1} \cup \cdots \cup V_{a_n}$ (each $U_{a_i}$ is disjoint from $V_{a_i}$, and the intersection is contained in each $U_{a_i}$).

6. So $U$ is a neighborhood of $x$ disjoint from $A$ (since $A$ is contained in the union of the $V_{a_i}$, and $U$ is disjoint from it).

Hence $X \setminus A$ is open at each of its points, so $A$ is closed.

The geometric picture: imagine $A$ as a cloud, and $x$ as a point outside it. Hausdorff lets us put a tiny "shield" $U_a$ around $x$ for each $a \in A$, paired with a corresponding "blob" $V_a$ around $a$ that does not touch $U_a$. Compactness lets us finitize the blobs into a finite cover of $A$. The intersection of the finitely many shields is still an open neighborhood of $x$ — and crucially, it is disjoint from *all* the finitely many blobs, hence from $A$.

The non-obviousness is step 5: *intersecting* finitely many shields gives an open neighborhood disjoint from the *union* of the corresponding blobs. This is the structural payoff of the finite-subcover extraction.

Why does this fail without Hausdorff? Without Hausdorff, step 2 fails — one cannot separate $x$ from each $a \in A$. The finitization works (compactness still applies), but there is no pair of opens to finitize *over*. So the proof breaks at the very first step.

---

# What Makes This Hard

The non-obvious step is realizing that the *intersection of the finitely many "shields" $U_{a_i}$* is open (finite intersection) and disjoint from the *union* of the corresponding "blobs" $V_{a_i}$. The two operations — intersection on the shield side, union on the blob side — are paired, and the disjointness is preserved because each individual $U_{a_i}$ is disjoint from each individual $V_{a_i}$, and intersecting on the shield side keeps the disjointness. The most common error is to try to use only one pair $(U_a, V_a)$ for a fixed $a$, which gives a neighborhood of $x$ disjoint from $V_a$ but not from all of $A$. A second pitfall is forgetting that the *finite* intersection in step 5 is the only intersection that remains open; an infinite intersection of opens need not be open.

---

# Rederivation Scaffold

**High-level strategy:**
For each $x \notin A$, build an open neighborhood of $x$ disjoint from $A$. Use Hausdorff to separate $x$ from each $a \in A$ by a pair of disjoint opens, compactness to extract a finite subcover of $A$ by the $V_a$ side, and intersect the corresponding $U_a$ side to get a single open neighborhood of $x$ disjoint from the finite cover, hence from $A$.

**Subgoal decomposition:**

1. **Fix $x \in X \setminus A$.** The goal is an open neighborhood of $x$ disjoint from $A$.
   - *Hint:* This makes $X \setminus A$ open at $x$.

2. **For each $a \in A$, separate $x$ from $a$.** By Hausdorff, choose disjoint opens $U_a \ni x$, $V_a \ni a$.
   - *Hint:* The Hausdorff axiom applied pointwise.

3. **The $V_a$ family covers $A$.** Each $a \in V_a$, so $\{V_a\}_{a \in A}$ covers $A$.

4. **Extract a finite subcover.** $A \subseteq V_{a_1} \cup \cdots \cup V_{a_n}$ by compactness.
   - *Hint:* Compactness applied to the cover.

5. **Intersect the corresponding $U_{a_i}$.** $U = U_{a_1} \cap \cdots \cap U_{a_n}$ is open, contains $x$, and is disjoint from $A$.
   - *Hint:* Finite intersection of opens is open; disjointness follows because each $U_{a_i}$ is disjoint from $V_{a_i}$, and $U \subseteq U_{a_i}$ for each $i$.

6. **Conclude $X \setminus A$ is open.** Every point of $X \setminus A$ has an open neighborhood in $X \setminus A$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Hausdorff gives pointwise separation of an external point from each internal point
> **Statement:** Let $X$ be Hausdorff, $A \subseteq X$, $x \in X \setminus A$. For each $a \in A$, there are disjoint opens $U_a \ni x$ and $V_a \ni a$.
>
> **Hint:** Direct Hausdorff application — distinct points $x, a$ get separated.
>
> **Why needed:** It is the building block of the separation construction.
>
> > [!note]- Full proof
> > Since $x \in X \setminus A$ and $a \in A$, $x \neq a$. By Hausdorffness, there exist disjoint open $U_a, V_a$ with $x \in U_a$, $a \in V_a$.

> [!note]- Lemma 2: Finite intersection of separating opens is disjoint from union of paired opens
> **Statement:** Let $\{(U_i, V_i)\}_{i=1}^n$ be pairs of disjoint opens (each $U_i \cap V_i = \emptyset$). Set $U = \bigcap_{i=1}^n U_i$ and $V = \bigcup_{i=1}^n V_i$. Then $U \cap V = \emptyset$.
>
> **Hint:** $U \subseteq U_i$ for each $i$, and $U_i$ is disjoint from $V_i$.
>
> **Why needed:** It is the key combinatorial step.
>
> > [!note]- Full proof
> > Suppose $z \in U \cap V$. Then $z \in V$ means $z \in V_i$ for some $i$. And $z \in U \subseteq U_i$. So $z \in U_i \cap V_i = \emptyset$, contradiction.

> [!note]- Lemma 3: A set is closed iff its complement is open at every point
> **Statement:** A set $A \subseteq X$ is closed iff for every $x \in X \setminus A$ there is an open neighborhood of $x$ contained in $X \setminus A$.
>
> **Hint:** Open = neighborhood of every point.
>
> **Why needed:** It is what we are checking.
>
> > [!note]- Full proof
> > $A$ closed $\iff X \setminus A$ open $\iff$ for every $x \in X \setminus A$, there is an open set $U$ with $x \in U \subseteq X \setminus A$ (by definition of open: a set is open iff it is a neighborhood of each of its points).

---

# Formal Proof

> [!note]- Complete formal proof
>
> Let $X$ be Hausdorff and $A \subseteq X$ compact. We show $X \setminus A$ is open.
>
> Fix $x \in X \setminus A$. For each $a \in A$, by Lemma 1 there are disjoint opens $U_a \ni x$ and $V_a \ni a$.
>
> The family $\{V_a\}_{a \in A}$ is an open cover of $A$ (since each $a \in V_a$). By compactness of $A$, there is a finite subcover: $A \subseteq V_{a_1} \cup \cdots \cup V_{a_n}$ for some $a_1, \ldots, a_n \in A$.
>
> Set $U = U_{a_1} \cap \cdots \cap U_{a_n}$. This is a finite intersection of opens, hence open. It contains $x$ (each $U_{a_i}$ does). By Lemma 2 applied to the pairs $(U_{a_i}, V_{a_i})$, $U$ is disjoint from $V_{a_1} \cup \cdots \cup V_{a_n} \supseteq A$. So $U \subseteq X \setminus A$.
>
> Hence $x$ has the open neighborhood $U \subseteq X \setminus A$. By Lemma 3, $A$ is closed. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Compact subsets of $\mathbb{R}^n$ are closed.** This is one direction of [[Thm - Heine–Borel Theorem|Heine–Borel]] in $\mathbb{R}^n$. The argument: $\mathbb{R}^n$ is Hausdorff (metric), so every compact subset is closed by this theorem. Combined with "compact in metric is bounded", we get the closed-and-bounded characterization. The application makes the abstract theorem concrete in the most-used setting.

**The image of a compact space under a continuous map to Hausdorff is closed.** Combine [[Thm - Continuous Image of a Compact Space]] and this theorem: $f : K \to Y$ continuous, $K$ compact, $Y$ Hausdorff. Then $f(K) \subseteq Y$ is compact (by the image theorem), hence closed in $Y$ (by this theorem). The application is the **closed-map property** of continuous maps from compact to Hausdorff, which is what makes [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism|the homeomorphism criterion]] true.

**Closed graphs of continuous functions in Hausdorff targets.** A continuous function $f : X \to Y$ with $Y$ Hausdorff has *closed graph* $\Gamma_f = \{(x, f(x)) : x \in X\} \subseteq X \times Y$. The proof: the graph is the preimage of the diagonal $\Delta_Y = \{(y, y) : y \in Y\}$ under the continuous map $(x, y) \mapsto (f(x), y)$, and $\Delta_Y$ is closed in $Y \times Y$ since $Y$ is Hausdorff. The application uses the closed-diagonal characterization of Hausdorff (the *dual* form of the unique-net-limits characterization) to extract closedness of the graph. This is the foundation of the closed graph theorem in functional analysis.

**Algebraic-geometric properness.** A morphism of schemes $f : X \to Y$ is **proper** if it is universally closed and separated (the scheme-theoretic analog of "image is closed and target is Hausdorff"). For varieties over $\mathbb{C}$, a morphism is proper if and only if the corresponding map of complex points is compact-fiber and the image is closed — exactly the closed-image property this theorem provides in the topological setting. The application is the cross-categorical translation: this topology theorem becomes the definition of *properness* in algebraic geometry, with all its consequences for cohomology and base change.

---

# Bridges

- **[[Def - Separation Axioms]]** — Hausdorff is the hypothesis. This theorem is one of the two "automatic upgrades" Hausdorffness provides for compact sets, the other being [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism|the homeomorphism criterion]] via the closed-map property.

- **[[Thm - Closed Subset of Compact is Compact]]** — the converse direction: closed subsets of compact are compact. Combined with this theorem, the closed and compact subsets of a compact Hausdorff space coincide.

- **[[Thm - Continuous Image of a Compact Space]]** — provides the supply of compact sets in $Y$ from continuous maps. Combined with this theorem, gives the closed-map property in the compact-to-Hausdorff setting.

- **[[Thm - Hausdorff Iff Unique Net Limits]]** — the net-theoretic characterization of Hausdorff. This theorem is the closure-theoretic consequence — Hausdorff gives both unique limits and closedness of compact sets.

- **[[Thm - Heine–Borel Theorem]]** — concretizes this theorem in $\mathbb{R}^n$: compact = closed + bounded. Half of the Heine-Borel statement is exactly this theorem applied in $\mathbb{R}^n$ (which is Hausdorff metric).

---

# Unlocked by This

> [!tip] **Closed-Map Property of Compact-to-Hausdorff Maps** *(from Topology II)*
> A continuous map $f : X \to Y$ with $X$ compact and $Y$ Hausdorff is a *closed map*: $f(F)$ is closed for every closed $F \subseteq X$. The proof combines [[Thm - Closed Subset of Compact is Compact]] (closed subsets of $X$ are compact) with [[Thm - Continuous Image of a Compact Space]] (their images are compact) with this theorem (compact subsets of Hausdorff $Y$ are closed).

> [!tip] **Homeomorphism Criterion** *(from Topology II)*
> A continuous bijection from a compact space to a Hausdorff space is a homeomorphism (see [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]]). The proof uses the closed-map property, which uses this theorem.

> [!tip] **Properness in Algebraic Geometry** *(from Algebraic Geometry)*
> A morphism of schemes is **proper** if it is separated, of finite type, and universally closed. The closed-image condition is the algebraic-geometric analog of "compact image in Hausdorff target". Proper morphisms have closed images by definition; this theorem is the topological prototype.
