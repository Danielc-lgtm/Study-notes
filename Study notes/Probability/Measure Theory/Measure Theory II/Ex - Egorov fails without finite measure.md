---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Egorov's Theorem"
  - "Def - Almost Everywhere"
tags: [analysis, measure-theory]
---

# Problem Statement

[[Thm - Egorov's Theorem|Egorov's theorem]] requires $\mu(\Omega)<\infty$.

**(a)** On $(\mathbb{R},\lambda)$ exhibit measurable $f_n\to0$ pointwise everywhere for which there is **no** set $F$ with $\lambda(\mathbb{R}\setminus F)<\infty$ — let alone $<\delta$ — on which $f_n\to0$ uniformly. Conclude Egorov fails on infinite-measure spaces.

**(b)** Show, conversely, that the conclusion of Egorov *does* survive if one only requires $F$ measurable (not compact) and assumes $\mu(\Omega)<\infty$ — i.e. the finiteness, not the topology, is what matters.

**Recall:**

![[Thm - Egorov's Theorem#Formal Statement]]

---

# Convergent Strategy

**Problem class:** demonstrating a hypothesis is necessary, by amputating it.

**Assumption pattern:** Egorov's proof used $\mu(\Omega)<\infty$ for [[Thm - Properties of Measures|continuity from above]] of the bad sets $C_{i,j}$. Kill finiteness $\Rightarrow$ the bad sets need not shrink in measure. The counterexample should be "a bump that converges pointwise but slides to infinity."

**Theorem routing:** uniform convergence on $F$ means $\sup_F|f_n|\to0$; design $f_n$ so this fails on every co-finite-measure set.

**Key decision point:** the bump $f_n=\mathbf{1}_{[n,n+1]}$ — converges to $0$ at every point, but the bump itself never shrinks.

---

# Legal Operations Used

1. **Escape-to-infinity counterexample.**
2. **Negate uniform convergence** — exhibit, for each candidate $F$, points where $|f_n|$ stays large.

---

# Hints

> [!note]- Hint 1
> Try $f_n=\mathbf{1}_{[n,n+1]}$. Does $f_n(x)\to0$ for every fixed $x$? Yes — once $n>x$.

> [!note]- Hint 2
> For $f_n\to0$ uniformly on $F$ you need $\sup_F f_n\to0$. If $F$ has co-finite measure $<\infty$, must $F$ meet $[n,n+1]$ for infinitely many $n$?

---

# Solution

**Step 1 — (a) The escaping bump.** Let $f_n=\mathbf{1}_{[n,n+1]}$ on $(\mathbb{R},\lambda)$. For every fixed $x$, $f_n(x)=0$ once $n>x$, so $f_n\to0$ *everywhere* (in particular $\lambda$-a.e.).

> [!note]- Derivation
> Suppose $F$ is measurable with $\lambda(\mathbb{R}\setminus F)<\infty$ and $f_n\to0$ uniformly on $F$. Uniform convergence forces $\sup_{x\in F}f_n(x)\to0$, so for large $n$, $f_n<1$ on $F$, i.e. $F\cap[n,n+1]=\emptyset$. Hence $[n,n+1]\subseteq\mathbb{R}\setminus F$ for all large $n$, giving $\lambda(\mathbb{R}\setminus F)\ge\sum_{n\ge N}\lambda([n,n+1])=\infty$ — contradiction. So no co-finite-measure $F$ carries uniform convergence; *a fortiori* none with $\lambda(\mathbb{R}\setminus F)<\delta$. Egorov fails.

The mechanism: the "mass" of $f_n$ never shrinks — it is always a bump of height $1$ — it merely translates to infinity. Pointwise each $x$ is eventually clear, but no *single* deadline works for all $x$, and there is infinitely much room ($\lambda(\mathbb{R})=\infty$) for the bump to keep escaping.

**Step 2 — (b) Finiteness alone suffices.** Inspecting Egorov's proof: the only use of "$\mu(\Omega)<\infty$" is [[Thm - Properties of Measures|continuity from above]] $\mu(C_{i,j})\downarrow0$ for the decreasing bad sets $C_{i,j}$ (which needs a finite-measure first term). Producing $F$ *compact* (when $\Omega\subseteq\mathbb{R}^n$) is an extra step via [[Thm - Regularity of Lebesgue Measure|inner regularity]]; if one only wants $F$ measurable, that step is dropped and the proof goes through verbatim for any finite measure space. So it is finiteness, not topology, that Egorov needs.

> [!note]- Complete formal solution
> (a) $f_n=\mathbf{1}_{[n,n+1]}\to0$ pointwise. If $f_n\to0$ uniformly on $F$ then $F\cap[n,n+1]=\emptyset$ for large $n$, so $\mathbb{R}\setminus F\supseteq\bigcup_{n\ge N}[n,n+1]$ has infinite measure — Egorov's conclusion is unattainable. (b) Egorov's proof uses $\mu(\Omega)<\infty$ solely for continuity from above of the bad sets; the compactness of $F$ is a separable inner-regularity add-on. Hence finiteness alone yields a measurable $F$. $\blacksquare$

---

# Key Takeaways

**Egorov's theorem is a finite-measure theorem, and the obstruction on infinite-measure spaces is escape to infinity.** The escaping bump $\mathbf{1}_{[n,n+1]}$ converges pointwise yet uniformly on no co-finite set: there is unboundedly much room for non-uniformity to flee into. This is the same mechanism that makes [[Thm - Fatou's Lemma|Fatou strict]], breaks [[Thm - Properties of Measures|continuity from above]] without finiteness, and forces the [[Thm - Dominated Convergence Theorem|DCT]] to demand a dominating function. The diagnostic "could the mass escape to infinity?" instantly predicts which finite-measure theorems fail on $\mathbb{R}$.

**A probability space has finite (indeed unit) total measure, so Egorov, Lusin, and the bounded convergence theorem are all available "for free" in probability** — there is no room for escape on a space of mass $1$. This is a recurring dividend: many measure-theoretic theorems that need a finiteness hypothesis become unconditional once one is on a probability space.
