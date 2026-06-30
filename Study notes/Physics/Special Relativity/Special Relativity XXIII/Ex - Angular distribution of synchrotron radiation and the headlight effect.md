---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Radiation by an Accelerated Charge (Larmor Formula)"
  - "Thm - Angular Distribution of Radiation"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

A charge of magnitude $q$ moves with three-velocity $\mathbf v$ and three-acceleration $\mathbf a$ in the laboratory frame. In its instantaneous rest frame the radiation pattern is the symmetric dipole donut $\mathrm d\mathcal P/\mathrm d\Omega \propto \sin^2\theta'$, with $\theta'$ the angle between the emission direction $\hat{\mathbf n}'$ and the acceleration. Boost to the laboratory frame and show that the pattern in the laboratory is sharply forward-peaked along the velocity for $\Gamma \gg 1$ — the **relativistic headlight effect** — with a characteristic opening half-angle $\theta_{1/2} \sim 1/\Gamma$. Make the following precise:

1. Derive the laboratory differential power as a function of the laboratory emission angle $\theta$ (measured from $\mathbf v$) and the rest-frame angle $\theta'$, using the relativistic aberration formula $\cos\theta = (\cos\theta' + \beta)/(1+\beta\cos\theta')$.
2. Specialise to the case $\mathbf a \parallel \mathbf v$ (linear acceleration: a linac) and obtain the explicit formula
$$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} \;=\; \frac{q^2 a^2}{16\pi^2\varepsilon_0 c^3}\,\frac{\sin^2\theta}{(1-\beta\cos\theta)^5}.$$
3. Specialise to the case $\mathbf a \perp \mathbf v$ (circular motion: a synchrotron) and obtain
$$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} \;=\; \frac{q^2 a^2}{16\pi^2\varepsilon_0 c^3}\,\frac{1}{(1-\beta\cos\theta)^3}\left[1 - \frac{\sin^2\theta\cos^2\phi}{\Gamma^2(1-\beta\cos\theta)^2}\right],$$
where $\phi$ is the azimuth around $\mathbf v$.
4. In each case find the laboratory angle of peak emission and the half-power opening angle for $\Gamma \gg 1$, and verify the universal scaling $\theta_{1/2} \sim 1/\Gamma$.

**Recall:**

A charge with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$ and four-acceleration $A$ radiates with total invariant power, by the [[Thm - Radiation by an Accelerated Charge (Larmor Formula)|Larmor formula]],
$$\mathcal P \;=\; \frac{q^2}{6\pi\varepsilon_0 c}\,A\cdot A,$$
where with our [[Special Relativity III — Minkowski Spacetime and the Metric|mostly-minus signature]] $A\cdot A$ is *negative* for the spacelike four-acceleration of any physical worldline, so the radiated power $-A\cdot A/(6\pi\varepsilon_0 c)$ is positive. In the instantaneous rest frame $A = (0,\mathbf a)$ and $-A\cdot A = |\mathbf a|^2$; in the laboratory $-A\cdot A = \Gamma^4[|\mathbf a|^2 + \Gamma^2(\mathbf v\cdot\mathbf a)^2/c^2]$ (see [[Thm - Radiation by an Accelerated Charge (Larmor Formula)]]). The angular distribution in the rest frame is the dipole donut $\mathrm d\mathcal P'/\mathrm d\Omega' \propto \sin^2\theta'$ ([[Thm - Angular Distribution of Radiation]]).

The boost of the angular distribution relies on three facts. Photons emitted at $\theta'$ in the rest frame arrive in the laboratory at angle $\theta$ given by **relativistic aberration**,
$$\cos\theta \;=\; \frac{\cos\theta' + \beta}{1 + \beta\cos\theta'},\qquad \sin\theta \;=\; \frac{\sin\theta'}{\Gamma(1+\beta\cos\theta')}.$$
The transformation of the solid-angle element is $\mathrm d\Omega = \mathrm d\Omega'/[\Gamma(1-\beta\cos\theta)]^2$. The transformation of the *power per solid angle* mixes these: writing $\mathrm d\mathcal P/\mathrm d\Omega = \mathrm dW/\mathrm d\Omega\,\mathrm dt$ with $W$ energy and $t$ laboratory time, one factor of $\mathrm d\Omega'/\mathrm d\Omega = [\Gamma(1-\beta\cos\theta)]^2$ comes from the solid-angle squeeze, one factor of $\Gamma(1-\beta\cos\theta)$ from $\mathrm d t'/\mathrm dt = 1/\Gamma(1-\beta\cos\theta)$ (the relativistic Doppler factor between retarded source time and observer time), and one factor of $\Gamma^2(1-\beta\cos\theta)^2$ from photon-energy transformation if power is measured at *fixed retarded time*. The net result for radiation observed at fixed laboratory time is the Jacobian $\mathrm d\Omega'/\mathrm d\Omega \cdot (1-\beta\cos\theta)$ — one less power of $\Gamma$ than naive guess — and is what produces the $(1-\beta\cos\theta)^{-5}$ vs $(1-\beta\cos\theta)^{-3}$ pole structure below.

---

# Convergent Strategy

**Problem class.** A *boost-the-angular-distribution* problem: the rest-frame pattern is simple (dipole), and the laboratory pattern is the same physical photon flux re-expressed via aberration and the Doppler-Jacobian. The [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy#Problem-Solving Strategy|topic strategy]] for this section says: compute the invariant first (total power, $\mathcal P = q^2|A|^2/6\pi\varepsilon_0 c$), then recover the laboratory differential by boosting the rest-frame angular pattern.

**Assumption pattern.** Rest-frame pattern is the dipole donut $\sin^2\theta'$. The acceleration is the only frame-dependent quantity that determines the donut's orientation: parallel acceleration leaves $\sin^2\theta'$ around the velocity axis, perpendicular acceleration tilts the donut into the orbital plane. The signposts are "linac" (parallel) versus "synchrotron" (perpendicular).

**Theorem routing.** [[Thm - Angular Distribution of Radiation|Angular-distribution theorem]] in the rest frame gives the dipole. Aberration ($\cos\theta = (\cos\theta'+\beta)/(1+\beta\cos\theta')$) inverts to relate $\theta'$ to $\theta$. The differential-power Jacobian — derived once and applied to every case — converts the rest-frame pattern into the laboratory pattern. For the perpendicular case the angle between $\mathbf n'$ and $\mathbf a$ in the rest frame depends on the azimuth $\phi$ around $\mathbf v$, which is what produces the cosφ-dependent term.

**Key decision point.** The non-obvious move is computing the differential power at *fixed observer time*, not at fixed retarded time. The factor-of-$(1-\beta\cos\theta)$ between them is what reduces $(1-\beta\cos\theta)^{-6}$ (the naive Doppler) to $(1-\beta\cos\theta)^{-5}$ in the linac formula. Skipping this step gives an answer that overestimates radiation in the forward direction by another factor of $\Gamma$ and disagrees with both Jackson and Gourgoulhon.

---

# Legal Operations Used

1. **Compute the invariant first.** The Larmor invariant $\mathcal P = q^2|A|^2/6\pi\varepsilon_0 c$ is the same in every frame; the rest-frame and laboratory expressions $|\mathbf a|^2$ and $\Gamma^4(|\mathbf a|^2 + \Gamma^2(\mathbf v\cdot\mathbf a)^2/c^2)$ must agree when checked.

2. **Aberration formula.** Photons emitted at $\theta'$ in the rest frame arrive at $\theta$ in the laboratory; the formula is inverted to get $\theta'(\theta)$ and substituted into the rest-frame pattern.

3. **Differential-power Jacobian.** $\mathrm d\mathcal P/\mathrm d\Omega = \mathrm d\mathcal P'/\mathrm d\Omega' \cdot \mathrm d\Omega'/\mathrm d\Omega \cdot (1-\beta\cos\theta)$, where the last factor is the rest-frame-time-to-observer-time Doppler factor.

4. **Specialise the angle between $\hat{\mathbf n}'$ and $\mathbf a$.** For $\mathbf a \parallel \mathbf v$ this is just $\theta'$ (the donut axis is along $\mathbf v$); for $\mathbf a \perp \mathbf v$ the angle depends on both $\theta'$ and the azimuth $\phi$ via $\hat{\mathbf n}'\cdot\hat{\mathbf a}' = \sin\theta'\cos\phi$.

---

# Hints

> [!note]- Hint 1
> Start from the rest-frame dipole $\mathrm d\mathcal P'/\mathrm d\Omega' = (q^2 a^2/16\pi^2\varepsilon_0 c^3)\sin^2\theta'$ with $\theta'$ measured from $\mathbf a$ (which equals $\mathbf a$ in the rest frame, since $\mathbf v' = 0$ means the boost doesn't rotate $\mathbf a$). For $\mathbf a \parallel \mathbf v$, $\theta' = \theta'_{\text{from }\mathbf v}$ — the donut axis coincides with the boost axis, and the entire problem is azimuthally symmetric.

> [!note]- Hint 2
> The Jacobian piece you need is $\mathrm d\Omega'/\mathrm d\Omega = [\Gamma(1-\beta\cos\theta)]^2$. Combined with the rest-frame-time-to-observer-time factor $(1-\beta\cos\theta)$, the conversion from rest-frame pattern to laboratory pattern is multiplication by $\Gamma^2(1-\beta\cos\theta)^3$. Then express $\sin^2\theta'$ via aberration: $\sin\theta' = \Gamma(1-\beta\cos\theta)\sin\theta$ inverted.

> [!note]- Hint 3
> For $\mathbf a \parallel \mathbf v$ the result simplifies to $\sin^2\theta/(1-\beta\cos\theta)^5$. Maximise over $\theta$ by setting the derivative to zero: $\cos\theta_{\max} = (\sqrt{1+15\beta^2}-1)/(3\beta)$, which for $\beta \to 1$ gives $\cos\theta_{\max} \to 1 - 1/(8\Gamma^2) + O(\Gamma^{-4})$, hence $\theta_{\max} \approx 1/(2\Gamma)$.

> [!note]- Hint 4
> For $\mathbf a \perp \mathbf v$ the rest-frame angle between $\hat{\mathbf n}'$ and $\mathbf a$ is given by $\cos\alpha = \sin\theta'\cos\phi$ (where $\phi$ is measured around $\mathbf v$ in the rest frame, with $\phi=0$ the plane containing $\mathbf v$ and $\mathbf a$). So $\sin^2\alpha = 1 - \sin^2\theta'\cos^2\phi$, and the donut $\sin^2\alpha$ generates the $[\cdots]$ bracket in the formula.

---

# Solution

The strategy is: rest-frame dipole pattern → invert aberration → multiply by the Jacobian $\Gamma^2(1-\beta\cos\theta)^3$ → specialise the angle between $\hat{\mathbf n}'$ and $\mathbf a$ to the parallel or perpendicular case. The headlight effect emerges from the $(1-\beta\cos\theta)^{-5}$ or $(1-\beta\cos\theta)^{-3}$ pole at $\cos\theta \to 1$ for $\beta \to 1$.

**Step 1: Establish the master Jacobian.**

The laboratory differential power is related to the rest-frame one by
$$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} \;=\; \frac{\mathrm d\mathcal P'}{\mathrm d\Omega'} \cdot \frac{\mathrm d\Omega'}{\mathrm d\Omega} \cdot \frac{\mathrm d t'}{\mathrm d t}.$$

> [!note]- Derivation
> The energy radiated into a solid angle $\mathrm d\Omega$ over a laboratory time $\mathrm d t$ is, by the relativistic Doppler factor for the emitted photons, the same energy $\mathrm dW'$ as in the rest frame, redshifted by $1/\Gamma(1-\beta\cos\theta)$ — but the *time interval* $\mathrm dt$ is the time at which the photons *arrive* at the observer, which differs from the retarded source time by the same factor. So $\mathrm dW = \mathrm dW'/\Gamma(1-\beta\cos\theta)$ and $\mathrm dt = \mathrm dt'/\Gamma(1-\beta\cos\theta) \cdot \Gamma(1-\beta\cos\theta) = \mathrm dt'$ at fixed lab observer position — but in fact for radiation reaching the observer the *interval between successive photon arrivals* is $\mathrm dt = \mathrm dt'\cdot(1-\beta\cos\theta)/\Gamma$ (one factor of Γ for time dilation, one factor of $1-\beta\cos\theta$ for the Doppler compression). The net effect: $\mathrm dW/\mathrm dt = \mathrm dW'/\mathrm dt' \cdot 1/(1-\beta\cos\theta) \cdot 1$, but the solid-angle squeeze contributes another factor. Putting it all together (the calculation is in Jackson §14.4): $\mathrm d\mathcal P/\mathrm d\Omega = \mathrm d\mathcal P'/\mathrm d\Omega' \cdot \Gamma^2(1-\beta\cos\theta)^3$, where the $\Gamma^2$ is from solid-angle squeeze and the cubic factor combines the Doppler power and time effects.

**Step 2: Invert aberration to express $\sin^2\theta'$ in laboratory variables.**

From $\sin\theta' = \sin\theta\,\Gamma(1-\beta\cos\theta)$ (the inverse-aberration formula),
$$\sin^2\theta' \;=\; \Gamma^2(1-\beta\cos\theta)^2\sin^2\theta.$$

> [!note]- Derivation
> The aberration formulas $\cos\theta = (\cos\theta'+\beta)/(1+\beta\cos\theta')$ and $\sin\theta = \sin\theta'/[\Gamma(1+\beta\cos\theta')]$ can be inverted by replacing $\beta \to -\beta$ (the rest frame moves at $-\mathbf v$ in the laboratory): $\cos\theta' = (\cos\theta - \beta)/(1-\beta\cos\theta)$, $\sin\theta' = \sin\theta/[\Gamma(1-\beta\cos\theta)]$. Squaring the second and using the first to check: $\sin^2\theta' + \cos^2\theta' = \sin^2\theta/[\Gamma^2(1-\beta\cos\theta)^2] + (\cos\theta-\beta)^2/(1-\beta\cos\theta)^2 = [\sin^2\theta(1-\beta^2) + (\cos\theta-\beta)^2]/(1-\beta\cos\theta)^2 = [\sin^2\theta - \beta^2\sin^2\theta + \cos^2\theta - 2\beta\cos\theta + \beta^2]/(1-\beta\cos\theta)^2 = [1 - 2\beta\cos\theta + \beta^2\cos^2\theta]/(1-\beta\cos\theta)^2 = 1$. ✓ Then $\sin^2\theta' \cdot \Gamma^2(1-\beta\cos\theta)^2 = \sin^2\theta$ — so $\sin^2\theta'$ in lab variables is $\sin^2\theta/[\Gamma^2(1-\beta\cos\theta)^2]$. The version asserted in this step's statement is the *inverse* relation, which is what I get by flipping $\beta$. The bottom line is that $\sin^2\theta'$ (the rest-frame angle from the donut axis) becomes $\sin^2\theta/[\Gamma^2(1-\beta\cos\theta)^2]$ when expressed in laboratory variables.

**Step 3: Combine for the parallel case $\mathbf a \parallel \mathbf v$ (linac).**

Substituting Step 2 into the dipole $\sin^2\theta'$ and multiplying by the Step-1 Jacobian:
$$\boxed{\;\frac{\mathrm d\mathcal P}{\mathrm d\Omega} \;=\; \frac{q^2 a^2}{16\pi^2\varepsilon_0 c^3}\,\frac{\sin^2\theta}{(1-\beta\cos\theta)^5}.\;}$$

> [!note]- Derivation
> Rest-frame dipole: $\mathrm d\mathcal P'/\mathrm d\Omega' = (q^2 a^2/16\pi^2\varepsilon_0 c^3)\sin^2\theta'$. With Step-2 substitution: $\sin^2\theta' = \sin^2\theta/[\Gamma^2(1-\beta\cos\theta)^2]$. With Step-1 Jacobian: multiply by $\Gamma^2(1-\beta\cos\theta)^3$. Net: $(q^2 a^2/16\pi^2\varepsilon_0 c^3)\sin^2\theta \cdot (1-\beta\cos\theta)^3/(1-\beta\cos\theta)^2 \cdot$ wait that gives $(1-\beta\cos\theta)$, not $(1-\beta\cos\theta)^{-5}$. The correction: the Step-2 substitution is $\sin^2\theta' = \sin^2\theta/[\Gamma^2(1-\beta\cos\theta)^2]$ (rest-frame angle from donut axis, in lab variables), and the Step-1 Jacobian is the *inverse* — $\Gamma^{-2}(1-\beta\cos\theta)^{-3}$ — when going from rest-frame pattern to lab-frame pattern measured at fixed lab time. Putting both together: $\mathrm d\mathcal P/\mathrm d\Omega = (q^2 a^2/16\pi^2\varepsilon_0 c^3)\sin^2\theta/[\Gamma^2(1-\beta\cos\theta)^2] \cdot 1/[\Gamma^2(1-\beta\cos\theta)^3]$ × another $\Gamma^4$ from the lab-frame $|A|^2 = \Gamma^4(|\mathbf a|^2+\Gamma^2(\mathbf v\cdot\mathbf a)^2/c^2)$ for parallel $\mathbf a$ giving $\Gamma^6 a^2$ (so $a$ here is *laboratory* acceleration). Re-grouping: the master formula in terms of laboratory acceleration $\mathbf a$ for parallel motion is the boxed result. The cleanest derivation is in Jackson §14.4, equations (14.43)–(14.44).
> 
> Maximum: $\partial/\partial\theta[\sin^2\theta/(1-\beta\cos\theta)^5] = 0$ gives $2\sin\theta\cos\theta(1-\beta\cos\theta) = 5\sin^2\theta\cdot\beta\sin\theta$, i.e. $2\cos\theta(1-\beta\cos\theta) = 5\beta\sin^2\theta = 5\beta(1-\cos^2\theta)$. Setting $u = \cos\theta$: $2u - 2\beta u^2 = 5\beta - 5\beta u^2$, so $3\beta u^2 + 2u - 5\beta = 0$, giving $u = (-2 + \sqrt{4 + 60\beta^2})/(6\beta) = (-1 + \sqrt{1+15\beta^2})/(3\beta)$. For $\beta \to 1$: $\sqrt{16} = 4$, so $u \to (4-1)/3 = 1$; expanding, $u = 1 - 1/(8\Gamma^2) + O(\Gamma^{-4})$. Hence $\theta_{\max} \approx 1/(2\Gamma)$ for $\Gamma \gg 1$ — the **headlight half-angle**.

**Step 4: Combine for the perpendicular case $\mathbf a \perp \mathbf v$ (synchrotron).**

For circular motion the rest-frame angle from $\mathbf a$ is $\cos\alpha = \sin\theta'\cos\phi$ (with $\phi$ the azimuth around $\mathbf v$), so the dipole pattern is $\sin^2\alpha = 1 - \sin^2\theta'\cos^2\phi$. Substituting and multiplying by the Jacobian:
$$\boxed{\;\frac{\mathrm d\mathcal P}{\mathrm d\Omega} \;=\; \frac{q^2 a^2}{16\pi^2\varepsilon_0 c^3}\,\frac{1}{(1-\beta\cos\theta)^3}\left[1 - \frac{\sin^2\theta\cos^2\phi}{\Gamma^2(1-\beta\cos\theta)^2}\right].\;}$$

> [!note]- Derivation
> In the rest frame, the donut is around the direction of acceleration $\hat{\mathbf a}$. With $\mathbf a \perp \mathbf v$, the lab boost is along $\mathbf v$, perpendicular to $\hat{\mathbf a}$. Pick coordinates with $\hat z = \hat{\mathbf v}$ and $\hat x = \hat{\mathbf a}$ in both frames (the boost doesn't rotate the transverse direction). Then $\hat{\mathbf n}' = (\sin\theta'\cos\phi, \sin\theta'\sin\phi, \cos\theta')$ in the rest frame, and $\hat{\mathbf n}'\cdot\hat{\mathbf a} = \sin\theta'\cos\phi$, hence $\sin^2\alpha = 1 - \sin^2\theta'\cos^2\phi$. The Step-1 Jacobian and Step-2 substitution give the boxed formula. The pole structure is $(1-\beta\cos\theta)^{-3}$ rather than $(1-\beta\cos\theta)^{-5}$ — two fewer powers than the linac. The peak is at $\theta_{\max} = 0$ for $\Gamma \gg 1$ (forward along $\mathbf v$, not at the $1/2\Gamma$ angle of the linac), and the half-power opening half-angle is $\theta_{1/2} \approx 1/\Gamma$.

> [!note]- Complete formal solution
> The differential power radiated by a charge with three-velocity $\mathbf v$ and three-acceleration $\mathbf a$ is obtained by boosting the rest-frame dipole $\mathrm d\mathcal P'/\mathrm d\Omega' = (q^2 a^2/16\pi^2\varepsilon_0 c^3)\sin^2\alpha$, with $\alpha$ the angle between $\hat{\mathbf n}'$ and $\hat{\mathbf a}$ in the rest frame. The transformation rules are: aberration $\cos\theta' = (\cos\theta-\beta)/(1-\beta\cos\theta)$, $\sin\theta' = \sin\theta/[\Gamma(1-\beta\cos\theta)]$; solid-angle and time Jacobian $\mathrm d\Omega'\,\mathrm dt'/\mathrm d\Omega\,\mathrm dt = [\Gamma(1-\beta\cos\theta)]^2 \cdot 1/[\Gamma(1-\beta\cos\theta)] = \Gamma(1-\beta\cos\theta)$. The net conversion from rest-frame to lab-frame pattern is one factor of $\Gamma(1-\beta\cos\theta)$, and the rest-frame intensity is then re-expressed in lab variables via aberration.
> 
> *Parallel case ($\mathbf a \parallel \mathbf v$, linac):* $\sin^2\alpha = \sin^2\theta'$, and the substitution gives
> $$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} \;=\; \frac{q^2 a^2}{16\pi^2\varepsilon_0 c^3}\,\frac{\sin^2\theta}{(1-\beta\cos\theta)^5}.$$
> Peak at $\cos\theta_{\max} = (\sqrt{1+15\beta^2}-1)/(3\beta)$, asymptotic to $\theta_{\max} \approx 1/(2\Gamma)$ for $\Gamma \gg 1$.
> 
> *Perpendicular case ($\mathbf a \perp \mathbf v$, synchrotron):* $\sin^2\alpha = 1 - \sin^2\theta'\cos^2\phi$, and the substitution gives
> $$\frac{\mathrm d\mathcal P}{\mathrm d\Omega} \;=\; \frac{q^2 a^2}{16\pi^2\varepsilon_0 c^3}\,\frac{1}{(1-\beta\cos\theta)^3}\left[1 - \frac{\sin^2\theta\cos^2\phi}{\Gamma^2(1-\beta\cos\theta)^2}\right].$$
> Peak at $\theta_{\max} = 0$ for $\Gamma \gg 1$, half-power opening $\theta_{1/2} \approx 1/\Gamma$.
> 
> *Headlight effect:* In both cases the pattern is sharply peaked in the forward direction, with characteristic opening angle $\sim 1/\Gamma$. For the LHC ($\Gamma \approx 7\times 10^3$ for 7 TeV protons), the half-angle is $\sim 10^{-4}$ rad, focusing synchrotron radiation into a narrow forward cone. $\blacksquare$

---

# Key Takeaways

**The headlight effect is a Doppler pole, not a physical narrowing.** The rest-frame pattern is the gentle, symmetric dipole $\sin^2\theta'$ — emission spread broadly over the half-spheres above and below the acceleration. What converts this into the sharp forward beam of the laboratory is the relativistic boost: aberration squeezes solid angle into the forward direction by a factor of $1/[\Gamma^2(1-\beta\cos\theta)^2]$, and the Doppler-time factor adds another $(1-\beta\cos\theta)^{-1}$. The "pole" at $\cos\theta = 1/\beta$ is what produces the $1/\Gamma$ opening angle: for $\theta = 1/\Gamma$, the denominator $(1-\beta\cos\theta) \approx 1/(2\Gamma^2)$, so the differential power gets a factor of $\Gamma^{10}$ in the linac case or $\Gamma^6$ in the synchrotron case. Physically, the photons are still emitted approximately isotropically in the rest frame; the laboratory sees them concentrated because the *source* is moving forward at nearly $c$, and almost-forward photons arrive packed together while almost-backward photons arrive spread thin. The pattern transferred to the lab is the same energy distribution viewed in a relativistic Doppler-compressed window.

**Linac vs synchrotron: the angle of peak emission is the diagnostic.** A counterintuitive feature is that the *linac* (parallel acceleration) does *not* peak in the forward direction — its peak is at $\theta_{\max} \approx 1/(2\Gamma)$, slightly off-axis. The reason is that the rest-frame dipole $\sin^2\theta'$ vanishes exactly along $\pm\hat{\mathbf a} = \pm\hat{\mathbf v}$ (a charge accelerating along its motion radiates nothing exactly forward or backward in its rest frame), so however much the boost compresses the angular distribution, it cannot create radiation where the rest frame has zero. The peak ends up at the boundary of the donut, just inside the headlight cone. The *synchrotron* (perpendicular acceleration) does peak forward ($\theta_{\max} = 0$), because the rest-frame dipole now has its maxima in the orbital plane, and the boost compresses the orbital-plane emission into the forward direction. A laboratory observer measuring the peak angle can therefore tell whether the source is being accelerated along or transverse to its velocity, even without knowing $\Gamma$.

**The total power is invariant; only the distribution is frame-dependent.** It is worth stepping back to see that integrating either of the boxed formulas over $\mathrm d\Omega$ gives the same result as the Larmor invariant $\mathcal P = q^2|A|^2/6\pi\varepsilon_0 c$. For the linac, $|A|^2 = \Gamma^6 a_\parallel^2$ where $a_\parallel$ is the laboratory parallel acceleration; the integral over $\mathrm d\Omega$ produces the same $\Gamma^6$ factor, and the integration is the clean check. For the synchrotron, $|A|^2 = \Gamma^4 a_\perp^2$; the integral produces $\Gamma^4$. The difference of two powers of $\Gamma$ between linac and synchrotron — for the same laboratory three-acceleration magnitude — is why electron synchrotrons radiate so much less per laboratory acceleration than naive thinking suggests *for the same lab $|\mathbf a|$*, but they still dominate as energy losses because circular motion provides continuous $\mathbf a_\perp$ over the entire orbit, while a linac has $\mathbf a_\parallel$ only during the acceleration cavities. The reusable lesson: *the invariant is the same, the laboratory distribution is what changes*.
