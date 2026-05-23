---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Bilinear Form"
  - "Def - Symmetric and Alternating Bilinear Form"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $M \in M_n(\mathbb{R})$ be a real $n \times n$ symmetric matrix, i.e., $M^t = M$. Define $\beta_M : \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ by

$$\beta_M(u, v) := u^t M v.$$

Show:

(a) $\beta_M$ is a [[Def - Bilinear Form|bilinear form]] on $\mathbb{R}^n$.
(b) $\beta_M$ is symmetric, i.e., $\beta_M(u, v) = \beta_M(v, u)$ for all $u, v$.
(c) The matrix of $\beta_M$ in the standard basis equals $M$.
(d) $\beta_M$ is **positive definite** (meaning $\beta_M(v, v) > 0$ for all $v \neq 0$) if and only if all eigenvalues of $M$ are positive.

**Recall:**

![[Def - Bilinear Form#The Definition]]

A bilinear form is symmetric if and only if its matrix in any basis (equivalently, some basis) is a symmetric matrix; see [[Def - Symmetric and Alternating Bilinear Form]]. **Positive definite** means $\beta(v, v) > 0$ for all $v \neq 0$.

The matrix $\mathcal{M}(\beta_M, (e_1, \dots, e_n))$ in the standard basis has $(i, j)$-entry $\beta_M(e_i, e_j) = e_i^t M e_j = M_{ij}$.

The **real spectral theorem** ([[Thm - Real Spectral Theorem]]) says that a real symmetric matrix $M$ has an orthonormal eigenbasis $(q_1, \dots, q_n)$ with real eigenvalues $\lambda_1, \dots, \lambda_n$, so $M = Q D Q^t$ where $Q$ has columns $q_i$ and $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$.

---

# Convergent Strategy

**Problem class.** This is a *direct verification* problem: check the definition of a bilinear form, recognise its matrix, and translate "positive definite" through the spectral decomposition. It is the foundational example of the bilinear-form-from-symmetric-matrix correspondence: every symmetric matrix gives a symmetric bilinear form on $\mathbb{R}^n$, and conversely. As the [[Linear Algebra IX — §9 Multilinear Algebra and Determinants#Problem-Solving Strategy|topic page strategy]] indicates, this is the level at which the formalism is built — it sits behind every $u^t M v$ computation in linear algebra, statistics, and physics.

**Assumption pattern.** We have a symmetric matrix $M$ (so $M^t = M$) and a defining formula $\beta_M(u, v) = u^t M v$. The assumption is rich because both bilinearity (separate linearity of $u^t$ and $v$) and the symmetry of $M$ feed into the conclusion. The positive-definite condition will then unlock via the real spectral theorem applied to $M$.

**Theorem routing.** Bilinearity of $u^t M v$ follows from properties of matrix multiplication (which distributes over addition and is compatible with scalar multiplication). Symmetry follows from the identity $u^t M v = v^t M^t u = v^t M u$ (using $M^t = M$). The matrix-of-$\beta_M$ computation is by definition: $\mathcal{M}(\beta_M)_{ij} = \beta_M(e_i, e_j) = e_i^t M e_j = M_{ij}$. The positive-definite criterion uses [[Thm - Real Spectral Theorem|real spectral theorem]]: $M = Q D Q^t$ with $D = \operatorname{diag}(\lambda_i)$, so $\beta_M(v, v) = v^t M v = v^t Q D Q^t v = (Q^t v)^t D (Q^t v) = \sum_i \lambda_i (Q^t v)^2_i$, which is positive iff all $\lambda_i > 0$.

**Key decision point.** The non-obvious move is in part (d): recognising that "positive definite for all $v$" must be translated into "all eigenvalues positive" via the spectral theorem. The temptation is to check positive-definiteness only on standard basis vectors $e_i$, which would give $M_{ii} > 0$ (a necessary condition) but not sufficient. The correct criterion is that all *eigenvalues* are positive, not all diagonal entries.

---

# Legal Operations Used

1. **Polarise / split a bilinear form into symmetric and alternating parts** (operation 2 from the topic page). The symmetry of $\beta_M$ is the content of $M^t = M$, so this operation directly characterises $\beta_M$.

2. **Diagonalise a symmetric bilinear form by an orthogonal change of basis** (operation 3 from the topic page). For part (d), we use the real spectral theorem to diagonalise $M$, converting "$\beta_M$ positive definite" into "all diagonal entries positive in the orthonormal eigenbasis".

3. **Apply Sylvester's law to read off the signature** (operation 4 from the topic page). Positive-definite is signature $(n, 0, 0)$ — equivalent to all eigenvalues positive.

---

# Hints

> [!note]- Hint 1
> For bilinearity: matrix multiplication $u^t M v$ is distributive over addition and compatible with scalar multiplication in both $u$ and $v$. Just expand $(\alpha u_1 + \beta u_2)^t M v$ and use the linearity of transpose plus matrix multiplication.

> [!note]- Hint 2
> For symmetry: compute $\beta_M(v, u) = v^t M u$ and rewrite using the transpose. Recall $(v^t M u)^t = u^t M^t v$, and the scalar $v^t M u$ equals its own transpose.

> [!note]- Hint 3
> For positive-definiteness, use the [[Thm - Real Spectral Theorem|real spectral theorem]]: $M = Q D Q^t$ with $Q$ orthogonal and $D$ diagonal containing eigenvalues. Then $\beta_M(v, v) = v^t M v = \|Q^t v\|_D^2 = \sum_i \lambda_i (Q^t v)_i^2$.

---

# Solution

The solution has four parts (a, b, c, d). Part (a) is bilinearity by matrix-multiplication distributivity; part (b) is symmetry via the transpose identity; part (c) is direct computation of the matrix; part (d) routes positive-definiteness through the spectral decomposition.

**Step 1: Bilinearity (part a).**

Each slot of $\beta_M(u, v) = u^t M v$ is linear.

> [!note]- Derivation
> Linearity in the first slot: for $u_1, u_2 \in \mathbb{R}^n$ and $\alpha, \beta \in \mathbb{R}$,
> $$\beta_M(\alpha u_1 + \beta u_2, v) = (\alpha u_1 + \beta u_2)^t M v = (\alpha u_1^t + \beta u_2^t) M v = \alpha u_1^t M v + \beta u_2^t M v = \alpha \beta_M(u_1, v) + \beta \beta_M(u_2, v).$$
> Linearity in the second slot: for $v_1, v_2 \in \mathbb{R}^n$ and $\gamma, \delta \in \mathbb{R}$,
> $$\beta_M(u, \gamma v_1 + \delta v_2) = u^t M (\gamma v_1 + \delta v_2) = \gamma u^t M v_1 + \delta u^t M v_2 = \gamma \beta_M(u, v_1) + \delta \beta_M(u, v_2).$$
> So $\beta_M$ is bilinear.

**Step 2: Symmetry (part b).**

Using $M^t = M$, $\beta_M(u, v) = \beta_M(v, u)$.

> [!note]- Derivation
> The quantity $\beta_M(u, v) = u^t M v$ is a $1 \times 1$ matrix, hence equal to its transpose:
> $$(u^t M v)^t = v^t M^t u = v^t M u = \beta_M(v, u),$$
> where the second equality uses $M^t = M$. Since $(u^t M v)^t = u^t M v$ (a scalar), we conclude $\beta_M(u, v) = \beta_M(v, u)$.

**Step 3: Matrix of $\beta_M$ equals $M$ (part c).**

Direct computation: $\mathcal{M}(\beta_M, (e_1, \dots, e_n))_{ij} = M_{ij}$.

> [!note]- Derivation
> By the definition of the matrix of a bilinear form ([[Def - Bilinear Form#The Definition|see the definition]]), the $(i, j)$-entry is $\beta_M(e_i, e_j)$. Compute:
> $$\beta_M(e_i, e_j) = e_i^t M e_j = M_{ij},$$
> by direct matrix-multiplication: $e_i^t M$ picks out the $i$-th row of $M$, and then dotting with $e_j$ picks out the $j$-th entry. So $\mathcal{M}(\beta_M, (e_1, \dots, e_n)) = M$.

**Step 4: Positive-definiteness iff all eigenvalues positive (part d).**

The real spectral theorem gives $M = Q D Q^t$ with $Q$ orthogonal and $D$ diagonal containing eigenvalues. Then $\beta_M(v, v) = \sum_i \lambda_i (Q^t v)_i^2$, which is positive for all $v \neq 0$ iff all $\lambda_i > 0$.

> [!note]- Derivation
> By the [[Thm - Real Spectral Theorem|real spectral theorem]], since $M$ is real symmetric, there exist an orthogonal matrix $Q$ (with $Q^t Q = I$) and a diagonal matrix $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ such that $M = Q D Q^t$. The $\lambda_i$ are the (real) eigenvalues of $M$.
>
> Compute $\beta_M(v, v) = v^t M v = v^t Q D Q^t v$. Let $w := Q^t v$; then $v^t Q = w^t$ and the expression becomes $w^t D w = \sum_i \lambda_i w_i^2$.
>
> The map $v \mapsto Q^t v$ is a bijection of $\mathbb{R}^n$ (since $Q$ is invertible, with $Q^{-1} = Q^t$), so as $v$ ranges over $\mathbb{R}^n \setminus \{0\}$, so does $w = Q^t v$.
>
> $\beta_M(v, v) > 0$ for all $v \neq 0$ iff $\sum_i \lambda_i w_i^2 > 0$ for all $w \neq 0$. The latter is equivalent to all $\lambda_i > 0$:
>
> - If all $\lambda_i > 0$: any $w \neq 0$ has some $w_i \neq 0$, and $\lambda_i w_i^2 > 0$ while all other terms are $\geq 0$, so the sum is $> 0$.
>
> - If some $\lambda_k \leq 0$: take $w = e_k$ (the standard basis vector). Then $\sum_i \lambda_i w_i^2 = \lambda_k \leq 0$, so the sum is not strictly positive. (Equivalently, taking $v = Q e_k$ gives $\beta_M(v, v) = \lambda_k \leq 0$ with $v \neq 0$.)
>
> Hence $\beta_M$ positive definite $\iff$ all eigenvalues of $M$ are positive.

> [!note]- Complete formal solution
> **(a) Bilinearity.** For $u_1, u_2, v \in \mathbb{R}^n$ and $\alpha, \beta \in \mathbb{R}$: $\beta_M(\alpha u_1 + \beta u_2, v) = (\alpha u_1 + \beta u_2)^t M v = \alpha u_1^t M v + \beta u_2^t M v = \alpha \beta_M(u_1, v) + \beta \beta_M(u_2, v)$. Linearity in the second slot is symmetric.
>
> **(b) Symmetry.** $\beta_M(u, v) = u^t M v$ is a scalar (a $1 \times 1$ matrix), so $(u^t M v)^t = u^t M v$. Also $(u^t M v)^t = v^t M^t u = v^t M u = \beta_M(v, u)$, using $M^t = M$. Combining, $\beta_M(u, v) = \beta_M(v, u)$.
>
> **(c) Matrix.** $\mathcal{M}(\beta_M, (e_1, \dots, e_n))_{ij} = \beta_M(e_i, e_j) = e_i^t M e_j = M_{ij}$, so $\mathcal{M}(\beta_M) = M$.
>
> **(d) Positive-definiteness.** By real spectral theorem, $M = Q D Q^t$ with $Q$ orthogonal and $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$. Setting $w = Q^t v$, $\beta_M(v, v) = w^t D w = \sum \lambda_i w_i^2$. Since $v \mapsto Q^t v$ is bijective, $\beta_M(v, v) > 0$ for all $v \neq 0$ iff $\sum \lambda_i w_i^2 > 0$ for all $w \neq 0$, which is equivalent to all $\lambda_i > 0$. $\blacksquare$

---

# Key Takeaways

**Symmetric matrices and symmetric bilinear forms are the same data, in finite [[Def - Dimension|dimensions]].** This exercise establishes the canonical bijection: every symmetric matrix $M$ gives a symmetric bilinear form $\beta_M(u, v) = u^t M v$, with matrix in the standard basis equal to $M$, and conversely every symmetric bilinear form on $\mathbb{R}^n$ has this form for a unique symmetric matrix. The "trigger" for this recognition is: whenever a problem asks about a symmetric bilinear form, you can convert to the matrix world (compute its matrix in some basis) and apply matrix techniques like diagonalisation or the spectral theorem; conversely, whenever a problem about a symmetric matrix asks about positive-definiteness or signature, you can interpret it as a bilinear-form question and apply Sylvester's law or polarisation. This translation is so fluid that experienced practitioners rarely write down which side they are on.

**Positive-definiteness of a symmetric bilinear form is governed by eigenvalues of its matrix.** The criterion "all eigenvalues positive" is the cleanest test for positive-definiteness — equivalent to "Sylvester signature $(n, 0, 0)$", to "$\beta_M(v, v) > 0$ for all $v \neq 0$", to "all leading principal minors positive" (Sylvester's criterion). The reasoning here connects positive-definiteness to spectral data via the real spectral theorem, and the key step is the change of variables $w = Q^t v$ which orthogonalises everything. This change of variables is one of the most-used tools in mathematical physics: it converts a coupled quadratic form (cross-terms $x_i x_j$) into an uncoupled one (only $x_i^2$ terms), which is precisely the normal-modes diagonalisation of coupled harmonic oscillators.

**The transpose identity $M = M^t$ propagates to the bilinear-form symmetry $\beta_M(u, v) = \beta_M(v, u)$ in two ways, both useful.** The first way is by direct calculation: $(u^t M v)^t = v^t M^t u = v^t M u$. The second is via the matrix-form coincidence: $\beta_M$ is symmetric iff its matrix in some basis is symmetric, and the matrix in the standard basis is $M$. The two arguments are equivalent — the first is an algebraic identity, the second is the symmetric-form-symmetric-matrix correspondence. Both should be in your toolkit, because the algebraic identity generalises cleanly to *any* bilinear form $u^t M v$ (with arbitrary, not necessarily symmetric $M$), telling you that the symmetric part of $\beta_M$ is $\beta_{\frac{1}{2}(M + M^t)}$ and the alternating part is $\beta_{\frac{1}{2}(M - M^t)}$ — the symmetrisation/antisymmetrisation in disguise.
