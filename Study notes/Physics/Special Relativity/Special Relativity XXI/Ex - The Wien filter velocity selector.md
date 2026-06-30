---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Motion of a Charge in a Uniform Field"
  - "Thm - Reduction to Parallel Electric and Magnetic Fields"
  - "Def - The Lorentz Four-Force"
tags: [physics, special-relativity, electromagnetism]
---

# Problem Statement

A region contains crossed, uniform fields $\mathbf{E} = E\,e_y$ and $\mathbf{B} = B\,e_z$, with $cB > E$ (so the field is mostly magnetic, $I_1 > 0$). A beam of charged particles enters along $e_x$ with a spread of speeds.

1. Show that a particle moving along $e_x$ with speed $U = E/B$ feels **zero net force** (the electric and magnetic forces cancel) and so passes undeflected, while particles of other speeds are deflected.
2. Show that $U = E/B$ is exactly the boost velocity that transforms the crossed field to a **purely magnetic** field (the [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction]] velocity), and explain why a particle at rest in that frame feels no force.
3. Verify $U = E/B < c$ using the condition $cB > E$, and explain what goes wrong if $cB < E$ (the "mostly electric" case) — why the Wien filter cannot then work.
4. Design a velocity selector to pass particles of speed $U = 0.1\,c$ given a magnetic field $B = 0.5\,$T: what electric field $E$ is required?

**Recall:**

![[Thm - Motion of a Charge in a Uniform Field#Statement]]

The spatial [[Def - The Lorentz Four-Force|Lorentz force]] is $\boldsymbol{\mathfrak{F}} = q(\mathbf{E} + \mathbf{V}\times\mathbf{B})$. The [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction theorem]] says a crossed field with $I_2 = 0$ and $I_1 > 0$ becomes purely magnetic in the frame boosted at $U = E/B$ perpendicular to both fields.

---

# Convergent Strategy

**Problem class.** A *force-balance and reduction* problem from [[Special Relativity XXI — The Electromagnetic Field#Problem-Solving Strategy|§21.3]]: find the velocity at which crossed fields exert no net force, and connect it to the reducing boost. The routine is to balance the electric and magnetic forces, then interpret the result as a change of frame.

**Assumption pattern.** Crossed fields ($\mathbf{E}\perp\mathbf{B}$, so $I_2 = 0$) with $cB > E$ (so $I_1 > 0$, mostly magnetic). The assumption $cB > E$ is exactly what makes the pass-velocity $U = E/B$ subluminal, and what makes the field reducible to purely magnetic. The signpost is "velocity selector": only one speed passes undeflected.

**Theorem routing.** Part 1 routes through the [[Def - The Lorentz Four-Force|Lorentz force]] $q(\mathbf{E}+\mathbf{V}\times\mathbf{B})$ and the force-balance condition. Part 2 routes through the [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction theorem]], identifying $U = E/B$ as the boost to the purely-magnetic frame. Parts 3–4 are the subluminality check and a numerical design.

**Key decision point.** The non-obvious unification is that "the speed at which forces balance" and "the speed of the frame where the field is purely magnetic" are the *same* speed $U = E/B$ — and the second viewpoint *explains* the first: in the purely-magnetic frame a particle at rest feels no force, and a particle at rest in that frame moves at $U = E/B$ in the lab. The temptation is to treat the force balance as an unrelated coincidence; the reduction theorem shows it is the same fact.

---

# Legal Operations Used

1. **Operation 9 (project the four-force onto an observer)** from the topic page: balance the electric and magnetic parts of the Lorentz force. This is part 1.

2. **Operation 5 (reduce to a pure or parallel field)** from the topic page: identify $U = E/B$ as the boost to the purely-magnetic frame. This is part 2.

3. **Operation 7 (use that the magnetic field does no work)** from the topic page: in the purely-magnetic frame a particle at rest feels no force. This is part 2's explanation.

---

# Hints

> [!note]- Hint 1
> The force on a particle moving at $\mathbf{V} = V\,e_x$ is $q(\mathbf{E} + \mathbf{V}\times\mathbf{B}) = q(E\,e_y + V\,e_x\times B\,e_z) = q(E - VB)e_y$ (since $e_x\times e_z = -e_y$). This vanishes when $V = E/B$.

> [!note]- Hint 2
> By the [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction theorem]], boosting at $U = E/B$ along $e_x$ (the $\mathbf{E}\times\mathbf{B}$ direction) makes $\mathbf{E}' = 0$. A particle moving at $U = E/B$ in the lab is *at rest* in that frame; at rest in a purely magnetic field, it feels no force ($q\mathbf{V}'\times\mathbf{B}' = 0$ for $\mathbf{V}'=0$).

> [!note]- Hint 3
> $U = E/B < c \Leftrightarrow E < cB$, which is the assumption $I_1 = c^2B^2 - E^2 > 0$. If $cB < E$ ($I_1 < 0$, mostly electric), then $E/B > c$ — no physical particle reaches that speed, so no particle passes undeflected, and the filter fails. (The field would instead reduce to purely *electric*.)

> [!note]- Hint 4
> $U = E/B \Rightarrow E = UB = (0.1\times3\times10^8)(0.5) = 1.5\times10^7\,$V/m.

---

# Solution

The plan: balance the forces to find the pass-velocity (Step 1), identify it as the reducing boost (Step 2), check subluminality and the failure mode (Step 3), and design numerically (Step 4). The unifying insight is that the force-balance velocity and the purely-magnetic-frame velocity coincide.

**Step 1: The force balance.**

> [!note]- Derivation
> A particle moving with velocity $\mathbf{V} = V\,e_x$ through the crossed fields feels the [[Def - The Lorentz Four-Force|Lorentz force]]
> $$\boldsymbol{\mathfrak{F}} = q(\mathbf{E} + \mathbf{V}\times\mathbf{B}) = q\big(E\,e_y + (V\,e_x)\times(B\,e_z)\big) = q\big(E\,e_y + VB\,(e_x\times e_z)\big) = q(E - VB)\,e_y,$$
> using $e_x\times e_z = -e_y$. The electric force ($qE\,e_y$, upward) and the magnetic force ($-qVB\,e_y$, downward) oppose along $e_y$. They cancel exactly when
> $$E - VB = 0 \quad\Longrightarrow\quad V = \frac{E}{B}.$$
> A particle with speed $U = E/B$ passes straight through, undeflected. Particles faster than $E/B$ feel a net downward force ($E - VB < 0$), particles slower feel a net upward force — both are deflected and miss the exit aperture. Only the speed $U = E/B$ is selected: this is the **Wien filter**, a velocity selector tuned by the ratio $E/B$.

**Step 2: The pass-velocity is the reducing boost.**

> [!note]- Derivation
> By the [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction theorem]], the crossed field (with $I_2 = 0$, $I_1 = c^2B^2 - E^2 > 0$) becomes **purely magnetic** in the frame moving at velocity $U = E/B$ along $\mathbf{E}\times\mathbf{B} \propto e_y\times e_z = e_x$ — exactly the beam direction. In that frame $\mathbf{E}' = 0$ and $\mathbf{B}' = \Gamma^{-1}\mathbf{B}$.
>
> Now reinterpret the force balance. A particle moving at $U = E/B$ in the lab is *at rest* in the purely-magnetic frame. A particle at rest in a purely magnetic field feels no force ($\boldsymbol{\mathfrak{F}}' = q\mathbf{V}'\times\mathbf{B}' = 0$ since $\mathbf{V}' = 0$). The four-force is a frame-independent object: if it vanishes in one frame, it vanishes in all. So the lab-frame force on the $U = E/B$ particle is zero — *the force balance and the field reduction are the same fact*. The Wien velocity $E/B$ is the velocity of the frame in which the field has no electric part, and a particle comoving with that frame sits in a pure magnetic field where, at rest, nothing pushes it.

**Step 3: Subluminality and the failure mode.**

> [!note]- Derivation
> The pass-velocity $U = E/B$ is physical (less than $c$) precisely when
> $$\frac{E}{B} < c \quad\Longleftrightarrow\quad E < cB \quad\Longleftrightarrow\quad I_1 = c^2B^2 - E^2 > 0,$$
> the "mostly magnetic" condition assumed. If instead $cB < E$ ($I_1 < 0$, mostly electric), then $E/B > c$: *no physical particle can reach the pass-velocity*, so no particle passes undeflected, and the Wien filter does not work. In that regime the field reduces not to purely magnetic but to purely *electric* (at $U = c^2B/E < c$), and there is no force-balance speed below $c$ — the electric force dominates for every attainable velocity. So the Wien filter requires a *mostly magnetic* field; the invariant $I_1 > 0$ is the design constraint. (This is exactly Remark 17.20 in the source: a Wien filter works only with a mostly-magnetic field.)

**Step 4: Numerical design.**

> [!note]- Derivation
> To select speed $U = 0.1\,c = 3\times10^7\,$m/s with $B = 0.5\,$T, the required electric field is
> $$E = UB = (3\times10^7\,\text{m/s})(0.5\,\text{T}) = 1.5\times10^7\,\text{V/m}.$$
> Check subluminality: $E/(cB) = (1.5\times10^7)/((3\times10^8)(0.5)) = 0.1 < 1$, so $I_1 > 0$ and the filter is in the valid mostly-magnetic regime. A particle of any charge-to-mass ratio with speed $0.1\,c$ passes undeflected; faster or slower particles are deflected away from the exit aperture. (Combined with a downstream magnetic momentum analysis, $P_\perp = qBR$, this selects a single mass — a velocity-plus-momentum filter is a mass spectrometer.)

> [!note]- Complete formal solution
> The force on a particle of velocity $V\,e_x$ is $q(\mathbf{E}+\mathbf{V}\times\mathbf{B}) = q(E - VB)e_y$, vanishing at $V = U = E/B$ — the pass-velocity, undeflected; other speeds are deflected. By the reduction theorem, $U = E/B$ is the boost (along $\mathbf{E}\times\mathbf{B}\propto e_x$) to the purely-magnetic frame, where a particle at rest feels no force; since the four-force is frame-independent, the lab force vanishes too — the balance and the reduction are one fact. Subluminality $U = E/B < c$ requires $E < cB$, i.e. $I_1 > 0$ (mostly magnetic); if $cB < E$ the pass-velocity exceeds $c$ and the filter fails. To select $U = 0.1c$ with $B = 0.5\,$T, $E = UB = 1.5\times10^7\,$V/m. $\blacksquare$

---

# Key Takeaways

**The Wien velocity $E/B$ is both a force balance and a change of frame.** The exercise's central unification is that the speed at which the electric and magnetic forces cancel ($U = E/B$) is *the same speed* as the frame in which the field is purely magnetic. The second viewpoint explains the first: a particle moving at $E/B$ in the lab is at rest in the purely-magnetic frame, where, being at rest, it feels no force; and because the four-force is frame-independent, it feels no force in the lab either. This is a recurring pattern in relativistic electromagnetism — a dynamical statement (forces balance) is the shadow of a kinematic one (a frame exists where the field simplifies). The reusable move is, when forces mysteriously cancel at a special velocity, to look for the frame in which that velocity is "at rest" and the field is simplest; the cancellation usually becomes obvious there.

**The Wien filter requires a mostly-magnetic field — the invariant $I_1 > 0$ is the design constraint.** The subluminality condition $U = E/B < c$ is exactly $I_1 = c^2B^2 - E^2 > 0$, the mostly-magnetic condition. If the field is mostly electric ($cB < E$), the pass-velocity $E/B$ exceeds $c$, no particle reaches it, and the filter fails — the field would instead reduce to purely electric, with the electric force dominating at every attainable speed. This is the operational meaning of the [[Thm - The Electromagnetic Field Invariants|invariant classification]]: a device that selects a subluminal velocity by force balance can only exist when the field is mostly magnetic. The diagnostic, before building a velocity selector, is to check $cB > E$; the invariant $I_1$ decides whether the design is physically possible. This connects the abstract field classification to a concrete engineering constraint.

**Velocity selection plus momentum analysis equals mass spectrometry.** A Wien filter selects a single *speed* $U = E/B$, independent of the particle's charge and mass. Following it with a magnetic momentum analyzer (which measures $P_\perp = qBR$ from a track radius) determines the *momentum*, and speed-plus-momentum yields the mass: $m = P/(\Gamma U)$. This two-stage scheme is the principle of the mass spectrometer, separating ions by mass-to-charge ratio. The reusable insight is that the crossed-field force balance isolates one kinematic variable (velocity) cleanly, and combining it with a second measurement (momentum, from the cyclotron radius) over-determines the kinematics enough to extract the particle's identity. The Wien filter and the Larmor radius — the two halves of [[Thm - Motion of a Charge in a Uniform Field|charged-particle motion]] — together make a mass analyzer.
