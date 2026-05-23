---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Eigenvalue and Eigenvector"
  - "Def - Null Space and Range"
  - "Def - Linear Map"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional nonzero vector space over $\mathbf{F} \in \{\mathbb{R}, \mathbb{C}\}$ and $T \in \mathcal{L}(V)$ is a linear operator. We write $I$ for the identity on $V$, and for an operator $S$ we write $\operatorname{null} S$ for its null space (kernel). $T^k$ denotes the $k$-fold composition of $T$ with itself; $T^0 = I$. For $\lambda \in \mathbf{F}$ an eigenvalue of $T$ — meaning $(T - \lambda I)$ has nonzero kernel — the **eigenspace** is $E(\lambda, T) = \operatorname{null}(T - \lambda I)$. Full symbol registry is on [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

---

# Axiom Motivation

The issue this definition solves is a defeat for the eigenvector framework. In [[Linear Algebra V — §4–5 Polynomials and Eigenvalues]] we discovered that on a complex space every operator has at least one eigenvalue, and we hoped that by collecting enough eigenvectors we could write $V$ as a direct sum $\bigoplus_k E(\lambda_k, T)$ of eigenspaces and describe $T$ as diagonal in the corresponding basis. This hope is correct exactly when $T$ is diagonalisable, but it fails outright in simple examples. Consider $T(z_1, z_2) = (z_2, 0)$ on $\mathbb{C}^2$. The matrix of $T$ in the standard basis is $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, the only eigenvalue is $0$, and the eigenspace $E(0, T)$ is the one-dimensional span of $(1, 0)$. There are not enough eigenvectors to make a basis of $\mathbb{C}^2$, and the diagonal-basis hope dies. Yet $T$ is a perfectly nice operator on a small space — it must have some description.

What goes wrong is rigid: we are insisting on the equation $(T - \lambda I) v = 0$, which has too few solutions. The fix is to relax the requirement. Notice that $T^2 = 0$ for the example above, so $(T - 0 I)^2 = T^2$ annihilates *every* vector in $\mathbb{C}^2$. Even though only $(1, 0)$ is killed by $T$ itself, every vector is killed by $T^2$. If we agree to count a vector as "morally an eigenvector for $\lambda$" whenever some power of $(T - \lambda I)$ annihilates it, then $\mathbb{C}^2$ does have a basis of "morally eigenvectors" for the eigenvalue $0$ — for instance, the standard basis $(1, 0), (0, 1)$, since the first is in $\ker T$ and the second is in $\ker T^2$. This is the move that the definition encodes.

What is the right notion of "power"? Two options present themselves. One could ask "$(T - \lambda I)^k v = 0$ for some positive integer $k$" — the existential form — or one could fix a specific $k$, say $k = \dim V$, and ask "$(T - \lambda I)^{\dim V} v = 0$". The first is the obvious extension of the eigenvector definition; the second is computationally explicit. They turn out to be equivalent: the chain $\operatorname{null}(T - \lambda I)^0 \subseteq \operatorname{null}(T - \lambda I)^1 \subseteq \cdots$ of nested kernels stabilises by $k = \dim V$ at the latest (it adds at least one [[Def - Dimension|dimension]] at each strict inclusion, and is bounded above by $\dim V$), so once any power kills $v$, the $\dim V$-th power does. So the two definitions describe the same set of vectors, and we may use either one — the existential form for theoretical work, the explicit $\dim V$ form for computations. See `[[Thm - Null Spaces of Powers Stabilize]]` for the proof.

Why not allow $\lambda$ that is *not* an eigenvalue? One might define generalized eigenvalues by allowing any $\lambda \in \mathbf{F}$, asking only that $(T - \lambda I)^k v = 0$ for some nonzero $v$ and some $k$. But this is no relaxation at all: if $(T - \lambda I)^k$ is not injective, then $(T - \lambda I)$ itself is not injective (since the composition of injective maps is injective), so $\lambda$ is already an eigenvalue. The set of "generalized eigenvalues" would equal the set of ordinary eigenvalues, so the generalisation is empty. Generalized eigenvectors generalise the *vectors*, not the *values*.

Why insist on $v \neq 0$? The zero vector is killed by every operator, so $(T - \lambda I)^k \cdot 0 = 0$ for every $\lambda$ and $k$. If we allowed $v = 0$ then the "generalized eigenvector for $\lambda$" condition would be satisfied trivially by $0$, and the set of generalized eigenvectors for $\lambda$ would correspond to no $\lambda$ in particular. The exclusion of $0$ is what makes the eigenvalue genuinely *associated* with the vector — and turns out to be unique: each nonzero generalized eigenvector belongs to a unique eigenvalue, exactly as eigenvectors do, but the proof requires more work because $(T - \lambda I)^k v = 0$ involves a power rather than a single application. (The proof is in §8A of LADR; the key step is to expand $(T - \lambda I)^n = ((T - \alpha I) + (\alpha - \lambda) I)^n$ binomially and apply $(T - \alpha I)^{m-1}$ to extract the leading term.)

What is the payoff of the definition? On a complex space, the generalized eigenvectors of $T$ for each eigenvalue $\lambda$ (together with zero) form a *[[Def - Subspace|subspace]]* $G(\lambda, T)$, called the **generalized eigenspace**, and these [[Def - Subspace|subspaces]] *always* sum to all of $V$:

$$V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T).$$

This is the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]], the headline theorem of [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]]. It would have been impossible without the generalisation: with only eigenvectors, the sum of eigenspaces falls short of $V$ whenever $T$ fails to be diagonalisable. With generalized eigenvectors, the sum is always all of $V$. So the definition is calibrated to make the decomposition work — and that is what it costs: the price of a clean structural theorem is admitting these slightly larger sets as "morally eigenvectors".

---

# The Definition

Suppose $T \in \mathcal{L}(V)$ and $\lambda$ is an eigenvalue of $T$. A vector $v \in V$ is a **generalized eigenvector** of $T$ corresponding to $\lambda$ if $v \neq 0$ and

$$(T - \lambda I)^k v = 0$$

for some positive integer $k$.

Equivalently, by the null-space stabilisation result [[Thm - Null Spaces of Powers Stabilize]] applied to $T - \lambda I$, $v$ is a generalized eigenvector of $T$ corresponding to $\lambda$ if and only if

$$(T - \lambda I)^{\dim V} v = 0.$$

The two definitions describe the same set of nonzero vectors.

---

# Relate to Other Fields / Compression

**True name:** A generalized eigenvector for $\lambda$ is *the endpoint of a chain* $v_1, v_2, \dots, v_k$ with $(T - \lambda I) v_j = v_{j-1}$ for $j \geq 2$ and $v_1$ an honest eigenvector. The chain starts with an eigenvector $v_1 \in E(\lambda, T)$ and propagates "upward" by repeatedly solving $(T - \lambda I) v =$ (previous vector). The length of the chain (the largest $k$ such that $v_k \neq 0$ in the chain) is exactly the size of the Jordan block containing this chain. This is the operational picture; it is the natural basis for a Jordan block, and it is how one *finds* generalized eigenvectors in practice.

The notion is also the linear-algebra incarnation of a more general phenomenon. In module theory ([[Def - Module|modules]] over a PID), the analogous object is a **torsion element** — an element annihilated by some nonzero element of the ring — and the generalised eigenspace is the **primary component** for the prime $(x - \lambda) \in \mathbb{C}[x]$. The decomposition $V = \bigoplus G(\lambda_k, T)$ is exactly the **primary decomposition** of $V$ regarded as a $\mathbb{C}[x]$-module via $T$ ([[Thm - Primary Decomposition Theorem]] and `[[Def - The Module of a Linear Operator]]`). So a generalized eigenvector is the $\mathbb{C}[x]$-module-theoretic torsion element for the prime ideal $(x - \lambda)$.

A third compression: in the language of nilpotent operators ([[Def - Nilpotent Operator]]), $v$ is a generalized eigenvector of $T$ for $\lambda$ iff $v$ is in the kernel of some power of $(T - \lambda I)$, iff $T - \lambda I$ acts *nilpotently on the subspace generated by $v$ under $T$*. So generalized eigenvectors are exactly the vectors where the "shift by $\lambda$" is locally nilpotent. The chapter's central idea — that $T = \lambda I + N$ on each generalized eigenspace — is just the global version of this observation.

---

# Examples / Corollaries

**Is an instance — the second standard basis vector of $\mathbb{C}^2$ for $T(z_1, z_2) = (z_2, 0)$.** The only eigenvalue is $0$. Then $(T - 0 \cdot I)(0, 1) = T(0, 1) = (1, 0) \neq 0$, so $(0, 1)$ is *not* an eigenvector. But $T^2 = 0$, so $(T - 0 \cdot I)^2 (0, 1) = 0$, and $(0, 1)$ is a generalized eigenvector for $\lambda = 0$. The chain is $v_1 = (1, 0)$ (an honest eigenvector), $v_2 = (0, 1)$ with $T v_2 = v_1$; this is the chain underlying the unique $2 \times 2$ Jordan block of $T$.

**Is an instance — non-eigenvector generalized eigenvectors on $\mathbb{C}^3$.** Define $T \in \mathcal{L}(\mathbb{C}^3)$ by $T(z_1, z_2, z_3) = (4 z_2, 0, 5 z_3)$. The eigenvalues are $0$ and $5$, with eigenvectors $(1, 0, 0)$ for $\lambda = 0$ and $(0, 0, 1)$ for $\lambda = 5$. Direct computation shows $T^3(z_1, z_2, z_3) = (0, 0, 125 z_3)$, so the generalized eigenvectors for $\lambda = 0$ are the nonzero vectors of the form $(z_1, z_2, 0)$ — in particular, $(0, 1, 0)$ is a generalized eigenvector for $\lambda = 0$ but is not an eigenvector. The chain is $v_1 = (4, 0, 0)$, $v_2 = (0, 1, 0)$ with $T v_2 = (4, 0, 0) = v_1$.

**Is an instance — every nonzero vector for a nilpotent operator.** If $N \in \mathcal{L}(V)$ is nilpotent then $N^{\dim V} = 0$ (by [[Thm - Null Spaces of Powers Stabilize]]), so $(N - 0 \cdot I)^{\dim V} v = N^{\dim V} v = 0$ for every $v$. Hence *every* nonzero vector in $V$ is a generalized eigenvector of $N$ for the unique eigenvalue $0$. This is the definition of nilpotence from the generalised-eigenvector point of view.

**Is NOT an instance — $(0, 1, 0)$ for $\lambda = 5$ in the previous $\mathbb{C}^3$ example.** Direct computation: $(T - 5 I)(0, 1, 0) = (0 - 0, 0 - 5, 0 - 0) = (0, -5, 0)$ — wait, let us recompute. $T(0, 1, 0) = (4, 0, 0)$ and $5 I \cdot (0, 1, 0) = (0, 5, 0)$, so $(T - 5 I)(0, 1, 0) = (4, -5, 0)$. Then $(T - 5 I)^2 (0, 1, 0) = (T - 5 I)(4, -5, 0) = (T(4, -5, 0)) - 5 (4, -5, 0) = (-20, 0, 0) - (20, -25, 0) = (-40, 25, 0)$. Continuing, $(T - 5I)^3 (0, 1, 0) = (T - 5I)(-40, 25, 0) = (100, 0, 0) - (-200, 125, 0) = (300, -125, 0)$. The components are growing, not shrinking, and no power of $(T - 5I)$ will ever annihilate $(0, 1, 0)$ because $(0, 1, 0)$ has no $z_3$-component, but $(T - 5I)$ acting on the $z_1, z_2$-plane is a non-nilpotent operator (it has eigenvalues $-5$ and... actually let us just say the result holds). The cleanest argument is **uniqueness of the eigenvalue**: $(0, 1, 0)$ is a generalized eigenvector for $\lambda = 0$ (as shown above), so it cannot also be a generalized eigenvector for any other eigenvalue. Each generalized eigenvector corresponds to a *unique* eigenvalue.

**Is NOT an instance — a vector $v$ with $\dim V \geq 2$ and $(T - \lambda I) v$ a nonzero eigenvector for a *different* eigenvalue.** For instance, on $\mathbb{C}^2$ with the diagonal operator $T = \operatorname{diag}(1, 2)$, the vector $v = (1, 1)$ satisfies $(T - 1 \cdot I) v = (0, 1)$, which is an eigenvector for $\lambda = 2$, not for $\lambda = 1$. Higher powers $(T - I)^k$ act as $(0, 1)$ on $v$ — the second coordinate, multiplied by $1^{k-1}$ — so they never vanish. Hence $v$ is not a generalized eigenvector for $\lambda = 1$. (It also is not for $\lambda = 2$, by the same argument run for $T - 2I$.) This shows that not every vector is a generalized eigenvector; only those that fall inside *some* generalized eigenspace are. Of course, on a complex space *some* generalized eigenspace contains $v$ — by the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] — but $v$ may need to be written as a sum of generalized eigenvectors of different eigenvalues, and *as a sum it is a generalized eigenvector for no single $\lambda$*.

**Corollary — every eigenvector is a generalized eigenvector.** Taking $k = 1$ in the definition gives $(T - \lambda I) v = 0$, the eigenvector condition. So the eigenspace is contained in the generalized eigenspace: $E(\lambda, T) \subseteq G(\lambda, T)$. The reverse inclusion fails in general; it holds for every $\lambda$ iff $T$ is diagonalisable. This containment is the source of the inequality "geometric multiplicity $\leq$ algebraic multiplicity" between $\dim E(\lambda, T)$ and $\dim G(\lambda, T)$ (see [[Def - Algebraic and Geometric Multiplicity]]).

**Calibration check.** Verify that for $T(z_1, z_2) = (z_2, 0)$ on $\mathbb{C}^2$ the chain $v_1 = (1, 0), v_2 = (0, 1)$ is a chain of generalized eigenvectors for $\lambda = 0$, with $T v_2 = v_1$ and $T v_1 = 0$; and that for the operator $T = \begin{pmatrix} 5 & 1 \\ 0 & 5 \end{pmatrix}$ the vector $(0, 1)$ is a generalized eigenvector for $\lambda = 5$ that is not an eigenvector — compute $(T - 5I)(0, 1) = (1, 0)$ and $(T - 5I)^2 (0, 1) = (T - 5I)(1, 0) = (0, 0)$. If you can produce two such chains, you have understood the definition correctly.

---

# Unlocked by This

> [!tip] Generalized Eigenspace *(from this topic)*
> The set of all generalized eigenvectors of $T$ for $\lambda$, together with zero, is a $T$-invariant subspace — the [[Def - Generalized Eigenspace|generalized eigenspace]] $G(\lambda, T)$. The Jordan form and the generalized eigenspace decomposition are statements about how $V$ is built out of these subspaces.

> [!tip] Jordan Basis *(from this topic)*
> A maximal chain of generalized eigenvectors $v_1, v_2, \dots, v_k$ with $(T - \lambda I) v_j = v_{j-1}$ is the canonical basis for a Jordan block (`[[Def - Jordan Basis and Jordan Form]]`). Building a Jordan basis is exactly the task of finding enough such chains to cover all of $V$.

> [!tip] Primary Decomposition of a Module over a PID *(from Module Theory)*
> A generalized eigenvector for $\lambda$ is the $\mathbb{C}[x]$-module-theoretic incarnation of a torsion element for the prime ideal $(x - \lambda)$. The decomposition of $V$ into generalized eigenspaces is the [[Thm - Primary Decomposition Theorem|primary decomposition]] of $V$ as a $\mathbb{C}[x]$-module, the same theorem that decomposes finitely generated abelian groups into prime-power cyclic pieces.

> [!tip] Resolvent and Spectral Projections *(from Functional Analysis)*
> In the holomorphic functional calculus, the **spectral projection** onto the generalized eigenspace $G(\lambda, T)$ is given by the contour integral $P_\lambda = \frac{1}{2\pi i} \oint_{\gamma_\lambda} (zI - T)^{-1}\, dz$ around a small loop encircling $\lambda$. The range of $P_\lambda$ is exactly $G(\lambda, T)$, the kernel is the sum of the other generalized eigenspaces, and $P_\lambda$ is the canonical projection associated with the generalized eigenspace decomposition.
