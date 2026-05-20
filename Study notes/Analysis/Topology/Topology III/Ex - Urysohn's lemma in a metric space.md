---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Thm - Urysohn's Lemma"
  - "Def - Metric Space"
tags: [analysis, topology]
---

# Problem Statement

Let $(X, d)$ be a metric space and let $F, G \subseteq X$ be disjoint, nonempty, closed subsets. Define the function $f : X \to [0, 1]$ by
$$f(x) = \frac{d(x, F)}{d(x, F) + d(x, G)},$$
where $d(x, A) = \inf_{a \in A} d(x, a)$ is the distance from $x$ to a set $A$.

(a) Show that the function $x \mapsto d(x, A)$ is continuous (in fact $1$-Lipschitz) for any nonempty $A \subseteq X$.

(b) Show that for *closed* $A$, $d(x, A) = 0 \iff x \in A$.

(c) Show that the denominator $d(x, F) + d(x, G)$ never vanishes on $X$, so $f$ is well-defined.

(d) Verify that $f$ is continuous, $f|_F \equiv 0$, $f|_G \equiv 1$.

This is an explicit **Urysohn function** for the disjoint closed sets $F$ and $G$ in any metric space — a constructive realization of [[Thm - Urysohn's Lemma|Urysohn's lemma]], without invoking the abstract dyadic-rationals construction.

**Recall:**

[[Thm - Urysohn's Lemma|Urysohn's lemma]] says: if $X$ is normal and $F, G \subseteq X$ are disjoint closed, there exists a continuous $f : X \to [0, 1]$ with $f|_F \equiv 0$ and $f|_G \equiv 1$. Metric spaces are normal, so this applies; this exercise gives an explicit construction.

The distance to a set $d(x, A) = \inf_{a \in A} d(x, a)$ is the metric-space replacement for "characteristic function" — it equals $0$ on $\overline{A}$ and increases linearly as $x$ moves away.

---

# Convergent Strategy

**Problem class.** *Explicit function construction* — produce a specific continuous function with prescribed boundary values, in a setting (metric spaces) where the abstract Urysohn construction is overkill. The metric structure gives a *quantitative* function $d(x, A)$ that does most of the work.

**Assumption pattern.** Two closed sets, disjoint, in a metric space. The two distance functions $d(x, F)$ and $d(x, G)$ are continuous, vanish exactly on $F$ and $G$ respectively (by closedness), and at least one is positive at every point (by disjointness). The normalized ratio $d(x, F)/(d(x, F) + d(x, G))$ is then $0$ on $F$, $1$ on $G$, and lies in $[0, 1]$ everywhere.

**Theorem routing.** The reverse triangle inequality gives $|d(x, A) - d(y, A)| \leq d(x, y)$ — distance is $1$-Lipschitz. Lipschitz implies continuous. The ratio of continuous functions, with non-vanishing denominator, is continuous.

**Key decision point.** The two ingredients are *closedness* (so $d(x, A) = 0 \iff x \in A$ for closed $A$ — this fails without closedness, e.g. $d(0, (0, 1)) = 0$) and *disjointness* (so denominator never vanishes — neither $F$ nor $G$ contains a point of the other). Both must be in the hypothesis; weakening either breaks the construction.

---

# Legal Operations Used

1. **Use $d(x, A) = \inf_{a \in A} d(x, a)$ as the "soft characteristic function" of $A$.** Continuous, $1$-Lipschitz, vanishes on $\overline A$, positive outside $\overline A$.

2. **Apply the reverse triangle inequality** to get Lipschitz continuity of $x \mapsto d(x, A)$.

3. **Form a normalized ratio of two distance functions** to get a function with values in $[0, 1]$ and prescribed boundary behavior.

4. **Use closedness of $A$ to convert $d(x, A) = 0$ into $x \in A$**, and disjointness to ensure non-vanishing denominator.

---

# Hints

> [!note]- Hint 1
> *(a) Lipschitz.* For any $a \in A$, $d(x, a) \leq d(x, y) + d(y, a)$. Taking infimum over $a$: $d(x, A) \leq d(x, y) + d(y, A)$, so $d(x, A) - d(y, A) \leq d(x, y)$. Symmetric, hence $|d(x, A) - d(y, A)| \leq d(x, y)$.

> [!note]- Hint 2
> *(b) Closed $A$, $d(x, A) = 0 \implies x \in A$.* If $d(x, A) = 0$ then there exist $a_n \in A$ with $d(x, a_n) \to 0$, so $a_n \to x$. $A$ closed means $A$ contains its limits, so $x \in A$.

> [!note]- Hint 3
> *(c) Non-vanishing denominator.* If $d(x, F) + d(x, G) = 0$ then $d(x, F) = d(x, G) = 0$, so by (b) $x \in F \cap G$, contradicting disjointness.

> [!note]- Hint 4
> *(d) Continuity.* Numerator and denominator are continuous (sum/ratio of continuous), and denominator is bounded away from $0$ on any bounded region (since continuous, positive, on a compact set is bounded below — but for continuity at a single point it suffices that the denominator is positive at $x$, which it is everywhere).

---

# Solution

The function $f(x) = d(x, F)/(d(x, F) + d(x, G))$ is the metric-space Urysohn function, built from the *distance-to-a-set* function, which is the natural quantitative surrogate for "characteristic function" in a metric setting.

**Step 1: $x \mapsto d(x, A)$ is $1$-Lipschitz (in particular, continuous) for any nonempty $A \subseteq X$.**

> [!note]- Derivation
> For any $a \in A$ and any $x, y \in X$, the triangle inequality gives $d(x, a) \leq d(x, y) + d(y, a)$. Taking infimum over $a \in A$ (with $x, y$ fixed):
> $$d(x, A) = \inf_{a \in A} d(x, a) \leq d(x, y) + \inf_{a \in A} d(y, a) = d(x, y) + d(y, A).$$
> So $d(x, A) - d(y, A) \leq d(x, y)$. Swapping $x \leftrightarrow y$ gives $d(y, A) - d(x, A) \leq d(x, y)$, hence $|d(x, A) - d(y, A)| \leq d(x, y)$.
>
> This is the *Lipschitz constant $1$* estimate for the distance-to-$A$ function. Lipschitz with constant $L$ implies continuous (take $\delta = \varepsilon/L$ for $L > 0$), so $x \mapsto d(x, A)$ is continuous.

**Step 2: For closed $A$, $d(x, A) = 0 \iff x \in A$.**

> [!note]- Derivation
> If $x \in A$, then $d(x, x) = 0 \in \{d(x, a) : a \in A\}$, so $d(x, A) = 0$.
>
> Conversely, suppose $d(x, A) = 0$. Then for every $n$ there exists $a_n \in A$ with $d(x, a_n) < 1/n$, so $a_n \to x$ in $X$. $A$ is closed, so the limit of any convergent sequence in $A$ lies in $A$: $x \in A$.
>
> *Closedness is essential.* For $A = (0, 1)$ in $\mathbb{R}$ (not closed), $d(0, A) = 0$ but $0 \notin A$.

**Step 3: The denominator $d(x, F) + d(x, G)$ is strictly positive everywhere.**

> [!note]- Derivation
> If $d(x, F) + d(x, G) = 0$ at some $x$, then both $d(x, F) = 0$ and $d(x, G) = 0$ (sum of non-negatives). By Step 2 (using closedness of $F$ and $G$), $x \in F$ and $x \in G$, so $x \in F \cap G$. But $F \cap G = \emptyset$ by disjointness — contradiction. So the denominator is everywhere strictly positive.

**Step 4: $f$ is continuous, $f|_F \equiv 0$, $f|_G \equiv 1$.**

> [!note]- Derivation
> *Continuity.* $f = d(\cdot, F)/(d(\cdot, F) + d(\cdot, G))$. Numerator and denominator are continuous (by Step 1), and denominator is everywhere positive (Step 3), so the ratio is continuous (standard arithmetic of continuous functions). Range $[0, 1]$ because $0 \leq d(x, F) \leq d(x, F) + d(x, G)$.
>
> *Values on $F$.* For $x \in F$, $d(x, F) = 0$, so $f(x) = 0/(0 + d(x, G)) = 0$.
>
> *Values on $G$.* For $x \in G$, $d(x, G) = 0$, so $f(x) = d(x, F)/(d(x, F) + 0) = 1$.

> [!note]- Complete formal solution
> *(a)* For $a \in A$, $d(x, a) \leq d(x, y) + d(y, a)$, so $d(x, A) \leq d(x, y) + d(y, A)$; by symmetry $|d(x, A) - d(y, A)| \leq d(x, y)$.
>
> *(b)* If $x \in A$, $d(x, A) = 0$. Conversely, if $d(x, A) = 0$, $\exists a_n \in A$ with $d(x, a_n) \to 0$, so $a_n \to x$, hence $x \in \overline A = A$.
>
> *(c)* If $d(x, F) + d(x, G) = 0$, both terms vanish, so by (b) $x \in F \cap G = \emptyset$, contradiction.
>
> *(d)* $f$ is continuous as a ratio of continuous with non-vanishing denominator. $f|_F = 0/(0 + d(x, G)) = 0$. $f|_G = d(x, F)/(d(x, F) + 0) = 1$. $\blacksquare$

---

# Key Takeaways

**The distance function $d(x, A)$ is the metric-space Urysohn function in disguise.** It is continuous (in fact $1$-Lipschitz), vanishes exactly on closed $A$, and grows linearly as $x$ moves away. This is the cleanest analog of a "characteristic function" in a metric setting — soft, continuous, but with a sharp boundary at $A$. Recognizing $d(\cdot, A)$ as a continuous-function-on-$X$ is one of the standard moves of metric space analysis. The general lesson: any time you need a continuous function that "knows about" a closed subset, $d(\cdot, A)$ is the first candidate. It feeds into the construction of partitions of unity, of approximations to step functions, and of [[Thm - Urysohn's Lemma|Urysohn functions]] generally.

**The reverse triangle inequality $|d(x, A) - d(y, A)| \leq d(x, y)$ is the structural reason metric-space arguments are quantitatively clean.** Lipschitz continuity with the *sharp* constant $1$ is what makes distance-based constructions stable: small perturbations in the point cause small perturbations in the distance. This is the analog of the reverse triangle inequality for the metric itself (see [[Ex - The completion of a metric space]]), now applied to a set rather than a single point. The triple uses of this Lipschitz estimate — continuity of $d(\cdot, A)$, well-definedness of $\inf$ over a closed set, stability of approximation arguments — are pervasive throughout analysis.

**The general principle "$d(\cdot, F) = 0$ characterizes $\overline F$, hence $F$ for closed $F$" connects distance to closure.** In metric spaces, the closure of a set is "the zero set of the distance function" — a striking re-expression that converts a topological notion (closure) into an analytical one (zero set). This is the *engine* of (a) why metric spaces have so much function-rich structure (every closed set is the zero set of a continuous function), and (b) why metric implies normal (separate two disjoint closed sets by their distance functions, exactly as in this exercise). The same logic transfers to other settings where there is a "distance-like" function — Hilbert space norms, semimetric quotients, sup-norm on bounded function spaces.

**Metric implies normal: this exercise *is* the proof.** A normal space is one where any two disjoint closed sets are separated by disjoint opens. In a metric space, the function $f$ constructed here lets us take $U = f^{-1}([0, 1/3))$ and $V = f^{-1}((2/3, 1])$ — disjoint opens (continuous preimages of disjoint opens) containing $F$ and $G$ respectively. So every metric space is normal. This is the cleanest entry of metric spaces into the separation hierarchy: regular (in fact completely regular, in fact normal) for free. By [[Thm - Urysohn Metrization Theorem|the Urysohn metrization theorem]], this matches up: the metrizable spaces sit inside the normal spaces.

**Trigger-reaction: "I need a continuous function separating two closed sets in a metric space" ⇒ "use $d(x, F)/(d(x, F) + d(x, G))$".** This is the standard recipe in metric space analysis, and it is much cleaner than the abstract Urysohn construction. The same construction generalizes: for *three* pairwise disjoint closed sets $F_1, F_2, F_3$ in a metric space, the maps $f_i = d(\cdot, F_i)/(d(\cdot, F_1) + d(\cdot, F_2) + d(\cdot, F_3))$ give a *partition of unity* subordinate to the cover $\{X \setminus F_j : j \neq i\}$. The trick scales to any locally finite collection of closed sets — the explicit partitions of unity used throughout differential geometry are built from this metric-space recipe combined with a paracompactness argument.

**The construction fails (and Urysohn must be invoked abstractly) precisely when no metric is in scope.** In a normal but non-metrizable space, you have *no* function $d(\cdot, A)$ to leverage; you must build the Urysohn function abstractly via the dyadic-rationals construction. The exercise *Failure of Tietze without normality* shows what happens when even normality fails. The hierarchy of constructions: metric ⇒ explicit Urysohn (this exercise); normal non-metric ⇒ abstract Urysohn (proof in the topic page); Hausdorff non-normal ⇒ no Urysohn at all (see [[Ex - Failure of Tietze without normality]]).
