---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - The Riemann Integral in Several Variables"
  - "Def - Jordan Measure"
  - "Thm - The Lebesgue Criterion for Riemann Integrability"
tags: [analysis, multivariate-analysis]
---

# Notation

$A \subseteq \mathbb{R}^m$ and $B \subseteq \mathbb{R}^n$ are [[Def - The Riemann Integral in Several Variables|cells]], with product cell $A \times B \subseteq \mathbb{R}^{m+n}$. For a function $f$ on $A \times B$ and a fixed $x \in A$, the **slice** is $f_x : B \to \mathbb{R}$, $f_x(y) = f(x,y)$. We write $\overline{I}$ and $\underline{I}$ for upper and lower [[Def - The Riemann Integral in Several Variables|Riemann integrals]]; $\int$ for the integral when it exists. A region of the form $\Omega = \{(x,y) : x \in \Sigma,\ g_0(x) \leq y \leq g_1(x)\}$, with $\Sigma$ a [[Def - Jordan Measure|Jordan measurable]] base and $g_0 \leq g_1$ continuous, is called a region **between two graphs**. The full symbol registry is on [[Multivariate Analysis III — Integration in Several Variables]].

---

# Statement

> **Fubini's Theorem (Riemann integrable case).** Let $A \subseteq \mathbb{R}^m$ and $B \subseteq \mathbb{R}^n$ be cells and $f$ a Riemann integrable function on the product cell $A \times B$. Then the multiple integral equals the iterated integrals, in either order:
> $$\int_{A \times B} f\,dV = \int_A \left( \int_B f(x,y)\,dy \right) dx = \int_B \left( \int_A f(x,y)\,dx \right) dy.$$
> (Precisely: the lower and upper integrals of the slice $f_x$ define integrable functions of $x$, and their integral over $A$ equals $\int_{A\times B} f$; when each slice $f_x$ is itself integrable — automatic if $f$ is continuous — the inner integral $\int_B f(x,y)\,dy$ is well-defined and the displayed identity holds verbatim.)
>
> **Region between two graphs.** Let $\Sigma \subseteq \mathbb{R}^{n-1}$ be a closed, bounded, [[Def - Jordan Measure|Jordan measurable]] set, let $g_0 \leq g_1$ be continuous on $\Sigma$, and set $\Omega = \{(x,y) : x \in \Sigma,\ g_0(x) \leq y \leq g_1(x)\}$. Then $\Omega$ is Jordan measurable, and for $f$ continuous on $\Omega$,
> $$\int_\Omega f\,dV = \int_\Sigma \left( \int_{g_0(x)}^{g_1(x)} f(x,y)\,dy \right) dV(x).$$

---

# Motivation

The [[Def - The Riemann Integral in Several Variables|multidimensional Riemann integral]] is defined as a limit of sums over an $n$-dimensional grid. As a definition this is fine; as a *computational procedure* it is hopeless. There is no algorithm for an $n$-fold limit of sums, and even for the area under a paraboloid you cannot evaluate $\int_R f$ from the definition. Something has to convert the genuinely $n$-dimensional object into pieces you can actually integrate — and the only integration you can actually do is one-variable integration, where you have antiderivatives and the fundamental theorem of calculus.

Fubini's theorem is that conversion. It says the integral over a box $A \times B$ can be computed by **integrating one variable at a time**: hold $x$ fixed, integrate over $y$, and you get a function of $x$; then integrate that over $x$. The $n$-dimensional integral becomes $n$ nested one-dimensional integrals — the **iterated integral** — and one-dimensional integrals are exactly what calculus can compute. This is the entire reason multiple integrals are tractable.

But the theorem has to do more than handle boxes, because the regions one actually integrates over — disks, triangles, the region under a surface and above another — are not boxes. The version that matters in practice handles a region **between two graphs**: $\Omega = \{g_0(x) \leq y \leq g_1(x)\}$ sitting over a base $\Sigma$. For such a region the iterated integral has the inner limits depending on the outer variable: $\int_\Sigma \int_{g_0(x)}^{g_1(x)} f(x,y)\, dy\, dx$. This is the form you use for every concrete multiple integral in a calculus course, and it works because the region, though not a box, is *sliceable*: for each fixed $x$ the cross-section is an interval.

There is one more thing the theorem buys, and it is the source of a famous trick. Since you may integrate in either order, you can *choose* the order — and sometimes one order is elementary while the other is impossible. The integral $\int_0^1\int_x^1 e^{y^2}\,dy\,dx$ has no elementary inner antiderivative in $y$; reverse the order and it becomes trivial. Fubini does not just make multiple integrals computable, it gives you two routes and lets you pick the one that works.

The hypothesis, though, is not optional. Fubini requires the function to be *integrable on the product* — and when it is not, the two iterated integrals can both exist and disagree. This is not a pathology to be filed away; it is the precise content of what "integrable" is buying, and recognizing the hypothesis is half of using the theorem correctly.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f$ is integrable on the product $A \times B$" (or the region $\Omega$). The skill is recognizing this from hypotheses that do not mention products.

The first disguised source is **$f$ is continuous on the region**. The property $B$ is "$f$ is continuous on the closed bounded region $\Omega$". The bridge: a continuous function on a cell is integrable, and if $\Omega$ is a region between continuous graphs over a [[Def - Jordan Measure|Jordan measurable]] base, then $\Omega$ is itself Jordan measurable (its boundary is a finite union of graphs, hence nil), so the extension of $f$ by zero has a nil discontinuity set and is integrable by the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]]. The non-obvious part is that the *geometry of the region* — bounded by graphs — is what certifies integrability. *Example problem:* integrate $xy$ over a triangle; the triangle is between two lines, $xy$ is continuous, Fubini applies.

The second disguised source is **$f$ is bounded with a discontinuity set of measure zero**. The property $B$ is "$f$ is bounded and $\operatorname{Disc}(f)$ is Lebesgue-null". The bridge is the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]] directly. The non-obviousness: Fubini is usually quoted for continuous functions, but it holds for the much larger class of Riemann integrable ones, so a function with jumps along a curve still admits the iterated reduction. *Example problem:* integrate a piecewise-defined function whose pieces are continuous and meet along a smooth curve.

The third disguised source is **$f$ is absolutely integrable on an unbounded domain**. The property $B$ is "$\int_{\mathbb{R}^{m+n}} |f| < \infty$". The bridge: the improper integral over $\mathbb{R}^{m+n}$ is a limit of integrals over expanding boxes, and absolute integrability is exactly what makes the limit and the iteration commute. The non-obviousness is that an integral over *all of space* still unwinds into iterated integrals — this is the form used for the Gaussian. *Example problem:* $\int_{\mathbb{R}^2} e^{-x^2-y^2}\,dA = (\int_{\mathbb{R}} e^{-x^2}dx)^2$ — see [[Ex - The Gaussian integral via polar coordinates]].

**Targets (Output Amplification)**

The conclusion is "$\int_{A\times B} f = \int_A(\int_B f\,dy)\,dx = \int_B(\int_A f\,dx)\,dy$".

Combine the conclusion with **a known antiderivative in one variable**. Once the integral is iterated, the inner integral is a one-variable problem, and if the integrand has an elementary antiderivative the fundamental theorem of calculus evaluates it. The further result $E$: a closed-form value for the multiple integral. This is non-obvious only in that it relocates all the difficulty into one-variable calculus, where the entire toolkit (substitution, parts, partial fractions) is available.

Combine the conclusion with **the freedom to choose the order of integration**. Fubini gives *both* iterated integrals, equal. If one order is intractable, the other may be elementary. The further result $E$: evaluation of integrals that have no elementary inner antiderivative in the given order — the order-reversal technique. This is non-obvious because the *value* is order-independent while the *difficulty* is wildly order-dependent. See [[Ex - Reversing the order of integration]].

Combine the conclusion with **a slicing recursion**. Applying Fubini to peel off one variable at a time, and recognizing that each slice is a lower-dimensional copy of the same kind of region, sets up a recursion. The further result $E$: dimension-by-dimension formulas, such as the volume of the $n$-ball expressed through the volume of the $(n-1)$-ball or $(n-2)$-ball. This is non-obvious because Fubini, a statement about one reduction, becomes through iteration a statement about an infinite family. See [[Ex - The volume of the n-dimensional ball]].

Combine the conclusion with **a product integrand**. If $f(x,y) = u(x)\,v(y)$ factors, the iterated integral separates: $\int_{A\times B} u(x)v(y) = (\int_A u)(\int_B v)$. The further result $E$: a multiple integral collapses to a *product of one-dimensional integrals*. This is non-obvious in reverse — it is the basis for *recognizing* that a multiple integral with a product integrand is secretly a product of independent one-dimensional problems, the structural fact behind independence in probability and behind the Gaussian computation.

---

# Why Is It True

The cleanest picture is the one Fubini's theorem is usually drawn with: an integral computes a volume, and you can compute a volume by **slicing**. Imagine the solid region under the graph of a non-negative $f$ over a box $A \times B$. Slice the solid by the family of hyperplanes "$x = \text{const}$". Each slice is a lower-dimensional solid, and its $(n-1)$-dimensional volume is exactly $\int_B f(x,y)\,dy$ — the area of the cross-section at that value of $x$. Now reassemble: the total volume is the integral of the cross-sectional areas as $x$ sweeps through $A$, that is $\int_A(\int_B f\,dy)\,dx$. This is Cavalieri's principle, and Fubini is its rigorous form. The two orders of iteration are just slicing the same solid two different ways — by $x = \text{const}$ planes or by $y = \text{const}$ planes — and they give the same volume because it is the *same solid*.

Why should the slicing be *legitimate* — why is the volume really the integral of the cross-sections? Here is the mechanism. Take a partition of the box $A \times B$ into subcells; it is the product of a partition $\{A_i\}$ of $A$ and a partition $\{B_j\}$ of $B$, so the subcells are $A_i \times B_j$. The Riemann sum is a double sum $\sum_{i,j} f(\xi_{ij}) V(A_i) V(B_j)$. Group the terms by $i$ first: $\sum_i V(A_i) \big[\sum_j f(\xi_{ij}) V(B_j)\big]$. The bracket is a Riemann sum for the slice integral $\int_B f(x,y)\,dy$ at $x \approx$ a point of $A_i$, and the outer sum is then a Riemann sum for $\int_A$ of that slice integral. So the iterated integral is literally the double Riemann sum *with the summation order chosen* — and a finite sum can always be reordered. The whole theorem is the statement that this reordering survives the limit.

And that is exactly where the integrability hypothesis enters. Reordering a *finite* sum is free. Reordering a *limit* of sums is not — it is an interchange of two limiting operations, and interchanges of limits require a hypothesis. Integrability of $f$ on the product is precisely the hypothesis that the double limit exists as a genuine limit, so that the order in which you take it does not matter. When $f$ is not integrable on the product, the double sum has no honest limit; the two iterated integrals are then two different *partial* ways of summing a non-convergent array, and just as a conditionally convergent series can be rearranged to any value, the two iterations can disagree. One should expect Fubini to be true because volume is slicing-independent, and one should expect it to *need* a hypothesis because it is, underneath, the reordering of a double limit.

---

# What Makes This Hard

The conceptual content — volume equals integral of cross-sections — is easy; the difficulty is entirely in the **role of the hypothesis** and in **describing a non-box region as a region between graphs**. The non-obvious point is that integrability on the product is not a formality: without it the two iterated integrals can both exist and be unequal, so the theorem is *false* without its hypothesis, and the standard error is to iterate mechanically without checking that $f$ is integrable (or, in the improper case, absolutely integrable). The second genuine difficulty is practical rather than logical: setting up the iterated integral for a region like a triangle or a disk requires correctly reading off the inner limits as functions of the outer variable, and the most common mistake is getting these limits wrong — describing the region from the wrong variable's standpoint, or swapping the order without re-deriving the limits.

---

# Rederivation Scaffold

**High-level strategy:**
A partition of the product box is a product of partitions of the factors, so the Riemann sum for $\int_{A\times B} f$ is a double sum. Group the double sum by one index, recognize the inner group as a Riemann sum for a slice integral and the outer as a Riemann sum for the iterated integral, and use integrability to pass to the limit. For a region between graphs, reduce to the box case by extending $f$ by zero.

**Subgoal decomposition:**

1. **Box case, set up the double sum.** Take a partition $P$ of $A \times B$; show it is $\{A_i \times B_j\}$ for partitions $\{A_i\}$ of $A$, $\{B_j\}$ of $B$, and write the upper/lower Darboux sums as double sums.
   - *Hint:* A partition of a product cell partitions each factor separately — this is the definition of a partition of a cell.
   - *Why needed:* It is the double sum whose two summation orders become the two iterated integrals.

2. **Box case, control the slice integrals.** For fixed $x$, define $\underline L f(x) = \underline I(f_x)$ and $\overline U f(x) = \overline I(f_x)$ (lower and upper integrals of the slice). Trap: $\underline I_P(f) \leq \underline I_A(\underline L f) \leq \overline I_A(\overline U f) \leq \overline I_P(f)$.
   - *Hint:* For each cell $A_i$, the slice sums on $B$ are squeezed between the lower and upper integrals of $f_x$; sum over $i$.
   - *Why needed:* Integrability of $f$ pinches the outer terms together, forcing $\underline L f$ and $\overline U f$ to be integrable with the common value $\int_{A\times B} f$.

3. **Box case, conclude.** Since $\underline I_P(f)$ and $\overline I_P(f)$ both converge to $\int_{A\times B} f$, the trapped quantities $\int_A \underline L f$ and $\int_A \overline U f$ equal it. If $f_x$ is integrable for each $x$ (automatic when $f$ is continuous), $\underline L f = \overline U f = \int_B f(x,y)\,dy$, giving the iterated formula.
   - *Hint:* The slice $f_x$ of a continuous $f$ is continuous, hence integrable.
   - *Why needed:* It identifies the abstract $\underline L f$ with the concrete inner integral.

4. **Region between graphs.** For $\Omega = \{g_0(x) \leq y \leq g_1(x)\}$ over a Jordan measurable base $\Sigma$, place $\Omega$ in a box and apply the box case to $\chi_\Omega f$.
   - *Hint:* The slice of $\chi_\Omega f$ at $x$ is supported on $[g_0(x), g_1(x)]$, so $\int_B \chi_\Omega f\,dy = \int_{g_0(x)}^{g_1(x)} f(x,y)\,dy$. The boundary of $\Omega$ is a finite union of graphs, hence nil, so $\Omega$ is Jordan measurable.
   - *Why needed:* It converts the box theorem into the form used for all concrete regions.

---

# Lemma Decomposition

> [!note]- Lemma 1: A partition of a product cell is a product of partitions
> **Statement:** Every partition of $A \times B$ has the form $\{A_i \times B_j\}$ where $\{A_i\}$ is a partition of $A$ and $\{B_j\}$ a partition of $B$, and $V(A_i \times B_j) = V(A_i)\,V(B_j)$.
>
> **Hint:** A partition of a cell is built by partitioning each interval factor; group the factors into the $A$-block and the $B$-block.
>
> **Why needed:** It is what turns the Riemann sum over $A \times B$ into a *double* sum, which is the object whose two summation orders are the two iterated integrals.
>
> > [!note]- Full proof
> > By definition ([[Def - The Riemann Integral in Several Variables]]), a partition of a cell $A \times B = I_1 \times \cdots \times I_{m+n}$ is obtained by partitioning each interval factor $I_\nu$ into subintervals and taking all product subcells. Split the factors: $I_1, \dots, I_m$ are the factors of $A$, and $I_{m+1}, \dots, I_{m+n}$ those of $B$. Partitioning the first $m$ factors yields a partition $\{A_i\}$ of $A$; partitioning the last $n$ yields a partition $\{B_j\}$ of $B$; and every product subcell of $A \times B$ is $A_i \times B_j$ for some $i, j$. The volume is multiplicative on products of intervals: $V(A_i \times B_j) = \prod (\text{lengths}) = \big(\prod_{A\text{-factors}}\big)\big(\prod_{B\text{-factors}}\big) = V(A_i) V(B_j)$.
>
> [!note]- Lemma 2: The slice of a continuous function is continuous, hence integrable
> **Statement:** If $f : A \times B \to \mathbb{R}$ is continuous, then for each fixed $x \in A$ the slice $f_x : B \to \mathbb{R}$, $f_x(y) = f(x,y)$, is continuous, hence Riemann integrable on $B$.
>
> **Hint:** Continuity of $f_x$ at $y_0$ follows from continuity of $f$ at $(x, y_0)$ by restricting to the slice; integrability is then the basic fact for continuous functions on a cell.
>
> **Why needed:** It guarantees the inner integral $\int_B f(x,y)\,dy$ is actually defined for each $x$, so the iterated integral makes sense.
>
> > [!note]- Full proof
> > Fix $x \in A$ and $y_0 \in B$. Given $\varepsilon > 0$, continuity of $f$ at $(x, y_0)$ supplies $\delta > 0$ such that $|f(x', y') - f(x, y_0)| < \varepsilon$ whenever $|(x',y') - (x, y_0)| < \delta$. Restricting to $x' = x$: for $|y' - y_0| < \delta$ we have $|f_x(y') - f_x(y_0)| = |f(x,y') - f(x,y_0)| < \varepsilon$. So $f_x$ is continuous at $y_0$; as $y_0$ was arbitrary, $f_x$ is continuous on $B$. A continuous function on a compact cell is Riemann integrable (uniform continuity closes the Darboux gap), so $f_x \in \mathcal{R}(B)$.
>
> [!note]- Lemma 3: A region between continuous graphs is Jordan measurable
> **Statement:** If $\Sigma \subseteq \mathbb{R}^{n-1}$ is [[Def - Jordan Measure|Jordan measurable]] and $g_0 \leq g_1$ are continuous on $\overline{\Sigma}$, then $\Omega = \{(x,y) : x \in \Sigma,\ g_0(x) \leq y \leq g_1(x)\}$ is Jordan measurable in $\mathbb{R}^n$.
>
> **Hint:** Its boundary is contained in the two graphs of $g_0, g_1$ together with the part lying over $\partial\Sigma$; each piece is nil.
>
> **Why needed:** It is what makes the integral $\int_\Omega f$ defined at all and licenses the region-between-graphs form of the theorem.
>
> > [!note]- Full proof
> > The boundary $\partial\Omega$ is contained in three sets: the graph of $g_0$ over $\overline\Sigma$, the graph of $g_1$ over $\overline\Sigma$, and the "side" $\{(x,y) : x \in \partial\Sigma,\ g_0(x) \leq y \leq g_1(x)\}$. The first two are graphs of continuous functions over a closed bounded base, hence have content zero (Taylor, Proposition 3.1.7). The side projects onto $\partial\Sigma$, which has content zero because $\Sigma$ is Jordan measurable; a content-zero base carrying bounded fibers gives a content-zero set in one higher dimension. So $\partial\Omega$ is a finite union of content-zero sets, hence content zero, and by the boundary characterization $\Omega$ is Jordan measurable.

---

# Formal Proof

> [!note]- Complete formal proof
> **Box case.** Let $f : A \times B \to \mathbb{R}$ be bounded and Riemann integrable on the product cell, with $B = \int_{A\times B} f\,dV$ (we reuse the letter; context disambiguates). For $x \in A$ define the lower and upper slice integrals
> $$\underline L f(x) = \underline I(f_x), \qquad \overline U f(x) = \overline I(f_x), \qquad \underline L f(x) \leq \overline U f(x).$$
> We show $\underline L f$ and $\overline U f$ are integrable on $A$ with $\int_A \underline L f = \int_A \overline U f = \int_{A \times B} f$.
>
> Take a partition $P$ of $A \times B$; by Lemma 1, $P = \{A_i \times B_j\}$ for partitions $\{A_i\}$ of $A$ and $\{B_j\}$ of $B$. For the lower Darboux sum,
> $$\underline I_P(f) = \sum_{i,j} \Big(\inf_{A_i \times B_j} f\Big) V(A_i) V(B_j) = \sum_i V(A_i) \sum_j \Big(\inf_{A_i \times B_j} f\Big) V(B_j).$$
> Fix $i$ and any $x \in A_i$. Since $\inf_{A_i \times B_j} f \leq \inf_{B_j} f_x$, the inner sum is $\leq \sum_j (\inf_{B_j} f_x) V(B_j) = \underline I_{\{B_j\}}(f_x) \leq \underline I(f_x) = \underline L f(x)$. Taking the infimum over $x \in A_i$: $\sum_j (\inf_{A_i \times B_j} f) V(B_j) \leq \inf_{A_i} \underline L f$. Therefore
> $$\underline I_P(f) \leq \sum_i \Big(\inf_{A_i} \underline L f\Big) V(A_i) = \underline I_{\{A_i\}}(\underline L f) \leq \underline I_A(\underline L f).$$
> Symmetrically, $\overline I_P(f) \geq \overline I_A(\overline U f)$. Combining, and using $\underline L f \leq \overline U f$,
> $$\underline I_P(f) \leq \underline I_A(\underline L f) \leq \overline I_A(\underline L f) \leq \overline I_A(\overline U f) \leq \overline I_P(f),$$
> and likewise $\underline I_P(f) \leq \underline I_A(\overline U f) \leq \overline I_A(\overline U f) \leq \overline I_P(f)$. Now $f$ is integrable on $A \times B$, so $\sup_P \underline I_P(f) = \inf_P \overline I_P(f) = \int_{A\times B} f$. The chain of inequalities pinches every quantity between them: $\underline L f$ and $\overline U f$ are both integrable on $A$, and
> $$\int_A \underline L f\,dV = \int_A \overline U f\,dV = \int_{A \times B} f\,dV.$$
> If, in addition, the slice $f_x$ is integrable for each $x$ (Lemma 2 gives this when $f$ is continuous), then $\underline L f(x) = \overline U f(x) = \int_B f(x,y)\,dy$, and the displayed identity reads
> $$\int_{A \times B} f\,dV = \int_A \Big( \int_B f(x,y)\,dy \Big) dx.$$
> Repeating with the roles of $A$ and $B$ exchanged gives the other order, so the two iterated integrals are equal.
>
> **Region between graphs.** Let $\Sigma \subseteq \mathbb{R}^{n-1}$ be Jordan measurable, $g_0 \leq g_1$ continuous on $\overline\Sigma$, and $\Omega = \{(x,y) : x \in \Sigma,\ g_0(x) \leq y \leq g_1(x)\}$. By Lemma 3, $\Omega$ is Jordan measurable. Place $\Omega$ in a box $\Sigma' \times [A, B] \supseteq \Omega$ and let $f$ be continuous on $\Omega$; extend $\chi_\Omega f$ by zero to the box. Its discontinuity set lies in $\partial\Omega$, which is nil, so $\chi_\Omega f$ is integrable by the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]]. Apply the box case: the slice of $\chi_\Omega f$ at $x \in \Sigma$ is $f(x, \cdot)$ on $[g_0(x), g_1(x)]$ and $0$ outside, so $\int \chi_\Omega(x,y) f(x,y)\,dy = \int_{g_0(x)}^{g_1(x)} f(x,y)\,dy$, and
> $$\int_\Omega f\,dV = \int_\Sigma \Big( \int_{g_0(x)}^{g_1(x)} f(x,y)\,dy \Big) dx. \qquad \blacksquare$$

---

# Cross-Field Exercise Suggestions

**Probability — marginal distributions.** A joint density $p(x,y)$ on $\mathbb{R}^2$ describes a pair of random variables. The marginal density of $X$ alone is $p_X(x) = \int_{\mathbb{R}} p(x,y)\,dy$ — the slice integral. Fubini is the statement that $\int_{\mathbb{R}^2} p = \int_{\mathbb{R}} p_X = 1$, so a joint distribution integrates to a marginal one coordinate at a time. The application is nonobvious because "marginalizing out a variable" *is* the inner integral in Fubini, and the order-independence is the symmetry between marginalizing $X$ or $Y$ first.

**Convolution and the Fubini swap.** The convolution $(u * v)(t) = \int u(s) v(t-s)\,ds$ satisfies $\int (u*v) = (\int u)(\int v)$. The proof writes the left side as a double integral $\int\int u(s) v(t-s)\,ds\,dt$ and swaps the order, after which the $t$-integral of $v(t-s)$ is $\int v$ by translation-invariance. The application is out-of-distribution because the integrand is not a product, yet the Fubini swap plus a substitution factorizes it.

**Volume by slicing — Cavalieri.** Two solids in $\mathbb{R}^3$ with equal cross-sectional areas at every height have equal volume. This is Fubini read as $V(\text{solid}) = \int (\text{cross-sectional area})\,dh$, and it is the principle by which the volume of a cone, a sphere, or a pyramid is computed without calculus-heavy machinery. The application is nonobvious because Cavalieri's principle predates the integral and looks like a geometric axiom, but it is exactly the theorem.

**Switching sum and integral.** A series $\sum_k a_k(x)$ integrated term by term, $\int \sum_k a_k = \sum_k \int a_k$, is Fubini for the product of a measure space with the counting measure on $\mathbb{N}$: a sum is an integral against counting measure, and term-by-term integration is the order swap. The application is out-of-distribution because one variable is *discrete*, yet the hypothesis (absolute convergence of $\sum_k \int |a_k|$) is exactly Fubini's absolute-integrability condition.

---

# Bridges

- **[[Thm - The Change of Variables Formula|The Change of Variables Formula]]** — the two computational engines of the topic. Change of variables deforms a domain into a box or a product; Fubini then iterates. They are constantly used together: the proof that polar coordinates evaluate the Gaussian integral applies change of variables and then Fubini, and the proof of the change of variables formula itself uses Fubini (to compute the volume of a parallelepiped via Proposition 3.1.10).

- **[[Thm - Differentiation Under the Integral Sign|Differentiation Under the Integral Sign]]** — the same phenomenon for a derivative in place of one of the integrals. Both theorems are statements that two limiting operations commute (two integrals, or a derivative and an integral), both require a hypothesis ruling out a counterexample, and the Leibniz rule can in fact be derived from Fubini by writing the derivative as an integral of the partial derivative.

- **The Lebesgue–Tonelli theorem** — the measure-theoretic upgrade. In [[Measure Theory III — §3–4 Product Measures and Differentiation|product-measure theory]], Tonelli's theorem removes the hypothesis for *non-negative* functions (the iterated integrals always agree, possibly both $+\infty$), and Fubini's theorem keeps it as *absolute integrability* for signed functions. The Riemann Fubini here is the bounded, Jordan-measurable shadow of that theory.

- **Cavalieri's principle** — the pre-calculus ancestor: solids with equal cross-sections have equal volume. Fubini is its proof and its precise statement.

---

# Unlocked by This

> [!tip] Product Measures and Tonelli's Theorem *(from Measure Theory)*
> Fubini's theorem in the Riemann setting is the model for the construction of **product measures**: given measure spaces $(X,\mu)$ and $(Y,\nu)$, the product measure $\mu \times \nu$ is built so that the Tonelli–Fubini theorems hold. See [[Measure Theory III — §3–4 Product Measures and Differentiation]].

> [!tip] Integration of Differential Forms *(from Multivariate Analysis IV)*
> The iterated-integral reduction is how the integral of a top-degree [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem|differential form]] over a region is *computed*: a form $f\,dx_1\wedge\cdots\wedge dx_n$ is integrated by writing $\int f\,dx_1\cdots dx_n$ as an iterated integral.
