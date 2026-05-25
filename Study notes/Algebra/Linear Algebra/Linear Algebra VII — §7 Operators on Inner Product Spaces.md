---
type: topic
subject: linear-algebra
chapter: "7A-7F"
title: "Linear Algebra VII — Operators on Inner Product Spaces"
tags: [algebra, linear-algebra]
---

# Notation Registry

Throughout this topic $V$ and $W$ are finite-dimensional [[Def - Inner Product Space|inner product spaces]] over $\mathbb{F}$, where $\mathbb{F}$ is either $\mathbb{R}$ or $\mathbb{C}$. The complex case is the typical case — most of the genuinely powerful theorems (the complex spectral theorem, the existence of singular value decomposition for arbitrary linear maps) require complex scalars or careful self-adjoint hypotheses to survive on the reals. We write $\mathcal{L}(V, W)$ for the space of linear maps $V \to W$ and $\mathcal{L}(V)$ for the operators $V \to V$.

> [!warning] Convention: the inner product is linear in the *first* slot.
> This is Axler's convention: $\langle \alpha v + w, u \rangle = \alpha \langle v, u \rangle + \langle w, u \rangle$, and $\langle v, w \rangle = \overline{\langle w, v \rangle}$. Many physics texts and parts of functional analysis use the opposite convention (linear in the second slot). To convert, swap arguments and complex-conjugate. Under Axler's convention the defining relation of the adjoint is $\langle Tv, w \rangle_W = \langle v, T^* w \rangle_V$.

- $V, W, U$ — finite-dimensional inner product spaces over $\mathbb{F}$
- $\mathbb{F}$ — either $\mathbb{R}$ or $\mathbb{C}$
- $\langle v, w \rangle$ — the inner product; $\|v\| = \sqrt{\langle v, v \rangle}$ — the induced norm
- $\mathcal{L}(V, W)$ — linear maps $V \to W$; $\mathcal{L}(V) = \mathcal{L}(V, V)$ — operators on $V$
- $T^*$ — the [[Def - Adjoint of a Linear Map|adjoint]] of $T$
- $A^*$ — the conjugate transpose of a matrix $A$: $(A^*)_{jk} = \overline{A_{kj}}$
- $I$ or $I_V$ — the identity operator
- $\operatorname{null} T$, $\operatorname{range} T$ — the [[Def - Null Space and Range|null space (kernel) and range (image)]] of $T$
- $U^{\perp}$ — the orthogonal complement of $U \subseteq V$
- $P_U$ — the [[Def - Orthogonal Projection|orthogonal projection]] onto a subspace $U \leq V$
- $\sigma_j(T)$ or $s_j(T)$ — the singular values of $T$, listed in decreasing order
- $\sqrt{T}$ — the unique positive square root of a [[Def - Positive Operator|positive operator]] $T$
- $|T| = \sqrt{T^* T}$ — the "absolute value" of $T$ (a positive operator on $V$)
- $\operatorname{GL}(V)$, $U(V)$, $O(V)$, $\operatorname{SO}(V)$ — the general linear group, unitary group, orthogonal group, special orthogonal group on $V$
- $\operatorname{diag}(\lambda_1, \ldots, \lambda_n)$ — the diagonal matrix with the listed entries

A standing convention worth flagging: an *operator* always means a linear map $V \to V$ (same domain and codomain). The adjoint of an operator is an operator; the adjoint of a general linear map $V \to W$ lives in $\mathcal{L}(W, V)$.

---

# Motivation

Here is the entire chapter in one sentence: **a normal operator on a complex inner product space has an orthonormal basis of eigenvectors**, and every other theorem in this chapter is a refinement, a corollary, or a reorganisation of that single fact. The chapter begins with the language needed to *state* the theorem — adjoints, self-adjoint, normal — and ends with the consequences of *applying* it in different ways — to $T$ itself (the spectral theorems), to $T^* T$ (the singular value decomposition), and to the resulting square root and partial [[Def - Isometry|isometry]] (the polar decomposition).

The hierarchy is short enough to display:

$$\text{unitary} \;\;\subset\;\; \text{normal with } |\lambda| = 1 \quad \text{and} \quad \text{self-adjoint} \;\;\subset\;\; \text{normal with } \lambda \in \mathbb{R} \quad \text{and} \quad \text{positive} \;\;\subset\;\; \text{self-adjoint with } \lambda \geq 0$$

Every class lives inside *normal*. Once you have the [[Thm - Complex Spectral Theorem|complex spectral theorem]] — every normal $T$ on a complex inner product space is diagonalised by an orthonormal basis — each of these classes is just "normal plus a condition on the eigenvalues". Self-adjoint operators are the ones whose eigenvalues are all real. Positive operators are the self-adjoint operators whose eigenvalues are non-negative; they are the "non-negative numbers" of the operator world, with the same square-root structure. [[Def - Unitary Operator|Unitary operators]] are the normal operators with eigenvalues on the unit circle, the operator analogue of complex numbers of modulus one.

The unifying frame extends to factorisations. **Singular value decomposition** is the [[Thm - Real Spectral Theorem|spectral theorem]] applied to the positive operator $T^* T$ — every eigenvalue of $T^*T$ is the square of a *singular value* of $T$, and the eigenvector orthonormal basis is precisely the right-singular basis of $T$. **Polar decomposition** is then SVD reorganised: every operator factors as an isometry times a positive operator, the operator analogue of $z = r\,e^{i\theta}$. **QR factorisation** is [[Thm - Gram-Schmidt Procedure|Gram–Schmidt]] applied to the columns of $T$. **Cholesky factorisation** is the operator square root applied to a positive operator. The whole chapter is one theorem and its rephrasings.

A warning that will recur: the *real* [[Thm - Real Spectral Theorem|spectral theorem]] applies only to self-adjoint operators, not to all normal operators. A rotation of $\mathbb{R}^2$ by $90^\circ$ is normal — it commutes with its transpose — but has no real eigenvectors at all. Over $\mathbb{R}$, normality is too weak; one needs the self-adjointness condition, which forces the (complex) eigenvalues to be real and lets them descend to the real space. Over $\mathbb{C}$ no such restriction is needed: normality alone suffices, because complex eigenvalues are always available.

This topic assumes [[Linear Algebra VI — §6 Inner Product Spaces]] — inner products, norms, orthonormal bases, [[Thm - Gram-Schmidt Procedure|Gram–Schmidt]], orthogonal complements and projections, and the finite-dimensional [[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz representation theorem]] — together with [[Linear Algebra V — §4–5 Polynomials and Eigenvalues|Linear Algebra V]] for eigenvalues, the minimal polynomial, and upper-triangular form. The reader who has refreshed those two topics will find the present chapter mostly an exercise in routing assumptions to the spectral theorem and reading off the consequences.

---

# Concept Map

## §7A Self-Adjoint and Normal Operators

- **[[Def - Adjoint of a Linear Map]]**
	- For $T \in \mathcal{L}(V, W)$, the **adjoint** $T^* \in \mathcal{L}(W, V)$ is the unique linear map satisfying $\langle Tv, w \rangle_W = \langle v, T^* w \rangle_V$ for all $v \in V$, $w \in W$. Existence and uniqueness come from the [[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz representation theorem]] applied to the linear functional $v \mapsto \langle Tv, w \rangle$. With respect to orthonormal bases the matrix of $T^*$ is the conjugate transpose of the matrix of $T$. Over $\mathbb{R}$ this is the transpose; over $\mathbb{C}$ it is the conjugate transpose. The adjoint is the inner-product analogue of the [[Def - Dual Map|dual map]] from [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

- **[[Thm - Properties of the Adjoint]]**
	- Adjoint is conjugate-linear in $T$, reverses composition $(ST)^* = T^* S^*$, satisfies $T^{**} = T$, $I^* = I$, and ties up null spaces and ranges via $\operatorname{null} T^* = (\operatorname{range} T)^{\perp}$ and $\operatorname{range} T^* = (\operatorname{null} T)^{\perp}$. These rules let you compute with adjoints symbolically, and the null-space/range identities are the bridge between the "primal" and "adjoint" worlds. They are the inner-product analogue of the corresponding [[Thm - Null Space and Range of Dual Map|theorem on dual maps]].

- **[[Def - Self-Adjoint Operator]]**
	- An operator $T \in \mathcal{L}(V)$ is **self-adjoint** (also called **Hermitian**, or **symmetric** when $\mathbb{F} = \mathbb{R}$) if $T = T^*$, equivalently $\langle Tv, w \rangle = \langle v, Tw \rangle$ for all $v, w \in V$. The matrix of $T$ in any orthonormal basis equals its own conjugate transpose. Self-adjoint operators are the "real numbers" of the operator world: their eigenvalues are real, and over $\mathbb{C}$ a self-adjoint operator is diagonalised by an orthonormal eigenbasis. The Hamiltonian and momentum operators of quantum mechanics are self-adjoint by axiom.

- **[[Def - Normal Operator]]**
	- An operator $T \in \mathcal{L}(V)$ is **normal** if $T T^* = T^* T$ — it commutes with its adjoint. Equivalently $\|Tv\| = \|T^*v\|$ for all $v$. Every self-adjoint, unitary, and positive operator is normal, and these classes are exactly the normal operators with eigenvalues respectively real, on the unit circle, and non-negative. The "true name" of normality is the commuting characterisation; the norm-equality characterisation is what one verifies in practice.

- **[[Thm - Normal Operators Commute with Their Adjoint]]**
	- For an operator $T$ on a complex inner product space, the following are equivalent: (i) $T$ is normal; (ii) $\|Tv\| = \|T^* v\|$ for all $v$; (iii) $T$ and $T^*$ have the same eigenvectors, with $T v = \lambda v$ iff $T^* v = \overline{\lambda} v$; (iv) eigenvectors of $T$ for distinct eigenvalues are orthogonal. Each equivalence opens a different door to the spectral theorem: (ii) is what one checks in practice, (iii) is what makes the eigenvalue analysis go through, and (iv) is the crucial step in the inductive proof.

- **[[Ex - Adjoint of differentiation is negative differentiation with boundary conditions]]** (⭐⭐)
	- On the space of differentiable functions on $[0,1]$ with the $L^2$ inner product, compute the adjoint of $\frac{d}{dx}$ and watch boundary conditions emerge from integration by parts.

- **[[Ex - Self-adjoint operators have real eigenvalues]]** (⭐)
	- Use $\langle Tv, v \rangle = \langle v, Tv \rangle$ together with the conjugate-linearity of the inner product to force $\lambda = \overline{\lambda}$. The single calculation that explains the "self-adjoint = real" analogy.

- **[[Ex - Eigenvectors of a normal operator with distinct eigenvalues are orthogonal]]** (⭐⭐)
	- The eigenvector pairing trick: if $Tv = \lambda v$ and $Tw = \mu w$ with $\lambda \neq \mu$, then $\lambda \langle v, w \rangle = \mu \langle v, w \rangle$, forcing $\langle v, w \rangle = 0$. The orthogonality that powers the spectral theorem.

> [!tip] Unlocked: [[Def - Lie Algebra|Lie Algebra]] *(from Differential Geometry / Lie Theory)*
> The space of skew-Hermitian operators $\{T : T^* = -T\}$ on $\mathbb{C}^n$ is the **Lie algebra $\mathfrak{u}(n)$** of the unitary group $U(n)$ — its elements are the "infinitesimal unitaries", and $\exp$ maps them into $U(n)$. The corresponding real version, anti-symmetric matrices $T^t = -T$, is $\mathfrak{so}(n)$, the Lie algebra of the rotation group. The decomposition of a complex matrix into self-adjoint and skew-adjoint parts is the linearisation, at the identity, of the polar decomposition.

> [!tip] Unlocked: Adjoint Functor *(from Category Theory)*
> The relation $\langle Tv, w \rangle = \langle v, T^* w \rangle$ has the shape of an adjunction between hom-sets: a morphism $V \to W$ corresponds to a morphism $W \to V$ via the inner product pairing. The categorical name for this is a **dagger structure** on the category of finite-dimensional Hilbert spaces — the operation $T \mapsto T^*$ is the dagger, and self-adjoint, unitary, and positive operators are all defined by relations involving the dagger.

> [!note] Exercise Index — §7A
> [[Exercise Index - §7A Self-Adjoint and Normal Operators]]

## §7B Spectral Theorem

- **[[Thm - Complex Spectral Theorem]]**
	- An operator $T$ on a complex finite-dimensional inner product space $V$ is normal if and only if $V$ has an orthonormal basis of eigenvectors of $T$. Equivalently, the matrix of $T$ in some orthonormal basis is diagonal. This is the headline theorem of the chapter: it says normal operators are precisely the operators that diagonalise in some orthonormal basis, no information lost beyond the eigenvalues. The unitary $U$ that diagonalises $T$ (in matrix form $T = U D U^*$) is the change-of-basis matrix into the eigenbasis.

- **[[Thm - Real Spectral Theorem]]**
	- An operator $T$ on a real finite-dimensional inner product space $V$ is self-adjoint if and only if $V$ has an orthonormal basis of eigenvectors of $T$. The hypothesis is *not* merely normal: on $\mathbb{R}^2$ a rotation by $90^\circ$ is normal (it commutes with its transpose, which is its inverse) but has no real eigenvectors. Self-adjointness rescues the situation by forcing all complex eigenvalues to be real and so available in $\mathbb{R}$. The proof uses an upper-triangular form for the complexification plus the reality of eigenvalues, or directly induction on dimension with the existence of one real eigenvalue and reduction to its orthogonal complement.

> [!tip] Unlocked: Spectral Measure *(from Functional Analysis)*
> In infinite [[Def - Dimension|dimensions]] a self-adjoint operator on a Hilbert space need not have eigenvalues, but it has a **spectral measure** — a projection-valued measure $E$ on the spectrum $\sigma(T) \subseteq \mathbb{R}$ such that $T = \int_{\sigma(T)} \lambda \, dE(\lambda)$. The spectral measure is the infinite-dimensional generalisation of the eigenvalue decomposition: a sum of one-dimensional projections becomes an integral of projection-valued differentials. Quantum measurement theory is built on this object: the probability that a measurement of an observable $T$ in state $|\psi\rangle$ yields a value in a Borel set $A \subseteq \mathbb{R}$ is $\langle \psi, E(A) \psi \rangle$.

> [!tip] Unlocked: Quantum Mechanics — Observables and the Born Rule *(from Physics)*
> In quantum mechanics every physical observable is by axiom a self-adjoint operator $\hat{A}$ on a Hilbert space; the spectral theorem then guarantees its eigenvalues are real (so possible measurement outcomes are real numbers) and that there is an orthonormal eigenbasis. The Born rule reads measurement statistics from the projection onto each eigenspace: if the state is $|\psi\rangle$, the probability of obtaining the eigenvalue $\lambda$ is $|\langle \lambda | \psi \rangle|^2$ (or the appropriate eigenspace integral in degenerate or continuous-spectrum cases). The entire mathematical structure of quantum measurement is the spectral theorem in disguise.

- **[[Ex - Spectral decomposition of a 2x2 normal matrix]]** (⭐)
	- Concrete computation: take $T = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$, verify normality, compute eigenvalues $1 \pm i$ and orthonormal eigenvectors, write spectral decomposition. Drill of the [[Thm - Complex Spectral Theorem|complex spectral theorem]] on a $2 \times 2$ case.

- **[[Ex - Functional calculus on a self-adjoint operator]]** (⭐⭐)
	- Establish $f(T) g(T) = (fg)(T)$ and $f(T)^* = \overline f(T)$ via spectral expansion and orthogonality of projections. Deduce the existence of the positive square root as a corollary.

- **[[Ex - Commuting self-adjoint operators simultaneously diagonalizable]]** (⭐⭐)
	- Two commuting self-adjoint operators share an orthonormal eigenbasis. The eigenspaces of $S$ are $T$-invariant when $ST = TS$, so the spectral theorem applies to $T|_{E_\lambda}$ within each eigenspace.

> [!note] Exercise Index — §7B
> [[Exercise Index - §7B Spectral Theorem]]

## §7C Positive Operators

- **[[Def - Positive Operator]]**
	- An operator $T \in \mathcal{L}(V)$ is **positive** (in some books **positive semidefinite**) if $T$ is self-adjoint and $\langle Tv, v \rangle \geq 0$ for all $v \in V$. It is **positive definite** if the inequality is strict for $v \neq 0$, equivalently if $T$ is positive and invertible. Equivalent characterisations: $T$ is self-adjoint with non-negative eigenvalues; $T = S^* S$ for some $S \in \mathcal{L}(V, W)$; $T$ has a positive square root. Over $\mathbb{C}$, the self-adjointness in the definition is automatic from $\langle Tv, v \rangle \geq 0$ (in particular real); over $\mathbb{R}$ it must be assumed.

- **[[Thm - Positive Operators Have a Unique Square Root]]**
	- Every positive operator $T$ has a unique positive square root $\sqrt{T}$ — a positive operator $R$ with $R^2 = T$. The proof uses the spectral theorem: $T = \sum \lambda_j P_j$ with $\lambda_j \geq 0$, and $\sqrt{T} = \sum \sqrt{\lambda_j} P_j$. Uniqueness comes from the fact that any positive square root must commute with $T$ and so be simultaneously diagonalised. This is the operator analogue of taking the non-negative square root of a non-negative real number, and it is what makes the absolute value $|T| = \sqrt{T^*T}$ well-defined.

- **[[Thm - Cholesky Factorization]]**
	- Every positive definite operator $T$ on $V$ factors uniquely as $T = R^* R$ where $R$ is upper-triangular (in a fixed orthonormal basis) with positive diagonal entries. Equivalently, a positive definite matrix $A$ factors as $A = L L^*$ with $L$ lower-triangular and positive diagonal. The Cholesky factor is half the work of an LU decomposition because the symmetry is exploited, and it is the standard way to solve $Ax = b$ for symmetric positive definite $A$ — numerically more stable than direct inversion and twice as fast as LU.

> [!tip] Unlocked: Positive Semidefinite Programming *(from Optimization)*
> The cone of positive semidefinite matrices is closed and convex; optimisation problems whose feasible region is the intersection of an affine [[Def - Subspace|subspace]] with this cone are called **semidefinite programs** (SDPs). They include linear programs as a special case and are powerful enough to encode max-cut relaxations, sum-of-squares optimisation, and the dual of many control-theoretic problems. The geometry of the PSD cone — its boundary corresponds to rank-deficient matrices — is governed by the spectral theorem.

- **[[Ex - Square root of a 2x2 positive matrix]]** (⭐)
	- Compute $\sqrt T$ for $T = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$ via spectral decomposition: diagonalise, square-root eigenvalues, reassemble. The standard recipe for any matrix square root.

- **[[Ex - Cholesky factorization by hand]]** (⭐⭐)
	- Walk through the Cholesky algorithm on a $3 \times 3$ positive definite matrix, computing entries of the upper-triangular factor $R$ from the equations $T_{ij} = (R^* R)_{ij}$. The algorithm's positive-diagonal check doubles as a positive-definiteness check.

- **[[Ex - Unitary 2x2 matrices form a Lie group]]** (⭐⭐)
	- Show $U(2)$ is a group; parameterise its elements via $T = e^{i\theta} \begin{pmatrix} a & b \\ -\overline b & \overline a \end{pmatrix}$ with $|a|^2 + |b|^2 = 1$; compute the real dimension to be $4$. Bridge to Lie theory.

> [!note] Exercise Index — §7C–D
> [[Exercise Index - §7C–D Positive Operators, Isometries, and Matrix Factorizations]]

## §7D Isometries, Unitary Operators, QR and Cholesky

- **[[Def - Isometry]]**
	- A linear map $S \in \mathcal{L}(V, W)$ is an **isometry** if it preserves norms: $\|Sv\| = \|v\|$ for all $v \in V$. Equivalently $\langle Sv, Sw \rangle = \langle v, w \rangle$ for all $v, w$ (preserves the inner product), or $S^* S = I_V$. An isometry is automatically injective. The matrix of an isometry in orthonormal bases has orthonormal columns. The word "isometry" is reserved for linear [[Def - Isometry|isometries]] here; the general notion of metric-space isometry coincides with this in the linear case.

- **[[Def - Unitary Operator]]**
	- An operator $T \in \mathcal{L}(V)$ is **unitary** if it is a surjective isometry, equivalently $T^* T = T T^* = I$, equivalently $T^{-1} = T^*$. Over $\mathbb{R}$ a unitary operator is called **orthogonal**. In a finite-dimensional setting an isometry $V \to V$ is automatically surjective (by dimension), so on $\mathcal{L}(V)$ "isometry" and "unitary" coincide; the distinction matters only for $V \to W$ with $\dim W > \dim V$. Unitary operators are normal with eigenvalues on the unit circle.

- **[[Thm - Characterization of Isometries]]**
	- The following are equivalent for $S \in \mathcal{L}(V, W)$ in finite [[Def - Dimension|dimensions]]: (i) $S$ is an isometry; (ii) $\langle Sv, Sw \rangle = \langle v, w \rangle$ for all $v, w$; (iii) $S^* S = I_V$; (iv) $S$ sends some orthonormal basis to an orthonormal list; (v) $S$ sends every orthonormal basis to an orthonormal list; (vi) the columns of the matrix of $S$ in orthonormal bases are orthonormal. Each item is the right characterisation for a different setting: (i) for verification by definition, (iii) for symbolic manipulation, (iv)/(v) for construction, (vi) for matrix calculations.

- **[[Thm - QR Factorization]]**
	- Every linear map $A : \mathbb{F}^n \to \mathbb{F}^m$ with linearly independent columns factors as $A = QR$, where $Q$ has orthonormal columns and $R$ is upper-triangular with positive real diagonal entries. The factorisation is unique under the positive-diagonal condition. It is exactly the [[Thm - Gram-Schmidt Procedure|Gram–Schmidt procedure]] read backwards: $Q$ is the orthonormal basis Gram–Schmidt produces from the columns of $A$, and $R$ encodes the inner products that recover the original columns from this orthonormal basis. QR is the standard numerically stable way to solve $Ax = b$ for invertible square $A$.

> [!tip] Unlocked: [[Def - The Lorentz Group|Lorentz Group]] $O(1,3)$ *(from Special Relativity)*
> Replace the positive-definite inner product with the **indefinite Minkowski form** $\eta(v, w) = -v^0 w^0 + v^1 w^1 + v^2 w^2 + v^3 w^3$ (see [[Def - Minkowski Space and the Metric]]), and ask for the linear maps preserving it. The result is the **Lorentz group** [[Def - The Lorentz Group|$O(1,3)$]] — exactly the orthogonal group construction performed for the indefinite signature $(1,3)$ instead of $(n, 0)$. The pseudo-orthogonal [[Def - Group|groups]] $O(p, q)$ form the broader family; the orthogonal group is the special case $q = 0$ where the inner product is positive definite. The proof that $O(p, q)$ is a Lie group is identical to the proof that $O(n)$ is one — both rest on the implicit function theorem applied to the polynomial equations $S^* J S = J$.

> [!tip] Unlocked: Orthogonal [[Def - Group|Group]] $O(n)$ as a [[Def - Lie Group|Lie Group]] *(from Lie Theory)*
> The orthogonal group $O(n) = \{S \in \operatorname{GL}_n(\mathbb{R}) : S^t S = I\}$ is a compact Lie group of dimension $\binom{n}{2}$ — the dimension of its Lie algebra $\mathfrak{so}(n)$ of antisymmetric matrices. The connected component containing the identity is $\operatorname{SO}(n)$, the rotation group; the other component consists of orientation-reversing maps. Every element of $\operatorname{SO}(n)$ is a rotation in some 2-plane (block-diagonal of rotation matrices), and the maximal torus of $\operatorname{SO}(n)$ is precisely the group of block-diagonal rotations.

## §7E SVD

- **[[Def - Singular Values]]**
	- For $T \in \mathcal{L}(V, W)$ the **singular values** of $T$ are the non-negative square roots of the eigenvalues of the positive operator $T^* T$, listed in decreasing order $s_1 \geq s_2 \geq \cdots \geq s_n \geq 0$ with multiplicity. Equivalently they are the eigenvalues of $|T| = \sqrt{T^* T}$. Geometrically the singular values are the lengths of the semi-axes of the ellipsoid $T(B)$, where $B = \{v : \|v\| \leq 1\}$ is the unit ball of $V$. The largest singular value $s_1$ equals the operator norm $\|T\|_{\text{op}} = \sup_{\|v\| = 1} \|Tv\|$.

- **[[Thm - Singular Value Decomposition]]**
	- Every linear map $T \in \mathcal{L}(V, W)$ admits a singular value decomposition: there exist orthonormal bases $e_1, \ldots, e_n$ of $V$ and $f_1, \ldots, f_n$ of (a [[Def - Subspace|subspace]] of) $W$, and non-negative reals $s_1 \geq \cdots \geq s_n \geq 0$, such that $T e_j = s_j f_j$ for each $j$. Equivalently, in matrix form, every matrix $A$ factors as $A = U \Sigma V^*$ where $U$ and $V$ are unitary and $\Sigma$ is the diagonal matrix of singular values padded with zeros. This is the **universal factorisation theorem** of finite-dimensional linear algebra: it holds for every linear map, square or rectangular, invertible or not, real or complex.

- **[[Ex - SVD computes the operator norm]]** (⭐⭐)
	- Show $\|T\|_{\text{op}} = s_1(T)$, the largest singular value, by writing the supremum in terms of an orthonormal basis of right-singular vectors and observing that the maximum of a non-negative weighted sum of unit-weighted terms is the largest weight.

- **[[Ex - Best low-rank approximation via SVD]]** (⭐⭐⭐)
	- Prove the **Eckart–Young theorem**: the rank-$k$ truncation of the SVD is the closest rank-$k$ matrix in the operator norm and the Frobenius norm. The unifying frame for low-rank approximation, dimensionality reduction, and PCA.

> [!tip] Unlocked: Principal Component Analysis *(from Statistics)*
> Given a data matrix $X \in \mathbb{R}^{n \times p}$ (rows = samples, columns = features), centre the columns to mean zero and form the sample covariance $\Sigma = \frac{1}{n-1} X^t X$. The eigenvectors of $\Sigma$ are the **principal components** — the orthogonal directions of maximal variance — and the eigenvalues are the variances along those directions. These are precisely the right-singular vectors and (squared, rescaled) singular values of $X$ itself. **PCA is SVD applied to a centred data matrix.** The Eckart–Young theorem provides its theoretical justification: projecting onto the top $k$ principal components gives the best rank-$k$ approximation of the data in the Frobenius norm.

> [!tip] Unlocked: Low-Rank Approximation *(from Numerical Linear Algebra)*
> The Eckart–Young theorem makes the SVD the universal tool for low-rank approximation: image compression (storing only the top singular values of an image matrix), latent semantic analysis in NLP (truncated SVD of a term-document matrix yields semantic embeddings), recommender systems (matrix completion via truncated SVD), and randomised numerical linear algebra (the randomised SVD scales the technique to enormous matrices). Every appearance of "best rank-$k$" in applied mathematics traces back to this theorem.

> [!note] Exercise Index — §7E–F
> [[Exercise Index - §7E–F SVD and Polar Decomposition]]

## §7F Polar Decomposition and Consequences

- **[[Thm - Polar Decomposition]]**
	- Every operator $T \in \mathcal{L}(V)$ on a complex inner product space factors as $T = S R$, where $S$ is an isometry (unitary, in the finite-dimensional operator case) and $R = \sqrt{T^* T} = |T|$ is the unique positive square root of $T^* T$. This is the operator analogue of the polar form $z = e^{i\theta} \, r$ of a complex number: $R$ plays the role of the magnitude, $S$ plays the role of the phase. The polar decomposition is unique when $T$ is invertible; for non-invertible $T$, $R$ is still unique but $S$ has freedom on the kernel of $T$. In SVD terms, if $T = U \Sigma V^*$ then $S = U V^*$ and $R = V \Sigma V^*$.

- **[[Ex - Polar decomposition unique for invertible operators]]** (⭐⭐)
	- Show that when $T$ is invertible, the polar factors $S$ and $R$ are uniquely determined. The non-invertible case has freedom on $\operatorname{null} T$, illustrating how invertibility is the precise condition that removes the gauge.

> [!tip] Unlocked: Operator Magnitude and Phase *(from Functional Analysis)*
> The polar decomposition extends to bounded operators on infinite-dimensional Hilbert spaces, with $S$ now a **partial isometry** (an isometry from $(\operatorname{null} T)^{\perp}$ onto $\overline{\operatorname{range} T}$). The decomposition $T = S |T|$ is then the operator-theoretic analogue of $z = e^{i\theta} |z|$. The positive operator $|T| = \sqrt{T^* T}$ is called the **absolute value** of $T$ and plays a central role in the theory of compact operators, Schatten classes, and the non-commutative integration theory of von Neumann algebras.

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The exercises in this chapter cluster around five recurring goals. The most common is **diagonalising an operator orthogonally** — given a normal or self-adjoint operator, produce an orthonormal eigenbasis or compute the spectral decomposition. A second is **computing a singular value decomposition** for a non-square or non-invertible matrix and reading off its consequences: operator norm, rank, low-rank approximations. A third is **factorising a positive or invertible operator** — producing the unique positive square root, the Cholesky factor, or the polar decomposition. A fourth is **establishing a characterisation** — that a given operator is normal, self-adjoint, positive, or an isometry, often by verifying one of the equivalent operational characterisations rather than the definition. A fifth, more delicate, is **extremal calculations** — finding the operator's largest singular value (the operator norm), the closest matrix of bounded rank, or the best fit subject to constraints. These goals all share a common skeleton: each is, at its heart, an application of the spectral theorem, sometimes to $T$ and sometimes to a positive operator built from $T$.

**Sources — what assumptions do we usually leverage?**

The recurring sources are equally stereotyped. **The operator is given as normal** (or self-adjoint, positive, unitary) — this is the most direct source, routing instantly to the spectral theorem. **The operator commutes with its adjoint** — the working definition of normality. **The operator preserves norms** — this is isometry, which characterises unitary operators on the same space. **The operator is presented as $S^* S$ for some $S$** — this guarantees positivity, opening the door to the square root and Cholesky. **The operator is given by a matrix in an orthonormal basis** — this makes the adjoint computable concretely (conjugate transpose) and allows direct verification of self-adjointness, normality, or unitarity. The chapter's central routing pattern is: **source = "this operator is normal"** routes through the spectral theorem to **target = "diagonal form with explicit eigenvalues"**, after which every other target — norm, rank, factorisation — follows. For a non-square or non-invertible map, the route detours through the positive operator $T^* T$ before reaching the SVD.

---

# Legal Operations

The moves below assemble nearly every solution in this topic. When stuck, scan the list and try each operation.

1. **Diagonalise a normal operator via the spectral theorem.** Given $T$ normal on a complex inner product space, the [[Thm - Complex Spectral Theorem|complex spectral theorem]] produces an orthonormal eigenbasis. Over $\mathbb{R}$, the same move requires self-adjointness ([[Thm - Real Spectral Theorem|real spectral theorem]]). *Trigger:* "$T$ is normal" or "$T = T^*$". *Pattern:* write $T = \sum \lambda_j P_j$ where $P_j$ is the orthogonal projection onto the $\lambda_j$-eigenspace; the $P_j$ are pairwise orthogonal and sum to $I$.

2. **Pass from $T$ to $T^* T$.** Every linear map $T : V \to W$ produces a positive operator $T^* T$ on $V$, which is diagonalisable by the spectral theorem even when $T$ itself is not square, not normal, or not invertible. *Trigger:* $T$ is non-square or non-normal but you want a spectral decomposition. *Pattern:* compute the eigenvalues of $T^* T$; their square roots are the singular values of $T$.

3. **Compute the adjoint as the conjugate transpose in an orthonormal basis.** When the operator is given by a matrix in an orthonormal basis, $T^*$ is obtained by conjugate-transposing. *Trigger:* the matrix of $T$ is in hand and you need $T^*$. *Pattern:* over $\mathbb{R}$ this is the transpose; over $\mathbb{C}$ conjugate each entry and transpose.

4. **Use the [[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz representation theorem]] to define an adjoint.** For an abstractly defined linear map, the adjoint is constructed by representing the linear functional $v \mapsto \langle Tv, w \rangle$ by some vector $T^* w$. *Trigger:* you need to *define* an adjoint, not just compute it. *Pattern:* apply Riesz to fix $T^* w$, then check linearity in $w$.

5. **Extract a positive square root.** A positive operator $T$ has a unique positive operator $R$ with $R^2 = T$. *Trigger:* you have a positive operator and need an operator whose square is it. *Pattern:* spectral theorem on $T$, take square roots of eigenvalues, reassemble as $R = \sum \sqrt{\lambda_j} P_j$. The operator $|T| = \sqrt{T^* T}$ is built this way.

6. **Build the polar decomposition $T = S |T|$.** Every operator factors as isometry times positive. *Trigger:* you want to separate a "rotation" from a "stretching" of $T$, or you want to read off the singular values without computing the full SVD. *Pattern:* compute $|T| = \sqrt{T^* T}$; then $S$ is determined by $S |T| = T$ (and uniquely if $T$ is invertible).

7. **Reduce to an invariant orthogonal complement.** If $U$ is invariant under a normal $T$, then $U^{\perp}$ is also invariant — and both are invariant under $T^*$. This is the inductive engine of the spectral theorem's proof. *Trigger:* you have one eigenvector or one invariant subspace; you want to recurse. *Pattern:* find a single eigenvalue (always exists on $\mathbb{C}$, or by self-adjointness on $\mathbb{R}$), pick an eigenvector, pass to its orthogonal complement, and recurse.

8. **Use orthonormality of an eigenbasis to read off operator-norm and trace-class quantities.** Once $T$ is diagonalised orthonormally, $\|Tv\|^2 = \sum |\lambda_j|^2 |\langle v, e_j \rangle|^2$, so the operator norm is $\max |\lambda_j|$, the Hilbert–Schmidt norm is $\sqrt{\sum |\lambda_j|^2}$, the trace is $\sum \lambda_j$, the determinant is $\prod \lambda_j$. *Trigger:* you have a diagonalisation and need an operator-theoretic invariant. *Pattern:* read it off the eigenvalues; spectral diagonalisation makes every invariant a function of the spectrum.

9. **Apply Gram–Schmidt for QR factorisation.** Gram–Schmidt on the columns of $A$ produces the columns of $Q$, and the inner products produced along the way fill in the upper triangle of $R$. *Trigger:* you want $A = QR$ with $Q$ orthonormal columns and $R$ upper-triangular. *Pattern:* run Gram–Schmidt and record the orthogonalisation coefficients.

10. **Compute a rank-$k$ approximation via SVD truncation.** Given $T = U \Sigma V^*$ and a target rank $k$, set $\Sigma_k$ to the truncation keeping the top $k$ singular values; $T_k = U \Sigma_k V^*$ is the unique best rank-$k$ approximation in operator and Frobenius norms ([[Ex - Best low-rank approximation via SVD|Eckart–Young]]). *Trigger:* "find the best rank-$k$ approximation". *Pattern:* compute SVD, truncate, multiply back.

**Illegal but tempting operations:**

> [!warning] 1. Applying the real spectral theorem to a normal but non-self-adjoint operator.
> Over $\mathbb{R}$, "normal" is not enough — the [[Thm - Real Spectral Theorem|real spectral theorem]] requires *self-adjoint*. The standard counterexample is the rotation by $90^\circ$ on $\mathbb{R}^2$, with matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$: it satisfies $T^t T = T T^t = I$ (so is normal, indeed orthogonal) but has no real eigenvectors. The operation becomes legal exactly when one of two extra conditions holds: $T$ is self-adjoint, or one complexifies $V$ and works over $\mathbb{C}$ where the [[Thm - Complex Spectral Theorem|complex spectral theorem]] applies.

> [!warning] 2. Treating the adjoint as the transpose in a non-orthonormal basis.
> The matrix of $T^*$ is the conjugate transpose of the matrix of $T$ only in an *orthonormal* basis. In a general basis it is more complicated — the inner product induces a matrix $G$ (the Gram matrix), and the matrix of $T^*$ is $G^{-1} M^* G$ where $M$ is the matrix of $T$. The operation becomes legal exactly when the basis is orthonormal, which is what makes orthonormal bases the only basis worth using in inner product space contexts.

> [!warning] 3. Claiming uniqueness of polar decomposition when $T$ is non-invertible.
> The polar factor $R = |T|$ is always unique, but the isometric factor $S$ is unique only when $T$ is invertible. For non-invertible $T$, $S$ is only determined on $\operatorname{range} |T| = (\operatorname{null} T)^{\perp}$; on $\operatorname{null} T$ it can be chosen freely. The operation becomes uniquely legal exactly when $\operatorname{null} T = \{0\}$, that is, when $T$ is invertible. See [[Ex - Polar decomposition unique for invertible operators]].

> [!warning] 4. Confusing eigenvalues of $T$ with singular values of $T$.
> The eigenvalues of $T$ live in $\mathbb{F}$ (complex unless $T$ is self-adjoint) and need not be non-negative; the singular values of $T$ are *always* non-negative reals. They coincide (up to absolute value) only when $T$ is normal: for normal $T$, $s_j(T) = |\lambda_j(T)|$. For non-normal $T$, the two sequences can diverge dramatically — the singular values measure the operator's stretching factors, while the eigenvalues measure its directional fixed-point structure. The operation "use eigenvalues to compute the operator norm" is legal *only* for normal operators; for general operators, use singular values.

> [!warning] 5. Forgetting the boundary terms in the integration-by-parts computation of an adjoint.
> When computing the adjoint of a differential operator on a function space, integration by parts produces boundary terms that the formal adjoint $-d/dx$ alone does not capture. The adjoint depends on the function-space boundary conditions: $(d/dx)^*$ equals $-d/dx$ on functions vanishing at the endpoints but acquires a boundary contribution otherwise. The operation becomes legal when one restricts to a domain where the boundary terms vanish — see [[Ex - Adjoint of differentiation is negative differentiation with boundary conditions]] for the full computation.

---

# Problem-Solving Strategy

Every problem in this topic is, at root, a routing problem: you start from a presentation of an operator $T$ — a matrix, an abstract definition, a property — and you want to reach a structural conclusion. The map from sources to targets is dictated by the spectral hierarchy, and the strategy is to identify your position in the hierarchy and to use the strongest theorem available.

If the problem **gives you a normal operator on a complex space**, route immediately through the [[Thm - Complex Spectral Theorem|complex spectral theorem]]. Diagonalising orthonormally is the most powerful single move in the chapter and it is available the moment normality is in hand. Once you have the diagonal form, *every* operator-theoretic invariant of $T$ — its norm, its trace, its determinant, its eigenvalues, its functional calculus values $f(T)$ — is a function of the eigenvalues. Many problems are won in one step by this move: "find the operator norm of a normal operator" reduces to "find the maximum modulus of an eigenvalue". On the real side, the same routing works if (and essentially only if) the operator is self-adjoint, via the [[Thm - Real Spectral Theorem|real spectral theorem]]. If the operator is normal but not self-adjoint over $\mathbb{R}$, the cleanest move is to complexify and apply the complex theorem, then descend.

If the problem **gives a non-square or non-invertible linear map**, normality is unavailable but the [[Thm - Singular Value Decomposition|SVD]] is. The route is universal: form $T^* T$, which is automatically positive and so diagonalises orthonormally; its eigenvalues are squares of singular values; an orthonormal eigenbasis of $T^* T$ together with the action of $T$ on it produces the full SVD. From the SVD you read off the rank ("number of nonzero singular values"), the operator norm ("largest singular value"), the Frobenius norm ("$\sqrt{\sum s_j^2}$"), the [[Def - Pseudoinverse|pseudoinverse]] ("$V \Sigma^+ U^*$"), and the best rank-$k$ approximation ("truncate"). Problems with a "find the best approximation" or "find the operator norm" flavour are reliably SVD problems.

If the problem **asks you to factorise an operator** — write $T$ as a product of simpler pieces — the chapter offers four standard factorisations, and the right one is dictated by what $T$ is. For $T$ positive definite, $T = R^* R$ with $R$ upper-triangular ([[Thm - Cholesky Factorization|Cholesky]]); for $T$ invertible square, $T = QR$ with $Q$ unitary and $R$ upper-triangular ([[Thm - QR Factorization|QR]], via Gram–Schmidt); for $T$ any operator, $T = S |T|$ with $S$ an isometry ([[Thm - Polar Decomposition|polar]]); for $T$ any linear map, $T = U \Sigma V^*$ ([[Thm - Singular Value Decomposition|SVD]]). The choice is forced by the structure of the input: Cholesky requires positivity, QR requires linear independence of columns, polar requires nothing beyond an inner product space, SVD requires nothing.

If the problem **asks you to verify a characterisation** — "show $T$ is normal" or "show $T$ is unitary" — use the equivalent operational characterisations rather than the definitions. Self-adjointness can often be read off the matrix (in an orthonormal basis: equals its conjugate transpose) without checking $\langle Tv, w \rangle = \langle v, Tw \rangle$ for all $v, w$. Unitarity is most efficiently checked via $T^* T = I$ on basis vectors. Normality is most efficiently checked via $\|Tv\| = \|T^* v\|$ on basis vectors, or via the matrix relation $M M^* = M^* M$. The work cost differs by orders of magnitude depending on which characterisation you pick, and the choice is where most novice solutions become unnecessarily painful.

A meta-strategy threads through all of this: **every theorem in this chapter is an application of the spectral theorem to some positive or normal operator built from $T$.** When stuck, the productive question is not "what theorem applies to $T$" but "what normal operator can I build from $T$ that the spectral theorem will diagonalise?" If $T$ is itself normal — done. If $T$ is a general linear map — $T^* T$ is positive, route through SVD. If $T$ is a positive operator and you need a square root or a Cholesky factor — apply the spectral theorem to $T$ directly. Each of the four factorisation theorems is the spectral theorem in disguise; recognising this collapses the chapter to a single technique applied in five contexts.

---

# Most Reusable Properties

- **[[Thm - Complex Spectral Theorem|Complex Spectral Theorem]]**: every normal operator on a complex inner product space is orthonormally diagonalisable. **Typical use:** once you have a normal operator, *every* downstream question about it — its norm, its functional calculus values $f(T)$, its commutant, its powers $T^n$, its square roots — is settled by the spectral decomposition. Reach for it first whenever any normal operator appears. The combination with functional calculus produces an inflation of usable identities: $\sqrt{T}$, $e^T$, $f(T)$ for any function $f$ defined on the spectrum.

- **[[Thm - Singular Value Decomposition|Singular Value Decomposition]]**: every linear map factors as $U \Sigma V^*$. **Typical use:** the workhorse for problems involving any linear map that is not visibly normal — non-square matrices, non-invertible operators, problems where the eigenvalues of $T$ are not what you want. The SVD reduces every such problem to a computation involving the singular values, which are non-negative reals and so always available. The combination with rank-$k$ truncation gives the Eckart–Young theorem, the basis of all low-rank approximation theory.

- **[[Thm - Positive Operators Have a Unique Square Root|Operator square root]]**: a positive operator has a unique positive square root, computed by taking square roots of eigenvalues in the spectral decomposition. **Typical use:** the absolute value $|T| = \sqrt{T^* T}$ of any operator, the polar decomposition's positive factor, the Cholesky factor, and the standard deviations in PCA all rely on this. The pattern "form a positive operator, take its square root" is the bridge from "I have a non-negative quantity" to "I have an operator I can manipulate".

- **[[Thm - Properties of the Adjoint|Adjoint as duality with the inner product]]**: $\operatorname{null} T^* = (\operatorname{range} T)^{\perp}$ and $\operatorname{range} T^* = (\operatorname{null} T)^{\perp}$. **Typical use:** any problem involving the "complement" of an image or kernel is a problem about the adjoint. The orthogonal complement of the range of $T$ is exactly the kernel of $T^*$ — this is the inner-product version of the rank-nullity theorem and underlies the Fredholm alternative in operator theory. The pattern "I want to characterise vectors orthogonal to the range of $T$" should immediately suggest "solve $T^* w = 0$".

- **[[Thm - QR Factorization|QR factorisation]]** and **[[Thm - Cholesky Factorization|Cholesky factorisation]]**: standard matrix factorisations that exploit, respectively, orthonormality and positivity. **Typical use:** numerical linear algebra problems — solving $Ax = b$ for an invertible square $A$ (use QR, more stable than direct inversion), solving for a positive definite system (use Cholesky, half the work of LU), or constructing orthonormal bases incrementally (Gram–Schmidt is the QR factorisation written algorithmically). The QR/Cholesky factor is unique under the positive-diagonal normalisation, so it gives canonical forms.

---

# Bridges

1. **Group Theory — the classical groups as preservers of forms.** Every classical matrix Lie group in this chapter is defined by preservation of an inner product or determinant. The [[Def - Unitary Operator|unitary group]] $U(n) = \{T \in \operatorname{GL}_n(\mathbb{C}) : T^* T = I\}$ — the operators preserving the Hermitian inner product on $\mathbb{C}^n$ — is a [[Def - Subgroup|subgroup]] of $\operatorname{GL}_n(\mathbb{C})$ in the sense of [[Def - Group|Group Theory]]; the orthogonal group $O(n)$ is its real analogue; and the special orthogonal group $\operatorname{SO}(n) = O(n) \cap \operatorname{SL}_n(\mathbb{R})$, the rotations, is the kernel of the determinant homomorphism $O(n) \to \{\pm 1\}$. The first isomorphism theorem ([[Thm - First Isomorphism Theorem]]) applied to $\det : O(n) \to \{\pm 1\}$ gives $O(n)/\operatorname{SO}(n) \cong \mathbb{Z}/2$ — a connectivity statement (orientation-preserving versus reversing). All these groups are also Lie groups, and the polar decomposition over $\mathbb{C}$ provides the canonical diffeomorphism $\operatorname{GL}_n(\mathbb{C}) \cong U(n) \times (\text{positive definite matrices})$, exhibiting $U(n)$ as a maximal compact subgroup.

2. **Special Relativity — the Lorentz group as the orthogonal group of an indefinite form.** Replace the positive-definite inner product on $\mathbb{R}^4$ with the indefinite **Minkowski form** $\eta(v, w) = -v^0 w^0 + v^1 w^1 + v^2 w^2 + v^3 w^3$ (see [[Def - Minkowski Space and the Metric]]). The linear maps preserving $\eta$ form the **Lorentz group** [[Def - The Lorentz Group|$O(1, 3)$]] — exactly the construction that produces the orthogonal group, performed for the indefinite signature $(1, 3)$ instead of $(4, 0)$. The constraint becomes $S^t \eta S = \eta$, mimicking $S^t S = I$ word for word. The proof that $O(1,3)$ is a Lie group of dimension $6$ runs by the same implicit-function-theorem argument as the proof that $O(4)$ is a Lie group of dimension $6$. Unitary, orthogonal, and Lorentz groups are three instances of one construction.

3. **Functional Analysis — the spectral theorem on infinite-dimensional Hilbert spaces.** On a separable Hilbert space, a bounded self-adjoint operator $T$ need not have eigenvalues but always has a *spectral measure* $E$ — a projection-valued measure on the spectrum $\sigma(T) \subseteq \mathbb{R}$ — and the spectral theorem reads $T = \int_{\sigma(T)} \lambda \, dE(\lambda)$. The eigenspace projections $P_j$ of the finite-dimensional spectral theorem become projection-valued differentials $dE(\lambda)$; the sum becomes an integral; the discrete spectrum becomes a continuous spectrum. **Functional calculus** for $T$ — the ability to form $f(T) = \int f(\lambda) \, dE(\lambda)$ for any bounded Borel function $f$ defined on the spectrum — is the precise generalisation of the finite-dimensional formula $f(T) = \sum f(\lambda_j) P_j$. The whole edifice of quantum measurement theory and the theory of self-adjoint extensions of unbounded operators rests on this generalisation.

4. **Statistics — Principal Component Analysis is SVD applied to a centred data matrix.** Given a data matrix $X \in \mathbb{R}^{n \times p}$ whose rows are samples and whose columns have been centred to mean zero, the sample covariance is $\Sigma = \frac{1}{n - 1} X^t X$. The eigenvectors of $\Sigma$ are the **principal components** — the orthogonal directions of maximal variance — and the eigenvalues are the variances along those directions. These are exactly the right-singular vectors and (squared, rescaled) singular values of $X$ itself. The Eckart–Young theorem (see [[Ex - Best low-rank approximation via SVD]]) then provides the theoretical justification for projecting onto the top $k$ principal components: this projection is the best rank-$k$ approximation of the data in the Frobenius norm, so PCA is optimal dimensionality reduction in the least-squares sense.

5. **Rings and Modules — minimal polynomial and functional calculus.** The minimal polynomial of a self-adjoint operator $T$ (see [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]]) factors completely over $\mathbb{R}$ as a product of linear factors $(x - \lambda_j)$ with distinct real $\lambda_j$ — no repeated roots, because $T$ is semisimple. The ring $\mathbb{R}[T]$ generated by $T$ is then a quotient of $\mathbb{R}[x]$ by the minimal polynomial and is in fact isomorphic to $\prod_j \mathbb{R}$ — one copy of $\mathbb{R}$ per eigenvalue — with the $j$-th projection corresponding to the eigenspace projection $P_j$. The Chinese remainder theorem for rings then *is* the spectral decomposition, restated. Functional calculus $f(T)$ is the homomorphism $\mathbb{R}[x] \to \mathcal{L}(V)$, $x \mapsto T$, extended to all functions on the spectrum.

---

# Insights

**The unifying frame: every theorem in this chapter is the spectral theorem in disguise.** State it once: a normal operator on a complex inner product space has an orthonormal eigenbasis. From this single fact, with the right choice of normal operator to apply it to, every other result follows. Apply it to $T$ itself when $T$ is normal — the complex spectral theorem. Apply it to $T$ when $T$ is self-adjoint, over $\mathbb{R}$ or $\mathbb{C}$ — the real and complex spectral theorems. Apply it to the positive operator $T^* T$ for an arbitrary linear map $T$ — the singular value decomposition. Apply it to $T^* T$ and reorganise — the polar decomposition. Apply it to a positive operator $T$ and take square roots of eigenvalues — the existence of the positive square root, and then Cholesky. The chapter has the shape of a fan, with the spectral theorem at the hub and these five theorems at the rim. Internalising this collapses the chapter from a list of theorems to one technique with five applications.

**The true name of normality is the commuting characterisation.** The "official" definition of normality is $T T^* = T^* T$, and this *is* the right thing to think — it is the cleanest, most algebraic statement and the one used in proofs. But the working-day characterisation, the one you reach for in problems, is $\|T v\| = \|T^* v\|$ for all $v$. This second form is what links normality to the spectral theorem: it implies that $T$ and $T^*$ have the same kernel on every shift $T - \lambda I$ (since $(T - \lambda I)^* = T^* - \overline{\lambda} I$ and $T - \lambda I$ is also normal), and so eigenvectors of $T$ are eigenvectors of $T^*$ with conjugated eigenvalues, and this in turn is what makes eigenspaces for distinct eigenvalues orthogonal. Use $TT^* = T^*T$ when proving things *about* normal operators; use $\|Tv\| = \|T^* v\|$ when verifying that a given $T$ is normal.

**The SVD is universal.** Every linear map between inner product spaces — square or rectangular, invertible or singular, real or complex — admits a singular value decomposition. This is the deepest universality theorem of finite-dimensional linear algebra: there is no finite-dimensional linear map without an SVD, no condition needs to be checked beyond the existence of inner products on the source and target. The singular values are intrinsic invariants: under unitary changes of basis on the source and target, they are unchanged. The cleanest geometric statement is that the image of the unit ball $B = \{v : \|v\| \leq 1\}$ under $T$ is an ellipsoid (possibly degenerate, if $T$ is not invertible) whose semi-axis lengths are the singular values. This geometric picture is the right way to remember the SVD: the singular values measure the *deformation* of the unit ball, the right-singular vectors are the directions that pull back to the principal axes, and the left-singular vectors are the directions of the resulting axes in the codomain.

**The polar decomposition is the operator analogue of $z = r e^{i\theta}$.** Every complex number factors as a modulus times a unit complex number, $z = |z| \cdot e^{i\theta}$, and the factorisation is unique when $z \neq 0$. The operator-theoretic generalisation reads $T = S |T|$, where $|T| = \sqrt{T^*T}$ is the "modulus" — a positive operator playing the role of $|z|$ — and $S$ is an isometry playing the role of $e^{i\theta}$. The decomposition is unique when $T$ is invertible (the analogue of $z \neq 0$); when $T$ is non-invertible, $|T|$ is still unique but the isometric factor has gauge freedom on the kernel of $T$ (the analogue of the angle of $0$ being undefined). On the SVD level the decomposition is trivial: $T = U \Sigma V^* = (UV^*)(V \Sigma V^*)$, with $UV^*$ unitary and $V \Sigma V^*$ positive. The deeper message is that every operator is, up to a "rotation", a positive operator — and positive operators are the operator analogue of non-negative reals.

**The real vs complex spectral theorem boundary is sharp, and it is normality that fails.** Over $\mathbb{C}$, normality alone suffices for orthonormal diagonalisability. Over $\mathbb{R}$, normality is too weak: a rotation by $90^\circ$ is orthogonal hence normal, yet has no real eigenvectors — it is diagonalisable only when allowed complex eigenvalues. The condition that survives the descent from $\mathbb{C}$ to $\mathbb{R}$ is self-adjointness, because the eigenvalues of a self-adjoint operator are real and so live in $\mathbb{R}$ even when the proof goes through $\mathbb{C}$. The trigger-reaction pattern is: "see a normal operator on $\mathbb{R}^n$ that is not visibly self-adjoint → either complexify, or work with the real block-diagonal form (rotations of 2-planes plus real eigenvalues)". Over $\mathbb{C}$, no such caution is needed.

**Trigger-reaction patterns.** "See a normal operator → spectral theorem, write $T = \sum \lambda_j P_j$." "See a non-square or non-invertible matrix → singular value decomposition, take eigenvalues of $T^* T$." "Want a positive square root → spectral theorem on a positive operator, take square roots of eigenvalues." "Want to solve $Ax = b$ for invertible square $A$ by hand → QR is more numerically stable than direct inversion." "Want to solve $A x = b$ for positive definite $A$ → Cholesky, half the work and stable." "Want the operator norm of any matrix → largest singular value." "Want a low-rank approximation → SVD truncation, by Eckart–Young this is best in operator and Frobenius norms." Each of these is a single sentence and each is one solid hour of operator theory practice compressed.
