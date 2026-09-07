---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Covering Space"
  - "Def - Continuous Map"
tags: [geometry, algebraic-topology, topology]
---

# Notation

$p : \tilde X \to X$ is a covering map. $Y$ is a topological space and $f : Y \to X$ a continuous map. A lift is denoted $\tilde f : Y \to \tilde X$. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the full registry.

---

# Axiom Motivation

A covering map $p : \tilde X \to X$ presents $\tilde X$ as a richer space sitting above $X$. The natural question is: given a map $f$ landing in $X$, can we "promote" it to a map landing in $\tilde X$? That is, can we factor $f$ through the covering?

This is exactly the question a **lift** answers. The diagram is the universal one for "factoring through a cover":
$$
\begin{array}{ccc}
& & \tilde X \\
& \tilde f \nearrow & \downarrow p \\
Y & \xrightarrow{f} & X
\end{array}
$$
We want $\tilde f : Y \to \tilde X$ continuous with $p \circ \tilde f = f$ — equivalently, $\tilde f(y)$ lies in the fibre $p^{-1}(f(y))$ for every $y \in Y$. So at each point $y$, the lift must *choose a point in the fibre* over $f(y)$, and the choices must vary continuously with $y$.

The crucial observation is that local existence of a lift is automatic — at each point we can pick any sheet, and on a small evenly covered neighbourhood the lift is forced to follow that sheet by continuity. The real question is **global existence**: can the local choices be glued into a single continuous map on all of $Y$? This is where the structure of $Y$ matters: if $Y$ is simply connected, local choices have no incompatibility and always glue (this is the easy case of the [[Thm - Lifting Criterion for Continuous Maps|lifting criterion]]); if $Y$ has non-trivial $\pi_1$, then a loop in $Y$ might force the local lifts to disagree when followed around, and obstruct the global lift.

This explains why path lifting is *always* possible (a path is parameterised by $I$, which is contractible and simply connected — see [[Thm - Path Lifting and Homotopy Lifting]]) and why lifting a general map requires the $\pi_1$ inclusion of [[Thm - Lifting Criterion for Continuous Maps]].

Why are lifts the right notion? Because they capture exactly the "extra structure" of the cover: a lift remembers, at each point of $Y$, *which sheet* of the cover we are on. This is the information $\pi_1(X)$ would erase, and what $\pi_1(\tilde X) \leq \pi_1(X)$ remembers. The image $\tilde f_*\pi_1(Y) \leq \pi_1(\tilde X) \leq \pi_1(X)$ is the algebraic data the lift encodes.

A lift is determined by its value at one point. Once you choose $\tilde f(y_0)$ in the fibre $p^{-1}(f(y_0))$, the continuity + local trivialisation forces $\tilde f$ everywhere else (uniqueness of lifts — see Examples). So the question of lifts splits into: (i) does a lift exist, and (ii) how many are there? The answer to (ii) is: at most one for each point of the fibre over a chosen base point (and exactly $|p^{-1}(\text{point})|$ when $Y$ is connected and a lift exists).

---

# The Definition

Let $p : \tilde X \to X$ be a [[Def - Covering Space|covering map]] and let $f : Y \to X$ be a [[Def - Continuous Map|continuous map]] from a topological space $Y$. A **lift** of $f$ through $p$ is a continuous map
$$
\tilde f : Y \to \tilde X
$$
satisfying
$$
p \circ \tilde f = f.
$$
Equivalently, $\tilde f(y) \in p^{-1}(f(y))$ for every $y \in Y$, and $\tilde f$ is continuous.

A lift **based** at a chosen point $y_0 \in Y$ with prescribed image $\tilde x_0 \in p^{-1}(f(y_0))$ is a lift $\tilde f$ with the additional condition $\tilde f(y_0) = \tilde x_0$.

Special cases:
- A **lift of a path** $\gamma : I \to X$ is a continuous $\tilde\gamma : I \to \tilde X$ with $p \circ \tilde\gamma = \gamma$. Once a starting lift $\tilde\gamma(0) \in p^{-1}(\gamma(0))$ is chosen, $\tilde\gamma$ is unique and exists ([[Thm - Path Lifting and Homotopy Lifting]]).
- A **lift of a homotopy** $H : I \times I \to X$ is a continuous $\tilde H : I \times I \to \tilde X$ with $p \circ \tilde H = H$. Once an initial lift on the bottom edge $I \times \{0\}$ is chosen, $\tilde H$ is unique and exists.

---

# Categorical / Structural Definition

In the category $\mathbf{Top}_{/X}$ of topological spaces over $X$ (objects: continuous maps to $X$; morphisms: continuous maps commuting with projection to $X$), a lift of $f : Y \to X$ through $p : \tilde X \to X$ is exactly a morphism $Y \to \tilde X$ in $\mathbf{Top}_{/X}$. So lifts are "morphisms over $X$" — the natural maps between objects living over the same base.

Equivalently, a lift is a section of the pullback bundle: pull $\tilde X \to X$ back via $f$ to get $f^*\tilde X = Y \times_X \tilde X \to Y$, a covering of $Y$; a lift of $f$ is the same as a continuous section $Y \to f^*\tilde X$ of this pullback. So **lifts of $f$** are in natural bijection with **continuous sections of the pulled-back cover** $f^*\tilde X \to Y$. The pulled-back cover is trivial (= disjoint union of copies of $Y$) iff lifts exist — and there are then as many lifts as components of the pullback.

This categorical picture clarifies the lifting criterion: $f^*\tilde X$ is trivial iff the **monodromy** of the cover $\tilde X \to X$ (a homomorphism $\pi_1(X) \to \mathrm{Sym}(p^{-1}(x_0))$) becomes trivial when pulled back via $f_* : \pi_1(Y) \to \pi_1(X)$, which is the case iff $f_*\pi_1(Y)$ lands inside the stabiliser of any fibre point, i.e., inside $p_*\pi_1(\tilde X)$.

---

# Relate to Other Fields / Compression

Lifting a map through a covering is the topological analogue of **section selection in a Galois extension**: given an extension $L/K$ and a $K$-algebra map $K \to A$, choosing a "lift" $A \to L$ is exactly the algebraic problem of factoring through $L$, with obstruction given by the action of $\mathrm{Gal}(L/K)$ on the choices. The categorical picture above is the same.

In differential geometry, lifting is the same operation as **horizontal lift** in a [[Def - Lie Group|principal bundle]] with a connection: a path in the base lifts to a path in the total space along the connection (see [[Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections]]). The covering-space case is the discrete version, where the connection is forced to be trivial (discrete fibre, no continuous gauge freedom).

**True name:** a lift is a *choice of sheet*. For each point $y \in Y$, the cover $p$ presents the fibre over $f(y)$ as a discrete set of options; a lift is a continuous selection — varying $y$, your choice of sheet must change in a coherent way. The lifting *criterion* says when such a coherent selection exists: when the only obstructions, which come from loops in $Y$ that might force inconsistent sheet choices, are killed by $f_*$ landing in the right subgroup.

---

# Examples / Corollaries

**Is an instance: lifting $\gamma : I \to S^1$ to $\mathbb{R}$ via $p(t) = e^{2\pi i t}$.** For any path $\gamma$ in $S^1$, choose a starting fibre point $\tilde\gamma(0) \in p^{-1}(\gamma(0)) \subset \mathbb{R}$ (an integer plus an angle). Then $\tilde\gamma$ exists uniquely; its endpoint $\tilde\gamma(1)$ minus $\tilde\gamma(0)$ is the **winding number** of $\gamma$ (when $\gamma$ is a loop, $\gamma(1) = \gamma(0)$ implies $\tilde\gamma(1) - \tilde\gamma(0) \in \mathbb{Z}$). This is the engine behind [[Thm - Pi_1 of S^1 is Z]].

**Is an instance: lifting a loop $S^1 \to \mathbb{RP}^2$ to $S^2$ via the antipodal cover.** A loop $\gamma : S^1 \to \mathbb{RP}^2$ either lifts to a closed loop on $S^2$ (when $\gamma$ is null-homotopic in $\mathbb{RP}^2$) or to a path joining a point to its antipode (when $\gamma$ is the non-trivial element of $\pi_1(\mathbb{RP}^2) = \mathbb{Z}/2$). The lifting picture *detects* $\pi_1(\mathbb{RP}^2) = \mathbb{Z}/2$.

**Is an instance: lifting a smooth map from a simply-connected space.** If $Y$ is simply connected, every continuous $f : Y \to X$ lifts through every covering $p : \tilde X \to X$ — by the [[Thm - Lifting Criterion for Continuous Maps|lifting criterion]], $f_*\pi_1(Y) = 0 \subseteq p_*\pi_1(\tilde X)$. So lifts $S^2 \to \mathrm{SO}(3)$ to $\mathrm{SU}(2)$ exist; lifts $\mathbb{R}^n \to T^n$ to $\mathbb{R}^n$ exist (trivially); lifts of contractible-domain maps always exist.

**Is NOT an instance: the identity $S^1 \to S^1$ does not lift to $\mathbb{R}$.** A continuous lift $\tilde f : S^1 \to \mathbb{R}$ with $p \circ \tilde f = \mathrm{id}_{S^1}$ would make $\mathbb{R}$ into a (one-sheeted) section of the cover, forcing $\tilde f$ to be a continuous embedding of $S^1$ into $\mathbb{R}$ — impossible, since $S^1$ is not homeomorphic to any subset of $\mathbb{R}$. Algebraically: $\mathrm{id}_*\pi_1(S^1) = \mathbb{Z} \not\subseteq 0 = p_*\pi_1(\mathbb{R})$. This is the prototypical obstruction.

**Is NOT an instance: a continuous loop in $\mathbb{RP}^2$ that is the non-trivial generator does not lift to a loop in $S^2$.** It lifts to a *path* from a point to its antipode — not to a loop. Algebraically, the non-trivial element of $\pi_1(\mathbb{RP}^2)$ is not in the image $p_*\pi_1(S^2) = 0$.

**Corollary (uniqueness of lifts):** if $Y$ is connected and $\tilde f_1, \tilde f_2$ are two lifts of $f$ with $\tilde f_1(y_0) = \tilde f_2(y_0)$ for some $y_0$, then $\tilde f_1 = \tilde f_2$. The set $\{y : \tilde f_1(y) = \tilde f_2(y)\}$ is both open (the two lifts must agree on a neighbourhood of any point of agreement, by the local triviality of $p$) and closed (preimage of the diagonal under $\tilde f_1 \times \tilde f_2 : Y \to \tilde X \times \tilde X$ intersected with the diagonal of $\tilde X$), hence the whole of $Y$ by connectedness.

**Corollary (lift commutes with composition):** if $g : Z \to Y$ is continuous and $\tilde f : Y \to \tilde X$ is a lift of $f : Y \to X$, then $\tilde f \circ g : Z \to \tilde X$ is a lift of $f \circ g : Z \to X$. So lifting plays well with precomposition.

**Corollary (lift determines homotopy class):** if $f_0, f_1 : Y \to X$ are homotopic via $H : Y \times I \to X$ and $\tilde f_0$ is a lift of $f_0$, then the homotopy $H$ lifts (by homotopy lifting on each slice) to $\tilde H : Y \times I \to \tilde X$ with $\tilde H(\cdot, 0) = \tilde f_0$, and $\tilde H(\cdot, 1)$ is then a lift of $f_1$. So homotopic maps lift to homotopic lifts, once initial lifts are chosen.

**Calibration check.** If you can (a) prove uniqueness of lifts on a connected domain, (b) lift the standard loop $\theta \mapsto e^{2\pi i \theta}$ on $S^1$ explicitly to $\mathbb{R}$ and read off the winding number, and (c) explain why the identity $S^1 \to S^1$ does not lift to $\mathbb{R}$ (both topologically and algebraically), you have understood the definition. Bonus: explain why lifting a map $S^1 \to X$ to a cover $\tilde X$ is equivalent to "the loop being a loop in $\tilde X$, not just a path".

---

# Unlocked by This

> [!tip] The Monodromy Action *(in this topic)*
> A covering $p : \tilde X \to X$ determines an action of $\pi_1(X, x_0)$ on the fibre $p^{-1}(x_0)$: given a loop $\gamma$ in $X$ and a point $\tilde x \in p^{-1}(x_0)$, lift $\gamma$ to a path starting at $\tilde x$, and set $\gamma \cdot \tilde x := \tilde\gamma(1)$ (the endpoint). This is the **monodromy action**, and it classifies connected covers up to base-point-preserving isomorphism: connected cover ↔ transitive $\pi_1$-set ↔ subgroup of $\pi_1$. See [[Thm - Galois Correspondence for Covering Spaces]].

> [!tip] Holonomy and Parallel Transport *(from Gauge Theory III)*
> The lift-of-a-path picture generalises to a [[Gauge Theory IV — Connections and Curvature on Principal Bundles|connection]] on a principal bundle: given a path in the base and a starting point in the fibre, the connection prescribes a unique **horizontal lift**, the **parallel transport** of the starting point along the path. The closed-loop version of this is the **holonomy** of the connection, an analogue of the monodromy action of $\pi_1$ on the fibre. The covering-space case is the special instance where the fibre is discrete and the connection has no continuous freedom.
