---
type: exercise-index
subject: linear-algebra
section: "2C"
tags: [algebra, linear-algebra]
---

## §2C Dimension — Exercises

The exercises of §2C drill the use of [[Def - Dimension|dimension]] as the integer-valued invariant that converts geometric and structural questions about finite-dimensional spaces into arithmetic. The key tools are the **length-of-basis shortcuts** ([[Thm - Length of Linearly Independent List Bounded by Length of Spanning List|2.22]] Corollaries 2 and 3 / [[Ex - A list with the right length is a basis iff spanning iff independent]]): a list of length $\dim V$ is a basis as soon as it is either independent or spanning. Combined with [[Thm - Dimension of a Sum of Subspaces|the dimension formula 2.43]], this is the principal tool for "find a basis", "compute a dimension", and "show two [[Def - Subspace|subspaces]] meet nontrivially" problems. The exercises in this section are where dimension genuinely earns its keep as a *comparative* invariant — and where the inclusion-exclusion structure of [[Def - Subspace|subspaces]] becomes computationally usable.

- [[Ex - A list with the right length is a basis iff spanning iff independent]] (⭐) — in a finite-dimensional space of dimension $n$, a list of length $n$ is a basis iff linearly independent iff spanning. The length-of-basis shortcut, derived from the structural theorems 2.30 and 2.32 ([[Def - Basis]], [[Def - Dimension]], [[Thm - Length of Linearly Independent List Bounded by Length of Spanning List]], [[Thm - Bases are Equinumerous]], [[Thm - Every Spanning List Contains a Basis]], [[Thm - Every Linearly Independent List Extends to a Basis]]).
- [[Ex - Dimension of a subspace equals dimension only if equal]] (⭐⭐) — if $U \subseteq V$ with $\dim U = \dim V$ in finite [[Def - Dimension|dimensions]], then $U = V$. The "non-shrinking" property of full-dimensional subspaces, derived by basis extension and the well-definedness of dimension ([[Def - Subspace]], [[Def - Dimension]], [[Def - Basis]], [[Thm - Every Linearly Independent List Extends to a Basis]], [[Thm - Bases are Equinumerous]]).
- [[Ex - Sum of dimensions in direct sum]] (⭐⭐) — in a direct sum $V = U \oplus W$ with bases of $U$ and $W$, the concatenated list is a basis of $V$, and $\dim V = \dim U + \dim W$. The constructive form of the additivity of dimension across direct sums; also appears in §2B ([[Def - Basis]], [[Def - Direct Sum]], [[Def - Dimension]], [[Thm - Dimension of a Sum of Subspaces]]).
