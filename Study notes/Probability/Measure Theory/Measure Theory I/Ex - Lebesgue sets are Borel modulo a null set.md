---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Lebesgue Measure"
  - "Def - Null Set and Completion"
  - "Thm - Regularity of Lebesgue Measure"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $A\subseteq\mathbb{R}^n$ be Lebesgue-measurable, $A\in\mathcal{B}^*(\mathbb{R}^n)$.

**(a)** Show there is a Borel set $B\supseteq A$ of **$G_\delta$ type** (a countable intersection of open sets) with $\lambda(B\setminus A)=0$.

**(b)** Show there is a Borel set $C\subseteq A$ of **$F_\sigma$ type** (a countable union of closed sets) with $\lambda(A\setminus C)=0$.

**(c)** Conclude: every Lebesgue-measurable set equals a Borel set modified on a Lebesgue-null set, $A=B\setminus N=C\cup M$ with $N,M$ null. Hence the Lebesgue $\sigma$-algebra is exactly $\{B\,\triangle\,N : B\in\mathcal{B}(\mathbb{R}^n),\ N\text{ null}\}$ — it is the [[Def - Null Set and Completion|completion]] of the Borel $\sigma$-algebra.

**Recall:**

[[Thm - Regularity of Lebesgue Measure|Regularity]]: for measurable $A$ and any $\varepsilon>0$ there is open $G\supseteq A$ with $\lambda(G\setminus A)<\varepsilon$ and closed $F\subseteq A$ with $\lambda(A\setminus F)<\varepsilon$. The [[Def - Null Set and Completion|completion]] of $(\mathbb{R}^n,\mathcal{B},\lambda)$ is the Lebesgue $\sigma$-algebra.

---

# Convergent Strategy

**Problem class:** structure theorem — pin down the *shape* of a generic measurable set relative to the Borel sets.

**Assumption pattern:** "$A$ measurable" gives, via [[Thm - Regularity of Lebesgue Measure|regularity]], approximation from outside by open sets to *any* tolerance $\varepsilon>0$. A single approximation leaves an $\varepsilon$-gap; *intersecting a sequence* of approximations with $\varepsilon=1/k$ drives the gap to exactly $0$.

**Theorem routing:** open $G_k\supseteq A$ with $\lambda(G_k\setminus A)<1/k$; then $B=\bigcap_k G_k$ is $G_\delta$, contains $A$, and $\lambda(B\setminus A)\le 1/k$ for all $k$, hence $=0$.

**Key decision point:** the move from "$\varepsilon$-close for every $\varepsilon$" to "exactly equal modulo null" — done by *intersecting/unioning a sequence of approximants*, the standard upgrade.

---

# Legal Operations Used

1. **Regularity** to get open supersets / closed subsets to any tolerance.
2. **Sequence-and-intersect** — take $\varepsilon=1/k$ and form $\bigcap_k G_k$ to collapse the gap to $0$.
3. **Complementation** to convert the $G_\delta$ statement into the $F_\sigma$ one.

---

# Hints

> [!note]- Hint 1
> Regularity gives, for each $k$, an open $G_k\supseteq A$ with $\lambda(G_k\setminus A)<1/k$. A single $G_k$ is not enough — combine them.

> [!note]- Hint 2
> Set $B=\bigcap_k G_k$. Then $A\subseteq B$ and $B\setminus A\subseteq G_k\setminus A$ for *every* $k$. What does that force $\lambda(B\setminus A)$ to be?

> [!note]- Hint 3
> For (b), apply (a) to $A^c$ (also measurable) and complement: a $G_\delta$ superset of $A^c$ complements to an $F_\sigma$ subset of $A$.

---

# Solution

**Step 1 — (a) The $G_\delta$ hull.** For each $k\ge1$, regularity gives an open set $G_k\supseteq A$ with $\lambda(G_k\setminus A)<1/k$. Put $B=\bigcap_{k\ge1}G_k$.

> [!note]- Derivation
> $B$ is a countable intersection of open sets — a $G_\delta$, in particular Borel. Since $A\subseteq G_k$ for every $k$, $A\subseteq B$. And $B\subseteq G_k$, so $B\setminus A\subseteq G_k\setminus A$, giving $\lambda(B\setminus A)\le\lambda(G_k\setminus A)<1/k$ for *every* $k$. A nonnegative number below $1/k$ for all $k$ is $0$: $\lambda(B\setminus A)=0$.

So $A=B\setminus N$ with $B$ a $G_\delta$ and $N=B\setminus A$ null.

**Step 2 — (b) The $F_\sigma$ kernel.** Apply (a) to $A^c$ (Lebesgue-measurable, as $\mathcal{B}^*$ is a $\sigma$-algebra): there is a $G_\delta$ set $B'\supseteq A^c$ with $\lambda(B'\setminus A^c)=0$. Set $C=(B')^c$.

> [!note]- Derivation
> $B'$ is a countable intersection of open sets, so $C=(B')^c$ is a countable union of closed sets — an $F_\sigma$, Borel. From $A^c\subseteq B'$ we get $C=(B')^c\subseteq A$. And $A\setminus C=A\cap B'=B'\cap(A^c)^c=B'\setminus A^c$, so $\lambda(A\setminus C)=\lambda(B'\setminus A^c)=0$.

So $A=C\cup M$ with $C$ an $F_\sigma$ and $M=A\setminus C$ null.

**Step 3 — (c) Identification of the completion.** From (a)–(b), every Lebesgue set $A$ satisfies $A=B\setminus N$ ($B$ Borel, $N$ null). Conversely, every set of the form $B\,\triangle\,N$ with $B$ Borel and $N$ contained in a Borel null set is Lebesgue-measurable, because $\mathcal{B}^*$ is a $\sigma$-algebra containing the Borel sets and (by [[Ex - Null sets are Carathéodory measurable|completeness]]) all subsets of null sets. Hence
$$\mathcal{B}^*(\mathbb{R}^n)=\{B\,\triangle\,N : B\in\mathcal{B}(\mathbb{R}^n),\ N\text{ a subset of a Borel null set}\},$$
which is precisely the [[Def - Null Set and Completion|completion]] of $\mathcal{B}(\mathbb{R}^n)$.

> [!note]- Complete formal solution
> (a) For each $k$, regularity yields open $G_k\supseteq A$, $\lambda(G_k\setminus A)<1/k$; $B=\bigcap_k G_k$ is $G_\delta$, $A\subseteq B$, and $\lambda(B\setminus A)\le\inf_k\lambda(G_k\setminus A)=0$. (b) Apply (a) to $A^c$: $G_\delta$ set $B'\supseteq A^c$ with $\lambda(B'\setminus A^c)=0$; $C=(B')^c$ is $F_\sigma$, $C\subseteq A$, $\lambda(A\setminus C)=\lambda(B'\setminus A^c)=0$. (c) Thus $A=B\setminus N$ with $B$ Borel, $N$ null; conversely $\mathcal{B}^*$ contains all such symmetric differences; so $\mathcal{B}^*(\mathbb{R}^n)$ is the completion of $\mathcal{B}(\mathbb{R}^n)$. $\blacksquare$

---

# Key Takeaways

**Approximation "to every $\varepsilon$" upgrades to "exact, modulo null" by sequencing the tolerances and intersecting.** A single regularity step gives $\lambda(G\setminus A)<\varepsilon$ — an $\varepsilon$-gap that never closes. But running it at $\varepsilon=1/k$ and intersecting, $B=\bigcap_k G_k$, makes the gap $\le 1/k$ for *all* $k$, hence $0$. This "$\varepsilon\to1/k\to$ intersect/union" upgrade is one of the most reused moves in measure theory: it turns the *quantitative* statement "Borel sets approximate" into the *qualitative* structure theorem "every measurable set is Borel up to a null set." Trigger: you have an estimate with a free $\varepsilon$ and want an exact statement — sequence the $\varepsilon$ and take a countable intersection (for $\supseteq$) or union (for $\subseteq$).

**The Lebesgue $\sigma$-algebra is just the Borel $\sigma$-algebra plus null-set fuzz — nothing more exotic.** Every Lebesgue set is a $G_\delta$ minus a null set (equivalently an $F_\sigma$ plus a null set). This is what "$\mathcal{B}^*$ is the [[Def - Null Set and Completion|completion]] of $\mathcal{B}$" *means* concretely, and it has a practical payoff: to prove a statement for all Lebesgue-measurable sets, prove it for Borel sets and check it is unaffected by null-set modifications — the null part carries no measure and, by [[Ex - Null sets are Carathéodory measurable|completeness]], no measurability obstruction. This is why one can almost always work with Borel sets and Borel functions and only invoke the completion when an a.e.-defined object needs to be honestly measurable.
