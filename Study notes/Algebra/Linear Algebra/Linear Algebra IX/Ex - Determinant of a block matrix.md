---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Determinant"
  - "Thm - Determinant is Multiplicative"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $A, D$ be square matrices of sizes $m \times m$ and $k \times k$ respectively, $B$ an $m \times k$ matrix, $C$ a $k \times m$ matrix.

(a) **Block-triangular case.** Prove that
$$\det \begin{pmatrix} A & B \\ 0 & D \end{pmatrix} \;=\; \det(A) \cdot \det(D).$$

(b) **Block matrix with invertible $D$.** If $D$ is invertible, prove the **Schur complement formula**:
$$\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} \;=\; \det(D) \cdot \det(A - B D^{-1} C).$$

(c) **Symmetric block case.** If $D$ is invertible and $B = C^t$ (the matrix is symmetric), explain how (b) gives the determinant in terms of a Schur complement.

**Recall:**

![[Def - Determinant#The Definition]]

The Leibniz formula gives $\det A = \sum_\sigma \operatorname{sign}(\sigma) \prod_k A_{\sigma(k), k}$.

![[Thm - Determinant is Multiplicative#Statement]]

For two square matrices of the same size, $\det(AB) = \det A \cdot \det B$.

A **block matrix** of the form $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$ with $A$ of size $m \times m$ and $D$ of size $k \times k$ is an $(m + k) \times (m + k)$ matrix with the indicated block structure.

The **Schur complement** of $D$ in the block matrix is $A - B D^{-1} C$ (assuming $D$ is invertible). It is the "effective matrix in the first block after eliminating the second block via Gaussian elimination".

---

# Convergent Strategy

**Problem class.** This is *determinant computation by factorisation*: factor the block matrix into a product of simpler matrices whose [[Def - Determinant|determinants]] are known, then apply [[Thm - Determinant is Multiplicative|multiplicativity]]. This is one of the standard techniques in linear algebra, and a recurring qualifying-exam pattern.

**Assumption pattern.** Block structure: a matrix split into blocks, with some block being zero (part a) or invertible (parts b, c). The block structure is what lets us factor the matrix; the zero or invertibility is what makes the factorisation clean.

**Theorem routing.** For (a), apply the Leibniz formula and use a Sylvester-style permutation analysis: the only contributing permutations are those that respect the block structure. Alternatively, factor $\begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \begin{pmatrix} A & 0 \\ 0 & I \end{pmatrix} \begin{pmatrix} I & A^{-1} B \\ 0 & D \end{pmatrix}$ (assuming $A$ invertible) and use multiplicativity. For (b), use the **Schur factorisation**: $\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} I & B D^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A - B D^{-1} C & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} I & 0 \\ D^{-1} C & I \end{pmatrix}$. The first and last factors are block-triangular with identity diagonal blocks, so $\det = 1$. The middle factor is block-diagonal, so $\det = \det(A - BD^{-1}C) \cdot \det D$. Multiplying: $\det = \det D \cdot \det(A - B D^{-1} C)$.

**Key decision point.** The non-obvious move is the Schur factorisation: writing the block matrix as a product of three block-triangular matrices with the "interaction" $B D^{-1} C$ absorbed into the upper-left block. This is the linear-algebra version of the Gauss elimination step "eliminate $C$ using $D$".

---

# Legal Operations Used

1. **Compute a determinant via the Leibniz formula on a structured matrix** (operation in spirit, from operation 6). For (a), the block-triangular structure means only permutations respecting the blocks contribute.

2. **Apply multiplicativity $\det(ST) = \det S \det T$** (operation 8 from the topic page). For (b), the Schur factorisation expresses the block matrix as a product of three matrices, with multiplicativity reducing the calculation.

3. **Recognise block-diagonal matrices have determinant equal to the product of block [[Def - Determinant|determinants]]** (operation 6 specialised). This is essentially (a) applied twice.

---

# Hints

> [!note]- Hint 1
> For (a), use the Leibniz formula. Identify which permutations $\sigma$ of $\{1, \dots, m + k\}$ can give a nonzero contribution, given that the $(i, j)$-entry is zero for $i \in \{m+1, \dots, m+k\}$ and $j \in \{1, \dots, m\}$.

> [!note]- Hint 2
> For (a), nonzero permutations must satisfy $\sigma(j) \in \{1, \dots, m\}$ when $j \in \{1, \dots, m\}$, and (consequently) $\sigma(j) \in \{m+1, \dots, m+k\}$ for $j \in \{m+1, \dots, m+k\}$. So $\sigma$ splits as $\sigma_1$ on the first block and $\sigma_2$ on the second block.

> [!note]- Hint 3
> For (b), try the **Schur factorisation**: $\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} I & B D^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A - B D^{-1} C & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} I & 0 \\ D^{-1} C & I \end{pmatrix}$. The outer factors are block-triangular with $\det = 1$, so the determinant equals that of the middle (block-diagonal) factor.

---

# Solution

The plan is to first prove the block-triangular case (a) by analysing the Leibniz sum, then use a Schur factorisation to reduce (b) to the block-triangular case.

**Step 1: (Part a) Block-triangular determinant equals product of diagonal-block determinants.**

The Leibniz formula on $\begin{pmatrix} A & B \\ 0 & D \end{pmatrix}$ gives nonzero contributions only from permutations $\sigma$ that map $\{1, \dots, m\}$ to itself; these split as $\sigma = \sigma_1 \sqcup \sigma_2$ on the two blocks, and $\operatorname{sign}(\sigma) = \operatorname{sign}(\sigma_1) \operatorname{sign}(\sigma_2)$.

> [!note]- Derivation
> Let $M = \begin{pmatrix} A & B \\ 0 & D \end{pmatrix}$ with size $(m + k) \times (m + k)$. By Leibniz,
> $$\det M = \sum_\sigma \operatorname{sign}(\sigma) \prod_{j=1}^{m+k} M_{\sigma(j), j}.$$
> Consider a permutation $\sigma$. For $j \in \{1, \dots, m\}$, the $j$-th column of $M$ has nonzero entries only in rows $\{1, \dots, m\}$ (since $M_{ij} = 0$ for $i \in \{m+1, \dots, m+k\}$ and $j \leq m$). So a nonzero contribution requires $\sigma(j) \in \{1, \dots, m\}$ for every $j \in \{1, \dots, m\}$. Since $\sigma$ is a permutation, this forces $\sigma$ to also map $\{m+1, \dots, m+k\}$ to itself.
>
> Write $\sigma = (\sigma_1, \sigma_2)$, where $\sigma_1 \in \operatorname{perm}(m)$ acts on $\{1, \dots, m\}$ and $\sigma_2 \in \operatorname{perm}(k)$ acts on $\{m+1, \dots, m+k\}$ (relabelled to $\{1, \dots, k\}$). The sign factors:
> $$\operatorname{sign}(\sigma) = \operatorname{sign}(\sigma_1) \operatorname{sign}(\sigma_2)$$
> (the inversions in $\sigma$ count separately within the two blocks, since indices in the first block are all less than indices in the second).
>
> The product factors:
> $$\prod_{j=1}^{m+k} M_{\sigma(j), j} = \prod_{j=1}^{m} M_{\sigma_1(j), j} \cdot \prod_{j=1}^{k} M_{\sigma_2(j) + m, j + m} = \prod_{j=1}^{m} A_{\sigma_1(j), j} \cdot \prod_{j=1}^{k} D_{\sigma_2(j), j}.$$
>
> Summing over factorising permutations:
> $$\det M = \left(\sum_{\sigma_1} \operatorname{sign}(\sigma_1) \prod_j A_{\sigma_1(j), j}\right) \left(\sum_{\sigma_2} \operatorname{sign}(\sigma_2) \prod_j D_{\sigma_2(j), j}\right) = \det A \cdot \det D.$$

**Step 2: (Part b) Schur factorisation for the general case.**

Write $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$ as a product of three matrices and apply multiplicativity.

> [!note]- Derivation
> We claim the factorisation
> $$\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} I & B D^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A - B D^{-1} C & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} I & 0 \\ D^{-1} C & I \end{pmatrix}.$$
>
> Verify by direct multiplication. Compute the right-hand side step by step:
>
> First, $\begin{pmatrix} A - B D^{-1} C & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} I & 0 \\ D^{-1} C & I \end{pmatrix} = \begin{pmatrix} A - B D^{-1} C & 0 \\ D \cdot D^{-1} C & D \end{pmatrix} = \begin{pmatrix} A - B D^{-1} C & 0 \\ C & D \end{pmatrix}$.
>
> Then $\begin{pmatrix} I & B D^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A - B D^{-1} C & 0 \\ C & D \end{pmatrix} = \begin{pmatrix} A - B D^{-1} C + B D^{-1} C & B D^{-1} D \\ C & D \end{pmatrix} = \begin{pmatrix} A & B \\ C & D \end{pmatrix}.$
>
> Confirmed.
>
> Now apply [[Thm - Determinant is Multiplicative|multiplicativity]]:
> $$\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det \begin{pmatrix} I & B D^{-1} \\ 0 & I \end{pmatrix} \cdot \det \begin{pmatrix} A - B D^{-1} C & 0 \\ 0 & D \end{pmatrix} \cdot \det \begin{pmatrix} I & 0 \\ D^{-1} C & I \end{pmatrix}.$$
>
> Each of the outer factors is block-triangular with identity blocks on the diagonal, so by part (a), $\det = \det(I) \cdot \det(I) = 1$.
>
> The middle factor is block-diagonal: $\det \begin{pmatrix} A - B D^{-1} C & 0 \\ 0 & D \end{pmatrix} = \det(A - B D^{-1} C) \cdot \det(D)$ (by part (a) again, with $B = 0$).
>
> So $\det \begin{pmatrix} A & B \\ C & D \end{pmatrix} = 1 \cdot \det(A - B D^{-1} C) \cdot \det(D) \cdot 1 = \det(D) \cdot \det(A - B D^{-1} C)$.

**Step 3: (Part c) Symmetric case.**

For a symmetric block matrix $\begin{pmatrix} A & B \\ B^t & D \end{pmatrix}$ with $D$ invertible, the formula reads $\det = \det(D) \cdot \det(A - B D^{-1} B^t)$. The Schur complement $A - B D^{-1} B^t$ is also symmetric, and inherits structure: it is positive (semi-)definite iff certain matrix conditions hold.

> [!note]- Derivation
> Substituting $C = B^t$ into the formula from (b): $\det \begin{pmatrix} A & B \\ B^t & D \end{pmatrix} = \det(D) \cdot \det(A - B D^{-1} B^t)$.
>
> The Schur complement $S := A - B D^{-1} B^t$ is symmetric: $S^t = A^t - (B D^{-1} B^t)^t = A - B (D^{-1})^t B^t = A - B D^{-1} B^t = S$ (using $A^t = A$, $(B^t)^t = B$, and $(D^{-1})^t = (D^t)^{-1} = D^{-1}$ since $D = D^t$).
>
> Useful consequence: a symmetric block matrix is **positive definite** if and only if both $D$ is positive definite and the Schur complement $S = A - B D^{-1} B^t$ is positive definite. This factorises a positive-definiteness check into two smaller ones — a key algorithmic optimisation in numerical linear algebra (the Cholesky decomposition).

> [!note]- Complete formal solution
> **(a) Block-triangular determinant.** Let $M = \begin{pmatrix} A & B \\ 0 & D \end{pmatrix}$. By the Leibniz formula, $\det M = \sum_\sigma \operatorname{sign}(\sigma) \prod_j M_{\sigma(j), j}$. For $j \in \{1, \dots, m\}$, the $j$-th column has zeros below row $m$, so nonzero contributions require $\sigma(j) \leq m$. Hence $\sigma$ preserves the block structure: $\sigma = \sigma_1 \sqcup \sigma_2$ with $\sigma_1 \in \operatorname{perm}(m)$, $\sigma_2 \in \operatorname{perm}(k)$, and $\operatorname{sign}(\sigma) = \operatorname{sign}(\sigma_1) \operatorname{sign}(\sigma_2)$. The sum factors:
> $$\det M = \left(\sum_{\sigma_1} \operatorname{sign}(\sigma_1) \prod_{j=1}^m A_{\sigma_1(j), j}\right) \cdot \left(\sum_{\sigma_2} \operatorname{sign}(\sigma_2) \prod_{j=1}^k D_{\sigma_2(j), j}\right) = \det A \cdot \det D.$$
>
> **(b) Schur factorisation.** Verify by direct multiplication that
> $$\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} I & B D^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} A - B D^{-1} C & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} I & 0 \\ D^{-1} C & I \end{pmatrix}.$$
> By multiplicativity ([[Thm - Determinant is Multiplicative]]) and the fact that the outer block-triangular factors have $\det = 1$ (part (a) with $B = 0$ or $C = 0$ and diagonal identity), the determinant equals
> $$\det(A - B D^{-1} C) \cdot \det D.$$
>
> **(c) Symmetric case.** Substituting $C = B^t$ gives $\det \begin{pmatrix} A & B \\ B^t & D \end{pmatrix} = \det D \cdot \det(A - B D^{-1} B^t)$. The Schur complement $A - B D^{-1} B^t$ is symmetric (direct check), and this formula is the basis of the Cholesky decomposition. $\blacksquare$

---

# Key Takeaways

**The Schur factorisation is the linear-algebra version of Gaussian elimination of a block.** The identity $\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} I & B D^{-1} \\ 0 & I \end{pmatrix} \begin{pmatrix} S & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} I & 0 \\ D^{-1} C & I \end{pmatrix}$ (with $S = A - B D^{-1} C$) is what happens when you eliminate $C$ using row operations from $D$, and then eliminate $B$ using column operations. The middle block-diagonal matrix has the "after Gaussian elimination" structure, and the outer factors record the elimination steps. This pattern recurs throughout linear algebra and numerical analysis: the LU decomposition, the Cholesky decomposition, the QR decomposition all have block analogues with similar Schur-complement structure. The trigger to use this: you have a block matrix with one invertible diagonal block; you want to compute a determinant, an inverse, or a system solution; factor with the invertible block as "pivot".

**Block-triangular structure dramatically simplifies determinant calculation.** The result $\det \begin{pmatrix} A & B \\ 0 & D \end{pmatrix} = \det A \cdot \det D$ — and its generalisation to multiple blocks — is the key step in most determinant calculations involving block structures. The reason it works: the Leibniz sum has $n!$ terms over the full $n + k$ permutations, but the block-zero forces nonzero contributions to come from permutations that respect the blocks, factoring the sum. Block-triangular structures appear in: companion matrices of polynomials (a non-trivial top-left block plus a permutation-style bottom), Jordan blocks (each Jordan block is upper-triangular), and "lifting" arguments in algebra. The trigger to use this: any block matrix with at least one zero block in the off-diagonal position.

**The Schur complement gives a recursive formula for determinants.** Iterating part (b) reduces the determinant of an $n \times n$ matrix to a sequence of smaller determinants. This is the **Schur complement recursion**, equivalent to LU decomposition. It is the algorithmic foundation of fast determinant computation in $O(n^3)$ time, compared to Leibniz at $O(n!)$. Numerically, the Schur complement is *also* the right object for **block iterative methods** in solving linear systems: when solving $\begin{pmatrix} A & B \\ C & D \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} b_1 \\ b_2 \end{pmatrix}$, the variable $y$ can be eliminated and the remaining equation in $x$ involves the Schur complement. This is the fundamental algorithm of multigrid methods, domain decomposition, and saddle-point systems in PDE-constrained optimisation.
