---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Positive Operator"
  - "Thm - QR Factorization"
  - "Thm - Positive Operators Have a Unique Square Root"
tags: [algebra, linear-algebra]
---

# Notation

$\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$. A matrix $T \in \mathbb{F}^{n \times n}$ is **positive definite** (PD) if it is self-adjoint and $\langle Tv, v \rangle > 0$ for all $v \neq 0$ (see [[Def - Positive Operator]]). Equivalently, $T$ is PD iff $T = R^* R$ for some invertible matrix $R$. A matrix is **upper-triangular** if entries below the main diagonal are zero, **lower-triangular** if entries above are zero. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

---

# Statement

> **Theorem (Cholesky Factorisation).** Let $T \in \mathbb{F}^{n \times n}$ be a [[Def - Positive Operator|positive definite]] matrix. Then $T$ factors uniquely as
> $$T = R^* R,$$
> where $R \in \mathbb{F}^{n \times n}$ is upper-triangular with strictly positive real diagonal entries.
>
> Equivalently, $T = L L^*$ where $L = R^*$ is lower-triangular with strictly positive real diagonal entries.

> [!warning] Two conventions: $T = R^* R$ (upper) vs $T = L L^*$ (lower).
> The two conventions are equivalent (set $L = R^*$). Numerical analysis textbooks often use the lower-triangular form $T = L L^*$; pure mathematics texts often use the upper-triangular form. The factor is unique given the convention.

---

# Motivation

The Cholesky factorisation is the **unique** triangular factorisation of a positive definite matrix. While LU decomposition $T = LU$ exists for any invertible $T$ (with appropriate pivoting), the Cholesky factorisation specifically exploits the positivity and self-adjointness of $T$ to produce a *symmetric* triangular factorisation: $T = R^* R$ instead of two separate triangular factors $L$ and $U$.

The motivation is computational. Solving the linear system $Tx = b$ for $T$ positive definite:
- **LU approach**: factor $T = LU$ (in general, $L$ and $U$ are independent). Solve $L y = b$, then $U x = y$. Two back-substitutions, each linear in $n^2$ operations.
- **Cholesky approach**: factor $T = R^* R$. Solve $R^* y = b$, then $R x = y$. Two back-substitutions, each linear in $n^2$ operations — but with *half* the storage (one triangular matrix instead of two) and *half* the work (the Cholesky algorithm computes about $n^3/6$ operations, vs $n^3/3$ for LU).

For positive definite systems, Cholesky is the standard algorithm: more efficient than LU, and numerically stable (no need for pivoting, because positive-definite-ness rules out the pivot failures that LU can encounter).

Cholesky is also the operator analogue of "extracting a square root" of a positive matrix — but with an upper-triangular factor instead of a self-adjoint one. The positive square root $\sqrt T$ (from [[Thm - Positive Operators Have a Unique Square Root]]) is self-adjoint with $(\sqrt T)^2 = T$; the Cholesky factor $R$ is upper-triangular with $R^* R = T$. They are different factorisations of the same positive operator.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$T$ is positive definite". Various ways this arises in practice:

The first disguised source is **a covariance matrix in statistics**. By construction, covariance matrices are positive semidefinite; positive definite if the random vector has non-degenerate components. The Cholesky factor $L$ of the covariance $\Sigma = L L^*$ is the **multivariate Gaussian sampling matrix**: if $Z \sim \mathcal{N}(0, I)$, then $X = LZ \sim \mathcal{N}(0, \Sigma)$. This is the standard way to sample from multivariate Gaussians.

The second disguised source is **a Gram matrix from a list of vectors**. The Gram matrix $G_{ij} = \langle v_i, v_j \rangle$ for linearly independent $v_i$ is positive definite. The Cholesky factor $R$ has rows that, when interpreted appropriately, encode the geometry of the original vectors.

The third disguised source is **a Hessian at a strict local minimum**. The Hessian of a smooth function $f$ at a strict local minimum is positive definite. Cholesky of the Hessian gives a "preconditioner" that accelerates the convergence of optimisation algorithms (the conjugate gradient method, Newton's method).

**Targets (Output Amplification)**

The conclusion is the unique factorisation $T = R^* R$.

Combine with **solving linear systems**: $Tx = b$ becomes $R^* R x = b$. Solve $R^* y = b$ by forward substitution (since $R^*$ is lower-triangular), then $R x = y$ by back substitution. Two triangular solves, total $O(n^2)$ operations.

Combine with **computing the determinant**: $\det T = \det R^* \cdot \det R = |\det R|^2 = \prod_j |R_{jj}|^2$. Since $R_{jj}$ are positive real, $\det T = \prod R_{jj}^2$. The determinant is *automatic* once Cholesky is computed.

Combine with **the connection to QR**: $T = A^* A$ for some $A$ iff $T$ is positive (semi)definite. The QR factorisation $A = QR$ gives $A^* A = R^* Q^* Q R = R^* R$, i.e., the upper-triangular factor of QR of $A$ is the Cholesky factor of $A^*A$. Numerically, computing Cholesky of $A^*A$ by first computing QR of $A$ is more stable than directly computing $A^*A$ and then Cholesky.

---

# Why Is It True

The proof is by induction on $n$.

**The one-liner mechanism: write $T$ in block form with a positive scalar in the top-left; perform a rank-1 update on the bottom-right block, which remains positive definite (Schur complement); recursively Cholesky-factor the smaller block.**

**Base case $n = 1$:** $T = [t_{11}]$ with $t_{11} > 0$. Set $R = [\sqrt{t_{11}}]$. Then $R^* R = [t_{11}] = T$.

**Inductive step.** Write $T$ in block form:
$$T = \begin{pmatrix} t_{11} & u^* \\ u & T_{22} \end{pmatrix}$$
with $t_{11} > 0$ (positivity on $e_1$), $u \in \mathbb{F}^{n-1}$, and $T_{22} \in \mathbb{F}^{(n-1) \times (n-1)}$ self-adjoint.

Compute the **Schur complement** $S = T_{22} - \frac{u u^*}{t_{11}}$. The Schur complement is positive definite (key lemma: positivity is preserved under the Schur complement of a positive scalar leading entry). Apply the inductive hypothesis to get $S = R_{22}^* R_{22}$ for $R_{22}$ upper-triangular with positive diagonal.

Define
$$R = \begin{pmatrix} \sqrt{t_{11}} & u^* / \sqrt{t_{11}} \\ 0 & R_{22} \end{pmatrix}.$$
Verify $R^* R = T$ by block multiplication:
$$R^* R = \begin{pmatrix} \sqrt{t_{11}} & 0 \\ u/\sqrt{t_{11}} & R_{22}^* \end{pmatrix} \begin{pmatrix} \sqrt{t_{11}} & u^* / \sqrt{t_{11}} \\ 0 & R_{22} \end{pmatrix} = \begin{pmatrix} t_{11} & u^* \\ u & uu^*/t_{11} + R_{22}^* R_{22} \end{pmatrix} = \begin{pmatrix} t_{11} & u^* \\ u & uu^*/t_{11} + S \end{pmatrix} = T.$$
✓

The diagonal entries of $R$ are $\sqrt{t_{11}}$ and the diagonal entries of $R_{22}$ — all positive by the inductive hypothesis and the base case.

**Uniqueness** follows from the uniqueness of QR (since $T = A^*A$ for $A =$ some matrix, and the QR of $A$ gives $R$ uniquely with positive diagonal).

---

# What Makes This Hard

The non-obvious step is **the Schur complement is positive definite**. This is what makes the induction proceed; without it, the smaller block in the bottom-right could fail to satisfy the inductive hypothesis. The reason: the Schur complement formula corresponds to performing one step of Gaussian elimination on $T$, and Gaussian elimination preserves positivity.

The second subtlety is that **the algorithm is incremental, not direct**. Unlike the spectral square root $\sqrt T$ (which requires diagonalising $T$), the Cholesky factorisation can be computed by simple arithmetic operations on the entries of $T$ — no eigenvalue computations needed. This makes it dramatically faster than spectral methods for solving systems.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Induct on $n$. At each step, peel off the first row and column of $T$ by Schur complement; the remaining $(n-1) \times (n-1)$ block is positive definite by Schur complement positivity, and the inductive hypothesis applies.

**Subgoal decomposition:**

1. **Schur complement of positive definite block is positive definite.** Show that if $\begin{pmatrix} a & b^* \\ b & C \end{pmatrix}$ is PD with $a > 0$, then $C - \frac{bb^*}{a}$ is PD.

2. **Block triangular factorisation.** Build $R$ block by block: top row gets $\sqrt{a}$ and $b^*/\sqrt a$; bottom block is the Cholesky factor of the Schur complement.

3. **Verify $R^* R = T$ by block multiplication.**

4. **Uniqueness via QR factorisation of $T = A^*A$.** Or directly by comparing diagonals.

---

# Lemma Decomposition

> [!note]- Lemma 1: Schur complement of a positive definite matrix is positive definite
> **Statement:** Let $T = \begin{pmatrix} a & b^* \\ b & C \end{pmatrix}$ be positive definite with $a > 0$ and $C \in \mathbb{F}^{(n-1) \times (n-1)}$ self-adjoint. Then $C - bb^*/a$ is positive definite.
>
> **Hint:** Test the positivity condition on a vector of the form $(- b^* y / a, y)^t$ to find the right form, then check $\langle (C - bb^*/a) y, y \rangle > 0$ for $y \neq 0$.
>
> **Why needed:** This is the inductive step engine. The Schur complement is positive definite by the same reason as the original, propagating positivity to the smaller block.
>
> > [!note]- Full proof
> > For any $y \in \mathbb{F}^{n-1}$ with $y \neq 0$, set $v = (- b^* y / a, y)^t \in \mathbb{F}^n$. Compute:
> > $$\langle Tv, v \rangle = -b^*y/a \cdot \overline{-b^*y/a} \cdot a + (- b^*y/a)(b^* y) + (y^* b)(-b^*y/a) + y^* C y.$$
> >
> > Wait, let me recompute more carefully. With $v = (\alpha, y)$ where $\alpha = -b^*y/a$:
> > $$Tv = (a\alpha + b^*y, b\alpha + Cy) = (a \cdot (-b^*y/a) + b^*y, -b b^*y/a + Cy) = (0, Cy - bb^*y/a).$$
> >
> > Then $\langle Tv, v \rangle = 0 \cdot \overline{\alpha} + (Cy - bb^*y/a)^* y = (Cy - bb^*y/a, y) = \langle (C - bb^*/a) y, y \rangle$.
> >
> > By positivity of $T$ and $v \neq 0$ (since $y \neq 0$), $\langle Tv, v \rangle > 0$. So $\langle (C - bb^*/a) y, y \rangle > 0$ for all $y \neq 0$. Self-adjointness of $C - bb^*/a$ is direct ($C$ is self-adjoint and $bb^*$ is self-adjoint). Hence $C - bb^*/a$ is positive definite.

---

# Formal Proof

> [!note]- Complete formal proof
>
> Induct on $n = \dim$.
>
> **Base case $n = 1$.** $T = [t_{11}]$ is positive definite, so $t_{11} > 0$. Set $R = [\sqrt{t_{11}}]$. Then $R^*R = t_{11} = T$, and $R$ has positive real diagonal. Unique: if $T = R'^* R' = [r'^2]$ with $r' > 0$, then $r' = \sqrt{t_{11}}$.
>
> **Inductive step.** Assume the theorem for matrices of size $< n$. Write
> $$T = \begin{pmatrix} t_{11} & u^* \\ u & T_{22} \end{pmatrix}$$
> with $t_{11} \in \mathbb{R}_{>0}$ (positivity of $T$ on $e_1$), $u \in \mathbb{F}^{n-1}$, $T_{22} \in \mathbb{F}^{(n-1) \times (n-1)}$ self-adjoint. By Lemma 1, the Schur complement $S = T_{22} - u u^* / t_{11}$ is positive definite. By the inductive hypothesis, $S = R_{22}^* R_{22}$ for a unique upper-triangular $R_{22}$ with positive real diagonal.
>
> Define
> $$R = \begin{pmatrix} \sqrt{t_{11}} & u^* / \sqrt{t_{11}} \\ 0 & R_{22} \end{pmatrix}.$$
> $R$ is upper-triangular with positive real diagonal (entries $\sqrt{t_{11}}$ and the diagonal entries of $R_{22}$).
>
> Verify $R^* R = T$ by block multiplication:
> $$R^* R = \begin{pmatrix} \sqrt{t_{11}} & 0 \\ u/\sqrt{t_{11}} & R_{22}^* \end{pmatrix} \begin{pmatrix} \sqrt{t_{11}} & u^* / \sqrt{t_{11}} \\ 0 & R_{22} \end{pmatrix} = \begin{pmatrix} t_{11} & u^* \\ u & u u^*/t_{11} + R_{22}^* R_{22} \end{pmatrix}.$$
> The bottom-right is $uu^*/t_{11} + R_{22}^* R_{22} = uu^*/t_{11} + S = T_{22}$. So $R^*R = T$. ✓
>
> **Uniqueness.** Suppose $T = R^*R = R'^* R'$ with both factors upper-triangular and positive real diagonal. Both are full-rank (since $T$ is invertible). Apply [[Thm - QR Factorization|QR factorisation uniqueness]] to $A := R$ vs $A := R'$ — but more directly: $R'^{-1} R$ is upper-triangular (product of upper-triangulars) and satisfies $(R'^{-1} R)^* (R'^{-1} R) = R^* (R'^*)^{-1} R'^{-1} R = R^* (R'^* R')^{-1} R = R^* T^{-1} R = R^* (R^*R)^{-1} R = R^* R^{-1} (R^*)^{-1} R = I$. So $R'^{-1} R$ is an upper-triangular [[Def - Isometry|isometry]], hence diagonal with unit-modulus entries. With positive-diagonal constraint, $R'^{-1} R = I$, so $R = R'$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

1. **Bayesian inference — multivariate Gaussian likelihoods.** Computing the log-likelihood of a multivariate Gaussian $\mathcal{N}(\mu, \Sigma)$ requires $\log |\Sigma|$ and $(x - \mu)^t \Sigma^{-1} (x - \mu)$. With $\Sigma = L L^*$, $\log |\Sigma| = 2 \sum \log L_{jj}$ (immediate), and $\Sigma^{-1}(x - \mu)$ is computed by solving $L y = x - \mu$ then $L^* z = y$ (back-substitution). Cholesky is the standard primitive in MCMC, Hamiltonian Monte Carlo, and Gaussian process regression.

2. **Linear regression — fast normal equations.** To solve $A^*A \beta = A^* y$ for the least-squares coefficient $\beta$, with $A \in \mathbb{F}^{m \times n}$ full column rank: compute Cholesky $A^*A = L L^*$, then solve $L u = A^*y$ and $L^* \beta = u$. This is faster than QR factorisation when $m \gg n$, though somewhat less numerically stable.

3. **Quadratic programming — convex QP solvers.** Convex quadratic programming minimises $\frac{1}{2} x^* P x + q^* x$ subject to constraints, with $P$ positive definite. The KKT system involves $P$ and the constraint matrices; Cholesky of $P$ is a basic primitive that speeds up the iteration. Interior-point methods for QP rely heavily on Cholesky factorisation.

4. **Kalman filter — covariance updates.** The Kalman filter maintains a covariance matrix $\Sigma$ of state estimates and updates it after each observation. To prevent the covariance from becoming non-positive due to numerical error, one maintains the Cholesky factor $L$ directly (the **square-root Kalman filter**), updating $L$ in place. This is the standard implementation in inertial navigation, sensor fusion, and SLAM.

---

# Bridges

- **[[Thm - QR Factorization|QR factorisation]]** — QR of $A$ gives Cholesky of $A^*A$: if $A = QR$, then $A^* A = R^* Q^* Q R = R^* R$. Numerically, computing Cholesky of $A^*A$ by first computing QR of $A$ avoids forming $A^*A$ explicitly (which would square the condition number). The two factorisations are coupled: QR for general matrices, Cholesky for positive operators; their factors agree on $A^*A$.

- **[[Thm - Positive Operators Have a Unique Square Root]]** — The positive square root $\sqrt T$ and the Cholesky factor $R$ are two different "square roots" of a positive operator $T$. $\sqrt T$ is self-adjoint with $(\sqrt T)^2 = T$; $R$ is upper-triangular with $R^* R = T$. They differ structurally — one is self-adjoint, the other triangular — but both factor $T$ as a "square" in their respective senses.

- **Schur complement** — The proof of Cholesky factorisation rests on the positivity of the Schur complement. The Schur complement formula $T_{22} - u u^*/t_{11}$ for the bottom-right block also gives the inverse of $T$ in terms of blocks of $T$, and is central to the analysis of block matrices in optimisation and statistics.

- **LDLT decomposition** — A variant of Cholesky avoids the square root: $T = L D L^*$ with $L$ unit-lower-triangular and $D$ diagonal positive. Useful when working with rational arithmetic or when the square roots are problematic numerically. Equivalent to the standard Cholesky $T = (L \sqrt D)(L \sqrt D)^* = R^* R$.

---

# Unlocked by This

> [!tip] Square-Root Kalman Filtering *(from Control / Signal Processing)*
> Maintaining the covariance matrix $\Sigma$ in a Kalman filter via direct updates accumulates numerical errors that can make $\Sigma$ lose positive-definiteness over time, leading to instability. The **square-root Kalman filter** instead maintains the Cholesky factor $L$ of $\Sigma$, updating $L$ in place via Householder reflections or Givens rotations. This guarantees positive-definiteness is preserved (since $LL^*$ is automatically positive semidefinite for any $L$). The square-root Kalman filter is the standard implementation in inertial navigation systems, GPS receivers, robotic SLAM, and high-precision sensor fusion — applications where numerical robustness over hours of operation is critical.

> [!tip] Sequential Monte Carlo and Particle Filters *(from Bayesian Statistics)*
> In sequential Monte Carlo (particle filter) methods for Bayesian inference, samples are propagated through dynamical models and resampled based on likelihood weights. The likelihood evaluation for Gaussian-noise models requires computing $\exp(-\frac{1}{2} (x - \mu)^* \Sigma^{-1} (x - \mu))$, which is done via Cholesky $\Sigma = LL^*$: solve $Ly = x - \mu$, return $\exp(-\frac{1}{2} \|y\|^2)$. The Cholesky factor is computed once per time step and reused for thousands of particles, making it the dominant cost in many SMC implementations.

> [!tip] Conjugate Gradient Method with Preconditioning *(from Numerical Optimization)*
> The conjugate gradient method solves $Ax = b$ for positive definite $A$ iteratively, converging in $n$ steps in exact arithmetic and faster (in $\sqrt{\kappa(A)}$ steps) for clustered eigenvalue spectra. **Preconditioning** transforms the system to $M^{-1} A x = M^{-1} b$, where $M$ is a "preconditioner" close to $A$ but easy to invert. The **incomplete Cholesky** preconditioner $M = L L^*$ (with $L$ an approximate Cholesky factor) is one of the most widely used choices: it captures the dominant structure of $A$ while being cheap to invert. Combined with conjugate gradient, this gives the **preconditioned CG method**, the standard algorithm for large sparse positive definite linear systems arising in PDE discretisations.
