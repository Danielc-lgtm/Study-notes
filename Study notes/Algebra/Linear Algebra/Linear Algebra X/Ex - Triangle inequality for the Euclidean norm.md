---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Norm and Distance"
  - "Thm - Cauchy-Schwarz and the Angle in Rn"
tags: [algebra, linear-algebra, applied]
---

# Problem Statement

Prove the **triangle inequality** for the Euclidean norm on $\mathbb R^n$: for any vectors $a, b \in \mathbb R^n$,
$$\|a + b\| \leq \|a\| + \|b\|.$$

Identify the equality case: when does $\|a + b\| = \|a\| + \|b\|$?

**Recall:**

The Euclidean norm of $x \in \mathbb R^n$ is $\|x\| = \sqrt{x^T x}$ (see [[Def - Norm and Distance]]).

The key algebraic identity is $\|x + y\|^2 = \|x\|^2 + 2 x^T y + \|y\|^2$, obtained by expanding $(x + y)^T(x + y)$ using the bilinearity of the inner product.

The [[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz inequality]]:
![[Thm - Cauchy-Schwarz and the Angle in Rn#Statement]]

---

# Convergent Strategy

**Problem class.** This is a *standard norm-inequality* — establishing one of the four defining properties of a norm. The proof technique is canonical: expand the squared norm, apply Cauchy–Schwarz to the cross term, take square roots.

**Assumption pattern.** No assumptions beyond "$a, b$ are vectors in $\mathbb R^n$". The expression $\|a + b\|$ that appears in the conclusion is the cue to *expand* it via the norm-of-sum identity, converting the question into one about inner products and norms separately.

**Theorem routing.** The route is: $\|a + b\|^2 = \|a\|^2 + 2 a^T b + \|b\|^2$ (expansion) $\leq \|a\|^2 + 2|a^T b| + \|b\|^2$ (trivially) $\leq \|a\|^2 + 2\|a\|\|b\| + \|b\|^2$ ([[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz]]) $= (\|a\| + \|b\|)^2$ (perfect square). Take square roots.

**Key decision point.** The non-obvious step is to **expand $\|a + b\|^2$ rather than $\|a + b\|$ directly**. Working with the squared norm makes everything quadratic in the entries and accessible via inner-product algebra; working with $\|a + b\|$ directly tangles you in square roots. The standard discipline: when a norm is the answer to a question, square it first.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra X — Applied I — Vectors, Distance, Equations, Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Operation 4 (expand a squared norm).** This is the foundational technique here: $\|a + b\|^2 = \|a\|^2 + 2 a^T b + \|b\|^2$ converts the triangle inequality into an inner-product question.

2. **Operation 3 (Cauchy–Schwarz to bound an inner product).** Applied to the cross term $a^T b$ in the expanded squared norm: $|a^T b| \leq \|a\|\|b\|$. This is the workhorse step.

---

# Hints

> [!note]- Hint 1
> Square the inequality. Show $\|a + b\|^2 \leq (\|a\| + \|b\|)^2$, then take square roots (using non-negativity of norms).

> [!note]- Hint 2
> Expand $\|a + b\|^2$ using $\|x\|^2 = x^T x$ and bilinearity of the inner product. You should get $\|a\|^2 + 2 a^T b + \|b\|^2$.

> [!note]- Hint 3
> The cross term $2 a^T b$ might be negative, but you can bound $a^T b \leq |a^T b| \leq \|a\|\|b\|$. The first step uses the trivial inequality $x \leq |x|$; the second uses Cauchy–Schwarz.

> [!note]- Hint 4
> Equality in the triangle inequality requires equality at each step: $a^T b = |a^T b|$ (i.e., $a^T b \geq 0$) and $|a^T b| = \|a\|\|b\|$ (i.e., Cauchy–Schwarz tight). The latter holds iff $a, b$ are scalar multiples; combining with $a^T b \geq 0$ forces a *non-negative* scalar multiple.

---

# Solution

The proof has two steps. Step 1 expands $\|a + b\|^2$ and applies Cauchy–Schwarz to the cross term, obtaining $(\|a\| + \|b\|)^2$. Step 2 takes square roots and traces back through to identify the equality case as $a$ and $b$ being non-negative scalar multiples (i.e., the aligned case $\angle(a, b) = 0$).

**Step 1: Bound $\|a + b\|^2$ by $(\|a\| + \|b\|)^2$.**

Use the norm-of-sum identity and Cauchy–Schwarz.

> [!note]- Derivation
> By the expansion $\|x\|^2 = x^T x$ applied to $x = a + b$:
> $$\|a + b\|^2 = (a + b)^T(a + b) = a^T a + 2 a^T b + b^T b = \|a\|^2 + 2 a^T b + \|b\|^2,$$
> using the bilinearity and symmetry of the inner product (so $a^T b + b^T a = 2 a^T b$).
>
> Now bound the cross term. We have $a^T b \leq |a^T b|$ trivially, and by [[Thm - Cauchy-Schwarz and the Angle in Rn|Cauchy–Schwarz]], $|a^T b| \leq \|a\|\|b\|$. So $a^T b \leq \|a\|\|b\|$, and
> $$\|a + b\|^2 \leq \|a\|^2 + 2\|a\|\|b\| + \|b\|^2 = (\|a\| + \|b\|)^2,$$
> where the last equality is the standard expansion of the squared sum.

**Step 2: Take square roots and identify the equality case.**

Square roots preserve $\leq$ for non-negative reals, giving the triangle inequality.

> [!note]- Derivation
> From Step 1, $\|a + b\|^2 \leq (\|a\| + \|b\|)^2$. Both sides are non-negative, so taking the (non-negative) square root preserves the inequality:
> $$\|a + b\| \leq \|a\| + \|b\|. \quad \checkmark$$
>
> *Equality case.* Equality in the triangle inequality requires equality in *both* steps where we used an inequality.
>
> (i) $a^T b = |a^T b|$: this is $a^T b \geq 0$.
>
> (ii) $|a^T b| = \|a\|\|b\|$: by the [[Thm - Cauchy-Schwarz and the Angle in Rn|equality case of Cauchy–Schwarz]], $a, b$ are scalar multiples of each other (one of them being possibly zero).
>
> Combining: $a, b$ are scalar multiples with $a^T b \geq 0$, i.e., the scalar is non-negative. So equality in the triangle inequality holds iff one of $a, b$ is a *non-negative* scalar multiple of the other (the aligned case $\angle(a, b) = 0$, or one of them is the zero vector).

> [!note]- Complete formal solution
> *Triangle inequality.* For any $a, b \in \mathbb R^n$,
> \begin{align}
> \|a + b\|^2 &= (a + b)^T (a + b) \\
> &= a^T a + 2 a^T b + b^T b \\
> &= \|a\|^2 + 2 a^T b + \|b\|^2 \\
> &\leq \|a\|^2 + 2 |a^T b| + \|b\|^2 \\
> &\leq \|a\|^2 + 2 \|a\|\|b\| + \|b\|^2 \quad \text{(Cauchy–Schwarz)} \\
> &= (\|a\| + \|b\|)^2.
> \end{align}
> Taking square roots (both sides non-negative): $\|a + b\| \leq \|a\| + \|b\|$.
>
> *Equality case.* The chain has two inequalities; equality requires both:
> - $a^T b \leq |a^T b|$: equality iff $a^T b \geq 0$.
> - $|a^T b| \leq \|a\|\|b\|$: equality iff $a$ and $b$ are scalar multiples (Cauchy–Schwarz equality case).
>
> Combined: equality in the triangle inequality holds iff $a, b$ are *aligned*, i.e., one of them is a non-negative scalar multiple of the other (including the cases $a = 0$ or $b = 0$). $\quad\blacksquare$

---

# Key Takeaways

**The "square the norm" reflex is the most-used technique in this topic.** Whenever an inequality involves $\|a \pm b\|$ on either side, the standard first move is to square both sides — converting the norm-of-sum (which is awkward) into a sum of squared norms plus a cross-term (which is algebraic). Once squared, the inequality lives in the world of inner products, where Cauchy–Schwarz, orthogonality, and the standard identities are available. This pattern recurs everywhere: deriving the parallelogram law, proving the Pythagorean theorem, bounding the standard deviation of a sum, controlling the operator norm of a matrix product. The trigger is the appearance of $\|a + b\|$, $\|a - b\|$, or any norm-of-sum; the move is "square it".

**Cauchy–Schwarz is the workhorse inequality, applied to bound the cross-term.** Almost every time you expand a squared norm, the result contains an inner-product cross-term that you want to bound by something positive. Cauchy–Schwarz is the universal bound: $|a^T b| \leq \|a\|\|b\|$. The equality case (scalar multiples) translates directly into geometric statements about alignment, which is what makes Cauchy–Schwarz pull double duty: it gives both the upper bound and the characterisation of when the bound is tight. Once you internalise that "cross-term bound = Cauchy–Schwarz", many norm inequalities become mechanical.

**The triangle inequality has a clean geometric interpretation that should be remembered alongside the algebraic proof.** In two or three dimensions, the inequality says "the length of one side of a triangle is at most the sum of the lengths of the other two". Equality holds when the triangle is degenerate — the three "vertices" lie on a straight line, with the middle one between the other two. The general $\mathbb R^n$ case is the same picture, with "between" generalised to "on the line segment from $a$ to $a + b$, passing through $a + b/2$". This geometric picture is the most compressing way to remember the inequality: the algebraic proof is a *verification* that the picture is correct in $n$ dimensions. The trigger-reaction pattern is: "see triangle inequality → square the norm and apply Cauchy–Schwarz", but the picture is the *understanding*, and the calculation is the *proof*.
