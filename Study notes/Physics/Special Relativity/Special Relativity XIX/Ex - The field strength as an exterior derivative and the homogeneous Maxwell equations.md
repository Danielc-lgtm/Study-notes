---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Exterior Derivative"
  - "Thm - Properties of the Exterior Derivative"
  - "Thm - Divergence of a Vector and Tensor Field"
tags: [physics, special-relativity]
---

# Problem Statement

This exercise previews electromagnetism using only the exterior-derivative machinery of this chapter. Let $A$ be a $1$-form on flat spacetime (the **electromagnetic potential**), and define the **field strength** $2$-form $F := \mathbf{d}A$.

1. Write the components $F_{\alpha\beta}$ and confirm $F$ is antisymmetric with six independent components.
2. Show that $F = \mathbf{d}A$ forces the **homogeneous Maxwell equations** $\mathbf{d}F = 0$, equivalently $(\mathbf{d}F)_{\alpha\beta\gamma} = \partial_\alpha F_{\beta\gamma} + \partial_\beta F_{\gamma\alpha} + \partial_\gamma F_{\alpha\beta} = 0$, with no computation beyond nilpotency.
3. Show that the potential is determined only up to a **gauge transformation** $A \to A + \mathbf{d}\chi$, and that this leaves $F$ unchanged.
4. Using the codifferential identity $\boldsymbol{\nabla}\!\cdot\vec{v} = -\star\mathbf{d}\star\underline{v}$, indicate how the **inhomogeneous** Maxwell equation $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ leads, via the determinant divergence formula, to charge conservation $\nabla_\nu J^\nu = 0$.

**Recall:**

![[Def - The Exterior Derivative#The Definition]]

The exterior derivative is nilpotent, $\mathbf{d}^2 = 0$ ([[Thm - Properties of the Exterior Derivative]]). The divergence of an antisymmetric tensor is $\nabla_\mu T^{\alpha\mu} = \frac{1}{\sqrt{-\det g}}\partial_\mu(\sqrt{-\det g}\,T^{\alpha\mu})$ ([[Thm - Divergence of a Vector and Tensor Field]]).

---

# Convergent Strategy

**Problem class.** A *derive-a-physical-law-from-form-structure* problem (operations 7 and 8 from the topic page), showing that the homogeneous Maxwell equations and gauge invariance are pure consequences of $\mathbf{d}^2 = 0$.

**Assumption pattern.** $A$ is a $1$-form and $F = \mathbf{d}A$ is its exterior derivative; the entire content is that $F$ is *exact*, which by nilpotency makes it *closed*. No metric is needed for the homogeneous equations; the metric enters only the inhomogeneous side through the Hodge star.

**Theorem routing.** Part 1 uses the $\mathbf{d}$-of-a-$1$-form formula. Part 2 is $\mathbf{d}^2 = 0$ from [[Thm - Properties of the Exterior Derivative]]. Part 3 uses $\mathbf{d}(\mathbf{d}\chi) = 0$. Part 4 uses the determinant divergence formula from [[Thm - Divergence of a Vector and Tensor Field]] and applies $\nabla_\nu$ to the field equation.

**Key decision point.** The crux of Part 4 is that applying $\nabla_\nu$ to $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ gives $\nabla_\nu\nabla_\mu F^{\mu\nu}$ on the left, which vanishes by the antisymmetry of $F$ against the (effectively symmetric) double derivative — forcing the right side $\mu_0\nabla_\nu J^\nu$ to vanish too. This is the form-theoretic origin of charge conservation as a *consistency condition* of Maxwell's equations.

---

# Legal Operations Used

1. **Use $\mathbf{d}^2 = 0$ to kill an exterior derivative of an exterior derivative** (operation 7 from the topic page) for Parts 2 and 3.
2. **Apply the graded Leibniz rule / recognise exactness** (operations 8, 9 from the topic page).
3. **Compute a divergence by the determinant formula** (operation 5 from the topic page) for Part 4.

---

# Hints

> [!note]- Hint 1
> $F = \mathbf{d}A$ means $F_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha$. This is manifestly antisymmetric, $F_{\alpha\beta} = -F_{\beta\alpha}$, so a $4\times 4$ antisymmetric matrix has $\binom{4}{2} = 6$ independent entries — the three electric and three magnetic field components.

> [!note]- Hint 2
> $\mathbf{d}F = \mathbf{d}(\mathbf{d}A) = \mathbf{d}^2 A = 0$ by nilpotency. No computation needed. In components, $(\mathbf{d}F)_{\alpha\beta\gamma} = \partial_\alpha F_{\beta\gamma} + \partial_\beta F_{\gamma\alpha} + \partial_\gamma F_{\alpha\beta}$, the cyclic "Bianchi" combination, which vanishes when $F = \mathbf{d}A$.

> [!note]- Hint 3
> Under $A \to A' = A + \mathbf{d}\chi$, $F' = \mathbf{d}A' = \mathbf{d}A + \mathbf{d}(\mathbf{d}\chi) = \mathbf{d}A + 0 = F$. The field strength is gauge-invariant precisely because $\mathbf{d}(\mathbf{d}\chi) = 0$.

> [!note]- Hint 4
> Apply $\nabla_\nu$ to $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$. The left side $\nabla_\nu\nabla_\mu F^{\mu\nu}$ vanishes: $F^{\mu\nu}$ is antisymmetric in $\mu\nu$, while the symmetric part of $\nabla_\nu\nabla_\mu$ contracts it to zero (on flat spacetime the derivatives commute, so $\nabla_\nu\nabla_\mu F^{\mu\nu} = \nabla_\mu\nabla_\nu F^{\mu\nu} = -\nabla_\mu\nabla_\nu F^{\nu\mu}$, equal to its own negative). Hence $\mu_0\nabla_\nu J^\nu = 0$.

---

# Solution

The plan: Step 1 writes $F = \mathbf{d}A$ in components. Step 2 gets $\mathbf{d}F = 0$ from nilpotency for free. Step 3 derives gauge invariance from $\mathbf{d}^2\chi = 0$. Step 4 applies the divergence twice to extract charge conservation.

**Step 1: The field strength.**

> [!note]- Derivation
> With $F := \mathbf{d}A$, the components are
> $$F_{\alpha\beta} = (\mathbf{d}A)_{\alpha\beta} = \frac{\partial A_\beta}{\partial x^\alpha} - \frac{\partial A_\alpha}{\partial x^\beta},$$
> manifestly antisymmetric: $F_{\alpha\beta} = -F_{\beta\alpha}$. A $4\times 4$ antisymmetric matrix has $\binom{4}{2} = 6$ independent components, which physically are the three components of the electric field $\mathbf{E}$ (the $F_{0i}$) and the three of the magnetic field $\mathbf{B}$ (the $F_{ij}$). So the single $2$-form $F$ packages the entire electromagnetic field, and it is exact by construction.

**Step 2: The homogeneous Maxwell equations come for free.**

> [!note]- Derivation
> Because $F = \mathbf{d}A$ is an exterior derivative, applying $\mathbf{d}$ again gives zero by nilpotency:
> $$\mathbf{d}F = \mathbf{d}(\mathbf{d}A) = \mathbf{d}^2 A = 0.$$
> No computation is required — this is pure $\mathbf{d}^2 = 0$. In components, the $3$-form equation reads
> $$(\mathbf{d}F)_{\alpha\beta\gamma} = \frac{\partial F_{\beta\gamma}}{\partial x^\alpha} + \frac{\partial F_{\gamma\alpha}}{\partial x^\beta} + \frac{\partial F_{\alpha\beta}}{\partial x^\gamma} = 0,$$
> the cyclic combination of derivatives of $F$. These are the **homogeneous Maxwell equations** — Gauss's law for magnetism $\nabla\cdot\mathbf{B} = 0$ and Faraday's law $\nabla\times\mathbf{E} + \partial_t\mathbf{B} = 0$ — and they hold *automatically*, with no reference to sources, currents, or the metric, the instant the field is written as $F = \mathbf{d}A$. This is the cleanest statement in all of physics: half of Maxwell's equations are the identity $\mathbf{d}^2 = 0$.

**Step 3: Gauge invariance.**

> [!note]- Derivation
> The potential $A$ is not unique. Replace it by $A' = A + \mathbf{d}\chi$ for any scalar field $\chi$ (a **gauge transformation**). The new field strength is
> $$F' = \mathbf{d}A' = \mathbf{d}(A + \mathbf{d}\chi) = \mathbf{d}A + \mathbf{d}(\mathbf{d}\chi) = \mathbf{d}A + 0 = F,$$
> using $\mathbf{d}(\mathbf{d}\chi) = \mathbf{d}^2\chi = 0$. So $F$ is **gauge-invariant**: all potentials differing by an exact form $\mathbf{d}\chi$ give the same physical field. Two facts of electromagnetism — the homogeneous equations and gauge freedom — are thus the *same* algebraic identity $\mathbf{d}^2 = 0$, read as "$\mathbf{d}$ of $F=\mathbf{d}A$ vanishes" and "$\mathbf{d}\chi$ is invisible to $F$" respectively. (The Poincaré lemma supplies the converse: on flat spacetime, any closed $F$, $\mathbf{d}F = 0$, *is* $\mathbf{d}A$ for some $A$, so the potential always exists.)

**Step 4: Charge conservation from the inhomogeneous equation.**

> [!note]- Derivation
> The inhomogeneous Maxwell equation relates the field to the four-current $J$:
> $$\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu,$$
> and the left side, by the antisymmetric-tensor determinant formula, is $\nabla_\mu F^{\mu\nu} = \frac{1}{\sqrt{-\det g}}\partial_\mu(\sqrt{-\det g}\,F^{\mu\nu})$ — computable in any coordinates without Christoffels. Now apply $\nabla_\nu$ to both sides:
> $$\nabla_\nu\nabla_\mu F^{\mu\nu} = \mu_0\nabla_\nu J^\nu.$$
> The left side vanishes. On flat spacetime the covariant derivatives commute (zero curvature), so $\nabla_\nu\nabla_\mu F^{\mu\nu} = \nabla_\mu\nabla_\nu F^{\mu\nu}$; relabelling $\mu\leftrightarrow\nu$ and using the antisymmetry $F^{\mu\nu} = -F^{\nu\mu}$ gives $\nabla_\nu\nabla_\mu F^{\mu\nu} = \nabla_\mu\nabla_\nu F^{\nu\mu} = -\nabla_\mu\nabla_\nu F^{\mu\nu}$, so the quantity equals its own negative and is zero. Therefore
> $$\mu_0\nabla_\nu J^\nu = 0 \quad\Longrightarrow\quad \boldsymbol{\nabla}\!\cdot J = \nabla_\nu J^\nu = 0:$$
> the four-current is divergence-free, which is **electric charge conservation**. It is forced as a *consistency condition* of Maxwell's equations — the inhomogeneous equation cannot even be written down unless the source is conserved. By the determinant formula this conservation law reads $\frac{1}{\sqrt{-\det g}}\partial_\nu(\sqrt{-\det g}\,J^\nu) = 0$ in any coordinates, and (next chapter) the divergence theorem turns it into the integral statement that net charge flux through any closed hypersurface vanishes.

> [!note]- Complete formal solution
> With $F := \mathbf{d}A$, $F_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha$ is antisymmetric with six independent components (the $\mathbf{E}$ and $\mathbf{B}$ fields). The homogeneous equations $\mathbf{d}F = \mathbf{d}\mathbf{d}A = 0$, i.e. $\partial_\alpha F_{\beta\gamma}+\partial_\beta F_{\gamma\alpha}+\partial_\gamma F_{\alpha\beta} = 0$, hold by nilpotency. Under $A\to A+\mathbf{d}\chi$, $F\to \mathbf{d}A + \mathbf{d}\mathbf{d}\chi = F$, so $F$ is gauge-invariant; both facts are $\mathbf{d}^2 = 0$. The inhomogeneous equation $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$, with $\nabla_\mu F^{\mu\nu} = \frac{1}{\sqrt{-\det g}}\partial_\mu(\sqrt{-\det g}F^{\mu\nu})$, gives on applying $\nabla_\nu$: $\nabla_\nu\nabla_\mu F^{\mu\nu} = 0$ (commuting derivatives on flat space against antisymmetric $F$), hence $\nabla_\nu J^\nu = 0$ — charge conservation as a consistency condition. $\blacksquare$

---

# Key Takeaways

**Half of Maxwell's equations and all of gauge invariance are the single identity $\mathbf{d}^2 = 0$.** The most striking lesson of this exercise is how much of electromagnetism is pure exterior-calculus structure, requiring no physics input beyond "the field is the exterior derivative of a potential". Writing $F = \mathbf{d}A$ makes the homogeneous Maxwell equations $\mathbf{d}F = \mathbf{d}^2 A = 0$ automatic — Gauss's law for magnetism and Faraday's law are *identities*, not dynamical laws — and it makes the field invariant under $A \to A + \mathbf{d}\chi$ because $\mathbf{d}^2\chi = 0$ hides the gauge term. So the field strength being closed and the potential being gauge-ambiguous are two readings of the same nilpotency. This is why the form formulation is the *right* language for electromagnetism: it makes manifest, with no computation, exactly the structural features that the vector-calculus formulation presents as separate facts to be verified.

**The metric splits Maxwell's equations into a topological half ($\mathbf{d}F = 0$) and a geometric half ($\mathbf{d}\star F = \mu_0\star J$).** The homogeneous equations $\mathbf{d}F = 0$ use only the exterior derivative and so are metric-free, coordinate-invariant, and automatic; the inhomogeneous equations couple the field to sources through the Hodge star and so depend on the metric. This is the seam, identified in the chapter's insights, between the metric-free topological content of physics and the metric-dependent geometric content. It is also why magnetic monopoles are forbidden in this formulation: $\nabla\cdot\mathbf{B} = 0$ is built into $F = \mathbf{d}A$, and admitting monopoles requires giving up the global existence of the potential (a topological obstruction). The transferable insight is to look, in any field theory, for which equations are "$\mathbf{d}$ of something $= 0$" (automatic, topological) and which involve the metric through $\star$ (dynamical, geometric) — the split organises the whole theory.

**Charge conservation is a consistency condition of Maxwell's equations, forced by antisymmetry and the commuting of derivatives.** The continuity equation $\nabla_\nu J^\nu = 0$ is not an independent postulate but a *necessary consequence* of the inhomogeneous Maxwell equation: applying the divergence to $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ annihilates the left side (antisymmetric $F$ against commuting derivatives), forcing the source to be conserved. This is a recurring and powerful pattern — whenever a field equation has the form "(antisymmetric-derivative of a field) $=$ source", the source is automatically conserved, because the double divergence of an antisymmetric object vanishes. The same mechanism conserves energy–momentum in general relativity (the Einstein tensor's divergence vanishes by the Bianchi identity, forcing $\nabla_\mu T^{\mu\nu} = 0$). Recognising that conservation laws can be *built into* the structure of field equations, rather than imposed separately, is one of the deepest organising principles of physics, and this exercise shows its simplest instance, derived entirely from the exterior-derivative and divergence machinery of the chapter.
