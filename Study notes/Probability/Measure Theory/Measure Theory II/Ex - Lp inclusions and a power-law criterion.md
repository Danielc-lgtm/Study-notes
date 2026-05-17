---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Lp Spaces"
  - "Thm - Hölder and Minkowski Inequalities"
tags: [analysis, measure-theory]
---

# Problem Statement

**(a)** Let $\mu(X)<\infty$ and $1\le p\le p'\le\infty$. Show $L^{p'}(\mu)\subseteq L^p(\mu)$, with $\|f\|_p\le\mu(X)^{1/p-1/p'}\|f\|_{p'}$.

**(b)** On $(\mathbb{N},\#)$ with counting measure show the *reverse* inclusion: $\ell^p\subseteq\ell^{p'}$ for $p\le p'$.

**(c)** On $([-1,1],\lambda)$ determine for which $p$ the function $f(x)=|x|^{-\alpha}$ ($\alpha>0$) lies in $L^p$.

**Recall:**

$\|f\|_p=(\int|f|^p\,d\mu)^{1/p}$; [[Thm - Hölder and Minkowski Inequalities|Hölder]]: $\int|fg|\le\|f\|_r\|g\|_s$ for $\tfrac1r+\tfrac1s=1$.

---

# Convergent Strategy

**Problem class:** comparing $L^p$ spaces for different $p$ — the inclusions go *opposite ways* on finite-measure vs. counting-measure spaces.

**Assumption pattern:** (a) finite measure — a higher power $|f|^{p'}$ controls a lower one $|f|^p$ *up to a factor of $\mu(X)$*, extracted by Hölder. (b) counting measure — summability of $|a_n|^p$ forces $a_n\to0$, so $|a_n|^{p'}\le|a_n|^p$ eventually. (c) a power-law singularity — integrate $|x|^{-\alpha p}$ directly.

**Theorem routing:** (a) Hölder with exponents $p'/p$ and its conjugate; (b) elementary; (c) $\int|x|^{-\alpha p}$ is a $p$-integral.

**Key decision point:** which direction the inclusion goes is governed entirely by whether the space has finite or infinite "many small atoms" structure.

---

# Legal Operations Used

1. **Hölder to compare powers** on a finite-measure space.
2. **Summability forces decay** on a discrete space.
3. **Direct integration** of a power-law singularity.

---

# Hints

> [!note]- Hint 1
> (a): $\int|f|^p\,d\mu=\int|f|^p\cdot1\,d\mu$. Apply Hölder with exponents $p'/p$ and its conjugate to the pair $(|f|^p,1)$.

> [!note]- Hint 2
> (b): if $\sum|a_n|^p<\infty$ then $|a_n|\to0$, so $|a_n|\le1$ eventually, whence $|a_n|^{p'}\le|a_n|^p$.

> [!note]- Hint 3
> (c): $\|f\|_p^p=\int_{-1}^1|x|^{-\alpha p}\,dx=2\int_0^1 x^{-\alpha p}\,dx$, finite iff $\alpha p<1$.

---

# Solution

**Step 1 — (a) Finite measure: $L^{p'}\subseteq L^p$.** Assume $p<p'<\infty$ (the case $p'=\infty$ is direct: $|f|\le\|f\|_\infty$, so $\int|f|^p\le\|f\|_\infty^p\mu(X)$). Apply [[Thm - Hölder and Minkowski Inequalities|Hölder]] to $|f|^p$ and $1$ with exponents $r=p'/p>1$ and $s=r/(r-1)$:
$$\int|f|^p\,d\mu=\int|f|^p\cdot1\,d\mu\le\big\||f|^p\big\|_r\,\|1\|_s=\Big(\int|f|^{p'}\Big)^{p/p'}\mu(X)^{1/s}.$$
Since $1/s=1-p/p'$, raising to the $1/p$: $\|f\|_p\le\|f\|_{p'}\,\mu(X)^{(1-p/p')/p}=\mu(X)^{1/p-1/p'}\|f\|_{p'}$. So $f\in L^{p'}\Rightarrow f\in L^p$.

**Step 2 — (b) Counting measure: $\ell^p\subseteq\ell^{p'}$.** Let $a\in\ell^p$, $p\le p'$. Then $\sum_n|a_n|^p<\infty$ forces $|a_n|\to0$, so $|a_n|\le1$ for all $n\ge N$. For such $n$, $|a_n|^{p'}\le|a_n|^p$ (raising a number $\le1$ to a larger power decreases it). Hence $\sum_n|a_n|^{p'}\le\sum_{n<N}|a_n|^{p'}+\sum_{n\ge N}|a_n|^p<\infty$, i.e. $a\in\ell^{p'}$.

> [!note]- Derivation
> The inclusions are *opposite*: finite measure gives $L^{p'}\subseteq L^p$ (high $p$ inside low $p$), counting measure gives $\ell^p\subseteq\ell^{p'}$ (low $p$ inside high $p$). On a finite-measure space the "danger" is large values, controlled by high exponents; on $\mathbb{N}$ the danger is slow decay, controlled by low exponents. On a general space (e.g. $\mathbb{R}$) *neither* inclusion holds.

**Step 3 — (c) The power-law singularity.** For $1\le p<\infty$,
$$\|f\|_p^p=\int_{-1}^1|x|^{-\alpha p}\,d\lambda=2\int_0^1 x^{-\alpha p}\,dx.$$
The integral $\int_0^1 x^{-\beta}\,dx$ converges iff $\beta<1$. So $\|f\|_p<\infty\iff\alpha p<1\iff p<1/\alpha$. Thus $f=|x|^{-\alpha}\in L^p([-1,1])$ **iff $p<1/\alpha$** (for $p=\infty$, $f\notin L^\infty$ as it is unbounded). The more severe the singularity (larger $\alpha$), the smaller the range of admissible $p$.

> [!note]- Complete formal solution
> (a) Hölder on $(|f|^p,1)$ with exponents $p'/p,\;(p'/p)'$ gives $\int|f|^p\le(\int|f|^{p'})^{p/p'}\mu(X)^{1-p/p'}$, so $\|f\|_p\le\mu(X)^{1/p-1/p'}\|f\|_{p'}$. (b) $a\in\ell^p\Rightarrow|a_n|\to0\Rightarrow|a_n|\le1$ eventually $\Rightarrow|a_n|^{p'}\le|a_n|^p$, summable. (c) $\|f\|_p^p=2\int_0^1 x^{-\alpha p}dx<\infty\iff\alpha p<1\iff p<1/\alpha$. $\blacksquare$

---

# Key Takeaways

**The $L^p$ inclusions run in *opposite directions* on finite-measure and on counting-measure spaces — and in *neither* direction in general.** On a probability space (or any $\mu(X)<\infty$), $L^{p'}\subseteq L^p$ for $p\le p'$: higher moments control lower ones, so "$X$ has a finite $p'$-th moment" is a *stronger* statement. On $\mathbb{N}$, $\ell^p\subseteq\ell^{p'}$: smaller $p$ is the stronger summability. The mechanism is whether the obstruction is *large values* (finite measure — beaten by high exponents) or *slow decay* (counting measure — beaten by low exponents). Knowing which space you are on tells you instantly which way moment inequalities point.

**A power-law singularity $|x|^{-\alpha}$ is in $L^p$ precisely when $\alpha p<1$ — integrability is a contest between singularity strength and exponent.** This $p<1/\alpha$ criterion is the prototype computation for membership in $L^p$, and the same arithmetic ($\int x^{-\beta}$ converges iff $\beta<1$ near $0$, iff $\beta>1$ near $\infty$) decides integrability of every algebraic singularity or tail. It is why a function can lie in $L^1$ but not $L^2$, or vice versa, and why specifying *which* $L^p$ a function belongs to is genuine information.
