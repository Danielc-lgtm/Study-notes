---
type: exercise-index
subject: spinors
section: "1.1"
tags: [geometry, spinors, lie-groups]
---

## §1.1 SU(2) and Spin-Half Rotations — Exercises

This section drills the basic mechanics of the $SU(2) \to SO(3)$ double cover and the spinor representation $\mathbb{C}^2$ of $SU(2)$. The unifying technique is the **Pauli identity** $\sigma_j\sigma_k = \delta_{jk}I + i\epsilon_{jkl}\sigma_l$, which packages the commutator (Lie algebra) and anticommutator (Clifford) structures into a single formula. The signature pattern: encountering a rotation in $\mathbb{R}^3$ and translating it via $u(\hat n, \theta) = \exp(-i\tfrac{\theta}{2}\vec\sigma\cdot\hat n)$ to an element of $SU(2)$. The factor of $\tfrac{1}{2}$ in the exponent is what makes spinors "rotate at half speed" relative to vectors — the source of all $4\pi$-periodicity phenomena.

- [[Ex - Computing the Cover SU(2) to SO(3) on a Specific Rotation]] (⭐⭐) — direct verification of the Pauli-conjugation cover on a $\pi/2$-rotation about the $z$-axis, showing how $u^2$ gives the $\pi$ rotation and $u^4 = -I$ corresponds to the topologically trivial $2\pi$ rotation ([[Def - The Pauli Matrices]], [[Def - SU(2) Action on Spinors]], [[Thm - SU(2) is the Double Cover of SO(3)]]).
- [[Ex - SU(2) is Diffeomorphic to S^3]] (⭐⭐) — topological identification of $SU(2)$ with the unit $3$-sphere $S^3 \subset \mathbb{C}^2$, establishing the simply-connectedness that makes $SU(2)$ the universal cover of $SO(3)$ ([[Def - Lie Group]], [[Thm - SU(2) is the Double Cover of SO(3)]]).
- [[Ex - The Lie Algebra of SO(3) is Antisymmetric Matrices]] (⭐⭐) — computation of $\mathfrak{so}(3)$ as $3 \times 3$ antisymmetric matrices, with the cross product as the Lie bracket, and the identification $\mathfrak{so}(3) \cong \mathfrak{su}(2) \cong (\mathbb{R}^3, \times)$ ([[Def - Lie Algebra]], [[Def - The Lie Algebra of a Lie Group]]).
