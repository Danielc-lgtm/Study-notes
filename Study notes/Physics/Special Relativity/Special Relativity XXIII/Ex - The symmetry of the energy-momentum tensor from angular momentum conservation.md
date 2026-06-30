---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Energy-Momentum Tensor"
  - "Thm - Energy-Momentum Conservation"
  - "Def - Angular Momentum Four-Tensor"
tags: [physics, special-relativity]
---

# Problem Statement

The energy-momentum tensor of every physical system is symmetric, $T^{\mu\nu} = T^{\nu\mu}$. This is *not* obvious from its definition — nothing in "energy density, momentum density, stress" demands that the energy-flux density equal $c^2$ times the momentum density, or that the stress matrix be symmetric. Prove the symmetry from the **conservation of angular momentum**, and verify there is no circularity. Working with $c = 1$:

1. Define the angular-momentum tensor density of the field about a point $C$ as $J^{\mu\nu\rho} = (x^\mu - x_C^\mu)T^{\nu\rho} - (x^\nu - x_C^\nu)T^{\mu\rho}$ (antisymmetric in $\mu\nu$). Show that its conservation, $\nabla_\rho J^{\mu\nu\rho} = 0$, holds for *all* choices of $C$ if and only if both $\nabla_\rho T^{\nu\rho} = 0$ (energy-momentum conservation) *and* $T^{\mu\nu} = T^{\nu\mu}$ (symmetry).
2. Conclude that, given energy-momentum conservation, the conservation of angular momentum is *equivalent* to the symmetry of $T$.
3. Explain why this derivation has no loophole: it establishes the symmetry of $T$ using only $\nabla_\rho T^{\nu\rho} = 0$, which was proved independently (without assuming symmetry).
4. Interpret physically: why does a non-symmetric $T$ correspond to a medium with an unbalanced internal torque?

**Recall:**

![[Def - The Energy-Momentum Tensor#The Definition]]

The [[Def - Angular Momentum Four-Tensor|angular-momentum tensor]] of a system about a point $C$ is the antisymmetric object built from the "lever arm" $(x - x_C)$ wedged with the momentum; for a continuum its density is $J^{\mu\nu\rho} = (x-x_C)^\mu T^{\nu\rho} - (x-x_C)^\nu T^{\mu\rho}$, and its conservation $\nabla_\rho J^{\mu\nu\rho} = 0$ is the statement that the total angular momentum on a closed hypersurface vanishes for an isolated system. [[Thm - Energy-Momentum Conservation|Energy-momentum conservation]] is $\nabla_\rho T^{\nu\rho} = 0$, proved without reference to the symmetry of $T$.

---

# Convergent Strategy

**Problem class.** A *prove-a-structural-property* problem. The [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy#Problem-Solving Strategy|topic strategy]] for structural properties: differentiate the relevant conserved current and read off what its conservation forces.

**Assumption pattern.** The signpost is "conservation of angular momentum". Angular momentum is the lever arm wedged with momentum, $J = (x-x_C)\wedge T$, so its divergence will produce a derivative of the lever arm (giving a bare $T$) plus a lever-arm-times-divergence-of-$T$ term. The bare $T$ term is where the symmetry condition will surface.

**Theorem routing.** Part 1: compute $\nabla_\rho J^{\mu\nu\rho}$ by the Leibniz rule; the derivative of the lever arm $(x-x_C)^\mu$ gives $\delta^\mu_\rho$, contracting $T^{\nu\rho}$ down to $T^{\nu\mu}$. The leftover lever-arm terms vanish by [[Thm - Energy-Momentum Conservation|energy-momentum conservation]]. What remains is $T^{\nu\mu} - T^{\mu\nu} = 0$. Part 2 is the logical equivalence; Part 3 checks the order of the proofs.

**Key decision point.** The crux is recognising that the derivative $\nabla_\rho(x-x_C)^\mu = \delta^\mu_\rho$ is what converts the rank-three angular-momentum density into the bare rank-two $T$ — this Kronecker delta is the entire mechanism. The non-obvious realisation is that the answer is *independent of $C$* (the $x_C$ terms drop because they are constant), which is why the symmetry must hold pointwise.

---

# Legal Operations Used

1. **Take the divergence and set it to zero** (operation 3 from the topic page): both $\nabla_\rho T^{\nu\rho} = 0$ and $\nabla_\rho J^{\mu\nu\rho} = 0$ are the isolated-system conservation laws.

2. **Leibniz rule on the lever-arm product**: $\nabla_\rho[(x-x_C)^\mu T^{\nu\rho}] = (\nabla_\rho(x-x_C)^\mu)T^{\nu\rho} + (x-x_C)^\mu\nabla_\rho T^{\nu\rho}$, with $\nabla_\rho(x-x_C)^\mu = \delta^\mu_\rho$.

3. **Exploit the independent proof of energy-momentum conservation** ([[Thm - Energy-Momentum Conservation]]): the divergence-free property of $T$ is used as an input, and it was established without assuming symmetry, closing the circularity gap.

---

# Hints

> [!note]- Hint 1
> Apply the Leibniz rule to $\nabla_\rho J^{\mu\nu\rho} = \nabla_\rho[(x-x_C)^\mu T^{\nu\rho} - (x-x_C)^\nu T^{\mu\rho}]$. The key derivative is $\nabla_\rho(x-x_C)^\mu = \partial_\rho x^\mu = \delta^\mu_\rho$ (the coordinate functions have constant gradient, and $x_C$ is a fixed point).

> [!note]- Hint 2
> The Leibniz expansion gives $\delta^\mu_\rho T^{\nu\rho} - \delta^\nu_\rho T^{\mu\rho} + (x-x_C)^\mu\nabla_\rho T^{\nu\rho} - (x-x_C)^\nu\nabla_\rho T^{\mu\rho}$. The Kronecker deltas contract the first two terms to $T^{\nu\mu} - T^{\mu\nu}$.

> [!note]- Hint 3
> By [[Thm - Energy-Momentum Conservation|energy-momentum conservation]] $\nabla_\rho T^{\nu\rho} = 0$, so the last two (lever-arm) terms vanish identically. Therefore $\nabla_\rho J^{\mu\nu\rho} = T^{\nu\mu} - T^{\mu\nu}$, and this vanishes for all $\mu,\nu$ if and only if $T$ is symmetric.

> [!note]- Hint 4
> For the no-circularity point: the proof of $\nabla_\rho T^{\nu\rho} = 0$ (the conservation theorem) is the localisation argument from the flux of $T$ through closed hypersurfaces — it never uses $T^{\mu\nu} = T^{\nu\mu}$. So symmetry is *derived* from conservation, not assumed; the two are logically independent inputs and the derivation is clean.

---

# Solution

The divergence of the angular-momentum density is, after the lever-arm derivative produces a Kronecker delta and energy-momentum conservation kills the leftover, exactly the antisymmetric part of $T$: $\nabla_\rho J^{\mu\nu\rho} = T^{\nu\mu} - T^{\mu\nu}$. Angular-momentum conservation thus forces $T^{\mu\nu} = T^{\nu\mu}$, and because the conservation theorem was proved without symmetry, there is no circularity.

**Step 1: The divergence of the angular-momentum density is $\nabla_\rho J^{\mu\nu\rho} = T^{\nu\mu} - T^{\mu\nu}$.**

> [!note]- Derivation
> Write the angular-momentum tensor density about $C$ as
> $$J^{\mu\nu\rho} = (x-x_C)^\mu T^{\nu\rho} - (x-x_C)^\nu T^{\mu\rho},$$
> antisymmetric in the index pair $\mu\nu$ (the lever-arm structure). Take the divergence on the current index $\rho$, using the Leibniz rule:
> $$\nabla_\rho J^{\mu\nu\rho} = \big[\nabla_\rho(x-x_C)^\mu\big]T^{\nu\rho} + (x-x_C)^\mu\nabla_\rho T^{\nu\rho} - \big[\nabla_\rho(x-x_C)^\nu\big]T^{\mu\rho} - (x-x_C)^\nu\nabla_\rho T^{\mu\rho}.$$
> The coordinate functions satisfy $\nabla_\rho(x-x_C)^\mu = \partial_\rho x^\mu = \delta^\mu_\rho$ (the point $C$ is fixed, so $\nabla_\rho x_C^\mu = 0$). Hence the first and third terms contract:
> $$\delta^\mu_\rho T^{\nu\rho} = T^{\nu\mu}, \qquad \delta^\nu_\rho T^{\mu\rho} = T^{\mu\nu},$$
> and
> $$\nabla_\rho J^{\mu\nu\rho} = T^{\nu\mu} - T^{\mu\nu} + (x-x_C)^\mu\nabla_\rho T^{\nu\rho} - (x-x_C)^\nu\nabla_\rho T^{\mu\rho}.$$
> By [[Thm - Energy-Momentum Conservation|energy-momentum conservation]], $\nabla_\rho T^{\nu\rho} = 0$ and $\nabla_\rho T^{\mu\rho} = 0$, so the last two (lever-arm) terms vanish identically. Therefore
> $$\boxed{\;\nabla_\rho J^{\mu\nu\rho} = T^{\nu\mu} - T^{\mu\nu}.\;}$$
> Notice the result is independent of $C$ — the $x_C$ terms dropped — so it is a pointwise statement about $T$.

**Step 2: Angular-momentum conservation $\Leftrightarrow$ symmetry of $T$.**

> [!note]- Derivation
> From Step 1, the angular-momentum density is conserved, $\nabla_\rho J^{\mu\nu\rho} = 0$, if and only if $T^{\nu\mu} - T^{\mu\nu} = 0$ for all $\mu,\nu$, i.e. if and only if $T^{\mu\nu} = T^{\nu\mu}$. Conversely, if $T$ is symmetric, the right-hand side vanishes and angular momentum is conserved. So, *given* energy-momentum conservation:
> $$\nabla_\rho J^{\mu\nu\rho} = 0 \quad\Longleftrightarrow\quad T^{\mu\nu} = T^{\nu\mu}.$$
> Physically: the principle that an isolated system conserves angular momentum about every point is *exactly* the statement that its energy-momentum tensor is symmetric. Since angular-momentum conservation is a fundamental physical law (the rotational analogue of momentum conservation), the symmetry of $T$ is a theorem, not an assumption.

**Step 3: No circularity.**

> [!note]- Derivation
> One might worry that this is circular — that proving symmetry "from conservation of angular momentum" secretly assumed symmetry somewhere. It does not. The chain of logic is:
>
> (i) The [[Thm - Energy-Momentum Conservation|energy-momentum conservation law]] $\nabla_\rho T^{\nu\rho} = 0$ is proved *independently* of any symmetry, by the localisation argument: the flux of $T$ through every closed hypersurface vanishes for an isolated system (Gauss/Stokes), hence the divergence vanishes pointwise. Nowhere in that proof is $T^{\mu\nu} = T^{\nu\mu}$ used.
>
> (ii) Step 1 uses *only* $\nabla_\rho T^{\nu\rho} = 0$ (from (i)) to reduce $\nabla_\rho J^{\mu\nu\rho}$ to $T^{\nu\mu} - T^{\mu\nu}$.
>
> (iii) Angular-momentum conservation then forces $T^{\nu\mu} - T^{\mu\nu} = 0$.
>
> So symmetry is *output*, derived from two independent inputs (energy-momentum conservation and angular-momentum conservation), neither of which presupposes it. The derivation is clean — there is no loophole.

**Step 4: Physical interpretation.**

> [!note]- Derivation
> The antisymmetric part of $T$ measures an internal torque density. Consider the stress block $S_{ij} = T_{ij}$ (with $c=1$): $S_{ij}$ is the $i$-momentum crossing a surface with normal $j$, i.e. the force per area on that face. A small cube of medium feels, on its $j$-face, a force with components $S_{ij}$; the *torque* this exerts about the cube's centre involves the antisymmetric combination $S_{ij} - S_{ji}$. If $S$ were not symmetric, $S_{ij} - S_{ji} \ne 0$ would be a net torque per unit volume acting on every infinitesimal element — and an infinitesimal element has infinitesimal moment of inertia, so a finite torque density would spin it up with infinite angular acceleration. A physical medium cannot do this: its stress must be symmetric so that infinitesimal elements feel no runaway torque. The off-diagonal time components similarly: $T^{0i} = T^{i0}$ is the statement that the energy flux equals $c^2$ times the momentum density ($\varphi = c^2\varpi$), which is the relativistic mass-energy equivalence — energy that flows *is* momentum. A non-symmetric $T$ would violate either the no-runaway-torque condition or mass-energy equivalence, both physically forbidden.

> [!note]- Complete formal solution
> For the angular-momentum density $J^{\mu\nu\rho} = (x-x_C)^\mu T^{\nu\rho} - (x-x_C)^\nu T^{\mu\rho}$, the Leibniz rule gives $\nabla_\rho J^{\mu\nu\rho} = \delta^\mu_\rho T^{\nu\rho} - \delta^\nu_\rho T^{\mu\rho} + (x-x_C)^\mu\nabla_\rho T^{\nu\rho} - (x-x_C)^\nu\nabla_\rho T^{\mu\rho}$, using $\nabla_\rho(x-x_C)^\mu = \delta^\mu_\rho$. By energy-momentum conservation $\nabla_\rho T^{\nu\rho} = 0$ the lever-arm terms drop, leaving $\nabla_\rho J^{\mu\nu\rho} = T^{\nu\mu} - T^{\mu\nu}$, independent of $C$. Hence angular-momentum conservation $\nabla_\rho J^{\mu\nu\rho} = 0$ holds if and only if $T^{\mu\nu} = T^{\nu\mu}$. There is no circularity: the conservation law $\nabla_\rho T^{\nu\rho} = 0$ is proved by the flux/localisation argument without using symmetry, so symmetry is genuinely derived. Physically, the antisymmetric part of $T$ is an internal torque density that would spin up infinitesimal elements without bound; its vanishing (the symmetry of $T$) is the absence of such runaway torque, and the equality $T^{0i} = T^{i0}$ is the mass-energy equivalence $\varphi = c^2\varpi$. $\blacksquare$

---

# Key Takeaways

**A symmetry of a tensor can be forced by a conservation law, and the mechanism is always a derivative producing a Kronecker delta.** The proof that $T$ is symmetric works by differentiating the angular-momentum density and noticing that the derivative of the lever arm $(x-x_C)^\mu$ produces $\delta^\mu_\rho$, which contracts the rank-three angular-momentum current down to a bare rank-two $T$ — and that bare $T$ is the antisymmetric part, which conservation then kills. This pattern — "differentiate a current built with an explicit coordinate factor, and the coordinate's derivative produces a delta that collapses the current" — recurs whenever a conservation law constrains a tensor's index symmetry: it is how the symmetry of the canonical stress tensor is improved (Belinfante), how the tracelessness of the dilatation current constrains $T$, and how spin currents are defined. The trigger is any conserved current carrying an explicit $x^\mu$ factor: differentiate, watch for the Kronecker delta, and read off the algebraic constraint on the lower-rank tensor.

**"No circularity" is a real worry in physics derivations, and the fix is to track which results were proved without the property being derived.** It is genuinely tempting to think that deriving the symmetry of $T$ "from conservation" must be circular, because $T$'s symmetry feels built into its definition. The resolution — and the reusable lesson — is to audit the logical order: the energy-momentum conservation law $\nabla_\rho T^{\rho\nu} = 0$ is established by the flux/localisation argument *without* assuming symmetry, so it is a legitimate independent input, and symmetry then follows as output. Whenever you derive property B "from" something that seems to involve property B, the discipline is to find a proof of the input that demonstrably does not use B. This is the same care needed in, for instance, proving the equality of mixed partials, or deriving the symmetry of the Christoffel connection from the torsion-free condition: identify the prior result and confirm it is symmetry-agnostic.

**The symmetry of $T$ encodes two physical facts at once: no runaway internal torque, and mass-energy equivalence.** The off-diagonal *spatial* symmetry $T^{ij} = T^{ji}$ is the statement that the stress exerts no net torque on infinitesimal volume elements — a non-symmetric stress would spin up vanishingly small elements with unbounded angular acceleration, which no physical medium does. The off-diagonal *time-space* symmetry $T^{0i} = T^{i0}$ is the statement $\varphi = c^2\varpi$, that the energy-flux density equals $c^2$ times the momentum density — which is mass-energy equivalence in continuum form: flowing energy *is* momentum. The reusable insight is that a single mathematical condition (symmetry of a tensor) can carry several independent-looking physical principles, and unpacking *which* component-block carries *which* principle is how you connect the abstract statement to laboratory consequences. When you meet a symmetry or antisymmetry condition on a physical tensor, ask separately what its time-time, time-space, and space-space components mean — they usually encode different physics.
