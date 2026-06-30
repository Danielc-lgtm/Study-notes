---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Angular Distribution of Radiation"
  - "Thm - Radiation by an Accelerated Charge (Larmor Formula)"
  - "Def - Synchrotron Radiation"
tags: [physics, special-relativity]
---

# Problem Statement

The radiation of an ultrarelativistic charge is **beamed** into a narrow forward cone of half-angle $\sim 1/\Gamma$, a phenomenon called *relativistic beaming* or *Doppler boosting*. The exercise is to derive the cone half-angle from the Doppler factor in the angular-distribution formula, see how the maxima of the radiation pattern depend on $\Gamma$ in the collinear and orthogonal cases, and recognise the astrophysical consequence (one-sided jets). Working with $c = 1$ except where $c$ is restored, mostly-minus signature:

1. **The universal beaming scale $\theta \sim 1/\Gamma$.** The relativistic angular-distribution formula for an accelerated charge contains the factor $(1 - \tfrac Vc\cos\theta)^{-n}$ ($n = 6$ for collinear acceleration, smaller powers for other geometries). Show that for $\Gamma\gg 1$,
$$1 - \tfrac Vc\cos\theta \approx \frac{1 + \Gamma^2\theta^2}{2\Gamma^2}\qquad\text{for small } \theta,$$
by expanding $V/c = 1 - 1/(2\Gamma^2) + O(\Gamma^{-4})$ and $\cos\theta \approx 1 - \theta^2/2$. Conclude that the factor is *small* — i.e. the radiation is *enhanced* — when $\Gamma^2\theta^2 \lesssim 1$, defining the beaming cone $\theta \lesssim 1/\Gamma$.

2. **Collinear case: maxima at $\theta_\pm \simeq \pm 1/(\sqrt5\,\Gamma)$.** For a charge with $\boldsymbol\gamma\parallel\mathbf V$ (linear accelerator), the angular distribution is
$$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} \propto \frac{\sin^2\theta}{(1 - \tfrac Vc\cos\theta)^6}.$$
The on-axis emission vanishes (by $\sin^2\theta = 0$), so the maxima sit just off-axis. Find them in the ultrarelativistic limit using Part 1: write $u = \Gamma\theta$, expand $\sin^2\theta \approx \theta^2$, and maximise $u^2/(1 + u^2)^6$ to find $u_\pm = \pm 1/\sqrt5$, i.e.
$$\theta_\pm \simeq \pm\frac{1}{\sqrt5\,\Gamma}.$$

3. **Orthogonal (synchrotron) case: forward cone of half-angle $1/\Gamma$.** For $\boldsymbol\gamma\perp\mathbf V$ (circular motion), the on-axis emission does *not* vanish; the angular distribution has a maximum at $\theta = 0$ and falls off when $\Gamma\theta \gtrsim 1$. Sketch the pattern as a forward-pointing cone of half-angle $\sim 1/\Gamma$, and explain why this is the *synchrotron* beaming case: the orbit is in the plane orthogonal to $\mathbf B$, the velocity sweeps around the orbit, and the cone of radiation sweeps with it like a lighthouse beam.

4. **Astrophysical consequence — one-sided jets.** A relativistic jet (e.g. from an active galactic nucleus, AGN) emits radiation isotropically in its own rest frame. In our frame, the approaching jet's radiation is concentrated in our line of sight with intensity boosted by a factor of order $\Gamma^3$ to $\Gamma^4$, while the receding jet's radiation is beamed *away* from us with intensity *suppressed* by the same factor. Estimate the intensity ratio approaching/receding for $\Gamma = 10$ and explain why intrinsically two-sided jets appear *one-sided* in our images.

**Recall:**

The exercise rests on the angular distribution of radiation and the Doppler factor.

![[Thm - Angular Distribution of Radiation#Statement]]

The radiation pattern of a non-relativistic accelerated charge is the dipole donut $\mathrm d\mathcal P/\mathrm d\Omega\propto\sin^2\theta$ (with $\theta$ the angle from the acceleration). For an ultrarelativistic charge the pattern is multiplied by powers of the inverse Doppler factor $(1 - \tfrac Vc\cos\theta)^{-n}$, which becomes small near $\theta = 0$, sweeping the radiation into a forward cone.

---

# Convergent Strategy

**Problem class.** A *find-the-beaming-angle* problem — a particularly clean asymptotic analysis. The [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy#Problem-Solving Strategy|topic strategy]] for direction-of-radiation: expand the Doppler factor near $\theta = 0$ to leading order in $1/\Gamma$, then find where the angular distribution is large; the boundary of "large" defines the cone.

**Assumption pattern.** Two signposts. (i) "Ultrarelativistic", $\Gamma\gg 1$, which lets $1/\Gamma$ be the small parameter for asymptotic expansion. (ii) The angular distribution's $(1 - V\cos\theta/c)^{-n}$ factor, where $n$ depends on the case (6 for collinear, 4 or 5 for orthogonal in different conventions). Once you have this factor, the rest is calculus.

**Theorem routing.** Part 1: Taylor expand $V/c$ and $\cos\theta$, combine, identify the natural variable $u = \Gamma\theta$. Part 2: maximise $u^2/(1+u^2)^6$ by differentiating. Part 3: maximise $1/(1+u^2)^n$, which has its maximum at $u = 0$ — the cone is rooted on-axis. Part 4: ratio of approaching/receding fluxes is $((1+V/c)/(1-V/c))^n \sim (2\Gamma^2)^n$ for $V\to c$.

**Key decision point.** The crux of Parts 2 and 3 is recognising that the natural variable is $u = \Gamma\theta$, not $\theta$. In the variable $u$ the angular distribution is *$\Gamma$-independent* — the same function $f(u)$ for every $\Gamma$ — and the cone half-angle is $u\sim 1$, i.e. $\theta\sim 1/\Gamma$. This kind of *rescaling to expose universality* is the master technique of asymptotic expansion.

---

# Legal Operations Used

1. **Read beaming from the Doppler factor** (operation 9 from the topic page): the relativistic distortion of the angular pattern is the factor $(1 - V\cos\theta/c)^{-n}$, which for $\Gamma\gg 1$ collimates the emission into a forward cone of half-angle $\sim 1/\Gamma$.

2. **Express the four-acceleration invariant in laboratory variables** (operation 8): the collinear vs orthogonal distinction is about whether $\boldsymbol\gamma$ is parallel or perpendicular to $\mathbf V$, which controls the form of the angular distribution.

3. **Use the dipole pattern's vanishing on-axis** (operation 1, dipole donut content): in the collinear case the $\sin^2\theta$ factor kills on-axis emission, forcing the maxima off-axis; in the orthogonal case the angular numerator does *not* vanish on-axis, so the cone points forward.

---

# Hints

> [!note]- Hint 1
> Expand $V/c$ and $\cos\theta$ for $\Gamma\gg 1$ and small $\theta$: $V/c = \sqrt{1 - 1/\Gamma^2} \approx 1 - 1/(2\Gamma^2)$. Then $1 - (V/c)\cos\theta = 1 - (1 - 1/(2\Gamma^2))(1 - \theta^2/2) = 1 - 1 + 1/(2\Gamma^2) + \theta^2/2 - \theta^2/(4\Gamma^2) \approx 1/(2\Gamma^2) + \theta^2/2 = (1 + \Gamma^2\theta^2)/(2\Gamma^2)$. The factor is *small* (radiation enhanced) when $\Gamma^2\theta^2 \lesssim 1$, i.e. $\theta\lesssim 1/\Gamma$.

> [!note]- Hint 2
> Variable change $u = \Gamma\theta$. The denominator becomes $(1 - V\cos\theta/c)^6 \to ((1+u^2)/(2\Gamma^2))^6 = (1+u^2)^6/(2\Gamma^2)^6$. The numerator $\sin^2\theta\approx\theta^2 = u^2/\Gamma^2$. So $\mathrm d\mathcal P/\mathrm d\Omega\propto u^2/\Gamma^2 \cdot (2\Gamma^2)^6/(1+u^2)^6 =$ constant in $\Gamma$, times $u^2/(1+u^2)^6$. Maximise: derivative of $\log f(u) = 2\log u - 6\log(1+u^2)$ gives $2/u - 12u/(1+u^2) = 0$, so $1 + u^2 = 6u^2$, $u^2 = 1/5$, $u = \pm 1/\sqrt5$. Hence $\theta_\pm = \pm 1/(\sqrt5\Gamma)$.

> [!note]- Hint 3
> In the orthogonal case the velocity is in the orbit plane, perpendicular to the line of sight (for an observer in the orbit plane). The on-axis emission is large rather than zero; the angular distribution at $\theta = 0$ is *not* killed by any $\sin^2\theta$ factor in this geometry (the $\sin\theta$-like factors arise relative to *different* axes). The dominant $\Gamma$-dependence is the inverse Doppler $(1 - V\cos\theta/c)^{-n}$ with $n = 4$ (combining intrinsic dipole and Doppler effects), maximal at $\theta = 0$, falling off as $\theta \gtrsim 1/\Gamma$. The beam is a forward cone, not split lobes.

> [!note]- Hint 4
> Intensity boost: a source emitting isotropic intensity $I_0$ in its rest frame appears, in the lab frame at angle $\theta$ to its velocity, with intensity $I = I_0/(\Gamma(1 - V\cos\theta/c))^4$ (the relativistic-Doppler effect for surface brightness). On-axis approaching ($\theta = 0$, $V/c \to 1$): $I_{\text{approach}}/I_0 = (\Gamma(1 - V/c))^{-4} \approx (\Gamma\cdot 1/(2\Gamma^2))^{-4} = (2\Gamma)^4 \approx 16\Gamma^4$. On-axis receding ($\theta = \pi$, $\cos\theta = -1$): $I_{\text{recede}}/I_0 = (\Gamma(1 + V/c))^{-4} \approx (2\Gamma)^{-4}$. Ratio: $I_{\text{approach}}/I_{\text{recede}} = (1 + V/c)^4/(1 - V/c)^4 \approx (2/(1/(2\Gamma^2)))^4 = (4\Gamma^2)^4 = 256\Gamma^8$. For $\Gamma = 10$: ratio $\approx 2.6\times 10^{10}$ — the receding jet is suppressed by *ten orders of magnitude*.

---

# Solution

The Doppler factor $(1 - V\cos\theta/c)$ becomes small for $\Gamma\theta\lesssim 1$, beaming the radiation into a forward cone of half-angle $1/\Gamma$. In the collinear case the on-axis $\sin^2\theta$ vanishing pushes the maxima to $\theta_\pm = \pm 1/(\sqrt5\Gamma)$; in the orthogonal (synchrotron) case the cone points forward. Astrophysically, this enhances approaching jets by $\sim\Gamma^4$ and suppresses receding ones by $\sim\Gamma^{-4}$, making intrinsically two-sided structures appear one-sided.

**Step 1: The universal beaming scale.**

> [!note]- Derivation
> The Doppler factor $1 - V\cos\theta/c$ governs every relativistic radiation pattern. Expand for $\Gamma\gg 1$ and $\theta$ small. From $\Gamma^2 = 1/(1 - V^2/c^2)$,
> $$\frac{V}{c} = \sqrt{1 - \frac{1}{\Gamma^2}} = 1 - \frac{1}{2\Gamma^2} - \frac{1}{8\Gamma^4} + O(\Gamma^{-6}).$$
> Combined with $\cos\theta = 1 - \theta^2/2 + O(\theta^4)$,
> $$1 - \frac{V}{c}\cos\theta = 1 - \left(1 - \frac{1}{2\Gamma^2}\right)\left(1 - \frac{\theta^2}{2}\right) = \frac{1}{2\Gamma^2} + \frac{\theta^2}{2} - \frac{\theta^2}{4\Gamma^2}.$$
> The last term is $O(\Gamma^{-4}\theta^2)$, negligible compared to the other two, so
> $$\boxed{1 - \frac{V}{c}\cos\theta \approx \frac{1 + \Gamma^2\theta^2}{2\Gamma^2}\qquad(\Gamma\gg 1,\;\theta\ll 1).}$$
> The factor is at its minimum when $\theta = 0$, where it equals $1/(2\Gamma^2)$ — exponentially small for large $\Gamma$. It rises rapidly: by the time $\Gamma\theta = 1$, the factor has *doubled* from its minimum, and the inverse Doppler $(1 - V\cos\theta/c)^{-n}$ has fallen by $2^n$. The natural angular variable is $u = \Gamma\theta$, and *significant radiation lives in $u\lesssim 1$* — the cone $\theta\lesssim 1/\Gamma$.
>
> The cone half-angle $1/\Gamma$ is universal: it appears in *every* relativistic radiation problem, from synchrotron to inverse Compton, from particle bremsstrahlung to gravitational radiation, because it traces back to the single relativistic kinematic fact that aberration sweeps emitted directions forward into a cone of angular size $1/\Gamma$ around the velocity.

**Step 2: Collinear case maxima at $\pm 1/(\sqrt5\Gamma)$.**

> [!note]- Derivation
> For $\boldsymbol\gamma\parallel\mathbf V$ (linear accelerator, bremsstrahlung in a thin slab), the radiation pattern is
> $$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} \propto \frac{\sin^2\theta}{(1 - V\cos\theta/c)^6}.$$
> The $\sin^2\theta$ in the numerator is the dipole donut — radiation vanishes along the acceleration axis ($\theta = 0$ or $\pi$). The $(1 - V\cos\theta/c)^{-6}$ in the denominator is the relativistic boost, pushing emission forward. The two compete: the donut wants to suppress $\theta = 0$, the Doppler wants to enhance it. The maxima sit where they balance.
>
> Rescale $u = \Gamma\theta$ and substitute Part 1's expansion:
> $$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} \propto \frac{(u/\Gamma)^2}{((1+u^2)/(2\Gamma^2))^6} = \frac{u^2}{\Gamma^2}\cdot\frac{(2\Gamma^2)^6}{(1+u^2)^6} = \frac{64\Gamma^{10}\,u^2}{(1+u^2)^6}.$$
> The $\Gamma^{10}$ is the *overall* amplitude enhancement — radiation in the cone is huge — but the *shape* in $u$ is $\Gamma$-independent. To find the maxima of $f(u) = u^2/(1+u^2)^6$, take the logarithmic derivative:
> $$\frac{f'(u)}{f(u)} = \frac{2}{u} - \frac{12u}{1+u^2} = 0 \;\Longrightarrow\; 2(1+u^2) = 12u^2 \;\Longrightarrow\; 1 + u^2 = 6u^2 \;\Longrightarrow\; u^2 = \frac{1}{5}.$$
> So $u = \pm 1/\sqrt5$, giving
> $$\boxed{\theta_\pm = \pm\frac{1}{\sqrt5\,\Gamma}.}$$
> The pattern is a *split donut*: two lobes straddling the forward direction at angles $\pm 1/(\sqrt5\Gamma)$ ($\approx\pm 0.45/\Gamma$ in radians). The on-axis emission is exactly zero (forced by the dipole's vanishing on the acceleration axis), but the Doppler boost has packed all the radiation into a cone of $1/\Gamma$ around the axis — just with a thin null line through the centre. For $\Gamma = 1000$, the lobes are $\approx 0.45$ mrad off the velocity direction, and a detector misaligned by that much sees a sharp drop-off rather than the peak.

**Step 3: Orthogonal (synchrotron) case.**

> [!note]- Derivation
> For $\boldsymbol\gamma\perp\mathbf V$ (circular motion, synchrotron), the geometry is different. The acceleration is *in the orbit plane* but *perpendicular to the instantaneous velocity*; the dipole-donut pattern is rotationally symmetric around the *acceleration* axis (perpendicular to $\mathbf V$), so an observer at angle $\theta$ from $\mathbf V$ in the orbit plane does *not* see a zero from $\sin^2\theta = 0$ (their $\theta$ from $\boldsymbol\gamma$ is $\pi/2 - \theta$ from $\mathbf V$, where $\sin$ is generically nonzero). The on-axis emission is *finite*, and the Doppler factor $(1 - V\cos\theta/c)^{-n}$ (with $n = 4$ to $5$ depending on whether intensity per solid angle or per frequency is used) is *maximal* at $\theta = 0$.
>
> The radiation is a forward-pointing cone of half-angle $\sim 1/\Gamma$ around the instantaneous $\mathbf V$, with maximum intensity on-axis and falling smoothly to a fraction $2^{-n}$ at $u = \Gamma\theta = 1$. The pattern *rotates* with the charge around the orbit — as the velocity sweeps through $360°$ during one orbit, the cone sweeps with it like a lighthouse beam. A *distant* observer is illuminated only during the brief instant the cone points toward them, an angular fraction $1/\Gamma$ of the orbit; the rest of the orbit, the cone points elsewhere and the observer sees nothing.
>
> This explains the *broad synchrotron spectrum*: the observer receives short pulses of duration
> $$\Delta t_{\text{pulse}} \sim \frac{1}{\Gamma\cdot\Omega}\cdot\frac{1}{\Gamma^2} = \frac{1}{\Gamma^3\Omega}$$
> (the angular fraction $1/\Gamma$ of the period $1/\Omega$, further compressed by the factor $1/\Gamma^2$ from the relativistic Doppler shortening of the pulse as the source moves toward the observer during the emission). A short pulse of duration $\Delta t$ has Fourier content extending up to frequency $\sim 1/\Delta t = \Gamma^3\Omega = \Gamma^3 c/R$ — the *characteristic synchrotron frequency*, far above the orbital frequency. This is the cone half-angle of $1/\Gamma$ doing its decisive work on the *spectrum*: collimation in space implies broadband emission in time, and the spectral width is set by $\Gamma^3$.

**Step 4: One-sided jets and Doppler boosting.**

> [!note]- Derivation
> A relativistic plasma jet from an active galactic nucleus (AGN), or from a young stellar object, emits radiation isotropically in its own rest frame with rest-frame intensity $I_0$. In our (observer) frame, the intensity *as a function of direction* in the lab is obtained by Lorentz-transforming the source's emission. The result is the **Doppler boosting** formula
> $$I(\theta) = \frac{I_0}{\Gamma^4\,(1 - V\cos\theta/c)^4},$$
> with $\theta$ the angle in our frame between the jet's velocity and our line of sight. (The fourth power combines: one factor of Doppler shift for the photon energy, one for the rate of photon arrival, one for the relativistic aberration compressing the solid angle, one from $\mathrm d\nu/\mathrm d\nu'$ in the per-frequency formula — totalling $\delta^4$ where $\delta = 1/(\Gamma(1 - V\cos\theta/c))$ is the Doppler factor.)
>
> For an *approaching* jet ($\theta = 0$, $\cos\theta = 1$), with $V/c\to 1$:
> $$I_{\text{approach}} = I_0\,\delta^4 = \frac{I_0}{(\Gamma(1 - V/c))^4} \approx \frac{I_0}{(\Gamma/(2\Gamma^2))^4} = (2\Gamma)^4\,I_0 = 16\,\Gamma^4\,I_0.$$
> For a *receding* jet ($\theta = \pi$, $\cos\theta = -1$):
> $$I_{\text{recede}} = \frac{I_0}{(\Gamma(1 + V/c))^4} \approx \frac{I_0}{(2\Gamma)^4} = \frac{I_0}{16\Gamma^4}.$$
> Ratio:
> $$\frac{I_{\text{approach}}}{I_{\text{recede}}} = (2\Gamma)^8 = 256\,\Gamma^8.$$
> For $\Gamma = 10$: ratio $= 2.56\times 10^{10}$. The approaching jet outshines the receding jet by *ten orders of magnitude* — the receding jet is, effectively, *invisible*. This is why intrinsically two-sided astrophysical jets (e.g. the radio jets of M87, Centaurus A, and many AGN) appear *one-sided* in our images: the counter-jet is real and emits the same intrinsic power, but its radiation is beamed away from us by Doppler de-boosting.
>
> A subtle corollary: when we *do* see counter-jets (as in nearby radio galaxies with moderate $\Gamma$), the brightness ratio between jet and counter-jet *measures* the jet velocity and orientation, since the ratio depends on both $V$ and $\theta$ in a known way. This is one of the standard methods for inferring jet velocities in AGN.

> [!note]- Complete formal solution
> The Doppler factor $1 - V\cos\theta/c \approx (1 + \Gamma^2\theta^2)/(2\Gamma^2)$ for $\Gamma\gg 1$, $\theta\ll 1$, defines the universal beaming cone of half-angle $1/\Gamma$. *Collinear case* ($\boldsymbol\gamma\parallel\mathbf V$): the angular pattern $\sin^2\theta/(1 - V\cos\theta/c)^6$ rescaled to $u = \Gamma\theta$ becomes $u^2/(1+u^2)^6$, maximised at $u = \pm 1/\sqrt5$, giving lobes at $\theta_\pm = \pm 1/(\sqrt5\Gamma)$ with on-axis null. *Orthogonal case* ($\boldsymbol\gamma\perp\mathbf V$, synchrotron): on-axis emission is finite, the cone points forward and sweeps with the velocity like a lighthouse; the cone half-angle $1/\Gamma$ produces short pulses ($\Delta t\sim 1/(\Gamma^3\Omega)$) and hence the broad synchrotron spectrum up to characteristic frequency $\Gamma^3 c/R$. *Astrophysical Doppler boosting*: an isotropically emitting jet appears with intensity $I \propto \delta^4 = (\Gamma(1 - V\cos\theta/c))^{-4}$; approaching jet enhanced by $(2\Gamma)^4 \sim 16\Gamma^4$, receding suppressed by $(2\Gamma)^{-4}$, ratio $(2\Gamma)^8 \sim 256\Gamma^8$. For $\Gamma = 10$, ratio $\approx 2.6\times 10^{10}$ — intrinsically two-sided jets appear one-sided. $\blacksquare$

---

# Key Takeaways

**The $1/\Gamma$ cone is the universal beaming scale of relativistic radiation, and it traces to a single algebraic identity.** Whenever an ultrarelativistic source emits radiation, its angular pattern is concentrated in a forward cone of half-angle approximately $1/\Gamma$. This is not specific to electromagnetism — it appears in gravitational radiation from relativistic sources, in neutrino radiation from a relativistic shock, in pair-creation cascades in QED — because it traces to the kinematics of relativistic aberration, which sweeps directions forward by the same $1/\Gamma$ factor for any messenger field. The algebraic root is the identity $1 - V\cos\theta/c \approx (1 + \Gamma^2\theta^2)/(2\Gamma^2)$ for small $\theta$ and large $\Gamma$, whose minimum occurs at $\theta = 0$ and rises as $1 + (\Gamma\theta)^2$, so significant radiation lives in $\Gamma\theta\lesssim 1$. Whenever you meet a radiation problem with $\Gamma\gg 1$, rescale to $u = \Gamma\theta$, and the pattern's *shape* becomes $\Gamma$-independent — a clean asymptotic structure that lets you read off cone half-angles, maxima locations, and spectral widths without ever computing a single $\Gamma$-dependent integral.

**Collinear vs orthogonal: dipole-donut zero on-axis vs filled-in centre — small geometric distinction, large pattern difference.** The collinear case ($\boldsymbol\gamma\parallel\mathbf V$, linear acceleration) and the orthogonal case ($\boldsymbol\gamma\perp\mathbf V$, circular motion) differ only in whether the acceleration is parallel or perpendicular to the velocity, but the radiation patterns are qualitatively different: collinear has *no* on-axis emission (split lobes at $\theta_\pm \simeq \pm 1/(\sqrt5\Gamma)$), orthogonal has on-axis *peak* (filled-in forward cone). The reason is the dipole donut: $\sin^2\theta$ vanishes when $\hat{\mathbf n}\parallel\boldsymbol\gamma$, and in the collinear case the forward direction *is* the acceleration direction, killing the on-axis emission; in the orthogonal case the forward direction is perpendicular to $\boldsymbol\gamma$, where the donut is maximal. The reusable lesson: in any radiation problem, identify the angle between observation and acceleration directions, not between observation and velocity directions. The dipole pattern responds to the *acceleration* axis; the Doppler boost responds to the *velocity* axis; and the visible pattern is the product of these two angular dependences. The split-lobe vs filled-cone distinction is just the dipole donut wrapped around different axes by the Doppler factor.

**Astrophysical Doppler boosting turns isotropic emitters into knife-edge searchlights, with the boost factor $\delta^4$ swinging by twenty orders of magnitude between approaching and receding sources.** The brightness of a moving source as seen in our frame is $I = I_0\delta^4$, with $\delta = 1/(\Gamma(1 - V\cos\theta/c))$ the relativistic Doppler factor. The fourth power compounds four separate effects (energy shift, arrival-rate shift, solid-angle compression, bandwidth shift), and for $\Gamma\gg 1$ this $\delta^4$ varies between $\sim (2\Gamma)^4$ on-axis approaching and $\sim (2\Gamma)^{-4}$ on-axis receding — a swing of $(2\Gamma)^8$, which for typical AGN values $\Gamma\sim 10$ is ten orders of magnitude. The astrophysical reusability is enormous: (i) one-sided jets — the apparent asymmetry of intrinsically two-sided AGN jets is *purely* a Doppler boosting artefact, and the jet/counter-jet brightness ratio *measures* the jet velocity. (ii) Blazars — when an AGN jet happens to point near our line of sight, the Doppler boost of $\Gamma^4$ makes it appear up to $10^4$ times brighter than its isotropic luminosity, the reason blazars are the most luminous persistent objects in the universe at high energies. (iii) GRB afterglow geometry — the visible portion of a gamma-ray burst's emission is the $1/\Gamma$ cone toward us, and the *jet break* in the afterglow light curve (the dimming when the cone widens to include the jet's edge) directly measures the jet opening angle.
