---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Dual Map"
  - "Def - Dual Basis"
  - "Def - Matrix of a Linear Map"
  - "Def - Matrix Multiplication"
tags: [algebra, linear-algebra]
---

# Notation

$V$ and $W$ are finite-dimensional vector spaces over $\mathbb{F}$. We fix bases $v_1, \dots, v_n$ of $V$ and $w_1, \dots, w_m$ of $W$, with dual bases $\varphi_1, \dots, \varphi_n$ of $V'$ and $\psi_1, \dots, \psi_m$ of $W'$. For $T \in \mathcal{L}(V, W)$, the matrix is $\mathcal{M}(T) \in \mathbb{F}^{m,n}$, computed in these bases. The matrix of the dual map $T' \in \mathcal{L}(W', V')$, $\mathcal{M}(T') \in \mathbb{F}^{n,m}$, is computed in the dual bases (so $\psi$'s for input, $\varphi$'s for output). The **transpose** of a matrix $A \in \mathbb{F}^{m,n}$ is $A^t \in \mathbb{F}^{n,m}$, with entries $(A^t)_{j,k} = A_{k,j}$. Full registry on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

---

# Statement

> **Theorem (Matrix of the Dual Map).** Let $V$ and $W$ be finite-dimensional vector spaces over $\mathbb{F}$, with bases $v_1, \dots, v_n$ and $w_1, \dots, w_m$ and dual bases $\varphi_1, \dots, \varphi_n$ and $\psi_1, \dots, \psi_m$. For $T \in \mathcal{L}(V, W)$,
> $$\mathcal{M}(T') = \big( \mathcal{M}(T) \big)^t.$$
> The matrix of the dual map, computed in the dual bases, is the *transpose* of the matrix of the original linear map.

A direct corollary: for $S \in \mathcal{L}(V, W)$ and $T \in \mathcal{L}(W, U)$,
$$(TS)' = S' T' \quad \text{at the level of dual maps} \qquad \Longleftrightarrow \qquad (\mathcal{M}(T) \mathcal{M}(S))^t = \mathcal{M}(S)^t \mathcal{M}(T)^t \quad \text{at the level of matrices}.$$
That is, the matrix identity $(AB)^t = B^t A^t$ is *contravariant functoriality* of the dual operation, read at the level of matrices.

---

# Motivation

The dual map has a natural matrix representation in dual bases, and the question is what it looks like. The answer — *the transpose of the original* — is striking for two reasons. First, it shows that the transpose operation, defined indexically as "swap rows and columns", has a deep structural meaning: it is the matrix expression of dualisation. Second, it explains why the transpose flips order in products: $(AB)^t = B^t A^t$ is the matrix shadow of $(ST)' = T'S'$, which is contravariant functoriality.

Both observations are *useful* far beyond their immediate context. Once you recognise the transpose as the dual map, a host of matrix identities become structural facts about linear maps. "Row rank equals column rank" becomes "the rank of $T$ equals the rank of $T'$" (the present chapter's Thm [[Thm - Null Space and Range of Dual Map]]). "Symmetric matrices have orthogonal eigenvectors" becomes a statement about self-adjoint operators (Chapter 7). And the entire machinery of dualisation in differential geometry — pullback of forms, transpose of derivatives — is the same structural pattern lifted to manifolds.

The theorem is one of the few places where a *computational* identity (the transpose formula) and a *structural* identity (the dual map) are explicitly related, and seeing the relation is one of the high-leverage insights of linear algebra.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal preconditions are finite-dimensionality and chosen bases. The disguised sources are:

The first disguised source is **any matrix identity involving the transpose**. The contravariant functoriality $(ST)' = T'S'$ translates directly into matrix identities by the theorem; the most useful is $(AB)^t = B^t A^t$, which can therefore be proved structurally without index manipulation. *Example problem:* prove $(AB)^t = B^t A^t$ for matrices $A \in \mathbb{F}^{m,n}$ and $B \in \mathbb{F}^{n,p}$ — interpret as linear maps and dualise.

The second disguised source is **a question about $\operatorname{rank}(A^t)$**. The rank of the transpose matrix is the rank of the dual map (by the theorem), which equals the rank of $T$ (by [[Thm - Null Space and Range of Dual Map|the dual rank theorem]]), which equals the column rank of $A$ ([[Def - Rank of a Linear Map]]). So rank of $A$ equals rank of $A^t$. *Example problem:* row rank equals column rank, see [[Ex - Row rank equals column rank]].

The third disguised source is **a problem written in terms of "the dual" that you would rather solve in matrix form**. Whenever the dual map appears in an abstract setting, choose dual bases and compute with the transpose matrix. *Example problem:* if $T : \mathbb{R}^2 \to \mathbb{R}^3$ has matrix $\begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$ in standard bases, then $T' : \mathbb{R}^{3 \prime} \to \mathbb{R}^{2 \prime}$ has matrix $\begin{pmatrix} 1 & 3 & 5 \\ 2 & 4 & 6 \end{pmatrix}$ in the dual bases.

**Targets (Output Amplification)**

Combine with **rank-nullity on both $T$ and $T'$** ([[Thm - Fundamental Theorem of Linear Maps]] applied dually) to get **column rank of $A$ = column rank of $A^t$ = row rank of $A$**. The rank equality is one of the most-used corollaries of duality in elementary linear algebra.

Combine with **the formula for matrix multiplication**. The product $(AB)^t = B^t A^t$ becomes, after recognizing the transpose as the dual, the contravariance identity at the level of matrices. *Useful for:* understanding *why* the order reverses, beyond index-pushing. It is because dualisation reverses arrows.

Combine with **the inner product duality** ([[Linear Algebra VI — §6 Inner Product Spaces|Chapter 6]]). Under Riesz representation $V \cong V'$, the dual map becomes the adjoint $T^*$, whose matrix is the *conjugate transpose* of $\mathcal{M}(T)$. So the present theorem is the real case (no conjugation) of the more general adjoint-matrix theorem.

---

# Why Is It True

The computation is mechanical but the underlying structure is what counts. The matrix entry $\mathcal{M}(T)_{j,k}$ is defined by the expansion $Tv_k = \sum_j \mathcal{M}(T)_{j,k} w_j$. The matrix entry $\mathcal{M}(T')_{r,s}$ is defined by $T'(\psi_s) = \sum_r \mathcal{M}(T')_{r,s} \varphi_r$. The connection between them is the *biorthogonality* of dual bases: $\varphi_j(v_k) = \delta_{jk}$ and $\psi_j(w_k) = \delta_{jk}$.

Apply both sides of $T'(\psi_s) = \sum_r \mathcal{M}(T')_{r,s} \varphi_r$ to the vector $v_k$:
- Left side: $(T'(\psi_s))(v_k) = (\psi_s \circ T)(v_k) = \psi_s(T v_k) = \psi_s(\sum_j \mathcal{M}(T)_{j,k} w_j) = \sum_j \mathcal{M}(T)_{j,k} \delta_{sj} = \mathcal{M}(T)_{s,k}$.
- Right side: $\sum_r \mathcal{M}(T')_{r,s} \varphi_r(v_k) = \sum_r \mathcal{M}(T')_{r,s} \delta_{rk} = \mathcal{M}(T')_{k,s}$.

Equating: $\mathcal{M}(T')_{k,s} = \mathcal{M}(T)_{s,k}$. This is exactly the definition of the transpose, $(\mathcal{M}(T)^t)_{k,s} = \mathcal{M}(T)_{s,k}$. So $\mathcal{M}(T') = \mathcal{M}(T)^t$.

> **The whole intuition in one sentence: the matrix entry computation $\psi_s(Tv_k) = \mathcal{M}(T)_{s,k}$ is the same as $(\mathcal{M}(T')_{r,s}) \varphi_r(v_k) = \mathcal{M}(T')_{k,s}$, and these two readings of the same scalar force the index swap that defines the transpose.**

The *structural* reason for the swap: the input of $T'$ is a functional on $W$ (with row index from $\{1, \dots, m\}$), the output is a functional on $V$ (with row index from $\{1, \dots, n\}$). So $T'$ has matrix size $n \times m$, transposed from $T$'s $m \times n$ — the size flip alone forces the transpose-shape, and the biorthogonality determines the entries.

---

# What Makes This Hard

The technical content is straightforward index-pushing once the dual-basis identities are written out. The trap is *bookkeeping*: students get confused about which basis of which space is being used, especially when both $V$ and $W$ change roles in the dual map. The clean approach is to write the *defining relation* for each matrix entry — $Tv_k = \sum_j \mathcal{M}(T)_{j,k} w_j$ for $T$, $T'(\psi_s) = \sum_r \mathcal{M}(T')_{r,s} \varphi_r$ for $T'$ — and then use biorthogonality to read off entries. The other slip is mixing up the dual basis indices: $\varphi_j$ is dual to $v_j$ (so $\varphi_j(v_k) = \delta_{jk}$), and similarly $\psi_j$ to $w_j$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Compute one entry of $\mathcal{M}(T')$ by applying its defining identity to a basis vector of $V$, then use biorthogonality of dual bases to extract a single entry of $\mathcal{M}(T)$ — but with indices swapped.

**Subgoal decomposition:**

1. **State the defining relations.** $Tv_k = \sum_j \mathcal{M}(T)_{j,k} w_j$ and $T'(\psi_s) = \sum_r \mathcal{M}(T')_{r,s} \varphi_r$.
   - *Hint:* These are the definitions of the matrices of $T$ and $T'$.
   - *Why needed:* Both define the entries you want to compare.

2. **Apply the second relation to $v_k$.** $T'(\psi_s)(v_k) = \sum_r \mathcal{M}(T')_{r,s} \varphi_r(v_k) = \mathcal{M}(T')_{k,s}$, using $\varphi_r(v_k) = \delta_{rk}$.
   - *Hint:* Biorthogonality collapses the sum.
   - *Why needed:* Computes one side of the equation.

3. **Compute the same scalar another way.** $T'(\psi_s)(v_k) = \psi_s(Tv_k) = \psi_s(\sum_j \mathcal{M}(T)_{j,k} w_j) = \mathcal{M}(T)_{s,k}$, using $\psi_s(w_j) = \delta_{sj}$.
   - *Hint:* Use $T'(\psi) = \psi \circ T$ and biorthogonality of $\psi$'s.
   - *Why needed:* Computes the other side.

4. **Equate and read off.** $\mathcal{M}(T')_{k,s} = \mathcal{M}(T)_{s,k}$, which is the transpose relation.
   - *Hint:* The transpose by definition has $A^t_{k,s} = A_{s,k}$.
   - *Why needed:* This is the conclusion.

5. **Conclude $\mathcal{M}(T') = \mathcal{M}(T)^t$.**

---

# Lemma Decomposition

> [!note]- Lemma 1: Matrix entry formula via the dual basis
> **Statement:** Let $v_1, \dots, v_n$ be a basis of $V$ with dual basis $\varphi_1, \dots, \varphi_n$, and let $w_1, \dots, w_m$ be a basis of $W$ with dual basis $\psi_1, \dots, \psi_m$. For $T \in \mathcal{L}(V, W)$, the matrix entry $\mathcal{M}(T)_{j,k}$ equals $\psi_j(Tv_k)$.
>
> **Hint:** Take the defining relation $Tv_k = \sum_i \mathcal{M}(T)_{i,k} w_i$ and apply $\psi_j$ to both sides; biorthogonality $\psi_j(w_i) = \delta_{ji}$ extracts $\mathcal{M}(T)_{j,k}$.
>
> **Why needed:** This is the dual-basis formula for matrix entries, used in both directions in the main proof.
>
> > [!note]- Full proof
> > By definition of the matrix of $T$, $Tv_k = \sum_{i=1}^m \mathcal{M}(T)_{i,k} w_i$. Apply $\psi_j$ to both sides:
> > $$\psi_j(Tv_k) = \psi_j\Big(\sum_i \mathcal{M}(T)_{i,k} w_i\Big) = \sum_i \mathcal{M}(T)_{i,k} \psi_j(w_i) = \sum_i \mathcal{M}(T)_{i,k} \delta_{ji} = \mathcal{M}(T)_{j,k}.$$

> [!note]- Lemma 2: Dual matrix entry formula
> **Statement:** With notation as in Lemma 1, the matrix entry $\mathcal{M}(T')_{r,s}$ equals $(T'(\psi_s))(v_r)$, which equals $\psi_s(Tv_r)$.
>
> **Hint:** Apply Lemma 1 in the dual setting: $\mathcal{M}(T')_{r,s} = \varphi_r(T'(\psi_s))$... no, actually the right form is the analogous formula applied to $T'$ between dual spaces. Then unwind $T'(\psi_s) = \psi_s \circ T$.
>
> **Why needed:** Gives the second computation of the same scalar, to be equated with Lemma 1's.
>
> > [!note]- Full proof
> > By definition of the matrix of $T'$ in the dual bases, $T'(\psi_s) = \sum_r \mathcal{M}(T')_{r,s} \varphi_r$. Apply both sides to $v_k$ (where I rename $k \to r$ in the lemma for clarity, so the index is $r$):
> > $$(T'(\psi_s))(v_r) = \sum_{r'} \mathcal{M}(T')_{r',s} \varphi_{r'}(v_r) = \mathcal{M}(T')_{r,s}.$$
> > Now expand the left side using $T'(\psi) = \psi \circ T$:
> > $$(T'(\psi_s))(v_r) = (\psi_s \circ T)(v_r) = \psi_s(Tv_r).$$
> > By Lemma 1, $\psi_s(Tv_r) = \mathcal{M}(T)_{s,r}$. Hence $\mathcal{M}(T')_{r,s} = \mathcal{M}(T)_{s,r}$.

---

# Formal Proof

> [!note]- Complete formal proof
> Fix bases $v_1, \dots, v_n$ of $V$ and $w_1, \dots, w_m$ of $W$, with dual bases $\varphi_1, \dots, \varphi_n$ of $V'$ and $\psi_1, \dots, \psi_m$ of $W'$. For $T \in \mathcal{L}(V, W)$ and indices $r \in \{1, \dots, n\}$, $s \in \{1, \dots, m\}$:
>
> **Step 1 — matrix entry of $T'$ as a pairing.** By the definition of $\mathcal{M}(T')$ (Lemma 2),
> $$\mathcal{M}(T')_{r,s} = (T'(\psi_s))(v_r).$$
>
> **Step 2 — unwind $T'(\psi_s)$.** By definition of $T'$, $T'(\psi_s) = \psi_s \circ T$, so
> $$(T'(\psi_s))(v_r) = (\psi_s \circ T)(v_r) = \psi_s(Tv_r).$$
>
> **Step 3 — read $\psi_s(Tv_r)$ as a matrix entry of $T$.** By Lemma 1 applied with indices swapped,
> $$\psi_s(Tv_r) = \mathcal{M}(T)_{s,r}.$$
>
> **Step 4 — conclude.** Combining, $\mathcal{M}(T')_{r,s} = \mathcal{M}(T)_{s,r}$ for all $r, s$. By definition of the transpose, this says $\mathcal{M}(T')_{r,s} = (\mathcal{M}(T)^t)_{r,s}$ for all $r, s$, hence
> $$\mathcal{M}(T') = \mathcal{M}(T)^t. \qquad \blacksquare$$

---

# The Identity $(AB)^t = B^t A^t$ as Contravariant Functoriality

This corollary deserves its own subsection because it is the most important consequence of the theorem and the cleanest illustration of contravariant functoriality.

**Setup.** Let $S \in \mathcal{L}(V, W)$ and $T \in \mathcal{L}(W, U)$ be linear maps, with $V, W, U$ all finite-dimensional. Choose bases of each, with dual bases. Let $A = \mathcal{M}(S) \in \mathbb{F}^{m, n}$ and $B = \mathcal{M}(T) \in \mathbb{F}^{p, m}$ (writing $n = \dim V, m = \dim W, p = \dim U$).

**Step 1 — at the level of linear maps.** The dual of the composition $TS : V \to U$ is
$$(TS)' = S' T'$$
by [[Def - Dual Map|contravariance of the dual]]. The reversal is the structural content of "$T$ then $S$ dualises to $S'$ then $T'$".

**Step 2 — apply the present theorem.** $\mathcal{M}((TS)') = \mathcal{M}(TS)^t = (\mathcal{M}(T) \mathcal{M}(S))^t = (BA)^t$ on one hand, and $\mathcal{M}(S' T') = \mathcal{M}(S') \mathcal{M}(T') = A^t B^t$ on the other (note: composition in matrices is in the same order as composition in maps, $\mathcal{M}(S' T') = \mathcal{M}(S') \mathcal{M}(T')$).

**Step 3 — equate.** $(BA)^t = A^t B^t$. Renaming for clarity ($X = B, Y = A$): $(XY)^t = Y^t X^t$.

So the identity $(AB)^t = B^t A^t$ is the matrix shadow of the structural fact $(TS)' = S' T'$. **The transpose reverses order because dualization reverses arrows**, and this is the entire content of the index-juggling identity. Once seen, the identity becomes part of a much larger structural pattern (contravariant functoriality) and is no longer a "coincidence about double sums".

---

# Cross-Field Exercise Suggestions

**Row rank equals column rank, once and for all.** The cleanest proof goes through the present theorem and [[Thm - Null Space and Range of Dual Map]]: rank of $A$ = $\dim \operatorname{range} T$ = $\dim \operatorname{range} T'$ = rank of $\mathcal{M}(T') = A^t$ = row rank of $A$. See [[Ex - Row rank equals column rank]].

**Transpose of a product as inverse-pulled-back.** For $A \in \mathrm{GL}_n(\mathbb{F})$, the identity $(A^{-1})^t = (A^t)^{-1}$ follows from $A A^{-1} = I$ via $(A^{-1})^t A^t = I^t = I$ — dualising preserves invertibility and inverts. This is the matrix shadow of "$T$ invertible implies $T'$ invertible with $(T')^{-1} = (T^{-1})'$".

**Numerical linear algebra — solving systems via transpose.** The system $Ax = b$ is solvable iff $b$ is in the column space of $A$; equivalently iff $b$ annihilates every $y$ with $A^t y = 0$ (the left null space). This is the present theorem at work, recognising $A^t$ as the matrix of the dual map and using the annihilator characterisation of the range.

---

# Bridges

- **[[Thm - Null Space and Range of Dual Map]]** — the present theorem is the matrix-level companion. The four-corner identity at the level of subspaces becomes "matrix and transpose have the same rank" at the level of numbers.

- **[[Def - Dual Map]]** — the present theorem is the matrix expression of dualisation. The contravariance identity $(ST)' = T'S'$ becomes $(AB)^t = B^t A^t$ in matrices.

- **Adjoint operator** ([[Linear Algebra VII — §7 Operators on Inner Product Spaces|Chapter 7]]) — for an inner product space, the adjoint $T^*$ has matrix the *conjugate transpose* $\overline{\mathcal{M}(T)}^t$ (or just transpose over $\mathbb{R}$). The present theorem is the real (or "without Riesz identification") version of the adjoint-matrix theorem. Over $\mathbb{R}$, dual map and adjoint match exactly after Riesz identification.

- **Pullback of forms** (Differential Geometry) — the pullback $f^*$ of differential 1-forms by a smooth map $f$ has matrix expression the *transpose of the Jacobian* of $f$ in local coordinates. This is the present theorem applied pointwise on cotangent spaces, and it makes the calculus of differential forms a direct generalisation of the present chapter.

---

# Unlocked by This

> [!tip] Row Rank Equals Column Rank *(from this topic)*
> The cleanest proof of the foundational identity "row rank equals column rank" goes through the present theorem combined with the rank equality from [[Thm - Null Space and Range of Dual Map]]. See [[Ex - Row rank equals column rank]].

> [!tip] Symmetric and Hermitian Matrices *(from Linear Algebra VII)*
> A real matrix is **symmetric** if $A = A^t$. Under the present theorem, this is the matrix condition for the linear map $T$ to satisfy $T = T'$ — meaning $T$ is its own dual. Over the reals with the standard inner product, this becomes the **self-adjoint** condition $T = T^*$, and the spectral theorem for self-adjoint operators (Chapter 7) is one of the deepest theorems in finite-dimensional linear algebra.

> [!tip] Bilinear Forms and Their Matrix Representations *(from Linear Algebra IX)*
> A bilinear form $B : V \times V \to \mathbb{F}$ is *symmetric* if $B(u, v) = B(v, u)$, which is the condition that its matrix (in any basis) is symmetric. The diagonalisation of symmetric bilinear forms via [[Linear Algebra IX — §9 Multilinear Algebra and Determinants|Sylvester's law of inertia]] depends on the transpose being the matrix of the dual, since symmetric matrices are exactly the matrices of dual-self-equal operators.
