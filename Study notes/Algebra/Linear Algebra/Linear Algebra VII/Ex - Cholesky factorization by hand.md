---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - Cholesky Factorization"
  - "Def - Positive Operator"
tags: [algebra, linear-algebra]
---

# Problem Statement

Compute the Cholesky factorisation $T = R^* R$ (with $R$ upper-triangular, positive diagonal) of the positive definite matrix
$$T = \begin{pmatrix} 4 & 2 & 6 \\ 2 & 5 & 5 \\ 6 & 5 & 14 \end{pmatrix}.$$

**Recall:**

![[Thm - Cholesky Factorization#Statement]]

The Cholesky factorisation is computed entry-by-entry from the equations $T_{ij} = (R^* R)_{ij} = \sum_k R_{ki} R_{kj}$, working through the entries in a specific order (diagonal first in each column, then off-diagonal entries).

---

# Convergent Strategy

**Problem class.** Direct computation by the Cholesky algorithm, which is a systematic walking-through of the equations $T_{ij} = \sum_k R_{ki} R_{kj}$ for the unknown entries of $R$.

**Theorem routing.** Use $T = R^* R$ entry-by-entry. The off-diagonal entries above the diagonal of $R$ are determined by the corresponding off-diagonal entries of $T$ once the row above is known; the diagonal entries are determined by the diagonal entries of $T$ after subtracting earlier contributions.

**Key decision point.** The order of computation. Standard order: compute $R_{11}, R_{12}, R_{13}, R_{22}, R_{23}, R_{33}$ — going row-by-row, left-to-right within each row.

---

# Hints

> [!note]- Hint 1
> $R$ is upper-triangular: $R_{ij} = 0$ for $i > j$. The first row of $R$ has entries $R_{11}, R_{12}, R_{13}$; the second row has $R_{22}, R_{23}$; the third has $R_{33}$.

> [!note]- Hint 2
> First column of $T$: $T_{11} = R_{11}^2$, so $R_{11} = \sqrt{T_{11}} = 2$. Then $T_{21} = R_{11} R_{12}$, so $R_{12} = T_{21}/R_{11} = 2/2 = 1$. Similarly $R_{13} = T_{31}/R_{11} = 6/2 = 3$.

> [!note]- Hint 3
> Second column of $T$: $T_{22} = R_{12}^2 + R_{22}^2$, so $R_{22}^2 = T_{22} - R_{12}^2 = 5 - 1 = 4$, $R_{22} = 2$. Then $T_{32} = R_{12} R_{13} + R_{22} R_{23}$, so $R_{23} = (T_{32} - R_{12} R_{13})/R_{22} = (5 - 1 \cdot 3)/2 = 1$.

---

# Solution

The plan is to walk through the Cholesky algorithm column-by-column, using the matrix equation $T = R^*R$ to determine each entry of $R$ once the previous columns are known. The diagonal entries $R_{jj}$ are positive square roots; the off-diagonal entries above the diagonal are determined by the corresponding entries of $T$ minus contributions from previously computed entries.

**Step 1: First column. $R_{11} = 2$, $R_{12} = 1$, $R_{13} = 3$.**

> [!note]- Derivation
> $R$ is upper-triangular, so $R^*$ is lower-triangular. The product $(R^*R)_{ij} = \sum_k \overline{R_{ki}} R_{kj}$, summed over $k \leq \min(i, j)$ (since $R_{ki} = 0$ for $k > i$).
>
> $T_{11} = (R^*R)_{11} = R_{11}^2$. So $R_{11} = \sqrt{4} = 2$.
>
> $T_{21} = (R^*R)_{21} = R_{12} R_{11}$ (only $k = 1$ contributes since $R_{k1} = 0$ for $k > 1$). So $R_{12} = T_{21}/R_{11} = 2/2 = 1$.
>
> $T_{31} = (R^*R)_{31} = R_{13} R_{11}$. So $R_{13} = T_{31}/R_{11} = 6/2 = 3$.

**Step 2: Second column. $R_{22} = 2$, $R_{23} = 1$.**

> [!note]- Derivation
> $T_{22} = (R^*R)_{22} = R_{12}^2 + R_{22}^2$. So $R_{22}^2 = T_{22} - R_{12}^2 = 5 - 1 = 4$, hence $R_{22} = 2$ (positive square root).
>
> $T_{32} = (R^*R)_{32} = R_{13} R_{12} + R_{23} R_{22}$. So $R_{23} = (T_{32} - R_{13} R_{12})/R_{22} = (5 - 3)/2 = 1$.

**Step 3: Third column. $R_{33} = 2$.**

> [!note]- Derivation
> $T_{33} = (R^*R)_{33} = R_{13}^2 + R_{23}^2 + R_{33}^2 = 9 + 1 + R_{33}^2 = 10 + R_{33}^2$. So $R_{33}^2 = T_{33} - 10 = 14 - 10 = 4$, hence $R_{33} = 2$.

**Final answer:**
$$R = \begin{pmatrix} 2 & 1 & 3 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}, \qquad R^* R = T. ✓$$

> [!note]- Complete formal solution
> Following the Cholesky algorithm:
> - $R_{11} = \sqrt{T_{11}} = 2$, $R_{12} = T_{21}/R_{11} = 1$, $R_{13} = T_{31}/R_{11} = 3$.
> - $R_{22} = \sqrt{T_{22} - R_{12}^2} = \sqrt{4} = 2$, $R_{23} = (T_{32} - R_{12}R_{13})/R_{22} = 1$.
> - $R_{33} = \sqrt{T_{33} - R_{13}^2 - R_{23}^2} = \sqrt{4} = 2$.
>
> So $R = \begin{pmatrix} 2 & 1 & 3 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$, and $T = R^* R$. $\blacksquare$

---

# Key Takeaways

**The Cholesky algorithm is direct, with no spectral computations.** Unlike the symmetric square root $\sqrt T$ (which requires eigendecomposition), the Cholesky factor is computed directly from the entries of $T$ by a finite sequence of arithmetic operations. This is what makes it computationally cheap: $O(n^3/6)$ operations for an $n \times n$ matrix, no eigenvalue solves.

**Each new diagonal entry has a positivity check.** At each step, computing the diagonal entry $R_{jj}$ requires $T_{jj} - \sum_{k < j} R_{kj}^2 > 0$. If this quantity is ever non-positive, the matrix $T$ is not positive definite. This is the algorithm's built-in positive-definiteness check: Cholesky fails (with a non-positive number under a square root) iff $T$ is not positive definite. Sylvester's criterion is the underlying reason: the leading principal minors of $T$ are exactly the squared partial products of the diagonal entries of $R$.

**The Cholesky factor is a triangular "square root", not a self-adjoint square root.** Both $R$ and $\sqrt T$ satisfy "something squared equals $T$" — $R^* R = T$ and $(\sqrt T)^2 = T$ — but they are different operators. $R$ is upper-triangular; $\sqrt T$ is self-adjoint. The two "square roots" of a positive operator answer different questions: $\sqrt T$ for spectral functional calculus, $R$ for triangular solving of linear systems.
