---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Eigenvalue and Eigenvector"
  - "Def - Minimal Polynomial"
  - "Def - Direct Sum"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over a field $F$, $T \in \mathcal{L}(V)$ is an operator on $V$. The eigenspace of $T$ for $\lambda \in F$ is $E(\lambda, T) = \ker(T - \lambda I)$. The minimal polynomial is $m_T$. The matrix of $T$ in a basis $\mathcal{B}$ is $\mathcal{M}(T, \mathcal{B})$. The full registry is on the parent page [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]].

---

# Axiom Motivation

A diagonal matrix is the simplest possible matrix: each basis vector is sent to a scalar multiple of itself. **An operator is diagonalizable** if some choice of basis makes its matrix diagonal — equivalently, if $V$ admits a basis of eigenvectors of $T$. This is the simplest possible structural form for an operator, and the bulk of §5D is about deciding when it can be achieved.

Why is diagonalizability so desirable? Three reasons.

**Computational.** If $T$ has a diagonal matrix $\operatorname{diag}(\lambda_1, \ldots, \lambda_n)$ in a basis $v_1, \ldots, v_n$, then computing $T^k$ is trivial: in the same basis, $T^k$ has matrix $\operatorname{diag}(\lambda_1^k, \ldots, \lambda_n^k)$. More generally, $p(T)$ has matrix $\operatorname{diag}(p(\lambda_1), \ldots, p(\lambda_n))$ for any polynomial $p$. Diagonalisation reduces operator algebra to scalar algebra, applied component-wise.

**Conceptual.** A diagonalizable operator is *exactly* a direct sum of $\dim V$ commuting one-dimensional pieces. The decomposition $V = E(\lambda_1, T) \oplus \cdots \oplus E(\lambda_m, T)$ — when it exists — breaks $V$ into invariant [[Def - Subspace|subspaces]] on each of which $T$ acts as a single scalar. So a diagonalizable operator is one we *fully understand*: knowing the eigenvalues and eigenspaces is knowing everything.

**Dynamical.** For an operator governing some kind of dynamics — iteration, differential equations, Markov chains — diagonalization decouples the dynamics into independent one-dimensional modes. Each eigenvector evolves independently with its own scalar rate (decay, growth, oscillation), and the general solution is a sum of these modes. This is the foundation of the theory of linear differential equations and the spectral analysis of stochastic processes.

What is the right axiomatic content of "diagonalizable"? Three formulations turn out to be equivalent.

1. **Matrix form:** there is a basis in which $\mathcal{M}(T)$ is diagonal.
2. **Eigenvector basis:** there is a basis of $V$ consisting of eigenvectors of $T$.
3. **Eigenspace decomposition:** $V$ is the direct sum of the eigenspaces of $T$: $V = E(\lambda_1, T) \oplus \cdots \oplus E(\lambda_m, T)$, where $\lambda_1, \ldots, \lambda_m$ are the distinct eigenvalues.

The equivalence (1) $\iff$ (2) is immediate: a basis $v_1, \ldots, v_n$ gives a diagonal matrix iff each $v_k$ is an eigenvector. The equivalence (2) $\iff$ (3) uses [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent|the linear independence of eigenvectors with distinct eigenvalues]] in one direction (the sum of eigenspaces is automatically direct) and a [[Def - Dimension|dimension]] count in the other.

A fourth equivalent condition — and the one that matters most in practice — is:

4. **Minimal polynomial form:** $m_T$ is a product of **distinct** linear factors in $F[x]$.

This is the content of [[Thm - Conditions for Diagonalizability]]. It is the *practical* test for diagonalizability because it does not require finding eigenvectors. One can verify or refute "$m_T$ has distinct linear factors" by computing $m_T$ via the iterate algorithm, or by guessing a polynomial $p$ with distinct linear factors and checking $p(T) = 0$ (since $m_T \mid p$, the minimal polynomial inherits distinct linear factors).

A subtle but critical distinction: "distinct" matters. The operator $T$ on $\mathbb{F}^3$ given by $T(a, b, c) = (b, c, 0)$ has $m_T = x^3$ — a *repeated* linear factor — and is not diagonalizable. Even though $0$ is the only eigenvalue of $T$, the eigenspace $E(0, T) = \operatorname{span}(e_1)$ has [[Def - Dimension|dimension]] $1$, not $3$, so condition (3) fails: $V = E(0, T)$ would mean $V$ is one-dimensional, which it is not. The minimal polynomial $x^3$ has the factor $x$ with multiplicity $3$, and this multiplicity counts the failure of diagonalizability (specifically, the maximum Jordan block size).

Why insist on "distinct" linear factors and not just "linear factors"? Because the failure mode of diagonalizability is precisely the presence of a [[Thm - Jordan Normal Form|Jordan block]] of size $> 1$, which corresponds to a repeated linear factor in $m_T$. The operator $T(a, b, c) = (b, c, 0)$ has a single Jordan block of size $3$ at $0$; the minimal polynomial $x^3$ records this size, but the size $> 1$ is exactly what prevents diagonalizability. So "distinct linear factors" is the precise algebraic condition for "no Jordan block of size $> 1$ at any eigenvalue".

Why does the chapter not first define "diagonalizable" by condition (4)? Because (4) is the *theorem*, not the definition — the definition should be geometric (in terms of the basis or the eigenspace decomposition), with the polynomial condition derived as a *characterisation*. The definition tells you what the structure looks like; the characterisation tells you how to detect it.

A field-dependence remark: diagonalizability depends on the field. Over $\mathbb{R}$, a rotation has no real eigenvalues and is therefore not diagonalizable over $\mathbb{R}$; over $\mathbb{C}$, it has eigenvalues $e^{\pm i\theta}$ and *is* diagonalizable (since $m_T = (z - e^{i\theta})(z - e^{-i\theta})$ has distinct linear factors over $\mathbb{C}$). This is the same phenomenon as before — the field matters, and complexification can reveal diagonalizability hidden over the reals.

---

# The Definition

Let $V$ be a finite-dimensional vector space over $F$ and let $T \in \mathcal{L}(V)$.

**Diagonalizable operator.** $T$ is **diagonalizable** if $V$ has a basis consisting of eigenvectors of $T$. Equivalently, there is a basis with respect to which the matrix of $T$ is diagonal:
$$\mathcal{M}(T, (v_1, \ldots, v_n)) = \begin{pmatrix} \lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_n \end{pmatrix},$$
where $T v_k = \lambda_k v_k$ for each $k$.

**Equivalent characterizations.** Let $\lambda_1, \ldots, \lambda_m$ denote the distinct eigenvalues of $T$. The following are equivalent:

(a) $T$ is diagonalizable;
(b) $V$ has a basis consisting of eigenvectors of $T$;
(c) $V = E(\lambda_1, T) \oplus E(\lambda_2, T) \oplus \cdots \oplus E(\lambda_m, T)$;
(d) $\dim V = \dim E(\lambda_1, T) + \dim E(\lambda_2, T) + \cdots + \dim E(\lambda_m, T)$;
(e) The minimal polynomial $m_T$ factors as $(x - \lambda_1)(x - \lambda_2) \cdots (x - \lambda_m)$, a product of **distinct** linear factors over $F$.

The equivalence of (a)–(d) is immediate from the definitions plus [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent]]. The equivalence with (e) is the content of [[Thm - Conditions for Diagonalizability]].

---

# Categorical / Structural Definition

In the language of $F[x]$-[[Def - Module|modules]] — $V$ with $x$ acting as $T$ — diagonalizability is the condition that $V_T$ is **semisimple** as an $F[x]$-module, equivalently that $V_T$ is a direct sum of *simple* $F[x]$-[[Def - Module|modules]]. The simple $F[x]$-modules over an algebraically closed field $F$ are the one-dimensional modules $F[x]/(x - \lambda)$, one for each $\lambda \in F$; over a general $F$, they are $F[x]/(p)$ for $p$ a monic irreducible polynomial.

So "diagonalizable" means: $V_T$ decomposes as a direct sum of one-dimensional simple [[Def - Submodule|submodules]]. This is the simplest possible module structure on $V_T$ — every other operator has more complicated indecomposable summands (corresponding to Jordan blocks of size $> 1$ over an algebraic closure, or to higher-power irreducible factors over a general field).

The characterisation (e) above — $m_T$ has distinct linear factors — is the **square-free condition** on the [[Def - Annihilator|annihilator]] [[Def - Ideal|ideal]]: the [[Def - Ideal|ideal]] $(m_T)$ has $m_T$ a product of distinct primes, equivalent to $\gcd(m_T, m_T') = 1$ where $m_T'$ is the formal derivative. In module-theoretic terms, this is exactly the condition that the module $V_T$ is semisimple — Jacobson's theorem in the special case of modules over $F[x]$.

In the **structure theorem** decomposition $V_T \cong \bigoplus_k F[x]/(f_k)$ with $f_1 \mid \cdots \mid f_s$, diagonalizability is the condition that each invariant factor $f_k$ is a product of distinct linear factors. Equivalently, the **Smith normal form** of the presentation matrix of $V_T$ has only linear factors on the diagonal, no powers.

---

# Relate to Other Fields / Compression

**True name.** $T$ is diagonalizable iff $V$ **decomposes as a direct sum of one-dimensional invariant subspaces** — i.e. $V$ is "spanned by eigenvectors". Equivalently, $T$ acts as a scalar on each summand of a direct-sum decomposition of $V$. Operationally: a diagonalizable operator is one we can completely understand by understanding it scalar-by-scalar on a basis of eigenvectors.

In **functional analysis**, the analogue of diagonalizability for operators on Hilbert spaces is the **spectral theorem**: a self-adjoint (or more generally normal) operator on a Hilbert space is unitarily diagonalizable, equivalently has an orthonormal basis of eigenvectors. In infinite dimensions the "basis of eigenvectors" becomes a **direct integral** of eigenvectors against a measure, but the essential structure is the same. See [[Thm - Complex Spectral Theorem]] and [[Linear Algebra VII — §7 Operators on Inner Product Spaces]].

In **quantum mechanics**, the diagonalizability of self-adjoint operators (Hermitian observables) is the mathematical content of the fact that **physical observables have spectra of definite values** — the eigenvalues are the possible measurement outcomes, the eigenvectors are the stationary states. The spectral theorem is the workhorse of quantum mechanics.

In **statistics**, diagonalisation of covariance matrices is **principal component analysis** (PCA). The covariance matrix is symmetric (real symmetric or complex Hermitian), so the real/complex spectral theorem guarantees diagonalizability with real eigenvalues and orthogonal eigenvectors. The eigenvalues are the variances along the principal directions.

In **graph theory**, diagonalisation of the adjacency matrix is the heart of **spectral graph theory**. Eigenvalues encode connectivity, expansion, the chromatic number, and the number of walks of given length. For undirected graphs the adjacency matrix is symmetric, so diagonalisability is automatic.

In **dynamical systems**, diagonalisation of the linearisation $Df_{x_*}$ at a hyperbolic fixed point reveals the local dynamics: each eigenvalue $\lambda_k$ corresponds to an invariant direction on which the dynamics is one-dimensional with rate of contraction/expansion $|\lambda_k|$ (and rotation $\arg \lambda_k$). The **stable and unstable manifolds** at the fixed point are tangent to the sums of eigenvectors with $|\lambda| < 1$ and $|\lambda| > 1$ respectively — the geometric picture is **decoupled directions of contraction and expansion**.

---

# Examples / Corollaries

**Identity and scalar operators are diagonalizable.** $T = I$ has $m_T = x - 1$, a single linear factor — diagonalizable trivially (every basis is a basis of eigenvectors with eigenvalue $1$). Same for any scalar operator $T = \lambda I$. *(Calibration check.)*

**Projection: $T^2 = T$.** As discussed in [[Def - Minimal Polynomial]], a non-trivial projection has $m_T = x(x - 1)$, a product of two **distinct** linear factors. So projections are diagonalizable, with eigenvalues $0$ and $1$ and eigenspaces $\ker T$ (kernel) and $\operatorname{im} T$ (image). The decomposition $V = \ker T \oplus \operatorname{im} T$ is the standard direct-sum description of a projection.

**Involution: $T^2 = I$.** Then $m_T \mid x^2 - 1 = (x - 1)(x + 1)$, distinct linear factors. So $T$ is diagonalizable with eigenvalues $\pm 1$. (Over a field of characteristic $\neq 2$. In characteristic $2$, $(x - 1)(x + 1) = (x - 1)^2$, so the analysis is different.) The eigenspaces are $E(1, T)$ (fixed points) and $E(-1, T)$ (anti-fixed points), and $V = E(1, T) \oplus E(-1, T)$ via $v = \tfrac12(v + Tv) + \tfrac12(v - Tv)$.

**Finite-order operator over $\mathbb{C}$: $T^k = I$.** Then $m_T \mid x^k - 1 = \prod_{j=0}^{k-1}(x - \zeta^j)$ for $\zeta = e^{2\pi i / k}$. These are distinct linear factors over $\mathbb{C}$, so $T$ is diagonalizable. **Every operator of finite order on a complex vector space is diagonalizable.** This is one of the most useful applications: it gives diagonalizability of $S$-equivariant maps for finite [[Def - Group|groups]] $S$, the engine of representation theory.

**Diagonal matrix:** trivially diagonalizable, with the standard basis as the basis of eigenvectors and the diagonal entries as eigenvalues.

**Rotation in $\mathbb{R}^2$ by angle $\theta \in (0, \pi)$:** not diagonalizable over $\mathbb{R}$ (no real eigenvalues), diagonalizable over $\mathbb{C}$ (with eigenvalues $e^{\pm i\theta}$ and eigenvectors $(1, \pm i)$). The complexification trick brings real geometry into algebraic shape.

**Non-example: $T(a, b, c) = (b, c, 0)$ on $\mathbb{F}^3$ is not diagonalizable.** Here $T^3 = 0$ (each application kills one degree), and $T^2 \neq 0$ ($T^2(e_1) = e_3 \neq 0$… wait, let me recompute. $T(1, 0, 0) = (0, 0, 0)$, $T(0, 1, 0) = (1, 0, 0)$, $T(0, 0, 1) = (0, 1, 0)$. So $T^2(0, 0, 1) = T(0, 1, 0) = (1, 0, 0) \neq 0$, and $T^3(0, 0, 1) = T(1, 0, 0) = 0$. So $T^3 = 0$ and $T^2 \neq 0$, hence $m_T = x^3$.) The minimal polynomial $x^3$ has a *repeated* root $0$, so $T$ is not diagonalizable. Confirming directly: the only eigenvalue is $0$, and $E(0, T) = \ker T = \operatorname{span}(e_1)$ has dimension $1 \neq 3 = \dim V$. So condition (d) fails.

**Non-example: a non-projection idempotent... wait, that's a contradiction.** Let me think. Every idempotent is a projection. The non-diagonalizable non-trivial examples are exactly the operators with Jordan blocks of size $> 1$.

**Restriction of a diagonalizable operator is diagonalizable.** If $T$ is diagonalizable on $V$ and $U \leq V$ is $T$-invariant, then $T|_U$ is diagonalizable on $U$. Reason: $m_{T|_U} \mid m_T$, and divisors of products of distinct linear factors are themselves products of distinct linear factors. So diagonalizability is inherited by restrictions to invariant [[Def - Subspace|subspaces]].

**Calibration check.** If you have absorbed the definition: (a) for $T$ with $T^k = I$ over $\mathbb{C}$, you can compute the eigenvalues as $k$-th roots of unity and write down the diagonal form abstractly without picking specific matrices; (b) you recognise that the failure of diagonalizability is concentrated in repeated factors of $m_T$ — equivalently, in Jordan blocks of size $> 1$; (c) you can verify "the eigenspaces sum directly" without invoking the dimension count by using [[Thm - Eigenvectors with Distinct Eigenvalues are Linearly Independent]].

---

# Unlocked by This

> [!tip] Spectral Decomposition *(from Functional Analysis)*
> Diagonalizability is the **finite-dimensional prototype of the spectral theorem**: normal operators on a Hilbert space are diagonalizable with respect to an orthonormal basis. In the spectral theorem for self-adjoint operators on infinite-dimensional spaces, the discrete sum $V = \bigoplus E(\lambda_k, T)$ becomes a direct integral over the spectrum, but the essential idea — decomposing into invariant pieces on which $T$ acts as a scalar — is the same. See [[Thm - Real Spectral Theorem]], [[Thm - Complex Spectral Theorem]].

> [!tip] Principal Component Analysis *(from Statistics)*
> Diagonalisation of the **covariance matrix** of a dataset is the PCA decomposition. The covariance matrix is real symmetric, hence diagonalizable by the real spectral theorem; its eigenvectors are the principal components and its eigenvalues are the variances. PCA is the foundational dimensionality-reduction technique in statistics and machine learning.

> [!tip] Solving Linear ODEs via Eigenvalue Decomposition *(from Differential Equations)*
> A linear ODE $\dot x = Ax$ on $\mathbb{R}^n$ or $\mathbb{C}^n$ has solution $x(t) = e^{At} x(0)$. When $A$ is diagonalizable, $e^{At}$ is computable component-by-component in the eigenvector basis: $e^{At} v_k = e^{\lambda_k t} v_k$, and the general solution is a linear combination of these exponential modes. Diagonalizability decouples the system into independent one-dimensional ODEs.

> [!tip] Simultaneous Diagonalization *(from Linear Algebra V, §5E)*
> Two (or more) diagonalizable operators that commute can be **simultaneously diagonalized** — there is a basis in which all of them have diagonal matrices. This is the engine for decomposing the action of a commutative family of operators, and underlies the decomposition of representations of abelian groups into one-dimensional pieces.
