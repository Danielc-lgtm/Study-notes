---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Argument Principle"
  - "Thm - Residue Theorem"
  - "Thm - Fundamental Theorem of Algebra via Rouché"
tags: [analysis, complex-analysis]
---

# Problem Statement

Let $p$ be a polynomial of degree $n$. Show directly via the argument principle that
$$\frac{1}{2\pi i}\oint_{|z| = R}\frac{p'(z)}{p(z)}\,dz = n$$
for $R$ sufficiently large that all zeros of $p$ lie in $|z| < R$. Use this as an alternative proof of the Fundamental Theorem of Algebra.

**Recall:**

![[Thm - Argument Principle#Notation]]

For meromorphic $f$, $\frac{1}{2\pi i}\oint f'/f\,dz = N - P$, the number of zeros minus poles.

---

# Convergent Strategy

**Problem class:** Verify the argument principle's count for a polynomial. The polynomial has $n$ zeros (the FTA result we want to prove) and no poles, so $N - P = n$. The verification proceeds in two ways: direct evaluation, and asymptotic comparison.

**Assumption pattern:** $p$ is a polynomial of degree $n$. The integrand $p'/p$ is rational with poles at the zeros of $p$.

**Theorem routing:** Direct computation of the residues of $p'/p$ at each zero, then sum via the residue theorem.

**Key decision point:** To prove FTA *from* the argument principle, we need to derive the integral $= n$ without already assuming the polynomial has $n$ zeros. Use asymptotic estimate: $p'/p \approx n/z$ for large $|z|$, giving the integral $\approx n$ for $R$ large.

---

# Legal Operations Used

1. **Compute $p'/p$ for a polynomial.** $p(z) = a_n z^n + \ldots$, $p'(z) = na_n z^{n-1} + \ldots$. So $p'/p \to n/z$ as $|z| \to \infty$.
2. **Estimate the difference $p'/p - n/z$ on $|z| = R$ for $R$ large.** Show it decays like $O(1/R^2)$, so the integral over $|z| = R$ of this difference vanishes as $R \to \infty$.
3. **Compute $\oint_{|z| = R} (n/z)\,dz = 2\pi i n$** by the standard residue at $0$.
4. **Combine: $\oint p'/p\,dz \to 2\pi i n$ as $R \to \infty$, and the integral is constant (independent of $R$) for $R$ large enough that all zeros of $p$ are enclosed.**

---

# Hints

> [!note]- Hint 1
> Direct method: by the argument principle, $\oint p'/p\,dz/(2\pi i) = N - P$, where $N$ is the zero count of $p$ and $P = 0$ (polynomial, no poles). To prove the polynomial has $n$ zeros (FTA), we need a separate argument for the integral value.

> [!note]- Hint 2
> Asymptotic: $p'(z)/p(z) = n/z + O(1/z^2)$ for $|z| \to \infty$.

> [!note]- Hint 3
> Compute $\oint_{|z| = R}(n/z)\,dz = 2\pi i n$. Bound the remainder.

---

# Solution

The proof breaks into four steps. Step 1 expands $p'(z)/p(z)$ asymptotically as $n/z + O(1/z^2)$ for $|z|$ large, exploiting that $p(z) \sim a_n z^n$; Step 2 evaluates the integral asymptotically — the $n/z$ term contributes $2\pi i n$ and the $O(1/z^2)$ error vanishes as $R \to \infty$ by ML; Step 3 observes that the integral is constant in $R$ once $R$ encloses all zeros of $p$, pinning the value at exactly $n$; Step 4 invokes the argument principle to read this as "$p$ has $n$ zeros," which is FTA. The non-obvious move is in Step 3 — combining "integral constant for $R$ large" with "asymptotic limit is $n$" is what forces the integral to be *exactly* $n$, not just close to it.

**Step 1: Asymptotic expansion of $p'/p$**

Let $p(z) = a_n z^n + a_{n-1}z^{n-1} + \ldots + a_0$ with $a_n \neq 0$. Then $p'(z) = na_n z^{n-1} + (n-1)a_{n-1}z^{n-2} + \ldots$.

> [!note]- Derivation
> For $|z|$ large:
> $$\frac{p(z)}{a_n z^n} = 1 + \frac{a_{n-1}}{a_n z} + \frac{a_{n-2}}{a_n z^2} + \ldots = 1 + O(1/z).$$
> So $p(z) = a_n z^n (1 + O(1/z))$, and similarly $p'(z) = na_n z^{n-1}(1 + O(1/z))$.
>
> Therefore:
> $$\frac{p'(z)}{p(z)} = \frac{na_n z^{n-1}(1 + O(1/z))}{a_n z^n (1 + O(1/z))} = \frac{n}{z}\cdot \frac{1 + O(1/z)}{1 + O(1/z)} = \frac{n}{z}(1 + O(1/z)).$$
> Hence $p'(z)/p(z) = n/z + O(1/z^2)$ for $|z|$ large.

**Step 2: Compute the integral asymptotically**

> [!note]- Derivation
> $\oint_{|z| = R}\frac{p'(z)}{p(z)}\,dz = \oint_{|z| = R}\frac{n}{z}\,dz + \oint_{|z| = R} O(1/z^2)\,dz$.
>
> First integral: $\oint_{|z| = R}n/z\,dz = 2\pi i n$ (standard, residue $n$ at $0$).
>
> Second integral: $|O(1/z^2)| \leq C/R^2$ on $|z| = R$ for some constant $C$, so $|\oint O(1/z^2)\,dz| \leq 2\pi R \cdot C/R^2 = 2\pi C/R \to 0$ as $R \to \infty$.
>
> Hence $\oint_{|z| = R}p'/p\,dz \to 2\pi i n$ as $R \to \infty$. Dividing by $2\pi i$: $(2\pi i)^{-1}\oint p'/p\,dz \to n$.

**Step 3: The integral is independent of $R$ for $R$ large**

> [!note]- Derivation
> Once $R$ is large enough that all zeros of $p$ are in $|z| < R$ (such $R$ exists by boundedness of polynomial zeros — they're contained in $|z| < 1 + \sum|a_i/a_n|$ by elementary bounds), the integrand $p'/p$ is meromorphic with poles only at the zeros of $p$, and the integral is determined by the residue sum:
> $$\frac{1}{2\pi i}\oint_{|z| = R}\frac{p'(z)}{p(z)}\,dz = \sum_{\text{zeros } z_k}\operatorname{Res}_{z_k}\frac{p'}{p}.$$
>
> Increasing $R$ doesn't enclose new poles (all zeros already enclosed), so the integral is the same. Combined with the asymptotic limit, this constant equals $n$.

**Step 4: Argument principle interpretation gives FTA**

> [!note]- Derivation
> By the [[Thm - Argument Principle|argument principle]], the integral equals $N - P = N$ (no poles). So $N = n$ — the polynomial has exactly $n$ zeros in $\mathbb{C}$ (counted with multiplicity, all enclosed by a sufficiently large circle).
>
> This is the **Fundamental Theorem of Algebra**, derived from the argument principle.

> [!note]- Complete formal solution
> Let $p(z) = a_n z^n + \ldots + a_0$ with $a_n \neq 0$ and $n \geq 1$.
>
> **Asymptotic.** For $|z|$ large:
> $$\frac{p'(z)}{p(z)} = \frac{n}{z}\cdot\frac{1 + (n-1)a_{n-1}/(na_n z) + \ldots}{1 + a_{n-1}/(a_n z) + \ldots} = \frac{n}{z} + O(1/z^2).$$
>
> **Compute the integral.** For $R$ large enough that all zeros of $p$ are in $|z| < R$:
> $$\oint_{|z| = R}\frac{p'(z)}{p(z)}\,dz = \oint_{|z| = R}\frac{n}{z}\,dz + \oint_{|z| = R}O(1/z^2)\,dz = 2\pi i n + O(1/R).$$
> As $R \to \infty$, the error vanishes: $\lim_{R \to \infty}(2\pi i)^{-1}\oint_{|z| = R}p'/p\,dz = n$.
>
> Since the integral is constant for $R$ sufficiently large (all zeros enclosed), the value is exactly $n$:
> $$\frac{1}{2\pi i}\oint_{|z| = R}\frac{p'(z)}{p(z)}\,dz = n.$$
>
> **FTA.** By the argument principle, this integral equals the number of zeros of $p$ in $|z| < R$ (since no poles), so $p$ has $n$ zeros there. As $R$ was sufficiently large to capture all zeros, $p$ has exactly $n$ zeros in $\mathbb{C}$. $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "polynomial of degree $n$" → "$p'/p \sim n/z$ at infinity".** The logarithmic derivative of a polynomial has a particular form at infinity. The residue at $\infty$ is $-n$ (because $\operatorname{Res}_\infty f = -\operatorname{Res}_0(1/w^2)f(1/w)$, and for $p'/p \sim n/z$, the residue at $\infty$ is $-n$). By the residue-at-infinity theorem (sum of all residues including $\infty$ is zero), $\sum_{\text{finite zeros}}\operatorname{ord}(\text{zero}) = n$.

**The asymptotic estimate is the key technique.** When evaluating $\oint p'/p$ for large circles, replace $p'/p$ by its leading asymptotic term $n/z$, and bound the error. This is the standard technique for residue-at-infinity calculations and a useful general approach.

**FTA via three different routes.** This exercise is the *argument principle* proof of FTA. The other two routes:
- **Via Rouché**: see [[Thm - Fundamental Theorem of Algebra via Rouché]]; compare $p$ with its leading term $z^n$ on a large circle.
- **Via Liouville**: if $p$ has no zeros, $1/p$ is entire and bounded (since $|p(z)| \to \infty$), hence constant by Liouville, contradicting $p$ non-constant.
All three are essentially the same fact phrased differently — they all use that polynomials behave like $z^n$ at infinity.

**Generalization to meromorphic functions on $\hat{\mathbb{C}}$.** For a rational function $f$ on $\hat{\mathbb{C}}$, the argument principle gives the *Riemann–Hurwitz formula* for branched covers: the genus of $\hat{\mathbb{C}}$ via the degree of $f$ and the branching profile.
