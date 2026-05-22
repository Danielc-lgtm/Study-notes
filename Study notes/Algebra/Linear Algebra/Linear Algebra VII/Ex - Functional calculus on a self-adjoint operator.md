---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - Real Spectral Theorem"
  - "Thm - Complex Spectral Theorem"
  - "Def - Self-Adjoint Operator"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $T$ be a self-adjoint operator on a finite-dimensional inner product space, with spectral decomposition $T = \sum_j \lambda_j P_j$ ($\lambda_j$ real, $P_j$ orthogonal projections). For a function $f : \mathbb{R} \to \mathbb{F}$ defined on the spectrum $\{\lambda_j\}$, define the **functional calculus**:
$$f(T) = \sum_j f(\lambda_j) P_j.$$

(a) Verify that $f(T) g(T) = (fg)(T)$ for any two functions $f, g$ on the spectrum.

(b) Verify that $f(T)^* = \overline{f}(T)$.

(c) Conclude: if $T \geq 0$ (positive), then $\sqrt{T} = \sum_j \sqrt{\lambda_j} P_j$ is well-defined and is the unique positive operator with square $T$.

**Recall:**

![[Thm - Complex Spectral Theorem#Statement]]

The orthogonal projections $P_j$ satisfy $P_i P_j = \delta_{ij} P_j$ and $\sum_j P_j = I$ (resolution of identity).

---

# Convergent Strategy

**Problem class.** This is a computation establishing that the functional calculus is a unital $*$-homomorphism. The class is: prove an algebraic compatibility property using the spectral decomposition's orthogonality and idempotency of projections.

**Assumption pattern.** The hypothesis is the spectral decomposition $T = \sum \lambda_j P_j$ with self-adjoint projections $P_j$ satisfying the orthogonality relations. The conclusions concern algebraic identities for functions evaluated at $T$.

**Theorem routing.** The route is direct computation using $P_i P_j = \delta_{ij} P_j$ — orthogonality of distinct projections.

**Key decision point.** None substantively — this is a clean computational exercise. The skill is in writing the formulas carefully.

---

# Legal Operations Used

1. **Use orthogonality of spectral projections** — $P_i P_j = \delta_{ij} P_j$ for distinct eigenvalues.
2. **Use idempotency** — $P_j^2 = P_j$.
3. **Use self-adjointness of orthogonal projections** — $P_j^* = P_j$.

---

# Hints

> [!note]- Hint 1
> Multiply the spectral expansions: $f(T) g(T) = \sum_i f(\lambda_i) P_i \cdot \sum_j g(\lambda_j) P_j$. Use orthogonality of projections.

> [!note]- Hint 2
> $P_i P_j = \delta_{ij} P_j$, so the double sum collapses to a single sum over $j$.

> [!note]- Hint 3
> For the adjoint: $f(T)^* = (\sum_j f(\lambda_j) P_j)^* = \sum_j \overline{f(\lambda_j)} P_j^* = \sum_j \overline{f(\lambda_j)} P_j = \overline f(T)$.

---

# Solution

**Step 1: Verify $f(T) g(T) = (fg)(T)$.**

$$f(T) g(T) = \left(\sum_i f(\lambda_i) P_i\right) \left(\sum_j g(\lambda_j) P_j\right) = \sum_{i, j} f(\lambda_i) g(\lambda_j) P_i P_j = \sum_j f(\lambda_j) g(\lambda_j) P_j = (fg)(T).$$

> [!note]- Derivation
> The cross-terms $P_i P_j$ for $i \neq j$ vanish: orthogonality of distinct-eigenvalue projections gives $P_i P_j = 0$ for $i \neq j$. Diagonal terms $P_j P_j = P_j$ by idempotency. So the double sum reduces to a single sum, with each term $f(\lambda_j) g(\lambda_j) P_j = (fg)(\lambda_j) P_j$.

**Step 2: Verify $f(T)^* = \overline{f}(T)$.**

$$f(T)^* = \left(\sum_j f(\lambda_j) P_j\right)^* = \sum_j \overline{f(\lambda_j)} P_j^* = \sum_j \overline{f(\lambda_j)} P_j = \overline{f}(T).$$

> [!note]- Derivation
> Take adjoint of the sum: use conjugate-linearity in the operator $(\alpha A)^* = \overline{\alpha} A^*$ (with $\alpha = f(\lambda_j)$) and self-adjointness of orthogonal projections $P_j^* = P_j$.

**Step 3: Conclude $\sqrt T$ is well-defined and unique.**

If $T \geq 0$, then $\lambda_j \geq 0$ for all $j$, so $\sqrt{\lambda_j}$ is well-defined (non-negative real). Define $\sqrt T = \sum_j \sqrt{\lambda_j} P_j$ via functional calculus.

Verify $(\sqrt T)^2 = T$: by Step 1, $\sqrt T \cdot \sqrt T = (\sqrt{\cdot})^2(T) = \sum_j (\sqrt{\lambda_j})^2 P_j = \sum_j \lambda_j P_j = T$. ✓

Verify $\sqrt T$ is positive: self-adjoint (Step 2: $(\sqrt T)^* = \overline{\sqrt{\cdot}}(T) = \sqrt T$ since $\sqrt{\lambda_j}$ is real) and has non-negative eigenvalues $\sqrt{\lambda_j} \geq 0$. ✓

Uniqueness: if $R$ is any other positive operator with $R^2 = T$, then $R$ commutes with $T$ (since $RT = R \cdot R^2 = R^3 = R^2 \cdot R = TR$), so $R$ shares the eigenspaces of $T$, and on each eigenspace $R$ is a positive scalar with square $\lambda_j$, hence $\sqrt{\lambda_j}$. So $R = \sqrt T$. ✓

> [!note]- Complete formal solution
> $f(T) g(T) = \sum_{i,j} f(\lambda_i) g(\lambda_j) P_i P_j = \sum_j f(\lambda_j) g(\lambda_j) P_j = (fg)(T)$, using $P_i P_j = \delta_{ij} P_j$.
>
> $f(T)^* = \sum_j \overline{f(\lambda_j)} P_j^* = \sum_j \overline{f(\lambda_j)} P_j = \overline f(T)$, using $P_j^* = P_j$.
>
> For $T \geq 0$, $\lambda_j \geq 0$, so $\sqrt T := \sum_j \sqrt{\lambda_j} P_j$ is well-defined, self-adjoint (by Step 2 with $f$ real-valued, so $\overline f = f$), with non-negative eigenvalues $\sqrt{\lambda_j}$, and $(\sqrt T)^2 = T$ (by Step 1 with $f = g = \sqrt{\cdot}$). Uniqueness: any other positive square root $R$ commutes with $T$, hence shares the eigenspaces, on each of which $R = \sqrt{\lambda_j} I$. $\blacksquare$

---

# Key Takeaways

**The functional calculus is a unital $*$-homomorphism.** The two identities $f(T) g(T) = (fg)(T)$ and $f(T)^* = \overline f(T)$ together with $1(T) = I$ make the assignment $f \mapsto f(T)$ a unital $*$-homomorphism from the algebra of functions on $\sigma(T)$ to $\mathcal{L}(V)$. This algebraic structure is what makes the functional calculus useful: every algebraic identity for functions on the spectrum lifts to an identity for the corresponding operators.

**The functional calculus is the bridge from operators to functions.** Once $T$ is in spectral form, every function of $T$ can be computed by applying the function entry-wise to the eigenvalues. This is what makes operator exponentials $e^{tT}$, square roots $\sqrt T$, logarithms $\log T$, sines, cosines, etc., all well-defined for normal operators. The whole edifice of operator-theoretic calculus rests on the spectral theorem and this functional calculus structure.

**Operator identities follow from scalar identities.** Any identity for scalar functions on the spectrum lifts to operator identities: $\sqrt{T_1 T_2} = \sqrt{T_1} \sqrt{T_2}$ if $T_1$ and $T_2$ commute (so they share an eigenbasis); $e^{T_1 + T_2} = e^{T_1} e^{T_2}$ if they commute. When operators do not commute, the identities fail or become more complex (the Baker–Campbell–Hausdorff formula for non-commuting exponentials). The functional calculus separates the "easy" commuting case (where scalar identities lift) from the "hard" non-commuting case (where they do not).
