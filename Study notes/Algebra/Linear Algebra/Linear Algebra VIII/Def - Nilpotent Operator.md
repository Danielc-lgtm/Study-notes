---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Eigenvalue and Eigenvector"
  - "Def - Minimal Polynomial"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional nonzero vector space over $\mathbf{F} \in \{\mathbb{R}, \mathbb{C}\}$ and $N \in \mathcal{L}(V)$ is a linear operator (the letter $N$ suggests "nilpotent"). $N^k$ is the $k$-fold composition; $N^0 = I$. Full registry on [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]]. The Latin *nil* means "nothing" or "zero" and *potens* means "having power"; **nilpotent** literally is "having a power that is zero".

---

# Axiom Motivation

A nilpotent operator is the simplest non-trivial kind of operator there is: it is one that, when raised to a sufficient power, becomes zero. The definition encodes the empirical observation that some operators "eat themselves" under composition — repeated applications grind every vector down to zero. Why is this a useful class to single out?

The strongest reason is structural: on a complex vector space, **every operator is locally a sum of a scalar and a nilpotent**, on each of its generalized eigenspaces. The [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] says $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$, and on each piece $T|_{G(\lambda_k, T)} = \lambda_k I + N_k$ with $N_k = (T - \lambda_k I)|_{G(\lambda_k, T)}$ nilpotent. So nilpotent operators are the universal *local* model for operators on complex spaces, and understanding nilpotent operators is exactly understanding all operators on a complex space (after the linear shift by an eigenvalue). The class is small enough to admit a complete description but rich enough to capture the entire content of non-diagonalisability.

What conditions might one impose, and which would be too strong or too weak? The strongest condition is "$N = 0$": this is the zero operator, the only operator that is its own first power that vanishes. Too strong — we want nonzero operators that vanish only after several steps. The condition "$N$ has zero as its only eigenvalue" is also natural: on a complex space, every operator has at least one eigenvalue (Fundamental Theorem of Algebra), and if zero is the only one then $N$ is somehow "all kernel". This turns out to be *equivalent* to nilpotence on a complex space, but it fails over $\mathbb{R}$ — the rotation matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has no real eigenvalues at all (so trivially zero is not among them, but the statement "zero is the only one" is vacuously true), yet it is not nilpotent: its powers cycle through $I, $ rotation, $-I$, $-$rotation. So "only eigenvalue zero" is the right *consequence* of nilpotence over $\mathbb{C}$ but not the right *definition* in general.

A still-weaker condition is "$N$ has zero as an eigenvalue", that is, $N$ is not injective. This is implied by nilpotence (if $N^k = 0$ then $N$ is not injective, otherwise $N^k$ would be) but it is far weaker — most singular operators are not nilpotent. So the condition "$N^k = 0$ for some $k$" is genuinely in between "$N = 0$" and "$N$ has nonzero kernel", and it is the right level for the structural role nilpotents play.

The most subtle question is *how large* the power $k$ needs to be. The definition says only that *some* positive integer $k$ works. Once we have the null-space stabilisation result [[Thm - Null Spaces of Powers Stabilize]], we know that if any $N^k = 0$ then $N^{\dim V} = 0$ — the universal bound is the dimension of the space. This is sharp: the standard example of a nilpotent operator on $\mathbb{C}^n$ is the shift $N(z_1, \dots, z_n) = (0, z_1, \dots, z_{n-1})$, which satisfies $N^n = 0$ but $N^{n-1} \neq 0$. So we cannot replace $\dim V$ by a smaller universal number; we *can* replace it by the **nilpotency index** (the smallest $k$ with $N^k = 0$), which depends on $N$. For the example just given the nilpotency index is exactly $n$; for the zero operator it is $1$. The nilpotency index equals the size of the largest Jordan block of $N$.

A useful test of the definition's correctness is the alternative characterisations it admits. *Nilpotence is equivalent to: every nonzero vector is a generalized eigenvector for the eigenvalue zero; the minimal polynomial is $z^m$ for some $m$; there is a basis in which the matrix is strictly upper triangular* (over $\mathbb{C}$, the last is also: $N$ has $0$ as its only eigenvalue). The fact that these four statements are equivalent — a definition by "some power vanishes", a generalized-eigenvector condition, a polynomial-annihilator condition, and a matrix-form condition — is the surest sign that nilpotence has been carved out at the right level of generality. Each characterisation is the most useful one for a different purpose: the matrix form for computation, the polynomial form for algebraic manipulation, the generalized-eigenvector form for connection to the chapter's main theorem, and the power-vanishing form for the definition itself.

---

# The Definition

An operator $N \in \mathcal{L}(V)$ is **nilpotent** if there exists a positive integer $k$ such that $N^k = 0$.

Equivalently (the equivalence requires no hypothesis on the field):

1. **Universal-power form.** $N^{\dim V} = 0$.
2. **Generalized-eigenvector form.** Every nonzero vector in $V$ is a generalized eigenvector of $N$ corresponding to the eigenvalue $0$.
3. **Minimal-polynomial form.** The minimal polynomial of $N$ is $z^m$ for some positive integer $m$.
4. **Upper-triangular form.** There is a basis of $V$ with respect to which the matrix of $N$ is upper triangular with $0$s on the diagonal (equivalently, $0$s on and below the diagonal).

Over $\mathbf{F} = \mathbb{C}$ there is one further equivalent: $0$ is the only eigenvalue of $N$. Over $\mathbf{F} = \mathbb{R}$ this last condition is strictly weaker (the rotation matrix above has no real eigenvalues at all).

The smallest $k$ such that $N^k = 0$ is called the **nilpotency index** of $N$. It satisfies $k \leq \dim V$, with equality possible (and achieved by the standard shift example).

---

# Relate to Other Fields / Compression

**True name:** A nilpotent operator is *the abstract shift*, or the abstract differentiation on polynomials of bounded degree. The two most operational mental models are the matrix $N = \begin{pmatrix} 0 & 1 & & \\ & 0 & 1 & \\ & & \ddots & \ddots \\ & & & 0 \end{pmatrix}$ (the Jordan block at zero), which shifts the basis $e_n \to e_{n-1} \to \cdots \to e_1 \to 0$, and the differentiation operator $D : \mathcal{P}_m(\mathbb{R}) \to \mathcal{P}_m(\mathbb{R})$, $D p = p'$, which sends $x^j \to j x^{j-1}$ and eventually reduces any polynomial to zero. Both are nilpotent with nilpotency index equal to the dimension of the space. Every nilpotent operator is, up to a choice of basis, a direct sum of such shifts (one shift per Jordan block); see [[Thm - Existence of Jordan Form]].

In ring-theoretic terms, $N \in \mathcal{L}(V)$ is nilpotent iff $N$ is a nilpotent element of the ring $\mathcal{L}(V)$ (cf. `[[Def - Ring]]`). The set of nilpotent elements of a commutative ring is the **nilradical**, the intersection of all prime ideals. The non-commutative ring $\mathcal{L}(V)$ does not have a nilradical in the same clean sense, but the nilpotent operators still form a useful class — for instance, the set of *strictly upper triangular matrices* (relative to a fixed basis) is closed under addition and multiplication of nilpotents that share that basis.

In module-theoretic terms, $N$ is nilpotent iff the $\mathbb{C}[x]$-module structure on $V$ defined by $x \cdot v = N v$ (see `[[Def - The Module of a Linear Operator]]`) is **annihilated by some power of $x$** — that is, $V$ is a torsion module whose only associated prime is $(x)$. Equivalently, $V$ is a $\mathbb{C}[x]/(x^m)$-module for some $m$, and the structure theorem for modules over a PID decomposes $V$ further into cyclic modules $\mathbb{C}[x]/(x^{k_i})$ — these are the Jordan blocks at $0$.

A third compression, and historically the original one: nilpotent operators are the operators that are *infinitesimally close to the identity* in a precise sense. The exponential $e^N = I + N + \frac{N^2}{2!} + \cdots$ is a *finite* sum (because $N^{\dim V} = 0$) and equals an *invertible* operator (its inverse is $e^{-N}$). So nilpotents exponentiate to **unipotent** operators — invertible operators of the form $I + $ (nilpotent). The exponential map gives a bijection between nilpotent and unipotent operators in finite dimensions, and this bijection is the Lie-theoretic foundation of the Jordan–Chevalley decomposition: every operator on a complex space decomposes uniquely into commuting *semisimple* (diagonalisable) and *unipotent* parts.

---

# Examples / Corollaries

**Is an instance — the shift on $\mathbf{F}^n$.** Define $N(z_1, \dots, z_n) = (0, z_1, \dots, z_{n-1})$. Then $N$ shifts each coordinate one position to the right and zeros out the first; the matrix is the $n \times n$ matrix with $1$s on the subdiagonal (or, equivalently, $1$s on the *super*diagonal depending on basis ordering convention) and $0$s elsewhere. Computing, $N^k$ shifts by $k$ positions, and $N^n = 0$ while $N^{n-1} \neq 0$. Nilpotency index $n$.

**Is an instance — differentiation on $\mathcal{P}_m(\mathbb{R})$.** The space $\mathcal{P}_m(\mathbb{R})$ of polynomials of degree at most $m$ is $(m+1)$-dimensional, with basis $1, x, x^2, \dots, x^m$. The differentiation operator $D p = p'$ sends $x^j \to j x^{j-1}$, so $D^{m+1} x^j = 0$ for every $j$, hence $D^{m+1} = 0$. But $D^m x^m = m! \neq 0$, so $D^m \neq 0$. Nilpotency index $m + 1 = \dim V$.

**Is an instance — the 4-dimensional operator $T(z_1, z_2, z_3, z_4) = (0, 0, z_1, z_2)$.** Computing $T^2 (z_1, z_2, z_3, z_4) = T(0, 0, z_1, z_2) = (0, 0, 0, 0)$, so $T^2 = 0$. Nilpotency index $2$, much smaller than $\dim V = 4$. The matrix in the standard basis is $\begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}$, which has the upper-triangular-with-zero-diagonal form after reordering the basis.

**Is an instance — the matrix $\begin{pmatrix} -3 & 9 & 0 \\ -7 & 9 & 6 \\ 4 & 0 & -6 \end{pmatrix}$.** Direct computation shows $A^3 = 0$ but $A^2 \neq 0$. Nilpotency index $3$, equal to $\dim V$. The eigenvalues (all equal to zero) are not visible from the matrix, but the nilpotence is exposed by computing the cube.

**Is NOT an instance — the rotation matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ on $\mathbb{R}^2$.** Its powers cycle: $A^2 = -I$, $A^3 = -A$, $A^4 = I$, and so on. No power is zero, so $A$ is not nilpotent. Yet $A$ has no real eigenvalues at all — so the *complex-field equivalence* "zero is the only eigenvalue $\Leftrightarrow$ nilpotent" cannot apply (vacuously the statement "zero is the only eigenvalue" is true here, since there are no real eigenvalues). Over $\mathbb{C}$, $A$ has eigenvalues $\pm i$, neither of which is zero, so the complex-field equivalence correctly diagnoses non-nilpotence. This is the failure that shows the four characterisations of nilpotence collapse over $\mathbb{C}$ but spread over $\mathbb{R}$.

**Is NOT an instance — the identity $I$.** $I^k = I \neq 0$ for every $k$. Nilpotents must vanish; the identity does not. Indeed, the only nilpotent invertible operator is the impossibility — if $N$ is nilpotent with $N^k = 0$, then $N$ is not injective (since some nonzero vector is in $\ker N$), hence not invertible. So no nonzero nilpotent is invertible.

**Is NOT an instance — the projection $P$ onto a nonzero proper subspace.** Such a $P$ satisfies $P^2 = P$, not $P^k = 0$. Indeed, $P^k = P$ for every $k \geq 1$, and $P \neq 0$. Projections are *idempotent*, not nilpotent — they are the orthogonal class of operators in the sense that $P^2 = P$ and $N^k = 0$ are at opposite ends of the spectrum of "what happens under iterated composition".

**Corollary — every nilpotent has zero as an eigenvalue.** If $N^k = 0$ then $N$ is not injective (otherwise $N^k$ would be), so there is a nonzero $v$ with $N v = 0$, that is, $0$ is an eigenvalue of $N$. Combined with the next corollary (over $\mathbb{C}$), this gives "$0$ is the *only* eigenvalue".

**Corollary — on a complex space, $0$ is the only eigenvalue of a nilpotent.** If $N v = \lambda v$ with $v \neq 0$, then $0 = N^k v = \lambda^k v$, so $\lambda^k = 0$, so $\lambda = 0$. This argument needs neither finite-dimensionality nor the complex field — it works over any field — so in fact "$0$ is the only eigenvalue" is true over any field provided the nilpotent has at least one eigenvalue (which over $\mathbb{C}$ is automatic, by FTA, but over $\mathbb{R}$ may fail).

**Corollary — every nilpotent is non-invertible.** Follows from "$0$ is an eigenvalue". The contrapositive — every invertible operator is non-nilpotent — is exactly what makes the [[Thm - Square Root of an Invertible Operator on a Complex Space|square-root theorem]] meaningful: the hypothesis of invertibility excludes the operators (nilpotents) for which the conclusion can fail.

**Corollary — $I + N$ is invertible for any nilpotent $N$.** With $N^k = 0$, the geometric series $I - N + N^2 - \cdots + (-1)^{k-1} N^{k-1}$ is the explicit inverse:
$$(I + N)(I - N + N^2 - \cdots) = I + (-N + N) + (N^2 - N^2) + \cdots = I.$$
This is the operator-theoretic version of $(1 + x)^{-1} = 1 - x + x^2 - \cdots$, and the truncation is rigorous because $N^k = 0$. Square roots, logarithms, exponentials all follow the same template — Taylor series, then truncation.

**Calibration check.** Verify directly that the operator $T : \mathcal{P}_3(\mathbb{R}) \to \mathcal{P}_3(\mathbb{R})$ given by $T p = p'$ is nilpotent with nilpotency index $4$, and that the matrix of $T$ in the basis $1, x, x^2, x^3$ is strictly upper triangular. Verify also that $(I + T)^{-1} = I - T + T^2 - T^3$ — this is the inverse formula above with $N = T$ — and check the product is the identity by computing $(I + T)(I - T + T^2 - T^3) p$ for $p = x^3$ specifically.

---

# Unlocked by This

> [!tip] Generalized Eigenspace Decomposition *(from this topic)*
> Nilpotent operators are exactly the operators $T$ for which $V = G(0, T)$ — the generalized eigenspace for $0$ is the whole space. The full [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] reduces every operator on a complex space to a direct sum of "scalar plus nilpotent" pieces.

> [!tip] Square Root of Invertible Operators *(from this topic)*
> A nilpotent operator $N$ makes $I + N$ admit a square root, computed by truncating the Taylor series $\sqrt{1 + x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \cdots$. Combined with a complex square root of $\lambda$, this gives a square root of $\lambda I + N = \lambda(I + N/\lambda)$ on each generalized eigenspace, yielding the [[Thm - Square Root of an Invertible Operator on a Complex Space|square-root theorem]].

> [!tip] Matrix Exponential and Linear ODEs *(from ODE Theory)*
> For nilpotent $N$, $e^{tN} = \sum_{j=0}^{k-1} \frac{(tN)^j}{j!}$ is a polynomial in $t$ of degree $k - 1$ where $k$ is the nilpotency index. Applied to the Jordan decomposition $T = \lambda I + N$ on a generalized eigenspace, $e^{tT} = e^{\lambda t} e^{tN} = e^{\lambda t} \sum_{j=0}^{k-1} \frac{(tN)^j}{j!}$, exhibiting the $t^j e^{\lambda t}$ behaviour of solutions to linear ODEs $\dot x = Tx$ with repeated eigenvalues. The polynomial part is *entirely* due to the nilpotent factor.

> [!tip] Unipotent Operators and the Jordan–Chevalley Decomposition *(from Lie Theory)*
> The exponential of a nilpotent is a **unipotent** operator $I + N$ (an invertible operator equal to identity plus a nilpotent). Every invertible operator on a complex space decomposes uniquely as a commuting product of a semisimple (diagonalisable) and a unipotent operator — the multiplicative Jordan–Chevalley decomposition, the Lie-group analogue of the additive decomposition into diagonalisable and nilpotent parts.
