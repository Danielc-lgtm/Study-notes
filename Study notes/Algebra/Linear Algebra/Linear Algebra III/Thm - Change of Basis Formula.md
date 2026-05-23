---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Matrix of a Linear Map"
  - "Def - Change of Basis Matrix"
  - "Def - Invertibility and Isomorphism"
  - "Thm - Composition Corresponds to Matrix Multiplication"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over $\mathbf{F}$, $T \in \mathcal{L}(V)$ is an operator on $V$, and $u_1, \ldots, u_n$ and $v_1, \ldots, v_n$ are two ordered bases of $V$. The change-of-basis matrix from $u$ to $v$ is $C = \mathcal{M}(I, (u), (v))$; the matrices of $T$ in the two bases are $A = \mathcal{M}(T, (u))$ and $B = \mathcal{M}(T, (v))$. Full notation on [[Linear Algebra III — §3A–D Linear Maps]].

---

# Statement

> **Theorem (Change of Basis Formula).** Let $V$ be finite-dimensional over $\mathbf{F}$, $T \in \mathcal{L}(V)$, and $u_1, \ldots, u_n$ and $v_1, \ldots, v_n$ two bases of $V$. Let $A = \mathcal{M}(T, (u))$ be the matrix of $T$ in the $u$-basis, $B = \mathcal{M}(T, (v))$ the matrix in the $v$-basis, and $C = \mathcal{M}(I, (u), (v))$ the [[Def - Change of Basis Matrix|change-of-basis matrix from $u$ to $v$]]. Then
>
> $$A \;=\; C^{-1}\, B\, C.$$

The relation $A = C^{-1} B C$ for some invertible $C$ is called **similarity**, and the matrices $A, B$ are said to be **similar**. So the theorem says: *the matrices of the same operator in different bases are similar*. The converse is also true: similar matrices represent the same operator, in different bases — see Remark below.

> **Corollary.** Two matrices $A, B \in M_n(\mathbf{F})$ are similar iff they represent the same operator in some pair of bases.

---

# Motivation

The change-of-basis formula is the **bridge** between the basis-free world of operators and the basis-dependent world of matrices. An operator $T \in \mathcal{L}(V)$ is a single mathematical object, but its matrix depends on the basis chosen. Asking "how do these matrices relate when the basis changes" produces the change-of-basis formula, and the answer is "by conjugation". This is the algebraic content of the platonic-vs-representation distinction.

The theorem's importance is not in the computation it enables (which is straightforward matrix multiplication) but in the *equivalence relation* it identifies on matrices. Two matrices $A, B \in M_n(\mathbf{F})$ are **similar** if $A = C^{-1} B C$ for some invertible $C$. This is an equivalence relation, and the equivalence classes — called **similarity classes** or **conjugacy classes** in $\operatorname{GL}_n$ acting on $M_n$ — are precisely the matrices that represent the same operator. So **similarity is the equivalence relation under which all operator-theoretic content is invariant**.

This sets up the entire program of operator theory: classify the similarity classes of matrices, and pick a canonical representative from each class. The simplest representatives reveal the structure of the operator most clearly. The program is:

- **Diagonal representative.** When possible, find a basis in which $T$ has a diagonal matrix; the diagonal entries are the eigenvalues. See [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].
- **Upper-triangular representative.** Over $\mathbb{C}$, every operator has an upper-triangular matrix in some basis (Schur decomposition). See [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].
- **Jordan canonical form.** Over algebraically closed fields, every similarity class has a unique Jordan-form representative — block-diagonal with Jordan blocks. See [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].
- **Rational canonical form.** Over arbitrary fields, every similarity class has a unique rational-canonical-form representative.

Without the change-of-basis formula, these would just be matrix-shape classifications. With it, they become *operator* classifications, applicable to any space with a basis.

A second motivation: the change-of-basis formula explains **why eigenvalues, trace, determinant, and rank are basis-independent**. Each of these is a similarity invariant — preserved under $A \mapsto C^{-1} A C$ — and so is a well-defined property of the operator, not just of one particular matrix representation.

A third motivation: in physics, the change-of-basis formula is the **transformation rule for tensors**. A vector transforms under a change of basis by left-multiplication by $C^{-1}$ (the inverse of the basis-change matrix); an operator (a $(1, 1)$-tensor) transforms by conjugation $C^{-1} \cdot C$; higher-rank tensors transform with more copies of $C$ and $C^{-1}$. The whole formalism of "covariant" and "contravariant" indices, "transforming as a tensor under coordinate changes" — see [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] — generalises the formula.

---

# Sources and Targets

**Sources (Input Broadening)**

**Source: "the matrix of $T$ in basis $u$ is ugly; find a nicer matrix in some other basis $v$".** Direct application. The non-obvious step is choosing the better basis. Common choices: a basis of eigenvectors (giving a diagonal matrix), a basis adapted to an invariant subspace decomposition (giving a block-triangular matrix), the Jordan basis. The reason to do this: the structure of $T$ becomes visible from the simpler matrix.

**Source: "two matrices look different; are they the same operator in different bases?"** Compute their similarity invariants (eigenvalues, characteristic polynomial, minimal polynomial, rank, trace, determinant). If any invariant differs, they are not similar. If all invariants agree, they may or may not be similar; finer tools (Jordan form, rational canonical form) decide. Example: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ have the same eigenvalues, characteristic polynomial, trace, determinant, and rank, but different minimal polynomials — so they are *not* similar.

**Source: "the same operator viewed in coordinates pulls back to a matrix in another set of coordinates".** This is the situation in physics: a tensor (operator, vector, etc.) has different coordinate descriptions in different reference frames, and the change-of-basis formula gives the transformation rule. The non-obvious step is identifying the change of basis as a coordinate transformation.

**Source: "computing the trace, determinant, or eigenvalues of an operator on an abstract space"**. The operator $T$ has these intrinsic invariants, but to compute them one chooses a basis and computes them from the matrix. The change-of-basis formula certifies that the answer does not depend on the basis: $\operatorname{tr}(C^{-1} B C) = \operatorname{tr}(B)$ (trace is conjugation-invariant), $\det(C^{-1} B C) = \det(B)$, and the eigenvalues of $C^{-1} B C$ are the eigenvalues of $B$ (with the same multiplicities). So the matrix-level computations give the operator-level answer.

**Targets (Output Amplification)**

**Combined with the goal "simplify the matrix as much as possible".** The change-of-basis formula sets up the **similarity classification problem**: find a canonical representative of each similarity class. The further results are:
- **Diagonal canonical form** (for diagonalisable operators);
- **Upper-triangular form** (Schur, over $\mathbb{C}$);
- **Jordan canonical form** (over algebraically closed fields);
- **Rational canonical form** (over arbitrary fields).
Each is a deep theorem about operators, made possible by the equivalence relation defined by the change-of-basis formula.

**Combined with the group $\operatorname{GL}_n(\mathbf{F})$ acting by conjugation on $M_n(\mathbf{F})$.** The action $C \cdot A = C A C^{-1}$ (or $C^{-1} A C$, depending on the convention) is a group action of $\operatorname{GL}_n$ on $M_n$. The orbits are exactly the similarity classes. So the change-of-basis formula is the statement that "matrices of the same operator form an orbit of $\operatorname{GL}_n$ acting by conjugation". The further result $E$: counting and characterising the orbits is a major problem in linear algebra, with the Jordan and rational canonical forms providing the orbit classification.

**Combined with eigenvalue computation.** The eigenvalues of $T$ are the same as the eigenvalues of $\mathcal{M}(T)$ in any basis — they are the roots of the characteristic polynomial $\det(xI - \mathcal{M}(T))$, which is a similarity invariant. The further result: eigenvalues are intrinsic to the operator, and any basis choice gives the correct eigenvalues. This is the foundation of spectral theory.

**Combined with the goal "find an invariant subspace decomposition".** If $V = V_1 \oplus V_2$ is an invariant decomposition ($T V_i \subseteq V_i$), then choosing bases of $V_1$ and $V_2$ separately and concatenating gives a basis of $V$ in which $\mathcal{M}(T)$ is block-diagonal. The change-of-basis formula gives the transformation. The further result $E$: block-diagonal form reveals the operator's invariant subspaces, which is the entire content of representation theory.

---

# Why Is It True

The formula is obvious from a diagrammatic argument. The operator $T$ acts on $V$. We have two ways of viewing $V$: with the $u$-basis or with the $v$-basis. The "identity-as-basis-change" $I : V_{(u)} \to V_{(v)}$ converts $u$-coordinates to $v$-coordinates (matrix $C$); its inverse $I : V_{(v)} \to V_{(u)}$ converts $v$-coordinates to $u$-coordinates (matrix $C^{-1}$).

The operator $T$ in the $u$-basis is the composition:
$$T_{(u)} : V_{(u)} \xrightarrow{I} V_{(v)} \xrightarrow{T} V_{(v)} \xrightarrow{I^{-1}} V_{(u)}.$$

That is: convert from $u$ to $v$, apply $T$ in $v$-coordinates, convert back from $v$ to $u$. By [[Thm - Composition Corresponds to Matrix Multiplication|the composition theorem]], the matrix of this composition is the product of the matrices of the three steps:

$$A = \mathcal{M}(I, (v), (u)) \cdot \mathcal{M}(T, (v)) \cdot \mathcal{M}(I, (u), (v)) = C^{-1} \cdot B \cdot C.$$

> **The whole intuition in one sentence: applying $T$ in one basis is the same as converting to another basis, applying $T$ there, and converting back — and the matrix product corresponding to this triple composition is exactly $C^{-1} B C$.**

The non-commutativity of matrix multiplication is what makes the formula a conjugation (rather than a simpler product): the order matters. Sandwiching $B$ between $C$ and $C^{-1}$ correctly tracks "go to $v$-coordinates, do something, return to $u$-coordinates". Conjugation is *the* operation that respects this round-trip-via-another-coordinate-system pattern, and it appears throughout mathematics for exactly this reason.

The reason the same formula works for any pair of bases is that the *role* of the change-of-basis matrix is symmetric in the two bases — $C^{-1}$ converts $v$-coordinates to $u$-coordinates, the reverse direction.

**Remark (the converse).** Two matrices $A, B$ similar via $A = C^{-1} B C$ for some invertible $C \in M_n(\mathbf{F})$ represent the same operator. Specifically: choose a basis $u_1, \ldots, u_n$ of $V$ in which the operator has matrix $B$; let $v_1, \ldots, v_n$ be the new basis whose change-of-basis matrix from $u$ to $v$ is $C^{-1}$ (i.e., the columns of $C^{-1}$ list the $v$-coordinates of $u_k$, so columns of $C$ list the $u$-coordinates of $v_k$). Then the matrix of the operator in the $v$-basis is $A = C B C^{-1}$. (Both directions need careful basis-bookkeeping; the convention in LADR makes $A = C^{-1} B C$ the formula.)

---

# What Makes This Hard

The formula is mechanically easy once one accepts the conventions. The traps are notational:

- **Direction of $C$.** The change-of-basis matrix from $u$ to $v$ has its columns listing the $v$-coordinates of the $u$-vectors. This convention varies across textbooks: some authors define $C$ in the opposite direction, leading to the formula $A = C B C^{-1}$ rather than $A = C^{-1} B C$. The error this produces is a sign/order error throughout the calculation. Stick to one convention and check it.

- **Operator vs. linear map.** The formula $A = C^{-1} B C$ holds for **operators** $T : V \to V$ (using the same basis for domain and codomain). For a linear map $T : V \to W$ between two different spaces with separate bases, the formula has two different change-of-basis matrices: $A = C_2^{-1} B C_1$, where $C_1$ is the change of basis on $V$ and $C_2$ on $W$.

- **Confusion of "matrix" with "operator".** A common error is to ask "what is the eigenvalue of the matrix $A$?" — eigenvalues are properties of the operator (= similarity class), not of one specific matrix in the class. All matrices in a similarity class have the same eigenvalues. The change-of-basis formula is what certifies this.

A subtler trap is **changing the basis on a non-square map**. For $T \in \mathcal{L}(V, W)$ with $V \neq W$, the matrix depends on bases of $V$ and $W$ independently, and there are two separate change-of-basis matrices. The "single-formula" version of the change of basis is only for operators (single space).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Decompose $T = I^{-1} \circ T \circ I$ (the trivial identity in any basis), where $I$ is the identity map between two basis-equipped versions of $V$. Apply the [[Thm - Composition Corresponds to Matrix Multiplication|composition theorem]] to get the matrix as a product of three matrices.

**Subgoal decomposition:**

1. **Write $T$ as a composition involving identities.** $T = I_{V \to V} \circ T \circ I_{V \to V}$, with the identity factors mediating between the $u$-basis and the $v$-basis.

2. **Compute the matrix of each factor in the appropriate basis pair.**
   - Outer identity $I : V_{(v)} \to V_{(u)}$ has matrix $C^{-1}$.
   - Middle $T : V_{(v)} \to V_{(v)}$ has matrix $B$.
   - Inner identity $I : V_{(u)} \to V_{(v)}$ has matrix $C$.

3. **Apply the [[Thm - Composition Corresponds to Matrix Multiplication|composition theorem]].** The matrix of $T : V_{(u)} \to V_{(u)}$ is $C^{-1} \cdot B \cdot C = A$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The matrix of the inverse equals the inverse of the matrix
> **Statement:** If the linear map $T : V \to V$ has matrix $A$ in some pair of bases (same on both sides), then $T^{-1}$ (when invertible) has matrix $A^{-1}$.
>
> **Hint:** $T T^{-1} = I$, so $\mathcal{M}(T) \mathcal{M}(T^{-1}) = \mathcal{M}(I) = I_n$ by the [[Thm - Composition Corresponds to Matrix Multiplication|composition theorem]], so $\mathcal{M}(T^{-1}) = \mathcal{M}(T)^{-1}$.
>
> **Why needed:** Used to show $\mathcal{M}(I, (v), (u)) = C^{-1}$, where $C = \mathcal{M}(I, (u), (v))$.
>
> > [!note]- Full proof
> > $I_V$ has matrix $I_n$ in any basis. By the composition theorem, $\mathcal{M}(T) \mathcal{M}(T^{-1}) = \mathcal{M}(T T^{-1}) = \mathcal{M}(I_V) = I_n$, and similarly $\mathcal{M}(T^{-1}) \mathcal{M}(T) = I_n$. So $\mathcal{M}(T^{-1}) = \mathcal{M}(T)^{-1}$.

> [!note]- Lemma 2: Change-of-basis matrices in opposite directions are inverses
> **Statement:** $\mathcal{M}(I_V, (v), (u)) = (\mathcal{M}(I_V, (u), (v)))^{-1}$, i.e., $C^{-1}$ is the change-of-basis matrix from $v$ to $u$.
>
> **Hint:** Apply Lemma 1 to the identity operator.
>
> **Why needed:** Recognize that $C^{-1}$ in the formula represents a specific change-of-basis matrix.
>
> > [!note]- Full proof
> > By the composition theorem, $\mathcal{M}(I, (v), (u)) \cdot \mathcal{M}(I, (u), (v)) = \mathcal{M}(I \circ I, (u), (u)) = \mathcal{M}(I, (u)) = I_n$. So the two matrices are inverses of each other.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V$ be finite-dimensional, $u_1, \ldots, u_n$ and $v_1, \ldots, v_n$ two bases of $V$, $T \in \mathcal{L}(V)$ an operator, $A = \mathcal{M}(T, (u))$, $B = \mathcal{M}(T, (v))$, and $C = \mathcal{M}(I, (u), (v))$.
>
> **Step 1: Express $T$ as a composition via the identity.**
> The operator $T : V \to V$ (with both copies of $V$ having the $u$-basis) can be written as the composite
> $$V_{(u)} \xrightarrow{\;I\;} V_{(v)} \xrightarrow{\;T\;} V_{(v)} \xrightarrow{\;I\;} V_{(u)},$$
> where each $I$ is the identity on $V$ but viewed as a linear map between different basis equipments. This composition is literally $T$, because three identities surrounding $T$ is still $T$ — only the basis changes mid-composition, but the underlying map is unchanged.
>
> **Step 2: Identify the matrix of each factor.**
> - $\mathcal{M}(I, (u), (v)) = C$ by definition.
> - $\mathcal{M}(T, (v)) = B$ by definition.
> - $\mathcal{M}(I, (v), (u)) = C^{-1}$ by Lemma 2.
>
> **Step 3: Apply the composition theorem.**
> By [[Thm - Composition Corresponds to Matrix Multiplication|the composition theorem]], the matrix of the composition (in the leftmost-domain and rightmost-codomain bases, both $u$ here) is the product of the matrices of the steps:
> $$A = \mathcal{M}(T, (u)) = \mathcal{M}(I, (v), (u)) \cdot \mathcal{M}(T, (v)) \cdot \mathcal{M}(I, (u), (v)) = C^{-1} \cdot B \cdot C.$$
>
> Hence $A = C^{-1} B C$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Diagonalisation as similarity transformation.** Diagonalising a matrix is finding a basis of eigenvectors, equivalently finding $C$ such that $C^{-1} A C$ is diagonal. The diagonal entries are the eigenvalues; the columns of $C$ are the eigenvectors. Diagonalisability is a property of the operator (the similarity class), and the change-of-basis formula is the formal mechanism. The application to numerical computation is enormous: many linear-algebra algorithms compute eigenvalues and eigenvectors precisely because diagonal matrices are trivial to manipulate.

**Spectral theorem in coordinates.** For self-adjoint operators on a real inner-product space, the spectral theorem says there is an orthonormal basis of eigenvectors; the change-of-basis matrix to this basis is *orthogonal* ($C^T = C^{-1}$), and the resulting diagonal form has real eigenvalues. So self-adjoint operators are similar (via *orthogonal* matrices) to real diagonal matrices. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]].

**Coordinate transformations in special relativity.** Lorentz transformations on Minkowski spacetime are changes of basis between inertial frames. A four-vector $x^\mu$ transforms as $x^{\prime\mu} = \Lambda^\mu_\nu x^\nu$ — left-multiplication by the change-of-basis matrix $\Lambda$. A $(1, 1)$-tensor (like an operator) transforms by conjugation $T^{\prime\mu}_\nu = \Lambda^\mu_\alpha (\Lambda^{-1})^\beta_\nu T^\alpha_\beta$, which is the change-of-basis formula in tensor index notation. Invariants under all $\Lambda$ — like the metric $\eta_{\mu\nu}$ — are the "Lorentz invariants" of physics. See [[Special Relativity I — Lorentz Transformations and Minkowski Space]] for the physics; [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] for the general tensor formalism.

**Conjugacy classes in matrix [[Def - Group|groups]].** The conjugacy classes of $\operatorname{GL}_n(\mathbf{F})$ (matrices $A, B$ with $A = C B C^{-1}$ for some $C \in \operatorname{GL}_n$) are exactly the similarity classes of $n$-by-$n$ matrices. Parametrising the conjugacy classes — by Jordan canonical form over $\mathbb{C}$, by rational canonical form over $\mathbf{F}$ — is a classical problem solved by the structure theorem for [[Def - Module|modules]] over a PID. The change-of-basis formula is the elementary statement of the equivalence relation.

**Preconditioning in numerical linear algebra.** When solving $Ax = b$ for an ill-conditioned matrix $A$, one **preconditions**: replace $A$ with $P^{-1} A P$ for an invertible $P$ chosen to make the new matrix well-conditioned. This is exactly a change of basis. The new system $P^{-1} A P y = P^{-1} b$ (with $x = Py$) is easier to solve numerically. Iterative methods (conjugate gradient, GMRES) exploit preconditioning heavily, and the change-of-basis formula is the theoretical foundation.

---

# Bridges

- **[[Def - Change of Basis Matrix]]** — supplies the change-of-basis matrix $C$ appearing in the formula. The columns of $C$ list the $v$-coordinates of the $u$-vectors, by the definition.

- **[[Thm - Composition Corresponds to Matrix Multiplication]]** — supplies the engine of the proof. The change-of-basis formula is three applications of the composition theorem, with the middle term being the operator and the outer terms being basis-change identities.

- **[[Def - Invertibility and Isomorphism]] and $\operatorname{GL}_n(\mathbf{F})$** — supplies the structure on which similarity is defined. The change-of-basis matrix $C$ is invertible (because the identity operator is), so $C \in \operatorname{GL}_n(\mathbf{F})$. The action $C \cdot A = C^{-1} A C$ is a left action of $\operatorname{GL}_n(\mathbf{F})$ on $M_n(\mathbf{F})$, and the orbits are the similarity classes.

- **Similarity invariants (eigenvalues, trace, determinant, characteristic polynomial, minimal polynomial, rank)** — every quantity preserved under $A \mapsto C^{-1} A C$ is a property of the operator, not the matrix. The change-of-basis formula is *why* these are well-defined for the operator. Conversely, properties not preserved (entries of the matrix, sparsity pattern, conditioning) are basis-dependent and not intrinsic.

- **Jordan canonical form** — the classification of similarity classes over algebraically closed fields. Two matrices are similar iff they have the same Jordan form (up to permutation of blocks). The change-of-basis formula sets up the equivalence relation; Jordan form is the canonical representative. See [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

- **Tensor transformation rules (covariance and contravariance)** — the change-of-basis formula for $(1, 1)$-tensors (operators) is $A' = C^{-1} A C$, with one contravariant index transforming with $C^{-1}$ and one covariant with $C$. Higher-rank tensors have multiple copies of each — the general formula generalises this. See [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]].

---

# Unlocked by This

> [!tip] Diagonalisable Operators *(from Linear Algebra V)*
> An operator $T \in \mathcal{L}(V)$ is **diagonalisable** if there exists a basis of eigenvectors of $T$. Equivalently, there exists $C \in \operatorname{GL}_n(\mathbf{F})$ with $C^{-1} \mathcal{M}(T) C$ diagonal — the diagonalisation says the operator is similar to a diagonal matrix. The change-of-basis formula is the formal engine of diagonalisation, and the question "is $T$ diagonalisable" is "is the similarity class of $\mathcal{M}(T)$ that of a diagonal matrix". See [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

> [!tip] Jordan Canonical Form *(from Linear Algebra VIII)*
> Over an algebraically closed field, every operator is similar to a unique (up to block permutation) matrix in **Jordan canonical form**: block-diagonal with Jordan blocks $J_\lambda = \lambda I + N$ (Jordan blocks consisting of $\lambda$ on the diagonal and $1$'s just above). This is the **complete similarity classification** over algebraically closed fields. See [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

> [!tip] Cartan's Theorem and Maximal Torus *(from Lie Theory)*
> For a compact Lie group $G$ (like $\operatorname{U}(n)$), every element is conjugate (similar) to an element of a **maximal torus** — a maximal connected abelian subgroup. The change-of-basis formula in the linear algebra of representations gives this conjugacy, and the Weyl group permutes the maximal-torus elements within the conjugacy class. This is the foundation of representation theory of compact groups (Peter–Weyl, weights, characters).

> [!tip] Frames and Gauge Transformations *(from Physics)*
> A **gauge transformation** in a gauge theory is a change of basis on the internal vector spaces (fibres of a vector bundle) at each point of spacetime, varying smoothly. The change-of-basis formula at each point gives the local transformation rule; the *consistency* of patching different gauge choices is the additional content of gauge theory. Physically observable quantities are gauge-invariant — i.e., similarity-invariant locally and globally.

> [!tip] Conjugation and Inner Automorphisms *(from Group Theory)*
> The change-of-basis formula realises the **inner automorphism** of $\operatorname{GL}_n$ given by conjugation by $C$: $\sigma_C : A \mapsto C^{-1} A C$. The inner automorphism group is $\operatorname{GL}_n / Z(\operatorname{GL}_n)$, where $Z(\operatorname{GL}_n)$ is the centre (scalar multiples of the identity). The fixed-point structure of conjugation (the centraliser of an element) governs much of the group's representation theory.
