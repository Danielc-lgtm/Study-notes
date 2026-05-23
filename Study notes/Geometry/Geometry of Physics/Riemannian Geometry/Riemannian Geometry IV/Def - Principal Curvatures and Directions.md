---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Shape Operator (Weingarten Map)"
  - "Def - Second Fundamental Form"
  - "Def - First Fundamental Form"
tags: [geometry, riemannian-geometry, surfaces, curvature, eigenvalues]
---

# Notation

Let $M \subset \mathbb{R}^3$ be an oriented regular surface, $p \in M$, $S_p$ the [[Def - Shape Operator (Weingarten Map)|shape operator]] at $p$, and $\mathrm{I}, \mathrm{II}$ the first and second fundamental forms. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Axiom Motivation

This is a compound page: it defines two interlocking notions — **principal curvatures** and **principal directions** — because they are the eigenvalues and eigenvectors of the shape operator $S_p$, and neither is fully understood without the other.

The desideratum is to identify, at each point $p \in M$, the **canonical extremal directions** of the second fundamental form: the directions in which the normal curvature $\mathrm{II}(T, T)$ is largest and smallest. These extremal directions are coordinate-independent — they have geometric meaning, unlike the coordinate directions $\mathbf{x}_u, \mathbf{x}_v$ which depend on the parametrisation. The corresponding extremal values of $\mathrm{II}(T, T)$ — the **principal curvatures** $\kappa_1 \geq \kappa_2$ — are then numerical invariants of the surface at $p$ that depend only on $M$ and the choice of normal.

**Why eigenvalues of $S$?** The normal curvature in direction $T \in T_pM$ (with $|T|_\mathrm{I} = 1$) is $\mathrm{II}(T, T) = \langle ST, T\rangle_\mathrm{I}$. Maximising and minimising this over unit $T$ is a classical Lagrange-multiplier problem: at an extremum, $ST = \lambda T$ for some real $\lambda$ — i.e., $T$ is an eigenvector of $S$, and $\lambda$ is the corresponding eigenvalue. By the spectral theorem for self-adjoint operators on a real $2$-dimensional inner-product space, $S$ has exactly two real eigenvalues (counted with multiplicity) and an orthonormal eigenbasis. These eigenvalues are the maximum and minimum of $\mathrm{II}(T, T)$ over unit vectors — exactly the **principal curvatures**.

**Why orthogonal eigenvectors (when eigenvalues differ)?** Self-adjoint operators on inner-product spaces have orthogonal eigenvectors for distinct eigenvalues — this is the spectral theorem. So when $\kappa_1 \neq \kappa_2$, the principal directions are perpendicular; this orthogonality was known to Euler in the eighteenth century (well before the spectral theorem was formalised). When $\kappa_1 = \kappa_2$ (an **umbilic** point), every direction is an eigendirection — every unit vector achieves the same normal curvature.

**Why does the assumption "$S$ self-adjoint" matter?** Without self-adjointness of $S$, the eigenvalues could be complex, the eigenvectors non-orthogonal, and there might be no eigenbasis at all (for a defective matrix). The fact that $S$ is self-adjoint (from symmetry of $\mathrm{II}$) is what guarantees: (i) real eigenvalues — so "principal curvatures" are real numbers; (ii) an orthogonal eigenbasis — so "principal directions" exist and are perpendicular when distinct; (iii) diagonalisability — so the shape operator is fully captured by its eigendata. Each of these is essential for the geometric picture.

**Why are these the right invariants?** The Gauss curvature $K = \kappa_1\kappa_2$ and the mean curvature $H = \kappa_1 + \kappa_2$ are the only algebraic invariants of $S$ at a point — every other polynomial in the eigenvalues is a polynomial in $K$ and $H$. So the principal curvatures encode the full algebraic information about the shape operator at a point. The reason they appear naturally — rather than, say, the average of $\kappa_1$ and $\kappa_2$ (which would be $H/2$) or some other combination — is that they are the *extremal* values of $\mathrm{II}(T, T)$, the most geometrically meaningful quantities.

A forward reference: at an umbilic ($\kappa_1 = \kappa_2$), the principal directions are not unique — every direction is an eigendirection. The **Hilbert–Liebmann theorem** (a classical rigidity theorem) says that a closed connected surface in $\mathbb{R}^3$ all of whose points are umbilic must be a sphere or a plane. So umbilics are rare and rigid — they only occur in any quantity on the model spaces of constant curvature.

---

# The Definition

> **Definition (Principal Curvatures).** Let $M \subset \mathbb{R}^3$ be an oriented regular surface, $p \in M$. The **principal curvatures** at $p$ are the eigenvalues $\kappa_1(p) \geq \kappa_2(p)$ of the [[Def - Shape Operator (Weingarten Map)|shape operator]] $S_p : T_pM \to T_pM$.
>
> Equivalently, $\kappa_1(p) = \max_{|T| = 1}\mathrm{II}_p(T, T)$ and $\kappa_2(p) = \min_{|T| = 1}\mathrm{II}_p(T, T)$, where the max and min are taken over unit tangent vectors $T \in T_pM$ with $|T|_\mathrm{I} = 1$.

> **Definition (Principal Directions).** The **principal directions** at $p$ are the eigenvectors of $S_p$ corresponding to $\kappa_1, \kappa_2$: unit vectors $T_1, T_2 \in T_pM$ with
> $$
> S_p T_i = \kappa_i T_i, \qquad i = 1, 2.
> $$
> When $\kappa_1 \neq \kappa_2$, $T_1$ and $T_2$ are orthogonal ($\langle T_1, T_2\rangle_\mathrm{I} = 0$) and unique up to signs. When $\kappa_1 = \kappa_2$ (an **umbilic** point), every direction is a principal direction.

A point $p \in M$ is called:
- **Umbilic** if $\kappa_1(p) = \kappa_2(p)$ — equivalently $S_p$ is a scalar multiple of the identity.
- **Elliptic** if $\kappa_1(p)\kappa_2(p) > 0$ — both principal curvatures have the same sign; locally $M$ is bowl-like (lies on one side of its tangent plane near $p$).
- **Hyperbolic** (or **saddle**) if $\kappa_1(p)\kappa_2(p) < 0$ — opposite signs; locally $M$ is saddle-like.
- **Parabolic** if exactly one of $\kappa_1, \kappa_2$ is zero — one principal curvature vanishes; locally $M$ is cylinder-like in that direction.
- **Planar** if $\kappa_1 = \kappa_2 = 0$ — both principal curvatures vanish; $S_p = 0$.

**Euler's formula.** For any unit tangent vector $T$ making angle $\theta$ with $T_1$,
$$
\mathrm{II}(T, T) = \kappa_1\cos^2\theta + \kappa_2\sin^2\theta.
$$
This expresses the normal curvature in any direction as a linear interpolation between the two extremal values.

In coordinates: the principal curvatures are the roots of the characteristic polynomial
$$
\det(b_{\alpha\beta} - \kappa g_{\alpha\beta}) = 0,
$$
which expands to
$$
(EG - F^2)\kappa^2 - (Eg_\mathrm{II} + Ge - 2Ff)\kappa + (eg_\mathrm{II} - f^2) = 0.
$$
The product of roots is $K = (eg_\mathrm{II} - f^2)/(EG - F^2)$ and the sum is $H = (Eg_\mathrm{II} + Ge - 2Ff)/(EG - F^2)$.

---

# Relate to Other Fields / Compression

The principal curvatures are the **eigenvalues** of the shape operator, just as the eigenvalues of the Hessian of a function are the principal "curvatures" of the function's graph at a critical point. The analogy is exact: at the origin of a graph $z = f(x, y)$ with $\nabla f(0) = 0$, the principal curvatures equal the eigenvalues of the Hessian $\nabla^2 f(0)$, and the principal directions are the eigenvector directions.

In **convex analysis**, the principal curvatures of a convex body's boundary are all positive (with the outward normal), and the **mixed volumes** of the body are expressible as integrals of elementary symmetric polynomials in the principal curvatures — the basis for the **Alexandrov–Fenchel inequalities**.

In **general relativity**, the principal extrinsic curvatures of a spacelike slice $\Sigma$ in a Lorentzian spacetime — the eigenvalues of the extrinsic curvature tensor $K_{ij}$ — encode the expansion and shear rates of normal observers, and are the inputs to the **Hamiltonian constraint** of the ADM formalism.

In **conformal geometry**, the deviation from $\kappa_1 = \kappa_2$ — captured by the **trace-free** part of $S$, the **umbilic tensor** $S - \tfrac{H}{2}\mathrm{Id}$ — vanishes precisely at umbilics. **Totally umbilic** surfaces are conformally equivalent to portions of the round sphere.

**True name:** The principal curvatures are *the maximum and minimum normal curvatures over all tangent directions*. The official "eigenvalues of $S$" is the right algebraic definition, but the operational picture is: stand at $p$, look in all directions, take the normal-plane section in each direction, measure its curvature as a plane curve — the largest and smallest values you ever see are $\kappa_1$ and $\kappa_2$. This extremal picture is what makes Euler's formula obvious and what underlies the geometric meaning of $K = \kappa_1\kappa_2$ (positive iff both extremes are same-sign, i.e., the surface bowls away in every direction).

---

# Examples / Corollaries

**Is an instance — the sphere of radius $a$.** With outward normal, $\kappa_1 = \kappa_2 = -1/a$ everywhere (Frankel convention; under do Carmo $\kappa_1 = \kappa_2 = +1/a$). Every direction is principal — the sphere is entirely umbilic. $K = 1/a^2$, $H = -2/a$.

**Is an instance — the cylinder of radius $a$.** The principal curvatures are $\kappa_1 = 1/a$ in the around-the-cylinder direction (the meridian of the circle) and $\kappa_2 = 0$ in the along-the-axis direction. $K = 0$ (the cylinder is parabolic everywhere), $H = 1/a$ (with outward normal). The principal directions are the longitudinal and azimuthal coordinate directions.

**Is an instance — the saddle $z = x^2 - y^2$ at origin.** $\kappa_1 = +2$ in the $x$-direction, $\kappa_2 = -2$ in the $y$-direction. The origin is a hyperbolic point with $K = -4 < 0$, $H = 0$.

**Is an instance — the torus of revolution.** Take a torus generated by rotating the circle $(R + r\cos v, 0, r\sin v)$ around the $z$-axis. At each point, one principal direction is the meridian (the rotated circle), with $\kappa_1 = 1/r$ (the curvature of the small circle); the other is the parallel (the rotation circle), with $\kappa_2 = \cos v/(R + r\cos v)$. So $K = (\cos v)/(r(R + r\cos v))$ — positive on the outer half ($\cos v > 0$), zero on the top and bottom circles, negative on the inner half. The integral $\int K\, dA = 0$ over the whole torus, consistent with $\chi(T^2) = 0$.

**Is NOT an instance — complex eigenvalues.** A non-self-adjoint operator could have complex eigenvalues, but the shape operator is *always* self-adjoint (by symmetry of $\mathrm{II}$), so principal curvatures are *always* real. "Complex principal curvatures" do not exist on a real surface.

**Is NOT an instance — repeated eigenvalues forcing one direction.** When $\kappa_1 = \kappa_2$ (umbilic), the operator $S$ is a scalar multiple of the identity, and **every direction** is principal — not just two. So "the principal directions at an umbilic" is not a well-defined pair of directions but is the entire tangent plane.

**Corollary — Euler's formula.** For unit $T \in T_pM$ making angle $\theta$ with $T_1$, $\mathrm{II}(T, T) = \kappa_1\cos^2\theta + \kappa_2\sin^2\theta$. **Proof:** Write $T = \cos\theta\, T_1 + \sin\theta\, T_2$ (orthonormal basis); then
$$
\mathrm{II}(T, T) = \langle ST, T\rangle = \cos^2\theta\langle ST_1, T_1\rangle + 2\cos\theta\sin\theta\langle ST_1, T_2\rangle + \sin^2\theta\langle ST_2, T_2\rangle.
$$
The cross term $\langle ST_1, T_2\rangle = \kappa_1\langle T_1, T_2\rangle = 0$, and the diagonal terms give $\kappa_1$ and $\kappa_2$. Done. This formula is the entire content of "diagonalisation of $\mathrm{II}$".

**Corollary — $K = \kappa_1\kappa_2$, $H = \kappa_1 + \kappa_2$.** Direct from the product and sum of eigenvalues of a $2 \times 2$ self-adjoint matrix.

**Corollary — under $N \to -N$, $\kappa_i \to -\kappa_i$.** The shape operator changes sign (since $S = -dN$), so each eigenvalue flips sign; $K = \kappa_1\kappa_2$ is preserved (product of two negatives), $H = \kappa_1 + \kappa_2$ flips sign.

**Corollary — sign of $K$ classifies the local shape.** At $p$, with principal frame $(T_1, T_2)$: in Monge coordinates $(x_1, x_2)$ along $(T_1, T_2)$ with $M$ as the graph $z = f(x_1, x_2)$ near origin, $f(x) = \tfrac{1}{2}(\kappa_1 x_1^2 + \kappa_2 x_2^2) + O(|x|^3)$. So $M$ near $p$ looks like the quadric $z = \tfrac{1}{2}(\kappa_1 x_1^2 + \kappa_2 x_2^2)$: elliptic paraboloid if $K > 0$, hyperbolic paraboloid if $K < 0$, parabolic cylinder if $K = 0$ and $H \neq 0$, plane if both vanish.

**Calibration check.** If you have understood the definition, you should be able to: (i) verify directly that for the sphere of radius $a$, $\mathrm{II}(T, T) = \pm 1/a$ for every unit $T$, so $\kappa_1 = \kappa_2 = \pm 1/a$ — the spherical case is the cleanest illustration of "umbilic with equal eigenvalues"; (ii) check Euler's formula on the cylinder $\mathbf{x}(u, v) = (a\cos u, a\sin u, v)$ by computing the normal curvature of the helix $u(s) = \omega s, v(s) = vs$ for some $\omega, v$, and verifying the result equals $\kappa_1\cos^2\theta = (1/a)\cos^2\theta$ where $\theta$ is the helix pitch angle; (iii) prove that on a connected open surface where every point is umbilic, the surface is contained in either a plane or a sphere (this is the local Hilbert–Liebmann theorem and an immediate consequence of the Codazzi equations applied to $b_{\alpha\beta} = \kappa g_{\alpha\beta}$).

---

# Unlocked by This

> [!tip] Gauss and Mean Curvatures *(from §4.2)*
> The basic invariants $K = \kappa_1\kappa_2$ and $H = \kappa_1 + \kappa_2$ are the [[Def - Gauss Curvature and Mean Curvature|Gauss and mean curvatures]]. They are the elementary symmetric polynomials in the principal curvatures and are sufficient to recover $\kappa_1, \kappa_2$ up to ordering — the quadratic $\kappa^2 - H\kappa + K = 0$ has roots $\kappa = (H \pm \sqrt{H^2 - 4K})/2$.

> [!tip] Lines of Curvature *(from Classical Surface Theory)*
> Away from umbilics, the principal directions form two smooth orthogonal vector fields on $M$, and their integral curves are the **lines of curvature** — an orthogonal coordinate net adapted to the geometry. In **principal coordinates** $(u, v)$ along lines of curvature, both $\mathrm{I}$ and $\mathrm{II}$ are diagonal: $\mathrm{I} = E\, du^2 + G\, dv^2$, $\mathrm{II} = e\, du^2 + g_\mathrm{II}\, dv^2$, and the principal curvatures are $\kappa_1 = e/E$, $\kappa_2 = g_\mathrm{II}/G$. This is the natural coordinate system for many computations.

> [!tip] The Umbilic Tensor and Conformal Flatness *(from Conformal Geometry)*
> The trace-free part of $S$, $S - \tfrac{H}{2}\mathrm{Id}$, is the **umbilic tensor**. Its norm $|\kappa_1 - \kappa_2|/2$ measures deviation from being umbilic. A surface in $\mathbb{R}^3$ where the umbilic tensor vanishes everywhere is **totally umbilic** and (by the Hilbert–Liebmann theorem) is a piece of a plane or a sphere. The umbilic tensor is a fundamental conformal invariant of immersed surfaces.

> [!tip] The Willmore Energy and Willmore Surfaces *(from Conformal Geometry / Geometric Analysis)*
> The integral $\mathcal{W}(M) = \int_M H^2\, dA - \int_M K\, dA = \int_M ((\kappa_1 - \kappa_2)/2)^2\, dA$ (the squared umbilic-tensor norm integrated against the area form) is the **Willmore energy**, a conformal invariant of immersed closed surfaces in $\mathbb{R}^3$. The **Willmore conjecture** (proved by Marques–Neves, 2014) says $\mathcal{W}(M) \geq 2\pi^2$ for all immersed tori in $\mathbb{R}^3$, with equality only for the Clifford torus. This is the prototypical "minimise a curvature integral subject to a topological constraint" problem.
