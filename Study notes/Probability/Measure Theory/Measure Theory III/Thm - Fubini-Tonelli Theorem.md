---
type: theorem
subject: measure-theory
prereqs:
  - "Thm - Product Measure"
  - "Thm - Monotone Convergence Theorem"
  - "Thm - Approximation by Simple Functions"
  - "Def - The Integral"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X_i,\mathcal{A}_i,\mu_i)$, $i=1,2$, $\sigma$-finite; $\mu_1\otimes\mu_2$ the [[Thm - Product Measure|product measure]] on $X_1\times X_2$. $f:X_1\times X_2\to[-\infty,\infty]$ measurable for $\mathcal{A}_1\otimes\mathcal{A}_2$.

---

# Motivation

A double integral $\int_{X_1\times X_2}f\,d(\mu_1\otimes\mu_2)$ is, in principle, an integral over the whole product space — hard to evaluate directly. Fubini–Tonelli reduces it to an **iterated integral**: integrate out $x_2$ first (a one-variable integral, for each fixed $x_1$), then integrate the result over $x_1$ — or in the other order. It is the theorem that makes multiple integrals *computable*, and that licenses interchanging the order of integration. **Tonelli** is the non-negative version (no integrability hypothesis needed); **Fubini** is the signed version (needs absolute integrability). Together they are among the most-used theorems in all of analysis and probability.

---

# Sources and Targets

**Sources.** Hypotheses: $\mu_1,\mu_2$ $\sigma$-finite, and either $f\ge0$ (Tonelli) or $f\in L^1(\mu_1\otimes\mu_2)$ (Fubini). The standard *bridge* to verify Fubini's hypothesis: first apply **Tonelli to $|f|$** — if the iterated integral of $|f|$ is finite, then $f\in L^1(\mu_1\otimes\mu_2)$ and Fubini applies. Tonelli is the gateway to Fubini.

**Targets.** The interchange $\iint=\iint$ yields: evaluation of multiple integrals; the identity $\int_X g\,d\mu=\int_0^\infty\mu(g>t)\,dt$ ("layer-cake"); convolution identities; in probability, $\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]$ for [[Def - Independence|independent]] $X,Y$, and the computation of expectations of functions of independent variables by iterated integration against the product law.

---

# Formal Statement

Let $(X_i,\mathcal{A}_i,\mu_i)$ be $\sigma$-finite and $f:X_1\times X_2\to[-\infty,\infty]$ be $\mathcal{A}_1\otimes\mathcal{A}_2$-measurable.

**(Tonelli)** If $f\ge0$, then the slice functions $x_2\mapsto f(x_1,x_2)$ and $x_1\mapsto f(x_1,x_2)$ are measurable, the iterated integrals $x_1\mapsto\int f(x_1,x_2)\,d\mu_2$ and $x_2\mapsto\int f(x_1,x_2)\,d\mu_1$ are measurable, and
$$\int_{X_1\times X_2}f\,d(\mu_1\otimes\mu_2)=\int_{X_1}\!\Big(\int_{X_2}f\,d\mu_2\Big)d\mu_1=\int_{X_2}\!\Big(\int_{X_1}f\,d\mu_1\Big)d\mu_2,$$
all three values equal in $[0,\infty]$.

**(Fubini)** If $f\in L^1(\mu_1\otimes\mu_2)$, then for $\mu_1$-a.e. $x_1$ the slice $f(x_1,\cdot)\in L^1(\mu_2)$, the (a.e.-defined) iterated integral is in $L^1(\mu_1)$, and the same chain of equalities holds.

---

# Why Is It True

Tonelli is the [[Thm - Approximation by Simple Functions|standard machine]] turned once.

*Indicators.* For $f=\mathbf{1}_E$, $\int_{X_2}\mathbf{1}_E(x_1,x_2)\,d\mu_2=\mu_2(E_{x_1})$, and the [[Thm - Product Measure|product measure theorem]] *is exactly* the statement $\int_{X_1}\mu_2(E_{x_1})\,d\mu_1=(\mu_1\otimes\mu_2)(E)$. So Tonelli holds for indicators *by the definition of the product measure*.

*Simple functions.* By [[Thm - Properties of the Integral|linearity]] of all three integrals, Tonelli extends to non-negative simple functions.

*General $f\ge0$.* Take simple $s_n\uparrow f$ ([[Thm - Approximation by Simple Functions]]). Each slice $s_n(x_1,\cdot)\uparrow f(x_1,\cdot)$, so by [[Thm - Monotone Convergence Theorem|MCT]] (in $x_2$) $\int s_n(x_1,\cdot)\,d\mu_2\uparrow\int f(x_1,\cdot)\,d\mu_2$; this limit is measurable in $x_1$. Apply MCT *again* (in $x_1$, and in the product space): all three integrals of $s_n$ converge to the corresponding integrals of $f$, and equality is preserved through the limit. **Tonelli is the product-measure identity for indicators, propagated to all $f\ge0$ by the standard machine, with MCT doing every limit interchange** — which is why Tonelli needs *no integrability hypothesis*: MCT never does.

*Fubini.* Split $f=f^+-f^-$. Apply Tonelli to $f^+$ and $f^-$ separately. The hypothesis $f\in L^1(\mu_1\otimes\mu_2)$ — equivalently, by Tonelli applied to $|f|$, the finiteness of the iterated integral of $|f|$ — guarantees $\int f^\pm\,d(\mu_1\otimes\mu_2)<\infty$, so the subtraction $\iint f^+-\iint f^-$ involves no "$\infty-\infty$" and the iterated integrals of $f^\pm$ are finite for $\mu_1$-a.e. $x_1$. Subtract.

---

# What Makes This Hard

Tonelli itself is routine *once* one accepts that "Tonelli for indicators $=$ the product measure theorem" — that recognition is the keystone, and it is why the [[Thm - Product Measure|product measure]] had to be built via the slice formula first. The genuine pitfall is **Fubini without integrability**: the iterated integrals can both exist and *disagree* if $f$ is not absolutely integrable (the classic $\sum_n\sum_m(\mathbf{1}_{n=m}-\mathbf{1}_{n=m+1})$ on $\mathbb{N}\times\mathbb{N}$ gives $0\neq1$). The discipline: **always run Tonelli on $|f|$ first**; only if that iterated integral is finite may one apply Fubini to $f$.

---

# Rederivation Scaffold

**High-level strategy.** Tonelli: standard machine — indicators (= product measure theorem), simple (linearity), $f\ge0$ (MCT twice). Fubini: split $f=f^+-f^-$, Tonelli on each, subtract using $L^1$.

**Subgoal decomposition.**

1. **Tonelli for indicators.** $\iint\mathbf{1}_E$ in any order $=(\mu_1\otimes\mu_2)(E)$ — restate the [[Thm - Product Measure|product measure theorem]].
2. **Tonelli for simple $f\ge0$.** Linearity of the three integrals.
3. **Tonelli for $f\ge0$.** $s_n\uparrow f$; MCT in $x_2$, then in $x_1$ and in the product — equality survives.
4. **Fubini.** $f=f^+-f^-$; Tonelli on $f^\pm$; $f\in L^1\Rightarrow\iint f^\pm<\infty$; subtract; slices in $L^1$ a.e.

---

# Lemma Decomposition

> [!note]- Lemma 1: Tonelli for non-negative functions
> **Statement:** For $f\ge0$ measurable, the three integrals coincide in $[0,\infty]$.
>
> > [!note]- Full proof
> > For $f=\mathbf{1}_E$ this is the [[Thm - Product Measure|product measure]] identity $(\mu_1\otimes\mu_2)(E)=\int\mu_2(E_{x_1})\,d\mu_1=\int\mu_1(E_{x_2})\,d\mu_2$. Linearity extends it to non-negative simple functions. For general $f\ge0$, take simple $s_n\uparrow f$; the slices $s_n(x_1,\cdot)\uparrow f(x_1,\cdot)$, so [[Thm - Monotone Convergence Theorem|MCT]] gives $\int s_n(x_1,\cdot)d\mu_2\uparrow\int f(x_1,\cdot)d\mu_2$ (measurable in $x_1$ as a limit of measurables); MCT again in $d\mu_1$ and in $d(\mu_1\otimes\mu_2)$ carries the three-way equality to the limit. $\square$

> [!note]- Lemma 2: Fubini from Tonelli
> **Statement:** $f\in L^1(\mu_1\otimes\mu_2)\Rightarrow$ the iterated integrals exist a.e., are finite, and equal $\int f\,d(\mu_1\otimes\mu_2)$.
>
> > [!note]- Full proof
> > By Lemma 1 applied to $|f|\ge0$, $\iint|f|=\int|f|\,d(\mu_1\otimes\mu_2)<\infty$, so the iterated integral of $|f|$ is finite — hence $\int|f(x_1,\cdot)|\,d\mu_2<\infty$ for $\mu_1$-a.e. $x_1$, i.e. $f(x_1,\cdot)\in L^1(\mu_2)$ a.e. Apply Lemma 1 to $f^+$ and $f^-$ (both $\ge0$, both with finite integral $\le\int|f|$). Subtracting the two finite iterated integrals (no $\infty-\infty$) gives $\iint f=\int f\,d(\mu_1\otimes\mu_2)$, in either order. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 is Tonelli; Lemma 2 is Fubini. Measurability of the slice and iterated-integral functions is part of Lemma 1's induction (limits of measurable functions). $\blacksquare$

---

# Cross-Field Exercise Suggestions

Fubini–Tonelli proves the **layer-cake formula** $\int g\,d\mu=\int_0^\infty\mu(g>t)\,dt$ (apply Tonelli to $\mathbf{1}_{\{(x,t):t<g(x)\}}$ on $X\times[0,\infty)$) — the bridge between integrating a function and integrating its tail. In probability it gives $\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]$ for [[Def - Independence|independent]] $X,Y$ (the joint law is a product, integrate the product against it), and the [[Thm - Doob's Maximal Inequality|$L^p$ maximal inequality]] uses Fubini to integrate $\int_0^\infty pt^{p-1}\mathbb{P}(X^*>t)\,dt$.

---

# Bridges

- **[[Thm - Product Measure]]** — supplies the measure; Tonelli-for-indicators *is* the product-measure theorem.
- **[[Thm - Monotone Convergence Theorem]]** — every limit interchange in Tonelli is an MCT; this is why Tonelli is hypothesis-free.
- **[[Def - Independence]]** *(Advanced Probability)* — Fubini against a product law is the computational engine for independent random variables.
