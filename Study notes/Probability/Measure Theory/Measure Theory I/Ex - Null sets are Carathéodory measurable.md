---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Outer Measure"
  - "Def - Carathéodory Measurable Sets"
  - "Def - Null Set and Completion"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $\mu^*$ be an [[Def - Outer Measure|outer measure]] on a set $X$, and let $\Sigma$ be its $\sigma$-algebra of [[Def - Carathéodory Measurable Sets|Carathéodory-measurable]] sets.

**(a)** Show that every set $N$ with $\mu^*(N)=0$ belongs to $\Sigma$.

**(b)** Deduce that every subset of a $\mu^*$-null set belongs to $\Sigma$ — i.e. the measure space $(X,\Sigma,\mu^*|_\Sigma)$ is **complete**.

**(c)** Conclude that Lebesgue measure, being built by the Carathéodory construction, is automatically complete, and hence that the Lebesgue $\sigma$-algebra contains every subset of every Borel null set.

**Recall:**

![[Def - Carathéodory Measurable Sets#The Definition]]

A set is **null** if $\mu^*(N)=0$; a measure space is [[Def - Null Set and Completion|complete]] if every subset of a null set is measurable.

---

# Convergent Strategy

**Problem class:** verifying membership in the Carathéodory $\sigma$-algebra — i.e. checking the splitting identity $\mu^*(B)=\mu^*(B\cap A)+\mu^*(B\setminus A)$.

**Assumption pattern:** the hypothesis $\mu^*(N)=0$ is *as strong as a hypothesis can be* — it forces $\mu^*$ to vanish on $N$ and, by monotonicity, on every subset of $N$. Whenever an outer measure of a set is $0$, monotonicity makes that set "invisible," and invisible sets split everything trivially.

**Theorem routing:** the Carathéodory criterion requires only the inequality "$\ge$" (subadditivity gives "$\le$" free). For a null set, bound $\mu^*(B\cap N)$ above by $\mu^*(N)=0$ and $\mu^*(B\setminus N)$ above by $\mu^*(B)$ — the two upper bounds already sum to $\mu^*(B)$.

**Key decision point:** recognising that "only $\ge$ needs checking" plus "$\mu^*(B\cap N)=0$" makes the verification a two-line monotonicity argument.

---

# Legal Operations Used

1. **Reduce the Carathéodory criterion to one inequality** — subadditivity supplies "$\le$" automatically.
2. **Monotonicity of the outer measure** — $C\subseteq D\Rightarrow\mu^*(C)\le\mu^*(D)$.
3. **Squeeze a nonnegative quantity to zero** by an upper bound of $0$.

---

# Hints

> [!note]- Hint 1
> By [[Def - Carathéodory Measurable Sets|definition]], $N\in\Sigma$ iff $\mu^*(B)=\mu^*(B\cap N)+\mu^*(B\setminus N)$ for all $B$. Subadditivity gives "$\le$" for free. Which inequality remains?

> [!note]- Hint 2
> Bound each of the two terms on the right separately. What is $\mu^*(B\cap N)$, given $B\cap N\subseteq N$ and $\mu^*(N)=0$?

> [!note]- Hint 3
> For (b), if $N'\subseteq N$ with $\mu^*(N)=0$, what does monotonicity say about $\mu^*(N')$?

---

# Solution

**Step 1 — Reduce to one inequality.** For any $A$ and any test set $B$, countable subadditivity of $\mu^*$ applied to $B\subseteq(B\cap A)\cup(B\setminus A)$ gives $\mu^*(B)\le\mu^*(B\cap A)+\mu^*(B\setminus A)$. So $A\in\Sigma$ iff the *reverse* inequality $\mu^*(B)\ge\mu^*(B\cap A)+\mu^*(B\setminus A)$ holds for all $B$.

**Step 2 — (a) Verify the reverse inequality for $N$.** Let $\mu^*(N)=0$ and let $B\subseteq X$ be arbitrary. Then
$$\mu^*(B\cap N)\le\mu^*(N)=0,\qquad \mu^*(B\setminus N)\le\mu^*(B),$$
both by monotonicity ($B\cap N\subseteq N$ and $B\setminus N\subseteq B$). Adding,
$$\mu^*(B\cap N)+\mu^*(B\setminus N)\le 0+\mu^*(B)=\mu^*(B).$$
This is the required "$\ge$". With Step 1's "$\le$", equality holds for every $B$, so $N\in\Sigma$.

> [!note]- Derivation
> $\mu^*(B\cap N)$ is nonnegative and bounded above by $0$, hence equals $0$. So the sum $\mu^*(B\cap N)+\mu^*(B\setminus N)$ is just $\mu^*(B\setminus N)\le\mu^*(B)$. The Carathéodory equation holds, so $N$ is Carathéodory-measurable.

**Step 3 — (b) Completeness.** Let $N'\subseteq N$ with $\mu^*(N)=0$. By monotonicity $\mu^*(N')\le\mu^*(N)=0$, so $N'$ is itself a null set. By Step 2, $N'\in\Sigma$. Thus every subset of a null set is measurable: $(X,\Sigma,\mu^*|_\Sigma)$ is complete.

> [!note]- Derivation
> The key observation: "subset of a null set" is itself a null set, by monotonicity — null-ness is *hereditary* downward. And part (a) showed *all* null sets are in $\Sigma$. Composition of these two facts is completeness.

**Step 4 — (c) Lebesgue measure is complete.** Lebesgue measure is constructed as $\mu^*|_\Sigma$ for $\mu^*$ the [[Def - Lebesgue Measure|Lebesgue outer measure]]. By (b) this is a complete measure space. Hence the Lebesgue $\sigma$-algebra $\mathcal{B}^*(\mathbb{R}^n)$ contains every subset of every Lebesgue-null set — in particular every subset of every Borel null set, e.g. every subset of the Cantor set.

> [!note]- Complete formal solution
> (a) Subadditivity gives $\mu^*(B)\le\mu^*(B\cap N)+\mu^*(B\setminus N)$ always. Conversely, for $\mu^*(N)=0$: $B\cap N\subseteq N\Rightarrow\mu^*(B\cap N)\le\mu^*(N)=0$, and $B\setminus N\subseteq B\Rightarrow\mu^*(B\setminus N)\le\mu^*(B)$; summing, $\mu^*(B\cap N)+\mu^*(B\setminus N)\le\mu^*(B)$. Both inequalities give equality, so $N\in\Sigma$. (b) If $N'\subseteq N$, $\mu^*(N)=0$, then $\mu^*(N')\le\mu^*(N)=0$ by monotonicity, so $N'$ is null and by (a) lies in $\Sigma$ — completeness. (c) The Carathéodory construction yields $\mu^*|_\Sigma$; by (b) it is complete, so $\mathcal{B}^*(\mathbb{R}^n)$ contains all subsets of Borel null sets. $\blacksquare$

---

# Key Takeaways

**Sets of outer measure zero are "invisible" — they split every test set trivially, hence are always Carathéodory-measurable.** The trigger pattern: the moment you know $\mu^*(N)=0$, you know $N\in\Sigma$ *and* $N$ contributes nothing to any measure computation, because monotonicity squeezes $\mu^*(\cdot\cap N)$ to $0$. This is why "[[Def - Almost Everywhere|almost everywhere]]" reasoning is robust: modifying a function on a null set, or excluding a null exceptional set, never leaves the world of measurable objects. Whenever a proof produces a "bad set" and you can bound its outer measure by $0$, that bad set can be absorbed for free.

**The Carathéodory construction is *automatically* complete — completeness is not an extra step, it is a built-in feature.** This is the structural reason the Lebesgue $\sigma$-algebra is strictly larger than the Borel one: $\mathcal{B}^*$ swallows every subset of every Borel null set, while $\mathcal{B}$ does not. The general principle: whenever a measure is obtained by restricting an outer measure to its Carathéodory $\sigma$-algebra (Lebesgue, Hausdorff, Lebesgue–Stieltjes, the [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]]'s output), you get completeness free of charge — so you may always assume a.e.-defined objects are measurable without re-checking. Only measures *not* built this way (e.g. the bare Borel restriction) need an explicit [[Def - Null Set and Completion|completion]].
