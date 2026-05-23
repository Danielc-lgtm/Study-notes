---
type: topic
subject: riemannian-geometry
chapter: "4.1-4.4"
title: "Riemannian Geometry IV — Classical Geometry of Surfaces in R^3"
tags: [geometry, riemannian-geometry, surfaces, curvature, gauss-bonnet]
---

# Notation Registry

A standing convention: throughout this chapter, $M \subset \mathbb{R}^3$ is an **oriented regular $2$-dimensional submanifold** of Euclidean $3$-space (cf. [[Def - Embedded Submanifold]]), thought of either locally as the image $M = F(U)$ of a parametrisation $F : U \subset \mathbb{R}^2 \to \mathbb{R}^3$ with $F_*$ of rank $2$, or globally as a closed embedded surface with a chosen continuous unit normal field $\hat n$. We use the **outward-pointing normal** convention whenever the surface bounds a region. We follow Frankel's sign choices: the shape operator is $S = -dN$ (so $S$ has positive eigenvalues for a sphere with outward normal), and we write the mean curvature as the **trace** $H = \kappa_1 + \kappa_2$ rather than the average $(\kappa_1 + \kappa_2)/2$ (Frankel uses the trace convention; the do Carmo / Lee convention divides by $2$). Where a formula is convention-sensitive, both versions are noted.

- $M \subset \mathbb{R}^3$ — an oriented regular surface
- $U \subset \mathbb{R}^2$ — a parametrising open set; $(u, v) = (u^1, u^2)$ — local coordinates on $U$
- $F : U \to \mathbb{R}^3$ — a parametrisation; $\mathbf{x}(u, v) = F(u, v)$ — the position vector
- $\mathbf{x}_\alpha = \partial \mathbf{x}/\partial u^\alpha$ — coordinate tangent vectors spanning $T_pM$
- $\hat n = N$ — the chosen unit normal field on $M$; for the sphere with outward normal, $N(p) = p/|p|$
- $\mathrm{I}$ or $g$ — the **first fundamental form**, the induced Riemannian metric on $M$; $\mathrm{I} = g_{\alpha\beta}\, du^\alpha\, du^\beta$
- Classical notation: $E = g_{11}$, $F = g_{12} = g_{21}$, $G = g_{22}$, so $\mathrm{I} = E\, du^2 + 2F\, du\, dv + G\, dv^2$
- $\mathrm{II}$ or $b$ — the **second fundamental form**; $\mathrm{II} = b_{\alpha\beta}\, du^\alpha\, du^\beta$
- Classical notation: $e = b_{11}$, $f = b_{12}$, $g_{\mathrm{II}} = b_{22}$ (we write $g$ for the metric, so $g_{\mathrm{II}}$ avoids clash); $\mathrm{II} = e\, du^2 + 2f\, du\, dv + g_{\mathrm{II}}\, dv^2$
- $S$ — the **shape operator** (Weingarten map) $S = -dN : T_pM \to T_pM$; $\mathrm{II}(X, Y) = \langle SX, Y\rangle = \langle X, SY\rangle$
- $\kappa_1, \kappa_2$ — **principal curvatures**, the eigenvalues of $S$
- $T_1, T_2$ — **principal directions**, the corresponding eigenvectors (orthogonal when $\kappa_1 \neq \kappa_2$)
- $K = \kappa_1\kappa_2 = \det S$ — the **Gauss curvature**
- $H = \kappa_1 + \kappa_2 = \mathrm{tr}\, S$ — the **mean curvature** (Frankel convention)
- $N : M \to S^2$ — the **Gauss normal map**, $N(p) = \hat n(p) \in S^2$
- $\mathrm{vol}^2_M$ or $dA$ — the area element of $M$; $dA = \sqrt{\det g_{\alpha\beta}}\, du \wedge dv$
- $\mathrm{vol}^2_S$ — the area element of $S^2$ (the round sphere)
- $\deg(\phi)$ — the **Brouwer degree** of a smooth map $\phi : M^n \to V^n$ between closed oriented manifolds of the same dimension
- $\mathrm{Ind}_p(v)$ — the **Kronecker / Poincaré–Hopf index** of a vector field $v$ at an isolated zero $p$
- $\chi(M)$ — the **Euler characteristic** of $M$
- $\nabla T/dt$ or $\nabla_T T$ — the **intrinsic (covariant) derivative** of a tangent field along a curve, the tangential projection of $dT/dt$
- $\kappa_g$ — the **geodesic curvature** of a curve on $M$; $\kappa_g = |\nabla T/ds|$ when $T$ is the unit tangent
- $\Gamma^\gamma_{\alpha\beta}$ — Christoffel symbols of the [[Def - Riemannian Metric|induced metric]]
- $R^\tau_{\,\alpha\gamma\beta}$ — components of the intrinsic Riemann curvature tensor; on a surface $R_{1212}/\det g = K$
- $\mathrm{Lk}(C_1, C_2)$ — the **Gauss linking number** of two disjoint closed curves in $\mathbb{R}^3$

---

# Motivation

Here is the entire chapter in one sentence: a surface in $\mathbb{R}^3$ carries two fundamental forms — the first measures its intrinsic geometry (lengths, angles, areas), the second measures its extrinsic curving inside ambient space — and the great miracle, **Gauss's Theorema Egregium**, says that one specific combination of the second form is in fact intrinsic and survives bending. This single fact is the historical origin of curvature as we now understand it: not as a property of the embedding, but as a property the surface carries with it under any rigid or non-rigid deformation that preserves arc length. Everything else in the chapter — geodesics, parallel displacement, the Gauss–Bonnet theorem, the Poincaré–Hopf theorem, minimal surfaces — is the unfolding of consequences of the fundamental forms and the Egregium principle.

Classical differential geometry is the bridge between the calculus of curves in space (the Frenet–Serret apparatus) and the abstract Riemannian geometry of [[Riemannian Geometry I — Connections and Covariant Differentiation|connections]], [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles|geodesics]], and [[Riemannian Geometry III — Riemann Curvature and Topology|curvature]]. Gauss and his successors — Codazzi, Bonnet, Mainardi, Beltrami — worked out the geometry of surfaces in $\mathbb{R}^3$ in painstaking concrete detail in the early nineteenth century, and from this concrete laboratory Riemann distilled the abstract notion of a Riemannian manifold in his 1854 habilitation lecture. Studying the surface case is not a quaint historical detour: it is the place where every modern concept appears at its most visualisable, and where the relations between intrinsic and extrinsic geometry, between local and global, between curvature and topology, can be touched with one's hands.

The structural backbone of the chapter is the following hierarchy of curvature notions:

$$
\underbrace{\mathrm{II} = -\langle d\mathbf{x}, dN\rangle}_{\text{extrinsic, vector-in-}\mathbb{R}^3}\;\longrightarrow\;\underbrace{S = -dN}_{\text{shape operator}}\;\longrightarrow\;\underbrace{\kappa_1, \kappa_2}_{\text{principal curvatures}}\;\longrightarrow\;\underbrace{H = \kappa_1+\kappa_2}_{\text{extrinsic}}\quad\text{and}\quad\underbrace{K = \kappa_1\kappa_2}_{\text{intrinsic (Theorema Egregium)}}.
$$

Moving left to right, more and more information is forgotten: the extrinsic vector $dN \in \mathbb{R}^3$ becomes a tangential linear map $S$, then a pair of eigenvalues, then their sum and product. The astonishing punchline is that the *product* $K = \kappa_1\kappa_2$ survives one extra projection: it is computable from the metric $g_{\alpha\beta}$ alone, without reference to the embedding. The sum $H$ does not survive — a flat sheet of paper ($H = 0$) and a rolled-up cylinder ($H \neq 0$) are isometric, so any intrinsic invariant they share, including $K = 0$, must agree, and indeed both have $K = 0$. The same sheet rolled into a cone keeps $K = 0$ but acquires $H \neq 0$.

The chapter then makes the leap from local to global. The Gauss normal map $N : M \to S^2$ on a closed oriented surface has a **Brouwer degree**, an integer that measures how many times $N$ wraps $M$ around $S^2$. The change-of-area formula $N^* \mathrm{vol}^2_S = K\, dA$ converts the degree into an integral of $K$: $\int_M K\, dA = 4\pi \deg(N)$, and this number turns out to equal $2\pi \chi(M)$, the Euler characteristic of $M$ — the **Gauss–Bonnet theorem for surfaces**. A pointwise local quantity (curvature) integrates over a closed surface to a topological invariant (Euler characteristic), and the surface cannot be smoothly deformed to change this integer. The same principle, in a parallel chapter ([[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet|Chern's generalisation]]), governs every "characteristic class" in modern differential topology.

A second global theorem, **Poincaré–Hopf**, says that the sum of indices of an isolated-zero vector field on a closed oriented surface also equals $\chi(M)$. Combined with Gauss–Bonnet, this yields one of the cleanest topological obstructions in mathematics: **the hairy ball theorem** — there is no nowhere-vanishing tangent vector field on $S^2$ — falls out as a one-line corollary, because $\chi(S^2) = 2 \neq 0$ forces every continuous tangent field to have a zero.

The last theme is **minimal surfaces**: surfaces with $H \equiv 0$, the equilibrium shapes of soap films spanning a wire frame. The first variation of area formula $\delta A = -\int H\, \langle v, N\rangle\, dA + \text{boundary term}$ makes the variational characterisation explicit: $M$ is a critical point of area for all compactly supported normal variations iff $H = 0$. The PDE $H = 0$ — in graph form, $(1+f_y^2)f_{xx} - 2f_xf_y f_{xy} + (1+f_x^2)f_{yy} = 0$ — is the **minimal surface equation**, one of the oldest and richest nonlinear PDEs in geometric analysis.

The reader is assumed to have worked through [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|embedded submanifolds]], [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|orientation and integration on manifolds]], [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds|Riemannian metrics]], and to be comfortable with [[Def - Inner Product Space|self-adjoint operators on Euclidean space]] (so that the spectral theorem for $S$ is automatic). The previous topics in this batch — [[Riemannian Geometry I — Connections and Covariant Differentiation|connections]], [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles|geodesics]], [[Riemannian Geometry III — Riemann Curvature and Topology|curvature]] — develop the same machinery at the abstract Riemannian-manifold level; this chapter is the concrete two-dimensional embedded case, simultaneously the historical origin and the most visualisable laboratory.

---

# Concept Map

## §4.1 First and Second Fundamental Forms

- **[[Def - First Fundamental Form]]**
	- The first fundamental form $\mathrm{I}$ on a parametrised surface $M = F(U) \subset \mathbb{R}^3$ is the Riemannian metric induced from the Euclidean inner product: $\mathrm{I}(X, Y) = \langle X, Y\rangle_{\mathbb{R}^3}$ for tangent vectors $X, Y \in T_pM$. In coordinates, with $\mathbf{x}_\alpha = \partial \mathbf{x}/\partial u^\alpha$, one has $g_{\alpha\beta} = \langle \mathbf{x}_\alpha, \mathbf{x}_\beta\rangle$, so $\mathrm{I} = E\, du^2 + 2F\, du\, dv + G\, dv^2$ with $E, F, G$ the components of the metric matrix. This is the data needed to compute lengths of curves, angles between tangents, and areas of regions on $M$; it is intrinsic in the sense that an inhabitant of $M$ (a "two-dimensional being") can measure it without leaving the surface.

- **[[Def - Gauss Normal Map]]**
	- For an oriented regular surface $M \subset \mathbb{R}^3$, the Gauss normal map is $N : M \to S^2$, $N(p) = \hat n(p)$, sending each point to its unit normal viewed as a point of the unit sphere. The differential $dN_p : T_pM \to T_{N(p)}S^2$ takes values in the tangent space to $S^2$ at $N(p)$, which is parallel-translated to $T_pM$ (both are the orthogonal complement of $\hat n(p)$ in $\mathbb{R}^3$). The Gauss map captures the entire extrinsic geometry of $M$: its differential encodes the second fundamental form, its Jacobian determinant is $K$, and its Brouwer degree on a closed surface is $\chi(M)/2$.

- **[[Def - Second Fundamental Form]]**
	- The second fundamental form is $\mathrm{II}(X, Y) = -\langle dN(X), Y\rangle = \langle \mathbf{x}_{\alpha\beta}, N\rangle\, du^\alpha du^\beta = b_{\alpha\beta}\, du^\alpha du^\beta$. It is a symmetric bilinear form on each $T_pM$ that measures the **normal component of the curvature** of any curve in $M$ — Meusnier's observation that all curves through $p$ with the same tangent $T$ have the same normal-component-of-curvature $\mathrm{II}(T,T)$. Unlike the first fundamental form, $\mathrm{II}$ depends on the embedding: bending a flat sheet changes $\mathrm{II}$ even though $\mathrm{I}$ is preserved.

- **[[Def - Shape Operator (Weingarten Map)]]**
	- The shape operator $S = -dN : T_pM \to T_pM$ is the metric dual of the second fundamental form: $\mathrm{II}(X, Y) = \langle SX, Y\rangle$. Equivalently $S$ is the **Weingarten map**, the rate at which the normal direction changes as one moves on the surface. Because $\mathrm{II}$ is symmetric, $S$ is self-adjoint with respect to the induced metric, so the spectral theorem gives real eigenvalues (the principal curvatures) and orthogonal eigenvectors (the principal directions) at every point.

> [!tip] Unlocked: Shape Operator on Higher-Codimension Submanifolds *(from Differential Geometry)*
> The construction generalises: for a submanifold $M^k \subset \mathbb{R}^N$ with normal bundle $\nu M$, the shape operator becomes a vector-valued bilinear form $\mathrm{II} : TM \times TM \to \nu M$. The **mean curvature vector** $\vec H = \mathrm{tr}_g \mathrm{II} \in \nu M$ governs the first variation of area, and the equation $\vec H = 0$ defines **minimal submanifolds**. This is the entryway to **geometric measure theory** and Federer–Fleming currents.

- **[[Ex - Gauss Curvature of the Sphere of Radius R is 1 over R Squared]]** (⭐)
	- Compute the first and second fundamental forms of the sphere of radius $a$ in spherical coordinates and verify $K = 1/a^2$ everywhere — Gauss's calibration example.

> [!note] Exercise Index — §4.1
> [[Exercise Index - §4.1 First and Second Fundamental Forms]]

## §4.2 Gauss and Mean Curvatures

- **[[Def - Principal Curvatures and Directions]]**
	- The principal curvatures $\kappa_1(p) \geq \kappa_2(p)$ at $p \in M$ are the eigenvalues of the shape operator $S_p$, equivalently the maximum and minimum of $\mathrm{II}(T, T)$ over unit tangent vectors $T$. The corresponding eigenvectors are the principal directions, orthogonal when $\kappa_1 \neq \kappa_2$. A point where $\kappa_1 = \kappa_2$ is called an **umbilic**; the sphere consists entirely of umbilic points, and a classical theorem (Hilbert–Liebmann) says any connected closed surface with all points umbilic must be a sphere. **Euler's formula** $\kappa(\theta) = \kappa_1\cos^2\theta + \kappa_2\sin^2\theta$ recovers the normal curvature in any direction.

- **[[Def - Gauss Curvature and Mean Curvature]]**
	- The Gauss curvature is $K = \kappa_1\kappa_2 = \det S = \det(b_{\alpha\beta})/\det(g_{\alpha\beta})$; the mean curvature (Frankel convention) is $H = \kappa_1 + \kappa_2 = \mathrm{tr}\, S = b^\alpha_{\;\alpha}$. The sign of $K$ classifies the local shape: $K > 0$ is elliptic (bowl-like, both principal curvatures same sign), $K < 0$ is hyperbolic (saddle-like, opposite signs), $K = 0$ is parabolic (one principal curvature vanishes). $K$ changes sign under no change of normal but is reversed in sign by an orientation-reversing isometry of $\mathbb{R}^3$; $H$ reverses sign under change of normal but is preserved under all isometries of $\mathbb{R}^3$.

> [!tip] Unlocked: Sectional Curvature *(from Riemannian Geometry III)*
> On a higher-dimensional Riemannian manifold the role of Gauss curvature is played by the **sectional curvature** $K(\Pi)$ of a 2-plane $\Pi \subset T_pM$: by the exponential map, $\Pi$ generates a 2-surface in $M$, and $K(\Pi)$ is the Gauss curvature of that surface at $p$. The sectional curvatures determine the full Riemann tensor (algebraically), and constant-sectional-curvature spaces are the model geometries $S^n$, $\mathbb{R}^n$, $\mathbb{H}^n$. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

- **[[Ex - Gauss Curvature of the Pseudosphere is -1]]** (⭐⭐)
	- The pseudosphere — the surface of revolution of a tractrix about the $z$-axis — has constant Gauss curvature $K = -1$. Compute the fundamental forms and verify; this gives the historically first concrete model of hyperbolic geometry as a (singular) surface in $\mathbb{R}^3$.

> [!note] Exercise Index — §4.2
> [[Exercise Index - §4.2 Gauss and Mean Curvatures]]

## §4.3 Theorema Egregium and Gauss–Bonnet

- **[[Thm - Equations of Gauss and Codazzi]]**
	- The Gauss equations $R^\tau_{\,\alpha\gamma\beta} = b^\tau_{\;\gamma}b_{\alpha\beta} - b^\tau_{\;\beta}b_{\alpha\gamma}$ and the Codazzi (Mainardi–Codazzi–Peterson) equations $\partial_\gamma b_{\alpha\beta} - \Gamma^\tau_{\alpha\gamma}b_{\tau\beta} = \partial_\beta b_{\alpha\gamma} - \Gamma^\tau_{\alpha\beta}b_{\tau\gamma}$ are integrability conditions that must hold for any pair $(g_{\alpha\beta}, b_{\alpha\beta})$ realised as the first and second fundamental forms of a surface in $\mathbb{R}^3$. The Bonnet fundamental theorem of surface theory states the converse: locally these conditions are also sufficient for a surface with prescribed forms to exist, uniquely up to rigid motion.

- **[[Thm - Theorema Egregium of Gauss]]**
	- The Gauss curvature $K$ is intrinsic — it depends only on the first fundamental form $g_{\alpha\beta}$ and its derivatives, not on how the surface sits in $\mathbb{R}^3$. Explicitly $K = R_{1212}/\det(g_{\alpha\beta})$, where $R_{1212}$ is the single non-redundant component of the Riemann curvature of the induced metric. Consequence: bending a surface without stretching (a local isometry) preserves $K$ even though $\kappa_1$, $\kappa_2$, and $H$ change wildly. The flat plane and a rolled cylinder both have $K = 0$, so the plane *can* be wrapped into a cylinder without distortion; the plane and the sphere have different $K$, so no piece of the Earth's surface can be flattened onto a map without distortion.

> [!tip] Unlocked: Intrinsic Curvature of Abstract Riemannian Manifolds *(from Riemannian Geometry III)*
> The Theorema Egregium is the historical seed of the modern definition of curvature: Riemann's curvature tensor $R^\sigma_{\,\rho\mu\nu}$ on an abstract Riemannian manifold is defined intrinsically (no embedding needed), and the Gauss curvature is the special $n=2$ case. The whole "intrinsic geometry" program — Riemann's 1854 *Habilitationsvortrag*, then Christoffel, Levi-Civita, Ricci, Einstein — is the consequence of taking Gauss's discovery seriously and asking what curvature *is*, as an intrinsic concept.

- **[[Def - Brouwer Degree of a Map]]**
	- For a smooth map $\phi : M^n \to V^n$ between closed oriented manifolds of the same dimension, the Brouwer degree is the integer $\deg(\phi) = \int_M \phi^*\omega$, where $\omega$ is any $n$-form on $V$ with $\int_V\omega = 1$. Equivalently, at any regular value $y \in V$, $\deg(\phi) = \sum_{x \in \phi^{-1}(y)} \mathrm{sign}\,\phi(x)$, with the sign $\pm 1$ recording whether $\phi_*$ at $x$ preserves or reverses orientation. The degree is independent of the choice of $\omega$ and of the regular value, and is a homotopy invariant — these are the three pillars of degree theory.

- **[[Thm - Brouwer Degree is a Homotopy Invariant]]**
	- If $\phi_t : M^n \to V^n$ is a smooth homotopy of maps between closed oriented manifolds of the same dimension, then $\deg(\phi_t)$ is independent of $t$. The proof uses the fact that $\phi_t^*\omega - \phi_0^*\omega = d(\text{something})$ via a homotopy operator, and the integral of an exact form on a closed manifold vanishes. The corollary that $\deg : C^\infty(M, V)/\text{homotopy} \to \mathbb{Z}$ is well-defined is what makes degree theory powerful — homotopy-invariant integer-valued, and almost the unique such invariant in this dimension.

- **[[Thm - The Gauss Normal Map has Degree Half the Euler Characteristic]]**
	- For a closed oriented surface $M \subset \mathbb{R}^3$, the Brouwer degree of the Gauss normal map equals half the Euler characteristic: $\deg(N) = \tfrac{1}{2}\chi(M) = 1 - g$, where $g$ is the genus. Combined with the change-of-area formula $N^*\mathrm{vol}^2_{S^2} = K\, dA$ and $\int_{S^2}\mathrm{vol}^2 = 4\pi$, this immediately yields the Gauss–Bonnet integral formula. The proof is two slogans: the degree of $N$ is $(\text{signed area of }N(M))/4\pi$, and the signed area can be computed by tilting $M$ until the regular preimages of a generic direction become countable saddles, sinks, and sources.

- **[[Thm - Gauss-Bonnet Theorem for Surfaces]]**
	- For a closed oriented surface $M$ (with or without an isometric embedding into $\mathbb{R}^3$), $\int_M K\, dA = 2\pi\chi(M)$. The right side depends only on the topology — the Euler characteristic $\chi(M) = 2 - 2g$ for an orientable closed surface of genus $g$. This is the prototypical "local-to-global" theorem: pointwise curvature integrates to a topological invariant, and no smooth deformation of the metric can change this integer (though it changes $K$ pointwise). The boundary-corrected form for surfaces with boundary or with corners involves geodesic curvature and exterior angles; the higher-dimensional generalisation is the Chern–Gauss–Bonnet theorem.

> [!tip] Unlocked: The Gauss–Bonnet–Chern Theorem *(from Gauge Theory II)*
> The two-dimensional Gauss–Bonnet integrates $K\, dA$. Its higher-dimensional generalisation, the **Gauss–Bonnet–Chern theorem**, integrates the **Pfaffian** of the curvature form of an even-dimensional Riemannian manifold and equals $\chi(M)$. Chern's 1944 proof works on the principal $SO(2n)$-bundle of orthonormal frames, expressing $\chi(M)$ as the integral of a polynomial in the curvature 2-form. This is the prototype "characteristic class" computation and the gateway to the **Atiyah–Singer index theorem**. See [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]].

- **[[Ex - Total Curvature of a Closed Surface via Gauss-Bonnet]]** (⭐⭐)
	- Apply Gauss–Bonnet to compute $\int_M K\, dA$ for the sphere, torus, and genus-$2$ surface, verifying $4\pi$, $0$, and $-4\pi$ respectively, and explain why no smooth deformation of these surfaces in $\mathbb{R}^3$ can change these totals.

- **[[Ex - Holonomy around a Spherical Cap is the Solid Angle]]** (⭐⭐)
	- On the unit $2$-sphere, the parallel-transport holonomy around the boundary of a spherical cap of solid angle $\Omega$ is a rotation by angle $\Omega$. This is the surface-level precursor of Gauss–Bonnet: $\int K\, dA = \Omega$ for the cap, and the rotation angle of parallel transport equals the integrated Gauss curvature.

> [!note] Exercise Index — §4.3
> [[Exercise Index - §4.3 Theorema Egregium and Gauss-Bonnet]]

## §4.4 Vector Fields, Minimal Surfaces, and Topology of Surfaces

- **[[Def - Geodesic Curvature]]**
	- The geodesic curvature vector $\vec\kappa_g = \nabla T/ds$ of a curve $C$ on $M$ (parametrised by arc length with unit tangent $T$) is the **tangential** projection of the ambient curvature vector $dT/ds$. Its magnitude $\kappa_g$ measures how much $C$ fails to be a [[Def - Geodesic|geodesic]]: a geodesic is precisely a curve with $\kappa_g \equiv 0$, so its tangent is parallel-transported along itself. Intrinsically, $\kappa_g$ is the rate at which the tangent direction turns within the tangent plane, measured relative to parallel transport.

- **[[Def - Minimal Surface]]**
	- A surface $M \subset \mathbb{R}^3$ is **minimal** if its mean curvature $H \equiv 0$ everywhere — equivalently if the first variation of area $\delta A$ vanishes for every compactly supported normal variation. The terminology is misleading: a minimal surface is only a *critical point* of area, not necessarily a minimum (it could be a saddle in the space of competitors). Soap films spanning a wire frame are equilibrium minimal surfaces (with $H = 0$ from $p_{\text{in}} - p_{\text{out}} = 0$); soap bubbles have constant $H \neq 0$ (Laplace's formula $\Delta p = -2\sigma H$). The plane, catenoid, helicoid, and Enneper surface are the classical embedded examples.

- **[[Def - Kronecker Index of a Vector Field]]**
	- For a continuous vector field $v$ on a closed oriented $n$-manifold $M$ with isolated zeros, the **Kronecker (Poincaré–Hopf) index** at an isolated zero $p$ is $\mathrm{Ind}_p(v) = \deg(v/|v| : S^{n-1}_\epsilon(p) \to S^{n-1})$ — the Brouwer degree of the unit-vector map on a small sphere around $p$. For a non-vanishing field defined on $\partial U$ for $U \subset \mathbb{R}^{n+1}$, the **Kronecker index of $v$ on $\partial U$** is $\deg(v/|v| : \partial U \to S^n)$. On a surface ($n=2$), $+1$ for sources, sinks, and centres; $-1$ for saddles; $\pm k$ for higher-order zeros. Indices add: the index over all of $\partial U$ is the sum of indices at the zeros inside $U$.

- **[[Thm - First Variation of Area]]**
	- For a smooth one-parameter family of surfaces $M(t)$ with $M(0) = M$ and normal variation field $v = \partial_t \mathbf{x}|_{t=0}$, the first variation of area is $\delta A = -\int_M H\, \langle v, N\rangle\, dA + \int_{\partial M} \langle v, n\rangle\, ds$, where $H$ is the mean curvature and $n$ the outward conormal on $\partial M$. The surface integral identifies the mean curvature as the $L^2$-gradient of area, and the boundary term records how moving $\partial M$ changes area. Consequence: $M$ is minimal $\iff$ $\delta A = 0$ for all compactly supported variations $\iff$ $H \equiv 0$.

- **[[Thm - Poincare-Hopf Theorem for Surfaces]]**
	- For a vector field $v$ with isolated zeros on a closed oriented surface $M$, $\sum_p \mathrm{Ind}_p(v) = \chi(M)$. The sum depends only on the topology of $M$, not on the field $v$ — any two such fields have the same index sum. Combined with Gauss–Bonnet, this gives the unified picture: $\chi(M) = \sum_p\mathrm{Ind}_p(v) = (1/2\pi)\int_M K\, dA$, so vector-field indices and integrated curvature both compute the same topological invariant. The proof reduces by the index-additivity lemma to the model cases $\mathrm{Ind} = \pm 1$ on small discs.

> [!tip] Unlocked: The Hopf Index Theorem and Atiyah–Singer *(from Algebraic Topology III)*
> Poincaré–Hopf for arbitrary $n$-dimensional closed oriented manifolds reads $\sum \mathrm{Ind}_p(v) = \chi(M)$ exactly the same way. The general statement, with $\chi(M) = \sum_k (-1)^k \dim H^k(M)$ on the right, is the prototype "index = topology" formula, and the **Atiyah–Singer index theorem** generalises this to elliptic operators on vector bundles, with the analytic index equal to a topological index built from characteristic classes. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

- **[[Ex - The Catenoid is a Minimal Surface]]** (⭐)
	- The catenoid $\mathbf{x}(u, v) = (a\cosh(v/a)\cos u,\, a\cosh(v/a)\sin u,\, v)$ has $H \equiv 0$. Compute $\kappa_1, \kappa_2$ explicitly and verify they sum to zero — this is the prototype embedded minimal surface, the only nonplanar surface of revolution that is minimal.

- **[[Ex - The Helicoid is Minimal]]** (⭐⭐)
	- The helicoid $\mathbf{x}(u, v) = (v\cos u, v\sin u, au)$ has $H \equiv 0$ everywhere. Verify by computing the principal curvatures, and remark that the helicoid is the unique nontrivial ruled minimal surface (Catalan's theorem) and is locally isometric to the catenoid under a one-parameter Bonnet deformation.

- **[[Ex - Hairy Ball Theorem from Poincare-Hopf]]** (⭐⭐)
	- Use Poincaré–Hopf to conclude that no continuous nowhere-vanishing tangent vector field exists on $S^2$: since $\chi(S^2) = 2 \neq 0$, every vector field has a zero, and one can derive $\chi(S^2) = 2$ by direct computation from the index sum of any concrete field (e.g., the "flow toward the north pole" with index $+1$ at south pole and $+1$ at north pole).

> [!note] Exercise Index — §4.4
> [[Exercise Index - §4.4 Vector Fields and Topology of Surfaces]]

---

# Sources and Targets

**Targets — What do we usually try to prove?** Five recurring goals dominate the chapter. (1) **Compute a curvature** — $K$, $H$, $\kappa_1$, $\kappa_2$ — for a specific surface, either from the parametrisation $(g_{\alpha\beta}, b_{\alpha\beta})$ formulae or from the intrinsic $K = R_{1212}/\det g$ when only the metric is known. (2) **Identify a critical point of area** — verify that a candidate surface is minimal ($H = 0$) or has constant mean curvature (a soap bubble), with the first-variation formula doing the work. (3) **Extract a topological invariant from geometry** — apply Gauss–Bonnet to deduce $\chi(M)$ from $\int K\, dA$, or apply Poincaré–Hopf to deduce $\chi(M)$ from the indices of any one vector field. (4) **Recognise rigidity or non-rigidity** — show two surfaces are or are not locally isometric by comparing $K$ (or its derivatives), the Theorema Egregium being the basic tool that detects bending-without-stretching. (5) **Compute a Brouwer degree** — for the Gauss normal map on a closed surface, for a polynomial map on the Riemann sphere (whose degree equals the polynomial's degree, giving the fundamental theorem of algebra), or for the Gauss linking integral of two disjoint loops in $\mathbb{R}^3$.

**Sources — What assumptions do we usually leverage?** Five recurring inputs route into these targets. (1) **A parametrisation $F : U \to \mathbb{R}^3$** with $F_*$ of rank $2$ — gives explicit $\mathbf{x}_\alpha, \mathbf{x}_{\alpha\beta}, N$ and hence direct formulae for $g_{\alpha\beta}, b_{\alpha\beta}, K, H$. The graph form $z = f(x, y)$ is the most common special case. (2) **Symmetry of the surface** — rotational symmetry (surfaces of revolution), constant Gauss curvature (the model spaces $\mathbb{R}^2, S^2, \mathbb{H}^2$), or constant mean curvature (planes, spheres, bubbles) drastically reduces computations and allows ODE reduction of the structural equations. (3) **Closedness and orientability of $M$** — these are the hypotheses for both Gauss–Bonnet and Poincaré–Hopf, so any topological-invariant computation begins by checking them. (4) **A choice of unit normal $N$** — required to define $\mathrm{II}$, $S$, $H$, the Gauss map; signs of $H$ and the orientation of the Gauss map all depend on this choice. (5) **A variation field $v$** — for variational problems (minimality, area extremisation), the first-variation formula needs the data $v$ along $M$ and the boundary behaviour.

**Routes.** Source (1) (parametrisation) routes directly to Target (1) (curvature computation) via the direct formulae. Source (2) (symmetry) routes to Target (4) (rigidity) via Theorema Egregium: surfaces of revolution with the same $K(r)$ profile are locally isometric. Source (3) (closed, oriented) routes to Targets (3) and (5) via Gauss–Bonnet, Poincaré–Hopf, and degree theory — the closedness is precisely what makes the integrals topological. Source (5) (variation) routes to Target (2) (criticality of area) via the first-variation formula, the geometric content being that $H$ is the $L^2$-gradient of area.

---

# Legal Operations

The legal operations of classical surface theory split into computational moves (manipulating $g_{\alpha\beta}, b_{\alpha\beta}, \kappa_1, \kappa_2$), variational moves (computing $\delta A$ and friends), and topological moves (degree, indices, integration of curvature over closed surfaces).

**Legal operations:**

1. **Compute $(g_{\alpha\beta}, b_{\alpha\beta})$ from a parametrisation $F : U \to \mathbb{R}^3$.** Given $\mathbf{x}(u, v) = F(u, v)$, compute $\mathbf{x}_u, \mathbf{x}_v$ and then $\mathbf{x}_{uu}, \mathbf{x}_{uv}, \mathbf{x}_{vv}$. The first fundamental form components are $E = \langle\mathbf{x}_u, \mathbf{x}_u\rangle$, $F = \langle\mathbf{x}_u, \mathbf{x}_v\rangle$, $G = \langle\mathbf{x}_v, \mathbf{x}_v\rangle$. The unit normal is $N = (\mathbf{x}_u \times \mathbf{x}_v)/|\mathbf{x}_u \times \mathbf{x}_v|$, and the second fundamental form components are $e = \langle\mathbf{x}_{uu}, N\rangle$, $f = \langle\mathbf{x}_{uv}, N\rangle$, $g_{\mathrm{II}} = \langle\mathbf{x}_{vv}, N\rangle$. *Trigger:* a parametrised surface and the need to compute $K$ or $H$. *Pattern:* "compute six dot products, two cross products, take ratios". See [[Ex - Gauss Curvature of the Sphere of Radius R is 1 over R Squared]] for the prototype.

2. **Use the determinant ratio formula $K = (eg_\mathrm{II} - f^2)/(EG - F^2)$.** Once $(E, F, G, e, f, g_\mathrm{II})$ are in hand, the Gauss curvature is $K = \det(b_{\alpha\beta})/\det(g_{\alpha\beta})$. This is the fastest computational route to $K$. The corresponding formula for the mean curvature is $H = (Eg_\mathrm{II} - 2Ff + Ge)/(EG - F^2)$ — symmetric in the metric components. *Trigger:* fundamental forms already computed. *Pattern:* "two determinants, take ratio; symmetric formula for $H$".

3. **Apply Theorema Egregium for intrinsic problems.** When only the metric $g_{\alpha\beta}$ is known — perhaps because the surface is given as an abstract Riemannian $2$-manifold without an embedding — compute $K$ via $K = R_{1212}/\det g$, where $R_{1212}$ is the unique non-redundant Riemann tensor component computed from the Christoffel symbols (8.32) of $g$. *Trigger:* an abstract metric, or two surfaces suspected to be isometric. *Pattern:* "compute $\Gamma^\gamma_{\alpha\beta}$, then $R^\tau_{\alpha\gamma\beta}$, then $K$ from the single component $R_{1212}$".

4. **Compute the Brouwer degree by counting signed preimages of a regular value.** Pick a regular value $y \in V^n$, find all preimages $\phi^{-1}(y)$ (a finite set by compactness + regularity), and add up the signs $\pm 1$ depending on whether $\phi_*$ is orientation-preserving at each preimage. *Trigger:* a map between closed oriented manifolds of the same dimension, needing its degree. *Pattern:* "find a generic-looking $y$; the preimages are countable saddles, sources, sinks; tally signs". For the Gauss map on a closed surface, this gives $\deg(N) = 1 - g$.

5. **Compute the Kronecker index of a vector field at a zero.** Excise a small disc around the isolated zero $p$, restrict to the boundary circle, normalise to a unit field, and read off the degree (winding number) of the map $\partial B_\epsilon(p) \to S^1$. For the standard zero types: sink and source give $+1$, saddle gives $-1$, dipole or higher-order gives $\pm 2$. *Trigger:* a vector field with isolated zeros, needing topological information. *Pattern:* "shrink onto a circle, count winds".

6. **Apply Gauss–Bonnet for global integrals.** For a closed oriented surface $M$, the integral $\int_M K\, dA$ equals $2\pi\chi(M)$ — known from the genus alone. Conversely, an integral $\int_M f(K, H)\, dA$ that can be reduced to $\int K\, dA$ via algebraic manipulation immediately gives a topological invariant. *Trigger:* an integral of curvature on a closed surface. *Pattern:* "if the integrand is $K$ (or reduces to it), the answer is $2\pi\chi(M)$".

7. **Apply Poincaré–Hopf for vector-field index sums.** For any vector field with isolated zeros on a closed oriented surface, the sum of indices is $\chi(M)$. So to compute $\chi(M)$ one can pick any convenient vector field (gradient of a Morse function, generator of a circle action) and add indices; or to prove a vector field must have a zero, observe $\chi(M) \neq 0$. *Trigger:* a closed orientable surface and a vector field, or a question about whether a non-vanishing field exists. *Pattern:* "pick any field, count indices; equals $\chi(M) = 2 - 2g$".

8. **Compute the first variation of area via $\delta A = -\int H\, \langle v, N\rangle\, dA + \text{boundary}$.** To test whether a surface is critical for the area functional, choose a variation field $v$ vanishing on $\partial M$ and apply the formula. Vanishing of $\delta A$ for all such $v$ is equivalent to $H \equiv 0$, by the fundamental lemma of the calculus of variations. *Trigger:* a variational problem in surface theory. *Pattern:* "isolate the integrand against the variation; demand it vanish".

9. **Identify principal directions via the eigenvector equation $b^\alpha_{\;\beta} T^\beta = \kappa T^\alpha$.** The principal directions diagonalise the shape operator. Equivalently they solve $(b_{\alpha\beta} - \kappa g_{\alpha\beta})T^\beta = 0$. At an umbilic ($\kappa_1 = \kappa_2$) every direction is principal; away from umbilics the two directions are orthogonal and unique. *Trigger:* a surface and the need for the principal frame. *Pattern:* "the $2 \times 2$ eigenvalue problem $\det(b - \kappa g) = 0$".

10. **Use intrinsic-derivative bookkeeping $\nabla X/dt = (dX/dt)_{\text{tangential}}$ for parallel transport.** A vector field $X$ tangent to $M$ along a curve is parallel-transported precisely when $\nabla X/dt = 0$ — i.e., $dX/dt$ is everywhere normal to $M$. To compute parallel transport along $C$, integrate $\dot X^\gamma + \Gamma^\gamma_{\alpha\beta}\dot u^\alpha X^\beta = 0$ with given initial vector. *Trigger:* a curve on a surface and the need to compare tangent vectors at distant points. *Pattern:* "set up the ODE in components; integrate; the result depends on the path".

**Illegal but tempting operations:**

> [!warning] 1. Assuming $H$ is intrinsic because $K$ is.
> Theorema Egregium proves that $K$ is intrinsic, but it is *only* $K$ — not $H$, not $\kappa_1$, not $\kappa_2$ individually. **Counterexample:** the flat plane has $H = 0$, while the cylinder (which is isometric to the plane) has $H = -1/a \neq 0$ with the outward normal. Both have $K = 0$, consistent with Theorema Egregium. The mean curvature depends on the embedding, and bending a flat sheet into a cylinder changes $H$ without violating any intrinsic invariant. **Repair:** $H$ is an extrinsic invariant — to compare it across surfaces you need to compare embeddings, not just metrics. The intrinsic analogue is the *scalar curvature* $R$, which in dimension $2$ is $R = 2K$ (intrinsic).

> [!warning] 2. Concluding $K > 0$ from $H > 0$ (or even $H \neq 0$).
> The mean curvature $H$ controls "average curving" but does not control sign of either principal curvature. **Counterexample:** the saddle $z = xy$ near the origin has principal curvatures of opposite sign at the origin (it is a saddle), so $K = \kappa_1\kappa_2 < 0$, while $H = \kappa_1 + \kappa_2$ can be made $0$ (it is in fact $0$ at the origin) or positive at nearby points. **Repair:** the sign of $K$ classifies the shape (elliptic/hyperbolic/parabolic), and the only way to read $K$ from $H$ alone is via the inequality $K \leq H^2/4$ (from $\kappa_1\kappa_2 \leq ((\kappa_1+\kappa_2)/2)^2$), which becomes equality only at umbilics. So $H \neq 0$ tells you nothing about whether $K$ is positive, zero, or negative.

> [!warning] 3. Applying Gauss–Bonnet to a non-closed or non-orientable surface and forgetting the boundary terms.
> The formula $\int_M K\, dA = 2\pi\chi(M)$ requires $M$ closed (compact, no boundary) and orientable. **Counterexample:** for a hemisphere of $S^2$ (radius $1$), $\int K\, dA = 2\pi$, while $\chi(\text{hemisphere}) = 1$, so $2\pi\chi = 2\pi$ matches the bulk integral *only by coincidence* — the boundary geodesic-curvature integral is $\int_{\partial M}\kappa_g\, ds = 0$ since the equator is a geodesic. For a disc cut out of the sphere by a non-geodesic latitude, $\int_{\partial M}\kappa_g\, ds \neq 0$ and one must include it. For the Möbius strip, the formula has no orientable version at all. **Repair:** use the boundary-and-corners form: $\int_M K\, dA + \int_{\partial M}\kappa_g\, ds + \sum(\pi - \text{exterior angles}) = 2\pi\chi(M)$.

> [!warning] 4. Confusing "minimal" with "minimum-of-area".
> A minimal surface has $H \equiv 0$ — it is a *critical point* of area, not necessarily a minimum. **Counterexample:** the catenoid spanning two coaxial circles is minimal, but for circles spaced more than a critical distance apart, the catenoid becomes a *saddle point*, and the area-minimising surface is a pair of discs (the Goldschmidt solution) — disconnected, not embedded as a smooth surface. Soap films do find local minima, but unstable minimal surfaces exist mathematically and cannot be realised as soap films. **Repair:** for a true minimum, examine the *second* variation: a minimal surface is stable iff the second variation is non-negative for all compactly supported variations, which translates into a Jacobi-operator spectral condition.

> [!warning] 5. Computing the index of a vector field zero by hand-waving.
> "It looks like a saddle, so the index is $-1$" is unreliable for higher-order zeros. **Counterexample:** the field $v(z) = z^2$ on $\mathbb{R}^2 = \mathbb{C}$ has a zero at the origin that looks superficially like a "double sink" — but its index is $+2$, not $+1$ (the unit-vector map $z/|z| \mapsto (z/|z|)^2$ has degree $2$). For $v(z) = z^n$, the index is $n$; for $v(z) = \bar z^n$, it is $-n$. **Repair:** always compute the degree of the unit-vector map on a small circle around the zero. For a holomorphic field $f(z)\partial_z$, the index at an isolated zero equals the algebraic order of vanishing of $f$.

> [!warning] 6. Forgetting that the Gauss map's degree depends on the choice of normal.
> Reversing the normal $N \to -N$ reverses the orientation of the Gauss map, hence changes $\deg(N)$ by a sign. **Counterexample:** for the standard $S^2$ with outward normal, $N : S^2 \to S^2$ is the identity with $\deg = +1$; with inward normal, $N$ is the antipodal map with $\deg = -1$. The Gauss–Bonnet integral $\int K\, dA$ is *unchanged* because $K$ itself is unchanged by reversing $N$ (it is the product $\kappa_1\kappa_2$, both signs flip). **Repair:** in the formula $\int K\, dA = 4\pi\deg(N)$, the $\deg(N)$ side acquires a sign $\pm 1$ depending on the normal convention; for the *outward* normal on a closed surface bounding a region of $\mathbb{R}^3$, the sign is fixed and the formula reads $\int K\, dA = 2\pi\chi(M)$, consistent with both conventions.

---

# Problem-Solving Strategy

Problems in classical surface theory split into three large families, and recognising which family a problem belongs to is half the work.

The first family is **direct computation of curvature for a specific surface**. A parametrisation $F(u, v)$ is given; the goal is to extract $E, F, G, e, f, g_\mathrm{II}, \kappa_1, \kappa_2, K, H$. The route is mechanical: compute first derivatives $\mathbf{x}_u, \mathbf{x}_v$, then $E = |\mathbf{x}_u|^2$, $G = |\mathbf{x}_v|^2$, $F = \mathbf{x}_u \cdot \mathbf{x}_v$; cross-product gives $\mathbf{x}_u \times \mathbf{x}_v$ and hence $N = (\mathbf{x}_u \times \mathbf{x}_v)/\sqrt{EG - F^2}$; second derivatives $\mathbf{x}_{uu}, \mathbf{x}_{uv}, \mathbf{x}_{vv}$ dotted with $N$ give $e, f, g_\mathrm{II}$; the formulae $K = (eg_\mathrm{II} - f^2)/(EG - F^2)$ and $H = (Eg_\mathrm{II} + Ge - 2Ff)/(EG - F^2)$ deliver the answer. For graph-of-function surfaces $z = f(x, y)$, the compact formula $K = (f_{xx}f_{yy} - f_{xy}^2)/(1 + f_x^2 + f_y^2)^2$ from problem 8.2(5) of Frankel saves work. The trigger for this family is "compute $K$" or "verify minimality" on a concrete parametrised surface.

The second family is **variational and minimality problems**. The goal is to verify or construct surfaces minimising area or having constant mean curvature. The first-variation formula is the only tool: write the variation as $\delta\mathbf{x} = v$, separate into normal and tangential components, apply $\delta A = -\int H\,\langle v, N\rangle\, dA + \int_{\partial M}\langle v, n\rangle\, ds$, and use the fundamental lemma of the calculus of variations to read off the Euler–Lagrange equation. The triggers are "show $M$ is critical for area" (verify $H = 0$ directly), "soap bubble" or "constant pressure" (verify $H = \text{const}$), or "minimal-surface equation in graph form" (verify the PDE $(1+f_y^2)f_{xx} - 2f_xf_yf_{xy} + (1+f_x^2)f_{yy} = 0$).

The third family is **topological-invariant computations**, where the surface is closed and oriented and the goal is a $\mathbb{Z}$-valued invariant. There are two routes: Gauss–Bonnet ($\int K\, dA = 2\pi\chi(M)$) and Poincaré–Hopf ($\sum\mathrm{Ind}_p(v) = \chi(M)$). Either reduces the problem to a topological count. For $\chi(M) = 2 - 2g$ on an orientable closed surface of genus $g$, the answer is $4\pi(1 - g)$ for the curvature integral and a known integer for any concrete vector field. The trigger is "closed orientable surface + a global integer should appear" — and the strategy is "any way you compute it, you get $\chi(M)$".

A meta-strategy: **every question in this chapter is a balance between intrinsic and extrinsic**. Theorema Egregium says $K$ crosses the divide; everything else (Brouwer degree, Gauss–Bonnet) shows that crossings between local geometry and global topology happen along very specific channels. When a problem mixes the two pictures, ask first whether the intrinsic version is true (e.g., does the result depend only on the metric?), then whether the extrinsic embedding adds new information (e.g., signs from the normal, integer-degree information from the Gauss map). The whole chapter is the question "what survives bending without stretching?", and the answer is the intrinsic geometry plus topology of $M$.

---

# Most Reusable Properties

- **[[Thm - Theorema Egregium of Gauss|Theorema Egregium]]**: $K = R_{1212}/\det g$ is intrinsic. **Typical use:** detect that two metrics with different $K$ profiles cannot be locally isometric; identify $K$ as the right notion of two-dimensional curvature for abstract Riemannian manifolds (no embedding required); compute $K$ from the metric alone when no embedding is convenient (the hyperbolic plane in the upper-half-plane model is the standard example).

- **[[Thm - Gauss-Bonnet Theorem for Surfaces|Gauss–Bonnet theorem]]**: $\int_M K\, dA = 2\pi\chi(M)$. **Typical use:** convert a curvature integral on a closed surface into a topological count; conclude that no closed surface of positive total curvature can have genus $\geq 1$ (so the sphere is rigid in this sense); prove the existence of "positively curved patches" on any surface of positive Euler characteristic; control the energy of harmonic-map problems by Euler-characteristic bounds.

- **[[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf theorem]]**: $\sum\mathrm{Ind}_p(v) = \chi(M)$. **Typical use:** show a tangent vector field on $S^2$ must have a zero (hairy ball); compute $\chi(M)$ by picking a convenient field (gradient of a height function in Morse theory, where index sums recover Euler characteristic via the Morse inequalities); detect critical points of smooth functions on closed surfaces.

- **[[Def - Shape Operator (Weingarten Map)|The shape operator $S = -dN$ is self-adjoint]]**. **Typical use:** invoke the spectral theorem to diagonalise $S$ at every point (principal curvatures, orthogonal principal directions); reduce surface-theory problems to two-by-two linear algebra at each point; identify $K = \det S$ and $H = \mathrm{tr}\, S$ as the basic invariants of $S$ at a point.

- **[[Thm - First Variation of Area|First variation of area]]**: $\delta A = -\int H\,\langle v, N\rangle\, dA + \text{boundary}$. **Typical use:** identify $H$ as the $L^2$-gradient of area; derive the minimal-surface equation $H = 0$ from variational principles; conclude that any area-extremising surface (with fixed boundary) must have $H = 0$; derive Laplace's pressure formula $\Delta p = -2\sigma H$ for soap films and bubbles.

---

# Bridges

1. **To abstract Riemannian geometry ([[Riemannian Geometry I — Connections and Covariant Differentiation|connections]] and [[Riemannian Geometry III — Riemann Curvature and Topology|curvature]]).** The intrinsic derivative $\nabla T/dt$ on a surface in $\mathbb{R}^3$, defined as the tangential projection of $dT/dt$, is *exactly* the [[Def - Levi-Civita Connection|Levi-Civita covariant derivative]] of the induced metric. Equation (8.42) of Frankel — $\nabla X^\gamma/dt = dX^\gamma/dt + \Gamma^\gamma_{\beta\alpha}X^\alpha\, du^\beta/dt$ — is the same formula one writes on an abstract Riemannian manifold, and the Christoffel symbols (8.32) are the metric-only formula that makes the connection unique. This is the historical sequence: Christoffel (1869) wrote the formula intrinsically without knowing it was a "connection"; Levi-Civita (1918) re-interpreted it as the tangential part of the Euclidean derivative for embedded surfaces; the abstract notion of an [[Def - Affine Connection on a Vector Bundle|affine connection on a vector bundle]] arose only later. The surface case is the special case to which the whole later abstract development reduces.

2. **To the [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet|Chern–Gauss–Bonnet–Chern theorem]].** The two-dimensional Gauss–Bonnet integrates $K$ on a closed surface. Chern's generalisation works on a closed Riemannian $2n$-manifold and integrates the **Pfaffian of the curvature form** — a degree-$n$ polynomial in the components of the Riemann tensor, normalised so that the integral equals $\chi(M)$. The construction lives on the $SO(2n)$-principal bundle of orthonormal frames, not on $M$ itself; on $M$ it descends to a closed $2n$-form representing the Euler class. The surface case is the case $n = 1$, where the Pfaffian collapses to $K/2\pi$ times the area element. The link to characteristic classes is the bridge to **Atiyah–Singer index theory**, where every elliptic operator's analytical index is computed as an integral of characteristic classes — the most expansive generalisation of Gauss–Bonnet known.

3. **To the [[Algebraic Topology II — Fundamental Group and Covering Spaces|fundamental group and covering theory]].** The Gauss–Bonnet integral controls the average curvature, and via **Bonnet–Myers** in [[Riemannian Geometry III — Riemann Curvature and Topology|Riemannian Geometry III]] this controls the diameter of the universal cover, hence the fundamental group: positive Ricci curvature bounded below forces finite $\pi_1$. On a closed surface, $\chi(M) > 0$ forces $g = 0$ (sphere or $\mathbb{RP}^2$) which forces $|\pi_1| \leq 2$; $\chi(M) = 0$ allows the torus and Klein bottle (infinite $\pi_1$); $\chi(M) < 0$ requires higher-genus surfaces with hyperbolic $\pi_1$. So Euler characteristic, total curvature, and the size of $\pi_1$ are linked through Gauss–Bonnet plus comparison geometry.

4. **To [[Complex Analysis I — Basic Notions|complex analysis]].** A polynomial map $P : \mathbb{C} \to \mathbb{C}$ of degree $n$ extends to a smooth map $P : \mathbb{CP}^1 \to \mathbb{CP}^1$ between Riemann spheres. The Brouwer degree of this map, computed by the count of preimages of a generic value, equals $n$ — and since a nonzero-degree map between compact manifolds is surjective, every nonconstant polynomial $P$ takes the value $0$. This is the **fundamental theorem of algebra** via degree theory, the most conceptually clean proof. The same machinery (degree of a holomorphic self-map of $\mathbb{CP}^1$) generalises to the Riemann–Hurwitz formula counting ramification points of holomorphic maps between Riemann surfaces.

5. **To **electromagnetism** and the Gauss looping integral.** Gauss's linking integral $\mathrm{Lk}(C_1, C_2) = (1/4\pi)\int_{C_1}\int_{C_2}\mathbf{r}_{12} \cdot (d\mathbf{r}_1 \times d\mathbf{r}_2)/|\mathbf{r}_{12}|^3$ is mathematically the Brouwer degree of the map $T^2 \to S^2$, $(\theta, \phi) \mapsto \mathbf{r}_{12}(\theta, \phi)/|\mathbf{r}_{12}|$. Physically it is **Ampère's law**: a unit current in $C_2$ generates a magnetic field $\mathbf{B}$ at $C_1$ given by Biot–Savart, and $\oint_{C_1}\mathbf{B} \cdot d\mathbf{r}_1$ counts the linking. This is the surface-level precursor of the modern Chern–Simons / knot-theory connection (Witten, 1989), where partition functions of $3$-dimensional gauge theory compute knot invariants — see [[Gauge Theory IV — Yang–Mills Fields and Instantons]].

6. **To variational PDE / **Plateau problem** / **mean curvature flow****. The first-variation formula $\delta A = -\int H\,\langle v, N\rangle\, dA$ identifies $-H N$ as the $L^2$-gradient of the area functional on the space of embedded surfaces. The **Plateau problem** — find a surface of least area spanning a given Jordan curve in $\mathbb{R}^3$ — is the prototypical variational problem in geometric analysis; Douglas (1931) and Radó solved it for embedded discs, Federer–Fleming developed geometric measure theory to handle topological complications, and **minimal-surface theory** became one of the central branches of nonlinear PDE. **Mean curvature flow** evolves a surface by $\partial_t \mathbf{x} = H N$ — the steepest-descent gradient flow of area — and is the geometric analogue of the heat equation; it concentrates singularities ("neck-pinches") and is fundamental in **Hamilton's Ricci flow** approach to the Poincaré conjecture (Perelman, 2002).

---

# Insights

**The unifying frame** of the chapter is the *two-form duality* between intrinsic and extrinsic geometry. Two symmetric $2$-tensors on $M$ encode everything: the first fundamental form $g_{\alpha\beta}$ (intrinsic, the metric), and the second fundamental form $b_{\alpha\beta}$ (extrinsic, the embedding into $\mathbb{R}^3$). Both are derived from a single piece of ambient data — the position vector $\mathbf{x}$ and its first and second derivatives — but they separate into the intrinsic and extrinsic halves of surface theory cleanly. Theorema Egregium says these halves talk to each other in exactly one way: the determinant ratio $K = \det b/\det g$ is intrinsic, while every other invariant (the trace $H$, the eigenvalues $\kappa_1, \kappa_2$ individually) genuinely depends on the embedding. So the deep slogan is: "intrinsic geometry equals first fundamental form; extrinsic geometry equals second fundamental form modulo the determinant".

**The true name of the Gauss curvature** is *the local-to-global ratio*: $K(p) = \lim_{U \to p}(\text{signed area of }N(U))/\text{area of }U$, the Jacobian of the Gauss normal map. This is Gauss's own definition, and it makes the global content of $\int K\, dA = 4\pi\deg(N) = 2\pi\chi(M)$ feel inevitable rather than miraculous: the integral is just "$4\pi$ times how many times $N$ wraps $M$ around $S^2$", and that wrapping number is forced by topology. Computational formulae like $K = (eg_\mathrm{II} - f^2)/(EG - F^2)$ are workhorses, but they hide the geometry; the local-to-global form makes the topological meaning visible.

**A trigger-reaction pattern** that pervades the chapter: *"closed oriented surface + curvature integral" $\Rightarrow$ Gauss–Bonnet*. Almost every problem of the form "compute $\int_M f(K)\, dA$ on a closed surface" reduces, via Gauss–Bonnet plus a little algebra, to $\chi(M)$ times something. Likewise, *"vector field on a closed surface" $\Rightarrow$ Poincaré–Hopf*: any global topological count is forced by $\chi(M)$, and any well-posed local-vs-global problem in this chapter has $\chi(M)$ as the eventual right-hand side. Internalising "every global integer on a closed surface comes from $\chi$" is the single most useful pattern in the chapter.

**An inheritance observation.** The intrinsic-derivative formula $\nabla X/dt = (dX/dt) - \langle dX/dt, N\rangle N$ inherits its properties from the Euclidean derivative of $\mathbb{R}^3$: tangential projection of a Leibniz-respecting operation is itself Leibniz-respecting, tangential projection of a linear operation is linear, and so on. This is why parallel transport on a surface is the *same operation* as parallel transport in flat $\mathbb{R}^3$, just with the result corrected to lie in the tangent plane. The abstract Riemannian-manifold definition of connection is essentially "what is the operation that *would* be the tangential projection of a Euclidean derivative, if we had an embedding?" — and the Fundamental Theorem of Riemannian Geometry says the answer is unique (the Levi-Civita connection), determined by the metric alone.

**A historical aside that illuminates.** Gauss's *Disquisitiones generales circa superficies curvas* (1827) presented the Theorema Egregium as a "remarkable theorem" — and *remarkable* it was: Gauss was studying surface theory for very practical reasons (he was conducting a geodetic survey of the kingdom of Hannover) and discovered, almost by accident, that one specific combination of his measurements survived the rolling of a flexible measuring tape. The discovery led directly to Riemann's 1854 lecture, where the question "what *is* curvature?" — intrinsically defined, without an ambient space — was posed and answered for general $n$-manifolds. The whole of modern differential geometry, including general relativity (where there *is* no ambient space and $K$-style intrinsic curvature is the only available notion), is the answer to a question that started with a measuring tape on a hill.

**A second forward observation.** The chapter's two great theorems — Gauss–Bonnet (curvature $\to$ topology) and Poincaré–Hopf (vector-field zeros $\to$ topology) — are both special cases of the **Chern–Gauss–Bonnet theorem** in higher dimensions, and ultimately of the **Atiyah–Singer index theorem** for elliptic operators. The pattern "local geometric quantity integrates to a topological integer" is one of the central organising principles of twentieth-century mathematics; the surface case is the cleanest place to internalise it before moving to characteristic classes, Chern–Simons theory, and the modern picture of **topological invariants of fibre bundles** developed in [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]] and [[Algebraic Topology III — Higher Homotopy and Chern Forms]].
