---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Four-Force"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ but restore it where instructive, with $\eta = \operatorname{diag}(+1,-1,-1,-1)$. A particle of rest mass $m$ has [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu = (E,\mathbf{p})$, [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U^\mu = \gamma(1,\mathbf{u})$, and [[Def - Four-Force|four-force]] $F^\mu = dP^\mu/d\tau$, parametrised by [[Def - Proper Time|proper time]] $\tau$. Relative to an inertial frame: $\mathbf{u} = d\mathbf{x}/dt$ the three-velocity, $u = |\mathbf{u}|$, $\gamma = (1-u^2)^{-1/2}$, $dt/d\tau = \gamma$, $\mathbf{a} = d\mathbf{u}/dt$ the ordinary three-acceleration, $\mathbf{f}$ the ordinary three-force. Full registry on [[Special Relativity XIII — Energy and Momentum]].

---

# Statement

> **Relativistic Newton's second law.** The equation of motion of a particle acted on by a [[Def - Four-Force|four-force]] $F^\mu$ is
> $$F^\mu \;=\; \frac{dP^\mu}{d\tau}.$$
> Relative to an inertial observer, writing $F^\mu = (F^0, \gamma\mathbf{f})$ with $\mathbf{f} = d\mathbf{p}/dt$ the ordinary three-force, this is equivalent to the pair
> $$\boxed{\ \frac{d\mathbf{p}}{dt} = \mathbf{f}, \qquad \frac{dE}{dt} = \mathbf{f}\cdot\mathbf{u}\ }\qquad (\mathcal{O}\ \text{inertial}),$$
> with $\mathbf{p} = \gamma m\mathbf{u}$ the relativistic momentum and $E = \gamma m$ the energy: the **spatial** part is Newton's second law for the relativistic momentum, the **temporal** part is the **work–energy theorem**, the power delivered equalling the rate of change of energy.

> **Acceleration is not parallel to force.** For a pure (mass-preserving) force, expanding $\mathbf{f} = d(\gamma m\mathbf{u})/dt$ gives
> $$\mathbf{f} = \gamma m\,\mathbf{a} + \gamma^3 m\,(\mathbf{a}\cdot\mathbf{u})\,\mathbf{u},$$
> so the response is $\gamma m$ to a transverse force and $\gamma^3 m$ to a longitudinal one; the acceleration is parallel to the force only when $\mathbf{f}$ is purely transverse or purely longitudinal, and is reduced relative to the Newtonian $\mathbf{a} = \mathbf{f}/m$ by these $\gamma$-factors. In the limit $\gamma\to 1$, $\mathbf{f} = m\mathbf{a}$, Newton's law.

---

# Motivation

The [[Def - Four-Force|four-force]] $F^\mu = dP^\mu/d\tau$ is a covariant equation, manifestly the same in every frame. But it is written with proper time and four-vectors, and a working physicist standing in a laboratory wants the law in *their* frame, in terms of the ordinary force they apply, the ordinary momentum, and the ordinary energy. This theorem projects the covariant equation onto an inertial observer and recovers two familiar-looking laws — Newton's second law and the work–energy theorem — in their relativistically corrected forms.

The reason both laws emerge from one equation is that $F^\mu = dP^\mu/d\tau$ is a four-vector equation, four scalar equations in one. Its *spatial* components, after converting proper time to coordinate time ($d/d\tau = \gamma\,d/dt$), give $\mathbf{f} = d\mathbf{p}/dt$ — Newton's $\mathbf{f} = $ rate of change of momentum, with the relativistic momentum $\mathbf{p} = \gamma m\mathbf{u}$ in place of $m\mathbf{u}$. Its *temporal* component gives $dE/dt = \mathbf{f}\cdot\mathbf{u}$ — the work–energy theorem, the power $\mathbf{f}\cdot\mathbf{u}$ equalling the rate of change of energy. Newton kept these as separate statements (his second law, and the work–energy relation derived from it); relativity reveals them as the space and time parts of a single four-vector law, just as it revealed momentum and energy as the space and time parts of a single four-vector.

The genuinely new physics is hidden in a place that looks innocuous: the relationship between force and *acceleration*. In Newtonian mechanics $\mathbf{a} = \mathbf{f}/m$ — acceleration is force over mass, always parallel to the force. Relativistically this fails, and it fails for a structural reason. The momentum is $\mathbf{p} = \gamma m\mathbf{u}$, and $\gamma$ depends on the *speed*, so when you push a particle you change both its direction of motion and its $\gamma$; differentiating $\gamma m\mathbf{u}$ produces a term along $\mathbf{u}$ (from $d\gamma/dt$) in addition to the term along $\mathbf{a}$. The upshot is that a force along the motion is "harder" than a force across it — the particle responds with effective inertia $\gamma^3 m$ longitudinally but only $\gamma m$ transversely. This is why a particle approaching $c$ becomes ever more reluctant to be sped up further (the $\gamma^3$ resists changes in speed) while still turning relatively easily (the $\gamma$ governs changes in direction), and it is the dynamical mechanism enforcing the speed limit: no finite force, applied for any finite time, gets a massive particle to $c$.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a particle subject to a four-force", and input-broadening is about recognising the projected forms.

The first disguised source is **"a known three-force in the lab"** — an applied electric field, a mechanical push. The lab force $\mathbf{f}$ is the spatial part of the four-force (up to $\gamma$), so $d\mathbf{p}/dt = \mathbf{f}$ governs the motion, with $\mathbf{p} = \gamma m\mathbf{u}$. The bridge is the projection of $F^\mu = dP^\mu/d\tau$ onto the lab observer. *Example problem:* a charge in a uniform electric field, $d\mathbf{p}/dt = q\mathbf{E}$ ([[Ex - A charged particle in a uniform electric field]]).

The second disguised source is **"the power delivered to a particle"** — the rate of working $\mathbf{f}\cdot\mathbf{u}$. This is the temporal part of the four-force law, equal to $dE/dt$. The bridge is the work–energy theorem. *Example problem:* finding how fast a particle's energy grows in an accelerator, $dE/dt = \mathbf{f}\cdot\mathbf{u}$.

The third disguised source is **"a charged particle in an electromagnetic field"** — the one fundamental relativistic force. The four-force is $F^\mu = q F^\mu{}_\nu U^\nu$, pure (mass-preserving), so $d\mathbf{p}/dt = q(\mathbf{E} + \mathbf{u}\times\mathbf{B})$ and the rest mass is constant. The bridge is the [[Def - Four-Force|Lorentz four-force]]. *Example problem:* cyclotron motion, $\omega = qB/\gamma m$.

**Targets (Output Amplification)**

The conclusions are $d\mathbf{p}/dt = \mathbf{f}$, $dE/dt = \mathbf{f}\cdot\mathbf{u}$, and the force–acceleration relation $\mathbf{f} = \gamma m\mathbf{a} + \gamma^3 m(\mathbf{a}\cdot\mathbf{u})\mathbf{u}$.

Combine $d\mathbf{p}/dt = \mathbf{f}$ with **a constant force**. Integrating $\mathbf{p} = \mathbf{f}t$ (from rest) and inverting $\mathbf{p} = \gamma m\mathbf{u}$ gives the velocity $u = ft/\sqrt{m^2 + f^2t^2}$, which approaches but never reaches $c$. The further result is hyperbolic motion — constant proper acceleration, the worldline $x^2 - t^2 = \text{const}$. The combination is useful because it shows a *constant* force does not give constant acceleration (Newton) but constant *proper* acceleration. *Example:* the uniformly accelerated observer of [[Special Relativity XVI — Accelerated Observers|Special Relativity XVI]].

Combine the force–acceleration relation with **a transverse vs longitudinal force**. Resolving $\mathbf{f}$ into parts along and across $\mathbf{u}$ gives $f_\parallel = \gamma^3 m\,a_\parallel$ and $f_\perp = \gamma m\,a_\perp$ — the "longitudinal mass" $\gamma^3 m$ and "transverse mass" $\gamma m$. The further result is that the same force produces different accelerations depending on its orientation relative to the velocity. The combination is nonobvious because it means inertia is *anisotropic* at relativistic speeds — a particle resists being sped up more than being turned. *Example:* the difference between accelerating and steering a relativistic beam ([[Ex - The acceleration is not parallel to the force]]).

---

# Why Is It True

The reason both Newton's law and the work–energy theorem fall out of one equation is that $F^\mu = dP^\mu/d\tau$ is a *four-vector* equation, and a four-vector equation is four scalar equations bundled together. The four-momentum is $P^\mu = (E, \mathbf{p})$, so its proper-time derivative is $(dE/d\tau, d\mathbf{p}/d\tau)$. Converting to coordinate time with $d/d\tau = \gamma\,d/dt$ (the chain rule, since $dt/d\tau = \gamma$), the spatial components read $\gamma\,d\mathbf{p}/dt = F^{\text{spatial}}$, and defining the ordinary force as $\mathbf{f} = d\mathbf{p}/dt$ (so $F^{\text{spatial}} = \gamma\mathbf{f}$) gives $d\mathbf{p}/dt = \mathbf{f}$. The temporal component reads $\gamma\,dE/dt = F^0$, and a short calculation (or the orthogonality $F\cdot U = 0$ for a pure force) shows $F^0 = \gamma\,\mathbf{f}\cdot\mathbf{u}$, giving $dE/dt = \mathbf{f}\cdot\mathbf{u}$. **The spatial part is Newton's force law and the temporal part is the work–energy theorem, because they are the space and time components of the single four-force equation.**

The work–energy theorem can also be seen as a consequence of the rest mass being constant. For a pure force, $P\cdot P = m^2$ is fixed, so differentiating, $\tfrac{d}{d\tau}(P\cdot P) = 2P\cdot\tfrac{dP}{d\tau} = 2P\cdot F = 0$. Writing this in components (with $P = (E,\mathbf{p})$ and $F = (\gamma\mathbf{f}\cdot\mathbf{u}\cdot\text{stuff})$) and simplifying yields $dE/dt = \mathbf{f}\cdot\mathbf{u}$. The deep statement is that the constancy of the rest mass *is* the work–energy theorem: the energy can only change in step with the momentum so as to keep $E^2 - \mathbf{p}^2$ fixed, and "in step" is precisely $dE = \mathbf{u}\cdot d\mathbf{p}$.

For the non-parallelism of acceleration and force, the mechanism is the speed-dependence of $\gamma$. Differentiate $\mathbf{p} = \gamma m\mathbf{u}$:
$$\mathbf{f} = \frac{d}{dt}(\gamma m\mathbf{u}) = \gamma m\,\frac{d\mathbf{u}}{dt} + m\mathbf{u}\,\frac{d\gamma}{dt} = \gamma m\mathbf{a} + m\mathbf{u}\,\gamma^3(\mathbf{a}\cdot\mathbf{u}),$$
using $d\gamma/dt = \gamma^3(\mathbf{u}\cdot\mathbf{a})$ (differentiate $\gamma = (1-u^2)^{-1/2}$). The first term $\gamma m\mathbf{a}$ is along the acceleration; the second $\gamma^3 m(\mathbf{a}\cdot\mathbf{u})\mathbf{u}$ is along the velocity, and it is present whenever the acceleration has a component along the motion (i.e. whenever the speed is changing). So a force at an oblique angle to the velocity produces an acceleration at a *different* oblique angle. The physical reading: changing a particle's *speed* (longitudinal) fights against the $\gamma^3$ growth of energy near $c$, so it is much harder than changing its *direction* (transverse), which only fights the $\gamma$. This anisotropy of inertia is what stops a constant force from ever reaching $c$ — as $u\to c$, $\gamma^3\to\infty$, and the longitudinal inertia diverges.

---

# What Makes This Hard

The non-obvious step is the non-parallelism of acceleration and force: students reflexively write $\mathbf{a} = \mathbf{f}/m$ (or $\mathbf{f}/\gamma m$) and miss the $\gamma^3$ longitudinal term, which only appears when one differentiates $\gamma m\mathbf{u}$ honestly, keeping $d\gamma/dt$. The conceptual hurdle is the factor of $\gamma$ relating the ordinary force $\mathbf{f}$ to the spatial four-force $F^{\text{spatial}} = \gamma\mathbf{f}$ — it is easy to confuse the two and to mis-state which one is "the force". The most common error is to use the Newtonian work–energy theorem $dE_{\text{kin}}/dt = \mathbf{f}\cdot\mathbf{u}$ with the Newtonian kinetic energy $\tfrac12 mu^2$, rather than the relativistic energy $E = \gamma m$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Start from the covariant $F^\mu = dP^\mu/d\tau$, convert proper time to coordinate time with $d/d\tau = \gamma\,d/dt$, read off the spatial part as Newton's law and the temporal part as the work–energy theorem. For the force–acceleration relation, differentiate $\mathbf{p} = \gamma m\mathbf{u}$ keeping $d\gamma/dt = \gamma^3(\mathbf{u}\cdot\mathbf{a})$.

**Subgoal decomposition:**

1. **Convert proper time to coordinate time.** Use $d/d\tau = \gamma\,d/dt$ in $F^\mu = dP^\mu/d\tau$.
   - *Hint:* $dt/d\tau = \gamma$, so the chain rule gives a factor of $\gamma$.
   - *Why needed:* It expresses the law in the observer's clock $t$ rather than the proper time $\tau$.

2. **Read off the spatial part.** The spatial components give $\gamma\,d\mathbf{p}/dt = F^{\text{spatial}} =: \gamma\mathbf{f}$, hence $d\mathbf{p}/dt = \mathbf{f}$.
   - *Hint:* Define the ordinary force $\mathbf{f}$ as the spatial four-force divided by $\gamma$.
   - *Why needed:* It is Newton's second law for the relativistic momentum $\mathbf{p} = \gamma m\mathbf{u}$.

3. **Read off the temporal part.** The time component gives $\gamma\,dE/dt = F^0 = \gamma\mathbf{f}\cdot\mathbf{u}$, hence $dE/dt = \mathbf{f}\cdot\mathbf{u}$.
   - *Hint:* For a pure force use $F\cdot U = 0$ to relate $F^0$ to $\gamma\mathbf{f}\cdot\mathbf{u}$.
   - *Why needed:* It is the work–energy theorem, the power equalling the rate of change of energy.

4. **Differentiate $\mathbf{p} = \gamma m\mathbf{u}$ for the force–acceleration relation.** Use $d\gamma/dt = \gamma^3(\mathbf{u}\cdot\mathbf{a})$.
   - *Hint:* Product rule on $\gamma m\mathbf{u}$; the $d\gamma/dt$ term produces the longitudinal $\gamma^3$ piece.
   - *Why needed:* It exposes the non-parallelism — $\gamma^3 m$ longitudinal, $\gamma m$ transverse.

---

# Lemma Decomposition

> [!note]- Lemma 1: $d\gamma/dt = \gamma^3(\mathbf{u}\cdot\mathbf{a})$
> **Statement:** The time derivative of the Lorentz factor is $d\gamma/dt = \gamma^3\,\mathbf{u}\cdot\mathbf{a}$, where $\mathbf{a} = d\mathbf{u}/dt$.
>
> **Hint:** Differentiate $\gamma = (1 - u^2)^{-1/2}$ with $u^2 = \mathbf{u}\cdot\mathbf{u}$.
>
> **Why needed:** It is the source of the longitudinal $\gamma^3$ term that breaks the parallelism of force and acceleration.
>
> > [!note]- Full proof
> > Write $\gamma = (1 - \mathbf{u}\cdot\mathbf{u})^{-1/2}$. Then
> > $$\frac{d\gamma}{dt} = -\tfrac12(1-u^2)^{-3/2}\cdot\frac{d}{dt}(-\mathbf{u}\cdot\mathbf{u}) = \tfrac12\gamma^3\cdot 2(\mathbf{u}\cdot\mathbf{a}) = \gamma^3(\mathbf{u}\cdot\mathbf{a}),$$
> > using $(1-u^2)^{-3/2} = \gamma^3$ and $\tfrac{d}{dt}(\mathbf{u}\cdot\mathbf{u}) = 2\mathbf{u}\cdot\mathbf{a}$. $\blacksquare$

> [!note]- Lemma 2: The spatial law is $d\mathbf{p}/dt = \mathbf{f}$
> **Statement:** The spatial components of $F^\mu = dP^\mu/d\tau$, with $F^{\text{spatial}} = \gamma\mathbf{f}$, give $d\mathbf{p}/dt = \mathbf{f}$ with $\mathbf{p} = \gamma m\mathbf{u}$.
>
> **Hint:** Use $d/d\tau = \gamma\,d/dt$ and cancel the common factor of $\gamma$.
>
> **Why needed:** It is Newton's second law in relativistic form, the spatial content of the equation of motion.
>
> > [!note]- Full proof
> > The spatial part of $F^\mu = dP^\mu/d\tau$ is $F^{\text{spatial}} = d\mathbf{p}/d\tau = \gamma\,d\mathbf{p}/dt$ (chain rule, $dt/d\tau = \gamma$). Defining the ordinary three-force as $\mathbf{f} := d\mathbf{p}/dt$, this reads $F^{\text{spatial}} = \gamma\mathbf{f}$, i.e. the ordinary force is the spatial four-force divided by $\gamma$. Hence $d\mathbf{p}/dt = \mathbf{f}$ with $\mathbf{p} = \gamma m\mathbf{u}$. $\blacksquare$

> [!note]- Lemma 3: The temporal law is the work–energy theorem $dE/dt = \mathbf{f}\cdot\mathbf{u}$
> **Statement:** The time component of $F^\mu = dP^\mu/d\tau$ gives $dE/dt = \mathbf{f}\cdot\mathbf{u}$ for a pure force.
>
> **Hint:** For a pure force $F\cdot U = 0$; expand this in components.
>
> **Why needed:** It is the relativistic work–energy theorem, the temporal content of the equation of motion.
>
> > [!note]- Full proof
> > For a pure force $F\cdot U = 0$. With $U = \gamma(1,\mathbf{u})$ and $F = (F^0, \gamma\mathbf{f})$, the contraction is $F\cdot U = \gamma F^0 - \gamma^2\mathbf{f}\cdot\mathbf{u} = 0$, giving $F^0 = \gamma\,\mathbf{f}\cdot\mathbf{u}$. The time component of the equation of motion is $F^0 = dE/d\tau = \gamma\,dE/dt$, so $\gamma\,dE/dt = \gamma\,\mathbf{f}\cdot\mathbf{u}$, hence $dE/dt = \mathbf{f}\cdot\mathbf{u}$. (Equivalently, from constancy of $P\cdot P = m^2$: $0 = \tfrac{d}{d\tau}(E^2 - \mathbf{p}^2) = 2\gamma(E\,dE/dt - \mathbf{p}\cdot d\mathbf{p}/dt)$, and with $\mathbf{p} = E\mathbf{u}$ and $d\mathbf{p}/dt = \mathbf{f}$ this gives $dE/dt = \mathbf{u}\cdot\mathbf{f}$.) $\blacksquare$

> [!note]- Lemma 4: The force–acceleration relation $\mathbf{f} = \gamma m\mathbf{a} + \gamma^3 m(\mathbf{a}\cdot\mathbf{u})\mathbf{u}$
> **Statement:** Differentiating $\mathbf{p} = \gamma m\mathbf{u}$ gives $\mathbf{f} = \gamma m\mathbf{a} + \gamma^3 m(\mathbf{a}\cdot\mathbf{u})\mathbf{u}$.
>
> **Hint:** Product rule, using Lemma 1 for $d\gamma/dt$.
>
> **Why needed:** It exhibits the non-parallelism of force and acceleration and the longitudinal/transverse masses.
>
> > [!note]- Full proof
> > For a pure force $m$ is constant, so $\mathbf{f} = d\mathbf{p}/dt = m\,d(\gamma\mathbf{u})/dt = m(\gamma\,d\mathbf{u}/dt + \mathbf{u}\,d\gamma/dt) = m\gamma\mathbf{a} + m\mathbf{u}\,\gamma^3(\mathbf{u}\cdot\mathbf{a})$, using Lemma 1. Resolving $\mathbf{f}$ along $\mathbf{u}$ (longitudinal) and perpendicular to it (transverse): the transverse component is $f_\perp = \gamma m\,a_\perp$, the longitudinal is $f_\parallel = \gamma m\,a_\parallel + \gamma^3 m\,u^2 a_\parallel/u\cdots$; collecting, $f_\parallel = \gamma m a_\parallel(1 + \gamma^2 u^2) = \gamma^3 m\,a_\parallel$ (using $1 + \gamma^2 u^2 = \gamma^2$). So the longitudinal inertia is $\gamma^3 m$ and the transverse inertia is $\gamma m$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Start from the covariant equation of motion $F^\mu = dP^\mu/d\tau$ (the definition of the [[Def - Four-Force|four-force]]), with $P^\mu = (E,\mathbf{p})$, $E = \gamma m$, $\mathbf{p} = \gamma m\mathbf{u}$.
>
> *Spatial part.* By Lemma 2, converting proper time to coordinate time ($d/d\tau = \gamma\,d/dt$) and defining the ordinary force $\mathbf{f} := d\mathbf{p}/dt$ (so the spatial four-force is $\gamma\mathbf{f}$), the spatial components give
> $$\frac{d\mathbf{p}}{dt} = \mathbf{f}, \qquad \mathbf{p} = \gamma m\mathbf{u}.$$
>
> *Temporal part.* By Lemma 3 (using $F\cdot U = 0$ for a pure force, or the constancy of $P\cdot P = m^2$), the time component gives the **work–energy theorem**
> $$\frac{dE}{dt} = \mathbf{f}\cdot\mathbf{u}.$$
>
> *Force and acceleration.* By Lemmas 1 and 4, differentiating $\mathbf{p} = \gamma m\mathbf{u}$ for a pure force gives
> $$\mathbf{f} = \gamma m\,\mathbf{a} + \gamma^3 m\,(\mathbf{a}\cdot\mathbf{u})\,\mathbf{u},$$
> so the response is $\gamma m$ transversely and $\gamma^3 m$ longitudinally, and the acceleration is in general *not* parallel to the force. As $\gamma\to 1$ ($u\ll c$), $\mathbf{f}\to m\mathbf{a}$ and $dE_{\text{kin}}/dt\to\mathbf{f}\cdot\mathbf{u}$ with $E_{\text{kin}}\to\tfrac12 mu^2$, recovering Newtonian mechanics. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Accelerator design — beam stiffness.** The transverse mass $\gamma m$ and longitudinal mass $\gamma^3 m$ determine how a relativistic beam responds to steering (transverse) and accelerating (longitudinal) fields; at the LHC, with $\gamma \sim 7500$, the beam is enormously "stiff" longitudinally, which is why accelerating it to higher energy is so much harder than bending it around the ring. The application uses the force–acceleration relation directly; see [[Ex - The acceleration is not parallel to the force]].

**Plasma physics — relativistic cyclotron frequency.** A charge in a uniform magnetic field moves in a circle, but the cyclotron frequency is $\omega = qB/\gamma m$ (not $qB/m$), because the relevant inertia is the energy-dependent $\gamma m$; the frequency *drops* as the particle is accelerated, which must be compensated in cyclotrons (the synchrocyclotron). The application is the magnetic-force case of the equation of motion, where $\mathbf{f}\cdot\mathbf{u} = 0$ so the energy is constant and only the direction changes.

**General relativity — the geodesic deviation from a force.** In curved spacetime the force-free equation is the geodesic $\nabla_U U = 0$; a four-force deflects the particle off the geodesic, $\nabla_U P = F$, the curved-space generalisation of $dP/d\tau = F$. The application carries the equation of motion into general relativity, where "force" and "curvature" are cleanly separated — gravity is in the connection $\nabla$, genuine forces on the right.

---

# Bridges

- **[[Def - Four-Force]]** — this theorem is the projection of the covariant four-force law $F^\mu = dP^\mu/d\tau$ onto an inertial observer. The orthogonality $F\cdot U = 0$ of a pure force is exactly what makes the temporal component the work–energy theorem and keeps the rest mass constant.

- **[[Def - Four-Momentum and Rest Mass]]** — the relativistic momentum $\mathbf{p} = \gamma m\mathbf{u}$ and energy $E = \gamma m$ that appear here are the spatial and time parts of the four-momentum. The non-parallelism of force and acceleration comes from the speed-dependence of $\gamma$ in $\mathbf{p} = \gamma m\mathbf{u}$.

- **Hyperbolic motion under constant force** — integrating $d\mathbf{p}/dt = \mathbf{f}$ with constant $\mathbf{f}$ gives not constant acceleration but constant *proper* acceleration, the hyperbolic worldline $x^2 - t^2 = 1/a^2$ with $a = f/m$. A constant force in the lab is a constant proper acceleration for the particle, the worldline of a [[Special Relativity XVI — Accelerated Observers|uniformly accelerated observer]]; see [[Ex - A charged particle in a uniform electric field]].

- **The Lorentz force and accelerators** — the one fundamental relativistic force is electromagnetic, $\mathbf{f} = q(\mathbf{E} + \mathbf{u}\times\mathbf{B})$, the spatial part of the [[Def - Four-Force|Lorentz four-force]]. Because it is pure, the rest mass is preserved, and the motion is found by integrating $d\mathbf{p}/dt = q(\mathbf{E} + \mathbf{u}\times\mathbf{B})$ — linear acceleration from $\mathbf{E}$, circular from $\mathbf{B}$. The full theory is [[Special Relativity XXI — The Electromagnetic Field|Special Relativity XXI]].

---

# Unlocked by This

> [!tip] Charged-Particle Motion and Accelerators *(from Electromagnetism)*
> Projected with the Lorentz force $\mathbf{f} = q(\mathbf{E} + \mathbf{u}\times\mathbf{B})$, the equation $d\mathbf{p}/dt = \mathbf{f}$ governs every accelerator: a uniform $\mathbf{E}$ gives hyperbolic (linear-accelerator) motion, a uniform $\mathbf{B}$ gives circular motion at the relativistic cyclotron frequency $\omega = qB/\gamma m$. The longitudinal/transverse mass anisotropy explains why accelerating a beam is harder than steering it. See [[Ex - A charged particle in a uniform electric field]].

> [!tip] Hyperbolic Motion and Accelerated Observers *(from §16)*
> A constant force produces constant *proper* acceleration — the hyperbolic worldline $x^2 - t^2 = 1/a^2$ — not the constant coordinate acceleration of Newton. This is the worldline of a **uniformly accelerated observer**, the carrier of the Rindler horizon and accelerated-frame redshift, developed in [[Special Relativity XVI — Accelerated Observers|Special Relativity XVI]].
