---
type: exercise
subject: complex-analysis
difficulty: "⭐"
prereqs:
  - "Def - Power Series and Radius of Convergence"
  - "Thm - Radius of Convergence Formula and Uniform Convergence on Sub-Discs"
tags: [analysis, complex-analysis]
---

# Problem Statement

Compute the radius of convergence $R$ of each power series:

(a) $\sum_{n=0}^\infty z^n$

(b) $\sum_{n=0}^\infty z^n/n!$

(c) $\sum_{n=0}^\infty n! z^n$

(d) $\sum_{n=1}^\infty z^n/n^2$

(e) $\sum_{n=1}^\infty z^n/n$

In each case, describe the convergence behaviour on the boundary $|z| = R$ where this can be determined.

**Recall:**

The [[Def - Power Series and Radius of Convergence|radius of convergence]] is $R = 1/\limsup_{n\to\infty} |c_n|^{1/n}$, with $1/0 = \infty$ and $1/\infty = 0$. Equivalently, when $\lim |c_n/c_{n+1}|$ exists, this is also $R$ (ratio test).

---

# Convergent Strategy

**Problem class:** Mechanical computation of radii using the root or ratio test.

**Assumption pattern:** Explicit coefficient formulas $c_n$.

**Theorem routing:** Choose root test (universal) or ratio test (cleaner when applicable).

**Key decision point:** Recognizing which limits to use — $n^{1/n} \to 1, (n!)^{1/n} \to \infty, (1/n!)^{1/n} \to 0$ via Stirling, etc.

---

# Legal Operations Used

1. **Compute $|c_n|^{1/n}$ as $n \to \infty$.**
2. **Apply standard limits:** $n^{1/n} \to 1$, $(n!)^{1/n} \sim n/e$ (Stirling), so $(n!)^{1/n} \to \infty$ and $(1/n!)^{1/n} \to 0$.
3. **Apply ratio test** $\lim |c_n/c_{n+1}|$ when the limit exists.
4. **Test boundary behaviour** via known tests (geometric, $p$-test, alternating series).

---

# Hints

> [!note]- Hint 1
> For (a)-(d), the coefficients are $1, 1/n!, n!, 1/n^2$. Take $n$-th roots: $|c_n|^{1/n}$ for each. Use Stirling $(n!)^{1/n} \sim n/e$.

> [!note]- Hint 2
> For boundary: on $|z| = 1$, $\sum z^n$ diverges (general term has modulus $1$, doesn't go to $0$). $\sum z^n/n^2$ converges absolutely (by $p$-test). $\sum z^n/n$ is more subtle: at $z = 1$ harmonic, divergent; at $z = -1$ alternating harmonic, conditionally convergent.

---

# Solution

**(a) $\sum z^n$.** Coefficients $c_n = 1$. So $|c_n|^{1/n} = 1$, $\limsup = 1$, hence $R = 1$.

> [!note]- Boundary on $|z| = 1$
> $|z^n| = 1$ for every $z$ on the circle, so the general term does not go to $0$: divergence everywhere on $|z| = 1$.

**(b) $\sum z^n/n!$.** $c_n = 1/n!$. By Stirling, $(n!)^{1/n} \sim n/e \to \infty$. So $|c_n|^{1/n} = 1/(n!)^{1/n} \to 0$, giving $R = 1/0 = \infty$.

> [!note]- Ratio-test alternative
> $|c_n/c_{n+1}| = (n+1)!/n! = n + 1 \to \infty$. Same answer $R = \infty$.

Converges for all $z \in \mathbb{C}$; defines the exponential $e^z$.

**(c) $\sum n! z^n$.** $c_n = n!$. By Stirling, $|c_n|^{1/n} = (n!)^{1/n} \to \infty$. So $R = 1/\infty = 0$.

> [!note]- Ratio-test alternative
> $|c_n/c_{n+1}| = n!/(n+1)! = 1/(n+1) \to 0$. Same answer $R = 0$.

Converges only at $z = 0$.

**(d) $\sum z^n/n^2$.** $c_n = 1/n^2$. So $|c_n|^{1/n} = 1/n^{2/n}$. Since $n^{2/n} = (n^{1/n})^2 \to 1^2 = 1$, $|c_n|^{1/n} \to 1$, giving $R = 1$.

> [!note]- Boundary on $|z| = 1$
> $|z^n/n^2| = 1/n^2$ for $|z| = 1$. The series $\sum 1/n^2 < \infty$ ($p$-series, $p = 2 > 1$). So the original series *converges absolutely* on the whole closed disc $|z| \leq 1$.

**(e) $\sum z^n/n$.** $c_n = 1/n$. So $|c_n|^{1/n} = 1/n^{1/n} \to 1$, giving $R = 1$.

> [!note]- Boundary on $|z| = 1$
> *At $z = 1$:* the series is the harmonic series $\sum 1/n$, divergent.
>
> *At $z = -1$:* the series is $\sum (-1)^n/n$, the alternating harmonic series, conditionally convergent (Leibniz).
>
> *At $z = e^{i\theta}$ for $\theta \neq 0 \pmod{2\pi}$:* by Dirichlet's test (partial sums of $z^n$ are bounded, $1/n$ is monotone decreasing to $0$), the series converges. So it converges everywhere on $|z| = 1$ *except* at $z = 1$.

Boundary behaviour can be subtle and depends on the specific series.

> [!note]- Complete formal solution
> All radii compute by the root test $R = 1/\limsup|c_n|^{1/n}$ and the standard limits $n^{1/n} \to 1$ and $(n!)^{1/n} \to \infty$ (Stirling).
>
> (a) $R = 1$, diverges on $|z| = 1$. (b) $R = \infty$. (c) $R = 0$. (d) $R = 1$, absolutely converges on closed disc. (e) $R = 1$, converges on $|z| = 1$ except at $z = 1$. $\blacksquare$

---

# Key Takeaways

**The two standard tools: root and ratio.**

The root test $R = 1/\limsup |c_n|^{1/n}$ always works but requires computing the $\limsup$. The ratio test $R = \lim |c_n/c_{n+1}|$ is cleaner when the limit exists — typically when $c_n$ involves factorials, where the ratio collapses to a single factor. For series like $\sum a_n z^n$ with $a_n$ algebraic in $n$ (powers, polynomials, factorials), the ratio test usually wins. For series with oscillating $|c_n|$ (e.g., $\sum c_n z^n$ where $c_n = 2^n$ on even indices and $c_n = 1$ on odd), only the root test reaches the answer.

**Standard limits to memorize.**

$n^{1/n} \to 1$ (so $(n^k)^{1/n} \to 1$ for any fixed $k$); $(n!)^{1/n} \to \infty$ (Stirling); $a^{n/n} = a$ for $a > 0$ constant. From these, every "typical" radius computation reduces to a few seconds.

**Boundary behaviour is genuinely a separate question.**

The radius of convergence determines the *open* disc of convergence. Behaviour on the boundary circle $|z| = R$ depends on subtler tests: $p$-test for absolute convergence; Dirichlet's test for conditional convergence at points where $z^n$ has bounded partial sums; Abel's theorem for one-sided limits at boundary points. The boundary is where the *most interesting* questions in summation theory live — and where the most delicate proofs reside.
