---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Riemannian Metric"
  - "Def - Constant Sectional Curvature"
tags: [geometry, riemannian-geometry, hyperbolic-geometry]
---

# Notation

$H^n$ denotes hyperbolic $n$-space. We adopt the **upper-half-space model** as the primary definition, with coordinates $(x_1, \ldots, x_n)$ and $x_n > 0$. Other models — Poincaré ball, hyperboloid, Klein — are introduced as equivalent presentations. The isometry group is $\mathrm{Iso}(H^n) = \mathrm{O}^+(1, n)$, the identity-component preserves time-orientation of the hyperboloid model.

This is a **compound page**: it defines $H^n$ via four interlocking models — upper half-space, Poincaré ball, hyperboloid, Klein — because each model is computationally convenient in a different setting, and none alone is fully usable in isolation.

---

# Axiom Motivation

We want to construct a complete simply-connected Riemannian $n$-manifold of constant sectional curvature $-1$. By the **Killing–Hopf theorem**, such a manifold is unique up to isometry; the question is what its explicit construction looks like.

The most direct route is to mimic the construction of the sphere — $S^n$ is the level set $\{|x|^2 = 1\}$ in $\mathbb{R}^{n+1}$ with the induced *positive-definite* inner product. The hyperbolic analogue uses Minkowski $\mathbb{R}^{1, n}$ with the Lorentzian inner product $\langle x, y\rangle_{\mathrm{Mink}} = -x_0 y_0 + x_1 y_1 + \cdots + x_n y_n$, and the level set $\{\langle x, x\rangle_{\mathrm{Mink}} = -1, x_0 > 0\}$ — the **hyperboloid**. The induced metric on this hyperboloid (restricted from the indefinite metric) turns out to be Riemannian (positive-definite on the tangent space at each hyperboloid point) and has constant sectional curvature $-1$. This is the hyperboloid model.

The hyperboloid model is geometrically clean and makes the isometry group transparent: it is the subgroup of Lorentz transformations $\mathrm{O}(1, n)$ preserving the hyperboloid (the time-orientation-preserving part $\mathrm{O}^+(1, n)$). But for computation in low dimensions, the **upper half-space model** is much more convenient: a single chart, no embedding in higher-dimensional ambient space, and a conformally-flat metric $g = |dx|^2/x_n^2$ that makes the geodesics easy to identify (vertical lines and semicircles meeting $\{x_n = 0\}$ orthogonally).

The desiderata for the half-space metric $g = |dx|^2/x_n^2$ are: (i) it should be **conformally flat** so that angles match the Euclidean angles in the half-space; (ii) it should have constant negative curvature; (iii) the boundary $\{x_n = 0\}$ should be at infinite distance, making the half-space complete. All three are realised: angles match by construction (conformality); the conformal factor $1/x_n^2$ is the unique radial profile producing constant curvature $-1$; and the integral $\int_0^1 dx_n/x_n = \infty$ shows the boundary is at infinite distance.

Why is hyperbolic space "harder to picture" than the sphere? Because it cannot be **isometrically embedded** in any Euclidean space of finite dimension (Hilbert's theorem rules out isometric embedding of even $H^2$ in $\mathbb{R}^3$ — the hyperbolic plane is "too big" to fit). The hyperboloid embedding works only because it uses indefinite Lorentzian ambient signature. So all our pictures of hyperbolic space are *distortions* — the disc and half-space models distort distances near the boundary, the Klein model distorts angles, and so on.

---

# The Definition

> **Definition (Hyperbolic $n$-space — primary form).** Hyperbolic $n$-space $H^n$ is the manifold
>
> $$H^n := \{(x_1, \ldots, x_n) \in \mathbb{R}^n : x_n > 0\}$$
>
> with the **upper-half-space metric**
>
> $$g_{H^n} := \frac{dx_1^2 + dx_2^2 + \cdots + dx_n^2}{x_n^2}.$$
>
> It is a complete Riemannian manifold of constant sectional curvature $-1$, diffeomorphic to $\mathbb{R}^n$, with diameter $\infty$ and volume $\infty$.

**Equivalent models** (all isometric to the above):

**Poincaré ball model.** $\mathbb{B}^n := \{x \in \mathbb{R}^n : |x| < 1\}$ with metric
$$g_{\mathbb{B}^n} = \frac{4(dx_1^2 + \cdots + dx_n^2)}{(1 - |x|^2)^2}.$$
The isometry $\mathbb{B}^n \to H^n$ is the **inversion through a sphere** centred on the boundary.

**Hyperboloid (Minkowski) model.** $\mathbb{H}^n := \{x \in \mathbb{R}^{1, n} : \langle x, x\rangle_{\mathrm{Mink}} = -1, x_0 > 0\}$ with the induced metric. This makes the isometry group $\mathrm{O}^+(1, n)$ manifestly the structure-preserving group.

**Klein (projective) model.** $\mathbb{K}^n := \{x \in \mathbb{R}^n : |x| < 1\}$ as a set, but with the metric inherited via gnomonic projection from the hyperboloid. Geodesics are straight chords. The metric is *not* conformally flat — angles are distorted — but geodesics are the simplest possible (Euclidean line segments).

All four models are isometric. The choice of model depends on the calculation:
- **Upper half-space**: conformal calculations, special role of "infinity" $\{x_n \to 0\}$.
- **Ball**: conformal calculations with symmetric boundary, picture of "the whole of hyperbolic space inside a Euclidean ball."
- **Hyperboloid**: isometry-group calculations, analogue of $S^n \subset \mathbb{R}^{n+1}$.
- **Klein**: geodesic calculations (straight lines), parallel postulate visualisation.

**Geodesics in the upper half-space model.** Vertical lines $\{(x_1, \ldots, x_{n-1}, t) : t > 0\}$ for fixed $(x_1, \ldots, x_{n-1})$, and Euclidean semicircles meeting the boundary $\{x_n = 0\}$ orthogonally. Both are infinite-length curves.

---

# Relate to Other Fields / Compression

In **complex analysis**, the Poincaré disc $\mathbb{B}^2 = \mathbb{D}$ is the unit disc in $\mathbb{C}$, and the Poincaré metric $g = 4|dz|^2/(1 - |z|^2)^2$ is the unique Hermitian metric (up to scaling) on the disc that is invariant under the **Möbius transformations** preserving the disc. The isometry group is $\mathrm{PSL}(2, \mathbb{R})$ acting via Möbius transformations.

In **number theory**, the upper half-plane $H^2 = \{z \in \mathbb{C} : \mathrm{Im}(z) > 0\}$ is the domain of **modular forms** and **automorphic forms**. The modular group $\mathrm{SL}(2, \mathbb{Z})$ acts on $H^2$ by Möbius transformations, and the quotient $H^2/\mathrm{SL}(2, \mathbb{Z})$ is the moduli space of elliptic curves.

In **special relativity**, the hyperboloid model is exactly the **mass shell** for a particle of mass $1$ in Minkowski space: the set of $4$-velocities $\langle u, u\rangle = -1$ with $u^0 > 0$ is a $3$-dimensional hyperboloid in $\mathbb{R}^{1, 3}$, which is isometric to $H^3$. The set of possible velocities forms a hyperbolic geometry; **rapidity** is the natural hyperbolic-distance parameter.

In **architecture and biology**, hyperbolic surfaces appear in nature: the saddle-shaped surfaces of certain ruffled leaves, sea slugs, and coral, can be modelled as immersed hyperbolic surfaces (locally). Their excess perimeter relative to area is the defining hyperbolic feature.

**True name:** *Hyperbolic $n$-space is the unique simply-connected complete Riemannian $n$-manifold of constant sectional curvature $-1$. It is realised by the upper half-space, Poincaré ball, hyperboloid, and Klein models — each isometric, each computationally convenient in a different setting.* The operational picture: distances grow exponentially as you move toward the boundary in the disc/half-space models; geodesic divergence is exponential, in stark contrast to the polynomial divergence in Euclidean space.

---

# Examples / Corollaries

**Example 1 ($H^2$ in the upper half-plane).** The hyperbolic plane $H^2 = \{(x, y) : y > 0\}$ with $g = (dx^2 + dy^2)/y^2$ has constant Gauss curvature $K = -1$. Geodesics are vertical lines $x = c$ and Euclidean semicircles with centres on the $x$-axis. Distance from $(0, 1)$ to $(0, e)$ along the vertical geodesic is $\int_1^e dy/y = 1$. The boundary $\{y = 0\}$ is at infinite distance: $\int_0^1 dy/y = \infty$.

**Example 2 (Poincaré disc, hyperbolic distance to the boundary).** In the disc model $\mathbb{B}^2$, hyperbolic distance from the origin to a point at Euclidean distance $r < 1$ is $d_H(0, x) = \log\bigl((1+r)/(1-r)\bigr)$. As $r \to 1$, $d_H \to \infty$ — the boundary is at infinite hyperbolic distance.

**Example 3 (hyperboloid as the mass shell).** In Minkowski $\mathbb{R}^{1, 3}$, the **mass shell** $\{u : \langle u, u\rangle_{\mathrm{Mink}} = -1, u^0 > 0\}$ is the set of $4$-velocities of a unit-mass particle. It is a 3D hyperboloid in $\mathbb{R}^4$, with induced metric of constant sectional curvature $-1$ — isometric to $H^3$. The **rapidity** parameter $\eta$ along a geodesic of this hyperboloid is the hyperbolic-distance analogue of arc length on the unit $3$-sphere.

**Example 4 (compact hyperbolic surfaces).** Every closed orientable surface of genus $g \ge 2$ admits a metric of constant Gauss curvature $-1$ — equivalently, is a quotient $H^2/\Gamma$ for some discrete subgroup $\Gamma \le \mathrm{PSL}(2, \mathbb{R})$ acting freely and properly discontinuously. The **uniformisation theorem** is the relevant rigidity result; the moduli space of such metrics on a genus-$g$ surface is the **Teichmüller space** $\mathcal{T}_g$, of real dimension $6g - 6$.

**Non-example (Hilbert's theorem).** $H^2$ cannot be isometrically immersed as a smooth $C^2$ submanifold of $\mathbb{R}^3$. The classical pseudosphere (a surface of revolution of the tractrix) achieves constant curvature $-1$ but has a singular edge; no smooth complete immersion exists. This is a deep obstruction first proved by **Hilbert** in 1901.

**Calibration check.** If you have understood this compound definition correctly you should be able to: (a) verify that the upper-half-space metric has Gauss curvature $-1$ (using Cartan's structural equations, see [[Ex - Sectional Curvature of the Hyperbolic Plane is -1]]); (b) state the geodesics in the upper-half-space and disc models; (c) recognise that all four models are isometric and recall the isometry between any two; (d) explain why the boundary $\{x_n = 0\}$ is at infinite distance (the integral $\int dx_n/x_n$ diverges).

---

# Unlocked by This

> [!tip] Mostow Rigidity *(from $3$-manifold topology)*
> **Mostow rigidity** ($1968$): a closed hyperbolic $n$-manifold of dimension $\ge 3$ is determined up to isometry by its homotopy type. In dimensions $\ge 3$, the hyperbolic structure is essentially unique. This is dramatically different from surfaces, where the **Teichmüller space** of hyperbolic structures on a genus-$g$ surface has dimension $6g - 6$. Mostow rigidity is the reason why hyperbolic $3$-manifolds carry numerical invariants like **hyperbolic volume** as topological invariants.

> [!tip] Modular Forms and the Upper Half-Plane *(from Number Theory)*
> The upper half-plane $H^2$ is the domain of **modular forms** for the modular group $\mathrm{SL}(2, \mathbb{Z})$. These are holomorphic functions transforming covariantly under $z \mapsto (az+b)/(cz+d)$, and they encode arithmetic information (Fourier coefficients give number-theoretic data: counts of representations of integers by quadratic forms, etc.). The connection between hyperbolic geometry and number theory is one of the most fertile in modern mathematics.

> [!tip] AdS/CFT Correspondence *(from String Theory)*
> The Lorentzian analogue of $H^n$ is **anti-de Sitter space** $\mathrm{AdS}_n$, a maximally symmetric Lorentzian manifold of constant negative curvature. The **AdS/CFT correspondence** (Maldacena, $1997$) conjectures a duality between quantum gravity in $\mathrm{AdS}_{d+1}$ and a conformal field theory on its boundary $\mathbb{R}^{1, d-1}$ — a precise realisation of the holographic principle.

> [!tip] Hyperbolic Geometry as Reference for the Sphere Theorem *(from Riemannian Geometry III)*
> The **Cartan–Hadamard theorem** says complete simply-connected manifolds with $K \le 0$ are diffeomorphic to $\mathbb{R}^n$ via the exponential map. In particular, $H^n$ itself satisfies this — it is diffeomorphic to $\mathbb{R}^n$. So $H^n$ serves as the "extremal example" for nonpositive-curvature theorems, much as $S^n$ serves as the extremal example for positive-curvature theorems.
