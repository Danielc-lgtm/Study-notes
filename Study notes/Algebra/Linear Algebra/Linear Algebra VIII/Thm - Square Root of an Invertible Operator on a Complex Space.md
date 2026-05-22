---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Nilpotent Operator"
  - "Def - Generalized Eigenspace"
  - "Thm - Generalized Eigenspace Decomposition"
  - "Def - Invertibility and Isomorphism"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional nonzero vector space over $\mathbb{C}$ and $T \in \mathcal{L}(V)$. A **square root** of $T$ is an operator $R \in \mathcal{L}(V)$ with $R^2 = T$. We restrict to $\mathbf{F} = \mathbb{C}$ throughout: the result fails over $\mathbb{R}$ in general (the operator of multiplication by $-1$ on $\mathbb{R}$ has no square root in $\mathbb{R}$). Full registry on [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

---

# Statement

> **Theorem (Square root of an invertible operator on a complex space).** Suppose $V$ is a finite-dimensional complex vector space and $T \in \mathcal{L}(V)$ is invertible. Then $T$ has a square root: there exists $R \in \mathcal{L}(V)$ with $R^2 = T$.

> **Lemma (Identity plus nilpotent has a square root).** Suppose $N \in \mathcal{L}(V)$ is nilpotent. Then $I + N$ has a square root, given by the truncated Taylor series $\sqrt{1 + x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \frac{x^3}{16} - \cdots$ applied to $N$ — a finite sum because $N^{\dim V} = 0$.

The same template extends: every invertible operator on a complex space has a $k$th root for every positive integer $k$, and more generally $f(T)$ is well-defined for any function $f$ holomorphic on a neighbourhood of the spectrum.

---

# Motivation

For a complex number $z$, the existence of a square root is automatic: write $z = r e^{i \theta}$ in polar form, and $\sqrt z = \sqrt r e^{i \theta / 2}$ is a square root. (Two square roots actually: $\pm \sqrt r e^{i \theta / 2}$.) The number $0$ is the only exception, and even it has the trivial square root $0$ — but $0$ does not behave well: its square roots are not invertible.

The analogous question for operators is: does every $T \in \mathcal{L}(V)$ on a complex space have a square root? The answer is *no* in general — the operator $T(z_1, z_2, z_3) = (z_2, z_3, 0)$ on $\mathbb{C}^3$ has no square root, as you are asked to show in exercise 1 of §8C of LADR. The obstruction is precisely that this $T$ is *not invertible*: its only eigenvalue is $0$ and the operator is nilpotent. The theorem says invertibility is the *exact* obstruction: every invertible operator on a complex space has a square root.

Why is invertibility the right hypothesis? Because the analogue of the polar form $z = r e^{i \theta}$ for an operator $T$ is the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] $T = \bigoplus (\lambda_k I + N_k)$ — each piece is "scalar plus nilpotent". To take a square root of $\lambda_k I + N_k$, we want to factor out the scalar: $\lambda_k I + N_k = \lambda_k (I + N_k / \lambda_k)$. This factorisation requires $\lambda_k \neq 0$ — that is, $0$ is not an eigenvalue — which is exactly *invertibility*. Once the factorisation is in place, we take a square root of $\lambda_k$ (any complex square root works) and a square root of $I + N_k / \lambda_k$ (via the Taylor truncation lemma). Their product is a square root of the block.

The Taylor truncation lemma is the key piece of new technology. We motivate the formula by analogy with the complex Taylor series:
$$\sqrt{1 + x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \frac{x^3}{16} - \cdots = \sum_{j = 0}^{\infty} \binom{1/2}{j} x^j,$$
which converges for $|x| < 1$. If we substitute $x \to N$ for $N$ nilpotent, the *infinite* series becomes a *finite* sum (because $N^k = 0$ for $k$ large enough), and convergence is no longer a worry — it is a polynomial identity. The polynomial $1 + \frac{N}{2} - \frac{N^2}{8} + \cdots + \binom{1/2}{m-1} N^{m-1}$ has square $I + N$ exactly because the Taylor series of $(1 + x)^{1/2}$ has this property as a formal power series identity. The "convergence" worry of complex analysis is replaced by the "truncation" reality of finite dimensions.

This pattern — Taylor series in $x$, then truncate by nilpotence — works for any function $f$ holomorphic in a neighbourhood of the spectrum, not just $\sqrt{1 + x}$. So the square-root result is the prototype of the **holomorphic functional calculus** in finite dimensions: for any such $f$, $f(T)$ is well-defined, and the assignment $f \mapsto f(T)$ is a ring homomorphism from holomorphic functions to operators.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is "invertible operator on a complex space". The source-broadening question is when this hypothesis is met in a non-obvious way.

The first disguised source is **an operator with all eigenvalues nonzero**. Equivalently: an operator whose minimal polynomial has nonzero constant term, or whose characteristic polynomial has nonzero constant term, or whose determinant is nonzero. *Example problem:* show that the operator $T \in \mathcal{L}(\mathbb{C}^2)$ with matrix $\begin{pmatrix} 1 & 1 \\ 0 & 4 \end{pmatrix}$ has a square root. Direct: the eigenvalues are $1$ and $4$, both nonzero, so $T$ is invertible. By the theorem, $T$ has a square root.

The second disguised source is **the product of an invertible operator and another invertible**. *Example problem:* show that $ABA^{-1}$ has a square root whenever $B$ does. (Easy: if $B = S^2$ then $ABA^{-1} = AS^2 A^{-1} = (ASA^{-1})^2$, and $ASA^{-1}$ is the square root.) This is the *conjugation-equivariance* of the square root construction: square roots transport along similarity.

The third disguised source is **a positive operator on an inner product space**. Positive operators are invertible iff they are positive *definite*, in which case they have a unique positive square root (see [[Thm - Positive Operators Have a Unique Square Root]] from [[Linear Algebra VII — §7 Operators on Inner Product Spaces]]). The current theorem extends this to *all* invertible operators on a complex space — the square root is no longer unique, and is no longer positive in any natural sense, but it exists. The transferable lesson is that uniqueness is an inner-product-space phenomenon; existence is purely algebraic.

**Targets (Output Amplification)**

The bare conclusion is "a square root exists". Combined with other facts it does much more.

Combine with **the spectral mapping theorem**. If $R$ is a square root of $T$, then the eigenvalues of $R$ are square roots of the eigenvalues of $T$. (Reason: if $R v = \mu v$ then $T v = R^2 v = \mu^2 v$, so $\mu^2$ is an eigenvalue of $T$.) The further result $E$ is a way to compute the *spectrum* of a square root from the spectrum of $T$ — each eigenvalue $\lambda$ of $T$ contributes one of $\pm \sqrt \lambda$ to the spectrum of $R$, and which one depends on the choice of square root. There are at most $2^m$ square roots up to similarity (one binary choice per distinct eigenvalue), and more if some Jordan blocks are large.

Combine with the same template applied to **$k$th roots and the exponential function**. The proof generalises to $f(T)$ for any function $f$ holomorphic on a neighbourhood of the spectrum: $f(T)$ is defined by the same eigenvalue-by-eigenvalue + Taylor-truncation construction. The further result is the **holomorphic functional calculus** in finite dimensions, with explicit formulas: $T^{1/k}$ for any positive integer $k$ when $T$ is invertible; $\log T$ when $T$ has spectrum avoiding the negative real axis; $e^T$ for any $T$. *See* the [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces#Concept Map|chapter's concept map]] for the holomorphic functional calculus tip.

Combine with the **polar decomposition** (see [[Thm - Polar Decomposition]] in [[Linear Algebra VII — §7 Operators on Inner Product Spaces]]). On an inner product space, every operator factors as $T = U |T|$ where $U$ is unitary and $|T| = \sqrt{T^* T}$ is positive. The square-root theorem here is what makes $|T|$ well-defined. The further result is the decomposition of any operator into "rotation × scaling", an analogue of the polar form $z = e^{i \theta} |z|$ for complex numbers.

---

# Why Is It True

The intuition is the polar-form analogy. A complex number $z = r e^{i \theta}$ has square roots $\pm \sqrt r e^{i \theta / 2}$ — we split off the modulus and the phase, take the square root of each, and recombine. An operator $T$ on a complex space has a structural decomposition $T = \bigoplus (\lambda_k I + N_k)$ on its generalized eigenspaces, with $\lambda_k$ the "modulus-and-phase part" (a complex number) and $N_k$ the "nilpotent perturbation part". To take a square root, we factor out $\lambda_k$: write $\lambda_k I + N_k = \lambda_k (I + N_k / \lambda_k)$. This factorisation only works when $\lambda_k \neq 0$ — that is, $T$ invertible. Then a square root is the product of (a complex square root of $\lambda_k$) and (a square root of $I + N_k / \lambda_k$).

The genuinely *new* idea is how to compute a square root of $I + N$ for $N$ nilpotent. The slogan is: **substitute the nilpotent into the formal Taylor series of $\sqrt{1 + x}$**, getting a polynomial expression in $N$ that, miraculously, squares to $I + N$.

The miracle is not really miraculous — it is just the formal Taylor expansion of $\sqrt{1 + x}$. As a formal power series identity in $\mathbb{Q}[[x]]$,
$$\left(1 + \frac{x}{2} - \frac{x^2}{8} + \frac{x^3}{16} - \cdots\right)^2 = 1 + x.$$
This holds at the level of formal power series, with no convergence question. Now substitute $x = N$ for $N$ nilpotent: both sides become *polynomials* in $N$ (because $N^{\dim V} = 0$ truncates the series), and the identity remains true as a polynomial identity. The infinite sum becomes a finite truncation, and the identity is preserved.

**Mechanism summary: the Taylor series of $\sqrt{1 + x}$ as a formal power series in $\mathbb{Q}[[x]]$ specialises to a polynomial identity $(R)^2 = I + N$ when the variable is replaced by a nilpotent $N$, because nilpotence truncates infinite sums to finite ones.**

The same mechanism powers the $k$th-root, the exponential, and any other holomorphic-functional-calculus identity. It is one of those "rigid" facts that work because of formal power series identities, not because of any analytic content.

---

# What Makes This Hard

The conceptual content is clear; the genuine difficulty is in *executing* the truncated Taylor series. Students sometimes try to use a closed-form formula for the coefficients $a_k = \binom{1/2}{k}$, but the explicit formula is not needed — only the *existence* of the series and the property that the leading coefficient is $a_1 = 1/2$. The standard derivation in LADR §8C uses an ansatz $R = I + a_1 N + a_2 N^2 + \cdots + a_{m-1} N^{m-1}$ with $m$ such that $N^m = 0$, computes $R^2 = I + 2 a_1 N + (2 a_2 + a_1^2) N^2 + \cdots$, and solves $2 a_1 = 1$, $2 a_2 + a_1^2 = 0$, etc. recursively. The lesson is that **we do not need explicit formulas, only solvability of a recursive system**.

The second subtle point is *why* the invertibility hypothesis is needed. Students sometimes assume the theorem fails only for the zero operator, but the failure mode is more general: any operator whose generalized eigenspace at $0$ is non-trivial (i.e., any non-invertible operator) might fail to have a square root. The specific failure mode is **the wrong Jordan structure at $0$**: the operator $\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = J_3(0)$ has no square root, because a square root $R$ would have to satisfy $R^2 = J_3(0)$, but $R^2$ has nilpotency index at most $\lceil 3/2 \rceil = 2 \neq 3$. (See exercise 1 of §8C in LADR for the explicit non-existence proof.)

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Two-step. First prove the lemma: $I + N$ has a square root for nilpotent $N$, by guessing the polynomial form and solving recursively. Then reduce the general invertible case to the lemma via the generalized eigenspace decomposition and the factorisation $\lambda I + N = \lambda(I + N/\lambda)$.

**Subgoal decomposition:**

1. **Step 0: precondition.** Verify that "invertible $T$" is equivalent to "$0$ is not an eigenvalue of $T$". The latter is the condition we will use to factor out scalars on each generalized eigenspace.
   - *Hint:* $T$ invertible iff $\ker T = \{0\}$ iff $0$ is not an eigenvalue.
   - *Why needed:* Without invertibility, $\lambda_k = 0$ for some $k$, and we cannot factor $\lambda_k I + N_k = \lambda_k (I + N_k / \lambda_k)$.

2. **Lemma — square root of $I + N$.** Prove that for $N$ nilpotent, $I + N$ has a square root.
   - *Hint:* Guess $R = I + a_1 N + a_2 N^2 + \cdots + a_{m-1} N^{m-1}$ where $m$ is the nilpotency index of $N$. Compute $R^2$, equate coefficients of $N^k$ with those of $I + N$, solve recursively.
   - *Why needed:* This is the workhorse — it shows how to take square roots in the "small" case where the operator is close to the identity.

3. **Reduction to the lemma.** For invertible $T$, on each generalized eigenspace $G(\lambda_k, T)$, write $T|_{G(\lambda_k, T)} = \lambda_k I + N_k = \lambda_k (I + N_k / \lambda_k)$ with $N_k = (T - \lambda_k I)|_{G(\lambda_k, T)}$ nilpotent. Apply the lemma to get a square root of $I + N_k / \lambda_k$. Multiply by a complex square root of $\lambda_k$ (any choice) to get a square root of $T|_{G(\lambda_k, T)}$.
   - *Hint:* The product of square roots is the square root of the product: if $A^2 = \lambda_k$ and $B^2 = I + N_k / \lambda_k$ then $(AB)^2 = A^2 B^2 = \lambda_k (I + N_k / \lambda_k) = T|_{G(\lambda_k, T)}$, provided $A$ and $B$ commute. Here $A = \sqrt \lambda_k \cdot I$ commutes with everything, so this works.
   - *Why needed:* Reduces each piece to the lemma.

4. **Assembly.** Combine the square roots on each generalized eigenspace into a square root of $T$.
   - *Hint:* By the generalized eigenspace decomposition, $V = \bigoplus G(\lambda_k, T)$. Define $R$ on each piece as the square root from step 3; on the whole space $R = \bigoplus R_k$. Verify $R^2 = T$ piece by piece.
   - *Why needed:* This is the final assembly into a global square root.

---

# Lemma Decomposition

> [!note]- Lemma 1 (LADR 8.39): Identity plus nilpotent has a square root
> **Statement:** Suppose $N \in \mathcal{L}(V)$ is nilpotent with $N^m = 0$. Then there exists $R \in \mathcal{L}(V)$ of the form $R = I + a_1 N + a_2 N^2 + \cdots + a_{m-1} N^{m-1}$ with $R^2 = I + N$.
>
> **Hint:** Compute $R^2 = I + 2 a_1 N + (2 a_2 + a_1^2) N^2 + (2 a_3 + 2 a_1 a_2) N^3 + \cdots$. Equate to $I + N$ to get the system $2 a_1 = 1$, $2 a_2 + a_1^2 = 0$, $2 a_3 + 2 a_1 a_2 = 0$, …, $2 a_k + (\text{polynomial in } a_1, \dots, a_{k-1}) = 0$ for $k \geq 2$. Solve recursively: $a_1 = 1/2$, $a_2 = -1/8$, $a_3 = 1/16$, etc.
>
> **Why needed:** This is the analytical heart of the theorem — the explicit construction of a square root for a near-identity operator.
>
> > [!note]- Full proof
> > Let $R = I + a_1 N + a_2 N^2 + \cdots + a_{m-1} N^{m-1}$ for coefficients $a_j$ to be determined. Computing $R^2$ term by term:
> > $$R^2 = I + 2 a_1 N + (2 a_2 + a_1^2) N^2 + (2 a_3 + 2 a_1 a_2) N^3 + \cdots + (2 a_{m-1} + \text{lower } a\text{'s}) N^{m-1},$$
> > where the higher terms $N^m, N^{m+1}, \dots$ vanish because $N^m = 0$.
> >
> > Setting $R^2 = I + N$ amounts to equating coefficients of $N^k$ on both sides:
> > - $N^0$: $1 = 1$. (automatic)
> > - $N^1$: $2 a_1 = 1$, so $a_1 = 1/2$.
> > - $N^2$: $2 a_2 + a_1^2 = 0$, so $a_2 = -a_1^2 / 2 = -1/8$.
> > - $N^3$: $2 a_3 + 2 a_1 a_2 = 0$, so $a_3 = -a_1 a_2 = -(1/2)(-1/8) = 1/16$.
> > - $N^k$ for $k = 4, \dots, m-1$: $2 a_k + (\text{polynomial in } a_1, \dots, a_{k-1}) = 0$, solving for $a_k$ recursively.
> >
> > At each step, the coefficient of $N^k$ on the left side of $R^2 = I + N$ is $2 a_k$ plus a polynomial in $a_1, \dots, a_{k-1}$, and on the right side it is $\delta_{k,1}$. So $a_k$ is uniquely determined by the previous $a$'s, and the recursion produces well-defined coefficients $a_1, a_2, \dots, a_{m-1}$.
> >
> > With these coefficients, $R^2 = I + N$, so $R$ is a square root of $I + N$.

> [!note]- Lemma 2: A square root of a scalar times an operator
> **Statement:** Suppose $\lambda \in \mathbf{F}$ and $S \in \mathcal{L}(V)$ with $S^2 = X$. Let $\mu \in \mathbf{F}$ be a square root of $\lambda$ (which exists when $\mathbf{F} = \mathbb{C}$). Then $\mu S$ is a square root of $\lambda X$.
>
> **Hint:** $(\mu S)^2 = \mu^2 S^2 = \lambda X$.
>
> **Why needed:** Lets us multiply a "small" square root (from Lemma 1) by a scalar square root to handle non-identity eigenvalues.
>
> > [!note]- Full proof
> > $(\mu S)^2 = \mu^2 S^2 = \lambda X$, using that $\mu^2 = \lambda$ and $S^2 = X$. So $\mu S$ is a square root of $\lambda X$.

> [!note]- Lemma 3 (LADR 8.41): Invertible operator on a complex space has a square root, generalized-eigenspace step
> **Statement:** Suppose $V$ is a complex vector space, $T \in \mathcal{L}(V)$ is invertible, and $\lambda_k$ is an eigenvalue of $T$. Then $T|_{G(\lambda_k, T)}$ has a square root.
>
> **Hint:** Write $T|_{G(\lambda_k, T)} = \lambda_k I + N_k = \lambda_k (I + N_k / \lambda_k)$ with $N_k = (T - \lambda_k I)|_{G(\lambda_k, T)}$ nilpotent and $\lambda_k \neq 0$ (since $T$ invertible). Apply Lemma 1 to get a square root $S$ of $I + N_k / \lambda_k$. Apply Lemma 2 with $X = I + N_k / \lambda_k$ and $\mu^2 = \lambda_k$.
>
> **Why needed:** This is the per-block construction of the square root.
>
> > [!note]- Full proof
> > Since $T$ is invertible, $0$ is not an eigenvalue, so $\lambda_k \neq 0$. Hence we can factor:
> > $$T|_{G(\lambda_k, T)} = \lambda_k I + N_k = \lambda_k (I + N_k / \lambda_k),$$
> > where $N_k = (T - \lambda_k I)|_{G(\lambda_k, T)}$ is nilpotent. (Recall from [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] (b) that $N_k$ is nilpotent.)
> >
> > Since $N_k / \lambda_k$ is also nilpotent, Lemma 1 gives a square root $S$ of $I + N_k / \lambda_k$: $S^2 = I + N_k / \lambda_k$.
> >
> > Let $\mu \in \mathbb{C}$ be a square root of $\lambda_k$ (any of the two complex square roots will do; pick one). By Lemma 2,
> > $$(\mu S)^2 = \mu^2 S^2 = \lambda_k (I + N_k / \lambda_k) = T|_{G(\lambda_k, T)}.$$
> > So $\mu S$ is a square root of $T|_{G(\lambda_k, T)}$.

> [!note]- Lemma 4: Square roots on direct summands assemble
> **Statement:** Suppose $V = V_1 \oplus \cdots \oplus V_m$ is a direct sum of $T$-invariant subspaces, and on each $V_k$ the operator $T|_{V_k}$ has a square root $R_k$. Then $T$ has a square root $R$ defined by $R|_{V_k} = R_k$ for each $k$.
>
> **Hint:** Define $R$ via the direct sum decomposition: every $v \in V$ has unique expression $v = v_1 + \cdots + v_m$ with $v_k \in V_k$, and set $R v = R_1 v_1 + \cdots + R_m v_m$. Then $R^2 v = R(R_1 v_1 + \cdots + R_m v_m) = R_1^2 v_1 + \cdots + R_m^2 v_m = T v_1 + \cdots + T v_m = T v$ (using that $R$ preserves each $V_k$ because $R|_{V_k} = R_k$, and $R_k^2 = T|_{V_k}$).
>
> **Why needed:** This is the assembly step from per-block to global.
>
> > [!note]- Full proof
> > Each $v \in V$ has a unique decomposition $v = v_1 + \cdots + v_m$ with $v_k \in V_k$, by the direct sum hypothesis. Define $R \in \mathcal{L}(V)$ by $R v = R_1 v_1 + \cdots + R_m v_m$. Since each $R_k$ is linear on $V_k$ and the decomposition is linear, $R$ is well-defined and linear.
> >
> > Note $R(V_k) = R_k(V_k) \subseteq V_k$, so $R$ preserves the decomposition and $R|_{V_k} = R_k$.
> >
> > Compute $R^2 v = R(R v)$. Since $R v = R_1 v_1 + \cdots + R_m v_m$ with $R_k v_k \in V_k$, $R^2 v = R(R_1 v_1) + \cdots + R(R_m v_m) = R_1^2 v_1 + \cdots + R_m^2 v_m = T|_{V_1}(v_1) + \cdots + T|_{V_m}(v_m) = T v_1 + \cdots + T v_m = T v$ (since $T$ also preserves the decomposition).
> >
> > So $R^2 = T$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V$ be a finite-dimensional complex vector space and $T \in \mathcal{L}(V)$ invertible.
>
> **Step 0 — precondition.** Since $T$ is invertible, $0$ is not an eigenvalue of $T$. So for every eigenvalue $\lambda_k$ of $T$, $\lambda_k \neq 0$.
>
> **Step 1 — generalized eigenspace decomposition.** By [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]], $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$ where $\lambda_1, \dots, \lambda_m$ are the distinct eigenvalues of $T$. Each $G(\lambda_k, T)$ is $T$-invariant.
>
> **Step 2 — square root on each generalized eigenspace.** Apply Lemma 3 to each generalized eigenspace $G(\lambda_k, T)$: there exists $R_k \in \mathcal{L}(G(\lambda_k, T))$ with $R_k^2 = T|_{G(\lambda_k, T)}$.
>
> **Step 3 — assemble.** By Lemma 4 applied to the decomposition in Step 1 with the square roots from Step 2, the operator $R \in \mathcal{L}(V)$ defined by $R|_{G(\lambda_k, T)} = R_k$ satisfies $R^2 = T$.
>
> Hence $T$ has a square root $R$. $\blacksquare$

The same template proves the general case: for any positive integer $k$, every invertible operator on a complex space has a $k$th root, obtained by replacing the Taylor series of $\sqrt{1 + x}$ with that of $(1 + x)^{1/k}$ in Lemma 1 and a complex $k$th root of $\lambda_j$ in Lemma 3.

---

# Cross-Field Exercise Suggestions

**Solving the heat equation on a finite-dimensional discretisation.** A discrete heat equation $\dot u = -L u$ on a graph (where $L$ is the graph Laplacian) is solved by $u(t) = e^{-tL} u_0$. To find a *time-reversed* solution (going from time $t$ to time $0$), one needs a square root of $e^{-tL}$, that is, $e^{-tL/2}$. The square root is computable by the present theorem: $e^{-tL}$ is invertible (eigenvalues $e^{-t \lambda_k}$ are nonzero), and the square root is $e^{-tL/2}$. The Jordan structure of $L$ controls the form of the square root.

**Logarithm of a rotation matrix in $\mathrm{SO}(n)$.** A rotation $R \in \mathrm{SO}(n)$ is the exponential of a skew-symmetric matrix $A \in \mathfrak{so}(n)$: $R = e^A$, and $A = \log R$. The logarithm exists because $R$ is invertible (with all eigenvalues on the unit circle in $\mathbb{C}$), and the same template — eigenvalue-by-eigenvalue plus Taylor truncation — gives the explicit formula. The applicability is more subtle here because the spectrum may include $-1$ (where $\log$ has a branch cut), but for rotations in $\mathrm{SO}(n)$ with no eigenvalue equal to $-1$, the construction goes through directly.

**Square root of a transition matrix.** For a Markov chain with transition matrix $P$, the "half-step" matrix $\sqrt P$ has $(\sqrt P)^2 = P$ and represents the chain run at half time. Existence of $\sqrt P$ is guaranteed by the theorem (when $P$ is invertible, which it is for nondegenerate chains), but interpretability is subtle: $\sqrt P$ may have negative or complex entries, so it is not a transition matrix in the probability sense. The mathematical existence is one thing; the probabilistic interpretation is another. The same theorem governs the question of "what is the half-iteration of a Markov chain".

---

# Bridges

- **[[Thm - Generalized Eigenspace Decomposition|Generalized Eigenspace Decomposition]]** — the structural input. The square root is computed block-by-block on the generalized eigenspaces.

- **[[Thm - Positive Operators Have a Unique Square Root|Square Root of Positive Operators]] in [[Linear Algebra VII — §7 Operators on Inner Product Spaces]]** — the inner-product-space version. On an inner product space, a positive operator has a unique *positive* square root. The current theorem extends to all invertible operators on a complex space, but at the cost of losing uniqueness and the "positive" property. The trade-off illustrates the role of the inner product structure in restoring uniqueness: without an inner product, square roots are not canonical.

- **Holomorphic Functional Calculus** — the meta-theorem of which the square root theorem is one instance. For any function $f$ holomorphic on a neighbourhood of the spectrum of $T$, the operator $f(T)$ is well-defined and is a polynomial in $T$ (in finite dimensions). The square root corresponds to $f(z) = \sqrt z$, the $k$th root to $f(z) = z^{1/k}$, the logarithm to $f(z) = \log z$, the exponential to $f(z) = e^z$. The construction is uniform: Taylor-expand $f$ at each eigenvalue, truncate by nilpotence on each generalized eigenspace, assemble.

- **Logarithm of an invertible operator** — same template, taking the Taylor series $\log(1 + x) = x - x^2/2 + x^3/3 - \cdots$ in place of $\sqrt{1 + x}$. Requires that the spectrum avoid the negative real axis (so that $\log$ has a well-defined value at each eigenvalue) — or more generally, that one can pick a branch of $\log$ on a neighbourhood of the spectrum. Important application: every operator close to the identity has a logarithm, giving the *Lie algebra–Lie group correspondence* in finite dimensions.

- **Matrix Exponential** — same template with $e^x = 1 + x + x^2/2! + \cdots$. Defined for any operator (no invertibility hypothesis needed), and central to ODE theory and Lie theory. See `[[Thm - Existence of Jordan Form]]` for the connection to explicit Jordan-block formulas for $e^{tA}$.

---

# Unlocked by This

> [!tip] $k$th Roots, Logarithms, and General Functional Calculus
> The same template — eigenvalue-by-eigenvalue + Taylor truncation — gives $T^{1/k}$ for any positive integer $k$ when $T$ is invertible, and $f(T)$ for any function $f$ holomorphic on a neighbourhood of the spectrum. This is the **holomorphic functional calculus** in finite dimensions, the matrix incarnation of the Cauchy integral formula.

> [!tip] Polar Decomposition *(from Linear Algebra VII)*
> The square-root theorem (in its positive-operator form, from [[Linear Algebra VII — §7 Operators on Inner Product Spaces]]) is what makes the polar decomposition $T = U |T|$ work: $|T| = \sqrt{T^* T}$ is defined via the positive-operator square root, and $U = T |T|^{-1}$ is the unitary "phase". The current theorem extends this to non-inner-product situations and to non-positive square roots.

> [!tip] Lie Algebra–Lie Group Correspondence *(from Lie Theory)*
> The exponential map $\exp : \mathfrak{gl}(V) \to \mathrm{GL}(V)$ has a local inverse $\log$ defined on a neighbourhood of the identity in $\mathrm{GL}(V)$. The logarithm of an invertible operator close to the identity is computable by the present-theorem template, and gives an explicit inverse to the exponential. Combined with the more general statement that every connected matrix Lie group is generated by exponentials of its Lie algebra, this builds the foundation for the Lie correspondence.

> [!tip] Heat Semigroup and Stochastic Calculus
> The fact that $e^{tL}$ has a square root $e^{tL/2}$ for any operator $L$ — equivalently, the heat semigroup $\{e^{-tL}\}_{t \geq 0}$ extends naturally to fractional times — is the operator-algebraic version of the **infinite divisibility** of the heat kernel. In stochastic calculus this corresponds to the Markov property and to the construction of Brownian motion as a continuous-time scaling limit of discrete random walks.
