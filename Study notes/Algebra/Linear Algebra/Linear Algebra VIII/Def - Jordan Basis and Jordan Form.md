---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Generalized Eigenvector"
  - "Def - Generalized Eigenspace"
  - "Def - Nilpotent Operator"
  - "Def - Basis"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional nonzero vector space over $\mathbf{F} \in \{\mathbb{R}, \mathbb{C}\}$ and $T \in \mathcal{L}(V)$. $J_k(\lambda)$ denotes the $k \times k$ matrix with $\lambda$ on the diagonal, $1$s on the superdiagonal, and $0$s elsewhere — the **Jordan block** of size $k$ for eigenvalue $\lambda$. Full registry on [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

This is a compound page: it defines two interlocking notions — *Jordan basis* and *Jordan form* — because they are the basis-side and matrix-side of one and the same statement, and neither is fully usable without the other.

---

# Axiom Motivation

The point of the Jordan form is to make the matrix of an operator as *sparse* as possible by a clever choice of basis. We have already seen this principle at work:

- A basis of eigenvectors makes the matrix *diagonal* (the entries off the diagonal are zero), but this is possible only when $T$ is diagonalisable.
- For arbitrary $T$ on a complex space, the upper-triangular form ([[Thm - Upper-Triangular Form on Complex Vector Spaces]]) makes the entries *below* the diagonal zero, which is better than nothing but leaves the upper-triangular part unrestricted.
- The block-diagonal-with-upper-triangular-blocks form of §8B adapts the basis to the generalized eigenspace decomposition and makes the matrix block-diagonal, with each block upper triangular and having a single eigenvalue $\lambda_k$ on its diagonal. This is better still.

The Jordan form is the *ultimate sparsification*: the matrix is block diagonal, each block is upper triangular with a single eigenvalue $\lambda$ on the diagonal, *and* the off-diagonal entries within each block are all zero except for $1$s on the superdiagonal. Every entry is then determined: $\lambda$s on the diagonal, $1$s or $0$s on the superdiagonal (and $0$s elsewhere). Two operators with the same multiset of Jordan blocks have the same matrix in their respective Jordan bases — they are similar. The Jordan form is thus the *similarity invariant*: the matrix that two operators share iff they are similar.

What is the right notion of "block" to allow? The block diagonal matrix of §8B used blocks that were $d_k \times d_k$ upper triangular with eigenvalue $\lambda_k$ on the diagonal, one block per eigenvalue. The Jordan form refines this: each $d_k \times d_k$ block is itself broken up into smaller blocks, each of which is a Jordan block $J_{m}(\lambda_k)$. The number of blocks at $\lambda_k$ is the geometric multiplicity, the sum of their sizes is the algebraic multiplicity, and the sizes are determined by the operator (uniquely up to ordering).

Why are the off-diagonal entries in each block forced to be $1$ — couldn't they be any other nonzero number? In principle, any nonzero number works to make the matrix as sparse as $1$s — the basis can be rescaled. The choice $1$ is a convention; some texts use $1$s on the *sub*diagonal instead, which corresponds to writing the basis in reverse order. The mathematical content is the same: a chain of $k$ vectors $v_1, v_2, \dots, v_k$ with $(T - \lambda I) v_j = v_{j-1}$ for $j \geq 2$ and $v_1$ an eigenvector (the bottom of the chain). The matrix of $T$ on $\operatorname{span}(v_1, \dots, v_k)$ in the basis $v_1, \dots, v_k$ has $\lambda$ on the diagonal and $1$ on the superdiagonal because $T v_j = \lambda v_j + v_{j-1}$ for $j \geq 2$. Without the $1$s on the superdiagonal, the off-diagonal action of $T$ would not be visible.

A failure analysis is illuminating. If we forced *all* off-diagonal entries in each block to be zero — that is, demanded the matrix be diagonal — we would be back to diagonalisability, which is not always achievable. If we *dropped* the requirement of "upper triangular within each block" and allowed arbitrary blocks, we would have nothing more than the change-of-basis freedom, and no canonical form. The Jordan form is calibrated to be *as restrictive as possible while still being achievable by any operator on a complex space*: the structural content (the generalized eigenspaces) is unavoidable, the diagonal entries are forced to be the eigenvalues, and within each generalized eigenspace the nilpotent $T - \lambda I$ can be put in the standard "$1$s on superdiagonal" nilpotent form. Anything weaker leaves residual structure; anything stronger fails to apply universally.

Why does it work over $\mathbb{C}$ but not over $\mathbb{R}$? Because the diagonal entries of any matrix of $T$ in any basis must be the eigenvalues of $T$ (over $\mathbb{C}$, where the matrix can be triangulated), and the eigenvalues are roots of the characteristic polynomial. Over $\mathbb{R}$ the characteristic polynomial may have complex roots that are not real, in which case the corresponding "diagonal entries" cannot lie in $\mathbb{R}$. The compromise on $\mathbb{R}$ is the **real Jordan form**, where complex-conjugate eigenvalue pairs $a \pm b i$ contribute $2 \times 2$ blocks $\begin{pmatrix} a & b \\ -b & a \end{pmatrix}$ instead of $1 \times 1$ blocks. The nilpotent part of the chapter goes through over $\mathbb{R}$; only the "eigenvalues exist" hypothesis fails.

What makes the Jordan form unique? The number and sizes of the Jordan blocks for each eigenvalue. The Jordan *basis* itself is not unique — for instance, scaling any chain by a nonzero scalar gives another Jordan basis — but the multiset of block sizes for each eigenvalue is an invariant of $T$. The invariance is detected from the [[Def - Dimension|dimensions]] $\dim \operatorname{null}(T - \lambda I)^k$ for $k = 1, 2, \dots$: the number of blocks of size $\geq j$ for $\lambda$ equals $\dim \operatorname{null}(T - \lambda I)^j - \dim \operatorname{null}(T - \lambda I)^{j-1}$. These numbers are basis-independent (they are kernels of basis-independent operators), so the block-size partition is basis-independent.

---

# The Definition

Suppose $T \in \mathcal{L}(V)$. A **Jordan block** of size $k$ for an eigenvalue $\lambda$ is the $k \times k$ matrix

$$J_k(\lambda) \;=\; \begin{pmatrix} \lambda & 1 & & & \\ & \lambda & 1 & & \\ & & \ddots & \ddots & \\ & & & \lambda & 1 \\ & & & & \lambda \end{pmatrix},$$

with $\lambda$ on the diagonal, $1$s on the superdiagonal, and $0$s elsewhere. The $1 \times 1$ Jordan block $J_1(\lambda) = (\lambda)$ has no superdiagonal and is just the scalar $\lambda$.

A basis of $V$ is a **Jordan basis** for $T$ if, with respect to this basis, the matrix of $T$ is block diagonal of the form

$$\mathcal{M}(T) \;=\; \begin{pmatrix} J_{k_1}(\mu_1) & & & 0 \\ & J_{k_2}(\mu_2) & & \\ & & \ddots & \\ 0 & & & J_{k_p}(\mu_p) \end{pmatrix},$$

where each $J_{k_i}(\mu_i)$ is a Jordan block and the $\mu_i$ are not necessarily distinct (different blocks may correspond to the same eigenvalue). This block-diagonal matrix is called the **Jordan form** of $T$.

Equivalently, a Jordan basis is a basis that decomposes into **Jordan chains**: collections of vectors $v_1, v_2, \dots, v_k$ for various eigenvalues $\lambda$, with $(T - \lambda I) v_j = v_{j-1}$ for $j \geq 2$ and $(T - \lambda I) v_1 = 0$. Each chain contributes one Jordan block $J_k(\lambda)$ of size $k$ to the Jordan form.

The Jordan form of $T$ is unique up to the order of the blocks: the multiset of pairs (eigenvalue, block size) is an invariant of $T$. The number of blocks of size $\geq j$ for eigenvalue $\lambda$ is $\dim \operatorname{null}(T - \lambda I)^j - \dim \operatorname{null}(T - \lambda I)^{j-1}$.

A Jordan basis exists for every operator $T$ on a complex vector space — this is the [[Thm - Existence of Jordan Form|Jordan form theorem]].

---

# Relate to Other Fields / Compression

**True name:** The Jordan form is *the matrix of an operator written so that one can read off, in one line per block, the entire structural data*. For each Jordan block $J_k(\lambda)$, the diagonal tells you the eigenvalue $\lambda$, and the size $k$ of the block tells you the "depth" of the generalized-eigenvector chain associated with that block. The block-diagonal arrangement tells you how the operator splits into independent pieces, and the off-diagonal $1$s tell you how each piece is *shifted* internally (by the nilpotent part $T - \lambda I$). Every other property of $T$ — characteristic polynomial, minimal polynomial, rank, nullity, square roots, $e^{tT}$, you name it — can be read off the Jordan form by inspection.

In module-theoretic terms, the Jordan form is the **primary cyclic decomposition** of $V$ as a $\mathbb{C}[x]$-module via $T$ (cf. [[Thm - Primary Decomposition Theorem]] and `[[Def - The Module of a Linear Operator]]`). Each Jordan block $J_k(\lambda)$ corresponds to the cyclic module $\mathbb{C}[x]/(x - \lambda)^k$: the basis of the block is $\bar 1, \overline{x - \lambda}, \overline{(x - \lambda)^2}, \dots, \overline{(x - \lambda)^{k-1}}$ in $\mathbb{C}[x]/(x - \lambda)^k$, on which $x$ (acting as $T$) operates as $\lambda \cdot (\text{itself}) + (\text{next lower})$, which is exactly the Jordan block action. The whole Jordan form expresses $V$ as a direct sum of such cyclic modules:

$$V \cong \bigoplus_{i} \mathbb{C}[x] / (x - \lambda_{k(i)})^{m_i}$$

with one summand per Jordan block. This is the **primary cyclic decomposition**, the form in which the structure theorem expresses the answer. The Jordan basis is the explicit basis exhibiting this decomposition; the Jordan form is the matrix of $T$ in this basis. See [[Thm - Jordan Normal Form]] in [[Modules II — §3.3–3.4]] for the module-theoretic statement.

A third compression: the Jordan form is the **multiplicative analogue of the prime factorisation of integers**. The integers have a unique prime factorisation $n = p_1^{a_1} \cdots p_r^{a_r}$; an operator on $\mathbb{C}^n$ has a unique Jordan-block decomposition $V = \bigoplus J_{k_i}(\lambda_i)$ with $\lambda_i$ the eigenvalues. The Jordan block $J_k(\lambda)$ plays the role of a prime power $p^k$ — it is an indivisible cyclic piece in the structural decomposition, and it cannot be split further. Two operators are similar iff they have the same multiset of Jordan blocks, iff (as integers) they have the same multiset of prime-power factors.

A fourth compression: in the language of **Young diagrams**, the Jordan form at a fixed eigenvalue $\lambda$ is encoded by a partition of $\dim G(\lambda, T)$, drawn as a Young diagram with column heights equal to the block sizes. The dimensions of the kernels of powers of $T - \lambda I$ are then read off as the row counts: $\dim \operatorname{null}(T - \lambda I)^j =$ sum of the first $j$ row counts, which equals the number of cells in the top $j$ rows. The "dual partition" (transposing the Young diagram) gives the block sizes from the cumulative row counts. This is the *Loehr-style* picture of nilpotent maps and is used in §8C exercises throughout — see Loehr Ch 8 for the partition-diagram approach.

---

# Examples / Corollaries

**Is an instance — the standard nilpotent shift's Jordan form is one block.** For $T(z_1, z_2, z_3) = (0, z_1, z_2)$ on $\mathbb{C}^3$, $T^3 = 0$ but $T^2 \neq 0$, so the chain $v_1 = T^2 v, v_2 = T v, v_3 = v$ for $v = e_3 = (0, 0, 1)$ gives $T^2 v = e_1, T v = e_2, v = e_3$. The matrix in the basis $e_1, e_2, e_3$ is $\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = J_3(0)$, a single $3 \times 3$ Jordan block at $0$. The whole space is a single chain.

**Is an instance — two blocks at the same eigenvalue.** For $T(z_1, z_2, z_3) = (0, z_1, 0)$ on $\mathbb{C}^3$ (note that this is not the same operator as above — the third coordinate is zeroed instead of mapped to the second), the matrix in standard basis is $\begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$. The kernel of $T$ is the span of $e_2, e_3$ (geometric multiplicity $2$). The kernel of $T^2$ is all of $\mathbb{C}^3$ (algebraic multiplicity $3$). The increments are $\dim \operatorname{null} T = 2$ (so $2$ blocks of size $\geq 1$), $\dim \operatorname{null} T^2 - \dim \operatorname{null} T = 1$ (so $1$ block of size $\geq 2$); hence partition $(2, 1)$, that is, one $2 \times 2$ block and one $1 \times 1$ block. A Jordan basis: $v_1 = e_2$ (gives chain $e_2$ since $T e_2 = 0$ — wait this is wrong, let me redo). Actually: $T e_1 = e_2$, $T e_2 = 0$, $T e_3 = 0$. So $e_2$ is an eigenvector and $e_1$ satisfies $T e_1 = e_2$, giving chain $(e_2, e_1)$ of length $2$; $e_3$ is an eigenvector by itself, chain of length $1$. Jordan basis $e_2, e_1, e_3$ (chain endpoint first within each chain, then chains laid end-to-end), matrix $\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ — a $2 \times 2$ Jordan block followed by a $1 \times 1$ block.

**Is an instance — a Jordan form with multiple eigenvalues.** The matrix $\begin{pmatrix} 6 & 1 & 0 & 0 \\ 0 & 6 & 0 & 0 \\ 0 & 0 & 6 & 0 \\ 0 & 0 & 0 & 7 \end{pmatrix}$ is in Jordan form: a $2 \times 2$ block at $6$, a $1 \times 1$ block at $6$, a $1 \times 1$ block at $7$. Eigenvalues $6$ (algebraic multiplicity $3$, partition $(2, 1)$, so geometric multiplicity $2$) and $7$ (algebraic and geometric multiplicity $1$).

**Is NOT an instance — the matrix $\begin{pmatrix} 0 & 1 \\ 2 & 0 \end{pmatrix}$ is not in Jordan form.** It is not even upper-triangular. Its eigenvalues are $\pm \sqrt 2$, so the Jordan form (over $\mathbb{C}$) is the diagonal matrix $\operatorname{diag}(\sqrt 2, -\sqrt 2)$. Bringing the matrix to Jordan form requires a change of basis to an eigenvector basis.

**Is NOT an instance — a basis is not unique.** For the operator $T(z_1, z_2) = (z_2, 0)$ on $\mathbb{C}^2$, the chain $(e_1, e_2)$ gives Jordan basis $e_1, e_2$ and matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$. But so does the chain $(e_1, e_2 + e_1)$: $T(e_2 + e_1) = T e_2 + T e_1 = e_1 + 0 = e_1$, so $(T - 0 I)(e_2 + e_1) = e_1$, confirming the chain. The basis $e_1, e_2 + e_1$ is a different Jordan basis with the *same* Jordan form. Many Jordan bases give the same Jordan form; the matrix is the invariant, not the basis.

**Is NOT an instance — operators with the same characteristic polynomial need not have the same Jordan form.** See [[Ex - Operators with the same characteristic polynomial need not have the same Jordan form]]: the operators $\operatorname{diag}(J_3(5), J_1(1))$ and $\operatorname{diag}(J_2(5), J_1(5), J_1(1))$ on $\mathbb{C}^4$ both have characteristic polynomial $(z - 5)^3 (z - 1)$ but different Jordan forms (partition $(3)$ vs partition $(2, 1)$ at $5$). They are not similar.

**Corollary — diagonalisable $\iff$ all Jordan blocks of size $1$.** If every block in the Jordan form is $1 \times 1$ then the matrix is diagonal in the Jordan basis, so $T$ is diagonalisable. Conversely if $T$ is diagonalisable then its matrix in some basis is diagonal, which is a Jordan form with all $1 \times 1$ blocks; by uniqueness of the Jordan form, *every* Jordan basis gives a diagonal matrix. So diagonalisability is equivalent to "no Jordan block of size $\geq 2$".

**Corollary — the minimal polynomial of a Jordan block $J_k(\lambda)$ is $(z - \lambda)^k$.** Direct computation: $(J_k(\lambda) - \lambda I)^k = 0$ (the nilpotent part raised to size of block kills everything), but $(J_k(\lambda) - \lambda I)^{k-1} \neq 0$ (it sends $e_k$ to $e_1$, which is nonzero). The minimal polynomial of the whole operator $T$ is the LCM of the minimal polynomials of the blocks: $m_T(z) = \prod_\lambda (z - \lambda)^{k_{\max}(\lambda)}$, where $k_{\max}(\lambda)$ is the size of the *largest* Jordan block at $\lambda$. This is much smaller than the characteristic polynomial $p_T(z) = \prod_\lambda (z - \lambda)^{d_\lambda}$, where $d_\lambda$ is the algebraic multiplicity (= sum of block sizes), unless all blocks at each $\lambda$ have the same size.

**Calibration check.** For the matrix $\begin{pmatrix} 5 & 1 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 5 \end{pmatrix}$, find a Jordan basis and verify the matrix in that basis is in Jordan form. (Answer: standard basis works; the matrix is already in Jordan form, with blocks $J_2(5)$ and $J_1(5)$.) For the matrix $\begin{pmatrix} 5 & 1 & 1 \\ 0 & 5 & 0 \\ 0 & 0 & 5 \end{pmatrix}$, find the Jordan form. (Answer: partition computation — $\dim \operatorname{null}(T - 5I)$? $(T - 5I)$ has matrix with first row $(0, 1, 1)$ and other rows zero, so $\operatorname{null}$ is span of $(1, 0, 0)$ and $(0, 1, -1)$, [[Def - Dimension|dimension]] $2$. $(T - 5I)^2$ has first row $(0, 0, 0)$ — yes the whole matrix squares to zero. So algebraic multiplicity $3$, partition $(2, 1)$, Jordan form $J_2(5) \oplus J_1(5)$ — same as the first matrix despite different appearance.) If you can locate a Jordan basis for the second matrix, you have the operational skill.

---

# Unlocked by This

> [!tip] Existence of Jordan Form *(from this topic)*
> Every operator on a complex vector space has a Jordan basis — see [[Thm - Existence of Jordan Form]]. The proof reduces to the nilpotent case via the generalized eigenspace decomposition.

> [!tip] Similarity Invariants *(from this topic)*
> Two operators are similar iff they have the same Jordan form (up to block ordering). The Jordan form is thus a complete set of similarity invariants for operators on a complex space — the analogue of the prime factorisation for integers.

> [!tip] Matrix Exponential and Linear ODE Solutions *(from ODE Theory)*
> The matrix exponential $e^{t J_k(\lambda)} = e^{\lambda t} e^{t N_k}$ where $N_k$ is the nilpotent part of $J_k(\lambda)$ is a polynomial of degree $k - 1$ in $t$ times $e^{\lambda t}$. Solutions of $\dot x = A x$ near a fixed point have polynomial-in-$t$ factors of degree at most "largest Jordan block at the eigenvalue minus one". The Jordan form is the *operational* link between the linear-algebra theorem and the differential equation theory.

> [!tip] Rational Canonical Form *(from Module Theory)*
> Over an arbitrary field $k$, the [[Thm - Rational Canonical Form|rational canonical form]] replaces Jordan blocks with **companion matrices** of irreducible polynomial factors. Over $\mathbb{C}$ the irreducible factors are linear and the companion matrices become Jordan blocks; over $\mathbb{R}$ one gets either Jordan blocks (for real eigenvalues) or $2 \times 2$ companion blocks (for complex-conjugate eigenvalue pairs). The Jordan form is the special case of the rational canonical form when the field is algebraically closed.

> [!tip] Filtration by Powers and the Associated Graded *(from Module Theory / Algebraic Geometry)*
> The Jordan structure at $\lambda$ defines a filtration $V \supseteq \operatorname{null}(T - \lambda I) \supseteq \operatorname{null}(T - \lambda I)^2 \supseteq \cdots$, and the associated graded module $\bigoplus_k \operatorname{null}(T - \lambda I)^k / \operatorname{null}(T - \lambda I)^{k-1}$ is the "abelianisation" of the operator at $\lambda$. The dimensions of the graded pieces are exactly the increment data $\dim \operatorname{null}(T - \lambda I)^k - \dim \operatorname{null}(T - \lambda I)^{k-1}$, which determine the partition. This filtration-and-grading viewpoint is the algebraic-geometry side of Jordan theory.
