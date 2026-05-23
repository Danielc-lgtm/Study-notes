---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Generalized Eigenvector"
  - "Def - Eigenvalue and Eigenvector"
  - "Def - Null Space and Range"
  - "Def - Invariant Subspace"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional nonzero vector space over $\mathbf{F} \in \{\mathbb{R}, \mathbb{C}\}$ and $T \in \mathcal{L}(V)$ is a linear operator. We write $I$ for the identity, $\operatorname{null} S$ for the kernel of an operator, and $E(\lambda, T) = \operatorname{null}(T - \lambda I)$ for the **eigenspace** corresponding to $\lambda$. The generalized eigenspace is denoted $G(\lambda, T)$; we will use this symbol throughout. Full registry on [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

---

# Axiom Motivation

Once we have admitted [[Def - Generalized Eigenvector|generalized eigenvectors]] — vectors $v$ for which $(T - \lambda I)^k v = 0$ for some power $k$ — the next question is what algebraic structure they form. A natural guess is that they constitute a [[Def - Subspace|subspace]]: closed under addition and scalar multiplication, containing zero. This is the right guess, and the generalized eigenspace is precisely the resulting subspace.

But there is a subtlety in the closure. If $v$ is killed by $(T - \lambda I)^k$ and $w$ is killed by $(T - \lambda I)^\ell$, is $v + w$ killed by some power? The answer is yes — by $(T - \lambda I)^{\max(k, \ell)}$, since both summands are then in its kernel. So $G(\lambda, T) = \{v : (T - \lambda I)^k v = 0 \text{ for some } k\} \cup \{0\}$ is closed under addition. Closure under scalar multiplication is immediate: $(T - \lambda I)^k (cv) = c (T - \lambda I)^k v = 0$ if $v$ is killed by $(T - \lambda I)^k$. Hence $G(\lambda, T)$ is a subspace of $V$.

The next step is to give $G(\lambda, T)$ a *uniform* description, not as the union of kernels of varying powers but as the kernel of a single operator. The chain $\operatorname{null}(T - \lambda I)^0 \subseteq \operatorname{null}(T - \lambda I)^1 \subseteq \cdots$ is nondecreasing and bounded above by $\dim V$, so once two consecutive terms agree, all subsequent terms agree (see [[Thm - Null Spaces of Powers Stabilize]]). The stabilisation occurs by index $\dim V$ at the latest, because each strict inclusion in the chain adds at least one [[Def - Dimension|dimension]] and a subspace of $V$ has dimension at most $\dim V$. Hence

$$G(\lambda, T) \;=\; \operatorname{null}(T - \lambda I)^{\dim V}.$$

This uniform description is the form one uses in proofs and in computations. It also reveals the algebraic structure immediately: $G(\lambda, T)$ is the kernel of the polynomial-in-$T$ operator $(T - \lambda I)^{\dim V}$, hence a subspace, and (more importantly) it is *invariant under $T$*: if $v \in G(\lambda, T)$ then $(T - \lambda I)^{\dim V} v = 0$, and $T$ commutes with $(T - \lambda I)^{\dim V}$ (any operator commutes with a polynomial in itself), so $(T - \lambda I)^{\dim V} (T v) = T (T - \lambda I)^{\dim V} v = T \cdot 0 = 0$, giving $T v \in G(\lambda, T)$.

Why is the right power $\dim V$ and not something tighter? It would be nice to have $G(\lambda, T) = \operatorname{null}(T - \lambda I)^{d}$ where $d$ is the *multiplicity* — the smallest power that stabilises — but $d$ depends on $T$ and is not known in advance. The bound $\dim V$ is universal and depends only on the ambient space, making it usable in all theorems. (After the theory is built, one can refine: the stabilisation actually occurs at the multiplicity, which is at most $\dim V$ but often much smaller. See exercise 7 in §8B of LADR.)

What is the test of a successful definition? It is that the generalized eigenspaces always sum to give $V$: on a complex space,

$$V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$$

with $\lambda_k$ the distinct eigenvalues. This is the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]], the headline theorem of [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]], and it would not work with eigenspaces alone: the sum $\bigoplus E(\lambda_k, T)$ has dimension equal to the sum of *geometric* multiplicities, which falls short of $\dim V$ unless $T$ is diagonalisable. Replacing eigenspaces by generalized eigenspaces enlarges each piece by exactly enough to make the sum total. The relevant inequality $\dim E(\lambda, T) \leq \dim G(\lambda, T)$ — geometric multiplicity at most algebraic multiplicity — is precisely the room that allows the upgrade.

Why insist that $\lambda$ be an eigenvalue? If $\lambda$ is *not* an eigenvalue, then $T - \lambda I$ is injective; in finite [[Def - Dimension|dimensions]] injective implies invertible, so $(T - \lambda I)^k$ is also invertible, hence has trivial kernel. So $G(\lambda, T) = \{0\}$ — the definition is consistent but gives a trivial space. There is no benefit to extending $\lambda$ beyond eigenvalues; doing so just adds zero [[Def - Subspace|subspaces]].

---

# The Definition

Suppose $T \in \mathcal{L}(V)$ and $\lambda \in \mathbf{F}$. The **generalized eigenspace** of $T$ corresponding to $\lambda$, denoted $G(\lambda, T)$, is

$$G(\lambda, T) \;=\; \{ v \in V : (T - \lambda I)^k v = 0 \text{ for some positive integer } k \}.$$

Equivalently,

$$G(\lambda, T) \;=\; \operatorname{null}(T - \lambda I)^{\dim V}.$$

The two descriptions define the same set; the equivalence is a corollary of the stabilisation of the null-space chain (see [[Thm - Null Spaces of Powers Stabilize]]).

The generalized eigenspace $G(\lambda, T)$ is a subspace of $V$ — the kernel of a linear operator — and it is **invariant under $T$**: if $v \in G(\lambda, T)$ then $T v \in G(\lambda, T)$.

When $\lambda$ is not an eigenvalue of $T$, the generalized eigenspace $G(\lambda, T) = \{0\}$ is the trivial subspace; the meaningful case is $\lambda$ an eigenvalue, where $G(\lambda, T) \supseteq E(\lambda, T) \neq \{0\}$.

---

# Relate to Other Fields / Compression

**True name:** $G(\lambda, T)$ is *the largest $T$-invariant subspace on which $T - \lambda I$ is nilpotent*. From the definition $(T - \lambda I)^{\dim V}|_{G(\lambda, T)} = 0$, the restriction $T - \lambda I$ to $G(\lambda, T)$ is nilpotent. Conversely, if $U \subseteq V$ is $T$-invariant and $(T - \lambda I)|_U$ is nilpotent (with $(T - \lambda I)^k|_U = 0$, say), then every $v \in U$ satisfies $(T - \lambda I)^k v = 0$ and so $v \in G(\lambda, T)$. So $G(\lambda, T)$ is exactly the locus where $T - \lambda I$ acts nilpotently — which is why $T$ on $G(\lambda, T)$ is structurally $\lambda I + (\text{nilpotent})$, the chapter's central building block.

In module-theoretic terms, $G(\lambda, T)$ is the **$(x - \lambda)$-primary component** of $V$ regarded as a $\mathbb{C}[x]$-module via $T$ (see `[[Def - The Module of a Linear Operator]]`). The primary decomposition theorem ([[Thm - Primary Decomposition Theorem]]) decomposes any torsion module over a PID into a direct sum of primary components; applied to $V$ over $\mathbb{C}[x]$ this gives the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]]. So $G(\lambda, T)$ has two parallel names: linear-algebraically it is the generalized eigenspace, module-theoretically it is the $(x - \lambda)$-primary component, and they refer to the same subspace.

A third compression: $G(\lambda, T)$ is the **kernel of the spectral projection** at every other eigenvalue, or equivalently the *range* of the spectral projection at $\lambda$. In the functional calculus picture, $P_\lambda = \frac{1}{2\pi i} \oint_{\gamma_\lambda} (z I - T)^{-1}\, dz$ is the canonical projection of $V$ onto $G(\lambda, T)$ along $\bigoplus_{\mu \neq \lambda} G(\mu, T)$. The generalized eigenspaces are not just abstract direct summands; they are the ranges of explicit, canonically defined operators.

---

# Examples / Corollaries

**Is an instance — $G(0, T) = \mathbb{C}^2$ for the shift on $\mathbb{C}^2$.** Let $T(z_1, z_2) = (z_2, 0)$. Then $T^2 = 0$, so $(T - 0 \cdot I)^2 v = 0$ for every $v \in \mathbb{C}^2$. Hence $G(0, T) = \mathbb{C}^2$. The eigenspace $E(0, T) = \operatorname{null} T = \{(z_1, 0) : z_1 \in \mathbb{C}\}$ is strictly smaller — one-dimensional — so $E(0, T) \subsetneq G(0, T)$ is a strict containment.

**Is an instance — $G(\lambda, T) = E(\lambda, T)$ for a diagonal operator.** If $T = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ with $\lambda_k$ pairwise distinct, then $(T - \lambda I)$ for each eigenvalue $\lambda = \lambda_j$ has nontrivial kernel only in the $\lambda_j$-coordinate, and $(T - \lambda_j I)^k$ does the same for every $k \geq 1$. Hence $G(\lambda_j, T) = E(\lambda_j, T) = \operatorname{span}(e_j)$, the standard basis vector. More generally, $T$ is diagonalisable iff $G(\lambda, T) = E(\lambda, T)$ for every eigenvalue, iff the algebraic and geometric multiplicities agree (see [[Def - Algebraic and Geometric Multiplicity]]).

**Is an instance — generalized eigenspaces of an explicit operator.** Let $T \in \mathcal{L}(\mathbb{C}^3)$ have matrix $\begin{pmatrix} 6 & 3 & 4 \\ 0 & 6 & 2 \\ 0 & 0 & 7 \end{pmatrix}$ in the standard basis. Its eigenvalues are $6$ and $7$ (the diagonal entries of an upper-triangular matrix). Computing kernels of powers of $T - 6 I$ and $T - 7 I$:

$$G(6, T) = \operatorname{span}((1, 0, 0), (0, 1, 0)), \qquad G(7, T) = \operatorname{span}((10, 2, 1)).$$

Then $G(6, T) \oplus G(7, T) = \mathbb{C}^3$, confirming the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]]. The multiplicities are $\dim G(6, T) = 2$ and $\dim G(7, T) = 1$, summing to $\dim \mathbb{C}^3 = 3$.

**Is NOT an instance — $G(\lambda, T)$ when $\lambda$ is not an eigenvalue is the trivial subspace.** For $T = \operatorname{diag}(1, 2)$ on $\mathbb{C}^2$, taking $\lambda = 3$ gives $T - 3 I = \operatorname{diag}(-2, -1)$, invertible, so $(T - 3 I)^k$ is invertible for every $k$ and $\operatorname{null}(T - 3 I)^k = \{0\}$. Hence $G(3, T) = \{0\}$. The definition is meaningful only for eigenvalues.

**Is NOT an instance — $G(\lambda, T)$ is not always closed under arbitrary functions of $T$.** It is closed under polynomials in $T$ (because the polynomial commutes with $T$, hence with $(T - \lambda I)$, hence with its powers), but it is not closed under, say, a square root of $T$ unless the square root happens also to be a polynomial in $T$. For most operators, $\sqrt{T}$ is not a polynomial in $T$ in general — though on each generalized eigenspace it *is* a polynomial in $T$ (the truncated Taylor series), and so $G(\lambda, T)$ is closed under each block-wise square root. The lesson is that "$T$-invariant" is the right invariance, not "invariant under every operator that is somehow built from $T$".

**Corollary — invariance under $T$.** Since $T$ commutes with $(T - \lambda I)^{\dim V}$ (any operator commutes with a polynomial in itself), if $v$ is in $\operatorname{null}(T - \lambda I)^{\dim V} = G(\lambda, T)$ then so is $Tv$. So $G(\lambda, T)$ is $T$-invariant; the restriction $T|_{G(\lambda, T)}$ is a well-defined operator on $G(\lambda, T)$, and the central observation $T|_{G(\lambda, T)} = \lambda I + N$ with $N$ nilpotent rests on this invariance.

**Corollary — the eigenspace is contained in the generalized eigenspace.** Every $v \in E(\lambda, T)$ satisfies $(T - \lambda I) v = 0$, hence $(T - \lambda I)^k v = 0$ for every $k \geq 1$, hence $v \in G(\lambda, T)$. So $E(\lambda, T) \subseteq G(\lambda, T)$, and the geometric multiplicity $\dim E(\lambda, T)$ is at most the algebraic multiplicity $\dim G(\lambda, T)$.

**Corollary — $G(\lambda, T) \cap G(\mu, T) = \{0\}$ for distinct eigenvalues.** Nonzero vectors in $G(\lambda, T) \cap G(\mu, T)$ would be generalized eigenvectors for two different eigenvalues, contradicting the uniqueness of the eigenvalue associated with a generalized eigenvector. So the generalized eigenspaces for distinct eigenvalues meet trivially, which is the direct-sum condition.

**Calibration check.** Verify directly that for $T \in \mathcal{L}(\mathbb{C}^3)$ with matrix $\begin{pmatrix} 6 & 3 & 4 \\ 0 & 6 & 2 \\ 0 & 0 & 7 \end{pmatrix}$, $\operatorname{null}(T - 6 I) = \operatorname{span}((1, 0, 0))$ and $\operatorname{null}(T - 6 I)^2 = \operatorname{span}((1, 0, 0), (0, 1, 0))$; deduce $G(6, T) = \operatorname{null}(T - 6 I)^2$ and that the algebraic multiplicity of $6$ is $2$ while the geometric multiplicity is $1$. If you can also check that $T$-invariance of $G(6, T)$ follows from the explicit calculation, you have understood the definition.

---

# Unlocked by This

> [!tip] Generalized Eigenspace Decomposition *(from this topic)*
> The principal payoff: on a complex space, the generalized eigenspaces sum to give $V$, as expressed by the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]]. This is the chapter's central structural result and the basis for everything downstream.

> [!tip] Multiplicity of an Eigenvalue *(from this topic)*
> The dimension $\dim G(\lambda, T)$ is the **algebraic multiplicity** of $\lambda$ (see [[Def - Algebraic and Geometric Multiplicity]]). It controls how much of $V$ is "attributable" to the eigenvalue $\lambda$ and is the key ingredient in the characteristic polynomial.

> [!tip] Jordan Form via Generalized Eigenspaces *(from this topic)*
> The Jordan form of $T$ is obtained by choosing, for each eigenvalue $\lambda$, a Jordan basis of $G(\lambda, T)$ — a basis adapted to the nilpotent operator $(T - \lambda I)|_{G(\lambda, T)}$. The block sizes are determined by the dimensions $\dim \operatorname{null}(T - \lambda I)^k$ for $k = 1, 2, \dots$. See [[Def - Jordan Basis and Jordan Form]] and [[Thm - Existence of Jordan Form]].

> [!tip] Primary Component of a $\mathbb{C}[x]$-Module *(from Module Theory)*
> $G(\lambda, T)$ is the $(x - \lambda)$-primary component of $V$ as a $\mathbb{C}[x]$-module. The decomposition into generalized eigenspaces is the [[Thm - Primary Decomposition Theorem|primary decomposition]] of $V$, and the further factoring of each $G(\lambda, T)$ into cyclic modules $\mathbb{C}[x]/(x - \lambda)^k$ is the Jordan form, equivalently the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem for modules over a PID]] applied to $\mathbb{C}[x]$.
