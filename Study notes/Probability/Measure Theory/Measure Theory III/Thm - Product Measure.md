---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Product σ-Algebra"
  - "Def - σ-Finite Measure"
  - "Thm - Dynkin's π-λ Theorem"
  - "Thm - Monotone Convergence Theorem"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X_1,\mathcal{A}_1,\mu_1)$, $(X_2,\mathcal{A}_2,\mu_2)$ are $\sigma$-finite measure spaces; $X=X_1\times X_2$, $\mathcal{A}=\mathcal{A}_1\otimes\mathcal{A}_2$ the [[Def - Product σ-Algebra|product $\sigma$-algebra]]. For $E\subseteq X$, $E_{x_1}=\{x_2:(x_1,x_2)\in E\}$ is the slice.

---

# Motivation

To integrate functions of two variables, or to model a *pair* of independent random experiments, one needs a measure on the product space. The product measure $\mu_1\otimes\mu_2$ is the unique measure assigning a rectangle $A_1\times A_2$ the *product of side measures* $\mu_1(A_1)\mu_2(A_2)$ — "area $=$ width $\times$ height," lifted to abstract measure spaces. Its existence and uniqueness are what make [[Thm - Fubini-Tonelli Theorem|Fubini's theorem]] and the measure-theoretic definition of [[Def - Independence|independence]] possible.

---

# Sources and Targets

**Sources.** Hypotheses: $\mu_1,\mu_2$ **$\sigma$-finite**. $\sigma$-finiteness is essential — for uniqueness (via [[Thm - Dynkin's π-λ Theorem|$\pi$–$\lambda$]]) and for the slice-integral to be well-defined. Probability measures are finite, hence $\sigma$-finite, so product *probability* measures always exist.

**Targets.** $\mu_1\otimes\mu_2$ feeds [[Thm - Fubini-Tonelli Theorem|Fubini–Tonelli]] (double integral $=$ iterated integral); it gives $\lambda_m\otimes\lambda_n=\lambda_{m+n}$ (Lebesgue measure is a product); and the joint law of [[Def - Independence|independent]] random variables is, by definition, the product of the marginal laws.

---

# Formal Statement

Let $(X_i,\mathcal{A}_i,\mu_i)$, $i=1,2$, be $\sigma$-finite measure spaces. Then there exists a **unique** measure $\mu_1\otimes\mu_2$ on $(X,\mathcal{A}_1\otimes\mathcal{A}_2)$ with
$$(\mu_1\otimes\mu_2)(A_1\times A_2)=\mu_1(A_1)\,\mu_2(A_2)\qquad\text{for all }A_i\in\mathcal{A}_i.$$
It is $\sigma$-finite, and for every $E\in\mathcal{A}_1\otimes\mathcal{A}_2$ the slice functions $x_1\mapsto\mu_2(E_{x_1})$ and $x_2\mapsto\mu_1(E_{x_2})$ are measurable, with
$$(\mu_1\otimes\mu_2)(E)=\int_{X_1}\mu_2(E_{x_1})\,d\mu_1(x_1)=\int_{X_2}\mu_1(E_{x_2})\,d\mu_2(x_2).$$
For Lebesgue measure, $\lambda_m\otimes\lambda_n=\lambda_{m+n}$.

---

# Why Is It True

**Existence by the slice formula.** Define directly $\sigma(E)=\int_{X_1}\mu_2(E_{x_1})\,d\mu_1(x_1)$ — "sweep a vertical line across $E$, integrate the heights." Two things must be checked. First, the integrand $x_1\mapsto\mu_2(E_{x_1})$ is measurable: this is a [[Thm - Dynkin's π-λ Theorem|$\pi$–$\lambda$]] argument — it holds for rectangles ($\mu_2((A_1\times A_2)_{x_1})=\mu_2(A_2)\mathbf{1}_{A_1}(x_1)$, measurable), the family of $E$ for which it holds is a $\lambda$-system, and the rectangles are a $\pi$-system generating $\mathcal{A}$. Second, $\sigma$ is $\sigma$-additive: $E=\bigsqcup E_n\Rightarrow E_{x_1}=\bigsqcup(E_n)_{x_1}$, so $\mu_2(E_{x_1})=\sum\mu_2((E_n)_{x_1})$, and [[Thm - Monotone Convergence Theorem|MCT]] (partial sums increase) pulls the sum out of the $d\mu_1$-integral. On rectangles $\sigma(A_1\times A_2)=\int\mu_2(A_2)\mathbf{1}_{A_1}\,d\mu_1=\mu_1(A_1)\mu_2(A_2)$ — the desired normalisation.

**Uniqueness by $\pi$–$\lambda$.** The rectangles form a $\pi$-system generating $\mathcal{A}$. Any two measures agreeing on them agree on $\mathcal{A}$ — by [[Thm - Dynkin's π-λ Theorem|Dynkin's lemma]], provided $\sigma$-finiteness supplies a countable exhaustion of $X$ by finite-measure rectangles $X_{1,k}\times X_{2,k}$. This is the *sole* role of $\sigma$-finiteness in uniqueness.

The slogan: **the product measure is "integrate the slice measure"; that this is a measure is MCT, that it is the *only* one is $\pi$–$\lambda$.** The symmetry of the two iterated formulas — sweeping vertically or horizontally — is uniqueness applied to two candidate constructions.

---

# What Makes This Hard

Two non-elementary inputs, neither obvious. (i) **Measurability of the slice-measure function** $x_1\mapsto\mu_2(E_{x_1})$ — one cannot check this set-by-set; it *must* go through the [[Thm - Dynkin's π-λ Theorem|$\pi$–$\lambda$ theorem]] (true on rectangles, $\lambda$-system, generate). (ii) The need for **$\sigma$-finiteness**: without it, uniqueness fails and the slice integral can be ill-defined. The common error is to treat the slice formula as a definition without verifying the integrand is measurable, or to forget $\sigma$-finiteness and lose uniqueness.

---

# Rederivation Scaffold

**High-level strategy.** Define $\sigma(E)$ as the integral of the slice measure. Prove the integrand measurable ($\pi$–$\lambda$), prove $\sigma$ a measure (MCT for $\sigma$-additivity), check the rectangle normalisation, get uniqueness from $\pi$–$\lambda$ + $\sigma$-finiteness.

**Subgoal decomposition.**

1. **Slices are measurable.** $E\in\mathcal{A}_1\otimes\mathcal{A}_2\Rightarrow E_{x_1}\in\mathcal{A}_2$ ($\pi$–$\lambda$ on the family of $E$ with measurable slices).
2. **$x_1\mapsto\mu_2(E_{x_1})$ is $\mathcal{A}_1$-measurable.** True for rectangles; $\lambda$-system; generate. (Finite-measure case first, then $\sigma$-finite truncation.)
3. **$\sigma(E)=\int\mu_2(E_{x_1})\,d\mu_1$ is a measure.** $\sigma(\emptyset)=0$; $\sigma$-additivity from slice-disjointness + MCT.
4. **Normalisation and uniqueness.** $\sigma(A_1\times A_2)=\mu_1(A_1)\mu_2(A_2)$; rectangles are a generating $\pi$-system; $\sigma$-finiteness + Dynkin $\Rightarrow$ uniqueness.

---

# Lemma Decomposition

> [!note]- Lemma 1: The slice-measure function is measurable
> **Statement:** For $E\in\mathcal{A}_1\otimes\mathcal{A}_2$, $x_1\mapsto\mu_2(E_{x_1})$ is $\mathcal{A}_1$-measurable.
>
> **Hint:** $\pi$–$\lambda$: true on rectangles, $\lambda$-system, generate.
>
> > [!note]- Full proof
> > Assume first $\mu_2$ finite. Let $\mathcal{L}=\{E\in\mathcal{A}:x_1\mapsto\mu_2(E_{x_1})\text{ is measurable}\}$. For a rectangle, $\mu_2((A_1\times A_2)_{x_1})=\mu_2(A_2)\mathbf{1}_{A_1}(x_1)$ — measurable, so $\mathcal{L}$ contains the rectangles, a $\pi$-system generating $\mathcal{A}$. $\mathcal{L}$ is a $\lambda$-system: $X\in\mathcal{L}$; for $E\subseteq F$, $\mu_2((F\setminus E)_{x_1})=\mu_2(F_{x_1})-\mu_2(E_{x_1})$ (finiteness!), measurable; for $E_n\uparrow E$, $\mu_2(E_{x_1})=\lim\mu_2((E_n)_{x_1})$, measurable. By [[Thm - Dynkin's π-λ Theorem|Dynkin]], $\mathcal{L}\supseteq\sigma(\text{rectangles})=\mathcal{A}$. For $\sigma$-finite $\mu_2$, write $X_2=\bigcup Y_m$, $\mu_2(Y_m)<\infty$, apply the finite case to $\mu_2(\cdot\cap Y_m)$, and sum. $\square$

> [!note]- Lemma 2: The slice formula defines a measure
> **Statement:** $\sigma(E)=\int_{X_1}\mu_2(E_{x_1})\,d\mu_1$ is a measure on $\mathcal{A}$ with $\sigma(A_1\times A_2)=\mu_1(A_1)\mu_2(A_2)$.
>
> > [!note]- Full proof
> > Well-defined by Lemma 1. $\sigma(\emptyset)=0$. For disjoint $(E_n)$, $E_{x_1}=\bigsqcup_n(E_n)_{x_1}$, so $\mu_2(E_{x_1})=\sum_n\mu_2((E_n)_{x_1})$ ($\sigma$-additivity of $\mu_2$); the partial sums increase, so [[Thm - Monotone Convergence Theorem|MCT]] gives $\sigma(E)=\int\sum_n\mu_2((E_n)_{x_1})\,d\mu_1=\sum_n\sigma(E_n)$. On a rectangle, $\sigma(A_1\times A_2)=\int\mu_2(A_2)\mathbf{1}_{A_1}\,d\mu_1=\mu_1(A_1)\mu_2(A_2)$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 2 constructs a measure $\mu_1\otimes\mu_2:=\sigma$ with the rectangle normalisation. Uniqueness: the rectangles form a $\pi$-system generating $\mathcal{A}_1\otimes\mathcal{A}_2$; by $\sigma$-finiteness $X$ is a countable union of finite-measure rectangles, so [[Thm - Dynkin's π-λ Theorem|Dynkin's uniqueness corollary]] forces any two measures agreeing on rectangles to agree on $\mathcal{A}$. The symmetric formula $\int\mu_1(E_{x_2})\,d\mu_2$ is another such measure, hence equal. $\lambda_m\otimes\lambda_n=\lambda_{m+n}$: both agree on boxes, a generating $\pi$-system, and are $\sigma$-finite. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The product construction iterates: $\bigotimes_{i\in\mathbb{N}}\mu_i$ builds a measure on an *infinite* product, the home of [[Def - Independence|independent sequences]] of random variables and of the **Kolmogorov extension theorem** — the device that constructs the law of a stochastic process from its finite-dimensional marginals. The simple random walk's law on $\{-1,1\}^{\mathbb{N}}$ is such an infinite product.

---

# Bridges

- **[[Thm - Fubini-Tonelli Theorem]]** — the product measure is the setting; Fubini computes integrals against it as iterated integrals.
- **[[Thm - Dynkin's π-λ Theorem]]** — supplies both the measurability of slices and the uniqueness.
- **[[Def - Independence]]** *(Advanced Probability)* — independence of random variables is "joint law $=$ product of marginal laws."
