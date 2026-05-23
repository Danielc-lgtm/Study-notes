---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Covering Space"
  - "Def - Lift of a Map"
tags: [geometry, algebraic-topology, topology]
---

# Notation

$p : \tilde X \to X$ is a [[Def - Covering Space|covering map]]. A **path** in $X$ is a continuous $\gamma : I \to X$. A **homotopy** in $X$ is a continuous $H : Y \times I \to X$ for some space $Y$; the special case $Y = I$ gives path-homotopies. A **lift** of $\gamma$ (resp. $H$) is a continuous $\tilde\gamma : I \to \tilde X$ (resp. $\tilde H : Y \times I \to \tilde X$) with $p \circ \tilde\gamma = \gamma$ (resp. $p \circ \tilde H = H$). See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the full registry.

---

# Statement

> **Theorem (Path Lifting).** Let $p : \tilde X \to X$ be a covering map. For every continuous path $\gamma : I \to X$ and every point $\tilde x_0 \in p^{-1}(\gamma(0))$, there exists a *unique* continuous lift $\tilde\gamma : I \to \tilde X$ with $p \circ \tilde\gamma = \gamma$ and $\tilde\gamma(0) = \tilde x_0$.

> **Theorem (Homotopy Lifting Property for Coverings).** Let $p : \tilde X \to X$ be a covering map and $Y$ any topological space. For every continuous homotopy $H : Y \times I \to X$ and every continuous lift $\tilde H_0 : Y \to \tilde X$ of $H|_{Y \times \{0\}}$ (i.e., $p \circ \tilde H_0 = H(\cdot, 0)$), there exists a *unique* continuous lift $\tilde H : Y \times I \to \tilde X$ with $p \circ \tilde H = H$ and $\tilde H|_{Y \times \{0\}} = \tilde H_0$.

Path lifting is the special case $Y = $ point of homotopy lifting (or more precisely, $Y = \{*\}$ and $I$ playing the role of homotopy parameter), but it is often easier to state and prove separately because the indexing is simpler. The two together are the foundation of all covering-space theory.

---

# Motivation

The whole point of a covering space $p : \tilde X \to X$ is that it "sits above $X$" in a controlled way — locally, $\tilde X$ looks like a disjoint union of copies of $X$. The natural question is: given motion in $X$ (a path, or more generally a continuous family of points), can we follow it up in $\tilde X$? That is, can we lift the motion?

Path lifting answers yes, and uniquely once a starting fibre point is chosen. Homotopy lifting extends this: not only does a single path lift, but a continuous *family* of paths (a homotopy) lifts coherently. This second part is the powerful one — it is what makes the winding number a homotopy invariant, what makes $\pi_1$ functorial, what makes the universal cover have the universal property it has.

These are the foundational technical lemmas of the chapter. Every concrete computation of $\pi_1$ uses them. The proof that $\pi_1(S^1) = \mathbb{Z}$ is *literally* path lifting + homotopy lifting + simple connectedness of $\mathbb{R}$, packaged as the winding number. The proof that homotopic loops give the same monodromy action on a fibre is homotopy lifting. The Galois correspondence proceeds by lifting carefully chosen maps. So this theorem is the engine room.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is bare — any covering map and any path (or homotopy) — but recognising when the theorem applies in non-covering-looking situations is the skill.

The first source is **a quotient $X = \tilde X / \Gamma$ by a free properly discontinuous group action**. Such a quotient is automatically a covering map $\tilde X \to X$ (the deck group is $\Gamma$). So whenever a problem presents a space as a quotient by such an action — $T^n = \mathbb{R}^n/\mathbb{Z}^n$, $\mathbb{RP}^n = S^n / \{\pm 1\}$, $G/H$ for Lie groups when $H$ acts freely properly discontinuously — path lifting and homotopy lifting are available. The bridge: free + properly discontinuous → covering → lifting available.

The second source is **a local diffeomorphism with appropriate connectedness/properness**. A surjective local diffeomorphism between manifolds is a covering map *provided* the fibres are discrete and the map is proper (in the sense of preimages of compact sets being compact, equivalently the appropriate "finite-to-one" or "discrete-fibre" condition). So path lifting applies to many smooth-geometry situations that are not explicitly framed as covers.

The third source is **a finite-to-one étale-like map of smooth manifolds**. The universal-covering structure of a manifold's frame bundle (in the spin/orientation context), the regular covering of the configuration space by particle-labeled configurations, the covering of a moduli space by a parameter space — all admit lifting properties via the path-lifting theorem.

**Targets (Output Amplification)**

The conclusion gives a lift; combining with other tools amplifies into structural results.

The first combination is **with the simple connectedness of the source**: if $Y$ is simply connected, every map $f : Y \to X$ lifts through any covering $p : \tilde X \to X$ (given a starting fibre point). The combination "homotopy lifting + simply connected source" gives the full [[Thm - Lifting Criterion for Continuous Maps|lifting criterion]] in the easy direction. The non-obvious conclusion: simply-connected spaces "see" any cover as if it were trivial.

The second combination is **with the discreteness of the fibre**: a continuous map from $I$ to a discrete set $p^{-1}(x_0)$ is constant. So if the endpoint of a lifted homotopy $\tilde H(1, \cdot) : I \to p^{-1}(\gamma(1))$ is continuous and lands in the discrete fibre, it is constant. The combination "homotopy lifting + discrete fibre + continuity" gives homotopy invariance of monodromy — the engine of $\pi_1$-computations.

The third combination is **with the deck-transformation action**: any two lifts of the same map $f$ at the same point differ by a deck transformation (if the cover is regular and $Y$ is connected). Combining "lifting exists" with "lifts differ by deck" gives the monodromy action of $\pi_1$ on the fibre — the explicit isomorphism $\pi_1(X) \cong \mathrm{Deck}(\widetilde X / X)$ for the universal cover.

---

# Why Is It True

The intuition is **local triviality assembles into global lifting via compactness**.

**The bolded one-liner: a covering is locally a disjoint union of copies of the base, so locally lifting is just "choose a sheet"; compactness of $I$ (or $Y \times I$) lets you do this finitely many times, and the chosen-sheet condition propagates uniquely along the path.**

Concretely:

1. **Local lifting is automatic.** Near any point $x \in X$, there is an evenly covered neighbourhood $U$, with $p^{-1}(U) = \bigsqcup_\alpha \tilde U_\alpha$ a disjoint union of sheets. Once you specify which sheet you are on, the lift is forced (it is the local inverse of $p$ on that sheet). So locally, lifting is just "pick a sheet."

2. **Compactness chops the path into local pieces.** The image $\gamma(I)$ of the path is compact (continuous image of compact), so a finite collection of evenly covered neighbourhoods covers it. Subdividing $I$ accordingly, each subinterval maps into a single evenly covered neighbourhood. Lift one subinterval at a time, starting from the prescribed starting lift, and use the matching condition at each subdivision point to determine which sheet to use next. There is a *unique* choice at each step (matching the previous endpoint), so the lifted path is unique.

3. **Uniqueness propagates by connectedness.** Two continuous lifts that agree at one point must agree on a neighbourhood (because the lift is locally determined by the sheet), and the set of points where they agree is both open and closed, hence all of $I$.

4. **Homotopy lifting works the same way, in two parameters.** The image $H(Y \times I)$ is covered by evenly covered neighbourhoods; subdivide $Y \times I$ into small rectangles each lying in such a preimage; lift one rectangle at a time, using the previously-lifted edges to determine sheet choices. For general $Y$, you need a slightly more care (subdivide using a refinement of the cover); for $Y = I$ (as in the application to $\pi_1$), the proof is straightforward.

The whole theorem is **compactness + local triviality + uniqueness propagation** — three ingredients that combine into a powerful global statement.

---

# What Makes This Hard

The intuition is clear, but the proof has technical pitfalls. The first is the **Lebesgue number lemma**: to chop $I$ into pieces that each fit in an evenly covered neighbourhood, you need to know there is a uniform subdivision scale that works — this is the content of the Lebesgue number lemma (applied to the open cover $\{\gamma^{-1}(U_x)\}$ of compact $I$). People sometimes try to do this without the Lebesgue number, getting tangled in pointwise estimates. The second pitfall is **continuity across subdivisions**: each subinterval gives a lifted piece, and one must verify that the pieces glue continuously across subdivision points. The matching condition (the lift's value at the right endpoint of one piece equals its value at the left endpoint of the next) is what guarantees this — but if you fail to insist on the matching, the lift can be discontinuous. The third pitfall is **uniqueness via connectedness**: people often prove existence and forget to prove uniqueness, but the connectedness argument is what makes the lift *the* lift, not just *a* lift.

For homotopy lifting with general $Y$, the additional subtlety is that the lift must depend continuously on $Y$ as well — you cannot just lift each $\{y\} \times I$ independently and paste, because the resulting "lift" may not be jointly continuous in $(y, t)$. The correct argument uses a *uniform* covering and *simultaneous* subdivision.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use compactness of $I$ (or $Y \times I$ on compact $Y$) and the Lebesgue number lemma to chop the parameter space into small pieces, each mapping into a single evenly covered neighbourhood of $X$. Lift one piece at a time, using the local sheet structure of the cover and the matching condition from the previous piece. Uniqueness comes from open-closed propagation.

**Subgoal decomposition:**

1. **Local lift exists and is unique.** Given an evenly covered open $U \subseteq X$ and a starting lift $\tilde x_0 \in p^{-1}(U)$ over $x_0 \in U$, any continuous $\gamma : I \to U$ with $\gamma(0) = x_0$ lifts uniquely to a continuous $\tilde\gamma : I \to \tilde X$ with $\tilde\gamma(0) = \tilde x_0$.
   - *Hint:* $\tilde x_0$ lies in a unique sheet $\tilde U_\alpha$; the lift is $\tilde\gamma = (p|_{\tilde U_\alpha})^{-1} \circ \gamma$.
   - *Why needed:* This is the base case for lifting on evenly covered pieces.

2. **Compactness gives a finite subdivision.** Cover $\gamma(I)$ by evenly covered neighbourhoods $U_1, \dots, U_N$. By the Lebesgue number lemma applied to the cover $\{\gamma^{-1}(U_j)\}$ of compact $I$, find $\delta > 0$ such that any subinterval of length $< \delta$ maps into a single $U_j$.
   - *Hint:* Standard Lebesgue number lemma argument.
   - *Why needed:* Enables a finite-step lifting procedure.

3. **Glue local lifts.** Subdivide $I$ as $0 = t_0 < \cdots < t_k = 1$ with $t_{i+1} - t_i < \delta$. Inductively lift on $[0, t_{i+1}]$ using the local-lift step and the matching condition $\tilde\gamma(t_i)$ as the starting point for the next piece.
   - *Hint:* Continuity at each $t_i$ follows because $\tilde\gamma|_{[t_{i-1}, t_i]}$ and $\tilde\gamma|_{[t_i, t_{i+1}]}$ both have $\tilde\gamma(t_i)$ as their endpoint.
   - *Why needed:* Builds the global lift from the local ones.

4. **Uniqueness via open-closed propagation.** If $\tilde\gamma_1, \tilde\gamma_2$ are two lifts with $\tilde\gamma_1(0) = \tilde\gamma_2(0)$, then $\{t : \tilde\gamma_1(t) = \tilde\gamma_2(t)\}$ is non-empty, open (lifts agree on the same sheet near any point of agreement), and closed (preimage of the diagonal under continuous map). By connectedness of $I$, the set is all of $I$.
   - *Hint:* Open because of sheet-discreteness; closed because of continuity.
   - *Why needed:* Uniqueness of the lift.

5. **Homotopy lifting via 2D subdivision.** Same strategy in two parameters. Chop $Y \times I$ (or $I \times I$ for path-homotopies) into small enough rectangles each mapping into a single evenly covered $U_j$. Lift rectangle-by-rectangle, using the already-lifted edges (left and bottom) to determine which sheet to use.
   - *Hint:* For $Y = I$, the picture is a grid of squares.
   - *Why needed:* Provides homotopy invariance of all $\pi_1$-related invariants.

---

# Lemma Decomposition

> [!note]- Lemma 1: Lift exists uniquely on an evenly covered piece
> **Statement:** If $U \subseteq X$ is evenly covered, $x_0 \in U$, $\tilde x_0 \in p^{-1}(x_0)$, and $\gamma : I \to U$ is continuous with $\gamma(0) = x_0$, then there is a unique continuous $\tilde\gamma : I \to \tilde X$ with $p \circ \tilde\gamma = \gamma$, $\tilde\gamma(0) = \tilde x_0$.
>
> **Hint:** $\tilde x_0$ lies in a unique sheet $\tilde U_\alpha$ of $p^{-1}(U)$. The restriction $p|_{\tilde U_\alpha} : \tilde U_\alpha \to U$ is a homeomorphism; its inverse provides the lift.
>
> **Why needed:** Base case for assembling global lifts via subdivision.
>
> > [!note]- Full proof
> > Since $U$ is evenly covered, $p^{-1}(U) = \bigsqcup_\alpha \tilde U_\alpha$ with each $p|_{\tilde U_\alpha}$ a homeomorphism. The point $\tilde x_0$ lies in *exactly one* component, say $\tilde U_{\alpha_0}$. Define $\tilde\gamma(s) := (p|_{\tilde U_{\alpha_0}})^{-1}(\gamma(s))$ for all $s \in I$. This is continuous (composition of continuous maps), $p \circ \tilde\gamma = \gamma$, and $\tilde\gamma(0) = (p|_{\tilde U_{\alpha_0}})^{-1}(x_0) = \tilde x_0$.
> >
> > Uniqueness: any continuous lift $\tilde\gamma'$ with $\tilde\gamma'(0) = \tilde x_0$ must have $\tilde\gamma'(I) \subseteq$ the connected component of $p^{-1}(U)$ containing $\tilde x_0$, which is $\tilde U_{\alpha_0}$. (Otherwise it would jump between disjoint open sheets, contradicting continuity of a path on the connected $I$.) So $\tilde\gamma' = (p|_{\tilde U_{\alpha_0}})^{-1} \circ \gamma = \tilde\gamma$.

> [!note]- Lemma 2: Lebesgue subdivision of a compact path
> **Statement:** Let $\gamma : I \to X$ be continuous and let $\{U_j\}$ be an open cover of $\gamma(I)$. There exists $\delta > 0$ and a subdivision $0 = t_0 < t_1 < \cdots < t_k = 1$ with $t_{i+1} - t_i < \delta$ such that $\gamma([t_i, t_{i+1}]) \subseteq U_{j(i)}$ for some $j(i)$.
>
> **Hint:** Apply the Lebesgue number lemma to the open cover $\{\gamma^{-1}(U_j)\}$ of compact $I$.
>
> **Why needed:** Makes the inductive lifting procedure work.
>
> > [!note]- Full proof
> > $\{\gamma^{-1}(U_j)\}$ is an open cover of $I$ (preimages of open sets). $I$ is compact, so the **Lebesgue number lemma** gives $\delta > 0$ such that every subset of $I$ of diameter $< \delta$ is contained in some $\gamma^{-1}(U_j)$. Pick any subdivision $0 = t_0 < t_1 < \cdots < t_k = 1$ with $t_{i+1} - t_i < \delta$ (always possible for $k$ large enough). Each $[t_i, t_{i+1}]$ has diameter $< \delta$, hence lies in some $\gamma^{-1}(U_{j(i)})$, hence $\gamma([t_i, t_{i+1}]) \subseteq U_{j(i)}$.

> [!note]- Lemma 3: Inductive gluing of local lifts
> **Statement:** With the subdivision from Lemma 2 and a starting lift $\tilde x_0 \in p^{-1}(\gamma(0))$, the unique-local-lift construction iteratively gives a continuous global lift $\tilde\gamma : I \to \tilde X$.
>
> **Hint:** Use Lemma 1 on each subinterval, with the starting lift on the $(i+1)$-th subinterval being the endpoint of the lift on the $i$-th subinterval.
>
> **Why needed:** Builds the global lift; provides existence in the main theorem.
>
> > [!note]- Full proof
> > Set $\tilde\gamma(t_0) := \tilde x_0$. Inductively: on the subinterval $[t_i, t_{i+1}]$, the path $\gamma|_{[t_i, t_{i+1}]}$ lies in $U_{j(i)}$ (evenly covered) and starts at $\gamma(t_i)$, whose lift $\tilde\gamma(t_i)$ has been defined. By Lemma 1 applied to $U_{j(i)}$, $\gamma(t_i)$, and $\tilde\gamma(t_i)$, there is a unique lift $\tilde\gamma|_{[t_i, t_{i+1}]}$ of $\gamma|_{[t_i, t_{i+1}]}$ with $\tilde\gamma|_{[t_i, t_{i+1}]}(t_i) = \tilde\gamma(t_i)$. The endpoint $\tilde\gamma(t_{i+1})$ is well-defined.
> >
> > The pieces glue continuously: at each $t_i$, both the $i$-th and the $(i+1)$-th piece agree on the value $\tilde\gamma(t_i)$, so $\tilde\gamma$ is continuous on $I$ by the pasting lemma.

> [!note]- Lemma 4: Uniqueness via connectedness
> **Statement:** Let $p : \tilde X \to X$ be a covering, $Y$ connected, $f : Y \to X$ continuous, $\tilde f_1, \tilde f_2 : Y \to \tilde X$ two continuous lifts of $f$ agreeing at one point $y_0$. Then $\tilde f_1 = \tilde f_2$.
>
> **Hint:** The set $A = \{y : \tilde f_1(y) = \tilde f_2(y)\}$ is non-empty, open (locally on each evenly covered preimage), and closed (preimage of diagonal). By connectedness, $A = Y$.
>
> **Why needed:** Uniqueness of the lift, completing the path lifting theorem.
>
> > [!note]- Full proof
> > $A = \{y \in Y : \tilde f_1(y) = \tilde f_2(y)\}$ is non-empty ($y_0 \in A$).
> >
> > $A$ is open: for $y \in A$, let $U$ be an evenly covered neighbourhood of $f(y)$; let $\tilde U_\alpha$ be the sheet containing $\tilde f_1(y) = \tilde f_2(y)$. By continuity of $\tilde f_1, \tilde f_2$, there is a neighbourhood $V$ of $y$ with $\tilde f_1(V), \tilde f_2(V) \subseteq \tilde U_\alpha$. On $V$, both lifts agree with $(p|_{\tilde U_\alpha})^{-1} \circ f$, hence agree.
> >
> > $A$ is closed: $A = \Delta_{\tilde X} \cap (\tilde f_1 \times \tilde f_2)^{-1}(\Delta_{\tilde X})$... more carefully, $A$ is the preimage of the diagonal in $\tilde X \times \tilde X$ under $(\tilde f_1, \tilde f_2) : Y \to \tilde X \times \tilde X$. Wait — actually the diagonal is closed iff $\tilde X$ is Hausdorff, which we assume. So $A$ is closed.
> >
> > $Y$ connected, $A$ non-empty open and closed, hence $A = Y$.

> [!note]- Lemma 5: Homotopy lifting (sketch for $Y = I$ case)
> **Statement:** A continuous $H : I \times I \to X$ with a continuous starting lift $\tilde H_0 : I \to \tilde X$ of $H|_{I \times \{0\}}$ lifts uniquely to $\tilde H : I \times I \to \tilde X$ with $\tilde H|_{I \times \{0\}} = \tilde H_0$.
>
> **Hint:** Apply Lemma 3 in two dimensions: subdivide $I \times I$ into small squares, lift one square at a time, using already-lifted edges for matching.
>
> **Why needed:** Homotopy invariance of monodromy and $\pi_1$-invariants.
>
> > [!note]- Full proof (sketch)
> > Cover $H(I \times I)$ by evenly covered neighbourhoods $U_j$. By Lebesgue applied to compact $I \times I$, subdivide as $0 = s_0 < s_1 < \cdots < s_m = 1$ and $0 = t_0 < t_1 < \cdots < t_n = 1$ such that each $[s_i, s_{i+1}] \times [t_j, t_{j+1}]$ maps into a single $U_{k(i,j)}$. Lift bottom-row squares using the prescribed bottom lift $\tilde H_0$ (each square has a left edge already lifted from the previous square in the row, after the first; the first square uses $\tilde H_0$). For each subsequent row, lift using the already-lifted bottom edge of each square (which is the top edge of the square below). Uniqueness from Lemma 4 ensures all sheet choices are consistent. Continuity follows from gluing.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem (Path Lifting).** Let $p : \tilde X \to X$ be a covering, $\gamma : I \to X$ continuous, $\tilde x_0 \in p^{-1}(\gamma(0))$. There exists a unique continuous $\tilde\gamma : I \to \tilde X$ with $p \circ \tilde\gamma = \gamma$ and $\tilde\gamma(0) = \tilde x_0$.
>
> *Proof.*
>
> **Existence.** Cover $\gamma(I)$ (compact) by finitely many evenly covered open sets $U_1, \dots, U_N$. By Lemma 2, find $\delta > 0$ and a subdivision $0 = t_0 < t_1 < \cdots < t_k = 1$ with $t_{i+1} - t_i < \delta$, so each $\gamma([t_i, t_{i+1}])$ lies in some $U_{j(i)}$. By Lemma 3, define $\tilde\gamma$ piecewise using Lemma 1 on each subinterval, starting from $\tilde\gamma(t_0) = \tilde x_0$ and using the endpoint of each piece as the starting lift for the next. The result is continuous.
>
> **Uniqueness.** Apply Lemma 4 to $Y = I$ (connected) and the two lifts.
>
> **Theorem (Homotopy Lifting).** With $H : Y \times I \to X$ and $\tilde H_0$, the lift $\tilde H$ exists uniquely.
>
> *Proof.* (For $Y = I$, the case used in $\pi_1$ theory.) Lemma 5. The general $Y$ case follows by a more delicate version of the same subdivision argument; the key ingredients are the same.
>
> $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Number theory: lifting paths in the upper half-plane for modular forms.** The action of $\mathrm{SL}_2(\mathbb{Z})$ on the upper half-plane $\mathbb{H}^2$ is properly discontinuous with quotient the **modular curve** $\mathbb{H}^2 / \mathrm{SL}_2(\mathbb{Z})$ — almost a covering (some points have non-trivial stabilisers, so it is a "branched cover"). Paths in the modular curve lift to paths in $\mathbb{H}^2$ once a starting fibre point is chosen, and the lift's endpoint records the modular transformation. This is a foundational ingredient in the theory of modular forms.

**Differential equations: lifting solutions through covering maps of phase spaces.** Consider a smooth dynamical system on $X$ with a covering $\tilde X \to X$; solutions on $X$ (continuous curves $\gamma : \mathbb{R} \to X$) lift to solutions on $\tilde X$ once an initial fibre point is chosen. This is used in the analysis of dynamical systems on quotient spaces (e.g., billiards on rational triangles via covers).

**Physics: lifting paths in configuration space to phase space.** In classical mechanics on a configuration manifold $Q$, the phase space is $T^*Q$ (cotangent bundle). For a non-orientable $Q$, the orientation cover $\widetilde Q^{\mathrm{or}}$ provides a "doubled" configuration space, and quantum mechanical wavefunctions can sometimes only be defined on the cover (the orientation-reversing loop creates a sign ambiguity). The path-lifting theorem ensures this construction is well-defined.

**Robotics: lifting paths in configuration space of articulated mechanisms.** A robot arm's configuration space is sometimes a non-trivial manifold (e.g., $\mathrm{SO}(3)$ for a single joint). Lifting paths through $\mathrm{SU}(2) \to \mathrm{SO}(3)$ provides a "double-cover representation" used in some control algorithms — the lifted path on $\mathrm{SU}(2)$ avoids the antipodal singularity present on $\mathrm{SO}(3)$.

---

# Bridges

- **[[Def - Covering Space]]** — this theorem is the foundational property of a covering map. Without lifting, the local-triviality structure of a cover is useful only locally; lifting promotes it to a global theory. Path lifting is the simplest consequence of even-covering; homotopy lifting is the deeper consequence that involves both the cover structure and the homotopy parameter.

- **[[Thm - Lifting Criterion for Continuous Maps]]** — the generalisation from "any path lifts" to "any continuous map from a sufficiently nice space lifts iff a $\pi_1$-subgroup inclusion holds." Path lifting is the special case where the domain is $I$ (which has trivial $\pi_1$, so the subgroup inclusion is automatic). Homotopy lifting with domain $I^2$ is the special case where the domain is contractible. The general lifting criterion uses both as input.

- **[[Thm - Pi_1 of S^1 is Z]]** — the prototypical application. Path lifting defines the winding number; homotopy lifting makes it homotopy-invariant; homomorphism property follows from the explicit form of lifts of concatenated paths. Every step of the $\pi_1(S^1) = \mathbb{Z}$ computation is path/homotopy lifting in action.

- **Monodromy and the action of $\pi_1$ on fibres** — the homotopy lifting theorem says that lifting a loop $\gamma$ at $x_0$ gives a path from $\tilde x_0$ to some other point $\tilde x_1$ in the same fibre, and this point depends *only* on the homotopy class of $\gamma$ (by homotopy invariance). So $\pi_1(X, x_0)$ acts on $p^{-1}(x_0)$ via $[\gamma] \cdot \tilde x_0 := \tilde\gamma(1)$. This is the **monodromy action**, central to the [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]] and to the identification of $\pi_1$ with the deck group of the universal cover.

- **The Serre fibration** — a generalisation of "covering map" to spaces where the fibres can be more complex. A **Serre fibration** is a map $p : E \to B$ satisfying the **homotopy lifting property** with respect to disc inclusions $D^n \times \{0\} \hookrightarrow D^n \times I$. Coverings are the special case where the fibres are discrete; general Serre fibrations include vector bundles, Hurewicz fibrations, and more. Most of homotopy theory rests on the homotopy lifting property in this more general form.
