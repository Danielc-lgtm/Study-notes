---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Determinant"
  - "Def - Alternating Multilinear Form"
  - "Thm - Determinant is Multiplicative"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $A$ is an $n \times n$ matrix over a field $\mathbb{F}$. The $(i, j)$-**minor** $M_{ij}$ is the determinant of the $(n-1) \times (n-1)$ submatrix of $A$ obtained by deleting row $i$ and column $j$. The $(i, j)$-**cofactor** is $C_{ij} = (-1)^{i+j} M_{ij}$. The **adjugate** (or **classical adjoint**) of $A$ is the matrix $\operatorname{adj}(A)$ with entries $(\operatorname{adj} A)_{ij} = C_{ji} = (-1)^{i+j} M_{ji}$ — the *transpose* of the cofactor matrix. Recall the Leibniz formula for $\det$: $\det A = \sum_{\sigma \in \operatorname{perm}(n)} \operatorname{sign}(\sigma) A_{\sigma(1), 1} \cdots A_{\sigma(n), n}$.

---

# Statement

> **Theorem (Cofactor Expansion).** Let $A$ be an $n \times n$ matrix. For any fixed row index $i \in \{1, \dots, n\}$,
>
> $$\det A \;=\; \sum_{j=1}^n (-1)^{i+j} A_{ij} M_{ij} \;=\; \sum_{j=1}^n A_{ij} C_{ij}$$
>
> (expansion along row $i$). Similarly, for any fixed column index $j$,
>
> $$\det A \;=\; \sum_{i=1}^n (-1)^{i+j} A_{ij} M_{ij} \;=\; \sum_{i=1}^n A_{ij} C_{ij}$$
>
> (expansion along column $j$).

> **Theorem (Adjugate Formula).** For any $n \times n$ matrix $A$,
>
> $$A \cdot \operatorname{adj}(A) \;=\; \operatorname{adj}(A) \cdot A \;=\; (\det A) \cdot I.$$
>
> In particular, if $\det A \neq 0$, then $A^{-1} = \operatorname{adj}(A) / \det A$.

> **Theorem (Cramer's Rule).** If $A$ is invertible and $b \in \mathbb{F}^n$, the unique solution $x$ of $A x = b$ has $j$-th component
>
> $$x_j \;=\; \frac{\det A_j}{\det A},$$
>
> where $A_j$ is the matrix obtained from $A$ by replacing its $j$-th column with $b$.

---

# Motivation

Cofactor expansion is the **recursive computational formula** for [[Def - Determinant|determinants]]: it reduces the $n \times n$ determinant to a sum of $n$ many $(n-1) \times (n-1)$ [[Def - Determinant|determinants]], each with a sign. The recursion bottoms out at $n = 1$, where $\det A = A_{11}$. Combined with the choice of expanding along a row or column with many zeros, this gives the most useful hand-computation algorithm for determinants of small matrices with structure.

The adjugate formula and Cramer's rule are theoretical companions: they express the inverse and the solution of a linear system *explicitly* in terms of determinants. They are **computationally useless** for $n \geq 4$ or so (the cost is dominated by the cost of computing $n^2$ many $(n-1) \times (n-1)$ determinants, each itself $\geq n!$ via Leibniz), but they are **conceptually invaluable**: they show that the inverse matrix and the solution of a linear system are *polynomials in the entries of $A$*, of degree at most $n$. This polynomiality is what underlies:

- **Smoothness of $A^{-1}$ as a function of $A$.** Since $A^{-1} = \operatorname{adj}(A) / \det A$ is a ratio of polynomials, with $\det A \neq 0$ at invertible $A$, the map $A \mapsto A^{-1}$ is smooth on $\mathrm{GL}(V)$.

- **[[Thm - Cayley-Hamilton (Minimal-Polynomial Form)|Cayley-Hamilton]].** The proof via the adjugate uses $(zI - A) \operatorname{adj}(zI - A) = \det(zI - A) \cdot I = p_A(z) I$, and substituting $z = A$ (with care) gives $p_A(A) = 0$.

- **Implicit function theorem applications.** When you need to invert a derivative matrix as part of an implicit-function argument, Cramer's rule gives the explicit dependence of the inverse on the original entries — useful for tracking how perturbations propagate.

- **Algebraic-geometric proofs.** The polynomiality of $\det A^{-1} \cdot A^{-1}_{ij}$ in $A$ means: the inverse extends as an algebraic function across the singular locus, with $\det A$ as the discriminant. This is the foundation of birational geometry and the study of $\mathrm{GL}_n$ as an algebraic variety.

So while you should *never* use Cramer's rule to numerically solve a system (Gaussian elimination is $O(n^3)$, Cramer is $O(n!)$), you should *always* reach for cofactor expansion when proving theoretical results about determinants and inverses.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem requires only an $n \times n$ matrix. Disguised sources:

**A matrix with zeros in some row or column.** If row $i$ has many zeros, expand along it: only the nonzero entries contribute to the cofactor sum. Bridge: a sparse row reduces the $n$-term cofactor sum to a much shorter sum. Example: $3 \times 3$ matrix with a zero in position $(1, 1)$ expands cleanly along row 1.

**A block-triangular matrix.** Expand along the row (or column) containing all of one block, and the cofactors give the product of the blocks. See [[Ex - Determinant of a block matrix]] for the full computation.

**A polynomial identity needed.** If you need to express the inverse $A^{-1}$ as a polynomial in $A$ (e.g., for Cayley-Hamilton), the adjugate formula $A^{-1} = \operatorname{adj}(A) / \det A$ gives the explicit polynomial expression. Bridge: from "need polynomial expression" to "use adjugate".

**A linear system $Ax = b$ to solve symbolically.** Cramer's rule expresses each $x_j$ explicitly as a ratio of determinants. Bridge: from "symbolic solution needed" to "use Cramer". Useful in computer algebra for small systems and in proofs requiring an explicit formula.

**Targets (Output Amplification)**

Combine with continuity: the cofactor expansion shows $A^{-1}$ is a *continuous* (in fact smooth) function of $A$ on the open set $\{A : \det A \neq 0\}$.

Combine with Cayley-Hamilton: $(zI - A) \operatorname{adj}(zI - A) = \det(zI - A) I$ gives a key step in proving Cayley-Hamilton, by viewing both sides as polynomials in $z$ with matrix coefficients and substituting $z = A$.

Combine with the implicit function theorem: when solving $F(x, y) = 0$ implicitly, the inverse Jacobian is needed, and Cramer's rule gives explicit dependence of $\partial y/\partial x$ on partial derivatives of $F$.

Combine with elimination theory: Cramer's rule and the resultant theory together give explicit formulas for eliminating variables in polynomial systems.

---

# Why Is It True

**For cofactor expansion.** Recall that the determinant is the unique alternating multilinear function of the columns (or rows) of the matrix, normalised to 1 on the identity. Expand along column $j$:

$$\det(A) = \det(a_1, a_2, \dots, a_n) \quad \text{where } a_k \text{ is the } k\text{-th column}.$$

The column $a_j$ can be written as $a_j = \sum_i A_{ij} e_i$. By multilinearity of $\det$ in column $j$:

$$\det A = \sum_i A_{ij} \det(a_1, \dots, e_i, \dots, a_n),$$

where $e_i$ is in slot $j$. Now $\det(a_1, \dots, e_i, \dots, a_n)$ is the determinant of a matrix with $e_i$ in position $(i, j)$ — that is, the column with a 1 in row $i$ and zeros elsewhere. By the alternating property, this determinant equals $(-1)^{i + j}$ times the determinant of the $(n-1) \times (n-1)$ submatrix $M_{ij}$ (obtained by deleting row $i$ and column $j$). The sign $(-1)^{i + j}$ comes from the permutation needed to move $e_i$ to the "natural" position and the deleted row to the bottom.

So $\det A = \sum_i A_{ij} (-1)^{i + j} M_{ij}$ — cofactor expansion along column $j$.

**For the adjugate formula.** Compute $(A \cdot \operatorname{adj}(A))_{ij} = \sum_k A_{ik} (\operatorname{adj} A)_{kj} = \sum_k A_{ik} C_{jk}$, where $C_{jk}$ is the $(j, k)$-cofactor. For $i = j$, this is exactly cofactor expansion along row $i$, giving $\det A$. For $i \neq j$, this is cofactor expansion of a *different* matrix: take $A$ and replace row $j$ by row $i$ (so the row $i$ appears twice). The result has two equal rows, hence determinant zero. So $(A \cdot \operatorname{adj}(A))_{ij} = (\det A) \delta_{ij}$, i.e., $A \cdot \operatorname{adj}(A) = (\det A) I$.

**For Cramer's rule.** Multiply both sides of $A x = b$ on the left by $\operatorname{adj}(A)$: $(\operatorname{adj} A)(Ax) = (\operatorname{adj} A) b$. By the adjugate formula, $(\operatorname{adj} A) A = (\det A) I$, so $(\det A) x = (\operatorname{adj} A) b$. The $j$-th component of $(\operatorname{adj} A) b$ is $\sum_i (\operatorname{adj} A)_{ji} b_i = \sum_i C_{ij} b_i$, which is the cofactor expansion of the matrix $A_j$ (with column $j$ replaced by $b$) along column $j$. So $(\det A) x_j = \det A_j$, hence $x_j = \det A_j / \det A$.

**The mechanism summary:**

> **Cofactor expansion is multilinearity-in-one-column applied to the identity decomposition of a column. The adjugate formula is two cofactor expansions combined (one giving $\det A$, the other giving $0$ via repeated-row alternation). Cramer's rule is the adjugate formula applied to a linear system.**

---

# What Makes This Hard

The trap is in the *sign* $(-1)^{i+j}$ in the cofactor: it is easy to forget where the sign comes from, or to use the wrong sign convention. The clean way to remember: the cofactor $C_{ij}$ accounts for the *permutation* required to move row $i$ and column $j$ to the "outside" before computing the minor. Going from a matrix with $(i, j)$-entry 1 and other entries in the row/column equal to zero to its "natural" form requires $i - 1$ row swaps and $j - 1$ column swaps, total $(i - 1) + (j - 1) = i + j - 2$ swaps, hence a sign of $(-1)^{i + j - 2} = (-1)^{i + j}$.

A second pitfall: the adjugate is the *transpose* of the cofactor matrix. Many textbooks (and student attempts) get this transpose wrong, leading to a formula that almost works but with the indices swapped. The way to remember: $(\operatorname{adj} A)_{ij} = C_{ji}$, with the indices swapped relative to the cofactor.

A third pitfall: Cramer's rule is *not* the algorithm to use for numerical computation. The cost of computing $n + 1$ many $n \times n$ determinants is dominated by Leibniz at $O((n+1) \cdot n!)$ — vastly worse than Gaussian elimination's $O(n^3)$. Use Cramer's rule for theory and for explicit formulas with small $n$; use Gaussian elimination for computation.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**

Cofactor expansion follows from multilinearity in one column and the alternating property. The adjugate formula combines two cofactor expansions, one for the diagonal entry (giving $\det A$) and one for off-diagonal entries (giving zero via repeated rows). Cramer's rule is the adjugate formula applied to $Ax = b$.

**Subgoal decomposition:**

1. **Prove cofactor expansion along column $j$.** Apply multilinearity in column $j$ of $\det$, expand $a_j = \sum_i A_{ij} e_i$, and use alternation to relate $\det(a_1, \dots, e_i, \dots, a_n)$ to $(-1)^{i+j} M_{ij}$.
   - *Hint:* The sign $(-1)^{i+j}$ comes from the permutation moving $e_i$ in column $j$ to position $(n, n)$, requiring $i + j - 2$ swaps.

2. **Prove cofactor expansion along row $i$.** By taking transpose: $\det A = \det A^t$, and column expansion of $A^t$ is row expansion of $A$.

3. **Compute $(A \cdot \operatorname{adj}(A))_{ii} = \det A$.** This is cofactor expansion of $A$ along row $i$.

4. **Compute $(A \cdot \operatorname{adj}(A))_{ij} = 0$ for $i \neq j$.** This is cofactor expansion of a matrix with row $j$ replaced by row $i$ (so two equal rows), giving $\det = 0$.

5. **Derive Cramer's rule.** From $A \cdot \operatorname{adj}(A) = (\det A) I$, multiply $A x = b$ on the left by $\operatorname{adj}(A)$ to get $(\det A) x = (\operatorname{adj} A) b$. Read off the components.

---

# Lemma Decomposition

> [!note]- Lemma 1: Cofactor expansion along a column
> **Statement:** For an $n \times n$ matrix $A$ and any column index $j$, $\det A = \sum_{i=1}^n (-1)^{i+j} A_{ij} M_{ij}$.
>
> **Hint:** Apply multilinearity of $\det$ in column $j$, then use alternation to compute $\det$ of matrices with a column equal to $e_i$.
>
> **Why needed:** This is the core combinatorial identity.
>
> > [!note]- Full proof
> > Let $a_1, \dots, a_n$ be the columns of $A$. Write $a_j = \sum_i A_{ij} e_i$ (decomposing in the standard basis). By multilinearity in slot $j$,
> > $$\det A = \det(a_1, \dots, a_j, \dots, a_n) = \sum_i A_{ij} \det(a_1, \dots, e_i, \dots, a_n),$$
> > where $e_i$ replaces $a_j$ in slot $j$. Now $\det(a_1, \dots, e_i, \dots, a_n)$ is the determinant of a matrix whose $j$-th column is $e_i$ (a standard basis vector with a single 1 in row $i$). Move column $j$ to column $n$ by $n - j$ swaps of adjacent columns, each multiplying $\det$ by $-1$; sign factor $(-1)^{n-j}$. Then move row $i$ to row $n$ by $n - i$ swaps; sign factor $(-1)^{n-i}$. The matrix now has $1$ in position $(n, n)$, zeros in row $n$ and column $n$ otherwise, and the upper-left $(n-1) \times (n-1)$ block is $M_{ij}$. The determinant of this matrix equals $M_{ij}$. Total sign factor: $(-1)^{(n-j) + (n-i)} = (-1)^{2n - i - j} = (-1)^{-i - j} = (-1)^{i + j}$. Hence $\det(a_1, \dots, e_i, \dots, a_n) = (-1)^{i+j} M_{ij}$, completing the formula.

> [!note]- Lemma 2: $A \cdot \operatorname{adj}(A) = (\det A) I$
> **Statement:** For any $n \times n$ matrix $A$, $A \cdot \operatorname{adj}(A) = (\det A) I$.
>
> **Hint:** Compute the $(i, k)$-entry of $A \cdot \operatorname{adj}(A)$. For $i = k$, this is cofactor expansion of $A$ along row $i$, giving $\det A$. For $i \neq k$, this is cofactor expansion of a matrix $A'$ obtained from $A$ by replacing row $k$ with row $i$, hence $A'$ has two equal rows and $\det A' = 0$.
>
> **Why needed:** This is the adjugate formula, the source of Cramer's rule and the formula $A^{-1} = \operatorname{adj}(A)/\det A$.
>
> > [!note]- Full proof
> > By definition, $(A \cdot \operatorname{adj}(A))_{ik} = \sum_j A_{ij} (\operatorname{adj} A)_{jk} = \sum_j A_{ij} C_{kj}$, where $C_{kj}$ is the $(k, j)$-cofactor. By cofactor expansion along row $k$: $\sum_j A'_{kj} C_{kj} = \det A'$, where $A'$ is the matrix with $A_{ij}$ in row $k$ (otherwise equal to $A$). For $i = k$: $A' = A$, so $\sum_j A_{ij} C_{ij} = \det A$. For $i \neq k$: $A'$ has the row $i$ of $A$ duplicated in position $k$ (so rows $i$ and $k$ of $A'$ are equal), hence $\det A' = 0$. So $(A \cdot \operatorname{adj}(A))_{ik} = (\det A) \delta_{ik}$, i.e., $A \cdot \operatorname{adj}(A) = (\det A) I$.

> [!note]- Lemma 3: Cramer's rule from the adjugate formula
> **Statement:** If $A$ is invertible and $A x = b$, then $x_j = \det A_j / \det A$, where $A_j$ is obtained from $A$ by replacing column $j$ with $b$.
>
> **Hint:** Multiply both sides of $A x = b$ on the left by $\operatorname{adj}(A)$. Use $\operatorname{adj}(A) \cdot A = (\det A) I$ to get $(\det A) x = (\operatorname{adj} A) b$. Read off component $j$ and recognise the cofactor expansion of $\det A_j$.
>
> **Why needed:** The explicit formula for the solution of a linear system, useful in proofs and small examples.
>
> > [!note]- Full proof
> > By Lemma 2 applied to $A^t$ (or just by direct computation), $\operatorname{adj}(A) A = (\det A) I$. Multiplying $A x = b$ on the left by $\operatorname{adj}(A)$: $(\operatorname{adj} A)(A x) = (\det A) x = (\operatorname{adj} A) b$. The $j$-th component:
> > $$(\det A) x_j = \sum_i (\operatorname{adj} A)_{ji} b_i = \sum_i C_{ij} b_i.$$
> > The right-hand side is cofactor expansion along column $j$ of the matrix $A_j$ (which equals $A$ except column $j$ is replaced by $b$), so it equals $\det A_j$. Hence $(\det A) x_j = \det A_j$, i.e., $x_j = \det A_j / \det A$.

---

# Formal Proof

> [!note]- Complete formal proof
> The proof is the combination of Lemmas 1, 2, 3.
>
> **Step 0 — Well-posedness.** The minors $M_{ij}$ and cofactors $C_{ij} = (-1)^{i+j} M_{ij}$ are well-defined for any $n \times n$ matrix (with $n \geq 2$; for $n = 1$ the formula is trivially $\det A = A_{11}$).
>
> **Step 1 — Cofactor expansion along column $j$.** By Lemma 1, $\det A = \sum_{i=1}^n A_{ij} C_{ij} = \sum_{i=1}^n (-1)^{i+j} A_{ij} M_{ij}$.
>
> **Step 2 — Cofactor expansion along row $i$.** Apply Step 1 to $A^t$: $\det A^t = \det A$, and column expansion of $A^t$ along column $i$ is row expansion of $A$ along row $i$. So $\det A = \sum_{j} (-1)^{i+j} A_{ij} M_{ij}$.
>
> **Step 3 — Adjugate formula $A \cdot \operatorname{adj}(A) = (\det A) I$.** By Lemma 2.
>
> **Step 4 — Cramer's rule.** By Lemma 3.
>
> **Corollary: $A^{-1} = \operatorname{adj}(A) / \det A$ when $\det A \neq 0$.** From Step 3, $A \cdot \operatorname{adj}(A) = (\det A) I$, so dividing by $\det A$ gives $A \cdot (\operatorname{adj}(A)/\det A) = I$. Hence $A^{-1} = \operatorname{adj}(A)/\det A$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Smoothness of $A^{-1}$ as a function of $A$ on $\mathrm{GL}_n$.** The adjugate formula $A^{-1} = \operatorname{adj}(A) / \det A$ writes $A^{-1}$ as a ratio of polynomials in the entries of $A$. So $A \mapsto A^{-1}$ is a smooth (in fact, rational) map from $\mathrm{GL}_n(\mathbb{R})$ to $\mathrm{GL}_n(\mathbb{R})$. This is the foundation of the implicit function theorem applied to "linear equations vary smoothly with their coefficients".

**[[Thm - Cayley-Hamilton (Minimal-Polynomial Form)|Cayley-Hamilton]] via the adjugate.** The matrix $zI - A$ has determinant $p_A(z) = \det(zI - A)$, the characteristic polynomial. By the adjugate formula, $(zI - A) \operatorname{adj}(zI - A) = p_A(z) I$. Both sides are polynomials in $z$ with matrix coefficients; "substituting $z = A$" (formally, expanding and rearranging) gives $p_A(A) = 0$, the **Cayley-Hamilton theorem**. See [[Ex - Cayley-Hamilton via determinants and via the minimal polynomial agree]].

**Implicit function theorem for linear systems.** Given $F(x, y) = 0$ with $F(x_0, y_0) = 0$ and $\partial F/\partial y(x_0, y_0)$ invertible, the implicit function theorem solves $y$ as a smooth function of $x$ near $x_0$. Computing the derivative $\partial y/\partial x$ requires inverting $\partial F/\partial y$, and Cramer's rule gives this explicitly. This is essential for understanding the smooth dependence of solutions on parameters in differential equations.

**Discrete Laplace operator and the matrix-tree theorem.** For a graph $G$, the **Laplacian matrix** $L$ has interesting cofactors: all cofactors of $L$ are equal (by some clever computation), and their common value is the number of spanning trees of $G$. This is the **matrix-tree theorem**, which uses cofactor expansion essentially.

**Resultant via determinants.** The resultant $\operatorname{Res}(f, g)$ of two polynomials $f, g$ is the determinant of the Sylvester matrix, an $(n + m) \times (n + m)$ matrix built from the coefficients. By cofactor expansion, $\operatorname{Res}$ is a polynomial in the coefficients of $f$ and $g$, and $\operatorname{Res}(f, g) = 0$ iff $f$ and $g$ have a common root. This is the foundational identity in elimination theory.

---

# Bridges

- **[[Def - Determinant|Determinant definition]]** — cofactor expansion is the most useful concrete computational formula. The expansion is a direct corollary of multilinearity (used in the proof). Together with the Leibniz formula and the eigenvalue product, it gives the full toolkit.

- **[[Thm - Determinant is Multiplicative|Multiplicativity of det]]** — used in proving Cayley-Hamilton via the adjugate. The factor-and-multiply pattern $(zI - A) \operatorname{adj}(zI - A) = p_A(z) I$ is the determinantal identity bridging $\det$ multiplicativity and the Cayley-Hamilton theorem.

- **The Cayley-Hamilton theorem** — proved via the adjugate identity. The cofactor formula is the gateway from "the determinant is a polynomial" to "the operator satisfies its own characteristic polynomial".

- **The matrix tree theorem and the Kirchhoff Laplacian** — cofactor expansion applied to specific structured matrices yields combinatorial identities. The matrix-tree theorem counts spanning trees as a cofactor; this is one of the most beautiful theorems in algebraic graph theory.

- **Inverse function theorem and implicit function theorem** — Cramer's rule gives the explicit dependence of the inverse on the original matrix entries, providing the polynomial dependence needed for analytic statements about smoothness.

---

# Unlocked by This

> [!tip] Cayley-Hamilton Theorem *(LADR §9C)*
> Every operator satisfies its own characteristic polynomial: $p_T(T) = 0$. The proof via the adjugate is the most direct: $(zI - T) \operatorname{adj}(zI - T) = p_T(z) I$, then substitute $z = T$. See [[Ex - Cayley-Hamilton via determinants and via the minimal polynomial agree]].

> [!tip] Matrix-Tree Theorem *(from Combinatorics)*
> For a graph $G$ with Laplacian $L$, the number of spanning trees of $G$ equals any cofactor of $L$. The proof uses cofactor expansion combined with the multilinearity of $\det$ and inclusion-exclusion arguments on subgraphs.

> [!tip] Resultant and Elimination Theory *(from Algebraic Geometry)*
> The resultant $\operatorname{Res}(f, g)$ of two polynomials is a determinant (of the Sylvester matrix), and $\operatorname{Res}(f, g) = 0$ iff $f, g$ share a root. Elimination theory uses resultants to eliminate variables in polynomial systems, with the cofactor expansion of the resultant giving explicit polynomial relations.

> [!tip] Polynomial Identity Testing *(from Theoretical Computer Science)*
> The determinant is a polynomial of degree $n$ in $n^2$ variables. Polynomial identity testing — deciding whether a given symbolic expression evaluates to zero — has efficient randomised algorithms when restricted to expressions like determinants. Cofactor expansion is the natural recursion structure for these algorithms.
