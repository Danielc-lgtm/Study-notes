---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Thm - Conservation of Four-Momentum"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ but restore it explicitly where the dimensional form is more recognisable, using $\eta = \operatorname{diag}(+1,-1,-1,-1)$. A particle of rest mass $m$ has [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu = (E,\mathbf{p})$ relative to a frame, with energy $E = \gamma m$, three-momentum $\mathbf{p} = \gamma m\mathbf{u}$, speed $u = |\mathbf{u}|$, and Lorentz factor $\gamma = (1-u^2)^{-1/2}$. The kinetic energy is $E_{\text{kin}}$. Full registry on [[Special Relativity XIII — Energy and Momentum]].

---

# Statement

> **Mass–energy equivalence.** The total energy of a particle of rest mass $m$, relative to an inertial observer in which it moves with Lorentz factor $\gamma$, is
> $$E \;=\; \gamma m \qquad\big(\text{with } c:\ E = \gamma m c^2\big),$$
> which for a particle **at rest** ($\gamma = 1$) gives the **rest energy**
> $$\boxed{\,E = m c^2\,}.$$
> The energy decomposes as rest energy plus **kinetic energy**,
> $$E = mc^2 + E_{\text{kin}}, \qquad E_{\text{kin}} = (\gamma - 1)mc^2,$$
> which reduces to the Newtonian $\tfrac12 m u^2$ in the limit $u \ll c$. Equivalently, in terms of the momentum, the energy obeys the invariant **energy–momentum relation**
> $$E^2 = \mathbf{p}^2 c^2 + m^2 c^4,$$
> the $\mu$-squared of the mass-shell $P\cdot P = m^2$.

> **Corollary (non-additivity of mass).** The rest mass of a composite system is *not* the sum of its constituents' rest masses: it is the length of the total [[Def - Four-Momentum and Rest Mass|four-momentum]], $M = \sqrt{(\sum P_a)\cdot(\sum P_a)}$, which exceeds $\sum m_a$ when the parts move relative to one another and falls below it by the binding energy when the parts are bound.

---

# Motivation

The four-momentum was built so that its spatial part is the relativistic momentum. This theorem is about the *other* part — the time component — and the question it answers is innocent-looking but turned out to be one of the most consequential in physics: what does $P^0$ mean?

The hint comes from a Taylor expansion. The time component is $P^0 = \gamma m = m(1 - u^2)^{-1/2}$, and expanding in powers of $u$ gives $P^0 = m + \tfrac12 mu^2 + \tfrac{3}{8}mu^4 + \cdots$. The second term is unmistakable: it is the Newtonian kinetic energy. A four-vector whose spatial part is the momentum and whose time part contains the kinetic energy can only be interpreted one way — the time component *is* the energy (this is confirmed rigorously by Noether's theorem: $P^0$ is the conserved charge of time-translation invariance). So $E = \gamma m$. But the expansion has a leading term the Newtonian energy lacks: the constant $m$. A particle at rest, with no kinetic energy at all, still has energy $E = m$ — that is, $E = mc^2$.

This is the whole content, and its importance is not the famous formula but what the formula *permits*. In Newtonian physics mass and energy were separate, separately conserved quantities; here the rest energy $mc^2$ says mass *is* energy, a frozen form of it, and the conservation law that governs energy ([[Thm - Conservation of Four-Momentum|conservation of four-momentum]]) therefore governs mass too — but only in combination, because what is conserved is the four-vector, and mass is its length, not an additive quantity. So mass can be converted into kinetic energy and back. A nucleus that binds releases the binding energy as radiation and ends up *lighter* than its parts; a collision energetic enough creates new massive particles out of kinetic energy. None of this is possible in a world with a separate conservation of mass, and all of it is the practical face of $E = mc^2$.

The third form of the statement, $E^2 = \mathbf{p}^2 + m^2$, is the one most used in calculation. It is obtained without any Taylor expansion, by the cleanest argument in the chapter: evaluate the invariant $P\cdot P$ in the rest frame (where it is $m^2$) and in a general frame (where it is $E^2 - \mathbf{p}^2$) and equate. This relation connects energy and momentum for any particle and degenerates correctly to $E = |\mathbf{p}|$ for a photon ($m = 0$); it is the dispersion relation of every field.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's hypothesis is simply "a particle with a four-momentum", which is universal, so input-broadening here is about recognising *when the rest-energy reading is the relevant one*.

The first disguised source is **"a reaction releases or absorbs energy"** — any process where the kinetic energy of the products differs from that of the reactants. The released energy must come from somewhere, and mass–energy equivalence says it comes from the rest mass: $\Delta E_{\text{kin}} = -\Delta(\text{rest mass})\cdot c^2$. The bridge is conservation of four-momentum, whose energy component balances rest energy against kinetic energy. *Example problem:* computing the energy released in a nuclear reaction from the mass defect, $Q = (m_{\text{initial}} - m_{\text{final}})c^2$.

The second disguised source is **"a composite system whose mass is asked for"** — a bound nucleus, a box of gas, a system of colliding particles. The system's rest mass is *not* the sum of parts; it is the length of the total four-momentum. The bridge is that mass is the Minkowski norm of $\sum P_a$, and the cross terms encode the relative motion and binding. *Example problem:* the invariant mass of two photons, or the mass of a hot gas exceeding that of a cold one ([[Ex - The invariant mass of a system of particles]]).

The third disguised source is **"a particle's energy and momentum are both in play"** — any kinematics problem giving one and needing the other. The energy–momentum relation $E^2 = \mathbf{p}^2 + m^2$ converts between them. The bridge is the mass-shell. *Example problem:* finding a decay product's momentum from its energy, $|\mathbf{p}| = \sqrt{E^2 - m^2}$ ([[Ex - Two-body decay kinematics]]).

**Targets (Output Amplification)**

The conclusions are $E = \gamma m$, $E = mc^2$ at rest, and $E^2 = \mathbf{p}^2 + m^2$.

Combine $E = \gamma m$ with **the divergence of $\gamma$ at $u\to c$**. Since $\gamma\to\infty$ as $u\to c$, the energy required to accelerate a massive particle to the speed of light is infinite. The further result is the speed limit, derived energetically rather than kinematically: no finite energy reaches $u = c$. The combination is useful because it gives a *dynamical* reason for the speed limit (the energy cost), complementing the kinematic one (the light cone). *Example:* explaining why an LHC proton at $7$ TeV has $\gamma = 7500$ yet still moves below $c$ ([[Ex - Rest energy, kinetic energy and the Newtonian limit]]).

Combine $E^2 = \mathbf{p}^2 + m^2$ with **the massless limit $m\to 0$**. The relation degenerates to $E = |\mathbf{p}|$, the photon's energy–momentum relation, recovering the [[Def - The Four-Momentum of a Photon|null four-momentum]] as the $m\to 0$ boundary of the mass shell. The further result is a unified treatment of massive and massless particles in one formula. The combination is nonobvious because "mass times $c^2$" suggests massless particles have no energy, whereas they have $E = |\mathbf{p}|c$. *Example:* photon kinematics in Compton scattering.

Combine the non-additivity corollary with **a bound system**. When the parts are bound, the cross terms in $M^2 = (\sum P_a)^2$ are negative (the binding energy), so $M < \sum m_a$: the bound system is *lighter* than its free constituents. The further result is the **mass defect** that powers nuclear energy — the missing mass is released as binding energy. The combination is nonobvious because it predicts that assembling a nucleus *destroys* mass. *Example:* the helium-4 nucleus weighing $0.7\%$ less than its four constituent nucleons, the energy source of the sun.

---

# Why Is It True

Take the rigorous route first, because it is one line and it is the cleanest argument in the chapter. The Minkowski square $P\cdot P$ is a Lorentz invariant — the same number in every frame. In the particle's *rest* frame, $P = (m, \mathbf{0})$, so $P\cdot P = m^2$. In any other frame, $P = (E,\mathbf{p})$, so $P\cdot P = E^2 - \mathbf{p}^2$. Equating the two values of the same invariant gives $E^2 - \mathbf{p}^2 = m^2$, the energy–momentum relation; setting $\mathbf{p} = 0$ recovers $E = m$ at rest. **The whole theorem is the statement that the rest mass is the length of the four-momentum, computed in the rest frame where the four-momentum is purely energy.**

The conceptual route is the Taylor expansion, and it is the one that makes the physics visible. Why should a particle at rest have energy? Because the energy is the time component of the four-momentum, and the four-momentum of a particle at rest is not zero — it points purely in the time direction, $P = (m, \mathbf{0})$. A particle "at rest in space" is still *moving through time*, at the maximal rate (proper time equals coordinate time for it), and the four-momentum measures that motion through spacetime. The rest energy $m$ is the time-component of the four-momentum of something sitting still in space but advancing through time. The kinetic energy is the *extra* time-component acquired when the particle also moves through space: $\gamma m - m = (\gamma - 1)m$, the difference between the time-component when moving and when still.

That this extra is the kinetic energy is confirmed by its low-speed limit, $(\gamma - 1)m = \tfrac12 mu^2 + O(u^4)$, exactly Newton's kinetic energy. And the constancy of the leading term $m$ — present whether the particle moves or not — is what Newtonian physics missed: it set the zero of energy at "particle at rest", discarding the rest energy as an irrelevant constant. Relativity cannot discard it, because the *zero of energy is no longer free*: the four-momentum is an absolute object, energy is its (observer-dependent) time component, and a particle at rest has a definite, nonzero time component $m$. The rest energy is the part of the energy that Newtonian physics conventionally set to zero, made unavoidable by the geometry.

The non-additivity of mass then follows because mass is a *length* and lengths do not add. For two particles, $M^2 = (P_1 + P_2)\cdot(P_1+P_2) = m_1^2 + m_2^2 + 2P_1\cdot P_2$, and the cross term $2P_1\cdot P_2 = 2(E_1 E_2 - \mathbf{p}_1\cdot\mathbf{p}_2)$ depends on the relative motion. When the parts move apart (positive relative kinetic energy) it raises $M$ above $m_1 + m_2$; when they are bound (negative potential energy) it lowers $M$. Mass is the Minkowski norm of the energy–momentum vector, and "the norm of a sum is not the sum of norms" is the whole story.

---

# What Makes This Hard

The conceptual difficulty is the rest energy itself: it is counterintuitive that a stationary object contains energy, because Newtonian intuition sets the energy of a thing at rest to zero. The non-obvious step in calculations is the non-additivity of mass — most errors come from writing $M = \sum m_a$ for a composite system, forgetting the cross terms $2P_i\cdot P_j$ that encode relative motion and binding. The most common conflation is between the rest energy $mc^2$ (particle at rest) and the total energy $\gamma mc^2$ (particle in motion): writing $E = mc^2$ for a moving particle silently discards its kinetic energy.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
For the energy–momentum relation, evaluate the invariant $P\cdot P$ in the rest frame and a general frame and equate. For the energy interpretation, identify $P^0$ as the energy (its low-speed expansion contains the Newtonian kinetic energy) and read off $E = \gamma m$ and the rest energy at $\gamma = 1$. For non-additivity, expand the square of a sum of four-momenta and isolate the cross terms.

**Subgoal decomposition:**

1. **Identify the time component as the energy.** Expand $P^0 = \gamma m = m + \tfrac12 mu^2 + \cdots$ and recognise the Newtonian kinetic energy.
   - *Hint:* The constant term $m$ is the rest energy; the next term is $\tfrac12 mu^2$.
   - *Why needed:* It establishes $E = \gamma m$ and, at $\gamma = 1$, the rest energy $E = mc^2$.

2. **Derive the energy–momentum relation by invariance.** Compute $P\cdot P$ in the rest frame ($=m^2$) and a general frame ($=E^2 - \mathbf{p}^2$) and equate.
   - *Hint:* $P\cdot P$ is a Lorentz scalar; evaluate it where it is easiest (rest frame).
   - *Why needed:* It gives $E^2 = \mathbf{p}^2 + m^2$ without any Taylor expansion, valid for all $u$ and (at $m=0$) for photons.

3. **Define the kinetic energy.** Set $E_{\text{kin}} = E - mc^2 = (\gamma - 1)mc^2$ and verify the low-speed limit.
   - *Hint:* Subtract the rest energy from the total energy; expand $(\gamma-1)$ for small $u$.
   - *Why needed:* It separates the rest energy (always present) from the motion-dependent part (reduces to Newton).

4. **Establish non-additivity.** Expand $M^2 = (\sum P_a)\cdot(\sum P_a)$ and isolate the cross terms $2\sum_{a<b}P_a\cdot P_b$.
   - *Hint:* $M^2 = \sum m_a^2 + 2\sum_{a<b}P_a\cdot P_b$, and the cross terms depend on relative motion.
   - *Why needed:* It shows mass is the length of the total four-momentum, not the sum of masses — the mass defect and the mass of photon systems.

---

# Lemma Decomposition

> [!note]- Lemma 1: The energy is the time component, $E = \gamma m$
> **Statement:** The conserved energy of a particle relative to an inertial frame is $P^0 = \gamma m$, whose low-speed expansion is $m + \tfrac12 m u^2 + O(u^4)$.
>
> **Hint:** Expand $\gamma = (1-u^2)^{-1/2}$ in powers of $u$.
>
> **Why needed:** It identifies $P^0$ with the energy and exhibits the rest energy $m$ and the Newtonian kinetic energy $\tfrac12 mu^2$.
>
> > [!note]- Full proof
> > The four-momentum is $P^\mu = \gamma m(1,\mathbf{u})$, so $P^0 = \gamma m$. Expanding $\gamma = (1-u^2)^{-1/2} = 1 + \tfrac12 u^2 + \tfrac38 u^4 + \cdots$ gives
> > $$P^0 = \gamma m = m + \tfrac12 m u^2 + \tfrac38 m u^4 + \cdots.$$
> > The second term $\tfrac12 m u^2$ is the Newtonian kinetic energy; together with the conservation of $P^0$ (Noether charge of time-translation invariance), this identifies $P^0 = E$ as the energy. With $c$ restored, $E = \gamma m c^2 = mc^2 + \tfrac12 mu^2 + \cdots$. At $u = 0$, $E = mc^2$, the rest energy. $\blacksquare$

> [!note]- Lemma 2: The energy–momentum relation $E^2 = \mathbf{p}^2 + m^2$
> **Statement:** For any particle, $E^2 - \mathbf{p}^2 = m^2$ (with $c$: $E^2 = \mathbf{p}^2c^2 + m^2c^4$), and for a photon ($m=0$), $E = |\mathbf{p}|$.
>
> **Hint:** Evaluate the invariant $P\cdot P$ in the rest frame and in a general frame.
>
> **Why needed:** It is the relation connecting energy and momentum, used in every dispersion calculation, and it includes the massless case.
>
> > [!note]- Full proof
> > The Minkowski square $P\cdot P$ is a Lorentz invariant. In the rest frame $P = (m,\mathbf{0})$, so $P\cdot P = m^2$. In a general frame $P = (E,\mathbf{p})$, so $P\cdot P = E^2 - \mathbf{p}^2$. Equating, $E^2 - \mathbf{p}^2 = m^2$, i.e. $E^2 = \mathbf{p}^2 + m^2$. Restoring $c$: $E^2 = \mathbf{p}^2 c^2 + m^2 c^4$. For a massless particle $m = 0$, giving $E = |\mathbf{p}|c$ — the photon's [[Def - The Four-Momentum of a Photon|null]] energy–momentum relation. (A photon has no rest frame, so the rest-frame step is replaced by the null condition $P\cdot P = 0$ directly.) $\blacksquare$

> [!note]- Lemma 3: The mass of a system is the length of the total four-momentum, not the sum of masses
> **Statement:** For a system of particles, $M^2 = (\sum_a P_a)\cdot(\sum_a P_a) = \sum_a m_a^2 + 2\sum_{a<b}P_a\cdot P_b$, and $M \ne \sum_a m_a$ in general.
>
> **Hint:** Expand the Minkowski square of the sum and use $P_a\cdot P_a = m_a^2$.
>
> **Why needed:** It is the non-additivity corollary — the mass defect of bound systems and the nonzero mass of photon systems.
>
> > [!note]- Full proof
> > Let $P = \sum_a P_a$ be the total four-momentum. Then
> > $$M^2 = P\cdot P = \Big(\sum_a P_a\Big)\cdot\Big(\sum_b P_b\Big) = \sum_a P_a\cdot P_a + 2\sum_{a<b}P_a\cdot P_b = \sum_a m_a^2 + 2\sum_{a<b}P_a\cdot P_b,$$
> > using $P_a\cdot P_a = m_a^2$ (or $0$ for a photon). Each cross term is $P_a\cdot P_b = E_a E_b - \mathbf{p}_a\cdot\mathbf{p}_b$, which depends on the relative motion of the two particles. For two massive particles at relative rest the cross term is $m_a m_b$ and $M = m_a + m_b$; for particles in relative motion $P_a\cdot P_b > m_a m_b$ (by the reversed Cauchy–Schwarz inequality for future-timelike vectors) so $M > \sum m_a$; for bound particles the (negative) interaction energy lowers $M$ below $\sum m_a$. In particular two photons in different directions have $M^2 = 2P_1\cdot P_2 = 2E_1 E_2(1-\cos\theta) > 0$ despite $m_1 = m_2 = 0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{P}$ be a particle of rest mass $m$ with four-momentum $P^\mu = mU^\mu = \gamma m(1,\mathbf{u}) = (E,\mathbf{p})$ relative to an inertial frame, so $E = \gamma m$ and $\mathbf{p} = \gamma m\mathbf{u}$.
>
> *Energy and rest energy.* By Lemma 1, the time component $P^0 = \gamma m$ is the energy (its low-speed expansion $m + \tfrac12 mu^2 + \cdots$ contains the Newtonian kinetic energy, and it is the conserved charge of time-translation invariance). Thus $E = \gamma m$, and at rest ($\gamma = 1$) the **rest energy** is $E = m$, i.e. $E = mc^2$ with $c$ restored.
>
> *Kinetic energy.* Define $E_{\text{kin}} := E - mc^2 = (\gamma - 1)mc^2$. Expanding, $E_{\text{kin}} = \tfrac12 mu^2 + \tfrac38 m u^4 c^{-2} + \cdots \to \tfrac12 mu^2$ as $u\ll c$, recovering the Newtonian kinetic energy.
>
> *Energy–momentum relation.* By Lemma 2, evaluating the invariant $P\cdot P$ in the rest frame ($=m^2$) and the general frame ($= E^2 - \mathbf{p}^2$) and equating gives $E^2 = \mathbf{p}^2 + m^2$ (with $c$: $E^2 = \mathbf{p}^2c^2 + m^2c^4$), reducing to $E = |\mathbf{p}|c$ for $m = 0$.
>
> *Non-additivity of mass.* By Lemma 3, the rest mass of a system is $M = \sqrt{(\sum_a P_a)\cdot(\sum_a P_a)} = \sqrt{\sum_a m_a^2 + 2\sum_{a<b}P_a\cdot P_b}$, which exceeds $\sum_a m_a$ for parts in relative motion and falls below it (by the binding energy) for bound parts; in particular a system of massless particles in different directions has nonzero mass. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Stellar and nuclear energy — the mass defect.** In the proton–proton chain that powers the sun, four protons fuse (via intermediate steps) into a helium-4 nucleus whose rest mass is about $0.7\%$ less than the four protons'; that $0.7\%$ of $mc^2$ is radiated. Computing the energy yield is a direct application of $E = mc^2$ to the mass defect, with conservation of four-momentum doing the bookkeeping. The application is out-of-distribution because it derives an astrophysical luminosity from a particle-physics mass difference; the technique is the invariant-mass calculation of [[Ex - The invariant mass of a system of particles]].

**Cosmology — radiation has pressure $p = \rho/3$.** A gas of photons has energy density $\rho$, and because every photon is massless with $E = |\mathbf{p}|$, the momentum flux gives an equation of state $p = \rho/3$. Mass–energy equivalence (energy gravitates) is why radiation curves spacetime in the early universe and why the radiation-dominated era expands differently from the matter-dominated era. The application connects $E = mc^2$ to general-relativistic cosmology.

**Particle physics — the invariant mass peak.** When a heavy particle decays, $X \to a + b$, the invariant mass $M^2 = (P_a + P_b)^2$ reconstructed from the products' four-momenta peaks at $m_X^2$ — this is how the Higgs boson was discovered, as a bump in the invariant-mass spectrum of photon pairs at $125$ GeV. The application uses the non-additivity corollary in reverse: the products' four-momenta sum to a four-momentum whose length is the parent's mass. See [[Ex - Two-body decay kinematics]].

---

# Bridges

- **[[Def - Four-Momentum and Rest Mass]]** — mass–energy equivalence is the reading of the four-momentum's time component. The mass-shell $P\cdot P = m^2$ of the definition, evaluated in the rest frame, *is* the energy–momentum relation, and the rest energy $mc^2$ is the time component there. This theorem is what gives the four-momentum's components their physical names.

- **[[Thm - Conservation of Four-Momentum]]** — conservation is what makes mass–energy equivalence operative. Because the conserved object is the four-vector and mass is its length, mass can convert to kinetic energy and back within the constraint that $\sum P$ is fixed; the energy released in a reaction is the mass defect, $Q = -\Delta(\text{rest mass})c^2$. Without conservation, $E = mc^2$ would be inert.

- **[[Def - The Four-Momentum of a Photon]]** — the energy–momentum relation $E^2 = \mathbf{p}^2 + m^2$ degenerates at $m = 0$ to the photon's $E = |\mathbf{p}|c$, so the massless particle is the boundary case of mass–energy equivalence. A photon has energy and momentum but no rest energy, because its mass-shell is the light cone.

- **Binding energy and the Cauchy–Schwarz inequality** — the non-additivity of mass rests on the *reversed* Cauchy–Schwarz inequality for future-timelike four-vectors, $P_a\cdot P_b \ge m_a m_b$, with equality only when $P_a \parallel P_b$. This is the same inequality behind the [[Thm - Inertial Worldlines Maximise Proper Time|reversed triangle inequality]], and it is why a system of particles in relative motion always weighs more than the sum of its parts, while binding (negative interaction energy) is what allows bound systems to weigh less.

---

# Unlocked by This

> [!tip] Nuclear and Particle Physics *(from Applied Physics)*
> Mass–energy equivalence is the energy source of stars, reactors, and weapons: the **mass defect** of a bound nucleus is released as binding energy, and the smallness of the fractional defect ($\sim 0.7\%$ for fusion) hides the enormousness of $c^2$ ($9\times10^{13}$ J per gram). In particle physics, kinetic energy is converted into the rest mass of new particles — the way particles are discovered — bounded by the [[Thm - Inelastic Collisions and Particle Production|production threshold]].

> [!tip] The Energy of Gravity *(from General Relativity)*
> Because energy and mass are equivalent, *all* energy gravitates — not just rest mass but kinetic energy, binding energy, and field energy. This is why the source of gravity in general relativity is the full **energy–momentum tensor** $T^{\mu\nu}$, not merely a mass density: pressure, stress, and energy flux all curve spacetime. The rest energy $mc^2$ of ordinary matter is the dominant term, but radiation pressure and field energy contribute, which matters in stars, the early universe, and near black holes.
