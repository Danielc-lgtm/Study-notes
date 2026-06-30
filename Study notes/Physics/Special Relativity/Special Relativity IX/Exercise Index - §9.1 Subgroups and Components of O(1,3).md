---
type: exercise-index
subject: special-relativity
section: "9.1"
tags: [physics, special-relativity]
---

## §9.1 Subgroups and Components of O(1,3) — Exercises

The exercises of §9.1 drill the coarse anatomy of the Lorentz group: its four connected components, the subgroups cut out by the two locally-constant signs $\det\Lambda = \pm 1$ and $\mathrm{sgn}\,\Lambda^0{}_0 = \pm 1$, and the discrete reflections that move between components. The unifying instrument is a *closure check on the defining data*: a set of Lorentz transformations is a subgroup exactly when products and inverses preserve whatever signs or inequalities define it, and the restricted group $SO^+(1,3)$ is the $(\det = +1,\ \Lambda^0{}_0 \ge 1)$ piece — the connected component of the identity, the only piece reachable by a continuous physical process. The reflections $I = -\mathrm{Id}$ (spacetime inversion), $P$ (parity), $T$ (time reversal) generate the quotient $O(1,3)/SO^+(1,3) \cong \mathbb{Z}/2\times\mathbb{Z}/2$ (the Klein four-group), and reduce any transformation to a restricted one. The recurring technical fact is the reversed Cauchy–Schwarz inequality for future-timelike vectors, which supplies the sign-of-the-time-component bookkeeping that makes the orthochronous condition multiplicative.

- [[Ex - Proving the restricted Lorentz group is a subgroup]] — verify directly from the defining relation $\Lambda^{\mathsf T}\eta\Lambda = \eta$ that $SO^+(1,3)$ is closed under products and inverses and contains the identity, using $(\det\Lambda)^2 = 1$ for the determinant and the reversed Cauchy–Schwarz inequality $\Lambda^0{}_0\Lambda'^0{}_0 \le (\Lambda\Lambda')^0{}_0$ to show the orthochronous condition $\Lambda^0{}_0 \ge 1$ survives composition (⭐⭐) ([[Def - Subgroups and Components of the Lorentz Group]], [[Thm - The Restricted Lorentz Group is a Normal Subgroup]], [[Def - The Lorentz Group]]).

- [[Ex - Reducing any Lorentz transformation to a restricted one]] — read the component of an arbitrary $\Lambda \in O(1,3)$ from the sign pair $(\mathrm{sgn}\det\Lambda, \mathrm{sgn}\,\Lambda^0{}_0)$, then exhibit it as exactly one of $\Lambda_0$, $I\Lambda_0$, $P\Lambda_0$, $T\Lambda_0$ with $\Lambda_0 \in SO^+(1,3)$, making the reduction-by-reflection explicit and showing the reflection is forced by the two signs (⭐⭐) ([[Def - Subgroups and Components of the Lorentz Group]], [[Thm - The Restricted Lorentz Group is a Normal Subgroup]], [[Def - The Lorentz Group]]).

- [[Ex - The discrete reflections form the Klein four-group]] — show $\{\mathrm{Id}, I, P, T\}$ is closed under composition with $I = PT = TP$, that each element is its own inverse, hence the group is isomorphic to $\mathbb{Z}/2\times\mathbb{Z}/2$, and identify it with the quotient $O(1,3)/SO^+(1,3)$ via the two sign homomorphisms (⭐⭐) ([[Def - Subgroups and Components of the Lorentz Group]], [[Thm - The Restricted Lorentz Group is a Normal Subgroup]]).
