---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Thm - Invariance of the Velocity of Light"
  - "Def - Photon Propagation Direction and Velocity"
tags: [physics, special-relativity]
---

# Problem Statement

In 1810, François Arago measured the deflection of starlight by a prism placed in front of a telescope, for stars in different directions relative to the Earth's motion around the Sun. The deflection angle through a prism depends, by Snell's law $n_1\sin\theta_1 = n_2\sin\theta_2$, on the refractive index, and the refractive index is inversely proportional to the speed of light in the medium. Working with $c$ restored:

1. **Corpuscular (Galilean) prediction.** Assume light from a star travels at $c_\odot \approx c$ relative to an inertial frame centred on the Sun, and that velocities compose by the Galilean rule. For a star in the direction of the Earth's motion, the light's speed relative to the Earth is $c_\odot - V_\oplus$; in the opposite direction, $c_\odot + V_\oplus$, where $V_\oplus \approx 30\,\mathrm{km\,s^{-1}}$ is the Earth's orbital speed. Show this predicts a *seasonal and directional* variation in the prism's deflection angle.
2. Given that Arago's prism, with $V_\oplus = 30\,\mathrm{km\,s^{-1}}$, should have shown a deflection difference of amplitude about $28''$ (arcseconds) between opposite directions, and that Arago measured all deflections equal to within $\pm 5''$, state his conclusion.
3. **Relativistic explanation.** Using [[Thm - Invariance of the Velocity of Light|the invariance of the velocity of light]], explain why the speed of starlight relative to the Earth is $c$ regardless of the star's direction or the Earth's motion, so the prism's deflection is the same for all stars — exactly Arago's null result.
4. Remark on the historical significance: Arago's experiment (1810) predates Michelson–Morley (1887) by 77 years and special relativity (1905) by 95 years. What relativistic effect did it unknowingly detect first, and why was it not recognised as such at the time?

**Recall:**

The exercise rests on the invariance of light.

![[Thm - Invariance of the Velocity of Light#Statement]]

[[Def - Photon Propagation Direction and Velocity|The speed of starlight relative to the Earth]] is $\|\mathbf V_{\mathrm{light}}\| = c$ — the propagation direction $N$ is a unit vector for any observer, so the speed is $c$ independent of the star's direction or the Earth's velocity. The Galilean (corpuscular) alternative would give $c_\odot \pm V_\oplus$, a direction-dependent speed that the prism's refractive index would register.

---

# Convergent Strategy

**Problem class.** A *predict-and-confront-an-experiment* problem of the chapter's [[Special Relativity VII — Kinematics I, Motion Relative to an Observer#Problem-Solving Strategy|fourth strategy]], the historically *first* such relativistic null result: compute the corpuscular-model prediction and confront it with Arago's null measurement, which the invariance of light explains.

**Assumption pattern.** Starlight observed from a moving Earth through a refracting prism — the signal that a *direction-dependent* speed of light (corpuscular model) would change the refractive index and hence the deflection angle, while an invariant speed would not. The prism is the detector: it converts a speed-of-light difference into a measurable deflection-angle difference via Snell's law.

**Theorem routing.** Part 1 computes the Galilean (corpuscular) prediction: $c_\odot \pm V_\oplus$ gives a direction- and season-dependent refractive index, hence deflection. Part 2 states Arago's null result ($28''$ predicted, equal within $5''$). Part 3 invokes [[Thm - Invariance of the Velocity of Light]]: $\|\mathbf V_{\mathrm{light}}\| = c$ for the Earth observer independent of direction or motion, so the deflection is uniform — Arago's result. Part 4 places the experiment historically as the first detection of the constancy of light, decades before the concept existed.

**Key decision point.** The crux is recognising that the prism's deflection angle is a *probe of the speed of light*: through Snell's law and the index–speed relation, any direction-dependence of the speed would show up as a direction-dependence of the deflection. The natural error is to think the experiment is about aberration or refraction generally; in fact it isolates the speed of light's directional dependence, which is precisely what relativity forbids and Arago found absent.

---

# Legal Operations Used

1. **Adapt the velocity of light to the observer** (operation 8 from the topic page). The Earth observer measures the speed of starlight; the corpuscular model predicts $c_\odot \pm V_\oplus$, relativity gives $c$.

2. **Specialise to the simplest case** (operation 7). The relativistic prediction is immediate: $\|\mathbf V_{\mathrm{light}}\| = c$ for the Earth observer (local measurement), so the refractive index and deflection are direction-independent.

3. **Confront a test-theory prediction with a null result** (the chapter's experimental-routing pattern). The corpuscular model with composition parameter (Galilean $c_\odot \pm V_\oplus$) predicts a $28''$ deflection variation; the null result bounds it.

---

# Hints

> [!note]- Hint 1
> Galilean composition: a star ahead of the Earth's motion sends light at $c_\odot - V_\oplus$ relative to the Earth; a star behind, at $c_\odot + V_\oplus$. The refractive index $n \propto 1/V_{\mathrm{light}}$, so a faster beam refracts less. Different stars (different directions relative to $V_\oplus$) would refract by different amounts, and the same star would refract differently in different seasons as $V_\oplus$ rotates.

> [!note]- Hint 2
> The predicted amplitude is $28''$, far larger than the $\pm5''$ scatter Arago measured. He found *all* deflections equal within his precision, with no correlation to the star's direction relative to the Earth's motion. Conclusion: the speed of light relative to the Earth is the same for all stars, independent of the Earth's motion relative to them.

> [!note]- Hint 3
> Relativity: $\|\mathbf V_{\mathrm{light}}\| = c$ for the Earth observer, whatever the star's direction or the Earth's velocity (the propagation direction is always a unit vector). So the refractive index is the same for every star, the deflection is uniform, and Arago's null result is exactly what relativity predicts — no $28''$ variation, no seasonal change.

> [!note]- Hint 4
> Arago detected the constancy of the speed of light in 1810 — but the *concept* of an invariant speed of light did not exist until 1905, so he could not interpret it. He explained the null result with ad hoc hypotheses about which "light corpuscles" the eye is sensitive to. Fresnel later patched it with partial aether dragging. The true explanation — the constancy of $c$ — was a century away.

---

# Solution

The route is to compute the corpuscular prediction (a direction- and season-dependent deflection), state Arago's null measurement, explain it relativistically via the invariance of light, and place it historically. Step 1 gives the Galilean prediction; Step 2 the null result; Step 3 the relativistic explanation; Step 4 the historical significance. The non-obvious thread is that a refracting prism is a speed-of-light detector, and Arago's null result is the constancy of light measured 95 years before it was understood.

**Step 1: The corpuscular model predicts a direction- and season-dependent deflection.**

> [!note]- Derivation
> In the corpuscular (Newtonian) picture, light is a stream of particles travelling at $c_\odot \approx c$ relative to an inertial frame centred on the Sun, and velocities compose by the Galilean rule. For a star in the direction of the Earth's orbital motion, the Earth moves *toward* the incoming light, so the light's speed *relative to the Earth* is, by Galilean composition,
> $$V_{\mathrm{light}} = c_\odot - V_\oplus\quad(\text{star ahead}),\qquad V_{\mathrm{light}} = c_\odot + V_\oplus\quad(\text{star behind}),$$
> with $V_\oplus \approx 30\,\mathrm{km\,s^{-1}}$ the Earth's orbital speed. Now a refracting prism's deflection depends on its refractive index $n$, which is inversely proportional to the speed of light *in the medium*, and the speed in the medium tracks the incident speed: a faster incident beam yields a smaller effective index and a smaller deflection (and conversely). So the deflection angle would depend on $V_{\mathrm{light}}$, hence on the star's direction relative to the Earth's motion: stars ahead (slower light, larger index, more deflection) and stars behind (faster light, less deflection) would refract by *different* amounts. Moreover, for a *fixed* star, the Earth's orbital velocity rotates over the year, so the relative speed $V_{\mathrm{light}}$ — and the deflection — would vary *seasonally*. The corpuscular model thus predicts a definite directional and seasonal variation in the prism deflection.

**Step 2: Arago found all deflections equal within $\pm5''$, against a predicted $28''$ variation.**

> [!note]- Derivation
> Given the refractive index of his prism and $V_\oplus = 30\,\mathrm{km\,s^{-1}}$, the corpuscular model predicts a deflection-angle difference of amplitude about $28''$ (arcseconds) between stars in opposite directions relative to the Earth's motion — a large, readily measurable effect for a careful astronomer. Arago measured the deflections for stars in many directions, with two different prisms, and at two epochs of the year (March and October) to sample different orbital phases. He found:
> $$\text{all deflections equal to within } \pm 5'',$$
> with the small residual scatter *uncorrelated* with the star's direction relative to the Earth's motion. The predicted $28''$ directional variation was absent. Arago's conclusion: the speed of light relative to the Earth is *constant* — the same for all stars, depending neither on the source star nor on the motion of the Earth relative to that star. This is a null result, falsifying the Galilean composition of the speed of light.

**Step 3: Relativity predicts uniform deflection, because $\|\mathbf V_{\mathrm{light}}\| = c$ for every star.**

> [!note]- Derivation
> By [[Thm - Invariance of the Velocity of Light|the invariance of the velocity of light]], the Earth-bound observer measures the speed of incoming starlight to be exactly $c$ at the observation point, *independent of the star's direction and of the Earth's velocity*. In the language of the chapter, the [[Def - Photon Propagation Direction and Velocity|propagation direction]] $N$ is a unit vector for any observer's four-velocity, so $\|\mathbf V_{\mathrm{light}}\| = c|\mathbf N| = c$ for every star, every direction, every season (the measurement at the telescope is local, $\overrightarrow{OM} = 0$, so the qualification on the theorem is met). Therefore the refractive index of the prism — which depends on the incident speed — is the *same* for all stars, and the deflection angle is *uniform*: no $28''$ directional variation, no seasonal change. Relativity predicts exactly Arago's null result. The Galilean $c_\odot \pm V_\oplus$ is simply wrong; the speed of light does not compose with the Earth's velocity, because it is the same in every frame.

**Step 4: Arago detected the constancy of light in 1810, but could not have understood it.**

> [!note]- Derivation
> Arago's experiment, in 1810, *unknowingly detected the constancy of the speed of light* — the very fact that Einstein would elevate to a postulate in 1905. It predates the Michelson–Morley experiment (1887) by 77 years and special relativity by 95 years. It is, as Gourgoulhon remarks, "the very first evidence of a relativistic effect, almost a century before the formulation of special relativity."
>
> Why was it not recognised? Because the *concept* of an invariant speed of light did not exist and seemed absurd: every other speed composes by the Galilean rule, and there was no framework in which a speed could be the same in all frames. Arago himself, then a proponent of the corpuscular theory, "explained" the null result with ad hoc hypotheses — that a star emits corpuscles with a range of velocities, and that the eye is sensitive only to those arriving at one particular speed, so the deflection always corresponds to that speed. When he later adopted the wave theory, the null result became a puzzle for *that* theory too (light should travel at $c$ relative to the aether, so the moving Earth should see $c \pm V_\oplus$), and Fresnel patched it with the hypothesis of *partial aether dragging*: transparent media partly drag the aether along, by an amount tuned to cancel the effect. Each "explanation" was a contrivance to preserve Galilean composition; the true explanation — that the speed of light is simply the same in every frame — was unthinkable until the geometry of spacetime made it natural. Arago's result is the historical lesson that a decisive experiment can sit unexplained for a century if the conceptual framework to interpret it is missing.

> [!note]- Complete formal solution
> In the corpuscular model with Galilean composition, starlight reaches the Earth at $c_\odot \mp V_\oplus$ depending on whether the star is ahead of or behind the Earth's orbital motion ($V_\oplus = 30\,\mathrm{km\,s^{-1}}$); since a prism's refractive index varies inversely with the incident speed, the deflection angle would vary with the star's direction and with the season — by a predicted amplitude of $\sim 28''$. Arago (1810) measured all deflections equal within $\pm5''$, uncorrelated with direction, concluding the speed of light relative to the Earth is constant. By [[Thm - Invariance of the Velocity of Light|the invariance of the velocity of light]], $\|\mathbf V_{\mathrm{light}}\| = c$ for the Earth observer independent of the star's direction or the Earth's motion (the propagation direction is always a unit vector), so the prism deflects every star equally — exactly Arago's null result. Historically, Arago thereby detected the constancy of $c$ in 1810, 95 years before special relativity, but could not interpret it: lacking the concept of an invariant speed, he and Fresnel preserved Galilean composition with ad hoc hypotheses (velocity-selective vision, partial aether dragging) until the geometry of spacetime made the constancy of light natural. $\blacksquare$

---

# Key Takeaways

**A refracting prism is a speed-of-light detector, and Arago's null result is the constancy of $c$ measured through Snell's law.** The cleverness of the experiment is indirect: it does not time a light beam, it *refracts* one, and because the refractive index depends on the speed of light in the medium, any direction-dependence of the incident speed shows up as a direction-dependence of the deflection angle. So the prism converts the abstract question "does the speed of light depend on the Earth's motion?" into the concrete, measurable question "does the deflection angle depend on the star's direction?". The reusable insight is that many properties of light (refraction, dispersion, interference) depend on its speed, so a wide variety of optical experiments can serve as speed-of-light probes — and a *null* result in any of them (no variation with the observer's motion) is a confirmation of the constancy of light. The trigger to recognise this pattern: whenever an optical measurement could in principle depend on the speed of light, and the apparatus moves, the experiment tests the invariance of $c$, and a null result bounds the deviation.

**A decisive experiment can predate the concept that explains it by a century — the framework, not the data, was missing.** Arago's 1810 null result is the constancy of the speed of light, detected 95 years before Einstein, 77 years before Michelson–Morley. The data were correct and the effect was real, yet it could not be *understood*, because the conceptual framework — an invariant speed, the relativity of simultaneity, the geometry of spacetime — did not exist and seemed impossible. Arago and Fresnel preserved Galilean composition with increasingly contrived hypotheses (velocity-selective vision, partial aether dragging), each one a patch to avoid the unthinkable conclusion. The historical lesson, which recurs throughout physics, is that an anomaly can sit in plain sight for generations when the only available interpretations are forced and ad hoc; the breakthrough is often not new data but a new framework that makes the old data natural. Special relativity did not discover the constancy of light — Arago had measured it — but it provided the geometry in which the constancy is a *theorem* rather than a paradox, retroactively explaining a century of null results (Arago, Fizeau, Michelson–Morley) at a stroke.

**The progression Arago → Michelson–Morley → Kennedy–Thorndike is the experimental tightening of one fact: the speed of light does not depend on the observer's motion.** The three experiments form a sequence of increasing precision and specificity, all confirming the same underlying invariance. Arago (1810) detected the gross constancy — the speed of starlight does not depend on the Earth's motion relative to the source, to $\sim 5''$ in a prism deflection. Michelson–Morley (1887) sharpened this to the *directional* dependence (isotropy), to a fraction of a fringe. Kennedy–Thorndike (1932) added the *magnitude* dependence, over seasons. Modern optical-cavity experiments push the bounds to $10^{-17}$. Each experiment confronts a test theory — the corpuscular model, the aether model — with a null result, and bounds the deviation from $\|\mathbf V_{\mathrm{light}}\| = c$ ever more tightly. The reusable principle is that the confirmation of a fundamental invariance is never a single experiment but a *programme* of null results across different regimes and parameters, each closing a loophole the previous left open, and the cumulative weight is what establishes the invariance beyond doubt. The companion modern experiments are [[Ex - Michelson-Morley null result]] (direction) and [[Ex - Kennedy-Thorndike and the speed independent of observer speed]] (magnitude).
