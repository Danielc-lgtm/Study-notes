---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Closure, Interior, and Boundary"
  - "Def - Neighbourhood and Neighbourhood Basis"
tags: [analysis, topology]
---

# Notation

Throughout, $X$ is a topological space. For points $x, y \in X$ and closed sets $F, G \subseteq X$, we say $X$ "separates" two objects (points, or a point and a set, or two sets) by *disjoint open sets* if there exist disjoint opens each containing one of them. We refer to the separation axioms by their numbering $T_0, T_1, T_2, T_3, T_4$, in increasing strength. The convention used here — that $T_3$ (regular) and $T_4$ (normal) include $T_1$ — is the Bredon convention; other books vary, and we note where this matters. The full registry of symbols is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Axiom Motivation

The bare axioms of a topological space — a collection of open sets closed under finite intersection and arbitrary union — are remarkably weak. They are weak enough that some "spaces" we would not normally think of as separated still satisfy them: a two-point space $\{x, y\}$ with topology $\{\emptyset, \{x, y\}\}$ (the trivial topology) has $x$ and $y$ literally indistinguishable from the perspective of open sets — every open set contains both or neither. In such a space, sequences can converge to multiple distinct points, continuous functions can fail to be determined by their values on dense sets, and a thousand other reasonable expectations fail. The separation axioms are the *minimum* extra hypotheses needed to recover the expectations.

The hierarchy is built by asking: how much can we *distinguish* via open sets? At the weakest level, $T_0$: given two distinct points, at least one open set should contain one of them but not the other. This is the bare minimum for points to be "topologically distinguishable" — if $T_0$ fails, two distinct points have *exactly the same* neighbourhoods, and from the topology's point of view they are the same. The trivial topology on a set with $\geq 2$ points fails $T_0$.

Slightly stronger, $T_1$: for *each* pair of distinct points, *each* should have an open neighbourhood excluding the other. Symmetric this time — both directions. The remarkable equivalent form: *every singleton is closed*. The bridge: if $T_1$ holds, for each $y \neq x$ pick an open $U_y \ni y$ with $x \notin U_y$; then $X \setminus \{x\} = \bigcup_{y \neq x} U_y$ is open, so $\{x\}$ is closed. Conversely, if $\{x\}$ is closed, then $X \setminus \{x\}$ is an open set containing every $y \neq x$ but not $x$. The $T_1$ axiom is the standard "points are individual" condition — fails in spaces like the Sierpiński space $\{0, 1\}$ with topology $\{\emptyset, \{1\}, \{0, 1\}\}$, where $\{0\}$ is not closed.

Now the most important one, $T_2$ or **Hausdorff**: for any two distinct points $x \neq y$, there exist *disjoint* open neighbourhoods $U \ni x$ and $V \ni y$. This is a substantive strengthening of $T_1$: the cofinite topology on an infinite set is $T_1$ (singletons are closed: their complements are cofinite, hence open) but *not* Hausdorff (any two nonempty opens have cofinite complements and so must intersect). What does Hausdorff buy? *Uniqueness of limits*. A net converges to at most one point iff $X$ is Hausdorff (see [[Thm - Hausdorff Iff Unique Net Limits]]). Without Hausdorff, the statement "$\lim x_n = L$" is multivalued, and basic identities of analysis fall apart. Essentially all spaces of interest in analysis and geometry are Hausdorff, and the assumption is often built into the definition of "topological space" in textbooks. In Bredon, Hausdorff is *not* built in and we keep it as an extra axiom.

Beyond Hausdorff, $T_3$ or **regular**: $X$ is $T_1$ and for any point $x$ and any closed set $F$ not containing $x$, there exist disjoint opens $U \ni x$, $V \supseteq F$. The $T_1$ clause ensures that regularity strengthens Hausdorff: a single point is a special case of a closed set (because $T_1$ ⇒ singletons closed), so regular implies Hausdorff. What does regular buy? *Closed neighbourhood bases*: a Hausdorff space $X$ is regular iff at every point, the closed neighbourhoods of the point form a neighbourhood basis (see [[Thm - Regular Iff Closed Neighborhoods Form a Basis]]). This is the natural condition for many constructions involving extension of functions.

Strongest, $T_4$ or **normal**: $X$ is $T_1$ and for any two *disjoint closed* sets $F, G$, there exist disjoint opens $U \supseteq F$, $V \supseteq G$. The $T_1$ clause again upgrades this so normal implies regular implies Hausdorff. Normal is the strongest separation axiom we routinely use. It is the assumption for **Urysohn's lemma** (every normal space admits, for any two disjoint closed sets, a continuous function $X \to [0, 1]$ equal to $0$ on one and $1$ on the other) and **Tietze's extension theorem** (every continuous real-valued function on a closed subset of a normal space extends to a continuous function on the whole space). These are the engines of much of analysis on topological spaces, and they require normal as their input.

A crucial point of convention. The above hierarchy with $T_1$ built into $T_3$ and $T_4$ ensures $T_4 \Rightarrow T_3 \Rightarrow T_2 \Rightarrow T_1 \Rightarrow T_0$, which is what we want. Without the $T_1$ clauses, "regular" and "normal" can hold in pathological non-Hausdorff spaces (the trivial topology is vacuously normal-without-$T_1$, for instance). Some books — notably Munkres — use "regular" and "normal" for the versions *without* $T_1$, calling the $T_1$ versions "$T_3$" and "$T_4$" instead. Bredon and we use the convention with $T_1$ built in. Whenever the literature is ambiguous, the careful thing is to spell out "regular Hausdorff" or "$T_3$" explicitly.

Each axiom is the *minimum hypothesis* under which a certain theorem becomes true. $T_2$ is the minimum for unique limits. $T_3$ is the minimum for closed neighbourhood bases. $T_4$ is the minimum for Urysohn's lemma. The discipline of using the *cheapest* separation axiom for each theorem — never more than needed — is the structural backbone of much of general topology.

---

# The Definition

Let $X$ be a topological space. The separation axioms are:

**$T_0$.** $X$ is **$T_0$** if for any two distinct points $x \neq y$ in $X$, there exists an open set containing one of $x, y$ but not the other.

**$T_1$.** $X$ is **$T_1$** if for any two distinct points $x \neq y$ in $X$, there exists an open set containing $x$ but not $y$, and an open set containing $y$ but not $x$. Equivalently, every singleton $\{x\} \subseteq X$ is closed.

**$T_2$ (Hausdorff).** $X$ is **$T_2$** or **Hausdorff** if for any two distinct points $x \neq y$ in $X$, there exist disjoint open sets $U, V$ with $x \in U$ and $y \in V$.

**$T_3$ (Regular).** $X$ is **$T_3$** or **regular** if $X$ is $T_1$ and for any point $x \in X$ and any closed set $F \subseteq X$ with $x \notin F$, there exist disjoint open sets $U, V$ with $x \in U$ and $F \subseteq V$.

**$T_4$ (Normal).** $X$ is **$T_4$** or **normal** if $X$ is $T_1$ and for any two disjoint closed sets $F, G \subseteq X$, there exist disjoint open sets $U, V$ with $F \subseteq U$ and $G \subseteq V$.

**Hierarchy.** Under this convention,
$$T_4 \implies T_3 \implies T_2 \implies T_1 \implies T_0,$$
each implication strict — counter-examples in the next section show none of the reverse implications hold.

---

# Relate to Other Fields / Compression

The separation axioms are commodities: each one buys a specific theorem. They are not a single property; they are a stratified list of *minimum hypotheses* for distinct purposes. In **functional analysis**, Hausdorff is built into the definition of "topological vector space" because the dual space, the weak topology, and every locally convex construction need uniqueness of limits. In **measure theory**, the underlying topological space of a Radon measure is required to be Hausdorff (and usually locally compact Hausdorff or Polish — completely metrisable separable) because the Riesz representation theorem and regularity properties of measures depend on Urysohn's lemma, which needs normality. In **algebraic geometry**, schemes are usually *not* Hausdorff — the Zariski topology on an irreducible variety has the generic point in every nonempty open, an extreme failure of Hausdorff — and so algebraic geometers built a parallel structure (sheaves, étale topology, scheme morphisms) that does not need separation in the topological sense. In **differential geometry**, manifolds are by convention Hausdorff and second countable; without Hausdorff, weird "line with two origins" objects appear that satisfy the local Euclidean condition but lack uniqueness of limits.

The separation hierarchy organizes which spaces admit which constructions. A normal Hausdorff space admits continuous separating functions (Urysohn) and continuous extensions of bounded continuous functions (Tietze). A completely regular space ($T_{3.5}$, an axiom intermediate between $T_3$ and $T_4$) is exactly the class of spaces embeddable into a product of intervals — the input to Stone–Čech compactification. A metric space is automatically normal (see [[Thm - Metric Spaces are Normal]]), so all separation axioms hold and the hierarchy is invisible. The hierarchy matters precisely outside the metric world.

In **logic and set theory**, the separation axioms relate to the axiom of choice through Urysohn's lemma — the construction of a continuous separating function uses a countably infinite sequence of refinements, which is a fragment of choice. In ZF without choice, separation axioms still work but Urysohn becomes a substantive theorem.

---

# Examples / Corollaries

**Is an instance of $T_4$ — every metric space.** For disjoint closed sets $F, G$ in a metric space $X$, the function $\varphi(x) = d(x, F)/(d(x, F) + d(x, G))$ is continuous (where $d(x, F) = \inf_{y \in F} d(x, y)$), and the open sets $\varphi^{-1}([0, 1/2))$ and $\varphi^{-1}((1/2, 1])$ are disjoint opens containing $F$ and $G$ respectively. So metric spaces satisfy all separation axioms $T_0$ through $T_4$. See [[Thm - Metric Spaces are Normal]].

**Is an instance of $T_4$ but interesting — every compact Hausdorff space.** The proof uses compactness in a tube-lemma style argument: for disjoint closed $F, G$ in a compact Hausdorff $X$, each pair $(x, y) \in F \times G$ can be separated by disjoint opens; use compactness of $F$ and $G$ (closed subsets of compact are compact) to extract finite covers and assemble disjoint opens. So $\text{compact} + \text{Hausdorff} \Rightarrow \text{normal}$ — see [[Ex - Compact + Hausdorff implies normal]]. This is one of the most useful instances and the reason "compact Hausdorff" is the most-used pair of hypotheses in topology.

**Is an instance of $T_1$ but NOT $T_2$ — the cofinite topology on an infinite set.** Let $X$ be infinite (say $X = \mathbb{N}$ or $\mathbb{R}$) with the cofinite topology: the open sets are the empty set and complements of finite sets. Then every singleton $\{x\}$ is closed (its complement is cofinite, hence open), so $T_1$ holds. But any two nonempty open sets are cofinite, so their intersection is also cofinite, in particular nonempty. There are no disjoint nonempty opens, so Hausdorff fails. The failure mode is dramatic: in the cofinite topology on $\mathbb{N}$, the sequence $x_n = n$ converges to *every* point of $\mathbb{N}$. See [[Ex - A T1 space that is not Hausdorff]].

**Is an instance of $T_2$ but NOT $T_3$ — the "tangent disc" topology on $\mathbb{R}^2$.** Take $\mathbb{R}^2$ with the topology generated by the usual opens together with sets of the form $\{(x, y) : x^2 + y^2 < a, y \neq 0\} \cup \{(0, 0)\}$ — i.e., the standard open balls combined with "punctured balls at the origin plus the origin itself". Distinct points are separated by usual opens, so Hausdorff holds. But the closed set $\{(0, y) : y \neq 0\}$ cannot be separated from the origin by disjoint opens — any open containing the origin must contain a "punctured ball" (the special basis element), whose closure contains points arbitrarily near $(0, y)$ for $y$ near $0$. So $T_3$ fails. See [[Ex - A Hausdorff space that is not regular]].

**Is an instance of $T_3$ but NOT $T_4$ — the Sorgenfrey plane $\mathbb{R}_\ell \times \mathbb{R}_\ell$ (lower-limit topology).** The Sorgenfrey line $\mathbb{R}_\ell$ — $\mathbb{R}$ with the topology generated by half-open intervals $[a, b)$ — is normal (it is hereditarily Lindelöf + regular). But the product $\mathbb{R}_\ell \times \mathbb{R}_\ell$ — the Sorgenfrey plane — is *not* normal: the antidiagonal $\{(x, -x) : x \in \mathbb{R}\}$ is closed and discrete (the subspace topology makes it homeomorphic to $\mathbb{R}$ with the discrete topology), and one can construct two disjoint closed subsets of the antidiagonal that cannot be separated. This is a famous counterexample showing that products of normal spaces are not always normal.

**Is NOT an instance of $T_0$ — the trivial topology on a set with $\geq 2$ points.** $X = \{x, y\}$ with topology $\{\emptyset, X\}$: the only open sets are $\emptyset$ and the whole space, neither of which distinguishes $x$ from $y$. Failure of $T_0$ in the cleanest possible way.

**Is an instance of $T_0$ but NOT $T_1$ — the Sierpiński space.** $X = \{0, 1\}$ with topology $\{\emptyset, \{1\}, \{0, 1\}\}$: the open set $\{1\}$ distinguishes $1$ from $0$ (containing one but not the other), so $T_0$ holds. But there is no open set containing $0$ that excludes $1$ — every open containing $0$ is the whole space. So $T_1$ fails. The Sierpiński space is the model space for "specialization order" in algebraic geometry and category theory.

**Corollary — singletons are closed in any $T_1$ space.** For each $y \neq x$, choose an open $U_y$ containing $y$ but not $x$. Then $X \setminus \{x\} = \bigcup_{y \neq x} U_y$ is open, so $\{x\}$ is closed.

**Corollary — Hausdorffness implies unique sequential/net limits.** If $x_\alpha \to x$ and $x_\alpha \to y$ in a Hausdorff space $X$, then $x = y$. The full characterisation is [[Thm - Hausdorff Iff Unique Net Limits]] — Hausdorff is *equivalent* to unique net limits.

**Corollary — closed subsets and graphs of continuous functions to Hausdorff spaces.** If $f, g : X \to Y$ are continuous and $Y$ is Hausdorff, then $\{x : f(x) = g(x)\}$ is closed in $X$. (Apply the closedness of the diagonal $\Delta_Y \subseteq Y \times Y$, which holds iff $Y$ is Hausdorff, and pull back along $(f, g)$.) So continuous functions to Hausdorff targets are determined by their values on dense subsets.

**Calibration check.** For each axiom in the hierarchy, identify both: (i) a space that satisfies it but not the next one up; (ii) a theorem that requires it. For $T_1$: cofinite topology on $\mathbb{N}$; theorem = "singletons are closed". For $T_2$: any non-regular Hausdorff space; theorem = "limits are unique". For $T_3$: Sorgenfrey plane; theorem = "closed neighbourhoods form a basis". For $T_4$: real line; theorem = "Urysohn's lemma".

---

# Unlocked by This

> [!tip] **Urysohn's Lemma** *(from Topology III)*
> A topological space is normal if and only if for any two disjoint closed sets $F, G$ there exists a continuous function $f : X \to [0, 1]$ with $f|_F = 0$ and $f|_G = 1$. The "only if" direction is the substantial one and is the construction at the heart of much of general topology. See [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

> [!tip] **Tietze Extension Theorem** *(from Topology III)*
> In a normal space $X$, any continuous function $f : F \to \mathbb{R}$ on a closed subset $F$ extends to a continuous function $\tilde f : X \to \mathbb{R}$. This is the engine behind extending continuous data from closed subsets, and is the input to many constructions in algebraic topology (partitions of unity, mapping cones, CW complex constructions).

> [!tip] **Stone–Čech Compactification** *(from Topology III)*
> A Hausdorff space $X$ embeds into a compact Hausdorff space if and only if it is *completely regular* (a separation axiom $T_{3.5}$ between $T_3$ and $T_4$). The maximal such compactification, the Stone–Čech compactification $\beta X$, is the universal target for continuous maps from $X$ into compact Hausdorff spaces.
