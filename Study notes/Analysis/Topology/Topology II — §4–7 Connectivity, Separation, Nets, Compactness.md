---
type: topic
subject: topology
chapter: "4-7"
title: "Topology II — §4–7 Connectivity, Separation, Nets, Compactness"
tags: [analysis, topology]
---

# Notation Registry

- $X, Y, Z$ — topological spaces
- $A, B, C, F, K$ — subsets; $F, G$ usually closed, $U, V, W$ usually open, $K$ usually compact
- $\overline{A}$ — closure of $A$
- $X = U \sqcup V$ — disjoint union (separation) of $X$
- $\pi_0(X)$ — the set of connected components of $X$
- $D$ — a directed set; $\alpha, \beta, \gamma, \tau \in D$ — directed-set elements
- $\Phi : D \to X$, $\{x_\alpha\}$ — a net in $X$; the notation $x_\alpha \to x$ means $\Phi$ converges to $x$
- $\{x_n\}$, $n \in \mathbb{N}$ — a sequence in $X$ (the special case of a net indexed by $\mathbb{N}$)
- $\mathcal{F}$ — a collection of subsets, often with the finite intersection property (FIP)
- $T_0, T_1, T_2, T_3, T_4$ — the separation axioms in increasing strength
- $S^1, S^2, S^n$ — the unit circle, unit 2-sphere, unit $n$-sphere
- $[0, 1] = I$ — the unit interval
- $\mathbb{R}, \mathbb{Q}, \mathbb{R}^n$ — reals, rationals, Euclidean $n$-space
- "Map" always means continuous function
- $f|_A$ — restriction of $f$ to $A$
- $A \subseteq^c B$ — $A$ is contained in $B$ with $B \setminus A$ finite (used for cofinite topology)

---

# Motivation

Once a topological space is in hand, the most powerful global properties one wants to talk about are *connectedness* — the space is in one piece — and *compactness* — the space is "topologically small". Both ideas were already implicit in $\mathbb{R}^n$ analysis: the intermediate value theorem is connectedness in action, the extreme value theorem is compactness in action, and the Heine–Borel theorem (closed and bounded subsets of $\mathbb{R}^n$ are compact) is the bridge between them. The work of this topic is to axiomatize these notions at the level of open sets alone, so they apply to spaces with no metric in sight — quotient spaces, function spaces, weak topologies, profinite spaces.

The chapter starts in §4 with **connectedness**. The intuitive picture is "no jumps": one cannot split the space into two open pieces. Formally, $X$ is connected if it is not a disjoint union of two nonempty opens. Three reformulations all say the same thing — that the only clopen subsets are $\emptyset$ and $X$, that every map to a discrete space is constant, that no nonconstant locally-constant function exists. The reformulations are the working tool, because they convert connectedness from a *negative* statement (no decomposition) into a *positive* one (every map of a certain kind is trivial). Continuous images of connected spaces are connected, products of connected spaces are connected, unions of connected pieces that overlap pairwise are connected — these are the moves you actually deploy, and they distill the intuition that "you can't break connectedness by squeezing or gluing".

In §5 we hit the **separation axioms**, the surprising fact that the bare topological space axioms are *too weak* to capture features one would have thought obvious. In a general topological space, distinct points need not be distinguishable by open sets — there can be a point in every open set containing another point. To rule out the pathologies, one stacks separation properties: $T_0$ (some open separates), $T_1$ (singletons are closed), $T_2$ or **Hausdorff** (disjoint opens for any two points), $T_3$ or **regular** (a point and a closed set can be separated), $T_4$ or **normal** (two disjoint closed sets can be separated). Each axiom is the *price paid* for a specific theorem to become true: Hausdorff buys the uniqueness of limits, regular buys the closed-neighborhood characterization, normal buys Urysohn's lemma and the Tietze extension theorem (those wait until [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]]). The story to keep in mind: separation axioms are not extra structure imposed on a topology; they are *minimum hypotheses* needed for the theorems one wants to be true.

§6 then introduces **nets** — Moore–Smith convergence — to fix a defect of sequences. In a metric space, $x \in \overline{A}$ if and only if a sequence in $A$ converges to $x$, and $f$ is continuous if and only if it preserves sequential limits. In a general topological space, sequences are too short and rigid to detect everything the topology sees: there exist points in closures that no sequence can reach, and discontinuous functions that nonetheless preserve all sequential limits. The cure is to replace $\mathbb{N}$ as an indexing set with an arbitrary *directed set* — a partially ordered set where any two elements have a common upper bound — and to define a net as a function from such a set into $X$. Nets restore the metric intuition in full generality: closure = set of net limits, continuity = preservation of net convergence. The deepest move is the existence of **universal subnets**: every net has a subnet that, for each subset $A \subseteq X$, is eventually in $A$ or eventually in $X \setminus A$. This is what makes the proof that every compactness equivalent is true (next section) clean, and it is equivalent to the Axiom of Choice.

The chapter culminates in §7 with **compactness**. The definition is operative: every open cover has a finite subcover. The intuition is that compactness is "topological finiteness" — finitely many open sets suffice to capture everything. Continuous images of compact spaces are compact, closed subsets of compact spaces are compact, compact subsets of Hausdorff spaces are closed, and continuous maps from compact spaces to Hausdorff spaces are *closed maps* (and therefore continuous bijections are homeomorphisms — the missing converse from §2). The biggest theorem of the section is the *equivalence of three compactness notions* in the most general setting: open-cover compactness, the finite intersection property for closed sets, and the existence of convergent subnets of every net (in metric spaces, equivalent to sequential compactness). Heine–Borel — closed and bounded in $\mathbb{R}^n$ is compact — is the bedrock special case, but the theorem one *uses* is the more general one.

A unifying theme: connectedness and compactness are both *invariants of continuity*. A continuous image of a connected space is connected; a continuous image of a compact space is compact. Anything you can prove from connectedness or compactness of a target you can pull back to the source via any continuous map. This is the engine that proves the intermediate value theorem (connectedness of $[0,1]$ + continuity of $f$ → connectedness of $f([0,1])$ → $f$ hits every intermediate value), the extreme value theorem (compactness of $X$ + continuity of $f$ → compactness of $f(X)$ in $\mathbb{R}$ → $f$ attains its sup and inf), and a dozen other "automatic" propagation facts.

---

# Concept Map

## §4 Connectivity and Components

- **[[Def - Connected Space]]**
	- $X$ is **connected** if it is not the disjoint union of two nonempty open subsets, equivalently if the only clopen subsets are $\emptyset$ and $X$, equivalently if every continuous map from $X$ to a discrete two-point space $\{0, 1\}$ is constant. Continuity preserves connectedness, and connectedness is a topological invariant: $\mathbb{R}$ is connected but $\mathbb{R} \setminus \{0\}$ is not, which is the cleanest proof that they are not homeomorphic. Subspaces inherit connectedness only with care — $\mathbb{Q}$ in $\mathbb{R}$ has every singleton as a connected component.

- **[[Def - Path-Connected Space]]**
	- $X$ is **path-connected** if for any two points $p, q \in X$ there is a continuous map $\gamma : [0, 1] \to X$ with $\gamma(0) = p, \gamma(1) = q$. Path-connectedness implies connectedness (the image of $[0,1]$ is connected, and unions of overlapping connected sets are connected). The converse fails — the **topologist's sine curve** $\{0\} \times [-1, 1] \cup \{(x, \sin(1/x)) : x > 0\}$ is connected but not path-connected. Path-connectedness is more useful when constructing maps into the space, connectedness when constructing maps out of it.

- **[[Thm - Continuous Image of a Connected Space]]**
	- If $f : X \to Y$ is continuous and $X$ is connected, then $f(X)$ is connected. The proof is one line: a clopen subset of $f(X)$ pulls back to a clopen subset of $X$, which must be $\emptyset$ or $X$, so the original was $\emptyset$ or $f(X)$. This is the source of every "continuous bijection preserves connectedness" argument, and of the **intermediate value theorem** when $Y = \mathbb{R}$: a continuous function on a connected space takes all intermediate values.

- **[[Thm - Union of Overlapping Connected Sets is Connected]]**
	- If $\{Y_\alpha\}$ is a family of connected subsets of $X$ and no two are disjoint, then $\bigcup_\alpha Y_\alpha$ is connected. More flexibly: if every pair has nonempty intersection, or if there is a fixed point in every $Y_\alpha$, the union is connected. This is the engine of the equivalence relation "$p \sim q$ if both lie in a connected set", whose equivalence classes are the components.

- **[[Def - Connected Components]]**
	- A **connected component** of $X$ is a maximal connected subset; equivalently, the equivalence class of $x$ under "$p \sim q$ if both lie in a connected subset". Components are connected, closed, partition the space, and contain every connected subset they meet. They are *not* always open — the rationals $\mathbb{Q}$ have singletons as components, none of which is open. A space whose components are open is called **locally connected**.

- **[[Ex - The interval [0,1] is connected]]** (⭐⭐)
	- Show that $[0, 1]$ is connected directly from the definition by assuming $[0,1] = U \sqcup V$ with $U, V$ open and nonempty and considering $\sup(U \cap [0, x])$ to derive a contradiction.

- **[[Ex - The topologist's sine curve]]** (⭐⭐⭐)
	- For $X = \{(x, \sin(1/x)) : x > 0\} \cup \{0\} \times [-1, 1]$ in $\mathbb{R}^2$, show $X$ is connected (it is the closure of a connected set) but not path-connected (any path entering the segment $\{0\} \times [-1,1]$ from $\{x > 0\}$ must traverse a non-locally-controllable oscillation, formalized via uniform continuity).

- **[[Ex - Components versus path-components]]** (⭐⭐)
	- Give an example of a space whose connected components and path-components differ (the topologist's sine curve), and a sufficient condition for them to coincide (local path-connectedness).

> [!tip] Unlocked: Fundamental Group *(from Algebraic Topology)*
> Once path-connectedness is in hand, one can talk about *equivalence classes of loops* at a basepoint — paths $\gamma : [0,1] \to X$ with $\gamma(0) = \gamma(1) = x_0$, modulo homotopy. These form a group, the **fundamental group** $\pi_1(X, x_0)$, the first algebraic invariant of $X$. The fact that $\pi_1(S^1) = \mathbb{Z}$ — counting how many times a loop winds — is the entry point to algebraic topology and the genuine reason $\mathbb{R}^2 \setminus \{0\}$ and $\mathbb{R}^2$ are not homeomorphic.

> [!note] Exercise Index — §4
> [[Exercise Index - §4 Connectivity]]

## §5 Separation Axioms

- **[[Def - Separation Axioms]]**
	- A space is **$T_0$** if any two points are distinguished by some open set; **$T_1$** if for any two points each has an open set excluding the other (equivalently, every singleton is closed); **$T_2$ or Hausdorff** if any two distinct points have disjoint open neighborhoods; **$T_3$ or regular** if $T_1$ and any point and disjoint closed set have disjoint open neighborhoods; **$T_4$ or normal** if $T_1$ and any two disjoint closed sets have disjoint open neighborhoods. Each axiom strictly strengthens its predecessor on the indexed scale, and each is the minimum hypothesis under which a specific theorem becomes true. The standard convention "regular ⇒ Hausdorff", "normal ⇒ Hausdorff" enforced via the $T_1$ clause is occasionally relaxed — different books disagree.

- **[[Thm - Hausdorff Iff Unique Net Limits]]**
	- $X$ is Hausdorff if and only if every convergent net in $X$ has a unique limit. The forward direction is immediate from the existence of disjoint neighborhoods. The reverse direction is the non-obvious one and requires the construction of a "splitting net" indexed by pairs $(U, V)$ of open sets around the two would-be limits, ordered by reverse inclusion in each coordinate. The corollary "sequence limits are unique in Hausdorff" suffices in first-countable spaces, but the *net* statement is the one that fully characterizes Hausdorff.

- **[[Thm - Regular Iff Closed Neighborhoods Form a Basis]]**
	- A Hausdorff space $X$ is regular if and only if at every point $x \in X$, the closed neighborhoods of $x$ form a neighborhood basis. The proof unwraps the regular axiom: a point $x \notin C$ (closed) gives disjoint opens $U \ni x, V \supseteq C$, and then $X \setminus V$ is a closed neighborhood of $x$ disjoint from $C$. Subspaces and products of regular spaces are regular; this is the cleanest separation axiom for taking subspaces.

- **[[Thm - Metric Spaces are Normal]]**
	- Every metric space is normal. The standard proof: for disjoint closed sets $F, G$, the function $\varphi(x) = d(x, F)/(d(x, F) + d(x, G))$ is continuous, takes value $0$ on $F$ and $1$ on $G$, and $\varphi^{-1}([0, 1/2))$ and $\varphi^{-1}((1/2, 1])$ are disjoint open sets containing $F$ and $G$. This proof is the model for Urysohn's lemma in general normal spaces.

- **[[Ex - A T1 space that is not Hausdorff]]** (⭐⭐)
	- Take $\mathbb{R}$ with the cofinite topology: every finite set is closed (so singletons are closed and $T_1$ holds), but any two nonempty opens have cofinite complements and hence intersect (so Hausdorff fails). Show explicitly that the sequence $x_n = n$ converges to *every* real, which is the failure mode of non-Hausdorff.

- **[[Ex - A Hausdorff space that is not regular]]** (⭐⭐⭐)
	- The plane $\mathbb{R}^2$ with the topology generated by usual opens *plus* sets $\{(x,y) : x^2 + y^2 < a, y \neq 0\} \cup \{(0,0)\}$. Show this is Hausdorff (the usual topology already separates points). Then exhibit the closed set $\{(0, y) : y \neq 0\}$ which cannot be separated from the origin by disjoint opens.

- **[[Ex - Subspace of Hausdorff is Hausdorff]]** (⭐)
	- Show that a subspace $A \subseteq X$ of a Hausdorff space is Hausdorff. The disjoint opens come for free from intersecting the ambient ones with $A$.

> [!note] Exercise Index — §5
> [[Exercise Index - §5 Separation Axioms]]

## §6 Nets and Moore–Smith Convergence

- **[[Def - Directed Set and Net]]**
	- A **directed set** is a partially ordered set $D$ such that for any two elements $\alpha, \beta \in D$ there exists $\gamma \in D$ with $\gamma \geq \alpha$ and $\gamma \geq \beta$. A **net** in $X$ is a function $\Phi : D \to X$ from a directed set $D$ to $X$. A sequence is the special case $D = \mathbb{N}$. The point: in general topology, the indexing $\mathbb{N}$ is too rigid; allowing arbitrary directed indexing recovers the metric intuition for closure, continuity, and compactness.

- **[[Def - Net Convergence]]**
	- A net $\{x_\alpha\}_{\alpha \in D}$ **converges to** $x$ if for every neighborhood $U$ of $x$ there exists $\alpha_0 \in D$ such that $x_\alpha \in U$ for all $\alpha \geq \alpha_0$ (the net is **eventually** in $U$). It is **frequently in $U$** if for every $\alpha$ there is $\beta \geq \alpha$ with $x_\beta \in U$. Convergence generalizes sequential convergence and detects all topological phenomena that sequences cannot.

- **[[Def - Subnet and Universal Net]]**
	- A **subnet** of $\Phi : D \to X$ is the composition $\Phi \circ h$ where $h : D' \to D$ is a **final function**: for every $\delta \in D$ there is $\delta' \in D'$ such that $\alpha' \geq \delta'$ in $D'$ implies $h(\alpha') \geq \delta$ in $D$. A net is **universal** if for every $A \subseteq X$ it is eventually in $A$ or eventually in $X \setminus A$. The definition of subnet is more general than "extract a subsequence by composing with an increasing function" and is exactly what makes the convergent-subnet characterization of compactness work.

- **[[Thm - Closure via Nets]]**
	- For $A \subseteq X$, $x \in \overline{A}$ if and only if there is a net in $A$ converging to $x$. The proof exhibits the canonical net: indexed by neighborhoods of $x$ ordered by reverse inclusion, with $\Phi(U) \in U \cap A$ (which exists because $x \in \overline{A}$). This is the net-level analog of the metric-space sequential closure characterization — and unlike that one, it holds in *every* topological space.

- **[[Thm - Continuity via Nets]]**
	- $f : X \to Y$ is continuous if and only if for every net $\{x_\alpha\}$ in $X$ converging to $x$, the image net $\{f(x_\alpha)\}$ converges to $f(x)$. This replaces the metric-space "continuous = sequentially continuous" with a statement that works in full generality. The proof is the natural one: $f^{-1}(V)$ contains a net eventually, giving openness.

- **[[Thm - Every Net Has a Universal Subnet]]**
	- Every net in any topological space has a universal subnet. The proof uses Zorn's lemma (axiom of choice) to extract a maximal collection of sets in which the net is frequently, and shows that this collection determines a universal subnet. The corollary that makes this useful: every net in a compact space has a convergent subnet (compactness equivalence).

- **[[Ex - A sequence is universal iff eventually constant]]** (⭐⭐)
	- Show that a sequence $\{x_n\}$ in any space is a universal net if and only if it is eventually constant. This is why "universal subsequence" is empty content — one *needs* the freedom of general directed sets for the universal-net machinery to be useful.

- **[[Ex - A net that converges to two points]]** (⭐⭐)
	- In a non-Hausdorff space (the cofinite topology on $\mathbb{N}$ works), construct an explicit net converging to two different points. Use the directed set of finite sets, ordered by inclusion, picking elements outside.

- **[[Ex - A closure point not reached by any sequence]]** (⭐⭐⭐)
	- In the space $\omega_1 + 1$ of ordinals up to and including the first uncountable, show that $\omega_1$ is in the closure of $[0, \omega_1)$ but no sequence in $[0, \omega_1)$ converges to $\omega_1$. (Any sequence in $[0, \omega_1)$ has a countable supremum, strictly less than $\omega_1$.)

> [!note] Exercise Index — §6
> [[Exercise Index - §6 Nets]]

## §7 Compactness

- **[[Def - Compact Space]]**
	- $X$ is **compact** if every open cover has a finite subcover. Equivalently (taking complements), every collection of closed sets with the **finite intersection property** (every finite subfamily has nonempty intersection) has nonempty total intersection. Equivalently, every net in $X$ has a convergent subnet. The three formulations are equally fundamental and one chooses among them depending on the problem.

- **[[Def - Sequentially Compact Space]]**
	- $X$ is **sequentially compact** if every sequence has a convergent subsequence. In general topological spaces, sequential compactness is neither stronger nor weaker than compactness. In metric spaces (more generally in second-countable spaces) the two coincide, which is the Bolzano–Weierstrass theorem in disguise.

- **[[Thm - Continuous Image of a Compact Space]]**
	- If $X$ is compact and $f : X \to Y$ is continuous, $f(X)$ is compact. Pull back any open cover of $f(X)$ via $f$, extract a finite subcover of $X$, push forward. This is the engine of the **extreme value theorem**: a continuous real-valued function on a compact space attains its maximum and minimum (the image is a compact subset of $\mathbb{R}$, hence closed and bounded, hence has a maximum).

- **[[Thm - Compact Subset of Hausdorff is Closed]]**
	- A compact subset of a Hausdorff space is closed. Take $x$ outside the compact $A$, separate each point of $A$ from $x$ by disjoint opens, extract a finite subcover of $A$, intersect the corresponding opens around $x$ to get a neighborhood of $x$ disjoint from $A$. Without Hausdorff, this fails — in the cofinite topology on $\mathbb{N}$, every subset is compact but not every subset is closed.

- **[[Thm - Closed Subset of Compact is Compact]]**
	- A closed subset of a compact space is compact. Add the complementary open set to any open cover of the subset and extract a finite subcover. This is the most-used compactness inheritance result and is true in every topological space, no separation axiom needed.

- **[[Thm - Heine–Borel Theorem]]**
	- A subset of $\mathbb{R}^n$ is compact if and only if it is closed and bounded. Proof routes through compactness of $[0, 1]$ (and hence of $[a, b]$ by scaling) plus Tychonoff for finite products (so $[a_1, b_1] \times \cdots \times [a_n, b_n]$ is compact), plus the fact that a closed subset of a compact space is compact (so any closed and bounded subset is compact), plus the fact that a compact subset of $\mathbb{R}^n$ is bounded (covered by finite collection of unit balls) and closed (compact in Hausdorff). This is the special case from which one trains every intuition.

- **[[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]]**
	- A continuous bijection $f : X \to Y$ from a compact space to a Hausdorff space is a homeomorphism. The proof: $f$ is a closed map (closed sets in $X$ are compact, hence their images are compact in $Y$, hence closed since $Y$ is Hausdorff), so $f^{-1}$ is continuous. This fills the gap from [[Topology I — §1–3 Metric and Topological Spaces|Topology I]] where we noted continuous bijections need not be homeomorphisms — this is exactly the hypothesis that closes the gap.

- **[[Thm - The Tube Lemma]]**
	- If $Y$ is compact and $N$ is an open subset of $X \times Y$ containing the slice $\{x_0\} \times Y$, then there is an open neighborhood $U$ of $x_0$ in $X$ with $U \times Y \subseteq N$. The "tube" $U \times Y$ over $U$ fits inside $N$. The proof: cover $\{x_0\} \times Y$ by box-basis elements inside $N$, use compactness of $Y$ to extract a finite subcover, intersect their $X$-projections. This is the engine of "product of compacts is compact" for finite products.

- **[[Ex - The unit interval is compact]]** (⭐⭐)
	- Show that $[0, 1]$ is compact directly from the definition by considering $\sup\{t \in [0,1] : [0, t] \text{ has a finite subcover}\}$ and arguing the sup is $1$ and is attained.

- **[[Ex - Compact + Hausdorff implies normal]]** (⭐⭐⭐)
	- Use the tube-lemma-style argument: for disjoint closed sets $F, G$ in compact Hausdorff $X$, separate each pair $(x, y) \in F \times G$ by disjoint opens, then use compactness of $F$ and $G$ (closed in compact) to extract finite covers and assemble disjoint opens around the original sets.

- **[[Ex - A non-Hausdorff space where compact subsets are not closed]]** (⭐⭐)
	- Take $\mathbb{R}$ with the cofinite topology. Show that every subset is compact (every open cover has a finite subcover after removing finitely many points) but most subsets are not closed (only finite sets and $\mathbb{R}$ itself are closed).

> [!tip] Unlocked: Banach–Alaoglu *(from Functional Analysis)*
> The closed unit ball of the dual of a normed space is compact in the **weak-$*$** topology. This is one of the keystone compactness results in analysis. The proof embeds the unit ball into a product $\prod_x [-\lVert x\rVert, \lVert x\rVert]$ (one factor per element $x$ of the original space), applies Tychonoff (in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]) to get compactness of the product, and identifies the unit ball as a closed subset. The compactness comes from §7; the construction uses the product topology of [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]].

> [!tip] Unlocked: Prokhorov's Theorem *(from Probability)*
> A family of probability measures on a complete separable metric space is precompact in the weak topology if and only if it is **tight** — for every $\varepsilon$ there is a compact $K$ such that every measure assigns mass $> 1 - \varepsilon$ to $K$. See [[Thm - Prokhorov's Theorem]]. The tight-iff-precompact equivalence is the probability-theoretic instance of the topological compactness apparatus of §7, with the role of "compact closure" replaced by "no mass escaping to infinity".

> [!note] Exercise Index — §7
> [[Exercise Index - §7 Compactness]]

---

# Sources and Targets

**Targets — What do we usually try to prove?**

The recurring targets in §4–7 are *existence statements* — "there is a fixed point", "there is a minimizer", "there is a convergent subsequence" — and *automatic propagation statements* — "the image is also compact / connected / Hausdorff". The existence side is where compactness earns its keep: nearly every existence proof in analysis uses compactness to upgrade a sequence of approximations into a convergent one. The propagation side is where connectedness and continuity meet: any topological property of a connected source pushes forward via continuous maps, giving the family of "automatic" theorems like the intermediate value theorem.

A second class of targets is *separation statements*: showing that two sets, two points, or a point and a set, can be put inside disjoint opens. These are the inputs to constructions of continuous functions (Urysohn) and continuous extensions (Tietze), which is why the separation hierarchy is the central organizing tool of [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]].

A third class is *no-homeomorphism* arguments. Find a topological invariant — number of components, compactness, presence of a cut point — held by one space and not the other. The intermediate value and extreme value theorems are special cases: the discrete topology on $\{0, 1\}$ has two components, so any continuous map from $[0, 1]$ to it is constant, so $f$ cannot jump.

**Sources — What assumptions do we usually leverage?**

The recurring assumption patterns are: a *compactness hypothesis* (on the source, on a subset, on a covering), a *connectedness hypothesis* (the source is path-connected; a subset is dense and connected), a *separation hypothesis* (Hausdorff, regular, normal), or a *continuity hypothesis* (a continuous map is in play). Each of these unlocks a specific transition:

- Compactness + continuity → compactness of the image, the extreme value theorem, closed-map property
- Connectedness + continuity → connectedness of the image, intermediate value theorem
- Hausdorff + compactness → compact subsets are closed, continuous bijections are homeomorphisms, uniqueness of limits
- Normal + closed sets → existence of separating functions (Urysohn, Tietze — in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]])

When a problem combines two of these (a continuous map from a compact connected space, a Hausdorff product of compact spaces), the conclusion is typically the conjunction of what each gives — these are the engine of the most-used theorems in topology.

---

# Legal Operations

1. **Pull back compactness, connectedness, and Hausdorffness through continuity.** Given a continuous $f : X \to Y$: connectedness of $X$ ⇒ connectedness of $f(X)$; compactness of $X$ ⇒ compactness of $f(X)$; Hausdorffness of $Y$ ⇒ ($f$ is determined by its values on a dense set) and ($\{x : f(x) = g(x)\}$ is closed for any other continuous $g$). *Trigger:* a continuous map is in play with the target a Hausdorff space, or the source compact/connected. *Pattern:* state the propagation and read off the consequence.

2. **Extract a convergent subnet from a compact space.** When dealing with a sequence or net in a compact space, every net has a convergent subnet (this is one definition of compactness). *Trigger:* compactness + a sequence/net that you want to converge. *Pattern:* "by compactness, pass to a convergent subnet $x_{\alpha_k} \to x_\infty$" and continue with the limit.

3. **Use the finite-intersection-property formulation.** $X$ is compact iff every collection of closed sets with the finite intersection property has nonempty total intersection. This is the form that converts the cover formulation to "existence of a common point" — exactly what you need to prove things like Tychonoff or the existence of fixed points. *Trigger:* you want to assert that some intersection is nonempty.

4. **Reduce a Hausdorff statement to nets having unique limits.** $X$ Hausdorff iff every convergent net has a unique limit. Conversely, if you can construct a net converging to two distinct points, $X$ cannot be Hausdorff. *Trigger:* prove or disprove Hausdorff.

5. **Apply the tube lemma.** If $Y$ is compact and $N \supseteq \{x_0\} \times Y$ open in $X \times Y$, then a tube $U \times Y \subseteq N$ exists with $U \ni x_0$ open. *Trigger:* a slice in a product space is contained in an open set. *Pattern:* this is the engine of finite products of compacts being compact and of every "compactly-supported" argument in product spaces.

6. **Apply the closed-map property for compact-to-Hausdorff continuous maps.** A continuous map $f : X \to Y$ with $X$ compact and $Y$ Hausdorff is a *closed map*: $f(F)$ is closed for every closed $F$. So if $f$ is also a bijection it is a homeomorphism. *Trigger:* upgrading a continuous bijection. *Pattern:* the "compact-to-Hausdorff" pair is one of the most useful pairs of hypotheses in topology.

7. **Use the Heine–Borel theorem in $\mathbb{R}^n$.** A subset of $\mathbb{R}^n$ is compact iff it is closed and bounded. So "compact" in Euclidean space is checkable by hand. *Trigger:* a problem in $\mathbb{R}^n$ that needs compactness — first check closed and bounded.

8. **Promote sequential statements to net statements in non-first-countable spaces.** If a property fails for sequences in a non-first-countable space (closure not reached by sequences, function not sequentially continuous), use nets — the net version of the same theorem will be true. *Trigger:* working in a product topology over uncountable index set, a weak topology, a quotient of a non-metric space.

9. **Establish path-connectedness, then conclude connectedness.** To prove a space is connected, often easiest is to prove path-connected — exhibit explicit paths between any two points. *Trigger:* path-construction is easier than open-set arguments. *Pattern:* product of path-connected is path-connected; union of path-connected at a common point is path-connected; continuous images of path-connected are path-connected.

**Illegal but tempting operations:**

> [!warning] 1. Using sequences in non-first-countable spaces
> "$x \in \overline{A}$ so a sequence in $A$ converges to $x$" is false in general — it requires first-countability. In a non-first-countable space (Stone–Čech, ordinal spaces, weak topologies on infinite-dimensional Banach spaces) closure is properly larger than sequential closure. The fix: replace sequences with nets, or restrict to first-countable spaces.

> [!warning] 2. Assuming "compact subset" means "closed and bounded" in a general space
> Heine–Borel is *specific to $\mathbb{R}^n$* (more generally finite-dimensional normed spaces). In an infinite-dimensional Banach space, the closed unit ball is bounded but *not* compact, by F. Riesz. In a metric space generally, "compact = closed + totally bounded + complete" — see [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]. Mistaking "closed and bounded" for compactness is the most expensive error in functional analysis.

> [!warning] 3. Treating a continuous bijection as a homeomorphism without compact + Hausdorff
> The unwinding map $[0, 2\pi) \to S^1$ is continuous and bijective but not a homeomorphism, because $[0, 2\pi)$ is not compact. Always check compactness of the source and Hausdorffness of the target before promoting.

> [!warning] 4. Believing connectedness preserves under arbitrary intersections or unions
> "Intersection of connected sets is connected" is false: the upper and lower halves of $S^1$ are both connected, but their intersection is two points. "Union of connected sets is connected" is false unless they share a point: $[0,1] \cup [2, 3]$ is disconnected. The correct statement is: if every pair of the connected sets has nonempty intersection (or more weakly, if there is a common point), the union is connected.

---

# Problem-Solving Strategy

Problems in §4–7 typically ask for one of: a connectedness or compactness statement about a specific space, the verification of a separation axiom, a proof of continuity using either net or sequence convergence, or a "no homeomorphism" argument distinguishing two spaces. Each type routes through one or two principal theorems, and recognizing the type is the main work.

For **proving a space is connected**, the cleanest route is usually path-connectedness: exhibit explicit paths between any two points. When this fails (e.g., the topologist's sine curve), one drops down to the open-cover definition: suppose $X = U \sqcup V$ with both nonempty open, and derive a contradiction. The middle ground — connectedness of a closure $\overline{A}$ given connectedness of $A$ — is the slickest tool when available. To prove a space is *dis*connected, exhibit a continuous nonconstant map to a discrete space, or exhibit a nontrivial clopen subset.

For **proving a space is compact**, the routes are: Heine–Borel if in $\mathbb{R}^n$; closed subset of a known compact (e.g. a closed subset of $[0,1]^n$); continuous image of a known compact; Tychonoff product of compacts (in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]); or direct subcover extraction. The direct extraction is rare and reserved for very concrete spaces. For *sequential* compactness in metric spaces, the route is Bolzano–Weierstrass: a sequence in a closed bounded subset of $\mathbb{R}^n$ has a convergent subsequence. To prove a space is *not* compact, exhibit an open cover with no finite subcover, or a sequence with no convergent subsequence (in first-countable spaces).

For **verifying a separation axiom**, the typical setup is: take the two objects to be separated (two points, or a point and a closed set, or two closed sets), construct disjoint open sets, often via a continuous function with separated values. The metric-space proof "every metric space is normal" — using $\varphi(x) = d(x,F)/(d(x,F) + d(x,G))$ — is the prototype, and it generalizes to **Urysohn's lemma** in normal spaces, which is the standard tool for constructing continuous separations.

For **continuity proofs in non-first-countable spaces**, switch to nets. If you can show "for every net $x_\alpha \to x$, $f(x_\alpha) \to f(x)$", then $f$ is continuous; this is more general than the sequential version and is the right tool when first countability fails. The fact that nets characterize closure and continuity is what makes the abstract topology setup self-consistent: anything you could do with sequences in $\mathbb{R}^n$ you can still do with nets in any space.

For **no-homeomorphism arguments**, the standard invariants in this topic are: number of connected components, presence of a cut point (a point whose removal disconnects the space), compactness or its failure, Hausdorffness or its failure. The classic example: $\mathbb{R}$ has the cut point property (removing any point disconnects it), but $S^1$ does not (removing one point leaves a connected space) — so $\mathbb{R} \not\cong S^1$. Or: $\mathbb{R}$ is not compact but $[0, 1]$ is, hence $\mathbb{R} \not\cong [0, 1]$.

A non-obvious general principle: the *combination* "compact + Hausdorff" is exceptionally well-behaved. Compact Hausdorff spaces are automatically normal, continuous bijections from a compact space to a Hausdorff space are homeomorphisms, compact subsets are closed, and the topology is in some sense "rigid" — any finer topology breaks compactness, any coarser breaks Hausdorffness. Whenever a problem has compact + Hausdorff in its hypotheses, exploit this rigidity: many results are nearly automatic.

---

# Most Reusable Properties

- **[[Thm - Continuous Image of a Compact Space|Continuous images of compact are compact]]**: This propagation is the engine of the extreme value theorem, the compactness of the image of every continuous map from a compact space, and the closed-map property when the target is Hausdorff. Recognize it whenever a compact space appears in the domain of a continuous map — its image is automatically compact, and in $\mathbb{R}$ that means closed and bounded, hence the sup and inf are attained.

- **[[Thm - Continuous Image of a Connected Space|Continuous images of connected are connected]]**: This is the source of the intermediate value theorem, the proof that $S^1 \not\cong S^2$ (one is connected after removing a point, the other isn't), and every "connected $\to$ everywhere" propagation. Recognize it when the goal is to fill in intermediate values, exclude disconnections, or transfer connectedness across a map.

- **[[Thm - Heine–Borel Theorem|Heine–Borel]]**: Compactness in Euclidean space is closed-and-bounded, full stop. This collapses the abstract compactness machinery to a calculable hand-check in $\mathbb{R}^n$, and it is the bridge from analysis to topology. Every "find a compact set in $\mathbb{R}^n$" argument routes through it, and forgetting that it fails in infinite dimensions is the most expensive mistake in functional analysis.

- **[[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism|Compact-to-Hausdorff bijection upgrade]]**: A continuous bijection $f : X \to Y$ with $X$ compact and $Y$ Hausdorff is automatically a homeomorphism. This eliminates the need to check continuity of $f^{-1}$ in a vast class of problems — quotients of compact spaces, embedding theorems, classification arguments. Recognize the hypothesis pair and the conclusion is free.

- **[[Thm - Hausdorff Iff Unique Net Limits|Hausdorff = unique net limits]]**: The characterization of Hausdorff in terms of convergence is what makes "Hausdorff" something usable, not just an axiom. Recognize this any time you want to *use* the Hausdorff hypothesis: it usually appears via uniqueness of a limit or via the closedness of the diagonal $\{(x, x) : x \in X\}$ in $X \times X$.

---

# Bridges

1. **Measure Theory — compact support and Lusin's theorem.** Borel measurable functions on a locally compact Hausdorff space $X$ are connected to continuous functions through **Lusin's theorem**: a measurable function is, off a set of small measure, the restriction of a continuous function. The proof uses the compact subsets of $X$ supplied by the locally compact Hausdorff structure (whose interaction is developed in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]) and Urysohn's lemma for the construction of bump functions. The **Riesz representation theorem** then identifies positive linear functionals on $C_c(X)$ with Radon measures on $X$ — the bridge from topological dual to measure-theoretic object. See [[Measure Theory I — §1 Measure Spaces]].

2. **Probability — tightness and weak compactness of measures.** A family of probability measures $\{\mu_n\}$ on a metric space is **tight** if for every $\varepsilon$ there is a compact $K$ with $\mu_n(K) > 1 - \varepsilon$ for all $n$. **Prokhorov's theorem** says tight families are precompact in the weak topology (see [[Thm - Prokhorov's Theorem]]) — directly a compactness statement in the topology of measures. The escape-of-mass mechanism (a Gaussian shifting to infinity) is exactly the failure mode of compactness, and tightness is the no-escape condition that restores it. See [[Advanced Probability II — Convergence and Limit Theorems]].

3. **Functional Analysis — weak topologies and Banach–Alaoglu.** A normed space $V$ has a **weak topology** generated by the subbasis $\{\varphi^{-1}(U) : \varphi \in V^*, U \subseteq \mathbb{R}\ \text{open}\}$. The closed unit ball of $V^*$ is **weak-$*$ compact** by Banach–Alaoglu — a corollary of Tychonoff (see [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]) applied to $V^*$ embedded in $\prod_{x \in V} [-\lVert x\rVert, \lVert x\rVert]$. This is the source of every "extract a weakly convergent subsequence" argument in PDE, calculus of variations, and stochastic analysis. The compactness comes from §7; the construction needs §8 of [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]].

4. **Algebraic Topology — fundamental group and covering spaces.** Path-connectedness of §4 is the input to the **fundamental group** $\pi_1(X, x_0)$, the first algebraic invariant of a topological space. Compactness shows up in the lifting theorems for covering spaces (a path lifts uniquely because the interval is compact and the cover is "locally split"). The intermediate-value-style argument that distinguishes $S^1$ from $S^2$ via $\pi_1$ is the prototype of using algebraic invariants to prove non-homeomorphism. Bredon Ch. 14 develops this; for now, path-connectedness is the foothold.

5. **Group Theory — topological groups and the closure of a subgroup.** A **topological group** is a group $G$ with a topology such that multiplication and inversion are continuous. The closure $\overline{H}$ of any subgroup $H$ is again a subgroup, a fact requiring continuity of multiplication and the closure characterization of §3 (now upgraded with the net-level closure characterization of §6 for non-metric groups). The connected component of the identity is a closed normal subgroup. These topological-algebra interactions are the foundation of Lie group theory — see [[Group Theory I — §1.1–1.2]] for the algebraic side; the topological side waits in Topology IV.

---

# Insights

The **unifying frame** of §4–7 is that *continuity propagates structure*. Connectedness, compactness, Hausdorffness — each is a structure on a space, and each propagates in a specific direction under continuous maps. Connectedness and compactness propagate *forward*: the image of a connected (compact) space under a continuous map is connected (compact). Hausdorffness propagates *backward in a sense*: the closure of the graph of a continuous map is small (the diagonal is closed). This duality — "compactness/connectedness as source-side properties, Hausdorffness as target-side properties" — organizes nearly every theorem in the chapter and explains why the pair "compact $\to$ Hausdorff" is so well-behaved (the source pulls along compactness, the target preserves the structure).

The **true name** of compactness is "every net has a convergent subnet" (or in metric spaces, "every sequence has a convergent subsequence"). The open-cover definition is technically equivalent, but the subnet/subsequence formulation is what you actually deploy to do analysis. When you want to extract a limit, this is the form. When you want a finite reduction, the open-cover form. They are dual perspectives on the same content. Similarly the true name of connectedness is "every continuous map to a discrete space is constant" — the equivalent which is most useful in practice because it converts a negative statement (no decomposition) into a positive one (locally constant ⇒ constant).

A **trigger-reaction pattern** that comes up throughout analysis: when you want to upgrade a sequence to a convergent subsequence, look for *any* compactness in the picture. The sequence may live in $\mathbb{R}^n$ (compact closed-and-bounded subset), in a separable Hilbert space's unit ball (weakly compact), in the dual of a normed space (weak-$*$ compact by Banach–Alaoglu), in a space of probability measures (compact when tight by Prokhorov). The pattern is always the same: name the compactness, extract a subsequence, pass to the limit. This is *the* signature move of modern analysis.

An **inheritance observation**: connectedness, compactness, and Hausdorffness are *inherited from somewhere*, and the inheritance lineage is often the deepest insight. Compactness in $\mathbb{R}^n$ is inherited from $[0,1]$ via Tychonoff (finite products of compacts are compact). Compactness in a closed bounded subset of a Hilbert space is inherited *not from anywhere* in infinite dimensions — F. Riesz's theorem says it's lost. Connectedness of $S^1$ is inherited from the continuous image of $[0, 2\pi]$. When stuck on whether a space has a property, ask: from where does it inherit? If there is no source, it doesn't have it.

A final pragmatic observation: separation axioms are *commodities*. Each one buys exactly one or two theorems. $T_0$ buys nothing useful in mainstream analysis. $T_1$ buys closed singletons. $T_2$ (Hausdorff) buys uniqueness of limits — universally assumed. $T_3$ (regular) buys closed-neighborhood bases. $T_4$ (normal) buys Urysohn's lemma and Tietze extension. Beyond $T_4$ lie completely regular spaces ($T_{3\frac12}$), paracompact spaces, and Lindelöf spaces, each of which buys further specific theorems. The discipline of *spending only what you need* — using the cheapest separation axiom for each theorem — is the structural backbone of the rest of the topology course.
