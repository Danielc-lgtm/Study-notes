---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Product of Vector Spaces"
  - "Def - Basis"
  - "Def - Dimension"
  - "Def - Direct Sum"
tags: [algebra, linear-algebra]
---

# Notation

$V_1, \dots, V_m$ are vector spaces over a field $\mathbb{F}$. The product is $V_1 \times \cdots \times V_m$; see [[Def - Product of Vector Spaces]]. We write $\dim V$ for the dimension and use $\iota_k : V_k \to V_1 \times \cdots \times V_m$ for the inclusion into the $k$-th slot. Full registry on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

---

# Statement

> **Theorem ([[Def - Dimension|Dimension]] of a Product).** Let $V_1, \dots, V_m$ be finite-dimensional vector spaces over $\mathbb{F}$. Then the product $V_1 \times \cdots \times V_m$ is finite-dimensional, and
> $$\dim(V_1 \times \cdots \times V_m) = \dim V_1 + \dim V_2 + \cdots + \dim V_m.$$

> **Companion (Sum as [[Def - Direct Sum|Direct Sum]]).** Suppose $V_1, \dots, V_m$ are [[Def - Subspace|subspaces]] of a common vector space $V$. The sum $V_1 + \cdots + V_m$ is a direct sum if and only if the natural map
> $$\Gamma : V_1 \times \cdots \times V_m \to V_1 + \cdots + V_m, \quad \Gamma(v_1, \dots, v_m) = v_1 + \cdots + v_m,$$
> is injective. In that case it is an isomorphism, and the [[Def - Dimension|dimension]] formula reads $\dim(V_1 \oplus \cdots \oplus V_m) = \dim V_1 + \cdots + \dim V_m$.

The product and direct-sum dimension formulas have the same shape because the constructions are essentially the same — internal direct sum is the image of external product under $\Gamma$.

---

# Motivation

The product of finite-dimensional vector spaces is itself finite-dimensional, and there is exactly one reasonable answer to "what is its dimension". The product $V_1 \times V_2$ has elements $(v_1, v_2)$ with $v_k \in V_k$; an element is $\dim V_1$ free choices in the first slot and $\dim V_2$ free choices in the second, so the total degrees of freedom is $\dim V_1 + \dim V_2$. The theorem makes this counting argument precise by exhibiting an explicit basis.

The companion statement does what the dimension formula was *built to do*: convert the external product construction to the internal direct-sum construction whenever the two coincide. When $V_1, \dots, V_m$ live inside a common ambient $V$, the question "is $V_1 + \cdots + V_m$ a direct sum?" is the same as the question "is $\Gamma$ injective?", which is purely about whether the only way to write $0$ as $v_1 + \cdots + v_m$ with $v_k \in V_k$ is to take all $v_k = 0$.

In one sentence: the external product is the "free" version of a sum of [[Def - Subspace|subspaces]], and it agrees with the internal direct sum exactly when no nontrivial cancellation happens.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is that the spaces $V_1, \dots, V_m$ are finite-dimensional. The interesting source question is: when does a problem secretly contain a product, even though no $\times$ is written?

The first disguised source is **a basis is given as a concatenation of independent sublists**. If $V$ has a basis that can be split as $v_1, \dots, v_n = (\text{basis of } V_1) \cup (\text{basis of } V_2) \cup \cdots$, with the $V_k$ subspaces, then $V$ is internally a direct sum $V_1 \oplus \cdots \oplus V_m$, hence isomorphic to the external product. *Example problem:* polynomials of degree $\leq n$ split as $\mathbb{F} \oplus \mathbb{F} x \oplus \cdots \oplus \mathbb{F} x^n$, with each summand 1-dimensional and the sum direct; $\dim \mathcal{P}_n = n + 1$ follows.

The second disguised source is **a linear map $T : V \to W_1 \times \cdots \times W_m$ assembled from $m$ component maps**. By the universal property of the product, $T$ is determined by its components $T_k = \pi_k \circ T : V \to W_k$. The product is invoked tacitly any time you have multiple linear maps with a common domain. *Example problem:* a 2D rotation $R_\theta : \mathbb{R}^2 \to \mathbb{R}^2$ is determined by where it sends $e_1$ and $e_2$; combining these gives $R_\theta : \mathbb{R}^2 \to \mathbb{R} \times \mathbb{R}$ via $v \mapsto (\langle R_\theta v, e_1 \rangle, \langle R_\theta v, e_2 \rangle)$.

The third disguised source is **a Cartesian set of solutions**. Solving a system of linear equations $T_k v = c_k$ in multiple components is equivalent to solving the single equation $T v = c$ for $T = (T_1, \dots, T_m) : V \to W_1 \times \cdots \times W_m$. *Example problem:* finding a vector lying in two affine subsets simultaneously becomes "find the preimage of the diagonal" in a product.

**Targets (Output Amplification)**

The theorem's bare conclusion is the dimension formula. Combined with other facts it does more.

Combine with **the fact that a sum of subspaces is direct iff dimensions add**. Then a sum $V_1 + \cdots + V_m$ inside a finite-dimensional ambient space $V$ is direct exactly when its dimension equals $\dim V_1 + \cdots + \dim V_m$. This is the *dimension test for directness*, and it is by far the easiest test in practice — much easier than checking that every element has a unique decomposition. *Why nonobvious:* the test converts a structural question (uniqueness of decomposition) into a numerical one (sum of dimensions). *Useful because:* counting is mechanical, decomposition is not.

Combine with **a quotient construction**. If $V$ is finite-dimensional and $U \leq V$, then $V \cong U \times (V/U)$ as vector spaces, with dimension $\dim V = \dim U + \dim V/U$ recovered (cf. [[Thm - Quotient Space Dimension and the Fundamental Theorem Reread]]). The isomorphism uses a chosen complement of $U$, so it is not canonical, but its dimension shadow is. *Useful for:* studying $V$ by separately studying $U$ and $V/U$ — the *short exact sequence* viewpoint.

Combine with **the universal property of the product** (linear maps into the product from a common source). Given $m$ linear maps $S_k : W \to V_k$, they assemble into a unique linear map $W \to V_1 \times \cdots \times V_m$. Dimension-wise, this assembly preserves rank: $\dim \operatorname{range}(S_1, \dots, S_m) = \dim \operatorname{range} S_1 + \cdots$ when the ranges are independent. *Useful for:* tracking how a multi-output linear map's rank decomposes.

---

# Why Is It True

The dimension formula is the basis-construction recipe made explicit. **A basis of the product is obtained by inserting each basis vector of each factor into the corresponding slot, with zeros elsewhere.**

Concretely: pick a basis $b_1^{(k)}, \dots, b_{n_k}^{(k)}$ of each $V_k$. For each $k = 1, \dots, m$ and each $j = 1, \dots, n_k$, the vector $\iota_k(b_j^{(k)}) = (0, \dots, 0, b_j^{(k)}, 0, \dots, 0)$ — with $b_j^{(k)}$ in the $k$-th slot — is an element of the product. The list of all such vectors has length $n_1 + n_2 + \cdots + n_m$.

This list is linearly independent: a vanishing linear combination
$$\sum_{k, j} \lambda_{k,j} \iota_k(b_j^{(k)}) = 0$$
must vanish slot by slot, which gives $\sum_j \lambda_{k,j} b_j^{(k)} = 0$ in $V_k$ for each $k$. Since the $b_j^{(k)}$ are a basis of $V_k$, $\lambda_{k,j} = 0$ for all $k, j$. Linear independence.

This list spans: every element of $V_1 \times \cdots \times V_m$ has the form $(v_1, \dots, v_m)$ with $v_k \in V_k$, so $v_k = \sum_j c_{k,j} b_j^{(k)}$, and $(v_1, \dots, v_m) = \sum_{k, j} c_{k,j} \iota_k(b_j^{(k)})$. Span.

So the list is a basis, of length $n_1 + \cdots + n_m$, and the dimension equals this length.

> **The whole intuition in one sentence: an element of the product is one element from each factor, independently chosen, so the degrees of freedom add.**

---

# What Makes This Hard

The theorem itself is straightforward; the trap is in the companion *internal direct sum* statement. Beginners check that $V_1 + \cdots + V_m$ is a direct sum by trying to verify "every element has a unique decomposition", which is harder than necessary. The correct route is via the dimension test or via injectivity of $\Gamma$. The other slip is confusing the external product $V_1 \times V_2$ with the internal direct sum $V_1 \oplus V_2 \subseteq V$: the former is a fresh vector space, the latter is a subspace of $V$ — they are isomorphic but not equal.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build a basis of the product by lifting bases of each factor through the inclusions $\iota_k$. Check linear independence (slot by slot) and spanning (decompose each tuple slot by slot). Count the elements of the basis.

**Subgoal decomposition:**

1. **Define the candidate basis.** For each $k$, choose a basis $b_1^{(k)}, \dots, b_{n_k}^{(k)}$ of $V_k$. Form the list of all $\iota_k(b_j^{(k)})$ for $k = 1, \dots, m, j = 1, \dots, n_k$.
   - *Hint:* The map $\iota_k$ puts $b_j^{(k)}$ in the $k$-th slot and zero elsewhere.
   - *Why needed:* This is the candidate basis whose properties you verify.

2. **Show linear independence.** A vanishing linear combination must vanish in each slot.
   - *Hint:* The $k$-th slot of $\sum_{k, j} \lambda_{k,j} \iota_k(b_j^{(k)})$ is $\sum_j \lambda_{k,j} b_j^{(k)}$. Since the $b_j^{(k)}$ are a basis, each $\lambda_{k,j} = 0$.
   - *Why needed:* Linear independence is half of being a basis.

3. **Show spanning.** Any $(v_1, \dots, v_m)$ is a linear combination of the candidate basis.
   - *Hint:* Write $v_k = \sum_j c_{k,j} b_j^{(k)}$; then $(v_1, \dots, v_m) = \sum_{k, j} c_{k,j} \iota_k(b_j^{(k)})$.
   - *Why needed:* Spanning is the other half of being a basis.

4. **Count.** The basis has $n_1 + \cdots + n_m$ elements, which is the dimension.
   - *Hint:* Counting is automatic — $n_k$ basis elements per slot, $m$ slots.
   - *Why needed:* This is the conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Slot-wise vanishing in the product
> **Statement:** An element $(v_1, \dots, v_m)$ of $V_1 \times \cdots \times V_m$ is zero if and only if $v_k = 0$ in $V_k$ for every $k$.
>
> **Hint:** The zero element of the product is $(0, \dots, 0)$ by definition of componentwise addition.
>
> **Why needed:** This is the basic identity used to convert a vanishing combination in the product into vanishing combinations in each factor.
>
> > [!note]- Full proof
> > The zero element of $V_1 \times \cdots \times V_m$ is $(0_{V_1}, \dots, 0_{V_m})$ by definition. So $(v_1, \dots, v_m) = (0, \dots, 0)$ in the product if and only if equal in each slot, i.e. $v_k = 0_{V_k}$ for every $k$.

> [!note]- Lemma 2: Basis of $V_k$ extends to a basis of the slot in the product
> **Statement:** If $b_1, \dots, b_n$ is a basis of $V_k$, then $\iota_k(b_1), \dots, \iota_k(b_n)$ is a linearly independent list in $V_1 \times \cdots \times V_m$. It spans the image $\iota_k(V_k)$.
>
> **Hint:** $\iota_k$ is injective and linear, so it preserves linear independence; spanning of $\iota_k(V_k)$ follows because $\iota_k(\sum c_j b_j) = \sum c_j \iota_k(b_j)$ for any $\sum c_j b_j \in V_k$.
>
> **Why needed:** It is the building block: each slot contributes its own dimension via this lifted basis.
>
> > [!note]- Full proof
> > For linear independence, suppose $\sum_j \lambda_j \iota_k(b_j) = 0$ in the product. By linearity of $\iota_k$, this is $\iota_k(\sum_j \lambda_j b_j) = 0$. Since $\iota_k$ is injective (its kernel is trivial), $\sum_j \lambda_j b_j = 0$ in $V_k$. The $b_j$ are a basis of $V_k$, so $\lambda_j = 0$ for all $j$.
> >
> > For spanning of $\iota_k(V_k)$: any element of $\iota_k(V_k)$ is $\iota_k(v)$ for some $v \in V_k$. Write $v = \sum_j c_j b_j$, so $\iota_k(v) = \sum_j c_j \iota_k(b_j)$.

---

# Formal Proof

> [!note]- Complete formal proof
> Choose a basis $b_1^{(k)}, \dots, b_{n_k}^{(k)}$ of each $V_k$, where $n_k = \dim V_k$. Define the list $\mathcal{B} \subseteq V_1 \times \cdots \times V_m$ to be the union over $k = 1, \dots, m$ of the lists $\{\iota_k(b_1^{(k)}), \dots, \iota_k(b_{n_k}^{(k)})\}$, where $\iota_k(v) = (0, \dots, v, \dots, 0)$ with $v$ in the $k$-th slot.
>
> **Step 1 — linear independence.** Suppose $\sum_{k=1}^m \sum_{j=1}^{n_k} \lambda_{k, j} \iota_k(b_j^{(k)}) = 0$. The $k$-th slot of the left-hand side is $\sum_j \lambda_{k,j} b_j^{(k)}$, while the $k$-th slot of the right-hand side is $0_{V_k}$. By Lemma 1 (slot-wise vanishing), $\sum_j \lambda_{k,j} b_j^{(k)} = 0$ in $V_k$ for each $k$. Since the $b_j^{(k)}$ form a basis of $V_k$, the coefficients $\lambda_{k,j}$ vanish: $\lambda_{k,j} = 0$ for all $k, j$. Hence $\mathcal{B}$ is linearly independent.
>
> **Step 2 — spanning.** Take any element $(v_1, \dots, v_m) \in V_1 \times \cdots \times V_m$. Expand each $v_k = \sum_j c_{k,j} b_j^{(k)}$. Then
> $$(v_1, \dots, v_m) = \sum_{k=1}^m \iota_k(v_k) = \sum_{k=1}^m \iota_k\left( \sum_{j=1}^{n_k} c_{k,j} b_j^{(k)} \right) = \sum_{k=1}^m \sum_{j=1}^{n_k} c_{k,j} \iota_k(b_j^{(k)}),$$
> using linearity of $\iota_k$ at the last step. So every element of the product is a linear combination of $\mathcal{B}$.
>
> **Step 3 — count.** The list $\mathcal{B}$ has $n_1 + n_2 + \cdots + n_m$ elements (the lists for different $k$ are disjoint because their nonzero entries occupy different slots). Since $\mathcal{B}$ is a basis of the product,
> $$\dim(V_1 \times \cdots \times V_m) = n_1 + \cdots + n_m = \dim V_1 + \cdots + \dim V_m. \qquad \blacksquare$$
>
> **For the companion (direct sum criterion):** the map $\Gamma : V_1 \times \cdots \times V_m \to V_1 + \cdots + V_m$ is surjective by definition of the sum. By the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]], $\Gamma$ is injective iff $\dim(V_1 + \cdots + V_m) = \dim(V_1 \times \cdots \times V_m) = \dim V_1 + \cdots + \dim V_m$. And the sum is direct iff the only way to write $0$ as $v_1 + \cdots + v_m$ with $v_k \in V_k$ is the all-zero decomposition — which is exactly the condition that $\Gamma$ has trivial null space, i.e. $\Gamma$ is injective. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Polynomial-coefficient product.** The space $\mathcal{P}_n(\mathbb{R})$ of polynomials of degree $\leq n$ is canonically the $(n+1)$-fold product $\mathbb{R}^{n+1}$ via "list of coefficients", and the dimension formula confirms $\dim \mathcal{P}_n = n+1$. This is a routine application, but the surprise is that *any* finite-dimensional vector space is some product of $\mathbb{F}^1 = \mathbb{F}$ with itself.

**Block-diagonal matrices.** The space of block-diagonal matrices with $m$ blocks of sizes $k_1, \dots, k_m$ is isomorphic to the product $\mathcal{L}(\mathbb{F}^{k_1}) \times \cdots \times \mathcal{L}(\mathbb{F}^{k_m})$. Its dimension is therefore $k_1^2 + k_2^2 + \cdots + k_m^2$, by combining the present theorem with $\dim \mathcal{L}(\mathbb{F}^k) = k^2$. This shows up in representation theory and in eigenvector decompositions.

**Function space decomposition.** The space of continuous functions on $[0, 1] \cup [2, 3]$ (disjoint union) is isomorphic to $C([0,1]) \times C([2,3])$, by "restrict to each piece". The same disjoint-union-equals-product holds for $L^p$ spaces, smooth functions, and indeed any sheaf-theoretic construction over a disjoint union of bases.

---

# Bridges

- **[[Thm - Dimension of a Sum of Subspaces]]** (from [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]]) — when the spaces are subspaces of a common $V$, the dimension formula for the sum is $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$. The product formula is the case where the intersection is trivial — exactly the case where the sum is direct.

- **[[Thm - Quotient Space Dimension and the Fundamental Theorem Reread]]** — for finite-dimensional $V$ and $U \leq V$, $V \cong U \times (V/U)$ (non-canonically), with the dimension formula $\dim V = \dim U + \dim V/U$. The "splitting" requires choosing a complement of $U$.

- **Categorical product** (general principle) — the product of vector spaces is the categorical product in the category $\operatorname{Vect}_{\mathbb{F}}$; the dimension formula reflects the universal property of the product. In categories where product and coproduct differ (sets, groups, topological spaces), this dimension formula has no direct analogue, but the universal property does.

- **Tensor product** (preview, [[Linear Algebra IX — §9 Multilinear Algebra and Determinants|Chapter 9]]) — the *tensor product* $V \otimes W$ is *not* the same as $V \times W$: it has dimension $(\dim V)(\dim W)$, not $\dim V + \dim W$. The tensor product is the universal object for bilinear maps out, while the product is the universal object for pairs of linear maps in. Confusing them is a common slip; the dimension formula is the cleanest discriminator.

---

# Unlocked by This

> [!tip] Module Direct Sums *(from Module Theory)*
> Products of modules over a ring satisfy the same dimension formula (with rank in place of dimension) for free modules. For general modules, where dimension is not always defined, the product still has a universal property and is functorial.
