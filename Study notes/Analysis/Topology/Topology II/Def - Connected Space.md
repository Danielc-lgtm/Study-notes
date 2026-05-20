---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
  - "Def - Closure, Interior, and Boundary"
tags: [analysis, topology]
---

# Notation

Throughout, $X$ is a topological space, with topology $\tau$ (its collection of open sets). A *clopen* subset of $X$ is one that is both open and closed in $X$. The two-point discrete space is $\{0, 1\}$ with topology $\{\emptyset, \{0\}, \{1\}, \{0, 1\}\}$; every map into a discrete space is continuous on each connected fibre of points mapped to the same value. For a continuous map between topological spaces we use the convention from [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]]: "map" means continuous function. The full registry of symbols lives on that parent page.

---

# Axiom Motivation

The intuitive picture we are trying to capture is "one piece" — a space that does not visibly fall apart into separated components. In $\mathbb{R}$, the interval $[0, 1]$ is one piece, the union $[0, 1] \cup [2, 3]$ is two pieces, and the rationals $\mathbb{Q}$ feel like something stranger — every point is somehow isolated from its neighbours by irrationals, even though no two rationals are at positive distance from each other. The challenge is to convert this intuition into a property phrased entirely in terms of the topology, with no reference to a metric.

Begin with the cleanest intuition. If $X$ falls into two separated pieces, then we should be able to write $X = U \sqcup V$ where $U$ and $V$ are open, disjoint, and nonempty. The opens enforce a kind of breathing room: if we tried instead to write $X = A \sqcup B$ with both halves *closed*, the requirement that they cover $X$ and not overlap means each must be the complement of the other, hence both clopen. The two formulations — disjoint nonempty *opens* and disjoint nonempty *clopens* — are the same statement. So we define $X$ to be *connected* if no such decomposition exists. This is a *negative* statement, "no nontrivial decomposition", which makes it slightly awkward to use directly. Hence we always pair it with two positive reformulations.

The first reformulation is that *the only clopen subsets of $X$ are $\emptyset$ and $X$*. If $A$ is a nontrivial clopen subset — neither empty nor everything — then both $A$ and $X \setminus A$ are nonempty opens that partition $X$, and conversely any partition $X = U \sqcup V$ exhibits each of $U, V$ as nontrivial clopen. So "no nontrivial decomposition" and "no nontrivial clopen" are identical claims, just relabelled. This formulation is more useful because to *prove* connectedness we now just have to rule out a single nontrivial clopen, rather than rule out all decompositions.

The second reformulation, which turns out to be the workhorse, is that *every continuous map from $X$ into a discrete space is constant*. The bridge: a continuous map $d : X \to \{0, 1\}$ with the discrete topology on $\{0, 1\}$ has $d^{-1}(0)$ and $d^{-1}(1)$ both clopen (preimages of clopen sets under continuous maps are clopen), and they partition $X$. If $d$ is non-constant, both fibres are nonempty, so we have a nontrivial decomposition. Conversely a nontrivial clopen $A \subsetneq X$ gives the non-constant function $d = \mathbf{1}_A$. This converts connectedness from "no decomposition" into "every locally constant function is constant" — a positive statement perfect for using connectedness as a hypothesis.

Why is this the right level of strictness? It is tempting to ask for something weaker, like "$X$ cannot be the disjoint union of two *closed* sets" — but that is the same statement, since complements of opens are closed. Asking for "$X$ cannot be the union of two disjoint nonempty *arbitrary* subsets" is way too strong — every space with more than one point has such a decomposition. Asking instead that "$X$ has at most one isolated point" or some such surface feature misses the deeper structure: $\mathbb{Q}$ has no isolated points (every neighbourhood contains infinitely many rationals) yet is utterly disconnected. The open/clopen formulation is the unique level at which the definition is strong enough to rule out the genuine pathologies and weak enough that natural spaces like $\mathbb{R}$, $S^1$, $[0,1]$, and $\mathbb{R}^n$ satisfy it.

A final motivating point: connectedness is exactly the property that allows the intermediate value theorem to work. If $f : X \to \mathbb{R}$ is continuous and $X$ is connected, then $f(X)$ is connected (because continuity preserves connectedness — see [[Thm - Continuous Image of a Connected Space]]). The connected subsets of $\mathbb{R}$ are precisely the intervals (an exercise in the open-set definition), and an interval contains every value between any two of its values. So $f$ takes every value between $f(p)$ and $f(q)$ for any $p, q \in X$. The classical intermediate value theorem is exactly this with $X = [a, b]$. The whole point of the abstract definition is to make this argument work in arbitrary topological settings — circles, spheres, function spaces, anywhere you can sensibly talk about continuity.

---

# The Definition

Let $X$ be a topological space.

**Connected space.** $X$ is **connected** if it is *not* the union of two disjoint nonempty open subsets, i.e., there do *not* exist nonempty open $U, V \subseteq X$ with $X = U \cup V$ and $U \cap V = \emptyset$.

**Equivalent formulations.** The following are equivalent for $X$ to be connected:

1. $X$ is not the disjoint union of two nonempty open sets.
2. The only clopen subsets of $X$ are $\emptyset$ and $X$.
3. Every continuous map $d : X \to D$ from $X$ into a discrete space $D$ is constant.

For any subset $A \subseteq X$, we say $A$ is **connected** if it is connected as a topological space in the subspace topology — equivalently, if it cannot be covered by two open sets $U, V \subseteq X$ with $A \cap U \neq \emptyset$, $A \cap V \neq \emptyset$, $A \cap U \cap V = \emptyset$, and $A \subseteq U \cup V$.

A space that is not connected is called **disconnected**, and an expression $X = U \sqcup V$ with $U, V$ disjoint nonempty open sets is called a **separation** of $X$.

---

# Relate to Other Fields / Compression

In **algebra**, a ring $R$ has "no nontrivial idempotents" — no $e \neq 0, 1$ with $e^2 = e$ — exactly when the topological space $\operatorname{Spec} R$ is connected. The bridge is the same disjunction: an idempotent $e$ produces a decomposition $R \cong eR \times (1-e)R$, which on spectra produces a decomposition into two clopen pieces. So connectedness of a space in topology and connectedness of a ring in algebraic geometry are literally the same statement, with the dictionary "nontrivial clopen $\leftrightarrow$ nontrivial idempotent".

In **graph theory**, a graph is connected if any two vertices are joined by a path; this is the discrete analogue and the source of the name. The connected components of a graph (maximal sets of vertices reachable from each other) are the discrete versions of the topological [[Def - Connected Components|connected components]].

In **measure theory** and **probability**, indicator functions of "connected events" — events that cannot be decomposed into mutually exclusive sub-events without losing structure — appear in ergodic theory, where the ergodic decomposition relates to the way a dynamical system's invariant sets sit inside a connected state space. But the most direct compression is to ring theory and algebraic geometry.

---

# Examples / Corollaries

**Is an instance — the real line $\mathbb{R}$.** Connectedness follows from connectedness of $[0, 1]$ (proved via the supremum argument; see [[Ex - The interval [0,1] is connected]]) and the fact that $\mathbb{R} = \bigcup_n [-n, n]$ is a union of overlapping connected sets sharing the origin, hence connected by [[Thm - Union of Overlapping Connected Sets is Connected]]. Same proof works for any interval — open, closed, half-open, finite, or infinite.

**Is an instance — the circle $S^1$.** Realize $S^1$ as the continuous image of $[0, 2\pi]$ under $t \mapsto (\cos t, \sin t)$. Continuous images of connected spaces are connected ([[Thm - Continuous Image of a Connected Space]]), so $S^1$ is connected. The same argument works for $S^n$ for any $n \geq 1$ — it is the continuous image of $\mathbb{R}^n \setminus \{0\}$ under normalisation, and $\mathbb{R}^n \setminus \{0\}$ is path-connected (hence connected) when $n \geq 2$.

**Is NOT an instance — the rationals $\mathbb{Q}$.** For any irrational $\alpha \in \mathbb{R}$, the sets $U = \mathbb{Q} \cap (-\infty, \alpha)$ and $V = \mathbb{Q} \cap (\alpha, \infty)$ are nonempty, open in $\mathbb{Q}$, disjoint, and their union is all of $\mathbb{Q}$. Every $\alpha \notin \mathbb{Q}$ furnishes a separation. In fact every $\mathbb{Q}$-singleton is its own connected component — $\mathbb{Q}$ is *totally disconnected*. Yet $\mathbb{Q}$ is dense in $\mathbb{R}$, so density and connectedness are unrelated.

**Is NOT an instance — the two-point discrete space $\{p, q\}$ with topology $\{\emptyset, \{p\}, \{q\}, \{p, q\}\}$.** Both $\{p\}$ and $\{q\}$ are clopen, so taking $U = \{p\}$, $V = \{q\}$ gives an immediate separation. This is the universal disconnection target: every continuous map into a connected space cannot hit both $p$ and $q$.

**Is NOT an instance — $\mathbb{R} \setminus \{0\}$.** The sets $(-\infty, 0)$ and $(0, \infty)$ are both open in $\mathbb{R}$ and remain open in $\mathbb{R} \setminus \{0\}$, partitioning it. This is the cleanest proof that $\mathbb{R} \setminus \{0\} \not\cong \mathbb{R}$: removing any single point from $\mathbb{R}$ disconnects it, but $\mathbb{R}$ is connected, so no homeomorphism can exist.

**Counter-example for a too-weak variant.** One might try to define "connected" as "not the union of two disjoint nonempty *closed* sets". This sounds like a weaker version. But if $X = A \sqcup B$ with both nonempty closed and disjoint, taking complements gives $A = X \setminus B$ which is open (being the complement of a closed set), and similarly $B$ is open. So both $A$ and $B$ are clopen, and we recover the original definition. The two are equivalent, and any weakening (e.g., demanding nonempty closed but allowing overlap) makes the definition trivially fail for everything.

**Corollary — connectedness is a topological invariant.** If $f : X \to Y$ is a homeomorphism, then $X$ is connected if and only if $Y$ is connected. This is immediate from [[Thm - Continuous Image of a Connected Space]] applied to $f$ and to $f^{-1}$, both of which are continuous.

**Corollary — the closure of a connected set is connected.** If $A \subseteq X$ is connected, so is $\overline{A}$. The proof: any clopen subset $C$ of $\overline{A}$ has $C \cap A$ clopen in $A$, hence equal to $\emptyset$ or $A$. By density of $A$ in $\overline{A}$, $C$ itself must be $\emptyset$ or $\overline{A}$. This is a calibration check that connectedness is "robust under boundary".

**Corollary — connected components are pre-images of "lying in a connected set".** The relation "$p \sim q$ if both lie in a common connected subset" is an equivalence relation (by [[Thm - Union of Overlapping Connected Sets is Connected]]), and its equivalence classes are the [[Def - Connected Components|connected components]]. So connectedness automatically generates a partition.

---

# Unlocked by This

> [!tip] Intermediate Value Theorem *(from this topic)*
> The classical intermediate value theorem is the special case "continuous image of a connected set in $\mathbb{R}$ is connected, hence an interval". See [[Thm - Continuous Image of a Connected Space]]. This pattern — propagation of connectedness across continuity — is the engine of every "no jumps" result in analysis.

> [!tip] **Fundamental Group** *(from Algebraic Topology)*
> A topological space's connected pieces are the input to its **fundamental group**, the first algebraic invariant — but the actual definition needs path-connectedness ([[Def - Path-Connected Space]]) rather than connectedness alone. The fact that $S^1$ has fundamental group $\mathbb{Z}$ — counting how many times a loop winds — is the prototype of using algebraic invariants to distinguish topological spaces.

> [!tip] **Connectedness of $\operatorname{Spec} R$** *(from Algebraic Geometry)*
> A commutative ring $R$ is "indecomposable" — has no nontrivial idempotents — exactly when $\operatorname{Spec} R$ is connected in the Zariski topology. This is the dictionary that lets algebraic geometers move between ring-theoretic decompositions and geometric pieces.
