---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Least Squares Problem"
  - "Def - Orthogonal Projection"
tags: [algebra, linear-algebra, applied, optimization]
---

# Notation

Let $A$ be an $m \times n$ matrix and $b$ an $m$-vector. The *Gram matrix* of $A$ is $A^T A$, an $n \times n$ symmetric positive semidefinite matrix; it is positive definite (hence invertible) iff the columns of $A$ are linearly independent. The right-hand side of the normal equations is the $n$-vector $A^T b$. See the parent topic page [[Linear Algebra XI — Applied II — Least Squares]] for the full registry.

---

# Axiom Motivation

The normal equations are the *linear-algebraic statement of the orthogonality principle* — and equivalently, the *first-order optimality condition* for the least squares problem. They appear from two different derivations that arrive at the same equation.

*Derivation via calculus.* The LS objective $f(x) = \|Ax - b\|^2 = (Ax - b)^T (Ax - b)$ is a smooth function of $x$. At any minimizer $\hat{x}$, the gradient must vanish: $\nabla f(\hat{x}) = 0$. Expanding,
$$f(x) = x^T A^T A x - 2 b^T A x + b^T b,$$
the gradient is $\nabla f(x) = 2 A^T A x - 2 A^T b$. Setting this to zero gives $A^T A x = A^T b$ — the normal equations. The Hessian $\nabla^2 f = 2 A^T A$ is positive semidefinite; under linear independence of the columns of $A$ it is positive definite, so the critical point is a minimum and the objective is *strictly* convex with a unique minimizer.

*Derivation via the orthogonality principle.* For $\hat{x}$ to be the closest point in $\mathrm{col}(A)$ to $b$, the residual $r = A\hat{x} - b$ must be orthogonal to $\mathrm{col}(A)$ — orthogonal, that is, to every vector in the column space, equivalently to every column of $A$. The condition "$r$ is orthogonal to every column of $A$" is exactly $A^T r = 0$, which expands to $A^T(A\hat{x} - b) = 0$, i.e., $A^T A \hat{x} = A^T b$. The normal equations.

Why are both derivations natural? Because the LS problem has *two faces* — algebraic (minimize a quadratic) and geometric (project onto a subspace) — and the normal equations are the meeting point. The calculus derivation says "set the gradient to zero"; the geometric derivation says "the residual is orthogonal to the column space." These are the same equation because the gradient of $\|Ax - b\|^2$ *is* (up to a factor of 2) the projection of $Ax - b$ onto the column space — the first-order linear approximation of the objective in directions within the column space is exactly the inner product of the residual with those directions. Calculus and geometry are saying the same thing in different languages.

The name "normal equations" comes from the geometric derivation: the residual $r$ is *normal* (i.e., orthogonal) to the column space of $A$, hence the equations are the ones expressing that normality.

A subtle point: the normal equations are *necessary* for $\hat{x}$ to minimize the LS objective, but not in themselves *sufficient* without an additional regularity condition. If $A$ has linearly dependent columns, $A^T A$ is singular and the normal equations have infinitely many solutions, all of which give the same LS objective value — they pick out the *affine subspace* of LS minimizers, but do not give a unique answer. This is why the assumption "$A$ has linearly independent columns" enters: it upgrades the necessary condition to a sufficient one for a unique minimizer.

---

# The Definition

> **Definition (Normal Equations).** For the least squares problem $\min_x \|Ax - b\|^2$ with $m \times n$ matrix $A$ and $m$-vector $b$, the *normal equations* are the linear system
> $$A^T A \, x = A^T b.$$
> The matrix $A^T A$ is the *Gram matrix* of $A$. Any minimizer $\hat{x}$ of the LS objective satisfies the normal equations, and conversely, when $A$ has linearly independent columns, the normal equations have a unique solution which is the unique LS minimizer.

When the columns of $A$ are linearly independent, $A^T A$ is invertible (positive definite) and the explicit solution is
$$\hat{x} = (A^T A)^{-1} A^T b = A^\dagger b,$$
where $A^\dagger = (A^T A)^{-1} A^T$ is the (left) [[Def - Pseudoinverse|pseudoinverse]] of $A$.

---

# Categorical / Structural Definition

The normal equations express the operator-theoretic statement that the residual $r = A\hat{x} - b$ lies in the orthogonal complement of $\mathrm{col}(A)$. In the language of [[Linear Algebra VI — §6 Inner Product Spaces]], this is the *orthogonal-decomposition theorem*: any $b \in \mathbb{R}^m$ decomposes uniquely as $b = b_\parallel + b_\perp$ with $b_\parallel \in \mathrm{col}(A)$ and $b_\perp \in \mathrm{col}(A)^\perp$. The LS problem is asking for $\hat{x}$ such that $A\hat{x} = b_\parallel$; this requires $r = A\hat{x} - b = -b_\perp \in \mathrm{col}(A)^\perp = \ker A^T$.

The statement "$r \in \ker A^T$" — equivalently $A^T r = 0$ — *is* the normal equations. So the normal equations are the operator-theoretic shadow of $\mathrm{col}(A)^\perp = \ker A^T$, the fundamental adjoint identity for finite-dimensional inner product spaces. See [[Def - Orthogonal Complement]] and the adjoint relations in [[Linear Algebra VII — §7 Operators on Inner Product Spaces]].

---

# Relate to Other Fields / Compression

**True name:** the normal equations are the *projection equations* — they express that $A\hat{x}$ is the orthogonal projection of $b$ onto $\mathrm{col}(A)$ via the algebraic condition that the residual is orthogonal to the column space. They are the *adjoint statement* of optimality.

This is the same construction as:
- **Linear Regression** (statistics): the normal equations $X^T X \beta = X^T y$ are exactly the regression equations; statistical theory adds noise models and inference machinery on top.
- **Galerkin methods** (numerical analysis): in finite-element approximation of PDEs, the Galerkin equations $\langle A u_h, v_h \rangle = \langle f, v_h \rangle$ for all $v_h$ in a test space have the same form — they are the normal equations for projecting the PDE solution onto a finite-dimensional subspace.
- **Conditional expectation in $L^2$** (probability): when $X \in L^2$ and $\mathcal{F}$ is a sub-$\sigma$-algebra, the conditional expectation $\mathbb{E}[X | \mathcal{F}]$ is the orthogonal projection of $X$ onto the closed subspace $L^2(\mathcal{F}) \subseteq L^2$, characterized by the equation $\mathbb{E}[(X - \mathbb{E}[X|\mathcal{F}]) Z] = 0$ for all $\mathcal{F}$-measurable $Z$. This is the normal equation in an infinite-dimensional Hilbert space.

---

# Examples / Corollaries

*Example 1 (simplest case: $A = I$).* If $A$ is the identity and $b$ is given, the normal equations become $I x = b$, which has solution $x = b$ — the residual is zero. The Gram matrix is $I$ and the LS problem trivializes.

*Example 2 (one variable, multiple measurements).* Take $A = (1, 1, \ldots, 1)^T$ (an $m \times 1$ matrix) and $b = (b_1, \ldots, b_m)$. Then $A^T A = m$ and $A^T b = \sum_i b_i$. The normal equation is $m x = \sum_i b_i$, giving $\hat{x} = (1/m) \sum_i b_i$ — the *sample mean*. So least squares "fitting a constant" gives the mean as the optimal constant; this is the elementary fact that the sample mean minimizes the sum of squared deviations.

*Example 3 (rank-deficient case — is NOT uniquely solvable).* Take $A = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $b = (1, 0)$. Then $A^T A = 2$, $A^T b = 1$, and the normal equation $2 x = 1$ has unique solution $\hat{x} = 1/2$. But if we use the rank-deficient $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ from earlier, $A^T A = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$ is singular. The normal equations $A^T A x = A^T b = (1, 1)$ have the family of solutions $x_1 + x_2 = 1/2$ — every point on this line is an LS minimizer, and the normal equations *cannot* distinguish among them.

*Example 4 (consistency check via the orthogonality principle).* Compute $A^T(A\hat{x} - b)$ where $\hat{x} = (A^T A)^{-1} A^T b$. We get $A^T A (A^T A)^{-1} A^T b - A^T b = A^T b - A^T b = 0$. So the residual is orthogonal to every column of $A$ — the orthogonality principle holds, as expected.

*Example 5 (positive definiteness of $A^T A$).* For any vector $v$, $v^T A^T A v = (Av)^T (Av) = \|Av\|^2 \geq 0$. Equality holds iff $Av = 0$. So $A^T A$ is positive semidefinite, and positive definite iff $A v = 0 \Rightarrow v = 0$, i.e., iff $A$ has linearly independent columns. This is the formal verification that the linear-independence assumption is exactly what gives invertibility of the Gram matrix.

**Calibration check.** If you have understood the normal equations, you should be able to verify: (i) the residual at the LS solution is $r = A\hat{x} - b = A(A^T A)^{-1} A^T b - b = (P - I) b$ where $P = A(A^T A)^{-1} A^T$ is the projection onto $\mathrm{col}(A)$; (ii) $A^T r = 0$ holds by direct computation; (iii) the LS solution is a linear function of $b$, with the linear map being $A^\dagger = (A^T A)^{-1} A^T$.

---

# Unlocked by This

> [!tip] Galerkin Methods *(from Numerical Analysis of PDEs)*
> The normal equations have an infinite-dimensional analog: in **Galerkin methods** for elliptic PDEs, the finite-dimensional approximation $u_h$ to the PDE solution $u$ is defined by the equations $\langle A u_h, v_h \rangle = \langle f, v_h \rangle$ for all test functions $v_h$ in a finite-dimensional subspace $V_h$. When written in coordinates, these are the normal equations for projecting the PDE residual onto $V_h$. The conditioning challenges (the Gram matrix can be poorly conditioned) and the regularization strategies (preconditioning, multigrid) directly extend the finite-dimensional intuition.

> [!tip] Conditional Expectation as Orthogonal Projection *(from Probability)*
> In $L^2$, conditional expectation $\mathbb{E}[X | \mathcal{F}]$ is the orthogonal projection of $X$ onto $L^2(\mathcal{F})$. This projection is characterized by the equation $\mathbb{E}[(X - Y) Z] = 0$ for all $\mathcal{F}$-measurable $Z$, where $Y = \mathbb{E}[X | \mathcal{F}]$. This is the *infinite-dimensional normal equation*, and it directly gives the defining properties of conditional expectation (linearity, tower property, Pythagoras). The Kalman filter — covered in this chapter — is exactly the iterative computation of a sequence of such projections, with the filtering update being the recursive solution of a normal equation.
