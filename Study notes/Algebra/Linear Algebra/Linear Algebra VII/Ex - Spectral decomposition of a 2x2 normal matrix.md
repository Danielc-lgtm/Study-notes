---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Thm - Complex Spectral Theorem"
  - "Def - Normal Operator"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $T = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ acting on $\mathbb{C}^2$ with the standard Hermitian inner product.

(a) Show that $T$ is normal.
(b) Compute the eigenvalues of $T$.
(c) Find an orthonormal eigenbasis of $T$.
(d) Write the spectral decomposition $T = \sum_j \lambda_j P_j$.

**Recall:**

![[Thm - Complex Spectral Theorem#Statement]]

A [[Def - Normal Operator|normal]] operator is one satisfying $T T^* = T^* T$. The spectral decomposition writes $T = \sum_j \lambda_j P_j$ where $\lambda_j$ are the eigenvalues and $P_j$ are orthogonal projections onto eigenspaces.

---

# Convergent Strategy

**Problem class.** This is a concrete spectral decomposition computation: verify normality of a small matrix, diagonalise via the spectral theorem, and write the answer in spectral form.

**Assumption pattern.** The matrix is given explicitly; the calculation is mechanical once normality is verified.

**Theorem routing.** Compute $T T^*$ and $T^* T$; check equality. Then find the characteristic polynomial and roots. Then find eigenvectors and normalise. Then express orthogonal projections as outer products of eigenvectors.

**Key decision point.** None — this is a routine computational exercise. The skill is in keeping the bookkeeping organised.

---

# Legal Operations Used

1. **Verify normality** by computing $TT^*$ and $T^*T$ and checking equality.
2. **Spectral theorem to diagonalise** a normal operator.
3. **Express projections as $f f^*$** outer products for unit eigenvectors $f$.

---

# Hints

> [!note]- Hint 1
> Verify normality: compute $T^* = \overline{T^t} = T^t$ (entries are real), then $TT^t$ and $T^t T$ — check they coincide.

> [!note]- Hint 2
> The characteristic polynomial is $\det(T - \lambda I) = (1-\lambda)^2 + 1 = \lambda^2 - 2\lambda + 2$. Roots are $\lambda = 1 \pm i$.

> [!note]- Hint 3
> Eigenvectors: for $\lambda = 1 + i$, solve $(T - (1+i)I) v = 0$. Normalise. Repeat for $\lambda = 1 - i$.

---

# Solution

**Step 1: Verify normality.**

$T^t = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$ (since $T$ has real entries, $T^* = T^t$).

$TT^t = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = 2I$.

$T^t T = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = 2I$.

So $TT^* = T^*T$, i.e., $T$ is normal.

> [!note]- Derivation
> Direct matrix multiplication. The result $TT^* = 2I$ also reveals that $T/\sqrt{2}$ is unitary.

**Step 2: Compute eigenvalues.**

$\det(T - \lambda I) = (1 - \lambda)^2 - (-1)(1) = (1-\lambda)^2 + 1 = \lambda^2 - 2\lambda + 2$.

Roots: $\lambda = \frac{2 \pm \sqrt{4 - 8}}{2} = 1 \pm i$.

**Step 3: Compute eigenvectors.**

For $\lambda_1 = 1 + i$: $(T - (1+i)I) v = 0$ gives $\begin{pmatrix} -i & -1 \\ 1 & -i \end{pmatrix} v = 0$. The two equations are equivalent (the second is $i$ times the first): $-i v_1 - v_2 = 0$, so $v_2 = -i v_1$. Take $v_1 = 1$: eigenvector $(1, -i)$. Normalise: $\|(1, -i)\| = \sqrt{1 + 1} = \sqrt 2$, so $f_1 = \frac{1}{\sqrt 2} (1, -i)$.

For $\lambda_2 = 1 - i$: similarly eigenvector $(1, i)$, normalised $f_2 = \frac{1}{\sqrt 2} (1, i)$.

> [!note]- Derivation
> Check orthogonality: $\langle f_1, f_2 \rangle = \frac{1}{2}(1 \cdot \overline{1} + (-i) \cdot \overline{i}) = \frac{1}{2}(1 + (-i)(-i)) = \frac{1}{2}(1 - 1) = 0$. ✓ (Note: $\overline{i} = -i$.)

**Step 4: Spectral decomposition.**

$P_1 = f_1 f_1^* = \frac{1}{2} \begin{pmatrix} 1 \\ -i \end{pmatrix} \begin{pmatrix} 1 & i \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 & i \\ -i & 1 \end{pmatrix}$.

$P_2 = f_2 f_2^* = \frac{1}{2} \begin{pmatrix} 1 \\ i \end{pmatrix} \begin{pmatrix} 1 & -i \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 & -i \\ i & 1 \end{pmatrix}$.

Verify $P_1 + P_2 = I$: $\frac{1}{2}\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I$. ✓

The spectral decomposition is
$$T = (1 + i) P_1 + (1 - i) P_2 = \frac{1+i}{2}\begin{pmatrix} 1 & i \\ -i & 1 \end{pmatrix} + \frac{1-i}{2}\begin{pmatrix} 1 & -i \\ i & 1 \end{pmatrix}.$$

> [!note]- Complete formal solution
> $T = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$, $T^* = T^t = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$. Direct computation: $TT^* = T^*T = 2I$, so $T$ is normal.
>
> Characteristic polynomial: $(1-\lambda)^2 + 1$, roots $\lambda = 1 \pm i$.
>
> Eigenvectors: $(1, -i)$ for $\lambda = 1 + i$ and $(1, i)$ for $\lambda = 1 - i$; orthogonal in the Hermitian inner product. Normalised: $f_1 = \frac{1}{\sqrt 2}(1, -i)$, $f_2 = \frac{1}{\sqrt 2}(1, i)$.
>
> Spectral decomposition: $T = (1+i) P_1 + (1-i) P_2$ with $P_j = f_j f_j^*$. $\blacksquare$

---

# Key Takeaways

**Verifying normality is mechanical.** Compute $TT^*$ and $T^*T$ as matrix products, check entry by entry. For small matrices this is the fastest verification; for general $T$, characterisations (2)–(4) of normality may be cheaper but for explicit small matrices, direct comparison wins.

**Real matrices over $\mathbb{C}$ still need complex eigenvalues.** $T$ has real entries but eigenvalues $1 \pm i$ — the complex spectral theorem applies because we are working over $\mathbb{C}$. Over $\mathbb{R}$, this $T$ is normal but not self-adjoint, and the [[Thm - Real Spectral Theorem|real spectral theorem]] does not apply. To diagonalise over $\mathbb{R}$, one block-diagonalises into $2 \times 2$ rotation blocks; over $\mathbb{C}$, the diagonalisation has eigenvalues $1 \pm i$.

**The spectral decomposition reveals structure.** $T = (1+i) P_1 + (1-i) P_2$ shows $T = (1)(P_1 + P_2) + i(P_1 - P_2) = I + i (P_1 - P_2)$. The operator $P_1 - P_2$ is the difference of two orthogonal projections, hence self-adjoint with eigenvalues $\pm 1$. So $T = I + iH$ for a self-adjoint $H$ — and $T$ is a "complex scalar plus pure imaginary self-adjoint" operator, exhibiting its complex structure.
