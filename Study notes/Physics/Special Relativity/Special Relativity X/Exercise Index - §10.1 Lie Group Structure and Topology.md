---
type: exercise-index
subject: special-relativity
section: "10.1"
tags: [physics, special-relativity, lie-groups]
---

## §10.1 Lie Group Structure and Topology — Exercises

The exercises of §10.1 establish the Lorentz group as a Lie group and probe its global shape. The first drills the linearisation that produces the Lie algebra — substitute $\Lambda = \mathrm{Id} + \varepsilon\,\omega$ into the defining equation and extract the generator condition $\omega^{\mathsf T}\eta + \eta\,\omega = 0$, equivalently that $\omega_{\mu\nu}$ is antisymmetric once an index is lowered. The second and third turn to topology via the polar decomposition $SO^+(1,3) \cong \mathbb{R}^3 \times SO(3)$: the boost factor $\mathbb{R}^3$ is non-compact and contractible, so it carries the group's non-compactness but none of its fundamental group, while the rotation factor $SO(3) \cong \mathbb{R}\mathbb{P}^3$ is compact and carries the entire fundamental group $\mathbb{Z}/2$ — the topological existence theorem for spinors. The unifying observation: every global property of the Lorentz group is the corresponding property of one of its two factors, and the deepest of them, $\pi_1 = \mathbb{Z}/2$, is the belt trick of the rotation subgroup.

- [[Ex - Infinitesimal Lorentz transformations are eta-antisymmetric]] (⭐) — linearise the group's defining equation to derive the generator condition $\omega^{\mathsf T}\eta + \eta\,\omega = 0$, recognise it as antisymmetry of $\omega_{\mu\nu}$, deduce that boosts are symmetric and rotations antisymmetric matrices, and count the dimension six ([[Def - Infinitesimal Lorentz Transformations]], [[Def - The Lorentz Group]], [[Def - Lie Algebra of the Lorentz Group]]).

- [[Ex - The Lorentz group is non-compact but the rotation subgroup is compact]] (⭐⭐) — exhibit unbounded boosts to prove non-compactness, show $SO(3)$ is closed and bounded hence compact, localise the non-compactness to the $\mathbb{R}^3$ boost factor (with the velocity-versus-rapidity subtlety), and conclude there are no non-trivial finite-dimensional unitary representations ([[Thm - Topology of the Lorentz Group]], [[Def - Rapidity]], [[Def - The Lorentz Group]], [[Thm - Polar Decomposition of the Lorentz Group]]).

- [[Ex - The fundamental group of the restricted Lorentz group is Z mod 2]] (⭐⭐⭐) — reduce $\pi_1(SO^+(1,3))$ to $\pi_1(SO(3))$ via the product manifold, compute $\pi_1(SO(3)) = \mathbb{Z}/2$ from the $\mathbb{R}\mathbb{P}^3$ model and the belt-trick loop, identify the double cover $SL(2,\mathbb{C})$, and explain the spinor sign under $2\pi$ rotation ([[Thm - Topology of the Lorentz Group]], [[Thm - Polar Decomposition of the Lorentz Group]], [[Def - The Lorentz Group]], [[Def - The Spinor Map and SL(2,C)]]).
