---
type: exercise-index
subject: differential-geometry
section: "8.2"
tags: [geometry, differential-geometry]
---

## §8.2 Differential Forms on Manifolds — Exercises

This section's exercises drill the bundle and pointwise constructions of differential forms on a manifold: smooth sections of $\Lambda^k T^*M$, pullback along smooth maps (with the structural advantage over vector fields that pullback works without invertibility), and the algebraic operation of contraction with a vector field (interior product). The exercises train recognition of forms in concrete settings — the cotangent bundle's $1$-forms as covector fields, the standard volume form on $\mathbb{R}^n$, the angular form as a globally non-trivial section — and exercise the pullback formula via parametrizations and changes of coordinates.

- **Compute the pullback of $dx \wedge dy$ under the polar-coordinate map $F(r, \theta) = (r\cos\theta, r\sin\theta)$** (⭐) — verify $F^*(dx \wedge dy) = r\,dr \wedge d\theta$, matching the polar Jacobian determinant ([[Def - Pullback of a Differential Form on a Manifold]])
- **Pullback of a form along a curve gives the line integral** (⭐) — for a $1$-form $\omega$ on $M$ and a smooth curve $\gamma : [a, b] \to M$, show $\gamma^*\omega = \omega_\gamma(\dot\gamma)\,dt$ as a $1$-form on $[a, b]$, so $\int_\gamma\omega = \int_a^b \gamma^*\omega$ ([[Def - Pullback of a Differential Form on a Manifold]])
- **Compute $\iota_X\Omega$ for the standard volume form $\Omega = dx \wedge dy \wedge dz$ on $\mathbb{R}^3$ and a vector field $X = (P, Q, R)$** (⭐) — verify the answer is the flux form $P\,dy \wedge dz + Q\,dz \wedge dx + R\,dx \wedge dy$, the form whose surface integral computes the flux of $(P, Q, R)$ ([[Def - Interior Product (Contraction with a Vector Field)]])
- **Show that a $C^\infty(M)$-multilinear alternating map $\mathfrak{X}(M)^k \to C^\infty(M)$ is a differential $k$-form (tensor characterization)** (⭐⭐) — uses partition-of-unity localization to show $C^\infty(M)$-linearity implies pointwise dependence ([[Def - Differential k-Form on a Manifold]])
- **Construct the angular form as a section of $\Lambda^1 T^*(\mathbb{R}^2 \setminus \{0\})$ and verify smoothness** (⭐) — preliminary to the closed-not-exact computation, simply checking the coefficient functions are smooth on the punctured plane ([[Def - Differential k-Form on a Manifold]])
