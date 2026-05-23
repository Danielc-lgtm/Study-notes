---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Positive Operator"
  - "Def - Self-Adjoint Operator"
  - "Thm - Complex Spectral Theorem"
  - "Thm - Real Spectral Theorem"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional [[Def - Inner Product Space|inner product space]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$. An operator $T \in \mathcal{L}(V)$ is [[Def - Positive Operator|positive]] if $T = T^*$ and $\langle Tv, v \rangle \geq 0$ for all $v$. The unique positive square root of a positive operator $T$ is denoted $\sqrt{T}$ or $T^{1/2}$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

---

# Statement

> **Theorem (Positive operators have a unique positive square root).** Let $T \in \mathcal{L}(V)$ be a positive operator. Then there exists a *unique* positive operator $R \in \mathcal{L}(V)$ such that $R^2 = T$. The operator $R = \sqrt{T}$ is constructed from the spectral decomposition: if $T = \sum_j \lambda_j P_j$, then $\sqrt{T} = \sum_j \sqrt{\lambda_j} P_j$.

This theorem extends to all five equivalent characterisations of positivity (via [[Def - Positive Operator]]), and the same construction yields the square root in each.

---

# Motivation

The motivating analogy is precise: a positive operator is to a non-negative real number what its square root is to the non-negative square root of that number. Just as $\sqrt{4} = 2$ unambiguously (rather than $\pm 2$), the positive operator square root is uniquely determined by the requirement that it be positive.

This result is the foundation for the **absolute value of an operator**: $|T| = \sqrt{T^* T}$, the unique positive square root of the positive operator $T^*T$. The absolute value $|T|$ is well-defined exactly because of this theorem. From $|T|$ we get the polar decomposition $T = U|T|$ (see [[Thm - Polar Decomposition]]), and from $|T|$'s eigenvalues we get the singular values of $T$ (see [[Def - Singular Values]]). The square root construction is therefore the bridge from "any operator" to "spectrally accessible data".

The theorem also provides the **Cholesky decomposition** (see [[Thm - Cholesky Factorization]]) — the existence of $T = R^* R$ with $R$ upper-triangular — and the operator analogue of "every non-negative real has a unique non-negative square root, in the same way that every positive operator has a unique positive square root".

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$T$ is positive". Sources include:

The first disguised source is **$T = S^* S$ for some operator $S$**. Then $T$ is positive (a calculation: $\langle T v, v \rangle = \|Sv\|^2 \geq 0$), and we can apply the theorem. *Example problem:* the operator $T^* T$ for any $T$ is positive — so $\sqrt{T^*T}$ exists uniquely; this gives the absolute value $|T|$ and underlies SVD.

The second disguised source is **a self-adjoint operator with non-negative eigenvalues**, which is the same condition viewed spectrally. *Example problem:* a covariance matrix in statistics has all eigenvalues $\geq 0$, so admits a unique positive square root used in the **whitening transformation** $X \mapsto \Sigma^{-1/2} (X - \mu)$.

The third disguised source is **a Gram matrix $G_{ij} = \langle v_i, v_j \rangle$**. Gram matrices are always positive; their square root is the matrix that realises the vectors as an isometric embedding. *Example problem:* for a set of vectors $v_1, \ldots, v_n$ in some Hilbert space, $\sqrt{G}$ acts on $\mathbb{F}^n$ to recover the geometry of the $v_i$.

**Targets (Output Amplification)**

The conclusion is "$\sqrt{T}$ exists and is unique".

Combine the conclusion with **the polar decomposition**: $T = U |T|$ where $|T| = \sqrt{T^*T}$. The further result $E$ is the universal factorisation "operator = isometry times positive", the matrix analogue of $z = e^{i\theta} |z|$. The existence of $|T|$ is supplied by this theorem.

Combine the conclusion with **operator inequalities**: $T \leq S$ implies $\sqrt{T} \leq \sqrt{S}$ — but only for positive $T, S$. The operator square root is **monotone**, in the Loewner order. The further result $E$ is the **Loewner–Heinz inequality**: for $\alpha \in [0, 1]$, $T \leq S$ implies $T^\alpha \leq S^\alpha$, but the inequality reverses direction for $\alpha > 1$ (or fails entirely) — a celebrated result of Heinz.

Combine the conclusion with **the Cauchy–Schwarz inequality for operators**: $|\langle Tv, w \rangle|^2 \leq \langle T v, v \rangle \langle T w, w \rangle$ for $T$ positive. Use $T = \sqrt{T}^2$ to write $\langle Tv, w \rangle = \langle \sqrt{T} v, \sqrt{T} w \rangle$, then apply standard Cauchy–Schwarz. The further result $E$ is the operator Cauchy–Schwarz, used extensively in operator inequality theory.

---

# Why Is It True

The existence is by direct construction: spectrally decompose $T = \sum \lambda_j P_j$, take square roots of eigenvalues, reassemble. The non-trivial content is **uniqueness**.

**The one-liner mechanism: any positive square root of $T$ must commute with $T$, hence is simultaneously diagonalised, hence is determined by its action on each eigenspace, where it must be multiplication by the non-negative square root.**

Why must a positive square root of $T$ commute with $T$? If $R^2 = T$, then $RT = R \cdot R^2 = R^3 = R^2 \cdot R = TR$. Commutativity is forced by squaring.

Why does this force unique diagonalisation? Two commuting normal operators share an orthonormal eigenbasis. So $R$ has the same eigenspaces as $T$. On each eigenspace $E(\lambda_j, T)$, $R$ acts as some positive operator $R_j$ with $R_j^2 = \lambda_j I_{E_j}$. Since $R_j$ is a positive operator with $R_j^2$ a positive scalar multiple of identity, $R_j$ is also a positive scalar multiple of identity: $R_j = \mu_j I_{E_j}$ with $\mu_j \geq 0$ and $\mu_j^2 = \lambda_j$, forcing $\mu_j = \sqrt{\lambda_j}$ (the non-negative square root). So $R = \sum \sqrt{\lambda_j} P_j$ is uniquely determined.

The uniqueness is *not* in the existence of *some* operator $R$ with $R^2 = T$ — there can be many (in 2D, $R^2 = I$ has infinitely many solutions among self-adjoint operators: any reflection!) — but in the uniqueness of the *positive* $R$. The positivity condition pins down the sign, exactly as $\sqrt{4} = 2$ (not $-2$) for real numbers.

---

# What Makes This Hard

The non-obvious step is **uniqueness**. Many operators square to a given positive operator; for example, $I = R^2$ has many self-adjoint solutions — $R = $ any orthogonal reflection. The positivity condition narrows this down to the unique non-negative square root. Forgetting that uniqueness requires the positivity of $R$ — not just that $R^2 = T$ — is the most common error.

The second subtlety is that **the square root is not analytic in $T$**. Two positive matrices that are close need not have close square roots if their eigenvalues are close to zero (the square root has infinite derivative at $0$). For positive *definite* operators (eigenvalues bounded away from zero), the square root is smooth in $T$; for merely positive (allowing zero eigenvalues), continuity holds but smoothness fails.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Construct $\sqrt T$ via the spectral decomposition. For uniqueness, observe that any positive square root must commute with $T$, hence shares the eigenbasis, hence is determined on each eigenspace.

**Subgoal decomposition:**

1. **Construction (existence).** Use the spectral theorem (on a self-adjoint, hence diagonalisable, $T$) to write $T = \sum \lambda_j P_j$. Define $R = \sum \sqrt{\lambda_j} P_j$.
   - *Hint:* The $\sqrt{\lambda_j}$ are well-defined because $\lambda_j \geq 0$.
   - *Why needed:* The constructed $R$ is the candidate; we then verify $R^2 = T$ and $R$ is positive.

2. **$R^2 = T$.** Verify by direct computation, using $P_i P_j = \delta_{ij} P_j$.
   - *Hint:* Multiply two such sums.

3. **$R$ is positive.** Verify by the spectral characterisation: $R$ is self-adjoint (real spectral decomposition with self-adjoint projections) and has non-negative eigenvalues $\sqrt{\lambda_j} \geq 0$.

4. **Uniqueness.** Suppose $R'$ is any positive operator with $(R')^2 = T$. Show $R' = R$.
   - *Hint:* From $(R')^2 = T$, $R'$ commutes with $T$. So $R'$ shares the eigenspaces of $T$. On each eigenspace, $R'$ is positive with $(R')^2 = \lambda I$, forcing $R' = \sqrt{\lambda} I$.

---

# Lemma Decomposition

> [!note]- Lemma 1: A positive operator $R$ with $R^2 = \lambda I$ is $\sqrt{\lambda} I$
> **Statement:** Let $R \in \mathcal{L}(V)$ be a positive operator with $R^2 = \lambda I$ for some $\lambda \geq 0$. Then $R = \sqrt{\lambda} I$.
>
> **Hint:** Diagonalise $R$ via the spectral theorem. The eigenvalues $\mu_j$ of $R$ satisfy $\mu_j^2 = \lambda$, and $\mu_j \geq 0$.
>
> **Why needed:** The key step in uniqueness — on each eigenspace of $T$, a positive square root is uniquely determined by the scalar action.
>
> > [!note]- Full proof
> > By the spectral theorem applied to the positive (hence self-adjoint) $R$, $R = \sum_j \mu_j Q_j$ with $\mu_j \geq 0$ and $Q_j$ orthogonal projections onto eigenspaces. Then $R^2 = \sum_j \mu_j^2 Q_j = \lambda I = \sum_j \lambda Q_j$. By uniqueness of the spectral decomposition (different projections cannot agree on different eigenspaces), $\mu_j^2 = \lambda$ for every $j$ with $Q_j \neq 0$, so $\mu_j = \sqrt{\lambda}$ for every $j$ (using $\mu_j \geq 0$). Hence $R = \sqrt{\lambda} \sum_j Q_j = \sqrt{\lambda} I$.

> [!note]- Lemma 2: A positive square root of $T$ commutes with $T$
> **Statement:** If $R \in \mathcal{L}(V)$ satisfies $R^2 = T$, then $RT = TR$.
>
> **Hint:** Direct: $RT = R \cdot R^2 = R^3 = R^2 \cdot R = TR$.
>
> **Why needed:** Commutation with $T$ lets $R$ be diagonalised in the same eigenbasis as $T$.
>
> > [!note]- Full proof
> > $RT = R \cdot R^2 = R^3$, and $TR = R^2 \cdot R = R^3$. So $RT = TR$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> **Step 0 — well-posedness.** The eigenvalues $\lambda_j$ of $T$ are non-negative (since $T$ is positive), so $\sqrt{\lambda_j}$ is well-defined as a non-negative real number.
>
> **Existence.** By the [[Thm - Complex Spectral Theorem|complex spectral theorem]] (or the [[Thm - Real Spectral Theorem|real spectral theorem]] over $\mathbb{R}$, where positivity implies self-adjointness), $T$ has spectral decomposition $T = \sum_j \lambda_j P_j$ with mutually orthogonal projections $P_j$ summing to $I$ and real $\lambda_j \geq 0$. Define
> $$R = \sum_j \sqrt{\lambda_j} P_j.$$
> Then $R$ is self-adjoint (each $P_j$ is, and $\sqrt{\lambda_j}$ is real). Its eigenvalues are $\sqrt{\lambda_j} \geq 0$, so $R$ is positive. And $R^2 = \sum_{i, j} \sqrt{\lambda_i \lambda_j} P_i P_j = \sum_j \lambda_j P_j = T$ (using $P_i P_j = \delta_{ij} P_j$).
>
> **Uniqueness.** Suppose $R'$ is any positive operator with $(R')^2 = T$. By Lemma 2, $R'$ commutes with $T$. Since $T = \sum_j \lambda_j P_j$ and $R'$ is normal (positive operators are normal), $R'$ shares the spectral projections of $T$: $R' = \sum_j \mu_j P_j$ for some $\mu_j$ (depending on $j$, with $\mu_j$ a positive operator on the eigenspace $E(\lambda_j, T)$, by the spectral theorem applied to the restriction).
>
> Wait, more carefully. Each eigenspace $E(\lambda_j, T)$ is invariant under any operator commuting with $T$ (because for $v \in E(\lambda_j, T)$, $T(R' v) = R'(Tv) = \lambda_j R' v$). So $R'$ restricts to an operator $R'|_{E(\lambda_j, T)}$, which is still positive. And $(R'|_{E_j})^2 = T|_{E_j} = \lambda_j I_{E_j}$. By Lemma 1, $R'|_{E_j} = \sqrt{\lambda_j} I_{E_j}$.
>
> Therefore $R'$ agrees with $R = \sum_j \sqrt{\lambda_j} P_j$ on every eigenspace, hence on $V$. So $R = R'$, proving uniqueness. $\blacksquare$

---

# Cross-Field Exercise Suggestions

1. **Statistics — Mahalanobis distance and whitening.** Given a covariance matrix $\Sigma$ (positive definite) of a random vector $X$, the **Mahalanobis distance** between two points is $d(x, y) = \sqrt{(x - y)^t \Sigma^{-1} (x - y)} = \|\Sigma^{-1/2}(x - y)\|$. The whitening transformation $X \mapsto \Sigma^{-1/2} (X - \mu)$ converts arbitrary correlated data to data with identity covariance. The existence and uniqueness of $\Sigma^{-1/2}$ rely on this theorem (applied to the positive operator $\Sigma^{-1}$).

2. **Quantum information — purification of mixed states.** A density matrix $\rho$ on $\mathcal{H}_A$ is positive with trace $1$. Its **purification** is a pure state $|\psi\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$ such that $\rho = \operatorname{tr}_B |\psi\rangle\langle\psi|$. One purification is $|\psi\rangle = \sum_j \sqrt{\lambda_j} |j\rangle_A \otimes |j\rangle_B$ where $\lambda_j$ are the eigenvalues of $\rho$. The square roots of eigenvalues are *the* essential ingredient, supplied by this theorem.

3. **PDE — heat semigroup and fractional Laplacian.** For a positive self-adjoint operator $A$ on a Hilbert space (e.g., $A = -\Delta$ with appropriate boundary conditions), the fractional power $A^{1/2}$ is well-defined and self-adjoint. It plays a central role in the **fractional Laplacian** $(-\Delta)^{1/2}$ — a non-local operator central to anomalous diffusion processes, fluid dynamics with long-range interactions, and Lévy stochastic processes.

4. **Differential geometry — exponential map of a positive symmetric matrix.** A positive definite symmetric matrix $A \in P_n(\mathbb{R})$ can be written as $A = e^X$ for a unique self-adjoint $X$ — the **matrix logarithm**. The set $P_n(\mathbb{R})$ has a Riemannian metric (the Karcher-Frechet mean), and the [[Def - Geodesic|geodesics]] in this metric are computed using matrix square roots: $\gamma(t) = A^{1/2}(A^{-1/2} B A^{-1/2})^t A^{1/2}$ is the [[Def - Geodesic|geodesic]] from $A$ to $B$. The existence of all the square roots in this formula is by this theorem.

---

# Bridges

- **[[Thm - Polar Decomposition]]** — The unique square root is what enables the polar decomposition $T = U |T|$, with $|T| = \sqrt{T^*T}$. The absolute value $|T|$ exists and is unique by this theorem applied to the positive operator $T^*T$.

- **[[Thm - Cholesky Factorization]]** — A different unique factorisation of a positive operator: $T = R^* R$ with $R$ upper-triangular. The factor $R$ is *not* in general the positive square root $\sqrt{T}$; the Cholesky $R$ is triangular (not self-adjoint), and is the unique such factor with positive diagonal. The positive square root is the self-adjoint factor.

- **Operator monotone functions** — A real-valued function $f$ on an interval $I \subseteq \mathbb{R}$ is **operator monotone** if $A \leq B$ implies $f(A) \leq f(B)$ for all self-adjoint operators with spectra in $I$. The function $f(x) = \sqrt{x}$ on $[0, \infty)$ is operator monotone (proved by integral representations), but $f(x) = x^2$ is not. The result that $\sqrt{\cdot}$ is operator monotone is one of the foundational facts of operator inequality theory.

- **Functional calculus** — The square root construction $\sqrt{T} = \sum \sqrt{\lambda_j} P_j$ is the **polynomial (or continuous) functional calculus** $\sqrt{\cdot}$ evaluated at $T$. The same construction defines $f(T)$ for any function $f$ on the spectrum, and this theorem is the special case $f(x) = \sqrt{x}$.

---

# Unlocked by This

> [!tip] Absolute Value of an Operator and the Polar Decomposition *(from Operator Theory)*
> The **absolute value** of an operator $T$ is $|T| = \sqrt{T^* T}$, a positive operator on $V$. By this theorem, $|T|$ exists uniquely for every $T$. The polar decomposition $T = U |T|$ (where $U$ is a partial isometry on $\operatorname{range} |T|$ and arbitrary elsewhere) is then the operator-theoretic analogue of $z = e^{i\theta} |z|$, with $|T|$ as the "magnitude" and $U$ as the "phase". The existence of $|T|$ is the foundational construction; everything else follows.

> [!tip] Loewner Order on Self-Adjoint Operators *(from Operator Theory)*
> Among self-adjoint operators, define the **Loewner order** by $T \leq S$ iff $S - T \geq 0$ (positive). This is a partial order, compatible with addition and non-negative scalar multiplication. The square root is **monotone with respect to the Loewner order**: $0 \leq T \leq S$ implies $\sqrt{T} \leq \sqrt{S}$. The square function, in contrast, is *not* monotone — there are operators with $0 \leq T \leq S$ but $T^2 \not\leq S^2$. The square root's monotonicity is non-trivial and is the key step in proving the **Loewner–Heinz inequality** $T \leq S \Rightarrow T^\alpha \leq S^\alpha$ for $\alpha \in [0, 1]$ — a deep result in operator inequality theory.

> [!tip] Bures Metric on Quantum States *(from Quantum Information)*
> The Bures (fidelity) distance between two density matrices $\rho$ and $\sigma$ is $d_B(\rho, \sigma) = \sqrt{2 - 2 F(\rho, \sigma)}$, where $F(\rho, \sigma) = \operatorname{tr}\sqrt{\sqrt{\rho} \sigma \sqrt{\rho}}$ is the **fidelity**. This expression uses iterated square roots of positive operators, well-defined by this theorem. The Bures metric is the quantum-information generalisation of the Wasserstein distance between probability distributions, and it endows the space of quantum states with a Riemannian structure whose curvature encodes geometric information about quantum measurement and estimation.
