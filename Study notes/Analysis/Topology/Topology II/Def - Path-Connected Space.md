---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Continuous Map"
  - "Def - Connected Space"
tags: [analysis, topology]
---

# Notation

Throughout, $X$ is a topological space, $[0, 1] = I$ is the unit interval with its standard topology, and a **path** in $X$ from $p$ to $q$ is a continuous map $\gamma : [0, 1] \to X$ with $\gamma(0) = p$ and $\gamma(1) = q$. The reverse path $\overline{\gamma}$ is defined by $\overline{\gamma}(t) = \gamma(1 - t)$; the concatenation of paths $\gamma$ from $p$ to $q$ and $\delta$ from $q$ to $r$ is the path $\gamma \cdot \delta$ from $p$ to $r$ defined piecewise by $\gamma \cdot \delta(t) = \gamma(2t)$ on $[0, 1/2]$ and $\delta(2t - 1)$ on $[1/2, 1]$. The constant path at $p$ is $c_p(t) = p$. The full symbol registry is on the parent page [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Axiom Motivation

We have the definition of [[Def - Connected Space|connectedness]] phrased entirely in terms of open sets: no nontrivial clopen decomposition. This is the right abstract definition, but in practice it is sometimes awkward to use directly — proving that a specific space is connected often requires either explicit construction of a clopen subset (to *disprove*) or a contradiction argument involving suprema (to *prove*, as for $[0, 1]$). What we want is a more *concrete*, *constructive* notion of connectedness: a way to say "any two points in $X$ can be linked".

The intuitive picture is to actually *walk* from $p$ to $q$ inside $X$. A walk is a continuous parameterized motion — a continuous function from a time interval into $X$ — that starts at $p$ and ends at $q$. Formally, we say $X$ is **path-connected** if for any two points $p, q \in X$ there exists a continuous map $\gamma : [0, 1] \to X$ with $\gamma(0) = p$ and $\gamma(1) = q$. The interval $[0, 1]$ is the canonical "time axis", though by reparameterization any other connected interval would do.

This definition is *operationally* stronger than connectedness in two ways. First, it provides an explicit witness — a path — rather than the absence of a clopen subset. Second, it interacts nicely with constructions: composing a continuous path with a continuous map gives a continuous path, so continuous images of path-connected spaces are path-connected; concatenating paths shows that "$p$ and $q$ can be joined by a path" is an equivalence relation. Third, since $[0, 1]$ itself is connected (and indeed path-connected), the image of a path is connected, and the union of the images of all paths from a fixed basepoint is connected — so path-connectedness implies connectedness.

But the converse is *false*. There exist topological spaces that are connected (no nontrivial clopen decomposition) yet not path-connected (no continuous parameterized walk between two specific points). The simplest example, and the canonical pathology of this whole story, is the *topologist's sine curve* — the closure of the graph of $\sin(1/x)$ for $x > 0$ in $\mathbb{R}^2$, with the segment $\{0\} \times [-1, 1]$ on the $y$-axis included. The full set is connected because the wiggly part is connected (a continuous image of $(0, \infty)$) and its closure includes the segment; closures of connected sets are connected. But there is no continuous path from a point on the wiggle to a point on the segment, because such a path would have to enter the segment in finite time after traversing the infinitely many oscillations of $\sin(1/x)$ near $0$, and continuity over $[0, 1]$ rules this out (formalized via uniform continuity on the compact interval).

So why have *both* notions if path-connectedness implies connectedness? The answer is that they are useful for opposite kinds of arguments. Path-connectedness is the *constructive* notion: it is the right concept when you want to *build* continuous maps out of $X$ — to show $X$ admits a continuous family of, say, real-valued functions or homotopies. The path itself is the witness, and concatenation is the construction. Connectedness is the *non-constructive* notion: it is the right concept when you want to *forbid* continuous functions from $X$ to a disconnected target. The contrapositive is what is operative — any continuous map to $\{0, 1\}$ must be constant, so the image cannot "jump". For many natural spaces — $\mathbb{R}^n$, $S^n$ ($n \geq 1$), open intervals, convex sets — the two notions coincide. But for the topologist's sine curve, ordinal spaces, and various pathologies, they diverge, and one always needs to be clear which is being used.

There is a clean condition under which the two notions coincide: **local path-connectedness**. A space is locally path-connected if every neighbourhood of every point contains a path-connected neighbourhood. For locally path-connected spaces, the connected components and path-components agree, and a connected space is automatically path-connected. Manifolds are locally path-connected (every point has a Euclidean neighbourhood, which is path-connected), so the distinction never bites in differential geometry — but the moment one steps outside the locally well-behaved world, the distinction matters.

A final note on the role of the unit interval $[0, 1]$. It is the *universal connected linearly-ordered domain*: any other choice of source ($\mathbb{R}$, $(0, 1)$, any interval) is equivalent by reparametrisation. The reason we pick $[0, 1]$ specifically is that it gives us *endpoint inclusion* — we want to *include* the start and end points $p$ and $q$ — and *compactness* of the source, which is what makes the limiting arguments work cleanly. Using $(0, 1)$ would let paths "escape" to infinity in time, ruining concatenation.

---

# The Definition

Let $X$ be a topological space.

**Path.** A **path** in $X$ from $p$ to $q$ is a continuous map $\gamma : [0, 1] \to X$ with $\gamma(0) = p$ and $\gamma(1) = q$. The points $p$ and $q$ are called the endpoints of $\gamma$.

**Path-connected space.** $X$ is **path-connected** if for any two points $p, q \in X$ there exists a path from $p$ to $q$.

**Path components.** Define a relation $\sim_p$ on $X$ by $p \sim_p q$ if and only if there exists a path from $p$ to $q$. This is an equivalence relation (reflexivity from the constant path $c_p$; symmetry from the reverse path $\overline{\gamma}$; transitivity from the concatenation $\gamma \cdot \delta$). The equivalence classes are called the **path components** of $X$.

**Locally path-connected space.** $X$ is **locally path-connected** if for every $x \in X$ and every neighbourhood $U$ of $x$ there is a path-connected open subset $V \subseteq U$ containing $x$.

A path-connected space is connected, but the converse fails in general; it holds when $X$ is locally path-connected.

---

# Relate to Other Fields / Compression

Path-connectedness is the *zeroth homotopy invariant*: the set of path components of $X$ is denoted $\pi_0(X)$ and is the entry point to **homotopy theory**. The next invariant, $\pi_1(X, x_0)$ — the **fundamental group** — counts equivalence classes of *loops* (paths with $\gamma(0) = \gamma(1) = x_0$) modulo homotopy. The reason path-connectedness rather than connectedness is the starting point for homotopy theory is constructive: one needs an explicit path to define what it means for two loops to be homotopic.

In **algebraic topology**, path-connectedness translates to "$H_0(X) = \mathbb{Z}$" — the zeroth homology group of $X$ has rank equal to the number of path components. So path-connectedness is the topological analogue of "one dimension in degree zero": the simplest algebraic statement about $X$.

In **differential geometry**, a smooth manifold is path-connected if and only if it is connected, because manifolds are locally Euclidean and hence locally path-connected. So the distinction between connectedness and path-connectedness vanishes for manifolds and one rarely worries about it.

In **probability**, an analogous notion appears in the theory of Markov chains and dynamical systems: a state is "reachable" from another if there is a sequence of transitions joining them. Path-connectedness of the state space is the topological version of strong communication in an ergodic Markov chain.

---

# Examples / Corollaries

**Is an instance — convex subsets of $\mathbb{R}^n$.** If $A \subseteq \mathbb{R}^n$ is convex, then for any $p, q \in A$ the straight-line path $\gamma(t) = (1 - t)p + tq$ is in $A$ for all $t$, and it is continuous, so $A$ is path-connected. This covers all open balls, all rectangles, all half-spaces, all convex polyhedra. It is the foundational source of path-connected examples.

**Is an instance — the $n$-sphere $S^n$ for $n \geq 1$.** Given $p, q \in S^n$ with $p \neq -q$, the path $\gamma(t) = \frac{(1-t)p + tq}{\|(1-t)p + tq\|}$ stays on $S^n$ and is continuous (the denominator never vanishes). If $p = -q$, use any intermediate point and concatenate two such paths. The case $S^0 = \{-1, 1\}$ is *not* path-connected — it has two components.

**Is an instance — $\mathbb{R}^n \setminus \{0\}$ for $n \geq 2$.** Any two points $p, q \in \mathbb{R}^n \setminus \{0\}$ can be joined by a piecewise-linear path avoiding the origin, because in dimension $\geq 2$ there is enough room to route around. This is the reason $\mathbb{R}^n \setminus \{0\}$ for $n \geq 2$ is path-connected, while $\mathbb{R} \setminus \{0\}$ is not — a fundamental dimension effect that propagates to topology, complex analysis (the role of $\mathbb{C} \setminus \{0\}$), and physics (no monopoles in $\mathbb{R}^3$ without a Dirac string).

**Is NOT an instance — the topologist's sine curve.** Let $X = \{(x, \sin(1/x)) : x > 0\} \cup \{0\} \times [-1, 1]$ in $\mathbb{R}^2$. Then $X$ is connected (the wiggle part is connected, and the closure of a connected set is connected) but *not* path-connected: there is no continuous $\gamma : [0, 1] \to X$ from a point on the segment, say $(0, 0)$, to a point on the wiggle, say $(1/\pi, 0)$. The reason is that as $\gamma$ leaves the segment and enters the wiggle, it would have to traverse the rapid oscillations of $\sin(1/x)$ near $x = 0$ — but $\gamma$ is continuous on the compact $[0, 1]$, hence uniformly continuous, and uniform continuity rules out the unbounded oscillation. See [[Ex - The topologist's sine curve]] for the full proof.

**Is NOT an instance — the long line.** The "long line" is a topological space obtained by gluing copies of $[0, 1)$ indexed by an uncountable ordinal. It is connected and locally Euclidean but not path-connected to any point at the "long end", because no path from a finite-ordinal point can reach beyond the first uncountable ordinal in finite time. This is a pathology relevant to the foundations of differential topology.

**Corollary — path-connectedness implies connectedness.** If $X$ is path-connected, fix any $x_0 \in X$ and write $X = \bigcup_{q \in X} \gamma_q([0, 1])$ where $\gamma_q$ is a path from $x_0$ to $q$. Each $\gamma_q([0, 1])$ is a continuous image of $[0, 1]$, hence connected. They all contain $x_0$, so by [[Thm - Union of Overlapping Connected Sets is Connected]] their union $X$ is connected.

**Corollary — path components partition $X$.** The relation $\sim_p$ is an equivalence relation by the constant/reverse/concatenation paths, so its equivalence classes — the path components — partition $X$. Each path component is path-connected (any two points in a path component are joined by a path, by definition).

**Corollary — continuous images of path-connected spaces are path-connected.** If $f : X \to Y$ is continuous and $X$ is path-connected, then $f(X)$ is path-connected: given $p', q' \in f(X)$, pick preimages $p, q$ and a path $\gamma : [0, 1] \to X$ from $p$ to $q$, then $f \circ \gamma$ is a path in $f(X)$ from $p'$ to $q'$.

**Calibration check.** Verify that the **comb space** $\{(x, 0) : x \in [0, 1]\} \cup \bigcup_{n \geq 1} \{1/n\} \times [0, 1] \cup \{0\} \times [0, 1]$ — a horizontal segment, vertical teeth at $1/n$, and a single vertical segment on the left — is path-connected, but that removing the horizontal segment's interior (keeping only the teeth and the left segment) gives a space that is connected but not path-connected. The mechanism is the same as the topologist's sine curve: the teeth get arbitrarily close to the left segment, but no path can jump from one to the other.

---

# Unlocked by This

> [!tip] **Fundamental Group $\pi_1$** *(from Algebraic Topology)*
> Once path-connectedness is fixed, one defines a **loop** at $x_0$ as a path $\gamma : [0, 1] \to X$ with $\gamma(0) = \gamma(1) = x_0$, and the **fundamental group** $\pi_1(X, x_0)$ as the set of homotopy classes of such loops under concatenation. The fact that $\pi_1(S^1) = \mathbb{Z}$ is the first nontrivial computation in algebraic topology and the source of degree theory, winding numbers, and the proof that $\mathbb{C} \setminus \{0\}$ has nontrivial complex analysis (logarithms, branch cuts).

> [!tip] **Higher Homotopy Groups $\pi_n$** *(from Algebraic Topology)*
> Replacing the source $[0, 1]$ with $S^n$ gives the higher homotopy groups $\pi_n(X, x_0)$ — equivalence classes of maps $S^n \to X$ taking the basepoint to $x_0$, modulo homotopy. These detect higher-dimensional "holes" in $X$. The computation $\pi_n(S^n) = \mathbb{Z}$ is the engine of degree theory and Brouwer's fixed point theorem.

> [!tip] **Covering Spaces** *(from Algebraic Topology)*
> A **covering space** of $X$ is a space $\widetilde X$ with a continuous surjection $\widetilde X \to X$ that is locally a homeomorphism on a discrete fibre. Covering spaces exist iff $X$ is path-connected, locally path-connected, and semi-locally simply connected — exactly the conditions for $\pi_1$ to behave well. The universal cover, the deck transformation group, and the Galois correspondence between covers and subgroups of $\pi_1$ all rest on path-connectedness.
