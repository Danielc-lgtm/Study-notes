---
type: definition
subject: multivariate-analysis
prereqs:
  - "Def - The Riemann Integral in Several Variables"
tags: [analysis, multivariate-analysis]
---

# Notation

A **cell** (box) in $\mathbb{R}^n$ is a product of closed bounded intervals $R = I_1 \times \cdots \times I_n$, and its **volume** is $V(R) = \ell(I_1) \cdots \ell(I_n)$, where $\ell(I)$ is the length of the interval $I$. A **partition** $P$ of a cell $R$ is the collection of subcells obtained by partitioning each interval factor. For a set $S$, $\chi_S$ denotes the indicator function ($1$ on $S$, $0$ off it); $\partial S$ the topological boundary; $\mathring S$ the interior; $\overline S$ the closure. We write $\overline{I}(\,\cdot\,)$ and $\underline{I}(\,\cdot\,)$ for the upper and lower [[Def - The Riemann Integral in Several Variables|Riemann integrals]]. The full symbol registry is on [[Multivariate Analysis III — Integration in Several Variables]].

---

# Axiom Motivation

We want to assign to a bounded subset $S \subseteq \mathbb{R}^n$ a number — its measure, its "$n$-dimensional volume" — that agrees with intuition: a box should get the product of its side lengths, a disk should get $\pi r^2$, and the measure of two disjoint pieces should be the sum of their measures. The problem is that "intuition" stops giving answers the moment $S$ is not a box. What is the volume of a disk? Of a triangle? Of the set of rational points in a square? We need a *procedure* that produces a number, and the procedure should reduce to the obvious answer when $S$ happens to be a box.

The natural idea is to *approximate*. Any bounded set can be covered from outside by finitely many cells; the total volume of such a cover is an overestimate of the set's volume, and the best overestimate — the infimum over all finite cell covers — is a candidate measure. Symmetrically, any set with non-empty interior contains finitely many disjoint cells; the total volume of such an interior packing is an underestimate, and the supremum over all packings is another candidate. Call these the **upper content** $\operatorname{cont}^+(S)$ and the **lower content** $\operatorname{cont}^-(S)$. For a box they coincide and equal the product of side lengths, which is the consistency check we demanded.

The decisive design choice is the word *finite*. We allow only finitely many cells in a cover or a packing. Why is this the right desideratum, and not "countably many"? Because the entire construction is tethered to the [[Def - The Riemann Integral in Several Variables|Riemann integral]]: a finite cover of $S$ by cells is precisely a partition of an enclosing box into cells, some of which meet $S$, and the total volume of the meeting cells is an upper Darboux sum of $\chi_S$. So $\operatorname{cont}^+(S)$ is *literally* the upper integral $\overline{I}(\chi_S)$, and $\operatorname{cont}^-(S)$ is the lower integral $\underline{I}(\chi_S)$. Jordan measurability of $S$ — the agreement of the two contents — is then exactly Riemann integrability of $\chi_S$. This is not a coincidence to be discovered later; it is the reason the definition is built from finite covers. Jordan measure is the measure theory that the Riemann integral *is*: a set is integrable as a domain precisely when its indicator is integrable as a function.

What breaks if we *weaken* the finiteness and allow countable covers? We get a strictly better-behaved notion — **Lebesgue outer measure** — but we leave the Riemann theory behind. The two genuinely differ. The set of rational points in $[0,1]^n$ can be covered by countably many cells of arbitrarily small total volume (enumerate the points, put a tiny cell around the $k$th one of volume $\varepsilon 2^{-k}$), so its Lebesgue outer measure is $0$. But no *finite* family of small cells can cover all the rationals, because the rationals are dense — any finite cover of them must cover the whole cube, forcing upper content $1$. So with finite covers this set is not Jordan measurable at all, while with countable covers it is negligible. The finiteness restriction is exactly what makes Jordan measure only *finitely additive* and not *countably additive*; that single missing axiom is the gap that motivates the entire subject of measure theory.

What breaks if we *strengthen* — say, demand a measure for *every* bounded set? Then no finitely-additive, translation-invariant, normalized notion exists with the properties we want (already in dimension $n \geq 3$ this is the Banach–Tarski obstruction; even in low dimensions, demanding countable additivity for all sets is impossible). So we must accept that *some sets are not measurable*, and the honest definition simply names the class on which the construction succeeds. Jordan measure does not pretend to measure everything; it measures exactly the sets whose two contents agree, and the clean characterization — boundary has content zero — tells you which sets those are.

---

# The Definition

Fix a cell $R \subseteq \mathbb{R}^n$, and let $S \subseteq R$ be a bounded set.

**Upper and lower content.** The **upper Jordan content** and **lower Jordan content** of $S$ are
$$\operatorname{cont}^+(S) = \overline{I}(\chi_S) = \inf\Big\{ \sum_{k=1}^{N} V(R_k) \ : \ S \subseteq R_1 \cup \cdots \cup R_N,\ R_k \text{ cells} \Big\},$$
$$\operatorname{cont}^-(S) = \underline{I}(\chi_S) = \sup\Big\{ \sum_{k=1}^{N} V(R_k) \ : \ R_1 \cup \cdots \cup R_N \subseteq S,\ R_k \text{ disjoint cells} \Big\}.$$
Always $\operatorname{cont}^-(S) \leq \operatorname{cont}^+(S)$.

**Jordan measurability.** The set $S$ is **Jordan measurable** (Taylor: *contented*) if
$$\operatorname{cont}^+(S) = \operatorname{cont}^-(S),$$
equivalently if $\chi_S$ is [[Def - The Riemann Integral in Several Variables|Riemann integrable]]. The common value is the **Jordan measure** (or **Jordan content**, or **volume**) of $S$:
$$V(S) = \operatorname{cont}^+(S) = \operatorname{cont}^-(S) = \int_R \chi_S \, dV.$$

**Nil set.** A set $\Sigma$ with $\operatorname{cont}^+(\Sigma) = 0$ is said to have **content zero**, or to be a **nil set** (a **Jordan-null set**). Such a set is automatically Jordan measurable with $V(\Sigma) = 0$.

**The boundary characterization.** A bounded set $S$ is Jordan measurable if and only if its topological boundary has content zero:
$$S \text{ is Jordan measurable} \quad \Longleftrightarrow \quad \operatorname{cont}^+(\partial S) = 0.$$
This follows from the identity $\operatorname{cont}^+(S) = \operatorname{cont}^+(\partial S) + \operatorname{cont}^-(\mathring S)$: the two contents of $S$ differ by exactly $\operatorname{cont}^+(\partial S)$.

**Finite additivity.** The Jordan-measurable subsets of $R$ form an *algebra of sets*: $R$ is measurable, complements of measurable sets are measurable, and finite unions of measurable sets are measurable (hence so are finite intersections). On this algebra $V$ is **finitely additive**: if $S_1, S_2$ are Jordan measurable and disjoint (more generally if $\operatorname{cont}^+(S_1 \cap S_2) = 0$), then $V(S_1 \cup S_2) = V(S_1) + V(S_2)$.

---

# Relate to Other Fields / Compression

Jordan measure is the **finitely-additive precursor of [[Def - Lebesgue Measure|Lebesgue measure]]**. The two are built by the identical recipe — cover the set by cells, infimize total volume — and differ in exactly one clause: Jordan content allows only *finite* covers, Lebesgue outer measure allows *countable* ones. That single change is everything. Allowing countable covers turns the finitely-additive $V$ into the countably-additive Lebesgue measure, the defining property of a [[Def - Measure and Measure Space|measure]] in the sense of [[Measure Theory I — §1 Measure Spaces|measure theory]]. Jordan measure is thus what you get if you try to do measure theory with only the tools the Riemann integral provides, and its limitations are precisely the limitations of the Riemann integral. The class of Jordan-measurable sets is strictly smaller than the class of Lebesgue-measurable sets, and where both apply they agree: a Jordan-measurable set has Lebesgue measure equal to its Jordan measure. The exact bridge between the two theories is the boundary characterization combined with one fact: $S$ is **Jordan measurable if and only if $\partial S$ is a [[Def - Null Set and Completion|Lebesgue-null set]]** — Jordan measurability is a measure-theoretic smallness condition imposed on the boundary.

Algebraically, the structure is also illuminating. The Jordan-measurable sets form an **algebra of sets** but not a **$\sigma$-algebra**: closed under finite unions but not countable ones. The collection of Lebesgue-measurable sets *is* a $\sigma$-algebra, and the prefix "$\sigma$" (for countable) is the precise marker of the difference. So "Jordan measure : Lebesgue measure" is the same relationship as "algebra of sets : $\sigma$-algebra" — the upgrade in both cases is from finite to countable operations.

---

# Examples / Corollaries

**Is an instance — a cell.** A cell $R = I_1 \times \cdots \times I_n$ is Jordan measurable with $V(R) = \ell(I_1) \cdots \ell(I_n)$. The single cell $R$ is both a finite cover of itself and a finite packing of itself, so the contents are pinched to the product of side lengths. This is the consistency check: Jordan measure assigns boxes the answer we already knew.

**Is an instance — the closed unit disk.** The disk $D = \{(x,y) : x^2 + y^2 \leq 1\}$ is Jordan measurable, with $V(D) = \pi$. Its boundary is the unit circle, which is the union of the two graphs $y = \pm\sqrt{1-x^2}$ over $[-1,1]$; the graph of a continuous function over a closed bounded base has content zero, so $\partial D$ is nil, and the boundary characterization gives Jordan measurability. See [[Ex - A Jordan-measurable region]]. The same argument makes any disk, ball, triangle, polygon, or region between finitely many continuous graphs Jordan measurable — these are exactly the "ordinary-looking regions" one wants to integrate over.

**Is an instance — any finite set.** A single point has content zero (cover it by one cell of volume $\varepsilon$), and a finite union of content-zero sets has content zero, so every finite subset of $\mathbb{R}^n$ is a nil set, Jordan measurable with measure $0$.

**Is NOT an instance — the rationals in a cube.** The set $S = \mathbb{Q}^n \cap [0,1]^n$ is bounded but not Jordan measurable. Because $S$ is dense in $[0,1]^n$, any finite cover of $S$ by cells must cover the whole cube — so $\operatorname{cont}^+(S) = 1$. Because $S$ has empty interior, no cell fits inside it — so $\operatorname{cont}^-(S) = 0$. The two contents disagree; equivalently $\chi_S$ (the Dirichlet function) is not Riemann integrable. See [[Ex - A bounded set that is not Jordan measurable]]. This is the canonical witness that Jordan measurability is a genuine restriction — and the same set *is* Lebesgue measurable (with measure $0$), which is the canonical witness that Lebesgue measure is strictly more powerful.

**Is NOT an instance — a "fat Cantor set" boundary.** A subtler non-example: there exist closed sets $S \subseteq [0,1]$ that are nowhere dense yet have positive Lebesgue measure (fat Cantor sets). Such a set has $\partial S = S$ with positive outer measure, so it is not Jordan measurable. This shows the boundary characterization has teeth even for closed sets — being closed and "thin-looking" is not enough; the boundary must genuinely be nil.

**Corollary — countable additivity fails.** Each rational point in $[0,1]^n$ is a nil set, so $S = \mathbb{Q}^n \cap [0,1]^n$ is a *countable* union of Jordan-measurable sets of measure $0$. If Jordan measure were countably additive, $S$ would have measure $0$; instead $S$ is not measurable at all. This is the precise failure that countable additivity, and hence measure theory, is built to repair.

**Calibration check.** Verify that the upper content of $\{1/k : k \in \mathbb{N}\} \cup \{0\}$ in $[0,1]$ is $0$ (this set is closed and "spread out" but countable and bounded — cover the first finitely many points by tiny cells and the tail by one small cell near $0$); that $V$ of the triangle with vertices $(0,0), (1,0), (0,1)$ is $\tfrac12$ via the boundary characterization; and that if $S$ is Jordan measurable so is its complement within an enclosing cell, with $V(R \setminus S) = V(R) - V(S)$. If you can also explain why the rationals fail while the sequence $\{1/k\}$ succeeds — density versus a single limit point — you have understood what content-zero detects.

---

# Unlocked by This

> [!tip] Integration over general regions *(from this topic)*
> Jordan measurability is exactly the hypothesis that makes $\int_S f$ well-defined for a non-box region $S$: extending $f$ by zero produces a function whose discontinuities sit on $\partial S$, and that set being nil is what the [[Thm - The Lebesgue Criterion for Riemann Integrability|Lebesgue criterion]] needs. Without Jordan measurability there is no integral over $S$.

> [!tip] Lebesgue Measure *(from Measure Theory)*
> Replacing "finite cover" by "countable cover" in the definition of upper content yields the [[Def - Lebesgue Measure|Lebesgue outer measure]], and the resulting set function is countably additive — a genuine [[Def - Measure and Measure Space|measure]]. Jordan measure is the prototype whose single defect, the failure of countable additivity, the Lebesgue theory exists to fix. See [[Measure Theory I — §1 Measure Spaces]].
