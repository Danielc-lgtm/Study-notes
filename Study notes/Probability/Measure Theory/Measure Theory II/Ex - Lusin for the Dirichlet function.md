---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Lusin's Theorem"
  - "Def - Measurable Function"
tags: [analysis, measure-theory]
---

# Problem Statement

The Dirichlet function $f=\mathbf{1}_{\mathbb{Q}\cap[0,1]}$ on $[0,1]$ is measurable but **continuous at no point**.

**(a)** Verify $f$ is Borel measurable and nowhere continuous.

**(b)** [[Thm - Lusin's Theorem|Lusin's theorem]] nonetheless yields, for each $\delta>0$, a closed $F\subseteq[0,1]$ with $\lambda([0,1]\setminus F)<\delta$ and $f|_F$ continuous. Construct such an $F$ *explicitly*.

**(c)** Explain why $\delta=0$ is impossible here.

**Recall:**

![[Thm - Lusin's Theorem#Formal Statement]]

---

# Convergent Strategy

**Problem class:** making an abstract theorem concrete on a worst-case example.

**Assumption pattern:** $f$ is constant ($=0$) on the irrationals and ($=1$) on the rationals. It is *continuous on the irrationals as a subspace* — on $[0,1]\setminus\mathbb{Q}$ it is identically $0$. The bad points are $\mathbb{Q}$, a countable set; cover it by intervals of total length $<\delta$ — the [[Ex - A fat Cantor set of positive measure|convergent-budget]] device.

**Theorem routing:** delete a small open neighbourhood of $\mathbb{Q}$; on the closed remainder $f$ is constantly $0$, hence continuous.

**Key decision point:** $f|_F$ continuous does **not** mean $f$ continuous at points of $F$ — it means continuous *as a function on the subspace $F$*.

---

# Legal Operations Used

1. **Convergent-budget covering** of a countable set by intervals of total length $<\delta$.
2. **Restriction to a subspace** changes the meaning of continuity.

---

# Hints

> [!note]- Hint 1
> $f=0$ everywhere on the irrationals. If $F$ contains no rationals, what is $f|_F$?

> [!note]- Hint 2
> Enumerate $\mathbb{Q}\cap[0,1]=\{q_1,q_2,\dots\}$ and cover $q_n$ by an interval of length $\delta2^{-n}$.

---

# Solution

**Step 1 — (a).** $f^{-1}(\{1\})=\mathbb{Q}\cap[0,1]$ is Borel (countable), $f^{-1}(\{0\})$ its complement; all preimages lie among $\emptyset,\mathbb{Q}\cap[0,1],(\cdot)^c,[0,1]$ — $f$ is Borel measurable. Nowhere continuous: every interval contains both rationals and irrationals, so $f$ takes both values $0,1$ in every neighbourhood of every point — the oscillation is $1$ everywhere.

**Step 2 — (b) Explicit $F$.** Enumerate $\mathbb{Q}\cap[0,1]=\{q_1,q_2,\dots\}$ and set
$$U=\bigcup_{n\ge1}\big(q_n-\delta2^{-n-1},\,q_n+\delta2^{-n-1}\big),\qquad F=[0,1]\setminus U.$$

> [!note]- Derivation
> $U$ is open with $\lambda(U)\le\sum_n\delta2^{-n}=\delta$, so $F=[0,1]\setminus U$ is closed and $\lambda([0,1]\setminus F)=\lambda(U)<\delta$. By construction $F$ contains no rational of $[0,1]$ (each $q_n\in U$), so $f|_F\equiv0$ — a constant function, hence continuous on $F$. (One may shrink $F$ to a compact subset, but $F$ is already closed and bounded, hence compact.)

**Step 3 — (c) Why $\delta=0$ fails.** A set $F$ with $\lambda([0,1]\setminus F)=0$ and $f|_F$ continuous would have to be a positive-measure set on which $f$ is continuous. But $f|_F$ continuous and $F$ of positive measure: $F$ contains points of $\mathbb{Q}$ and of $\mathbb{Q}^c$ arbitrarily close (any positive-measure set is dense in a positive-measure portion of itself and meets both $\mathbb{Q}$ and $\mathbb{Q}^c$ near its density points), forcing $f|_F$ to oscillate. More simply: $f$ continuous on a *full-measure* $F$ would make $f$ equal a.e. to a function continuous on a dense set; but $f$ is a.e. $0$ and a continuous-on-$F$ representative cannot be $0$ on all of $F\cap\mathbb{Q}$ which is nonempty for full-measure $F$. The countable bad set $\mathbb{Q}$ has measure $0$, yet cannot be entirely *avoided* by a full-measure closed set — only by deleting an open neighbourhood, which costs positive measure $\delta>0$.

> [!note]- Complete formal solution
> (a) Preimages of $f$ lie in $\{\emptyset,\mathbb{Q}\cap[0,1],\text{irrationals},[0,1]\}$, all Borel; every interval meets $\mathbb{Q}$ and $\mathbb{Q}^c$, so $f$ has oscillation $1$ at every point. (b) Cover $\mathbb{Q}\cap[0,1]$ by an open $U$ of measure $<\delta$ (interval $\delta2^{-n-1}$ around $q_n$); $F=[0,1]\setminus U$ is compact, $\lambda([0,1]\setminus F)<\delta$, and $f|_F\equiv0$ is continuous. (c) $\delta=0$ would need a full-measure closed $F$ avoiding $\mathbb{Q}$ — impossible, since deleting the dense $\mathbb{Q}$ from a full-measure set still leaves a set whose closure is all of $[0,1]$, on which a continuous extension cannot agree with the nowhere-continuous $f$. $\blacksquare$

---

# Key Takeaways

**"$f|_F$ continuous" means continuous as a function on the *subspace* $F$ — not that $f$ is continuous at the points of $F$.** The Dirichlet function is continuous at no point of $[0,1]$, yet its restriction to the irrational-rich closed set $F$ is continuous, because on $F$ it is simply constant. Lusin does not repair the function; it finds a large set on whose *induced topology* the function happens to be tame. Keeping the subspace-vs-ambient distinction straight is essential to using Lusin correctly.

**A countable (hence null) bad set still costs positive measure to *excise by an open set* — which is why $\delta>0$ is unavoidable.** $\mathbb{Q}$ has measure zero, but it is dense, so any open neighbourhood of it has positive measure, and a *closed* set avoiding $\mathbb{Q}$ is exactly the complement of such a neighbourhood. This is the same [[Ex - A fat Cantor set of positive measure|convergent-budget]] phenomenon — one covers the countable bad set by intervals summing to $<\delta$ — and it shows why Lusin, Egorov, and regularity are all "$\delta>0$" theorems, never "$\delta=0$."
