---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
  - "Def - Orthogonal Projection"
  - "Def - Orthogonal Complement"
  - "Thm - Pythagorean Theorem"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is an inner product space over $\mathbf{F}$. $U \subseteq V$ is a finite-dimensional subspace. $P_U : V \to V$ is the [[Def - Orthogonal Projection|orthogonal projection]] onto $U$. The notation registry is on [[Linear Algebra VI — §6 Inner Product Spaces]].

---

# Statement

> **Theorem (Best Approximation by [[Def - Orthogonal Projection|Orthogonal Projection]]).** Let $V$ be an inner product space and $U \subseteq V$ a finite-dimensional subspace. For any $v \in V$,
> $$\|v - P_U v\| \leq \|v - u\| \qquad \text{for every } u \in U,$$
> with equality if and only if $u = P_U v$. That is, $P_U v$ is the unique closest point in $U$ to $v$.

> **Corollary (Computation via orthonormal basis).** If $e_1, \dots, e_m$ is an orthonormal basis of $U$, then the closest point in $U$ to $v$ is
> $$P_U v = \langle v, e_1\rangle e_1 + \cdots + \langle v, e_m\rangle e_m.$$

> **Corollary (Bessel's inequality).** If $e_1, \dots, e_m$ is an orthonormal list in $V$ and $v \in V$, then
> $$\sum_{k=1}^m |\langle v, e_k\rangle|^2 \leq \|v\|^2.$$

---

# Motivation

This is the **central theorem of the chapter** and the engine that powers virtually every application of inner-product geometry. It says: to find the closest point in a subspace, project orthogonally. Conversely, the orthogonal projection *is* the closest-point map. The two statements — orthogonality and minimization — are the same statement, two faces of one identification.

This identification is what makes the chapter applicable. Pure mathematics asks "what is the perpendicular from $v$ to $U$?"; applied mathematics asks "what is the best approximation to $v$ in $U$?". The two questions have the same answer, $P_U v$, and the chapter shows they are the same question. Every applied-mathematics minimization in a vector space — **least squares**, **best polynomial approximation**, **Fourier truncation**, **denoising**, **signal compression**, **regression**, **conditional expectation** — routes through this theorem.

The role of the theorem in the chapter:

First, it **identifies the orthogonal projection with the closest-point map**. The operator $P_U$ defined abstractly by the orthogonal decomposition has a geometric meaning: $P_U v$ is "the foot of the perpendicular from $v$ to $U$", which is the same as "the point in $U$ closest to $v$". The two definitions agree, and the theorem proves this.

Second, it **converts minimization problems to orthogonality conditions**. To minimise $\|v - u\|^2$ over $u \in U$, the necessary and sufficient condition is "$v - u \perp U$" — the residual is orthogonal to the search subspace. This is the **first-order optimality condition** for the squared-distance objective, and it characterizes the minimum without doing any minimization.

Third, it gives the **fundamental identity** $\|v\|^2 = \|P_U v\|^2 + \|v - P_U v\|^2$, the Pythagorean decomposition of the squared length of $v$ into "norm in $U$" and "norm in $U^\perp$". From this identity, Bessel's inequality follows immediately ($\|v\|^2 \geq \|P_U v\|^2 = \sum |\langle v, e_k\rangle|^2$), with equality iff $v \in U$. Bessel's inequality, in turn, is the foundation of convergence of orthonormal expansions in $L^2$ and infinite-dimensional Hilbert spaces.

The theorem is also the **finite-dimensional case of the Hilbert projection theorem**, which extends to closed convex subsets of any Hilbert space. This generalization is the workhorse of convex optimization, variational calculus, and the calculus of variations in infinite [[Def - Dimension|dimensions]].

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is: a finite-dimensional subspace $U$ and a vector $v$. The skill is recognising minimization problems that are projections in disguise.

The first source is **a question about minimising $\|v - u\|$ over $u \in U$**. Property $B$: an explicit minimization problem with the squared-distance objective. Bridge: the minimum is achieved at $u = P_U v$, computable as $\sum_k \langle v, e_k\rangle e_k$ in any orthonormal basis of $U$.

The second source is **a least-squares problem** $\min_x \|Ax - b\|$. Property $B$: minimise the residual norm of a linear system that may have no exact solution. Bridge: this is the projection of $b$ onto $\operatorname{range}(A) = \operatorname{col}(A)$; the minimum is $\|b - P_{\operatorname{col} A} b\|$, and the minimizer $x^*$ satisfies $Ax^* = P_{\operatorname{col} A} b$.

The third source is **a best-polynomial-approximation problem**. Property $B$: find $p \in \mathcal{P}_m$ minimising $\int_a^b (f - p)^2$. Bridge: this is projection of $f$ onto $\mathcal{P}_m \subseteq L^2[a, b]$; the minimiser is $p^* = P_{\mathcal{P}_m} f$, computable by Gram-Schmidt to get an orthonormal polynomial basis and then summing inner products with $f$.

The fourth source is the **conditional expectation problem**. Property $B$: find $Y \in L^2(\mathcal{G})$ (the space of $\mathcal{G}$-measurable random variables) minimising $E[(X - Y)^2]$. Bridge: this is projection of $X$ onto $L^2(\mathcal{G}) \subseteq L^2(\mathcal{F})$; the minimiser is $E[X | \mathcal{G}]$, the conditional expectation. The orthogonality condition $X - E[X|\mathcal{G}] \perp L^2(\mathcal{G})$ is the defining property of conditional expectation in $L^2$.

**Targets (Output Amplification)**

The conclusion is $\|v - P_U v\| \leq \|v - u\|$ for all $u \in U$.

The first target is **Bessel's inequality** $\sum_k |\langle v, e_k\rangle|^2 \leq \|v\|^2$ for orthonormal lists. Property $D$: with the orthonormal list, $P_U v = \sum_k \langle v, e_k\rangle e_k$ and $\|P_U v\|^2 = \sum_k |\langle v, e_k\rangle|^2$. Combination: $\|P_U v\| \leq \|v\|$ (from $\|v\|^2 = \|P_U v\|^2 + \|v - P_U v\|^2 \geq \|P_U v\|^2$) gives Bessel.

The second target is **Parseval's identity** $\sum_k |\langle v, e_k\rangle|^2 = \|v\|^2$ for orthonormal bases. Property $D$: when $\{e_k\}$ spans $V$, $P_V v = v$ and the equality case of Bessel holds. Combination: $\|v\|^2 = \sum |\langle v, e_k\rangle|^2$ — the squared norm equals the sum of squared coordinates.

The third target is the **first-order optimality condition** for least-squares-style minimization. Property $D$: the residual $v - P_U v$ is orthogonal to $U$ — equivalently, $\langle v - P_U v, u\rangle = 0$ for every $u \in U$. Combination: this is the variational characterization of the projection, used throughout PDE analysis and optimization.

The fourth target is **convergence of orthonormal expansions in $L^2$**. Property $D$: in a Hilbert space, an orthonormal sequence $e_1, e_2, \dots$ produces partial sums $S_N v = \sum_{k \leq N} \langle v, e_k\rangle e_k$, which are projections onto the $N$-dimensional subspaces $U_N = \operatorname{span}(e_1, \dots, e_N)$. Combination: Bessel's inequality gives $\sum_k |\langle v, e_k\rangle|^2 \leq \|v\|^2$, hence the series $\sum_k |\langle v, e_k\rangle|^2$ converges; this in turn gives Cauchy-convergence of the partial sums and hence convergence of the orthonormal expansion.

---

# Why Is It True

The intuition is the cleanest geometric picture in the chapter: **the perpendicular from a point to a subspace minimises the distance to the subspace**.

Here is the picture in $\mathbb{R}^3$ with $U$ a plane through the origin. Take any point $v$ above the plane. Drop a perpendicular from $v$ to $U$; the foot of the perpendicular is the closest point on $U$ to $v$. Any other point $u \in U$ is connected to $v$ by a path that goes from $u$ to the foot of the perpendicular (a horizontal segment in $U$) and then from the foot up to $v$ (a vertical segment of length $\|v - P_U v\|$, the perpendicular distance). The total length, by Pythagoras, is $\sqrt{\|u - P_U v\|^2 + \|v - P_U v\|^2}$, which is at least $\|v - P_U v\|$, with equality iff $u = P_U v$.

The proof in general is the same picture made algebraic. For any $u \in U$, write
$$
v - u = (v - P_U v) + (P_U v - u).
$$
The first summand is in $U^\perp$ (by definition of orthogonal projection); the second is in $U$ (a difference of elements of $U$). So the two summands are orthogonal. By the [[Thm - Pythagorean Theorem|Pythagorean theorem]],
$$
\|v - u\|^2 = \|v - P_U v\|^2 + \|P_U v - u\|^2 \geq \|v - P_U v\|^2,
$$
with equality iff $\|P_U v - u\|^2 = 0$, i.e., $u = P_U v$.

**The one-liner mechanism: $v - u = (v - P_U v) + (P_U v - u)$ is an orthogonal decomposition (first summand in $U^\perp$, second in $U$); Pythagoras gives $\|v - u\|^2 = \|v - P_U v\|^2 + \|P_U v - u\|^2 \geq \|v - P_U v\|^2$, with equality iff $u = P_U v$.**

The orthogonality condition has a different reading. Setting the derivative of $\|v - u\|^2$ to zero (treating $u$ as a variable in $U$) gives $\langle v - u, w\rangle = 0$ for every $w \in U$ — i.e., $v - u \in U^\perp$. The condition that the residual is orthogonal to the search space is exactly the first-order optimality condition for the squared-distance objective. The theorem says this necessary condition is also sufficient, and the unique optimum is $u = P_U v$.

---

# What Makes This Hard

The proof is one line (Pythagoras applied to an orthogonal decomposition), but two subtleties are worth flagging.

First, **recognising the orthogonality of the decomposition**. The key step is $v - u = (v - P_U v) + (P_U v - u)$, where the first summand is in $U^\perp$ (by definition of $P_U$) and the second is in $U$ (a difference of elements of $U$). The decomposition is *orthogonal*, which is exactly what triggers Pythagoras. A student who tries to expand $\|v - u\|^2$ directly without this decomposition will not see the inequality come out cleanly.

Second, **the equality case** clarifies that the minimum is *unique*. Equality in Pythagoras $\|v - u\|^2 = \|v - P_U v\|^2 + \|P_U v - u\|^2$ requires $\|P_U v - u\|^2 = 0$, i.e., $u = P_U v$. Without uniqueness, the orthogonal projection could in principle be one of many "best approximations"; the theorem asserts it is the unique one.

A third subtlety: in infinite-dimensional Hilbert spaces, the theorem extends to **closed** [[Def - Subspace|subspaces]]. For non-closed [[Def - Subspace|subspaces]], the projection (best-approximation) map may not exist. The pathology occurs because the existence of $P_U v$ requires the orthogonal decomposition $V = U \oplus U^\perp$, which holds only for closed $U$ in Hilbert space. This is the same closedness assumption that underlies the orthogonal decomposition.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write $v - u = (v - P_U v) + (P_U v - u)$ as an orthogonal decomposition and apply Pythagoras.

**Subgoal decomposition:**

1. **Write the orthogonal decomposition.** $v - u = (v - P_U v) + (P_U v - u)$, where the first summand is in $U^\perp$ and the second is in $U$.
   - *Hint:* by definition of orthogonal projection, $v - P_U v \in U^\perp$; and $P_U v - u \in U$ as a difference of elements of $U$.
   - *Why needed:* the two summands being orthogonal is what triggers Pythagoras.

2. **Apply Pythagoras.** $\|v - u\|^2 = \|v - P_U v\|^2 + \|P_U v - u\|^2$.
   - *Hint:* the [[Thm - Pythagorean Theorem|Pythagorean theorem]] applied to orthogonal summands.
   - *Why needed:* this is the key identity.

3. **Conclude.** $\|v - u\|^2 \geq \|v - P_U v\|^2$, with equality iff $\|P_U v - u\|^2 = 0$, i.e., $u = P_U v$.
   - *Hint:* $\|P_U v - u\|^2 \geq 0$ with equality iff $P_U v = u$.
   - *Why needed:* this is the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: The decomposition $v - u = (v - P_U v) + (P_U v - u)$ is orthogonal
> **Statement:** For any $v \in V$ and $u \in U$, the vectors $v - P_U v$ and $P_U v - u$ are orthogonal: $\langle v - P_U v, P_U v - u\rangle = 0$.
>
> **Hint:** $v - P_U v \in U^\perp$ (by definition of $P_U$), and $P_U v - u \in U$ (a difference of elements of $U$). The two subspaces are orthogonal.
>
> **Why needed:** This is the orthogonality of the decomposition that triggers the Pythagorean theorem.
>
> > [!note]- Full proof
> > By construction (the definition of $P_U$ via orthogonal decomposition), $v = P_U v + (v - P_U v)$ with $P_U v \in U$ and $v - P_U v \in U^\perp$. So $v - P_U v \in U^\perp$.
> >
> > $P_U v - u$ is a difference of two elements of $U$ (both $P_U v$ and $u$ are in $U$), hence in $U$.
> >
> > Since $v - P_U v \in U^\perp$ and $P_U v - u \in U$, their inner product vanishes: $\langle v - P_U v, P_U v - u\rangle = 0$.

> [!note]- Lemma 2: Equality case in Pythagoras
> **Statement:** In an inner product space, $\|a + b\|^2 = \|a\|^2 + \|b\|^2$ for orthogonal $a, b$, with the additional remark that $\|a + b\|^2 = \|a\|^2 \iff \|b\| = 0 \iff b = 0$.
>
> **Hint:** Pythagoras gives the equation; the equality case is direct algebra plus the definiteness of the norm.
>
> **Why needed:** Identifies the equality case in the inequality $\|v - u\|^2 \geq \|v - P_U v\|^2$.
>
> > [!note]- Full proof
> > By Pythagoras for orthogonal $a, b$: $\|a + b\|^2 = \|a\|^2 + \|b\|^2$. So $\|a + b\|^2 = \|a\|^2$ iff $\|b\|^2 = 0$, iff $b = 0$ (definiteness).

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $V$ be an inner product space, $U \subseteq V$ a finite-dimensional subspace, and $v \in V$. Then $\|v - P_U v\| \leq \|v - u\|$ for every $u \in U$, with equality iff $u = P_U v$.
>
> *Proof.* Fix $u \in U$. Write
> $$v - u = (v - P_U v) + (P_U v - u).$$
> By Lemma 1, $v - P_U v \in U^\perp$ and $P_U v - u \in U$ are orthogonal. By the [[Thm - Pythagorean Theorem|Pythagorean theorem]],
> $$\|v - u\|^2 = \|v - P_U v\|^2 + \|P_U v - u\|^2 \geq \|v - P_U v\|^2.$$
> Taking square roots gives $\|v - u\| \geq \|v - P_U v\|$.
>
> Equality holds iff $\|P_U v - u\|^2 = 0$, iff $P_U v = u$. $\qquad\blacksquare$
>
> **Corollary (Bessel's inequality).** If $e_1, \dots, e_m$ is an orthonormal list in $V$ and $v \in V$, then $\sum_{k=1}^m |\langle v, e_k\rangle|^2 \leq \|v\|^2$.
>
> *Proof.* Let $U = \operatorname{span}(e_1, \dots, e_m)$. The orthogonal projection of $v$ onto $U$ is $P_U v = \sum_k \langle v, e_k\rangle e_k$ (the orthonormal-basis formula). Its norm is $\|P_U v\|^2 = \sum_k |\langle v, e_k\rangle|^2$ (Pythagoras for an orthonormal list).
>
> The best-approximation theorem applied with $u = 0$ gives $\|v - P_U v\| \leq \|v - 0\| = \|v\|$. Squaring and using $\|v\|^2 = \|P_U v\|^2 + \|v - P_U v\|^2$ (Pythagoras applied to the orthogonal decomposition $v = P_U v + (v - P_U v)$): rearranging gives $\|P_U v\|^2 = \|v\|^2 - \|v - P_U v\|^2 \leq \|v\|^2$, i.e., $\sum_k |\langle v, e_k\rangle|^2 \leq \|v\|^2$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Least-squares regression.** For data $(x_i, y_i)_{i=1}^n$ and a linear model $y = \beta_0 + \beta_1 x$, the least-squares estimates $\hat\beta_0, \hat\beta_1$ minimize $\sum_i (y_i - \beta_0 - \beta_1 x_i)^2$. This is the orthogonal projection of the $y$-vector onto the column space of the design matrix $X = (\mathbf{1}\ x)$, and the estimates are $\hat\beta = (X^TX)^{-1}X^T y$ — the **normal-equations** formula. The residual $y - X\hat\beta$ is orthogonal to the column space, which is the **first-order optimality condition**. See [[Linear Algebra XI — Applied II — Least Squares]].

**Fourier series partial sums.** For $f \in L^2[-\pi, \pi]$, the partial Fourier sum $S_N(f) = \sum_{|n| \leq N} c_n e^{inx}$ with $c_n = \frac{1}{2\pi}\int_{-\pi}^\pi f e^{-inx}$ is the orthogonal projection of $f$ onto the trigonometric polynomials of degree $\leq N$. By the best-approximation theorem, $S_N(f)$ is the **best $L^2$ approximation** to $f$ by such polynomials — better than any Taylor truncation. Bessel's inequality $\sum |c_n|^2 \leq \|f\|^2/(2\pi)$ becomes Parseval's identity $\sum |c_n|^2 = \|f\|^2/(2\pi)$ as $N \to \infty$, showing the Fourier expansion converges in $L^2$. See [[Ex - Best polynomial approximation to sine]] for an analogous polynomial-approximation problem.

**Conditional expectation as orthogonal projection.** For a random variable $X \in L^2(\Omega, \mathcal{F}, P)$ and sub-$\sigma$-algebra $\mathcal{G}$, the **conditional expectation** $E[X|\mathcal{G}]$ is the orthogonal projection of $X$ onto $L^2(\Omega, \mathcal{G}, P)$. The defining property — $E[X 1_A] = E[E[X|\mathcal{G}] 1_A]$ for every $A \in \mathcal{G}$ — is the orthogonality condition $X - E[X|\mathcal{G}] \perp L^2(\mathcal{G})$. The best-approximation theorem gives the **minimum mean-square error** interpretation: $E[X|\mathcal{G}]$ is the $L^2$-best predictor of $X$ using only $\mathcal{G}$-measurable information.

**Method of normal equations in numerical analysis.** Solving the overdetermined system $Ax = b$ (with $A$ tall) by minimising $\|Ax - b\|^2$ uses the orthogonality condition $A^T(Ax - b) = 0$, giving the **normal equations** $A^TA x = A^T b$. The orthogonality of the residual to the column space is the first-order optimality condition for the squared-distance objective. Conversely, the QR factorization $A = QR$ gives an alternative algorithm: $Ax = b$ becomes $QRx = b$, so $Rx = Q^T b$, solvable by back-substitution. Both algorithms are projection-based and rest on the best-approximation theorem.

---

# Bridges

- **[[Def - Orthogonal Projection|Orthogonal Projection]]** — the best-approximation theorem identifies the orthogonal projection with the closest-point map. The two definitions of $P_U$ — "the $U$-component in the orthogonal decomposition" and "the closest point in $U$ to $v$" — agree, and the theorem proves this. Every property of $P_U$ (idempotency, self-adjointness, norm-decreasing) has a geometric reading via the best-approximation interpretation.

- **Bessel's Inequality** *(within this topic)* — Bessel's inequality is the direct corollary of the best-approximation theorem applied to orthonormal lists with $u = 0$. It says $\|P_U v\| \leq \|v\|$, which in coordinates is $\sum |\langle v, e_k\rangle|^2 \leq \|v\|^2$. Bessel's inequality is also the infinite-dimensional foundation: in a Hilbert space, an orthonormal sequence gives partial sums $S_N(v) = \sum_{k \leq N} \langle v, e_k\rangle e_k$, and Bessel ensures convergence of $\sum |\langle v, e_k\rangle|^2$, hence convergence of the expansion.

- **Hilbert Projection Theorem** *(Functional Analysis)* — the best-approximation theorem generalizes to closed convex subsets of any Hilbert space: every closed convex $C \subseteq H$ has a unique closest point $P_C v$ to any $v \in H$. For closed subspaces, $P_C$ is linear and is the orthogonal projection. The proof uses the parallelogram law to show that a minimizing sequence is Cauchy and hence converges (by completeness). This generalization is the workhorse of variational calculus, convex optimization in infinite dimensions, and existence proofs in PDE theory.

- **Variational Calculus and the Calculus of Variations** *(Analysis)* — the variational principle "stationarity of $\|v - u\|^2$ over $u \in U$ gives $\langle v - u, w\rangle = 0$ for all $w \in U$" extends to non-quadratic functionals on Banach and Hilbert spaces. Euler-Lagrange equations are the first-order optimality conditions for such variational problems; the best-approximation theorem is the special case where the functional is the squared $L^2$-distance and the search space is a linear subspace.

- **Least Squares and Pseudoinverse** *(Linear Algebra XI)* — the least-squares solution $\hat x$ of $\min \|Ax - b\|^2$ has $A\hat x = P_{\operatorname{col} A} b$, the orthogonal projection of $b$ onto the column space. The pseudoinverse $A^\dagger$ implements this: $A^\dagger b =$ the minimum-norm $\hat x$. Every regression, every parameter-fitting problem in statistics and data analysis routes through the best-approximation theorem at this point.
