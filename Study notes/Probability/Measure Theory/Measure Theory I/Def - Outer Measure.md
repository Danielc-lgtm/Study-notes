---
type: definition
subject: measure-theory
prereqs:
  - "Def - Pre-Measure"
  - "Def - Measure and Measure Space"
tags: [analysis, measure-theory]
---

# Notation

$X$ is a set, $2^X$ its power set. $\mu^*$ denotes an outer measure. A family $\mathcal{K} \subseteq 2^X$ is a **cover** of $X$ if $\emptyset \in \mathcal{K}$ and $X = \bigcup_{n} K_n$ for some sequence $(K_n) \subseteq \mathcal{K}$.

---

# Axiom Motivation

We have a [[Def - Pre-Measure|pre-measure]] $\widetilde\mu$ defined only on an algebra (or, more generally, a "cover" — any family containing $\emptyset$ that covers $X$). We want a size for *every* subset of $X$, even the wild ones. The honest, geometric way to estimate the size of an arbitrary set $E$ is the one Lebesgue used: **cover it from outside** by countably many elementary pieces whose sizes we already know, add those sizes, and take the most economical such cover:
$$\mu^*(E) = \inf\Big\{ \textstyle\sum_j \widetilde\mu(K_j) : E \subseteq \bigcup_j K_j,\ K_j \in \mathcal{K} \Big\}.$$
This is an *over*-estimate by construction — hence "outer." It is defined for every $E \subseteq 2^X$, so it solves the domain problem completely.

The price is that $\mu^*$ is *not* a measure: it is only **countably subadditive**, not additive. Covering $A$ and $B$ separately and adding can over-count their overlap, and even for disjoint sets the two optimal covers need not combine into an optimal cover of the union — so $\mu^*(A\sqcup B)$ can be strictly less than $\mu^*(A)+\mu^*(B)$. (For a *non-measurable* set this failure of additivity is unavoidable; that is the content of [[Thm - Existence of a Non-Measurable Set|Vitali's construction]].)

So an outer measure is a deliberately weakened object: it trades additivity for *total* domain. The three axioms it does keep — $\mu^*(\emptyset)=0$, monotonicity, countable subadditivity — are exactly the ones that survive the "$\inf$ over covers" construction. The job of the [[Def - Carathéodory Measurable Sets|Carathéodory criterion]] is then to *carve out* of $2^X$ the sub-$\sigma$-algebra on which $\mu^*$ does become additive, recovering a genuine measure.

---

# The Definition

An **outer measure** on $X$ is a function $\mu^* : 2^X \to [0,\infty]$ such that

1. $\mu^*(\emptyset) = 0$;
2. (**monotonicity**) $A \subseteq B \implies \mu^*(A) \leq \mu^*(B)$;
3. (**countable subadditivity**) $A \subseteq \bigcup_{k=1}^\infty A_k \implies \mu^*(A) \leq \sum_{k=1}^\infty \mu^*(A_k)$.

Crucially, $\mu^*$ is defined on **all** of $2^X$, and is *not* required to be additive.

**Construction from a cover.** Given a cover $\mathcal{K}$ of $X$ and any $\widetilde\mu : \mathcal{K} \to [0,\infty]$ with $\widetilde\mu(\emptyset)=0$, the formula
$$\mu^*(A) = \inf\Big\{ \textstyle\sum_{j=1}^\infty \widetilde\mu(K_j) : K_j \in \mathcal{K},\ A \subseteq \bigcup_{j=1}^\infty K_j \Big\}$$
defines an outer measure on $X$ ([[Thm - Carathéodory's σ-Algebra|Proposition 1.10]]). The infimum is over a nonempty set because $\mathcal{K}$ covers $X$.

---

# Relate to Other Fields / Compression

An outer measure is the measure-theoretic instance of a *gauge* or *capacity*: a monotone, subadditive set function. It is the analogue of the **outer content** in Jordan's theory, but with *countable* covers replacing finite ones — and that single change (finite $\to$ countable) is exactly what makes the resulting class of measurable sets a $\sigma$-algebra rather than a mere algebra, and what makes the integral handle limits. The "$\inf$ over coverings" pattern recurs as Hausdorff measure (covers by small balls, weighted by a power of the diameter), as the definition of a norm via covers in geometric measure theory, and as outer regularity $\lambda(A) = \inf\{\lambda(G): G \supseteq A \text{ open}\}$.

---

# Examples / Corollaries

**Lebesgue outer measure.** On $\mathbb{R}^n$, take $\mathcal{K}$ = boxes and $\widetilde\mu$ = elementary volume; the resulting $\mu^* = \lambda^*$ assigns an outer size to *every* subset, including non-measurable ones.

**A subadditive-but-not-additive outer measure.** Define $\mu^*(\emptyset)=0$ and $\mu^*(A)=1$ for every nonempty $A \subseteq X$. Axioms (1)–(3) hold, yet $\mu^*$ is wildly non-additive ($\mu^*(A\sqcup B)=1 < 2$). It illustrates that "outer measure" is a strictly weaker notion than "measure."

Calibration: (i) Is every measure an outer measure? Only after extending it by $0$ outside its $\sigma$-algebra — a measure is defined on a $\sigma$-algebra, an outer measure on all of $2^X$; on its domain a measure *is* monotone and subadditive. (ii) Is an outer measure ever additive? Yes — on its [[Def - Carathéodory Measurable Sets|Carathéodory-measurable sets]], where it restricts to a genuine measure. (iii) Why "outer"? Because $\mu^*(E)$ is computed by approximating $E$ *from outside* by covers, so it over-estimates.

---

# Unlocked by This

> [!tip] Carathéodory's criterion
> An outer measure becomes a measure once restricted to the sets $A$ that "split every test set additively": $\mu^*(B) = \mu^*(B\cap A) + \mu^*(B\setminus A)$ for all $B$. These form the [[Def - Carathéodory Measurable Sets|Carathéodory $\sigma$-algebra]] $\Sigma$, and $\mu^*|_\Sigma$ is a measure — see [[Thm - Carathéodory's σ-Algebra]].
