---
type: definition
subject: multivariate-analysis
prereqs:
  - "Def - Directional Derivative and the Gradient"
  - "Def - Higher-Order Derivatives and Ck Maps"
  - "Thm - Schwarz's Theorem on Mixed Partials"
tags: [analysis, multivariate-analysis]
---

# Notation

Throughout, $U \subseteq \mathbb{R}^n$ is an open set and $f : U \to \mathbb{R}$ is a real-valued function, of class $C^1$ or $C^2$ as stated. The **gradient** of $f$ at $x$ is the column vector $\nabla f(x) = (\partial_1 f(x), \dots, \partial_n f(x))^T$, equal to the transpose of the Jacobian matrix $Jf(x)$ of the scalar function $f$. The total derivative $Df_x$ is the linear map $h \mapsto \nabla f(x)\cdot h$. We write $\partial_i\partial_j f$ for the second partial derivative, and $\langle x, y\rangle = x^T y$ for the standard inner product. The full symbol registry is on the parent page [[Multivariate Analysis II — Inverse and Implicit Function Theorems]].

---

# Axiom Motivation

We are setting up to do optimization in several variables, and the entire programme is a translation of one-variable calculus. So begin by asking what the one-variable story actually used, and find the multivariable shadow of each piece.

In one variable, to find where $f$ is largest or smallest you look where $f'(x) = 0$. *Why* is that the right place? Because if $f'(x_0) \neq 0$ then $f$ is strictly increasing or strictly decreasing through $x_0$ — moving a little in one direction raises $f$, moving the other lowers it — so $x_0$ cannot be an extremum. The points where $f' = 0$ are the only *candidates*. The multivariable version must capture exactly this: a point is a candidate for an extremum precisely when no direction of motion changes $f$ to first order. The first-order change of $f$ in the direction $v$ is the directional derivative $\nabla f(x_0)\cdot v$. For *no* direction to give a first-order change we need $\nabla f(x_0)\cdot v = 0$ for every $v$, which forces $\nabla f(x_0) = 0$. This is the definition of a **critical point**, and it is forced on us: it is the unique condition that says "$f$ is first-order flat at $x_0$ in every direction". Anything weaker — say, $\partial_1 f = 0$ only — would admit points that are obvious non-extrema, because $f$ could still be climbing in the $x_2$ direction.

Now the harder question: a critical point is only a candidate, and in one variable you settle which kind it is with the *second* derivative. If $f''(x_0) > 0$ the graph curves upward and $x_0$ is a minimum; if $f''(x_0) < 0$ it curves downward, a maximum; if $f''(x_0) = 0$ the test is silent. What is the multivariable second derivative? It cannot be a single number, because in several variables the function can curve *differently in different directions* — upward along one axis, downward along another, producing a saddle. The right object must record the curvature in *every* direction and every mixed direction. That object is the matrix of all second partials, $\partial_i\partial_j f$ — the **Hessian**. The reason it is a *matrix* and not a list of numbers is exactly that curvature is a two-input quantity: the second-order term of the Taylor expansion is the quadratic form $h \mapsto \tfrac12 h^T (Hf) h$, and a quadratic form is encoded by a symmetric matrix.

Why *symmetric*? Because $\partial_i\partial_j f = \partial_j\partial_i f$ whenever $f$ is $C^2$ — this is Schwarz's theorem, and it is not a convention we impose but a fact we inherit. We could refuse to assume $f$ is $C^2$ and then the Hessian would not be symmetric, but we would lose the entire spectral theory: a non-symmetric matrix need not be diagonalizable and need not have real eigenvalues, and the whole sign classification below would collapse. Symmetry is the hypothesis that makes the second-order test *possible*.

Finally, why classify symmetric matrices into the four types — positive definite, negative definite, indefinite, degenerate — and not some other partition? Because these four are exactly the cases the second-order Taylor expansion distinguishes. The quadratic form $h^T H h$ either is positive for all $h \neq 0$ (bowl, minimum), negative for all $h \neq 0$ (dome, maximum), takes both signs (saddle), or vanishes for some $h \neq 0$ (a flat direction, where second order tells you nothing). A symmetric matrix is positive definite exactly when all its eigenvalues are positive — because in an orthonormal eigenbasis $h^T H h = \sum\lambda_i w_i^2$, which is positive for all $h \neq 0$ iff every $\lambda_i > 0$. So the eigenvalue-sign classification is not arbitrary: it is the *complete* invariant that determines the behaviour of the quadratic form, hence of $f$ near a critical point. The degenerate case — $0$ an eigenvalue — is carved out separately precisely because it is the case where second order is inconclusive and the answer escapes to higher-order terms.

---

# The Definition

Let $U \subseteq \mathbb{R}^n$ be open.

**Critical point.** Let $f \in C^1(U)$. A point $x_0 \in U$ is a **critical point** of $f$ if
$$\nabla f(x_0) = 0,$$
equivalently if every partial derivative $\partial_i f(x_0)$ vanishes, equivalently if the total derivative $Df_{x_0} : \mathbb{R}^n \to \mathbb{R}$ is the zero map. The value $f(x_0)$ is then a **critical value**.

**Hessian.** Let $f \in C^2(U)$. The **Hessian matrix** of $f$ at $x \in U$ is the $n \times n$ matrix
$$\big(Hf(x)\big)_{ij} = \partial_i\partial_j f(x), \qquad i, j \in \{1, \dots, n\}.$$
By Schwarz's theorem (see [[Thm - Schwarz's Theorem on Mixed Partials]]), $\partial_i\partial_j f = \partial_j\partial_i f$, so $Hf(x)$ is a **symmetric** matrix. An alternative standard notation is $D^2 f(x)$. The trace of the Hessian is the **Laplacian** $\Delta f(x) = \operatorname{tr} Hf(x) = \sum_{i=1}^n \partial_{ii} f(x)$.

**Definiteness.** A symmetric matrix $A \in \mathbb{R}^{n\times n}$ — all of whose eigenvalues are real — is called:

1. **positive definite** if all of its eigenvalues are strictly positive, equivalently $h^T A h > 0$ for every $h \neq 0$;
2. **negative definite** if all of its eigenvalues are strictly negative, equivalently $h^T A h < 0$ for every $h \neq 0$;
3. **indefinite** if it has at least one strictly positive and at least one strictly negative eigenvalue, equivalently $h^T A h$ takes both signs;
4. **degenerate** (or singular) if $0$ is an eigenvalue, equivalently $\det A = 0$.

A symmetric matrix that is positive definite, negative definite, or indefinite-and-nondegenerate is **nondegenerate**. A critical point $x_0$ of a $C^2$ function is called **nondegenerate** if its Hessian $Hf(x_0)$ is a nondegenerate matrix.

---

# Relate to Other Fields / Compression

The Hessian is the same object as the **second fundamental form** of differential geometry, restricted to the graph of $f$ at a critical point: it is the curvature tensor of the surface $z = f(x)$, and the eigenvalues of $Hf(x_0)$ are the *principal curvatures* of that surface at a flat point. The four definiteness types translate directly into the geometry of the graph — a bowl, a dome, a saddle, or a degenerate cylinder.

In **convex analysis**, the positive-semidefiniteness of $Hf$ *everywhere* is the differential criterion for $f$ to be a convex function; the strict version, positive-definiteness everywhere, gives strict convexity. The single condition "$Hf \succeq 0$ on all of $U$" is what collapses the local/global distinction: for a convex function every critical point is automatically a global minimum, so the entire apparatus of distinguishing local extrema becomes unnecessary.

In **statistics and information theory**, the Hessian of a log-likelihood is (the negative of) the **observed Fisher information**, and its definiteness governs whether a maximum-likelihood estimate is a genuine maximum and how sharply it is determined. In **physics**, the Hessian of a potential energy at an equilibrium is the matrix of *spring constants*: positive definite means a stable equilibrium, indefinite means an unstable one, and its eigenvalues are the squared normal-mode frequencies. The single linear-algebraic notion of definiteness is thus simultaneously a statement about curvature, convexity, statistical sharpness, and physical stability — the same fact wearing four coats.

---

# Examples / Corollaries

**Is an instance — the origin for $f(x,y) = x^2 + y^2$.** Here $\nabla f = (2x, 2y)$, vanishing only at $(0,0)$, so the origin is the unique critical point. The Hessian is $\begin{pmatrix} 2 & 0 \\ 0 & 2\end{pmatrix}$, with both eigenvalues equal to $2 > 0$: positive definite. The origin is a strict local (indeed global) minimum, and this is the prototype of the positive-definite case.

**Is an instance — the origin for $f(x,y) = x^2 - y^2$.** Again $\nabla f = (2x, -2y)$ vanishes only at the origin. The Hessian $\begin{pmatrix} 2 & 0 \\ 0 & -2\end{pmatrix}$ has eigenvalues $2$ and $-2$: indefinite. The origin is a saddle — $f$ increases along the $x$-axis and decreases along the $y$-axis. This is the genuinely multivariable phenomenon with no one-variable analogue.

**Is NOT an instance of a nondegenerate critical point — the origin for $f(x,y) = x^4 + y^4$.** The gradient $\nabla f = (4x^3, 4y^3)$ vanishes at the origin, so it *is* a critical point. But the Hessian is $\begin{pmatrix} 12x^2 & 0 \\ 0 & 12y^2\end{pmatrix}$, which at the origin is the *zero matrix* — both eigenvalues are $0$, so the critical point is degenerate. The function $x^4 + y^4$ has a strict minimum there, but the Hessian cannot detect it; the answer lives in the fourth-order term. Contrast $-x^4 - y^4$ (maximum) and $x^4 - y^4$ (saddle): all three share the zero Hessian, which is why the degenerate case is genuinely inconclusive.

**Is NOT an instance of a critical point — any point of $f(x,y) = x$.** The gradient is $\nabla f = (1, 0)$, which never vanishes. This function has no critical points at all and no extrema on any open set — a useful reminder that "critical point" is a property of a *specific point*, and a function may have none.

**Corollary — a critical point is necessary but not sufficient for an extremum.** Every interior local extremum is a critical point (this is the [[Thm - First-Order Optimality Condition|first-order optimality condition]]), but the converse fails: the saddle of $x^2 - y^2$ is a critical point that is not an extremum. The Hessian's job is precisely to filter the critical points into extrema and saddles.

**Corollary — the Hessian of a quadratic form is constant and equals (twice) its matrix.** For $f(x) = \tfrac12 x^T A x$ with $A$ symmetric, $\nabla f(x) = Ax$ and $Hf(x) = A$ at every point. So the local picture near the critical point $x = 0$ is *exactly* the quadratic form, with no error term — this is why the second-order Taylor expansion, which approximates a general $f$ near a critical point by such a quadratic, is the natural tool.

**Calibration check.** Verify that $f(x,y) = x^3 - 3xy^2$ has the origin as a degenerate critical point (compute the Hessian there); that the matrix $\begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix}$ is positive definite by finding its eigenvalues $1, 3$, or by the $2\times 2$ test "top-left entry $> 0$ and determinant $> 0$"; and that $\begin{pmatrix} 1 & 2 \\ 2 & 1\end{pmatrix}$ is indefinite (determinant $-3 < 0$). If you can also explain why a symmetric matrix with a zero eigenvalue makes the second-order test fail, you have understood every clause of the definition.

---

# Unlocked by This

> [!tip] The Second-Order Optimality Test *(from this topic)*
> The definiteness type of the Hessian at a critical point is precisely the input to the [[Thm - Second-Order Optimality Conditions|second-order optimality conditions]]: positive definite gives a minimum, negative definite a maximum, indefinite a saddle. The classification was set up exactly so that this test could be stated.

> [!tip] Morse Functions and Topology *(from Differential Topology)*
> A function all of whose critical points are nondegenerate is a **Morse function**, and the number of negative Hessian eigenvalues at a critical point is its **Morse index**. Morse theory shows that the indices of the critical points of a generic function on a manifold determine the manifold's topology — how many holes of each dimension it has.

> [!tip] Convex Functions *(from Convex Optimization)*
> A $C^2$ function is **convex** exactly when its Hessian is positive *semi*definite at every point. For a convex function the local/global distinction vanishes: every critical point is a global minimum. The definiteness vocabulary defined here is the language in which convexity is stated.
