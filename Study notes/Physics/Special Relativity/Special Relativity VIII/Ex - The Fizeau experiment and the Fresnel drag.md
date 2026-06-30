---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Law of Velocity Composition"
  - "Thm - Relativistic Velocity Addition"
tags: [physics, special-relativity]
---

# Problem Statement

Light propagates through water (refractive index $n \approx 1.33$) that is itself flowing at speed $V$ relative to the laboratory. A light beam travels through the water, co-moving with the flow in one branch of a U-tube and counter-moving in the other (the Fizeau apparatus). Working with $c = 1$ except where restoring $c$ aids recognition:

1. Using the collinear velocity-composition law, find the speed $c_1$ of the co-moving beam relative to the laboratory, exactly, and then expand to first order in $V$ (taking $V \ll 1$).
2. Show that to first order the result has the form $c_1 = c/n + \alpha V$ (and the counter-moving beam $c_2 = c/n - \alpha V$), and identify the **Fresnel drag coefficient** $\alpha$.
3. The two beams travel a length $\ell$ of tube in opposite senses relative to the water and are recombined to interfere. Show the phase difference is $\Delta\phi = 8\pi n^2 (\ell/\lambda)(V/c)\,\alpha$, where $\lambda$ is the vacuum wavelength.
4. Explain why this 1850 experiment, performed half a century before relativity, is correctly read today as a confirmation of the relativistic velocity-composition law rather than of any "aether drag".

**Recall:**

The exercise rests entirely on the collinear law of velocity composition.

![[Thm - Law of Velocity Composition#Statement]]

The speed of light in a medium at rest is $c/n$ (with $c = 1$, just $1/n$), where $n$ is the [refractive index]. This is the velocity of the beam *relative to the water*; the water moves at $V$ relative to the lab, and the lab speed of the beam is the composition of these two collinear velocities. The composition is the relativistic correction to the Galilean expectation $1/n \pm V$.

---

# Convergent Strategy

**Problem class.** A *transform-a-velocity* problem of the simplest kind: a speed is given relative to a moving medium, and we want it relative to the lab. The [[Special Relativity VIII — Kinematics II, Change of Observer#Problem-Solving Strategy|topic strategy]] says: recognise the medium as a moving observer, identify the velocities as collinear, and apply the addition law, then expand to the order the experiment probes.

**Assumption pattern.** Two collinear velocities — the beam's $1/n$ relative to the water and the water's $V$ relative to the lab — and the smallness $V \ll 1$. The smallness is the signpost that the *first-order* expansion is what the experiment measures, so the exact formula must be Taylor-expanded; the leading correction to the naive sum is the physics.

**Theorem routing.** The collinear [[Thm - Law of Velocity Composition|velocity-composition]] law $V' = (V_1 + V_2)/(1 + V_1 V_2)$ (here in addition form, the [[Thm - Relativistic Velocity Addition|velocity-addition]] law) converts the two collinear speeds into the lab speed. The route is: compose $1/n$ with $V$; expand the denominator $(1 + V/n)^{-1} \approx 1 - V/n$ to first order; collect the coefficient of $V$.

**Key decision point.** The crux is recognising that the experimentally accessible quantity is the *coefficient of $V$*, not the speed itself, and that this coefficient — the Fresnel drag $\alpha = 1 - 1/n^2$ — is neither $0$ (no drag, the naive "light unaffected by the medium's motion") nor $1$ (full drag, the Galilean sum $1/n + V$) but a specific intermediate value that *only* the relativistic composition law predicts. The natural Galilean alternative ($\alpha = 1$) is exactly what the experiment refutes.

---

# Legal Operations Used

1. **Apply the velocity-composition law in the collinear form** (operation 4 from the topic page). The beam's speed relative to water and the water's speed relative to the lab are collinear, so $c_1 = (1/n + V)/(1 + V/n)$.

2. **Take a Galilean / low-speed limit to organise the expansion** (operation 9 from the topic page). Expanding to first order in $V$ isolates the leading relativistic correction, which is the measured quantity; the zeroth order is the medium speed $1/n$ and the first order is the Fresnel coefficient.

---

# Hints

> [!note]- Hint 1
> The water is a moving observer. The beam moves at $1/n$ relative to the water; the water moves at $V$ relative to the lab. These two velocities are collinear (along the tube), so the lab speed is the *addition* $c_1 = (1/n + V)/(1 + (1/n)V)$ — not $1/n + V$.

> [!note]- Hint 2
> Expand the denominator: $(1 + V/n)^{-1} \approx 1 - V/n + O(V^2)$. Multiply out $(1/n + V)(1 - V/n)$ and keep terms through first order in $V$. The $V^0$ term is $1/n$; collect the coefficient of $V^1$.

> [!note]- Hint 3
> The coefficient of $V$ is $1 - 1/n^2$. So $c_1 \approx 1/n + (1 - 1/n^2)V$, giving $\alpha = 1 - 1/n^2$. For the phase, the travel-time difference is $\Delta t = 2\ell/c_2 - 2\ell/c_1$ (each beam traverses length $\ell$ in each of two branches); expand and convert to phase via $\Delta\phi = 2\pi\Delta t/T$ with $T = \lambda/c$.

> [!note]- Hint 4
> The Galilean law would give $c_1 = 1/n + V$, i.e. $\alpha = 1$ (full drag). The "no drag" hypothesis gives $\alpha = 0$. Fresnel had *postulated* $\alpha = 1 - 1/n^2$ in 1818 to explain stellar aberration in water-filled telescopes, treating it as a partial aether drag; relativity *derives* the same number with no aether at all.

---

# Solution

The Fizeau coefficient is the first-order-in-$V$ expansion of the collinear velocity-composition law. Step 1 composes the two collinear speeds exactly; Step 2 expands to first order and reads off $\alpha = 1 - 1/n^2$; Step 3 converts the speed difference of the two beams into a measurable phase shift; Step 4 places the result historically. The non-obvious move is recognising that the *coefficient of $V$*, not the speed, is the experimental observable, and that its value distinguishes relativity from both "no drag" and "full drag".

**Step 1: The exact lab speed of the co-moving beam.**

> [!note]- Derivation
> The beam travels at speed $1/n$ relative to the water; the water moves at $V$ relative to the lab, in the same direction. By the collinear [[Thm - Law of Velocity Composition|velocity-composition (addition) law]], the lab speed is
> $$c_1 = \frac{\tfrac{1}{n} + V}{1 + \tfrac{1}{n}V} = \frac{1/n + V}{1 + V/n}.$$
> (Restoring $c$: the beam speed relative to water is $c/n$, and $c_1 = (c/n + V)/(1 + V/(nc))$.) The counter-moving beam has $V \to -V$ relative to the water, giving $c_2 = (1/n - V)/(1 - V/n)$. These are exact; nothing is approximated yet.

**Step 2: First-order expansion and the Fresnel coefficient.**

> [!note]- Derivation
> Expand $c_1$ for $V \ll 1$. Write the denominator's reciprocal as $(1 + V/n)^{-1} = 1 - V/n + O(V^2)$. Then
> $$c_1 = \Big(\frac{1}{n} + V\Big)\Big(1 - \frac{V}{n} + O(V^2)\Big) = \frac{1}{n} - \frac{V}{n^2} + V + O(V^2) = \frac{1}{n} + \Big(1 - \frac{1}{n^2}\Big)V + O(V^2).$$
> Thus $c_1 = 1/n + \alpha V$ with
> $$\boxed{\alpha = 1 - \frac{1}{n^2}.}$$
> The counter-moving beam gives $c_2 = 1/n - \alpha V$ by the same expansion with $V \to -V$. For water, $n = 1.33$, so $\alpha = 1 - 1/1.77 \approx 0.44$: the light is "dragged" by the moving water at about $44\%$ of the water's speed — neither $0$ (no drag) nor $100\%$ (full Galilean drag).

**Step 3: The phase difference.**

> [!note]- Derivation
> Each beam traverses a total length $2\ell$ (the U-tube has two branches of length $\ell$, and in the Fizeau geometry each beam moves with the water in both branches it traverses, or against it). The travel times are $t_1 = 2\ell/c_1$ and $t_2 = 2\ell/c_2$, so the time difference is
> $$\Delta t = t_2 - t_1 = 2\ell\Big(\frac{1}{c_2} - \frac{1}{c_1}\Big).$$
> To first order, $1/c_{1,2} = 1/(1/n \pm \alpha V) \approx n(1 \mp n\alpha V) = n \mp n^2\alpha V$, so
> $$\frac{1}{c_2} - \frac{1}{c_1} = (n + n^2\alpha V) - (n - n^2\alpha V) = 2n^2\alpha V,$$
> giving $\Delta t = 4\ell n^2\alpha V$. The phase difference is $\Delta\phi = 2\pi\Delta t/T = 2\pi\Delta t\,c/\lambda$ (with $T = \lambda/c$ the period, $c=1$):
> $$\Delta\phi = 2\pi\cdot 4\ell n^2\alpha V\cdot\frac{1}{\lambda} = 8\pi n^2\,\frac{\ell}{\lambda}\,\frac{V}{c}\,\alpha,$$
> restoring $c$ in the last factor. Measuring the fringe shift $\Delta\phi$ at known $\ell, \lambda, V, n$ yields $\alpha$, and the measured value agrees with $1 - 1/n^2$, not with the Galilean $\alpha = 1$.

**Step 4: The historical reading.**

> [!note]- Derivation
> Fizeau performed this experiment in 1850, fifty-five years before Einstein's 1905 paper. At the time the result was interpreted through Fresnel's 1818 hypothesis of *partial aether drag*: Fresnel had introduced the coefficient $\alpha = 1 - 1/n^2$ to explain why stellar aberration is unaffected by filling a telescope with water, proposing that a moving transparent body drags the luminiferous aether along with it, but only fractionally. Fizeau's measurement confirmed Fresnel's coefficient.
>
> Special relativity dissolves the aether entirely and yet reproduces the *same* coefficient as a mathematical identity: $\alpha = 1 - 1/n^2$ is simply the first-order term in the relativistic composition of $1/n$ with $V$. There is no medium being dragged; there is only the non-additivity of velocities. The agreement is total, and for Einstein the Fizeau experiment was among the strongest empirical supports for relativity — on a par with, or above, Michelson–Morley — precisely because the relativistic prediction is unique: neither "no drag" ($\alpha = 0$) nor "full drag" ($\alpha = 1$), but the specific intermediate value forced by the composition law.

> [!note]- Complete formal solution
> The co-moving beam's lab speed is the collinear composition $c_1 = (1/n + V)/(1 + V/n)$. Expanding for $V \ll 1$: $c_1 = (1/n + V)(1 - V/n) + O(V^2) = 1/n + (1 - 1/n^2)V + O(V^2)$, so the Fresnel drag coefficient is $\alpha = 1 - 1/n^2$ (and $c_2 = 1/n - \alpha V$ for the counter-moving beam). The travel-time difference over length $\ell$ per branch is $\Delta t = 2\ell(1/c_2 - 1/c_1) = 4\ell n^2\alpha V$ to first order, giving the phase shift $\Delta\phi = 2\pi\Delta t/\lambda = 8\pi n^2(\ell/\lambda)(V/c)\alpha$. The measured $\alpha = 1 - 1/n^2$ matches the relativistic prediction and excludes the Galilean $\alpha = 1$; Fresnel's pre-relativistic "partial aether drag" coefficient is reproduced by relativity as the first-order velocity-composition correction, with no aether. $\blacksquare$

---

# Key Takeaways

**The Fresnel drag is the first-order velocity-composition correction, and its value rules out both naive alternatives.** The whole content of the Fizeau experiment is that the coefficient of $V$ in the lab speed of light in a moving medium is $1 - 1/n^2$, a number that sits strictly between the "light is unaffected by the medium's motion" prediction ($\alpha = 0$) and the "velocities just add" Galilean prediction ($\alpha = 1$). This is the trigger to recognise across many problems: whenever a result is a *specific intermediate value* between two intuitive extremes, suspect that a relativistic composition (or a similar exact law) is being expanded to first order, and that the leading correction is the physics. The experimentally decisive quantity is almost never the full nonlinear formula but its leading deviation from the Galilean expectation, because that is where theories first disagree and where a precision measurement at modest speed can discriminate. The same logic recurs in the [[Ex - The Ives-Stilwell experiment and transverse Doppler|Ives–Stilwell]] (where the decisive quantity is the second-order time-dilation factor) and in stellar aberration (where it is the first-order $U/c$).

**A medium in motion is just a moving observer, and "the speed of light in the medium" is a velocity relative to that observer.** The conceptual move that makes Fizeau trivial is to stop thinking of the water as a mysterious modifier of light and start thinking of it as a second inertial observer, relative to whom the beam has the perfectly ordinary speed $1/n$. Then the lab speed is a velocity composition, full stop. This reframing — *medium as observer* — generalises: the speed of sound in wind, the drift of a signal in a moving plasma, the propagation of any disturbance in a moving carrier are all velocity-composition problems once the carrier is recognised as a frame. The reusable diagnostic: when a speed is quoted "relative to a substance" and the substance is itself moving, do not add the speeds — compose them.

**Pre-relativistic "aether" results often survive as relativistic identities, because relativity had to reproduce every confirmed low-speed measurement.** Fizeau's confirmation of Fresnel's partial-drag coefficient looks, at first, like evidence for the aether — and for sixty years it was read that way. Its survival into relativity, with the aether deleted, is a model of how a successful new theory must relate to the old: relativity could not contradict any *measurement* Fresnel's aether theory had got right, only its *interpretation*, so the coefficient $1 - 1/n^2$ had to reappear, and it does, as the first-order term of the composition law. The transferable lesson for reading physics history (and for trusting new theories) is that empirically confirmed numbers are robust across paradigm shifts even when their explanations are overturned; the formula $\alpha = 1 - 1/n^2$ is correct in both frameworks, and only the story behind it changed. Recognising this guards against both over-crediting a discredited theory (the aether) and doubting a correct measurement (Fizeau's) merely because its original interpretation was wrong.
