---
type: exercise
subject: measure-theory
difficulty: "⭐"
prereqs:
  - "Def - The Integral"
  - "Thm - Properties of the Integral"
tags: [analysis, measure-theory, probability]
---

# Problem Statement

Let $(X,\mathcal{A},\mu)$ be a measure space and $f\ge0$ measurable.

**(a) (Markov's inequality.)** Prove that for every $\lambda>0$,
$$\mu\big(\{x:f(x)\ge\lambda\}\big)\ \le\ \frac1\lambda\int_X f\,d\mu.$$

**(b)** Deduce **Chebyshev's inequality**: for $g\in L^2(\mu)$ on a probability space, $\mu(|g-\mathbb{E}g|\ge\lambda)\le\lambda^{-2}\mathrm{Var}(g)$.

**(c)** Deduce that if $\int f\,d\mu=0$ and $f\ge0$, then $f=0$ $\mu$-a.e.

**Recall:**

[[Def - The Integral|The integral]] of $f\ge0$ is monotone: $0\le f\le g\Rightarrow\int f\le\int g$ ([[Thm - Properties of the Integral]]).

---

# Convergent Strategy

**Problem class:** bounding the measure of a level set by an integral — trading a "size of a set" for an "integral."

**Assumption pattern:** $f\ge0$. The one idea: on the set $\{f\ge\lambda\}$, the function $f$ is *at least $\lambda$*, so $f$ dominates the simple function $\lambda\mathbf{1}_{\{f\ge\lambda\}}$ everywhere. Monotonicity of the integral converts this pointwise domination into the inequality.

**Theorem routing:** $f\ge\lambda\mathbf{1}_{\{f\ge\lambda\}}\Rightarrow\int f\ge\lambda\mu(\{f\ge\lambda\})$.

**Key decision point:** seeing that the right comparison function is the *indicator scaled by the threshold*.

---

# Legal Operations Used

1. **Dominate by a scaled indicator** — $f\ge\lambda\mathbf{1}_{\{f\ge\lambda\}}$.
2. **Monotonicity of the integral.**
3. **Apply Markov to a transformed variable** — $g\mapsto(g-\mathbb{E}g)^2$ for Chebyshev.

---

# Hints

> [!note]- Hint 1
> On $\{f\ge\lambda\}$, $f$ is at least $\lambda$; everywhere else $f\ge0$. So $f\ge\lambda\mathbf{1}_{\{f\ge\lambda\}}$ pointwise. Integrate.

> [!note]- Hint 2
> For Chebyshev, apply Markov to the non-negative function $(g-\mathbb{E}g)^2$ with threshold $\lambda^2$.

> [!note]- Hint 3
> For (c): if $\int f=0$, Markov gives $\mu(f\ge1/n)=0$ for every $n$. What is $\{f>0\}$ in terms of these?

---

# Solution

**Step 1 — (a) Markov.** Pointwise, $f\ge\lambda\mathbf{1}_{\{f\ge\lambda\}}$: on $\{f\ge\lambda\}$ both sides compare $f\ge\lambda$, off it the right side is $0\le f$. By [[Thm - Properties of the Integral|monotonicity]] and the integral of a simple function,
$$\int_X f\,d\mu\ \ge\ \int_X\lambda\mathbf{1}_{\{f\ge\lambda\}}\,d\mu\ =\ \lambda\,\mu(\{f\ge\lambda\}).$$
Divide by $\lambda>0$.

**Step 2 — (b) Chebyshev.** Apply (a) to the non-negative function $(g-\mathbb{E}g)^2$ with threshold $\lambda^2$:
$$\mu(|g-\mathbb{E}g|\ge\lambda)=\mu\big((g-\mathbb{E}g)^2\ge\lambda^2\big)\le\frac{1}{\lambda^2}\int(g-\mathbb{E}g)^2\,d\mu=\frac{\mathrm{Var}(g)}{\lambda^2}.$$

**Step 3 — (c).** If $\int f\,d\mu=0$, Markov gives $\mu(f\ge1/n)\le n\int f=0$ for every $n\ge1$. The set $\{f>0\}=\bigcup_{n\ge1}\{f\ge1/n\}$ is a countable union of null sets, hence null. So $f=0$ $\mu$-a.e.

> [!note]- Complete formal solution
> (a) $f\ge\lambda\mathbf{1}_{\{f\ge\lambda\}}$ pointwise; monotonicity gives $\int f\ge\lambda\mu(f\ge\lambda)$. (b) Markov applied to $(g-\mathbb{E}g)^2\ge0$ at level $\lambda^2$. (c) $\int f=0$ and Markov give $\mu(f\ge1/n)=0$ $\forall n$; $\{f>0\}=\bigcup_n\{f\ge1/n\}$ is null by $\sigma$-subadditivity. $\blacksquare$

---

# Key Takeaways

**Markov's inequality is the universal "tail bound": it converts a bound on the *integral* (a global average) into a bound on the *measure of a level set* (a local extreme).** The entire content is the one-line pointwise domination $f\ge\lambda\mathbf{1}_{\{f\ge\lambda\}}$, integrated. This trade — average controls tail — is the most-used estimate in probability: it is the route from $L^1$-convergence to [[Def - Convergence in Measure|convergence in measure]], the proof of the [[Thm - Weak Law of Large Numbers|weak law of large numbers]] (via Chebyshev), and the first step of the [[Thm - Hahn-Carathéodory Extension Theorem|first Borel–Cantelli]] applications.

**Markov applied to a *transformed* variable yields the whole family of moment inequalities.** Apply it to $(g-\mathbb{E}g)^2$ and you get Chebyshev; to $|g|^p$, the $p$-th moment bound; to $e^{tg}$, the exponential Chernoff bound that powers [[Thm - Cramér's Theorem|large deviations]]. The trigger-reaction: "I need to bound $\mu(\text{$g$is extreme})$" → "apply Markov to a well-chosen non-negative function of $g$." The corollary $\int f=0\Rightarrow f=0$ a.e. is itself a workhorse — it is how one proves two functions are equal a.e. (show their difference integrates to $0$ in absolute value).
