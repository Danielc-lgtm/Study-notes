---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Sectional Curvature"
  - "Def - Riemann Curvature Tensor"
tags: [geometry, riemannian-geometry, curvature]
---

# Notation

$(M, g)$ is a Riemannian manifold of dimension $n \ge 2$. We write $K(\sigma)$ for the [[Def - Sectional Curvature|sectional curvature]] of a $2$-plane $\sigma \subset T_pM$. The Riemann tensor is $R$.

---

# Axiom Motivation

We want to name the simplest possible Riemannian manifolds: those whose curvature is "the same in every direction." There are two natural candidate notions, and we need to disentangle them.

The first is **pointwise constancy**: at each point $p$, the sectional curvature $K(\sigma)$ is the same for every $2$-plane $\sigma \subset T_pM$. This is the condition "no preferred plane at $p$."

The second is **global constancy**: $K(\sigma) = K_0$ for the same constant $K_0$ at every point and every plane.

In dimension $\ge 3$, **Schur's lemma** says these are equivalent: if $K(\sigma)$ depends only on $p$ and not on $\sigma$, then it does not depend on $p$ either. The proof uses the second Bianchi identity. Under the pointwise hypothesis, the Riemann tensor has the form

$$R(X, Y)Z = f(p)(\langle Y, Z\rangle X - \langle X, Z\rangle Y)$$

with $f$ a function on $M$. The second Bianchi identity applied to this expression forces $\nabla f = 0$, hence $f$ is constant.

In dimension $2$, this is vacuous: there is only one $2$-plane at each point, so pointwise constancy is automatic and global constancy is just "constant Gauss curvature" — a genuinely meaningful constraint that distinguishes the sphere from a non-round surface.

The desiderata for "constant sectional curvature $K_0$" are: (i) the three model spaces $S^n$, $\mathbb{R}^n$, $H^n$ should each be the prototypical example for $K_0 = 1, 0, -1$ respectively; (ii) the condition should be expressible as a simple algebraic constraint on $R$; (iii) every complete simply-connected constant-curvature manifold should be isometric to one of the rescaled models. All three are met by the definition $K \equiv K_0$, and the third (the **Killing–Hopf theorem**) is one of the foundational rigidity results in Riemannian geometry.

Why the specific algebraic form $R(X, Y)Z = K_0(\langle Y, Z\rangle X - \langle X, Z\rangle Y)$? It is the unique Riemann-tensor algebra consistent with sectional curvature equal to $K_0$ on every plane. To see this: by the symmetries of $R$, the value $\langle R(X, Y)Y, X\rangle$ on an orthonormal pair $X, Y$ determines $R$ entirely (this is [[Thm - Sectional Curvature Determines the Riemann Tensor|the polarisation identity]]). If this value is $K_0(\langle X, X\rangle\langle Y, Y\rangle - \langle X, Y\rangle^2) = K_0$ on every orthonormal pair, then $R$ is forced to be the displayed form. So "constant sectional curvature" pins down $R$ up to the choice of $K_0$.

What if we strengthened the definition to "constant Ricci tensor proportional to $g$"? That is the **Einstein condition**, and it is strictly weaker in dimension $\ge 4$: $\mathbb{CP}^n$ is Einstein but not constant-sectional. What if we weakened to "constant scalar curvature"? Much weaker: any compact $M$ admits a constant-scalar-curvature metric in its conformal class (the resolved Yamabe problem), but only very special $M$ admit constant-sectional-curvature metrics.

---

# The Definition

> **Definition (Constant sectional curvature).** A Riemannian manifold $(M, g)$ has **constant sectional curvature** $K_0$ if $K(\sigma) = K_0$ for every $2$-plane $\sigma \subset T_pM$ at every point $p \in M$.
>
> Equivalently, the Riemann tensor has the algebraic form
>
> $$R(X, Y)Z = K_0\bigl(\langle Y, Z\rangle X - \langle X, Z\rangle Y\bigr) \qquad X, Y, Z \in T_pM, \forall p.$$
>
> In dimension $n \ge 3$, by **Schur's lemma**, the pointwise condition "$K(\sigma)$ depends only on $p$, not on $\sigma$" automatically implies the constant condition.

The three signs $K_0 > 0, K_0 = 0, K_0 < 0$ correspond to the three families of **space forms**: spherical, flat, and hyperbolic.

---

# Categorical / Structural Definition

A Riemannian manifold of constant sectional curvature $K_0$ is characterised by having **maximal isometry group**: the isometry group $\mathrm{Iso}(M, g)$ has dimension $n(n+1)/2$, the maximum possible for an $n$-manifold. (This dimension is achieved exactly by the model spaces and their quotients.) The isometry-group action is **transitive** (the manifold is homogeneous) and the stabiliser at any point is the full orthogonal group $\mathrm{O}(n)$ (the manifold is **isotropic** — no preferred direction at any point). The three model spaces realise this maximal symmetry:

- $S^n = \mathrm{O}(n+1)/\mathrm{O}(n)$, isometry group $\mathrm{O}(n+1)$ of dimension $n(n+1)/2$.
- $\mathbb{R}^n = E(n)/\mathrm{O}(n)$ where $E(n)$ is the Euclidean group, of dimension $n(n+1)/2$.
- $H^n = \mathrm{O}(1, n)/\mathrm{O}(n)$ (using the hyperboloid model), isometry group $\mathrm{O}(1, n)$ of dimension $n(n+1)/2$.

These are the three **isotropic homogeneous spaces** in the Riemannian category — the maximally symmetric Riemannian manifolds.

---

# Relate to Other Fields / Compression

In **classical geometry**, constant-sectional-curvature surfaces are the subject of **non-Euclidean geometry**: the sphere (elliptic/spherical), the plane (Euclidean), and the hyperbolic plane (Bolyai–Lobachevsky geometry). The historical motivation for hyperbolic geometry — finding a surface where the parallel postulate fails — found its rigorous formulation in the upper-half-plane and Poincaré-disc models, both of which are constant-curvature-$(-1)$ surfaces.

In **homogeneous space theory**, the three model spaces are the **simply-connected complete Riemannian symmetric spaces of constant curvature**. Their quotients by free, properly-discontinuous group actions give all the **space forms** — closed manifolds of constant curvature. The spherical space forms (quotients of $S^n$) include $\mathbb{RP}^n$, lens spaces, and so on; the Euclidean space forms include $T^n$, the Klein bottle, etc.; the hyperbolic space forms are the **hyperbolic manifolds**, central in **Thurston's geometrization** of $3$-manifolds.

In **physics**, $\mathbb{R}^n$ is the prototypical inertial reference space; the round $S^n$ is the spatial slice of a closed positively-curved cosmology (the **closed FLRW universe**); $H^n$ is the spatial slice of a negatively-curved cosmology. The de Sitter and anti-de Sitter spacetimes of GR are Lorentzian analogues.

**True name:** *A manifold of constant sectional curvature $K_0$ is one whose Riemann tensor reduces to the simplest possible algebraic shape $R(X, Y)Z = K_0(\langle Y, Z\rangle X - \langle X, Z\rangle Y)$ — equivalently, one whose isometry group acts transitively and isotropically.* The geometric picture is "looks the same at every point and in every direction"; the algebraic picture is "Riemann tensor is a polynomial in $g$ alone."

---

# Examples / Corollaries

**Example 1 (the three simply-connected models).** $(S^n_r, g_{\mathrm{round}})$, the sphere of radius $r$ in $\mathbb{R}^{n+1}$, has constant sectional curvature $K_0 = 1/r^2$. $(\mathbb{R}^n, g_{\mathrm{flat}})$ has $K_0 = 0$. $(H^n_r, g_{\mathrm{hyp}})$, hyperbolic $n$-space of "radius" $r$, has $K_0 = -1/r^2$. By the **Killing–Hopf theorem**, every complete simply-connected Riemannian $n$-manifold of constant sectional curvature is isometric to one of these (for the appropriate $r$).

**Example 2 (space forms).** Real projective space $\mathbb{RP}^n = S^n/\{\pm 1\}$ inherits the round metric, has constant sectional curvature $1$, and is the simplest spherical space form. The flat torus $T^n = \mathbb{R}^n/\mathbb{Z}^n$ has $K \equiv 0$ and is the simplest Euclidean space form. Compact hyperbolic surfaces (genus $\ge 2$) have $K \equiv -1$ — by the **uniformisation theorem** every closed surface of genus $\ge 2$ admits a hyperbolic metric.

**Example 3 (Killing–Hopf rigidity).** Any closed orientable surface of constant Gauss curvature $K_0 > 0$ is $S^2$ ($\chi = 2$, so $\int K\, dV = 4\pi > 0$ forces $\chi > 0$, only $S^2$ qualifies). Of constant $K_0 = 0$: $T^2$ or the Klein bottle. Of constant $K_0 < 0$: any surface of genus $\ge 2$. The space-forms classification gives a complete topological list in each curvature sign.

**Non-example.** $\mathbb{CP}^n$ has sectional curvature pinched in $[1/4, 1]$ — not constant. The varying curvature is essential to its complex geometry: the maximum $K = 1$ is achieved on complex lines, the minimum $K = 1/4$ on totally real planes, with $K = 1$ exactly for $J$-invariant $2$-planes.

**Non-example.** $S^2 \times S^2$ has $\mathrm{Ric} = g$ (Einstein) but $K = 0$ on mixed $2$-planes — not of constant sectional curvature. This shows the strict containment "constant sectional curvature ⊊ Einstein" in dimension $\ge 4$.

**Calibration check.** If you have understood the definition correctly you should be able to: (a) verify that the algebraic form $R(X, Y)Z = K_0(\langle Y, Z\rangle X - \langle X, Z\rangle Y)$ gives $K(\sigma) = K_0$ for every $\sigma$; (b) recall the three model spaces with their dimensions of isometry groups; (c) state Schur's lemma in the form "$K$ pointwise constant + $n \ge 3$ $\implies$ $K$ globally constant"; (d) recognise that every $2$-manifold is "pointwise of constant sectional curvature" trivially.

---

# Unlocked by This

> [!tip] Killing–Hopf Theorem *(from Riemannian Geometry)*
> Every complete simply-connected Riemannian $n$-manifold of constant sectional curvature is isometric to a model space $S^n_r$, $\mathbb{R}^n$, or $H^n_r$. Combined with covering-space theory, this gives the **space-form classification**: every closed manifold of constant sectional curvature is a quotient of a model space by a free, properly-discontinuous isometric group action. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]].

> [!tip] Uniformization Theorem *(from Complex Analysis)*
> Every simply-connected Riemann surface is biholomorphic to one of $\mathbb{CP}^1 = S^2$, $\mathbb{C}$, or the unit disc $\Delta$. Equipped with the standard metrics (round, Euclidean, Poincaré), these realise constant Gauss curvature $+1$, $0$, $-1$ respectively. Every closed orientable surface admits a metric of constant Gauss curvature; the sign is determined by the Euler characteristic by Gauss–Bonnet.

> [!tip] Thurston Geometrization *(from $3$-manifold topology)*
> **Thurston's geometrization conjecture** (proved by **Perelman** via Ricci flow with surgery, $2003$) says every closed $3$-manifold can be canonically decomposed into pieces, each carrying one of **eight model geometries**. Three of these are the constant-sectional-curvature geometries $S^3$, $\mathbb{R}^3$, $H^3$; the other five involve mixed-curvature symmetric spaces. This generalises the genus-and-curvature classification of surfaces to dimension $3$.
