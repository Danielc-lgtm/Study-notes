---
type: definition
subject: spinors
prereqs:
  - "Def - Vector Space"
  - "Def - Bilinear Form"
tags: [geometry, spinors, lie-groups, quantum-mechanics]
---

# Notation

The **Pauli matrices** are denoted $\sigma_1, \sigma_2, \sigma_3$ (or $\sigma_x, \sigma_y, \sigma_z$ in physics texts). The identity is $I$ or $\sigma_0$. The shorthand $\vec\sigma = (\sigma_1, \sigma_2, \sigma_3)$ is the *vector of Pauli matrices*, and for $\vec a \in \mathbb{R}^3$ we write $\vec\sigma \cdot \vec a = \sum_j \sigma_j a^j$. The Levi-Civita symbol $\epsilon_{jkl}$ is the totally antisymmetric tensor on three indices with $\epsilon_{123} = 1$, and $\delta_{jk}$ is the Kronecker delta. The anticommutator is $\{A, B\} = AB + BA$; the commutator is $[A, B] = AB - BA$. The trace pairing $\langle A, B\rangle = \tfrac{1}{2}\mathrm{tr}(A^\dagger B)$ is the Hilbert–Schmidt inner product on $2 \times 2$ complex matrices.

---

# Axiom Motivation

The Pauli matrices are *forced* on us as soon as we ask the following question: **what is the smallest associative algebra of $n \times n$ matrices containing three anticommuting square roots of the identity?** The answer is the $2 \times 2$ complex matrix algebra $M_2(\mathbb{C})$, and the three required matrices are uniquely determined (up to choice of basis) to be the Pauli matrices.

To see why this is the natural starting point, take a step back. We want to construct a "linear representation" of rotations of $\mathbb{R}^3$ — a way of associating a matrix to each rotation, such that composing rotations corresponds to multiplying matrices. The infinitesimal rotations form the Lie algebra $\mathfrak{so}(3)$ of antisymmetric $3 \times 3$ real matrices, with bracket $[E_j, E_k] = \epsilon_{jkl}E_l$. We could try to represent this on $\mathbb{R}^3$ itself (the *vector representation*, where the rotation $R$ acts as $\vec x \mapsto R\vec x$), but that does not give us anything new. The *smallest* nontrivial representation we have not yet seen is on $\mathbb{C}^2$ — a $2$-dimensional complex space. For an $\mathfrak{su}(2)$-representation on $\mathbb{C}^2$ we need three matrices $J_1, J_2, J_3$ satisfying $[J_j, J_k] = i\epsilon_{jkl}J_l$ (the $i$ enters because anti-Hermitian matrices in $\mathfrak{su}(2)$ are $-i$ times Hermitian matrices in physical observables). It turns out — and this is the content of $\mathfrak{su}(2) \cong \mathfrak{so}(3)$ — that this representation exists and is unique up to isomorphism, with $J_j = \tfrac{1}{2}\sigma_j$ and the $\sigma_j$ the Pauli matrices.

What makes the Pauli matrices special, beyond just realizing $\mathfrak{su}(2)$, is that they simultaneously satisfy a *second* algebraic relation: $\{\sigma_j, \sigma_k\} = 2\delta_{jk}I$. This is the **Clifford relation** for the quadratic form $|\cdot|^2$ on $\mathbb{R}^3$, and it says: the Pauli matrices are square roots of the identity that anti-commute with each other. The pair of relations $[\sigma_j, \sigma_k] = 2i\epsilon_{jkl}\sigma_l$ and $\{\sigma_j, \sigma_k\} = 2\delta_{jk}I$ packages into the single product identity $\sigma_j\sigma_k = \delta_{jk}I + i\epsilon_{jkl}\sigma_l$. This is the operational form of the Pauli algebra, and is what makes every spinor calculation in $\mathbb{R}^3$ tractable.

Why is it impossible to have *real* $2 \times 2$ matrices satisfying $\{A_j, A_k\} = 2\delta_{jk}I$? The trace of $A_j^2 = I$ is $2$, and since $\det(A_j) = \pm 1$, $A_j$ has eigenvalues $\pm 1$. So $A_j$ is diagonalizable over $\mathbb{R}$ — but if both eigenvalues are $\pm 1$, $A_j$ is symmetric. Two symmetric matrices that anticommute must be simultaneously diagonalisable in some sense, which contradicts the existence of three independent ones in $\mathbb{R}^{2 \times 2}$ (only $4$-dimensional). The escape route is to allow *complex* matrices: $\sigma_2$ has imaginary entries, and the three Pauli matrices fit comfortably inside $M_2(\mathbb{C})$, which is $8$-real-dimensional and easily accommodates them along with $I$, $\sigma_1\sigma_2 = i\sigma_3$, etc.

A physical motivation for the same construction: in quantum mechanics, observables are Hermitian operators, and the spin-$1/2$ angular momentum is described by three Hermitian operators $S_x, S_y, S_z$ satisfying $[S_j, S_k] = i\hbar\epsilon_{jkl}S_l$. The smallest representation is $2$-dimensional (corresponding to the two spin states of an electron, $|\uparrow\rangle$ and $|\downarrow\rangle$), and $S_j = \tfrac{\hbar}{2}\sigma_j$. Pauli wrote these down in 1927 in his work on the electron's spin, and they have carried his name ever since.

---

# The Definition

The **Pauli matrices** are the three $2 \times 2$ complex Hermitian matrices
$$\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$
They are traceless ($\mathrm{tr}\sigma_j = 0$), Hermitian ($\sigma_j^\dagger = \sigma_j$), and unitary ($\sigma_j^{-1} = \sigma_j$). They satisfy the **product identity**
$$\sigma_j \sigma_k = \delta_{jk} I + i\epsilon_{jkl}\sigma_l,$$
which decomposes into the **commutator (Lie algebra) relation**
$$[\sigma_j, \sigma_k] = 2i\epsilon_{jkl}\sigma_l$$
and the **anticommutator (Clifford) relation**
$$\{\sigma_j, \sigma_k\} = 2\delta_{jk} I.$$

The product of all three is $\sigma_1\sigma_2\sigma_3 = iI$.

---

# Categorical / Structural Definition

The Pauli matrices, together with $I$, form an orthonormal basis (with respect to the Hilbert–Schmidt inner product $\langle A, B\rangle = \tfrac{1}{2}\mathrm{tr}(A^\dagger B)$) of the *real* vector space of $2 \times 2$ Hermitian complex matrices, which is $4$-dimensional over $\mathbb{R}$. As an algebra over $\mathbb{R}$, the span of $\{I, \sigma_1, \sigma_2, \sigma_3\}$ closed under products generates all of $M_2(\mathbb{C}) = \mathbb{C}^{2 \times 2}$, which is $8$-dimensional over $\mathbb{R}$.

The structural perspective: the Pauli matrices realize the **Clifford algebra** $\mathrm{Cl}(\mathbb{R}^3, |\cdot|^2)$ as $M_2(\mathbb{C})$. The defining relation $\sigma_j^2 = I = |e_j|^2 I$ (for $\{e_j\}$ the standard basis of $\mathbb{R}^3$) plus the anticommutation $\sigma_j \sigma_k = -\sigma_k\sigma_j$ ($j \neq k$) is precisely the Clifford relation $\{e_j, e_k\} = 2\delta_{jk} I$. The eight basis elements $\{I, \sigma_1, \sigma_2, \sigma_3, \sigma_1\sigma_2, \sigma_2\sigma_3, \sigma_3\sigma_1, \sigma_1\sigma_2\sigma_3\}$ form a basis of $M_2(\mathbb{C}) = \mathrm{Cl}(\mathbb{R}^3, |\cdot|^2)$ over $\mathbb{R}$. See [[Def - Clifford Algebra]] for the general construction.

Equivalently, the Pauli matrices give the unique (up to unitary equivalence) irreducible representation of the [[Def - Pin and Spin Groups|spin group]] $\mathrm{Spin}(3) = SU(2)$ on $\mathbb{C}^2$ — they are the generators of the $\mathfrak{spin}(3) = \mathfrak{su}(2)$ Lie algebra in this representation, with $J_j = \tfrac{1}{2}\sigma_j$ (factor of $\tfrac{1}{2}$ because spin is half-integer).

---

# Relate to Other Fields / Compression

The Pauli matrices appear in three guises that look distinct but are facets of the same object:

1. **Lie algebra basis for $\mathfrak{su}(2)$.** The matrices $\tfrac{i}{2}\sigma_j$ form a real basis for the Lie algebra $\mathfrak{su}(2)$ of traceless anti-Hermitian $2 \times 2$ complex matrices, with bracket $[\tfrac{i}{2}\sigma_j, \tfrac{i}{2}\sigma_k] = -\tfrac{1}{4}[\sigma_j, \sigma_k] = -\tfrac{i}{2}\epsilon_{jkl}\sigma_l = \epsilon_{jkl}(\tfrac{i}{2}\sigma_l)$ — exactly the structure constants of $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$. See [[Ex - The Lie Algebra of SO(3) is Antisymmetric Matrices]].

2. **Clifford-algebra generators for $\mathrm{Cl}(\mathbb{R}^3)$.** The anticommutation $\{\sigma_j, \sigma_k\} = 2\delta_{jk}I$ is the Clifford relation for the standard Euclidean form on $\mathbb{R}^3$, and the algebra generated by $\{\sigma_1, \sigma_2, \sigma_3\}$ inside $M_2(\mathbb{C})$ is $\mathrm{Cl}(3, 0) = M_2(\mathbb{C})$. See [[Ex - Pauli Matrices Generate Cl(R^3)]].

3. **Quantum-mechanical spin operators.** $\vec S = \tfrac{\hbar}{2}\vec\sigma$ are the spin angular momentum operators for a spin-$1/2$ particle (electron, proton, neutron, neutrino). The eigenvalues $\pm\tfrac{\hbar}{2}$ of $S_z = \tfrac{\hbar}{2}\sigma_3$ are the *spin up / spin down* states.

**True name:** The Pauli matrices are *the standard 2-dimensional irreducible representation of the Clifford algebra of Euclidean $\mathbb{R}^3$, or equivalently of the Lie algebra $\mathfrak{su}(2)$.* All three descriptions above unfold from this single statement. The factor of $\tfrac{1}{2}$ relating them to physical spin is essentially a unit-system choice: with the convention $\vec\sigma$ for the matrices and $\vec J = \tfrac{i}{2}\vec\sigma$ for the Lie-algebra generators, the central identity $\sigma_j\sigma_k = \delta_{jk}I + i\epsilon_{jkl}\sigma_l$ encodes both the Clifford and the Lie structure at once.

The matrices appear, less obviously, in many other contexts: as the **bosonic-fermionic coordinates** in supersymmetric quantum mechanics; as the **generators of the qubit gates** $X = \sigma_1$, $Y = \sigma_2$, $Z = \sigma_3$ in quantum computing; as the **isospin matrices** in nuclear physics (where they act on the $(p, n)$ proton-neutron doublet rather than spin states); as the **Wess–Zumino matrices** in 2-dimensional conformal field theory.

---

# Examples / Corollaries

The Pauli matrices are concrete enough that all the structure can be verified by direct computation. Several key examples:

**Example 1: Squaring.** $\sigma_j^2 = I$ for each $j$, as direct calculation shows. This is the Clifford relation $\sigma_j^2 = |e_j|^2 I = I$ in this Euclidean signature.

**Example 2: The Pauli identity for products.** For any two vectors $\vec a, \vec b \in \mathbb{R}^3$,
$$(\vec\sigma \cdot \vec a)(\vec\sigma \cdot \vec b) = (\vec a \cdot \vec b)I + i\vec\sigma \cdot (\vec a \times \vec b).$$
This follows from $\sigma_j\sigma_k = \delta_{jk}I + i\epsilon_{jkl}\sigma_l$ multiplied by $a^j b^k$: the symmetric part of $\delta_{jk}a^jb^k$ gives $\vec a \cdot \vec b$, and the antisymmetric part $i\epsilon_{jkl}\sigma_l a^j b^k$ gives $i\vec\sigma \cdot (\vec a \times \vec b)$. As a consequence, for a unit vector $\hat n$, $(\vec\sigma\cdot \hat n)^2 = I$.

**Example 3: Exponentiation.** Using $(\vec\sigma\cdot\hat n)^2 = I$:
$$\exp(i\theta \vec\sigma\cdot\hat n) = \cos\theta \cdot I + i\sin\theta \cdot \vec\sigma\cdot\hat n.$$
This is the generic element of $SU(2)$ near the identity, parameterizing a "half rotation" — the corresponding $SO(3)$ rotation is by angle $2\theta$ about the axis $\hat n$. See [[Thm - SU(2) is the Double Cover of SO(3)]] for the full statement.

**Example 4: Trace pairings.** $\mathrm{tr}(\sigma_j) = 0$, $\mathrm{tr}(\sigma_j\sigma_k) = 2\delta_{jk}$, $\mathrm{tr}(\sigma_j\sigma_k\sigma_l) = 2i\epsilon_{jkl}$. These let one extract the coefficients of any $2 \times 2$ Hermitian matrix expanded in the Pauli basis: $A = \tfrac{1}{2}\mathrm{tr}(A) I + \tfrac{1}{2}\sum_j \mathrm{tr}(A\sigma_j)\sigma_j$.

**Non-example: Real $2 \times 2$ matrices satisfying the Clifford relation.** No three real symmetric $2 \times 2$ matrices can simultaneously satisfy $\{A_j, A_k\} = 2\delta_{jk}I$. The reason: the space of real symmetric $2 \times 2$ matrices is $3$-dimensional, so any three independent such matrices would span the whole space, including $\mathrm{diag}(1, -1) = \sigma_3$ — but $\sigma_3^2 = I$ and anticommutation with another symmetric matrix $A$ would force $A$ off-diagonal with zero diagonal entries, then $A^2 = I$ forces $A_{12}A_{21} = 1$ and $A_{12}^2 = A_{21}^2$, so $A_{12} = A_{21} = \pm 1$. There are only two such matrices, contradicting the requirement of three.

**Non-example: $4 \times 4$ Pauli analogues.** The relations $\{P_j, P_k\} = 2\delta_{jk}I$ with $P_j \in M_4(\mathbb{C})$ have many solutions, but they decompose as direct sums of the standard $2 \times 2$ Pauli matrices. The smallest *irreducible* solution is $2 \times 2$. In Minkowski signature one needs $4 \times 4$: the Dirac matrices $\gamma^\mu$ are the *minimal* representation of $\mathrm{Cl}(1, 3)$ because $\mathrm{Cl}(1, 3) \otimes \mathbb{C} \cong M_4(\mathbb{C})$. See [[Def - Dirac Gamma Matrices]].

**Calibration check.** A reader who has understood the Pauli matrices should be able to verify the following without consulting references: (i) compute $\sigma_1 \sigma_2 \sigma_3$ explicitly and confirm it equals $iI$; (ii) verify $\exp(i\pi\sigma_3/2) = i\sigma_3$ by series expansion; (iii) check that $\det(\vec x \cdot \vec\sigma) = -|\vec x|^2$ for $\vec x \in \mathbb{R}^3$. If any of these is unclear, return to Example 2 and re-derive from $\sigma_j\sigma_k = \delta_{jk}I + i\epsilon_{jkl}\sigma_l$.

---

# Unlocked by This

> [!tip] Pauli Equation *(from Nonrelativistic Quantum Mechanics)*
> The **Pauli equation** is the nonrelativistic Schrödinger equation for a spin-$1/2$ particle in an electromagnetic field, with the two-component wave function $\psi \in L^2(\mathbb{R}^3, \mathbb{C}^2)$ and Hamiltonian $H = \tfrac{1}{2m}(\vec p - e\vec A)^2 + e\Phi - \tfrac{e\hbar}{2m}\vec\sigma\cdot\vec B$. The last term is the **Pauli term**, coupling the spin to the magnetic field $\vec B$; the gyromagnetic ratio $g = 2$ emerges automatically as the *nonrelativistic limit* of the Dirac equation, and is one of the early experimental confirmations of Dirac theory. The Pauli equation is the bridge between the abstract Pauli matrices and the concrete spin physics of atoms, where it explains the Zeeman effect, the Stern–Gerlach experiment, and the structure of magnetic moments.

> [!tip] Quantum Computing and Qubits *(from Quantum Information Theory)*
> A **qubit** is a quantum-mechanical 2-state system, i.e., a unit vector in $\mathbb{C}^2$. The Pauli matrices are the three basic single-qubit gates: $X = \sigma_1$ is the bit-flip, $Z = \sigma_3$ is the phase-flip, $Y = \sigma_2$ is their product. Together with the Hadamard gate $H = \tfrac{1}{\sqrt 2}(\sigma_1 + \sigma_3)$ and the phase gate $S = \mathrm{diag}(1, i)$, they generate the **Clifford group** — the group of unitaries that map Pauli operators to Pauli operators under conjugation. The structure theorem here is the **Gottesman–Knill theorem**: quantum circuits built only from Clifford gates can be efficiently simulated classically, and so a quantum computational advantage requires non-Clifford gates (typically $T = \mathrm{diag}(1, e^{i\pi/4})$). This is one of the deepest places where the Pauli algebra's structure controls computational complexity.

> [!tip] Bloch Sphere Representation of Pure States
> The pure states of a single qubit (unit vectors in $\mathbb{C}^2$ modulo global phase) form a $2$-sphere $S^2$, the **Bloch sphere**. The map is $\psi \mapsto \vec n$ where $\vec n = \langle\psi|\vec\sigma|\psi\rangle$ is the expectation value of the Pauli vector; the surface of the unit ball corresponds to pure states, and the interior to mixed states (density matrices $\rho = \tfrac{1}{2}(I + \vec n \cdot \vec\sigma)$ with $|\vec n| \leq 1$). The Bloch sphere makes the topological aspect of $SU(2) \to SO(3)$ vivid: rotations of $\mathbb{R}^3$ (rotations of the Bloch sphere) are realized by $SU(2)$ acting on $\psi$, with the same $4\pi$-periodicity. The fact that one full rotation in $SO(3)$ maps $\psi \to -\psi$ corresponds to the antipodal identification.
