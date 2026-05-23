---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Symmetric and Alternating Bilinear Form"
  - "Def - Basis"
  - "Def - Dimension"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over a field $\mathbb{F}$ of characteristic $\neq 2$ (which includes $\mathbb{R}$ and $\mathbb{C}$), and $\rho$ is a [[Def - Symmetric and Alternating Bilinear Form|symmetric bilinear form]] on $V$. The matrix of $\rho$ in a basis $(e_1, \dots, e_n)$ is $\mathcal{M}(\rho, (e_1, \dots, e_n))$ with entries $A_{ij} = \rho(e_i, e_j)$.

---

# Statement

> **Theorem (Diagonalization of a Symmetric [[Def - Bilinear Form|Bilinear Form]], LADR 9.12).** Let $\rho$ be a symmetric bilinear form on a finite-dimensional vector space $V$ over a field of characteristic $\neq 2$. Then there exists a basis $(e_1, \dots, e_n)$ of $V$ in which the matrix of $\rho$ is **diagonal**:
>
> $$\mathcal{M}(\rho, (e_1, \dots, e_n)) = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$$
>
> for some $\lambda_1, \dots, \lambda_n \in \mathbb{F}$.

> **Companion form (the inner-product version, LADR 9.13).** When $\mathbb{F} = \mathbb{R}$ and $V$ is a real inner product space, the basis can be chosen to be an **orthonormal** basis of $V$. In this orthonormal basis, $\lambda_1, \dots, \lambda_n$ are the eigenvalues of the self-adjoint operator $T$ with $\rho(u, v) = \langle u, Tv\rangle$.

The companion form follows immediately from the [[Thm - Real Spectral Theorem|real spectral theorem]] applied to the operator $T$.

---

# Motivation

This theorem is the structural foundation underlying [[Thm - Sylvester's Law of Inertia|Sylvester's law of inertia]]. Sylvester's law says "the signature of the diagonal form is intrinsic"; this theorem says "the diagonal form *exists*". Without this theorem, Sylvester would be vacuous.

The conceptual content: every symmetric bilinear form admits a basis in which it looks like a weighted sum of squares, $\rho(\sum x_i e_i, \sum y_j e_j) = \sum \lambda_i x_i y_i$. The diagonal entries $\lambda_i$ are not invariants (they depend on basis), but their *signs* are (Sylvester). The route to this canonical form is by induction on [[Def - Dimension|dimension]]: find one vector $v$ where $\rho(v, v) \neq 0$, take the $\rho$-orthogonal complement of $v$, and recurse.

The companion-form inner-product version is the more familiar statement: every real symmetric matrix has an orthonormal eigenbasis with real eigenvalues. This is the spectral theorem dressed as a bilinear-form statement. The non-inner-product version is *strictly more general* — it works over any field of characteristic $\neq 2$, including $\mathbb{C}$ and even finite fields, but the resulting basis is not orthonormal because there is no metric structure to be orthonormal *to*. In return, the diagonal entries are merely "diagonal entries" and not "eigenvalues in any intrinsic sense" — only their *signs* (over $\mathbb{R}$) are intrinsic.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem requires a symmetric bilinear form on a finite-dimensional space. Disguised sources:

**A symmetric matrix.** Every symmetric $n \times n$ matrix $A$ defines a symmetric bilinear form $\rho_A(u, v) = u^t A v$, so every symmetric matrix problem is implicitly a diagonalisation problem in this sense. The bridge: $A \to \rho_A$ via the matrix-as-bilinear-form correspondence. Example problem: find a basis in which the form with matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1\end{pmatrix}$ is diagonal — by the theorem, such a basis exists.

**A quadratic form.** Every [[Def - Quadratic Form|quadratic form]] $q$ has a unique symmetric bilinear form $\rho_q$ realising it. Diagonalising $\rho_q$ gives a basis in which $q$ is a sum of squares of coordinates: $q(\sum x_i e_i) = \sum \lambda_i x_i^2$. Example problem: complete the square on $q(x, y) = x^2 + 4xy + y^2$ to find its signature. This is exactly the classical "completion of squares" algorithm, which diagonalises symmetric bilinear forms in low dimension.

**A symmetric operator on an inner product space.** When $V$ has an inner product, the operator $T_\rho$ with $\rho(u, v) = \langle u, T_\rho v\rangle$ is self-adjoint, and the real spectral theorem gives an orthonormal eigenbasis. The diagonal entries in this basis are the eigenvalues of $T_\rho$. Example problem: diagonalise the "energy form" of a coupled-oscillator system, which is symmetric in the kinetic energy and potential energy contributions.

**A Riemannian or pseudo-Riemannian metric on a tangent space.** At any single point of a manifold, the metric is a symmetric bilinear form on the tangent space. Diagonalising gives a basis of the tangent space adapted to the metric — the "principal axes" of the metric ellipsoid (Riemannian) or hyperboloid (pseudo-Riemannian).

**Targets (Output Amplification)**

The bare conclusion is "a diagonalising basis exists". Combined with other facts:

**Combine with the symmetry of the diagonal form to invoke Sylvester.** Once we have a diagonal form, [[Thm - Sylvester's Law of Inertia|Sylvester's law of inertia]] says the signature pattern is invariant. So diagonalisation plus Sylvester gives the complete classification of symmetric bilinear forms up to congruence: each form is determined by its dimension and signature. This is a non-obvious payoff — what looked like "merely finding a nice form" turns out to give a *classification theorem*.

**Combine with positive-definiteness criteria.** Once $\rho$ is diagonalised as $\operatorname{diag}(\lambda_1, \dots, \lambda_n)$, it is positive definite iff all $\lambda_i > 0$. So diagonalisation reduces positive-definiteness checking to "all diagonal entries positive in some diagonalisation" — equivalently (by Sylvester) "all diagonal entries positive in *every* diagonalisation".

**Combine with the spectral theorem to characterise spectrum.** In the inner-product version, the diagonal entries are eigenvalues. So diagonalisation of a symmetric bilinear form on an inner product space is the same as spectral decomposition of the associated self-adjoint operator. This bridges symmetric-bilinear-form theory to operator theory.

---

# Why Is It True

The proof is by induction on $\dim V$. The intuition: a symmetric bilinear form is "symmetric" in the sense that it treats its two inputs the same way, so it has the right kind of symmetry to be diagonalised by a clever choice of basis. The induction uses the **$\rho$-orthogonal complement** to peel off one [[Def - Dimension|dimension]] at a time, in much the same way the spectral theorem proof peels off eigenvectors one at a time.

**The mechanism summary:**

> **Find one vector $v$ where $\rho(v, v) \neq 0$ (so $v$ is "$\rho$-non-isotropic"). The $\rho$-orthogonal complement $U = \{u : \rho(u, v) = 0\}$ is a hyperplane; $\rho$ restricted to $U$ is again a symmetric bilinear form, on a smaller space. Inductively diagonalise on $U$ and append $v$ as the last basis vector.**

The base case $n = 1$ is trivial: every $1 \times 1$ matrix is "diagonal". The induction step: given a symmetric bilinear form $\rho$ on $V$ with $\dim V \geq 2$, either $\rho \equiv 0$ (trivially diagonalised by any basis) or there exists $v \in V$ with $\rho(v, v) \neq 0$. The existence of such $v$ is the non-obvious part: $\rho$ being symmetric *might* be zero on the diagonal (an alternating bilinear form has $\rho(v, v) = 0$ for all $v$), but a *symmetric* one in characteristic $\neq 2$ cannot — if $\rho(v, v) = 0$ for all $v$, polarisation gives $\rho \equiv 0$. So a nonzero symmetric $\rho$ has $\rho(v, v) \neq 0$ for some $v$.

Now the linear functional $u \mapsto \rho(u, v)$ is *not* the zero functional (since $v$ itself maps to $\rho(v, v) \neq 0$), so its kernel $U$ has dimension $n - 1$. The vector $v$ is not in $U$, so $V = U \oplus \mathbb{F} v$. By induction, $\rho|_U$ has a diagonal matrix in some basis $(e_1, \dots, e_{n-1})$ of $U$. The basis $(e_1, \dots, e_{n-1}, v)$ of $V$ diagonalises $\rho$: $\rho(e_i, v) = 0$ for $i < n$ (by membership in $U$), $\rho(v, e_i) = 0$ by symmetry, and the upper-left $(n-1) \times (n-1)$ block is diagonal by inductive hypothesis.

---

# What Makes This Hard

The two non-obvious moves are: (i) the existence of $v$ with $\rho(v, v) \neq 0$ for nonzero symmetric $\rho$, which uses the polarisation identity in a subtle way (a *symmetric* bilinear form is determined by its values on the diagonal, so identical-diagonal-zero forces identically-zero); and (ii) the recognition that taking the $\rho$-orthogonal complement of a non-isotropic vector splits $V$ as a *direct sum*, which is a strong condition — for alternating forms this is *not* true (a symplectic vector is always $\rho$-orthogonal to itself), and the difference is exactly what symmetry buys.

A common pitfall: trying to use eigenvalues directly without an inner product. Eigenvalues are intrinsic to operators (similarity invariants), but the matrix of a bilinear form transforms by congruence ($C^t A C$, not $C^{-1} A C$), so eigenvalues are *not* invariants of a symmetric bilinear form. The diagonalisation theorem produces diagonal entries that depend on the basis chosen, and only their signs (Sylvester) are intrinsic. If you reach for eigenvalues, you are implicitly choosing an inner product to convert the form to a self-adjoint operator — at which point you are using the *companion form* of the theorem, the inner-product version, where eigenvalues *do* equal the diagonal entries.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**

Induction on dimension. Find a non-isotropic vector (one with $\rho(v, v) \neq 0$), take its $\rho$-orthogonal complement to split off a one-dimensional piece, recurse on the smaller space.

**Subgoal decomposition:**

1. **Find $v$ with $\rho(v, v) \neq 0$** (provided $\rho \neq 0$).
   - *Hint:* Use the polarisation identity: if $\rho(v, v) = 0$ for all $v$, then $\rho \equiv 0$.
   - *Why needed:* Without a non-isotropic vector, the inductive step has no starting point.

2. **Show $U := \{u : \rho(u, v) = 0\}$ has dimension $n - 1$.**
   - *Hint:* $u \mapsto \rho(u, v)$ is a *nonzero* linear functional (because $v$ itself maps to $\rho(v, v) \neq 0$), so its kernel has codimension 1.
   - *Why needed:* This is the "splitting" of $V$ as $U \oplus \mathbb{F} v$.

3. **Apply the inductive hypothesis to diagonalise $\rho|_U$.**
   - *Hint:* $\rho|_U$ is a symmetric bilinear form on $U$, of dimension $n - 1$.
   - *Why needed:* This gives a diagonal basis $(e_1, \dots, e_{n-1})$ of $U$.

4. **Append $v$ to form a basis of $V$ in which $\rho$ is diagonal.**
   - *Hint:* $\rho(e_i, v) = \rho(v, e_i) = 0$ for $i < n$ by the definition of $U$ and symmetry. The matrix of $\rho$ in $(e_1, \dots, e_{n-1}, v)$ has zeros in the last row and column except at the $(n, n)$ entry $\rho(v, v)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: A nonzero symmetric bilinear form (over $\operatorname{char} \neq 2$) has a non-isotropic vector
> **Statement:** If $\rho$ is a symmetric bilinear form on $V$ with $\rho \neq 0$ and $\operatorname{char}(\mathbb{F}) \neq 2$, then there exists $v \in V$ with $\rho(v, v) \neq 0$.
>
> **Hint:** Use the polarisation identity: $2 \rho(u, w) = \rho(u + w, u + w) - \rho(u, u) - \rho(w, w)$. If the right-hand-side is always 0, then $\rho \equiv 0$.
>
> **Why needed:** Without a non-isotropic vector, the inductive step has no starting point.
>
> > [!note]- Full proof
> > Suppose for contradiction that $\rho(v, v) = 0$ for all $v \in V$. We show $\rho \equiv 0$. For any $u, w \in V$, compute
> > $$\rho(u + w, u + w) = \rho(u, u) + \rho(u, w) + \rho(w, u) + \rho(w, w).$$
> > Using symmetry ($\rho(u, w) = \rho(w, u)$) and the hypothesis $\rho(v, v) = 0$ for all $v$ (applied to $v = u + w, u, w$):
> > $$0 = 0 + \rho(u, w) + \rho(u, w) + 0 = 2 \rho(u, w).$$
> > Since $\operatorname{char}(\mathbb{F}) \neq 2$, we can divide by 2: $\rho(u, w) = 0$ for all $u, w$, so $\rho \equiv 0$ — contradicting our hypothesis. Hence some $v$ has $\rho(v, v) \neq 0$.

> [!note]- Lemma 2: The $\rho$-orthogonal complement of a non-isotropic vector is a hyperplane
> **Statement:** If $v \in V$ has $\rho(v, v) \neq 0$, then $U := \{u \in V : \rho(u, v) = 0\}$ has $\dim U = \dim V - 1$, and $V = U \oplus \mathbb{F} v$.
>
> **Hint:** The map $u \mapsto \rho(u, v)$ is a *nonzero* linear functional (since $v \mapsto \rho(v, v) \neq 0$), so its kernel has codimension 1.
>
> **Why needed:** Gives the codimension-1 [[Def - Subspace|subspace]] on which we can recurse, and the splitting that lets us reassemble.
>
> > [!note]- Full proof
> > Define the linear functional $\varphi : V \to \mathbb{F}$ by $\varphi(u) := \rho(u, v)$. This is linear by linearity of $\rho$ in its first slot. It is *nonzero*, since $\varphi(v) = \rho(v, v) \neq 0$. Hence $\dim \ker \varphi = \dim V - 1$. By definition, $U = \ker \varphi$, so $\dim U = n - 1$.
> >
> > Since $v \notin U$ (because $\varphi(v) \neq 0$), the sum $U + \mathbb{F} v$ has dimension $\dim U + \dim \mathbb{F} v = n$, equal to $\dim V$. Also $U \cap \mathbb{F} v = \{0\}$ (any nonzero $\lambda v \in U$ would have $\varphi(\lambda v) = \lambda \varphi(v) = 0$, but $\lambda \neq 0$ and $\varphi(v) \neq 0$). Hence $V = U \oplus \mathbb{F} v$.

> [!note]- Lemma 3: The restriction of $\rho$ to a [[Def - Subspace|subspace]] is a symmetric bilinear form
> **Statement:** If $U$ is a subspace of $V$ and $\rho$ is a symmetric bilinear form on $V$, then the restriction $\rho|_{U \times U} : U \times U \to \mathbb{F}$ is a symmetric bilinear form on $U$.
>
> **Hint:** Each axiom (bilinearity, symmetry) is inherited from $\rho$ because the restriction just shrinks the domain.
>
> **Why needed:** Allows the inductive hypothesis to apply to $\rho|_U$.
>
> > [!note]- Full proof
> > Linearity of $\rho|_U$ in each slot: for $u_1, u_2, u \in U$ and $a \in \mathbb{F}$, $\rho|_U(a u_1 + u_2, u) = \rho(a u_1 + u_2, u) = a \rho(u_1, u) + \rho(u_2, u) = a \rho|_U(u_1, u) + \rho|_U(u_2, u)$. Symmetric in the second slot likewise. Symmetry: $\rho|_U(u_1, u_2) = \rho(u_1, u_2) = \rho(u_2, u_1) = \rho|_U(u_2, u_1)$. So $\rho|_U$ is a symmetric bilinear form on $U$.

---

# Formal Proof

> [!note]- Complete formal proof
> Proceed by strong induction on $n = \dim V$.
>
> **Base case ($n = 1$).** The matrix of any bilinear form on a one-dimensional space is a $1 \times 1$ matrix, which is trivially diagonal.
>
> **Step 0 — well-posedness preconditions.** The theorem is interesting only when $\rho \neq 0$; if $\rho = 0$, then the matrix of $\rho$ in any basis is the zero matrix, which is diagonal (with all zero diagonal entries). So we may assume $\rho \neq 0$.
>
> **Inductive step ($n \geq 2$, assuming the theorem for $n - 1$).** Let $V$ have dimension $n \geq 2$, and let $\rho \neq 0$ be a symmetric bilinear form on $V$.
>
> **Step 1 — Find $v \in V$ with $\rho(v, v) \neq 0$.** By Lemma 1 (using $\rho \neq 0$ and $\operatorname{char} \neq 2$), such $v$ exists.
>
> **Step 2 — Define $U := \{u \in V : \rho(u, v) = 0\}$.** By Lemma 2, $\dim U = n - 1$ and $V = U \oplus \mathbb{F} v$.
>
> **Step 3 — Restrict $\rho$ to $U$.** By Lemma 3, $\rho|_U$ is a symmetric bilinear form on $U$. Since $\dim U = n - 1$, the inductive hypothesis gives a basis $(e_1, \dots, e_{n-1})$ of $U$ in which $\rho|_U$ has a diagonal matrix $\operatorname{diag}(\lambda_1, \dots, \lambda_{n-1})$.
>
> **Step 4 — Append $v$ to form a basis of $V$.** Set $e_n := v$. Since $V = U \oplus \mathbb{F} v$ and $(e_1, \dots, e_{n-1})$ is a basis of $U$, the tuple $(e_1, \dots, e_{n-1}, e_n)$ is a basis of $V$.
>
> **Step 5 — Compute the matrix of $\rho$ in $(e_1, \dots, e_n)$.** For $i, j < n$, $\rho(e_i, e_j) = \rho|_U(e_i, e_j) = \begin{cases} \lambda_i & i = j \\ 0 & i \neq j \end{cases}$ by the inductive hypothesis. For $i < n, j = n$: $\rho(e_i, e_n) = \rho(e_i, v) = 0$ since $e_i \in U$. By symmetry $\rho(e_n, e_j) = 0$ for $j < n$. For $i = j = n$: $\rho(e_n, e_n) = \rho(v, v) \neq 0$, call this value $\lambda_n$.
>
> So the matrix of $\rho$ in $(e_1, \dots, e_n)$ is
> $$\operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_{n-1}, \lambda_n),$$
> a diagonal matrix as required. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Diagonalising the Hessian at a critical point.** Given $f : \mathbb{R}^n \to \mathbb{R}$ smooth with $\nabla f(x_0) = 0$, the Hessian $H = D^2 f(x_0)$ defines a symmetric bilinear form on $\mathbb{R}^n$. Diagonalising gives **principal-curvature directions** at the critical point, and the diagonal entries are the second derivatives along these directions. This is exactly the setup for the second-derivative test, classifying critical points as min, max, or saddle by the signs of the diagonal entries.

**Diagonalising the metric tensor at a point.** A Riemannian metric on a manifold is a symmetric bilinear form on each tangent space, varying smoothly. At any single point, the metric can be diagonalised; if the metric is positive definite (Riemannian), the diagonalising basis can be chosen orthonormal in the standard sense, giving **orthonormal coordinates** at that point. Geometrically, diagonalisation reveals the principal axes of the metric ellipsoid.

**Diagonalising the inertia tensor of a rigid body.** In classical mechanics, the inertia tensor $I$ of a rigid body is a symmetric $3 \times 3$ matrix (a symmetric bilinear form on the rotation space). Diagonalising $I$ produces the **principal moments of inertia** (the diagonal entries) and the **principal axes** (the basis vectors). A spinning body rotates stably around the principal axes corresponding to the largest and smallest moments, and unstably around the intermediate axis — a classical demonstration whose mathematical foundation is this diagonalisation.

**Diagonalising the strain tensor in continuum mechanics.** The strain tensor $\epsilon_{ij}$ at a point of a deformed elastic body is a symmetric $3 \times 3$ matrix. Diagonalising produces the **principal strains** (eigenvalues) and **principal axes of deformation** (eigenvectors). This decomposition is the foundation of the theory of elasticity and material yielding.

---

# Bridges

- **[[Thm - Sylvester's Law of Inertia|Sylvester's law of inertia]]** — diagonalisation says a diagonal basis exists; Sylvester says the signature pattern is invariant across diagonalising bases. The pair gives a complete classification of symmetric bilinear forms up to congruence. Diagonalisation is necessary for Sylvester to be meaningful.

- **[[Thm - Real Spectral Theorem|Real spectral theorem]]** — the inner-product version of diagonalisation, in which the diagonalising basis is orthonormal and the diagonal entries are the eigenvalues of the associated self-adjoint operator. The real spectral theorem is "diagonalisation plus orthogonality" for the inner-product case.

- **The polarisation identity** — the key technical lemma in the proof: $2\rho(u, w) = \rho(u + w, u + w) - \rho(u, u) - \rho(w, w)$. This lets us deduce $\rho = 0$ from $\rho(v, v) = 0$ for all $v$, which is what gives existence of a non-isotropic vector when $\rho \neq 0$.

- **Sylvester's criterion** — a real symmetric matrix is positive definite iff all leading principal minors are positive. This gives a determinantal alternative to the diagonalisation approach for testing positive definiteness, and uses Gaussian elimination as an implicit diagonalisation algorithm.

---

# Unlocked by This

> [!tip] Spectral Theorem for Self-Adjoint Operators *(LADR §7)*
> The companion form of this theorem, in the inner-product setting. See [[Thm - Real Spectral Theorem]]. Every self-adjoint operator on a real inner product space is diagonalisable in an orthonormal eigenbasis.

> [!tip] Principal-Axis Theorem *(from Classical Mechanics)*
> The "principal-axis theorem" in mechanics is exactly this diagonalisation applied to the inertia tensor or the strain tensor. Every symmetric tensor admits a basis of principal axes.

> [!tip] Quadratic Form Reduction *(from Number Theory)*
> Over $\mathbb{Q}$, $\mathbb{Z}$, or $p$-adic fields, the "diagonalisation" of a symmetric bilinear form is the first step in classification — but the diagonal entries cannot be normalised to $\pm 1$ as easily as over $\mathbb{R}$, and the full classification involves $p$-adic invariants. Sylvester's law gives the archimedean classification; Hasse-Minkowski packages the $p$-adic part.
