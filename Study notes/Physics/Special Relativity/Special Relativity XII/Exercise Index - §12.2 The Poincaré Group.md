---
type: exercise-index
subject: special-relativity
section: "12.2"
tags: [physics, special-relativity]
---

## §12.2 The Poincaré Group — Exercises

The exercises of §12.2 drill the group structure of the Poincaré group, and all of them route through the single master object: the semidirect composition law $(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2, \Lambda_2) = (\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$. The first exercise derives this law from the affine action and reads off the identity, inverse, and associativity; the lone factor $\Lambda_1$ in front of $\boldsymbol{v}_2$ — the outer Lorentz part acting on the inner translation — is the source of everything that follows. The second exercise uses one conjugation to prove the translations a normal abelian subgroup, hence the group non-simple (in contrast to the simple restricted Lorentz group), and shows by contrast that the Lorentz subgroup is *not* normal — the asymmetry of the semidirect product. The third disentangles the active reading (move an event) from the passive reading (relabel a fixed event), which share a formula but oppose in meaning and are related by inversion. The fourth proves the structure is semidirect, not direct, by exhibiting a boost and a translation that fail to commute. The unifying theme: the semidirect twist is geometry, not convention — a boost re-expresses a translation in rotated axes — and every structural fact is one substitution into the composition law away.

- [[Ex - The semidirect product group law of the Poincaré group]] (⭐⭐) — compose two Poincaré transformations by applying the affine action twice, derive $(\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$, identify where $\Lambda_1$ enters, and extract the identity $(\boldsymbol{0}, \mathrm{Id})$, inverse $(-\Lambda^{-1}\boldsymbol{v}, \Lambda^{-1})$, and associativity ([[Def - The Poincaré Group]], [[Def - The Lorentz Group]]).

- [[Ex - Translations form a normal abelian subgroup]] (⭐⭐) — show the translations form an abelian subgroup isomorphic to (ℝ⁴, +), conjugate to find $(\boldsymbol{w}, \Lambda)(\boldsymbol{v}, \mathrm{Id})(\boldsymbol{w}, \Lambda)^{-1} = (\Lambda\boldsymbol{v}, \mathrm{Id})$ hence normality, conclude non-simplicity, and exhibit that the Lorentz subgroup is *not* normal ([[Def - The Poincaré Group]], [[Def - The Lorentz Group]]).

- [[Ex - Active versus passive Poincaré transformations]] (⭐⭐) — distinguish the passive coordinate change (relabel one event in two frames) from the active map (move one event in one frame), show their identical algebraic form and opposite meaning, exhibit the inverse-transpose relation between basis and component transformation, and demonstrate that a passive change to a frame moving at $v$ equals an active boost by $-v$ ([[Def - The Poincaré Group]], [[Def - The Lorentz Transformation]]).

- [[Ex - The Poincaré group is not a direct product]] (⭐⭐⭐) — show the direct-product law $(\boldsymbol{v}_1 + \boldsymbol{v}_2, \Lambda_1\Lambda_2)$ agrees with the actual law iff the Lorentz action is trivial, exhibit a boost with $\Lambda_1\boldsymbol{v}_2 \neq \boldsymbol{v}_2$, and prove boost and translation fail to commute — the geometric reason the semidirect twist is forced ([[Def - The Poincaré Group]], [[Def - The Lorentz Group]]).
