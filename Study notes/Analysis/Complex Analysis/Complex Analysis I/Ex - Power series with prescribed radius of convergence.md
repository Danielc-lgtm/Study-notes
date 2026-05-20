---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Power Series and Radius of Convergence"
  - "Thm - Radius of Convergence Formula and Uniform Convergence on Sub-Discs"
tags: [analysis, complex-analysis]
---

# Problem Statement

For each value $R \in [0, \infty]$, exhibit a power series $\sum c_n z^n$ with radius of convergence *exactly* $R$. Specifically:

(a) $R = 0$.

(b) $R = 1$.

(c) $R = R_0$ for an arbitrary $R_0 \in (0, \infty)$.

(d) $R = \infty$.

**Recall:**

The [[Def - Power Series and Radius of Convergence|radius of convergence]] is $R = 1/\limsup |c_n|^{1/n}$. To get a specific radius, choose coefficients with the appropriate growth rate: $|c_n|$ growing like $1/R^n$ gives radius $R$.

---

# Convergent Strategy

**Problem class:** Constructive — for each prescribed radius, exhibit explicit coefficients.

**Assumption pattern:** Free choice of $c_n$.

**Theorem routing:** The radius formula $R = 1/\limsup |c_n|^{1/n}$ tells us: if $|c_n|^{1/n} \to 1/R$, then radius is $R$. So we need $|c_n|$ to grow like $1/R^n$.

**Key decision point:** The cleanest choice is $c_n = 1/R^n$ for finite positive $R$ (giving $\sum z^n/R^n = R/(R-z)$), $c_n = 1/n!$ for $R = \infty$, and $c_n = n!$ for $R = 0$.

---

# Legal Operations Used

1. **Engineer the coefficient growth rate** so $|c_n|^{1/n} \to 1/R$.
2. **Recognize** the resulting series as a known function (geometric series, exponential, etc.) where possible.

---

# Hints

> [!note]- Hint 1
> For positive finite $R$, scale the geometric series: $\sum (z/R)^n = \sum z^n/R^n$. By geometric series, this converges for $|z/R| < 1$, i.e., $|z| < R$.

> [!note]- Hint 2
> For $R = \infty$, take coefficients decaying faster than any geometric, e.g., $1/n!$.

> [!note]- Hint 3
> For $R = 0$, take coefficients growing faster than any geometric, e.g., $n!$.

---

# Solution

**(a) $R = 0$.**

Take $c_n = n!$ — that is, $\sum_{n=0}^\infty n! z^n$.

> [!note]- Verification
> By Stirling, $(n!)^{1/n} \sim n/e \to \infty$. So $|c_n|^{1/n} \to \infty$ and $R = 1/\infty = 0$. Equivalently, the ratio test: $|c_{n+1}/c_n| = n + 1 \to \infty$, so $|z| < 0$ for convergence, i.e., the series converges only at $z = 0$.

**(b) $R = 1$.**

Take the geometric series $\sum_{n=0}^\infty z^n = 1/(1-z)$ on $|z| < 1$.

> [!note]- Verification
> $|c_n|^{1/n} = 1$, so $R = 1$.

**(c) $R = R_0$ for arbitrary $R_0 \in (0, \infty)$.**

Take $c_n = 1/R_0^n$ — that is, $\sum_{n=0}^\infty z^n/R_0^n = \sum (z/R_0)^n$.

> [!note]- Verification
> $|c_n|^{1/n} = 1/R_0$, so $R = R_0$.
>
> *Closed form:* this is the geometric series in $z/R_0$, summing to $1/(1 - z/R_0) = R_0/(R_0 - z)$ on $|z| < R_0$.

**(d) $R = \infty$.**

Take $c_n = 1/n!$ — the exponential series $\sum z^n/n!$.

> [!note]- Verification
> $(n!)^{1/n} \to \infty$ by Stirling, so $|c_n|^{1/n} = 1/(n!)^{1/n} \to 0$ and $R = 1/0 = \infty$.

> [!note]- Complete formal solution
> Choose $c_n$ so $|c_n|^{1/n} \to 1/R$:
>
> **(a) $R = 0$:** $c_n = n!$; $|c_n|^{1/n} \to \infty$; $R = 0$.
>
> **(b) $R = 1$:** $c_n = 1$; $|c_n|^{1/n} = 1$; $R = 1$.
>
> **(c) $R = R_0 \in (0, \infty)$:** $c_n = 1/R_0^n$; $|c_n|^{1/n} = 1/R_0$; $R = R_0$. (Closed form $R_0/(R_0 - z)$ on $|z| < R_0$.)
>
> **(d) $R = \infty$:** $c_n = 1/n!$; $|c_n|^{1/n} \to 0$; $R = \infty$. (Closed form $e^z$ on $\mathbb{C}$.)
>
> Every $R \in [0, \infty]$ is achieved by some explicit power series. $\blacksquare$

---

# Key Takeaways

**The radius is just a coefficient growth rate translated.**

The relationship $R = 1/\limsup |c_n|^{1/n}$ converts "rate of decay/growth of $|c_n|$" into "size of disc". Slow decay (or growth) — like $1/n^k$ — gives radius $1$. Geometric decay $1/R_0^n$ gives radius $R_0$. Super-geometric decay $1/n!$ gives radius $\infty$. Super-geometric growth $n!$ gives radius $0$. The exercise drills the bijection.

**Engineering examples by scaling.**

Once you have a series with one radius, you can scale to get any other: $\sum c_n z^n$ has radius $R$ iff $\sum c_n (z/k)^n$ has radius $kR$. Substituting $w = z/k$ rescales the convergence disc. This is a useful trick for adapting standard series to non-standard radii.

**The "all radii are achieved" lesson.**

A function-of-radius perspective: there is no "preferred" radius — the entire interval $[0, \infty]$ is achieved by some power series. This is part of why the boundary $|z| = R$ is genuinely subtle: it depends on the specific series, not on $R$ alone.
