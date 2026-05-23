---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Eigenvalue and Eigenvector"
  - "Def - Minimal Polynomial"
  - "Def - Invariant Subspace"
  - "Thm - Existence of Eigenvalues on Complex Vector Spaces"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over $F$, $T \in \mathcal{L}(V)$ an operator. A matrix $A = (A_{j,k})$ is **upper triangular** if $A_{j,k} = 0$ for $j > k$. The diagonal entries are $A_{1,1}, A_{2,2}, \ldots, A_{n,n}$. The full registry is on the parent page [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

---

# Statement

> **Theorem (Upper-Triangular Form on $\mathbb{C}$).** Let $V$ be a finite-dimensional complex vector space and $T \in \mathcal{L}(V)$. Then there is a basis $v_1, v_2, \ldots, v_n$ of $V$ with respect to which the matrix of $T$ is upper triangular.

> **Theorem (Upper-Triangular Form, General).** Let $V$ be a finite-dimensional vector space over a field $F$ and $T \in \mathcal{L}(V)$. Then $T$ has an upper-triangular matrix with respect to some basis of $V$ **if and only if** the minimal polynomial $m_T$ factors as
> $$m_T(z) = (z - \lambda_1)(z - \lambda_2) \cdots (z - \lambda_m)$$
> for some $\lambda_1, \ldots, \lambda_m \in F$ (with the linear factors not necessarily distinct).

The complex case is an immediate corollary of the general case combined with the fundamental theorem of algebra, since over $\mathbb{C}$ every polynomial factors into linear factors.

> **Corollary.** Let $T$ have upper-triangular matrix with diagonal entries $\lambda_1, \ldots, \lambda_n$. Then the set of eigenvalues of $T$ is $\{\lambda_1, \ldots, \lambda_n\}$.

---

# Motivation

Upper-triangular form is **the basic structural reduction available for an operator over an algebraically closed field**. While diagonalisation is not always possible — repeated eigenvalues with insufficient eigenvectors block it — upper-triangularisation is *always* possible over $\mathbb{C}$. This theorem says: even when an operator has Jordan blocks of size $> 1$, you can at least arrange its matrix to be upper triangular, with the eigenvalues read off the diagonal.

The motivation in three steps:
1. **Diagonalisation is too strong.** Many operators (those with repeated minimal-polynomial factors) are not diagonalizable. A weaker, more universally available reduction is needed.
2. **Upper-triangular is the right weakening.** It still puts the matrix in a "structured" form (zeros below the diagonal), and the diagonal entries are still the eigenvalues. Computations of powers, traces, [[Def - Determinant|determinants]], and characteristic polynomials remain simple in upper-triangular form.
3. **It exists over $\mathbb{C}$.** This is the substance of the theorem. The proof is iterative — find one eigenvalue and corresponding eigenvector $v_1$, then descend to a quotient and repeat.

The theorem is the basis of **most induction-on-[[Def - Dimension|dimension]] proofs** in subsequent chapters. The Schur decomposition (the inner-product-space refinement), the Jordan form (the further refinement to "block diagonal of Jordan blocks"), and the spectral theorem (a further refinement for normal operators) all rest on upper-triangularizability as their foundation.

The general (field-independent) statement reveals the structural content: upper-triangularizability is **exactly equivalent to the minimal polynomial factoring into linear factors over $F$**. Over $\mathbb{C}$ this is automatic; over $\mathbb{R}$ it can fail (rotation has $m_T = z^2 + 1$, irreducible), and this failure is exactly the failure of upper-triangularisation over $\mathbb{R}$.

---

# Sources and Targets

**Sources (Input Broadening)**

The complex case has only one precondition ($F = \mathbb{C}$, $V$ finite-dimensional). The general case requires the minimal polynomial to factor into linear factors.

The first disguised source is **$T$ has an annihilating polynomial that splits into linear factors over $F$**. Even without knowing $m_T$, if you can find some $p \in F[x]$ with $p(T) = 0$ and $p$ splitting into linear factors (over $F$), then $m_T \mid p$, so $m_T$ also splits. *Example problem:* "Show that $T$ with $T^k = I$ over $\mathbb{C}$ has an upper-triangular form." Disguised source: $T$ annihilates $z^k - 1$, which factors over $\mathbb{C}$.

The second disguised source is **$T$ commutes with $S$, both on a complex vector space**. Then [[Ex - Commuting operators share an eigenvector on complex spaces|commuting operators share an eigenvector]], which is the base step of the inductive simultaneous-triangularisation argument. *Example problem:* "Show that two commuting operators on $\mathbb{C}^n$ have a common upper-triangular form." Disguised source: shared eigenvector by commutativity.

The third disguised source is **the underlying field is algebraically closed**. The fundamental theorem of algebra is the algebraic statement that $\mathbb{C}$ is algebraically closed; the theorem applies over any algebraically closed field of characteristic zero (and indeed any field, modulo the factoring hypothesis).

**Targets (Output Amplification)**

Combined with **the diagonal-entries-are-eigenvalues fact**, the theorem amplifies to: *over $\mathbb{C}$, an operator's eigenvalues can be read off the diagonal of any upper-triangular matrix representing it, with appropriate counting for multiplicities*.

Combined with **invertibility = no zero on the diagonal**, the theorem amplifies to: *over $\mathbb{C}$, $T$ is invertible iff $0$ is not an eigenvalue*. This is one of the most-used facts in operator theory and is the proof of the equivalent statement "$T$ is invertible iff $\det T \neq 0$" (once determinants are defined).

Combined with **inductive structural arguments**, the theorem is the foundation of subsequent canonical-form results: the [[Thm - Generalized Eigenspace Decomposition]], the [[Thm - Jordan Normal Form]], and the [[Thm - Complex Spectral Theorem]] all use upper-triangularisation as the first move.

---

# Why Is It True

The mechanism is **iterative descent along a flag of invariant [[Def - Subspace|subspaces]]**. Over $\mathbb{C}$, every operator has an eigenvalue, hence a one-dimensional invariant subspace; quotient by it, the resulting operator on the smaller-dimensional quotient has an eigenvalue, hence a one-dimensional invariant subspace; continue. This builds a chain
$$\{0\} = V_0 \subset V_1 \subset V_2 \subset \cdots \subset V_n = V$$
with $\dim V_k = k$ and each $V_k$ $T$-invariant. Pick $v_k \in V_k \setminus V_{k-1}$; the resulting basis $v_1, \ldots, v_n$ satisfies $T v_k \in V_k$, which in matrix form says $T v_k$ has no components in directions $v_{k+1}, \ldots, v_n$ — that is, the matrix is upper triangular.

> **The mechanism in one sentence: every operator on a complex vector space has an eigenvector (giving an invariant line); descend to the quotient and iterate to build an invariant flag whose chosen basis triangulises $T$.**

The general statement (over an arbitrary $F$, requiring $m_T$ to split) follows the same induction but uses the *minimal polynomial* directly: if $m_T$ has a root $\lambda \in F$, we get an eigenvalue, hence an invariant line, and we induct on the quotient where the minimal polynomial still splits (this requires checking that the minimal polynomial of the quotient operator divides $m_T$, hence also splits).

---

# What Makes This Hard

There are two non-obvious moves. First, the **induction must be on the quotient $V/V_k$, not on a complementary subspace**. Picking a complement requires a choice, and the choice need not be $T$-invariant; the quotient is canonical. Second, the **upper-triangularity is verified by checking $T v_k \in V_k = \operatorname{span}(v_1, \ldots, v_k)$**, not by directly computing the matrix entries below the diagonal. The connection between the two — that $T v_k \in V_k$ is equivalent to "no entries below the diagonal in column $k$" — is the **conditions-for-upper-triangular** lemma (Axler 5.39), which is a standalone preliminary result (it is Lemma 1 below).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Build a flag of $T$-invariant [[Def - Subspace|subspaces]] inductively, using the existence-of-eigenvalues theorem at each step. Pick a basis adapted to the flag; that basis triangulises $T$.

**Subgoal decomposition:**

1. **Invariant flag from iterated eigenvalues.** Build $\{0\} = V_0 \subset V_1 \subset \cdots \subset V_n = V$ with $\dim V_k = k$ and each $V_k$ $T$-invariant.
   - *Hint:* on $V/V_{k-1}$ (a complex vector space of [[Def - Dimension|dimension]] $n - k + 1$), the induced operator has an eigenvalue, hence a one-dimensional invariant subspace $\bar L = V_k / V_{k-1}$; lift to $V_k$.
   - *Why needed:* the flag is the data that produces the upper-triangular basis.

2. **Basis adapted to the flag.** Pick $v_k \in V_k \setminus V_{k-1}$ for each $k$. Then $v_1, \ldots, v_n$ is a basis of $V$.
   - *Hint:* since $V_k$ has dimension $k$ and $V_{k-1}$ has dimension $k - 1$, any vector $v_k \in V_k \setminus V_{k-1}$ extends $V_{k-1}$ to $V_k$; combine.
   - *Why needed:* this is the basis in which $T$ is triangular.

3. **In this basis, $T$ is upper triangular.** $T v_k \in T V_k \subseteq V_k = \operatorname{span}(v_1, \ldots, v_k)$, so the coordinates of $T v_k$ in the basis are zero for indices $> k$. This is the upper-triangular condition.
   - *Hint:* invariance gives $T V_k \subseteq V_k$; the basis-vector coordinates encode "no components in $v_{k+1}, \ldots, v_n$".
   - *Why needed:* extracts the matrix form from the geometric construction.

4. **General-field version.** If $m_T$ factors into linear factors $(z - \lambda_1) \cdots (z - \lambda_m)$ over $F$, the same induction works using these factors to produce eigenvectors at each step. The minimal polynomial of the quotient $T/V_{k-1}$ divides $m_T$, so it also factors into linear factors over $F$ — the inductive hypothesis remains satisfied.

---

# Lemma Decomposition

> [!note]- Lemma 1: Upper-triangular matrix iff each $V_k = \operatorname{span}(v_1, \ldots, v_k)$ is $T$-invariant
> **Statement:** Let $v_1, \ldots, v_n$ be a basis of $V$. The matrix of $T$ in this basis is upper triangular if and only if $V_k = \operatorname{span}(v_1, \ldots, v_k)$ is $T$-invariant for each $k = 1, \ldots, n$.
>
> **Hint:** upper-triangular means $T v_k$ has no components on $v_{k+1}, \ldots, v_n$, i.e. $T v_k \in V_k$; invariance of $V_k$ for all $k$ is exactly this.
>
> **Why needed:** translates the geometric "invariant flag" picture into the matrix form.
>
> > [!note]- Full proof
> > Suppose the matrix of $T$ is upper triangular with respect to $v_1, \ldots, v_n$. Then for each $k$, $T v_k = A_{1,k} v_1 + A_{2,k} v_2 + \cdots + A_{k,k} v_k$ — no components on $v_{k+1}, \ldots, v_n$. So $T v_k \in \operatorname{span}(v_1, \ldots, v_k) = V_k$. Hence $T V_k = \operatorname{span}(T v_1, \ldots, T v_k) \subseteq V_k$ (since each $T v_j$ for $j \leq k$ is in $V_j \subseteq V_k$). So each $V_k$ is $T$-invariant.
> >
> > Conversely, if each $V_k$ is $T$-invariant, then $T v_k \in T V_k \subseteq V_k = \operatorname{span}(v_1, \ldots, v_k)$. So the coordinates of $T v_k$ in the basis are zero for indices $> k$, meaning $A_{j,k} = 0$ for $j > k$. So the matrix is upper triangular.

> [!note]- Lemma 2: Quotient operator $T/V_{k-1}$ is well-defined
> **Statement:** Let $U \leq V$ be $T$-invariant. The map $T/U : V/U \to V/U$ defined by $(T/U)(v + U) = Tv + U$ is well-defined and linear.
>
> **Hint:** well-defined: if $v + U = v' + U$, then $v - v' \in U$, so $T(v - v') \in U$ (by invariance), so $Tv - Tv' \in U$, hence $Tv + U = Tv' + U$.
>
> **Why needed:** the inductive step uses the quotient operator.
>
> > [!note]- Full proof
> > To check well-definedness, suppose $v + U = v' + U$, i.e. $v - v' \in U$. By $T$-invariance of $U$, $T(v - v') \in U$, i.e. $Tv - Tv' \in U$, i.e. $Tv + U = Tv' + U$. So the map $(T/U)(v + U) = Tv + U$ does not depend on the choice of representative. Linearity is immediate from linearity of $T$: $(T/U)((v + U) + (w + U)) = (T/U)((v + w) + U) = T(v + w) + U = (Tv + U) + (Tw + U)$, and similarly for scalar multiplication.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V$ be a finite-dimensional complex vector space and $T \in \mathcal{L}(V)$, $n = \dim V$.
>
> **Step 0 — base case.** If $n = 1$, any nonzero vector is a basis and gives a $1 \times 1$ "upper-triangular" matrix.
>
> **Step 1 — induct on dimension.** Assume the result for all complex vector spaces of dimension $< n$.
>
> **Step 2 — find an eigenvector $v_1$.** By [[Thm - Existence of Eigenvalues on Complex Vector Spaces]], $T$ has an eigenvalue $\lambda_1 \in \mathbb{C}$ with eigenvector $v_1 \neq 0$. Let $V_1 = \operatorname{span}(v_1)$; this is a one-dimensional $T$-invariant subspace, and $T v_1 = \lambda_1 v_1$.
>
> **Step 3 — descend to the quotient.** Let $V' = V / V_1$ (dimension $n - 1$), and let $T' = T / V_1$ be the induced operator on $V'$ (well-defined by Lemma 2 since $V_1$ is $T$-invariant). By the inductive hypothesis applied to $T'$, there is a basis $\bar v_2, \bar v_3, \ldots, \bar v_n$ of $V'$ with respect to which the matrix of $T'$ is upper triangular. Lift each $\bar v_k$ to a vector $v_k \in V$ — that is, pick $v_k \in V$ with $v_k + V_1 = \bar v_k$.
>
> **Step 4 — $v_1, v_2, \ldots, v_n$ is a basis of $V$.** The list $v_1$ together with $v_2, \ldots, v_n$ (which project to a basis of $V/V_1$) is a basis of $V$ by the dimension count: $\dim V_1 + \dim V/V_1 = n$, so any basis of each plus a basis of the other gives a basis of $V$.
>
> **Step 5 — the matrix of $T$ in this basis is upper triangular.** It suffices (by Lemma 1) to show that $V_k = \operatorname{span}(v_1, v_2, \ldots, v_k)$ is $T$-invariant for each $k$. For $k = 1$, $V_1$ is $T$-invariant by Step 2.
>
> For $k \geq 2$: the inductive hypothesis says the matrix of $T'$ in $\bar v_2, \ldots, \bar v_n$ is upper triangular, so $T' \bar v_k \in \operatorname{span}(\bar v_2, \ldots, \bar v_k)$. Lifting: $T v_k + V_1 = T'(v_k + V_1) = T' \bar v_k \in \operatorname{span}(\bar v_2, \ldots, \bar v_k) = \operatorname{span}(v_2, \ldots, v_k) / V_1$. So $T v_k \in V_1 + \operatorname{span}(v_2, \ldots, v_k) = \operatorname{span}(v_1, v_2, \ldots, v_k) = V_k$. So $V_k$ is $T$-invariant. $\blacksquare$

> [!note]- General-field version
> Suppose $V$ is a finite-dimensional vector space over an arbitrary field $F$, and $m_T$ factors over $F$ as $(z - \lambda_1) \cdots (z - \lambda_m)$. The same induction works: by [[Thm - Eigenvalues are Zeros of the Minimal Polynomial]], $\lambda_1$ is an eigenvalue, so the existence-of-eigenvalue conclusion holds without needing $\mathbb{C}$; the quotient operator $T'$ has minimal polynomial dividing $m_T$ (by [[Def - Minimal Polynomial]] property 4), hence also factors into linear factors over $F$, so the induction continues.
>
> Conversely, suppose $T$ has an upper-triangular matrix with diagonal $\alpha_1, \ldots, \alpha_n$. Then $(T - \alpha_1 I)(T - \alpha_2 I) \cdots (T - \alpha_n I) = 0$ as an operator (proved by checking on each basis vector $v_k$: the operator $T - \alpha_j I$ kills $v_j$ and maps $\operatorname{span}(v_1, \ldots, v_{j-1})$ into itself), so $m_T$ divides $\prod_j (z - \alpha_j)$, hence $m_T$ factors into linear factors $(z - \lambda_j)$ over $F$.

---

# Cross-Field Exercise Suggestions

**Schur decomposition (numerical linear algebra).** The Schur theorem is the inner-product-space refinement: every complex matrix is unitarily similar to an upper-triangular matrix. The proof is the upper-triangularisation construction with an additional Gram-Schmidt orthogonalisation at each step. The Schur form is the basis of the **QR algorithm** for numerical eigenvalue computation.

**Lie's theorem (Lie algebra theory).** A solvable Lie subalgebra of $\mathfrak{gl}(V)$ over $\mathbb{C}$ admits a basis with respect to which all elements are simultaneously upper triangular. This is the **simultaneous upper-triangularisation** of a family of operators, generalising the single-operator theorem.

**Gauss elimination produces upper-triangular form (linear systems).** The reduction of a matrix to row echelon form by Gauss elimination is computationally the same construction as upper-triangularisation (when the operator is interpreted in the right way) — the matrix becomes upper triangular through a sequence of row operations.

---

# Bridges

- **[[Thm - Existence of Eigenvalues on Complex Vector Spaces|Existence of Eigenvalues on ℂ]]** — the base step of the induction. Each iteration of the induction invokes the existence theorem on a quotient space.

- **[[Thm - Conditions for Diagonalizability|Conditions for Diagonalizability]]** — the stronger sibling. Diagonalisation is to upper-triangularisation as "$m_T$ has distinct linear factors" is to "$m_T$ has linear factors (possibly repeated)". Every diagonalisable operator is upper-triangularisable; the converse fails.

- **[[Thm - Generalized Eigenspace Decomposition|Generalized Eigenspace Decomposition]]** — the next refinement. Over $\mathbb{C}$, the upper-triangular form can be sharpened to a block-diagonal form with one block per eigenvalue, each block having a single eigenvalue on its diagonal — the generalised eigenspace decomposition.

- **[[Thm - Jordan Normal Form|Jordan Normal Form]]** — the canonical refinement. Within each generalised eigenspace block, the Jordan form gives a further refined upper-triangular structure with $\lambda$'s on the diagonal and $0$'s or $1$'s on the superdiagonal. The Jordan form is the unique-up-to-block-ordering canonical form for operators over $\mathbb{C}$.

- **Schur Decomposition** — the unitary refinement (Linear Algebra VII). For operators on a complex inner product space, the basis can be chosen orthonormal, giving a unitarily upper-triangular form.

---

# Unlocked by This

> [!tip] Generalized Eigenspace Decomposition *(from Linear Algebra VIII)*
> Within each generalised eigenspace $G(\lambda, T)$, the operator $T - \lambda I$ is nilpotent, and upper-triangularisation refines to a block-diagonal form. The full decomposition is $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$. See [[Thm - Generalized Eigenspace Decomposition]].

> [!tip] Jordan Normal Form *(from Modules II — §3.4)*
> The canonical refinement of upper-triangular form: every operator on a complex vector space has a unique Jordan form (up to block ordering), consisting of Jordan blocks $J_k(\lambda)$ — upper-triangular matrices with $\lambda$ on the diagonal, $1$'s on the superdiagonal. See [[Thm - Jordan Normal Form]].

> [!tip] Schur Decomposition *(from Linear Algebra VII / Numerical Linear Algebra)*
> The unitary refinement: any complex matrix $A = U^* T U$ with $U$ unitary and $T$ upper triangular. This is the basis of the QR algorithm for numerical eigenvalue computation, the workhorse of numerical linear algebra.

> [!tip] Lie's Theorem *(from Lie Algebra Theory)*
> A solvable Lie algebra of operators on a complex vector space can be **simultaneously upper-triangularised** — there is a basis in which every operator in the algebra has upper-triangular form. The proof generalises the single-operator argument by exploiting commutation relations.
