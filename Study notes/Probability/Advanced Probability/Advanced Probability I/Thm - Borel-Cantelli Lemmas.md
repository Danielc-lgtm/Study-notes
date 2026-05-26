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

**Sources (Input Broadening)**

The literal hypothesis is a numerical condition on $\sum_n\mathbb{P}(A_n)$, but Borel–Cantelli is deployed throughout probability whenever one wants to upgrade quantitative tail estimates to a qualitative almost-sure statement. The art is recognising that a problem about pathwise behaviour is *secretly* a problem about summability of a series of probabilities.

The first source is **almost-sure convergence of a sequence of random variables**. The problem "$X_n\to X$ a.s." rarely arrives presented as "$\mathbb{P}(\limsup A_n)=0$"; it arrives as a question about pathwise limits. The bridge: for each $\varepsilon>0$ set $A_n^\varepsilon=\{|X_n-X|>\varepsilon\}$, and observe that $X_n\to X$ a.s. iff $\mathbb{P}(A_n^\varepsilon\text{ i.o.})=0$ for every $\varepsilon$. BC1 then reduces a.s. convergence to a *summability* condition $\sum_n\mathbb{P}(|X_n-X|>\varepsilon)<\infty$, checkable by [[Def - Convergence in Measure|in-probability]] tail bounds (Markov, Chebyshev, Chernoff). The example: to show estimators with $\mathbb{E}|X_n-X|^p\le C/n^2$ converge a.s. to $X$, apply Markov to get $\mathbb{P}(|X_n-X|>\varepsilon)\le C/(\varepsilon^p n^2)$ — summable — and invoke BC1, with no extraction-of-subsequence detour.

The second source is **independent events appearing in a problem with summable or non-summable tails**. Whenever a model produces a sequence of independent or pairwise independent trials — coin flips, returns of an MCMC chain, blocks of an i.i.d. sample — questions like "does this rare event keep recurring forever?" are exactly questions about $\{A_n\text{ i.o.}\}$. The bridge is that *for independent events*, the dichotomy $\sum\mathbb{P}(A_n)<\infty$ vs. $=\infty$ already settles $\mathbb{P}(\limsup A_n)\in\{0,1\}$: BC2 promotes "probability summed to infinity" into "happens infinitely often a.s." The example: in i.i.d. fair coin tosses, the event $A_n=\{n\text{ consecutive heads start at time }n^2\}$ has $\mathbb{P}(A_n)=2^{-n}$, summable, so by BC1 only finitely many occur; whereas $B_n=\{\text{head at time }n\}$ has $\sum\mathbb{P}(B_n)=\infty$, so BC2 gives infinitely many heads a.s.

The third source is **a hierarchy of intersections or unions of events whose probabilities can be bounded by independence-based product or union bound**. Often the events of interest are built as $C_n=\bigcap_{k\in I_n}D_{n,k}$ or $C_n=\bigcup_{k\in I_n}D_{n,k}$, with $|I_n|$ growing and $\mathbb{P}(D_{n,k})$ decaying. The bridge: bound $\mathbb{P}(C_n)$ by independence (product) or [[Thm - Properties of Measures|σ-subadditivity]] (sum), check summability, apply BC1. The example: to show that an Erdős–Rényi graph $G(n,p)$ with $p=c\log n/n$, $c>1$, has no isolated vertex for all large $n$ a.s., let $C_n=\{G(n,p)\text{ has an isolated vertex}\}$ and bound $\mathbb{P}(C_n)\le n(1-p)^{n-1}\le n e^{-pn}=n^{1-c}$ — summable for $c>1$ — and BC1 delivers the conclusion.

**Targets (Output Amplification)**

The conclusion is $\mathbb{P}(\limsup A_n)\in\{0,1\}$ depending on the dichotomy. Each amplification turns this single zero/one verdict into a far stronger almost-sure pathwise statement by composing with a complementary principle.

The first amplification is **BC1 unioned over a countable sequence $\varepsilon_k\downarrow0$** to extract *almost-sure convergence to zero* of random sequences whose probabilities of large excursion are summable. If $\sum_n\mathbb{P}(|X_n|>\varepsilon_k)<\infty$ for every $\varepsilon_k$ in a countable set tending to $0$, BC1 gives $\{|X_n|>\varepsilon_k\text{ i.o.}\}$ null for each $k$; a countable union of null sets is null, so a.s. $|X_n|\le\varepsilon_k$ eventually for every $k$, i.e. $X_n\to0$ a.s. The non-obvious upshot is that **"in probability + summable rate" gives almost-sure convergence for free** — no extraction of subsequences, no $L^p$ machinery. The example: in the elementary proof of the SLLN under a finite fourth moment, $\mathbb{P}(|S_n/n|>\varepsilon)\le\mathbb{E}(S_n/n)^4/\varepsilon^4=O(n^{-2})$, summable; BC1 directly delivers $S_n/n\to0$ a.s. without any martingale theory.

The second amplification is **BC combined with [[Thm - Kolmogorov 0-1 Law|Kolmogorov's 0–1 law]] for tail events**. Since $\{A_n\text{ i.o.}\}$ is a tail event of the underlying independent sequence, the 0–1 law forces $\mathbb{P}(\limsup A_n)\in\{0,1\}$ *a priori* — even without independence of the $A_n$ themselves, only of an underlying sequence — and BC then *computes which value*. The non-obvious upshot is that for a wide class of pathwise events constructed from i.i.d. inputs, the answer is automatically all-or-nothing, and BC's role is to identify the side. The example: for i.i.d. $(X_n)$, the event $\{X_n>c\text{ i.o.}\}$ is tail, hence in $\{0,1\}$; BC2 applied to $A_n=\{X_n>c\}$ with $\sum\mathbb{P}(X_1>c)$ either finite or infinite determines on which side — yielding the standard formula $\limsup X_n=\inf\{c:\mathbb{P}(X_1>c)\text{ summable}\}$ a.s.

The third amplification is **BC1+BC2 combined with the Cramér–Chernoff large-deviation bound** to derive sharp fluctuation laws like the **law of the iterated logarithm**. The [[Thm - Strong Law of Large Numbers|SLLN]] says $S_n/n\to\mu$ a.s. but says nothing about *rate*. Applying Chernoff $\mathbb{P}(S_n-n\mu>t\sqrt n)\le e^{-t^2/2}$ along a geometric subsequence $n_k=\lfloor q^k\rfloor$, summing, and exploiting monotonicity between consecutive blocks yields $\limsup_n(S_n-n\mu)/\sqrt{2n\sigma^2\log\log n}=1$ a.s. The non-obvious upshot is that a precise envelope for the fluctuations drops out of two routine BC applications — one for "achieved infinitely often" (BC2 on the lower bound) and one for "never exceeded eventually" (BC1 on the upper) — sharpening "fluctuations are $o(n)$" to "fluctuations are exactly $\sqrt{2n\sigma^2\log\log n}$."

---

# Statement

Let $(A_n)_{n\ge1}$ be events.

**(First Borel–Cantelli lemma.)** If $\displaystyle\sum_{n=1}^\infty\mathbb{P}(A_n)<\infty$, then $\mathbb{P}(\limsup_n A_n)=0$ — almost surely only finitely many $A_n$ occur.

**(Second Borel–Cantelli lemma.)** If the $(A_n)$ are independent and $\displaystyle\sum_{n=1}^\infty\mathbb{P}(A_n)=\infty$, then $\mathbb{P}(\limsup_n A_n)=1$ — almost surely infinitely many $A_n$ occur.

Hence for an independent sequence, $\mathbb{P}(A_n\text{ i.o.})\in\{0,1\}$, dichotomised by convergence/divergence of $\sum\mathbb{P}(A_n)$.

---

# Why Is It True

**First lemma — $\sigma$-subadditivity and a vanishing tail.** $\limsup A_n\subseteq\bigcup_{n\ge N}A_n$ for *every* $N$. By [[Thm - Properties of Measures|σ-subadditivity]], $\mathbb{P}(\limsup A_n)\le\sum_{n\ge N}\mathbb{P}(A_n)$. Since $\sum\mathbb{P}(A_n)<\infty$, the tail $\to0$ as $N\to\infty$; the left side does not depend on $N$, so it is $0$. (Equivalently: $\mathbb{E}[\sum\mathbf{1}_{A_n}]=\sum\mathbb{P}(A_n)<\infty$, so $\sum\mathbf{1}_{A_n}<\infty$ a.s.) This is exactly the [[Ex - The first Borel-Cantelli lemma|set-level argument from measure theory]] — no probability beyond a finite measure is used.

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
> > For each $N$, $\limsup_n A_n=\bigcap_M\bigcup_{n\ge M}A_n\subseteq\bigcup_{n\ge N}A_n$, so by [[Thm - Properties of Measures|σ-subadditivity]] $\mathbb{P}(\limsup A_n)\le\sum_{n\ge N}\mathbb{P}(A_n)$. The right side is the tail of a convergent series, $\to0$ as $N\to\infty$; the left side is fixed, hence $0$. $\square$

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
