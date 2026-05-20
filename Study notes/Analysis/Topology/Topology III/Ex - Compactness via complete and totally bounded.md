---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Cauchy Sequence and Complete Metric Space"
  - "Def - Totally Bounded Metric Space"
  - "Thm - Compactness in Metric Spaces (Three Equivalents)"
tags: [analysis, topology]
---

# Problem Statement

Let $(X, d)$ be a metric space. Prove the implication (3) ⇒ (1) of the [[Thm - Compactness in Metric Spaces (Three Equivalents)|metric compactness equivalents]] *directly*, by sequential extraction:

> If $X$ is **complete** and **totally bounded**, then $X$ is **sequentially compact** (every sequence has a convergent subsequence).

(This is, in metric spaces, equivalent to compactness, by the equivalence of compactness and sequential compactness — the part you may use as already-established.)

**Recall:**

A metric space $(X, d)$ is [[Def - Cauchy Sequence and Complete Metric Space|**complete**]] if every Cauchy sequence in $X$ converges in $X$. It is [[Def - Totally Bounded Metric Space|**totally bounded**]] if for every $\varepsilon > 0$ there exists a finite cover by $\varepsilon$-balls — i.e. finitely many points $x_1, \dots, x_N \in X$ with $X = \bigcup_{i=1}^N B_\varepsilon(x_i)$. It is **sequentially compact** if every sequence $\{x_n\}$ has a subsequence converging in $X$.

![[Def - Cauchy Sequence and Complete Metric Space#The Definition]]

![[Def - Totally Bounded Metric Space#The Definition]]

---

# Convergent Strategy

**Problem class.** A *constructive existence* problem: from an arbitrary sequence, produce a convergent subsequence using only complete + totally bounded. The classical proof uses *diagonal subsequence extraction* — at each scale $1/k$, use total boundedness to find a ball containing infinitely many terms of the current subsequence; refine; diagonalize.

**Assumption pattern.** Total boundedness provides, at every scale $\varepsilon$, a finite cover. The pigeonhole principle then forces *some* ball in the cover to contain infinitely many terms of any infinite sequence. Iterating this at finer and finer scales produces a nested sequence of "thinned" sequences, each Cauchy at its own scale. The diagonal takes the $k$-th term of the $k$-th thinning — gathering up Cauchy-ness at every scale.

**Theorem routing.** Total boundedness + pigeonhole at each scale $1/k$ ⇒ infinite-subsequence-in-each-ball, refined to nested sub-subsequences ⇒ diagonal subsequence is Cauchy ⇒ converges by [[Def - Cauchy Sequence and Complete Metric Space|completeness]].

**Key decision point.** The diagonal is the crux. A naive "take the first element from each thinning" subsequence does not work, because successive thinnings are not nested in their *index* — they are nested as *sets of indices*, but the first element of the $k$-th thinning is *not* necessarily later than the first element of the $(k-1)$-th. The diagonal "the $k$-th element of the $k$-th thinning" *is* a subsequence (its indices increase), and it inherits the Cauchy property by lying in the $k$-th thinning past position $k$.

---

# Legal Operations Used

1. **Apply total boundedness at scale $\varepsilon$** to get a finite cover by $\varepsilon$-balls.

2. **Apply pigeonhole** to a finite cover of an infinite set: some cover element contains infinitely many points.

3. **Diagonal subsequence extraction** to combine countably many nested infinite subsequences into a single Cauchy subsequence.

4. **Invoke completeness** to convert a Cauchy subsequence into a convergent subsequence.

---

# Hints

> [!note]- Hint 1
> Use total boundedness at scale $1$: cover $X$ by finitely many $1$-balls; by pigeonhole, some ball contains infinitely many $x_n$'s. Restrict the sequence to this ball — getting a sub-subsequence $\{x_n^{(1)}\}$ all within distance $2$ of each other.

> [!note]- Hint 2
> Iterate: at scale $1/2$, cover $X$ (or the previous ball) by finitely many $1/2$-balls, pigeonhole to a ball containing infinitely many $x_n^{(1)}$, restrict to $\{x_n^{(2)}\}$. Continue at scales $1/k$ to get $\{x_n^{(k)}\}$ with all terms within $2/k$ of each other.

> [!note]- Hint 3
> Diagonal: take $y_k = x_k^{(k)}$. Then for $m, n \geq k$, $y_m$ and $y_n$ both lie in the $1/k$-ball used at stage $k$, so $d(y_m, y_n) < 2/k$. Hence $\{y_k\}$ is Cauchy.

> [!note]- Hint 4
> By [[Def - Cauchy Sequence and Complete Metric Space|completeness]], the Cauchy sequence $\{y_k\}$ converges. So $\{y_k\}$ is a convergent subsequence of $\{x_n\}$.

---

# Solution

Given an arbitrary sequence $\{x_n\}$ in $X$, total boundedness at every scale $1/k$ produces a finite cover; pigeonhole at each scale extracts a sub-subsequence trapped in a small ball; a diagonal of these sub-subsequences is Cauchy; completeness converts Cauchy to convergent.

**Step 1: At every scale $1/k$, some ball contains infinitely many terms of any infinite subsequence.**

> [!note]- Derivation
> Fix $k \geq 1$. By [[Def - Totally Bounded Metric Space|total boundedness]], there exist finitely many points $z_1^{(k)}, \dots, z_{N_k}^{(k)} \in X$ with $X = \bigcup_{i=1}^{N_k} B_{1/k}(z_i^{(k)})$. Given any infinite sequence $\{a_n\}$ in $X$, the index set is partitioned into finitely many subsets according to which $B_{1/k}(z_i^{(k)})$ each $a_n$ falls into (taking the lowest-indexed $i$ if multiple); since the partition has finitely many parts and the index set is infinite, *some* part is infinite (pigeonhole). Hence some $B_{1/k}(z_i^{(k)})$ contains $a_n$ for infinitely many indices $n$.

**Step 2: Iteratively thin the original sequence at scales $1/1, 1/2, 1/3, \dots$**

Construct an infinite nested chain of subsequences $\{x_n^{(0)}\}, \{x_n^{(1)}\}, \{x_n^{(2)}\}, \dots$ where $\{x_n^{(0)}\} = \{x_n\}$, and $\{x_n^{(k)}\}$ is a subsequence of $\{x_n^{(k-1)}\}$ with all terms in a common ball of radius $1/k$.

> [!note]- Derivation
> Start with $\{x_n^{(0)}\} = \{x_n\}$. Suppose $\{x_n^{(k-1)}\}$ is defined and is an infinite subsequence of the original sequence. By Step 1 applied to scale $1/k$, some ball $B_{1/k}(z^{(k)})$ contains infinitely many terms of $\{x_n^{(k-1)}\}$. Let $\{x_n^{(k)}\}$ be the subsequence of $\{x_n^{(k-1)}\}$ consisting of those terms lying in this ball.
>
> By construction, $\{x_n^{(k)}\}$ is a subsequence of $\{x_n^{(k-1)}\}$, all of whose terms lie in $B_{1/k}(z^{(k)})$. In particular, *any two terms* of $\{x_n^{(k)}\}$ are within distance $2/k$ (by triangle inequality through the center $z^{(k)}$).

**Step 3: The diagonal subsequence $y_k = x_k^{(k)}$ is Cauchy.**

> [!note]- Derivation
> *Subsequence-ness.* The sequence $\{y_k\}$ is a subsequence of $\{x_n\}$: define $\{y_k\}$ by reading off the $k$-th term of the $k$-th thinning $\{x_n^{(k)}\}$. The indices in the original sequence are strictly increasing because each $x_n^{(k)}$ is a subsequence of all previous thinnings, so $y_k = x_{n_k}$ for an increasing sequence of indices $\{n_k\}$. (Formally: when extracting $\{x_n^{(k)}\}$ from $\{x_n^{(k-1)}\}$, write each $x_n^{(k)}$ in terms of its position in the original sequence; iterate.)
>
> *Cauchy.* For $m, k \geq k_0$, the sequence $\{x_n^{(k_0)}\}$ contains $y_m$ and $y_k$ as terms (since for $j \geq k_0$, $\{x_n^{(j)}\}$ is a subsequence of $\{x_n^{(k_0)}\}$, so $y_j = x_j^{(j)} \in \{x_n^{(k_0)}\}$). All terms of $\{x_n^{(k_0)}\}$ lie in $B_{1/k_0}(z^{(k_0)})$, so $d(y_m, y_k) \leq 2/k_0$. Hence, for every $\varepsilon > 0$, choosing $k_0 > 2/\varepsilon$, we get $d(y_m, y_k) < \varepsilon$ for all $m, k \geq k_0$ — the Cauchy condition.

**Step 4: Apply completeness.**

By [[Def - Cauchy Sequence and Complete Metric Space|completeness]] of $X$, the Cauchy sequence $\{y_k\}$ converges in $X$. So $\{y_k\}$ is a convergent subsequence of the original sequence $\{x_n\}$. Since $\{x_n\}$ was arbitrary, every sequence in $X$ has a convergent subsequence — $X$ is sequentially compact.

> [!note]- Complete formal solution
> Let $\{x_n\}$ be a sequence in $X$. Inductively construct subsequences: $\{x_n^{(0)}\} = \{x_n\}$, and given $\{x_n^{(k-1)}\}$, choose $z^{(k)} \in X$ such that $B_{1/k}(z^{(k)})$ contains infinitely many terms of $\{x_n^{(k-1)}\}$ (possible by total boundedness + pigeonhole), and let $\{x_n^{(k)}\}$ be the subsequence in this ball. Set $y_k = x_k^{(k)}$, the diagonal. Then $\{y_k\}$ is a subsequence of $\{x_n\}$, and for $m, k \geq k_0$, $y_m, y_k \in B_{1/k_0}(z^{(k_0)})$, so $d(y_m, y_k) \leq 2/k_0$. Hence $\{y_k\}$ is Cauchy, and by completeness it converges. $\blacksquare$

---

# Key Takeaways

**The diagonal subsequence argument is the universal mechanism for converting "infinitely many constraints, each at its own scale" into a single object satisfying all of them.** In this exercise: at scale $1/k$, total boundedness traps the sequence in a small ball; iterating produces nested thinnings each at a finer scale; the diagonal inherits *every* trapping, hence is Cauchy. The same pattern appears throughout analysis: in the Arzelà–Ascoli theorem (extract a uniformly convergent subsequence from a sequence of functions, using equicontinuity and pointwise convergence at countably many points); in the proof of compactness of $L^p$ balls under weak convergence in reflexive spaces; in the existence of solutions to ODEs via Peano's theorem; in the construction of a Brownian motion via dyadic interpolation. Whenever you have "countably many extraction steps, each refining the previous one", the diagonal is the move.

**Total boundedness + completeness *are* compactness, in the metric world.** Total boundedness is the "finite at every scale" property — the metric analog of finite-dimensionality, in some sense. Completeness fills in the limits. The two together perfectly capture compactness, and the [[Thm - Compactness in Metric Spaces (Three Equivalents)|three-equivalents theorem]] makes them interchangeable with both the open-cover and sequential definitions. The intuition: compactness is "the space is small at every scale and contains all its limits". This dual characterization — *fine-scale finitude* (total boundedness) + *limits exist* (completeness) — is often the most computable form. To check compactness of a concrete metric space, you usually verify these two properties directly. Conversely, when total boundedness is *missing* (e.g., the unit ball of an infinite-dimensional Banach space — see [[Ex - LC + Hausdorff is needed for closure-of-open-bounded properties]]), compactness fails.

**The pigeonhole at every scale is the engine.** Total boundedness gives a finite cover at each scale; pigeonhole forces infinitely-many-in-one-cell. This is the most basic possible "finite cover + infinite pigeons" argument, and it is the structural reason finite-dimensional things behave so much better than infinite-dimensional things. In an infinite-dimensional Banach space, the unit ball can be covered by $\varepsilon$-balls *only* in infinitely many of them (no finite cover at small scales), so the pigeonhole step fails, and the diagonal does not yield Cauchy. The trigger: any time you want to extract a convergent subsequence from a bounded sequence, ask whether the boundedness is *total* (uniform-in-scale finite cover) or just *bounded*; only the former works.

**Trigger-reaction: "I have a sequence in a metric space and want a convergent subsequence" ⇒ "check total boundedness + completeness, then diagonal".** This is one of the standard moves in analysis. Examples: (a) any bounded sequence in $\mathbb{R}^n$ has a convergent subsequence (Bolzano–Weierstrass) — by Heine–Borel, bounded sets in $\mathbb{R}^n$ are totally bounded, and $\mathbb{R}^n$ is complete. (b) Any equicontinuous, uniformly bounded sequence of continuous functions on a compact metric space has a uniformly convergent subsequence (Arzelà–Ascoli) — equicontinuity + uniform boundedness give total boundedness in $C(K)$ with the sup norm, and $C(K)$ is complete. (c) Any tight sequence of probability measures on a Polish space has a weakly convergent subsequence (Prokhorov) — tightness gives total-boundedness-in-Lévy-Prokhorov-metric on the probability measure space. Each of these is an instance of "use total boundedness in the right metric, then diagonal extract".

**Why the diagonal works even though individual extractions do not nest in original-sequence index.** The subtlety: a subsequence is *not* the same as a subset of the index set — a subsequence is an order-preserving choice of indices. When you extract $\{x_n^{(k)}\}$ from $\{x_n^{(k-1)}\}$, the indices in the original sequence are sub-indices but not consecutive. The diagonal $y_k = x_k^{(k)}$ chooses the $k$-th index of the $k$-th level. Why does this work? Because the *original* index of $y_k$ is at least the $k$-th original index of $\{x_n^{(k)}\}$, which is at least the $k$-th original index of every earlier level. Since each level is a subsequence of all previous, this chain of inequalities forces the original indices of $\{y_k\}$ to be strictly increasing. This is one of the canonical "index-bookkeeping" arguments in analysis, and getting it right requires care.
