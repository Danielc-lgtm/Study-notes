---
type: theorem
subject: special-relativity
prereqs:
  - "Thm - Maxwell Equations"
  - "Def - The Electric Four-Current"
  - "Thm - Stokes Theorem on Spacetime"
  - "Thm - Properties of the Exterior Derivative"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. The [[Def - The Electric Four-Current|four-current]] is $J$, with metric-dual $1$-form $\underline J$ and Hodge-dual $3$-form $\star J$; $\nabla\cdot J = \nabla_\mu J^\mu$ is its divergence. The field is $F$, $\star$ the [[Def - The Hodge Star|Hodge star]], $d$ the [[Special Relativity XIX/Def - The Exterior Derivative|exterior derivative]]. Relative to an observer of four-velocity $U_0$, the current gives charge density $\rho = U_0\cdot J$ and current density $\mathbf J$. A spatial domain in the observer's rest space is $\mathcal V$, with boundary $2$-surface $\mathcal S = \partial\mathcal V$; $Q = \int_{\mathcal V}\rho\,dV$ is the enclosed charge. A closed hypersurface is $\Sigma$, a four-dimensional domain $\mathcal U$ with $\partial\mathcal U = \Sigma$. Full registry on [[Special Relativity XXII — Maxwell's Equations]].

---

# Statement

> **Theorem (electric charge conservation).** The electric four-current is divergence-free,
> $$d{\star}J = 0, \qquad \text{equivalently}\qquad \nabla\cdot J = \nabla_\mu J^\mu = 0,$$
> as a consequence of [[Thm - Maxwell Equations|Maxwell's equations]] and the nilpotence $d^2 = 0$ of the exterior derivative — not as an independent postulate. Relative to an observer it is the **continuity equation**
> $$\frac{\partial\rho}{\partial t} + \nabla\cdot\mathbf J = 0.$$

> **Corollary (conservation of total charge).** For any closed hypersurface $\Sigma = \partial\mathcal U$, the flux of $J$ through $\Sigma$ vanishes,
> $$\Phi_\Sigma(J) = \int_\Sigma \star J = 0.$$
> Consequently, if $\mathcal U$ is a spacetime "tube" capped by two spatial slices $\mathcal V$, $\mathcal V'$ (at times $t$, $t'$) with no charge crossing its side wall, the enclosed charges are equal: $Q' = Q$. Charge is neither created nor destroyed, and is the same for every inertial observer.

> **Corollary (Gauss theorem).** For a closed $2$-surface $\mathcal S = \partial\mathcal V$ bounding a spatial domain $\mathcal V$ containing charge $Q$, the flux of the electric field equals the enclosed charge over $\varepsilon_0$:
> $$\oint_{\mathcal S}\mathbf E\cdot d\mathbf S = \frac{Q}{\varepsilon_0}, \qquad \text{equivalently}\qquad \int_{\mathcal S}\star F = \frac{Q}{\varepsilon_0}.$$

---

# Motivation

Electric charge is one of the most precisely conserved quantities in physics — no experiment has ever seen a net charge created or destroyed. In pre-relativistic electromagnetism this conservation is imposed as a separate empirical law, the continuity equation $\partial_t\rho + \nabla\cdot\mathbf J = 0$, on the same footing as Maxwell's four equations. This theorem makes a stronger and more elegant claim: charge conservation is **not** an independent law. It is a forced consequence of Maxwell's equations together with the bare algebraic fact $d^2 = 0$. There is nothing to postulate; once you accept that the field obeys $d{\star}F = \mu_0{\star}J$, charge conservation follows by applying $d$ once more.

This is a striking instance of a general principle: the structure of a field theory's equations *forces* its conservation laws. The mechanism is the nilpotence of the exterior derivative. The inhomogeneous Maxwell equation says the source $3$-form $\star J$ equals (up to $\mu_0$) the exterior derivative $d{\star}F$ of something; applying $d$ to both sides annihilates the right by $d^2 = 0$, leaving $d{\star}J = 0$ — the source is itself closed, which is exactly conservation. The same pattern, with the same logic, forces energy–momentum conservation in general relativity from the Einstein equations and current conservation in every gauge theory. Charge conservation is the simplest member of this family.

The integral corollaries turn the local statement into the global facts of electromagnetism. Integrating $d{\star}J = 0$ over a closed hypersurface, by Stokes' theorem, shows the total charge flux through any closed surface vanishes — so charge on a later time-slice equals charge on an earlier one, and charge is conserved in time. The same Stokes argument applied to the inhomogeneous equation gives Gauss's law: the electric flux out of a closed surface measures the charge inside. These are the integral laws every physics student learns first; here they appear as boundary-equals-bulk consequences of the exterior calculus.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "the field obeys the inhomogeneous Maxwell equation $d{\star}F = \mu_0{\star}J$".

The first disguised source is **"the field has a potential and the inhomogeneous equation holds"**. Whenever $F = dA$ with $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$, charge conservation follows by applying $\nabla_\nu$ and using the antisymmetry of $F^{\mu\nu}$ (the index version of $d^2 = 0$). The bridge is that $\nabla_\nu\nabla_\mu F^{\mu\nu} = 0$ because a symmetric operator contracts an antisymmetric tensor to zero. The nonobviousness is that conservation is a property of the *equation's structure*, not of the particular source. *Example problem:* show that any $J$ appearing as the source in a consistent Maxwell system is automatically divergence-free.

The second disguised source is **"a source term sits on the right of an exact-form equation"**. The pattern $d\omega = (\text{source})$ for any form $\omega$ forces $d(\text{source}) = 0$. So whenever a quantity is the exterior derivative of something, that quantity is conserved. The bridge is $d^2 = 0$ alone, independent of electromagnetism. *Example problem:* in a generic field theory $d{\star}F = {\star}J$, conclude $\nabla\cdot J = 0$ without using any property of $F$ beyond the equation.

The third disguised source is **"the four-current is given as $\rho_0 U$ with a conserved-flow assumption"**. If $J = \rho_0 U$ and the matter flow conserves particle number, then $\nabla\cdot J = 0$ directly, and Maxwell's consistency is automatically satisfied. The bridge is the [[Def - The Electric Four-Current|four-current form]] $J = \rho_0 U$ and the continuity of the flow. *Example problem:* verify that a fluid of charged particles with conserved number gives a divergence-free four-current.

**Targets (Output Amplification)**

The conclusion is "$\nabla\cdot J = 0$".

Combine the conclusion with **[[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] over a closed hypersurface**. Since $d{\star}J = 0$, $\oint_\Sigma\star J = \int_{\mathcal U}d{\star}J = 0$ for any $\Sigma = \partial\mathcal U$. The further result is conservation of total charge: capping a tube with two time-slices shows the charge is the same on both. The combination is nonobvious because the *local* statement $\nabla\cdot J = 0$ becomes a *global* invariance through the topology of the bounding surface. *Example:* prove that the charge of an isolated system is constant in time and the same for every observer.

Combine the conclusion with **a choice of observer**. Projecting $\nabla\cdot J = 0$ onto an inertial observer, with $J^\mu = (\rho, \mathbf J)$, gives $\partial_t\rho + \nabla\cdot\mathbf J = 0$, the continuity equation. The further result is the familiar three-dimensional statement that the rate of charge decrease in a region equals the current flowing out. The combination connects the covariant conservation to the everyday continuity equation. *Example:* derive the rate at which charge leaves a region from its current density.

Combine the conclusion with **the inhomogeneous Maxwell equation and Stokes over a $2$-surface**. The same closedness used for conservation, applied to $d{\star}F = \mu_0{\star}J$, gives $\oint_{\mathcal S}\star F = \mu_0\int_{\mathcal V}\star J = \mu_0 Q$, i.e. Gauss's law $\oint\mathbf E\cdot d\mathbf S = Q/\varepsilon_0$. The further result is the integral form of the inhomogeneous equation. The combination shows that conservation and Gauss's law are two faces of the same Stokes argument. *Example:* compute the field of a point charge by Gauss's law on a sphere.

---

# Why Is It True

The bolded mechanism: **applying the exterior derivative to the inhomogeneous Maxwell equation $d{\star}F = \mu_0{\star}J$ annihilates the left side by $d^2 = 0$, leaving $d{\star}J = 0$ — so charge conservation is the shadow, on the source, of the nilpotence of $d$.** There is no physics in this step beyond the form of Maxwell's equations; it is pure calculus.

Take it slowly. The inhomogeneous equation says that the source $3$-form $\mu_0\star J$ is the exterior derivative of the $2$-form $\star F$: $\mu_0\star J = d({\star}F)$. Now, the exterior derivative of *anything* of the form $d(\text{something})$ is zero — that is what $d^2 = 0$ means. So $d(\mu_0{\star}J) = d(d{\star}F) = 0$, which is $d{\star}J = 0$. The source, being an exact form, is automatically closed; and "closed" for the source $3$-form is exactly "conserved" for the current. The four-current cannot be anything other than divergence-free, because it sits in Maxwell's equations as an exact form.

The index version makes the same point with the antisymmetry of $F$. The divergence form is $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$. Apply $\nabla_\nu$: $\nabla_\nu\nabla_\mu F^{\mu\nu} = \mu_0\nabla_\nu J^\nu$. The left side has $\nabla_\nu\nabla_\mu$ symmetric in $\mu, \nu$ (second derivatives commute in flat space) contracted against $F^{\mu\nu}$ antisymmetric in $\mu, \nu$ — and a symmetric object contracted with an antisymmetric one vanishes identically. So $\nabla_\nu J^\nu = 0$. This is $d^2 = 0$ in disguise: the statement "$\nabla_\nu\nabla_\mu$ symmetric kills $F^{\mu\nu}$ antisymmetric" is precisely the component form of the nilpotence of the exterior derivative.

Why does conservation come out of *structure* rather than *dynamics*? Because the inhomogeneous equation does not merely relate the field to the source — it expresses the source as the boundary (in the $d$ sense) of the field. Anything that is a boundary has no boundary of its own ($\partial\partial = \emptyset$, dually $d^2 = 0$), so the source is automatically "boundaryless", i.e. conserved. This is the deep reason conservation laws are so robust in field theory: they are not extra inputs but consequences of writing the dynamics in the form "source = derivative of field". Noether's theorem is the systematic version of this observation — every continuous symmetry yields a current that is conserved for the same structural reason.

The integral statements are then just the geometric content of $d{\star}J = 0$, read through Stokes' theorem: a closed form integrates to zero over a boundary, so the flux through any closed surface vanishes, which is conservation of the enclosed charge. The local nilpotence becomes a global invariance.

---

# What Makes This Hard

The conceptual difficulty is accepting that conservation is *free* — that you do not need to postulate it, that it is forced by the shape of Maxwell's equations; many treatments list the continuity equation as an independent axiom and miss that it is a theorem. The technical subtlety is the sign and degree bookkeeping in $d{\star}J = 0 \Leftrightarrow \nabla\cdot J = 0$: one must track that $\star J$ is a $3$-form, that $d{\star}J$ is a $4$-form proportional to the divergence times the volume form, and the relation $\nabla\cdot\vec j = -\star d\star\underline j$ (a sign from the Lorentzian double-dual). The most common error in the integral corollary is to forget that the orientation of the two time-slices capping a tube is opposite (one boundary is future-pointing, the other past-pointing), which is exactly what turns $\oint\star J = 0$ into $Q' - Q = 0$ rather than $Q' + Q = 0$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Apply $d$ to the inhomogeneous Maxwell equation and invoke $d^2 = 0$ to get $d{\star}J = 0$; translate to $\nabla\cdot J = 0$; integrate over a closed hypersurface with Stokes for conservation; project onto an observer for the continuity equation; and run the same Stokes argument on the inhomogeneous equation for Gauss's law.

**Subgoal decomposition:**

1. **Differentiate the inhomogeneous equation.** Apply $d$ to $d{\star}F = \mu_0{\star}J$.
   - *Hint:* The left becomes $d(d{\star}F) = 0$ by nilpotence.
   - *Why needed:* It produces $d{\star}J = 0$, the closedness of the source.

2. **Translate to the divergence.** Use $\nabla\cdot J = -\star d{\star}\underline J$ (up to sign) to write $d{\star}J = 0$ as $\nabla_\mu J^\mu = 0$.
   - *Hint:* The Hodge dual of a closed $3$-form's exterior derivative is the divergence of the metric-dual vector.
   - *Why needed:* The divergence form is what projects to the continuity equation.

3. **Integrate for total-charge conservation.** Apply [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] to $\star J$ over a closed hypersurface $\Sigma = \partial\mathcal U$.
   - *Hint:* $\oint_\Sigma\star J = \int_{\mathcal U}d{\star}J = 0$; cap a tube with two time-slices of opposite orientation.
   - *Why needed:* It yields $Q' = Q$, conservation in time and invariance across observers.

4. **Project for the continuity equation, and repeat for Gauss.** Set $J^\mu = (\rho, \mathbf J)$ to get $\partial_t\rho + \nabla\cdot\mathbf J = 0$; apply Stokes to $\star F$ over a $2$-surface for $\oint\mathbf E\cdot d\mathbf S = Q/\varepsilon_0$.
   - *Hint:* Gauss's law is $\int_{\mathcal S}\star F = \mu_0\int_{\mathcal V}\star J = \mu_0 Q$.
   - *Why needed:* It recovers the elementary three-dimensional laws.

---

# Lemma Decomposition

> [!note]- Lemma 1: The source is closed
> **Statement:** $d{\star}J = 0$, as a consequence of $d{\star}F = \mu_0{\star}J$ and $d^2 = 0$.
>
> **Hint:** Apply $d$ to both sides of the inhomogeneous Maxwell equation.
>
> **Why needed:** This is the entire conservation law in differential-form language; everything else is translation.
>
> > [!note]- Full proof
> > The inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]] is $d{\star}F = \mu_0{\star}J$. Apply the exterior derivative $d$ to both sides. On the left, $d(d{\star}F) = 0$ by the [[Thm - Properties of the Exterior Derivative|nilpotence]] $d\circ d = 0$. On the right, $d(\mu_0{\star}J) = \mu_0\,d{\star}J$. Hence $\mu_0\,d{\star}J = 0$, and since $\mu_0 \ne 0$, $d{\star}J = 0$. The $3$-form $\star J$ is closed. $\blacksquare$

> [!note]- Lemma 2: Closedness of the source equals vanishing divergence
> **Statement:** $d{\star}J = 0$ is equivalent to $\nabla_\mu J^\mu = 0$.
>
> **Hint:** The divergence of a vector is (up to sign) the Hodge dual of the exterior derivative of the dual $3$-form.
>
> **Why needed:** It connects the form statement to the index statement and the continuity equation.
>
> > [!note]- Full proof
> > For a vector field $\vec j$ with metric-dual $1$-form $\underline j$ and Hodge-dual $3$-form $\star\underline j$, the identity $d{\star}\underline j = (\nabla_\mu j^\mu)\,\epsilon$ holds, where $\epsilon$ is the volume $4$-form (this follows from $\nabla\cdot\vec j\,\epsilon = d(\star\underline j)$, a standard divergence-form identity; see [[Thm - Divergence of a Vector and Tensor Field]]). Therefore $d{\star}J = 0$ if and only if $(\nabla_\mu J^\mu)\,\epsilon = 0$, i.e. $\nabla_\mu J^\mu = 0$. In inertial coordinates this is $\partial_\mu J^\mu = \partial_t\rho + \partial_i J^i = \partial_t\rho + \nabla\cdot\mathbf J = 0$, the continuity equation. $\blacksquare$

> [!note]- Lemma 3: Stokes gives zero net flux through a closed hypersurface
> **Statement:** For any closed hypersurface $\Sigma = \partial\mathcal U$, $\oint_\Sigma\star J = 0$.
>
> **Hint:** Apply [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] to the closed $3$-form $\star J$.
>
> **Why needed:** It is the integral conservation law, from which $Q' = Q$ follows.
>
> > [!note]- Full proof
> > Since $\Sigma$ is closed, it bounds a four-dimensional domain $\mathcal U$, $\Sigma = \partial\mathcal U$. [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] gives $\int_\Sigma\star J = \int_{\mathcal U}d{\star}J$. By Lemma 1, $d{\star}J = 0$, so $\int_\Sigma\star J = 0$. Now take $\mathcal U$ to be a "tube": a four-dimensional region whose boundary $\Sigma$ is the union of an early spatial slice $\mathcal V$ (at time $t$), a late spatial slice $\mathcal V'$ (at time $t'$), and a side wall $\mathcal W$. The slice $\mathcal V$, as a boundary component, carries the opposite (past-directed) orientation to the future-directed normal used in the charge $Q = \int_{\mathcal V}\rho\,dV$ via $\star J$, so its contribution is $-Q$; $\mathcal V'$ contributes $+Q'$. If no charge crosses the side wall, $\int_{\mathcal W}\star J = 0$. Hence $-Q + Q' + 0 = 0$, i.e. $Q' = Q$. $\blacksquare$

> [!note]- Lemma 4: Gauss's law from the inhomogeneous equation
> **Statement:** For a closed $2$-surface $\mathcal S = \partial\mathcal V$, $\int_{\mathcal S}\star F = \mu_0 Q$, equivalently $\oint_{\mathcal S}\mathbf E\cdot d\mathbf S = Q/\varepsilon_0$.
>
> **Hint:** Apply Stokes to $\star F$ over $\mathcal S = \partial\mathcal V$ and use the inhomogeneous Maxwell equation.
>
> **Why needed:** It is the integral form of the dynamical equation, the elementary Gauss's law.
>
> > [!note]- Full proof
> > By [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]], $\int_{\mathcal S}\star F = \int_{\mathcal V}d{\star}F$ for $\mathcal S = \partial\mathcal V$. By the inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]] $d{\star}F = \mu_0{\star}J$, this is $\mu_0\int_{\mathcal V}\star J = \mu_0 Q$, the enclosed charge. For an inertial observer with $\mathcal S$ in the rest space, $\int_{\mathcal S}\star F = \int_{\mathcal S}\mathbf E\cdot d\mathbf S$ (the Hodge dual of $F$ restricted to a spatial $2$-surface is the electric flux; see the decomposition $\star F = -\underline{U_0}\wedge c\underline{\mathbf B} + \star(\underline{U_0}\wedge\underline{\mathbf E})$ from topic XXI, whose only surviving term on a spatial surface is $\mathbf E\cdot d\mathbf S$). Thus $\oint_{\mathcal S}\mathbf E\cdot d\mathbf S = \mu_0 Q = Q/\varepsilon_0$ with $c = 1$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Local conservation.** By Lemma 1, applying $d$ to the inhomogeneous Maxwell equation $d{\star}F = \mu_0{\star}J$ and using $d^2 = 0$ gives $d{\star}J = 0$. By Lemma 2, this is equivalent to $\nabla_\mu J^\mu = 0$, the covariant continuity equation; projecting onto an inertial observer with $J^\mu = (\rho, \mathbf J)$ yields $\partial_t\rho + \nabla\cdot\mathbf J = 0$.
>
> Equivalently, in index form: the divergence form of Maxwell is $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$; applying $\nabla_\nu$ gives $\nabla_\nu\nabla_\mu F^{\mu\nu} = \mu_0\nabla_\nu J^\nu$, and the left side vanishes because $\nabla_\nu\nabla_\mu$ is symmetric in $(\mu,\nu)$ while $F^{\mu\nu}$ is antisymmetric, so $\nabla\cdot J = 0$.
>
> **Global conservation.** By Lemma 3, $\oint_\Sigma\star J = 0$ for any closed hypersurface; capping a tube with two oppositely-oriented spatial slices, with no charge crossing the side wall, gives $Q' = Q$ — the total charge is constant in time. Because the same argument holds for any two slices (including slices of different inertial observers), $Q$ is also independent of the observer: charge is a Lorentz invariant.
>
> **Gauss theorem.** By Lemma 4, the same Stokes argument applied to $\star F$ and the inhomogeneous equation gives $\int_{\mathcal S}\star F = \mu_0 Q$, i.e. $\oint_{\mathcal S}\mathbf E\cdot d\mathbf S = Q/\varepsilon_0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Probability conservation in relativistic quantum mechanics.** The Klein–Gordon and Dirac equations each yield a conserved four-current $j^\mu$ with $\partial_\mu j^\mu = 0$, derived by the same "apply the derivative and use the equation of motion" mechanism; the conserved charge is total probability (or, for charged fields, electric charge). Recognising probability conservation as the same structural theorem is nonobvious because it is usually derived by a Wronskian-style manipulation rather than as a $d^2 = 0$ consequence.

**Energy–momentum conservation in general relativity.** The Einstein equation $G^{\mu\nu} = 8\pi G\,T^{\mu\nu}$ forces $\nabla_\mu T^{\mu\nu} = 0$ because the Einstein tensor $G^{\mu\nu}$ is automatically divergence-free (the contracted Bianchi identity, the gravitational analogue of $d^2 = 0$). This is charge conservation's exact structural twin, one tensor rank higher; the application is out-of-distribution because $\nabla_\mu T^{\mu\nu} = 0$ is the local conservation of energy and momentum, not charge.

**Conservation of topological charge (winding number).** In field theories with nontrivial topology — solitons, vortices, instantons — a topological current $j^\mu = \epsilon^{\mu\nu\rho\sigma}\partial_\nu(\cdots)$ is conserved *identically*, by $\partial_\mu\epsilon^{\mu\nu\rho\sigma}\partial_\nu = 0$, with no equation of motion needed at all. This is the purest form of the same mechanism: the antisymmetry of $\epsilon$ against the symmetry of mixed partials. The application is surprising because the conserved charge is a winding number, an integer counting topological configurations.

---

# Bridges

- **[[Thm - Maxwell Equations]]** — charge conservation is a *corollary* of the inhomogeneous Maxwell equation, obtained by applying $d$ once more and using $d^2 = 0$. It is not independent input; the consistency of Maxwell's equations *requires* $\nabla\cdot J = 0$, so a source that does not conserve charge cannot drive a Maxwell field. This is the structural dependency that makes the displacement current necessary.

- **[[Thm - Stokes Theorem on Spacetime]]** — the integral conservation law and Gauss's law are both [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] applied to a closed form: $\oint\star J = \int d{\star}J = 0$ over a closed hypersurface gives charge conservation, and $\oint\star F = \mu_0 Q$ over a closed surface gives Gauss. The local-to-global passage is entirely the boundary-equals-bulk content of Stokes.

- **[[Def - The Electric Four-Current]]** — the conserved quantity is the charge $Q = \int_{\mathcal V}\star J$, the flux of the four-current through a spatial slice; the theorem says this flux is the same through any two homologous slices, which is exactly why charge is invariant and why the four-current had to be a four-vector in the first place.

- **Noether's theorem** — charge conservation is the Noether current of the global $\mathrm{U}(1)$ phase symmetry of charged matter; the structural fact that "source = $d(\text{field})$ implies source conserved" is the differential-form face of Noether's first theorem. Every continuous symmetry yields a conserved current by this same mechanism; here the symmetry is the constant phase rotation and the current is the electric four-current.

---

# Unlocked by This

> [!tip] The Continuity Equation Across Physics *(from Hydrodynamics and Field Theory)*
> The form $\partial_t\rho + \nabla\cdot\mathbf J = 0$ recurs for every conserved scalar: mass in fluid dynamics, baryon number in [[Special Relativity XXIV — Relativistic Hydrodynamics|relativistic hydrodynamics]], probability in quantum mechanics. The covariant statement $\nabla_\mu J^\mu = 0$ is the universal local conservation law, and its integral form (charge in a region changes only by flux through the boundary) is the operational meaning of conservation.

> [!tip] The Bianchi Identity and Energy–Momentum Conservation *(from General Relativity)*
> The mechanism "field equation + structural identity ⇒ conservation" reappears in gravitation: the contracted Bianchi identity $\nabla_\mu G^{\mu\nu} = 0$ (the curvature analogue of $d^2 = 0$) forces $\nabla_\mu T^{\mu\nu} = 0$ from the Einstein equation, the local conservation of energy and momentum. Charge conservation here is the rank-one prototype of this rank-two gravitational fact; see [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy|topic XXIII]] and [[General Relativity I — Einstein's Equations and Schwarzschild|General Relativity I]].
