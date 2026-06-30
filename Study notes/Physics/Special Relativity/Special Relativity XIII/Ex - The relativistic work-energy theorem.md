---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Thm - Relativistic Newton's Second Law"
  - "Def - Four-Force"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Problem Statement

A particle of rest mass $m$ moves under a **pure** (mass-preserving) three-force $\mathbf{f}$ as seen by an inertial observer. Work with $c = 1$.

1. Starting from the constancy of the rest mass, $\tfrac{d}{d\tau}(P\cdot P) = 0$, derive the **relativistic work–energy theorem**
$$\frac{dE}{dt} = \mathbf{f}\cdot\mathbf{u},$$
the rate of change of the particle's energy equalling the power delivered by the force.
2. Show that this is precisely the *time component* of the covariant equation of motion $F^\mu = dP^\mu/d\tau$, and that it follows directly from the orthogonality $F\cdot U = 0$ of a pure four-force.
3. Integrate the theorem to find the work $W$ done in accelerating the particle from rest to speed $u$, and confirm $W = (\gamma - 1)m$, the relativistic kinetic energy.
4. Verify the Newtonian limit: show $dE/dt \to \tfrac{d}{dt}(\tfrac12 m u^2)$ as $u\to 0$, and identify the leading relativistic correction.

**Recall:**

![[Thm - Relativistic Newton's Second Law#Statement]]

The [[Def - Four-Momentum and Rest Mass|four-momentum]] is $P^\mu = (E, \mathbf{p})$ with $E = \gamma m$, $\mathbf{p} = \gamma m\mathbf{u}$, $P\cdot P = E^2 - \mathbf{p}^2 = m^2$. The [[Def - Four-Force|four-force]] is $F^\mu = dP^\mu/d\tau$, satisfying $F\cdot U = dm/d\tau$; a **pure** force has $F\cdot U = 0$ and so preserves the rest mass. Proper and coordinate time are related by $dt/d\tau = \gamma$, so $d/d\tau = \gamma\,d/dt$. The four-velocity is $U^\mu = \gamma(1, \mathbf{u})$.

---

# Convergent Strategy

**Problem class.** A *projection of the covariant equation of motion* problem: take the four-vector law $F^\mu = dP^\mu/d\tau$ and read off its time component relative to an inertial observer. The work–energy theorem is the temporal partner of Newton's spatial law $d\mathbf{p}/dt = \mathbf{f}$.

**Assumption pattern.** A pure force, so $dm/d\tau = 0$ and $P\cdot P = m^2$ is fixed. The signpost is "power" or "work" or "energy change": these are the time component of the equation of motion.

**Theorem routing.** Two equivalent routes, both from [[Thm - Relativistic Newton's Second Law]]: (i) differentiate the invariant $P\cdot P = m^2$ and use $\mathbf{p} = E\mathbf{u}$; (ii) contract the four-force law with $U$ and use the purity $F\cdot U = 0$. The integration in Part 3 uses $dE = \mathbf{f}\cdot d\mathbf{x}$ and the energy $E = \gamma m$.

**Key decision point.** The crux is recognising that the rest-mass constraint $P\cdot P = m^2$ is *itself* the work–energy theorem in disguise: differentiating it forces $E\,dE = \mathbf{p}\cdot d\mathbf{p}$, and with $\mathbf{p} = E\mathbf{u}$ this is exactly $dE = \mathbf{u}\cdot d\mathbf{p} = \mathbf{u}\cdot\mathbf{f}\,dt$. Energy and momentum cannot change independently — they are tied by the fixed Minkowski length — and "tied" is precisely the statement $dE = \mathbf{u}\cdot d\mathbf{p}$.

---

# Legal Operations Used

1. **Square (here differentiate the square of) a four-momentum to use its invariant mass** (operation 2). The constraint $P\cdot P = m^2$ differentiated gives $P\cdot dP/d\tau = 0$, the seed of the theorem.

2. **Differentiate four-momentum with respect to proper time to get the four-force** (operation 9). $F^\mu = dP^\mu/d\tau$, whose time component is $dE/d\tau$, converts to $dE/dt$ via $d/d\tau = \gamma\,d/dt$.

3. **Use $E = P\cdot U_0$ to read the energy an observer measures** (operation 5). The energy whose evolution we track is the time component of $P$ relative to the inertial observer.

---

# Hints

> [!note]- Hint 1
> For a pure force the rest mass is constant, so $P\cdot P = E^2 - \mathbf{p}^2 = m^2$ is fixed in time. Differentiate with respect to $t$: $2E\,\tfrac{dE}{dt} - 2\mathbf{p}\cdot\tfrac{d\mathbf{p}}{dt} = 0$.

> [!note]- Hint 2
> Use $\mathbf{p} = \gamma m\mathbf{u} = E\mathbf{u}$ (since $E = \gamma m$) and Newton's spatial law $d\mathbf{p}/dt = \mathbf{f}$. Then $E\,\tfrac{dE}{dt} = \mathbf{p}\cdot\mathbf{f} = E\mathbf{u}\cdot\mathbf{f}$; cancel $E$.

> [!note]- Hint 3
> For the covariant route: a pure four-force satisfies $F\cdot U = 0$. Write it in components, $F = (F^0, \gamma\mathbf{f})$ and $U = \gamma(1, \mathbf{u})$: $F\cdot U = \gamma F^0 - \gamma^2\mathbf{f}\cdot\mathbf{u} = 0$, so $F^0 = \gamma\mathbf{f}\cdot\mathbf{u}$. Since $F^0 = dE/d\tau = \gamma\,dE/dt$, this gives $dE/dt = \mathbf{f}\cdot\mathbf{u}$.

> [!note]- Hint 4
> For the work: $W = \int \mathbf{f}\cdot d\mathbf{x} = \int \mathbf{f}\cdot\mathbf{u}\,dt = \int \tfrac{dE}{dt}\,dt = \Delta E = \gamma m - m = (\gamma - 1)m$. The work done equals the change in $E = \gamma m$, and starting from rest that change is the kinetic energy.

---

# Solution

The relativistic work–energy theorem is the time component of the equation of motion, and it is forced by the constancy of the rest mass: energy and momentum are locked together by $E^2 - \mathbf{p}^2 = m^2$, so a force that changes the momentum must change the energy in lockstep, and the lockstep ratio is exactly the velocity.

**Step 1: From the mass-shell to $dE/dt = \mathbf{f}\cdot\mathbf{u}$.**

> [!note]- Derivation
> For a pure force the rest mass is preserved, so the [[Def - Four-Momentum and Rest Mass|mass-shell relation]] holds at all times with constant $m$:
> $$P\cdot P = E^2 - \mathbf{p}^2 = m^2 = \text{const}.$$
> Differentiate with respect to coordinate time $t$:
> $$2E\,\frac{dE}{dt} - 2\mathbf{p}\cdot\frac{d\mathbf{p}}{dt} = 0 \quad\Longrightarrow\quad E\,\frac{dE}{dt} = \mathbf{p}\cdot\frac{d\mathbf{p}}{dt}.$$
> Now use two facts from [[Thm - Relativistic Newton's Second Law|the relativistic second law]]: the spatial equation of motion $d\mathbf{p}/dt = \mathbf{f}$, and the relation $\mathbf{p} = \gamma m\mathbf{u} = E\mathbf{u}$ (since $E = \gamma m$). Substituting,
> $$E\,\frac{dE}{dt} = (E\mathbf{u})\cdot\mathbf{f} = E\,(\mathbf{u}\cdot\mathbf{f}),$$
> and cancelling the common $E > 0$:
> $$\boxed{\ \frac{dE}{dt} = \mathbf{f}\cdot\mathbf{u}\ }.$$
> The rate of change of the particle's energy equals the power delivered by the force — the **relativistic work–energy theorem**. Note this used *only* the constancy of the rest mass and Newton's spatial law; the theorem is, at bottom, the differential statement of the mass-shell constraint.

**Step 2: It is the time component of $F^\mu = dP^\mu/d\tau$.**

> [!note]- Derivation
> The covariant equation of motion is $F^\mu = dP^\mu/d\tau$. Its time component is $F^0 = dE/d\tau = \gamma\,dE/dt$ (using $d/d\tau = \gamma\,d/dt$). To identify $F^0$, contract the four-force with the four-velocity. For a **pure** force $F\cdot U = 0$ ([[Def - Four-Force|definition of pure force]]); writing $F^\mu = (F^0, \gamma\mathbf{f})$ (the spatial four-force is $\gamma$ times the ordinary force) and $U^\mu = \gamma(1, \mathbf{u})$,
> $$F\cdot U = F^0 U^0 - \mathbf{F}\cdot\mathbf{U} = \gamma F^0 - \gamma\mathbf{f}\cdot(\gamma\mathbf{u}) = \gamma F^0 - \gamma^2\mathbf{f}\cdot\mathbf{u} = 0,$$
> so $F^0 = \gamma\,\mathbf{f}\cdot\mathbf{u}$. Equating to $F^0 = \gamma\,dE/dt$ and cancelling $\gamma$:
> $$\frac{dE}{dt} = \mathbf{f}\cdot\mathbf{u},$$
> the same theorem. So the spatial part of $F^\mu = dP^\mu/d\tau$ is Newton's force law $d\mathbf{p}/dt = \mathbf{f}$ and the *time part is the work–energy theorem* — the two are the space and time components of a single four-vector equation, and the orthogonality $F\cdot U = 0$ is what makes the time component come out as the power. (This is Gourgoulhon's eq. 9.124, $dE/dt = \langle F, V\rangle + (c^2/\Gamma)\,dm/dt$, specialised to a pure force, $dm/dt = 0$.)

**Step 3: The work integrates to the kinetic energy.**

> [!note]- Derivation
> Integrate the theorem along the trajectory from rest to speed $u$. The work done by the force is
> $$W = \int \mathbf{f}\cdot d\mathbf{x} = \int \mathbf{f}\cdot\mathbf{u}\,dt = \int \frac{dE}{dt}\,dt = E_{\text{final}} - E_{\text{initial}}.$$
> With $E = \gamma m$ and the particle starting at rest ($\gamma = 1$, $E_{\text{initial}} = m$) and ending at speed $u$ ($\gamma = (1-u^2)^{-1/2}$, $E_{\text{final}} = \gamma m$),
> $$\boxed{\ W = \gamma m - m = (\gamma - 1)m\ } = E_{\text{kin}}.$$
> The work done equals the change in the total energy, and since the rest energy $m$ does not change (pure force), it equals the **kinetic energy** $E_{\text{kin}} = (\gamma - 1)m$. This is the relativistic replacement for the Newtonian $\tfrac12 mu^2$, and it diverges as $u\to c$: infinite work is required to reach the speed of light, the energetic statement of the speed limit.

**Step 4: Newtonian limit and leading correction.**

> [!note]- Derivation
> Expand the kinetic energy for small $u$. With $\gamma = (1-u^2)^{-1/2} = 1 + \tfrac12 u^2 + \tfrac38 u^4 + \cdots$,
> $$E_{\text{kin}} = (\gamma - 1)m = \tfrac12 m u^2 + \tfrac38 m u^4 + \cdots.$$
> The leading term is the Newtonian kinetic energy $\tfrac12 mu^2$, so $dE/dt = dE_{\text{kin}}/dt \to \tfrac{d}{dt}(\tfrac12 mu^2) = m\mathbf{u}\cdot\mathbf{a}$ as $u\to 0$, recovering the Newtonian work–energy theorem (with $\mathbf{f} = m\mathbf{a}$). The first relativistic correction is $+\tfrac38 mu^4$ (restoring $c$: $\tfrac38 mu^4/c^2$), positive — the true kinetic energy *exceeds* the Newtonian value, increasingly so as $u$ grows, because the particle's inertia rises with speed. At $u = 0.1c$ the correction is about $0.4\%$; near $c$ it dominates entirely.

> [!note]- Complete formal solution
> For a pure force $m$ is constant, so $E^2 - \mathbf{p}^2 = m^2$; differentiating in $t$, $E\,dE/dt = \mathbf{p}\cdot d\mathbf{p}/dt$. With $\mathbf{p} = E\mathbf{u}$ and $d\mathbf{p}/dt = \mathbf{f}$, this gives $dE/dt = \mathbf{f}\cdot\mathbf{u}$ — the work–energy theorem. Equivalently it is the time component of $F^\mu = dP^\mu/d\tau$: purity $F\cdot U = 0$ gives $F^0 = \gamma\mathbf{f}\cdot\mathbf{u}$, and $F^0 = \gamma\,dE/dt$ yields the same. Integrating, $W = \int\mathbf{f}\cdot\mathbf{u}\,dt = \Delta E = (\gamma-1)m$, the relativistic kinetic energy. For $u\to 0$, $(\gamma-1)m = \tfrac12 mu^2 + \tfrac38 mu^4 + \cdots$, recovering Newton with leading correction $+\tfrac38 mu^4$. $\blacksquare$

---

# Key Takeaways

**The work–energy theorem is the constancy of the rest mass, differentiated.** The most economical way to understand $dE/dt = \mathbf{f}\cdot\mathbf{u}$ is not as an independent dynamical law but as the time-derivative of the mass-shell constraint $E^2 - \mathbf{p}^2 = m^2$. Because a pure force keeps the rest mass fixed, the energy and momentum are forced to move together along the mass-shell hyperboloid, and "together" means $E\,dE = \mathbf{p}\cdot d\mathbf{p}$; substituting $\mathbf{p} = E\mathbf{u}$ collapses this to $dE = \mathbf{u}\cdot d\mathbf{p} = \mathbf{u}\cdot\mathbf{f}\,dt$. This is the same structural fact that makes energy and momentum the two parts of one four-vector: they are not free to vary independently, and the relation that binds them *is* the work–energy theorem. The reusable insight is that a conserved invariant, differentiated, generally yields a useful evolution equation — here the invariant rest mass yields the power law — so when you need to relate the rates of change of two quantities, look first for an invariant that ties them together.

**Energy and Newton's law are the time and space parts of one four-vector equation.** This exercise drills the master pattern of relativistic dynamics: the single covariant equation $F^\mu = dP^\mu/d\tau$ contains *both* the familiar force law and the work–energy theorem, as its spatial and temporal components relative to an inertial observer. Newton kept these separate — his second law, and the work–energy relation derived from it — but relativity reveals them as one statement, just as it reveals momentum and energy as one four-vector $P^\mu = (E, \mathbf{p})$. The orthogonality $F\cdot U = 0$ of a pure force is the precise hinge: it forces the time component $F^0$ to equal $\gamma\mathbf{f}\cdot\mathbf{u}$, which is exactly the power. Whenever a problem asks about the rate of working or the energy gained, recognise it as the time component of the equation of motion, and either project $F^\mu = dP^\mu/d\tau$ or — faster — differentiate the rest-mass constraint.

**The work to accelerate is $(\gamma-1)m$, and it diverges at $c$.** Integrating the theorem gives the relativistic kinetic energy $W = (\gamma - 1)m$, the proper replacement for $\tfrac12 mu^2$, and its behaviour as $u\to c$ is the energetic face of the speed limit: $\gamma\to\infty$, so the work required to reach the speed of light is infinite, and no finite energy source can get a massive particle there. The Newtonian $\tfrac12 mu^2$ is only the first term of the expansion $(\gamma-1)m = \tfrac12 mu^2 + \tfrac38 mu^4 + \cdots$, and the corrections are all positive — the true kinetic energy always exceeds the Newtonian estimate, because the inertia grows with speed. The reusable diagnostic: to judge how much energy a relativistic process costs, use $E = \gamma m$ and $E_{\text{kin}} = (\gamma - 1)m$, never $\tfrac12 mu^2$; the divergence of $\gamma$ near $c$ is what makes accelerators ever more expensive per increment of speed, and it is the same divergence that appears as the punishing mass ratio of the [[Ex - The relativistic rocket|relativistic rocket]].
