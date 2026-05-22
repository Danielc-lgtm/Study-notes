---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Isometry"
  - "Def - Adjoint of a Linear Map"
  - "Def - Normal Operator"
  - "Def - Inner Product Space"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional [[Def - Inner Product Space|inner product space]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$. An operator $T \in \mathcal{L}(V)$ has an [[Def - Adjoint of a Linear Map|adjoint]] $T^*$; the identity is $I = I_V$. Over $\mathbb{R}$, a unitary operator is called **orthogonal**; the convention is universal, and we use both terms freely (with the implicit field $\mathbb{R}$ for "orthogonal" and $\mathbb{C}$ for "unitary"). The **unitary group** on $V$ is $U(V) = \{T \in \operatorname{GL}(V) : T^*T = I\}$; over $\mathbb{R}$ this is the **orthogonal group** $O(V)$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

This is a compound page: it defines two interlocking notions — the unitary operator (over $\mathbb{C}$) and the orthogonal operator (over $\mathbb{R}$, the real case) — because they are introduced together and none is fully usable without the others. The unitary case and the orthogonal case are the same definition in two fields, and the theory is uniform; we use "unitary" as the umbrella term.

---

# Axiom Motivation

A unitary operator is a **surjective [[Def - Isometry|isometry]]** on $V$. The motivation runs as follows. Isometries are linear maps preserving the norm; the special case where the domain and codomain coincide (and the isometry is consequently surjective by dimension counting) is the case of operators that preserve the entire inner product structure of $V$ *and* are bijective. These operators form a group under composition — the **unitary group** $U(V)$ — and are precisely the "symmetries" of an inner product space, the analogue of rotations and reflections in Euclidean geometry.

The condition $T^* T = I$ (equivalently $T^* = T^{-1}$, when $T$ is invertible) is the algebraic embodiment of "norm-preserving, invertible". The three equivalent conditions
1. $T$ is a surjective isometry;
2. $T^* T = T T^* = I$;
3. $T^{-1} = T^*$ (i.e., $T$ is invertible and its inverse is its adjoint),

are different views of the same object. In finite dimensions, $T^* T = I$ alone forces $T$ to be invertible (an isometry $V \to V$ is automatically surjective), so $T^* T = I$ suffices for unitarity. In infinite dimensions both $T^* T = I$ and $T T^* = I$ must be checked — the unilateral shift on $\ell^2$ is an example where $S^* S = I$ but $S S^* \neq I$, so $S$ is an isometry but not unitary.

A unitary operator is automatically [[Def - Normal Operator|normal]]: $T T^* = I = T^* T$. The eigenvalues of a unitary operator have modulus $1$. Why? If $T v = \lambda v$ with $v \neq 0$, then $\|v\| = \|Tv\| = |\lambda| \|v\|$, forcing $|\lambda| = 1$. So unitary operators are precisely the **normal operators with eigenvalues on the unit circle of $\mathbb{C}$**. They are the operator analogue of complex numbers of modulus $1$ — points on the unit circle — and the spectral decomposition takes the form $T = \sum_j e^{i\theta_j} P_j$ with real phases $\theta_j$.

Why is this class important? Three reasons:
- **Unitaries are the symmetries of inner product spaces.** Any structural question about an inner product space — bases, subspaces, decompositions — has a meaning "up to unitary equivalence", and the unitary group acts on everything in the chapter.
- **Unitaries are the time evolution operators of quantum mechanics.** Schrödinger's equation has the solution $|\psi(t)\rangle = U(t) |\psi(0)\rangle$ where $U(t) = e^{-i \hat H t / \hbar}$ is unitary (because the Hamiltonian $\hat H$ is self-adjoint, and exponentials of $i$ times self-adjoint are unitary). The unitarity of time evolution is the algebraic encoding of probability conservation.
- **Unitaries are the change-of-basis matrices between orthonormal bases.** A unitary operator $T$ is exactly the change-of-basis matrix from one orthonormal basis to another. So "the spectral decomposition diagonalises a normal operator in some orthonormal basis" is equivalent to "there is a unitary $U$ such that $U^* T U$ is diagonal".

What if you tried to drop the surjectivity? Then you get a (possibly non-surjective) isometry — see [[Def - Isometry]]. In finite dimensions with $V = W$, surjectivity is automatic, so this distinction is invisible there; it matters only for non-square or infinite-dimensional cases.

What if you tried to drop $T^* T = I$ and demand only that $T$ preserves some specific basis? Then you have a permutation matrix (in that basis), a strict subset of the unitary operators. Permutation matrices are unitary, but most unitaries are not permutations — they mix basis vectors continuously.

What if you tried to keep $T^* T = I$ but relax the codomain? Then you get linear isometries $V \to W$ with $\dim W \geq \dim V$. These form a "Stiefel manifold" of orthonormal $k$-frames in $\mathbb{F}^n$, which is important in algebraic topology but not in elementary linear algebra.

What if you tried to strengthen by demanding $\det T = 1$? You get the **special unitary group** $SU(V)$ (or **special orthogonal group** $SO(V)$ over $\mathbb{R}$). These are the orientation-preserving, "rotation"-type isometries: rotations in $\mathbb{R}^n$ are exactly the elements of $SO(n)$, while reflections sit in $O(n) \setminus SO(n)$ with $\det = -1$.

---

# The Definition

An operator $T \in \mathcal{L}(V)$ is **unitary** if $T^* T = T T^* = I$.

Over $\mathbb{R}$ this is called **orthogonal**.

**Equivalent characterisations** (in finite dimensions):
1. $T^* T = T T^* = I$ — equivalently $T^{-1} = T^*$.
2. $T$ is a bijective [[Def - Isometry|isometry]].
3. $\langle Tv, Tw \rangle = \langle v, w \rangle$ for all $v, w$ (preserves inner product), and $T$ is invertible.
4. $T$ sends an orthonormal basis to an orthonormal basis.
5. The matrix of $T$ in some (equivalently, every) orthonormal basis has orthonormal columns *and* orthonormal rows.
6. $T$ is a [[Def - Normal Operator|normal]] operator whose eigenvalues all have modulus $1$.

In finite dimensions, the conditions $T^* T = I$ alone and $T T^* = I$ alone are each equivalent to "$T$ is unitary" (each implies $T$ is invertible by injectivity-via-norm-preservation and dimension count, hence the other condition follows automatically). In infinite dimensions both must be checked.

A matrix is called a **unitary matrix** (over $\mathbb{C}$) or **orthogonal matrix** (over $\mathbb{R}$) if it represents a unitary operator in some orthonormal basis. Equivalently, $U \in M_n(\mathbb{F})$ is unitary if $U^* U = I$, where $U^*$ is the conjugate transpose.

---

# Categorical / Structural Definition

The unitary operators on $V$ form a group under composition: the **unitary group** $U(V)$, a closed Lie subgroup of $\operatorname{GL}(V)$. Over $\mathbb{C}$ with $V = \mathbb{C}^n$ this is $U(n) = \{T \in \operatorname{GL}_n(\mathbb{C}) : T^* T = I\}$, a compact real Lie group of (real) dimension $n^2$. Its Lie algebra $\mathfrak{u}(n)$ is the space of **skew-Hermitian** matrices $\{X : X^* = -X\}$, and the exponential map $\exp : \mathfrak{u}(n) \to U(n)$ is surjective.

Over $\mathbb{R}$ with $V = \mathbb{R}^n$ this is $O(n) = \{T \in \operatorname{GL}_n(\mathbb{R}) : T^t T = I\}$, a compact real Lie group of dimension $\binom{n}{2} = n(n-1)/2$. Its Lie algebra $\mathfrak{o}(n) = \mathfrak{so}(n)$ is the space of **antisymmetric** matrices.

The **determinant homomorphism** $\det : U(n) \to U(1) = S^1$ (or $O(n) \to \{\pm 1\}$) is surjective with kernel $SU(n)$ (or $SO(n)$), giving short exact sequences
$$1 \to SU(n) \to U(n) \to U(1) \to 1, \qquad 1 \to SO(n) \to O(n) \to \{\pm 1\} \to 1.$$
By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]], $U(n)/SU(n) \cong U(1) = S^1$ and $O(n)/SO(n) \cong \mathbb{Z}/2$.

**Categorical role:** the unitary group $U(V)$ is the **automorphism group** of $V$ as an inner product space — the group of structure-preserving self-isomorphisms. Just as $\operatorname{GL}(V)$ is the automorphism group of $V$ as a vector space (no inner product), $U(V)$ is the automorphism group when the inner product structure is preserved.

---

# Relate to Other Fields / Compression

In **quantum mechanics**, **unitary operators are the time evolutions and symmetry transformations**. Schrödinger's equation $i\hbar \partial_t |\psi\rangle = \hat H |\psi\rangle$ has solution $|\psi(t)\rangle = e^{-i\hat H t / \hbar} |\psi(0)\rangle$; the operator $U(t) = e^{-i\hat H t / \hbar}$ is unitary because $\hat H$ is self-adjoint and $iH$ is then skew-adjoint, exponentiating to a unitary. Conservation of probability — total $|\psi|^2$ remains $1$ — is the unitarity of $U(t)$. Quantum gates in computing are unitary operators. CPTP (completely positive trace preserving) maps in open quantum systems are *not* unitary in general; only closed-system evolution is.

In **special relativity**, the analogue of $U(n)$ for the indefinite Minkowski inner product is the [[Def - The Lorentz Group|Lorentz group]] $O(1, 3)$. The relation defining it is $\Lambda^t \eta \Lambda = \eta$ (where $\eta$ is the Minkowski metric), exactly mirroring $U^* U = I$ with $\eta$ in place of $I$. The Lorentz group has the same Lie-theoretic structure as $O(n)$ but with indefinite signature; its connected component containing the identity is $SO^+(1, 3)$, the **proper orthochronous Lorentz group**.

In **Fourier analysis**, the **Fourier transform** on $L^2(\mathbb{R})$ is a unitary operator: it preserves the $L^2$ inner product (Parseval's theorem). This is the infinite-dimensional analogue of the change-of-basis matrix between two orthonormal bases. The discrete Fourier transform on $\mathbb{C}^n$ is similarly unitary, with the columns of the DFT matrix being orthogonal complex exponentials.

In **classical mechanics**, **symplectic transformations** preserve a symplectic form $\omega$ rather than an inner product; they form the **symplectic group** $\operatorname{Sp}(2n, \mathbb{R})$, a non-compact Lie group of dimension $n(2n + 1)$. Symplectic, unitary, and orthogonal groups all share the structural pattern "preserve a non-degenerate bilinear form"; they differ in which form is preserved.

**True name:** A unitary operator is the **change-of-basis matrix between orthonormal bases**. Whenever you change from one orthonormal basis of $V$ to another, the change-of-basis matrix is unitary, and conversely every unitary matrix arises this way. This is the most operationally useful characterisation: spectral diagonalisation of a normal operator $T$ amounts to finding a unitary $U$ such that $U^* T U$ is diagonal, and that $U$ is the change of basis to the eigenbasis. The matrix relation $U^* U = I$ is what guarantees that the columns of $U$ form an orthonormal basis.

A second true name: **the operator that preserves all geometric structure** — distances, angles, volumes (up to sign over $\mathbb{R}$). This is the geometric picture: unitaries are the isometries of $V$, the analogue of rigid motions of Euclidean space.

---

# Examples / Corollaries

The identity $I$ is the trivial unitary. The negation $-I$ is unitary, with all eigenvalues $-1$.

Rotations of $\mathbb{R}^2$: $R_\theta = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$, orthogonal with $\det = 1$. Eigenvalues are $e^{\pm i \theta}$, on the unit circle. Element of $SO(2)$ for any $\theta$.

Reflections of $\mathbb{R}^2$: $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, etc. Orthogonal with $\det = -1$. Elements of $O(2) \setminus SO(2)$.

The diagonal unitary $\operatorname{diag}(e^{i \alpha_1}, \ldots, e^{i \alpha_n})$ over $\mathbb{C}$ is unitary, normal, with eigenvalues $e^{i \alpha_j}$ on the unit circle.

A canonical $2 \times 2$ unitary over $\mathbb{C}$: the **Hadamard matrix**
$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$$
Check: $H^* H = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I$. Also $H^2 = I$, so $H = H^{-1} = H^*$ — self-adjoint and unitary, an involution. This is the single-qubit Hadamard gate in quantum computing.

The **Pauli matrices** $\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $\sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$, $\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ are all self-adjoint and unitary (also involutions). They are basic building blocks of two-state quantum systems.

A unitary that is not self-adjoint: the **shift on $\mathbb{C}^n$**, $T(z_1, \ldots, z_n) = (z_n, z_1, \ldots, z_{n-1})$ (cyclic permutation). Its matrix is a permutation matrix, hence unitary. Eigenvalues are $n$-th roots of unity.

A non-example: $T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. Not unitary (the columns are not orthonormal: $(1, 0)$ and $(1, 1)$ are not orthogonal). Determinant $1$ but not in $SL_2$ subgroup-of-$U$, so not unitary.

A subtle non-example: $T = \begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix}$. Determinant $1$. Is normal (diagonal). But not unitary: the eigenvalues are $2$ and $1/2$, not on the unit circle. It is in $\operatorname{SL}_2(\mathbb{R})$ but not in $\operatorname{SO}(2)$.

A corollary: if $T$ is unitary then $\det T$ has modulus $1$. (Use $|\det T|^2 = \det T \cdot \overline{\det T} = \det T \cdot \det T^* = \det(T T^*) = \det I = 1$.) Over $\mathbb{C}$, $\det T$ is on the unit circle of $\mathbb{C}$; over $\mathbb{R}$, $\det T = \pm 1$.

Another corollary: the eigenvalues of a unitary operator have modulus $1$. (Shown above; this is part of the spectral characterisation.)

A third corollary: every unitary $T$ over $\mathbb{C}$ has the form $T = e^{iH}$ for some self-adjoint $H$. (Use the spectral theorem to write $T = \sum e^{i\theta_j} P_j$, then set $H = \sum \theta_j P_j$.) This is the Lie-theoretic statement that the unitary group is connected (over $\mathbb{C}$) and that the exponential map $\mathfrak{u}(n) \to U(n)$ — extended by Cayley-like transforms — is surjective.

**Calibration check.** Verify these:
1. The Pauli $\sigma_y$ is self-adjoint, unitary, has $\sigma_y^2 = I$, and has eigenvalues $\pm 1$. (Conjugate transpose: $\sigma_y^* = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \sigma_y$. Squared: $\sigma_y^2 = I$ by direct computation. Eigenvalues: characteristic polynomial $\lambda^2 - 1$.)
2. Every unitary $T$ on $\mathbb{C}^n$ has $|\det T| = 1$.
3. The product of two unitaries is unitary. (Use $(UV)^* (UV) = V^* U^* U V = V^* V = I$.)

If these check out, the definition is in your hands.

---

# Unlocked by This

> [!tip] Lorentz Group $O(1, 3)$ and Special Relativity *(from Physics)*
> Replace the positive-definite inner product on $\mathbb{R}^4$ with the **indefinite Minkowski form** $\eta(v, w) = -v^0 w^0 + v^1 w^1 + v^2 w^2 + v^3 w^3$ (see [[Def - Minkowski Space and the Metric]]). The linear maps preserving $\eta$ form the **[[Def - The Lorentz Group|Lorentz group]]** $O(1, 3)$ — the construction defining the orthogonal group, performed for the indefinite signature $(1, 3)$ instead of $(4, 0)$. The defining relation is $\Lambda^t \eta \Lambda = \eta$, structurally identical to $U^* U = I$ with $\eta$ in place of $I$. The proof that $O(1, 3)$ is a Lie group of dimension $6$ runs exactly like the proof that $O(4)$ is a Lie group of dimension $6$. The connected component of the identity, $SO^+(1, 3)$, is the **proper orthochronous Lorentz group** — the symmetry group of special relativity.

> [!tip] Quantum Computing and Unitary Gates *(from Physics / Computer Science)*
> In quantum computing, the state of $n$ qubits is a unit vector in $\mathbb{C}^{2^n}$, and every quantum *gate* is a unitary operator on $\mathbb{C}^{2^n}$. Single-qubit gates are $2 \times 2$ unitaries (Hadamard $H$, phase gates, Pauli gates, rotations); two-qubit gates are $4 \times 4$ unitaries (controlled-NOT, controlled-Z, SWAP). The Solovay–Kitaev theorem says any single-qubit unitary can be approximated to any desired precision using a finite gate set, with the number of gates polylog in the precision. Universal quantum computation requires a gate set that generates a dense subgroup of $U(2^n)$. The unitarity of quantum gates is what makes quantum computing **reversible**: every unitary $U$ has an inverse $U^*$ implementable by another quantum gate, in contrast with classical computation where many-to-one operations (like AND) lose information.

> [!tip] Special Orthogonal Group $SO(n)$ as the Rotation Group *(from Lie Theory)*
> The special orthogonal group $SO(n) = \{T \in O(n) : \det T = 1\}$ is the connected component of $O(n)$ containing the identity, and it is the **group of rotations of $\mathbb{R}^n$**. For $n = 2$, $SO(2)$ is the unit circle, abelian. For $n = 3$, $SO(3)$ is the rotations of three-space, a $3$-dimensional Lie group with the famous topology of $\mathbb{RP}^3$ (and hence not simply connected — its double cover $\operatorname{Spin}(3) \cong SU(2)$ is the universal cover, related to the "rotation by $720^\circ$" phenomenon of spin-$1/2$ particles). The Lie algebra $\mathfrak{so}(3)$ is the space of antisymmetric $3 \times 3$ matrices, isomorphic to $\mathbb{R}^3$ with the cross product as Lie bracket. Every classical mechanical system with rotational symmetry has $SO(3)$ as part of its symmetry group, and the angular momentum operators are the generators of $\mathfrak{so}(3)$.

> [!tip] The Quantum Fourier Transform *(from Quantum Computing)*
> The discrete Fourier transform matrix $F \in U(\mathbb{C}^n)$ with $F_{jk} = \frac{1}{\sqrt{n}} e^{2\pi i jk / n}$ is unitary. The **quantum Fourier transform** implements $F$ as a quantum circuit using $O(\log^2 n)$ gates on $\log n$ qubits — exponentially faster than the classical FFT. This speedup is the engine of Shor's factoring algorithm and of quantum algorithms for the hidden subgroup problem. The fact that $F$ is unitary is what makes its quantum implementation possible (only unitaries can be quantum gates) and is what links classical Fourier analysis to quantum computation.
