---
type: exercise-index
subject: riemannian-geometry
section: "4.4"
tags: [geometry, riemannian-geometry, surfaces, vector-fields, minimal-surfaces, topology]
---

## §4.4 Vector Fields and Topology of Surfaces — Exercises

This section drills the connection between **vector fields on surfaces** and their **topology**, through the Poincaré–Hopf theorem (sum of vector-field indices = Euler characteristic), as well as the variational characterisation of **minimal surfaces** ($H = 0$ as critical points of area). The exercises cover the prototypical minimal surfaces (catenoid, helicoid) and the simplest topological obstruction (hairy ball theorem on $S^2$), giving complementary views of how local geometric data assembles into global topological information.

- [[Ex - The Catenoid is a Minimal Surface]] (⭐) — direct verification that the catenoid $\mathbf{x}(u, v) = (a\cosh(v/a)\cos u, a\cosh(v/a)\sin u, v)$ has $H = 0$, the prototype embedded minimal surface (uses [[Def - Minimal Surface]], [[Def - Gauss Curvature and Mean Curvature]])

- [[Ex - The Helicoid is Minimal]] (⭐⭐) — verification that the helicoid $\mathbf{x}(u, v) = (v\cos u, v\sin u, au)$ has $H = 0$, the unique nonplanar ruled minimal surface and Bonnet conjugate of the catenoid (uses [[Def - Minimal Surface]], [[Def - Second Fundamental Form]])

- [[Ex - Hairy Ball Theorem from Poincare-Hopf]] (⭐⭐) — using Poincaré–Hopf to derive $\chi(S^2) = 2$ and conclude that no nowhere-vanishing tangent vector field exists on $S^2$ (uses [[Thm - Poincare-Hopf Theorem for Surfaces]], [[Def - Kronecker Index of a Vector Field]])

- **Practice problem 1:** Show that the **flat torus** $T^2 = \mathbb{R}^2/\mathbb{Z}^2$ admits a nowhere-vanishing tangent vector field — namely, any constant translation field $v = (\alpha, \beta)$ for $(\alpha, \beta) \neq 0$. Confirm consistency with Poincaré–Hopf: $\chi(T^2) = 0$, so the index sum is zero, achieved by the empty zero set. ⭐. Uses [[Thm - Poincare-Hopf Theorem for Surfaces]], [[Def - Vector Field on a Manifold]].

- **Practice problem 2 (Frankel 8.4(1)):** Schwarz's area formula. Let $M$ be a minimal surface in $\mathbb{R}^3$ with boundary curve $C = \partial M$, and consider the dilation variation $\mathbf{x}_t = (1 + t)\mathbf{x}$ moving every point radially outward. (a) Show that $A(t) = (1 + t)^2 A(0)$. (b) Show that $2A(0) = \int_C\det(N, \mathbf{x}, d\mathbf{x})$ — the area of the minimal surface depends only on the boundary data $(N, \mathbf{x})$ restricted to $C$. This is **Schwarz's formula** and has the striking consequence that the area of any minimal surface spanning $C$ is determined entirely by boundary data (the normal field values at the boundary). ⭐⭐⭐. Uses [[Thm - First Variation of Area]], [[Def - Minimal Surface]].

- **Practice problem 3 (Morse theory of the height function on the torus):** Embed the torus $T^2$ in $\mathbb{R}^3$ as a doughnut, and use the height function $f(p) = p_z$ as a Morse function. Identify the $4$ critical points (1 minimum at the bottom, 2 saddles in the middle, 1 maximum at the top) and compute the Poincaré–Hopf indices ($+1, -1, -1, +1$). Verify the index sum equals $\chi(T^2) = 0$, consistent with the torus admitting nowhere-vanishing tangent fields. ⭐⭐. Uses [[Thm - Poincare-Hopf Theorem for Surfaces]], [[Def - Kronecker Index of a Vector Field]].

- **Practice problem 4:** Show that the **Möbius strip** does *not* admit a Gauss normal map globally (because it is non-orientable), but does admit one locally on each chart. Conclude that classical surface theory (including Theorema Egregium, Gauss–Bonnet in standard form, and the second fundamental form) applies to the Möbius strip only in modified or local form. ⭐⭐. Uses [[Def - Gauss Normal Map]], [[Def - Orientation of a Smooth Manifold]].
