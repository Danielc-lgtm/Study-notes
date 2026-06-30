---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Inertial Observer"
  - "Def - Local Frame and Four-Rotation"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

Gourgoulhon's Remark 8.1 asserts that the converse of "inertial observer $\Rightarrow$ straight worldline" is false: a straight worldline guarantees only a vanishing four-acceleration, not a vanishing four-rotation. Construct an explicit counterexample. Working with $c = 1$ in an inertial coordinate system $(O; e_0, e_1, e_2, e_3)$:

1. Take an observer at rest at the spatial origin, with constant four-velocity $U = e_0$, so the worldline is the straight line $x^\alpha(\tau) = (\tau, 0, 0, 0)$. Verify $a = \mathrm{d}U/\mathrm{d}\tau = 0$.
2. Equip this observer with a spatial triad that *rotates* in proper time: $e_1'(\tau) = \cos(\Omega\tau)\,e_1 + \sin(\Omega\tau)\,e_2$, $e_2'(\tau) = -\sin(\Omega\tau)\,e_1 + \cos(\Omega\tau)\,e_2$, $e_3'(\tau) = e_3$, with $e_0'(\tau) = U = e_0$. Check this is an orthonormal frame at each $\tau$.
3. Compute $\mathrm{d}e_\alpha'/\mathrm{d}\tau$ and show it is nonzero for $\alpha = 1, 2$, so the frame is not constant; identify the four-rotation $\omega$ and confirm $\omega \neq 0$ while $a = 0$.
4. Conclude that this observer has a straight worldline but is *not* inertial, and explain in one sentence why "straight worldline" captures strictly less than "inertial observer".

**Recall:**

![[Def - Inertial Observer#The Definition]]

A [[Def - Local Frame and Four-Rotation|local frame]] is an orthonormal tetrad $(e_0', e_1', e_2', e_3')$ carried along the worldline with $e_0' = U$ the four-velocity; orthonormality means $e_0'\cdot e_0' = 1$, $e_i'\cdot e_i' = -1$, all cross products zero (mostly-minus). The frame evolves by $\mathrm{d}e_\alpha'/\mathrm{d}\tau = (a\cdot e_\alpha')U - (U\cdot e_\alpha')a + \omega\times_U e_\alpha'$, decomposing into a four-acceleration part $a$ and a four-rotation part $\omega$ (a spatial vector in the rest space). An observer is inertial exactly when this derivative vanishes, equivalently $a = 0$ and $\omega = 0$.

---

# Convergent Strategy

**Problem class.** A *construct-a-counterexample* problem: exhibit an object satisfying one condition ($a = 0$, straight worldline) but failing another ($\omega = 0$, inertiality). The [[Special Relativity XII — Inertial Observers and the Poincaré Group#Problem-Solving Strategy|topic strategy]] warns that the two conditions of inertiality are independent and that straightness controls only the first; this exercise makes the warning concrete.

**Assumption pattern.** We are *free to choose* the frame, and the construction exploits exactly that freedom: fix the four-velocity (controls $a$) and let the spatial triad spin (controls $\omega$). The signpost is that inertiality has two independent knobs, $a$ and $\omega$; setting one to zero leaves the other free, so a counterexample exists.

**Theorem routing.** The route is computational, not theorem-driven: verify $a = \mathrm{d}U/\mathrm{d}\tau = 0$ (constant $U$), verify orthonormality of the rotating triad, then differentiate the triad to find $\mathrm{d}e_i'/\mathrm{d}\tau \neq 0$ and read off $\omega = \Omega\,e_3$ from the frame-evolution law (with $a = 0$ the law reduces to $\mathrm{d}e_\alpha'/\mathrm{d}\tau = \omega\times_U e_\alpha'$).

**Key decision point.** The crux is recognising that the four-velocity and the spatial frame are *separately* specifiable: the worldline (hence $a$) depends only on $e_0' = U$, while $\omega$ depends on how the spatial triad turns. Choosing a constant $U$ with a rotating triad decouples them, producing $a = 0$ but $\omega \neq 0$. The natural-but-wrong intuition that "straight worldline = inertial" comes from forgetting that the frame carries information the worldline does not.

---

# Legal Operations Used

1. **Test inertiality by the conditions $a = 0$ and $\omega = 0$** (operation 1 from the topic page). Both conditions are computed: $a = 0$ from the constant four-velocity, $\omega \neq 0$ from the rotating triad, demonstrating that the first holds and the second fails.

2. The exercise is the explicit counterexample behind illegal operation 1 of the topic page ("concluding straight worldline, therefore inertial"): it supplies the concrete observer with $a = 0$ but $\omega \neq 0$ that forbids the shortcut.

---

# Hints

> [!note]- Hint 1
> The worldline depends only on the four-velocity $e_0' = U$. With $U = e_0$ constant, the worldline is the straight time axis and $a = \mathrm{d}U/\mathrm{d}\tau = 0$. The four-acceleration knows nothing about the spatial triad.

> [!note]- Hint 2
> Differentiate the rotating triad. For instance $\mathrm{d}e_1'/\mathrm{d}\tau = -\Omega\sin(\Omega\tau)\,e_1 + \Omega\cos(\Omega\tau)\,e_2 = \Omega\,e_2'(\tau)$. This is nonzero, so the frame is not constant.

> [!note]- Hint 3
> With $a = 0$, the frame-evolution law reduces to $\mathrm{d}e_\alpha'/\mathrm{d}\tau = \omega\times_U e_\alpha'$. Compare with the computed derivatives $\mathrm{d}e_1'/\mathrm{d}\tau = \Omega\,e_2'$, $\mathrm{d}e_2'/\mathrm{d}\tau = -\Omega\,e_1'$, $\mathrm{d}e_3'/\mathrm{d}\tau = 0$ to read off $\omega = \Omega\,e_3$ — the spatial rotation rate about the $e_3$ axis.

---

# Solution

The counterexample decouples the two conditions of inertiality. Step 1 fixes a constant four-velocity, forcing $a = 0$ and a straight worldline. Step 2 attaches a spatial triad rotating at rate $\Omega$ and checks it stays orthonormal. Step 3 differentiates the triad, finds it non-constant, and reads off $\omega = \Omega\,e_3 \neq 0$. The conclusion: straight worldline, but not inertial.

**Step 1: Constant four-velocity, straight worldline, $a = 0$.**

> [!note]- Derivation
> Take $U = e_0$, constant. The worldline is $x^\alpha(\tau) = (\tau, 0, 0, 0)$ — the straight time axis through the origin, with the observer sitting still in space. The four-acceleration is
> $$a = \frac{\mathrm{d}U}{\mathrm{d}\tau} = \frac{\mathrm{d}e_0}{\mathrm{d}\tau} = 0,$$
> since $e_0$ does not depend on $\tau$. So the four-acceleration vanishes and the worldline is straight, exactly the conditions of [[Ex - Inertial worldline is a straight line]]. So far the observer looks inertial.

**Step 2: The rotating triad is orthonormal.**

> [!note]- Derivation
> Define the spatial triad
> $$e_1'(\tau) = \cos(\Omega\tau)\,e_1 + \sin(\Omega\tau)\,e_2, \qquad e_2'(\tau) = -\sin(\Omega\tau)\,e_1 + \cos(\Omega\tau)\,e_2, \qquad e_3'(\tau) = e_3,$$
> with $e_0'(\tau) = U = e_0$. This is a proper-time-dependent rotation of the spatial axes about $e_3$ at angular rate $\Omega$. Check orthonormality at each $\tau$ (mostly-minus, so $e_i\cdot e_j = -\delta_{ij}$):
> $$e_1'\cdot e_1' = \cos^2(\Omega\tau)\,(e_1\cdot e_1) + \sin^2(\Omega\tau)\,(e_2\cdot e_2) = -\cos^2 - \sin^2 = -1,$$
> and similarly $e_2'\cdot e_2' = -1$, $e_3'\cdot e_3' = -1$, $e_0'\cdot e_0' = 1$. The cross terms vanish:
> $$e_1'\cdot e_2' = -\cos\sin\,(e_1\cdot e_1) + \sin\cos\,(e_2\cdot e_2)\cdot(\cdots) = \cos\sin - \sin\cos = 0,$$
> and $e_i'\cdot e_0' = 0$ since the spatial triad lies in the rest space $e_0^\perp$. So $(e_0', e_1', e_2', e_3')$ is a valid orthonormal [[Def - Local Frame and Four-Rotation|local frame]] at every $\tau$.

**Step 3: The frame is not constant; $\omega = \Omega\,e_3 \neq 0$.**

> [!note]- Derivation
> Differentiate the triad in proper time:
> $$\frac{\mathrm{d}e_1'}{\mathrm{d}\tau} = -\Omega\sin(\Omega\tau)\,e_1 + \Omega\cos(\Omega\tau)\,e_2 = \Omega\,e_2'(\tau),$$
> $$\frac{\mathrm{d}e_2'}{\mathrm{d}\tau} = -\Omega\cos(\Omega\tau)\,e_1 - \Omega\sin(\Omega\tau)\,e_2 = -\Omega\,e_1'(\tau),$$
> $$\frac{\mathrm{d}e_3'}{\mathrm{d}\tau} = 0, \qquad \frac{\mathrm{d}e_0'}{\mathrm{d}\tau} = 0.$$
> The derivatives of $e_1'$ and $e_2'$ are nonzero, so the frame is *not* constant: $\mathrm{d}e_\alpha'/\mathrm{d}\tau \neq 0$. Since $a = 0$, the frame-evolution law reduces to $\mathrm{d}e_\alpha'/\mathrm{d}\tau = \omega\times_U e_\alpha'$, a spatial rotation in the rest space. Comparing with the computed derivatives — $e_1'\mapsto\Omega e_2'$, $e_2'\mapsto-\Omega e_1'$, $e_3'\mapsto 0$ — this is rotation about the $e_3$-axis at rate $\Omega$, so the [[Def - Local Frame and Four-Rotation|four-rotation]] is
> $$\omega = \Omega\,e_3 \neq 0.$$
> The observer has $a = 0$ but $\omega \neq 0$.

**Step 4: Straight worldline, but not inertial.**

> [!note]- Derivation
> By [[Def - Inertial Observer|the definition]], an inertial observer requires *both* $a = 0$ and $\omega = 0$. This observer has $a = 0$ — its worldline is the straight time axis — but $\omega = \Omega\,e_3 \neq 0$: its spatial triad precesses about $e_3$ at rate $\Omega$. So it is **not inertial**, despite having a perfectly straight worldline. A gyroscope it carries would be seen to precess (relative to its own spinning frame) for no dynamical reason, which is exactly the symptom of a rotating, non-inertial frame.
>
> The one-sentence moral: a straight worldline captures only the vanishing of the four-acceleration, which fixes how the four-velocity $e_0'$ moves, and is entirely silent about the four-rotation, which fixes how the *spatial* triad turns — so "straight worldline" is strictly weaker than "inertial observer".

> [!note]- Complete formal solution
> Take $U = e_0$ constant, giving the straight worldline $x^\alpha(\tau) = (\tau, 0, 0, 0)$ and four-acceleration $a = \mathrm{d}e_0/\mathrm{d}\tau = 0$. Attach the spatial triad $e_1' = \cos(\Omega\tau)e_1 + \sin(\Omega\tau)e_2$, $e_2' = -\sin(\Omega\tau)e_1 + \cos(\Omega\tau)e_2$, $e_3' = e_3$, with $e_0' = U$; orthonormality holds at each $\tau$ ($e_i'\cdot e_j' = -\delta_{ij}$, $e_0'\cdot e_0' = 1$, mixed products zero). Differentiating, $\mathrm{d}e_1'/\mathrm{d}\tau = \Omega e_2'$, $\mathrm{d}e_2'/\mathrm{d}\tau = -\Omega e_1'$, $\mathrm{d}e_3'/\mathrm{d}\tau = 0$, so the frame is not constant; with $a = 0$ the evolution law $\mathrm{d}e_\alpha'/\mathrm{d}\tau = \omega\times_U e_\alpha'$ gives $\omega = \Omega e_3 \neq 0$. Thus $a = 0$ but $\omega \neq 0$: the worldline is straight yet the observer is not inertial, since inertiality requires both four-acceleration and four-rotation to vanish. The converse of "inertial $\Rightarrow$ straight" therefore fails (Gourgoulhon Remark 8.1). $\blacksquare$

---

# Key Takeaways

**Inertiality has two independent knobs, $a$ and $\omega$, and this exercise turns one off while leaving the other on.** The four-acceleration $a$ governs how the four-velocity $e_0'$ changes — it controls the *worldline* — while the four-rotation $\omega$ governs how the *spatial triad* turns. They are logically independent: the construction here fixes a constant $U$ (so $a = 0$, straight worldline) and freely spins the triad (so $\omega \neq 0$, non-inertial). The transferable lesson is that whenever a definition has two independent conditions, the way to show they are independent is to satisfy one and violate the other by a free choice — here, the freedom to rotate the spatial frame independently of the worldline. This is the standard counterexample-construction move, and it generalises far beyond relativity.

**A straight worldline is necessary but not sufficient for inertiality — the gyroscope, not the trajectory, is the final arbiter.** The seductive shortcut "straight worldline, therefore inertial" fails precisely because the worldline sees only $e_0'$, not the spatial triad. The physical diagnostic that catches the failure is a gyroscope: an inertial observer's gyroscope holds fixed directions, while this observer's spinning frame precesses relative to a carried gyroscope (or equivalently, a carried gyroscope precesses relative to the spinning frame). Whenever you have shown a worldline is straight, the residual question is always "does the frame rotate?" — and only a gyroscope (testing $\omega = 0$), not the trajectory (testing $a = 0$), answers it. This is why the definition of an inertial observer is phrased through the *frame* ($\mathrm{d}e_\alpha/\mathrm{d}\tau = 0$) rather than the worldline.

**The construction is the seed of Fermi–Walker transport and Thomas precession.** The rotating triad here is an artificial, hand-imposed spin, but the same structure arises *physically* for accelerated observers, where the four-rotation is forced rather than chosen. An accelerated observer who tries to keep its frame "as non-rotating as possible" follows Fermi–Walker transport, and even then, for a worldline that curves in two planes, the frame acquires a residual rotation — Thomas precession — exactly of the form $\mathrm{d}e_\alpha'/\mathrm{d}\tau = \omega\times_U e_\alpha'$ with a computable $\omega$. So this toy counterexample, where $\omega$ is put in by hand, is the kinematic skeleton of the genuine spin-precession phenomena of accelerated and orbiting observers studied later. Recognise the pattern $\mathrm{d}e'/\mathrm{d}\tau = \omega\times_U e'$ whenever a carried frame rotates, whether the rotation is imposed (as here) or dynamically generated (as in Thomas precession).
