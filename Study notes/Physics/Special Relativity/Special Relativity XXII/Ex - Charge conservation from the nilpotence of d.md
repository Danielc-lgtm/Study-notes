---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Electric Charge Conservation and the Gauss Theorem"
  - "Thm - Maxwell Equations"
  - "Def - The Electric Four-Current"
tags: [physics, special-relativity]
---

# Problem Statement

Prove that electric charge is conserved as a *consequence* of Maxwell's equations, not as an independent postulate.

1. Starting from the inhomogeneous Maxwell equation $d{\star}F = \mu_0{\star}J$, apply the exterior derivative and use $d^2 = 0$ to derive $d{\star}J = 0$, equivalently $\nabla\cdot J = 0$.
2. Give the same derivation in index form, from $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$, using the antisymmetry of $F^{\mu\nu}$.
3. Project $\nabla\cdot J = 0$ onto an inertial observer to obtain the continuity equation $\partial_t\rho + \nabla\cdot\mathbf J = 0$.
4. Integrate over a spacetime "tube" (a four-dimensional region capped by two spatial slices) using Stokes' theorem to show that the total charge on the two slices is equal, hence conserved in time and invariant across observers.

**Recall:**

![[Thm - Electric Charge Conservation and the Gauss Theorem#Statement]]

The [[Def - The Electric Four-Current|four-current]] $J$ has, relative to an observer of four-velocity $U_0$, the decomposition $J = \rho U_0 + \mathbf J$ with charge density $\rho = U_0\cdot J$ and current density $\mathbf J$ (the spatial part); in the observer's frame $J^\mu = (\rho, \mathbf J)$. The [[Def - The Exterior Derivative|exterior derivative]] is nilpotent, $d\circ d = 0$. [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] states $\int_{\partial\mathcal U}\omega = \int_{\mathcal U}d\omega$ for a form $\omega$ and a domain $\mathcal U$ with boundary $\partial\mathcal U$.

---

# Convergent Strategy

**Problem class.** A *derive-a-conservation-law-from-$d^2 = 0$* problem, the second target in the [[Special Relativity XXII — Maxwell's Equations#Problem-Solving Strategy|topic strategy]]: extract a free identity by applying the exterior derivative to an equation whose right side is a source. The routine is "see a source on the right, apply $d$ on the left".

**Assumption pattern.** The given is the inhomogeneous Maxwell equation $d{\star}F = \mu_0{\star}J$ — a form equation with the current as source. The signpost is that the left side is *itself* an exterior derivative, $d({\star}F)$; this is precisely the structure that $d^2 = 0$ annihilates. What this unlocks is that the source $\star J$ must be closed, which is conservation.

**Theorem routing.** The route is: $d{\star}F = \mu_0{\star}J \to$ apply $d \to d^2{\star}F = 0$ on the left $\to d{\star}J = 0 \to \nabla\cdot J = 0$ (Lemmas 1, 2 of [[Thm - Electric Charge Conservation and the Gauss Theorem]]) $\to$ project to continuity, or integrate via [[Thm - Stokes Theorem on Spacetime|Stokes]] to global conservation. The index version routes through $\nabla_\nu\nabla_\mu F^{\mu\nu} = 0$ by symmetry-antisymmetry.

**Key decision point.** The crux is recognising that the *structure* of the equation forces conservation, with no extra input. The temptation is to look for a separate physical reason charge is conserved; the insight is that there is none needed — applying $d$ to an exact-form equation is purely algebraic, and the conservation is the shadow of $d^2 = 0$. The decision is to *trust the structure* rather than seek additional physics.

---

# Legal Operations Used

1. **Operation 2 from the topic page (apply $d$ and use $d^2 = 0$).** Part 1 is exactly this: $d$ applied to $d{\star}F = \mu_0{\star}J$ kills the left side, leaving $d{\star}J = 0$.

2. **Operation 3 from the topic page (convert $d\star$ to a divergence).** Part 2 uses the index form $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ and the identity relating $d{\star}J = 0$ to $\nabla\cdot J = 0$.

3. **Operation 7 from the topic page (project onto an observer).** Part 3 projects $\nabla\cdot J = 0$ with $J^\mu = (\rho, \mathbf J)$ to get the continuity equation.

---

# Hints

> [!note]- Hint 1
> The left side of the inhomogeneous Maxwell equation is $d({\star}F)$ — already an exterior derivative. What does applying $d$ once more to an exterior derivative give? Use $d\circ d = 0$.

> [!note]- Hint 2
> For the index form: apply $\nabla_\nu$ to $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$. The left side is $\nabla_\nu\nabla_\mu F^{\mu\nu}$. The operator $\nabla_\nu\nabla_\mu$ is symmetric in $\mu, \nu$ (partial derivatives commute in flat space), while $F^{\mu\nu}$ is antisymmetric. What does a symmetric object contracted with an antisymmetric one give?

> [!note]- Hint 3
> For the continuity equation: write $\nabla_\mu J^\mu = 0$ in inertial coordinates as $\partial_0 J^0 + \partial_i J^i$, and use $J^0 = \rho$, $J^i = \mathbf J$. With $x^0 = t$ (and $c = 1$), this is $\partial_t\rho + \nabla\cdot\mathbf J = 0$.

> [!note]- Hint 4
> For global conservation: $\nabla\cdot J = 0$ means $d{\star}J = 0$, so $\star J$ is closed. Apply [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] over a tube whose boundary is two spatial slices plus a side wall. Watch the orientation: the two end-caps carry *opposite* orientations as boundary components, which turns $\oint\star J = 0$ into $Q' - Q = 0$.

---

# Solution

Charge conservation is forced by the shape of Maxwell's equations. Step 1 applies $d$ to the inhomogeneous equation and uses $d^2 = 0$ to get $d{\star}J = 0$; Step 2 gives the index version via the antisymmetry of $F$; Step 3 projects to the continuity equation; Step 4 integrates with Stokes to global conservation. The non-obvious move is in Step 1: the conservation law is purely a consequence of $d^2 = 0$, requiring no physics beyond Maxwell's structure.

**Step 1: Applying $d$ gives $d{\star}J = 0$.**

> [!note]- Derivation
> The inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]] is $d{\star}F = \mu_0{\star}J$. Apply the exterior derivative $d$ to both sides:
> $$d(d{\star}F) = \mu_0\,d{\star}J.$$
> The left side is $d\circ d$ applied to $\star F$, which vanishes by the [[Thm - Properties of the Exterior Derivative|nilpotence]] $d\circ d = 0$. Hence $\mu_0\,d{\star}J = 0$, and since $\mu_0 \ne 0$,
> $$d{\star}J = 0.$$
> The source $3$-form $\star J$ is closed. By the standard divergence-form identity $d{\star}\underline J = (\nabla_\mu J^\mu)\epsilon$, this is equivalent to $\nabla\cdot J = 0$.

**Step 2: The index version uses the antisymmetry of $F^{\mu\nu}$.**

> [!note]- Derivation
> The divergence form of Maxwell is $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$. Apply $\nabla_\nu$:
> $$\nabla_\nu\nabla_\mu F^{\mu\nu} = \mu_0\nabla_\nu J^\nu.$$
> On the left, $\nabla_\nu\nabla_\mu$ is symmetric under $\mu\leftrightarrow\nu$ (second partial derivatives commute in flat space, and there are no curvature terms), while $F^{\mu\nu} = -F^{\nu\mu}$ is antisymmetric. The full contraction of a symmetric tensor with an antisymmetric one vanishes:
> $$\nabla_\nu\nabla_\mu F^{\mu\nu} = \tfrac12(\nabla_\nu\nabla_\mu + \nabla_\mu\nabla_\nu)F^{\mu\nu} = \tfrac12\nabla_\nu\nabla_\mu(F^{\mu\nu} + F^{\nu\mu}) = 0.$$
> Hence $\nabla_\nu J^\nu = 0$. This is the index form of $d^2 = 0$: "symmetric kills antisymmetric" *is* the nilpotence of $d$.

**Step 3: Projecting gives the continuity equation.**

> [!note]- Derivation
> In inertial coordinates adapted to an observer, $\nabla_\mu J^\mu = \partial_\mu J^\mu$ (Christoffel symbols vanish). With $J^\mu = (\rho, \mathbf J)$ and $x^0 = t$ (using $c = 1$):
> $$\partial_\mu J^\mu = \partial_0 J^0 + \partial_i J^i = \frac{\partial\rho}{\partial t} + \nabla\cdot\mathbf J = 0.$$
> This is the **continuity equation**: the rate of decrease of charge density at a point equals the divergence of the current flowing away from it. Charge that disappears from a region must have flowed out across the boundary.

**Step 4: Integration gives global conservation.**

> [!note]- Derivation
> Since $d{\star}J = 0$, the $3$-form $\star J$ is closed. Take a four-dimensional "tube" $\mathcal U$ whose boundary $\partial\mathcal U$ consists of an early spatial slice $\mathcal V$ (at time $t$), a late spatial slice $\mathcal V'$ (at time $t'$), and a side wall $\mathcal W$. By [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]],
> $$\oint_{\partial\mathcal U}\star J = \int_{\mathcal U}d{\star}J = 0.$$
> The boundary integral splits as $\int_{\mathcal V}\star J + \int_{\mathcal V'}\star J + \int_{\mathcal W}\star J$. As a boundary component, the early slice $\mathcal V$ carries the *past-directed* orientation, opposite to the future-directed normal used in the charge $Q = \int_{\mathcal V}\rho\,dV$, so its contribution is $-Q$; the late slice contributes $+Q'$. If no charge crosses the side wall ($\int_{\mathcal W}\star J = 0$), then
> $$-Q + Q' + 0 = 0 \qquad\Longrightarrow\qquad Q' = Q.$$
> The total charge is the same on the two slices — conserved in time. Since the slices may belong to *different* inertial observers, the same argument shows $Q$ is independent of the observer: **charge is a Lorentz invariant.**

> [!note]- Complete formal solution
> Apply $d$ to the inhomogeneous Maxwell equation $d{\star}F = \mu_0{\star}J$: the left side $d(d{\star}F) = 0$ by $d^2 = 0$, so $d{\star}J = 0$, equivalently $\nabla\cdot J = 0$. (In index form: applying $\nabla_\nu$ to $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ gives $\nabla_\nu\nabla_\mu F^{\mu\nu} = 0$ because $\nabla_\nu\nabla_\mu$ is symmetric and $F^{\mu\nu}$ antisymmetric, hence $\nabla\cdot J = 0$.) Projecting onto an observer with $J^\mu = (\rho, \mathbf J)$ gives the continuity equation $\partial_t\rho + \nabla\cdot\mathbf J = 0$. Integrating the closed form $\star J$ over a tube via Stokes, $\oint_{\partial\mathcal U}\star J = \int_{\mathcal U}d{\star}J = 0$; the two oppositely-oriented end-caps and a charge-free side wall give $Q' = Q$, so charge is conserved in time and invariant across observers. Charge conservation is thus a consequence of Maxwell's equations and $d^2 = 0$, not an independent postulate. $\blacksquare$

---

# Key Takeaways

**Conservation laws are forced by the structure "source = derivative of field", through $d^2 = 0$.** The master lesson, transferable to every field theory, is that whenever the dynamics is written as $d(\text{field}) = (\text{source})$, the source is automatically conserved: applying $d$ again kills the left side, so $d(\text{source}) = 0$. Charge conservation needs no separate postulate because the inhomogeneous Maxwell equation already expresses the current as $d{\star}F$, an exterior derivative. The exact same mechanism, one tensor rank higher, forces $\nabla_\mu T^{\mu\nu} = 0$ in general relativity (the Einstein tensor is divergence-free by the contracted Bianchi identity) and current conservation in every gauge theory. The trigger to recognise this everywhere: see an equation of the form $d\omega = (\text{source})$, and immediately conclude the source is closed. Conservation is a free consequence of the equations' shape, never an independent input.

**"Symmetric contracted with antisymmetric vanishes" is the index incarnation of $d^2 = 0$.** The index-form derivation in Step 2 uses a fact worth internalising as its own tool: the full contraction $S^{\mu\nu}A_{\mu\nu}$ of a symmetric tensor $S$ with an antisymmetric tensor $A$ is zero. Here $\nabla_\nu\nabla_\mu$ (symmetric, commuting derivatives) contracted with $F^{\mu\nu}$ (antisymmetric) gives zero, delivering $\nabla\cdot J = 0$. This is not a coincidence — it is precisely how $d^2 = 0$ appears when one works in components rather than forms. The reusable diagnostic: whenever you see a double covariant derivative contracted with an antisymmetric field strength, it vanishes, and that vanishing usually encodes a conservation law or a Bianchi identity. Recognising the symmetric/antisymmetric clash saves the computation.

**Local conservation becomes global invariance through the topology of the bounding surface.** Step 4 shows the passage from the differential statement $\nabla\cdot J = 0$ to the integral statement "total charge is constant" is entirely Stokes' theorem applied to a closed form. The key subtlety, which recurs in every flux-conservation argument, is the orientation of the bounding surfaces: the two time-slices capping a tube carry opposite orientations as boundary components, which is exactly what turns the vanishing total flux $\oint\star J = 0$ into the equality $Q' = Q$ rather than $Q' + Q = 0$. The transferable principle is that a conserved current's charge is a *topological* quantity — it depends only on the homology class of the slice, so any two slices through the same physical region (including slices of different observers) carry the same charge. This is why charge is both conserved in time and Lorentz-invariant, two facts that are really one fact about closed forms.
