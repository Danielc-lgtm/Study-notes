---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Aberration of Light"
  - "Thm - The Doppler Effect"
  - "Def - Apparent Rotation and Images of Moving Objects"
tags: [physics, special-relativity]
---

# Problem Statement

A source emits photons *isotropically* in its own rest frame. Viewed from a frame in which the source moves at speed $V$ (Lorentz factor $\Gamma$), the emission is beamed forward — the **relativistic headlight effect**. Working with $c = 1$:

1. Let $\theta_0$ be the emission angle of a photon in the source rest frame (measured from the direction of motion) and $\theta$ the angle in the lab frame. Write the aberration relation $\cos\theta = (\cos\theta_0 + V)/(1 + V\cos\theta_0)$ connecting them.
2. The source emits isotropically, so the fraction of photons in $[\theta_0, \theta_0 + \mathrm{d}\theta_0]$ is $\tfrac12\sin\theta_0\,\mathrm{d}\theta_0$. Show that the photon emitted at $\theta_0 = \pi/2$ (sideways in the rest frame) appears in the lab at $\cos\theta = V$, so that **half** the photons are beamed into the forward cone of half-angle $\theta_{1/2} = \arccos V$.
3. Show that for $\Gamma \gg 1$ this half-angle is $\theta_{1/2} \approx 1/\Gamma$, so almost all the light is concentrated in a forward cone of opening $\sim 1/\Gamma$.
4. Combine with the Doppler effect to find how the lab-frame *intensity* (power per solid angle) in the forward direction scales with $\Gamma$, and explain the relativistic beaming of astrophysical sources.

**Recall:**

The exercise combines aberration and Doppler to compute the beamed appearance of an isotropic source.

![[Thm - Aberration of Light#Statement]]

The [[Thm - Aberration of Light|aberration]] law sweeps every emission direction toward the forward direction of motion: $\theta \le \theta_0$ when the source moves forward. The half-angle $\theta_{1/2} = \arccos V$ is where the rest-frame *equatorial* photons ($\theta_0 = \pi/2$) land. The [[Thm - The Doppler Effect|Doppler factor]] $\mathcal{D} = 1/[\Gamma(1 - V\cos\theta)]$ additionally blueshifts and boosts the forward photons. The [[Def - Apparent Rotation and Images of Moving Objects|beaming]] is the global appearance of the forward-concentrated, blueshifted source.

---

# Convergent Strategy

**Problem class.** A *global appearance* problem combining the [[Thm - Aberration of Light|aberration]] map (where photons go) with the [[Thm - The Doppler Effect|Doppler]] factor (how bright they are). The [[Special Relativity VIII — Kinematics II, Change of Observer#Problem-Solving Strategy|topic strategy]] for light problems is to apply aberration to directions and Doppler to intensities, together.

**Assumption pattern.** Rest-frame isotropy is the key input: it fixes the angular distribution of emission ($\tfrac12\sin\theta_0\,\mathrm{d}\theta_0$), so the lab distribution is obtained purely by transforming angles. The high-$\Gamma$ limit is the regime where the beaming is dramatic and the simple $\sim 1/\Gamma$ scaling emerges.

**Theorem routing.** The aberration formula maps the rest-frame median direction $\theta_0 = \pi/2$ to the lab half-angle $\arccos V$, routing "half the photons go forward of $\theta_0 = \pi/2$" to "half land within $\theta_{1/2} = \arccos V$". The small-angle expansion routes $\arccos V$ to $1/\Gamma$. The Doppler factor routes the forward intensity to its $\Gamma$-scaling.

**Key decision point.** The crux is using the rest-frame *median* photon (the one at $\theta_0 = \pi/2$, with exactly half the photons ahead of it) and tracking where aberration sends it — this gives the half-light cone directly, without integrating. The natural but laborious alternative is to integrate the full transformed distribution; the median-photon shortcut gives the headline result ($\theta_{1/2} = \arccos V \approx 1/\Gamma$) in one line. For the intensity, the decision is to count *both* the angular compression (aberration) and the energy/rate boost (Doppler), since both contribute powers of $\Gamma$.

---

# Legal Operations Used

1. **Specialise to light via aberration** (operation 5 from the topic page), mapping rest-frame emission angles to lab angles.

2. **Build the global image from the per-ray map** (operation 7 from the topic page), here assembling the lab-frame angular distribution from the rest-frame isotropic one.

3. **Combine aberration with the Doppler factor** (operations 5 and from [[Thm - The Doppler Effect]]), to get the intensity, not just the direction.

4. **Take the high-$\Gamma$ limit** (operation 9 from the topic page, in the ultrarelativistic rather than Galilean direction), to extract the $\sim 1/\Gamma$ cone and the intensity scaling.

---

# Hints

> [!note]- Hint 1
> The source moves forward at $V$. A photon emitted at angle $\theta_0$ in the rest frame appears at $\theta$ in the lab via aberration: $\cos\theta = (\cos\theta_0 + V)/(1 + V\cos\theta_0)$.

> [!note]- Hint 2
> The "median" photon is the one at $\theta_0 = \pi/2$: in the isotropic rest frame, exactly half the photons are emitted into the forward hemisphere $\theta_0 < \pi/2$. Aberration sends $\theta_0 = \pi/2$ to $\cos\theta = (0 + V)/(1+0) = V$, i.e. $\theta_{1/2} = \arccos V$. So half the photons land within the forward cone of half-angle $\arccos V$.

> [!note]- Hint 3
> For $\Gamma \gg 1$, $V = \sqrt{1 - 1/\Gamma^2} \approx 1 - 1/(2\Gamma^2)$, so $\cos\theta_{1/2} = V \approx 1 - 1/(2\Gamma^2)$. For small $\theta_{1/2}$, $\cos\theta_{1/2} \approx 1 - \theta_{1/2}^2/2$, so $\theta_{1/2}^2/2 \approx 1/(2\Gamma^2)$, giving $\theta_{1/2} \approx 1/\Gamma$.

> [!note]- Hint 4
> Two boosts of the forward intensity: (i) aberration compresses solid angle by $\sim\Gamma^2$ (the forward cone shrinks from $2\pi$ steradians to $\sim\pi/\Gamma^2$); (ii) the Doppler factor blueshifts each photon's energy by $\mathcal{D} \sim \Gamma$ forward, and boosts the arrival rate by another $\mathcal{D}$. The forward specific intensity scales as a high power of $\Gamma$ (the exact power depends on whether one counts photon number, energy, or per-frequency intensity — typically $\mathcal{D}^{3+\alpha}$ for a power-law spectrum of index $\alpha$).

---

# Solution

The headlight effect is aberration concentrating an isotropic source's light into a forward cone, with Doppler boosting its brightness. Step 1 writes the aberration relation; Step 2 tracks the median photon to get the half-light cone $\arccos V$; Step 3 reduces it to $1/\Gamma$ at high $\Gamma$; Step 4 adds the Doppler intensity boost and explains astrophysical beaming. The non-obvious move is the median-photon shortcut, which gives the cone angle without integration.

**Step 1: The aberration relation.**

> [!note]- Derivation
> Let the source move forward at speed $V$. A photon emitted at angle $\theta_0$ to the motion in the *source rest frame* appears at lab angle $\theta$, related by the [[Thm - Aberration of Light|aberration]] formula (with the source moving, so the forward direction gains):
> $$\cos\theta = \frac{\cos\theta_0 + V}{1 + V\cos\theta_0}.$$
> Since the formula sweeps every $\theta_0$ toward smaller $\theta$, all photons are tilted toward the forward direction.

**Step 2: Half the light in the cone $\arccos V$.**

> [!note]- Derivation
> In the isotropic rest frame, the photons are distributed uniformly over solid angle, so the fraction emitted into $[\theta_0, \theta_0 + \mathrm{d}\theta_0]$ is $\tfrac12\sin\theta_0\,\mathrm{d}\theta_0$, and exactly *half* are emitted into the forward hemisphere $\theta_0 \in [0, \pi/2)$ (the other half into the backward hemisphere). The dividing photon is the one at $\theta_0 = \pi/2$ — the rest-frame "equator". Aberration sends it to
> $$\cos\theta_{1/2} = \frac{\cos(\pi/2) + V}{1 + V\cos(\pi/2)} = \frac{0 + V}{1 + 0} = V,$$
> so $\theta_{1/2} = \arccos V$. Because aberration is monotonic ($\theta$ increases with $\theta_0$), all the forward-hemisphere photons ($\theta_0 < \pi/2$) land at $\theta < \theta_{1/2}$. Therefore **half the photons are beamed into the forward cone of half-angle $\theta_{1/2} = \arccos V$**.

**Step 3: The cone is $\sim 1/\Gamma$ at high $\Gamma$.**

> [!note]- Derivation
> For an ultrarelativistic source, $\Gamma \gg 1$, so $V = \sqrt{1 - 1/\Gamma^2} \approx 1 - \tfrac{1}{2\Gamma^2}$. Then
> $$\cos\theta_{1/2} = V \approx 1 - \frac{1}{2\Gamma^2}.$$
> For a small angle, $\cos\theta_{1/2} \approx 1 - \tfrac12\theta_{1/2}^2$, so $\tfrac12\theta_{1/2}^2 \approx \tfrac{1}{2\Gamma^2}$, giving
> $$\boxed{\theta_{1/2} \approx \frac{1}{\Gamma}.}$$
> Half the source's light is concentrated into a forward cone of half-angle $\sim 1/\Gamma$ — a tiny cone for large $\Gamma$. A source with $\Gamma = 10$ beams half its photons into a cone of half-angle $\sim 6^\circ$; with $\Gamma = 100$, into $\sim 0.6^\circ$. This is why a relativistic emitter appears as a bright forward "headlight".

**Step 4: The Doppler intensity boost and astrophysical beaming.**

> [!note]- Derivation
> Aberration concentrates the light; the [[Thm - The Doppler Effect|Doppler]] effect further brightens the forward beam. Three compounding factors boost the forward specific intensity:
> - *Solid-angle compression (aberration).* The forward hemisphere's $2\pi$ steradians are squeezed into $\sim\pi\theta_{1/2}^2 \sim \pi/\Gamma^2$ steradians, a compression of $\sim\Gamma^2$, raising the photon number per solid angle by $\sim\Gamma^2$.
> - *Energy boost (Doppler blueshift).* Each forward photon's energy is multiplied by the Doppler factor $\mathcal{D} = 1/[\Gamma(1 - V\cos\theta)]$, which forward ($\theta \to 0$) is $\mathcal{D} \approx 1/[\Gamma(1-V)] \approx 2\Gamma$ — a blueshift by $\sim\Gamma$.
> - *Arrival-rate boost (Doppler).* The rate at which photons arrive is boosted by another factor of $\mathcal{D} \sim\Gamma$ (time compression).
>
> Combining, the forward specific intensity is boosted by a high power of the Doppler factor. For a source with a power-law spectrum $I_\nu \propto \nu^{-\alpha}$, the standard result is that the observed intensity scales as $\mathcal{D}^{3+\alpha}$ (the "$\delta^3$" of relativistic beaming, with one power from arrival rate, one from energy, one from solid-angle aberration, plus the spectral $\alpha$). Forward, $\mathcal{D} \sim 2\Gamma$, so the brightening is $\sim\Gamma^{3+\alpha}$.
>
> *Astrophysical consequence.* In a two-sided jet (such as M87 or a microquasar), the approaching jet has large forward $\mathcal{D}$ and is brightened by $\mathcal{D}^{3+\alpha}$, while the receding jet has small $\mathcal{D}$ and is *dimmed* by the reciprocal. The brightness ratio between approaching and receding jets can be enormous (factors of $10^3$–$10^6$ for $\Gamma \sim 10$), which is why one typically observes only *one* jet — the counter-jet is beamed away and Doppler-dimmed below detection. This relativistic beaming, the combination of the aberration cone and the Doppler boost computed here, is the dominant factor shaping the appearance of relativistic astrophysical sources; its radiative content is developed in [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

> [!note]- Complete formal solution
> A source moving forward at $V$ aberrates a rest-frame emission angle $\theta_0$ to $\cos\theta = (\cos\theta_0 + V)/(1 + V\cos\theta_0)$. For an isotropic source, half the photons are emitted into $\theta_0 < \pi/2$; the dividing photon at $\theta_0 = \pi/2$ maps to $\cos\theta_{1/2} = V$, so half the light lands in the forward cone of half-angle $\theta_{1/2} = \arccos V$. For $\Gamma \gg 1$, $V \approx 1 - 1/(2\Gamma^2)$ gives $\theta_{1/2} \approx 1/\Gamma$. The forward intensity is boosted by aberration's solid-angle compression ($\sim\Gamma^2$) and the Doppler factor's energy and rate boosts ($\sim\Gamma$ each), giving $\sim\mathcal{D}^{3+\alpha} \sim \Gamma^{3+\alpha}$ for a power-law spectrum; the approaching jet of a two-sided source is brightened and the receding one dimmed, explaining the one-sided appearance of relativistic jets. $\blacksquare$

---

# Key Takeaways

**The median-photon trick gives the beaming cone without integration.** Rather than integrate the transformed angular distribution, one tracks the single rest-frame photon that has exactly half the emission ahead of it — the $\theta_0 = \pi/2$ "equatorial" photon — and asks where aberration sends it. Because aberration is monotonic, "half the photons are forward of $\theta_0 = \pi/2$" maps directly to "half the photons are within $\theta_{1/2} = \arccos V$", giving the half-light cone in one line. The reusable principle: when a transformation is monotonic, the image of a *quantile* (median, quartile) of the input distribution is the same quantile of the output distribution, so you can read off cumulative properties of the transformed distribution from a single representative ray. This shortcut works for any monotone reparametrisation and turns a beaming-angle calculation that looks like it needs an integral into a one-step substitution. The same idea computes, e.g., the angle containing $90\%$ of the light (track the $\theta_0$ with $90\%$ ahead).

**Beaming has two compounding causes — aberration concentrates direction, Doppler boosts energy and rate — and both must be counted.** The dramatic forward brightening of a relativistic source is not a single effect but a product: aberration squeezes the solid angle (factor $\sim\Gamma^2$), the Doppler blueshift raises each photon's energy (factor $\sim\Gamma$ forward), and the Doppler time-compression raises the arrival rate (another factor $\sim\Gamma$). A calculation that includes only the aberration cone underestimates the brightness by the large Doppler powers; one that includes only Doppler misses the angular concentration. The trigger to remember: any "how bright does a relativistic source appear" question requires *both* the aberration map and the Doppler factor, combining into the beaming factor $\mathcal{D}^{3+\alpha}$. Forgetting either is a common and serious error in estimating the luminosity of jets, pulsar beams, and synchrotron sources. The deeper unity is that aberration and Doppler are two components of one object — the action of the boost on the photon's null tangent — so they always travel together.

**Relativistic beaming is why we see one jet, not two — appearance is dominated by the boost, not the intrinsic symmetry.** A physically symmetric two-sided jet appears wildly asymmetric because the approaching side is beamed toward us (brightened by $\mathcal{D}^{3+\alpha}$) and the receding side beamed away (dimmed by the reciprocal), with a brightness ratio reaching $10^3$–$10^6$. The general and transferable lesson is that for relativistic sources the *observed* morphology can differ qualitatively from the *intrinsic* morphology — what you see is the intrinsic source convolved with the beaming pattern, and the beaming can hide an entire symmetric counterpart. This forces a discipline when interpreting relativistic sources: never read the intrinsic structure directly off the image; always ask what the beaming and Doppler boost have done to it. The same caution applies to the [[Def - Apparent Rotation and Images of Moving Objects|apparent superluminal motion and image distortion]] of these sources — the appearance is a boosted, light-travel-time-distorted projection, and recovering the intrinsic physics requires inverting those effects.
