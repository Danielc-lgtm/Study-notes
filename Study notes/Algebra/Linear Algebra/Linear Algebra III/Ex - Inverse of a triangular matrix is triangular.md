---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Matrix of a Linear Map"
  - "Def - Matrix Multiplication"
  - "Def - Invertibility and Isomorphism"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $A \in \mathbf{F}^{n, n}$ be an invertible upper-triangular matrix — i.e., $A_{j, k} = 0$ whenever $j > k$, and $A$ has a two-sided inverse. Show that $A^{-1}$ is also upper-triangular, and that the diagonal entries of $A^{-1}$ are the reciprocals of the diagonal entries of $A$:
$$(A^{-1})_{k, k} \;=\; (A_{k, k})^{-1}.$$
The same conclusion holds for lower-triangular invertible matrices.

**Recall:**

A matrix $A \in \mathbf{F}^{n, n}$ is **upper-triangular** if $A_{j, k} = 0$ for all $j > k$, i.e., all entries below the diagonal are zero. Lower-triangular is defined symmetrically.

![[Def - Invertibility and Isomorphism#The Definition]]

For a triangular matrix, the **diagonal entries** $A_{1, 1}, A_{2, 2}, \ldots, A_{n, n}$ are the entries on the main diagonal. An upper-triangular matrix is invertible iff all diagonal entries are non-zero (its determinant is the product of the diagonal entries; we will use the equivalent fact that an upper-triangular matrix has the *standard subspaces* $\operatorname{span}(e_1, \ldots, e_k)$ as invariant subspaces).

---

# Convergent Strategy

**Problem class.** This is a *structural property of the inverse* problem. The topic-page Problem-Solving Strategy categorises it under "matrix-level computation with structural input": exploit that triangularity has a clean structural meaning (the standard subspaces $V_k = \operatorname{span}(e_1, \ldots, e_k)$ are invariant), and check that the inverse preserves it.

**Assumption pattern.** $A$ is upper-triangular and invertible, hence has non-zero diagonal entries. The defining feature: triangularity is equivalent to a chain of invariant subspaces, and invertibility plus this chain forces the inverse to also preserve the chain.

**Theorem routing.** The cleanest argument: triangularity of $A$ means $A V_k \subseteq V_k$ for each $k$ (where $V_k = \operatorname{span}(e_1, \ldots, e_k)$). Since $A$ is invertible and these are equal-dimension subspaces ($\dim AV_k \leq \dim V_k = k$, but $A$ is injective on $V_k$ so $\dim A V_k = k$, and $AV_k \subseteq V_k$ forces $AV_k = V_k$), $A^{-1}$ also satisfies $A^{-1} V_k = V_k$ for each $k$, which is equivalent to $A^{-1}$ being upper-triangular.

For the diagonal entries: from $AA^{-1} = I_n$, the $(k, k)$-entry gives $\sum_r A_{k, r} (A^{-1})_{r, k} = 1$. The sum collapses by triangularity: $A_{k, r} = 0$ for $r < k$, and $(A^{-1})_{r, k} = 0$ for $r > k$, so only $r = k$ survives, giving $A_{k, k} (A^{-1})_{k, k} = 1$, i.e., $(A^{-1})_{k, k} = (A_{k, k})^{-1}$.

**Key decision point.** The crucial choice is to translate "triangular" into the invariant-subspace condition $A V_k \subseteq V_k$. Direct computation of $A^{-1}$ by adjoint formulas or Gauss–Jordan is possible but messy; the invariant-subspace reformulation makes everything clean. The "key decision" is also to deduce the diagonal entries by reading off a specific entry of $AA^{-1} = I_n$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra III — §3A–D Linear Maps#Legal Operations|the topic page's Legal Operations]]:

1. **Pass between a linear map and its matrix** (operation 6). Triangularity is a basis-dependent matrix property, but it has the basis-free interpretation "the chain of subspaces $V_k = \operatorname{span}(e_1, \ldots, e_k)$ is invariant".

2. **Use $\mathcal{M}(ST) = \mathcal{M}(S)\mathcal{M}(T)$** (operation 7). Reading off entries of $AA^{-1}$ via matrix multiplication.

3. **Convert injectivity to surjectivity (or vice versa) using equal finite dimension** (operation 4). In the invariant-subspace argument: $A V_k \subseteq V_k$ plus $A$ invertible (hence injective on $V_k$) plus $\dim V_k = k$ forces $A V_k = V_k$.

4. **Decompose a domain via $V = \operatorname{null} T \oplus U$** (operation 9), used implicitly via invariant-subspace chain.

---

# Hints

> [!note]- Hint 1
> What is the meaning of "upper-triangular" in terms of invariant subspaces? Consider the subspaces $V_k = \operatorname{span}(e_1, \ldots, e_k)$. What does upper-triangularity say about $A V_k$?

> [!note]- Hint 2
> Upper-triangularity of $A$ is equivalent to $A V_k \subseteq V_k$ for each $k = 1, \ldots, n$ (each $V_k$ is *invariant* under $A$). Combine with invertibility to show $A V_k = V_k$ (not just $\subseteq$), then $A^{-1} V_k = V_k$, hence $A^{-1}$ is upper-triangular.

> [!note]- Hint 3
> For the diagonal entries: from $AA^{-1} = I_n$, the $(k, k)$-entry is $\sum_r A_{k, r} (A^{-1})_{r, k} = 1$. Use triangularity of both $A$ and $A^{-1}$ to collapse the sum to a single term $A_{k, k} (A^{-1})_{k, k} = 1$, giving the reciprocal formula.

---

# Solution

The plan: convert triangularity to an invariant-subspace condition $A V_k \subseteq V_k$, use invertibility to upgrade $\subseteq$ to $=$, deduce $A^{-1} V_k = V_k$ and hence $A^{-1}$ is upper-triangular. The diagonal-entry formula then follows by reading off the $(k, k)$-entry of $AA^{-1} = I$.

**Step 1: Upper-triangularity ⟺ chain of invariant subspaces.**

Let $V_k := \operatorname{span}(e_1, \ldots, e_k) \subseteq \mathbf{F}^n$ for $k = 1, \ldots, n$.

Claim: $A$ is upper-triangular iff $A V_k \subseteq V_k$ for every $k$.

> [!note]- Derivation
> ($\Rightarrow$) Suppose $A$ is upper-triangular. The $k$-th column of $A$ is $A_{\cdot, k}$. Since $A_{j, k} = 0$ for $j > k$, the column $A_{\cdot, k}$ has nonzero entries only in positions $1, 2, \ldots, k$. So $A e_k = A_{\cdot, k} \in V_k$. Hence $A V_k = \operatorname{span}(A e_1, \ldots, A e_k) \subseteq V_k$ (each $A e_l$ for $l \leq k$ lies in $V_l \subseteq V_k$).
>
> ($\Leftarrow$) Suppose $A V_k \subseteq V_k$ for every $k$. Then $A e_k \in A V_k \subseteq V_k$, so $A_{\cdot, k}$ has nonzero entries only in positions $1, \ldots, k$. That is, $A_{j, k} = 0$ for $j > k$, which is the upper-triangularity condition.

**Step 2: $A$ invertible plus $A V_k \subseteq V_k$ implies $A V_k = V_k$.**

> [!note]- Derivation
> Restrict $A$ to $V_k$: the map $A|_{V_k} : V_k \to V_k$ (codomain landing in $V_k$ by the invariance hypothesis). $A$ is invertible on the whole of $\mathbf{F}^n$, hence injective; the restriction to $V_k$ is also injective. By [[Thm - Injectivity Equals Surjectivity in Finite Dimensions]] (since $\dim V_k = k$ is finite), an injective operator from $V_k$ to itself is surjective. So $A V_k = V_k$.

**Step 3: $A^{-1} V_k = V_k$, hence $A^{-1}$ is upper-triangular.**

> [!note]- Derivation
> From $A V_k = V_k$ and $A$ invertible, applying $A^{-1}$ to both sides: $V_k = A^{-1}(A V_k) = A^{-1} V_k$. So $A^{-1} V_k = V_k$ (in particular, $A^{-1} V_k \subseteq V_k$).
>
> By the converse direction of Step 1 (with $A$ replaced by $A^{-1}$): $A^{-1} V_k \subseteq V_k$ for every $k$ means $A^{-1}$ is upper-triangular.

**Step 4: Diagonal entries are reciprocals.**

> [!note]- Derivation
> From $AA^{-1} = I_n$, the $(k, k)$-entry is
> $$\sum_{r=1}^n A_{k, r} \, (A^{-1})_{r, k} \;=\; (I_n)_{k, k} \;=\; 1.$$
> Since $A$ is upper-triangular, $A_{k, r} = 0$ for $r < k$. Since $A^{-1}$ is upper-triangular, $(A^{-1})_{r, k} = 0$ for $r > k$. So the only term that survives is $r = k$:
> $$A_{k, k} \, (A^{-1})_{k, k} \;=\; 1.$$
> Hence $A_{k, k} \neq 0$ (already known, since the diagonal entries of an invertible upper-triangular matrix are non-zero, equivalent to $\det A \neq 0$ being the product of the diagonal), and $(A^{-1})_{k, k} = (A_{k, k})^{-1}$.

> [!note]- Complete formal solution
> Let $A \in \mathbf{F}^{n, n}$ be upper-triangular and invertible, and let $V_k := \operatorname{span}(e_1, \ldots, e_k)$.
>
> **Step 1: $A$ is upper-triangular iff $A V_k \subseteq V_k$ for all $k$.** Upper-triangularity says $A_{j, k} = 0$ for $j > k$, equivalently $A e_k \in V_k$ for each $k$, equivalently $A V_k \subseteq V_k$ for each $k$ (since $V_k = \operatorname{span}(e_1, \ldots, e_k)$ and $A V_l \subseteq V_l \subseteq V_k$ for $l \leq k$).
>
> **Step 2: $A V_k = V_k$.** $A|_{V_k} : V_k \to V_k$ is injective (since $A$ is invertible). By [[Thm - Injectivity Equals Surjectivity in Finite Dimensions]] with $\dim V_k = k$, $A|_{V_k}$ is bijective, so $A V_k = V_k$.
>
> **Step 3: $A^{-1} V_k = V_k$.** Applying $A^{-1}$ to $A V_k = V_k$: $V_k = A^{-1}(V_k)$, so $A^{-1} V_k = V_k$.
>
> **Step 4: $A^{-1}$ is upper-triangular.** By the converse in Step 1 applied to $A^{-1}$: $A^{-1} V_k \subseteq V_k$ for all $k$ implies $A^{-1}$ is upper-triangular.
>
> **Step 5: $(A^{-1})_{k, k} = (A_{k, k})^{-1}$.** The $(k, k)$-entry of $AA^{-1} = I_n$ is $\sum_r A_{k, r} (A^{-1})_{r, k} = 1$. Triangularity of $A$ ($A_{k, r} = 0$ for $r < k$) and of $A^{-1}$ ($(A^{-1})_{r, k} = 0$ for $r > k$) reduce the sum to the single term $r = k$: $A_{k, k} (A^{-1})_{k, k} = 1$. Hence $(A^{-1})_{k, k} = (A_{k, k})^{-1}$. $\blacksquare$

> [!note]- Sanity check on a $2$-by-$2$ example
> $A = \begin{pmatrix} 2 & 5 \\ 0 & 3 \end{pmatrix}$. Direct computation: $A^{-1} = \frac{1}{6} \begin{pmatrix} 3 & -5 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1/2 & -5/6 \\ 0 & 1/3 \end{pmatrix}$, upper-triangular with diagonal entries $1/2 = 1/A_{1,1}$ and $1/3 = 1/A_{2,2}$.

---

# Key Takeaways

**Triangular matrices have an invariant-subspace interpretation.** "Upper-triangular" is a basis-dependent matrix property, but it has the basis-free meaning "the standard subspace chain $V_1 \subseteq V_2 \subseteq \cdots \subseteq V_n = \mathbf{F}^n$ is invariant". This translation — from a *matrix shape* to an *invariant-subspace condition* — is the reusable principle. The trigger is any property of matrices defined by zeros in specific positions; translate to invariant subspaces and the structural content becomes visible. The strategy generalises: "block upper-triangular" corresponds to invariant flags of higher-rank subspaces, "block-diagonal" corresponds to invariant decomposition $V = V_1 \oplus \cdots \oplus V_k$, and so on.

**Invertibility transfers structural properties through inversion.** When a matrix has a structural property (preserves a chain of subspaces, preserves an inner product, has some block structure), invertibility plus rank-rigidity often forces the inverse to have the *same* structural property. The mechanism is: the structural property gives an inclusion or containment; invertibility upgrades it to equality (by [[Thm - Injectivity Equals Surjectivity in Finite Dimensions]] or rank–nullity). The reusable principle: a structural property + invertibility ⟹ same property holds for the inverse. The trigger: "I have a structured invertible matrix; what is the structure of its inverse?". The same logic works for orthogonal matrices (inverse is orthogonal), unitary matrices, permutation matrices, etc.

**Reading off matrix entries from products gives algebraic identities.** When a matrix identity like $AA^{-1} = I$ holds, examining specific entries gives algebraic relations between entries. Here the $(k, k)$-entry of $AA^{-1} = I_n$, combined with the triangularity of both $A$ and $A^{-1}$, forces the sum to collapse to a single term. The reusable principle: when matrix identities meet sparsity patterns (triangular, banded, sparse), most of the sum vanishes and a single equation remains. This is the basis of much of computational linear algebra — Gauss elimination, $LU$ decomposition, Cholesky — where exploiting triangular structure reduces an $n^3$ operation to an $n^2$ one. The trigger is any matrix identity for matrices with specific sparsity patterns.

---
