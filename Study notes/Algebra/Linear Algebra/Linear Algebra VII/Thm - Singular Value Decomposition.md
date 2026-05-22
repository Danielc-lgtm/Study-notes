---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Singular Values"
  - "Def - Positive Operator"
  - "Thm - Positive Operators Have a Unique Square Root"
  - "Thm - Complex Spectral Theorem"
  - "Def - Isometry"
tags: [algebra, linear-algebra]
---

# Notation

$V$ and $W$ are finite-dimensional [[Def - Inner Product Space|inner product spaces]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$ with $\dim V = n$, $\dim W = m$. The [[Def - Singular Values|singular values]] of $T \in \mathcal{L}(V, W)$ are $s_1(T) \geq \cdots \geq s_n(T) \geq 0$, the non-negative square roots of the eigenvalues of $T^* T$. The unit ball of $V$ is $B = B_V = \{v \in V : \|v\| \leq 1\}$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

---

# Statement

> **Theorem (Singular Value Decomposition).** Let $T \in \mathcal{L}(V, W)$ be any linear map between finite-dimensional inner product spaces. Then there exist:
> - orthonormal vectors $e_1, \ldots, e_n \in V$,
> - orthonormal vectors $f_1, \ldots, f_n \in W$ (some possibly zero in number, padded),
> - non-negative real numbers $s_1 \geq s_2 \geq \cdots \geq s_n \geq 0$,
>
> such that
> $$T e_j = s_j f_j \quad \text{for } j = 1, \ldots, n.$$
> The $s_j$ are the singular values of $T$. The number of strictly positive $s_j$ equals $\operatorname{rank} T$.
>
> In matrix form: every matrix $A \in \mathbb{F}^{m \times n}$ factors as
> $$A = U \Sigma V^*,$$
> where $U \in \mathbb{F}^{m \times m}$ and $V \in \mathbb{F}^{n \times n}$ are [[Def - Unitary Operator|unitary]], and $\Sigma \in \mathbb{R}^{m \times n}$ is a "diagonal" matrix (zero off the main diagonal) with non-negative entries in decreasing order.
>
> **Geometric statement.** The image of the unit ball $T(B_V) \subseteq W$ is an ellipsoid (possibly degenerate) whose principal semi-axes have lengths $s_1, \ldots, s_n$, with the $j$-th semi-axis pointing in the direction $f_j$.

---

# Motivation

The singular value decomposition is the **universal factorisation theorem** of finite-dimensional linear algebra. Every linear map between inner product spaces — square or rectangular, invertible or singular, real or complex — admits an SVD. No condition needs to be checked; it always exists. This universality is what makes the SVD the most widely used factorisation in numerical linear algebra, data science, and signal processing.

The SVD answers the question: **what is the simplest possible representation of a linear map between inner product spaces?** The answer is: in an appropriate pair of orthonormal bases (one for the domain, one for the codomain), the matrix becomes diagonal. The catch — and what distinguishes SVD from eigendecomposition — is that the source and target bases are *different*. Eigendecomposition uses the *same* basis for both, which requires the map to be square and diagonalisable in that basis; SVD allows different bases on each side, and consequently exists for every linear map.

The construction is conceptually straightforward: the positive operator $T^* T$ on $V$ is diagonalised by the [[Thm - Complex Spectral Theorem|spectral theorem]], producing an orthonormal eigenbasis $e_1, \ldots, e_n$ of $V$ with eigenvalues $\lambda_j = s_j^2 \geq 0$. The vectors $T e_j$ are then orthogonal (a computation using $\langle T e_i, T e_j \rangle = \langle T^* T e_i, e_j \rangle = \lambda_i \delta_{ij}$), with norms $\|T e_j\| = \sqrt{\lambda_j} = s_j$. After normalising, $T e_j = s_j f_j$ with $f_j = T e_j / s_j$ orthonormal. Done — the SVD has been constructed from the spectral theorem applied to $T^* T$.

The geometric content is exact: $T$ maps the unit ball of $V$ to an ellipsoid in $W$, and the singular values are the lengths of this ellipsoid's principal semi-axes. The right-singular vectors $e_j$ are the pre-images of the principal axes (in $V$), and the left-singular vectors $f_j$ are the principal axes themselves (in $W$). Visualising the SVD as "the unit ball maps to an ellipsoid" is the right mental model.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is universally satisfied: *any* linear map between finite-dimensional inner product spaces has an SVD. The challenge is recognising *when* SVD is the right tool.

The first disguised source is **a rectangular matrix that is not square**. Eigendecomposition is unavailable, but SVD always exists. *Example problem:* find the rank, operator norm, or pseudoinverse of an $m \times n$ matrix.

The second disguised source is **a non-normal matrix whose eigenvalues are misleading**. The matrix $\begin{pmatrix} 1 & 1000 \\ 0 & 1 \end{pmatrix}$ has both eigenvalues $= 1$ but singular values $\approx 1000$. *Example problem:* what is the condition number of this matrix? Eigenvalues say $\kappa = 1$; SVD says $\kappa \approx 10^6$.

The third disguised source is **a problem asking for the "closest" something**. The best rank-$k$ approximation, best orthogonal projection onto a subspace, distance to a subspace, etc., are all SVD problems. *Example problem:* find the closest unitary matrix to a given matrix; the answer is $UV^*$ from the SVD $T = U \Sigma V^*$.

**Targets (Output Amplification)**

The conclusion is the factorisation $T = U \Sigma V^*$ (or its operator form).

Combine the conclusion with **operator norm computation**: $\|T\|_{\text{op}} = s_1(T)$, the largest singular value. The further result $E$: the operator norm — defined as a supremum — is computed in closed form once the SVD is in hand.

Combine the conclusion with **rank-$k$ truncation**: keep only the largest $k$ singular values and corresponding singular vectors. The result $T_k$ is the unique best rank-$k$ approximation in the operator norm and the Frobenius norm — the **Eckart–Young theorem** (see [[Ex - Best low-rank approximation via SVD]]). This is the foundation of all low-rank approximation: PCA, image compression, latent semantic analysis, recommender systems.

Combine the conclusion with **pseudoinverse**: define $T^+ = V \Sigma^+ U^*$, where $\Sigma^+$ inverts the non-zero entries of $\Sigma$. This is the **Moore–Penrose pseudoinverse**, satisfying $T T^+ T = T$ and three other "Moore–Penrose conditions". The pseudoinverse exists for every linear map, square or not, invertible or not — universality from the SVD.

Combine the conclusion with **polar decomposition**: $T = U \Sigma V^* = (UV^*)(V \Sigma V^*)$, with $UV^*$ a [[Def - Unitary Operator|unitary]] (the "phase") and $V \Sigma V^*$ a [[Def - Positive Operator|positive]] operator (the "magnitude"). The further result $E$ is the [[Thm - Polar Decomposition|polar decomposition]] of $T$.

---

# Why Is It True

The proof is almost a one-liner once you have the spectral theorem.

**The one-liner mechanism: apply the spectral theorem to $T^* T$ — a positive operator — to get an orthonormal eigenbasis $\{e_j\}$ of $V$ with eigenvalues $s_j^2 \geq 0$. Then $\{T e_j / s_j\}$ (for $s_j \neq 0$) is automatically orthonormal in $W$, and $T e_j = s_j (T e_j / s_j)$ is exactly the SVD.**

The key calculation: $\langle T e_i, T e_j \rangle = \langle T^* T e_i, e_j \rangle = \lambda_i \langle e_i, e_j \rangle = \lambda_i \delta_{ij} = s_i^2 \delta_{ij}$. So $\{T e_j\}$ are pairwise orthogonal, with $\|T e_j\| = s_j$. Normalising (dividing by $s_j$) when $s_j > 0$ gives orthonormal vectors $f_j$.

For the singular vectors corresponding to $s_j = 0$: $T e_j = 0$, so $e_j \in \operatorname{null} T$. These vectors do not give us $f_j$ from the formula; we choose them arbitrarily from $(\operatorname{range} T)^\perp$ (over $W$), padded to an orthonormal basis if needed.

The "ellipsoid picture" follows from this. The unit ball $B_V$ is $\{v : \|v\|^2 \leq 1\}$. Write $v = \sum_j \alpha_j e_j$ in the orthonormal eigenbasis of $T^*T$. Then $\|v\|^2 = \sum |\alpha_j|^2$ and $T v = \sum \alpha_j s_j f_j$. The image $T(B_V)$ is the set $\{\sum \alpha_j s_j f_j : \sum |\alpha_j|^2 \leq 1\}$. Substituting $\beta_j = \alpha_j s_j$ (for $s_j \neq 0$), the constraint becomes $\sum |\beta_j|^2/s_j^2 \leq 1$ — the equation of an ellipsoid in $W$ with semi-axis lengths $s_j$.

---

# What Makes This Hard

The non-obvious step is the **realisation that $T^* T$ is the right object** to spectrally analyse — not $T$. For non-square $T$, $T$ has no eigenvalues at all; for square non-normal $T$, the eigenvalues are not informative about the operator norm. The detour through $T^* T$ — converting "any operator" to "a positive operator" — is the trick that makes SVD universally available.

The second subtle step is **handling the zero singular values**. The construction gives orthonormal $f_j$ only for $s_j > 0$. When $s_j = 0$ (which happens precisely on $\operatorname{null} T$), the formula $f_j = T e_j / s_j$ is $0/0$. The fix is to choose the corresponding $f_j$ freely from $(\operatorname{range} T)^\perp$. This is also the source of the *non-uniqueness* of the SVD: multiple choices of $f_j$ for zero singular values give different (but related) decompositions.

The third subtlety is the **uniqueness statement**. The singular values are unique. The singular vectors are unique up to multiplication by a phase (for simple singular values) and up to a unitary rotation within each multi-dimensional singular subspace. So the SVD is "essentially unique" but not literally unique.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Apply the spectral theorem to $T^*T$. Use the orthonormal eigenbasis of $T^*T$ as the right-singular vectors. The vectors $T e_j$ are automatically orthogonal; normalise them to get the left-singular vectors.

**Subgoal decomposition:**

1. **$T^* T$ is positive.** Verify positivity to apply the spectral theorem.

2. **Spectral theorem on $T^*T$.** Get orthonormal $e_1, \ldots, e_n$ of $V$ with $T^* T e_j = \lambda_j e_j$, $\lambda_j \geq 0$.

3. **Define singular values.** Set $s_j = \sqrt{\lambda_j}$, in decreasing order.

4. **Define left-singular vectors.** For $s_j > 0$, set $f_j = T e_j / s_j$. Show $\{f_j\}$ are orthonormal.

5. **Check $T e_j = s_j f_j$.** Immediate from the definition.

6. **Matrix form.** With $V = [e_1, \ldots, e_n]$, $U = [f_1, \ldots, f_m]$ (extended orthonormally if needed), and $\Sigma$ diagonal: $A = U \Sigma V^*$.

---

# Lemma Decomposition

> [!note]- Lemma 1: $T^* T$ is positive
> **Statement:** For any $T \in \mathcal{L}(V, W)$, the operator $T^*T \in \mathcal{L}(V)$ is positive.
>
> **Hint:** Self-adjoint: $(T^*T)^* = T^* T^{**} = T^* T$. Non-negative quadratic form: $\langle T^*T v, v \rangle = \langle Tv, Tv \rangle = \|Tv\|^2 \geq 0$.
>
> **Why needed:** Lets the spectral theorem apply to $T^*T$, producing the right-singular basis.
>
> > [!note]- Full proof
> > $(T^*T)^* = T^* (T^*)^* = T^* T$, using $T^{**} = T$. So $T^*T$ is self-adjoint.
> >
> > For any $v \in V$: $\langle T^*T v, v \rangle = \langle Tv, Tv \rangle_W = \|Tv\|^2_W \geq 0$. So $T^*T$ is positive.

> [!note]- Lemma 2: Vectors $\{T e_j\}$ for orthonormal eigenbasis of $T^* T$ are orthogonal
> **Statement:** If $\{e_1, \ldots, e_n\}$ is an orthonormal eigenbasis of $T^*T$ with eigenvalues $\lambda_j$, then $\langle T e_i, T e_j \rangle = \lambda_i \delta_{ij}$.
>
> **Hint:** Push one $T$ across the inner product: $\langle T e_i, T e_j \rangle = \langle T^* T e_i, e_j \rangle$.
>
> **Why needed:** This orthogonality is what makes the normalised $T e_j / s_j$ form an orthonormal list.
>
> > [!note]- Full proof
> > $\langle T e_i, T e_j \rangle = \langle T^* T e_i, e_j \rangle = \lambda_i \langle e_i, e_j \rangle = \lambda_i \delta_{ij}$.

> [!note]- Lemma 3: The non-zero $T e_j / s_j$ are orthonormal
> **Statement:** If $\lambda_j > 0$ for $j = 1, \ldots, r$ and we set $f_j = T e_j / s_j$ where $s_j = \sqrt{\lambda_j}$, then $\{f_1, \ldots, f_r\}$ is an orthonormal list in $W$.
>
> **Hint:** Use Lemma 2.
>
> **Why needed:** These are the left-singular vectors corresponding to non-zero singular values.
>
> > [!note]- Full proof
> > $\langle f_i, f_j \rangle = \frac{1}{s_i s_j} \langle T e_i, T e_j \rangle = \frac{\lambda_i}{s_i s_j} \delta_{ij}$. When $i = j$, this is $\lambda_i / s_i^2 = 1$. When $i \neq j$, this is $0$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> By Lemma 1, $T^*T \in \mathcal{L}(V)$ is positive. By the spectral theorem ([[Thm - Complex Spectral Theorem]] or [[Thm - Real Spectral Theorem]] depending on $\mathbb{F}$), there is an orthonormal basis $e_1, \ldots, e_n$ of $V$ with $T^* T e_j = \lambda_j e_j$, $\lambda_j \geq 0$. Order the $e_j$ so that $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n \geq 0$. Set $s_j = \sqrt{\lambda_j}$.
>
> Let $r$ be the number of strictly positive $\lambda_j$ (equivalently, $\operatorname{rank}(T^* T) = \operatorname{rank} T$). For $j = 1, \ldots, r$, set $f_j = T e_j / s_j$. By Lemma 3, $\{f_1, \ldots, f_r\}$ is an orthonormal list in $W$.
>
> Extend $\{f_1, \ldots, f_r\}$ to an orthonormal basis $\{f_1, \ldots, f_m\}$ of $W$ (Gram–Schmidt; possible since $r \leq m$). The extended vectors $f_{r+1}, \ldots, f_m$ correspond to "zero singular values" — formally, they pad to make the index sets match. (When $n > m$, the indices $j > m$ may not have corresponding $f_j$; the convention is to pad zeros in $\Sigma$.)
>
> Verification: for $j \leq r$, $T e_j = s_j f_j$ by definition. For $j > r$, $\lambda_j = 0$, so $\|T e_j\|^2 = \langle T^*T e_j, e_j \rangle = 0$, so $T e_j = 0 = s_j f_j$ (since $s_j = 0$).
>
> This completes the orthonormal-basis form of the SVD. The matrix form $A = U \Sigma V^*$ follows by taking $V = [e_1, \ldots, e_n]$, $U = [f_1, \ldots, f_m]$ — both unitary by orthonormality — and $\Sigma$ the diagonal matrix with $s_j$ on the diagonal: $A e_j = s_j f_j$, equivalent to $A V = U \Sigma$, equivalent to $A = U \Sigma V^*$ (since $V$ is unitary). $\blacksquare$
>
> **Uniqueness of singular values.** The $s_j$ are the non-negative square roots of the eigenvalues of $T^*T$, which are uniquely determined by $T$. So the singular value list is unique.

---

# Cross-Field Exercise Suggestions

1. **Statistics — Principal Component Analysis.** Given a centred data matrix $X \in \mathbb{R}^{n \times p}$, the SVD $X = U \Sigma V^*$ gives the principal components as the columns of $V$, with singular values $s_j$ proportional to standard deviations along each component. Truncating to the top $k$ singular values gives the best rank-$k$ approximation of the data — the **Eckart–Young theorem**. PCA is SVD applied to centred data.

2. **Numerical analysis — least squares via SVD.** To solve the overdetermined system $A x = b$ in the least-squares sense — find $x$ minimising $\|Ax - b\|$ — use the SVD $A = U \Sigma V^*$ and set $x = V \Sigma^+ U^* b$, where $\Sigma^+$ inverts the non-zero entries of $\Sigma$. This is the Moore–Penrose pseudoinverse approach to least squares, the most numerically stable method.

3. **Image processing — JPEG-like compression.** An image, viewed as a matrix of pixel values, has SVD $X = U \Sigma V^*$. Truncating to the top $k$ singular values gives a compressed image (storing only the $k$ singular values and $k$ singular vectors instead of all $n \times p$ pixels). The visual quality of the reconstruction depends on how rapidly the singular values decay; natural images have rapidly decaying singular values, making them compressible.

4. **Information retrieval — Latent Semantic Analysis.** A term-document matrix $T$ has rows indexed by words, columns by documents, and entries equal to term frequencies. SVD truncation $T \approx U_k \Sigma_k V_k^*$ gives a $k$-dimensional "semantic embedding" — words and documents become points in $\mathbb{R}^k$, with similarity measured by inner product. This is the foundation of latent semantic analysis and the precursor to modern word embeddings like word2vec.

---

# Bridges

- **[[Thm - Polar Decomposition]]** — Polar decomposition follows from SVD by regrouping: $T = U\Sigma V^* = (UV^*)(V\Sigma V^*)$, with $S = UV^*$ unitary (a partial isometry in general) and $R = V\Sigma V^* = \sqrt{T^*T} = |T|$ positive. The SVD is "factored polar decomposition"; the polar decomposition is "regrouped SVD".

- **[[Thm - Positive Operators Have a Unique Square Root]]** — The square root construction is what produces the singular values from $T^*T$. The eigenvalues of $T^*T$ are non-negative; their square roots are well-defined (this theorem); these square roots are the singular values.

- **[[Thm - Complex Spectral Theorem]] / [[Thm - Real Spectral Theorem]]** — The spectral theorem applied to $T^*T$ produces the right-singular basis. The SVD is "spectral theorem applied to a derived positive operator".

- **Operator norm and Frobenius norm** — The SVD makes both norms computable: $\|T\|_{\text{op}} = s_1$ and $\|T\|_F^2 = \sum_j s_j^2$. The whole family of **Schatten $p$-norms** is $\|T\|_p = (\sum_j s_j^p)^{1/p}$. These norms generalise the corresponding $\ell^p$ norms on sequence spaces, with the singular values playing the role of "the operator's components".

- **Moore–Penrose pseudoinverse** — Defined via the SVD as $T^+ = V \Sigma^+ U^*$, where $\Sigma^+$ replaces each nonzero $s_j$ on the diagonal with $1/s_j$ and leaves zeros zero. The pseudoinverse satisfies $TT^+T = T$, $T^+TT^+ = T^+$, and the **Moore–Penrose conditions** characterising it uniquely. It is the operator-theoretic analogue of "the inverse on the range, zero on the null space".

---

# Unlocked by This

> [!tip] Eckart–Young Theorem and Low-Rank Approximation *(from Numerical Linear Algebra)*
> The **Eckart–Young theorem** (see [[Ex - Best low-rank approximation via SVD]]) states that the rank-$k$ truncation of the SVD — $T_k = \sum_{j=1}^{k} s_j f_j e_j^*$ — is the best rank-$k$ approximation of $T$ in both the operator norm and the Frobenius norm. The error is $\|T - T_k\|_{\text{op}} = s_{k+1}$ and $\|T - T_k\|_F^2 = \sum_{j > k} s_j^2$. This is the theorem behind **dimensionality reduction**: every modern technique (PCA, randomized SVD, sketching, dynamic mode decomposition) relies on the Eckart–Young theorem for its theoretical justification.

> [!tip] Randomised SVD and Scalable Numerical Algorithms *(from Modern Numerical Analysis)*
> For very large matrices (where direct SVD is computationally infeasible), the **randomised SVD** computes an approximate truncated SVD in time $O(mn k + (m + n) k^2)$ instead of the $O(mn^2)$ of standard SVD. The algorithm sketches the matrix by random projection, computes SVD of the much smaller sketch, and lifts back. The error analysis — bounded by something involving $\sqrt{s_{k+1}}$ and the random projection dimension — relies on the Eckart–Young theorem. Randomised SVD scales to terabyte matrices and is the engine of modern recommendation systems, network analysis, and large-scale machine learning.

> [!tip] Wasserstein Distance and Optimal Transport on Matrix Manifolds *(from Optimization)*
> The set of $m \times n$ matrices of rank exactly $k$ forms an algebraic variety; the **fixed-rank manifold** $\mathcal{M}_k$ is naturally identified with $V_k(\mathbb{F}^m) \times \mathbb{R}_{>0}^k \times V_k(\mathbb{F}^n)$ via SVD, where $V_k$ is the Stiefel manifold of orthonormal $k$-frames. The Riemannian metric on $\mathcal{M}_k$ inherited from $\mathbb{F}^{m \times n}$ makes optimisation over rank-$k$ matrices a manifold optimisation problem; the **Riemannian conjugate gradient** and related methods solve such problems efficiently. Matrix completion, robust PCA, and tensor decomposition all reduce to optimisation on these manifolds, with SVD as the basic coordinate system.
