---
type: theorem
subject: topology
prereqs:
  - "Def - Compact Space"
  - "Def - Topological Space"
  - "Def - Closure, Interior, and Boundary"
tags: [analysis, topology, compactness]
---

# Notation

$X$ is a [[Def - Topological Space|topological space]], $F \subseteq X$ a closed subset. $X$ is **compact** if every open cover has a finite subcover (see [[Def - Compact Space]]). The subspace $F$ is equipped with the [[Def - Subspace Topology|subspace topology]] from $X$. The full registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Theorem.** Let $X$ be a compact topological space and $F \subseteq X$ a **closed** subset. Then $F$ (with the subspace topology) is compact.

The proof is short: any open cover of $F$ in the subspace topology lifts to an open cover of $X$ by adding the open complement $X \setminus F$; compactness of $X$ extracts a finite subcover; restricting back to $F$ removes the complement and leaves a finite subcover of $F$.

---

# Motivation

Compactness is inherited by closed subsets, full stop. No separation axiom needed, no Hausdorff, no Lindelöf — just closed-in-compact gives compact. Combined with [[Thm - Continuous Image of a Compact Space|continuous-image-of-compact is compact]], this gives the two most-used compactness inheritance results.

The question this theorem answers is: *how does compactness propagate down to subsets*? The answer: only to closed subsets, but for those, always. The reason it works is that "closed" is exactly the property that lets one *patch the missing piece* — adding the open complement to any open cover of the subset gives an open cover of the whole space, which compactness handles, and the patch can be removed at the end since it was added as a single open set.

The pragmatic content is enormous. Many compact sets in practice arise as closed subsets of known-compact spaces: closed subsets of $[a, b]$, closed subsets of $[0, 1]^n$, closed subsets of the Hilbert cube $[0, 1]^{\mathbb{N}}$ (compact by Tychonoff), closed subsets of any compact group. Every "I know my space is compact" argument in functional analysis routes through this theorem at some point: closed subspaces of compact operators, closed unit balls in weak topologies (compact by Banach–Alaoglu) — all use this.

The theorem also makes compactness *transitive in a useful sense*: if $A \subseteq B$ with $B$ compact and $A$ closed in $B$ (not in the ambient space), then $A$ is compact. This is the inheritance through nested compact subsets, used constantly in extracting subdomains for analysis.

A common error is to drop "closed" and conclude "subsets of compact are compact". This is false: $(0, 1) \subseteq [0, 1]$, the source is compact, but the subset is not (the open cover $\{(1/n, 1) : n \in \mathbb{N}\}$ has no finite subcover). The closedness is the precise condition that distinguishes inherit-able subsets from non-inherit-able ones.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$F \subseteq X$ closed, $X$ compact".

The first disguised source is **$F$ is the zero set of a continuous function on a compact space**. Property $B$: $f : X \to \mathbb{R}$ continuous, $F = f^{-1}(0)$, $X$ compact. The bridge: $\{0\}$ is closed in $\mathbb{R}$, preimage of closed under continuous is closed, hence $F$ is closed. *Example:* the unit sphere $S^{n-1} = \{x \in \mathbb{R}^n : \lVert x \rVert = 1\}$ is the zero set of $\lVert \cdot \rVert^2 - 1$, hence closed; combined with being a subset of the compact ball, it is compact.

The second disguised source is **$F$ is an intersection of closed sets** (which include the compact $X$). Property $B$: $F = \bigcap_\alpha F_\alpha$ with each $F_\alpha$ closed in $X$. The bridge: arbitrary intersection of closed is closed. *Example:* the **Cantor set** is the intersection of nested closed sets in $[0, 1]$, hence closed in $[0, 1]$ (compact), hence compact.

The third disguised source is **$F$ is the support of a continuous function on a compact space** — the closure of $\{x : f(x) \neq 0\}$. Property $B$: $f : X \to \mathbb{R}$ continuous, $X$ compact. The bridge: closures are closed by definition. *Example:* compactly supported continuous functions on $\mathbb{R}^n$ — even though $\mathbb{R}^n$ is not compact, the support of such a function, being a closed bounded subset of $\mathbb{R}^n$, is compact by [[Thm - Heine–Borel Theorem|Heine–Borel]] (and the boundedness, via $X$ being inside a larger compact region).

**Targets (Output Amplification)**

The conclusion is "$F$ is compact".

Combine the conclusion with **a continuous map $f : X \to Y$**. Property $D$: $f$ continuous. Amplified result $E$: $f(F)$ is compact in $Y$ (by [[Thm - Continuous Image of a Compact Space]]). *Example:* the image of any closed subset of $[0, 1]$ under a continuous map is compact. The chain "closed-in-compact → compact → continuous-image-of-compact = compact" is the most-used compactness extraction in analysis.

Combine the conclusion with **Hausdorffness of an ambient space**. Property $D$: $X$ is Hausdorff (or $F$ is in some Hausdorff space). Amplified result $E$: $F$ is closed in the ambient space too (by [[Thm - Compact Subset of Hausdorff is Closed]]). The double conclusion "$F$ is compact *and* closed in any Hausdorff superspace" is the gold standard for compact subsets.

Combine the conclusion with **the FIP characterization of compactness**. Property $D$: a family of closed sets in $F$ with the finite intersection property. Amplified result $E$: the family has a nonempty total intersection (by FIP characterization of compactness in $F$). *Example:* the Nested Intervals Theorem and its generalizations come from this — a nested decreasing sequence of closed nonempty subsets of a compact space has a nonempty intersection.

Combine the conclusion with **continuity of an extremum**. Property $D$: a continuous real-valued function $f$ on $F$. Amplified result $E$: $f$ attains its maximum and minimum on $F$ (Extreme Value Theorem). The bridge: $F$ compact, $f$ continuous, so $f(F) \subseteq \mathbb{R}$ is compact, hence closed and bounded, hence has a maximum. *Example:* the closest point to a fixed point in a closed bounded subset of a Hilbert space (which is compact in finite dimensions but not in infinite — this is exactly where the theorem's hypotheses must be checked carefully).

---

# Why Is It True

The intuition: compactness is "finite-subcover" — closed-ness of $F$ means $F$'s complement is open, and that single open complement *plus any open cover of $F$* gives an open cover of all of $X$.

The mechanism:

1. Let $\{U_i\}_{i \in I}$ be an open cover of $F$ in the subspace topology — each $U_i = V_i \cap F$ for some open $V_i \subseteq X$. (Equivalently, the $V_i$ are opens in $X$ covering $F$.)

2. Add the open complement: $\{V_i\}_{i \in I} \cup \{X \setminus F\}$ is an open cover of *all of $X$*: any $x \in X$ is either in $F$ (then $x \in V_i$ for some $i$) or in $X \setminus F$.

3. By compactness of $X$, extract a finite subcover: $X = V_{i_1} \cup \cdots \cup V_{i_n} \cup (X \setminus F)$ for some indices. (The complement $X \setminus F$ may or may not be needed; either way, finitely many $V_{i_k}$ together with possibly $X \setminus F$ cover $X$.)

4. Restrict back to $F$: $F = F \cap X = F \cap (V_{i_1} \cup \cdots \cup V_{i_n} \cup (X \setminus F)) = (F \cap V_{i_1}) \cup \cdots \cup (F \cap V_{i_n}) \cup (F \cap (X \setminus F)) = U_{i_1} \cup \cdots \cup U_{i_n}$ (the last term vanishes). So the finitely many $U_{i_k}$ cover $F$.

The geometric picture: $X$ is compact, so any open cover finitizes. $F$ is closed, so its complement is a single open set that we can append to any open cover of $F$ to fill out a cover of $X$. After finitizing, the appended complement comes off again because it does not intersect $F$.

The reason "closed" is needed: without it, the complement of $F$ is not open, and the "patching" step fails. We cannot extend an open cover of $F$ to an open cover of $X$ by adding finitely many extra opens — the missing pieces of $X$ might require an *arbitrarily large* collection of new opens.

The reason this works for *any* compact $X$ (no Hausdorff needed, no separation needed) is that the argument uses only the *open-cover formulation* of compactness, which is the most primitive form. No separation, no metric, no countability — just the open-cover definition of compactness and the closed = complement-of-open characterization.

---

# What Makes This Hard

The non-obvious step is the **patching trick**: extending an open cover of $F$ to an open cover of $X$ by adding the single open set $X \setminus F$. The most common error is to omit this step and try to extract a finite subcover of $F$ directly from compactness of $X$ — which fails because compactness is about $X$'s open covers, not $F$'s. A second pitfall is forgetting that closedness of $F$ in $X$ is essential — without it, $X \setminus F$ is not open, and the extension does not give an open cover.

---

# Rederivation Scaffold

**High-level strategy:**
Add the open complement $X \setminus F$ to any open cover of $F$ to get an open cover of $X$; extract a finite subcover by compactness; restrict to $F$, the complement falls out, finitely many opens remain covering $F$.

**Subgoal decomposition:**

1. **Open cover of $F$.** Take $\{U_i\}$ open cover of $F$ in subspace topology, or equivalently $\{V_i\}$ opens in $X$ covering $F$.
   - *Hint:* Compactness is a finite-subcover property; start with arbitrary.

2. **Extend to open cover of $X$.** Add $X \setminus F$ (open since $F$ closed) to get an open cover of $X$.
   - *Hint:* Every $x \in X$ is in $F$ or not.
   - *Why needed:* It is the key step.

3. **Extract finite subcover of $X$.** By compactness of $X$.

4. **Restrict back to $F$.** $X \setminus F$ does not contribute (disjoint from $F$); the remaining finitely many opens cover $F$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Adding an open complement extends a cover of $F$ to a cover of $X$
> **Statement:** Let $F \subseteq X$ be closed and $\{V_i\}_{i \in I}$ a collection of opens in $X$ covering $F$. Then $\{V_i\}_{i \in I} \cup \{X \setminus F\}$ is an open cover of $X$.
>
> **Hint:** Every $x \in X$ is in $F$ (covered by the $V_i$) or in $X \setminus F$ (covered by itself).
>
> **Why needed:** It is the patching construction.
>
> > [!note]- Full proof
> > $X \setminus F$ is open since $F$ is closed. For any $x \in X$: if $x \in F$, then $x \in V_i$ for some $i$ (by hypothesis); if $x \notin F$, then $x \in X \setminus F$. Either way, $x$ is in the extended cover.

> [!note]- Lemma 2: A finite subcover of $X$ restricts to a finite cover of $F$ after dropping $X \setminus F$
> **Statement:** If $\{V_{i_1}, \ldots, V_{i_n}\} \cup \{X \setminus F\}$ covers $X$, then $\{V_{i_1}, \ldots, V_{i_n}\}$ covers $F$.
>
> **Hint:** $F \cap (X \setminus F) = \emptyset$, so the complement contributes nothing to $F$.
>
> **Why needed:** It removes the patch after finitization.
>
> > [!note]- Full proof
> > For any $x \in F$, $x \in X$, so $x \in V_{i_k}$ for some $k$ or $x \in X \setminus F$. The second is impossible since $x \in F$. So $x \in V_{i_k}$ for some $k$, and $\{V_{i_k}\}$ covers $F$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> Let $X$ be compact and $F \subseteq X$ closed. We show $F$ is compact in the subspace topology.
>
> Let $\{U_i\}_{i \in I}$ be an open cover of $F$ in the subspace topology. By the definition of subspace topology, $U_i = V_i \cap F$ for some open $V_i \subseteq X$. Since $\{U_i\}$ covers $F$, $\{V_i\}$ covers $F$ in $X$.
>
> By Lemma 1, $\{V_i\}_{i \in I} \cup \{X \setminus F\}$ is an open cover of $X$. By compactness of $X$, there is a finite subcover: $X = V_{i_1} \cup \cdots \cup V_{i_n} \cup (X \setminus F)$ for some indices $i_1, \ldots, i_n \in I$ (with possibly the complement included, but not necessary if the $V_{i_k}$ alone already cover $X$; in either case we extract at most $n$ of the $V_{i_k}$).
>
> By Lemma 2, $\{V_{i_1}, \ldots, V_{i_n}\}$ covers $F$. Restricting to subspace topology, $\{U_{i_1}, \ldots, U_{i_n}\}$ covers $F$.
>
> So every open cover of $F$ has a finite subcover, i.e., $F$ is compact. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Closed bounded subsets of $\mathbb{R}^n$.** Every closed bounded subset of $\mathbb{R}^n$ is compact. The argument: a closed bounded subset is contained in some cube $[-N, N]^n$ (compact by [[Thm - Heine–Borel Theorem|Heine–Borel]]), and being closed in the ambient $\mathbb{R}^n$ makes it closed in the cube (since the cube has the subspace topology, and $F \cap [-N, N]^n$ is just $F$ when $F \subseteq [-N, N]^n$). By this theorem, $F$ is compact. This is the standard proof of one direction of Heine–Borel.

**Nested intervals theorem.** A decreasing nested sequence $F_1 \supseteq F_2 \supseteq F_3 \supseteq \cdots$ of nonempty closed subsets of a compact space $X$ has nonempty total intersection $\bigcap_n F_n$. Proof: each $F_n$ is closed in compact $X$, hence compact (this theorem). The collection $\{F_n\}$ has the finite intersection property (any finite subfamily contains its smallest member, which is nonempty). By the FIP form of compactness ([[Def - Compact Space]]'s alternative characterization), $\bigcap_n F_n \neq \emptyset$. Applied to $[0, 1]$ and a sequence of nested closed intervals, this is the classical Nested Intervals Theorem.

**Cantor's diagonal compactness argument.** Let $K = \{0, 1\}^{\mathbb{N}}$ be the Cantor set (the product of countably many copies of $\{0, 1\}$, compact by Tychonoff). Any closed subset of $K$ is compact by this theorem. The middle-thirds Cantor set in $[0, 1]$ is the image of $K$ under a continuous embedding, hence closed in $[0, 1]$ (closed image of a compact space in Hausdorff), hence compact by this theorem applied in $[0, 1]$. Both routes prove the same fact: the Cantor set is compact.

**Closed unit ball in an infinite-dimensional Banach space — counterexample for the converse.** In an infinite-dimensional Banach space, the closed unit ball is closed and bounded but *not* compact (by F. Riesz's lemma; the closure of the unit ball is closed and the ball is bounded, but compactness fails — there is a sequence of points at mutual distance $\geq 1$). The application illustrates that this theorem only gives compactness when the ambient space *itself* is compact — being closed in a non-compact space gives nothing. The contrast with the finite-dimensional Heine–Borel theorem is what makes infinite-dimensional functional analysis genuinely different.

---

# Bridges

- **[[Thm - Continuous Image of a Compact Space]]** — the complementary inheritance result. Together they give the two most-used compactness inheritance theorems: closed-in-compact and continuous-image-of-compact. Almost every compact-set argument routes through one or both.

- **[[Thm - Compact Subset of Hausdorff is Closed]]** — the partial converse. In a Hausdorff space, compact subsets are closed. Together with this theorem: in a compact Hausdorff space, "compact" and "closed" coincide. This is the gold-standard duality.

- **[[Thm - Heine–Borel Theorem]]** — concretizes the closed-in-compact direction in $\mathbb{R}^n$. The proof of Heine–Borel uses this theorem applied to closed subsets of $[-N, N]^n$.

- **The FIP characterization of compactness** — a closed subset of a compact space inherits the FIP characterization: any family of relatively closed subsets with the finite intersection property has nonempty total intersection.

- **The Nested Intervals Theorem and its generalizations** — direct consequences via FIP.

---

# Unlocked by This

> [!tip] **The Cantor Set** *(from Real Analysis)*
> The middle-thirds Cantor set is a closed subset of $[0, 1]$, hence compact by this theorem. Its topological properties — uncountable, perfect, totally disconnected, homeomorphic to $\{0, 1\}^{\mathbb{N}}$ — make it the canonical example in dimension theory and dynamics.

> [!tip] **Compactness Arguments in PDE** *(from Functional Analysis)*
> In Sobolev space theory, **Rellich–Kondrachov compactness** lets one extract convergent subsequences from bounded sequences in $H^1$ via compactness of the embedding into $L^2$ on bounded domains. The compactness of the embedded image comes from being a closed subset of a compact set (the closure in $L^2$).

> [!tip] **Tychonoff's Theorem and Stone–Čech Compactification** *(from Topology III)*
> Closed subsets of Tychonoff products of compact spaces are themselves compact, by this theorem. This is the engine of Stone–Čech compactification, which represents $\beta X$ as a closed subset of a Tychonoff cube.

> [!tip] **Compact Operators and Spectral Theory** *(from Functional Analysis)*
> A **compact operator** $T : V \to V$ on a Banach space is one such that the image of the unit ball has compact closure. The spectrum of a compact operator on an infinite-dimensional space is a sequence converging to $0$, plus possibly $0$ — a closed bounded subset of $\mathbb{C}$, which is compact (by Heine–Borel and this theorem). The spectral theory of compact operators rests on this compactness.
