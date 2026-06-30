---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Def - The Four-Momentum of a Photon"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \operatorname{diag}(+1,-1,-1,-1)$. A system is a finite collection of particles $\mathcal{P}_1,\ldots,\mathcal{P}_N$, each carrying a [[Def - Four-Momentum and Rest Mass|four-momentum]] $P_a^\mu$ (timelike for massive particles, null for [[Def - The Four-Momentum of a Photon|photons]]). A hypersurface $\Sigma$ is a three-dimensional slice of spacetime; it is **spacelike** if every tangent vector to it is spacelike (the [[Def - Observer and Local Rest Space|local rest space]] of an observer at an instant is the prototype). The total four-momentum of the system on $\Sigma$ is written $\mathbf{P}_\Sigma$ (or just $P$ when $\Sigma$ is suppressed). "In" and "out" denote the states before and after a localised interaction. Full registry on [[Special Relativity XIII — Energy and Momentum]].

---

# Statement

> **Conservation of four-momentum.** Let $\mathcal{S}$ be an **isolated** system of particles (subject to no external interaction). Then its total four-momentum is conserved. Stated frame-independently: the total four-momentum of $\mathcal{S}$ on any **closed** hypersurface vanishes,
> $$\mathcal{S}\ \text{isolated and}\ \Sigma\ \text{closed} \implies \mathbf{P}_\Sigma = \sum_{a}\varepsilon_a\,P_a(M_a) = 0,$$
> the sum running over the intersections $M_a$ of the particle worldlines with $\Sigma$, with sign $\varepsilon_a = \pm 1$ according to whether $P_a$ is directed into or out of $\Sigma$. Equivalently, the total four-momentum takes the *same value on every spacelike hypersurface* crossing all the worldlines: for two such slices $\Sigma, \Sigma'$,
> $$\mathbf{P}_{\Sigma'} = \mathbf{P}_\Sigma.$$

> **Collision form.** For a localised interaction (collision, decay, creation) converting an incoming set of particles into an outgoing set, the total four-momentum is conserved:
> $$\sum_{\text{in}} P_i^\mu \;=\; \sum_{\text{out}} P_j^\mu.$$
> The number of outgoing particles need not equal the number of incoming ones. As four scalar equations, this comprises conservation of energy ($\mu = 0$) and conservation of three-momentum ($\mu = 1,2,3$) relative to any inertial observer, and it holds in every inertial frame.

---

# Motivation

Newtonian physics had two great conservation laws of mechanics — conservation of momentum and conservation of energy — and, underneath them, a third so obvious nobody named it: conservation of mass. They were logically independent. A collision could conserve momentum and kinetic energy (elastic) or only momentum (inelastic); mass was simply never in question, because in Newton's world matter is neither created nor destroyed.

Relativity demands a single law in place of these, and this theorem is it. The reason a single law is *forced* is that energy and momentum are no longer separate quantities but the time and space parts of one four-vector, the [[Def - Four-Momentum and Rest Mass|four-momentum]]. A conservation law for that four-vector is automatically a conservation law for energy and for momentum together — and it must be, because a law that conserved energy but not momentum (or conserved them in only one frame) would not be a tensor equation and would violate the principle of relativity. The theorem is thus the dynamical core of the subject: it is the *one* input most problems need, and it is exact, not approximate.

The deeper motivation is what it does to mass. Because mass is the *length* of the four-momentum, and the length of a sum of four-vectors is not the sum of lengths, conservation of the four-momentum vector does *not* imply conservation of mass. Mass can be converted into kinetic energy and back, within the constraint that the total four-momentum is fixed. This is what licenses particle decay, particle creation, nuclear binding energy, and the whole of particle physics — phenomena impossible in a world with a separate conservation of mass. The single law is more permissive than Newton's three precisely because it ties energy, momentum, and mass into one object and conserves only the object.

Finally, the frame-independent formulation — total four-momentum vanishes on any closed hypersurface — is worth the abstraction because it makes the conservation law *geometric* rather than tied to a notion of "now". In Newtonian physics one says "the total momentum at time $t_1$ equals the total momentum at time $t_2$", which presupposes an absolute time slicing. Relativistically there is no absolute "now"; instead one says "what flows out of a closed region of spacetime equals what flowed in", which needs no preferred time and makes manifest that the law holds for every observer's slicing at once.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "the system is isolated". The art is recognising the many disguises that hypothesis wears.

The first disguised source is **"the interaction is localised in space and time"** — a collision, decay, or scattering event confined to a small region, with the particles free before and after. Even though forces act *during* the interaction (the particles push on each other), the *system as a whole* is isolated because no external agent touches it, and the four-momentum carried in equals the four-momentum carried out. The bridge is that internal forces, being mutual, cancel in the total: particle $a$ pushing $b$ is matched by $b$ pushing $a$ (the relativistic Newton's third law). *Example problem:* in $\gamma + e^- \to \gamma + e^-$ ([[Ex - Compton scattering]]), the photon and electron exert violent electromagnetic forces on each other during the scattering, yet the total four-momentum before equals that after, because those forces are internal.

The second disguised source is **"a single free particle"** — the degenerate one-particle system. A free particle is isolated, so its four-momentum is conserved, which means *constant*: $dP/d\tau = 0$. This is the law of inertia, and it is the source whenever a problem asserts a particle moves freely between interactions. The bridge is that "free" $=$ "isolated one-particle system" $=$ "constant four-momentum". *Example problem:* between emission and reception, a photon's four-momentum is constant, which is what lets the relativistic Doppler effect be computed by comparing the emitter's and receiver's contractions $P\cdot U_0$ ([[Def - The Four-Momentum of a Photon]]).

The third disguised source is **"the difference of total four-momenta before and after is a four-vector"** — a meta-source used to extend conservation across frames. If $\Delta P = \sum P_{\text{out}} - \sum P_{\text{in}}$ vanishes in one inertial frame, it vanishes in all, because a four-vector that is zero in one frame is zero in every frame (all its components, and its norm, are zero, an instance of the frame-independence of four-vector statements). The bridge is the tensorial character of $\Delta P$. *Example problem:* showing that if a reaction conserves four-momentum in the lab it does so in the centre-of-momentum frame — needed to combine the two-frame evaluations in [[Ex - Threshold energy for particle production|threshold]] calculations.

**Targets (Output Amplification)**

The conclusion is "$\sum P_{\text{in}} = \sum P_{\text{out}}$" — a four-vector equation.

Combine the conclusion with **the invariant-mass technique (squaring)**. Since the equation relates four-vectors, you may isolate an unwanted four-momentum on one side and take the Minkowski square; the unwanted four-momentum becomes the scalar $m^2$ (or $0$ for a photon) and disappears. The further result is a *scalar* equation in exactly the quantities of interest — the engine of nearly every collision calculation. The combination is useful because it converts a four-component vector statement, with an unknown four-momentum in it, into a single scalar relation with the unknown eliminated. *Example:* the Compton wavelength shift, obtained by $P_e' = P_\gamma + P_e - P_\gamma'$ then squaring ([[Ex - Compton scattering]]).

Combine the conclusion with **the freedom to choose the frame**. Because the conserved object is a four-vector, the conservation equation holds in every frame, so you may evaluate it in whichever frame trivialises the kinematics — almost always the centre-of-momentum frame, where the total spatial momentum vanishes and the total four-momentum is purely temporal. The further result is that "go to the smart frame" is a *theorem*, not a trick. *Example:* particle-production thresholds, where the centre-of-momentum frame makes $\sum P_{\text{out}} = (\sum m_{\text{out}}, \mathbf{0})$ at threshold ([[Ex - Threshold energy for particle production]]).

Combine the conclusion with **the mass-shell sign of each four-momentum**. Each $P_a$ is timelike (massive) or null (photon), and a sum of future-directed timelike/null vectors is future-directed timelike (or, exceptionally, null only if all are parallel null vectors). The further result is a *possibility filter*: a reaction whose two sides have four-momenta of incompatible character cannot occur. The combination is nonobvious because it turns a *dynamical* conservation law into a *kinematic* impossibility statement. *Example:* a single photon cannot decay to $e^+e^-$, since a null four-momentum cannot equal the timelike sum of two massive four-momenta ([[Ex - Whether a particle reaction is kinematically allowed]]).

---

# Why Is It True

The frame-independent reason is the cleanest, and it is essentially a flux-conservation argument. Picture a closed hypersurface $\Sigma$ in spacetime — a three-dimensional "surface" enclosing a four-dimensional region, the spacetime analogue of a balloon enclosing a volume. Each particle worldline that enters the region must also leave it (worldlines do not end inside, for an isolated system), so it pierces $\Sigma$ an even number of times, contributing its four-momentum with a $+$ sign going in and a $-$ sign going out. For a worldline that simply passes through, the in and out contributions are *the same four-momentum with opposite signs* (the four-momentum is constant on a free segment), so they cancel. At a collision *inside* the region, the worldlines that meet there are continued by the worldlines that leave, and the total four-momentum is unchanged at the vertex (this is the local statement being proved). Summing over all piercings, everything cancels: $\mathbf{P}_\Sigma = 0$.

**The whole theorem is the statement that four-momentum is a conserved current: what crosses out of any closed region equals what crossed in.** From this the collision form follows by taking $\Sigma$ to be a "pillbox" straddling the collision — two spacelike slices, one just before and one just after, joined by a timelike side through which no worldline passes. The vanishing of $\mathbf{P}_\Sigma$ becomes $\mathbf{P}_{\text{after}} - \mathbf{P}_{\text{before}} = 0$, i.e. $\sum P_{\text{in}} = \sum P_{\text{out}}$.

Why should the local statement at a collision vertex — that four-momentum is conserved there — hold? In the present axiomatic formulation it is *postulated*: conservation of four-momentum is the first fundamental principle of relativistic dynamics, on the same footing as Newton's laws. But it is not arbitrary; it is forced by symmetry. By **Noether's theorem**, every continuous symmetry of a system's action yields a conserved quantity, and the four-momentum is the conserved charge of *spacetime translation invariance*: the statement that the laws of physics are the same at every point of spacetime. An isolated system has no preferred location, so its action is translation-invariant, so its four-momentum is conserved. The Lagrangian formulation ([[Special Relativity XV — The Principle of Least Action|Special Relativity XV]]) demotes this theorem from an axiom to a consequence of translation symmetry — but in either telling, the conservation of four-momentum is the dynamical expression of the homogeneity of spacetime.

The reason a *single* four-vector law replaces Newton's separate laws is then transparent: spacetime translation invariance is *one* symmetry (a four-parameter group of translations in $t, x, y, z$), so Noether produces *one* conserved object with four components — the four-momentum — whose time component is energy (conserved by time-translation invariance) and spatial components are momentum (conserved by space-translation invariance). Newton's "separate" conservation of energy and momentum are the time and space parts of this single symmetry, artificially split because Newtonian physics treats time and space as different.

---

# What Makes This Hard

The conceptual hurdle is not the proof but believing that mass is not separately conserved: students reflexively impose $\sum m_{\text{in}} = \sum m_{\text{out}}$ in addition to four-momentum conservation, which is wrong and over-determines the problem. The non-obvious step in the frame-independent formulation is that the total four-momentum is independent of the spacelike slice chosen — that "the total momentum now" is well-defined despite there being no absolute "now" — which rests on the absence of a preferred time and on every worldline crossing every slice exactly once. The most common computational error is sign bookkeeping: getting $\varepsilon_a = \pm 1$ wrong on a closed hypersurface, or forgetting that the number of outgoing particles can differ from the number incoming.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Postulate the local conservation at each interaction vertex (or derive it from translation symmetry via Noether). Define the total four-momentum on a hypersurface as the signed sum of the four-momenta of the worldlines crossing it. Apply this to a closed hypersurface and use that free worldline segments carry constant four-momentum, so each worldline's in and out contributions cancel, giving total zero; specialise to a pillbox to get the collision form.

**Subgoal decomposition:**

1. **Define the total four-momentum on a hypersurface.** For a spacelike slice $\Sigma$, set $\mathbf{P}_\Sigma = \sum_a P_a(M_a)$ over the single crossing $M_a$ of each worldline; for a general closed $\Sigma$, attach signs $\varepsilon_a$ for in/out.
   - *Hint:* On a spacelike slice each timelike or null worldline crosses exactly once.
   - *Why needed:* Conservation is a statement comparing this quantity on different slices, so it must be well-defined first.

2. **Show a free worldline contributes zero to a closed $\Sigma$.** A free segment has constant four-momentum; crossing into and out of the closed region contributes $+P_a$ and $-P_a$, which cancel.
   - *Hint:* The four-momentum is constant on a free segment ([[Def - Four-Momentum and Rest Mass]], law of inertia), and the in/out orientations give opposite signs.
   - *Why needed:* This cancellation, summed over all worldlines, is the vanishing $\mathbf{P}_\Sigma = 0$.

3. **Handle collisions inside the region.** At a vertex, the incoming worldlines are continued by outgoing ones; the local postulate $\sum P_{\text{in}} = \sum P_{\text{out}}$ at the vertex ensures the four-momentum threading the region is conserved across it.
   - *Hint:* This is the postulated (or Noether-derived) local conservation.
   - *Why needed:* It is the only place the dynamical content enters; everything else is bookkeeping.

4. **Specialise to a pillbox for the collision form.** Take $\Sigma$ as two spacelike slices before and after the collision joined by a timelike wall crossed by nothing; $\mathbf{P}_\Sigma = 0$ becomes $\mathbf{P}_{\text{after}} = \mathbf{P}_{\text{before}}$.
   - *Hint:* The timelike wall contributes nothing because no worldline crosses it.
   - *Why needed:* It produces the practical form $\sum P_{\text{in}} = \sum P_{\text{out}}$ used in every exercise.

---

# Lemma Decomposition

> [!note]- Lemma 1: An isolated single particle has constant four-momentum
> **Statement:** If $\mathcal{P}$ is a free particle then $dP/d\tau = 0$, so $P$ is the same constant four-vector at every event of its worldline.
>
> **Hint:** Apply the conservation principle to a closed hypersurface cutting the worldline at two points.
>
> **Why needed:** This is the cancellation engine of the main argument — each free worldline segment carries a constant four-momentum, so its in and out crossings cancel.
>
> > [!note]- Full proof
> > Choose a closed hypersurface $\Sigma$ cutting the worldline $\mathcal{L}$ of the free particle at exactly two events $A$ and $B$, with $A$ where the worldline enters the enclosed region and $B$ where it leaves. The orientation gives $\varepsilon_A = +1$, $\varepsilon_B = -1$ (or vice versa), so the total four-momentum on $\Sigma$ is $\mathbf{P}_\Sigma = P(A) - P(B)$. By the conservation principle for the isolated one-particle system, $\mathbf{P}_\Sigma = 0$, hence $P(A) = P(B)$. Varying $\Sigma$, and hence the points $A, B$, over the whole worldline shows $P$ is the same four-vector everywhere: $P(M) = \text{const}$ for all $M\in\mathcal{L}$, i.e. $dP/d\tau = 0$. Since the four-momentum vector is tangent to the worldline, a constant tangent means $\mathcal{L}$ is a straight line; and since $m = \sqrt{P\cdot P}$, the mass is constant too. $\blacksquare$

> [!note]- Lemma 2: The total four-momentum is independent of the spacelike slice
> **Statement:** For an isolated system and two spacelike hypersurfaces $\Sigma, \Sigma'$ each crossing all worldlines, $\mathbf{P}_{\Sigma'} = \mathbf{P}_\Sigma$.
>
> **Hint:** Complete $\Sigma$ and $\Sigma'$ to a closed hypersurface and apply the vanishing principle.
>
> **Why needed:** It is the precise content of "four-momentum is conserved" in the frame-independent language, and it is what makes the collision form well-defined.
>
> > [!note]- Full proof
> > Take $\Sigma'$ to lie entirely to the future of $\Sigma$ (possible since both are spacelike and they do not intersect), and join them with a third hypersurface $\Sigma''$ — a timelike "side wall" — so that $\Sigma\cup\Sigma'\cup\Sigma''$ is a closed hypersurface enclosing the region between the two slices. Arrange $\Sigma''$ so that no worldline of the system crosses it (the particles all pass between $\Sigma$ and $\Sigma'$, not out the sides). By the conservation principle, $\mathbf{P}_{\Sigma\cup\Sigma'\cup\Sigma''} = 0$. The natural orientation of the closed surface (positive towards the interior) gives $\mathbf{P}_\Sigma$ with one sign and $\mathbf{P}_{\Sigma'}$ with the opposite (because $\Sigma'$ is traversed in the opposite sense as part of the closed boundary), while $\mathbf{P}_{\Sigma''} = 0$ since nothing crosses it. Thus $\mathbf{P}_\Sigma - \mathbf{P}_{\Sigma'} + 0 = 0$, giving $\mathbf{P}_{\Sigma'} = \mathbf{P}_\Sigma$. $\blacksquare$

> [!note]- Lemma 3: Conservation in one frame implies conservation in all
> **Statement:** If $\sum P_{\text{in}} = \sum P_{\text{out}}$ holds in one inertial frame, it holds in every inertial frame.
>
> **Hint:** The difference $\Delta P = \sum P_{\text{out}} - \sum P_{\text{in}}$ is a four-vector.
>
> **Why needed:** It justifies evaluating the conservation equation in whichever frame is convenient (rest frame, centre-of-momentum frame), the basis of the invariant-mass technique.
>
> > [!note]- Full proof
> > Each $P_a$ is a four-vector, so the finite sum $\Delta P^\mu = \sum_{\text{out}} P_j^\mu - \sum_{\text{in}} P_i^\mu$ is a four-vector. A four-vector that vanishes in one inertial frame vanishes in every inertial frame: under a Lorentz transformation $\Delta P'^\mu = \Lambda^\mu{}_\nu\Delta P^\nu$, and if $\Delta P^\nu = 0$ then $\Delta P'^\mu = 0$. Hence $\sum P_{\text{in}} = \sum P_{\text{out}}$ in the original frame implies the same in every frame. (Equivalently: all four components and the Minkowski norm of $\Delta P$ are zero, and these are frame-independent statements.) $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — the local postulate.** The first principle of relativistic dynamics is that four-momentum is conserved at each localised interaction: at a collision vertex the sum of the incoming four-momenta equals the sum of the outgoing four-momenta. (In the Lagrangian formulation of [[Special Relativity XV — The Principle of Least Action|Special Relativity XV]] this follows from spacetime-translation invariance via Noether's theorem; here we take it as an axiom.)
>
> **Total four-momentum on a hypersurface.** For an oriented hypersurface $\Sigma$ cutting the worldlines $\mathcal{L}_a$ of an isolated system, define
> $$\mathbf{P}_\Sigma = \sum_a \sum_{M\in\mathcal{L}_a\cap\Sigma}\varepsilon\,P_a(M),$$
> with $\varepsilon = +1$ if $P_a(M)$ points to the positive side of $\Sigma$ and $-1$ otherwise. For a *spacelike* $\Sigma$, each timelike or null worldline crosses exactly once (a spacelike surface lies outside the light cone at each of its points, so it cannot be tangent to or recross a causal worldline), and the natural future-orientation gives all $\varepsilon = +1$, so $\mathbf{P}_\Sigma = \sum_a P_a(M_a)$.
>
> **Vanishing on a closed hypersurface.** Let $\Sigma$ be closed (compact, no boundary). By Lemma 1 every free worldline segment carries a constant four-momentum, so a worldline entering and leaving the enclosed region contributes $+P_a$ and $-P_a$, cancelling. At any collision inside the region, Step 0 ensures the four-momentum threading the region is conserved across the vertex (incoming worldlines continued by outgoing ones, with equal total four-momentum). Summing all contributions, every four-momentum cancels and $\mathbf{P}_\Sigma = 0$. This is the frame-independent statement.
>
> **Independence of the slice.** By Lemma 2, for two spacelike slices $\Sigma, \Sigma'$ completed by a side wall $\Sigma''$ crossed by no worldline, $\mathbf{P}_{\Sigma'} = \mathbf{P}_\Sigma$: the total four-momentum is the same on every spacelike slice.
>
> **Collision form.** Take $\Sigma_{\text{before}}$ just before a localised interaction and $\Sigma_{\text{after}}$ just after, both spacelike. By the slice-independence, $\mathbf{P}_{\Sigma_{\text{after}}} = \mathbf{P}_{\Sigma_{\text{before}}}$, i.e. $\sum_{\text{out}} P_j = \sum_{\text{in}} P_i$. Relative to any inertial observer this is four scalar equations: the $\mu=0$ component is conservation of energy $\sum_{\text{in}} E_i = \sum_{\text{out}} E_j$, the spatial components conservation of three-momentum $\sum_{\text{in}}\mathbf{p}_i = \sum_{\text{out}}\mathbf{p}_j$.
>
> **All frames.** By Lemma 3, the difference $\Delta P = \sum P_{\text{out}} - \sum P_{\text{in}}$ is a four-vector; vanishing in one inertial frame, it vanishes in all. Hence the conservation law holds in every inertial frame. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Nuclear binding energy and the mass defect.** Apply conservation of four-momentum to a fusion or fission reaction: the total four-momentum is conserved, so the rest mass of the products (the length of the total four-momentum) plus the kinetic energy released equals the initial rest mass. The mass *defect* — the difference between the initial rest mass and the products' rest masses — is the energy liberated, $\Delta m\,c^2$. The application is out-of-distribution because it treats a nuclear reaction with the identical four-momentum bookkeeping as a particle collision; see [[Ex - The invariant mass of a system of particles]] for the technique.

**The relativistic rocket.** A rocket emitting photons (or exhaust) backwards is an isolated system, so its total four-momentum is conserved; integrating the conservation law over the burn gives a relativistic Tsiolkovsky equation relating final rapidity to the fraction of rest mass ejected ([[Ex - The relativistic rocket]]). The application is nonobvious because conservation is usually applied to instantaneous collisions, here to a continuous process.

**Photon gas and the equation of state.** A box of photons (blackbody radiation) is a system whose total four-momentum, in the box's rest frame, is purely temporal with energy $E$ and zero net momentum — yet its invariant mass $M = E$ is nonzero even though every constituent photon is massless. Conservation of four-momentum plus this observation underlies the statement that radiation has energy density $\rho$ and pressure $p = \rho/3$, the equation of state used in cosmology. The application connects particle conservation to thermodynamics and the early universe.

---

# Bridges

- **[[Def - Four-Momentum and Rest Mass]]** — this theorem is what makes the four-momentum *the* dynamical object: it is conserved, and its conservation is the master law. The mass-shell $P\cdot P = m^2$ of the definition combines with conservation through the invariant-mass technique (square the conserved sum) to solve every collision problem.

- **[[Thm - Mass-Energy Equivalence]]** — conservation of four-momentum is what makes mass–energy equivalence *physically operative*: because the conserved object is the four-vector and mass is only its length, mass can be converted to kinetic energy and back, within the constraint that $\sum P$ is fixed. Without conservation, $E = mc^2$ would be a static curiosity; with it, it is the bookkeeping of every reaction.

- **Noether's theorem and spacetime translation invariance** — conservation of four-momentum is the Noether charge of the four-parameter group of spacetime translations, the statement that physics is the same at every event. This is why a *single* four-vector law replaces Newton's separate energy and momentum conservation: one symmetry (translations), one conserved four-vector. The Lagrangian derivation is [[Special Relativity XV — The Principle of Least Action|Special Relativity XV]].

- **Conservation of the energy–momentum tensor** — for a *continuous* distribution of matter, the conserved object is not a four-vector $P^\mu$ but a tensor field $T^{\mu\nu}$, and conservation becomes the local equation $\partial_\mu T^{\mu\nu} = 0$. This theorem is its particle-mechanics ancestor; the tensor version, developed in [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy|Special Relativity XXIII]], is the source term of Einstein's field equations.

---

# Unlocked by This

> [!tip] Particle Collisions, Decays, and Thresholds *(from §13.2)*
> Conservation of four-momentum is the single input to every collision and decay calculation: combined with the mass-shell $P\cdot P = m^2$ and the invariant-mass technique, it determines decay energies, scattering angles, the Compton shift, and reaction thresholds. See [[Thm - Elastic Collisions and the Compton Effect]] and [[Thm - Inelastic Collisions and Particle Production]].

> [!tip] The Energy–Momentum Tensor *(from General Relativity and Field Theory)*
> For continuous media the conserved four-momentum becomes the **energy–momentum tensor** $T^{\mu\nu}$, whose conservation $\partial_\mu T^{\mu\nu} = 0$ is the local form of this theorem. It packages energy density, momentum density, and stress, is the source of gravity in **Einstein's field equations** $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$, and its covariant conservation $\nabla_\mu T^{\mu\nu} = 0$ is built into the geometry via the contracted Bianchi identity. Developed in [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy|Special Relativity XXIII]].
