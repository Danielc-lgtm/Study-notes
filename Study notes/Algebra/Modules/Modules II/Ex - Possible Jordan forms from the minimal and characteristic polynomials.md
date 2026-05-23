---
type: exercise
subject: module-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - The Module of a Linear Operator"
  - "Def - Polynomial Ring"
  - "Thm - Jordan Normal Form"
  - "Thm - Primary Decomposition Theorem"
tags: [algebra, module-theory]
---

# Problem Statement

Let $\alpha : V \to V$ be an endomorphism of a finite-dimensional complex vector space $V$, with

$$\text{characteristic polynomial} \quad \chi_\alpha(X) = (X-2)^3(X-5)^2, \qquad \text{minimal polynomial} \quad m_\alpha(X) = (X-2)^2(X-5).$$

1. List **all** Jordan normal forms (up to reordering of blocks) consistent with this pair of polynomials.
2. Explain precisely how the minimal polynomial fixes the **size of the largest block** for each eigenvalue, and how the characteristic polynomial fixes the **total size** contributed by each eigenvalue.
3. Determine which data — the eigenvalue $2$ or the eigenvalue $5$ — is *not* pinned down by $(\chi_\alpha, m_\alpha)$ alone, and say what extra invariant would resolve the remaining ambiguity.

The point of the exercise is to understand exactly how much of the Jordan structure the pair $(\chi_\alpha, m_\alpha)$ determines — and exactly where it falls short of a complete invariant.

**Recall:**

The objects in play are an endomorphism $\alpha$ of a complex vector space $V$, its associated $\mathbb{C}[X]$-[[Def - Module|module]] $V_\alpha$, and the Jordan normal form.

![[Def - The Module of a Linear Operator#The Definition]]

The vector space $V$ becomes a $\mathbb{C}[X]$-module $V_\alpha$ by letting $X$ act as $\alpha$. By [[Thm - Jordan Normal Form|the Jordan normal form theorem]], over $\mathbb{C}$ there is a basis in which $\alpha$ is block-diagonal with **Jordan blocks** $J_m(\lambda)$ — eigenvalue $\lambda$ on the diagonal, $1$'s on the subdiagonal. The block $J_m(\lambda)$ corresponds to the cyclic summand $\mathbb{C}[X]/((X-\lambda)^m)$ of $V_\alpha$ in its [[Thm - Primary Decomposition Theorem|primary decomposition]].

For a fixed eigenvalue $\lambda$, the relevant bookkeeping is the multiset of $\lambda$-block sizes — a **partition** of the total size. Two facts connect this partition to the classical polynomials. The **characteristic polynomial** is $\chi_\alpha(X) = \prod_\lambda (X-\lambda)^{b_\lambda}$, where $b_\lambda$ is the *sum* of the $\lambda$-block sizes (the algebraic multiplicity). The **minimal polynomial** is $m_\alpha(X) = \prod_\lambda (X-\lambda)^{a_\lambda}$, where $a_\lambda$ is the *largest* $\lambda$-block size. The geometric multiplicity $\dim\ker(\alpha-\lambda I)$ equals the *number* of $\lambda$-blocks — a third invariant, not visible in $(\chi_\alpha, m_\alpha)$.

A **partition** of a positive integer $n$ is a way of writing $n$ as a sum of positive integers, order irrelevant; e.g. the partitions of $3$ are $3$, $2+1$, $1+1+1$.

---

# Convergent Strategy

**Problem class.** This is a *enumerate the fibres of an invariant* problem. We are handed two invariants — $\chi_\alpha$ and $m_\alpha$ — and asked to describe every Jordan form mapping to that pair, i.e. to compute the fibre. As the topic page strategy [[Modules II — §3.3–3.4#Problem-Solving Strategy|notes]], understanding *which* invariants are complete and which are partial is done by exhibiting the fibre: the set of objects an invariant fails to separate.

**Assumption pattern.** The data are two factored polynomials over $\mathbb{C}$. The decisive structural fact is that the Jordan analysis *splits across eigenvalues*: the $\lambda$-block partition for $\lambda=2$ is constrained only by the $(X-2)$-exponents of $\chi_\alpha$ and $m_\alpha$, independently of $\lambda=5$. So the problem factors into one independent sub-problem per eigenvalue, and the answer is the *product* of the per-eigenvalue answer sets.

**Theorem routing.** The route is [[Thm - Jordan Normal Form|the Jordan theorem]] read through [[Thm - Primary Decomposition Theorem|primary decomposition]]. For each eigenvalue $\lambda$, the partition of $b_\lambda$ (the total) into $\lambda$-block sizes must have *largest part exactly* $a_\lambda$. Enumerate, for each $\lambda$, all partitions of $b_\lambda$ whose largest part is $a_\lambda$; the consistent Jordan forms are all combinations across eigenvalues.

**Key decision point.** The non-obvious recognition is *which* constraint each polynomial imposes. The characteristic polynomial fixes the *sum* of block sizes; the minimal polynomial fixes the *maximum*. Neither fixes the *number* of blocks (geometric multiplicity), so when an eigenvalue's exponent data leaves more than one partition with the prescribed sum-and-max, the Jordan form is genuinely undetermined by $(\chi_\alpha, m_\alpha)$. Spotting that "sum and max do not determine a partition" is the entire content of part 3.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Modules II — §3.3–3.4#Legal Operations|the topic page's Legal Operations]]:

1. **Split the analysis eigenvalue by eigenvalue.** The Jordan structure decomposes as a direct sum over distinct eigenvalues; the block partition at $\lambda$ depends only on the $(X-\lambda)$-exponents of $\chi_\alpha$ and $m_\alpha$, so treat each eigenvalue as an independent sub-problem.

2. **Read the algebraic multiplicity off the characteristic polynomial.** The exponent $b_\lambda$ of $(X-\lambda)$ in $\chi_\alpha$ is the total size contributed by $\lambda$ — the sum of the $\lambda$-block sizes.

3. **Read the largest-block size off the minimal polynomial.** The exponent $a_\lambda$ of $(X-\lambda)$ in $m_\alpha$ is the size of the largest Jordan $\lambda$-block.

4. **Enumerate partitions with a prescribed sum and largest part.** For each eigenvalue list every partition of $b_\lambda$ whose maximal part is exactly $a_\lambda$; each such partition is a candidate $\lambda$-block multiset.

5. **Form the product over eigenvalues.** Every consistent Jordan form is obtained by choosing one admissible partition at each eigenvalue independently; the count of consistent forms is the product of the per-eigenvalue counts.

6. **Detect incompleteness of an invariant by a non-singleton fibre.** When the admissible-partition set at some eigenvalue has more than one element, $(\chi_\alpha, m_\alpha)$ does not determine the Jordan form; the geometric multiplicity (block count) is the missing invariant.

---

# Hints

> [!note]- Hint 1
> The two eigenvalues $2$ and $5$ can be handled completely separately — the Jordan blocks for $\lambda=2$ have nothing to do with those for $\lambda=5$. For each eigenvalue, you must decide the multiset of block sizes. Two numbers constrain this multiset: one comes from $\chi_\alpha$, one from $m_\alpha$. Which exponent tells you the *total* of the block sizes, and which tells you the *largest*?

> [!note]- Hint 2
> The exponent of $(X-\lambda)$ in $\chi_\alpha$ is the algebraic multiplicity — the *sum* of the $\lambda$-block sizes. The exponent of $(X-\lambda)$ in $m_\alpha$ is the size of the *largest* $\lambda$-block. So for $\lambda=2$: the block sizes are positive integers summing to $3$ with largest part $2$. For $\lambda=5$: positive integers summing to $2$ with largest part $1$. Now just list the partitions.

> [!note]- Hint 3
> For $\lambda = 5$: partitions of $2$ with largest part $1$. The only partition of $2$ with all parts $\le 1$ is $1+1$. So $\lambda=5$ is forced: two blocks $J_1(5), J_1(5)$. There is *no* ambiguity at $5$. For $\lambda = 2$: partitions of $3$ with largest part exactly $2$ — list all partitions of $3$, then keep those whose biggest part is $2$.

> [!note]- Hint 4
> Partitions of $3$: $\;3\;$; $\;2+1\;$; $\;1+1+1$. Largest parts are $3, 2, 1$ respectively. Only $2+1$ has largest part exactly $2$. So $\lambda=2$ is *also* forced — blocks $J_2(2), J_1(2)$. In this particular problem the pair $(\chi_\alpha, m_\alpha)$ happens to determine the Jordan form *uniquely*. For part 3, you must explain *why* it worked here and construct a nearby example where it fails: take a characteristic polynomial with a higher exponent, say $(X-2)^4(X-5)^2$ with the same $m_\alpha$, and watch the ambiguity appear.

---

# Solution

The strategy is to translate each polynomial exponent into a constraint on a block-size partition, enumerate the admissible partitions eigenvalue by eigenvalue, and then ask whether the enumeration ever produced more than one option.

**Step 1: Translate the polynomial data into per-eigenvalue constraints.**

For $\lambda = 2$: block sizes are positive integers summing to $3$, with largest part $2$. For $\lambda = 5$: block sizes summing to $2$, with largest part $1$.

> [!note]- Derivation
> Read off the exponents. In $\chi_\alpha = (X-2)^3(X-5)^2$ the exponent of $(X-2)$ is $3$ and of $(X-5)$ is $2$; in $m_\alpha = (X-2)^2(X-5)^1$ the exponent of $(X-2)$ is $2$ and of $(X-5)$ is $1$.
>
> The two facts connecting these to block sizes, both consequences of [[Thm - Jordan Normal Form|the Jordan theorem]] / [[Thm - Primary Decomposition Theorem|primary decomposition]]:
> - The exponent of $(X-\lambda)$ in $\chi_\alpha$ is $b_\lambda$, the *sum* of the $\lambda$-block sizes. (The characteristic polynomial of a block-diagonal matrix is the product of the blocks' characteristic polynomials, and $J_m(\lambda)$ has characteristic polynomial $(X-\lambda)^m$; so the $(X-\lambda)$-exponent accumulates $\sum m$ over the $\lambda$-blocks.)
> - The exponent of $(X-\lambda)$ in $m_\alpha$ is $a_\lambda$, the *largest* $\lambda$-block size. (The polynomial $(X-\lambda)^k$ kills the summand $\mathbb{C}[X]/((X-\lambda)^m)$ if and only if $k \ge m$; to kill *all* $\lambda$-blocks one needs $k \ge \max m$, and the minimal such $k$ is the largest block size.)
>
> Hence:
> - **$\lambda = 2$:** the $2$-block sizes are positive integers with sum $b_2 = 3$ and maximum $a_2 = 2$.
> - **$\lambda = 5$:** the $5$-block sizes are positive integers with sum $b_5 = 2$ and maximum $a_5 = 1$.
>
> The problem now decouples: choose an admissible block partition at $\lambda=2$, choose one at $\lambda=5$, independently.

**Step 2: Enumerate admissible partitions at $\lambda = 5$.**

The only partition of $2$ with largest part $1$ is $1 + 1$. The eigenvalue $5$ contributes exactly **two $1\times 1$ blocks**, $J_1(5)$ and $J_1(5)$ — no ambiguity.

> [!note]- Derivation
> The partitions of $2$ are: $\;2\;$ (one part) and $\;1+1\;$ (two parts). Their largest parts are $2$ and $1$. The constraint $a_5 = 1$ forces the largest part to be $1$, eliminating the partition $2$. Only $1+1$ survives.
>
> So at $\lambda = 5$ the block structure is completely determined: two Jordan blocks of size $1$. In module terms, the $5$-primary part of $V_\alpha$ is $\mathbb{C}[X]/(X-5) \oplus \mathbb{C}[X]/(X-5)$. Note that $a_5 = 1$ means $(X-5)$ appears to the first power in $m_\alpha$, which says $\alpha$ is *diagonalisable on its $5$-eigenspace*: all $5$-blocks have size $1$.

**Step 3: Enumerate admissible partitions at $\lambda = 2$.**

The only partition of $3$ with largest part exactly $2$ is $2 + 1$. The eigenvalue $2$ contributes exactly one $J_2(2)$ and one $J_1(2)$ — again no ambiguity.

> [!note]- Derivation
> The partitions of $3$ are: $\;3\;$ (largest part $3$); $\;2+1\;$ (largest part $2$); $\;1+1+1\;$ (largest part $1$).
>
> The constraint is $a_2 = 2$: the largest part must be *exactly* $2$.
> - $3$ — largest part $3 \ne 2$. Rejected. (This would force $m_\alpha$ to contain $(X-2)^3$.)
> - $2+1$ — largest part $2$. **Accepted.**
> - $1+1+1$ — largest part $1 \ne 2$. Rejected. (This would force $m_\alpha$ to contain only $(X-2)^1$.)
>
> Exactly one partition survives: $2+1$. So at $\lambda = 2$ the block structure is also determined: one block of size $2$ and one of size $1$. The $2$-primary part of $V_\alpha$ is $\mathbb{C}[X]/((X-2)^2) \oplus \mathbb{C}[X]/(X-2)$.

**Step 4: Assemble — there is a unique consistent Jordan form.**

Combining the forced partitions at both eigenvalues, the *only* Jordan normal form consistent with the given $(\chi_\alpha, m_\alpha)$ is

$$J = \operatorname{diag}\big(J_2(2),\; J_1(2),\; J_1(5),\; J_1(5)\big) = \begin{pmatrix} 2 & 0 & & & \\ 1 & 2 & & & \\ & & 2 & & \\ & & & 5 & \\ & & & & 5 \end{pmatrix}.$$

> [!note]- Derivation
> Every Jordan form consistent with $(\chi_\alpha, m_\alpha)$ is obtained by choosing an admissible $\lambda$-partition at each eigenvalue independently (Step 1). Step 2 found exactly one admissible partition at $\lambda=5$, namely $1+1$; Step 3 found exactly one at $\lambda=2$, namely $2+1$. The number of consistent Jordan forms is the *product* of the per-eigenvalue counts: $1 \times 1 = 1$.
>
> So the consistent Jordan form is unique (up to reordering blocks). Its blocks are $J_2(2), J_1(2)$ from $\lambda=2$ and $J_1(5), J_1(5)$ from $\lambda=5$; the displayed $5\times 5$ matrix is one ordering. Sanity check: the diagonal entries are $2,2,2,5,5$, so $\chi_\alpha = (X-2)^3(X-5)^2$; the largest blocks have sizes $2$ (for $\lambda=2$) and $1$ (for $\lambda=5$), so $m_\alpha = (X-2)^2(X-5)$. Both match the data.

**Step 5: Where $(\chi_\alpha, m_\alpha)$ fails to be a complete invariant.**

The pair $(\chi_\alpha, m_\alpha)$ determined the Jordan form *here* only because every eigenvalue's "sum and max" admitted a unique partition. In general the pair is **not** a complete invariant: the missing datum is the *number* of blocks per eigenvalue, i.e. the geometric multiplicity $\dim\ker(\alpha-\lambda I)$.

> [!note]- Derivation
> The pair $(b_\lambda, a_\lambda)$ — sum and maximum of a partition — does *not* determine the partition once $b_\lambda$ is large enough. The smallest failure is $b_\lambda = 4$, $a_\lambda = 2$: the partitions of $4$ with largest part exactly $2$ are
> $$2 + 2 \qquad \text{and} \qquad 2 + 1 + 1,$$
> two distinct partitions with the same sum and the same maximum. They differ in the *number of parts* — two parts versus three.
>
> Concretely, modify the present problem to $\chi_\alpha = (X-2)^4(X-5)^2$ with the *same* $m_\alpha = (X-2)^2(X-5)$. Now $b_2 = 4$, $a_2 = 2$, and the eigenvalue $2$ admits *two* block structures:
> $$\{J_2(2), J_2(2)\} \qquad \text{or} \qquad \{J_2(2), J_1(2), J_1(2)\}.$$
> Both give characteristic polynomial $(X-2)^4$ on the $2$-part and minimal polynomial $(X-2)^2$; the pair $(\chi_\alpha, m_\alpha)$ cannot tell them apart. The two are distinguished by the *number of $2$-blocks* — two versus three — which is the **geometric multiplicity** $\dim\ker(\alpha - 2I)$. Adding that one number per eigenvalue (or, fully, the [[Def - Dimension|dimensions]] $\dim\ker(\alpha-\lambda I)^k$ for all $k$) pins the partition down completely.
>
> So the precise statement: $(\chi_\alpha, m_\alpha)$ is a complete invariant of $\alpha$ up to similarity **if and only if**, for every eigenvalue, the "sum $b_\lambda$, max $a_\lambda$" data forces a unique partition — which happens exactly when $b_\lambda \le a_\lambda + 1$, or $a_\lambda \in \{1, b_\lambda\}$, the small cases. The given problem fell into this lucky regime at *both* eigenvalues ($\lambda=2$: $b_2=3, a_2=2$, and $3 \le 2+1$; $\lambda=5$: $a_5 = 1$). The complete similarity invariant, valid with no luck required, is the full list of elementary divisors — equivalently the rational canonical form, equivalently the Smith normal form of $XI - A$.

> [!note]- Complete formal solution
> **Claim.** The pair $\chi_\alpha = (X-2)^3(X-5)^2$, $m_\alpha = (X-2)^2(X-5)$ is consistent with exactly one Jordan normal form, $\operatorname{diag}(J_2(2), J_1(2), J_1(5), J_1(5))$; in general $(\chi_\alpha, m_\alpha)$ is not a complete similarity invariant, the missing datum being the per-eigenvalue block count $\dim\ker(\alpha-\lambda I)$.
>
> *Constraints.* For each eigenvalue $\lambda$, the $\lambda$-block sizes form a partition of $b_\lambda := [\,(X-\lambda)$-exponent of $\chi_\alpha\,]$ with largest part $a_\lambda := [\,(X-\lambda)$-exponent of $m_\alpha\,]$. Here $b_2 = 3, a_2 = 2$ and $b_5 = 2, a_5 = 1$.
>
> *Eigenvalue $5$.* Partitions of $2$ with largest part $1$: only $1+1$. Blocks: $J_1(5), J_1(5)$.
>
> *Eigenvalue $2$.* Partitions of $3$ with largest part exactly $2$: among $3,\,2+1,\,1+1+1$ only $2+1$ qualifies. Blocks: $J_2(2), J_1(2)$.
>
> *Assembly.* Each eigenvalue admits a unique partition, so the consistent Jordan form is unique: $\operatorname{diag}(J_2(2), J_1(2), J_1(5), J_1(5))$.
>
> *Incompleteness.* "Sum and maximum" determine a partition only in degenerate cases. For $b_\lambda = 4, a_\lambda = 2$ the partitions $2+2$ and $2+1+1$ share both invariants but differ in part-count. Hence with $\chi_\alpha = (X-2)^4(X-5)^2$ and the same $m_\alpha$, the eigenvalue $2$ admits two Jordan structures, separated only by $\dim\ker(\alpha-2I)$. The complete invariant is the full elementary-divisor list. $\blacksquare$

---

# Key Takeaways

**The minimal polynomial records the *maximum* block size; the characteristic polynomial records the *sum*. Both, per eigenvalue.** This is the central dictionary of the exercise, and it is worth committing to muscle memory. For each eigenvalue $\lambda$, the Jordan structure is a *partition* — a multiset of block sizes. The exponent of $(X-\lambda)$ in $\chi_\alpha$ is the **sum** of that partition (the algebraic multiplicity), because characteristic polynomials of blocks multiply. The exponent of $(X-\lambda)$ in $m_\alpha$ is the **largest part** of that partition, because $(X-\lambda)^k$ annihilates the $\lambda$-primary part exactly when $k$ reaches the biggest block. So reading $(\chi_\alpha, m_\alpha)$ is reading, for each eigenvalue, a (sum, max) pair for an unknown partition. The trigger "I know $\chi_\alpha$ and $m_\alpha$, what is the Jordan form?" should fire the reaction "per eigenvalue: total from $\chi_\alpha$, biggest block from $m_\alpha$, then enumerate partitions". A first useful corollary: $\alpha$ is diagonalisable if and only if $m_\alpha$ is squarefree, because squarefree $m_\alpha$ means every largest block has size $1$, hence every block has size $1$.

**Jordan analysis factors over eigenvalues — solve one prime at a time.** The reason the problem was tractable is that the eigenvalues $2$ and $5$ were *independent*: the $2$-block partition is constrained only by the $(X-2)$-exponents, the $5$-block partition only by the $(X-5)$-exponents, and the consistent Jordan forms are the *product* of the per-eigenvalue solution sets. Structurally this is the [[Thm - Primary Decomposition Theorem|primary decomposition]]: $V_\alpha$ splits as a direct sum of $\lambda$-primary parts, one per eigenvalue, and each part is analysed in isolation. This "factor over primes" move is universal in module theory over a PID — the structure of a finitely generated abelian group is likewise determined prime by prime — and it is the right first step for *any* question about Jordan or rational canonical structure: never reason about the whole operator at once when you can reason about one eigenvalue (one prime) at a time. The count of consistent global forms is then a product of independent local counts.

**A partition is not determined by its sum and maximum — this is the precise gap between $(\chi_\alpha, m_\alpha)$ and a complete invariant.** The deepest takeaway is *why* $(\chi_\alpha, m_\alpha)$ is an *incomplete* similarity invariant, and exactly how incomplete. The pair gives, per eigenvalue, the sum and the maximum of the block partition — but a partition has a third feature these miss: the *number of parts*, equivalently the geometric multiplicity $\dim\ker(\alpha-\lambda I)$. Sum and maximum pin a partition only in degenerate ranges ($a_\lambda \in \{1, b_\lambda\}$, or $b_\lambda \le a_\lambda+1$); the smallest genuine ambiguity is sum $4$, max $2$, where $2+2$ and $2+1+1$ are indistinguishable. The present exercise happened to land in the degenerate range at both eigenvalues, which is *why* the Jordan form came out unique — but that is luck, not a theorem. The honest complete invariant is the full multiset of **elementary divisors** (equivalently the rational canonical form, equivalently the Smith normal form of $XI-A$, equivalently the dimensions $\dim\ker(\alpha-\lambda I)^k$ for all $\lambda, k$). The general lesson for invariant-theory problems: to test whether a proposed invariant is complete, hunt for the smallest pair of non-isomorphic objects it identifies — the smallest non-singleton fibre — and whatever feature separates that pair is exactly the missing invariant. Here that feature is "how the generalised eigenspaces grow", and naming it both diagnoses the gap and tells you what extra measurement closes it.

**Enumerate by listing partitions with prescribed constraints — a reusable counting skill.** Operationally, the entire exercise reduced to "list the partitions of $n$ with largest part $k$". This is a small but recurring combinatorial subroutine in canonical-form questions: counting the matrices with a given characteristic and minimal polynomial, counting the conjugacy classes of nilpotent matrices of a fixed size (partitions of $n$, no constraint), counting the abelian [[Def - Group|groups]] of order $p^n$ (again partitions of $n$). The discipline is always the same — write out *all* partitions of the total, then filter by the maximum-part (or part-count) constraint. When the filtered list has one element the structure is forced; when it has several, you have found exactly where the given invariants run out and must report the residual ambiguity. Being fluent at "partitions of $n$ with largest part $k$" turns every such classification question into a short, mechanical enumeration.
