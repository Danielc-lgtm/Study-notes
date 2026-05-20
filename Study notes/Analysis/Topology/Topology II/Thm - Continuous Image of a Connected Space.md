---
type: theorem
subject: topology
prereqs:
  - "Def - Connected Space"
  - "Def - Continuous Map"
  - "Def - Topological Space"
tags: [analysis, topology, connectedness]
---

# Notation

$X, Y$ are topological spaces (see [[Def - Topological Space]]). A **map** in this topic always means a continuous map (see [[Def - Continuous Map]]). $f(X) \subseteq Y$ is the image of $f$, equipped with the [[Def - Subspace Topology|subspace topology]] inherited from $Y$. A subset $A \subseteq Z$ is **clopen** if it is both open and closed; equivalently, the indicator $\mathbf{1}_A : Z \to \{0, 1\}$ (discrete topology on $\{0, 1\}$) is continuous. The full registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Theorem.** Let $f : X \to Y$ be a continuous map and suppose $X$ is [[Def - Connected Space|connected]]. Then the image $f(X) \subseteq Y$, regarded with the subspace topology, is connected.

The conclusion says nothing about $Y$ as a whole — only about the image. This is the cleanest theorem in the chapter: a one-line proof using the equivalent formulation of connectedness in terms of discrete-valued maps.

---

# Motivation

Connectedness is the topological encoding of "no jumps". It is what makes the intermediate value theorem true: a continuous function on a connected interval cannot skip values. The general question this theorem answers is: *which structural properties of a space transfer to its continuous images?* For most properties the answer is "very few" — continuity is a weak condition. But for connectedness, the answer is automatic and free: every continuous map takes connected sets to connected sets. This is *the* propagation theorem from which the intermediate value theorem and a dozen other "automatic" facts of analysis flow.

The reason this works while propagation under continuity often fails is that connectedness is a *negative* property — the absence of a clopen decomposition — and continuity *creates* preimages of opens in $Y$ from opens in $X$. A clopen decomposition of $f(X)$ would pull back to a clopen decomposition of $X$, which connectedness forbids. So *continuity propagates connectedness in the same direction continuity propagates open sets*: backwards, in the form of an obstruction.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$X$ is connected". One needs ways to recognize connectedness in disguise.

The first disguised source is **path-connectedness**. Property $B$: every two points of $X$ are joined by a continuous path $\gamma : [0, 1] \to X$. The bridge: each path-image is the continuous image of the connected interval $[0, 1]$ (using *this theorem* applied to $\gamma$), so it is connected; and the whole space is the union of paths through any fixed basepoint, all sharing the basepoint, so by [[Thm - Union of Overlapping Connected Sets is Connected|the overlap theorem]] $X$ itself is connected. *Example:* $\mathbb{R}^n$, $S^n$ for $n \geq 1$, the disk $D^n$, and every convex set are path-connected, hence connected, hence this theorem applies to every continuous image of any of them.

The second disguised source is **a dense connected subset**. Property $B$: $A \subseteq X$ is connected and $X \subseteq \overline{A}$. The bridge: the closure of a connected set is connected. *Example:* to show $\mathbb{R}$ with the standard topology is connected, observe that $\mathbb{Q}$ is *dis*connected but $\mathbb{R} = \overline{[0, 1] \cup [0, 1]^c \cap \mathbb{R}}$ — or more usefully, prove $[0, 1]$ is connected by hand and apply this to the inclusion $[0, 1] \hookrightarrow \mathbb{R}$.

The third disguised source is **a union of connected sets sharing a common point or with pairwise nonempty intersection**. Property $B$: $X = \bigcup_\alpha Y_\alpha$ where each $Y_\alpha$ is connected and they pairwise overlap. The bridge: this is precisely [[Thm - Union of Overlapping Connected Sets is Connected]]. *Example:* a star-shaped region in $\mathbb{R}^n$ is the union of line segments from a centre point — each segment is connected (homeomorphic to $[0, 1]$), all share the centre, so the union is connected, and this theorem applies to any continuous image.

**Targets (Output Amplification)**

The conclusion is "$f(X)$ is connected".

Combine the conclusion with **$Y = \mathbb{R}$ and the fact that connected subsets of $\mathbb{R}$ are intervals**. Property $D$: $f : X \to \mathbb{R}$ is real-valued. Amplified result $E$: $f$ attains *every value between any two of its values*. This is the **intermediate value theorem** in its general topological form. The non-obviousness is that no specific property of $\mathbb{R}$ beyond "connected subsets are intervals" is needed; this is a pure topology theorem masquerading as an analysis theorem.

Combine the conclusion with **$Y$ Hausdorff and $f(X)$ finite**. Property $D$: $f(X)$ has only finitely many points and $Y$ is Hausdorff. Amplified result $E$: $f$ is constant. The bridge: in a Hausdorff space, finite sets are discrete subspaces, but connected subsets of a discrete space are singletons. *Example:* every continuous map from a connected space to $\mathbb{Z}$ (with the subspace topology from $\mathbb{R}$) is constant — the engine of countless "winding number is locally constant" arguments.

Combine the conclusion with **the contrapositive: $f(X)$ has more than one component**. Property $D$: one knows $f(X) \subseteq Y_0 \sqcup Y_1$ where $Y_0, Y_1$ are disjoint open neighborhoods that each meet $f(X)$. Amplified result $E$: $X$ is not connected. This is the standard tool for *proving disconnectedness* of $X$: build a continuous map to a discrete space with at least two values.

---

# Why Is It True

Connectedness is best thought of as the condition "every continuous map to a discrete space is constant". This reformulation converts connectedness from a *negative* statement (no clopen decomposition) into a *positive* one (every locally-constant function is globally constant), which is what makes proofs work.

Now consider a continuous $f : X \to Y$ with $X$ connected, and suppose for contradiction $f(X)$ is *not* connected. Then there is a nonconstant continuous map $d : f(X) \to \{0, 1\}$ to the two-point discrete space. Compose: $d \circ f : X \to \{0, 1\}$ is continuous (composition of continuous maps) and *also* nonconstant (because $d$ is nonconstant on the image of $f$). But this contradicts the connectedness of $X$. So $f(X)$ admits no such $d$, hence $f(X)$ is connected.

The proof is one line because the discrete-valued map formulation of connectedness is *exactly* the formulation that interacts well with continuity. A clopen subset $A$ of $f(X)$ gives the nonconstant discrete map $\mathbf{1}_A$; pulled back via $f$, it becomes a nonconstant discrete map on $X$, which connectedness forbids. The whole content of the proof is choosing the right reformulation of connectedness.

A geometric picture: think of $X$ as a "single piece of clay". A continuous map can stretch, fold, and pinch — but it cannot tear. If $f(X)$ were two separated pieces, those pieces' preimages would tear $X$ apart, which it forbids. Continuity transports "no tearing" from $X$ to its image.

---

# What Makes This Hard

The theorem itself is one line, but the *application* requires recognizing the disguised source: many "$X$ is connected" hypotheses arrive as "$X$ is path-connected", "$X$ is convex", "$X$ is the closure of a connected set", or "$X$ is a union of overlapping connected pieces", and the reader must reroute each to connectedness before applying the theorem. The most common error in the proof itself is to use the clopen-subset formulation directly — which works but is two or three lines longer than the discrete-map version — and to forget that the *image* gets the subspace topology, so "clopen in $f(X)$" is what one pulls back, not "clopen in $Y$".

---

# Rederivation Scaffold

**High-level strategy:**
Rewrite connectedness in its operational form: *every continuous map to a discrete space is constant*. Then a discrete-valued map on $f(X)$, composed with $f$, would be a discrete-valued map on $X$, hence constant — forcing the original to be constant. One line.

**Subgoal decomposition:**

1. **Switch to the discrete-map form of connectedness.** $X$ is connected if and only if every continuous map $d : X \to \{0, 1\}$ (with discrete topology) is constant.
   - *Hint:* This is [[Def - Connected Space|Definition / Proposition 4.5 of Bredon]], equivalent to "no nontrivial clopen subset" by taking $d = \mathbf{1}_A$.
   - *Why needed:* Discrete-valued maps compose with continuous maps cleanly; clopen subsets need preimage-of-clopen-is-clopen, which is the same content but less direct.

2. **Lift any discrete map on $f(X)$ to one on $X$ via composition.** Given continuous $d : f(X) \to D$, set $d \circ f : X \to D$.
   - *Hint:* Compositions of continuous maps are continuous.
   - *Why needed:* This is the only nontrivial step. $X$ connected forces $d \circ f$ constant, hence $d$ constant on $f(X)$.

3. **Conclude $f(X)$ connected.** Every continuous map from $f(X)$ to a discrete space is constant, hence $f(X)$ is connected.
   - *Hint:* Apply the equivalence of subgoal 1 to $f(X)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Connectedness equals "every discrete-valued map is constant"
> **Statement:** A topological space $Z$ is connected if and only if every continuous map $d : Z \to D$, with $D$ any discrete topological space, is constant.
>
> **Hint:** A clopen subset $A$ gives the discrete map $\mathbf{1}_A$ to $\{0, 1\}$; conversely, $d^{-1}(\{y\})$ is clopen.
>
> **Why needed:** It is the form of connectedness this proof uses.
>
> > [!note]- Full proof
> > ($\Rightarrow$) Suppose $Z$ is connected, $d : Z \to D$ continuous, and $y \in d(Z)$. Then $d^{-1}(\{y\})$ is the preimage of the open set $\{y\}$ (open in the discrete $D$), so it is open. Its complement $d^{-1}(D \setminus \{y\})$ is the preimage of the open set $D \setminus \{y\}$, so it is also open. So $d^{-1}(\{y\})$ is clopen and nonempty, hence equal to $Z$ by connectedness. So $d$ is constant with value $y$.
> >
> > ($\Leftarrow$) If $Z$ has a nontrivial clopen subset $A$, then $\mathbf{1}_A : Z \to \{0, 1\}$ is continuous (preimage of any subset of $\{0, 1\}$ is one of $\emptyset, A, Z \setminus A, Z$, all open) and nonconstant. Contrapositively, if every discrete-valued map is constant, no nontrivial clopen subset exists, so $Z$ is connected.

> [!note]- Lemma 2: The composition of continuous maps is continuous
> **Statement:** If $f : X \to Y$ and $g : Y \to Z$ are continuous, then $g \circ f : X \to Z$ is continuous.
>
> **Hint:** $(g \circ f)^{-1}(W) = f^{-1}(g^{-1}(W))$.
>
> **Why needed:** It is what lets a discrete map on $f(X)$ be lifted to a discrete map on $X$.
>
> > [!note]- Full proof
> > For any open $W \subseteq Z$, $g^{-1}(W)$ is open in $Y$ by continuity of $g$, and $f^{-1}(g^{-1}(W))$ is open in $X$ by continuity of $f$. But $(g \circ f)^{-1}(W) = f^{-1}(g^{-1}(W))$, so the preimage of every open set under $g \circ f$ is open.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : X \to Y$ be continuous with $X$ connected; consider the image $f(X) \subseteq Y$ with the subspace topology.
>
> Let $d : f(X) \to D$ be a continuous map to a discrete space $D$. By Lemma 2, $d \circ f : X \to D$ is continuous, so it is a discrete-valued map on $X$. By Lemma 1 (using that $X$ is connected), $d \circ f$ is constant. Since $f$ is surjective onto its image $f(X)$, this means $d$ takes the same value on every point of $f(X)$: for any $y \in f(X)$, choose $x \in X$ with $f(x) = y$, and $d(y) = (d \circ f)(x) = $ the constant value.
>
> Hence every continuous map from $f(X)$ to a discrete space is constant. By Lemma 1 applied to $f(X)$, $f(X)$ is connected. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The intermediate value theorem from pure topology.** Given a continuous $f : [a, b] \to \mathbb{R}$ with $f(a) < c < f(b)$, the image $f([a, b])$ is connected (this theorem, applied to the connectedness of $[a, b]$). The connected subsets of $\mathbb{R}$ are exactly the intervals — singletons, open, closed, half-open, half-infinite, and all of $\mathbb{R}$ — so $f([a, b])$ is an interval containing $f(a)$ and $f(b)$, hence containing $c$. The application is nonobvious because the IVT is conventionally proved by a bisection argument; the topological proof reveals it as pure connectedness propagation.

**Winding numbers are locally constant.** For a continuous loop $\gamma : S^1 \to \mathbb{C} \setminus \{0\}$, the winding number $n(\gamma) \in \mathbb{Z}$ is constant on path-components of the space of such loops (with the sup norm topology). The path-component is connected, and the winding number is a continuous map into the discrete space $\mathbb{Z}$, hence constant. This is the topological foundation of the index calculus in **complex analysis**.

**Sign of the determinant on $\mathrm{GL}_n(\mathbb{R})$.** The group $\mathrm{GL}_n(\mathbb{R})$ has two path-components, distinguished by the sign of the determinant. The determinant is continuous to $\mathbb{R} \setminus \{0\}$, which has two components $(-\infty, 0)$ and $(0, \infty)$; by this theorem, $\det$ must map each component of $\mathrm{GL}_n(\mathbb{R})$ to one component of $\mathbb{R} \setminus \{0\}$, hence the sign is constant on each. This is the topological version of the algebraic fact that $\det$ is a group homomorphism with kernel $\mathrm{SL}_n$.

---

# Bridges

- **[[Thm - Continuous Image of a Compact Space]]** — the *exact same propagation phenomenon* but for compactness instead of connectedness. Both theorems express the principle that continuity preserves structural "size" properties of the source. The proofs are nearly identical in form: pull back the relevant structure (open cover for compactness, clopen decomposition for connectedness) via $f$ to get a structure on $X$, exploit the source-side hypothesis, then push forward.

- **[[Thm - Union of Overlapping Connected Sets is Connected]]** — the companion construction theorem. Where this theorem propagates connectedness *along* a continuous map, the overlap theorem *builds* connectedness from smaller connected pieces. Together: build small connected pieces, glue them via overlaps, then propagate via continuity.

- **[[Def - Path-Connected Space]]** — path-connectedness implies connectedness via this theorem applied to each path $\gamma : [0, 1] \to X$ (image of a connected interval is connected) followed by the overlap theorem. So this theorem is half the engine of "path-connected ⇒ connected".

- **The intermediate value theorem** — the canonical corollary. A continuous function on a connected source whose target is $\mathbb{R}$ takes every intermediate value, because the image is a connected subset of $\mathbb{R}$, which is an interval.

---

# Unlocked by This

> [!tip] Fundamental Group *(from Algebraic Topology)*
> Once path-connectedness is in hand (which this theorem feeds into via "path = continuous image of $[0,1]$"), one can talk about *equivalence classes of loops* at a basepoint, modulo homotopy. These form a group, the **fundamental group** $\pi_1(X, x_0)$ — the first algebraic invariant distinguishing topological spaces.

> [!tip] Brouwer Fixed Point Theorem *(from Algebraic Topology)*
> A continuous map $f : D^n \to D^n$ has a fixed point. The proof for $n = 1$ is a direct application of this theorem: $g(x) = f(x) - x$ is continuous on the connected $[-1, 1]$, with $g(-1) \geq 0$ and $g(1) \leq 0$, so by IVT $g$ vanishes. The higher-dimensional case requires the **degree theory** of algebraic topology, but the engine is still the propagation of connectedness/topological invariants via continuity.
