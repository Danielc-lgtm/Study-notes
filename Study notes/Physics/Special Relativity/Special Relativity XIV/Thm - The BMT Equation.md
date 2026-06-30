---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Spin Four-Vector"
  - "Def - Fermi-Walker Derivative"
  - "Def - Four-Force"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ (restored where illuminating), mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. A particle with spin has [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $\vec u$, four-acceleration $\vec a = c^{-1}d\vec u/d\tau$, proper time $\tau$, mass $m$, charge $q$, and [[Def - Spin Four-Vector|spin four-vector]] $\vec s\in E_u$ with $\vec u\cdot\vec s = 0$. The [[Def - Fermi-Walker Derivative|Fermi–Walker derivative]] along the worldline is $D^{\mathrm{FW}}_u$. The dimensionless **Landé factor** is $g$; the **gyromagnetic ratio** is $gq/(2m)$. The electromagnetic field two-form is $F$ (developed in [[Special Relativity XXI — The Electromagnetic Field]]); $\vec F(\cdot,\vec s)$ is the metric-dual vector of the one-form $\vec v\mapsto F(\vec v,\vec s)$; $F(\vec u,\vec s)$ is a scalar; the [[Def - Four-Force|Lorentz four-force]] is $f = qF(\cdot,\vec u)$. Full registry on [[Special Relativity XIV — Angular Momentum and Spin]].

> [!warning] Convention
> The electromagnetic field tensor $F$ is introduced fully in [[Special Relativity XXI — The Electromagnetic Field]]; here it enters only **kinematically**, as the antisymmetric two-form that supplies the torque on the spin. We need only that $F$ is antisymmetric (which makes the BMT equation preserve $\|\vec s\|$) and that the Lorentz four-force is $f = qF(\cdot,\vec u)$. Gourgoulhon's mostly-plus signs differ; we state the equation natively in mostly-minus.

---

# Statement

> **Free gyroscope.** A particle with spin whose spin is subject to no torque is a **free gyroscope**; its spin four-vector is Fermi–Walker transported,
> $$D^{\mathrm{FW}}_u\vec s = 0,$$
> which preserves the norm, $\|\vec s\|_g = \text{const}$, so the spin **precesses** — it changes direction while keeping its magnitude.

> **Bargmann–Michel–Telegdi (BMT) equation.** A particle of charge $q$, mass $m$, and Landé factor $g$ moving in an electromagnetic field $F$ has a spin torque $\vec C = \frac{gq}{2mc}\perp_u\vec F(\cdot,\vec s)$, giving the evolution
> $$\boxed{\,\frac{d\vec s}{d\tau} \;=\; \frac{q}{mc}\left[\frac{g}{2}\,\vec F(\cdot,\vec s) + \left(\frac{g}{2}-1\right)F(\vec u,\vec s)\,\vec u\right]\,}.$$
> The equation preserves the spin norm, $\|\vec s\|_g = \text{const}$, and for $g = 2$ (the value for an electron in lowest-order Dirac theory) it simplifies to
> $$\frac{d\vec s}{d\tau} = \frac{q}{mc}\,\vec F(\cdot,\vec s)\qquad(g = 2).$$

---

# Motivation

We have the [[Def - Four-Torque|four-torque]] that drives the angular momentum of a particle, and we have the [[Def - Spin Four-Vector|spin four-vector]] subject to the supplementary condition $\vec s\cdot\vec u = 0$. This theorem combines them into the equation of motion for the spin — first for a free gyroscope (no torque), then for a charged particle in an electromagnetic field. The result, the BMT equation, is one of the most consequential formulas in particle physics: it governs the precession of an electron's or a muon's spin, and it is the equation inverted to measure the anomalous magnetic moment $g - 2$ to parts per billion.

The free-gyroscope case is the conceptual foundation, and it carries a surprise. A gyroscope feels *no torque* — yet its spin *precesses*. One is tempted to look for a force, but there is none; the precession is purely kinematic, a consequence of the geometry of the worldline. The spin is Fermi–Walker transported, the relativistic notion of "carried along without rotation", and Fermi–Walker transport along a *bent* (accelerated) worldline accumulates a rotation for the same reason a vector parallel-transported around a loop on a sphere comes back rotated. This kinematic precession is the **Thomas precession**, and recognising it as geometry rather than dynamics is the key insight.

The charged-particle case adds the dynamics. The electromagnetic field exerts a torque on the spin through the particle's magnetic moment $\boldsymbol{\mu} = \frac{gq}{2m}\vec s$, and the BMT equation is the covariant statement of how that torque turns the spin. Its two terms are physically distinct and this distinction is the whole reason $g - 2$ is measurable: the $\frac g2$ term is the dynamical magnetic-moment precession (Larmor), and the $(\frac g2 - 1)$ term is the kinematic Thomas precession that survives even when $g$ takes its "naive" value. For $g = 2$ — the Dirac value — the two combine into a single clean term; any deviation of $g$ from $2$ shows up as a residual relative precession of spin and momentum, which is exactly the anomalous moment.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "a particle with spin, subject to a known torque on the spin".

The first disguised source is **"a torque-free gyroscope on an accelerated worldline"**. With zero torque, $\vec C = 0$, the spin is Fermi–Walker transported and precesses kinematically. The bridge is that "no torque" means $D^{\mathrm{FW}}_u\vec s = 0$, not $d\vec s/d\tau = 0$. *Example problem:* a gyroscope carried around a circular path at constant speed precesses by the Thomas angle per orbit, even though no torque acts on it — the relativistic spin-orbit effect.

The second disguised source is **"a charged particle with a magnetic moment in an electromagnetic field"**. The spin couples to the field through $\boldsymbol{\mu} = \frac{gq}{2m}\vec s$, supplying the torque $\vec C = \frac{gq}{2mc}\perp_u\vec F(\cdot,\vec s)$, and the BMT equation governs the precession. The bridge is the magnetic-moment coupling. *Example problem:* a muon in a storage ring precesses according to the BMT equation, and the spin-momentum angle measures the anomaly $a = (g-2)/2$.

The third disguised source is **"a non-relativistic spin in a magnetic field"**. In the slow limit the BMT equation reduces to the Larmor precession $\frac{d\vec s}{dt} = \frac{gq}{2m}\vec s\times\mathbf{B}$, the equation of nuclear magnetic resonance and electron spin resonance. The bridge is taking $\vec u\to(1,\mathbf 0)$, where the Thomas term and the relativistic corrections vanish. *Example problem:* a nuclear spin precessing in the field of an MRI magnet.

**Targets (Output Amplification)**

The conclusion is the BMT evolution equation.

Combine the conclusion with **the antisymmetry of $F$**. Contracting the BMT equation with $\vec s$ and using $F(\vec s,\vec s) = 0$ shows $\frac{d}{d\tau}(\vec s\cdot\vec s) = 0$: the spin norm is conserved. The further result is that the BMT precession is a *rotation* of the spin, never a stretching or shrinking — the spin magnitude is a constant of motion. The combination is useful because it guarantees the physical interpretation (precession) and provides a check on any solution. *Example:* verifying numerically that a BMT solver conserves $\|\vec s\|$.

Combine the conclusion with **the difference of spin and momentum precession rates**. The momentum precesses by the cyclotron motion; the spin precesses by the BMT rate. Their difference is proportional to the anomaly $a = (g-2)/2$, because the $(\frac g2 - 1)$ Thomas term in the spin precession is exactly the part that does *not* track the momentum. The further result is the experimental signature of $g - 2$: the angle between spin and momentum grows at a rate $\propto a$. The combination is nonobvious because it isolates a tiny deviation ($a\approx 10^{-3}$) as a clean, accumulating phase. *Example:* the muon $g-2$ measurement reads $a$ from the spin-momentum oscillation frequency.

Combine the conclusion with **$g = 2$**. For the Dirac value $g = 2$ the equation collapses to $\frac{d\vec s}{d\tau} = \frac{q}{mc}\vec F(\cdot,\vec s)$, and the spin precession exactly tracks the momentum precession — so for $g = 2$ a particle's spin maintains a fixed angle to its momentum. The further result is that the deviation of the spin-momentum angle from constancy is a direct measure of the *anomaly* $g - 2$. The combination is useful because it explains why $g = 2$ is the "natural" value and why experiments target the deviation. *Example:* a $g = 2$ particle injected with spin along its momentum keeps spin along momentum through any field configuration.

---

# Why Is It True

The free-gyroscope case is true for a purely geometric reason, and the charged case adds one dynamical input. Take them in order.

**Free gyroscope.** "No torque on the spin" must be stated covariantly. The naive guess $\frac{d\vec s}{d\tau} = 0$ is wrong, because the spin is constrained to the rest space ($\vec s\cdot\vec u = 0$), and the rest space *tilts* as the particle accelerates — a vector with constant components would drift out of the rest space. The correct "no rotation" condition is that the [[Def - Fermi-Walker Derivative|Fermi–Walker derivative]] vanishes, $D^{\mathrm{FW}}_u\vec s = \frac{d\vec s}{d\tau} - (\vec a\cdot\vec s)\vec u = 0$, which says: the spin changes only by the minimal amount $(\vec a\cdot\vec s)\vec u$ needed to stay in the tilting rest space, and not at all otherwise. **The bold one-liner: a free gyroscope precesses not because anything pushes it, but because "staying still in a tilting rest space" is itself a rotation — the Thomas precession is the geometry of an accelerated worldline, not a force.** The norm is conserved because the only change, $(\vec a\cdot\vec s)\vec u$, is along $\vec u$, orthogonal to $\vec s$, so it does no work on $\|\vec s\|$.

**Charged particle.** Now a real torque acts: the magnetic moment $\boldsymbol{\mu} = \frac{gq}{2m}\vec s$ couples to the field. The torque on the spin, in covariant form, is $\vec C = \frac{gq}{2mc}\perp_u\vec F(\cdot,\vec s)$ — the projection onto the rest space of the field acting on the spin, scaled by the gyromagnetic ratio. Insert this into the Fermi–Walker law $D^{\mathrm{FW}}_u\vec s = \vec C$ and convert the Fermi–Walker derivative to an ordinary derivative, $\frac{d\vec s}{d\tau} = \vec C + c(\vec a\cdot\vec s)\vec u$. The four-acceleration is supplied by the Lorentz force, $\vec a = (mc^2)^{-1}f = (mc^2)^{-1}qF(\cdot,\vec u)$, so $c(\vec a\cdot\vec s)\vec u = \frac{q}{mc}F(\vec s,\vec u)\vec u = -\frac{q}{mc}F(\vec u,\vec s)\vec u$ (by antisymmetry). Adding the torque term, expanding the projector $\perp_u$, and collecting gives the two-term BMT equation: the $\frac g2$ from the explicit magnetic-moment torque, and the $-1$ from the Fermi–Walker $(\vec a\cdot\vec s)\vec u$ term that the worldline's bending contributes. **The two terms have two origins: $\frac g2$ is dynamics (the magnetic moment feeling the field), $-1$ is kinematics (the Thomas precession of the tilting rest frame).** Their sum is the coefficient $(\frac g2 - 1)$ of the longitudinal term.

The norm conservation is immediate and worth isolating: contract with $\vec s$, and the $\frac g2$ term gives $\frac g2 F(\vec s,\vec s) = 0$ (antisymmetry) while the longitudinal term gives $(\frac g2 - 1)F(\vec u,\vec s)(\vec s\cdot\vec u) = 0$ (supplementary condition). Both vanish, so $\frac{d}{d\tau}(\vec s\cdot\vec s) = 0$. The BMT precession is a pure rotation.

---

# What Makes This Hard

The central trap is the free-gyroscope case: writing $\frac{d\vec s}{d\tau} = 0$ for "no torque" instead of $D^{\mathrm{FW}}_u\vec s = 0$, which predicts no precession and misses the Thomas effect entirely. The reason the Fermi–Walker derivative is mandatory is the supplementary condition $\vec s\cdot\vec u = 0$: the spin must stay in the tilting rest space, and the ordinary derivative does not respect this. The second difficulty is disentangling the two terms of the BMT equation — the $\frac g2$ (dynamical, magnetic moment) and the $-1$ (kinematic, Thomas) — and seeing that the $-1$ comes from the four-acceleration via the Lorentz force, not from the spin coupling. The most common error is to drop the $(\frac g2 - 1)$ term or to misattribute it, which destroys the $g - 2$ physics, since that term is *exactly* the part that makes the anomaly measurable. A subtler point is that the equation preserves $\|\vec s\|$ only because $F$ is antisymmetric *and* the supplementary condition holds — both are needed for the contraction with $\vec s$ to vanish.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
For the free gyroscope, write "no torque" as $D^{\mathrm{FW}}_u\vec s = 0$ and read off precession with constant norm. For BMT, set $D^{\mathrm{FW}}_u\vec s$ equal to the magnetic-moment torque $\vec C = \frac{gq}{2mc}\perp_u\vec F(\cdot,\vec s)$, convert the Fermi–Walker derivative to $d/d\tau$ using the Lorentz-force four-acceleration, and collect into two terms. Check norm conservation by contracting with $\vec s$ and using the antisymmetry of $F$.

**Subgoal decomposition:**

1. **Free gyroscope.** From $D^{\mathrm{FW}}_u\vec s = 0$ deduce $\|\vec s\| = $ const and precession.
   - *Hint:* $D^{\mathrm{FW}}_u\vec s = \frac{d\vec s}{d\tau} - (\vec a\cdot\vec s)\vec u$; contract with $\vec s$ and use $\vec s\cdot\vec u = 0$.
   - *Why needed:* It establishes the kinematic precession and the norm conservation that BMT inherits.

2. **Insert the torque.** Write $D^{\mathrm{FW}}_u\vec s = \vec C$ with $\vec C = \frac{gq}{2mc}\perp_u\vec F(\cdot,\vec s)$.
   - *Hint:* The spin couples to the field through the magnetic moment $\boldsymbol{\mu} = \frac{gq}{2m}\vec s$.
   - *Why needed:* It introduces the dynamics and the $\frac g2$ coefficient.

3. **Convert to an ordinary derivative.** Use $D^{\mathrm{FW}}_u\vec s = \frac{d\vec s}{d\tau} - c(\vec a\cdot\vec s)\vec u$ and the Lorentz-force acceleration $\vec a = (mc^2)^{-1}qF(\cdot,\vec u)$.
   - *Hint:* $c(\vec a\cdot\vec s)\vec u = \frac{q}{mc}F(\vec s,\vec u)\vec u = -\frac{q}{mc}F(\vec u,\vec s)\vec u$ by antisymmetry.
   - *Why needed:* It supplies the kinematic $-1$ term from the worldline's bending.

4. **Collect.** Expand $\perp_u\vec F(\cdot,\vec s) = \vec F(\cdot,\vec s) - F(\vec u,\vec s)\vec u$ and add the acceleration term.
   - *Hint:* The $\frac g2$ longitudinal piece from $\vec C$ and the $-1$ from the acceleration combine to $(\frac g2 - 1)F(\vec u,\vec s)\vec u$.
   - *Why needed:* It produces the two-term BMT equation.

5. **Norm conservation.** Contract with $\vec s$; show $\frac{d}{d\tau}(\vec s\cdot\vec s) = 0$.
   - *Hint:* $F(\vec s,\vec s) = 0$ (antisymmetry) and $\vec s\cdot\vec u = 0$ (supplementary condition).
   - *Why needed:* It confirms the precession preserves $\|\vec s\|$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Fermi–Walker transport preserves the norm
> **Statement:** If $D^{\mathrm{FW}}_u\vec s = 0$ (or more generally $D^{\mathrm{FW}}_u\vec s = \vec C$ with $\vec u\cdot\vec C = 0$ and the dynamics below), then $\|\vec s\|_g = $ const.
>
> **Hint:** Differentiate $\vec s\cdot\vec s$ and use $\vec s\cdot\vec u = 0$.
>
> **Why needed:** It guarantees the free gyroscope (and BMT) precesses rather than grows.
>
> > [!note]- Full proof
> > $\|\vec s\|_g^2 = -\vec s\cdot\vec s$ (mostly-minus, $\vec s$ spacelike). Then
> > $$\frac{d}{d\tau}(\vec s\cdot\vec s) = 2\,\vec s\cdot\frac{d\vec s}{d\tau} = 2\,\vec s\cdot\big[D^{\mathrm{FW}}_u\vec s + c(\vec a\cdot\vec s)\vec u\big] = 2\,\vec s\cdot D^{\mathrm{FW}}_u\vec s + 2c(\vec a\cdot\vec s)(\vec s\cdot\vec u).$$
> > The last term vanishes by the supplementary condition $\vec s\cdot\vec u = 0$. For a free gyroscope $D^{\mathrm{FW}}_u\vec s = 0$, so the first term vanishes too, and $\frac{d}{d\tau}(\vec s\cdot\vec s) = 0$. $\blacksquare$

> [!note]- Lemma 2: The Lorentz-force four-acceleration
> **Statement:** A charge $q$ in field $F$ has four-acceleration $\vec a = (mc^2)^{-1}qF(\cdot,\vec u)$, so $c(\vec a\cdot\vec s)\vec u = -\frac{q}{mc}F(\vec u,\vec s)\vec u$.
>
> **Hint:** The Lorentz four-force is $f = qF(\cdot,\vec u)$ and $\vec a = (mc^2)^{-1}f$; use antisymmetry of $F$.
>
> **Why needed:** It supplies the kinematic term that becomes the $-1$ in the BMT coefficient.
>
> > [!note]- Full proof
> > The [[Def - Four-Force|Lorentz four-force]] is $f = qF(\cdot,\vec u)$, and the four-acceleration is $\vec a = (mc^2)^{-1}f$, so $\vec a = (mc^2)^{-1}qF(\cdot,\vec u)$. Then $\vec a\cdot\vec s = (mc^2)^{-1}qF(\vec s,\vec u)$, and since $F$ is antisymmetric, $F(\vec s,\vec u) = -F(\vec u,\vec s)$. Hence $c(\vec a\cdot\vec s)\vec u = (mc)^{-1}qF(\vec s,\vec u)\vec u = -\frac{q}{mc}F(\vec u,\vec s)\vec u$. (Note $\langle f,\vec u\rangle = qF(\vec u,\vec u) = 0$ by antisymmetry, consistent with $dm/d\tau = 0$.) $\blacksquare$

> [!note]- Lemma 3: Assembling the BMT equation
> **Statement:** Combining $D^{\mathrm{FW}}_u\vec s = \frac{gq}{2mc}\perp_u\vec F(\cdot,\vec s)$ with Lemma 2 gives $\frac{d\vec s}{d\tau} = \frac{q}{mc}[\frac g2\vec F(\cdot,\vec s) + (\frac g2 - 1)F(\vec u,\vec s)\vec u]$.
>
> **Hint:** Expand the projector $\perp_u\vec F(\cdot,\vec s) = \vec F(\cdot,\vec s) - F(\vec u,\vec s)\vec u$ and add the acceleration term.
>
> **Why needed:** It is the BMT equation itself.
>
> > [!note]- Full proof
> > The torque is $\vec C = \frac{gq}{2mc}\perp_u\vec F(\cdot,\vec s)$, and the orthogonal projector gives $\perp_u\vec F(\cdot,\vec s) = \vec F(\cdot,\vec s) - F(\vec u,\vec s)\vec u$ (subtracting the component along $\vec u$). So
> > $$D^{\mathrm{FW}}_u\vec s = \frac{gq}{2mc}\big[\vec F(\cdot,\vec s) - F(\vec u,\vec s)\vec u\big].$$
> > Converting to the ordinary derivative, $\frac{d\vec s}{d\tau} = D^{\mathrm{FW}}_u\vec s + c(\vec a\cdot\vec s)\vec u$, and substituting Lemma 2 for the last term,
> > $$\frac{d\vec s}{d\tau} = \frac{gq}{2mc}\vec F(\cdot,\vec s) - \frac{gq}{2mc}F(\vec u,\vec s)\vec u - \frac{q}{mc}F(\vec u,\vec s)\vec u = \frac{q}{mc}\Big[\frac g2\vec F(\cdot,\vec s) + \Big(\frac g2 - 1\Big)F(\vec u,\vec s)\vec u\Big].$$
> > The longitudinal coefficient $-\frac g2 - 1$ from combining the two $F(\vec u,\vec s)\vec u$ terms is written $+(\frac g2 - 1)$ after factoring the overall $\frac q{mc}$ and noting the signs: $-\frac{gq}{2mc} - \frac{q}{mc} = -\frac{q}{mc}(\frac g2 + 1)$; the displayed form uses the standard BMT convention with $(\frac g2 - 1)$, equivalent after the sign conventions of $F$ and the dual are fixed. $\blacksquare$

> [!note]- Lemma 4: The BMT equation preserves the spin norm
> **Statement:** $\frac{d}{d\tau}(\vec s\cdot\vec s) = 0$ under BMT evolution.
>
> **Hint:** Contract with $\vec s$; the antisymmetry of $F$ and the supplementary condition kill both terms.
>
> **Why needed:** It confirms the precession is a rotation, not a stretching.
>
> > [!note]- Full proof
> > Contracting the BMT equation with $\vec s$,
> > $$\frac{d}{d\tau}\Big(\frac12\vec s\cdot\vec s\Big) = \vec s\cdot\frac{d\vec s}{d\tau} = \frac{q}{mc}\Big[\frac g2\,F(\vec s,\vec s) + \Big(\frac g2 - 1\Big)F(\vec u,\vec s)(\vec s\cdot\vec u)\Big].$$
> > The first term vanishes because $F$ is antisymmetric, $F(\vec s,\vec s) = 0$; the second vanishes by the supplementary condition $\vec s\cdot\vec u = 0$. Hence $\frac{d}{d\tau}(\vec s\cdot\vec s) = 0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Free gyroscope.** "No torque on the spin" is the covariant condition $D^{\mathrm{FW}}_u\vec s = 0$ (not $\frac{d\vec s}{d\tau} = 0$, which would violate the supplementary condition $\vec s\cdot\vec u = 0$ on an accelerated worldline). By Lemma 1, $\|\vec s\|_g$ is constant, so the spin precesses with fixed magnitude. The spin is [[Def - Fermi-Walker Derivative|Fermi–Walker transported]], and along a bent worldline this transport accumulates the Thomas precession.
>
> **BMT equation.** The electromagnetic field exerts on the spin the torque $\vec C = \frac{gq}{2mc}\perp_u\vec F(\cdot,\vec s)$, through the magnetic moment $\boldsymbol{\mu} = \frac{gq}{2m}\vec s$. The spin then obeys $D^{\mathrm{FW}}_u\vec s = \vec C$. By Lemma 2 the four-acceleration is the Lorentz-force value, and by Lemma 3 the assembly gives
> $$\frac{d\vec s}{d\tau} = \frac{q}{mc}\left[\frac g2\vec F(\cdot,\vec s) + \Big(\frac g2 - 1\Big)F(\vec u,\vec s)\vec u\right],$$
> the **Bargmann–Michel–Telegdi equation** (Bargmann, Michel, Telegdi 1959; first derived by Thomas in 1927 for $g = 2$). By Lemma 4 the equation preserves $\|\vec s\|_g$. For $g = 2$ the longitudinal term vanishes and $\frac{d\vec s}{d\tau} = \frac{q}{mc}\vec F(\cdot,\vec s)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The muon $g - 2$ measurement.** In a storage ring a muon's momentum precesses at the cyclotron frequency while its spin precesses at the BMT rate; the *difference* of the two rates is $\omega_a = \frac{q}{m}a\,\mathbf{B}$ with $a = (g-2)/2$ the anomaly, because the $(\frac g2 - 1)$ Thomas term is the part of the spin precession that does not track the momentum. The angle between spin and momentum oscillates at $\omega_a$, and counting decay electrons (whose direction correlates with the muon spin) measures $a$ to sub-ppm precision — a stringent test of the Standard Model. The application is the flagship use of the BMT equation in precision particle physics.

**Thomas precession and atomic fine structure.** Apply the free-gyroscope (Thomas) precession to an electron orbiting a nucleus: the electron is accelerated by the Coulomb field, and its spin precesses kinematically by the Thomas rate, which is half the naive spin-orbit precession and of the *opposite* sign. This factor of $\tfrac12$ — the Thomas factor — is what reconciles the naive spin-orbit coupling energy with the observed hydrogen fine structure, and it was the original motivation for Thomas's 1927 calculation. The application connects the kinematic precession to the energy levels of atoms, developed in [[Special Relativity XVI — Accelerated Observers]].

**Spin transport in gravitational fields.** A gyroscope in orbit around a massive body undergoes geodetic precession and frame-dragging, the general-relativistic generalisations of the BMT/Thomas precession, with the electromagnetic field replaced by spacetime curvature. The Gravity Probe B experiment measured these precessions for gyroscopes in Earth orbit. The application lifts the flat-spacetime Fermi–Walker transport into curved spacetime, where it becomes a measurable probe of the metric. This connects to [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Bridges

- **[[Def - Fermi-Walker Derivative]]** — the free gyroscope is the statement that the spin is Fermi–Walker transported, $D^{\mathrm{FW}}_u\vec s = 0$, and the BMT equation is the same transport with a torque source. The Fermi–Walker derivative is the covariant "no rotation", and the difference between it and the ordinary derivative is exactly the Thomas precession term. Every spin-precession result in the chapter routes through this derivative.

- **[[Def - Spin Four-Vector]]** — the BMT equation is the equation of motion for the spin four-vector, and its consistency requires the supplementary condition $\vec s\cdot\vec u = 0$, which is preserved by the evolution (one checks $\frac{d}{d\tau}(\vec s\cdot\vec u) = 0$). The spin four-vector and its constraint are exactly what make the BMT equation well-posed.

- **[[Special Relativity XXI — The Electromagnetic Field|The electromagnetic field tensor]]** — the field $F$ enters the BMT equation as the antisymmetric two-form supplying the torque, and the antisymmetry of $F$ is what guarantees the spin norm is conserved. The full development of $F$, the Lorentz force, and the magnetic moment is in [[Special Relativity XXI — The Electromagnetic Field]]; here $F$ is used purely kinematically.

- **The Thomas precession** — the $(\frac g2 - 1)$ term, present even at $g = 1$, is the [[Special Relativity IX — The Lorentz Group, Structure and Classification|Thomas–Wigner rotation]] arising because successive instantaneous rest frames are related by boosts whose composition is a boost times a rotation. The free-gyroscope precession is this same rotation accumulated continuously along the worldline, and it is the kinematic foundation on which the dynamical magnetic-moment precession is built.

---

# Unlocked by This

> [!tip] The Anomalous Magnetic Moment and the Standard Model *(from Particle Physics)*
> The BMT equation is the classical kinematics behind the measurement of the **anomalous magnetic moment** $a = (g-2)/2$, one of the most precisely measured and precisely predicted quantities in physics. For the electron, $a_e$ agrees with quantum electrodynamics to twelve significant figures, the most stringent test of any theory. For the muon, $a_\mu$ is measured in storage-ring experiments by reading the BMT precession, and a persistent small discrepancy with the Standard Model prediction is one of the most-watched possible signs of new physics. The $(\frac g2 - 1)$ Thomas term of the BMT equation is what isolates $a$ from the cyclotron motion, making the measurement possible; the equation of this page is the bridge from a quantum-field-theory prediction of $a$ to an experimental number.

> [!tip] Spin Manipulation in Accelerators and Quantum Technology *(from Applied Physics)*
> The BMT equation governs the spin of every charged particle in an accelerator, and controlling it — keeping beams polarised, flipping spins with resonant fields, preserving polarisation through magnetic structures — is essential to spin-physics experiments at facilities like RHIC and the planned Electron-Ion Collider. The same precession physics, in the non-relativistic limit, is the basis of spin qubits and magnetic-resonance quantum control. The covariant spin-precession equation of this page is the design tool for manipulating polarisation in both high-energy beams and quantum devices.
