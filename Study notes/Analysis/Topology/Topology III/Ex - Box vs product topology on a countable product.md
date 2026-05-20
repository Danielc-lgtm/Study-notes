---
type: exercise
subject: topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Product Topology"
  - "Thm - Net Convergence in Product is Coordinatewise"
tags: [analysis, topology]
---

# Problem Statement

Consider $\mathbb{R}^\mathbb{N} = \prod_{n=1}^\infty \mathbb{R}$ — the set of all sequences of real numbers — with two competing topologies:

- the [[Def - Product Topology|product topology]], with basis $\prod_n U_n$ where each $U_n \subseteq \mathbb{R}$ is open and $U_n = \mathbb{R}$ for all but finitely many $n$;
- the **box topology**, with basis $\prod_n U_n$ where each $U_n \subseteq \mathbb{R}$ is open (no cofiniteness constraint).

(a) Show that the box topology is *strictly* finer than the product topology.

(b) Consider the sequence $\{x^{(k)}\}_{k=1}^\infty$ in $\mathbb{R}^\mathbb{N}$ defined by $x^{(k)} = (1/k, 1/k, 1/k, \dots)$ — the constant-$1/k$ sequence. Show that $x^{(k)} \to 0$ (the zero sequence) in the **product topology**, but $x^{(k)} \not\to 0$ in the **box topology**.

**Recall:**

A topology $\tau_1$ is **finer** than $\tau_2$ (and $\tau_2$ is **coarser** than $\tau_1$) if $\tau_2 \subseteq \tau_1$, i.e. every $\tau_2$-open set is $\tau_1$-open. *Strictly finer* means $\tau_2 \subsetneq \tau_1$.

A sequence $x^{(k)}$ in a topological space $X$ **converges** to a point $x \in X$ if for every open neighborhood $U$ of $x$ there exists $K$ such that $x^{(k)} \in U$ for all $k \geq K$. Finer topologies have *fewer* convergent sequences: more opens means more neighborhoods to enter, a stricter condition.

In a product space, convergence in the [[Thm - Net Convergence in Product is Coordinatewise|product topology]] is coordinate-by-coordinate: $x^{(k)} \to x$ if and only if $x_n^{(k)} \to x_n$ in $X_n$ for every $n$.

---

# Convergent Strategy

**Problem class.** This is a *topology comparison* exercise: two topologies are defined on the same set, and the task is to determine the inclusion relation between them, plus exhibit a phenomenon (convergence) that distinguishes them. The [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact#Legal Operations|topic page legal operations]] flag the box-vs-product distinction as one of the central "illegal-but-tempting" traps.

**Assumption pattern.** Every product-basic-open set is a box-basic-open set (cofinitely-many factors being $\mathbb{R}$ is a special case of arbitrary opens). So box ⊇ product. The strict inequality must come from a *box-open set that is not product-open*, and the natural choice is a box with *all* factors a proper open: $\prod_n (-1/n^2, 1/n^2)$ has every factor properly bounded, so cannot be a product-basic-open.

**Theorem routing.** For convergence in the product topology, use the coordinate-by-coordinate characterization ([[Thm - Net Convergence in Product is Coordinatewise]]). Each coordinate is constantly $1/k \to 0$, so coordinatewise convergence holds. For non-convergence in box topology, exhibit a specific box neighborhood of $0$ that $x^{(k)}$ never enters — choose factor sizes shrinking faster than $1/k$ for each $k$, e.g. $(-1/n^2, 1/n^2)$ in coordinate $n$. Since $x_n^{(k)} = 1/k$ is fixed across all $n$, no $k$ can satisfy $1/k < 1/n^2$ for *all* $n$ — pick $n$ large enough.

**Key decision point.** Two cleverness points. First, for strict finer, the chosen box must have *every* factor proper — that is what makes it not arise from finitely many cylinders. Second, for non-convergence in box, the box-neighborhood must have factors shrinking *with $n$*; a box where each factor is the same fixed interval $(-\varepsilon, \varepsilon)$ *would* be entered by $x^{(k)}$ for $k > 1/\varepsilon$. The strength of box topology comes from being allowed to coordinate-wise tighten as $n$ grows.

---

# Legal Operations Used

This solution uses these operations from [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact#Legal Operations|the topic page]]:

1. **Compare topologies via basis inclusion.** Show every product-basic-open is box-basic-open, hence product $\subseteq$ box. Exhibit a single box-open not in the product topology to get strict inclusion.

2. **Use coordinatewise convergence in the product topology.** Apply [[Thm - Net Convergence in Product is Coordinatewise]] to reduce convergence in the product to convergence in each factor.

3. **Defeat convergence by exhibiting a single bad neighborhood.** Non-convergence to a point means there exists *some* open neighborhood the sequence fails to eventually enter — finding one such neighborhood is enough.

---

# Hints

> [!note]- Hint 1
> *(a)* A product-basic-open is a special case of a box-basic-open (one where cofinitely many factors are all of $\mathbb{R}$). So every product-open set is box-open. For strict, exhibit a box-open with *every* factor a proper subset — such as $\prod_n (-1/n^2, 1/n^2)$ — and show no product-basic-open of $0$ fits inside it.

> [!note]- Hint 2
> *(b), product convergence:* Use coordinatewise convergence ([[Thm - Net Convergence in Product is Coordinatewise]]). For each $n$, the $n$-th coordinate of $x^{(k)}$ is $1/k \to 0$ as $k \to \infty$.

> [!note]- Hint 3
> *(b), box non-convergence:* Choose a box-neighborhood $U = \prod_n (-1/n^2, 1/n^2)$ of $0$. For $x^{(k)} \in U$ we would need $|1/k| < 1/n^2$ for *every* $n$, but for any fixed $k$ this fails as soon as $n^2 > k$, i.e. $n > \sqrt{k}$.

---

# Solution

The box topology is strictly finer than the product topology because it has "more open sets" — boxes are allowed to be proper in every coordinate. This extra freedom makes convergence in the box topology *much* harder: the sequence has to eventually enter every box, including boxes that tighten with $n$, which the coordinatewise convergence of the product cannot guarantee.

**Step 1: Every product-basic-open is a box-basic-open, so the box topology is finer.**

The product topology has a basis of cylinder products $\prod_n U_n$ where $U_n = \mathbb{R}$ for all but finitely many $n$. Each such set is a particular case of a box product. Hence every product-open set is box-open, and the box topology is finer.

> [!note]- Derivation
> A *product-basic-open* is by definition $\prod_n U_n$ with $U_n \subseteq \mathbb{R}$ open and $U_n = \mathbb{R}$ for $n \notin F$, where $F \subseteq \mathbb{N}$ is finite. A *box-basic-open* is $\prod_n U_n$ with $U_n \subseteq \mathbb{R}$ open and no constraint on the indices. Trivially, every product-basic-open is a box-basic-open (with $U_n = \mathbb{R}$ in cofinitely many slots). Every open set in either topology is a union of its basics, so unions of product-basic-opens are unions of box-basic-opens, hence open in the box topology. So $\tau_{\text{prod}} \subseteq \tau_{\text{box}}$, i.e. the box topology is finer.

**Step 2: The box topology is *strictly* finer.**

Consider $U = \prod_n (-1/n^2, 1/n^2)$ — the box around $0$ with $n$-th factor of width $2/n^2$. This is box-open but not product-open, exhibiting strict containment.

> [!note]- Derivation
> *Box-open:* every factor $(-1/n^2, 1/n^2)$ is open in $\mathbb{R}$, so $U$ is box-basic-open by definition.
>
> *Not product-open:* suppose for contradiction $U$ were a (necessarily nonempty) open set in the product topology containing $0$. Then there would be a product-basic-open $V = \prod_n V_n$ with $0 \in V \subseteq U$ and $V_n = \mathbb{R}$ for $n \notin F$, $F$ finite. Pick any $n_0 \notin F$, so $V_{n_0} = \mathbb{R}$. The point with all coordinates $0$ except the $n_0$-th coordinate equal to $1$ (say) lies in $V$ (any value is allowed in coordinate $n_0$), but its $n_0$-th coordinate is $1 \notin (-1/n_0^2, 1/n_0^2)$ (since $n_0 \geq 1$ gives $1/n_0^2 \leq 1$, and the interval is open so does not contain $1$). So this point is in $V \setminus U$, contradicting $V \subseteq U$. Hence $U$ is not product-open.
>
> Therefore the box topology has an open set not in the product topology, so box is *strictly* finer.

**Step 3: $x^{(k)} \to 0$ in the product topology.**

The sequence converges to the zero sequence in the product topology, because each coordinate converges to $0$ in $\mathbb{R}$.

> [!note]- Derivation
> By [[Thm - Net Convergence in Product is Coordinatewise]], $x^{(k)} \to 0$ in the product topology if and only if $x_n^{(k)} \to 0$ in $\mathbb{R}$ for every fixed $n$. Here $x_n^{(k)} = 1/k$ for every $n$, and $1/k \to 0$ as $k \to \infty$. Coordinatewise convergence holds, so $x^{(k)} \to 0$ in the product topology.
>
> Direct verification via opens: a product-basic-open $V = \prod_n V_n$ around $0$ has $V_n = \mathbb{R}$ for $n \notin F$ (finite) and $V_n$ an open neighborhood of $0$ in $\mathbb{R}$ for $n \in F$. Choose $\varepsilon > 0$ with $(-\varepsilon, \varepsilon) \subseteq V_n$ for *every* $n \in F$ (a finite intersection of open neighborhoods of $0$ in $\mathbb{R}$ is still an open neighborhood of $0$). For $k > 1/\varepsilon$, $|1/k| < \varepsilon$, so $x_n^{(k)} = 1/k \in V_n$ for $n \in F$, and $x_n^{(k)} = 1/k \in \mathbb{R} = V_n$ for $n \notin F$. So $x^{(k)} \in V$ for all $k > 1/\varepsilon$. Convergence in the product topology confirmed.

**Step 4: $x^{(k)} \not\to 0$ in the box topology.**

Exhibit a single box-open neighborhood of $0$ that $x^{(k)}$ never enters.

> [!note]- Derivation
> Take $U = \prod_n (-1/n^2, 1/n^2)$ — the box from Step 2. This is open in the box topology and contains $0$. For $x^{(k)}$ to lie in $U$, we would need
> $$|x_n^{(k)}| = 1/k < 1/n^2 \qquad \text{for every } n.$$
> But for any *fixed* $k$, the inequality $1/k < 1/n^2$ requires $n^2 < k$, i.e. $n < \sqrt{k}$, which fails for all $n \geq \sqrt{k}$. Hence $x^{(k)} \notin U$ for *every* $k$: the sequence never enters $U$, much less eventually. So $x^{(k)} \not\to 0$ in the box topology.

> [!note]- Complete formal solution
> *(a) Finer.* Every product-basic-open $\prod_n U_n$ with $U_n = \mathbb{R}$ outside a finite $F$ is a box-basic-open, so product $\subseteq$ box. The box-open $U = \prod_n (-1/n^2, 1/n^2)$ is not product-open: any product-basic-open inside $U$ would have $U_{n_0} = \mathbb{R}$ for some $n_0$, putting points with arbitrarily large $n_0$-th coordinate inside $U$, contradiction. Hence box is strictly finer.
>
> *(b) Product convergence.* By coordinatewise convergence ([[Thm - Net Convergence in Product is Coordinatewise]]), $x_n^{(k)} = 1/k \to 0$ for every $n$, so $x^{(k)} \to 0$ in product topology.
>
> *(b) Box non-convergence.* In $U = \prod_n (-1/n^2, 1/n^2)$, $x^{(k)} \in U$ requires $1/k < 1/n^2$ for all $n$, impossible for any fixed $k$. So $x^{(k)} \notin U$ for any $k$ and $x^{(k)} \not\to 0$ in box. $\blacksquare$

---

# Key Takeaways

**The product topology is "the right" topology on an infinite product because it is the *coarsest* one making projections continuous — and coarseness is what enables coordinatewise convergence.** The box topology is finer (more open sets, more restrictive convergence) and breaks the equivalence "convergent in product $\iff$ convergent coordinatewise" that makes product topology genuinely useful. In particular, the box topology makes projection-by-projection arguments fail and breaks Tychonoff's theorem: an infinite product of compacta is generally not box-compact (consider $[0, 1]^\mathbb{N}$ with the box topology — it is not even sequentially compact, by an argument similar to this exercise). This is the structural reason topologists almost never use the box topology — the product topology is what is needed to do analysis on function spaces, weak topologies, and dual spaces.

**Finer topologies have fewer convergent sequences.** This is a recurring trigger-reaction pattern: when you make the topology finer (add more opens), you make convergence harder (more neighborhoods to enter eventually). The extreme case is the discrete topology, where every set is open and the only convergent sequences are eventually constant. The opposite extreme is the indiscrete topology, where every sequence converges to every point. The box vs product comparison is in the middle of this spectrum: product convergence is coordinatewise (very generous), box convergence requires uniform-in-some-sense control (much stricter). When working with an unfamiliar topology, identifying its coarseness/fineness relative to the standard product topology often immediately tells you what kinds of sequences converge.

**The mechanism for divergence in the box topology is "the box can tighten with $n$".** This is the *escape-to-infinity* phenomenon transported to a box-topology setting: the sequence $1/k$ is uniform across coordinates, but the box $\prod_n (-1/n^2, 1/n^2)$ refuses to be a single uniform interval — it shrinks coordinate-by-coordinate to absorb the "uniform" sequence's failure to scale with $n$. Recognizing this as the trigger for box-vs-product distinctions: any time you encounter a box where "factor $n$ has size $\varepsilon_n$" with $\varepsilon_n \to 0$, you have a box neighborhood that is not in the product topology, and you have a candidate witness for non-convergence in box.

**The diagonal sequence $x^{(k)}_n = 1/k$ is a model failure case across analysis.** This is the simplest example of a "uniform-in-coordinate, decaying-in-iteration" sequence: it converges coordinatewise but not uniformly across coordinates, since there is no scale at which all coordinates are simultaneously small relative to a shrinking box. Variations of the same sequence appear as counterexamples in many places: a sequence converging weakly but not strongly in $\ell^2$ (the orthonormal basis $e_k$), a sequence converging pointwise but not in $L^1$ (a moving bump), a sequence converging in measure but not almost surely. The general principle: when comparing two convergence notions, the typical counter-example has uniform-in-the-index behavior that the stronger convergence requires control over.

**Trigger-reaction: "is sequential convergence enough to determine the topology?"** First-countable spaces (those with countable neighborhood bases) are characterized by their convergent sequences. Metric spaces are first countable; the product topology on a countable product of metric spaces is first countable (with the standard $\sum 2^{-n} d_n$ metric); the box topology on $\mathbb{R}^\mathbb{N}$ is *not* first countable, because there is no countable neighborhood basis at $0$ — any countable family of boxes can be diagonalized against by a stricter box. This is why the box topology is "pathological" for analysis: sequential reasoning fails. The reaction: whenever a topology is unusually strict, check whether it remains first countable, and if not, switch to nets or filters for convergence arguments.
