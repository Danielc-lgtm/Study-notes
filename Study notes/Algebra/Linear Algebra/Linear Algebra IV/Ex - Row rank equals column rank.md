---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Linear Map"
  - "Def - Matrix of a Linear Map"
  - "Def - Rank of a Linear Map"
  - "Def - Dual Map"
  - "Thm - Matrix of Dual Map is Transpose"
  - "Thm - Null Space and Range of Dual Map"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $A \in \mathbb{F}^{m, n}$ be an $m \times n$ matrix with entries in $\mathbb{F}$.

The **column rank** of $A$ is the dimension of the span of its columns (a subspace of $\mathbb{F}^{m,1}$).

The **row rank** of $A$ is the dimension of the span of its rows (a subspace of $\mathbb{F}^{1,n}$).

Prove that
$$\text{column rank of } A = \text{row rank of } A.$$

Use the duality machinery of §3F: interpret $A$ as the matrix of a linear map $T : \mathbb{F}^{n,1} \to \mathbb{F}^{m,1}$, dualise to $T' : (\mathbb{F}^{m,1})' \to (\mathbb{F}^{n,1})'$, and apply [[Thm - Null Space and Range of Dual Map]] together with [[Thm - Matrix of Dual Map is Transpose]].

**Recall:**

The **rank** of a matrix $A$ is the dimension of the range of the linear map $A$ acts as. For a linear map $T \in \mathcal{L}(V, W)$, $\operatorname{rank} T = \dim \operatorname{range} T$.

The **column rank** of $A$ equals $\dim \operatorname{range} T$ when $T : \mathbb{F}^{n,1} \to \mathbb{F}^{m,1}$ is defined by $Tx = Ax$, because $\operatorname{range} T$ is spanned by the columns of $A$ (as $T e_k = $ the $k$-th column of $A$ for standard basis $e_k$).

![[Thm - Matrix of Dual Map is Transpose#Statement]]

![[Thm - Null Space and Range of Dual Map#Statement]]

The **transpose** $A^t$ of $A$ has entries $(A^t)_{j,k} = A_{k,j}$, so the columns of $A^t$ are the rows of $A$. Hence **column rank of $A^t$ = row rank of $A$**.

---

# Convergent Strategy

**Problem class.** This is *deriving a matrix identity from duality* (problem class 5 from the [[Linear Algebra IV — §3E–F Products, Quotients, Duality#Problem-Solving Strategy|topic page]]). The goal is to use the duality machinery to prove a classical identity that admits other (longer, more computational) proofs.

**Assumption pattern.** A matrix $A$ is given, with no further structure. The recognisable signal is *row vs column rank* — whenever this comparison appears, duality is the cleanest route.

**Theorem routing.** The route has four steps, each a one-line application of a theorem:
- Step 1: interpret $A$ as the matrix of $T : \mathbb{F}^{n,1} \to \mathbb{F}^{m,1}$.
- Step 2: column rank of $A$ equals $\dim \operatorname{range} T$.
- Step 3: by [[Thm - Null Space and Range of Dual Map]], $\dim \operatorname{range} T = \dim \operatorname{range} T'$.
- Step 4: by [[Thm - Matrix of Dual Map is Transpose]], $\mathcal{M}(T') = A^t$, so $\dim \operatorname{range} T'$ equals the column rank of $A^t$, which is the row rank of $A$.

Chaining: column rank of $A$ = $\dim \operatorname{range} T$ = $\dim \operatorname{range} T'$ = column rank of $A^t$ = row rank of $A$.

**Key decision point.** The non-obvious move is *recognising the row-vs-column distinction as a duality phenomenon*. Most students think of rows and columns as a symmetric pair and never quite understand why their dimensions should match. The duality view reveals that the equality is *not* a symmetry — it is *contravariance*: the rank of $T$ equals the rank of $T'$, and the dual map $T'$ has matrix $A^t$. The match of dimensions is a structural consequence of duality, not a coincidence of indices.

---

# Legal Operations Used

From [[Linear Algebra IV — §3E–F Products, Quotients, Duality#Legal Operations|the topic page]]:

1. **Dualize a map to reverse direction** (operation 6). The whole proof reduces row rank to column rank via dualisation.

2. **Translate between matrices and dual maps via transpose** (operation 9). The dual map of $T$ has the transpose matrix; this is the matrix-level shadow of duality.

3. **Use the fundamental theorem (rank-nullity) on the dual** (operation 2, extended). The rank equality $\dim \operatorname{range} T = \dim \operatorname{range} T'$ is the central fact derived from [[Thm - Null Space and Range of Dual Map]], which itself uses rank-nullity on both $T$ and $T'$.

---

# Hints

> [!note]- Hint 1
> Interpret $A \in \mathbb{F}^{m,n}$ as the matrix of a linear map $T : \mathbb{F}^{n,1} \to \mathbb{F}^{m,1}$ defined by $Tx = Ax$ for $x \in \mathbb{F}^{n,1}$ (column vector). Then the columns of $A$ are $T e_k$ for the standard basis $e_k$, and column rank of $A$ equals $\dim \operatorname{range} T$.

> [!note]- Hint 2
> By [[Thm - Null Space and Range of Dual Map]], $\dim \operatorname{range} T = \dim \operatorname{range} T'$. The dual map $T'$ goes from $(\mathbb{F}^{m,1})'$ to $(\mathbb{F}^{n,1})'$ in *reverse* direction.

> [!note]- Hint 3
> By [[Thm - Matrix of Dual Map is Transpose]], the matrix of $T'$ in dual bases is $A^t$. So $\dim \operatorname{range} T'$ equals the column rank of $A^t$.

> [!note]- Hint 4
> The columns of $A^t$ are the rows of $A$. So column rank of $A^t$ equals row rank of $A$. Chaining the four equalities gives the result.

---

# Solution

The proof is a chain of four equalities, each justified by one of the three duality theorems.

The plan: interpret $A$ as the matrix of $T$; use $\operatorname{rank} T = \operatorname{rank} T'$ from [[Thm - Null Space and Range of Dual Map]]; use $\mathcal{M}(T') = A^t$ from [[Thm - Matrix of Dual Map is Transpose]]; conclude by identifying column rank of $A^t$ with row rank of $A$.

**Step 1: Interpret $A$ as the matrix of a linear map.**

Define $T : \mathbb{F}^{n,1} \to \mathbb{F}^{m,1}$ by $Tx = Ax$. Then column rank of $A$ equals $\dim \operatorname{range} T$.

> [!note]- Derivation
> $T$ is a linear map by linearity of matrix-vector multiplication: $A(x + y) = Ax + Ay$ and $A(\lambda x) = \lambda (Ax)$.
>
> The matrix of $T$ in the standard bases of $\mathbb{F}^{n,1}$ and $\mathbb{F}^{m,1}$ is $A$ itself, because $Te_k = Ae_k$ equals the $k$-th column of $A$.
>
> The range of $T$ is $\{Ax : x \in \mathbb{F}^{n,1}\} = \operatorname{span}(\text{columns of } A)$, because every $Ax$ is a linear combination of the columns of $A$ (with coefficients the entries of $x$). So $\dim \operatorname{range} T = \dim \operatorname{span}(\text{columns of } A) = $ column rank of $A$.

**Step 2: $\dim \operatorname{range} T = \dim \operatorname{range} T'$.**

By [[Thm - Null Space and Range of Dual Map]], the rank of $T$ equals the rank of its dual.

> [!note]- Derivation
> [[Thm - Null Space and Range of Dual Map]] states $\dim \operatorname{range} T' = \dim \operatorname{range} T$ for any linear map between finite-dimensional spaces. So $\dim \operatorname{range} T' = $ column rank of $A$.

**Step 3: $\mathcal{M}(T') = A^t$.**

By [[Thm - Matrix of Dual Map is Transpose]], the matrix of the dual map in dual bases is the transpose.

> [!note]- Derivation
> Let $\varphi_1, \dots, \varphi_n$ be the dual basis of the standard basis of $\mathbb{F}^{n,1}$, and $\psi_1, \dots, \psi_m$ be the dual basis of the standard basis of $\mathbb{F}^{m,1}$. By [[Thm - Matrix of Dual Map is Transpose]], the matrix of $T' : (\mathbb{F}^{m,1})' \to (\mathbb{F}^{n,1})'$ in these dual bases is $\mathcal{M}(T') = (\mathcal{M}(T))^t = A^t$.

**Step 4: $\dim \operatorname{range} T' = $ column rank of $A^t = $ row rank of $A$.**

The dimension of the range of $T'$ is the column rank of its matrix $A^t$. The columns of $A^t$ are the rows of $A$, so this equals the row rank of $A$.

> [!note]- Derivation
> By the same reasoning as Step 1 applied to $T'$ and its matrix $A^t$: $\dim \operatorname{range} T' = \dim \operatorname{span}(\text{columns of } A^t) = $ column rank of $A^t$.
>
> The columns of $A^t$ are, by definition of the transpose, the rows of $A$: the $j$-th column of $A^t$ is the vector $((A^t)_{1,j}, (A^t)_{2,j}, \dots)^t = (A_{j,1}, A_{j,2}, \dots)^t$, which is the $j$-th row of $A$ written as a column. So $\operatorname{span}(\text{columns of } A^t) = \operatorname{span}(\text{rows of } A)$ (as subspaces of $\mathbb{F}^{n,1}$, identifying row vectors with column vectors via transpose).
>
> Hence column rank of $A^t$ = row rank of $A$.

**Conclusion.** Chaining the four equalities:
$$\text{column rank of } A \;\overset{\text{Step 1}}{=}\; \dim \operatorname{range} T \;\overset{\text{Step 2}}{=}\; \dim \operatorname{range} T' \;\overset{\text{Step 4}}{=}\; \text{column rank of } A^t \;\overset{\text{def}}{=}\; \text{row rank of } A. \qquad \blacksquare$$

> [!note]- Complete formal solution
> Let $A \in \mathbb{F}^{m,n}$ and define $T : \mathbb{F}^{n,1} \to \mathbb{F}^{m,1}$ by $Tx = Ax$. Then $\mathcal{M}(T) = A$ in standard bases.
>
> *Step 1.* Column rank of $A$ = $\dim \operatorname{span}(\text{columns of } A)$ = $\dim \operatorname{range} T$.
>
> *Step 2.* By [[Thm - Null Space and Range of Dual Map]], $\dim \operatorname{range} T' = \dim \operatorname{range} T$.
>
> *Step 3.* By [[Thm - Matrix of Dual Map is Transpose]], $\mathcal{M}(T') = A^t$ in dual bases.
>
> *Step 4.* By Step 1 applied to $T'$ and $A^t$, $\dim \operatorname{range} T'$ = column rank of $A^t$ = row rank of $A$ (since the columns of $A^t$ are the rows of $A$).
>
> Chaining: column rank of $A$ = $\dim \operatorname{range} T$ = $\dim \operatorname{range} T'$ = row rank of $A$. $\blacksquare$

> [!note]- Sanity check on a specific matrix
> Take $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}$. The columns are $(1, 2)^t$, $(2, 4)^t$, $(3, 6)^t$; the second and third are scalar multiples of the first, so column rank = 1. The rows are $(1, 2, 3)$ and $(2, 4, 6)$; the second is twice the first, so row rank = 1. Match.

> [!warning] Illegal but tempting: the symmetric proof
> A tempting "symmetric" proof is to argue "rows and columns are dual to each other, so their ranks must be the same". This intuition is correct but the proof in this form does not give a rigorous statement — it does not say *what* duality is or *why* it preserves dimension. The exercise's proof gives the precise mechanism: duality is encoded by the dual map, and the rank equality is [[Thm - Null Space and Range of Dual Map]] (proved by rank-nullity on both $T$ and $T'$). The vague symmetry argument *suggests* the result but does not establish it.

---

# Key Takeaways

**Row rank equals column rank because the dual map has the transpose matrix and the same rank.** This is the cleanest conceptual proof of the foundational identity. The classical proof of row rank = column rank uses row reduction or matrix manipulation; both work but offer no insight into *why* the identity should hold. The duality proof reveals the structural reason: row rank of $A$ is the column rank of $A^t$, and $A^t$ is the matrix of the *dual map* $T'$, which has the same rank as $T$ by [[Thm - Null Space and Range of Dual Map]]. Three structural facts in sequence give the identity for free, with no row reduction. Once you internalise this proof, "row rank = column rank" is no longer a coincidence — it is a direct expression of duality.

**Matrix manipulation often hides linear-algebraic structure that becomes clear under interpretation as linear maps.** The transpose, the determinant, multiplication of matrices — each of these has a structural interpretation as a linear-map operation. The transpose is the dual map ([[Thm - Matrix of Dual Map is Transpose]]); the determinant is the unique alternating multilinear form normalised at the identity ([[Linear Algebra IX — §9 Multilinear Algebra and Determinants|Chapter 9]]); matrix multiplication is composition. The lesson: *whenever you have a matrix identity, ask what the corresponding linear-map statement is*. The matrix identity often has an obscure indexical proof; the linear-map statement often has a clean structural proof.

**The duality argument generalises far beyond matrices.** The structural identity is "rank of $T$ equals rank of $T'$", and it holds in any finite-dimensional setting (vector spaces, modules over a field), not just for finite matrices. In infinite dimensions it becomes more subtle (the dual of a Banach space is its continuous dual, and rank means dimension of the range), but the structural identity persists in the form of the **Fredholm alternative**. So learning the duality proof here teaches you a pattern that recurs in functional analysis: "transpose-rank arguments" via duality of operators.

**Recognition trigger: any problem mentioning rows-vs-columns or transpose-rank is a duality problem.** Beyond the present exercise, the same template solves:
- "$AB$ and $BA$ have the same nonzero eigenvalues" (use traces and duality).
- "Rank of $A$ equals rank of $A^t A$" (dualise and use trace identity).
- "Symmetric matrices have orthogonal eigenvectors" (use $T = T'$ and apply spectral theorem from [[Linear Algebra VII — §7 Operators on Inner Product Spaces|Chapter 7]]).
- "The system $Ax = b$ is solvable iff $b$ is orthogonal to every $y$ with $A^t y = 0$" (annihilator of range = null space of dual).
Whenever you see one of these patterns, reach for duality.

**Cross-link to companion exercises.** This exercise is the matrix-level companion of [[Ex - Annihilator of a subspace has complementary dimension]] and [[Thm - Null Space and Range of Dual Map]]. The rank equality used here ($\dim \operatorname{range} T' = \dim \operatorname{range} T$) is proved in that theorem; the present exercise just applies it together with the transpose-as-dual-matrix identification.
