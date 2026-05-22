---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Normal Operator"
  - "Def - Adjoint of a Linear Map"
  - "Def - Inner Product Space"
  - "Def - Orthonormal Basis"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional [[Def - Inner Product Space|inner product space]] over $\mathbb{C}$. An operator $T \in \mathcal{L}(V)$ has [[Def - Adjoint of a Linear Map|adjoint]] $T^*$; it is [[Def - Normal Operator|normal]] if $TT^* = T^*T$. An [[Def - Orthonormal Basis|orthonormal basis]] of $V$ is a basis whose vectors are mutually orthogonal unit vectors. For an eigenvalue $\lambda$ of $T$, the eigenspace is $E(\lambda, T) = \{v \in V : Tv = \lambda v\}$, and $P_\lambda$ denotes the orthogonal projection onto $E(\lambda, T)$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

---

# Statement

> **Theorem (Complex Spectral Theorem).** Let $V$ be a finite-dimensional complex inner product space and $T \in \mathcal{L}(V)$. The following are equivalent:
>
> 1. $T$ is [[Def - Normal Operator|normal]] ($TT^* = T^*T$).
> 2. $V$ has an orthonormal basis consisting of eigenvectors of $T$.
> 3. The matrix of $T$ in some orthonormal basis is diagonal.
>
> Equivalently, $T$ admits a **spectral decomposition**
> $$T = \sum_{j} \lambda_j P_j,$$
> where $\lambda_1, \ldots, \lambda_k$ are the distinct eigenvalues of $T$ and $P_j$ is the orthogonal projection onto $E(\lambda_j, T)$, with $\sum_j P_j = I$ and $P_i P_j = 0$ for $i \neq j$.

---

# Motivation

This is the headline theorem of the chapter. It says that the **normal operators** on a complex inner product space are exactly the operators that can be **orthonormally diagonalised** — equivalently, the operators that look like diagonal matrices in some orthonormal basis. Every other theorem in this chapter is a refinement, a corollary, or a consequence of this one.

The theorem answers a question first asked once one has the [[Linear Algebra V — §4–5 Polynomials and Eigenvalues|general theory of diagonalisability]]: when is an operator diagonalisable in such a way that the eigenbasis is *orthonormal*, not merely linearly independent? On a complex inner product space, the complete answer is: precisely when $T$ commutes with its adjoint. The condition is algebraic, easy to check, and pin-points exactly the right class.

The decomposition $T = \sum_j \lambda_j P_j$ is the **functional calculus seed**. Once $T$ is in this form, every function of $T$ — its powers, exponentials, square roots, logarithms, polynomials, more generally any function defined on the spectrum — can be computed by applying the function entry-wise to the eigenvalues:

$$f(T) = \sum_j f(\lambda_j) P_j.$$

This is the operator-theoretic content of "the spectral theorem gives functional calculus". Every concrete computation with a normal operator routes through this formula.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$T$ is a normal operator on a complex inner product space". Recognising normality is the main practical challenge — normality has equivalent characterisations more useful than $TT^* = T^*T$ for verification.

The first disguised source is **the matrix of $T$ in an orthonormal basis equals its conjugate transpose** (self-adjoint case). Self-adjoint operators are automatically normal, since $T = T^*$ implies $TT^* = T \cdot T = T^* T$. *Example problem:* "given a Hermitian matrix, diagonalise it orthonormally". The spectral theorem applies even though "normal" was not explicitly mentioned; self-adjointness is a recognisable special case.

The second disguised source is **the operator preserves norms**, i.e., is unitary. Unitary operators are normal (both compositions equal $I$). *Example problem:* "diagonalise a unitary $U \in U(n)$". The spectral theorem gives an orthonormal eigenbasis with eigenvalues on the unit circle, providing the unitary diagonalisation.

The third disguised source is **the operator commutes with another normal operator that is itself diagonalisable**. Commuting normal operators share an eigenbasis (when one is non-degenerate), so a normal operator commuting with a diagonalisable one is itself orthonormally diagonalisable. *Example problem:* "show that the Pauli matrices $\sigma_x$ and $\sigma_z$ do not share an eigenbasis"; they do not commute, so cannot be simultaneously orthonormally diagonalised — this is the Heisenberg uncertainty principle for spin observables.

The fourth disguised source is **the operator is a polynomial $p(S)$ in a normal operator $S$**. Then $T$ commutes with $S^*$ (since $S$ does), and similarly commutes with $T^* = \overline{p}(S^*)$, so $T$ is normal. *Example problem:* "if $S$ is self-adjoint, show $e^{iS}$ is unitary" — $e^{iS}$ is a polynomial-in-the-limit in $S$, hence shares its eigenbasis, hence is normal (in fact unitary, since the eigenvalues become $e^{i\lambda_j}$ on the unit circle).

**Targets (Output Amplification)**

The conclusion is the orthonormal eigenbasis (or equivalently the spectral decomposition $T = \sum \lambda_j P_j$). Once you have this, an enormous range of additional results becomes accessible.

Combine the conclusion with **the operator norm formula**: $\|T\|_{\text{op}} = \max_j |\lambda_j|$, the largest modulus of an eigenvalue, since in the orthonormal eigenbasis $\|Tv\|^2 = \sum |\lambda_j|^2 |\langle v, e_j \rangle|^2 \leq (\max |\lambda_j|)^2 \|v\|^2$ with equality on the corresponding eigenvector. The result $E$ is the operator norm, computable directly from the spectrum without needing to take a supremum over the unit ball.

Combine the conclusion with **functional calculus**: for any function $f$ on the spectrum, $f(T) = \sum f(\lambda_j) P_j$. The result $E$ is a homomorphism from the algebra of functions on $\sigma(T)$ to $\mathcal{L}(V)$, with $f(T)^* = \overline{f}(T)$, $(fg)(T) = f(T) g(T)$, and so on. The polynomial functional calculus extends to continuous functions on the spectrum, and the assignment $f \mapsto f(T)$ is the **Gelfand transform** of the abelian subalgebra generated by $T$ and $T^*$.

Combine the conclusion with **operator inequalities** (the Loewner order): $T \geq 0$ iff every $\lambda_j \geq 0$ (this is the spectral characterisation of positive operators); $T \leq S$ for self-adjoint $T, S$ iff every eigenvalue $\lambda_j(T - S) \leq 0$. The order theory of self-adjoint operators is the spectral order theory of their eigenvalues, modulo basis change.

Combine the conclusion with **the geometric structure of the eigenspaces**: the eigenspaces $E(\lambda_j, T)$ are mutually orthogonal, and they sum to $V$. The orthogonal projections $P_j$ onto these eigenspaces are mutually orthogonal (in the sense $P_i P_j = 0$ for $i \neq j$) and sum to $I$. The result $E$ is the **resolution of identity**, the orthogonal decomposition $V = \bigoplus_j E(\lambda_j, T)$ together with the projections onto each piece.

---

# Why Is It True

The intuition has three layers. First, every operator on a complex inner product space has at least one eigenvalue (the **fundamental theorem of algebra**: the characteristic polynomial of $T$ factors over $\mathbb{C}$ into linear factors, each giving an eigenvalue). Second, for a normal operator, eigenvectors with different eigenvalues are *orthogonal* — this is the [[Thm - Normal Operators Commute with Their Adjoint|eigenvector-orthogonality lemma]] for normal operators, which is where the spectral theorem's distinctively *orthonormal* diagonalisability comes from. Third, the eigenspaces decompose $V$ completely — there is no "deficient" subspace where $T$ acts non-diagonalisably — because for a normal operator there are no nontrivial generalised eigenvectors that are not actual eigenvectors.

**The one-liner mechanism: for a normal $T$, $\|(T - \lambda I) v\| = \|(T - \overline{\lambda} I)^* v\| = \|(T^* - \overline{\lambda} I) v\|$, so the kernels of $T - \lambda I$ and $T^* - \overline{\lambda} I$ coincide — eigenvectors of $T$ with eigenvalue $\lambda$ are eigenvectors of $T^*$ with eigenvalue $\overline{\lambda}$. This is what forces eigenvectors of $T$ for distinct eigenvalues to be orthogonal and what makes the spectral decomposition possible.**

The clean inductive proof runs as follows. Given a normal $T$, find any eigenvalue $\lambda_1$ (possible by FTA) and an eigenvector $v_1$. The subspace $E(\lambda_1, T)$ — the $\lambda_1$-eigenspace — is invariant under $T$ (trivially) and *also* under $T^*$ (since $T$ and $T^*$ have the same eigenvectors with conjugate eigenvalues, as above). Therefore the orthogonal complement $E(\lambda_1, T)^\perp$ is *also* invariant under both $T$ and $T^*$ — taking orthogonal complements swaps invariance under $T$ with invariance under $T^*$, and a normal operator's eigenspaces are invariant under both. Restrict $T$ to $E(\lambda_1, T)^\perp$, where it is still normal (the restricted adjoint is the restriction of $T^*$, by the joint invariance). Induct on dimension.

Each step extracts one eigenspace and recurses on its orthogonal complement. The eigenspaces emerge mutually orthogonal because they are extracted from a recursively shrinking sequence of orthogonal complements. The total dimension of the eigenspaces equals $\dim V$, so the eigenspace decomposition is complete.

**Why this fails over $\mathbb{R}$:** the proof needs FTA to produce an eigenvalue at each induction step. Over $\mathbb{R}$, FTA does not apply; a normal operator can have no real eigenvalues (e.g., the $90^\circ$ rotation of $\mathbb{R}^2$). The fix is to use [[Thm - Real Spectral Theorem|self-adjointness]], which over $\mathbb{R}$ forces every eigenvalue to be real (so accessible in $\mathbb{R}$); the induction then proceeds as in the complex case.

---

# What Makes This Hard

The non-obvious step is showing that **eigenspaces of a normal operator are invariant under both $T$ and $T^*$**. The forward direction — eigenspaces are $T$-invariant — is trivial. The backward direction — they are also $T^*$-invariant — requires the normality calculation $\|(T - \lambda I) v\| = \|(T^* - \overline{\lambda} I) v\|$, which gives that $T v = \lambda v$ implies $T^* v = \overline{\lambda} v$. Without this, the orthogonal complement argument fails. The most common error is to attempt the induction without first establishing this conjugation pairing.

The second subtle step is the **orthogonality of distinct eigenspaces**. The calculation: if $T v = \lambda v$, $T w = \mu w$ with $\lambda \neq \mu$, then $\lambda \langle v, w \rangle = \langle Tv, w \rangle = \langle v, T^* w \rangle = \langle v, \overline{\mu} w \rangle = \mu \langle v, w \rangle$, so $\langle v, w \rangle (\lambda - \mu) = 0$, forcing orthogonality. This is short but conceptually loaded: it uses the conjugation pairing $T^* w = \overline{\mu} w$, which is the input from normality.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Induct on $\dim V$. At each step, use the fundamental theorem of algebra to extract one eigenvalue and eigenvector, observe that the eigenspace is invariant under both $T$ and $T^*$ (using the normality-implies-conjugation-pairing lemma), and recurse on its orthogonal complement.

**Subgoal decomposition:**

1. **Normality implies eigenvector-eigenvalue conjugation pairing.** Show that for normal $T$, $Tv = \lambda v$ implies $T^* v = \overline{\lambda} v$.
   - *Hint:* Compute $\|(T - \lambda I) v\|^2$ using normality of $T - \lambda I$.
   - *Why needed:* This is what makes eigenspaces of $T$ also eigenspaces of $T^*$, forcing the orthogonal complement to be invariant under both.

2. **Eigenvectors for distinct eigenvalues are orthogonal.** Show that if $Tv = \lambda v$ and $Tw = \mu w$ with $\lambda \neq \mu$, then $\langle v, w \rangle = 0$.
   - *Hint:* Use the conjugation pairing to compute $\langle Tv, w \rangle$ two ways.
   - *Why needed:* This is the central orthogonality statement; without it, the eigenbasis is not orthonormal.

3. **The orthogonal complement of an eigenspace is invariant under both $T$ and $T^*$.** Show that if $U = E(\lambda, T)$, then $T(U^\perp) \subseteq U^\perp$ and $T^*(U^\perp) \subseteq U^\perp$.
   - *Hint:* Use subgoal 1 to argue $U$ is $T^*$-invariant; then orthogonal-complement reverses operator and adjoint invariance.
   - *Why needed:* Lets the induction recurse on a strictly smaller space.

4. **The restriction of $T$ to $U^\perp$ is still normal.** Show that $(T|_{U^\perp})^* = T^*|_{U^\perp}$, hence $T|_{U^\perp} \cdot (T|_{U^\perp})^* = (T|_{U^\perp})^* \cdot T|_{U^\perp}$.
   - *Hint:* The adjoint of a restriction to an invariant subspace is the restriction of the adjoint, *provided the subspace is also $T^*$-invariant*. Subgoal 3 provides this.
   - *Why needed:* Without this, the induction fails — normality is the hypothesis, and we need it to hold for the smaller operator.

5. **Induction.** Combine subgoals 1–4: extract one eigenvalue, isolate an eigenvector, pass to the orthogonal complement of the eigenspace (which is invariant and on which $T$ is still normal), recurse.
   - *Hint:* Base case $\dim V = 1$ is trivial.
   - *Why needed:* The full proof structure.

---

# Lemma Decomposition

> [!note]- Lemma 1: Normal operator's eigenvectors are eigenvectors of the adjoint
> **Statement:** Let $T \in \mathcal{L}(V)$ be normal, $\lambda \in \mathbb{C}$. Then $Tv = \lambda v$ if and only if $T^* v = \overline{\lambda} v$.
>
> **Hint:** Compute $\|(T - \lambda I) v\|^2 = \langle (T - \lambda I) v, (T - \lambda I) v \rangle$ and use normality of $T - \lambda I$ to relate it to $\|(T - \lambda I)^* v\|^2 = \|(T^* - \overline{\lambda} I) v\|^2$.
>
> **Why needed:** The defining feature of normality at the eigenvector level. Without this, eigenspaces are not $T^*$-invariant and the induction fails.
>
> > [!note]- Full proof
> > First, $T - \lambda I$ is also normal: $(T - \lambda I)(T - \lambda I)^* = (T - \lambda I)(T^* - \overline{\lambda} I) = TT^* - \overline{\lambda} T - \lambda T^* + |\lambda|^2 I$, and $(T - \lambda I)^*(T - \lambda I) = (T^* - \overline{\lambda} I)(T - \lambda I) = T^* T - \overline{\lambda} T - \lambda T^* + |\lambda|^2 I$. Since $T T^* = T^* T$, these are equal.
> >
> > For a normal operator $S$, $\|Sv\|^2 = \langle Sv, Sv \rangle = \langle v, S^* S v \rangle = \langle v, S S^* v \rangle = \langle S^* v, S^* v \rangle = \|S^* v\|^2$, so $\|Sv\| = \|S^* v\|$.
> >
> > Applied to $S = T - \lambda I$: $\|(T - \lambda I) v\| = \|(T - \lambda I)^* v\| = \|(T^* - \overline{\lambda} I) v\|$. Therefore $(T - \lambda I) v = 0$ iff $(T^* - \overline{\lambda} I) v = 0$, i.e., $Tv = \lambda v$ iff $T^* v = \overline{\lambda} v$.

> [!note]- Lemma 2: Distinct eigenvalues have orthogonal eigenvectors
> **Statement:** Let $T \in \mathcal{L}(V)$ be normal, and let $v, w$ be eigenvectors with eigenvalues $\lambda \neq \mu$. Then $\langle v, w \rangle = 0$.
>
> **Hint:** Compute $\lambda \langle v, w \rangle$ in two ways: using $Tv = \lambda v$ and using $T^* w = \overline{\mu} w$ (from Lemma 1).
>
> **Why needed:** The orthogonality of distinct-eigenvalue eigenvectors is the central conclusion; without it the eigenbasis is not orthonormal.
>
> > [!note]- Full proof
> > $\lambda \langle v, w \rangle = \langle \lambda v, w \rangle = \langle Tv, w \rangle = \langle v, T^* w \rangle = \langle v, \overline{\mu} w \rangle = \mu \langle v, w \rangle$, using Lemma 1 at the second-to-last step and conjugate-linearity in the second slot at the last. So $(\lambda - \mu) \langle v, w \rangle = 0$, and since $\lambda \neq \mu$, $\langle v, w \rangle = 0$.

> [!note]- Lemma 3: Orthogonal complement of an invariant subspace is invariant under both $T$ and $T^*$
> **Statement:** Suppose $T \in \mathcal{L}(V)$ is normal and $U \leq V$ is a subspace invariant under both $T$ and $T^*$. Then $U^\perp$ is also invariant under both $T$ and $T^*$.
>
> **Hint:** $w \in U^\perp$ means $\langle u, w \rangle = 0$ for all $u \in U$; show $\langle u, Tw \rangle = 0$ for all $u \in U$ by moving $T$ across.
>
> **Why needed:** This is the inductive step engine. Passing to the orthogonal complement of an eigenspace would not work if it were not invariant.
>
> > [!note]- Full proof
> > Let $w \in U^\perp$. For any $u \in U$: $\langle u, Tw \rangle = \langle T^* u, w \rangle = 0$, where the last equality uses $T^* u \in U$ (by $T^*$-invariance of $U$) and $w \perp U$. So $Tw \in U^\perp$. The argument with $T$ and $T^*$ swapped shows $U^\perp$ is also $T^*$-invariant.

> [!note]- Lemma 4: Restriction of a normal operator to a doubly-invariant subspace is normal
> **Statement:** Let $T \in \mathcal{L}(V)$ be normal, and let $W \leq V$ be invariant under both $T$ and $T^*$. Then $T|_W \in \mathcal{L}(W)$ is normal, with adjoint $T^*|_W$.
>
> **Hint:** Check $\langle T|_W \cdot v, w \rangle_W = \langle v, T^*|_W \cdot w \rangle_W$ for $v, w \in W$, using the original adjoint relation in $V$ and that $W$ inherits the inner product.
>
> **Why needed:** The induction requires that the restricted operator continue to be normal so the hypothesis applies again.
>
> > [!note]- Full proof
> > For $v, w \in W$: since $T(W) \subseteq W$ and $T^*(W) \subseteq W$, both $T|_W v$ and $T^*|_W w$ are in $W$, and the inner product on $W$ is inherited from $V$. So $\langle T|_W v, w \rangle = \langle Tv, w \rangle = \langle v, T^* w \rangle = \langle v, T^*|_W w \rangle$, using that the inner products coincide. By uniqueness of the adjoint within $\mathcal{L}(W)$, $(T|_W)^* = T^*|_W$. Then $T|_W \cdot (T|_W)^* = (T T^*)|_W = (T^* T)|_W = (T|_W)^* \cdot T|_W$, confirming normality.

---

# Formal Proof

> [!note]- Complete formal proof
> We prove (1) $\Leftrightarrow$ (2); the equivalence with (3) is just a matrix-form restatement of (2).
>
> **(2) $\Rightarrow$ (1).** Suppose $V$ has an orthonormal eigenbasis $e_1, \ldots, e_n$ with $Te_j = \lambda_j e_j$. In this basis the matrix of $T$ is $D = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$, and the matrix of $T^*$ is $D^* = \operatorname{diag}(\overline{\lambda_1}, \ldots, \overline{\lambda_n})$. Both are diagonal, hence commute: $DD^* = D^* D$. Therefore $T T^* = T^* T$ as operators, so $T$ is normal.
>
> **(1) $\Rightarrow$ (2).** Proceed by induction on $n = \dim V$.
>
> *Base case $n = 1$:* any unit vector is an eigenvector, and the operator $T$ is scalar multiplication by some $\lambda \in \mathbb{C}$.
>
> *Inductive step.* Assume the result for inner product spaces of dimension less than $n$. By the fundamental theorem of algebra, the characteristic polynomial of $T$ has a root $\lambda_1 \in \mathbb{C}$, so $E_1 = E(\lambda_1, T) \neq \{0\}$. By Lemma 1, $E_1$ is also $T^*$-invariant — every $v \in E_1$ satisfies $Tv = \lambda_1 v$, hence $T^* v = \overline{\lambda_1} v \in E_1$.
>
> Let $W = E_1^\perp$. By Lemma 3, $W$ is invariant under both $T$ and $T^*$ (since $E_1$ is). By Lemma 4, $T|_W$ is normal. Since $\dim W = \dim V - \dim E_1 < n$, the inductive hypothesis gives an orthonormal eigenbasis of $W$ consisting of eigenvectors of $T|_W$ (hence of $T$).
>
> Concatenate an orthonormal basis of $E_1$ (which exists and consists of eigenvectors of $T$ with eigenvalue $\lambda_1$) with the orthonormal eigenbasis of $W$. By construction, these are orthogonal (vectors in $E_1$ are orthogonal to vectors in $W = E_1^\perp$). The result is an orthonormal eigenbasis of $V = E_1 \oplus W$. $\blacksquare$
>
> **Spectral decomposition.** With $\lambda_1, \ldots, \lambda_k$ the distinct eigenvalues and $P_j$ the orthogonal projection onto $E(\lambda_j, T)$, the identity $\sum P_j = I$ follows from the direct sum decomposition $V = \bigoplus_j E(\lambda_j, T)$ (by Lemma 2 the eigenspaces are mutually orthogonal, so the sum is orthogonal direct). The identity $T = \sum \lambda_j P_j$ follows by evaluating both sides on each eigenvector. The relation $P_i P_j = 0$ for $i \neq j$ is orthogonality of the eigenspaces.

---

# Cross-Field Exercise Suggestions

1. **Quantum mechanics — the energy eigenbasis.** The Hamiltonian $\hat H$ of any closed quantum system is self-adjoint, hence normal. The complex spectral theorem gives an orthonormal basis $|n\rangle$ of energy eigenstates with $\hat H |n\rangle = E_n |n\rangle$. The state at time $t$ is then $|\psi(t)\rangle = \sum_n c_n e^{-iE_n t/\hbar} |n\rangle$, where $c_n = \langle n | \psi(0) \rangle$. The dynamics decouples completely in the energy eigenbasis. Every concrete calculation in quantum mechanics begins by diagonalising the Hamiltonian.

2. **Markov chains — the stationary distribution.** A reversible Markov chain on a finite state space is described by a transition matrix $P$ which is self-adjoint with respect to a weighted inner product (the detailed balance condition). The complex spectral theorem then gives an orthonormal eigenbasis with real eigenvalues; the eigenvalue $1$ corresponds to the stationary distribution, and the second-largest eigenvalue $\lambda_2$ controls the mixing rate as $1 - \lambda_2$.

3. **Image processing — the discrete Fourier transform of a circulant matrix.** A circulant matrix is normal (it commutes with the cyclic shift, hence with its conjugate transpose), so it is diagonalised by the discrete Fourier transform. This is the algebraic underlay of "convolution in the spatial domain equals multiplication in the frequency domain", and is what makes Fourier-based image processing efficient.

4. **Quantum information — Pauli decomposition.** Any $2 \times 2$ Hermitian matrix $H$ can be written as $H = \frac{a_0 I + a_1 \sigma_x + a_2 \sigma_y + a_3 \sigma_z}{2}$ with real coefficients. By the spectral theorem, this matrix has two orthogonal eigenvectors with real eigenvalues. The eigenvalues are $\frac{a_0 \pm |a|}{2}$ where $|a| = \sqrt{a_1^2 + a_2^2 + a_3^2}$, and the eigenvectors are the points $\pm \frac{\vec a}{|a|}$ on the Bloch sphere. The spectral decomposition is the geometric Bloch-sphere picture of qubits.

---

# Bridges

- **[[Thm - Real Spectral Theorem]]** — The real-field analogue requires self-adjointness instead of normality, because over $\mathbb{R}$ a normal operator can have complex eigenvalues with no real eigenvectors (e.g., a rotation by $90^\circ$). Self-adjointness forces eigenvalues to be real, so they descend to $\mathbb{R}$. The proof structure is otherwise identical, with the FTA-supplied complex eigenvalue replaced by the existence of a real eigenvalue of a self-adjoint operator.

- **[[Thm - Singular Value Decomposition]]** — The SVD is the complex spectral theorem applied to the positive operator $T^* T$. Take $T^* T$, diagonalise it orthonormally with eigenvalues $s_j^2$ (squares of singular values) and eigenvectors $v_j$; then $T v_j$ are orthogonal vectors with $\|T v_j\| = s_j$, and they form the left singular vectors (after normalisation). The spectral theorem for $T^* T$ produces the SVD of $T$ — even when $T$ is not normal.

- **[[Thm - Polar Decomposition]]** — Polar decomposition follows from SVD by regrouping: $T = U \Sigma V^* = (UV^*)(V \Sigma V^*) = S \cdot |T|$. The positive factor $|T| = \sqrt{T^* T}$ is the spectral-theorem positive square root of $T^* T$; the isometric factor $S = UV^*$ encodes the "phase". The polar decomposition is the spectral theorem twice removed: spectral theorem on $T^* T$ gives SVD, regrouping gives polar.

- **[[Thm - Existence of Eigenvalues on Complex Vector Spaces]]** — The starting input for the spectral theorem's induction. Without an eigenvalue at each step, the proof cannot bootstrap. The reason the *complex* spectral theorem works but the *real* spectral theorem requires self-adjointness is precisely that this theorem (the existence of an eigenvalue) requires complex scalars unless an extra condition is imposed.

- **Spectral measure (Functional Analysis)** — In infinite dimensions, a bounded normal operator $T$ on a Hilbert space has a **spectral measure** $E$ on $\sigma(T) \subseteq \mathbb{C}$, and the spectral theorem reads $T = \int z \, dE(z)$. The finite-dimensional sum $T = \sum \lambda_j P_j$ becomes an integral. Functional calculus extends accordingly: $f(T) = \int f(z) \, dE(z)$ for any bounded Borel function $f$.

---

# Unlocked by This

> [!tip] Functional Calculus *(from Functional Analysis)*
> Once $T$ is in spectral form $T = \sum \lambda_j P_j$, any function $f : \mathbb{C} \to \mathbb{C}$ defined on the spectrum gives an operator $f(T) = \sum f(\lambda_j) P_j$. The map $f \mapsto f(T)$ is a homomorphism of unital $*$-algebras: $(fg)(T) = f(T) g(T)$, $\overline{f}(T) = f(T)^*$, $(\alpha f + \beta g)(T) = \alpha f(T) + \beta g(T)$. In infinite dimensions this construction extends to bounded continuous functions on the spectrum (continuous functional calculus) and then to bounded Borel functions (Borel functional calculus). It is what makes $e^{tH}$ — the time-evolution operator in quantum mechanics — well-defined for any self-adjoint $H$.

> [!tip] Min-Max Characterisation of Eigenvalues *(from Variational Calculus / Optimization)*
> The eigenvalues $\lambda_1 \geq \cdots \geq \lambda_n$ of a self-adjoint operator $T$ admit the **Courant–Fischer min-max characterisation**: $\lambda_k = \min_{\dim U = n - k + 1} \max_{v \in U, \|v\| = 1} \langle Tv, v \rangle$, and a dual max-min formula. This converts eigenvalue computations into optimisation problems over subspaces. Applied to graph Laplacians, it gives the **Cheeger inequality** relating the second eigenvalue to the graph's edge expansion. Applied to elliptic PDEs, it gives the **Rayleigh quotient** variational characterisation of eigenvalues of $-\Delta$ — the basis of finite-element methods for computing them.
