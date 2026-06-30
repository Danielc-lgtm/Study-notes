---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Conservation of Four-Momentum"
  - "Def - The Four-Momentum of a Photon"
  - "Def - Four-Force"
tags: [physics, special-relativity]
---

# Problem Statement

A **photon rocket** propels itself by converting part of its rest mass into radiation and emitting it straight backward. Let the rocket start at rest with rest mass $M_0$, and let $M$ be its rest mass and $v$ its speed (relative to the launch frame $S$) after it has emitted some radiation. All exhaust is radiation (the most efficient possible propellant, since photons carry the most momentum per unit energy). Work with $c = 1$.

1. By applying conservation of four-momentum to the emission of an infinitesimal burst of radiation, derive the differential relation between the rocket's rest mass $M$ and its rapidity $\phi$ (where $v = \tanh\phi$), and integrate it.
2. Deduce the **relativistic Tsiolkovsky equation** in the form
$$\gamma(1 + v) \;=\; \frac{M_0}{M},$$
and solve it for the final speed $v$ as a function of the mass ratio $M_0/M$.
3. Find the fraction of the initial rest mass that must be converted to radiation to reach $v = 0.99$, and compare with the Newtonian rocket result.
4. Show that the energy carried away by the radiation, measured in $S$, equals $M_0 - \gamma M$, and interpret this as the relativistic statement "exhaust energy $=$ rest-mass lost $-$ kinetic-plus-rest energy gained".

**Recall:**

![[Thm - Conservation of Four-Momentum#Statement]]

A burst of radiation emitted backward (in the $-x$ direction of $S$) is a collection of photons with total energy $\varepsilon$ and total three-momentum $-\varepsilon$ along $x$; its four-momentum is $(\varepsilon, -\varepsilon, 0, 0)$, which is [[Def - The Four-Momentum of a Photon|null]] ($\varepsilon^2 - \varepsilon^2 = 0$). The rocket of rest mass $M$ moving at speed $v$ has four-momentum $P = \gamma M(1, v, 0, 0) = (E, p, 0, 0)$ with $E = \gamma M$, $p = \gamma M v$. The **rapidity** $\phi$ is defined by $v = \tanh\phi$, so $\gamma = \cosh\phi$ and $\gamma v = \sinh\phi$ ([[Def - Rapidity]]); rapidities of collinear boosts add. The rest mass is the [[Def - Four-Momentum and Rest Mass|Minkowski length]] of the four-momentum, $P\cdot P = M^2$, and a mass-changing emission is governed by the four-force identity $F\cdot U = dm/d\tau$ from [[Def - Four-Force|the four-force]].

---

# Convergent Strategy

**Problem class.** A *mass-changing emission* problem solved by conservation of four-momentum, with the decisive simplification coming from rapidity: the natural variable is not $v$ (which adds awkwardly) but $\phi$ (which adds linearly), turning a differential equation into a trivial integral.

**Assumption pattern.** A body that ejects null four-momentum and thereby loses rest mass. The signpost is "rocket" or "continuous emission": you are not looking at a single collision but at an integrated sequence of infinitesimal recoils, each of which is a conservation-of-four-momentum statement.

**Theorem routing.** Each infinitesimal emission is [[Thm - Conservation of Four-Momentum|conservation of four-momentum]]; evaluating it in the rocket's *instantaneous rest frame* gives a clean relation $dM = -d\varepsilon$ (rest mass lost equals energy radiated) and a momentum kick $d p_{\text{rest}} = +d\varepsilon$, hence a rapidity increment $d\phi = d\varepsilon/M = -dM/M$. Integrating gives $M = M_0 e^{-\phi}$, and converting back to laboratory variables via $\gamma + \gamma v = e^{\phi}$ yields the Tsiolkovsky equation.

**Key decision point.** The crux is to work in the *instantaneous rest frame* of the rocket and to integrate the rapidity, not the velocity. In the rest frame the recoil is symmetric and the rest-mass change is simply $-d\varepsilon$; and because successive boosts compose by adding rapidities, the total effect of many infinitesimal kicks is the *sum* of their rapidity increments — an ordinary integral. Attempting the same in the velocity variable forces the velocity-addition formula at every step and obscures the simple exponential.

---

# Legal Operations Used

1. **Write down the total four-momentum and set it equal before and after** (operation 1 from the topic page). For each infinitesimal emission, $P_{\text{rocket, before}} = P_{\text{rocket, after}} + P_{\text{radiation}}$.

2. **Go to the rest frame of a chosen massive particle** (operation 4). Evaluating the emission in the rocket's instantaneous rest frame makes the rocket four-momentum $(M, \mathbf{0})$ and turns conservation into the elementary $dM = -d\varepsilon$, $dp = d\varepsilon$.

3. **Use the rapidity additivity of collinear boosts** ([[Def - Rapidity]]). Each kick adds $d\phi$ to the rapidity, so the integrated result is $\phi = \int d\phi$ — the device that linearises the problem.

4. **Use the mass-shell to convert between $(M, \phi)$ and $(E, p)$** (operation 8). The laboratory energy and momentum are $E = M\cosh\phi$, $p = M\sinh\phi$, so $E + p = M e^{\phi}$ packages the answer.

---

# Hints

> [!note]- Hint 1
> Do not track the whole history at once. Look at *one* infinitesimal emission, and look at it in the frame where the rocket is *momentarily at rest*. In that frame the rocket has four-momentum $(M, 0)$; it emits radiation of energy $d\varepsilon$ backward, with four-momentum $(d\varepsilon, -d\varepsilon)$ (null). Conservation then determines the rocket's new rest mass and its new (small) momentum.

> [!note]- Hint 2
> In the instantaneous rest frame, energy conservation gives $M = (M + dM) + d\varepsilon$, so $dM = -d\varepsilon$: the rest mass *decreases* by exactly the energy radiated. Momentum conservation gives the rocket a forward momentum $dp = +d\varepsilon = -dM$. A small momentum $dp$ given to a mass $M$ at rest is a rapidity increment $d\phi = dp/M$ (since $p = M\sinh\phi \approx M\phi$ for small $\phi$). Hence $d\phi = -dM/M$.

> [!note]- Hint 3
> Integrate $d\phi = -dM/M$ from the start ($\phi = 0$, $M = M_0$) to a general state ($\phi$, $M$): $\phi = -\ln(M/M_0) = \ln(M_0/M)$, i.e. $M = M_0 e^{-\phi}$. The rapidity is the logarithm of the mass ratio.

> [!note]- Hint 4
> Convert rapidity to laboratory speed. With $\gamma = \cosh\phi$ and $\gamma v = \sinh\phi$, $\gamma(1+v) = \cosh\phi + \sinh\phi = e^{\phi} = M_0/M$. Solve $\gamma(1+v) = M_0/M$ for $v$ using $\gamma(1+v) = \sqrt{(1+v)/(1-v)}$.

---

# Solution

The relativistic rocket is conservation of four-momentum integrated over a continuous emission, and the integration is trivial in the rapidity variable because collinear boosts add rapidities. The result is the exponential law $M = M_0 e^{-\phi}$, equivalently the relativistic Tsiolkovsky equation $\gamma(1+v) = M_0/M$.

**Step 1: One emission in the instantaneous rest frame gives $d\phi = -dM/M$.**

> [!note]- Derivation
> Consider the rocket at the instant it has rest mass $M$ and is momentarily at rest in an inertial frame $S^*$ (its instantaneous rest frame). Its four-momentum in $S^*$ is
> $$P_{\text{before}} = (M,\ 0,\ 0,\ 0).$$
> It emits a burst of radiation of energy $d\varepsilon$ (in $S^*$) straight backward, four-momentum $(d\varepsilon,\ -d\varepsilon,\ 0,\ 0)$ — null, as a photon burst must be. Afterward the rocket has rest mass $M + dM$ (with $dM < 0$) and some small forward velocity $d v^*$, hence four-momentum
> $$P_{\text{after}} = (M+dM)\big(1,\ dv^*,\ 0,\ 0\big) + O(dv^{*2}) = \big(M+dM,\ M\,dv^*,\ 0,\ 0\big)$$
> to first order. Conservation of four-momentum $P_{\text{before}} = P_{\text{after}} + P_{\text{radiation}}$ reads, component by component,
> $$M = (M + dM) + d\varepsilon \quad\Longrightarrow\quad dM = -\,d\varepsilon,$$
> $$0 = M\,dv^* - d\varepsilon \quad\Longrightarrow\quad M\,dv^* = d\varepsilon = -\,dM.$$
> The first equation is the content of [[Thm - Mass-Energy Equivalence|mass–energy equivalence]] for emission: the rocket's rest mass drops by precisely the radiated energy. The second is the recoil. Now a small velocity $dv^*$ acquired from rest *is* a small rapidity, $d\phi = dv^*$ (since $v = \tanh\phi \approx \phi$ near zero), so
> $$d\phi = dv^* = \frac{d\varepsilon}{M} = -\frac{dM}{M}.$$
> The rapidity gained equals minus the fractional rest-mass change. This is the entire physics of the rocket; everything else is integration.

**Step 2: Integrate to the exponential law and the Tsiolkovsky equation.**

> [!note]- Derivation
> Successive infinitesimal boosts are collinear (all along $+x$), and collinear boosts *add their rapidities* ([[Def - Rapidity]]) — this is exactly why rapidity, not velocity, is the right variable. So the rocket's total rapidity relative to the launch frame $S$ is the sum of all the increments,
> $$\phi = \int d\phi = -\int_{M_0}^{M}\frac{dM'}{M'} = -\ln\frac{M}{M_0} = \ln\frac{M_0}{M}, \qquad\text{i.e.}\qquad M = M_0\,e^{-\phi}.$$
> Now translate rapidity into the laboratory speed. With $\gamma = \cosh\phi$ and $\gamma v = \sinh\phi$,
> $$\gamma(1 + v) = \cosh\phi + \sinh\phi = e^{\phi} = \frac{M_0}{M},$$
> the **relativistic Tsiolkovsky equation**:
> $$\boxed{\ \gamma(1+v) = \frac{M_0}{M}\ }.$$
> Restoring $c$ and a finite exhaust speed $u \le c$ (so $d\phi = (u/c)\,(-dM/M)$ for a non-photon rocket) generalises this to $\gamma(1 + v/c)^{c/u} \cdots$; for the photon rocket $u = c$ and the clean form above holds. Squaring $\gamma(1+v) = M_0/M$ and using $\gamma^2(1+v)^2 = (1+v)/(1-v)$ gives the explicit final speed
> $$\frac{1+v}{1-v} = \left(\frac{M_0}{M}\right)^2 \quad\Longrightarrow\quad v = \frac{(M_0/M)^2 - 1}{(M_0/M)^2 + 1} = \frac{M_0^2 - M^2}{M_0^2 + M^2}.$$

**Step 3: Mass budget to reach $v = 0.99$, versus Newton.**

> [!note]- Derivation
> Invert for the required mass ratio: $\dfrac{M_0}{M} = \sqrt{\dfrac{1+v}{1-v}}$. For $v = 0.99$,
> $$\frac{M_0}{M} = \sqrt{\frac{1.99}{0.01}} = \sqrt{199} \approx 14.1.$$
> So the rocket must *start* about $14$ times heavier than it ends: only $M/M_0 \approx 1/14.1 \approx 7.1\%$ of the initial mass remains as payload, and the other $\approx 92.9\%$ is converted to radiation and ejected. For $v = 0.999$, $M_0/M = \sqrt{1999} \approx 44.7$, so only $2.2\%$ remains; the cost climbs steeply as $v\to c$, because $\gamma$ diverges and reaching the last sliver of speed demands ever more fuel.
>
> The *Newtonian* photon-like rocket (using $\mathbf{p} = m\mathbf{u}$ and treating exhaust speed $c$) would give the ordinary Tsiolkovsky law $v = c\,\ln(M_0/M)$, predicting $v = 0.99c$ at $M_0/M = e^{0.99} \approx 2.7$ — almost six times less fuel than relativity actually demands. The Newtonian formula even permits $v > c$ for $M_0/M > e$, which is nonsense; the relativistic law instead has $v\to c$ only as $M_0/M\to\infty$. The contrast is the [[Special Relativity XIII — Energy and Momentum#Legal Operations|illegal Newtonian momentum]] making the speed limit invisible.

**Step 4: The radiated energy.**

> [!note]- Derivation
> Total four-momentum is conserved in the launch frame $S$. Initially the rocket is at rest with four-momentum $(M_0, 0)$; finally it has $(\gamma M, \gamma M v)$ and the total radiation emitted over the whole flight has some four-momentum $(\mathcal{E}_\gamma, \mathcal{P}_\gamma)$ with $\mathcal{E}_\gamma = -\mathcal{P}_\gamma$ wait — the radiation goes backward, so its $S$-momentum is negative, $\mathcal{P}_\gamma = -\mathcal{E}_\gamma$ for a single direction; in general the bursts were emitted from a moving rocket so they are not all monochromatic, but energy conservation still gives, for the time component,
> $$M_0 = \gamma M + \mathcal{E}_\gamma \quad\Longrightarrow\quad \mathcal{E}_\gamma = M_0 - \gamma M.$$
> So the radiation carries away exactly the initial rest energy minus the rocket's final *total* (relativistic) energy $\gamma M$. Read as a balance sheet: the rest mass *lost* is $M_0 - M$; of this, an amount $\gamma M - M = (\gamma - 1)M$ has gone into the rocket's own kinetic energy, and the remainder
> $$\mathcal{E}_\gamma = (M_0 - M) - (\gamma - 1)M = M_0 - \gamma M$$
> is radiated. Mass converted is split between the kinetic energy the rocket keeps and the energy it throws away — and because the exhaust must carry backward momentum to push the rocket forward, a photon rocket is forced to "waste" a large share of the converted mass as exhaust energy, which is the deep reason the mass ratios in Step 3 are so punishing.

> [!note]- Complete formal solution
> In the rocket's instantaneous rest frame, emitting radiation of energy $d\varepsilon$ backward conserves four-momentum as $dM = -d\varepsilon$ (rest mass lost $=$ energy radiated) and $M\,dv^* = d\varepsilon$, giving a rapidity increment $d\phi = dv^* = -dM/M$. Collinear boosts add rapidities, so $\phi = -\int_{M_0}^{M}dM'/M' = \ln(M_0/M)$, hence $M = M_0 e^{-\phi}$. Converting with $\gamma = \cosh\phi$, $\gamma v = \sinh\phi$: $\gamma(1+v) = e^{\phi} = M_0/M$ (relativistic Tsiolkovsky), so $(1+v)/(1-v) = (M_0/M)^2$ and $v = (M_0^2 - M^2)/(M_0^2 + M^2)$. Reaching $v = 0.99$ needs $M_0/M = \sqrt{199}\approx 14.1$ (about $93\%$ of the mass radiated), against the Newtonian $e^{0.99}\approx 2.7$. Launch-frame energy conservation $M_0 = \gamma M + \mathcal{E}_\gamma$ gives radiated energy $\mathcal{E}_\gamma = M_0 - \gamma M = (M_0 - M) - (\gamma-1)M$, the converted mass minus the rocket's retained kinetic energy. $\blacksquare$

---

# Key Takeaways

**Rapidity is the rocket's natural variable — emissions add rapidities, so the velocity law is exponential.** The single move that makes the relativistic rocket tractable is to integrate the rapidity rather than the velocity. Each infinitesimal recoil is a small collinear boost, and collinear boosts compose by *adding* rapidities, so the total rapidity is the plain integral of the increments, $\phi = -\int dM/M = \ln(M_0/M)$. Had one tried to track the velocity directly, every infinitesimal kick would require the velocity-addition formula, and the simple structure would be buried. The lesson generalises far beyond rockets: whenever a relativistic process is built from many successive collinear boosts — a sequence of accelerations, a chain of frames, hyperbolic motion — switch to rapidity, where the boosts are additive and the calculus is Euclidean. The exponential $M = M_0 e^{-\phi}$ and the appearance of $e^{\phi} = \gamma(1+v)$ are the fingerprints of this additivity.

**Rest mass lost equals energy radiated — the rocket is mass–energy equivalence in motion.** The relation $dM = -d\varepsilon$, derived in one line in the instantaneous rest frame, is the operational heart of $E = mc^2$: the rocket *is* a machine for converting rest mass into the energy of ejected radiation. This is not an analogy but an identity forced by conservation of four-momentum, and it makes the rocket the cleanest dynamical illustration of the chapter's central fact that mass is a form of energy and is not separately conserved. The overall energy budget $\mathcal{E}_\gamma = (M_0 - M) - (\gamma - 1)M$ then shows precisely where the converted mass goes — part into the rocket's kinetic energy, the rest thrown overboard as exhaust — and exposes the inefficiency that no propulsion scheme can evade: to gain forward momentum you must give the exhaust backward momentum, and the exhaust energy that carries it is energy the payload never sees.

**The relativistic speed limit shows up as a punishing mass ratio — $v\to c$ costs $M_0/M\to\infty$.** Comparing the relativistic Tsiolkovsky equation $\gamma(1+v) = M_0/M$ with its Newtonian counterpart $v = c\ln(M_0/M)$ is the most vivid demonstration in the chapter of how the speed limit is enforced dynamically. The Newtonian law cheerfully predicts any speed for a large enough mass ratio, including $v > c$; the relativistic law instead requires $M_0/M = \sqrt{(1+v)/(1-v)}$, which diverges as $v\to c$, so no finite amount of fuel ever reaches the speed of light. Reaching $0.99c$ already demands burning $93\%$ of the initial mass, and each further nine of the speed roughly squares the required ratio. The reusable diagnostic: whenever a Newtonian formula for a cumulative process (rocket speed, accumulated velocity, energy gained under constant force) lets a speed cross $c$, the relativistic correction will replace the offending linear or logarithmic growth with a quantity that diverges exactly at $c$ — here, the mass ratio; for a charged particle in a field, the time; for velocity addition, the rapidity sum.
