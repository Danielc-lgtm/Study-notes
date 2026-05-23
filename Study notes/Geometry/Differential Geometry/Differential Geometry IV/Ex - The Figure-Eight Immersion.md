---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Immersion, Submersion, and Embedding"
  - "Def - Embedded Submanifold"
  - "Def - Immersed Submanifold"
  - "Def - Subspace Topology"
tags: [geometry, differential-geometry]
---

# Problem Statement

Consider the **figure-eight curve**, the image of $\beta : (-\pi, \pi) \to \mathbb{R}^2$ defined by
$$\beta(t) = (\sin 2t, \sin t).$$

(a) Show that $\beta$ is an **injective smooth immersion**.

(b) Show that the image $S = \beta((-\pi, \pi)) \subseteq \mathbb{R}^2$ is *not* an embedded submanifold of $\mathbb{R}^2$. In particular, $\beta$ is not a smooth embedding.

(c) Show that $S$, equipped with the topology and smooth structure that make $\beta$ a diffeomorphism onto $S$ (i.e., the pulled-back topology from $(-\pi, \pi)$), is an **immersed submanifold** of $\mathbb{R}^2$ diffeomorphic to $(-\pi, \pi) \cong \mathbb{R}$.

(d) Verify that the immersed-submanifold structure on $S$ from part (c) is *not* compatible with the subspace topology from $\mathbb{R}^2$: the two topologies disagree.

This is the canonical counterexample showing that injective smooth immersions are not always embeddings. It is the simplest illustration of the [[Def - Immersed Submanifold|immersed-but-not-embedded]] phenomenon and a key example in the foundations of submanifold theory.

**Recall:**

An **immersion** has injective differential at every point; an **embedding** is an immersion that is also a topological embedding (homeomorphism onto image with the subspace topology). For [[Def - Immersion, Submersion, and Embedding|the precise definitions]], see the topic page.

The image of an embedding is an [[Def - Embedded Submanifold|embedded submanifold]] of the target; the image of an injective immersion (with the pulled-back topology) is an [[Def - Immersed Submanifold|immersed submanifold]] of the target. The two notions coincide when the parametrising map is also a topological embedding.

---

# Convergent Strategy

**Problem class:** This is a multi-part counterexample exercise: prove the parametrisation is an immersion, prove the image is not an embedded submanifold, and exhibit an immersed-submanifold structure for the image. The exercise tests the distinction between the three layers of structure (smooth-as-map, smooth immersion, smooth embedding) and shows that injection is not sufficient for embedding.

**Assumption pattern:** The map $\beta : (-\pi, \pi) \to \mathbb{R}^2$ is a smooth parametrisation of a curve. Smoothness is automatic from the formula; injectivity requires a computation; immersion requires the velocity to be nonvanishing. The failure of embedding comes from the *boundary behaviour*: as $t \to \pm\pi$, the image converges to the origin $(0,0)$, which is *also* in the image (at $t = 0$). So the subspace topology of the image has the origin as a limit of two non-converging-in-domain sequences.

**Theorem routing:** Three independent verifications:
1. Injectivity of $\beta$: trigonometric identities + careful case analysis.
2. Non-vanishing of $\beta'$: direct computation of the velocity vector.
3. Non-embedding: exhibit the failing sequence (domain points $t_n \to \pm\pi$ with images converging to a point not at the boundary).

For the immersed-submanifold structure: pull the topology of $(-\pi, \pi)$ back to $S$ via $\beta^{-1}$, defined as a set-theoretic inverse. With this topology, $S$ is homeomorphic to $\mathbb{R}$.

**Key decision point:** The crucial step is producing the right *failing sequences*. The two natural failing sequences are $t_n^- = -\pi + 1/n$ and $t_n^+ = \pi - 1/n$, both with images converging to $(0,0)$ (the crossing point of the figure-eight). The two sequences correspond to "approaching the crossing from the lower-left lobe" versus "approaching from the upper-right lobe" — in the subspace topology, both converge to the crossing, but in the domain topology, they converge to opposite ends and have no common limit.

---

# Legal Operations Used

1. **Operation 1 (compute the differential in coordinates):** computing $\beta'(t) = (2\cos 2t, \cos t)$ and verifying it never vanishes.

2. **The contrapositive of operation 6 (compactness criterion):** the failing case has non-compact domain. The compact-domain criterion ([[Def - Immersion, Submersion, and Embedding|Proposition 4.22(c)]]) would force $\beta$ to be an embedding if $(-\pi, \pi)$ were compact, but it's not — and the figure-eight phenomenon is exactly the obstruction.

---

# Hints

> [!note]- Hint 1
> Visualise the figure-eight: as $t$ ranges from $-\pi$ to $\pi$, the curve traces out a "$\infty$" shape (or rotated figure-eight) with the crossing at the origin. As $t \to 0$ from either side, the curve passes through the origin. As $t \to \pm \pi$, the curve again approaches the origin (sketch the trigonometry to see this).

> [!note]- Hint 2
> For injectivity, suppose $\beta(t_1) = \beta(t_2)$ with $t_1, t_2 \in (-\pi, \pi)$. From $\sin t_1 = \sin t_2$, deduce $t_1 = t_2$ or $t_1 + t_2 = \pi$. Use $\sin 2t_1 = \sin 2t_2$ to rule out the second case (case analysis).

> [!note]- Hint 3
> For immersion, compute $\beta'(t) = (2\cos 2t, \cos t)$. Verify both components do not vanish simultaneously for any $t \in (-\pi, \pi)$.

> [!note]- Hint 4
> For non-embedding, find a sequence $t_n$ in $(-\pi, \pi)$ with $t_n \not\to t_0$ for any $t_0 \in (-\pi, \pi)$, but $\beta(t_n) \to \beta(t_0)$ for some $t_0$. The natural choice: $t_n \to \pi$ (or $-\pi$).

> [!note]- Hint 5
> For the immersed-submanifold structure: define a topology on the image $S$ by declaring $U \subseteq S$ open iff $\beta^{-1}(U) \subseteq (-\pi, \pi)$ is open. With this topology, $\beta : (-\pi, \pi) \to S$ is a homeomorphism, hence a diffeomorphism after declaring $\beta$ to be a smooth chart.

---

# Solution

The proof breaks into four parts. (a) Verify $\beta$ is an injective smooth immersion. (b) Show the image is not an embedded submanifold. (c) Exhibit the immersed-submanifold structure on the image. (d) Verify the immersed structure's topology disagrees with the subspace topology.

**Step (a): $\beta$ is an injective smooth immersion.**

> [!note]- Derivation
> *Smoothness:* both components $\sin 2t$ and $\sin t$ are smooth in $t$, so $\beta$ is smooth.
>
> *Injectivity:* Suppose $\beta(t_1) = \beta(t_2)$ for $t_1, t_2 \in (-\pi, \pi)$. Then $\sin t_1 = \sin t_2$ and $\sin 2t_1 = \sin 2t_2$.
>
> *Case 1: $t_1 = t_2$.* Done.
>
> *Case 2: $t_1 \neq t_2$ but $\sin t_1 = \sin t_2$.* Then $t_1 + t_2 = \pi$ (mod $2\pi$), since $\sin$ takes equal values at $\theta$ and $\pi - \theta$. Both $t_1, t_2 \in (-\pi, \pi)$, so $t_1 + t_2 \in (-2\pi, 2\pi)$, allowing $t_1 + t_2 \in \{-\pi, \pi\}$. If $t_1 + t_2 = \pi$, then $2 t_2 = 2\pi - 2 t_1$, so $\sin 2 t_2 = \sin(2\pi - 2t_1) = -\sin 2t_1$. Combined with $\sin 2t_1 = \sin 2t_2$, this gives $\sin 2t_1 = -\sin 2t_1$, i.e., $\sin 2t_1 = 0$, hence $2t_1 \in \pi\mathbb{Z}$, i.e., $t_1 \in \{0, \pm\pi/2, \pm\pi, \dots\}$. Since $t_1 \in (-\pi, \pi)$, $t_1 \in \{0, \pi/2, -\pi/2\}$. Checking each:
> - $t_1 = 0$: then $t_2 = \pi$, outside the domain. Contradiction.
> - $t_1 = \pi/2$: then $t_2 = \pi/2 = t_1$. Case 1.
> - $t_1 = -\pi/2$: then $t_2 = 3\pi/2$, outside the domain. Contradiction.
>
> If $t_1 + t_2 = -\pi$, by symmetry (swap signs), the same conclusions apply.
>
> So in all cases $t_1 = t_2$, proving injectivity.
>
> *Immersion:* The velocity vector is
> $$\beta'(t) = (2\cos 2t, \cos t).$$
> This vanishes iff $\cos 2t = 0$ and $\cos t = 0$ simultaneously. $\cos t = 0$ iff $t = \pm\pi/2 + k\pi$; restricted to $(-\pi, \pi)$, $t \in \{\pi/2, -\pi/2\}$. At $t = \pi/2$, $\cos 2t = \cos \pi = -1 \neq 0$. At $t = -\pi/2$, $\cos 2t = \cos(-\pi) = -1 \neq 0$. So $\beta'(t)$ never vanishes on $(-\pi, \pi)$, and $\beta$ is a smooth immersion.

**Step (b): The image $S = \beta((-\pi, \pi))$ is not an embedded submanifold of $\mathbb{R}^2$.**

> [!note]- Derivation
> If $S$ were a $1$-dimensional embedded submanifold of $\mathbb{R}^2$, every point of $S$ would have a slice chart making $S$ locally a coordinate line. Look at the crossing point $(0, 0) = \beta(0)$ in $S$.
>
> Approach this point along the parametrisation as $t \to 0$: $\beta(t) \to (0, 0)$ smoothly along the tangent $(\beta'(0)) = (2, 1)$ (so the "first branch" passes through $(0,0)$ tangent to $(2, 1)$). But $(0, 0)$ is *also* a limit point of $S$ approached as $t \to \pm\pi$:
> $$\beta(\pm\pi - 1/n) = (\sin(\mp 2/n), \sin(\pm\pi - 1/n)) = (\sin(\mp 2/n), \mp\sin(1/n)) \to (0, 0)$$
> with tangent direction (computed by taking derivative at $t = \pm\pi$ formally, or just looking at the leading terms) $\beta'(\pm\pi) = (2\cos(\pm 2\pi), \cos(\pm\pi)) = (2, -1)$. So a "second branch" passes through $(0, 0)$ tangent to $(2, -1)$.
>
> In the subspace topology of $\mathbb{R}^2$, the crossing point $(0, 0) \in S$ has neighbourhoods that include pieces of *both* branches — but the two branches have different tangent directions $(2, 1)$ and $(2, -1)$, which are linearly independent. So any small ball around $(0, 0)$ intersected with $S$ contains points from two distinct tangent lines, meaning $S$ near $(0, 0)$ has a "two-tangent-line" structure — not the "one-tangent-line" structure of a smooth $1$-submanifold.
>
> More precisely: a $1$-submanifold has a unique tangent line at each point. If $S$ were a $1$-submanifold of $\mathbb{R}^2$, $T_{(0,0)} S$ would be a $1$-dimensional subspace of $\mathbb{R}^2$. But sequences in $S$ from the two branches have velocities approaching $(2, 1)$ and $(2, -1)$ respectively, both of which would have to be in $T_{(0,0)} S$ — forcing $T_{(0,0)} S$ to contain both directions, hence have dimension $\geq 2$. Contradiction. So $S$ is not an embedded $1$-submanifold of $\mathbb{R}^2$.

**Step (c): The image $S$ admits an immersed-submanifold structure.**

> [!note]- Derivation
> Define a topology $\tau$ on $S$ by declaring $U \subseteq S$ open iff $\beta^{-1}(U) \subseteq (-\pi, \pi)$ is open. (Note: this *defines* a topology because $\beta$ is injective, so $\beta^{-1}$ is a well-defined function from $S$ to $(-\pi, \pi)$, and the preimage of an open set under any function is open in the topology pulled back.) With this topology, $(S, \tau)$ is homeomorphic to $(-\pi, \pi)$ via $\beta$ (now considered as a bijection $\beta : (-\pi, \pi) \to S$, which is a homeomorphism by construction).
>
> Equip $S$ with a smooth structure by declaring the single chart $(\beta : (-\pi, \pi) \to S, \beta^{-1})$ to be smooth. With this smooth structure, $S$ is a smooth $1$-manifold, and $\beta : (-\pi, \pi) \to S$ is a diffeomorphism.
>
> The inclusion $\iota : (S, \tau) \to \mathbb{R}^2$ factors as $\iota = \beta \circ \beta^{-1}$ (interpreting $\beta^{-1}$ as the inverse of $\beta : (-\pi, \pi) \to S$). Since $\beta : (-\pi, \pi) \to \mathbb{R}^2$ is a smooth immersion (part (a)), and $\beta^{-1} : S \to (-\pi, \pi)$ is a diffeomorphism (by construction), the composition $\iota$ is a smooth immersion from $S$ to $\mathbb{R}^2$.
>
> Hence $(S, \tau)$ with this smooth structure is an immersed submanifold of $\mathbb{R}^2$, diffeomorphic to $(-\pi, \pi) \cong \mathbb{R}$.

**Step (d): The topology $\tau$ disagrees with the subspace topology from $\mathbb{R}^2$.**

> [!note]- Derivation
> Consider the sequence $t_n = \pi - 1/n$ in $(-\pi, \pi)$ and its image $\beta(t_n) \in S$. As shown in part (b), $\beta(t_n) \to (0, 0)$ in the subspace topology of $\mathbb{R}^2$, where $(0, 0) = \beta(0) \in S$.
>
> In the topology $\tau$ (the pulled-back topology from $(-\pi, \pi)$), $\beta(t_n) \to \beta(t_\infty)$ would require $t_n \to t_\infty$ in $(-\pi, \pi)$ — but $t_n \to \pi \notin (-\pi, \pi)$, so $t_n$ does not converge in $(-\pi, \pi)$, hence $\beta(t_n)$ does not converge in $(S, \tau)$.
>
> So $\beta(t_n) \to (0, 0)$ in the subspace topology but $\beta(t_n)$ does *not* converge in $\tau$. Hence $\tau \neq $ subspace topology. The two topologies disagree, and $\iota : (S, \tau) \to \mathbb{R}^2$ is not a topological embedding.

> [!note]- Complete formal solution
>
> **(a) $\beta$ is an injective smooth immersion.**
>
> Smoothness: clear from the formula. Injectivity: from $\sin t_1 = \sin t_2$ and $\sin 2t_1 = \sin 2t_2$, case analysis (Case 1: $t_1 = t_2$; Case 2: $t_1 + t_2 = \pm\pi$, which forces $t_1 \in \{0, \pm\pi/2\}$ — only $t_1 = \pm\pi/2$ gives $t_2$ in domain, and that gives $t_1 = t_2$). Immersion: $\beta'(t) = (2\cos 2t, \cos t)$, which vanishes nowhere on $(-\pi, \pi)$.
>
> **(b) $S = \beta((-\pi, \pi))$ is not embedded.**
>
> At $(0, 0) \in S$, sequences from $t \to 0$ and $t \to \pm\pi$ both converge to $(0, 0)$ in $\mathbb{R}^2$, with limiting tangent directions $(2, 1)$ and $(2, -1)$ respectively — linearly independent. A $1$-submanifold has a unique tangent line at each point, contradiction.
>
> **(c) The pulled-back topology makes $S$ an immersed submanifold.**
>
> Define $\tau$ on $S$ by $U \in \tau$ iff $\beta^{-1}(U)$ open in $(-\pi, \pi)$. Then $\beta : (-\pi, \pi) \to (S, \tau)$ is a homeomorphism by construction. Equip $S$ with the smooth structure of a single chart $\beta^{-1}$, making $(S, \tau)$ a smooth manifold diffeomorphic to $(-\pi, \pi)$. The inclusion $\iota : (S, \tau) \to \mathbb{R}^2$ is smooth (it factors through $\beta : (-\pi, \pi) \to \mathbb{R}^2$ which is smooth) and an immersion (the differential at any $p \in S$ is the velocity of $\beta$ at $\beta^{-1}(p)$, which is nonzero).
>
> **(d) $\tau$ disagrees with the subspace topology.**
>
> The sequence $\beta(\pi - 1/n) \to (0, 0)$ in $\mathbb{R}^2$ but not in $\tau$: in $\tau$, convergence requires $\pi - 1/n \to t_\infty \in (-\pi, \pi)$, but $\pi - 1/n \to \pi$, outside the domain.
>
> $\qquad\blacksquare$

---

# Key Takeaways

**The figure-eight is the canonical injective-immersion-non-embedding.** This is the single most-referenced counterexample in submanifold theory. Memorise it: $\beta(t) = (\sin 2t, \sin t)$ on $(-\pi, \pi)$; injective; immersive; *not* an embedding because the crossing point is approached from two sides of the domain boundary. When asked to give an example of "injective immersion that is not embedding", this is the answer.

**Two tangent directions = not a submanifold.** A clean test for whether a subset $S$ of $\mathbb{R}^n$ can be a $1$-submanifold: look at each point and identify all tangent directions of curves in $S$ through that point. If a single point has *two* tangent lines, $S$ is not a $1$-submanifold there (a submanifold has a unique tangent space at each point). This is the test that fails for the figure-eight at the crossing.

**Domain topology vs. subspace topology.** The figure-eight illustrates the most important distinction in submanifold theory: a subset of a manifold can be a smooth manifold *with its own topology* (the immersed-submanifold structure) even when its subspace topology is not locally Euclidean. The two topologies disagree, and the choice between them is the choice between immersed and embedded submanifolds. For the figure-eight, the domain topology (pulled back from $(-\pi, \pi)$) makes the image a smooth $1$-manifold; the subspace topology makes it a non-manifold space (with a singular crossing).

**Sequence-based detection of topology mismatch.** The standard tool for showing two topologies disagree is to exhibit a sequence that converges in one but not the other. The figure-eight's failing sequences $t_n = \pm\pi - 1/n$ converge in the subspace topology (to the crossing $(0,0)$) but not in the domain topology (where they diverge to $\pm\pi$, outside the domain). Whenever you suspect a topology mismatch, look for a sequence that "escapes" through the boundary or "wraps around" globally — these are the typical sources of mismatch.

**The general pattern: bounded domain + unboundary-approaches.** The figure-eight fails to be embedded because the parametrisation approaches the same limit point $(0,0)$ from two different ends of the open domain $(-\pi, \pi)$. The general pattern: when a parametrisation's image has limit points approached from sequences that diverge in the domain, the immersion is not an embedding. This is what compactness of the domain prevents: a compact domain has no "escape to the boundary".

**Cross-link to companion exercises.** This is the canonical injective-immersion-non-embedding. The companion [[Ex - An Injective Immersion is Not Always an Embedding]] develops both the figure-eight and the irrational-line-on-torus examples in parallel; this exercise focuses on the figure-eight in detail. The lessons from this example recur in Lie theory (closed-vs-non-closed Lie subgroups), foliation theory (leaves can be densely wound), and dynamical systems (orbits can be quasi-periodic).
