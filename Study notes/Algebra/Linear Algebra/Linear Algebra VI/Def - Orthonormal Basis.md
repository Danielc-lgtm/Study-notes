---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Orthogonal and Orthonormal Vectors"
  - "Def - Basis"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional inner product space over $\mathbf{F}$, with $n = \dim V$. An orthonormal basis is denoted $e_1, \dots, e_n$. The Kronecker delta $\delta_{jk}$ equals $1$ if $j = k$ and $0$ otherwise. The parent topic page is [[Linear Algebra VI — §6 Inner Product Spaces]].

---

# Axiom Motivation

We have a finite-dimensional inner product space $V$ and want to choose a basis $e_1, \dots, e_n$ that makes every inner-product computation maximally clean. What does "maximally clean" mean?

Consider expressing an arbitrary vector $v$ as $v = \sum_k a_k e_k$. For a general basis, computing the coefficients $a_k$ requires solving a linear system: $\langle v, e_j\rangle = \sum_k a_k \langle e_k, e_j\rangle$, where the matrix $G_{jk} = \langle e_k, e_j\rangle$ (the **Gram matrix** of the basis) appears. Solving for $a_k$ requires inverting the Gram matrix. Now ask: what choice of basis makes the Gram matrix the simplest possible — namely, the identity matrix? The answer is: a basis in which $\langle e_j, e_k\rangle = \delta_{jk}$, i.e., the basis is an [[Def - Orthogonal and Orthonormal Vectors|orthonormal list]]. With such a basis, the coefficient formula collapses to $a_k = \langle v, e_k\rangle$ — a single inner product per coordinate, with no system to solve.

This is the entire motivation: an orthonormal basis is the basis in which the matrix of the inner product, restricted to the basis vectors, is the identity. Every clean computation in the chapter — expansion coefficients $a_k = \langle v, e_k\rangle$; norm-squared $\|v\|^2 = \sum |a_k|^2$ (Parseval); inner product $\langle v, w\rangle = \sum a_k \bar b_k$; orthogonal projection $P_U v = \sum_{k \leq m} \langle v, e_k\rangle e_k$ — gets its cleanness from the choice of orthonormal basis. A non-orthonormal basis can also be used, but every formula picks up Gram-matrix corrections that obscure the geometry.

The existence of an orthonormal basis is non-trivial: it is the conclusion of the [[Thm - Gram-Schmidt Procedure|Gram-Schmidt procedure]], which takes any basis and produces an orthonormal one. Existence is therefore *constructive*: you choose any basis, apply Gram-Schmidt, and get an orthonormal basis with the same partial spans. The further fact that every orthonormal list can be *extended* to an orthonormal basis (also via Gram-Schmidt applied to an extension of the list to a basis) makes orthonormal bases supremely flexible.

The motivation is summarised by a single dictum: **work in an orthonormal basis whenever the inner product is in play.** If you do not have one, Gram-Schmidt produces one cheaply, and every subsequent computation is dramatically simpler.

---

# The Definition

An **orthonormal basis** of a finite-dimensional inner product space $V$ is a list $e_1, \dots, e_n$ in $V$ that is both:

1. an [[Def - Orthogonal and Orthonormal Vectors|orthonormal list]] — $\langle e_j, e_k\rangle = \delta_{jk}$ for all $j, k$, and
2. a [[Def - Basis|basis]] of $V$ — the list is linearly independent and spans $V$.

Equivalently, by the corollary that orthonormal lists are automatically linearly independent (see [[Ex - Orthonormal lists are linearly independent]]), an orthonormal basis is an orthonormal list of length $\dim V$.

The defining feature of an orthonormal basis is that the matrix of the inner product, restricted to the basis vectors, is the identity. Concretely, for $v = \sum_k a_k e_k$ and $w = \sum_k b_k e_k$:

$$
\langle v, w\rangle = \sum_{k=1}^n a_k \bar b_k, \qquad \|v\|^2 = \sum_{k=1}^n |a_k|^2.
$$

The coefficients satisfy

$$
a_k = \langle v, e_k\rangle \qquad \text{for each } k = 1, \dots, n,
$$

the **orthonormal expansion formula**. The identity $\|v\|^2 = \sum |\langle v, e_k\rangle|^2$ is **Parseval's identity**.

---

# Categorical / Structural Definition

An orthonormal basis is an isomorphism of inner product spaces $V \cong \mathbf{F}^n$, where $\mathbf{F}^n$ is equipped with the Euclidean inner product. The isomorphism sends $e_k \mapsto $ standard $k$-th basis vector, and the inner product is preserved by construction. This is the precise sense in which an orthonormal basis is a coordinate system: it identifies $V$ with $\mathbf{F}^n$ in a way that respects all the inner-product geometry.

From this perspective, **two orthonormal bases differ by a unitary transformation**. If $e_1, \dots, e_n$ and $f_1, \dots, f_n$ are both orthonormal bases of $V$, the change-of-basis map $e_k \mapsto f_k$ extends linearly to an isometry $V \to V$. The set of orthonormal bases of $V$ is therefore a (left or right) coset of the unitary group $U(V)$ — or of the orthogonal group $O(V)$ when $\mathbf{F} = \mathbb{R}$.

---

# Relate to Other Fields / Compression

An orthonormal basis is the discrete-dimension analogue of an **orthonormal set in a Hilbert space** that is complete in the sense of forming a maximal orthonormal set. In separable infinite-dimensional Hilbert spaces, orthonormal bases are *countable* and the expansion $v = \sum_k \langle v, e_k\rangle e_k$ is an infinite series converging in norm (the truncations being orthogonal projections onto finite-dimensional subspaces, with errors controlled by [[Thm - Best Approximation by Orthogonal Projection|Bessel's inequality]]). The basic structure transfers verbatim modulo the convergence questions.

**True name:** an orthonormal basis is a linear isomorphism $V \cong \mathbf{F}^n$ that preserves the inner product — equivalently, a unitary identification of $V$ with the standard inner product space $\mathbf{F}^n$. The set of orthonormal bases is the unitary group (or orthogonal group) acting transitively on any one of them.

---

# Examples / Corollaries

**Is an instance: the standard basis $e_1, \dots, e_n$ of $\mathbf{F}^n$.** With the Euclidean inner product, $\langle e_j, e_k\rangle = \delta_{jk}$ by definition. This is the orthonormal basis of $\mathbf{F}^n$ that is taken for granted unless one is told otherwise.

**Is an instance: $(\cos\theta, \sin\theta), (-\sin\theta, \cos\theta)$ in $\mathbb{R}^2$.** A rotation of the standard basis by angle $\theta$. Every orthonormal basis of $\mathbb{R}^2$ is of this form (with possibly a reflection: $(\sin\theta, -\cos\theta)$ replacing the second vector).

**Is an instance: $\tfrac{1}{\sqrt{2}}(1, 1), \tfrac{1}{\sqrt{2}}(1, -1)$ in $\mathbb{R}^2$.** This is the $\theta = \pi/4$ case. The two vectors have norm $1$ and are orthogonal. They form an orthonormal basis "rotated by $45°$ from the standard basis".

**Is an instance: Hermite functions in $L^2(\mathbb{R})$.** The Hermite functions $h_n(x) = (2^n n! \sqrt{\pi})^{-1/2} H_n(x) e^{-x^2/2}$, where $H_n$ is the Hermite polynomial, form an orthonormal basis of $L^2(\mathbb{R})$. They are the energy eigenstates of the quantum harmonic oscillator.

**Is an instance: an orthonormal basis of $\mathcal{P}_2(\mathbb{R})$ with $\langle p, q\rangle = \int_{-1}^1 pq$.** Apply Gram-Schmidt to $1, x, x^2$: $e_1 = 1/\sqrt{2}$; $e_2 = \sqrt{3/2}\, x$; $e_3 = \sqrt{45/8}\,(x^2 - 1/3)$. These are the normalized Legendre polynomials of degree $\leq 2$. See [[Ex - Legendre polynomials from Gram-Schmidt]].

**Is NOT an instance: $(1, 0), (1, 1)$ in $\mathbb{R}^2$.** Linearly independent, hence a basis; but $\langle (1, 0), (1, 1)\rangle = 1 \neq 0$, so not orthonormal. The Gram matrix is $\begin{pmatrix}1 & 1 \\ 1 & 2\end{pmatrix}$, not the identity. Computing $\langle v, w\rangle$ in this basis would require carrying around this Gram matrix.

**Is NOT an instance: $(1, 0), (0, 2)$ in $\mathbb{R}^2$.** Orthogonal, but the second vector has norm $2$, not $1$. So this is an **orthogonal basis** (vectors pairwise orthogonal) but not an **orthonormal basis** (also requires unit-length). Normalizing the second vector to $(0, 1)$ yields the standard orthonormal basis.

**Corollary (existence of orthonormal bases).** Every finite-dimensional inner product space has an orthonormal basis. *Proof:* take any basis and apply [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]].

**Corollary (extension to a basis).** Every orthonormal list in a finite-dimensional inner product space can be extended to an orthonormal basis. *Proof:* extend the list to any basis (existence by [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]]), then apply Gram-Schmidt — the first vectors are already orthonormal, so they are unchanged.

**Corollary (Parseval's identity).** If $e_1, \dots, e_n$ is an orthonormal basis, then $\|v\|^2 = \sum_{k=1}^n |\langle v, e_k\rangle|^2$ for every $v \in V$. *Proof:* expand $v = \sum a_k e_k$ with $a_k = \langle v, e_k\rangle$ and use $\|v\|^2 = \sum |a_k|^2$ (corollary of orthonormality).

**Corollary (inner-product formula via expansion coefficients).** $\langle v, w\rangle = \sum_{k=1}^n \langle v, e_k\rangle \overline{\langle w, e_k\rangle}$ for any $v, w \in V$ and any orthonormal basis. *Proof:* expand both sides and use orthonormality.

**Calibration check.** Three verifications: (i) for $V = \mathbb{R}^2$, write down two different orthonormal bases and verify Parseval's identity for $v = (1, 2)$ in each — the sum of squared coordinates must equal $5$ regardless of the basis chosen; (ii) given the orthogonal but not orthonormal pair $(1, 1), (1, -1)$ in $\mathbb{R}^2$, normalize each to get an orthonormal basis; (iii) verify the expansion-coefficient formula for $v = (1, 2, 3)$ in the standard basis of $\mathbb{R}^3$, i.e. check $\langle v, e_k\rangle$ equals the $k$-th coordinate.

---

# Unlocked by This

> [!tip] Spectral Theorem for Self-Adjoint Operators *(from Linear Algebra VII)*
> A self-adjoint operator $T \in \mathcal{L}(V)$ on a finite-dimensional inner product space is **diagonalizable by an orthonormal basis**: there exists an orthonormal basis $e_1, \dots, e_n$ of $V$ consisting of eigenvectors of $T$, with all eigenvalues real. This is the **spectral theorem**, the central structural result for self-adjoint (and more generally normal) operators. The corresponding statement for matrices: every Hermitian matrix is unitarily diagonalizable, i.e., $H = U\,\Lambda\,U^*$ with $U$ unitary and $\Lambda$ real diagonal. Quantum-mechanical observables are self-adjoint operators on Hilbert space, and their spectral decompositions are how the theory extracts probabilities of measurement outcomes.

> [!tip] Fourier Series and Parseval/Bessel *(from Analysis)*
> The trigonometric system $\{e^{inx}/\sqrt{2\pi}\}_{n \in \mathbb{Z}}$ is an orthonormal basis of $L^2[-\pi, \pi]$ (countable, in the infinite-dimensional sense). The Fourier expansion $f = \sum c_n e^{inx}/\sqrt{2\pi}$ with $c_n = \langle f, e^{inx}/\sqrt{2\pi}\rangle$ is the infinite-dimensional analogue of the orthonormal expansion. **Parseval's identity** $\sum |c_n|^2 = \|f\|^2$ is exactly the orthonormal-basis Parseval — and **Bessel's inequality**, which holds for any orthonormal list (basis or not), specialises to a strict inequality for incomplete lists. Fourier series are the prototype for orthonormal expansion in infinite dimensions, and they are the reason $L^2$ is the natural function space for Fourier analysis.
