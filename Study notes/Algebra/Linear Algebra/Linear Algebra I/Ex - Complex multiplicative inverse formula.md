---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Field"
tags: [algebra, linear-algebra]
---

# Problem Statement

Show that for every $\alpha \in \mathbb{C}$ with $\alpha \neq 0$, there exists a unique $\beta \in \mathbb{C}$ with $\alpha \beta = 1$, and derive the explicit formula

$$\alpha^{-1} = \frac{a - bi}{a^2 + b^2}, \qquad \text{when } \alpha = a + bi.$$

(LADR Exercise 1A.6.)

**Recall:**

A [[Def - Field|field]] requires multiplicative inverses for every nonzero element. For $\mathbb{C}$ this is one of the axioms to verify in showing $\mathbb{C}$ is a field. The complex conjugate is $\overline{a + bi} = a - bi$, and the modulus squared is $|a + bi|^2 = a^2 + b^2$.

---

# Convergent Strategy

**Problem class:** This is an **existence-and-uniqueness** problem for an algebraic equation $\alpha \beta = 1$. The pattern is to write the equation in terms of real coordinates, solve the resulting real system, and verify uniqueness.

**Assumption pattern:** $\alpha = a + bi \neq 0$, so $(a, b) \neq (0, 0)$, hence $a^2 + b^2 > 0$ (positive over $\mathbb{R}$).

**Theorem routing:** Direct: write $\beta = c + di$ and expand $\alpha \beta = (ac - bd) + (ad + bc) i = 1 + 0 i$. The real and imaginary parts give a $2 \times 2$ linear system; solve.

**Key decision point:** The slickest derivation multiplies $\alpha$ by its conjugate $\overline{\alpha} = a - bi$: $\alpha \overline{\alpha} = a^2 + b^2$, a positive real. Hence $\alpha^{-1} = \overline{\alpha} / (a^2 + b^2)$. The trick (multiplying by the conjugate) is the natural one for any field of the form $K(\sqrt{-d})$ and recurs throughout number theory.

---

# Legal Operations Used

1. **Multiply numerator and denominator by the conjugate.** A reusable trick for rationalizing complex denominators and for inverting in $K(\sqrt{-d})$.
2. **Solve a $2 \times 2$ real linear system from real/imaginary parts.** The standard pattern for converting a complex equation into two real equations.

---

# Hints

> [!note]- Hint 1
> Multiply both numerator and denominator of $1/\alpha$ by the conjugate $\overline{\alpha} = a - bi$.

> [!note]- Hint 2
> $\alpha \cdot \overline{\alpha} = (a + bi)(a - bi) = a^2 - (bi)^2 = a^2 + b^2$, a nonzero real.

---

# Solution

The plan: multiply by the conjugate, get a real denominator, and divide.

**Step 1: Compute $\alpha \cdot \overline{\alpha} = a^2 + b^2$.**

> [!note]- Derivation
> $(a + bi)(a - bi) = a^2 - abi + abi - b^2 i^2 = a^2 + b^2$, using $i^2 = -1$ and cancellation of the cross terms.

**Step 2: Identify $\alpha^{-1} = \overline{\alpha}/(a^2 + b^2)$.**

> [!note]- Derivation
> Since $\alpha \neq 0$, $(a, b) \neq (0, 0)$, so $a^2 + b^2 > 0$ in $\mathbb{R}$, hence has a real reciprocal. Define $\beta = (a - bi) / (a^2 + b^2)$. Then $\alpha \beta = (a + bi)(a - bi)/(a^2 + b^2) = (a^2 + b^2)/(a^2 + b^2) = 1$. Uniqueness: if $\alpha \beta' = 1$ also, then $\beta = \beta \cdot 1 = \beta \cdot \alpha \beta' = (\beta \alpha) \beta' = 1 \cdot \beta' = \beta'$.

> [!note]- Complete formal solution
> Let $\alpha = a + bi \in \mathbb{C}$ with $\alpha \neq 0$. Then $(a, b) \neq (0, 0)$, so $a^2 + b^2 > 0$.
>
> Set $\beta = (a - bi)/(a^2 + b^2)$. Then
> $$\alpha \beta = \frac{(a + bi)(a - bi)}{a^2 + b^2} = \frac{a^2 + b^2}{a^2 + b^2} = 1.$$
>
> So $\beta$ is a multiplicative inverse of $\alpha$. Uniqueness: if $\beta'$ also satisfies $\alpha \beta' = 1$, then $\beta' = \beta' \cdot 1 = \beta' \cdot \alpha \beta = (\alpha \beta') \beta = 1 \cdot \beta = \beta$ (using commutativity and associativity of complex multiplication). $\blacksquare$

---

# Key Takeaways

**The conjugate trick rationalizes denominators in any quadratic field.** The same maneuver $\alpha \cdot \overline{\alpha} = a^2 + b^2$ works in $\mathbb{Q}(\sqrt{-d})$ and more generally in $K(\sqrt{-d})$ for any field $K$: multiply by the Galois conjugate to land in $K$. This is the source of the **norm map** in algebraic number theory and the technique used to invert elements in many concrete number rings. Recognizing the conjugate as a useful symmetry is one of the first steps in working with field extensions.

**Uniqueness follows from associativity and the inverse property, generally.** The uniqueness argument $\beta = \beta \alpha \beta' = \beta'$ is purely structural — it uses associativity, the identity property of $1$, and the inverse property of $\beta$. It works in any monoid in which inverses exist, including groups and rings with units. The same pattern proved uniqueness of inverses in [[Def - Group|group theory]] and applies to multiplicative inverses in fields without modification.

**Modulus squared $|\alpha|^2 = a^2 + b^2$ is the geometric content of $\alpha \overline{\alpha}$.** The product $\alpha \overline{\alpha} = a^2 + b^2$ is the squared distance from $\alpha$ to the origin in the Argand plane. The fact that it is real and non-negative is the geometric source of $\mathbb{C}$ being an inner-product space (over $\mathbb{R}$, via $\langle \alpha, \beta \rangle = \operatorname{Re}(\alpha \overline{\beta})$). This bridges the field-theoretic structure of $\mathbb{C}$ with its geometric structure, and is the prototype of inner-product spaces in [[Linear Algebra VI — §6 Inner Product Spaces]].
