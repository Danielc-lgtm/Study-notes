---
type: definition
subject: measure-theory
prereqs:
  - "Def - Simple Function"
  - "Def - Measurable Function"
  - "Def - Almost Everywhere"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X,\mathcal{A},\mu)$ a measure space; $\mathcal{S}^+$ the cone of non-negative measurable [[Def - Simple Function|simple functions]]. $\int f\,d\mu$, $\mu(f)$ — the integral of $f$. $f^+=\max(f,0)$, $f^-=\max(-f,0)$, $|f|=f^++f^-$.

---

# Axiom Motivation

We want to integrate every measurable function against a measure. There is no single formula, so the integral is built in **three steps**, each forced by the previous one's limitation.

*Step 1 — simple functions.* For $s=\sum\alpha_i\mathbf{1}_{A_i}\in\mathcal{S}^+$ the integral must be $\sum\alpha_i\mu(A_i)$ — value times measure, summed. Nothing else is consistent with "integral of an indicator $=$ measure of the set" plus additivity. The only thing to check is that this does not depend on the (non-unique) representation; it does not, by finite additivity of $\mu$.

*Step 2 — non-negative functions.* A general $f\ge0$ is approximated *from below* by simple functions ([[Thm - Approximation by Simple Functions]]). Its integral must be at least $\int s\,d\mu$ for every simple $s\le f$, and there is no reason to make it larger, so
$$\int f\,d\mu=\sup\Big\{\int s\,d\mu:s\in\mathcal{S}^+,\ s\le f\Big\}.$$
Approximation *from below* (not above) is the deliberate choice that makes the integral interact correctly with *increasing* limits — it is what powers the [[Thm - Monotone Convergence Theorem|monotone convergence theorem]]. The integral of $f\ge0$ always exists in $[0,\infty]$; it may be $+\infty$.

*Step 3 — signed functions.* For $f$ of either sign, split $f=f^+-f^-$ into non-negative parts and set $\int f=\int f^+-\int f^-$. This is meaningful only when the subtraction avoids "$\infty-\infty$" — hence one demands $\int|f|\,d\mu<\infty$, the definition of **integrability**. Integrability is exactly the condition "$|f|$ has finite area," and it is what makes the signed integral well-defined and linear.

The whole construction mirrors the construction of [[Def - Lebesgue Measure|Lebesgue measure]]: define on an easy class (simple functions / elementary figures), extend by a monotone limiting process, handle signs last.

---

# The Definition

Let $(X,\mathcal{A},\mu)$ be a measure space.

**Step 1.** For $s=\sum_{i=1}^\ell\alpha_i\mathbf{1}_{A_i}\in\mathcal{S}^+$,
$$\int s\,d\mu=\sum_{i=1}^\ell\alpha_i\,\mu(A_i)\ \in[0,\infty].$$
This is independent of the representation chosen.

**Step 2.** For measurable $f:X\to[0,\infty]$,
$$\int f\,d\mu=\sup\Big\{\int s\,d\mu:s\in\mathcal{S}^+,\ s\le f\Big\}\ \in[0,\infty].$$

**Step 3.** A measurable $f:X\to[-\infty,\infty]$ is **$\mu$-integrable** if $\int|f|\,d\mu<\infty$; the set of such $f$ is $L^1(\mu)$. For $f\in L^1(\mu)$,
$$\int f\,d\mu=\int f^+\,d\mu-\int f^-\,d\mu,$$
a difference of two finite non-negative numbers. For $A\in\mathcal{A}$, $\int_A f\,d\mu:=\int f\,\mathbf{1}_A\,d\mu$.

When $\mu=\mathbb{P}$ is a probability measure, $\int f\,d\mathbb{P}$ is written $\mathbb{E}[f]$, the **expectation**.

---

# Categorical Definition

Integration against $\mu$ is the *unique* functional $L^1(\mu)\to\mathbb{R}$ that is **linear**, **monotone** ($f\le g\Rightarrow\int f\le\int g$), **monotone-continuous** ($f_n\uparrow f\Rightarrow\int f_n\uparrow\int f$, [[Thm - Monotone Convergence Theorem|MCT]]), and **normalised** ($\int\mathbf{1}_A=\mu(A)$). These four properties characterise it — and conversely, by the Riesz representation theorem, suitable such functionals *are* integration against a measure. Measure and integral are two faces of one object.

---

# Relate to Other Fields / Compression

The Lebesgue integral against $\lambda$ **extends the Riemann integral**: every Riemann-integrable $f$ on $[a,b]$ is Lebesgue-integrable with the same value, but $\mathbf{1}_\mathbb{Q}$ is Lebesgue-integrable ($\int=0$) and not Riemann-integrable. Against [[Def - Measure and Measure Space|counting measure]] on $\mathbb{N}$ the integral *is* the series $\sum a_n$ — so series are a special case of integration, and the [[Thm - Dominated Convergence Theorem|convergence theorems]] become theorems about interchanging sum and limit. Against a probability measure it is **expectation**; against a [[Def - Absolute Continuity and Density|measure with density]] $f\mu$ it computes weighted averages.

---

# Examples / Corollaries

$\int\mathbf{1}_A\,d\mu=\mu(A)$. $\int\mathbf{1}_\mathbb{Q}\,d\lambda=0$ (it equals $0$ a.e.). On $(\mathbb{N},2^\mathbb{N},\#)$, $\int a\,d\#=\sum_n a_n$ and $L^1=\ell^1$. The geometric law on $\mathbb{N}$, $\mathbb{P}(\{k\})=(1-p)^{k-1}p$, has $\mathbb{E}[X]=\sum_k k(1-p)^{k-1}p=1/p$.

Two consistency facts: Step 2 agrees with Step 1 on $\mathcal{S}^+$; and $f=0$ a.e. $\iff\int f\,d\mu=0$ for $f\ge0$. If $\int f\,d\mu<\infty$ then $f<\infty$ a.e.

Calibration: (i) Does $\int f\,d\mu$ exist for every $f\ge0$? Yes — possibly $+\infty$. (ii) For signed $f$? Only if $\int|f|<\infty$. (iii) If $f=g$ a.e., are the integrals equal? Yes — the integral ignores null sets.

---

# Unlocked by This

> [!tip] Expectation *(from [[Advanced Probability I — Probability Spaces and Random Variables|Advanced Probability]])*
> For a [[Def - Random Variable|random variable]] $X$ on $(\Omega,\mathcal{F},\mathbb{P})$, $\mathbb{E}[X]=\int X\,d\mathbb{P}$. All of expectation, variance, moments, and — via the [[Thm - Radon-Nikodym Theorem|Radon–Nikodym theorem]] — [[Def - Conditional Expectation|conditional expectation]] are built on this integral.

> [!tip] $L^p$ spaces
> $\int|f|^p\,d\mu$ defines the [[Def - Lp Spaces|Lᵖ norm]]; the integral is the engine of the entire $L^p$ theory.
