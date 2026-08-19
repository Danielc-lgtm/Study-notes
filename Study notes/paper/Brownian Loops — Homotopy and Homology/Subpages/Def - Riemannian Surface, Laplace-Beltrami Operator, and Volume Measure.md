---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Semi-Riemannian Metric and Signature"
tags: [differential-geometry, riemannian-geometry, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

A **surface** here means a smooth 2-dimensional manifold $X$: a space that looks like a piece of the plane $\mathbb{R}^2$ near every point, glued together smoothly (the sphere, the torus, an infinite cylinder). A **Riemannian metric** $g$ on $X$ is a smooth choice, at each point $x\in X$, of an inner product $g_x(\cdot,\cdot)$ on the tangent plane $T_xX$ (the plane of velocity vectors at $x$); it tells you the length of every tangent vector and the angle between any two. The pair $(X,g)$ is a **Riemannian surface**. In a local coordinate patch with coordinates $(x^1,x^2)$ the metric is a symmetric positive-definite $2\times2$ matrix $g_{ij}(x)$ varying smoothly with $x$, and $g^{ij}$ denotes the inverse matrix. Write $\det g$ for $\det(g_{ij})$. This page assumes the reader knows multivariable calculus (gradient, divergence) and linear algebra (inner products, symmetric matrices); it recalls only the two operations the paper actually uses on $(X,g)$: the **volume measure** and the **Laplace–Beltrami operator**. See [[Def - Smooth Manifold]] and [[Def - Semi-Riemannian Metric and Signature]] for the underlying objects.

---

# Axiom Motivation

The paper runs a random particle on a curved surface and integrates functions of its position, so it needs two things a flat-space calculus takes for granted: a way to *integrate* over the surface, and a *Laplacian* to generate the diffusion. On $\mathbb{R}^2$ these are $\int f\,dx^1dx^2$ and $\Delta f = \partial_1^2 f + \partial_2^2 f$. The problem on a curved surface is that neither the area element $dx^1dx^2$ nor the flat Laplacian is coordinate-independent: change coordinates and both change, so they are not intrinsic to $(X,g)$. The metric $g$ is exactly the extra data needed to build coordinate-free versions.

For the **volume**, the metric measures how much a coordinate square is stretched: an infinitesimal coordinate square $dx^1dx^2$ has true area $\sqrt{\det g}\,dx^1dx^2$, because $\sqrt{\det g}$ is the factor by which the linear map $g^{1/2}$ scales area (the same $\sqrt{\det}$ that appears in the change-of-variables formula). This is forced: it is the *only* density that both restores the flat answer when $g=\mathrm{Id}$ and transforms correctly under change of coordinates.

For the **Laplacian**, the flat $\Delta = \operatorname{div}\operatorname{grad}$ is built from two operations — gradient (turn a function into its steepest-ascent vector field) and divergence (measure the net outflow of a vector field) — and each has a metric version. The gradient must use $g$ to convert the derivative $df$ (a covector) into a vector; the divergence must use the volume $\sqrt{\det g}$ to measure outflow against the correct area. Composing them gives the unique second-order operator that is intrinsic to $(X,g)$, agrees with the flat Laplacian when $g$ is flat, and is symmetric with respect to the volume measure. That symmetry is what later makes $\Delta$ self-adjoint and its heat semigroup a well-defined family of self-adjoint operators — the property the whole paper stands on.

---

# The Definition

> **Definition (Riemannian volume measure).** On a Riemannian surface $(X,g)$, the **volume measure** $\operatorname{vol}_g$ (here an *area* measure, since $\dim X = 2$) is the measure that in any local coordinates $(x^1,x^2)$ is
> $$\operatorname{vol}_g = \sqrt{\det g(x)}\; dx^1\,dx^2,$$
> and is glued together across coordinate patches. For a Borel set $A\subseteq X$ contained in one patch, $\operatorname{vol}_g(A) = \int_A \sqrt{\det g(x)}\,dx^1 dx^2$. On $\mathbb{H}^2$ (the [[Def - Hyperbolic Plane|hyperbolic plane]], metric $g_{ij} = y^{-2}\delta_{ij}$ in coordinates $z=x+iy$) this gives the hyperbolic area $\rho = y^{-2}\,dx\,dy$.

> **Definition (Laplace–Beltrami operator).** The **gradient** of a smooth $f:X\to\mathbb{R}$ is the vector field with components $(\operatorname{grad}_g f)^i = g^{ij}\partial_j f$ (sum over $j$). The **divergence** of a vector field $V=(V^i)$ is $\operatorname{div}_g V = \frac{1}{\sqrt{\det g}}\,\partial_i\!\big(\sqrt{\det g}\,V^i\big)$. The (geometer's, positive) **Laplace–Beltrami operator** is
> $$\Delta_X \;=\; -\operatorname{div}_g \operatorname{grad}_g,\qquad (\Delta_X f) = -\frac{1}{\sqrt{\det g}}\,\partial_i\!\big(\sqrt{\det g}\,g^{ij}\partial_j f\big).$$
> The leading minus sign is the paper's convention: with it, $\Delta_X$ is a *positive* operator (its spectrum lies in $[0,\infty)$), so the heat semigroup $e^{-t\Delta_X}$ is contracting rather than exploding.

**Concrete unpacking.** On flat $\mathbb{R}^2$ with $g=\mathrm{Id}$: $\det g = 1$, so $\operatorname{vol}_g = dx^1dx^2$ is ordinary area, $\operatorname{grad}_g f=(\partial_1 f,\partial_2 f)$ is the ordinary gradient, $\operatorname{div}_g V=\partial_1 V^1+\partial_2 V^2$ is the ordinary divergence, and $\Delta_X f = -(\partial_1^2 f + \partial_2^2 f)$ — the familiar Laplacian, up to the geometer's sign. So every formula reduces to first-year vector calculus when the surface is flat; the metric factors $\sqrt{\det g}$ and $g^{ij}$ are exactly the corrections curvature demands.

**Standard names.** $\Delta_X = -\operatorname{div}_g\operatorname{grad}_g$ is the **Laplace–Beltrami operator** (also called the *Laplace operator on functions*, or the *scalar Laplacian*). The sign here — spectrum in $[0,\infty)$ — is the **geometer's / analyst's positive Laplacian**; physicists often use the opposite sign $\operatorname{div}\operatorname{grad}$ with spectrum in $(-\infty,0]$. The paper states its sign choice explicitly, and so must you.

---

# Examples and Non-Examples

**Is an instance.** The round sphere $S^2$ of radius $1$ has $\Delta_{S^2}$ whose eigenvalues are $k(k+1)$, $k=0,1,2,\dots$ (the spherical harmonics) — all $\ge 0$, consistent with positivity. The flat torus $\mathbb{R}^2/\mathbb{Z}^2$ has eigenvalues $4\pi^2(m^2+n^2)$, $(m,n)\in\mathbb{Z}^2$. In both cases $\operatorname{vol}_g$ is ordinary area.

**Is NOT an instance.** The operator $f\mapsto -(\partial_1^2 f+\partial_2^2 f)$ written in *some fixed coordinate chart* on a curved surface is **not** the Laplace–Beltrami operator: it is not coordinate-independent and not symmetric with respect to $\operatorname{vol}_g$, so it fails to generate a well-defined diffusion on $(X,g)$. The metric corrections $\sqrt{\det g}$ and $g^{ij}$ are exactly what is missing.

**Calibration check.** (1) Verify that on $\mathbb{H}^2$ with $g_{ij}=y^{-2}\delta_{ij}$ one has $\det g = y^{-4}$, hence $\sqrt{\det g}=y^{-2}$ and $\operatorname{vol}_g = y^{-2}dx\,dy$. (2) Check that $\Delta_{\mathbb{H}^2} = -y^2(\partial_x^2+\partial_y^2)$ from the formula (using $g^{ij}=y^2\delta_{ij}$ and $\sqrt{\det g}=y^{-2}$). (3) Confirm that on flat $\mathbb{R}^2$ every formula collapses to the first-year one.

---

# Where the paper uses this

The surface $(X,g)$, its area measure $\operatorname{vol}_g$ (written $\rho$ on $\mathbb{H}^2$, $\rho_X$ on $X$), and the operator $\Delta_X$ are the fixed stage for the entire paper. $\Delta_X$ generates the Brownian motion whose loops are measured; $\operatorname{vol}_g$ is the measure integrated against throughout (e.g. in the loop measure $\int_X \mathbb{W}^t_{x\to x}\,d\operatorname{vol}_g(x)$). The positivity convention fixes the sign of $e^{-t\Delta_X}$. **[[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2]]**.

---

# Verified against

Lee, *Introduction to Riemannian Manifolds* (2nd ed.), §2 (Riemannian metrics, volume form) and the Laplace–Beltrami operator $\Delta = -\operatorname{div}\operatorname{grad}$ in local coordinates; Grigor'yan, *Heat Kernel and Analysis on Manifolds*, §3.1–3.3 for the coordinate formula and the positivity sign convention. Both give $\operatorname{vol}_g=\sqrt{\det g}\,dx$ and $\Delta f = -\frac{1}{\sqrt{\det g}}\partial_i(\sqrt{\det g}\,g^{ij}\partial_j f)$.
