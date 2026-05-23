---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Lebesgue Measure"
  - "Thm - Translation Invariance of Lebesgue Measure"
  - "Def - Borel σ-Algebra"
tags: [analysis, measure-theory]
---

# Notation

$\lambda$ is [[Def - Lebesgue Measure|Lebesgue measure]] on $\mathbb{R}$, $\mathcal{B}^*(\mathbb{R})$ the Lebesgue $\sigma$-algebra. $V\subseteq(0,1]$ denotes a **Vitali set**. $q+V=\{q+v:v\in V\}$.

---

# Motivation

We have built a measure $\lambda$ on the Borel (and Lebesgue) sets. The natural greedy wish is to define $\lambda$ on *all* subsets of $\mathbb{R}$ — why stop at the Borel sets? This theorem says the wish is *impossible*: there is no way to extend $\lambda$ to all of $2^{\mathbb{R}}$ while keeping countable additivity and translation invariance. Some sets are genuinely non-measurable.

This is not a curiosity. It explains *why measure theory is built the way it is* — why one cannot skip the $\sigma$-algebra and just measure everything, why the Borel/Lebesgue $\sigma$-algebra is a real restriction and not a technicality. It is the negative theorem that justifies the entire apparatus of $\sigma$-algebras. It also exposes the exact tension: three innocuous demands — countable additivity, translation invariance, and "every set has a size" — are *jointly inconsistent*. Something must go, and what goes is "every set has a size."

The construction uses the **axiom of choice** essentially: in Solovay's model of ZF (without choice) every set of reals *is* Lebesgue-measurable. Non-measurability is the price of choice.

---

# Sources and Targets

**Sources.** The proof needs three ingredients, and recognising them is recognising when a non-measurability argument is available: (i) a group acting by [[Thm - Translation Invariance of Lebesgue Measure|measure-preserving translations]] — here $(\mathbb{Q},+)$ acting on $\mathbb{R}$; (ii) the action having a *bounded fundamental domain* (a set of coset representatives inside $(0,1]$); (iii) the orbit being *countable and dense*. Any countable dense subgroup of $\mathbb{R}$ works in place of $\mathbb{Q}$.

**Targets.** The conclusion "$V\notin\mathcal{B}^*(\mathbb{R})$" yields: (i) $\mathcal{B}^*(\mathbb{R})\subsetneq 2^{\mathbb{R}}$ — Lebesgue measure is *not* defined on all sets; (ii) $\lambda^*$ (the outer measure) is **not countably additive** on $2^{\mathbb{R}}$ — it must be cut down to $\mathcal{B}^*$ to become a measure, retroactively justifying the [[Def - Carathéodory Measurable Sets|Carathéodory restriction]]; (iii) by scaling, non-measurable sets of every positive outer measure exist.

---

# Statement

There exists a set $V\subseteq(0,1]$ that is **not Lebesgue-measurable**: $V\notin\mathcal{B}^*(\mathbb{R})$. Consequently $\mathcal{B}^*(\mathbb{R})\neq 2^{\mathbb{R}}$, and there is no countably additive, translation-invariant extension of $\lambda$ to all of $2^{\mathbb{R}}$.

---

# Why Is It True

The intuition is a *counting paradox forced by symmetry*. Define $x\sim y$ iff $x-y\in\mathbb{Q}$. This partitions $\mathbb{R}$ into countably-infinite [[Def - Coset|cosets]], each dense. By the axiom of choice, pick one representative from each coset lying in $(0,1]$; collect them into $V$.

Now look at the rational translates $q+V$ for $q\in\mathbb{Q}\cap(-1,1]$. Two facts hold by *construction*: (a) distinct rationals give *disjoint* translates — if $q_1+V$ and $q_2+V$ met, two representatives would differ by a rational, so lie in the same coset, contradicting "one representative per coset"; (b) these translates *sandwich* the unit interval: $(0,1]\subseteq\bigsqcup_{q}(q+V)\subseteq(-1,2]$, because every point of $(0,1]$ is a rational shift of its representative.

Suppose now $V$ *were* measurable, with $\lambda(V)=c$. [[Thm - Translation Invariance of Lebesgue Measure|Translation invariance]] forces every translate to have the *same* measure $c$. Countable additivity over the disjoint union then gives
$$\lambda\Big(\bigsqcup_q(q+V)\Big)=\sum_{q}c=\begin{cases}0,&c=0\\\infty,&c>0.\end{cases}$$
But the sandwich (b) forces this total to lie in $[\,\lambda((0,1]),\,\lambda((-1,2])\,]=[1,3]$. A countably-infinite sum of a *single constant* $c$ is only ever $0$ or $\infty$ — it can never land in $[1,3]$. Contradiction. So $V$ is not measurable.

The whole argument is the clash: **translation invariance makes all translates equal**, **countable additivity makes their total a sum of equal terms** (hence $0$ or $\infty$), and **the geometry traps that total strictly between $1$ and $3$**. No measure can satisfy all three. The deep point: the size $c$ has nowhere to go — if $c=0$ the unit interval is null, if $c>0$ a bounded set has infinite measure.

---

# What Makes This Hard

The argument is short; the difficulty is *believing* each construction-fact and seeing *which axiom each contradiction-step uses*. The two facts to internalise: distinct translates are disjoint (uses "one representative per coset" — the axiom of choice), and the translates sandwich $(0,1]$ (uses density of $\mathbb{Q}$). The killer step is recognising that $\sum_{q\in\mathbb{Q}}c$ is a sum of *infinitely many equal terms*, hence $\in\{0,\infty\}$ — students often try to assign $c$ a clever value, missing that *no* value works. The role of the axiom of choice is the subtle part: it is *needed*, not laziness — without it (Solovay) no such $V$ exists.

---

# Rederivation Scaffold

**High-level strategy.** Build $V$ by choosing one representative per $\mathbb{Q}$-coset in $(0,1]$. Show its rational translates are disjoint (choice) and sandwich $(0,1]$ (density). Assume $V$ measurable and derive that a sum of a constant lands in $[1,3]$ — impossible.

**Subgoal decomposition.**

1. **Construct $V$.** Equivalence $x\sim y\iff x-y\in\mathbb{Q}$; axiom of choice picks one $v\in(0,1]$ per class.
2. **Disjointness.** For $q_1\neq q_2$ in $\mathbb{Q}$, $(q_1+V)\cap(q_2+V)=\emptyset$.
   - *Hint:* a common point yields two representatives in one class.
3. **Sandwich.** $(0,1]\subseteq\bigsqcup_{q\in\mathbb{Q}\cap(-1,1]}(q+V)\subseteq(-1,2]$.
   - *Hint:* every $y\in(0,1]$ equals $q+v$ for its representative $v$ and some $q\in(-1,1]$.
4. **Contradiction.** If $\lambda(V)=c$ exists: translation invariance $\Rightarrow$ each translate has measure $c$; $\sigma$-additivity $\Rightarrow$ total $=\sum c\in\{0,\infty\}$; sandwich $\Rightarrow$ total $\in[1,3]$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Disjointness of rational translates
> **Statement:** For $q_1,q_2\in\mathbb{Q}$, $q_1\neq q_2$: $(q_1+V)\cap(q_2+V)=\emptyset$.
>
> **Hint:** A shared point gives two representatives in the same $\sim$-class.
>
> > [!note]- Full proof
> > Suppose $x\in(q_1+V)\cap(q_2+V)$, so $x=q_1+v_1=q_2+v_2$ with $v_1,v_2\in V$. Then $v_1-v_2=q_2-q_1\in\mathbb{Q}$, so $v_1\sim v_2$. But $V$ contains exactly one representative per $\sim$-class, forcing $v_1=v_2$, hence $q_1=q_2$ — contradiction. $\square$

> [!note]- Lemma 2: The translates sandwich the unit interval
> **Statement:** With $A=\mathbb{Q}\cap(-1,1]$, $\ (0,1]\subseteq\bigcup_{q\in A}(q+V)\subseteq(-1,2]$.
>
> **Hint:** Density of $\mathbb{Q}$; representatives lie in $(0,1]$.
>
> > [!note]- Full proof
> > Right inclusion: $q\in(-1,1]$ and $V\subseteq(0,1]$ give $q+V\subseteq(-1,2]$. Left inclusion: take $y\in(0,1]$; let $v\in V$ be the representative of $y$'s class, so $q:=y-v\in\mathbb{Q}$. Since $y,v\in(0,1]$, $q\in(-1,1]$, so $q\in A$ and $y=q+v\in q+V$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Construct $V$ by the axiom of choice as one representative in $(0,1]$ of each class of $x\sim y\iff x-y\in\mathbb{Q}$. Suppose for contradiction $V\in\mathcal{B}^*(\mathbb{R})$, $\lambda(V)=c\in[0,\infty]$. By Lemma 1 the sets $\{q+V:q\in A\}$, $A=\mathbb{Q}\cap(-1,1]$, are pairwise disjoint and (Lemma 2) satisfy $(0,1]\subseteq\bigsqcup_{q\in A}(q+V)\subseteq(-1,2]$. By monotonicity, $1=\lambda((0,1])\le\lambda\big(\bigsqcup_{q\in A}(q+V)\big)\le\lambda((-1,2])=3$. By $\sigma$-additivity and [[Thm - Translation Invariance of Lebesgue Measure|translation invariance]], $\lambda\big(\bigsqcup_{q\in A}(q+V)\big)=\sum_{q\in A}\lambda(q+V)=\sum_{q\in A}c$. Since $A$ is countably infinite, this sum is $0$ if $c=0$ and $\infty$ if $c>0$ — never in $[1,3]$. Contradiction; hence $V\notin\mathcal{B}^*(\mathbb{R})$. In particular $\mathcal{B}^*(\mathbb{R})\subsetneq 2^{\mathbb{R}}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The same "symmetry $+$ countable additivity $\Rightarrow$ paradox" template, pushed harder, yields the **Banach–Tarski paradox** in $\mathbb{R}^3$ (where the symmetry [[Def - Group|group]] is the non-amenable $SO(3)$, so even *finite* additivity fails). The contrast is instructive: $\mathbb{R}/\mathbb{Z}$ is *amenable*, so a finitely-additive invariant mean *does* exist there — it is only *countable* additivity that Vitali kills. In probability, the lesson is structural: a "uniform distribution on a countable group" cannot exist, which is why [[Def - Probability Space|probability spaces]] insist on a $\sigma$-algebra and forbid measuring every event.

---

# Bridges

- **[[Thm - Translation Invariance of Lebesgue Measure]]** — the property exploited; without it the translates need not have equal measure and the paradox dissolves.
- **[[Def - Carathéodory Measurable Sets]]** — this theorem is the *reason* one restricts to $\Sigma$: the outer measure $\lambda^*$ genuinely fails additivity on the Vitali set.
- **[[Def - Borel σ-Algebra]]** — establishes the strict chain $\mathcal{B}(\mathbb{R})\subsetneq\mathcal{B}^*(\mathbb{R})\subsetneq 2^{\mathbb{R}}$.
