---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Fubini-Tonelli Theorem"
  - "Thm - Product Measure"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $(X,\mathcal{A},\mu)$ be $\sigma$-finite and $f:X\to[0,\infty]$ measurable. Consider the **region under the graph**
$$\Gamma_f=\{(x,t)\in X\times[0,\infty):0\le t<f(x)\}.$$

**(a)** Show $\Gamma_f\in\mathcal{A}\otimes\mathcal{B}([0,\infty))$.

**(b)** Prove the **layer-cake formula**: $\displaystyle(\mu\otimes\lambda)(\Gamma_f)=\int_X f\,d\mu=\int_0^\infty\mu(\{f>t\})\,dt.$

**(c)** Conclude "the integral is the area under the graph" and that $\int_X f\,d\mu$ can always be computed from the tail function $t\mapsto\mu(\{f>t\})$.

**Recall:**

[[Thm - Fubini-Tonelli Theorem|Tonelli]]: for $g\ge0$ measurable, $\int g\,d(\mu\otimes\lambda)$ equals either iterated integral.

---

# Convergent Strategy

**Problem class:** evaluating a product-measure of a region two ways — the two iterated integrals of a single indicator.

**Assumption pattern:** $\Gamma_f$ is a region; $(\mu\otimes\lambda)(\Gamma_f)=\int\mathbf{1}_{\Gamma_f}\,d(\mu\otimes\lambda)$. [[Thm - Fubini-Tonelli Theorem|Tonelli]] computes it as an iterated integral — and *which variable is integrated first* gives the two formulas.

**Theorem routing:** integrate $t$ first → vertical slices have length $f(x)$ → $\int f\,d\mu$; integrate $x$ first → horizontal slices have $\mu$-measure $\mu(\{f>t\})$ → $\int_0^\infty\mu(\{f>t\})\,dt$.

---

# Legal Operations Used

1. **Express a region's measure as an integral of an indicator.**
2. **Tonelli** to compute it as an iterated integral, in each order.

---

# Hints

> [!note]- Hint 1
> $(\mu\otimes\lambda)(\Gamma_f)=\int\mathbf{1}_{\Gamma_f}\,d(\mu\otimes\lambda)$. Apply Tonelli — $\mathbf{1}_{\Gamma_f}\ge0$, no integrability needed.

> [!note]- Hint 2
> Vertical slice: $(\Gamma_f)_x=\{t:0\le t<f(x)\}=[0,f(x))$, of length $f(x)$.

> [!note]- Hint 3
> Horizontal slice: $(\Gamma_f)^t=\{x:f(x)>t\}$, of $\mu$-measure $\mu(\{f>t\})$.

---

# Solution

**Step 1 — (a).** $\Gamma_f=\{(x,t):t<f(x)\}\cap\{t\ge0\}$. The function $(x,t)\mapsto f(x)-t$ is $\mathcal{A}\otimes\mathcal{B}$-measurable (composition of projections with measurable maps), so $\{(x,t):t<f(x)\}$ is measurable; intersecting with $\{t\ge0\}$ keeps it in $\mathcal{A}\otimes\mathcal{B}([0,\infty))$.

**Step 2 — (b).** Apply [[Thm - Fubini-Tonelli Theorem|Tonelli]] to $\mathbf{1}_{\Gamma_f}\ge0$:
$$(\mu\otimes\lambda)(\Gamma_f)=\int\mathbf{1}_{\Gamma_f}\,d(\mu\otimes\lambda)=\int_X\Big(\int_0^\infty\mathbf{1}_{\Gamma_f}(x,t)\,dt\Big)d\mu=\int_X\Big(\int_0^\infty\mathbf{1}_{[0,f(x))}(t)\,dt\Big)d\mu=\int_X f(x)\,d\mu.$$
Integrating in the *other* order:
$$(\mu\otimes\lambda)(\Gamma_f)=\int_0^\infty\Big(\int_X\mathbf{1}_{\Gamma_f}(x,t)\,d\mu\Big)dt=\int_0^\infty\mu(\{x:f(x)>t\})\,dt.$$
Equating the two iterated integrals gives the layer-cake formula.

**Step 3 — (c).** The first equality, $\int f\,d\mu=(\mu\otimes\lambda)(\Gamma_f)$, says literally **the integral is the area under the graph** — the picture made into a theorem. The second, $\int f\,d\mu=\int_0^\infty\mu(\{f>t\})\,dt$, says the integral is recoverable from the *tail / distribution function* of $f$ alone — one need not know $f$ pointwise, only how much of the space exceeds each level $t$.

> [!note]- Complete formal solution
> (a) $\Gamma_f$ is the measurable set $\{f(x)-t>0\}\cap\{t\ge0\}$. (b) Tonelli on $\mathbf{1}_{\Gamma_f}\ge0$: integrating $t$ first gives $\int_X\lambda([0,f(x)))\,d\mu=\int f\,d\mu$; integrating $x$ first gives $\int_0^\infty\mu(f>t)\,dt$; both equal $(\mu\otimes\lambda)(\Gamma_f)$. (c) Hence $\int f\,d\mu$ is the area under the graph and equals $\int_0^\infty\mu(f>t)\,dt$. $\blacksquare$

---

# Key Takeaways

**The layer-cake formula $\int f\,d\mu=\int_0^\infty\mu(\{f>t\})\,dt$ is Tonelli applied to the indicator of the region under the graph — the integral computed by slicing two ways.** Slice vertically and you read off "$\int f$" (the picture's intuition); slice horizontally and you read off the tail integral. Equating them is the formula. This is the single most useful identity for converting between *integrating a function* and *integrating its distribution* — and it shows the integral depends only on the law/distribution of $f$, never on its pointwise values.

**In probability the layer-cake formula is $\mathbb{E}[X]=\int_0^\infty\mathbb{P}(X>t)\,dt$ for $X\ge0$** — expectation as the integral of the survival function. It generalises to $\mathbb{E}[\varphi(X)]=\int_0^\infty\varphi'(t)\mathbb{P}(X>t)\,dt$ and is the workhorse behind moment computations, the proof of [[Thm - Doob's Maximal Inequality|Doob's Lᵖ inequality]] (integrate $\int pt^{p-1}\mathbb{P}(X^*>t)\,dt$), and the equivalence of "finite expectation" with "summable tail."
