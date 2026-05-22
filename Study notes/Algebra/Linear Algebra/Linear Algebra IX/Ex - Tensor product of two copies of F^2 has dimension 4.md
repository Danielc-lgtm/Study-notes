---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Tensor Product of Vector Spaces"
  - "Thm - Universal Property of the Tensor Product"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V = W = \mathbb{F}^2$ with standard basis $(e_1, e_2)$.

(a) Compute $\dim(V \otimes W)$ and exhibit a basis explicitly.

(b) Show that $V \otimes V \cong M_2(\mathbb{F})$, the space of $2 \times 2$ matrices, via the canonical map $u \otimes v \mapsto u v^t$.

(c) Find $u, v \in \mathbb{F}^2$ such that $u \otimes v = e_1 \otimes e_1 + e_2 \otimes e_2$, or prove no such $u, v$ exist.

**Recall:**

![[Def - Tensor Product of Vector Spaces#The Definition]]

The dimension formula: $\dim(V \otimes W) = \dim V \cdot \dim W$.

![[Thm - Universal Property of the Tensor Product#Statement]]

If $(e_i)$ is a basis of $V$ and $(f_j)$ is a basis of $W$, then $\{e_i \otimes f_j\}$ is a basis of $V \otimes W$.

An **elementary tensor** is an element of $V \otimes W$ of the form $v \otimes w$ for $v \in V, w \in W$. Elementary tensors span $V \otimes W$ but do not exhaust it: most elements are sums of elementary tensors.

---

# Convergent Strategy

**Problem class.** This is a *concrete computation* in the tensor product that exposes the abstract definition. Part (a) verifies the dimension formula; part (b) gives an explicit isomorphism between an abstract tensor product and a concrete space; part (c) probes whether elementary tensors exhaust the tensor product. This is the foundational hands-on exercise establishing the geometry of $V \otimes V$.

**Assumption pattern.** $V = W = \mathbb{F}^2$, a 2-dimensional space with a specific basis. The dimension count is $\dim V \cdot \dim W = 4$; the isomorphism $V \otimes V \cong M_2$ comes from the "outer product" bilinear map. The non-elementary tensor in (c) requires recognising when a tensor *isn't* a single $u \otimes v$.

**Theorem routing.** For (a), use the dimension formula and basis result from [[Def - Tensor Product of Vector Spaces|the tensor product definition]]. For (b), invoke the [[Thm - Universal Property of the Tensor Product|universal property]]: the outer product $(u, v) \mapsto u v^t$ is bilinear, so it extends uniquely to a linear map $V \otimes V \to M_2$; show it is an isomorphism by dimension count plus injectivity. For (c), use the matrix correspondence from (b): $u \otimes v$ corresponds to the rank-one matrix $u v^t$, while $e_1 \otimes e_1 + e_2 \otimes e_2$ corresponds to the identity matrix $I_2$, which has rank 2.

**Key decision point.** The non-obvious move in (c) is the rank argument: elementary tensors are precisely the rank-one matrices, and the identity matrix has rank 2, so it cannot be an elementary tensor. This shows that **most** elements of $V \otimes V$ are *not* elementary — they require sums of multiple elementary tensors to express.

---

# Legal Operations Used

1. **Use the universal property to construct a linear map out of $V \otimes W$** (operation 9 from the topic page). For (b), the outer product $(u, v) \mapsto u v^t$ is bilinear, so the universal property gives a unique linear $V \otimes V \to M_2$.

2. **Identify a candidate alternating multilinear form by evaluating on a basis** (operation 5, in spirit). Two linear maps on $V \otimes V$ that agree on the spanning set $\{e_i \otimes e_j\}$ are equal.

---

# Hints

> [!note]- Hint 1
> For (a), use $\dim(V \otimes W) = \dim V \cdot \dim W$. The four basis elements $e_i \otimes e_j$ for $i, j \in \{1, 2\}$ are linearly independent (by the basis result for tensor products) and span (by the dimension count).

> [!note]- Hint 2
> For (b), define a bilinear map $\Gamma : V \times V \to M_2(\mathbb{F})$ by $\Gamma(u, v) := u v^t$ (outer product). Check it is bilinear, then use the [[Thm - Universal Property of the Tensor Product|universal property]] to get a unique linear $\hat\Gamma : V \otimes V \to M_2(\mathbb{F})$.

> [!note]- Hint 3
> For (c), use the result from (b): the map $u \otimes v \mapsto u v^t$ sends elementary tensors to *rank-one* matrices. Conversely, $e_1 \otimes e_1 + e_2 \otimes e_2 \mapsto e_1 e_1^t + e_2 e_2^t = \operatorname{diag}(1, 1) = I_2$, the identity matrix. Is the identity matrix rank-one?

---

# Solution

The plan is to (a) verify dimension and exhibit a basis, (b) construct the matrix isomorphism via the universal property, and (c) use the rank correspondence from (b) to settle whether $e_1 \otimes e_1 + e_2 \otimes e_2$ is elementary.

**Step 1: Dimension and basis (part a).**

$\dim(V \otimes V) = 2 \cdot 2 = 4$. A basis is $\{e_1 \otimes e_1, e_1 \otimes e_2, e_2 \otimes e_1, e_2 \otimes e_2\}$.

> [!note]- Derivation
> By [[Def - Tensor Product of Vector Spaces#The Definition|the dimension formula]], $\dim(V \otimes V) = (\dim V)^2 = 2^2 = 4$.
>
> By the [[Def - Tensor Product of Vector Spaces|basis result]]: if $(e_1, e_2)$ is a basis of $V$, then $\{e_i \otimes e_j\}_{i, j = 1, 2}$ is a basis of $V \otimes V$. The four elements are $e_1 \otimes e_1, e_1 \otimes e_2, e_2 \otimes e_1, e_2 \otimes e_2$.

**Step 2: Construct the isomorphism $V \otimes V \cong M_2(\mathbb{F})$ (part b).**

The bilinear outer product $\Gamma(u, v) = u v^t$ extends to a linear isomorphism $\hat\Gamma : V \otimes V \to M_2$ by the universal property.

> [!note]- Derivation
> Define $\Gamma : V \times V \to M_2(\mathbb{F})$ by $\Gamma(u, v) := u v^t$ — the outer product. Check bilinearity:
> $$\Gamma(\alpha u_1 + \beta u_2, v) = (\alpha u_1 + \beta u_2) v^t = \alpha u_1 v^t + \beta u_2 v^t = \alpha \Gamma(u_1, v) + \beta \Gamma(u_2, v),$$
> and similarly in the second slot. So $\Gamma$ is bilinear.
>
> By the [[Thm - Universal Property of the Tensor Product|universal property]] of the tensor product, there exists a unique linear $\hat\Gamma : V \otimes V \to M_2(\mathbb{F})$ with $\hat\Gamma(u \otimes v) = u v^t$.
>
> To show $\hat\Gamma$ is an isomorphism, it suffices (by equal dimensions $\dim V \otimes V = 4 = \dim M_2(\mathbb{F})$) to show $\hat\Gamma$ is surjective. Equivalently, every $2 \times 2$ matrix is in the image.
>
> Compute $\hat\Gamma$ on the basis:
> - $\hat\Gamma(e_1 \otimes e_1) = e_1 e_1^t = \begin{pmatrix} 1 \\ 0 \end{pmatrix} (1\ 0) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} =: E_{11}$.
> - $\hat\Gamma(e_1 \otimes e_2) = e_1 e_2^t = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = E_{12}$.
> - $\hat\Gamma(e_2 \otimes e_1) = E_{21} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$.
> - $\hat\Gamma(e_2 \otimes e_2) = E_{22} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.
>
> The image $\{E_{11}, E_{12}, E_{21}, E_{22}\}$ is the standard basis of $M_2(\mathbb{F})$. So $\hat\Gamma$ sends a basis of $V \otimes V$ to a basis of $M_2$, hence is a linear isomorphism.

**Step 3: Show $e_1 \otimes e_1 + e_2 \otimes e_2$ is not an elementary tensor (part c).**

Use the isomorphism from (b): $e_1 \otimes e_1 + e_2 \otimes e_2$ corresponds to $I_2$, which has rank 2; elementary tensors $u \otimes v$ correspond to $u v^t$, which has rank $\leq 1$.

> [!note]- Derivation
> By the isomorphism $\hat\Gamma$ from part (b), the element $z := e_1 \otimes e_1 + e_2 \otimes e_2 \in V \otimes V$ corresponds to the matrix
> $$\hat\Gamma(z) = e_1 e_1^t + e_2 e_2^t = E_{11} + E_{22} = I_2,$$
> the $2 \times 2$ identity matrix, which has **rank 2**.
>
> Suppose, for contradiction, $z = u \otimes v$ for some $u, v \in \mathbb{F}^2$. Then $\hat\Gamma(z) = u v^t$, which is a **rank-one** matrix (the rank of an outer product $u v^t$ is $\leq 1$; it equals 1 iff both $u, v \neq 0$). But $\operatorname{rank}(I_2) = 2 \neq 1$. Contradiction.
>
> Hence no $u, v$ exist with $u \otimes v = e_1 \otimes e_1 + e_2 \otimes e_2$. $\blacksquare$

> [!note]- Complete formal solution
> **(a)** $\dim(V \otimes V) = (\dim V)^2 = 4$. A basis is $\{e_1 \otimes e_1, e_1 \otimes e_2, e_2 \otimes e_1, e_2 \otimes e_2\}$.
>
> **(b)** The bilinear map $\Gamma(u, v) = u v^t$ extends by the [[Thm - Universal Property of the Tensor Product|universal property]] to a unique linear $\hat\Gamma : V \otimes V \to M_2(\mathbb{F})$. Computing $\hat\Gamma$ on the basis: $\hat\Gamma(e_i \otimes e_j) = e_i e_j^t = E_{ij}$, the standard matrix unit. The image of a basis is a basis, so $\hat\Gamma$ is an isomorphism.
>
> **(c)** Under $\hat\Gamma$, the element $e_1 \otimes e_1 + e_2 \otimes e_2$ corresponds to $I_2$, the identity matrix of rank 2. Elementary tensors $u \otimes v$ correspond to rank-one matrices $u v^t$. Since $\operatorname{rank}(I_2) = 2 \neq 1$, $I_2$ is not an outer product, so $e_1 \otimes e_1 + e_2 \otimes e_2$ is not an elementary tensor. $\blacksquare$

---

# Key Takeaways

**The tensor product $V \otimes V$ is isomorphic to the space of bilinear forms on $V' \times V'$, and (in finite dimensions) to $\mathcal{L}(V', V) \cong M_n(\mathbb{F})$.** This exercise establishes the most useful concrete model of $V \otimes V$: matrices. The elementary tensor $u \otimes v$ becomes the outer-product matrix $u v^t$, and the dimension counts match: $\dim(V \otimes V) = n^2 = \dim M_n$. This identification turns abstract tensor-product computations into concrete matrix computations. The trigger to use it: whenever you encounter $V \otimes V$ or $V^* \otimes V$ for a finite-dimensional space, you can replace it by $M_n(\mathbb{F})$ (or $\mathcal{L}(V, V)$), with elementary tensors becoming rank-one matrices. The same identification works for $V \otimes W$ as $M_{m \times n}(\mathbb{F})$ when $\dim V = m, \dim W = n$.

**Elementary tensors are rank-one matrices; the failure of an element of $V \otimes W$ to be elementary is the failure of the corresponding matrix to be rank-one.** This is the **algebraic foundation of quantum entanglement**. A "product state" in quantum mechanics is a state $|\psi\rangle \otimes |\phi\rangle$ — an elementary tensor in $\mathcal{H}_1 \otimes \mathcal{H}_2$. An **entangled state** is one that *cannot* be written as a product state — like the singlet $|\!\uparrow\downarrow\rangle - |\!\downarrow\uparrow\rangle$, which corresponds to a rank-2 matrix in $M_2$, not a rank-one one. So entanglement is *literally* "the corresponding matrix has rank $> 1$", and the **Schmidt rank** of a state is the rank of the corresponding matrix. This translation between tensor structure and matrix rank is one of the deepest applications of linear algebra in physics.

**The universal property is the right tool for constructing linear maps on tensor products, even in this concrete-feeling case.** One could try to define $\hat\Gamma$ directly on elementary tensors and "extend linearly" — but as discussed in the [[Linear Algebra IX — §9 Multilinear Algebra and Determinants#Legal Operations|topic page's illegal operations]], this requires care because elementary tensors do not have unique representations. The universal property does the well-definedness check for free: as long as the formula $\Gamma(u, v) = u v^t$ is *bilinear* in $(u, v)$, it lifts uniquely to a linear $\hat\Gamma$ on the tensor product. The same pattern works for every tensor-product construction: $V \otimes \mathbb{F} \cong V$, $V \otimes W \cong W \otimes V$, $(U \otimes V) \otimes W \cong U \otimes (V \otimes W)$, etc. Get used to the routine: write a bilinear formula, invoke the universal property, check it is an isomorphism by dimensions or by exhibiting an inverse.
