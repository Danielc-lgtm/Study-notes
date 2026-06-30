---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity"
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
tags: [physics, special-relativity]
---

# Problem Statement

A physicist is sealed in a windowless cabin. She is allowed any local apparatus — clocks, accelerometers, lasers, plumb lines, freely-falling test particles — but no signal from outside. Consider the following two situations:

**Situation A.** The cabin sits at rest on the surface of a planet whose surface gravity is $\vec g = -g\,\vec e_x$ ($g > 0$, $\vec e_x$ pointing upward).

**Situation B.** The cabin is in deep, gravity-free space, accelerating uniformly with proper acceleration $\vec a = g\,\vec e_x$, the floor pushing "up" against the physicist's feet.

1. Show that no measurement of the *fall of a test particle* released at the centre of the cabin can distinguish A from B.
2. Show that an *accelerometer fixed to the floor* gives the same reading $g$ in both situations.
3. Argue that a *horizontal laser beam* fired across the cabin falls toward the floor in B, hence (by the equivalence principle) must do the same in A — predicting the gravitational deflection of light from a thought experiment with no field equation.
4. Argue that a *clock at the ceiling* runs faster than one on the floor in B, hence must do the same in A — predicting the gravitational redshift from the same thought experiment.
5. State a *physical* measurement that *would* distinguish A from B, and identify it with the irreducible part of gravity that no acceleration can mimic.

**Recall:**

![[Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity#Statement]]

The equivalence principle is the experimentally ironclad statement that, for *local* measurements, a uniform gravitational field cannot be distinguished from a uniformly accelerated frame. Its physical content is the equality of inertial and gravitational mass — the universality of free fall — which Eötvös verified to one part in $10^8$ and modern experiments to $3\times 10^{-13}$. Locally, situations A and B are physically identical; the substitution of B for A is the operational meaning of "by the equivalence principle".

---

# Convergent Strategy

**Problem class.** A *predict-by-equivalence-principle* problem, of the kind solved in [[Thm - Gravitational Redshift|the redshift theorem]] and [[Thm - Light Deflection|the deflection theorem]]. The procedure: replace situation A by situation B, compute the answer in flat spacetime using accelerated-frame kinematics, then assert the same answer holds in A. The thought experiment makes the substitution physically transparent and is the historical route by which Einstein first reached the redshift and the light deflection.

**Assumption pattern.** Two ingredients sit at the heart of the equivalence principle: the equality $m_{\mathrm{inert}} = m_{\mathrm{grav}}$ (which makes test-particle free-fall universal) and the *uniformity* of the field (which makes the entire field, not just one event, mimicked by an acceleration). Both are needed: without equal masses, different particles would fall differently in A but identically in B; without uniformity, the cabin would feel tidal forces in A but not in B.

**Theorem routing.** Parts 1–2 use only that all bodies fall with the same acceleration $g$ in both A and B, so the relative motion of cabin and test particles is identical — pure Newtonian kinematics. Part 3 imports light-bending from B (where it is elementary: while light crosses the cabin, the cabin accelerates upward) to A by the equivalence principle, and routes to [[Thm - Light Deflection]]. Part 4 imports the redshift from B (where it is the Doppler shift between an accelerating emitter and receiver) to A, routing to [[Thm - Gravitational Redshift]]. Part 5 exposes the boundary of the equivalence principle — *tidal* effects from field inhomogeneity, which an acceleration cannot reproduce — routing to the geodesic deviation of [[General Relativity I — Einstein's Equations and Schwarzschild]].

**Key decision point.** The crux is recognising that the equivalence principle is *local*: it asserts the indistinguishability of A and B only in a region small enough that the field is uniform and the duration short enough that tidal effects do not accumulate. Within that region the substitution A $\leftrightarrow$ B is exact and licenses any flat-spacetime computation; outside it, the inhomogeneity of any real field is the irreducible residue and the natural diagnostic of A versus B.

---

# Legal Operations Used

1. **Invoke the equivalence principle to swap a gravitational field for an accelerated frame** (operation 2 from the topic page): the whole exercise is one sustained application of this move, replacing situation A by situation B and computing in flat spacetime.

2. **Derive the redshift from the accelerated-frame spectral shift** (operation 6 from the topic page): part 4 imports the Doppler shift between two accelerated observers and reinterprets it gravitationally.

3. **Set the gravitational charge equal to the inertial mass** (operation 4 from the topic page): part 1 uses universality of free fall — equal masses — to argue that *every* test particle falls identically in A, just as in B.

---

# Hints

> [!note]- Hint 1
> In B (no gravity, cabin accelerating up at $g$), a particle released at the cabin's centre is inertial — it continues to drift at its initial velocity in the global flat frame. The cabin, however, accelerates upward. Relative to the cabin, the particle "falls" with acceleration $g$ downward. In A (no acceleration, gravity $g$ down), the particle falls with acceleration $g$ downward in the cabin frame, by Newton. The two relative motions are identical. By the equality of inertial and gravitational mass, this is true for every particle regardless of its composition.

> [!note]- Hint 2
> An accelerometer measures *proper acceleration* — what a freely-falling reference body does relative to the accelerometer. In both A and B, the accelerometer, bolted to the floor, has the same proper acceleration ($g$ upward) as the cabin. A freely-falling reference inside the device accelerates downward at $g$ relative to the floor. The reading is $g$ in both cases.

> [!note]- Hint 3
> In B, fire a horizontal laser pulse from one wall to the other, distance $L$. Transit time $L/c$. During this time the cabin moves *up* by $\tfrac12 g(L/c)^2$, so the pulse strikes the far wall a height $\tfrac12 g L^2/c^2$ *below* the point opposite the emitter — the beam "falls". By the equivalence principle, the same fall occurs in A: light bends downward in a gravitational field. The angle of deflection per unit length is $g/c^2$. This is *qualitatively* the light deflection of [[Thm - Light Deflection]].

> [!note]- Hint 4
> In B, a clock at the ceiling (height $h$ above the floor) emits light pulses to a receiver on the floor. While each pulse travels, the floor accelerates upward, *toward* the pulse — a blueshift. Equivalently a floor-emitted pulse climbing to the ceiling encounters a ceiling that has accelerated *away* — a redshift. The fractional shift is $\Delta\nu/\nu = -g h / c^2$ upward. By the equivalence principle the same happens in A: clocks at higher gravitational potential run *faster* (or equivalently, light climbing out of a potential well is redshifted). This is [[Thm - Gravitational Redshift]].

> [!note]- Hint 5
> Release *two* test particles, separated horizontally by a distance $d$. In B they drift inertially — parallel and constant velocity — so their separation remains exactly $d$ forever. In A (a real planetary field), each particle falls toward the planet's centre, not "straight down" in the same direction; their trajectories *converge*. The relative acceleration is the tidal effect: $\Delta a \sim (GM/r^3)\,d$, the gradient of the field. This effect *cannot* be reproduced by any uniform acceleration of the cabin, because in B the field is exactly uniform — by construction. Tidal forces are the boundary of the equivalence principle, and their geometric name is *curvature*.

---

# Solution

The Einstein elevator is the original carrier of the equivalence principle: it allows Einstein (and the reader) to derive the gravitational redshift and the bending of light with no field equation, no metric calculation, no detailed theory — just by substituting "accelerated cabin" for "gravity" and computing in flat Minkowski space. The price is that the substitution is only valid *locally*, and the part of gravity that cannot be transformed away — tidal forces — is left over as the seed of curvature.

**Step 1: A released particle falls identically in A and B.**

> [!note]- Derivation
> *In B:* the cabin has proper acceleration $\vec a = g\,\vec e_x$, the particle released at rest in the cabin centre is inertial. In the global inertial frame the particle moves with constant velocity (zero, after the release); the cabin accelerates upward at $g$. So relative to the cabin floor the particle accelerates downward: $\vec a_{\mathrm{rel}} = -g\,\vec e_x$.
>
> *In A:* the particle, of inertial mass $m_I$ and gravitational mass $m_G$, experiences a gravitational force $\vec F = -m_G g\,\vec e_x$, hence Newtonian acceleration $\vec a = -(m_G/m_I) g\,\vec e_x$. The equivalence principle is precisely $m_G = m_I$, so $\vec a = -g\,\vec e_x$ — the same as in B.
>
> The two relative motions are identical, and crucially they are identical *for every particle*, because the equality $m_G = m_I$ is universal (Eötvös, $10^{-8}$; modern, $3\times 10^{-13}$). A feather and a hammer fall identically in A as in B. By measurements of relative motion of test particles, the physicist cannot tell A from B. $\checkmark$

**Step 2: An accelerometer reads $g$ in both situations.**

> [!note]- Derivation
> An accelerometer is essentially a small test mass suspended by a spring inside a housing. The reading is the proper acceleration of the housing — the deviation of the housing's worldline from inertial.
>
> *In B:* the housing (bolted to the cabin floor) has proper acceleration $g$ upward; the suspended test mass tends to lag, stretching the spring "downward" with reading $g$.
>
> *In A:* the housing sits at rest on the planet's surface, but is held against the gravitational pull by the normal force from the planet — its worldline is *not* inertial. The proper acceleration of a static observer in the field $\vec g = -g\,\vec e_x$ is $\vec a = +g\,\vec e_x$ (upward). The suspended test mass tends to fall inside the housing; the spring stretches "downward" with reading $g$.
>
> The accelerometer cannot tell A from B. $\checkmark$ The deeper point: a static observer in a gravitational field is *not* inertial — only a freely-falling observer is. This is the precise content of "gravity is what you feel when you resist free fall".

**Step 3: A horizontal laser beam falls in B, hence in A — light bending.**

> [!note]- Derivation
> *In B:* fire a horizontal light pulse from the wall at $x = 0$ aimed at the opposite wall at $x = L$. In the global inertial frame the pulse travels in a straight line at speed $c$, reaching the far wall after time $L/c$ (treating $L/c$ as small, so the cabin's speed remains nonrelativistic during the transit). During this time the cabin has moved upward by
> $$\Delta y = \frac{1}{2}g\left(\frac{L}{c}\right)^2 = \frac{gL^2}{2c^2}.$$
> Therefore, in the cabin frame, the pulse strikes the far wall at height $-\Delta y$ relative to the emission point: the beam "falls" along a parabolic arc of curvature $g/c^2$.
>
> *In A:* by the equivalence principle, the same trajectory must be observed in a uniform gravitational field of magnitude $g$. Light "falls" with the same coordinate acceleration $g$, deflecting downward by $g L^2/(2c^2)$ over a horizontal distance $L$, an angular deflection per unit length of $g/c^2$.
>
> Even with no field equation, the equivalence principle predicts the *existence* of gravitational light bending and gives the correct order of magnitude in a locally uniform field. For the Sun's grazing ray ($L \sim R_\odot$, $g \sim GM_\odot/R_\odot^2$) this argument gives $\delta\theta \sim 2GM_\odot/(c^2 R_\odot) = 0.87''$ — the Newtonian / equivalence-principle estimate, half the measured value. The missing factor of two is the *spatial* curvature of the Schwarzschild metric, beyond what the uniform-field argument can see; see [[Thm - Light Deflection]] and Illegal Operation 3 of the topic page.

**Step 4: A clock at the ceiling runs faster than one on the floor — gravitational redshift.**

> [!note]- Derivation
> *In B:* the ceiling emitter, at height $h$ above the floor, emits light pulses at proper period $\Delta t_{\mathrm{em}}$. The light takes transit time $h/c$ to reach the floor. During the transit the cabin (rigidly accelerating at $g$ upward) gains velocity $\Delta v = g\,(h/c) = gh/c$ in the direction of light propagation — but wait, the floor receiver is moving *toward* the oncoming light (which travels downward), gaining velocity $\Delta v$ in the direction of approach. So the receiver sees a *blueshift*: $\nu_{\mathrm{rec}}/\nu_{\mathrm{em}} = 1 + \Delta v/c = 1 + gh/c^2$, with received period $\Delta t_{\mathrm{rec}} = \Delta t_{\mathrm{em}}/(1 + gh/c^2)$.
>
> Conversely, a floor-to-ceiling pulse encounters a ceiling that has accelerated *away*, a redshift: $\nu_{\mathrm{rec}}/\nu_{\mathrm{em}} = 1 - gh/c^2$.
>
> *In A:* by the equivalence principle, the same shifts must occur in the gravitational field. Light climbing the potential is redshifted, light descending is blueshifted. The clock-rate consequence: ceiling-frequency $>$ floor-frequency means the ceiling clock *ticks faster* than the floor clock by the factor $1 + gh/c^2 = 1 + \Delta\Phi/c^2$.
>
> This is the gravitational redshift of [[Thm - Gravitational Redshift]], derived from one accelerated-frame Doppler computation and the equivalence principle. The Pound-Rebka tower test of 1960 measured exactly this shift over $h = 22.5\,\mathrm{m}$ — fractional shift $2.5\times 10^{-15}$, agreement with the prediction to $1\%$.

**Step 5: Tidal forces distinguish A from B — the boundary of the equivalence principle.**

> [!note]- Derivation
> Release *two* test particles, separated by a horizontal distance $d$ in the cabin, simultaneously and at rest.
>
> *In B:* both particles are inertial; their worldlines are parallel straight lines in the global frame. Their horizontal separation in the cabin frame remains exactly $d$ forever.
>
> *In A:* both particles fall toward the planet's centre, not "straight down" in the same direction. If the planet is at depth $R$ below the cabin, each particle's gravitational acceleration is directed along the line from particle to centre. The two lines converge — the angle between them is $d/R$ — and the relative inward acceleration is
> $$\Delta a \approx g \cdot \frac{d}{R} = \frac{GM}{R^2}\cdot\frac{d}{R} = \frac{GM\,d}{R^3}.$$
> The particles drift toward each other at this acceleration: a *tidal* effect. No uniform acceleration of the cabin can reproduce this — by construction situation B has *exactly uniform* equivalent gravity, so any two particles released in B remain exactly parallel.
>
> The physicist detects the tidal effect and concludes she is in a real gravitational field, not an accelerated cabin in empty space. *The tidal field is the part of gravity that the equivalence principle cannot transform away.* Its size is the gradient of the field — proportional to the *second* spatial derivative of the potential — and its geometric encoding in general relativity is the **Riemann curvature tensor**. The equivalence principle removes gravity at a point; what is left is the curvature, and curvature *is* the gravitational field in the geometric sense.
>
> This is the cleanest physical statement of the boundary of the equivalence principle and the reason general relativity needs curvature: a *uniform* gravitational field is locally indistinguishable from acceleration (and so can be transformed away), but a *real* gravitational field is never uniform over any extended region, and the residual inhomogeneity is genuine geometry.

> [!note]- Complete formal solution
> The equivalence principle is the indistinguishability of situations A (cabin in field $-g\hat e_x$) and B (cabin accelerating at $+g\hat e_x$ in empty space) by any *local* measurement. (1) A released particle falls identically because $m_G = m_I$ in A gives Newtonian acceleration $-g\hat e_x$, while in B the inertial particle accelerates at $-g\hat e_x$ relative to the cabin floor — identical motion for every test body (universality of free fall). (2) The accelerometer reads $g$ in both: its housing has proper acceleration $g$ upward in both A (static observer in field, non-inertial) and B (rigidly accelerating cabin). (3) Horizontal light fired across the cabin: in B the cabin moves up by $gL^2/(2c^2)$ during the transit time $L/c$, so the pulse strikes the far wall below its initial height — light "falls" at $g/c^2$ per unit length, and by the equivalence principle the same happens in A; for the Sun grazing this gives $0.87''$, half the GR value. (4) A ceiling clock runs faster than a floor clock: in B the floor moves toward downward pulses (blueshift) and away from upward pulses (redshift), giving $\nu_{\mathrm{ceiling}}/\nu_{\mathrm{floor}} = 1 + gh/c^2$, hence by equivalence in A the gravitational redshift $\Delta\nu/\nu = -\Delta\Phi/c^2$. (5) Release two horizontally separated particles: in B they remain parallel, in A they converge with relative acceleration $\sim GMd/R^3$ — a *tidal* effect. Tides cannot be transformed away by any acceleration and are the geometric residue of a real gravitational field, encoded in general relativity by the Riemann curvature tensor. The thought experiment thus simultaneously establishes the equivalence principle (parts 1–4) and locates its boundary (part 5). $\blacksquare$

---

# Key Takeaways

**The equivalence principle is not a metaphysical claim about the equivalence of gravity and acceleration — it is a constructive *substitution rule*.** What the elevator demonstrates is purely operational: when computing a *local* effect in a uniform gravitational field, swap "gravity" for "accelerated frame", do the entire computation in flat Minkowski space using only special-relativistic kinematics, and the answer is correct. This is the trick that gave Einstein the redshift in 1907 with no field equation and the light deflection in 1911 long before general relativity existed. The recurring move — replace the field by the acceleration $\vec a = -\vec g$ and compute — is by far the highest-leverage operation in this chapter, and it is what makes the redshift, the light deflection, the GPS correction, and Schild's argument all reduce to accelerated-observer kinematics. Recognise its applicability the instant you see a *local* measurement in a *uniform-enough* gravitational field; the substitution is exact in that regime.

**The equivalence principle is *local*, and its boundary is the tidal field — which is curvature.** The single most important caveat the elevator experiment carries is that the indistinguishability of A and B holds only over a region small enough that the real gravitational field is uniform. Any region large enough for the field's *gradient* to matter detects the inhomogeneity — two test particles fall along converging lines toward a common centre, no single acceleration of the lab can reproduce that convergence, and the lab knows it sits in a real field. This residual relative acceleration of nearby freely-falling worldlines is the *tidal* effect, geometrically encoded as the Riemann curvature tensor and dynamically described by the geodesic deviation equation. The boundary it traces is sharp: the equivalence principle removes the field at one point and to first order around it; what remains is curvature, and curvature *is* the gravitational field once one accepts the geometric viewpoint. This is the cleanest statement of why general relativity needs a curved spacetime: a *uniform* field can be transformed away and is therefore not really geometry, but a *real* field has irreducible inhomogeneity and must be encoded in the second derivatives of a position-dependent metric.

**A "static observer in a gravitational field" is not an inertial observer — it has proper acceleration, and that is why it feels weight.** The most counterintuitive consequence of the equivalence principle is the inversion of what counts as inertial. In Newtonian physics, an observer standing on Earth's surface is "at rest" and therefore inertial; an observer in free fall is "accelerating downward" and therefore non-inertial. The equivalence principle reverses both judgements: the freely-falling observer has *zero* proper acceleration (locally indistinguishable from a Minkowski inertial observer, weightless, an accelerometer reads zero) and the standing observer has proper acceleration $g$ *upward* (the normal force from the ground), because she is being *prevented from falling*. This is why she feels weight, why her accelerometer reads $g$, and why she is non-inertial in the relativistic sense. The reusable lesson is that "feeling gravity" is the same physical phenomenon as "being in a non-inertial frame", and free fall is the only way to occupy a locally inertial frame in a gravitational field — exactly the setting that becomes the local Lorentz frame of general relativity.
