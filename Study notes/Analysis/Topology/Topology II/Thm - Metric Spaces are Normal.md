---
type: theorem
subject: topology
prereqs:
  - "Def - Separation Axioms"
  - "Def - Metric Space"
  - "Def - Continuous Map"
tags: [analysis, topology, separation, metric]
---

# Notation

$(X, d)$ is a [[Def - Metric Space|metric space]]; $d : X \times X \to [0, \infty)$ is the metric. For a nonempty $A \subseteq X$, the **distance from a point to $A$** is $d(x, A) = \inf\{d(x, a) : a \in A\}$. A space is **normal** ([[Def - Separation Axioms|$T_4$]]) if it is $T_1$ and any two disjoint closed sets $F, G$ have disjoint open neighborhoods. The full registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Theorem.** Every [[Def - Metric Space|metric space]] $(X, d)$ is **normal**.

The proof is explicit: given two disjoint closed sets $F, G$, the continuous function $\varphi(x) = d(x, F)/(d(x, F) + d(x, G))$ takes values $0$ on $F$ and $1$ on $G$; its preimages $\varphi^{-1}([0, 1/2))$ and $\varphi^{-1}((1/2, 1])$ are disjoint open sets containing $F$ and $G$ respectively.

---

# Motivation

The separation axioms are a hierarchy of conditions on a topology. $T_0, T_1, T_2$ are about *points* — distinguish them, isolate them, separate them. $T_3$ (regular) and $T_4$ (normal) escalate to closed sets — separate a *point* from a closed set, then separate two *closed sets*. The question this theorem answers is: *which spaces achieve the strongest separation*?

The answer is universally: every metric space. The metric structure, which seems like extra data, is *strictly stronger* than every separation axiom up through $T_4$. So when one works in $\mathbb{R}^n$ or any Banach space or function space with a sup norm, separation is automatic — every closed-set pair can be separated.

But more than the *fact*, the *proof method* is the deeper takeaway. The proof exhibits an *explicit continuous function* $\varphi : X \to [0, 1]$ that *vanishes on one closed set and equals one on the other*. This is the **separating function**: a single continuous function whose level sets achieve the separation, rather than two unrelated open sets cobbled together. The separating function is what one actually wants — much stronger than just disjoint opens, because it gives a *partition* of $X$ into level sets, a continuous interpolation between $F$ and $G$, and a foothold for constructions (extensions, partitions of unity, smooth bump functions in differential geometry).

The generalization to all normal spaces is **Urysohn's lemma**: in any normal space, disjoint closed sets can be separated by a continuous function $[0, 1]$-valued. The metric-space proof is the prototype — it works because metric spaces are *constructively* normal: the function $\varphi$ is given by a formula, not produced by iterative limiting. Urysohn's lemma in arbitrary normal spaces requires a deeper iterative construction (waiting in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]), but the metric-space case is direct.

This theorem is also the bridge between metric geometry and abstract topology. It says: every topological property derivable from normality (which is a long list, including Urysohn, Tietze extension, paracompactness in second-countable, partitions of unity in smooth manifolds) is automatically true in every metric space. So once a result is proved in the metric setting, the question becomes "does it generalize to normal?" — and if so, the metric case was already a special case of a topological theorem.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$X$ is a metric space".

The first disguised source is **$X$ is a normed vector space**. Property $B$: $X$ has a norm $\lVert \cdot \rVert$. The bridge: $d(x, y) = \lVert x - y \rVert$ is a metric. *Example:* $L^p$ spaces, $C([0,1])$ with sup norm, $\mathbb{R}^n$ with any norm.

The second disguised source is **$X$ is metrizable** — there exists *some* metric on $X$ inducing the given topology, even if no canonical one is given. Property $B$: the topology is metrizable. The bridge: just pick any compatible metric. *Example:* by **Urysohn's metrization theorem**, every second-countable regular Hausdorff space is metrizable, hence normal — this is a substantial promotion. Most "nice" topological spaces met in analysis (manifolds, separable Hilbert spaces, separable Banach spaces) are metrizable.

The third disguised source is **$X$ is a subspace of a metric space**. Property $B$: $X$ embeds in a metric space. The bridge: subspaces of metric spaces are metric. *Example:* this is how one shows quotients and subspaces in $\mathbb{R}^n$ inherit normality automatically.

**Targets (Output Amplification)**

The conclusion is "$X$ is normal".

Combine the conclusion with **a continuous function on a closed subspace**. Property $D$: $f : F \to \mathbb{R}$ continuous on closed $F \subseteq X$. Amplified result $E$: $f$ extends to a continuous $\tilde f : X \to \mathbb{R}$ (Tietze extension theorem). The bridge is that normal spaces support continuous extensions, and the proof of Tietze uses the metric-space-style explicit construction. *Example:* extending a continuous function on a closed disk to a continuous function on the plane.

Combine the conclusion with **two disjoint closed sets and the need for a "smooth" separation**. Property $D$: one wants a continuous function $\varphi : X \to [0, 1]$ with $\varphi = 0$ on $F$ and $\varphi = 1$ on $G$. Amplified result $E$: such $\varphi$ exists explicitly via the distance-function formula. *Example:* construction of bump functions in $C^\infty(\mathbb{R}^n)$, partitions of unity on metric (and in particular smooth) manifolds. The bump function $\psi : \mathbb{R} \to [0, 1]$ with $\psi = 0$ outside $(-1, 1)$ and $\psi > 0$ on $(-1, 1)$ is a refinement of the separation construction.

Combine the conclusion with **the Urysohn metrization or paracompactness machinery**. Property $D$: $X$ is normal Hausdorff with countable open cover refinement. Amplified result $E$: $X$ has paracompact structure, partitions of unity exist subordinate to any open cover, and every continuous function can be expressed via partitions of unity. *Example:* every metric space is paracompact (a deeper theorem in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]); this is a stronger statement than normality and is built atop it.

---

# Why Is It True

Normality is the statement that disjoint closed sets can be separated by disjoint opens. In a metric space, *distances control everything*. The function $\varphi(x) = d(x, F)/(d(x, F) + d(x, G))$ is designed to be a smoothed indicator: $0$ on $F$ (because $d(x, F) = 0$ for $x \in F$), $1$ on $G$ (because $d(x, F)/d(x, F) = 1$ when $d(x, G) = 0$), and varying continuously in between.

That the denominator $d(x, F) + d(x, G)$ is *never zero* is the crucial point: it would be zero if and only if $d(x, F) = 0$ and $d(x, G) = 0$, i.e., $x$ is in *both* closures. Since $F$ and $G$ are closed and disjoint, $\overline{F} \cap \overline{G} = F \cap G = \emptyset$, so the denominator is positive everywhere. This is *where the closedness of $F, G$ does its work* — without closedness, the closures could overlap and the formula could blow up.

Once $\varphi : X \to [0, 1]$ is constructed and continuous, the separation falls out: $\varphi^{-1}([0, 1/2))$ is open (preimage of an open interval under continuous $\varphi$), contains $F$ (since $\varphi = 0$ on $F$), and is disjoint from $\varphi^{-1}((1/2, 1])$ which is open and contains $G$. The midpoint $1/2$ is the "barrier" — points strictly below $1/2$ are unambiguously on $F$'s side, points strictly above $1/2$ are unambiguously on $G$'s side, and the level set $\varphi^{-1}(1/2)$ is the "boundary" between the two open neighborhoods.

The geometric picture: $\varphi$ measures the *relative distance* of $x$ from $F$ versus $G$. It is $0$ if $x$ is at $F$, $1$ if $x$ is at $G$, and an interpolation otherwise based on the ratio of distances. The level sets of $\varphi$ are "equidistant locuses" — surfaces along which the ratio $d(x, F)/d(x, G)$ is constant. In Euclidean space these are hyperboloids or planes (depending on the geometry of $F, G$), but for the topological separation argument, only their continuity matters.

The reason this proof generalizes to normal spaces (Urysohn's lemma) but not in this *direct* form is that there is no distance function in a general normal space. Urysohn's lemma instead builds $\varphi$ as a limit of step functions, with the levels indexed by dyadic rationals in $[0, 1]$ — at each step, the closed-neighborhood-basis form of regularity ([[Thm - Regular Iff Closed Neighborhoods Form a Basis]]) is used to insert a new open set between the previous opens. The metric-space proof is the special case where this dyadic construction collapses to a single explicit formula.

---

# What Makes This Hard

The proof is short, but the non-obvious step is *choosing the formula* $\varphi(x) = d(x, F)/(d(x, F) + d(x, G))$ — specifically, the *normalization* $d(x, F) + d(x, G)$ in the denominator, which is what guarantees the formula is well-defined (no zero denominator) when $F$ and $G$ are *closed* and *disjoint*. The most common error is to use $\varphi(x) = d(x, F)$ alone (which is continuous and zero on $F$, but does not equal $1$ on $G$) or $\varphi(x) = d(x, F)/d(x, G)$ (which blows up on $G$). A second pitfall is forgetting that the denominator is positive *only because $F$ and $G$ are both closed*: if either were open, points in the boundary could have zero distance to both.

---

# Rederivation Scaffold

**High-level strategy:**
Define $\varphi(x) = d(x, F)/(d(x, F) + d(x, G))$. The denominator is positive (since $F, G$ closed and disjoint), $\varphi$ is continuous, takes values in $[0, 1]$, equals $0$ on $F$, equals $1$ on $G$. The preimages of $[0, 1/2)$ and $(1/2, 1]$ are the disjoint open separators.

**Subgoal decomposition:**

1. **Verify the distance function $d(\cdot, A)$ is continuous.** For any nonempty $A \subseteq X$, $|d(x, A) - d(y, A)| \leq d(x, y)$.
   - *Hint:* Triangle inequality: $d(x, a) \leq d(x, y) + d(y, a)$, take inf over $a$.
   - *Why needed:* It makes $\varphi$ continuous, since $\varphi$ is built from continuous distance functions.

2. **Note $d(x, A) = 0$ if and only if $x \in \overline{A}$.** And $A$ is closed if and only if $A = \overline{A}$.
   - *Hint:* $d(x, A) = 0$ means there are points of $A$ arbitrarily close to $x$, which is the characterization of closure.
   - *Why needed:* It guarantees $\varphi = 0$ exactly on $F$ and (combined with disjointness) that the denominator never vanishes.

3. **Verify the denominator $d(x, F) + d(x, G)$ is positive.** Since $F \cap G = \emptyset$, for any $x \in X$ at least one of $d(x, F), d(x, G)$ is positive.
   - *Hint:* If both are zero, $x \in \overline{F} \cap \overline{G} = F \cap G = \emptyset$, contradiction.
   - *Why needed:* Makes $\varphi$ well-defined.

4. **Verify $\varphi : X \to [0, 1]$ is continuous.** A continuous quotient (denominator nonzero) of continuous functions.
   - *Hint:* The division map $\mathbb{R} \times \mathbb{R} \setminus \{0\} \to \mathbb{R}$, $(a, b) \mapsto a/b$, is continuous, and composition with continuous functions is continuous.

5. **Verify $\varphi(x) = 0$ on $F$ and $\varphi(x) = 1$ on $G$.** Direct from the formula.

6. **Define $U = \varphi^{-1}([0, 1/2))$ and $V = \varphi^{-1}((1/2, 1])$.** Both open (preimages of open intervals), $U \supseteq F, V \supseteq G$, $U \cap V = \emptyset$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The distance function $d(\cdot, A)$ is 1-Lipschitz, hence continuous
> **Statement:** For any nonempty $A \subseteq X$, the function $x \mapsto d(x, A) = \inf_{a \in A} d(x, a)$ is 1-Lipschitz: $|d(x, A) - d(y, A)| \leq d(x, y)$ for all $x, y \in X$.
>
> **Hint:** Triangle inequality: $d(x, a) \leq d(x, y) + d(y, a)$, take inf over $a \in A$.
>
> **Why needed:** It is the continuity of the components from which $\varphi$ is built.
>
> > [!note]- Full proof
> > For any $a \in A$ and any $x, y \in X$, $d(x, a) \leq d(x, y) + d(y, a)$ by the triangle inequality. Taking inf over $a \in A$ on both sides (right side: inf only over the $a$-dependent term),
> > $$d(x, A) = \inf_{a \in A} d(x, a) \leq d(x, y) + \inf_{a \in A} d(y, a) = d(x, y) + d(y, A).$$
> > So $d(x, A) - d(y, A) \leq d(x, y)$. By symmetry, $d(y, A) - d(x, A) \leq d(x, y)$. Together: $|d(x, A) - d(y, A)| \leq d(x, y)$. A 1-Lipschitz function is continuous.

> [!note]- Lemma 2: $d(x, A) = 0$ if and only if $x \in \overline{A}$
> **Statement:** For any $A \subseteq X$ and $x \in X$, $d(x, A) = 0 \iff x \in \overline{A}$.
>
> **Hint:** $d(x, A) = 0$ means there are points of $A$ in every ball $B_\epsilon(x)$, which is the closure characterization.
>
> **Why needed:** It guarantees the denominator $d(x, F) + d(x, G)$ is positive whenever $F, G$ are closed and disjoint.
>
> > [!note]- Full proof
> > ($\Rightarrow$) If $d(x, A) = 0$, then $\inf_{a \in A} d(x, a) = 0$, so for every $\epsilon > 0$ there is $a \in A$ with $d(x, a) < \epsilon$. Hence $B_\epsilon(x) \cap A \neq \emptyset$ for all $\epsilon > 0$, so $x \in \overline{A}$.
> >
> > ($\Leftarrow$) If $x \in \overline{A}$, every ball $B_\epsilon(x)$ meets $A$, so for each $\epsilon > 0$ there is $a \in A$ with $d(x, a) < \epsilon$, hence $d(x, A) \leq \epsilon$. Since $\epsilon$ was arbitrary, $d(x, A) = 0$.

> [!note]- Lemma 3: $\varphi(x) = d(x, F) / (d(x, F) + d(x, G))$ is continuous on $X$, takes values in $[0, 1]$, equals $0$ on $F$, equals $1$ on $G$
> **Statement:** When $F, G$ are disjoint closed subsets of the metric space $X$, the function $\varphi$ defined above is well-defined, continuous, $[0, 1]$-valued, with $\varphi|_F = 0$ and $\varphi|_G = 1$.
>
> **Hint:** Use Lemmas 1, 2 and the continuity of arithmetic operations.
>
> **Why needed:** It is the separating function.
>
> > [!note]- Full proof
> > *Well-defined.* The denominator $d(x, F) + d(x, G)$ is zero only if both terms are zero, i.e., $x \in \overline{F} \cap \overline{G} = F \cap G = \emptyset$ (using closedness of $F, G$ via Lemma 2). So the denominator is positive everywhere, and $\varphi$ is defined on all of $X$.
> >
> > *Continuous.* $d(\cdot, F)$ and $d(\cdot, G)$ are continuous by Lemma 1. Their sum is continuous (sum of continuous), and the sum is positive everywhere, so $1/(\text{sum})$ is continuous (since the reciprocal is continuous on nonzero reals). Hence the product $d(\cdot, F) \cdot (d(\cdot, F) + d(\cdot, G))^{-1} = \varphi$ is continuous.
> >
> > *Values in $[0, 1]$.* Both $d(x, F)$ and $d(x, F) + d(x, G)$ are nonnegative, and $d(x, F) \leq d(x, F) + d(x, G)$, so $0 \leq \varphi(x) \leq 1$.
> >
> > *Values on $F$.* For $x \in F$, $d(x, F) = 0$ (Lemma 2), so $\varphi(x) = 0/(0 + d(x, G)) = 0$.
> >
> > *Values on $G$.* For $x \in G$, $d(x, G) = 0$, so $\varphi(x) = d(x, F)/(d(x, F) + 0) = 1$ (note $d(x, F) > 0$ for $x \in G$ since $F$ and $G$ are disjoint and $F$ is closed).

---

# Formal Proof

> [!note]- Complete formal proof
>
> Let $(X, d)$ be a metric space; we must show every metric space is $T_1$ (singletons closed) and that disjoint closed sets are separated by disjoint opens.
>
> *$T_1$.* For any $x \neq y$ in $X$, the ball $B_{d(x, y)}(x)$ contains $x$ but not $y$, so $\{y\}$ is the intersection of closed complements of balls, hence closed.
>
> *Normality.* Let $F, G$ be disjoint closed subsets of $X$. Define
> $$\varphi(x) = \frac{d(x, F)}{d(x, F) + d(x, G)}.$$
> By Lemma 3, $\varphi : X \to [0, 1]$ is continuous with $\varphi|_F = 0$ and $\varphi|_G = 1$.
>
> Set $U = \varphi^{-1}([0, 1/2))$ and $V = \varphi^{-1}((1/2, 1])$. Both are preimages of open subsets of $[0, 1]$ under the continuous $\varphi$, hence open in $X$. By the values of $\varphi$, $F \subseteq U$ and $G \subseteq V$. And $U \cap V = \varphi^{-1}([0, 1/2)) \cap \varphi^{-1}((1/2, 1]) = \varphi^{-1}([0, 1/2) \cap (1/2, 1]) = \varphi^{-1}(\emptyset) = \emptyset$.
>
> So $U$ and $V$ are disjoint open neighborhoods of $F$ and $G$. Hence $X$ is normal. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Bump functions in $\mathbb{R}^n$ via this construction.** The classical bump function $\psi : \mathbb{R} \to [0, 1]$ with $\psi = 1$ on $[-1, 1]$ and $\psi = 0$ outside $[-2, 2]$ is a smoothed version of the separating function for $F = [-1, 1]$ and $G = \mathbb{R} \setminus (-2, 2)$. The metric-space construction $\varphi(x) = d(x, F)/(d(x, F) + d(x, G))$ gives a *continuous* but not smooth function; convolving with a smoothing kernel yields a $C^\infty$ bump function, the foundational tool of distribution theory and partitions of unity in differential geometry.

**Local-to-global gluing on manifolds.** A smooth manifold $M$ is metrizable (paracompact + Hausdorff + locally Euclidean). By this theorem, $M$ is normal. Disjoint closed subsets of $M$ have continuous separating functions. Combined with smoothing, this yields **smooth partitions of unity** subordinate to any open cover — the engine of every local-to-global construction in differential geometry (integration of differential forms, gluing local connections, building global vector fields). The application is nonobvious because the metric on $M$ is *not* canonical (depends on a Riemannian structure or embedding), but the *consequence* (normality) is topology-only.

**Distance to a closed subset in a Banach space.** In a Banach space, the distance $d(x, F) = \inf_{f \in F} \lVert x - f \rVert$ to a closed convex $F$ is the foundation of projection theory (in Hilbert space, the minimizer is unique and gives the orthogonal projection). The continuity of $d(\cdot, F)$ — a corollary of Lemma 1 — is the topological input to the regularity of the projection operator. This is the bridge between separating function constructions and the geometry of Hilbert spaces.

---

# Bridges

- **[[Def - Separation Axioms]]** — normality is $T_4$. This theorem is the *cleanest source* of normal spaces: every metric space.

- **[[Thm - Regular Iff Closed Neighborhoods Form a Basis]]** — the previous step in the separation hierarchy. Metric spaces are normal (this theorem), normal implies regular (a point is closed, so closed-set vs closed-set separation includes point vs closed-set), regular has closed-neighborhood basis. So metric spaces have closed-neighborhood basis, which one sees directly: $\overline{B_{r/2}(x)} \subseteq B_r(x)$.

- **Urysohn's lemma** — the generalization. In *any* normal space (not just metric), disjoint closed sets can be separated by a continuous function $X \to [0, 1]$. The metric-space proof — explicit formula — is the model; the general proof — dyadic iteration of closed-neighborhood-basis arguments — is the elaboration.

- **Tietze extension theorem** — built atop Urysohn's lemma. A continuous function on a closed subspace of a normal space extends to the whole space. For metric spaces, this means continuous functions on closed subsets of $\mathbb{R}^n$ extend to $\mathbb{R}^n$ — a foundational construction in real analysis.

- **Paracompactness of metric spaces** — every metric space is *paracompact*, a property strictly stronger than normality. Stone's theorem proves this; the upshot is partitions of unity subordinate to any open cover, in any metric space. The path is: metric → normal (this theorem) → paracompact (Stone) → partitions of unity exist.

---

# Unlocked by This

> [!tip] **Urysohn's Lemma** *(from Topology III)*
> In every normal space (not just metric), disjoint closed sets are separated by a continuous $[0, 1]$-valued function. This generalizes the explicit formula of this theorem to a more abstract iterative construction. The proof uses the closed-neighborhood-basis form of regularity to dyadically interpolate level sets between the two closed sets.

> [!tip] **Tietze Extension Theorem** *(from Topology III)*
> A continuous bounded function on a closed subset of a normal space extends continuously to the whole space. Built atop Urysohn's lemma, this is the foundation of many extension and approximation results in analysis.

> [!tip] **Partitions of Unity** *(from Differential Geometry)*
> On a paracompact Hausdorff space (in particular every smooth manifold), for any open cover one can find continuous (smooth if the space is smooth) functions $\{\psi_\alpha\}$ subordinate to the cover, with $\sum \psi_\alpha = 1$. The construction uses Urysohn's lemma (and hence implicitly this theorem) at the local level.

> [!tip] **Bump Functions and Mollifiers** *(from Distribution Theory)*
> Smoothed indicator functions in $\mathbb{R}^n$ — the analytic building blocks of test functions, distributions, and convolutions — descend from the metric separating function $\varphi$ in this theorem, refined by convolution with smooth kernels.
