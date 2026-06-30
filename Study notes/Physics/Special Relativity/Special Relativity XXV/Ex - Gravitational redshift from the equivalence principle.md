---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Gravitational Redshift"
  - "Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity"
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
tags: [physics, special-relativity]
---

# Problem Statement

This is the exercise that turns the equivalence principle into a measurable number, the gravitational redshift. We derive it three ways — accelerated-frame Doppler, photon energy conservation, accelerated-clock period — and verify they agree, then evaluate the result for the Pound-Rebka tower experiment.

Two observers $\mathcal{O}$ (at $x = 0$, the receiver) and $\mathcal{O}'$ (at altitude $x_{\mathrm{em}} > 0$, the emitter) are mutually at rest in a uniform gravitational field $\vec g = -\gamma\,\vec e_x$ (with $\gamma > 0$). The emitter $\mathcal{O}'$ sends a periodic signal of proper period $\Delta t'$ down to $\mathcal{O}$.

1. *Equivalence-principle substitution.* By the equivalence principle, the observers are equivalent to uniformly accelerated observers in flat spacetime, with proper acceleration $\vec a = (\gamma/c^2)\,\vec e_x$. Set up this auxiliary problem precisely.
2. *Accelerated-frame Doppler.* Compute the time it takes a downward-travelling photon to reach $\mathcal{O}$. During this transit, find the velocity the receiver has gained *toward* the oncoming photon. Apply the first-order Doppler formula to get the received period
$$\Delta t = \frac{\Delta t'}{1 + \gamma\,x_{\mathrm{em}}/c^2}.$$
3. *Photon energy conservation.* Treat the photon as having gravitational mass $h\nu/c^2$ (from $E = mc^2$) and demand energy conservation as it climbs the potential. Recover the same fractional shift $\Delta\nu/\nu = -\Delta\Phi/c^2$.
4. *Pound-Rebka experiment.* The 1960 experiment of Pound and Rebka used ${}^{57}\mathrm{Fe}$ Mössbauer gamma rays ($E = 14.4\,\mathrm{keV}$, frequency $\nu \approx 3.5\times 10^{18}\,\mathrm{Hz}$) over the $h = 22.5\,\mathrm{m}$ Jefferson tower at Harvard. Compute the predicted fractional shift $\Delta\nu/\nu$ for upward propagation, and identify why the Mössbauer effect was *required* to resolve the shift.
5. *Sign check.* Convince yourself that the shift is a *redshift* for a signal going up (out of the potential well) and a *blueshift* for a signal going down. State this in terms of the gravitational potential difference $\Delta\Phi = \Phi_{\mathrm{rec}} - \Phi_{\mathrm{em}}$.

**Recall:**

![[Thm - Gravitational Redshift#Statement]]

![[Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity#Statement]]

The exercise uses the equivalence principle to import the spectral shift between two accelerated observers — pure flat-spacetime kinematics — into the gravitational setting. The accelerated-frame period relation between two observers of common proper acceleration $a$ is, exactly,
$$\Delta t = \frac{\Delta t'}{1 + a\,x_{\mathrm{em}}/c^2},$$
which is what was derived from the [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|hyperbolic motion]] of [[Special Relativity XVI — Accelerated Observers|XVI]].

---

# Convergent Strategy

**Problem class.** A *equivalence-principle calculation*, of the kind solved in [[Thm - Gravitational Redshift]]. Replace gravity by uniform acceleration, apply the flat-spacetime accelerated-observer kinematics, translate back. The exercise's pedagogical purpose is to derive the same answer three independent ways, exposing the result as robust.

**Assumption pattern.** Two ingredients: a uniform gravitational field (so the field can be exactly replaced by a uniform acceleration), and two observers mutually at rest in it (so the redshift between their clocks is well-defined and time-independent). The result generalises to a non-uniform static field by integrating along the line of constant potential.

**Theorem routing.** Part 1 invokes the equivalence principle (operation 2 from the topic page) to set up the auxiliary accelerated-frame problem. Part 2 uses the first-order Doppler formula on a receiver gaining velocity toward an oncoming photon during its transit. Part 3 uses photon mass-energy equivalence and energy conservation in a potential. Part 4 plugs in numbers. Part 5 fixes the sign by appealing to energy conservation: a photon climbing out of a well loses energy, hence frequency, hence is redshifted.

**Key decision point.** The crux is that *all three* derivations give the same answer to first order. This redundancy is not a coincidence — it is the signature of a result forced by symmetry (the equivalence principle plus a uniform field), not by any particular dynamical mechanism. The reusable lesson: when an effect can be computed by independent routes that all agree, it is a robust prediction immune to detailed model assumptions.

---

# Legal Operations Used

1. **Invoke the equivalence principle to swap a gravitational field for an accelerated frame** (operation 2 from the topic page): part 1 — the whole derivation is built on this substitution.

2. **Derive the redshift from the accelerated-frame spectral shift** (operation 6 from the topic page): part 2 — the accelerated-receiver Doppler argument.

3. **Take the Newtonian (weak, slow) limit** (operation 1 from the topic page): part 4 — the linearised formula $\Delta\nu/\nu = -gh/c^2$ is the small-shift limit of the exact $1/(1+\gamma x_{\mathrm{em}}/c^2)$.

---

# Hints

> [!note]- Hint 1
> A static observer at height $x_{\mathrm{em}}$ in a field of strength $g$ must be supported by a force producing proper acceleration $+g$ upward (the floor pushes up on you with normal force $mg$, opposing the gravitational pull $mg$ downward). So the equivalent flat-spacetime configuration is two observers undergoing common proper acceleration $\vec a = (\gamma/c^2)\vec e_x$ upward, one at $x = 0$ (receiver $\mathcal{O}$) and one at $x = x_{\mathrm{em}}$ (emitter $\mathcal{O}'$).

> [!note]- Hint 2
> Photon transit time: $t_{\mathrm{transit}} \approx x_{\mathrm{em}}/c$. During this time the receiver accelerates upward at $a = \gamma/c^2$, gaining velocity $\Delta v = a\,t_{\mathrm{transit}} = \gamma x_{\mathrm{em}}/c^3$ in the $+\vec e_x$ direction. The receiver moves *toward* the downward-falling photon at $\Delta v$, so by first-order Doppler the received frequency is *higher* (blueshift): $\nu_{\mathrm{rec}}/\nu_{\mathrm{em}} = 1 + \Delta v/c = 1 + \gamma x_{\mathrm{em}}/c^2$. Equivalently $\Delta t = \Delta t'/(1 + \gamma x_{\mathrm{em}}/c^2)$ — receiver sees the period shortened. (For an upward photon, the geometry flips: receiver accelerates away from the oncoming photon, redshift.)

> [!note]- Hint 3
> Photon at the top has energy $E_{\mathrm{em}} = h\nu_{\mathrm{em}}$. It descends to the bottom; during the descent it gains kinetic energy from the gravitational potential, $\Delta E = (h\nu_{\mathrm{em}}/c^2)\cdot g\cdot x_{\mathrm{em}}$, by analogy with a mass falling. So at the bottom $E_{\mathrm{rec}} = h\nu_{\mathrm{em}}(1 + g x_{\mathrm{em}}/c^2)$, and $\nu_{\mathrm{rec}} = \nu_{\mathrm{em}}(1 + g x_{\mathrm{em}}/c^2)$ — blueshift on descent, same answer as part 2.

> [!note]- Hint 4
> $h = 22.5\,\mathrm{m}$, $g = 9.8\,\mathrm{m\,s^{-2}}$, $c = 3\times 10^8\,\mathrm{m\,s^{-1}}$. For *upward* propagation, $\Delta\nu/\nu = -gh/c^2 = -(9.8)(22.5)/(9\times 10^{16}) \approx -2.45\times 10^{-15}$. Without the Mössbauer effect, thermal motion of emitting atoms broadens the gamma line by $\sim 10^{-6}$, swamping the shift by 9 orders of magnitude. The Mössbauer effect — recoilless emission and absorption by gamma-ray transitions in nuclei locked in a crystal lattice — gives line widths $\sim 10^{-12}$, narrow enough to *resolve* a $10^{-15}$ shift.

> [!note]- Hint 5
> Energy conservation. A photon climbing up the potential does work against gravity, losing energy: $\Delta E = -(E/c^2)g h$, so $\Delta\nu/\nu = -gh/c^2 < 0$ — *redshift* (frequency drops, period lengthens). Falling down, it gains energy: blueshift. In potential terms: $\Delta\Phi = \Phi_{\mathrm{rec}} - \Phi_{\mathrm{em}}$. For upward, $\Phi_{\mathrm{rec}} > \Phi_{\mathrm{em}}$, so $\Delta\Phi > 0$, and the formula $\Delta\nu/\nu = -\Delta\Phi/c^2$ correctly gives negative (redshift). Pattern: positive $\Delta\Phi$ (climbing) $\Rightarrow$ negative $\Delta\nu$ (red); negative $\Delta\Phi$ (descending) $\Rightarrow$ positive $\Delta\nu$ (blue).

---

# Solution

The exercise turns the equivalence principle into the quantitative gravitational redshift, the first measurable consequence of relativistic gravity and the seed of every later result of the chapter. Three independent derivations agree — the accelerated-frame Doppler, photon energy conservation, and the accelerated-clock period — and the prediction is then confirmed by Pound and Rebka in 1960.

**Step 1: The equivalence-principle setup.**

> [!note]- Derivation
> By the equivalence principle, two observers $\mathcal{O}$, $\mathcal{O}'$ at rest at altitudes $0$, $x_{\mathrm{em}}$ in the field $\vec g = -\gamma\vec e_x$ are physically equivalent to two uniformly accelerated observers in flat Minkowski space, sharing common proper acceleration $\vec a = (\gamma/c^2)\,\vec e_x$ (upward). Specifically, the receiver $\mathcal{O}$ accelerates upward at $\gamma/c^2$ from the origin, and the emitter $\mathcal{O}'$ accelerates upward at $\gamma/c^2$ from height $x_{\mathrm{em}}$. Both maintain their separation rigidly (Born rigidity in the appropriate limit; see [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)]]).
>
> The emitter sends a periodic signal of proper period $\Delta t'$ downward toward the receiver, who measures it with proper period $\Delta t$. We want the relation between $\Delta t'$ and $\Delta t$.

**Step 2: Accelerated-frame Doppler derivation.**

> [!note]- Derivation
> Consider one cycle of the signal: a wave crest is emitted at $\mathcal{O}'$ at proper time $0$ and the next crest is emitted at proper time $\Delta t'$. Each propagates downward at the speed of light.
>
> Working in the (instantaneous) global inertial frame in which both observers are momentarily at rest at the emission of the first crest:
> - First crest: emitted at $(t_1, x_1) = (0, x_{\mathrm{em}})$, reaches $\mathcal{O}$ (at the origin) after a transit time $\approx x_{\mathrm{em}}/c$.
> - Second crest: emitted at $(t_2, x_2) \approx (\Delta t', x_{\mathrm{em}})$ (the emitter has accelerated upward by a negligible $\sim a\Delta t'^2/2$ in time $\Delta t'$), reaches $\mathcal{O}$ after a transit time $\approx x_{\mathrm{em}}/c$.
>
> So in the global frame, the two crests arrive at the origin at times $\approx x_{\mathrm{em}}/c$ and $\approx \Delta t' + x_{\mathrm{em}}/c$, with a separation of $\Delta t'$ (essentially unchanged from the emission separation). But $\mathcal{O}$ is *not* at the origin when the second crest arrives — she has accelerated upward during the time $\Delta t' + x_{\mathrm{em}}/c$, with velocity at that moment $v_2 = a\,(\Delta t' + x_{\mathrm{em}}/c)$ and position $x_2^{(\mathcal{O})} \approx \tfrac12 a (\Delta t' + x_{\mathrm{em}}/c)^2$.
>
> More cleanly, consider the *velocity gained by $\mathcal{O}$ during the photon's transit* of duration $x_{\mathrm{em}}/c$:
> $$\Delta v = a\cdot\frac{x_{\mathrm{em}}}{c} = \frac{\gamma\,x_{\mathrm{em}}}{c^3}.$$
> This velocity is directed *upward* — i.e., *toward* the oncoming photon. A receiver moving toward a signal at velocity $\Delta v$ sees the photon blueshifted by first-order Doppler:
> $$\frac{\nu_{\mathrm{rec}}}{\nu_{\mathrm{em}}} = 1 + \frac{\Delta v}{c} = 1 + \frac{\gamma\,x_{\mathrm{em}}}{c^2}.$$
> In terms of periods:
> $$\Delta t = \frac{\Delta t'}{1 + \gamma\,x_{\mathrm{em}}/c^2}.\qquad\checkmark$$
> This *is* the gravitational redshift formula (for *downward* propagation; upward gives the inverse with the same magnitude). The result agrees, to first order in $\gamma x_{\mathrm{em}}/c^2$, with the exact accelerated-clock period relation of [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)]].

**Step 3: Photon energy conservation cross-check.**

> [!note]- Derivation
> The photon, treated as a quantum of energy $E = h\nu$, has effective gravitational mass $m = E/c^2 = h\nu/c^2$ by [[Thm - Mass-Energy Equivalence|mass-energy equivalence]] (Einstein 1907). When this "mass" descends through the potential difference $\Delta\Phi = \Phi(\text{top}) - \Phi(\text{bottom}) = \gamma x_{\mathrm{em}}$ (with the convention that lower is more negative for a planet), it gains kinetic energy:
> $$\Delta E_{\mathrm{photon}} = +m\,g\,x_{\mathrm{em}} = \frac{h\nu_{\mathrm{em}}}{c^2}\,\gamma\,x_{\mathrm{em}} = h\nu_{\mathrm{em}}\,\frac{\gamma x_{\mathrm{em}}}{c^2}.$$
> Energy conservation: $E_{\mathrm{rec}} = E_{\mathrm{em}} + \Delta E$, hence
> $$h\nu_{\mathrm{rec}} = h\nu_{\mathrm{em}}\left(1 + \frac{\gamma x_{\mathrm{em}}}{c^2}\right) \quad\Longrightarrow\quad \frac{\nu_{\mathrm{rec}}}{\nu_{\mathrm{em}}} = 1 + \frac{\gamma x_{\mathrm{em}}}{c^2} = 1 + \frac{\Delta\Phi}{c^2}.$$
> Identical to part 2. *Crucially*, no detail of the photon's trajectory entered — only that it traversed a potential difference $\Delta\Phi$ and that energy is conserved. The result is forced by thermodynamics.
>
> The deeper meaning: the agreement between Doppler and energy-conservation arguments is a sign that the redshift is a property of *clocks*, not of light. The accelerated-frame argument derives it from the receiver's motion; the energy argument derives it from the photon's energy bookkeeping; but they must agree because both are constrained by the same equivalence principle, and the underlying content is that proper time itself depends on gravitational potential.

**Step 4: Pound-Rebka.**

> [!note]- Derivation
> Plug in $h = 22.5\,\mathrm{m}$, $g = 9.8\,\mathrm{m\,s^{-2}}$, $c = 3\times 10^8\,\mathrm{m\,s^{-1}}$:
> $$\frac{\Delta\nu}{\nu} = -\frac{g\,h}{c^2} = -\frac{(9.8)(22.5)}{(3\times 10^8)^2} = -\frac{220.5}{9\times 10^{16}} \approx -2.45\times 10^{-15}.$$
> So a $14.4\,\mathrm{keV}$ gamma ray climbing the tower is redshifted by $\Delta E/E \approx 2.5\times 10^{-15}$, or $\Delta E \approx 3.5\times 10^{-11}\,\mathrm{eV}$ — an utterly tiny energy shift on top of a $14\,\mathrm{keV}$ photon.
>
> *Why the Mössbauer effect was indispensable.* In an ordinary atomic or nuclear transition, the emitting nucleus recoils to conserve momentum, shifting the emitted photon's frequency by $\Delta\nu/\nu_{\mathrm{recoil}} \sim E/(M c^2)$. For ${}^{57}\mathrm{Fe}$ at $14.4\,\mathrm{keV}$, $M c^2 \approx 53\,\mathrm{GeV}$, so $\Delta\nu/\nu_{\mathrm{recoil}} \sim 14.4\times 10^3 / 53\times 10^9 \sim 2.7\times 10^{-7}$ — many orders of magnitude larger than the gravitational shift. Additionally, thermal motion of the nuclei broadens the line by $\Delta\nu/\nu_{\mathrm{thermal}} \sim \sqrt{kT/Mc^2} \sim 10^{-6}$ at room temperature. The Mössbauer effect — recoilless emission and absorption by nuclei locked in a crystal lattice, so the *whole crystal* absorbs the recoil — eliminates the recoil shift entirely and reduces the thermal broadening, giving a line width of $\Delta\nu/\nu \sim 10^{-13}$, just narrow enough to resolve a $10^{-15}$ shift. The technique earned Rudolf Mössbauer the 1961 Nobel Prize, partly because it enabled this gravitational redshift measurement.
>
> Pound and Rebka used a Doppler shift of the source itself (vibrating it at a few $\mu\mathrm{m\,s^{-1}}$) to compensate for the gravitational shift, recording the velocity at which the gamma rays were absorbed maximally. Their result: $0.99\pm 0.05$ times the predicted $\Delta\nu/\nu = -2.45\times 10^{-15}$ — confirming Einstein's prediction at the $5\%$ level. A 1965 refinement (Pound-Snider) tightened this to $1\%$. The equivalence principle, derived in 1907, was confirmed to $1\%$ in 1965 — over a 58-year arc punctuated by general relativity.

**Step 5: Sign check.**

> [!note]- Derivation
> *Upward propagation* (signal climbing out of the well, from low to high potential): photon does work against gravity, loses energy, $\nu$ decreases — **redshift**, $\Delta\nu < 0$.
>
> *Downward propagation* (signal falling into the well, from high to low potential): photon gains energy, $\nu$ increases — **blueshift**, $\Delta\nu > 0$.
>
> Sign rule: $\Delta\nu/\nu = -\Delta\Phi/c^2$, where $\Delta\Phi = \Phi(\mathrm{receiver}) - \Phi(\mathrm{emitter})$.
> - Upward ($\Phi_{\mathrm{rec}} > \Phi_{\mathrm{em}}$): $\Delta\Phi > 0$, $\Delta\nu < 0$. $\checkmark$ Redshift.
> - Downward ($\Phi_{\mathrm{rec}} < \Phi_{\mathrm{em}}$): $\Delta\Phi < 0$, $\Delta\nu > 0$. $\checkmark$ Blueshift.
>
> Equivalent clock-rate statement: *a clock at higher potential runs faster* than one at lower potential, by the fractional rate $\Delta\Phi/c^2$. The Earth's surface clock runs slow compared to a clock on a mountain (gravitational redshift); the GPS satellite clock runs *fast* compared to the ground (it is higher in the potential), which is the dominant relativistic correction to GPS — see the next exercise [[Ex - The relativistic clock corrections in GPS]].
>
> Pneumonic: *deeper in the well, slower the clock*. Or: *light climbing out of a well loses energy*. Both encode the same physical fact, the second by photon, the first by clock.

> [!note]- Complete formal solution
> (1) Equivalence principle: replace observers at rest in $\vec g = -\gamma\vec e_x$ at altitudes $0, x_{\mathrm{em}}$ by uniformly accelerated observers in flat space with proper acceleration $\vec a = (\gamma/c^2)\vec e_x$ upward, same separation $x_{\mathrm{em}}$. (2) For a downward-propagating photon: transit time $x_{\mathrm{em}}/c$, during which $\mathcal{O}$ gains velocity $\Delta v = a x_{\mathrm{em}}/c = \gamma x_{\mathrm{em}}/c^3$ *toward* the photon (since $\mathcal{O}$ accelerates upward). First-order Doppler: $\nu_{\mathrm{rec}}/\nu_{\mathrm{em}} = 1 + \Delta v/c = 1 + \gamma x_{\mathrm{em}}/c^2$, blueshift, period $\Delta t = \Delta t'/(1+\gamma x_{\mathrm{em}}/c^2)$. (3) Photon energy conservation: with $m_{\mathrm{photon}} = h\nu/c^2$, energy gained on descent $\Delta E = m g x_{\mathrm{em}} = h\nu_{\mathrm{em}}\gamma x_{\mathrm{em}}/c^2$, so $\nu_{\mathrm{rec}}/\nu_{\mathrm{em}} = 1 + \gamma x_{\mathrm{em}}/c^2$ — same answer, no trajectory detail. (4) Pound-Rebka: $h = 22.5\,\mathrm{m}$, $g = 9.8\,\mathrm{m\,s^{-2}}$, upward gives $\Delta\nu/\nu = -gh/c^2 = -2.45\times 10^{-15}$, an energy shift of $\sim 3.5\times 10^{-11}\,\mathrm{eV}$ on a $14.4\,\mathrm{keV}$ Mössbauer gamma. The Mössbauer effect (recoilless emission/absorption in a crystal lattice) is required because ordinary recoil and thermal broadening exceed the shift by 8+ orders of magnitude; the Mössbauer line width $\sim 10^{-13}$ allows the $10^{-15}$ shift to be resolved. Pound-Rebka 1960 confirmed the prediction to $5\%$, Pound-Snider 1965 to $1\%$. (5) Sign rule $\Delta\nu/\nu = -\Delta\Phi/c^2$: upward (positive $\Delta\Phi$) is redshift, downward is blueshift; equivalently, a clock deeper in the potential runs slow by $\Delta\Phi/c^2$. $\blacksquare$

---

# Key Takeaways

**Three independent derivations agree because the gravitational redshift is forced by the equivalence principle and energy conservation, not by any detail of the field or the photon trajectory.** The exercise's most important structural lesson is the *robustness* of the result: the same $\Delta\nu/\nu = -\Delta\Phi/c^2$ emerges from the accelerated-frame Doppler argument (which uses receiver motion), photon energy conservation (which uses mass-energy equivalence), and the exact accelerated-clock period relation (which uses Rindler kinematics). When three completely different physical pictures give the identical answer, the answer is not an artifact of any one picture but a consequence of the deeper assumptions all three share — here, the equivalence principle and the proportionality of energy and inertial mass. This is the signature of a result one can trust. The reusable problem-solving lesson: when computing an effect for the first time, try at least two independent routes; agreement is the most powerful sanity check available, and it is also how Einstein convinced himself the redshift was real in 1907 (he discovered it twice — once by Doppler, once by energy conservation — before publishing).

**The Mössbauer effect made the redshift a measurable laboratory quantity by suppressing the recoil and thermal noise that would otherwise drown it.** The Pound-Rebka experiment is a beautiful case study in *technique meeting prediction*. The gravitational redshift over a $22\,\mathrm{m}$ tower is $\sim 10^{-15}$, smaller than recoil shifts ($\sim 10^{-7}$) and thermal Doppler broadening ($\sim 10^{-6}$) by 8–9 orders of magnitude. The Mössbauer effect — recoilless gamma emission and absorption by ${}^{57}\mathrm{Fe}$ nuclei locked in a crystal lattice, with the lattice absorbing the recoil — eliminates the recoil shift and gives line widths of $\sim 10^{-13}$, just narrow enough to resolve the shift. Pound and Rebka used a calibrated vibration of the source as a Doppler compensator. The lesson is methodological: a prediction that looks technologically inaccessible can suddenly become measurable when a serendipitously developed technique appears. The Mössbauer effect was discovered in 1958 for unrelated reasons; within two years it enabled the first laboratory confirmation of the equivalence principle's redshift consequence. Modern atomic clocks now measure redshifts over $\sim 30\,\mathrm{cm}$ height differences ($\sim 10^{-17}$), with even Mössbauer-free precision.

**The redshift is a statement about clocks, not photons — and that is why it forces a position-dependent metric.** Although energy conservation makes the calculation work in terms of photon energies, the physical content of the redshift is that *the emitting clock at depth runs slower* than the receiving clock at altitude. The photon just carries the news. This is why the redshift is the lever that pries spacetime loose from flatness (see [[Ex - Why the gravitational redshift forces a position-dependent metric]]): if proper time depended on position, no time-translation-invariant metric like $\eta_{\mu\nu}$ could measure it — proper time must instead come from a position-dependent metric $g_{\mu\nu}(x)$, and that is general relativity. The reusable thread: whenever you compute a relativistic effect in terms of photon energy or wave bookkeeping, ask whether the deeper content is really about *time itself* (clock rates, periods, simultaneity) — and you will usually find the answer is yes. Photons are convenient probes; what is being probed is the metric.
