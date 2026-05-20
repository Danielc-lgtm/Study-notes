---
type: theorem
subject: topology
prereqs:
  - "Def - Product Topology"
  - "Def - Compact Space"
  - "Thm - The Tube Lemma"
  - "Thm - Closed Subset of Compact is Compact"
tags: [analysis, topology]
---

# Notation

$X_1, \dots, X_n$ are topological spaces. $X_1 \times \cdots \times X_n$ is their Cartesian product with the **product topology** (which on finite products is the same as the box topology — basic opens are open rectangles $U_1 \times \cdots \times U_n$ with $U_i \subseteq X_i$ open). $\pi_i$ is the projection to the $i$-th factor. The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Statement

> **Tychonoff Theorem for Finite Products.** Let $X_1, \dots, X_n$ be compact topological spaces. Then the product $X_1 \times \cdots \times X_n$ with the product topology is compact.
>
> By induction it suffices to prove this for $n = 2$: if $X$ and $Y$ are compact, then $X \times Y$ is compact.

---

# Motivation

Compactness is the central tool of topology for analysis: finite subcovers convert global problems to finite ones. Products of spaces arise everywhere — coordinate spaces, function spaces, fiber bundles — and we want to know whether compactness is preserved by the product operation. The finite-product version of Tychonoff says yes: if each factor is compact, the product is.

The result is non-trivial: a basic open set in $X \times Y$ has the form $U \times V$ where $U \subseteq X, V \subseteq Y$ are open, and a general open set is a union of such basic opens. An open cover of $X \times Y$ does not obviously refine to one whose elements are basic; even when it does, extracting a finite subcover is not immediate because basic opens are "rectangular" and a cover might require many basic rectangles to capture a single open set.

The right tool is the **tube lemma**: if $X$ is compact and $U$ is an open subset of $X \times Y$ containing a "slice" $X \times \{y\}$, then $U$ contains a tube $X \times V$ for some open neighborhood $V$ of $y$. The tube lemma lets us "thicken" a slice into a small tube, and finite covers of $Y$ then assemble to cover $X \times Y$. The finite case of Tychonoff is essentially the tube lemma applied carefully, and it does *not* require the axiom of choice (the proof is constructive in this sense — the finite subcover is built explicitly).

The application is the immediate result that **$[0, 1]^n$ is compact**, which gives **Heine–Borel** in $\mathbb{R}^n$: a subset of $\mathbb{R}^n$ is compact if and only if it is closed and bounded. Every compactness result in classical analysis traces back to Heine–Borel.

The infinite-product analog ([[Thm - Tychonoff Theorem]]) is a much deeper result, equivalent to the axiom of choice; the finite case is genuinely easier and constructive. Most of the "real-world" applications of compact products in analysis use only the finite version: Heine–Borel, the Extreme Value Theorem, joint continuity, etc.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is: each factor $X_i$ is compact. The skill is recognizing this in problems where the relevant compact pieces appear in disguise.

The first source is **a closed bounded subset of $\mathbb{R}^n$ presented as a Cartesian product**. Property $B$: an object of the form $[a_1, b_1] \times \cdots \times [a_n, b_n]$, or a closed subset thereof. The bridge: each $[a_i, b_i]$ is compact (closed bounded in $\mathbb{R}$, by [[Thm - Heine–Borel Theorem|Heine–Borel]] in dimension $1$), and Tychonoff gives the product compact; passing to closed subsets gives compactness of the full closed bounded set. The nonobviousness: the original set need not be presented as a product, but if one can write it as a closed subset of a product of intervals (which is *always* possible for a bounded set), Tychonoff applies. *Example:* a closed disk $\{x^2 + y^2 \leq 1\}$ is closed in $[-1, 1]^2$; the product is compact by Tychonoff, and the disk is closed inside, so it inherits compactness.

The second source is **the unit cube as a parameter space**. Property $B$: a problem whose parameters live in $[0, 1]^n$ — a Bayesian posterior over $n$ parameters, a probability simplex, a hyperrectangle of constraints. The bridge: $[0, 1]^n$ is compact by Tychonoff, so continuous functions on the parameter space attain extrema, sequences have convergent subsequences, and limits exist. *Example:* in optimization, the unit simplex $\{(p_1, \dots, p_n) : p_i \geq 0, \sum p_i = 1\}$ is a compact subset of $[0, 1]^n$, hence compact, hence continuous objective functions attain a minimum — this is the foundation of finite-dimensional optimization theory.

The third source is **a graph of a continuous function as a compact subset of a product**. Property $B$: the graph $\{(x, f(x)) : x \in K\}$ of a continuous $f : K \to L$ with $K, L$ compact. The bridge: the graph is the image of the continuous map $x \mapsto (x, f(x))$ from $K$ into $K \times L$; $K \times L$ is compact by Tychonoff, continuous images of compact are compact, so the graph is compact. The nonobviousness: compactness is being used to certify properties of *functions* by treating their graphs as compact subsets of products.

**Targets (Output Amplification)**

The conclusion is "$X_1 \times \cdots \times X_n$ is compact".

Combine the conclusion with **the closedness of compact sets in Hausdorff spaces.** Property $D$: each $X_i$ is also Hausdorff. The amplified result $E$: the product is compact Hausdorff, hence normal, hence has all the Urysohn-Tietze function-construction toolkit. The combination is nonobvious in the sense that "compact + Hausdorff" buys far more than either alone, and the product inherits both axioms cleanly.

Combine the conclusion with **the extreme value theorem.** Property $D$: a continuous function $f : X_1 \times \cdots \times X_n \to \mathbb{R}$. The amplified result $E$: $f$ attains its maximum and minimum (continuous image of compact is closed bounded in $\mathbb{R}$). The combination gives **joint extrema**: optima exist as a function of *all* parameters simultaneously, not just each one separately. This is the foundation of joint optimization problems in operations research and economics.

Combine the conclusion with **the tube lemma in reverse.** Property $D$: a closed subset $C \subseteq X \times Y$. The amplified result $E$: the projection $\pi_X(C) \subseteq X$ is closed (when $Y$ is compact). The combination is the **closed map** property of projections from compact spaces, which is used to prove that compact spaces have many properties under continuous and quotient operations.

---

# Why Is It True

The intuition is geometric. Take two compact factors $X$ and $Y$. Imagine an open cover $\{W_\alpha\}$ of $X \times Y$ — possibly infinite, with each $W_\alpha$ a complicated open set, not a basic rectangle.

For each point $(x, y) \in X \times Y$, the open set covering it contains some basic open neighborhood $U(x, y) \times V(x, y)$ with $x \in U(x, y), y \in V(x, y)$. So *locally* the cover refines to a cover by basic rectangles. The question is whether we can pass from this local refinement to a finite subcover globally.

Fix $y \in Y$ for the moment. The slice $X \times \{y\}$ is homeomorphic to $X$, hence compact. The cover $\{U(x, y) \times V(x, y) : x \in X\}$ refined to this slice gives an open cover of $X \times \{y\}$, which has a finite subcover. Call the corresponding open sets $U_1(y), \dots, U_{n(y)}(y) \subseteq X$ and $V_1(y), \dots, V_{n(y)}(y) \subseteq Y$, with each rectangle $U_i(y) \times V_i(y)$ inside some $W_\alpha$. Let $V(y) = V_1(y) \cap \cdots \cap V_{n(y)}(y)$ — a finite intersection of opens, hence open, and $y \in V(y)$.

Now the **tube lemma** insight: the "tube" $X \times V(y)$ — a thin slab over $V(y)$ in $Y$ — is covered by the finitely many rectangles $U_i(y) \times V_i(y)$ (since they cover the slice $X \times \{y\}$, and each is "rectangular", so they cover $X \times V(y)$ too, as long as we take $V(y) \subseteq V_i(y)$ for each $i$, which we have). So a finite subset of the original cover covers the tube $X \times V(y)$.

The collection $\{V(y) : y \in Y\}$ is an open cover of $Y$. By compactness of $Y$, take a finite subcover $V(y_1), \dots, V(y_m)$. The tubes $X \times V(y_j)$ cover $X \times Y$, and each tube is covered by a finite subset of the original cover. The union over $j$ of these finite subsets is again finite — so we have a finite subcover.

The whole argument is "iterated compactness": use compactness of $X$ on each slice to get a tube, then compactness of $Y$ on the resulting tube-cover to finish. The finiteness propagates through iteration because we only ever take finite unions of finite sets.

The induction to $n$ factors is by associativity: $X_1 \times X_2 \times \cdots \times X_n = (X_1 \times \cdots \times X_{n-1}) \times X_n$, and the two-factor case applied to the compact (by inductive hypothesis) $X_1 \times \cdots \times X_{n-1}$ and the compact $X_n$ gives compactness of the whole product.

---

# What Makes This Hard

The non-obvious step is the **tube lemma**: thinking to pass from a finite cover of a slice $X \times \{y\}$ to a finite cover of a *tube* $X \times V$ for some open $V$ around $y$. Most people, given an open cover of $X \times Y$, do not immediately think to fix $y$, cover the slice, then thicken — they try to take a finite subcover directly, which is doomed because the original cover need not even consist of rectangles. The most common error is to try to use compactness of $X$ and $Y$ simultaneously by some kind of "product compactness" argument, rather than the sequential extraction (slice $\to$ tube $\to$ finite cover of $Y$ via tubes).

---

# Rederivation Scaffold

**High-level strategy:**
Induct on the number of factors; the two-factor case is the engine. For two factors $X \times Y$ with $X, Y$ compact, fix $y \in Y$, cover the slice $X \times \{y\}$ by finitely many basic rectangles, intersect their $Y$-projections to get an open $V(y) \ni y$ over which a tube of finitely many rectangles covers $X \times V(y)$. Then compactness of $Y$ gives a finite subcover of $Y$ by such $V(y)$, and the corresponding finite collection of rectangles covers $X \times Y$.

**Subgoal decomposition:**

1. **Reduce to two factors via induction.** Show that if the theorem holds for $n$ factors, it holds for $n+1$.
   - *Hint:* Write $X_1 \times \cdots \times X_{n+1} \cong (X_1 \times \cdots \times X_n) \times X_{n+1}$ and use the two-factor case.
   - *Why needed:* Reduces the general case to the two-factor base.

2. **Refine the cover to basic rectangles locally.** Given an open cover $\{W_\alpha\}$, for each $(x, y)$ choose a basic rectangle $U(x, y) \times V(x, y)$ inside some $W_\alpha$.
   - *Hint:* Use the definition of product topology — every open contains a basic rectangle around each interior point.
   - *Why needed:* The compactness arguments work on rectangles.

3. **Cover each slice with finitely many rectangles (use compactness of $X$).** For each fixed $y \in Y$, the slice $X \times \{y\}$ is compact (homeomorphic to $X$).
   - *Hint:* Apply compactness to the cover of $X \times \{y\}$ by the chosen rectangles.
   - *Why needed:* Reduces the slice-cover to a finite one.

4. **Form the tube via intersection of $V$-projections.** Let $V(y) = V_1(y) \cap \cdots \cap V_{n(y)}(y)$ be a finite intersection of opens in $Y$.
   - *Hint:* Finite intersections of opens are open, and $y \in V(y)$.
   - *Why needed:* The tube $X \times V(y)$ is covered by the finitely many rectangles from step 3.

5. **Cover $Y$ by tubes (use compactness of $Y$).** Take a finite subcover of $\{V(y) : y \in Y\}$.
   - *Hint:* This is the second use of compactness in the proof.
   - *Why needed:* The tubes $X \times V(y_1), \dots, X \times V(y_m)$ then cover $X \times Y$, and the union of their finite covers is finite.

---

# Lemma Decomposition

> [!note]- Lemma 1: The Tube Lemma
> **Statement:** Let $X$ be compact, $Y$ any topological space, and $y_0 \in Y$. If $W \subseteq X \times Y$ is open and $X \times \{y_0\} \subseteq W$, then there is an open neighborhood $V$ of $y_0$ in $Y$ with $X \times V \subseteq W$.
>
> **Hint:** For each $x \in X$, find a basic rectangle $U_x \times V_x \subseteq W$ with $(x, y_0) \in U_x \times V_x$; use compactness of $X$ to get finitely many $U_{x_1}, \dots, U_{x_n}$ covering $X$, and set $V = V_{x_1} \cap \cdots \cap V_{x_n}$.
>
> **Why needed:** It is the engine of the proof; the finite-rectangle covering of a slice can be thickened to a tube.
>
> > [!note]- Full proof
> > For each $x \in X$, $(x, y_0) \in W$ open, so there is a basic open neighborhood $U_x \times V_x \subseteq W$ with $x \in U_x \subseteq X$ open and $y_0 \in V_x \subseteq Y$ open. The collection $\{U_x : x \in X\}$ is an open cover of $X$; by compactness, finitely many $U_{x_1}, \dots, U_{x_n}$ cover $X$. Set $V = V_{x_1} \cap \cdots \cap V_{x_n}$, a finite intersection of opens, hence open, with $y_0 \in V$.
> >
> > Verify $X \times V \subseteq W$: for any $(x, y) \in X \times V$, $x \in U_{x_i}$ for some $i$, and $y \in V \subseteq V_{x_i}$, so $(x, y) \in U_{x_i} \times V_{x_i} \subseteq W$.

> [!note]- Lemma 2: Closed projection from compact factor
> **Statement:** Let $X$ be compact. Then the projection $\pi_Y : X \times Y \to Y$ is a **closed map**: $\pi_Y(C)$ is closed in $Y$ for every closed $C \subseteq X \times Y$.
>
> **Hint:** Apply the tube lemma to the complement of $C$.
>
> **Why needed:** Often useful as a corollary; gives the closed-map property of compact-factor projections.
>
> > [!note]- Full proof
> > Let $C \subseteq X \times Y$ be closed; we show $Y \setminus \pi_Y(C)$ is open. Pick $y \in Y \setminus \pi_Y(C)$; this means $(x, y) \notin C$ for all $x \in X$, i.e., $X \times \{y\} \subseteq (X \times Y) \setminus C$. The complement is open, so by Lemma 1 there is an open $V \ni y$ with $X \times V \subseteq (X \times Y) \setminus C$. So $V \cap \pi_Y(C) = \emptyset$, meaning $V \subseteq Y \setminus \pi_Y(C)$, which is therefore open.

---

# Formal Proof

> [!note]- Complete formal proof
> By induction on $n$, it suffices to prove that $X \times Y$ is compact when $X, Y$ are compact.
>
> Let $\{W_\alpha\}_{\alpha \in A}$ be an open cover of $X \times Y$. We show that it has a finite subcover.
>
> **Step 1: Local refinement to rectangles.** For each $(x, y) \in X \times Y$, $(x, y)$ lies in some $W_{\alpha(x, y)}$, and by the definition of the product topology there is a basic open rectangle $U(x, y) \times V(x, y) \subseteq W_{\alpha(x, y)}$ with $(x, y) \in U(x, y) \times V(x, y)$ — i.e., $U(x, y) \subseteq X$ and $V(x, y) \subseteq Y$ are open and contain $x, y$ respectively.
>
> **Step 2: Slice argument (compactness of $X$).** Fix $y \in Y$. The slice $X \times \{y\}$ is homeomorphic to $X$, hence compact. The collection $\{U(x, y) \times V(x, y) : x \in X\}$ refined to this slice forms an open cover (restricted to $X \times \{y\}$). By compactness of $X \times \{y\}$, there are finitely many points $x_1(y), \dots, x_{n(y)}(y) \in X$ with the rectangles $U_i(y) \times V_i(y) := U(x_i(y), y) \times V(x_i(y), y)$ ($i = 1, \dots, n(y)$) covering $X \times \{y\}$. In particular, $U_1(y), \dots, U_{n(y)}(y)$ cover $X$.
>
> **Step 3: Form the tube.** Let $V(y) = V_1(y) \cap \cdots \cap V_{n(y)}(y)$, a finite intersection of open subsets of $Y$, hence open; and $y \in V(y)$ since $y \in V_i(y)$ for each $i$. The tube $X \times V(y) \subseteq \bigcup_{i=1}^{n(y)} U_i(y) \times V_i(y)$: for any $(x, y') \in X \times V(y)$, $x \in U_i(y)$ for some $i$ (the $U_i(y)$ cover $X$), and $y' \in V(y) \subseteq V_i(y)$, so $(x, y') \in U_i(y) \times V_i(y)$. This is the tube lemma in action.
>
> **Step 4: Cover $Y$ by tubes (compactness of $Y$).** The collection $\{V(y) : y \in Y\}$ is an open cover of $Y$ (each $y$ is in $V(y)$). By compactness of $Y$, there are finitely many $y_1, \dots, y_m$ with $V(y_1) \cup \cdots \cup V(y_m) = Y$.
>
> **Step 5: Assemble the finite subcover.** $X \times Y = \bigcup_{j=1}^m X \times V(y_j) \subseteq \bigcup_{j=1}^m \bigcup_{i=1}^{n(y_j)} U_i(y_j) \times V_i(y_j) \subseteq \bigcup_{j=1}^m \bigcup_{i=1}^{n(y_j)} W_{\alpha(x_i(y_j), y_j)}$. The right side is a finite union of $W_\alpha$ — at most $\sum_j n(y_j) < \infty$ elements of the original cover. So $\{W_\alpha\}$ has a finite subcover, and $X \times Y$ is compact. $\blacksquare$
>
> For the general case, induct: if $X_1, \dots, X_n$ are compact and $X_1 \times \cdots \times X_{n-1}$ is compact by IH, then $X_1 \times \cdots \times X_n \cong (X_1 \times \cdots \times X_{n-1}) \times X_n$ is compact by the two-factor case. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Compactness of the orthogonal group $O(n)$.** $O(n) = \{A \in \mathbb{R}^{n \times n} : A^T A = I\}$ is a closed subset of $\mathbb{R}^{n^2}$ (closed because $A^T A = I$ is a continuous equation). It is bounded ($\lVert A\rVert_F^2 = n$ for $A \in O(n)$). Hence by Heine–Borel — which follows from Tychonoff finite — $O(n)$ is compact. This is the foundation for the harmonic analysis of compact Lie groups; the compactness comes from a Tychonoff-finite argument.

**Joint continuity from separate continuity in special cases.** If $f : X \times Y \to Z$ is continuous in each variable separately and $X \times Y$ is compact (by Tychonoff), then under additional hypotheses (e.g., $Z = \mathbb{R}$ and a sequence-based criterion) one can deduce joint continuity. The compactness of the domain is exactly what allows the leap from "separately continuous" to "jointly continuous".

**Existence of saddle points in finite games.** A finite zero-sum game with strategy sets $S_1 = \{1, \dots, m\}$ and $S_2 = \{1, \dots, n\}$ has mixed strategy spaces equal to the unit simplices $\Delta_m \subseteq [0, 1]^m$ and $\Delta_n \subseteq [0, 1]^n$. The expected payoff $\sum_{i,j} p_i q_j a_{ij}$ is continuous, and the product $\Delta_m \times \Delta_n$ is compact by Tychonoff finite. The minimax theorem then follows from existence of optima — a continuous function on a compact product attains its extrema. Tychonoff finite is what guarantees the existence.

---

# Bridges

- **[[Thm - Heine–Borel Theorem]]** — Tychonoff finite implies that closed bounded subsets of $\mathbb{R}^n$ are compact (as closed subsets of $[-N, N]^n$, which is a product of compacts).

- **[[Thm - The Tube Lemma]]** — the engine of the proof of Tychonoff finite, applied at each slice.

- **[[Thm - Tychonoff Theorem]]** — the generalization to arbitrary index sets. The finite case is genuinely simpler and AC-free.

- **[[Thm - Continuous Image of a Compact Space]]** — applied to projections, says continuous images of compact products are compact, so e.g. the maximum of a continuous function on $X \times Y$ exists.

- **[[Thm - Compact Subset of Hausdorff is Closed]]** — applied to products: a compact subset of a Hausdorff product is closed, often used to identify limits.

---

# Unlocked by This

> [!tip] Heine–Borel Theorem *(from Real Analysis)*
> A subset of $\mathbb{R}^n$ is compact if and only if it is closed and bounded. The forward direction is Tychonoff finite + closed subsets of compacts are compact; the converse is by the extreme value theorem.

> [!tip] Extreme Value Theorem for Joint Optimization *(from Real Analysis)*
> A continuous real-valued function on a product of compact spaces attains its maximum and minimum. This is the foundation of joint optimization over multiple compact parameter spaces.

> [!tip] Compactness of Classical Lie Groups *(from Lie Theory)*
> $O(n), U(n), SO(n), SU(n)$ are all closed and bounded subsets of $\mathbb{R}^{n^2}$ or $\mathbb{C}^{n^2}$, hence compact by Heine–Borel, hence by Tychonoff finite. Their representation theory and harmonic analysis depend on this compactness.
