---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Bilinear Form"
  - "Def - Symmetric and Alternating Bilinear Form"
  - "Def - Quadratic Form"
  - "Thm - Diagonalization of a Symmetric Bilinear Form"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over $\mathbb{R}$ of dimension $n$, and $\rho$ is a [[Def - Symmetric and Alternating Bilinear Form|symmetric bilinear form]] on $V$. We assume $\rho$ is fixed and study its behaviour in different bases. The matrix of $\rho$ in a basis $(e_1, \dots, e_n)$ is $\mathcal{M}(\rho, (e_1, \dots, e_n))$ with entries $\rho(e_i, e_j)$. See [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] for the full notation registry.

---

# Statement

> **Theorem (Sylvester's Law of Inertia).** Let $V$ be a finite-dimensional real vector space and $\rho$ a symmetric bilinear form on $V$. If $(e_1, \dots, e_n)$ and $(e_1', \dots, e_n')$ are two bases of $V$ in each of which the matrix of $\rho$ is diagonal — say with diagonal entries $(\lambda_1, \dots, \lambda_n)$ and $(\lambda_1', \dots, \lambda_n')$ respectively — then the number of *positive* diagonal entries, the number of *negative* diagonal entries, and the number of *zero* diagonal entries are the same:
>
> $$\#\{i : \lambda_i > 0\} \;=\; \#\{i : \lambda_i' > 0\}, \quad \#\{i : \lambda_i < 0\} \;=\; \#\{i : \lambda_i' < 0\}, \quad \#\{i : \lambda_i = 0\} \;=\; \#\{i : \lambda_i' = 0\}.$$
>
> The triple $(p, q, r) := (\#\text{positive}, \#\text{negative}, \#\text{zero})$ is called the **signature** of $\rho$. It is an intrinsic invariant of $\rho$, depending only on $\rho$ and not on any choice of diagonalising basis.

> **Companion form (the symmetric-matrix version).** Two real symmetric matrices $A$ and $B$ are **congruent** (i.e., $B = C^t A C$ for some invertible $C$) if and only if they have the same signature.

The diagonalisation theorem ([[Thm - Diagonalization of a Symmetric Bilinear Form]]) guarantees that *some* diagonalising basis exists; Sylvester's law says that the signature pattern $(p, q, r)$ extracted from any diagonalising basis is the same.

---

# Motivation

Sylvester's law answers the question: **what is invariant about the diagonal form of a symmetric bilinear form?** The diagonalisation theorem gives us a basis in which $\rho$ has matrix $\operatorname{diag}(\lambda_1, \dots, \lambda_n)$, but the diagonal entries themselves are *not* invariants — scaling a basis vector $e_i$ by $\mu$ scales the corresponding diagonal entry $\lambda_i$ by $\mu^2$, which changes its magnitude but not its sign. So magnitudes are not basis-independent, but signs *are* (because $\mu^2 \geq 0$ for real $\mu$), and what Sylvester's law makes precise is that the *count* of positive, negative, and zero diagonal entries is intrinsic to $\rho$.

This is the theorem that makes "signature $(1, 3)$" a coordinate-free statement. Without Sylvester's law, declaring that the Minkowski metric has signature $(1, 3)$ would be a statement about a choice of coordinates, and could be undermined by changing coordinates. With Sylvester's law, the signature is a property of the metric itself, and the distinction between timelike, spacelike, and null directions is intrinsic geometry. Similarly, the statement that a Riemannian metric is "positive definite" — signature $(n, 0)$ — is a basis-free statement about the metric. The same theorem underlies the second-derivative test in multivariate calculus, where the signature of the Hessian classifies critical points (signature $(n, 0)$: minimum; $(0, n)$: maximum; otherwise: saddle), and the classification of conic sections (the eccentricity of a conic is determined by the signature of the associated quadratic form). Sylvester's law is the structural fact that makes all these "signature classifications" meaningful.

The historical name "law of inertia" comes from a beautiful 19th-century intuition: the signature is "inert" in the sense that no change of basis (no "perturbation" of viewpoint) can shift it. Sylvester himself proved the theorem in 1852.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is mild — a symmetric bilinear form on a finite-dimensional real vector space — so the "source" question is: when does a problem secretly hand you a symmetric bilinear form, even if none is named?

The first disguised source is **a symmetric matrix**. Every symmetric matrix $A \in M_n(\mathbb{R})$ defines a symmetric bilinear form $\rho_A(u, v) := u^t A v$ on $\mathbb{R}^n$, and conversely every symmetric bilinear form on $\mathbb{F}^n$ arises this way for a unique symmetric matrix. So *every* symmetric matrix problem is implicitly a Sylvester problem. The bridge $B \to A$ is the canonical $A \mapsto \rho_A$; the example problem is "show that two real symmetric matrices are congruent iff they have the same number of positive and negative eigenvalues" — Sylvester's law makes this a corollary of "congruence preserves signature".

The second disguised source is **a quadratic form on a real vector space**. Every [[Def - Quadratic Form|quadratic form]] $q : V \to \mathbb{R}$ has a unique symmetric bilinear form $\rho_q$ realising it (in characteristic $\neq 2$), so the signature of $q$ is by definition the signature of $\rho_q$. Quadratic forms arise in physics (kinetic energy, potential energy, proper time), differential geometry (the second fundamental form of a hypersurface), and optimisation (the Hessian at a critical point). All these contexts feed into Sylvester via $q \to \rho_q$. The example problem: "classify the critical points of $f(x, y, z) = x^2 + 2xy - y^2 + z^2 + xz$ at the origin" — compute the Hessian, polarise to the symmetric matrix, diagonalise, read the signature.

The third disguised source is **a Hermitian form (over $\mathbb{C}$)**. Hermitian forms on complex vector spaces also admit diagonalisation with real diagonal entries, and Sylvester's law holds *verbatim* for the signature of a Hermitian form. The bridge from "Hermitian form" to "symmetric bilinear form" goes via the real subspace structure: a Hermitian form on $V$ over $\mathbb{C}$ becomes a symmetric bilinear form on the underlying real space $V_\mathbb{R}$ of double the dimension, but the signature multiplies by 2 in a predictable way. Hermitian forms appear in quantum mechanics (observables), complex geometry (Kähler metrics), and number theory (quadratic forms over rings).

The fourth disguised source is **a self-adjoint operator on a real inner product space**. Given a self-adjoint $T$, the bilinear form $\rho_T(u, v) := \langle u, Tv\rangle$ is symmetric (because $T$ is self-adjoint), so Sylvester applies. The signature of $\rho_T$ equals (#positive eigenvalues of $T$, #negative eigenvalues, #zero eigenvalues) by the spectral theorem. Conversely, given any symmetric $\rho$ on an inner product space, the operator $T_\rho$ defined by $\langle u, T_\rho v\rangle = \rho(u, v)$ is self-adjoint. So self-adjoint operators and symmetric bilinear forms are interchangeable inputs, and Sylvester translates between them.

**Targets (Output Amplification)**

The bare conclusion is that the signature is basis-independent. Combined with other facts it does much more.

**Combine with congruence-invariance to classify symmetric matrices.** Two real symmetric matrices are *congruent* iff they have the same signature. So Sylvester's law gives a *complete* classification of real symmetric matrices up to congruence: just count positive, negative, and zero eigenvalues. The further result is that the moduli space of $n \times n$ real symmetric matrices up to congruence is finite — there are $\binom{n+2}{2}$ congruence classes, one for each triple $(p, q, r)$ with $p + q + r = n$. This is one of the cleanest classification theorems in linear algebra.

**Combine with positive-definiteness criteria to detect positive definite forms.** A symmetric bilinear form is **positive definite** iff its signature is $(n, 0, 0)$. By Sylvester's law, this is a well-defined notion: positive-definiteness is intrinsic. Combined with the spectral theorem, the form is positive definite iff all its eigenvalues (as a self-adjoint operator on an inner product space) are positive. Combined with the **Sylvester criterion**, positive definiteness is equivalent to all leading principal minors of the matrix being positive — a determinantal criterion that avoids eigenvalue computation.

**Combine with completeness of $\mathbb{R}$ to define topological invariants.** The signature of a manifold (or more generally, of a 4k-dimensional oriented manifold) is a topological invariant defined via the intersection form on middle-dimensional cohomology. The intersection form is symmetric for manifolds of dimension $4k$, and Sylvester's law gives its signature as an integer invariant. This integer is a key tool in the classification of 4-manifolds (Donaldson's theorem, Freedman's theorem, the Hirzebruch signature theorem).

---

# Why Is It True

The proof is a beautiful dimension-counting argument. Given two diagonalisations with signature triples $(p, q, r)$ and $(p', q', r')$ — meaning two bases $(e_1, \dots, e_n)$ and $(e_1', \dots, e_n')$ in which $\rho$ has diagonal matrices with diagonal entries of the given signs — we want to show $p = p'$, $q = q'$, $r = r'$.

Consider the subspaces

$$P := \operatorname{span}(e_1, \dots, e_p) \quad \text{(positive subspace from the first basis)},$$

$$N' := \operatorname{span}(e_{p'+1}', \dots, e_{p'+q'}') \quad \text{(negative subspace from the second basis)}.$$

In $P$, the form $\rho$ is **strictly positive** on nonzero vectors: $\rho(v, v) = \sum_{i \leq p} \lambda_i x_i^2 > 0$ for $v = \sum x_i e_i \neq 0$ (since $\lambda_i > 0$ for $i \leq p$). In $N'$, the form $\rho$ is **strictly negative** on nonzero vectors. So $P \cap N' = \{0\}$ — any nonzero vector in the intersection would be both $\rho$-positive and $\rho$-negative, a contradiction.

By the standard dimension formula, $\dim(P + N') = \dim P + \dim N' = p + q'$, and this must be $\leq n$. So $p + q' \leq n$. By symmetry (swap roles of the two diagonalisations), $p' + q \leq n$. We need to extract $p = p'$ from these inequalities, which requires a slightly more careful argument involving the **null subspace** $\{v : \rho(v, \cdot) = 0\}$, but the key idea is the disjointness of positive and negative subspaces.

A cleaner formulation: the **maximum dimension of a $\rho$-positive subspace** (a subspace on which $\rho$ is positive definite) is the invariant $p$. This is basis-independent because it is a property of the form $\rho$, not of any diagonalisation. The argument that the diagonal-positive count in any diagonalisation equals this maximum is what does the work.

**The mechanism summary:**

> **A $\rho$-positive subspace of dimension $p$ and a $\rho$-non-positive subspace of dimension $q + r$ can only intersect in $\{0\}$, forcing $p + q + r \leq n$ on the one hand, and combined with $p + q + r = n$ on the other, $p$ is determined as the largest such positive subspace.**

The positive subspace and the negative-or-null subspace cannot share any nonzero vector, so they fit disjointly inside $V$, and their dimensions sum to at most $n$. Conversely, the diagonalisation provides explicit subspaces of these dimensions, so the inequalities are equalities. This dimension-counting is the entire content of the theorem.

---

# What Makes This Hard

The trap is in seeing why $p$ is invariantly defined as "the maximum dimension of a subspace on which $\rho$ is positive definite" — and recognising that *this* characterisation is what makes the count basis-free. Beginners often try to argue directly that "the diagonal entries are similar to the eigenvalues, and eigenvalues are invariants" — but this is *wrong* without an inner product: the diagonal entries in a diagonalising basis are *not* the eigenvalues of any natural operator, because changing basis by $C$ changes them to $C^t A C$, not $C^{-1} A C$. The cleanest fix is to realise that Sylvester's law is about **congruence**, not similarity, and to characterise the signature *intrinsically* (via maximum positive subspaces) rather than via matrix entries.

A second common pitfall: assuming Sylvester's law extends to non-real fields. Over $\mathbb{C}$, every non-degenerate symmetric bilinear form is congruent to the identity (one can always extract a square root, so the diagonal entries can be normalised to all $+1$); the "signature" notion collapses. Over $\mathbb{Q}$ or $\mathbb{Z}$, the classification is finer and involves the **Hasse–Minkowski theorem** and the $p$-adic structure of the form. Sylvester's law is specifically a real phenomenon.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**

Set up the two diagonal forms and identify subspaces on which $\rho$ has a fixed sign behaviour. Argue that these subspaces are disjoint (intersect only in $\{0\}$). The disjointness, combined with their dimensions summing to at most $n$, forces the counts to match.

**Subgoal decomposition:**

1. **Set up subspaces with definite sign behaviour.** Given two diagonalisations, let $P, N, Z$ be the spans of basis vectors with positive, negative, zero diagonal entries in the first basis; $P', N', Z'$ in the second.
   - *Hint:* $\rho$ is positive definite on $P$ (sum of positive scalars times squares), negative definite on $N$, and zero on $Z$ — and similarly for the primed versions.
   - *Why needed:* The subspaces translate the "diagonal-entry sign count" into intrinsic geometric data about $\rho$.

2. **Show $P \cap (N' \oplus Z') = \{0\}$.** A nonzero vector in this intersection would be $\rho$-positive (in $P$) and $\rho$-non-positive (in $N' \oplus Z'$), a contradiction.
   - *Hint:* The positive subspace and the negative-or-zero subspace are disjoint as subsets of $V$.
   - *Why needed:* This is the key dimension constraint.

3. **Apply the dimension formula.** $\dim P + \dim(N' \oplus Z') = \dim(P + N' \oplus Z') \leq n$, so $p + (q' + r') \leq n$.
   - *Hint:* Direct sums add dimensions; disjoint subspaces stay $\leq$ ambient dimension.
   - *Why needed:* Converts the disjointness into a numerical inequality.

4. **Swap the roles of the two diagonalisations.** By symmetry, $p' + (q + r) \leq n$.

5. **Combine with $p + q + r = p' + q' + r' = n$.** From $p + q' + r' \leq n = p + q + r$, we get $q' + r' \leq q + r$. From $p' + q + r \leq n = p' + q' + r'$, we get $q + r \leq q' + r'$. So $q + r = q' + r'$. By a symmetric argument with $N$ replacing $P$, $p + r = p' + r'$. And combining, $p = p'$, $q = q'$, $r = r'$.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\rho$ is positive definite on $P = \operatorname{span}(e_1, \dots, e_p)$
> **Statement:** If $\lambda_1, \dots, \lambda_p > 0$ are the positive diagonal entries of $\rho$ in the basis $(e_1, \dots, e_n)$, then for any nonzero $v \in P$ (the span of $e_1, \dots, e_p$), $\rho(v, v) > 0$.
>
> **Hint:** Expand $v = \sum_{i \leq p} x_i e_i$, compute $\rho(v, v) = \sum \lambda_i x_i^2$, and use that all $\lambda_i > 0$ and at least one $x_i \neq 0$.
>
> **Why needed:** This gives us a $p$-dimensional subspace on which $\rho$ is strictly positive, which we will combine with the negative subspace from the second diagonalisation.
>
> > [!note]- Full proof
> > Let $v \in P$ be nonzero, so $v = \sum_{i \leq p} x_i e_i$ with at least one $x_i \neq 0$. Then by bilinearity and the diagonal form of $\rho$,
> > $$\rho(v, v) = \sum_{i, j \leq p} x_i x_j \rho(e_i, e_j) = \sum_{i \leq p} x_i^2 \rho(e_i, e_i) = \sum_{i \leq p} \lambda_i x_i^2.$$
> > Since $\lambda_i > 0$ for all $i \leq p$ and $x_i^2 \geq 0$ for all $i$ with at least one strictly positive (because some $x_i \neq 0$ means $x_i^2 > 0$), the sum is strictly positive. Hence $\rho(v, v) > 0$ for $v \in P \setminus \{0\}$.

> [!note]- Lemma 2: $\rho$ is non-positive on $N \oplus Z$
> **Statement:** Let $N = \operatorname{span}(e_{p+1}, \dots, e_{p+q})$ and $Z = \operatorname{span}(e_{p+q+1}, \dots, e_n)$ be the spans of basis vectors with negative and zero diagonal entries. Then for any $v \in N \oplus Z$, $\rho(v, v) \leq 0$.
>
> **Hint:** Expand $v$ as a sum over indices $i > p$ and observe that all diagonal entries $\lambda_i$ for $i > p$ are $\leq 0$.
>
> **Why needed:** Provides the "negative-or-zero" companion subspace to combine with the positive subspace via disjointness.
>
> > [!note]- Full proof
> > Let $v \in N \oplus Z$, so $v = \sum_{i > p} x_i e_i$. By the diagonal structure, $\rho(v, v) = \sum_{i > p} \lambda_i x_i^2$. For $i \in \{p+1, \dots, p+q\}$, $\lambda_i < 0$, so $\lambda_i x_i^2 \leq 0$. For $i \in \{p+q+1, \dots, n\}$, $\lambda_i = 0$, so $\lambda_i x_i^2 = 0$. Summing, $\rho(v, v) \leq 0$.

> [!note]- Lemma 3: Disjointness of $P$ and $N' \oplus Z'$
> **Statement:** Let $P$ be the $p$-dimensional $\rho$-positive subspace from the first diagonalisation, and $N' \oplus Z'$ be the $(q' + r')$-dimensional $\rho$-non-positive subspace from the second diagonalisation. Then $P \cap (N' \oplus Z') = \{0\}$.
>
> **Hint:** Suppose $v$ is nonzero in the intersection. From Lemma 1 (applied to the first basis), $\rho(v, v) > 0$. From Lemma 2 (applied to the second basis), $\rho(v, v) \leq 0$. Contradiction.
>
> **Why needed:** Disjointness combined with the dimension formula will force the inequalities that prove signature invariance.
>
> > [!note]- Full proof
> > Suppose $v \in P \cap (N' \oplus Z')$ is nonzero. Since $v \in P$, Lemma 1 gives $\rho(v, v) > 0$. Since $v \in N' \oplus Z'$, Lemma 2 (applied to the second diagonalising basis) gives $\rho(v, v) \leq 0$. These contradict, so no such $v$ exists, i.e., $P \cap (N' \oplus Z') = \{0\}$.

> [!note]- Lemma 4: Dimension counting forces $p \leq p'$
> **Statement:** With the setup of Lemma 3, $p + q' + r' \leq n$, hence $p \leq p'$.
>
> **Hint:** The disjointness $P \cap (N' \oplus Z') = \{0\}$ and the dimension formula give $\dim(P + N' \oplus Z') = p + (q' + r')$, and this is $\leq n = \dim V$.
>
> **Why needed:** Together with the symmetric argument $p' \leq p$, this gives $p = p'$.
>
> > [!note]- Full proof
> > By Lemma 3, $P \cap (N' \oplus Z') = \{0\}$, so the sum is direct: $P + (N' \oplus Z') = P \oplus N' \oplus Z'$ (subspace of $V$). Hence
> > $$\dim(P \oplus N' \oplus Z') = p + q' + r' \leq \dim V = n.$$
> > Since $p' + q' + r' = n$ (the second diagonalisation has signature summing to $n$), we get $p + q' + r' \leq p' + q' + r'$, i.e., $p \leq p'$. By the symmetric argument exchanging the two diagonalisations, $p' \leq p$. Hence $p = p'$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $(e_1, \dots, e_n)$ and $(e_1', \dots, e_n')$ be two bases of $V$ in each of which the symmetric bilinear form $\rho$ has diagonal matrix. Suppose the diagonal entries in the first basis are $\lambda_1, \dots, \lambda_n$ with $p$ positive entries (say $\lambda_1, \dots, \lambda_p > 0$), $q$ negative entries ($\lambda_{p+1}, \dots, \lambda_{p+q} < 0$), and $r = n - p - q$ zero entries. Similarly the second basis has signature $(p', q', r')$.
>
> **Step 0 — Setup.** Define subspaces from the first basis:
> $$P := \operatorname{span}(e_1, \dots, e_p), \quad N := \operatorname{span}(e_{p+1}, \dots, e_{p+q}), \quad Z := \operatorname{span}(e_{p+q+1}, \dots, e_n),$$
> with $\dim P = p$, $\dim N = q$, $\dim Z = r$, and $V = P \oplus N \oplus Z$. Similarly $P', N', Z'$ from the second basis. By Lemma 1, $\rho$ is positive definite on $P$; by Lemma 2, $\rho$ is non-positive on $N \oplus Z$. The primed analogues hold for the second basis.
>
> **Step 1 — Disjointness.** By Lemma 3, $P \cap (N' \oplus Z') = \{0\}$, because a nonzero vector in the intersection would be both $\rho$-positive (by membership in $P$) and $\rho$-non-positive (by membership in $N' \oplus Z'$), a contradiction.
>
> **Step 2 — Dimension count gives $p \leq p'$.** By Lemma 4, the disjointness $P \cap (N' \oplus Z') = \{0\}$ implies $p + q' + r' \leq n$. Combined with $p' + q' + r' = n$, this gives $p \leq p'$.
>
> **Step 3 — Symmetric argument gives $p' \leq p$.** Swap the roles of the two bases (consider $P' \cap (N \oplus Z)$). The same argument gives $p' \leq p$.
>
> **Step 4 — $p = p'$.** Combining Steps 2 and 3, $p = p'$.
>
> **Step 5 — Similar argument for $q$ and $r$.** Replace $P$ by $N$ (the $\rho$-negative subspace) and run the same argument with the roles of positive/negative swapped: $q = q'$. Then $r = n - p - q = n - p' - q' = r'$.
>
> Combining, $(p, q, r) = (p', q', r')$. The signature is basis-independent. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Hessian classification of critical points.** Given a smooth function $f : \mathbb{R}^n \to \mathbb{R}$ with $\nabla f(x_0) = 0$, the Hessian $H = (\partial_i \partial_j f)(x_0)$ is a symmetric matrix, giving a symmetric bilinear form on $\mathbb{R}^n$. By Sylvester's law, its signature $(p, q, r)$ is a basis-free invariant of the critical point, and classifies it: $(n, 0, 0)$ is a local minimum, $(0, n, 0)$ a local maximum, otherwise either a saddle or degenerate. This is the foundation of Morse theory and the classical second-derivative test. The nonobviousness: the *eigenvalues* of $H$ depend on the choice of inner product on $\mathbb{R}^n$ (you can scale coordinates and change them), but the *signature* doesn't — only the signature is the "intrinsic" classification.

**Topological signature of a 4k-manifold.** For a closed oriented manifold $M^{4k}$, the cup product on the middle cohomology $H^{2k}(M; \mathbb{R})$ is a symmetric bilinear form. Its signature is the **signature of the manifold**, a topological invariant. By the Hirzebruch signature theorem, this signature equals an integral of certain characteristic classes — connecting global topology to local geometry. The nonobviousness: the bilinear form is defined on a cohomology space, with no obvious metric structure, yet Sylvester's law makes its signature well-defined.

**Classification of real semisimple Lie algebras.** The **Killing form** $K(X, Y) = \operatorname{tr}(\operatorname{ad}_X \operatorname{ad}_Y)$ on a real semisimple Lie algebra is symmetric and bilinear. The Cartan-Killing classification uses the signature of the Killing form to organise the real forms of complex Lie algebras: a Lie algebra is **compact** iff its Killing form is negative definite (signature $(0, n, 0)$), **split** iff its signature contains both positive and negative entries in a maximal symmetric way. So Sylvester's law is foundational for the classification of real Lie groups and their representations.

**Indefinite quadratic forms in number theory.** Over $\mathbb{Q}$, the classification of quadratic forms involves the signature (Sylvester's input) combined with $p$-adic invariants (Hasse-Minkowski theorem). This is one of the cornerstones of arithmetic geometry. The nonobviousness: Sylvester's law is the "archimedean part" of a much deeper number-theoretic classification.

**Pseudo-Riemannian geometry beyond Minkowski.** Sylvester's law makes the signature of a non-degenerate symmetric bilinear form on a tangent space a basis-free invariant. This is what allows the classification of pseudo-Riemannian metrics by signature: Riemannian $(n, 0)$, Lorentzian $(1, n-1)$, ultra-hyperbolic $(p, q)$ with $p, q \geq 2$. Each signature gives a different geometry with its own physics — for instance, Riemannian signature gives elliptic equations, Lorentzian gives hyperbolic equations (wave propagation), and ultra-hyperbolic gives mixed-type equations rare in physics but appearing in twistor theory.

---

# Bridges

- **[[Thm - Diagonalization of a Symmetric Bilinear Form|Diagonalisation of a symmetric bilinear form]]** — Sylvester's law builds directly on diagonalisation. Diagonalisation says "a diagonalising basis exists"; Sylvester says "the signature pattern from any such basis is the same". The pair gives a complete classification of symmetric bilinear forms up to congruence: every form is congruent to a normalised diagonal form with signs $\pm 1$ and $0$, and the multiplicity of each sign is the invariant.

- **[[Thm - Real Spectral Theorem|Real spectral theorem]]** — when $V$ is an inner product space and $T$ is the self-adjoint operator with $\rho(u, v) = \langle u, Tv\rangle$, the spectral theorem diagonalises $T$ in an orthonormal basis with diagonal entries equal to the eigenvalues of $T$. So in the inner product setting, Sylvester's signature equals (#positive eigenvalues of $T$, #negative, #zero). This is the "spectral interpretation" of the signature: it counts eigenvalues by sign. Without the inner product, eigenvalues do not make invariant sense for a symmetric bilinear form, but Sylvester's signature still does.

- **[[Def - Minkowski Space and the Metric|Minkowski metric and special relativity]]** — the Minkowski metric on $\mathbb{R}^4$ is a non-degenerate symmetric bilinear form of signature $(1, 3)$ (or $(3, 1)$, depending on convention). Sylvester's law is what makes "this metric has one timelike and three spacelike directions" a coordinate-free statement. Without Sylvester's law, the distinction between timelike and spacelike would depend on coordinates, and special relativity's covariance would be undermined. The [[Def - The Lorentz Group|Lorentz group]] is then the isometry group of this signature-$(1, 3)$ form, and its abstract structure is determined by the signature.

- **The Sylvester criterion for positive definiteness** — a real symmetric matrix is positive definite iff all leading principal minors are positive. This is a *determinantal* test for positive-definiteness, providing a different proof of the result that does not require eigenvalues. Combined with Sylvester's law of inertia, it gives a complete computational toolkit for testing signature.

- **Hasse-Minkowski theorem** — the local-global principle for quadratic forms over $\mathbb{Q}$. Sylvester's law gives the *archimedean* (real-valued) classification; Hasse-Minkowski adds the $p$-adic classifications, and the theorem says two rational quadratic forms are equivalent iff they are equivalent over each local field (each $\mathbb{Q}_p$ and over $\mathbb{R}$). This is one of the foundational results of number theory, with Sylvester's law as the real-place ingredient.

---

# Unlocked by This

> [!tip] Pseudo-Riemannian Geometry *(from Differential Geometry)*
> A **pseudo-Riemannian metric** on a manifold is a smoothly varying family of non-degenerate symmetric bilinear forms on tangent spaces, with constant signature. Sylvester's law applied pointwise makes the signature globally well-defined. Riemannian metrics have signature $(n, 0)$; Lorentzian metrics (the setting of general relativity) have signature $(1, n-1)$. The signature determines the type of PDE governing geodesics and curvature equations.

> [!tip] Morse Theory *(from Differential Topology)*
> A **non-degenerate critical point** of a smooth function $f : M \to \mathbb{R}$ on a manifold is one where the Hessian has empty null space. The Morse index of the critical point is the number of negative eigenvalues of the Hessian — a Sylvester invariant. Morse theory studies how the topology of $M$ relates to the configuration of critical points classified by their indices.

> [!tip] Signature Theorem (Hirzebruch) *(from Algebraic Topology)*
> For a closed oriented 4k-dimensional manifold $M$, the signature of $M$ (defined via the cup product on $H^{2k}(M)$) equals the integral of the **L-polynomial** in the Pontryagin classes of $M$. This is one of the great theorems linking topology to characteristic classes, and Sylvester's law is what makes "the signature" a meaningful integer invariant of $M$.

> [!tip] Witt's Theorem and Cancellation *(from Quadratic-Form Theory)*
> Witt's theorem says that any isometry between subspaces of a quadratic space extends to an isometry of the whole space. Combined with Sylvester's law, this gives the *cancellation property*: if $V \oplus W \cong V' \oplus W$ as quadratic spaces, then $V \cong V'$. This makes the Grothendieck group of quadratic spaces a useful invariant.
