---
type: exercise-index
subject: hodge-theory
section: "1.1"
tags: [geometry, hodge-theory, differential-forms]
---

## §1.1 The Hodge Star Operator — Exercises

This section drills the algebraic properties of the Hodge star operator on (pseudo-)Riemannian manifolds, with emphasis on coordinate computation, sign conventions across signatures, and the geometric meaning of the star as a metric-and-orientation duality. The exercises cluster around computing $\star$ explicitly on small manifolds (Euclidean $\mathbb{R}^3$, the round $S^2$), translating between form-language and classical vector-calculus / electromagnetic formulations, and verifying the algebraic identities ($\star\star$, [[Def - Isometry|isometry]], intertwining with $d$). The recurring techniques are the orthonormal-coframe formula $\star\sigma^I = \mathrm{sgn}(I, I^c)\epsilon_I\sigma^{I^c}$ and careful sign-tracking through the signature parameter $s$.

- [[Ex - Hodge Star on R^3 Recovers Cross Product and Scalar Triple Product]] (⭐) — direct coordinate computation of $\star$ on every basis form in Euclidean $\mathbb{R}^3$, showing the cross product is $(\star(u^\flat\wedge v^\flat))^\sharp$ and the scalar triple product is $\star(u^\flat\wedge v^\flat\wedge w^\flat)$ ([[Def - The Hodge Star Operator]], [[Thm - Properties of the Hodge Star]], [[Def - Musical Isomorphism (Flat and Sharp)]])
- [[Ex - Computing the Hodge Star on S^2]] (⭐⭐) — Hodge star on the round sphere in spherical coordinates, deriving the Laplace–Beltrami operator $\Delta f = -\star d\star df$ from form-language operations ([[Def - The Hodge Star Operator]], [[Def - Riemannian Volume Form]], [[Thm - Properties of the Hodge Star]], [[Def - Hodge Laplacian]])
- [[Ex - Self-Duality of the Electromagnetic Tensor in Minkowski]] (⭐⭐⭐) — eigenvalue analysis of $\star$ on $2$-forms in Lorentzian $4$D, contrasting with Riemannian, and the complex self-dual combination $F + i\star F$ as electromagnetic duality ([[Def - The Hodge Star Operator]], [[Def - Self-Dual and Anti-Self-Dual Forms]], [[Def - Minkowski Space and the Metric]], [[Thm - Properties of the Hodge Star]])
