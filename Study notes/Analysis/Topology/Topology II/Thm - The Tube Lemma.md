---
type: theorem
subject: topology
prereqs:
  - "Def - Compact Space"
  - "Def - Topological Space"
  - "Def - Continuous Map"
tags: [analysis, topology, compactness, products]
---

# Notation

$X, Y$ are topological spaces. The **product** $X \times Y$ has the [[Def - Subspace Topology|product topology]]: a base is given by *boxes* $U \times V$ with $U$ open in $X$ and $V$ open in $Y$. The **slice** $\{x_0\} \times Y \subseteq X \times Y$ is the fiber over a point $x_0 \in X$, homeomorphic to $Y$. A **tube** around a slice is a set of the form $U \times Y$ for an open $U \subseteq X$. The full registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Tube Lemma.** Let $X, Y$ be topological spaces with $Y$ **compact**. Suppose $N \subseteq X \times Y$ is an open set containing the slice $\{x_0\} \times Y$ over a point $x_0 \in X$:
> $$\{x_0\} \times Y \subseteq N.$$
> Then there exists an open neighborhood $U \subseteq X$ of $x_0$ such that the *tube* $U \times Y$ is contained in $N$:
> $$U \times Y \subseteq N.$$

The lemma says that an open set containing a fiber over a compact factor always contains a "tube" — an open set in the form of an "extruded slice" with thickness equal to a neighborhood of the base point.

---

# Motivation

The Tube Lemma is the *technical engine* of the finite-product case of Tychonoff's theorem. It is what lets one conclude "product of compacts is compact" from "each factor is compact" without invoking the axiom of choice (the finite case is choice-free; the infinite case is equivalent to AC).

The question the lemma answers is: *what is the structure of an open neighborhood of a compact fiber in a product*? The answer is: it always contains a tube. This is a *compactness-driven thickening* result: although the open set $N$ may be a complicated union of boxes, its intersection with the slice $\{x_0\} \times Y$ is open in the slice, and compactness of $Y$ lets us "thicken" this slice-open into a true open neighborhood of the slice that is *cylindrical* (a tube $U \times Y$).

The geometric picture: $N$ is an open set in $X \times Y$ touching the slice $\{x_0\} \times Y$ in a complicated way. Each *vertical line* $\{x\} \times Y$ through nearby $x$ may have a different intersection with $N$. The lemma asserts that for $x$ near enough to $x_0$, the *entire* vertical line $\{x\} \times Y$ is inside $N$. So the "set of $x$ such that the full vertical line is in $N$" is open and contains $x_0$.

The proof is the workhorse demonstration of compactness in product spaces:

1. Cover the slice $\{x_0\} \times Y$ by box-shaped basis elements inside $N$.
2. Each box has the form $U_i \times V_i$ with $U_i \ni x_0$.
3. Since $\{x_0\} \times Y$ is homeomorphic to $Y$ (compact), the box-cover has a finite subcover via compactness.
4. Intersect the finitely many $U_i$ over $X$: $U = U_1 \cap \cdots \cap U_n$ is an open neighborhood of $x_0$.
5. For any $x \in U$ and any $y \in Y$, $y$ is in some $V_i$ (finite cover of $Y$), and $x$ is in the corresponding $U_i \supseteq U$, so $(x, y) \in U_i \times V_i \subseteq N$. Hence $U \times Y \subseteq N$.

This is the "intersect-and-project" pattern that recurs throughout compactness theory: a finite subcover of a compact set, intersected on one side and projected on the other, gives a global structural result.

The Tube Lemma also has independent significance beyond Tychonoff. It is what lets one **continuity-pass to slices**: a function continuous on $X \times Y$ at $(x_0, y_0)$ has continuity in $x$ that is uniform over $y$ when $Y$ is compact. This is the engine of every "compact-fiber" theorem in analysis: parameter-dependent integrals, semi-continuity of supremum-over-compact, the theory of holomorphic functions of several variables.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$Y$ compact, $N$ open containing the slice".

The first disguised source is **a closed graph on a compact fiber**. Property $B$: $f : X \to Y$ continuous, $Y$ compact, $N$ the complement of the graph in some neighborhood. The bridge: if $N$ contains a slice, the tube lemma gives a tube. *Example:* used in proving that continuous maps to Hausdorff spaces have closed graph.

The second disguised source is **$Y = [a, b]$ or any compact metric interval**. Property $B$: $Y$ compact metric. The bridge: direct. *Example:* in calculus, $Y = [a, b]$ is the standard compact factor; the tube lemma underlies the differentiation-under-the-integral-sign theorems.

The third disguised source is **$\{x_0\} \times Y$ is compact in $X \times Y$**. Property $B$: any compact subset of the form $\{x_0\} \times K$ for compact $K \subseteq Y$. The bridge: the same proof generalizes — the lemma holds for any compact slice, not just the full fiber. *Example:* the tube lemma can be generalized to: if $C \subseteq Y$ is compact and $\{x_0\} \times C \subseteq N$ open, then $U \times C \subseteq N$ for some neighborhood $U$ of $x_0$.

**Targets (Output Amplification)**

The conclusion is "a tube $U \times Y \subseteq N$ exists".

Combine the conclusion with **a finite product of compact factors**. Property $D$: a product $X = X_1 \times \cdots \times X_n$ where one wants to prove compactness inductively. Amplified result $E$: by iterating the tube lemma, every open cover of the product has a finite subcover. *Example:* this is the finite-case Tychonoff proof (Bredon 8.4–8.5). The argument: for each $x_0 \in X_1$, the slice $\{x_0\} \times X_2$ is covered by finitely many boxes; the tube lemma gives a tube around the slice in $X_1 \times X_2$; covering $X_1$ by finitely many such tubes gives a finite subcover of $X_1 \times X_2$.

Combine the conclusion with **a parameter-dependent compact set**. Property $D$: a map $\phi : X \to \mathcal{P}(Y)$ where $\phi(x)$ is compact for each $x$ and the function "is in $\phi(x)$" is continuous in $x$. Amplified result $E$: compactness propagates uniformly in $x$, by tube-lemma arguments applied to compact slices. *Example:* compactness of the family of orbits of a continuous dynamical system on a compact phase space.

Combine the conclusion with **the closed-graph property of a continuous function on a compact space**. Property $D$: $f : X \to Y$ continuous, $X$ compact (or $Y$ compact). Amplified result $E$: the graph of $f$ is closed in $X \times Y$, and complement-of-graph contains tubes around each fiber, giving the locally-uniform continuity of $f$. *Example:* the Heine theorem — continuous functions on compact metric spaces are uniformly continuous — is essentially this in metric clothing.

---

# Why Is It True

The proof is "cover the slice with boxes, finitize via compactness, intersect on the base side". Each step has clean geometric content.

**Step 1: Cover the slice with boxes inside $N$.** The slice $\{x_0\} \times Y$ is in the open $N$. The product topology has the box-basis: every open set is a union of boxes $U_i \times V_i$. For each point $(x_0, y) \in \{x_0\} \times Y$, there is a box $U \times V \subseteq N$ with $x_0 \in U$ and $y \in V$. So $\{x_0\} \times Y$ is covered by such boxes — say, indexed by $\alpha$: each $\alpha$ gives a box $U_\alpha \times V_\alpha \subseteq N$ with $x_0 \in U_\alpha$.

**Step 2: Use compactness of $Y$ to finitize.** The slice $\{x_0\} \times Y$ is homeomorphic to $Y$ (the projection $\pi_Y$ restricted to the slice is a homeomorphism). So $\{x_0\} \times Y$ is compact. The boxes restricted to the slice — i.e., $V_\alpha$ inside $Y$ — form an open cover of $Y$. By compactness of $Y$, extract a finite subcover: $V_{\alpha_1}, \ldots, V_{\alpha_n}$ cover $Y$.

**Step 3: Intersect on the $X$-side.** The corresponding $U_{\alpha_i}$ are open neighborhoods of $x_0$ in $X$. Their intersection $U = U_{\alpha_1} \cap \cdots \cap U_{\alpha_n}$ is *finite*, hence open, and contains $x_0$.

**Step 4: Verify the tube $U \times Y$ is in $N$.** For any $(x, y) \in U \times Y$: $y \in V_{\alpha_i}$ for some $i$ (finite cover of $Y$), and $x \in U \subseteq U_{\alpha_i}$, so $(x, y) \in U_{\alpha_i} \times V_{\alpha_i} \subseteq N$. So $U \times Y \subseteq N$.

The geometric picture: think of $X \times Y$ as a (possibly infinite-dimensional) rectangle, with the slice $\{x_0\} \times Y$ as a vertical line through $x_0$. The open set $N$ is a "blob" that surrounds the line. As $y$ varies along the line, $N$ has some local thickness in the $X$-direction near each $y$ — given by the $U_\alpha$ in the box at that $y$. The thicknesses $U_\alpha$ all contain $x_0$, but might be very thin for some $y$.

If the thicknesses *vary continuously* in $y$, one might worry that the intersection of all $U_\alpha$ (as $y$ ranges over $Y$) is empty — the "tube" would have zero width. The compactness of $Y$ rescues this: finitely many $y$'s suffice to cover, and the intersection of *finitely many* open thicknesses is still open and contains $x_0$.

Without compactness, this fails. *Example of failure when $Y$ is not compact:* let $X = Y = \mathbb{R}$, and $N = \{(x, y) : |x| < e^{-y^2}\}$, an open set containing the slice $\{0\} \times \mathbb{R}$. As $y \to \pm\infty$, the "thickness" of $N$ in the $X$-direction shrinks to zero. Any tube $U \times \mathbb{R}$ with $U \ni 0$ open must contain points $(x, y)$ with $x > e^{-y^2}$ for $y$ large enough, so $U \times \mathbb{R} \not\subseteq N$. The tube lemma fails because $\mathbb{R}$ is not compact: the slice is "infinitely long" and the thickness has nowhere to converge to a uniform bound.

---

# What Makes This Hard

The non-obvious step is the **intersect-and-project**: cover the slice by boxes, extract a finite subcover *of the $Y$-projections* using compactness of $Y$, then *intersect the corresponding $X$-projections* over $X$ to get the tube's base $U$. The "$Y$ side gets finitized, $X$ side gets intersected" duality is the key combinatorial move. The most common error is to attempt to apply compactness of $Y$ to the full open cover of $X \times Y$ rather than to the projected cover of $Y$ — which fails because $X \times Y$ may not be compact. A second pitfall is to forget that the lemma genuinely requires *compactness of $Y$* — the failure example $N = \{|x| < e^{-y^2}\}$ shows that without compactness of $Y$, the tube lemma is false.

---

# Rederivation Scaffold

**High-level strategy:**
Cover the slice $\{x_0\} \times Y$ by box-basis elements inside $N$, with each box of the form $U_\alpha \times V_\alpha$ where $x_0 \in U_\alpha$. The $V_\alpha$ cover $Y$; compactness of $Y$ gives a finite subcover $V_{\alpha_1}, \ldots, V_{\alpha_n}$. Set $U = U_{\alpha_1} \cap \cdots \cap U_{\alpha_n}$. For any $(x, y) \in U \times Y$, $y \in V_{\alpha_i}$ for some $i$, and $x \in U \subseteq U_{\alpha_i}$, so $(x, y) \in U_{\alpha_i} \times V_{\alpha_i} \subseteq N$.

**Subgoal decomposition:**

1. **Cover the slice by boxes inside $N$.** For each $y \in Y$, $(x_0, y) \in N$ open; the product topology has box-basis, so $(x_0, y) \in U_y \times V_y \subseteq N$ for some open $U_y \ni x_0$, $V_y \ni y$.
   - *Hint:* Product topology has box basis.
   - *Why needed:* It puts the slice in a form where the $Y$-projection is amenable to compactness.

2. **The $V_y$ cover $Y$.** Each $V_y \ni y$, so $\{V_y\}_{y \in Y}$ is an open cover of $Y$.

3. **Extract a finite subcover of $Y$.** By compactness of $Y$: $Y = V_{y_1} \cup \cdots \cup V_{y_n}$.
   - *Hint:* Definition of compactness applied to $Y$.

4. **Intersect the corresponding $U_{y_i}$.** $U = U_{y_1} \cap \cdots \cap U_{y_n}$ is open (finite intersection), contains $x_0$.

5. **Verify $U \times Y \subseteq N$.** For $(x, y) \in U \times Y$: $y \in V_{y_i}$ for some $i$ (finite cover), $x \in U \subseteq U_{y_i}$, so $(x, y) \in U_{y_i} \times V_{y_i} \subseteq N$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Box-basis covering of the slice
> **Statement:** Let $N$ be open in $X \times Y$ with $\{x_0\} \times Y \subseteq N$. For each $y \in Y$, there is a box $U_y \times V_y$ with $x_0 \in U_y$, $y \in V_y$, $U_y \times V_y \subseteq N$.
>
> **Hint:** Product topology has box basis; $(x_0, y) \in N$ means there is a box around $(x_0, y)$ in $N$.
>
> **Why needed:** It is the box-cover construction.
>
> > [!note]- Full proof
> > The product topology on $X \times Y$ has the boxes $U \times V$ (with $U \subseteq X$ open, $V \subseteq Y$ open) as a basis. Hence every open set is a union of boxes. In particular, $N$ open and $(x_0, y) \in N$ means there is a box $U_y \times V_y \subseteq N$ with $(x_0, y) \in U_y \times V_y$. So $x_0 \in U_y, y \in V_y$, and the box is inside $N$.

> [!note]- Lemma 2: The slice is homeomorphic to $Y$, hence compact
> **Statement:** $\{x_0\} \times Y$ with the subspace topology from $X \times Y$ is homeomorphic to $Y$, via the projection $\pi_Y$.
>
> **Hint:** Projection is continuous; the inclusion $y \mapsto (x_0, y)$ is continuous; mutual inverses.
>
> **Why needed:** It lets us apply compactness of $Y$ to the slice.
>
> > [!note]- Full proof
> > Define $\iota : Y \to X \times Y$ by $\iota(y) = (x_0, y)$. $\iota$ is continuous (each component is: the first is constant $x_0$, the second is identity). $\iota$ is injective (by structure) and has image $\{x_0\} \times Y$.
> >
> > The inverse $\pi_Y |_{\{x_0\} \times Y} : \{x_0\} \times Y \to Y$, $(x_0, y) \mapsto y$, is the restriction of the projection $\pi_Y$, which is continuous in the product topology. It is the inverse of $\iota$. Hence $\iota$ is a homeomorphism onto its image.
> >
> > In particular, $\{x_0\} \times Y$ is compact iff $Y$ is compact. Since $Y$ is compact, so is the slice.

> [!note]- Lemma 3: Finite subcover gives the tube
> **Statement:** Let $Y = V_{y_1} \cup \cdots \cup V_{y_n}$ (finite cover) and let $U_{y_i} \times V_{y_i} \subseteq N$ for each $i$. Then $U = \bigcap_{i=1}^n U_{y_i}$ is open, contains $x_0$, and $U \times Y \subseteq N$.
>
> **Hint:** For each $(x, y) \in U \times Y$, find $i$ with $y \in V_{y_i}$, use $x \in U \subseteq U_{y_i}$.
>
> **Why needed:** It is the tube construction.
>
> > [!note]- Full proof
> > $U$ is open: finite intersection of opens. $x_0 \in U$: $x_0 \in U_{y_i}$ for each $i$.
> >
> > For any $(x, y) \in U \times Y$: by the finite cover of $Y$, $y \in V_{y_i}$ for some $i$. And $x \in U = \bigcap_j U_{y_j} \subseteq U_{y_i}$. So $(x, y) \in U_{y_i} \times V_{y_i} \subseteq N$. Hence $U \times Y \subseteq N$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> Let $X, Y$ be topological spaces with $Y$ compact, $x_0 \in X$, and $N \subseteq X \times Y$ open with $\{x_0\} \times Y \subseteq N$.
>
> By Lemma 1, for each $y \in Y$, choose a box $U_y \times V_y \subseteq N$ with $x_0 \in U_y, y \in V_y$.
>
> The family $\{V_y\}_{y \in Y}$ is an open cover of $Y$. By Lemma 2, $Y$ is compact (and equivalently the slice $\{x_0\} \times Y$ is compact); by compactness of $Y$, extract a finite subcover $Y = V_{y_1} \cup \cdots \cup V_{y_n}$.
>
> By Lemma 3, $U = U_{y_1} \cap \cdots \cap U_{y_n}$ is open, contains $x_0$, and $U \times Y \subseteq N$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Finite Tychonoff via the Tube Lemma.** Iterating the tube lemma proves the finite case of Tychonoff's theorem: if $X_1, \ldots, X_n$ are compact, then $X_1 \times \cdots \times X_n$ is compact. Argument: cover $X_1 \times X_2$ by opens; for each $x_0 \in X_1$, the slice $\{x_0\} \times X_2$ is compact (homeomorphic to $X_2$), so has a finite subcover; by the tube lemma, this finite subcover extends to a tube $U(x_0) \times X_2$; the family $\{U(x_0)\}_{x_0 \in X_1}$ covers $X_1$, which is compact, so has a finite subcover; assembling, the original cover of $X_1 \times X_2$ has a finite subcover. Inductively, $X_1 \times \cdots \times X_n$ is compact. The application is the cleanest one and explains why the Tube Lemma is the technical engine.

**Continuity of integrals dependent on a parameter.** Let $f : X \times [a, b] \to \mathbb{R}$ be continuous, with $[a, b]$ compact. Define $F(x) = \int_a^b f(x, t) \, dt$. Then $F$ is continuous. The proof uses the tube lemma: for any $\epsilon > 0$ and any $x_0$, the set $N = \{(x, t) : |f(x, t) - f(x_0, t)| < \epsilon/(b-a)\}$ contains the slice $\{x_0\} \times [a, b]$ (by continuity at each $(x_0, t)$); the tube lemma gives a neighborhood $U$ of $x_0$ with $U \times [a, b] \subseteq N$; hence $|F(x) - F(x_0)| < \epsilon$ for $x \in U$. The application is the continuity of integrals over compact parameter sets, the topological foundation of differentiation under the integral sign and related parameter-dependent constructions.

**Uniform continuity on compact spaces.** A continuous function $f : X \to Y$ between metric spaces is uniformly continuous if $X$ is compact. The proof uses a tube-lemma-style argument on $X \times X$ applied to the continuity-witnessing open set $N = \{(x, x') : d_Y(f(x), f(x')) < \epsilon\}$ around the diagonal. Compactness of one factor (or in fact of the diagonal $\Delta \subseteq X \times X$) gives a uniform thickness $\delta$ for which $d_X(x, x') < \delta \Rightarrow d_Y(f(x), f(x')) < \epsilon$. This is the Heine–Cantor theorem, a standard real-analysis result.

**Continuity of holomorphic functions in several variables.** A function $f : U \times V \to \mathbb{C}$ holomorphic in $(z, w)$ with $V$ compact has continuity in $z$ that is uniform in $w$, by tube-lemma applied to the compact factor $V$. This underlies the local-uniform-convergence arguments in multi-variable complex analysis.

---

# Bridges

- **[[Thm - Continuous Image of a Compact Space]]** — the slice $\{x_0\} \times Y$ is the continuous image of $Y$ under the inclusion $y \mapsto (x_0, y)$. Compactness of the slice descends from compactness of $Y$.

- **[[Def - Compact Space]]** — the definition used. The tube lemma is the basic compactness argument in product spaces.

- **Tychonoff's theorem (finite case)** — direct consequence by iteration. The infinite case requires the axiom of choice and a different proof technique (universal nets, see [[Thm - Every Net Has a Universal Subnet]]).

- **Heine–Cantor theorem (uniform continuity on compact)** — a tube-lemma-style argument applied to the diagonal.

- **Continuity of integrals over compact parameter sets** — direct application.

---

# Unlocked by This

> [!tip] **Tychonoff's Finite Product Theorem** *(from Topology II)*
> The product of finitely many compact spaces is compact. Proof by iterated tube-lemma. The arbitrary-index version requires the axiom of choice and a different proof via universal nets.

> [!tip] **Continuity of Parameter Integrals** *(from Real Analysis)*
> $F(x) = \int_a^b f(x, t) \, dt$ is continuous when $f$ is continuous and $[a, b]$ is compact. Tube lemma gives the uniformity needed.

> [!tip] **Heine–Cantor Theorem** *(from Real Analysis)*
> Continuous functions on compact metric spaces are uniformly continuous. Proof: tube-lemma style argument on $X \times X$ around the diagonal.

> [!tip] **Closed-Graph Theorem and Banach Open Mapping Theorem Analogs** *(from Functional Analysis)*
> Compactness of fibers underlies many closed-graph and open-mapping theorems in functional analysis. The tube lemma is the foundational topological input.

> [!tip] **Local Triviality of Fiber Bundles** *(from Differential Geometry)*
> A **fiber bundle** with compact fiber is locally trivial: every point of the base has a neighborhood over which the bundle is a product. The proof uses tube-lemma-style arguments to extend local sections over the compact fiber to a neighborhood in the base.
