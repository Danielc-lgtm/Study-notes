---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Self-Adjoint Operator"
  - "Def - Adjoint of a Linear Map"
  - "Def - Inner Product Space"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional [[Def - Inner Product Space|inner product space]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$. An operator $T \in \mathcal{L}(V)$ has an [[Def - Adjoint of a Linear Map|adjoint]] $T^*$; it is [[Def - Self-Adjoint Operator|self-adjoint]] if $T = T^*$. We write $T \geq 0$ to mean "$T$ is positive" and $T > 0$ to mean "$T$ is positive definite". Some references (Boyd; numerical analysis) use **positive semidefinite (PSD)** for what we call positive, reserving "positive definite (PD)" for what we call positive definite — the same convention. Axler reserves "positive" for $T \geq 0$ and uses "positive definite" for $T > 0$ in §7C; we follow Axler.

> [!warning] Convention: "positive" means $\geq 0$, not $> 0$.
> Some authors (e.g. Bhatia, some functional analysis texts) use "positive" for what we call "positive definite". The conventions are universally distinguishable by context: "positive operator" with no further qualifier most commonly means $\geq 0$ (so $T = 0$ is positive). When we want to exclude $0$ and force invertibility, we say "positive definite".

The unique positive square root of a positive operator $T$ is denoted $\sqrt{T}$ — its existence and uniqueness is the content of [[Thm - Positive Operators Have a Unique Square Root]].

---

# Axiom Motivation

A positive operator is the operator analogue of a non-negative real number. The motivation is simple: in the ladder

$$\text{normal} \supset \text{self-adjoint} \supset \text{positive}$$

each successive class corresponds, via the spectral theorem, to a more restricted location of eigenvalues. Normal operators have arbitrary complex eigenvalues; self-adjoint operators have real eigenvalues; positive operators have *non-negative* eigenvalues. They form the operator analogues of $\mathbb{C}$, $\mathbb{R}$, and $\mathbb{R}_{\geq 0}$.

Why is this analogy substantive? Because **a positive operator has a unique positive square root** ([[Thm - Positive Operators Have a Unique Square Root]]) — exactly as a non-negative real number has a unique non-negative square root. The square root is taken in the operator sense: $\sqrt{T}$ is the unique positive operator $R$ with $R^2 = T$. This is what makes the "absolute value" $|T| = \sqrt{T^* T}$ of an arbitrary operator well-defined; the operator $T^* T$ is positive (Step 2 of the SVD argument: $\langle T^*Tv, v \rangle = \langle Tv, Tv \rangle = \|Tv\|^2 \geq 0$), so $\sqrt{T^* T}$ makes sense and is unique. The polar decomposition $T = S |T|$ from §7F then realises the analogy $z = e^{i\theta} \cdot |z|$ at the operator level.

The definition combines two clauses: $T$ is self-adjoint, **and** $\langle Tv, v \rangle \geq 0$ for all $v$. Why both? Over $\mathbb{C}$, the condition $\langle Tv, v \rangle \geq 0$ for all $v$ actually implies self-adjointness (because $\langle Tv, v \rangle \in \mathbb{R}$ for all $v$ implies $T = T^*$ via polarisation). So over $\mathbb{C}$, the self-adjointness clause is redundant — but it is included for emphasis and for parallelism with the real case. Over $\mathbb{R}$, the condition $\langle Tv, v \rangle \geq 0$ for all real $v$ does *not* imply self-adjointness (skew-symmetric matrices satisfy $\langle Tv, v \rangle = 0$ for all $v$, hence $\geq 0$, but are not self-adjoint). The self-adjointness clause is essential over $\mathbb{R}$, redundant over $\mathbb{C}$. Including it uniformly is the cleanest convention.

What if you tried to drop the self-adjointness over $\mathbb{R}$? Then "positive" operators would include all skew-symmetric matrices (the quadratic form $v^t T v$ vanishes for skew-symmetric $T$), and the spectral theorem would not apply — skew-symmetric matrices have purely imaginary eigenvalues, not non-negative real ones. The square-root construction would also fail catastrophically. The self-adjointness clause is the precise condition that makes the eigenvalues real (so "non-negative" makes sense) and forces orthonormal diagonalisability.

What if you tried to weaken $\geq 0$ to "every eigenvalue is non-negative"? Then non-self-adjoint operators with real non-negative eigenvalues — for example $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ — would count as "positive". But these do not have non-negative numerical range, do not arise as $S^* S$, and do not have positive square roots (in any reasonable sense). The condition $\langle Tv, v \rangle \geq 0$ — the *quadratic form* being non-negative — is the right strengthening of "eigenvalues non-negative" for inner-product purposes.

The equivalent characterisations are worth understanding as a single picture. The four conditions

(a) $T$ is self-adjoint with non-negative eigenvalues
(b) $\langle Tv, v \rangle \geq 0$ for all $v$ (with $T = T^*$ over $\mathbb{R}$, automatic over $\mathbb{C}$)
(c) $T = S^* S$ for some $S \in \mathcal{L}(V, W)$
(d) $T = R^2$ for some self-adjoint $R$
(e) $T$ has a (necessarily unique) positive square root $\sqrt{T}$

are equivalent. Each captures a different *flavour* of "positive":
- (a) is the spectral characterisation: the eigenvalues are in the right half-line.
- (b) is the quadratic form characterisation: the operator gives non-negative inner products on the diagonal.
- (c) is the **factorisation characterisation**: positive operators are exactly the "norm-squared" operators $S^*S$ — every positive operator arises this way, and every $S^*S$ is positive.
- (d) is the **square characterisation**: positive operators are exactly the squares of self-adjoint operators.
- (e) is the **uniqueness characterisation**: positive operators have a *uniquely determined* positive square root, the operator-theoretic analogue of the principal square root of a non-negative real.

The equivalence of all five is the content of §7C.

---

# The Definition

An operator $T \in \mathcal{L}(V)$ is **positive** (or **positive semidefinite**) if:
1. $T$ is [[Def - Self-Adjoint Operator|self-adjoint]] ($T = T^*$);
2. $\langle Tv, v \rangle \geq 0$ for all $v \in V$.

It is **positive definite** if the inequality is strict for $v \neq 0$:
$$\langle Tv, v \rangle > 0 \quad \text{for all } v \neq 0.$$

We write $T \geq 0$ and $T > 0$ for these conditions respectively. The relation $T \geq S$ means $T - S \geq 0$.

**Equivalent characterisations.** For $T \in \mathcal{L}(V)$ self-adjoint, the following are equivalent:
1. $T$ is positive.
2. $T$ has only non-negative eigenvalues.
3. $T = S^* S$ for some $S \in \mathcal{L}(V, W)$ (some inner product space $W$).
4. $T = R^2$ for some self-adjoint $R \in \mathcal{L}(V)$.
5. $T$ has a (unique) positive square root: there is a unique positive operator $\sqrt{T}$ with $(\sqrt{T})^2 = T$.

Over $\mathbb{C}$, the self-adjointness in the definition is automatic from $\langle Tv, v \rangle \geq 0$ (use polarisation: $\langle Tv, v \rangle \in \mathbb{R}$ for all $v$ forces $T = T^*$ over $\mathbb{C}$). Over $\mathbb{R}$ the self-adjointness must be assumed.

For positive definite operators, replace (2) with "only positive eigenvalues" and (3) with "$S$ injective".

---

# Categorical / Structural Definition

The set of positive operators on $V$ forms a **convex cone** in $\mathcal{L}(V)$: it is closed under non-negative real linear combinations, and contains $0$ as its apex. The interior of the cone (in the appropriate topology) is the set of positive definite operators.

In the language of **ordered vector spaces**, positivity defines a partial order on the self-adjoint part of $\mathcal{L}(V)$ by $T \geq S \iff T - S$ is positive. This order has the following properties: it is compatible with addition ($T \geq S$ implies $T + R \geq S + R$); it is compatible with non-negative scalar multiplication; and it satisfies the **Loewner order** properties — most importantly, $0 \leq T \leq S$ does *not* imply $T^2 \leq S^2$ (Loewner monotonicity fails for the square function), which is one of the deepest results in operator theory.

In **operator algebra theory**, the positive cone is the defining ingredient of the **partial order** on a $C^*$-algebra, and the existence of a unique positive square root is part of the abstract characterisation of $C^*$-algebras. The categorical content of the positive cone is encoded in the fact that morphisms of $C^*$-algebras preserve positivity: if $\varphi : A \to B$ is a $*$-homomorphism, then $a \geq 0$ implies $\varphi(a) \geq 0$.

---

# Relate to Other Fields / Compression

A **bilinear/sesquilinear form** $b : V \times V \to \mathbb{F}$ on a finite-dimensional vector space (without an a priori inner product) is **positive definite** if $b(v, v) > 0$ for all $v \neq 0$; if also $b(v, w) = \overline{b(w, v)}$ (Hermitian symmetry), then $b$ *is* an inner product. So inner products are positive definite Hermitian forms. The "matrix of a Hermitian form in a basis" is positive definite as a matrix exactly when the form is positive definite as a form. **A choice of inner product on $V$ is a choice of positive definite self-adjoint operator on $V$** (viewing the inner product as a sesquilinear pairing represented by a matrix).

In **statistics**, the **covariance matrix** of a random vector is always positive (semi-definite if degenerate, definite if non-degenerate). The Cholesky factorisation of the covariance — its decomposition as $L L^*$ — is the standard way to compute multivariate Gaussian samples from independent univariate Gaussians (multiply by $L$).

In **optimisation**, **convex quadratic functions** $f(x) = \tfrac{1}{2} x^t A x + b^t x + c$ are convex if and only if $A \geq 0$, and strictly convex if and only if $A > 0$. The Hessian of a smooth function is positive definite at a point if and only if the point is a local minimum (with non-degenerate Hessian).

In **physics and probability**, **density matrices** in quantum mechanics are positive operators with trace $1$. The positivity ensures the probabilities of measurement outcomes are non-negative; the trace constraint ensures they sum to $1$.

**True name:** The most operational characterisation of a positive operator is **"$T = S^* S$ for some $S$"**. This is the definition-by-construction: any norm-squared-style operator is positive, and every positive operator arises this way. When checking that a given operator is positive, exhibiting it as $S^* S$ is often the slickest method. When applying positivity, the form $T = S^* S$ lets you express $\langle Tv, v \rangle$ as $\|Sv\|^2$, immediately giving non-negativity. This is also the right characterisation for $|T| = \sqrt{T^* T}$, the absolute value of an arbitrary operator: $T^* T$ is positive because it is of the form "something* times something".

---

# Examples / Corollaries

Most basic examples: the zero operator (positive but not positive definite), the identity (positive definite), $\alpha I$ for $\alpha \geq 0$ (positive; positive definite iff $\alpha > 0$).

Orthogonal projections are positive — $P_U^* P_U = P_U^2 = P_U$, so $\langle P_U v, v \rangle = \langle P_U^2 v, v \rangle = \langle P_U v, P_U v \rangle = \|P_U v\|^2 \geq 0$. Eigenvalues: $0$ and $1$.

The matrix $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ over $\mathbb{R}$ is positive definite. Check: self-adjoint, eigenvalues $1$ and $3$, both positive. Equivalently, $\langle Tv, v \rangle = 2 v_1^2 + 2 v_1 v_2 + 2 v_2^2 = v_1^2 + (v_1 + v_2)^2 + v_2^2 > 0$ for $v \neq 0$.

The matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ is self-adjoint but *not* positive — eigenvalues $-1$ and $3$. The quadratic form $v_1^2 + 4 v_1 v_2 + v_2^2$ is negative for, e.g., $v = (1, -1)$.

A canonical family: for any linear map $S \in \mathcal{L}(V, W)$, the operator $S^* S \in \mathcal{L}(V)$ is positive. Indeed $\langle S^* S v, v \rangle = \langle Sv, Sv \rangle = \|Sv\|^2 \geq 0$, and self-adjointness comes from $(S^* S)^* = S^* S^{**} = S^* S$. This is the **fundamental construction** that produces every positive operator — and the basis of singular value decomposition. The operator $S^* S$ is positive definite if and only if $S$ is injective (its kernel is zero).

Another canonical family: covariance matrices. For a random vector $X \in \mathbb{R}^n$ with finite second moments, the covariance matrix $\Sigma = E[(X - \mu)(X - \mu)^t]$ is positive (semi)definite. It is positive definite iff no linear combination of components is constant.

A non-example: a matrix with non-real entries on the diagonal cannot be positive — for $v = e_j$, $\langle Tv, v \rangle = T_{jj}$ would be a diagonal entry, which must be real and non-negative. Diagonal entries of positive matrices are non-negative reals. (For positive definite, strictly positive reals.)

Another non-example: a matrix with $|T_{ij}|^2 > T_{ii} T_{jj}$ for some $i \neq j$ cannot be positive. This is the **principal minor criterion**: a self-adjoint matrix is positive (semi)definite iff every principal minor is non-negative (positive). Equivalently, by **Sylvester's criterion**, a self-adjoint matrix is positive definite iff every leading principal minor is positive.

A corollary: if $T \geq 0$ and $T \leq 0$, then $T = 0$. (If both $\langle Tv, v \rangle \geq 0$ and $\leq 0$ for all $v$, then $\langle Tv, v \rangle = 0$ for all $v$; for self-adjoint $T$, this forces $T = 0$ via polarisation.)

Another corollary: $T \geq 0$ iff every eigenvalue is $\geq 0$. (Use the spectral theorem.)

A subtle observation: $T \geq 0$ does *not* imply $T^k \geq 0$ for arbitrary real $k$, but it does for integer $k \geq 0$ (use the spectral decomposition $T = \sum \lambda_j P_j$ with $\lambda_j \geq 0$, then $T^k = \sum \lambda_j^k P_j$ with $\lambda_j^k \geq 0$). For $T > 0$ (positive definite), $T^{-1} > 0$ as well. The square root extends this to half-integer powers, and the functional calculus extends to arbitrary continuous functions.

**Calibration check.** Verify these three calibrations:
1. The matrix $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ is positive but not positive definite. (Eigenvalues $0$ and $2$. Equivalently it equals $\begin{pmatrix} 1 \\ 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \end{pmatrix}$, of the form $S^*S$ but with $S$ a $1 \times 2$ rank-$1$ matrix.)
2. For $T \in \mathcal{L}(V)$, the operator $T + T^*$ is self-adjoint and the operator $T T^*$ is positive. (For self-adjointness of $T + T^*$: $(T + T^*)^* = T^* + T = T + T^*$. For positivity of $TT^*$: it has the form $SS^*$ where $S = T$, so positive; explicitly $\langle TT^* v, v \rangle = \langle T^* v, T^* v \rangle = \|T^* v\|^2 \geq 0$.)
3. The Cauchy–Schwarz inequality for an inner product is the positivity statement $\det \begin{pmatrix} \|v\|^2 & \langle v, w \rangle \\ \langle w, v \rangle & \|w\|^2 \end{pmatrix} \geq 0$, equivalent to $|\langle v, w \rangle|^2 \leq \|v\|^2 \|w\|^2$. (The matrix is the Gram matrix of $v$ and $w$, which is always positive.)

If these check out, the definition is in your hands.

---

# Unlocked by This

> [!tip] Positive Semidefinite Programming *(from Optimization)*
> The cone of positive semidefinite matrices is **closed and convex**; optimisation problems with affine constraints and PSD feasibility are called **semidefinite programs** (SDPs). The general form is: minimise $\langle C, X \rangle$ subject to $\langle A_i, X \rangle = b_i$ and $X \geq 0$, where $X$ is a symmetric matrix. SDPs generalise linear programs (the LP cone is the non-negative orthant) and contain a vast range of problems: max-cut relaxations, sum-of-squares optimisation, control-theoretic Lyapunov conditions, and quantum information optimisation. The **interior-point methods** for SDP run in polynomial time, making them tractable for medium-scale instances. The geometry of the PSD cone — its boundary corresponds to rank-deficient matrices, and the rank stratification is highly non-trivial — is the source of both the power and the difficulty of SDP.

> [!tip] Multivariate Gaussian Distribution *(from Probability)*
> A multivariate Gaussian random vector $X \in \mathbb{R}^n$ is characterised by a mean $\mu \in \mathbb{R}^n$ and a positive definite covariance matrix $\Sigma$. The density is $p(x) = \frac{1}{(2\pi)^{n/2} (\det \Sigma)^{1/2}} \exp(-\tfrac{1}{2}(x - \mu)^t \Sigma^{-1} (x - \mu))$. The positive definiteness of $\Sigma$ is what makes this density integrable (the quadratic form in the exponent is bounded below by a positive multiple of $\|x - \mu\|^2$) and makes the determinant $\det \Sigma > 0$ so the normalisation is well-defined. Sampling from $\mathcal{N}(\mu, \Sigma)$ uses the **Cholesky decomposition** $\Sigma = L L^t$: if $Z \sim \mathcal{N}(0, I)$, then $X = \mu + L Z \sim \mathcal{N}(\mu, \Sigma)$. The positive square root $\Sigma^{1/2}$ would also work and gives the "principal square root" parameterisation. All of multivariate statistics is, at heart, the spectral theory of positive operators.

> [!tip] Kernel Methods and Mercer's Theorem *(from Machine Learning)*
> A **positive definite kernel** $K : X \times X \to \mathbb{R}$ is a symmetric function such that the Gram matrix $(K(x_i, x_j))_{ij}$ is positive semidefinite for every finite set $\{x_1, \ldots, x_n\} \subseteq X$. **Mercer's theorem** then states that $K$ has an integral representation $K(x, y) = \sum_j \lambda_j \phi_j(x) \phi_j(y)$ with $\lambda_j \geq 0$ — the eigendecomposition of a positive operator, transported to function spaces. The reproducing-kernel Hilbert space (RKHS) construction associates to every positive definite kernel a Hilbert space of functions on $X$; the kernel trick of support vector machines is, at root, the observation that positive definite kernels let you do inner product calculations in a high-dimensional feature space without ever computing the feature embeddings explicitly.
