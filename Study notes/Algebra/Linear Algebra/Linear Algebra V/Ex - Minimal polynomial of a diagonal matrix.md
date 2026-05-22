---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Minimal Polynomial"
  - "Def - Diagonalizable Operator"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a finite-dimensional vector space over $F$ and $T \in \mathcal{L}(V)$ be diagonal in some basis $v_1, \ldots, v_n$, with diagonal entries $\mu_1, \mu_2, \ldots, \mu_n \in F$ (some possibly repeated). Let $\lambda_1, \lambda_2, \ldots, \lambda_m$ be the *distinct* values among $\mu_1, \ldots, \mu_n$. Show that the minimal polynomial of $T$ is
$$m_T(z) = (z - \lambda_1)(z - \lambda_2) \cdots (z - \lambda_m).$$

**Recall:**

![[Def - Minimal Polynomial#The Definition]]

A polynomial is **monic** if its leading coefficient is $1$. The minimal polynomial is unique with smallest positive degree among monic annihilators of $T$.

A **diagonal matrix** $\operatorname{diag}(\mu_1, \ldots, \mu_n)$ acts on the basis $v_1, \ldots, v_n$ as $T v_k = \mu_k v_k$. So each $v_k$ is an eigenvector with eigenvalue $\mu_k$.

---

# Convergent Strategy

**Problem class.** This is a direct computation of the minimal polynomial of a known operator. The diagonal form makes everything explicit, so the structural facts about $m_T$ (its degree, its roots, its uniqueness) can be verified by inspection.

**Assumption pattern.** The recognisable signal is that $T$ acts on each basis vector by scalar multiplication. So $(T - \lambda I) v_k = (\mu_k - \lambda) v_k$ for any $\lambda$, and $(T - \lambda I) v_k = 0$ exactly when $\mu_k = \lambda$. By taking a product over the *distinct* values $\lambda_1, \ldots, \lambda_m$, every $v_k$ is killed by exactly one factor, hence by the product.

**Theorem routing.** Use the **characterization of the minimal polynomial as the smallest-degree monic annihilator**, plus **the divisibility property**: any monic annihilator is a multiple of $m_T$, so $m_T$ divides $(z - \lambda_1) \cdots (z - \lambda_m)$. Conversely, $m_T$ must vanish at each eigenvalue (by [[Thm - Eigenvalues are Zeros of the Minimal Polynomial]]), so $(z - \lambda_k) \mid m_T$ for each distinct $\lambda_k$; combining, the product divides $m_T$. So $m_T = \prod (z - \lambda_k)$.

**Key decision point.** The non-obvious step (if it can be called that) is to recognise that $m_T$ has only the *distinct* eigenvalues as roots — not the eigenvalues with multiplicity. The multiplicity comes from the *characteristic polynomial* $\chi_T$, not from the minimal polynomial. So even when $\mu_1 = \mu_2 = \cdots = \mu_n = 7$ (a scalar matrix), the minimal polynomial is just $z - 7$, not $(z - 7)^n$.

---

# Legal Operations Used

1. **Compute the minimal polynomial by the iterate algorithm** (operation 3 from the topic page). For a diagonal matrix, the iterate algorithm is replaced by direct evaluation: each basis vector is an eigenvector, so we directly check which polynomial annihilates the basis.

2. **Diagonalize via the minimal polynomial** (operation 6). The result — $m_T$ has distinct linear factors — is exactly the characterisation of diagonalisability ([[Thm - Conditions for Diagonalizability]]), confirming consistency.

3. **Translate operator equations to divisibility of $m_T$** (operation 4). Once we show $\prod (T - \lambda_k I) = 0$, we conclude $m_T \mid \prod (z - \lambda_k)$.

---

# Hints

> [!note]- Hint 1
> Each basis vector $v_k$ is an eigenvector with eigenvalue $\mu_k$. So $(T - \mu_k I) v_k = 0$ and $(T - \lambda I) v_k = (\mu_k - \lambda) v_k$ for any $\lambda \neq \mu_k$.

> [!note]- Hint 2
> The product $\prod_{k=1}^m (T - \lambda_k I)$ acts on $v_j$ (with eigenvalue $\mu_j$) as the scalar $\prod_{k=1}^m (\mu_j - \lambda_k)$. Since $\mu_j$ equals one of the $\lambda_k$, one factor is zero. So the product kills $v_j$.

> [!note]- Hint 3
> The product $\prod_k (T - \lambda_k I)$ kills every basis vector, hence is the zero operator. So $m_T \mid \prod_k (z - \lambda_k)$. For the converse: $m_T$ vanishes at each eigenvalue (by [[Thm - Eigenvalues are Zeros of the Minimal Polynomial]]), so each $(z - \lambda_k)$ divides $m_T$.

---

# Solution

The plan is to show that the polynomial $p(z) = \prod_k (z - \lambda_k)$ annihilates $T$ (so $m_T$ divides $p$), and conversely that $m_T$ must have each $\lambda_k$ as a root (so $p$ divides $m_T$). Combining, $m_T = p$.

**Step 1: $p(z) = \prod_{k=1}^m (z - \lambda_k)$ annihilates $T$.**

Show that $p(T) v_j = 0$ for every basis vector $v_j$, hence $p(T) = 0$ as an operator on $V$.

> [!note]- Derivation
> Take any basis vector $v_j$. It is an eigenvector of $T$ with eigenvalue $\mu_j$, which equals one of the distinct values $\lambda_1, \ldots, \lambda_m$. Say $\mu_j = \lambda_{k_0}$.
>
> Compute $p(T) v_j$ using the polynomial expansion and the fact that any two polynomials in the same operator commute:
> $$p(T) v_j = \prod_{k=1}^m (T - \lambda_k I) v_j.$$
> By [[Thm - Eigenvalues are Zeros of the Minimal Polynomial|Lemma 1 of the eigenvalue-zero theorem]], $(T - \lambda_k I) v_j = (\mu_j - \lambda_k) v_j = (\lambda_{k_0} - \lambda_k) v_j$. So
> $$p(T) v_j = \left(\prod_{k=1}^m (\lambda_{k_0} - \lambda_k)\right) v_j.$$
> The product $\prod_{k=1}^m (\lambda_{k_0} - \lambda_k)$ contains the factor $(\lambda_{k_0} - \lambda_{k_0}) = 0$, so it is zero. Hence $p(T) v_j = 0$.
>
> Since $p(T)$ vanishes on every basis vector $v_j$ and $\{v_1, \ldots, v_n\}$ is a basis of $V$, $p(T)$ is the zero operator on $V$. Hence $p(T) = 0$, i.e. $m_T \mid p$.

**Step 2: Each $(z - \lambda_k)$ divides $m_T$.**

> [!note]- Derivation
> Each $\lambda_k$ is an eigenvalue of $T$ — indeed, it is among the diagonal entries $\mu_1, \ldots, \mu_n$, hence some basis vector $v_{j_k}$ has $T v_{j_k} = \lambda_k v_{j_k}$, so $\lambda_k$ is an eigenvalue with eigenvector $v_{j_k}$.
>
> By [[Thm - Eigenvalues are Zeros of the Minimal Polynomial]], every eigenvalue of $T$ is a root of $m_T$. So $m_T(\lambda_k) = 0$, hence by the [[Def - Division Algorithm and Factorization|factor theorem]], $(z - \lambda_k)$ divides $m_T$.
>
> Since the linear factors $(z - \lambda_k)$ for distinct $\lambda_k$ are pairwise coprime, their product $p(z) = \prod_{k=1}^m (z - \lambda_k)$ also divides $m_T$.

**Step 3: $m_T = p$.**

> [!note]- Derivation
> By Step 1, $m_T \mid p$. By Step 2, $p \mid m_T$. So $m_T$ and $p$ divide each other; since both are monic polynomials, they are equal:
> $$m_T(z) = (z - \lambda_1)(z - \lambda_2) \cdots (z - \lambda_m).$$
> $\blacksquare$

> [!note]- Complete formal solution
> Let $T \in \mathcal{L}(V)$ have diagonal matrix $\operatorname{diag}(\mu_1, \ldots, \mu_n)$ in the basis $v_1, \ldots, v_n$, and let $\lambda_1, \ldots, \lambda_m$ be the distinct values among $\{\mu_1, \ldots, \mu_n\}$. Define $p(z) = \prod_{k=1}^m (z - \lambda_k)$.
>
> *$p(T) = 0$.* For each basis vector $v_j$ with eigenvalue $\mu_j$, the polynomial $p$ evaluated at $T$ acts on $v_j$ as the scalar $p(\mu_j)$:
> $$p(T) v_j = p(\mu_j) v_j = \left(\prod_k (\mu_j - \lambda_k)\right) v_j.$$
> Since $\mu_j$ equals some $\lambda_{k_0}$ (by definition of "distinct values"), the factor $(\mu_j - \lambda_{k_0}) = 0$ is in the product, so $p(\mu_j) = 0$, hence $p(T) v_j = 0$. This holds for every basis vector, so $p(T) = 0$. Hence $m_T \mid p$.
>
> *$p \mid m_T$.* Each $\lambda_k$ is an eigenvalue of $T$ (the basis vectors with $\mu_{j_k} = \lambda_k$ are eigenvectors), so by [[Thm - Eigenvalues are Zeros of the Minimal Polynomial]], $(z - \lambda_k)$ divides $m_T$. The factors $(z - \lambda_k)$ for distinct $\lambda_k$ are pairwise coprime, so their product $p$ divides $m_T$.
>
> *Conclude.* Both $m_T$ and $p$ are monic and divide each other, so $m_T = p = \prod_k (z - \lambda_k)$. $\blacksquare$

> [!note]- Sanity check via diagonalisability
> The result is consistent with [[Thm - Conditions for Diagonalizability]]: $T$ is diagonalisable (given), so $m_T$ must factor as a product of *distinct* linear factors over $F$. The answer $m_T = \prod_{k=1}^m (z - \lambda_k)$ has exactly distinct linear factors, confirming the consistency check. Conversely, the diagonalisability theorem says that *any* operator with $m_T = \prod (z - \lambda_k)$ for distinct $\lambda_k$ is diagonalisable.

---

# Key Takeaways

**The minimal polynomial sees the *distinct* eigenvalues, not the eigenvalues with multiplicity.** The most common error in computing minimal polynomials of diagonal (or diagonalisable) matrices is including multiplicities. The matrix $\operatorname{diag}(5, 5, 5)$ has minimal polynomial $z - 5$, *not* $(z - 5)^3$ — even though the eigenvalue $5$ has algebraic multiplicity $3$. The minimal polynomial corresponds to the *distinct* eigenvalues; the multiplicities are encoded in the characteristic polynomial $\chi_T = \prod_k (z - \mu_k) = \prod_k (z - \lambda_k)^{a_k}$ (the product of $(z - \mu_k)$ over all $n$ diagonal entries including repetitions, which equals the product of $(z - \lambda_k)^{a_k}$ over distinct eigenvalues with $a_k$ counting the repetitions). The pair $(m_T, \chi_T)$ records different information: $m_T$ records "which Jordan blocks at most" (the size of the largest Jordan block at each eigenvalue); $\chi_T$ records "the total sum of Jordan block sizes at each eigenvalue". For diagonal matrices, all Jordan blocks have size $1$, so $m_T$ has distinct linear factors, while $\chi_T$ has the eigenvalues with multiplicity.

**The diagonalisability characterisation $m_T = \prod_k (z - \lambda_k)$ for distinct $\lambda_k$ is *the* practical test.** Once you know $m_T$ has distinct linear factors over $F$, you know $T$ is diagonalisable. The converse — that diagonalisability implies $m_T$ has distinct linear factors — is what this exercise verifies in the concrete case. The implication "$T$ is diagonal ⟹ $m_T$ has distinct linear factors" is the basis for the more general "$T$ is diagonalisable ⟹ $m_T$ has distinct linear factors", since a diagonalisable operator is similar to a diagonal one and similar operators have the same minimal polynomial.

**A trigger-reaction pattern: "compute $m_T$ of an explicit operator" → reach for the iterate or direct-relation approach.** For a diagonal matrix, the direct approach via "$p(T) v_j$ acts as the scalar $p(\mu_j)$" is fastest. For a general matrix, the iterate algorithm (find the smallest $m$ with $T^m v$ in the span of $v, Tv, \ldots, T^{m-1}v$) is the workhorse, often combined with looking for an obvious polynomial relation $p(T) = 0$ from special structure. In each case, the minimal polynomial is constructed and then characterised by its divisibility property.
