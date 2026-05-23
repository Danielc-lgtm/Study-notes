---
type: exercise-index
subject: riemannian-geometry
section: "4.2"
tags: [geometry, riemannian-geometry, surfaces, curvature, principal-curvatures]
---

## §4.2 Gauss and Mean Curvatures — Exercises

This section drills the invariants of the shape operator $S$: the Gauss curvature $K = \det S = \kappa_1\kappa_2$ and the mean curvature $H = \mathrm{tr}\, S = \kappa_1 + \kappa_2$ (Frankel convention), as well as the principal curvatures $\kappa_1, \kappa_2$ and principal directions (eigenstructure of $S$). The exercises calibrate intuition for the sign of $K$ (elliptic / hyperbolic / parabolic / planar local shape), for the use of Euler's formula $\kappa(\theta) = \kappa_1\cos^2\theta + \kappa_2\sin^2\theta$ to compute normal curvature in arbitrary directions, and for the special features of constant-curvature surfaces (sphere $K = +$ const, pseudosphere $K = -$ const, plane $K = 0$).

- [[Ex - Gauss Curvature of the Pseudosphere is -1]] (⭐⭐) — computing $K = -1/a^2$ for the surface of revolution of the tractrix; the prototype of constant negative curvature (uses [[Def - Gauss Curvature and Mean Curvature]], [[Def - First Fundamental Form]], [[Def - Second Fundamental Form]])

- **Practice problem 1 (Frankel 8.2(2)–8.2(3)):** For the surface $z = x^2 - 2y^2$ near the origin, compute the Gauss curvature $K$ and mean curvature $H$ at the origin. Show that the origin is a hyperbolic point ($K < 0$) and find the asymptotic directions (where $\mathrm{II}(T, T) = 0$). Also compute the normal curvature in the direction $y = x$ at the origin using Euler's formula. ⭐. Uses [[Def - Gauss Curvature and Mean Curvature]], [[Def - Principal Curvatures and Directions]].

- **Practice problem 2:** Show that the **ellipsoid** $x^2/a^2 + y^2/b^2 + z^2/c^2 = 1$ has umbilic points (where $\kappa_1 = \kappa_2$). For the case $a > b > c > 0$, there are exactly $4$ umbilic points, lying in the plane of the "middle" axis ($y = 0$ plane in the convention $a > b > c$). Compute their locations explicitly. ⭐⭐⭐. Uses [[Def - Principal Curvatures and Directions]], [[Def - Gauss Curvature and Mean Curvature]].

- **Practice problem 3:** For the **catenoid** $\mathbf{x}(u, v) = (a\cosh(v/a)\cos u, a\cosh(v/a)\sin u, v)$, compute the Gauss curvature $K(v) = -1/(a^2\cosh^4(v/a))$ directly via the determinant formula and verify it is negative everywhere, with maximum (least negative) at $v = 0$ and decaying exponentially. ⭐⭐. Uses [[Def - Gauss Curvature and Mean Curvature]], [[Def - First Fundamental Form]]; preview for [[Ex - The Catenoid is a Minimal Surface]].

- **Practice problem 4 (Frankel 8.2(5)):** For a surface in graph form $z = f(x, y)$ over the $xy$-plane, derive the compact formulae
$$
K = \frac{f_{xx}f_{yy} - f_{xy}^2}{(1 + f_x^2 + f_y^2)^2}, \quad H = \frac{(1 + f_y^2)f_{xx} - 2f_xf_yf_{xy} + (1 + f_x^2)f_{yy}}{(1 + f_x^2 + f_y^2)^{3/2}}.
$$
These are the universal formulae for graph-of-function surfaces, useful for the minimal surface equation $H = 0$. ⭐⭐. Uses [[Def - Gauss Curvature and Mean Curvature]].

- **Practice problem 5:** A surface in $\mathbb{R}^3$ has all points umbilic ($\kappa_1 = \kappa_2$ everywhere). Use the Codazzi equations ([[Thm - Equations of Gauss and Codazzi]]) to show that the surface is contained in a plane (if the common $\kappa = 0$) or a sphere (if $\kappa = c \neq 0$, the sphere of radius $1/|c|$). This is the local **Hilbert–Liebmann theorem** for umbilic surfaces. ⭐⭐⭐. Uses [[Thm - Equations of Gauss and Codazzi]], [[Def - Principal Curvatures and Directions]].
