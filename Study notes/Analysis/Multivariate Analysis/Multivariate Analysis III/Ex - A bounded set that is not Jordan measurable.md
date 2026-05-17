---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Jordan Measure"
  - "Def - The Riemann Integral in Several Variables"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $S = \mathbb{Q}^n \cap [0,1]^n$ be the set of points of the unit cube all of whose coordinates are rational.

1. Show that $\operatorname{cont}^+(S) = 1$.
2. Show that $\operatorname{cont}^-(S) = 0$.
3. Conclude that $S$ is **not Jordan measurable**, and that the indicator $\chi_S$ (the Dirichlet function) is **not Riemann integrable** on $[0,1]^n$.
4. Explain why $S$ is nonetheless a *countable union of Jordan-measurable sets*, and what this says about the additivity of Jordan measure.

**Recall:**

![[Def - Jordan Measure#The Definition]]

The two quantities to compute are the **upper content** $\operatorname{cont}^+(S)$, an infimum of total cell-volume over *finite* covers of $S$, and the **lower content** $\operatorname{cont}^-(S)$, a supremum of total cell-volume over *finite* interior packings. The set $S$ is [[Def - Jordan Measure|Jordan measurable]] iff these agree, equivalently iff $\chi_S$ is [[Def - The Riemann Integral in Several Variables|Riemann integrable]]. A set is **dense** in $[0,1]^n$ if every cell of positive volume inside the cube contains a point of it; the rationals are dense, and so are the irrationals.

---

# Convergent Strategy

**Problem class.** This is a *refute-measurability* problem — exhibit a bounded set that the Jordan theory cannot handle. As the [[Multivariate Analysis III — Integration in Several Variables#Problem-Solving Strategy|topic strategy]] notes, integrability questions are decided by the size of a bad set; here the bad set is the whole cube, and the point is to *use density* to compute the two contents and watch them disagree.

**Assumption pattern.** The defining feature is that $S$ is **dense** in $[0,1]^n$ but has **empty interior**. Density forces every finite cover to be wasteful; empty interior forbids any interior packing. These two facts pull the upper and lower content to opposite extremes.

**Theorem routing.** For the upper content: any finite collection of cells covering $S$ must — because $S$ is dense — cover the closure $\overline{S} = [0,1]^n$, so the total volume is at least $V([0,1]^n) = 1$; and the single cell $[0,1]^n$ shows the infimum is exactly $1$. For the lower content: any cell of positive volume inside $[0,1]^n$ contains an irrational point, hence is not a subset of $S$, so no nonempty packing exists and $\operatorname{cont}^-(S) = 0$. The contents disagree, so $\chi_S$ fails the integrability definition $\overline{I} = \underline{I}$.

**Key decision point.** The non-obvious step is the upper-content argument: realizing that a *finite* cover of a *dense* set is forced to cover the entire closure. This is exactly where the finiteness in the definition of Jordan content bites — a *countable* cover of $S$ could be far more economical, which is precisely why $S$ *is* Lebesgue measurable (with measure $0$). The exercise is, at heart, a demonstration of the gap between finite and countable covers.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis III — Integration in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Certify (here, refute) measurability by examining content.** Compute $\operatorname{cont}^+$ and $\operatorname{cont}^-$ directly and exhibit the disagreement; equivalently, exhibit the Darboux gap of $\chi_S$.

2. **Recognize the finite-cover restriction.** The whole phenomenon is driven by the definition of Jordan content using only *finite* covers — the contrast with countable covers is the lesson.

---

# Hints

> [!note]- Hint 1
> To find $\operatorname{cont}^+(S)$, think about what a *finite* union of cells covering $S$ must look like. The set $S$ is dense in the cube — every region of positive volume contains a rational point. If finitely many cells cover all rational points of the cube, what else must they cover?

> [!note]- Hint 2
> For $\operatorname{cont}^-(S)$, ask whether any cell of positive volume can fit *inside* $S$. A cell of positive volume contains points with irrational coordinates. Are those in $S$?

> [!note]- Hint 3
> For the indicator $\chi_S$: on any subcell of any partition, what is $\sup \chi_S$ and what is $\inf \chi_S$? Use that both rationals and irrationals are dense. Compute the upper and lower Darboux sums and compare.

> [!note]- Hint 4
> For part 4: each single point $\{q\}$ with $q \in S$ is a nil set, hence Jordan measurable with measure $0$. The set $S$ is countable, so $S = \bigcup_{q} \{q\}$ is a countable union of measure-zero sets. If Jordan measure were countably additive, what would $V(S)$ have to be — and what does that contradict?

---

# Solution

The set $S$ is dense in the cube but has empty interior. Density forces every finite cover to spill over the entire cube, so $\operatorname{cont}^+(S) = 1$; empty interior forbids any interior packing, so $\operatorname{cont}^-(S) = 0$. The two disagree, so $S$ is not Jordan measurable.

**Step 1: $\operatorname{cont}^+(S) = 1$.**

Every finite cell cover of $S$ has total volume $\geq 1$, and the single cell $[0,1]^n$ achieves $1$.

> [!note]- Derivation
> Let $R_1, \dots, R_N$ be cells with $S \subseteq R_1 \cup \cdots \cup R_N$. The union $R_1 \cup \cdots \cup R_N$ is a *closed* set (a finite union of closed cells). It contains $S$, hence it contains the closure $\overline{S}$. But the rationals are dense in the cube, so $\overline{S} = \overline{\mathbb{Q}^n \cap [0,1]^n} = [0,1]^n$. Therefore
> $$[0,1]^n = \overline{S} \subseteq R_1 \cup \cdots \cup R_N.$$
> A finite union of cells covering the unit cube has total volume at least the volume of the cube: $\sum_{k=1}^N V(R_k) \geq V([0,1]^n) = 1$ (any cover of a cell by finitely many cells overestimates its volume — this is the content of $\operatorname{cont}^+([0,1]^n) = 1$). Taking the infimum over all finite covers, $\operatorname{cont}^+(S) \geq 1$. Conversely the single cell $[0,1]^n$ covers $S$ and has volume $1$, so $\operatorname{cont}^+(S) \leq 1$. Hence $\operatorname{cont}^+(S) = 1$.

**Step 2: $\operatorname{cont}^-(S) = 0$.**

No nonempty cell fits inside $S$, so the only interior packing is empty, of total volume $0$.

> [!note]- Derivation
> Suppose a cell $R$ of positive volume satisfied $R \subseteq S$. A cell of positive volume contains points with *irrational* coordinates — indeed the irrationals are dense, so every cell of positive volume contains a point $x$ with at least one irrational coordinate. Such an $x$ is not in $S = \mathbb{Q}^n \cap [0,1]^n$, contradicting $R \subseteq S$. Therefore the only cells contained in $S$ have volume $0$, and any finite interior packing of $S$ has total volume $0$. Taking the supremum, $\operatorname{cont}^-(S) = 0$.

**Step 3: $S$ is not Jordan measurable; $\chi_S$ is not Riemann integrable.**

Since $\operatorname{cont}^+(S) = 1 \neq 0 = \operatorname{cont}^-(S)$, the set $S$ fails the definition of Jordan measurability, and $\chi_S$ fails the definition of Riemann integrability.

> [!note]- Derivation
> Jordan measurability of $S$ is, by definition, the equality $\operatorname{cont}^+(S) = \operatorname{cont}^-(S)$. Steps 1 and 2 give $\operatorname{cont}^+(S) = 1$ and $\operatorname{cont}^-(S) = 0$; the two are unequal, so $S$ is **not Jordan measurable**.
>
> Equivalently, work directly with the indicator $\chi_S$ — the **Dirichlet function** — and its Darboux sums on $R = [0,1]^n$. Take any partition $P = \{R_\alpha\}$. Each subcell $R_\alpha$ has positive volume, hence contains both a rational point (where $\chi_S = 1$) and a point with an irrational coordinate (where $\chi_S = 0$). So on every subcell $\sup_{R_\alpha} \chi_S = 1$ and $\inf_{R_\alpha} \chi_S = 0$, giving
> $$\overline{I}_P(\chi_S) = \sum_\alpha 1 \cdot V(R_\alpha) = V(R) = 1, \qquad \underline{I}_P(\chi_S) = \sum_\alpha 0 \cdot V(R_\alpha) = 0,$$
> for *every* partition $P$. Therefore the upper integral is $\overline{I}(\chi_S) = 1$ and the lower integral is $\underline{I}(\chi_S) = 0$. Since $\overline{I}(\chi_S) \neq \underline{I}(\chi_S)$, the function $\chi_S$ is **not Riemann integrable**. (This is the same fact as the non-measurability of $S$: $\operatorname{cont}^\pm(S)$ are by definition $\overline{I}(\chi_S)$ and $\underline{I}(\chi_S)$.)

**Step 4: $S$ is a countable union of measure-zero Jordan-measurable sets — so Jordan measure is not countably additive.**

> [!note]- Derivation
> The set $S$ is *countable*: $\mathbb{Q}^n$ is countable (a finite product of countable sets), and a subset of a countable set is countable. Enumerate $S = \{q_1, q_2, q_3, \dots\}$.
>
> Each singleton $\{q_j\}$ is a nil set: cover it by one cell of volume $\varepsilon$, so $\operatorname{cont}^+(\{q_j\}) = 0$, and a nil set is Jordan measurable with measure $V(\{q_j\}) = 0$. Thus
> $$S = \bigcup_{j=1}^\infty \{q_j\}$$
> is a *countable* union of Jordan-measurable sets, each of measure $0$.
>
> Now suppose, for contradiction, that Jordan measure were **countably additive** — that the measure of a countable disjoint union equals the sum of the measures. The singletons are pairwise disjoint, so countable additivity would force
> $$V(S) = \sum_{j=1}^\infty V(\{q_j\}) = \sum_{j=1}^\infty 0 = 0,$$
> in particular that $S$ *has* a Jordan measure. But Step 3 showed $S$ is not Jordan measurable at all. Contradiction. Hence **Jordan measure is not countably additive**: a countable union of Jordan-measurable sets need not be Jordan measurable, and even when it is, the measure of the union need not be the sum.
>
> This is the precise defect that [[Def - Lebesgue Measure|Lebesgue measure]] repairs. With *countable* covers allowed, $S$ *is* measurable: enumerate $S$ and cover $q_j$ by a cell of volume $\varepsilon 2^{-j}$, total volume $\varepsilon$, so the Lebesgue outer measure of $S$ is $0$. Lebesgue measure is countably additive by construction, and $S$ is a Lebesgue-null set. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** $S = \mathbb{Q}^n \cap [0,1]^n$ is not Jordan measurable.
>
> *Upper content.* Any finite family of cells covering $S$ has a closed union containing $\overline{S} = [0,1]^n$ (the rationals are dense), so its total volume is $\geq V([0,1]^n) = 1$; the single cell $[0,1]^n$ attains $1$. Hence $\operatorname{cont}^+(S) = 1$.
>
> *Lower content.* Every cell of positive volume contains an irrational point, so no nonempty cell lies inside $S$; the only interior packing has volume $0$, so $\operatorname{cont}^-(S) = 0$.
>
> Since $\operatorname{cont}^+(S) = 1 \neq 0 = \operatorname{cont}^-(S)$, $S$ is not Jordan measurable; equivalently, on every partition of $[0,1]^n$ the Dirichlet function $\chi_S$ has $\overline{I}_P = 1$, $\underline{I}_P = 0$, so $\chi_S \notin \mathcal{R}([0,1]^n)$.
>
> Finally $S$ is countable, hence a countable union $\bigcup_j \{q_j\}$ of nil (measure-zero, Jordan-measurable) singletons. Were Jordan measure countably additive, $S$ would have measure $\sum_j 0 = 0$ — contradicting its non-measurability. So Jordan measure is only finitely additive; Lebesgue measure, built from countable covers, makes $S$ a null set. $\blacksquare$

---

# Key Takeaways

**Density versus interior is the diagnostic for non-measurability.** The whole exercise turns on two opposing facts: $S$ is *dense* (its closure is the full cube) and $S$ has *empty interior* (no cell fits inside). Density inflates the upper content to the volume of the closure; empty interior deflates the lower content to zero. Whenever a set is simultaneously dense and interior-empty in a region, its upper and lower contents are the volumes of the closure and interior respectively, and it fails to be Jordan measurable. The trigger to suspect non-measurability is exactly this combination — a set that is "everywhere but nowhere", spread throughout a region yet containing no solid chunk. The general principle, made precise by the boundary characterization, is that non-measurability lives in a *fat boundary*: here $\partial S$ is the entire cube.

**The failure is the finiteness of the covers, and this is the birth of measure theory.** The upper content came out as $1$ for one reason only: a *finite* cover of a dense set is forced to cover the whole closure. The instant countable covers are permitted, the same set $S$ becomes economically coverable — cells of volume $\varepsilon 2^{-j}$ around the $j$-th point — and its outer measure drops to $0$. So $S$ is the canonical witness that "finite cover" and "countable cover" are genuinely different, and that the difference is not a technicality but the entire content of the upgrade from Jordan to [[Def - Lebesgue Measure|Lebesgue measure]]. The reusable lesson: when a Jordan-measure computation gives a pathological answer, ask whether countable covers would rescue it — if so, the object is Lebesgue-measurable and the pathology is an artifact of the finite-cover restriction.

**Countable additivity is exactly the axiom Jordan measure lacks.** The cleanest way to see the defect is part 4: $S$ is a countable union of measure-zero singletons, yet $S$ is not measurable. A countably additive measure would assign $S$ the value $\sum 0 = 0$; Jordan measure cannot, because it is only *finitely* additive. This is not a quirk of this one set — it is the structural reason measure theory exists. A [[Def - Measure and Measure Space|measure]] is *defined* to be countably additive, and the construction of [[Def - Lebesgue Measure|Lebesgue measure]] is precisely the project of extending the finitely-additive Jordan content to a countably-additive set function on a $\sigma$-algebra. Every time you see a countable union — of points, of sets, of events — and want the measure of the union to be the sum, you are using the axiom that distinguishes Lebesgue from Jordan, and this exercise is the demonstration that the axiom is not free.
