---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Basis"
  - "Def - Vector Space"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $T : V \to W$ is a linear map between finite-dimensional $\mathbf{F}$-vector spaces, $v_1, \ldots, v_n$ is an ordered basis of $V$, and $w_1, \ldots, w_m$ is an ordered basis of $W$. The matrix of $T$ with respect to these bases is denoted $\mathcal{M}(T)$ when the bases are clear from context; the unambiguous form is $\mathcal{M}(T, (v_1, \ldots, v_n), (w_1, \ldots, w_m))$. The entry in row $j$, column $k$ is $A_{j, k}$. The vector space of $m$-by-$n$ matrices with entries in $\mathbf{F}$ is $\mathbf{F}^{m, n}$, of dimension $mn$.

**Standing convention.** A matrix here is a rectangular array of scalars, *together with* an implicit choice of bases for the spaces it represents linear maps between; the matrix in isolation is meaningful as an element of $\mathbf{F}^{m, n}$, but the assignment $T \leftrightarrow \mathcal{M}(T)$ depends on those bases. The first index of $A_{j, k}$ is **row**, the second is **column** — a convention nearly universal but worth stating explicitly to avoid the very common confusion. For the standard basis of $\mathbf{F}^n$, the $k$-th basis vector is $(0, \ldots, 0, 1, 0, \ldots, 0)$ with the $1$ in the $k$-th slot.

This is a compound page: it defines two interlocking notions — **matrix of a linear map** $\mathcal{M}(T)$ and **matrix of a vector** $\mathcal{M}(v)$ — because they are introduced together and the matrix algebra of linear maps cannot be done without both.

---

# Axiom Motivation

The motivation is entirely about *recording* a linear map as finite data. The [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] says a linear map $T : V \to W$ is determined by its values on a basis $v_1, \ldots, v_n$ of $V$: once $Tv_1, \ldots, Tv_n$ are specified, $T$ is fixed. So the question is: how do you efficiently write down $n$ vectors in $W$? Each vector $Tv_k$, being an element of $W$, is uniquely a linear combination of the basis $w_1, \ldots, w_m$: $Tv_k = A_{1, k} w_1 + A_{2, k} w_2 + \cdots + A_{m, k} w_m$ for unique scalars $A_{1, k}, \ldots, A_{m, k} \in \mathbf{F}$. Collect all these scalars into a rectangular array with $m$ rows (one per coordinate in $W$) and $n$ columns (one per basis vector of $V$), and you have the matrix of $T$. The $k$-th column is *literally* the coordinate column of $Tv_k$ in the $W$-basis.

Why this layout — columns indexed by domain basis, rows by codomain basis — rather than the transpose? The convention is forced by the *use* of the matrix. When you compute $Tv$ for an arbitrary $v = \sum_k b_k v_k$, linearity gives $Tv = \sum_k b_k Tv_k = \sum_k b_k \sum_j A_{j, k} w_j = \sum_j \left(\sum_k A_{j, k} b_k\right) w_j$. The $j$-th coordinate of $Tv$ in the $W$-basis is $\sum_k A_{j, k} b_k$, which is exactly *row $j$ of $A$ times column $b$ of coordinates of $v$*. So with this convention, **"apply $T$" = "multiply the matrix on the left of the coordinate column"** — the identity $\mathcal{M}(Tv) = \mathcal{M}(T)\, \mathcal{M}(v)$ becomes the operational reason matrix multiplication and matrix-vector multiplication are defined the way they are. The transpose layout would not make this work; the asymmetry is real.

A second motivation: the matrix is *only* the data of the action on a basis. Two different choices of basis give two different matrices for the same map, and the matrix of $T$ is not a property of $T$ alone but of the triple (map, $V$-basis, $W$-basis). This is the platonic-vs-representation distinction in action. The matrix is the *representation* of $T$; the map is the *platonic object*. [[Thm - Change of Basis Formula|Change of basis]] is the rule for transforming representations of the same platonic object under different basis choices.

A third motivation: in the standard basis of $\mathbf{F}^n$ and $\mathbf{F}^m$, the matrix $\mathcal{M}(T)$ has a very concrete description — its $k$-th column is $T(e_k)$, the value of $T$ on the $k$-th standard basis vector, read as a column vector. So for $T : \mathbf{F}^n \to \mathbf{F}^m$, "the matrix of $T$" is something one can compute by hand in a moment: just apply $T$ to each standard basis vector and write down the result in a column.

Why also define $\mathcal{M}(v)$ — the matrix of a vector? Without it, the identity $\mathcal{M}(Tv) = \mathcal{M}(T)\, \mathcal{M}(v)$ cannot be stated, because the right-hand side has nothing to multiply against. The matrix of a vector is just its coordinate column in a chosen basis: if $v = b_1 v_1 + \cdots + b_n v_n$, then $\mathcal{M}(v) = (b_1, \ldots, b_n)^T$ as an $n$-by-$1$ matrix. This makes vectors and matrices live in the same algebraic universe, and turns "evaluating a linear map" into "multiplying a matrix by a column vector".

---

# The Definition

Let $T \in \mathcal{L}(V, W)$ with $V$ and $W$ finite-dimensional. Choose an ordered basis $v_1, \ldots, v_n$ of $V$ and an ordered basis $w_1, \ldots, w_m$ of $W$.

**Matrix of a linear map.** The **matrix of $T$ with respect to these bases**, denoted $\mathcal{M}(T)$ (or in full, $\mathcal{M}(T, (v_1, \ldots, v_n), (w_1, \ldots, w_m))$), is the $m$-by-$n$ matrix $A$ whose entries $A_{j, k} \in \mathbf{F}$ are defined by

$$T v_k \;=\; A_{1, k}\, w_1 + A_{2, k}\, w_2 + \cdots + A_{m, k}\, w_m \;=\; \sum_{j=1}^{m} A_{j, k}\, w_j$$

for each $k = 1, \ldots, n$. So the $k$-th column of $\mathcal{M}(T)$ is the coordinate column of $Tv_k$ in the $W$-basis.

**Matrix of a vector.** For $v \in V$ written as $v = b_1 v_1 + \cdots + b_n v_n$, the **matrix of $v$ with respect to the $V$-basis** is the $n$-by-$1$ matrix

$$\mathcal{M}(v) \;=\; \begin{pmatrix} b_1 \\ \vdots \\ b_n \end{pmatrix}.$$

**The central identity.** For every $v \in V$,

$$\mathcal{M}(Tv) \;=\; \mathcal{M}(T)\, \mathcal{M}(v),$$

where the right-hand side is the [[Def - Matrix Multiplication|matrix-vector product]]. Read aloud: "the coordinates of $Tv$ are obtained from the coordinates of $v$ by multiplying on the left by the matrix of $T$".

**The matrix isomorphism.** With bases fixed, the map $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$ sending $T \mapsto \mathcal{M}(T)$ is itself a linear map; it is an [[Def - Invertibility and Isomorphism|isomorphism]]. So $\mathcal{L}(V, W) \cong \mathbf{F}^{m, n}$ as vector spaces, and $\dim \mathcal{L}(V, W) = mn$.

---

# Categorical / Structural Definition

The matrix construction is a **representation of a hom-space**. The hom-space $\mathcal{L}(V, W) = \operatorname{Hom}_{\mathbf{Vect}_\mathbf{F}}(V, W)$ in the category of vector spaces is itself a vector space (this is what it means for $\mathbf{Vect}_\mathbf{F}$ to be enriched over itself). Fixing bases of $V$ and $W$ is equivalent to fixing isomorphisms $V \cong \mathbf{F}^n$ and $W \cong \mathbf{F}^m$. These two isomorphisms induce an isomorphism of hom-spaces $\mathcal{L}(V, W) \cong \mathcal{L}(\mathbf{F}^n, \mathbf{F}^m)$, and the right-hand hom-space is (canonically) $\mathbf{F}^{m, n}$ — the matrices being just the coordinate version of the maps.

The functoriality of this is: composition of linear maps becomes matrix multiplication (see [[Thm - Composition Corresponds to Matrix Multiplication]]), and the matrix of the identity operator is the identity matrix. So we have a functor (well, a pair of functors, one for each chosen basis system) from "the category of finite-dimensional vector spaces with chosen bases" to "the category of finite matrices". This functor is faithful and full on each hom-space — once bases are chosen, the linear maps and their matrices are in bijection — and it converts categorical statements about linear maps into computational statements about matrices.

Two different choices of basis give two different such functors, related by [[Thm - Change of Basis Formula|change of basis]] — a natural isomorphism between the functors. This is the abstract reason "the matrix depends on the basis": there are many choices of how to identify $V$ with $\mathbf{F}^n$, and the matrix records the choice.

---

# Relate to Other Fields / Compression

**True name:** "the coordinate description of a linear map". A linear map $T$ is the platonic object — basis-free, intrinsic — and the matrix $\mathcal{M}(T)$ is one of many possible *coordinate-based pictures* of it, with different bases giving different pictures of the same underlying map. The matrix is to the linear map as the Cartesian-coordinate equation $x^2 + y^2 = 1$ is to the unit circle: a useful encoding, not the thing itself.

In differential geometry, the matrix of a linear map is the **direct analogue of the Jacobian** of a smooth map. For a smooth $f : M \to N$ and a point $x \in M$, the total derivative $Df_x : T_x M \to T_{f(x)} N$ is a linear map (see [[Def - The Total Derivative and Differentiability]]); the **Jacobian** $(\partial f_j / \partial x_k)$ is its matrix in the coordinate-induced bases on the tangent spaces. The chain rule in coordinates — "Jacobian of a composition equals the product of Jacobians" — is exactly $\mathcal{M}(S \circ T) = \mathcal{M}(S)\, \mathcal{M}(T)$, transported to derivatives.

In ring theory, the **endomorphism ring** $\mathcal{L}(V)$ is identified, after choosing a basis, with the **matrix ring** $M_n(\mathbf{F}) = \mathbf{F}^{n, n}$ — an isomorphism of [[Def - Ring|rings]] with addition componentwise and multiplication by matrix product. This is the source of the entire subject of matrix algebra, including the theory of [[Def - Polynomial Ring|polynomials]] in a matrix, minimal and characteristic polynomials, and the structure of similar matrices (see [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]]).

In numerical analysis and applied linear algebra, the matrix is the unit of computation — everything is done in coordinates, and the abstract linear map is rarely mentioned. The discipline of remembering "this matrix is the representation of a basis-independent operator, and these properties — eigenvalues, rank, determinant — are intrinsic to the operator, while these other properties — sparsity, entry-by-entry decay — depend on the basis" is what separates good numerical analysts from people who push matrices around.

---

# Examples / Corollaries

**Example: zero map.** The matrix of $T = 0$ in any bases is the $m$-by-$n$ zero matrix.

**Example: identity operator on $V$.** In any basis $v_1, \ldots, v_n$ of $V$ (used as both domain and codomain basis), the matrix of $I : V \to V$ is the $n$-by-$n$ **identity matrix** $I_n$ with $1$'s on the diagonal and $0$'s elsewhere. The $k$-th column is the coordinate vector of $v_k$, which is the standard basis vector $e_k$ in $\mathbf{F}^n$.

**Example: $T : \mathbf{F}^2 \to \mathbf{F}^3$, $T(x, y) = (x + 3y, 2x + 5y, 7x + 9y)$.** Using the standard bases, $T(1, 0) = (1, 2, 7)$ and $T(0, 1) = (3, 5, 9)$, so

$$\mathcal{M}(T) \;=\; \begin{pmatrix} 1 & 3 \\ 2 & 5 \\ 7 & 9 \end{pmatrix}.$$

A $3$-by-$2$ matrix because $T$ goes from a $2$-dimensional space to a $3$-dimensional one. Each column is $T$ applied to a standard basis vector.

**Example: differentiation $D : \mathcal{P}_3(\mathbb{R}) \to \mathcal{P}_2(\mathbb{R})$.** With standard bases $1, x, x^2, x^3$ on the domain and $1, x, x^2$ on the codomain, $D(1) = 0$, $D(x) = 1$, $D(x^2) = 2x$, $D(x^3) = 3x^2$. So

$$\mathcal{M}(D) \;=\; \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{pmatrix}.$$

A $3$-by-$4$ matrix, reflecting $D : \mathcal{P}_3 \to \mathcal{P}_2$ between a $4$-dimensional and a $3$-dimensional space.

**Example: a vector and its matrix.** The matrix of $2 - 7x + 5x^3 + x^4$ in the standard basis of $\mathcal{P}_4(\mathbb{R})$ is

$$\begin{pmatrix} 2 \\ -7 \\ 0 \\ 5 \\ 1 \end{pmatrix}.$$

Each coefficient occupies its corresponding row of the column.

**Example: the central identity in action.** For $T$ as in the $\mathbf{F}^2 \to \mathbf{F}^3$ example, take $v = (4, 1) \in \mathbf{F}^2$. Then $\mathcal{M}(v) = \begin{pmatrix} 4 \\ 1 \end{pmatrix}$, and
$$\mathcal{M}(T)\, \mathcal{M}(v) = \begin{pmatrix} 1 & 3 \\ 2 & 5 \\ 7 & 9 \end{pmatrix} \begin{pmatrix} 4 \\ 1 \end{pmatrix} = \begin{pmatrix} 7 \\ 13 \\ 37 \end{pmatrix}.$$
Indeed $Tv = T(4, 1) = (4 + 3, 8 + 5, 28 + 9) = (7, 13, 37)$, and these are exactly the coordinates of $Tv$ in the standard basis of $\mathbf{F}^3$.

**Example (non-standard bases): a basis-dependent matrix.** For the identity operator on $\mathbf{F}^2$ with domain basis $(4, 2), (5, 3)$ and codomain basis the standard $(1, 0), (0, 1)$: since $I(4, 2) = 4 e_1 + 2 e_2$ and $I(5, 3) = 5 e_1 + 3 e_2$, the matrix is $\begin{pmatrix} 4 & 5 \\ 2 & 3 \end{pmatrix}$. The *same* identity operator has matrix $I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ when the same basis is used on both sides. This makes vivid that "the matrix of $T$" is not a property of $T$ alone.

**Non-example (matrix without a linear map).** A bare matrix $A \in \mathbf{F}^{m, n}$ certainly defines a linear map $T_A : \mathbf{F}^n \to \mathbf{F}^m$, $T_A(x) = Ax$, using the standard basis on each side. But the assignment $A \mapsto T_A$ already implicitly chooses standard bases. With a different basis choice, the same matrix would represent a different map. There is no "the linear map of the matrix $A$" without specifying bases.

**Corollary (the matrix isomorphism).** With bases fixed, $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$ is bijective (every matrix arises from some unique linear map: build $T$ by the linear-map lemma to send $v_k$ to the vector with coordinates equal to column $k$). It is clearly linear: $\mathcal{M}(S + T) = \mathcal{M}(S) + \mathcal{M}(T)$ and $\mathcal{M}(\lambda T) = \lambda \mathcal{M}(T)$, by computing entries directly. Hence $\mathcal{L}(V, W) \cong \mathbf{F}^{m, n}$ via $\mathcal{M}$, and dimension counts give $\dim \mathcal{L}(V, W) = mn$. This is essentially [[Ex - The space of linear maps has dimension mn]].

**Corollary (rank of $T$ equals rank of $\mathcal{M}(T)$).** The dimension of $\operatorname{range} T$ equals the dimension of the column span of $\mathcal{M}(T)$ in $\mathbf{F}^{m, 1}$ — that is, equals the rank of $\mathcal{M}(T)$ — for any choice of bases. This is the bridge between the basis-free notion of [[Def - Rank of a Linear Map|rank of a linear map]] and the matrix-theoretic notion of the rank of a matrix.

**Calibration check.** A reader who has understood the definition should be able to verify, in under a minute each: (1) the matrix of the identity operator in any basis $v_1, \ldots, v_n$ (using the same basis on both sides) is the identity matrix; (2) the matrix of a vector $v$ in a basis $v_1, \ldots, v_n$ is a column of its coordinates; (3) the entry $A_{j, k}$ of $\mathcal{M}(T)$ is read by writing $Tv_k$ as $\sum_j A_{j, k} w_j$ and picking out the $j$-th coefficient.

---

# Unlocked by This

> [!tip] Matrix Multiplication and Composition *(in §3C)*
> The matrix of a composition is the product of the matrices: $\mathcal{M}(ST) = \mathcal{M}(S)\, \mathcal{M}(T)$. This is the reason the [[Def - Matrix Multiplication|definition of matrix multiplication]] looks the way it does — the row-times-column rule is reverse-engineered to make this identity hold. See [[Thm - Composition Corresponds to Matrix Multiplication]].

> [!tip] Change of Basis *(in §3D)*
> The matrix of an operator changes when the basis changes. The transformation rule is $A = C^{-1} B C$ where $C$ is the matrix of the identity operator between the two bases ([[Thm - Change of Basis Formula]]). Two matrices arising as representations of the same operator in different bases are called **similar**, and similarity is the equivalence relation under which most of operator theory is conducted.

> [!tip] The Jacobian and the Chain Rule *(from Multivariate Analysis)*
> For a smooth map between manifolds, the **Jacobian** is the matrix of the [[Def - The Total Derivative and Differentiability|total derivative]] in coordinate-induced bases on tangent spaces. The **chain rule** $D(g \circ f)_x = Dg_{f(x)} \circ Df_x$ in coordinates becomes the matrix identity $J_{g \circ f}(x) = J_g(f(x)) \cdot J_f(x)$ — composition of derivatives is matrix multiplication of Jacobians.

> [!tip] Matrix Ring and Polynomial of an Operator *(from Linear Algebra V)*
> The space $\mathbf{F}^{n, n}$ of square matrices is a [[Def - Ring|ring]] under addition and matrix multiplication. Polynomials in a single matrix $A$ — expressions like $A^3 - 2A + 5I$ — make sense, and the **minimal polynomial** is the lowest-degree monic polynomial annihilating $A$. Cayley–Hamilton, the spectral theorem for normal operators, Jordan canonical form: all are statements about polynomials in matrices. See [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].
