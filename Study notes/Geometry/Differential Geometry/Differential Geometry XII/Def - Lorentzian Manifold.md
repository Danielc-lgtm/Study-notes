---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Semi-Riemannian Metric and Signature"
  - "Def - Minkowski Space and the Metric"
tags: [geometry, differential-geometry, pseudo-riemannian-geometry, lorentzian-geometry]
---

# Notation

A Lorentzian manifold is a pair $(M, g)$ with $M$ a smooth $n$-manifold and $g$ a [[Def - Semi-Riemannian Metric and Signature|semi-Riemannian metric]] of signature $(1, n-1)$ (Lee's "mostly minus" convention used here). The flat Lorentzian manifold $(\mathbb{R}^n, \eta)$ with $\eta = \mathrm{diag}(1, -1, \ldots, -1)$ is the model, written $\mathbb{R}^{1, n-1}$; for $n = 4$, this is **Minkowski space** $\mathbb{M} = \mathbb{R}^{1, 3}$. Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

> [!warning] Convention: signature
> Two conventions are in use:
> - **"Mostly minus"** $(1, n-1)$ — $\eta = \mathrm{diag}(1, -1, \ldots, -1)$ — used by Lee, by [[Special Relativity I — Lorentz Transformations and Minkowski Space|Special Relativity I]] in this vault, and by most general-relativity textbooks (MTW, Wald, Hawking-Ellis).
> - **"Mostly plus"** $(n-1, 1)$ — $\eta = \mathrm{diag}(-1, 1, \ldots, 1)$ — used by Carroll, by many field-theory textbooks, and natural when one wants the spatial part to look Euclidean.
>
> The two differ by an overall sign of $\eta$. Every invariant flips sign, but the physical content is identical. **Timelike** means $g(v, v) > 0$ in the mostly-minus convention and $g(v, v) < 0$ in the mostly-plus convention; *which sign means timelike depends on the convention*. We use the mostly-minus convention throughout, so $g(v, v) > 0$ is timelike.

---

# Axiom Motivation

The desideratum is to install on a smooth manifold the kind of geometric structure that supports a *causal* distinction between time and space — a structure on which the light cone exists, on which "before" and "after" are meaningful (along timelike worldlines), on which the special-relativistic kinematics of [[Special Relativity I — Lorentz Transformations and Minkowski Space|SR I]] makes sense locally. The flat case of all of this is Minkowski space, the affine space $\mathbb{R}^4$ equipped with the indefinite metric $\eta$ of signature $(1, 3)$. The curved generalisation — the geometry of an arbitrary smooth manifold $M$ equipped with a metric of the same signature — is the **Lorentzian manifold**.

The single design decision is signature, $(1, n-1)$. Everything else is forced. We need a smooth, symmetric, non-degenerate $(0, 2)$-tensor field (a [[Def - Semi-Riemannian Metric and Signature|semi-Riemannian metric]]) so that the inner-product-like machinery of Riemannian geometry — musical [[Def - Isomorphism|isomorphisms]], Levi-Civita connection, [[Def - Geodesic|geodesics]], curvature — is available. The specific signature $(1, n-1)$ is what produces the causal structure: at every tangent space, one direction is "timelike" (positive $g$-norm-squared in our convention) and $n - 1$ directions are "spacelike" (negative). This is precisely the local structure of Minkowski space, repeated at every point of the manifold.

**Why signature $(1, n-1)$ in particular?** Because that is the signature of [[Def - Minkowski Space and the Metric|Minkowski space]], which is the *empirical* model for spacetime in special relativity. The Michelson–Morley experiment, the constancy of the speed of light, the Lorentz transformations — all of these tell us that the local structure of spacetime is Minkowski-like. So the signature is fixed by physics: there is one time direction and three space directions, and the indefinite form between them is what produces the causal structure. The mathematical generalisation, then, is to allow $g$ to *vary* from point to point, while keeping the signature constant.

**Why is this a deep generalisation?** Because it is *exactly* what general relativity says spacetime is. Einstein's insight — the **equivalence principle** — is that gravity is not a force superimposed on a flat Minkowski background but a manifestation of the *curvature* of spacetime, encoded in the metric $g$ deviating from the constant $\eta$. The Einstein field equations $R_{\mu\nu} - \tfrac{1}{2}R\, g_{\mu\nu} = 8\pi G\, T_{\mu\nu}$ relate the curvature of $g$ to the matter content. The bridge from special relativity (constant $\eta$) to general relativity (varying $g$) is exactly the bridge from "Minkowski space" to "Lorentzian manifold". So the Lorentzian-manifold definition is the mathematical setting of all of relativistic gravitation.

**Why not signature $(n-1, 1)$?** It is the same theory up to an overall sign of $g$. The choice is a matter of convention (see the warning above). Both conventions appear in textbooks; we choose mostly-minus to align with [[Special Relativity I — Lorentz Transformations and Minkowski Space]].

**Why constant signature?** Because the causal structure must be globally coherent. If at some points the signature were $(1, 3)$ and at others $(3, 1)$ or $(2, 2)$, the notion of "timelike direction" would be inconsistent across $M$, and the causal structure of the manifold would not exist as a global notion. On a connected manifold, the signature of a non-degenerate symmetric form *is* automatically locally constant (eigenvalues vary continuously and cannot pass through zero), so the constraint is automatically satisfied — the constancy is a *consequence* of non-degeneracy plus connectivity, not an independent axiom.

**Why "Lorentzian" and not "pseudo-Riemannian of signature $(1, n-1)$"?** The name "Lorentzian" reflects the physical origin: the signature $(1, n-1)$ is the one whose [[Def - Isometry|isometry]] [[Def - Group|group]] includes the **Lorentz [[Def - Group|group]]** $O(1, n-1)$, named after H. A. Lorentz, who derived the special-relativistic coordinate transformations in 1899–1904 before Einstein's interpretive synthesis of 1905. So "Lorentzian manifold" is "manifold whose local pseudo-orthogonal group is the Lorentz group" — the manifold on which the Lorentz transformations act locally at every tangent space, generalising the global Lorentz invariance of flat Minkowski space.

**Per-axiom failure analysis:**

(a) *Use a Riemannian metric instead.* You get a Riemannian manifold (signature $(n, 0)$), with no causal structure. No light cone, no distinction between time and space, no timelike-spacelike trichotomy. Riemannian geometry is the geometry of *space*; Lorentzian is the geometry of *spacetime*. Both are mathematically rich, but they are genuinely different geometries.

(b) *Use signature $(p, q)$ with $p, q \geq 2$.* You get a higher-mixed-signature pseudo-Riemannian manifold (e.g., the neutral signature $(2, 2)$ in 4-D). These are mathematically interesting (twistor theory, self-dual gravity) but have no causal structure in the physical sense — there is no single "time direction" at each point but a multi-dimensional "timelike cone".

(c) *Drop non-degeneracy.* The musical isomorphism fails, the Levi-Civita connection construction breaks. You get a degenerate metric, used in sub-Riemannian or null-hypersurface geometry, but not in semi-Riemannian geometry proper.

(d) *Drop the constancy of signature.* Allow the signature to change across the manifold. On a connected manifold this would require the metric to become degenerate at the transition, which is excluded by non-degeneracy. On a disconnected manifold, different components could have different signatures, but then "the signature of $(M, g)$" is not a single number — and the global causal structure is not coherent.

---

# The Definition

> **Definition (Lorentzian Manifold).** A **Lorentzian manifold** is a pair $(M, g)$, where $M$ is a smooth $n$-manifold and $g$ is a [[Def - Semi-Riemannian Metric and Signature|semi-Riemannian metric]] on $M$ of signature $(1, n-1)$ (or, in the opposite convention, $(n-1, 1)$).

A **spacetime** in physics is typically a 4-dimensional Lorentzian manifold, often with additional structure (orientation, time orientation, connectedness, sometimes a fixed asymptotic structure).

The signature condition means: at every $p \in M$ there is a basis of $T_pM$ in which the matrix of $g_p$ is $\mathrm{diag}(1, -1, \ldots, -1)$ (one positive, $n-1$ negative entries; "mostly minus" convention). Equivalently: at every $p$, the bilinear form $g_p$ has exactly one positive eigenvalue and $n-1$ negative eigenvalues. By Sylvester's law of inertia (and the connectedness of $M$), the signature is constant.

A **pseudo-orthonormal frame** at $p$ is a basis $(e_0, e_1, \ldots, e_{n-1})$ of $T_pM$ with $g(e_0, e_0) = 1$, $g(e_i, e_i) = -1$ for $i = 1, \ldots, n-1$, and $g(e_i, e_j) = 0$ for $i \neq j$. The vector $e_0$ is the **timelike direction**, and the $e_i$ are the **spatial directions**.

**The causal classification of vectors at $p$** is a fundamental immediate consequence; see [[Def - Causal Classification of Tangent Vectors]] for the full definition.

---

# Categorical / Structural Definition

A Lorentzian manifold of [[Def - Dimension|dimension]] $n$ is a smooth manifold $M$ equipped with a reduction of the structure group of $TM$ from $GL(n, \mathbb{R})$ to the **Lorentz group** $O(1, n-1)$. This reduction is the data of a pseudo-orthonormal frame at every point, defined up to $O(1, n-1)$ changes of frame.

The Lorentz group $O(1, n-1)$ in $n$ [[Def - Dimension|dimensions]] has dimension $n(n-1)/2$ (the same as $O(n)$, since the dimension counts antisymmetric matrices in the relevant pseudo-orthonormal Lie algebra). For $n = 4$ it has dimension $6$: three boosts and three spatial rotations.

A **time orientation** is a further choice: at each point, a continuous choice of one of the two halves of the timelike cone (future-directed vs. past-directed). Equivalently, a smooth nowhere-vanishing timelike vector field, or a reduction of structure group from $O(1, n-1)$ to its orthochronous [[Def - Subgroup|subgroup]] $O^\uparrow(1, n-1)$ (the [[Def - Subgroup|subgroup]] preserving time orientation). Not every Lorentzian manifold is time-orientable, and time-orientability is an additional topological condition.

A **spacetime** in the most refined sense is a connected, oriented, time-oriented, 4-dimensional Lorentzian manifold.

The category $\mathbf{Lor}$ has Lorentzian manifolds as objects and smooth maps preserving the Lorentzian metric (Lorentzian [[Def - Isometry|isometries]]) as morphisms. It is a higher-structured version of the smooth category, just as Riemannian manifolds form $\mathbf{Riem}$.

---

# Relate to Other Fields / Compression

This is the natural setting for relativistic physics. [[Special Relativity I — Lorentz Transformations and Minkowski Space|Special relativity]] is the case where $M = \mathbb{R}^4$ and $g = \eta$ is constant (the flat case). General relativity is the case where $M$ is a four-dimensional smooth manifold and $g$ is a dynamical Lorentzian metric obeying the Einstein equations. The bridge is the **equivalence principle**: at every event there is a locally inertial frame in which $g_{\mu\nu}$ reduces to $\eta_{\mu\nu}$ and its first derivatives vanish, so [[Special Relativity I — Lorentz Transformations and Minkowski Space|special relativity]] holds exactly at that event. Curvature is the obstruction to this reduction being global. So a Lorentzian manifold is *locally* always Minkowski; the global geometry can be wildly curved.

In mathematics, Lorentzian geometry sits inside [[Def - Semi-Riemannian Metric and Signature|semi-Riemannian geometry]] as the signature-$(1, n-1)$ slice. The general theory of semi-Riemannian connections, geodesics, curvature, and the Levi-Civita connection ([[Thm - Fundamental Theorem of Riemannian Geometry (Statement)]]) applies, with the understanding that the indefiniteness changes what "length" means: timelike vectors have positive length squared and spacelike have negative, with null vectors in between.

The **causal structure** of a Lorentzian manifold — the partition of tangent vectors into [[Def - Causal Classification of Tangent Vectors|timelike, spacelike, null]] and the resulting global causal partial order on events — is the *new* feature compared to Riemannian geometry. The theorems of **Penrose** and **Hawking** on causal structure (chronology, causality, strong causality, global hyperbolicity, the singularity theorems) live here. There is no Riemannian analogue.

**True name:** A Lorentzian manifold is *a smooth manifold whose tangent spaces all look like Minkowski space*. Locally — in a tangent space at one event — the geometry is exactly that of [[Special Relativity I — Lorentz Transformations and Minkowski Space|special relativity]]. Globally — across all of $M$ — the metric can vary and produce curvature, which is the mathematical content of gravitation.

---

# Examples / Corollaries

**Is an instance — Minkowski space $(\mathbb{R}^n, \eta)$.** The flat Lorentzian manifold, with $\eta = \mathrm{diag}(1, -1, \ldots, -1)$. The whole content of [[Special Relativity I — Lorentz Transformations and Minkowski Space|special relativity]] is the geometry of $(\mathbb{R}^4, \eta)$. The isometry group is the Poincaré group $O(1, 3) \ltimes \mathbb{R}^{1, 3}$, with the Lorentz group $O(1, 3)$ as the part fixing the origin. See [[Def - Minkowski Space and the Metric]] and [[Ex - Minkowski Space as the Flat Lorentzian Manifold]].

**Is an instance — Schwarzschild spacetime.** The 4-dimensional Lorentzian manifold $M = \mathbb{R}_t \times (2GM, \infty)_r \times S^2$ with metric
$$
g = \left(1 - \frac{2GM}{r}\right) dt^2 - \left(1 - \frac{2GM}{r}\right)^{-1} dr^2 - r^2 \mathring g_{S^2}
$$
(in geometric units, $c = 1$). This is the exterior of a static, spherically symmetric black hole; it solves the vacuum Einstein equations. The Schwarzschild metric is *not* flat — its curvature decays as $1/r^3$ — and timelike [[Def - Geodesic|geodesics]] are bent towards $r = 2GM$, the **event horizon**.

**Is an instance — the de Sitter universe.** A 4-dimensional Lorentzian manifold with constant positive curvature, solving the Einstein equations with cosmological constant $\Lambda > 0$ and no matter. Topologically $\mathbb{R} \times S^3$, with metric in static coordinates
$$
g = (1 - \tfrac{\Lambda r^2}{3}) dt^2 - (1 - \tfrac{\Lambda r^2}{3})^{-1} dr^2 - r^2\, d\Omega^2_{S^2}.
$$
This is the simplest curved Lorentzian spacetime and the de Sitter model of cosmology.

**Is an instance — FRW (Friedmann–Robertson–Walker) cosmology.** The Lorentzian metric
$$
g = dt^2 - a(t)^2 \mathring g_\Sigma
$$
on $\mathbb{R} \times \Sigma$, with $\Sigma$ a Riemannian 3-manifold of constant curvature and $a(t)$ a "scale factor" function. These are the homogeneous, isotropic cosmological models on which modern cosmology is built. The Big Bang corresponds to a coordinate singularity where $a(t) \to 0$, and the metric becomes degenerate at $t = 0$.

**Is NOT an instance — the 2-sphere $(S^2, \mathring g)$.** $S^2$ admits no Lorentzian metric at all: the [[Thm - A Lorentzian Manifold Need Not Exist on Every Smooth Manifold|hairy-ball obstruction]] says no nowhere-vanishing line field exists on $S^2$, but a Lorentzian metric requires one. The 2-sphere is a Riemannian manifold (with the round metric) but never a Lorentzian one.

**Is NOT an instance — $(\mathbb{R}^4, g)$ with $g$ Riemannian.** The same smooth manifold $\mathbb{R}^4$ underlies both Minkowski space and 4-dimensional Euclidean space, but the latter is a Riemannian manifold (signature $(4, 0)$) and the former is Lorentzian (signature $(1, 3)$). They have entirely different geometric content.

**Corollary — the causal structure is global.** On a Lorentzian manifold the [[Def - Causal Classification of Tangent Vectors|trichotomy]] of timelike-spacelike-null applies at every tangent space, and the local light cones piece together globally into the **causal structure**: a partial order on events recording which events can causally influence which. This is the central new feature of Lorentzian over Riemannian geometry.

**Corollary — every Lorentzian manifold is locally Minkowski.** Around any point $p$ there are coordinates in which $g_{\mu\nu}(p) = \eta_{\mu\nu}$ and $\partial_\rho g_{\mu\nu}(p) = 0$ — the **Riemann normal coordinates** of the Levi-Civita connection. These are the **locally inertial coordinates** of the equivalence principle: at $p$, the geometry is Minkowski; the deviation from Minkowski is encoded in second derivatives of $g$, which are the curvature.

**Corollary — geodesic classification.** A geodesic $\gamma$ on a Lorentzian manifold has the property that $g(\dot\gamma, \dot\gamma)$ is constant along $\gamma$ (parallel transport preserves $g$-norm). So a geodesic that is timelike at one point is timelike everywhere, and similarly for spacelike and null. **Timelike geodesics** are the worldlines of free-falling massive particles; **null geodesics** are the worldlines of light; **spacelike geodesics** are "spatial straight lines" with no direct physical interpretation as a particle trajectory.

**Calibration check.** First, verify that the metric $g = dt^2 - dx^2 - dy^2 - dz^2$ on $\mathbb{R}^4$ is Lorentzian of signature $(1, 3)$ (using Lee's convention). Second, identify which of the following are Lorentzian manifolds: (i) $S^1 \times \mathbb{R}^3$ with metric $d\theta^2 - dx^2 - dy^2 - dz^2$ (yes — this is a closed-time-curve toy spacetime); (ii) $S^2$ with the round metric (no — wrong signature, and even with the right ambition the round metric is Riemannian); (iii) the 4-torus $T^4 = \mathbb{R}^4 / \mathbb{Z}^4$ with the quotient Minkowski metric (yes — this is a "compactified Minkowski" with closed timelike curves). Third, verify the signature of $g = -dt^2 + dx^2 + dy^2 + dz^2$ (mostly-plus convention) is $(3, 1)$; identify the timelike vectors (those with $g(v, v) < 0$ in this convention) — this is the convention shift, the physical content is identical.

---

# Unlocked by This

> [!tip] The Causal Classification of Tangent Vectors *(from §12.4)*
> Every tangent vector on a Lorentzian manifold is exactly one of timelike, spacelike, or null; see [[Def - Causal Classification of Tangent Vectors]]. This trichotomy is invariant under isometries and is the local model for the global causal structure of spacetime.

> [!tip] The Lorentz Group as Local Isometry Group *(from Group Theory and Special Relativity)*
> The group of linear isometries of $T_pM$ as a Lorentzian inner product space is the **Lorentz group** $O(1, n-1)$ — the same group that acts on flat [[Def - Minkowski Space and the Metric|Minkowski space]]. In a Lorentzian manifold, this Lorentz group acts at every tangent space, with no canonical way to compare frames at different points: this is **local Lorentz invariance**, which replaces the global Lorentz invariance of flat special relativity. See [[Def - The Lorentz Group]].

> [!tip] General Relativity — The Einstein Field Equations *(from General Relativity)*
> Once we have committed to "spacetime is a 4-dimensional Lorentzian manifold", the dynamics of the metric is governed by the **Einstein field equations**:
> $$
> R_{\mu\nu} - \tfrac{1}{2} R\, g_{\mu\nu} + \Lambda\, g_{\mu\nu} \;=\; 8\pi G\, T_{\mu\nu},
> $$
> where $R_{\mu\nu}$ is the Ricci tensor of the Levi-Civita connection of $g$, $R$ is the scalar curvature, $\Lambda$ is the cosmological constant, $G$ is Newton's constant, and $T_{\mu\nu}$ is the energy–momentum tensor of matter. The left-hand side is curvature; the right-hand side is matter. The equations are nonlinear coupled second-order PDEs in $g_{\mu\nu}(x)$, and their solutions include flat Minkowski space, Schwarzschild and Kerr black holes, FRW cosmologies, gravitational wave spacetimes, and the asymptotically flat solutions modelling isolated systems. The whole subject of **mathematical general relativity** is the study of these equations, their well-posedness as a Cauchy problem (Choquet-Bruhat, Geroch), the structure of their solutions, and the global properties of solution manifolds.

> [!tip] Causal Structure and the Penrose–Hawking Singularity Theorems *(from Mathematical General Relativity)*
> The causal structure of a Lorentzian manifold — chronological and causal future/past, achronal sets, Cauchy surfaces, global hyperbolicity — is a rich geometric structure with no Riemannian analogue. The **Penrose** and **Hawking** singularity theorems use causal-structure arguments combined with energy conditions (positivity properties of $T_{\mu\nu}$) and the Raychaudhuri equation to prove that singularities (geodesic incompleteness) are inevitable under physically reasonable conditions — generic gravitational collapse produces a singular interior, and any expanding universe satisfying the energy conditions must have had a beginning (the Big Bang). These are some of the deepest theorems in mathematical physics and exhibit the unique flavour of Lorentzian geometry.

> [!tip] Global Lorentzian Geometry *(from Differential Topology)*
> The existence question for Lorentzian metrics — settled by [[Thm - A Lorentzian Manifold Need Not Exist on Every Smooth Manifold]] — has a positive resolution exactly when the manifold admits a nowhere-vanishing line field. The further question of which Lorentzian manifolds are **time-orientable**, **causal** (no closed timelike curves), **strongly causal**, **stably causal**, **globally hyperbolic** — the **causal hierarchy** — is the subject of global Lorentzian geometry. Globally hyperbolic spacetimes are diffeomorphic to $\mathbb{R} \times \Sigma$ with $\Sigma$ a smooth manifold (the Geroch–Bernal–Sánchez theorem), and they are the well-behaved setting for the initial value problem of general relativity.
