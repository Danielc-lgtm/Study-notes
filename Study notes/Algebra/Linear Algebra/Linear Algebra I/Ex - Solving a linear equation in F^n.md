---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Field"
  - "Def - Vector Space"
tags: [algebra, linear-algebra]
---

# Problem Statement

Find $x \in \mathbb{R}^4$ such that

$$(4, -3, 1, 7) + 2 x = (5, 9, -6, 8).$$

More generally: given $v, w$ in a vector space $V$ over $\mathbb{F}$, explain why there exists a *unique* $x \in V$ such that $v + 3 x = w$.

(LADR Exercises 1A.9 and 1B.3.)

**Recall:**

A [[Def - Vector Space|vector space]] over $\mathbb{F}$ has well-defined addition, additive inverses, and scalar multiplication, with $(-v) + v = 0$ and division by a nonzero scalar via the inverse $1/\lambda$ in $\mathbb{F}$.

---

# Convergent Strategy

**Problem class:** This is a **linear equation solving** problem in the simplest setting — a single linear equation in one unknown vector. The pattern is the same as solving $a + b x = c$ over $\mathbb{R}$: subtract $a$, divide by $b$. The vector-space version uses additive inverses and scalar division.

**Assumption pattern:** $v, w$ in a vector space over a field $\mathbb{F}$, and the scalar (here $3$) is nonzero in $\mathbb{F}$ — so it has a multiplicative inverse $1/3$.

**Theorem routing:** Direct — invoke [[Thm - Uniqueness of Additive Identity and Inverses]] for the well-definedness of $-v$, then use distributivity to manipulate $v + 3x = w$ into $x = \frac{1}{3}(w - v)$.

**Key decision point:** The non-obvious step (only because students sometimes overlook it) is **using that the scalar $3$ has an inverse in $\mathbb{F}$**. This is the field axiom of multiplicative inverses for nonzero elements. In a vector space over a ring (a module), the same equation might have no solution or multiple solutions.

---

# Legal Operations Used

1. **Solve a linear equation by subtracting and dividing** (operation 7 from the topic page). Applied here: subtract $v$ from both sides of $v + \lambda x = w$, then multiply by $1/\lambda$. The cancellation step uses uniqueness of additive inverses ([[Thm - Uniqueness of Additive Identity and Inverses]]) implicitly.

2. **Use the multiplicative inverse of a nonzero scalar in $\mathbb{F}$** (operation 7 from the topic page, by way of the field axioms). Applied here: $1/3 \in \mathbb{F}$ exists because $3 \neq 0$ in $\mathbb{R}$ (more generally, $\mathbb{F}$ being a [[Def - Field|field]] guarantees inverses for all nonzero scalars).

---

# Hints

> [!note]- Hint 1
> Subtract $(4, -3, 1, 7)$ from both sides, then divide by the scalar $2$.

> [!note]- Hint 2
> $x = \frac{1}{2}((5, 9, -6, 8) - (4, -3, 1, 7)) = \frac{1}{2}(1, 12, -7, 1)$.

---

# Solution

Plan: solve mechanically — subtract from both sides, then divide.

**Step 1: Subtract $(4, -3, 1, 7)$ from both sides.**

> [!note]- Derivation
> $2x = (5, 9, -6, 8) - (4, -3, 1, 7) = (1, 12, -7, 1)$.

**Step 2: Divide by $2$ (multiplication by $1/2$).**

> [!note]- Derivation
> $x = \frac{1}{2}(1, 12, -7, 1) = (1/2, 6, -7/2, 1/2)$.

**Step 3: Verify uniqueness in the general setting.**

> [!note]- Derivation
> If $v + 3 x = w$ and $v + 3 x' = w$, subtracting gives $3(x - x') = 0$. Then $x - x' = \frac{1}{3} \cdot 3 (x - x') = \frac{1}{3} \cdot 0 = 0$, so $x = x'$.

> [!note]- Complete formal solution
> Given the equation $(4, -3, 1, 7) + 2x = (5, 9, -6, 8)$, add the additive inverse of $(4, -3, 1, 7)$ to both sides: $2 x = (1, 12, -7, 1)$. Multiplying both sides by the scalar $\frac{1}{2}$: $x = (1/2, 6, -7/2, 1/2)$. Verification by substitution: $(4, -3, 1, 7) + 2 (1/2, 6, -7/2, 1/2) = (4, -3, 1, 7) + (1, 12, -7, 1) = (5, 9, -6, 8)$. $\checkmark$
>
> **General case.** Given $v, w \in V$, the equation $v + 3 x = w$ has the unique solution $x = \frac{1}{3}(w - v) = \frac{1}{3}(w + (-v))$. Existence: substitute $x = \frac{1}{3}(w - v)$ into $v + 3x = v + (w - v) = w$. Uniqueness: if $v + 3x = v + 3 x'$, then by [[Thm - Uniqueness of Additive Identity and Inverses|cancellation]] (add $-v$ to both sides) $3x = 3x'$, and multiplying by $1/3$ gives $x = x'$. $\blacksquare$

---

# Key Takeaways

**Linear equations in one unknown over a field have unique solutions.** The equation $v + \lambda x = w$ with $\lambda \neq 0$ has the unique solution $x = (w - v)/\lambda$ in any vector space over a field. The two ingredients are additive cancellation (additive inverses in $V$) and scalar division (multiplicative inverses for nonzero scalars in $\mathbb{F}$). Both are field-axiom-level features; their conjunction makes vector spaces over fields the natural setting for linear equations. Over a ring (a [[Def - Module|module]]) the same equation might have multiple solutions or none, illustrating again why the field hypothesis matters.

**Cancellation is the operational form of "additive inverses are unique".** The step $v + 3x = v + 3x' \Rightarrow 3x = 3x'$ is the cancellation law in $V$, and it follows from [[Thm - Uniqueness of Additive Identity and Inverses|uniqueness of additive inverses]]: add $-v$ to both sides and use associativity. Cancellation is the most-used algebraic consequence of inverses, and is the engine of solving linear equations throughout the chapter and beyond. Recognizing cancellation in disguise — wherever you can subtract a common term — saves work in countless proofs.
