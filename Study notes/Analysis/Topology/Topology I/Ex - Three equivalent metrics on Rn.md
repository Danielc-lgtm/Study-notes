---
type: exercise
subject: topology
difficulty: "⭐"
prereqs:
  - "Def - Metric Space"
  - "Def - Equivalent Metrics"
  - "Def - Open and Closed Sets in a Metric Space"
tags: [analysis, topology]
---

# Problem Statement

On $\mathbb{R}^n$, define three metrics:
$$d_1(x, y) = \sum_{i=1}^n |x_i - y_i|, \qquad d_2(x, y) = \left(\sum_{i=1}^n (x_i - y_i)^2\right)^{1/2}, \qquad d_\infty(x, y) = \max_{1 \leq i \leq n} |x_i - y_i|.$$

These are the $\ell^1$ (taxicab), $\ell^2$ (Euclidean), and $\ell^\infty$ (sup) metrics on $\mathbb{R}^n$.

1. Prove the comparison inequalities
$$d_\infty(x, y) \leq d_2(x, y) \leq d_1(x, y) \leq n \cdot d_\infty(x, y).$$
2. Deduce that $d_1, d_2, d_\infty$ are pairwise [[Def - Equivalent Metrics|topologically equivalent]] on $\mathbb{R}^n$.
3. Comment on why the analogous statement *fails* in infinite dimensions — that is, in the sequence spaces $\ell^1, \ell^2, \ell^\infty$ — and what changes.

**Recall:**

![[Def - Equivalent Metrics#The Definition]]

Two metrics $d, \rho$ on the same set $X$ are [[Def - Equivalent Metrics|topologically equivalent]] iff they generate the same open sets, equivalently iff every $d$-ball about a point contains a $\rho$-ball about the same point and vice versa. A sufficient (and stronger) condition is the **Lipschitz comparison**: $C_1 \cdot \rho \leq d \leq C_2 \cdot \rho$ for some constants $C_1, C_2 > 0$. This forces every $\rho$-ball of radius $r$ to contain a $d$-ball of radius $C_1 r$, and every $d$-ball of radius $r$ to contain a $\rho$-ball of radius $r/C_2$.

The **Cauchy–Schwarz inequality** in $\mathbb{R}^n$ states $\sum a_i b_i \leq (\sum a_i^2)^{1/2} (\sum b_i^2)^{1/2}$ for nonnegative $a_i, b_i$; equivalently $\sum |x_i| \leq \sqrt{n} \cdot (\sum x_i^2)^{1/2}$ by taking $a_i = |x_i|, b_i = 1$.

---

# Convergent Strategy

**Problem class.** Compare three explicit metrics on a familiar set via numerical inequalities, then read off topological equivalence from a Lipschitz comparison.

**Assumption pattern.** All three metrics are *translation-invariant* — $d(x, y)$ depends only on the difference $x - y$ — so the inequalities reduce to comparison of three *norms* on $\mathbb{R}^n$:
$$\|v\|_\infty = \max |v_i|, \qquad \|v\|_2 = \sqrt{\sum v_i^2}, \qquad \|v\|_1 = \sum |v_i|.$$

**Theorem routing.** Each inequality in the chain $\|v\|_\infty \leq \|v\|_2 \leq \|v\|_1 \leq n \|v\|_\infty$ has a one-line elementary proof: the sup-vs-sum inequalities are immediate, and the only nontrivial step is $\|v\|_2 \leq \|v\|_1$, which follows from $\sqrt{\sum v_i^2} \leq \sqrt{(\sum |v_i|)^2} = \sum |v_i|$ (or, equivalently, Cauchy–Schwarz). Once the chain is established, topological equivalence follows from the general principle "Lipschitz comparison $\Rightarrow$ topological equivalence", because every ball in one metric contains a ball in the other.

**Key decision point.** The non-obvious part is the *constant $n$* in the last inequality $\|v\|_1 \leq n \|v\|_\infty$. This constant *grows with dimension*, and as $n \to \infty$ the comparison becomes useless: the ratio $\|v\|_1 / \|v\|_\infty$ is unbounded over $\ell^\infty$. This is exactly why infinite-dimensional sequence spaces $\ell^1, \ell^2, \ell^\infty$ are *not* equivalent.

---

# Legal Operations Used

This solution deploys the following operations from [[Topology I — §1–3 Metric and Topological Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Compare norms by pointwise inequalities on coefficients.** Each entry of $v$ satisfies $|v_i| \leq \|v\|_\infty$, $|v_i|^2 \leq \|v\|_\infty^2$, and so on — these are the building blocks.

2. **Use the "Lipschitz comparison implies topological equivalence" criterion.** If $C_1 \rho \leq d \leq C_2 \rho$, then every $d$-ball of radius $r$ contains the $\rho$-ball of radius $r/C_2$ (because $\rho < r/C_2 \Rightarrow d \leq C_2 \rho < r$), and similarly in reverse. So balls in one metric refine balls in the other, and the topologies coincide.

3. **Use Cauchy–Schwarz to compare $\ell^2$ with $\ell^1$.** $\sum |x_i| = \sum |x_i| \cdot 1 \leq \sqrt{\sum |x_i|^2} \sqrt{\sum 1} = \sqrt{n} \|x\|_2$, giving $\|x\|_1 \leq \sqrt{n} \|x\|_2$.

---

# Hints

> [!note]- Hint 1
> Reduce everything to norms: $d_p(x, y) = \|x - y\|_p$, so all three inequalities are inequalities between norms of a single vector $v = x - y$.

> [!note]- Hint 2
> Each inequality has a one-line proof. *$\|v\|_\infty \leq \|v\|_2$:* the maximum is at most the square root of the sum of squares (the max squared is one of the summands). *$\|v\|_2 \leq \|v\|_1$:* $(\sum |v_i|)^2 \geq \sum |v_i|^2$ since cross terms are nonnegative. *$\|v\|_1 \leq n \|v\|_\infty$:* each summand bounded by the max.

> [!note]- Hint 3
> Topological equivalence follows from Lipschitz comparison: if $C_1 \rho \leq d \leq C_2 \rho$, balls in one metric are sandwiched by balls in the other. State this as a ball-containment.

> [!note]- Hint 4
> In infinite dimensions: take $v_n = (1, 1, \dots, 1, 0, 0, \dots)$ with the first $n$ entries equal to $1$. Compute $\|v_n\|_1, \|v_n\|_2, \|v_n\|_\infty$. Notice $\|v_n\|_1 = n$ but $\|v_n\|_\infty = 1$ — no Lipschitz bound is possible.

---

# Solution

All three metrics are translation-invariant: $d_p(x, y) = \|x - y\|_p$. So the inequalities reduce to a single chain on the norms of an arbitrary $v \in \mathbb{R}^n$.

**Step 1: The norm chain $\|v\|_\infty \leq \|v\|_2 \leq \|v\|_1 \leq n \|v\|_\infty$.**

Each inequality is one line.

> [!note]- Derivation
> *$\|v\|_\infty \leq \|v\|_2$.* Let $j$ be an index achieving the maximum: $|v_j| = \|v\|_\infty$. Then
> $$\|v\|_\infty^2 = v_j^2 \leq \sum_{i=1}^n v_i^2 = \|v\|_2^2,$$
> so $\|v\|_\infty \leq \|v\|_2$.
>
> *$\|v\|_2 \leq \|v\|_1$.* Square both sides — we want $\sum v_i^2 \leq (\sum |v_i|)^2$:
> $$\left(\sum_{i} |v_i|\right)^2 = \sum_{i} v_i^2 + 2 \sum_{i < j} |v_i| |v_j| \geq \sum_i v_i^2,$$
> since the cross terms are nonnegative. So $\|v\|_2^2 \leq \|v\|_1^2$, hence $\|v\|_2 \leq \|v\|_1$.
>
> *$\|v\|_1 \leq n \|v\|_\infty$.* Each $|v_i| \leq \|v\|_\infty$, so $\sum_{i=1}^n |v_i| \leq \sum_{i=1}^n \|v\|_\infty = n \|v\|_\infty$.
>
> Combining:
> $$\|v\|_\infty \leq \|v\|_2 \leq \|v\|_1 \leq n \|v\|_\infty.$$
>
> One can also sharpen the middle inequality via **Cauchy–Schwarz**: $\sum |v_i| \cdot 1 \leq \sqrt{\sum v_i^2} \cdot \sqrt{n} = \sqrt{n} \|v\|_2$, giving $\|v\|_1 \leq \sqrt{n} \|v\|_2$. This is tighter (factor $\sqrt n$ rather than $n$) but the cruder $\|v\|_1 \leq n \|v\|_\infty$ is what we need for the comparison with $d_\infty$ — and it follows from the chain alone.

**Step 2: Topological equivalence.**

The Lipschitz comparison forces ball containment in both directions, hence topological equivalence.

> [!note]- Derivation
> The chain $\|v\|_\infty \leq \|v\|_2 \leq \|v\|_1 \leq n \|v\|_\infty$ gives, for every $v$ and every choice of two indices $p, q \in \{1, 2, \infty\}$, a constant $C_{pq} > 0$ with $\|v\|_p \leq C_{pq} \|v\|_q$. Specifically, $C_{\infty,1} = 1$, $C_{1,\infty} = n$, etc.
>
> Consequently, the $d_p$-ball $B^{d_p}_r(x) = \{y : \|y - x\|_p < r\}$ satisfies
> $$B^{d_p}_{r / C_{pq}}(x) \subseteq B^{d_q}_r(x).$$
> (Proof: if $\|y - x\|_p < r/C_{pq}$, then $\|y - x\|_q \leq C_{pq} \|y - x\|_p < r$.)
>
> So every $d_q$-ball about $x$ contains a $d_p$-ball about $x$ of positive radius, and vice versa. By [[Def - Equivalent Metrics|the definition of topological equivalence]], $d_p$ and $d_q$ generate the same topology on $\mathbb{R}^n$.

**Step 3: Why the analogous statement fails in infinite dimensions.**

The constant $n$ in $\|v\|_1 \leq n \|v\|_\infty$ is *finite* in finite dimensions. In infinite dimensions — say, the space $\ell^\infty$ of bounded sequences with the sup norm — the same inequality $\|v\|_1 \leq n \|v\|_\infty$ would require $n \to \infty$ as a constant, which is no constant at all. Concretely:

Take $v^{(n)} = (1, 1, \dots, 1, 0, 0, \dots) \in \ell^\infty$ with the first $n$ entries equal to $1$. Then $\|v^{(n)}\|_\infty = 1$ for every $n$, but $\|v^{(n)}\|_1 = n \to \infty$. So no constant $C$ satisfies $\|v\|_1 \leq C \|v\|_\infty$ on $\ell^\infty$: the ratio is unbounded.

> [!note]- Derivation
> The spaces $\ell^p$ are defined as
> $$\ell^p = \left\{(v_i)_{i=1}^\infty : \sum_i |v_i|^p < \infty\right\} \ (1 \leq p < \infty), \qquad \ell^\infty = \{(v_i) : \sup_i |v_i| < \infty\}.$$
>
> In finite dimensions $\mathbb{R}^n$, the spaces $\ell^p$ all coincide as sets (every finite sequence is summable for every $p$), and the comparison constants $C_{pq}$ are finite. In infinite dimensions, $\ell^p$ depends on $p$:
> - $\ell^1 \subsetneq \ell^2 \subsetneq \ell^\infty$ — for example, $v_i = 1/i \in \ell^2 \setminus \ell^1$ since $\sum 1/i^2 < \infty$ but $\sum 1/i = \infty$. So the spaces are not even the same set.
> - Even on their intersection (sequences in $\ell^1$, which lie in every $\ell^p$), no Lipschitz comparison holds: the example $v^{(n)}$ above gives $\|v^{(n)}\|_1 = n$ and $\|v^{(n)}\|_\infty = 1$, so $\|v\|_1 / \|v\|_\infty$ is unbounded.
>
> This means the $\ell^1$ and $\ell^\infty$ norms on (say) $c_{00}$ (the space of eventually-zero sequences, which is dense in all the $\ell^p$ spaces) generate *different* topologies. Convergence in $\ell^\infty$ means uniform convergence of the entries; convergence in $\ell^1$ means absolute convergence with bounded total mass. The two notions are incomparable.

> [!note]- Complete formal solution
> **(1)** The three norm inequalities — sup $\leq$ Euclidean (sup of squares lower-bounded by single square), Euclidean $\leq$ $\ell^1$ (square of sum has nonneg cross terms), $\ell^1 \leq n \cdot$ sup (each entry at most max) — translate to the metric chain. **(2)** A Lipschitz comparison $\|v\|_p \leq C_{pq} \|v\|_q$ gives ball containment $B^{d_p}_{r/C_{pq}}(x) \subseteq B^{d_q}_r(x)$ in both directions, so the topologies generated coincide. **(3)** The Lipschitz constants depend on $n$; in $\ell^\infty$ the sequence $v^{(n)} = (1, \dots, 1, 0, \dots)$ has $\|v^{(n)}\|_1 = n \to \infty$ but $\|v^{(n)}\|_\infty = 1$, so no constant works and the topologies genuinely differ. $\blacksquare$

---

# Key Takeaways

**On *finite-dimensional* normed spaces, all norms are equivalent — this is one of the cornerstone facts of finite-dimensional analysis, and the explicit constants in the $\ell^1$–$\ell^2$–$\ell^\infty$ comparison are the cleanest illustration.** The general theorem says: for any two norms $\|\cdot\|_a, \|\cdot\|_b$ on a finite-dimensional vector space $V$, there exist constants $C_1, C_2 > 0$ with $C_1 \|v\|_a \leq \|v\|_b \leq C_2 \|v\|_a$. The standard proof goes through compactness: the unit sphere $\{v : \|v\|_a = 1\}$ is compact (closed and bounded in $\mathbb{R}^n$, which we get by picking a basis), and $\|v\|_b$ is continuous on it, so attains a strictly positive minimum and finite maximum. The lesson to internalize: in finite dimensions, no choice of norm has any *topological* consequence — convergence, continuity, openness, compactness are all norm-independent. The choice of norm matters only for *quantitative* questions (best constants in inequalities, computational complexity, geometry of unit balls).

**The Lipschitz comparison $C_1 \rho \leq d \leq C_2 \rho$ is the strongest form of metric equivalence and implies topological equivalence via direct ball containment.** This is the operational reflex: when comparing two metrics, look first for global Lipschitz constants. If they exist, no further argument is needed — the topologies coincide. The three increasingly fine layers of equivalence to keep distinct are: *Lipschitz equivalent* (constants both ways), $\Rightarrow$ *uniformly equivalent* (same Cauchy sequences), $\Rightarrow$ *topologically equivalent* (same opens, see [[Def - Equivalent Metrics]]). Each implication is strict in general but they all coincide for the finite-dimensional examples here. In infinite dimensions, even uniformly equivalent norms can fail to be Lipschitz equivalent (rare, but possible), and topologically equivalent norms can fail to be uniformly equivalent (every locally convex topology on a Banach space that is not Banach-norm-comparable).

**The geometric picture of the unit balls explains the inequalities visually.** The unit ball of $\ell^1$ in $\mathbb{R}^2$ is a diamond (square rotated $45^\circ$); the unit ball of $\ell^2$ is a circle; the unit ball of $\ell^\infty$ is a square. The chain $\|v\|_\infty \leq \|v\|_2 \leq \|v\|_1$ corresponds to the geometric chain *diamond $\subseteq$ circle $\subseteq$ square* (unit balls; a smaller norm corresponds to a *larger* unit ball, since the ball is $\{\|v\| < 1\}$). In $n$ dimensions, the $\ell^1$-ball is the cross-polytope, the $\ell^2$-ball is the round $n$-ball, the $\ell^\infty$-ball is the cube. The cube's volume is $2^n$ while the round ball's volume goes to $0$ super-exponentially, giving an enormous *volume ratio* that grows with $n$ — a hint of why the Lipschitz constants blow up in the limit $n \to \infty$ and why infinite-dimensional Banach space geometry is qualitatively different.

**The transition from finite to infinite dimensions is where most of the *real* content of functional analysis lives.** In $\mathbb{R}^n$ everything is equivalent to everything; in $\ell^p$ spaces the inequalities $\ell^1 \subsetneq \ell^2 \subsetneq \ell^\infty$ become *strict inclusions*, the unit ball ceases to be compact, weak and strong convergence diverge, and the choice of norm controls every analytical question. The trigger to develop: *whenever an inequality has a constant depending on $n$ that grows unboundedly, the inequality has no infinite-dimensional analogue and the topologies diverge*. The same phenomenon explains why every finite-dimensional Banach space is reflexive (every continuous linear functional on the dual is evaluation at some point) and is the source of all the non-reflexive examples ($\ell^1$ has a much larger dual than $\ell^1$). For the polymath, the gateway concept to keep is: $\ell^p$ spaces are the *smallest* infinite-dimensional Banach spaces, and their non-equivalence is the very first thing the theory has to say.
