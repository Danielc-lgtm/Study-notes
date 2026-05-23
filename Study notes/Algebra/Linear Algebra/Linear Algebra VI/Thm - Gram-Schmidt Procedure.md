---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
  - "Def - Orthogonal and Orthonormal Vectors"
  - "Def - Orthonormal Basis"
  - "Def - Linear Independence"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is an inner product space over $\mathbf{F}$. We use $v_1, \dots, v_m$ for an input list and $e_1, \dots, e_m$ (or $q_1, \dots, q_m$ in matrix notation) for the orthonormal output. The intermediate orthogonal-but-not-yet-normalized vectors are $f_1, \dots, f_m$. The notation registry is on [[Linear Algebra VI — §6 Inner Product Spaces]].

---

# Statement

> **Theorem (Gram-Schmidt Procedure).** Let $V$ be an inner product space, and let $v_1, \dots, v_m$ be a linearly independent list in $V$. Define $f_1 = v_1$, and for $k = 2, \dots, m$ inductively
> $$f_k = v_k - \frac{\langle v_k, f_1\rangle}{\|f_1\|^2} f_1 - \cdots - \frac{\langle v_k, f_{k-1}\rangle}{\|f_{k-1}\|^2} f_{k-1}.$$
> Then $f_k \neq 0$ for each $k$, and setting $e_k = f_k / \|f_k\|$ gives an orthonormal list $e_1, \dots, e_m$ in $V$ with
> $$\operatorname{span}(v_1, \dots, v_k) = \operatorname{span}(e_1, \dots, e_k) \qquad \text{for each } k = 1, \dots, m.$$

> **Corollary (Existence of orthonormal bases).** Every finite-dimensional inner product space has an orthonormal basis.

> **Corollary (Extension to orthonormal basis).** Every orthonormal list in a finite-dimensional inner product space can be extended to an orthonormal basis.

> **Corollary (QR factorization).** Every $A \in \mathbf{F}^{m \times n}$ with linearly independent columns can be written as $A = QR$, where $Q \in \mathbf{F}^{m \times n}$ has orthonormal columns and $R \in \mathbf{F}^{n \times n}$ is upper triangular with positive diagonal entries.

---

# Motivation

The Gram-Schmidt procedure is the **workhorse algorithm** of finite-dimensional inner-product-space theory. It answers a single question: given any linearly independent list, how do you produce an orthonormal list with the same span? The answer is constructive, inductive, and computationally explicit — at each step, subtract from $v_k$ its orthogonal projection onto the span of the already-orthonormalized vectors, then normalize.

The procedure exists because **inner product spaces have a natural geometric structure** (orthogonality, projection) that vector spaces alone do not. The construction is not available in a general vector space — there is nothing to "orthogonalize" without an inner product. With an inner product, the algorithm is forced: at each step, the only natural choice is the orthogonal projection, which is uniquely determined.

Three things make Gram-Schmidt foundational:

First, it **proves the existence of orthonormal bases**. Theorem: every finite-dimensional inner product space has an orthonormal basis. Proof: take any basis, apply Gram-Schmidt. The existence is constructive — you can actually compute the orthonormal basis, not just assert its existence.

Second, it **gives the QR factorization** of a matrix. Writing $v_k$ in terms of $f_1, \dots, f_k$ (or equivalently $e_1, \dots, e_k$) gives a triangular system: $v_k = c_{k1} e_1 + c_{k2} e_2 + \cdots + c_{kk} e_k$ with $c_{kj}$'s read off from the procedure. In matrix form $A = QR$, where $Q$ has the $e_k$'s as columns and $R$ is upper-triangular with the $c_{kj}$'s as entries. This factorization is the basis of one of the standard algorithms for solving least-squares problems and computing eigenvalues numerically.

Third, it **realizes any inner-product-space computation in an orthonormal basis**. Once you have Gram-Schmidt, every theoretical statement using "let $e_1, \dots, e_n$ be an orthonormal basis" is constructive — produce one by Gram-Schmidt. The procedure is the bridge from theoretical statements about orthonormal bases to practical computations.

The Gram-Schmidt procedure is also the **algorithm behind classical orthogonal polynomials**. Applied to $1, x, x^2, \dots$ on $[-1, 1]$ with $\langle f, g\rangle = \int fg$, it produces (up to normalization) the **Legendre polynomials**. With weight $e^{-x^2}$ on $\mathbb{R}$, it produces the **Hermite polynomials**. With weight $(1 - x^2)^{-1/2}$, the **Chebyshev polynomials**. Each classical family is "Gram-Schmidt applied to the monomials with a specific weight" — different weights produce different geometries, and hence different orthogonal polynomials.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is: a linearly independent list in an inner product space. The skill is recognising when a problem implicitly demands orthonormalization.

The first source is **a non-orthonormal basis with which you need to compute inner products**. Property $B$: you are given a basis but the basis is not orthonormal. Bridge: Gram-Schmidt produces an orthonormal basis with the same span, after which every inner-product computation becomes a clean sum-of-products with no Gram-matrix corrections.

The second source is **a finite-dimensional subspace $U \subseteq V$ given by its span**. Property $B$: $U = \operatorname{span}(v_1, \dots, v_m)$, where the $v_k$ may not be orthonormal (or even linearly independent). Bridge: Gram-Schmidt the $v_k$'s (after removing any linear dependence) to get an orthonormal basis of $U$, which is what you need for any orthogonal-projection computation $P_U v = \sum_k \langle v, e_k\rangle e_k$.

The third source is **a polynomial-approximation problem** on a specific function space. Property $B$: you want polynomials of degree $\leq n$ as a subspace, but the monomial basis $1, x, x^2, \dots, x^n$ is not orthonormal in any $L^2$-inner product. Bridge: Gram-Schmidt produces the appropriate orthogonal polynomials, which then serve as the orthonormal basis for the projection-onto-polynomials problem.

The fourth source is **a question about QR factorization**. Property $B$: you have a matrix $A$ with linearly independent columns and want to factor it as $A = QR$ with $Q$ orthonormal-column and $R$ upper-triangular. Bridge: Gram-Schmidt the columns of $A$; the $Q$ has the orthonormal output as columns, and $R$ has the projection coefficients as entries.

**Targets (Output Amplification)**

The conclusion is an orthonormal list with prescribed partial spans.

The first target is **existence of orthonormal bases**. Property $D$: given any basis. Combination: Gram-Schmidt produces an orthonormal one. This is the workhorse existence proof in inner-product-space theory.

The second target is the **QR factorization** $A = QR$. Property $D$: write each $v_k$ in terms of $e_1, \dots, e_k$ to get an upper-triangular relationship. Combination: $A = QR$ with $Q$ orthonormal-column and $R$ upper triangular with positive diagonal.

The third target is **orthogonal-projection coefficients in numerical computations**. Property $D$: once you have an orthonormal basis $e_1, \dots, e_m$ of $U$, projections are sums: $P_U v = \sum_k \langle v, e_k\rangle e_k$. Combination: Gram-Schmidt + projection-coefficient formula = a complete algorithm for least-squares fitting.

The fourth target is **classical orthogonal polynomials**. Property $D$: apply Gram-Schmidt to $1, x, x^2, \dots$ with a specific inner product (interval, weight function). Combination: produces Legendre, Hermite, Chebyshev, Laguerre — different inner products give different classical families, each with their own functional applications (quantum mechanics, signal processing, numerical analysis).

---

# Why Is It True

The intuition is geometric: **subtract from $v_k$ everything already accounted for by $e_1, \dots, e_{k-1}$, leaving only the new direction**.

At step $k$, you have an orthonormal list $e_1, \dots, e_{k-1}$ whose span is $\operatorname{span}(v_1, \dots, v_{k-1})$. The new vector $v_k$ is not in this span (linear independence). The vector $v_k$ has an orthogonal decomposition:
$$
v_k = P_{\operatorname{span}(e_1, \dots, e_{k-1})}(v_k) + (v_k - P_{\operatorname{span}(e_1, \dots, e_{k-1})}(v_k))
$$
where the first summand is in $\operatorname{span}(e_1, \dots, e_{k-1})$ and the second is orthogonal to it. The orthogonal-projection formula in an orthonormal basis gives
$$
P_{\operatorname{span}(e_1, \dots, e_{k-1})}(v_k) = \sum_{j=1}^{k-1} \langle v_k, e_j\rangle e_j = \sum_{j=1}^{k-1} \frac{\langle v_k, f_j\rangle}{\|f_j\|^2} f_j,
$$
and the orthogonal residual is $f_k = v_k - \sum_j \frac{\langle v_k, f_j\rangle}{\|f_j\|^2} f_j$. This residual is nonzero (because $v_k \notin \operatorname{span}(e_1, \dots, e_{k-1})$), it is orthogonal to all the previous $e_j$'s (by construction), and after normalizing $e_k = f_k/\|f_k\|$, we have a new orthonormal vector that extends the list while preserving the span.

**The one-liner mechanism: at each step, subtract the orthogonal projection of $v_k$ onto the span of previous orthonormal vectors, leaving the part of $v_k$ orthogonal to that span — which is the new direction added by $v_k$.**

The reason linear independence is essential: if $v_k$ were in $\operatorname{span}(v_1, \dots, v_{k-1})$, the residual $f_k$ would be zero (the projection would be all of $v_k$), and we could not normalize. Linear independence guarantees that each $v_k$ brings something genuinely new, hence each $f_k$ is nonzero.

The reason the partial spans match: by induction, $\operatorname{span}(e_1, \dots, e_{k-1}) = \operatorname{span}(v_1, \dots, v_{k-1})$ (induction hypothesis), and $f_k = v_k - \sum_j (\ldots) e_j$ is a linear combination of $v_k$ and $e_1, \dots, e_{k-1}$, hence is in $\operatorname{span}(v_1, \dots, v_k)$. Adding $e_k = f_k/\|f_k\|$ to the list keeps everything in $\operatorname{span}(v_1, \dots, v_k)$, and the new vector is not in the previous span, so [[Def - Dimension|dimensions]] match.

The procedure is **unique up to signs/phases**: an orthonormal list with the same partial spans and with $\langle v_k, e_k\rangle > 0$ for each $k$ is determined by the input list (LADR Exercise 6B.10).

---

# What Makes This Hard

The procedure is mechanical, but two errors are common.

First, **forgetting to normalize after orthogonalizing**. The intermediate vectors $f_k$ are orthogonal but not generally unit-length. The orthonormality requires the normalization step $e_k = f_k / \|f_k\|$. Skipping this leaves you with an orthogonal but not orthonormal list, which still satisfies "pairwise orthogonal" but fails $\|e_k\| = 1$.

Second, **using $f_j / \|f_j\|^2$ when the formula calls for $f_j / \|f_j\|^2 \cdot \langle v_k, f_j\rangle$**, or its orthonormal equivalent $e_j \langle v_k, e_j\rangle$. The two formulas are equivalent: $\frac{\langle v_k, f_j\rangle}{\|f_j\|^2} f_j = \frac{\langle v_k, f_j\rangle}{\|f_j\|} \cdot \frac{f_j}{\|f_j\|} = \langle v_k, e_j\rangle e_j$. So the procedure has two natural formulations: one using the un-normalized $f_j$'s (LADR's), one using the normalized $e_j$'s (Boyd's). They are equivalent up to where the normalization step is performed.

A third subtlety is **numerical stability**: the classical Gram-Schmidt procedure as described is numerically unstable in finite-precision arithmetic. The **modified Gram-Schmidt** rearranges the order of subtractions to achieve better stability. For theoretical work the classical version is fine; for numerical work, the modified version (or alternative algorithms like Householder reflections) is preferred.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Induction on $k$. At each step, subtract from $v_k$ its projection onto the span of the previous orthonormal vectors; the residual is nonzero (by linear independence) and orthogonal to that span (by construction). Normalize.

**Subgoal decomposition:**

1. **Base case ($k = 1$):** Set $f_1 = v_1$, $e_1 = v_1 / \|v_1\|$. Then $\{e_1\}$ is orthonormal and $\operatorname{span}(e_1) = \operatorname{span}(v_1)$.
   - *Hint:* a single nonzero vector divided by its norm is automatically a one-vector orthonormal list.
   - *Why needed:* starts the induction.

2. **Inductive step.** Assume $e_1, \dots, e_{k-1}$ is orthonormal with $\operatorname{span}(e_1, \dots, e_{k-1}) = \operatorname{span}(v_1, \dots, v_{k-1})$. Define $f_k = v_k - \sum_{j=1}^{k-1} \langle v_k, e_j\rangle e_j$. Then $f_k \neq 0$ and $f_k \perp e_j$ for each $j < k$.
   - *Hint:* nonzero because $v_k \notin \operatorname{span}(v_1, \dots, v_{k-1}) = \operatorname{span}(e_1, \dots, e_{k-1})$ (linear independence). Orthogonality by direct check: $\langle f_k, e_l\rangle = \langle v_k, e_l\rangle - \sum_j \langle v_k, e_j\rangle\langle e_j, e_l\rangle = \langle v_k, e_l\rangle - \langle v_k, e_l\rangle = 0$.
   - *Why needed:* extends the orthogonal list by one vector.

3. **Normalize.** Set $e_k = f_k / \|f_k\|$. Then $\|e_k\| = 1$, $e_k \perp e_j$ for $j < k$, and $e_k \in \operatorname{span}(v_1, \dots, v_k)$.
   - *Hint:* normalizing a nonzero vector gives a unit vector; orthogonality is preserved.
   - *Why needed:* completes the inductive step with a genuinely orthonormal new vector.

4. **Match partial spans.** Verify $\operatorname{span}(e_1, \dots, e_k) = \operatorname{span}(v_1, \dots, v_k)$.
   - *Hint:* $e_k$ is a linear combination of $v_k$ and $e_1, \dots, e_{k-1}$, hence in $\operatorname{span}(v_1, \dots, v_k)$. The two spans have the same [[Def - Dimension|dimension]] $k$ and one is contained in the other; hence they coincide.
   - *Why needed:* the partial-span condition in the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: Orthogonality of the residual
> **Statement:** Let $e_1, \dots, e_{k-1}$ be orthonormal and let $f_k = v_k - \sum_{j=1}^{k-1} \langle v_k, e_j\rangle e_j$. Then $\langle f_k, e_l\rangle = 0$ for every $l \in \{1, \dots, k-1\}$.
>
> **Hint:** Apply $\langle \cdot, e_l\rangle$ directly and use orthonormality: $\langle e_j, e_l\rangle = \delta_{jl}$.
>
> **Why needed:** The residual being orthogonal to the previous orthonormal vectors is the entire reason Gram-Schmidt builds an orthonormal list.
>
> > [!note]- Full proof
> > $$\langle f_k, e_l\rangle = \langle v_k, e_l\rangle - \sum_{j=1}^{k-1} \langle v_k, e_j\rangle \langle e_j, e_l\rangle.$$
> > By orthonormality, $\langle e_j, e_l\rangle = \delta_{jl}$, so $\sum_j \langle v_k, e_j\rangle \delta_{jl} = \langle v_k, e_l\rangle$ (only the $j = l$ term survives). Hence $\langle f_k, e_l\rangle = \langle v_k, e_l\rangle - \langle v_k, e_l\rangle = 0$.

> [!note]- Lemma 2: Non-vanishing of the residual
> **Statement:** If $v_1, \dots, v_m$ is linearly independent and $e_1, \dots, e_{k-1}$ is the Gram-Schmidt orthonormalization of $v_1, \dots, v_{k-1}$ (with matching partial spans), then $f_k = v_k - \sum_{j=1}^{k-1} \langle v_k, e_j\rangle e_j \neq 0$.
>
> **Hint:** If $f_k = 0$, then $v_k = \sum_j \langle v_k, e_j\rangle e_j \in \operatorname{span}(e_1, \dots, e_{k-1}) = \operatorname{span}(v_1, \dots, v_{k-1})$, contradicting linear independence.
>
> **Why needed:** Without this, we could not normalize $f_k$ to get $e_k$, and the procedure would terminate prematurely.
>
> > [!note]- Full proof
> > Suppose for contradiction $f_k = 0$. Then $v_k = \sum_{j=1}^{k-1} \langle v_k, e_j\rangle e_j$, a linear combination of $e_1, \dots, e_{k-1}$. By the induction hypothesis, $e_1, \dots, e_{k-1} \in \operatorname{span}(v_1, \dots, v_{k-1})$, so $v_k \in \operatorname{span}(v_1, \dots, v_{k-1})$ — contradicting the linear independence of $v_1, \dots, v_m$. Hence $f_k \neq 0$.

> [!note]- Lemma 3: Span preservation
> **Statement:** Under the same hypotheses, $\operatorname{span}(e_1, \dots, e_k) = \operatorname{span}(v_1, \dots, v_k)$.
>
> **Hint:** Show inclusion in both directions, then conclude equality by dimension count.
>
> **Why needed:** This is the partial-span statement that makes Gram-Schmidt useful — it ensures that the orthonormal output has the same span as the input at every stage.
>
> > [!note]- Full proof
> > *Inclusion $\operatorname{span}(e_1, \dots, e_k) \subseteq \operatorname{span}(v_1, \dots, v_k)$:* By induction, $e_1, \dots, e_{k-1} \in \operatorname{span}(v_1, \dots, v_{k-1}) \subseteq \operatorname{span}(v_1, \dots, v_k)$. And $e_k = f_k/\|f_k\|$ where $f_k = v_k - \sum_j \langle v_k, e_j\rangle e_j$ is a linear combination of $v_k$ and the previous $e_j$'s, hence in $\operatorname{span}(v_1, \dots, v_k)$.
> >
> > Both spans have dimension $k$ ($e_1, \dots, e_k$ being orthonormal hence linearly independent, $v_1, \dots, v_k$ being linearly independent by hypothesis). Since one contains the other and they have the same dimension, they are equal.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $v_1, \dots, v_m$ be linearly independent in an inner product space $V$. The Gram-Schmidt procedure produces an orthonormal list $e_1, \dots, e_m$ with $\operatorname{span}(v_1, \dots, v_k) = \operatorname{span}(e_1, \dots, e_k)$ for each $k$.
>
> *Proof.* We proceed by induction on $k$.
>
> **Base case ($k = 1$):** Set $f_1 = v_1$. Since $v_1 \neq 0$ (linear independence), $\|f_1\| > 0$ and $e_1 = f_1/\|f_1\|$ has $\|e_1\| = 1$. Trivially $\{e_1\}$ is orthonormal (a single unit vector), and $\operatorname{span}(e_1) = \operatorname{span}(v_1)$.
>
> **Inductive step:** Suppose $e_1, \dots, e_{k-1}$ is an orthonormal list with $\operatorname{span}(e_1, \dots, e_{k-1}) = \operatorname{span}(v_1, \dots, v_{k-1})$. Define
> $$f_k = v_k - \sum_{j=1}^{k-1} \langle v_k, e_j\rangle e_j.$$
> By Lemma 2, $f_k \neq 0$. By Lemma 1, $\langle f_k, e_l\rangle = 0$ for each $l < k$. Hence $e_k = f_k/\|f_k\|$ satisfies $\|e_k\| = 1$ and $\langle e_k, e_l\rangle = 0$ for $l < k$. Thus $e_1, \dots, e_k$ is orthonormal.
>
> By Lemma 3, $\operatorname{span}(e_1, \dots, e_k) = \operatorname{span}(v_1, \dots, v_k)$, completing the inductive step.
>
> By induction, the orthonormal list $e_1, \dots, e_m$ is constructed with the required partial-span property. $\qquad\blacksquare$
>
> **Corollary (existence of orthonormal bases).** Every finite-dimensional inner product space $V$ has an orthonormal basis.
>
> *Proof.* Choose any basis $v_1, \dots, v_n$ of $V$. Apply Gram-Schmidt to get an orthonormal list $e_1, \dots, e_n$ of length $n = \dim V$. Since orthonormal lists are linearly independent (see [[Ex - Orthonormal lists are linearly independent]]) and the list has length $\dim V$, it is a basis of $V$.
>
> **Corollary (extension to orthonormal basis).** Every orthonormal list $e_1, \dots, e_m$ in a finite-dimensional inner product space $V$ extends to an orthonormal basis.
>
> *Proof.* Extend $e_1, \dots, e_m$ to a basis $e_1, \dots, e_m, v_1, \dots, v_{n-m}$ of $V$. Apply Gram-Schmidt to this basis. By the Gram-Schmidt formula, the first $m$ vectors are unchanged (they are already orthonormal), and the procedure produces an orthonormal basis $e_1, \dots, e_m, f_1, \dots, f_{n-m}$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Classical orthogonal polynomials.** Apply Gram-Schmidt to $1, x, x^2, x^3, \dots$ in $C[-1, 1]$ with $\langle f, g\rangle = \int_{-1}^1 fg$. The result is, up to constants, the **Legendre polynomials** $P_n(x)$. The first few normalized Legendre polynomials are $P_0 = 1/\sqrt{2}$, $P_1 = \sqrt{3/2}\, x$, $P_2 = \sqrt{45/8}\,(x^2 - 1/3)$. See [[Ex - Legendre polynomials from Gram-Schmidt]]. Changing to weight $e^{-x^2}$ on $\mathbb{R}$ gives Hermite polynomials; weight $(1 - x^2)^{-1/2}$ on $[-1, 1]$ gives Chebyshev polynomials of the first kind. Different weights produce different classical families, each with its own functional applications.

**QR factorization for least squares.** The least-squares problem $\min_x \|Ax - b\|$ with $A \in \mathbb{R}^{m \times n}$ having linearly independent columns reduces, via $A = QR$, to $\min_x \|QRx - b\| = \min_x \|Rx - Q^T b\|$ (using orthogonality of $Q$). Since $R$ is square and invertible, the solution is $\hat x = R^{-1} Q^T b$ — computable by back-substitution. This is the **QR-based least-squares algorithm**, more numerically stable than the normal-equations approach $\hat x = (A^TA)^{-1}A^T b$.

**Schur decomposition for matrices.** Schur's theorem says every $n \times n$ complex matrix $A$ is unitarily similar to an upper-triangular matrix: $A = U T U^*$ with $U$ unitary and $T$ upper-triangular. The proof uses Gram-Schmidt to convert a basis of generalized eigenvectors (which gives an upper-triangular form in some basis) into an orthonormal basis (which gives an upper-triangular form in an *orthonormal* basis). This is a foundational result in eigenvalue theory.

**Numerical analysis of $\pi$.** The Gauss-Legendre algorithm for computing $\pi$ uses values of orthogonal polynomials at specific nodes — the **Legendre nodes** — which are the roots of Legendre polynomials. These polynomials are themselves the Gram-Schmidt orthogonalization of monomials. So the high-precision approximation of $\pi$ is, deep down, an application of Gram-Schmidt-derived special functions.

---

# Bridges

- **[[Def - Orthonormal Basis|Orthonormal Basis]]** — Gram-Schmidt is the constructive existence proof for orthonormal bases. Given any basis, Gram-Schmidt produces an orthonormal one. This is the entire mechanism behind "we may assume the basis is orthonormal" in proofs throughout the rest of the chapter and beyond.

- **[[Def - Orthogonal Projection|Orthogonal Projection]]** — each step of Gram-Schmidt computes an orthogonal projection (onto the span of the previous orthonormal vectors) and subtracts it. So Gram-Schmidt is "iterated orthogonal projection with subtraction": at each step, subtract the projection of the new vector onto the current orthonormal span, leaving the orthogonal residual.

- **QR factorization** *(Numerical Linear Algebra)* — the matrix form of Gram-Schmidt is $A = QR$, where the columns of $A$ become the columns of $Q$ (orthonormal) and the coefficients of the Gram-Schmidt decomposition become the entries of $R$ (upper triangular). The QR factorization is one of the fundamental numerical algorithms: it gives least-squares solutions, eigenvalue iterations (QR algorithm), and basis-orthogonalization for general linear algebra problems.

- **Schur decomposition** *(Linear Algebra VII)* — the [[Linear Algebra V — §4–5 Polynomials and Eigenvalues|upper-triangular-form theorem]] for complex operators says there is a basis in which the operator is upper-triangular. Gram-Schmidt upgrades this basis to an orthonormal one without losing the upper-triangular structure — this is **Schur's theorem**: every operator on a finite-dim complex inner product space has an upper-triangular matrix in some orthonormal basis. The result is the bridge from the eigenvalue-theory chapter to the spectral theory chapter.

- **Hilbert space generalization** *(Functional Analysis)* — Gram-Schmidt extends to any inner product space, and in separable Hilbert spaces it can be applied to any countable linearly independent family. The result is an orthonormal sequence with the same closed span. This is what produces orthonormal bases of separable Hilbert spaces like $L^2[-\pi, \pi]$, and it underlies the construction of wavelet bases, orthonormal polynomial bases for $L^2$ with various weights, and the explicit eigenfunctions of the harmonic oscillator (Hermite functions).
