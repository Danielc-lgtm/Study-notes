---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Constant Sectional Curvature"
  - "Def - Riemannian Metric"
  - "Def - The Hyperbolic Space H^n"
tags: [geometry, riemannian-geometry, model-spaces]
---

# Notation

The three **model spaces** of constant sectional curvature are denoted $S^n_\kappa$ (sphere of curvature $\kappa > 0$), $\mathbb{R}^n$ (Euclidean space, curvature $0$), and $H^n_\kappa$ (hyperbolic space of curvature $-|\kappa| < 0$). When the curvature is normalised to $\pm 1$ or $0$ we drop the subscript and write $S^n, \mathbb{R}^n, H^n$. Rescaling the metric by a factor $\lambda^2$ rescales sectional curvature by $\lambda^{-2}$, so $S^n_\kappa$ is the sphere of radius $1/\sqrt{\kappa}$.

This is a **compound page**: it defines three interlocking notions — the round sphere $S^n$, Euclidean space $\mathbb{R}^n$, and hyperbolic space $H^n$ — because they are introduced together as the trichotomy of constant-curvature model spaces and none is fully usable in isolation from the comparison structure to the other two.

---

# Axiom Motivation

The desideratum is to name a single canonical Riemannian manifold for each value of constant sectional curvature, so that *comparison theorems* in Riemannian geometry can refer to "the model space of curvature $K_0$." This is what makes Bonnet–Myers's bound "$\mathrm{diam} \le \pi/\sqrt{\kappa}$" — comparison with $S^n_\kappa$ of diameter exactly $\pi/\sqrt{\kappa}$ — readable. The three model spaces are the *calibration points* of comparison geometry.

The fundamental result behind picking *these* particular three is the **Killing–Hopf theorem**: every complete simply-connected Riemannian manifold of constant sectional curvature is isometric to exactly one of $S^n_\kappa$, $\mathbb{R}^n$, or $H^n_\kappa$ (up to rescaling). So the trichotomy is forced — there is no choice. The three model spaces exhaust the possibilities, each one for a sign of curvature.

Why insist on simple connectedness? Because constant-curvature manifolds with nontrivial $\pi_1$ — the **space forms** — are quotients of the simply-connected models: $\mathbb{RP}^n = S^n/\{\pm 1\}$ (spherical space form), $T^n = \mathbb{R}^n/\mathbb{Z}^n$ (flat space form), compact hyperbolic surfaces and $3$-manifolds (hyperbolic space forms). The model spaces are the universal covers; quotients give the rest. By fixing the simply-connected representative we get a canonical reference point.

Why does the trichotomy mirror the trichotomy in surface theory ($S^2$, $\mathbb{R}^2$, $H^2$)? Because the higher-dimensional constructions are direct generalisations. $S^n \subset \mathbb{R}^{n+1}$ with the induced metric; $\mathbb{R}^n$ with the flat metric; $H^n$ as the upper half-space with the conformally-flat metric $g = |dx|^2/x_n^2$, or as the hyperboloid in Minkowski $(1, n)$-space. Each model has multiple equivalent descriptions, all isometric.

---

# The Definition

> **Definition (Sphere model $S^n$).** The **round $n$-sphere** is
>
> $$S^n := \{x \in \mathbb{R}^{n+1} : |x|^2 = 1\}$$
>
> with the metric $g$ induced from the Euclidean inner product on $\mathbb{R}^{n+1}$ via the inclusion $S^n \hookrightarrow \mathbb{R}^{n+1}$. It has constant sectional curvature $K \equiv 1$ (so $\mathrm{Ric} = (n-1)g$, $S = n(n-1)$), diameter $\pi$, and volume $\omega_n := \mathrm{vol}(S^n) = 2\pi^{(n+1)/2}/\Gamma((n+1)/2)$. The isometry group is $\mathrm{O}(n+1)$; the rotation subgroup $\mathrm{SO}(n+1)$ acts transitively, with stabiliser $\mathrm{O}(n)$ at any point, giving the homogeneous-space presentation $S^n = \mathrm{O}(n+1)/\mathrm{O}(n)$.

> **Definition (Euclidean model $\mathbb{R}^n$).** **Euclidean $n$-space** is $\mathbb{R}^n$ equipped with the standard flat metric $g = \sum (dx^i)^2$. It has constant sectional curvature $K \equiv 0$, infinite diameter, infinite volume, and the isometry group $E(n) = \mathbb{R}^n \rtimes \mathrm{O}(n)$ (Euclidean group: translations composed with rotations and reflections).

> **Definition (Hyperbolic model $H^n$).** **Hyperbolic $n$-space** is the upper half-space
>
> $$H^n := \{(x_1, \ldots, x_n) \in \mathbb{R}^n : x_n > 0\}$$
>
> with metric $g = (dx_1^2 + \cdots + dx_n^2)/x_n^2$. It has constant sectional curvature $K \equiv -1$ (so $\mathrm{Ric} = -(n-1)g$, $S = -n(n-1)$), infinite diameter, infinite volume, and isometry group $\mathrm{O}^+(1, n)$ (the identity component preserves the hyperboloid model's time-orientation; see [[Def - The Hyperbolic Space H^n]] for full definition). Geodesics in the upper half-space model are vertical lines and semicircles meeting the boundary $\{x_n = 0\}$ orthogonally.

**Killing–Hopf theorem.** Every complete simply-connected Riemannian $n$-manifold of constant sectional curvature $K_0$ is isometric to a rescaling of one of these three model spaces, the choice determined by $\mathrm{sgn}(K_0)$.

---

# Relate to Other Fields / Compression

In **homogeneous space theory**, the three model spaces are the three **isotropic Riemannian symmetric spaces of constant curvature**, each presented as $G/H$ where $G$ is the isometry group and $H = \mathrm{O}(n)$ is the stabiliser at a basepoint:

- $S^n = \mathrm{O}(n+1)/\mathrm{O}(n)$,
- $\mathbb{R}^n = (\mathbb{R}^n \rtimes \mathrm{O}(n))/\mathrm{O}(n)$,
- $H^n = \mathrm{O}^+(1, n)/\mathrm{O}(n)$.

These are the **rank-one symmetric spaces** of constant curvature; the higher-rank symmetric spaces are products and Grassmannians.

In **special and general relativity**, the Lorentzian analogues are:
- **de Sitter space** $\mathrm{dS}_n$, constant positive Lorentzian curvature, vacuum solution with $\Lambda > 0$;
- **Minkowski space** $\mathbb{R}^{1, n-1}$, flat Lorentzian, vacuum with $\Lambda = 0$;
- **Anti-de Sitter space** $\mathrm{AdS}_n$, constant negative Lorentzian curvature, vacuum with $\Lambda < 0$.

These three Lorentzian model spaces play the same calibration role in general relativity that the Riemannian models play in Riemannian geometry. **Anti-de Sitter** in particular features centrally in **AdS/CFT correspondence**.

In **classical non-Euclidean geometry**, $S^2$ is the prototype of **spherical** (or **elliptic**) geometry, where there are no parallel lines and triangles have angle sum exceeding $\pi$; $\mathbb{R}^2$ is **Euclidean** geometry; $H^2$ is **Bolyai–Lobachevsky** (**hyperbolic**) geometry, where through a point not on a line there are infinitely many parallels, and triangles have angle sum less than $\pi$.

**True name:** *The three model spaces are the maximally-symmetric Riemannian manifolds of each curvature sign: $S^n$ (positive), $\mathbb{R}^n$ (zero), $H^n$ (negative). They are the unique simply-connected complete representatives in each curvature class.* Every comparison theorem in Riemannian geometry reads as a statement of the form "manifold $M$ behaves no worse than the model space of the same curvature bound."

---

# Examples / Corollaries

**Example 1 (low-dimensional cases).** $S^2$ is the surface of a ball, Gauss curvature $1$, diameter $\pi$ along great-circle distance. $\mathbb{R}^2$ is the plane. $H^2$ is the **Poincaré upper half-plane**, also realised as the Poincaré disc $\{|z| < 1\}$ with metric $g = 4|dz|^2/(1-|z|^2)^2$. The hyperbolic plane is the model for non-Euclidean geometry.

**Example 2 (space-form quotients).** $\mathbb{RP}^n = S^n/\{\pm 1\}$ is a spherical space form: same constant curvature $1$, half the volume, fundamental group $\mathbb{Z}/2$. $T^n = \mathbb{R}^n/\mathbb{Z}^n$ is a Euclidean space form: $K \equiv 0$, compact, finite volume, fundamental group $\mathbb{Z}^n$. A compact hyperbolic surface of genus $g \ge 2$ is a hyperbolic space form: $K \equiv -1$, fundamental group a surface group (not a Lie group).

**Example 3 (volume comparison).** The volume of the geodesic ball of radius $r$ in $S^n$ is *less* than $\omega_n r^n$ for small $r$ (geodesics converge), in $\mathbb{R}^n$ is exactly $\omega_n r^n$, and in $H^n$ is *more* than $\omega_n r^n$ (geodesics diverge). The leading-order correction is $1 - S(p)r^2/(6(n+2)) + O(r^4)$, exhibiting the role of scalar curvature.

**Example 4 (sphere theorem context).** The sphere theorem says a simply-connected complete manifold with $1/4 < K \le 1$ is homeomorphic to $S^n$. The boundary case $K = 1/4$ is achieved by $\mathbb{CP}^n$ — a non-sphere — and $K = 1$ is the round sphere itself. So the model space $S^n$ sits at one end of the pinching interval and $\mathbb{CP}^n$ at the other.

**Non-example.** A flat torus $T^n$ is *not* a model space in our sense: it has constant curvature $0$ but is not simply connected. It is a *space form* (quotient of $\mathbb{R}^n$), but the model space is the universal cover $\mathbb{R}^n$.

**Calibration check.** If you have understood this compound definition correctly you should be able to: (a) state the constant sectional curvature of each model and the scaling rule under metric rescaling; (b) recall the diameter of $S^n$ (it is $\pi$, the maximal geodesic distance between two points); (c) recognise that $H^n$ has multiple isometric models (upper half-space, Poincaré disc, hyperboloid) and that each has its own computational advantages; (d) write down the homogeneous-space presentation $G/H$ for each.

---

# Unlocked by This

> [!tip] Comparison Geometry *(from Riemannian Geometry, advanced)*
> Almost every comparison theorem in Riemannian geometry is formulated by reference to a model space: **Rauch comparison** (Jacobi fields under $K \le K_0$ behave no worse than in the $K_0$-model), **Toponogov triangle comparison** (geodesic triangles under $K \le K_0$ are fatter than in the $K_0$-model), **Bishop–Gromov volume comparison** (geodesic balls under $\mathrm{Ric} \ge (n-1)\kappa\, g$ have volume bounded above by those in $S^n_\kappa$). The model spaces are the universal calibration points.

> [!tip] Hyperbolic 3-Manifolds *(from $3$-manifold topology)*
> **Hyperbolic $3$-manifolds** are quotients of $H^3$ by discrete isometry groups (**Kleinian groups**). By **Thurston's geometrization** (proved by Perelman), "most" closed $3$-manifolds admit a hyperbolic structure. **Mostow rigidity** ($1968$): a closed hyperbolic $3$-manifold's geometry is uniquely determined by its topology — the hyperbolic structure is a topological invariant. This is dramatically different from surfaces, where moduli spaces of hyperbolic structures are positive-dimensional.

> [!tip] Maximally Symmetric Spacetimes *(from General Relativity)*
> The Lorentzian analogues — **de Sitter**, **Minkowski**, **anti-de Sitter** — are the maximally symmetric spacetimes of GR, each a vacuum solution of Einstein's equations with cosmological constant of the matching sign. **De Sitter** is the leading model for an accelerating expanding universe (dark energy). **Anti-de Sitter** is the geometric arena for the **AdS/CFT correspondence** of string theory, relating gravity in $\mathrm{AdS}_{d+1}$ to a conformal field theory on its boundary.
