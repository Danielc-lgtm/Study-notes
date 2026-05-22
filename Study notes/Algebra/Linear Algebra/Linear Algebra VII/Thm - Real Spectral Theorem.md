---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Self-Adjoint Operator"
  - "Def - Adjoint of a Linear Map"
  - "Def - Inner Product Space"
  - "Def - Orthonormal Basis"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional [[Def - Inner Product Space|inner product space]] over $\mathbb{R}$. An operator $T \in \mathcal{L}(V)$ is [[Def - Self-Adjoint Operator|self-adjoint]] if $T = T^*$, equivalently $\langle Tv, w \rangle = \langle v, Tw \rangle$ for all $v, w$ — in an orthonormal basis the matrix of $T$ is symmetric. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

---

# Statement

> **Theorem (Real Spectral Theorem).** Let $V$ be a finite-dimensional real inner product space and $T \in \mathcal{L}(V)$. The following are equivalent:
>
> 1. $T$ is [[Def - Self-Adjoint Operator|self-adjoint]] ($T = T^*$).
> 2. $V$ has an orthonormal basis consisting of eigenvectors of $T$.
> 3. The matrix of $T$ in some orthonormal basis is real diagonal.
>
> Equivalently, $T$ admits a **spectral decomposition** $T = \sum_j \lambda_j P_j$ with real eigenvalues $\lambda_j$ and mutually orthogonal projections $P_j$ onto the eigenspaces $E(\lambda_j, T)$.

> [!warning] The hypothesis is not "normal"; it is "self-adjoint".
> Over $\mathbb{C}$, normality suffices for orthonormal diagonalisability ([[Thm - Complex Spectral Theorem|complex spectral theorem]]). Over $\mathbb{R}$, normality is insufficient — the $90^\circ$ rotation matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ is orthogonal hence normal, but has no real eigenvectors. Self-adjointness is the precise condition over $\mathbb{R}$ that forces the (a priori complex) eigenvalues to be real, allowing them to descend to $\mathbb{R}$.

---

# Motivation

The real spectral theorem is the real-field counterpart to the complex spectral theorem. The headline statement is parallel: an operator on a real inner product space is orthonormally diagonalisable if and only if it satisfies an algebraic condition involving its adjoint. The condition, however, is *self-adjointness*, not normality — and this stricter requirement is precisely what is needed to make the proof go through over $\mathbb{R}$.

Why is the requirement stronger? Because the fundamental theorem of algebra is in play, and over $\mathbb{R}$ the FTA does not deliver real eigenvalues — the characteristic polynomial $\det(T - \lambda I)$ might have only complex roots. The $90^\circ$ rotation has $\det(T - \lambda I) = \lambda^2 + 1$ with roots $\pm i$, neither real. So a normal operator over $\mathbb{R}$ might have no real eigenvalues at all, and the spectral theorem's inductive proof — which extracts one eigenvector at a time — cannot start.

Self-adjointness rescues the situation. **An eigenvalue of a self-adjoint operator is automatically real**: if $Tv = \lambda v$ with $v \neq 0$ on a complex inner product space, then $\lambda \|v\|^2 = \langle Tv, v \rangle = \langle v, Tv \rangle = \overline{\lambda \|v\|^2}$, so $\lambda \in \mathbb{R}$. This statement (proved formally in [[Ex - Self-adjoint operators have real eigenvalues]]) is the crucial input that makes the real spectral theorem work: even though we start over $\mathbb{R}$, complexifying $V$ and using the FTA gives a complex eigenvalue, but self-adjointness forces it real, so the eigenvalue and its eigenvector descend back to the real space.

The clean way to think about this: the real spectral theorem is the complex spectral theorem, with the condition tightened from "normal" to "self-adjoint" to compensate for the FTA's weakness over $\mathbb{R}$. Every other aspect — the orthonormal eigenbasis, the spectral decomposition, the functional calculus — is identical. The boundary between $\mathbb{R}$ and $\mathbb{C}$ in the spectral theorem is precisely the requirement of self-adjointness.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$T$ is a self-adjoint operator on a real inner product space" — most often realised as "the matrix of $T$ in an orthonormal basis is real symmetric".

The first disguised source is **a real symmetric matrix arising from an optimisation problem**. The Hessian matrix of a smooth real-valued function $f : \mathbb{R}^n \to \mathbb{R}$ at a critical point is $H_{ij} = \partial^2 f / \partial x_i \partial x_j$, which is symmetric (mixed partials commute, by Schwarz's theorem). The spectral theorem then gives an orthonormal basis of "principal directions" with real eigenvalues, classifying the critical point as minimum, maximum, or saddle. *Example problem:* find the principal curvatures of a surface at a point.

The second disguised source is **a real symmetric matrix from a quadratic form**. Any quadratic form $q : V \to \mathbb{R}$ can be written as $q(v) = \langle Tv, v \rangle$ for a *unique* self-adjoint operator $T$. The spectral theorem then diagonalises the form: in the eigenbasis, $q(v) = \sum \lambda_j v_j^2$, expressing the form as a weighted sum of squares. This is Sylvester's law of inertia in its constructive version. *Example problem:* classify a real quadric surface by its signature.

The third disguised source is **a Gram matrix or covariance matrix**. These are always symmetric and positive (semi)definite — special cases of self-adjoint operators. The spectral theorem then provides the principal components and the variance decomposition. *Example problem:* the covariance matrix of $n$ data points in $\mathbb{R}^d$ is symmetric and positive semidefinite; its spectral decomposition is PCA.

**Targets (Output Amplification)**

The conclusion is "$V$ has an orthonormal eigenbasis with real eigenvalues for $T$".

Combine the conclusion with **a real symmetric quadratic form**: the form is diagonalised by the eigenbasis, and the eigenvalues are the coefficients of the diagonal form. The further result $E$ is **Sylvester's law of inertia**: the number of positive, negative, and zero eigenvalues (the *signature*) is a basis-independent invariant of the quadratic form.

Combine the conclusion with **the simultaneous diagonalisation of two real symmetric forms** (one positive definite): given $A$ symmetric and $B$ symmetric positive definite, there is a basis (not orthonormal in the standard inner product but orthonormal with respect to $B$) in which both $A$ and $B$ are diagonal. The further result $E$ is **generalised eigenvalue decomposition** $A v = \lambda B v$, used in mechanical vibration problems, generalised principal component analysis, and Fisher's linear discriminant analysis.

Combine the conclusion with **the polar decomposition over $\mathbb{R}$**: every invertible real matrix factors as $T = OS$ where $O$ is orthogonal and $S$ is symmetric positive definite. The further result $E$ is the canonical decomposition of $\operatorname{GL}_n(\mathbb{R})$ into rotation and stretching parts, generalising the polar form of a complex number to the matrix setting.

---

# Why Is It True

The proof must produce a real eigenvalue at each step of the induction, even though the FTA only gives complex eigenvalues over $\mathbb{R}$. The trick is to **complexify**: extend $V$ to $V_\mathbb{C} = V \otimes_\mathbb{R} \mathbb{C}$, extend $T$ to a $\mathbb{C}$-linear operator on $V_\mathbb{C}$, apply the FTA to get a complex eigenvalue, then use self-adjointness to force the eigenvalue real and the eigenvector to live in the real subspace.

**The one-liner mechanism: complexify, get a complex eigenvalue from the FTA, and use $\lambda \|v\|^2 = \langle Tv, v \rangle = \langle v, Tv \rangle = \overline{\lambda \|v\|^2}$ to force $\lambda \in \mathbb{R}$; the eigenvector then descends to the real subspace and induction proceeds as in the complex case.**

The key intuition: self-adjointness *kills the imaginary parts*. The quadratic form $\langle Tv, v \rangle$ is symmetric in $v$ and equal to its conjugate, hence real. Eigenvalues, which are $\langle Tv, v \rangle / \|v\|^2$ for an eigenvector $v$, are therefore real. The eigenvectors, being eigenvectors of a real symmetric operator on the complexification, must have real and imaginary parts each also being eigenvectors (or zero) — so we can extract a real eigenvector.

Alternatively, one can prove the real spectral theorem more directly without complexification, by an argument analogous to the complex case but with self-adjointness in place of normality. The advantage of the complexification proof is conceptual clarity: it shows precisely why self-adjointness is needed (to force the FTA-supplied complex eigenvalue to be real). The advantage of the direct proof is that it stays within the real category. We give the complexification proof in the formal section.

The orthogonality of distinct-eigenvalue eigenvectors is the same calculation as in the complex case: $\lambda \langle v, w \rangle = \langle Tv, w \rangle = \langle v, Tw \rangle = \mu \langle v, w \rangle$ (using $T = T^*$ and that $\mu$ is real, so no conjugation), giving orthogonality when $\lambda \neq \mu$.

---

# What Makes This Hard

The non-obvious step is the **eigenvalue reality calculation**: that a self-adjoint operator's eigenvalues are real, even though the operator is defined over $\mathbb{R}$. The naive reading "eigenvalues of a real matrix are real" is *false* (e.g., for the rotation matrix). What is true is "eigenvalues of a *self-adjoint* real matrix are real". The condition $T = T^*$ does the work, and the proof requires the trick of computing $\langle Tv, v \rangle$ in two ways.

The second subtle step is **why complexification is licit**. Extending $T$ to $V_\mathbb{C}$ is straightforward, but one must check that the complexified operator is still self-adjoint with respect to the complex inner product on $V_\mathbb{C}$. This requires extending the inner product to $V_\mathbb{C}$ as a Hermitian form (taking complex conjugates in one slot), so the real symmetric matrix becomes a complex Hermitian matrix.

The third subtle step is **descending the eigenvector to the real subspace**. The complex eigenvector $v = v_1 + i v_2$ (with $v_1, v_2 \in V$) for real eigenvalue $\lambda$ satisfies $T(v_1 + iv_2) = \lambda(v_1 + iv_2)$, so $Tv_1 = \lambda v_1$ and $Tv_2 = \lambda v_2$ — both real and imaginary parts are real eigenvectors (when non-zero). At least one of $v_1, v_2$ is non-zero (since $v \neq 0$), giving a real eigenvector.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Show that every self-adjoint operator on a finite-dimensional real inner product space has at least one real eigenvalue (by complexification and the FTA, forcing the eigenvalue real via self-adjointness). Then induct on dimension as in the complex case.

**Subgoal decomposition:**

1. **Eigenvalues of a self-adjoint operator are real.** Show that for $T = T^*$ on any (real or complex) inner product space, every eigenvalue is real.
   - *Hint:* If $Tv = \lambda v$, $v \neq 0$, then $\lambda \langle v, v \rangle = \langle Tv, v \rangle = \langle v, Tv \rangle = \overline{\lambda \langle v, v \rangle}$ — but $\langle v, v \rangle$ is real and positive.
   - *Why needed:* Without this, the complexification step cannot land back in the real space.

2. **A real self-adjoint operator has a real eigenvalue.** Use complexification: extend $T$ to $V_\mathbb{C}$, get a complex eigenvalue from the FTA, use subgoal 1 to force it real, descend the eigenvector to $V$.
   - *Hint:* The complexified operator on $V_\mathbb{C}$ is still self-adjoint. Real and imaginary parts of a complex eigenvector with real eigenvalue are themselves real eigenvectors.
   - *Why needed:* The induction base.

3. **Eigenspaces are invariant under $T$, and orthogonal complements of eigenspaces are also invariant.** Follow the complex spectral theorem proof — the same argument works, with self-adjointness in place of normality (and trivially: if $T = T^*$, then $T$ and $T^*$ are the same operator, so $T^*$-invariance is the same as $T$-invariance).
   - *Hint:* This step is even easier than over $\mathbb{C}$ — there is no separate $T^*$-invariance to check.
   - *Why needed:* Inductive step engine.

4. **Restriction of $T$ to an invariant subspace is self-adjoint.** A subspace $U$ that is $T$-invariant has $T|_U$ self-adjoint with respect to the inherited inner product (since $T^*|_U = T|_U$ trivially when $T = T^*$).
   - *Hint:* Self-adjointness restricts to invariant subspaces for free.
   - *Why needed:* For induction to work.

5. **Induction on dimension.** Combine 1–4 with the orthogonality of distinct-eigenvalue eigenvectors (same as the complex case).

---

# Lemma Decomposition

> [!note]- Lemma 1: Eigenvalues of self-adjoint operators are real
> **Statement:** Let $T$ be self-adjoint on an inner product space (real or complex), and $\lambda$ an eigenvalue. Then $\lambda \in \mathbb{R}$.
>
> **Hint:** Compute $\lambda \langle v, v \rangle$ two ways using $T = T^*$, and use that $\langle v, v \rangle > 0$ for $v \neq 0$.
>
> **Why needed:** The crucial input that distinguishes self-adjoint operators from general operators. Without it, the FTA's complex eigenvalue might not descend.
>
> > [!note]- Full proof
> > Let $v$ be a nonzero eigenvector with eigenvalue $\lambda$. Then $\lambda \langle v, v \rangle = \langle \lambda v, v \rangle = \langle Tv, v \rangle = \langle v, Tv \rangle = \langle v, \lambda v \rangle = \overline{\lambda} \langle v, v \rangle$, using self-adjointness at the middle step and conjugate-linearity in the second slot at the end. So $(\lambda - \overline{\lambda}) \langle v, v \rangle = 0$; since $\langle v, v \rangle > 0$, $\lambda = \overline{\lambda}$, i.e., $\lambda \in \mathbb{R}$.

> [!note]- Lemma 2: Real self-adjoint operators have a real eigenvalue
> **Statement:** Let $V$ be a finite-dimensional real inner product space and $T \in \mathcal{L}(V)$ self-adjoint. Then $T$ has at least one real eigenvalue.
>
> **Hint:** Complexify: extend $V$ to $V_\mathbb{C}$ and $T$ to $T_\mathbb{C}$. Apply the FTA, then Lemma 1, then descend.
>
> **Why needed:** Without this base case the induction over $\mathbb{R}$ cannot start.
>
> > [!note]- Full proof
> > Let $V_\mathbb{C} = V \otimes_\mathbb{R} \mathbb{C}$, with the Hermitian inner product extending the real inner product: $\langle v + iw, v' + iw' \rangle = \langle v, v' \rangle + \langle w, w' \rangle + i(\langle w, v' \rangle - \langle v, w' \rangle)$. Extend $T$ to $T_\mathbb{C} : V_\mathbb{C} \to V_\mathbb{C}$ by $\mathbb{C}$-linearity. The matrix of $T_\mathbb{C}$ in a real orthonormal basis of $V$ is the same real symmetric matrix as $T$; since real symmetric matrices are Hermitian, $T_\mathbb{C}$ is self-adjoint with respect to the Hermitian inner product.
> >
> > Apply the fundamental theorem of algebra to the characteristic polynomial of $T_\mathbb{C}$ to get a complex eigenvalue $\lambda \in \mathbb{C}$. By Lemma 1, $\lambda \in \mathbb{R}$.
> >
> > Let $u = v_1 + iv_2 \in V_\mathbb{C}$ ($v_1, v_2 \in V$) be a nonzero eigenvector: $T_\mathbb{C} u = \lambda u$, i.e., $T v_1 + i T v_2 = \lambda v_1 + i \lambda v_2$. Equating real and imaginary parts: $T v_1 = \lambda v_1$ and $T v_2 = \lambda v_2$. Since $u \neq 0$, at least one of $v_1, v_2$ is nonzero — providing a real eigenvector of $T$ with real eigenvalue $\lambda$.

> [!note]- Lemma 3: Eigenspaces and orthogonal complements are invariant
> **Statement:** Let $T \in \mathcal{L}(V)$ be self-adjoint and $U = E(\lambda, T)$ an eigenspace. Then $T(U) \subseteq U$ and $T(U^\perp) \subseteq U^\perp$.
>
> **Hint:** $T$-invariance of eigenspaces is trivial. For $U^\perp$, push $T$ across the inner product, using $T = T^*$.
>
> **Why needed:** Lets the induction recurse on the orthogonal complement, which is strictly smaller.
>
> > [!note]- Full proof
> > $T$-invariance of $U$ is trivial: if $v \in U$ then $Tv = \lambda v \in U$.
> >
> > For $T$-invariance of $U^\perp$: let $w \in U^\perp$. For any $u \in U$, $\langle u, Tw \rangle = \langle Tu, w \rangle$ (self-adjointness) $= \lambda \langle u, w \rangle = 0$ (since $u \in U$ means $Tu = \lambda u$, and $w \perp U$). So $Tw \perp U$, i.e., $Tw \in U^\perp$.

---

# Formal Proof

> [!note]- Complete formal proof
> We prove (1) $\Leftrightarrow$ (2); (3) is a matrix-form restatement of (2).
>
> **(2) $\Rightarrow$ (1).** If $V$ has an orthonormal eigenbasis $e_1, \ldots, e_n$ with $Te_j = \lambda_j e_j$ ($\lambda_j \in \mathbb{R}$), then in this basis the matrix of $T$ is $D = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$, a real diagonal matrix. The conjugate transpose (over $\mathbb{R}$, just the transpose) of $D$ is $D$ itself. So $T = T^*$, i.e., $T$ is self-adjoint.
>
> **(1) $\Rightarrow$ (2).** Induct on $n = \dim V$.
>
> *Base case $n = 1$:* any unit vector is an eigenvector.
>
> *Inductive step.* Assume the result for inner product spaces of dimension less than $n$. By Lemma 2, $T$ has a real eigenvalue $\lambda_1 \in \mathbb{R}$ with a real eigenvector $e_1$, which we normalise to unit length. Let $U = E(\lambda_1, T) \supseteq \mathbb{R} e_1$. By Lemma 3, $W := U^\perp$ is $T$-invariant.
>
> The restriction $T|_W$ is self-adjoint with respect to the inner product on $W$: for $v, w \in W$, $\langle T|_W v, w \rangle_W = \langle Tv, w \rangle_V = \langle v, Tw \rangle_V = \langle v, T|_W w \rangle_W$, where the inner products coincide because $W$ inherits the inner product from $V$.
>
> Since $\dim W = \dim V - \dim U < n$, the inductive hypothesis gives an orthonormal eigenbasis of $W$ consisting of eigenvectors of $T|_W$ (hence of $T$), with real eigenvalues by Lemma 1.
>
> Concatenate an orthonormal basis of $U$ (which exists and consists of eigenvectors of $T$ for $\lambda_1$) with the orthonormal eigenbasis of $W$. By the orthogonal decomposition $V = U \oplus W$ with $U \perp W$, the result is an orthonormal eigenbasis of $V$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

1. **Riemannian geometry — principal curvatures of a surface.** At each point of a smooth surface $\Sigma \subseteq \mathbb{R}^3$, the **shape operator** (or Weingarten map) is a self-adjoint operator on the tangent plane. Its eigenvalues are the **principal curvatures** $\kappa_1, \kappa_2$, the eigenvectors are the **principal curvature directions**. The real spectral theorem gives an orthogonal pair of principal directions at every point. The Gaussian curvature is $K = \kappa_1 \kappa_2$, and the mean curvature is $H = \frac{1}{2}(\kappa_1 + \kappa_2)$ — invariants of the spectral decomposition.

2. **Mechanical vibrations — normal modes.** For an oscillating system of $n$ point masses on linear springs, the equation of motion is $M \ddot x = -K x$ where $M$ is the diagonal mass matrix (symmetric positive definite) and $K$ is the symmetric (positive semidefinite) stiffness matrix. The eigenvalue problem $K v = \omega^2 M v$ — a *generalised* eigenvalue problem — diagonalises both $M$ and $K$ simultaneously, by reducing it to $\tilde K \tilde v = \omega^2 \tilde v$ where $\tilde K = M^{-1/2} K M^{-1/2}$ is symmetric. The real spectral theorem then gives orthogonal **normal modes** $v_j$ oscillating at frequencies $\omega_j$, with arbitrary initial conditions decomposing into a sum of normal modes.

3. **Optimisation — second-order conditions and the Hessian.** For a smooth function $f : \mathbb{R}^n \to \mathbb{R}$ at a critical point $x_0$, the Hessian $H f(x_0)$ is a real symmetric matrix. Its spectral decomposition gives orthogonal **principal axes** of the local quadratic approximation, with eigenvalues classifying the critical point: all positive ⇒ local minimum; all negative ⇒ local maximum; mixed signs ⇒ saddle. The signature of the Hessian is a basis-independent invariant of the critical point.

4. **Inertia tensor in classical mechanics.** A rigid body has an **inertia tensor** $I_{ij} = \int (\|x\|^2 \delta_{ij} - x_i x_j) \rho(x) \, dV$, a real symmetric matrix. Its eigenvalues are the **principal moments of inertia** and its eigenvectors are the **principal axes**. Rotation about a principal axis is stable; rotation about a non-principal axis is, generically, not (the tennis racket theorem). The real spectral theorem is what makes the concept of "principal axes" well-defined.

---

# Bridges

- **[[Thm - Complex Spectral Theorem]]** — The complex case has the weaker hypothesis "normal" instead of "self-adjoint", because over $\mathbb{C}$ the FTA gives complex eigenvalues directly, with no need to force them real. The real spectral theorem is the complex spectral theorem with the hypothesis tightened to compensate for the FTA's weakness over $\mathbb{R}$.

- **Sylvester's Law of Inertia** — A real symmetric matrix $A$ has an associated quadratic form $q(v) = v^t A v$. The spectral decomposition $A = O D O^t$ (with $O$ orthogonal and $D$ diagonal) gives a basis in which $q(\tilde v) = \sum \lambda_j \tilde v_j^2$ — sum of squares with weights. The number of positive, negative, and zero eigenvalues — the **signature** $(p, q, 0)$ — is a complete invariant of the form under arbitrary changes of basis (not just orthogonal ones). The real spectral theorem is the constructive content of Sylvester's law of inertia.

- **Generalised eigenvalue problem** — Given $A$ symmetric and $B$ symmetric positive definite, the **generalised eigenvalue problem** is $Av = \lambda Bv$. It is equivalent to the ordinary eigenvalue problem $B^{-1/2} A B^{-1/2} \tilde v = \lambda \tilde v$, with $\tilde v = B^{1/2} v$ and the modified matrix $B^{-1/2} A B^{-1/2}$ symmetric. So both $A$ and $B$ can be simultaneously diagonalised by a non-orthogonal change of basis. This generalisation is used wherever two quadratic forms appear together — mechanical vibrations, Fisher's linear discriminant analysis, generalised canonical correlation analysis.

- **Min-max characterisation (Courant–Fischer)** — The eigenvalues of a real symmetric matrix $A$ admit the characterisation $\lambda_k(A) = \min_{\dim U = n - k + 1} \max_{v \in U, \|v\| = 1} v^t A v$. This converts eigenvalue computations to variational problems and gives **Weyl's inequality**: if $A$ and $B$ are symmetric and $C = A + B$, then $\lambda_k(A) + \lambda_n(B) \leq \lambda_k(C) \leq \lambda_k(A) + \lambda_1(B)$. The variational characterisation is the foundation of finite-element methods for elliptic PDEs.

---

# Unlocked by This

> [!tip] Quantum Mechanics on Real-Spectrum Observables *(from Physics)*
> Every observable in quantum mechanics is a self-adjoint operator. Over a complex Hilbert space, the [[Thm - Complex Spectral Theorem|complex spectral theorem]] applies (with the stronger normality hypothesis) — but quantum mechanics in fact only ever uses *self-adjoint* operators, so the conclusion of the real spectral theorem (real eigenvalues, orthonormal eigenbasis) is what is actually needed. The reality of measurement outcomes is the reality of eigenvalues of a self-adjoint operator. The real spectral theorem on its own is enough to set up quantum mechanics on a real Hilbert space, although the standard formulation uses complex Hilbert spaces for the additional flexibility of phase.

> [!tip] Sylvester's Law of Inertia and Classification of Real Quadrics *(from Algebraic Geometry / Classical Geometry)*
> A **real quadric** is a hypersurface in $\mathbb{R}^n$ defined by a degree-2 polynomial $q(x) = \sum_{ij} A_{ij} x_i x_j + \sum b_i x_i + c$. The matrix $A$ is symmetric and admits an orthonormal eigendecomposition by the real spectral theorem. Diagonalising gives the quadric in the form $\sum \lambda_j x_j^2 + \text{linear terms}$ — a sum of squares with signs. The signature $(p, q, 0)$ of $A$ — the number of positive, negative, and zero eigenvalues — classifies the quadric up to affine equivalence: $(2, 0, 0)$ in $\mathbb{R}^2$ is an ellipse, $(1, 1, 0)$ is a hyperbola, etc. The full classification of real quadrics is the application of Sylvester's law to the matrix of the quadratic form, made constructive by the real spectral theorem.

> [!tip] Spectral Graph Theory — Real Spectral Theorem for Laplacians *(from Combinatorics / Network Science)*
> The Laplacian matrix $L$ of an undirected graph is real symmetric and positive semidefinite. By the real spectral theorem, $L$ has an orthonormal eigenbasis with real non-negative eigenvalues $0 = \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_n$. The multiplicity of $0$ is the number of connected components; $\lambda_2$ (the **algebraic connectivity** or **Fiedler value**) measures how strongly connected the graph is; $\lambda_n$ controls expansion. The eigenvectors define the **spectral embedding** of the graph into $\mathbb{R}^k$, which is the foundation of spectral clustering, the normalised cut algorithm, and many community-detection methods. The eigenvectors corresponding to small eigenvalues give a "natural coordinate system" on the graph that respects its connectivity.
