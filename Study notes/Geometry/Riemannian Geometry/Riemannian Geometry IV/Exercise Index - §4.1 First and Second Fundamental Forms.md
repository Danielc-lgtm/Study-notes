---
type: exercise-index
subject: riemannian-geometry
section: "4.1"
tags: [geometry, riemannian-geometry, surfaces, fundamental-forms]
---

## §4.1 First and Second Fundamental Forms — Exercises

This section drills the core computational mechanic of classical surface theory: given an explicit parametrisation $\mathbf{x}(u, v)$ of a surface in $\mathbb{R}^3$, compute the first fundamental form (metric components $E, F, G$ from inner products of tangent vectors) and the second fundamental form (components $e, f, g_\mathrm{II}$ from inner products of second derivatives with the unit normal). The technique is mechanical — six computations in roughly the same form for any surface — but the recurring patterns (rotational symmetry simplifying $F = 0$; convenient choices of unit normal; the special structure of ruled surfaces and surfaces of revolution) reward practice. The exercises here calibrate one's intuition on a few key examples (sphere, ellipsoid, torus, graph of a function) before moving on to curvature invariants in §4.2.

- [[Ex - Gauss Curvature of the Sphere of Radius R is 1 over R Squared]] (⭐) — computing $\mathrm{I}$, $\mathrm{II}$, and $K = 1/a^2$ on the sphere via spherical coordinates (the prototype computation; uses [[Def - First Fundamental Form]], [[Def - Second Fundamental Form]], [[Def - Gauss Curvature and Mean Curvature]])

- **Practice problem 1:** Compute the first and second fundamental forms of the **torus of revolution** $\mathbf{x}(u, v) = ((R + r\cos v)\cos u, (R + r\cos v)\sin u, r\sin v)$ (major radius $R$, minor radius $r$), and verify that $K(v) = \cos v/(r(R + r\cos v))$, which has sign equal to the sign of $\cos v$ — positive on the outer half ($v \in (-\pi/2, \pi/2)$), negative on the inner half. ⭐⭐. Uses [[Def - First Fundamental Form]], [[Def - Second Fundamental Form]], [[Def - Gauss Curvature and Mean Curvature]].

- **Practice problem 2 (Frankel 8.1(2)):** A **loxodrome** on a sphere of radius $a$ is a curve making a constant angle $\omega$ with each meridian of longitude. Using the first fundamental form $\mathrm{I} = a^2(d\theta^2 + \sin^2\theta\, d\varphi^2)$ on $S^2_a$, compute the arc length of the loxodrome from one pole to the other. ⭐⭐. Uses [[Def - First Fundamental Form]].

- **Practice problem 3 (Frankel 8.1(4)–8.1(5)):** Consider the graph $z = x^2 - 2y^2$ near the origin. With $u = x, v = y$ as coordinates, compute the matrices $(g_{\alpha\beta})$ and $(b^\alpha_{\;\beta})$ at the origin (where the tangent plane is the $xy$-plane). Use the result to show that near $p_0 = 0$, the surface is given approximately by $z = \tfrac{1}{2}b_{\alpha\beta}(0)x^\alpha x^\beta$ — a geometric interpretation of the second fundamental form as the Hessian of the "height-over-tangent-plane" function in Monge coordinates. ⭐. Uses [[Def - First Fundamental Form]], [[Def - Second Fundamental Form]].

- **Practice problem 4:** Compute the first fundamental form of the **catenoid** $\mathbf{x}(u, v) = (a\cosh(v/a)\cos u, a\cosh(v/a)\sin u, v)$, and show it is **conformally flat** in $(u, v)$ coordinates: $\mathrm{I} = \cosh^2(v/a)\bigl(a^2\, du^2 + dv^2\bigr)$, which is a conformal multiple of the Euclidean metric on the cylinder. Conclude that the catenoid is *intrinsically* a "stretched cylinder" with conformal factor $\cosh^2$. ⭐⭐. Uses [[Def - First Fundamental Form]]; preview for [[Ex - The Catenoid is a Minimal Surface]].
