---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Jordan Basis and Jordan Form"
  - "Def - Algebraic and Geometric Multiplicity"
  - "Def - Minimal Polynomial"
tags: [algebra, linear-algebra]
---

# Problem Statement

Exhibit on $\mathbb{C}^4$ two operators $T_1, T_2$ such that

(a) $T_1$ and $T_2$ have the same characteristic polynomial $(z - 1)(z - 5)^3$;

(b) $T_1$ and $T_2$ have *different* Jordan forms.

For each of your operators, compute the characteristic polynomial, the minimal polynomial, the algebraic multiplicities, the geometric multiplicities, and the Jordan form. Conclude that $T_1$ and $T_2$ are not similar.

(See exercises 12–14 of §8B of LADR for related problems.)

**Recall:**

The objects are operators on $\mathbb{C}^4$ and their associated polynomial and dimensional invariants.

![[Def - Jordan Basis and Jordan Form#The Definition]]

The characteristic polynomial is $p_T(z) = \prod_\lambda (z - \lambda)^{d_\lambda}$ where $d_\lambda$ is the algebraic multiplicity, $= \dim G(\lambda, T)$; the minimal polynomial is $m_T(z) = \prod_\lambda (z - \lambda)^{k_\lambda}$ where $k_\lambda$ is the size of the largest Jordan block at $\lambda$.

![[Def - Algebraic and Geometric Multiplicity#The Definition]]

The Jordan form's block partition at each eigenvalue is recovered from the dimensions of $\operatorname{null}(T - \lambda I)^j$: the number of blocks of size $\geq j$ at $\lambda$ is $\dim \operatorname{null}(T - \lambda I)^j - \dim \operatorname{null}(T - \lambda I)^{j-1}$.

---

# Convergent Strategy

**Problem class.** This is a *separate two operators by an invariant finer than the characteristic polynomial* problem. The class is drilled by all of canonical-form theory — showing that some invariant is finer than another (here, Jordan form $\succ$ characteristic polynomial) by exhibiting operators that the coarser invariant cannot distinguish.

**Assumption pattern.** The characteristic polynomial is fixed: $(z - 1)(z - 5)^3$. This pins down (i) the eigenvalues: $1$ and $5$; (ii) the algebraic multiplicities: $\dim G(1, T) = 1$ and $\dim G(5, T) = 3$. The remaining freedom is in the *block partition* at $\lambda = 5$, since $\lambda = 5$ has multiplicity $3$ and the partitions of $3$ are $(3), (2, 1), (1, 1, 1)$. The partition at $\lambda = 1$ is forced to be $(1)$ since the multiplicity is $1$. So there are three possible Jordan forms total — and three corresponding similarity classes — even though the characteristic polynomial is the same.

**Theorem routing.** [[Def - Jordan Basis and Jordan Form]] tells us what Jordan forms are possible; we pick two with different block partitions at $\lambda = 5$ and verify by direct matrix exhibition. The minimal polynomial discriminates between the partitions: the largest block size at $\lambda = 5$ determines the exponent of $(z - 5)$ in $m_T$.

**Key decision point.** The non-obvious move is to *pick two specific block partitions that exhibit the failure of the characteristic polynomial to determine similarity*. The natural choices are the most-and-least split: partition $(3)$ (one big block) and partition $(1, 1, 1)$ (three small blocks). These have minimal polynomials $(z - 1)(z - 5)^3$ and $(z - 1)(z - 5)$ respectively — sharply different. (We could also pick $(2, 1)$, with minimal polynomial $(z - 1)(z - 5)^2$, giving a third possibility.) The decision is to exhibit two operators with different *minimal polynomials* but the same characteristic polynomial — this is the cleanest way to make the difference visible.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Read off the Jordan structure from the null-space dimensions** (operation 4). For each candidate operator we compute $\dim \operatorname{null}(T - \lambda I)^j$ for relevant $j$ and read off the block partition.

2. **Use polynomial constraints** (operation 5). The characteristic and minimal polynomials constrain the Jordan structure: the characteristic polynomial fixes the multiplicity, the minimal polynomial fixes the largest block size at each eigenvalue.

---

# Hints

> [!note]- Hint 1
> The eigenvalues are forced to be $1$ (multiplicity $1$) and $5$ (multiplicity $3$). The remaining freedom is the block partition at $\lambda = 5$. The partitions of $3$ are $(3), (2, 1), (1, 1, 1)$ — three possibilities. Pick any two.

> [!note]- Hint 2
> Concretely: pick block partition $(3)$ at $\lambda = 5$ and block partition $(1, 1, 1)$ at $\lambda = 5$. The Jordan forms are then
> $$T_1 = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 5 & 1 & 0 \\ 0 & 0 & 5 & 1 \\ 0 & 0 & 0 & 5 \end{pmatrix}, \qquad T_2 = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 5 & 0 & 0 \\ 0 & 0 & 5 & 0 \\ 0 & 0 & 0 & 5 \end{pmatrix}.$$
> $T_2$ is diagonal — and is $T_1$'s Jordan form? No: $T_1$ has a $3 \times 3$ Jordan block at $5$, $T_2$ has three $1 \times 1$ blocks. These are different Jordan forms, hence the operators are not similar.

> [!note]- Hint 3
> To distinguish, compute the minimal polynomials: $m_{T_1}(z) = (z - 1)(z - 5)^3$ (because the largest Jordan block at $5$ has size $3$, requiring $(z - 5)^3$ to kill it); $m_{T_2}(z) = (z - 1)(z - 5)$ (because all Jordan blocks at $5$ have size $1$, so $(z - 5)$ suffices). Different minimal polynomials $\implies$ different Jordan forms $\implies$ not similar.

---

# Solution

The strategy is to exhibit two specific matrices with the same characteristic polynomial but different Jordan-block partitions at $\lambda = 5$, and verify by computing the relevant invariants.

**Step 1: Define $T_1$ as the operator with Jordan form $J_1(1) \oplus J_3(5)$ and $T_2$ as the operator with Jordan form $J_1(1) \oplus J_1(5) \oplus J_1(5) \oplus J_1(5)$.**

In matrix form,

$$T_1 = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 5 & 1 & 0 \\ 0 & 0 & 5 & 1 \\ 0 & 0 & 0 & 5 \end{pmatrix}, \qquad T_2 = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 5 & 0 & 0 \\ 0 & 0 & 5 & 0 \\ 0 & 0 & 0 & 5 \end{pmatrix} = \operatorname{diag}(1, 5, 5, 5).$$

> [!note]- Derivation
> By [[Thm - Existence of Jordan Form]], any matrix in Jordan form is a valid operator. The matrices above are block diagonal with blocks $J_1(1)$ and either $J_3(5)$ (for $T_1$) or three copies of $J_1(5)$ (for $T_2$). These are well-defined operators on $\mathbb{C}^4$ in the standard basis.

**Step 2: Both $T_1$ and $T_2$ have characteristic polynomial $(z - 1)(z - 5)^3$.**

For a block-diagonal matrix, the characteristic polynomial is the product of the characteristic polynomials of the blocks. The block $J_1(1)$ contributes $(z - 1)$; the Jordan blocks at $5$ contribute $(z - 5)^{\text{block size}}$.

> [!note]- Derivation
> For $T_1$, the blocks are $J_1(1)$ and $J_3(5)$, contributing $(z - 1) \cdot (z - 5)^3 = (z - 1)(z - 5)^3$.
>
> For $T_2$, the blocks are $J_1(1)$, $J_1(5)$, $J_1(5)$, $J_1(5)$, contributing $(z - 1)(z - 5)(z - 5)(z - 5) = (z - 1)(z - 5)^3$.
>
> So $p_{T_1}(z) = p_{T_2}(z) = (z - 1)(z - 5)^3$.

**Step 3: The minimal polynomials differ.**

The minimal polynomial of $T_k$ is the product of $(z - \lambda)^{(\text{largest block size at } \lambda)}$ over the eigenvalues.

> [!note]- Derivation
> For $T_1$, the largest block at $\lambda = 1$ is size $1$ and the largest at $\lambda = 5$ is size $3$. So $m_{T_1}(z) = (z - 1)(z - 5)^3$.
>
> For $T_2$, the largest block at $\lambda = 1$ is size $1$ and the largest at $\lambda = 5$ is size $1$ (all blocks are $1 \times 1$). So $m_{T_2}(z) = (z - 1)(z - 5)$.
>
> $m_{T_1} \neq m_{T_2}$. Confirms the operators are not similar.

**Step 4: The geometric multiplicities differ at $\lambda = 5$.**

The geometric multiplicity equals the *number* of Jordan blocks at the eigenvalue; the algebraic multiplicity equals the *total size* of all blocks at the eigenvalue.

> [!note]- Derivation
> For both operators, the algebraic multiplicity of $\lambda = 5$ is $3$ (the exponent of $(z - 5)$ in the characteristic polynomial), and the algebraic multiplicity of $\lambda = 1$ is $1$.
>
> For $T_1$, the geometric multiplicity at $\lambda = 5$ is $1$ — there is one Jordan block at $5$, contributing one eigenvector (the first column of the $J_3(5)$ block, which is $e_2$).
>
> For $T_2$, the geometric multiplicity at $\lambda = 5$ is $3$ — there are three $1 \times 1$ Jordan blocks at $5$, each contributing one eigenvector.
>
> Both operators have geometric multiplicity $1$ at $\lambda = 1$.

**Step 5: Conclude not similar.**

Operators with different Jordan forms (equivalently, different minimal polynomials, or different geometric multiplicities at some eigenvalue) are not similar, by [[Thm - Existence of Jordan Form|uniqueness of the Jordan form up to block ordering]].

> [!note]- Derivation
> The Jordan form is a complete similarity invariant: $T_1$ and $T_2$ are similar iff they have the same Jordan form up to block ordering. Since the Jordan forms have different block partitions at $\lambda = 5$ (partition $(3)$ versus partition $(1, 1, 1)$), the Jordan forms are not equal up to ordering. Hence $T_1$ and $T_2$ are not similar.

> [!note]- Complete formal solution
> Define $T_1, T_2 \in \mathcal{L}(\mathbb{C}^4)$ by their matrices in the standard basis:
> $$T_1 = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 5 & 1 & 0 \\ 0 & 0 & 5 & 1 \\ 0 & 0 & 0 & 5 \end{pmatrix}, \qquad T_2 = \operatorname{diag}(1, 5, 5, 5).$$
>
> Both are in Jordan form: $T_1$ has blocks $J_1(1)$ and $J_3(5)$ (block partition $(1)$ at $\lambda = 1$, partition $(3)$ at $\lambda = 5$); $T_2$ has blocks $J_1(1)$, $J_1(5)$, $J_1(5)$, $J_1(5)$ (partitions $(1)$ at $\lambda = 1$ and $(1, 1, 1)$ at $\lambda = 5$).
>
> **Characteristic polynomial.** For both operators, the characteristic polynomial is the product over the blocks. Each $J_k(\lambda)$ contributes $(z - \lambda)^k$. So
> $$p_{T_1}(z) = (z - 1)(z - 5)^3 = p_{T_2}(z).$$
>
> **Multiplicities.** Algebraic: both operators have $\dim G(1, T) = 1$ and $\dim G(5, T) = 3$. Geometric: $T_1$ has $\dim E(1, T) = 1$, $\dim E(5, T) = 1$ (one Jordan block at $5$); $T_2$ has $\dim E(1, T) = 1$, $\dim E(5, T) = 3$ (three $1 \times 1$ Jordan blocks at $5$).
>
> **Minimal polynomial.** For $T_1$: $m_{T_1}(z) = (z - 1)(z - 5)^3$ (largest block at $5$ has size $3$). For $T_2$: $m_{T_2}(z) = (z - 1)(z - 5)$ (all blocks have size $1$).
>
> **Conclusion.** $T_1$ and $T_2$ have the same characteristic polynomial but different minimal polynomials, hence different Jordan forms, hence are *not similar*. $\blacksquare$

> [!warning] A subtler example with same characteristic and minimal polynomials
> Even the pair (characteristic polynomial, minimal polynomial) does not always determine the Jordan form! Consider eigenvalue $\lambda$ with multiplicity $4$ and possible block partitions $(2, 2)$ and $(2, 1, 1)$. The first has characteristic polynomial $(z - \lambda)^4$ and minimal polynomial $(z - \lambda)^2$. The second has the *same* characteristic polynomial $(z - \lambda)^4$ and the *same* minimal polynomial $(z - \lambda)^2$ (because the largest block size is $2$ in both). But the partitions $(2, 2)$ and $(2, 1, 1)$ are different — the first has $2$ blocks, the second has $3$ blocks. The geometric multiplicities are $2$ and $3$ respectively. So the pair (characteristic, minimal) fails to distinguish them; one needs the geometric multiplicity (or equivalently, the full sequence of null-space dimensions $\dim \operatorname{null}(T - \lambda I)^j$). This is exercise 12 of §8B in LADR. The Jordan form is the *complete* invariant; lesser invariants leave ambiguity.

---

# Key Takeaways

**The Jordan form is strictly finer than the characteristic polynomial as a similarity invariant.** The characteristic polynomial gives the eigenvalues with their algebraic multiplicities — equivalently, the *total dimension* of each generalized eigenspace. The Jordan form gives, in addition, the *partition* of each generalized eigenspace into Jordan-block-sized pieces. For algebraic multiplicities $\leq 3$ the partition is determined by the multiplicity alone (since partitions of $1, 2, 3$ are determined by their largest part), so characteristic polynomial $+$ minimal polynomial is enough up to multiplicity $3$. Starting at multiplicity $4$, ambiguity creeps in. The reusable diagnostic is that *whenever a problem fails to be settled by characteristic and minimal polynomial alone, the failure is at multiplicity $\geq 4$ and requires the full Jordan partition*.

**The minimal polynomial captures the largest Jordan block, not the whole partition.** The exponent of $(z - \lambda)$ in $m_T$ equals the size of the *largest* Jordan block at $\lambda$. So the minimal polynomial sees only one feature of the partition — the maximum — and misses everything else. Diagonalisable operators are exactly those whose minimal polynomial has all exponents equal to $1$ (i.e., distinct linear factors). When you need more refined Jordan information, the minimal polynomial alone is insufficient; you need to know the full multiset of block sizes. The transferable lesson is that the minimal polynomial is a *one-dimensional projection* of the Jordan structure; the characteristic polynomial captures the total dimension; the full Jordan structure (the partition) needs the entire kernel-dimension sequence.

**Two diagonalisable operators are similar iff they have the same characteristic polynomial.** This is a corollary worth extracting: when both operators are diagonalisable, the Jordan form is diagonal and is determined by the multiset of eigenvalues with multiplicity — which is exactly the characteristic polynomial. So in the diagonalisable case, characteristic polynomial is a complete invariant. The subtlety only enters when one of the operators fails to be diagonalisable, and then the Jordan-block structure becomes the distinguishing feature. The transferable insight: *similarity in the diagonalisable case is easy (just compare eigenvalue multisets), but the full theory is genuinely about non-diagonalisable operators*. The Jordan-form refinement is precisely what handles the non-diagonalisable case.

The pair of operators $T_1, T_2$ above illustrates the textbook example. For a related exercise drilling the same point at multiplicity $4$ — where characteristic and minimal polynomial together still fail — see exercise 12 of §8B in LADR.
