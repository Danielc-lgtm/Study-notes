---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Covering Space"
  - "Def - Lift of a Map"
  - "Thm - Path Lifting and Homotopy Lifting"
  - "Def - Path-Product and the Fundamental Group"
tags: [geometry, algebraic-topology, topology]
---

# Notation

$p : \tilde X \to X$ is a [[Def - Covering Space|covering map]]. $Y$ is a connected, locally path-connected topological space. $f : Y \to X$ is a continuous map. $y_0 \in Y$ is a base point, with $x_0 = f(y_0) \in X$ and $\tilde x_0 \in p^{-1}(x_0)$. $f_* : \pi_1(Y, y_0) \to \pi_1(X, x_0)$ and $p_* : \pi_1(\tilde X, \tilde x_0) \to \pi_1(X, x_0)$ are the induced homomorphisms. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the full registry.

---

# Statement

> **Theorem (Lifting Criterion).** Let $p : \tilde X \to X$ be a covering, $Y$ a connected and locally path-connected space, $f : Y \to X$ continuous, $y_0 \in Y$ with $x_0 = f(y_0)$, and $\tilde x_0 \in p^{-1}(x_0)$. A continuous lift $\tilde f : Y \to \tilde X$ with $\tilde f(y_0) = \tilde x_0$ exists **if and only if**
> $$f_* \pi_1(Y, y_0) \;\subseteq\; p_* \pi_1(\tilde X, \tilde x_0).$$
> When the lift exists, it is unique.

The condition says: every loop in $Y$ at $y_0$, pushed forward via $f$ to a loop in $X$ at $x_0$, must already be representable by a loop in $\tilde X$ starting and ending at $\tilde x_0$.

---

# Motivation

Path lifting ([[Thm - Path Lifting and Homotopy Lifting]]) tells us every *path* lifts uniquely once a starting point is chosen. The natural question is: what about more general continuous maps? Given $f : Y \to X$ and a chosen starting fibre point in $\tilde X$, does $f$ lift through the cover? The path-lifting answer is "yes for paths"; the general answer turns out to be "yes if and only if a certain $\pi_1$ subgroup inclusion holds."

This is the converse to the obvious half. If a lift $\tilde f$ exists, then any loop $\gamma$ in $Y$ at $y_0$ pushes to $f \circ \gamma$, which equals $p \circ (\tilde f \circ \gamma)$ — and $\tilde f \circ \gamma$ is a loop in $\tilde X$ at $\tilde x_0$, so $f \circ \gamma$ is in the image of $p_*$. Hence $f_*\pi_1(Y) \subseteq p_*\pi_1(\tilde X)$. The lifting criterion is the deep converse: the algebraic condition is *also sufficient*. Given the subgroup inclusion, you can construct the lift point-by-point, using path lifting.

The criterion is the central existence-of-lifts theorem and the engine of all subsequent applications. It tells you exactly when a continuous map factors through a cover, and in doing so it sets up the **Galois correspondence**: covers of $X$ are classified by subgroups of $\pi_1(X)$, with the inclusion structure mirrored on both sides. When $Y$ is simply connected (so $f_*\pi_1(Y) = 0$, which is included in *every* subgroup), the criterion says every map from $Y$ lifts to every cover — the easy and most-used case.

A historical note: this theorem first explicitly appears in Hurewicz's work on fibrations and lifting properties, though the underlying ideas were used informally by Poincaré in his original development of $\pi_1$. The criterion in its current form is a 20th-century clean-up.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis "$f_*\pi_1(Y) \subseteq p_*\pi_1(\tilde X)$" can hold for non-obvious reasons.

The first source is **$Y$ simply connected**. Then $\pi_1(Y) = 0$ and the inclusion is trivial. So *every* map from a simply-connected space to $X$ lifts through *every* covering of $X$. This is the most useful case in practice: when you need to lift a map and your domain happens to be a disc, a sphere, a contractible space, lifting is automatic.

The second source is **a path or homotopy with contractible domain**. Paths and homotopies are maps from $I$ and $I^2$, both contractible. So path/homotopy lifting from [[Thm - Path Lifting and Homotopy Lifting|the previous theorem]] is a special case of this criterion.

The third source is **a map whose image winds in a "tame" way around obstructions in $X$**. Even when $Y$ is not simply connected, $f$ might be chosen carefully so that $f_*\pi_1(Y)$ lands in $p_*\pi_1(\tilde X)$. For example, a map $S^1 \to X$ with $\pi_1(X) = \mathbb{Z}$ has $f_*\pi_1(S^1) = n\mathbb{Z}$ for the winding number $n$; if $\tilde X$ is the $k$-fold cover, $p_*\pi_1(\tilde X) = k\mathbb{Z}$; the lift exists iff $k | n$. This is the algebraic divisibility criterion behind many lifting decisions.

The fourth source is **a covering map $p$ with $p_*\pi_1(\tilde X)$ being a specific known subgroup**. For the universal cover $\widetilde X \to X$, $p_*\pi_1(\widetilde X) = 0$, so the only liftable maps are those with $f_*\pi_1(Y) = 0$ — i.e., maps from simply connected sources. So the universal cover has the strongest lifting requirement: only simply-connected sources lift to it (without restriction on the cover). For the trivial cover $X \to X$, $p_*\pi_1(X) = \pi_1(X)$ contains everything, and every map lifts (trivially).

**Targets (Output Amplification)**

The conclusion gives a unique lift; combined with other tools, this produces structural results.

The first combination is **with classification of covers**: the lifting criterion, applied to the identity map $\mathrm{id}_X : X \to X$ on the base, identifies subgroups of $\pi_1(X)$ with isomorphism classes of pointed connected covers. The map sends a cover to its $\pi_1$-image; the converse construction uses universal covers and the lifting criterion. Combined: lifting criterion + universal cover = Galois correspondence (see [[Thm - Galois Correspondence for Covering Spaces]]).

The second combination is **with deck transformations**: lifts of $\mathrm{id}_{\tilde X} : \tilde X \to \tilde X$ through $p$ are exactly deck transformations. The criterion says: given a chosen target lift, the lift exists iff the conjugacy class of subgroups is preserved (since $\tilde X \to X$ factors through itself with the right subgroup match). Combined: lifting criterion + universal cover = $\mathrm{Deck}(\widetilde X / X) \cong \pi_1(X)$.

The third combination is **with uniqueness on connected domains**: when $Y$ is connected, the lift (if it exists) is determined by its value at a single point. So the set of lifts (over varying starting points) is in bijection with the fibre $p^{-1}(x_0)$ when the subgroup inclusion holds. Combined: lifting criterion + connectedness = "number of lifts equals (intersection of fibre with a coset)" = controlled multiplicity.

The fourth combination is **with the homotopy extension property in CW complexes**: lifts can be extended cell-by-cell, with the lifting criterion checked one cell at a time. This converts global lifting questions into local cellular obstructions — the foundation of obstruction theory.

---

# Why Is It True

The intuition is that the algebraic condition $f_*\pi_1(Y) \subseteq p_*\pi_1(\tilde X)$ is *exactly* the obstruction to lifting being consistent.

**The bolded one-liner: define the lift point-by-point via path lifting; the algebraic condition guarantees that loops in $Y$ at $y_0$ lift to loops (not just paths) in $\tilde X$ at $\tilde x_0$, which is precisely what makes the point-by-point definition independent of path choice and hence well-defined.**

The construction:

1. **Define $\tilde f(y)$ for each $y \in Y$.** Choose a path $\alpha : I \to Y$ from $y_0$ to $y$ (exists by path-connectedness of $Y$). Push to $X$: $f \circ \alpha$ is a path from $x_0 = f(y_0)$ to $f(y)$. Lift to $\tilde X$ starting at $\tilde x_0$: get $\widetilde{f \circ \alpha} : I \to \tilde X$, a path from $\tilde x_0$ to some point in $p^{-1}(f(y))$. Define $\tilde f(y) := \widetilde{f \circ \alpha}(1)$.

2. **The definition is independent of the choice of path $\alpha$.** Suppose $\alpha, \beta$ are two paths from $y_0$ to $y$. Then $\alpha \cdot \beta^{-1}$ is a loop at $y_0$ in $Y$, and $f \circ (\alpha \cdot \beta^{-1})$ is a loop at $x_0$ in $X$. By the hypothesis $f_*\pi_1(Y) \subseteq p_*\pi_1(\tilde X)$, this loop equals (up to homotopy) $p \circ \delta$ for some loop $\delta$ at $\tilde x_0$ in $\tilde X$. So the lift of $f \circ (\alpha \cdot \beta^{-1})$ starting at $\tilde x_0$ is also a loop (by homotopy lifting applied to a homotopy that takes the loop to $p \circ \delta$, whose lift is $\delta$, a loop). So the lift of $\alpha$ and the lift of $\beta$ (both starting at $\tilde x_0$) have the same endpoint. Hence $\tilde f(y)$ is well-defined.

3. **Continuity of $\tilde f$ uses local path-connectedness of $Y$.** Near any $y \in Y$, choose a path-connected neighbourhood $V$. For $y' \in V$, choose a path inside $V$ from $y$ to $y'$. Lifting through the local structure of the cover near $f(y)$ shows $\tilde f$ is continuous on $V$. This is where local path-connectedness is essential: without it, the lifting near $y$ may not vary continuously.

4. **Uniqueness from connectedness.** Two lifts agreeing at $y_0$ agree everywhere, by Lemma 4 of [[Thm - Path Lifting and Homotopy Lifting]].

So the proof is a careful construction by path lifting, with the algebraic condition being exactly what makes the construction independent of choices.

---

# What Makes This Hard

The deep direction is the "if" part — given the subgroup inclusion, construct the lift. The construction is straightforward in outline but requires care with three details. **First**, the well-definedness step uses the *homotopy* lifting theorem (not just path lifting) to convert the subgroup condition into a loop-lifts-to-loop statement. People often try to do this with just path lifting and miss the role of homotopy lifting. **Second**, the continuity step requires *local* path-connectedness, not just path-connectedness — without it, the lift may be defined but discontinuous. This is the standard counterexample point: the "long line" or other pathological spaces can be path-connected but not locally path-connected, and the lifting criterion fails there. **Third**, the proof requires the *correct base-point matching*: the subgroup $p_*\pi_1(\tilde X, \tilde x_0)$ depends on $\tilde x_0$, and changing $\tilde x_0$ in the same fibre conjugates the subgroup. The condition is on the *conjugacy class* of subgroups when ignoring base points, or on the specific subgroup when matching base points.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For the "only if" direction, apply $\pi_1$ functoriality directly. For the "if" direction, construct $\tilde f$ point-by-point using path lifting, prove well-definedness via homotopy lifting and the subgroup condition, and prove continuity via local path-connectedness.

**Subgoal decomposition:**

1. **Only if direction (easy).** Assume a lift $\tilde f$ exists with $\tilde f(y_0) = \tilde x_0$. For any loop $\gamma$ at $y_0$, $f \circ \gamma = p \circ \tilde f \circ \gamma$; since $\tilde f \circ \gamma$ is a loop in $\tilde X$ at $\tilde x_0$, $f_*[\gamma] = p_*[\tilde f \circ \gamma] \in p_*\pi_1(\tilde X, \tilde x_0)$.
   - *Hint:* Functoriality and the definition of lift.
   - *Why needed:* Establishes necessity of the condition.

2. **If direction: point-by-point definition.** Assume the subgroup inclusion. For each $y \in Y$, pick a path $\alpha$ from $y_0$ to $y$; lift $f \circ \alpha$ starting at $\tilde x_0$; define $\tilde f(y)$ as the endpoint.
   - *Hint:* Use path-connectedness of $Y$ to get $\alpha$, path lifting to get the lift.
   - *Why needed:* Defines the candidate lift.

3. **Well-definedness.** Show that the definition does not depend on the choice of $\alpha$.
   - *Hint:* If $\alpha, \beta$ are two paths from $y_0$ to $y$, then $\alpha \cdot \beta^{-1}$ is a loop at $y_0$; the hypothesis says its image under $f$ is in $p_*\pi_1(\tilde X)$, so it lifts to a loop in $\tilde X$ at $\tilde x_0$. This forces the two lifts to have the same endpoint.
   - *Why needed:* Without well-definedness, the construction does not give a function $Y \to \tilde X$.

4. **Continuity.** Show $\tilde f$ is continuous, using local path-connectedness of $Y$.
   - *Hint:* Near each $y$, choose a path-connected open neighbourhood $V$, then for $y' \in V$ use a path inside $V$; the lift near $y$ varies continuously with $y'$ via local triviality of the cover.
   - *Why needed:* The lift must be a continuous map.

5. **Uniqueness.** Two lifts agreeing at $y_0$ agree everywhere on $Y$ (connected).
   - *Hint:* Lemma 4 of [[Thm - Path Lifting and Homotopy Lifting]].
   - *Why needed:* Uniqueness of the lift.

---

# Lemma Decomposition

> [!note]- Lemma 1: Necessity of the subgroup condition
> **Statement:** If a continuous lift $\tilde f : Y \to \tilde X$ with $\tilde f(y_0) = \tilde x_0$ exists, then $f_*\pi_1(Y, y_0) \subseteq p_*\pi_1(\tilde X, \tilde x_0)$.
>
> **Hint:** Apply $\pi_1$ to the relation $f = p \circ \tilde f$.
>
> **Why needed:** Establishes the "only if" direction trivially.
>
> > [!note]- Full proof
> > By functoriality, $f_* = p_* \circ \tilde f_* : \pi_1(Y, y_0) \to \pi_1(X, x_0)$. So for any $[\gamma] \in \pi_1(Y, y_0)$, $f_*[\gamma] = p_*\tilde f_*[\gamma] \in p_*\pi_1(\tilde X, \tilde x_0)$.

> [!note]- Lemma 2: Loop-lifts-to-loop iff subgroup inclusion
> **Statement:** Let $\delta$ be a loop in $X$ at $x_0$. Its lift to $\tilde X$ starting at $\tilde x_0$ is a loop (ends at $\tilde x_0$) if and only if $[\delta] \in p_*\pi_1(\tilde X, \tilde x_0)$.
>
> **Hint:** If $[\delta] = p_*[\tilde \delta]$ for some loop $\tilde \delta$, the lift of $\delta$ starting at $\tilde x_0$ is homotopic to $\tilde\delta$ (homotopy lifting), hence ends at $\tilde x_0$. Conversely, if the lift is a loop, it directly gives a $\tilde \delta$.
>
> **Why needed:** The bridge between the algebraic subgroup condition and the geometric loop-lifting condition.
>
> > [!note]- Full proof
> > ($\Leftarrow$) Suppose $[\delta] = p_*[\tilde\delta]$, i.e., $\delta \simeq p \circ \tilde\delta$ via a homotopy $H : I \times I \to X$. By homotopy lifting, $H$ lifts to $\tilde H : I \times I \to \tilde X$ with $\tilde H(\cdot, 0) = \widetilde\delta$ (the lift of $\delta$ starting at $\tilde x_0$) and $\tilde H(\cdot, 1) = \tilde\delta$ (a loop). The endpoints $\tilde H(1, t)$ lie in the fibre $p^{-1}(x_0)$ (discrete) for all $t$ (because $H(1, t) = x_0$ by the rel-endpoints condition on $H$), so they are constant in $t$. Hence $\widetilde\delta(1) = \tilde H(1, 0) = \tilde H(1, 1) = \tilde x_0$, so $\widetilde\delta$ is a loop.
> >
> > ($\Rightarrow$) Suppose $\widetilde\delta$ is a loop at $\tilde x_0$. Then $[\delta] = p_*[\widetilde\delta] \in p_*\pi_1(\tilde X, \tilde x_0)$.

> [!note]- Lemma 3: Well-definedness of the point-by-point construction
> **Statement:** Assume $f_*\pi_1(Y, y_0) \subseteq p_*\pi_1(\tilde X, \tilde x_0)$. For $y \in Y$ and two paths $\alpha, \beta$ from $y_0$ to $y$, the lifts of $f \circ \alpha$ and $f \circ \beta$ starting at $\tilde x_0$ have the same endpoint.
>
> **Hint:** The concatenation $\alpha \cdot \beta^{-1}$ is a loop, $f \circ (\alpha \cdot \beta^{-1})$ is in $f_*\pi_1(Y, y_0) \subseteq p_*\pi_1(\tilde X, \tilde x_0)$; apply Lemma 2.
>
> **Why needed:** Defines the lift as a function.
>
> > [!note]- Full proof
> > The path $\alpha \cdot \beta^{-1}$ is a loop in $Y$ at $y_0$; $f \circ (\alpha \cdot \beta^{-1}) = (f \circ \alpha) \cdot (f \circ \beta^{-1})$ is a loop in $X$ at $x_0$, in $f_*\pi_1(Y, y_0)$. By hypothesis, $f_*\pi_1(Y, y_0) \subseteq p_*\pi_1(\tilde X, \tilde x_0)$, so the loop is in $p_*\pi_1(\tilde X, \tilde x_0)$. By Lemma 2, the lift of $(f \circ \alpha) \cdot (f \circ \beta^{-1})$ starting at $\tilde x_0$ is a loop — i.e., it ends at $\tilde x_0$.
> >
> > The lift of $(f \circ \alpha) \cdot (f \circ \beta^{-1})$ starting at $\tilde x_0$ is constructed as: lift $f \circ \alpha$ first (ends at $\widetilde{f \circ \alpha}(1)$), then lift $f \circ \beta^{-1}$ starting from that endpoint (ends at... call it $z$). The whole lift being a loop means $z = \tilde x_0$. But the lift of $f \circ \beta^{-1}$ starting from $\widetilde{f \circ \alpha}(1)$ is the reverse of the lift of $f \circ \beta$ starting at $z = \tilde x_0$. So the lift of $f \circ \beta$ starting at $\tilde x_0$ ends at $\widetilde{f \circ \alpha}(1)$. Hence $\widetilde{f \circ \alpha}(1) = \widetilde{f \circ \beta}(1)$.

> [!note]- Lemma 4: Continuity of $\tilde f$ via local path-connectedness
> **Statement:** With $Y$ locally path-connected, the function $\tilde f : Y \to \tilde X$ defined by Lemma 3 is continuous.
>
> **Hint:** Near each $y$, take a path-connected open neighbourhood $V$ such that $f(V)$ lies in an evenly covered open set; show $\tilde f|_V$ equals the local inverse of $p$ followed by $f$.
>
> **Why needed:** $\tilde f$ must be continuous.
>
> > [!note]- Full proof
> > Fix $y \in Y$; let $\tilde y := \tilde f(y)$. Choose an evenly covered open neighbourhood $U$ of $f(y)$ in $X$ with $\tilde U_\alpha$ the sheet containing $\tilde y$, so $p|_{\tilde U_\alpha} : \tilde U_\alpha \to U$ is a homeomorphism. Let $W = f^{-1}(U) \cap V$ where $V$ is a path-connected open neighbourhood of $y$ (exists by local path-connectedness). For $y' \in W$, choose a path $\sigma$ from $y$ to $y'$ inside $V$ (path-connected). The path $f \circ \sigma$ lies in $U$ (since $\sigma \subseteq V$ and $V \subseteq f^{-1}(U)$... wait, more carefully: $\sigma \subseteq V$ and $f(V) \subseteq U$ is not necessarily true, only $f(W) \subseteq U$. Better: take $W = V \cap f^{-1}(U)$ open in $Y$, path-connected if $V$ is path-connected and we take $V$ small enough). Then by Lemma 1 of [[Thm - Path Lifting and Homotopy Lifting]] applied to $f \circ \sigma : I \to U$, the lift starting at $\tilde y$ stays in the sheet $\tilde U_\alpha$, and equals $(p|_{\tilde U_\alpha})^{-1} \circ f \circ \sigma$. So $\tilde f(y') = (p|_{\tilde U_\alpha})^{-1}(f(y'))$ — explicitly continuous in $y'$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem (Lifting Criterion).** A continuous lift $\tilde f : Y \to \tilde X$ with $\tilde f(y_0) = \tilde x_0$ exists iff $f_*\pi_1(Y, y_0) \subseteq p_*\pi_1(\tilde X, \tilde x_0)$, and is unique when it exists.
>
> *Proof.*
>
> **Step 0 (well-posedness):** $Y$ connected and locally path-connected; $X$ underlying any covering $p$; $f$ continuous; choices of base points fixed.
>
> **Necessity (only if):** Lemma 1 — apply $\pi_1$ functoriality to $f = p \circ \tilde f$.
>
> **Sufficiency (if):** Assume the subgroup inclusion. For $y \in Y$, define $\tilde f(y)$ as in Lemma 3: choose a path $\alpha$ from $y_0$ to $y$, lift $f \circ \alpha$ to $\tilde X$ starting at $\tilde x_0$, set $\tilde f(y)$ to the endpoint. Lemma 3 confirms well-definedness. Lemma 4 confirms continuity.
>
> Then $p(\tilde f(y)) = p(\widetilde{f \circ \alpha}(1)) = (f \circ \alpha)(1) = f(y)$, so $p \circ \tilde f = f$. And $\tilde f(y_0)$ is the endpoint of the lift of $f \circ c_{y_0} = c_{x_0}$ starting at $\tilde x_0$, which is the constant lift $\tilde c_{\tilde x_0}$, ending at $\tilde x_0$. So $\tilde f(y_0) = \tilde x_0$.
>
> **Uniqueness:** Lemma 4 of [[Thm - Path Lifting and Homotopy Lifting]] applied to $Y$ (connected) and the two lifts.
>
> $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Complex analysis: existence of holomorphic branches of logarithm.** A branch of $\log z$ on an open set $U \subseteq \mathbb{C}^* = \mathbb{C} \setminus \{0\}$ is a lift of $U \hookrightarrow \mathbb{C}^*$ through the universal cover $\exp : \mathbb{C} \to \mathbb{C}^*$. By the lifting criterion, this exists iff $\pi_1(U) = 0$ (or more precisely, the image $i_*\pi_1(U)$ is trivial). So $\log$ has a branch on any simply-connected open subset of $\mathbb{C}^*$, but not on $\mathbb{C}^*$ itself (which has $\pi_1 = \mathbb{Z}$, generated by the unit circle).

**Differential geometry: existence of orientations.** An orientation of a manifold $M$ is a lift of the identity $M \to M$ through the orientable double cover $\widetilde M^{\mathrm{or}} \to M$. By the lifting criterion, this exists iff the orientation character $w_1 : \pi_1(M) \to \mathbb{Z}/2$ is trivial, i.e., iff $M$ is orientable. The criterion makes orientability a homotopy-theoretic property.

**Gauge theory: existence of spin structures.** A spin structure on a Riemannian manifold $M$ is a lift of the frame bundle through $\mathrm{Spin}(n) \to \mathrm{SO}(n)$. By the lifting criterion (a fibre-bundle version of the same theorem), this exists iff a certain $\pi_1$-condition holds — equivalently iff $w_2(TM) = 0$, where $w_2$ is the second Stiefel-Whitney class. The criterion explains why spin structures are an obstruction theory.

**Number theory: existence of $K$-rational points on covers.** For an étale cover of algebraic varieties (the algebraic analogue), the criterion takes the form: a $K$-rational point of the base lifts to a $K$-rational point of the cover iff the corresponding Galois-theoretic condition holds. This is the foundation of arithmetic descent theory.

---

# Bridges

- **[[Thm - Path Lifting and Homotopy Lifting]]** — the lifting criterion is the deep extension. Path lifting is the special case $Y = I$ (which has $\pi_1 = 0$, so the criterion's inclusion is automatic). Homotopy lifting is the special case $Y = I \times I$ (also $\pi_1 = 0$). Both are degenerate cases of the general criterion, with the algebraic condition trivially satisfied because the domain is simply connected.

- **[[Thm - Galois Correspondence for Covering Spaces]]** — the criterion is the key technical input for the Galois correspondence. To show every subgroup of $\pi_1(X)$ comes from a cover, you build the cover as a quotient of the universal cover by the subgroup (action by deck transformations) and verify the lift exists using the criterion. To show every cover gives a subgroup, use $p_*\pi_1(\tilde X)$. The criterion ensures the bijection is well-defined and uniquely determined.

- **[[Def - Universal Cover]]** — the universal cover has the strongest lifting property: every map from a sufficiently-nice space lifts through it iff its $\pi_1$-image is trivial. In particular, every map from a simply-connected space lifts through every cover, with the universal cover being the "destination" that retains the maximum amount of detail.

- **Obstruction theory and characteristic classes** — the lifting criterion is the simplest case of obstruction theory: extend a section over the next cell iff a cocycle condition vanishes. For coverings, the obstruction is in $H^1$ (the $\pi_1$ subgroup inclusion); for general fibrations, the obstruction lives in higher cohomology with twisted coefficients. Characteristic classes (Stiefel-Whitney, Chern, Pontryagin) are obstructions to lifting structure groups through certain principal bundles.

- **Étale fundamental group and Galois descent** — in algebraic geometry, lifting through étale morphisms is governed by exactly the same criterion (with the étale $\pi_1$ replacing the topological $\pi_1$). This is the algebraic version of the lifting criterion and underlies arithmetic descent theory and the theory of Galois cohomology.
