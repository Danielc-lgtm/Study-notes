---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Lebesgue Measure"
  - "Def - Borel σ-Algebra"
  - "Thm - Properties of Measures"
tags: [analysis, measure-theory]
---

# Notation

$\lambda$ is [[Def - Lebesgue Measure|Lebesgue measure]] on $\mathbb{R}^n$, $\mathcal{B}(\mathbb{R}^n)$ the Borel sets. $G$ ranges over open sets, $F$ over closed sets, $K$ over compact sets. $A\,\triangle\,B$ is symmetric difference.

---

# Motivation

A Borel set can be arbitrarily intricate. The point of regularity is that, *as far as measure is concerned*, every Borel set is indistinguishable from a simple one: it can be squeezed between a closed set from inside and an open set from outside, with the gap as small as we like. Measure-theoretically, the wild Borel sets are a tame open set plus-or-minus a negligible error.

This is the workhorse approximation principle of the subject. Want to prove something for all measurable sets? Prove it for open sets (or for [[Def - Interval and Elementary Figure|elementary figures]], or compact sets), then transport it across the small-measure gap. Regularity is what makes that transport legitimate — it is the set-level form of the [[Def - Lp Spaces|density]] of continuous functions in $L^p$, and of the approximation of measurable functions by simple ones.

---

# Sources and Targets

**Sources.** The hypothesis is just "$A$ Borel" (or Lebesgue-measurable). The theorem is really a property of the *construction*: it holds for any measure built from a $\sigma$-finite pre-measure on an algebra (Proposition 1.22), because the outer measure is by definition an infimum over algebra-covers, and an algebra-cover can be fattened to an open set. So the genuine source is "$\mu$ comes from the [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]] with a $\sigma$-finite, topologically-compatible pre-measure" — which includes Lebesgue and every Lebesgue–Stieltjes measure.

**Targets.** Regularity feeds: (i) **approximation of sets by elementary figures** — every Borel set is, up to $\varepsilon$, a finite union of boxes (used to prove [[Thm - Translation Invariance of Lebesgue Measure|translation invariance]] and [[Def - Lp Spaces|density of continuous functions]]); (ii) **inner regularity by compacts**, which combined with [[Def - Almost Everywhere|a.e. convergence]] gives [[Thm - Egorov's Theorem|Egorov]] and [[Thm - Lusin's Theorem|Lusin]]'s theorems; (iii) the structural fact that every Lebesgue set is a $G_\delta$ minus a null set, and an $F_\sigma$ plus a null set.

---

# Formal Statement

Let $A\in\mathcal{B}(\mathbb{R}^n)$ (or $A$ Lebesgue-measurable).

1. **(Outer regularity)** $\displaystyle\lambda(A)=\inf\{\lambda(G):G\supseteq A,\ G\text{ open}\}$.
2. **(Approximation)** For every $\varepsilon>0$ there is an open $G\supseteq A$ with $\lambda(G\setminus A)<\varepsilon$, and a closed $F\subseteq A$ with $\lambda(A\setminus F)<\varepsilon$; hence $F\subseteq A\subseteq G$ with $\lambda(G\setminus F)<\varepsilon$.
3. **(Inner regularity)** $\displaystyle\lambda(A)=\sup\{\lambda(K):K\subseteq A,\ K\text{ compact}\}$.
4. **(Structure)** $A=B\setminus N$ with $B$ a $G_\delta$ and $N$ null; also $A=C\sqcup M$ with $C$ an $F_\sigma$ and $M$ null.

---

# Why Is It True

The whole theorem is the single fact that **$\lambda$ was *defined* by covering from outside**. The [[Def - Outer Measure|outer measure]] is $\lambda(A)=\inf\{\sum\widetilde\lambda(I_j):A\subseteq\bigcup I_j\}$ — an infimum over countable covers by boxes. So for any $\varepsilon$ there is a cover $\bigcup I_j$ with total volume within $\varepsilon$ of $\lambda(A)$. Each box $I_j$ can be enlarged to a slightly bigger *open* box $I_j^\varepsilon$ costing only $\varepsilon 2^{-j}$ extra. Then $G=\bigcup I_j^\varepsilon$ is **open**, contains $A$, and has $\lambda(G)\le\lambda(A)+2\varepsilon$. That is outer regularity, and it is nothing but "the definition of $\lambda$, with the covering boxes nudged open." Outer regularity is not a theorem *about* Lebesgue measure so much as a *restatement* of how it was built.

Inner regularity is outer regularity applied to the **complement**, then complemented back. Approximate $A^c$ from outside by an open $\widetilde G$; then $F=\widetilde G^c$ is *closed*, sits inside $A$, and $\lambda(A\setminus F)=\lambda(\widetilde G\setminus A^c)<\varepsilon$. To upgrade "closed" to "compact" intersect with a large ball $[-L,L]^n$ — for $\sigma$-finite $\lambda$ the lost mass vanishes as $L\to\infty$ by [[Thm - Properties of Measures|continuity from below]].

The structure statement (4) is approximation iterated: take $G_k\supseteq A$ open with $\lambda(G_k\setminus A)<\tfrac1k$; then $B=\bigcap_k G_k$ is a $G_\delta$, contains $A$, and $\lambda(B\setminus A)=0$, so $A=B\setminus N$ with $N$ null. The complementary statement is the same on $A^c$.

---

# What Makes This Hard

Conceptually it is *easy* once you see that outer regularity is just the definition of $\lambda$ re-read — the common mistake is to look for a deep argument where there is only an "enlarge each covering box by $\varepsilon 2^{-j}$." The one genuine technical point is the upgrade from *closed* to *compact* in inner regularity: it requires $\sigma$-finiteness (intersecting with $[-L,L]^n$ and letting $L\to\infty$), and fails for non-$\sigma$-finite measures. The other place to be careful: outer regularity holds for *every* set if one writes $\lambda^*$ on the left, but the squeeze $F\subseteq A\subseteq G$ with small $\lambda(G\setminus F)$ characterises *measurability* — it is exactly the dividing line a [[Thm - Existence of a Non-Measurable Set|Vitali set]] fails.

---

# Rederivation Scaffold

**High-level strategy.** Outer regularity = unwind the definition of $\lambda$ as an inf over box-covers, nudging boxes open. Inner regularity = outer regularity on the complement. Structure = intersect/union a sequence of approximants.

**Subgoal decomposition.**

1. **Outer regularity.** Near-optimal box cover of $A$; enlarge box $I_j$ to open $I_j^\varepsilon$ with $\lambda(I_j^\varepsilon)\le\lambda(I_j)+\varepsilon 2^{-j}$; $G=\bigcup I_j^\varepsilon$.
   - *Hint:* this is just the definition of the outer measure.
2. **Inner regularity (closed).** Apply step 1 to $A^c$; complement the open superset to a closed subset.
3. **Compact upgrade.** Intersect the closed $F$ with $[-L,L]^n$; $\sigma$-finiteness $\Rightarrow$ $\lambda(A\setminus(F\cap[-L,L]^n))\to\lambda(A\setminus F)$ as $L\to\infty$.
4. **Structure.** $B=\bigcap_k G_k$ for $G_k\supseteq A$ open with $\lambda(G_k\setminus A)<1/k$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Outer regularity
> **Statement:** $\lambda(A)=\inf\{\lambda(G):G\supseteq A\text{ open}\}$, and for each $\varepsilon$ there is open $G\supseteq A$ with $\lambda(G\setminus A)<\varepsilon$.
>
> **Hint:** Cover $A$ near-optimally by boxes; open each box up by $\varepsilon 2^{-j}$.
>
> > [!note]- Full proof
> > "$\le$" is monotonicity. "$\ge$": given $\varepsilon>0$, by definition of $\lambda=\lambda^*$ choose boxes $I_j$ with $A\subseteq\bigcup_j I_j$ and $\sum_j\widetilde\lambda(I_j)\le\lambda(A)+\varepsilon$. For each $j$ pick an open box $I_j^\varepsilon\supseteq I_j$ with $\widetilde\lambda(I_j^\varepsilon)\le\widetilde\lambda(I_j)+\varepsilon 2^{-j}$. Then $G=\bigcup_j I_j^\varepsilon$ is open, $A\subseteq G$, and $\lambda(G)\le\sum_j\widetilde\lambda(I_j^\varepsilon)\le\lambda(A)+2\varepsilon$. Since $\lambda(A)\le\lambda(G)$ and (when $\lambda(A)<\infty$) $\lambda(G\setminus A)=\lambda(G)-\lambda(A)\le 2\varepsilon$, both claims follow; the infinite-measure case is handled by $\sigma$-finite truncation. $\square$

> [!note]- Lemma 2: Inner regularity by closed, then compact, sets
> **Statement:** For each $\varepsilon$ there is closed $F\subseteq A$ with $\lambda(A\setminus F)<\varepsilon$; $F$ may be taken compact.
>
> **Hint:** Apply Lemma 1 to $A^c$; then intersect with a large ball.
>
> > [!note]- Full proof
> > Apply Lemma 1 to $A^c$ (Borel): there is open $\widetilde G\supseteq A^c$ with $\lambda(\widetilde G\setminus A^c)<\varepsilon$. Set $F=\widetilde G^c$, closed, $F\subseteq A$, and $A\setminus F=A\cap\widetilde G=\widetilde G\setminus A^c$, so $\lambda(A\setminus F)<\varepsilon$. Now $F\cap[-L,L]^n$ is compact, increases to $F$ as $L\to\infty$, so by continuity from below $\lambda(F\cap[-L,L]^n)\uparrow\lambda(F)$; pick $L$ with $\lambda(F\setminus[-L,L]^n)<\varepsilon$. $\square$

> [!note]- Lemma 3: $G_\delta$/$F_\sigma$ structure
> **Statement:** $A=B\setminus N$, $B$ a $G_\delta$, $N$ null; $A=C\sqcup M$, $C$ an $F_\sigma$, $M$ null.
>
> > [!note]- Full proof
> > By Lemma 1 take open $G_k\supseteq A$ with $\lambda(G_k\setminus A)<1/k$. Then $B=\bigcap_k G_k$ is a $G_\delta$, $A\subseteq B$, and $\lambda(B\setminus A)\le\lambda(G_k\setminus A)<1/k$ for all $k$, so $N=B\setminus A$ is null. The $F_\sigma$ statement is the same applied to $A^c$ and complemented. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 is (1) and the outer half of (2); Lemma 2 is the inner half of (2) and statement (3); together $F\subseteq A\subseteq G$, $\lambda(G\setminus F)=\lambda(G\setminus A)+\lambda(A\setminus F)<2\varepsilon$. Lemma 3 is (4). $\blacksquare$

---

# Cross-Field Exercise Suggestions

Regularity, applied to *measurable functions*, gives [[Thm - Lusin's Theorem|Lusin's theorem]] (a measurable function is continuous off a small set — split the function by [[Def - Simple Function|simple approximants]] and approximate the level sets by compacts) and underlies the density of $C_c(\mathbb{R}^n)$ in $L^p$. In probability, regularity of a law $\mu$ on $\mathbb{R}$ — every law is *tight*, $\mu(K)>1-\varepsilon$ for some compact $K$ — is the single-measure precursor of [[Thm - Prokhorov's Theorem|Prokhorov's theorem]] and the definition of [[Def - Tightness|tightness]].

---

# Bridges

- **[[Thm - Translation Invariance of Lebesgue Measure]]** — proved by reducing arbitrary sets to open sets to boxes, exactly the approximation regularity provides.
- **[[Thm - Lusin's Theorem]]**, **[[Thm - Egorov's Theorem]]** — inner regularity by compacts is the engine of both.
- **[[Def - Tightness]]** *(Advanced Probability)* — regularity says every finite Borel measure on $\mathbb{R}^n$ is *inner regular by compacts*, i.e. tight.
