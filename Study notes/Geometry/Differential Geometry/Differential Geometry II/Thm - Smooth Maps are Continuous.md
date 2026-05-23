---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - Continuous Map"
tags: [geometry, differential-geometry]
---

# Notation

$M, N$ are smooth manifolds. $F : M \to N$ is a map. Charts on $M$ are $(U, \varphi)$ with $\varphi : U \to \widetilde U \subseteq \mathbb{R}^m$; charts on $N$ are $(V, \psi)$ with $\psi : V \to \widetilde V \subseteq \mathbb{R}^n$. Chart maps and their inverses are homeomorphisms by definition. The full registry is on [[Differential Geometry II — Smooth Maps and Partitions of Unity]].

---

# Statement

> **Theorem (Smooth Maps are Continuous).** Let $M$ and $N$ be smooth manifolds and let $F : M \to N$ be a smooth map. Then $F$ is continuous.

---

# Motivation

This is the first sanity check on the definition of a smooth map. We have defined smoothness chart-by-chart, demanding only that the coordinate representation $\widehat F = \psi \circ F \circ \varphi^{-1}$ be smooth in the Euclidean sense, together with the chart-containment condition $F(U) \subseteq V$. We have *not* required continuity in the definition. Is continuity automatic?

The answer is yes, and the proof reveals why the chart-containment condition $F(U) \subseteq V$ is in the definition of smoothness. Without it, a counterexample (Lee Problem 2-1) shows that a discontinuous map could satisfy "chart-by-chart smooth", which would be absurd. The containment is precisely the topological hook by which smoothness drags continuity along.

The theorem is conceptually a "type-check": smoothness lives in a refined category ($\mathbf{Man}^\infty$), continuity lives in a coarser category ($\mathbf{Top}$), and one would expect the morphisms of the finer category to be morphisms of the coarser one. This expectation is realized here. The forgetful functor $\mathbf{Man}^\infty \to \mathbf{Top}$ is well-defined.

The theorem is also operationally useful: it lets us invoke continuity-based arguments (preimages of opens are open, compactness of continuous images, etc.) freely on smooth maps, without having to verify continuity separately.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem requires only that $F : M \to N$ be smooth. The skill is recognizing maps that are *secretly* smooth — and therefore secretly continuous, even if continuity is hard to verify directly.

The first source is **a map defined locally by formulas in coordinates**. Property $B$: $F$ is given by explicit formulas $\widehat F(x) = (f_1(x), \ldots, f_n(x))$ in chart coordinates, with each $f_j$ smooth in the Euclidean sense. The bridge: this is exactly the definition of smoothness in coordinates, so $F$ is smooth, hence continuous. *Example:* a polynomial map between affine varieties, when restricted to a chart, is given by polynomials — smooth, hence continuous.

The second source is **a composition of known smooth maps**. Property $B$: $F = G_k \circ G_{k-1} \circ \cdots \circ G_1$ where each $G_i$ is smooth. The bridge: composition of smooth maps is smooth (Exercise 2.7 in Lee, or [[Ex - Composition of Smooth Maps is Smooth]]), so the entire composition is smooth, hence continuous. *Example:* the antipodal map on $S^n$, defined as $x \mapsto -x$ for $x \in S^n \subseteq \mathbb{R}^{n+1}$, is the composition of inclusion $S^n \hookrightarrow \mathbb{R}^{n+1}$, the linear map $-\operatorname{id}$, and the restriction to $S^n$ — all smooth, hence the antipodal map is smooth and continuous.

The third source is **a quotient map between specific manifolds**, when the quotient operation is explicitly smooth in coordinates. Property $B$: $F : M \to M/\sim$ for a smooth equivalence relation $\sim$ that gives $M/\sim$ a smooth structure, with the quotient map smooth by construction. The bridge: by definition of the smooth quotient, the projection is smooth, hence continuous. *Example:* the quotient map $\mathbb{R}^{n+1} \setminus \{0\} \to \mathbb{R}P^n$ is smooth in standard charts (rational functions of $x_i$'s with non-vanishing denominators), hence continuous.

**Targets (Output Amplification)**

The conclusion is "$F$ is continuous". Combined with one further property $D$, this becomes a stronger result $E$.

Combine the conclusion with **compactness of the source**. Property $D$: $M$ is compact. The amplified result $E$: $F(M)$ is compact in $N$ (continuous image of compact is compact), hence closed in $N$ (compact subsets of a Hausdorff space are closed). The combination is non-obvious because compactness of $F(M)$ does not obviously follow from smoothness of $F$ alone — the compactness propagates through the continuity, not the smoothness. *Example:* a smooth map from a compact manifold has closed image; this is the standard tool for proving that a smooth bijection from a compact manifold is a homeomorphism (the inverse is automatically continuous since continuous bijections from compact to Hausdorff are homeomorphisms).

Combine the conclusion with **continuity of the inverse**. Property $D$: $F$ is also bijective. The amplified result $E$: $F$ is a continuous bijection. If additionally $F^{-1}$ is smooth (so $F$ is a diffeomorphism), then $F^{-1}$ is also continuous, and $F$ is a homeomorphism. So diffeomorphisms are automatically homeomorphisms — every smooth-category isomorphism is also a topological isomorphism. *Example:* this is how diffeomorphism-invariant topological invariants (Euler characteristic, fundamental group, homology) become diffeomorphism invariants of smooth manifolds.

Combine the conclusion with **a topological covering space structure**. Property $D$: $F : M \to N$ is locally an injective smooth map. The amplified result $E$: by combining smoothness, continuity, and local injectivity (plus a connectedness hypothesis on $N$), $F$ is a covering space. The continuity hands you the open-set lifting; the smoothness hands you the differential machinery to verify local diffeomorphism. *Example:* the universal cover construction in [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]] uses both layers.

---

# Why Is It True

The intuition: in a chart neighbourhood, the smooth map $F$ factors as

$$F|_U = \psi^{-1} \circ \widehat F \circ \varphi,$$

a composition of three maps: the homeomorphism $\varphi : U \to \widetilde U$, the smooth Euclidean map $\widehat F : \widetilde U \to \widetilde V$, and the inverse homeomorphism $\psi^{-1} : \widetilde V \to V$. Each factor is continuous: $\varphi$ and $\psi^{-1}$ by definition of chart, $\widehat F$ because smooth Euclidean maps are continuous (basic multivariable calculus). The composition of continuous maps is continuous. So $F|_U$ is continuous.

**The mechanism in one line:** $F$ is locally a chart-pulled-back smooth Euclidean map, and smooth Euclidean maps are continuous, so $F$ is locally continuous; continuity is a local property, so $F$ is continuous.

The chart-containment condition $F(U) \subseteq V$ is what makes the factoring work. Without it, $F|_U$ might not map into $V$ at all, and the composition $\psi \circ F \circ \varphi^{-1}$ would not even be well-defined as a map $\widetilde U \to \widetilde V$. The smooth-Euclidean composition $\widehat F = \psi \circ F \circ \varphi^{-1}$ being defined on all of $\widetilde U$ is precisely what the containment guarantees.

So the theorem is *not* a sophisticated topological fact about manifolds; it is a definitional consequence of the chart-containment requirement, which was put into the definition of smoothness specifically to make this theorem true. The depth is in the *definition*, not in the proof.

---

# What Makes This Hard

The proof is genuinely short, and the only non-obvious step is recognizing that the chart-containment $F(U) \subseteq V$ is what makes the local factoring valid. Many students try to prove continuity by appealing to chart-by-chart smoothness without first writing the explicit composition $F|_U = \psi^{-1} \circ \widehat F \circ \varphi$, which causes confusion when the smoothness statement seems disconnected from the continuity statement. The other common error is to confuse "$F$ is continuous in the chart" (which says nothing about $F$ outside the chart) with "$F$ is continuous as a map $M \to N$" — the local-to-global step uses that continuity is a *local* property of maps.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
At each point $p \in M$, write $F$ locally as a composition of three maps: the chart $\varphi$ on $M$, the Euclidean coordinate representation $\widehat F$, and the inverse chart $\psi^{-1}$ on $N$. Each factor is continuous; continuity of $F$ follows locally and propagates globally since continuity is local.

**Subgoal decomposition:**

1. **Pick charts and exhibit the local factoring of $F$.** Given $p \in M$, by smoothness of $F$ at $p$ there exist charts $(U, \varphi)$, $(V, \psi)$ with $p \in U$, $F(p) \in V$, $F(U) \subseteq V$, and $\widehat F = \psi \circ F \circ \varphi^{-1}$ smooth.
   - *Hint:* The chart-containment $F(U) \subseteq V$ is provided by the smoothness definition.
   - *Why needed:* Lets us write $F|_U = \psi^{-1} \circ \widehat F \circ \varphi$, the key factoring.

2. **Verify each factor is continuous.** $\varphi : U \to \varphi(U) \subseteq \mathbb{R}^m$ is a homeomorphism (chart). $\widehat F : \varphi(U) \to \psi(V)$ is smooth, hence continuous (basic multivariable calculus). $\psi^{-1} : \psi(V) \to V$ is the inverse of the homeomorphism $\psi$, hence continuous.
   - *Hint:* Each factor's continuity is a definitional / elementary fact.
   - *Why needed:* Composition of continuous maps is continuous, so $F|_U$ is continuous at $p$.

3. **Continuity is local, hence $F$ is continuous on $M$.** Every $p$ has a neighbourhood $U$ on which $F$ is continuous, and a map continuous at every point is continuous.
   - *Hint:* Use the definition of continuity at a point.
   - *Why needed:* This is the final step.

---

# Lemma Decomposition

> [!note]- Lemma 1: Smooth Euclidean maps are continuous
> **Statement:** Any smooth $G : \widetilde U \to \widetilde V$ between open subsets of Euclidean spaces is continuous.
>
> **Hint:** $G$ being smooth means all partial derivatives of every order exist and are continuous. In particular, $G$ is $C^1$, so $G$ is differentiable, hence continuous (differentiability implies continuity).
>
> **Why needed:** This is the multivariable-calculus base case from which manifold continuity will be lifted.
>
> > [!note]- Full proof
> > $G$ smooth $\Rightarrow$ $G$ is $C^1$ $\Rightarrow$ $G$ is differentiable at every point $\Rightarrow$ $G$ is continuous at every point. The implication "differentiable $\Rightarrow$ continuous" is standard: if $G$ is differentiable at $a$ with derivative $DG_a$, then $G(a + h) = G(a) + DG_a \cdot h + o(|h|)$, so as $h \to 0$, $G(a + h) \to G(a)$.

> [!note]- Lemma 2: Continuity is local
> **Statement:** A map $F : M \to N$ between topological spaces is continuous if and only if every point $p \in M$ has an open neighbourhood $U_p$ such that $F|_{U_p} : U_p \to N$ is continuous.
>
> **Hint:** For the forward direction: restrict $F$ to any subset, the restriction is continuous. For the reverse: take a preimage of any open set $V \subseteq N$, and write it as the union over $p \in F^{-1}(V)$ of $U_p \cap F|_{U_p}^{-1}(V)$.
>
> **Why needed:** Lets us pass from "$F$ continuous in each chart" to "$F$ continuous on $M$".
>
> > [!note]- Full proof
> > *Forward:* if $F$ is continuous on $M$, then for any subset $U_p \subseteq M$, $F|_{U_p}$ is continuous (preimages of opens by restriction are opens in $U_p$ in the subspace topology — automatic).
> >
> > *Reverse:* suppose every $p$ has a neighbourhood $U_p$ on which $F$ is continuous. To show $F$ is continuous, let $V \subseteq N$ be open. We show $F^{-1}(V)$ is open in $M$. For each $p \in F^{-1}(V)$, the set $F|_{U_p}^{-1}(V)$ is open in $U_p$ (by continuity of $F|_{U_p}$), hence open in $M$ (since $U_p$ is open in $M$ and open subsets of open sets are open). Thus
> > $$F^{-1}(V) = \bigcup_{p \in F^{-1}(V)} F|_{U_p}^{-1}(V)$$
> > is a union of opens, hence open.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F : M \to N$ be a smooth map between smooth manifolds, and let $p \in M$.
>
> By the definition of smoothness at $p$ ([[Def - Smooth Map between Manifolds]]), there exist smooth charts $(U, \varphi)$ on $M$ with $p \in U$ and $(V, \psi)$ on $N$ with $F(p) \in V$ such that
> $$F(U) \subseteq V \quad \text{and} \quad \widehat F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \psi(V)$$
> is smooth at $\varphi(p)$.
>
> Since $\varphi : U \to \varphi(U)$ is a homeomorphism (by the definition of a chart), so is $\varphi^{-1}$. The chart $\psi : V \to \psi(V)$ is also a homeomorphism, and so is $\psi^{-1}$. The smooth Euclidean map $\widehat F$ is continuous (Lemma 1).
>
> The containment $F(U) \subseteq V$ lets us write, for any $q \in U$:
> $$F(q) = \psi^{-1}(\widehat F(\varphi(q))),$$
> i.e. $F|_U = \psi^{-1} \circ \widehat F \circ \varphi$ as a map $U \to V$.
>
> This is a composition of continuous maps (homeomorphism $\varphi$, continuous $\widehat F$, homeomorphism $\psi^{-1}$), hence continuous.
>
> So $F$ is continuous on $U$, an open neighbourhood of $p$. Since $p$ was arbitrary, $F$ is continuous at every point. By Lemma 2 (continuity is local), $F$ is continuous on $M$. $\quad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Number theory / algebraic geometry: smooth quotient maps.** The quotient map $\mathbb{R}^{n+1} \setminus \{0\} \to \mathbb{R}P^n$, sending $x \mapsto [x]$, is smooth in standard charts (each homogeneous coordinate function is rational with non-vanishing denominator on its chart's domain). By this theorem, the quotient map is automatically continuous — recovering a topological fact (the quotient topology makes the map continuous) from differential-geometric input.

**Physics: smoothness of physical maps implies continuity.** In general relativity, spacetime is a smooth manifold and physical fields (electromagnetic potential, metric perturbations) are smooth tensor fields. The theorem ensures that any smooth field is automatically continuous — which is the regularity hypothesis needed for the wave equation, the Einstein equations, and other PDE-based formulations to make sense.

**Algebraic topology: smooth maps induce continuous maps on homology.** Singular homology $H_*(M; \mathbb{Z})$ is a functor from continuous maps. The de Rham theorem identifies $H^*_{\mathrm{dR}}(M; \mathbb{R})$ with the singular cohomology $H^*(M; \mathbb{R})$. A smooth map $F : M \to N$ induces $F^* : H^*_{\mathrm{dR}}(N) \to H^*_{\mathrm{dR}}(M)$ via pullback of forms, *and* (via this theorem) $F$ is continuous, so it induces $F^* : H^*(N; \mathbb{R}) \to H^*(M; \mathbb{R})$. The two induced maps agree under the de Rham isomorphism — and the consistency is what makes the de Rham theorem a *natural* isomorphism. See [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]].

---

# Bridges

- **[[Def - Smooth Map between Manifolds]]** — the input. The proof is essentially the unfolding of this definition with the chart-containment condition properly used.

- **[[Def - Continuous Map]]** — the output. The theorem says the smooth-map condition implies the continuous-map condition.

- **Counterexample without chart containment (Lee Problem 2-1)** — drops the chart-containment condition $F(U) \subseteq V$ from the smoothness definition and shows that a discontinuous step function then satisfies the modified "smoothness". This pathology is the reason the containment is in the definition: it is what closes the gap between local smooth-in-coordinates and global continuity. The pathology vanishes the moment containment is required, by exactly the proof above.

- **The forgetful functor $\mathbf{Man}^\infty \to \mathbf{Top}$** — this theorem is the statement that the assignment "smooth manifold $\mapsto$ underlying topological space, smooth map $\mapsto$ same underlying map" is a *well-defined* functor (smooth maps are continuous, so the assignment goes to morphisms in $\mathbf{Top}$). The functor is faithful (different smooth maps with the same underlying continuous map cannot exist — they would differ at some point, where their coordinate representations would differ) but *not* full (there are continuous maps between smooth manifolds that are not smooth, like $|x|$ on $\mathbb{R}$).
