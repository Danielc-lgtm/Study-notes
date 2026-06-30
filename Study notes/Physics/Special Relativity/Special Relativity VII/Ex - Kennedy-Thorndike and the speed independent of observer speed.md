---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Invariance of the Velocity of Light"
  - "Def - Photon Propagation Direction and Velocity"
  - "Thm - Time Dilation (General Observer)"
tags: [physics, special-relativity]
---

# Problem Statement

The Kennedy–Thorndike experiment (1932) was designed to test the half of the constancy of light that Michelson–Morley leaves open. It differs from Michelson–Morley in three ways: (i) the interferometer arms have *unequal* lengths $L_1 \neq L_2$; (ii) the apparatus is held *fixed* in the laboratory (no rotation); (iii) the fringes are monitored over a *long* period, several months. Working with $c$ restored:

1. Explain why Michelson–Morley, comparing two directions at a single instant, cannot detect a dependence of the speed of light on the *magnitude* of the observer's velocity, only on its direction.
2. In a test theory where the speed of light depends on the observer's speed $V$ through the aether — say $V_{\mathrm{light}} = c\,f(V)$ for some function $f$ with $f(0) = 1$ — show that the phase difference between the two unequal arms is proportional to $(L_1 - L_2)$ and depends on $V$. Why does the Earth's orbital motion make $V$ vary over the year?
3. **The result.** Kennedy and Thorndike observed no fringe drift over the months. Using [[Thm - Invariance of the Velocity of Light|the invariance of the velocity of light]], explain why relativity predicts exactly zero drift, and state precisely what the experiment establishes that Michelson–Morley does not.
4. Combine the two experiments: argue that Michelson–Morley (isotropy) plus Kennedy–Thorndike (magnitude-independence) together establish the *full* constancy of the speed of light — independence from both the direction and the magnitude of the observer's velocity.

**Recall:**

The exercise rests on the invariance of light and on the role of time dilation in a full analysis.

![[Thm - Invariance of the Velocity of Light#Statement]]

[[Def - Photon Propagation Direction and Velocity|The speed of light relative to an observer]] is $\|\mathbf V_{\mathrm{light}}\| = c$, independent of the observer's velocity. A full analysis of an interferometer at speed $V$ also invokes [[Thm - Time Dilation (General Observer)|time dilation]] of the laboratory clock; the combination of length contraction (Michelson–Morley) and time dilation (Kennedy–Thorndike) is what makes the speed of light come out independent of $V$ in a complete relativistic treatment.

---

# Convergent Strategy

**Problem class.** A *predict-and-confront-an-experiment* problem of the chapter's [[Special Relativity VII — Kinematics I, Motion Relative to an Observer#Problem-Solving Strategy|fourth strategy]], complementary to Michelson–Morley: where that experiment tests the directional dependence of $c$, this one tests the magnitude dependence, and the strategy is to isolate which free parameter of the test theory each experiment bounds.

**Assumption pattern.** Unequal arms and no rotation, monitored over months — the signal that the experiment is differential in the *magnitude* of $V$ (which the Earth's orbit varies seasonally) rather than its direction (which rotation would vary). The phase difference $\propto (L_1 - L_2)$ is the observable; equal arms ($L_1 = L_2$) would give zero difference and detect nothing, which is exactly why Michelson–Morley (equal arms) cannot see this effect.

**Theorem routing.** Part 1 contrasts the two experimental geometries, explaining why a directional comparison (Michelson–Morley) is blind to magnitude dependence. Part 2 computes, in a test theory with speed-dependent $V_{\mathrm{light}}$, the phase difference $\propto (L_1 - L_2)f(V)$ and notes the Earth's orbital speed varies $V$. Part 3 invokes [[Thm - Invariance of the Velocity of Light]]: $\|\mathbf V_{\mathrm{light}}\| = c$ independent of $V$, so no drift. Part 4 combines the two null results, using that the full relativistic analysis needs both [[Thm - Length Contraction|length contraction]] and [[Thm - Time Dilation (General Observer)|time dilation]].

**Key decision point.** The crux is recognising that *unequal arms* and *long monitoring* are precisely what make the experiment sensitive to magnitude-dependence: equal arms cancel any common (direction-independent) effect, and a single observation cannot see a seasonal variation. The natural error is to think Kennedy–Thorndike is just a worse Michelson–Morley; in fact it is a *different* test, complementary, probing the orthogonal free parameter, and only the two together pin down the full constancy postulate.

---

# Legal Operations Used

1. **Adapt the velocity of light to the observer** (operation 8 from the topic page). The lab observer measures $\|\mathbf V_{\mathrm{light}}\| = c$ independent of its speed $V$ through any aether.

2. **Confront a test-theory prediction with a null result** (the chapter's experimental-routing pattern). A test theory with speed-dependent $V_{\mathrm{light}} = cf(V)$ predicts a seasonal fringe drift; the null result bounds the magnitude-dependence.

3. **Use time dilation** (from [[Thm - Time Dilation (General Observer)|time dilation]]). A complete relativistic analysis of the moving interferometer combines length contraction (which Michelson–Morley needs) with time dilation (which Kennedy–Thorndike needs) to keep $V_{\mathrm{light}} = c$.

4. **Combine two complementary null results** (the chapter's structural-target pattern). Isotropy (Michelson–Morley) plus magnitude-independence (Kennedy–Thorndike) jointly establish full constancy.

---

# Hints

> [!note]- Hint 1
> Michelson–Morley measures the *difference* between two perpendicular arms. A speed-of-light dependence on the magnitude of $V$ (not its direction) would slow or speed *both* arms by the same factor, so it cancels in the difference. To see a magnitude effect you need something that does *not* cancel — an unequal-arm comparison, or a comparison over time as $V$ changes.

> [!note]- Hint 2
> With unequal arms, the round-trip times are $t_i = 2L_i f(V)^{-1}/c$ (schematically), and the phase difference $\propto t_1 - t_2 \propto (L_1 - L_2)$ times a function of $V$. The Earth's orbital velocity (about $30\,\mathrm{km\,s^{-1}}$) adds to or subtracts from the Sun's motion through any aether over a year, so the lab's speed $V$ through the aether varies seasonally — and so would the phase, if $f$ depended on $V$.

> [!note]- Hint 3
> Relativity: $\|\mathbf V_{\mathrm{light}}\| = c$ for the lab observer *independent of $V$* — the propagation direction is a unit vector whatever the lab's speed. So the round-trip times are $2L_i/c$, fixed, and the phase difference $\propto (L_1 - L_2)$ is constant in time: no drift as $V$ varies over the year. The null result establishes that the speed of light does not depend on the *magnitude* of the observer's velocity.

> [!note]- Hint 4
> Michelson–Morley: speed independent of *direction* (isotropy). Kennedy–Thorndike: speed independent of *magnitude*. A velocity is a magnitude plus a direction, so independence from both is independence from the velocity entirely — the full constancy postulate. In a complete relativistic derivation, length contraction handles the direction part and time dilation the magnitude part.

---

# Solution

The route is to explain Michelson–Morley's blind spot, show how unequal arms and seasonal monitoring expose the magnitude-dependence, invoke the invariance of light for the null prediction, and combine the two experiments into the full constancy postulate. Step 1 identifies the blind spot; Step 2 sets up the test-theory observable; Step 3 gives the relativistic null prediction and what it establishes; Step 4 combines the two results. The non-obvious thread is that the two experiments probe *orthogonal* free parameters — direction and magnitude — and only together pin down constancy.

**Step 1: Michelson–Morley, being a directional comparison, is blind to magnitude-dependence.**

> [!note]- Derivation
> Michelson–Morley measures the *difference* in round-trip time between two perpendicular arms, and detects a fringe shift only if that difference *changes* on rotation. Suppose the speed of light depended on the *magnitude* $V$ of the lab's velocity through some aether, but not on direction — say $V_{\mathrm{light}} = c\,f(V)$ for all directions equally. Then *both* arms would have their light speed scaled by the same factor $f(V)$, and the round-trip times would be
> $$t_1 = \frac{2L}{c f(V)},\qquad t_2 = \frac{2L}{c f(V)}\qquad(\text{equal arms}),$$
> identical, so $\Delta t = 0$ regardless of $f$. A common, direction-independent factor cancels in the difference of equal arms. Rotation does nothing either, since both arms are affected equally at any orientation. So Michelson–Morley, comparing two *directions*, is structurally incapable of detecting a dependence on the *magnitude* of $V$: that dependence affects both arms identically and cancels. To see it, one must break the symmetry between the arms (unequal lengths) and watch over time as $V$ changes.

**Step 2: Unequal arms give a phase difference $\propto (L_1 - L_2)$ depending on $V$, which the Earth's orbit varies.**

> [!note]- Derivation
> Make the arms *unequal*, $L_1 \neq L_2$, and suppose the test theory has a speed-of-light magnitude $V_{\mathrm{light}} = c\,f(V)$. The round-trip times are
> $$t_1 = \frac{2L_1}{c\,f(V)},\qquad t_2 = \frac{2L_2}{c\,f(V)},$$
> and the phase difference between the recombined beams is proportional to
> $$t_1 - t_2 = \frac{2(L_1 - L_2)}{c\,f(V)}.$$
> Now the common factor $f(V)^{-1}$ does *not* cancel — it multiplies the *nonzero* difference $(L_1 - L_2)$. So the phase difference depends on $V$ through $f(V)$, and it is proportional to the arm-length difference $L_1 - L_2$ (which is why the arms must be unequal; equal arms give zero and detect nothing). If $f$ varies with $V$, the phase drifts as $V$ changes.
>
> The Earth's velocity through any hypothetical aether is the (vector) sum of the Sun's motion through the aether and the Earth's orbital velocity around the Sun, about $30\,\mathrm{km\,s^{-1}}$. As the Earth orbits, its orbital velocity rotates, so its *speed* $V$ relative to the aether waxes and wanes over the year (maximal when the orbital motion aligns with the Sun's aether-motion, minimal when anti-aligned). Thus $V$ varies seasonally by up to $\sim 60\,\mathrm{km\,s^{-1}}$ over six months, and a speed-dependent $f(V)$ would produce a *seasonal drift* of the fringe pattern — which is why the apparatus must be monitored over months, not rotated over minutes.

**Step 3: Relativity predicts zero drift; the null result establishes magnitude-independence.**

> [!note]- Derivation
> By [[Thm - Invariance of the Velocity of Light|the invariance of the velocity of light]], the lab observer measures $\|\mathbf V_{\mathrm{light}}\| = c$ at its own location, *independent of the lab's speed $V$* — the propagation direction is a unit vector whatever the observer's four-velocity. In the test-theory language, this is $f(V) = 1$ for all $V$. The round-trip times are then
> $$t_1 = \frac{2L_1}{c},\qquad t_2 = \frac{2L_2}{c},$$
> fixed constants, and the phase difference $\propto (t_1 - t_2) = 2(L_1 - L_2)/c$ is *constant in time* — it does not drift as the Earth's orbital speed varies over the year. Relativity predicts exactly zero seasonal drift, which is what Kennedy and Thorndike observed (and modern versions confirm to extraordinary precision).
>
> What the null result establishes, that Michelson–Morley does not: the speed of light does not depend on the *magnitude* of the observer's velocity. Kennedy–Thorndike, by watching the unequal-arm phase as $V$ varies seasonally, tests precisely the magnitude-dependence that the directional comparison of Michelson–Morley cancels. It is the complementary half of the constancy postulate — and it is a genuinely independent test, requiring different apparatus (unequal arms, fixed orientation) and a different observable (seasonal drift rather than rotational shift).

**Step 4: Michelson–Morley plus Kennedy–Thorndike together give the full constancy of light.**

> [!note]- Derivation
> A velocity is specified by a *direction* and a *magnitude*. The constancy of the speed of light — that it is the same for every observer regardless of motion — means independence from the observer's velocity, hence independence from *both* its direction and its magnitude. The two experiments establish exactly these two halves:
> - **Michelson–Morley** compares two *directions* at fixed speed and finds no difference: the speed of light is independent of the *direction* of the observer's motion (isotropy).
> - **Kennedy–Thorndike** compares the phase at different *speeds* (over the year) and finds no drift: the speed of light is independent of the *magnitude* of the observer's velocity.
>
> Together, independence from direction *and* magnitude is independence from the velocity entirely — the full constancy postulate, now established experimentally rather than assumed. In a *complete relativistic derivation* of either experiment, both [[Thm - Length Contraction|length contraction]] and [[Thm - Time Dilation (General Observer)|time dilation]] are needed: length contraction of the moving arm handles the directional asymmetry (Michelson–Morley), while time dilation of the moving laboratory clock handles the magnitude (Kennedy–Thorndike). Historically this is significant: the FitzGerald–Lorentz length contraction alone explains Michelson–Morley but *not* Kennedy–Thorndike — to explain the second null result within an aether theory one must *also* assume time dilation, and once you have postulated both length contraction and time dilation with exactly the relativistic factors, you have effectively assumed the full Lorentz transformation. So Kennedy–Thorndike is the experiment that forces the *time-dilation* half of relativity, closing the loophole that a length-contraction-only aether theory left open, and the pair of experiments together is equivalent to confirming the complete Lorentz transformation.

> [!note]- Complete formal solution
> Michelson–Morley measures the *difference* between two perpendicular arms, so a speed-of-light dependence on the *magnitude* $V$ (affecting both arms equally) cancels and is invisible. Kennedy–Thorndike uses *unequal* arms, giving a phase difference $\propto (L_1 - L_2)/f(V)$ in a test theory with $V_{\mathrm{light}} = cf(V)$; the nonzero $(L_1 - L_2)$ prevents cancellation, and the Earth's orbital motion varies $V$ seasonally, so a speed-dependent $f$ would drift the fringes over months. By [[Thm - Invariance of the Velocity of Light|the invariance of the velocity of light]], $\|\mathbf V_{\mathrm{light}}\| = c$ independent of $V$ (i.e. $f \equiv 1$), so the round-trip times $2L_i/c$ are fixed and the phase is constant — no seasonal drift, as observed. This establishes magnitude-independence, the half Michelson–Morley (isotropy) leaves open. Together the two null results give independence from both direction and magnitude — the full constancy of light — and in a complete relativistic analysis [[Thm - Length Contraction|length contraction]] handles the directional part while [[Thm - Time Dilation (General Observer)|time dilation]] handles the magnitude, so Kennedy–Thorndike is the experiment that forces the time-dilation half of the Lorentz transformation. $\blacksquare$

---

# Key Takeaways

**Two complementary null experiments probe orthogonal parameters — direction and magnitude — and only together establish the full constancy of light.** The decomposition is clean and worth internalising: a velocity is a direction plus a magnitude, the constancy of light is independence from the velocity, and the two are tested separately. Michelson–Morley compares two *directions* (perpendicular arms) at a fixed speed and bounds the *directional* dependence (isotropy); Kennedy–Thorndike compares the phase at different *speeds* (the Earth's varying orbital velocity) with *unequal* arms and bounds the *magnitude* dependence. Neither alone suffices — Michelson–Morley is blind to a common factor affecting both arms, Kennedy–Thorndike does not compare directions — but together they pin down independence from the velocity entirely. The reusable principle is that when a quantity (a velocity) has independent components (direction, magnitude), a complete null test of "independence from that quantity" requires experiments differential in *each* component, and identifying which experiment probes which component is the substance of the analysis.

**Unequal arms and long monitoring are not refinements of Michelson–Morley but the specific design that exposes magnitude-dependence.** Each feature of Kennedy–Thorndike is dictated by what it must detect. *Unequal* arms ($L_1 \neq L_2$): a magnitude-dependent speed scales both arms equally, cancelling in the difference of equal arms, so the arms must differ for the effect to survive in the phase $\propto (L_1 - L_2)$. *No rotation*: rotation tests direction, which is Michelson–Morley's job, not this one's. *Long monitoring*: the magnitude of the lab's velocity through any aether varies *seasonally* with the Earth's orbit, so the effect appears as a slow drift over months, not a fast shift over a rotation. The reusable lesson is that experimental design is reverse-engineered from the observable: to detect a dependence on parameter $X$, build an apparatus whose signal does *not* cancel under variation of $X$ and arrange for $X$ to vary in a controlled, measurable way. The seasonal variation of the Earth's velocity is the "knob" that turns $V$, and unequal arms are the configuration whose phase responds to it.

**Kennedy–Thorndike forces the time-dilation half of relativity, closing the loophole a length-contraction-only aether theory left open.** This is the deep historical and structural point. The FitzGerald–Lorentz [[Thm - Length Contraction|length contraction]] alone explains the Michelson–Morley null result (the parallel arm contracts to cancel the aether effect), and for a decade this saved the aether. But length contraction alone does *not* explain Kennedy–Thorndike: to make the unequal-arm phase independent of the lab's speed, one must *also* invoke [[Thm - Time Dilation (General Observer)|time dilation]] of the laboratory clock, with exactly the relativistic factor. Once an aether theory has assumed both length contraction and time dilation with the Lorentz factors, it has effectively assumed the entire Lorentz transformation — at which point it is observationally indistinguishable from relativity, and the unobservable aether is excess baggage. So Kennedy–Thorndike is the experiment that demands the *time* part of spacetime geometry, complementing Michelson–Morley's demand for the *space* (contraction) part, and the pair together is equivalent to confirming the full Lorentz transformation. The reusable insight is that a sequence of null experiments can incrementally force the components of a theory — space contraction, then time dilation — until the only consistent description is the complete one, and relativity's advantage is deriving all of it from two postulates while the aether theory must assume each piece. The companion directional test is [[Ex - Michelson-Morley null result]]; the first historical relativistic null result is [[Ex - Arago and the first relativistic null result]].
