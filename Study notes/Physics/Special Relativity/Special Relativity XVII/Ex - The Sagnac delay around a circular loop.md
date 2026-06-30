---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Sagnac Effect"
  - "Thm - Relativistic Velocity Addition"
  - "Def - Uniformly Rotating Observer"
tags: [physics, special-relativity]
---

# Problem Statement

A corotating observer $\mathcal{O}'$ at radius $r$ on a disk of angular velocity $\omega$ emits two light pulses at the same event, one prograde (with the rotation) and one retrograde, each travelling once around the circle of radius $r$ before returning to $\mathcal{O}'$. Working with $c = 1$ where convenient:

1. In the inertial frame, write the worldlines of the two pulses as helices with inertial angular velocities $\Omega_+ > 0$ and $\Omega_- < 0$, and find the return times $t_{B_\pm}$ when each pulse rejoins the (moving) emitter.
2. Convert to the emitter's proper time and obtain $\Delta t' = \frac{2\pi}{\Gamma}\big(\frac{1}{\Omega_+ - \omega} + \frac{1}{\Omega_- - \omega}\big)$.
3. Use the relativistic velocity-composition law to express $\Omega_\pm$ in terms of the common signal speed $v$ relative to corotating observers, and show the signal speed $v$ cancels, leaving $\Delta t' = 4\pi\Gamma r^2\omega/c^2$.
4. Confirm this equals twice the desynchronization gap, and check the small-velocity form $\Delta t'\simeq 4\omega A/c^2$ with $A = \pi r^2$.

**Recall:**

![[Thm - The Sagnac Effect#Statement]]

The [[Thm - Relativistic Velocity Addition|relativistic velocity-composition law]] for collinear velocities: a signal moving at speed $v$ relative to a frame that itself moves at $r\omega$ (the rim) has inertial speed $r\Omega_+ = (v + r\omega)/(1 + r\omega v/c^2)$ (prograde) or, with $v\to -v$, the retrograde value. A [[Def - Uniformly Rotating Observer|corotating observer]] has Lorentz factor $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$.

---

# Convergent Strategy

**Problem class.** A *counter-propagation* problem, the §17.3 type. The [[Special Relativity XVII — Rotating Observers#Problem-Solving Strategy|topic strategy]]: write the two signal worldlines as helices, solve for the return times, and difference them; the velocity-composition law supplies the inertial angular velocities.

**Assumption pattern.** Two signals of equal speed sent in opposite senses around a rotating loop. The signpost is "prograde and retrograde signals returning to a moving emitter": the prograde signal must chase the receding emitter (longer time), the retrograde meets the approaching emitter (shorter time), and the difference is the Sagnac delay.

**Theorem routing.** Parts 1–2 solve the helix-meeting condition $\Omega_\pm t_{B_\pm} = \omega t_{B_\pm}\pm 2\pi$ and convert to proper time; part 3 substitutes the [[Thm - Relativistic Velocity Addition|velocity-composition law]] and watches $v$ cancel, recovering [[Thm - The Sagnac Effect]]; part 4 checks against the desynchronization gap.

**Key decision point.** The crux is the meeting condition: the prograde signal returns when it has gained one full turn *on the emitter* (not on a fixed point), i.e. $\Omega_+ t = \omega t + 2\pi$. Getting the $\pm 2\pi$ and the emitter's motion right is the whole subtlety. The non-obvious payoff is that the signal speed $v$ cancels from the final answer — the hallmark of the Sagnac effect's speed-independence.

---

# Legal Operations Used

1. **Operation 1 from the topic page (helical worldlines).** The two signal worldlines are helices with angular velocities $\Omega_\pm$; their meeting with the emitter's helix gives the return times.

2. **Operation 7 from the topic page (relativistic velocity composition).** $r\Omega_\pm = (\pm v + r\omega)/(1\pm r\omega v/c^2)$ converts the signal speed relative to the disk into the inertial angular velocity.

3. **Operation 8 from the topic page (equal signal speeds relative to corotating observers).** Setting $v_+ = v_- = v$ (here $= c$ for light) makes the proper travel times equal and the delay twice the desynchronization gap.

---

# Hints

> [!note]- Hint 1
> The prograde signal at inertial angular velocity $\Omega_+$ catches the emitter (at angular position $\omega t$) after gaining one full turn: $\Omega_+ t_{B_+} = \omega t_{B_+} + 2\pi$, so $t_{B_+} = 2\pi/(\Omega_+ - \omega)$. The retrograde signal ($\Omega_- < 0$) meets the emitter after the emitter has gone one turn the other way: $\Omega_- t_{B_-} = \omega t_{B_-} - 2\pi$, so $t_{B_-} = 2\pi/(\omega - \Omega_-)$.

> [!note]- Hint 2
> The emitter's proper-time delay is $\Delta t' = \Gamma^{-1}(t_{B_+} - t_{B_-})$ (convert inertial time to corotating proper time via $d\tau = \Gamma^{-1}dt$). Substitute $t_{B_\pm}$ from Hint 1.

> [!note]- Hint 3
> From velocity composition, $r\Omega_+ = (v + r\omega)/(1 + r\omega v/c^2)$, so $\Omega_+ - \omega = \frac{(v + r\omega) - r\omega(1 + r\omega v/c^2)}{r(1 + r\omega v/c^2)} = \frac{v(1 - r^2\omega^2/c^2)}{r(1 + r\omega v/c^2)} = \frac{v\,\Gamma^{-2}}{r(1 + r\omega v/c^2)}$. Similarly for $\Omega_- - \omega$ with $v\to -v$. Add the reciprocals and watch $v$ cancel.

> [!note]- Hint 4
> The desynchronization gap at constant radius is $\Delta t'_{\text{desync}} = 2\pi\Gamma r^2\omega/c^2$. The Sagnac delay should be exactly twice this. For the small-velocity form, $\Gamma\to 1$ and $A = \pi r^2$, so $4\pi\Gamma r^2\omega/c^2\to 4\omega(\pi r^2)/c^2 = 4\omega A/c^2$.

---

# Solution

The route has four steps. Step 1 solves the helix-meeting conditions for the return times. Step 2 converts to the emitter's proper time. Step 3 substitutes velocity composition and watches the signal speed $v$ cancel, giving $\Delta t' = 4\pi\Gamma r^2\omega/c^2$. Step 4 confirms it is twice the desynchronization gap and reduces to $4\omega A/c^2$. The non-obvious move is the cancellation of $v$, which proves the speed-independence.

**Step 1: The return times are $t_{B_+} = 2\pi/(\Omega_+ - \omega)$ and $t_{B_-} = 2\pi/(\omega - \Omega_-)$.**

> [!note]- Derivation
> The prograde signal's worldline is $x_*(t) = r\cos\Omega_+ t$, $y_*(t) = r\sin\Omega_+ t$ with $\Omega_+ > 0$; the emitter sits at angular position $\omega t$ (choosing $\varphi = 0$). The signal returns to the emitter when their angular positions coincide modulo $2\pi$ — specifically, when the prograde signal has gained exactly one full turn on the emitter:
> $$\Omega_+ t_{B_+} = \omega t_{B_+} + 2\pi \;\Longrightarrow\; t_{B_+} = \frac{2\pi}{\Omega_+ - \omega}.$$
> The retrograde signal ($\Omega_- < 0$) goes the other way; it meets the emitter when it has lost one full turn (the $-2\pi$ accounting for the retrograde sense):
> $$\Omega_- t_{B_-} = \omega t_{B_-} - 2\pi \;\Longrightarrow\; t_{B_-} = \frac{2\pi}{\omega - \Omega_-}.$$

**Step 2: The proper-time delay is $\Delta t' = \frac{2\pi}{\Gamma}\big(\frac{1}{\Omega_+ - \omega} + \frac{1}{\Omega_- - \omega}\big)$.**

> [!note]- Derivation
> The emitter's proper-time interval between the two return events $B_+$ and $B_-$ is $\Delta t' = \Gamma^{-1}(t_{B_+} - t_{B_-})$ (the inertial-time interval converted to corotating proper time). Substituting,
> $$\Delta t' = \frac{1}{\Gamma}\left(\frac{2\pi}{\Omega_+ - \omega} - \frac{2\pi}{\omega - \Omega_-}\right) = \frac{2\pi}{\Gamma}\left(\frac{1}{\Omega_+ - \omega} + \frac{1}{\Omega_- - \omega}\right),$$
> using $-1/(\omega - \Omega_-) = 1/(\Omega_- - \omega)$. (Both terms are positive: $\Omega_+ > \omega$ and $\Omega_- < \omega$, so $\Omega_- - \omega < 0$, but combined with the helix geometry the delay comes out positive.)

**Step 3: Velocity composition gives $\Delta t' = 4\pi\Gamma r^2\omega/c^2$, with $v$ cancelling.**

> [!note]- Derivation
> The relativistic [[Thm - Relativistic Velocity Addition|velocity-composition law]] gives the inertial signal speed from the speed $v$ relative to the disk and the rim speed $r\omega$:
> $$r\Omega_+ = \frac{v + r\omega}{1 + r\omega v/c^2}.$$
> Then
> $$\Omega_+ - \omega = \frac{(v + r\omega) - r\omega(1 + r\omega v/c^2)}{r(1 + r\omega v/c^2)} = \frac{v(1 - r^2\omega^2/c^2)}{r(1 + r\omega v/c^2)} = \frac{v\,\Gamma^{-2}}{r(1 + r\omega v/c^2)}.$$
> For the retrograde signal, replace $v\to -v$: $\Omega_- - \omega = -\frac{v\,\Gamma^{-2}}{r(1 - r\omega v/c^2)}$, so $\frac{1}{\Omega_- - \omega} = -\frac{r(1 - r\omega v/c^2)}{v\,\Gamma^{-2}}$ — and reusing the combination, the reciprocals add to
> $$\frac{1}{\Omega_+ - \omega} + \frac{1}{\Omega_- - \omega} = \frac{r\Gamma^2}{v}\big[(1 + r\omega v/c^2) - (1 - r\omega v/c^2)\big] = \frac{r\Gamma^2}{v}\cdot\frac{2r\omega v}{c^2} = \frac{2r^2\omega\Gamma^2}{c^2}.$$
> The signal speed $v$ has **cancelled**. Substituting into Step 2,
> $$\Delta t' = \frac{2\pi}{\Gamma}\cdot\frac{2r^2\omega\Gamma^2}{c^2} = \frac{4\pi\Gamma r^2\omega}{c^2}.$$
> This matches [[Thm - The Sagnac Effect]], and the cancellation of $v$ proves the delay is **independent of the signal speed**.

**Step 4: This is twice the desynchronization gap and reduces to $4\omega A/c^2$.**

> [!note]- Derivation
> The desynchronization gap at constant radius is $\Delta t'_{\text{desync}} = 2\pi\Gamma r^2\omega/c^2$ (from [[Thm - Impossibility of Global Clock Synchronization on a Rotating Disk]]). The Sagnac delay is
> $$\Delta t' = \frac{4\pi\Gamma r^2\omega}{c^2} = 2\cdot\frac{2\pi\Gamma r^2\omega}{c^2} = 2\Delta t'_{\text{desync}},$$
> exactly twice — the prograde signal accumulates $+\Delta t'_{\text{desync}}$ and the retrograde $-\Delta t'_{\text{desync}}$. For small velocities, $\Gamma\to 1$ and the enclosed area is $A = \pi r^2$, so
> $$\Delta t' \to \frac{4\pi r^2\omega}{c^2} = \frac{4\omega(\pi r^2)}{c^2} = \frac{4\omega A}{c^2},$$
> the universal small-velocity Sagnac formula.

> [!note]- Complete formal solution
> The two pulses, as helices with inertial angular velocities $\Omega_\pm$, return to the emitter at $t_{B_+} = 2\pi/(\Omega_+ - \omega)$, $t_{B_-} = 2\pi/(\omega - \Omega_-)$. The proper-time delay is $\Delta t' = \Gamma^{-1}(t_{B_+} - t_{B_-}) = \frac{2\pi}{\Gamma}(\frac{1}{\Omega_+ - \omega} + \frac{1}{\Omega_- - \omega})$. Velocity composition gives $\Omega_\pm - \omega = \pm v\Gamma^{-2}/[r(1\pm r\omega v/c^2)]$, so the reciprocals sum to $2r^2\omega\Gamma^2/c^2$ with $v$ cancelling, yielding $\Delta t' = 4\pi\Gamma r^2\omega/c^2$. This is $2\Delta t'_{\text{desync}}$ and reduces to $4\omega A/c^2$ ($A = \pi r^2$) for small velocities. $\blacksquare$

**Frame-invariance check.** The same delay follows from the synchronization route: each signal's arrival time is its (equal) proper travel time plus $\pm\Delta t'_{\text{desync}}$, so $\Delta t' = 2\Delta t'_{\text{desync}} = 4\pi\Gamma r^2\omega/c^2$ — agreeing with the direct helix computation. The two independent routes confirm the result.

---

# Key Takeaways

**The Sagnac delay comes from the emitter moving while the signals travel — chase versus meet.** In the inertial frame, both signals travel at the same speed, but the prograde signal must *chase* the emitter, which has moved forward along the circle, so it travels a longer arc and arrives later; the retrograde signal *meets* the emitter coming the other way, traveling a shorter arc and arriving sooner. The difference is the Sagnac delay. The trigger for this picture is any counter-propagating signals returning to a moving source: the asymmetry is in the source's motion, not the signals'. This is the most intuitive route to the effect, and it makes the sign obvious (prograde later). The helix-meeting conditions $\Omega_\pm t = \omega t\pm 2\pi$ encode exactly this chase-versus-meet geometry, and getting the $\pm 2\pi$ right — one full turn gained or lost on the emitter — is the crux of the calculation.

**The cancellation of the signal speed $v$ is the signature of the Sagnac effect's metric origin.** When the velocity-composition algebra is carried through, the signal speed $v$ drops out entirely, leaving $\Delta t' = 4\pi\Gamma r^2\omega/c^2$ with the $c^2$ from the metric, not the propagation. This cancellation is not an accident — it is the mathematical expression of the fact that the Sagnac delay is twice the clock-desynchronization gap, a property of the rotating frame's geometry independent of any signal. The trigger to expect this is the structure of the velocity-composition law: when you compose $\pm v$ with $r\omega$ and difference the results, the $v$-dependent factors are symmetric and cancel. The lesson transfers to the matter-wave Sagnac effect, where the same speed-independence means a slow atom and a fast photon suffer the same delay — and where one must therefore *not* replace the metric $c^2$ by the particle's phase velocity. The cancellation of $v$ is the cleanest demonstration that the Sagnac effect is about spacetime geometry, not propagation.

**Two independent routes — direct helix and synchronization gap — confirm the same delay, which is the hallmark of a robust physical result.** The Sagnac delay can be derived by writing the signal worldlines explicitly and differencing return times, or by recognizing it as twice the desynchronization gap; both give $4\pi\Gamma r^2\omega/c^2$. The trigger to seek a second route is any result that "feels" like it might depend on hidden assumptions: deriving it two ways, especially when one route is geometric (the synchronization gap, a circulation) and the other kinematic (the helix, a velocity composition), confirms it is frame-independent and assumption-free. The agreement also illuminates the physics: the kinematic route shows the chase-versus-meet mechanism, while the synchronization route shows the deeper origin in the impossibility of global time. When two such different methods converge, you have understood the effect, not just computed it. See [[Ex - The impossibility of global synchronization and the time gap around a loop]] for the desynchronization gap this delay doubles.
