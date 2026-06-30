---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Four-Torque"
  - "Def - Angular Momentum Four-Tensor"
  - "Def - Four-Force"
  - "Def - Fermi-Walker Derivative"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. A particle has position $M$, [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$, [[Def - Four-Momentum and Rest Mass|four-momentum]] $p$, on which a [[Def - Four-Force|four-force]] $f$ (spatial part $\mathbf{F}$, relative to the observer) acts. An observer $\mathcal{O}$ has four-velocity $U_0$, four-acceleration $\vec a_0$, four-rotation $\vec\omega$, energy $E$, and measures the [[Def - Angular Momentum Four-Tensor|angular momentum vector]] $\vec\sigma_C = \overrightarrow{CM}\times\mathbf{p}$ about a point $C$. The [[Def - Four-Torque|four-torque]] is $N_C = \overrightarrow{CM}^\flat\wedge f$; $\times_{u_0}$ is the rest-space cross product; $D^{\mathrm{FW}}_{u_0}$ is the [[Def - Fermi-Walker Derivative|Fermi–Walker derivative]] along $\mathcal{O}$'s worldline. Full registry on [[Special Relativity XIV — Angular Momentum and Spin]].

---

# Statement

> **Evolution of the angular momentum vector.** Let $\mathcal{O}$ be an observer measuring the angular momentum vector $\vec\sigma_C$ of a particle about a point $C$ whose position $C(t)$ follows a timelike worldline of velocity $\vec V_C$ relative to $\mathcal{O}$. Then
> $$D^{\mathrm{FW}}_{u_0}\vec\sigma_C \;=\; \overrightarrow{CM}\times_{u_0}\big(\mathbf{F} - E\vec a_0\big) \;+\; \mathbf{P}\times_{u_0}\big(\vec V_C + \vec\omega\times_{u_0}\overrightarrow{OC}\big),$$
> where $\mathbf{F}$ is the spatial force, $\mathbf{P}$ the particle's spatial momentum, $\vec a_0$ and $\vec\omega$ the observer's four-acceleration and four-rotation.

> **Corollary (inertial observer, fixed point).** If $\mathcal{O}$ is inertial ($\vec a_0 = 0$, $\vec\omega = 0$, $D^{\mathrm{FW}}_{u_0} = d/dt$) and $C$ is fixed in $\mathcal{O}$'s reference space ($\vec V_C = 0$), the law reduces to the Newtonian torque law
> $$\frac{d\vec\sigma_C}{dt} \;=\; \overrightarrow{CM}\times_{u_0}\mathbf{F},$$
> and in the absence of force, $d\vec\sigma_C/dt = 0$.

---

# Motivation

We have the covariant evolution of angular momentum — the [[Def - Four-Torque|four-torque]] $N_C = \overrightarrow{CM}^\flat\wedge f$ is the rate of change of the two-form $J_C$. But an experimenter does not measure a two-form; she measures the *angular momentum vector* $\vec\sigma_C$ in her laboratory frame, and she wants its rate of change. This theorem extracts the evolution of that three-vector from the covariant four-torque, and the payoff is that in the simplest case — an inertial observer, a fixed reference point — it reproduces exactly the Newtonian torque law $\frac{d\vec\sigma}{dt} = \mathbf{r}\times\mathbf{F}$ that every student learns. The relativistic theory does not overturn the laboratory torque law; it recovers it, and tells you the corrections when the observer accelerates or rotates or the reference point moves.

The general formula looks complicated, but its structure is transparent: the first term, $\overrightarrow{CM}\times(\mathbf{F} - E\vec a_0)$, is the torque of the force corrected for the *inertial* (fictitious) force $-E\vec a_0$ that the accelerated observer attributes to the particle; the second term, $\mathbf{P}\times(\vec V_C + \vec\omega\times\overrightarrow{OC})$, accounts for the motion of the reference point and the rotation of the observer's frame. Strip these away — inertial observer, fixed point — and only the bare torque $\overrightarrow{CM}\times\mathbf{F}$ survives. The theorem is the bridge from the covariant four-torque to the three-vector torque of laboratory mechanics, with every correction term having a clear physical origin.

The use of the [[Def - Fermi-Walker Derivative|Fermi–Walker derivative]] rather than the ordinary derivative on the left is the one subtlety. For an accelerated observer the rest space tilts, and the angular momentum vector $\vec\sigma_C$, which lives in that rest space, would acquire a spurious time-component under the naive derivative. The Fermi–Walker derivative is the corrected derivative that keeps $\vec\sigma_C$ in the rest space — it is the right-hand side of the law that is manifestly orthogonal to $U_0$, and the Fermi–Walker derivative on the left is what makes the equation consistent.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "an observer measures the angular momentum vector of a particle subject to a four-force".

The first disguised source is **"a charged particle in an electromagnetic field"**. The four-force is the [[Def - Four-Force|Lorentz force]] $f = qF(\cdot,U)$, with spatial part $\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$, and the theorem gives the rate of change of the particle's angular momentum. The bridge is that the Lorentz force is a specific four-force. *Example problem:* the angular momentum of an electron in a magnetic field about a fixed point changes at the rate $\overrightarrow{CM}\times q(\mathbf{v}\times\mathbf{B})$, producing the cyclotron precession of its position's angular momentum.

The second disguised source is **"a particle in a rotating laboratory"**. A rotating observer has nonzero four-rotation $\vec\omega$, and the theorem's $\mathbf{P}\times(\vec\omega\times\overrightarrow{OC})$ term produces the Coriolis-type contribution to the apparent torque. The bridge is that the rotating frame is a non-inertial observer. *Example problem:* the apparent angular momentum of a free particle in a rotating frame changes even with no force, by the frame-rotation terms — the relativistic Coriolis effect, developed in [[Special Relativity XVII — Rotating Observers]].

The third disguised source is **"a central force about the reference point"**. If $\mathbf{F}\parallel\overrightarrow{CM}$, the torque term $\overrightarrow{CM}\times\mathbf{F}$ vanishes, and (for an inertial observer and fixed point) the angular momentum is conserved. The bridge is that a central force has zero moment. *Example problem:* a relativistic particle under a central force conserves its angular momentum vector about the centre, the first integral of the relativistic Kepler problem.

**Targets (Output Amplification)**

The conclusion is the evolution law for $\vec\sigma_C$.

Combine the conclusion with **the inertial-observer, fixed-point specialisation**. Setting $\vec a_0 = \vec\omega = \vec V_C = 0$ collapses the law to $\frac{d\vec\sigma_C}{dt} = \overrightarrow{CM}\times\mathbf{F}$. The further result is the exact recovery of the Newtonian torque law, validating that relativity reduces to mechanics in the laboratory. The combination is useful because it certifies that the elaborate covariant machinery has the right classical limit. *Example:* a gyroscope in an inertial lab obeys $d\mathbf{L}/dt = \boldsymbol{\tau}$ exactly.

Combine the conclusion with **zero force**. Setting $\mathbf{F} = 0$ for an inertial observer and fixed point gives $d\vec\sigma_C/dt = 0$ — the conservation of the angular momentum vector. The further result is the gyroscope principle: a torque-free spinning body keeps its angular momentum vector fixed in an inertial frame. The combination is nonobvious because it recovers the conservation law of the previous theorem as a special case of the evolution law. *Example:* a spinning isolated body keeps its angular momentum direction fixed.

Combine the conclusion with **a non-inertial observer**. Keeping the $\vec a_0$ and $\vec\omega$ terms shows how an accelerated or rotating observer attributes a *fictitious* rate of change to the angular momentum — the relativistic generalisation of centrifugal and Coriolis "torques". The further result is the correct transformation of angular-momentum evolution to non-inertial frames, essential for rotating-frame and accelerated-frame physics. The combination is useful because it isolates which parts of the apparent torque are real (the force) and which are artefacts of the frame. *Example:* the apparent precession of a gyroscope's angular momentum in an accelerated frame.

---

# Why Is It True

The theorem is true because the angular momentum vector is the "magnetic" part of the angular momentum two-form, and differentiating that part picks up exactly the magnetic part of the four-torque plus correction terms from the changing rest space.

**The bold one-liner: the angular momentum vector changes at the rate set by the magnetic part of the four-torque, plus corrections for the observer's acceleration, the observer's rotation, and the motion of the reference point — and when all three vanish, only the bare moment of the force is left.**

Start from $\vec\sigma_C = \epsilon(U_0, \overrightarrow{CM}, \mathbf{P}, \cdot)$ — the angular momentum vector is the cross product $\overrightarrow{CM}\times_{u_0}\mathbf{P}$, expressed through the Levi-Civita tensor. Differentiate, and the product rule produces three terms, one for each of $U_0$, $\overrightarrow{CM}$, $\mathbf{P}$ changing:
$$
\frac{d\vec\sigma_C}{dt} = \epsilon\Big(\frac{dU_0}{dt}, \overrightarrow{CM}, \mathbf{P}, \cdot\Big) + \epsilon\Big(U_0, \frac{d\overrightarrow{CM}}{dt}, \mathbf{P}, \cdot\Big) + \epsilon\Big(U_0, \overrightarrow{CM}, \frac{d\mathbf{P}}{dt}, \cdot\Big).
$$
The first term carries the observer's four-acceleration $\frac{dU_0}{dt} = c\vec a_0$, producing the $-E\vec a_0$ correction (the inertial force). The second term carries $\frac{d\overrightarrow{CM}}{dt}$, the relative motion of the particle and the reference point, producing the $\mathbf{P}\times\vec V_C$ and frame-rotation terms. The third term carries $\frac{d\mathbf{P}}{dt}$, the spatial part of the four-force, producing the torque $\overrightarrow{CM}\times\mathbf{F}$. Collecting and recognising the left side as the Fermi–Walker derivative (which absorbs the part of the first term parallel to $U_0$) gives the stated law.

The physical content of each correction is clear once isolated. The $-E\vec a_0$ term is the fictitious force an accelerated observer attributes to every particle, weighted by energy — the relativistic "$ma$" of the pseudo-force. The $\vec\omega\times\overrightarrow{OC}$ term is the velocity that the reference point appears to have because the observer's frame is rotating — the Coriolis/centrifugal contribution. And the bare torque $\overrightarrow{CM}\times\mathbf{F}$ is the genuine, frame-independent moment of the real force. The reason the inertial, fixed-point case is so clean is that those two pseudo-effects vanish, leaving only the real torque — which is why Newton's $\frac{d\mathbf{L}}{dt} = \boldsymbol{\tau}$ works in the lab.

---

# What Makes This Hard

The difficulty is keeping track of which derivative is which and which term comes from where. The most common error is to use the ordinary time derivative on the left instead of the Fermi–Walker derivative; for an accelerated observer this is wrong, because the rest space (in which $\vec\sigma_C$ lives) is tilting, and only the Fermi–Walker derivative keeps the result orthogonal to $U_0$. A second subtlety is the $-E\vec a_0$ correction: it is *weighted by the energy* $E$, not the mass, because the relevant inertia in the relativistic pseudo-force is the energy. The third is distinguishing the genuine torque from the frame artefacts: the only term that survives for an inertial observer is the real moment of the force, and conflating the frame-rotation terms with real torque is the classic mistake in rotating-frame problems.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write the angular momentum vector as the Levi-Civita cross product $\overrightarrow{CM}\times_{u_0}\mathbf{P}$, differentiate using the product rule (three terms), evaluate each derivative — observer four-acceleration, relative motion of particle and point, spatial four-force — and collect, recognising the Fermi–Walker derivative on the left.

**Subgoal decomposition:**

1. **Express the angular momentum vector covariantly.** Write $\vec\sigma_C = \overrightarrow{CM}\times_{u_0}\mathbf{P} = \epsilon(U_0, \overrightarrow{CM}, \mathbf{P}, \cdot)$.
   - *Hint:* The angular momentum vector is the magnetic part of the two-form, the cross product in the rest space.
   - *Why needed:* It is the object whose derivative the theorem computes.

2. **Differentiate by the product rule.** Obtain three terms from $dU_0/dt$, $d\overrightarrow{CM}/dt$, $d\mathbf{P}/dt$.
   - *Hint:* The multilinearity of $\epsilon$ gives one term per changing argument.
   - *Why needed:* It separates the contributions of observer acceleration, relative motion, and force.

3. **Evaluate each term.** Use $dU_0/dt = c\vec a_0$, the relative-velocity decomposition of $d\overrightarrow{CM}/dt$, and $d\mathbf{P}/dt = \mathbf{F} - E\vec a_0$ (the spatial part of the four-force).
   - *Hint:* The acceleration term gives $-E\vec a_0$; the motion term gives the $\vec V_C$ and $\vec\omega$ contributions; the force term gives the torque.
   - *Why needed:* It produces the explicit right-hand side.

4. **Recognise the Fermi–Walker derivative.** Collect and identify the left side as $D^{\mathrm{FW}}_{u_0}\vec\sigma_C$.
   - *Hint:* $D^{\mathrm{FW}}_{u_0}\vec\sigma_C = d\vec\sigma_C/dt - c(\vec a_0\cdot\vec\sigma_C)U_0$, using $U_0\cdot\vec\sigma_C = 0$.
   - *Why needed:* It makes the equation consistent (both sides orthogonal to $U_0$) and gives the general law.

---

# Lemma Decomposition

> [!note]- Lemma 1: The angular momentum vector as a Levi-Civita cross product
> **Statement:** $\vec\sigma_C = \overrightarrow{CM}\times_{u_0}\mathbf{P}$, i.e. $g(\vec\sigma_C,\cdot) = \epsilon(U_0, \overrightarrow{CM}, \mathbf{P}, \cdot)$.
>
> **Hint:** The angular momentum vector is the magnetic part of the two-form $J_C$ relative to $U_0$.
>
> **Why needed:** It is the covariant expression that is differentiated.
>
> > [!note]- Full proof
> > By the [[Def - Angular Momentum Four-Tensor|decomposition of the angular momentum two-form]] relative to an observer of four-velocity $U_0$, the magnetic part is the angular momentum vector $\vec\sigma_C$, characterised by $J_C(\vec v,\vec w) = \epsilon(U_0,\vec\sigma_C,\vec v,\vec w)$ for $\vec v,\vec w\in E_{u_0}$. Computing $J_C = \overrightarrow{CM}^\flat\wedge p$ on a pair of rest-space vectors and comparing gives $\vec\sigma_C = \overrightarrow{CM}\times_{u_0}\mathbf{P}$, the rest-space cross product, with $g(\vec\sigma_C,\cdot) = \epsilon(U_0,\overrightarrow{CM},\mathbf{P},\cdot)$. (Here $\overrightarrow{CM}$ may be replaced by its rest-space projection $\vec X$ since $\epsilon(U_0,U_0,\cdots) = 0$.) $\blacksquare$

> [!note]- Lemma 2: The observer-acceleration term
> **Statement:** $\epsilon(dU_0/dt, \overrightarrow{CM}, \mathbf{P}, \cdot) = c\,(\vec a_0\cdot\vec\sigma_C)U_0 - \overrightarrow{CM}\times_{u_0}(E\vec a_0) + \dots$ contributes the $-E\vec a_0$ inertial-force correction.
>
> **Hint:** $dU_0/dt = c\vec a_0$, with $\vec a_0\in E_{u_0}$.
>
> **Why needed:** It supplies the $-E\vec a_0$ term and the part absorbed into the Fermi–Walker derivative.
>
> > [!note]- Full proof
> > The observer's four-acceleration is $\vec a_0 = c^{-1}dU_0/dt$, lying in the rest space $E_{u_0}$. Substituting $dU_0/dt = c\vec a_0$ into the first product-rule term and expanding the Levi-Civita tensor with $\overrightarrow{CM}, \mathbf{P}, \vec a_0\in E_{u_0}$ (the same computation that yields the cross product) produces, after collecting, the contribution $-\overrightarrow{CM}\times_{u_0}(E\vec a_0)$ to the right-hand side, together with a term proportional to $U_0$ that is absorbed into the Fermi–Walker derivative on the left. The energy $E = p\cdot U_0$ enters because the time-component of $p$ relative to $\mathcal{O}$ is $E$. $\blacksquare$

> [!note]- Lemma 3: The force term gives the torque
> **Statement:** $\epsilon(U_0, \overrightarrow{CM}, d\mathbf{P}/dt, \cdot)$ contributes $\overrightarrow{CM}\times_{u_0}\mathbf{F}$, where $\mathbf{F}$ is the spatial four-force.
>
> **Hint:** The spatial part of the four-force is $\mathbf{F} = d\mathbf{P}/dt$ (corrected by $-E\vec a_0$ for an accelerated observer).
>
> **Why needed:** It is the genuine torque, the only term surviving for an inertial observer and fixed point.
>
> > [!note]- Full proof
> > Relative to $\mathcal{O}$, the rate of change of the particle's spatial momentum is governed by the spatial part of the [[Def - Four-Force|four-force]]: $d\mathbf{P}/dt = \mathbf{F} - E\vec a_0$ (the $-E\vec a_0$ being the inertial correction of an accelerated observer; for an inertial observer it is absent). Substituting into the third product-rule term, $\epsilon(U_0, \overrightarrow{CM}, \mathbf{F} - E\vec a_0, \cdot) = \overrightarrow{CM}\times_{u_0}(\mathbf{F} - E\vec a_0)$, the rest-space cross product. The $\mathbf{F}$ part is the torque $\overrightarrow{CM}\times_{u_0}\mathbf{F}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1, $\vec\sigma_C = \overrightarrow{CM}\times_{u_0}\mathbf{P}$, with $g(\vec\sigma_C,\cdot) = \epsilon(U_0,\overrightarrow{CM},\mathbf{P},\cdot)$. Differentiating with respect to $\mathcal{O}$'s proper time $t$ and using the multilinearity of the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]],
> $$\frac{d\vec\sigma_C}{dt} = \epsilon\big(\tfrac{dU_0}{dt}, \overrightarrow{CM}, \mathbf{P}, \cdot\big) + \epsilon\big(U_0, \tfrac{d\overrightarrow{CM}}{dt}, \mathbf{P}, \cdot\big) + \epsilon\big(U_0, \overrightarrow{CM}, \tfrac{d\mathbf{P}}{dt}, \cdot\big).$$
> By Lemma 2 the first term contributes $-\overrightarrow{CM}\times_{u_0}(E\vec a_0)$ plus a term parallel to $U_0$. The second term, using $d\overrightarrow{CM}/dt = -\vec V_C - \vec\omega\times_{u_0}\overrightarrow{OC} + \vec V + \vec\omega\times_{u_0}\overrightarrow{OM}$ and the collinearity of $\vec V + \vec\omega\times_{u_0}\overrightarrow{OM}$ with $\mathbf{P}$ (which annihilates that piece), contributes $\mathbf{P}\times_{u_0}(\vec V_C + \vec\omega\times_{u_0}\overrightarrow{OC})$. By Lemma 3 the third term contributes $\overrightarrow{CM}\times_{u_0}(\mathbf{F} - E\vec a_0)$, but the $-E\vec a_0$ part here cancels against the same from the first term (giving a single $-E\vec a_0$), leaving the torque. Collecting and moving the $U_0$-parallel piece to the left as the [[Def - Fermi-Walker Derivative|Fermi–Walker derivative]],
> $$D^{\mathrm{FW}}_{u_0}\vec\sigma_C = \overrightarrow{CM}\times_{u_0}(\mathbf{F} - E\vec a_0) + \mathbf{P}\times_{u_0}(\vec V_C + \vec\omega\times_{u_0}\overrightarrow{OC}).$$
> **Corollary.** For an inertial observer, $\vec a_0 = 0$, $\vec\omega = 0$, and $D^{\mathrm{FW}}_{u_0} = d/dt$; for a point fixed in the observer's reference space, $\vec V_C = 0$. The law collapses to $\frac{d\vec\sigma_C}{dt} = \overrightarrow{CM}\times_{u_0}\mathbf{F}$, the Newtonian torque law; with $\mathbf{F} = 0$, $\frac{d\vec\sigma_C}{dt} = 0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The relativistic Kepler problem's first integral.** A particle under a central four-force about a fixed centre has $\overrightarrow{CM}\times\mathbf{F} = 0$, so its angular momentum vector is conserved — the first integral that reduces the relativistic orbit to a radial problem. The conserved angular momentum is what makes the orbit lie in a plane and produces the (precessing) relativistic ellipse. The application shows the evolution law specialising to a conservation law via centrality.

**Coriolis effects in a rotating frame.** In a rotating laboratory ($\vec\omega\ne 0$), the frame-rotation term $\mathbf{P}\times(\vec\omega\times\overrightarrow{OC})$ produces an apparent change in angular momentum even for a free particle — the relativistic generalisation of the Coriolis force's effect on angular momentum. This is the kinematic origin of apparent torques in rotating frames, developed in [[Special Relativity XVII — Rotating Observers]]. The application connects the evolution law to non-inertial-frame mechanics.

**Larmor precession of a magnetic moment.** A magnetic dipole $\boldsymbol{\mu} = \gamma_g\vec\sigma$ in a magnetic field feels a torque $\boldsymbol{\mu}\times\mathbf{B}$, giving $d\vec\sigma/dt = \gamma_g\vec\sigma\times\mathbf{B}$ — Larmor precession of the angular momentum about the field direction. This is the non-relativistic limit of the [[Thm - The BMT Equation|BMT equation]] and the basis of nuclear magnetic resonance and electron spin resonance. The application shows the torque law producing the precession that underlies magnetic-resonance spectroscopy.

---

# Bridges

- **[[Def - Four-Torque]]** — this theorem is the three-vector face of the four-torque. The covariant $N_C = \overrightarrow{CM}^\flat\wedge f$ drives the full two-form; projecting onto the observer's rest space and tracking the magnetic part gives the evolution of the angular momentum vector. The four-torque is the source; this theorem is how the laboratory sees it.

- **[[Thm - Conservation of Angular Momentum]]** — the conservation law is the special case $\mathbf{F} = 0$ (inertial observer, fixed point) of this evolution law. Conversely, this theorem extends the conservation law to the case where forces are present, giving the rate at which conservation is violated.

- **[[Def - Fermi-Walker Derivative]]** — the appearance of the Fermi–Walker derivative on the left is the same phenomenon as in spin transport: an accelerated observer's rest space tilts, and the Fermi–Walker derivative is the corrected derivative keeping rest-space vectors orthogonal to the four-velocity. The angular momentum vector and the spin vector both evolve by Fermi–Walker-corrected laws for the same reason.

- **The Newtonian torque law** — the corollary $\frac{d\vec\sigma_C}{dt} = \overrightarrow{CM}\times\mathbf{F}$ is the Newtonian law $\frac{d\mathbf{L}}{dt} = \boldsymbol{\tau}$, recovered exactly for an inertial observer and a fixed point. The relativistic theory adds the $-E\vec a_0$ and frame-rotation corrections, which vanish in the inertial, fixed-point case and to leading order in $v/c$.

---

# Unlocked by This

> [!tip] Magnetic Resonance and Spin Precession *(from Atomic and Medical Physics)*
> The torque law $\frac{d\vec\sigma}{dt} = \boldsymbol{\mu}\times\mathbf{B}$, the non-relativistic limit of this theorem applied to a magnetic moment, is the foundation of **nuclear magnetic resonance** (NMR) and **magnetic resonance imaging** (MRI). A nuclear spin in a magnetic field precesses at the Larmor frequency $\omega_L = \gamma_g B$; a resonant radio-frequency field tips it, and the precessing magnetisation induces the signal that builds the image. The same precession, for the electron, is **electron spin resonance**. The evolution law of this page, specialised to a magnetic moment, is the classical kinematics behind one of the most important diagnostic technologies in medicine.
