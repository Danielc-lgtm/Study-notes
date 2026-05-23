---
type: exercise-index
subject: linear-algebra
section: "3E"
tags: [algebra, linear-algebra]
---

## §3E Products and Quotients of Vector Spaces — Exercises

This section drills the two new constructions of §3E: the **product** of vector spaces and the **quotient** by a [[Def - Subspace|subspace]]. The product is the easy direction — its dimension is the sum of [[Def - Dimension|dimensions]], its bases are concatenations of basis lists, and it gives the external version of the internal direct sum. The quotient is the deep direction. Its elements are *equivalence classes* (translates $v + U$), and the well-definedness of the quotient operations is the structural payoff that makes the [[Thm - Quotient Space Dimension and the Fundamental Theorem Reread|first isomorphism theorem]] possible. The central exercise drills *the first isomorphism theorem for vector spaces*, the cleanest structural identity in the chapter: $V/\operatorname{null} T \cong \operatorname{range} T$. The other exercises cover the partition property of [[Def - Coset|cosets]], the dimension formula $\dim V/U = \dim V - \dim U$, and the relation between quotients and complementary [[Def - Subspace|subspaces]]. Master the quotient construction here — exactly the same construction recurs in [[Def - Module|module]] theory, [[Def - Ring|ring]] theory, topology, and homological algebra throughout the rest of the vault.

- [[Ex - Quotient by null space is isomorphic to range]] (⭐⭐) — the first isomorphism theorem for vector spaces, with the structural rereading of rank-nullity ([[Def - Quotient Space]], [[Def - Quotient Map of Linear Map]], [[Def - Null Space and Range]], [[Thm - Fundamental Theorem of Linear Maps]], [[Thm - Quotient Space Dimension and the Fundamental Theorem Reread]])

- **Translates of a subspace and the partition property** (⭐) — Show that for a subspace $U \leq V$ and $v, w \in V$, the translates $v + U$ and $w + U$ are either equal or disjoint, with equality iff $v - w \in U$. ([[Def - Affine Subset]], [[Def - Subspace]])

- **[[Def - Dimension|Dimension]] of a quotient** (⭐) — Show that for finite-dimensional $V$ and subspace $U \leq V$, $\dim(V/U) = \dim V - \dim U$. ([[Def - Quotient Space]], [[Def - Quotient Map of Linear Map]], [[Thm - Fundamental Theorem of Linear Maps]])

- **Solution sets of linear equations are translates or empty** (⭐⭐) — Let $T \in \mathcal{L}(V, W)$ and $c \in W$. Show that $\{x \in V : Tx = c\}$ is either the empty set or a translate of $\operatorname{null} T$. Conclude that solution sets of linear equation systems $\mathbf{A}\mathbf{x} = \mathbf{b}$ are affine subsets of $\mathbb{F}^n$. ([[Def - Affine Subset]], [[Def - Null Space and Range]])

- **Affine combinations characterise translates** (⭐⭐) — A nonempty subset $A \subseteq V$ is a translate of some subspace if and only if $\lambda v + (1 - \lambda) w \in A$ for all $v, w \in A$ and all $\lambda \in \mathbb{F}$. This characterises affine subsets as those closed under *affine combinations* (combinations whose coefficients sum to $1$). ([[Def - Affine Subset]])

- **Splitting of $V$ as $U \oplus W$** (⭐⭐) — If $V$ is finite-dimensional and $U$ is a subspace, then $V$ is isomorphic to $U \times (V/U)$. The isomorphism uses a chosen complement $W$ of $U$ — extend a basis of $U$ to a basis of $V$ and let $W$ be the span of the added vectors. ([[Def - Product of Vector Spaces]], [[Def - Quotient Space]])

- **Basis of $V/U$ from a basis of a complement** (⭐⭐) — Suppose $V = U \oplus W$ and $w_1, \dots, w_m$ is a basis of $W$. Show that $w_1 + U, \dots, w_m + U$ is a basis of $V/U$. ([[Def - Quotient Space]], [[Def - Basis]])

- **Hyperplanes as kernels of linear functionals** (⭐⭐) — If $\varphi \in \mathcal{L}(V, \mathbb{F})$ is a non-zero functional, prove that $\dim V/\operatorname{null} \varphi = 1$. Conversely, if $U \leq V$ has $\dim V/U = 1$, prove there exists a non-zero functional with $\operatorname{null} \varphi = U$. ([[Def - Quotient Space]], [[Def - Dual Space]])

- **Universal property of the quotient** (⭐⭐⭐) — Let $T \in \mathcal{L}(V, W)$ and $U$ a subspace of $V$ with $U \subseteq \operatorname{null} T$. Prove that there exists a unique $S \in \mathcal{L}(V/U, W)$ such that $T = S \circ \pi$, where $\pi : V \to V/U$ is the quotient map. ([[Def - Quotient Space]], [[Def - Quotient Map of Linear Map]])

- **Infinite-dimensional quotient example** (⭐⭐) — Let $U = \{(x_1, x_2, \dots) \in \mathbb{F}^\infty : x_k \neq 0 \text{ only for finitely many } k\}$ (the finitely-supported sequences). Show that $U$ is a subspace of $\mathbb{F}^\infty$ and that $\mathbb{F}^\infty / U$ is infinite-dimensional. ([[Def - Quotient Space]], [[Def - Subspace]])
