---
type: definition
subject: linear-algebra
prereqs:
tags: [algebra, linear-algebra, applied]
---

# Notation

Throughout, $A \in \mathbb R^{m \times n}$ is a matrix; $I_n$ and $I_m$ are the identity matrices of size $n$ and $m$. A **left inverse** of $A$ is a matrix $X \in \mathbb R^{n \times m}$ with $XA = I_n$. A **right inverse** is a matrix $X \in \mathbb R^{n \times m}$ with $AX = I_m$. The **(two-sided) inverse** is denoted $A^{-1}$. The **pseudoinverse** $A^\dagger$ refers, in this topic, to the Moore-Penrose pseudoinverse, which specialises depending on the shape of $A$.

This is a compound page: it defines four interlocking notions — **left inverse**, **right inverse**, **(two-sided) inverse**, and **pseudoinverse** — because they form a structured family of "inverses" appropriate to different shapes and ranks of $A$, and one cannot understand the structure without all four.

---

# Axiom Motivation

The desideratum is to generalise the scalar notion of multiplicative inverse — "the number $1/a$ such that $a \cdot (1/a) = 1$" — to matrices. For non-zero scalars this is unique and always exists. For matrices the story is richer: the analogue of "multiplication" has two sides ($XA$ versus $AX$), and a matrix may have a left inverse but no right inverse, or vice versa, or both, or neither. The framework of left and right inverses captures these possibilities.

The motivation for the **left inverse** comes from the problem of *solving over-determined linear systems*. Suppose $A \in \mathbb R^{m \times n}$ is tall ($m \geq n$) with linearly independent columns, and we are given $b \in \mathbb R^m$ with the hope that $Ax = b$ has a solution. If a left inverse $C$ exists ($CA = I$), then we can recover $x$ from $b$ by $x = C b$: if $Ax = b$, then $C b = C A x = I x = x$. So the left inverse is "the tool that undoes $A$", but only on the column space of $A$ — applying it to $b$ outside the column space gives some $x$ with $A x \neq b$, which simply means the system has no exact solution.

The motivation for the **right inverse** comes from the dual problem of *solving under-determined systems*. Suppose $A$ is wide ($m \leq n$) with linearly independent rows, and we want *some* solution $x$ to $Ax = b$. If a right inverse $B$ exists ($AB = I$), then $x = B b$ is one solution: $A x = A B b = I b = b$. The right inverse is "a section of $A$" — it picks out one $x$ for each $b$, even though there may be many.

These two notions emerge as separate concepts because $A$ is not symmetric in its rows and columns. A tall matrix has *more rows than columns*, so its rows are typically dependent (an over-determined system); its columns can be independent (giving a left inverse). A wide matrix is the opposite. Only square matrices can be invertible from both sides, and for them the two notions coincide.

What goes wrong with nearby variants? **Suppose we tried to define "an inverse" as any matrix $X$ with $AX$ and $XA$ both close to $I$ but not exactly $I$**. This is the world of *approximate inverses* and *preconditioners*, used in numerical linear algebra. It is genuinely useful when $A$ is ill-conditioned, but it conflates two distinct things: exact inverses (when they exist) and approximations (when they do not). The crisp notion above lets us separate these.

**What if we required both $XA = I$ and $AX = I$ simultaneously?** Then $A$ must be square (counting [[Def - Dimension|dimensions]]: $n = m$ on both sides), and a matrix with both a left and a right inverse has $X = Y$ (where $Y$ is any other right inverse), so the inverse is unique. This is the **two-sided inverse**, denoted $A^{-1}$, and the matrix is then called **invertible** or **nonsingular**. For square matrices, having a one-sided inverse forces having a two-sided inverse: this is the non-trivial theorem that the [[Thm - Conditions for a Square Matrix to be Invertible|six equivalent conditions]] for invertibility codify.

**Why is the inverse, when it exists, unique?** Suppose $A X = I = Y A$. Then $X = (Y A) X = Y (A X) = Y I = Y$, so any left inverse equals any right inverse. So a matrix with both a left and a right inverse has a *unique* two-sided inverse, and this is the matrix denoted $A^{-1}$.

**Why introduce the [[Def - Pseudoinverse|pseudoinverse]]?** When $A$ is *not* square (so no two-sided inverse exists), but has linearly independent columns (so a left inverse exists), the choice of left inverse is generally not unique — there can be infinitely many. The **Moore–Penrose pseudoinverse** $A^\dagger = (A^T A)^{-1} A^T$ singles out a canonical one: the unique left inverse with smallest Frobenius norm, equivalently the one obtained from the QR factorization $A = QR$ by $A^\dagger = R^{-1} Q^T$. This canonical left inverse has the additional property that $\hat x = A^\dagger b$ is the **least-squares solution** of $Ax = b$: it minimises $\|Ax - b\|^2$ when the system is over-determined.

---

# The Definition

**Left inverse.** A matrix $X \in \mathbb R^{n \times m}$ is a **left inverse** of $A \in \mathbb R^{m \times n}$ if
$$XA = I_n.$$
The matrix $A$ is **left-invertible** if a left inverse exists. Left invertibility requires $m \geq n$ (the matrix must be square or tall).

**Right inverse.** A matrix $X \in \mathbb R^{n \times m}$ is a **right inverse** of $A \in \mathbb R^{m \times n}$ if
$$AX = I_m.$$
The matrix $A$ is **right-invertible** if a right inverse exists. Right invertibility requires $m \leq n$ (the matrix must be square or wide).

**Two-sided inverse.** If $A$ has both a left inverse $Y$ and a right inverse $X$, then $X = Y$ and this common matrix is the **inverse** $A^{-1}$:
$$A A^{-1} = A^{-1} A = I.$$
A square matrix with a two-sided inverse is called **invertible** or **nonsingular**. A square matrix without one is **singular**.

**Properties of the inverse.**
1. **Inverse of inverse:** $(A^{-1})^{-1} = A$.
2. **Inverse of transpose:** $(A^T)^{-1} = (A^{-1})^T$, sometimes written $A^{-T}$.
3. **Inverse of product:** $(AB)^{-1} = B^{-1} A^{-1}$ (note the reversed order).
4. **Inverse of scalar multiple:** $(\alpha A)^{-1} = (1/\alpha) A^{-1}$ for $\alpha \neq 0$.
5. **Inverse of orthogonal matrix:** if $Q^T Q = I$ (square $Q$), then $Q^{-1} = Q^T$.
6. **Inverse of diagonal matrix:** $\operatorname{diag}(a_1, \dots, a_n)^{-1} = \operatorname{diag}(1/a_1, \dots, 1/a_n)$ when all $a_i \neq 0$.

**[[Def - Pseudoinverse|Pseudoinverse]] (left-invertible case).** For $A \in \mathbb R^{m \times n}$ with $m \geq n$ and linearly independent columns, the **Moore-Penrose pseudoinverse** is
$$A^\dagger = (A^T A)^{-1} A^T \in \mathbb R^{n \times m}.$$
This is a left inverse: $A^\dagger A = (A^T A)^{-1}(A^T A) = I_n$. The matrix $A^T A$ is the **Gram matrix** of the columns of $A$, and is invertible exactly when the columns are linearly independent.

**Pseudoinverse (right-invertible case).** For $A \in \mathbb R^{m \times n}$ with $m \leq n$ and linearly independent rows, the **Moore-Penrose pseudoinverse** is
$$A^\dagger = A^T (A A^T)^{-1} \in \mathbb R^{n \times m}.$$
This is a right inverse: $A A^\dagger = (A A^T)(A A^T)^{-1} = I_m$.

**Equivalent characterisations for square matrices.** For $A \in \mathbb R^{n \times n}$, the following are equivalent:
1. $A$ is invertible.
2. $A$ has linearly independent columns.
3. $A$ has linearly independent rows.
4. $A$ has a left inverse.
5. $A$ has a right inverse.
6. $A x = b$ has a unique solution for every $b \in \mathbb R^n$.
7. $A x = 0$ has only the trivial solution $x = 0$.
8. $\det A \neq 0$.

See [[Thm - Conditions for a Square Matrix to be Invertible]] for details.

---

# Relate to Other Fields / Compression

The notion of inverse for matrices is the special case, in the **monoid of matrices under multiplication**, of inverses in any monoid. The complication that left and right inverses can differ — and that one-sided invertibility is weaker than two-sided — is general to non-commutative monoids; for *commutative* monoids (like $(\mathbb R, \cdot)$ for scalars) the two-sidedness is automatic.

In the language of [[Def - Linear Map|linear maps]], a left inverse of $A : \mathbb R^n \to \mathbb R^m$ is a left inverse of the corresponding linear map: a map $C : \mathbb R^m \to \mathbb R^n$ with $C \circ A = \operatorname{id}_{\mathbb R^n}$. This forces $A$ to be injective. A right inverse is a *section*: a map $B : \mathbb R^m \to \mathbb R^n$ with $A \circ B = \operatorname{id}_{\mathbb R^m}$, which forces $A$ to be surjective. The two-sided inverse exists iff $A$ is bijective.

In the language of categories, an isomorphism is exactly a morphism with a two-sided inverse, and the bijective linear maps $\mathbb R^n \to \mathbb R^n$ are the isomorphisms in the category of finite-dimensional real vector spaces. They form a group under composition, the **general linear group** $GL_n(\mathbb R)$, which is the same as the group of $n \times n$ invertible matrices under multiplication.

The pseudoinverse generalises further: for *any* matrix (not just left- or right-invertible), the **Moore–Penrose pseudoinverse** $A^\dagger$ is the unique matrix satisfying four conditions: $AA^\dagger A = A$, $A^\dagger A A^\dagger = A^\dagger$, $(AA^\dagger)^T = AA^\dagger$, $(A^\dagger A)^T = A^\dagger A$. For full-rank tall matrices it reduces to $(A^T A)^{-1} A^T$; for full-rank wide matrices, to $A^T (AA^T)^{-1}$; for square invertible matrices, to $A^{-1}$. So the pseudoinverse is a *universal* notion of inverse that always exists.

**True name:** The inverse of a matrix is *the matrix that undoes it*. Left inverse: undoes from the left (column-side). Right inverse: undoes from the right (row-side). Two-sided inverse: undoes from both sides, exists only for square full-rank matrices, and is unique when it exists. Pseudoinverse: the canonical "best" choice when uniqueness fails or two-sided existence fails.

---

# Examples / Corollaries

**Is an instance — square invertible matrix.** $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$. The determinant is $2 - 1 = 1 \neq 0$, so $A$ is invertible, with $A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$. Verify: $AA^{-1} = \begin{pmatrix} 2 - 1 & -2 + 2 \\ 1 - 1 & -1 + 2 \end{pmatrix} = I$ ✓.

**Is an instance — multiple left inverses.** $A = \begin{pmatrix} -3 & -4 \\ 4 & 6 \\ 1 & 1 \end{pmatrix}$ has two distinct left inverses (Boyd's example): $B = (1/9)\begin{pmatrix} -11 & -10 & 16 \\ 7 & 8 & -11 \end{pmatrix}$ and $C = (1/2)\begin{pmatrix} 0 & -1 & 6 \\ 0 & 1 & -4 \end{pmatrix}$. Both satisfy $BA = CA = I_2$, but $B \neq C$. The matrix has linearly independent columns (so a left inverse exists), but is not square (so no unique inverse).

**Is an instance — pseudoinverse computation.** For $A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix}$, $A^T A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, $(A^T A)^{-1} = (1/3)\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$, $A^\dagger = (1/3)\begin{pmatrix} 2 & -1 & 1 \\ -1 & 2 & 1 \end{pmatrix}$. Verify $A^\dagger A = I_2$ by direct multiplication.

**Is an instance — orthogonal matrix.** Any matrix with $Q^T Q = I$ (square or tall with orthonormal columns) has $Q^T$ as a left inverse. For square $Q$ this means $Q^{-1} = Q^T$ — orthogonal matrices have *transposes as inverses*, which is computationally trivial. The rotation matrices in $\mathbb R^2$ are examples: $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ has transpose-inverse $\begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}$, the rotation by $-\theta$.

**Is NOT an instance — singular square matrix.** $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$. The rows are linearly dependent (the second is twice the first), so $A$ is singular. There is no matrix $X$ with $XA = I$ or $AX = I$. This can be confirmed by computing $\det A = 4 - 4 = 0$.

**Is NOT an instance — wide matrix as left-invertible.** $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}$ is wide ($2 \times 3$); its three columns cannot be linearly independent (only $2$-vectors), so no left inverse exists. However, the rows are linearly independent, so a right inverse exists. The pseudoinverse $A^\dagger = A^T (AA^T)^{-1}$ provides one canonical choice.

**Corollary — inverse and orientation.** An invertible $n \times n$ matrix has $\det A \neq 0$, and the sign of $\det A$ determines whether $A$ preserves orientation ($\det > 0$) or reverses it ($\det < 0$). Rotation matrices have $\det = +1$, reflection matrices have $\det = -1$. The inverse $A^{-1}$ has $\det(A^{-1}) = 1/\det A$ with the same sign.

**Corollary — left inverse + linear independence.** If $A$ has a left inverse $C$ ($CA = I$), then the columns of $A$ are linearly independent. Proof: if $Ax = 0$, then $0 = C(Ax) = (CA)x = Ix = x$. So $x = 0$ is the only solution, which is the definition of linear independence.

**Corollary — pseudoinverse is a left inverse.** For tall $A$ with linearly independent columns, $A^\dagger = (A^T A)^{-1} A^T$ satisfies $A^\dagger A = (A^T A)^{-1} (A^T A) = I$. So $A^\dagger$ is *a* left inverse — moreover, it is the canonical one selected by the Moore-Penrose conditions, and the one that gives the least-squares solution $\hat x = A^\dagger b$ of the over-determined system $Ax = b$.

**Calibration check.** Verify that $(AB)^{-1} = B^{-1} A^{-1}$ by direct multiplication: $(AB)(B^{-1} A^{-1}) = A(B B^{-1})A^{-1} = A I A^{-1} = AA^{-1} = I$. Verify that the inverse of the diagonal matrix $\operatorname{diag}(2, 3, 5)$ is $\operatorname{diag}(1/2, 1/3, 1/5)$. Verify that an upper-triangular matrix with nonzero diagonal has an upper-triangular inverse (the inverse-of-triangular structure is preserved).

---

# Unlocked by This

> [!tip] Solving Linear Systems via Inverses and QR *(from Boyd Ch 11)*
> When $A$ is invertible, the unique solution of $Ax = b$ is $x = A^{-1} b$. In practice this is computed not by forming $A^{-1}$ explicitly (which is numerically unstable and computationally wasteful) but by **QR factorization**: $A = QR$, then $Rx = Q^T b$, then back-substitution. See [[Thm - QR Factorization via Gram-Schmidt (Boyd)]].

> [!tip] Least Squares as Pseudoinverse *(from Linear Algebra XI)*
> The pseudoinverse $A^\dagger = (A^T A)^{-1} A^T$ for a tall full-rank $A$ gives the least-squares solution $\hat x = A^\dagger b$ minimising $\|Ax - b\|^2$. This is the foundation of regression, data fitting, and parameter estimation. See [[Linear Algebra XI — Applied II — Least Squares]] for the full theory.

> [!tip] The General Linear Group and Lie Groups *(from Group Theory and Differential Geometry)*
> The set of invertible $n \times n$ matrices, denoted $GL_n(\mathbb R)$, forms a **group** under matrix multiplication — the **general linear group**. It is a Lie group: a group that is also a smooth manifold (of dimension $n^2$), with smooth multiplication and inversion. Its identity component, the matrices with positive determinant, is $GL_n^+(\mathbb R)$, and it contains the rotation group $SO(n)$ as a compact subgroup.
