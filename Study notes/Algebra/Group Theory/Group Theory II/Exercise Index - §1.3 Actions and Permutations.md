---
type: exercise-index
subject: group-theory
section: "1.3"
tags: [algebra, group-theory]
---

## §1.3 Actions and Permutations — Exercises

The exercises of §1.3 drill the orbit-stabiliser theorem and the action-as-homomorphism correspondence. Each exercise illustrates a recurring move: count a group order by acting on a natural feature set (cube rotations), force normality by a coset action into $S_p$ (smallest prime index), identify normalisers as stabilisers of the conjugation action, and prove Cauchy's theorem by McKay's cyclic-rotation argument. The unifying technique is the same — "to count or constrain a group, find the right action."

- [[Ex - Counting the rotations of the cube]] (⭐) — counts the order of a geometric symmetry group by acting on a concrete feature set (faces) and reading off orbit and stabiliser sizes; cross-checked via vertices and edges, with the action on long diagonals identifying the group as $S_4$ ([[Def - Group Action]], [[Def - Orbit and Stabiliser]], [[Def - Subgroup]], [[Def - Isomorphism]], [[Thm - Orbit-Stabiliser Theorem]], [[Thm - Actions Correspond to Homomorphisms]])
- [[Ex - Subgroups of smallest prime index are normal]] (⭐⭐) — proves normality of a subgroup of smallest-prime index by the coset action into $S_p$, squeezing the index $|H:K|$ between $(p-1)!$ and $|G|$ until the minimality of $p$ forces it to $1$ ([[Def - Group Action]], [[Def - Coset]], [[Def - Normal Subgroup]], [[Def - Homomorphism]], [[Def - Kernel and Image]], [[Thm - Coset Action and the Normal Core]], [[Thm - Actions Correspond to Homomorphisms]], [[Thm - Orbit-Stabiliser Theorem]], [[Thm - Lagrange's Theorem]], [[Thm - First Isomorphism Theorem]])
- [[Ex - Conjugation of subgroups and the number of conjugates]] (⭐⭐) — verifies that $G$ acts on its set of subgroups by conjugation, identifies the stabiliser of $H$ as the normaliser $N_G(H)$ straight from the definition, and counts conjugate subgroups as $|G:N_G(H)|$ by orbit-stabiliser ([[Def - Group Action]], [[Def - Subgroup]], [[Def - Orbit and Stabiliser]], [[Def - Normaliser]], [[Def - Normal Subgroup]], [[Def - Isomorphism]], [[Def - Centraliser and Centre]], [[Thm - Orbit-Stabiliser Theorem]])
- [[Ex - Cauchy's theorem via a cyclic action]] (⭐⭐⭐) — proves Cauchy's theorem by McKay's method: a $\mathbb{Z}/p$-action rotating the coordinates of $p$-tuples with product $e$, whose fixed points are constant tuples $(g,\dots,g)$ with $g^p=e$, counted modulo $p$ to force a non-trivial element of order $p$ ([[Def - Group Action]], [[Def - Orbit and Stabiliser]], [[Thm - Orbit-Stabiliser Theorem]], [[Thm - Lagrange's Theorem]])