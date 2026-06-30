---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Invariance of the Velocity of Light"
  - "Def - Photon Propagation Direction and Velocity"
  - "Thm - Length Contraction"
tags: [physics, special-relativity]
---

# Problem Statement

The Michelson–Morley experiment (1887) used an interferometer with two perpendicular arms of equal length $L$. A light beam is split, each half makes a round trip along one arm and back, and the two halves are recombined; the interference fringes record the difference in round-trip times. The apparatus could be rotated by $90^\circ$ about a vertical axis. Working with the speed of light $c$ restored:

1. **Aether prediction.** Assume the classical (pre-relativistic) picture: light travels at $c$ relative to a stationary aether, and the laboratory moves through the aether at speed $V$ along arm 1. Using Galilean velocity addition, compute the round-trip time along arm 1 (parallel to $V$) and along arm 2 (perpendicular to $V$), and find the time difference $\Delta t$ to leading order in $V^2/c^2$.
2. Show that rotating the apparatus by $90^\circ$ swaps the roles of the arms and reverses the sign of $\Delta t$, so the *change* in $\Delta t$ on rotation is $2\Delta t \approx \frac{L V^2}{c^3}$ (in time), producing a predicted fringe shift.
3. **The result.** Michelson and Morley observed *no* fringe shift on rotation. Using [[Thm - Invariance of the Velocity of Light|the invariance of the velocity of light]], explain why relativity predicts exactly zero shift: what does the experiment establish about the dependence of the speed of light on the *direction* of the observer's motion?
4. **The pre-relativistic patch.** FitzGerald and Lorentz proposed that arm 1 (along $V$) is physically *contracted* by the factor $\Gamma^{-1} = \sqrt{1 - V^2/c^2}$. Show that this contraction makes the aether-model time difference vanish, "explaining" the null result without abandoning the aether — and explain why relativity makes this contraction automatic rather than ad hoc.

**Recall:**

The exercise rests on the invariance of light and (for the patch) length contraction.

![[Thm - Invariance of the Velocity of Light#Statement]]

In the aether model, the speed of light relative to the moving laboratory is direction-dependent: $c - V$ chasing the beam, $c + V$ returning, $\sqrt{c^2 - V^2}$ transverse — the Galilean composition of the aether-frame speed $c$ with the lab velocity $V$. Relativity ([[Def - Photon Propagation Direction and Velocity]]) replaces this with the observer-independent $\|\mathbf V_{\mathrm{light}}\| = c$. The FitzGerald–Lorentz patch invokes [[Thm - Length Contraction|length contraction]] of the parallel arm.

---

# Convergent Strategy

**Problem class.** A *predict-and-confront-an-experiment* problem of the chapter's [[Special Relativity VII — Kinematics I, Motion Relative to an Observer#Problem-Solving Strategy|fourth strategy]]: compute the prediction of a *test theory* (the aether model with a free parameter $V$) and confront it with the null result, isolating which aspect of the constancy of light the experiment establishes — here, isotropy (direction-independence).

**Assumption pattern.** Two perpendicular light paths are compared as the apparatus moves — the signal that the experiment tests the *directional* dependence of the speed of light. The aether model supplies a definite, falsifiable prediction (a fringe shift on rotation); the null result falsifies it. The phrase "rotating swaps the arms" is the key to extracting an observable (the *change* in $\Delta t$) that does not require knowing the absolute path lengths.

**Theorem routing.** Parts 1–2 are a Galilean (aether-model) computation of round-trip times and the rotation-induced fringe shift — the prediction to be tested. Part 3 invokes [[Thm - Invariance of the Velocity of Light]]: since $\|\mathbf V_{\mathrm{light}}\| = c$ in every direction for the moving lab, both arms have identical round-trip times, $\Delta t = 0$, independent of orientation — zero shift. Part 4 shows the FitzGerald–Lorentz [[Thm - Length Contraction|length contraction]] of the parallel arm cancels the aether prediction, and explains why relativity makes it automatic.

**Key decision point.** The crux is recognising what the *null result* establishes: not that the speed of light is constant outright, but specifically that it is independent of the *direction* of the observer's motion (isotropy). The natural error is to claim Michelson–Morley proves the full constancy postulate; in fact it tests only the directional half, and the magnitude half requires the separate Kennedy–Thorndike experiment. Identifying this limitation precisely is the conceptual payoff.

---

# Legal Operations Used

1. **Adapt the velocity of light to the observer** (operation 8 from the topic page, applied to the lab observer). In the aether model the lab measures a direction-dependent light speed; relativity gives $\|\mathbf V_{\mathrm{light}}\| = c$ in all directions.

2. **Specialise to the simplest case** (operation 7). The relativistic prediction is immediate: $\|\mathbf V_{\mathrm{light}}\| = c$ for the lab observer (local measurement, $\overrightarrow{OM} = 0$), so both arms have equal round-trip times.

3. **Use length contraction** (from [[Thm - Length Contraction|length contraction]]). The FitzGerald–Lorentz patch contracts the parallel arm by $\Gamma^{-1}$ to cancel the aether-model time difference.

4. **Confront a test-theory prediction with a null result** (the chapter's experimental-routing pattern). The aether model's free parameter $V$ predicts a fringe shift; the null result bounds the directional anisotropy of $c$.

---

# Hints

> [!note]- Hint 1
> Arm 1 (along $V$): chasing the beam, the light's lab-frame speed is $c - V$; returning, $c + V$. Round-trip time $t_\parallel = \frac{L}{c-V} + \frac{L}{c+V} = \frac{2Lc}{c^2 - V^2} = \frac{2L/c}{1 - V^2/c^2}$. Arm 2 (transverse): the light's speed across is $\sqrt{c^2 - V^2}$, round-trip $t_\perp = \frac{2L}{\sqrt{c^2 - V^2}} = \frac{2L/c}{\sqrt{1 - V^2/c^2}}$.

> [!note]- Hint 2
> Expand to leading order: $t_\parallel \approx \frac{2L}{c}(1 + V^2/c^2)$, $t_\perp \approx \frac{2L}{c}(1 + \frac12 V^2/c^2)$, so $\Delta t = t_\parallel - t_\perp \approx \frac{L V^2}{c^3}$. Rotating by $90^\circ$ exchanges parallel and transverse, sending $\Delta t \to -\Delta t$, so the observable *change* is $2\Delta t \approx \frac{2LV^2}{c^3}$ — a definite predicted fringe shift.

> [!note]- Hint 3
> Relativity: the speed of light is $c$ for the lab observer in *every* direction (local measurement). So $t_\parallel = t_\perp = 2L/c$ regardless of orientation: $\Delta t = 0$, and rotating changes nothing. The experiment, finding zero shift, establishes that the speed of light does not depend on the *direction* of the lab's motion through any hypothetical aether — the isotropy of $c$.

> [!note]- Hint 4
> If arm 1 is contracted to $L/\Gamma = L\sqrt{1-V^2/c^2}$, then $t_\parallel = \frac{2(L/\Gamma)/c}{1-V^2/c^2} = \frac{2L/c}{\sqrt{1-V^2/c^2}} = t_\perp$, so $\Delta t = 0$. The contraction exactly cancels. In relativity this contraction is not a mechanical effect of the aether on the arm but a property of spacetime geometry — automatic, not imposed.

---

# Solution

The route is to compute the aether-model fringe shift (the prediction), extract the rotation observable, then show relativity predicts zero shift because light travels at $c$ in every direction, and finally interpret the FitzGerald–Lorentz contraction patch. Step 1 gives the round-trip times; Step 2 the rotation-induced shift; Step 3 the relativistic null prediction and what it establishes; Step 4 the contraction patch and why relativity makes it natural. The non-obvious thread is that the experiment tests *isotropy* of $c$ specifically — the directional, not the magnitude, dependence.

**Step 1: The aether model predicts $t_\parallel = \frac{2L/c}{1 - V^2/c^2}$ and $t_\perp = \frac{2L/c}{\sqrt{1 - V^2/c^2}}$, differing at order $V^2/c^2$.**

> [!note]- Derivation
> In the aether model, light moves at $c$ relative to the aether, and the lab moves through the aether at $V$ along arm 1.
>
> *Arm 1 (parallel to $V$).* Going out, the beam chases the receding far mirror, so its speed relative to the lab is $c - V$ (Galilean composition), taking time $L/(c-V)$. Returning, the beam meets the approaching near mirror at relative speed $c + V$, taking $L/(c+V)$. Total:
> $$t_\parallel = \frac{L}{c-V} + \frac{L}{c+V} = \frac{L(c+V) + L(c-V)}{(c-V)(c+V)} = \frac{2Lc}{c^2 - V^2} = \frac{2L}{c}\cdot\frac{1}{1 - V^2/c^2}.$$
>
> *Arm 2 (perpendicular to $V$).* To return to the moving beam-splitter, the light must travel at an angle into the aether wind; its speed *across* (the component reaching the far mirror and back) is $\sqrt{c^2 - V^2}$ by Pythagoras. Round-trip:
> $$t_\perp = \frac{2L}{\sqrt{c^2 - V^2}} = \frac{2L}{c}\cdot\frac{1}{\sqrt{1 - V^2/c^2}}.$$
> The two round-trip times differ: the parallel arm has the full factor $(1-V^2/c^2)^{-1}$, the transverse arm only its square root.

**Step 2: Rotating by $90^\circ$ reverses $\Delta t$, predicting a fringe shift $\propto LV^2/c^3$.**

> [!note]- Derivation
> Expand both times to leading order in $V^2/c^2$:
> $$t_\parallel \approx \frac{2L}{c}\Big(1 + \frac{V^2}{c^2}\Big),\qquad t_\perp \approx \frac{2L}{c}\Big(1 + \frac{1}{2}\frac{V^2}{c^2}\Big).$$
> The time difference is
> $$\Delta t = t_\parallel - t_\perp \approx \frac{2L}{c}\Big(\frac{V^2}{c^2} - \frac{1}{2}\frac{V^2}{c^2}\Big) = \frac{L V^2}{c^3}.$$
> Now rotate the apparatus by $90^\circ$. This exchanges the two arms: arm 2 becomes parallel to $V$ and arm 1 becomes transverse, so the new difference is $-\Delta t$. The *observable change* on rotation — the quantity the fringe pattern actually registers, since the absolute path lengths are not known to optical precision — is
> $$\delta(\Delta t) = \Delta t - (-\Delta t) = 2\Delta t \approx \frac{2L V^2}{c^3}.$$
> For Michelson and Morley's apparatus ($L \sim 11\,\mathrm{m}$ of folded path, $V \sim 30\,\mathrm{km\,s^{-1}}$ the Earth's orbital speed), this predicted a fringe shift of about $0.4$ fringes — well within their resolution. The aether model makes a definite, measurable prediction.

**Step 3: Relativity predicts exactly zero shift; the null result establishes the isotropy of $c$.**

> [!note]- Derivation
> By [[Thm - Invariance of the Velocity of Light|the invariance of the velocity of light]], an observer measures the speed of light to be $c$ at a point of their own worldline, *regardless of direction* — the propagation direction $N$ is always a unit vector, so $\|\mathbf V_{\mathrm{light}}\| = c$ along every arm. The light measurement at the beam-splitter is local ($\overrightarrow{OM} = 0$), so the qualification on the theorem is met. Therefore both round-trip times are simply
> $$t_\parallel = t_\perp = \frac{2L}{c},$$
> identical, with *no* dependence on the lab's velocity $V$ or on the arm's orientation. The time difference is
> $$\Delta t = 0,$$
> and rotating the apparatus changes nothing: $\delta(\Delta t) = 0$. Relativity predicts exactly zero fringe shift, which is what Michelson and Morley observed.
>
> What the null result *establishes* is precise: the speed of light does not depend on the *direction* of the observer's motion through any hypothetical aether — the **isotropy** of the speed of light. The experiment compares two *directions* (parallel and perpendicular to $V$) and finds no difference, so it rules out any directional dependence. It does *not*, by itself, establish that the speed is independent of the *magnitude* of the lab's velocity — that is a separate question, because Michelson–Morley measures only the *difference* between two directions at a single speed $V$, and a magnitude-dependence that affected both arms equally would cancel in the difference. The magnitude-independence requires the Kennedy–Thorndike experiment ([[Ex - Kennedy-Thorndike and the speed independent of observer speed]]).

**Step 4: The FitzGerald–Lorentz contraction cancels the aether prediction; relativity makes it automatic.**

> [!note]- Derivation
> FitzGerald and Lorentz proposed, *within* the aether theory, that a body moving through the aether at speed $V$ is physically contracted along its direction of motion by the factor $\Gamma^{-1} = \sqrt{1 - V^2/c^2}$ — the cohesion forces holding the arm together, being electromagnetic, are modified by the motion. If arm 1 (parallel to $V$) is contracted to length $L' = L/\Gamma = L\sqrt{1 - V^2/c^2}$, its round-trip time becomes
> $$t_\parallel = \frac{2L'/c}{1 - V^2/c^2} = \frac{2L\sqrt{1-V^2/c^2}/c}{1 - V^2/c^2} = \frac{2L/c}{\sqrt{1 - V^2/c^2}} = t_\perp.$$
> The contraction exactly cancels the parallel arm's extra factor, making $\Delta t = 0$ — the null result is "explained" without abandoning the aether. This is the historical patch (1889–1892) that saved the aether for a decade.
>
> The decisive difference is *why* the contraction occurs. In the FitzGerald–Lorentz theory it is a dynamical effect: a real physical compression caused by motion through a real aether, contrived to match the experiment. In relativity, [[Thm - Length Contraction|length contraction]] is a *kinematic* consequence of the geometry of spacetime — a moving rod is short because of the relativity of simultaneity, with no aether and no force, and it follows from the same postulates that give the constancy of light. So relativity predicts the contraction *automatically* and *for free*, as a theorem rather than an ad hoc hypothesis, and it predicts the null result directly (Step 3) without ever invoking the contraction at all. The FitzGerald–Lorentz contraction is what the aether theory had to *assume*; relativity *derives* it. This is the methodological superiority that, together with the elimination of the unobservable aether, made special relativity supersede the patched aether model.

> [!note]- Complete formal solution
> In the aether model the lab, moving at $V$ through the aether along arm 1, sees the round-trip times $t_\parallel = \frac{2L/c}{1 - V^2/c^2}$ (Galilean speeds $c\mp V$) and $t_\perp = \frac{2L/c}{\sqrt{1-V^2/c^2}}$ (transverse speed $\sqrt{c^2 - V^2}$), differing by $\Delta t \approx LV^2/c^3$ to leading order. Rotating $90^\circ$ swaps the arms, sending $\Delta t \to -\Delta t$, so the predicted fringe-shift observable is $2\Delta t \approx 2LV^2/c^3$ — about $0.4$ fringes for the actual apparatus. By [[Thm - Invariance of the Velocity of Light|the invariance of the velocity of light]], the lab measures $\|\mathbf V_{\mathrm{light}}\| = c$ in every direction (local measurement), so $t_\parallel = t_\perp = 2L/c$ and $\Delta t = 0$ regardless of orientation — exactly the observed null result. The null result establishes the *isotropy* of the speed of light (no dependence on the *direction* of the lab's motion), but not its magnitude-independence, which needs Kennedy–Thorndike. The FitzGerald–Lorentz patch — contracting arm 1 by $\Gamma^{-1}$ — cancels the aether prediction, but relativity makes this [[Thm - Length Contraction|length contraction]] an automatic kinematic theorem rather than an ad hoc dynamical hypothesis, and predicts the null result directly. $\blacksquare$

---

# Key Takeaways

**The Michelson–Morley experiment tests the *isotropy* of the speed of light — its independence from the *direction* of the observer's motion — and not the full constancy postulate.** This precision matters. The experiment compares two perpendicular directions at a single laboratory speed and finds no difference, which rules out any *directional* dependence of $c$ (any "aether wind" that would make light faster one way than another). But it says nothing about whether the speed depends on the *magnitude* of the observer's velocity, because a magnitude-dependence affecting both arms equally cancels in their difference. The full constancy of light — independence from both direction and magnitude — therefore requires two experiments: Michelson–Morley for the direction, Kennedy–Thorndike for the magnitude. The reusable lesson is that a null result bounds exactly the parameter the experiment is differential in, and stating *which* parameter is the discipline of interpreting null experiments. Relativity predicts the isotropy directly from $\|\mathbf V_{\mathrm{light}}\| = c$: the propagation direction is a unit vector whichever way the photon goes, so every arm has the same round-trip time.

**A null experiment is the falsification of a test theory's free parameter, and computing the prediction is the substance of the test.** Michelson–Morley is not "checking whether light is constant" in the abstract — it is computing what the *aether model* (a test theory with a free parameter $V$, the lab's speed through the aether) predicts, and finding the prediction false. The aether model gives a definite fringe shift $\propto LV^2/c^3$ on rotation; the null result sets this to zero, bounding the anisotropy of $c$. This is the anatomy of every precision test of relativity: embed the theory in a wider framework with adjustable parameters that are zero in relativity, compute the observable as a function of those parameters, and let the null measurement bound them. Modern versions (optical-cavity experiments) bound the anisotropy parameters of the Standard Model Extension to better than $10^{-17}$. The reusable principle is that "confirming relativity" means *bounding the parameters of its competitors* — and the more carefully you compute the competitor's prediction, the tighter the bound the null result yields.

**The FitzGerald–Lorentz contraction shows the difference between an ad hoc patch and a derived theorem — and why relativity superseded the aether.** Faced with the null result, the aether theory could be saved by *assuming* that moving bodies contract by exactly $\Gamma^{-1}$ along their motion — a dynamical hypothesis, contrived to cancel the predicted shift, with the contraction caused by the aether's effect on the body's cohesion forces. Relativity *derives* the identical [[Thm - Length Contraction|length contraction]] as a kinematic consequence of spacetime geometry and the relativity of simultaneity, with no aether and no force, from the same postulates that give the constancy of light — and it predicts the null result directly, without even invoking the contraction. The methodological lesson, which is general, is that a theory that *derives* an effect from its core principles is superior to one that must *assume* the effect to match data: the former makes a prediction, the latter accommodates an observation. Special relativity replaced the patched aether not because the patch was wrong (it gave the right contraction) but because relativity made the patch unnecessary and the aether unobservable, deriving as theorems what the aether theory had to postulate. The companion magnitude-independence test is [[Ex - Kennedy-Thorndike and the speed independent of observer speed]]; the first historical relativistic null result is [[Ex - Arago and the first relativistic null result]].
