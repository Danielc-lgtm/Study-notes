---
type: exercise
subject: complex-analysis
difficulty: "⭐"
prereqs:
  - "Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)"
tags: [analysis, complex-analysis]
---

# Problem Statement

Find the power series expansion of $f(z) = 1/(1 - z)$ around $z = 0$. Verify two ways:

(a) Directly via the geometric series identity.

(b) Using the [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)|analyticity theorem]]: $f^{(n)}(0)/n! = c_n$.

Identify the radius of convergence and explain it geometrically.

**Recall:**

A holomorphic function on a disc $D(a, R)$ has a power series $f(z) = \sum c_n (z - a)^n$ with $c_n = f^{(n)}(a)/n!$, converging on the disc. The radius is at least $R$ (and equals the distance from $a$ to the nearest singularity).

---

# Convergent Strategy

**Problem class:** Computing a power series two ways and reconciling.

**Assumption pattern:** A known closed form with an explicit pole.

**Theorem routing:** Direct geometric series for (a); successive differentiation for (b).

**Key decision point:** Recognize $f(z) = 1/(1-z)$ has a singularity at $z = 1$, distance $1$ from $0$, so radius of convergence is $1$.

---

# Legal Operations Used

1. **Geometric series identity:** $1/(1 - z) = \sum_{n=0}^\infty z^n$ for $|z| < 1$.
2. **Differentiate $f$** to find $f^{(n)}(z)$ explicitly, evaluate at $0$.
3. **Apply the coefficient formula** $c_n = f^{(n)}(0)/n!$.

---

# Hints

> [!note]- Hint 1
> The geometric series gives $1/(1-z) = \sum z^n$ directly, valid for $|z| < 1$. So $c_n = 1$ for all $n$.

> [!note]- Hint 2
> Compute $f'(z) = 1/(1-z)^2, f''(z) = 2/(1-z)^3, \ldots, f^{(n)}(z) = n!/(1-z)^{n+1}$. At $z = 0$: $f^{(n)}(0) = n!$. So $c_n = n!/n! = 1$.

---

# Solution

**(a) Geometric series.**

$1/(1 - z) = \sum_{n=0}^\infty z^n$ for $|z| < 1$. This is the standard geometric series identity, immediate from $S_N(z) = \sum_{n=0}^N z^n = (1 - z^{N+1})/(1 - z) \to 1/(1 - z)$ as $N \to \infty$ for $|z| < 1$.

So $c_n = 1$ for all $n \geq 0$, and the power series at $0$ is
$$f(z) = 1 + z + z^2 + z^3 + \ldots$$

**(b) Via the coefficient formula.**

Compute $f$ and its derivatives:
- $f(z) = 1/(1-z)$, $f(0) = 1$, so $c_0 = 1$.
- $f'(z) = 1/(1-z)^2$, $f'(0) = 1$, so $c_1 = 1$.
- $f''(z) = 2/(1-z)^3$, $f''(0) = 2$, so $c_2 = 2/2! = 1$.
- Inductively, $f^{(n)}(z) = n!/(1-z)^{n+1}$, so $f^{(n)}(0) = n!$ and $c_n = n!/n! = 1$. ✓

The two methods agree: $c_n = 1$ for all $n$.

**Radius of convergence.**

$f(z) = 1/(1-z)$ has a singularity (pole) at $z = 1$. The distance from the centre $0$ to the nearest singularity is $|1 - 0| = 1$. So the radius of convergence of the power series at $0$ is exactly $1$.

This matches the root test: $|c_n|^{1/n} = 1^{1/n} = 1$, so $R = 1/\limsup = 1$. ✓

> [!note]- Complete formal solution
> $1/(1-z) = \sum_{n=0}^\infty z^n$ on $|z| < 1$, by geometric series. Equivalently, $f^{(n)}(z) = n!/(1-z)^{n+1}$ gives $f^{(n)}(0) = n!$, so $c_n = n!/n! = 1$ — confirming. Radius of convergence is $1$, equal to the distance from $0$ to the pole at $z = 1$. $\blacksquare$

---

# Key Takeaways

**Radius equals distance to nearest singularity.**

For a holomorphic $f$ defined on a region $\Omega$ except for isolated singularities, the radius of convergence of the Taylor series at $a \in \Omega$ is exactly the distance from $a$ to the nearest singularity. This is a beautiful structural fact: the *geometric* placement of singularities determines the *analytic* radius. For $1/(1-z)$ at $0$: pole at $1$, radius $1$. For $1/(z^2 + 1)$ at $0$: poles at $\pm i$, radius $1$ (distance to nearest, which is either pole). For $\sin z$ at $0$: no singularities, radius $\infty$ — and indeed $\sin z = z - z^3/3! + z^5/5! - \ldots$ converges everywhere.

**Two routes give the same answer.**

Whenever a function has both a closed form (allowing explicit differentiation) and a known series expansion (via algebraic identity, e.g., geometric or binomial), the two routes give the same series — by the uniqueness of power series representation. This consistency is the operational meaning of [[Thm - Identity Theorem for Power Series|the identity theorem for power series]].

**Coefficients encode derivatives.**

The Taylor coefficients $c_n = f^{(n)}(a)/n!$ encode the *derivatives* of $f$ at the centre. For $f(z) = 1/(1-z)$ at $0$: $f^{(n)}(0) = n!$, so all derivatives at $0$ are factorials. This is the precise sense in which "Taylor coefficients are derivatives": $c_n \cdot n! = f^{(n)}(a)$.
