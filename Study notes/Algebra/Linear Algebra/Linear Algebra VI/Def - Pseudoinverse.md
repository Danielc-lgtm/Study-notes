---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Orthogonal Projection"
  - "Def - Orthogonal Complement"
tags: [algebra, linear-algebra]
---

# Notation

$V, W$ are finite-dimensional inner product spaces over $\mathbf{F}$. $T \in \mathcal{L}(V, W)$ is a linear map. The pseudoinverse is denoted $T^\dagger$ (read "$T$ dagger"). $T|_X$ is the restriction of $T$ to a subspace $X \subseteq V$. See [[Linear Algebra VI — §6 Inner Product Spaces]] for the full notation registry.

---

# Axiom Motivation

We have a linear map $T \in \mathcal{L}(V, W)$ and want to "invert" it. If $T$ is invertible — equivalently, bijective — then $T^{-1}$ exists and the equation $Tv = w$ has the unique solution $v = T^{-1}w$ for every $w$. But what if $T$ is not invertible? Two failures can occur:

1. $T$ is **not injective**: there are multiple $v$'s with $Tv = w$ for some $w$, so a "unique solution" doesn't exist.
2. $T$ is **not surjective**: there are $w$'s for which $Tv = w$ has no solution at all.

In applied mathematics, both failures happen all the time. A regression problem $Ax = b$ with more equations than unknowns is almost never solvable exactly (no surjectivity); a problem with more unknowns than equations has infinitely many solutions (no injectivity). The question is: what is the *best* substitute for an inverse?

The answer is the **pseudoinverse**, and the philosophy is to address each failure separately by orthogonal projection.

**Addressing non-surjectivity.** If $w \notin \operatorname{range} T$, the equation $Tv = w$ has no exact solution. The natural substitute is to find $v$ such that $Tv$ is as close as possible to $w$ — minimise $\|Tv - w\|$. By the [[Thm - Best Approximation by Orthogonal Projection|best-approximation theorem]], $Tv$ should be $P_{\operatorname{range} T} w$, the orthogonal projection of $w$ onto $\operatorname{range} T$. We have replaced "solve $Tv = w$" by "solve $Tv = P_{\operatorname{range} T} w$", which always has at least one solution because the right-hand side is in $\operatorname{range} T$ by construction.

**Addressing non-injectivity.** If $T$ is not injective, the equation $Tv = P_{\operatorname{range} T} w$ has multiple solutions, differing by elements of $\ker T$. To select a canonical one, we ask for the solution of **smallest norm**. By the same minimization principle, this is the solution lying in $(\ker T)^\perp$ — because any solution can be decomposed as a component in $\ker T$ (which we want to throw away to minimise norm) and a component in $(\ker T)^\perp$ (which we keep).

Combining: define $T^\dagger w$ to be the unique $v \in (\ker T)^\perp$ such that $Tv = P_{\operatorname{range} T} w$. This is the **pseudoinverse**.

There is one piece of well-definedness to check: the restriction $T|_{(\ker T)^\perp} : (\ker T)^\perp \to \operatorname{range} T$ must be an **isomorphism**. This is the content of LADR 6.67: the restriction is injective (its kernel is $(\ker T) \cap (\ker T)^\perp = \{0\}$) and surjective (every $w \in \operatorname{range} T$ comes from some $v$, and decomposing $v$ along $\ker T \oplus (\ker T)^\perp$ shows the component in $(\ker T)^\perp$ still maps to $w$). So the restriction is invertible, and the inverse is what feeds into the definition of $T^\dagger$.

The motivation is: an inner product gives orthogonal decompositions $W = \operatorname{range} T \oplus (\operatorname{range} T)^\perp$ and $V = \ker T \oplus (\ker T)^\perp$. The pseudoinverse uses both decompositions — orthogonal projection on the codomain side handles non-surjectivity, restriction to $(\ker T)^\perp$ on the domain side handles non-injectivity, and the residual restricted map is a genuine isomorphism. Without inner products, no such canonical choice exists; with them, the pseudoinverse is forced.

The properties are: $T^\dagger$ is the **unique** linear map $W \to V$ satisfying the four **Moore-Penrose conditions**:
1. $T T^\dagger T = T$.
2. $T^\dagger T T^\dagger = T^\dagger$.
3. $(T T^\dagger)^* = T T^\dagger$ (i.e., $T T^\dagger$ is self-adjoint).
4. $(T^\dagger T)^* = T^\dagger T$ (i.e., $T^\dagger T$ is self-adjoint).

Equivalently (and more illuminatingly): $T T^\dagger = P_{\operatorname{range} T}$ and $T^\dagger T = P_{(\ker T)^\perp}$. These two identities pin down what $T^\dagger$ is doing: composing with $T$ on either side gives orthogonal projections.

---

# The Definition

Let $V, W$ be finite-dimensional inner product spaces and $T \in \mathcal{L}(V, W)$. The **pseudoinverse** (also called the **Moore-Penrose inverse**) of $T$ is the linear map $T^\dagger \in \mathcal{L}(W, V)$ defined by

$$
T^\dagger w = (T|_{(\ker T)^\perp})^{-1}\, P_{\operatorname{range} T}\, w \qquad \text{for each } w \in W.
$$

Here $(T|_{(\ker T)^\perp}) : (\ker T)^\perp \to \operatorname{range} T$ is the restriction of $T$ to $(\ker T)^\perp$, which is an isomorphism, and $P_{\operatorname{range} T} : W \to W$ is the orthogonal projection of $W$ onto $\operatorname{range} T$.

Concretely:
- If $w \in (\operatorname{range} T)^\perp$, then $P_{\operatorname{range} T} w = 0$, so $T^\dagger w = 0$.
- If $w \in \operatorname{range} T$, then $T^\dagger w$ is the unique element of $(\ker T)^\perp$ such that $T(T^\dagger w) = w$.

**Algebraic properties (Moore-Penrose identities):**

1. **If $T$ is invertible, then $T^\dagger = T^{-1}$.** The pseudoinverse generalises the inverse.
2. $T T^\dagger = P_{\operatorname{range} T}$. The composition is the orthogonal projection of $W$ onto $\operatorname{range} T$.
3. $T^\dagger T = P_{(\ker T)^\perp}$. The composition is the orthogonal projection of $V$ onto $(\ker T)^\perp$.
4. $T T^\dagger T = T$.
5. $T^\dagger T T^\dagger = T^\dagger$.
6. $(T^\dagger)^\dagger = T$.

**Geometric properties (the best-fit interpretation):**

7. For any $w \in W$ and $v \in V$, $\|T(T^\dagger w) - w\| \leq \|Tv - w\|$, with equality iff $v \in T^\dagger w + \ker T$. So $T^\dagger w$ is a vector making $\|Tv - w\|$ smallest.
8. Among all $v$ with $\|Tv - w\|$ minimal, $T^\dagger w$ has the **smallest norm**.

The pair (best-fit + smallest-norm) is what makes the pseudoinverse the canonical "best substitute for the inverse" when $T$ is not invertible.

---

# Categorical / Structural Definition

The pseudoinverse is the **unique** linear map $T^\dagger \in \mathcal{L}(W, V)$ such that both $T T^\dagger$ and $T^\dagger T$ are orthogonal projections — equivalently, the unique map satisfying the four Moore-Penrose conditions. The map $T \mapsto T^\dagger$ is an involution on $\mathcal{L}(V, W) \sqcup \mathcal{L}(W, V)$ (swapping domain and codomain), and it specialises to ordinary inversion on invertible operators.

In matrix language (with $V = \mathbf{F}^n$, $W = \mathbf{F}^m$, $T$ represented by a matrix $A \in \mathbf{F}^{m \times n}$), the pseudoinverse $A^\dagger \in \mathbf{F}^{n \times m}$ exists for every matrix and equals: $A^{-1}$ if $A$ is square invertible; $(A^*A)^{-1}A^*$ if $A$ has linearly independent columns (full column rank); $A^*(AA^*)^{-1}$ if $A$ has linearly independent rows (full column rank from the other side); and the general case is computed via the **singular value decomposition** $A = U\Sigma V^*$, where $A^\dagger = V\Sigma^\dagger U^*$ and $\Sigma^\dagger$ is obtained from $\Sigma$ by reciprocating nonzero singular values. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the SVD.

---

# Relate to Other Fields / Compression

**The pseudoinverse is the unifying notion behind least squares.** For $A \in \mathbb{R}^{m \times n}$ and $b \in \mathbb{R}^m$, the **least-squares problem** is to minimise $\|Ax - b\|^2$. The solution is $\hat x = A^\dagger b$: this $\hat x$ both minimises $\|Ax - b\|$ over all $x$ (best fit) and has the smallest norm among all minimisers (canonical choice when the minimiser is not unique). When $A$ has linearly independent columns, $A^\dagger = (A^TA)^{-1}A^T$ and the solution is $\hat x = (A^TA)^{-1}A^T b$ — the **normal-equations** formula. The geometric interpretation: $A\hat x = AA^\dagger b = P_{\operatorname{col} A} b$ is the orthogonal projection of $b$ onto the column space of $A$. See [[Linear Algebra XI — Applied II — Least Squares]] for the full development.

**Generalization beyond Hilbert spaces.** The pseudoinverse is a Hilbert-space notion — it requires inner products on $V$ and $W$ to define $(\ker T)^\perp$ and $P_{\operatorname{range} T}$. For matrices, this is automatic (Euclidean inner products are standard). For more general settings (e.g., Banach spaces), the pseudoinverse may not exist, and one falls back on weaker notions like generalised inverses (which are unique only up to the kernel).

**True name:** the pseudoinverse is the unique linear map sending each $w \in W$ to "the smallest-norm best-fit solution of $Tv = w$". Algebraically, it is the unique map satisfying the Moore-Penrose conditions; geometrically, it solves the rank-deficient least-squares problem.

---

# Examples / Corollaries

**Is an instance: pseudoinverse of an invertible operator.** If $T : V \to V$ is invertible, then $\ker T = \{0\}$, so $(\ker T)^\perp = V$; $\operatorname{range} T = V$, so $P_{\operatorname{range} T} = I$. The pseudoinverse becomes $T^\dagger = T^{-1}$.

**Is an instance: pseudoinverse of an injective operator.** If $T : V \to W$ is injective but not surjective, then $\ker T = \{0\}$ and $(\ker T)^\perp = V$. $T$ restricted to $V$ is the original $T$, and $T^\dagger = (T)^{-1} P_{\operatorname{range} T}$ where $(T)^{-1}$ means the inverse on the range. Concretely, $T^\dagger T = I_V$ (the identity on $V$), but $T T^\dagger$ is the orthogonal projection onto $\operatorname{range} T$, not the identity on $W$.

**Is an instance: pseudoinverse of a surjective operator.** If $T : V \to W$ is surjective but not injective, then $\operatorname{range} T = W$ and $P_{\operatorname{range} T} = I$. The pseudoinverse is the inverse of $T$ on $(\ker T)^\perp$, extended trivially. We have $T T^\dagger = I_W$ but $T^\dagger T = P_{(\ker T)^\perp}$, not the identity.

**Is an instance: pseudoinverse of the matrix $A = \begin{pmatrix}1 & 1 & 1 & 0 \\ 0 & 0 & 2 & 1 \\ 0 & 0 & 0 & 0\end{pmatrix}$.** Following LADR 6.71: $\operatorname{range} A = \{(x, y, 0) : x, y \in \mathbb{R}\}$ and $\ker A = \operatorname{span}((-1, 1, 0, 0), (-1, 0, 1, -2))$. The pseudoinverse can be computed (after some algebra) to be
$$
A^\dagger = \tfrac{1}{11}\begin{pmatrix}5 & -2 & 0 \\ 5 & -2 & 0 \\ 1 & 4 & 0 \\ -2 & 3 & 0\end{pmatrix}.
$$
You can verify $AA^\dagger = P_{\operatorname{range} A}$ — the operator $(x, y, z) \mapsto (x, y, 0)$.

**Is an instance: pseudoinverse of the zero map.** If $T = 0$, then $\operatorname{range} T = \{0\}$, so $P_{\operatorname{range} T} = 0$, and $T^\dagger = 0$. The pseudoinverse of the zero map is the zero map.

**Is NOT an instance: a general right-inverse.** A map $S : W \to V$ with $TS = I_W$ is a right-inverse of $T$ (existence requires $T$ surjective). There can be many such $S$'s, differing by elements of $\mathcal{L}(W, \ker T)$. The pseudoinverse $T^\dagger$ is the specific right-inverse whose range is in $(\ker T)^\perp$ — the "canonical" right-inverse fixed by the inner product. Without the inner product, no canonical choice of right-inverse exists.

**Corollary (range and kernel of $T^\dagger$).** $\operatorname{range} T^\dagger = (\ker T)^\perp$ and $\ker T^\dagger = (\operatorname{range} T)^\perp$. These are precisely the orthogonal complements of $\ker T$ and $\operatorname{range} T$ — the pseudoinverse swaps the two pairs.

**Corollary (pseudoinverse of an orthogonal projection).** If $P \in \mathcal{L}(V)$ is an orthogonal projection, then $P^\dagger = P$. *Proof:* $P^2 = P$ and $P$ is self-adjoint, so checking the Moore-Penrose conditions $P P P = P$, $P P P = P$, $(PP)^* = P^* = P$, $(PP)^* = P^* = P$ — all satisfied. Hence $P^\dagger = P$ by uniqueness. An orthogonal projection is its own pseudoinverse.

**Calibration check.** Three verifications: (i) for $T = \operatorname{diag}(2, 0)$ on $\mathbb{R}^2$, compute $T^\dagger = \operatorname{diag}(1/2, 0)$ — reciprocate non-zero entries, leave zeros alone; (ii) verify the identity $T T^\dagger T = T$ for this example; (iii) check that the smallest-norm minimiser of $\|x\|$ subject to $Ax = b$ (for $b \in \operatorname{range} A$) is exactly $A^\dagger b$, by noting that any solution $x$ has $x - A^\dagger b \in \ker A$, hence the orthogonal decomposition $x = A^\dagger b + (\text{kernel component})$ has $\|x\|^2 = \|A^\dagger b\|^2 + \|(\text{kernel component})\|^2 \geq \|A^\dagger b\|^2$.

---

# Unlocked by This

> [!tip] Least Squares Solution via Pseudoinverse *(from Linear Algebra XI)*
> The least-squares problem $\min_x \|Ax - b\|^2$ has solution set $A^\dagger b + \ker A$; the minimum-norm solution is $x^* = A^\dagger b$. When $A$ has linearly independent columns, $A^\dagger = (A^TA)^{-1}A^T$ and the formula $x^* = (A^TA)^{-1}A^T b$ is the **normal-equations** solution. The geometric content — $Ax^*$ is the orthogonal projection of $b$ onto $\operatorname{col} A$ — is what makes the formula intuitive. Every regression, every parameter-fitting problem in data analysis routes through this. See [[Linear Algebra XI — Applied II — Least Squares]].

> [!tip] Singular Value Decomposition and Compact-Operator Theory *(from Linear Algebra VII / Functional Analysis)*
> The general formula for the pseudoinverse uses the **singular value decomposition** $T = U \Sigma V^*$, where $\Sigma$ is diagonal with non-negative entries (singular values). Then $T^\dagger = V \Sigma^\dagger U^*$, where $\Sigma^\dagger$ reciprocates the non-zero entries of $\Sigma$. This formula is robust, numerically stable, and extends to compact operators on Hilbert spaces (where the singular value decomposition exists in the form $T = \sum_k \sigma_k\, e_k\, \langle f_k, \cdot\rangle$ for orthonormal $\{e_k\}, \{f_k\}$ and decreasing singular values $\sigma_k \to 0$). The pseudoinverse via SVD is the gold standard for solving rank-deficient or ill-conditioned linear systems in applied mathematics.

> [!tip] Tikhonov Regularization *(from Inverse Problems and Machine Learning)*
> When $A$ is nearly rank-deficient, the pseudoinverse $A^\dagger$ becomes numerically unstable (small singular values blow up under reciprocation). **Tikhonov regularization** replaces the least-squares problem $\min \|Ax - b\|^2$ by $\min \|Ax - b\|^2 + \lambda \|x\|^2$ for a small $\lambda > 0$. The regularised solution is $(A^TA + \lambda I)^{-1} A^T b$, which converges to $A^\dagger b$ as $\lambda \to 0$ but is numerically stable for $\lambda > 0$. This connects the pseudoinverse to the modern theory of inverse problems, statistical regularisation, and ridge regression in machine learning.
