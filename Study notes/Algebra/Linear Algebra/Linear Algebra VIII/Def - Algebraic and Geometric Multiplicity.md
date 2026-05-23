---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Eigenvalue and Eigenvector"
  - "Def - Generalized Eigenspace"
  - "Def - Dimension"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional nonzero vector space over $\mathbf{F} \in \{\mathbb{R}, \mathbb{C}\}$ and $T \in \mathcal{L}(V)$. For an eigenvalue $\lambda$ we write $E(\lambda, T) = \operatorname{null}(T - \lambda I)$ (the **eigenspace**) and $G(\lambda, T) = \operatorname{null}(T - \lambda I)^{\dim V}$ (the **generalized eigenspace**). Full registry on [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

This is a compound page: it defines two interlocking notions — *algebraic multiplicity* and *geometric multiplicity* — because they are introduced together, the inequality between them is the central content, and neither is fully usable without the other.

---

# Axiom Motivation

When you encounter an eigenvalue $\lambda$ of an operator $T$, you can ask "how much" of the operator is due to $\lambda$. This question has two natural answers, and they coincide in the easy case but split in general. The split is the content of the definition.

The first natural measure is the dimension of the eigenspace, $\dim E(\lambda, T) = \dim \operatorname{null}(T - \lambda I)$. This counts how many *independent eigenvectors* there are for $\lambda$ — equivalently, how many independent solutions $v$ there are of $(T - \lambda I) v = 0$. It is the dimension of the locus where $T$ acts as $\lambda I$, and it is the "raw eigenvector count". This is the **geometric multiplicity** of $\lambda$, and the name reflects the fact that the eigenspace is the geometric object — an invariant [[Def - Subspace|subspace]] — that one immediately associates with $\lambda$.

The second natural measure is the dimension of the generalized eigenspace, $\dim G(\lambda, T) = \dim \operatorname{null}(T - \lambda I)^{\dim V}$. This counts how many independent *generalized eigenvectors* there are for $\lambda$, where a generalized eigenvector ([[Def - Generalized Eigenvector]]) is a vector $v$ killed by *some* power of $T - \lambda I$. The generalized eigenspace is the locus where $T - \lambda I$ acts nilpotently, and it includes the eigenspace as a [[Def - Subspace|subspace]] but typically is strictly larger. This is the **algebraic multiplicity** of $\lambda$, named because it is the exponent of $(z - \lambda)$ in the characteristic polynomial — a purely algebraic quantity that, surprisingly, also has a geometric meaning as the dimension of $G(\lambda, T)$.

Why two definitions? Because they agree exactly when $T$ is diagonalisable in a neighbourhood of $\lambda$ — that is, when $G(\lambda, T) = E(\lambda, T)$. The inclusion $E(\lambda, T) \subseteq G(\lambda, T)$ is automatic (every eigenvector is a generalized eigenvector), so the geometric multiplicity is always at most the algebraic multiplicity. When they are equal, $T$ acts as $\lambda I$ on the entire generalized eigenspace, and the local picture is just diagonalisation. When they disagree, $T$ acts as $\lambda I$ on only a proper subspace of $G(\lambda, T)$, and the rest of $G(\lambda, T)$ is filled out by generalized eigenvectors that are *not* eigenvectors — equivalently, by Jordan blocks of size $\geq 2$ for $\lambda$. The discrepancy

$$\dim G(\lambda, T) - \dim E(\lambda, T)$$

is exactly the failure of $T$ to be diagonalisable in the $\lambda$-block, and it equals the number of Jordan blocks of size $\geq 2$ for $\lambda$.

Why is the algebraic multiplicity the *right* notion for global structural results? Because it has the additive property: on a complex space, $\sum_\lambda \dim G(\lambda, T) = \dim V$, since the generalized eigenspaces sum to all of $V$ via the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]]. The geometric multiplicities do *not* in general sum to $\dim V$ — they sum to $\dim V$ only when $T$ is diagonalisable. So the algebraic multiplicity is the one that accounts for "all of $V$" in the eigenvalue decomposition, even when not all of $V$ is reached by eigenvectors.

Why call the algebraic multiplicity "algebraic"? In [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] the characteristic polynomial is defined via the determinant: $p_T(z) = \det(z I - T)$. The factor $(z - \lambda)^d$ in this polynomial has exponent $d$ equal to the multiplicity of $\lambda$ as a root, and this $d$ turns out to equal $\dim G(\lambda, T)$. So the same number $d$ appears in two guises: algebraically as the exponent in $p_T$, geometrically as $\dim G(\lambda, T)$. Axler's textbook takes the geometric form as the definition and proves the algebraic equality as a theorem; more traditional treatments do the reverse. The two definitions are equivalent. We follow Axler.

A failure analysis is illuminating. If we *dropped* the requirement of "powers" in the definition of algebraic multiplicity and used $\dim E(\lambda, T)$ everywhere — that is, if we collapsed the two definitions into the geometric one — then the sum-of-multiplicities theorem would fail. For $T(z_1, z_2) = (z_2, 0)$ on $\mathbb{C}^2$, the only eigenvalue is $0$ and the geometric multiplicity is $1$, but $\dim V = 2$, so the sum $\sum_\lambda \dim E(\lambda, T) = 1 < 2 = \dim V$. Without the algebraic notion, we would have no way to track "where the missing dimension went". The algebraic multiplicity says: it went into the second-order generalized eigenvectors — the ones killed by $(T - 0 I)^2$ but not by $T$ itself.

The inequality "geometric $\leq$ algebraic" is sharp in the sense that the discrepancy can be any non-negative integer up to $\dim V - 1$: for an operator with one eigenvalue $\lambda$ of multiplicity $n = \dim V$ and a single Jordan block, the geometric multiplicity is $1$ and the algebraic is $n$, so the discrepancy is $n - 1$.

---

# The Definition

Suppose $T \in \mathcal{L}(V)$ and $\lambda$ is an eigenvalue of $T$.

The **algebraic multiplicity** of $\lambda$, sometimes simply called the *multiplicity* of $\lambda$, is

$$\operatorname{mult}_{\text{alg}}(\lambda) \;=\; \dim G(\lambda, T) \;=\; \dim \operatorname{null}(T - \lambda I)^{\dim V}.$$

The **geometric multiplicity** of $\lambda$ is

$$\operatorname{mult}_{\text{geo}}(\lambda) \;=\; \dim E(\lambda, T) \;=\; \dim \operatorname{null}(T - \lambda I).$$

These satisfy

$$1 \;\leq\; \operatorname{mult}_{\text{geo}}(\lambda) \;\leq\; \operatorname{mult}_{\text{alg}}(\lambda) \;\leq\; \dim V,$$

with the lower bound $1$ holding because $\lambda$ is an eigenvalue, the middle inequality holding because $E(\lambda, T) \subseteq G(\lambda, T)$, and the upper bound holding because $G(\lambda, T) \subseteq V$.

On a complex vector space, the algebraic multiplicities sum to the dimension:

$$\sum_{\lambda \text{ eigenvalue of } T} \operatorname{mult}_{\text{alg}}(\lambda) \;=\; \dim V.$$

Equivalently, the algebraic multiplicity of $\lambda$ equals the exponent of $(z - \lambda)$ in the characteristic polynomial $p_T(z)$, and it also equals the number of times $\lambda$ appears on the diagonal of any upper-triangular matrix of $T$ ([[Thm - Upper-Triangular Form on Complex Vector Spaces]] gives one; the multiplicity counts repetitions on the diagonal of any such).

---

# Relate to Other Fields / Compression

**True name:** The geometric multiplicity is *the number of Jordan blocks for $\lambda$*; the algebraic multiplicity is *the total size of all Jordan blocks for $\lambda$*. From the Jordan form ([[Def - Jordan Basis and Jordan Form]]): each Jordan block $J_k(\lambda)$ contributes one eigenvector (the bottom of the block's chain) and $k$ generalized eigenvectors total. So the number of blocks for $\lambda$ — counted by geometric multiplicity — is the *count*, and the sum of block sizes for $\lambda$ — counted by algebraic multiplicity — is the *area*. The discrepancy "algebraic minus geometric" is the total length of the *strictly inside* parts of the Jordan blocks, equivalently the number of Jordan blocks of size $\geq 2$ counted with their excess over $1$.

In terms of partitions, the Jordan structure at $\lambda$ is described by a partition of $\operatorname{mult}_{\text{alg}}(\lambda)$ into block sizes $k_1 \geq k_2 \geq \cdots \geq k_r$. Then $\operatorname{mult}_{\text{geo}}(\lambda) = r$ (the number of parts) and $\operatorname{mult}_{\text{alg}}(\lambda) = k_1 + k_2 + \cdots + k_r$ (the sum of parts). The two multiplicities are the simplest two invariants of the partition; the full Jordan structure is the partition itself, recovered from the increment-of-null-spaces sequence $\dim \operatorname{null}(T - \lambda I)^k$ via **operation 4** in [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces#Legal Operations|Legal Operations]].

In module-theoretic terms, $G(\lambda, T)$ is the $(x - \lambda)$-primary component of the $\mathbb{C}[x]$-module $V$ (cf. `[[Def - The Module of a Linear Operator]]`), and the structure theorem decomposes it as $\mathbb{C}[x]/(x - \lambda)^{k_1} \oplus \cdots \oplus \mathbb{C}[x]/(x - \lambda)^{k_r}$. The algebraic multiplicity is $k_1 + \cdots + k_r = \dim G(\lambda, T)$; the geometric multiplicity is $r$, the number of summands; the partition $(k_1, \dots, k_r)$ is the **invariant factor decomposition** for the prime $(x - \lambda)$. So the two multiplicities are the two extremes of the structural information: the sum and the count of the cyclic summands.

A third compression — and the historically original definition: the algebraic multiplicity is *the order of the zero of $p_T(z)$ at $z = \lambda$*. This is the definition in textbooks that develop determinants before generalized eigenspaces; Axler's approach inverts the order, defining multiplicity first geometrically and proving the determinant identity later. Either way the number is the same. The order-of-zero definition has the advantage of being purely algebraic — no kernels of operators are needed — but the disadvantage of being mysteriously connected to the structural content; Axler's definition makes the structural content immediate at the cost of needing the generalized eigenspace machinery up front.

---

# Examples / Corollaries

**Is an instance — diagonal operator: algebraic = geometric.** If $T = \operatorname{diag}(2, 2, 5)$ on $\mathbb{C}^3$, the eigenvalues are $2$ (with multiplicities $2$, $2$) and $5$ (with multiplicities $1$, $1$). Both multiplicities of $2$ are $2$; both of $5$ are $1$. This is the diagonalisable case: every multiplicity is equal in the two senses, the geometric multiplicities sum to $3 = \dim V$, and the Jordan form is the diagonal matrix itself (Jordan blocks all of size $1$).

**Is an instance — a single Jordan block: algebraic = $n$, geometric = $1$.** If $T \in \mathcal{L}(\mathbb{C}^n)$ has matrix $\begin{pmatrix} \lambda & 1 & & \\ & \lambda & 1 & \\ & & \ddots & \ddots \\ & & & \lambda \end{pmatrix}$ in the standard basis (a single $n \times n$ Jordan block), the only eigenvalue is $\lambda$, with algebraic multiplicity $n$ (the whole space is in $G(\lambda, T)$ since $(T - \lambda I)^n = 0$) and geometric multiplicity $1$ (the eigenspace is the span of $e_1$, since $(T - \lambda I) e_1 = 0$ but no other standard basis vector is in the kernel). The discrepancy is $n - 1$, the maximum possible, reflecting the single block of maximum size.

**Is an instance — two Jordan blocks of sizes 2 and 1 at the same eigenvalue.** The $3 \times 3$ matrix $\begin{pmatrix} 5 & 1 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 5 \end{pmatrix}$ has only eigenvalue $5$. The algebraic multiplicity is $3$ (the whole space is in $G(5, T)$, since $(T - 5 I)^2 = 0$). The geometric multiplicity is $2$: $(T - 5I) e_1 = 0$ and $(T - 5I) e_3 = 0$, but $(T - 5I) e_2 = e_1 \neq 0$, so $E(5, T) = \operatorname{span}(e_1, e_3)$. The partition of $3$ into block sizes is $(2, 1)$, with two parts, matching the geometric multiplicity.

**Is NOT an instance — non-eigenvalues have multiplicity zero.** For $T = \operatorname{diag}(1, 2, 3)$ on $\mathbb{C}^3$, the value $\lambda = 4$ is not an eigenvalue. Then $\operatorname{null}(T - 4 I) = \{0\}$ and $\operatorname{null}(T - 4I)^k = \{0\}$ for every $k$, so $E(4, T) = G(4, T) = \{0\}$ and both multiplicities are $0$. The definition is genuinely an "eigenvalue $\to$ multiplicity" pairing; non-eigenvalues are not in its domain.

**Is NOT an instance — the geometric and algebraic multiplicities need not agree, even on a complex space.** The simplest example: $T = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ on $\mathbb{C}^2$. The only eigenvalue is $0$. Geometric multiplicity $= \dim E(0, T) = \dim \operatorname{null} T = 1$ (eigenvector $e_1$, but not $e_2$ since $T e_2 = e_1 \neq 0$). Algebraic multiplicity $= \dim G(0, T) = \dim \operatorname{null} T^2 = \dim \mathbb{C}^2 = 2$. The two differ by $1$; equivalently, the Jordan form has a single $2 \times 2$ block. Diagonalisability fails exactly because of this disagreement.

**Corollary — $T$ is diagonalisable iff geometric = algebraic for every eigenvalue.** If equality holds for every $\lambda$ then $G(\lambda, T) = E(\lambda, T)$ for every $\lambda$, so the [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] becomes $V = \bigoplus_\lambda E(\lambda, T)$, which is the eigenspace decomposition — the definition of diagonalisability. Conversely if $T$ is diagonalisable then $V = \bigoplus E(\lambda, T)$ and the [[Def - Dimension|dimensions]] sum to $\dim V$; combined with $\dim E(\lambda, T) \leq \dim G(\lambda, T)$ and $\sum \dim G(\lambda, T) = \dim V$, the inequalities must be equalities. See [[Thm - Conditions for Diagonalizability]].

**Corollary — the algebraic multiplicities sum to $\dim V$ on a complex space.** The [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] gives $V = \bigoplus_\lambda G(\lambda, T)$; taking [[Def - Dimension|dimensions]] and using the additivity of dimension across direct sums, $\dim V = \sum_\lambda \dim G(\lambda, T) = \sum_\lambda \operatorname{mult}_{\text{alg}}(\lambda)$.

**Corollary — geometric multiplicities sum to $\leq \dim V$ on a complex space.** By the inclusion $E(\lambda, T) \subseteq G(\lambda, T)$ and the additivity of dimension, $\sum_\lambda \dim E(\lambda, T) \leq \sum_\lambda \dim G(\lambda, T) = \dim V$. Equality iff $T$ is diagonalisable.

**Corollary — algebraic multiplicity counts diagonal repetitions in any upper-triangular form.** If $T$ has upper-triangular matrix $A$ in some basis (always possible over $\mathbb{C}$, by [[Thm - Upper-Triangular Form on Complex Vector Spaces]]), then for each eigenvalue $\lambda$ the algebraic multiplicity equals the number of times $\lambda$ appears on the diagonal of $A$. This is proved in §8B of LADR using the null-space argument; the upshot is that for upper-triangular matrices, reading off algebraic multiplicities is trivial.

**Calibration check.** For $T = \begin{pmatrix} 5 & 1 & 0 & 0 \\ 0 & 5 & 0 & 0 \\ 0 & 0 & 5 & 1 \\ 0 & 0 & 0 & 5 \end{pmatrix}$ on $\mathbb{C}^4$, verify that the only eigenvalue is $5$, that the algebraic multiplicity is $4$, that the geometric multiplicity is $2$ (compute $\operatorname{null}(T - 5 I)$ explicitly), and that the Jordan form is two $2 \times 2$ blocks at $5$. For $T = \begin{pmatrix} 5 & 1 & 0 & 0 \\ 0 & 5 & 1 & 0 \\ 0 & 0 & 5 & 0 \\ 0 & 0 & 0 & 5 \end{pmatrix}$, verify that the algebraic multiplicity is again $4$ but the geometric multiplicity is $2$, and the Jordan form is a $3 \times 3$ block and a $1 \times 1$ block. Despite identical *algebraic* and *geometric* multiplicities, the two operators are not similar — the partition of the algebraic multiplicity differs.

---

# Unlocked by This

> [!tip] Characteristic Polynomial *(from this topic)*
> The algebraic multiplicities are the exponents in the characteristic polynomial $p_T(z) = (z - \lambda_1)^{d_1} \cdots (z - \lambda_m)^{d_m}$. Since the algebraic multiplicities sum to $\dim V$, the characteristic polynomial has degree $\dim V$, matching its definition.

> [!tip] Jordan Form *(from this topic)*
> The geometric multiplicity at $\lambda$ counts the *number* of Jordan blocks for $\lambda$; the algebraic multiplicity gives the *total dimension* of all Jordan blocks for $\lambda$. The full Jordan-block partition is read off from the increments $\dim \operatorname{null}(T - \lambda I)^k - \dim \operatorname{null}(T - \lambda I)^{k-1}$ for $k = 1, 2, \dots$ — see [[Def - Jordan Basis and Jordan Form]] and [[Thm - Existence of Jordan Form]].

> [!tip] Conditions for Diagonalizability *(from this topic, see [[Thm - Conditions for Diagonalizability]])*
> $T$ is diagonalisable iff geometric multiplicity equals algebraic multiplicity for every eigenvalue, iff the minimal polynomial has distinct roots, iff the geometric multiplicities sum to $\dim V$.

> [!tip] Invariant Factor and Elementary Divisor Decompositions *(from Module Theory)*
> The partition of the algebraic multiplicity into Jordan-block sizes is the elementary divisor decomposition for the prime $(x - \lambda) \in \mathbb{C}[x]$; collecting these across all eigenvalues gives the invariant factor decomposition of $V$ as a $\mathbb{C}[x]$-module. See [[Modules II — §3.3–3.4]] and the [[Thm - Structure Theorem for Finitely Generated Modules over a Euclidean Domain|structure theorem]].
