---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Left and Right Inverse of a Matrix"
tags: [algebra, linear-algebra, applied]
---

# Notation

Throughout, $A \in \mathbb R^{n \times n}$ is a square matrix; the columns are $a_1, \dots, a_n$ and the rows are $b_1^T, \dots, b_n^T$. The identity matrix is $I = I_n$. The inverse, if it exists, is $A^{-1}$, satisfying $AA^{-1} = A^{-1} A = I$.

---

# Statement

> **Theorem (Equivalent characterisations of invertibility).** For any $A \in \mathbb R^{n \times n}$, the following ten conditions are equivalent:
> 1. $A$ is **invertible**: there exists $A^{-1}$ with $AA^{-1} = A^{-1} A = I$.
> 2. $A$ has a **left inverse**: there exists $C$ with $CA = I$.
> 3. $A$ has a **right inverse**: there exists $B$ with $AB = I$.
> 4. The **columns of $A$ are linearly independent**: $Ax = 0 \implies x = 0$.
> 5. The **rows of $A$ are linearly independent**.
> 6. **$Ax = b$ has a unique solution for every $b \in \mathbb R^n$.**
> 7. **$Ax = b$ has at least one solution for every $b \in \mathbb R^n$** (i.e., $A$ is surjective as a linear map).
> 8. **$Ax = 0$ has only the trivial solution $x = 0$** (i.e., $A$ is injective as a linear map).
> 9. **$\det A \neq 0$.**
> 10. **All eigenvalues of $A$ are nonzero.**

The theorem is sometimes called the **invertibility theorem** or the **rank theorem** (when phrased in terms of full rank), and it is one of the most-quoted results in linear algebra. Each condition is a different "face" of invertibility, and the equivalences let you choose the easiest face to check in any given problem.

---

# Motivation

A square matrix corresponds to a linear map $\mathbb R^n \to \mathbb R^n$, and there are many natural questions one can ask of such a map: is it injective? surjective? does the system $Ax = b$ have a unique solution? do the columns span $\mathbb R^n$? does the determinant vanish? In general (for *non-square* matrices), these questions have *different* answers, and there are matrices that are injective but not surjective (tall left-invertible matrices) or surjective but not injective (wide right-invertible matrices). The remarkable fact for *square* matrices is that all of these questions collapse to a single condition: invertibility.

The theorem is the foundation of every result that conditions on invertibility — the existence of a unique solution to $Ax = b$, the existence of $A^{-1}$, the non-vanishing of $\det A$, the absence of zero eigenvalues. Each of these conditions can be checked in different ways depending on what the problem hands you, and the theorem says they all measure the same thing.

The economic significance of the theorem is that it gives the practitioner **freedom to choose which check is computationally cheapest**. To determine whether $A$ is invertible:
- Check linear independence of columns by Gaussian elimination ($O(n^3)$ flops).
- Check $\det A \neq 0$ by cofactor expansion ($O(n!)$) or LU decomposition ($O(n^3)$).
- Try to solve $Ax = e_1$ and see if it has a unique solution.
- Compute the eigenvalues and check none is zero.
- Try to factor $A = QR$ via Gram-Schmidt and check that $R$ has nonzero diagonal.

All of these are mathematically equivalent, but their computational costs and numerical stability differ wildly. The theorem says you can choose whichever route is convenient — *and* that the theory is consistent: if any of them succeeds, all of them succeed.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis "$A$ is a square matrix" is concrete, but the *practical* hypothesis varies enormously: in different problems you start from different evidence about $A$, and the theorem tells you that one piece of evidence implies all the others.

**Source 1 — known structural form of $A$.** If $A$ is **upper triangular** with nonzero diagonal entries, then $A$ is invertible. The argument: linear independence of columns follows by induction (an upper-triangular column is nonzero in row $k$ but zero below, and to be a linear combination of *earlier* columns it would need to be zero in row $k$, contradiction). Similarly for *lower triangular* and for *diagonal* matrices. The bridge from "triangular with nonzero diagonal" to "invertible" is non-obvious if one only knows the definition $AA^{-1} = I$, but trivial via condition 4.

**Source 2 — orthogonal columns.** If $A$ has *orthonormal columns* (i.e., $A^T A = I$), then $A$ is invertible with $A^{-1} = A^T$. The argument: orthonormal columns are linearly independent (any orthonormal set is), and condition 4 applies. The bridge from "orthonormal" to "invertible" via condition 4 is essentially the only way to see this without computation.

**Source 3 — $A$ is a product of invertibles.** If $A = B C$ where $B, C$ are invertible, then $A$ is invertible with $A^{-1} = C^{-1} B^{-1}$. The bridge: condition 4 holds for $A$ because $Ax = 0 \Rightarrow BCx = 0 \Rightarrow Cx = B^{-1} 0 = 0 \Rightarrow x = C^{-1} 0 = 0$. This is the source most used in algorithm analysis: any LU or QR factorization expresses $A$ as a product, and invertibility is read off.

**Source 4 — $A$ is small perturbation of identity.** If $\|A - I\| < 1$ (Frobenius or spectral norm), then $A$ is invertible by the **Neumann series** $A^{-1} = I + (I - A) + (I - A)^2 + \cdots$, which converges. The bridge is condition 6: for any $b$, define $x_k = b + (I - A)x_{k-1}$, a contraction-mapping iteration that converges to the unique fixed point $x$ with $Ax = b$.

**Targets (Output Amplification)**

The conclusion "$A$ is invertible" delivers $A^{-1}$ as a tool, but the practical content of the theorem is what one can *do* with this conclusion.

**Target 1 — explicit formula for $A^{-1}$ in special cases.** For $2 \times 2$ matrices, invertibility $\Leftrightarrow$ $\det A \neq 0$, and $A^{-1} = (1/\det A)\begin{pmatrix} A_{22} & -A_{12} \\ -A_{21} & A_{11} \end{pmatrix}$. For diagonal matrices, $A^{-1} = \operatorname{diag}(1/A_{11}, \dots, 1/A_{nn})$. For orthogonal matrices, $A^{-1} = A^T$. Each is an instance of the theorem combined with a specific structural property.

**Target 2 — solvability of $Ax = b$.** If $A$ is invertible (by any condition), then for every $b$ the system $Ax = b$ has a unique solution $x = A^{-1} b$. This is the link between invertibility and linear-equation-solving: the existence of $A^{-1}$ is the most powerful possible solvability statement.

**Target 3 — uniqueness of factorization.** Many factorizations of a matrix — LU, QR, Cholesky, eigendecomposition — are *unique* when $A$ is invertible (up to obvious normalisation), but admit many factorisations when $A$ is singular. The theorem provides the unique-factorisation guarantee in the invertible case.

**Target 4 — invariance under similarity.** $A$ and $P A P^{-1}$ (for invertible $P$) are **similar** matrices; they share invertibility (and all eigenvalues, the determinant, the trace, and other "spectral" properties). The equivalence in the theorem implies that whichever side of $P$ we are looking at, "invertible" means the same thing.

---

# Why Is It True

**The mechanism in one bolded line: for a square matrix, "the columns span $\mathbb R^n$" and "the columns are linearly independent" are the same condition — both mean "the columns form a basis", which is what gives every $b$ a unique representation $b = Ax$.**

The non-obvious part of the theorem is the equivalence between *left-invertibility* (conditions 2, 4, 8) and *right-invertibility* (conditions 3, 5, 7) *for square matrices*. For non-square matrices these are genuinely different; a tall matrix can be left-invertible without being right-invertible. The fact that they coincide for squares is the heart of the theorem.

The intuition: for a square matrix, the columns of $A$ are $n$ vectors in $\mathbb R^n$. By the [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces|independence-dimension inequality]] from Boyd Ch 5, $n$ linearly independent vectors in $\mathbb R^n$ automatically *span* $\mathbb R^n$ — they form a basis. So if the columns are linearly independent, every $b \in \mathbb R^n$ can be written uniquely as $\sum_i x_i a_i = Ax$, which is the surjectivity of $A$. Conversely, if every $b$ can be expressed as $Ax$, then in particular each $e_j$ can be, so there exist $b_j$ with $A b_j = e_j$, and the matrix $B$ with columns $b_j$ is a right inverse. Then by the uniqueness of inverses on square matrices, $B$ is also a left inverse, and $B = A^{-1}$.

The independence-dimension inequality is itself a non-trivial fact, requiring an induction argument. The economic content of the invertibility theorem is that, given this inequality, *all the natural conditions on a square matrix become equivalent*.

The determinant and eigenvalue conditions (9 and 10) deserve separate comment. $\det A = 0$ iff the columns are linearly dependent iff $A$ has a nonzero null vector iff $0$ is an eigenvalue. These three statements are equivalent by direct algebraic computation: the determinant of a matrix is a polynomial in its entries that vanishes exactly when the matrix is singular, the null space contains the eigenspace of eigenvalue $0$, and the characteristic polynomial $\det(A - \lambda I)$ has $0$ as a root iff $\det A = 0$.

---

# What Makes This Hard

The proof has many implications to verify, and the *number* of implications is the main hurdle. With ten equivalent conditions, the natural proof — chase implications $1 \Rightarrow 2 \Rightarrow 3 \Rightarrow \cdots \Rightarrow 10 \Rightarrow 1$ — has ten arrows, each needing its own short argument. Organising these arrows cleanly is the challenge.

The non-trivial step in the proof is the equivalence of conditions 4 and 7 (or, what is the same, conditions 2 and 3 for square matrices). This requires the independence-dimension inequality, which is a substantial result in its own right. Once this is in hand, the rest of the theorem is bookkeeping.

A subtle pitfall: the theorem is *specific* to square matrices. For non-square matrices, conditions 4 and 7 are genuinely different (a tall matrix can be injective without being surjective, and vice versa for a wide matrix). Conflating the square and non-square cases is a common error.

Another pitfall: condition 9 (the determinant condition) is *mathematically* equivalent to invertibility but **numerically useless** for large or ill-conditioned matrices. The determinant of a near-singular matrix can be tiny but nonzero, while the matrix is numerically singular. In numerical practice, conditions 4–8 are checked via QR or SVD, not via the determinant.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove the chain of implications $(2) \Rightarrow (4) \Rightarrow (7) \Rightarrow (3) \Rightarrow (1) \Rightarrow (2)$, which gives the equivalence of the four "core" invertibility conditions. Then sketch the remaining conditions (5, 6, 8, 9, 10) as equivalent reformulations.

**Subgoal decomposition:**

1. **Left invertibility $\Rightarrow$ column independence.** If $CA = I$, then $Ax = 0 \Rightarrow CAx = 0 \Rightarrow x = 0$.
   - *Hint:* Multiply $Ax = 0$ on the left by $C$.
   - *Why needed:* Goes from condition 2 to condition 4.

2. **Column independence $\Rightarrow$ columns span $\mathbb R^n$ $\Rightarrow$ right invertibility.** Use the independence-dimension inequality: $n$ linearly independent vectors in $\mathbb R^n$ form a basis. So every $b$ can be uniquely written as $\sum_i x_i a_i = Ax$, hence $A$ is surjective. To get a right inverse, take $b_j$ with $Ab_j = e_j$; the matrix $B$ with columns $b_j$ satisfies $AB = [Ab_1 | \cdots | Ab_n] = [e_1 | \cdots | e_n] = I$.
   - *Hint:* The crucial step is the independence-dimension inequality, an inductive fact about $\mathbb R^n$.
   - *Why needed:* Goes from condition 4 to condition 3 (via condition 7 implicitly).

3. **Right invertibility $\Rightarrow$ left invertibility.** Suppose $AB = I$. Define $X = BA$, so $X A = BA \cdot A = B \cdot (A \cdot A)$... wait, this doesn't quite work. Use instead: from condition 4 (which we've just established), the columns are independent, so the linear map $A : \mathbb R^n \to \mathbb R^n$ is injective. By the rank-nullity theorem (or by counting dimensions), an injective linear map between equal-dimensional spaces is surjective. Hence $A$ has a right inverse, which is the same as $B$, and then $BA = I$ too (by the uniqueness argument).
   - *Hint:* Cleanest is to argue: $AB = I$ and $A(BA) = (AB)A = A$, so $A(BA - I) = 0$. Since the columns of $A$ are linearly independent (condition 4 holds, proved in subgoal 2), $BA - I = 0$, i.e., $BA = I$. So $B$ is also a left inverse.
   - *Why needed:* This is the closure of the loop; it makes $B$ a two-sided inverse.

4. **Two-sided invertibility is unique.** If $A$ has a left inverse $C$ and a right inverse $B$, then $C = (CA)B = C(AB) = C$ and $B = (CA)B = C(AB) = C$, so the two coincide. Hence the inverse is unique.
   - *Hint:* Multiply $C(AB)$ associatively.
   - *Why needed:* Establishes condition 1 from conditions 2 and 3.

5. **Determinant and eigenvalue conditions are equivalent to column independence.** $\det A = 0$ iff columns are linearly dependent (a standard property of determinants); columns are dependent iff $A$ has a nontrivial null vector iff $0$ is an eigenvalue.
   - *Hint:* These are textbook properties of determinants and eigenvalues.
   - *Why needed:* Extends the theorem to conditions 9, 10.

---

# Lemma Decomposition

> [!note]- Lemma 1: Left inverse implies linear independence of columns
> **Statement:** If $A \in \mathbb R^{n \times n}$ has a left inverse $C$ ($CA = I$), then the columns of $A$ are linearly independent.
>
> **Hint:** If $Ax = 0$, multiply both sides on the left by $C$ to get $x = 0$.
>
> **Why needed:** This is the simplest direction in the equivalence chain.
>
> > [!note]- Full proof
> > Suppose $Ax = 0$ for some $x$. Multiplying on the left by $C$: $CAx = C \cdot 0 = 0$. But $CA = I$, so $CAx = Ix = x$. Hence $x = 0$. This means the only linear combination of the columns of $A$ equalling $0$ is the trivial one, i.e., the columns are linearly independent.

> [!note]- Lemma 2: $n$ linearly independent vectors in $\mathbb R^n$ form a basis
> **Statement:** If $a_1, \dots, a_n \in \mathbb R^n$ are linearly independent, then they span $\mathbb R^n$, i.e., every vector in $\mathbb R^n$ is a linear combination of them.
>
> **Hint:** Boyd's independence-dimension inequality says that any list of $n + 1$ vectors in $\mathbb R^n$ is linearly dependent. Apply this to $a_1, \dots, a_n, b$ for an arbitrary $b$.
>
> **Why needed:** This is the heart of the theorem; it converts column-independence to spanning, and hence to surjectivity of $A$.
>
> > [!note]- Full proof
> > By the independence-dimension inequality, the list $a_1, \dots, a_n, b$ of $n + 1$ vectors in $\mathbb R^n$ is linearly dependent. So there exist coefficients $\beta_1, \dots, \beta_n, \beta_{n+1}$, not all zero, with $\sum_i \beta_i a_i + \beta_{n+1} b = 0$.
> >
> > Suppose $\beta_{n+1} = 0$. Then $\sum_i \beta_i a_i = 0$ with not all $\beta_i$ zero, contradicting the linear independence of $a_1, \dots, a_n$. So $\beta_{n+1} \neq 0$, and we can solve:
> > $$b = -\frac{1}{\beta_{n+1}}\sum_i \beta_i a_i = \sum_i \left(-\frac{\beta_i}{\beta_{n+1}}\right) a_i.$$
> > Hence $b$ is a linear combination of $a_1, \dots, a_n$. Since $b$ was arbitrary, every vector in $\mathbb R^n$ is a linear combination.

> [!note]- Lemma 3: Uniqueness of two-sided inverse
> **Statement:** If $A$ has both a left inverse $C$ and a right inverse $B$, then $C = B$, and this matrix is the unique two-sided inverse.
>
> **Hint:** Compute $CAB$ associatively.
>
> **Why needed:** Establishes that the inverse, when it exists, is unique.
>
> > [!note]- Full proof
> > By associativity of matrix multiplication, $C(AB) = (CA)B$. The left side is $C \cdot I = C$. The right side is $I \cdot B = B$. So $C = B$. Uniqueness follows: if $A$ has another left inverse $C'$, the same argument gives $C' = B = C$. Similarly for right inverses.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** For $A \in \mathbb R^{n \times n}$, the ten conditions of the statement are pairwise equivalent.
>
> *Proof.* We prove the chain $(2) \Rightarrow (4) \Rightarrow (3) \Rightarrow (1) \Rightarrow (2)$, then address the remaining conditions.
>
> **$(2) \Rightarrow (4)$**: By Lemma 1, $CA = I$ implies columns of $A$ are linearly independent.
>
> **$(4) \Rightarrow (3)$**: Suppose columns of $A$ are linearly independent. By Lemma 2, they span $\mathbb R^n$. In particular, each standard unit vector $e_j$ is expressible as $e_j = \sum_i (b_j)_i a_i = A b_j$ for some $n$-vector $b_j$. Let $B$ be the matrix with $b_j$ as its $j$-th column. Then $AB = A[b_1 | \cdots | b_n] = [Ab_1 | \cdots | Ab_n] = [e_1 | \cdots | e_n] = I$. So $B$ is a right inverse of $A$.
>
> **$(3) \Rightarrow (1)$**: Suppose $AB = I$. We claim $BA = I$ also. Compute: $A(BA - I) = (AB)A - A = IA - A = 0$. Each column of $A(BA - I)$ is a linear combination of the columns of $A$ summing to $0$. By (4) (which we have already established from (2) implicitly — but here we are at (3), and need to show (4) holds; doing so requires care).
>
> Cleaner organisation: from $(3)$, we deduce $(4)$ for $A^T$ (since $AB = I \Rightarrow B^T A^T = I$, so $B^T$ is a left inverse of $A^T$, so $A^T$ has linearly independent columns by Lemma 1, i.e., $A$ has linearly independent rows). And $A^T$ has the same dimensions as $A$. Now apply $(4) \Rightarrow (3)$ to $A^T$: there exists $C^T$ with $A^T C^T = I$, i.e., $CA = I$. So $A$ has a left inverse $C$. By Lemma 3, $C = B$, and this matrix is the two-sided inverse.
>
> **$(1) \Rightarrow (2)$**: Trivial: $A^{-1}$ is a left inverse.
>
> So conditions (1), (2), (3), (4) are all equivalent. Condition (5) (linear independence of rows) is equivalent to condition (4) applied to $A^T$, hence equivalent. Conditions (6) and (7) follow from (3): right invertibility gives existence for any $b$, and uniqueness follows from left invertibility (suppose $Ax = Ax' = b$; then $A(x - x') = 0$, so by injectivity (condition 8) $x = x'$). Condition (8) is equivalent to (4) (the null space of $A$ is $\{0\}$ iff the columns are independent). Condition (9), $\det A \neq 0$, is equivalent to (4) by the determinant's vanishing-iff-linearly-dependent-columns property, a standard fact about determinants. Condition (10), all eigenvalues nonzero, is equivalent to $\det A \neq 0$ because $\det A = \prod \lambda_i$ (the determinant equals the product of eigenvalues, counted with multiplicity).
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Numerical analysis — condition number and numerical singularity.** A matrix $A$ is mathematically invertible if $\det A \neq 0$, but *numerically* invertible only if the condition number $\kappa(A) = \|A\|\|A^{-1}\| \ll 1/\epsilon_\text{machine}$. The condition number measures how much a tiny perturbation in $b$ can amplify into a large change in the solution $x$ of $Ax = b$. This is a quantitative refinement of the theorem: invertibility is binary, but conditioning is continuous.

**Algebra — invertibility in matrix rings.** The set of $n \times n$ invertible real matrices forms a group under multiplication, the general linear group $GL_n(\mathbb R)$. The theorem applies verbatim to matrices over any field; over a ring (like $\mathbb Z$), invertibility is more restrictive ($\det A$ must be a unit in the ring), and the analogous theorem requires careful restatement.

**Geometry — diffeomorphisms via the inverse function theorem.** The inverse function theorem in multivariate analysis says: if $f : \mathbb R^n \to \mathbb R^n$ is $C^1$ and $Df(z)$ is invertible, then $f$ is locally a diffeomorphism near $z$. The invertibility of the Jacobian $Df(z)$ — a specific square matrix — is the hypothesis, and the theorem of this page is what one checks to see if the hypothesis is satisfied.

**Probability — Gaussian distributions and covariance matrices.** A multivariate Gaussian distribution $\mathcal N(\mu, \Sigma)$ has a well-defined density iff its covariance matrix $\Sigma$ is invertible (i.e., positive *definite*, not just positive semidefinite). If $\Sigma$ is singular, the distribution is supported on a proper affine subspace and has no density relative to Lebesgue measure. The theorem of this page is the structural condition; positive-definiteness adds the spectral refinement.

---

# Bridges

- **[[Def - Left and Right Inverse of a Matrix|Left and right inverses for non-square matrices]]** — for tall left-invertible matrices (more rows than columns, linearly independent columns), left inverses exist but are not unique, and there is no two-sided inverse. The theorem of this page collapses these distinctions for square matrices. The non-square case is where the pseudoinverse becomes the right tool, providing a *canonical* choice of left or right inverse.

- **[[Thm - QR Factorization via Gram-Schmidt (Boyd)|QR factorization]]** — a square matrix $A$ with linearly independent columns has a QR factorization $A = QR$ with $Q$ orthogonal and $R$ upper triangular with positive diagonal. Then $A^{-1} = R^{-1} Q^T$. Computing $A^{-1}$ via QR is the numerical standard, more stable than direct matrix inversion. The condition "linearly independent columns" is condition 4 of the theorem.

- **The determinant function** — the determinant is a multilinear, alternating, normalised function of the columns of $A$. The vanishing of the determinant is equivalent (by the theorem) to all of invertibility's other failure modes. The determinant is also the *unique* function with these properties up to scaling, and its non-vanishing is the canonical algebraic check for invertibility. In numerical practice, however, the determinant is a poor diagnostic (a tiny but nonzero determinant can correspond to numerical singularity).

- **Eigenvalue structure and the spectral theorem** — the eigenvalues of $A$ are the roots of the characteristic polynomial $\det(\lambda I - A) = 0$. Condition 10 ("no zero eigenvalue") is equivalent to invertibility because $\det A = \prod \lambda_i$. The eigenvalues characterise much more than invertibility: they control dynamics ($A^t$ for large $t$), stability, and similarity classes. The theorem says invertibility is *one consequence* of the eigenvalue structure, with the other consequences awaiting in later chapters.

- **The rank-nullity theorem** — for any linear map $A : \mathbb R^n \to \mathbb R^m$, $\dim(\ker A) + \operatorname{rank}(A) = n$. For square $A$, full rank ($n$) means trivial kernel, which is condition 8; conversely, trivial kernel implies full rank (column space dimension $n$), which means $A$ is surjective. This is the abstract version of the equivalence between conditions 7 and 8 of the theorem, proved using rank-nullity.

---

# Unlocked by This

> [!tip] Algorithms for Solving $Ax = b$ *(from Numerical Linear Algebra)*
> Once invertibility is established, every algorithm for solving $Ax = b$ — LU decomposition, QR decomposition, Cholesky decomposition (for symmetric positive definite $A$), Gauss-Seidel iteration, conjugate gradient — relies on different *checkable* conditions equivalent to invertibility, leveraging different structural properties of $A$. The theorem unifies all these.

> [!tip] The General Linear Group $GL_n(\mathbb R)$ *(from Group Theory and Lie Theory)*
> The set of $n \times n$ invertible real matrices forms a group under multiplication. It is the **general linear group** $GL_n(\mathbb R)$, the largest matrix group, containing as subgroups the orthogonal group $O(n)$ (with the additional condition $A^T A = I$), the special linear group $SL_n(\mathbb R)$ ($\det A = 1$), and many others. The theorem is what makes "invertible" a well-defined group-membership condition.

> [!tip] Inverse and Implicit Function Theorems *(from Multivariate Analysis)*
> The **inverse function theorem** says: if a $C^1$ function $f : \mathbb R^n \to \mathbb R^n$ has $Df(z)$ invertible at $z$, then $f$ is locally a diffeomorphism near $z$. The hypothesis is checked by the theorem of this page applied to the Jacobian. The **implicit function theorem** is a related result: it says that the equation $f(x, y) = 0$ can be locally solved for $y$ as a function of $x$ if the relevant partial Jacobian is invertible. Both theorems propagate the invertibility hypothesis from a single matrix to a local property of a function.
