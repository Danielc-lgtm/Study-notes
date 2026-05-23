---
type: exercise-index
subject: linear-algebra
section: "3F"
tags: [algebra, linear-algebra]
---

## §3F Duality — Exercises

This section drills the dual-space construction: the [[Def - Dual Space|dual space]] $V'$ of linear functionals, the [[Def - Dual Basis|dual basis]] of a chosen basis, the [[Def - Dual Map|dual map]] $T'$ of a linear map $T$, and the [[Def - Annihilator (Dual Space)|annihilator]] $U^0$ of a subspace. The exercises cover the foundational dimension theorem ($\dim V' = \dim V$), the [[Def - Annihilator|annihilator]] dimension formula ($\dim U + \dim U^0 = \dim V$), the four-corner duality identities ($\operatorname{null} T' = (\operatorname{range} T)^0$ and dual versions), the canonical double-dual isomorphism, and the matrix-level identification of transpose with dual map. The central exercise is the **double-dual natural isomorphism** $V \cong V''$, which is the cleanest instance of *naturality* (basis-free isomorphism) in linear algebra, and the closing exercise on **row-rank-equals-column-rank** which reaps a famous classical identity as a direct corollary of duality. The exercises here are forward-leaning: the patterns drilled ([[Def - Annihilator|annihilators]], naturality, transpose-as-dual) recur in differential geometry, functional analysis, and algebraic geometry, and are the foundation for inner-product duality in [[Linear Algebra VI — §6 Inner Product Spaces|Chapter 6]] and beyond.

- [[Ex - Dual of a finite-dimensional space]] (⭐) — the dual basis is a basis of $V'$, and $\dim V' = \dim V$ ([[Def - Dual Space]], [[Def - Dual Basis]], [[Def - Basis]], [[Thm - Dimension of Dual Space]])

- [[Ex - Annihilator of a subspace has complementary dimension]] (⭐⭐) — $\dim U + \dim U^0 = \dim V$ for $U \leq V$ finite-dimensional, with both basis-extension and dual-inclusion proofs ([[Def - Annihilator (Dual Space)]], [[Thm - Dimension of Dual Space]], [[Thm - Fundamental Theorem of Linear Maps]])

- [[Ex - Double dual is naturally isomorphic to the original]] (⭐⭐) — the canonical evaluation map $\Lambda : V \to V''$ is a natural isomorphism in finite [[Def - Dimension|dimensions]] ([[Def - Dual Space]], [[Def - Dual Map]], [[Thm - Dimension of Dual Space]], [[Thm - Fundamental Theorem of Linear Maps]])

- [[Ex - Row rank equals column rank]] (⭐⭐) — derive the classical identity from duality: row rank of $A$ = $\dim \operatorname{range} T$ = $\dim \operatorname{range} T'$ = column rank of $A^t$ = row rank of $A$ ([[Def - Rank of a Linear Map]], [[Def - Dual Map]], [[Thm - Matrix of Dual Map is Transpose]], [[Thm - Null Space and Range of Dual Map]])

- **A non-zero vector is detected by some functional** (⭐) — For finite-dimensional $V$ and $v \in V$ with $v \neq 0$, prove there exists $\varphi \in V'$ with $\varphi(v) = 1$. (In infinite [[Def - Dimension|dimensions]] this is Hahn-Banach.) ([[Def - Dual Space]], [[Def - Dual Basis]])

- **Existence of a functional vanishing on a proper subspace** (⭐) — For finite-dimensional $V$ and a proper subspace $U \subsetneq V$, prove there exists $\varphi \in V'$ that vanishes on $U$ but is not the zero functional. ([[Def - Dual Space]], [[Def - Annihilator (Dual Space)]])

- **Null spaces of functionals and scalar multiples** (⭐⭐) — For $\varphi, \beta \in V'$, prove $\operatorname{null} \varphi \subseteq \operatorname{null} \beta$ if and only if $\beta = c \varphi$ for some $c \in \mathbb{F}$. ([[Def - Dual Space]], [[Def - Null Space and Range]])

- **Dual basis at a shifted point** (⭐⭐) — Find the dual basis of the basis $1, x - a, (x - a)^2, \dots, (x - a)^m$ of $\mathcal{P}_m(\mathbb{R})$ for fixed $a \in \mathbb{R}$. (Hint: Taylor expansion gives $\varphi_j(p) = p^{(j)}(a)/j!$.) ([[Def - Dual Basis]])

- **Coordinates of a functional in the dual basis** (⭐) — Suppose $v_1, \dots, v_n$ is a basis of $V$ with dual basis $\varphi_1, \dots, \varphi_n$. Prove that for every $\psi \in V'$, $\psi = \psi(v_1) \varphi_1 + \cdots + \psi(v_n) \varphi_n$. ([[Def - Dual Basis]])

- **Algebraic properties of the dual** (⭐) — For $S, T \in \mathcal{L}(V, W)$ and $\lambda \in \mathbb{F}$, prove $(S + T)' = S' + T'$ and $(\lambda T)' = \lambda T'$. ([[Def - Dual Map]])

- **Dual of the identity** (⭐) — Show that the dual of the identity operator on $V$ is the identity operator on $V'$. ([[Def - Dual Map]])

- **Dualisation preserves invertibility** (⭐⭐) — Suppose $V, W$ finite-dimensional and $T \in \mathcal{L}(V, W)$. Prove that $T$ is invertible iff $T' \in \mathcal{L}(W', V')$ is invertible, with $(T')^{-1} = (T^{-1})'$. ([[Def - Dual Map]])

- **Dualisation is an isomorphism of $\mathcal{L}$-spaces** (⭐⭐) — For finite-dimensional $V, W$, the map $T \mapsto T'$ is an isomorphism $\mathcal{L}(V, W) \cong \mathcal{L}(W', V')$. ([[Def - Dual Map]], [[Thm - Dimension of Dual Space]])

- **Annihilator and inclusion** (⭐⭐) — For [[Def - Subspace|subspaces]] $U, W \leq V$ with $V$ finite-dimensional: (a) $W^0 \subseteq U^0$ iff $U \subseteq W$. (b) $W^0 = U^0$ iff $U = W$. ([[Def - Annihilator (Dual Space)]])

- **Annihilator turns sum into intersection** (⭐⭐) — For finite-dimensional $V$ and [[Def - Subspace|subspaces]] $U, W \leq V$: $(U + W)^0 = U^0 \cap W^0$ and $(U \cap W)^0 = U^0 + W^0$. ([[Def - Annihilator (Dual Space)]], [[Thm - Dimension of a Sum of Subspaces]])

- **Subspace recovered from its annihilator** (⭐⭐⭐) — For finite-dimensional $V$ and subspace $U \leq V$: $U = \{v \in V : \varphi(v) = 0 \text{ for all } \varphi \in U^0\}$. This is the "double annihilator" identity. ([[Def - Annihilator (Dual Space)]], [[Ex - Annihilator of a subspace has complementary dimension]])
