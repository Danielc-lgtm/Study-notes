---
type: exercise-index
subject: differential-geometry
section: "8.3"
tags: [geometry, differential-geometry]
---

## §8.3 The Exterior Derivative — Exercises

This section's exercises drill the central differential operator of the chapter: the exterior derivative $d$, its coordinate computation, the algebraic identities $d^2 = 0$ and $F^*d = dF^*$, and the closed-versus-exact dichotomy on different manifolds. The mechanical exercises (computing $d$ of specific forms, recovering grad-curl-div) train the bookkeeping; the conceptual exercises (closed-not-exact on the punctured plane) train the recognition of how topology enters the calculus.

- [[Ex - Computing the Exterior Derivative in Coordinates]] (⭐) — mechanical computation of $d\omega$ for several explicit forms on $\mathbb{R}^2$ and $\mathbb{R}^3$ ([[Def - Exterior Derivative on a Manifold]], [[Thm - Coordinate Expression for the Exterior Derivative]])
- [[Ex - The Exterior Derivative on R^3 Recovers Grad-Curl-Div]] (⭐⭐) — construct the commuting diagram between vector-calculus operators and the exterior derivative in degrees $0, 1, 2$, deriving $\operatorname{curl}\operatorname{grad} = 0$ and $\operatorname{div}\operatorname{curl} = 0$ from $d^2 = 0$ in one step ([[Def - Exterior Derivative on a Manifold]], [[Thm - d-Squared-is-Zero]], [[Thm - Wedge Product Properties]])
- [[Ex - A Form that is Closed but Not Exact on the Punctured Plane]] (⭐⭐⭐) — verify the angular form on $\mathbb{R}^2 \setminus \{0\}$ is closed by direct computation, compute its period $2\pi$ around the unit circle, conclude non-exactness via Stokes, and connect to $H^1_{dR}(\mathbb{R}^2 \setminus \{0\}) \cong \mathbb{R}$ ([[Def - Closed and Exact Forms]], [[Thm - d-Squared-is-Zero]], [[Thm - The General Stokes Theorem]])
- **Show $F^*(d\omega) = d(F^*\omega)$ directly on a basic $1$-form** (⭐⭐) — for $F : \mathbb{R}^2 \to \mathbb{R}$, $F(x, y) = x^2 - y^2$, and $\omega = z\,dz$ on $\mathbb{R}$, compute both sides of the naturality identity ([[Thm - Pullback Commutes with d for Forms on Manifolds]])
- **Verify $d^2 f = 0$ explicitly on $f(x, y, z) = xyz$ and identify the Schwarz cancellation** (⭐) — compute $df$, then $d(df)$, and identify exactly how the $\partial_i\partial_j f \,dx^i \wedge dx^j$ pairs cancel by Schwarz + anticommutativity ([[Thm - d-Squared-is-Zero]])
