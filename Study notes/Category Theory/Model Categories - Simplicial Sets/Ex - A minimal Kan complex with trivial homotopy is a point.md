---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Minimal Fibration"
  - "Def - Simplicial Homotopy Group"
  - "Def - Kan Complex and the Nerve"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $M$ be a connected [[Def - Minimal Fibration|minimal Kan complex]] (a minimal fibration over the point) all of whose [[Def - Simplicial Homotopy Group|simplicial homotopy groups]] vanish: $\pi_0(M) = \ast$ and $\pi_n(M, x) = 0$ for all $n \ge 1$. Prove that $M$ is isomorphic to the point $\Delta^0$.

(Contrast: a non-minimal contractible Kan complex — for instance $\mathrm{Sing}(\ast)$ enlarged, or any contractible $\mathrm{Sing}(Y)$ with $Y$ contractible — has many simplices in each dimension. Minimality is exactly what collapses a contractible complex down to a point.)

**Recall:**

![[Def - Minimal Fibration#The Definition]]

A [[Def - Kan Complex and the Nerve|Kan complex]] $M$ has $\pi_n(M, x) = 0$ when every [[Def - Simplicial Homotopy Group|spheroid]] (degenerate-boundary $n$-simplex at $x$) is homotopic rel boundary to the degenerate one. More generally, $M$ is **$n$-connected** when every map $\partial\Delta^{k} \to M$ with $k \le n+1$ extends over $\Delta^{k}$.

---

# Convergent Strategy

**Problem class:** This is a *minimisation/rigidity* problem (topic-page Problem-Solving Strategy): we exploit the defining rigidity of a [[Def - Minimal Fibration|minimal]] object — "fibrewise homotopic rel boundary $\Rightarrow$ equal" — to force a strong structural conclusion. The routine is induction on dimension: show that in each dimension the only simplex with a given boundary is the degenerate one, using triviality of homotopy groups to produce a homotopy and minimality to upgrade it to equality.

**Assumption pattern:** The recognisable feature is "minimal Kan complex + vanishing homotopy". Vanishing homotopy gives, for any simplex, a *homotopy* to a degenerate one; minimality converts that homotopy into an *equality*. The interplay — homotopy from connectivity, equality from minimality — is the entire mechanism, and recognising that these two hypotheses are the two halves of one squeeze is the key.

**Theorem routing:** The route is induction on $n$. Base case: $\pi_0 = \ast$ and minimality force a single vertex. Inductive step: given $M$ agrees with $\Delta^0$ through dimension $n-1$, a non-degenerate $n$-simplex would have totally degenerate boundary (by induction), hence be a spheroid; triviality of $\pi_n$ gives a homotopy to the degenerate spheroid; minimality forces equality; so there is no non-degenerate $n$-simplex. Hence $M = \Delta^0$.

**Key decision point:** The crux is realising that, after the inductive hypothesis kills all lower non-degenerate simplices, *every* $n$-simplex has degenerate boundary and so is a spheroid — which is what lets triviality of $\pi_n$ apply. The natural error is to try to use $\pi_n = 0$ on simplices with arbitrary boundary; the inductive collapse of the boundary is what makes the homotopy-group hypothesis bite.

---

# Legal Operations Used

1. **Operation 6 from the topic page (use minimality for rigidity).** The defining property "fibrewise homotopic rel boundary $\Rightarrow$ equal" is invoked at every inductive step to convert a homotopy into an equality.

2. **Operation 1 from the topic page (fill a horn).** Triviality of $\pi_n$ is itself a horn-filling statement: a spheroid is null-homotopic, witnessed by a filled horn, supplying the homotopy that minimality then collapses.

3. **The vanishing of homotopy groups (from [[Def - Simplicial Homotopy Group]]).** $\pi_n = 0$ provides, for each spheroid, a homotopy to the degenerate one — the input minimality consumes.

---

# Hints

> [!note]- Hint 1
> Induct on dimension. Show $M$ has exactly one simplex in each dimension (the degenerate one), which forces $M \cong \Delta^0$.

> [!note]- Hint 2
> Base case: $\pi_0(M) = \ast$ means all vertices are connected by edges. In a *minimal* Kan complex, two vertices joined by an edge homotopic to a degenerate edge must be equal — show $\pi_0 = \ast$ plus minimality gives a single vertex.

> [!note]- Hint 3
> Inductive step: assume $M$ agrees with $\Delta^0$ in dimensions $< n$ (only degenerate simplices). Then any $n$-simplex $\sigma$ has all faces $d_i\sigma$ of dimension $n-1$, hence degenerate, so $\sigma$ is a *spheroid*. Use $\pi_n(M) = 0$.

> [!note]- Hint 4
> $\pi_n(M) = 0$ gives a homotopy rel boundary from $\sigma$ to the degenerate spheroid. Both lie over the same (trivial) base and have the same boundary. What does *minimality* say about two simplices that are homotopic rel boundary over the same base?

> [!note]- Hint 5
> Minimality forces $\sigma =$ (the degenerate spheroid). So $M$ has no non-degenerate $n$-simplex, completing the induction: $M$ has a single non-degenerate simplex (the vertex) and hence $M \cong \Delta^0$.

---

# Solution

Induct on dimension. The vanishing homotopy groups supply, for any spheroid, a homotopy to the degenerate one; minimality upgrades each such homotopy to an equality. Step by step this shows $M$ has only degenerate simplices above dimension $0$ and a single vertex, so $M \cong \Delta^0$.

**Step 1: Base case — a single vertex.**

> [!note]- Derivation
> $\pi_0(M) = \ast$ means $M$ is connected: any two vertices $x, y \in M_0$ are joined by a path, and (since $M$ is Kan) by a single edge $e : x \to y$. Consider the degenerate edge $s_0x : x \to x$. Connectedness with trivial $\pi_0$ structure means the edge $e$ is homotopic rel endpoints to a degenerate edge — but more directly: minimality applied in dimension $1$ says two edges with the same endpoints that are fibrewise homotopic rel boundary are equal. The triviality of $\pi_1$-type data at this level (and connectedness) forces, after identifying homotopic vertices, that $M_0$ has a single element. Fix it as the basepoint $x$; from now on every degenerate simplex is the degeneracy of $x$.

**Step 2: Inductive hypothesis.**

> [!note]- Derivation
> Suppose, for some $n \ge 1$, that $M$ has only degenerate simplices in every dimension $0 < k < n$ — i.e. $M$ agrees with $\Delta^0$ through dimension $n-1$ (one vertex, and only degeneracies above it up to dimension $n-1$). We show the same in dimension $n$.

**Step 3: Every $n$-simplex is a spheroid.**

> [!note]- Derivation
> Let $\sigma \in M_n$. Each face $d_i\sigma$ is an $(n-1)$-simplex, hence by the inductive hypothesis degenerate, equal to $s_0^{(n-1)}x$. So $\sigma$ has totally degenerate boundary: $\sigma$ is a [[Def - Simplicial Homotopy Group|spheroid]] based at $x$.

**Step 4: Triviality of $\pi_n$ plus minimality forces $\sigma$ degenerate.**

> [!note]- Derivation
> Since $\pi_n(M, x) = 0$, the spheroid $\sigma$ is homotopic rel boundary to the degenerate spheroid $\ast = s_0^{(n)}x$: there is an $(n+1)$-simplex $H$ exhibiting $\sigma \sim \ast$ rel boundary. Both $\sigma$ and $\ast$ lie over the same simplex of the base (the point), have the same boundary (the degenerate one), and are fibrewise homotopic rel boundary via $H$. By [[Def - Minimal Fibration|minimality]] of $M$ — two simplices that are $p$-related and fibrewise homotopic rel boundary are equal — we conclude $\sigma = \ast = s_0^{(n)}x$. So *every* $n$-simplex of $M$ is the degenerate one; $M$ has no non-degenerate $n$-simplex.

**Step 5: Conclude.**

> [!note]- Derivation
> By induction, $M$ has exactly one non-degenerate simplex — the vertex $x$ — and every higher simplex is degenerate. A simplicial set with a single non-degenerate simplex, a $0$-simplex, is isomorphic to $\Delta^0$. Hence $M \cong \Delta^0$. (Contrapositively: a contractible Kan complex with more than one simplex in some dimension cannot be minimal — its redundancy is exactly the homotopic-but-unequal simplices minimality forbids.)

> [!note]- Complete formal solution
> Induct on dimension, proving $M$ has only degenerate simplices above dimension $0$ and a single vertex. *Base:* $\pi_0(M) = \ast$ gives connectedness; minimality in dimension $1$ collapses homotopic vertices, leaving one vertex $x$. *Step:* assume $M$ agrees with $\Delta^0$ in dimensions $< n$. Any $\sigma \in M_n$ has faces $d_i\sigma$ of dimension $n-1$, hence degenerate (hypothesis), so $\sigma$ is a [[Def - Simplicial Homotopy Group|spheroid]]. As $\pi_n(M,x) = 0$, $\sigma$ is homotopic rel boundary to the degenerate spheroid $\ast$; both have the same boundary and project to the same base simplex, so by [[Def - Minimal Fibration|minimality]] $\sigma = \ast$. Thus no non-degenerate $n$-simplex exists. By induction $M$ has the single non-degenerate simplex $x$, so $M \cong \Delta^0$. $\quad\blacksquare$

---

# Key Takeaways

**Minimality + vanishing homotopy is a squeeze: connectivity gives a homotopy, minimality gives equality.** The whole proof is the repeated interplay of two hypotheses pulling in the same direction. Triviality of $\pi_n$ says "every spheroid is *homotopic* to the degenerate one"; minimality says "homotopic rel boundary *implies equal*". Composing them gives "every spheroid *equals* the degenerate one", which is the rigidity that collapses $M$. The trigger-reaction to install: *whenever you have a minimal object and a connectivity/vanishing hypothesis, expect to upgrade homotopies to equalities and conclude a strict structural statement.* This is the mechanism behind the uniqueness of minimal models, the simplicial Whitehead theorem, and Quillen's product-preservation proof — all run on "homotopy from connectivity, equality from minimality".

**The inductive collapse of the boundary is what makes the homotopy-group hypothesis applicable.** A subtle but transferable point: $\pi_n = 0$ is a statement about *spheroids* (degenerate boundary), but a generic $n$-simplex has a non-trivial boundary. The induction is essential precisely because it first kills all lower non-degenerate simplices, which forces every $n$-simplex to have degenerate boundary — only then is it a spheroid, and only then does $\pi_n = 0$ bite. The diagnostic: when a homotopy-group hypothesis seems not to apply because boundaries are in the way, induct downward to trivialise the boundary first. This "clear the lower skeleton, then the homotopy hypothesis applies to the top cells" pattern is the skeleton of obstruction theory.

**Minimal models are the simplicial analogue of reduced/canonical forms, and this is why they are unique.** The result here — a contractible minimal Kan complex *is* a point — is the extreme case of the general fact that minimal models have no redundancy and are unique up to isomorphism. It is the homotopy-theoretic analogue of "a free resolution with no superfluous generators is minimal" or "a reduced word is unique". The conceptual payoff is that minimisation turns the floppy notion "same homotopy type" into the rigid notion "isomorphic minimal model", which is why minimal fibrations can be *classified* (by fibre plus fundamental-groupoid action) where general fibrations can only be classified up to fibre homotopy equivalence. Whenever you need a canonical, redundancy-free representative of a homotopy type, the minimal model is it.
