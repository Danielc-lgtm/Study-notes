---
type: exercise-index
subject: special-relativity
section: "19.1"
tags: [physics, special-relativity]
---

## §19.1 Arbitrary Coordinates and Tensor Fields — Exercises

The exercises of §19.1 drill the foundational operation of the chapter: turning a non-inertial coordinate system into a definite array of metric components, and reading off the coordinate basis and its dual. The recurring technique is the change-of-basis law $g_{\alpha\beta} = (\partial x'^\mu/\partial x^\alpha)(\partial x'^\nu/\partial x^\beta)g'_{\mu\nu}$ — get the Jacobian, sandwich the inertial metric, read off the result — and the recurring lesson is that a position-dependent or non-diagonal metric is a property of the *coordinates*, not of the *geometry*, which remains flat. Two structural facts get established here for use throughout: the coordinate basis is generically orthogonal but not orthonormal (so its non-unit lengths are the metric's content), and the gradients of the coordinates are exactly the dual basis, $e^\alpha = \mathbf{d}x^\alpha$, with scalar-field gradients having components equal to the partial derivatives. These are the inputs the covariant derivative and the exterior derivative will both consume.

- [[Ex - The metric and coordinate basis in rotating coordinates]] (⭐⭐) — transform the inertial metric through a co-rotating coordinate change to obtain the Langevin metric, read off the frame-dragging cross term $g_{(ct)\varphi}$ and the position-dependent $g_{(ct)(ct)}$ vanishing at the light cylinder, and recognise the spacetime as flat via the vanishing Riemann tensor ([[Def - Arbitrary Coordinates and the Coordinate Basis]]).

- [[Ex - The coordinate basis of spherical coordinates is orthogonal but not orthonormal]] (⭐) — compute the spherical coordinate basis vectors and metric $\mathrm{diag}(1,-1,-r^2,-r^2\sin^2\theta)$, show the basis is orthogonal but not orthonormal, and prove the orthonormal frame $\hat r,\hat\theta,\hat\varphi$ is not a coordinate basis because it has nonzero Lie brackets ([[Def - Arbitrary Coordinates and the Coordinate Basis]]).

- [[Ex - The gradient of a coordinate is the dual basis vector]] (⭐) — show $\langle\boldsymbol{\nabla}x^\alpha,\vec{e}_\beta\rangle = \delta^\alpha{}_\beta$ so that the coordinate gradients are the dual basis $e^\alpha = \mathbf{d}x^\alpha$, deduce that a scalar field's gradient has components $\nabla_\alpha f = \partial f/\partial x^\alpha$ with no Christoffel correction, and explain why the gradient is intrinsically a covector ([[Def - Arbitrary Coordinates and the Coordinate Basis]], [[Def - The Covariant Derivative]]).
