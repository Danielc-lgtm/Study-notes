---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Angular Momentum Four-Tensor"
  - "Def - Four-Momentum and Rest Mass"
  - "Thm - Conservation of Four-Momentum"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. A particle has [[Def - Worldline of a Particle|worldline]] $\mathscr{L}$, [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$, proper time $\tau$, [[Def - Four-Momentum and Rest Mass|four-momentum]] $p = mU$. A system $\mathscr{S}$ has particles $a$ with four-momenta $p_a$ and total momentum $P = \sum_a p_a$. The [[Def - Angular Momentum Four-Tensor|angular momentum]] about an event $C$ is $J_C = \overrightarrow{CM}^\flat\wedge p$ (particle) or $J_C|_\Sigma = \sum_a\overrightarrow{CM_a}^\flat\wedge p_a$ on a spacelike hypersurface $\Sigma$ (system); $\vec\sigma_C$ is the angular momentum vector relative to an observer of four-velocity $U_0$. "Isolated" means no external force, so each free particle obeys the law of inertia $dp/d\tau = 0$ and $P$ is conserved. Full registry on [[Special Relativity XIV — Angular Momentum and Spin]].

---

# Statement

> **Conservation of angular momentum (particle).** For an isolated particle, the angular momentum about any fixed event $C\in\mathscr{E}$ is constant along the worldline:
> $$\forall M\in\mathscr{L},\qquad J_C(M) = \text{const}.$$

> **Conservation of angular momentum (system).** For an isolated system $\mathscr{S}$, the total angular momentum $J_C|_\Sigma$ about any event $C$ is independent of the spacelike hypersurface $\Sigma$ (provided $\Sigma$ meets every worldline once), hence defines a single two-form $J_C$; it is also independent of the observer. This conservation is an **independent first principle** for a system of two or more particles, on the same footing as the conservation of four-momentum.

> **Conservation of the angular momentum vector.** For an isolated system, the angular momentum vector $\vec\sigma_C$ relative to any *inertial* observer is constant:
> $$\frac{d\vec\sigma_C}{dt} = 0.$$

A companion identity, the **change-of-origin rule**, holds whether or not the system is isolated: for two events $C, C'$,
$$
J_{C'} = J_C + \overrightarrow{C'C}^\flat\wedge P,
$$
with $P$ the total four-momentum on the hypersurface.

---

# Motivation

The previous chapter established the conservation of four-momentum, the relativistic statement that the total energy and the total three-momentum of an isolated system are constant. But energy and momentum are not the only conserved quantities of mechanics — the other great conservation law, as old as Kepler's second law, is the conservation of angular momentum. This theorem is its relativistic form, and the chapter would be incomplete without it: the two conservation laws together are what make relativistic dynamics a closed, predictive theory.

What needs proving, and what is merely postulated, differs between the single-particle and many-particle cases, and the distinction is instructive. For a *single* isolated particle the conservation is a *theorem* — it follows from the law of inertia, because a particle that moves in a straight line at constant momentum sweeps out a worldline about which its moment of momentum is constant. For a *system* of two or more particles the conservation is a *first principle*, an independent postulate. This is one of the genuine structural differences between relativistic and Newtonian mechanics. In Newtonian mechanics, the conservation of a system's angular momentum is *derived* from Newton's third law in its strong form — that the forces between two particles are not only equal and opposite but also directed along the line joining them. Relativity has no such law: there is no instantaneous action at a distance, forces are mediated by fields, and the "line joining two particles" is not even a frame-independent notion. So the strong third law is unavailable, and the conservation of angular momentum cannot be derived from it. It must be postulated separately — and it is, with as much empirical warrant as the conservation of four-momentum.

The third statement, that the angular momentum *vector* relative to an inertial observer is constant, is the laboratory face of the abstract conservation. It is what an experimenter actually measures: a spinning isolated body keeps its angular momentum vector fixed in an inertial frame, the principle behind every gyroscope. The theorem says this follows from the conservation of the full two-form, once one is careful that the inertial observer's rest space does not itself rotate.

---

# Sources and Targets

**Sources (Input Broadening)**

The single-particle theorem's precondition is "the particle is isolated", i.e. obeys the law of inertia $dp/d\tau = 0$. The disguises this wears are the disguises of "free particle".

The first disguised source is **"the particle is in free fall in special relativity", i.e. subject to no force**. Any particle on which the net four-force vanishes is isolated, and its angular momentum about any fixed point is conserved — even if forces are present but balanced. The bridge is that $f = dp/d\tau = 0$ is exactly the law of inertia. *Example problem:* a particle drifting through a region where the net force is zero conserves its angular momentum about every fixed event, so its impact parameter (the perpendicular distance of its straight-line path from a chosen point) is constant — the relativistic statement that a free particle's trajectory is a straight line at fixed distance from any point.

The second disguised source is **"the four-force is central about $C$"**. If the force always points along $\overrightarrow{CM}$, then $N_C = \overrightarrow{CM}^\flat\wedge f = 0$ even though the particle is not free, and angular momentum about $C$ is conserved. The bridge is that a central force has zero moment. The nonobviousness is that conservation about $C$ can hold for a *non*-isolated particle, provided the force is central about that particular point. *Example problem:* a relativistic particle orbiting a fixed centre under a central four-force conserves its angular momentum about the centre, giving the relativistic Kepler problem its first integral.

The third disguised source is **"the system is isolated", for the many-particle law**. Here the source is the first-principle isolation of a system — no external forces, internal interactions mediated by fields that themselves carry the balancing angular momentum. The bridge is the postulate itself. The nonobviousness is that one must include the *field* angular momentum to make the total conserved when the interaction is not contact; the particle angular momentum alone is conserved only for genuinely isolated, non-interacting (or contact-interacting) systems. *Example problem:* two charges interacting electromagnetically conserve total angular momentum only when the angular momentum stored in the electromagnetic field is included.

**Targets (Output Amplification)**

The conclusion is "$J_C$ is constant".

Combine the conclusion with **the change-of-origin rule**. Since $J_C$ is conserved about every point, and $J_{C'} = J_C + \overrightarrow{C'C}^\flat\wedge P$ with $P$ also conserved, the angular momentum about *every* point is conserved simultaneously. The further result is that one may freely choose the most convenient reference point — typically the centre of inertia, where the orbital part vanishes and $J_G = S$ is the pure spin. The combination is useful because it lets a hard computation about an awkward point be replaced by an easy one about $G$. *Example:* computing the spin of a system by evaluating $J_G$ in the centre-of-momentum frame.

Combine the conclusion with **the observer-independence of the two-form**. Since $J_C$ is the same for all observers and all hypersurfaces, any *contraction* of it with a fixed four-vector is a conserved scalar or vector. The further result is that the [[Def - Spin Four-Vector|spin four-vector]] $S^\mu = W^\mu/(mc)$ — built by contracting $J$ with $P$ through the Levi-Civita tensor — is a conserved invariant of the system. The combination is nonobvious because it produces a *vector* conservation law (three conserved components) from the tensor conservation law. *Example:* the spin direction of an isolated body is fixed in spacetime.

Combine the conclusion with **a collision or decay**. Angular momentum conservation across a reaction — $J_C$ before equals $J_C$ after — constrains the outgoing configuration just as four-momentum conservation does. The further result is selection rules: a spin-$0$ system cannot decay into a configuration with net orbital plus spin angular momentum unequal to zero. The combination is useful because it supplies constraints independent of, and complementary to, energy-momentum conservation. *Example:* the angular distribution of decay products is restricted by the conservation of total angular momentum.

---

# Why Is It True

The single-particle case is true for a reason that is almost visual once stated. A free particle moves in a straight line at constant momentum. Its angular momentum about a fixed point $C$ is the moment of that momentum — the momentum times the perpendicular distance from $C$ to the line of motion. As the particle slides along its straight path, the perpendicular distance from $C$ to the *line* does not change (the line is fixed), and the momentum does not change (it is free), so the moment does not change. That is the whole content: **a constant momentum along a fixed line has a constant moment about any point.**

The algebra makes this exact and reveals the relativistic ingredient. Differentiate $J_C = \overrightarrow{CM}^\flat\wedge p$:
$$
\frac{dJ_C}{d\tau} = \underbrace{\frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p}_{\text{motion of the particle}} + \underbrace{\overrightarrow{CM}^\flat\wedge\frac{dp}{d\tau}}_{\text{change of momentum}}.
$$
The second term vanishes by the law of inertia, $dp/d\tau = 0$ — that is the "constant momentum" half. The first term vanishes for a *purely relativistic* reason: $\frac{d\overrightarrow{CM}}{d\tau} = cU$ is the four-velocity, and $p = mU$ is parallel to it, so $cU\wedge p = cm\,U\wedge U = 0$. **The bold one-liner: the moment of momentum is constant because the velocity is parallel to the momentum (killing the "sliding along the line" term) and the momentum is constant (killing the "force" term).** The first cancellation, $p\parallel U$, is the relativistic identity $p = mU$ doing work that has no Newtonian analogue in this derivation — in Newton one argues geometrically with the perpendicular distance; here it is the four-dimensional parallelism that makes the term disappear.

The many-particle case cannot be true for this reason, because the particles interact and no single one is free. Here the honesty of the relativistic theory shows: there is no way to derive the conservation from the individual motions, because the strong action-reaction law that Newton used is simply false relativistically. The conservation is instead a *symmetry* statement — it is the Noether charge of Lorentz invariance, conserved because the laws of physics do not single out any direction or any boost. That this charge is conserved is as fundamental as the isotropy of space itself, and it is *postulated* at the same level as four-momentum conservation precisely because, like that law, it expresses a symmetry of nature rather than a consequence of particle mechanics. The deep reason it is true is Noether's theorem applied to Lorentz invariance, made explicit in [[Special Relativity XV — The Principle of Least Action]].

---

# What Makes This Hard

The conceptual trap is to expect the many-particle conservation to be *derivable*, as it is in Newtonian mechanics, and to waste effort trying to derive it from the particle motions — it cannot be, because relativity has no strong third law, and the conservation is a separate first principle. The technical subtlety in the single-particle proof is recognising that the term $\frac{d\overrightarrow{CM}}{d\tau}\wedge p$ vanishes not by the law of inertia but by the parallelism $p\parallel U$; people often kill both terms with "$dp/d\tau = 0$" and miss that the first term would vanish even with a force present (as long as the particle's momentum stays parallel to its velocity, which for $p = mU$ it always does). The most common error is in the change-of-origin rule: forgetting that the shift uses the *total* four-momentum $P$, so that the spin (about the centre of inertia) is point-independent only because the shift acts purely on the orbital part.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
For a single particle, differentiate the angular momentum two-form along the worldline and show both terms vanish — one by $p\parallel U$, the other by the law of inertia. For the change-of-origin rule, use bilinearity of the wedge and Chasles' relation. For the system, invoke the first-principle conservation and the constancy of $P$.

**Subgoal decomposition:**

1. **Differentiate the angular momentum.** Show $\frac{dJ_C}{d\tau} = \frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p + \overrightarrow{CM}^\flat\wedge\frac{dp}{d\tau}$.
   - *Hint:* Leibniz rule for the exterior product of two one-form-valued functions.
   - *Why needed:* It exposes the two terms that must each be shown to vanish.

2. **Kill the first term.** Show $\frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p = 0$.
   - *Hint:* $\frac{d\overrightarrow{CM}}{d\tau} = cU$ and $p = mU$, so this is $cm\,U^\flat\wedge U = 0$.
   - *Why needed:* It removes the "motion of the particle" contribution using the relativistic identity $p\parallel U$.

3. **Kill the second term.** Show $\overrightarrow{CM}^\flat\wedge\frac{dp}{d\tau} = 0$ for an isolated particle.
   - *Hint:* The law of inertia gives $dp/d\tau = 0$.
   - *Why needed:* It is the "constant momentum" half; combined with step 2 it gives $dJ_C/d\tau = 0$.

4. **Change of origin.** Show $J_{C'} = J_C + \overrightarrow{C'C}^\flat\wedge P$.
   - *Hint:* $\overrightarrow{C'M} = \overrightarrow{C'C} + \overrightarrow{CM}$ (Chasles); expand the wedge by bilinearity and sum over particles.
   - *Why needed:* It shows conservation holds about every point and isolates the orbital part.

5. **Angular momentum vector.** Show $d\vec\sigma_C/dt = 0$ for an inertial observer.
   - *Hint:* Write $J_C(\vec v,\vec w) = \epsilon(U_0,\vec\sigma_C,\vec v,\vec w)$ for constant $U_0$ and $\vec v,\vec w\in E_{u_0}$; differentiate, use $dJ_C/dt = 0$ and the constancy of $U_0$, and conclude $d\vec\sigma_C/dt$ is parallel to $U_0$; but $\vec\sigma_C\in E_{u_0}$, so it vanishes.
   - *Why needed:* It is the laboratory statement of conservation.

---

# Lemma Decomposition

> [!note]- Lemma 1: The displacement's derivative is parallel to the momentum
> **Statement:** Along the worldline, $\frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p = 0$.
>
> **Hint:** $\overrightarrow{CM}$ runs from a fixed point to the moving particle, so its derivative is the four-velocity.
>
> **Why needed:** It removes the term in $dJ_C/d\tau$ that comes from the particle's motion, using only $p = mU$, independently of any force.
>
> > [!note]- Full proof
> > Since $C$ is fixed and $M$ moves along $\mathscr{L}$, $\frac{d\overrightarrow{CM}}{d\tau} = \frac{dM}{d\tau} = cU$, the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] (with $c$; here $c=1$). The [[Def - Four-Momentum and Rest Mass|four-momentum]] is $p = mU$, parallel to $U$. Hence $\frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p = cU^\flat\wedge(mU) = cm\,(U^\flat\wedge U) = 0$, since the exterior product of a one-form with (the dual of) the same vector is antisymmetric and vanishes. $\blacksquare$

> [!note]- Lemma 2: For a free particle the angular momentum is constant
> **Statement:** If $dp/d\tau = 0$, then $dJ_C/d\tau = 0$, so $J_C(M)$ is constant along $\mathscr{L}$.
>
> **Hint:** Combine Lemma 1 with the law of inertia.
>
> **Why needed:** It is the single-particle conservation theorem.
>
> > [!note]- Full proof
> > By the Leibniz rule, $\frac{dJ_C}{d\tau} = \frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p + \overrightarrow{CM}^\flat\wedge\frac{dp}{d\tau}$. The first term vanishes by Lemma 1. The second vanishes because the law of inertia for an isolated particle gives $\frac{dp}{d\tau} = 0$. Hence $\frac{dJ_C}{d\tau} = 0$, and $J_C$ is a constant two-form along the worldline. $\blacksquare$

> [!note]- Lemma 3: Change-of-origin rule
> **Statement:** $J_{C'} = J_C + \overrightarrow{C'C}^\flat\wedge P$, with $P$ the total four-momentum.
>
> **Hint:** Chasles' relation and bilinearity of the wedge.
>
> **Why needed:** It shows conservation holds about every point and isolates the $C$-dependence as the orbital part.
>
> > [!note]- Full proof
> > For each particle, $\overrightarrow{C'M_a} = \overrightarrow{C'C} + \overrightarrow{CM_a}$ (Chasles). Then
> > $$J_{C'}|_\Sigma = \sum_a \overrightarrow{C'M_a}^\flat\wedge p_a = \sum_a\big(\overrightarrow{C'C}^\flat + \overrightarrow{CM_a}^\flat\big)\wedge p_a = \overrightarrow{C'C}^\flat\wedge\Big(\sum_a p_a\Big) + \sum_a\overrightarrow{CM_a}^\flat\wedge p_a,$$
> > using bilinearity of $\wedge$. The first sum is $\overrightarrow{C'C}^\flat\wedge P$ and the second is $J_C|_\Sigma$. $\blacksquare$

> [!note]- Lemma 4: The angular momentum vector is conserved for an inertial observer
> **Statement:** For an isolated system and an inertial observer of constant four-velocity $U_0$, $d\vec\sigma_C/dt = 0$.
>
> **Hint:** Express $J_C$ through the Levi-Civita tensor and the angular momentum vector, then differentiate.
>
> **Why needed:** It is the laboratory ("gyroscope") form of the conservation law.
>
> > [!note]- Full proof
> > For an inertial observer, $J_C(\vec v,\vec w) = \epsilon(U_0,\vec\sigma_C,\vec v,\vec w)$ for any $\vec v,\vec w\in E_{u_0}$ (the angular momentum vector is the "magnetic" part of the two-form). Differentiating with respect to the observer's proper time $t$, and using that $J_C$ is constant (the system is isolated, so $dJ_C/dt = 0$) and that $U_0$ and the chosen $\vec v,\vec w$ are constant,
> > $$0 = \frac{d}{dt}J_C(\vec v,\vec w) = \epsilon\Big(U_0, \frac{d\vec\sigma_C}{dt}, \vec v, \vec w\Big)$$
> > for all $\vec v,\vec w\in E_{u_0}$. The alternate (totally antisymmetric) character of $\epsilon$ then forces $\frac{d\vec\sigma_C}{dt}$ to be collinear with $U_0$. But $\vec\sigma_C\in E_{u_0}$ and $E_{u_0}$ is constant (inertial observer), so $\frac{d\vec\sigma_C}{dt}\in E_{u_0}$, orthogonal to $U_0$. A vector both collinear with and orthogonal to $U_0$ is zero. Hence $\frac{d\vec\sigma_C}{dt} = 0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Single particle.** Let $\mathscr{P}$ be isolated, with angular momentum $J_C = \overrightarrow{CM}^\flat\wedge p$ about the fixed event $C$. By Lemma 2, $\frac{dJ_C}{d\tau} = 0$, so $J_C(M)$ is the same two-form at every $M\in\mathscr{L}$.
>
> **System.** For a system of two or more interacting particles, the conservation of $J_C|_\Sigma$ — its independence of the spacelike hypersurface $\Sigma$ and of the observer — is taken as a first principle, on the same footing as the [[Thm - Conservation of Four-Momentum|conservation of four-momentum]]. (It cannot be derived from the particle motions: relativity has no strong action-reaction law. The Noether derivation from Lorentz invariance is given in [[Special Relativity XV — The Principle of Least Action]].) Granting the principle, $J_C|_\Sigma$ is independent of $\Sigma$, so it defines a single two-form $J_C$; this is the content of the boxed statement (10.28)–(10.29) of the source.
>
> **Change of origin.** Lemma 3 gives $J_{C'} = J_C + \overrightarrow{C'C}^\flat\wedge P$. Since $P$ is conserved and $J_C$ is conserved, so is $J_{C'}$ for every $C'$: angular momentum about every point is conserved at once.
>
> **Angular momentum vector.** Lemma 4 gives $\frac{d\vec\sigma_C}{dt} = 0$ for any inertial observer: the angular momentum vector relative to an inertial frame is constant. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The relativistic Kepler problem.** A particle moving under a central four-force about a fixed centre $C$ conserves its angular momentum about $C$ because the four-torque $\overrightarrow{CM}^\flat\wedge f$ vanishes for a central force ([[Def - Four-Torque]]). This first integral reduces the relativistic orbit problem to a one-dimensional radial problem, exactly as in the Newtonian case, and the conserved angular momentum is what produces the (precessing) orbit. The application is nonobvious because conservation here holds for a *non-isolated* particle, by virtue of the centrality of the force about that particular point.

**Field angular momentum in electromagnetism.** Two charges interacting electromagnetically do *not* conserve their mechanical angular momentum alone; the deficit is stored in the electromagnetic field, and only the total — mechanical plus field — is conserved. Computing the angular momentum density $\mathbf{r}\times(\mathbf{E}\times\mathbf{B})$ of the field and showing the total is constant is the genuine relativistic content of the conservation law, and it is the reason the strong action-reaction law fails: the field carries momentum and angular momentum of its own. This connects to [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

**Selection rules in particle decay.** Conservation of total angular momentum across a decay constrains the spins and orbital angular momenta of the products, complementing energy-momentum conservation. A spin-$0$ particle decaying to two photons, for instance, has its photon polarisations correlated by angular momentum conservation. The application is out-of-distribution because it uses the conservation law as a *selection rule* in quantum kinematics rather than as a classical equation of motion.

---

# Bridges

- **[[Thm - Conservation of Four-Momentum]]** — the companion conservation law. Both are first principles for a system; both express a symmetry (translation invariance for four-momentum, Lorentz invariance for angular momentum). The change-of-origin rule $J_{C'} = J_C + \overrightarrow{C'C}^\flat\wedge P$ shows the two are intertwined: the conservation of $J$ about every point requires the conservation of $P$. Together they are the ten conserved quantities of the Poincaré group — four from translations, six from Lorentz transformations.

- **[[Thm - König Theorem (Relativistic)]]** — the change-of-origin rule, specialised to $C' = G$ (the centre of inertia), produces the König decomposition $J_C = S + \overrightarrow{CG}^\flat\wedge P$. The conservation theorem guarantees that both the spin $S$ and the orbital part are separately conserved for an isolated system, so the decomposition is stable in time.

- **[[Def - Spin Four-Vector]]** — contracting the conserved two-form $J$ with the conserved momentum $P$ through the Levi-Civita tensor gives the conserved [[Def - Spin Four-Vector|spin four-vector]]. The conservation of angular momentum is thus the source of the conservation of spin direction for an isolated body.

- **Noether's theorem** — the deep reason the many-particle law holds. Angular momentum is the Noether charge of Lorentz invariance, exactly as four-momentum is the charge of translation invariance; the explicit derivation is in [[Special Relativity XV — The Principle of Least Action]]. This is why the conservation is a first principle rather than a consequence of particle mechanics: it expresses a symmetry of nature.

---

# Unlocked by This

> [!tip] The Ten Conservation Laws of the Poincaré Group *(from Field Theory)*
> Four-momentum conservation (four laws) and angular momentum conservation (six laws) together are the **ten conservation laws** corresponding to the ten generators of the [[Def - The Poincaré Group|Poincaré group]] — four translations, three rotations, three boosts. Noether's theorem ties each to a symmetry of spacetime: homogeneity of time and space gives energy and momentum; isotropy gives angular momentum; the boost invariance gives the uniform motion of the centre of inertia. These ten quantities are the complete set of conserved charges of any Poincaré-invariant theory, and they organise the entire kinematics of isolated systems.
