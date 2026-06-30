---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Measurement of Rotation (Non-rotating Observer)"
  - "Def - Uniformly Rotating Observer"
  - "Def - Fermi-Walker Derivative"
tags: [physics, special-relativity]
---

# Problem Statement

1. An observer wishes to determine their four-rotation $\vec\omega$ using free gyroscopes. Show that a *single* free gyroscope is insufficient: it constrains only two of the three components of $\vec\omega$. Identify which component is undetermined and explain physically why.
2. Show that two non-parallel free gyroscopes suffice to determine $\vec\omega$ completely.
3. For the uniformly rotating disk, a corotating observer at radius $r$ carries free gyroscopes. Using the four-rotation $\vec\omega' = \Gamma^2\vec\omega$, find the radius at which a gyroscope's precession rate (relative to the corotating frame) would formally diverge, and relate it to the light cylinder $r = c/\omega$.
4. Explain why no physical corotating observer exists at or beyond the light cylinder, and what happens to the gyroscope there.

**Recall:**

![[Def - Measurement of Rotation (Non-rotating Observer)#The Definition]]

A free (torque-free) gyroscope's spin vector $\vec s$ is [[Def - Fermi-Walker Derivative|Fermi–Walker transported]], so $D_{\mathcal{O}}\vec s = -\vec\omega\times_U\vec s$ for an observer $\mathcal{O}$ with four-rotation $\vec\omega$ — the spin precesses, as seen by $\mathcal{O}$, at angular velocity $-\vec\omega$. A [[Def - Uniformly Rotating Observer|corotating observer]] at radius $r$ has Lorentz factor $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$, diverging at the light cylinder $r = c/\omega$.

---

# Convergent Strategy

**Problem class.** A *why-this-construction* problem probing the operational definition of non-rotating, combined with a limit analysis of the light cylinder. The [[Special Relativity XVII — Rotating Observers#Problem-Solving Strategy|topic strategy]] emphasizes that $\vec\omega$ is measurable and that the radius bound $r < c/\omega$ is forced by timelikeness.

**Assumption pattern.** Free gyroscopes carried by an observer. The signpost is the cross-product structure of the gyroscope precession law $D_{\mathcal{O}}\vec s = -\vec\omega\times_U\vec s$: a cross product annihilates the component of $\vec\omega$ parallel to $\vec s$, so one gyroscope is blind to one direction. This algebraic fact drives parts 1–2.

**Theorem routing.** Parts 1–2 analyze the kernel of the cross-product map $\vec\omega\times_U(\cdot)$ from [[Def - Measurement of Rotation (Non-rotating Observer)]]; parts 3–4 use $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$ from [[Def - Uniformly Rotating Observer]] and the four-rotation $\vec\omega' = \Gamma^2\vec\omega$, taking the limit $r\to c/\omega$.

**Key decision point.** For parts 1–2 the crux is recognizing that "a gyroscope detects rotation" means "the cross product $\vec\omega\times\vec s$ is nonzero", which fails exactly when $\vec\omega\parallel\vec s$ — so one gyroscope has a blind direction. For parts 3–4 the crux is that the divergence of $\Gamma$ at the light cylinder signals not a real infinite precession but the breakdown of the corotating observer's existence (the worldline ceases to be timelike).

---

# Legal Operations Used

1. **Operation 2 from the topic page (the rim Lorentz factor).** $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$ and its divergence at $r = c/\omega$ drive parts 3–4.

2. **Operation 8 from the topic page (the local invariance of $c$).** Even an accelerated or rotating observer measures local light speed $c$; this underlies why the light cylinder is a genuine causal boundary, not a coordinate artifact.

---

# Hints

> [!note]- Hint 1
> The gyroscope precession law is $D_{\mathcal{O}}\vec s = -\vec\omega\times_U\vec s$. A cross product $\vec\omega\times\vec s$ vanishes when $\vec\omega$ and $\vec s$ are parallel. So if the observer's four-rotation happens to be *along* the gyroscope's spin, the gyroscope shows no precession at all — it cannot detect rotation about its own spin axis.

> [!note]- Hint 2
> The precession $-\vec\omega\times_U\vec s$ determines the components of $\vec\omega$ perpendicular to $\vec s$. A second gyroscope with spin $\vec s'$ not parallel to $\vec s$ determines the components perpendicular to $\vec s'$. Between the two, all three components are pinned: the only direction left undetermined by the first (along $\vec s$) is detected by the second (since $\vec s'\not\parallel\vec s$).

> [!note]- Hint 3
> The corotating observer's four-rotation magnitude is $\Gamma^2\omega = \omega/(1 - r^2\omega^2/c^2)$, which $\to\infty$ as $r\to c/\omega$. But before reading this as a physical infinity, ask whether a corotating observer even exists at $r = c/\omega$.

> [!note]- Hint 4
> At $r = c/\omega$ the rim speed equals $c$, so $\Gamma\to\infty$ and the would-be worldline is null; no clock can be carried along it, and proper time does not advance. The "infinite precession" is not physical — it signals that there is no corotating observer there to carry the gyroscope.

---

# Solution

The route has four steps. Steps 1–2 analyze the cross-product structure of the gyroscope law: one gyroscope is blind to rotation about its own spin (the kernel of $\vec\omega\times$), two non-parallel gyroscopes pin all three components. Steps 3–4 take the light-cylinder limit, showing the formal divergence of $\Gamma^2\omega$ is the non-existence of the corotating observer, not a real infinite precession. The non-obvious move is reading the divergence as a breakdown of the worldline, not a physical singularity.

**Step 1: One gyroscope is blind to rotation about its own spin axis.**

> [!note]- Derivation
> The free gyroscope's spin obeys $D_{\mathcal{O}}\vec s = -\vec\omega\times_U\vec s$. Decompose $\vec\omega = \vec\omega_\parallel + \vec\omega_\perp$ into components parallel and perpendicular to $\vec s$. The cross product annihilates the parallel part:
> $$\vec\omega\times_U\vec s = (\vec\omega_\parallel + \vec\omega_\perp)\times_U\vec s = \vec\omega_\perp\times_U\vec s,$$
> since $\vec\omega_\parallel\times_U\vec s = 0$ (parallel vectors have zero cross product). So the observed precession depends *only* on $\vec\omega_\perp$, the two components of $\vec\omega$ perpendicular to $\vec s$. The component $\vec\omega_\parallel$ — rotation about the gyroscope's own spin axis — produces no precession and is undetectable by this gyroscope. Physically: a spinning top cannot tell whether the platform beneath it is rotating about the top's own axis, because such a rotation does not tip the top's axis. The single gyroscope determines two of the three components of $\vec\omega$; one is blind.

**Step 2: Two non-parallel gyroscopes determine $\vec\omega$ completely.**

> [!note]- Derivation
> Gyroscope $1$ (spin $\vec s_1$) determines the two components of $\vec\omega$ perpendicular to $\vec s_1$, leaving undetermined only the component along $\vec s_1$. Gyroscope $2$ (spin $\vec s_2$, not parallel to $\vec s_1$) determines the components perpendicular to $\vec s_2$ — and since $\vec s_2\not\parallel\vec s_1$, the direction $\vec s_1$ has a nonzero component perpendicular to $\vec s_2$, so gyroscope $2$ "sees" the very component gyroscope $1$ missed. Formally, the union of the planes $\vec s_1^\perp$ and $\vec s_2^\perp$ spans the whole rest space (two distinct planes through the origin in $\mathbb{R}^3$ have union spanning $\mathbb{R}^3$), so together the two gyroscopes constrain all three components of $\vec\omega$. Three orthogonal gyroscopes over-determine $\vec\omega$ robustly and supply a complete non-rotating frame, which is why the construction of a non-rotating observer uses three.

**Step 3: The formal precession diverges as $r\to c/\omega$.**

> [!note]- Derivation
> The corotating observer's four-rotation has magnitude
> $$\|\vec\omega'\| = \Gamma^2\omega = \frac{\omega}{1 - r^2\omega^2/c^2}.$$
> As $r\to c/\omega$ from below, the denominator $\to 0$ and $\|\vec\omega'\|\to\infty$. Taken at face value, this says a gyroscope carried by a corotating observer near the light cylinder precesses (relative to the corotating frame) arbitrarily fast. But this formal divergence must be interpreted carefully, because $\Gamma$ also diverges, signalling that the corotating observer itself is becoming ill-defined.

**Step 4: No corotating observer exists at the light cylinder; the divergence is the breakdown of the worldline.**

> [!note]- Derivation
> At $r = c/\omega$ the rim speed is exactly $\|\vec V\| = r\omega = c$. The would-be corotating worldline $x_*(t) = (c/\omega)\cos(\omega t + \varphi)$, $y_*(t) = (c/\omega)\sin(\omega t + \varphi)$ has tangent of speed $c$ at every point — it is a *null* curve. No clock can be carried along a null curve (proper time does not advance), so there is no corotating *observer* there. For $r > c/\omega$ the tangent is spacelike, even more unphysical. Therefore the divergence of $\Gamma^2\omega$ is not a real infinite precession of a physical gyroscope; it is the mathematical signal that the corotating observer ceases to exist at the light cylinder. The local invariance of the speed of light — even rotating observers measure local light speed $c$ — guarantees this is a genuine causal boundary: a corotating observer would have to move *at* light speed to keep up with the disk at $r = c/\omega$, which is impossible. The gyroscope, like the observer, simply has no worldline to be carried along.

> [!note]- Complete formal solution
> The gyroscope law $D_{\mathcal{O}}\vec s = -\vec\omega\times_U\vec s$ has $\vec\omega\times_U\vec s$ depending only on the component of $\vec\omega$ perpendicular to $\vec s$ (the cross product kills the parallel part), so one gyroscope determines two components of $\vec\omega$ and is blind to rotation about its own spin axis. Two non-parallel gyroscopes have perpendicular planes $\vec s_1^\perp\cup\vec s_2^\perp$ spanning the rest space, so together they fix all three components; three orthogonal ones over-determine $\vec\omega$ and give a full non-rotating frame. For the disk, $\|\vec\omega'\| = \Gamma^2\omega = \omega/(1 - r^2\omega^2/c^2)\to\infty$ as $r\to c/\omega$, but this is not a physical infinity: at $r = c/\omega$ the rim speed is $c$, the worldline is null, no clock advances, and there is no corotating observer to carry the gyroscope. The light cylinder is a genuine causal boundary, forced by the impossibility of corotation at light speed. $\blacksquare$

---

# Key Takeaways

**A cross product has a kernel, and that kernel is why one gyroscope is not enough.** The gyroscope precession law is a cross product $-\vec\omega\times\vec s$, and cross products annihilate parallel vectors — so a gyroscope is blind to rotation about its own spin axis. This is a purely algebraic fact with a sharp physical consequence: determining a three-component angular velocity requires at least two non-parallel probes, because each probe is blind to one direction. The trigger to recognize this pattern is any measurement law of the form "response $= \vec\omega\times(\text{probe})$": the probe direction is always undetectable, so a complete determination needs a second, non-parallel probe. The same structure appears in magnetometry (a single current loop is blind to the field along its axis) and in determining angular velocity from any single vector observation. The operational definition of "non-rotating" must therefore invoke *three* gyroscopes, not one, and the reason is this kernel.

**A divergent Lorentz factor signals the breakdown of an observer, not a physical infinity.** When $\Gamma^2\omega\to\infty$ at the light cylinder, the naive reading "infinite precession" is wrong: the divergence is the mathematics warning that the corotating observer ceases to exist, because its worldline becomes null at the speed of light. The trigger to watch for is any quantity that diverges *together with* $\Gamma$: such divergences almost always signal the approach to a causal boundary (a light cylinder, an event horizon, a speed limit) rather than a genuine physical singularity, and the right response is to check whether the observer or trajectory is still admissible. This is the flat-spacetime rehearsal for the coordinate singularities of general relativity, where a diverging metric component at a horizon signals the breakdown of a coordinate system or an observer, not curvature. Learning to distinguish "the formula blew up" from "physics blew up" is one of the most transferable skills in relativity.

**The light cylinder is a hard causal boundary, the same kind that organizes pulsars and rotating black holes.** The bound $r < c/\omega$ is not a quirk of the construction but a genuine limit: corotation at the speed of light is impossible, so no rigid rotation extends past $r = c/\omega$. The trigger is any rotating system with a fixed angular velocity — immediately ask where the corotation speed reaches $c$. In a pulsar, the magnetic field lines anchored to the star corotate only within the light cylinder; beyond it they must open, and the open field lines channel the relativistic wind and beamed emission. In a Kerr black hole, the analogous surface is the ergosphere, where frame dragging reaches light speed. The flat-spacetime light cylinder of this exercise is the conceptual seed of both, and recognizing it as a timelikeness boundary — derived in [[Ex - The four-velocity and four-acceleration of a corotating observer]] — is what lets you transfer the idea to those strong-field settings.
