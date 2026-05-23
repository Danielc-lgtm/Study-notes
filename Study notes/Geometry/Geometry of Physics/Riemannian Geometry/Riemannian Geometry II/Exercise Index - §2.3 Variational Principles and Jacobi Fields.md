---
type: exercise-index
subject: riemannian-geometry
section: "2.3"
tags: [geometry, riemannian-geometry, variational-calculus, jacobi-fields, exercise-index]
---

## §2.3 Variational Principles and Jacobi Fields — Exercises

This section drills the second-derivative calculus of the length and energy functionals — the **index form**, its kernel (Jacobi fields vanishing at the endpoints), and its sign (positive vs negative vs zero) which determines whether a geodesic is a local minimiser, saddle, or non-minimum. The unifying principle is the **Morse Index Theorem**: the index of $I$ on a geodesic arc equals the number of interior conjugate points counted with multiplicity. This converts a *spectral* question (eigenvalues of the Jacobi operator) into a *geometric counting* question (conjugate points), and is the prototype of all subsequent Morse-theoretic counting in differential geometry. The exercises here compute the index form explicitly on the simplest concrete cases (sphere [[Def - Geodesic|geodesics]]) and identify the kernel as the sinusoidal Jacobi fields.

- [[Ex - Jacobi Fields on a Sphere are Sinusoidal]] (⭐⭐) — solving the Jacobi equation $J'' + R(J, T)T = 0$ on $S^n$ in a parallel frame, reducing to $f'' + f = 0$ with sinusoidal solutions ([[Def - Jacobi Field]], [[Ex - Great Circles are the Geodesics of the Sphere]], [[Thm - Jacobi Equation and Conjugate Points]])

- [[Ex - Conjugate Points on the Round Sphere are Antipodal]] (⭐⭐) — identifying conjugate points as zeros of the sinusoidal Jacobi field; concluding that the conjugate locus along any geodesic from $p$ is the periodic set $\{(-1)^k p\}$ for $k \in \mathbb{Z}^+$, each with multiplicity $n - 1$ ([[Def - Conjugate Point]], [[Def - Jacobi Field]], [[Ex - Jacobi Fields on a Sphere are Sinusoidal]], [[Thm - Jacobi Equation and Conjugate Points]])

- [[Ex - Computing the Index Form for a Pole-to-Pole Geodesic on S^2]] (⭐⭐⭐) — direct computation of $I(V, V)$ on $S^2$ for the half-great-circle, evaluation on the Fourier basis $\sin(kt)$, identification of the kernel ($k = 1$) and the positive directions ($k \geq 2$); interpretation as "minimising but not strictly so" ([[Def - The Index Form]], [[Ex - Jacobi Fields on a Sphere are Sinusoidal]], [[Ex - Conjugate Points on the Round Sphere are Antipodal]], [[Thm - Second Variation of Arc Length]])
