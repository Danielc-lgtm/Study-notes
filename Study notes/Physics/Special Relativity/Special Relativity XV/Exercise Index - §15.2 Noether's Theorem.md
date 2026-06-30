---
type: exercise-index
subject: special-relativity
section: "15.2"
tags: [physics, special-relativity]
---

## §15.2 Noether's Theorem — Exercises

The exercises of §15.2 drill the conversion of symmetries into conservation laws via Noether's theorem for a relativistic particle. The recurring routine is the same in every case: identify a symmetry of the Lagrangian, read off its generator $G^\mu$, and write down the conserved charge $p_\mu G^\mu$ — with no equation of motion solved. The first exercise treats spacetime translations and obtains the conservation of four-momentum (energy from time translation, momentum from space translation), and dwells on why the conserved charge being a pairing $p_\mu G^\mu$ forces four-momentum to be a one-form. The second treats Lorentz transformations and obtains the angular-momentum tensor, splitting it into the angular momentum (rotations) and the centre-of-inertia theorem (boosts) — the surprising result that boost invariance is a dynamical statement about the centre of mass. The third treats cyclic coordinates of a particle in a field, where the conserved quantity is the *canonical* momentum including the field term, not the kinetic momentum. The unifying observation: the ten conservation laws of free relativistic motion are the Noether charges of the ten-parameter Poincaré group, and a field's conservation laws are the Noether charges of its symmetries.

- [[Ex - Four-momentum conservation from translation invariance]] (⭐⭐) — verify translation invariance of the free Lagrangian, apply Noether's theorem to conclude $p_\mu = mu_\mu$ is conserved, decompose into energy and three-momentum, and argue from the pairing $p_\mu G^\mu$ that four-momentum is fundamentally a one-form ([[Thm - Noether Theorem (Relativistic Particle)]], [[Def - Relativistic Action of a Free Particle]], [[Def - Four-Momentum and Rest Mass]], [[Def - The Poincaré Group]]).

- [[Ex - Angular momentum and the centre of inertia from Lorentz invariance]] (⭐⭐⭐) — write the Lorentz generator $G^\mu = \omega^\mu_{\;\nu}x^\nu$ with $\omega$ antisymmetric, use the antisymmetry to extract the conserved angular-momentum tensor $J^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu$, split into rotation charges (angular momentum) and boost charges (the centre-of-inertia theorem $x^i - (P^i/E)t = \text{const}$), and interpret why frame equivalence implies uniform centre-of-mass motion ([[Thm - Noether Theorem (Relativistic Particle)]], [[Def - Angular Momentum Four-Tensor]], [[Def - The Poincaré Group]], [[Def - Four-Momentum and Rest Mass]]).

- [[Ex - Conserved energy and momentum in a static field]] (⭐) — for a charged particle in a vector field, use cyclic coordinates of the potential (time-independence, spatial translation invariance, axial symmetry) to find the conserved canonical momenta $p_0$, $p_1$, $J_{xy}$, and contrast the conserved *canonical* momentum $mu_\mu + qA_\mu$ with the non-conserved *kinetic* momentum $mu_\mu$ ([[Thm - Noether Theorem (Relativistic Particle)]], [[Def - Lagrangian for a Particle in a Vector Field]], [[Def - Generalized Four-Momentum and the Relativistic Hamiltonian]]).
