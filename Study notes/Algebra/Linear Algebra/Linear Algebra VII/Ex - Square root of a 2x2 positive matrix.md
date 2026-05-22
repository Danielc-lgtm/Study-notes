---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Thm - Positive Operators Have a Unique Square Root"
  - "Def - Positive Operator"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $T = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$ acting on $\mathbb{R}^2$ with the standard inner product.

(a) Show that $T$ is positive definite.
(b) Compute the eigenvalues and an orthonormal eigenbasis of $T$.
(c) Compute the unique positive square root $\sqrt T$.

**Recall:**

![[Thm - Positive Operators Have a Unique Square Root#Statement]]

A self-adjoint matrix is [[Def - Positive Operator|positive definite]] iff all eigenvalues are positive. The positive square root is constructed by taking square roots of eigenvalues in the spectral decomposition.

---

# Convergent Strategy

**Problem class.** Concrete computation of a matrix square root using the spectral theorem.

**Theorem routing.** Diagonalise $T$ via the spectral theorem, take square roots of eigenvalues, reassemble.

**Key decision point.** Whether to compute $\sqrt T$ via the spectral decomposition formula $\sqrt T = O \sqrt D O^t$ (orthogonal diagonalisation then square-root eigenvalues), or via a direct ansatz $\sqrt T = aI + bT$ exploiting that $T$ is $2 \times 2$. Both routes work; the spectral decomposition is more general.

---

# Hints

> [!note]- Hint 1
> Eigenvalues of $T$: compute the characteristic polynomial $\det(T - \lambda I) = (5 - \lambda)^2 - 16 = \lambda^2 - 10\lambda + 9$. Factor.

> [!note]- Hint 2
> Eigenvectors for $\lambda = 9, 1$. The eigenvectors are $(1, 1)/\sqrt 2$ and $(1, -1)/\sqrt 2$ — orthonormal.

> [!note]- Hint 3
> Spectral decomposition: $T = 9 P_1 + 1 \cdot P_2$ with $P_j$ orthogonal projections onto eigenvectors. Square root: $\sqrt T = 3 P_1 + 1 \cdot P_2$.

---

# Solution

The plan is to diagonalise $T$ via the spectral theorem, take square roots of the eigenvalues, and reassemble. Three steps: positive-definiteness via eigenvalue signs, orthonormal eigenbasis, and the square root by functional calculus.

**Step 1: $T$ is positive definite, with eigenvalues $\{1, 9\}$.**

> [!note]- Derivation
> The characteristic polynomial of $T$ is $\det(T - \lambda I) = (5 - \lambda)^2 - 16 = \lambda^2 - 10 \lambda + 9 = (\lambda - 9)(\lambda - 1)$. So the eigenvalues are $\lambda = 1, 9$, both positive. Since $T$ is symmetric (real, self-adjoint) with positive eigenvalues, $T$ is positive definite.

**Step 2: Orthonormal eigenbasis $\{u_1, u_2\} = \{(1, 1)/\sqrt 2, (1, -1)/\sqrt 2\}$.**

> [!note]- Derivation
> For $\lambda = 9$: $(T - 9I) v = 0$ gives $\begin{pmatrix} -4 & 4 \\ 4 & -4 \end{pmatrix} v = 0$. Solution: $v_1 = v_2$. Take $v = (1, 1)$, normalised $u_1 = (1, 1)/\sqrt 2$.
>
> For $\lambda = 1$: $(T - I) v = 0$ gives $\begin{pmatrix} 4 & 4 \\ 4 & 4 \end{pmatrix} v = 0$. Solution: $v_1 = -v_2$. Take $v = (1, -1)$, normalised $u_2 = (1, -1)/\sqrt 2$.
>
> Check orthogonality: $\langle u_1, u_2 \rangle = \frac{1}{2}(1 \cdot 1 + 1 \cdot (-1)) = 0$. ✓

**Step 3: Square root is $\sqrt T = 3 P_1 + P_2 = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.**

> [!note]- Derivation
> With $P_j = u_j u_j^t$, the orthogonal projection onto the $j$-th eigenspace:
>
> $P_1 = \frac{1}{2} \begin{pmatrix} 1 \\ 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.
>
> $P_2 = \frac{1}{2} \begin{pmatrix} 1 \\ -1 \end{pmatrix} \begin{pmatrix} 1 & -1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$.
>
> Square root via functional calculus: $\sqrt T = \sqrt 9 \cdot P_1 + \sqrt 1 \cdot P_2 = 3 P_1 + P_2$:
> $$\sqrt T = 3 \cdot \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} + \frac{1}{2} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 4 & 2 \\ 2 & 4 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}.$$
>
> Verify: $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}^2 = \begin{pmatrix} 4 + 1 & 2 + 2 \\ 2 + 2 & 1 + 4 \end{pmatrix} = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix} = T$. ✓

> [!note]- Complete formal solution
> Eigenvalues of $T$: $\lambda = 1, 9$; both positive, so $T$ is positive definite.
>
> Orthonormal eigenvectors: $u_1 = (1, 1)/\sqrt 2$ for $\lambda = 9$ and $u_2 = (1, -1)/\sqrt 2$ for $\lambda = 1$.
>
> Spectral decomposition: $T = 9 P_1 + P_2$ with $P_j = u_j u_j^t$. Square root: $\sqrt T = 3 P_1 + P_2 = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$. Verify $(\sqrt T)^2 = T$. $\blacksquare$

---

# Key Takeaways

**Square root construction: spectral decompose, square-root eigenvalues, reassemble.** This three-step recipe — diagonalise, function-of-eigenvalues, reassemble — is the engine of all functional calculus. For polynomials, exponentials, logarithms, sines, etc., the same three steps apply.

**The square root is self-adjoint, not the original operator's "off-diagonal data".** $\sqrt T$ is self-adjoint and shares the eigenbasis of $T$. It is *not* a triangular factor (like the Cholesky factor); it is the symmetric positive square root, distinct from Cholesky.

**Verification by squaring is the easiest check.** Computing $\sqrt T$ via spectral decomposition involves real number square roots and matrix multiplications. The cleanest sanity check is to square the candidate $\sqrt T$ and verify the result equals $T$. This costs one matrix multiplication, comparable to the spectral decomposition itself but much simpler conceptually.
