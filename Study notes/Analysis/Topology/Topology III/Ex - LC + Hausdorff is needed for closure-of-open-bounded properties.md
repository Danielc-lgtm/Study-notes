---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Locally Compact Space"
  - "Def - Cauchy Sequence and Complete Metric Space"
  - "Thm - Compactness in Metric Spaces (Three Equivalents)"
tags: [analysis, topology]
---

# Problem Statement

Let $\ell^2 = \ell^2(\mathbb{N})$ be the Hilbert space of square-summable real sequences:
$$\ell^2 = \left\{x = (x_n)_{n=1}^\infty \in \mathbb{R}^\mathbb{N} : \sum_n x_n^2 < \infty\right\},$$
with inner product $\langle x, y \rangle = \sum_n x_n y_n$ and induced norm $\lVert x \rVert = (\sum_n x_n^2)^{1/2}$. Let $e_n \in \ell^2$ be the standard basis vector with $1$ in position $n$ and $0$ elsewhere, and let $\overline{B} = \{x \in \ell^2 : \lVert x \rVert \leq 1\}$ be the closed unit ball.

(a) Show that $\overline{B}$ is *bounded* and *closed* in $\ell^2$.

(b) Show that $\overline{B}$ is *not* compact: the sequence $\{e_n\}_{n=1}^\infty$ lies in $\overline{B}$ but has no convergent subsequence.

(c) Conclude that $\ell^2$ is *not* [[Def - Locally Compact Space|locally compact]]: the point $0 \in \ell^2$ has no compact neighborhood.

Thus the **Heine–Borel theorem** ("closed + bounded ⇒ compact") *fails* in infinite-dimensional Hilbert space, and the LCH hypothesis is genuinely needed for all the constructions of [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III §11]].

**Recall:**

A space $X$ is **[[Def - Locally Compact Space|locally compact]]** if every point has a compact neighborhood. Equivalently in Hausdorff: every point has a neighborhood basis of compact neighborhoods.

![[Def - Locally Compact Space#The Definition]]

A metric space is **compact** iff it is **complete** and **totally bounded** ([[Thm - Compactness in Metric Spaces (Three Equivalents)|three-equivalents theorem]]). For sequences, equivalent to: every sequence has a convergent subsequence. In $\mathbb{R}^n$, *Heine–Borel* says closed + bounded ⇒ compact. This statement is false in infinite-dimensional normed spaces.

---

# Convergent Strategy

**Problem class.** A *counterexample* exercise: exhibit an infinite-dimensional Banach space whose closed unit ball is non-compact, witnessing the failure of Heine–Borel and of local compactness. The orthonormal sequence $\{e_n\}$ is the canonical witness, with pairwise distances $\sqrt 2$.

**Assumption pattern.** $\ell^2$ has infinitely many *orthogonal* directions $e_n$, each unit vector. Distances between distinct $e_n$ and $e_m$ are $\sqrt 2$ — uniformly bounded *away* from $0$. This rules out any convergent subsequence in $\ell^2$, because a convergent sequence is Cauchy, hence has pairwise distances going to $0$.

**Theorem routing.**
- *Boundedness:* $\lVert x \rVert \leq 1 \implies$ bounded.
- *Closedness:* $\overline B$ is the preimage of $(-\infty, 1]$ under the continuous norm function $x \mapsto \lVert x \rVert$.
- *Non-compactness:* compute $\lVert e_n - e_m \rVert = \sqrt 2$ for $n \neq m$, so the sequence has no Cauchy subsequence, hence no convergent subsequence.
- *Non-local-compactness:* any compact set in $\ell^2$ has empty interior (in any infinite-dimensional Banach space, compact ⇒ no interior). So $0$ has no compact neighborhood.

**Key decision point.** The unit-distance orthonormal basis is the simplest witness, but the *structural reason* is that infinite dimensions allow infinitely many "directions" that cannot be simultaneously approximated. The compact subset of a Banach space must be *totally bounded*, and total boundedness requires finite-$\varepsilon$-coverings — which fail for the orthonormal basis at $\varepsilon = \sqrt 2 / 2$.

---

# Legal Operations Used

1. **Use total boundedness as the operational form of compactness in metric spaces.** Compact ⇔ complete + totally bounded. To disprove compactness, exhibit a non-totally-bounded structure.

2. **Compute distances between basis vectors directly.** In $\ell^2$, $\lVert e_n - e_m \rVert^2 = 2$ by orthogonality.

3. **Use "convergent ⇒ Cauchy ⇒ pairwise distances small" as the obstruction.** A bounded sequence with pairwise distances bounded *away* from $0$ has no convergent subsequence.

4. **Argue non-local-compactness via "compact ⇒ no interior in infinite dimension".** Riesz's theorem: a Banach space is finite-dimensional iff its closed unit ball is compact iff it is locally compact.

---

# Hints

> [!note]- Hint 1
> *(a) Boundedness.* For $x \in \overline B$, $\lVert x \rVert \leq 1$ — bounded by $1$ in the norm. *Closedness:* $\overline B = \lVert \cdot \rVert^{-1}([0, 1])$, preimage of a closed set under the continuous norm, hence closed.

> [!note]- Hint 2
> *(b) Non-compactness.* Compute $\lVert e_n - e_m \rVert$ for $n \neq m$. By orthogonality, $\lVert e_n - e_m \rVert^2 = \lVert e_n \rVert^2 + \lVert e_m \rVert^2 = 2$, so $\lVert e_n - e_m \rVert = \sqrt 2$.

> [!note]- Hint 3
> If $\{e_{n_k}\}$ were a convergent subsequence, it would be Cauchy: $\lVert e_{n_k} - e_{n_l} \rVert \to 0$ as $k, l \to \infty$. But $\lVert e_{n_k} - e_{n_l} \rVert = \sqrt 2$ for $k \neq l$ — no convergence.

> [!note]- Hint 4
> *(c) Non-local-compactness.* If $0$ had a compact neighborhood $K$, $K$ would contain some closed ball $\overline B_r(0)$. By scaling, $\overline B = (1/r) \overline B_r(0)$ would be compact — contradicting (b).

---

# Solution

The infinite-dimensionality of $\ell^2$ supplies infinitely many orthogonal directions $e_n$, each at distance $\sqrt 2$ from all others. This pairwise separation rules out total boundedness of the unit ball, and hence its compactness. The same obstruction shows $\ell^2$ is not locally compact.

**Step 1: $\overline B$ is bounded.**

> [!note]- Derivation
> By definition, $\overline B = \{x : \lVert x \rVert \leq 1\}$, so every element has norm $\leq 1$ — this *is* the boundedness condition. In any normed space, "bounded" means "the norm is bounded on the set".

**Step 2: $\overline B$ is closed in $\ell^2$.**

> [!note]- Derivation
> The norm $\lVert \cdot \rVert : \ell^2 \to [0, \infty)$ is continuous (in fact $1$-Lipschitz: $|\lVert x \rVert - \lVert y \rVert| \leq \lVert x - y \rVert$ by the reverse triangle inequality). The set $[0, 1] \subseteq \mathbb{R}$ is closed. Hence $\overline B = \lVert \cdot \rVert^{-1}([0, 1])$ is the preimage of a closed set under a continuous map, hence closed.

**Step 3: The sequence $\{e_n\}$ in $\overline B$ has pairwise distances $\sqrt 2$.**

> [!note]- Derivation
> Each $e_n$ has $\lVert e_n \rVert = 1$, so $e_n \in \overline B$ for every $n$. For $n \neq m$, by orthogonality $\langle e_n, e_m \rangle = 0$, so
> $$\lVert e_n - e_m \rVert^2 = \langle e_n - e_m, e_n - e_m \rangle = \lVert e_n \rVert^2 - 2\langle e_n, e_m \rangle + \lVert e_m \rVert^2 = 1 - 0 + 1 = 2.$$
> Hence $\lVert e_n - e_m \rVert = \sqrt 2$ for every $n \neq m$.

**Step 4: $\{e_n\}$ has no convergent subsequence.**

> [!note]- Derivation
> Suppose for contradiction $\{e_{n_k}\}_k$ is a convergent subsequence with limit $x \in \ell^2$. Then $\{e_{n_k}\}$ is Cauchy:
> $$\forall \varepsilon > 0, \exists K, \forall k, l \geq K : \lVert e_{n_k} - e_{n_l} \rVert < \varepsilon.$$
> Pick $\varepsilon = 1 < \sqrt 2$. Then for $k, l \geq K$ with $k \neq l$ (which exists since the indices $n_k$ are distinct), $\lVert e_{n_k} - e_{n_l} \rVert = \sqrt 2 > 1$ — contradicting $< 1$.
>
> So no subsequence is Cauchy, hence no subsequence converges. Hence $\overline B$ is not sequentially compact — in a metric space, this is the same as not compact, by the [[Thm - Compactness in Metric Spaces (Three Equivalents)|three-equivalents theorem]].

**Step 5: $\ell^2$ is not locally compact.**

The point $0$ has no compact neighborhood.

> [!note]- Derivation
> Suppose for contradiction $K \subseteq \ell^2$ were a compact neighborhood of $0$. Then $K$ contains some open ball $B_r(0) = \{x : \lVert x \rVert < r\}$ with $r > 0$, hence contains the closed ball $\overline B_{r/2}(0)$ (closure of a smaller open ball). A closed subset of a compact set is compact (closed in compact ⇒ compact), so $\overline B_{r/2}(0)$ is compact.
>
> But $\overline B_{r/2}(0) = (r/2) \cdot \overline B$ via the scaling map $x \mapsto (r/2)x$ (a homeomorphism $\ell^2 \to \ell^2$). Homeomorphisms preserve compactness, so $\overline B$ would be compact — contradicting Step 4.
>
> Hence $0$ has no compact neighborhood, and $\ell^2$ is not locally compact.
>
> *By translation, $\ell^2$ is not locally compact at any point* — translation is a homeomorphism, so if any point had a compact neighborhood, then $0$ would too.

> [!note]- Complete formal solution
> *(a)* $\overline B = \lVert \cdot \rVert^{-1}([0, 1])$ is closed; bounded by $1$ in norm.
>
> *(b)* $\lVert e_n - e_m \rVert^2 = 2$ for $n \neq m$ by orthogonality, so $\lVert e_n - e_m \rVert = \sqrt 2$. No subsequence can be Cauchy, hence none converges. So $\overline B$ is not (sequentially) compact.
>
> *(c)* If $0$ had compact neighborhood $K \supseteq \overline B_r(0)$, then $\overline B_{r/2}(0) \subseteq K$ would be compact, so $\overline B = (2/r) \overline B_{r/2}(0)$ compact — contradiction. $\ell^2$ is not locally compact. $\blacksquare$

---

# Key Takeaways

**Heine–Borel ("closed + bounded ⇒ compact") is *finite-dimensional*; in infinite dimensions, it fails dramatically.** This is one of the most important phase transitions in analysis: the moment you cross from $\mathbb{R}^n$ to a Banach space (or even a finite-dimensional space with a non-standard topology), the bounded subsets stop being compact, and the entire toolkit of "extract convergent subsequence from bounded sequence" breaks. The replacement, for many purposes, is *weak* compactness: in reflexive Banach spaces, the closed unit ball is weakly compact (Banach–Alaoglu). The weak topology has fewer open sets, so more sequences converge — at the cost that weak limits are usually not strong limits. This is the recurring story of infinite-dimensional analysis: the topology has to be relaxed to keep compactness, and then one has to handle the resulting weakness.

**The trigger-reaction "closed + bounded" ⇒ "compact" is *forbidden* outside finite dimensions.** This is one of the four "illegal but tempting" operations called out in the topic page. Always check whether the space is finite-dimensional before applying Heine–Borel. The "correct" replacement in metric spaces is "complete + totally bounded ⇒ compact" — but total boundedness is *much* stronger than boundedness in infinite dimensions (it requires finite-$\varepsilon$ covers, which the unit ball fails for $\varepsilon < \sqrt 2 / 2$ in $\ell^2$). Identifying the right replacement (weak compactness, Arzelà–Ascoli equicontinuity, Prokhorov's tightness for measures, Frechét–Kolmogorov for $L^p$) is part of the craft of infinite-dimensional analysis.

**Riesz's theorem: a Banach space is finite-dimensional if and only if its closed unit ball is compact if and only if it is locally compact.** This exercise is the negative half. The positive half: in finite-dimensional Banach spaces, all norms are equivalent, and the closed unit ball is homeomorphic to a closed Euclidean ball, hence compact. So local compactness exactly *measures* finite-dimensionality for Banach spaces — and it is one of the cleanest characterizations of finite-dimensional vs. infinite-dimensional. The structural consequence: any time you need local compactness (Riesz representation, LCA groups, Haar measure, one-point compactification), you are restricted to finite-dimensional or otherwise "small" spaces; on infinite-dimensional Banach spaces, these tools fail unless you switch to weak topologies.

**The orthonormal sequence $\{e_n\}$ in $\ell^2$ is the prototype "no convergent subsequence" sequence in infinite dimensions.** It is uniformly bounded ($\lVert e_n \rVert = 1$), uniformly separated ($\lVert e_n - e_m \rVert = \sqrt 2$), and weakly convergent to $0$ (every continuous linear functional $\phi$ on $\ell^2$ has $\phi(e_n) = \langle e_n, \xi_\phi \rangle = \xi_n \to 0$ as the coordinates of $\xi_\phi \in \ell^2$ decay). So this sequence is the canonical example showing the *gap* between strong and weak convergence in Hilbert space — a recurring motif throughout functional analysis. Recognizing it (or variants: orthonormal sequences in $L^2$, Fourier basis $e^{inx}$ on $L^2[0, 2\pi]$) is part of the standard toolkit.

**Trigger-reaction: "I want compactness of a bounded set in an infinite-dimensional setting" ⇒ "switch to weak topology, or impose equicontinuity / tightness".** The standard moves: in reflexive Banach spaces, use Banach–Alaoglu (closed unit ball of the dual is weak-$*$ compact); in function spaces $C(K)$, use Arzelà–Ascoli (uniformly bounded + equicontinuous ⇒ relatively compact); in measure spaces, use Prokhorov (tight ⇒ relatively weakly compact); in $L^p$ spaces, use Frechét–Kolmogorov ($L^p$-equicontinuity + uniform tail decay). Each is the *replacement* for Heine–Borel in its setting, and each adds a hypothesis (the missing equicontinuity, tightness, or uniformity) to compensate for the failure of bounded ⇒ compact.

**The structural lesson: $\sigma$-compactness, second countability, and separability survive infinite dimensions, but local compactness does not.** $\ell^2$ is *separable* (the rational sequences are dense), *second countable* (separable + metric ⇒ second countable), and *complete* (Hilbert spaces are complete by definition). It is *not* locally compact, not $\sigma$-compact (a $\sigma$-compact metric space is the countable union of compact sets, hence has $\sigma$-finite Lebesgue-type measure; on $\ell^2$ no such structure exists). This delineates the *separability* property (preserved into infinite dimensions, leading to Polish spaces, Banach spaces, Hilbert spaces) from the *local compactness* property (lost in infinite dimensions). Polish space theory, Banach space theory, and modern probability all live with separability but without local compactness — and the tools they use (tightness, weak compactness, measurability arguments) reflect this.
