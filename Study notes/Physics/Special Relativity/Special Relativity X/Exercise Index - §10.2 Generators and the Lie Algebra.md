---
type: exercise-index
subject: special-relativity
section: "10.2"
tags: [physics, special-relativity, lie-groups]
---

## §10.2 Generators and the Lie Algebra — Exercises

The exercises of §10.2 build fluency with the six generators and their commutators — the entire algebraic content of the Lorentz group. Two of them establish the structure relations by direct matrix multiplication: $[K_1, K_2] = -J_3$ (two boosts bracket to minus a rotation, the seed of the Thomas rotation and of non-compactness) and $[J_3, K_1] = K_2$ (the boost generators transform as a $3$-vector under rotations). A third identifies the rotation block as the familiar cross-product algebra $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$, so the reader recognises half the Lorentz algebra as angular momentum. The fourth assembles the general element from its six parameters and verifies the membership and tracelessness conditions. The unifying observation: the sign pattern $(+, +, -)$ on $([J,J], [J,K], [K,K])$ is the whole structure, and the lone minus sign in $[K,K] = -J$ — the difference from the compact Euclidean $\mathfrak{so}(4)$ — is where all the interesting physics lives.

- [[Ex - Deriving the commutator of two boost generators]] (⭐⭐) — multiply the explicit boost-generator matrices to obtain $[K_1, K_2] = -J_3$, establish the relation $[K_i, K_j] = -\epsilon_{ijk}J_k$, and explain why the minus sign distinguishes the non-compact $\mathfrak{so}(1,3)$ from $\mathfrak{so}(4)$ and forbids a boost subgroup ([[Def - Lie Algebra of the Lorentz Group]], [[Def - Generators and Structure Constants]]).

- [[Ex - The boost-rotation commutator and why boosts do not close]] (⭐⭐) — compute $[J_3, K_1] = K_2$ to confirm $[J_i, K_j] = \epsilon_{ijk}K_k$ (the boost is a vector operator), show $[J_3, K_3] = 0$ geometrically, and prove the rotations close into $\mathfrak{so}(3)$ while the boosts do not ([[Def - Lie Algebra of the Lorentz Group]], [[Def - Generators and Structure Constants]]).

- [[Ex - The rotation generators act as the cross product]] (⭐) — show $J_i$ acts as $\mathbf{e}_i \times$ on the spatial part, identify the rotation block as $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$ via the hat map, and connect to the angular-momentum algebra in its Poisson and quantum forms ([[Def - Lie Algebra of the Lorentz Group]], [[Def - Generators and Structure Constants]]).

- [[Ex - Writing a general so(1,3) element from its six parameters]] (⭐) — assemble the general generator with boost rapidities in the time row and rotation angles in the spatial block, verify $\eta\,\omega$ is antisymmetric, count the six independent components, and check $\mathrm{tr}\,\omega = 0$ so that $\det\exp(\omega) = 1$ ([[Def - Lie Algebra of the Lorentz Group]], [[Def - Infinitesimal Lorentz Transformations]]).
