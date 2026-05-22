---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Multilinear Form"
  - "Def - Alternating Multilinear Form"
  - "Def - Dual Space"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a finite-dimensional vector space over $\mathbb{F}$, with dual space $V^*$. For $\varphi_1, \dots, \varphi_m \in V^*$, define the **wedge product** $\varphi_1 \wedge \varphi_2 \wedge \cdots \wedge \varphi_m : V^m \to \mathbb{F}$ by

$$(\varphi_1 \wedge \cdots \wedge \varphi_m)(v_1, \dots, v_m) := \det \big[ \varphi_i(v_j) \big]_{1 \leq i, j \leq m},$$

where $[\varphi_i(v_j)]$ is the $m \times m$ matrix with $(i, j)$-entry $\varphi_i(v_j)$.

(a) Show that $\varphi_1 \wedge \cdots \wedge \varphi_m$ is an [[Def - Alternating Multilinear Form|alternating $m$-linear form]] on $V$.

(b) Show that swapping any two of the dual vectors $\varphi_i, \varphi_j$ (with $i \neq j$) multiplies the wedge product by $-1$: $\varphi_1 \wedge \cdots \wedge \varphi_j \wedge \cdots \wedge \varphi_i \wedge \cdots \wedge \varphi_m = -(\varphi_1 \wedge \cdots \wedge \varphi_i \wedge \cdots \wedge \varphi_j \wedge \cdots \wedge \varphi_m)$.

(c) For a basis $(e_1, \dots, e_n)$ of $V$ with dual basis $(e^*_1, \dots, e^*_n)$, show that the wedge products $\{e^*_{i_1} \wedge e^*_{i_2} \wedge \cdots \wedge e^*_{i_m} : 1 \leq i_1 < i_2 < \cdots < i_m \leq n\}$ form a basis of $V^{(m)}_{\mathrm{alt}}$ for $1 \leq m \leq n$.

**Recall:**

![[Def - Multilinear Form#The Definition]]

![[Def - Alternating Multilinear Form#The Definition]]

The **dual space** $V^* = \mathcal{L}(V, \mathbb{F})$ consists of linear functionals on $V$. For a basis $(e_1, \dots, e_n)$ of $V$, the **dual basis** $(e^*_1, \dots, e^*_n)$ is defined by $e^*_i(e_j) = \delta_{ij}$.

The determinant is alternating multilinear in its columns (and equivalently in its rows) — by the [[Def - Determinant|definition of determinant]] as the unique alternating $n$-linear form with $\det(I) = 1$.

---

# Convergent Strategy

**Problem class.** This is a *construction* exercise: build an explicit alternating multilinear form (the wedge product) and verify its key properties, including being a basis for the space of alternating forms. This is the foundational exercise that connects abstract alternating multilinear theory to concrete computation via determinants. As the [[Linear Algebra IX — §9 Multilinear Algebra and Determinants#Problem-Solving Strategy|topic page strategy]] indicates, "identify an alternating multilinear form as a determinant" is one of the central techniques.

**Assumption pattern.** We have linear functionals $\varphi_i \in V^*$ and want to combine them into an alternating multilinear form on $V$. The defining formula is the determinant of the matrix $[\varphi_i(v_j)]$ — the determinant inherits multilinearity and alternation from its definition.

**Theorem routing.** For (a), use the multilinearity and alternation of $\det$ in its columns. For (b), swapping $\varphi_i$ and $\varphi_j$ swaps the $i$-th and $j$-th rows of the matrix $[\varphi_i(v_j)]$, which multiplies $\det$ by $-1$. For (c), use the dimension count $\binom{n}{m} = \#\{(i_1 < \cdots < i_m)\}$ and linear independence via evaluation on tuples of basis vectors.

**Key decision point.** The non-obvious move in (c) is the linear-independence argument: how do you distinguish the wedge products $e^*_{i_1} \wedge \cdots \wedge e^*_{i_m}$? Evaluate them on tuples of basis vectors $(e_{j_1}, \dots, e_{j_m})$ with $j_1 < \cdots < j_m$; the wedge product gives $1$ if $(i_1, \dots, i_m) = (j_1, \dots, j_m)$ and $0$ otherwise (because the matrix becomes the identity or has a zero column).

---

# Legal Operations Used

1. **Identify an alternating $n$-linear form by checking values on a basis** (operation 5 from the topic page). For (c), we identify two alternating forms as equal by checking them on basis tuples.

2. **Use the abstract definition of $\det$ as an alternating multilinear form** (in spirit, from the determinant definition). The wedge product inherits its alternating-multilinear properties from $\det$.

3. **Compute alternating forms on linearly dependent tuples (vanishing)** — the inherited alternation of $\det$.

---

# Hints

> [!note]- Hint 1
> For (a), linearity of $\varphi_1 \wedge \cdots \wedge \varphi_m$ in each slot $v_j$ follows from linearity of $\det$ in column $j$ (and the linearity of $\varphi_i(v_j)$ in $v_j$, which makes column $j$ of the matrix depend linearly on $v_j$).

> [!note]- Hint 2
> For (a), alternation: if $v_j = v_k$ for $j \neq k$, then columns $j$ and $k$ of the matrix $[\varphi_i(v_j)]$ are equal, so $\det = 0$ (alternating property of $\det$ in columns).

> [!note]- Hint 3
> For (b), swapping $\varphi_i, \varphi_j$ swaps rows $i$ and $j$ of the matrix; $\det$ flips sign under row swap.

> [!note]- Hint 4
> For (c), to show the wedges are linearly independent, evaluate $\sum c_{i_1, \dots, i_m} (e^*_{i_1} \wedge \cdots \wedge e^*_{i_m})$ on a specific tuple $(e_{j_1}, \dots, e_{j_m})$ with $j_1 < \cdots < j_m$. Only one term — the one with $(i_1, \dots, i_m) = (j_1, \dots, j_m)$ — gives a nonzero value (which is 1), the rest give zero. Read off $c_{j_1, \dots, j_m} = 0$ for all sorted tuples.

> [!note]- Hint 5
> For the spanning part of (c), use the dimension count: $\dim V^{(m)}_{\mathrm{alt}} = \binom{n}{m}$ (from [[Def - Alternating Multilinear Form]]), and there are exactly $\binom{n}{m}$ sorted tuples. So the $\binom{n}{m}$ linearly independent wedge products form a basis.

---

# Solution

The plan is to verify in turn (a) multilinearity and alternation of the wedge product, (b) antisymmetry in the dual-vector arguments, and (c) that the sorted-index wedge products form a basis of $V^{(m)}_{\mathrm{alt}}$, by combining linear independence with the dimension count.

**Step 1: Multilinearity and alternation in the vector arguments (part a).**

The wedge product is alternating $m$-linear in $(v_1, \dots, v_m)$ because $\det$ is alternating $m$-linear in the columns of the matrix $[\varphi_i(v_j)]$.

> [!note]- Derivation
> **Multilinearity.** Fix $(v_1, \dots, v_{j-1}, v_{j+1}, \dots, v_m)$ and vary $v_j$. The $j$-th column of the matrix $[\varphi_i(v_j)]$ is $(\varphi_1(v_j), \dots, \varphi_m(v_j))^t$, which is linear in $v_j$ (because each $\varphi_i$ is linear). Now $\det$ is multilinear in its columns: scaling or adding to the $j$-th column scales or adds correspondingly to $\det$. So
> $$(\varphi_1 \wedge \cdots \wedge \varphi_m)(v_1, \dots, \alpha v_j + \beta v_j', \dots, v_m) = \alpha (\varphi_1 \wedge \cdots)(\dots, v_j, \dots) + \beta (\varphi_1 \wedge \cdots)(\dots, v_j', \dots).$$
> This holds in each of the $m$ slots, so the wedge product is multilinear.
>
> **Alternation.** Suppose $v_j = v_k$ for some $j \neq k$. Then columns $j$ and $k$ of the matrix $[\varphi_i(v_j)]_{i=1, \dots, m; j=1, \dots, m}$ are equal (both equal to $(\varphi_1(v_j), \dots, \varphi_m(v_j))^t$). The determinant of a matrix with two equal columns is zero (by the alternating property of $\det$). So $(\varphi_1 \wedge \cdots \wedge \varphi_m)(v_1, \dots, v_m) = 0$ when the tuple has a repeated entry. Hence the wedge product is alternating.

**Step 2: Antisymmetry in the dual-vector arguments (part b).**

Swapping $\varphi_i$ and $\varphi_j$ swaps rows $i$ and $j$ of $[\varphi_i(v_j)]$, multiplying $\det$ by $-1$.

> [!note]- Derivation
> The matrix $M = [\varphi_i(v_j)]_{i, j = 1}^m$ has $\varphi_i$ in the $i$-th row position. Swapping $\varphi_i$ and $\varphi_j$ in the wedge product list (positions $i$ and $j$) corresponds to swapping rows $i$ and $j$ of $M$. The determinant of a matrix flips sign under a row swap (the alternating property of $\det$ in rows, equivalent to alternation in columns since $\det A = \det A^t$).
>
> So $\varphi_1 \wedge \cdots \wedge \varphi_j \wedge \cdots \wedge \varphi_i \wedge \cdots \wedge \varphi_m = \det(\text{row-swapped } M) = -\det M = -(\varphi_1 \wedge \cdots \wedge \varphi_i \wedge \cdots \wedge \varphi_j \wedge \cdots \wedge \varphi_m)$.

**Step 3: Sorted-index wedge products form a basis of $V^{(m)}_{\mathrm{alt}}$ (part c).**

The $\binom{n}{m}$ products $e^*_{i_1} \wedge \cdots \wedge e^*_{i_m}$ (with $i_1 < \cdots < i_m$) are linearly independent and span; together with the dimension count, they form a basis.

> [!note]- Derivation
> Step 3a: Compute $(e^*_{i_1} \wedge \cdots \wedge e^*_{i_m})(e_{j_1}, \dots, e_{j_m})$ for sorted index tuples $(i_1 < \cdots < i_m)$ and $(j_1 < \cdots < j_m)$.
>
> The matrix is $[e^*_{i_a}(e_{j_b})]_{a, b} = [\delta_{i_a, j_b}]_{a, b}$.
>
> - If $(i_1, \dots, i_m) = (j_1, \dots, j_m)$: the matrix is the $m \times m$ identity, $\det = 1$.
> - If $(i_1, \dots, i_m) \neq (j_1, \dots, j_m)$ (both sorted): there is some $a$ with $i_a \neq j_a$; say $i_1 \neq j_1$ (the smallest disagreement). Then either $i_1 < j_1$ or $i_1 > j_1$. In either case, $i_1 \notin \{j_1, \dots, j_m\}$ (by the sortedness and the smallest-disagreement assumption), so row $a = 1$ of the matrix is all zero: $\delta_{i_1, j_b} = 0$ for all $b$. So $\det = 0$.
>
> Conclusion: $(e^*_{i_1} \wedge \cdots \wedge e^*_{i_m})(e_{j_1}, \dots, e_{j_m}) = \delta_{(i_1, \dots, i_m), (j_1, \dots, j_m)}$ (Kronecker delta on sorted tuples).
>
> Step 3b: Linear independence. Suppose $\sum_{i_1 < \cdots < i_m} c_{i_1, \dots, i_m} (e^*_{i_1} \wedge \cdots \wedge e^*_{i_m}) = 0$. Evaluate at $(e_{j_1}, \dots, e_{j_m})$ for any sorted $(j_1, \dots, j_m)$. By the Kronecker delta computation, only the term with $(i_1, \dots, i_m) = (j_1, \dots, j_m)$ contributes, giving $c_{j_1, \dots, j_m} = 0$. So all coefficients vanish.
>
> Step 3c: Spanning. The number of sorted tuples is $\binom{n}{m}$. By [[Def - Alternating Multilinear Form|the dimension theorem]], $\dim V^{(m)}_{\mathrm{alt}} = \binom{n}{m}$. So the $\binom{n}{m}$ linearly independent wedges span all of $V^{(m)}_{\mathrm{alt}}$.
>
> Hence $\{e^*_{i_1} \wedge \cdots \wedge e^*_{i_m} : i_1 < \cdots < i_m\}$ is a basis of $V^{(m)}_{\mathrm{alt}}$.

> [!note]- Complete formal solution
> **(a) Alternating multilinearity in vector arguments.** For each slot $j$, the wedge product is linear in $v_j$ because the determinant is linear in column $j$ (with column $j$ being $(\varphi_1(v_j), \dots, \varphi_m(v_j))^t$, linear in $v_j$ by linearity of each $\varphi_i$). For alternation: if $v_j = v_k$ for $j \neq k$, columns $j, k$ of $[\varphi_i(v_l)]$ are equal, so $\det = 0$.
>
> **(b) Antisymmetry in dual-vector arguments.** Swapping $\varphi_i, \varphi_j$ swaps rows $i, j$ of the matrix, which multiplies $\det$ by $-1$.
>
> **(c) Sorted wedges form a basis.** Compute $(e^*_{i_1} \wedge \cdots \wedge e^*_{i_m})(e_{j_1}, \dots, e_{j_m}) = \det[\delta_{i_a, j_b}]$, which equals 1 if $(i_*) = (j_*)$ (identity matrix) and 0 otherwise (row of zeros). This Kronecker structure gives linear independence: evaluating at $(e_{j_1}, \dots, e_{j_m})$ picks out exactly one coefficient. Combined with $\#$ sorted tuples $= \binom{n}{m} = \dim V^{(m)}_{\mathrm{alt}}$, the wedge products form a basis. $\blacksquare$

---

# Key Takeaways

**The wedge product is the canonical alternating-multilinear construction from linear functionals.** Given any $m$ linear functionals $\varphi_1, \dots, \varphi_m \in V^*$, the wedge product packages them into a single alternating $m$-linear form. This construction is universal: every alternating multilinear form can be written as a linear combination of wedge products (by part (c)), and the wedge product algebra $\Lambda^* V^*$ — graded by degree, with multiplication being the obvious extension of the wedge construction — is the **exterior algebra** of $V^*$. The trigger to recognise this in practice: whenever you encounter "antisymmetric tensor" or "differential form" or "Plücker coordinate", you are working in the exterior algebra, and the wedge product is the natural multiplication. Throughout differential geometry, the wedge product of differential forms is exactly this construction extended to sections of cotangent bundles.

**Linear independence via "evaluation on a basis" is the universal technique for alternating multilinear forms.** Part (c) demonstrates the master pattern: to show wedge products are linearly independent, evaluate them on tuples of basis vectors $(e_{j_1}, \dots, e_{j_m})$ with $j_1 < \cdots < j_m$, and the wedge $e^*_{i_1} \wedge \cdots \wedge e^*_{i_m}$ gives a clean Kronecker-delta response (1 on the matching sorted tuple, 0 otherwise). This is the alternating-multilinear analogue of "linear functionals are determined by their values on a basis", and it works because alternating multilinear forms in $m$ arguments on an $n$-dimensional space are determined by their values on the $\binom{n}{m}$ sorted basis tuples (the other tuples give either zero or a sign-related repetition). The same pattern works in differential geometry: to verify a differential-form identity, evaluate on tuples of coordinate vector fields $(\partial_{i_1}, \dots, \partial_{i_m})$.

**The exterior algebra structure $\Lambda^* V^* = \bigoplus_m \Lambda^m V^*$ has dimensions $\binom{n}{0}, \binom{n}{1}, \dots, \binom{n}{n}$ summing to $2^n$.** This is the structural fact behind the **Hodge star** $\star : \Lambda^m V^* \to \Lambda^{n-m} V^*$, the **Poincaré duality** in topology (relating $\Lambda^m$ and $\Lambda^{n-m}$ via the top form), and many other deep dualities. The peak dimension is at $m = n/2$ (where the binomial coefficient is largest), and the **top form** $\Lambda^n V^*$ has dimension 1 — this one-dimensionality is precisely the structural fact that makes [[Def - Determinant|the determinant]] well-defined. So the wedge-product framework unifies the determinant, the volume form, and the entire exterior calculus into a single algebraic structure indexed by degree $m$, with the determinant living at the top ($m = n$).
