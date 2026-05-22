---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Left and Right Inverse of a Matrix"
tags: [algebra, linear-algebra, applied]
---

# Problem Statement

Let $A \in \mathbb R^{m \times n}$ and suppose there exists $C \in \mathbb R^{n \times m}$ with $CA = I_n$ (so $C$ is a **left inverse** of $A$).

Show that the columns of $A$ are linearly independent — equivalently, that $Ax = 0$ implies $x = 0$.

**Recall:**

The columns of an $m \times n$ matrix $A$ are **linearly independent** if $Ax = 0 \Rightarrow x = 0$ (i.e., the only linear combination of the columns that yields the zero vector is the trivial one).

A **left inverse** of $A$ is a matrix $C \in \mathbb R^{n \times m}$ satisfying $CA = I_n$. See [[Def - Left and Right Inverse of a Matrix]].

---

# Convergent Strategy

**Problem class.** This is a *direct deduction* from a hypothesis ($A$ has a left inverse) to a structural property of $A$ (linearly independent columns). It is one half of the equivalence "$A$ has a left inverse $\Leftrightarrow$ columns are linearly independent" that underpins much of the invertibility theory.

**Assumption pattern.** $A$ has a left inverse $C$ with $CA = I$. The conclusion needs to be obtained by manipulating this equation.

**Theorem routing.** Direct: multiply $Ax = 0$ on the left by $C$, use associativity and $CA = I$ to get $x = 0$. One-line proof.

**Key decision point.** The non-obvious step is **multiplying $Ax = 0$ on the left by $C$**, which "undoes" the action of $A$ via the left inverse. This is the prototypical move for left inverses: the left inverse undoes left-multiplication.

---

# Legal Operations Used

1. **Operation 10 (invoke linear independence to count and eliminate).** Directly: we are *proving* that the columns are linearly independent, which is the operation we are unlocking.

2. **Associativity of matrix multiplication** ($C(Ax) = (CA)x$): standard property, used to rearrange the product.

---

# Hints

> [!note]- Hint 1
> Suppose $Ax = 0$. Apply $C$ from the left to both sides.

> [!note]- Hint 2
> Use associativity: $C(Ax) = (CA)x$. Then use $CA = I$.

---

# Solution

The proof is a single one-line computation.

**Step 1: Apply $C$ to $Ax = 0$.**

> [!note]- Derivation
> Suppose $x \in \mathbb R^n$ satisfies $Ax = 0$. Multiplying both sides on the left by $C$:
> $$C(Ax) = C \cdot 0 = 0.$$
> By associativity of matrix multiplication, $C(Ax) = (CA)x$. Substituting the hypothesis $CA = I$:
> $$(CA)x = I x = x.$$
> So $x = 0$.

**Step 2: Conclude linear independence.**

> [!note]- Derivation
> We have shown: $Ax = 0 \Rightarrow x = 0$, for any $x \in \mathbb R^n$. This is exactly the definition of linear independence of the columns of $A$: the only linear combination of the columns that equals the zero vector is the trivial one (all coefficients zero).

> [!note]- Complete formal solution
> Let $A \in \mathbb R^{m \times n}$ have a left inverse $C \in \mathbb R^{n \times m}$ ($CA = I_n$). We show the columns of $A$ are linearly independent.
>
> Suppose $x \in \mathbb R^n$ satisfies $Ax = 0$. Then
> $$x = (CA)x = C(Ax) = C \cdot 0 = 0,$$
> using $CA = I$, then associativity, then the hypothesis $Ax = 0$. Hence $x = 0$, so the only $x$ with $Ax = 0$ is the zero vector. By definition, the columns of $A$ are linearly independent. $\quad\blacksquare$

---

# Key Takeaways

**The left inverse "undoes" left-multiplication by $A$.** The proof is one line because the left inverse is, by its definition, *exactly* the tool that converts $Ax$ back to $x$. Whenever a problem hands you a left inverse and asks for something about $A$, the standard first move is to multiply the relevant equation by the left inverse to remove $A$ from it. The trigger-reaction pattern: "left inverse $+$ equation $Ax = b$ $\to$ multiply both sides by $C$, get $x = Cb$". This is the foundation of solving over-determined linear systems and of the pseudoinverse approach to least-squares.

**Left invertibility implies linear independence of columns — but for square matrices, the converse also holds, and they are equivalent to all other invertibility conditions.** For non-square matrices, this exercise gives one direction: left inverse $\Rightarrow$ columns linearly independent. The reverse direction — columns linearly independent $\Rightarrow$ left inverse exists — also holds but requires the independence-dimension inequality to construct the left inverse explicitly. For square matrices, [[Thm - Conditions for a Square Matrix to be Invertible|all ten invertibility conditions]] are equivalent, and the present exercise is one of the bidirectional implications. This is the structural reason "linearly independent columns" is the canonical check for solvability and invertibility in applied linear algebra.

**The one-line proof reveals the structural meaning of "invertibility".** The proof did nothing except manipulate the equations algebraically — no spatial geometry, no eigenvalue analysis. This is characteristic of invertibility-style proofs: the result is purely algebraic, and the cleanest derivations are equational. The lesson generalises: when working with inverses (left, right, or two-sided), the standard technique is to multiply equations by the inverse on the appropriate side and use the cancellation $A^{-1} A = I$ (or $CA = I$, or $AB = I$). The structural insight is that invertibility is an *algebraic* property — it is about the existence of a cancelling element — not a geometric one. Geometric content (rank, dimension, surjectivity, injectivity) is *consequences* of invertibility, not its definition.
