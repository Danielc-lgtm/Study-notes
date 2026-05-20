---
type: theorem
subject: topology
prereqs:
  - "Def - Connected Space"
  - "Def - Topological Space"
tags: [analysis, topology, connectedness]
---

# Notation

$X$ is a topological space (see [[Def - Topological Space]]), $\{Y_\alpha\}_{\alpha \in A}$ is an indexed family of subsets, each equipped with the [[Def - Subspace Topology|subspace topology]] from $X$. A subset $Y \subseteq X$ is **[[Def - Connected Space|connected]]** if it is not the disjoint union of two nonempty relatively open subsets, equivalently if every continuous map $Y \to \{0, 1\}$ (with discrete topology) is constant. The full notation registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Theorem (overlap form).** Let $\{Y_\alpha\}_{\alpha \in A}$ be a family of connected subsets of a topological space $X$, and suppose that *no two of the $Y_\alpha$ are disjoint*: $Y_\alpha \cap Y_\beta \neq \emptyset$ for all $\alpha, \beta \in A$. Then $\bigcup_{\alpha \in A} Y_\alpha$ is connected.

> **Theorem (common-point form).** A weaker hypothesis suffices: if there exists $p \in X$ with $p \in Y_\alpha$ for *every* $\alpha \in A$, then $\bigcup_\alpha Y_\alpha$ is connected.

> **Theorem (chain form).** Even more flexibly: if for any two $\alpha, \beta \in A$ there is a finite chain $\alpha = \alpha_0, \alpha_1, \ldots, \alpha_n = \beta$ such that $Y_{\alpha_i} \cap Y_{\alpha_{i+1}} \neq \emptyset$ for each $i$, then $\bigcup_\alpha Y_\alpha$ is connected.

The strongest hypothesis (pairwise nonempty intersection) is what is used most commonly in the proof of "path-connected implies connected"; the chain form is the most flexible and is what one reaches for when constructing connected components.

---

# Motivation

Connectedness is a global property — it sees the whole space at once. The question this theorem answers is: *how does global connectedness assemble from local connectedness?* The instinct from set theory is that "union" should preserve everything, but it does not preserve connectedness in general: $[0, 1] \cup [2, 3]$ is disconnected even though each piece is connected. Something must couple the pieces, and the minimal coupling is *they share a point* — or, weakly, *they all touch transitively*.

The pragmatic value is this. The cleanest way to prove a complicated space $X$ is connected is to write it as a union of simpler connected pieces sharing a common point or chained by overlaps. A star-shaped region is the union of line segments from a basepoint. A path-connected space is the union of paths through a basepoint. A torus is the union of meridian circles intersecting one longitude. In every case, the global connectedness is *built* from the local connectedness of the pieces via this theorem.

The theorem also drives the very *existence* of [[Def - Connected Components|connected components]]: the relation "$p \sim q$ if both lie in a common connected subset" is an equivalence relation precisely *because* this theorem lets one combine two connected sets through $r \in Y_1 \cap Y_2$ to get a third connected set containing both endpoints. Without this theorem, "the component of $p$" would not even be well-defined as a connected set.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "every $Y_\alpha$ is connected and the family overlaps".

The first disguised source is **path-connectedness via a common basepoint**. Property $B$: $X$ is path-connected, and one fixes a basepoint $p \in X$, then writes $X = \bigcup_{q \in X} \gamma_q([0, 1])$ where $\gamma_q$ is a path from $p$ to $q$. The bridge: each $\gamma_q([0, 1])$ is connected (as the continuous image of the connected interval $[0, 1]$ via [[Thm - Continuous Image of a Connected Space]]), and they all contain $p$, so this theorem applies. *Example:* this is *the* proof that path-connectedness implies connectedness.

The second disguised source is **a chain of connected subsets**. Property $B$: $X = \bigcup_n Y_n$ where each $Y_n$ is connected and $Y_n \cap Y_{n+1} \neq \emptyset$. The bridge: induct using the pairwise overlap form. *Example:* the real line $\mathbb{R} = \bigcup_{n \in \mathbb{Z}} [n, n+1]$ — each $[n, n+1]$ is connected, and $[n, n+1] \cap [n+1, n+2] = \{n+1\} \neq \emptyset$. This proves $\mathbb{R}$ connected once you know intervals are. Same idea: any open star-shaped subset of $\mathbb{R}^n$ is connected; $S^n = (S^n \setminus \{N\}) \cup (S^n \setminus \{S\})$, each homeomorphic to $\mathbb{R}^n$ hence connected, overlapping at the equator (which is nonempty for $n \geq 1$).

The third disguised source is **a connected set together with the closure of one of its points' neighborhoods**. Property $B$: $Y$ is connected and $\overline{Y}$ is its closure; equivalently $Y \subseteq Z \subseteq \overline{Y}$. The bridge: $\overline{Y}$ is the union of $Y$ with limit points; each limit point $q$ has every neighborhood meeting $Y$, so $\{q\} \cup Y$ is "joined" to $Y$ via overlap... actually the cleaner argument is that the closure of a connected set is connected directly. *Example:* the topologist's sine curve $\{(0, y) : y \in [-1, 1]\} \cup \{(x, \sin(1/x)) : x > 0\}$ is the closure of its second piece (a connected continuous image of $(0, \infty)$), hence connected.

**Targets (Output Amplification)**

The conclusion is "$\bigcup_\alpha Y_\alpha$ is connected".

Combine the conclusion with **the fact that the closure of a connected set is connected**. Property $D$: $\bigcup_\alpha Y_\alpha$ has a closure $Z$ with $\bigcup_\alpha Y_\alpha \subseteq Z \subseteq \overline{\bigcup_\alpha Y_\alpha}$. Amplified result $E$: $Z$ is connected. *Example:* the closure of a path-connected set is connected (but not necessarily path-connected — see topologist's sine curve).

Combine the conclusion with **continuity propagation**. Property $D$: there is a continuous $f$ defined on $\bigcup_\alpha Y_\alpha$. Amplified result $E$: $f(\bigcup_\alpha Y_\alpha)$ is connected (by [[Thm - Continuous Image of a Connected Space]]), so $f$'s image is automatically also connected, and we can iterate this construction.

Combine the conclusion with **defining components**. Property $D$: declare $p \sim q$ if both belong to a connected subset. Amplified result $E$: $\sim$ is an equivalence relation whose classes are connected (each is the union of all connected subsets containing a given point, which all share that point). The *components* of $X$ are well-defined as a set partition, and each is automatically a maximal connected subset.

---

# Why Is It True

The reason is the same as for [[Thm - Continuous Image of a Connected Space|continuous-image-of-connected]]: the discrete-valued map formulation of connectedness composes well, not just with continuity, but with restriction. A discrete-valued map $d : \bigcup_\alpha Y_\alpha \to D$ restricts to a discrete-valued map on each $Y_\alpha$. Each restriction is constant (because $Y_\alpha$ is connected). If two of the $Y_\alpha$ overlap at a point $r$, then their two constant values must both equal $d(r)$ — hence the two restrictions agree. So all the restrictions agree, and $d$ is globally constant.

The geometric picture: imagine $d$ as "colouring" each point of $X$ with one of finitely many discrete colours. Connectedness of each $Y_\alpha$ means each piece is uniformly coloured. Overlap at a point forces two pieces to share a colour. Pairwise overlap forces all pieces to share. Chain overlap does the same by transitivity. So the union is uniformly coloured, i.e., $d$ is constant, i.e., the union is connected.

The reason a *common* point form suffices and even a *chain* form suffices is that the colour-sharing argument is *transitive*: if pieces $Y_\alpha$ and $Y_\beta$ share a colour and $Y_\beta$ and $Y_\gamma$ share a colour, then $Y_\alpha$ and $Y_\gamma$ share that same colour. Chains of overlaps propagate colour-equality through the entire family, even without direct overlap between every pair.

Why the theorem *fails* without any coupling: $[0, 1] \cup [2, 3]$ in $\mathbb{R}$. The discrete map sending $[0, 1] \to 0$ and $[2, 3] \to 1$ is well-defined (no shared point to force agreement) and continuous (preimages are clopen in the union, since each piece is open and closed in the union). So the union is disconnected. Some coupling between pieces is essential, and pairwise nonempty intersection is the cleanest sufficient condition.

---

# What Makes This Hard

The non-obvious step is recognizing that *pairwise* overlap (or even chain overlap) is sufficient — not just a single common point. The proof is the same in all three cases because the "common point" is, in spirit, the same colour-forcing mechanism, but the chain form is what is usually needed in applications and beginners often weaken the theorem to "common point" when "pairwise overlap" or "chain" would work. The most common error is to forget that the *discrete-valued maps must be defined on the subspace topology of $Y_\alpha$*, not as restrictions of maps defined elsewhere — which makes no functional difference but trips up readers who try to use clopen subsets of $X$ instead of clopen subsets of $Y_\alpha$.

---

# Rederivation Scaffold

**High-level strategy:**
Use the discrete-valued map form of connectedness. A discrete map on the union, restricted to each $Y_\alpha$, is constant. Overlaps force these constant values to be the same. Hence the global map is constant, hence the union is connected.

**Subgoal decomposition:**

1. **Set up: a discrete-valued map on the union.** Let $d : \bigcup_\alpha Y_\alpha \to D$ be continuous, $D$ discrete.
   - *Hint:* This is the form of "$\bigcup_\alpha Y_\alpha$ is connected" we want to prove — that every such $d$ is constant.
   - *Why needed:* Continuous discrete-valued maps compose with restrictions, which is the leverage.

2. **Each restriction is constant.** For each $\alpha$, $d|_{Y_\alpha} : Y_\alpha \to D$ is continuous (composition of $d$ with inclusion $Y_\alpha \hookrightarrow \bigcup Y_\alpha$). Since $Y_\alpha$ is connected, $d|_{Y_\alpha}$ is constant, with value $c_\alpha$.
   - *Hint:* This is the definition of connectedness applied to $Y_\alpha$.
   - *Why needed:* It reduces the problem to "all $c_\alpha$ are equal".

3. **Overlap forces $c_\alpha = c_\beta$.** For any $r \in Y_\alpha \cap Y_\beta$, $c_\alpha = d(r) = c_\beta$.
   - *Hint:* The values of $d$ at any point are well-defined, regardless of which $Y_\alpha$ contains the point.
   - *Why needed:* It is the only place the hypothesis "no two are disjoint" enters.

4. **Conclude $d$ is constant.** All $c_\alpha$ are equal, so $d$ is constant, so the union is connected.

**Chain form modification:**

3'. **Chain overlap forces $c_\alpha = c_\beta$ transitively.** If $\alpha = \alpha_0, \alpha_1, \ldots, \alpha_n = \beta$ is a chain with $Y_{\alpha_i} \cap Y_{\alpha_{i+1}} \neq \emptyset$, then $c_{\alpha_0} = c_{\alpha_1} = \cdots = c_{\alpha_n}$.

---

# Lemma Decomposition

> [!note]- Lemma 1: A continuous map $d$ on $\bigcup Y_\alpha$ restricts to a continuous map on each $Y_\alpha$
> **Statement:** If $d : Z \to D$ is continuous and $Y \subseteq Z$ with the subspace topology, then $d|_Y : Y \to D$ is continuous.
>
> **Hint:** $(d|_Y)^{-1}(W) = d^{-1}(W) \cap Y$.
>
> **Why needed:** It is the bridge from "$d$ defined on the whole union" to "$d$ constant on each $Y_\alpha$".
>
> > [!note]- Full proof
> > For any open $W \subseteq D$, $(d|_Y)^{-1}(W) = d^{-1}(W) \cap Y$. Since $d^{-1}(W)$ is open in $Z$ by continuity of $d$, its intersection with $Y$ is open in the subspace topology of $Y$.

> [!note]- Lemma 2: Three formulations of overlap yield the same conclusion
> **Statement:** Pairwise overlap, common point, and chain overlap each force a discrete-valued map on $\bigcup Y_\alpha$ to be constant — given that each $Y_\alpha$ is connected.
>
> **Hint:** The argument is transitive in the chain case.
>
> **Why needed:** It shows the three forms of the theorem stand or fall together.
>
> > [!note]- Full proof
> > *Common point form:* If $p \in \bigcap_\alpha Y_\alpha$, then $c_\alpha = d(p)$ for every $\alpha$ (since $d|_{Y_\alpha}$ is constant with value $c_\alpha$, and $p \in Y_\alpha$). All $c_\alpha$ equal $d(p)$, so $d$ is constant on the union.
> >
> > *Pairwise overlap:* If $Y_\alpha \cap Y_\beta \neq \emptyset$ for all $\alpha, \beta$, pick any $r_{\alpha\beta} \in Y_\alpha \cap Y_\beta$ and conclude $c_\alpha = d(r_{\alpha\beta}) = c_\beta$. So all $c_\alpha$ are equal.
> >
> > *Chain form:* If $\alpha = \alpha_0, \ldots, \alpha_n = \beta$ is a chain with $Y_{\alpha_i} \cap Y_{\alpha_{i+1}} \neq \emptyset$, pick $r_i \in Y_{\alpha_i} \cap Y_{\alpha_{i+1}}$ and conclude $c_{\alpha_i} = d(r_i) = c_{\alpha_{i+1}}$. By induction, $c_\alpha = c_\beta$. Since the chain exists for any $\alpha, \beta$, all $c_\alpha$ are equal.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\{Y_\alpha\}_{\alpha \in A}$ be a family of connected subsets of $X$ with $Y_\alpha \cap Y_\beta \neq \emptyset$ for all $\alpha, \beta \in A$, and let $Z = \bigcup_\alpha Y_\alpha$ with the subspace topology.
>
> Let $d : Z \to D$ be a continuous map to a discrete space $D$. We show $d$ is constant, which by the discrete-map characterization of connectedness (see [[Thm - Continuous Image of a Connected Space]], Lemma 1) shows $Z$ is connected.
>
> For each $\alpha$, $d|_{Y_\alpha} : Y_\alpha \to D$ is continuous (Lemma 1). Since $Y_\alpha$ is connected, $d|_{Y_\alpha}$ is constant; call its value $c_\alpha \in D$.
>
> Fix any $\alpha_0 \in A$. For any other $\beta \in A$, the hypothesis gives a point $r \in Y_{\alpha_0} \cap Y_\beta$. Then $c_{\alpha_0} = d(r) = c_\beta$. So $c_\beta = c_{\alpha_0}$ for every $\beta$, and $d$ is constant on $Z$ with value $c_{\alpha_0}$.
>
> Hence every continuous discrete-valued map on $Z$ is constant, so $Z$ is connected. $\blacksquare$
>
> **Chain form.** Same setup; the only modification is that for $\alpha, \beta$ joined by a chain $\alpha = \alpha_0, \ldots, \alpha_n = \beta$, pick $r_i \in Y_{\alpha_i} \cap Y_{\alpha_{i+1}}$ and conclude $c_{\alpha_i} = d(r_i) = c_{\alpha_{i+1}}$ for each $i$; by induction $c_\alpha = c_\beta$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Closure of a connected set.** If $A \subseteq X$ is connected and $A \subseteq B \subseteq \overline{A}$, then $B$ is connected. The standard proof: writing $B = \bigcup_{p \in B} (A \cup \{p\})$ — but more economically, observing that any clopen subset of $B$ meets $A$ on a clopen subset of $A$, hence is empty or all of $A$, and density propagates this to $B$. The connection to this theorem is that $B$ is the union of $A$ with limit points, each of which has every neighborhood intersecting $A$, providing the colour-forcing overlap.

**Path-connected implies connected.** Given path-connected $X$ with basepoint $p$, write $X = \bigcup_{q \in X} \gamma_q([0, 1])$ where $\gamma_q$ is a path from $p$ to $q$. Each $\gamma_q([0, 1])$ is connected by [[Thm - Continuous Image of a Connected Space|continuous image of connected]] applied to the connected interval $[0, 1]$, and all share $p$. By this theorem, $X$ is connected. This is the canonical use, and once it is in hand, every concrete connectedness proof for a path-constructible space (the disk, the sphere $S^n$ for $n \geq 1$, $\mathrm{GL}_n^+(\mathbb{R})$, every convex set) is one line.

**Connectedness of $\mathbb{R}^n$ and $S^n$.** $\mathbb{R}^n = \bigcup_{r > 0} B_r(0)$ — each open ball is convex, hence path-connected, hence connected; all share the origin. By this theorem, $\mathbb{R}^n$ is connected. For $S^n$ with $n \geq 1$: $S^n = (S^n \setminus \{N\}) \cup (S^n \setminus \{S\})$ where $N, S$ are the north and south poles; each is homeomorphic to $\mathbb{R}^n$ (stereographic projection) hence connected; they overlap on $S^n \setminus \{N, S\}$ which is nonempty for $n \geq 1$. By this theorem, $S^n$ is connected.

---

# Bridges

- **[[Thm - Continuous Image of a Connected Space]]** — the complementary engine. Where this theorem builds connectedness from overlap, that one propagates connectedness through continuity. Together they constitute the entire arithmetic of connectedness: build small connected pieces, glue them via overlaps, propagate via continuity. Almost every concrete connectedness proof routes through one or both.

- **[[Def - Connected Components]]** — depends on this theorem for the very *well-definedness* of components. The relation "$p \sim q$ if both lie in a common connected set" is symmetric and reflexive by inspection; transitivity requires this theorem: $p, q \in Y_1$ and $q, r \in Y_2$ with both connected gives $p, r \in Y_1 \cup Y_2$, which is connected by overlap at $q$. Without this theorem, $\sim$ is not an equivalence relation.

- **[[Def - Path-Connected Space]]** — path-connectedness is best understood via this theorem applied to the family of paths through a basepoint.

---

# Unlocked by This

> [!tip] Locally Connected Spaces *(from General Topology)*
> A space is **locally connected** if every point has a neighborhood basis of connected open sets. In a locally connected space, components are open, and "component" and "quasi-component" coincide. The proof uses this theorem to assemble local connected pieces into open components.

> [!tip] Connected Sum of Manifolds *(from Differential Topology)*
> The **connected sum** $M_1 \# M_2$ of two manifolds is built by gluing them along the boundaries of removed disks. The resulting space is connected (when both are): this theorem applied to $M_1 \setminus D$ and $M_2 \setminus D$ glued along the shared sphere boundary. The construction is the foundation of surface classification.
