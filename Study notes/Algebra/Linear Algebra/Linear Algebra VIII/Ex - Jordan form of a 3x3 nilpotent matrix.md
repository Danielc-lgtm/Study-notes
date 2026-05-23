---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Nilpotent Operator"
  - "Def - Jordan Basis and Jordan Form"
  - "Thm - Existence of Jordan Form"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $T \in \mathcal{L}(\mathbb{C}^3)$ be the operator whose matrix in the standard basis is

$$A = \begin{pmatrix} -3 & 9 & 0 \\ -7 & 9 & 6 \\ 4 & 0 & -6 \end{pmatrix}.$$

(a) Verify that $A$ is nilpotent by computing $A^3 = 0$ (and $A^2 \neq 0$).

(b) Find a Jordan basis for $T$ and the Jordan form.

**Recall:**

The objects are an operator on a $3$-dimensional complex space, its iterates, and a basis adapted to its nilpotent structure.

![[Def - Nilpotent Operator#The Definition]]

A Jordan basis (see [[Def - Jordan Basis and Jordan Form]]) is a basis in which the matrix of $T$ is block-diagonal with each block a Jordan block — entries $\lambda$ on the diagonal, $1$ on the superdiagonal, $0$ elsewhere. For a nilpotent operator, every Jordan block is $J_k(0)$ (only eigenvalue $0$). The block sizes form a partition of $\dim V$; for $\dim V = 3$ the only partitions are $(3), (2, 1), (1, 1, 1)$, corresponding to Jordan forms $J_3(0)$, $J_2(0) \oplus J_1(0)$, and the zero matrix respectively.

The block partition is read off the [[Def - Dimension|dimensions]] $\dim \operatorname{null} A^j$: the number of blocks of size $\geq j$ is $\dim \operatorname{null} A^j - \dim \operatorname{null} A^{j-1}$.

To find an explicit Jordan basis: identify a vector $v$ with $A^{n-1} v \neq 0$ where $n$ is the nilpotency index; the chain $A^{n-1} v, A^{n-2} v, \dots, A v, v$ (read in this order) is the basis for the longest Jordan block. If $\dim V$ is larger than $n$, find additional chains for the smaller blocks.

---

# Convergent Strategy

**Problem class.** This is a *compute the Jordan form of a small nilpotent matrix* problem — the simplest version of the canonical-form-finding task, with the small dimension ($n = 3$) making explicit computations tractable. The general routine is: (i) verify nilpotence and find the nilpotency index $m$; (ii) compute the [[Def - Dimension|dimensions]] $\dim \operatorname{null} A^j$ for $j = 1, 2, \dots, m$; (iii) read off the block partition; (iv) find an explicit Jordan basis.

**Assumption pattern.** The matrix has $3 \times 3$ entries, eigenvalues are not immediately visible (it is not upper-triangular), and the problem hints that the matrix is nilpotent by asking us to verify $A^3 = 0$. The hypothesis "nilpotent with nilpotency index $3$" pins down the block partition: the only partition of $3$ with a part of size $3$ is $(3)$ itself, so the Jordan form must be $J_3(0)$. Once we know this, the problem reduces to finding an explicit Jordan basis.

**Theorem routing.** Two theorems are in play. [[Thm - Existence of Jordan Form]] guarantees that a Jordan basis exists; the nilpotent case is exactly the heart of that theorem's proof. The construction of a Jordan basis follows the recipe from the proof: find $v$ with $A^{m-1} v \neq 0$, take the chain $A^{m-1} v, A^{m-2} v, \dots, A v, v$.

**Key decision point.** The non-obvious move is to *choose $v$ such that $A^2 v \neq 0$*. Since $A^2 \neq 0$, there is some standard basis vector $e_i$ with $A^2 e_i \neq 0$; we pick one. Picking the wrong vector (one with $A^2 v = 0$) gives a chain that is too short and does not work. The recipe is to compute $A^2$ first, identify any column that is nonzero, and use any vector whose image under $A$ contributes to that column.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Use the null-space-stabilisation chain** (operation 3). We compute $\dim \operatorname{null} A^j$ for $j = 1, 2, 3$ and verify the chain stabilises at $\operatorname{null} A^3 = \mathbb{C}^3$.

2. **Read off the Jordan structure from null-space dimensions** (operation 4). The increments $\dim \operatorname{null} A^1 - 0 = 1$, $\dim \operatorname{null} A^2 - \dim \operatorname{null} A = 1$, $\dim \operatorname{null} A^3 - \dim \operatorname{null} A^2 = 1$ give the partition (number of blocks of size $\geq j$): one block of size $\geq 1$, one of size $\geq 2$, one of size $\geq 3$. So one block, of size $3$. The partition is $(3)$, the Jordan form is $J_3(0)$.

3. **Build a Jordan basis from chains** (operation 8). We identify $v = e_3$ (or any vector with $A^2 v \neq 0$) and take the chain $A^2 v, A v, v$.

---

# Hints

> [!note]- Hint 1
> First verify the matrix is nilpotent by computing $A^2$ and $A^3$. Once you have $A^3 = 0$ and $A^2 \neq 0$, you know the nilpotency index is exactly $3$ — the largest possible for a $3 \times 3$ matrix — and the Jordan form must be a single $3 \times 3$ Jordan block.

> [!note]- Hint 2
> The Jordan basis is constructed from a chain: find a vector $v$ with $A^2 v \neq 0$, then the chain is $A^2 v, A v, v$. Since $A^2 \neq 0$, *some* column of $A^2$ is nonzero, so for that column index $i$, $A^2 e_i \neq 0$ — pick $v = e_i$.

> [!note]- Hint 3
> The Jordan basis is the chain $A^2 v, A v, v$ (in that order). The matrix of $A$ in this basis has $1$ in entry $(1, 2)$ and $(2, 3)$, with all other entries zero — the $3 \times 3$ Jordan block $J_3(0)$. Verify by computing $A$ applied to each basis vector: $A \cdot (A^2 v) = A^3 v = 0$, $A \cdot (A v) = A^2 v$, $A \cdot v = A v$.

---

# Solution

The strategy is to verify the nilpotence directly, read off the Jordan form from the nilpotency index, and construct a Jordan basis by chasing a single chain.

**Step 1: Verify $A^2 \neq 0$ and $A^3 = 0$.**

Direct computation. $A^2$ is computed by squaring $A$; $A^3 = A \cdot A^2$. We find $A^2$ has a nonzero column and $A^3 = 0$.

> [!note]- Derivation
> Compute $A^2 = A \cdot A$:
> $$A^2 = \begin{pmatrix} -3 & 9 & 0 \\ -7 & 9 & 6 \\ 4 & 0 & -6 \end{pmatrix} \begin{pmatrix} -3 & 9 & 0 \\ -7 & 9 & 6 \\ 4 & 0 & -6 \end{pmatrix}.$$
>
> Row 1 of $A^2$: $(-3)(-3) + 9(-7) + 0 \cdot 4, \; (-3)(9) + 9 \cdot 9 + 0 \cdot 0, \; (-3) \cdot 0 + 9 \cdot 6 + 0 \cdot (-6) = 9 - 63 + 0, \; -27 + 81 + 0, \; 0 + 54 + 0 = -54, 54, 54$.
>
> Row 2: $(-7)(-3) + 9(-7) + 6 \cdot 4, \; (-7) \cdot 9 + 9 \cdot 9 + 6 \cdot 0, \; (-7) \cdot 0 + 9 \cdot 6 + 6 \cdot (-6) = 21 - 63 + 24, \; -63 + 81 + 0, \; 0 + 54 - 36 = -18, 18, 18$.
>
> Row 3: $4 \cdot (-3) + 0 + (-6) \cdot 4, \; 4 \cdot 9 + 0 + (-6) \cdot 0, \; 4 \cdot 0 + 0 + (-6)(-6) = -12 + 0 - 24, \; 36 + 0 + 0, \; 0 + 0 + 36 = -36, 36, 36$.
>
> So $A^2 = \begin{pmatrix} -54 & 54 & 54 \\ -18 & 18 & 18 \\ -36 & 36 & 36 \end{pmatrix}$. This is nonzero — in fact, each row is a scalar multiple of $(-1, 1, 1)$, so $A^2$ has rank $1$, i.e. $\dim \operatorname{range} A^2 = 1$ and $\dim \operatorname{null} A^2 = 2$.
>
> Now compute $A^3 = A \cdot A^2$:
>
> Row 1 of $A^3$: $(-3)(-54) + 9(-18) + 0(-36), \; (-3)(54) + 9 \cdot 18 + 0, \; \dots = 162 - 162 + 0, \; -162 + 162 + 0, \; \dots = 0, 0, 0$.
>
> Row 2: $(-7)(-54) + 9(-18) + 6(-36), \; \dots = 378 - 162 - 216, \; \dots = 0, 0, 0$.
>
> Row 3: $4(-54) + 0(-18) + (-6)(-36), \; \dots = -216 + 0 + 216, \; \dots = 0, 0, 0$.
>
> So $A^3 = 0$. Combined with $A^2 \neq 0$, the nilpotency index is exactly $3$.

**Step 2: Read off the Jordan form from the nilpotency index.**

For a nilpotent operator on $\mathbb{C}^3$ with nilpotency index $3$, the only Jordan form is a single $3 \times 3$ Jordan block at $0$: $J_3(0) = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$.

> [!note]- Derivation
> The Jordan form of a nilpotent operator on a $3$-dimensional space is a block-diagonal matrix with Jordan blocks $J_k(0)$ summing to size $3$. The possible block partitions are $(3), (2, 1), (1, 1, 1)$, giving Jordan forms $J_3(0)$, $J_2(0) \oplus J_1(0)$, and the zero matrix.
>
> The nilpotency index equals the size of the *largest* Jordan block. Here the index is $3$, so the largest block has size $3$, so the partition is $(3)$ — a single $3 \times 3$ block. The Jordan form is $J_3(0)$.

**Step 3: Construct an explicit Jordan basis.**

A Jordan basis for $J_3(0)$ is a chain $v_1 = A^2 v, v_2 = A v, v_3 = v$ for some $v$ with $A^2 v \neq 0$. Since $A^2 \neq 0$, we can pick $v = e_3$ (the third standard basis vector) — checking: $A^2 e_3 = (54, 18, 36)^T = 18 (3, 1, 2)^T$. Then the chain is $(54, 18, 36)^T, A e_3, e_3$.

> [!note]- Derivation
> Pick $v = e_3 = (0, 0, 1)^T$. Compute the chain:
> - $A^2 v = A^2 e_3$: the third column of $A^2$ is $(54, 18, 36)^T$.
> - $A v = A e_3$: the third column of $A$ is $(0, 6, -6)^T$.
> - $v = e_3 = (0, 0, 1)^T$.
>
> So the chain is
> $$v_1 = (54, 18, 36)^T, \quad v_2 = (0, 6, -6)^T, \quad v_3 = (0, 0, 1)^T.$$
>
> We verify this is a chain by checking $A v_3 = v_2$, $A v_2 = v_1$, $A v_1 = 0$:
> - $A v_3 = A e_3 = (0, 6, -6)^T = v_2$. ✓
> - $A v_2 = A (0, 6, -6)^T = A \cdot 6 e_2 + A \cdot (-6) e_3 = 6 (9, 9, 0)^T - 6 (0, 6, -6)^T = (54, 54, 0)^T - (0, 36, -36)^T = (54, 18, 36)^T = v_1$. ✓
> - $A v_1 = A^3 e_3 = 0$ (since $A^3 = 0$). ✓
>
> Hence $v_1, v_2, v_3$ is a Jordan basis for $T$.

**Step 4: Verify the matrix in this basis is $J_3(0)$.**

In the basis $v_1, v_2, v_3$:
- $A v_1 = 0 = 0 v_1 + 0 v_2 + 0 v_3$, so column 1 of the matrix is $(0, 0, 0)^T$.
- $A v_2 = v_1 = 1 v_1 + 0 v_2 + 0 v_3$, so column 2 is $(1, 0, 0)^T$.
- $A v_3 = v_2 = 0 v_1 + 1 v_2 + 0 v_3$, so column 3 is $(0, 1, 0)^T$.

Hence the matrix of $A$ in the basis $v_1, v_2, v_3$ is

$$\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = J_3(0),$$

confirming the Jordan form.

> [!note]- Complete formal solution
> Let $T \in \mathcal{L}(\mathbb{C}^3)$ have matrix $A = \begin{pmatrix} -3 & 9 & 0 \\ -7 & 9 & 6 \\ 4 & 0 & -6 \end{pmatrix}$ in the standard basis.
>
> **(a)** Direct computation gives
> $$A^2 = \begin{pmatrix} -54 & 54 & 54 \\ -18 & 18 & 18 \\ -36 & 36 & 36 \end{pmatrix} \neq 0, \qquad A^3 = 0.$$
> Hence $T$ is nilpotent with nilpotency index exactly $3$.
>
> **(b)** Since the nilpotency index of $T$ equals $\dim \mathbb{C}^3 = 3$, the Jordan form of $T$ is a single $3 \times 3$ Jordan block at $0$, namely $J_3(0)$.
>
> An explicit Jordan basis is obtained by picking any vector $v \in \mathbb{C}^3$ with $A^2 v \neq 0$ and taking the chain $A^2 v, A v, v$. We pick $v = e_3 = (0, 0, 1)^T$ — the third column of $A^2$ is nonzero, so $A^2 e_3 \neq 0$.
>
> Computing:
> - $v_1 := A^2 e_3 = (54, 18, 36)^T$,
> - $v_2 := A e_3 = (0, 6, -6)^T$,
> - $v_3 := e_3 = (0, 0, 1)^T$.
>
> Verifications:
> - $A v_3 = v_2$ (directly $A e_3$ is the third column of $A$).
> - $A v_2 = v_1$ (computed: $A (0, 6, -6)^T = 6 A e_2 - 6 A e_3 = 6 (9, 9, 0)^T - 6 (0, 6, -6)^T = (54, 18, 36)^T$).
> - $A v_1 = A^3 e_3 = 0$.
>
> In the ordered basis $v_1, v_2, v_3$, the matrix of $T$ is
> $$\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = J_3(0).$$
>
> Hence the Jordan basis is $v_1, v_2, v_3$ and the Jordan form is $J_3(0)$. $\blacksquare$

> [!warning] Illegal but tempting alternative — choose $v = e_1$
> One might be tempted to start with $v = e_1$, but $A^2 e_1 = (-54, -18, -36)^T \neq 0$, so this also works. However, $v = e_2$ would *also* give $A^2 e_2 = (54, 18, 36)^T \neq 0$. The recipe is "pick any $v$ with $A^2 v \neq 0$"; all such $v$ give valid Jordan bases. Different choices give different Jordan bases but the *same* Jordan form (since the form is unique up to ordering of blocks, and there is only one block here). The only mistake to avoid is picking $v \in \operatorname{null} A^2$ — for instance, any vector in the kernel of $A^2$, which has dimension $2$. Such a $v$ would give a chain of length only $1$ or $2$, missing the longest block.

---

# Key Takeaways

**For nilpotent matrices, the nilpotency index alone determines the Jordan form only when it equals the dimension.** When the nilpotency index $m$ of a nilpotent operator on $V$ equals $\dim V$, the Jordan form *must* be a single Jordan block $J_{\dim V}(0)$ — there is no partition of $\dim V$ with a part of size $\dim V$ except $(\dim V)$ itself. This makes the case of "maximal nilpotency index" the easiest sub-case of Jordan-form computation: read off the form from the index. The reusable diagnostic is to check whether the nilpotency index matches the dimension, and if so to skip directly to the construction of a single-chain basis. (Failure of the equality is the more interesting case, requiring the full null-space-dimension calculation to extract the partition.)

**The Jordan basis is built from a chain emanating from a vector at the top of the kernel hierarchy.** The construction "find $v$ with $A^{m-1} v \neq 0$, take chain $A^{m-1} v, A^{m-2} v, \dots, A v, v$" is the canonical recipe. The vector $v$ lies in $\operatorname{null} A^m \setminus \operatorname{null} A^{m-1}$ — it is "at the top" of the kernel hierarchy, one step beyond the kernel of $A^{m-1}$. The chain then propagates *downward* by applying $A$, each step landing in the next kernel level. The reusable diagnostic is: when seeking a Jordan basis, search for vectors at the top of the kernel hierarchy and propagate down by applying the operator. For multi-block cases, find one chain at a time, each from a top-level vector, with the chains together being linearly independent and exhausting $V$.

**The block partition is the dual of the null-space-dimension sequence.** For a nilpotent $A$ on a space of dimension $n$ with nilpotency index $m$, the sequence $\dim \operatorname{null} A^j$ for $j = 0, 1, \dots, m$ is $0, \dim_1, \dim_2, \dots, n$ — a strictly increasing sequence from $0$ to $n$. The successive differences $\dim_j - \dim_{j-1}$ form the **dual** of the block partition: the number of blocks of size $\geq j$. The original partition (block sizes in decreasing order) is recovered by transposing the Young diagram of the dual partition. This duality is the essential combinatorial content of Jordan form for nilpotent operators, and it generalises to all of nilpotent-orbit theory in Lie theory and to the **Robinson–Schensted correspondence** in algebraic combinatorics. The transferable lesson is that *any time a sequence of nested kernels appears, the increments are the dual of a block partition* — and in nilpotent settings, the partition is the operative invariant.
