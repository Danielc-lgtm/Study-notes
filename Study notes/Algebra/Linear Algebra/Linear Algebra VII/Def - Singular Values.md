---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Positive Operator"
  - "Def - Adjoint of a Linear Map"
  - "Def - Self-Adjoint Operator"
  - "Def - Inner Product Space"
tags: [algebra, linear-algebra]
---

# Notation

$V$ and $W$ are finite-dimensional [[Def - Inner Product Space|inner product spaces]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$ with $\dim V = n$, $\dim W = m$. For $T \in \mathcal{L}(V, W)$, the [[Def - Adjoint of a Linear Map|adjoint]] $T^* \in \mathcal{L}(W, V)$ is the unique linear map with $\langle Tv, w \rangle_W = \langle v, T^* w \rangle_V$. The operator $T^* T \in \mathcal{L}(V)$ is [[Def - Positive Operator|positive]], so it has a unique positive square root $\sqrt{T^* T} = |T| \in \mathcal{L}(V)$ — the **absolute value** of $T$. The singular values of $T$ are denoted $s_1(T) \geq s_2(T) \geq \cdots \geq s_n(T) \geq 0$, also written $\sigma_j(T)$. The unit ball of $V$ is $B = B_V = \{v \in V : \|v\| \leq 1\}$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

---

# Axiom Motivation

A linear map $T : V \to W$ stretches some directions more than others. The right way to quantify this stretching is to track the **principal axes** of the image of the unit ball. The unit ball $B_V$ is a perfectly symmetric "round" object — a sphere — and its image $T(B_V)$ in $W$ is generically an ellipsoid (possibly degenerate). The singular values are the **semi-axis lengths** of this image ellipsoid, listed in decreasing order. They are the intrinsic, basis-free measure of how much $T$ stretches its inputs.

This geometric picture is the right one to keep in mind, and it makes a lot of the theory transparent. The number of nonzero singular values equals the rank of $T$ (the dimension of $T(V)$). The largest singular value $s_1(T)$ equals the **operator norm** $\|T\|_{\text{op}}$ — the maximum stretching factor. The smallest nonzero singular value $s_r(T)$ (where $r = \operatorname{rank} T$) measures the *worst-case-best* stretching, the "least possible" amount of expansion on the directions $T$ does not collapse. The product of all the nonzero singular values is the **absolute value of the determinant** (when $T$ is square): $|\det T| = \prod_j s_j(T)$ — the volume-distortion factor.

Why is the right definition to take square roots of eigenvalues of $T^* T$? Because $T^* T$ is the right object to extract stretching information from. The operator $T^* T$ is self-adjoint and positive ([[Def - Positive Operator|positivity]] of $T^* T$: $\langle T^*T v, v \rangle = \langle Tv, Tv \rangle = \|Tv\|^2 \geq 0$), so the spectral theorem gives it an orthonormal eigenbasis with non-negative eigenvalues. In this eigenbasis, the orthonormal eigenvectors $e_j$ of $T^* T$ map to vectors $T e_j$ whose squared norms are exactly $\langle T^* T e_j, e_j \rangle = \lambda_j$ (the eigenvalues of $T^*T$). So the eigenvectors of $T^* T$ are the *right singular vectors* of $T$ — the directions in $V$ that get sent to the principal axes — and the eigenvalues of $T^* T$ are the *squares of the singular values* of $T$.

What if you tried to define singular values as eigenvalues of $T$ directly? Two problems: first, $T$ might not be square, so it has no eigenvalues; second, even when $T$ is square, the eigenvalues of $T$ are in $\mathbb{F}$ (possibly complex) and can have arbitrary modulus, while singular values are always non-negative real. For *normal* operators, the singular values are the absolute values of the eigenvalues; for general operators, the two sequences can diverge dramatically. The matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has all eigenvalues $0$ (so eigenvalue-style sizing would call it the zero operator) but singular values $1$ and $0$ (so the SVD-style sizing correctly registers its nonzero action). Using $T^* T$ instead of $T$ is the precise fix.

What if you tried to use $T T^*$ instead of $T^* T$? Both are positive operators, and they have the **same nonzero eigenvalues** (with the same multiplicities). The eigenvalues of $T T^*$ also give the singular values of $T$; the difference is that $T T^*$ acts on $W$ rather than $V$, and its eigenvectors are the *left singular vectors* — the principal axes of the image ellipsoid in $W$, rather than their preimages in $V$. For the singular values, either definition is equivalent; for the SVD, both eigenbases play a role.

The square root step — taking $s_j = \sqrt{\lambda_j(T^*T)}$ rather than just using the eigenvalues directly — is justified by what one wants the singular values to *be*. The largest singular value should equal the operator norm, the maximum of $\|Tv\|/\|v\|$. The maximum of $\|Tv\|^2/\|v\|^2$ is the largest eigenvalue of $T^* T$. Taking the square root converts "norm squared" to "norm", which is the geometrically meaningful quantity (lengths, not their squares). The convention of taking the non-negative square root forces uniqueness.

The decreasing order convention is universal: $s_1 \geq s_2 \geq \cdots \geq s_n \geq 0$. The reason is that "the first $k$ singular values" then refers to the *largest* $k$ — the ones encoding the dominant stretching directions, the ones that survive after rank-$k$ truncation, and the ones that PCA selects as principal components.

---

# The Definition

Let $T \in \mathcal{L}(V, W)$. The **singular values** of $T$ are the non-negative square roots of the eigenvalues of the positive operator $T^* T \in \mathcal{L}(V)$, listed with multiplicity in decreasing order:

$$s_1(T) \geq s_2(T) \geq \cdots \geq s_n(T) \geq 0, \qquad s_j(T) = \sqrt{\lambda_j(T^* T)},$$

where $\lambda_j(T^* T)$ are the eigenvalues of $T^* T$ listed in decreasing order.

Equivalently, the singular values of $T$ are the eigenvalues (with multiplicity) of the **absolute value operator**

$$|T| = \sqrt{T^* T} \in \mathcal{L}(V),$$

which is itself a positive operator.

**Equivalent characterisations.**
1. $s_j(T) = \sqrt{\lambda_j(T^* T)}$, the non-negative square roots of eigenvalues of $T^* T$.
2. $s_j(T) = \lambda_j(|T|)$, the eigenvalues of $|T| = \sqrt{T^* T}$.
3. $s_j(T) = \lambda_j(\sqrt{T T^*}) = \sqrt{\lambda_j(T T^*)}$ — the nonzero singular values can equally be extracted from $T T^*$.
4. **Geometric.** $s_j(T)$ is the length of the $j$-th principal semi-axis of the ellipsoid $T(B_V)$.
5. **Min-max (Courant–Fischer).** $s_j(T) = \min_{\dim U = n - j + 1} \max_{v \in U, \|v\| = 1} \|T v\|$.

The number of *nonzero* singular values equals $\operatorname{rank} T$. The full vector of singular values (length $\min(n, m)$) characterises $T$ up to unitary equivalence on source and target — that is, $T_1$ and $T_2$ have the same singular values if and only if there are unitaries $U$ and $V$ with $T_2 = U T_1 V^*$.

---

# Categorical / Structural Definition

The singular values of $T$ are the **diagonal entries of the diagonal matrix in the singular value decomposition** $T = U \Sigma V^*$, where $U$ and $V$ are unitary and $\Sigma$ is diagonal with non-negative entries in decreasing order. The existence of this decomposition is the [[Thm - Singular Value Decomposition|singular value decomposition theorem]], the central result of §7E.

Equivalently, the singular values are the **eigenvalues of $|T| = \sqrt{T^*T}$**, where the absolute value is defined by spectral functional calculus. The singular values are invariant under unitary transformations on either side: for $U \in U(W)$ and $V \in U(V)$, the map $UTV^*$ has the same singular values as $T$.

The map $T \mapsto (s_1(T), \ldots, s_n(T))$ is a continuous map $\mathcal{L}(V, W) \to \mathbb{R}^n_{\geq 0}$ that is **invariant under the double unitary action** $T \mapsto U T V^*$. It is, in the language of representation theory, a complete invariant of the orbit of $T$ under this action.

---

# Relate to Other Fields / Compression

In **statistics and machine learning**, singular values are the **standard deviations along principal axes** in PCA. Given a data matrix $X$ (with centred columns), the columns of $V$ in the SVD $X = U \Sigma V^*$ are the principal components, and the singular values $s_j$ (rescaled by $\sqrt{n - 1}$) are the standard deviations of the data along each principal component. Equivalently, $s_j^2/(n - 1)$ are the eigenvalues of the sample covariance.

In **numerical linear algebra**, singular values are the **condition number quantifier**: the **condition number** $\kappa(T) = s_1(T)/s_n(T)$ (ratio of largest to smallest nonzero singular value) measures how much a linear system $Tx = b$ amplifies relative errors. A large condition number means the system is **ill-conditioned**, and small perturbations in $b$ can produce large changes in $x$.

In **signal processing and image compression**, singular values measure **how much information** is concentrated in each principal mode. Image compression by truncated SVD discards small singular values (and their corresponding modes) to reduce storage, and the visual quality of the reconstruction depends on how rapidly the singular values decay.

In **operator theory and functional analysis**, the **Schatten $p$-norm** $\|T\|_p = (\sum_j s_j(T)^p)^{1/p}$ generalises the operator norm ($p = \infty$, the largest singular value), the trace norm ($p = 1$, the sum), and the Hilbert–Schmidt norm ($p = 2$, the $\ell^2$ norm). These norms make precise sense of "$T$ is a small operator" in various senses.

**True name:** The singular values are the **principal-axis lengths of $T(B_V)$** — the geometry of the unit ball under the action of $T$. The eigenvalue-of-$T^*T$ characterisation is the computational definition; the principal-axis-length characterisation is the geometric one. Both are essential: one is how you compute, the other is how you visualise.

---

# Examples / Corollaries

For a diagonal matrix $T = \operatorname{diag}(d_1, \ldots, d_n)$ over $\mathbb{C}$, $T^* T = \operatorname{diag}(|d_1|^2, \ldots, |d_n|^2)$, so the singular values are $|d_1|, \ldots, |d_n|$ — the absolute values of the diagonal entries, rearranged in decreasing order. The unit ball $\{|z| \leq 1\}^n$ maps to the box $\{|d_j z_j| \leq 1\}$, which is a (degenerate-axis-aligned) ellipsoid with semi-axes $|d_j|$.

For the nilpotent matrix $T = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $T^* T = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$, eigenvalues $\{0, 1\}$, so singular values are $\{1, 0\}$. (Eigenvalues of $T$ itself are both $0$.) Geometrically, $T$ collapses the $y$-axis to $0$ and stretches the $x$-axis to length $1$ — but maps it to the $y$-direction in the image (so $T$ both rotates and degenerates).

For a rotation matrix $R_\theta \in O(2)$: $R_\theta^t R_\theta = I$, so $T^* T = I$, eigenvalues $\{1, 1\}$, so both singular values are $1$. A rotation does not stretch the unit ball at all — it maps the unit ball to the unit ball — and so both singular values are $1$. Same for any [[Def - Unitary Operator|unitary]]/orthogonal operator: all singular values are $1$.

For a projection matrix $P_U$ (orthogonal projection onto $U$): $P_U^* P_U = P_U^2 = P_U$, eigenvalues $\{1, \ldots, 1, 0, \ldots, 0\}$ ($\dim U$ ones and $\dim U^\perp$ zeros), so singular values are $\{1, \ldots, 1, 0, \ldots, 0\}$. The unit ball is mapped to the unit ball in $U$ (a disk of dimension $\dim U$), which has $\dim U$ semi-axes of length $1$ and $\dim U^\perp$ semi-axes of length $0$.

For a $2 \times 3$ rectangular matrix $T : \mathbb{R}^3 \to \mathbb{R}^2$: $T$ has at most $\min(2, 3) = 2$ singular values. The unit ball in $\mathbb{R}^3$ maps to a 2D ellipse in $\mathbb{R}^2$ (the image is at most 2-dimensional), and the two singular values are the semi-axes of this ellipse. Specifically for $T = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$, $T^* T = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$, eigenvalues $\{1, 1, 0\}$, so singular values are $\{1, 1\}$ (or $\{1, 1, 0\}$ depending on convention — sometimes the trailing zeros are dropped). The geometric picture: projection to the first two coordinates, the unit ball in $\mathbb{R}^3$ projects to the unit disk in $\mathbb{R}^2$.

A non-example: the eigenvalues of $T = \begin{pmatrix} 1 & 100 \\ 0 & 1 \end{pmatrix}$ are both $1$ (so eigenvalue-based sizing would give "$T$ is close to the identity"). But the singular values are large: $T^* T = \begin{pmatrix} 1 & 100 \\ 100 & 10001 \end{pmatrix}$, with eigenvalues approximately $\{10001.01, 0.0001\}$, so singular values approximately $\{100.005, 0.0099\}$. The condition number is approximately $10^4$, very ill-conditioned. This dramatic difference between eigenvalues and singular values for non-normal operators is the central motivation for SVD: eigenvalues miss the relevant scaling information for non-normal $T$.

A corollary: **singular values equal absolute values of eigenvalues for normal operators.** If $T$ is normal with $T = \sum \lambda_j P_j$, then $T^* T = \sum |\lambda_j|^2 P_j$, eigenvalues $\{|\lambda_j|^2\}$, so $s_j(T) = |\lambda_j(T)|$. For normal $T$, "eigenvalue absolute value" and "singular value" coincide. For non-normal $T$, they generally do not.

Another corollary: **$\|T\|_{\text{op}} = s_1(T)$**. The operator norm is the largest singular value (see [[Ex - SVD computes the operator norm]]).

Another corollary: **$\|T\|_F^2 = \sum_j s_j^2(T)$**, the Frobenius norm squared equals the sum of squared singular values. (Use $\|T\|_F^2 = \operatorname{tr}(T^* T) = \sum \lambda_j(T^* T) = \sum s_j(T)^2$.)

A subtle calculation: **$|\det T| = \prod_j s_j(T)$** for square $T$. (Use $|\det T|^2 = \det(T^* T) = \prod_j \lambda_j(T^* T) = \prod_j s_j(T)^2$, then square-root.) The product of singular values is the volume distortion factor; the eigenvalues, in contrast, can have arbitrary moduli.

**Calibration check.** Verify these three facts:
1. The matrix $T = \begin{pmatrix} 3 & 0 \\ 0 & 4 \end{pmatrix}$ has singular values $\{4, 3\}$ (largest first), corresponding to the unit disk mapping to an ellipse with semi-axes $3$ and $4$.
2. The matrix $T = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has singular values $\{1, 1\}$. (It is a reflection, which is unitary, hence all singular values are $1$.)
3. The matrix $T = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ has singular values $\{\sqrt{2}, 0\}$. (Compute $T^* T = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, eigenvalues $\{2, 0\}$, square roots $\{\sqrt{2}, 0\}$.)

If these check out, the definition is in your hands.

---

# Unlocked by This

> [!tip] Principal Component Analysis *(from Statistics)*
> Given an $n \times p$ data matrix $X$ with mean-centred columns, the **principal components** of the data are the columns of $V$ in the SVD $X = U \Sigma V^*$. The singular values $s_j$ (rescaled) are the standard deviations of the data along each principal component, and the squared singular values $s_j^2$ are proportional to the variances. **PCA truncation** keeps the principal components corresponding to the top $k$ singular values, discarding the rest; the Eckart–Young theorem guarantees this is the best rank-$k$ approximation of $X$ in the Frobenius norm. Singular values are the "explanatory power" of each principal component, and their decay rate is the quantitative measure of the data's intrinsic dimensionality.

> [!tip] Schatten Norms and Trace-Class Operators *(from Functional Analysis)*
> For an operator $T$ on a Hilbert space, the **Schatten $p$-norm** is $\|T\|_p = (\sum_j s_j(T)^p)^{1/p}$. The case $p = \infty$ recovers the operator norm $\|T\|_{\text{op}}$ (only the largest singular value matters), $p = 2$ gives the **Hilbert–Schmidt norm** (the $\ell^2$ norm of the singular value vector), and $p = 1$ gives the **trace norm** (the sum of singular values). Operators with $\|T\|_1 < \infty$ are called **trace-class operators**; they form a two-sided ideal in $\mathcal{L}(H)$, and the trace functional $T \mapsto \operatorname{tr}(T) = \sum \lambda_j$ (sum of eigenvalues) is well-defined on this class. The Schatten norms are the operator-theoretic analogue of the $\ell^p$ norms on sequence spaces — and the relations $\|T\|_p$ decreasing in $p$, embedding properties, duality $\ell^p \cong (\ell^{p'})^*$, all transfer to Schatten norms.

> [!tip] Condition Number and Numerical Stability *(from Numerical Linear Algebra)*
> The **condition number** of an invertible linear map $T$ is $\kappa(T) = s_1(T) / s_n(T)$, the ratio of largest to smallest singular value. For solving the linear system $Tx = b$, the condition number bounds the relative error amplification: $\|\delta x\| / \|x\| \leq \kappa(T) \cdot \|\delta b\| / \|b\|$ (to first order). A matrix is **well-conditioned** if $\kappa$ is small (close to $1$), **ill-conditioned** if $\kappa$ is large. The Hilbert matrix $H_n$ with $H_{ij} = 1/(i + j - 1)$ has condition number growing as $e^{3.5n}$, making large Hilbert matrices catastrophically ill-conditioned. Direct inversion of an ill-conditioned matrix loses approximately $\log_{10}(\kappa)$ digits of precision; QR factorisation and SVD are the standard ways to avoid this loss.
