---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Maxwell Equations"
  - "Def - The Electromagnetic Field Tensor"
  - "Def - The Electric Four-Current"
tags: [physics, special-relativity]
---

# Problem Statement

Derive all four three-dimensional Maxwell equations by projecting the two covariant equations onto a rigid array of inertial observers of four-velocity $U_0$, and in doing so show that the **displacement current** is the inevitable companion of the spatial current.

1. From the inhomogeneous equation $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$, contract with $U_0$ (the part parallel to the observer's four-velocity) to obtain Gauss's law $\nabla\cdot\mathbf E = \rho/\varepsilon_0$.
2. From the same equation, project onto the rest space (the part orthogonal to $U_0$) to obtain the Ampère–Maxwell law $\nabla\times\mathbf B = \mu_0\mathbf J + \tfrac{1}{c^2}\partial_t\mathbf E$, and identify the displacement current as arising from the time-derivative ($\mu = 0$) part of the divergence.
3. From the homogeneous equation $dF = 0$, recover $\nabla\cdot\mathbf B = 0$ and $\nabla\times\mathbf E = -\partial_t\mathbf B$ (this part may quote the companion exercise on $dF = 0$).
4. Show that the pre-Maxwell Ampère law $\nabla\times\mathbf B = \mu_0\mathbf J$ (without the displacement current) is inconsistent with charge conservation, and that the covariant form forces the correction.

**Recall:**

![[Thm - Maxwell Equations#Statement]]

The field-tensor components relative to the observer are $F^{0i} = -E^i$, $F^{ij} = -\epsilon^{ijk}B_k$ (so $F_{0i} = E_i$, $F_{ij} = -\epsilon_{ijk}B_k$); the [[Def - The Electric Four-Current|four-current]] is $J^\mu = (\rho, \mathbf J)$ in the observer's frame. The constants satisfy $\varepsilon_0\mu_0 = c^{-2} = 1$. The orthogonal projector onto the observer's rest space is $\perp_{U_0} = \mathrm{Id} - U_0\otimes\underline{U_0}$ (in our signature, with $U_0\cdot U_0 = 1$).

---

# Convergent Strategy

**Problem class.** A *translate-the-covariant-equation* problem at full strength, the first target of the [[Special Relativity XXII — Maxwell's Equations#Problem-Solving Strategy|topic strategy]]: project both covariant Maxwell equations onto an observer to recover the four three-dimensional laws, and read off the physical structure (the displacement current) from the index sorting.

**Assumption pattern.** The given is the pair $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ and $dF = 0$. The signpost is "rigid array of inertial observers" — a single global four-velocity $U_0$, so the projection is the same at every point and the partial derivatives commute with the projection. What this unlocks is that contracting with $U_0$ extracts the scalar (Gauss) part and projecting orthogonally extracts the vector (Ampère) part.

**Theorem routing.** The route is: $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu \to \nu = 0$ component (contract with $U_0$) $\to$ Gauss; $\nu = i$ components (project orthogonally) $\to$ Ampère, with the $\mu = 0$ term supplying the displacement current; $dF = 0 \to$ Faraday and no-monopole (Lemmas 3, 4 of [[Thm - Maxwell Equations]]). Part 4 routes through [[Thm - Electric Charge Conservation and the Gauss Theorem|charge conservation]]: taking the divergence of $\nabla\times\mathbf B = \mu_0\mathbf J$ forces $\nabla\cdot\mathbf J = 0$, which fails for accumulating charge.

**Key decision point.** The crux is recognising that the displacement current $\tfrac{1}{c^2}\partial_t\mathbf E$ is not an optional correction but the time-component partner of the spatial current $\mathbf J$ inside $J^\mu = (\rho, \mathbf J)$: it arises from the $\mu = 0$ (time-derivative) term in the divergence $\nabla_\mu F^{\mu i}$. The decision is to track *which* part of the divergence produces *which* term, so that the displacement current's origin is transparent rather than mysterious.

---

# Legal Operations Used

1. **Operation 7 from the topic page (project a tensor equation onto an observer).** The whole exercise is this operation: contract with $U_0$ for the scalar equations, project orthogonally for the vector equations.

2. **Operation 3 from the topic page (convert $d{\star}F$ to the divergence).** The inhomogeneous equation is used in its divergence form $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$, the form that projects cleanly.

3. **Operation 4 (illegal-but-tempting) and the topic's warning on the displacement current.** Part 4 uses the consistency argument: dropping the displacement current violates charge conservation, the repair being the covariant form.

---

# Hints

> [!note]- Hint 1
> For Gauss's law, set $\nu = 0$ in $\nabla_\mu F^{\mu 0} = \mu_0 J^0$. The left side is $\partial_\mu F^{\mu 0} = \partial_i F^{i0}$ (since $F^{00} = 0$); with $F^{i0} = +E^i$ this is $\nabla\cdot\mathbf E$. The right side is $\mu_0\rho = \rho/\varepsilon_0$.

> [!note]- Hint 2
> For Ampère's law, set $\nu = i$ in $\nabla_\mu F^{\mu i} = \mu_0 J^i$. Split the left side into $\mu = 0$ and $\mu = j$ terms: $\partial_0 F^{0i} + \partial_j F^{ji}$. The first term $\partial_t F^{0i} = -\partial_t E^i$ is the displacement current; the second $\partial_j F^{ji}$ is $(\nabla\times\mathbf B)^i$. Rearrange to isolate the curl.

> [!note]- Hint 3
> Parts of part 3 reduce to the companion exercise [[Ex - The homogeneous Maxwell equations from dF equals zero]]: the all-spatial Bianchi component gives $\nabla\cdot\mathbf B = 0$, the one-temporal component gives Faraday's law.

> [!note]- Hint 4
> Take the divergence of $\nabla\times\mathbf B = \mu_0\mathbf J$. The left side is $\nabla\cdot(\nabla\times\mathbf B) = 0$ identically. So this would force $\nabla\cdot\mathbf J = 0$ — but the continuity equation says $\nabla\cdot\mathbf J = -\partial_t\rho$, nonzero when charge accumulates. The fix is the displacement current, which makes the divergence of the full Ampère law consistent with charge conservation.

---

# Solution

Projecting the two covariant equations onto an observer recovers the four three-dimensional laws, and the index sorting reveals the displacement current's origin. Step 1 extracts Gauss from the $\nu = 0$ component; Step 2 extracts Ampère from the spatial components, with the displacement current from the $\mu = 0$ term; Step 3 quotes the homogeneous projection; Step 4 shows the displacement current is forced by charge conservation. The non-obvious move is in Step 2, isolating the time-derivative term as the displacement current.

**Step 1: Gauss's law from the time component.**

> [!note]- Derivation
> Set $\nu = 0$ in the inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]] $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$. In inertial coordinates, $\nabla_\mu = \partial_\mu$, and $F^{00} = 0$ (antisymmetry), so the left side is
> $$\partial_\mu F^{\mu 0} = \partial_i F^{i0} = \partial_i E^i = \nabla\cdot\mathbf E,$$
> using $F^{i0} = +E^i$ (from $F^{0i} = -E^i$ and antisymmetry). The right side is $\mu_0 J^0 = \mu_0\rho$. With $\mu_0 = 1/\varepsilon_0$ (since $c = 1$),
> $$\nabla\cdot\mathbf E = \frac{\rho}{\varepsilon_0}.$$
> This is Gauss's law: the divergence of the electric field is the charge density. It is the part of the inhomogeneous equation parallel to the observer's four-velocity.

**Step 2: Ampère's law, with the displacement current from the $\mu = 0$ term.**

> [!note]- Derivation
> Set $\nu = i$ (spatial) in $\nabla_\mu F^{\mu i} = \mu_0 J^i$. Split the contracted index $\mu$ into its temporal and spatial parts:
> $$\partial_\mu F^{\mu i} = \underbrace{\partial_0 F^{0i}}_{\mu = 0\text{ term}} + \underbrace{\partial_j F^{ji}}_{\mu = j\text{ terms}}.$$
> The $\mu = 0$ term: $\partial_0 F^{0i} = \partial_t(-E^i) = -\partial_t E^i$ — this is the **displacement current**, arising entirely from the *time-derivative* of the electric field, the $\mu = 0$ part of the divergence. The $\mu = j$ terms: $\partial_j F^{ji}$ with $F^{ji} = -\epsilon^{jik}B_k$ gives $-\epsilon^{jik}\partial_j B_k = \epsilon^{ijk}\partial_j B_k = (\nabla\times\mathbf B)^i$. So
> $$-\partial_t E^i + (\nabla\times\mathbf B)^i = \mu_0 J^i.$$
> Rearranging,
> $$\nabla\times\mathbf B = \mu_0\mathbf J + \partial_t\mathbf E,$$
> and restoring $c$ (the time term carries $1/c^2$),
> $$\nabla\times\mathbf B = \mu_0\mathbf J + \frac{1}{c^2}\frac{\partial\mathbf E}{\partial t}.$$
> The displacement current $\tfrac{1}{c^2}\partial_t\mathbf E$ is the time-component partner of the spatial current $\mathbf J$ inside $J^\mu = (\rho, \mathbf J)$ — they enter the single covariant equation together, and the projection separates them into the source $\mathbf J$ and the displacement term.

**Step 3: The homogeneous equation gives no-monopole and Faraday.**

> [!note]- Derivation
> From $dF = 0$, the Bianchi identity $\partial_{[\alpha}F_{\beta\gamma]} = 0$, projected onto the observer (companion exercise [[Ex - The homogeneous Maxwell equations from dF equals zero]]), gives the all-spatial component
> $$\nabla\cdot\mathbf B = 0$$
> and the one-temporal component
> $$\nabla\times\mathbf E = -\frac{\partial\mathbf B}{\partial t}.$$
> These complete the four three-dimensional Maxwell equations. The component count matches: the two covariant equations have $4 + 4 = 8$ independent components, and the four three-dimensional equations have $1 + 3 + 1 + 3 = 8$.

**Step 4: The displacement current is forced by charge conservation.**

> [!note]- Derivation
> Suppose, with Ampère before Maxwell, that $\nabla\times\mathbf B = \mu_0\mathbf J$ (no displacement current). Take the divergence of both sides:
> $$\nabla\cdot(\nabla\times\mathbf B) = \mu_0\nabla\cdot\mathbf J.$$
> The left side is identically zero (the divergence of a curl vanishes). So this would force $\nabla\cdot\mathbf J = 0$. But the [[Thm - Electric Charge Conservation and the Gauss Theorem|continuity equation]] says $\nabla\cdot\mathbf J = -\partial_t\rho$, which is *nonzero* whenever charge accumulates — for instance, the current charging a capacitor flows into a plate where $\partial_t\rho \ne 0$. The pre-Maxwell Ampère law is therefore inconsistent with charge conservation.
>
> The fix is exactly the displacement current. With the full law $\nabla\times\mathbf B = \mu_0\mathbf J + \tfrac{1}{c^2}\partial_t\mathbf E$, taking the divergence gives $0 = \mu_0\nabla\cdot\mathbf J + \tfrac{1}{c^2}\partial_t(\nabla\cdot\mathbf E) = \mu_0\nabla\cdot\mathbf J + \tfrac{1}{c^2}\partial_t(\rho/\varepsilon_0) = \mu_0(\nabla\cdot\mathbf J + \partial_t\rho)$, which is consistent precisely because of charge conservation. In the covariant form there was never any inconsistency: $\nabla\cdot J = 0$ follows automatically from $\nabla_\nu\nabla_\mu F^{\mu\nu} = 0$, and the displacement current is built in as the $\mu = 0$ part of the spatial equation. The displacement current is not a correction Maxwell added by inspiration; it is forced by the structure of the four-dimensional equation.

> [!note]- Complete formal solution
> Project $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ onto the observer. The $\nu = 0$ component is $\partial_i E^i = \mu_0\rho$, i.e. $\nabla\cdot\mathbf E = \rho/\varepsilon_0$ (Gauss). The $\nu = i$ component is $\partial_0 F^{0i} + \partial_j F^{ji} = \mu_0 J^i$, i.e. $-\partial_t E^i + (\nabla\times\mathbf B)^i = \mu_0 J^i$, giving $\nabla\times\mathbf B = \mu_0\mathbf J + \tfrac{1}{c^2}\partial_t\mathbf E$ (Ampère–Maxwell), with the displacement current arising from the $\mu = 0$ (time-derivative) term. The homogeneous $dF = 0$ gives $\nabla\cdot\mathbf B = 0$ and $\nabla\times\mathbf E = -\partial_t\mathbf B$. The displacement current is mandatory: dropping it makes $\nabla\cdot(\nabla\times\mathbf B) = \mu_0\nabla\cdot\mathbf J$ force $\nabla\cdot\mathbf J = 0$, contradicting $\nabla\cdot\mathbf J = -\partial_t\rho$ for accumulating charge; the full law is consistent exactly because of charge conservation, which the covariant form guarantees automatically. $\blacksquare$

---

# Key Takeaways

**Projection onto an observer sorts a covariant equation into a scalar (parallel) part and a vector (orthogonal) part.** The systematic technique, which recovers all of three-dimensional electromagnetism from two four-dimensional equations, is to contract a tensor equation with the observer's four-velocity $U_0$ for the part parallel to time (yielding a scalar equation: Gauss, or no-monopole) and to project orthogonally onto the rest space for the part in space (yielding a vector equation: Ampère, or Faraday). The trigger is "I have a covariant equation and want its laboratory content"; the move is "contract with $U_0$ and project with $\perp_{U_0}$". This is the universal dictionary between the manifestly-covariant and the laboratory descriptions, and it applies equally to the conservation $\nabla_\mu T^{\mu\nu} = 0$ (energy equation parallel, momentum/Euler equation orthogonal) in hydrodynamics and field theory.

**The displacement current is the time-component partner of the spatial current, not an afterthought.** The single most illuminating result of this exercise is that the term $\tfrac{1}{c^2}\partial_t\mathbf E$, which Maxwell famously added to Ampère's law to make electromagnetism consistent and which makes light possible, is *automatic* in the covariant formulation: it is the $\mu = 0$ (time-derivative) part of the divergence $\nabla_\mu F^{\mu i}$, the inevitable companion of the spatial source $\mathbf J$ inside the single four-current $J^\mu = (\rho, \mathbf J)$. There is no Ampère's law without it in four dimensions; the two halves enter together. The reusable insight is that apparent "corrections" in three-dimensional physics often turn out to be unavoidable components of a four-dimensional object — the covariant view removes the appearance of arbitrariness. Whenever a three-dimensional law looks like it needs an ad hoc fix for consistency, suspect that the fix is a component of a covariant equation.

**Charge conservation is the consistency condition that forces the displacement current.** Part 4 exhibits a powerful pattern: a candidate field equation is tested by taking its divergence and checking compatibility with the relevant conservation law. The pre-Maxwell Ampère law fails because $\nabla\cdot(\nabla\times\mathbf B) = 0$ would force $\nabla\cdot\mathbf J = 0$, contradicting charge conservation; the displacement current is exactly the term that restores compatibility. This "divergence test" is a general diagnostic for field equations — in general relativity, the same logic forces the Einstein tensor (rather than the bare Ricci tensor) on the left of the field equation, because only $G^{\mu\nu}$ is divergence-free and hence compatible with $\nabla_\mu T^{\mu\nu} = 0$. The transferable principle: the structure of a relativistic field equation is constrained by the conservation law of its source, and checking the divergence is how you discover the required terms.
