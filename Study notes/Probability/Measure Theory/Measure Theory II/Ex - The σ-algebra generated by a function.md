---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Measurable Function"
  - "Thm - Approximation by Simple Functions"
tags: [analysis, measure-theory, probability]
---

# Problem Statement

Let $(X,\mathcal{A})$ be a measurable space and $f:X\to\mathbb{R}$ measurable. Recall $\sigma(f)=\{f^{-1}(B):B\in\mathcal{B}(\mathbb{R})\}$, the smallest $\sigma$-algebra making $f$ measurable.

**(a)** Show $\sigma(f)$ is a $\sigma$-algebra and $f$ is $\sigma(f)$-measurable.

**(b) (Doob–Dynkin lemma.)** Show that a function $g:X\to\mathbb{R}$ is $\sigma(f)$-measurable **if and only if** $g=h\circ f$ for some Borel function $h:\mathbb{R}\to\mathbb{R}$.

**(c)** Interpret in probability: a random variable $g$ is "a function of $f$" exactly when it is $\sigma(f)$-measurable. This is the foundation of [[Def - Conditional Expectation|conditional expectation]] "$\mathbb{E}[Y\mid X]=h(X)$."

**Recall:**

A function is [[Def - Measurable Function|measurable]] if preimages of Borel sets are measurable. [[Thm - Approximation by Simple Functions|Every]] measurable function is a pointwise limit of [[Def - Simple Function|simple functions]].

---

# Convergent Strategy

**Problem class:** characterising measurability with respect to a *function-generated* $\sigma$-algebra in terms of "being a function of."

**Assumption pattern:** $\sigma(f)$-measurability means $g$'s level sets are *built from $f$'s level sets*. The natural way to manufacture "a function of $f$" is the [[Thm - Approximation by Simple Functions|standard machine]]: prove it for indicators, then simple functions, then limits.

**Theorem routing:** indicator of a $\sigma(f)$-set is $\mathbf{1}_{f^{-1}(B)}=\mathbf{1}_B\circ f$; linear combinations give simple functions $=$ (simple)$\circ f$; pointwise limits give general $g=h\circ f$.

**Key decision point:** the limit step — the $h$ for $g=\lim g_n$ is $h=\lim h_n$ *where the limit exists*, and one must handle the set where it does not.

---

# Legal Operations Used

1. **The standard machine** — indicators → simple → limits.
2. **Composition of measurable maps is measurable.**
3. **Restrict a limit to its convergence set** (a Borel set).

---

# Hints

> [!note]- Hint 1
> "$\Leftarrow$" is easy: if $g=h\circ f$ with $h$ Borel, $g$ is a composition of measurable maps.

> [!note]- Hint 2
> "$\Rightarrow$": first do $g=\mathbf{1}_A$ with $A\in\sigma(f)$. By definition $A=f^{-1}(B)$, so $\mathbf{1}_A=\mathbf{1}_B\circ f$.

> [!note]- Hint 3
> Extend by linearity to simple $g$, then take $g=\lim g_n$ with $g_n$ simple; let $h=\lim h_n$ on the set where it converges, $0$ elsewhere.

---

# Solution

**Step 1 — (a).** $\sigma(f)$ is a $\sigma$-algebra (preimage of a $\sigma$-algebra under a fixed map), and $f$ is $\sigma(f)$-measurable by construction: $f^{-1}(B)\in\sigma(f)$ for every Borel $B$.

**Step 2 — (b), "$\Leftarrow$".** If $g=h\circ f$ with $h$ Borel, then for Borel $B$, $g^{-1}(B)=f^{-1}(h^{-1}(B))\in\sigma(f)$ since $h^{-1}(B)$ is Borel. So $g$ is $\sigma(f)$-measurable.

**Step 3 — (b), "$\Rightarrow$".** Let $g$ be $\sigma(f)$-measurable. Run the standard machine.

> [!note]- Derivation
> *Indicators.* If $g=\mathbf{1}_A$, $A\in\sigma(f)$, then $A=f^{-1}(B)$ for some Borel $B$, so $g=\mathbf{1}_{f^{-1}(B)}=\mathbf{1}_B\circ f$ — take $h=\mathbf{1}_B$, Borel.
> *Simple functions.* If $g=\sum_i\alpha_i\mathbf{1}_{A_i}$ with $A_i=f^{-1}(B_i)\in\sigma(f)$, then $g=(\sum_i\alpha_i\mathbf{1}_{B_i})\circ f$ — take $h=\sum_i\alpha_i\mathbf{1}_{B_i}$, Borel.
> *General $g$.* By [[Thm - Approximation by Simple Functions]] there are $\sigma(f)$-measurable simple $g_n\to g$ pointwise; write $g_n=h_n\circ f$ with $h_n$ Borel. Let $D=\{y\in\mathbb{R}:\lim_n h_n(y)\text{ exists}\}$ — a Borel set ([[Thm - Operations Preserve Measurability]]) — and set $h=\lim_n h_n$ on $D$, $h=0$ off $D$; $h$ is Borel. For every $x$, $h_n(f(x))=g_n(x)\to g(x)$, so $f(x)\in D$ and $h(f(x))=g(x)$. Thus $g=h\circ f$.

**Step 4 — (c).** A $\sigma(f)$-measurable random variable is, by (b), exactly an $h(f)$ — "a deterministic function of $f$." This is why the conditional expectation $\mathbb{E}[Y\mid X]$, being $\sigma(X)$-measurable, must have the form $h(X)$, and one writes $\mathbb{E}[Y\mid X=x]=h(x)$.

> [!note]- Complete formal solution
> (a) $\sigma(f)=f^{-1}(\mathcal{B}(\mathbb{R}))$ is a $\sigma$-algebra and makes $f$ measurable. (b) "$\Leftarrow$": $g^{-1}(B)=f^{-1}(h^{-1}(B))\in\sigma(f)$. "$\Rightarrow$": for indicators $\mathbf{1}_{f^{-1}(B)}=\mathbf{1}_B\circ f$; extend linearly to simple functions; for general $g$, approximate by simple $g_n=h_n\circ f$, set $h=\lim h_n$ on its (Borel) convergence set and $0$ elsewhere — then $g=h\circ f$. (c) $\sigma(f)$-measurable $=$ "a function of $f$," whence $\mathbb{E}[Y\mid X]=h(X)$. $\blacksquare$

---

# Key Takeaways

**$\sigma(f)$ is exactly "the information in $f$": a quantity is $\sigma(f)$-measurable iff it is a deterministic function of $f$.** This is the Doob–Dynkin lemma, and it gives $\sigma$-algebras their information-theoretic meaning — $\sigma(f)$ is everything decidable by observing $f$ alone, no more. The proof is the [[Thm - Approximation by Simple Functions|standard machine]]: establish the claim for indicators (trivial — a $\sigma(f)$-set *is* an $f$-preimage), lift by linearity to simple functions, lift by pointwise limits to all measurable functions.

**This is the structural fact that makes [[Def - Conditional Expectation|conditional expectation]] "a function of the conditioning variable."** Because $\mathbb{E}[Y\mid X]$ is required to be $\sigma(X)$-measurable, the Doob–Dynkin lemma forces it to equal $h(X)$ for some Borel $h$ — which is what licenses the everyday notation $\mathbb{E}[Y\mid X=x]=h(x)$ even when $\mathbb{P}(X=x)=0$. The same lemma underlies the notion of a *statistic* and of *measurability with respect to a filtration*.
