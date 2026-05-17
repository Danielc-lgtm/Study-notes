---
type: definition
subject: multivariate-analysis
prereqs: []
tags: [analysis, multivariate-analysis]
---

# Notation

A **cell** in $\mathbb{R}^n$ is a product $R = I_1 \times \cdots \times I_n$ of closed bounded intervals $I_\nu = [a_\nu, b_\nu]$; its **volume** is $V(R) = \ell(I_1) \cdots \ell(I_n)$, where $\ell(I)$ is the length of $I$. A **partition** $P$ of $R$ is obtained by partitioning each interval factor $I_\nu$ into subintervals and forming all product subcells $R_\alpha$. Write $\operatorname{maxsize}(P) = \max_\alpha \operatorname{diam}(R_\alpha)$ for the **mesh**. A function $f : R \to \mathbb{R}$ is **bounded** if $\sup_R |f| < \infty$. The full symbol registry is on [[Multivariate Analysis III — Integration in Several Variables]].

---

# Axiom Motivation

In one variable, the Riemann integral of a function on $[a,b]$ is built by cutting the interval into small subintervals, estimating the function from above and below on each, summing, and squeezing the two estimates together. We want the same construction in $\mathbb{R}^n$, and at first glance there is nothing to invent — just do it. But two questions have to be answered before the definition is even well-posed, and they are the entire content of the definition.

The first question is: *what do you cut up?* In one variable the domain is an interval, and you cut intervals into subintervals — there is no choice. In $\mathbb{R}^n$ the natural domain is a **cell**, a product of intervals, and a partition of a cell is built by partitioning each interval factor separately and taking the product subcells. This is a deliberate choice: a cell can be cut into subcells, each of which is again a cell with an obvious volume $\ell(I_1) \cdots \ell(I_n)$. You do *not* try to partition a disk into subdisks — that has no good notion of refinement. The integral is defined on cells first, and only afterward extended to general regions by the trick described below. The desideratum the cell structure satisfies is *refinability*: any two partitions of a cell have a common refinement, which is what makes the upper and lower estimates monotone and lets the squeeze work.

The second question is: *what does it mean for the squeeze to succeed?* On each subcell $R_\alpha$ of a partition, the most $f$ contributes is $(\sup_{R_\alpha} f) V(R_\alpha)$ and the least is $(\inf_{R_\alpha} f) V(R_\alpha)$. Summing gives an **upper Darboux sum** $\overline{I}_P(f)$ and a **lower Darboux sum** $\underline{I}_P(f)$, with $\underline{I}_P(f) \leq \overline{I}_P(f)$ always. Refining a partition can only lower the upper sum and raise the lower sum, so the upper sums decrease toward a limiting **upper integral** $\overline{I}(f)$ and the lower sums increase toward a **lower integral** $\underline{I}(f)$, with $\underline{I}(f) \leq \overline{I}(f)$. We *declare* $f$ integrable when these meet. Why is this the right desideratum, rather than "the limit of Riemann sums exists"? Because the Darboux formulation makes integrability a *checkable* condition — the gap $\overline{I}_P(f) - \underline{I}_P(f)$ is a single non-negative number to drive to zero — and the multidimensional Darboux theorem shows it is equivalent to the Riemann-sum formulation anyway. The upper-equals-lower definition is the one you can prove things about; the Riemann-sum picture is the one that explains what the integral *means*.

What breaks if we *weaken* boundedness — allow $f$ to be unbounded? Then $\sup_{R_\alpha} f$ can be $+\infty$ on a subcell no matter how fine the partition, the upper sum is $+\infty$, and the squeeze never starts. Unbounded functions require a separate "improper" treatment (a limiting process trapping the function from below), and the basic Riemann integral is reserved for *bounded* $f$. What breaks if we *strengthen* — demand continuity? Then the integral always exists, but we have thrown away every interesting discontinuous function: indicators of regions, piecewise-defined functions, anything with a jump. The point of the upper-equals-lower definition is precisely to admit a controlled class of discontinuous functions, and the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]] identifies exactly which: those whose discontinuity set is negligible.

The final design question is how to integrate over a region that is *not* a cell — a disk, a ball, a triangle. The answer is the **extension-by-zero trick**: place the region $S$ inside a cell $R$, redefine $f$ to be $0$ outside $S$, and integrate the extended function over $R$. This is the only mechanism by which $\int_S f$ has any meaning, and it forces a hypothesis on $S$: the extended function jumps along $\partial S$, so it is integrable only if $\partial S$ is small — that is, only if $S$ is [[Def - Jordan Measure|Jordan measurable]]. The integral over a region and the measure of a region are, from the start, the same theory.

---

# The Definition

Let $R \subseteq \mathbb{R}^n$ be a cell and $f : R \to \mathbb{R}$ a bounded function.

**Darboux sums.** For a partition $P = \{R_\alpha\}$ of $R$, define the **upper** and **lower Darboux sums**
$$\overline{I}_P(f) = \sum_\alpha \Big( \sup_{R_\alpha} f \Big)\, V(R_\alpha), \qquad \underline{I}_P(f) = \sum_\alpha \Big( \inf_{R_\alpha} f \Big)\, V(R_\alpha).$$
If $P$ refines $Q$ then $\overline{I}_P(f) \leq \overline{I}_Q(f)$ and $\underline{I}_P(f) \geq \underline{I}_Q(f)$; and for *any* two partitions $P_1, P_2$, taking a common refinement gives $\underline{I}_{P_1}(f) \leq \overline{I}_{P_2}(f)$.

**Upper and lower integral.** The **upper integral** and **lower integral** of $f$ over $R$ are
$$\overline{I}(f) = \inf_{P} \overline{I}_P(f), \qquad \underline{I}(f) = \sup_{P} \underline{I}_P(f),$$
the infimum and supremum taken over all partitions $P$ of $R$. Always $\underline{I}(f) \leq \overline{I}(f)$.

**Riemann integrability.** The function $f$ is **Riemann integrable** on $R$, written $f \in \mathcal{R}(R)$, if
$$\underline{I}(f) = \overline{I}(f),$$
and the common value is the **Riemann integral**
$$\int_R f \, dV = \int_R f(x)\, dV(x) = \overline{I}(f) = \underline{I}(f).$$
(When $n = 2$ one often writes $dA$; for general $n$, simply $dx$.)

**The Darboux theorem (Riemann-sum formulation).** If $f \in \mathcal{R}(R)$ and $(P_\nu)$ is any sequence of partitions with $\operatorname{maxsize}(P_\nu) \to 0$, and $\xi_{\nu\alpha}$ is any choice of one point in each subcell $R_{\nu\alpha}$, then
$$\int_R f \, dV = \lim_{\nu \to \infty} \sum_\alpha f(\xi_{\nu\alpha})\, V(R_{\nu\alpha}).$$
The sums on the right are **Riemann sums**.

**Basic properties.** The integral is **linear** ($\int_R (c_1 f_1 + c_2 f_2) = c_1 \int_R f_1 + c_2 \int_R f_2$ for $f_1, f_2 \in \mathcal{R}(R)$), **monotone** ($f \leq g \Rightarrow \int_R f \leq \int_R g$), and **multiplicative-stable** ($f, g \in \mathcal{R}(R) \Rightarrow fg \in \mathcal{R}(R)$).

**Integral over a region.** Let $S \subseteq \mathbb{R}^n$ be a [[Def - Jordan Measure|Jordan measurable]] set contained in a cell $R$, and let $f \in \mathcal{R}(R)$. Since $\chi_S$ is Riemann integrable (that *is* Jordan measurability) and products of integrable functions are integrable, $\chi_S f \in \mathcal{R}(R)$, and one defines
$$\int_S f \, dV = \int_R \chi_S(x)\, f(x)\, dV(x).$$
This is independent of the enclosing cell $R$.

---

# Relate to Other Fields / Compression

The multivariate Riemann integral is the one-variable Riemann integral with "interval" replaced by "cell" and "subinterval" by "subcell" — the Darboux machinery is verbatim. What is genuinely new is not the integral but the *integrability question*: in one variable almost every function one writes down is integrable, while in $\mathbb{R}^n$ the indicator of a region is integrable only when the region is well-behaved, so integrability becomes a real subject.

The integral is the analogue of the **[[Measure Theory II — §2 Integration|Lebesgue integral]]** obtained by insisting on finite partitions of the domain. The Lebesgue integral partitions the *range* instead of the domain — it sums values weighted by the [[Def - Lebesgue Measure|Lebesgue measure]] of the level sets — and this re-grouping is what gives it countable additivity and the powerful limit theorems (monotone and dominated convergence) the Riemann integral lacks. Where both are defined they agree: a Riemann integrable function is Lebesgue integrable with the same integral. The [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]] is the precise statement of how much smaller the Riemann theory is — it handles exactly the bounded functions whose discontinuity set is [[Def - Null Set and Completion|Lebesgue-null]].

There is also a compression worth recording: the Riemann integral, the [[Def - Jordan Measure|Jordan measure]] of a set, and the Jordan content are *one object*. The measure of $S$ is the integral of $\chi_S$; the upper content is the upper integral of $\chi_S$; integrability of $\chi_S$ is Jordan measurability of $S$. "Integrate a function" and "measure a set" are not two theories but one, viewed through a function or through a set.

---

# Examples / Corollaries

**Is an instance — every continuous function on a cell.** If $f : R \to \mathbb{R}$ is continuous, then $f \in \mathcal{R}(R)$. On a compact cell $f$ is uniformly continuous, so for a fine enough partition $f$ varies by less than $\varepsilon$ on each subcell, making $\overline{I}_P(f) - \underline{I}_P(f) \leq \varepsilon \, V(R)$; the gap closes. This is the basic supply of integrable functions.

**Is an instance — the indicator of a Jordan measurable set.** For $S \subseteq R$ [[Def - Jordan Measure|Jordan measurable]], $\chi_S \in \mathcal{R}(R)$ with $\int_R \chi_S = V(S)$. This is the definitional link: Jordan measurability of $S$ *is* Riemann integrability of $\chi_S$. A function discontinuous along a circle (such as the indicator of a disk) is integrable, because the circle is a nil set.

**Is an instance — a bounded function with a nil discontinuity set.** If $f : R \to \mathbb{R}$ is bounded and its set of discontinuities has content zero, then $f \in \mathcal{R}(R)$. This generalizes the previous two and is the working version of the integrability criterion; the sharp form, allowing the discontinuity set merely to have outer measure zero, is the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]].

**Is NOT an instance — the Dirichlet function.** Let $f = \chi_{\mathbb{Q}^n}$ on $R = [0,1]^n$, equal to $1$ at rational points and $0$ elsewhere. On every subcell of every partition, $\sup f = 1$ and $\inf f = 0$ (rationals and irrationals are both dense), so $\overline{I}_P(f) = V(R) = 1$ and $\underline{I}_P(f) = 0$ for every $P$. Thus $\overline{I}(f) = 1 \neq 0 = \underline{I}(f)$, and $f$ is not Riemann integrable — its discontinuity set is all of $[0,1]^n$. See [[Ex - A bounded set that is not Jordan measurable]].

**Is NOT an instance — an unbounded function.** The function $f(x) = |x|^{-1/2}$ on the punctured unit ball is not Riemann integrable in the basic sense, because it is unbounded: no matter how fine the partition, the subcell containing the singularity has $\sup f = \infty$, so every upper Darboux sum is $\infty$. Such functions require the separate improper-integral construction (trapping $f$ from below by its truncations $f_A = \min(f, A)$ and passing $A \to \infty$).

**Corollary — linearity and monotonicity as calibration.** From the definition: $\int_R (f + g) = \int_R f + \int_R g$ for integrable $f, g$; if $0 \leq f \leq M$ on $R$ then $0 \leq \int_R f \leq M \, V(R)$; and if $f = 0$ except on a nil set then $\int_R f = 0$. The last fact — integrals ignore content-zero sets — is the seed of the slogan that the integral does not see negligible sets.

**Calibration check.** Verify that a function which is $1$ at one point of $[0,1]^n$ and $0$ elsewhere is integrable with integral $0$ (its single discontinuity is a nil set); that $\overline{I}(f) + \underline{I}(-f) = 0$ for any bounded $f$; and that for the Dirichlet function the upper and lower integrals are $1$ and $0$ regardless of the partition. If you can also explain why boundedness is needed for the upper sum to be finite, you have understood every clause of the definition.

---

# Unlocked by This

> [!tip] Fubini's Theorem and the Change of Variables Formula *(from this topic)*
> Once the integral is defined, the two computational theorems become available: [[Thm - Fubini's Theorem]] reduces an $n$-dimensional integral to iterated one-dimensional ones, and [[Thm - The Change of Variables Formula]] transports an integral by a diffeomorphism with the Jacobian factor. Both are stated and proved in terms of this definition.

> [!tip] The Lebesgue Integral *(from Measure Theory)*
> Partitioning the *range* rather than the domain, and weighting by [[Def - Lebesgue Measure|Lebesgue measure]], produces the **Lebesgue integral** of [[Measure Theory II — §2 Integration]] — a strict extension of this integral that interchanges freely with limits. The Riemann integral is the Lebesgue integral's finitely-additive shadow.
