---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Adjoint of a Linear Map"
  - "Def - Inner Product Space"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional [[Def - Inner Product Space|inner product space]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$ with inner product $\langle \cdot, \cdot \rangle$, linear in the first slot. An [[Def - Adjoint of a Linear Map|adjoint]] of an operator $T \in \mathcal{L}(V)$ is the unique operator $T^*$ satisfying $\langle Tv, w \rangle = \langle v, T^* w \rangle$ for all $v, w \in V$. We freely interchange "operator" and "matrix" (in an orthonormal basis); the matrix of $T^*$ is then the conjugate transpose $A^*$ of the matrix $A$ of $T$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

The two synonyms for "self-adjoint" in widespread use are **Hermitian** (especially in physics, especially over $\mathbb{C}$) and **symmetric** (especially in real linear algebra). We use "self-adjoint" because it is the cleanest term and is field-agnostic.

---

# Axiom Motivation

The right way to motivate the definition is by analogy: **self-adjoint operators are to operators what real numbers are to complex numbers.** A complex number $z$ is real if and only if $z = \overline{z}$, where $\overline{\cdot}$ is complex conjugation — the unique field automorphism of $\mathbb{C}$ of order $2$ that fixes $\mathbb{R}$. The "complex conjugate" of an operator on an inner product space is its adjoint $T^*$ — also an order-$2$ involution (since $T^{**} = T$) — and the operators it fixes, $T = T^*$, are the *real* operators. The whole zoo of operator classes in this chapter is built by analogy with subsets of $\mathbb{C}$: self-adjoint operators play the role of $\mathbb{R}$, positive operators play the role of $\mathbb{R}_{\geq 0}$, unitary operators play the role of the unit circle, normal operators play the role of $\mathbb{C}$ itself.

Why is this analogy substantive and not just suggestive? Because the spectral theorem makes it literally true: the **eigenvalues of a self-adjoint operator are real** (see [[Ex - Self-adjoint operators have real eigenvalues]]) and the **eigenvalues of a unitary operator have modulus 1**. So the eigenvalue spectrum of a self-adjoint operator is a finite subset of $\mathbb{R}$ — every eigenvalue is a real number — and the operator itself, written in the spectral basis, is a real diagonal matrix. The operator behaves, on each eigenvector, like a real-number multiplication. The analogy with $\mathbb{R}$ is exact at the level of spectra.

There is a second motivation, perhaps deeper: self-adjointness is the *physically meaningful* condition. In quantum mechanics every observable — energy, momentum, position, angular momentum — is by axiom a self-adjoint operator on the Hilbert space of states. The reason the operator must be self-adjoint and not merely linear is that *measurement outcomes must be real numbers*, and the spectrum of a self-adjoint operator is real. Without self-adjointness there is no way for quantum mechanics to produce real-valued measurements, and the connection between the formalism and experiment breaks. The axiom $T = T^*$ is, from the physics side, the precise condition for an operator to deserve being called a measurement.

What if you tried to weaken the condition? Demanding only $\langle Tv, v \rangle \in \mathbb{R}$ for all $v$ — that the operator yields real "expectation values" — turns out to be equivalent to $T = T^*$ over $\mathbb{C}$ (via polarisation), but is strictly weaker over $\mathbb{R}$. The strongest form $T = T^*$ is the right uniform condition. Demanding only that the eigenvalues be real is strictly weaker still: an operator with real eigenvalues can have non-orthogonal eigenvectors (any upper-triangular real matrix with distinct entries is an example), losing the orthonormal diagonalisability that makes self-adjointness so powerful.

What if you tried to strengthen the condition? Demanding $T = T^*$ together with $T^2 = T$ gives **orthogonal projections** — the self-adjoint idempotents. Demanding $T = T^*$ together with non-negativity $\langle Tv, v \rangle \geq 0$ gives [[Def - Positive Operator|positive operators]]. Demanding $T = T^*$ together with $T^2 = I$ gives **reflections** or sign operators. Each of these strengthenings carves out an important subclass. The unstrengthened condition $T = T^*$ is the right level of generality: it is strong enough to imply the spectral theorem, weak enough to encompass all the relevant subclasses.

One more remark, particular to the real case. Over $\mathbb{R}$, "self-adjoint" and "symmetric" are synonyms — both mean $T^t = T$ for the matrix in an orthonormal basis. The distinction between them is purely notational: physicists prefer "self-adjoint" because it remains correct over $\mathbb{C}$ (where the matrix relation is $T = T^*$ with conjugation, not just $T = T^t$), while pure linear-algebra texts often prefer "symmetric" over $\mathbb{R}$. We use "self-adjoint" throughout for uniformity; if you see a real-symmetric matrix in another text, read it as a real self-adjoint operator.

---

# The Definition

An operator $T \in \mathcal{L}(V)$ is **self-adjoint** (also: **Hermitian** over $\mathbb{C}$, **symmetric** over $\mathbb{R}$) if

$$T = T^*,$$

equivalently $\langle Tv, w \rangle = \langle v, Tw \rangle$ for all $v, w \in V$.

In an orthonormal basis, this is the matrix condition $A = A^*$ (conjugate transpose): the matrix of $T$ equals its conjugate transpose. Over $\mathbb{R}$ this is the symmetric matrix condition $A = A^t$.

**Equivalent characterisations** (over $\mathbb{C}$, with $V \neq 0$):
1. $T = T^*$.
2. $\langle Tv, w \rangle = \langle v, Tw \rangle$ for all $v, w \in V$.
3. $\langle Tv, v \rangle \in \mathbb{R}$ for all $v \in V$ (uses polarisation).
4. There is an orthonormal basis of $V$ with respect to which the matrix of $T$ is real diagonal ([[Thm - Complex Spectral Theorem|complex spectral theorem]] applied to $T$).

Over $\mathbb{R}$, condition (3) is strictly weaker than (1) and is not equivalent; (1) and (2) and (4) (with [[Thm - Real Spectral Theorem|real spectral theorem]]) remain equivalent.

---

# Categorical / Structural Definition

Self-adjoint operators are the **fixed points of the dagger structure** on the category of finite-dimensional inner product spaces. The dagger functor sends $T \in \mathcal{L}(V)$ to $T^* \in \mathcal{L}(V)$, and the self-adjoint operators are exactly $\{T : T^* = T\}$ — the "real" part of the algebra $\mathcal{L}(V)$ under the involution $T \mapsto T^*$.

Equivalently, every operator $T \in \mathcal{L}(V)$ decomposes uniquely as

$$T = \underbrace{\tfrac{1}{2}(T + T^*)}_{\text{self-adjoint}} + i \cdot \underbrace{\tfrac{1}{2i}(T - T^*)}_{\text{self-adjoint over } \mathbb{C}},$$

the operator analogue of $z = \operatorname{Re}(z) + i \operatorname{Im}(z)$. The first summand is self-adjoint; the second is *skew-adjoint* ($T^* = -T$), and $i$ times a skew-adjoint operator is self-adjoint. So every operator on a complex inner product space is, up to a sign, a complex linear combination of two self-adjoint operators. This is the precise sense in which self-adjoint operators are the "real coordinates" on $\mathcal{L}(V)$.

The (real) vector space of self-adjoint operators on $\mathbb{C}^n$ has real [[Def - Dimension|dimension]] $n^2$ — even though $\mathcal{L}(\mathbb{C}^n)$ has complex [[Def - Dimension|dimension]] $n^2$ and so real dimension $2n^2$. Half the complex degrees of freedom are killed by the constraint $T = T^*$, and what remains is the *Hermitian matrix space*, the real Lie algebra $\mathfrak{u}(n)$ rotated by $i$.

---

# Relate to Other Fields / Compression

In **quantum mechanics**, every physical observable is a self-adjoint operator on the Hilbert space of states. Energy is the Hamiltonian $\hat H$; momentum is $\hat p = -i\hbar \nabla$; position is $\hat x$; angular momentum components are $\hat L_i$. The spectral theorem then provides the eigenvalue decomposition: the possible measurement outcomes for the observable $\hat A$ are the eigenvalues of $\hat A$, which are real, and the Born rule reads off the probabilities from the projections onto eigenspaces.

In **Hodge theory and Riemannian geometry**, the **Laplace–Beltrami operator** $\Delta = d d^* + d^* d$ on differential forms of a closed Riemannian manifold is self-adjoint with respect to the $L^2$ inner product. Hodge's theorem then states that the cohomology classes are in bijection with harmonic forms — the kernel of $\Delta$. The spectrum of $\Delta$ provides geometric invariants: the heat kernel and zeta function carry information about the manifold's topology and geometry.

In **statistical mechanics and PDE**, the Schrödinger operator $H = -\Delta + V(x)$ on $L^2(\mathbb{R}^n)$ is self-adjoint under appropriate conditions on $V$, and its spectral decomposition splits $L^2(\mathbb{R}^n)$ into a bound-state part (point spectrum, eigenfunctions of $H$) and a scattering part (absolutely continuous spectrum). The two regimes have completely different qualitative behaviour.

**True name:** Self-adjoint operators are precisely the operators with **real eigenvalues *and* orthogonal eigenvectors** — what is gained over a general real-eigenvalued operator is the orthogonality of eigenvectors for distinct eigenvalues, which is the source of all the chapter's geometric content. The matrix characterisation "$A$ equals its conjugate transpose" is the right thing to *check*; the eigenvalue characterisation is the right thing to *use* once you have it.

---

# Examples / Corollaries

The simplest examples: the identity operator $I$, the zero operator $0$, any real scalar multiple of either. The matrix $\begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ is self-adjoint, and so is $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$ — any real symmetric matrix.

Over $\mathbb{C}$: the matrix $\begin{pmatrix} 2 & 3 + 4i \\ 3 - 4i & 7 \end{pmatrix}$ is self-adjoint (the off-diagonal entries are complex conjugates of each other). The matrix $\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ is *not* self-adjoint (its conjugate transpose is $\begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}$, a different matrix); but $\begin{pmatrix} 1 & i \\ -i & 1 \end{pmatrix}$ *is* self-adjoint.

A canonical family: **orthogonal projections** $P_U$ onto [[Def - Subspace|subspaces]] $U \leq V$. Orthogonal projection is self-adjoint and idempotent ($P^2 = P$), and conversely a projection (i.e., $P^2 = P$) is *orthogonal* in the sense of "projection along the orthogonal complement" if and only if it is self-adjoint. The two characterisations of orthogonal projection coincide. Eigenvalues: $0$ (on $U^{\perp}$) and $1$ (on $U$).

Another family: the **density matrices** of quantum mechanics. A density matrix $\rho \in \mathcal{L}(V)$ on a finite-dimensional state space is a self-adjoint positive operator with $\operatorname{tr}(\rho) = 1$. Pure states are rank-1 density matrices; mixed states are convex combinations.

A non-example: the rotation $R_{\theta} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$ for $\theta \notin \pi \mathbb{Z}$. Its transpose is $R_{-\theta}$, which is not $R_\theta$, so $R_\theta$ is not self-adjoint (it is, however, orthogonal — see [[Def - Unitary Operator]]). For $\theta = \pi$, $R_\pi = -I$ is self-adjoint.

A subtle non-example: the matrix $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$. It is not symmetric, so not self-adjoint. But it *has* eigenvalues $(5 \pm \sqrt{33})/2$, which are real — having real eigenvalues does not imply self-adjointness. The additional content of self-adjointness over "real eigenvalues" is the orthogonality of the eigenvectors.

A corollary: every self-adjoint operator over $\mathbb{C}$ has only real eigenvalues. If $Tv = \lambda v$ with $v \neq 0$, then
$$\lambda \langle v, v \rangle = \langle Tv, v \rangle = \langle v, Tv \rangle = \overline{\langle Tv, v \rangle} = \overline{\lambda \langle v, v \rangle} = \overline{\lambda} \langle v, v \rangle,$$
and since $\langle v, v \rangle \neq 0$, $\lambda = \overline{\lambda} \in \mathbb{R}$. See [[Ex - Self-adjoint operators have real eigenvalues]] for the detailed proof.

Another corollary: eigenvectors for distinct eigenvalues of a self-adjoint operator are orthogonal. If $Tv = \lambda v$ and $Tw = \mu w$ with $\lambda \neq \mu$ (both real), then $\lambda \langle v, w \rangle = \langle Tv, w \rangle = \langle v, Tw \rangle = \mu \langle v, w \rangle$ (using that $\mu$ is real), so $(\lambda - \mu) \langle v, w \rangle = 0$, forcing $\langle v, w \rangle = 0$.

A third corollary: the spectrum of a self-adjoint operator equals the closure of its numerical range. The **numerical range** $\{\langle Tv, v \rangle : \|v\| = 1\}$ of a self-adjoint operator is a real interval $[\lambda_{\min}, \lambda_{\max}]$, where $\lambda_{\min}$ and $\lambda_{\max}$ are the smallest and largest eigenvalues. This is the foundation of the *min-max principle* and the Courant–Fischer theorem for eigenvalues.

**Calibration check.** Verify these three facts about self-adjoint operators:
1. The matrix $\begin{pmatrix} 0 & i \\ -i & 0 \end{pmatrix}$ is self-adjoint over $\mathbb{C}$. (Conjugate transpose it explicitly.)
2. The eigenvalues of the above matrix are $\pm 1$, both real. (Compute the characteristic polynomial.)
3. The sum, real scalar multiple, and conjugate $T \mapsto T^*$ of self-adjoint operators are self-adjoint; the product of two self-adjoint operators is self-adjoint *if and only if they commute*. (The last is a quick exercise: $(ST)^* = T^* S^* = TS$, so $(ST)^* = ST$ iff $ST = TS$.)

If these check out, you have understood the definition.

---

# Unlocked by This

> [!tip] Quantum Mechanics — Observables and the Born Rule *(from Physics)*
> The axiom that every physical observable is a self-adjoint operator on the Hilbert space of states is one of the four cornerstones of quantum mechanics (the others being: states are unit vectors mod phase; time evolution is unitary; composite systems are tensor products). The **spectral theorem** then forces every measurement outcome to be real — it is an eigenvalue of a self-adjoint operator — and the **Born rule** reads off the probability of a measurement outcome as the squared inner product with the corresponding eigenvector. In the language of [[Thm - Complex Spectral Theorem|the complex spectral theorem]]: $T = \sum_j \lambda_j P_j$, the eigenvalues $\lambda_j$ are the measurement outcomes, and $P(\text{outcome } \lambda_j | \text{state } \psi) = \|P_j \psi\|^2 = \langle \psi, P_j \psi \rangle$. The Heisenberg uncertainty principle is the operator-theoretic statement that two non-commuting self-adjoint operators cannot share an eigenbasis, so the variances of their measurements are bounded below by $\frac{1}{2} |\langle [\hat A, \hat B] \rangle|$.

> [!tip] Spectral Measure and Functional Calculus *(from Functional Analysis)*
> A self-adjoint operator $T$ on an infinite-dimensional Hilbert space has a **spectral measure** $E$ — a projection-valued measure on the spectrum $\sigma(T) \subseteq \mathbb{R}$ — and the spectral theorem reads $T = \int_{\sigma(T)} \lambda \, dE(\lambda)$. The **functional calculus** then forms $f(T) = \int f(\lambda) \, dE(\lambda)$ for any bounded Borel function $f$ defined on the spectrum. This is what makes operator-valued exponentials $e^{itH}$ (the time-evolution operator in quantum mechanics) well-defined, and what gives meaning to expressions like $\sqrt{T}$ and $\sin(T)$. The functional calculus respects all algebraic and order relations: $f(T) g(T) = (fg)(T)$, $f(T)^* = \overline{f}(T)$, and if $f \geq 0$ on the spectrum then $f(T)$ is positive. The entire spectral theory of bounded and unbounded self-adjoint operators rests on this construction.

> [!tip] Sturm–Liouville Operators *(from PDE / Mathematical Physics)*
> A **Sturm–Liouville operator** on $[a, b]$ has the form $L u = -(p u')' + q u$ on a domain of functions satisfying boundary conditions, where $p > 0$ and $q$ are continuous real-valued functions. With the right choice of boundary conditions and domain, $L$ is self-adjoint with respect to a weighted $L^2$ inner product. The spectral theorem then guarantees that $L$ has a discrete real spectrum $\lambda_1 \leq \lambda_2 \leq \cdots \to \infty$ with an orthonormal eigenbasis $\{\phi_n\}$ that diagonalises $L$. Every "boundary value problem with self-adjoint operator" — vibration of a string, heat conduction on an interval, the radial Schrödinger equation, the hydrogen atom — is a Sturm–Liouville problem, and its solution is obtained by expanding in the orthonormal eigenbasis. The classical orthogonal polynomials (Legendre, Hermite, Laguerre, Chebyshev) are all eigenfunctions of specific Sturm–Liouville operators.
