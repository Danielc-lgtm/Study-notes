---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Minimal Polynomial"
  - "Def - Diagonalizable Operator"
tags: [algebra, linear-algebra]
---

# Problem Statement

Construct two operators $S, T \in \mathcal{L}(\mathbb{C}^4)$ that **both have minimal polynomial $z^2$** but are **not similar** to each other (i.e., there is no invertible $P \in \mathrm{GL}(\mathbb{C}^4)$ with $T = P^{-1} S P$).

(Equivalently: produce two $4 \times 4$ nilpotent matrices with the same minimal polynomial that are not conjugate.)

**Recall:**

![[Def - Minimal Polynomial#The Definition]]

Two operators $S, T$ on the same vector space $V$ are **similar** if there exists an invertible $P \in \mathcal{L}(V)$ such that $T = P^{-1} S P$. Similar operators represent the same operator in different bases. Similar operators have the same minimal polynomial, characteristic polynomial, rank, nullity, trace, determinant, and many other invariants.

An operator $T$ is **nilpotent** if $T^k = 0$ for some positive integer $k$. The smallest such $k$ is the **nilpotency index**. For a nilpotent operator, the minimal polynomial has the form $m_T = z^k$ where $k$ is the nilpotency index.

The **rank** of an operator $T$ is $\dim \operatorname{im} T$; the **nullity** is $\dim \ker T$. By [[Thm - Fundamental Theorem of Linear Maps|rank-nullity]], $\operatorname{rank}(T) + \operatorname{nullity}(T) = \dim V$.

Similar operators have the same rank: $\operatorname{rank}(P^{-1} S P) = \operatorname{rank}(S)$, since $P^{-1}$ and $P$ are invertible and rank is invariant under composition with invertibles.

---

# Convergent Strategy

**Problem class.** This is a **non-existence problem disguised as a construction problem**: we are asked to construct two operators with the same minimal polynomial but different similarity class, demonstrating that the minimal polynomial is *not* a complete similarity invariant. The construction proves the negative result: $m_T$ alone is insufficient to classify operators up to similarity.

**Assumption pattern.** The hypothesis $m_T = z^2$ on both operators says they are both *nilpotent of index $2$*: $T^2 = 0$ but $T \neq 0$. This is a structural constraint; there are still many such operators. The key insight is that the *rank* of a nilpotent-index-$2$ operator can vary while the minimal polynomial stays the same.

**Theorem routing.** The route is:
1. **Both operators have $m_T = z^2$** ⟹ both nilpotent of index $2$, both have only eigenvalue $0$.
2. **Construct two such operators with different ranks.** Rank is invariant under similarity, so different ranks ⟹ not similar.
3. **The natural candidates**: a $4 \times 4$ matrix with two $2 \times 2$ Jordan blocks at $0$ (rank $2$), versus a $4 \times 4$ matrix with one $2 \times 2$ Jordan block at $0$ plus two zero blocks of size $1$ (rank $1$). Both have $m_T = z^2$ (the largest Jordan block size is $2$), but they differ in rank.

The construction is essentially the **non-uniqueness of Jordan type given the minimal polynomial**: the minimal polynomial determines the maximum Jordan block size at each eigenvalue, but not the *number* of Jordan blocks of each size. The full Jordan structure is encoded in the **invariant factors** of the operator (see [[Thm - Rational Canonical Form]] and [[Thm - Jordan Normal Form]] in Modules II), not just the minimal polynomial.

**Key decision point.** The non-obvious move is recognising that **rank is a similarity invariant** and using it to distinguish operators with the same minimal polynomial. This requires familiarity with the deeper structure of operators — specifically, that the **invariant factors** (or equivalently, the multiset of Jordan block sizes) are the complete similarity invariant, while $m_T$ only sees the largest block size at each eigenvalue.

---

# Legal Operations Used

1. **Compute the minimal polynomial by the iterate algorithm** (operation 3 from the topic page). For the two candidates, verify $T^2 = 0$ but $T \neq 0$ directly.

2. **Translate operator equations to divisibility of $m_T$** (operation 4). From $T^2 = 0$ and $T \neq 0$, conclude $m_T = z^2$ (the only monic polynomial of degree $2$ dividing $z^2$ and not dividing $z$).

3. **Use rank as a similarity invariant** (a general principle, not a specific topic-page operation). Rank invariance under similarity is the obstruction to similarity between our two operators.

---

# Hints

> [!note]- Hint 1
> The minimal polynomial $z^2$ says: $T^2 = 0$ and $T \neq 0$. So $T$ is nilpotent of nilpotency index $2$. Such operators are characterised by $\operatorname{im} T \subseteq \ker T$ (since $T(Tv) = T^2 v = 0$).

> [!note]- Hint 2
> What is *the* similarity invariant of an operator beyond the minimal polynomial? The answer is the *rank* (and more deeply, the **Jordan structure** — the multiset of Jordan block sizes).

> [!note]- Hint 3
> Construct two specific matrices with $m_T = z^2$ but different ranks. For example, $S$ a "two-block" shift and $T$ a "one-block-plus-zeros" shift on $\mathbb{C}^4$.

> [!note]- Hint 4
> Concretely: let
> $$S = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad T = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
> Compute $S^2$, $T^2$, $\operatorname{rank}(S)$, $\operatorname{rank}(T)$. Verify $m_S = m_T = z^2$ and $\operatorname{rank}(S) = 2 \neq 1 = \operatorname{rank}(T)$.

---

# Solution

The plan is to define two $4 \times 4$ complex matrices, verify that both have minimal polynomial $z^2$, and verify that they have different ranks, which prevents similarity.

**Step 1: Define $S$ and $T$.**

> [!note]- Derivation
> Let
> $$S = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad T = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
> Both are upper-triangular with zero diagonal. $S$ is block-diagonal with two $2 \times 2$ Jordan blocks $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ at the eigenvalue $0$. $T$ is block-diagonal with one $2 \times 2$ Jordan block $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and two $1 \times 1$ zero blocks. In matrix form, $S$ has structure "two-Jordan-blocks-of-size-2" and $T$ has structure "one-Jordan-block-of-size-2-plus-two-trivial-blocks".

**Step 2: Verify $m_S = m_T = z^2$.**

> [!note]- Derivation
> Compute $S^2$. Using matrix multiplication:
> $$S^2 = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} = 0.$$
> So $S^2 = 0$ as a matrix. Hence $m_S \mid z^2$. The candidates for $m_S$ are then $1$, $z$, or $z^2$. $m_S = 1$ is impossible ($S \neq 0$). $m_S = z$ would mean $S = 0$, but $S \neq 0$ (the (1,2) entry is nonzero). So $m_S = z^2$.
>
> Similarly:
> $$T^2 = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} = 0.$$
> So $T^2 = 0$, and (as before) $T \neq 0$, so $m_T = z^2$.
>
> Hence $m_S = m_T = z^2$.

**Step 3: Verify $\operatorname{rank}(S) = 2$ and $\operatorname{rank}(T) = 1$.**

> [!note]- Derivation
> $S$ has two non-zero columns (columns $2$ and $4$, equal to $e_1$ and $e_3$ respectively), and these are linearly independent (different standard basis vectors). So $\operatorname{rank}(S) = 2$.
>
> Alternatively, $\operatorname{im}(S) = \operatorname{span}(e_1, e_3) \subseteq \mathbb{C}^4$ (the image of $e_2$ is $e_1$ and of $e_4$ is $e_3$; other basis vectors go to $0$). So $\operatorname{rank}(S) = \dim \operatorname{span}(e_1, e_3) = 2$.
>
> $T$ has one non-zero column (column $2$, equal to $e_1$). So $\operatorname{rank}(T) = 1$.
>
> Alternatively, $\operatorname{im}(T) = \operatorname{span}(e_1)$ (the only non-zero image is $T e_2 = e_1$). So $\operatorname{rank}(T) = 1$.

**Step 4: Conclude $S$ and $T$ are not similar.**

> [!note]- Derivation
> Suppose for contradiction that $S$ and $T$ are similar: $T = P^{-1} S P$ for some invertible $P \in \mathrm{GL}(\mathbb{C}^4)$. Then
> $$\operatorname{im}(T) = \operatorname{im}(P^{-1} S P) = P^{-1}(\operatorname{im}(S P)) = P^{-1}(\operatorname{im}(S)) \quad (\text{since } P \text{ is invertible}),$$
> so $\dim \operatorname{im}(T) = \dim P^{-1}(\operatorname{im}(S)) = \dim \operatorname{im}(S)$ (since $P^{-1}$ is invertible, hence dimension-preserving).
>
> So $\operatorname{rank}(T) = \operatorname{rank}(S)$. But $\operatorname{rank}(T) = 1 \neq 2 = \operatorname{rank}(S)$. Contradiction.
>
> Therefore $S$ and $T$ are not similar. $\blacksquare$

> [!note]- Complete formal solution
> Define
> $$S = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad T = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
>
> *Minimal polynomial of $S$.* Direct computation gives $S^2 = 0$, so $m_S \mid z^2$. Since $S \neq 0$, $m_S \neq z$, so $m_S = z^2$.
>
> *Minimal polynomial of $T$.* Similarly $T^2 = 0$ and $T \neq 0$, so $m_T = z^2$.
>
> *Ranks differ.* $\operatorname{im}(S) = \operatorname{span}(e_1, e_3)$, so $\operatorname{rank}(S) = 2$. $\operatorname{im}(T) = \operatorname{span}(e_1)$, so $\operatorname{rank}(T) = 1$.
>
> *Similarity is impossible.* If $T = P^{-1} S P$ for some invertible $P$, then $\operatorname{im}(T) = P^{-1}(\operatorname{im}(S))$, and so $\dim \operatorname{im}(T) = \dim \operatorname{im}(S)$ (since $P^{-1}$ is an isomorphism). But $1 \neq 2$, contradiction. So $S$ and $T$ are not similar.
>
> Thus $S$ and $T$ are two operators on $\mathbb{C}^4$ with the same minimal polynomial $m_S = m_T = z^2$ that are not similar. $\blacksquare$

> [!note]- Connection to Jordan form
> The deeper picture: every nilpotent operator on $\mathbb{C}^n$ decomposes (up to similarity) as a direct sum of *nilpotent Jordan blocks* $J_k = \begin{pmatrix} 0 & 1 & & \\ & 0 & 1 & \\ & & \ddots & \\ & & & 0 \end{pmatrix}$ of various sizes $k$.
>
> $S$ has Jordan decomposition $J_2 \oplus J_2$ (two blocks of size $2$). Total size $4$, largest block size $2$, so $m_S = z^2$.
>
> $T$ has Jordan decomposition $J_2 \oplus J_1 \oplus J_1$ (one block of size $2$, two trivial blocks of size $1$). Total size $4$, largest block size $2$, so $m_T = z^2$.
>
> The two decompositions differ — the multisets of block sizes are $\{2, 2\}$ vs. $\{2, 1, 1\}$. The minimal polynomial sees only the largest block size (here, $2$ in both cases). The *number* of blocks (and the multiplicities of each block size) are not captured by $m_T$ alone — they are encoded in the **invariant factors** of $T$. See [[Thm - Jordan Normal Form]] for the full story.

---

# Key Takeaways

**The minimal polynomial is not a complete similarity invariant.** This is the central pedagogical point of the exercise. Beginners often (incorrectly) believe that two operators with the same minimal polynomial are similar; this exercise dispels that. The correct statement is: similar operators have the same minimal polynomial; but the converse fails. The full similarity invariant is the multiset of **invariant factors** $f_1 \mid f_2 \mid \cdots \mid f_s$, of which $m_T = f_s$ is the *largest* — the other invariant factors are additional information that the minimal polynomial does not see.

**The "missing" information is the Jordan block structure.** $m_T$ sees the *maximum* Jordan block size at each eigenvalue, but not the *number* of blocks of each size. In our example, both $S$ and $T$ have maximum Jordan block size $2$ at the eigenvalue $0$, so they share $m_T = z^2$. But $S$ has *two* blocks of size $2$ (and total dimension $4$), while $T$ has *one* block of size $2$ plus *two* trivial blocks (and total dimension $4$). The full information is the partition of the eigenvalue's dimension into block sizes — see [[Thm - Jordan Normal Form]] for the systematic classification.

**Rank distinguishes operators with the same $m_T$.** For a nilpotent operator, $\operatorname{rank}(T)$ tells you the total number of "shifts" — equivalently, $\dim \operatorname{im}(T)$ — which is $\sum_k (\text{size}_k - 1)$ where $\text{size}_k$ ranges over Jordan block sizes. So two nilpotent operators with the same $m_T$ but different ranks must have different Jordan structures, hence are not similar. This rank-based discrimination is the simplest example of using invariants beyond the minimal polynomial. Higher invariants come from $\operatorname{rank}(T^k)$ for various $k$: the sequence $(\operatorname{rank}(T^k))_{k \geq 0}$ determines the full Jordan structure (up to a basis change), and is the **complete** invariant.

**Trigger-reaction: "operators with the same minimal polynomial" → don't conclude similarity; check additional invariants like rank or invariant factors.** This trigger should fire whenever a problem talks about classification or similarity. The minimal polynomial is *necessary* for similarity but *not sufficient*. The full invariant is the Jordan structure (over $\mathbb{C}$) or the rational canonical form (over a general field). Computing these requires the [[Thm - Smith Normal Form|Smith normal form]] of the matrix $xI - A$, or equivalently the elementary divisors of the $F[x]$-module $V_T$ — see [[Modules II — §3.3–3.4]].
