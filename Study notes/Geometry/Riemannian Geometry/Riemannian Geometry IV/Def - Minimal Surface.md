---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Gauss Curvature and Mean Curvature"
  - "Def - Shape Operator (Weingarten Map)"
  - "Thm - First Variation of Area"
tags: [geometry, riemannian-geometry, surfaces, minimal-surfaces, variational]
---

# Notation

Let $M \subset \mathbb{R}^3$ be an oriented regular surface (possibly with boundary) and $H$ its [[Def - Gauss Curvature and Mean Curvature|mean curvature]]. We use Frankel's convention $H = \kappa_1 + \kappa_2 = \mathrm{tr}\, S$ — for do Carmo's convention divide by $2$. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Axiom Motivation

The desideratum is to characterise the **equilibrium shape** of a thin elastic film spanning a wire frame — a soap film. Physically, surface tension produces a force proportional to the area of the film, and the film minimises this force by minimising its area subject to the boundary constraint. Mathematically, the equilibrium condition is that the **first variation** of area vanishes for every compactly supported deformation that fixes the boundary — and by the [[Thm - First Variation of Area|first variation of area formula]], this is equivalent to $H \equiv 0$. So the natural mathematical definition of a minimal surface is "$H = 0$ everywhere", which we adopt.

**Why "$H = 0$" rather than "smallest area among competitors"?** The naive definition "$M$ is minimal iff it minimises area among all surfaces with the same boundary" is too strong: most $H = 0$ surfaces (the catenoid, for instance) are only *critical* for area, not minimisers — they may be saddle points in the space of competitor surfaces (the catenoid spanning two coaxial circles loses to the disconnected "Goldschmidt solution" when the circles are far apart). The mathematical definition uses the criticality condition $\delta A = 0$ (first variation vanishes), which by the first-variation formula is exactly $H = 0$. So:
- "Minimal" in classical mathematics = critical point of area = $H = 0$.
- "Area-minimising" = global minimum among competitors. Stricter.

Some authors prefer "stationary surface" for $H = 0$ to avoid the misleading "minimal", but "minimal surface" is the entrenched terminology.

**Why does $H = 0$ correspond to vanishing first variation?** The first-variation formula reads $\delta A = -\int_M H\langle v, N\rangle\, dA + \int_{\partial M}\langle v, n\rangle\, ds$ for a variation field $v$ along $M$. If $v$ has compact support in the interior ($v = 0$ on $\partial M$), the boundary integral vanishes, and $\delta A = 0$ for all such $v$ iff the integrand $H\langle v, N\rangle$ vanishes for all $v$ — iff $H \equiv 0$ on the interior (by the fundamental lemma of the calculus of variations). This is the mathematical content: $H$ is the $L^2$-gradient of the area functional with respect to normal variations.

**Why does $H = 0$ force $K \leq 0$?** From $K \leq H^2/4$ (the inequality $\kappa_1\kappa_2 \leq ((\kappa_1+\kappa_2)/2)^2$ from AM-GM), $H = 0$ gives $K \leq 0$ with equality iff $\kappa_1 = \kappa_2 = 0$ (a flat point). So **minimal surfaces have non-positive Gauss curvature everywhere**, with flat points being the umbilic-of-minimal-surfaces. This is a strong restriction: a minimal surface cannot be elliptic ($K > 0$) at any point.

**Why does $H = 0$ in the parametric form give the **minimal surface equation**?** For a graph $z = f(x, y)$ over the $xy$-plane, the formula $H = ((1 + f_y^2)f_{xx} - 2f_xf_yf_{xy} + (1 + f_x^2)f_{yy})/(1 + |\nabla f|^2)^{3/2}$ gives $H = 0$ iff
$$
(1 + f_y^2)f_{xx} - 2f_xf_yf_{xy} + (1 + f_x^2)f_{yy} = 0,
$$
the **minimal surface equation** — a quasilinear elliptic second-order PDE. Solutions are exactly graph-form minimal surfaces. This is one of the oldest nonlinear PDEs in mathematics (studied by Lagrange in the 18th century) and the prototype of **geometric PDE**.

**Why is this definition stable under coordinate change?** The mean curvature $H$ is a geometric invariant (it depends only on $M$ and the choice of normal), so "$H = 0$" is a property of $M$ as a geometric object, independent of any parametrisation. Two surfaces obtained from each other by a rigid motion (isometry of $\mathbb{R}^3$) are simultaneously minimal or non-minimal.

A forward reference: the **Plateau problem** — for any closed Jordan curve $C \subset \mathbb{R}^3$, find a minimal surface with boundary $C$ — has solutions for every $C$ (Douglas, Radó, 1931), but the solutions may have singularities and may not be embedded. The full theory requires **geometric measure theory** (Federer–Fleming currents) and is one of the most developed parts of modern variational analysis. The mathematical study of minimal surfaces is a major branch of **geometric analysis** and continues to be highly active.

---

# The Definition

> **Definition (Minimal Surface).** An oriented regular surface $M \subset \mathbb{R}^3$ is **minimal** if its [[Def - Gauss Curvature and Mean Curvature|mean curvature]] vanishes everywhere:
> $$
> H(p) = \kappa_1(p) + \kappa_2(p) = 0 \quad\text{for all } p \in M.
> $$

Equivalently, by the [[Thm - First Variation of Area|first variation of area formula]], $M$ is minimal iff $\delta A = 0$ for every smooth one-parameter variation of $M$ that is supported in the interior of $M$ (i.e., the variation field $v$ vanishes on $\partial M$, if $M$ has boundary).

**Equivalent characterisations:**
1. $H \equiv 0$ on $M$.
2. The principal curvatures are everywhere opposite: $\kappa_1 = -\kappa_2$.
3. The shape operator is everywhere trace-free: $\mathrm{tr}\, S = 0$.
4. For graph $z = f(x, y)$ over the $xy$-plane: the **minimal surface equation** $(1 + f_y^2)f_{xx} - 2f_xf_yf_{xy} + (1 + f_x^2)f_{yy} = 0$.
5. The coordinate functions $x^1, x^2, x^3 : M \to \mathbb{R}$ are harmonic with respect to the induced metric, $\Delta_g x^i = 0$ — equivalently, the embedding $\mathbf{x} : M \to \mathbb{R}^3$ is a **harmonic map** from $(M, g)$ to $\mathbb{R}^3$.

**Consequences:**
- **Saddle-shaped at every point.** From $\kappa_1 = -\kappa_2$, the Gauss curvature is $K = -\kappa_1^2 \leq 0$, with equality only at flat points. So $M$ is locally saddle-like everywhere (or flat).
- **No closed embedded minimal surface in $\mathbb{R}^3$.** A closed bounded surface in $\mathbb{R}^3$ has a point of maximal distance from any chosen interior point, and at that maximum, the surface is locally convex relative to the chosen interior — forcing $K > 0$ at that point, contradicting $K \leq 0$. So embedded minimal surfaces in $\mathbb{R}^3$ are always non-compact or have boundary.

---

# Categorical / Structural Definition

Structurally, a minimal surface is a **critical point of the area functional** on the space of immersions $M \to \mathbb{R}^3$ with fixed boundary. The area functional is
$$
A : \mathrm{Imm}(M, \mathbb{R}^3) \to \mathbb{R}, \qquad A(\mathbf{x}) = \int_M\sqrt{\det g_{\alpha\beta}}\, du\, dv,
$$
where $g_{\alpha\beta} = \langle\partial_\alpha\mathbf{x}, \partial_\beta\mathbf{x}\rangle$ is the induced metric of the immersion $\mathbf{x}$. The first variation $\delta A$ at a critical point vanishes for all variations vanishing on $\partial M$, and the Euler–Lagrange equations are precisely $H = 0$.

From the perspective of **calculus of variations**, the area functional is *non-quadratic* and *not convex* — solutions of the Euler–Lagrange equation may be saddle points (unstable critical points), not minima. The **second variation** of area
$$
\delta^2 A(v) = -\int_M v\cdot(\Delta_g v + |\mathrm{II}|^2 v)\, dA \quad\text{(for normal variations of magnitude }v\text{)}
$$
involves the **Jacobi operator** $J = \Delta_g + |\mathrm{II}|^2$, which is a Schrödinger-type operator on $M$. A minimal surface is **stable** iff $J \geq 0$ as an operator (no negative eigenvalues with eigenfunctions vanishing on $\partial M$), and **unstable** otherwise. The catenoid is stable for short distances between bounding circles, unstable for long.

From a **PDE-theoretic** perspective, the minimal-surface equation is a **quasilinear elliptic** PDE of second order — uniformly elliptic when the gradient $\nabla f$ is bounded, degenerate as $|\nabla f| \to \infty$. Bernstein's theorem says: a *complete* minimal graph $z = f(x, y)$ over all of $\mathbb{R}^2$ must be a plane (the only entire solutions are linear). This is in stark contrast to the linear case (the Laplace equation has many entire solutions) and is the prototype of a **Liouville-type rigidity theorem** in geometric analysis.

---

# Relate to Other Fields / Compression

Minimal surfaces are the **codimension-$1$ case** of **minimal submanifolds** of any codimension in any Riemannian manifold: $M^k \subset N^n$ is minimal iff the mean curvature vector $\vec H = \mathrm{tr}_g\mathrm{II} \in \nu M$ vanishes. The same first-variation argument identifies $-\vec H$ as the $L^2$-gradient of the volume functional.

In **complex analysis** (the theory of Riemann surfaces), every minimal surface in $\mathbb{R}^3$ has a **Weierstrass–Enneper representation**: it can be parametrised by holomorphic data on a Riemann surface — a meromorphic function $g$ (the **Gauss map** of the minimal surface, valued in $\mathbb{CP}^1$) and a holomorphic $1$-form $\eta$. So the study of minimal surfaces in $\mathbb{R}^3$ is essentially the study of pairs $(g, \eta)$ on a Riemann surface, bridging differential geometry and complex analysis intimately.

In **soap film physics**, the empirical Plateau laws state: (i) soap films are smooth $H = 0$ surfaces; (ii) three smooth surfaces meet along curves at $120°$ angles; (iii) four such curves meet at points at the **tetrahedral angle** $\arccos(-1/3) \approx 109.47°$. The mathematical theory of singularity formation in minimal-surface clusters (proved by Taylor) is one of the centrepieces of geometric measure theory.

In **general relativity**, the analogue of a minimal surface is a **marginally outer-trapped surface** (MOTS) or, in the time-symmetric case, exactly a minimal surface in the spatial slice — these surfaces are the apparent horizons of black holes and are central to the Penrose singularity theorem and the modern study of black hole geometry.

In **string theory**, the worldsheet of a free string is a $2$-dimensional surface in spacetime, and its dynamics is governed by minimising the (Polyakov or Nambu–Goto) area functional — so minimal surfaces appear directly in fundamental physics.

**True name:** A minimal surface is *a critical point of area, with mean curvature zero*. The official "$H \equiv 0$" is the right algebraic definition; the operational picture is "a soap film stretched between wires, balancing surface tension". Both definitions characterise the same objects, and the bridge between them — the first variation formula — is the chapter's central variational identity.

---

# Examples / Corollaries

**Is an instance — the plane.** $H = 0$ trivially (in fact, $\kappa_1 = \kappa_2 = 0$). The plane is the simplest minimal surface.

**Is an instance — the catenoid.** Parametrise as $\mathbf{x}(u, v) = (a\cosh(v/a)\cos u, a\cosh(v/a)\sin u, v)$ for $u \in [0, 2\pi)$, $v \in \mathbb{R}$, $a > 0$. Direct computation gives $\kappa_1 = -1/(a\cosh^2(v/a))$, $\kappa_2 = 1/(a\cosh^2(v/a))$, so $H = 0$ and $K = -1/(a\cosh(v/a))^4 < 0$. The catenoid is the only nonplanar minimal **surface of revolution** in $\mathbb{R}^3$ (Euler, 1744). See [[Ex - The Catenoid is a Minimal Surface]].

**Is an instance — the helicoid.** Parametrise as $\mathbf{x}(u, v) = (v\cos u, v\sin u, au)$ for $u \in \mathbb{R}$, $v \in \mathbb{R}$. Computation yields $H = 0$ everywhere. The helicoid is the only nonplanar **ruled minimal surface** (Catalan, 1842). See [[Ex - The Helicoid is Minimal]]. The catenoid and helicoid are locally isometric — related by a one-parameter family of minimal surfaces (the **Bonnet deformation**).

**Is an instance — Enneper's surface.** Parametrise as $\mathbf{x}(u, v) = (u - u^3/3 + uv^2, v - v^3/3 + vu^2, u^2 - v^2)$. Mean curvature is zero everywhere. Enneper's surface is the prototype of a **non-embedded minimal surface** in $\mathbb{R}^3$ (it self-intersects). It has a particularly simple Weierstrass–Enneper representation $g(z) = z$, $\eta = dz$.

**Is an instance — Scherk's first surface.** $z = \log(\cos y/\cos x)$ — a doubly periodic minimal surface, defined on the chessboard-pattern domain where the argument of the logarithm is positive. The first known nontrivial minimal surface other than catenoid and helicoid (Scherk, 1834).

**Is NOT an instance — the sphere.** $\kappa_1 = \kappa_2 = \pm 1/a$, so $H = \pm 2/a \neq 0$. The sphere is not minimal — it has constant non-zero mean curvature (it is a **soap bubble**, not a soap film).

**Is NOT an instance — any compact embedded surface without boundary in $\mathbb{R}^3$.** As noted in the consequences, no such surface can be minimal. The closest analogues are minimal surfaces in $S^3$ (where, e.g., the Clifford torus is minimal) — but these live in the round sphere, not in Euclidean space.

**Corollary — a minimal surface satisfies $\Delta_g \mathbf{x} = 0$.** The Laplace–Beltrami operator of the induced metric applied to each coordinate function $x^i : M \to \mathbb{R}$ gives $\Delta_g x^i = -2H N^i$, so $H = 0$ iff each $x^i$ is harmonic on $M$. Equivalently, the embedding $\mathbf{x} : M \to \mathbb{R}^3$ is a **harmonic map**. This is one of the most useful characterisations: any harmonic-map technique (maximum principle, removable singularities, energy minimisation) applies to minimal surfaces.

**Corollary — Bernstein's theorem (1915).** Any minimal graph $z = f(x, y)$ defined on all of $\mathbb{R}^2$ must be a plane (i.e., $f$ linear). The proof uses an a priori gradient estimate and is the prototype of a **rigidity theorem** in geometric PDE. In dimensions $\geq 8$, the analogous statement (for minimal hypergraphs over $\mathbb{R}^n$) fails — there are nontrivial entire minimal hypergraphs, like Simons' cone (1968). Dimension $7$ is the threshold.

**Corollary — Laplace's pressure formula for soap films.** For a soap film $M$ in equilibrium, the pressure difference across the film is $\Delta p = -2\sigma H$, where $\sigma$ is the surface tension. A film spanning a wire frame has $\Delta p = 0$ (atmospheric pressure on both sides), forcing $H = 0$ — a minimal surface. A bubble (closed surface) has constant $H \neq 0$ inside, with $H = -p/2\sigma$ in equilibrium — the bubble is a **constant mean curvature** (CMC) surface, with a sphere as the simplest example.

**Calibration check.** If you have understood the definition, you should be able to: (i) verify directly that the helicoid $(v\cos u, v\sin u, au)$ has $H = 0$ at the origin (where $u = v = 0$): one computes $E = a^2 + v^2$, $F = 0$, $G = 1$, $e = 0$, $f = -a/\sqrt{a^2 + v^2}$, $g_{\mathrm{II}} = 0$, so $H = (eG - 2fF + gE)/(EG - F^2) = 0$; (ii) check that the catenoid is the only nonplanar minimal surface of revolution — set up the surface of revolution as $\mathbf{x}(u, v) = (r(v)\cos u, r(v)\sin u, z(v))$, derive the meridian ODE from $H = 0$, and integrate to find the catenary $r = a\cosh((z - z_0)/a)$; (iii) confirm that a minimal surface has $K = -\kappa_1^2 \leq 0$ everywhere, with $K = 0$ exactly at flat points where $\kappa_1 = \kappa_2 = 0$.

---

# Unlocked by This

> [!tip] The Plateau Problem *(from Geometric Analysis)*
> The **Plateau problem** asks: given a Jordan curve $C \subset \mathbb{R}^3$, does there exist a minimal surface with boundary $C$? **Solution** (Douglas, Radó, 1931): yes, always, via direct minimisation of the Dirichlet integral on a parametrising disc. **Existence is the easy part; smoothness and embeddedness are subtle.** Generalisations: minimal surfaces of higher genus (Federer–Fleming via geometric measure theory), minimal hypersurfaces in higher dimensions (Almgren), free-boundary problems (water-droplet shapes).

> [!tip] The Weierstrass–Enneper Representation *(from Complex Analysis / Minimal Surfaces)*
> Every minimal surface in $\mathbb{R}^3$ admits a Weierstrass–Enneper parametrisation: there is a Riemann surface $\Sigma$, a meromorphic function $g : \Sigma \to \mathbb{CP}^1$ (the **Gauss map** of the minimal surface, in $\mathbb{CP}^1 = S^2$), and a holomorphic $1$-form $\eta$ such that the surface is the real part of $\int(1 - g^2, i(1 + g^2), 2g)\eta$. This converts the study of minimal surfaces into the study of pairs $(g, \eta)$ on Riemann surfaces, a complex-analytic problem.

> [!tip] Bernstein's Theorem and Higher-Dimensional Cones *(from Geometric Measure Theory)*
> **Bernstein's theorem** (1915): any complete minimal graph on $\mathbb{R}^2$ is a plane. Generalisations: the theorem holds for $\mathbb{R}^n$ with $n \leq 7$ (Almgren, Simons), fails for $n \geq 8$ (Simons' cone is a singular minimiser). This dimensional threshold is one of the most surprising results in geometric analysis and is the entry to the **regularity theory** for area-minimising hypersurfaces.

> [!tip] Mean Curvature Flow *(from Geometric Analysis)*
> The parabolic flow $\partial_t \mathbf{x} = HN$ (or $\partial_t \mathbf{x} = -HN$ depending on sign convention) is **mean curvature flow** — the gradient flow of area. It contracts surfaces, develops singularities (necks, points), and has been a major tool in geometric topology (Huisken's proof of the Riemannian Penrose inequality, Hamilton–Perelman's program for the Poincaré conjecture using **Ricci flow** as a higher-dimensional analogue).

> [!tip] The Willmore Conjecture *(from Conformal Geometry)*
> The **Willmore conjecture** (proved by Marques–Neves, 2014) says that for any immersed torus $T^2 \to \mathbb{R}^3$, $\int_M H^2/4\, dA \geq 2\pi^2$, with equality only for the Clifford torus (the standard torus in $\mathbb{R}^3$ obtained from the round torus in $S^3$ by stereographic projection). This is a **conformal-geometry** rigidity theorem and one of the deepest in $21$st-century geometric analysis.
