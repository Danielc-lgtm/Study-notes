---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Power Series is Holomorphic with Termwise Derivative"
  - "Def - Power Series and Radius of Convergence"
tags: [analysis, complex-analysis]
---

# Problem Statement

Consider the geometric series $f(z) = \sum_{n=0}^\infty z^n = 1/(1 - z)$, convergent on $|z| < 1$.

(a) Compute $f'(z)$ by termwise differentiation of the power series. Confirm the new series has the same radius of convergence.

(b) Compute $f'(z)$ directly from the closed form $1/(1 - z)$.

(c) Verify the two answers agree by showing the resulting power series equals the derivative computed directly.

(d) Using a similar method, compute $\sum_{n=2}^\infty n(n-1) z^{n-2}$ as a closed form.

**Recall:**

By [[Thm - Power Series is Holomorphic with Termwise Derivative]], a power series $f(z) = \sum c_n (z - a)^n$ with radius $R > 0$ is holomorphic on $D(a, R)$ with $f'(z) = \sum n c_n (z - a)^{n-1}$ on the same disc. The geometric series $\sum z^n = 1/(1 - z)$ on $|z| < 1$.

---

# Convergent Strategy

**Problem class:** Verifying the consistency of termwise differentiation against direct closed-form differentiation.

**Assumption pattern:** A power series with a known closed form.

**Theorem routing:** Termwise differentiation theorem in one direction; the chain/quotient rule in the other. Compare.

**Key decision point:** Recognizing that $\sum_{n=1}^\infty n z^{n-1}$ should equal $1/(1-z)^2$ by direct differentiation, then verifying via re-indexing or pattern recognition.

---

# Legal Operations Used

1. **Termwise differentiation** of the power series, valid on the open disc of convergence.
2. **Quotient/chain rule** for the closed form $1/(1-z) = (1-z)^{-1}$.
3. **Re-indexing the series** to match the differentiated form.
4. **Iteration:** apply termwise differentiation again to compute $f''$.

---

# Hints

> [!note]- Hint 1
> For (a), differentiate each term of $\sum z^n$ to get $\sum n z^{n-1}$ for $n \geq 1$. The new radius is also $1$ (since $n^{1/n} \to 1$).

> [!note]- Hint 2
> For (b), $f(z) = (1-z)^{-1}$, so $f'(z) = (1-z)^{-2}$ by the chain rule.

> [!note]- Hint 3
> For (d), differentiate $f'(z) = \sum_{n=1}^\infty n z^{n-1}$ termwise to get $\sum_{n=2}^\infty n(n-1) z^{n-2}$. Equate with $f''(z) = 2/(1-z)^3$.

---

# Solution

**(a) Termwise differentiation.**

$$f(z) = \sum_{n=0}^\infty z^n, \qquad f'(z) = \sum_{n=1}^\infty n z^{n-1} = 1 + 2z + 3z^2 + 4z^3 + \ldots$$

> [!note]- Radius of the derivative series
> The new coefficients are $c_n' = n$ (so the coefficient of $z^{n-1}$ is $n$, or equivalently shifting index, the coefficient of $z^k$ is $k + 1$). Either way, $|c_n'|^{1/n} = n^{1/n} \to 1$, so radius $1$. Same as the original series.

**(b) Direct differentiation.**

$$f(z) = (1 - z)^{-1}, \qquad f'(z) = -(1-z)^{-2}\cdot(-1) = (1-z)^{-2} = \frac{1}{(1-z)^2}.$$

**(c) Verifying agreement.**

We must show $\sum_{n=1}^\infty n z^{n-1} = 1/(1-z)^2$ on $|z| < 1$.

> [!note]- Direct verification
> The Cauchy product of two geometric series: $1/(1-z)^2 = (1/(1-z))^2 = (\sum_{n=0}^\infty z^n)^2 = \sum_{n=0}^\infty (\sum_{j=0}^n 1 \cdot 1) z^n = \sum_{n=0}^\infty (n+1) z^n$.
>
> Shifting the index $n \to n - 1$: this is $\sum_{n=1}^\infty n z^{n-1}$. ✓

So both methods give $f'(z) = 1/(1-z)^2 = \sum_{n=1}^\infty n z^{n-1}$ on $|z| < 1$.

**(d) Computing $\sum_{n=2}^\infty n(n-1) z^{n-2}$.**

Apply termwise differentiation to $f'(z) = \sum_{n=1}^\infty n z^{n-1}$ to get
$$f''(z) = \sum_{n=2}^\infty n(n-1) z^{n-2} = 2 + 6z + 12z^2 + 20 z^3 + \ldots$$

By direct differentiation, $f''(z) = (d/dz)[(1-z)^{-2}] = 2(1-z)^{-3} = 2/(1-z)^3$.

So $\sum_{n=2}^\infty n(n-1) z^{n-2} = 2/(1-z)^3$ on $|z| < 1$.

> [!note]- Complete formal solution
> Set $f(z) = \sum z^n = 1/(1-z)$ on $|z| < 1$.
>
> **(a)** By [[Thm - Power Series is Holomorphic with Termwise Derivative]], $f'(z) = \sum_{n=1}^\infty n z^{n-1}$ with the same radius $R = 1$ (since $\limsup n^{1/n} = 1$).
>
> **(b)** From the closed form, $f'(z) = (d/dz)(1-z)^{-1} = (1-z)^{-2}$.
>
> **(c)** Compute $(1-z)^{-2} = ((1-z)^{-1})^2 = (\sum z^n)^2 = \sum_{n \geq 0} (n+1) z^n = \sum_{n \geq 1} n z^{n-1}$ (Cauchy product, geometric series squared). Matches (a). ✓
>
> **(d)** Differentiate (a) again: $f''(z) = \sum_{n=2}^\infty n(n-1) z^{n-2}$. From the closed form, $f''(z) = 2(1-z)^{-3} = 2/(1-z)^3$. Hence $\sum_{n=2}^\infty n(n-1) z^{n-2} = 2/(1-z)^3$ on $|z| < 1$. $\blacksquare$

---

# Key Takeaways

**Termwise differentiation is consistent with closed-form differentiation.**

The theorem says: any power series $f$ has a holomorphic derivative obtainable by termwise differentiation. When $f$ happens to have a closed form, the two methods *must* agree — and verifying this consistency on simple examples (like the geometric series) builds confidence. The agreement is not a coincidence but a structural consequence of the theorem.

**Cauchy product as a tool for power-series identities.**

The identity $(\sum z^n)^2 = \sum (n+1) z^n$ is the Cauchy product applied to the geometric series. More generally, $(\sum a_n z^n)(\sum b_n z^n) = \sum c_n z^n$ with $c_n = \sum_{k=0}^n a_k b_{n-k}$. This is the natural way to multiply power series and is essential for proving identities like $\exp(z + w) = \exp(z)\exp(w)$ via the binomial theorem applied to series.

**Iteration gives all derivatives + the coefficient formula.**

Repeated application of termwise differentiation gives $f^{(k)}(z) = \sum_{n \geq k} n(n-1)\ldots(n-k+1) c_n (z - a)^{n-k}$. Evaluated at $z = a$, only the $n = k$ term survives, giving the **Taylor coefficient formula** $c_k = f^{(k)}(a)/k!$. This is the source of the explicit formulas: for $1/(1-z)$ at $0$, $f^{(k)}(0) = k!$, so $c_k = 1$ — matches $1, 1, 1, \ldots$. For $1/(1-z)^2$, $f^{(k)}(0) = (k+1)!$, so $c_k = k + 1$ — matches.
