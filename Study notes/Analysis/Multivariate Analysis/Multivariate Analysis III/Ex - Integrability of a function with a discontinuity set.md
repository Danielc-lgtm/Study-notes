---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Lebesgue Criterion for Riemann Integrability"
  - "Def - The Riemann Integral in Several Variables"
  - "Def - Jordan Measure"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Work on the cell $R = [0,1]^2$.

1. Let $f : R \to \mathbb{R}$ be the function equal to $1$ on the closed unit-quarter disk $D = \{x^2 + y^2 \leq 1\} \cap R$ and equal to $0$ elsewhere on $R$. Show that $f$ is Riemann integrable.
2. Let $g : R \to \mathbb{R}$ be the Dirichlet function: $g(x,y) = 1$ if both coordinates are rational, $g(x,y) = 0$ otherwise. Show that $g$ is **not** Riemann integrable.
3. Let $h : R \to \mathbb{R}$ be defined by $h(x,y) = 1$ if $x \in \{1/k : k \in \mathbb{N}\}$ and $h(x,y) = 0$ otherwise. Decide whether $h$ is Riemann integrable, and explain which feature of its discontinuity set settles it.

In each case the method is the same: locate the discontinuity set and measure it.

**Recall:**

![[Thm - The Lebesgue Criterion for Riemann Integrability#Notation]]

![[Thm - The Lebesgue Criterion for Riemann Integrability#Statement]]

The [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]]: a bounded $f : R \to \mathbb{R}$ is [[Def - The Riemann Integral in Several Variables|Riemann integrable]] **if and only if** its set of discontinuities $\operatorname{Disc}(f)$ has Lebesgue outer measure zero — coverable by countably many cells of arbitrarily small total volume. The discontinuity set of an indicator $\chi_S$ is exactly the boundary $\partial S$. A graph of a continuous function over a closed bounded base has content zero, hence outer measure zero. A countable set has outer measure zero. A *dense* set in a cell has the whole cell as its closure.

---

# Convergent Strategy

**Problem class.** This is a *decide-integrability* problem, the canonical use of the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]]. The [[Multivariate Analysis III — Integration in Several Variables#Problem-Solving Strategy|topic strategy]] is explicit: never estimate Darboux sums; instead identify the discontinuity set and decide whether it is Lebesgue-null.

**Assumption pattern.** Each of the three functions is built so that its discontinuity set is geometrically transparent. For $f$, the indicator of a region, the discontinuities sit on the boundary curve. For $g$, the Dirichlet function, the discontinuities are *everywhere*. For $h$, the discontinuities lie on countably many vertical lines. The three illustrate the three regimes — a null curve, a non-null everywhere-set, and a null countable family of lines.

**Theorem routing.** For $f$: $\operatorname{Disc}(f) = \partial D$ is an arc of the unit circle plus segments of the axes — a finite union of continuous graphs, content zero, so outer measure zero; the criterion gives integrability. For $g$: $\operatorname{Disc}(g) = R$ entirely, which has outer measure $1$; the criterion gives non-integrability. For $h$: $\operatorname{Disc}(h)$ is the union of the vertical segments $\{1/k\} \times [0,1]$, a countable union of nil sets, hence outer measure zero; the criterion gives integrability.

**Key decision point.** The instructive contrast is $g$ versus $h$. Both have discontinuity sets that are, in a loose sense, "spread out", yet $g$ fails and $h$ succeeds. The decisive distinction is that $\operatorname{Disc}(g)$ is *dense* (closure = whole cell, outer measure $1$) while $\operatorname{Disc}(h)$, though infinite, is a *countable* union of measure-zero lines and therefore itself measure zero. This is precisely where content zero would be too crude — the countable union of lines is not nil, but it is null — and the criterion, stated with outer measure, sees the difference.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis III — Integration in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Certify integrability by measuring the discontinuity set.** For each function, identify $\operatorname{Disc}(f)$ and apply the Lebesgue criterion.

2. **Show a set is nil by covering it with continuous graphs.** The boundary arc for $f$ and each vertical line for $h$ are graphs of continuous functions, hence content zero.

3. **Use countable subadditivity of outer measure.** For $h$, the discontinuity set is a countable union of measure-zero lines, hence measure zero — a step content zero could not perform.

---

# Hints

> [!note]- Hint 1
> For all three parts, do *not* compute Darboux sums. State the Lebesgue criterion and then, for each function, answer one question: where is the function discontinuous?

> [!note]- Hint 2
> An indicator $\chi_S$ is discontinuous exactly on $\partial S$ — at interior points it is locally constant $1$, at exterior points locally constant $0$, and only at boundary points does it jump. For $f$, what is the boundary of the quarter-disk?

> [!note]- Hint 3
> For $g$, recall that the rationals and the irrationals are both dense. At which points of $R$ is $g$ continuous? What is the outer measure of the set where it is discontinuous?

> [!note]- Hint 4
> For $h$, the function is discontinuous along the vertical line $x = 1/k$ for each $k$ (and also potentially the limit line $x = 0$). Each line is a measure-zero set. There are countably many of them. Is a countable union of measure-zero sets measure zero?

---

# Solution

All three are settled by the same one-line test: integrability holds exactly when the discontinuity set has outer measure zero. The work is locating that set.

**Step 1: $f$ is integrable — its discontinuity set is a content-zero curve.**

$\operatorname{Disc}(f) = \partial D$, the boundary of the quarter-disk, which is a finite union of continuous graphs and hence has outer measure zero.

> [!note]- Derivation
> The function $f = \chi_D$ is the indicator of $D = \{x^2 + y^2 \leq 1\} \cap [0,1]^2$. An indicator is continuous at every interior point of $D$ (where it is locally constant $1$) and at every point of the exterior (locally constant $0$); it is discontinuous exactly at the points of the boundary $\partial D$, where every neighborhood contains both a point of $D$ and a point outside. So $\operatorname{Disc}(f) = \partial D$.
>
> The boundary $\partial D$ within the cell $[0,1]^2$ consists of: the circular arc $\{x^2 + y^2 = 1, \ x, y \geq 0\}$, which is the graph of the continuous function $y = \sqrt{1-x^2}$ over $[0,1]$; and the two segments of the coordinate axes $\{0\} \times [0,1]$ and $[0,1] \times \{0\}$ that bound the quarter-disk, each the graph of a continuous (constant) function. Each piece is the graph of a continuous function over a closed bounded interval, hence has content zero (Taylor's Proposition 3.1.7). A finite union of content-zero sets has content zero, so $\operatorname{cont}^+(\partial D) = 0$, and content zero implies outer measure zero: $m^*(\operatorname{Disc}(f)) = 0$.
>
> By the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]], $f$ is Riemann integrable. (Its integral is the Jordan measure of the quarter-disk, $\pi/4$.)

**Step 2: $g$ is not integrable — its discontinuity set is the whole cell.**

$\operatorname{Disc}(g) = R$, which has outer measure $1 \neq 0$.

> [!note]- Derivation
> Fix any point $p = (x_0, y_0) \in R$. Every neighborhood of $p$ contains a point with both coordinates rational (where $g = 1$) and a point with an irrational coordinate (where $g = 0$), because $\mathbb{Q}^2$ and its complement are both dense in $R$. So $g$ oscillates by $1$ in every neighborhood of $p$, and $g$ is discontinuous at $p$. Since $p$ was arbitrary, $\operatorname{Disc}(g) = R = [0,1]^2$.
>
> The outer measure of the cell $R$ is its volume, $m^*(R) = 1$, which is not zero. By the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]] (the "only if" direction), $g$ is **not** Riemann integrable. Concretely, every partition has $\overline{I}_P(g) = 1$ and $\underline{I}_P(g) = 0$, so the upper and lower integrals are $1$ and $0$.

**Step 3: $h$ is integrable — its discontinuity set is a countable union of measure-zero lines.**

$\operatorname{Disc}(h)$ is contained in the union of the vertical segments $\{1/k\} \times [0,1]$ together with $\{0\} \times [0,1]$ — a countable union of measure-zero sets, hence measure zero.

> [!note]- Derivation
> The function $h$ depends only on $x$: $h(x,y) = 1$ when $x \in A := \{1/k : k \in \mathbb{N}\}$ and $h(x,y) = 0$ otherwise. Examine continuity by cases.
>
> If $x_0 \notin A$ and $x_0 \neq 0$, then $x_0$ has a neighborhood in $[0,1]$ disjoint from $A$ (the points $1/k$ accumulate only at $0$, so away from $0$ they are isolated and $A$ is closed there). On that neighborhood $h \equiv 0$, so $h$ is continuous at $(x_0, y_0)$. If $x_0 = 1/k \in A$, then every neighborhood contains points with $x \notin A$ (where $h = 0$) and the line itself (where $h = 1$), so $h$ jumps: $h$ is discontinuous along $\{1/k\} \times [0,1]$. If $x_0 = 0$, then every neighborhood of $x_0$ contains points $1/k$ (where $h = 1$) and points not in $A$ (where $h = 0$), so $h$ is discontinuous along $\{0\} \times [0,1]$ as well.
>
> Hence
> $$\operatorname{Disc}(h) \subseteq \Big( \bigcup_{k=1}^\infty \{1/k\} \times [0,1] \Big) \cup \big( \{0\} \times [0,1] \big).$$
> Each vertical segment $\{c\} \times [0,1]$ is the graph of the continuous function $x = c$ (a constant) over $[0,1]$, hence has content zero, in particular outer measure zero. This is a *countable* family of measure-zero sets. By countable subadditivity of Lebesgue outer measure — cover the $k$-th line by cells of total volume $< \varepsilon 2^{-k}$, total over all lines $< \varepsilon$ — the union has outer measure zero:
> $$m^*(\operatorname{Disc}(h)) = 0.$$
> By the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]], $h$ is Riemann integrable. (Its integral is $0$, since $h$ is nonzero only on a measure-zero set.)
>
> **The decisive feature.** Note what made $h$ succeed where $g$ failed: $\operatorname{Disc}(h)$ is a *countable* union of measure-zero lines, hence measure zero, while $\operatorname{Disc}(g)$ is *dense*, with the whole cell as closure and outer measure $1$. The set $\operatorname{Disc}(h)$ is not nil in the content-zero sense — a content-zero argument with finite covers would not reach all countably many lines — but it *is* Lebesgue-null, and the criterion, stated with outer measure, detects this. $\blacksquare$

> [!note]- Complete formal solution
> The [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]]: a bounded function is Riemann integrable iff its discontinuity set has Lebesgue outer measure zero.
>
> *Part 1.* $f = \chi_D$ has $\operatorname{Disc}(f) = \partial D$, consisting of a circular arc and two axis segments, each a graph of a continuous function over a closed interval — content zero, hence $m^*(\operatorname{Disc}(f)) = 0$. So $f$ is integrable.
>
> *Part 2.* $g$ is discontinuous at every point of $R$ (rationals and irrationals are dense), so $\operatorname{Disc}(g) = R$ with $m^*(R) = 1 \neq 0$. So $g$ is not integrable.
>
> *Part 3.* $h$ is continuous off the lines $x = 1/k$ ($k \in \mathbb{N}$) and $x = 0$, and discontinuous on them; $\operatorname{Disc}(h)$ is contained in a countable union of vertical segments, each measure zero. By countable subadditivity $m^*(\operatorname{Disc}(h)) = 0$. So $h$ is integrable. The contrast with part 2: a countable union of measure-zero lines is measure zero, whereas a dense set has positive outer measure. $\blacksquare$

---

# Key Takeaways

**Deciding integrability is always the same procedure: name the discontinuity set, measure it.** The [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]] makes integrability a two-step routine — locate $\operatorname{Disc}(f)$, then check whether it has outer measure zero — and this replaces any direct manipulation of Darboux sums. For an indicator $\chi_S$ the discontinuity set is the boundary $\partial S$; for a function depending on one coordinate it is a union of slices; for a function built from a pointwise rule it is wherever the rule is locally non-constant. The trigger "decide whether $f$ is integrable" should immediately produce the question "where is $f$ discontinuous, and how big is that set". Estimating $\overline{I}_P - \underline{I}_P$ by hand is the beginner's route and yields nothing reusable; the criterion is the professional's route.

**Outer measure, not content, is the right notion of "small" — and the countable union is where the difference shows.** The pair $g$ and $h$ is engineered to expose this. The function $h$ is discontinuous on infinitely many lines; no *finite* cover of small total volume reaches all of them, so $\operatorname{Disc}(h)$ is *not* a content-zero (nil) set in the strict finite-cover sense. Yet $h$ is integrable, because $\operatorname{Disc}(h)$ is a countable union of measure-zero lines and Lebesgue outer measure *is* countably subadditive. The criterion is correctly stated with outer measure precisely so that it can absorb countable unions. The reusable warning: when a discontinuity set is infinite, do not ask "is it nil" (a content question) — ask "is it Lebesgue-null" (an outer-measure question), and remember that a countable union of null sets is null while a finite-cover argument cannot see that.

**Density is the enemy of integrability.** The single feature that kills $g$ is that its discontinuity set is *dense* — its closure is the entire cell, forcing outer measure $1$. A dense discontinuity set can never be Lebesgue-null (a null set has empty interior in a strong sense and certainly cannot have full-measure closure), so any bounded function discontinuous on a dense set is non-integrable. This is the fast diagnostic for non-integrability: if you can show the function jumps in every neighborhood of every point — typically by a density argument playing two dense sets against each other — it is not Riemann integrable, no further work needed. Conversely, a discontinuity set that is *closed and thin*, or *countable*, or a *finite union of lower-dimensional graphs*, is null and poses no obstruction. The mental sorting is: dense bad set means non-integrable; thin or countable bad set means integrable.
