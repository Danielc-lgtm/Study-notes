---
type: topic
subject: riemannian-geometry
chapter: "3.1-3.4"
title: "Riemannian Geometry III — Riemann Curvature and Topology: Synge, Bonnet–Myers, Cartan–Hadamard"
tags: [geometry, riemannian-geometry, curvature]
---

# Notation Registry

A standing convention for this topic: **$(M, g)$ is a smooth, connected, paracompact Riemannian manifold of dimension $n$, and $\nabla$ denotes its unique [[Riemannian Geometry I — Connections and Covariant Differentiation|Levi-Civita connection]]** — the torsion-free, metric-compatible affine connection on $TM$. All Lie brackets, exterior derivatives, and pullbacks are the usual ones from [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket|smooth manifold theory]]. Sign conventions are convention-sensitive: we use the **Lee / do Carmo / Frankel** sign for the Riemann tensor,

$$R(X, Y)Z := \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]}Z.$$

Some texts (notably Petersen and older Russian literature) use the opposite sign. Sectional curvature $K(X, Y) = \langle R(X, Y)Y, X\rangle / (|X|^2|Y|^2 - \langle X, Y\rangle^2)$ comes out positive for the round sphere in our convention.

> [!warning] Convention: index placement in $R^a_{\;bcd}$
> Different sources permute the four indices of the Riemann tensor differently. We use $R(\partial_c, \partial_d)\partial_b = R^a_{\;bcd}\partial_a$, so $\Omega^a_b = \tfrac{1}{2}R^a_{\;bcd}\,\omega^c \wedge \omega^d$. Frankel writes $R^i_{\;jkl}$ with $k, l$ in the same position; Lee writes $R^l_{\;ijk}$ but with the same geometric content. Always check a source's first line.

- $\nabla$ — the [[Def - Levi-Civita Connection|Levi-Civita connection]] (torsion-free, metric-compatible)
- $R$ — the **[[Def - Riemann Curvature Tensor|Riemann curvature tensor]]**, a $(1,3)$-tensor $R(X, Y)Z$
- $R(X, Y, Z, W) = \langle R(X, Y)Z, W\rangle$ — the purely covariant $(0,4)$ Riemann tensor
- $R^a_{\;bcd}$ — components of $R$ in a local frame: $R(\partial_c, \partial_d)\partial_b = R^a_{\;bcd}\partial_a$
- $R_{abcd} = g_{ae} R^e_{\;bcd}$ — components of the covariant Riemann tensor
- $\sigma = \mathrm{span}(X, Y) \subset T_pM$ — a $2$-plane in a tangent space
- $K(\sigma) = K(X, Y) = \langle R(X, Y)Y, X\rangle / (|X|^2|Y|^2 - \langle X, Y\rangle^2)$ — the **[[Def - Sectional Curvature|sectional curvature]]** of the plane $\sigma$
- $\mathrm{Ric}(X, Y) = \mathrm{tr}(Z \mapsto R(Z, X)Y) = R^a_{\;XaY}$ — the **[[Def - Ricci Tensor|Ricci tensor]]**, a symmetric $(0,2)$-tensor
- $\mathrm{Ric}_{ab} = R^c_{\;acb}$ — components of the Ricci tensor
- $S = \mathrm{tr}_g \mathrm{Ric} = g^{ab}\mathrm{Ric}_{ab} = R^{ab}_{\;\;ab}$ — the **[[Def - Scalar Curvature|scalar curvature]]**
- $\mathcal{R} : \Lambda^2 T_pM \to \Lambda^2 T_pM$ — the **[[Def - Curvature Operator|curvature operator]]**, the symmetric endomorphism of $2$-forms with $\langle \mathcal{R}(X \wedge Y), Z \wedge W\rangle = R(X, Y, W, Z)$
- $\omega^a, e_a$ — dual coframe and frame; the connection 1-forms $\omega^a_{\;b}$ satisfy $\nabla_X e_b = \omega^a_{\;b}(X)e_a$
- $\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c} \wedge \omega^c_{\;b}$ — the **curvature 2-forms** (Cartan's second structural equation)
- $K$ — sectional curvature; $\kappa$ — a constant lower bound on sectional curvature; $H^n$ — hyperbolic $n$-space
- $\exp_p : T_pM \to M$ — the [[Def - The Riemannian Exponential Map|exponential map]] at $p$
- $J$ — a [[Def - Jacobi Field|Jacobi field]] along a geodesic; satisfies $\nabla_T \nabla_T J + R(J, T)T = 0$
- $\pi_1(M)$ — the [[Def - Path-Product and the Fundamental Group|fundamental group]] of $M$
- $\mathrm{Iso}(M, g)$ — the group of isometries of $(M, g)$; a Lie group
- $X^\flat$ — the 1-form dual to a vector field $X$ via $g$; $\mathcal{L}_X g$ — Lie derivative of $g$

---

# Motivation

Here is the entire topic in one sentence: **curvature, an infinitesimal quantity, controls the global shape and topology of a Riemannian manifold**. We have spent the previous two chapters building the Levi-Civita connection and the [[Def - Geodesic|geodesics]] that come with it, and we have noticed in passing that the second derivative of parallel transport around an infinitesimal loop fails to close — the failure is encoded in a tensor, the Riemann curvature tensor $R$. This chapter argues that this purely local tensor secretly determines whether the manifold can be a sphere, whether it can have nontrivial fundamental [[Def - Group|group]], whether its geodesics can ever cross each other, and whether the exponential map at a point can be extended to a [[Def - Diffeomorphism|diffeomorphism]] onto the whole manifold. None of these are infinitesimal questions; all of them are answered by an integral over the manifold of the local Riemann tensor.

The phenomenon to keep in mind is the equatorial geodesic on the round sphere. It is a closed geodesic, satisfies the geodesic equation at every point, has length $2\pi$, and yet a slippery rubber band stretched along the equator can be made shorter by pushing it north toward a pole. The first variation of arc length vanishes — the equator really is a critical point — but the second variation is negative for the variation that pushes north. Synge worked out the precise formula in 1925: for a closed geodesic with parallel-transported normal variation field $J$, the second variation is

$$L''(0) = -\int_0^L K(T \wedge J)\, ds,$$

where $K(T \wedge J)$ is the [[Def - Sectional Curvature|sectional curvature]] of the $2$-plane spanned by the tangent and the variation. When $K > 0$, the integral is positive and $L''(0) < 0$ — the geodesic is unstable, the rubber band contracts. This single computation underlies essentially every comparison theorem in this chapter.

The structural backbone of the topic is the hierarchy of curvature invariants extracted from $R$, each weaker than the last:

$$\text{full Riemann tensor } R \;\supset\; \text{sectional curvatures } K(\sigma) \;\supset\; \text{Ricci tensor } \mathrm{Ric} \;\supset\; \text{scalar curvature } S.$$

The sectional curvatures determine $R$ (this is a small but useful theorem — see [[Thm - Sectional Curvature Determines the Riemann Tensor]]). The Ricci tensor is the trace of $R$ over one index pair, and the scalar curvature is its further trace. Each weaker invariant controls a weaker but still substantial class of theorems. **Sectional curvature** controls the [[Thm - Cartan-Hadamard Theorem|Cartan–Hadamard]] and [[Thm - Synge's Theorem|Synge]] theorems and most of comparison geometry. **Ricci curvature** controls the [[Thm - Bonnet-Myers Theorem|Bonnet–Myers]] diameter bound and Bochner-type vanishing theorems for harmonic forms. **Scalar curvature** controls **Yamabe-type problems** and the **positive mass theorem** of general relativity. The chapter is organised by walking down this hierarchy.

The three signature global theorems are the targets of the chapter. The [[Thm - Cartan-Hadamard Theorem|Cartan–Hadamard theorem]] says that on a simply-connected complete manifold with sectional curvature $\le 0$, the exponential map at any point is a diffeomorphism onto $M$; equivalently, $M$ is diffeomorphic to $\mathbb{R}^n$ via $\exp_p$. The [[Thm - Bonnet-Myers Theorem|Bonnet–Myers theorem]] says that if Ricci curvature satisfies $\mathrm{Ric} \ge (n-1)\kappa\, g$ with $\kappa > 0$, then the diameter of $M$ is at most $\pi/\sqrt{\kappa}$ and $\pi_1(M)$ is finite. [[Thm - Synge's Theorem|Synge's theorem]] says that an even-dimensional, compact, orientable manifold with positive sectional curvature is simply connected. All three theorems are proved by the same fundamental tool: the second variation of arc length, with curvature appearing through the Jacobi equation $\nabla_T\nabla_T J + R(J, T)T = 0$.

A final motivating remark. The three model spaces of constant curvature — the round sphere $S^n$ ($K = +1$), Euclidean space $\mathbb{R}^n$ ($K = 0$), and hyperbolic space $H^n$ ($K = -1$) — are the calibration points of the entire theory. Every comparison theorem can be read as "this manifold behaves no worse than the model space of the same constant curvature." Bonnet–Myers compares to the sphere, Cartan–Hadamard compares to Euclidean space, and the **Rauch and Toponogov comparison theorems** (forward references) compare triangles and Jacobi fields to those of the model space.

The reader is assumed to have worked through [[Differential Geometry I — Smooth Manifolds and Atlases|smooth manifolds]], [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket|vector fields and the Lie bracket]], [[Differential Geometry VII — Tensors and Tensor Fields|tensors and tensor fields]], [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds|Riemannian metrics]], and the two preceding Riemannian Geometry topics — [[Riemannian Geometry I — Connections and Covariant Differentiation]] for the Levi-Civita connection and Cartan structural equations, and [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]] for geodesics, the exponential map, Jacobi fields, and the second variation. The fundamental-group machinery is from [[Algebraic Topology II — Fundamental Group and Covering Spaces]], and we will use a single fact: a compact manifold has finite fundamental group if and only if its universal cover is compact.

---

# Concept Map

## §3.1 The Riemann Curvature Tensor

- **[[Def - Riemann Curvature Tensor]]**
	- The Riemann curvature tensor of a Riemannian manifold $(M, g)$ is the $(1, 3)$-tensor field $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z$, measuring the failure of the second covariant derivative to commute. Equivalently in the orthonormal-frame formulation, $R$ is the curvature 2-form of the Levi-Civita connection: $\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c}\wedge\omega^c_{\;b} = \tfrac{1}{2}R^a_{\;bcd}\,\omega^c\wedge\omega^d$. The vanishing of $R$ is exactly the condition for $(M, g)$ to be locally isometric to Euclidean space — the Levi-Civita connection is then flat, parallel transport is path-independent, and a local orthonormal frame of parallel vector fields exists. The Riemann tensor on $\mathbb{R}^n$ with the flat metric vanishes identically; on $S^n$ with the round metric, $R(X, Y)Z = \langle Y, Z\rangle X - \langle X, Z\rangle Y$.

- **[[Def - Curvature Operator]]**
	- The curvature operator $\mathcal{R} : \Lambda^2 T_pM \to \Lambda^2 T_pM$ is the symmetric linear endomorphism on bivectors uniquely determined by $\langle \mathcal{R}(X \wedge Y), Z \wedge W\rangle = R(X, Y, W, Z)$. This packages the Riemann tensor as a bilinear form on $2$-forms, manifesting the pair-swap symmetry $R(X, Y, Z, W) = R(Z, W, X, Y)$ explicitly. **Positive curvature operator** (a strong condition) implies positive sectional curvature (a much weaker condition), and conditions on $\mathcal{R}$ play a major role in **Hamilton–Brendle–Schoen sphere theorems** and in Ricci-flow proofs of the differentiable sphere theorem.

- **[[Thm - Symmetries of the Riemann Tensor]]**
	- The covariant Riemann tensor $R(X, Y, Z, W) = \langle R(X, Y)Z, W\rangle$ satisfies three algebraic symmetries: antisymmetry in the first pair $R(X, Y, Z, W) = -R(Y, X, Z, W)$ (manifest from the definition), antisymmetry in the second pair $R(X, Y, Z, W) = -R(X, Y, W, Z)$ (this requires metric compatibility of $\nabla$), and the pair-swap symmetry $R(X, Y, Z, W) = R(Z, W, X, Y)$ (this follows from the first Bianchi identity). These symmetries cut the $n^4$ components of $R$ down to $\tfrac{1}{12}n^2(n^2-1)$ independent components: $1$ in [[Def - Dimension|dimension]] $2$, $6$ in dimension $3$, $20$ in dimension $4$.

- **[[Thm - First and Second Bianchi Identities]]**
	- The first Bianchi identity, $R(X, Y)Z + R(Y, Z)X + R(Z, X)Y = 0$, is an algebraic identity following from $d^2 = 0$ on the soldering form $\sigma$ in Cartan's structural equations (equivalently, from the Jacobi identity for $\nabla$ in the torsion-free case). The second Bianchi identity, $(\nabla_E R)(X, Y)Z + (\nabla_X R)(Y, E)Z + (\nabla_Y R)(E, X)Z = 0$, is a differential identity following from $d\Omega + \omega \wedge \Omega - \Omega \wedge \omega = 0$. The second Bianchi identity, after two contractions, yields $\nabla_a (R^{ab} - \tfrac{1}{2}g^{ab}S) = 0$ — the divergence-freeness of the **[[Def - Einstein Manifold|Einstein tensor]]** $G_{ab} = \mathrm{Ric}_{ab} - \tfrac{1}{2}g_{ab}S$, the geometric reason why Einstein's field equations are consistent with conservation of energy-momentum.

> [!tip] Unlocked: Connection on a Principal Bundle *(from Gauge Theory III)*
> The Riemann curvature tensor is the curvature of the Levi-Civita connection on the frame bundle $\mathrm{Fr}(M)$, a principal $O(n)$-bundle. The components $R^a_{\;bcd}$ are exactly the components of the **$\mathfrak{o}(n)$-valued curvature 2-form** $\Omega$ on $\mathrm{Fr}(M)$ pulled back to $M$ via a local frame, and the Bianchi identities are special cases of the universal Bianchi identity $d^A\Omega = 0$ valid for any connection on any principal bundle. See [[Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections]].

> [!tip] Unlocked: Ricci Flow *(from Geometric Analysis)*
> The Riemann curvature tensor (specifically its trace, the Ricci tensor) drives the geometric heat equation $\partial_t g = -2\,\mathrm{Ric}(g)$, the **Ricci flow** introduced by Hamilton in 1982 and used by Perelman to prove the **Poincaré conjecture** and Thurston's **Geometrization theorem** for closed $3$-manifolds. The flow tends to homogenise curvature, and through it one can produce the canonical "geometric structure" guaranteed by Thurston's classification.

- **[[Ex - Computing the Riemann Tensor of S^2 from Cartan's Equations]]** (⭐⭐)
	- Using the orthonormal coframe $\sigma^1 = d\theta$, $\sigma^2 = \sin\theta\, d\varphi$ on the round 2-sphere, compute the connection 1-form $\omega^1_{\;2}$ and the curvature 2-form $\Omega^1_{\;2}$, and read off $R^1_{\;212} = 1$.

> [!note] Exercise Index — §3.1
> [[Exercise Index - §3.1 The Riemann Curvature Tensor]]

## §3.2 Sectional, Ricci, and Scalar Curvature

- **[[Def - Sectional Curvature]]**
	- The sectional curvature of a $2$-plane $\sigma = \mathrm{span}(X, Y) \subset T_pM$ is the scalar $K(\sigma) = \langle R(X, Y)Y, X\rangle / (|X|^2|Y|^2 - \langle X, Y\rangle^2)$. The denominator is the squared area of the parallelogram on $X, Y$, ensuring $K(\sigma)$ depends only on the $2$-plane $\sigma$, not on the choice of basis. Geometrically, $K(\sigma)$ is the Gauss curvature at $p$ of the $2$-dimensional totally geodesic surface formed by all geodesics emanating from $p$ tangent to $\sigma$. The sphere has $K \equiv +1$, Euclidean space has $K \equiv 0$, hyperbolic space has $K \equiv -1$.

- **[[Thm - Sectional Curvature Determines the Riemann Tensor]]**
	- The function $\sigma \mapsto K(\sigma)$ on $2$-planes uniquely determines the full Riemann tensor $R(X, Y, Z, W)$. Concretely, polarisation of the quadratic form $\langle R(X, Y)Y, X\rangle$ in $X$ and $Y$ recovers all components. This means that in any chapter where only sectional curvatures appear in hypotheses (Synge, Cartan–Hadamard, comparison theorems), no information is lost — the sectional curvatures are a complete description of curvature, even though they are scalar-valued.

- **[[Def - Ricci Tensor]]**
	- The Ricci tensor is the trace $\mathrm{Ric}(X, Y) = \mathrm{tr}(Z \mapsto R(Z, X)Y)$, equivalently $\mathrm{Ric}_{ab} = R^c_{\;acb}$. It is a symmetric $(0,2)$-tensor (symmetry follows from the pair-swap symmetry of $R$). In an orthonormal frame, $\mathrm{Ric}(e_i, e_i) = \sum_{j \neq i} K(e_i \wedge e_j)$ is the sum of sectional curvatures of the $n-1$ planes containing $e_i$. The Ricci tensor measures the average sectional curvature in directions transverse to a given direction — the rate at which a small ball of geodesics emanating in direction $e_i$ contracts ($\mathrm{Ric} > 0$) or expands ($\mathrm{Ric} < 0$) relative to flat space.

- **[[Def - Scalar Curvature]]**
	- The scalar curvature is the trace of the Ricci tensor with respect to the metric: $S = g^{ab}\mathrm{Ric}_{ab} = \sum_{i \neq j} K(e_i \wedge e_j)$ in an orthonormal frame. It is a single function on $M$ — the most aggregated curvature invariant. For a $2$-manifold, $S = 2K$ where $K$ is the Gauss curvature; for $S^n$, $S = n(n-1)$; for $H^n$, $S = -n(n-1)$. The scalar curvature is the quantity that appears in the Einstein–Hilbert action and the Yamabe problem.

- **[[Def - Einstein Manifold]]**
	- A Riemannian manifold is **Einstein** if $\mathrm{Ric} = \lambda g$ for some constant $\lambda$ (necessarily $\lambda = S/n$). All constant-sectional-curvature manifolds are Einstein, but the converse fails in dimension $\ge 4$: $S^2 \times S^2$ with the product metric is Einstein but not of constant sectional curvature. By Schur's lemma, if $\mathrm{Ric}(p) = f(p)g(p)$ pointwise (with $f$ a function on $M$) and $n \ge 3$, then $f$ is constant — so the apparently weaker condition forces the stronger one. In dimension $4$, Einstein manifolds satisfy a topological constraint via the **Hitchin–Thorpe inequality**.

- **[[Def - Constant Sectional Curvature]]**
	- A Riemannian manifold has **constant sectional curvature** $K_0$ if $K(\sigma) = K_0$ for every tangent $2$-plane at every point. Equivalently, $R(X, Y)Z = K_0(\langle Y, Z\rangle X - \langle X, Z\rangle Y)$, the simplest possible form for the Riemann tensor consistent with its symmetries. Schur's lemma again: if the sectional curvature depends only on the point (not on the plane) and $n \ge 3$, then it is constant in the point too. The complete simply-connected examples are exactly the three model spaces $S^n$ ($K_0 > 0$), $\mathbb{R}^n$ ($K_0 = 0$), $H^n$ ($K_0 < 0$).

> [!tip] Unlocked: Einstein's Field Equations *(from General Relativity)*
> The Einstein tensor $G_{\mu\nu} = \mathrm{Ric}_{\mu\nu} - \tfrac{1}{2}g_{\mu\nu}S$ is divergence-free by the second [[Thm - First and Second Bianchi Identities|Bianchi identity]], making it the only natural symmetric $(0,2)$-tensor constructed from $g$ and its first two derivatives that is automatically conserved. Einstein's equations $G_{\mu\nu} = 8\pi T_{\mu\nu}$ on a Lorentzian $4$-manifold equate this geometric tensor with the stress-energy tensor; consistency demands $\nabla^\mu T_{\mu\nu} = 0$, which is guaranteed by Bianchi. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

- **[[Ex - Sectional Curvature of the Round Sphere is 1]]** (⭐⭐)
	- Verify directly that the unit sphere $S^n \subset \mathbb{R}^{n+1}$ with the induced metric has $K \equiv 1$ in every tangent $2$-plane, using either the Gauss equation for a hypersurface or Cartan's structural equations.

- **[[Ex - Sectional Curvature of the Hyperbolic Plane is -1]]** (⭐⭐)
	- Verify that the upper half-plane $H^2 = \{(x, y) : y > 0\}$ with the metric $g = y^{-2}(dx^2 + dy^2)$ has $K \equiv -1$ everywhere, using Cartan's method.

- **[[Ex - The Ricci Tensor of a 2-Manifold is g times K]]** (⭐)
	- Show that on a $2$-dimensional Riemannian manifold, $\mathrm{Ric} = K\, g$ where $K$ is the Gauss curvature, and hence every $2$-manifold is Einstein.

> [!note] Exercise Index — §3.2
> [[Exercise Index - §3.2 Sectional, Ricci, and Scalar Curvature]]

## §3.3 Comparison Theorems

- **[[Def - Model Spaces (Sphere Euclidean Hyperbolic)]]**
	- The three simply-connected complete Riemannian manifolds of constant sectional curvature, one for each sign: the round sphere $(S^n, g_{\mathrm{round}})$ with $K = +1$, Euclidean space $(\mathbb{R}^n, g_{\mathrm{flat}})$ with $K = 0$, and hyperbolic $n$-space $(H^n, g_{\mathrm{hyp}})$ with $K = -1$. Rescaling gives constant curvature $\kappa$: $S^n_\kappa$ has radius $1/\sqrt{\kappa}$ when $\kappa > 0$. By the Killing–Hopf theorem, every complete simply-connected Riemannian manifold of constant sectional curvature is isometric to one of these three (up to scaling). All other constant-curvature manifolds are quotients of these by free, properly discontinuous group actions — the spherical, Euclidean, and hyperbolic **space forms**.

- **[[Def - The Hyperbolic Space H^n]]**
	- Hyperbolic $n$-space has three standard models: the **upper half-space** $\{(x_1, \ldots, x_n) : x_n > 0\}$ with metric $g = (dx_1^2 + \cdots + dx_n^2)/x_n^2$, the **Poincaré ball** $\{|x| < 1\}$ with metric $g = 4(1 - |x|^2)^{-2}\sum (dx^i)^2$, and the **hyperboloid model** $\{x \in \mathbb{R}^{1,n} : \langle x, x\rangle_{\mathrm{Mink}} = -1, x_0 > 0\}$ with the induced Lorentzian-restricted metric. All three are isometric. The hyperboloid model makes the [[Def - Isometry|isometry]] group $O(1, n)$ transparent — hyperbolic space is the homogeneous space $O(1, n)/O(n)$, exactly analogous to $S^n = O(n+1)/O(n)$. Geodesics in the upper-half-space model are vertical lines and semicircles meeting the boundary orthogonally.

- **[[Thm - Cartan-Hadamard Theorem]]**
	- Let $(M, g)$ be a complete, simply-connected Riemannian manifold with sectional curvature $K \le 0$ everywhere. Then for any $p \in M$, the exponential map $\exp_p : T_pM \to M$ is a diffeomorphism. In particular, $M$ is diffeomorphic to $\mathbb{R}^n$, two distinct points are joined by a unique geodesic, and there are no conjugate points along any geodesic. The proof uses the Jacobi-field characterisation of conjugate points: in nonpositive curvature, the Jacobi equation $J'' + K(J)J = 0$ becomes $J'' + (\text{nonneg})\cdot J = 0$ with the wrong sign, and Jacobi fields grow rather than oscillate. Without simple connectedness, the conclusion is that the universal cover is diffeomorphic to $\mathbb{R}^n$ — every compact $K \le 0$ manifold is $K(\pi_1, 1)$ in algebraic-topology terminology.

- **[[Thm - Bonnet-Myers Theorem]]**
	- Let $(M, g)$ be a complete Riemannian manifold with Ricci curvature satisfying $\mathrm{Ric}(v, v) \ge (n-1)\kappa\, |v|^2$ for some constant $\kappa > 0$ and all $v$. Then $M$ is compact, $\mathrm{diam}(M) \le \pi/\sqrt{\kappa}$, and $\pi_1(M)$ is finite. The proof is by contradiction: any minimising geodesic of length $> \pi/\sqrt{\kappa}$ would have a conjugate point in its interior (Jacobi-field comparison with the sphere of curvature $\kappa$), contradicting minimality. Finiteness of $\pi_1$ follows because the universal cover satisfies the same Ricci bound and so is also compact; a compact cover of a compact space has finite degree. Bonnet–Myers is sharp: the sphere $S^n_\kappa$ saturates both bounds.

- **[[Thm - Synge's Theorem]]**
	- Let $(M, g)$ be a compact, orientable, even-dimensional Riemannian manifold with positive sectional curvature $K > 0$. Then $M$ is simply connected. The proof: if $\pi_1(M) \neq 0$, there exists a shortest closed geodesic $C$ in some nontrivial free [[Def - Homotopy|homotopy]] class. Parallel transport around $C$ preserves the normal bundle, acts as an orientation-preserving isometry of the $(2n-1)$-dimensional normal space, and so (odd dimension) has $+1$ as an eigenvalue. The corresponding parallel-transported normal vector field $J$ yields a variation along which Synge's formula gives $L''(0) = -\int K(T \wedge J)\, ds < 0$ — the geodesic can be shortened, contradicting its minimality. The example $\mathbb{RP}^{2n}$ (positively curved but not orientable) and $S^{2n+1}$ (positively curved, odd-dim, simply connected anyway) show that both even-dim and orientability are essential.

> [!tip] Unlocked: Sphere Theorem *(from Comparison Geometry)*
> A natural question after Synge: which positively-curved manifolds are spheres? The **classical sphere theorem** of Berger and Klingenberg says: a simply-connected, complete Riemannian manifold whose sectional curvatures satisfy $1/4 < K \le 1$ is homeomorphic to $S^n$. The **differentiable sphere theorem** of **Brendle–Schoen** (2009) sharpens this to diffeomorphism — proved via Ricci flow. The constant $1/4$ is sharp: $\mathbb{CP}^n$ with the Fubini–Study metric has $1/4 \le K \le 1$ and is not homeomorphic to $S^{2n}$.

> [!tip] Unlocked: Comparison Geometry *(from Riemannian Geometry, advanced)*
> The **Rauch comparison theorem** says Jacobi fields in a manifold with $K \le K_0$ grow at least as fast as in the model space of curvature $K_0$, and the **Toponogov triangle comparison theorem** says geodesic triangles are "fatter" than in the model space. Both generalise Bonnet–Myers and Cartan–Hadamard and underlie almost all of modern Riemannian comparison geometry — the **Bishop–Gromov volume comparison**, **Cheeger–Gromoll splitting theorem**, **Gromov compactness theorem** for collections of manifolds with bounded curvature and diameter.

- **[[Ex - Schwarzschild Sectional Curvatures (Statement)]]** (⭐⭐⭐)
	- Compute the orthonormal-frame sectional curvatures of the Schwarzschild metric $g = -(1-2M/r)dt^2 + (1-2M/r)^{-1}dr^2 + r^2 d\Omega^2$ on $r > 2M$, and verify the Ricci tensor vanishes (so Schwarzschild is a vacuum solution of Einstein's equations).

> [!note] Exercise Index — §3.3
> [[Exercise Index - §3.3 Comparison Theorems]]

## §3.4 Synge, Killing Fields, and Curvature–Topology Bridges

- **[[Def - Killing Vector Field]]**
	- A vector field $X$ on $(M, g)$ is a **Killing field** if $\mathcal{L}_X g = 0$ — that is, the flow of $X$ consists of isometries. Equivalently, $X$ satisfies **Killing's equation** $\nabla_a X_b + \nabla_b X_a = 0$ in any frame. The Killing fields on $(M, g)$ form a Lie algebra under the Lie bracket of vector fields, isomorphic to the Lie algebra $\mathfrak{iso}(M, g)$ of the isometry group $\mathrm{Iso}(M, g)$. The dimension of this Lie algebra is at most $n(n+1)/2$, achieved exactly by manifolds of constant sectional curvature; this maximum is attained by $S^n$, $\mathbb{R}^n$, $H^n$.

- **[[Thm - Killing Equation]]**
	- A vector field $X$ on $(M, g)$ is a Killing field if and only if $\nabla_a X_b + \nabla_b X_a = 0$, equivalently $\nabla X$ is a skew-symmetric $(0,2)$-tensor (with the second slot a $1$-form via the metric). The proof unpacks the Lie-derivative formula $(\mathcal{L}_X g)(Y, Z) = X\langle Y, Z\rangle - \langle [X, Y], Z\rangle - \langle Y, [X, Z]\rangle$, uses metric compatibility to rewrite the Lie brackets in terms of $\nabla$, and observes the antisymmetric combination of covariant derivatives that emerges. The "skew $\nabla X$" form is the most operationally useful: it makes Killing fields the geometric analogue of harmonic forms in many ways and underlies the **Bochner technique** for ruling out their existence.

> [!tip] Unlocked: Symmetry Reduction *(from Geometric Mechanics)*
> Every Killing field gives a conserved quantity along geodesics: if $X$ is Killing and $\gamma$ is a geodesic with tangent $T$, then $\langle X, T\rangle$ is constant. This is **Noether's theorem** in its purest geometric form. In [[General Relativity I — Einstein's Equations and Schwarzschild]], the timelike Killing field of Schwarzschild yields energy conservation; the axial Killing field yields angular-momentum conservation. The reduction of geodesic flow by a Killing symmetry is the prototype of **symplectic reduction** in [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]].

> [!tip] Unlocked: Bochner Technique *(from Hodge Theory)*
> The **Bochner formula** for a vector field $X$ — $\tfrac{1}{2}\Delta|X|^2 = |\nabla X|^2 - \langle \nabla^*\nabla X, X\rangle + \mathrm{Ric}(X, X)$ — combined with positive Ricci curvature, gives **Bochner's vanishing theorem**: on a compact manifold with $\mathrm{Ric} > 0$, every Killing field (and every harmonic $1$-form) vanishes. This pattern — curvature-positivity forces vanishing of geometric objects via integration by parts — is one of the most powerful techniques in Riemannian geometry. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

- **[[Ex - Bonnet-Myers Gives a Finite Fundamental Group of CP^n]]** (⭐⭐)
	- The complex projective space $\mathbb{CP}^n$ with the Fubini–Study metric has sectional curvature in $[1/4, 1]$; deduce that $\pi_1(\mathbb{CP}^n)$ is finite, then check it is actually trivial.

- **[[Ex - Killing Fields on the Sphere from SO(n+1)]]** (⭐⭐)
	- Exhibit the $n(n+1)/2$-dimensional space of Killing fields on $S^n$ explicitly: each skew-symmetric matrix $A \in \mathfrak{so}(n+1)$ defines a Killing field $X_A(p) = A p$ restricted to $S^n$, and these span the full Killing algebra.

> [!note] Exercise Index — §3.4
> [[Exercise Index - §3.4 Synge and Curvature-Topology Bridges]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

Five recurring targets show up across every exercise and theorem in this chapter. *Topological conclusions from curvature bounds*: a manifold has finite fundamental group, is simply connected, is diffeomorphic to $\mathbb{R}^n$, has bounded diameter, or is compact. These are the "global from local" theorems, the headline content. *Comparison estimates*: a quantity (Jacobi-field norm, distance between geodesics, volume of a ball, length of a triangle side) is bounded above or below by the same quantity in a model space of constant curvature. *Curvature computations in specific manifolds*: given an explicit metric, compute $R^a_{\;bcd}$, $\mathrm{Ric}$, $S$, or check that the metric satisfies a curvature condition (Einstein, vacuum, constant sectional). *Algebraic identities for $R$*: the Bianchi identities, the symmetries, polarisation formulae relating $K$ to $R$. *Existence of distinguished structures*: Killing fields, parallel vector fields, parallel transport that respects extra structure.

**Sources — what assumptions do we usually leverage?**

Five recurring source patterns underlie this chapter. *A pointwise bound on curvature* — $K \ge \kappa$ or $K \le \kappa$ or $\mathrm{Ric} \ge \lambda g$ — is the workhorse hypothesis. It enters proofs via the Jacobi equation $J'' + K(J)J = 0$, which under such a bound can be compared to the constant-coefficient model equation $J'' + \kappa J = 0$. *Completeness* (every geodesic extends to all of $\mathbb{R}$) is the second universal hypothesis, ensuring geodesics actually reach where they need to and that the exponential map is globally defined. *Compactness* gives finite diameter, attainability of minima of length functionals on path spaces, and the existence of shortest closed geodesics in every free-homotopy class. *Simple connectedness* or its analogue (working on the universal cover) lets the local-to-global passage of the exponential map go through without obstruction by deck transformations. *Even-dimensionality and orientability* enter through the eigenvalue analysis of parallel transport around a loop — these are the precise conditions that force a parallel-transport map to have $+1$ as an eigenvalue (Synge).

The routes are systematic: *curvature bound + completeness + simple connectedness → diffeomorphism with $\mathbb{R}^n$* (Cartan–Hadamard); *Ricci bound + completeness → compactness and finite $\pi_1$* (Bonnet–Myers); *positive sectional + compactness + even-dim + orientable → simply connected* (Synge); *curvature bound alone → Jacobi-field comparison* (Rauch, on the way to all the above).

---

# Legal Operations

The legal operations of this chapter are all moves that get curvature out of an integral, or get topology out of a variational inequality. Almost every proof in the comparison-theorem world routes through one or two of them.

**Legal operations:**

1. **Apply the second variation of arc length to a geodesic with a chosen variation field.** *Trigger:* the conclusion involves "this geodesic is not minimising" or "the manifold has bounded diameter" or "the fundamental group is constrained." *Pattern:* take a minimising geodesic $\gamma$ in some homotopy class (its existence guaranteed by compactness + some homotopy condition); cook up a normal variation field $J$ (parallel-transported field for Synge, eigenfunction of the Jacobi equation for Bonnet–Myers); compute $L''(0)$ using Synge's formula; argue that $L''(0) < 0$ for $\gamma$ long enough or curvature positive enough; conclude the geodesic can be shortened — a contradiction with minimality. Every comparison theorem in this chapter follows this template. See [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]] for the formula.

2. **Use the Jacobi equation $\nabla_T\nabla_T J + R(J, T)T = 0$ to convert curvature bounds into bounds on Jacobi-field growth.** *Trigger:* you have a sectional-curvature bound and want a statement about distance between nearby geodesics or about conjugate points. *Pattern:* fix a geodesic $\gamma$ with unit tangent $T$; an orthogonal Jacobi field $J$ satisfies $J'' + K(J \wedge T)J = 0$ (in arc-length parameterisation, projecting onto a parallel frame); under $K \le 0$ this becomes $J'' + (\text{nonpositive}) J = 0$, so $|J|$ is convex and $J$ has no zeros after its initial one — no conjugate points (Cartan–Hadamard); under $K \ge \kappa > 0$ comparing to $J'' + \kappa J = 0$, $J$ must vanish by time $\pi/\sqrt{\kappa}$ — there is a conjugate point (Bonnet–Myers).

3. **Compute the curvature 2-form via Cartan's second structural equation $\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c}\wedge\omega^c_{\;b}$ in an orthonormal coframe.** *Trigger:* the metric is given in coordinates and you need an explicit value of $R^a_{\;bcd}$ or $K$. *Pattern:* find a convenient orthonormal coframe $(\sigma^a)$; solve $d\sigma^a + \omega^a_{\;b}\wedge\sigma^b = 0$ and $\omega_{ab} = -\omega_{ba}$ for the connection 1-forms uniquely; compute $\Omega^a_{\;b}$ from the structural equation; read off components $R^a_{\;bcd}$ by expanding in $\sigma^c \wedge \sigma^d$. Much faster than the Christoffel-symbol route in coordinates. See [[Riemannian Geometry I — Connections and Covariant Differentiation]] §1.3 for the structural equations.

4. **Trace the Riemann tensor to descend to Ricci or scalar curvature.** *Trigger:* you have control over $R^a_{\;bcd}$ but a hypothesis or conclusion is phrased in terms of $\mathrm{Ric}$ or $S$. *Pattern:* contract $R^a_{\;bcd}$ over the appropriate index pair: $\mathrm{Ric}_{bc} = R^a_{\;bac}$; then $S = g^{bc}\mathrm{Ric}_{bc}$. The contraction is information-losing but turns matrix-valued conditions into scalar ones; many global theorems (Bonnet–Myers, Bochner) need only the trace, even though the proof of the underlying inequality holds for $K$.

5. **Apply the second Bianchi identity $\nabla R = 0$ (cyclic) to deduce conservation laws.** *Trigger:* a divergence of a curvature quantity needs to vanish (e.g., for an Einstein-equations consistency check), or a curvature scalar's gradient needs to be expressed in terms of a Ricci divergence. *Pattern:* the contracted second Bianchi $\nabla_a R^{ab} = \tfrac{1}{2}\nabla^b S$ implies $\nabla_a(R^{ab} - \tfrac{1}{2}g^{ab}S) = 0$, the Einstein-tensor divergence identity. In Einstein-manifold proofs, $\mathrm{Ric} = (S/n)g$ combined with Bianchi forces $\nabla S = 0$ in dimension $\ge 3$, hence $S$ constant — this is **Schur's lemma**.

6. **Lift a problem to the universal cover.** *Trigger:* a hypothesis is local (a curvature bound) and the conclusion is global, but $M$ is not simply connected. *Pattern:* take the [[Algebraic Topology II — Fundamental Group and Covering Spaces|universal cover]] $\tilde M \to M$ with the pulled-back metric $\tilde g$; the curvature of $\tilde g$ matches the curvature of $g$ pointwise (the projection is a local isometry); apply the simply-connected theorem to $\tilde M$; pull conclusions back to $M$. This is how Cartan–Hadamard says "compact $K \le 0$ manifolds have $\tilde M = \mathbb{R}^n$" and how Bonnet–Myers's finite-$\pi_1$ conclusion is derived (compactness of $\tilde M$ from the same Ricci bound, then covering-space-degree counts $\pi_1$).

7. **Exploit a Killing field to reduce dimension or extract a conserved quantity.** *Trigger:* the metric has a continuous symmetry (a Killing field $X$ exists), and the geodesic flow is conservative. *Pattern:* along any geodesic $\gamma$ with tangent $T$, the inner product $\langle X, T\rangle$ is constant. This reduces the geodesic equation by one dimension, often making integration in closed form possible. In Schwarzschild, the timelike Killing field $\partial_t$ gives the conserved energy and the rotational Killing fields give angular momentum, reducing geodesic motion to a 1D radial problem.

8. **Compare a Jacobi-field equation to a constant-coefficient model on a constant-curvature space.** *Trigger:* you need a quantitative bound on a geodesic-related quantity (distance, angle, conjugate point) under a curvature bound. *Pattern:* the relevant ODE is $J'' + K(s)J = 0$; under $K \ge \kappa$, Sturm's comparison theorem says $J$ has its first zero no later than the corresponding solution of $J'' + \kappa J = 0$, which is $\sin(\sqrt{\kappa}s)/\sqrt{\kappa}$ — first zero at $s = \pi/\sqrt{\kappa}$. This gives Bonnet–Myers's diameter bound directly. Toponogov and Rauch are the general versions.

9. **Convert a parallel-transport-around-a-loop question to a question about the holonomy group.** *Trigger:* a problem asks whether some object (orientation, complex structure, parallel field) survives transport around a loop. *Pattern:* parallel transport defines a representation of $\pi_1(M)$ on $T_pM$ (in fact on any tensor bundle); the image is the **holonomy group**. For an orientable Riemannian manifold, holonomy lies in $\mathrm{SO}(n)$; reductions of the holonomy group correspond to extra parallel structure (e.g., $\mathrm{U}(n)$-holonomy ⟺ Kähler structure). Synge's proof uses precisely this: orientation-preserving + odd-dim normal bundle forces $+1$ eigenvalue.

**Illegal but tempting operations:**

> [!warning] 1. Inferring topology from a *pointwise* sectional-curvature bound without completeness
> One is tempted to say "positive sectional curvature implies compact" or "negative sectional curvature implies $\mathbb{R}^n$" with no further hypothesis. **Counterexample:** the open disc $\{|x| < 1\} \subset \mathbb{R}^2$ with the Poincaré metric $g = (1-|x|^2)^{-2}|dx|^2$ has $K = -4$ everywhere (constant negative curvature), is *not* simply connected as a Riemannian manifold but is diffeomorphic to $\mathbb{R}^2$ — it is, in fact, hyperbolic $2$-space, so the conclusion happens to hold. But take a small open subset of a positively-curved manifold: $K > 0$ everywhere on it, yet it is neither compact nor closed. **The repair:** completeness is the missing ingredient. Without it, no global theorem from a curvature bound is true.

> [!warning] 2. Assuming the *Ricci* tensor controls sectional curvature
> The Ricci tensor is the trace of the Riemann tensor over one index pair, so it loses information about how curvature is distributed among $2$-planes. **Counterexample:** $S^2 \times S^2$ with the product metric has $\mathrm{Ric} = g$ (positive Ricci) but contains totally geodesic flat $2$-tori (the leaves $\{p\} \times S^2$ and $S^2 \times \{p\}$ at fixed $p$... wait, those are not flat — but mixed $2$-planes spanned by one vector from each factor have $K = 0$). So $S^2 \times S^2$ has positive Ricci but not positive sectional curvature, and the Brendle–Schoen sphere theorem hypothesis $1/4 < K \le 1$ fails. **The repair:** for theorems that need positive sectional curvature (Synge, the sphere theorem) you must verify the sectional bound directly; Ricci is not enough.

> [!warning] 3. Treating "Einstein" as "constant sectional curvature"
> In dimension $\ge 4$, the conditions $\mathrm{Ric} = \lambda g$ and $K \equiv \lambda$ are not equivalent. **Counterexample:** complex projective space $\mathbb{CP}^n$ with the Fubini–Study metric is Einstein but has sectional curvature varying in $[1/4, 1]$ — not constant. **The repair:** Einstein is a weaker condition. In dimension $2$ or $3$ they happen to coincide (Schur's lemma plus low-dimensional constraints), but starting in dimension $4$ there are genuinely Einstein non-constant-sectional-curvature manifolds.

> [!warning] 4. Dropping orientability or even-dimensionality from Synge's theorem
> Both hypotheses are essential. **Counterexample to dropping orientability:** $\mathbb{RP}^{2n}$ is compact, even-dimensional, has positive sectional curvature (inherited from $S^{2n}$), but $\pi_1(\mathbb{RP}^{2n}) = \mathbb{Z}/2 \ne 0$. **Counterexample to dropping even-dim:** $\mathbb{RP}^{2n+1}$ is compact, orientable, has positive sectional curvature, but again $\pi_1 = \mathbb{Z}/2$. **The repair:** Synge's hypothesis is sharp. In both cases, parallel transport around a generator of $\pi_1$ fails to have $+1$ as an eigenvalue: orientation reversal in the first case, lack of guaranteed real eigenvalue in odd-dim normal bundle in the second.

> [!warning] 5. Polarising "$K(\sigma)$ determines $R$" carelessly
> One might write $R(X, Y, Z, W) = K(X \wedge Y) (\langle Y, Z\rangle\langle X, W\rangle - \langle X, Z\rangle\langle Y, W\rangle)$ as a global formula. **Counterexample:** this formula gives a tensor with the right value on the diagonal $\langle R(X,Y)Y, X\rangle$ but is missing off-diagonal contributions; only on constant-sectional-curvature manifolds is it correct. **The repair:** polarisation requires four distinct vectors and the linearity of $R$; the correct formula is a sum of six terms (the polarisation identity for the symmetric bilinear form $(X \wedge Y, Z \wedge W) \mapsto R(X, Y, W, Z)$).

---

# Problem-Solving Strategy

Problems in this chapter come in three flavours, and the routing is different for each. **First, "compute the curvature of this specific manifold."** When the metric is given in coordinates or has a natural orthonormal coframe, Cartan's structural equations (legal operation 3) are essentially always faster than Christoffel symbols. The recipe: find an orthonormal coframe; solve the first structural equation $d\sigma^a + \omega^a_{\;b}\wedge\sigma^b = 0$ under skew-symmetry $\omega_{ab} = -\omega_{ba}$ to find the connection 1-forms uniquely; compute the curvature 2-forms via $\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c}\wedge\omega^c_{\;b}$; expand in the coframe to read off $R^a_{\;bcd}$. For dimension $2$, this reduces to computing the single 1-form $\omega^1_{\;2}$ and reading $K$ off $d\omega^1_{\;2} = K\, \sigma^1\wedge\sigma^2$. For dimension $4$ in the Einstein-equation context, choose a coframe adapted to the symmetry (spherical, axisymmetric); the calculation is long but mechanical.

**Second, "prove a topological conclusion from a curvature hypothesis."** The unifying strategy is *second variation of arc length applied to a geodesic produced by some compactness argument*. The recipe: identify a class of curves that must contain a length-minimiser (a free homotopy class for Synge, a fixed pair of endpoints for the diameter bound, the loop space at a point for Bonnet–Myers); produce a minimising geodesic in the class; choose a variation field $J$ designed to make Synge's formula negative under the curvature hypothesis (parallel field for closed-geodesic problems, eigenvalue of the Jacobi equation for endpoint problems); derive a contradiction with minimality. The choice of $J$ is the creative step — for Bonnet–Myers one uses $J(s) = \sin(\pi s/L)\, e$ for $e$ a parallel unit normal; for Synge one uses a parallel unit normal directly; for Cartan–Hadamard one uses convexity of $|J|^2$ to bypass second variation entirely.

**Third, "manipulate the algebra of $R$, $\mathrm{Ric}$, or $S$."** These are computational exercises in tensor contraction and the use of symmetries. Use the antisymmetries to halve and re-halve index ranges; use the first Bianchi identity to cyclically permute and cancel; use the second Bianchi identity to relate covariant derivatives of $R$ to those of $\mathrm{Ric}$ and $S$. **The single unifying question of this chapter is: how does the local infinitesimal data $R$ at a point control the global geometry and topology of the whole manifold?** Every theorem answers a special case; every exercise drills a different bridge from the local algebraic side to the global geometric or topological side.

---

# Most Reusable Properties

- **[[Thm - Bonnet-Myers Theorem|Bonnet–Myers]]**: $\mathrm{Ric} \ge (n-1)\kappa\, g$, $\kappa > 0$, $M$ complete $\implies$ $M$ compact, $\mathrm{diam}(M) \le \pi/\sqrt{\kappa}$, $\pi_1(M)$ finite. *Typical use:* whenever you have a positive Ricci lower bound on a complete manifold, this theorem produces both a quantitative diameter bound and a topological finiteness statement. The route from $\mathrm{Ric}$-positivity to "no harmonic 1-forms" via Bochner extends this into Hodge theory. Recognise the trigger by *any* hypothesis equivalent to a Ricci lower bound: $\mathrm{Ric} \ge \lambda g$, Einstein with positive scalar, or in physics, "matter with positive energy density satisfying the strong energy condition."

- **[[Thm - Cartan-Hadamard Theorem|Cartan–Hadamard]]**: $K \le 0$, $M$ complete and simply connected $\implies$ $\exp_p$ is a global diffeomorphism, $M \approx \mathbb{R}^n$. *Typical use:* on any nonpositively-curved complete simply-connected manifold, geodesics are unique global minimisers and the manifold is contractible. The pulled-back conclusion is enormous: every nonpositively-curved compact manifold is a $K(\pi_1, 1)$ space (its universal cover is contractible), so its cohomology is the group cohomology of $\pi_1$. The strategy of working on the universal cover is itself a routinely-reused move.

- **[[Thm - Synge's Theorem|Synge]]**: compact + orientable + even-dim + $K > 0$ $\implies$ simply connected. *Typical use:* the strongest topological conclusion from positive sectional curvature. Read in the contrapositive: if a compact orientable even-dim manifold has nontrivial $\pi_1$, then $K$ must change sign somewhere. Synge's *method* (analyse parallel transport around a shortest closed geodesic) is reused for the related Synge corollary that compact odd-dimensional positively-curved manifolds are orientable.

- **[[Thm - First and Second Bianchi Identities|Second Bianchi identity]]**: $\nabla_E R + \nabla_X R + \nabla_Y R = 0$ (cyclic), implying $\nabla_a(R^{ab} - \tfrac{1}{2}g^{ab}S) = 0$. *Typical use:* the divergence-freeness of the Einstein tensor is the geometric reason Einstein's field equations $G_{\mu\nu} = 8\pi T_{\mu\nu}$ are compatible with $\nabla^\mu T_{\mu\nu} = 0$. In any curvature manipulation that needs to commute covariant derivatives or that involves a "conservation law for curvature," Bianchi is the move.

- **The Jacobi equation along a geodesic**: $J'' + R(J, T)T = 0$. *Typical use:* the bridge between local curvature data and global geodesic behaviour. Every comparison theorem (Rauch, Bonnet–Myers, Cartan–Hadamard) is a statement about solutions of this ODE under curvature bounds. Recognising "this is really a question about Jacobi fields" is the diagnostic move — questions about conjugate points, about second variation, about volume of geodesic balls all reduce to Jacobi analysis.

---

# Bridges

1. **General Relativity and the Einstein equations.** The Einstein field equations $G_{\mu\nu} = 8\pi T_{\mu\nu}$ on a Lorentzian $4$-manifold equate the Einstein tensor $G_{\mu\nu} = \mathrm{Ric}_{\mu\nu} - \tfrac{1}{2}g_{\mu\nu}S$ — a curvature combination built entirely from the metric and its first two derivatives — with the stress-energy tensor $T_{\mu\nu}$. The reason for the specific combination is precisely the contracted second Bianchi identity proved in this chapter: $\nabla^\mu G_{\mu\nu} = 0$ automatically, matching $\nabla^\mu T_{\mu\nu} = 0$ (conservation of energy-momentum). Without Bianchi, Einstein's equations would not be self-consistent. The geometric content of the equations is exactly that the sum of the sectional curvatures of $2$-planes orthogonal to a timelike direction measures the nongravitational energy density seen by an observer with that 4-velocity. See [[General Relativity I — Einstein's Equations and Schwarzschild]] for the Schwarzschild geodesic computations and the linearised wave-equation form.

2. **Algebraic topology of the fundamental group.** Bonnet–Myers connects Riemannian curvature directly to the fundamental group: positive Ricci curvature on a complete manifold forces $\pi_1$ to be finite. The proof works by lifting to the universal cover, which by [[Algebraic Topology II — Fundamental Group and Covering Spaces|covering-space theory]] has the same local curvature; applying compactness of the cover; and counting sheets. Synge gives an even stronger statement under even-dim + positive sectional + orientable, deducing $\pi_1 = 0$. In the opposite direction, Cartan–Hadamard says nonpositively-curved complete manifolds have contractible universal cover, making $\pi_1$ the entire homotopy type. The curvature-to-topology dictionary in this chapter is the *prototypical* example of how analysis on a manifold ($R$-tensor, geodesics) determines its discrete topological invariants ($\pi_1$).

3. **Hodge theory and the Bochner technique.** The pattern "positive curvature + integration by parts ⟹ vanishing of harmonic forms" is the **Bochner technique**, the central tool of [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition|Hodge theory]] for vanishing theorems. The basic identity is $\tfrac{1}{2}\Delta|\omega|^2 = |\nabla\omega|^2 - \langle\Delta_{\mathrm{Hodge}}\omega, \omega\rangle + W(\omega, \omega)$, where $W$ is a curvature-built quadratic form (for $1$-forms, $W = \mathrm{Ric}$). On a compact manifold, integrating over $M$ and using $\Delta_{\mathrm{Hodge}}\omega = 0$ kills the second term, leaving $0 = \int |\nabla\omega|^2 + \int W(\omega, \omega)$; if $W > 0$ pointwise, both terms vanish individually, so $\nabla\omega = 0$ and $W(\omega, \omega) = 0$, hence $\omega = 0$ (since $W > 0$). Result: compact + $\mathrm{Ric} > 0$ implies first Betti number $b_1 = 0$, a sharpening of Bonnet–Myers's $\pi_1$-finiteness in cohomology language.

4. **Gauge theory and the curvature of a principal bundle.** The Riemann curvature tensor is the curvature of the Levi-Civita connection viewed as a connection on the principal $\mathrm{O}(n)$-bundle of orthonormal frames over $M$. From this viewpoint, the components $R^a_{\;bcd}$ are the components of an $\mathfrak{o}(n)$-valued 2-form $\Omega$ on the frame bundle, pulled back to $M$ via a local frame. The two Bianchi identities become the *single* universal Bianchi identity $d^A\Omega = 0$ for any connection on any principal bundle, and the structural equations become $\Omega = dA + \tfrac{1}{2}[A, A]$ for the connection 1-form $A$. See [[Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections]] for the general bundle setup and the comparison with the Yang–Mills field strength $F$.

5. **Geometric mechanics and the symmetry-conservation correspondence.** A Killing field $X$ on $(M, g)$ generates a 1-parameter group of isometries, and Noether's theorem in this geometric guise says: along any geodesic $\gamma$ with tangent $T$, the function $\langle X, T\rangle$ is constant. This is the cleanest expression of the symmetry-conservation correspondence: continuous symmetries of the metric directly produce conserved quantities of geodesic motion. In [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|geometric mechanics]], this generalises to **momentum maps** for Hamiltonian group actions, and the **symplectic reduction** theorem (Marsden–Weinstein) generalises the dimensional reduction of geodesic flow by a Killing-field action.

6. **Algebraic Topology — homology and the fundamental class.** On a closed orientable Riemannian manifold of even dimension $2n$, the **Chern–Gauss–Bonnet theorem** integrates a curvature polynomial (the Pfaffian of $R$) over $M$ to compute the Euler characteristic. For surfaces ($n = 1$), this reads $\int_M K\, dV = 2\pi\chi(M)$ — the **Gauss–Bonnet theorem** of [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]] §4.4. In higher even dimensions, the appropriate curvature polynomial is the **Euler form**, and the corresponding integral computes $\chi(M)$ via [[Algebraic Topology I — Singular Homology and the de Rham Theorem|de Rham cohomology]]. This is one of the first nontrivial **characteristic-class** results.

---

# Insights

**The unifying frame.** The whole chapter is the statement that *curvature is the obstruction to second covariant derivatives commuting*. The Riemann tensor is *defined* as that obstruction: $R(X, Y)Z = [\nabla_X, \nabla_Y]Z - \nabla_{[X, Y]}Z$. Every subsequent theorem unpacks a consequence of this commutator failure. The Jacobi equation is literally a statement that the second derivative of the family-of-geodesics map fails to commute — the failure is the Jacobi field's growth rate. Bonnet–Myers and Cartan–Hadamard are statements that this growth rate, controlled by $R$, controls the global behaviour of geodesics. Synge's theorem is a statement that parallel transport around a loop, governed by the integral of $R$ over a disc bounding the loop, controls whether closed geodesics can be minima.

**The true name of sectional curvature.** The official definition $K(\sigma) = \langle R(X, Y)Y, X\rangle / (|X|^2|Y|^2 - \langle X, Y\rangle^2)$ is hard to work with. The operational definition: $K(\sigma)$ is the Gauss curvature at $p$ of the $2$-dimensional surface formed by all geodesics emanating from $p$ tangent to $\sigma$. So $K > 0$ on a $2$-plane means geodesics spreading out into that $2$-plane converge back like longitudes on a sphere; $K < 0$ means they diverge exponentially like geodesics on the hyperbolic plane. When you want to know what sectional curvature *means*, look at this $2$-D totally geodesic surface and apply your intuition for surfaces in $\mathbb{R}^3$.

**A trigger-reaction pattern: "compact + curvature condition → use shortest-loop-in-its-homotopy-class."** Whenever a compact manifold has a curvature hypothesis and you want to constrain $\pi_1$, the move is the same: in every nontrivial free-homotopy class of loops on a compact manifold, there is a length-minimising representative, and that representative is a closed geodesic. Compute the second variation along it with a clever variation field; if you can make $L''(0) < 0$, the geodesic was not minimising — contradiction. The free-homotopy class was nontrivial by assumption, so the only escape is that the class did not exist, i.e., $\pi_1 = 0$. Synge is this pattern with positive sectional + even-dim + orientable. Bonnet–Myers is a different pattern with $\mathrm{Ric}$ + fixed endpoints.

**A trigger-reaction pattern: "see the Jacobi equation $J'' + KJ = 0$ → think Sturm comparison."** Solutions of $J'' + K(s)J = 0$ with $K(s) \ge \kappa$ have first zero no later than those of $J'' + \kappa J = 0$. This single fact, **Sturm's comparison theorem from ODE**, is the entire engine of comparison geometry. Every Jacobi-field bound, every conjugate-point estimate, every Bonnet–Myers diameter bound, every Cartan–Hadamard no-conjugate-point claim, is a direct application. Whenever you see "Jacobi field" and a "curvature bound," reach for Sturm.

**Inheritance — where do the global theorems come from?** The global topological conclusions (compactness in Bonnet–Myers, $\mathbb{R}^n$ in Cartan–Hadamard, simple connectedness in Synge) are inherited from the global behaviour of solutions to a *linear* second-order ODE — the Jacobi equation. The Jacobi equation, in turn, is inherited from the structure of $\nabla$ on geodesics, and $\nabla$ from the metric $g$. So the entire chain is: *metric → connection → geodesics → Jacobi equation → ODE comparison → global topology*. Every link is forced by the previous; the only creative move is the *choice of variation field* that turns a curvature inequality into a topology constraint via Synge's formula.

**Why even-dim and orientability in Synge.** The single technical fact behind Synge is: an orthogonal matrix $P \in \mathrm{SO}(2k+1)$ has at least one real eigenvalue $+1$. Both hypotheses contribute: orientability gives $P \in \mathrm{SO}$ rather than $\mathrm{O}$ (so $\det P = +1$), and odd dimension of the normal bundle (forced by even dim of $M$) gives the odd number of eigenvalues that, combined with $\det P = +1$ and the pairing of complex eigenvalues, forces $+1$ to appear. Lose either hypothesis and the eigenvalue $+1$ is no longer guaranteed; lose the $+1$ eigenvalue and you cannot produce the parallel-transported normal field that makes $L''(0) < 0$.
