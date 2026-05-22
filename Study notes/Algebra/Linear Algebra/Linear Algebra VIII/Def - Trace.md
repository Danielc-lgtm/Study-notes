---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Matrix of a Linear Map"
  - "Def - Change of Basis Matrix"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional nonzero vector space over $\mathbf{F} \in \{\mathbb{R}, \mathbb{C}\}$ and $T \in \mathcal{L}(V)$. $\mathcal{M}(T, (v_1, \dots, v_n))$ is the matrix of $T$ in the ordered basis $v_1, \dots, v_n$. For a square matrix $A \in M_n(\mathbf{F})$, $A_{i,j}$ denotes the entry in row $i$, column $j$. Full registry on [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

This is a compound page: it defines two interlocking notions — the *trace of a matrix* and the *trace of an operator* — because the second depends on the first (and on the cyclic identity $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ to ensure well-definedness), and neither is fully usable without the other.

---

# Axiom Motivation

The trace is the simplest non-trivial linear functional on the space of operators $\mathcal{L}(V)$. It assigns to each operator a single number, basis-independently, and it is the *one* scalar invariant that can be read off any matrix without any structural analysis — no diagonalisation, no eigenvalue computation, no normal forms. Just add up the diagonal entries. Yet it carries genuine spectral information: on a complex space, the trace equals the sum of the eigenvalues with multiplicity ([[Thm - Trace Equals Sum of Eigenvalues]]).

The first question is: *what is the right way to assign a number to a matrix?* The obvious candidates are the sum of entries, the sum of diagonal entries, the product of diagonal entries, the determinant, the sum of squares of entries, and so on. The constraint we want to satisfy is **basis-independence**: when $A$ represents an operator $T$ in one basis and $B$ represents the same $T$ in another basis, we want our assigned number to be the same. The change-of-basis formula says $B = C^{-1} A C$ for some invertible $C$ (see [[Def - Change of Basis Matrix]]). So our function $f : M_n(\mathbf{F}) \to \mathbf{F}$ must satisfy $f(C^{-1} A C) = f(A)$ for all invertible $C$ — a class function on $M_n(\mathbf{F})$ under conjugation.

The candidates differ sharply on this test. The sum-of-all-entries is not conjugation-invariant: conjugating $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ by various $C$ changes the off-diagonal entries while leaving the sum on the diagonal alone, and the sum-of-all-entries changes. The sum-of-squares-of-entries is also not conjugation-invariant (this is the Frobenius norm; it depends on the basis). The product of diagonal entries is not conjugation-invariant either. But two functions *are*: the sum of diagonal entries (the trace), and the determinant.

The sum-of-diagonal-entries succeeds because of the **cyclic property** of matrix multiplication:

$$\operatorname{tr}(AB) = \sum_i \sum_j A_{i,j} B_{j,i} = \sum_j \sum_i B_{j,i} A_{i,j} = \operatorname{tr}(BA).$$

This *single* identity is the engine of basis-independence: writing $\operatorname{tr}(C^{-1} A C) = \operatorname{tr}((C^{-1} A) C) = \operatorname{tr}(C (C^{-1} A)) = \operatorname{tr}((CC^{-1}) A) = \operatorname{tr}(A)$, the cyclic shuffle of the three factors converts the conjugate-trace into the original trace. The trace is conjugation-invariant *because* of cyclicity, and cyclicity is in turn an immediate consequence of the commutativity of scalar multiplication (the sum $\sum_{i,j} A_{i,j} B_{j,i}$ is the same as $\sum_{i,j} B_{j,i} A_{i,j}$, since scalar entries commute).

The determinant also satisfies conjugation-invariance, via the multiplicativity $\det(AB) = \det(A) \det(B)$. It is multiplicatively cyclic: $\det(AB) = \det(BA)$ for $A, B$ square, even though it is *not* additive. So the determinant is the *multiplicative* analogue of the trace.

Why pick the trace among the conjugation-invariants? Because it is **linear**: $\operatorname{tr}(\lambda T) = \lambda \operatorname{tr}(T)$ and $\operatorname{tr}(S + T) = \operatorname{tr}(S) + \operatorname{tr}(T)$. The trace is a *linear functional* on $\mathcal{L}(V)$, the simplest kind of function. The determinant is multilinear and not linear. So if you want one scalar invariant that respects linearity, the trace is essentially forced.

In fact, the trace is the *unique* linear functional on $\mathcal{L}(V)$ (up to scalar multiple) satisfying $\operatorname{tr}(ST) = \operatorname{tr}(TS)$, normalised by $\operatorname{tr}(I) = \dim V$. The uniqueness is exercise 10 of §8D in LADR: any other such linear functional must equal the trace by a check on the basis matrices $P_{j,k}$ that send $v_k \mapsto v_j$ and other basis vectors to $0$. So the trace is the canonical object; everything else is its multiple.

A failure analysis: if we tried to define a "matrix-only" notion of trace (the sum of diagonal entries, no basis-independence claim) and then *operator* trace by some other route, we would have to either pick a basis (and accept basis-dependence) or pick a definition without using matrices at all. The latter is possible — for instance, in a coordinate-free language, $\operatorname{tr} T$ is the contraction of $T$ regarded as a $(1, 1)$-tensor; or it is the value of the **dual pairing** between $T \in \operatorname{End}(V) \cong V \otimes V^*$ and the identity element $I \in V \otimes V^* \cong \operatorname{End}(V)^*$. These definitions are coordinate-free and rigorous, but they require the language of tensors and dual spaces, which are exactly what one usually introduces *after* the trace. The pragmatic choice is to define the matrix trace first, prove cyclicity, then upgrade to operators via basis-independence — exactly the order Axler follows.

---

# The Definition

**Trace of a matrix.** Suppose $A$ is a square matrix with entries in $\mathbf{F}$. The **trace** of $A$, denoted $\operatorname{tr} A$, is the sum of the diagonal entries:

$$\operatorname{tr} A \;=\; \sum_i A_{i, i}.$$

**Cyclic property.** If $A$ is $m \times n$ and $B$ is $n \times m$, then $AB$ is $m \times m$ and $BA$ is $n \times n$, and

$$\operatorname{tr}(AB) \;=\; \operatorname{tr}(BA).$$

**Trace of an operator.** Suppose $T \in \mathcal{L}(V)$. The **trace** of $T$, denoted $\operatorname{tr} T$, is

$$\operatorname{tr} T \;=\; \operatorname{tr} \mathcal{M}(T, (v_1, \dots, v_n))$$

for any basis $v_1, \dots, v_n$ of $V$. By the change-of-basis formula and the cyclic property, this is independent of the basis chosen: if $A$ and $B$ are matrices of $T$ in two bases, related by $B = C^{-1} A C$ for an invertible $C$, then

$$\operatorname{tr} B = \operatorname{tr}(C^{-1} A C) = \operatorname{tr}(A C C^{-1}) = \operatorname{tr}(A I) = \operatorname{tr} A.$$

**Algebraic properties.** The trace $\operatorname{tr} : \mathcal{L}(V) \to \mathbf{F}$ is a **linear functional**:
$$\operatorname{tr}(\lambda T) = \lambda \operatorname{tr}(T), \qquad \operatorname{tr}(S + T) = \operatorname{tr}(S) + \operatorname{tr}(T)$$
for all $\lambda \in \mathbf{F}$ and $S, T \in \mathcal{L}(V)$. It also satisfies the cyclic identity $\operatorname{tr}(ST) = \operatorname{tr}(TS)$ for all $S, T \in \mathcal{L}(V)$.

In addition, $\operatorname{tr} I = \dim V$, and the trace is *uniquely* characterised among linear functionals on $\mathcal{L}(V)$ by these two properties.

On a complex space, $\operatorname{tr} T$ equals the sum of the eigenvalues of $T$ with multiplicity — see [[Thm - Trace Equals Sum of Eigenvalues]].

---

# Categorical / Structural Definition

The trace can be defined coordinate-freely as the **contraction** of an endomorphism. In categorical language, the space $\operatorname{End}(V) = V \otimes V^*$ admits a canonical evaluation map $\operatorname{ev} : V \otimes V^* \to \mathbf{F}$ given by $v \otimes \phi \mapsto \phi(v)$; the trace of an endomorphism is the value of this evaluation map after the canonical identification $\operatorname{End}(V) \cong V \otimes V^*$. Concretely, if $T = \sum_i v_i \otimes \phi_i$ in this identification then $\operatorname{tr} T = \sum_i \phi_i(v_i)$.

Equivalently, the trace is the unique element of $V \otimes V^*$ corresponding to the identity $I \in \operatorname{End}(V) \cong V \otimes V^*$, evaluated via the canonical pairing $V \otimes V^* \to \mathbf{F}$. This is the **dual basis identity**: if $v_1, \dots, v_n$ is a basis with dual basis $\phi_1, \dots, \phi_n$ ($\phi_i(v_j) = \delta_{ij}$), then $I = \sum_i v_i \otimes \phi_i$, and applying $\operatorname{ev}$ to both sides gives $\operatorname{tr}(I) = \sum_i \phi_i(v_i) = \sum_i 1 = n$.

In Lie-theoretic terms, the trace is the unique (up to scalar) ad-invariant linear functional on $\mathfrak{gl}(V) = \operatorname{End}(V)$: $\operatorname{tr}([X, Y]) = \operatorname{tr}(XY - YX) = 0$ for all $X, Y$, exactly the cyclic property. The kernel $\mathfrak{sl}(V) = \{X : \operatorname{tr}(X) = 0\}$ is the **special linear Lie algebra**.

---

# Relate to Other Fields / Compression

**True name:** The trace is *the simplest invariant of an operator — its only invariant that is linear in the operator and basis-independent*. Every linear functional on $\mathcal{L}(V)$ that vanishes on commutators (i.e. satisfies $\operatorname{tr}(ST) = \operatorname{tr}(TS)$) is a scalar multiple of the trace; this characterisation, together with the normalisation $\operatorname{tr} I = \dim V$, makes the trace canonical.

In differential geometry, the trace of the Jacobian $\operatorname{tr}(Df)_x$ is the **divergence** of the vector field $f$ at $x$ (see [[Def - Partial Derivatives and the Jacobian Matrix]]). For a flow $\dot x = f(x)$, Liouville's theorem says the rate of change of phase-space volume along the flow is $\operatorname{tr}(Df)$, so trace-zero (divergence-free) flows preserve volume — these are the *Hamiltonian* and *incompressible* flows. The trace is thus the linear-algebraic shadow of *volume preservation* in dynamical systems.

In probability theory, $\operatorname{tr}(AB)$ where $A$ is a covariance matrix and $B$ is a positive operator gives the *expected quadratic form* — relevant for $\chi^2$ statistics, second-moment computations, and the trace inner product on covariance matrices.

In quantum mechanics, the trace defines the **expectation value** of an observable in a mixed state: $\langle A \rangle = \operatorname{tr}(\rho A)$ where $\rho$ is the density matrix and $A$ is the observable. The cyclic property is here the **invariance under change of basis on the Hilbert space**, and the linearity is the **superposition principle** for mixed states.

A third compression — and the connection to Lie theory — is that the trace is *the differential of the determinant at the identity*: $\det(I + \varepsilon X) = 1 + \varepsilon \operatorname{tr}(X) + O(\varepsilon^2)$. So the trace is to determinant as derivative is to function — the *infinitesimal* version of the multiplicative invariant. Equivalently, in the Lie algebra–Lie group correspondence, $\mathfrak{gl}(V) \to \mathfrak{F}$ given by $X \mapsto \operatorname{tr}(X)$ is the Lie-algebra functional corresponding to the Lie-group homomorphism $\det : \mathrm{GL}(V) \to \mathbf{F}^\times$, and the kernel of one matches the kernel of the other under the exponential map: $\mathfrak{sl}(V) = \exp^{-1}(\mathrm{SL}(V))$ in a precise sense.

---

# Examples / Corollaries

**Is an instance — diagonal matrix.** For $A = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$, $\operatorname{tr} A = \lambda_1 + \cdots + \lambda_n$. This is the simplest case, and it is the form that makes the spectral formula "$\operatorname{tr} T = $ sum of eigenvalues" most transparent.

**Is an instance — upper-triangular matrix.** For $A$ upper-triangular with diagonal entries $\lambda_1, \dots, \lambda_n$, $\operatorname{tr} A = \lambda_1 + \cdots + \lambda_n$. Because the diagonal entries of an upper-triangular matrix of $T$ are exactly the eigenvalues of $T$ counted with multiplicity ([[Thm - Upper-Triangular Form on Complex Vector Spaces]] + [[Def - Algebraic and Geometric Multiplicity]]), this confirms $\operatorname{tr} T = \sum d_k \lambda_k$ even before invoking the full spectral theorem.

**Is an instance — Jordan block.** For $A = J_k(\lambda)$ the Jordan block of size $k$ for $\lambda$, the diagonal is all $\lambda$ and there are $k$ entries, so $\operatorname{tr} J_k(\lambda) = k \lambda$. This is the contribution of one Jordan block to the trace — equal to the eigenvalue times the block size — and summing over all blocks gives the spectral formula.

**Is an instance — explicit $3 \times 3$ computation.** For $A = \begin{pmatrix} 3 & -1 & -2 \\ 3 & 2 & -3 \\ 1 & 2 & 0 \end{pmatrix}$, the diagonal entries are $3, 2, 0$, so $\operatorname{tr} A = 5$. The eigenvalues of $A$ turn out to be $1$, $2 + 3i$, $2 - 3i$, each with multiplicity $1$, and $1 + (2 + 3i) + (2 - 3i) = 5$. The trace is computed in one step from the matrix; computing the eigenvalues required either expanding a determinant or guessing.

**Is NOT an instance — sum of all entries.** For the same matrix $A$ above, the sum of all entries is $3 - 1 - 2 + 3 + 2 - 3 + 1 + 2 + 0 = 5$. By coincidence this matches the trace, but if we change the off-diagonal entries (which does change the eigenvalues), the trace stays at $5$ while the sum of all entries changes. The trace ignores the off-diagonal entries entirely. The sum-of-entries is *not* a similarity invariant; the trace is. Try, for instance, $A' = \begin{pmatrix} 3 & 7 & 2 \\ -1 & 2 & 5 \\ 0 & -3 & 0 \end{pmatrix}$ (which has the same diagonal as $A$, hence the same trace, but different sum of entries): $\operatorname{tr} A' = 5$ still, and indeed $A$ and $A'$ have the same trace because both represent operators with the same first symmetric function of eigenvalues, even though their full eigenvalue lists differ in general.

**Is NOT an instance — $\operatorname{tr}(AB) \neq (\operatorname{tr} A)(\operatorname{tr} B)$ in general.** Take $A = \operatorname{diag}(1, 0)$ and $B = \operatorname{diag}(0, 1)$. Then $\operatorname{tr} A = \operatorname{tr} B = 1$, but $AB = \operatorname{diag}(0, 0) = 0$, so $\operatorname{tr}(AB) = 0 \neq 1$. The trace is *linear* in $T$ but not *multiplicative*: $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ is the right cyclic identity, not $\operatorname{tr}(AB) = (\operatorname{tr} A)(\operatorname{tr} B)$.

**Corollary — basis-independence.** For invertible $C$, $\operatorname{tr}(C^{-1} A C) = \operatorname{tr}(A)$. Proof: by cyclicity, $\operatorname{tr}(C^{-1} A C) = \operatorname{tr}((C^{-1} A) C) = \operatorname{tr}(C (C^{-1} A)) = \operatorname{tr}((C C^{-1}) A) = \operatorname{tr}(A)$.

**Corollary — additivity, scalar-out, $\operatorname{tr} I = \dim V$.** Direct from the definition. The linearity makes $\operatorname{tr}$ a linear functional on $\mathcal{L}(V)$; the value at the identity equals $\dim V$.

**Corollary — $\operatorname{tr}(\lambda I) = \lambda \dim V$ and $\operatorname{tr}(\lambda I + N) = \lambda \dim V + \operatorname{tr}(N)$.** The trace of a multiple of identity is *linear* in the multiplier. On a generalized eigenspace $G(\lambda, T)$ of dimension $d$, $T|_{G(\lambda, T)} = \lambda I + N$ with $N$ nilpotent, so $\operatorname{tr}(T|_{G(\lambda, T)}) = \lambda d + \operatorname{tr}(N) = \lambda d + 0 = \lambda d$ (since the trace of a nilpotent operator on a complex space is zero — its only eigenvalue is $0$, with multiplicity equal to the dimension, summing to $0$). Hence $\operatorname{tr} T = \sum_k \lambda_k d_k$, recovering the spectral formula.

**Corollary — identity is not a commutator.** There do not exist $S, T \in \mathcal{L}(V)$ with $ST - TS = I$. Proof: take traces of both sides. The trace of the left side is $\operatorname{tr}(ST) - \operatorname{tr}(TS) = 0$ by cyclicity, but the trace of the right side is $\operatorname{tr}(I) = \dim V \neq 0$. Contradiction. This is the famous LADR theorem 8.57 and is one of the cleanest demonstrations of the trace's utility — a statement *not involving traces in its statement* gets a one-line proof via the trace. (In infinite dimensions the result fails: the canonical commutation relation $[Q, P] = i \hbar I$ of quantum mechanics shows the identity *is* a commutator for unbounded operators on an infinite-dimensional Hilbert space.)

**Calibration check.** For $T \in \mathcal{L}(\mathbb{C}^3)$ with matrix $\begin{pmatrix} 51 & -12 & -21 \\ 60 & -40 & -28 \\ 57 & -68 & 1 \end{pmatrix}$, compute $\operatorname{tr} T = 51 - 40 + 1 = 12$. Suppose you are told two eigenvalues are $-48$ and $24$. The third eigenvalue $\mu$ satisfies $-48 + 24 + \mu = 12$ by the trace identity, so $\mu = 36$. You have just computed a missing eigenvalue without diagonalising — this is the prototypical use of the trace, and the central exercise [[Exercise Index - §8D Trace|8D.7]] of LADR.

---

# Unlocked by This

> [!tip] Trace Equals Sum of Eigenvalues *(from this topic)*
> On a complex space, $\operatorname{tr} T = \sum_k d_k \lambda_k$ where $\lambda_k$ are the eigenvalues and $d_k$ the multiplicities. See [[Thm - Trace Equals Sum of Eigenvalues]] and the explicit derivation via the upper-triangular form.

> [!tip] Hilbert–Schmidt Inner Product on Operators *(from Functional Analysis)*
> On an inner product space, $\langle S, T \rangle = \operatorname{tr}(T^* S)$ defines an inner product on $\mathcal{L}(V)$ — the **Hilbert–Schmidt** (or **Frobenius**) inner product. The associated norm $\|T\|_{HS} = \sqrt{\operatorname{tr}(T^* T)} = \sqrt{\sum_{i,j} |T_{i,j}|^2}$ is the sum of squares of matrix entries (basis-independent on orthonormal bases). This inner product is the standard object on operator spaces in quantum mechanics and quantum information theory.

> [!tip] Liouville's Theorem and Phase-Space Volume *(from Dynamical Systems / Statistical Mechanics)*
> For a flow $\dot x = f(x)$ in $\mathbb{R}^n$, the rate of change of phase-space volume along the flow is $\operatorname{tr}(Df)$ (the divergence). Hamiltonian flows have $\operatorname{tr}(Df) = 0$ — they preserve phase-space volume. This is **Liouville's theorem**, the linear-algebraic foundation for the use of phase-space density in statistical mechanics, and the reason the **microcanonical ensemble** is well-defined.

> [!tip] Trace as Lie Algebra Functional *(from Lie Theory)*
> The trace is the differential of the determinant at the identity: $\det(I + \varepsilon X) = 1 + \varepsilon \operatorname{tr}(X) + O(\varepsilon^2)$. Its kernel $\mathfrak{sl}(V) = \{X : \operatorname{tr}(X) = 0\}$ is the **special linear Lie algebra**, the Lie algebra of $\mathrm{SL}(V)$. The decomposition $\mathfrak{gl}(V) = \mathfrak{sl}(V) \oplus \mathbf{F} \cdot I$ at the Lie-algebra level mirrors $\mathrm{GL}(V) / \mathrm{SL}(V) \cong \mathbf{F}^\times$ at the Lie-group level via $\det$.

> [!tip] Trace and the Characteristic Polynomial *(from Multilinear Algebra)*
> The trace is the negative of the coefficient of $z^{n-1}$ in the characteristic polynomial $p_T(z) = z^n - (\operatorname{tr} T) z^{n-1} + \cdots + (-1)^n \det T$. Together with the determinant (the constant term up to sign), the trace gives the first two elementary symmetric functions of the eigenvalues. Newton's identities then give power sums $\operatorname{tr}(T^j) = \sum_k d_k \lambda_k^j$ recursively. See [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] for the full theory.
