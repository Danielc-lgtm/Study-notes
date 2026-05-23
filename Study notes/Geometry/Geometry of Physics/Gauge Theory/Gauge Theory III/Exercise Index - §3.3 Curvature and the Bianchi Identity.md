---
type: exercise-index
subject: gauge-theory
section: "3.3"
tags: [geometry, gauge-theory, curvature, bianchi]
---

## §3.3 Curvature and the Bianchi Identity — Exercises

This section defines the **curvature 2-form** $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$ of a principal connection and derives its central properties: horizontality, equivariance, descent to a section of the adjoint bundle, and the **Bianchi identity** $d_\omega\Omega = 0$. The exercises drill the *computation* of curvature in components (especially the non-abelian self-coupling term $\varepsilon^a{}_{bc}A^bA^c$ that distinguishes non-abelian from abelian gauge theory), the *gauge covariance* of the field strength ($F$ transforms in the adjoint representation, with the inhomogeneous gauge term cancelling), and the *abelian Bianchi identity* $dF = 0$ — the geometric half of Maxwell's equations. The point of the section is to distinguish *kinematic* (geometric, automatic) identities — structural equation, Bianchi — from *dynamical* equations like Yang-Mills.

- [[Ex - Computing the Curvature in Two Different Gauges]] (⭐⭐) — non-abelian $SU(2)$ field strength $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + \varepsilon^a{}_{bc}A^b_\mu A^c_\nu$ in components, finite gauge transformation by $g(x) = e^{i\sigma_3\chi(x)/2}$, and verification that $F$ transforms in the adjoint representation while $A$ transforms inhomogeneously ([[Thm - Cartan Structural Equation for Principal Connections]], [[Thm - Gauge Transformation Law for Local Connection 1-Forms]], [[Def - Curvature 2-Form on a Principal Bundle]])

- [[Ex - Bianchi Identity for the Electromagnetic Field is dF = 0]] (⭐) — abelian special case of the Bianchi identity $d_\omega F = 0$ reduces to $dF = 0$; expansion in Minkowski-space components gives the magnetic Gauss law $\nabla \cdot \mathbf{B} = 0$ and Faraday's law of induction $\nabla \times \mathbf{E} + \partial_t\mathbf{B} = 0$ — the geometric half of Maxwell's equations ([[Thm - Bianchi Identity for Principal Connections]], [[Def - Curvature 2-Form on a Principal Bundle]], [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]])

- [[Ex - Adjoint Bundle of a U(1)-Bundle is Trivial]] (⭐) — for an abelian structure group, the adjoint action is trivial and $\mathrm{Ad}\,P = M \times \mathfrak{u}(1)$ is the trivial line bundle; consequence: the electromagnetic field strength is a globally defined ordinary 2-form on $M$, independent of gauge choice — contrasting with the non-abelian case where $\mathrm{Ad}\,P$ is generically non-trivial ([[Def - Adjoint Bundle]], [[Def - Adjoint Representation]], [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]])

- [[Ex - The Affine Space of Connections on a Principal Bundle]] (⭐⭐⭐) — the curvature expansion $F_{\omega_0 + \pi^*\eta} = F_{\omega_0} + d_{\omega_0}\eta + \tfrac{1}{2}[\eta, \eta]$ around a reference connection $\omega_0$; the linear term involves the exterior covariant derivative $d_{\omega_0}$, the quadratic term is the self-bracket — central to perturbative Yang-Mills and instanton moduli theory ([[Thm - Cartan Structural Equation for Principal Connections]], [[Def - Exterior Covariant Derivative on Associated Bundles]], [[Def - Adjoint Bundle]])
