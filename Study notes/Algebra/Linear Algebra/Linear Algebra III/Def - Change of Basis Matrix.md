---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Matrix of a Linear Map"
  - "Def - Invertibility and Isomorphism"
  - "Def - Basis"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over $\mathbf{F}$ with two ordered bases $u_1, \ldots, u_n$ and $v_1, \ldots, v_n$. The **change-of-basis matrix from $u$ to $v$** is denoted $C$ and defined below; it is an element of $\mathbf{F}^{n, n}$. The full notation registry is on [[Linear Algebra III — §3A–D Linear Maps]].

---

# Axiom Motivation

A vector $w \in V$ has different coordinate descriptions in different bases. In the $u$-basis, $w = a_1 u_1 + \cdots + a_n u_n$ has coordinates $(a_1, \ldots, a_n)$; in the $v$-basis, $w = b_1 v_1 + \cdots + b_n v_n$ has coordinates $(b_1, \ldots, b_n)$. The two coordinate columns are different lists of scalars; how are they related?

The relationship must be linear (because change of representation should preserve the linear structure) and invertible (because the relationship is symmetric — we can also go from the $v$-coordinates back to the $u$-coordinates). So there exists an invertible linear map between coordinate columns — equivalently, an invertible matrix — that does the conversion. That matrix is the **change-of-basis matrix**.

Now: in which direction does the matrix go? The convention turns out to be slightly counterintuitive. The change-of-basis matrix $C$ from $u$ to $v$ is *not* the matrix that converts $u$-coordinates to $v$-coordinates. It is the matrix of the identity operator $I : V \to V$ when the **domain** has basis $u$ and the **codomain** has basis $v$ — that is, $C = \mathcal{M}(I, (u_1, \ldots, u_n), (v_1, \ldots, v_n))$. By the definition of the matrix of a linear map, the $k$-th column of $C$ is the coordinate column of $I u_k = u_k$ in the $v$-basis. So **the columns of $C$ list the $v$-coordinates of the $u$-vectors**.

The reason for this convention: under it, the central identity $\mathcal{M}(Tv) = \mathcal{M}(T) \mathcal{M}(v)$ specialises perfectly. Take $T = I$ with $V$-on-the-left having basis $u$, $V$-on-the-right having basis $v$. For any vector $w \in V$, applying the identity gives $\mathcal{M}_v(w) = C \cdot \mathcal{M}_u(w)$, where $\mathcal{M}_u(w)$ and $\mathcal{M}_v(w)$ are the coordinate columns of $w$ in the two bases. So $C$ converts $u$-coordinates to $v$-coordinates by left-multiplication — exactly the action we want.

A further motivation: $C$ being an invertible matrix is forced. Because the identity operator is invertible (its inverse is itself), its matrix in any pair of bases is invertible. The inverse $C^{-1}$ is the change-of-basis matrix in the reverse direction — from $v$ to $u$. So change of basis is naturally a *[[Def - Group|group]]* action: $\operatorname{GL}_n(\mathbf{F})$ acts on coordinate columns, and the change-of-basis matrix is the [[Def - Group|group]] element implementing the relabelling.

A subtler motivation: change of basis is a *passive* transformation. The vectors of $V$ do not move; only their descriptions change. This is in contrast to an *active* transformation, where the vectors are actually moved by a linear map $T \neq I$. The matrix $\mathcal{M}(T, (u))$ describes an active transformation in $u$-coordinates; the matrix $\mathcal{M}(I, (u), (v))$ describes the same identity operator (i.e., no movement) in a passive shift of coordinates. The [[Thm - Change of Basis Formula|change of basis formula]] then says that the matrix of $T$ in the new basis is $C^{-1} B C$: relabel from $u$ to $v$ (apply $C^{-1}$ if we want to go from $v$-coords to $u$-coords, do the actual transformation $B$ in $u$-coords, then relabel back). Wait — let's double-check the direction.

Actually: the [[Thm - Change of Basis Formula|change of basis formula]] reads $A = C^{-1} B C$, where $A = \mathcal{M}(T, (u))$, $B = \mathcal{M}(T, (v))$, and $C = \mathcal{M}(I, (u), (v))$. So $A$ is the matrix of $T$ in the $u$-basis, and $B$ in the $v$-basis. The relationship $A = C^{-1} B C$ says: to get $A$ from $B$, you conjugate by $C$ in the right order. The motivation here is the diagrammatic statement $T = I^{-1} \circ T \circ I$, expanded in matrices using the multiplication theorem. We avoid the conventional ambiguity by writing the matrices explicitly with the bases.

---

# The Definition

Let $V$ be a finite-dimensional vector space over $\mathbf{F}$, and let $u_1, \ldots, u_n$ and $v_1, \ldots, v_n$ be two ordered bases of $V$.

**Change-of-basis matrix.** The **change-of-basis matrix from $u$ to $v$** is the matrix of the identity operator $I_V$ with domain basis $u$ and codomain basis $v$:

$$C \;:=\; \mathcal{M}(I_V,\, (u_1, \ldots, u_n),\, (v_1, \ldots, v_n)) \;\in\; \mathbf{F}^{n, n}.$$

Explicitly, the entries of $C$ are determined by

$$u_k \;=\; C_{1, k}\, v_1 + C_{2, k}\, v_2 + \cdots + C_{n, k}\, v_n \;=\; \sum_{j=1}^{n} C_{j, k}\, v_j$$

for each $k = 1, \ldots, n$. The **$k$-th column of $C$ lists the $v$-coordinates of $u_k$**.

**$C$ is invertible.** Since $I_V$ is invertible, its matrix in any pair of bases is invertible (Theorem 3.82 of LADR). The inverse $C^{-1}$ is the change-of-basis matrix in the reverse direction:

$$C^{-1} \;=\; \mathcal{M}(I_V,\, (v_1, \ldots, v_n),\, (u_1, \ldots, u_n)).$$

**Action on coordinate columns.** For any $w \in V$, denote $\mathcal{M}_u(w)$ and $\mathcal{M}_v(w)$ the coordinate columns of $w$ in the two bases. Then

$$\mathcal{M}_v(w) \;=\; C\, \mathcal{M}_u(w).$$

That is, $C$ left-multiplies $u$-coordinates to produce $v$-coordinates.

**Change-of-basis formula (for operators).** For an operator $T \in \mathcal{L}(V)$ with $A = \mathcal{M}(T, (u))$ and $B = \mathcal{M}(T, (v))$,
$$A \;=\; C^{-1} B C.$$
See [[Thm - Change of Basis Formula]] for the proof and the full statement.

---

# Categorical / Structural Definition

The change-of-basis matrix is, structurally, an **invertible matrix realizing the isomorphism between two bases**. Two ordered bases of $V$ are equivalent ways to identify $V$ with $\mathbf{F}^n$; the change-of-basis matrix is the matrix of the resulting identification map $\mathbf{F}^n \to \mathbf{F}^n$ induced by the change.

Categorically: a basis of $V$ is the same data as an isomorphism $\phi_u : \mathbf{F}^n \xrightarrow{\sim} V$ (sending the $k$-th standard basis vector to $u_k$). Two bases give two such [[Def - Isomorphism|isomorphisms]], $\phi_u$ and $\phi_v$, and the composition $\phi_v^{-1} \circ \phi_u : \mathbf{F}^n \to \mathbf{F}^n$ is an automorphism of $\mathbf{F}^n$, i.e., an element of $\operatorname{GL}_n(\mathbf{F})$. **The matrix of this automorphism is exactly $C^{-1}$**, the change-of-basis matrix from $v$ to $u$ (the columns of $C^{-1}$ list the $u$-coordinates of $v_k$, equivalently, the action of $\phi_v^{-1} \circ \phi_u$ on standard basis vectors). The two conventions for "$C$ goes which way" differ by inverse, and the convention adopted here matches LADR's.

In group-theoretic language, the set of ordered bases of $V$ is a **principal homogeneous space** (a "torsor") for $\operatorname{GL}(V) \cong \operatorname{GL}_n(\mathbf{F})$: the group of invertible operators acts simply-transitively on the set of bases, and the change-of-basis matrix is the unique group element relating two given bases. This is the abstract reason why "the matrix of an operator depends on the basis, but only up to conjugation": conjugation is the action of $\operatorname{GL}_n$ on $M_n$ corresponding to the action on bases.

---

# Relate to Other Fields / Compression

**True name:** "the matrix that converts coordinates in one basis to coordinates in another, by left-multiplication". This is the operational description; the "matrix of the identity in two bases" form is the *definition*, which makes the proof of [[Thm - Change of Basis Formula]] clean, but the *use* is "convert coordinates".

In **differential geometry**, the change-of-basis matrix appears as the **Jacobian of a coordinate change** on a smooth manifold. If $(U, \phi)$ and $(V, \psi)$ are overlapping coordinate charts on a manifold, the **transition map** $\psi \circ \phi^{-1}$ is a diffeomorphism of open subsets of $\mathbb{R}^n$, and its Jacobian at a point is exactly the change-of-basis matrix between the coordinate-induced bases on the tangent space at that point. Tensors transform under change of basis in a prescribed way — the "transformation rule for tensors" is just multiple applications of the change-of-basis matrix.

In **physics**, change of basis is the **change of frame of reference**. The matrix of a Lorentz transformation in special relativity is the change-of-basis matrix between two inertial frames (see [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] for the algebra; [[Special Relativity I — Lorentz Transformations and Minkowski Space]] for the physics). The metric tensor $\eta_{\mu \nu}$ is invariant under Lorentz transformations because the change-of-basis matrices for Lorentz frames preserve it.

In **numerical linear algebra**, the change of basis is the operation of **preconditioning**: a poorly conditioned matrix $A$ becomes well-conditioned after replacing it with $P A P^{-1}$ for a suitable $P$. The choice of preconditioner is the choice of a basis in which the operator has better numerical properties. Iterative methods like conjugate gradient and GMRES exploit this aggressively.

In **representation theory**, a change of basis on the representation space gives an **equivalent representation**: $\rho'(g) = C^{-1} \rho(g) C$. Two representations are isomorphic iff they are related by such a change of basis. The character $\chi_\rho(g) = \operatorname{tr} \rho(g)$ is invariant under change of basis (because trace is similarity-invariant), which is why character theory works.

---

# Examples / Corollaries

**Example: $\mathbf{F}^2$ with non-standard basis.** Let $u_1 = (4, 2)$, $u_2 = (5, 3)$, and $v_1 = (1, 0)$, $v_2 = (0, 1)$ (the standard basis). To find $C = \mathcal{M}(I, (u), (v))$: $u_1 = 4 v_1 + 2 v_2$, $u_2 = 5 v_1 + 3 v_2$. So
$$C \;=\; \begin{pmatrix} 4 & 5 \\ 2 & 3 \end{pmatrix}.$$
To check: a vector $w$ with $u$-coordinates $(a_1, a_2)^T$ is $a_1 u_1 + a_2 u_2 = a_1 (4, 2) + a_2 (5, 3) = (4 a_1 + 5 a_2, 2 a_1 + 3 a_2)$. These are precisely the entries of $C \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}$, the $v$-coordinates (since $v$ is the standard basis).

The inverse:
$$C^{-1} \;=\; \begin{pmatrix} 3/2 & -5/2 \\ -1 & 2 \end{pmatrix}.$$
This is the change-of-basis matrix from the standard basis to the $u$-basis: its columns are the $u$-coordinates of $(1, 0)$ and $(0, 1)$ respectively.

**Example: a rotation of basis in $\mathbb{R}^2$.** Let $u_1 = (1, 0)$, $u_2 = (0, 1)$ (standard), and $v_1 = (\cos\theta, \sin\theta)$, $v_2 = (-\sin\theta, \cos\theta)$ (rotated by $\theta$). To find $C$ from $u$ to $v$: write $u_1, u_2$ in terms of $v_1, v_2$. We have $u_1 = \cos\theta \cdot v_1 - \sin\theta \cdot v_2$ and $u_2 = \sin\theta \cdot v_1 + \cos\theta \cdot v_2$. So
$$C \;=\; \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} = R_{-\theta}.$$
Note: $C$ is the rotation matrix by $-\theta$. The reason is the convention: $C$ goes from $u$-coords to $v$-coords; if $v$ is the rotated-by-$\theta$ basis, the coords-of-the-same-vector get rotated by $-\theta$ to compensate.

**Example: change of basis for a polynomial.** $\mathcal{P}_2(\mathbb{R})$ with $u$-basis $1, x, x^2$ and $v$-basis $1, 1 + x, (1 + x)^2 = 1 + 2x + x^2$. Express each $u$-vector in the $v$-basis: $1 = 1$, so the first column of $C$ is $(1, 0, 0)^T$. $x = (1 + x) - 1 = -1 \cdot 1 + 1 \cdot (1 + x) + 0 \cdot (1 + x)^2$, so the second column is $(-1, 1, 0)^T$. $x^2 = (1 + x)^2 - 2x - 1 - 2 \cdot ((1 + x) - 1) - 1 = 1 - 2 \cdot (1 + x) + 1 \cdot (1 + x)^2$ (verify: $1 - 2 - 2x + 1 + 2x + x^2 = x^2$, yes). So
$$C \;=\; \begin{pmatrix} 1 & -1 & 1 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix}.$$

**Example: identity change of basis.** If $u_k = v_k$ for every $k$, then $C = I_n$, the identity matrix. The identity change of basis does nothing.

**Non-example: a non-square "change of basis".** A change-of-basis matrix is always square ($n$-by-$n$, where $n = \dim V$). One does not "change basis" between spaces of different [[Def - Dimension|dimensions]] — that would be a change between non-isomorphic vector spaces, which is meaningless.

**Corollary (composition of changes of basis).** If $u, v, w$ are three bases of $V$, and $C_{u \to v}$, $C_{v \to w}$ are the corresponding change-of-basis matrices, then $C_{u \to w} = C_{v \to w} \cdot C_{u \to v}$. Proof: $C_{u \to v}$ converts $u$-coords to $v$-coords; $C_{v \to w}$ converts $v$-coords to $w$-coords; the composition converts $u$-coords to $w$-coords. Note the order: matrix multiplication is reverse of "first do, then do", because we left-multiply.

**Corollary (inverse direction).** $C^{-1}_{u \to v} = C_{v \to u}$, i.e., the inverse of the change-of-basis matrix from $u$ to $v$ is the change-of-basis matrix from $v$ to $u$. This follows from $I = C_{v \to u} \cdot C_{u \to v}$ (identity change of basis $u \to v \to u$).

**Corollary (columns are the new basis in old coordinates — alternative convention).** Some authors define the change-of-basis matrix in the opposite direction: the columns of $C'$ list the $u$-coordinates of $v_k$. Then $C' = C^{-1}$, and the conversion rule reads $\mathcal{M}_u(w) = C' \mathcal{M}_v(w)$. Both conventions are in use; the LADR convention (followed here) puts the $v$-coordinates of the $u$-vectors in the columns.

**Calibration check.** A reader who has understood the definition should be able to verify, in under a minute each: (1) the change-of-basis matrix from a basis to itself is the identity; (2) the change-of-basis matrix is always invertible; (3) the change-of-basis matrix from $v$ to $u$ is the inverse of the matrix from $u$ to $v$.

---

# Unlocked by This

> [!tip] Similar Matrices and Operator Theory *(in §3D and beyond)*
> Two matrices $A, B \in \mathbf{F}^{n, n}$ are **similar** if $A = C^{-1} B C$ for some invertible $C$. Similar matrices represent the **same operator** in different bases. Properties of an operator that are basis-free — eigenvalues, characteristic polynomial, minimal polynomial, trace, determinant, rank — are **similarity invariants**. The project of operator theory (eigentheory, diagonalisation, Jordan form) is to find for each similarity class the **simplest representative**. See [[Thm - Change of Basis Formula]] and [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

> [!tip] Coordinate Charts and Manifolds *(from Differential Geometry)*
> A smooth manifold is glued from coordinate charts $\phi : U \to \mathbb{R}^n$; the transition maps between overlapping charts are the **change-of-basis** operations (in tangent spaces, at each point). The structure of the manifold is encoded in how these transition maps interact, and tensors are objects that transform "correctly" under these changes. The matrix calculus you learn here is the local linear approximation of this whole machinery.

> [!tip] Gauge Transformations and Physics *(from Theoretical Physics)*
> A **gauge transformation** in physics is a change of basis in the internal (fibre) coordinates of a vector bundle. Gauge-invariant quantities are similarity-invariants — they do not depend on the basis chosen. The trace and determinant of operators on internal spaces are gauge-invariant; the components of vectors and matrices are not. The principle of gauge invariance — that physical laws should depend only on gauge-invariant quantities — is the basis of modern field theory.

> [!tip] Conjugacy Classes and Group Action *(from Group Theory)*
> The set $M_n(\mathbf{F})$ carries an action of $\operatorname{GL}_n(\mathbf{F})$ by conjugation $A \mapsto C A C^{-1}$. The orbits of this action are the **conjugacy classes** (= similarity classes) of matrices. Parametrising these classes is exactly the problem solved by [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces|Jordan canonical form]] over $\mathbb{C}$ and by **rational canonical form** over $\mathbf{F}$ more generally. The classification of conjugacy classes is one of the deepest problems in linear algebra, and the change-of-basis matrix is the elementary object whose action defines the equivalence relation.
