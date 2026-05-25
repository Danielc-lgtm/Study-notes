---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Determinant"
  - "Def - Eigenvalue and Eigenvector"
  - "Thm - Upper-Triangular Form on Complex Vector Spaces"
  - "Thm - Determinant is Multiplicative"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over $\mathbb{C}$ (or more generally an algebraically closed field), and $T \in \mathcal{L}(V)$ is an operator with $n = \dim V$. The eigenvalues of $T$, listed with **algebraic multiplicity**, are $\lambda_1, \dots, \lambda_n \in \mathbb{C}$ (each eigenvalue $\lambda$ appears as many times as its multiplicity as a root of the characteristic polynomial). The **characteristic polynomial** of $T$ is $p_T(z) := \det(zI - T)$.

---

# Statement

> **Theorem (Determinant Equals Product of Eigenvalues, LADR 9.55).** Let $T \in \mathcal{L}(V)$ be an operator on a finite-dimensional complex vector space $V$. Then
>
> $$\det T \;=\; \lambda_1 \cdot \lambda_2 \cdots \lambda_n,$$
>
> where $\lambda_1, \dots, \lambda_n$ are the eigenvalues of $T$ listed with **algebraic multiplicity**.

> **Companion form (characteristic polynomial form, LADR 9.62).** The characteristic polynomial of $T$ factors completely over $\mathbb{C}$ as
>
> $$p_T(z) \;=\; \det(zI - T) \;=\; (z - \lambda_1)(z - \lambda_2) \cdots (z - \lambda_n).$$
>
> In particular, $p_T(0) = (-1)^n \det T = (-1)^n \lambda_1 \cdots \lambda_n$, recovering the theorem statement.

> **Real-field corollary.** For $T$ on a *real* finite-dimensional vector space, $\det T = \prod \lambda_i$ where the product is over the complex eigenvalues (with multiplicity). Since non-real eigenvalues come in complex-conjugate pairs $\lambda, \bar\lambda$ with product $|\lambda|^2 > 0$, the right-hand side is automatically real, even though individual $\lambda_i$ may be complex.

---

# Motivation

This theorem bridges two computational worlds: the abstract definition of $\det$ as the scaling factor on the alternating $n$-form space, and the concrete eigenvalue structure of $T$. It converts a determinant computation into a spectral computation — for operators with known eigenvalue structure, the determinant is *just the product*.

The conceptual content: the determinant is the operator's net "volume scaling factor", and an eigenvalue $\lambda$ is how much $T$ scales the corresponding eigenvector. So a diagonalisable operator stretches each eigenvector by $\lambda_i$, and the total volume scaling is the product $\prod \lambda_i$. For non-diagonalisable operators, the same fact holds with eigenvalues taken with algebraic multiplicity — the result of the **Schur upper-triangularisation theorem**, which says every complex operator has an upper-triangular matrix in some basis.

This theorem is the source of the very useful fact that $\det T = 0$ iff $T$ has eigenvalue $0$ iff $T$ is not invertible — connecting three a priori distinct conditions through the eigenvalue framework. It also makes the characteristic polynomial $p_T(z) = \det(zI - T)$ the natural object whose zeros are eigenvalues, and whose coefficients encode symmetric functions of the eigenvalues (the trace, the determinant, and intermediate elementary symmetric polynomials).

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem requires $T$ on a complex (or algebraically closed) vector space, with known eigenvalues. Disguised sources:

**A diagonalisable operator.** If $T$ is diagonalisable, $T = SDS^{-1}$ with $D$ diagonal, and $\det T = \det D = \prod \text{(diagonal entries)} = \prod \text{(eigenvalues)}$. Bridge: diagonalisability gives spectrum directly. Example problem: find $\det T$ for a self-adjoint operator on a real inner product space, knowing its eigenvalues from the real spectral theorem.

**An operator on a complex space (any operator).** By the upper-triangular theorem (LADR Ch 5), every complex operator has an upper-triangular matrix in some basis, with eigenvalues on the diagonal. So *every* complex operator's determinant equals the product of its eigenvalues. The bridge is via Schur reduction. Example: compute $\det T$ for a complex $T$ with known characteristic polynomial.

**An operator given via Jordan form.** Operators in Jordan canonical form have eigenvalues on the diagonal (with each Jordan block contributing $\lambda$ on its diagonal entries). Multiplicativity plus block-triangular structure gives $\det = \prod \lambda_i$ with algebraic multiplicities. Bridge: Jordan form to upper-triangular form. Example: compute $\det T$ from the Jordan form.

**An operator whose characteristic polynomial is known.** Given $p_T(z) = \prod (z - \lambda_i)$, we read off $\det T = \prod \lambda_i = (-1)^n p_T(0)$. Bridge: characteristic-polynomial calculation gives eigenvalues via factoring. Example: compute $\det$ for a companion matrix of a known polynomial.

**Targets (Output Amplification)**

Combine with invertibility: $T$ is invertible iff all eigenvalues are nonzero. So $\det T = 0$ iff $T$ has eigenvalue 0 iff $T$ is not injective — three equivalent conditions across multiple frameworks (the determinant criterion, the spectral criterion, the rank-nullity criterion).

Combine with the trace ($\operatorname{tr} T = \sum \lambda_i$) to get **Newton-Girard identities**: $\operatorname{tr}$ and $\det$ are two members of the family of "elementary symmetric polynomials in the eigenvalues", $e_1 = \sum \lambda_i = \operatorname{tr} T$, $e_n = \prod \lambda_i = \det T$. The intermediate $e_k$ are also intrinsic invariants of $T$ (the coefficients of the characteristic polynomial).

Combine with continuity arguments: $\det T$ is a polynomial in the matrix entries (Leibniz formula), and the eigenvalues are continuous functions of the matrix entries (by stability of roots). So the identity $\det T = \prod \lambda_i$ relates two continuous functions of $T$, useful for perturbative arguments.

Combine with the spectral theorem: for a normal operator on a complex inner product space, the eigenvalues are explicit, and $\det T = \prod \lambda_i$ allows easy computation. Self-adjoint operators have real eigenvalues; unitary operators have eigenvalues of modulus 1; positive operators have positive eigenvalues.

---

# Why Is It True

The proof has two main ingredients: the [[Thm - Upper-Triangular Form on Complex Vector Spaces|upper-triangular form theorem]] and the [[Thm - Determinant is Multiplicative|multiplicativity of det]].

The upper-triangular form theorem says there is a basis in which $T$ has upper-triangular matrix $A$, with the eigenvalues of $T$ on the diagonal (counted with algebraic multiplicity).

For an upper-triangular matrix $A$ with diagonal entries $\lambda_1, \dots, \lambda_n$, $\det A = \prod \lambda_i$. This is direct from the Leibniz formula: $\det A = \sum_\sigma \operatorname{sign}(\sigma) A_{\sigma(1), 1} \cdots A_{\sigma(n), n}$. For the identity permutation, the product is $\lambda_1 \cdots \lambda_n$ (diagonal entries). For any other permutation, some $\sigma(k) > k$ (the permutation isn't the identity), so $A_{\sigma(k), k}$ is below the diagonal and zero. So only the identity contributes, and the sum is $\lambda_1 \cdots \lambda_n$.

Combining: $\det T = \det A = \prod \lambda_i$.

**The mechanism summary:**

> **Every complex operator has an upper-triangular matrix with eigenvalues on the diagonal (Schur). The determinant of any upper-triangular matrix is the product of diagonal entries (Leibniz collapse). Hence the determinant of any complex operator is the product of its eigenvalues.**

The two facts combine cleanly because $\det$ is similarity-invariant (multiplicativity): the basis change to upper-triangular form does not change the determinant.

---

# What Makes This Hard

The trap is in the multiplicity counting. "$\lambda_1 \cdots \lambda_n$ with multiplicity" has to be carefully unpacked: each *distinct* eigenvalue $\mu$ appears in the product with exponent equal to its **algebraic multiplicity** (the multiplicity as a root of the characteristic polynomial), which is the same as its multiplicity in the upper-triangular diagonal. The **geometric multiplicity** (the [[Def - Dimension|dimension]] of the eigenspace $\ker(T - \mu I)$) is in general *less than* the algebraic multiplicity, and using geometric multiplicity gives the wrong product.

A common error: assuming the operator is diagonalisable and concluding $\det T = \prod (\text{distinct eigenvalues})^{\text{geometric multiplicity}}$. This is correct when geometric = algebraic multiplicity (diagonalisable case) but wrong otherwise. The correct formulation always uses algebraic multiplicity.

Another subtle point: over $\mathbb{R}$, the eigenvalues may be complex, but their product is real (because non-real eigenvalues come in conjugate pairs). The theorem extends to real operators with this caveat: $\det T = \prod \lambda_i$ where the product is over complex eigenvalues with algebraic multiplicity.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**

Reduce to the upper-triangular case by Schur, then use the Leibniz formula to collapse the sum to the diagonal product. Multiplicativity (similarity invariance) ensures $\det$ doesn't change under the basis change.

**Subgoal decomposition:**

1. **Reduce to upper-triangular form.** Apply Schur's theorem ([[Thm - Upper-Triangular Form on Complex Vector Spaces]]): every complex operator has an upper-triangular matrix in some basis.
   - *Hint:* The diagonal entries of the upper-triangular form are the eigenvalues (with algebraic multiplicity).
   - *Why needed:* Once $T$ is upper-triangular, $\det T$ is straightforward.

2. **Compute the determinant of an upper-triangular matrix.** Show $\det A =$ product of diagonal entries via Leibniz formula.
   - *Hint:* Only the identity permutation contributes to the Leibniz sum, because any other permutation has $\sigma(k) > k$ for some $k$, making $A_{\sigma(k), k}$ a below-diagonal entry, hence zero.
   - *Why needed:* This is the explicit computation that reads off $\det$ from diagonal entries.

3. **Combine: the determinant is similarity-invariant.** The basis change to upper-triangular form doesn't change $\det T$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Determinant of an upper-triangular matrix is the product of diagonal entries
> **Statement:** If $A$ is an $n \times n$ upper-triangular matrix with diagonal entries $\lambda_1, \dots, \lambda_n$, then $\det A = \lambda_1 \lambda_2 \cdots \lambda_n$.
>
> **Hint:** In the Leibniz formula $\det A = \sum_\sigma \operatorname{sign}(\sigma) A_{\sigma(1), 1} \cdots A_{\sigma(n), n}$, identify which permutations $\sigma$ make a nonzero contribution. For $\sigma \neq \operatorname{id}$, there is some $k$ with $\sigma(k) > k$ (so $A_{\sigma(k), k} = 0$).
>
> **Why needed:** This is the key calculational lemma. See also [[Ex - Determinant of an upper-triangular matrix is the product of diagonal entries]].
>
> > [!note]- Full proof
> > By the Leibniz formula,
> > $$\det A = \sum_{\sigma \in \operatorname{perm}(n)} \operatorname{sign}(\sigma) A_{\sigma(1), 1} A_{\sigma(2), 2} \cdots A_{\sigma(n), n}.$$
> > Suppose $\sigma \neq \operatorname{id}$. Then there is some index $k$ with $\sigma(k) \neq k$. The smallest such $k$ satisfies $\sigma(k) > k$ (because $\sigma$ is a permutation: $\sigma(1), \dots, \sigma(k-1)$ together with $\sigma(k)$ all lie in $\{1, \dots, n\}$, and by choice of $k$, $\sigma(1) = 1, \dots, \sigma(k-1) = k - 1$, so $\sigma(k) \in \{k, k+1, \dots, n\} \setminus \{k\} = \{k+1, \dots, n\}$, hence $\sigma(k) > k$). For this $k$, $A_{\sigma(k), k}$ is an entry strictly below the diagonal (row index $\sigma(k) > k =$ column index), hence zero since $A$ is upper-triangular. Therefore the product $A_{\sigma(1), 1} \cdots A_{\sigma(n), n}$ contains a zero factor and equals zero. Only the identity permutation contributes:
> > $$\det A = \operatorname{sign}(\operatorname{id}) A_{1, 1} A_{2, 2} \cdots A_{n, n} = (+1) \lambda_1 \lambda_2 \cdots \lambda_n.$$

> [!note]- Lemma 2: Diagonal entries of the upper-triangular form are the eigenvalues with multiplicity
> **Statement:** If $T \in \mathcal{L}(V)$ has upper-triangular matrix $A$ in some basis, then the diagonal entries $A_{ii}$ are exactly the eigenvalues of $T$ (counted with algebraic multiplicity).
>
> **Hint:** The characteristic polynomial of an upper-triangular matrix $A$ is the product of $(z - A_{ii})$, by the Leibniz-formula reasoning above (applied to the upper-triangular $(zI - A)$). The eigenvalues with algebraic multiplicity are exactly the roots of $p_T(z) = \prod(z - A_{ii})$.
>
> **Why needed:** Connects the upper-triangular diagonal entries (which Lemma 1 multiplies for $\det$) to the eigenvalues (which the theorem asserts the product equals).
>
> > [!note]- Full proof
> > Compute $p_T(z) = \det(zI - T) = \det(zI - A)$ where $A$ is the upper-triangular matrix of $T$. The matrix $zI - A$ is also upper-triangular, with diagonal entries $(z - A_{11}), (z - A_{22}), \dots, (z - A_{nn})$. By Lemma 1, $\det(zI - A) = \prod_i (z - A_{ii})$. The roots of $p_T(z)$ are exactly $A_{11}, A_{22}, \dots, A_{nn}$ (with multiplicity as repeated diagonal entries), which is the definition of "eigenvalues with algebraic multiplicity".

---

# Formal Proof

> [!note]- Complete formal proof
> Let $T \in \mathcal{L}(V)$ be an operator on a finite-dimensional complex vector space $V$.
>
> **Step 0 — Preconditions.** $\mathbb{F} = \mathbb{C}$ is algebraically closed, so the characteristic polynomial $p_T(z)$ factors as $\prod (z - \lambda_i)$ with the $\lambda_i$ the eigenvalues of $T$ (counted with algebraic multiplicity).
>
> **Step 1 — Reduce to upper-triangular form.** By [[Thm - Upper-Triangular Form on Complex Vector Spaces|Schur's theorem]], there exists a basis $(e_1, \dots, e_n)$ of $V$ in which $T$ has upper-triangular matrix $A$, with diagonal entries $\lambda_1, \dots, \lambda_n$ (the eigenvalues of $T$ with algebraic multiplicity, by Lemma 2).
>
> **Step 2 — Compute $\det T$ in this basis.** Since the determinant of an operator equals the determinant of its matrix in any basis (similarity invariance, a corollary of [[Thm - Determinant is Multiplicative|multiplicativity]]),
> $$\det T = \det A.$$
>
> **Step 3 — Apply Lemma 1.** Since $A$ is upper-triangular with diagonal entries $\lambda_1, \dots, \lambda_n$,
> $$\det A = \lambda_1 \lambda_2 \cdots \lambda_n.$$
>
> **Step 4 — Conclude.** Combining Steps 2 and 3,
> $$\det T = \lambda_1 \lambda_2 \cdots \lambda_n. \qquad \blacksquare$$
>
> **For the characteristic polynomial form.** $p_T(z) = \det(zI - T)$. By the same argument (apply Schur and Lemma 1 to $zI - T$, whose upper-triangular matrix has diagonal entries $z - \lambda_i$),
> $$p_T(z) = \det(zI - A) = \prod_i (z - \lambda_i). \qquad \blacksquare$$

---

# Cross-Field Exercise Suggestions

**Volume of a parallelepiped via eigenvalues.** Given a $3 \times 3$ symmetric matrix $A$, the parallelepiped spanned by the columns has volume $|\det A| = |\lambda_1 \lambda_2 \lambda_3|$, where $\lambda_i$ are the eigenvalues. So for a symmetric positive-definite matrix (an inner product), the volume is the product of "semi-axis lengths" of the associated ellipsoid — a geometric interpretation of the determinant-as-eigenvalue-product.

**Determinant of the matrix exponential.** $\det e^T = e^{\operatorname{tr} T}$. Proof: eigenvalues of $e^T$ are $e^{\lambda_i}$ (with multiplicity), so $\det e^T = \prod e^{\lambda_i} = e^{\sum \lambda_i} = e^{\operatorname{tr} T}$. This is the key identity behind **Liouville's theorem** in ODE theory: the time-evolution operator of $\dot x = A x$ has determinant $e^{t \operatorname{tr} A}$.

**Probability that a random matrix is singular.** A random matrix $A$ has $\det A = \prod \lambda_i$, and $A$ is singular iff some $\lambda_i = 0$. So computing the probability of singularity reduces to "probability that the spectrum of a random matrix contains 0". For Gaussian random matrices, this involves the **circular law** and **GUE/GOE** statistics from random matrix theory.

**Stability of dynamical systems via eigenvalues.** A linear dynamical system $x_{n+1} = A x_n$ converges to zero from generic initial conditions iff all eigenvalues of $A$ have $|\lambda_i| < 1$. The determinant $\det A = \prod \lambda_i$ gives the "average shrinking rate" — but the spectral radius $\max |\lambda_i|$, not $|\det A|$, governs stability. Eigenvalue-product gives volume contraction; spectral radius gives directional contraction.

**Birkhoff-Hopf theorem in ergodic theory.** For a positive linear operator $T$ on an ordered vector space, the Birkhoff-Hopf theorem relates the contraction rate of $T$ in the projective metric to a ratio of eigenvalues. The determinant of related products of eigenvalues appears in the contraction-rate formula. This is a key tool in the analysis of stochastic operators and Markov chains.

---

# Bridges

- **[[Thm - Upper-Triangular Form on Complex Vector Spaces|Schur's theorem]] (upper-triangular form on $\mathbb{C}$)** — the structural ingredient. Schur says every complex operator is upper-triangular in some basis, with eigenvalues on the diagonal. Without Schur, the leap from "determinant" to "eigenvalue product" would not be available.

- **[[Thm - Determinant is Multiplicative|Multiplicativity of det]]** — used implicitly to say "$\det T = \det A$" for the upper-triangular matrix $A$ of $T$. Multiplicativity is the similarity-invariance that lets us choose any basis.

- **The trace as a sum of eigenvalues.** Parallel to "$\det = \prod \lambda_i$", we have "$\operatorname{tr} T = \sum \lambda_i$". The two are the extremal **elementary symmetric polynomials** in the eigenvalues, the only two that are universally meaningful for any operator. The intermediate symmetric polynomials $e_k(\lambda_1, \dots, \lambda_n)$ are the coefficients of the characteristic polynomial.

- **The characteristic polynomial $p_T(z) = \det(zI - T)$** — the "generating function" for the eigenvalues. The theorem says $p_T$ factors as $\prod (z - \lambda_i)$ over $\mathbb{C}$; the determinant $\det T = (-1)^n p_T(0)$ is essentially $p_T$ evaluated at zero, with a sign correction.

- **[[Thm - Cayley-Hamilton (Minimal-Polynomial Form)|Cayley-Hamilton]]** — $T$ satisfies its own characteristic polynomial, $p_T(T) = 0$. Combined with $p_T(z) = \prod (z - \lambda_i)$, this gives $(T - \lambda_1 I)(T - \lambda_2 I) \cdots (T - \lambda_n I) = 0$. The eigenvalue-product theorem is one of the data points feeding into Cayley-Hamilton: the determinant is the constant term of $p_T$ (up to sign), so it appears in the polynomial annihilator.

---

# Unlocked by This

> [!tip] Liouville's Formula and Volume Preservation *(from ODE Theory)*
> $\det e^T = e^{\operatorname{tr} T}$. For a Hamiltonian flow with $\operatorname{tr} J = 0$ (where $J$ is the Jacobian of the Hamiltonian vector field), the flow has $\det = 1$, i.e., is volume-preserving. This is one of the foundational results in classical mechanics and ergodic theory.

> [!tip] Trace and Determinant as Lie Algebra Invariants *(from Lie Theory)*
> $\operatorname{tr}$ and $\det$ are the two universal traces of an operator. The Lie algebra of $\mathrm{SL}(n)$ is $\mathfrak{sl}(n) = \ker(\operatorname{tr})$, and the exponential map $\exp : \mathfrak{sl}(n) \to \mathrm{SL}(n)$ respects $\det$ via $\det e^X = e^{\operatorname{tr} X} = e^0 = 1$.

> [!tip] Spectral Radius Formula *(from Functional Analysis)*
> The spectral radius $r(T) = \max |\lambda_i|$ satisfies $r(T) = \lim_n \|T^n\|^{1/n}$. While $\det T = \prod \lambda_i$ measures the "average" eigenvalue, the spectral radius measures the "largest". For applications in iterative algorithms, the spectral radius is what matters.

> [!tip] Random Matrix Theory and Eigenvalue Statistics *(from Probability)*
> The distribution of eigenvalues of a random matrix is studied in random matrix theory, with key results being the **semicircle law** (Wigner), the **circular law**, and the **Tracy-Widom distribution**. The determinant $\det A = \prod \lambda_i$ enters as a polynomial invariant, with its statistical behaviour governed by joint eigenvalue distributions.
