---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Linear Map"
  - "Def - Matrix of a Linear Map"
  - "Def - Dimension"
  - "Thm - Linear Map Determined by Action on Basis"
  - "Thm - Two Vector Spaces Isomorphic iff Same Dimension"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ and $W$ be finite-dimensional vector spaces over $\mathbf{F}$ with $\dim V = n$ and $\dim W = m$. Prove that
$$\dim \mathcal{L}(V, W) \;=\; (\dim V)(\dim W) \;=\; m n.$$
Exhibit an explicit isomorphism $\mathcal{L}(V, W) \cong \mathbf{F}^{m, n}$.

**Recall:**

![[Def - Linear Map#The Definition]]

The vector space $\mathcal{L}(V, W)$ has pointwise operations, with the zero map as the additive identity.

![[Def - Matrix of a Linear Map#The Definition]]

The matrix isomorphism $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$ (with bases fixed) is what this exercise constructs and proves to be an isomorphism. The dimension of $\mathbf{F}^{m, n}$ is $mn$ (basis: matrix units $E_{j, k}$ with a single $1$).

The [[Thm - Two Vector Spaces Isomorphic iff Same Dimension|dimension equality of isomorphic spaces]] then gives $\dim \mathcal{L}(V, W) = mn$.

---

# Convergent Strategy

**Problem class.** This is a *compute the dimension of a constructed space* problem. The topic-page Problem-Solving Strategy classifies it under "structural facts about $\mathcal{L}(V, W)$": exploit the matrix isomorphism to translate $\mathcal{L}(V, W)$ into a concrete matrix space, count dimensions there.

**Assumption pattern.** $V$ and $W$ are finite-dimensional. Bases of each must be chosen to enable the matrix representation. Once bases are chosen, every linear map has a unique matrix, and every matrix specifies a unique linear map (by the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]]).

**Theorem routing.** The route is: choose bases of $V$ and $W$ $\Rightarrow$ define the matrix map $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$ $\Rightarrow$ show $\mathcal{M}$ is linear, injective, and surjective $\Rightarrow$ conclude $\mathcal{M}$ is an isomorphism $\Rightarrow$ apply [[Thm - Two Vector Spaces Isomorphic iff Same Dimension|the dimension equality]] to get $\dim \mathcal{L}(V, W) = \dim \mathbf{F}^{m, n} = mn$.

**Key decision point.** The crucial recognition is that the *natural* map $\mathcal{M}$ is itself a linear isomorphism. The "key decision" is to verify each of the three properties (linear, injective, surjective) cleanly, using the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] for surjectivity. An alternative approach would compute the dimension directly by exhibiting a basis of $\mathcal{L}(V, W)$ of size $mn$, but the matrix-isomorphism approach is cleaner.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra III — §3A–D Linear Maps#Legal Operations|the topic page's Legal Operations]]:

1. **Pass between a linear map and its matrix** (operation 6). The entire proof runs through the matrix isomorphism.

2. **Identify a vector space up to isomorphism by counting dimensions** (operation 5). Once $\mathcal{L}(V, W) \cong \mathbf{F}^{m, n}$, dimensions are equal, and the dimension of $\mathbf{F}^{m, n}$ is $mn$.

3. **Specify a linear map by its action on a basis** (operation 1). Used in the surjectivity step: given a matrix $A$, construct the corresponding linear map by specifying its action on a basis of $V$ via the columns of $A$.

---

# Hints

> [!note]- Hint 1
> What is the natural map $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$, with bases of $V$ and $W$ fixed? Show this is linear.

> [!note]- Hint 2
> Show $\mathcal{M}$ is injective: if $\mathcal{M}(T) = 0$ (the zero matrix), what does that say about $T$ on the basis vectors of $V$?

> [!note]- Hint 3
> Show $\mathcal{M}$ is surjective: given any matrix $A \in \mathbf{F}^{m, n}$, use the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] to construct a linear map whose matrix is $A$.

> [!note]- Hint 4
> Once $\mathcal{M}$ is shown to be an isomorphism, dimensions agree: $\dim \mathcal{L}(V, W) = \dim \mathbf{F}^{m, n} = mn$. (For the dimension of $\mathbf{F}^{m, n}$, note that the "matrix units" $E_{j, k}$ — matrices with a single $1$ in position $(j, k)$ and zeros elsewhere — form a basis.)

---

# Solution

The plan has three steps. Choose bases of $V$ and $W$, defining the matrix map $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$. Show $\mathcal{M}$ is linear (immediate from definitions), injective (uses that a linear map vanishing on a basis is zero), and surjective (uses the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] to lift matrices to linear maps). Conclude via the [[Thm - Two Vector Spaces Isomorphic iff Same Dimension|dimension equality]] that $\dim \mathcal{L}(V, W) = mn$.

**Step 1: Define the matrix map.**

Choose ordered bases $v_1, \ldots, v_n$ of $V$ and $w_1, \ldots, w_m$ of $W$. For $T \in \mathcal{L}(V, W)$, define $\mathcal{M}(T) \in \mathbf{F}^{m, n}$ via [[Def - Matrix of a Linear Map|the matrix-of-a-linear-map construction]]: column $k$ of $\mathcal{M}(T)$ lists the $w$-coordinates of $T v_k$.

> [!note]- Derivation
> The map $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$ is well-defined: every $T \in \mathcal{L}(V, W)$ has a well-defined matrix in any pair of bases, because each $Tv_k$ has a unique expression in the $w$-basis as $\sum_j A_{j, k} w_j$, and these scalars $A_{j, k}$ are the entries of $\mathcal{M}(T)$.

**Step 2: $\mathcal{M}$ is linear.**

The maps $\mathcal{M}(S + T) = \mathcal{M}(S) + \mathcal{M}(T)$ and $\mathcal{M}(\lambda T) = \lambda \mathcal{M}(T)$, by computing both sides entry-by-entry.

> [!note]- Derivation
> For additivity: the $(j, k)$-entry of $\mathcal{M}(S + T)$ is the $w_j$-coefficient in $(S + T)(v_k) = S v_k + T v_k = \sum_j \mathcal{M}(S)_{j, k} w_j + \sum_j \mathcal{M}(T)_{j, k} w_j = \sum_j (\mathcal{M}(S)_{j, k} + \mathcal{M}(T)_{j, k}) w_j$. So $\mathcal{M}(S + T)_{j, k} = \mathcal{M}(S)_{j, k} + \mathcal{M}(T)_{j, k} = (\mathcal{M}(S) + \mathcal{M}(T))_{j, k}$.
>
> For homogeneity: the $(j, k)$-entry of $\mathcal{M}(\lambda T)$ is the $w_j$-coefficient in $(\lambda T)(v_k) = \lambda T v_k = \lambda \sum_j \mathcal{M}(T)_{j, k} w_j$. So $\mathcal{M}(\lambda T)_{j, k} = \lambda \mathcal{M}(T)_{j, k} = (\lambda \mathcal{M}(T))_{j, k}$.

**Step 3: $\mathcal{M}$ is injective.**

If $\mathcal{M}(T) = 0$ (the zero matrix), then $T v_k = 0$ for every basis vector $v_k$. By linearity and the fact that $v_1, \ldots, v_n$ is a basis, $T = 0$.

> [!note]- Derivation
> If $\mathcal{M}(T) = 0$, then for each $k$, $T v_k = \sum_j 0 \cdot w_j = 0$. By [[Ex - Linear maps preserve linear combinations|linearity preserved on linear combinations]], for any $v = \sum_k c_k v_k \in V$,
> $$T v = T\!\sum_k c_k v_k = \sum_k c_k T v_k = \sum_k c_k \cdot 0 = 0.$$
> So $T = 0$. Hence $\operatorname{null} \mathcal{M} = \{0\}$, i.e., $\mathcal{M}$ is injective.

**Step 4: $\mathcal{M}$ is surjective.**

Given any matrix $A \in \mathbf{F}^{m, n}$, the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] constructs a linear map $T$ with $T v_k$ specified to be the vector with column-$k$ coordinates equal to $A_{\cdot, k}$ in the $w$-basis. Then $\mathcal{M}(T) = A$.

> [!note]- Derivation
> Let $A \in \mathbf{F}^{m, n}$ be arbitrary. For each $k = 1, \ldots, n$, define $u_k := \sum_{j=1}^m A_{j, k} w_j \in W$. By the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]], there exists a unique linear map $T : V \to W$ with $T v_k = u_k$ for each $k$.
>
> The matrix of $T$ in the chosen bases is $\mathcal{M}(T)$, with column $k$ equal to the coordinate column of $T v_k = u_k = \sum_j A_{j, k} w_j$ — that is, $\mathcal{M}(T)_{j, k} = A_{j, k}$ for all $j, k$. So $\mathcal{M}(T) = A$.
>
> Hence every $A \in \mathbf{F}^{m, n}$ is in the range of $\mathcal{M}$, i.e., $\mathcal{M}$ is surjective.

**Step 5: $\mathcal{M}$ is an isomorphism, and $\dim \mathcal{L}(V, W) = mn$.**

Combining Steps 2, 3, and 4, $\mathcal{M}$ is a linear bijection, hence an isomorphism (by [[Def - Invertibility and Isomorphism]], since the set-theoretic inverse of a linear bijection is automatically linear). By the [[Thm - Two Vector Spaces Isomorphic iff Same Dimension|dimension equality of isomorphic spaces]],
$$\dim \mathcal{L}(V, W) = \dim \mathbf{F}^{m, n}.$$
The space $\mathbf{F}^{m, n}$ has the **matrix units** $E_{j, k}$ as a basis: $E_{j, k}$ is the matrix with a $1$ in position $(j, k)$ and zeros elsewhere. There are $m \cdot n$ such units, and they are linearly independent (a linear combination $\sum c_{j, k} E_{j, k} = 0$ has all entries zero, i.e., all $c_{j, k} = 0$) and spanning (every matrix is uniquely $\sum_{j, k} A_{j, k} E_{j, k}$). So $\dim \mathbf{F}^{m, n} = mn$, hence $\dim \mathcal{L}(V, W) = mn$.

> [!note]- Complete formal solution
> Let $V$ and $W$ be finite-dimensional vector spaces over $\mathbf{F}$ with $\dim V = n$, $\dim W = m$. Choose bases $v_1, \ldots, v_n$ of $V$ and $w_1, \ldots, w_m$ of $W$.
>
> **The matrix map.** Define $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$ by sending each linear map $T$ to its matrix $\mathcal{M}(T)$ in these bases: column $k$ of $\mathcal{M}(T)$ is the coordinate column of $T v_k$ in the $w$-basis.
>
> **Linearity.** Entry-by-entry, $\mathcal{M}(S + T)_{j, k} = \mathcal{M}(S)_{j, k} + \mathcal{M}(T)_{j, k}$ and $\mathcal{M}(\lambda T)_{j, k} = \lambda \mathcal{M}(T)_{j, k}$, by computing the $w_j$-coefficient of $(S + T) v_k$ and $(\lambda T) v_k$ respectively.
>
> **Injectivity.** If $\mathcal{M}(T) = 0$, then $T v_k = 0$ for every $k$, hence $T = 0$ on $\operatorname{span}(v_1, \ldots, v_n) = V$.
>
> **Surjectivity.** Given $A \in \mathbf{F}^{m, n}$, define $u_k := \sum_{j=1}^m A_{j, k} w_j$ for each $k$. By the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]], there is a unique linear $T : V \to W$ with $T v_k = u_k$. Then $\mathcal{M}(T) = A$.
>
> So $\mathcal{M}$ is a linear isomorphism. By [[Thm - Two Vector Spaces Isomorphic iff Same Dimension|the dimension equality]], $\dim \mathcal{L}(V, W) = \dim \mathbf{F}^{m, n} = mn$. The last equality follows from the matrix-unit basis $\{E_{j, k} : 1 \leq j \leq m, 1 \leq k \leq n\}$ of $\mathbf{F}^{m, n}$, which has size $mn$. $\blacksquare$

> [!note]- Sanity check via direct basis construction
> An alternative verification: exhibit a basis of $\mathcal{L}(V, W)$ of size $mn$ directly. For each $(j, k)$ with $1 \leq j \leq m$, $1 \leq k \leq n$, define $T_{j, k} \in \mathcal{L}(V, W)$ by
> $$T_{j, k}(v_l) := \begin{cases} w_j & \text{if } l = k \\ 0 & \text{if } l \neq k. \end{cases}$$
> By the linear-map lemma, this is well-defined. The collection $\{T_{j, k}\}$ has size $mn$. Under the matrix map, $\mathcal{M}(T_{j, k}) = E_{j, k}$ — the matrix unit. So the $T_{j, k}$ map bijectively to the matrix-unit basis of $\mathbf{F}^{m, n}$, and they form a basis of $\mathcal{L}(V, W)$. This gives $\dim \mathcal{L}(V, W) = mn$ directly, confirming the result.

---

# Key Takeaways

**The matrix isomorphism is the bridge between linear maps and matrices.** Once bases are chosen, every linear map $V \to W$ is represented by a unique matrix, and every matrix represents a unique linear map. The isomorphism $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$ is the central computational device of linear algebra: abstract problems become concrete matrix problems. The reusable principle is to exploit the matrix isomorphism whenever the structure of $\mathcal{L}(V, W)$ is in question. The trigger is "I am working with linear maps and want to compute something about them" — pass to matrices via $\mathcal{M}$. The dimension formula $\dim \mathcal{L}(V, W) = mn$ is the simplest consequence.

**Counting dimensions via matrix units.** The space $\mathbf{F}^{m, n}$ has dimension $mn$ because the matrix units $E_{j, k}$ — single-$1$ matrices — form an obvious basis. By the matrix isomorphism, $\mathcal{L}(V, W)$ has the corresponding basis $T_{j, k}$ — linear maps that send the $k$-th basis vector to the $j$-th basis vector of $W$ and all other basis vectors to zero. The reusable principle is to use *natural* bases adapted to the structure of the space, and to read off dimensions by counting basis elements. The trigger is "compute the dimension of a space" — exhibit a basis or transport to a space whose basis you already know.

**The size of $\mathcal{L}(V, W)$ grows like the product of dimensions.** This is the algebraic shadow of "a linear map is finite data: $n$ vectors in $W$, each of dimension $m$, so $mn$ scalars total". The reusable principle: when both source and target are finite-dimensional, the space of linear maps between them is also finite-dimensional, with dimension equal to the product. The result extends to the space of $k$-linear forms ($V_1 \times \cdots \times V_k \to W$ multilinear), the space of bilinear forms, the space of tensors of various ranks — all of these have dimensions that are products of the relevant dimensions, with the linear-maps case being the simplest. See [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]] for the multilinear generalisation.

---
