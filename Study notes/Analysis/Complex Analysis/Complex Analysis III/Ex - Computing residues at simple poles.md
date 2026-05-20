---
type: exercise
subject: complex-analysis
difficulty: "⭐"
prereqs:
  - "Def - Residue"
  - "Thm - Computing Residues"
  - "Def - Removable Singularity, Pole, Essential Singularity"
tags: [analysis, complex-analysis]
---

# Problem Statement

Compute the residues of $f(z) = 1/(z^2 - 1)$ at each of its poles.

**Recall:**

![[Def - Residue#The Definition]]

For a simple pole at $a$, $\operatorname{Res}_a f = \lim_{z \to a}(z - a) f(z)$.

For a quotient $f = g/h$ with $h$ having a simple zero at $a$ ($h(a) = 0$, $h'(a) \neq 0$) and $g(a) \neq 0$, $\operatorname{Res}_a(g/h) = g(a)/h'(a)$.

---

# Convergent Strategy

**Problem class:** Routine residue computation at simple poles of a rational function. Goal: drill the simple-pole limit and quotient formulas.

**Assumption pattern:** $f = 1/(z^2 - 1) = 1/((z - 1)(z + 1))$ has two simple poles at $z = 1$ and $z = -1$ (the denominator factors).

**Theorem routing:** [[Thm - Computing Residues|simple pole formula]] in either form. Use the factorization to identify the poles, then apply $\lim(z - a) f(z)$ or $g(a)/h'(a)$.

**Key decision point:** Use the quotient form $g(a)/h'(a)$ for elegance, or the limit form $\lim(z - a)f(z)$ for directness — both give the same answer.

---

# Legal Operations Used

1. **Factor the denominator** to identify poles: $z^2 - 1 = (z - 1)(z + 1)$.
2. **Apply the simple-pole formula** at each pole.
3. **Sanity check via the alternative formula**: limit vs quotient should agree.

---

# Hints

> [!note]- Hint 1
> Factor $z^2 - 1 = (z - 1)(z + 1)$. The poles are at $z = 1$ and $z = -1$.

> [!note]- Hint 2
> At $z = 1$: $\operatorname{Res}_1 1/((z-1)(z+1)) = \lim_{z \to 1} (z - 1)/((z - 1)(z + 1)) = \lim_{z \to 1} 1/(z + 1) = 1/2$.

> [!note]- Hint 3
> At $z = -1$: $\operatorname{Res}_{-1} = \lim_{z \to -1} (z + 1)/((z - 1)(z + 1)) = \lim_{z \to -1} 1/(z - 1) = -1/2$.

---

# Solution

**Step 1: Identify the poles**

$f(z) = 1/(z^2 - 1) = 1/((z - 1)(z + 1))$, so the poles are at $z = 1$ and $z = -1$, both simple.

**Step 2: Compute $\operatorname{Res}_1 f$**

> [!note]- Derivation
> Using the limit form:
> $$\operatorname{Res}_1 f = \lim_{z \to 1}(z - 1) f(z) = \lim_{z \to 1}\frac{z - 1}{(z - 1)(z + 1)} = \lim_{z \to 1}\frac{1}{z + 1} = \frac{1}{2}.$$
> Alternatively, using the quotient form with $g = 1, h = z^2 - 1$, $h'(z) = 2z$, so $h'(1) = 2$:
> $$\operatorname{Res}_1 f = g(1)/h'(1) = 1/2.$$
> Both methods agree.

**Step 3: Compute $\operatorname{Res}_{-1} f$**

> [!note]- Derivation
> Limit form:
> $$\operatorname{Res}_{-1} f = \lim_{z \to -1}(z + 1) f(z) = \lim_{z \to -1}\frac{z + 1}{(z - 1)(z + 1)} = \lim_{z \to -1}\frac{1}{z - 1} = \frac{1}{-2} = -\frac{1}{2}.$$
> Quotient form: $h'(-1) = 2 \cdot (-1) = -2$, so $\operatorname{Res}_{-1} f = 1/(-2) = -1/2$.

**Step 4: Sanity check**

> [!note]- Derivation
> The residues at $z = 1$ and $z = -1$ are $1/2$ and $-1/2$, summing to $0$. For a rational function on $\hat{\mathbb{C}}$, the sum of all residues (including the residue at $\infty$) is zero. $f(z) = 1/(z^2 - 1) = O(1/z^2)$ at infinity, so $\operatorname{Res}_\infty f = 0$. Consistency check: $1/2 + (-1/2) + 0 = 0$. ✓

> [!note]- Complete formal solution
> The function $f(z) = 1/(z^2 - 1) = 1/((z - 1)(z + 1))$ has simple poles at $z = 1$ and $z = -1$.
>
> By the simple pole formula:
> $$\operatorname{Res}_1 f = \lim_{z \to 1}\frac{z - 1}{(z - 1)(z + 1)} = \frac{1}{2},$$
> $$\operatorname{Res}_{-1} f = \lim_{z \to -1}\frac{z + 1}{(z - 1)(z + 1)} = -\frac{1}{2}.$$
>
> Verification by the quotient formula: with $g = 1$, $h(z) = z^2 - 1$, $h'(z) = 2z$, we get $\operatorname{Res}_a f = g(a)/h'(a) = 1/(2a)$, giving $1/2$ at $z = 1$ and $-1/2$ at $z = -1$. $\blacksquare$

---

# Key Takeaways

**The two simple-pole formulas — limit and quotient — give the same answer, and the choice between them is taste.** For most rational functions, the quotient formula $g(a)/h'(a)$ is faster: you read off $g(a)$ and $h'(a)$ without algebraic manipulation. The limit form $\lim(z - a)f(z)$ is more general (applies to any simple pole, not just quotients of holomorphic functions) and more natural to derive from the definition.

**The residue at a simple pole is "what's left after dividing out $(z - a)$".** For $f = g/((z - a) k(z))$ with $k(a) \neq 0$, the residue is $g(a)/k(a)$ — just "remove the $(z - a)$ factor and evaluate." This is the operational content of the simple-pole formula, and it's the standard mental model for residues at simple poles.

**Trigger-reaction pattern — rational function with simple zeros of denominator → simple poles, residue = numerator over derivative of denominator.** The most-used pattern in residue calculus. When you see $f = P(z)/Q(z)$ with $Q$ having distinct simple zeros (none coinciding with zeros of $P$), the residues are $P(a)/Q'(a)$ at each zero $a$ of $Q$.

**Sum-of-residues check.** For a rational function on $\hat{\mathbb{C}}$, the sum of all residues (including the residue at $\infty$) is zero. This is a powerful sanity check: if you compute residues at all finite poles and the sum doesn't match the residue at $\infty$, you've made an error.
