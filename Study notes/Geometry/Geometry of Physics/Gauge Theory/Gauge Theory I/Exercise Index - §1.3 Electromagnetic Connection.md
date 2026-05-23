---
type: exercise-index
subject: gauge-theory
section: "1.3"
tags: [geometry, gauge-theory, electromagnetism, U(1)]
---

## §1.3 Electromagnetic Connection — Exercises

This section drills the *dictionary* between classical electromagnetism (vector potential $A$, field strength $F = dA$) and gauge-theoretic geometry ($U(1)$-connection $\omega = -(ie/\hbar)A$, curvature $\theta = -(ie/\hbar)F$). The central technique is the **minimal-coupling prescription** $\partial_\mu \to \partial_\mu - (ie/\hbar)A_\mu$, which converts any free-field equation into its EM-coupled version. The exercises verify gauge invariance both directly (by algebra) and geometrically (via covariance of the covariant derivative), and they connect to the wider story by formulating Maxwell's equations as differential-form identities.

- [[Ex - Gauge-Invariant Coupling of Schrödinger to EM Field]] (⭐⭐) — Derives Schrödinger's equation in an EM field via minimal coupling, verifies invariance under the joint transformation $(\psi, A, \varphi) \to (e^{(ie/\hbar)f}\psi, A + \nabla f, \varphi - \partial_t f)$, and reinterprets the result as $\nabla$-covariance of the free Schrödinger equation in a $U(1)$-bundle ([[Def - U(1) Gauge Field and Electromagnetic Connection]], [[Def - Gauge Transformation]], [[Def - Connection on a Vector Bundle]])
- [[Ex - Maxwell's Equations as Two Form Equations on Minkowski Space]] (⭐⭐) — *Supplementary, from [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].* Rewrites Maxwell's equations in differential-form language as $dF = 0$ (homogeneous, $=$ Bianchi identity for the $U(1)$-connection) and $d \star F = J$ (inhomogeneous, $=$ dynamical equation). The first equation is automatic from $F = dA$; the second is the Yang-Mills equation specialized to the abelian $U(1)$ case ([[Def - Differential k-Form on a Manifold]], [[Def - Exterior Derivative on a Manifold]], [[Def - Closed and Exact Forms]])
- [[Ex - A Form that is Closed but Not Exact on the Punctured Plane]] (⭐⭐) — *Supplementary, from [[Differential Geometry VIII — Differential Forms]].* The standard example: $\omega = d\phi$ on $\mathbb{R}^2 \setminus \{0\}$ is closed but not exact, generating $H^1(\mathbb{R}^2 \setminus \{0\}, \mathbb{R}) = \mathbb{R}$. This is the topological obstruction that *forces* the Aharonov-Bohm phase to be non-trivial in §1.4 — without the non-triviality of $H^1$ on non-simply-connected configuration spaces, the AB effect would not exist ([[Def - Closed and Exact Forms]], [[Def - de Rham Cohomology]])
