---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Four-Vector"
  - "Def - The Lorentz Transformation"
  - "Thm - Mass-Energy Equivalence"
tags: [physics, special-relativity]
---

# Notation

Natural units, $c = 1$, with $c$ restored where the Newtonian limit is the point. Particle $i$ has [[Def - Four-Momentum and Rest Mass|four-momentum]] $P_i^\mu = (E_i/c,\mathbf{p}_i)$, rest mass $m_i$, speed $u_i$, Lorentz factor $\gamma_i$. The Minkowski inner product is $A\cdot B = A^0B^0 - \mathbf{A}\cdot\mathbf{B}$; a Lorentz transformation is $\Lambda^\mu{}_\nu$. The full registry is on [[Special Relativity II — Relativistic Kinematics and Dynamics]].

---

# Statement

> **Conservation of four-momentum.** Consider any physical process in which a set of particles interact in the **absence of external forces** — a collision, a decay, an absorption, an emission, a creation of new particles. Let particles $1,\dots,k$ be the incoming particles and $k+1,\dots,n$ the outgoing particles, with [[Def - Four-Momentum and Rest Mass|four-momenta]] $P_i^\mu$. Then the **total four-momentum is conserved**:
> $$\sum_{i=1}^{k} P_i^\mu \;=\; \sum_{j=k+1}^{n} P_j^\mu.$$
> This single four-vector equation comprises four scalar conservation laws:
> $$\sum_{\text{in}} E_i = \sum_{\text{out}} E_j \quad(\mu = 0,\ \text{conservation of energy}), \qquad \sum_{\text{in}}\mathbf{p}_i = \sum_{\text{out}}\mathbf{p}_j\quad(\mu = 1,2,3,\ \text{conservation of three-momentum}).$$
> The law is **Lorentz-covariant**: because both sides transform identically as four-vectors, if it holds in one inertial frame it holds in every inertial frame. In the non-relativistic limit it reduces to the two separate Newtonian laws of conservation of mass and conservation of momentum. The number of outgoing particles need not equal the number of incoming particles.

---

# Motivation

Newtonian collision physics rested on two conservation laws: momentum was always conserved, and mass was always conserved. Kinetic energy was conserved only for elastic collisions — in an inelastic collision it leaked away into heat. These were three statements of unequal status, and they were logically independent: one could imagine a universe with momentum conservation but not mass conservation.

Relativity has, by [[Thm - Mass-Energy Equivalence|mass–energy equivalence]], already told us that mass and kinetic energy are interconvertible — they are different forms of the one thing, energy. So the Newtonian picture of *two* separate conserved quantities cannot survive. The question this theorem answers is: **what single quantity replaces them, and why is its conservation a law?**

The answer is dictated by the requirement that physics look the same in every inertial frame. A conservation law is a statement that some quantity is the same before and after. If that quantity is a frame-dependent thing — a single number like energy alone, or a triple like three-momentum alone — then the *statement* of the law involves a choice of frame, and one must check separately that it holds in every frame. That is unsatisfactory and, it turns out, unnecessary. The quantity that is genuinely conserved is the [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu$, a four-vector. Conservation of a four-vector, $\sum P_{\text{in}}^\mu = \sum P_{\text{out}}^\mu$, is a four-vector equation: both sides are four-vectors, both transform by the same matrix $\Lambda$, so the equation is automatically true in all frames if true in one. The frame-independence is built into the *type* of the conserved object. This is the deep reason the conserved quantity must be a four-vector and not a loose collection of components — and it is why the four-momentum was constructed, in [[Def - Four-Momentum and Rest Mass|its definition]], to be a four-vector in the first place.

The unification is then automatic. The four scalar equations packed inside the one four-vector equation are conservation of energy (the time component) and conservation of three-momentum (the spatial components). The Newtonian conservation of mass is recovered as the leading term of the energy equation in the low-speed expansion. Three Newtonian statements of unequal standing collapse into one covariant law — and the law's power in problem-solving comes precisely from its being a *vector* equation that one can transform, square, and contract at will.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "no external forces act during the process". The skill is recognising when this holds and what counts as a single "process".

The first disguised source is **a sufficiently short and isolated interaction.** Property $B$: any collision or decay localised in space and time, far from other matter. The bridge: external forces (gravity from distant bodies, ambient fields) act over the whole trajectory, but over the brief instant of the interaction their impulse is negligible compared with the momentum exchanged between the participants. The non-obviousness: even in a gravitational field or a lab full of apparatus, the four-momentum is conserved *across the interaction* to excellent accuracy. *Example:* any particle-physics scattering event, analysed as if in empty space.

The second disguised source is **a closed system, with all participants accounted for.** Property $B$: a process in which every particle that carries energy or momentum — including photons of radiation — is included in the bookkeeping. The bridge: "no external force" really means "nothing outside the system exchanges four-momentum with it"; if radiation is emitted, it carries four-momentum, so as long as the emitted photons are counted as outgoing particles the law holds exactly. The non-obviousness: an inelastic collision that "loses energy to radiation" still conserves four-momentum once the radiation is on the books — unlike the Newtonian case where energy genuinely vanished into heat. *Example:* an excited atom decaying, with the emitted photon included.

The third disguised source is **a process described by a Lorentz-covariant equation of motion with vanishing force.** Property $B$: particles obeying [[Thm - The Relativistic Equation of Motion|the relativistic equation of motion]] $dP^\mu/d\tau = F^\mu$ with $F^\mu = 0$ for each free particle between interactions. The bridge: $F^\mu = 0$ means $P^\mu$ is constant along each worldline, and a local interaction conserving four-momentum at the vertex then conserves the total. The non-obviousness: conservation of four-momentum is the integrated, global form of the differential law $dP^\mu/d\tau = 0$. *Example:* this is how conservation is justified from Noether's theorem and the equation of motion.

**Targets (Output Amplification)**

The conclusion is the four-vector equation $\sum P_{\text{in}}^\mu = \sum P_{\text{out}}^\mu$.

Combine the conclusion with **the operation of squaring.** Property $D$: a problem containing a four-momentum you do not want to know in detail. The amplified result $E$: isolate the unwanted four-momentum on one side, $P_{\text{unwanted}} = \sum(\text{known}) - \sum(\text{known})$, and take the Minkowski square; the left side becomes the known scalar $m^2c^2$ (or $0$ for a photon), eliminating the unwanted particle entirely. This "rearrange and square" combination is the single most powerful technique in relativistic kinematics, and it works *because* conservation is a four-vector equation that can be squared.

Combine the conclusion with **a change to the centre-of-momentum frame.** Property $D$: a multi-particle process. The amplified result $E$: in the frame where $\sum\mathbf{p} = 0$, the conserved total four-momentum is purely temporal, $(\,E_{\text{tot}}/c,\mathbf{0})$, and the conservation law becomes a *scalar* statement about total energies; combined with [[Thm - Mass-Energy Equivalence|mass–energy equivalence]] this gives the invariant mass of the system and the threshold conditions for reactions.

Combine the conclusion with **the demand that a reaction be kinematically possible.** Property $D$: a proposed process $A\to B+C+\cdots$. The amplified result $E$: conservation of four-momentum is a *necessary condition* for the process to occur, and evaluating it (often by squaring) yields inequalities — a particle can decay only if heavier than its products; a single photon cannot decay in vacuum. The law is thus a filter ruling processes in or out.

---

# Why Is It True

The conservation of four-momentum is, at the deepest level, a consequence of a symmetry, and the cleanest way to see why it is true is through that symmetry — though the experimental and the structural arguments both illuminate it.

The structural argument runs as follows. We know two facts independently. First, the spatial three-momentum $\mathbf{p} = \gamma m\mathbf{u}$ is conserved in interactions: this is the relativistic upgrade of Newtonian momentum conservation, confirmed by every collision experiment, and it must hold because momentum conservation follows from the homogeneity of space — the fact that the laws of physics do not care *where* an experiment is done. Second, the four-momentum $P^\mu$ is a four-vector: its time and space components rotate into each other under Lorentz boosts. Now suppose, for contradiction, that the *spatial* part $\sum\mathbf{p}$ were conserved but the *time* part $\sum E$ were not. Conservation of $\sum\mathbf{p}$ is the statement that the spatial part of the four-vector $\Delta P^\mu_{\text{tot}} = \sum P_{\text{out}} - \sum P_{\text{in}}$ vanishes. But $\Delta P^\mu_{\text{tot}}$ is a four-vector (a difference of sums of four-vectors), and a four-vector whose spatial part vanishes *in one frame* has, in general, a nonzero spatial part in a boosted frame — because boosts mix time and space components. So if $\sum\mathbf{p}$ is conserved in every frame, the four-vector $\Delta P^\mu_{\text{tot}}$ must have *vanishing spatial part in every frame*, which forces it to be the zero vector — its time part vanishes too. **You cannot conserve the spatial part of a four-vector in all frames without conserving the whole thing.** Conservation of three-momentum, *promoted to a frame-independent law*, drags conservation of energy along with it. The two are not independent; the four-vector structure welds them together.

The symmetry argument makes this precise and is the modern foundation. Noether's theorem says every continuous symmetry of the action yields a conserved quantity. Invariance under spatial translations gives conservation of three-momentum; invariance under *time* translations gives conservation of energy. In a relativistic theory, space and time translations are unified into translations of Minkowski space — the translation part of the Poincaré group — and the four conserved quantities they generate are unified into the single conserved four-vector $P^\mu$. The conservation of four-momentum is the Noether current of spacetime-translation invariance: it holds because the laws of physics do not care *where or when* an experiment is performed, and "where" and "when" are unified in relativity.

The low-speed sanity check confirms the picture. Expanding the conserved energy $\sum\gamma_i m_i c^2 = \sum(m_ic^2 + \tfrac12 m_iu_i^2 + \cdots)$, the leading term is $c^2\sum m_i$. For this to be conserved at leading order is Newtonian conservation of *mass*; the next term, $\sum\tfrac12 m_iu_i^2$, conserved at next order, is conservation of *kinetic energy*. So the single relativistic law contains, as successive terms in a $u/c$ expansion, both of the things the Newtonian world conserved separately — exactly as it should, since relativity must reduce to Newton at low speed.

---

# What Makes This Hard

The non-obvious step is conceptual: recognising that conservation of four-momentum is *one* law, not two, and that its power comes from being a four-vector equation one is allowed to square and to transform. The most common error is to invoke conservation of *kinetic energy* — true for elastic Newtonian collisions — in a relativistic problem; relativistically it is the *total* energy $\sum\gamma m c^2$ that is conserved, and rest mass can convert to kinetic energy, so kinetic energy alone is generally not conserved. A second frequent slip is forgetting a participant: "energy is lost to radiation" is a Newtonian habit; relativistically the radiation carries four-momentum and must be counted as an outgoing particle, after which the law holds exactly.

---

# Rederivation Scaffold

**High-level strategy:**
Conservation of three-momentum follows from homogeneity of space; promoting it to a frame-independent law and using that $P^\mu$ is a four-vector forces conservation of the whole four-vector. Equivalently, it is the Noether current of spacetime-translation invariance.

**Subgoal decomposition:**

1. **Take conservation of relativistic three-momentum as given.** $\sum\mathbf{p}_{\text{in}} = \sum\mathbf{p}_{\text{out}}$, the relativistic upgrade of Newtonian momentum conservation.
   - *Hint:* This follows from homogeneity of space; accept it as the experimental/Noether input.
   - *Why needed:* It is the spatial part of the four-vector law.

2. **Form the total four-momentum change.** Define $\Delta P^\mu = \sum P_{\text{out}}^\mu - \sum P_{\text{in}}^\mu$, a four-vector.
   - *Hint:* A difference of sums of four-vectors is a four-vector.
   - *Why needed:* The claim is $\Delta P^\mu = 0$.

3. **Use that the spatial part vanishes in every frame.** Three-momentum conservation, as a law, holds in all inertial frames, so the spatial part of $\Delta P^\mu$ is zero in all frames.
   - *Hint:* A law is frame-independent by assumption (Postulate 1).
   - *Why needed:* This is the lever.

4. **Conclude the four-vector vanishes.** A four-vector with vanishing spatial part in every frame is the zero vector.
   - *Hint:* Boosts mix time and space components; if the spatial part were nonzero in time but zero in space in one frame, a boost would give a nonzero spatial part — contradiction unless $\Delta P^\mu = 0$.
   - *Why needed:* It delivers conservation of energy ($\Delta P^0 = 0$) and hence of the whole four-momentum.

5. **Check the Newtonian limit.** Expand $\sum E_i = \sum\gamma_i m_ic^2$ in $u/c$; leading term is mass conservation, next term kinetic-energy conservation.
   - *Hint:* $\gamma = 1 + \tfrac12 u^2/c^2 + \cdots$.
   - *Why needed:* Confirms the law reduces correctly.

---

# Lemma Decomposition

> [!note]- Lemma 1: A four-vector with vanishing spatial part in all frames is zero
> **Statement:** If $V^\mu$ is a four-vector whose spatial components $\mathbf{V}$ vanish in *every* inertial frame, then $V^\mu = 0$.
>
> **Hint:** Apply a boost and see what it does to a four-vector of the form $(V^0,\mathbf{0})$.
>
> **Why needed:** It is the step that upgrades conservation of three-momentum to conservation of the full four-momentum.
>
> > [!note]- Full proof
> > Suppose $V^\mu$ has vanishing spatial part in some frame $S$: $V^\mu = (V^0,\mathbf{0})$. Apply a [[Def - The Lorentz Transformation|Lorentz boost]] of speed $v$ along the $x$-axis. The transformed components are $V'^0 = \gamma_v V^0$, $V'^1 = -\gamma_v v\,V^0/c$, $V'^2 = V'^3 = 0$. The spatial part in $S'$ is therefore $\mathbf{V}' = (-\gamma_v v\,V^0/c,0,0)$, which vanishes only if $V^0 = 0$ (since $\gamma_v v\neq 0$ for $v\neq 0$). By hypothesis the spatial part vanishes in *every* frame, in particular in $S'$, so $V^0 = 0$. Then $V^\mu = (0,\mathbf{0}) = 0$ in $S$, hence in all frames. $\square$

> [!note]- Lemma 2: The Newtonian limit
> **Statement:** Conservation of the energy components, $\sum\gamma_i m_ic^2 = \text{const}$, reduces at successive orders in $u/c$ to conservation of mass $\sum m_i = \text{const}$ and conservation of kinetic energy $\sum\tfrac12 m_iu_i^2 = \text{const}$.
>
> **Hint:** Binomial-expand each $\gamma_i$.
>
> **Why needed:** It shows the relativistic law contains both Newtonian conservation laws.
>
> > [!note]- Full proof
> > For each particle, $\gamma_i m_ic^2 = m_ic^2(1 + \tfrac12 u_i^2/c^2 + \cdots) = m_ic^2 + \tfrac12 m_iu_i^2 + O(u_i^4/c^2)$. Summing over incoming particles and over outgoing particles and equating (conservation of the energy component):
> > $$\sum_{\text{in}}\Big(m_ic^2 + \tfrac12 m_iu_i^2 + \cdots\Big) = \sum_{\text{out}}\Big(m_jc^2 + \tfrac12 m_ju_j^2 + \cdots\Big).$$
> > At order $c^2$ (the leading term, with the explicit factor $c^2$): $\sum_{\text{in}}m_i = \sum_{\text{out}}m_j$ — Newtonian conservation of mass. At the next order: $\sum_{\text{in}}\tfrac12 m_iu_i^2 = \sum_{\text{out}}\tfrac12 m_ju_j^2$ — conservation of Newtonian kinetic energy. (The latter holds only to this order; relativistically the rest-mass term and the kinetic term mix, which is why kinetic energy alone is not exactly conserved.) $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Consider an interaction with incoming four-momenta $P_1^\mu,\dots,P_k^\mu$ and outgoing four-momenta $P_{k+1}^\mu,\dots,P_n^\mu$, no external forces acting.
>
> **Input.** Conservation of relativistic three-momentum, $\sum_{\text{in}}\mathbf{p}_i = \sum_{\text{out}}\mathbf{p}_j$, holds in every inertial frame. This is the relativistic form of Newtonian momentum conservation, itself the Noether consequence of the homogeneity of space; as a *law* it is frame-independent by Postulate 1.
>
> **The four-vector of imbalance.** Define
> $$\Delta P^\mu = \sum_{j=k+1}^n P_j^\mu - \sum_{i=1}^k P_i^\mu.$$
> Each $P^\mu$ is a [[Def - Four-Vector|four-vector]], so $\Delta P^\mu$, a difference of sums of four-vectors, is a four-vector.
>
> **Spatial part vanishes everywhere.** The spatial components of $\Delta P^\mu$ are $\sum_{\text{out}}\mathbf{p}_j - \sum_{\text{in}}\mathbf{p}_i$, which vanish by the input — and they vanish in *every* inertial frame, since three-momentum conservation is a frame-independent law.
>
> **The whole four-vector vanishes.** By **Lemma 1**, a four-vector whose spatial part vanishes in every inertial frame is the zero four-vector. Hence $\Delta P^\mu = 0$, that is,
> $$\sum_{i=1}^k P_i^\mu = \sum_{j=k+1}^n P_j^\mu.$$
> The time component of this equation, $\sum E_i = \sum E_j$, is conservation of energy; the spatial components are conservation of three-momentum. The law is manifestly Lorentz-covariant: under $\Lambda$ both sides transform as $P^\mu\to\Lambda^\mu{}_\nu P^\nu$, so the equation holds in $S'$ whenever it holds in $S$.
>
> **Newtonian limit.** By **Lemma 2**, expanding the conserved energy component in powers of $u/c$ recovers conservation of mass at leading order and conservation of kinetic energy at next order. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Inelastic collisions and the creation of mass.** Two lumps of clay, each of rest mass $m$, collide head-on and stick. Newtonian physics says kinetic energy is "lost to heat". Relativistically, conservation of four-momentum says the combined lump has rest mass $M > 2m$, the excess being exactly the lost kinetic energy over $c^2$ — the heat has *weight*. Computing $M$ from $\sum P_{\text{in}} = P_{\text{out}}$ and squaring is the exercise; the application is nonobvious because it reveals "heat" as rest mass.

**Why a particle accelerator collides two beams.** To create a heavy particle of mass $M$ by colliding two particles of mass $m$, the threshold energy depends drastically on the frame: in a fixed-target setup (one particle at rest) the required beam energy scales as $M^2/m$, while in a colliding-beam setup it scales only as $M$. The difference is a pure four-momentum-conservation calculation — see [[Ex - Threshold energy for particle production]] — and it is *the* reason the LHC collides two beams rather than firing one beam at a stationary target.

**Conservation in a decay chain.** A particle decays, and its products decay further. Conservation of four-momentum applies at *each* vertex, and the total four-momentum of the final-state particles equals that of the original. Reconstructing the mass of an unseen intermediate particle (a resonance) from the four-momenta of the final products — the "invariant mass" technique of experimental particle physics — is conservation of four-momentum run backwards, and it is how the Higgs boson was found in the $h\to\gamma\gamma$ channel.

---

# Bridges

- **[[Thm - Mass-Energy Equivalence]]** — the partner theorem. Mass–energy equivalence says the time component of $P^\mu$ is the energy; conservation of four-momentum says the whole vector is conserved. Together they replace Newtonian conservation of mass and of energy.

- **[[Thm - The Relativistic Equation of Motion]]** — the differential parent. The equation of motion $dP^\mu/d\tau = F^\mu$ becomes, for $F^\mu = 0$, the statement that each free particle's four-momentum is constant; conservation of total four-momentum is its integrated, multi-particle form.

- **[[Def - The Four-Momentum of a Photon]]** — photons enter the conservation law on the same footing as massive particles, through their null four-momentum. This is what makes Compton scattering, pair production, and the Doppler effect computable.

- **Noether's theorem** *(Geometric Mechanics)* — conservation of four-momentum is the Noether current associated with invariance of the action under translations of Minkowski space. Energy conservation is the time-translation current; three-momentum conservation the space-translation current; relativity unifies them.

- **The energy–momentum tensor** *(General Relativity, Continuum Mechanics)* — for a continuous medium, conservation of four-momentum becomes the local law $\partial_\mu T^{\mu\nu} = 0$, the vanishing divergence of the energy–momentum tensor.

---

# Unlocked by This

> [!tip] Relativistic Collision and Decay Kinematics *(from this topic)*
> Every problem of §2.2 and §2.3 — [[Ex - Threshold energy for particle production|threshold]], [[Ex - Compton scattering|Compton scattering]], [[Ex - Two-body decay kinematics|decay]], [[Ex - Pair production and the photon-photon threshold|pair production]] — is solved by writing this conservation law and then squaring or changing frame.

> [!tip] Local Conservation and the Energy–Momentum Tensor *(from General Relativity)*
> For fields and continua, conservation of four-momentum is the local equation $\partial_\mu T^{\mu\nu} = 0$. In curved spacetime it becomes $\nabla_\mu T^{\mu\nu} = 0$, and its compatibility with the geometry is what fixes the form of Einstein's field equations.
