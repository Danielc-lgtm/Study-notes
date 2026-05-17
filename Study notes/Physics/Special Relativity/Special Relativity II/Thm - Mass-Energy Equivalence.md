---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

Natural units, $c = 1$, with $c$ restored where the Newtonian limit is the point. A particle has [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu = (E/c,\mathbf{p})$, rest mass $m$, speed $u$, Lorentz factor $\gamma = (1-u^2/c^2)^{-1/2}$. The Minkowski inner product is $A\cdot B = A^0B^0 - \mathbf{A}\cdot\mathbf{B}$. Kinetic energy is $T = E - mc^2$. The full registry is on [[Special Relativity II — Relativistic Kinematics and Dynamics]].

---

# Statement

> **Mass–energy equivalence.** The total energy of a particle of [[Def - Four-Momentum and Rest Mass|rest mass]] $m$ moving at speed $u$ is
> $$E \;=\; \gamma m c^2 \;=\; \frac{mc^2}{\sqrt{1 - u^2/c^2}}.$$
> Expanding in powers of $u/c$,
> $$E \;=\; mc^2 \;+\; \tfrac12 m u^2 \;+\; \tfrac38\,\frac{m u^4}{c^2} \;+\; \cdots,$$
> so the energy is the sum of a velocity-independent **rest energy** $mc^2$, the Newtonian kinetic energy $\tfrac12 mu^2$, and relativistic corrections. In particular a particle **at rest** has energy
> $$E \;=\; m c^2,$$
> and the [[Def - Four-Momentum and Rest Mass|four-momentum]] obeys the **energy–momentum relation**, obtained from the invariant $P\cdot P = m^2c^2$:
> $$E^2 \;=\; \mathbf{p}^2 c^2 \;+\; m^2 c^4.$$
> Consequently the rest mass of a composite system is **not** the sum of the rest masses of its constituents: it includes their kinetic energies and binding energies divided by $c^2$, and mass can be converted into kinetic energy and back.

---

# Motivation

Before relativity, mass and energy were utterly different things. Mass was the amount of matter in a body, conserved absolutely; energy came in kinds — kinetic, potential, thermal — that could convert into one another but never into mass. A chemistry experiment weighed the same before and after a reaction to the precision of any balance. The two were tracked by two separate conservation laws.

The question this theorem answers is: **what is the time component of the four-momentum?** [[Def - Four-Momentum and Rest Mass|The four-momentum]] $P^\mu = mU^\mu$ was built so that its spatial part $\mathbf{p} = \gamma m\mathbf{u}$ generalises the Newtonian momentum. But a four-vector has four components, and the time component $P^0 = \gamma mc$ has so far been unnamed. What physical quantity is it? The answer, and the reason it deserves to be called *energy*, is what makes this the most consequential single result in the topic.

The clue is to do what one always does with an unfamiliar relativistic expression: expand it for small $u/c$ and see what familiar physics appears. The expansion of $\gamma mc^2$ produces, as its second term, *exactly* the Newtonian kinetic energy $\tfrac12 mu^2$. So the time component of $P^\mu$, up to the constant $mc^2$, *is* the kinetic energy at low speed. Since the spatial components of $P^\mu$ are conserved (that is what four-momentum conservation says) and they are the relativistic momentum, the time component is conserved too — and a conserved quantity that reduces to kinetic energy can only be the total energy. The unnamed component is the energy.

But the expansion contains more than the kinetic term. It contains a *constant*, $mc^2$, present even when the particle does not move. A particle at rest, with no kinetic energy of any kind, still carries energy $mc^2$. This is the genuinely new physics: **mass is a form of energy.** The two nineteenth-century conservation laws — of mass and of energy — were not independent after all; they are the time component of the single law of [[Thm - Conservation of Four-Momentum|four-momentum conservation]], and mass can be spent as kinetic energy just as potential energy can. A theorem about Taylor-expanding a $\gamma$ factor turns out to license nuclear power, the energy of the stars, and the bomb.

---

# Sources and Targets

**Sources (Input Broadening)**

The result $E = \gamma mc^2$ and the relation $E^2 = \mathbf{p}^2c^2 + m^2c^4$ apply whenever a particle has a [[Def - Four-Momentum and Rest Mass|four-momentum]] — which is to say, always. The skill is recognising the *disguised* situations where the rest-energy content, not just the formula, is the operative fact.

The first disguised source is **a bound system whose binding energy is known.** Property $B$: a composite object — a nucleus, an atom, a molecule — held together with binding energy $E_b$ (the energy needed to separate its parts to rest at infinity). The bridge: the bound system at rest has total energy equal to the sum of its constituents' rest energies *minus* $E_b$; since its energy at rest *is* its rest mass times $c^2$, the bound system's mass is $M = \sum m_i - E_b/c^2$. The non-obviousness: a stable nucleus weighs measurably *less* than its free protons and neutrons, and the mass deficit *is* the binding energy. *Example:* the mass defect of the helium-4 nucleus, which powers the Sun.

The second disguised source is **a process that changes the total kinetic energy.** Property $B$: an inelastic collision, an absorption, an excitation — anything where kinetic energy appears or disappears. The bridge: by [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] the total energy is fixed, so any kinetic energy that vanishes must reappear as rest energy, i.e. as an increase in the total rest mass of the products. The non-obviousness: a perfectly inelastic collision of two equal masses produces an object *heavier* than the sum $2m$, the excess being the lost kinetic energy over $c^2$. *Example:* a hot brick weighs more than a cold one.

The third disguised source is **a system in the centre-of-momentum frame.** Property $B$: a collection of particles whose total three-momentum vanishes. The bridge: in that frame the total four-momentum is purely temporal, $(E_{\text{tot}}/c,\mathbf{0})$, and its invariant square is $E_{\text{tot}}^2/c^2$; this is the *invariant mass squared* of the whole system, $M^2c^2$. The non-obviousness: the invariant mass of a multi-particle system is read off as its total energy in the centre-of-momentum frame, and that energy includes every particle's kinetic energy. *Example:* the rest mass of a box of gas exceeds the sum of the molecules' masses by the thermal energy.

**Targets (Output Amplification)**

The conclusions are $E = \gamma mc^2$, the rest energy $mc^2$, and the relation $E^2 = \mathbf{p}^2c^2 + m^2c^4$.

Combine the relation with **the goal of eliminating an unknown speed.** Property $D$: a problem gives a particle's energy and asks for its momentum, or vice versa, with the speed $u$ a nuisance variable. The amplified result $E$: $E^2 = \mathbf{p}^2c^2 + m^2c^4$ connects energy and momentum *directly*, with no $u$ and no $\gamma$ in sight. This is why the relation, not the formula $E = \gamma mc^2$, is the workhorse of collision problems — it is algebraic in the quantities one actually wants.

Combine the rest-energy statement with **conservation of four-momentum across a decay or reaction.** Property $D$: a process $A\to B + C$ with the masses given. The amplified result $E$: the reaction releases kinetic energy $Q = (m_A - m_B - m_C)c^2$, the **$Q$-value**, positive exactly when the parent is heavier than the products; this is the energy budget of every decay and every nuclear reaction. The combination converts a table of masses into an energy yield.

Combine the relation with **the massless limit $m\to 0$.** Property $D$: a particle whose rest mass is zero or negligible. The amplified result $E$: $E^2 = \mathbf{p}^2c^2 + m^2c^4$ collapses to $E = |\mathbf{p}|c$, the [[Def - The Four-Momentum of a Photon|photon's energy–momentum relation]]. The single relation thus covers massive and massless particles uniformly, with the photon as the boundary case $m = 0$.

---

# Why Is It True

The result should feel inevitable once you accept two things: that the four-momentum is a four-vector, and that conservation laws come from symmetries.

Start with the four-vector fact. [[Def - Four-Momentum and Rest Mass|The four-momentum]] $P^\mu = mU^\mu$ is a genuine four-vector, so its four components stand or fall together — they transform into each other under boosts and they are conserved together or not at all. We *know* the spatial three components are physically meaningful and conserved: they are the relativistic momentum, the thing that reduces to $m\mathbf{u}$ and is conserved in collisions. A four-vector cannot have three conserved components and one meaningless fourth. So the time component $P^0$ must also be a conserved physical quantity. The only question is *which* quantity, and the low-speed expansion answers it: $cP^0 = \gamma mc^2 = mc^2 + \tfrac12 mu^2 + \cdots$, whose velocity-dependent part is the kinetic energy. A conserved scalar that equals kinetic energy at low speed (up to an additive constant) is the energy. So $cP^0 = E$ is forced — not by a new postulate, but by the four-vector structure plus the identification of the spatial part.

Now the rest-energy term. Why is there a constant $mc^2$ at all, rather than an expansion that simply starts at $\tfrac12 mu^2$? Because $E$ is the time component of a four-vector, and the time component of a *timelike* four-vector cannot vanish. The four-momentum has fixed Minkowski length $P\cdot P = m^2c^2 > 0$; the shortest its time component can be — achieved when the spatial part is zero, i.e. at rest — is $E = mc^2$. The rest energy is the *minimum* of the energy, the value forced by the four-momentum having a nonzero invariant length. Geometrically: the four-momentum lives on a hyperboloid $E^2 - \mathbf{p}^2c^2 = m^2c^4$, and the hyperboloid does not pass through the origin — its vertex is at $E = mc^2$, $\mathbf{p}=0$. A massive particle cannot have zero energy because its four-momentum cannot be the zero vector.

Finally the non-additivity of mass. The total four-momentum of a system is the *sum* $\sum P_i^\mu$, because four-momenta add (that is conservation). But the mass is the Minkowski *length* of that sum, $M^2c^2 = (\sum P_i)\cdot(\sum P_i)$, and the length of a sum of vectors is not the sum of their lengths. Expanding, $(\sum P_i)\cdot(\sum P_i) = \sum_i P_i\cdot P_i + 2\sum_{i<j}P_i\cdot P_j = \sum m_i^2c^2 + 2\sum_{i<j}P_i\cdot P_j$, and the cross terms $P_i\cdot P_j$ depend on the relative motion of the particles. They are positive for particles in relative motion, so a collection of moving particles has more invariant mass than the sum of their rest masses. This is not a paradox — it is the elementary geometric fact that $|\mathbf{a}+\mathbf{b}|\ne|\mathbf{a}|+|\mathbf{b}|$, applied to four-vectors. Mass is a length, lengths do not add, and that is the whole of "mass is not additive".

---

# What Makes This Hard

The non-obvious step is the *interpretation*, not the algebra: the Taylor expansion of $\gamma mc^2$ is a one-line computation, but recognising that the time component of a four-vector *must* be a conserved energy because its spatial partners are conserved momenta — that is the conceptual leap. The most common error is to read the rest energy $mc^2$ as the *total* energy of a moving particle, conflating $E = mc^2$ (rest) with $E = \gamma mc^2$ (in motion). The second frequent error is to assume rest mass is additive: students compute the mass of a composite system as $\sum m_i$, forgetting that mass is the length of the summed four-momentum and that the cross terms $2P_i\cdot P_j$ contribute kinetic and binding energy.

---

# Rederivation Scaffold

**High-level strategy:**
The energy is the time component of the four-momentum; identify it by Taylor-expanding, and obtain the energy–momentum relation by evaluating the invariant $P\cdot P$ in two ways.

**Subgoal decomposition:**

1. **Write the time component of the four-momentum.** From $P^\mu = mU^\mu = m\gamma(c,\mathbf{u})$, the time component is $P^0 = \gamma mc$.
   - *Hint:* The four-velocity is $\gamma(c,\mathbf{u})$; the four-momentum is $m$ times it.
   - *Why needed:* This is the quantity to be interpreted.

2. **Expand $\gamma mc^2$ for small $u/c$.** Use $\gamma = (1-u^2/c^2)^{-1/2} = 1 + \tfrac12 u^2/c^2 + \tfrac38 u^4/c^4 + \cdots$.
   - *Hint:* Binomial series for $(1-x)^{-1/2}$ with $x = u^2/c^2$.
   - *Why needed:* The second term is the Newtonian kinetic energy, identifying $cP^0$ as the energy; the first term is the rest energy.

3. **Read off the rest energy.** Set $u = 0$: $E = mc^2$.
   - *Hint:* The zeroth-order term of the expansion is velocity-independent.
   - *Why needed:* This is the mass–energy equivalence proper.

4. **Derive the energy–momentum relation.** Evaluate the Lorentz invariant $P\cdot P$ in the rest frame and in a general frame, and equate.
   - *Hint:* In the rest frame $P^\mu = (mc,\mathbf{0})$ so $P\cdot P = m^2c^2$; in a general frame $P\cdot P = E^2/c^2 - \mathbf{p}^2$.
   - *Why needed:* Equating gives $E^2 = \mathbf{p}^2c^2 + m^2c^4$, the form used in all collision problems.

5. **Deduce non-additivity of mass.** For a system, $M^2c^2 = (\sum P_i)\cdot(\sum P_i) = \sum m_i^2c^2 + 2\sum_{i<j}P_i\cdot P_j$.
   - *Hint:* Expand the square of a sum; the cross terms are nonzero.
   - *Why needed:* Shows mass is the length of the total four-momentum, not the sum of lengths.

---

# Lemma Decomposition

> [!note]- Lemma 1: The low-speed expansion of the energy
> **Statement:** $E = \gamma mc^2 = mc^2 + \tfrac12 mu^2 + \tfrac38 mu^4/c^2 + O(u^6/c^4)$.
>
> **Hint:** Binomial expansion of $(1 - u^2/c^2)^{-1/2}$.
>
> **Why needed:** The $\tfrac12 mu^2$ term identifies $cP^0$ as the energy; the $mc^2$ term is the rest energy.
>
> > [!note]- Full proof
> > Write $x = u^2/c^2$. The binomial series gives $(1-x)^{-1/2} = 1 + \tfrac12 x + \tfrac{1}{2}\cdot\tfrac{3}{2}\cdot\tfrac{1}{2!}x^2 + \cdots = 1 + \tfrac12 x + \tfrac38 x^2 + \cdots$, valid for $|x| < 1$, i.e. $u < c$. Hence
> > $$\gamma = 1 + \tfrac12\frac{u^2}{c^2} + \tfrac38\frac{u^4}{c^4} + \cdots,$$
> > and multiplying by $mc^2$:
> > $$E = \gamma mc^2 = mc^2 + \tfrac12 mu^2 + \tfrac38\frac{mu^4}{c^2} + \cdots.$$
> > The first term is velocity-independent (the rest energy), the second is precisely the Newtonian kinetic energy $\tfrac12 mu^2$, and the rest are relativistic corrections, suppressed by powers of $u^2/c^2$. $\square$

> [!note]- Lemma 2: The energy–momentum relation from the invariant
> **Statement:** $E^2 = \mathbf{p}^2c^2 + m^2c^4$.
>
> **Hint:** $P\cdot P$ is a Lorentz invariant; compute it in the rest frame and in a general frame.
>
> **Why needed:** It is the algebraic relation between $E$ and $\mathbf{p}$ used in every collision and decay problem, free of $u$ and $\gamma$.
>
> > [!note]- Full proof
> > The four-momentum is $P^\mu = (E/c,\mathbf{p})$, and $P\cdot P = \eta_{\mu\nu}P^\mu P^\nu = (E/c)^2 - \mathbf{p}^2$ is a Lorentz scalar — the same number in every inertial frame. Evaluate it in the particle's **rest frame**, where $\mathbf{u}=0$, $\gamma=1$, so $P^\mu = (mc,\mathbf{0})$ and
> > $$P\cdot P = (mc)^2 - 0 = m^2c^2.$$
> > Now evaluate it in a **general frame**, where $P^\mu = (E/c,\mathbf{p})$:
> > $$P\cdot P = \frac{E^2}{c^2} - \mathbf{p}^2.$$
> > Since $P\cdot P$ is invariant, the two expressions are equal:
> > $$\frac{E^2}{c^2} - \mathbf{p}^2 = m^2c^2 \;\Longrightarrow\; E^2 = \mathbf{p}^2c^2 + m^2c^4. \qquad\square$$
> > (One could instead substitute $E = \gamma mc^2$, $\mathbf{p} = \gamma m\mathbf{u}$ and grind through the algebra; the invariant route is shorter precisely because it exploits that $P\cdot P$ may be computed in the easiest frame.)

> [!note]- Lemma 3: Rest mass is not additive
> **Statement:** For a system of particles with total four-momentum $P_{\text{tot}}^\mu = \sum_i P_i^\mu$, the invariant mass $M$ defined by $P_{\text{tot}}\cdot P_{\text{tot}} = M^2c^2$ satisfies $M \neq \sum_i m_i$ in general.
>
> **Hint:** Expand the Minkowski square of the sum.
>
> **Why needed:** It is the precise statement that mass is the length of the total four-momentum, and the source of binding-energy and mass-defect phenomena.
>
> > [!note]- Full proof
> > By definition $M^2c^2 = P_{\text{tot}}\cdot P_{\text{tot}} = \big(\sum_i P_i\big)\cdot\big(\sum_j P_j\big)$. Expanding the Minkowski inner product of the sum,
> > $$M^2c^2 = \sum_i P_i\cdot P_i + 2\sum_{i<j}P_i\cdot P_j = \sum_i m_i^2c^2 + 2\sum_{i<j}P_i\cdot P_j,$$
> > using $P_i\cdot P_i = m_i^2c^2$ for each particle. The cross terms $P_i\cdot P_j$ are not zero: for two particles with four-momenta $(E_i/c,\mathbf{p}_i)$ and $(E_j/c,\mathbf{p}_j)$, $P_i\cdot P_j = E_iE_j/c^2 - \mathbf{p}_i\cdot\mathbf{p}_j$, which depends on their relative motion. For particles at rest relative to each other this exceeds $m_im_jc^2$ only by... in general $P_i\cdot P_j \ge m_im_jc^2$ for two future-pointing timelike four-momenta, with equality only when the particles are mutually at rest. Hence
> > $$M^2c^2 = \sum_i m_i^2c^2 + 2\sum_{i<j}P_i\cdot P_j \;\ge\; \sum_i m_i^2c^2 + 2\sum_{i<j}m_im_jc^2 = \Big(\sum_i m_i\Big)^2c^2,$$
> > so $M \ge \sum m_i$ for free particles, with equality only when they are all mutually at rest. (Binding *lowers* the energy and so can make a bound system lighter than $\sum m_i$ — the cross terms are then evaluated for the interacting, not free, configuration.) Either way $M\neq\sum m_i$ in general: mass is the length of the total four-momentum, and the length of a sum is not the sum of lengths. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Let a particle have [[Def - Four-Momentum and Rest Mass|rest mass]] $m$, speed $u$, and four-momentum $P^\mu = mU^\mu = m\gamma(c,\mathbf{u})$ with $\gamma = (1-u^2/c^2)^{-1/2}$.
>
> **The energy.** The time component is $P^0 = \gamma mc$, and we define the total energy by $E = cP^0 = \gamma mc^2$. By **Lemma 1**, the binomial expansion gives
> $$E = \gamma mc^2 = mc^2 + \tfrac12 mu^2 + \tfrac38 mu^4/c^2 + \cdots.$$
> The velocity-dependent terms reduce, at leading order, to the Newtonian kinetic energy $\tfrac12 mu^2$; since the spatial components of $P^\mu$ are the conserved relativistic momentum, and a four-vector's components are conserved together, $cP^0$ is a conserved quantity reducing to kinetic energy at low speed — hence it is the total energy. Setting $u = 0$ leaves the velocity-independent **rest energy**
> $$E = mc^2.$$
>
> **The energy–momentum relation.** By **Lemma 2**, evaluating the Lorentz invariant $P\cdot P$ in the rest frame ($= m^2c^2$) and in a general frame ($= E^2/c^2 - \mathbf{p}^2$) and equating,
> $$E^2 = \mathbf{p}^2c^2 + m^2c^4.$$
>
> **Non-additivity.** By **Lemma 3**, for a system of particles the invariant mass $M$ defined through $P_{\text{tot}}\cdot P_{\text{tot}} = M^2c^2$ satisfies
> $$M^2c^2 = \sum_i m_i^2c^2 + 2\sum_{i<j}P_i\cdot P_j \;\neq\; \Big(\sum_i m_i\Big)^2c^2$$
> in general, the cross terms encoding relative kinetic energy and (for interacting systems) binding energy. Mass is therefore the Minkowski length of the total four-momentum, not the sum of constituent masses, and energy may be exchanged between the rest-mass and kinetic forms. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Nuclear binding and the mass defect.** The helium-4 nucleus has rest mass about $0.7\%$ less than the sum of the masses of its two protons and two neutrons. By Lemma 3 applied to a *bound* (interacting) system, this mass defect *is* the binding energy divided by $c^2$. Computing the energy released when four protons fuse to helium — the proton–proton chain — is a direct application: the released energy is $\Delta m\,c^2$, and it is what powers the Sun. The application is nonobvious because "mass" and "energy released" seem like different categories until the theorem identifies them.

**The mass of a hot body.** A box of gas at temperature $T$ has more invariant mass than the same box at absolute zero, by the total thermal kinetic energy of its molecules over $c^2$ (Lemma 3, cross terms from molecular motion). A charged capacitor is heavier than an uncharged one by the field energy over $c^2$; a compressed spring is heavier than a relaxed one. The application battle-tests the rest-energy concept: *any* form of internal energy contributes to the rest mass of a system, not just rest masses of particles.

**Threshold energy via invariant mass.** In a collision producing new particles, the minimum (threshold) energy is set by requiring the invariant mass of the system to reach the total rest mass of the products. Since the invariant mass is computed as $(\sum P)\cdot(\sum P)$ — a Lorentz scalar — one evaluates it in the lab frame and in the centre-of-momentum frame and equates. This is exactly the method of [[Ex - Threshold energy for particle production]], and it is a pure consequence of Lemma 2 and Lemma 3.

---

# Bridges

- **[[Thm - Conservation of Four-Momentum]]** — the partner theorem. Mass–energy equivalence identifies the time component of $P^\mu$ as the energy; conservation of four-momentum says the whole vector, energy included, is conserved. Together they replace the two Newtonian laws of mass conservation and energy conservation by one.

- **[[Def - The Four-Momentum of a Photon]]** — the massless boundary case. Setting $m = 0$ in $E^2 = \mathbf{p}^2c^2 + m^2c^4$ gives $E = |\mathbf{p}|c$, the photon's energy–momentum relation.

- **[[Def - Four-Momentum and Rest Mass]]** — the source. Mass–energy equivalence is the interpretation of the four-momentum's time component and the unpacking of its invariant length $P\cdot P = m^2c^2$.

- **The energy–momentum tensor** *(General Relativity)* — for a continuum, the rest energy density $\rho$ is the $T^{00}$ component of the energy–momentum tensor, and its conservation generalises this theorem to fields. The mass–energy of all forms of matter is the source of spacetime curvature.

---

# Unlocked by This

> [!tip] Nuclear and Particle Physics *(from this topic and downstream)*
> The $Q$-value of a reaction, $Q = (\sum m_{\text{in}} - \sum m_{\text{out}})c^2$, is the kinetic energy released, and it is positive exactly when the reaction is energetically allowed. Fission, fusion, radioactive decay, and the entire chart of the nuclides are bookkeeping with $E = mc^2$.

> [!tip] The Stress–Energy Tensor and Gravitation *(from General Relativity)*
> Because mass and energy are the same, *all* energy — kinetic, thermal, electromagnetic, even pressure — gravitates. The source of gravity in Einstein's field equations is the **energy–momentum tensor** $T^{\mu\nu}$, not mass density alone, and this theorem is why.
