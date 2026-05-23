---
type: exercise-index
subject: riemannian-geometry
section: "4.3"
tags: [geometry, riemannian-geometry, surfaces, theorema-egregium, gauss-bonnet, topology]
---

## §4.3 Theorema Egregium and Gauss-Bonnet — Exercises

This section drills the global-topological content of surface curvature: the intrinsic nature of $K$ (Theorema Egregium), the Gauss–Bonnet formula $\int K\, dA = 2\pi\chi(M)$, the Brouwer degree of the Gauss normal map, and the precursor of Gauss–Bonnet via the holonomy of parallel transport. The exercises move from local-to-global, calibrating intuition for the surface-level intrinsic / extrinsic split, and culminating in the topological obstruction "the integrated $K$ on a closed surface is locked by its genus".

- [[Ex - Total Curvature of a Closed Surface via Gauss-Bonnet]] (⭐⭐) — applying Gauss–Bonnet to compute $\int K\, dA$ on the sphere ($4\pi$), torus ($0$), and genus-$g$ surface ($4\pi(1-g)$), with the deformation-invariance corollary (uses [[Thm - Gauss-Bonnet Theorem for Surfaces]], [[Def - Gauss Curvature and Mean Curvature]])

- [[Ex - Holonomy around a Spherical Cap is the Solid Angle]] (⭐⭐) — computing the parallel-transport holonomy around a spherical cap and verifying it equals the cap's solid angle $\Omega = 2\pi(1 - \cos\theta_0) = \int K\, dA$ (uses [[Def - Geodesic Curvature]], [[Thm - Gauss-Bonnet Theorem for Surfaces]])

- **Practice problem 1 (Frankel 8.5(2)):** Compute the Gauss curvature of the unit sphere using only the intrinsic formula $K = R_{1212}/\det g$, without reference to the embedding. Start from $\mathrm{I} = d\theta^2 + \sin^2\theta\, d\varphi^2$, compute the Christoffel symbols, then $R^\theta_{\;\varphi\theta\varphi} = \sin^2\theta$, and verify $K = 1$ — Theorema Egregium in action. ⭐⭐. Uses [[Thm - Theorema Egregium of Gauss]], [[Def - First Fundamental Form]].

- **Practice problem 2:** Derive the **spherical excess** formula. For a geodesic triangle on a unit sphere with vertices at angles $A, B, C$ at corners, the area of the triangle equals $A + B + C - \pi$. Use the boundary-corrected Gauss–Bonnet formula: $\int K\, dA + \int_{\partial T}\kappa_g\, ds + \sum\alpha_i = 2\pi$, with $\kappa_g = 0$ on geodesic sides and exterior angles $\pi - A, \pi - B, \pi - C$ at the corners. Conclude $\mathrm{Area} = A + B + C - \pi$. ⭐⭐. Uses [[Thm - Gauss-Bonnet Theorem for Surfaces]], [[Def - Geodesic Curvature]].

- **Practice problem 3 (Frankel 8.3(2)–8.3(4)):** Compute the Brouwer degree of a polynomial map $P : \mathbb{CP}^1 \to \mathbb{CP}^1$, $P(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_0$, by deforming $P$ to $z \mapsto z^n$ via the linear interpolation $z \mapsto z^n + t(a_{n-1}z^{n-1} + \cdots + a_0)$. Conclude $\deg(P) = n$, hence the **fundamental theorem of algebra**: any nonconstant polynomial has a root. ⭐⭐. Uses [[Def - Brouwer Degree of a Map]], [[Thm - Brouwer Degree is a Homotopy Invariant]].

- **Practice problem 4:** Show that on a closed orientable surface of genus $g \geq 1$, no Riemannian metric can have everywhere positive Gauss curvature. (Hint: $\int K\, dA = 2\pi\chi = 2\pi(2 - 2g) \leq 0$ for $g \geq 1$.) Conversely, the sphere admits metrics of constant positive curvature, the torus admits flat metrics (and only flat — modulo conformal changes), and higher-genus surfaces admit metrics of constant negative curvature. This is the rough form of the **uniformisation theorem**. ⭐⭐⭐. Uses [[Thm - Gauss-Bonnet Theorem for Surfaces]].

- **Practice problem 5 (Frankel 8.3(7)):** Verify the genus formula $\int_M K\, dA = 4\pi(1 - g)$ for a surface of genus $g$ embedded in $\mathbb{R}^3$, by counting the signed sheets covered by the Gauss map $N : M \to S^2$. The "outer" regions of the surface contribute positively to $\deg(N)$; the "saddle" regions inside the handle holes contribute negatively. ⭐⭐. Uses [[Thm - The Gauss Normal Map has Degree Half the Euler Characteristic]], [[Def - Gauss Normal Map]].
