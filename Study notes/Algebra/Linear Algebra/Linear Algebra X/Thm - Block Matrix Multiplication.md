---
type: theorem
subject: linear-algebra
prereqs:
tags: [algebra, linear-algebra, applied]
---

# Notation

A **block matrix** is a matrix partitioned into rectangular sub-matrices (**blocks**), arranged in a grid. We write block matrices using square brackets or aligned notation:
$$M = \begin{pmatrix} A & B \\ C & D \end{pmatrix}.$$
The blocks $A, B, C, D$ are themselves matrices whose dimensions must fit together: in the same block-row they have the same number of rows; in the same block-column they have the same number of columns. The blocks need not be square individually, but their dimensions must conform.

---

# Statement

> **Theorem (Block [[Def - Matrix Multiplication|Matrix Multiplication]]).** Let
> $$M_1 = \begin{pmatrix} A & B \\ C & D \end{pmatrix}, \quad M_2 = \begin{pmatrix} E & F \\ G & H \end{pmatrix}$$
> be block matrices such that the inner block [[Def - Dimension|dimensions]] are compatible — that is, $A E$, $A F$, $B G$, $B H$, $C E$, $C F$, $D G$, $D H$ all make sense as matrix products. Then the product $M_1 M_2$ is the block matrix
> $$M_1 M_2 = \begin{pmatrix} A E + B G & A F + B H \\ C E + D G & C F + D H \end{pmatrix},$$
> computed by the usual matrix-multiplication formula treating each block as if it were a single entry.

> **Generalisation.** For block matrices with an arbitrary number of block rows and columns, the analogous formula holds: $(M_1 M_2)_{ij} = \sum_k (M_1)_{ik} (M_2)_{kj}$, where the indices $i, j, k$ range over block indices and each "entry" is itself a matrix-product.

This is sometimes also called the **Cayley block-matrix rule** or the **Schur block formula**. The crucial caveat is that the inner block [[Def - Dimension|dimensions]] must match — multiplication of *blocks* must be defined.

---

# Motivation

Block matrix multiplication is more than a notational convenience. It is the algebraic engine behind a wide variety of computational and structural results:

- **Recursive and parallel algorithms.** Block-multiplying a matrix means each block can be computed independently, exposing parallelism. Strassen's algorithm achieves sub-cubic matrix multiplication ($O(n^{2.81})$ flops) by recursively splitting matrices into $2 \times 2$ block structures and reducing the number of block multiplications from $8$ to $7$.

- **Schur complement and block inversion.** Inverting a $2 \times 2$ block matrix uses the **Schur complement** formula: if $D$ is invertible, the Schur complement is $S = A - B D^{-1} C$, and
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix}^{-1} = \begin{pmatrix} S^{-1} & -S^{-1} B D^{-1} \\ -D^{-1} C S^{-1} & D^{-1} + D^{-1} C S^{-1} B D^{-1}\end{pmatrix}.$$
This is the algebraic foundation of LU factorization, partial inversion in optimization, and conditional-distribution formulas in statistics.

- **Composite linear systems.** Block matrices naturally arise when describing systems that have multiple sub-systems (e.g., a control system with state and input dynamics), and block multiplication lets one compose the sub-systems algebraically. The composition of two linear dynamical systems with state-input matrices $(A_1, B_1)$ and $(A_2, B_2)$ produces a system whose dynamics matrix has a block-triangular structure, which block multiplication makes manifest.

- **Tensor products and Kronecker products.** The Kronecker product $A \otimes B$ is a block matrix where each entry of $A$ is replaced by $A_{ij} B$. Block multiplication is exactly what makes the formula $(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$ work; this identity is the workhorse of Kronecker algebra.

The theorem itself is *easy*: it just says block matrices multiply like matrices of matrices. But the implications are profound — it converts large-matrix computations into structured sequences of smaller-matrix computations, exposing parallelism, recursion, and algebraic identities.

---

# Sources and Targets

**Sources (Input Broadening)**

**Source 1 — large matrix split for parallel computation.** A massive matrix $M$ is split into $4 \times 4$ blocks for distributed computation across $16$ processors. Each processor receives one block. Block multiplication tells each processor which blocks of $M_1$ and $M_2$ to multiply and sum to produce its assigned output block. The bridge: parallel computation is enabled by the structural recipe of block multiplication.

**Source 2 — composite linear system.** Two dynamical systems $x_{t+1} = A_1 x_t + B_1 u_t$ and $y_{t+1} = A_2 y_t + B_2 v_t$ are composed into a single system on $(x, y)$ with cross-coupling $C_{12}, C_{21}$. The combined dynamics matrix is the block matrix $\begin{pmatrix} A_1 & C_{12} \\ C_{21} & A_2 \end{pmatrix}$, and block multiplication describes how iterating this combined matrix advances the joint state. The bridge: structured systems decompose naturally as block matrices, and composition is block multiplication.

**Source 3 — Kronecker structure.** When matrices have Kronecker-product structure $M = A \otimes B$, products $M_1 M_2 = (A_1 \otimes B_1)(A_2 \otimes B_2) = (A_1 A_2) \otimes (B_1 B_2)$ are computed via block multiplication. This is the algebraic basis of efficient algorithms for problems with tensor structure, like discrete Fourier transforms in multiple dimensions and the multi-dimensional finite element method.

**Targets (Output Amplification)**

**Target 1 — Schur complement and block inversion.** Inverting a block matrix via the Schur complement gives, in addition to the inverse itself, a wealth of derived results: the partial determinant formula $\det\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det(D) \det(A - B D^{-1} C)$, the conditional-distribution formula for jointly Gaussian random variables, the eliminant of a system of equations. The Schur complement is, structurally, the result of partial Gaussian elimination viewed via block multiplication.

**Target 2 — Strassen's sub-cubic matrix multiplication.** For two $n \times n$ matrices split as $2 \times 2$ block matrices with $n/2 \times n/2$ blocks, the standard formula requires $8$ block multiplications. Strassen showed that $7$ specially-chosen combinations suffice, yielding an algorithm with complexity $O(n^{\log_2 7}) = O(n^{2.807})$. Block multiplication is the structural framework that makes Strassen's algebraic identity meaningful.

**Target 3 — block-LU and block-Cholesky factorizations.** Standard LU and Cholesky factorizations can be performed block-wise, yielding factorizations that respect the block structure. This is what makes sparse-direct solvers (like those in scientific computing libraries) tractable: by exploiting the block-sparsity structure of the matrix (e.g., a banded matrix or a hierarchical block structure), the factorization can be computed in $O(\text{nonzeros})$ time rather than $O(n^3)$.

---

# Why Is It True

**The mechanism in one bolded line: the entry $(M_1 M_2)_{ij}$ in the standard matrix-multiplication formula is the sum over an index $k$ of products $(M_1)_{ik} (M_2)_{kj}$; partitioning $k$ into blocks reorganises this sum into a sum of inner products of *block-row*$ \cdot$ *block-column* products, which is exactly the block-multiplication formula.**

Concretely: if $M_1$ is $m \times p$ and $M_2$ is $p \times n$, then $(M_1 M_2)_{ij} = \sum_{k=1}^p (M_1)_{ik}(M_2)_{kj}$ is a sum over $p$ inner terms. Partition the inner index $k$ into blocks $K_1 = \{1, \dots, p_1\}$, $K_2 = \{p_1 + 1, \dots, p_1 + p_2\}$, etc., with $p = p_1 + p_2 + \cdots$. Then
$$\sum_{k=1}^p (M_1)_{ik}(M_2)_{kj} = \sum_{l} \sum_{k \in K_l}(M_1)_{ik}(M_2)_{kj}.$$
If we further partition the row indices into blocks $I_1, I_2, \dots$ and the column indices into $J_1, J_2, \dots$, the inner sum over $k \in K_l$ for fixed block-positions $(I_r, J_s)$ is exactly the block-product of the $(r, l)$ block of $M_1$ with the $(l, s)$ block of $M_2$. Summing over $l$ gives the $(r, s)$ block of the product.

So block multiplication is *just matrix multiplication with the inner sum reorganised by block-partitioning the indices*. The dimensions of the blocks must be such that the inner products make sense — this is the compatibility requirement.

The non-obvious depth is that **the formula looks the same whether the entries are numbers or matrices**, as long as the block dimensions are compatible. This is the universal phenomenon of multiplication being associative: matrix multiplication is itself a "multiplication in a non-commutative [[Def - Ring|ring]]", and matrix multiplication of block matrices is multiplication in that same [[Def - Ring|ring]], just viewed at a coarser granularity.

---

# What Makes This Hard

The theorem itself is not deep — it follows directly from rearranging summation indices. But two subtle points often trip up readers.

First, **the block dimensions must match for *every* block product in the formula**. It is not enough that the outer dimensions of $M_1$ and $M_2$ match (giving a valid matrix product); each of the inner block products $A_{ij} B_{jk}$ must be valid. If the block structure of $M_1$ and $M_2$ are incompatible (e.g., row partitioning of $M_2$ does not match column partitioning of $M_1$), the block product cannot be computed even though the matrix product can.

Second, **block matrix arithmetic preserves the non-commutativity of matrix multiplication**. In the formula $A E + B G$ for the top-left block of the product, the order $A E$ matters (since matrix multiplication is non-commutative in general). One cannot rearrange to $E A + G B$ as one might with scalars. Forgetting this is a common bug in derivations involving block matrices.

A third subtlety is **block-triangular structure**. If $M_1$ is block upper-triangular (so $C = 0$ in the $2 \times 2$ case), the product $M_1 M_2$ is *not* in general block upper-triangular unless $M_2$ is also. But the product of two block-upper-triangular matrices is block-upper-triangular, and the diagonal blocks of the product are products of the diagonal blocks. This is the basis of block-LU factorization.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Compute the $(I, J)$ block of $M_1 M_2$ directly from the matrix-multiplication formula, partitioning the inner index $k$ into the blocks of the column partition of $M_1$ (equivalently, the row partition of $M_2$). The resulting sum is exactly $\sum_l (M_1)_{IL}(M_2)_{LJ}$.

**Subgoal decomposition:**

1. **Recall scalar matrix multiplication.** For matrices $X$ of size $m \times p$ and $Y$ of size $p \times n$, $(XY)_{ij} = \sum_{k=1}^p X_{ik} Y_{kj}$.
   - *Hint:* Definition of matrix multiplication.
   - *Why needed:* Starting point for the block version.

2. **Partition the indices.** Let $I_1, \dots, I_r$ be a partition of row indices, $K_1, \dots, K_s$ a partition of column indices of $X$ (which is also the row partition of $Y$), and $J_1, \dots, J_t$ the column partition of $Y$. The $(I, J)$ block of $XY$ consists of entries $(XY)_{ij}$ with $i \in I, j \in J$.
   - *Hint:* Index partitioning aligns with the block partitioning.
   - *Why needed:* Sets up the block-by-block computation.

3. **Reorganise the inner sum.** For fixed $i \in I$ and $j \in J$, $(XY)_{ij} = \sum_{k=1}^p X_{ik} Y_{kj} = \sum_{l=1}^s \sum_{k \in K_l} X_{ik} Y_{kj}$. The inner sum $\sum_{k \in K_l} X_{ik} Y_{kj}$ is the $(i, j)$ entry of the matrix product $X_{IL} Y_{LJ}$, where the subscripts denote sub-matrices.
   - *Hint:* Splitting the sum over $k$ by the block it lies in.
   - *Why needed:* Identifies the inner sum as a block-product entry.

4. **Read off the block formula.** Summing over the partition, $(XY)_{IJ} = \sum_l X_{IL} Y_{LJ}$. This is the entry of the block matrix product at position $(I, J)$, computed by the standard matrix-multiplication formula with matrix-valued entries.
   - *Hint:* Matching the formula to the statement.
   - *Why needed:* Concludes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: Inner sum equals block product
> **Statement:** Let $X$ be $m \times p$ and $Y$ be $p \times n$. For any subsets $I \subseteq \{1, \dots, m\}$, $L \subseteq \{1, \dots, p\}$, $J \subseteq \{1, \dots, n\}$, with $L$ contiguous, the partial sum $\sum_{k \in L} X_{ik} Y_{kj}$ for $i \in I, j \in J$ equals the $(i, j)$ entry of the matrix product $X_{I, L} Y_{L, J}$, where $X_{I, L}$ and $Y_{L, J}$ are the sub-matrices with the indicated rows and columns.
>
> **Hint:** Direct verification by the matrix-multiplication formula applied to the sub-matrices.
>
> **Why needed:** This identifies each "inner" sum in the block formula with a matrix-product of blocks.
>
> > [!note]- Full proof
> > By definition, the matrix product $X_{I, L} Y_{L, J}$ has $(i, j)$ entry (for $i \in I$, $j \in J$) equal to $\sum_{k \in L} (X_{I, L})_{i, k} (Y_{L, J})_{k, j} = \sum_{k \in L} X_{ik} Y_{kj}$, since the sub-matrix entries are inherited from the original matrices.

> [!note]- Lemma 2: Total sum decomposes over a partition
> **Statement:** For any partition $K_1, \dots, K_s$ of $\{1, \dots, p\}$ and any function $f : \{1, \dots, p\} \to \mathbb R$, $\sum_{k=1}^p f(k) = \sum_{l=1}^s \sum_{k \in K_l} f(k)$.
>
> **Hint:** Direct: each $k \in \{1, \dots, p\}$ belongs to exactly one block $K_l$.
>
> **Why needed:** This is the algebraic identity that lets us rewrite the inner sum in the matrix product as a sum over blocks.
>
> > [!note]- Full proof
> > Every $k \in \{1, \dots, p\}$ lies in exactly one $K_l$, so the right-hand sum visits each $f(k)$ exactly once. Hence both sides equal $\sum_k f(k)$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $M_1$ and $M_2$ be block matrices with compatible inner block dimensions. Then $(M_1 M_2)_{IJ} = \sum_L (M_1)_{IL} (M_2)_{LJ}$, where the sum is over the columns of $M_1$ (equivalently the rows of $M_2$) block-by-block.
>
> *Proof.* Let $M_1$ be $m \times p$ partitioned by row blocks $I_1, \dots, I_r$ and column blocks $K_1, \dots, K_s$. Let $M_2$ be $p \times n$ partitioned by row blocks $K_1, \dots, K_s$ (same as $M_1$'s column partition, by compatibility) and column blocks $J_1, \dots, J_t$.
>
> Pick any block row index $u \in \{1, \dots, r\}$ and block column index $v \in \{1, \dots, t\}$. The $(I_u, J_v)$ block of $M_1 M_2$ consists of entries $(M_1 M_2)_{ij}$ for $i \in I_u$, $j \in J_v$.
>
> By the scalar matrix-multiplication formula,
> $$(M_1 M_2)_{ij} = \sum_{k=1}^p (M_1)_{ik}(M_2)_{kj}.$$
>
> By Lemma 2, $\sum_{k=1}^p = \sum_{l=1}^s \sum_{k \in K_l}$. So
> $$(M_1 M_2)_{ij} = \sum_{l=1}^s \sum_{k \in K_l} (M_1)_{ik}(M_2)_{kj}.$$
>
> By Lemma 1, the inner sum $\sum_{k \in K_l} (M_1)_{ik}(M_2)_{kj}$ is the $(i, j)$ entry of the matrix product $(M_1)_{I_u, K_l}(M_2)_{K_l, J_v}$, which is the product of the $(u, l)$ block of $M_1$ and the $(l, v)$ block of $M_2$.
>
> So
> $$(M_1 M_2)_{ij} = \sum_{l=1}^s \big((M_1)_{u, l}(M_2)_{l, v}\big)_{ij}$$
> (where the inner subscripts now refer to block-indices). Equivalently, the $(u, v)$ block of $M_1 M_2$ is
> $$(M_1 M_2)_{uv} = \sum_{l=1}^s (M_1)_{ul} (M_2)_{lv},$$
> which is the matrix product of block-row $u$ of $M_1$ with block-column $v$ of $M_2$, computed by ordinary matrix-multiplication formula with matrix-valued entries. $\quad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Numerical analysis — block LU factorization.** A block LU factorization writes $M = LU$ where $L$ is block lower-triangular with identity diagonal blocks and $U$ is block upper-triangular. Computing this factorization uses the Schur complement at each step: factor the top-left block, then use the Schur complement of the remaining sub-matrix. This is the standard algorithm for solving large sparse linear systems with block structure, and is implemented in libraries like SuperLU and MUMPS.

**Statistics — multivariate Gaussian conditional distribution.** For jointly Gaussian $(X, Y)$ with mean $(\mu_X, \mu_Y)$ and covariance $\begin{pmatrix} \Sigma_{XX} & \Sigma_{XY} \\ \Sigma_{YX} & \Sigma_{YY} \end{pmatrix}$, the conditional distribution of $X$ given $Y = y$ is Gaussian with mean $\mu_X + \Sigma_{XY}\Sigma_{YY}^{-1}(y - \mu_Y)$ and covariance $\Sigma_{XX} - \Sigma_{XY}\Sigma_{YY}^{-1}\Sigma_{YX}$ (the Schur complement). Block matrix manipulation is the entire derivation.

**Control theory — closed-loop dynamics.** A linear dynamical system $x_{t+1} = A x_t + B u_t$ with state feedback $u_t = K x_t$ has closed-loop dynamics $x_{t+1} = (A + BK) x_t$. Combining state and input in a block matrix and using block multiplication gives the standard formula. For more elaborate systems with multiple feedback paths, the block-matrix view exposes the structure clearly.

**Quantum mechanics — tensor product of states.** The state space of a composite quantum system is the tensor product of the components' state spaces. Operators on the composite system act via Kronecker products of operators on the components. The block-multiplication identity $(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$ describes how composite operators compose, and is the basis of quantum circuit design.

---

# Bridges

- **The Schur complement formula** — given a block matrix with invertible bottom-right block $D$, the Schur complement is $S = A - BD^{-1}C$. The matrix is invertible iff $S$ is invertible, and the inverse has a block-form involving $S^{-1}$ and partial products. The Schur complement appears in: conditional distributions of Gaussians, partial Gaussian elimination, the Karush-Kuhn-Tucker conditions in optimization, and Schur complement-based bound improvements in semidefinite programming. The derivation is direct block multiplication.

- **Block LU factorization and structured-direct solvers** — for matrices with block-structure (e.g., sparse block matrices from finite-element methods, block-tridiagonal matrices from PDE discretisations), block LU factorization preserves the block structure and is the foundation of efficient direct solvers. The factorization $M = LU$ with $L$ block-unit-lower-triangular and $U$ block-upper-triangular uses block multiplication at every step.

- **Kronecker products and tensor algebras** — the Kronecker product $A \otimes B$ has the multiplicative identity $(A_1 \otimes B_1)(A_2 \otimes B_2) = (A_1 A_2) \otimes (B_1 B_2)$, derivable from block multiplication. The Kronecker product is the matrix realisation of tensor products of linear maps in finite-dimensional spaces, and the identity is what makes Kronecker algebra a powerful tool for computations involving tensor structure.

- **Strassen's algorithm and fast matrix multiplication** — block matrix multiplication is the framework for sub-cubic matrix multiplication algorithms. Strassen's identity reduces $2 \times 2$ block matrix multiplication from $8$ to $7$ block products, giving $O(n^{\log_2 7}) \approx O(n^{2.807})$ complexity. More sophisticated algorithms (Coppersmith-Winograd and successors) reduce the exponent further, with the current best being around $O(n^{2.37})$.

- **Block-diagonal forms and direct-sum decompositions** — for an operator $T$ on $V = V_1 \oplus V_2$, the matrix in a basis adapted to the decomposition is block-diagonal: $\operatorname{diag}(A, D)$ where $A$ acts on $V_1$ and $D$ on $V_2$. Block multiplication shows that products and powers of block-diagonal matrices are block-diagonal: $\operatorname{diag}(A, D)^k = \operatorname{diag}(A^k, D^k)$. This is the algebraic basis of the spectral theorem and of generalised eigenspace decompositions in [[Linear Algebra V — §4–5 Polynomials and Eigenvalues|Linear Algebra V]].

---

# Unlocked by This

> [!tip] Schur Complement and Block Inversion *(from Linear Algebra IX and Statistics)*
> The Schur complement formula gives the inverse of a block matrix in terms of inverses of smaller blocks. It is the algebraic basis of conditional distributions of multivariate Gaussians, Karush-Kuhn-Tucker conditions in convex optimization, semidefinite-programming-based bounds, and block-LU factorization in numerical linear algebra.

> [!tip] Strassen and Sub-Cubic Matrix Multiplication *(from Theoretical Computer Science)*
> The discovery that $2 \times 2$ block matrix multiplication can be done with $7$ block-product operations (Strassen 1969) opened the field of fast matrix multiplication, leading to a long line of improvements down to the current best of $O(n^{2.37})$ flops. The block-multiplication formula is the structural template; the speedup comes from algebraic identities that exploit specific symmetries.

> [!tip] Kronecker Products and Multilinear Algebra *(from Linear Algebra IX)*
> The Kronecker product $A \otimes B$ of two matrices is a block matrix where each entry of $A$ is replaced by $A_{ij} B$. The compatibility of Kronecker products with matrix multiplication, $(A_1 \otimes B_1)(A_2 \otimes B_2) = (A_1 A_2) \otimes (B_1 B_2)$, follows directly from block multiplication and is the foundation of efficient algorithms for multi-dimensional Fourier transforms, finite-element methods, and quantum circuits.
