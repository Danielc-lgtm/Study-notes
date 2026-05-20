---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)"
  - "Def - Branch of the Logarithm"
  - "Thm - Power Series is Holomorphic with Termwise Derivative"
tags: [analysis, complex-analysis]
---

# Problem Statement

Find the power series expansion of $f(z) = \operatorname{Log}(1 + z)$ around $z = 0$, where $\operatorname{Log}$ is the principal branch of the logarithm. Identify the radius of convergence and verify by termwise differentiation.

**Recall:**

[[Def - Branch of the Logarithm|Principal branch]] $\operatorname{Log}$ is defined on $\mathbb{C} \setminus (-\infty, 0]$. The function $f(z) = \operatorname{Log}(1 + z)$ is defined for $z$ such that $1 + z \in \mathbb{C} \setminus (-\infty, 0]$, i.e., $1 + z \notin (-\infty, 0]$, i.e., $z \notin (-\infty, -1]$. So $f$ is holomorphic on the open set $\mathbb{C} \setminus (-\infty, -1]$, which contains the open disc $|z| < 1$.

[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]: on a disc, every holomorphic function is its Taylor series.

---

# Convergent Strategy

**Problem class:** Compute a Taylor series via differentiation, or via termwise integration of a known series.

**Assumption pattern:** $f(z) = \operatorname{Log}(1 + z)$ has $f'(z) = 1/(1 + z)$, a known geometric-series function.

**Theorem routing:** Compute $f'(z) = 1/(1 + z) = \sum (-z)^n$ on $|z| < 1$. Integrate termwise (legitimate by [[Thm - Power Series is Holomorphic with Termwise Derivative]] applied to the integrated series). Apply $f(0) = 0$.

**Key decision point:** Recognizing that integrating a power series term-by-term gives the antiderivative power series, but the constant of integration is fixed by $f(0) = \operatorname{Log}(1) = 0$.

---

# Legal Operations Used

1. **Differentiate:** $f'(z) = 1/(1 + z)$ (chain rule, with $\operatorname{Log}'(w) = 1/w$).
2. **Expand $1/(1 + z)$ as a geometric series.** $1/(1 + z) = \sum_{n=0}^\infty (-z)^n = \sum (-1)^n z^n$ on $|z| < 1$.
3. **Integrate termwise.** Each $(-1)^n z^n$ integrates to $(-1)^n z^{n+1}/(n+1)$, plus a constant determined by $f(0) = 0$.
4. **Identify the radius of convergence.** Distance from $0$ to the nearest non-holomorphicity: at $z = -1$, the argument $1 + z = 0$, on the boundary of the principal branch's domain. So radius $= 1$.

---

# Hints

> [!note]- Hint 1
> Differentiate: $f'(z) = 1/(1+z)$. Expand as a geometric series. Then integrate termwise.

> [!note]- Hint 2
> Integration: $\int (-1)^n z^n\,dz = (-1)^n z^{n+1}/(n+1)$. Adjust the constant of integration so $f(0) = 0$.

---

# Solution

**Step 1: Differentiate.**

By the chain rule and $\operatorname{Log}'(w) = 1/w$:
$$f'(z) = \frac{1}{1 + z} \cdot 1 = \frac{1}{1 + z}.$$

**Step 2: Expand as a geometric series.**

$$\frac{1}{1 + z} = \frac{1}{1 - (-z)} = \sum_{n=0}^\infty (-z)^n = \sum_{n=0}^\infty (-1)^n z^n, \quad |z| < 1.$$

**Step 3: Integrate termwise.**

By [[Thm - Power Series is Holomorphic with Termwise Derivative]] (specifically, by the existence of the antiderivative power series with the same radius), there is a power series $F(z) = \sum a_n z^n$ on $|z| < 1$ with $F'(z) = f'(z)$, and $F$ is determined up to a constant.

Term-by-term integration of $\sum (-1)^n z^n$ gives $\sum (-1)^n z^{n+1}/(n+1) = \sum_{n=1}^\infty (-1)^{n-1} z^n/n$ (re-indexing).

Check: differentiate $\sum (-1)^{n-1} z^n/n$ term by term: $\sum (-1)^{n-1} z^{n-1} = \sum_{m=0}^\infty (-1)^m z^m = 1/(1+z)$. ✓

**Step 4: Fix the constant.**

The general solution is $F(z) = \sum_{n=1}^\infty (-1)^{n-1} z^n/n + C$ for some constant $C$. We require $F(0) = f(0) = \operatorname{Log}(1) = 0$. Substituting $z = 0$: $F(0) = 0 + C = 0$, so $C = 0$.

**Step 5: Conclude.**

$$\operatorname{Log}(1 + z) = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} z^n = z - \frac{z^2}{2} + \frac{z^3}{3} - \frac{z^4}{4} + \ldots, \quad |z| < 1.$$

**Step 6: Radius of convergence.**

$|c_n|^{1/n} = (1/n)^{1/n} \to 1$, so $R = 1$. Geometrically: $f(z) = \operatorname{Log}(1 + z)$ has the singularity (boundary of the principal branch) at $z = -1$, distance $1$ from $0$. So radius equals this distance, consistent with the structural fact "radius = distance to nearest singularity".

> [!note]- Complete formal solution
> $f(z) = \operatorname{Log}(1+z)$ has $f'(z) = 1/(1+z) = \sum (-1)^n z^n$ on $|z| < 1$. Termwise integrate: $\sum (-1)^n z^{n+1}/(n+1) = \sum_{n \geq 1} (-1)^{n-1} z^n/n$. Constant determined by $f(0) = 0$. So
> $$\operatorname{Log}(1+z) = z - z^2/2 + z^3/3 - z^4/4 + \ldots = \sum_{n=1}^\infty (-1)^{n-1} z^n/n, \quad |z| < 1.$$
> Radius $= 1$, equal to the distance from $0$ to the singularity at $z = -1$. $\blacksquare$

---

# Key Takeaways

**Differentiate-expand-integrate is the standard pattern.**

For functions whose derivative has a known power series (geometric, $1/(1 + z^2)$, etc.), the Taylor series is obtained by differentiating, expanding, integrating term-by-term, and fixing the constant. This trio recovers:
- $\operatorname{Log}(1+z) = \sum (-1)^{n-1} z^n/n$ from $1/(1+z)$;
- $\arctan z = \sum (-1)^n z^{2n+1}/(2n+1)$ from $1/(1+z^2) = \sum (-z^2)^n$;
- $\arcsin z$ from $1/\sqrt{1-z^2}$ (with binomial series).

The cleanest examples involve simple algebraic singularities at the boundary of the disc of convergence.

**Convergence at the boundary is subtle.**

At $z = 1$ (boundary), the series $\sum (-1)^{n-1}/n = 1 - 1/2 + 1/3 - \ldots = \operatorname{Log} 2$ converges conditionally to $\operatorname{Log} 2$ by Abel's theorem (boundary convergence + continuity at boundary points outside the cut). At $z = -1$, the series $\sum (-1)^{n-1}(-1)^n/n = -\sum 1/n$ is the harmonic series, divergent — consistent with the singularity there.

**Constant of integration matters.**

When integrating a power series term-by-term to recover a function whose derivative we know, the constant of integration is determined by *one value* of the function. For functions defined via $\operatorname{Log}$, the natural choice is $\operatorname{Log}(1) = 0$, fixing the constant to $0$. For other branches, the constant shifts by $2\pi i k$.
