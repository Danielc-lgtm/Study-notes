# PAGE SPEC

- **Filename:** `Thm - Dirac Operators are Formally Self-Adjoint.md`
- **Type:** theorem
- **Chapter:** Gauge Theory VIII — Clifford Algebras, Spin Structures, and Dirac Operators  (folder `Gauge Theory VIII/`)
- **Section:** §8.2 Dirac Bundles and Dirac Operators

## Spec (from the manifest)

type: theorem; source items: A-X4.2.1 (the exercise's content is this page's proof); prereqs: [Def - Spinor Bundle and Dirac Operator, Thm - Stokes' Theorem on Manifolds, Def - Riemannian Volume Form, Thm - Cartan's Magic Formula]; statement: For a Dirac bundle $E$ over a Riemannian manifold $M$ and $s_1,s_2\in\Gamma(E)$ with $s_1$ or $s_2$ compactly supported (in particular for all $s_1,s_2$ when $M$ is closed): $\int_M\langle Ds_1,s_2\rangle\,\mathrm{vol} = \int_M\langle s_1,Ds_2\rangle\,\mathrm{vol}$; more precisely the writer proves the pointwise identity $\langle Ds_1,s_2\rangle - \langle s_1,Ds_2\rangle = \operatorname{div}(V)$ for the vector field $V$ defined by $\langle V,X\rangle := -\langle X\cdot s_1,s_2\rangle$ (sign verified on the page), then integrates; proof: local orthonormal frame, skew-adjointness of Clifford multiplication (condition (2)), metric compatibility (1), compatibility (3) with $\nabla^{LC}e_i$, the divergence formula $\operatorname{div}V = \sum_i\langle\nabla_{e_i}V,e_i\rangle$ and $\int\operatorname{div}V\,\mathrm{vol} = 0$ for compactly supported $V$ (Lemma 1 via $\operatorname{div}V\,\mathrm{vol} = d(\iota_V\mathrm{vol})$ and Stokes; same lemma as in VII); spec: mechanism: **Clifford multiplication is skew-adjoint and the connection is metric, so the only non-symmetric term is a divergence**; targets: $\langle\slashed D^+\dot\psi,\phi\rangle = \langle\dot\psi,\slashed D^-\phi\rangle$ in XI; Weitzenböck integration; ellipticity plus self-adjointness gives $\operatorname{coker}D\cong\ker D$ in IX.
