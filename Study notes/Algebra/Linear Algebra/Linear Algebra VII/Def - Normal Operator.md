---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Adjoint of a Linear Map"
  - "Def - Self-Adjoint Operator"
  - "Def - Inner Product Space"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional [[Def - Inner Product Space|inner product space]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$, with inner product $\langle \cdot, \cdot \rangle$ and induced norm $\|v\| = \sqrt{\langle v, v \rangle}$. An operator on $V$ is a linear map $T \in \mathcal{L}(V)$; its [[Def - Adjoint of a Linear Map|adjoint]] $T^*$ is the unique operator satisfying $\langle Tv, w \rangle = \langle v, T^* w \rangle$ for all $v, w$. In an orthonormal basis, the matrix of $T^*$ is the conjugate transpose of the matrix of $T$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the complete notation registry.

---

# Axiom Motivation

The definition of a normal operator — $T T^* = T^* T$ — looks like a technical condition, an arbitrary commutativity demand. It is anything but. Normality is the **minimal hypothesis under which the spectral theorem holds**: in the chain of theorems in this chapter, normality is the precise threshold at which an operator becomes orthonormally diagonalisable over $\mathbb{C}$. Everything in the chapter is either a corollary, a special case, or a refinement of "normal operators have an orthonormal eigenbasis".

Why this condition and not another? Begin with the goal: we want to find operators $T$ on a complex inner product space that admit an orthonormal eigenbasis, so that $T = \sum \lambda_j P_j$ where the $P_j$ are the orthogonal projections onto eigenspaces. What conditions does this entail? First, the eigenspaces must be mutually orthogonal — a condition on $T$ alone. Second, the projections $P_j$ must be self-adjoint (they are orthogonal projections, hence self-adjoint by §6). Third, the decomposition $T = \sum \lambda_j P_j$ then forces $T^* = \sum \overline{\lambda_j} P_j$ (taking adjoints, using that the $P_j$ are self-adjoint and orthogonal projection sums are conjugate-transpose under linear combinations with complex coefficients). And here is the consequence: any two such expressions in *commuting* projections commute, so $T$ and $T^*$ commute. **Orthogonally diagonalisable forces $T T^* = T^* T$.** Normality is *necessary*.

The remarkable converse — that normality is also *sufficient* — is the content of the [[Thm - Complex Spectral Theorem|complex spectral theorem]]. To see why one should expect this to work, observe that $T$ and $T^*$ commute iff they share a common eigenvector iff they share a complete eigenbasis (in finite-dimensional complex spaces — a standard fact about commuting diagonalisable operators). And commuting eigenbasis means: $Tv = \lambda v$ implies $T^* v = \overline{\lambda} v$ (the same eigenvector, with the conjugate eigenvalue). Once that happens, eigenvectors for distinct eigenvalues of $T$ are eigenvectors for distinct eigenvalues of $T^*$, so are orthogonal (the calculation $\lambda \langle v, w \rangle = \langle Tv, w \rangle = \langle v, T^* w \rangle = \overline{\overline{\mu}} \langle v, w \rangle = \mu \langle v, w \rangle$ gives orthogonality directly). Normality is the input; orthogonal eigenbasis is the output.

What if you tried to weaken the condition? Demanding only that $T$ be diagonalisable (no orthonormality) is weaker, and far weaker — any matrix with distinct eigenvalues is diagonalisable but generically not orthonormally so. Demanding only that $T$ have real eigenvalues with non-orthogonal eigenvectors is again weaker. The single condition that nails down "orthonormally diagonalisable" is *normality*, and the [[Thm - Complex Spectral Theorem|spectral theorem]] gives the converse.

What if you tried to strengthen it? The standard strengthenings carve out important subclasses:
- **Self-adjoint** ($T = T^*$) is normal with real eigenvalues. The constraint $T = T^*$ implies $T T^* = T T = T^* T$, so self-adjoint operators are normal.
- **Unitary** ($T^* T = T T^* = I$) is normal with eigenvalues on the unit circle.
- **Positive** ($T = T^*$ with $\langle Tv, v \rangle \geq 0$) is self-adjoint, hence normal, with non-negative eigenvalues.
- **Skew-adjoint** ($T^* = -T$, equivalently $iT$ is self-adjoint) is normal with purely imaginary eigenvalues.

So the operator zoo of this chapter is a stratification of normal operators by eigenvalue location. The general normal operator has *no* restriction on the location of its eigenvalues in $\mathbb{C}$, beyond their being a finite multiset — it is the *most general* class of operators with the orthonormal diagonalisability property.

Why does the analogous theorem fail over $\mathbb{R}$? A rotation of $\mathbb{R}^2$ by $90^\circ$ has matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$. It is normal ($T^t T = T T^t = I$, so it is even orthogonal), but its eigenvalues are $\pm i$ — not in $\mathbb{R}$ — and it has no real eigenvectors. So over $\mathbb{R}$, normality does not suffice for diagonalisability: the eigenvalues might escape into $\mathbb{C}$, taking their eigenvectors with them. The fix is to demand self-adjointness, which forces the eigenvalues to be real (see [[Def - Self-Adjoint Operator]]); the [[Thm - Real Spectral Theorem|real spectral theorem]] is the resulting statement.

The equivalent characterisation $\|Tv\| = \|T^* v\|$ is worth dwelling on. The relation $T T^* = T^* T$ is a relation between two operators on $V$; the equivalent relation $\|Tv\| = \|T^* v\|$ is a relation between two real-valued functions on $V$. The latter is much easier to verify in practice: pick a basis, compute both norms, check equality. It is also the form that explains *why* normal operators have orthogonal eigenspaces: if $Tv = \lambda v$ then by the relation $\|Tv - \lambda v\| = \|(T - \lambda I)v\| = \|(T - \lambda I)^* v\| = \|T^* v - \overline{\lambda} v\|$ — but the left side is zero, so $T^* v = \overline{\lambda} v$. So eigenvectors of $T$ and $T^*$ coincide with conjugated eigenvalues, and the orthogonality follows.

---

# The Definition

An operator $T \in \mathcal{L}(V)$ is **normal** if it commutes with its [[Def - Adjoint of a Linear Map|adjoint]]:

$$T T^* = T^* T.$$

Equivalently, $\|Tv\| = \|T^* v\|$ for all $v \in V$.

In an orthonormal basis, the matrix condition is $A A^* = A^* A$.

**Equivalent characterisations.** Over $\mathbb{C}$:
1. $T T^* = T^* T$.
2. $\|Tv\| = \|T^* v\|$ for all $v \in V$.
3. $Tv = \lambda v$ implies $T^* v = \overline{\lambda} v$ (eigenvectors of $T$ are eigenvectors of $T^*$ with conjugate eigenvalue).
4. Eigenvectors of $T$ for distinct eigenvalues are orthogonal.
5. $T$ has an orthonormal eigenbasis ([[Thm - Complex Spectral Theorem|complex spectral theorem]]).

The full theorem stating (1)–(5) equivalent is [[Thm - Normal Operators Commute with Their Adjoint]].

**Subclasses of normal operators:**
- **[[Def - Self-Adjoint Operator|Self-adjoint]]**: $T = T^*$. Eigenvalues are real.
- **Skew-adjoint**: $T = -T^*$. Eigenvalues are purely imaginary.
- **[[Def - Unitary Operator|Unitary]]**: $T T^* = T^* T = I$. Eigenvalues have modulus 1.
- **[[Def - Positive Operator|Positive]]**: $T = T^*$ and $\langle Tv, v \rangle \geq 0$. Eigenvalues are non-negative.

---

# Categorical / Structural Definition

A normal operator is precisely an operator that commutes with its image under the **dagger involution** on $\mathcal{L}(V)$. In the language of $C^*$-algebras (the infinite-dimensional generalisation of $\mathcal{L}(V)$), a normal element of a $C^*$-algebra is an element $a$ with $a a^* = a^* a$, and the **continuous functional calculus** for normal elements assigns to each continuous function $f \in C(\sigma(a))$ on the spectrum an element $f(a)$ of the algebra. This generalises the finite-dimensional spectral theorem to bounded normal operators on Hilbert spaces.

Equivalently, $T$ is normal if and only if the unital $*$-subalgebra of $\mathcal{L}(V)$ generated by $T$ and $T^*$ is **commutative**. (The subalgebra is the $\mathbb{F}$-span of all products of $T$s and $T^*$s; normality says any such product equals its rearrangement by commutativity.) This commutativity is exactly the precondition that the algebra is isomorphic to $\mathbb{F}^n$ (one copy of $\mathbb{F}$ per eigenvalue), which is the algebraic content of the spectral theorem.

---

# Relate to Other Fields / Compression

In **functional analysis**, the definition of "normal" extends without change to bounded operators on Hilbert spaces, and the spectral theorem (for bounded normal operators) gives an integral representation $T = \int_{\sigma(T)} z \, dE(z)$ over the spectrum $\sigma(T) \subseteq \mathbb{C}$, against a projection-valued measure $E$. For *unbounded* operators normality is subtler and requires care about domains. The class of normal operators is the natural setting for spectral theory.

In **$C^*$-algebra theory**, the normal elements are the ones to which the *continuous* functional calculus applies — for normal $a$, the homomorphism $C(\sigma(a)) \to A$, $f \mapsto f(a)$, is an isometric $*$-isomorphism onto the unital $C^*$-algebra generated by $a$. The Gelfand–Naimark theorem then identifies this algebra with the algebra of continuous functions on $\sigma(a)$. This is the deep version of "a normal operator is the multiplication operator $M_z$ on $L^2(\sigma(T), \mu)$ for some measure $\mu$".

**True name:** The true name of normality is $\|Tv\| = \|T^* v\|$ for all $v$. The official definition $TT^* = T^*T$ is the *algebraic* statement, the right thing to use in proofs and to characterise normality at the category level. The norm-equality is the *operational* statement, the right thing to verify in problems and the one that makes the consequences of normality visible (it gives the eigenvector-eigenvalue conjugation pairing in two lines). Both formulations are necessary; the algebraic one is for high-level reasoning, the analytic one is for hands-on verification.

A second, equally important, true name: **normal = orthonormally diagonalisable** (over $\mathbb{C}$). This is the [[Thm - Complex Spectral Theorem|spectral theorem]] in one phrase. The official definition is in terms of commutation with the adjoint; the operational consequence is the orthonormal eigenbasis. The two are equivalent, and one uses the equivalence implicitly every time one diagonalises a normal operator.

---

# Examples / Corollaries

The simplest examples — every self-adjoint operator. The identity, the zero operator, orthogonal projections, real scalar multiples of any of these.

A second family — every unitary operator. The rotation matrix $R_\theta = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$ is normal ($R_\theta R_\theta^t = R_\theta R_{-\theta} = I = R_\theta^t R_\theta$). The unitary diagonal matrix $\operatorname{diag}(e^{i \theta_1}, \ldots, e^{i \theta_n})$ is normal.

A "pure normal" example, not self-adjoint and not unitary — the matrix
$$T = \begin{pmatrix} 2 & 0 \\ 0 & 3 + 4i \end{pmatrix}.$$
This is diagonal in the standard basis, so its adjoint is $T^* = \begin{pmatrix} 2 & 0 \\ 0 & 3 - 4i \end{pmatrix}$, and $TT^* = T^*T = \begin{pmatrix} 4 & 0 \\ 0 & 25 \end{pmatrix}$. Normal, but neither self-adjoint (the entries $3 \pm 4i$ differ) nor unitary (one eigenvalue has modulus $2 \neq 1$).

A non-trivially normal $2 \times 2$ matrix: $T = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$. Check: $T^t T = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = T T^t$. Normal. Eigenvalues are $1 \pm i$, eigenvectors $(1, -i)$ and $(1, i)$ — orthogonal in the standard Hermitian inner product on $\mathbb{C}^2$. The matrix is $\sqrt{2} R_{\pi/4}$ — scaled rotation.

A non-example: the matrix $T = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$. We have $T^* = T^t = \begin{pmatrix} 1 & 0 \\ 1 & 2 \end{pmatrix}$, so $TT^* = \begin{pmatrix} 2 & 2 \\ 2 & 4 \end{pmatrix}$ and $T^* T = \begin{pmatrix} 1 & 1 \\ 1 & 5 \end{pmatrix}$ — these are different. Not normal. The eigenvalues are $1$ and $2$, real, but the eigenvectors are not orthogonal — the matrix is diagonalisable but not *orthonormally* diagonalisable, which is exactly what normality controls.

A subtle non-example: a nilpotent matrix. $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has $N N^* = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $N^* N = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$. Not normal. Its only eigenvalue is $0$, of algebraic multiplicity $2$ but geometric multiplicity $1$ — so there is no eigenbasis at all, let alone an orthonormal one. Normality fails dramatically.

A corollary: a normal operator with all real eigenvalues is self-adjoint. (Proof: if $T = \sum \lambda_j P_j$ with $\lambda_j \in \mathbb{R}$ and $P_j$ self-adjoint orthogonal projections, then $T^* = \sum \overline{\lambda_j} P_j = \sum \lambda_j P_j = T$.) So self-adjoint operators are "normal operators with real eigenvalues" — the eigenvalue characterisation of self-adjointness.

Another corollary: a normal operator $T$ is invertible if and only if zero is not an eigenvalue. (Proof: in the spectral decomposition $T = \sum \lambda_j P_j$, $T$ is invertible iff every $\lambda_j \neq 0$, iff $T^{-1} = \sum \lambda_j^{-1} P_j$ exists.)

A consequence on commutation: two normal operators that commute are simultaneously orthonormally diagonalisable. (Proof: each is diagonalisable, and commuting diagonalisable operators are simultaneously diagonalisable. The orthonormality of the shared eigenbasis takes a separate argument.)

**Calibration check.** Verify:
1. Every diagonal matrix is normal. (Two diagonal matrices commute.)
2. A normal upper-triangular matrix is diagonal. (Compute $A A^*$ and $A^* A$ entry by entry on a $2 \times 2$ upper-triangular matrix; you will find they agree only when the off-diagonal entry is zero.)
3. The product of two normal operators need not be normal. (Take $S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $T = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$; both self-adjoint, but $ST = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, which is unitary but not normal in the sense of being self-adjoint, and you can check $ST \cdot (ST)^* \neq (ST)^* \cdot ST$ — wait, $ST$ is the rotation by $-\pi/2$, *is* normal. Try $S$ and $T$ self-adjoint but not commuting: $S = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, $T = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. Then $ST = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$, which is not normal.)

If these check out, the definition is in your hands.

---

# Unlocked by This

> [!tip] Spectral Measure and the Continuous Functional Calculus *(from Functional Analysis)*
> A bounded normal operator $T$ on a Hilbert space $H$ has a **spectral measure** $E$ on the spectrum $\sigma(T) \subseteq \mathbb{C}$ — now a complex subset, since the eigenvalues of a normal operator need not be real. The integral representation reads $T = \int_{\sigma(T)} z \, dE(z)$. The functional calculus then assigns to each continuous function $f \in C(\sigma(T))$ an operator $f(T) = \int_{\sigma(T)} f(z) \, dE(z)$, with the homomorphism $f \mapsto f(T)$ preserving all algebraic operations and the involution. This is the operator analogue of "you can evaluate any continuous function at a complex number"; for a normal operator, the entire algebra $C(\sigma(T))$ acts on $H$, and the operator $T$ corresponds to the function $z \mapsto z$.

> [!tip] Gelfand–Naimark Theorem *(from C*-algebra theory)*
> The Gelfand–Naimark theorem identifies the commutative unital $C^*$-algebra generated by a normal element $a$ with $C(\sigma(a))$, the continuous functions on the spectrum. The element $a$ itself corresponds under this identification to the function $z \mapsto z$. The functional calculus $f \mapsto f(a)$ is then *literally* the inverse of this identification: it sends a function $f$ to its "evaluation" on $a$. For finite-dimensional $V$, the algebra generated by a normal operator $T$ is $\mathbb{F}^k$ where $k$ is the number of distinct eigenvalues, and the Gelfand transform is $T \mapsto (T|_{V_1}, \ldots, T|_{V_k}) = (\lambda_1, \ldots, \lambda_k)$. This is the same spectral theorem, dressed in different language.

> [!tip] The Heisenberg Uncertainty Principle *(from Physics)*
> Two self-adjoint operators $\hat A$ and $\hat B$ on a Hilbert space commute if and only if they share an orthonormal eigenbasis — both are normal, and commuting normal operators are simultaneously orthonormally diagonalisable. Physically, two observables can be simultaneously measured with arbitrary precision if and only if they commute. When they do not commute, the variances of measurements are bounded below: $\sigma_A \sigma_B \geq \frac{1}{2} |\langle [\hat A, \hat B] \rangle|$. For position and momentum, $[\hat x, \hat p] = i \hbar$, giving the classical $\sigma_x \sigma_p \geq \hbar / 2$. The uncertainty principle is the operator-theoretic statement that non-commuting observables have a quantitative obstruction to joint measurement — and the source of the obstruction is exactly the failure of joint orthonormal diagonalisability of non-commuting normal operators.
