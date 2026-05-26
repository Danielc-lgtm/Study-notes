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

**Sources (Input Broadening)**

The literal hypothesis is "$\alpha$ a signed measure on $(X,\mathcal{A})$." But in practice one almost never encounters an object already labelled as a signed measure — one encounters arithmetic combinations and integrals of mixed-sign integrands, and the recognition that these *are* signed measures is the source skill.

The first source is **any difference $\mu-\nu$ of two finite positive measures on the same space**. By construction this is a signed measure, but it is *not* already written in mutually singular form: the parts $\mu$ and $\nu$ can overlap, share mass, agree on chunks of $X$. The bridge is that Jordan re-expresses the same object as a *canonical* difference $\alpha^+-\alpha^-$ with the two parts forced apart onto disjoint sets. A concrete problem: in statistical hypothesis testing, the difference $\mathbb{P}-\mathbb{Q}$ of two competing distributions is a signed measure, and the [[Thm - Neyman-Pearson Lemma|Neyman-Pearson test region]] is precisely the Hahn-positive set of $\mathbb{P}-\mathbb{Q}$ — the set on which the likelihood ratio favours $\mathbb{P}$.

The second source is **any "charge" $\alpha(A)=\int_A f\,d\mu$ where $f$ takes both signs and lies in $L^1(\mu)$**. This is the prototype: $\alpha$ is signed because $f$ is, and Hahn-Jordan applied to $\alpha$ reproduces the splitting $f=f^+-f^-$ at the level of measures, with positive set $\{f\ge0\}$ and $\alpha^\pm(A)=\int_A f^\pm\,d\mu$. The example: in spectral theory one studies projection-valued measures, and for a self-adjoint operator $T=\int\lambda\,dE_\lambda$, the operator $T$ itself decomposes via the Hahn decomposition of $\lambda\mapsto\lambda$ into positive and negative parts $T^+,T^-$ — the functional calculus reads off from Jordan.

The third source is **a finite-energy or signed-mass difference in physics or economics**. Consider two charge distributions $\rho_+(x),\rho_-(x)$ on $\mathbb{R}^3$ representing positive and negative ions; the net charge density $\rho=\rho_+-\rho_-$ is a signed measure, and Hahn-Jordan identifies the spatial regions of net positive and net negative charge. The same structure appears in economics as net flow: cash inflows minus outflows define a signed measure on time intervals, and the Hahn decomposition isolates the surplus and deficit periods. Recognising "I have two positive flows competing" as a signed measure unlocks the decomposition.

**Targets (Output Amplification)**

The conclusion is "$\alpha=\alpha^+-\alpha^-$ with $\alpha^+\perp\alpha^-$, unique." This minimal statement combines with three other tools to produce structures that the bare decomposition does not hint at.

The first combination is **Jordan together with [[Thm - Radon-Nikodym Theorem|Radon-Nikodym]]**. Each part $\alpha^\pm$ is a positive measure, and if $\alpha\ll\mu$ for some reference $\mu$, then $\alpha^\pm\ll\mu$ as well, so each has a density $f^\pm=d\alpha^\pm/d\mu\ge0$. The amplified result: $\alpha$ itself has a *signed* density $f=f^+-f^-\in L^1(\mu)$, and $\alpha(A)=\int_A f\,d\mu$. The combination is non-obvious because Radon-Nikodym is usually stated for positive measures only; Jordan is precisely the bridge that extends it to the signed case, and without Jordan there is no notion of "density of a signed measure."

The second combination is **Jordan together with the total variation norm**. Define $\|\alpha\|_{TV}=|\alpha|(X)=\alpha^+(X)+\alpha^-(X)$. The amplified result: the space $\mathcal{M}(X)$ of finite signed measures, equipped with $\|\cdot\|_{TV}$, is a **Banach space**. This is non-obvious because the construction of the norm itself depends on the Jordan decomposition — one cannot define $|\alpha|$ without first splitting $\alpha$ into mutually singular pieces. Completeness then makes $\mathcal{M}(X)$ a venue for functional-analytic methods on measures: weak convergence, compactness via [[Thm - Prokhorov's Theorem|Prokhorov]], and operator theory on measure spaces all live downstream of this Banach structure.

The third combination is **Hahn together with the [[Thm - Riesz Representation Theorem|Riesz representation theorem]]**. For compact Hausdorff $K$, Riesz identifies $C(K)^*$ with $\mathcal{M}(K)$ — every continuous linear functional on $C(K)$ is integration against a signed Radon measure. The amplified result: the *positive* and *negative* parts of a functional $\Lambda\in C(K)^*$ are exactly the integrals against $\alpha^\pm$, and the Hahn decomposition geometrically separates the support of "where $\Lambda$ acts positively" from "where $\Lambda$ acts negatively." This is the duality between $C(K)$ and signed measures, and it gives the structural picture of $C(K)^*$ as a Banach lattice — a non-obvious consequence of pairing an analytic theorem (Riesz) with a measure-theoretic one (Hahn).

---

# Statement

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
