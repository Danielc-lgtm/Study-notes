---
type: exercise-index
subject: linear-algebra
section: "3D"
tags: [algebra, linear-algebra]
---

## §3D Invertibility and Isomorphism — Exercises

This section culminates the chapter with [[Def - Invertibility and Isomorphism|invertibility and isomorphism]] of linear maps. The exercises drill three skills. *First*, exhibiting inverses for compositions of invertible maps, including the "socks-and-shoes" reversal $(TS)^{-1} = S^{-1} T^{-1}$ that pervades non-commutative algebra. *Second*, using triangular structure (and other matrix-shape conditions) together with invertibility to deduce structural properties of the inverse — including the principle "*invertibility transfers structural properties through inversion*". *Third*, computing with change-of-basis matrices, verifying that the matrix of the identity in two bases is invertible (with the inverse being the change-of-basis in the opposite direction), and using [[Thm - Change of Basis Formula|the change of basis formula]] $A = C^{-1} B C$. The themes converge on the **similarity classification** of operators: similar matrices are operators in different bases, and the project of finding "the simplest matrix in a similarity class" begins here.

- [[Ex - Composition of invertible linear maps is invertible]] (⭐) — the socks-and-shoes reversal $(TS)^{-1} = S^{-1} T^{-1}$; direct verification by associativity ([[Def - Invertibility and Isomorphism]], [[Def - Linear Map]]).
- [[Ex - Inverse of a triangular matrix is triangular]] (⭐⭐) — triangularity of a matrix is preserved under inversion, with diagonal entries inverting; uses the invariant-[[Def - Subspace|subspace]] interpretation of triangularity ([[Def - Matrix of a Linear Map]], [[Def - Invertibility and Isomorphism]], [[Thm - Injectivity Equals Surjectivity in Finite Dimensions]]).
- [[Ex - Matrix of identity in two bases is invertible]] (⭐) — the change-of-basis matrices in opposite directions are mutual inverses; one-line application of the composition theorem to $I \circ I = I$ ([[Def - Change of Basis Matrix]], [[Def - Matrix of a Linear Map]], [[Thm - Composition Corresponds to Matrix Multiplication]]).
