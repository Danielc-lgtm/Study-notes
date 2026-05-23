---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Determinant"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $A$ be an $n \times n$ upper-triangular matrix with diagonal entries $\lambda_1, \dots, \lambda_n$, i.e., $A_{ij} = 0$ whenever $i > j$. Show that

$$\det A \;=\; \lambda_1 \cdot \lambda_2 \cdots \lambda_n.$$

**Recall:**

![[Def - Determinant#The Definition]]

The **Leibniz formula** ([[Def - Determinant|LADR 9.46]]) is

$$\det A = \sum_{\sigma \in \operatorname{perm}(n)} \operatorname{sign}(\sigma)\, A_{\sigma(1), 1} \cdot A_{\sigma(2), 2} \cdots A_{\sigma(n), n}.$$

A matrix $A$ is **upper-triangular** if $A_{ij} = 0$ whenever $i > j$. Equivalently, all entries below the diagonal are zero. The **diagonal entries** are $A_{11}, A_{22}, \dots, A_{nn}$.

A **permutation** of $\{1, \dots, n\}$ is a bijection $\sigma : \{1, \dots, n\} \to \{1, \dots, n\}$. The **identity permutation** is $\sigma(k) = k$ for all $k$.

---

# Convergent Strategy

**Problem class.** This is a direct application of the Leibniz formula combined with the zero-pattern of an upper-triangular matrix. It is the foundational determinantal computation: every routine determinant calculation (Gaussian elimination, LU decomposition) reduces to this one. As the [[Linear Algebra IX — §9 Multilinear Algebra and Determinants#Problem-Solving Strategy|topic page strategy]] indicates, "compute a determinant" is one of the five recurring problem classes, and "triangular or block-triangular" is the case where the answer is read off in one step.

**Assumption pattern.** $A$ is upper-triangular, meaning many entries are zero. The Leibniz formula is a sum over *all* permutations, with each term a product over all rows. The assumption guarantees that *most* terms vanish — specifically, every term except the one corresponding to the identity permutation.

**Theorem routing.** Apply the [[Def - Determinant|Leibniz formula]] (LADR 9.46): $\det A = \sum_\sigma \operatorname{sign}(\sigma) \prod_k A_{\sigma(k), k}$. The route is to show that for every $\sigma \neq \operatorname{id}$, the product $\prod_k A_{\sigma(k), k}$ contains at least one zero factor (because $A_{\sigma(k), k}$ is below-diagonal for some $k$). Only the identity permutation contributes the product $\prod_k A_{kk} = \prod \lambda_k$.

**Key decision point.** The non-obvious move is recognising that for $\sigma \neq \operatorname{id}$, *some* $\sigma(k) > k$ — and the way to see this is the following: if $\sigma(k) \leq k$ for all $k$, then $\sigma(1) = 1$ (since $\sigma(1) \in \{1\}$), $\sigma(2) \in \{1, 2\}$, but $\sigma(2) \neq \sigma(1) = 1$, so $\sigma(2) = 2$, and so on inductively, forcing $\sigma = \operatorname{id}$. So $\sigma \neq \operatorname{id}$ forces $\sigma(k) > k$ for some $k$. This pigeonhole-style argument is the crux.

---

# Legal Operations Used

1. **Compute a determinant via cofactor expansion when the matrix has zeros** (operation 6 from the topic page). This problem is the cleanest instance: the upper-triangular structure makes cofactor expansion (or Leibniz) collapse to a single term.

2. **Use the abstract definition of the determinant** (operation in spirit). The Leibniz formula is the explicit computational form of the alternating-multilinear definition of $\det$.

---

# Hints

> [!note]- Hint 1
> Apply the Leibniz formula directly. The sum has $n!$ terms; most of them will be zero. Which ones are nonzero?

> [!note]- Hint 2
> A term $A_{\sigma(1), 1} A_{\sigma(2), 2} \cdots A_{\sigma(n), n}$ is nonzero only if every factor $A_{\sigma(k), k}$ is nonzero — that is, only if $\sigma(k) \leq k$ for all $k$ (since $A_{ij} = 0$ for $i > j$). What does this constraint, combined with $\sigma$ being a permutation, force?

> [!note]- Hint 3
> If $\sigma(k) \leq k$ for all $k$, then $\sigma(1) \in \{1\}$, $\sigma(2) \in \{1, 2\} \setminus \{\sigma(1)\}$, etc. By induction, $\sigma$ must be the identity. So only one term survives.

---

# Solution

The plan is to apply Leibniz, observe that any non-identity permutation forces a below-diagonal (hence zero) factor, and read off the survival of the identity permutation's contribution.

**Step 1: Set up the Leibniz sum.**

By the Leibniz formula, $\det A = \sum_\sigma \operatorname{sign}(\sigma) \prod_{k=1}^n A_{\sigma(k), k}$.

> [!note]- Derivation
> The [[Def - Determinant|determinant formula]] is
> $$\det A = \sum_{\sigma \in \operatorname{perm}(n)} \operatorname{sign}(\sigma)\, A_{\sigma(1), 1} \cdots A_{\sigma(n), n}.$$
> Each term in the sum corresponds to a permutation $\sigma$ and is a signed product of $n$ matrix entries, one from each column with the row indexed by $\sigma$.

**Step 2: Identify which permutations contribute nonzero terms.**

A term is nonzero iff $\sigma(k) \leq k$ for all $k$, which forces $\sigma = \operatorname{id}$.

> [!note]- Derivation
> Suppose the product $A_{\sigma(1), 1} A_{\sigma(2), 2} \cdots A_{\sigma(n), n}$ is nonzero. Then every factor $A_{\sigma(k), k} \neq 0$, which means (since $A$ is upper-triangular) that $\sigma(k) \leq k$ for every $k \in \{1, \dots, n\}$.
>
> Now we claim that the only permutation $\sigma$ with $\sigma(k) \leq k$ for all $k$ is the identity.
>
> Proof by induction on $k$: $\sigma(1) \leq 1$ implies $\sigma(1) = 1$ (since $\sigma$ takes positive integer values $\geq 1$). Assume $\sigma(1) = 1, \sigma(2) = 2, \dots, \sigma(k-1) = k-1$. Then $\sigma(k) \in \{1, 2, \dots, k\} \setminus \{1, 2, \dots, k-1\} = \{k\}$ (using the constraint $\sigma(k) \leq k$ and that $\sigma$ is injective). So $\sigma(k) = k$.
>
> By induction, $\sigma = \operatorname{id}$.

**Step 3: Compute the contribution of the identity permutation.**

For $\sigma = \operatorname{id}$, $\operatorname{sign}(\operatorname{id}) = +1$ and the product is $A_{1,1} A_{2,2} \cdots A_{n,n} = \lambda_1 \lambda_2 \cdots \lambda_n$.

> [!note]- Derivation
> $\operatorname{sign}(\operatorname{id}) = 1$ (the identity permutation has zero inversions).
>
> The product $\prod_{k=1}^n A_{\operatorname{id}(k), k} = \prod_{k=1}^n A_{kk} = A_{11} A_{22} \cdots A_{nn} = \lambda_1 \lambda_2 \cdots \lambda_n$ by the definition $\lambda_k := A_{kk}$.

**Step 4: Conclude.**

Only the identity contributes, so $\det A = \lambda_1 \lambda_2 \cdots \lambda_n$.

> [!note]- Derivation
> Every term in the Leibniz sum is zero except the one with $\sigma = \operatorname{id}$, which contributes $+\lambda_1 \lambda_2 \cdots \lambda_n$. So
> $$\det A = \lambda_1 \cdot \lambda_2 \cdots \lambda_n.$$
> $\blacksquare$

> [!note]- Complete formal solution
> By the [[Def - Determinant|Leibniz formula]],
> $$\det A = \sum_{\sigma \in \operatorname{perm}(n)} \operatorname{sign}(\sigma)\, A_{\sigma(1), 1} A_{\sigma(2), 2} \cdots A_{\sigma(n), n}.$$
>
> Suppose $\sigma \in \operatorname{perm}(n)$ is such that the product $A_{\sigma(1), 1} \cdots A_{\sigma(n), n} \neq 0$. Then every $A_{\sigma(k), k} \neq 0$, which (since $A$ is upper-triangular) requires $\sigma(k) \leq k$ for all $k$. We show this forces $\sigma = \operatorname{id}$ by induction: $\sigma(1) = 1$ (as $\sigma(1) \leq 1$ and $\sigma(1) \geq 1$); given $\sigma(1) = 1, \dots, \sigma(k-1) = k-1$, the value $\sigma(k) \in \{1, \dots, k\}$ must avoid $1, \dots, k-1$ (by injectivity), so $\sigma(k) = k$.
>
> Hence only the identity permutation contributes a nonzero term, and that contribution is $\operatorname{sign}(\operatorname{id}) \cdot A_{11} A_{22} \cdots A_{nn} = (+1) \lambda_1 \lambda_2 \cdots \lambda_n$. So
> $$\det A = \lambda_1 \lambda_2 \cdots \lambda_n. \qquad \blacksquare$$

---

# Key Takeaways

**The Leibniz formula collapses dramatically for sparse matrices.** This is the structural reason cofactor expansion and Gaussian elimination work as determinant algorithms: they reduce the matrix to a form (triangular or block-triangular) where only one permutation contributes, and the answer is a simple product. Every routine computation of a determinant in practice converts the matrix to a triangular form (via row operations that track how $\det$ changes) and reads off the diagonal product. The same reasoning extends to **block-triangular** matrices ($\det$ = product of block [[Def - Determinant|determinants]]) and to matrices with zero rows or columns ($\det = 0$). The trigger to recognise: any matrix with structure that limits which permutations can contribute is a candidate for this technique. Conversely, if you find yourself contemplating all $n!$ permutations for $n \geq 5$, you have probably missed a structural simplification.

**The argument generalises to "all-or-nothing" permutation-survival.** The technical content of the proof — "if $\sigma(k) \leq k$ for all $k$ then $\sigma = \operatorname{id}$" — is a pigeonhole-style argument about permutations, and it generalises immediately. For instance, a **lower-triangular** matrix has $A_{ij} = 0$ for $i < j$, so nonzero terms require $\sigma(k) \geq k$, which by the same argument forces $\sigma = \operatorname{id}$ — hence $\det$ = diagonal product for lower-triangular too. For a **block-upper-triangular** matrix with diagonal blocks of sizes $n_1, n_2, \dots$, nonzero terms require $\sigma$ to permute *within* each block, giving $\det$ = product of block [[Def - Determinant|determinants]]. The general lesson: the Leibniz sum's structure mirrors the matrix's structure, and zero-pattern in the matrix translates directly into permutation-restriction in the sum.

**This is the engine behind "$\det T = \prod \lambda_i$".** The eigenvalue-product formula for $\det$ on a complex vector space (see [[Thm - Determinant Equals Product of Eigenvalues with Multiplicity]]) reduces every $\det$ computation to this exercise via Schur's upper-triangularisation theorem: every complex operator has an upper-triangular matrix in some basis, with eigenvalues on the diagonal. So once Schur is in hand, this exercise gives $\det T = \prod \lambda_i$ in one line. The conceptual chain is: alternating-multilinear-uniqueness defines $\det$; Schur reduces to upper-triangular; this exercise reads off the diagonal. The fact that the most powerful theorem about determinants ("$\det = $ product of eigenvalues") rests on the simplest computational lemma is one of the satisfying structural patterns of linear algebra.
