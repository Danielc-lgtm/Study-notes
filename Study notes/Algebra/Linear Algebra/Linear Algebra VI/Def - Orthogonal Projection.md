---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
  - "Def - Orthogonal Complement"
  - "Def - Orthonormal Basis"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is an inner product space over $\mathbf{F}$. $U \subseteq V$ is a finite-dimensional subspace. The orthogonal projection is denoted $P_U$. We also use $P : V \to V$ to denote an abstract operator and check when it is an orthogonal projection. See [[Linear Algebra VI — §6 Inner Product Spaces]] for the full notation registry.

---

# Axiom Motivation

We have a finite-dimensional subspace $U \subseteq V$ and want to define an operator $P_U : V \to V$ that "projects $V$ onto $U$ orthogonally" — informally, drops a perpendicular from each $v \in V$ onto $U$. This is the natural geometric operation, generalising the picture in $\mathbb{R}^3$ where "the projection of a vector onto a plane" is its shadow when you stand directly above the plane.

The mathematical setup is the [[Thm - Orthogonal Decomposition|orthogonal decomposition theorem]]: $V = U \oplus U^\perp$ for any finite-dimensional subspace $U$. Every $v \in V$ has a unique decomposition $v = u + w$ with $u \in U$ and $w \in U^\perp$. The orthogonal projection is the operator that picks out the first summand: $P_U v = u$.

Why is this the *right* definition? Three reasons.

First, it gives a **well-defined linear operator**. Uniqueness of the decomposition means $P_U$ is single-valued; linearity comes from the fact that $V = U \oplus U^\perp$ is a direct-sum decomposition (the decomposition of $v_1 + v_2$ is $(u_1 + u_2) + (w_1 + w_2)$, etc.). So $P_U$ is automatically a linear map, not merely a function.

Second, it satisfies $P_U^2 = P_U$ — **idempotency**. If $v = u + w$, then $P_U v = u$, and computing $P_U(P_U v) = P_U u$ uses the decomposition $u = u + 0$ (with $u \in U$ and $0 \in U^\perp$), giving $P_U u = u$. So $P_U^2 v = P_U v$ for every $v$. Idempotency is the algebraic statement that "projecting twice is the same as projecting once" — once you're in $U$, staying in $U$ does nothing.

Third, and crucially, it satisfies **self-adjointness**: $\langle P_U v_1, v_2\rangle = \langle v_1, P_U v_2\rangle$ for all $v_1, v_2 \in V$. *Why this matters:* idempotency alone characterises a *general* (possibly oblique) projection — its range and kernel are complementary [[Def - Subspace|subspaces]], but not necessarily orthogonal. Self-adjointness is the extra condition that forces $\ker P_U = (\operatorname{range} P_U)^\perp$, making the projection *orthogonal* rather than oblique. The two conditions together characterise $P_U$ uniquely among all linear operators: an operator $P$ is the orthogonal projection onto some subspace if and only if $P^2 = P$ and $P^* = P$.

This is the **categorical characterisation** of an orthogonal projection: idempotent and self-adjoint. The subspace is then $U = \operatorname{range}(P)$, and $\ker(P) = U^\perp$ automatically. This characterisation is the operational definition for problems where you suspect an operator is an orthogonal projection — check $P^2 = P$ and $P^* = P$.

What if we drop self-adjointness? Then we have a general projection, which is still useful but no longer geometric. A general projection along a non-orthogonal direction has $\operatorname{range}(P) \oplus \ker(P) = V$ but the two [[Def - Subspace|subspaces]] are not orthogonal; the "projection of $v$" is what you get by sliding $v$ along $\ker P$ until you hit $\operatorname{range} P$. The orthogonal case is the special case where you slide perpendicular to $\operatorname{range} P$.

What if we drop the requirement that $U$ be finite-dimensional? In a Hilbert space, the construction extends to **closed** subspaces; for non-closed subspaces, the orthogonal decomposition fails and there is no well-defined orthogonal projection. The closedness condition is the infinite-dimensional analog of "finite-dimensional" for this purpose.

---

# The Definition

Let $V$ be an inner product space and $U \subseteq V$ a **finite-dimensional** subspace. The **orthogonal projection** of $V$ onto $U$ is the operator $P_U \in \mathcal{L}(V)$ defined as follows. For each $v \in V$, by the [[Thm - Orthogonal Decomposition|orthogonal decomposition theorem]] there exist unique $u \in U$ and $w \in U^\perp$ with $v = u + w$. Set

$$
P_U v = u.
$$

Equivalently — and this is often more useful in computation — if $e_1, \dots, e_m$ is an **orthonormal basis** of $U$, then

$$
P_U v = \langle v, e_1\rangle e_1 + \cdots + \langle v, e_m\rangle e_m.
$$

The two formulations agree, and the orthonormal-basis formula is the explicit way to compute $P_U v$.

**Properties of $P_U$:**

1. $P_U \in \mathcal{L}(V)$ — $P_U$ is a linear operator on $V$.
2. $P_U u = u$ for every $u \in U$.
3. $P_U w = 0$ for every $w \in U^\perp$.
4. $\operatorname{range} P_U = U$.
5. $\ker P_U = U^\perp$.
6. $v - P_U v \in U^\perp$ for every $v \in V$.
7. **Idempotency:** $P_U^2 = P_U$.
8. **Self-adjointness:** $\langle P_U v_1, v_2\rangle = \langle v_1, P_U v_2\rangle$ for all $v_1, v_2 \in V$.
9. $\|P_U v\| \leq \|v\|$ for every $v \in V$ (the projection cannot increase length).
10. **Minimization:** $P_U v$ is the unique closest point in $U$ to $v$ — see [[Thm - Best Approximation by Orthogonal Projection]].

---

# Categorical / Structural Definition

An **orthogonal projection** on $V$ is a linear operator $P \in \mathcal{L}(V)$ satisfying both:

1. **Idempotency:** $P^2 = P$.
2. **Self-adjointness:** $\langle Pv_1, v_2\rangle = \langle v_1, Pv_2\rangle$ for all $v_1, v_2 \in V$.

Equivalently, $P^2 = P$ and $\ker P = (\operatorname{range} P)^\perp$.

Given any such $P$, the subspace $U = \operatorname{range} P$ is finite-dimensional (or closed, in Hilbert space), and $P = P_U$ in the constructive sense above. Conversely, every $P_U$ for $U$ finite-dimensional (or closed) is idempotent and self-adjoint. So the construction $U \mapsto P_U$ is a bijection between (finite-dimensional or closed) subspaces of $V$ and orthogonal projections in $\mathcal{L}(V)$.

This categorical view promotes orthogonal projections from constructed objects to *operators satisfying these two axioms*, and it is the perspective that generalizes most cleanly to Hilbert spaces, von Neumann algebras, and the lattice of projections in an operator algebra.

---

# Relate to Other Fields / Compression

**The minimizer/projector unity.** The geometric content of $P_U$ is captured by two equivalent statements that recur throughout applied mathematics:
- **Orthogonality:** $v - P_U v \perp U$.
- **Minimization:** $P_U v = \operatorname*{argmin}_{u \in U} \|v - u\|$.

The equivalence is the [[Thm - Best Approximation by Orthogonal Projection|best-approximation theorem]], and it is the bridge that turns geometric problems ("perpendicular to $U$") into optimisation problems ("closest in $U$"), and vice versa. Every applied-math problem of the form "fit a model to data" routes through this unity: least squares is "find $\beta$ minimising $\|y - X\beta\|^2$", which is "project $y$ onto the column space of $X$", which is "make $y - X\beta$ perpendicular to the column space" — three statements of the same problem.

**Connection to the pseudoinverse.** For $T \in \mathcal{L}(V, W)$ between finite-dimensional inner product spaces, the [[Def - Pseudoinverse|pseudoinverse]] $T^\dagger$ is built from orthogonal projections: $T T^\dagger = P_{\operatorname{range} T}$ and $T^\dagger T = P_{(\ker T)^\perp}$. The pseudoinverse "inverts $T$ on the orthogonal complement of its kernel, projecting onto the range".

**Hilbert space.** In a Hilbert space, the orthogonal projection onto a closed subspace exists and is bounded with operator norm $\leq 1$. More generally, the **Hilbert projection theorem** asserts that for any *closed convex* subset $C$ of a Hilbert space, every $v \in H$ has a unique nearest point $P_C v$ in $C$. This is much stronger than the subspace case and is the workhorse of convex optimisation in infinite dimensions.

**True name:** an orthogonal projection is the idempotent self-adjoint operator with a chosen range. The subspace $U$ and the operator $P_U$ are two views of one object, and the projection lattice of $V$ is isomorphic to the lattice of (closed) subspaces.

---

# Examples / Corollaries

**Is an instance: projection onto a one-dimensional subspace.** Let $u \in V$ be nonzero and $U = \operatorname{span}(u)$. With orthonormal basis $\{u/\|u\|\}$ of $U$, the projection is
$$
P_U v = \left\langle v, \frac{u}{\|u\|}\right\rangle \frac{u}{\|u\|} = \frac{\langle v, u\rangle}{\|u\|^2} u.
$$
This is the formula for "the projection of $v$ onto the line through $u$", familiar from $\mathbb{R}^3$ vector calculus.

**Is an instance: projection onto a coordinate plane.** In $\mathbb{R}^3$, let $U = \{(x, y, 0)\}$, the $xy$-plane. Then $P_U(x, y, z) = (x, y, 0)$ — set the last coordinate to zero. This is the "shadow on the floor" picture.

**Is an instance: projection onto an orthonormal-basis subspace.** If $e_1, \dots, e_m, e_{m+1}, \dots, e_n$ is an orthonormal basis of $V$ and $U = \operatorname{span}(e_1, \dots, e_m)$, then
$$
P_U\left(\sum_{k=1}^n a_k e_k\right) = \sum_{k=1}^m a_k e_k,
$$
i.e., set the last $n - m$ coordinates to zero.

**Is an instance: projection onto polynomials of degree $\leq 5$ in $L^2[-\pi, \pi]$.** Let $V = L^2[-\pi, \pi]$, $U = \mathcal{P}_5(\mathbb{R})$ (degree $\leq 5$ polynomials). After Gram-Schmidting $1, x, x^2, x^3, x^4, x^5$ to an orthonormal basis $e_1, \dots, e_6$ of $U$, the projection of $\sin x$ onto $U$ is $\sum_k \langle \sin x, e_k\rangle e_k$, which is the **best polynomial approximation to $\sin x$ of degree $\leq 5$ in the $L^2$ sense**. See [[Ex - Best polynomial approximation to sine]].

**Is NOT an instance: projection along a non-orthogonal direction.** Let $V = \mathbb{R}^2$ and consider $P(x, y) = (x + y, 0)$. This satisfies $P^2 = P$ (check: $P(x + y, 0) = (x + y + 0, 0) = P(x, y)$), so it is *a* projection — but it is not orthogonal because the kernel $\{(x, -x)\}$ is not perpendicular to the range $\{(t, 0)\}$. Check self-adjointness: $\langle P(1, 0), (0, 1)\rangle = \langle (1, 0), (0, 1)\rangle = 0$, but $\langle (1, 0), P(0, 1)\rangle = \langle (1, 0), (1, 0)\rangle = 1$. Not self-adjoint, so not orthogonal. The repair for orthogonality: project along the perpendicular direction, which gives $P_{\text{orth}}(x, y) = (x, 0)$.

**Is NOT an instance: any operator with $P^2 = P$ and $\|P\| > 1$.** An orthogonal projection has $\|P_U v\| \leq \|v\|$ for every $v$ (property 9 above). So an idempotent operator with norm strictly greater than $1$ — for example, the oblique projection $P(x, y) = (x + y, 0)$ above has $\|P(0, 1)\| = \|(1, 0)\| = 1$ but $\|P(1, 1)\| = \|(2, 0)\| = 2$ vs. $\|(1, 1)\| = \sqrt{2}$ — cannot be orthogonal.

**Corollary (linearity).** $P_U \in \mathcal{L}(V)$ — the orthogonal projection is a linear operator. *Proof:* the decomposition $v = u + w$ depends linearly on $v$ because $V = U \oplus U^\perp$ is a direct sum.

**Corollary (orthonormal-basis formula).** If $e_1, \dots, e_m$ is an orthonormal basis of $U$, then $P_U v = \sum_k \langle v, e_k\rangle e_k$ for every $v \in V$. *Proof:* the right-hand side is in $U$, and $v - \sum_k \langle v, e_k\rangle e_k$ is orthogonal to every $e_j$ (by direct calculation), hence to all of $U$. Uniqueness of the decomposition forces the right-hand side to equal $P_U v$.

**Corollary (idempotent + self-adjoint = orthogonal projection).** An operator $P \in \mathcal{L}(V)$ is an orthogonal projection onto its range if and only if $P^2 = P$ and $P^* = P$ (self-adjointness in the inner-product sense). *Proof:* the forward direction is properties 7 and 8 above; the reverse uses self-adjointness to show $\ker P = (\operatorname{range} P)^\perp$, and then idempotency identifies $P$ with the projection onto $\operatorname{range} P$.

**Corollary (norm bound).** $\|P_U v\| \leq \|v\|$ for every $v \in V$. *Proof:* $\|v\|^2 = \|P_U v\|^2 + \|v - P_U v\|^2$ by Pythagoras (since $P_U v \in U$ and $v - P_U v \in U^\perp$), so $\|P_U v\|^2 \leq \|v\|^2$.

**Calibration check.** Three things a reader should verify: (i) compute $P_U(1, 2, 3)$ in $\mathbb{R}^3$ where $U = \operatorname{span}((1, 0, 1))$, and verify the result is on the line through $(1, 0, 1)$; (ii) check that the orthogonal-projection operator on $\mathbb{R}^2$ onto the $x$-axis is given by the matrix $\begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix}$, which is idempotent and self-adjoint (symmetric); (iii) verify directly that $P_U v$ is orthogonal to $v - P_U v$, i.e., $\langle P_U v, v - P_U v\rangle = 0$ — this is the orthogonality-of-decomposition statement.

---

# Unlocked by This

> [!tip] Spectral Theorem and Spectral Decomposition *(from Linear Algebra VII)*
> A self-adjoint operator $T \in \mathcal{L}(V)$ on a finite-dimensional inner product space decomposes as $T = \sum_k \lambda_k P_k$, where $\lambda_k$ are the (real) eigenvalues and $P_k$ are the orthogonal projections onto the eigenspaces. The $P_k$ are pairwise orthogonal projections summing to the identity ($\sum_k P_k = I$, $P_j P_k = 0$ for $j \neq k$). The **spectral theorem** is the assertion that every self-adjoint (or more generally normal) operator has such a decomposition. Quantum mechanics uses this decomposition daily: a self-adjoint observable's spectral decomposition partitions the Hilbert space into eigenspaces of definite-value states, with the orthogonal projections giving the probability amplitudes for measurement outcomes.

> [!tip] Least Squares and the Normal Equations *(from Linear Algebra XI)*
> For $A \in \mathbb{R}^{m \times n}$ with linearly independent columns, the **least-squares problem** $\min_x \|Ax - b\|^2$ is solved by $\hat x = (A^TA)^{-1}A^T b$, and $A\hat x = P_{\operatorname{col} A} b$ is the orthogonal projection of $b$ onto the column space of $A$. The normal equations $A^T A x = A^T b$ are the algebraic statement that the residual $A x - b$ is orthogonal to the column space (since $A^T(Ax - b) = 0$ says the columns of $A$ are orthogonal to the residual). Every statistical regression problem is, at its core, an orthogonal projection onto a column space.

> [!tip] Kalman Filter *(from Estimation Theory and Control)*
> The Kalman filter is, mathematically, an orthogonal projection onto the linear span of observed data, with the inner product being conditional covariance. At each step, the new estimate is the orthogonal projection of the unknown state onto the data-so-far Hilbert space; the "innovation" is the orthogonal complement of the new observation with respect to the previous observations. Linear minimum-variance estimation is orthogonal projection in disguise, and the recursive updates of the Kalman filter are how the projection is computed efficiently.
