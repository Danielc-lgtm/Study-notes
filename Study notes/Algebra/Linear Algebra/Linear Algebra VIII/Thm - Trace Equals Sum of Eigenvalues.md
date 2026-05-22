---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Trace"
  - "Def - Eigenvalue and Eigenvector"
  - "Def - Algebraic and Geometric Multiplicity"
  - "Thm - Upper-Triangular Form on Complex Vector Spaces"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional nonzero vector space over $\mathbb{C}$ and $T \in \mathcal{L}(V)$. $\operatorname{tr} T$ is the trace of $T$ (see [[Def - Trace]]). $\lambda_1, \dots, \lambda_m$ are the distinct eigenvalues of $T$ with multiplicities $d_1, \dots, d_m$. Equivalently $\lambda_1, \dots, \lambda_n$ (with $n = \dim V$) is the list of eigenvalues, each included as many times as its multiplicity. Full registry on [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

---

# Statement

> **Theorem (Trace equals sum of eigenvalues).** Suppose $\mathbf{F} = \mathbb{C}$ and $T \in \mathcal{L}(V)$. Then $\operatorname{tr} T$ equals the sum of the eigenvalues of $T$, each included as many times as its multiplicity:
> $$\operatorname{tr} T = d_1 \lambda_1 + d_2 \lambda_2 + \cdots + d_m \lambda_m = \lambda_1 + \cdots + \lambda_n,$$
> where the second form uses the list with repetition.

> **Corollary (Trace and characteristic polynomial).** With $n = \dim V$, the trace of $T$ equals the negative of the coefficient of $z^{n-1}$ in the characteristic polynomial $p_T(z) = z^n - (\operatorname{tr} T) z^{n-1} + \cdots + (-1)^n \det T$.

---

# Motivation

The trace and the determinant are the two simplest invariants of an operator. The trace is the sum of the eigenvalues with multiplicity; the determinant is the product. Both are read off any matrix of $T$ in any basis — the trace by adding diagonal entries, the determinant by a more elaborate (but still basis-independent) calculation — without knowing or computing the eigenvalues. This is the central content of the theorem: **the simplest scalar invariant of $T$ is computable from any matrix representation, and equals the symmetric function of the eigenvalues**.

The relationship is not accidental. Both the trace and the determinant are *coefficients* of the characteristic polynomial $p_T(z) = \prod_{k=1}^n (z - \lambda_k)$, where the $\lambda_k$ are eigenvalues with multiplicity. Expanding,
$$p_T(z) = z^n - (\lambda_1 + \cdots + \lambda_n) z^{n-1} + (\text{further symmetric functions}) z^{n-2} + \cdots + (-1)^n \lambda_1 \cdots \lambda_n.$$
The coefficient of $z^{n-1}$ is $-(\lambda_1 + \cdots + \lambda_n) = -\operatorname{tr} T$, and the constant term is $(-1)^n \lambda_1 \cdots \lambda_n = (-1)^n \det T$. So the trace and determinant are *the two extreme elementary symmetric functions of the eigenvalues*, and the characteristic polynomial encodes them — along with all the intermediate elementary symmetric functions — as a single algebraic object.

The use of the theorem in practice is to extract eigenvalue information from a matrix without diagonalising. The matrix $A = \begin{pmatrix} 51 & -12 & -21 \\ 60 & -40 & -28 \\ 57 & -68 & 1 \end{pmatrix}$ has trace $51 - 40 + 1 = 12$. If you are told two eigenvalues are $-48$ and $24$, the third is determined: $-48 + 24 + \mu = 12$, so $\mu = 36$. You have computed an eigenvalue *without diagonalising* — at the cost of needing two eigenvalues to start with. The technique generalises: knowing the elementary symmetric functions $e_1 = \operatorname{tr} T$, $e_2$, …, $e_n = \det T$ is equivalent to knowing the eigenvalues (as roots of the polynomial $z^n - e_1 z^{n-1} + e_2 z^{n-2} - \cdots$).

Why use the upper-triangular form to prove the theorem? Because the diagonal entries of any upper-triangular matrix of $T$ are exactly the eigenvalues with multiplicity (see [[Def - Algebraic and Geometric Multiplicity]]: the algebraic multiplicity of $\lambda$ equals the number of times $\lambda$ appears on the diagonal of any upper-triangular matrix). The trace of an upper-triangular matrix is the sum of its diagonal entries — which is the sum of the eigenvalues with multiplicity. Basis-independence of the trace finishes the argument: the trace is the same in any basis, so we may compute it in the upper-triangular basis.

The proof is short — three lines — because all the structural work has already been done in earlier sections: existence of an upper-triangular form ([[Thm - Upper-Triangular Form on Complex Vector Spaces]]), the diagonal-entries-are-eigenvalues identification, and basis-independence of the trace.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is "$\mathbf{F} = \mathbb{C}$ and $T \in \mathcal{L}(V)$". The source-broadening question is when the *theorem* (rather than just the trace itself) is invoked, often in service of extracting partial eigenvalue information.

The first disguised source is **a partial-eigenvalue problem**: most eigenvalues are known, one or two are unknown. *Example problem:* the operator $T$ has trace $12$, dimension $3$, and known eigenvalues $-48, 24$. Find the third. By the theorem, the missing eigenvalue is $12 - (-48) - 24 = 36$. This is the prototypical use; *exercise 7 of §8D in LADR* is exactly this.

The second disguised source is **a problem combining trace with determinant or other elementary symmetric functions**. *Example problem:* $T$ on $\mathbb{C}^2$ has $\operatorname{tr} T = 5$ and $\det T = 4$. Find the eigenvalues. The eigenvalues are roots of $z^2 - 5z + 4 = (z - 1)(z - 4)$, so the eigenvalues are $1$ and $4$. The trace and determinant together gave the characteristic polynomial, which gave the eigenvalues.

The third disguised source is **a problem involving $\operatorname{tr}(T^k)$ for various $k$**. The trace of $T^k$ equals the sum of $\lambda_j^k$ over the eigenvalues with multiplicity — the *power sums* — and **Newton's identities** convert power sums into elementary symmetric functions (and vice versa). *Example problem:* on $\mathbb{C}^2$, $\operatorname{tr} T = 0$ and $\operatorname{tr} T^2 = 2$. Find the eigenvalues. We have $\lambda_1 + \lambda_2 = 0$ and $\lambda_1^2 + \lambda_2^2 = 2$. From the first, $\lambda_2 = -\lambda_1$, and the second becomes $2 \lambda_1^2 = 2$, so $\lambda_1 = \pm 1$ and $\lambda_2 = \mp 1$. So the eigenvalues are $\pm 1$.

**Targets (Output Amplification)**

The bare conclusion is "trace = sum of eigenvalues". Combined with other facts it does much more.

Combine with **the matching identity for determinants** ($\det T = $ product of eigenvalues). Together these say the trace and determinant are the first and last elementary symmetric polynomials of the eigenvalues. The further result is the **characteristic polynomial in coefficient form**: $p_T(z) = z^n - e_1 z^{n-1} + e_2 z^{n-2} - \cdots + (-1)^n e_n$, with $e_k$ the $k$th elementary symmetric function of the eigenvalues. Knowing the trace and determinant gives $e_1$ and $e_n$; knowing all $e_k$ via the characteristic polynomial is equivalent to knowing the eigenvalues.

Combine with **Newton's identities**. Power sums $p_k = \sum_j \lambda_j^k = \operatorname{tr}(T^k)$ are related to elementary symmetric functions $e_k$ by Newton's identities: $p_k = e_1 p_{k-1} - e_2 p_{k-2} + \cdots + (-1)^{k-1} k e_k$. Hence the traces $\operatorname{tr}(T), \operatorname{tr}(T^2), \dots, \operatorname{tr}(T^n)$ determine the characteristic polynomial. The further result is a procedure for computing eigenvalues from traces of powers — equivalently, from the trace inner product on $\mathcal{L}(V)$ and its iterates.

Combine with **the spectral theorem on inner product spaces** (cf. [[Thm - Complex Spectral Theorem]]). On a complex inner product space, a normal operator has algebraic = geometric multiplicities (no Jordan blocks larger than $1$), so the trace identity becomes $\operatorname{tr} T = \sum \lambda_i \langle e_i, e_i \rangle$ for an orthonormal eigenbasis $e_i$. The further result is the cleaner identity $\operatorname{tr} T = \sum \lambda_i$ (now $\lambda_i$ counted with geometric multiplicity), which on an inner product space is straightforward.

---

# Why Is It True

The argument is essentially one observation: in any basis where the matrix of $T$ is upper triangular, the diagonal entries are exactly the eigenvalues of $T$ with multiplicity. So the trace (sum of diagonal entries) is the sum of eigenvalues with multiplicity.

**Mechanism summary: the diagonal of an upper-triangular matrix of $T$ contains the eigenvalues with multiplicity, and the trace adds them up.**

Why is the diagonal of an upper-triangular matrix the multiplicities-counted list of eigenvalues? Because for an upper-triangular matrix, the eigenvalues are exactly the diagonal entries (this is in [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]]: for upper-triangular $A$, $A - \lambda I$ is upper triangular with diagonal $\lambda_k - \lambda$, and is non-invertible iff some $\lambda_k = \lambda$). The algebraic multiplicity of $\lambda$ equals the number of times $\lambda$ appears on the diagonal — see [[Def - Algebraic and Geometric Multiplicity]] and [[Thm - Upper-Triangular Form on Complex Vector Spaces]].

The proof is a one-line invocation of these earlier results plus basis-independence of the trace.

---

# What Makes This Hard

There is no genuine difficulty — the theorem is essentially a corollary of "every operator on a complex space has an upper-triangular matrix" and "the trace is basis-independent". The trap is to forget that the *complex* field is required for upper-triangulability: over $\mathbb{R}$, the theorem fails because $T$ may have no real eigenvalues (a rotation matrix has trace $\cos \theta + \cos \theta = 2 \cos \theta$ but the eigenvalues are $e^{\pm i \theta}$, complex). The theorem statement is correct only over $\mathbb{C}$ — or over $\mathbb{R}$ if we count *complex* eigenvalues with multiplicity, but then "eigenvalues with multiplicity sum to trace" is the same statement over the complexified operator.

The other potential confusion is that "multiplicity" in the statement refers to the **algebraic multiplicity** (= $\dim G(\lambda, T)$), not the geometric multiplicity. On a complex space the algebraic multiplicities sum to $\dim V$, which is what makes the formula $\operatorname{tr} T = d_1 \lambda_1 + \cdots + d_m \lambda_m$ correct.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Find an upper-triangular matrix of $T$. Use that its diagonal entries are the eigenvalues with multiplicity. Compute the trace.

**Subgoal decomposition:**

1. **Upper-triangular form exists.** Use [[Thm - Upper-Triangular Form on Complex Vector Spaces]] to find a basis in which the matrix of $T$ is upper triangular.
   - *Hint:* Existence of upper-triangular form is a separate theorem proved in [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].
   - *Why needed:* This is the setup in which the diagonal entries are explicit.

2. **Diagonal entries are eigenvalues with multiplicity.** Use the fact (proved in §8B of LADR) that the multiplicity of each eigenvalue $\lambda$ equals the number of times $\lambda$ appears on the diagonal of the upper-triangular matrix.
   - *Hint:* The eigenvalues of an upper-triangular matrix are its diagonal entries; the algebraic multiplicity is the number of repetitions on the diagonal.
   - *Why needed:* Identifies the diagonal entries as the eigenvalue list.

3. **Trace is basis-independent.** Use the cyclic property of the trace to conclude that $\operatorname{tr} T$ equals the trace of any matrix of $T$, including the upper-triangular one.
   - *Hint:* $\operatorname{tr}(C^{-1} A C) = \operatorname{tr}(A)$ by cyclicity. See [[Def - Trace]].
   - *Why needed:* Lets us choose the basis.

4. **Compute the trace.** Sum the diagonal entries = sum of eigenvalues with multiplicity.
   - *Hint:* Direct.
   - *Why needed:* The conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Existence of upper-triangular form on a complex space
> **Statement:** For any $T \in \mathcal{L}(V)$ on a complex space, there exists a basis of $V$ in which the matrix of $T$ is upper triangular.
>
> **Hint:** This is [[Thm - Upper-Triangular Form on Complex Vector Spaces]], proved in [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].
>
> **Why needed:** The proof of the trace theorem uses upper-triangular form as the privileged basis.
>
> > [!note]- Full proof
> > See [[Thm - Upper-Triangular Form on Complex Vector Spaces]]. The proof is by induction on $\dim V$: find an eigenvalue $\lambda$ (Fundamental Theorem of Algebra), an eigenvector $v$, an invariant complement of the line spanned by $v$, and induct.

> [!note]- Lemma 2: Diagonal of upper-triangular = eigenvalues with multiplicity
> **Statement:** Suppose $T \in \mathcal{L}(V)$ on a complex space and $T$ has upper-triangular matrix $A$ in some basis. Then for each eigenvalue $\lambda$ of $T$, the number of times $\lambda$ appears on the diagonal of $A$ equals the (algebraic) multiplicity of $\lambda$.
>
> **Hint:** This is the substance of §8B of LADR (theorem 8.31 there). It uses the null-space stabilisation result to count algebraic multiplicities. Take it as a given here.
>
> **Why needed:** This is what makes the diagonal-entries-of-upper-triangular = eigenvalues-with-multiplicity identification rigorous.
>
> > [!note]- Full proof
> > Let $\lambda_1, \dots, \lambda_n$ be the diagonal entries of $A$ (with multiplicity for repetitions). For each $\lambda$ that appears, count the multiplicity. The proof uses the null-space stabilisation argument plus rank-nullity applied to powers of $T - \lambda I$. See LADR 8.31 for the full argument.

> [!note]- Lemma 3: Trace is basis-independent
> **Statement:** Suppose $A$ and $B$ are matrices of the same operator $T \in \mathcal{L}(V)$ in two different bases. Then $\operatorname{tr} A = \operatorname{tr} B$.
>
> **Hint:** $B = C^{-1} A C$ for the change-of-basis matrix $C$. Apply cyclicity of the trace.
>
> **Why needed:** Lets us compute $\operatorname{tr} T$ in any convenient basis.
>
> > [!note]- Full proof
> > By the change-of-basis formula for matrices of operators, $B = C^{-1} A C$ for an invertible matrix $C$. By the cyclic property of trace (Lemma applied to the matrix factors),
> > $$\operatorname{tr} B = \operatorname{tr}(C^{-1} A C) = \operatorname{tr}((C^{-1} A) C) = \operatorname{tr}(C (C^{-1} A)) = \operatorname{tr}((C C^{-1}) A) = \operatorname{tr}(I \cdot A) = \operatorname{tr} A.$$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathbf{F} = \mathbb{C}$ and $T \in \mathcal{L}(V)$. Let $n = \dim V$.
>
> **Step 1 — upper-triangular form.** By Lemma 1, there is a basis $v_1, \dots, v_n$ of $V$ in which the matrix of $T$ is upper triangular. Let $A = \mathcal{M}(T, (v_1, \dots, v_n))$ and let $\mu_1, \dots, \mu_n$ be the diagonal entries of $A$ (listed in order).
>
> **Step 2 — eigenvalues with multiplicity.** By Lemma 2, for each distinct eigenvalue $\lambda$ of $T$, the multiplicity $d_\lambda$ equals the number of indices $k$ such that $\mu_k = \lambda$. Hence $\{\mu_1, \dots, \mu_n\}$ as a multiset is exactly $\{\lambda_1 \text{ (with mult } d_1\text{)}, \dots, \lambda_m \text{ (with mult } d_m\text{)}\}$.
>
> **Step 3 — trace.** Since the trace of an upper-triangular matrix is the sum of its diagonal entries,
> $$\operatorname{tr} A = \sum_{k=1}^n \mu_k = \sum_{k=1}^m d_k \lambda_k.$$
>
> **Step 4 — basis-independence.** By Lemma 3, $\operatorname{tr} T = \operatorname{tr} A$ regardless of the basis. Hence
> $$\operatorname{tr} T = \sum_{k=1}^m d_k \lambda_k = \lambda_1 + \cdots + \lambda_n \quad \text{(eigenvalues with multiplicity)}.$$
>
> $\blacksquare$
>
> **Corollary (Trace and characteristic polynomial).** The characteristic polynomial $p_T(z) = \prod_{k=1}^m (z - \lambda_k)^{d_k}$ expands as
> $$p_T(z) = z^n - \left(\sum_k d_k \lambda_k \right) z^{n-1} + \cdots + (-1)^n \prod_k \lambda_k^{d_k},$$
> so the coefficient of $z^{n-1}$ is $-\operatorname{tr} T$. Equivalently, $\operatorname{tr} T = -(\text{coefficient of } z^{n-1} \text{ in } p_T)$.

---

# Cross-Field Exercise Suggestions

**Quantum mechanics — expectation values via trace.** The expectation value of an observable $A$ in a mixed quantum state with density matrix $\rho$ is $\langle A \rangle = \operatorname{tr}(\rho A)$. The eigenvalues of $A$ are the possible measurement outcomes, with probabilities given by the diagonal entries of $\rho$ in an eigenbasis of $A$. The trace identity here is the probabilistic interpretation: $\langle A \rangle = \sum_i p_i \lambda_i$, the weighted average of eigenvalues. The trace is computed in *any* basis, basis-independence is the physical statement that expectation values do not depend on the measurement basis.

**Statistical mechanics — partition function.** The partition function $Z(\beta) = \operatorname{tr}(e^{-\beta H})$ for a Hamiltonian $H$ with eigenvalues $E_n$ (energy levels) equals $\sum_n e^{-\beta E_n}$ — a sum over the spectrum of $H$. The trace identity is exactly the spectral formula here, recovering the canonical partition function as a sum of Boltzmann factors. The generating function for the moments of energy is $\log Z(\beta)$.

**Newton's identities and symmetric polynomials.** The traces $\operatorname{tr}(T^k) = \sum_j \lambda_j^k$ for $k = 1, 2, \dots, n$ are the **power sums** of the eigenvalues. Newton's identities recursively convert these into the elementary symmetric polynomials $e_k$. So the traces of powers of $T$ determine the characteristic polynomial — and hence the eigenvalues — even without diagonalising. This is the algebraic foundation of *moment-method spectral algorithms*: estimate $\operatorname{tr}(T^k)$ for small $k$ by sampling, then back-solve for the eigenvalues. The technique generalises to infinite dimensions via heat-kernel traces.

---

# Bridges

- **[[Def - Trace]]** — the definition of trace (matrix and operator) and the cyclic property that makes it basis-independent. The current theorem is the *spectral identity* for the trace; the definition only gave the algebraic identity.

- **[[Thm - Upper-Triangular Form on Complex Vector Spaces]]** — the existential lemma. Without an upper-triangular basis, the diagonal-equals-eigenvalues argument does not start. Over $\mathbb{R}$ the upper-triangular form may fail (an operator may have no real eigenvalues), and the theorem fails along with it.

- **[[Def - Algebraic and Geometric Multiplicity]]** — the multiplicity counting. The algebraic multiplicity equals the number of times the eigenvalue appears on the diagonal of any upper-triangular matrix of $T$ — the proof of this in §8B of LADR uses the null-space stabilisation argument.

- **Determinant equals product of eigenvalues** (proved in [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]]) — the analogous result for the other extreme symmetric function. Trace and determinant are the first and last coefficients (up to sign) of the characteristic polynomial; both have basis-independent meanings.

- **Newton's identities** — the algebraic dictionary between power sums and elementary symmetric polynomials. Given $\operatorname{tr}(T^k)$ for $k = 1, \dots, n$, Newton's identities reconstruct the characteristic polynomial. This is how one extracts eigenvalues from traces of iterates without diagonalising.

---

# Unlocked by This

> [!tip] Trace Identity for the Characteristic Polynomial
> The coefficient of $z^{n-1}$ in the characteristic polynomial is $-\operatorname{tr} T$. Together with the constant term being $(-1)^n \det T$, this gives the two extreme coefficients explicitly. Newton's identities then fill in the intermediate coefficients from $\operatorname{tr}(T^k)$ for $k = 2, \dots, n$.

> [!tip] Quantum-Mechanical Expectation Values
> The trace identity is the algebraic foundation of quantum measurement: expectation values are traces over the spectrum, weighted by the density matrix. The basis-independence of the trace is the statement that physics does not depend on the choice of measurement basis.

> [!tip] Partition Function in Statistical Mechanics
> $Z(\beta) = \operatorname{tr}(e^{-\beta H})$ encodes the spectrum of $H$. The free energy $F = -\beta^{-1} \log Z$ generates moments of $H$ via differentiation. The trace identity here is the spectral decomposition of $Z$ as a sum of Boltzmann factors $\sum_n e^{-\beta E_n}$ — the link from the algebraic operator $H$ to the thermodynamic ensemble.

> [!tip] Trace as Lie Algebra Functional *(from Lie Theory)*
> The trace is the differential of the determinant at the identity: $\det(I + \varepsilon X) = 1 + \varepsilon \operatorname{tr} X + O(\varepsilon^2)$. The kernel $\mathfrak{sl}(V) = \{X : \operatorname{tr}(X) = 0\}$ is the **special linear Lie algebra**, the Lie algebra of $\mathrm{SL}(V)$. The relation $\operatorname{tr}([X, Y]) = 0$ — the Lie-algebraic version of cyclicity — is the infinitesimal form of conjugation-invariance.

> [!tip] Spectral Methods in Numerical Linear Algebra
> The **power method** for computing the largest eigenvalue uses $\operatorname{tr}(T^k) \approx \lambda_{\max}^k$ for large $k$ when $|\lambda_{\max}| > |\lambda_j|$ for all other $j$. More sophisticated **Lanczos** and **Arnoldi** methods leverage similar trace-based identities. The Jordan form theoretical guarantees in [[Thm - Existence of Jordan Form]] are what justify these numerical procedures.
