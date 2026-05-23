---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - First Fundamental Form"
  - "Def - Gauss Normal Map"
  - "Def - Embedded Submanifold"
tags: [geometry, riemannian-geometry, surfaces, curvature]
---

# Notation

Let $M \subset \mathbb{R}^3$ be an oriented regular surface with unit normal field $N$. Local coordinates $(u, v) = (u^1, u^2)$, position vector $\mathbf{x}(u, v)$, coordinate tangents $\mathbf{x}_\alpha = \partial \mathbf{x}/\partial u^\alpha$, second partials $\mathbf{x}_{\alpha\beta} = \partial^2\mathbf{x}/\partial u^\alpha\partial u^\beta$, normal derivatives $N_\alpha = \partial N/\partial u^\alpha$. We write the [[Def - First Fundamental Form|first fundamental form]] as $\mathrm{I} = g_{\alpha\beta}\, du^\alpha du^\beta = E\, du^2 + 2F\, du\, dv + G\, dv^2$. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Axiom Motivation

The [[Def - First Fundamental Form|first fundamental form]] captures everything an inhabitant of $M$ can measure with a tape measure on the surface. But $M$ sits in $\mathbb{R}^3$ and *curves* inside it — and this extrinsic curving is invisible to $\mathrm{I}$ alone (the plane and the cylinder have the same first fundamental form). The desideratum is to capture the second piece of geometric data: how a curve on $M$ at a point $p$ curves *out of the tangent plane* — that is, the **normal component** of its acceleration. The second fundamental form is exactly the bilinear form that encodes this.

**Why a bilinear form on $T_pM$?** Consider any curve $\gamma(s) = \mathbf{x}(u(s), v(s))$ on $M$ parametrised by arc length, with unit tangent $T(s) = \dot\gamma(s) \in T_{\gamma(s)}M$. Its acceleration $\dot T = \ddot\gamma$ is a vector in $\mathbb{R}^3$ — not generally tangent to $M$. Decompose $\dot T$ into tangential and normal parts:
$$
\dot T = (\dot T)_{\text{tangential}} + \langle \dot T, N\rangle N.
$$
The tangential part is the [[Def - Geodesic Curvature|geodesic curvature vector]] (an intrinsic notion); the normal part is what we want to capture. The remarkable fact, due to Meusnier, is that $\langle \dot T, N\rangle$ depends only on the *tangent direction* $T$, not on the choice of curve through $p$ with that tangent. So the function $T \mapsto \langle \dot T, N\rangle$ is well-defined as a function on $T_pM$, and it turns out to be the *quadratic form* associated to a unique symmetric bilinear form — the second fundamental form $\mathrm{II}(T, T)$.

**Why symmetric?** The symmetry $\mathrm{II}(X, Y) = \mathrm{II}(Y, X)$ follows from the fundamental identity $\mathbf{x}_{\alpha\beta} = \mathbf{x}_{\beta\alpha}$ — the order of partial derivatives does not matter (since $\mathbf{x}$ is smooth, by **Clairaut's theorem**). Concretely, $b_{\alpha\beta} = \langle\mathbf{x}_{\alpha\beta}, N\rangle = \langle\mathbf{x}_{\beta\alpha}, N\rangle = b_{\beta\alpha}$. Without this symmetry, the second fundamental form would split into symmetric and antisymmetric parts, and only the symmetric part would capture geometry (the antisymmetric part of a normal-projected second derivative tensor turns out to vanish identically).

**Why "$-\langle dN(X), Y\rangle$" as the alternative formula?** The equivalence
$$
\langle\mathbf{x}_{\alpha\beta}, N\rangle = -\langle\mathbf{x}_\alpha, N_\beta\rangle
$$
follows from differentiating $\langle\mathbf{x}_\alpha, N\rangle = 0$ (the tangent vector $\mathbf{x}_\alpha$ is normal to $N$) with respect to $u^\beta$: $0 = \partial_\beta\langle\mathbf{x}_\alpha, N\rangle = \langle\mathbf{x}_{\alpha\beta}, N\rangle + \langle\mathbf{x}_\alpha, N_\beta\rangle$. The minus sign in $\mathrm{II} = -\langle d\mathbf{x}, dN\rangle$ is exactly this identity. The two formulae are equivalent, but the second is computationally easier when $N$ is known explicitly (e.g., on the sphere where $N(p) = p$), and the first is easier when the parametrisation $\mathbf{x}(u, v)$ is given explicitly.

**Why does it depend on the embedding?** Unlike $\mathrm{I}$, the second fundamental form $\mathrm{II}$ depends on *how $M$ sits in $\mathbb{R}^3$*: bending a flat sheet of paper into a cylinder preserves $\mathrm{I}$ (both are locally Euclidean) but changes $\mathrm{II}$ from zero to nonzero. This is the right dependence: $\mathrm{II}$ is *designed* to encode the embedding-dependent piece of the geometry — what an external observer in $\mathbb{R}^3$ can see, but an inhabitant of $M$ cannot. If $\mathrm{II}$ were intrinsic, it would tell the inhabitant whether their sheet of paper had been rolled up, which contradicts the flat-paper / cylinder [[Def - Isometry|isometry]].

The deep punchline is **Theorema Egregium** ([[Thm - Theorema Egregium of Gauss]]): even though $\mathrm{II}$ depends on the embedding, the *determinant ratio* $\det(\mathrm{II})/\det(\mathrm{I})$ does not — this is the Gauss curvature $K$, an intrinsic invariant. So the bilinear form $\mathrm{II}$ is extrinsic, but its determinant relative to $\mathrm{I}$ is intrinsic. This precise mixed dependence is what makes the chapter's structure work.

---

# The Definition

> **Definition (Second Fundamental Form).** Let $M \subset \mathbb{R}^3$ be an oriented regular surface with unit normal $N$. The **second fundamental form** at $p \in M$ is the symmetric bilinear form
> $$
> \mathrm{II}_p : T_pM \times T_pM \to \mathbb{R}, \qquad \mathrm{II}_p(X, Y) := -\langle dN_p(X), Y\rangle_{\mathbb{R}^3},
> $$
> equivalently
> $$
> \mathrm{II}_p(X, Y) = \langle \nabla^{\mathbb{R}^3}_X Y, N(p)\rangle,
> $$
> where $\nabla^{\mathbb{R}^3}$ is the Euclidean covariant derivative (i.e., partial derivative in coordinates) and $Y$ on the right is extended to a smooth field tangent to $M$ near $p$ (the result is independent of the extension).

In local coordinates $\mathbf{x}(u, v)$, the components are
$$
b_{\alpha\beta}(u, v) = \langle \mathbf{x}_{\alpha\beta}, N\rangle = -\langle \mathbf{x}_\alpha, N_\beta\rangle,
$$
so
$$
\mathrm{II} = b_{\alpha\beta}\, du^\alpha\, du^\beta = e\, du^2 + 2f\, du\, dv + g_{\mathrm{II}}\, dv^2,
$$
where (in Gauss's classical notation) $e = b_{11}$, $f = b_{12}$, $g_{\mathrm{II}} = b_{22}$. The mixed tensor $b^\alpha_{\;\beta} = g^{\alpha\gamma}b_{\gamma\beta}$ is the matrix of the [[Def - Shape Operator (Weingarten Map)|shape operator]] $S = -dN$ in the basis $\{\mathbf{x}_\alpha\}$.

**Meusnier's interpretation.** For a curve $\gamma(s)$ on $M$ with unit tangent $T$, the normal component of the ambient curvature vector $\dot T = \kappa \mathbf{n}$ (where $\kappa$ is the curve's curvature and $\mathbf{n}$ its principal normal as a space curve) is
$$
\langle \dot T, N\rangle = \mathrm{II}(T, T) = \kappa \cos\phi,
$$
where $\phi$ is the angle between $\mathbf{n}$ and $N$. So $\mathrm{II}(T, T)$ is the curvature of the normal-plane section in the direction $T$ — the "normal curvature" — and Meusnier's theorem says this depends only on $T$, not on the choice of curve through $p$ with tangent $T$.

---

# Categorical / Structural Definition

Structurally, the second fundamental form is the **normal-component of the ambient covariant derivative**. The Gauss formula decomposes the ambient $\nabla^{\mathbb{R}^3}_X Y$ into tangential and normal parts:
$$
\nabla^{\mathbb{R}^3}_X Y = \nabla^M_X Y + \mathrm{II}(X, Y) N,
$$
where $\nabla^M$ is the induced Levi-Civita connection on $M$ and $\mathrm{II}(X, Y)$ is a scalar (the normal coefficient, since the normal bundle is one-dimensional). For higher-codimension submanifolds $M^k \subset \mathbb{R}^n$, the analogous decomposition reads
$$
\nabla^{\mathbb{R}^n}_X Y = \nabla^M_X Y + \mathrm{II}(X, Y),
$$
where $\mathrm{II}(X, Y) \in \nu_pM$ is **vector-valued** in the normal bundle. The codimension-$1$ case collapses $\nu_pM = \mathbb{R}\cdot N$ to one [[Def - Dimension|dimension]], and $\mathrm{II}$ becomes scalar-valued — the form we have defined.

From the perspective of jet bundles, the second fundamental form is the $2$-jet of the embedding $\mathbf{x} : U \to \mathbb{R}^3$ relative to the tangent plane: the first jet recovers the tangent space, and the second jet (modulo the tangential part, which is just Christoffel symbols of the metric) gives $\mathrm{II}$. This is one perspective on why $\mathrm{II}$ "completes" $\mathrm{I}$ as the data needed to reconstruct the embedding (Bonnet's fundamental theorem of surface theory).

A bundle-theoretic interpretation: the data $(\mathrm{I}, \mathrm{II})$ on $M$ is equivalent to a **connection on the normal bundle** $\nu M \to M$ together with the metric. The Gauss and Codazzi equations ([[Thm - Equations of Gauss and Codazzi]]) are the curvature and torsion identities for this combined structure. This bundle perspective is the one that generalises to **Riemannian submersions**, **harmonic maps**, and the geometry of [[Def - Foliation|foliations]].

---

# Relate to Other Fields / Compression

The second fundamental form is the **extrinsic counterpart** to the first fundamental form. Where $\mathrm{I}$ encodes "what an inhabitant of $M$ can measure", $\mathrm{II}$ encodes "what an external observer in $\mathbb{R}^3$ sees but an inhabitant cannot". The two together (modulo signs and orientations) determine $M$ up to rigid motion (Bonnet's theorem).

In **general relativity**, the analogue is the **extrinsic curvature** $K_{ij}$ of a spacelike slice $\Sigma$ in a Lorentzian spacetime $(M, g)$: $K_{ij} = -\frac{1}{2}\mathcal{L}_n g_{ij}|_\Sigma$, where $n$ is the unit normal to $\Sigma$. This is the second fundamental form of the slice viewed as a submanifold of spacetime, and it plays a central role in the [[General Relativity I — Einstein's Equations and Schwarzschild|3+1 formulation of Einstein's equations]] (the ADM formalism) and in the Gauss–Codazzi equations relating the intrinsic and extrinsic curvature of slices to the spacetime curvature.

In **convex geometry**, the second fundamental form of a convex hypersurface is positive semi-definite, and the principal curvatures encode the "support function" — the basis for the **Brunn–Minkowski inequality** and its descendants.

In **continuum mechanics**, $\mathrm{II}$ on the surface of a deformable body governs how the body resists out-of-plane deformations (bending energy), in contrast to in-plane stretching governed by $\mathrm{I}$.

**True name:** The second fundamental form is *the normal projection of the acceleration of any tangent curve*. The official "$\mathrm{II}(X, Y) = -\langle dN(X), Y\rangle$" is the right formula, but the operational picture is Meusnier's: $\mathrm{II}(T, T)$ is the **normal curvature** of the surface in the direction $T$ — what you would measure if you took the plane through $p$ spanned by $T$ and $N$, intersected it with $M$, and measured the curvature of the resulting plane curve.

---

# Examples / Corollaries

**Is an instance — the plane $z = 0$.** Take $\mathbf{x}(u, v) = (u, v, 0)$, $N = (0, 0, 1)$. Then $N_u = N_v = 0$, so $\mathrm{II} \equiv 0$. Every direction has zero normal curvature, $\kappa_1 = \kappa_2 = 0$, $K = H = 0$. The plane is the prototypical flat surface.

**Is an instance — the unit sphere with outward normal.** $\mathbf{x}(p) = p$, $N(p) = p$. The differential $dN = \mathrm{id}$ as a linear map (the position vector equals the normal vector), so $\mathrm{II}(X, Y) = -\langle dN(X), Y\rangle = -\langle X, Y\rangle = -\mathrm{I}(X, Y)$. With Frankel's sign convention, principal curvatures are $-1$ (the shape operator has matrix $-\mathrm{Id}$); with the opposite convention they are $+1$. Under either convention $K = +1$ and $H$ has the same sign as the chosen convention. See [[Ex - Gauss Curvature of the Sphere of Radius R is 1 over R Squared]].

**Is an instance — the cylinder of radius $a$ around the $z$-axis.** With $\mathbf{x}(u, v) = (a\cos u, a\sin u, v)$ and outward normal $N = (\cos u, \sin u, 0)$, one computes $\mathbf{x}_{uu} = (-a\cos u, -a\sin u, 0) = -aN$, $\mathbf{x}_{uv} = (0, 0, 0)$, $\mathbf{x}_{vv} = (0, 0, 0)$. So $b_{11} = \langle\mathbf{x}_{uu}, N\rangle = -a$, $b_{12} = 0$, $b_{22} = 0$. The matrix $(b_{\alpha\beta}) = \mathrm{diag}(-a, 0)$, with principal curvatures $\kappa_1 = -1/a$ (in the $u$-direction) and $\kappa_2 = 0$ (in the $v$-direction). So $K = 0$, $H = -1/a$ — the cylinder is flat ($K = 0$) but extrinsically curved ($H \neq 0$).

**Is an instance — the saddle $z = x^2 - y^2$ at the origin.** With $\mathbf{x}(u, v) = (u, v, u^2 - v^2)$, at the origin $\mathbf{x}_u = (1, 0, 0)$, $\mathbf{x}_v = (0, 1, 0)$, so $E = G = 1$, $F = 0$, $N = (0, 0, 1)$ at origin. $\mathbf{x}_{uu} = (0, 0, 2)$, $\mathbf{x}_{vv} = (0, 0, -2)$, $\mathbf{x}_{uv} = 0$. So $b_{11} = 2$, $b_{22} = -2$, $b_{12} = 0$. Principal curvatures at origin are $\kappa_1 = 2$, $\kappa_2 = -2$, giving $K = -4 < 0$ (hyperbolic point) and $H = 0$ (minimal).

**Is NOT an instance — a non-symmetric "form".** Suppose one tried to define $\widetilde{\mathrm{II}}(X, Y) = -\langle dN(X), Y\rangle$ but neglected to check symmetry; one might expect it to fail. In fact, symmetry of $\mathrm{II}$ is *automatic* from the smoothness of $\mathbf{x}$ (equality of mixed partials), so any "non-symmetric" $\widetilde{\mathrm{II}}$ on a smooth surface is just a calculation error. The symmetry is a theorem, not an axiom.

**Is NOT an instance — a "second fundamental form" without a normal.** Without a choice of normal $N$, the formula $\mathrm{II} = \langle\mathbf{x}_{\alpha\beta}, N\rangle\, du^\alpha du^\beta$ is undefined. On a non-orientable surface (Möbius strip), no global $N$ exists, and the second fundamental form does not exist globally — though it does exist locally on each orientation-preserving chart, with a sign ambiguity. This is one reason classical surface theory assumes orientability.

**Corollary — the second fundamental form vanishes iff the surface is a piece of a plane.** If $\mathrm{II} \equiv 0$ on a connected open set, then $b_{\alpha\beta} = 0$, so $dN \equiv 0$, so $N$ is constant — i.e., the tangent plane to $M$ does not change as one moves on $M$. A surface with constant tangent plane is contained in a plane. Conversely a plane has $\mathrm{II} = 0$. So planar pieces are exactly the totally [[Def - Geodesic|geodesic]] surfaces of $\mathbb{R}^3$.

**Corollary — Meusnier's theorem.** For any curve $C$ on $M$ through $p$ with unit tangent $T$, the curvature vector $\dot T$ has normal component $\langle \dot T, N\rangle = \mathrm{II}(T, T)$, depending only on $T$. So the "normal-section curvature" in direction $T$ is the same as the "oblique-section curvature" up to a $\cos\phi$ factor: $\kappa_C = \mathrm{II}(T,T)/\cos\phi$ for a curve $C$ whose principal normal makes angle $\phi$ with $N$. This is a strong constraint on which curves can lie on a surface — Bertrand's theorem and Joachimsthal's theorem on lines of curvature are downstream consequences.

**Corollary — the equation $\mathrm{II}(X, X) = 0$ defines the **asymptotic directions** at $p$.** A tangent direction $T$ is **asymptotic** if $\mathrm{II}(T, T) = 0$, i.e., the normal curvature in that direction vanishes. On an elliptic point ($K > 0$), no asymptotic directions exist; on a parabolic point ($K = 0$), one asymptotic direction; on a hyperbolic point ($K < 0$), two asymptotic directions. The asymptotic curves (integral curves of asymptotic directions) play a special role in classical surface theory.

**Calibration check.** If you have understood the definition, you should be able to: (i) verify that for the graph $z = f(x, y)$, the matrix of $\mathrm{II}$ at the origin (where $f(0,0) = 0$ and $\nabla f(0,0) = 0$, achieved by choosing coordinates so that the tangent plane at the origin is $z = 0$) is the Hessian $f_{ij}(0)$, giving $K = \det\nabla^2 f$ and $H = \Delta f$ at the origin; (ii) check that under reversal of normal $N \to -N$, $\mathrm{II} \to -\mathrm{II}$, so $H \to -H$ but $K \to +K$ (the determinant of a $2 \times 2$ matrix is unchanged by sign reversal); (iii) compute that the second fundamental form of a surface of revolution $\mathbf{x}(u, v) = (r(v)\cos u, r(v)\sin u, z(v))$ is diagonal in $(u, v)$ coordinates whenever the meridian $(r(v), z(v))$ is parametrised by arc length.

---

# Unlocked by This

> [!tip] The Shape Operator *(from §4.1)*
> The bilinear form $\mathrm{II}$ has an associated linear operator $S : T_pM \to T_pM$ defined by $\mathrm{II}(X, Y) = \langle SX, Y\rangle$ — the [[Def - Shape Operator (Weingarten Map)|shape operator]] or **Weingarten map**, equal to $-dN$. Symmetry of $\mathrm{II}$ becomes self-adjointness of $S$, and the spectral theorem then gives [[Def - Principal Curvatures and Directions|principal curvatures and directions]].

> [!tip] The Gauss Curvature *(from §4.2)*
> The combination $K = \det\mathrm{II}/\det\mathrm{I} = (eg_\mathrm{II} - f^2)/(EG - F^2)$ is the [[Def - Gauss Curvature and Mean Curvature|Gauss curvature]]. The astonishing fact of [[Thm - Theorema Egregium of Gauss|Theorema Egregium]] is that this specific combination is *intrinsic* — depends only on the first fundamental form — even though both $\mathrm{II}$ individually and each $b_{\alpha\beta}$ are extrinsic.

> [!tip] Mean Curvature Flow *(from Geometric Analysis)*
> The mean curvature $H = \mathrm{tr}\,\mathrm{II}$ controls the first variation of area ([[Thm - First Variation of Area]]). The geometric heat equation $\partial_t \mathbf{x} = -HN$ — **mean curvature flow** — evolves a surface by its mean curvature vector, contracting it toward minimal surfaces. This flow plays a central role in **geometric measure theory**, **singularity formation in nonlinear PDE**, and (in higher dimensions) **Hamilton's Ricci flow** approach to the Poincaré conjecture.

> [!tip] The Gauss–Codazzi Equations *(from §4.3)*
> The integrability conditions for $(\mathrm{I}, \mathrm{II})$ to come from a surface in $\mathbb{R}^3$ are the [[Thm - Equations of Gauss and Codazzi|Gauss and Codazzi equations]], which express the intrinsic Riemann curvature in terms of $\mathrm{II}$ and impose compatibility constraints on the derivatives of $\mathrm{II}$. Bonnet's fundamental theorem says that any pair $(g_{\alpha\beta}, b_{\alpha\beta})$ satisfying these equations arises from a (locally unique) surface in $\mathbb{R}^3$.
