---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Expectation and Moments"
  - "Thm - Properties of the Integral"
  - "Def - Independence"
tags: [probability, advanced-probability]
---

# Problem Statement

**(a)** State why $\mathbb{E}[a X+bY]=a\mathbb{E}X+b\mathbb{E}Y$ holds for *all* integrable $X,Y$ — with **no independence assumption**.

**(b) (Indicator method.)** Compute the expected number of fixed points of a uniformly random permutation of $\{1,\dots,n\}$ by writing the count as a sum of indicators.

**(c)** Show that variance is *not* additive in general — $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y+2\,\mathrm{Cov}(X,Y)$ — and is additive exactly when $X,Y$ are uncorrelated (in particular when independent).

**Recall:**

[[Def - Expectation and Moments|Expectation]] is the integral against $\mathbb{P}$; [[Thm - Properties of the Integral|linearity of the integral]].

---

# Convergent Strategy

**Problem class:** computing an expectation by *decomposition into indicators* — exploiting that linearity needs no independence.

**Assumption pattern:** a counting random variable $N$ is a *sum* $\sum_i\mathbf{1}_{A_i}$; linearity gives $\mathbb{E}[N]=\sum_i\mathbb{P}(A_i)$ regardless of dependence among the $A_i$. Variance, being quadratic, *does* feel the dependence.

**Theorem routing:** (a),(b) linearity of expectation; (c) expand the square.

---

# Legal Operations Used

1. **Indicator decomposition** — write a count as $\sum\mathbf{1}_{A_i}$.
2. **Linearity of expectation** — unconditional.
3. **Expand a square** for variance.

---

# Hints

> [!note]- Hint 1
> Linearity of expectation is linearity of the [[Thm - Properties of the Integral|integral]] — a property of $\int\cdot\,d\mathbb{P}$, with no probabilistic hypothesis.

> [!note]- Hint 2
> The number of fixed points is $N=\sum_{i=1}^n\mathbf{1}_{\{\pi(i)=i\}}$. What is $\mathbb{P}(\pi(i)=i)$?

> [!note]- Hint 3
> $\mathrm{Var}(X+Y)=\mathbb{E}[((X-\mathbb{E}X)+(Y-\mathbb{E}Y))^2]$ — expand.

---

# Solution

**Step 1 — (a).** Expectation is $\mathbb{E}[X]=\int_\Omega X\,d\mathbb{P}$, and the [[Thm - Properties of the Integral|integral is linear]]: $\int(aX+bY)\,d\mathbb{P}=a\int X+b\int Y$ for all integrable $X,Y$. Linearity is a property of integration, not of probability — it makes *no reference* to independence, joint laws, or correlation. This is the single most exploited fact in elementary probability.

**Step 2 — (b) Fixed points of a random permutation.** Let $\pi$ be uniform on the $n!$ permutations and $N=\#\{i:\pi(i)=i\}$ the number of fixed points. Write
$$N=\sum_{i=1}^n\mathbf{1}_{A_i},\qquad A_i=\{\pi(i)=i\}.$$
For each $i$, by symmetry $\mathbb{P}(\pi(i)=i)=\frac{(n-1)!}{n!}=\frac1n$ (fix $i$, permute the rest freely). By linearity,
$$\mathbb{E}[N]=\sum_{i=1}^n\mathbb{P}(A_i)=\sum_{i=1}^n\frac1n=1.$$
The expected number of fixed points is exactly $1$, for every $n$ — *even though the events $A_i$ are dependent* (knowing $\pi(1)=1$ changes $\mathbb{P}(\pi(2)=2)$). Linearity did not care.

**Step 3 — (c) Variance is not additive.** For $X,Y\in L^2$, writing $\tilde X=X-\mathbb{E}X$, $\tilde Y=Y-\mathbb{E}Y$,
$$\mathrm{Var}(X+Y)=\mathbb{E}[(\tilde X+\tilde Y)^2]=\mathbb{E}[\tilde X^2]+\mathbb{E}[\tilde Y^2]+2\mathbb{E}[\tilde X\tilde Y]=\mathrm{Var}X+\mathrm{Var}Y+2\,\mathrm{Cov}(X,Y).$$
So variance adds iff $\mathrm{Cov}(X,Y)=0$ — iff $X,Y$ are *uncorrelated*. Independent variables are uncorrelated ($\mathbb{E}[\tilde X\tilde Y]=\mathbb{E}\tilde X\,\mathbb{E}\tilde Y=0$ by independence and [[Thm - Fubini-Tonelli Theorem|Fubini]]), so for independent $X,Y$, $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y$ — but uncorrelated is strictly weaker than independent.

> [!note]- Complete formal solution
> (a) $\mathbb{E}=\int\cdot\,d\mathbb{P}$ is linear because the integral is — no probabilistic hypothesis. (b) $N=\sum_i\mathbf{1}_{\{\pi(i)=i\}}$, $\mathbb{P}(\pi(i)=i)=1/n$, so $\mathbb{E}[N]=n\cdot\frac1n=1$ by linearity despite dependence. (c) Expanding the square, $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y+2\mathrm{Cov}(X,Y)$, additive iff uncorrelated; independence $\Rightarrow$ uncorrelated $\Rightarrow$ additive. $\blacksquare$

---

# Key Takeaways

**Linearity of expectation holds unconditionally — it is linearity of the integral — and the *indicator method* turns this into a computational superpower.** To find the expected size of any count, write the count as a sum of indicators and add up their probabilities; *dependence is irrelevant*. The expected number of fixed points, of records, of triangles in a random graph, of empty boxes — all fall to one line, because $\mathbb{E}[\sum\mathbf{1}_{A_i}]=\sum\mathbb{P}(A_i)$ no matter how the $A_i$ interact. The trigger: "expected number of ..." → decompose into indicators.

**Variance is quadratic, so it *does* feel dependence: $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y+2\mathrm{Cov}(X,Y)$.** Additivity of variance holds only for *uncorrelated* (in particular independent) summands — this is exactly why the [[Thm - Strong Law of Large Numbers|law of large numbers]] for sums of independent variables has $\mathrm{Var}(S_n)=n\,\mathrm{Var}(X_1)$, hence $\mathrm{Var}(S_n/n)=\mathrm{Var}(X_1)/n\to0$, the [[Ex - Markov's inequality|Chebyshev]] route to the weak law. The lesson: linear functionals of random variables ignore dependence; quadratic ones do not.
