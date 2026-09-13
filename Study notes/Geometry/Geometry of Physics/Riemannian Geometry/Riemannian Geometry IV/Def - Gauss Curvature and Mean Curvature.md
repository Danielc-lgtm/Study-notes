---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Shape Operator (Weingarten Map)"
  - "Def - Principal Curvatures and Directions"
  - "Def - Second Fundamental Form"
  - "Def - First Fundamental Form"
tags: [geometry, riemannian-geometry, surfaces, curvature]
---

# Notation

Let $M \subset \mathbb{R}^3$ be an oriented regular surface, $p \in M$, $S_p$ the [[Def - Shape Operator (Weingarten Map)|shape operator]], $\kappa_1 \geq \kappa_2$ the [[Def - Principal Curvatures and Directions|principal curvatures]]. We adopt **Frankel's convention** $H = \kappa_1 + \kappa_2$ (the *trace*) rather than the do Carmo / Lee average $(\kappa_1 + \kappa_2)/2$; if the average convention is needed, divide our $H$ by $2$. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

This is a compound page: it defines two interlocking notions — the **Gauss curvature** $K$ and the **mean curvature** $H$ — because they are the two basis-independent algebraic invariants of the shape operator at a point, and the surface theory is built on their interplay.

---

# Axiom Motivation

The desideratum is to extract from the shape operator $S_p$ at each point $p \in M$ the **scalar invariants** that have geometric meaning — quantities depending only on the geometry of $M$ at $p$ and the choice of normal, not on the parametrisation or any chosen basis. Linear algebra tells us that for any $2 \times 2$ matrix the only two such invariants are the **trace** and the **determinant** (every other invariant is a polynomial in these). So the Gauss curvature $K = \det S$ and mean curvature $H = \mathrm{tr}\, S$ are forced by linear algebra — they are *the* two scalar invariants of $S$ at a point.

**Why these specifically?** Among all conceivable scalar invariants — the eigenvalues individually $\kappa_1, \kappa_2$, their ratio $\kappa_1/\kappa_2$, the discriminant $(\kappa_1 - \kappa_2)^2 = H^2 - 4K$ — only the symmetric functions of the eigenvalues are basis-independent. The fundamental theorem of symmetric polynomials says every symmetric polynomial in two variables is a polynomial in the elementary ones, $e_1 = \kappa_1 + \kappa_2$ and $e_2 = \kappa_1\kappa_2$. So $H$ and $K$ are the universal invariants from which every other symmetric invariant is built. The individual principal curvatures $\kappa_1, \kappa_2$ are not invariants in this sense — they require a *choice* of which eigenvalue to call "first", which is meaningful only away from umbilics.

**Why is $K$ intrinsic and $H$ not?** This is the entire content of the [[Thm - Theorema Egregium of Gauss|Theorema Egregium]]: $K = R_{1212}/\det g$ can be computed from the first fundamental form alone, while $H = b^\alpha_{\;\alpha}$ requires the second fundamental form. The reason at a structural level is that $K = \det S = \det b_{\alpha\beta}/\det g_{\alpha\beta}$ is a determinant ratio, and this ratio happens to satisfy an identity (one of the Gauss equations) expressing it as a Riemann-curvature component of $g$ alone; the analogous identity for $\mathrm{tr}\, S$ does not exist — the trace of the shape operator genuinely depends on the embedding.

**Why is $K$ the "right" curvature of a surface?** $K$ has three independent characterisations, each of which justifies the name "curvature":
1. **Algebraic:** $K = \kappa_1\kappa_2 = \det S$ — the product of principal curvatures.
2. **Geometric (Gauss):** $K(p) = \lim_{U \to p}(\text{signed area of }N(U))/\text{area of }U$ — the local Jacobian of the [[Def - Gauss Normal Map|Gauss normal map]].
3. **Intrinsic (Theorema Egregium):** $K = R_{1212}/\det g$ — depends only on the first fundamental form.

The agreement of these three definitions is the deep content of the theory. Each suggests a different generalisation: the algebraic one suggests sectional curvature; the geometric one suggests characteristic-class theory; the intrinsic one suggests Riemann curvature on abstract manifolds. All three generalisations are correct and consistent (in their respective contexts).

**Why is $H$ the right "variational" curvature?** The first variation of area formula ([[Thm - First Variation of Area]]) gives $\delta A = -\int H\,\langle v, N\rangle\, dA + \text{boundary}$, identifying $H$ as the $L^2$-gradient of the area functional. So $H = 0$ characterises critical points of area (minimal surfaces), and $H = \text{const}$ characterises critical points of area with fixed-volume constraint (soap bubbles). The mean curvature is the right object for variational and PDE problems even though it is extrinsic, because area is an extrinsic quantity that depends on the embedding.

**Forced form.** Once one accepts that the shape operator $S$ is the right object encoding curvature at a point, the Gauss and mean curvatures are forced by linear algebra: they are the *only two* basis-independent invariants of a self-adjoint $2 \times 2$ operator. Everything else in the chapter — Theorema Egregium, Gauss–Bonnet, minimal surfaces — is the unfolding of consequences of $K$ and $H$, especially of the intrinsic / extrinsic split between them.

---

# The Definition

> **Definition (Gauss Curvature).** Let $M \subset \mathbb{R}^3$ be an oriented regular surface, $p \in M$. The **Gauss curvature** at $p$ is
> $$
> K(p) := \kappa_1(p)\kappa_2(p) = \det S_p,
> $$
> the product of the [[Def - Principal Curvatures and Directions|principal curvatures]] or equivalently the determinant of the [[Def - Shape Operator (Weingarten Map)|shape operator]] at $p$.

> **Definition (Mean Curvature, Frankel convention).** The **mean curvature** at $p$ is
> $$
> H(p) := \kappa_1(p) + \kappa_2(p) = \mathrm{tr}\, S_p,
> $$
> the sum of principal curvatures (i.e., the trace of the shape operator). Some authors (do Carmo, Lee) define the mean curvature as $(\kappa_1 + \kappa_2)/2$, the average; we follow Frankel.

In local coordinates,
$$
K = \frac{\det b_{\alpha\beta}}{\det g_{\alpha\beta}} = \frac{eg_\mathrm{II} - f^2}{EG - F^2},
\qquad
H = b^\alpha_{\;\alpha} = g^{\alpha\beta}b_{\alpha\beta} = \frac{Eg_\mathrm{II} + Ge - 2Ff}{EG - F^2}.
$$
For a graph $z = f(x, y)$ over the $xy$-plane, with $W := 1 + f_x^2 + f_y^2$,
$$
K = \frac{f_{xx}f_{yy} - f_{xy}^2}{W^2},
\qquad
H = \frac{(1 + f_y^2)f_{xx} - 2f_xf_yf_{xy} + (1 + f_x^2)f_{yy}}{W^{3/2}}.
$$

**Sign conventions and behaviour under normal reversal.** Under $N \to -N$, $S \to -S$, so $H \to -H$ and $K = \det(-S) = (-1)^2\det S = +K$ (preserved). So $K$ is invariant of the choice of normal; $H$ is sign-dependent.

**Sign of $K$ and local shape.** $K > 0$: elliptic (locally bowl-like, $M$ lies on one side of its tangent plane near $p$). $K < 0$: hyperbolic (saddle-like). $K = 0$: parabolic (one principal curvature zero) or planar (both zero).

---

# Categorical / Structural Definition

Structurally, $K$ and $H$ are the **elementary symmetric polynomials** in the eigenvalues of $S_p$. They sit in the broader story of **higher mean curvatures** $\sigma_k = e_k(\kappa_1, \kappa_2, \ldots, \kappa_n)$ for hypersurfaces of dimension $n$: $\sigma_1 = H$ (sum, the **mean curvature**), $\sigma_n = K$ (product, the **Gauss–Kronecker curvature**, generalising Gauss curvature), and intermediate $\sigma_k$ for $1 < k < n$. The $\sigma_k$ are the objects of interest in **fully nonlinear curvature flows** ($\sigma_k$-flows), the **Christoffel–Minkowski problem**, and **prescribed curvature** PDE problems.

From the perspective of **characteristic classes**, the Gauss curvature $K$ is a degree-$2$ form on $M$ (specifically $K\cdot \mathrm{vol}^2_M = K\, dA$ is a $2$-form), and on a closed oriented surface its integral is a topological invariant — the **Euler number** $\chi(M)$ — via Gauss–Bonnet. The mean curvature $H$ does not produce a topological invariant on integration; $\int H\, dA$ is a non-topological quantity (the **total mean curvature**), although $\int H^2\, dA$ is a conformal invariant (the **Willmore energy**).

In the language of **principal bundles**, the curvature 2-form of the connection on the principal $O(2)$-bundle of orthonormal frames on $M$ is $K\, dA$ — see [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]]. The Gauss curvature is the local coefficient of the curvature of the Levi-Civita connection.

---

# Relate to Other Fields / Compression

The Gauss curvature is the surface case of the more general **sectional curvature** $K(\Pi)$ on a higher-dimensional Riemannian manifold: for a $2$-plane $\Pi \subset T_pM$, $K(\Pi)$ is the Gauss curvature of the $2$-surface obtained by exponentiating $\Pi$. The full Riemann curvature tensor is determined algebraically by the sectional curvatures, so the surface case generates all the higher-dimensional notions.

The mean curvature is the **trace of the second fundamental form** (with respect to the metric), which generalises immediately to hypersurfaces in any Riemannian manifold: $H = g^{ij}\mathrm{II}_{ij}$. The mean curvature vector $\vec H = H\cdot N$ is the **codimension-$1$ case** of the general mean curvature vector on a submanifold of any codimension, and it is always the $L^2$-gradient of the volume functional.

In **general relativity**, the analogue of $K$ for a spacelike $3$-slice $\Sigma$ in a Lorentzian $4$-spacetime is the **scalar curvature** $R(\Sigma)$ — which enters the **Hamiltonian constraint** of the ADM formulation. The analogue of $H$ is the **trace of the extrinsic curvature** $K = K^i_{\;i}$, which enters the **momentum constraint**.

In **soap film and bubble physics**, $H$ determines the pressure jump across a film via Laplace's formula $\Delta p = -2\sigma H$ ($\sigma$ = surface tension), and the equilibrium shape of a free soap film is a minimal surface ($H = 0$); the equilibrium shape of a bubble is a constant-mean-curvature surface ($H = \text{const}$). See [[Ex - The Catenoid is a Minimal Surface]].

**True name:** The Gauss curvature is *the intrinsic measure of curvature*. The mean curvature is *the extrinsic / variational measure of curvature*. The official "determinant and trace of the shape operator" is the right algebraic definition, but the operational picture is the intrinsic-vs-extrinsic split that Theorema Egregium makes precise.

---

# Examples / Corollaries

**Is an instance — the plane.** $\kappa_1 = \kappa_2 = 0$, $K = 0$, $H = 0$. The flat plane is the simplest surface.

**Is an instance — the sphere of radius $a$.** $\kappa_1 = \kappa_2 = -1/a$ (outward normal, Frankel convention) or $+1/a$ (inward), $K = 1/a^2$, $H = \mp 2/a$. The sphere has constant positive Gauss curvature — the prototype of a **positively curved surface**.

**Is an instance — the cylinder of radius $a$.** $\kappa_1 = 1/a$, $\kappa_2 = 0$, $K = 0$, $H = 1/a$. The cylinder is flat ($K = 0$, intrinsically equivalent to the plane by Theorema Egregium) but extrinsically curved.

**Is an instance — the pseudosphere** (surface of revolution of tractrix). $K = -1$ everywhere — constant negative Gauss curvature. See [[Ex - Gauss Curvature of the Pseudosphere is -1]]. This is the classical concrete model of (part of) the hyperbolic plane.

**Is an instance — the catenoid $\mathbf{x}(u, v) = (a\cosh(v/a)\cos u, a\cosh(v/a)\sin u, v)$.** $H = 0$ everywhere — the catenoid is minimal. $K = -1/(a^2\cosh^4(v/a)) < 0$ — hyperbolic everywhere, consistent with the general theorem that minimal surfaces have $K \leq 0$.

**Is NOT an instance — a "Gauss curvature" without the embedding.** On an abstract Riemannian $2$-manifold (e.g., $\mathbb{H}^2$ in the upper half-plane), $K$ is *defined* via the intrinsic formula $K = R_{1212}/\det g$ (Theorema Egregium). But $H$ has no meaning — there is no embedding to provide a shape operator. So on an abstract $2$-manifold, $K$ exists but $H$ does not.

**Is NOT an instance — a non-symmetric "trace".** The trace of a non-self-adjoint matrix could be complex; the shape operator is always self-adjoint (by symmetry of $\mathrm{II}$), so $H = \mathrm{tr}\, S$ is always real. "Complex mean curvature" does not occur on a real surface.

**Corollary — inequality $K \leq H^2/4$.** From $(\kappa_1 - \kappa_2)^2 = (\kappa_1 + \kappa_2)^2 - 4\kappa_1\kappa_2 = H^2 - 4K \geq 0$. Equality only at umbilics. So large $|H|$ does not imply large $K$, but large $K$ does imply $|H| \geq 2\sqrt K$. Consequence: minimal surfaces ($H = 0$) automatically have $K \leq 0$.

**Corollary — under conformal change of metric.** If $\tilde g = e^{2u}g$ on a Riemannian $2$-manifold, the Gauss curvatures are related by $\tilde K = e^{-2u}(K - \Delta_g u)$ (the **uniformisation equation**). This formula does not involve the embedding and is purely intrinsic. The corresponding mean curvature transformation requires the embedding and involves more terms.

**Corollary — sign of $K$ classifies the local geometry.** Near $p$, in principal coordinates with origin at $p$, $M$ is the graph $z = \tfrac{1}{2}(\kappa_1 x_1^2 + \kappa_2 x_2^2) + O(|x|^3)$. If $K(p) > 0$, this quadric is an elliptic paraboloid; the surface lies on one side of the tangent plane. If $K(p) < 0$, hyperbolic paraboloid (saddle); the surface crosses the tangent plane. If $K(p) = 0$ and $H(p) \neq 0$, parabolic cylinder.

**Calibration check.** If you have understood the definitions, you should be able to: (i) compute $K = 1/a^2$ for the sphere of radius $a$ using the coordinate formula with $E = a^2$, $G = a^2\sin^2\theta$, $F = 0$, $e = -a$, $f = 0$, $g_\mathrm{II} = -a\sin^2\theta$ (giving $eg_\mathrm{II} - f^2 = a^2\sin^2\theta$ and $EG - F^2 = a^4\sin^2\theta$, ratio $1/a^2$); (ii) check the inequality $K \leq H^2/4$ on a saddle of the form $z = ax^2 - by^2$ at the origin, where $\kappa_1 = a, \kappa_2 = -b$ (so $K = -ab \leq (a-b)^2/4 = H^2/4$ — strict for $a, b > 0$); (iii) verify that the catenoid's mean curvature vanishes by computing the explicit formulae from the parametrisation $\mathbf{x}(u, v) = (a\cosh(v/a)\cos u, a\cosh(v/a)\sin u, v)$.

---

# Unlocked by This

> [!tip] Theorema Egregium *(from §4.3)*
> The Gauss curvature is intrinsic: $K = R_{1212}/\det g$. This means $K$ can be computed from the first fundamental form alone and is preserved by isometries (bending without stretching). The mean curvature $H$ is not intrinsic. See [[Thm - Theorema Egregium of Gauss]].

> [!tip] Gauss–Bonnet Theorem *(from §4.3)*
> For a closed oriented surface, $\int_M K\, dA = 2\pi\chi(M)$. The pointwise local quantity $K$ integrates to a topological invariant. No analogous formula exists for $H$. See [[Thm - Gauss-Bonnet Theorem for Surfaces]].

> [!tip] Minimal Surfaces and the Plateau Problem *(from §4.4)*
> Surfaces with $H \equiv 0$ are the **minimal surfaces** ([[Def - Minimal Surface]]), the critical points of area. The **Plateau problem** of finding a minimal surface with prescribed boundary is one of the oldest variational problems in mathematics; **mean curvature flow** $\partial_t \mathbf{x} = HN$ is the parabolic gradient flow that drives surfaces toward minimal surfaces. This is the entry to **geometric analysis** and **geometric measure theory**.

> [!tip] Sectional Curvature *(from Riemannian Geometry III)*
> On a higher-dimensional Riemannian manifold $M^n$, the sectional curvature $K(\Pi)$ of a $2$-plane $\Pi \subset T_pM$ generalises Gauss curvature. The **constant sectional curvature** model spaces are $S^n$ (curvature $+1$), $\mathbb{R}^n$ (curvature $0$), and $\mathbb{H}^n$ (curvature $-1$), and comparison theorems (Toponogov, Rauch) relate the geometry of an arbitrary Riemannian manifold to these models via sectional curvature bounds.

> [!tip] The Willmore Energy and Willmore Conjecture *(from Conformal Geometry)*
> The integral $\mathcal{W}(M) = \int_M (H/2)^2\, dA$ (in the do-Carmo convention, or $\int H^2/4\, dA$ in Frankel's) is the **Willmore energy** — a conformal invariant of immersed closed surfaces. The **Willmore conjecture** (now a theorem of Marques–Neves) says $\mathcal{W}(M) \geq 2\pi^2$ for tori, with equality only for the Clifford torus. This is one of the central results in $21$st-century **conformal geometry**.
