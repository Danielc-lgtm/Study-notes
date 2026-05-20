---
type: theorem
subject: topology
prereqs:
  - "Def - Metric Space"
  - "Def - Compact Space"
  - "Thm - Compactness in Metric Spaces (Three Equivalents)"
tags: [analysis, topology]
---

# Notation

$(X, d)$ is a compact metric space. $\{U_\alpha\}_{\alpha \in A}$ is an open cover of $X$. $\operatorname{diam}(A) = \sup\{d(p, q) : p, q \in A\}$ is the diameter of a subset $A$. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Statement

> **Lebesgue Number Lemma.** Let $(X, d)$ be a compact metric space and let $\{U_\alpha\}_{\alpha \in A}$ be an open cover of $X$. Then there exists $\delta > 0$, called a **Lebesgue number** for the cover, such that:
>
> $$\forall A \subseteq X \text{ with } \operatorname{diam}(A) < \delta, \quad \exists \alpha \in A : A \subseteq U_\alpha.$$
>
> In words: every subset of $X$ of diameter less than $\delta$ is contained in some single cover element.

---

# Motivation

Given an open cover of a compact metric space, the Lebesgue number lemma gives you a *uniform scale* — a single $\delta > 0$ such that any small enough set is fitted inside some cover element. This is a uniformity statement that converts the locally varying "scale of fineness" of an open cover into a globally uniform one.

The lemma is often invoked exactly to *avoid* fiddling with $\varepsilon$-$\delta$ arguments at every point separately. The standard recipe: given an open cover and any compact subset, the lemma gives a uniform $\delta$; partition the compact subset into pieces of diameter $< \delta$ (possible by total boundedness); each piece is in some cover element. This converts a global cover-fitting problem into a local one, with a uniform scale.

Concrete applications:

1. **Uniform continuity from continuity on compacts.** Let $f : X \to Y$ be continuous, $X$ compact metric, $Y$ metric. For each $x$, there is $\delta_x > 0$ such that $d(x, y) < \delta_x$ implies $d(f(x), f(y)) < \varepsilon$. The collection $\{B_{\delta_x/2}(x) : x \in X\}$ is an open cover; the Lebesgue number lemma gives a uniform $\delta$. This is the standard proof of uniform continuity on compact metric spaces.

2. **Homotopy lifting.** In covering space theory, lifting a homotopy $H : I \times Y \to X$ (with $I = [0, 1]$ compact) to the covering space requires breaking $I$ into small subintervals such that each $H([t, t'] \times Y)$ lies in an evenly covered neighborhood. The Lebesgue number lemma gives the uniform subdivision: take $\delta$ for the cover by evenly covered neighborhoods, and the partition of $I$ into intervals of length $< \delta$ works simultaneously for all $y \in Y$.

3. **Existence of geodesics.** In a compact Riemannian manifold, the existence of length-minimizing geodesics between any two points uses the Lebesgue number lemma to choose a uniform scale of "small enough" geodesic balls where local geodesic equations have solutions.

4. **Simplicial approximation.** In algebraic topology, approximating a continuous map $f : |K| \to |L|$ between simplicial complexes by a simplicial map requires choosing a uniform subdivision of $|K|$ — the Lebesgue number for the cover of $|K|$ by open stars of $L$-vertices via $f$.

The phrase "Lebesgue number" reflects Lebesgue's use of this principle in his foundational work on covering spaces and homotopy theory.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "compact metric space + open cover". The skill is to recognize when a uniform scale of fineness is needed.

The first source is **a continuous function on a compact metric domain**. Property $B$: a continuous $f : X \to Y$ with $X$ compact metric. The bridge: for each $\varepsilon > 0$, the family of preimage balls $\{f^{-1}(B_{\varepsilon/2}(y)) : y \in Y\}$ is an open cover, and the Lebesgue number gives a uniform $\delta$ such that diameter-$\delta$ sets in $X$ map into $\varepsilon$-balls in $Y$. *Example:* every continuous function on a closed bounded interval is uniformly continuous — direct application.

The second source is **a covering map $p : \tilde X \to X$ and a continuous map $f : [0, 1] \times Y \to X$ with $Y$ compact**. Property $B$: a compact-parametrized family of maps into the base of a covering space, with evenly covered neighborhoods forming an open cover of the image. The bridge: the Lebesgue number gives a uniform subdivision of $[0, 1]$ such that each piece $f([t_i, t_{i+1}] \times Y)$ lies in an evenly covered neighborhood, allowing path-by-path or homotopy-class-by-homotopy-class lifting. *Example:* path lifting, homotopy lifting in covering space theory.

The third source is **simplicial approximation of continuous maps**. Property $B$: a continuous $f : |K| \to |L|$ between geometric realizations of finite simplicial complexes. The bridge: the cover $\{f^{-1}(\text{open star}(v)) : v \in L^{(0)}\}$ is an open cover of $|K|$; the Lebesgue number gives a uniform scale at which barycentric subdivision aligns with the cover, enabling simplicial approximation. *Example:* simplicial approximation theorem in algebraic topology.

**Targets (Output Amplification)**

The conclusion is "there is $\delta > 0$ such that diameter-$<\delta$ sets fit inside some cover element".

Combine the conclusion with **a total boundedness argument**. Property $D$: the compact space $X$ has a finite $\delta/3$-net (or finer). The amplified result $E$: $X$ admits a finite partition into pieces each of diameter $< \delta$, each fitting in some cover element. The combination produces a *finite* refinement of the cover with explicit size constraints, useful in inductive constructions.

Combine the conclusion with **a continuous map on each piece**. Property $D$: a function defined piecewise on each cover element. The amplified result $E$: gluing works because each diameter-$\delta$ piece is contained in some cover element, so the function's local definition there applies. The combination is the basic mechanism of patching local data into global on a compact space.

Combine the conclusion with **a sequence of refining covers**. Property $D$: a sequence of open covers $\{U_n\}$ with $\delta_n \to 0$. The amplified result $E$: every point has a basis of "uniform balls" of radius $\delta_n$ which fit in some cover element of $\{U_n\}$. The combination gives a kind of uniform-scale neighborhood basis adapted to the covers, used in fixed-point and approximation arguments.

---

# Why Is It True

The intuition: for each point $x \in X$, the open cover provides an open neighborhood (some $U_\alpha$ containing $x$); this neighborhood contains a ball $B_{2\varepsilon(x)}(x)$ of positive radius. So at each point we have a *pointwise* scale $\varepsilon(x) > 0$ such that anything within distance $\varepsilon(x)$ of $x$ is in $U_\alpha$. The question is whether we can pass to a *uniform* scale — a single $\delta$ that works at every $x$.

Compactness lets us. The collection of smaller balls $\{B_{\varepsilon(x)}(x) : x \in X\}$ is an open cover, so by compactness there is a finite subcover $B_{\varepsilon(x_1)}(x_1), \dots, B_{\varepsilon(x_n)}(x_n)$ with $\varepsilon_i = \varepsilon(x_i)$. Define $\delta = \min_i \varepsilon_i > 0$.

Now take any subset $A$ of diameter $< \delta$. Pick any point $a_0 \in A$; it lies in some $B_{\varepsilon_i}(x_i)$, so $d(a_0, x_i) < \varepsilon_i$. For any other $a \in A$, $d(a, a_0) < \delta \leq \varepsilon_i$, so by triangle inequality $d(a, x_i) < \varepsilon_i + \varepsilon_i = 2\varepsilon_i$, putting $a \in B_{2\varepsilon_i}(x_i) \subseteq U_\alpha$ (the cover element associated to $x_i$). So $A \subseteq U_\alpha$ — uniformly across $A$.

The trick is the **double radius**: we work with balls $B_{\varepsilon(x)}(x)$ but the cover-fitting is at radius $B_{2\varepsilon(x)}(x)$. The factor of $2$ is what makes the triangle inequality close: if $A$ has small diameter and one point is in $B_\varepsilon(x_i)$, then *every* point is within $2\varepsilon$ of $x_i$, fitting in the larger ball.

The "compactness $\to$ finite subcover" step is the engine. Without compactness, the inf of $\varepsilon(x)$ over all $x$ might be $0$ (no positive uniform scale), and the conclusion fails. The compactness reduces the inf over $X$ to a min over a finite set, which is positive.

This is a beautiful instance of how compactness converts a *pointwise* condition (each $x$ has its own scale) into a *uniform* condition (a single scale works everywhere).

---

# What Makes This Hard

The non-obvious step is the **double-radius trick**: choose $\varepsilon(x)$ such that $B_{2\varepsilon(x)}(x) \subseteq U_\alpha$, but use the smaller $B_{\varepsilon(x)}(x)$ in the cover. The factor of $2$ is what makes the triangle inequality work: one needs the cover-fitting ball to be *larger* than the working ball so that diameter-$\delta$ sets fit. The most common error is to pick the same radius for both (which gives a slightly weaker conclusion: sets of diameter $< \delta/2$ fit, not $< \delta$), or to forget the factor entirely. Another common slip is to forget that compactness is needed for the min over the finite subcover to be positive — without compactness, the inf over $X$ might be $0$.

---

# Rederivation Scaffold

**High-level strategy:**
For each $x$, pick a scale $\varepsilon(x)$ such that the *doubled* ball $B_{2\varepsilon(x)}(x)$ lies in some cover element. The half-radius balls cover $X$, and compactness gives a finite subcover. The minimum of the chosen $\varepsilon$'s is the Lebesgue number $\delta$; any diameter-$\delta$ subset fits in some cover element via triangle inequality with the double radius.

**Subgoal decomposition:**

1. **Pointwise scale.** For each $x \in X$, find $\varepsilon(x) > 0$ such that $B_{2\varepsilon(x)}(x) \subseteq U_{\alpha(x)}$ for some $\alpha(x)$.
   - *Hint:* $x \in U_{\alpha(x)}$ for some $\alpha(x)$, and openness gives a ball.
   - *Why needed:* Establishes a pointwise notion of "small enough".

2. **Finite subcover.** $\{B_{\varepsilon(x)}(x) : x \in X\}$ is an open cover; extract a finite subcover $B_{\varepsilon_i}(x_i)$, $i = 1, \dots, n$.
   - *Hint:* Compactness of $X$.
   - *Why needed:* Reduces the inf over $X$ to a min over finitely many points.

3. **Take the minimum.** Define $\delta = \min_i \varepsilon_i > 0$ (positive because the min is over a finite set).
   - *Hint:* Finite min of positives is positive.
   - *Why needed:* The Lebesgue number.

4. **Triangle inequality argument.** Show every diameter-$\delta$ set $A$ fits in some $U_\alpha$ using the double-radius.
   - *Hint:* Pick $a_0 \in A$, find $i$ with $d(a_0, x_i) < \varepsilon_i$, use triangle inequality with $\delta \leq \varepsilon_i$ to get every $a \in A$ within $2\varepsilon_i$ of $x_i$.
   - *Why needed:* Completes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: Cover by small balls of a compact metric space
> **Statement:** Let $X$ be a compact metric space and $\{U_\alpha\}$ an open cover. For each $x \in X$, there exists $\varepsilon(x) > 0$ such that $B_{2\varepsilon(x)}(x) \subseteq U_\alpha$ for some $\alpha$.
>
> **Hint:** Openness of cover elements.
>
> **Why needed:** Step 1 of the main proof — establishes the pointwise scale.
>
> > [!note]- Full proof
> > Since $\{U_\alpha\}$ covers $X$, $x \in U_\alpha$ for some $\alpha$. Since $U_\alpha$ is open and metric balls form a basis, there is a ball $B_r(x) \subseteq U_\alpha$ for some $r > 0$. Take $\varepsilon(x) = r/2$; then $B_{2\varepsilon(x)}(x) = B_r(x) \subseteq U_\alpha$.

> [!note]- Lemma 2: Min over a finite subcover is positive
> **Statement:** Let $\{B_{\varepsilon(x_i)}(x_i)\}_{i=1}^n$ be a finite cover of a metric space, with $\varepsilon(x_i) > 0$. Then $\delta := \min_i \varepsilon(x_i) > 0$.
>
> **Hint:** Finite min of positives is positive.
>
> **Why needed:** Step 3 — the Lebesgue number must be positive to be useful.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X$ be a compact metric space and $\{U_\alpha\}_{\alpha \in A}$ an open cover.
>
> **Step 1: Pointwise scale.** By Lemma 1, for each $x \in X$, there is $\varepsilon(x) > 0$ such that $B_{2\varepsilon(x)}(x) \subseteq U_{\alpha(x)}$ for some $\alpha(x) \in A$.
>
> **Step 2: Finite subcover.** The collection $\{B_{\varepsilon(x)}(x) : x \in X\}$ is an open cover of $X$. By compactness, finitely many cover $X$: say $B_{\varepsilon_1}(x_1), \dots, B_{\varepsilon_n}(x_n)$ with $\varepsilon_i = \varepsilon(x_i)$.
>
> **Step 3: Lebesgue number.** Define $\delta = \min(\varepsilon_1, \dots, \varepsilon_n)$. Since each $\varepsilon_i > 0$ and the min is over a finite set, $\delta > 0$.
>
> **Step 4: Verify the conclusion.** Let $A \subseteq X$ with $\operatorname{diam}(A) < \delta$. We must show $A \subseteq U_\alpha$ for some $\alpha$. If $A = \emptyset$, trivially. Otherwise, pick $a_0 \in A$. Since $\{B_{\varepsilon_i}(x_i)\}$ covers $X$, $a_0 \in B_{\varepsilon_i}(x_i)$ for some $i$, i.e., $d(a_0, x_i) < \varepsilon_i$.
>
> For any $a \in A$, $d(a, a_0) \leq \operatorname{diam}(A) < \delta \leq \varepsilon_i$. By the triangle inequality:
> $$d(a, x_i) \leq d(a, a_0) + d(a_0, x_i) < \varepsilon_i + \varepsilon_i = 2\varepsilon_i.$$
> So $a \in B_{2\varepsilon_i}(x_i) \subseteq U_{\alpha(x_i)}$ (by choice of $\varepsilon(x_i) = \varepsilon_i$ in Lemma 1).
>
> Since this holds for every $a \in A$, $A \subseteq U_{\alpha(x_i)}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Uniform continuity on compacts.** Let $f : X \to Y$ be continuous, $X$ compact metric, $Y$ metric. Then $f$ is uniformly continuous. *Proof:* Given $\varepsilon > 0$, for each $y \in Y$ the ball $B_{\varepsilon/2}(y)$ is open; preimages $f^{-1}(B_{\varepsilon/2}(y))$ form an open cover of $X$. By the Lebesgue number lemma, there is $\delta > 0$ such that any set of diameter $< \delta$ in $X$ lies in some $f^{-1}(B_{\varepsilon/2}(y))$. Hence $d(x, x') < \delta$ implies $f(x), f(x') \in B_{\varepsilon/2}(y)$ for some $y$, so $d(f(x), f(x')) < \varepsilon$. This battle-tests the input-broadening: a uniform continuity statement is a Lebesgue number argument in disguise.

**Path lifting in covering space theory.** Let $p : \tilde X \to X$ be a covering map and $\gamma : [0, 1] \to X$ a path. The image $\gamma([0, 1])$ is compact (continuous image of compact), and is covered by evenly covered neighborhoods $\{V_\alpha\}$. By the Lebesgue number lemma applied to $[0, 1]$ with the open cover $\{\gamma^{-1}(V_\alpha)\}$, there is $\delta > 0$ such that any subinterval of $[0, 1]$ of length $< \delta$ maps into a single evenly covered neighborhood. So partitioning $[0, 1]$ into $\lceil 1/\delta \rceil$ subintervals, each $\gamma([t_i, t_{i+1}])$ lies in some $V_\alpha$ with a fixed local trivialization. Lift one piece at a time, matching endpoints.

**Existence of geodesics in compact Riemannian manifolds.** On a compact Riemannian manifold $M$, take an open cover by *geodesically convex* neighborhoods (where any two points are joined by a unique minimizing geodesic). The Lebesgue number $\delta$ gives a uniform scale: any pair of points at distance $< \delta$ are joined by a unique minimizing geodesic. This is the cornerstone of local geodesic theory.

---

# Bridges

- **[[Thm - Compactness in Metric Spaces (Three Equivalents)]]** — the underlying compactness is what gives the finite subcover; the Lebesgue number lemma is a corollary applied to a specific kind of cover.

- **[[Def - Totally Bounded Metric Space]]** — total boundedness gives finite $\varepsilon$-nets, useful in tandem with the Lebesgue number.

- **[[Thm - Compact Subset of Hausdorff is Closed]]** — related compactness results in metric/Hausdorff spaces.

- **Uniform continuity** — the standard application of the Lebesgue number lemma in real analysis.

---

# Unlocked by This

> [!tip] Uniform Continuity on Compacts *(from Real Analysis)*
> Every continuous function on a compact metric space is uniformly continuous. The proof is a direct Lebesgue number application.

> [!tip] Homotopy and Path Lifting *(from Algebraic Topology)*
> Continuous maps from compact spaces into the base of a covering map can be subdivided into pieces each lying in an evenly covered neighborhood, enabling pathwise and homotopy lifting. The Lebesgue number gives the uniform subdivision.

> [!tip] Simplicial Approximation Theorem *(from Algebraic Topology)*
> Every continuous map between simplicial complexes can be approximated by a simplicial map after barycentric subdivision. The Lebesgue number provides the uniform fineness of the required subdivision.

> [!tip] Existence of Geodesics in Compact Riemannian Manifolds *(from Differential Geometry)*
> The Lebesgue number for a cover by geodesically convex neighborhoods gives a uniform scale at which minimizing geodesics exist and are unique.
