---
type: theorem
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - First and Second Countable"
  - "Def - Separation Axioms"
  - "Def - Completely Regular Space"
  - "Def - Product Topology"
  - "Thm - Urysohn's Lemma"
tags: [analysis, topology]
---

# Notation

$X$ is a topological space; specifically, we will consider $X$ second countable, Hausdorff, and regular. $\mathcal{B}$ is a countable basis for the topology. The Hilbert cube is $[0, 1]^\mathbb{N}$ with the metric $d(x, y) = \sum_n |x_n - y_n|/2^n$ (or the equivalent $d_n(x_n, y_n)/2^n$ for any bounded metric $d_n$). The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Statement

> **Urysohn Metrization Theorem.** Let $X$ be a topological space that is **second countable**, **Hausdorff**, and **regular**. Then $X$ is **metrizable**: there exists a metric $d$ on $X$ such that the topology induced by $d$ is the original topology on $X$.
>
> Equivalently: $X$ embeds homeomorphically into the **Hilbert cube** $[0, 1]^\mathbb{N}$.

---

# Motivation

The question is: which topological spaces admit a metric inducing their topology? This is a fundamental question in topology — metric spaces are familiar, computable, support most of analysis, while general topological spaces are wild. A *metrization theorem* gives a sufficient condition for a topological space to be metric, in terms of separation axioms and countability.

Urysohn's theorem says: **second countable + Hausdorff + regular** is enough. The hypotheses are natural: second countable gives a countable structure (enough to build a single metric); Hausdorff + regular give the separation needed to construct enough continuous functions; together they imply complete regularity (regular + second countable is enough for complete regularity, by a Lemma in §9 of Bredon), so there are continuous functions separating points from closed sets.

The proof has a beautiful three-step structure:

1. **Complete regularity comes for free.** Regular + second countable implies completely regular (Bredon Lemma 9.9): from the countable basis, one can extract a countable family of separating functions, sufficient to verify complete regularity.

2. **Embed in a countable product of intervals.** The countable family of separating functions $f_i : X \to [0, 1]$ gives a map $\Phi : X \to [0, 1]^\mathbb{N}$ by $\Phi(x) = (f_i(x))_i$. Hausdorffness ensures $\Phi$ is injective; complete regularity ensures $\Phi$ is a homeomorphism onto its image.

3. **The Hilbert cube is metrizable.** The product topology on $[0, 1]^\mathbb{N}$ is induced by the explicit metric $d(x, y) = \sum_n |x_n - y_n|/2^n$. The convergence of the series is by geometric series; the topology check is by directly verifying that this metric induces the product topology.

The result is constructive: given a second countable Hausdorff regular space, the proof exhibits an explicit embedding in $[0, 1]^\mathbb{N}$, and the pullback metric is computable.

The theorem is not the most general metrization theorem — the **Nagata–Smirnov theorem** (regular + $\sigma$-locally-finite base) and the **Bing metrization theorem** (collectionwise normal + $\sigma$-discrete base) characterize metrizability without the second-countable hypothesis. But Urysohn covers the spaces of practical interest: every "nice" topological space that one encounters in analysis (second countable Hausdorff regular) is metrizable.

A different perspective: **the Hilbert cube is "universal"** for second countable metric spaces. Every separable metric space embeds in the Hilbert cube. So second countable Hausdorff regular spaces are exactly the spaces that embed in $[0, 1]^\mathbb{N}$, which is the standard "universal" metric space.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "second countable + Hausdorff + regular". The skill is recognizing this triple in problems where metrizability is needed.

The first source is **second countable + locally compact Hausdorff**. Property $B$: an LCH space with countable basis. The bridge: LCH implies regular (in fact completely regular, by [[Thm - LCH Implies Completely Regular]]); combined with second countable, we get the Urysohn hypotheses, so $X$ is metrizable. *Example:* a $\sigma$-compact LCH space is automatically second countable (one can show), so it is metrizable. This is the standard route to metrizability of nice topological spaces.

The second source is **a topological manifold (Hausdorff, locally Euclidean, second countable)**. Property $B$: a manifold in the standard sense. The bridge: manifolds are LCH (locally Euclidean), Hausdorff, second countable by definition; the Urysohn hypotheses are satisfied. So every topological manifold is metrizable — a fact often taken for granted but actually a Urysohn-metrization consequence. *Example:* the existence of a Riemannian metric on a smooth manifold relies first on topological metrizability.

The third source is **a CW complex with countably many cells**. Property $B$: a CW complex built from countably many cells of each dimension. The bridge: CW complexes are Hausdorff and regular (a standard fact); countability of cells gives second countable; hence metrizable by Urysohn. *Example:* most CW complexes studied in algebraic topology (finite ones, countable simplicial complexes) are metrizable.

**Targets (Output Amplification)**

The conclusion is "$X$ is metrizable, equivalently embeds in $[0, 1]^\mathbb{N}$".

Combine the conclusion with **a completeness consideration**. Property $D$: $X$ is locally compact and $\sigma$-compact. The amplified result $E$: $X$ is **completely metrizable** (admits a complete metric in some compatible metric). The combination is useful in Polish space theory — Polish spaces are exactly the completely metrizable separable spaces, and Urysohn gives metrizability; an extra argument gives completeness.

Combine the conclusion with **the full metric-space toolkit**. Property $D$: any theorem that works in metric spaces (uniform continuity on compacts, Bolzano–Weierstrass for sequences, completion via Cauchy sequences). The amplified result $E$: every such theorem applies to $X$. Once metrizability is established, the topologist's toolbox doubles: every metric-space technique is now available.

Combine the conclusion with **the explicit embedding in $[0, 1]^\mathbb{N}$**. Property $D$: a specific construction needed on $X$ (e.g., a continuous function, a sequence, a partition). The amplified result $E$: pull back the construction from $[0, 1]^\mathbb{N}$ via the embedding. The combination converts abstract topological problems into concrete Hilbert-cube problems, often more tractable.

---

# Why Is It True

The intuition: a topological space is metrizable if and only if it can be "coordinatized" by countably many real-valued continuous functions, with the topology being precisely the topology of coordinate-wise convergence.

Why countably many? Because a metric provides a countable basis at each point ($1/n$-balls), so the topology has a countable structure locally; for a *separable* metric space (countable dense subset), this assembles into a global countable basis. Thus a metric topology has at most "countable-basis-many" coordinates — and conversely, if we have a countable family of separating functions, we can attempt to assemble them into a metric.

The proof unfolds this idea:

**Step 1: Regular + second countable ⇒ completely regular.** This is the key technical lemma. Take the countable basis $\mathcal{B}$. For each pair $(U, V) \in \mathcal{B}^2$ with $\overline{U} \subseteq V$ (a countable collection of pairs), find a continuous $f_{U, V} : X \to [0, 1]$ with $f_{U, V} \equiv 0$ on $\overline U$ and $f_{U, V} \equiv 1$ on $X \setminus V$. The existence of such $f$ for each pair uses regularity at points: given $x \in U$ and closed $X \setminus V$, regularity gives disjoint opens, and the closure-containing structure gives a Urysohn-style function via iterated regularity. This produces a countable family $\{f_i\}$ that separates points from closed sets.

**Step 2: Embed via the family.** The map $\Phi : X \to [0, 1]^\mathbb{N}$, $\Phi(x) = (f_i(x))_i$, is continuous (each $\pi_i \circ \Phi = f_i$ is continuous). It is injective (Hausdorff + separating functions: given $x \neq y$, some closed set $C \ni y$ has $x \notin C$, and $f_i$ for the appropriate pair separates, so $\Phi(x) \neq \Phi(y)$). It is a homeomorphism onto its image (open maps to open: given $U$ open in $X$ and $x \in U$, complete regularity gives $f_i$ with $f_i(x) = 0$, $f_i \equiv 1$ on $X \setminus U$; the set $\Phi(U)$ contains the open neighborhood $\{y \in \Phi(X) : y_i < 1/2\}$ of $\Phi(x)$ in $\Phi(X)$).

**Step 3: $[0, 1]^\mathbb{N}$ is metrizable.** The metric $d(x, y) = \sum_n |x_n - y_n|/2^n$ induces the product topology — direct verification: a basis of the product topology is $\{x : |x_i - x_i^0| < \varepsilon \text{ for } i \leq N\}$, and a basis of the metric topology is $\{x : d(x, x^0) < \varepsilon\}$; the two agree up to constants.

So the entire proof is **"separation gives functions, functions give an embedding, the universal space is metric"** — a beautiful three-step structure.

---

# What Makes This Hard

The non-obvious step is **Step 1: deriving complete regularity from regular + second countable** — the recognition that the countable basis lets one *select* a countable family of separating functions, parametrized by pairs $(U, V)$ in the basis with $\overline U \subseteq V$. Most people, seeing the theorem statement, expect the proof to use Urysohn's lemma directly — but Urysohn's lemma requires normality, and we only have regularity, so the construction must derive separation functions more carefully. The most common error is to try to invoke Urysohn's lemma directly without proving normality first (which is not generally implied by regularity alone). Another slip is forgetting that the countable family of separating functions must be *the same family* used to embed in the product — i.e., one cannot first establish complete regularity abstractly and then choose a fresh countable family of functions; one must explicitly construct *a countable family* of separating functions, since the embedding lives in $[0, 1]^\mathbb{N}$, not in $[0, 1]^{C(X, [0, 1])}$.

---

# Rederivation Scaffold

**High-level strategy:**
Three steps. (1) Use regular + second countable to extract a countable family of separating functions (a kind of "small Urysohn"). (2) Embed $X$ in the Hilbert cube $[0, 1]^\mathbb{N}$ via the separating family. (3) Pull back the explicit metric on the Hilbert cube.

**Subgoal decomposition:**

1. **Find a countable family of separating functions.** Use the countable basis and regularity to select a countable family $\{f_i\}$ of continuous functions $X \to [0, 1]$ such that for every $x \in X$ and every closed $C \not\ni x$, some $f_i$ is $0$ at $x$ and $1$ on $C$.
   - *Hint:* Index the family by pairs $(U, V) \in \mathcal{B}^2$ with $\overline U \subseteq V$; for each such pair, find a function vanishing on $\overline U$ and $\equiv 1$ outside $V$ (requires more than just regularity: use iterated regularity for a dyadic-construction).
   - *Why needed:* Provides the coordinates for embedding into $[0, 1]^\mathbb{N}$.

2. **Build the embedding $\Phi : X \to [0, 1]^\mathbb{N}$.** Define $\Phi(x) = (f_i(x))_i$, where $\{f_i\}$ is the countable family from step 1.
   - *Hint:* Continuity of $\Phi$ is by the universal property of the product; injectivity and "homeomorphism onto image" use the separating property.
   - *Why needed:* The Hilbert cube is metric, so its subspaces are metric.

3. **Metrize the Hilbert cube.** Show $[0, 1]^\mathbb{N}$ with the metric $d(x, y) = \sum_n |x_n - y_n|/2^n$ has the same topology as the product topology.
   - *Hint:* Direct verification: the metric and the product topology have equivalent bases.
   - *Why needed:* Gives the metric on $X$ via pullback through $\Phi$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Regular + second countable ⇒ countable family of separating functions
> **Statement:** Let $X$ be second countable, Hausdorff, regular with countable basis $\mathcal{B}$. There is a countable family $\{f_i : X \to [0, 1]\}_{i \in \mathbb{N}}$ of continuous functions such that for every $x \in X$ and every closed $C \subseteq X$ with $x \notin C$, there exists $i$ with $f_i \equiv 0$ on a neighborhood of $x$ and $f_i \equiv 1$ on $C$.
>
> **Hint:** Index by pairs $(U, V) \in \mathcal{B}^2$ with $\overline U \subseteq V$; for each, construct a separating function via iterated regularity (Urysohn-style dyadic construction inside the regular hypothesis).
>
> **Why needed:** Provides the countable family of coordinates for the Hilbert cube embedding.
>
> > [!note]- Full proof
> > Index the countable basis $\mathcal{B} = \{B_1, B_2, \dots\}$. Let $\mathcal{P} = \{(B_i, B_j) : \overline{B_i} \subseteq B_j\}$ — a countable subset of $\mathbb{N}^2$. For each pair $(B_i, B_j) \in \mathcal{P}$, we claim there is a continuous $f_{ij} : X \to [0, 1]$ with $f_{ij} \equiv 0$ on $\overline{B_i}$ and $f_{ij} \equiv 1$ on $X \setminus B_j$.
> >
> > Construction: this is a Urysohn-style construction *inside the regularity hypothesis*. We do not have normality, but for the *specific* pair $\overline{B_i}, X \setminus B_j$ (which are disjoint), we can construct $f_{ij}$ using iterated regularity. The construction parallels Urysohn's lemma but starts from the regularity-given disjoint opens around $\overline{B_i}$ and $X \setminus B_j$, building dyadic intermediate opens by repeated application of regularity. (This is Bredon Lemma 9.9 in detail.)
> >
> > The family $\{f_{ij}\}$ is countable (parametrized by pairs in $\mathcal{P} \subseteq \mathbb{N}^2$). For any $x \in X$ and closed $C \not\ni x$: regularity gives an open $U \ni x$ with $\overline U \subseteq X \setminus C$, and using the basis we can shrink $U$ to a basis element $B_i \subseteq U$ and find another basis element $B_j$ with $\overline{B_i} \subseteq B_j \subseteq X \setminus C$. Then $(B_i, B_j) \in \mathcal{P}$, and $f_{ij}$ has $f_{ij}(x) = 0$ (since $x \in \overline{B_i}$) and $f_{ij} \equiv 1$ on $C$ (since $C \subseteq X \setminus B_j$).

> [!note]- Lemma 2: The Hilbert cube metric induces the product topology
> **Statement:** On $[0, 1]^\mathbb{N}$, the metric $d(x, y) = \sum_{n=1}^\infty |x_n - y_n|/2^n$ induces the product topology.
>
> **Hint:** Show the metric balls form a basis for the product topology, and vice versa.
>
> **Why needed:** Provides the explicit metric on the Hilbert cube, hence on $X$ via pullback.
>
> > [!note]- Full proof
> > Let $\tau_p$ be the product topology and $\tau_d$ the metric topology.
> >
> > $\tau_d \subseteq \tau_p$: Given a metric ball $B_\varepsilon(x^0)$, take $N$ such that $\sum_{n > N} 1/2^n < \varepsilon/2$, and the product-open set $V = \{x : |x_n - x_n^0| < \varepsilon/2 \text{ for } n \leq N\}$. For $x \in V$, $d(x, x^0) = \sum_{n \leq N} |x_n - x_n^0|/2^n + \sum_{n > N} |x_n - x_n^0|/2^n < (\varepsilon/2)(1) + (\varepsilon/2) = \varepsilon$. So $x^0 \in V \subseteq B_\varepsilon(x^0)$, and $B_\varepsilon(x^0) \in \tau_p$.
> >
> > $\tau_p \subseteq \tau_d$: Given a basic product-open set $V = \{x : |x_{n_i} - x_{n_i}^0| < \varepsilon_i, i = 1, \dots, k\}$ for finitely many coordinates, choose $\delta = \min_i (\varepsilon_i / 2^{n_i})$; then $B_\delta(x^0) \subseteq V$: $d(x, x^0) < \delta$ implies $|x_{n_i} - x_{n_i}^0|/2^{n_i} < \delta \leq \varepsilon_i/2^{n_i}$, so $|x_{n_i} - x_{n_i}^0| < \varepsilon_i$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X$ be second countable, Hausdorff, regular. By Lemma 1, choose a countable family $\{f_i : X \to [0, 1]\}_{i \in \mathbb{N}}$ separating points from closed sets.
>
> **Define the embedding.** Let $\Phi : X \to [0, 1]^\mathbb{N}$ by $\Phi(x) = (f_i(x))_i$.
>
> **Continuity.** Each projection $\pi_i \circ \Phi = f_i$ is continuous, so by the universal property of the product topology, $\Phi$ is continuous.
>
> **Injectivity.** Suppose $\Phi(x) = \Phi(y)$, so $f_i(x) = f_i(y)$ for all $i$. If $x \neq y$, by Hausdorffness there is a closed $C$ containing $y$ but not $x$ (the complement of any open neighborhood of $y$ not containing $x$, with closure inside $X \setminus \{x\}$ — using regularity to get a closed neighborhood of $y$). By Lemma 1, some $f_i$ has $f_i(x) = 0$ and $f_i \equiv 1$ on $C$, so $f_i(y) = 1 \neq 0 = f_i(x)$, contradicting $\Phi(x) = \Phi(y)$. Hence $\Phi$ is injective.
>
> **Open map onto image.** Let $U$ be open in $X$ and $x \in U$. The set $C = X \setminus U$ is closed and $x \notin C$. By Lemma 1, some $f_i$ has $f_i(x) = 0$ and $f_i \equiv 1$ on $C$. The set $W = \{y \in [0, 1]^\mathbb{N} : y_i < 1/2\}$ is open in the product topology and contains $\Phi(x)$. For any $y' \in W \cap \Phi(X)$, write $y' = \Phi(x')$; then $f_i(x') < 1/2$, so $x' \notin C$ (where $f_i \equiv 1$), so $x' \in U$, so $\Phi(x') \in \Phi(U)$. Hence $W \cap \Phi(X) \subseteq \Phi(U)$, showing $\Phi(U)$ is open in $\Phi(X)$.
>
> So $\Phi : X \to \Phi(X) \subseteq [0, 1]^\mathbb{N}$ is a homeomorphism.
>
> **Metrize.** By Lemma 2, the Hilbert cube $[0, 1]^\mathbb{N}$ is metrizable by $d(x, y) = \sum_n |x_n - y_n|/2^n$, with this metric inducing the product topology. Pulling back via $\Phi$ gives a metric $d_X(x, y) = d(\Phi(x), \Phi(y))$ on $X$ that induces the original topology. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Every topological manifold is metrizable.** A topological manifold is defined as Hausdorff, second countable, locally Euclidean. Locally Euclidean implies regular (Euclidean space is regular, and the property is local). Hence Urysohn applies, and every topological manifold is metrizable. The application is foundational: when working with manifolds, one freely assumes a metric (e.g., a Riemannian metric, which exists by partition of unity), and Urysohn metrization is what justifies this.

**The Stone–Čech compactification of $\mathbb{N}$ is not metrizable.** $\beta\mathbb{N}$ is compact Hausdorff, hence regular and normal. But it is *not* second countable — it has cardinality $2^{2^{\aleph_0}}$, while a second countable compact Hausdorff space has cardinality at most $2^{\aleph_0}$. So $\beta\mathbb{N}$ falls outside the Urysohn hypotheses, and indeed it is not metrizable — the sequence $\{1, 2, 3, \dots\} \subseteq \beta\mathbb{N}$ has no convergent subsequence (in a metric space it would, by compactness). This shows the second-countable hypothesis is essential.

**Polish spaces.** A Polish space is a separable completely metrizable space. By Urysohn, separable + Hausdorff + regular gives metrizable; the additional "completely" requires choosing the metric carefully (or extending to a complete metric). Polish spaces are the setting for modern measure-theoretic probability — Daniell–Kolmogorov, regular conditional probabilities, weak convergence of measures. The Urysohn theorem provides the underlying metric.

---

# Bridges

- **[[Def - Completely Regular Space]]** — derived as a step in the proof: regular + second countable ⇒ completely regular.

- **[[Thm - Urysohn's Lemma]]** — the philosophical cousin: produces separating functions from separation axioms. Urysohn's lemma needs normality; Urysohn metrization uses iterated regularity inside second-countability.

- **[[Def - Product Topology]]** — the embedding is into the Hilbert cube, a product space.

- **[[Def - First and Second Countable]]** — second countability is a key hypothesis.

- **Nagata–Smirnov theorem** — the more general metrization theorem (regular + $\sigma$-locally-finite base) that drops second countability.

- **Bing metrization theorem** — another general metrization (collectionwise normal + $\sigma$-discrete base).

---

# Unlocked by This

> [!tip] Every Topological Manifold is Metrizable *(from Differential Geometry)*
> Topological manifolds (Hausdorff + locally Euclidean + second countable) satisfy the Urysohn hypotheses, so they are metrizable. This is the topological underpinning of Riemannian geometry: a Riemannian metric (smoothly varying inner product) exists on every smooth manifold, by partition of unity on the topologically metrizable underlying space.

> [!tip] Polish Spaces *(from Probability)*
> Polish spaces (separable completely metrizable) are the standard setting for measure-theoretic probability. Their metrizability comes from Urysohn metrization (separable Hausdorff regular).

> [!tip] Nagata–Smirnov General Metrization *(from Topology)*
> The **Nagata–Smirnov theorem** characterizes metrizability without second-countability: a topological space is metrizable if and only if it is regular and has a $\sigma$-locally-finite base. This is the general metrization, of which Urysohn is the second-countable special case.

> [!tip] Hilbert Cube as Universal *(from Topology)*
> The Hilbert cube $[0, 1]^\mathbb{N}$ is universal for second-countable metric spaces: every such space embeds in it. Urysohn metrization makes this universality possible by guaranteeing the embedding for the broader class of second-countable Hausdorff regular spaces.
