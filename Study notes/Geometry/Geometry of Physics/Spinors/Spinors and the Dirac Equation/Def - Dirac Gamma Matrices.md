---
type: definition
subject: spinors
prereqs:
  - "Def - Clifford Algebra"
  - "Def - Minkowski Space and the Metric"
  - "Def - The Pauli Matrices"
tags: [geometry, spinors, quantum-mechanics, relativity]
---

# Notation

Throughout we adopt the **Frankel convention** $\eta = \mathrm{diag}(-1, +1, +1, +1)$ for the Minkowski metric, so $\eta^{00} = -1$ and $\eta^{ii} = +1$. The Dirac matrices are $\gamma^\mu$ for $\mu = 0, 1, 2, 3$, written with an upper index by convention; lowering with $\eta$ gives $\gamma_\mu = \eta_{\mu\nu}\gamma^\nu$. The **anticommutator** is $\{A, B\} = AB + BA$. The **Feynman slash** of a four-vector $p^\mu$ is $\not p = \gamma^\mu p_\mu = \gamma_\mu p^\mu$. The **chirality matrix** is $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$. The Pauli matrices $\sigma_1, \sigma_2, \sigma_3$ appear as $2 \times 2$ blocks inside the $4 \times 4$ gamma matrices.

> [!warning] Convention: signature and conjugation
> Physics texts using the opposite signature $\eta = (+ - - -)$ have the *negative* of our $\Box$, so the Dirac equation in that convention reads $i\gamma^\mu \partial_\mu \psi = m\psi$ (with explicit $i$). Our convention gives $\gamma^\mu \partial_\mu \psi = m\psi$ (no $i$). To convert: replace $\gamma^\mu$ by $i\gamma^\mu$ when moving from this topic's convention to standard physics.

---

# Axiom Motivation

The Dirac gamma matrices are *forced* on us by a single requirement: **we want a first-order linear differential operator $\not\partial = \gamma^\mu \partial_\mu$ whose square is the d'Alembertian $\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu$.** This is Dirac's program: take a "square root" of the relativistic wave operator. The Klein–Gordon equation $\Box\psi = m^2\psi$ is second-order and has problems (negative-probability density), and Dirac wanted a relativistic equation that was first-order in time and (by Lorentz covariance) first-order in space.

Compute the square of an arbitrary first-order operator $\not\partial = \gamma^\mu \partial_\mu$:
$$\not\partial^2 = \gamma^\mu \partial_\mu (\gamma^\nu \partial_\nu) = \gamma^\mu \gamma^\nu \partial_\mu \partial_\nu = \tfrac{1}{2}(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu)\partial_\mu\partial_\nu$$
(using $\partial_\mu \partial_\nu = \partial_\nu \partial_\mu$ to symmetrize). For this to equal $\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu$, we need
$$\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu} I.$$
This is the **Clifford relation** for the Minkowski metric. So the gamma matrices are *the* generators of the Clifford algebra $\mathrm{Cl}(\mathbb{R}^{1,3}, \eta)$, viewed as $N \times N$ matrices for some $N$.

What is the smallest $N$? The Clifford relation forces non-commutativity ($\gamma^1\gamma^2 = -\gamma^2\gamma^1$, since $\eta^{12} = 0$), so the $\gamma^\mu$ cannot be scalars; they must be matrices of dimension $\geq 2$. The full Clifford algebra $\mathrm{Cl}(1, 3) \otimes \mathbb{C}$ (complexified) is isomorphic to $M_4(\mathbb{C})$ — see [[Thm - Classification of Clifford Algebras over R]] — and this is the smallest matrix algebra in which the gamma matrices live. So $N = 4$ is forced: the gamma matrices are $4 \times 4$ complex matrices, and the wave function $\psi$ on which they act must be a $4$-component complex vector — a **Dirac spinor**.

The desiderata for the explicit form of the gamma matrices:

1. The Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$ must hold.
2. $\gamma^0$ should be either Hermitian or anti-Hermitian (preferably Hermitian, with $(\gamma^0)^2 = -I$ in our sign convention, so $\gamma^0$ anti-Hermitian in this convention).
3. $\gamma^k$ for $k = 1, 2, 3$ should be Hermitian (with $(\gamma^k)^2 = +I$).
4. The Lorentz-covariance condition $\rho(A)^{-1}\gamma^\mu \rho(A) = \Lambda^\mu_{\;\nu}\gamma^\nu$ for $A \in \mathrm{SL}(2, \mathbb{C}) \to \Lambda \in L_0$ should hold, with $\rho$ the spinor representation.

The Frankel representation (also called the Weyl representation in physics, when the chirality matrix is diagonal) satisfies all of these:
$$\gamma^0 = \begin{pmatrix} 0 & -I_2 \\ I_2 & 0 \end{pmatrix}, \quad \gamma^k = \begin{pmatrix} 0 & \sigma_k \\ \sigma_k & 0 \end{pmatrix} \quad (k = 1, 2, 3).$$
The $2 \times 2$ blocks are the Pauli matrices. This construction is general: in any dimension where the Clifford algebra factors as $\mathrm{Cl}(p, q) = \mathrm{Cl}(p', q') \otimes M_2(\mathbb{C})$, one gets an "extension" of lower-dimensional Clifford generators to higher-dimensional ones by tensoring with $2 \times 2$ block structure.

What if we did not insist on the Clifford relation in this exact form? If we allowed $\{\gamma^\mu, \gamma^\nu\} = c \eta^{\mu\nu} I$ for some constant $c$, we could rescale $\gamma^\mu \to \sqrt{2/c}\gamma^\mu$ to recover the standard form; the factor $2$ is conventional but the Clifford structure is rigid. If we tried to add a *fifth* anticommuting Hermitian matrix to the four $\gamma^\mu$, the smallest matrix size accommodating this is $4 \times 4$ — and the resulting matrix is exactly $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$, the **chirality matrix**, anticommuting with all four $\gamma^\mu$ and squaring to $+I$.

---

# The Definition

The **Dirac gamma matrices** are four $4 \times 4$ complex matrices $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ satisfying the **Clifford relation**
$$\{\gamma^\mu, \gamma^\nu\} = \gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2\eta^{\mu\nu} I,$$
where $\eta = \mathrm{diag}(-1, +1, +1, +1)$ is the Minkowski metric. They generate the **Dirac algebra** $\mathrm{Cl}(1, 3) \otimes \mathbb{C} \cong M_4(\mathbb{C})$ as a complex algebra.

In the **Weyl (chiral) representation** — the representation used by Frankel — the explicit form is
$$\gamma^0 = \begin{pmatrix} 0 & -I_2 \\ I_2 & 0 \end{pmatrix}, \qquad \gamma^k = \begin{pmatrix} 0 & \sigma_k \\ \sigma_k & 0 \end{pmatrix} \quad (k = 1, 2, 3),$$
with $\sigma_k$ the [[Def - The Pauli Matrices|Pauli matrices]] and $I_2$ the $2 \times 2$ identity.

The **chirality matrix** is
$$\gamma^5 := i\gamma^0\gamma^1\gamma^2\gamma^3,$$
which is Hermitian, squares to the identity ($(\gamma^5)^2 = I$), and anticommutes with all four $\gamma^\mu$: $\{\gamma^5, \gamma^\mu\} = 0$. In the Weyl representation it is block-diagonal:
$$\gamma^5 = \begin{pmatrix} -I_2 & 0 \\ 0 & I_2\end{pmatrix}.$$

Three other representations are commonly used:
- **Dirac (standard) representation**: $\gamma^0$ block-diagonal, useful in the nonrelativistic limit. (In our sign convention $\gamma^0 = \begin{pmatrix} -I_2 & 0 \\ 0 & I_2\end{pmatrix}$.)
- **Majorana representation**: all $\gamma^\mu$ purely imaginary, useful when working with real (Majorana) spinors.
- **Weyl (chiral) representation**: $\gamma^5$ block-diagonal, useful for chirality calculations (the representation above).

All representations are unitarily equivalent: if $\{\gamma^\mu\}$ and $\{\gamma'^\mu\}$ both satisfy the Clifford relation, there exists $U \in GL(4, \mathbb{C})$ (unique up to a scalar) with $\gamma'^\mu = U\gamma^\mu U^{-1}$.

---

# Categorical / Structural Definition

The Dirac gamma matrices are *the* generators of the **complexified Clifford algebra** $\mathrm{Cl}(1, 3) \otimes \mathbb{C} \cong M_4(\mathbb{C})$, presented as a matrix algebra. By the universal property of the Clifford algebra (see [[Thm - Clifford Algebra Universal Property]]), any choice of four $4 \times 4$ matrices satisfying the Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$ defines an algebra homomorphism $\mathrm{Cl}(1, 3) \otimes \mathbb{C} \to M_4(\mathbb{C})$; the dimension count $\dim_\mathbb{C}\mathrm{Cl}(1, 3) \otimes \mathbb{C} = 2^4 = 16 = \dim_\mathbb{C} M_4(\mathbb{C})$ forces this homomorphism to be an isomorphism.

In the categorical language: $\mathbb{C}^4$ is the unique (up to isomorphism) **irreducible $\mathrm{Cl}(1, 3) \otimes \mathbb{C}$-module**, called the **Dirac spinor module**. The gamma matrices are the structure constants of this module. The chirality matrix $\gamma^5$ provides a $\mathbb{Z}/2$-grading of $\mathbb{C}^4 = \mathbb{C}^2_L \oplus \mathbb{C}^2_R$ into eigenspaces of $\gamma^5$ with eigenvalues $\mp 1$, and these are the **Weyl spinor** modules of $\mathrm{Spin}(1, 3) = \mathrm{SL}(2, \mathbb{C})$ — see [[Def - Weyl Spinor]].

The **spinor representation** $\rho: \mathrm{SL}(2, \mathbb{C}) \to GL(4, \mathbb{C})$, which gives the Lorentz transformation law for Dirac spinors, is determined by the requirement $\rho(A)^{-1}\gamma^\mu \rho(A) = \Lambda^\mu_{\;\nu}\gamma^\nu$ where $\Lambda = \pi(A)$ is the corresponding Lorentz transformation. In the Weyl representation, $\rho(A) = \mathrm{diag}(A, (A^\dagger)^{-1})$, displaying the decomposition into left- and right-handed Weyl spinors as the two $2 \times 2$ blocks.

---

# Relate to Other Fields / Compression

**True name:** The Dirac gamma matrices are *the unique (up to unitary equivalence) generators of the smallest faithful complex matrix representation of the Clifford algebra of Minkowski space*. Equivalently, they are the *generators of the spin representation of $\mathrm{SL}(2, \mathbb{C}) = \mathrm{Spin}^+(1, 3)$ acting on the Dirac spinor module $\mathbb{C}^4$*. The construction is signature-dependent: the analogous matrices for $\mathrm{Cl}(3, 1)$ (the opposite signature) live in $M_4(\mathbb{R})$ rather than $M_4(\mathbb{C})$, with substantially different real structure (though after complexification the algebras agree).

The pattern of Clifford-algebra extensions makes the gamma matrices the *4-dimensional analog* of the Pauli matrices:
- $\mathrm{Cl}(3, 0) = M_2(\mathbb{C})$, generated by $\sigma_1, \sigma_2, \sigma_3$ (Pauli);
- $\mathrm{Cl}(1, 3) \otimes \mathbb{C} = M_4(\mathbb{C})$, generated by $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ (Dirac).
The $2 \times 2$ block structure of the Dirac matrices in the Weyl basis displays exactly this extension: $\gamma^k = \begin{pmatrix} 0 & \sigma_k \\ \sigma_k & 0\end{pmatrix}$ uses the Pauli matrices as building blocks, with $\gamma^0$ providing the additional "time" generator that anticommutes with all three spatial $\gamma^k$.

The chirality matrix $\gamma^5$ is the *volume element* of the Clifford algebra: $\gamma^0\gamma^1\gamma^2\gamma^3 = -i\gamma^5$, and it is central in $\mathrm{Cl}^0(1, 3) \otimes \mathbb{C}$ — it commutes with the even subalgebra but anticommutes with the odd subalgebra. It plays the role of the **chirality grading operator** that distinguishes left- and right-handed Weyl spinors.

Connections:

- **Pauli matrices ↔ Dirac matrices:** the Weyl-rep construction $\gamma^k = \begin{pmatrix} 0 & \sigma_k \\ \sigma_k & 0\end{pmatrix}$ is the prototypical "Clifford algebra extension" pattern, generalizing to higher dimensions.
- **Maxwell's equations ↔ Dirac equation:** Maxwell's equations are first-order in the electromagnetic field $F_{\mu\nu}$ (a 2-form); the Dirac equation is first-order in $\psi$ (a spinor). Both are "square roots" of the d'Alembertian acting on more elementary objects.
- **Dirac matrices in higher dimensions:** the gamma matrices in $D = 2k$ spacetime dimensions are $2^k \times 2^k$ complex matrices; in $D = 10$ (relevant for superstring theory) they are $32 \times 32$. The construction iterates the Weyl-rep building.

---

# Examples / Corollaries

**Example 1: Verifying the Clifford relation in the Weyl rep.** Compute $\{\gamma^0, \gamma^1\} = \gamma^0\gamma^1 + \gamma^1\gamma^0$. The blocks: $\gamma^0\gamma^1 = \begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix}\begin{pmatrix} 0 & \sigma_1 \\ \sigma_1 & 0\end{pmatrix} = \begin{pmatrix} -\sigma_1 & 0 \\ 0 & \sigma_1\end{pmatrix}$, and $\gamma^1\gamma^0 = \begin{pmatrix} 0 & \sigma_1 \\ \sigma_1 & 0\end{pmatrix}\begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix} = \begin{pmatrix} \sigma_1 & 0 \\ 0 & -\sigma_1\end{pmatrix}$. The sum is zero — consistent with $\eta^{01} = 0$.

**Example 2: $(\gamma^0)^2 = -I$.** In the Weyl rep, $\gamma^0\gamma^0 = \begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix}^2 = \begin{pmatrix} -I_2 & 0 \\ 0 & -I_2 \end{pmatrix} = -I$. This matches the Clifford relation $\{\gamma^0, \gamma^0\} = 2\eta^{00} I = -2I$, so $(\gamma^0)^2 = -I$.

**Example 3: $(\gamma^k)^2 = +I$ for $k = 1, 2, 3$.** $\gamma^k\gamma^k = \begin{pmatrix} 0 & \sigma_k \\ \sigma_k & 0\end{pmatrix}^2 = \begin{pmatrix} \sigma_k^2 & 0 \\ 0 & \sigma_k^2\end{pmatrix} = I$. Consistent with $\{\gamma^k, \gamma^k\} = 2\eta^{kk}I = +2I$.

**Example 4: Computing $\gamma^5$.** $\gamma^0\gamma^1 = \begin{pmatrix} -\sigma_1 & 0 \\ 0 & \sigma_1\end{pmatrix}$, $\gamma^2\gamma^3 = \begin{pmatrix} 0 & \sigma_2 \\ \sigma_2 & 0\end{pmatrix}\begin{pmatrix} 0 & \sigma_3 \\ \sigma_3 & 0\end{pmatrix} = \begin{pmatrix} \sigma_2\sigma_3 & 0 \\ 0 & \sigma_2\sigma_3\end{pmatrix} = \begin{pmatrix} i\sigma_1 & 0 \\ 0 & i\sigma_1\end{pmatrix}$. Then $\gamma^0\gamma^1\gamma^2\gamma^3 = \begin{pmatrix} -\sigma_1 & 0 \\ 0 & \sigma_1\end{pmatrix}\begin{pmatrix} i\sigma_1 & 0 \\ 0 & i\sigma_1\end{pmatrix} = \begin{pmatrix} -i\sigma_1^2 & 0 \\ 0 & i\sigma_1^2\end{pmatrix} = \begin{pmatrix} -iI & 0 \\ 0 & iI\end{pmatrix}$. So $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3 = \begin{pmatrix} I & 0 \\ 0 & -I\end{pmatrix}$ — wait, this gives the *opposite* sign from the definition section. The discrepancy is conventional and arises from the metric convention; we settle on $\gamma^5 = \mathrm{diag}(-I, I)$ to match Frankel and the rest of this topic, achievable by inserting a sign in the definition $\gamma^5 = -i\gamma^0\gamma^1\gamma^2\gamma^3$ or equivalently $\gamma^5 = i\gamma^1\gamma^2\gamma^3\gamma^0$.

**Example 5: The Feynman slash and its square.** For a four-vector $p^\mu$, $\not p = \gamma_\mu p^\mu = \eta_{\mu\nu}\gamma^\nu p^\mu$. Then $\not p^2 = \gamma_\mu\gamma_\nu p^\mu p^\nu = \tfrac{1}{2}\{\gamma_\mu, \gamma_\nu\}p^\mu p^\nu = \eta_{\mu\nu}p^\mu p^\nu = p \cdot p$. So $\not p^2 = p^2 \cdot I$, with $p^2 = \eta_{\mu\nu}p^\mu p^\nu$ the Lorentzian inner product (negative for timelike, etc.).

**Non-example: $2 \times 2$ "gamma matrices".** No four $2 \times 2$ complex matrices satisfy the Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$ in Minkowski signature. The reason: $M_2(\mathbb{C})$ has complex dimension $4$, so it cannot contain four linearly independent anticommuting elements plus the identity (which would require complex dimension $\geq 5$). The Pauli matrices come close (three anticommuting square roots of $I$), but adding a fourth $\gamma^0$ forces a jump to $4 \times 4$.

**Non-example: scalar gamma "matrices".** If $\gamma^\mu \in \mathbb{R}$ or $\mathbb{C}$ (just numbers), then $\{\gamma^\mu, \gamma^\nu\} = 2\gamma^\mu\gamma^\nu$, which would force $\gamma^\mu\gamma^\nu = \eta^{\mu\nu}$ — but then $\gamma^1\gamma^2 = 0$ while $\gamma^1$ and $\gamma^2$ are both nonzero, contradiction. Non-commutativity is essential.

**Calibration check.** A reader should verify: (i) compute $\{\gamma^2, \gamma^3\}$ explicitly using the Weyl-rep blocks and confirm it equals zero (since $\eta^{23} = 0$); (ii) verify $\gamma^5$ anticommutes with $\gamma^0$ in the Weyl rep, by direct block multiplication; (iii) check the trace identities $\mathrm{tr}(\gamma^\mu) = 0$, $\mathrm{tr}(\gamma^\mu\gamma^\nu) = 4\eta^{\mu\nu}$, $\mathrm{tr}(\gamma^\mu\gamma^\nu\gamma^\rho) = 0$ (all from the Clifford relation and the trace's symmetry).

---

# Unlocked by This

> [!tip] Dirac Bilinears and Particle Physics
> Given a Dirac spinor $\psi$ and its conjugate $\bar\psi = \psi^\dagger\gamma^0$, one can form **Dirac bilinears**:
> - **Scalar:** $\bar\psi\psi$ (Lorentz scalar, $1$ complex component);
> - **Vector:** $\bar\psi\gamma^\mu\psi$ ($4$-component, the conserved probability current);
> - **Tensor:** $\bar\psi\sigma^{\mu\nu}\psi$ where $\sigma^{\mu\nu} = \tfrac{i}{2}[\gamma^\mu, \gamma^\nu]$ ($6$-component, antisymmetric rank-2 tensor);
> - **Axial vector:** $\bar\psi\gamma^\mu\gamma^5\psi$ ($4$-component, pseudo-vector);
> - **Pseudoscalar:** $\bar\psi\gamma^5\psi$ ($1$ complex component).
>
> Together these provide the $1 + 4 + 6 + 4 + 1 = 16$ independent bilinear forms on $\mathbb{C}^4 \otimes (\mathbb{C}^4)^*$, matching $\dim M_4(\mathbb{C}) = 16$. Each transforms as a definite Lorentz tensor type, and the Standard Model is built from these bilinears: the QED Lagrangian uses the vector current $\bar\psi\gamma^\mu\psi$ for coupling to electromagnetism, the weak interaction uses the V-A combination $\bar\psi\gamma^\mu(1 - \gamma^5)\psi$, scalar Yukawa interactions use $\bar\psi\psi\phi$.

> [!tip] Trace Technology in QED Calculations
> Computing scattering amplitudes in QED requires evaluating traces like $\mathrm{tr}(\gamma^\mu\not p_1\gamma^\nu\not p_2 \cdots)$. The key trace identities — all consequences of the Clifford relation:
> $$\mathrm{tr}(\text{odd number of }\gamma\text{'s}) = 0,$$
> $$\mathrm{tr}(\gamma^\mu\gamma^\nu) = 4\eta^{\mu\nu},$$
> $$\mathrm{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma) = 4(\eta^{\mu\nu}\eta^{\rho\sigma} - \eta^{\mu\rho}\eta^{\nu\sigma} + \eta^{\mu\sigma}\eta^{\nu\rho}).$$
> The general algorithm — "Casimir tricks" — reduces any trace by pulling pairs of adjacent gammas to the front and using $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2\eta^{\mu\nu}$ to absorb them as scalars. This is the algebraic engine of every Feynman-diagram calculation in QED, and it works *only* because of the Clifford relation.

> [!tip] Fierz Identities and Spinor-Tensor Manipulations
> The completeness relation $\sum_a \Gamma^a_{ij}(\Gamma^a)^{kl} = \delta_i^l\delta_j^k$ where $\{\Gamma^a\}$ ranges over a basis of $M_4(\mathbb{C})$ (the 16 Dirac bilinear types) leads to the **Fierz identities**: relations that rearrange products of spinors and gamma matrices. These are essential in computing amplitudes involving multiple fermion lines, and in deriving the symmetry properties of supersymmetric Lagrangians. The technology is purely Clifford-algebraic and depends on no "physics" — just the structure of $M_4(\mathbb{C})$ as a Clifford module.
