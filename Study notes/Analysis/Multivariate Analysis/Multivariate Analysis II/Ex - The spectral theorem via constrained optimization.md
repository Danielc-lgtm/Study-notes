---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Method of Lagrange Multipliers"
  - "Thm - First-Order Optimality Condition"
  - "Def - Critical Point, Hessian, and Definiteness"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $A \in \mathbb{R}^{n\times n}$ be a **symmetric** matrix. Prove the **spectral theorem**: there is an orthonormal basis $v_1, \dots, v_n$ of $\mathbb{R}^n$ consisting of eigenvectors of $A$, with real eigenvalues. Equivalently, there is an orthogonal matrix $O$ with $O^T A O$ diagonal.

Do this *analytically*, using only multivariable optimization. Specifically:

1. Show that extremising the quadratic form $q(x) = \langle x, Ax\rangle$ on the unit sphere produces, via Lagrange multipliers, an eigenvector of $A$ with a real eigenvalue.
2. Show that repeating this on the unit sphere intersected with the orthogonal complement of the eigenvectors already found produces a *new* eigenvector orthogonal to all of them.
3. Conclude that iterating $n$ times yields a full orthonormal eigenbasis.

**Recall:**

The objects in play are the symmetric matrix, the quadratic form, the constrained optimization, and Lagrange multipliers.

![[Thm - The Method of Lagrange Multipliers#Statement]]

By the [[Thm - The Method of Lagrange Multipliers|method of Lagrange multipliers]], at a local extremum of $q$ restricted to the constraint set $\{g_1 = \dots = g_m = 0\}$, the gradient $\nabla q$ is a linear combination of the constraint gradients $\nabla g_j$ (in the regular case). A **symmetric** matrix $A$ satisfies $\langle Ax, y\rangle = \langle x, Ay\rangle$ for all $x, y$, equivalently $A^T = A$. An **eigenvector** of $A$ is a nonzero $v$ with $Av = \mu v$ for some scalar $\mu$, the **eigenvalue**. Vectors are **orthonormal** if they are mutually orthogonal and each has unit length. The unit sphere $S^{n-1} = \{x : |x|^2 = 1\}$ is compact, so the Weierstrass theorem guarantees a continuous function attains its extrema on it.

The gradient of the quadratic form $q(x) = \langle x, Ax\rangle = \sum_{k,\ell}A_{k\ell}x_kx_\ell$ for symmetric $A$ is $\nabla q(x) = 2Ax$; the gradient of the constraint $g(x) = |x|^2 - 1$ is $\nabla g(x) = 2x$; and the gradient of a linear constraint $\ell_v(x) = \langle x, v\rangle$ is $\nabla\ell_v(x) = v$.

---

# Convergent Strategy

**Problem class.** This is a *constrained optimization used as a construction*: rather than asking for the value of an extremum, we use the Lagrange equation *itself* as the deliverable — the equation $\nabla q = \mu\nabla g$ will read $Ax = \mu x$, which is the eigenvector equation. The [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Problem-Solving Strategy|topic strategy]] notes that the multiplier often *is* the quantity of interest; here the multiplier is the eigenvalue.

**Assumption pattern.** Two features are essential. First, the sphere is *compact*, so $q$ attains a genuine maximum on it — the extremum exists, it is not assumed. Second, $A$ is *symmetric*, so $\nabla q = 2Ax$ (a non-symmetric $A$ would give $\nabla q = (A + A^T)x$ and the construction would produce eigenvectors of $A + A^T$, not $A$). Symmetry is also what makes the inductive step work: $A$ maps the orthogonal complement of an eigenvector back into itself.

**Theorem routing.** Step 1: extremise $q$ on $S^{n-1}$; Lagrange gives $2Ax = \mu\cdot 2x$, i.e. $Ax = \mu x$. Step 2: extremise $q$ on $S^{n-1} \cap \{x \perp v_1, \dots, v_k\}$; Lagrange now gives $2Ax = \mu\cdot 2x + \sum_j\lambda_j v_j$, and the symmetry of $A$ forces every $\lambda_j = 0$, recovering $Ax = \mu x$. Step 3: induction on the dimension.

**Key decision point.** The crux is the inductive step: when you extremise on the smaller sphere, the Lagrange equation carries *extra* terms $\sum\lambda_j v_j$ from the orthogonality constraints, and it is not obvious the new point is an eigenvector of $A$ at all. The decisive move is to take the inner product of the Lagrange equation with each $v_j$ and use *symmetry of $A$* together with the fact that the $v_j$ are *already eigenvectors* to show each $\lambda_j$ vanishes. This is where the symmetry hypothesis is genuinely consumed.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Legal Operations|the topic page's Legal Operations]]:

1. **Invoke Weierstrass on a compact set to guarantee an extremum exists.** The unit sphere (intersected with subspaces) is compact, so $q$ attains a maximum there.

2. **Set up the Lagrange equations on a constraint set.** Extremise $q$ subject to $|x|^2 = 1$ and the orthogonality constraints, producing $\nabla q = \mu\nabla g + \sum\lambda_j v_j$.

3. **Take inner products to extract scalar information.** Pair the Lagrange equation with each constraint gradient and use the symmetry of $A$ to kill the extra multipliers.

4. **Induct on dimension by passing to an orthogonal complement.** Each eigenvector found shrinks the search space by one dimension; symmetry keeps $A$ acting within the complement.

---

# Hints

> [!note]- Hint 1
> For a symmetric $A$, compute $\nabla q$ where $q(x) = \langle x, Ax\rangle$. Write $q = \sum_{k,\ell}A_{k\ell}x_kx_\ell$ and differentiate; the symmetry $A_{k\ell} = A_{\ell k}$ is what makes the two sums combine to $2Ax$.

> [!note]- Hint 2
> Extremise $q$ on $S^{n-1} = \{|x|^2 = 1\}$. The sphere is compact, so a maximum $v$ exists. The single constraint is $g(x) = |x|^2 - 1$ with $\nabla g = 2x$. Lagrange: $\nabla q(v) = \mu\nabla g(v)$. What does this say about $Av$?

> [!note]- Hint 3
> For the inductive step, suppose orthonormal eigenvectors $v_1, \dots, v_k$ (with $Av_j = \mu_j v_j$) are found. Extremise $q$ on $K = S^{n-1} \cap \{x : \langle x, v_j\rangle = 0,\ j = 1,\dots,k\}$ — still compact. The constraints are $|x|^2 = 1$ and $\langle x, v_j\rangle = 0$. Write out the full Lagrange equation: $2Av = 2\mu v + \sum_j\lambda_j v_j$.

> [!note]- Hint 4
> To kill the $\lambda_j$: take the inner product of $2Av = 2\mu v + \sum_j\lambda_j v_j$ with $v_j$. The left side is $2\langle Av, v_j\rangle = 2\langle v, Av_j\rangle$ (symmetry of $A$) $= 2\mu_j\langle v, v_j\rangle = 0$ (since $v \perp v_j$). The right side is $\lambda_j$ (since the $v_j$ are orthonormal and $v \perp v_j$). Hence each $\lambda_j = 0$, so $Av = \mu v$: a new eigenvector.

---

# Solution

The idea is that the eigenvector equation $Av = \mu v$ is *itself* a Lagrange-multiplier equation: it is the stationarity condition for the quadratic form $\langle x, Ax\rangle$ on the unit sphere, with $\mu$ playing the role of the multiplier. Compactness of the sphere supplies the extremum for free; symmetry of $A$ makes the gradient come out as $2Ax$ and, more subtly, makes the inductive step close.

**Step 1: The gradient of the quadratic form.**

For symmetric $A$, the quadratic form $q(x) = \langle x, Ax\rangle$ has gradient $\nabla q(x) = 2Ax$.

> [!note]- Derivation
> Write $q(x) = \sum_{k,\ell=1}^n A_{k\ell}x_kx_\ell$. Differentiating in $x_i$, the variable $x_i$ appears in the term $A_{k\ell}x_kx_\ell$ whenever $k = i$ or $\ell = i$:
> $$\partial_i q = \sum_{\ell}A_{i\ell}x_\ell + \sum_k A_{ki}x_k = (Ax)_i + (A^T x)_i.$$
> Since $A$ is symmetric, $A^T = A$, so $\partial_i q = 2(Ax)_i$, that is $\nabla q(x) = 2Ax$. (Had $A$ not been symmetric, the gradient would be $(A + A^T)x$ — the construction below would then produce eigenvectors of the symmetrized matrix.)

**Step 2: The base case — a first eigenvector.**

Extremising $q$ on the unit sphere $S^{n-1}$ produces a unit vector $v_1$ with $Av_1 = \mu_1 v_1$ for a real $\mu_1$.

> [!note]- Derivation
> The sphere $S^{n-1} = \{x : |x|^2 = 1\}$ is closed and bounded, hence compact, and $q$ is continuous, so by the Weierstrass theorem $q$ attains a maximum on $S^{n-1}$ at some point $v_1$. This is a local extremum of $q$ restricted to the constraint set $\{g = 0\}$ with $g(x) = |x|^2 - 1$.
>
> The constraint gradient is $\nabla g(x) = 2x$, which is nonzero on the sphere — so every point of $S^{n-1}$ is a *regular* constraint point. By the [[Thm - The Method of Lagrange Multipliers|method of Lagrange multipliers]] in its regular form, there is a multiplier $\mu_1$ with
> $$\nabla q(v_1) = \mu_1\nabla g(v_1), \qquad\text{i.e.}\qquad 2Av_1 = \mu_1\cdot 2v_1.$$
> Dividing by $2$: $Av_1 = \mu_1 v_1$. Since $v_1$ is a unit vector it is nonzero, so $v_1$ is an eigenvector of $A$ with eigenvalue $\mu_1 \in \mathbb{R}$. (Indeed $\mu_1 = \langle v_1, Av_1\rangle = q(v_1)$ is the *maximum* value of the quadratic form — the largest eigenvalue of $A$.)

**Step 3: The inductive step — a new orthogonal eigenvector.**

Suppose orthonormal eigenvectors $v_1, \dots, v_k$ have been found, with $Av_j = \mu_j v_j$, where $k < n$. Extremising $q$ on the unit sphere intersected with $\{v_1, \dots, v_k\}^\perp$ produces a unit vector $v_{k+1}$, orthogonal to all the $v_j$, with $Av_{k+1} = \mu_{k+1}v_{k+1}$.

> [!note]- Derivation
> Consider the constraint set
> $$K = \{x \in \mathbb{R}^n : |x|^2 = 1,\ \langle x, v_1\rangle = 0,\ \dots,\ \langle x, v_k\rangle = 0\}.$$
> $K$ is the intersection of the sphere with a linear subspace; it is closed and bounded, hence compact, and *non-empty* because $k < n$ leaves an $(n-k)$-dimensional complement, whose unit sphere is non-empty. So $q$ attains a maximum on $K$ at some point $v_{k+1}$.
>
> The constraints are $g(x) = |x|^2 - 1$ and $\ell_j(x) = \langle x, v_j\rangle$ for $j = 1,\dots,k$, with gradients $\nabla g = 2x$ and $\nabla\ell_j = v_j$. At $v_{k+1}$ these gradients are $\{2v_{k+1}, v_1, \dots, v_k\}$ — and they are linearly independent (the $v_j$ are orthonormal and $v_{k+1} \perp v_j$ is orthogonal to all of them and nonzero). So $v_{k+1}$ is a regular constraint point, and the [[Thm - The Method of Lagrange Multipliers|method of Lagrange multipliers]] gives multipliers $\mu, \lambda_1, \dots, \lambda_k$ with
> $$\nabla q(v_{k+1}) = \mu\nabla g(v_{k+1}) + \sum_{j=1}^k\lambda_j\nabla\ell_j(v_{k+1}),$$
> that is,
> $$2Av_{k+1} = 2\mu v_{k+1} + \sum_{j=1}^k\lambda_j v_j. \tag{$\star$}$$
>
> Now extract the $\lambda_j$. Fix an index $j$ and take the inner product of ($\star$) with $v_j$:
> $$2\langle Av_{k+1}, v_j\rangle = 2\mu\langle v_{k+1}, v_j\rangle + \sum_{i=1}^k\lambda_i\langle v_i, v_j\rangle.$$
> The right side simplifies: $\langle v_{k+1}, v_j\rangle = 0$ because $v_{k+1} \in K$, and $\langle v_i, v_j\rangle = \delta_{ij}$ because the $v_i$ are orthonormal — so the right side is $\lambda_j$.
> The left side simplifies using *symmetry of $A$* and the fact that $v_j$ is *already an eigenvector*:
> $$2\langle Av_{k+1}, v_j\rangle = 2\langle v_{k+1}, Av_j\rangle = 2\langle v_{k+1}, \mu_j v_j\rangle = 2\mu_j\langle v_{k+1}, v_j\rangle = 0.$$
> Therefore $\lambda_j = 0$. As $j$ was arbitrary, *every* $\lambda_j$ vanishes, and ($\star$) collapses to
> $$2Av_{k+1} = 2\mu v_{k+1} \quad\Longrightarrow\quad Av_{k+1} = \mu v_{k+1}.$$
> So $v_{k+1}$ is a unit eigenvector of $A$, orthogonal to $v_1, \dots, v_k$ by construction, with real eigenvalue $\mu_{k+1} := \mu$.

**Step 4: Conclusion by induction.**

Iterating the construction $n$ times yields an orthonormal eigenbasis $v_1, \dots, v_n$, proving the spectral theorem.

> [!note]- Derivation
> Step 2 produces $v_1$. Step 3, applied with $k = 1, 2, \dots, n-1$ in turn, produces $v_2, \dots, v_n$, each a unit eigenvector orthogonal to all previously found ones. After $n$ steps we have $n$ mutually orthogonal unit eigenvectors of $A$ — an orthonormal set of $n$ vectors in $\mathbb{R}^n$, hence an orthonormal *basis*. Each $v_j$ satisfies $Av_j = \mu_j v_j$ with $\mu_j \in \mathbb{R}$.
>
> Assembling the $v_j$ as the columns of a matrix $O$, orthonormality of the columns is exactly the statement $O^T O = I$, i.e. $O$ is orthogonal; and $AO = O\operatorname{diag}(\mu_1, \dots, \mu_n)$ rearranges to $O^T A O = \operatorname{diag}(\mu_1, \dots, \mu_n)$. So $A$ is orthogonally diagonalizable. $\blacksquare$

> [!note]- Complete formal solution
> Let $A = A^T \in \mathbb{R}^{n\times n}$ and $q(x) = \langle x, Ax\rangle$. Differentiating $q = \sum_{k\ell}A_{k\ell}x_kx_\ell$ and using $A_{k\ell} = A_{\ell k}$ gives $\nabla q(x) = 2Ax$.
>
> *Base case.* The unit sphere $S^{n-1}$ is compact, so $q$ has a maximum at some $v_1 \in S^{n-1}$. With $g(x) = |x|^2 - 1$, $\nabla g = 2x \neq 0$ on the sphere, [[Thm - The Method of Lagrange Multipliers|Lagrange's theorem]] gives $2Av_1 = \mu_1\cdot 2v_1$, so $Av_1 = \mu_1 v_1$, a real eigenvalue.
>
> *Inductive step.* Given orthonormal eigenvectors $v_1, \dots, v_k$ ($k < n$) with $Av_j = \mu_j v_j$, the set $K = S^{n-1} \cap \{v_1,\dots,v_k\}^\perp$ is compact and non-empty, so $q$ has a maximum at some $v_{k+1} \in K$. The constraint gradients $2v_{k+1}, v_1, \dots, v_k$ are independent, so Lagrange gives $2Av_{k+1} = 2\mu v_{k+1} + \sum_j\lambda_j v_j$. Pairing with $v_j$: the left side is $2\langle v_{k+1}, Av_j\rangle = 2\mu_j\langle v_{k+1}, v_j\rangle = 0$ by symmetry of $A$ and $v_{k+1} \perp v_j$; the right side is $\lambda_j$. Hence all $\lambda_j = 0$ and $Av_{k+1} = \mu v_{k+1}$.
>
> *Conclusion.* Iterating gives orthonormal eigenvectors $v_1, \dots, v_n$, an orthonormal basis. With $O = [v_1 | \cdots | v_n]$, $O^T O = I$ and $O^T A O = \operatorname{diag}(\mu_1, \dots, \mu_n)$. $\blacksquare$

---

# Key Takeaways

**A Lagrange multiplier is not always an auxiliary nuisance — sometimes it is the answer.** In a routine optimization the multiplier $\lambda$ is a byproduct, discarded once the extremal point is found. Here the entire point is that the multiplier *is* the eigenvalue: the Lagrange stationarity equation $\nabla q = \mu\nabla g$ unfolds to $Ax = \mu x$, the eigenvector equation, with $\mu$ the eigenvalue. Whenever a problem's deliverable is a *relation* of the form "vector $X$ is proportional to vector $Y$", the method of Lagrange multipliers is a candidate engine: set up an optimization whose stationarity condition is exactly that proportionality. This reframing — optimization as a *construction* rather than a measurement — recurs in deriving the Boltzmann distribution (multiplier = inverse temperature), the normal equations (multiplier = ...), and throughout the calculus of variations.

**Compactness is what gives the construction something to work with.** The eigenvector $v_1$ is produced as the *maximizer* of $q$ on the sphere, and that maximizer exists only because the sphere is compact and $q$ continuous. There is no algebra here, no characteristic polynomial — the existence of an eigenvector is wrung purely from the Weierstrass theorem. This is the analytic proof of the spectral theorem, and its lesson is general: when you need to *produce* an object satisfying a stationarity condition, package it as the extremum of a continuous function on a compact set, and compactness manufactures it. The same idea underlies the analytic proof of the fundamental theorem of algebra (minimise $|f(z)|$ on a large disc) and the existence of geodesics (minimise length).

**Symmetry of $A$ is consumed twice, and the second use — in the inductive step — is the subtle one.** The first use is visible: symmetry makes $\nabla q = 2Ax$ rather than $(A + A^T)x$. The second is where the proof genuinely turns. In the inductive step the Lagrange equation carries parasitic terms $\sum\lambda_j v_j$ from the orthogonality constraints, and a priori the new point need not be an eigenvector of $A$ at all. The terms are killed by pairing the equation with each $v_j$ and computing $\langle Av_{k+1}, v_j\rangle = \langle v_{k+1}, Av_j\rangle$ — *this swap is symmetry of $A$* — and then using that $v_j$ is *already* an eigenvector so $Av_j = \mu_j v_j \perp v_{k+1}$. The deeper structural fact behind this is that a symmetric $A$ maps the orthogonal complement of an invariant subspace back into itself, which is what lets the induction descend cleanly. When an inductive argument must restrict an operator to a subspace, the operator's symmetry (or self-adjointness) is typically the hypothesis that keeps the subspace invariant.

**The construction is greedy, and the multipliers come out in decreasing order.** Each step *maximises* $q$ over the largest available sphere, so $\mu_1 = \max_{S^{n-1}}q$ is the largest eigenvalue, $\mu_2$ the largest on the orthogonal complement, and so on — the eigenvalues emerge sorted from largest to smallest. This is not incidental: it is the **Courant–Fischer / Rayleigh–Ritz** characterization of eigenvalues as successive constrained extrema of the Rayleigh quotient $\langle x, Ax\rangle/\langle x,x\rangle$, and it is the foundation of the variational methods that estimate eigenvalues in infinite-dimensional settings — quantum mechanics, vibration analysis, spectral graph theory. The trigger "I need the largest eigenvalue of a symmetric operator" should summon "maximise the Rayleigh quotient", and this exercise is the finite-dimensional prototype of that entire toolkit.
