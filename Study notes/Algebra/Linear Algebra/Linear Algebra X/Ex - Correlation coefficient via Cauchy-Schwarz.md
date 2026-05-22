---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Standard Deviation and Correlation Coefficient"
  - "Thm - Cauchy-Schwarz and the Angle in Rn"
tags: [algebra, linear-algebra, applied, statistics]
---

# Problem Statement

Let $a, b \in \mathbb R^n$ be two non-constant vectors (i.e., both have positive standard deviation). The **correlation coefficient** is
$$\rho(a, b) = \frac{\tilde a^T \tilde b}{\|\tilde a\| \|\tilde b\|}, \quad \tilde a = a - \operatorname{avg}(a)\mathbf 1, \quad \tilde b = b - \operatorname{avg}(b)\mathbf 1.$$

Show that $-1 \leq \rho(a, b) \leq 1$, and characterise when equality at the extremes is attained.

**Recall:**

The de-meaned vector $\tilde a = a - \operatorname{avg}(a)\mathbf 1$ satisfies $\operatorname{avg}(\tilde a) = 0$; see [[Def - Standard Deviation and Correlation Coefficient]].

The [[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz inequality]]: for any $u, v \in \mathbb R^n$,
$$|u^T v| \leq \|u\| \|v\|,$$
with equality iff $u, v$ are scalar multiples of each other.

---

# Convergent Strategy

**Problem class.** This is a *direct application of Cauchy–Schwarz to interpret a standardised quantity*. The correlation coefficient is, by construction, the cosine of an angle, and Cauchy–Schwarz is exactly the statement that this cosine lies in $[-1, 1]$.

**Assumption pattern.** Two non-constant vectors $a, b$ — the non-constancy ensures $\|\tilde a\| > 0$ and $\|\tilde b\| > 0$, so the correlation is well-defined (no division by zero). The expression $\tilde a^T \tilde b / (\|\tilde a\|\|\tilde b\|)$ is *exactly* the form to which Cauchy–Schwarz applies.

**Theorem routing.** Apply [[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz]] to $u = \tilde a, v = \tilde b$: $|\tilde a^T \tilde b| \leq \|\tilde a\|\|\tilde b\|$, so $|\rho| \leq 1$, i.e., $\rho \in [-1, 1]$. The equality case of Cauchy–Schwarz characterises the extreme values $\rho = \pm 1$.

**Key decision point.** The non-obvious step is recognising that *Cauchy–Schwarz applied to the de-meaned vectors* gives the bound on correlation directly. There is no manipulation needed; the correlation coefficient is *constructed* to be cosine-like, and Cauchy–Schwarz bounds the cosine of any angle. The structural insight is that the correlation coefficient is the cosine of the angle between $\tilde a$ and $\tilde b$, and Cauchy–Schwarz is the geometric fact that cosines lie in $[-1, 1]$.

---

# Legal Operations Used

1. **Operation 3 (Cauchy–Schwarz to bound an inner product).** Applied to $u = \tilde a$, $v = \tilde b$: $|\tilde a^T \tilde b| \leq \|\tilde a\|\|\tilde b\|$.

2. **Operation 5 (de-mean to extract variability).** The correlation coefficient is by definition built from the de-meaned vectors, which separate the "level" (mean) from the "variation" (de-meaned vector). The bound applies to the variation only.

---

# Hints

> [!note]- Hint 1
> The correlation coefficient is an inner product over a product of norms. Cauchy–Schwarz is the most natural thing to try.

> [!note]- Hint 2
> Apply Cauchy–Schwarz to the de-meaned vectors $\tilde a, \tilde b$. The conclusion $|\tilde a^T \tilde b| \leq \|\tilde a\|\|\tilde b\|$ is exactly $|\rho| \leq 1$ after dividing.

> [!note]- Hint 3
> Equality in Cauchy–Schwarz holds iff one vector is a scalar multiple of the other. Translate this back into a statement about $a$ and $b$: $\rho = \pm 1$ iff $\tilde a = \alpha \tilde b$ for some scalar $\alpha$, iff $a$ is an affine function of $b$.

---

# Solution

The proof has two steps. Step 1 applies Cauchy–Schwarz to the de-meaned vectors to bound $|\rho| \leq 1$. Step 2 traces back the Cauchy–Schwarz equality case to identify when $\rho = \pm 1$.

**Step 1: $|\rho(a, b)| \leq 1$.**

Apply Cauchy–Schwarz to $\tilde a, \tilde b$.

> [!note]- Derivation
> By the [[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz inequality]] applied to the de-meaned vectors $\tilde a, \tilde b \in \mathbb R^n$:
> $$|\tilde a^T \tilde b| \leq \|\tilde a\| \|\tilde b\|.$$
> Since $a, b$ are non-constant, $\|\tilde a\| > 0$ and $\|\tilde b\| > 0$, so we can divide:
> $$\frac{|\tilde a^T \tilde b|}{\|\tilde a\| \|\tilde b\|} \leq 1.$$
> The left side is $|\rho(a, b)|$, so $|\rho| \leq 1$, equivalently $-1 \leq \rho \leq 1$.

**Step 2: Characterise $\rho = \pm 1$.**

Use the equality case of Cauchy–Schwarz.

> [!note]- Derivation
> $\rho = +1$ holds iff $\tilde a^T \tilde b = \|\tilde a\|\|\tilde b\|$, which is the equality case of Cauchy–Schwarz in the "positive" direction. By the [[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz equality case]], this happens iff $\tilde a$ and $\tilde b$ are *positively* aligned: $\tilde a = \alpha \tilde b$ for some $\alpha > 0$.
>
> Re-interpret this in terms of $a, b$: $\tilde a = \alpha \tilde b$ means $a - \operatorname{avg}(a)\mathbf 1 = \alpha(b - \operatorname{avg}(b)\mathbf 1)$, so $a = \alpha b + (\operatorname{avg}(a) - \alpha \operatorname{avg}(b))\mathbf 1 = \alpha b + \beta \mathbf 1$ for some scalar $\beta = \operatorname{avg}(a) - \alpha \operatorname{avg}(b)$. In words, $a$ is a *positive affine function* of $b$ — a positive slope times $b$, plus a constant shift.
>
> Similarly, $\rho = -1$ holds iff $\tilde a^T \tilde b = -\|\tilde a\|\|\tilde b\|$, iff $\tilde a = \alpha \tilde b$ with $\alpha < 0$, iff $a = \alpha b + \beta \mathbf 1$ with $\alpha < 0$ — a *negative affine function* of $b$.
>
> So: $\rho(a, b) = 1$ iff $a$ is a positive affine function of $b$ (perfect positive linear relationship); $\rho(a, b) = -1$ iff $a$ is a negative affine function of $b$ (perfect negative linear relationship); $|\rho| < 1$ otherwise.

> [!note]- Complete formal solution
> Let $a, b \in \mathbb R^n$ be non-constant (so $\|\tilde a\|, \|\tilde b\| > 0$).
>
> *Bound.* By the [[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz inequality]] applied to $\tilde a, \tilde b \in \mathbb R^n$,
> $$|\tilde a^T \tilde b| \leq \|\tilde a\|\|\tilde b\|.$$
> Dividing by the positive product $\|\tilde a\|\|\tilde b\|$,
> $$|\rho(a, b)| = \frac{|\tilde a^T \tilde b|}{\|\tilde a\|\|\tilde b\|} \leq 1.$$
> So $-1 \leq \rho(a, b) \leq 1$.
>
> *Equality cases.* By the Cauchy–Schwarz equality case, $|\tilde a^T \tilde b| = \|\tilde a\|\|\tilde b\|$ iff $\tilde a$ and $\tilde b$ are scalar multiples of each other (with the scalar's sign matching $\tilde a^T \tilde b$).
>
> $\rho = +1$ iff $\tilde a^T \tilde b = +\|\tilde a\|\|\tilde b\|$, iff $\tilde a = \alpha \tilde b$ for some $\alpha > 0$. Re-arranging: $a = \alpha b + \beta \mathbf 1$ where $\beta = \operatorname{avg}(a) - \alpha\operatorname{avg}(b)$ — i.e., $a$ is a positive affine function of $b$.
>
> $\rho = -1$ iff $\tilde a^T \tilde b = -\|\tilde a\|\|\tilde b\|$, iff $\tilde a = \alpha \tilde b$ for some $\alpha < 0$. Similarly, $a$ is a negative affine function of $b$.
>
> In all other cases, $|\rho| < 1$. $\quad\blacksquare$

---

# Key Takeaways

**The correlation coefficient is, by construction, a cosine — and Cauchy–Schwarz is the universal cosine bound.** Every quantity of the form $u^T v / (\|u\|\|v\|)$ is a cosine of an angle, and by Cauchy–Schwarz lies in $[-1, 1]$. The correlation coefficient is this construction applied to *de-meaned* vectors, which strips out the mean before measuring alignment. This is why "correlation $\in [-1, 1]$" is automatic; it requires no statistical assumption, no probability theory, no Gaussian distribution — just the algebraic fact that cosines lie in $[-1, 1]$. Understanding this clarifies why the correlation coefficient is so robust as a statistical measure: its bound is structural, not distributional.

**Perfect correlation $\rho = \pm 1$ corresponds to perfect affine dependence.** $\rho = +1$ iff one variable is a *positive affine function* of the other; $\rho = -1$ iff a *negative affine function*. This is the deterministic content of "perfect linear relationship", and it sharpens the loose statistical intuition. The Cauchy–Schwarz equality case provides the structural reason: equality in the inequality requires alignment (scalar multiples), and the sign of the scalar determines the sign of the correlation. The trigger-reaction pattern: when $\rho$ is near $\pm 1$ in a dataset, expect that the data lie close to an affine line, and use linear regression to extract the slope and intercept.

**Uncorrelated does NOT mean independent (in either the deterministic or probabilistic sense).** The example $a = (-2, -1, 0, 1, 2)$, $b = (4, 1, 0, 1, 4)$ has $\rho(a, b) = 0$ even though $b_i = a_i^2$ for every $i$ — a deterministic dependence! Correlation measures *linear* relationship only; non-linear relationships are invisible. In probability, the analogous statement is that uncorrelated random variables can still be dependent through any non-linear functional relationship; the converse — independence implies zero correlation — does hold. The asymmetry between "uncorrelated" and "independent" is the most important structural fact about the correlation coefficient: it is a *linear-only* dependence measure, and reaching for it to detect arbitrary dependence is a category error. For arbitrary dependence one needs *mutual information* (in probability) or more sophisticated nonparametric measures.
