---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Thomas Precession"
  - "Def - Thomas Rotation"
  - "Thm - The Thomas Equation"
tags: [physics, special-relativity]
---

# Problem Statement

Derive the Thomas precession rate directly from the kinematics of Lorentz boosts, showing it is the continuous accumulation of infinitesimal [[Def - Thomas Rotation|Thomas rotations]]. Let $\mathcal{O}$ be a non-rotating accelerated observer ($\vec\omega = 0$), $\mathcal{O}_*$ the reference inertial observer, $S$ the boost carrying $\mathcal{O}_*$'s four-velocity to $\mathcal{O}$'s at proper time $t$, and $\mathbf{V}, \boldsymbol\gamma$ the velocity and acceleration of $\mathcal{O}$ relative to $\mathcal{O}_*$. Working with $c = 1$ except where restored:

1. Set up the evolution of the local frame as $S_{t+\mathrm{d}t} = \Lambda\circ S_t$, where $\Lambda$ is the infinitesimal boost of velocity $\mathbf{W} = c^2\,\mathrm{d}t\,\boldsymbol\gamma$ representing the velocity change in $\mathrm{d}t$.
2. Apply the boost-composition theorem: the product $\Lambda\circ S$ of two non-collinear boosts is *not* a boost but a boost $S'$ times a residual spatial rotation $R$ — the Thomas rotation. Show $\Lambda\circ S = S'\circ R$ with $S' = S_{t+\mathrm{d}t}$.
3. Extract the rotation angle of $R$ per unit time and recover $\vec\omega_T = \frac{\Gamma^2}{c^2(1+\Gamma)}\boldsymbol\gamma\times\mathbf{V}$.
4. Confirm this agrees with the result obtained by the direct Fermi–Walker computation (the [[Thm - The Thomas Equation|Thomas equation]]), and explain why the two routes must give the same answer.

**Recall:**

![[Def - Thomas Precession#The Definition]]

The [[Def - Thomas Rotation|Thomas rotation]] is the spatial rotation left over when two Lorentz boosts of *different* directions are composed: $\Lambda_2\circ\Lambda_1 = S'\circ R$, with $S'$ a boost and $R$ a rotation (the [[Thm - Polar Decomposition of the Lorentz Group|polar decomposition]]). The triad $\boldsymbol\varepsilon_i(t_*) = S^{-1}(e_i(t))$ represents $\mathcal{O}$'s spatial frame in $\mathcal{O}_*$'s rest space, and its evolution $\boldsymbol\varepsilon_i(t_*+\mathrm{d}t_*) = R(\boldsymbol\varepsilon_i(t_*))$ is governed by the Thomas rotation $R$. An infinitesimal boost of velocity $\mathbf{W}$ has Lorentz factor $\approx 1$ and rapidity $\approx |\mathbf{W}|/c$.

---

# Convergent Strategy

**Problem class.** A *compute-a-precession* problem approached through pure group theory: rather than solve the Fermi–Walker transport equation, build the precession from the composition of infinitesimal boosts. The decisive move is to recognise that the boost relating $\mathcal{O}$ to $\mathcal{O}_*$ reorients along the worldline, leaving residual Thomas rotations.

**Assumption pattern.** The observer is non-rotating ($\vec\omega = 0$), so the local frame is dragged along with no intrinsic twist; the *only* rotation seen in $\mathcal{O}_*$'s frame is the kinematic one from composing boosts. The signpost is that the velocity changes direction ($\boldsymbol\gamma$ not collinear with $\mathbf{V}$), so successive boosts are non-collinear and their composition leaves a rotation.

**Theorem routing.** The route is: write the frame evolution $S_{t+\mathrm{d}t} = \Lambda\circ S_t$ with $\Lambda$ the infinitesimal boost of velocity $\mathbf{W} = c^2\mathrm{d}t\,\boldsymbol\gamma$ $\Rightarrow$ apply the [[Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation|boost-composition theorem]] $\Lambda\circ S = S'\circ R$ $\Rightarrow$ extract $R$'s angle per unit time $\Rightarrow$ $\vec\omega_T = \frac{\Gamma^2}{c^2(1+\Gamma)}\boldsymbol\gamma\times\mathbf{V}$. This is the [[Def - Thomas Precession|kinematic derivation]], complementary to the Fermi–Walker route of the [[Thm - The Thomas Equation|Thomas equation]].

**Key decision point.** The crux is that the precession is *pure group theory* — it lives entirely in the non-closure of the boosts under composition, independent of any dynamics or torque. The trap is to look for a force causing the rotation; there is none. The rotation is the residue of $\Lambda\circ S\neq$ boost, and its rate is the differential of the Thomas rotation angle. The two derivations (composition-of-boosts here, Fermi–Walker in the theorem) must agree because they describe the same physical frame.

---

# Legal Operations Used

1. **Decompose a composition of boosts as boost-times-rotation** (operation 7 from the topic page). The entire derivation is this operation: $\Lambda\circ S = S'\circ R$, with the residual rotation $R$ — the [[Def - Thomas Rotation|Thomas rotation]] — accumulating along the worldline into the precession.

2. **Choose the tangent inertial observer and compute there** (operation 2 from the topic page). The boost $S$ relating $\mathcal{O}$ to $\mathcal{O}_*$ is the natural object, and the representative triad $\boldsymbol\varepsilon_i = S^{-1}(e_i)$ lives in $\mathcal{O}_*$'s rest space, where the rotation is read off.

3. **Take the low-velocity / small-distance limit** (operation 9 from the topic page). The infinitesimal boost $\Lambda$ has Lorentz factor $\approx 1$ and rapidity $\approx |\mathbf{W}|/c$, the small-velocity approximation that linearises the composition.

---

# Hints

> [!note]- Hint 1
> The local frame evolves by $\vec e_\alpha(t + \mathrm{d}t) = \Lambda(\vec e_\alpha(t))$ where $\Lambda = \mathrm{Id} + c\,\mathrm{d}t\,a^i K_i$ is the infinitesimal boost generated by the four-acceleration ($K_i$ the boost generators). Its velocity parameter is $\mathbf{W} = c^2\,\mathrm{d}t\,\boldsymbol\gamma$ (the change in $\mathcal{O}$'s velocity over $\mathrm{d}t$, expressed in the instantaneous rest frame). Since the boost $S_{t+\mathrm{d}t}$ carries $\mathcal{O}_*$ to $\mathcal{O}$ at time $t + \mathrm{d}t$, and $\vec e_0(t+\mathrm{d}t) = \Lambda(\vec e_0(t)) = \Lambda\circ S(\vec e_0^*)$, you get $S_{t+\mathrm{d}t} = \Lambda\circ S$ (acting on $\vec e_0^*$).

> [!note]- Hint 2
> $\Lambda$ (boost of velocity $\mathbf{W}$) and $S$ (boost of velocity $\mathbf{V}$) are boosts of *different* directions (since $\boldsymbol\gamma\not\parallel\mathbf{V}$). By the boost-composition theorem their product is $\Lambda\circ S = S'\circ R$, $S'$ a boost and $R$ a spatial rotation in the plane orthogonal to $\vec e_0^*$. Showing $S' = S_{t+\mathrm{d}t}$: both are boosts carrying $\vec e_0^*$ to $\vec e_0(t+\mathrm{d}t)$, so they coincide; hence the triad obeys $\boldsymbol\varepsilon_i(t_*+\mathrm{d}t_*) = R(\boldsymbol\varepsilon_i(t_*))$.

> [!note]- Hint 3
> The Thomas rotation angle for composing a boost of rapidity $\varphi_1$ (velocity $\mathbf{V}$, here $\Gamma_1 = \Gamma$, $V_1 = V$) with an infinitesimal boost of velocity $\mathbf{W} = ac^2\mathrm{d}t$ (so $V_2 = W$, $\Gamma_2\approx 1$) is, to first order in $\mathrm{d}t$, $\mathrm{d}\varphi_T = -\frac{\Gamma}{1+\Gamma}aV\sin\theta\,\mathrm{d}t$ where $\theta$ is the angle between the boosts. Convert $\mathrm{d}t\to\Gamma^{-1}\mathrm{d}t_*$ and express $\sin\theta$ in terms of $\boldsymbol\gamma, \mathbf{V}$ in $\mathcal{O}_*$'s frame.

> [!note]- Hint 4
> The rate $\mathrm{d}\varphi_T/\mathrm{d}t_*$ has magnitude $\frac{\Gamma^2}{c^2(1+\Gamma)}|\boldsymbol\gamma\times\mathbf{V}|$ (since $|\boldsymbol\gamma\times\mathbf{V}| = \gamma V\sin\theta_*$), in the direction $-(\boldsymbol\gamma\times\mathbf{V})$-normal. Assembling the magnitude and direction gives $\vec\omega_T = \frac{\Gamma^2}{c^2(1+\Gamma)}\boldsymbol\gamma\times\mathbf{V}$ — identical to the Fermi–Walker result.

---

# Solution

The precession is the residue of composing boosts. Step 1 writes the frame evolution as an infinitesimal boost applied to the existing one. Step 2 invokes the composition theorem to extract the residual rotation. Step 3 reads off its rate. Step 4 confirms agreement with the direct computation. The non-obvious content is that the rotation is *purely kinematic* — no dynamics — and that its differential reconstructs the same $\vec\omega_T$ as the Fermi–Walker transport.

**Step 1: The frame evolves by $S_{t+\mathrm{d}t} = \Lambda\circ S_t$, $\Lambda$ the infinitesimal boost of velocity $\mathbf{W} = c^2\mathrm{d}t\,\boldsymbol\gamma$.**

> [!note]- Derivation
> The local frame $(\vec e_\alpha(t))$ of the non-rotating observer evolves along the worldline by the law for a frame with vanishing four-rotation: at first order, $\vec e_\alpha(t + \mathrm{d}t) = \Lambda(\vec e_\alpha(t))$, where
> $$\Lambda := \mathrm{Id} + c\,\mathrm{d}t\,a^i K_i$$
> is an infinitesimal Lorentz boost ($a^i$ the components of the four-acceleration in the spatial frame, $K_i$ the boost generators). $\Lambda$ is a *boost* (not a rotation) because $\vec\omega = 0$ — the only generators appearing are the boost generators $K_i$. At first order in $\mathrm{d}t$ its Lorentz factor is $\approx 1$ and its velocity parameter is
> $$\mathbf{W} = c^2\,\mathrm{d}t\,\boldsymbol\gamma,$$
> the change in $\mathcal{O}$'s velocity over the proper-time step $\mathrm{d}t$, expressed in the instantaneous rest frame (to see this, write $\Lambda$ in terms of its rapidity $\delta\psi$ and use $W = c\tanh(\delta\psi)\approx c\,\delta\psi$). Now the boost $S_{t}$ is defined by $\vec e_0(t) = S_t(\vec e_0^*)$; applying $\Lambda$, $\vec e_0(t + \mathrm{d}t) = \Lambda(\vec e_0(t)) = (\Lambda\circ S_t)(\vec e_0^*)$. So the boost at time $t + \mathrm{d}t$ satisfies
> $$S_{t+\mathrm{d}t} = \Lambda\circ S_t \quad(\text{acting on } \vec e_0^*).$$

**Step 2: $\Lambda\circ S = S'\circ R$ with $S' = S_{t+\mathrm{d}t}$ and $R$ the Thomas rotation.**

> [!note]- Derivation
> $\Lambda$ is a boost of velocity $\mathbf{W} = c^2\mathrm{d}t\,\boldsymbol\gamma$, and $S = S_t$ is a boost of velocity $\mathbf{V}$. Since $\boldsymbol\gamma$ is *not* collinear with $\mathbf{V}$ (the velocity is turning), these two boosts have different directions. By the [[Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation|composition theorem]] (equivalently the [[Thm - Polar Decomposition of the Lorentz Group|polar decomposition]]), the product of two non-collinear boosts is *not* a boost but a boost times a spatial rotation:
> $$\Lambda\circ S = S'\circ R,$$
> where $S'$ is a boost whose plane contains $\vec e_0^*$, and $R$ is the **Thomas rotation**, a spatial rotation in the plane orthogonal to $\vec e_0^*$ (i.e. acting within $\mathcal{O}_*$'s rest space).
>
> To identify $S'$: since $R(\vec e_0^*) = \vec e_0^*$ (a spatial rotation fixes the time axis), $S'(\vec e_0^*) = (S'\circ R)(\vec e_0^*) = (\Lambda\circ S)(\vec e_0^*) = \vec e_0(t + \mathrm{d}t) = S_{t+\mathrm{d}t}(\vec e_0^*)$. Both $S'$ and $S_{t+\mathrm{d}t}$ are boosts carrying $\vec e_0^*$ to the *same* vector $\vec e_0(t+\mathrm{d}t)$, hence they coincide: $S' = S_{t+\mathrm{d}t}$. Therefore $\Lambda\circ S_t = S_{t+\mathrm{d}t}\circ R$, i.e. $S_{t+\mathrm{d}t}^{-1}\circ\Lambda\circ S_t = R$.
>
> The representative triad is $\boldsymbol\varepsilon_i(t_*) = S_t^{-1}(\vec e_i(t))$. Its evolution: $\boldsymbol\varepsilon_i(t_* + \mathrm{d}t_*) = S_{t+\mathrm{d}t}^{-1}(\vec e_i(t+\mathrm{d}t)) = S_{t+\mathrm{d}t}^{-1}\Lambda(\vec e_i(t)) = S_{t+\mathrm{d}t}^{-1}\Lambda S_t(\boldsymbol\varepsilon_i(t_*)) = R(\boldsymbol\varepsilon_i(t_*))$. So the triad rotates by the Thomas rotation $R$ each step — even though the local frame is non-rotating ($\vec\omega = 0$).

**Step 3: The rotation rate is $\vec\omega_T = \frac{\Gamma^2}{c^2(1+\Gamma)}\boldsymbol\gamma\times\mathbf{V}$.**

> [!note]- Derivation
> The Thomas rotation angle for composing a boost of velocity $\mathbf{V}$ (Lorentz factor $\Gamma_1 = \Gamma$, speed $V_1 = V$) with an infinitesimal boost of velocity $\mathbf{W}$ (speed $V_2 = W = ac^2\mathrm{d}t$, factor $\Gamma_2\approx 1$) is given by the general boost-composition rotation-angle formula. To first order in $\mathrm{d}t$ (so all higher-order terms in $W$ drop), it reduces to
> $$\mathrm{d}\varphi_T = -\frac{\Gamma}{1 + \Gamma}\,a\,V\,\sin\theta\,\mathrm{d}t,$$
> where $\theta$ is the angle between the two boosts $S(\vec V)$ and $\mathbf{W}\propto\boldsymbol\gamma$, measured in the instantaneous rest space $E_u(t)$ of $\mathcal{O}$. Converting proper time to laboratory time via $\mathrm{d}t = \Gamma^{-1}\mathrm{d}t_*$, and re-expressing $a\sin\theta$ in $\mathcal{O}_*$'s frame: using $a\sin\theta = \Gamma^2\gamma\sin\theta_*/c^2$ (the relation between the rest-frame angle $\theta$ and the $\mathcal{O}_*$-frame angle $\theta_*$ between $\boldsymbol\gamma$ and $\mathbf{V}$, where $\gamma = \|\boldsymbol\gamma\|$),
> $$\frac{\mathrm{d}\varphi_T}{\mathrm{d}t_*} = -\frac{\Gamma^2}{1+\Gamma}\frac{\gamma V}{c^2}\sin\theta_*.$$
> Now $|\boldsymbol\gamma\times\mathbf{V}| = \gamma V\sin\theta_*$, and the rotation is in the plane $\mathrm{Span}(\mathbf{V}, \boldsymbol\gamma)$ with axis along $-(\boldsymbol\gamma\times\mathbf{V})$-normal (the $-$ sign from the formula). Assembling magnitude and direction into a vector,
> $$\vec\omega_T = \frac{\Gamma^2}{c^2(1+\Gamma)}\,\boldsymbol\gamma\times\mathbf{V}.$$
> This is the [[Def - Thomas Precession|Thomas precession rate]], built purely from the composition of boosts.

**Step 4: Agreement with the Fermi–Walker computation, and why it must hold.**

> [!note]- Derivation
> The [[Thm - The Thomas Equation|Thomas equation]], derived by a completely different route — directly integrating the Fermi–Walker transport law for the spin without ever invoking the composition of boosts — gives the *same* precession vector
> $$\vec\omega_T = \frac{\Gamma^2}{c^2(1+\Gamma)}\,\boldsymbol\gamma\times\mathbf{V}.$$
> The two derivations agree exactly. They must, because they describe the *same physical object*: the rotation, relative to $\mathcal{O}_*$, of the spatial frame carried non-rotatingly by $\mathcal{O}$. The Fermi–Walker route says "the spin is intrinsically rigid; express it in the lab frame and watch it precess"; the composition-of-boosts route says "the boost displaying the spin keeps reorienting, leaving residual Thomas rotations". These are two descriptions of one fact, related by the identity that the boost $S$ stopping the particle is exactly the inverse of the Fermi–Walker transport's frame.
>
> The conceptual lesson is that Thomas precession is *purely kinematic* — it lives entirely in the non-closure of the Lorentz boosts under composition (the failure of two boosts to compose to a boost), with no reference to any dynamics, force, or torque. The same non-closure makes the open velocity ball a **gyrogroup**: the Thomas rotation is the *gyration* that repairs the failure of velocity addition to be commutative, and Thomas precession is its time-derivative version. Composing boosts and precessing a gyroscope are the same fact at two scales — discrete and differential.

> [!note]- Complete formal solution
> The non-rotating frame evolves by $\vec e_\alpha(t+\mathrm{d}t) = \Lambda(\vec e_\alpha(t))$ with $\Lambda$ an infinitesimal boost of velocity $\mathbf{W} = c^2\mathrm{d}t\,\boldsymbol\gamma$, so $S_{t+\mathrm{d}t} = \Lambda\circ S_t$. Since $\boldsymbol\gamma\not\parallel\mathbf{V}$, the boosts $\Lambda$ and $S_t$ are non-collinear, and by the composition theorem $\Lambda\circ S_t = S'\circ R$ with $S'$ a boost, $R$ the Thomas rotation; as $R$ fixes $\vec e_0^*$, $S' = S_{t+\mathrm{d}t}$, so the representative triad obeys $\boldsymbol\varepsilon_i(t_*+\mathrm{d}t_*) = R(\boldsymbol\varepsilon_i(t_*))$ — the triad rotates despite $\vec\omega = 0$. The Thomas rotation angle to first order is $\mathrm{d}\varphi_T = -\frac{\Gamma}{1+\Gamma}aV\sin\theta\,\mathrm{d}t$; converting $\mathrm{d}t = \Gamma^{-1}\mathrm{d}t_*$ and using $|\boldsymbol\gamma\times\mathbf{V}| = \gamma V\sin\theta_*$ gives $\vec\omega_T = \frac{\Gamma^2}{c^2(1+\Gamma)}\boldsymbol\gamma\times\mathbf{V}$ — identical to the Fermi–Walker result of the Thomas equation, as it must be since both describe the same physical frame. The precession is pure group theory: the residue of boosts failing to close under composition, the differential of the gyrogroup gyration. $\blacksquare$

---

# Key Takeaways

**Thomas precession is the residue of boosts failing to compose to a boost — pure group theory, no dynamics.** The deepest takeaway is that the precession arises *entirely* from the non-closure of the Lorentz boosts under composition: the product of two non-collinear boosts is a boost *times a rotation* (the [[Def - Thomas Rotation|Thomas rotation]]), and integrating these residual rotations along a curving worldline gives the precession. There is no force, no torque, no dynamics — it is a kinematic fact about the structure of the Lorentz group. The trigger to recognise this: whenever a frame is transported by a continuously-reorienting boost (any non-straight-line motion), expect a kinematic rotation from the boost non-closure, independent of whatever forces are bending the trajectory. This is why the precession appears identically for a gyroscope, an electron, and a charged beam — the cause is the group, not the particle.

**Two derivations of the same precession must agree — and seeing why is instructive.** The composition-of-boosts route here and the Fermi–Walker route of the [[Thm - The Thomas Equation|Thomas equation]] give *identical* $\vec\omega_T$, by entirely different computations. They must, because both describe the rotation of the same physical frame relative to the laboratory. The reusable principle: when a physical quantity can be computed two ways, the agreement is not a coincidence but a constraint, and finding the dictionary between the two computations (here: the stopping boost $S$ is the inverse of the Fermi–Walker frame) deepens the understanding of both. The composition route emphasises the *origin* (boosts not closing); the Fermi–Walker route emphasises the *transport* (a rigid spin displayed in a turning frame). Holding both pictures is what makes Thomas precession intuitive rather than a formula.

**The Thomas rotation is the gyration of the velocity gyrogroup.** A unifying structural insight is that the same non-closure that produces Thomas precession makes the open ball of velocities a *gyrogroup* — a group-like structure in which addition is non-commutative and non-associative, repaired by a "gyration" automorphism. That gyration is exactly the Thomas rotation: the rotation by which $\mathbf{u}\oplus\mathbf{v}$ and $\mathbf{v}\oplus\mathbf{u}$ differ. Thomas precession is the *differential, time-rate version* of this discrete gyration. The trigger: whenever relativistic velocity addition's non-commutativity matters (composing boosts in different directions), the correction is a Thomas rotation, and its accumulation in time is a Thomas precession. This links the kinematics of this chapter to the algebraic structure of the [[Special Relativity XVI — Accelerated Observers#Bridges|velocity ball]], and shows that "boosts don't commute" and "gyroscopes precess" are one phenomenon.

This exercise gives the kinematic origin of the rate used in [[Ex - Thomas precession of a gyroscope in circular orbit]] and applied in [[Ex - The Thomas half and atomic fine structure]]; it is the bridge from the [[Def - Thomas Rotation|Thomas rotation]] of the Lorentz-group chapter to the [[Def - Thomas Precession|Thomas precession]] of this one.
