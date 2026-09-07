---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Connection on a Vector Bundle"
  - "Def - Curvature of a Vector-Bundle Connection"
  - "Def - Levi-Civita Connection"
tags: [geometry, gauge-theory, curvature, sphere, Gauss-Bonnet]
---

# Prerequisite Concepts

- [[Def - Connection on a Vector Bundle]]
- [[Def - Curvature of a Vector-Bundle Connection]]
- [[Def - Levi-Civita Connection]]

# Problem Statement

On the unit round sphere use the oriented orthonormal coframe
$$\vartheta^1=d\theta,\qquad \vartheta^2=\sin\theta\,d\varphi.$$
Find the Levi–Civita connection matrix from Cartan's first structure equation, compute its curvature, and verify the Gauss–Bonnet integral.

# Convergent Strategy

Metric compatibility makes the matrix skew-symmetric, leaving one unknown form $\omega^1{}_2$. Torsion-freeness determines it from $d\vartheta^a+\omega^a{}_b\wedge\vartheta^b=0$.

# Solution

> [!proof]- Solution
> Since $d\vartheta^1=0$ and
> $$d\vartheta^2=\cos\theta,d\theta\wedge d\varphi
> =\cot\theta\,\vartheta^1\wedge\vartheta^2,$$
> the skew-symmetric matrix
> $$
> \omega=
> \begin{pmatrix}
> 0&-\cos\theta\,d\varphi\\
> \cos\theta\,d\varphi&0
> \end{pmatrix}
> $$
> satisfies both structure equations. Uniqueness of the torsion-free metric connection shows this is the Levi–Civita matrix on the coordinate patch.
>
> Because every matrix entry is a multiple of the same $1$-form $d\varphi$, $\omega\wedge\omega=0$. Hence
> $$
> \Omega=d\omega=
> \begin{pmatrix}
> 0&\sin\theta,d\theta\wedge d\varphi\\
> -\sin\theta,d\theta\wedge d\varphi&0
> \end{pmatrix}.
> $$
> Thus $\Omega^1{}_2=\vartheta^1\wedge\vartheta^2$, so the Gaussian curvature is $K=1$ in this orientation convention. Although the chosen frame is singular at the poles, the curvature form extends smoothly. Finally,
> $$
> \frac1{2\pi}\int_{S^2}\Omega^1{}_2
> =\frac1{2\pi}\int_0^{2\pi}\int_0^\pi\sin\theta\,d\theta,d\varphi
> =2=\chi(S^2).
> $$

# Key Takeaways

The connection matrix is local and frame-dependent; the curvature represents global geometry. On an oriented surface the structure group $SO(2)$ is abelian, so the curvature calculation resembles a $U(1)$ gauge field.
