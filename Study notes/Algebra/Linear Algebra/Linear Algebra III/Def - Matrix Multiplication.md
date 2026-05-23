---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Matrix of a Linear Map"
  - "Def - Linear Map"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $A \in \mathbf{F}^{m, n}$ is an $m$-by-$n$ matrix and $B \in \mathbf{F}^{n, p}$ is an $n$-by-$p$ matrix, with entries in a field $\mathbf{F}$. Entries are indexed $A_{j, k}$ for "row $j$, column $k$". The product $AB \in \mathbf{F}^{m, p}$ is the matrix defined below. The row notation $A_{j, \cdot}$ denotes the $j$-th row of $A$ (as a $1$-by-$n$ matrix), and the column notation $A_{\cdot, k}$ denotes the $k$-th column (as an $m$-by-$1$ matrix). The full notation registry is on [[Linear Algebra III — §3A–D Linear Maps]].

**Standing convention.** Matrix multiplication is defined *only* when the inner dimensions match: an $m$-by-$n$ times an $n$-by-$p$ gives an $m$-by-$p$, but an $m$-by-$n$ times a $q$-by-$p$ with $q \neq n$ is undefined. Square matrices of the same size always multiply. Matrix multiplication is associative and distributive but **not commutative**: in general $AB \neq BA$ even when both products are defined.

---

# Axiom Motivation

The motivation is not "why this formula" but "why this formula is *forced*". Suppose we have linear maps $T : U \to V$ and $S : V \to W$ between finite-dimensional spaces with chosen bases, and we want to compute the matrix of the composition $ST : U \to W$. The composition is the linear map $u \mapsto S(T(u))$, and we know:

- $\mathcal{M}(T) = B \in \mathbf{F}^{n, p}$ has column $k$ equal to the coordinate column of $T u_k$ in the $V$-basis: $T u_k = \sum_r B_{r, k} v_r$.
- $\mathcal{M}(S) = A \in \mathbf{F}^{m, n}$ has column $r$ equal to the coordinate column of $S v_r$ in the $W$-basis: $S v_r = \sum_j A_{j, r} w_j$.

Computing $(ST)(u_k) = S(T(u_k))$ directly:

$$(ST)(u_k) \;=\; S\!\left(\sum_{r=1}^n B_{r, k} v_r\right) \;=\; \sum_{r=1}^n B_{r, k}\, Sv_r \;=\; \sum_{r=1}^n B_{r, k} \sum_{j=1}^m A_{j, r} w_j \;=\; \sum_{j=1}^m \left(\sum_{r=1}^n A_{j, r} B_{r, k}\right) w_j.$$

So the coefficient of $w_j$ in $(ST)(u_k)$ — which is, by definition, the $(j, k)$-entry of $\mathcal{M}(ST)$ — equals $\sum_{r=1}^n A_{j, r} B_{r, k}$. This is the row-$j$-of-$A$-times-column-$k$-of-$B$ dot product. The only way to define a "product" $AB$ that makes $\mathcal{M}(ST) = \mathcal{M}(S)\, \mathcal{M}(T)$ — the equation we *must* have for matrix bookkeeping to track composition — is the formula

$$(AB)_{j, k} \;=\; \sum_{r=1}^n A_{j, r} B_{r, k}.$$

That is the entire content of the definition. Matrix multiplication is **not** an arbitrary combinatorial operation; it is the operation reverse-engineered from the demand that representations respect composition. Every property of matrix multiplication — associativity, distributivity, non-commutativity, the dimension-compatibility rule — is a property *inherited from composition of linear maps*.

This explains immediately several otherwise-mysterious features:

1. **Why the inner [[Def - Dimension|dimensions]] must match.** Composition $S \circ T$ requires the codomain of $T$ to equal the domain of $S$; in [[Def - Dimension|dimensions]], the codomain of $T$ has dimension $n$ (the inner index of $\mathcal{M}(T)$, columns of $B$ being inputs in $V$ of dimension $n$ — wait, rows of $B$). Concretely, $B \in \mathbf{F}^{n, p}$ means $T : U \to V$ with $\dim U = p$, $\dim V = n$; and $A \in \mathbf{F}^{m, n}$ means $S : V \to W$ with $\dim V = n$, $\dim W = m$. The inner $n$ is the shared dimension of $V$, and matching it is matching codomain-of-$T$ with domain-of-$S$.

2. **Why $AB \neq BA$ in general.** Composition of linear maps is non-commutative: do-$T$-then-$S$ is genuinely different from do-$S$-then-$T$ when the maps are different. Concrete example: on $\mathcal{P}(\mathbb{R})$, let $T$ multiply by $x^2$ and $D$ differentiate; then $(DT)p = (x^2 p)' = x^2 p' + 2x p$ but $(TD)p = x^2 p'$, so $DT \neq TD$. The non-commutativity of matrix multiplication is the matrix shadow of the non-commutativity of composition.

3. **Why matrix multiplication is associative.** Composition of functions is always associative — $(S \circ T) \circ R = S \circ (T \circ R)$ — and the corresponding matrices inherit this: $(AB)C = A(BC)$.

4. **Why matrix multiplication is distributive over addition.** Linear maps are pointwise: $(S_1 + S_2) \circ T = S_1 \circ T + S_2 \circ T$ and $S \circ (T_1 + T_2) = S \circ T_1 + S \circ T_2$, so the matrices satisfy $(A_1 + A_2) B = A_1 B + A_2 B$ and $A(B_1 + B_2) = A B_1 + A B_2$.

5. **Why the multi-views of matrix multiplication exist.** Once the definition is in place, the dot-product-row-times-column form is one view, but several others are equivalent: column $k$ of $AB$ equals $A$ times column $k$ of $B$ (i.e., $(AB)_{\cdot, k} = A B_{\cdot, k}$); row $j$ of $AB$ equals row $j$ of $A$ times $B$; and $Ax$ for $x \in \mathbf{F}^{n, 1}$ is the linear combination of columns of $A$ with coefficients $x_k$. Each view emphasises a different aspect of "composition", and they are all rigid consequences of the single formula.

The mystery of why the formula looks the way it does is removed by remembering that the formula was *designed* — by the inventors of the notation in the 19th century — to make exactly one thing true: composition of linear maps corresponds to multiplication of their matrices.

---

# The Definition

Let $A \in \mathbf{F}^{m, n}$ and $B \in \mathbf{F}^{n, p}$ be matrices over a field $\mathbf{F}$. The **product** $AB$ is the $m$-by-$p$ matrix whose entry in row $j$, column $k$ is

$$(AB)_{j, k} \;:=\; \sum_{r=1}^{n} A_{j, r}\, B_{r, k} \quad \text{for } 1 \leq j \leq m,\; 1 \leq k \leq p.$$

In words: the entry in row $j$, column $k$ of $AB$ is the dot product of **row $j$ of $A$** with **column $k$ of $B$**.

Matrix multiplication is **defined only** when the number of columns of $A$ equals the number of rows of $B$ — the common dimension $n$ that gets summed over.

**Equivalent views.** For $A \in \mathbf{F}^{m, n}$ and $B \in \mathbf{F}^{n, p}$:

1. **Entry-wise (row times column).** $(AB)_{j, k} = A_{j, \cdot}\, B_{\cdot, k}$.

2. **Column-wise.** $(AB)_{\cdot, k} = A\, B_{\cdot, k}$ for each $k = 1, \ldots, p$ — column $k$ of $AB$ is $A$ times column $k$ of $B$.

3. **Row-wise.** $(AB)_{j, \cdot} = A_{j, \cdot}\, B$ for each $j = 1, \ldots, m$ — row $j$ of $AB$ is row $j$ of $A$ times $B$.

4. **Linear combination of columns.** For $x = (x_1, \ldots, x_n)^T \in \mathbf{F}^{n, 1}$,

$$A x \;=\; x_1\, A_{\cdot, 1} + x_2\, A_{\cdot, 2} + \cdots + x_n\, A_{\cdot, n}.$$

That is, $Ax$ is the linear combination of the columns of $A$ with coefficients from $x$.

**Algebraic properties.** For matrices of compatible dimensions:

- **Associativity:** $(AB)C = A(BC)$.
- **Distributivity:** $A(B + C) = AB + AC$ and $(B + C) A = BA + CA$.
- **Scalar compatibility:** $(\lambda A) B = \lambda (AB) = A (\lambda B)$ for $\lambda \in \mathbf{F}$.
- **Identity:** $I_m A = A = A I_n$ for $A \in \mathbf{F}^{m, n}$.
- **Transpose:** $(AB)^T = B^T A^T$.
- **Non-commutativity:** $AB \neq BA$ in general, even when both products are defined.

---

# Categorical / Structural Definition

Matrix multiplication is, structurally, **composition in the category of matrices**. Define $\operatorname{Mat}_\mathbf{F}$ as the category whose objects are positive integers (or, equivalently, the spaces $\mathbf{F}^n$) and whose morphisms $n \to m$ are $m$-by-$n$ matrices over $\mathbf{F}$. Composition is matrix multiplication, and the identity morphism on $n$ is $I_n$. The associativity and identity axioms for a category are exactly the algebraic properties above.

The category $\operatorname{Mat}_\mathbf{F}$ is **equivalent** to the category $\mathbf{Vect}_\mathbf{F}^{\mathrm{fin}}$ of finite-dimensional vector spaces (with chosen bases) via the functor "send $n$ to $\mathbf{F}^n$ and send a matrix to the linear map it represents in standard bases". Matrix multiplication is the composition operation of $\operatorname{Mat}_\mathbf{F}$, and equivalence of categories transfers this to composition in $\mathbf{Vect}_\mathbf{F}^{\mathrm{fin}}$.

For square matrices, the set $M_n(\mathbf{F}) = \mathbf{F}^{n, n}$ under matrix addition and matrix multiplication forms a **non-commutative associative algebra** over $\mathbf{F}$: it has a multiplicative identity ($I_n$), associativity, distributivity, and scalar compatibility — all the axioms of an [[Def - Ring|associative algebra]]. The invertible elements form a [[Def - Group|group]] under multiplication, the **general linear [[Def - Group|group]]** $\operatorname{GL}_n(\mathbf{F})$. Both structures are central to the rest of linear algebra.

---

# Relate to Other Fields / Compression

**True name:** "matrix multiplication is composition of linear maps, expressed in coordinates". The dot-product formula is the *computational consequence*, but the *meaning* is composition. Whenever matrix multiplication appears in mathematics or its applications, what is really happening is the composition of two linear operations — even when the linear operations are disguised as something else.

In multivariate calculus, the **chain rule** $\nabla(g \circ f)(x) = (\nabla g)(f(x)) \cdot (\nabla f)(x)$ in coordinates is matrix multiplication: the Jacobian of $g \circ f$ is the matrix product of the Jacobian of $g$ at $f(x)$ with the Jacobian of $f$ at $x$. The product is non-commutative because the order of differentiation matters (do $f$ first, then $g$). See [[Def - The Total Derivative and Differentiability]].

In the theory of [[Def - Module|modules]], matrix multiplication is composition in the category of free modules: $M_n(R)$ for any ring $R$ is the endomorphism ring of $R^n$. For $R = \mathbb{Z}$, the integer matrices $M_n(\mathbb{Z})$ govern the linear algebra of free abelian groups; for $R = \mathbf{F}[x]$, the matrices over a polynomial ring govern the structure of $\mathbf{F}[x]$-modules and thence the Jordan-form theorem.

In Markov-chain theory, matrices are transition matrices: an entry $P_{j, k}$ is the probability of moving from state $j$ to state $k$ in one step (or from $k$ to $j$ in the other convention). The matrix product $P \cdot Q$ tracks "first move according to $Q$, then according to $P$" — composition of transitions. The eigenvalues and eigenvectors of $P$ — themselves objects of [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]] — give the long-run behaviour.

In quantum mechanics, observables are self-adjoint operators on a Hilbert space; in finite dimensions they are matrices. Time evolution is a unitary matrix; composing time evolutions (the dynamics over two intervals) is matrix multiplication of the unitaries; the non-commutativity of observables is the matrix non-commutativity, which expresses the uncertainty principle. The entire formalism of finite-dimensional quantum mechanics is a chapter of matrix algebra.

In numerical linear algebra, the *cost* of multiplying two $n$-by-$n$ matrices is the celebrated open question. The naive algorithm costs $O(n^3)$; Strassen's algorithm (1969) brought this down to $O(n^{\log_2 7}) \approx O(n^{2.807})$; the current best is $O(n^{2.371})$ (Williams 2014 and successors). The true exponent $\omega$ is conjectured to be $2$ — the absolute minimum, since one must at least read every entry — but this remains open. The structural questions of how matrix multiplication can be computed efficiently form a deep subject in their own right.

---

# Examples / Corollaries

**Example: a concrete multiplication.** Multiply a $3$-by-$2$ and a $2$-by-$4$:

$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix} \begin{pmatrix} 6 & 5 & 4 & 3 \\ 2 & 1 & 0 & -1 \end{pmatrix} \;=\; \begin{pmatrix} 10 & 7 & 4 & 1 \\ 26 & 19 & 12 & 5 \\ 42 & 31 & 20 & 9 \end{pmatrix}.$$

The $(2, 1)$-entry of the product is row $2$ of $A$ times column $1$ of $B$: $3 \cdot 6 + 4 \cdot 2 = 18 + 8 = 26$. Each of the $12$ entries of the product is a similar $2$-term sum.

**Example: matrix-vector multiplication as linear combination of columns.** $\begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix} \begin{pmatrix} 5 \\ 1 \end{pmatrix} = \begin{pmatrix} 7 \\ 19 \\ 31 \end{pmatrix}$. This equals $5 \begin{pmatrix} 1 \\ 3 \\ 5 \end{pmatrix} + 1 \begin{pmatrix} 2 \\ 4 \\ 6 \end{pmatrix}$ — five times the first column plus one times the second.

**Example: non-commutativity.** Take $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$. Then $AB = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ but $BA = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$. The two products are both rank-$1$ projections, but onto different lines.

**Example: a vector dotted with a row.** A $1$-by-$n$ matrix times an $n$-by-$1$ matrix is a $1$-by-$1$ matrix — a scalar. $\begin{pmatrix} 3 & 4 \end{pmatrix} \begin{pmatrix} 6 \\ 2 \end{pmatrix} = (3)(6) + (4)(2) = 26$.

**Example: matrix powers.** For a square matrix $A \in \mathbf{F}^{n, n}$, define $A^0 = I_n$, $A^1 = A$, $A^k = A \cdot A^{k-1}$ for $k \geq 2$. The entry $(A^3)_{j, k}$ is a triple sum: $\sum_p \sum_r A_{j, p} A_{p, r} A_{r, k}$. For an adjacency matrix of a graph, $(A^k)_{j, k}$ counts the number of paths of length $k$ from vertex $j$ to vertex $k$. The same identity for transition matrices in a Markov chain: $(P^k)_{j, k}$ is the probability of being at state $k$ after $k$ steps starting from state $j$ (when $P_{j, k}$ is the one-step probability).

**Non-example (dimension mismatch).** $A = \begin{pmatrix} 1 & 2 \end{pmatrix}$ (a $1$-by-$2$) and $B = \begin{pmatrix} 1 & 2 & 3 \end{pmatrix}$ (a $1$-by-$3$). The product $AB$ is **undefined** because the inner dimensions $2$ and $1$ disagree (cols of $A$ is $2$, rows of $B$ is $1$). The product $BA$ is also undefined for the same reason in reverse.

**Corollary (linearity in each argument).** $(\lambda A + B) C = \lambda (AC) + BC$ and $A (\lambda B + C) = \lambda (AB) + AC$. Matrix multiplication is a *bilinear* operation $\mathbf{F}^{m, n} \times \mathbf{F}^{n, p} \to \mathbf{F}^{m, p}$.

**Corollary (associativity).** $(AB)C = A(BC)$ whenever the products are defined. Proof: compute the $(j, l)$-entry of both sides, both equal $\sum_{r, s} A_{j, r} B_{r, s} C_{s, l}$. The cleaner proof is via composition: matrix multiplication tracks composition of linear maps, and function composition is associative, so matrix multiplication is associative. (Emil Artin: "It is my experience that proofs involving matrices can be shortened by 50% if one throws the matrices out.")

**Corollary (transpose reverses order).** $(AB)^T = B^T A^T$. Proof: the $(k, j)$-entry of $(AB)^T$ is the $(j, k)$-entry of $AB$, which is $\sum_r A_{j, r} B_{r, k}$. The $(k, j)$-entry of $B^T A^T$ is $\sum_r (B^T)_{k, r} (A^T)_{r, j} = \sum_r B_{r, k} A_{j, r}$, the same sum. The reversal is the operational counterpart of "the dual of a composition is the composition of duals in reverse order" — a categorical phenomenon.

**Corollary (rank bound on a product).** $\operatorname{rank}(AB) \leq \min\{\operatorname{rank} A, \operatorname{rank} B\}$. Each column of $AB$ is a linear combination of columns of $A$ (column-wise view), so the column span of $AB$ is contained in the column span of $A$, giving $\operatorname{rank}(AB) \leq \operatorname{rank} A$. Each row of $AB$ is a linear combination of rows of $B$ (row-wise view), giving $\operatorname{rank}(AB) \leq \operatorname{rank} B$. See [[Ex - Rank of a product is bounded by individual ranks]].

**Calibration check.** A reader who has understood the definition should be able to verify, in under a minute each: (1) the product of a $3$-by-$2$ matrix and a $2$-by-$3$ matrix is a $3$-by-$3$ matrix; (2) the product of a $1$-by-$n$ row and an $n$-by-$1$ column is a $1$-by-$1$ matrix (a scalar); (3) for square $A, B$ of the same size, $AB$ and $BA$ both exist but are typically not equal.

---

# Unlocked by This

> [!tip] Matrix Ring and Polynomial Algebra *(from Ring Theory)*
> The $n$-by-$n$ matrices over $\mathbf{F}$ form a [[Def - Ring|ring]] $M_n(\mathbf{F})$ under addition and multiplication. Polynomials in a single matrix $A$ — $p(A) = a_k A^k + \cdots + a_1 A + a_0 I$ — make sense and produce the **polynomial algebra generated by $A$**. The minimal polynomial of $A$ is the lowest-degree monic polynomial $p$ with $p(A) = 0$; this is the generator of the kernel of the ring homomorphism $\mathbf{F}[x] \to M_n(\mathbf{F})$, $x \mapsto A$, and it controls the operator theory of $A$. See [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

> [!tip] General Linear Group *(from Lie Theory)*
> The invertible matrices in $M_n(\mathbf{F})$ form a [[Def - Group|group]] $\operatorname{GL}_n(\mathbf{F})$ under matrix multiplication — the **general linear group**. It is the prototypical matrix Lie group, and its closed subgroups — $\operatorname{SL}_n$, $\operatorname{O}(n)$, $\operatorname{U}(n)$, $\operatorname{Sp}_n$ — are the classical matrix Lie groups, the bread and butter of representation theory, geometry, and physics.

> [!tip] Tensor Product and Multilinear Algebra *(from Linear Algebra IX)*
> Matrix multiplication is a special case of **tensor contraction**: $(AB)_{j, k} = \sum_r A_{j, r} B_{r, k}$ is the contraction of an upper-row index of $A$ with the lower-row index of $B$. More general tensor contractions multiply arrays of higher rank; matrix multiplication is the rank-$2$ case. The unifying setting is the **tensor algebra** of a vector space. See [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]].

> [!tip] Block Matrix Multiplication *(from Applied Linear Algebra)*
> Matrices can be partitioned into blocks, and matrix multiplication respects the partitioning: a product of block matrices is computed by the "same" row-times-column formula at the block level, provided the block sizes match. This is the algorithmic basis of **block Gauss elimination**, the **Schur complement**, and the high-performance linear-algebra libraries used in scientific computing. See Boyd's treatment in [[Linear Algebra X — Applied I — Vectors, Distance, Equations, Dynamics]].
