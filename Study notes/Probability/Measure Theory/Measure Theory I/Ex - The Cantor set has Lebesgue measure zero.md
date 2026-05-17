---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Lebesgue Measure"
  - "Thm - Properties of Measures"
tags: [analysis, measure-theory]
---

# Problem Statement

The **middle-thirds Cantor set** $C\subseteq[0,1]$ is $C=\bigcap_{k=0}^\infty C_k$, where $C_0=[0,1]$ and $C_{k+1}$ is obtained from $C_k$ by deleting the open middle third of each of its constituent intervals. Thus $C_k$ is a union of $2^k$ closed intervals each of length $3^{-k}$.

**(a)** Show $C$ is closed, hence Borel, hence Lebesgue-measurable.

**(b)** Show $\lambda(C)=0$.

**(c)** Show $C$ is **uncountable**. Conclude that $C$ is an uncountable set of Lebesgue measure zero, and that the Lebesgue $\sigma$-algebra contains $2^{|C|}=2^{2^{\aleph_0}}$ subsets of $C$ — strictly more than the $2^{\aleph_0}$ Borel sets.

**Recall:**

[[Def - Lebesgue Measure|Lebesgue measure]] $\lambda$ on $\mathbb{R}$ assigns each interval its length and is countably additive. From [[Thm - Properties of Measures]]: **monotonicity** and **continuity from above** ($C_k\downarrow C$, $\lambda(C_0)=1<\infty$).

---

# Convergent Strategy

**Problem class:** computing the measure of a set defined by an infinite intersection of decreasing approximants.

**Assumption pattern:** $C$ is presented as $\bigcap_k C_k$ with $C_k\downarrow C$ and $\lambda(C_0)=1<\infty$. This is *exactly* the input type of [[Thm - Properties of Measures|continuity from above]] — a decreasing sequence with finite first term. The measure of the limit is the limit of the measures.

**Theorem routing:** $\lambda(C)=\lim_k\lambda(C_k)$ (continuity from above); $\lambda(C_k)=2^k\cdot 3^{-k}=(2/3)^k\to 0$ (finite additivity over the $2^k$ pieces).

**Key decision point:** for (c), measure and cardinality are *independent* — small measure does not mean few points. The address (base-3) description of $C$ is what reveals its uncountability.

---

# Legal Operations Used

1. **Continuity from above** for $\lambda(\bigcap C_k)=\lim\lambda(C_k)$.
2. **Finite additivity** to compute $\lambda(C_k)$ as a sum over its $2^k$ intervals.
3. **Ternary-expansion coding** to inject $\{0,1\}^{\mathbb{N}}$ into $C$.

---

# Hints

> [!note]- Hint 1
> $C_k$ is a *finite* union of intervals — finite additivity computes $\lambda(C_k)$ exactly. How many intervals, of what length?

> [!note]- Hint 2
> $C=\bigcap_k C_k$ with $C_0\supseteq C_1\supseteq\cdots$ and $\lambda(C_0)=1<\infty$. Which property of $\lambda$ converts $\lambda(\bigcap C_k)$ into $\lim\lambda(C_k)$?

> [!note]- Hint 3
> For (c): $x\in C$ iff $x$ has a base-3 expansion using only the digits $0$ and $2$. Map such expansions to binary sequences.

---

# Solution

**Step 1 — (a) $C$ is closed.** Each $C_k$ is a finite union of closed intervals, hence closed; $C=\bigcap_k C_k$ is an intersection of closed sets, hence closed. A closed set is Borel, hence Lebesgue-measurable.

**Step 2 — (b) $\lambda(C)=0$.** Count: $C_k$ consists of $2^k$ disjoint closed intervals each of length $3^{-k}$, so by finite additivity $\lambda(C_k)=2^k\cdot 3^{-k}=(2/3)^k$. Since $C_k\downarrow C$ and $\lambda(C_0)=1<\infty$, continuity from above gives
$$\lambda(C)=\lim_{k\to\infty}\lambda(C_k)=\lim_{k\to\infty}(2/3)^k=0.$$

> [!note]- Derivation
> Each removal step replaces an interval $I$ of length $\ell$ by two intervals of length $\ell/3$ each, total $2\ell/3$ — so $\lambda(C_{k+1})=\tfrac23\lambda(C_k)$, and $\lambda(C_k)=(2/3)^k$. The sequence $C_k$ is decreasing with $\bigcap_k C_k=C$ and the finite-first-term hypothesis $\lambda(C_0)=1<\infty$ of [[Thm - Properties of Measures|continuity from above]] is met. Hence $\lambda(C)=\lim(2/3)^k=0$. (Alternatively: $\lambda(C)\le\lambda(C_k)=(2/3)^k$ for every $k$ by monotonicity, so $\lambda(C)\le\inf_k(2/3)^k=0$.)

**Step 3 — (c) $C$ is uncountable.** A point $x\in[0,1]$ lies in $C$ iff it admits a base-$3$ expansion $x=\sum_{j\ge1}d_j3^{-j}$ with every digit $d_j\in\{0,2\}$ (the middle-third removals delete exactly the points *forced* to have a digit $1$).

> [!note]- Derivation
> The first removal deletes $(\tfrac13,\tfrac23)$ — the points whose first ternary digit must be $1$. Inductively, the $k$-th step deletes points forced to have digit $1$ in position $k$. So $C=\{x:\text{some base-3 expansion of }x\text{ uses only }0,2\}$. The map $\{0,1\}^{\mathbb{N}}\to C$, $(b_j)\mapsto\sum_j(2b_j)3^{-j}$, is injective (distinct $0/2$-expansions give distinct reals). Hence $|C|\ge|\{0,1\}^{\mathbb{N}}|=2^{\aleph_0}$: $C$ is uncountable.
> Consequence: $C$ is a Lebesgue-null set with $2^{\aleph_0}$ points, so it has $2^{2^{\aleph_0}}$ subsets, *all* Lebesgue-measurable (subsets of a null set, by [[Def - Null Set and Completion|completeness]] of $\lambda$). But there are only $2^{\aleph_0}$ Borel sets in total. So most subsets of $C$ are Lebesgue-measurable but not Borel — the strict inclusion $\mathcal{B}(\mathbb{R})\subsetneq\mathcal{B}^*(\mathbb{R})$.

> [!note]- Complete formal solution
> (a) Each $C_k$ is a finite union of closed intervals, hence closed; $C=\bigcap C_k$ is closed, so Borel and Lebesgue-measurable. (b) $C_k$ is $2^k$ disjoint closed intervals of length $3^{-k}$, so $\lambda(C_k)=(2/3)^k$; $C_k\downarrow C$, $\lambda(C_0)<\infty$, so by continuity from above $\lambda(C)=\lim(2/3)^k=0$. (c) $C$ is the set of reals with a base-3 expansion in digits $\{0,2\}$; $(b_j)\in\{0,1\}^{\mathbb{N}}\mapsto\sum(2b_j)3^{-j}$ injects $\{0,1\}^{\mathbb{N}}$ into $C$, so $|C|=2^{\aleph_0}$. As a null set, all $2^{2^{\aleph_0}}$ subsets of $C$ are Lebesgue-measurable, exceeding the $2^{\aleph_0}$ Borel sets. $\blacksquare$

---

# Key Takeaways

**A set defined as a decreasing intersection of finite-measure approximants is tailor-made for continuity from above.** The trigger: you see "$E=\bigcap_k E_k$" with $E_k\downarrow$ and $\lambda(E_1)<\infty$ — immediately $\lambda(E)=\lim\lambda(E_k)$, and if the approximants' measures are computable (finite unions of intervals) the answer falls out. The Cantor set, $G_\delta$ sets, the set of "Lebesgue points," and many limiting constructions all arrive in this form; continuity from above (or just plain monotonicity, $\lambda(E)\le\lambda(E_k)$ for all $k$) is the first tool to reach for.

**Measure and cardinality are completely independent: a set can be uncountable yet null.** The Cantor set has the cardinality of the continuum but length zero — "almost all" reals (in the measure sense) avoid it, yet it has just as many points as $[0,1]$. This decouples two intuitions of "size" that coincide for intervals but diverge in general, and it is the reason [[Def - Null Set and Completion|completion]] is necessary: a single null set already carries more subsets than there are Borel sets, so the Lebesgue $\sigma$-algebra must be strictly larger than the Borel one. The trigger-reaction: never infer "uncountable, therefore positive measure" — for that you need a *fat* Cantor set, built by removing *summably small* middles.
