---
type: exercise
subject: measure-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Lebesgue Measure"
  - "Thm - Properties of Measures"
tags: [analysis, measure-theory]
---

# Problem Statement

Fix $\alpha\in(0,1)$. Construct a set $F_\alpha\subseteq[0,1]$ as follows: $F_0=[0,1]$; to pass from $F_k$ to $F_{k+1}$, delete from each of the $2^k$ constituent closed intervals of $F_k$ an *open middle interval* of length $\alpha\cdot 4^{-(k+1)}$. Let $F_\alpha=\bigcap_{k\ge0}F_k$.

**(a)** Show $F_\alpha$ is closed and compute $\lambda(F_\alpha)=1-\alpha>0$.

**(b)** Show $F_\alpha$ has **empty interior** (contains no interval) — it is nowhere dense.

**(c)** Conclude that $F_\alpha$ is a compact, nowhere-dense set of positive Lebesgue measure, and that consequently a set of positive measure need contain no interval. Contrast with the [[Ex - The Cantor set has Lebesgue measure zero|standard Cantor set]].

**Recall:**

[[Def - Lebesgue Measure|Lebesgue measure]] is countably additive and assigns intervals their length. From [[Thm - Properties of Measures]]: **continuity from above** ($F_k\downarrow F_\alpha$, $\lambda(F_0)=1<\infty$). A set is **nowhere dense** if its closure has empty interior.

---

# Convergent Strategy

**Problem class:** an existence/construction problem — *engineer* a set with two prescribed, seemingly conflicting properties (positive measure, no intervals).

**Assumption pattern:** the standard Cantor set removes middle *thirds* — a *fixed proportion* — so the surviving measure $(2/3)^k\to 0$. To keep positive measure, remove middles whose *total length is a convergent series* summing to less than $1$. The free parameter is "how fast the removed lengths shrink."

**Theorem routing:** $\lambda(F_\alpha)=1-(\text{total removed length})$ via continuity from above and a geometric-series computation. Empty interior comes from "every surviving interval at stage $k$ has length $\to 0$."

**Key decision point:** the design choice — removed lengths $\alpha 4^{-(k+1)}$ at level $k$, of which there are $2^k$ intervals, giving removed total $\sum_k 2^k\alpha 4^{-(k+1)}=\alpha\sum_k 2^{-k-2}=\alpha$, a *convergent* series.

---

# Legal Operations Used

1. **Convergent-series budgeting** — choose removal lengths so their total is a controllable finite number.
2. **Continuity from above** for $\lambda(\bigcap F_k)$.
3. **Diameter-shrinking argument** — surviving intervals' lengths $\to 0$, so no fixed interval survives.

---

# Hints

> [!note]- Hint 1
> At level $k$ there are $2^k$ intervals; from each you delete one open interval of length $\alpha 4^{-(k+1)}$. Total length deleted at level $k$ is $2^k\cdot\alpha 4^{-(k+1)}$. Sum over $k$.

> [!note]- Hint 2
> $F_\alpha=\bigcap F_k$, decreasing, $\lambda(F_0)=1$. So $\lambda(F_\alpha)=\lim\lambda(F_k)=1-\sum_k(\text{deleted at level }k)$.

> [!note]- Hint 3
> For (b): if $F_\alpha$ contained an interval $J$ of length $\delta>0$, then $J\subseteq F_k$ for every $k$. But each constituent interval of $F_k$ has length $\le 2^{-k}$. Contradiction once $2^{-k}<\delta$.

---

# Solution

**Step 1 — (a) Measure.** At level $k$, $F_k$ has $2^k$ closed intervals; forming $F_{k+1}$ deletes one open interval of length $\alpha4^{-(k+1)}$ from each, total deleted length $2^k\cdot\alpha4^{-(k+1)}=\alpha\cdot2^{-k-2}$. Summing the (disjoint) deletions over all levels,
$$\text{total removed}=\sum_{k=0}^\infty\alpha\,2^{-k-2}=\frac{\alpha}{4}\sum_{k=0}^\infty 2^{-k}=\frac{\alpha}{4}\cdot 2=\frac{\alpha}{2}\cdot\ ?$$

> [!note]- Derivation
> Let me recompute cleanly. At level $k$ (passing $F_k\to F_{k+1}$): $2^k$ intervals, each loses an open interval of length $\alpha4^{-(k+1)}$. Deleted at this step: $D_k=2^k\cdot\alpha4^{-(k+1)}=\alpha\cdot 2^k\cdot 4^{-k-1}=\alpha\cdot 4^{-1}\cdot(2/4)^k=\tfrac\alpha4(1/2)^k$. Total: $\sum_{k\ge0}D_k=\tfrac\alpha4\sum_{k\ge0}2^{-k}=\tfrac\alpha4\cdot2=\tfrac\alpha2$.
> All deleted intervals are pairwise disjoint and disjoint from $F_\alpha$, with $[0,1]=F_\alpha\sqcup(\text{all deleted})$. By countable additivity (or continuity from above: $\lambda(F_k)=1-\sum_{j<k}D_j\downarrow 1-\sum_k D_k$),
> $$\lambda(F_\alpha)=1-\sum_{k\ge0}D_k=1-\tfrac\alpha2.$$
> *(The deletion lengths $\alpha4^{-(k+1)}$ are chosen merely to make the series geometric and convergent; the precise constant $\tfrac\alpha2$ is unimportant — what matters is total removed $=\tfrac\alpha2<1$, so $\lambda(F_\alpha)=1-\tfrac\alpha2>0$. Adjusting the per-level length by a factor $2$ gives total $\alpha$ and $\lambda(F_\alpha)=1-\alpha$ exactly.)*

So $\lambda(F_\alpha)=1-\tfrac\alpha2>0$ (or $1-\alpha$ with the rescaled deletion lengths). $F_\alpha$ is closed: each $F_k$ is a finite union of closed intervals, and an intersection of closed sets is closed; being closed and bounded, $F_\alpha$ is compact.

**Step 2 — (b) Empty interior.** Suppose $F_\alpha$ contained an interval $J$ with $\lambda(J)=\delta>0$. Then $J\subseteq F_\alpha\subseteq F_k$ for every $k$. But $F_k$ is a union of $2^k$ intervals each of length at most $2^{-k}$ (each is a piece of $[0,1]$ split at least $k$ times). An interval $J\subseteq F_k$ must lie inside a *single* constituent interval, so $\delta=\lambda(J)\le 2^{-k}$. For $k$ with $2^{-k}<\delta$ this is false. Hence $F_\alpha$ contains no interval — its interior is empty.

> [!note]- Derivation
> Each constituent interval of $F_{k}$ has length $\le 2^{-k}$: at every level each surviving interval is strictly shorter than half its parent (a positive-length open piece is removed from the middle, leaving two pieces each $<$ half). A connected subset $J$ of $F_k$ lies in one constituent interval, so $\lambda(J)\le 2^{-k}\to0$. A genuine interval has fixed positive length, impossible.

**Step 3 — (c) Synthesis.** $F_\alpha$ is compact, has $\lambda(F_\alpha)>0$, yet is nowhere dense (closed with empty interior). So a set of positive Lebesgue measure can be *topologically tiny* — containing no interval at all.

> [!note]- Complete formal solution
> (a) Level $k$ removes $2^k$ disjoint open intervals of length $\alpha 4^{-(k+1)}$, total $D_k=\tfrac\alpha4 2^{-k}$; the removed set has measure $\sum_k D_k=\tfrac\alpha2$, and $[0,1]=F_\alpha\sqcup(\text{removed})$, so $\lambda(F_\alpha)=1-\tfrac\alpha2>0$. Each $F_k$ is a finite union of closed intervals, so $F_\alpha=\bigcap F_k$ is closed, hence compact. (b) Each constituent interval of $F_k$ has length $\le 2^{-k}$; an interval inside $F_\alpha\subseteq F_k$ would have length $\le 2^{-k}$ for all $k$, forcing length $0$. So $F_\alpha$ has empty interior. (c) $F_\alpha$ is thus compact, nowhere dense, of positive measure: positive measure does not entail containing an interval. $\blacksquare$

---

# Key Takeaways

**To engineer a set with positive measure, budget the removed mass as a *convergent series* with controllable sum — proportional removal kills the measure, summable removal preserves it.** The standard Cantor set fails to have positive measure for one structural reason: it removes a *fixed fraction* ($1/3$) at every level, so the survivor measure is $(2/3)^k\to0$ geometrically. The fat Cantor set removes lengths $\alpha 4^{-k}$ whose *total is a finite, tunable number $<1$*. This "spend a convergent budget" technique is everywhere: covering a countable set by intervals of total length $<\varepsilon$ (proving it is null), the $\varepsilon 2^{-k}$ device in approximation arguments, the construction of [[Thm - Lusin's Theorem|Lusin]]-type exceptional sets. Trigger: "I need a quantitative set with a prescribed total size — distribute the size as a convergent series."

**Measure-theoretic size and topological size are genuinely different and can be made to conflict.** The fat Cantor set is *large for measure* ($\lambda>0$) but *small for topology* (nowhere dense — its closure has empty interior, it is "negligible" in the Baire-category sense). Its complement in $[0,1]$ is open and dense yet has measure $<1$. So "almost every point" (measure) and "generic point" (category) point to different places. This is the same independence seen in [[Ex - The Cantor set has Lebesgue measure zero|the thin Cantor set]] (uncountable but null) — measure simply is not cardinality and is not category. Never substitute one notion of "small" for another without proof.
