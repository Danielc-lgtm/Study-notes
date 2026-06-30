---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Uniformly Rotating Observer"
  - "Def - Einstein-Poincaré Simultaneity"
  - "Def - Lorentz Factor and Relative Velocity"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. The disk rotates at $\omega$; a corotating observer at radius $r$ has velocity $\vec V = r\omega\,\vec n$ relative to the inertial $\mathcal{O}_*$ and Lorentz factor $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$. A one-parameter family of corotating observers $\mathcal{O}'_{(\lambda)}$, $\lambda\in[0,1]$, traces a curve $\mathscr{C}$ in $\mathcal{O}$'s reference space $R_{\mathcal{O}}$; the family is **closed** if $\mathcal{O}'_{(1)} = \mathcal{O}'_{(0)}$. The proper separation vector between neighbours is $d\vec\ell = (dx^i_{(\lambda)}/d\lambda)\,e_i\,d\lambda$, with proper length $d\ell'$. The accumulated coordinate-time and proper-time gaps around a loop are $\Delta t$ and $\Delta t'_{\text{desync}}$. The area vector of the surface enclosed by $\mathscr{C}$ is $\vec{\mathcal{A}}$. Full registry on [[Special Relativity XVII — Rotating Observers]].

> [!warning] Convention: Gourgoulhon's opposite signature
> Gourgoulhon (Chapter 13) uses $\mathrm{diag}(-1,+1,+1,+1)$. The synchronization condition $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$ involves the rest-space scalar product $\vec V\cdot d\vec\ell$ of two spacelike vectors; under the overall sign flip this Euclidean rest-space product is positive-definite in either convention, so the formula is carried over unchanged.

---

# Statement

> **Local synchronization.** Two infinitely close [[Def - Uniformly Rotating Observer|corotating observers]] $\mathcal{O}'_{(\lambda)}$ and $\mathcal{O}'_{(\lambda+d\lambda)}$ can be Einstein–Poincaré synchronized: the event on $\mathcal{O}'_{(\lambda+d\lambda)}$ simultaneous (for both) with a given event of $\mathcal{O}'_{(\lambda)}$ has its central coordinate time $t$ shifted by
> $$dt = \Gamma^2\,\frac{\vec V\cdot d\vec\ell}{c^2},$$
> where $d\vec\ell$ is the proper separation vector between the two observers.

> **Impossibility of global synchronization.** For a *closed* family of corotating observers tracing a loop $\mathscr{C}$ (with $\mathcal{O}'_{(1)} = \mathcal{O}'_{(0)}$), the accumulated proper-time gap on returning to the starting observer is
> $$\Delta t'_{\text{desync}} = \frac{1}{c^2\,\Gamma_{(0)}}\oint_{\mathscr{C}}\Gamma^2\,\vec V\cdot d\vec\ell \;\ne\; 0,$$
> the circulation of $\Gamma^2\vec V$ around $\mathscr{C}$. For a loop at constant radius $r$, $\Delta t'_{\text{desync}} = \pm 2\pi\Gamma\,r^2\omega/c^2$; for small velocities ($r\omega\ll c$), by Stokes' theorem and $\mathrm{curl}\,\vec V = 2\vec\omega$,
> $$\Delta t'_{\text{desync}} \simeq \frac{2}{c^2}\,\vec\omega\cdot\vec{\mathcal{A}}.$$
> Hence the clocks of corotating observers cannot be globally synchronized: starting from one observer and synchronizing neighbour-to-neighbour around the loop, one returns with the clock offset by $\Delta t'_{\text{desync}}$.

---

# Motivation

In an inertial frame, synchronizing clocks is routine: pick a master clock, send light signals, and assign times so that every observer agrees on simultaneity. The slices of constant time are flat spatial hypersurfaces, and they fit together into a single global time coordinate. This theorem asks whether the same can be done on a rotating disk, and the answer — no — is the structural fact from which everything dramatic in the chapter descends.

The local part is reassuring and matches inertial intuition: any two *nearby* corotating observers can synchronize their clocks perfectly well, by exchanging light signals and applying the [[Def - Einstein-Poincaré Simultaneity|Einstein–Poincaré convention]]. The synchronization simply requires their coordinate times to differ by a definite amount $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$. So far there is no obstruction; each observer can agree with their immediate neighbours.

The global part is where rotation bites. Synchronize observer $1$ with observer $2$, then $2$ with $3$, and so on around a closed loop back to observer $1$. Each step is legitimate, but the little time-shifts $dt$ do not cancel — they accumulate, and when you return to your starting observer, the time you have assigned disagrees with the starting observer's own clock by a nonzero amount $\Delta t'_{\text{desync}}$. There is no consistent global time on the disk. The gap is a *circulation* — a line integral of $\Gamma^2\vec V$ around the loop — and like any circulation it is nonzero precisely because the underlying field has nonzero "curl", which here is twice the rotation, $\mathrm{curl}\,\vec V = 2\vec\omega$.

This is not an experimental nuisance to be engineered away; it is the geometric heart of rotating-frame physics, and it has immediate, measurable, and economically consequential manifestations. The Hafele–Keating experiment flew atomic clocks around the world and measured exactly this desynchronization (with the famous east–west asymmetry). The Global Positioning System must apply an explicit Sagnac correction for it. International Atomic Time is *defined* by correcting each ground clock for it. And the Sagnac effect itself — the next section — is precisely twice this gap, dressed as an arrival-time difference between counter-propagating signals. The theorem is the chapter's keystone: the Ehrenfest paradox, the Sagnac effect, and the timekeeping corrections are all this one nonzero loop integral.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem applies whenever a closed loop of corotating (or, more generally, rotating) observers is in play — and that hypothesis appears in several guises.

The first disguised source is **"a global time coordinate is sought on a rotating system"**. Any attempt to assign a single consistent time to all observers on a spinning platform is governed by this theorem, and it fails by exactly $\Delta t'_{\text{desync}}$. The bridge is that "global time" means "globally consistent simultaneity", and synchronization around a loop is the test. *Example problem:* show that no time coordinate $t'$ exists on the rotating disk for which all corotating observers' clocks read $t'$ on a common slice.

The second disguised source is **"atomic clocks distributed over the rotating Earth"**. Each ground clock reads the proper time of a corotating observer; combining them to define a worldwide time is exactly the global-synchronization problem, and the desynchronization is the term that must be corrected. The bridge is that the Earth's surface is a corotating congruence. *Example problem:* compute the synchronization correction needed to compare two atomic clocks at different longitudes (the basis of TAI).

The third disguised source is **"counter-propagating signals around a closed path"**. The Sagnac delay is twice this desynchronization gap, so any problem about signals sent both ways around a rotating loop invokes this theorem. The bridge is that the prograde and retrograde signals accumulate the gap with opposite signs. *Example problem:* find the delay between clockwise and counter-clockwise light pulses on a rotating ring ([[Thm - The Sagnac Effect]]).

**Targets (Output Amplification)**

The conclusion is $\Delta t'_{\text{desync}} = \frac{1}{c^2\Gamma_{(0)}}\oint_{\mathscr{C}}\Gamma^2\vec V\cdot d\vec\ell \ne 0$.

Combine the conclusion with **Stokes' theorem and the vorticity identity $\mathrm{curl}\,\vec V = 2\vec\omega$**. The circulation becomes the flux $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$, giving the desynchronization (and hence the Sagnac delay) the universal area-proportional form. The combination is useful because it replaces a path-dependent line integral with a clean enclosed-area quantity, and it is nonobvious that the answer depends only on the enclosed area, not the loop's shape. *Example:* the GPS and ring-laser-gyroscope formulas.

Combine the conclusion with **the factor of two for counter-propagation**. A prograde signal sees $+\Delta t'_{\text{desync}}$ and a retrograde one $-\Delta t'_{\text{desync}}$, so the difference of their arrival times is $2\Delta t'_{\text{desync}}$ — the Sagnac delay. The combination is the bridge from synchronization to the Sagnac effect, and it is nonobvious because the proper *travel* times of the two signals are in fact equal; only the arrival times differ. *Example:* [[Thm - The Sagnac Effect]].

Combine the conclusion with **the Hafele–Keating clock transport**. A clock flown around the world at velocity $v$ relative to the ground accumulates, on return, the desynchronization gap plus a velocity-dependent term, giving the measured east–west asymmetry. The combination connects the abstract obstruction to a table-top (well, airline) experiment, and it is nonobvious that slow clock transport and light-signal synchronization give the *same* desynchronization. *Example:* the 1971 Hafele–Keating flights.

---

# Why Is It True

The cleanest way to see the impossibility is to recognize the synchronization condition as a **differential one-form** and ask whether it is exact.

Locally, synchronizing neighbour $\lambda$ with neighbour $\lambda+d\lambda$ requires the central coordinate time to advance by $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$. Think of the right-hand side as a one-form $\alpha = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$ defined on the disk. A global time coordinate would exist if and only if this one-form were *exact* — if there were a function $t(\lambda)$ on the disk with $dt = \alpha$ — because then "set every clock to read $t$" would be consistent everywhere. A function's differential, integrated around any closed loop, gives zero (you return to the same value). So a global time exists if and only if $\oint_{\mathscr{C}}\alpha = 0$ for every loop.

But $\oint_{\mathscr{C}}\alpha \ne 0$. The reason is the rotation. By Stokes' theorem the loop integral equals the flux of the *exterior derivative* (the "curl") of $\alpha$ through the enclosed surface, and the curl of the velocity field of a rigidly rotating disk is not zero — it is twice the angular velocity, $\mathrm{curl}\,\vec V = 2\vec\omega$. A rotating flow has vorticity; vorticity is exactly the obstruction to the velocity one-form being a gradient; and that obstruction is what makes the synchronization gap nonzero. The disk rotates, so its velocity field has vorticity, so the synchronization one-form has nonzero curl, so its loop integral is nonzero, so no global time exists.

**The one-line mechanism:** *the synchronization condition is a one-form whose curl is the vorticity $2\vec\omega$ of the rotating congruence; a closed loop encircles a nonzero vorticity flux, so the synchronization fails to close by exactly that flux.*

This explains every feature at once. The gap is proportional to the enclosed area (it is a flux). It is proportional to $\omega$ (the vorticity is $2\omega$). It changes sign with the sense of traversal (the flux's sign follows the orientation). It vanishes if and only if $\omega = 0$ (no vorticity, the inertial case, where a global time does exist). And it is a genuinely relativistic effect, not a Newtonian limit, because in Newtonian physics all observers share one absolute time and the synchronization is trivially global — the surviving $c^2$ in $\Delta t'_{\text{desync}}$ is the tell that this is special-relativistic geometry, not classical mechanics.

---

# What Makes This Hard

The conceptual hurdle is accepting that something achievable *locally* (any two neighbours synchronize fine) is impossible *globally* — the failure is in the integration around a loop, not in any single step, which is counterintuitive if one thinks of synchronization as a purely pairwise relation. The non-obvious step is recognizing the synchronization condition as a one-form and the obstruction as its non-exactness (nonzero loop integral), equivalently the nonzero vorticity of the rotating congruence. The most common error is to assume that because local synchronization always works, a global time must exist by "patching together" the local synchronizations — exactly the patching that fails, because the patches are inconsistent around a loop by $\Delta t'_{\text{desync}}$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Derive the local synchronization condition from the orthogonality of the corotating four-velocity to the proper separation vector (Einstein–Poincaré simultaneity is metric orthogonality). Expand the orthogonality, using $U' = \Gamma(U + c^{-1}\vec V)$ and the rest-space relations, to get $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$. Then integrate this $dt$ around a closed loop; the integral is a nonzero circulation, which Stokes' theorem (with $\mathrm{curl}\,\vec V = 2\vec\omega$) evaluates as a vorticity flux for small velocities, and direct integration evaluates as $\pm 2\pi\Gamma r^2\omega/c^2$ at constant radius.

**Subgoal decomposition:**

1. **Express simultaneity as orthogonality.** Two events $A_{(\lambda)}$, $A_{(\lambda+d\lambda)}$ are simultaneous for $\mathcal{O}'_{(\lambda)}$ iff $U'_{(\lambda)}\cdot\overrightarrow{A_{(\lambda)}A_{(\lambda+d\lambda)}} = 0$.
   - *Hint:* Einstein–Poincaré simultaneity is metric orthogonality of the separation to the four-velocity.
   - *Why needed:* It is the equation whose expansion yields the $dt$ condition.

2. **Compute the separation vector.** Show $\overrightarrow{A_{(\lambda)}A_{(\lambda+d\lambda)}} = c\,dt\,U + d\vec\ell + dt\,\vec V$, where $d\vec\ell$ is the proper separation in $\mathcal{O}$'s rest space.
   - *Hint:* Add the displacements via the central worldline; use $de_i/dt = \vec\omega\times_U e_i$ and $x^i_{(\lambda)}\vec\omega\times_U e_i = \vec V$.
   - *Why needed:* It puts the orthogonality condition in computable form.

3. **Expand orthogonality to get the local gap.** Substitute $U'_{(\lambda)} = \Gamma(U + c^{-1}\vec V)$ and use $U\cdot U = 1$ (mostly-minus), $U\cdot d\vec\ell = 0$, $U\cdot\vec V = 0$, $1 - \vec V\cdot\vec V/c^2 = \Gamma^{-2}$ to obtain $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$.
   - *Hint:* The $U\cdot U$ and $\vec V\cdot\vec V$ terms combine to $\Gamma^{-2}$; the surviving cross term is $\vec V\cdot d\vec\ell$.
   - *Why needed:* This is the local synchronization condition.

4. **Integrate around a closed loop.** Show $\Delta t'_{\text{desync}} = \frac{1}{c^2\Gamma_{(0)}}\oint_{\mathscr{C}}\Gamma^2\vec V\cdot d\vec\ell$, evaluate at constant radius as $\pm 2\pi\Gamma r^2\omega/c^2$, and for small velocities via Stokes and $\mathrm{curl}\,\vec V = 2\vec\omega$ as $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$.
   - *Hint:* Divide the coordinate-time gap $\oint\Gamma^2\vec V\cdot d\vec\ell/c^2$ by $\Gamma_{(0)}$ to convert to $\mathcal{O}'_{(0)}$'s proper time; at constant $r$, $\vec V\cdot d\vec\ell = r^2\omega\,d\varphi$.
   - *Why needed:* This is the global obstruction, the theorem's conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Local simultaneity is orthogonality of $U'$ to the separation
> **Statement:** The events $A_{(\lambda)}$ and $A_{(\lambda+d\lambda)}$ (the latter on $\mathcal{O}'_{(\lambda+d\lambda)}$) are simultaneous from $\mathcal{O}'_{(\lambda)}$'s viewpoint iff $U'_{(\lambda)}\cdot\overrightarrow{A_{(\lambda)}A_{(\lambda+d\lambda)}} = 0$.
>
> **Hint:** [[Def - Einstein-Poincaré Simultaneity|Einstein–Poincaré simultaneity]] of two events relative to an observer is exactly metric orthogonality of their separation to the observer's four-velocity.
>
> **Why needed:** It is the condition whose expansion produces the local time gap.
>
> > [!note]- Full proof
> > By the [[Def - Einstein-Poincaré Simultaneity|Einstein–Poincaré convention]], an observer with four-velocity $U'$ deems two events simultaneous when the vector joining them lies in the observer's local rest space, i.e. is orthogonal to $U'$. Here $A_{(\lambda)}$ is an event of $\mathcal{O}'_{(\lambda)}$ and $A_{(\lambda+d\lambda)}$ the event of $\mathcal{O}'_{(\lambda+d\lambda)}$ simultaneous to it; the simultaneity condition is $U'_{(\lambda)}\cdot\overrightarrow{A_{(\lambda)}A_{(\lambda+d\lambda)}} = 0$. $\blacksquare$

> [!note]- Lemma 2: The proper separation vector
> **Statement:** $\overrightarrow{A_{(\lambda)}A_{(\lambda+d\lambda)}} = c\,dt\,U + d\vec\ell + dt\,\vec V$, where $d\vec\ell = dx^i\,e_i$ is the proper separation between the two corotating observers in $\mathcal{O}$'s rest space and $dt$ is the central-time gap between the two events.
>
> **Hint:** Decompose the separation through the central worldline: from $A_{(\lambda)}$ to $O(t)$, along $\mathcal{O}$ to $O(t+dt)$, then to $A_{(\lambda+d\lambda)}$; use $de_i/dt = \vec\omega\times_U e_i$.
>
> **Why needed:** It writes the separation in terms of the measurable quantities $dt$, $d\vec\ell$, $\vec V$.
>
> > [!note]- Full proof
> > Write $\overrightarrow{A_{(\lambda)}A_{(\lambda+d\lambda)}} = \overrightarrow{A_{(\lambda)}O(t)} + \overrightarrow{O(t)O(t+dt)} + \overrightarrow{O(t+dt)A_{(\lambda+d\lambda)}}$. The first term is $-x^i_{(\lambda)}e_i(t)$, the third is $x^i_{(\lambda+d\lambda)}e_i(t+dt)$, and the middle is $c\,dt\,U$. Expanding $e_i(t+dt) = e_i(t) + dt\,\vec\omega\times_U e_i$ (from $de_i/dt = \vec\omega\times_U e_i$) and writing $dx^i = x^i_{(\lambda+d\lambda)} - x^i_{(\lambda)}$, the sum becomes $c\,dt\,U + dx^i\,e_i(t) + dt\,x^i_{(\lambda)}\vec\omega\times_U e_i$ to first order. Since $\vec\omega = \omega e_3$, $x^i\vec\omega\times_U e_i = \omega(x^1 e_2 - x^2 e_1) = \vec V$, the corotating velocity. With $d\vec\ell := dx^i\,e_i$, this is $c\,dt\,U + d\vec\ell + dt\,\vec V$. $\blacksquare$

> [!note]- Lemma 3: The local synchronization condition
> **Statement:** $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$.
>
> **Hint:** Substitute Lemma 2 into Lemma 1 with $U'_{(\lambda)} = \Gamma(U + c^{-1}\vec V)$; use $U\cdot U = 1$, $U\cdot d\vec\ell = 0$, $U\cdot\vec V = 0$, $1 - \vec V\cdot\vec V/c^2 = \Gamma^{-2}$.
>
> **Why needed:** It is the local time gap that integrates to the global obstruction.
>
> > [!note]- Full proof
> > By Lemma 1, $\big(U + c^{-1}\vec V\big)\cdot\big(c\,dt\,U + d\vec\ell + dt\,\vec V\big) = 0$ (dropping the overall $\Gamma$). Expand, using $U\cdot U = 1$, $U\cdot d\vec\ell = 0$ (the separation is spacelike, in $\mathcal{O}$'s rest space), $U\cdot\vec V = 0$ ($\vec V$ is spacelike): the terms are $c\,dt(U\cdot U) + c^{-1}dt(\vec V\cdot\vec V) + c^{-1}(\vec V\cdot d\vec\ell) = c\,dt + c^{-1}dt\,\vec V\cdot\vec V + c^{-1}\vec V\cdot d\vec\ell = 0$. (The cross terms $U\cdot d\vec\ell$, $U\cdot\vec V$, and $dt\,U\cdot\vec V$ vanish.) Thus $c\,dt\,(1 - \vec V\cdot\vec V/c^2) = -c^{-1}\vec V\cdot d\vec\ell$ with the rest-space sign convention; carrying the mostly-minus rest-space (Euclidean) product as positive, one obtains $c\,dt\,\Gamma^{-2} = c^{-1}\vec V\cdot d\vec\ell$, i.e. $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$. $\blacksquare$

> [!note]- Lemma 4: The loop integral does not vanish
> **Statement:** $\Delta t'_{\text{desync}} = \frac{1}{c^2\Gamma_{(0)}}\oint_{\mathscr{C}}\Gamma^2\vec V\cdot d\vec\ell$; at constant radius this is $\pm 2\pi\Gamma r^2\omega/c^2$, and for small velocities $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$.
>
> **Hint:** Integrate the coordinate-time gap $dt$ around $\mathscr{C}$, then divide by $\Gamma_{(0)}$ to convert to $\mathcal{O}'_{(0)}$'s proper time; apply Stokes' theorem with $\mathrm{curl}\,\vec V = 2\vec\omega$ for the small-velocity form.
>
> **Why needed:** It is the nonvanishing obstruction — the whole point of the theorem.
>
> > [!note]- Full proof
> > Summing the local gaps $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$ around the closed loop gives the central-coordinate-time gap $\Delta t = \frac{1}{c^2}\oint_{\mathscr{C}}\Gamma^2\vec V\cdot d\vec\ell$ between the start and end events on $\mathcal{O}'_{(0)}$'s worldline. The corresponding gap in $\mathcal{O}'_{(0)}$'s *proper* time follows by dividing by $\Gamma_{(0)}$ (since $dt' = \Gamma^{-1}dt$ along that worldline): $\Delta t'_{\text{desync}} = \frac{1}{c^2\Gamma_{(0)}}\oint_{\mathscr{C}}\Gamma^2\vec V\cdot d\vec\ell$. For a loop at constant radius $r$, $\Gamma$ is constant and $\vec V\cdot d\vec\ell = r\omega\,\vec n\cdot(r\,d\varphi\,\vec n) = r^2\omega\,d\varphi$, so $\oint = r^2\omega\int_0^{2\pi}d\varphi = 2\pi r^2\omega$ and $\Delta t'_{\text{desync}} = \pm 2\pi\Gamma r^2\omega/c^2$ (sign from the sense of traversal). For small velocities $\Gamma\to 1$, the circulation $\oint_{\mathscr{C}}\vec V\cdot d\vec\ell = \int_S(\mathrm{curl}\,\vec V)\cdot d\vec{\mathcal{A}}$ by Stokes' theorem; for rigid rotation $\mathrm{curl}\,\vec V = 2\vec\omega$, giving $\Delta t'_{\text{desync}} \simeq \frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$. Since $\omega\ne 0$ and the enclosed area is positive, the gap is nonzero. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> *Step 0 — well-posedness of local synchronization.* For two infinitely close corotating observers the Einstein–Poincaré procedure (light emitted, reflected, received) is well-defined because their separation is spacelike and the round-trip is short; the simultaneous event is fixed by orthogonality of the separation to the four-velocity (Lemma 1).
>
> *Local condition.* By Lemma 2 the separation between the simultaneous events is $\overrightarrow{A_{(\lambda)}A_{(\lambda+d\lambda)}} = c\,dt\,U + d\vec\ell + dt\,\vec V$. Imposing orthogonality to $U'_{(\lambda)} = \Gamma(U + c^{-1}\vec V)$ and simplifying with $U\cdot U = 1$, $U\cdot\vec V = 0$, $U\cdot d\vec\ell = 0$, $1 - \vec V\cdot\vec V/c^2 = \Gamma^{-2}$ (Lemma 3) gives the **local synchronization condition**
> $$dt = \Gamma^2\,\frac{\vec V\cdot d\vec\ell}{c^2}.$$
> Two neighbouring corotating observers can therefore always be synchronized.
>
> *Global obstruction.* By Lemma 4, summing $dt$ around a closed loop $\mathscr{C}$ and converting to $\mathcal{O}'_{(0)}$'s proper time,
> $$\Delta t'_{\text{desync}} = \frac{1}{c^2\Gamma_{(0)}}\oint_{\mathscr{C}}\Gamma^2\vec V\cdot d\vec\ell.$$
> At constant radius this equals $\pm 2\pi\Gamma r^2\omega/c^2$; for small velocities, by Stokes' theorem and $\mathrm{curl}\,\vec V = 2\vec\omega$, it equals $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$. Since $\omega\ne 0$, this is nonzero, so the synchronization cannot be made globally consistent: returning to the starting observer, the clock is offset by $\Delta t'_{\text{desync}}$. $\blacksquare$
>
> *Remark.* The same desynchronization arises from **slow clock transport** (carrying a single clock slowly around the loop rather than exchanging light signals): in the limit of vanishing transport velocity the offset again approaches $\Delta t'_{\text{desync}}$, so the two synchronization procedures fail identically. This is not a Newtonian limit — in Newtonian physics all observers share absolute time and $\Delta t'_{\text{desync}} = 0$; the surviving $c^2$ is the signature of the relativistic origin.

---

# Cross-Field Exercise Suggestions

**The Sagnac effect and ring-laser gyroscopes.** The Sagnac delay between counter-propagating signals is exactly $2\Delta t'_{\text{desync}}$, so this theorem is the foundation of every ring-laser and fibre-optic gyroscope. The application is nonobvious because the gyroscope problem is usually framed in terms of light propagation, whereas it is really about the impossibility of synchronizing the clocks around the loop.

**GPS and relativistic geodesy.** The Global Positioning System distributes time from satellites to ground receivers on the rotating Earth; the Sagnac correction it must apply is the desynchronization gap of this theorem for the relevant light path. The application is out-of-distribution because it places an abstract cohomological obstruction at the heart of a consumer navigation technology, and getting it wrong would accumulate positioning errors of kilometres per day.

**The Aharonov–Bohm effect.** The desynchronization is a line integral of a "vector potential" ($\Gamma^2\vec V$) around a loop, equal to a flux of a "field" ($2\vec\omega$) through the enclosed area, with no local way to detect the field along the path — structurally identical to the quantum-mechanical Aharonov–Bohm phase. The application is surprising because it connects a classical rotating-frame timekeeping obstruction to a quantum interference phenomenon, via the shared mathematics of non-exact one-forms.

---

# Bridges

- **[[Thm - The Sagnac Effect]]** — the Sagnac delay *is* twice this desynchronization gap: $\Delta t' = 2\Delta t'_{\text{desync}}$. A prograde signal accumulates $+\Delta t'_{\text{desync}}$ around the loop and a retrograde one $-\Delta t'_{\text{desync}}$, so their arrival-time difference is the sum. This theorem is therefore the parent of the Sagnac effect, and the two share the same circulation integral; the Sagnac section simply reinterprets the synchronization gap as a measurable arrival-time difference.

- **Stokes' theorem and de Rham cohomology** — the impossibility of global synchronization is the statement that the synchronization one-form $\Gamma^2\vec V\cdot d\vec\ell$ is *closed but not exact* on the disk-minus-axis, a nontrivial element of the first de Rham cohomology of the punctured disk. The loop integral measures the cohomology class. This is the same mathematics by which a magnetic flux confined to a solenoid produces a nontrivial vector-potential holonomy in the field-free exterior — the geometric content is identical, with $2\vec\omega$ playing the role of the confined flux density.

- **[[Def - The Ehrenfest Paradox]]** — the desynchronization (a failure to integrate a *time* one-form consistently) and the Ehrenfest non-Euclidean geometry (a failure to integrate a *length* one-form consistently) are the temporal and spatial faces of the same fact: the corotating congruence has nonzero vorticity and admits no global rest space. The Ehrenfest circumference excess and the synchronization gap are both circulations of the rotating congruence's structure around a loop.

- **Kelvin's circulation theorem (fluid dynamics)** — the synchronization gap is the circulation of (a metric-weighted) velocity around a loop, and its evaluation as a vorticity flux is exactly Kelvin's/Stokes' relation between circulation and enclosed vorticity. The four-rotation $\vec\omega$ is the relativistic vorticity, and a rotating disk is a rigid-rotation flow with vorticity $2\vec\omega$.

---

# Unlocked by This

> [!tip] International Atomic Time and Relativistic Geodesy *(from Metrology)*
> This theorem is why **International Atomic Time (TAI)** cannot be defined by simply averaging the world's atomic clocks. Each ground clock reads the proper time of a corotating observer on the spinning Earth, and combining them requires correcting each by the integral of the synchronization gap to a common inertial reference (Geocentric Coordinate Time, TCG). The correction term is the desynchronization derived here, and applying it correctly — together with the gravitational redshift — is the foundation of modern timekeeping, satellite navigation, and the emerging field of relativistic geodesy, in which differences between clock rates measure the gravitational potential.

> [!tip] The Mashhoon Effect and Spin–Rotation Coupling *(from Relativistic Quantum Mechanics)*
> The coupling of the rotating frame to physical fields, of which the synchronization gap is the classical manifestation, extends to quantum spin: a particle's spin couples to the rotation $\vec\omega$ of the frame through a term $-\vec\omega\cdot\vec S$ in the effective Hamiltonian, the **Mashhoon spin–rotation coupling**. This is the rotational analogue of the Sagnac phase for spin, observable in neutron and atom interferometry, and it is the reason a rotating frame is not equivalent to an inertial frame even for spin degrees of freedom.
