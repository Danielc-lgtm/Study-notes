---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Electric Four-Current"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Problem Statement

A continuous medium of charged matter has proper charge density $\rho_0$ (charge per unit volume in its own rest frame) and moves with four-velocity field $U$. Its four-current is $J = \rho_0 U$.

1. Show that an observer of four-velocity $U_0$ measures charge density $\rho = U_0\cdot J = \gamma\rho_0$, where $\gamma = U_0\cdot U$ is the Lorentz factor between observer and matter, and explain physically why the density is *enhanced* by $\gamma$.
2. Show that the observer measures current density $\mathbf J = \rho_0\gamma\mathbf v = \rho\mathbf v$, where $\mathbf v$ is the matter's velocity relative to the observer, recovering the elementary relation between current and moving charge.
3. Verify that $\nabla\cdot J = 0$ (charge conservation) is equivalent to $\partial_t\rho + \nabla\cdot\mathbf J = 0$ together with conservation of the proper charge of each matter element.
4. Compare with the dust four-momentum $P = mU$ and explain the structural analogy between charge and rest mass.

**Recall:**

![[Def - The Electric Four-Current#The Definition]]

The Lorentz factor between an observer of four-velocity $U_0$ and matter of four-velocity $U$ is $\gamma = U_0\cdot U$ (timelike inner product, $\geq 1$ in our signature). The matter's velocity relative to the observer enters through the decomposition $U = \gamma(U_0 + \mathbf v)$ with $\mathbf v\perp U_0$ and $|\mathbf v| < 1$. The dust [[Def - Four-Momentum and Rest Mass|four-momentum]] is $P = mU$ with $m$ the rest mass.

---

# Convergent Strategy

**Problem class.** A *project-a-four-vector-onto-an-observer* problem combined with a *recognise-the-structural-analogy* problem. The [[Special Relativity XXII — Maxwell's Equations#Problem-Solving Strategy|topic strategy]] says: write the source in its cleanest covariant form $J = \rho_0 U$, then project onto the observer to read off $\rho$ and $\mathbf J$.

**Assumption pattern.** The given is $J = \rho_0 U$ — the four-current of a continuous medium, the proper charge density times the four-velocity. The signpost is "proper": $\rho_0$ is a scalar, defined in the rest frame, the only frame-independent density available. What this unlocks is that everything an observer measures follows by contracting and projecting this single object.

**Theorem routing.** The route is: $J = \rho_0 U \to$ contract with $U_0$ for $\rho = U_0\cdot J = \rho_0(U_0\cdot U) = \gamma\rho_0$; project orthogonally for $\mathbf J = \rho_0\gamma\mathbf v$. The structural analogy routes through comparing $J = \rho_0 U$ with the dust [[Def - Four-Momentum and Rest Mass|four-momentum]] $P = mU$, with charge density and rest mass playing identical roles. Conservation $\nabla\cdot J = 0$ unpacks via the continuity equation.

**Key decision point.** The crux is recognising that $\rho_0$, not $\rho$, is the fundamental scalar — the proper charge density measured in the rest frame — and that the observer's density $\rho = \gamma\rho_0$ is *enhanced*, not reduced, because the rest-frame volume length-contracts and packs the charge denser. Confusing which density carries the $\gamma$ (and in which direction) is the standard error; the rest-frame quantity is the bare scalar.

---

# Legal Operations Used

1. **Operation 7 from the topic page (project onto an observer).** Parts 1 and 2 contract $J = \rho_0 U$ with the observer's four-velocity (for $\rho$) and project orthogonally (for $\mathbf J$).

2. **Operation 9 from the topic page (restore $c$ to recover the textbook form).** Part 2 recovers the elementary $\mathbf J = \rho\mathbf v$, the familiar current of moving charge.

3. **Operation 2 from the topic page (apply $d$ and use $d^2 = 0$).** Part 3 connects $\nabla\cdot J = 0$ to the continuity equation and to conservation of proper charge along the flow.

---

# Hints

> [!note]- Hint 1
> The observer's charge density is the time-component of $J$ in the observer's frame, which is the invariant contraction $\rho = U_0\cdot J$. Substitute $J = \rho_0 U$: $\rho = \rho_0(U_0\cdot U) = \rho_0\gamma$. For the physical reason, think about what happens to a box of charge when you boost: its volume *contracts* along the motion, so the same charge occupies less space.

> [!note]- Hint 2
> The current density is the spatial part of $J$, obtained by projecting out the time component: $\mathbf J = J - (U_0\cdot J)U_0 = \rho_0 U - \rho U_0$. Use $U = \gamma(U_0 + \mathbf v)$ to find $\mathbf J = \rho_0\gamma\mathbf v$, and note $\rho_0\gamma = \rho$, so $\mathbf J = \rho\mathbf v$.

> [!note]- Hint 3
> $\nabla\cdot J = \nabla\cdot(\rho_0 U) = U\cdot\nabla\rho_0 + \rho_0\nabla\cdot U$. The first term is the change in proper charge density following the flow; the second involves the expansion of the flow. Project onto an observer to see the continuity equation, and interpret the vanishing as conservation of each element's proper charge.

> [!note]- Hint 4
> Lay $J = \rho_0 U$ and $P = mU$ side by side. Both are a scalar invariant of the matter (proper charge density / rest mass) times the four-velocity. Both have a conservation law ($\nabla\cdot J = 0$ / $\nabla\cdot P = 0$ for free dust). What plays the role of "amount of stuff" in each?

---

# Solution

The four-current of a medium is $\rho_0 U$, and everything an observer measures follows by projecting it. Step 1 contracts with the observer's four-velocity for the density; Step 2 projects orthogonally for the current; Step 3 unpacks conservation; Step 4 draws the analogy with four-momentum. The non-obvious point is in Step 1: the observed density is *enhanced* by $\gamma$ because the rest-frame volume contracts.

**Step 1: The observed density is $\rho = \gamma\rho_0$.**

> [!note]- Derivation
> The charge density measured by the observer is the invariant contraction of the four-current with the observer's four-velocity (the time-component of $J$ in the observer's frame):
> $$\rho = U_0\cdot J = U_0\cdot(\rho_0 U) = \rho_0\,(U_0\cdot U) = \rho_0\gamma,$$
> using $\gamma = U_0\cdot U$ for the Lorentz factor between observer and matter. So $\rho = \gamma\rho_0 \geq \rho_0$.
>
> **Physical reason for the enhancement.** Consider a small element of charge $dq$ occupying rest-frame volume $dV_0 = $ (length)$\times$(area), so $\rho_0 = dq/dV_0$. To the observer, the element moves at speed $|\mathbf v|$, and its extent along the motion is **length-contracted** by $1/\gamma$: $dV = dV_0/\gamma$. The charge $dq$ is invariant (a Lorentz scalar), so the observed density is $\rho = dq/dV = \gamma\,dq/dV_0 = \gamma\rho_0$. The density goes *up*, not down — the same charge is squeezed into a contracted volume. This is the charge analogue of relativistic mass-density increase.

**Step 2: The observed current is $\mathbf J = \rho\mathbf v$.**

> [!note]- Derivation
> The current density is the spatial part of $J$ in the observer's rest space, obtained by subtracting the time-component:
> $$\mathbf J = J - (U_0\cdot J)U_0 = \rho_0 U - \rho U_0.$$
> Substitute $U = \gamma(U_0 + \mathbf v)$ (the decomposition of the matter's four-velocity relative to the observer, with $\mathbf v\perp U_0$):
> $$\mathbf J = \rho_0\gamma(U_0 + \mathbf v) - \rho U_0 = \rho_0\gamma U_0 + \rho_0\gamma\mathbf v - \rho U_0.$$
> Since $\rho = \rho_0\gamma$, the $U_0$ terms cancel, leaving
> $$\mathbf J = \rho_0\gamma\mathbf v = \rho\mathbf v.$$
> This is the elementary relation between current density and moving charge: the current is the charge density times its velocity. Charge moving at $\mathbf v$ carries current $\rho\mathbf v$, exactly as in non-relativistic electromagnetism — but now $\rho$ is the relativistically-enhanced density.

**Step 3: Conservation is the continuity equation plus proper-charge conservation.**

> [!note]- Derivation
> Expand the divergence of $J = \rho_0 U$:
> $$\nabla\cdot J = \nabla_\mu(\rho_0 U^\mu) = U^\mu\nabla_\mu\rho_0 + \rho_0\nabla_\mu U^\mu = \frac{d\rho_0}{d\tau} + \rho_0\theta,$$
> where $\frac{d\rho_0}{d\tau} = U^\mu\nabla_\mu\rho_0$ is the rate of change of proper density following a matter element, and $\theta = \nabla_\mu U^\mu$ is the expansion of the flow (the fractional rate of volume increase). Setting $\nabla\cdot J = 0$ gives $\frac{d\rho_0}{d\tau} = -\rho_0\theta$: the proper density decreases exactly as fast as the volume expands, so the proper charge $dq = \rho_0\,dV_0$ of each element is conserved.
>
> Projected onto an observer, $\nabla_\mu J^\mu = \partial_t\rho + \nabla\cdot\mathbf J = 0$ — the continuity equation (using Step 1, 2). The two statements are equivalent: covariant charge conservation $\nabla\cdot J = 0$ *is* the continuity equation, and it expresses that the charge carried by each matter element never changes, only flows.

**Step 4: Charge density is to the four-current as rest mass is to the four-momentum.**

> [!note]- Derivation
> Compare:
> $$J = \rho_0 U \qquad\text{(four-current)}, \qquad P = mU \qquad\text{(dust four-momentum)}.$$
> Both are a *scalar invariant of the matter* — the proper charge density $\rho_0$, the rest mass $m$ — multiplied by the four-velocity $U$. The four-velocity transports the invariant through spacetime; the scalar is the "amount of stuff" (charge per volume / mass). The observer's measurements mirror each other: $\rho = \gamma\rho_0$ (density enhanced by $\gamma$) parallels the energy density of dust scaling as $\gamma^2\rho_0^{\mathrm{mass}}$ (one $\gamma$ from the energy per particle $\gamma m$, one from the contracted volume); the current $\mathbf J = \rho\mathbf v$ parallels the momentum density. The conservation laws match: $\nabla\cdot J = 0$ (charge conserved) and $\nabla\cdot P = 0$ (force-free dust, momentum conserved). Charge and rest mass play identical structural roles, which is why the same projection techniques apply to both — and why the four-current is the "charge version" of the momentum of dust.

> [!note]- Complete formal solution
> For a medium with four-current $J = \rho_0 U$: the observer's charge density is $\rho = U_0\cdot J = \rho_0(U_0\cdot U) = \gamma\rho_0$, enhanced by $\gamma$ because the invariant charge $dq$ occupies a length-contracted volume $dV = dV_0/\gamma$. The current density is $\mathbf J = J - \rho U_0 = \rho_0 U - \rho U_0 = \rho_0\gamma\mathbf v = \rho\mathbf v$ (using $U = \gamma(U_0 + \mathbf v)$ and $\rho = \rho_0\gamma$), the elementary current of moving charge. Conservation $\nabla\cdot J = \frac{d\rho_0}{d\tau} + \rho_0\theta = 0$ says each element's proper charge $\rho_0\,dV_0$ is conserved, and projects to the continuity equation $\partial_t\rho + \nabla\cdot\mathbf J = 0$. Structurally $J = \rho_0 U$ is the exact charge analogue of the dust four-momentum $P = mU$, with proper charge density replacing rest mass. $\blacksquare$

---

# Key Takeaways

**The cleanest source is the proper scalar times the four-velocity, and everything observed is a projection of it.** The reusable principle, applying to charge, mass, baryon number, and any conserved "stuff", is to write the source as (proper density)$\times$(four-velocity) — a single covariant object built from the frame-independent rest-frame density and the flow — and then obtain every observer's measurement by projection: contract with the observer's four-velocity for the density, project orthogonally for the current. The trigger is "a continuous distribution of conserved stuff in motion"; the move is $J = \rho_0 U$, then project. This converts every three-dimensional measurement into a one-line contraction and makes the relativistic transformation of densities and currents automatic. Whenever you meet a current or flux of a conserved quantity, reach first for its covariant form $\rho_0 U$.

**Densities are enhanced by $\gamma$ under a boost, because volume contracts while the conserved charge does not.** A frequently-misremembered fact, settled cleanly here, is the *direction* of the relativistic density change: the observed charge density $\rho = \gamma\rho_0$ goes *up*, not down. The reason is that the conserved quantity (charge) is a Lorentz scalar, invariant, while the volume containing it is length-contracted by $1/\gamma$; dividing a fixed charge by a smaller volume gives a larger density. The diagnostic to keep straight: anything that is "amount per volume" gets multiplied by $\gamma$ under a boost (because volume shrinks), while anything that is "amount per time" or a total amount behaves differently. The same logic gives the relativistic increase of energy density (with $\gamma^2$, because both the per-particle energy and the volume scale) and is the microscopic origin of the magnetic force between current-carrying wires, where the relativistic length-contraction of moving charge produces an unbalanced charge density.

**Charge and rest mass are structurally identical: both are the scalar "amount" carried by the four-velocity.** The deep takeaway is the exact parallel between $J = \rho_0 U$ and $P = mU$ — charge density and rest mass play the same role, each a Lorentz-invariant measure of "how much matter is here" that the four-velocity transports through spacetime, each obeying a conservation law of the form $\nabla\cdot(\text{scalar}\times U) = 0$. This analogy is not a loose metaphor: it is why the energy–momentum tensor of dust, $T = \rho_0^{\mathrm{mass}}U\otimes U$, is the "two-index version" of the four-current, and why the same projection and conservation techniques apply across electromagnetism, hydrodynamics, and the energy–momentum tensor of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy|topic XXIII]]. Recognising a quantity as "scalar invariant carried by $U$" immediately tells you how it transforms, how it is conserved, and how to project it onto any observer.
