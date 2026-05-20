---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Cauchy Estimates"
  - "Thm - Higher Derivatives via CIF"
  - "Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)"
tags: [analysis, complex-analysis]
---

# Problem Statement

Let $f : \mathbb{C} \to \mathbb{C}$ be entire and suppose there exist constants $A, R_0 > 0$ and a non-negative integer $n$ such that
$$|f(z)| \leq A|z|^n \quad \text{for all } |z| \geq R_0.$$

Prove that $f$ is a polynomial of degree at most $n$.

**Recall:**

[[Thm - Cauchy Estimates]]: for $f$ holomorphic on $D(a, R)$, $|f^{(k)}(a)| \leq k! M(r)/r^k$ for $0 < r < R$, where $M(r) = \sup_{|z-a|=r}|f|$.

[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]: an entire function equals its Taylor series at $0$ on all of $\mathbb{C}$.

---

# Convergent Strategy

**Problem class:** Use polynomial growth bound + Cauchy estimates to bound Taylor coefficients.

**Assumption pattern:** Entire $f$ with $|f(z)| = O(|z|^n)$ as $|z| \to \infty$.

**Theorem routing:** Cauchy estimate at $a = 0$ for $r$ large: $|f^{(k)}(0)| \leq k! M(r)/r^k$. With $M(r) \leq Ar^n$, this bound becomes $A k! r^{n-k}$. For $k > n$, $r^{n-k} \to 0$ as $r \to \infty$, so $f^{(k)}(0) = 0$. All Taylor coefficients of degree $> n$ vanish, so the power series is a polynomial of degree $\leq n$.

**Key decision point:** Recognizing that the Cauchy estimate must be evaluated *as $r \to \infty$* to leverage the entire-function hypothesis (which requires $r$ unbounded).

---

# Legal Operations Used

1. **Power series expansion at $0$.** $f(z) = \sum c_k z^k$ on $\mathbb{C}$, with $c_k = f^{(k)}(0)/k!$.
2. **Cauchy estimate.** $|f^{(k)}(0)| \leq k!M(r)/r^k$ for any $r > 0$.
3. **Bound $M(r)$.** For $r \geq R_0$, $M(r) \leq Ar^n$.
4. **Let $r \to \infty$.** For $k > n$, $|f^{(k)}(0)| \leq A k! r^{n - k} \to 0$, so $f^{(k)}(0) = 0$.
5. **Conclude.** All coefficients with $k > n$ vanish; $f$ is a polynomial of degree $\leq n$.

---

# Hints

> [!note]- Hint 1
> $f$ is entire, so by analyticity $f(z) = \sum c_k z^k$ on $\mathbb{C}$. Apply Cauchy estimates at $0$ with radius $r$ large.

> [!note]- Hint 2
> Use $M(r) \leq Ar^n$ for $r \geq R_0$. Substitute into the Cauchy estimate. For $k > n$, the bound $\to 0$ as $r \to \infty$.

---

# Solution

The proof breaks into four steps that use Cauchy estimates plus a "let $r \to \infty$" trick. Step 1 writes $f$ as a globally convergent Taylor series at $0$ (entire = analytic everywhere); Step 2 applies Cauchy estimates with the bound $M(r) \leq A r^n$ to get $|c_k| \leq A r^{n-k}$; Step 3 sends $r \to \infty$ to force $c_k = 0$ whenever $k > n$; Step 4 reads off the polynomial. The non-obvious move is in Step 3 — Cauchy estimates hold for *every* radius, so the optimization $r \to \infty$ converts the polynomial growth bound into vanishing of high-degree coefficients.

**Step 1: Power series at $0$.**

$f$ is entire, so by [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]], $f(z) = \sum_{k=0}^\infty c_k z^k$ on all of $\mathbb{C}$, with $c_k = f^{(k)}(0)/k!$. The series converges for every $z$.

**Step 2: Apply Cauchy estimates.**

For any $r > 0$, by [[Thm - Cauchy Estimates]]:
$$|f^{(k)}(0)| \leq \frac{k!\,M(r)}{r^k}, \quad M(r) = \sup_{|z|=r}|f(z)|.$$
For $r \geq R_0$, the hypothesis gives $|f(z)| \leq A|z|^n = Ar^n$ on $|z| = r$, hence $M(r) \leq Ar^n$. So
$$|f^{(k)}(0)| \leq \frac{k! \cdot A r^n}{r^k} = A k! r^{n-k}.$$

**Step 3: Let $r \to \infty$.**

For $k > n$ (i.e., $n - k < 0$): $r^{n-k} \to 0$ as $r \to \infty$. So $|f^{(k)}(0)| \leq 0$, hence $f^{(k)}(0) = 0$.

Therefore $c_k = f^{(k)}(0)/k! = 0$ for all $k > n$.

**Step 4: Conclude.**

$f(z) = \sum_{k=0}^\infty c_k z^k = \sum_{k=0}^n c_k z^k + 0 + 0 + \ldots$, which is a polynomial of degree $\leq n$ (the degree is exactly the largest $k \leq n$ with $c_k \neq 0$, possibly less than $n$ if higher coefficients also happen to vanish).

> [!note]- Complete formal solution
> $f$ entire, so $f(z) = \sum c_k z^k$ globally. By Cauchy estimates with $M(r) \leq Ar^n$ for $r \geq R_0$: $|c_k| = |f^{(k)}(0)|/k! \leq Ar^{n-k}$. For $k > n$: $r^{n-k} \to 0$ as $r \to \infty$, hence $c_k = 0$. So $f$ is a polynomial of degree $\leq n$. $\blacksquare$

---

# Key Takeaways

**Growth controls degree.**

This generalizes [[Thm - Liouville's Theorem|Liouville]] from $n = 0$ (bounded entire = constant) to arbitrary $n$ (polynomial growth = polynomial). The key fact: *Cauchy estimates with $r \to \infty$ force vanishing of high-degree Taylor coefficients whenever the growth of $M(r)$ is slower than $r^k$*.

**The structural statement.**

For entire functions, the growth rate $|f(z)|$ as $|z| \to \infty$ classifies the function:
- Bounded ($n = 0$): constant.
- Polynomial growth ($n \geq 1$): polynomial of degree $\leq n$.
- Sub-exponential ($|f(z)| = O(e^{|z|^\alpha})$ with $\alpha < 1$): special "order" classification (Hadamard's factorization theorem in advanced complex analysis).
- Sub-polynomial growth ($|f(z)| = o(|z|^n)$): polynomial of degree $< n$.

The complex setting gives clean polynomial classifications; real analysis has nothing comparable.

**Trigger-reaction pattern.**

When you see "$f$ entire with polynomial growth bound", reach for Cauchy estimates and let the radius go to infinity. The bound on $M(r)/r^k$ controls the $k$-th Taylor coefficient; sub-polynomial growth forces high coefficients to zero, giving a polynomial.

**Why $r \to \infty$ is the move.**

The Cauchy estimate $|c_k| \leq M(r)/r^k$ is *one* inequality for *every* $r > 0$. If we take the infimum over $r$, we get the *best* bound. For polynomial $M(r) \leq Ar^n$, the bound $Ar^{n - k}$ is minimized as $r \to \infty$ when $k > n$ (giving $0$) and as $r \to 0$ when $k < n$ (but the original Cauchy estimate requires $r$ inside the disc of holomorphicity, which for entire $f$ is unconstrained). The "take $r \to \infty$" move is exactly the right optimization.
