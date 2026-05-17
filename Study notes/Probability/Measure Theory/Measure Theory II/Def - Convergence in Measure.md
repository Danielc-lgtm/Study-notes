---
type: definition
subject: measure-theory
prereqs:
  - "Def - Measurable Function"
  - "Def - Almost Everywhere"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X,\mathcal{A},\mu)$ a measure space; $f,f_n$ measurable functions. $f_n\xrightarrow{\mu}f$ denotes convergence in measure.

---

# Axiom Motivation

[[Def - Almost Everywhere|Almost-everywhere convergence]] asks $f_n(x)\to f(x)$ for almost every fixed $x$ — a statement about each *point's trajectory*. There is a weaker, more "global" notion that turns out to be exactly the right hypothesis for several theorems: instead of tracking each point, track the *size of the bad set*.

Fix a tolerance $\varepsilon>0$ and ask: how large is the set where $f_n$ and $f$ still differ by more than $\varepsilon$? **Convergence in measure** demands that this set's measure $\to0$ for every $\varepsilon$. It does not require any individual point to converge — at each stage a *different* small region may be bad, and a fixed point may be bad infinitely often.

Why introduce it? Because a.e. convergence is *unnecessarily strong* for the [[Thm - Vitali Convergence Theorem|Vitali convergence theorem]]: the optimal hypothesis for $L^1$-convergence is convergence in measure plus [[Def - Absolute Continuity and Density|uniform integrability]], not a.e. convergence. Convergence in measure is also the natural mode in which the [[Thm - Dominated Convergence Theorem|DCT]] can be restated, and — on a probability space — it is exactly **convergence in probability**, the mode of the weak law of large numbers. It sits strictly between a.e. convergence and convergence in distribution.

---

# The Definition

Let $f,f_n:X\to\mathbb{R}$ ($n\in\mathbb{N}$) be measurable. The sequence $(f_n)$ **converges to $f$ in measure**, written $f_n\xrightarrow{\mu}f$, if for every $\varepsilon>0$
$$\mu\big(\{x\in X:|f_n(x)-f(x)|>\varepsilon\}\big)\ \xrightarrow[n\to\infty]{}\ 0.$$
When $\mu=\mathbb{P}$ is a probability measure this is called **convergence in probability**.

Relations (on a space of finite measure, $\mu(X)<\infty$):
- $f_n\to f$ $\mu$-a.e. $\implies f_n\xrightarrow{\mu}f$;
- $\int|f_n-f|\,d\mu\to0\implies f_n\xrightarrow{\mu}f$ (by [[Thm - Markov's Inequality|Markov's inequality]]);
- $f_n\xrightarrow{\mu}f\implies$ some **subsequence** converges a.e. to $f$.

The converses fail: convergence in measure does not imply a.e. convergence (the "typewriter sequence"), and on infinite-measure spaces a.e. convergence need not imply convergence in measure.

---

# Relate to Other Fields / Compression

Convergence in measure is "$L^0$ convergence" — convergence in the topology of the metric $d(f,g)=\int\frac{|f-g|}{1+|f-g|}\,d\mu$ (for $\mu$ finite) on the space of measurable functions modulo a.e.-equality. It is weaker than $L^p$ convergence for every $p\ge1$ and weaker than a.e. convergence, but stronger than convergence in distribution. In probability it *is* convergence in probability — the mode in which the [[Thm - Weak Law of Large Numbers|weak law of large numbers]] holds, and the natural target of [[Thm - Markov's Inequality|Markov]]/Chebyshev bounds.

---

# Examples / Corollaries

**The typewriter sequence.** On $([0,1],\lambda)$, enumerate the dyadic intervals $I_{n,k}=[k2^{-n},(k+1)2^{-n}]$ and let $f_m=\mathbf{1}_{I_{n,k}}$ run through them. Then $\lambda(\{f_m>\varepsilon\})=2^{-n}\to0$, so $f_m\xrightarrow{\lambda}0$ — yet for *every* $x$, $f_m(x)=1$ infinitely often, so $f_m\not\to0$ at any point. Convergence in measure without a.e. convergence.

**Subsequence rescue.** From any sequence converging in measure one can extract a subsequence with $\mu(\{|f_{n_k}-f|>2^{-k}\})<2^{-k}$; the [[Ex - The first Borel-Cantelli lemma|first Borel–Cantelli lemma]] then forces $f_{n_k}\to f$ a.e.

Calibration: (i) Does $f_n\xrightarrow{\mu}f$ require any point to converge? No. (ii) On $(\mathbb{R},\lambda)$, does $\mathbf{1}_{[n,n+1]}\to0$ in measure? No — $\lambda(\{>\tfrac12\})=1\not\to0$ (mass escapes to infinity). (iii) Does $L^1$-convergence imply convergence in measure? Yes, by Markov's inequality.

---

# Unlocked by This

> [!tip] Convergence in probability and the weak law *(from [[Advanced Probability II — Convergence and Limit Theorems|Advanced Probability]])*
> On a probability space this is [[Def - Modes of Convergence|convergence in probability]], the conclusion of the [[Thm - Weak Law of Large Numbers|weak law of large numbers]] and a hypothesis of the [[Thm - Vitali Convergence Theorem|Vitali convergence theorem]].
