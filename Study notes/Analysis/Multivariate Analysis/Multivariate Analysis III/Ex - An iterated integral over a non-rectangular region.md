---
type: exercise
subject: multivariate-analysis
difficulty: "⭐"
prereqs:
  - "Thm - Fubini's Theorem"
  - "Def - The Riemann Integral in Several Variables"
  - "Def - Jordan Measure"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $T$ be the closed triangle in $\mathbb{R}^2$ with vertices $(0,0)$, $(1,0)$, and $(1,1)$. Evaluate
$$\iint_T xy \, dA.$$

**Recall:**

![[Thm - Fubini's Theorem#Statement]]

For a region **between two graphs**, $\Omega = \{(x,y) : x \in \Sigma,\ g_0(x) \leq y \leq g_1(x)\}$ with $\Sigma$ a [[Def - Jordan Measure|Jordan measurable]] base and $g_0 \leq g_1$ continuous, [[Thm - Fubini's Theorem|Fubini's theorem]] gives
$$\int_\Omega f \, dA = \int_\Sigma \left( \int_{g_0(x)}^{g_1(x)} f(x,y)\,dy \right) dx.$$
The integrand $f(x,y) = xy$ is continuous, the triangle is bounded by line segments (graphs of affine functions, hence content zero), so $T$ is Jordan measurable and the iterated reduction applies.

---

# Convergent Strategy

**Problem class.** This is a *direct-evaluation* problem: compute a multiple integral over a non-box region. The [[Multivariate Analysis III — Integration in Several Variables#Problem-Solving Strategy|topic strategy]] prescribes reduction to one dimension via [[Thm - Fubini's Theorem|Fubini]], with the work concentrated in correctly reading off the inner limits.

**Assumption pattern.** The triangle is a region between two graphs. The recognizable feature: for each fixed $x \in [0,1]$, the cross-section $\{y : (x,y) \in T\}$ is an interval — and the endpoints of that interval are the two edges of the triangle, read as functions of $x$.

**Theorem routing.** Describe $T$ as $\{0 \leq x \leq 1,\ 0 \leq y \leq x\}$: the lower edge is $y = 0$, the slanted edge from $(0,0)$ to $(1,1)$ is $y = x$, and these are the inner limits. Fubini turns the double integral into $\int_0^1\int_0^x xy\,dy\,dx$, two nested one-variable integrals, each evaluated by the fundamental theorem of calculus.

**Key decision point.** The one place to be careful is identifying the inner limits as *functions of $x$*. The slanted edge is the line $y = x$, not a constant; writing the inner limit as a constant (a common error) would integrate over a rectangle instead of the triangle. Sketching the region and, for a typical fixed $x$, marking where the vertical slice enters and exits $T$ is the reliable procedure.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis III — Integration in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Reduce a multiple integral to iterated single integrals (Fubini).** The double integral over $T$ becomes $\int_0^1\int_0^x xy\,dy\,dx$.

2. **Describe a region between graphs.** The triangle is rewritten as $\{0\leq x\leq 1,\ 0\leq y\leq x\}$, identifying the inner limits with its edges.

---

# Hints

> [!note]- Hint 1
> Sketch the triangle. For a fixed value of $x$ between $0$ and $1$, draw the vertical line at that $x$. Where does it enter the triangle, and where does it leave? Those two heights are your inner limits of integration.

> [!note]- Hint 2
> The bottom edge is the segment from $(0,0)$ to $(1,0)$ — the line $y = 0$. The slanted edge runs from $(0,0)$ to $(1,1)$ — the line $y = x$. So for fixed $x$, the slice runs from $y = 0$ up to $y = x$.

> [!note]- Hint 3
> The iterated integral is $\int_0^1 \left( \int_0^x xy\,dy \right) dx$. Do the inner integral first, treating $x$ as a constant; then integrate the result over $x$.

---

# Solution

The triangle is the region $0 \leq y \leq x$ over $0 \leq x \leq 1$. Fubini turns the double integral into a nested pair of one-variable integrals, which the fundamental theorem of calculus evaluates.

**Step 1: Describe the triangle as a region between graphs.**

$T = \{(x,y) : 0 \leq x \leq 1,\ 0 \leq y \leq x\}$.

> [!note]- Derivation
> The triangle has vertices $(0,0), (1,0), (1,1)$. Its three edges are: the bottom edge from $(0,0)$ to $(1,0)$, lying on the line $y = 0$; the right edge from $(1,0)$ to $(1,1)$, lying on $x = 1$; the slanted edge from $(0,0)$ to $(1,1)$, lying on the line $y = x$. The interior of the triangle is the set of points below the slant and above the bottom — that is, $0 < y < x$ — with $x$ ranging over $(0,1)$. Taking the closure,
> $$T = \{(x,y) : 0 \leq x \leq 1,\ 0 \leq y \leq x\}.$$
> This exhibits $T$ as a region between the graphs $g_0(x) = 0$ and $g_1(x) = x$ over the base $\Sigma = [0,1]$. Both $g_0, g_1$ are continuous (indeed affine), and the base $[0,1]$ is Jordan measurable, so $T$ is Jordan measurable and Fubini's region-between-graphs form applies. The integrand $xy$ is continuous, so $\iint_T xy\,dA$ is defined.

**Step 2: Apply Fubini and do the inner integral.**

$\displaystyle \iint_T xy\,dA = \int_0^1\int_0^x xy\,dy\,dx$, and the inner integral is $\int_0^x xy\,dy = \tfrac{x^3}{2}$.

> [!note]- Derivation
> By [[Thm - Fubini's Theorem|Fubini's theorem]] for a region between graphs,
> $$\iint_T xy\,dA = \int_0^1 \left( \int_{0}^{x} xy\,dy \right) dx.$$
> Compute the inner integral, holding $x$ fixed (so $x$ is a constant for the $y$-integration):
> $$\int_0^x xy\,dy = x \int_0^x y\,dy = x \cdot \left[ \frac{y^2}{2} \right]_{y=0}^{y=x} = x \cdot \frac{x^2}{2} = \frac{x^3}{2}.$$

**Step 3: Do the outer integral.**

$\displaystyle \int_0^1 \frac{x^3}{2}\,dx = \frac{1}{8}$.

> [!note]- Derivation
> $$\int_0^1 \frac{x^3}{2}\,dx = \frac{1}{2}\int_0^1 x^3\,dx = \frac{1}{2}\left[ \frac{x^4}{4} \right]_0^1 = \frac{1}{2}\cdot\frac{1}{4} = \frac{1}{8}.$$
> Hence $\iint_T xy\,dA = \dfrac{1}{8}$. $\blacksquare$
>
> *Cross-check by the other order.* Fubini permits integrating $x$ first. Describing $T$ from the $y$-standpoint: for fixed $y \in [0,1]$, the horizontal slice runs from the slant $x = y$ to the right edge $x = 1$, so $T = \{0\leq y\leq 1,\ y\leq x\leq 1\}$. Then
> $$\iint_T xy\,dA = \int_0^1\int_y^1 xy\,dx\,dy = \int_0^1 y\cdot\frac{1-y^2}{2}\,dy = \frac12\int_0^1(y - y^3)\,dy = \frac12\left(\frac12 - \frac14\right) = \frac18.$$
> The two orders agree, as Fubini guarantees.

> [!note]- Complete formal solution
> The triangle with vertices $(0,0),(1,0),(1,1)$ is $T = \{0\leq x\leq 1,\ 0\leq y\leq x\}$, a region between the continuous graphs $y = 0$ and $y = x$ over $[0,1]$; it is Jordan measurable and $xy$ is continuous, so [[Thm - Fubini's Theorem|Fubini's theorem]] applies:
> $$\iint_T xy\,dA = \int_0^1\int_0^x xy\,dy\,dx = \int_0^1 x\cdot\frac{x^2}{2}\,dx = \int_0^1\frac{x^3}{2}\,dx = \frac{1}{8}. \qquad \blacksquare$$

---

# Key Takeaways

**A multiple integral over a non-box region is evaluated by reading the region as "between two graphs" and letting the edges become the inner limits.** The entire technique is: pick an outer variable, and for each fixed value of it determine the interval the cross-section sweeps; the two endpoints of that interval, expressed as functions of the outer variable, are the inner limits. For the triangle the cross-section at fixed $x$ runs from the bottom edge $y=0$ to the slant $y=x$. The trigger is any double (or higher) integral over a region described by a sketch or by inequalities: do not look for a clever substitution first, just describe the region as a stack of slices. This generalizes immediately — a region between two curves, a solid between two surfaces, an $n$-dimensional region — and it is the workhorse for every concrete multiple integral.

**The inner limits are functions of the outer variable, not constants — that is the whole difference from a rectangle.** The single most common error is to write the slanted edge as a constant limit, which silently integrates over the bounding rectangle instead of the triangle. The discipline that prevents it: after writing the iterated integral, check that the inner limits genuinely depend on the outer variable whenever the region is non-rectangular, and confirm by sketching one representative slice. A region is rectangular if and only if both inner limits are constant; any other region has at least one variable inner limit, and that variation is exactly how the integral "knows" the region is not a box.

**Either order works, and checking both is a free correctness test.** Fubini guarantees $\int\int f\,dy\,dx = \int\int f\,dx\,dy$ for an integrable $f$, so re-deriving the answer with the variables swapped — which forces you to re-describe the region from the other axis's standpoint — is an independent verification that costs only a second computation. When the two orders disagree, either the region was described wrongly in one of them or the integrability hypothesis fails. For genuinely hard integrals this same freedom becomes a *strategy* rather than a check: when the inner integral has no elementary antiderivative in one order, the other order may be elementary, as in [[Ex - Reversing the order of integration]].
