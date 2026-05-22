---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Matrix of a Linear Map"
  - "Def - Matrix Multiplication"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $T \in \mathcal{L}(U, V)$ and $S \in \mathcal{L}(V, W)$ are linear maps between finite-dimensional vector spaces, with bases $u_1, \ldots, u_p$ of $U$, $v_1, \ldots, v_n$ of $V$, $w_1, \ldots, w_m$ of $W$ — the same basis of $V$ used in considering both $T$ and $S$. Matrices: $\mathcal{M}(T)$ is the $n$-by-$p$ matrix of $T$ in these bases, $\mathcal{M}(S)$ is the $m$-by-$n$ matrix of $S$, and $\mathcal{M}(ST)$ is the $m$-by-$p$ matrix of the composition. Full notation on [[Linear Algebra III — §3A–D Linear Maps]].

---

# Statement

> **Theorem.** Let $U, V, W$ be finite-dimensional vector spaces with chosen bases, $T \in \mathcal{L}(U, V)$, and $S \in \mathcal{L}(V, W)$. Then
>
> $$\mathcal{M}(ST) \;=\; \mathcal{M}(S)\, \mathcal{M}(T).$$
>
> Here the matrix of $S$ is computed with respect to the bases of $V$ and $W$; the matrix of $T$ with respect to the bases of $U$ and $V$; the matrix of $ST$ with respect to the bases of $U$ and $W$. The same basis of $V$ must be used in both contexts.

The product on the right-hand side is the [[Def - Matrix Multiplication|matrix product]], a $(m \text{-by-} n) \cdot (n \text{-by-} p) = m \text{-by-} p$ matrix.

---

# Motivation

This theorem is the **operational identity** that makes matrix algebra worth studying. It says that the seemingly arbitrary [[Def - Matrix Multiplication|matrix multiplication formula]] $\sum_r A_{j, r} B_{r, k}$ is *precisely* what makes the matrix-of-a-composition equal the product of the matrices. Without this theorem, matrix multiplication would be just one combinatorial operation among many; with it, matrix multiplication is *the* algebraic shadow of composition of linear maps, the central operation of linear algebra.

The motivation for the theorem is, structurally, that [[Def - Matrix Multiplication|matrix multiplication was reverse-engineered to make this identity hold]]. In LADR's treatment, the chain of motivation runs:

1. We want to represent linear maps by matrices.
2. We want representation to respect composition: the matrix of $ST$ should be some computable function of the matrices of $S$ and $T$.
3. Computing the matrix of $ST$ directly — from $(ST)(u_k) = S(T(u_k))$, expanding everything in bases — produces a specific formula involving sums of products of matrix entries.
4. Define matrix multiplication so the formula is exactly the product.

The theorem then becomes almost trivial: matrix multiplication is *by definition* what makes $\mathcal{M}(ST) = \mathcal{M}(S) \mathcal{M}(T)$ hold. The "proof" is "compare the definitions". But this structural circularity is precisely the point: the theorem is the *reason* matrix multiplication exists as a concept.

Once this identity is established, vast amounts of linear algebra collapse to matrix computations. Composition of $k$ linear maps becomes a product of $k$ matrices; the powers of an operator become powers of a matrix; the chain rule of multivariate calculus becomes matrix multiplication of Jacobians; representations of groups become matrices satisfying group relations under multiplication. The entire computational world of linear algebra runs on this identity.

A consequence often overlooked: the theorem implies $\mathcal{L}(V)$ is a [[Def - Ring|ring]] under composition and addition. Matrix multiplication is associative (because composition is), distributes over addition (because composition is bilinear), and has an identity (because the identity matrix corresponds to the identity operator). So once a basis is chosen, $\mathcal{L}(V) \cong M_n(\mathbf{F})$ as rings — the abstract endomorphism ring is identified with the concrete matrix ring.

---

# Sources and Targets

**Sources (Input Broadening)**

**Source: "a composition of linear maps needs to be computed".** The direct application. The non-obvious step is to *recognize when a problem secretly involves a composition* — sometimes a single linear map is really a composition with a hidden intermediate space.

**Source: "the matrix of an inverse map is needed".** If $T$ is invertible, then $TT^{-1} = I$, so $\mathcal{M}(T) \mathcal{M}(T^{-1}) = \mathcal{M}(I) = I_n$. So $\mathcal{M}(T^{-1}) = \mathcal{M}(T)^{-1}$ — the matrix of the inverse is the inverse of the matrix. This is the source of every formula for matrix inverses in computational linear algebra. *Example problem:* compute the matrix of $T^{-1}$ in some basis. The disguised input is that $T \cdot T^{-1} = I$ is a composition.

**Source: "the change-of-basis formula is invoked".** The change-of-basis formula $A = C^{-1} B C$ in [[Thm - Change of Basis Formula]] is *three* compositions: $A = \mathcal{M}(I^{-1} \circ T \circ I)$, with the identities being basis-conversions. Each of the three matrix multiplications is an application of the composition theorem. So the theorem is the engine underlying every basis-change computation.

**Source: "an operator polynomial $p(T)$ is in sight".** A polynomial $p(T) = a_k T^k + a_{k-1} T^{k-1} + \cdots + a_0 I$ in an operator $T$ is a sum of compositions. By the composition theorem and linearity of $\mathcal{M}$, $\mathcal{M}(p(T)) = p(\mathcal{M}(T))$ — the matrix of $p(T)$ is the same polynomial in the matrix of $T$. This is the bridge between *operator polynomials* and *matrix polynomials*, which is the language of the [[Linear Algebra V — §4–5 Polynomials and Eigenvalues|minimal polynomial]] and Cayley–Hamilton.

**Targets (Output Amplification)**

**Combined with the invertibility theorem.** $T$ invertible iff $\mathcal{M}(T)$ invertible, with $\mathcal{M}(T^{-1}) = \mathcal{M}(T)^{-1}$. So in coordinates, finding the inverse of an operator is *exactly* finding the inverse of a matrix, by Gauss–Jordan elimination, Cramer's rule, etc. The further result $E$: operator invertibility is computable, with explicit algorithms.

**Combined with the row-times-column structure.** The matrix-vector identity $\mathcal{M}(Tv) = \mathcal{M}(T) \mathcal{M}(v)$ (which is itself a special case of the composition theorem, applied to $T : V \to W$ and the implicit map $\mathbf{F} \to V$, $\lambda \mapsto \lambda v$) gives the *evaluation* of a linear map on a vector as matrix-vector multiplication. The further result: linear-system solving $Ax = b$ becomes the central computational problem, and Gauss elimination, $LU$ factorisation, and iterative methods are tools for it.

**Combined with non-commutativity.** Matrix multiplication is non-commutative because composition of linear maps is non-commutative. The further result $E$: the *commutator* $[A, B] = AB - BA$ of two matrices measures the failure of $S, T$ to commute, and its structure governs the **Lie algebra** of $\operatorname{GL}_n$ — the infinitesimal version of the matrix group. Quantum-mechanical observables are non-commuting operators, and their commutators (e.g., $[x, p] = i\hbar$ for position and momentum) encode physical content.

**Combined with the action on coordinate vectors.** For $A \in \mathbf{F}^{m, n}$ and $x \in \mathbf{F}^n$, $(Ax)_j = \sum_k A_{j, k} x_k$. The composition theorem gives that applying $A$ to $x$ "by hand" — multiplying each entry of $x$ against the corresponding column of $A$ and summing — produces the correct linear combination, equivalent to "applying $T_A$ to the vector with coordinates $x$". The further result: every linear map $\mathbf{F}^n \to \mathbf{F}^m$ is given by a matrix, and the matrix is the only datum needed (LADR Exercise 16 of §3D).

---

# Why Is It True

The theorem is "true" because matrix multiplication was *defined* to make it true. But this circular justification hides a real computation, and the computation is the actual content.

Let $A = \mathcal{M}(S)$ and $B = \mathcal{M}(T)$. So $S v_r = \sum_j A_{j, r} w_j$ and $T u_k = \sum_r B_{r, k} v_r$. Compute $(ST)(u_k)$ directly:
$$(ST)(u_k) = S(T(u_k)) = S\!\left(\sum_r B_{r, k} v_r\right) = \sum_r B_{r, k}\, S v_r = \sum_r B_{r, k} \sum_j A_{j, r} w_j = \sum_j \left(\sum_r A_{j, r} B_{r, k}\right) w_j.$$

The coefficient of $w_j$ in $(ST)(u_k)$ — which is, by definition of the matrix of a linear map, the $(j, k)$-entry of $\mathcal{M}(ST)$ — equals $\sum_r A_{j, r} B_{r, k}$. This is the $(j, k)$-entry of the matrix product $AB$ by definition of matrix multiplication. So $\mathcal{M}(ST) = AB = \mathcal{M}(S) \mathcal{M}(T)$.

> **The whole proof in one sentence: compute the matrix of $ST$ entry-by-entry from the definitions, and observe that the formula matches matrix multiplication.**

The reason this works is the **double linearity**. The linear map $S$ is linear in its input, so $S(\sum B_{r, k} v_r) = \sum B_{r, k} S v_r$ (homogeneity and additivity together). Then $S v_r$ is expanded in the $w$-basis using the $A$-matrix. The double sum that emerges is exactly the matrix product, because matrix multiplication is "summing over the inner index" — the same index $r$ that connects the input-side of $S$ to the output-side of $T$.

A more abstract reading: matrix multiplication is the **composition operation in the category $\operatorname{Mat}_\mathbf{F}$** of matrices, and the assignment $T \mapsto \mathcal{M}(T)$ (with bases fixed) is a *functor* from finite-dimensional-vector-spaces-with-bases to matrices. Functors preserve composition, by definition. So the theorem is the functoriality statement of this assignment.

---

# What Makes This Hard

The theorem itself is easy — the computation is direct. The trap is that the theorem only holds when **the same basis of $V$ is used in both contexts**: when computing $\mathcal{M}(T)$ (which uses bases of $U$ and $V$) and when computing $\mathcal{M}(S)$ (which uses bases of $V$ and $W$), the basis of $V$ must agree. If a different basis of $V$ is used for $S$ versus for $T$, the identity becomes $\mathcal{M}(ST) = \mathcal{M}(S) C \mathcal{M}(T)$ where $C$ is the change-of-basis matrix between the two $V$-bases, *not* the simple product.

A second subtle point is the **order**: $S$ comes first in $\mathcal{M}(S) \mathcal{M}(T)$ because $S$ is applied *after* $T$. This matches function composition $(S \circ T)(u) = S(T(u))$, but it can be confusing when written without the $\circ$. The trap is to multiply matrices in the wrong order.

A third subtle point is that the theorem is the *reason* matrix multiplication is non-commutative. Beginners sometimes find it strange that $AB \neq BA$; the resolution is that composition $ST \neq TS$ in general, and matrices inherit this. The non-commutativity is not a bug of matrix multiplication; it is a faithful encoding of the non-commutativity of operator composition.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Compute $(ST)(u_k)$ for each basis vector $u_k$ of $U$ by chasing the definitions of $\mathcal{M}(T)$ and $\mathcal{M}(S)$. The double application of "expand in basis using matrix entries" produces a double sum that is exactly matrix multiplication.

**Subgoal decomposition:**

1. **Write down $T u_k$ using $\mathcal{M}(T)$.** $T u_k = \sum_r B_{r, k} v_r$, where $B = \mathcal{M}(T)$.
   - *Hint:* By definition of the matrix of a linear map, the $k$-th column of $B$ is the coordinate column of $T u_k$ in the $v$-basis.
   - *Why needed:* Need to start from the definitions of the matrices.

2. **Apply $S$ using linearity.** $S(T u_k) = S(\sum_r B_{r, k} v_r) = \sum_r B_{r, k} S v_r$ by linearity of $S$.

3. **Expand $S v_r$ using $\mathcal{M}(S)$.** $S v_r = \sum_j A_{j, r} w_j$, where $A = \mathcal{M}(S)$.

4. **Substitute and rearrange.** $(ST)(u_k) = \sum_r B_{r, k} \sum_j A_{j, r} w_j = \sum_j (\sum_r A_{j, r} B_{r, k}) w_j$. The coefficient of $w_j$ is $(AB)_{j, k}$ by the definition of matrix multiplication.

5. **Conclude.** This is the $(j, k)$-entry of $\mathcal{M}(ST)$ by the matrix-of-a-linear-map definition. So $\mathcal{M}(ST)_{j, k} = (AB)_{j, k} = (\mathcal{M}(S) \mathcal{M}(T))_{j, k}$ for all $j, k$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The matrix of a linear map encodes images of basis vectors
> **Statement:** If $T \in \mathcal{L}(U, V)$ with bases $u_1, \ldots, u_p$ of $U$ and $v_1, \ldots, v_n$ of $V$, then $\mathcal{M}(T)_{r, k}$ is defined by $T u_k = \sum_r B_{r, k} v_r$ with $B = \mathcal{M}(T)$.
>
> **Hint:** This is the definition of the matrix of a linear map — see [[Def - Matrix of a Linear Map]].
>
> **Why needed:** This is the starting equation for the calculation.
>
> > [!note]- Full proof
> > By definition, $\mathcal{M}(T) = B$ is the $n$-by-$p$ matrix whose $k$-th column is the coordinate column of $T u_k$ in the $v$-basis: $T u_k = B_{1, k} v_1 + B_{2, k} v_2 + \cdots + B_{n, k} v_n = \sum_r B_{r, k} v_r$.

> [!note]- Lemma 2: Matrix multiplication entry formula
> **Statement:** For $A \in \mathbf{F}^{m, n}$ and $B \in \mathbf{F}^{n, p}$, $(AB)_{j, k} = \sum_r A_{j, r} B_{r, k}$.
>
> **Hint:** This is the definition of matrix multiplication — see [[Def - Matrix Multiplication]].
>
> **Why needed:** This is the formula that the computed double sum matches.
>
> > [!note]- Full proof
> > By definition of [[Def - Matrix Multiplication|matrix multiplication]], the $(j, k)$-entry of $AB$ is the inner product of row $j$ of $A$ with column $k$ of $B$, i.e., $\sum_r A_{j, r} B_{r, k}$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $T \in \mathcal{L}(U, V)$ and $S \in \mathcal{L}(V, W)$, with bases $u_1, \ldots, u_p$ of $U$, $v_1, \ldots, v_n$ of $V$, $w_1, \ldots, w_m$ of $W$. Denote $A = \mathcal{M}(S)$ (so $S v_r = \sum_j A_{j, r} w_j$) and $B = \mathcal{M}(T)$ (so $T u_k = \sum_r B_{r, k} v_r$). We compute the matrix of $ST$.
>
> By Lemma 1 applied to $T$ and to $S$, for each $k = 1, \ldots, p$:
> $$T u_k = \sum_{r=1}^n B_{r, k} v_r.$$
>
> Apply $S$, using linearity:
> $$S(T u_k) = S\!\left(\sum_{r=1}^n B_{r, k} v_r\right) = \sum_{r=1}^n B_{r, k}\, S v_r.$$
>
> Substitute the expansion of $S v_r$:
> $$S(T u_k) = \sum_{r=1}^n B_{r, k} \sum_{j=1}^m A_{j, r} w_j = \sum_{j=1}^m \left(\sum_{r=1}^n A_{j, r} B_{r, k}\right) w_j.$$
>
> The coefficient of $w_j$ in $(ST)(u_k)$ is $\sum_r A_{j, r} B_{r, k}$. By the definition of $\mathcal{M}(ST)$, this coefficient is precisely the $(j, k)$-entry of $\mathcal{M}(ST)$. By Lemma 2, the same sum is the $(j, k)$-entry of the matrix product $AB = \mathcal{M}(S) \mathcal{M}(T)$.
>
> Therefore $\mathcal{M}(ST)_{j, k} = (\mathcal{M}(S) \mathcal{M}(T))_{j, k}$ for all $j = 1, \ldots, m$, $k = 1, \ldots, p$, i.e., $\mathcal{M}(ST) = \mathcal{M}(S) \mathcal{M}(T)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The chain rule in coordinates.** For smooth maps $f : \mathbb{R}^n \to \mathbb{R}^m$ and $g : \mathbb{R}^m \to \mathbb{R}^k$, the [[Def - The Total Derivative and Differentiability|total derivative]] of $g \circ f$ at a point $x$ is $D(g \circ f)_x = Dg_{f(x)} \circ Df_x$. In coordinates, $D(g \circ f)_x$ is the **Jacobian matrix** of $g \circ f$ at $x$, and the chain rule reads $J_{g \circ f}(x) = J_g(f(x)) \cdot J_f(x)$ — matrix multiplication of Jacobians. This is the composition theorem applied to derivatives, and it is the foundation of all of multivariable calculus, from constrained optimisation to the geometry of manifolds.

**Markov chain transition matrices.** A Markov chain with $n$ states has a **transition matrix** $P \in \mathbb{R}^{n, n}$ with $P_{j, k}$ the probability of going from state $j$ to state $k$ in one step (using the row-stochastic convention). The probability of going from state $j$ to state $k$ in exactly two steps is $\sum_r P_{j, r} P_{r, k}$, which is the $(j, k)$-entry of $P^2$. More generally, the $k$-step transition probabilities are the entries of $P^k$. Composition of "one-step transitions" is matrix multiplication of transition matrices, and the long-run behaviour is governed by the eigenvalues of $P$. The composition theorem is the basic principle.

**Convolution as matrix multiplication.** Convolution of two finite sequences $(a_0, \ldots, a_n)$ and $(b_0, \ldots, b_m)$ produces a sequence of length $n + m + 1$ via $(a * b)_k = \sum_j a_j b_{k - j}$. This is matrix-vector multiplication, where the convolution matrix is a banded **Toeplitz matrix**. Composition of linear filters in signal processing is multiplication of their Toeplitz matrices — a direct application of the composition theorem in a different language.

**Group representations as matrix-valued functions.** A representation $\rho : G \to \operatorname{GL}(V)$ assigns to each $g \in G$ an invertible linear map $\rho(g)$. The homomorphism condition $\rho(g_1 g_2) = \rho(g_1) \rho(g_2)$, expressed in matrices, becomes $\mathcal{M}(\rho(g_1 g_2)) = \mathcal{M}(\rho(g_1)) \cdot \mathcal{M}(\rho(g_2))$ — matrix multiplication. So a matrix representation of $G$ is exactly a function $G \to \operatorname{GL}_n(\mathbf{F})$ that turns group multiplication into matrix multiplication. The composition theorem makes this identification possible.

**Quantum mechanics: composition of time evolutions.** A quantum state $|\psi\rangle$ evolves over time via a unitary operator $U(t)$: $|\psi(t)\rangle = U(t) |\psi(0)\rangle$. Composing time evolutions over intervals $t_1$ and $t_2$ gives $U(t_1 + t_2) = U(t_1) U(t_2)$ — operator (matrix) multiplication, by the composition theorem. The Hamiltonian $H$ generates the evolution via $U(t) = e^{-iHt/\hbar}$, and properties of the dynamics (energy conservation, periodicity, etc.) are read off from the composition of these matrices.

---

# Bridges

- **[[Def - Matrix Multiplication]]** — the theorem is the reason the matrix product is defined the way it is. The row-times-column formula is the *operational definition* derived from the demand that $\mathcal{M}(ST) = \mathcal{M}(S) \mathcal{M}(T)$.

- **[[Def - The Total Derivative and Differentiability]] and the chain rule** — the composition theorem applied to derivatives is the chain rule. The total derivative of a composition is the composition of total derivatives, and in coordinates this is matrix multiplication of Jacobians. The chain rule is, structurally, "linearise both, compose the linearisations".

- **[[Thm - Change of Basis Formula]]** — the change of basis $A = C^{-1} B C$ is three applications of the composition theorem, with one of the matrices being a basis-change identity. The matrix algebra of changes of basis runs on composition.

- **[[Def - Ring|Ring structure on $\mathcal{L}(V)$]]** — the composition theorem makes $\mathcal{L}(V)$ a ring (associative, distributive, with identity). Choosing a basis of $V$ identifies this ring with the matrix ring $M_n(\mathbf{F})$. The minimal polynomial of an operator (see [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]]) is a fact about this ring structure.

- **The functor $\mathcal{M}$ from $\mathbf{Vect}_\mathbf{F}^{\mathrm{fin}, \mathrm{basis}}$ to $\operatorname{Mat}_\mathbf{F}$** — the composition theorem is the **functoriality** of the matrix-representation assignment. The same identity holds in any algebraic structure where one represents abstract objects by concrete coordinate data: composition of abstract morphisms corresponds to composition (multiplication) of concrete representations.

---

# Unlocked by This

> [!tip] Matrix Group $\operatorname{GL}_n(\mathbf{F})$ as a Lie Group *(from Lie Theory)*
> The set of invertible matrices forms a group under multiplication, with the composition theorem providing the multiplication. Over $\mathbb{R}$ or $\mathbb{C}$, this is also a smooth manifold (an open subset of the matrix space, the matrices with nonzero determinant), making it a **Lie group** — the prototypical matrix Lie group. The classical matrix Lie groups — $\operatorname{SL}_n, \operatorname{O}(n), \operatorname{U}(n), \operatorname{Sp}_n$ — are subgroups preserving extra structure.

> [!tip] Cayley–Hamilton and the Minimal Polynomial *(from Linear Algebra V)*
> The composition theorem makes powers of an operator equivalent to powers of a matrix: $\mathcal{M}(T^k) = \mathcal{M}(T)^k$. Polynomials in an operator are polynomials in its matrix, and the **minimal polynomial** of $T$ is the lowest-degree monic polynomial $p$ with $p(\mathcal{M}(T)) = 0$. **Cayley–Hamilton** says the characteristic polynomial annihilates the matrix — every matrix satisfies its own characteristic polynomial. See [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

> [!tip] Operator Exponential and Matrix Lie Algebras *(from Lie Theory)*
> The matrix exponential $e^A = \sum_{k \geq 0} \frac{A^k}{k!}$ is defined for any square matrix; the composition theorem makes the powers $A^k$ well-defined as matrix products. The exponential maps the Lie algebra (the tangent space at the identity of a matrix Lie group) to the Lie group itself, via $A \mapsto e^A$. For instance, the Lie algebra of $\operatorname{SO}(n)$ is the antisymmetric matrices, and exponentiating gives the rotations. The non-commutativity of matrix multiplication produces the **Baker–Campbell–Hausdorff formula** for $e^A e^B$ in terms of commutators.

> [!tip] Tensor Networks and Diagrammatic Algebra *(from Modern Mathematical Physics)*
> Matrix multiplication is the simplest case of **tensor contraction**, which generalises to higher-rank tensors. A **tensor network** is a graphical representation of compositions of multi-index linear maps, with edges representing contractions. The composition theorem is the rule for evaluating tensor networks: contracting an internal edge corresponds to summing over the index. Tensor networks underlie modern approaches to quantum many-body systems, gauge theory, and topological quantum field theory.
