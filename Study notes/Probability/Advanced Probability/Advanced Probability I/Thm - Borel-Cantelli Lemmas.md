---
type: theorem
subject: advanced-probability
prereqs:
  - "Def - Probability Space"
  - "Def - Independence"
  - "Thm - Properties of Measures"
tags: [probability, advanced-probability]
---

# Notation

$(\Omega,\mathcal{F},\mathbb{P})$ a [[Def - Probability Space|probability space]]; $(A_n)$ events. $\limsup_n A_n=\bigcap_N\bigcup_{n\ge N}A_n=\{A_n\text{ infinitely often}\}=\{A_n\text{ i.o.}\}$.

---

# Motivation

A central question about an infinite sequence of events $(A_n)$: do *infinitely many* of them occur, or only finitely many? The event "$A_n$ infinitely often" is $\limsup_n A_n$. The two Borel–Cantelli lemmas give a near-complete answer in terms of the single number $\sum_n\mathbb{P}(A_n)$: if the series **converges**, then a.s. only finitely many $A_n$ occur; if it **diverges** *and the $A_n$ are independent*, then a.s. infinitely many occur. Together they are a **zero–one law** — $\mathbb{P}(A_n\text{ i.o.})$ is $0$ or $1$ — and the standard machine for proving almost-sure statements (almost-sure convergence, the existence/non-existence of records, the [[Thm - Strong Law of Large Numbers|strong law]]).

---

# Sources and Targets

**Sources.** First lemma: hypothesis $\sum\mathbb{P}(A_n)<\infty$ — *no independence needed*. Second lemma: $\sum\mathbb{P}(A_n)=\infty$ *and* [[Def - Independence|independence]] — independence is essential (pairwise suffices, but some such hypothesis is needed). The standard *bridge into* the first lemma: to prove $X_n\to X$ a.s., set $A_n=\{|X_n-X|>\varepsilon\}$ and show $\sum\mathbb{P}(A_n)<\infty$.

**Targets.** The first lemma gives almost-sure convergence from a summable error series — the route from $L^p$ or in-probability convergence to an [[Ex - Lp convergence and almost-everywhere subsequences|a.e.-convergent subsequence]], and a step in the [[Thm - Strong Law of Large Numbers|SLLN]]. The second gives "rare independent events still happen infinitely often" — recurrence statements, the infinite-monkey theorem, the optimality of [[Thm - Kolmogorov 0-1 Law|0–1 laws]].

---

# Formal Statement

Let $(A_n)_{n\ge1}$ be events.

**(First Borel–Cantelli lemma.)** If $\displaystyle\sum_{n=1}^\infty\mathbb{P}(A_n)<\infty$, then $\mathbb{P}(\limsup_n A_n)=0$ — almost surely only finitely many $A_n$ occur.

**(Second Borel–Cantelli lemma.)** If the $(A_n)$ are [[Def - Independence|independent]] and $\displaystyle\sum_{n=1}^\infty\mathbb{P}(A_n)=\infty$, then $\mathbb{P}(\limsup_n A_n)=1$ — almost surely infinitely many $A_n$ occur.

Hence for an independent sequence, $\mathbb{P}(A_n\text{ i.o.})\in\{0,1\}$, dichotomised by convergence/divergence of $\sum\mathbb{P}(A_n)$.

---

# Why Is It True

**First lemma — $\sigma$-subadditivity and a vanishing tail.** $\limsup A_n\subseteq\bigcup_{n\ge N}A_n$ for *every* $N$. By [[Thm - Properties of Measures|$\sigma$-subadditivity]], $\mathbb{P}(\limsup A_n)\le\sum_{n\ge N}\mathbb{P}(A_n)$. Since $\sum\mathbb{P}(A_n)<\infty$, the tail $\to0$ as $N\to\infty$; the left side does not depend on $N$, so it is $0$. (Equivalently: $\mathbb{E}[\sum\mathbf{1}_{A_n}]=\sum\mathbb{P}(A_n)<\infty$, so $\sum\mathbf{1}_{A_n}<\infty$ a.s.) This is exactly the [[Ex - The first Borel-Cantelli lemma|set-level argument from measure theory]] — no probability beyond a finite measure is used.

**Second lemma — independence turns "divergent sum" into "complement is null."** Work with the complement: $(\limsup A_n)^c=\liminf A_n^c=\bigcup_N\bigcap_{n\ge N}A_n^c=\{A_n\text{ eventually never occurs}\}$. It suffices to show each $\bigcap_{n\ge N}A_n^c$ has probability $0$. By independence (of the $A_n^c$), for any $M\ge N$,
$$\mathbb{P}\Big(\bigcap_{n=N}^M A_n^c\Big)=\prod_{n=N}^M(1-\mathbb{P}(A_n))\le\prod_{n=N}^M e^{-\mathbb{P}(A_n)}=\exp\Big(-\sum_{n=N}^M\mathbb{P}(A_n)\Big),$$
using the elementary bound $1-x\le e^{-x}$. As $M\to\infty$ the exponent $\to-\infty$ (the series diverges), so $\mathbb{P}(\bigcap_{n\ge N}A_n^c)=0$. A countable union of null sets is null, so $(\limsup A_n)^c$ is null.

The contrast in mechanism: **the first lemma is "a convergent series has a small tail"; the second is "independence multiplies $(1-\mathbb{P}(A_n))$, and $1-x\le e^{-x}$ turns the divergent *sum* in the exponent into a vanishing *product*."** Independence is what converts $\mathbb{P}(\bigcap A_n^c)$ into $\prod\mathbb{P}(A_n^c)$ — without it the product rule fails and the lemma is false.

---

# What Makes This Hard

The first lemma is easy ($\sigma$-subadditivity, tail). The second has two steps people miss: (i) **pass to the complement** — "infinitely often" is awkward, "eventually never" factors; (ii) the **$1-x\le e^{-x}$ trick**, which converts a product of $(1-\mathbb{P}(A_n))$ into $\exp(-\sum\mathbb{P}(A_n))$, so that *divergence of the sum* becomes *vanishing of the product*. Forgetting that independence is *essential* to the second lemma is the classic error — the first needs none, the second cannot do without it.

---

# Rederivation Scaffold

**High-level strategy.** First: $\limsup A_n\subseteq$ every tail union, bound by the tail sum, let $N\to\infty$. Second: complement to "eventually never," factor by independence, bound the product by $\exp(-\sum)$, use divergence.

**Subgoal decomposition.**

1. **First lemma.** $\limsup A_n\subseteq\bigcup_{n\ge N}A_n$; $\mathbb{P}\le\sum_{n\ge N}\mathbb{P}(A_n)\to0$.
2. **Second, setup.** $(\limsup A_n)^c=\bigcup_N\bigcap_{n\ge N}A_n^c$; show each $\bigcap_{n\ge N}A_n^c$ is null.
3. **Factor.** Independence $\Rightarrow\mathbb{P}(\bigcap_{n=N}^M A_n^c)=\prod_{n=N}^M(1-\mathbb{P}(A_n))$.
4. **Bound and diverge.** $1-x\le e^{-x}\Rightarrow$ product $\le\exp(-\sum_{n=N}^M\mathbb{P}(A_n))\to0$ as $M\to\infty$.

---

# Lemma Decomposition

> [!note]- Lemma 1: First Borel–Cantelli
> **Statement:** $\sum\mathbb{P}(A_n)<\infty\Rightarrow\mathbb{P}(\limsup A_n)=0$.
>
> > [!note]- Full proof
> > For each $N$, $\limsup_n A_n=\bigcap_M\bigcup_{n\ge M}A_n\subseteq\bigcup_{n\ge N}A_n$, so by [[Thm - Properties of Measures|$\sigma$-subadditivity]] $\mathbb{P}(\limsup A_n)\le\sum_{n\ge N}\mathbb{P}(A_n)$. The right side is the tail of a convergent series, $\to0$ as $N\to\infty$; the left side is fixed, hence $0$. $\square$

> [!note]- Lemma 2: Second Borel–Cantelli
> **Statement:** $(A_n)$ independent, $\sum\mathbb{P}(A_n)=\infty\Rightarrow\mathbb{P}(\limsup A_n)=1$.
>
> > [!note]- Full proof
> > $(\limsup A_n)^c=\bigcup_N\bigcap_{n\ge N}A_n^c$. Fix $N$. The $A_n^c$ are independent, so for $M\ge N$, $\mathbb{P}(\bigcap_{n=N}^M A_n^c)=\prod_{n=N}^M(1-\mathbb{P}(A_n))\le\prod_{n=N}^M e^{-\mathbb{P}(A_n)}=\exp(-\sum_{n=N}^M\mathbb{P}(A_n))$. Let $M\to\infty$: the exponent $\to-\infty$, so $\mathbb{P}(\bigcap_{n\ge N}A_n^c)=0$. Then $\mathbb{P}((\limsup A_n)^c)\le\sum_N\mathbb{P}(\bigcap_{n\ge N}A_n^c)=0$, so $\mathbb{P}(\limsup A_n)=1$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 is the first lemma; Lemma 2 is the second. For an independent sequence, exactly one of $\sum\mathbb{P}(A_n)<\infty$, $=\infty$ holds, giving $\mathbb{P}(\limsup A_n)=0$ or $1$ — the zero–one dichotomy. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The first lemma is the workhorse for **almost-sure convergence**: $X_n\to X$ a.s. follows from $\sum_n\mathbb{P}(|X_n-X|>\varepsilon)<\infty$ for each $\varepsilon$ — the route used to extract an a.e.-convergent subsequence from [[Def - Convergence in Measure|convergence in probability]] and a step in the [[Thm - Strong Law of Large Numbers|strong law]]. The second lemma proves the **infinite-monkey theorem** (a fixed text eventually appears in random typing) and, for i.i.d. $X_n$ with unbounded support, that $\limsup X_n=+\infty$ a.s.

---

# Bridges

- **[[Thm - Kolmogorov 0-1 Law]]** — $\{A_n\text{ i.o.}\}$ is a tail event; the 0–1 law explains *a priori* why $\mathbb{P}(\limsup A_n)\in\{0,1\}$ for independent $A_n$, and Borel–Cantelli computes *which*.
- **[[Thm - Properties of Measures]]** — the first lemma is $\sigma$-subadditivity plus a convergent tail, pure measure theory.
- **[[Thm - Strong Law of Large Numbers]]** — Borel–Cantelli is a standard step in proving a.s. convergence.
