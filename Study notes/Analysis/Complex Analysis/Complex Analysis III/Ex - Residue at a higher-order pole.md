---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Residue"
  - "Thm - Computing Residues"
  - "Def - Removable Singularity, Pole, Essential Singularity"
tags: [analysis, complex-analysis]
---

# Problem Statement

Compute $\operatorname{Res}_0 (e^z/z^3)$ — the residue of $f(z) = e^z/z^3$ at $z = 0$.

**Recall:**

![[Def - Residue#The Definition]]

For a pole of order $k$ at $a$, $\operatorname{Res}_a f = \frac{1}{(k-1)!}\lim_{z \to a}\frac{d^{k-1}}{dz^{k-1}}[(z - a)^k f(z)]$.

---

# Convergent Strategy

**Problem class:** Compute the residue at a higher-order pole. The key tool is the $(k-1)$-th derivative formula.

**Assumption pattern:** $e^z/z^3$ has a pole of order $3$ at $z = 0$ (numerator $e^z$ is holomorphic with $e^0 = 1 \neq 0$, denominator $z^3$ has a zero of order $3$).

**Theorem routing:** [[Thm - Computing Residues|order-k formula]] with $k = 3$. Multiply by $z^3$, take the second derivative ($k - 1 = 2$), evaluate at $z = 0$, divide by $2!$.

**Key decision point:** Recognize the pole order from the explicit form $1/z^3$. The numerator $e^z$ does not vanish at $0$ (it equals $1$ there), so the order is exactly $3$.

---

# Legal Operations Used

1. **Determine the pole order** by reading $1/z^3$ off the denominator.
2. **Apply the order-$k$ residue formula** with $k = 3$.
3. **Multiply by $z^3$**: $z^3 f(z) = e^z$.
4. **Differentiate twice**: $d^2 e^z/dz^2 = e^z$.
5. **Evaluate at $z = 0$**: $e^0 = 1$.
6. **Divide by $(k-1)! = 2$**.

Alternative: **Laurent-expand $e^z = \sum z^n/n!$ and read off the $1/z$ coefficient of $e^z/z^3 = \sum z^{n-3}/n!$**: the term $z^{-1}$ comes from $n - 3 = -1$, i.e., $n = 2$, with coefficient $1/2!$. Same answer.

---

# Hints

> [!note]- Hint 1
> Identify the pole order: $e^z$ is holomorphic at $0$ with $e^0 = 1 \neq 0$, so the pole order is exactly $3$.

> [!note]- Hint 2
> Apply the order-$3$ formula: $\operatorname{Res}_0 f = \frac{1}{2!}\lim_{z \to 0}(d^2/dz^2)[z^3 \cdot e^z/z^3] = \frac{1}{2}\lim_{z \to 0}(d^2/dz^2)[e^z]$.

> [!note]- Hint 3
> $d^2 e^z/dz^2 = e^z$, evaluated at $0$ gives $1$. So $\operatorname{Res}_0 f = 1/2$.

> [!note]- Hint 4 (alternative)
> Laurent-expand: $e^z = 1 + z + z^2/2 + z^3/6 + \ldots$, so $e^z/z^3 = z^{-3} + z^{-2} + z^{-1}/2 + 1/6 + \ldots$. The coefficient of $z^{-1}$ is $1/2$.

---

# Solution

**Step 1: Determine pole order**

$f(z) = e^z/z^3$. At $z = 0$: $e^z$ is holomorphic and $e^0 = 1 \neq 0$, while $z^3$ has a zero of order $3$. Hence $f$ has a pole of order $3$ at $z = 0$.

**Step 2: Apply the order-$3$ formula**

By [[Thm - Computing Residues|the order-k residue formula]] with $k = 3$:
$$\operatorname{Res}_0 f = \frac{1}{2!}\lim_{z \to 0}\frac{d^2}{dz^2}\left[z^3 \cdot \frac{e^z}{z^3}\right] = \frac{1}{2}\lim_{z \to 0}\frac{d^2}{dz^2}\,e^z.$$

> [!note]- Derivation
> Multiplying $z^3 f(z) = z^3 \cdot e^z/z^3 = e^z$, which is holomorphic at $0$. Differentiating: $(d/dz) e^z = e^z$, $(d^2/dz^2) e^z = e^z$. Evaluating at $z = 0$: $e^0 = 1$. Dividing by $2! = 2$: $\operatorname{Res}_0 f = 1/2$.

**Step 3: Verify via Laurent expansion**

> [!note]- Derivation
> Expand $e^z = \sum_{n \geq 0} z^n/n!$, so
> $$\frac{e^z}{z^3} = \sum_{n \geq 0}\frac{z^{n-3}}{n!} = \frac{1}{z^3} + \frac{1}{z^2} + \frac{1}{2z} + \frac{1}{6} + \frac{z}{24} + \ldots.$$
> The coefficient of $z^{-1}$ — by definition the residue — is $1/2$. Matches.

> [!note]- Complete formal solution
> The function $f(z) = e^z/z^3$ has a pole of order $3$ at $z = 0$ (numerator holomorphic and nonzero at $0$, denominator with triple zero at $0$).
>
> By the order-$k$ residue formula with $k = 3$:
> $$\operatorname{Res}_0(e^z/z^3) = \frac{1}{(3 - 1)!}\lim_{z \to 0}\frac{d^{3 - 1}}{dz^{3 - 1}}\left[z^3 \cdot \frac{e^z}{z^3}\right] = \frac{1}{2!}\cdot\frac{d^2}{dz^2}e^z\bigg|_{z = 0} = \frac{1}{2}\cdot 1 = \frac{1}{2}.$$
> $\blacksquare$

---

# Key Takeaways

**Higher-order pole residues require differentiating $(z - a)^k f(z)$.** This is the workhorse formula for higher-order poles. The intuition: multiplying by $(z - a)^k$ shifts the Laurent expansion so the most-negative term becomes a *constant*; the $(z - a)^{-1}$ term becomes $(z - a)^{k - 1}$; taking $(k - 1)$ derivatives at $z = a$ extracts the coefficient of $(z - a)^{k - 1}$, which is the residue (up to $(k - 1)!$).

**For complicated functions, Laurent-expand and read off $c_{-1}$ directly.** When the function has a complicated Laurent expansion (especially essential singularities), the derivative formula is heavy, and direct expansion is cleaner. Mental rule: if differentiating $k - 1$ times would be painful, expand the Laurent series.

**Trigger-reaction pattern — "exponential or trig function divided by polynomial" → "Laurent-expand the numerator, divide".** The pattern $e^z/z^n$, $\sin z/z^n$, $\cos z/z^n$ is common: expand the numerator's Taylor series, divide each term by $z^n$, identify the $1/z$ coefficient. This is faster than the derivative formula for these examples.

**The pole order is read off the denominator, but watch for cancellation.** A function like $\sin z/z^3$ might look like a triple pole, but $\sin z = z - z^3/6 + \ldots$ has a zero of order $1$ at $0$, so $\sin z/z^3$ actually has a double pole. The pole order is "order of zero of denominator minus order of zero of numerator" (with negative meaning removable).
