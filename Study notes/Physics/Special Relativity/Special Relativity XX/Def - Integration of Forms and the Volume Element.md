---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Levi-Civita Tensor"
  - "Def - Alternate Forms and the Exterior Product"
  - "Def - Spacetime Orientation"
  - "Def - Tensors on Minkowski Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$. We work in an arbitrary (possibly curvilinear) right-handed coordinate system $(x^\alpha)$ on Minkowski spacetime $\mathscr{E}$, with coordinate basis $(\vec{e}_\alpha)$, $\vec{e}_\alpha = \partial/\partial x^\alpha$. The metric components are $g_{\mu\nu} = \vec{e}_\mu\cdot\vec{e}_\nu$ and $g = \det(g_{\mu\nu})$; in an inertial frame $g_{\mu\nu} = \eta_{\mu\nu}$ and $g = -1$. The **Levi-Civita tensor** $\epsilon$ is the totally antisymmetric 4-form with $\epsilon_{0123} = \sqrt{|g|}$ in a right-handed coordinate basis (see [[Def - The Levi-Civita Tensor]]). The infinitesimal displacement vectors are $\mathrm{d}\vec{\ell}_\alpha = \mathrm{d}x^\alpha\,\vec{e}_\alpha$ (no sum on $\alpha$). A region $\mathscr{V}\subseteq\mathscr{E}$ is a compact four-dimensional domain. Full registry on [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem]].

This is a compound page: it defines three interlocking notions — the **four-volume element** $\mathrm{d}U$, the **four-volume** $\mathrm{vol}\,\mathscr{V}$ of a region, and the **integral of a differential 4-form** $\int_{\mathscr{V}} A$ — because they are introduced together and none is fully usable without the others.

> [!warning] Convention
> Gourgoulhon uses the opposite signature $g = \mathrm{diag}(-1,+1,+1,+1)$ and writes the volume element as $\sqrt{-\det g}\,\mathrm{d}^4x$ with $\det g < 0$. In any four-dimensional Lorentzian metric the determinant is negative in *both* conventions (one positive eigenvalue, three negative, product negative), so $\sqrt{|\det g|} = \sqrt{-\det g}$ denotes the same positive number and the volume element $\sqrt{|g|}\,\mathrm{d}^4x$ requires no sign change between conventions. We write $\sqrt{|g|}$.

---

# Axiom Motivation

We want to integrate over spacetime. The end goal of the chapter is conservation laws, and a conservation law is a statement about *totals* — total charge, total energy — which means we must be able to add up a density over a region and get a number that every observer agrees on. So the first thing to pin down is the measure: what is the four-dimensional analogue of "$\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$", and what makes it observer-independent?

Start in three Euclidean dimensions, where the answer is familiar. The volume of the parallelepiped built on three vectors $\mathrm{d}\vec{\ell}_1, \mathrm{d}\vec{\ell}_2, \mathrm{d}\vec{\ell}_3$ is the scalar triple product $\mathrm{d}\vec{\ell}_1\cdot(\mathrm{d}\vec{\ell}_2\times\mathrm{d}\vec{\ell}_3)$, and for an orthonormal basis this is just $\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3$. The triple product is a totally antisymmetric function of three vectors — it changes sign when you swap two of them and vanishes when two coincide, which is exactly the statement that a degenerate box has zero volume. The desideratum for four dimensions is the same: a totally antisymmetric function of *four* vectors, returning the four-volume of the box they span.

A totally antisymmetric function of four vectors is precisely a **4-form**, and on a four-dimensional space the space of 4-forms is one-dimensional — they are all multiples of a single one. The natural choice, the one fixed by the metric and an orientation, is the **Levi-Civita tensor** $\epsilon$ ([[Def - The Levi-Civita Tensor]]), which plays in four dimensions exactly the role the triple product plays in three. So the four-volume of the elementary box must be $\mathrm{d}U = \epsilon(\mathrm{d}\vec{\ell}_0, \mathrm{d}\vec{\ell}_1, \mathrm{d}\vec{\ell}_2, \mathrm{d}\vec{\ell}_3)$. This is forced: anything else either fails antisymmetry (so a degenerate box has nonzero volume) or is a non-unit multiple of $\epsilon$ (so the orthonormal box does not have unit volume).

Why the factor $\sqrt{|g|}$, and why is it the right one? Evaluate $\mathrm{d}U$ on the coordinate displacements $\mathrm{d}\vec{\ell}_\alpha = \mathrm{d}x^\alpha\,\vec{e}_\alpha$. By multilinearity $\mathrm{d}U = \mathrm{d}x^0\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3\,\epsilon(\vec{e}_0,\vec{e}_1,\vec{e}_2,\vec{e}_3) = \epsilon_{0123}\,\mathrm{d}x^0\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3$, and the component $\epsilon_{0123}$ of the Levi-Civita tensor in a right-handed coordinate basis is $\sqrt{|g|}$. The point of this factor is that it is exactly the Jacobian compensator. Fix the convention $J = \det(\partial x^\mu/\partial x'^\alpha)$. Under the change of coordinates, expressing the old measure in the new coordinates introduces a factor $|J|$, since $\mathrm{d}^4x = |J|\,\mathrm{d}^4x'$, while the metric factor transforms by $\sqrt{|g'|} = |J|\,\sqrt{|g|}$ (because $\det g' = J^2\det g$). These are the two halves of one cancellation: $\sqrt{|g|}\,\mathrm{d}^4x = \sqrt{|g'|}\,\mathrm{d}^4x'$, so the combination is invariant. That is the whole reason $\sqrt{|g|}\,\mathrm{d}^4x$ deserves to be called *the* volume element: it is the unique density that gives the same total for every coordinate system.

Now the subtle and beautiful point, which separates the integral of a *form* from the *volume* of a region. The volume needs the metric, through $\sqrt{|g|}$ — "how big is this region" is a metric question. But the integral of a *4-form* $A$ does not. To integrate $A$ over $\mathscr{V}$, evaluate it on the coordinate box: $\int_{\mathscr{V}} A = \int_{\mathscr{V}} A(\mathrm{d}\vec{\ell}_0,\dots,\mathrm{d}\vec{\ell}_3) = \int_{\mathscr{V}} A_{0123}\,\mathrm{d}^4x$, the plain Lebesgue integral of the single independent component $A_{0123}$. This is coordinate-independent *without* any metric, because the antisymmetric component $A_{0123}$ transforms exactly by the Jacobian — it absorbs the change-of-variables factor on its own. The desideratum "integrate a 4-form invariantly" is met by antisymmetry alone; the metric is needed only for the special 4-form $\epsilon$, whose integral is the volume. If one tried the same with a generic, non-antisymmetric type-$(0,4)$ tensor, the single-component integral would *not* be coordinate-independent — the transformation would carry extra terms the Jacobian cannot absorb. This is the precise sense in which differential forms, and not arbitrary tensors, are the natural objects of integration.

---

# The Definition

Let $(x^\alpha)$ be a right-handed coordinate system on Minkowski spacetime, with coordinate basis $(\vec{e}_\alpha)$ and metric determinant $g = \det(g_{\mu\nu})$.

**The four-volume element.** The **four-volume** of the elementary hyperparallelepiped spanned by the infinitesimal displacement vectors $\mathrm{d}\vec{\ell}_0,\dots,\mathrm{d}\vec{\ell}_3$ is
$$
\mathrm{d}U \;:=\; \epsilon(\mathrm{d}\vec{\ell}_0, \mathrm{d}\vec{\ell}_1, \mathrm{d}\vec{\ell}_2, \mathrm{d}\vec{\ell}_3),
$$
where $\epsilon$ is the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]]. For the coordinate displacements $\mathrm{d}\vec{\ell}_\alpha = \mathrm{d}x^\alpha\,\vec{e}_\alpha$,
$$
\mathrm{d}U \;=\; \sqrt{|g|}\,\,\mathrm{d}x^0\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3 ,
$$
which in inertial coordinates $(x^\alpha) = (t, x, y, z)$ (with $c$ restored, $(ct,x,y,z)$) reduces to $\mathrm{d}U = \mathrm{d}t\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$ (with $c$: $\mathrm{d}U = c\,\mathrm{d}t\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$).

**The four-volume of a region.** For a compact four-dimensional domain $\mathscr{V}\subseteq\mathscr{E}$,
$$
\mathrm{vol}\,\mathscr{V} \;:=\; \int_{\mathscr{V}} \sqrt{|g|}\,\,\mathrm{d}x^0\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3 \;=\; \int_{\mathscr{V}} \epsilon,
$$
the right-hand side being a Lebesgue integral over the coordinate ranges covering $\mathscr{V}$, with $\sqrt{|g|}$ regarded as a function of $(x^0,x^1,x^2,x^3)$. This value is independent of the choice of right-handed coordinates.

**The integral of a differential 4-form.** For any differential 4-form $A$ on $\mathscr{E}$,
$$
\int_{\mathscr{V}} A \;:=\; \int_{\mathscr{V}} A(\mathrm{d}\vec{\ell}_0, \mathrm{d}\vec{\ell}_1, \mathrm{d}\vec{\ell}_2, \mathrm{d}\vec{\ell}_3) \;=\; \int_{\mathscr{V}} A_{0123}\,\,\mathrm{d}x^0\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3 ,
$$
where $A_{0123} = A(\vec{e}_0, \vec{e}_1, \vec{e}_2, \vec{e}_3)$ is the single independent component of $A$ in the coordinates $(x^\alpha)$. This value is independent of the choice of right-handed coordinates and, unlike the four-volume, does not depend on the metric. Writing $A = \alpha\,\epsilon$ for a scalar field $\alpha$ (possible since the space of 4-forms is one-dimensional) gives $\int_{\mathscr{V}} A = \int_{\mathscr{V}}\alpha\,\sqrt{|g|}\,\mathrm{d}^4x$, and the choice $A = \epsilon$ ($\alpha = 1$) recovers $\mathrm{vol}\,\mathscr{V}$.

---

# Categorical / Structural Definition

Integration of $n$-forms is the canonical pairing that makes the top exterior power $\Lambda^n E^*$ into the space of densities on an $n$-dimensional oriented vector space. On an oriented $n$-dimensional vector space $E$, the space $\Lambda^n E^*$ of alternating $n$-forms is one-dimensional, and an orientation is a choice of a connected component of $\Lambda^n E^*\setminus\{0\}$ (the "positive" forms). Evaluating an $n$-form on an ordered basis of $E$ gives a real number — positive for a positively-oriented basis — and integration extends this fibrewise pairing to a global one: $\int_{\mathscr{V}}$ is the unique linear functional on $n$-forms that, on the indicator of a positively-oriented coordinate box, returns the box's coordinate measure weighted by the form's component.

In this language the four-volume element $\epsilon$ is the *metric volume form*: the unique (up to sign) $n$-form taking the value $+1$ on every positively-oriented $g$-orthonormal basis. The metric singles it out from the one-dimensional family $\Lambda^4 E^*$ by the normalisation $\epsilon(e_0,e_1,e_2,e_3) = +1$ for orthonormal right-handed $(e_\alpha)$; the orientation singles out the sign. The integral of a general 4-form is then metric-free precisely because the pairing $\langle A, \mathscr{V}\rangle = \int_{\mathscr{V}} A$ only ever evaluates $A$ on bases and sums — it never measures lengths — whereas $\mathrm{vol}\,\mathscr{V} = \langle\epsilon, \mathscr{V}\rangle$ inherits the metric through $\epsilon$. This is the structural source of the chapter's central dichotomy: forms pair with regions without a metric; the volume form, which carries the metric, is the one form whose pairing returns a size.

---

# Relate to Other Fields / Compression

This is the four-dimensional, Lorentzian instance of the **Riemannian volume form** of differential geometry ([[Def - Riemannian Volume Form]]). On any oriented pseudo-Riemannian $n$-manifold the metric and orientation determine a canonical top-degree form, in coordinates $\sqrt{|g|}\,\mathrm{d}x^1\wedge\dots\wedge\mathrm{d}x^n$, and integration against it gives the invariant volume; the only thing special about the present case is that the metric is the constant $\eta$ and the manifold is flat $\mathbb{R}^4$, so $\sqrt{|g|}$ varies only because the coordinates are curvilinear. The integral of a general $n$-form is the construction studied abstractly in [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]] and [[Differential Geometry VIII — Differential Forms]].

**True name:** the four-volume element is "$\epsilon$ evaluated on the coordinate box", and the integral of a 4-form is "the Lebesgue integral of its one antisymmetric component". The operational content is that integrating a 4-form is *never* harder than an ordinary multivariable Lebesgue integral — you extract the single number $A_{0123}$ and integrate it — and that the metric enters *only* through the special case $A = \epsilon$, where $A_{0123} = \sqrt{|g|}$. Reaching for "$\sqrt{|g|}\,\mathrm{d}^4x$" the instant a scalar is to be integrated over a four-region, and "$\int A_{0123}\,\mathrm{d}^4x$" the instant a 4-form is, is the whole practical skill.

---

# Examples / Corollaries

**Is an instance — a coordinate box in an inertial frame.** Take inertial coordinates $(t,x,y,z)$ and the region $\mathscr{V} = [0,T]\times[0,L]^3$. Here $g_{\mu\nu} = \eta_{\mu\nu}$, $g = -1$, $\sqrt{|g|} = 1$, so $\mathrm{vol}\,\mathscr{V} = \int_{\mathscr{V}}\mathrm{d}t\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z = T L^3$. The four-volume of a "box of spacetime" is just the product of the time interval and the spatial volume.

**Is an instance — spherical coordinates.** In inertial spherical coordinates $(t,r,\theta,\varphi)$ the metric is $g_{\mu\nu} = \mathrm{diag}(1, -1, -r^2, -r^2\sin^2\theta)$, so $g = -r^4\sin^2\theta$ and $\sqrt{|g|} = r^2\sin\theta$. The four-volume element is $\mathrm{d}U = r^2\sin\theta\,\mathrm{d}t\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$, and integrating $1$ over $t\in[0,T]$, $r\in[0,R]$, $\theta\in[0,\pi]$, $\varphi\in[0,2\pi)$ gives $T\cdot\frac{4}{3}\pi R^3$ — the same answer as the inertial computation, as coordinate-independence requires. The factor $r^2\sin\theta$ is exactly the $\sqrt{|g|}$ that compensates the spherical Jacobian.

**Is an instance — the integral of a 4-form recovers a volume.** Let $A = \rho\,\epsilon$ for a scalar field $\rho$. Then $A_{0123} = \rho\,\epsilon_{0123} = \rho\sqrt{|g|}$, and $\int_{\mathscr{V}} A = \int_{\mathscr{V}}\rho\sqrt{|g|}\,\mathrm{d}^4x$ is the integral of the density $\rho$ against the metric volume element. Taking $\rho = 1$ ($A = \epsilon$) returns $\mathrm{vol}\,\mathscr{V}$. This is the mechanism by which "integrate a scalar density over spacetime" is realised as "integrate a 4-form".

**Is NOT an instance — integrating a coordinate differential without $\sqrt{|g|}$.** The expression $\int_{\mathscr{V}}\mathrm{d}t\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$ (no $r^2\sin\theta$) is *not* the four-volume of $\mathscr{V}$ in spherical coordinates: it gives $T\cdot R\cdot\pi\cdot 2\pi$, a coordinate-dependent number with no geometric meaning. The bare product of coordinate differentials is not a geometric measure; only $\sqrt{|g|}\,\mathrm{d}^4x$ is. This is the single most common error in the chapter.

**Is NOT an instance — the integral of a generic tensor's component.** For a non-antisymmetric type-$(0,4)$ tensor $T$, the quantity $\int T_{0123}\,\mathrm{d}^4x$ is not coordinate-independent: under a coordinate change the component $T_{0123}$ transforms with sixteen terms (one per assignment of new indices to the four slots), only the antisymmetric combination of which matches the Jacobian. So this integral depends on the coordinates and is not a geometric quantity. Only when $T$ is *alternating* — a 4-form — do the extra terms organise into the single Jacobian factor, which is the whole reason forms are integrable and generic tensors are not.

**Corollary — the four-volume is coordinate-independent.** Under $(x^\alpha)\mapsto(x'^\alpha)$ with Jacobian $J = \det(\partial x^\beta/\partial x'^\alpha)$, the metric determinant transforms as $\det g' = J^2\det g$, so $\sqrt{|g'|} = |J|\sqrt{|g|}$, while $\mathrm{d}^4x = |J|^{-1}\mathrm{d}^4x'$. The product $\sqrt{|g|}\,\mathrm{d}^4x = \sqrt{|g'|}\,\mathrm{d}^4x'$ is invariant, so $\mathrm{vol}\,\mathscr{V}$ does not depend on the coordinates.

**Calibration check.** If you have understood these definitions you should be able to: (i) compute $\sqrt{|g|}$ for cylindrical inertial coordinates $(t,\rho,\phi,z)$ and confirm the four-volume element is $\rho\,\mathrm{d}t\,\mathrm{d}\rho\,\mathrm{d}\phi\,\mathrm{d}z$; (ii) state in one sentence why $\int_{\mathscr{V}} A$ for a 4-form $A$ needs no metric while $\mathrm{vol}\,\mathscr{V}$ does; and (iii) explain why a degenerate box (two of the $\mathrm{d}\vec{\ell}_\alpha$ parallel) has $\mathrm{d}U = 0$, by appeal to the antisymmetry of $\epsilon$.

---

# Unlocked by This

> [!tip] The Action Principle of Field Theory *(from Classical Field Theory and QFT)*
> The metric four-volume element $\sqrt{|g|}\,\mathrm{d}^4x$ is the measure on which every field theory is built. A field theory is specified by an **action** $S = \int\mathcal{L}\,\sqrt{|g|}\,\mathrm{d}^4x$, where the Lagrangian density $\mathcal{L}$ is a Lorentz scalar built from the fields, and Lorentz invariance of the physics is precisely the statement that $\mathcal{L}$ is a scalar and $\sqrt{|g|}\,\mathrm{d}^4x$ is an invariant measure. Demanding that $S$ be stationary under variations of the fields gives the **Euler–Lagrange field equations** — Maxwell's equations from the electromagnetic action, the Klein–Gordon and Dirac equations from theirs. The identical measure $\sqrt{|g|}\,\mathrm{d}^4x$ appears in the **Einstein–Hilbert action** $\int R\,\sqrt{|g|}\,\mathrm{d}^4x$ of general relativity, whose variation with respect to the metric yields Einstein's equations; there the volume element is dynamical because $g$ is.

> [!tip] The Invariant Integration Measure of a Lie Group *(from Representation Theory)*
> The same logic — a top-degree form, made invariant by a square-root-of-determinant factor — produces the **Haar measure** on a Lie group, the unique (up to scale) translation-invariant volume form, in coordinates $\sqrt{|\det h|}\,\mathrm{d}^n x$ for the group's metric $h$. Integration against the Haar measure is what makes averaging over a group well-defined, and it underlies the orthogonality of characters and the whole representation theory of compact groups — the tool by which the [[Special Relativity IX — The Lorentz Group, Structure and Classification|Lorentz group]]'s representations are organised.
