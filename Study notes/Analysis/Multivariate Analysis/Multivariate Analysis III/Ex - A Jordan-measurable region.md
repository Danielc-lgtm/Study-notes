---
type: exercise
subject: multivariate-analysis
difficulty: "⭐"
prereqs:
  - "Def - Jordan Measure"
  - "Def - The Riemann Integral in Several Variables"
  - "Thm - The Lebesgue Criterion for Riemann Integrability"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $D = \{(x,y) \in \mathbb{R}^2 : x^2 + y^2 \leq 1\}$ be the closed unit disk.

1. Show that the unit circle $C = \{(x,y) : x^2 + y^2 = 1\}$ is a **nil set** (has content zero) in $\mathbb{R}^2$.
2. Conclude that $D$ is **Jordan measurable**.

**Recall:**

The objects in play are Jordan content, Jordan measurability, and the fact that the graph of a continuous function over a closed bounded base has content zero.

![[Def - Jordan Measure#The Definition]]

A [[Def - Jordan Measure|nil set]] (content-zero set) $\Sigma$ has $\operatorname{cont}^+(\Sigma) = 0$: it can be covered by *finitely many* cells of arbitrarily small total volume. The key structural fact (Taylor's Proposition 3.1.7) is that **the graph of a continuous function over a closed bounded base is nil**: if $\Sigma \subseteq \mathbb{R}^{n-1}$ is closed and bounded and $g : \Sigma \to \mathbb{R}$ is continuous, then $\{(x, g(x)) : x \in \Sigma\}$ has content zero in $\mathbb{R}^n$. A **finite union** of nil sets is nil.

The boundary characterization of Jordan measurability: a bounded set $S$ is **Jordan measurable if and only if its boundary $\partial S$ has content zero**.

---

# Convergent Strategy

**Problem class.** This is a *certify-measurability* problem: show a concrete region is a legitimate domain of integration. As the [[Multivariate Analysis III — Integration in Several Variables#Problem-Solving Strategy|topic strategy]] records, such problems are never attacked from the definition of content — instead one identifies the *bad set* (here the boundary) and proves it is small, typically by recognizing it as a finite union of continuous graphs.

**Assumption pattern.** The boundary of the disk is the unit circle, and the circle is not itself a graph (it fails the vertical line test). But it splits into two pieces, the upper and lower semicircles, each of which *is* the graph of a continuous function over the closed interval $[-1,1]$. The recognizable feature is "boundary = finite union of graphs".

**Theorem routing.** The graph of the continuous function $g_\pm(x) = \pm\sqrt{1 - x^2}$ over $[-1,1]$ has content zero (Taylor's Proposition 3.1.7). The circle is the union of two such graphs, and a finite union of nil sets is nil, so $C$ is nil. Then the [[Def - Jordan Measure|boundary characterization]] of Jordan measurability — $S$ is Jordan measurable iff $\partial S$ is nil — gives the conclusion, since $\partial D = C$.

**Key decision point.** The one non-obvious move is the *splitting of the circle into graphs*. A circle is a single connected curve, and it is tempting to look for a single function whose graph it is — there is none. Recognizing that the obstruction (the vertical tangents at $(\pm 1, 0)$) is removed by cutting the circle into two graphs is the whole idea; everything after is routine.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis III — Integration in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Certify integrability/measurability by measuring the bad set.** The question "is $D$ Jordan measurable" is converted to "is $\partial D$ nil" via the boundary characterization.

2. **Show a set is nil by covering it with continuous graphs.** The circle $\partial D$ is exhibited as the union of two graphs of continuous functions over $[-1,1]$, each nil.

---

# Hints

> [!note]- Hint 1
> Do not try to estimate the content of the disk directly. The right object to study is the *boundary* of the disk. What theorem connects "the boundary is small" to "the region is Jordan measurable"?

> [!note]- Hint 2
> The boundary is the unit circle. The circle is not the graph of a single function $y = g(x)$ — but can you write it as a *union* of two graphs? Solve $x^2 + y^2 = 1$ for $y$.

> [!note]- Hint 3
> The upper semicircle is the graph of $g_+(x) = \sqrt{1 - x^2}$ over $x \in [-1,1]$, and $g_+$ is continuous on the closed bounded interval $[-1,1]$. Quote the fact that the graph of a continuous function over a closed bounded base is nil, and that a finite union of nil sets is nil.

---

# Solution

The disk is Jordan measurable because its boundary, the unit circle, is the union of two graphs of continuous functions — and graphs of continuous functions are nil.

**Step 1: The circle is a finite union of two continuous graphs.**

Solving $x^2 + y^2 = 1$ for $y$ gives $y = \pm\sqrt{1 - x^2}$, so $C = G_+ \cup G_-$ where $G_\pm$ is the graph of $g_\pm(x) = \pm\sqrt{1 - x^2}$ over $[-1,1]$.

> [!note]- Derivation
> A point $(x,y)$ lies on the unit circle exactly when $x^2 + y^2 = 1$, equivalently $y^2 = 1 - x^2$. For this to have a real solution $y$ we need $1 - x^2 \geq 0$, i.e. $x \in [-1, 1]$, and then $y = \sqrt{1 - x^2}$ or $y = -\sqrt{1 - x^2}$. Define
> $$g_+(x) = \sqrt{1 - x^2}, \qquad g_-(x) = -\sqrt{1 - x^2}, \qquad x \in [-1, 1].$$
> Both are continuous on the closed bounded interval $[-1,1]$: the function $x \mapsto 1 - x^2$ is a polynomial, hence continuous and non-negative on $[-1,1]$, and $t \mapsto \sqrt{t}$ is continuous on $[0,\infty)$, so the composites are continuous. The circle is the union of the two graphs:
> $$C = \{(x, g_+(x)) : x \in [-1,1]\} \cup \{(x, g_-(x)) : x \in [-1,1]\} = G_+ \cup G_-.$$
> (The two graphs meet at $(\pm 1, 0)$, but that overlap is harmless.)

**Step 2: Each graph has content zero, so the circle is nil.**

By the graph-is-nil fact, $G_+$ and $G_-$ each have content zero; a finite union of nil sets is nil, so $C$ is nil.

> [!note]- Derivation
> Taylor's Proposition 3.1.7 states that the graph of a continuous function over a closed bounded base is a nil set. Here is the mechanism for $G_+$, to make the citation self-contained. Fix $\varepsilon > 0$. Since $g_+$ is continuous on the compact interval $[-1,1]$, it is *uniformly* continuous: there is $\delta > 0$ such that $|x - x'| < \delta \Rightarrow |g_+(x) - g_+(x')| < \varepsilon$. Partition $[-1,1]$ into $N$ subintervals $J_1, \dots, J_N$ each of length $< \delta$. Over each $J_k$, the graph of $g_+$ lies inside a rectangle $J_k \times [m_k, M_k]$ where $M_k - m_k \leq \varepsilon$ (the values of $g_+$ on $J_k$ span less than $\varepsilon$). The total area of these $N$ rectangles is
> $$\sum_{k=1}^N \ell(J_k) \cdot (M_k - m_k) \leq \varepsilon \sum_{k=1}^N \ell(J_k) = \varepsilon \cdot 2.$$
> So $G_+$ is covered by finitely many cells of total area $\leq 2\varepsilon$; since $\varepsilon$ is arbitrary, $\operatorname{cont}^+(G_+) = 0$. The identical argument gives $\operatorname{cont}^+(G_-) = 0$.
>
> A finite union of nil sets is nil: cover $G_+$ by cells of total area $< \varepsilon/2$ and $G_-$ by cells of total area $< \varepsilon/2$; together they cover $C = G_+ \cup G_-$ with total area $< \varepsilon$. Hence $\operatorname{cont}^+(C) = 0$ — the unit circle is a nil set.

**Step 3: The disk is Jordan measurable.**

The boundary of $D$ is exactly $C$, which is nil; by the boundary characterization, $D$ is Jordan measurable.

> [!note]- Derivation
> The topological boundary of the closed disk $D$ is the unit circle: the interior of $D$ is the open disk $\{x^2 + y^2 < 1\}$, the exterior is $\{x^2 + y^2 > 1\}$, and $\partial D$ is what is left, $\{x^2 + y^2 = 1\} = C$. By Step 2, $\operatorname{cont}^+(\partial D) = \operatorname{cont}^+(C) = 0$.
>
> The boundary characterization in [[Def - Jordan Measure]] states that a bounded set $S$ is Jordan measurable if and only if $\operatorname{cont}^+(\partial S) = 0$. With $S = D$ and $\partial D = C$ nil, $D$ is Jordan measurable. $\blacksquare$
>
> (Its Jordan measure is $V(D) = \pi$, computable once the [[Thm - The Change of Variables Formula|change of variables formula]] is available — see [[Ex - The volume of the n-dimensional ball]] for the $n = 2$ case.)

> [!note]- Complete formal solution
> **Claim.** The closed unit disk $D = \{x^2 + y^2 \leq 1\}$ is Jordan measurable.
>
> The boundary $\partial D$ equals the unit circle $C = \{x^2 + y^2 = 1\}$. Writing $g_\pm(x) = \pm\sqrt{1-x^2}$ for $x \in [-1,1]$ — continuous functions on a closed bounded interval — the circle is the finite union $C = G_+ \cup G_-$ of their graphs.
>
> The graph of a continuous function over a closed bounded base is nil (Taylor, Proposition 3.1.7): by uniform continuity, partitioning the base into subintervals of small length confines the graph to thin rectangles of total area $\leq \varepsilon \cdot (\text{base length})$, arbitrarily small. Hence $\operatorname{cont}^+(G_+) = \operatorname{cont}^+(G_-) = 0$, and since a finite union of nil sets is nil, $\operatorname{cont}^+(C) = 0$.
>
> By the boundary characterization of Jordan measurability ([[Def - Jordan Measure]]), $\operatorname{cont}^+(\partial D) = 0$ implies $D$ is Jordan measurable. $\blacksquare$

---

# Key Takeaways

**To prove a region is a legitimate domain of integration, certify that its boundary is negligible — never estimate the content directly.** The boundary characterization converts the question "is $S$ Jordan measurable" into "is $\partial S$ nil", and this is always the productive route. Estimating $\operatorname{cont}^+(S)$ and $\operatorname{cont}^-(S)$ separately and showing they agree is far harder and yields no reusable insight. The trigger is any problem of the form "show $S$ is Jordan measurable" or, equivalently, "show $\chi_S$ is integrable" or "show $\int_S f$ is defined": immediately shift attention to $\partial S$. This is the same move that, in the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]], shifts attention from a function to its discontinuity set — integrability is always a verdict on the size of a *bad set*, and the skill is identifying which set that is.

**A boundary is small because it is built from continuous graphs, and the graph-is-nil fact is the universal certificate.** The single reusable lemma is that the graph of a continuous function over a closed bounded base has content zero — an $(n-1)$-dimensional surface is measure-theoretically invisible in $\mathbb{R}^n$. Almost every "ordinary-looking region" has a boundary assembled from finitely many such graphs: a disk's boundary is two graphs, a sphere's is two, a polygon's boundary is finitely many line segments (graphs of affine functions), the boundary of a region between two surfaces is those two surfaces. The trigger pattern is: you need a set to be nil, and you can describe it as the union of finitely many graphs. The mechanism behind the lemma — uniform continuity confines the graph to thin slabs — is worth remembering, because it is the same mechanism that proves continuous functions are integrable.

**When a curve is not a graph, cut it into graphs.** The circle fails the vertical line test, so it is not a single graph; the resolution is to split it at the points of vertical tangency into the upper and lower semicircles, each a genuine graph. This splitting move is general: any reasonable curve or surface can be cut into finitely many pieces each of which is a graph (over an appropriately chosen coordinate axis), and since finite unions of nil sets are nil, the whole curve is then nil. The same idea — chop the object at its "bad points" into pieces each of which is of a manageable type — recurs throughout integration theory, for instance in describing a region for Fubini by splitting it into pieces that are each "between two graphs".
