---
type: definition
subject: measure-theory
prereqs:
  - "Def - Measurable Function"
  - "Def - Measure and Measure Space"
tags: [analysis, measure-theory]
---

# Notation

$(X,\mathcal{A},\mu)$ is a measure space. $\mathbf{1}_A$ is the indicator of $A$. $s$ denotes a simple function; $\mathcal{S}^+$ the cone of non-negative measurable simple functions.

---

# Axiom Motivation

The Lebesgue integral cannot be defined for a general measurable function in one stroke — there is no formula. It is built, like Lebesgue measure itself, by *defining it on an easy class and extending by approximation*. The easy class is the **simple functions**: measurable functions taking only finitely many values.

Why finitely many values? Because for such a function the integral writes itself. If $s$ takes value $\alpha_i$ on the measurable set $A_i$, the "area under $s$" is unambiguously $\sum_i\alpha_i\mu(A_i)$ — a finite sum of (value)$\times$(measure), no limiting process. Simple functions are to integration what [[Def - Interval and Elementary Figure|elementary figures]] are to measure: the hand-computable building blocks on which the theory is *defined* before any limit.

The pair of facts that make them the right class: simple functions are closed under the algebraic operations (sums, products, max, min), and — decisively — *every* non-negative measurable function is an increasing pointwise limit of simple functions ([[Thm - Approximation by Simple Functions]]). So "define the integral on simple functions, then take limits" reaches every measurable function. The key contrast with Riemann's step functions: Lebesgue's simple functions partition the *range* (level sets $\{s=\alpha_i\}$, which can be arbitrarily wild measurable sets) rather than the *domain* (intervals). Partitioning the range is what lets the integral handle discontinuous functions and commute with limits.

---

# The Definition

A function $s:X\to\mathbb{R}$ is **simple** if its image $s(X)$ is a finite set. Writing the distinct values as $\alpha_1,\dots,\alpha_\ell$ and $A_i=s^{-1}(\{\alpha_i\})$, every simple function has the **canonical representation**
$$s=\sum_{i=1}^\ell\alpha_i\,\mathbf{1}_{A_i},\qquad X=\bigsqcup_{i=1}^\ell A_i.$$
$s$ is **measurable** iff each $A_i\in\mathcal{A}$. The cone of non-negative measurable simple functions is
$$\mathcal{S}^+=\{s:X\to[0,\infty) : s\text{ simple, measurable}\}.$$
A representation $s=\sum_i\alpha_i\mathbf{1}_{A_i}$ with $\alpha_i\ge0$ and $A_i\in\mathcal{A}$ disjoint is called *a* representation (not unique — values may be repeated or sets split); the canonical one uses the *distinct* values.

---

# Relate to Other Fields / Compression

Simple functions generalise the **step functions** of the Riemann integral by one decisive change: the pieces $A_i$ are arbitrary measurable sets, not intervals. Riemann partitions the domain; Lebesgue partitions the range. This is the difference that lets the Lebesgue integral handle $\mathbf{1}_\mathbb{Q}$ and commute with limits. In probability a simple function is a **discrete random variable** taking finitely many values, and $\sum\alpha_i\mu(A_i)$ is its expectation $\sum\alpha_i\mathbb{P}(A_i)$ — expectation of a discrete variable is the simple-function integral.

---

# Examples / Corollaries

The indicator $\mathbf{1}_A$ ($A\in\mathcal{A}$) is simple with values $\{0,1\}$. Any finite real combination of indicators of measurable sets is a simple function. The function $\varphi_n(t)=k2^{-n}$ for $t\in[k2^{-n},(k+1)2^{-n})$, capped at $n$, is the simple function used to approximate $f\ge0$ from below ([[Thm - Approximation by Simple Functions]]).

Closure: if $s,s'$ are measurable simple, so are $s+s'$, $ss'$, $s\wedge s'$, $s\vee s'$, $\alpha s$ — each takes finitely many values and has measurable level sets.

Calibration: (i) Is $\mathbf{1}_\mathbb{Q}$ simple? Yes — values $\{0,1\}$, level sets $\mathbb{Q},\mathbb{R}\setminus\mathbb{Q}$ both Borel. (ii) Is $x\mapsto\lfloor x\rfloor$ on $\mathbb{R}$ simple? No — infinitely many values (though it is measurable and simple on each bounded set). (iii) Is the canonical representation unique? Yes — but non-canonical representations (repeating a value, or splitting an $A_i$) are not, which is why $\int s\,d\mu$ must be checked independent of representation.

---

# Unlocked by This

> [!tip] The integral, built in three steps *(from [[Measure Theory II — Integration|Measure Theory II]])*
> $\int s\,d\mu=\sum\alpha_i\mu(A_i)$ for simple $s\ge0$; then $\int f\,d\mu=\sup\{\int s\,d\mu:s\le f\}$ for $f\ge0$; then $\int f=\int f^+-\int f^-$ for integrable $f$. See [[Def - The Integral]].
