---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Outer Measure"
  - "Def - Carathéodory Measurable Sets"
  - "Def - Measure and Measure Space"
tags: [analysis, measure-theory]
---

# Notation

$\mu^*$ is an [[Def - Outer Measure|outer measure]] on $X$; $\Sigma$ is the family of [[Def - Carathéodory Measurable Sets|Carathéodory-measurable]] sets, those $A$ with $\mu^*(B)=\mu^*(B\cap A)+\mu^*(B\setminus A)$ for all $B\subseteq X$. $\mathcal{K}$ is a [[Def - Outer Measure|cover]] of $X$, $\widetilde\mu:\mathcal{K}\to[0,\infty]$ a set function with $\widetilde\mu(\emptyset)=0$.

---

# Motivation

An outer measure is defined everywhere but is only subadditive — not a measure. The [[Def - Carathéodory Measurable Sets|Carathéodory criterion]] proposes a subclass $\Sigma$ on which $\mu^*$ ought to behave. This theorem delivers the two facts that make the whole construction of measures work: $\Sigma$ is *automatically a $\sigma$-algebra* (we never assumed closure under countable unions — it is forced), and $\mu^*$ restricted to $\Sigma$ is *automatically a genuine, countably additive measure*. Together with the companion fact that the "$\inf$ over covers" formula produces an outer measure in the first place, this is the machine that turns a [[Def - Pre-Measure|pre-measure]] into a measure.

---

# Sources and Targets

**Sources.** The theorem's input is "$\mu^*$ is an outer measure." The non-obvious source: *any cover $\mathcal{K}$ with a set function $\widetilde\mu$* produces, via $\mu^*(A)=\inf\{\sum\widetilde\mu(K_j):A\subseteq\bigcup K_j\}$, an outer measure — so the theorem applies. One does not need to *verify* the outer-measure axioms by hand each time; recognising "$\inf$ over countable covers" is enough.

**Targets.** The output "$\Sigma$ is a $\sigma$-algebra and $\mu^*|_\Sigma$ is a measure" combines with: (i) *the algebra $\mathcal{A}\subseteq\Sigma$* (proved separately) to give $\sigma(\mathcal{A})\subseteq\Sigma$, hence a measure on the generated $\sigma$-algebra — this is the [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]]; (ii) *completeness* — since null sets always lie in $\Sigma$, the resulting measure is complete; (iii) *$\sigma$-finiteness of $\widetilde\mu$* to give uniqueness.

---

# Formal Statement

**(A) Outer measure from a cover.** Let $\mathcal{K}$ be a cover of $X$ and $\widetilde\mu:\mathcal{K}\to[0,\infty]$ with $\widetilde\mu(\emptyset)=0$. Then
$$\mu^*(A) = \inf\Big\{\sum_{j=1}^\infty\widetilde\mu(K_j) : K_j\in\mathcal{K},\ A\subseteq\textstyle\bigcup_j K_j\Big\}, \qquad A\subseteq X,$$
is an [[Def - Outer Measure|outer measure]] on $X$.

**(B) Carathéodory's theorem.** For any outer measure $\mu^*$ on $X$, the family $\Sigma$ of Carathéodory-measurable sets is a $\sigma$-algebra, and the restriction $\mu := \mu^*|_\Sigma : \Sigma \to [0,\infty]$ is a [[Def - Measure and Measure Space|measure]] on $(X,\Sigma)$. Moreover $\Sigma$ is **complete**: every set of $\mu^*$-outer-measure zero lies in $\Sigma$.

---

# Why Is It True

**(A)** is bookkeeping. The "$\inf$ over covers" is well-defined because the cover $\mathcal{K}$ supplies at least one admissible covering of any $A$. Monotonicity is clear — a cover of $B$ is a cover of any $A\subseteq B$, so the infimum for $A$ is over a *larger* family, hence smaller. Subadditivity is the standard "$\varepsilon/2^k$" argument: cover each $A_k$ to within $\varepsilon 2^{-k}$ of its outer measure, take the union of all these covers, and the total cost overshoots $\sum\mu^*(A_k)$ by at most $\varepsilon$.

**(B)** is the real content. Why should the Carathéodory criterion — a condition phrased with a *universal quantifier over all test sets $B$* — produce closure under *countable* unions? Precisely *because* of that universal quantifier. When you try to show $A_1\cup A_2 \in\Sigma$, you split a test set $B$ using $A_1$, then split each piece again using $A_2$; because $A_1,A_2\in\Sigma$ the criterion can be invoked *on the sub-pieces*, not just on $B$. The quantifier is strong enough to be applied recursively. Iterating gives finite unions; then for a countable union you split off finitely many pieces, use *monotonicity* of $\mu^*$ to bound the rest, and let the number of pieces $\to\infty$. The tail estimate goes through because the finite-union criterion produces, for disjoint sets, the *exact additive* identity $\mu^*(B\cap\bigcup_{k\le m}A_k)=\sum_{k\le m}\mu^*(B\cap A_k)$, whose partial sums are monotone and bounded.

That same identity, taken with $B=X$, *is* countable additivity of $\mu^*$ on $\Sigma$: subadditivity gives one inequality, the finite-additivity-plus-monotonicity argument gives the other. So $\mu^*|_\Sigma$ is a measure for the same reason $\Sigma$ is a $\sigma$-algebra — both are the universal quantifier paying off.

---

# What Makes This Hard

The proof of (B) is not hard *step by step* but is hard to *motivate*: every move is "split the test set $B$ by the next available measurable set and invoke the criterion on the pieces," and one must trust that the universal quantifier survives the recursion. The single non-obvious step is, in proving closure under countable unions, the passage from finite unions to the infinite union: one keeps finitely many disjointified pieces explicit and *bounds the infinite tail by monotonicity*, then lets the finite count $\to\infty$. Most errors come from trying to handle all infinitely many pieces at once instead of "finitely many exact, tail bounded."

---

# Rederivation Scaffold

**High-level strategy.** (A): unwind the $\inf$ with an $\varepsilon 2^{-k}$ cover. (B): verify the $\sigma$-algebra axioms for $\Sigma$ in the order $X,\ {}^c,\ \cup$ (finite then countable), reading additivity of $\mu^*|_\Sigma$ off the finite-union computation.

**Subgoal decomposition.**

1. **(A) $\mu^*$ is an outer measure.** Show $\mu^*(\emptyset)=0$ (cover by $\emptyset$), monotonicity (larger set, smaller family of covers), subadditivity ($\varepsilon 2^{-k}$).
2. **$X,\emptyset\in\Sigma$ and $\Sigma$ is complement-closed.** The criterion for $A$ and for $A^c$ are the same equation.
   - *Hint:* the two terms $B\cap A$ and $B\setminus A$ swap roles.
3. **$\Sigma$ closed under finite unions.** For $A_1,A_2\in\Sigma$ and any $B$: split $B$ by $A_1$, split $B\setminus A_1$ by $A_2$, recombine using subadditivity.
   - *Why needed:* base case; iterate for all finite unions.
4. **Finite additivity on disjoint sets.** For disjoint $A_1,\dots,A_m\in\Sigma$, prove $\mu^*(B\cap\bigsqcup A_k)=\sum\mu^*(B\cap A_k)$ by induction, peeling off $A_m$ with its criterion.
5. **$\Sigma$ closed under countable unions + $\sigma$-additivity.** Reduce to disjoint $A_k$ (disjointify). For each $m$ use step 4 plus monotonicity: $\mu^*(B)\ge\sum_{k\le m}\mu^*(B\cap A_k)+\mu^*(B\setminus\bigcup_{k}A_k)$; let $m\to\infty$, then use subadditivity for the reverse inequality. Setting $B=X$ yields $\sigma$-additivity.

---

# Lemma Decomposition

> [!note]- Lemma 1: The cover formula gives an outer measure
> **Statement:** $\mu^*$ defined by the $\inf$-over-covers formula satisfies $\mu^*(\emptyset)=0$, monotonicity, countable subadditivity.
>
> **Hint:** $\varepsilon 2^{-k}$ for subadditivity.
>
> > [!note]- Full proof
> > $\mu^*(\emptyset)=0$: cover $\emptyset$ by $K_j=\emptyset$, cost $0$. Monotonicity: every cover of $B$ covers $A\subseteq B$, so $\mu^*(A)$ is an inf over a superset of covers, hence $\le\mu^*(B)$. Subadditivity: given $A\subseteq\bigcup_k A_k$ and $\varepsilon>0$, pick covers $(K_{k,j})_j$ of $A_k$ with $\sum_j\widetilde\mu(K_{k,j})<\mu^*(A_k)+\varepsilon 2^{-k}$. Then $(K_{k,j})_{k,j}$ covers $A$, so $\mu^*(A)\le\sum_{k,j}\widetilde\mu(K_{k,j})<\sum_k\mu^*(A_k)+\varepsilon$; let $\varepsilon\downarrow 0$. $\square$

> [!note]- Lemma 2: $\Sigma$ is an algebra
> **Statement:** $X\in\Sigma$; $A\in\Sigma\Rightarrow A^c\in\Sigma$; $A_1,A_2\in\Sigma\Rightarrow A_1\cup A_2\in\Sigma$.
>
> **Hint:** Closure under union: split $B$, then split $B\setminus A_1$.
>
> > [!note]- Full proof
> > $X\in\Sigma$: $\mu^*(B\cap X)+\mu^*(B\setminus X)=\mu^*(B)+\mu^*(\emptyset)=\mu^*(B)$. Complement: the defining equation is symmetric in $A\leftrightarrow A^c$ since $B\cap A^c=B\setminus A$. Union: for any $B$, applying the criterion of $A_1$ then of $A_2$ to $B\setminus A_1$,
> > $$\mu^*(B)=\mu^*(B\cap A_1)+\mu^*(B\setminus A_1)=\mu^*(B\cap A_1)+\mu^*((B\setminus A_1)\cap A_2)+\mu^*((B\setminus A_1)\setminus A_2).$$
> > The first three sets cover $B\cap(A_1\cup A_2)$, so by subadditivity their measures sum to $\ge\mu^*(B\cap(A_1\cup A_2))$; the last set is $B\setminus(A_1\cup A_2)$. Hence $\mu^*(B)\ge\mu^*(B\cap(A_1\cup A_2))+\mu^*(B\setminus(A_1\cup A_2))$, the only inequality needed. $\square$

> [!note]- Lemma 3: $\Sigma$ is a $\sigma$-algebra and $\mu^*|_\Sigma$ is a measure
> **Statement:** $\Sigma$ is closed under countable unions and $\mu^*|_\Sigma$ is $\sigma$-additive.
>
> **Hint:** Disjointify; keep $m$ pieces exact, bound the tail by monotonicity, let $m\to\infty$.
>
> > [!note]- Full proof
> > It suffices to treat pairwise disjoint $A_k\in\Sigma$ (disjointify via $\widetilde A_k=A_k\setminus\bigcup_{j<k}A_j\in\Sigma$ by Lemma 2). Induction with the criterion of $A_m$ gives, for every test $B$,
> > $$\mu^*\Big(B\cap\bigcup_{k=1}^m A_k\Big)=\sum_{k=1}^m\mu^*(B\cap A_k).$$
> > Since $\bigcup_{k\le m}A_k\in\Sigma$ (Lemma 2),
> > $$\mu^*(B)=\mu^*\Big(B\cap\bigcup_{k\le m}A_k\Big)+\mu^*\Big(B\setminus\bigcup_{k\le m}A_k\Big)\ge\sum_{k=1}^m\mu^*(B\cap A_k)+\mu^*\Big(B\setminus\bigcup_{k=1}^\infty A_k\Big),$$
> > using monotonicity for the tail. Let $m\to\infty$: $\mu^*(B)\ge\sum_k\mu^*(B\cap A_k)+\mu^*(B\setminus\bigcup A_k)\ge\mu^*(B\cap\bigcup A_k)+\mu^*(B\setminus\bigcup A_k)$, the last by subadditivity. So $\bigcup A_k\in\Sigma$. Taking $B=X$ in the displayed chain forces equality throughout, giving $\mu^*(\bigsqcup A_k)=\sum\mu^*(A_k)$ — $\sigma$-additivity of $\mu^*|_\Sigma$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 is statement (A). Lemmas 2–3 prove (B): $\Sigma$ contains $X$, is closed under complement and countable union, so is a $\sigma$-algebra; $\mu^*|_\Sigma$ satisfies $\mu(\emptyset)=\mu^*(\emptyset)=0$ and $\sigma$-additivity, so is a measure. Completeness: if $\mu^*(N)=0$ then for any $B$, $\mu^*(B\cap N)\le\mu^*(N)=0$ and $\mu^*(B\setminus N)\le\mu^*(B)$, so $N\in\Sigma$; any subset of $N$ also has outer measure $0$, hence lies in $\Sigma$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The Carathéodory machine is not special to length: feed it $\mathcal{K}=$ balls and $\widetilde\mu(K)=(\operatorname{diam}K)^s$ and you get **$s$-dimensional Hausdorff measure**, the foundation of fractal geometry. Feed it cylinder sets of an infinite product and a consistent family of finite-dimensional laws, and the same theorem builds the law of a [[Def - Brownian Motion|stochastic process]] — the Kolmogorov extension theorem is Carathéodory in disguise.

---

# Bridges

- **[[Thm - Hahn-Carathéodory Extension Theorem]]** — this theorem is its engine: the extension theorem is "(B) plus the verification $\mathcal{A}\subseteq\Sigma$."
- **[[Def - Null Set and Completion]]** — completeness of $\Sigma$ is why the Lebesgue $\sigma$-algebra is the *completion* of the Borel $\sigma$-algebra.
- **[[Thm - Properties of Measures]]** — once $\mu^*|_\Sigma$ is known to be a measure, all five general properties apply to it.
