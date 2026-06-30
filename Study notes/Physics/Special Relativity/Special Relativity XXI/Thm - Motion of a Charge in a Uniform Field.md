---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Lorentz Four-Force"
  - "Thm - The Electromagnetic Field Invariants"
  - "Thm - Reduction to Parallel Electric and Magnetic Fields"
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
tags: [physics, special-relativity, electromagnetism]
---

# Notation

SI units, $c$ kept. Signature $\mathrm{diag}(+1,-1,-1,-1)$. A particle of rest mass $m>0$, charge $q$, [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$ (components $u^\mu = dx^\mu/d\tau$, with $u^0 = \Gamma_{\mathcal{P}}$) moves in a *uniform* [[Def - The Electromagnetic Field Tensor|field]] $F$ (constant over spacetime) relative to an inertial observer $\mathcal{O}$. Relative to $\mathcal{O}$ the fields are $\mathbf{E}$, $\mathbf{B}$ (magnitudes $E$, $B$). The particle's velocity relative to $\mathcal{O}$ is $\mathbf{V}$; its initial speed at $\tau = 0$ is $V_0$, with $\Gamma_0 = (1 - V_0^2/c^2)^{-1/2}$. The **cyclotron frequency** is $\omega_B := qB/m$; the **synchrotron (gyration) frequency** is $\omega := \omega_B/\Gamma_0$. The **Larmor radius** is $R := \Gamma_0 V_0\sin\theta/\omega_B = P\sin\theta/(qB)$, with $P = \Gamma_0 m V_0$ the momentum and $\theta$ the pitch angle. The relativistic kinetic energy is $\mathfrak{E}_{\mathrm{kin}} = (\Gamma_{\mathcal{P}} - 1)mc^2$. The [[Thm - The Electromagnetic Field Invariants|invariants]] are $I_1 = c^2B^2 - E^2$, $I_2 = c\,\mathbf{E}\cdot\mathbf{B}$. Full registry on [[Special Relativity XXI — The Electromagnetic Field]].

---

# Statement

> **Theorem (motion in a uniform field).** A charged particle in a uniform electromagnetic field obeys the covariant equation of motion
> $$m\,\frac{dU^\mu}{d\tau} \;=\; q\,F^\mu{}_\nu\,U^\nu, \qquad\text{equivalently}\qquad \frac{dU}{d\tau} = \frac{q}{mc}\,F(\,\cdot\,,U).$$
> Its solutions are classified by the [[Thm - The Electromagnetic Field Invariants|field invariants]]:
>
> **(a) Purely magnetic field** ($\mathbf{E} = 0$): the trajectory is a **helix** about $\mathbf{B}$, of radius $|R| = P\sin\theta/(qB)$, at the **synchrotron frequency** $\omega = \omega_B/\Gamma_0$ with $\omega_B = qB/m$ the cyclotron frequency; the speed (and energy) is constant. For pitch angle $\theta = \pi/2$ (velocity $\perp\mathbf{B}$) the helix degenerates to a circle.
>
> **(b) Purely electric field** ($\mathbf{B} = 0$): the motion is **hyperbolic** (uniformly accelerated) along $\mathbf{E}$, with proper acceleration $a = qE/m$, gaining kinetic energy $\mathfrak{E}_{\mathrm{kin}} = qEz = q\,\Delta V$ over a displacement $z$ (potential difference $\Delta V$).
>
> **(c) Crossed fields** ($I_2 = 0$, $\mathbf{E}\perp\mathbf{B}$, velocity $\perp$ to both): the trajectory is a **trochoid** in the plane perpendicular to $\mathbf{B}$, governed by $\ddot u^2 + (1 - \beta^2)\omega_B^2\,u^2 = 0$ with $\beta = E/(cB)$ and $1 - \beta^2 = I_1/(c^2B^2)$ — oscillatory (cycloid/trochoid) if $I_1 > 0$ (mostly magnetic), uniformly accelerated if $I_1 < 0$, cubic-in-time if $I_1 = 0$ (null). The **Wien condition**: a particle with speed $U = E/B$ passes undeflected.

> **Corollary (the magnetic field does no work).** Only the electric field changes the particle's energy: $d\mathfrak{E}/dt = q\,\mathbf{E}\cdot\mathbf{V}$. In a purely magnetic field $\Gamma_{\mathcal{P}}$, hence the speed, is constant.

---

# Motivation

This theorem is where the abstract machinery of the field tensor and the Lorentz four-force pays off in concrete trajectories — and where the entire technology of particle accelerators is grounded. Every accelerator, from a cathode-ray tube to the Large Hadron Collider, is an exercise in pushing charged particles around with $\mathbf{E}$ and $\mathbf{B}$ fields, and the design of each rests on the three cases catalogued here.

The single most consequential fact is the corollary: *a magnetic field does no work*. Because the [[Def - The Lorentz Four-Force|Lorentz force]] is perpendicular to the velocity, a magnetic field can only bend a trajectory, never speed it up — the energy gain is always $q\,\mathbf{E}\cdot\mathbf{V}$, electric only. This is why accelerators are built with electric fields in the accelerating gaps and magnetic fields only for steering: the magnets bend the beam back through the gaps (cyclotron, synchrotron), but every joule of energy is delivered by an electric field. The relativistic kinetic-energy relation $\mathfrak{E}_{\mathrm{kin}} = q\Delta V$ — identical in form to the non-relativistic one — is the basic accounting of a linear accelerator.

The case division by [[Thm - The Electromagnetic Field Invariants|invariants]] is the organising principle. A purely magnetic field ($I_1 > 0$, $\mathbf{E}=0$) gives bounded helical motion and the cyclotron frequency; a purely electric field ($I_1 < 0$, $\mathbf{B}=0$) gives unbounded hyperbolic acceleration; crossed fields give the trochoidal motion of the Wien filter, with the qualitative character (bounded versus runaway) again set by the sign of $I_1$. By the [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction theorem]], a general non-null field can be boosted to parallel fields, where the motion separates into a magnetic (circular) part and an electric (hyperbolic) part — so these three cases, suitably combined, cover everything.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a charged particle in a uniform field."

The first disguised source is **"a particle in a static laboratory field."** Any static, spatially-uniform field in the lab qualifies; the cases are selected by which of $\mathbf{E}$, $\mathbf{B}$ is present and their relative magnitude. The bridge is recognising laboratory steering and accelerating fields as uniform fields. *Example problem:* an electron in the uniform field between capacitor plates undergoes case (b) hyperbolic acceleration; a proton in a cyclotron's dee undergoes case (a) circular motion.

The second disguised source is **"a general non-null field, reduced to parallel form."** By the [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction theorem]], an arbitrary non-null uniform field becomes parallel $\mathbf{E}'\parallel\mathbf{B}'$ in a suitable frame, where the motion is a superposition of cases (a) and (b). The bridge is the reduction. *Example problem:* a charge in arbitrary uniform $\mathbf{E}$, $\mathbf{B}$ with $I_2\ne0$ — boost to the parallel frame, get a helix with exponentially increasing pitch, boost back.

The third disguised source is **"a momentum measurement from a track radius."** In a known magnetic field, a particle's curvature radius $R$ determines its momentum via $P = qBR/\sin\theta$ — the basis of every magnetic spectrometer and bubble-chamber analysis. The bridge is the Larmor-radius formula run backwards. *Example problem:* a track of radius $R$ in a $1\,$T field has transverse momentum $P_\perp = qBR$; reading $R$ off a photograph gives the particle's momentum.

**Targets (Output Amplification)**

The conclusion is "the trajectory and frequency for each field case."

Combine the conclusion with **the energy-gain relation.** The kinetic energy gained is $q\Delta V$ regardless of the field configuration's complexity, because only $\mathbf{E}$ works. The further result is the design rule for accelerators: total energy is the sum of the potential drops the particle traverses. The combination is the engine of linear-accelerator and RF-cavity design. *Example:* SLAC's 50 GeV is the integrated potential drop over 3.2 km of accelerating cavities.

Combine the conclusion with **the resonance condition.** In a cyclotron the accelerating field must oscillate at the cyclotron frequency $\omega_B = qB/m$; but the *actual* orbital frequency is the velocity-dependent $\omega = \omega_B/\Gamma_0$, so resonance is maintained only while $\Gamma_0\approx1$. The further result is the breakdown of the simple cyclotron at relativistic energies and the need for the synchrocyclotron (ramp the frequency) or synchrotron (ramp the field). The combination explains the historical development of accelerators. *Example:* a proton cyclotron is limited to $\lesssim20\,$MeV before $\Gamma$ detunes it.

Combine the conclusion with **the fixed-radius constraint.** To keep particles on a ring of fixed radius $R$ as their momentum grows, the magnetic field must ramp as $B = P/(qR)$. The further result is the synchrotron principle and the magnet specification for a given energy. The combination is the design equation of every circular collider. *Example:* the LHC's $7\,$TeV protons on a $4.3\,$km radius need $B = P/(qR)\approx5.4\,$T (raised to $8.3\,$T for the straight sections), provided by superconducting magnets at $1.9\,$K.

---

# Why Is It True

The equation of motion is a *linear* differential equation with constant coefficients (the field is uniform, so $F^\mu{}_\nu$ is a constant matrix), and the solution is therefore an exponential — the structure of that exponential is dictated by whether the field acts as a rotation or a boost.

**The one-line mechanism: $qF^\mu{}_\nu/m$ is a constant element of the Lorentz Lie algebra $\mathfrak{so}(1,3)$, so $U(\tau) = \exp\big(\tfrac{q}{m}\tau\,\check F\big)U(0)$ is a one-parameter subgroup of $SO(1,3)$ acting on the four-velocity — a rotation if $\check F$ is magnetic-like (circular motion), a boost if it is electric-like (hyperbolic motion).**

Unpack this. The magnetic part of $F^\mu{}_\nu$ is, when an index is raised, a generator of *spatial rotations*: $\exp$ of a rotation generator is a rotation, so the four-velocity rotates in the plane perpendicular to $\mathbf{B}$ at a fixed rate. A rotation of the velocity at fixed speed is uniform circular motion — hence the helix and the cyclotron frequency. The speed is constant because a rotation preserves the norm of $\mathbf{V}$, which is the statement that the magnetic field does no work. The electric part of $F^\mu{}_\nu$ is a generator of *boosts*: $\exp$ of a boost generator is a boost, so the four-velocity is hyperbolically rotated in the time–$\mathbf{E}$ plane, which is exactly uniformly accelerated (hyperbolic) motion — the same $x^2 - c^2t^2 = \text{const}$ worldline as a [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]], with proper acceleration $qE/m$. The two cases are the two types of one-parameter subgroup of the Lorentz group: elliptic (rotation, bounded) and hyperbolic (boost, unbounded).

For crossed fields, the sign of $I_1 = c^2B^2 - E^2$ decides which character dominates. The master equation $\ddot u^2 + (1-\beta^2)\omega_B^2 u^2 = 0$ is a harmonic oscillator with "frequency squared" $(1-\beta^2)\omega_B^2 = I_1\omega_B^2/(c^2B^2)$. If $I_1 > 0$ this is positive — oscillatory motion, a trochoid; the field is "mostly magnetic" and there is a frame ($U = E/B$) where it is purely magnetic, with circular motion. If $I_1 < 0$ the "frequency squared" is negative — the solutions are hyperbolic, runaway acceleration; the field is "mostly electric". If $I_1 = 0$ the equation is $\ddot u^2 = 0$, marginal, giving polynomial (cubic-in-time) growth — the null field. The reduction theorem makes this transparent: in the rest frame of the appropriate observer the field is pure, and the motion is manifestly circular or hyperbolic.

The Wien condition drops out of force balance: a particle moving at $\mathbf{V}$ through crossed $\mathbf{E}\perp\mathbf{B}$ feels $q(\mathbf{E} + \mathbf{V}\times\mathbf{B})$, which vanishes when $|\mathbf{V}| = E/B$ (and $\mathbf{V}$ is oriented so $\mathbf{V}\times\mathbf{B} = -\mathbf{E}$). At that speed the electric and magnetic forces cancel and the particle goes straight — equivalently, it is the speed of the frame in which the field is purely magnetic, where a particle at rest feels no force.

---

# What Makes This Hard

The conceptual trap is conflating the cyclotron frequency $\omega_B = qB/m$ (a constant, depending only on the field and the charge-to-mass ratio) with the actual orbital frequency $\omega = \omega_B/\Gamma_0$ (velocity-dependent): the relativistic mass increase slows the gyration, and this detuning is *the* reason simple cyclotrons fail at high energy — missing it makes the whole accelerator story incoherent. The computational difficulty is that the coupled equations of motion (17.59) require recognising the decoupling into a hyperbolic pair (time and $\mathbf{E}$-direction) and a circular pair (the two directions $\perp\mathbf{B}$); students often try to solve all four together. For crossed fields, the subtlety is that the qualitative behaviour flips at $I_1 = 0$ — the same equation gives bounded, marginal, or runaway motion depending on the sign of a single invariant, and the null case is easy to overlook.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write the equation of motion in components in a frame adapted to the field. For parallel fields along $e_3$, the four equations decouple into a hyperbolic pair $(u^0, u^3)$ driven by $E$ and a circular pair $(u^1, u^2)$ driven by $B$. Solve each pair (exponential / trigonometric), apply initial conditions, and integrate $dx^\mu/d\tau = u^\mu$ to get the trajectory. For crossed fields, derive the second-order equation for $u^2$ and read off the case by the sign of $1-\beta^2 = I_1/(c^2B^2)$.

**Subgoal decomposition:**

1. **Write the equation of motion in an adapted frame.** For $\mathbf{E} = E\,e_3$, $\mathbf{B} = B\,e_3$, the components of $m\dot U = qF(\cdot,U)$ split into $(\dot u^0, \dot u^3)$ coupled by $qE/(mc)$ and $(\dot u^1, \dot u^2)$ coupled by $\omega_B = qB/m$.
   - *Hint:* Use the antidiagonal block form of $F$ for parallel fields.
   - *Why needed:* It exhibits the decoupling that makes the problem solvable.

2. **Solve the magnetic (circular) pair.** $\dot u^1 = \omega_B u^2$, $\dot u^2 = -\omega_B u^1$ give $u^1 + iu^2 \propto e^{-i\omega_B\tau}$ — rotation at the cyclotron frequency.
   - *Hint:* This is a 2D harmonic oscillator; the speed in the plane is constant.
   - *Why needed:* It produces the circular/helical part and the frequency.

3. **Solve the electric (hyperbolic) pair.** $\dot u^0 = (qE/mc)u^3$, $\dot u^3 = (qE/mc)u^0$ give $u^0, u^3 \propto \cosh, \sinh$ of $(qE/mc)\tau$ — boost at proper acceleration $a = qE/(mc^2)\cdot c$.
   - *Hint:* This is the hyperbolic-motion equation; compare [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)]].
   - *Why needed:* It produces the accelerated part and the energy gain.

4. **Integrate to the trajectory and extract the physics.** Integrate $u^\mu = dx^\mu/d\tau$; read off the Larmor radius $R = P\sin\theta/(qB)$, the synchrotron frequency $\omega = \omega_B/\Gamma_0$, and $\mathfrak{E}_{\mathrm{kin}} = qEz$.
   - *Hint:* The radius is velocity over angular frequency; energy is force times distance.
   - *Why needed:* It delivers the quantities used in accelerator design.

For crossed fields: derive $\ddot u^2 + (1-\beta^2)\omega_B^2 u^2 = 0$ by differentiating the $u^2$ equation and substituting; the sign of $1-\beta^2 = I_1/(c^2B^2)$ classifies the motion (oscillatory / runaway / marginal).

---

# Lemma Decomposition

> [!note]- Lemma 1: The equation of motion decouples for parallel fields
> **Statement:** For $\mathbf{E} = E\,e_3$, $\mathbf{B} = B\,e_3$, the equation $m\dot U^\mu = qF^\mu{}_\nu U^\nu$ separates into $\dot u^0 = \tfrac{qE}{mc}u^3$, $\dot u^3 = \tfrac{qE}{mc}u^0$ and $\dot u^1 = \omega_B u^2$, $\dot u^2 = -\omega_B u^1$.
>
> **Hint:** Insert the antidiagonal (parallel-field) component matrix of $F$ into the equation of motion.
>
> **Why needed:** The decoupling is what reduces the problem to two solvable 2D systems.
>
> > [!note]- Full proof
> > For parallel fields along $e_3$, the nonzero components of $F$ are $F_{03} = E$ (electric, along $e_3$) and $F_{12} = -cB$ (magnetic, in the $e_1e_2$ plane). Raising indices, $F^0{}_3 = E$, $F^3{}_0 = E$, $F^1{}_2 = \omega_B mc/q\cdot$-type entries, concretely $F^1{}_2 = -cB$, $F^2{}_1 = cB$ (mostly-minus). The equation $m\dot u^\mu = qF^\mu{}_\nu u^\nu$ then reads, component by component: $m\dot u^0 = qF^0{}_3 u^3 = qE u^3$, $m\dot u^3 = qE u^0$ (hyperbolic pair); $m\dot u^1 = qF^1{}_2 u^2 = qB u^2$, $m\dot u^2 = -qB u^1$ (circular pair, with $\omega_B = qB/m$). The pairs share no variables. $\blacksquare$

> [!note]- Lemma 2: The magnetic pair gives circular motion at ω_B
> **Statement:** $\dot u^1 = \omega_B u^2$, $\dot u^2 = -\omega_B u^1$ have solution $u^1 + iu^2 = (u^1(0)+iu^2(0))e^{-i\omega_B\tau}$; the speed in the $e_1e_2$ plane is constant.
>
> **Hint:** Combine into a single complex equation $\dot w = -i\omega_B w$ with $w = u^1 + iu^2$.
>
> **Why needed:** It is the circular/helical part and yields the cyclotron frequency and Larmor radius.
>
> > [!note]- Full proof
> > Set $w = u^1 + iu^2$. Then $\dot w = \dot u^1 + i\dot u^2 = \omega_B u^2 - i\omega_B u^1 = -i\omega_B(u^1 + iu^2) = -i\omega_B w$, so $w(\tau) = w(0)e^{-i\omega_B\tau}$. Hence $|w|^2 = (u^1)^2 + (u^2)^2$ is constant: the transverse speed is fixed. Integrating $dx/d\tau = c u^1$, $dy/d\tau = c u^2$ gives a circle of radius $R = c|w|/\omega_B = \Gamma_0 V_0\sin\theta/\omega_B = P\sin\theta/(qB)$ (using $c|w| = \Gamma_0 V_0\sin\theta$ for the transverse velocity and $P = \Gamma_0 m V_0$). The angular frequency *in coordinate time* $t = \Gamma_0\tau$ is $\omega = \omega_B/\Gamma_0$. $\blacksquare$

> [!note]- Lemma 3: The electric pair gives hyperbolic motion
> **Statement:** $\dot u^0 = \tfrac{qE}{mc}u^3$, $\dot u^3 = \tfrac{qE}{mc}u^0$ have solution $u^0 = \Gamma_0\cosh(a\tau/c\cdot c)$-type, i.e. uniformly accelerated motion with proper acceleration $a = qE/m$.
>
> **Hint:** The pair is the hyperbolic analogue of Lemma 2; solutions are $\cosh$, $\sinh$.
>
> **Why needed:** It is the accelerated part and gives the energy-gain relation.
>
> > [!note]- Full proof
> > Set $s = u^0 + u^3$, $d = u^0 - u^3$. Then $\dot s = \tfrac{qE}{mc}s$, $\dot d = -\tfrac{qE}{mc}d$, so $s\propto e^{qE\tau/mc}$, $d\propto e^{-qE\tau/mc}$, hence $u^0 = A\cosh(qE\tau/mc) + B\sinh(\cdots)$ and $u^3$ similarly. Starting from rest ($V_0 = 0$, $u^0(0)=1$, $u^3(0)=0$): $u^0 = \cosh(qE\tau/mc)$, $u^3 = \sinh(qE\tau/mc)$. Integrating $dz/d\tau = cu^3$ gives $z = \tfrac{mc^2}{qE}[\cosh(qE\tau/mc) - 1]$, and $cdt/d\tau = u^0$ gives $ct = \tfrac{mc^2}{qE}\sinh(qE\tau/mc)$; eliminating $\tau$ yields the hyperbola $(z + \tfrac{mc^2}{qE})^2 - (ct)^2 = (\tfrac{mc^2}{qE})^2$. The proper acceleration is $a = qE/m$, matching [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|hyperbolic motion]]. The kinetic energy is $\mathfrak{E}_{\mathrm{kin}} = (u^0-1)mc^2 = qEz$ (using $az = \cosh - 1$ with $a = qE/mc^2$). $\blacksquare$

> [!note]- Lemma 4: Crossed fields give the master oscillator equation
> **Statement:** For $\mathbf{E} = E\,e_y$, $\mathbf{B} = B\,e_z$, $\mathbf{V}_0 = V_0 e_x$, the transverse component obeys $\ddot u^2 + (1-\beta^2)\omega_B^2 u^2 = 0$ with $\beta = E/(cB)$ and $1-\beta^2 = I_1/(c^2B^2)$.
>
> **Hint:** Differentiate the $u^2$ equation of motion and substitute the $u^0$, $u^1$ equations.
>
> **Why needed:** Its "frequency squared" $\propto I_1$ classifies the crossed-field motion into the three cases.
>
> > [!note]- Full proof
> > With $\beta = E/(cB)$, the equations of motion (source Eq. (17.81)) are $\dot u^0 = \beta\omega_B u^2$, $\dot u^1 = \omega_B u^2$, $\dot u^2 = \omega_B(\beta u^0 - u^1)$, $\dot u^3 = 0$. Differentiate the third: $\ddot u^2 = \omega_B(\beta\dot u^0 - \dot u^1) = \omega_B(\beta\cdot\beta\omega_B u^2 - \omega_B u^2) = -\omega_B^2(1-\beta^2)u^2$. Hence $\ddot u^2 + (1-\beta^2)\omega_B^2 u^2 = 0$. Since $I_1 = c^2B^2 - E^2 = c^2B^2(1-\beta^2)$, the coefficient is $(1-\beta^2)\omega_B^2 = I_1\omega_B^2/(c^2B^2)$: positive (oscillatory) for $I_1>0$, zero (marginal/cubic) for $I_1=0$, negative (hyperbolic/runaway) for $I_1<0$. The Wien condition $U = E/B$ ($\beta = U/c$) makes the magnetic and electric forces cancel for a particle at that speed. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> The equation of motion is the [[Def - The Lorentz Four-Force|Lorentz four-force]] law $m\,dU^\mu/d\tau = qF^\mu{}_\nu U^\nu$, with $F$ uniform so $F^\mu{}_\nu$ is a constant matrix.
>
> **(a) Purely magnetic ($\mathbf{E}=0$).** By Lemma 1 (with $E=0$) the $(u^0,u^3)$ pair is constant ($u^0 = \Gamma_0$, $u^3 = \Gamma_0 V_0\cos\theta/c$) and by Lemma 2 the $(u^1,u^2)$ pair rotates at $\omega_B$. Integrating, the trajectory is a helix of radius $R = P\sin\theta/(qB)$ about $\mathbf{B}$, advancing uniformly along $\mathbf{B}$; the orbital frequency in coordinate time is $\omega = \omega_B/\Gamma_0$. Since $u^0 = \Gamma_0$ is constant, the energy is constant: the magnetic field does no work.
>
> **(b) Purely electric ($\mathbf{B}=0$).** By Lemma 3 the $(u^0,u^3)$ pair is hyperbolic; starting from rest, the worldline is the hyperbola of proper acceleration $a = qE/m$, and the kinetic energy gained over displacement $z$ is $\mathfrak{E}_{\mathrm{kin}} = qEz = q\Delta V$.
>
> **(c) Crossed fields ($I_2=0$, $\mathbf{E}\perp\mathbf{B}$).** By Lemma 4 the transverse motion obeys $\ddot u^2 + (1-\beta^2)\omega_B^2 u^2 = 0$. For $I_1>0$ ($\beta<1$) the solution is sinusoidal and the trajectory a trochoid; by the [[Thm - Reduction to Parallel Electric and Magnetic Fields|reduction theorem]] there is a frame ($U = E/B$) where the field is purely magnetic and the motion is the circle of case (a). For $I_1<0$ ($\beta>1$) the solution is hyperbolic (runaway), with a purely-electric frame at $U = c^2B/E$. For $I_1 = 0$ ($\beta=1$, null field) the equation is $\ddot u^2 = 0$ and the trajectory is cubic in proper time. The Wien condition: at speed $U = E/B$ the Lorentz force $q(\mathbf{E}+\mathbf{V}\times\mathbf{B})$ vanishes, so the particle is undeflected.
>
> **Corollary.** The temporal component of the equation of motion is $d\mathfrak{E}/dt = q\,\mathbf{E}\cdot\mathbf{V}$ (from the [[Def - The Lorentz Four-Force|Lorentz force]]); with $\mathbf{E}=0$ this is zero, so $\Gamma_{\mathcal{P}}$ and the speed are constant. Only the electric field changes the energy. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Magnetic spectrometry and momentum measurement.** A charged particle's track in a known magnetic field has curvature radius $R = P_\perp/(qB)$, so measuring $R$ (from a bubble-chamber photograph or a tracking detector) yields the momentum. This is how every particle physics detector measures momentum, and the relativistic formula (with $P = \Gamma m V$, not $mV$) is essential at high energy. The application turns the theorem into a measurement tool.

**The cyclotron resonance condition and its relativistic breakdown.** Show that a simple cyclotron, with a fixed-frequency accelerating field, falls out of resonance once the particle's $\Gamma$ departs appreciably from $1$, because the orbital frequency is $\omega = \omega_B/\Gamma$. This forces the synchrocyclotron (ramped frequency) and the synchrotron (ramped field). The application is the historical logic of accelerator development, derivable from the frequency formula.

**The Wien filter as a velocity selector.** Crossed $\mathbf{E}\perp\mathbf{B}$ pass only particles of speed $U = E/B$ undeflected; tuning $E/B$ selects a velocity. Combined with a subsequent magnetic momentum analysis, this separates particles by mass (a velocity-plus-momentum filter is a mass filter). The application connects the crossed-field motion to mass spectrometry.

**Synchrotron radiation power.** A relativistic charge on a circular orbit radiates; the radiated power (relativistic Larmor formula) scales as $\Gamma^4$, which limits electron synchrotrons and is exploited in synchrotron light sources. Computing the energy loss per turn and the magnet field needed to compensate connects this theorem to [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy|radiation theory]]. The application is the reason electron colliders are linear at the highest energies.

---

# Bridges

- **[[Def - The Lorentz Four-Force]]** — the equation of motion is the Lorentz four-force law; the case division (rotation versus boost) reflects whether the constant matrix $qF^\mu{}_\nu/m$ is magnetic-like (a rotation generator) or electric-like (a boost generator) in the Lorentz Lie algebra. The corollary "$\mathbf{B}$ does no work" is the purity $f\cdot U = 0$ read in the temporal component.

- **[[Def - Uniformly Accelerated Observer (Hyperbolic Motion)]]** — the purely-electric case is *exactly* hyperbolic motion: a charge starting from rest in a uniform $\mathbf{E}$ follows the same worldline $x^2 - c^2t^2 = (mc^2/qE)^2$ as a uniformly accelerated observer with proper acceleration $a = qE/m$. The electric field is a constant-proper-acceleration machine.

- **[[Thm - The Electromagnetic Field Invariants]]** — the qualitative motion in crossed fields is governed by the sign of $I_1$ through the master equation's coefficient $(1-\beta^2)\omega_B^2 = I_1\omega_B^2/(c^2B^2)$: oscillatory, marginal, or runaway as $I_1$ is positive, zero, or negative. The invariant predicts the trajectory's character before any integration.

- **[[Thm - Reduction to Parallel Electric and Magnetic Fields]]** — for a general non-null field, reduce to parallel fields, where the motion separates into the circular (case a) and hyperbolic (case b) parts; the general trajectory is their superposition, boosted back. The reduction makes the general case a combination of the two simple ones.

- **The one-parameter subgroups of the Lorentz group** — circular motion is the action of an elliptic (rotation) one-parameter subgroup on the four-velocity; hyperbolic motion is a hyperbolic (boost) subgroup. The trajectory types are the [[Special Relativity X — The Lorentz Group as a Lie Group|Lie-group]] orbit types, with the field as the algebra element.

---

# Unlocked by This

> [!tip] Particle Accelerators *(from Accelerator Physics)*
> The three cases are the building blocks of all accelerators: the **linac** (case b, energy gain $q\Delta V$ in successive cavities), the **cyclotron** (case a, constant $\omega_B$, limited to $\Gamma\approx1$), the **synchrocyclotron** (ramp the frequency as $\omega = \omega_B/\Gamma$), and the **synchrotron** (ramp the field as $B = P/(qR)$ to hold a fixed radius). The LHC, a synchrotron, needs $8.3\,$T superconducting magnets to bend $7\,$TeV protons on a $4.3\,$km radius. **Storage rings** hold pre-accelerated particles for collisions or to harvest synchrotron radiation.

> [!tip] Guiding-Centre Motion and Magnetic Confinement *(from Plasma Physics)*
> In a strong magnetic field a charged particle executes rapid gyration at $\omega_B$ about a slowly drifting **guiding centre**; superimposed electric or inhomogeneous fields produce the $\mathbf{E}\times\mathbf{B}$, gradient, and curvature drifts. This separation of fast gyration from slow drift, with the Larmor radius $R = P_\perp/(qB)$ as the small parameter, is the foundation of magnetic-confinement fusion and of the dynamics of the Van Allen belts and the solar wind.

> [!tip] The Penning Trap and Precision Measurement *(from Atomic Physics)*
> A static magnetic field plus a quadrupole electric field — a **Penning trap** — confines a single charged particle, whose cyclotron and axial frequencies can be measured to extraordinary precision. This yields the most accurate measurements of the electron and proton magnetic moments and mass ratios, and the cleanest tests of QED, all resting on the cyclotron frequency $\omega_B = qB/m$ of this theorem.
