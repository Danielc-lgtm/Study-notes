---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Signed Measure"
  - "Def - Mutual Singularity"
tags: [analysis, measure-theory]
---

# Notation

$(X,\mathcal{A})$ a measurable space; $\alpha$ a [[Def - Signed Measure|signed measure]]. *Positive* / *negative* sets as in the definition of a signed measure.

---

# Motivation

A [[Def - Signed Measure|signed measure]] mixes positive and negative "charge." The Hahn decomposition theorem says the mixing is only apparent: the space splits *cleanly* into a region of pure positive charge and a region of pure negative charge. The Jordan decomposition is the equivalent statement at the level of measures — $\alpha=\alpha^+-\alpha^-$, a difference of two genuine, mutually [[Def - Mutual Singularity|singular]], positive measures. Together they say: **every signed measure is a difference of two positive measures living on disjoint sets.** This is the structural foundation on which [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] is built, and it makes the space of signed measures a vector space with a norm (total variation $|\alpha|=\alpha^++\alpha^-$).

---

# Sources and Targets

**Sources.** Hypothesis: $\alpha$ a signed measure (taking at most one infinite value). The prototype to keep in mind: $\alpha(A)=\int_A f\,d\mu$, where the positive set is $\{f\ge0\}$.

**Targets.** The decomposition yields: the **total variation measure** $|\alpha|=\alpha^++\alpha^-$ and the total-variation *norm* $\|\alpha\|=|\alpha|(X)$, making signed measures a Banach space; the reduction of any signed-measure question to two positive-measure questions; and the structural input to [[Thm - Radon-Nikodym Theorem|Lebesgue decomposition]] (which is proved for signed $\nu$ by Jordan-decomposing first).

---

# Formal Statement

**(Hahn decomposition.)** For any signed measure $\alpha$ on $(X,\mathcal{A})$ there exist a [[Def - Signed Measure|positive set]] $P$ and a negative set $N$ with $X=P\sqcup N$. The decomposition is unique up to $\alpha$-null sets: if $(P',N')$ is another, then $\alpha(P\,\triangle\,P')=0$.

**(Jordan decomposition.)** There is a *unique* pair of mutually [[Def - Mutual Singularity|singular]] positive measures $\alpha^+,\alpha^-$ with
$$\alpha=\alpha^+-\alpha^-,\qquad\alpha^+\perp\alpha^-.$$
Explicitly $\alpha^+(E)=\alpha(E\cap P)$, $\alpha^-(E)=-\alpha(E\cap N)$. The measure $|\alpha|=\alpha^++\alpha^-$ is the **total variation**.

---

# Why Is It True

**Hahn.** The idea: find the "most negative possible" set and call its complement positive.

Consider $b=\inf\{\alpha(B):B\text{ a negative set}\}$ (the infimum is over $[-\infty,0]$, attained in the limit). Take negative sets $B_n$ with $\alpha(B_n)\to b$; their union $N=\bigcup B_n$ is *also negative* (a countable union of negative sets is negative — disjointify and use $\sigma$-additivity), and $\alpha(N)=b$ (it is $\le b$ by being a negative superset of each $B_n$, and $\ge b$ by definition of the infimum). So $N$ is a *maximally negative* set, and $b>-\infty$.

Claim: $P=N^c$ is positive. If not, $P$ contains a subset $A_0$ with $\alpha(A_0)<0$. The key lemma — *every set of negative measure contains a negative subset of negative measure* — then produces a negative $A_0'\subseteq P$ with $\alpha(A_0')<0$. But then $N\sqcup A_0'$ is a negative set with $\alpha(N\sqcup A_0')=b+\alpha(A_0')<b$, contradicting the minimality of $b$. So $P$ is positive.

The slogan: **push all the negative charge into one maximally-negative set $N$; its complement, having no negative charge left to give, is positive.** The minimality of $b$ is the lever.

**Jordan.** Given Hahn's $(P,N)$, define $\alpha^+(E)=\alpha(E\cap P)\ge0$ (a measure, since $P$ is positive) and $\alpha^-(E)=-\alpha(E\cap N)\ge0$. Then $\alpha^+-\alpha^-=\alpha(\cdot\cap P)+\alpha(\cdot\cap N)=\alpha$, and $\alpha^+\perp\alpha^-$ because $\alpha^+(N)=0=\alpha^-(P)$ — they live on the disjoint sets $P,N$. Uniqueness: any singular splitting $\alpha=\beta^+-\beta^-$, $\beta^+\perp\beta^-$, forces a Hahn decomposition (the set carrying $\beta^+$), which by Hahn's uniqueness agrees with $(P,N)$ up to $\alpha$-null sets, hence $\beta^\pm=\alpha^\pm$.

---

# What Makes This Hard

The proof of Hahn has one genuinely subtle ingredient: the lemma "**a set of negative measure contains a *negative* subset of negative measure**." A set with $\alpha<0$ might have positive-measure subsets; one must *remove the positive chunks* — and removing them is itself an inductive, $\varepsilon$-budgeted construction (peel off subsets that spoil negativity, controlling their total). Without this lemma the contradiction in the main argument cannot be sprung. The second subtle point is recognising that "$\inf$ over negative sets is *attained*" — that the union of an optimising sequence of negative sets is again negative — which needs the closure of negative sets under countable union.

---

# Rederivation Scaffold

**High-level strategy.** Hahn: take $N$ minimising $\alpha$ over negative sets; show $N^c$ is positive by contradiction with minimality, using the negative-subset lemma. Jordan: read $\alpha^\pm$ off $(P,N)$.

**Subgoal decomposition.**

1. **Negative sets are closed under countable union.** Disjointify, use $\sigma$-additivity.
2. **Negative-subset lemma.** Any $B$ with $\alpha(B)<0$ contains a negative $B'$ with $\alpha(B')\le\alpha(B)<0$ (peel off positive chunks with an $\varepsilon$-budget).
3. **Maximally negative set.** $b=\inf\{\alpha(B):B\text{ negative}\}$ is attained by $N=\bigcup B_n$; $b>-\infty$.
4. **$N^c$ is positive.** Else extract a negative subset of negative measure, contradict minimality of $b$.
5. **Jordan.** $\alpha^+=\alpha(\cdot\cap P)$, $\alpha^-=-\alpha(\cdot\cap N)$; mutually singular; uniqueness via Hahn-uniqueness.

---

# Lemma Decomposition

> [!note]- Lemma 1: Negative subsets of negative-measure sets
> **Statement:** If $\alpha(B)<0$, there is a negative set $B'\subseteq B$ with $\alpha(B')\le\alpha(B)$.
>
> **Hint:** Repeatedly remove subsets that carry positive measure, budgeting their sizes.
>
> > [!note]- Full proof
> > Inductively let $\varepsilon_n=\sup\{\alpha(A):A\subseteq B\setminus\bigcup_{k<n}A_k\}\ge0$ and pick $A_n$ in that range with $\alpha(A_n)\ge\min(\varepsilon_n/2,1)$. Set $B'=B\setminus\bigcup_n A_n$. The $A_n$ are disjoint, $\alpha(A_n)\ge0$, so $\alpha(B')=\alpha(B)-\sum_n\alpha(A_n)\le\alpha(B)<0$; finiteness of $\alpha(B')$ forces $\sum\alpha(A_n)<\infty$, hence $\varepsilon_n\to0$. Any $A\subseteq B'$ has $\alpha(A)\le\varepsilon_n\to0$, so $\alpha(A)\le0$ — $B'$ is negative. $\square$

> [!note]- Lemma 2: A maximally negative set exists
> **Statement:** $b=\inf\{\alpha(B):B\text{ negative}\}$ is attained by a negative set $N$, and $b>-\infty$.
>
> > [!note]- Full proof
> > Negative sets are closed under countable union (disjointify; $\sigma$-additivity of $\alpha$ over negative pieces keeps the sum $\le0$ on every subset). Take negative $B_n$ with $\alpha(B_n)\to b$; $N=\bigcup_n B_n$ is negative, $\alpha(N)\le\alpha(B_n)$ for each $n$ (as $B_n\subseteq N$, $N\setminus B_n$ negative), so $\alpha(N)\le b$; and $\alpha(N)\ge b$ by definition of $b$. Thus $\alpha(N)=b$; $b>-\infty$ since $\alpha$ omits $-\infty$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 2 take a negative $N$ with $\alpha(N)=b=\inf$. Set $P=N^c$. If $P$ were not positive, some $A_0\subseteq P$ has $\alpha(A_0)<0$; by Lemma 1, $A_0$ contains a negative $A_0'$ with $\alpha(A_0')<0$. Then $N\cup A_0'$ is negative ($N,A_0'$ disjoint negative sets) with $\alpha(N\cup A_0')=b+\alpha(A_0')<b$ — contradicting minimality. So $P$ is positive and $X=P\sqcup N$ is a Hahn decomposition. Uniqueness up to $\alpha$-null sets: for two decompositions, $P\triangle P'$ is contained both in a positive and in a negative set, hence $\alpha$-null. Jordan: $\alpha^+(E)=\alpha(E\cap P)$, $\alpha^-(E)=-\alpha(E\cap N)$ are positive measures with $\alpha=\alpha^+-\alpha^-$, $\alpha^+(N)=\alpha^-(P)=0$ so $\alpha^+\perp\alpha^-$; uniqueness follows from Hahn-uniqueness. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The Jordan decomposition makes the **space of finite signed measures a Banach space** under $\|\alpha\|=|\alpha|(X)$ — and the Riesz representation theorem identifies it with $C(X)^*$, the dual of continuous functions. In probability, decomposing $\mathbb{P}-\mathbb{Q}$ for two laws $\mathbb{P},\mathbb{Q}$ gives the **total variation distance** $\|\mathbb{P}-\mathbb{Q}\|_{TV}=\tfrac12|\mathbb{P}-\mathbb{Q}|(X)=\sup_A|\mathbb{P}(A)-\mathbb{Q}(A)|$, the basic metric on distributions.

---

# Bridges

- **[[Thm - Radon-Nikodym Theorem]]** — to decompose a *signed* $\nu$, Jordan-decompose first and treat $\nu^+,\nu^-$ separately.
- **[[Def - Mutual Singularity]]** — $\alpha^+\perp\alpha^-$ is the canonical example of mutual singularity.
- **[[Def - Signed Measure]]** — this theorem is the structure theorem promised there.
