# PAGE SPEC

- **Filename:** `Thm - The Top de Rham Cohomology of a Closed Connected Oriented Manifold is R.md`
- **Type:** theorem
- **Chapter:** Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles  (folder `Gauge Theory III/`)
- **Section:** §3.5 Smooth-Topological Tools — Generic Sections, Degree, and Homotopy Invariance of Bundles

## Spec (from the manifest)

type: theorem; source items: A-I3.1.3 (in its de Rham reading), needed for the degree; prereqs: [Def - de Rham Cohomology, Thm - Stokes' Theorem on Manifolds, Thm - Integration is Well-Defined on Oriented Manifolds, Thm - The Poincaré Lemma on a Star-Shaped Region, Thm - Existence of Smooth Partitions of Unity]; statement: If $N$ is a closed connected oriented $n$-manifold then $\int_N\colon H^n_{dR}(N)\to\mathbb R$ is an isomorphism; equivalently an $n$-form is exact iff its integral vanishes; proof: Lee ISM 2e Thm 17.31 and Lemma 17.27 (compactly supported Poincaré lemma on $\mathbb R^n$: a compactly supported $n$-form with integral zero is $d$ of a compactly supported $(n-1)$-form — proved by induction on $n$ using integration in the last variable) and the "chain of balls" lemma (every $n$-form is cohomologous to one supported in a given coordinate ball, using a partition of unity and connectedness); write all steps; reference: Lee ISM 2e Lemma 17.27, Thm 17.30, Thm 17.31; Bott–Tu Prop 4.7 / Thm 5.? (compactly supported version); spec: Bridges: Hodge I `Thm - Poincare Duality via Hodge Star` gives the same statement analytically; RG IV `Def - Brouwer Degree of a Map` asserts exactly this exactness. Targets: the degree; the integral of the Chern form over a surface as the only invariant (VI).
