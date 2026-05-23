---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Universal Cover"
  - "Def - Deck Transformation Group"
  - "Def - Free Group and Free Product"
  - "Thm - Seifert-van Kampen Theorem (Statement)"
tags: [geometry, algebraic-topology, topology, geometric-group-theory]
---

# Problem Statement

Let $X = S^1 \vee S^1$ be the figure-eight (two circles joined at a single point, the **wedge point** $x_0$). Let the two loops be called $a$ and $b$.

(a) Show, using [[Thm - Seifert-van Kampen Theorem (Statement)|Seifert-van Kampen]], that $\pi_1(X, x_0) = F_2 = \langle a, b \rangle$ is the free group on two generators.

(b) Construct the universal cover $\widetilde X$ of $X$ as a topological space. Show that it is the **infinite 4-valent tree** $T_4$: an infinite graph where every vertex has exactly 4 edges incident to it, and there are no cycles.

(c) Show that $T_4$ is the **Cayley graph** of $F_2$ with respect to the standard generating set $\{a, b\}$: vertices are elements of $F_2$, edges connect $g$ to $g \cdot a$, $g \cdot a^{-1}$, $g \cdot b$, $g \cdot b^{-1}$.

(d) Show that the deck group acts on $T_4$ as $F_2$ does on its Cayley graph by left multiplication, confirming $\mathrm{Deck}(T_4 / X) = F_2$.

**Recall:**

The universal cover and its defining properties:

![[Def - Universal Cover#The Definition]]

The deck transformation group:

![[Def - Deck Transformation Group#The Definition]]

The free group $F_2$:

![[Def - Free Group and Free Product#The Definition]]

Seifert-van Kampen:

![[Thm - Seifert-van Kampen Theorem (Statement)#Statement]]

---

# Convergent Strategy

**Problem class:** The "universal cover of a CW complex with free $\pi_1$" computation. This is the canonical example for the figure-eight and a flagship demonstration of the [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]]: when $\pi_1$ is a free group, the universal cover is the corresponding **Cayley graph** of that free group. The geometric structure of the cover (a tree) reflects the algebraic structure of $\pi_1$ (a free group with no relations).

**Assumption pattern:** The figure-eight is a 1-dimensional CW complex with one 0-cell and two 1-cells. By Seifert-van Kampen with $U \cap V$ contractible (small neighbourhood of the wedge point), $\pi_1$ is the free product $\mathbb{Z} \ast \mathbb{Z} = F_2$. The universal cover construction (homotopy classes of paths from $x_0$) produces an explicit space whose elements are *reduced words* in $a, b, a^{-1}, b^{-1}$ — the same as elements of $F_2$. The deck group acts by left multiplication.

**Theorem routing:** [[Thm - Seifert-van Kampen Theorem (Statement)|Seifert-van Kampen]] gives the $\pi_1$ computation. [[Def - Universal Cover|Universal cover construction]] gives the explicit topology. The [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]] confirms that the universal cover corresponds to the trivial subgroup of $F_2$, with deck group equal to all of $F_2$.

**Key decision point:** Recognising that the universal cover is *exactly* the Cayley graph of $F_2$. This identification is not arbitrary — it is forced by the universal property: any simply-connected cover of the figure-eight must be a graph (1-dimensional CW), and any cover with deck group $F_2$ must be the Cayley graph of $F_2$ (with $F_2$ acting by left translation). The graph must be 4-valent because the figure-eight has 4 "directions" at the wedge point (incoming/outgoing for each circle), and the cover preserves this local structure. Being a *tree* (acyclic) is forced by simple-connectedness — a cycle in the cover would project to a non-trivial loop in $X$ that lifts to a closed loop, contradicting universal-cover-ness.

---

# Legal Operations Used

1. **Operation 5 from the topic page (Seifert-van Kampen).** Decompose $X = S^1 \vee S^1$ as $U \cup V$ with $U$ a thickening of the first circle, $V$ a thickening of the second, $U \cap V$ a small neighbourhood of the wedge point (contractible). $\pi_1(X) = \mathbb{Z} \ast \mathbb{Z} = F_2$.

2. **Operation 6 from the topic page (pass to the universal cover).** Construct the universal cover $\widetilde X$ explicitly as the space of homotopy classes of paths from $x_0$. Elements of $\widetilde X$ above $x_0$ correspond bijectively to reduced words in $\{a, b, a^{-1}, b^{-1}\}$ — i.e., to elements of $F_2$.

3. **Operation 8 from the topic page (exploit deck-transformation symmetry).** The deck group acts on $\widetilde X$ by left multiplication on words; this matches the Cayley graph structure of $F_2$ where vertices are group elements and edges record right multiplication by generators.

---

# Hints

> [!note]- Hint 1
> First compute $\pi_1(X)$ via Seifert-van Kampen. Take $U$ = thickening of one circle, $V$ = thickening of the other. The intersection $U \cap V$ is a small star around the wedge point, contractible.

> [!note]- Hint 2
> For the universal cover: any simply-connected cover of a 1-dimensional CW complex is a 1-dimensional CW complex (loops would project to non-trivial loops in $X$, contradicting simple-connectedness — but only the universal cover has *trivial* $\pi_1$, so it must be a tree).

> [!note]- Hint 3
> What is the local picture of $\widetilde X$? Around each vertex, there must be the same 4 edges as around the wedge point of $X$: outgoing/incoming for the $a$-loop, outgoing/incoming for the $b$-loop. So $\widetilde X$ is 4-valent.

> [!note]- Hint 4
> Construct $\widetilde X$ explicitly: pick a base point $\tilde x_0$ in the fibre $p^{-1}(x_0)$; the other points in the fibre correspond to reduced words in $\{a^{\pm 1}, b^{\pm 1}\}$ (paths from $x_0$ to $x_0$ in $X$ up to homotopy). Each edge in $\widetilde X$ corresponds to a single generator multiplication.

---

# Solution

**Plan:** Three parts. (a) Compute $\pi_1(X) = F_2$ via Seifert-van Kampen. (b) Explicitly construct $\widetilde X$ as a 4-valent tree by tracking lifts of paths. (c) Identify $\widetilde X$ with the Cayley graph of $F_2$ by matching vertices to group elements and edges to generator multiplications.

**Step 1: $\pi_1(X) = F_2 = \langle a, b \rangle$.**

> [!note]- Derivation
> Let $X = S^1_a \vee S^1_b$ with the wedge point $x_0$. Define $U := X \setminus \{p_b\}$ where $p_b$ is an interior point of $S^1_b$ (the "south pole" of the $b$-circle, on the far side from the wedge point). Then $U$ deformation-retracts to $S^1_a$ (collapse the punctured $b$-circle to a point, which is contractible). Similarly $V := X \setminus \{p_a\}$ deformation-retracts to $S^1_b$.
>
> $U \cap V = X \setminus \{p_a, p_b\}$ deformation-retracts to the wedge point $\{x_0\}$ (collapse both punctured circles to a point each, then join). So $U \cap V$ is contractible: $\pi_1(U \cap V, x_0) = 0$.
>
> By [[Thm - Seifert-van Kampen Theorem (Statement)|Seifert-van Kampen]]: $\pi_1(X, x_0) = \pi_1(U) \ast_{\pi_1(U \cap V)} \pi_1(V) = \pi_1(S^1_a) \ast_{0} \pi_1(S^1_b) = \mathbb{Z} \ast \mathbb{Z} = F_2$. The generator of $\pi_1(S^1_a) = \mathbb{Z}$ becomes the free generator $a$; similarly for $b$.

**Step 2: Construct $\widetilde X$ as a 4-valent tree.**

> [!note]- Derivation
> The universal cover construction (from [[Def - Universal Cover]]) gives $\widetilde X$ as the space of pairs $(p, [\gamma])$ where $p \in X$ and $\gamma$ is a path from $x_0$ to $p$ up to homotopy rel endpoints.
>
> Above the wedge point $x_0$, the fibre $p^{-1}(x_0)$ consists of homotopy classes of *loops* at $x_0$ — that is, elements of $\pi_1(X, x_0) = F_2$. So the fibre over $x_0$ is in canonical bijection with $F_2$.
>
> What does $\widetilde X$ look like locally? Each point $\tilde p \in \widetilde X$ has a neighbourhood mapped homeomorphically by $p$ to a small neighbourhood of $p(\tilde p)$ in $X$. For a point above $x_0$: the wedge point in $X$ has a neighbourhood that looks like a "$+$"-shape (two crossing arcs from the two circles); this lifts to a "$+$"-shape neighbourhood of each fibre point in $\widetilde X$. So each fibre point has *4 edges* emanating from it — corresponding to multiplication by $a$, $a^{-1}$, $b$, $b^{-1}$.
>
> The space $\widetilde X$ is therefore a graph (1-dimensional CW complex) where each vertex (= a point above $x_0$ = an element of $F_2$) is 4-valent, and the edges between vertices correspond to traversing one of the four generators.
>
> *Why is $\widetilde X$ a tree (no cycles)?* Because $\widetilde X$ is simply connected. A cycle in $\widetilde X$ would be a non-trivial loop, contradicting $\pi_1(\widetilde X) = 0$. So $\widetilde X$ is an infinite tree: connected (path-connected, by definition of universal cover) and acyclic.
>
> Conclusion: $\widetilde X$ is the **infinite 4-valent tree** $T_4$, with vertices canonically labelled by elements of $F_2$ and edges corresponding to generator multiplications.

**Step 3: Identify $\widetilde X$ with the Cayley graph of $F_2$.**

> [!note]- Derivation
> The **Cayley graph** of a group $G$ with generating set $S$ has vertices $G$ and edges $\{(g, gs) : g \in G, s \in S\}$. For $G = F_2$ and $S = \{a, b\}$ (so $S \cup S^{-1} = \{a, a^{-1}, b, b^{-1}\}$), each vertex has 4 edges: $g$ connects to $ga$, $ga^{-1}$, $gb$, $gb^{-1}$.
>
> The Cayley graph of $F_2$ is exactly the infinite 4-valent tree $T_4$, with vertices labelled by reduced words in $\{a^{\pm 1}, b^{\pm 1}\}$ — i.e., elements of $F_2$. It is a tree because $F_2$ is free (no relations), so no non-trivial reduced word equals the identity, hence no closed loop.
>
> Comparing with the construction in Step 2: the universal cover $\widetilde X$ of the figure-eight has vertices in bijection with $F_2$ (via fibre identification) and 4 edges per vertex (one per generator $\pm 1$). The edges correspond exactly to multiplication by a generator: the edge from $g$ (corresponding to the loop $\gamma_g$) to $g \cdot a$ corresponds to extending $\gamma_g$ by the $a$-loop, giving a new homotopy class $\gamma_g \cdot a$.
>
> So $\widetilde X$ is *identical* to the Cayley graph of $F_2$ with generating set $\{a, b\}$: same vertex set, same edge structure.

**Step 4: Deck group acts as $F_2$ by left multiplication.**

> [!note]- Derivation
> The deck group $\mathrm{Deck}(\widetilde X / X)$ acts on $\widetilde X$ by self-homeomorphisms commuting with the projection. On the fibre $p^{-1}(x_0) = F_2$ (vertices of $\widetilde X$), the deck action is by left multiplication: an element $g \in \pi_1(X) = F_2$ corresponds to the deck transformation that sends the vertex labelled $w$ to the vertex labelled $gw$.
>
> This is the standard left action of $F_2$ on its Cayley graph: vertex labelled $w$ goes to vertex labelled $gw$, and edges go to edges (since the edge from $w$ to $w \cdot s$ goes to the edge from $gw$ to $gws = (gw) \cdot s$, which is the corresponding edge in the Cayley graph).
>
> The action is free (a non-trivial $g$ moves every vertex, since multiplication by $g$ is injective and $gw \neq w$ unless $g = 1$) and transitive on the fibre (every vertex $w$ is reached from $1$ by left-multiplication by $w$). So $\mathrm{Deck}(\widetilde X / X) = F_2$, in agreement with the Galois correspondence (the universal cover's deck group is $\pi_1$).

> [!note]- Complete formal solution
> **Theorem.** Let $X = S^1 \vee S^1$ be the figure-eight. Then:
>
> 1. $\pi_1(X, x_0) = F_2 = \langle a, b \rangle$, the free group on two generators (where $a, b$ are the homotopy classes of the two circles).
>
> 2. The universal cover of $X$ is the infinite 4-valent tree $T_4$, which is the Cayley graph of $F_2$ with respect to the generating set $\{a, b\}$.
>
> 3. The deck group $\mathrm{Deck}(T_4 / X)$ is $F_2$ acting by left multiplication on vertices.
>
> *Proof.*
>
> **Part 1.** Apply Seifert-van Kampen with $U$ = $X$ minus an interior point of the $b$-circle, $V$ = $X$ minus an interior point of the $a$-circle, $U \cap V$ = $X$ minus two points (deformation-retracts to wedge point, contractible). $\pi_1(U) = \pi_1(V) = \mathbb{Z}$; $\pi_1(U \cap V) = 0$. So $\pi_1(X) = \mathbb{Z} \ast_0 \mathbb{Z} = \mathbb{Z} \ast \mathbb{Z} = F_2$.
>
> **Part 2.** By the universal cover construction, $\widetilde X$ exists (figure-eight is path-connected, locally path-connected, semi-locally simply connected — verify by inspection of local neighbourhoods). $\widetilde X$ has a graph structure: above each open arc of a circle in $X$, the cover has disjoint open arcs (it is a covering); above the wedge point, the cover has a discrete fibre, each of whose points has a 4-valent local structure (inherited from the wedge). So $\widetilde X$ is a 4-valent graph.
>
> $\widetilde X$ is simply connected by definition (universal cover), hence contains no non-trivial loops, hence is a tree. It is connected (by connectedness of $X$ and definition of universal cover) and 4-valent at every vertex. The only such graph (up to graph isomorphism) is the infinite 4-valent tree $T_4$.
>
> *Identification with Cayley graph:* the fibre $p^{-1}(x_0)$ corresponds to $\pi_1(X) = F_2$ canonically. Edges connect $g$ to $g \cdot s$ for $s \in \{a^{\pm 1}, b^{\pm 1}\}$. This matches the Cayley graph definition.
>
> **Part 3.** The deck group acts on $T_4$ by graph automorphisms commuting with the projection to $X$. On the vertex set $F_2$, the action is left multiplication (an element $g$ of $\pi_1$ corresponds to the deck transformation $w \mapsto gw$). This action is free and transitive on each fibre (free: $gw = w \Rightarrow g = 1$; transitive: from $1$ to $w$ via left-multiplication by $w$). So $\mathrm{Deck}(T_4 / X) = F_2$, confirming the Galois correspondence ($\pi_1$ = deck group of universal cover).
>
> $\qquad\blacksquare$

> [!warning] Illegal but tempting alternative route: "$\widetilde X$ is some known surface"
> One might try to identify $\widetilde X$ with a familiar surface — perhaps $\mathbb{R}^2$, perhaps the upper half-plane. This is wrong: $\widetilde X$ is *not a surface* (no 2-dimensional structure), it is a 1-dimensional graph. The wedge of two circles is itself 1-dimensional, and covering maps preserve dimension. The tree $T_4$ is *the* universal cover, with a very specific combinatorial structure. The general lesson: dimension of the cover = dimension of the base, even for "wild" covers like infinite trees.

---

# Key Takeaways

**Universal covers of 1-dimensional CW complexes are trees, and Cayley graphs are the natural picture.** For any graph (1-dimensional CW complex) $X$, the fundamental group $\pi_1(X)$ is free (a deep theorem: the Nielsen-Schreier theorem), and the universal cover is the Cayley graph of $\pi_1(X)$ with respect to a generating set determined by a maximal tree of $X$. The trigger condition is: a graph $X$ → free $\pi_1$ → universal cover is the Cayley graph. The transferable diagnostic: whenever you have a 1-dimensional CW complex, the universal cover is a tree, and the tree's structure encodes the free generators of $\pi_1$ directly. The figure-eight is the canonical 2-generator case; an $n$-rose (wedge of $n$ circles) has universal cover the infinite $2n$-valent tree, $\pi_1 = F_n$.

**The Galois correspondence is most vivid for free groups, where subgroups are trees and intermediate covers are quotient trees.** The lattice of subgroups of $F_2$ is enormous (subgroups of finite index alone are infinitely many, and they have arbitrarily high rank — every finite-rank free group is a subgroup of $F_2$), but each subgroup corresponds to a specific connected cover of the figure-eight, and that cover is a sub-tree of $T_4$ modded out by the subgroup's action. The trigger condition is: when $\pi_1$ is free, the cover lattice is the *subgroup lattice* of the free group, and the geometry of intermediate covers is the geometry of those subgroup quotients. This unlocks computing covers of any graph as quotients of trees by subgroups of free groups.

**Cayley graphs are the bridge from algebra to geometry for groups.** The identification of $\widetilde X$ with the Cayley graph of $F_2$ is one instance of a much larger principle: every group $G$ with a generating set $S$ has a Cayley graph $\mathrm{Cay}(G, S)$, and the geometry of this graph (its growth, its quasi-isometry type, its Gromov hyperbolicity, its ends) is a $G$-invariant called the **geometric structure** of $G$. For $F_n$, the Cayley graph is an infinite tree, which is the prototype of a Gromov-hyperbolic graph (negatively curved at infinity). For $\mathbb{Z}^n$, the Cayley graph is the integer lattice, which is Euclidean and not hyperbolic. **Geometric group theory** is the systematic study of groups via the geometry of their Cayley graphs, and the universal cover of a CW complex with $\pi_1 = G$ is essentially the geometric realisation of $\mathrm{Cay}(G, S)$ as a CW complex.

**Bass-Serre theory: the algebraic structure of groups acting on trees.** The action of $F_2$ on its Cayley tree $T_4$ is the prototype for **Bass-Serre theory**: a group $G$ acting on a tree without inversions, with the structure of the action encoded in a "graph of groups." Conversely, the fundamental group of any graph of groups acts on a tree, and the basic building blocks are *free products* (action with two orbits of vertices and one orbit of edges, edge stabilisers trivial), *amalgamated free products* (similar but edge stabilisers non-trivial), and **HNN extensions**. So this exercise is also a window into Bass-Serre theory, which generalises the Seifert-van Kampen theorem to the categorical statement "the fundamental group commutes with graphs of groups." See [[Def - Free Group and Free Product]].
