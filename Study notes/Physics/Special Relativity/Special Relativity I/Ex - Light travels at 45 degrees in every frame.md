---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Spacetime Diagram"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

On a [[Def - Spacetime Diagram|spacetime diagram]] with $ct$ vertical and $x$ horizontal ($c = 1$), light rays are drawn at $45^\circ$. Justify and explore this convention.

1. **Why $45^\circ$.** Explain why plotting $ct$ (rather than $t$) on the vertical axis makes a light ray $x = ct$ appear at exactly $45^\circ$, and why this is the right choice given the second postulate.
2. **Frame-independence.** Show, using the [[Def - The Lorentz Transformation|Lorentz transformation]], that a $45^\circ$ light ray in $S$ is *also* a $45^\circ$ light ray in any boosted frame $S'$ — so all inertial observers agree that the light lines are at $45^\circ$. (Treat both the $+x$ and $-x$ directions.)
3. **The light cone.** Describe the set of all light rays through the origin in $1+1$ and in $3+1$ dimensions, and explain why this set — the light cone — is the same for every inertial observer.
4. **Light in a transverse direction.** A light pulse moves in the $y$-direction in $S$ ($y = ct$, $x = 0$). Show that in $S'$ (boosted along $x$) its speed is still $c$, even though its direction is no longer purely transverse. (This is the relativistic aberration of the pulse's direction; the *speed* is invariant.)

**Recall:**

![[Def - Spacetime Diagram#The Definition]]

The [[Def - The Lorentz Transformation|Lorentz boost]] along $x$ is $x' = \gamma(x - vt)$, $t' = \gamma(t - vx)$, $y' = y$, $z' = z$ ($c = 1$). The [[Def - Inertial Frame and the Postulates of Special Relativity|second postulate]] states that light travels at $c$ in every inertial frame.

---

# Convergent Strategy

**Problem class.** This is a *verification / consistency* problem: confirm that a drawing convention (light at $45^\circ$) is consistent with, and indeed forced by, the [[Def - The Lorentz Transformation|Lorentz transformation]] and the [[Def - Inertial Frame and the Postulates of Special Relativity|second postulate]]. The [[Special Relativity I — Postulates and Lorentz Transformations#Problem-Solving Strategy|topic strategy]] treats "the constancy of $c$ fixes the light lines" as a foundational source.

**Assumption pattern.** The inputs are the rescaling to $ct$ and the boost. The recognition is that the $45^\circ$ convention is the *only* one that makes light's slope frame-independent: because light has speed $c$ in every frame (second postulate), its slope in the $ct$–$x$ plane is $1$ in every frame, and only the $ct$ rescaling realises slope $1$ as a fixed $45^\circ$.

**Theorem routing.** For frame-independence, substitute $x = \pm t$ into the boost and confirm $x' = \pm t'$. For transverse light, transform $(t, 0, ct, 0)$ and compute $|\mathbf{v}'| = \sqrt{v_x'^2 + v_y'^2}$, showing it equals $c$.

**Key decision point.** The instructive subtlety is part 4: transverse light *changes direction* under a boost (aberration) but keeps *speed* $c$. The temptation is to think a boost along $x$ leaves $y$-light alone (since $y' = y$); in fact the boost mixes $t$ and $x$, so the *time* the pulse takes changes, giving it an apparent $x$-velocity in $S'$ — yet the total speed remains $c$. Recognising that direction and speed behave differently (direction transforms, speed is invariant) is the key insight.

---

# Legal Operations Used

1. **Operation 1 from the topic page (apply the Lorentz transformation).** Frame-independence and the transverse-light computation are direct substitutions into the boost.

2. **Operation 8 from the topic page (use the $45^\circ$ light structure / classify by the light cone).** The light cone is the central object, and its frame-independence is the point.

---

# Hints

> [!note]- Hint 1
> A light ray is $x = ct$, i.e. $x = t$ when $c = 1$. On a plot with $ct$ vertical and $x$ horizontal, the slope is $\Delta(ct)/\Delta x = 1$ — a $45^\circ$ line. If you plotted $t$ vertical and $x$ horizontal in mismatched units, the slope would be $c$, some unit-dependent number.

> [!note]- Hint 2
> Take $x = t$ (light in $+x$). Then $x' = \gamma(t - vt) = \gamma t(1 - v)$ and $t' = \gamma(t - vt) = \gamma t(1 - v)$, so $x' = t'$. The same with $x = -t$ gives $x' = -t'$. Both light lines map to themselves.

> [!note]- Hint 3
> In $1+1$ the light cone through the origin is the two lines $x = \pm ct$ (an "X"). In $3+1$ it is $x^2 + y^2 + z^2 = c^2 t^2$, a genuine cone. Since light is at $45^\circ$ in every frame (part 2), every observer draws the same cone.

> [!note]- Hint 4
> For $y$-light: in $S$, $x = 0$, $y = t$ (so $z = 0$). Transform: $t' = \gamma t$, $x' = -\gamma v t$, $y' = y = t$. So in $S'$, $x' = -v t = -v(t'/\gamma)$ and $y' = t = t'/\gamma$. Compute $v_x' = x'/t' = -v$, $v_y' = y'/t' = 1/\gamma$, then $|\mathbf{v}'|^2 = v^2 + 1/\gamma^2$.

---

# Solution

Plotting $ct$ on the vertical axis makes light's slope exactly $1$ — a $45^\circ$ line (Step 1) — and the boost maps these lines to themselves, so all observers agree light is at $45^\circ$ (Step 2). The light cone they all draw is therefore identical (Step 3). Even transverse light keeps speed $c$ in a boosted frame, though its direction aberrates (Step 4).

**Step 1: $ct$ on the vertical makes light slope $1$, hence $45^\circ$.**

> [!note]- Derivation
> A light ray moving in $+x$ obeys $x = ct$. On a diagram with the vertical coordinate $ct$ and horizontal coordinate $x$, the ray's slope is
> $$\frac{\Delta(ct)}{\Delta x} = \frac{\Delta(ct)}{\Delta(ct)} = 1$$
> (since $x = ct$), a line at $45^\circ$ to both axes. Had we plotted the *bare* time $t$ vertically against $x$ horizontally in mismatched units, the slope would be $\Delta t/\Delta x = 1/c$, a tiny number ($\sim 3\times 10^{-9}$ in SI), and the light line would be nearly horizontal — no special angle. Rescaling the time axis to $ct$ (equivalently, measuring time in light-seconds, so that one second of time and one light-second of distance occupy the same length on the page) is exactly what promotes the light line to a clean $45^\circ$. This is the *right* choice because, by the [[Def - Inertial Frame and the Postulates of Special Relativity|second postulate]], light is the one thing every observer agrees travels at $c$, so making its worldline a fixed, frame-independent $45^\circ$ line builds the postulate into the picture.

**Step 2: Light at $45^\circ$ in $S$ is at $45^\circ$ in every $S'$.**

> [!note]- Derivation
> Take a light ray in the $+x$ direction in $S$: $x = t$ ($c = 1$). Apply the boost:
> $$x' = \gamma(x - vt) = \gamma(t - vt) = \gamma t(1 - v), \qquad t' = \gamma(t - vx) = \gamma(t - vt) = \gamma t(1 - v).$$
> Hence $x' = t'$ — the ray is at $45^\circ$ in $S'$ too, with speed $x'/t' = 1 = c$. For the $-x$ direction, $x = -t$:
> $$x' = \gamma(-t - vt) = -\gamma t(1 + v), \qquad t' = \gamma(t + vt) = \gamma t(1 + v),$$
> so $x' = -t'$ — again at $45^\circ$ (the other diagonal), speed $c$. Both light lines map to themselves under the boost (they are the *eigendirections* of the boost matrix; see [[Ex - The k-calculus (Bondi) derivation|the k-calculus]], where they are the eigenvectors with eigenvalues $k^{\mp 1}$). So every inertial observer agrees the light lines are the two $45^\circ$ diagonals — the constancy of the speed of light, drawn.

**Step 3: The light cone is frame-independent.**

> [!note]- Derivation
> In $1+1$ dimensions, the light rays through the origin form the two lines $x = \pm ct$ — an "X" on the diagram, the boundary between the future/past (steeper than $45^\circ$) and the spacelike "elsewhere" (shallower). In $3+1$ dimensions, a light pulse emitted from the origin reaches, at time $t$, the sphere $x^2 + y^2 + z^2 = c^2 t^2$; the union over all $t$ is the **light cone**, the set
> $$\{(t, x, y, z) : x^2 + y^2 + z^2 = c^2 t^2\}.$$
> Because light travels at $c$ in *every* inertial frame (Step 2 in each spatial direction), every observer draws the *same* cone: the cone is the locus $\Delta s^2 = c^2 t^2 - x^2 - y^2 - z^2 = 0$, and this locus is preserved by every [[Def - The Lorentz Transformation|Lorentz transformation]] (a boost maps null separations to null separations). The frame-independence of the light cone is the geometric foundation of the invariant *causal structure*: all observers agree on which events lie on, inside, or outside the cone of a given event (see [[Ex - Why nothing can be drawn flatter than 45 degrees]]).

**Step 4: Transverse light keeps speed $c$ but aberrates in direction.**

> [!note]- Derivation
> In $S$, a pulse moves in $+y$: $x = 0$, $y = t$, $z = 0$ (so $|\mathbf{v}| = |dy/dt| = 1 = c$). Apply the boost along $x$:
> $$t' = \gamma(t - v\cdot 0) = \gamma t, \qquad x' = \gamma(0 - vt) = -\gamma v t, \qquad y' = y = t, \qquad z' = 0.$$
> In $S'$, express positions against $t'$: from $t' = \gamma t$, we have $t = t'/\gamma$, so
> $$x' = -\gamma v\cdot\frac{t'}{\gamma} = -v t', \qquad y' = \frac{t'}{\gamma}.$$
> The velocity components in $S'$ are $v_x' = dx'/dt' = -v$ (the pulse now drifts in $-x$, because $S'$ rushes in $+x$) and $v_y' = dy'/dt' = 1/\gamma$. The *speed* is
> $$|\mathbf{v}'| = \sqrt{v_x'^2 + v_y'^2} = \sqrt{v^2 + \frac{1}{\gamma^2}} = \sqrt{v^2 + (1 - v^2)} = \sqrt{1} = 1 = c,$$
> using $1/\gamma^2 = 1 - v^2$. So the pulse still travels at $c$ in $S'$, confirming the second postulate for transverse light — but its *direction* has changed: it now makes an angle $\theta'$ with the $y'$-axis where $\tan\theta' = |v_x'|/v_y' = v/(1/\gamma) = \gamma v$. This tilting of the light's direction under a boost is **relativistic aberration** (the same effect that shifts the apparent positions of stars due to the Earth's motion). The lesson: a boost changes light's *direction* but never its *speed*.

> [!note]- Complete formal solution
> Plotting $ct$ vertically makes a light ray $x = ct$ have slope $\Delta(ct)/\Delta x = 1$, a $45^\circ$ line; this realises the second postulate visually. Under the boost, $x = t \Rightarrow x' = \gamma t(1-v) = t'$ and $x = -t \Rightarrow x' = -t'$, so both light lines map to themselves — light is at $45^\circ$ in every frame (the light lines are the boost's eigendirections). The light cone $x^2 + y^2 + z^2 = c^2t^2$ is the locus $\Delta s^2 = 0$, preserved by every Lorentz transformation, hence frame-independent. For transverse light ($x=0$, $y=t$ in $S$): the boost gives $t' = \gamma t$, $x' = -\gamma vt$, $y' = t$, so $v_x' = -v$, $v_y' = 1/\gamma$, and $|\mathbf{v}'| = \sqrt{v^2 + 1/\gamma^2} = \sqrt{v^2 + (1-v^2)} = c$ — speed invariant, direction aberrated by $\tan\theta' = \gamma v$. $\blacksquare$

---

# Key Takeaways

**The $45^\circ$ light convention builds the second postulate into the diagram, and it is the reason the spacetime diagram works at all.** Choosing $ct$ for the vertical axis is not a cosmetic rescaling; it is what makes light's slope frame-independent ($= 1$ in every frame), so that the light lines become the fixed $45^\circ$ scaffolding shared by all inertial observers. Every other feature of the diagram — the tilted boosted axes, the calibration hyperbolae, the causal cone — is arranged relative to these light lines. The reusable recognition: when setting up coordinates for a problem with an invariant speed, rescale so that speed becomes $1$ (a $45^\circ$ slope, or a unit cone), which makes the invariance manifest and the geometry clean. This is the same impulse that motivates natural units $c = 1$ throughout relativity: putting the invariant speed at the center of the unit system makes the symmetry visible.

**Light directions are the eigendirections of the boost, which is why they map to themselves and why the $k$-factor governs the Doppler shift.** The computation $x = \pm t \Rightarrow x' = \pm t'$ shows the two light lines are *invariant* under the boost — they are the eigenvectors of the boost matrix (with eigenvalues $k$ and $k^{-1}$, the [[Ex - The k-calculus (Bondi) derivation|Bondi k-factors]]). This is the structural reason light's slope is frame-independent: a boost rescales light signals along $+x$ and compresses them along $-x$, but never tilts the null lines off $45^\circ$. The transferable insight: invariant subspaces of a transformation are physically privileged, and here the privileged subspace is the light cone — the boundary every observer agrees on. Diagonalising the boost on its null eigendirections is the cleanest route to the Doppler effect, velocity composition, and the whole structure of the [[Def - The Lorentz Group|Lorentz group]].

**Speed and direction transform differently under a boost: the speed of light is invariant, but its direction aberrates.** The transverse-light calculation isolates a subtle and important distinction. A boost along $x$ leaves the $y$-*coordinate* untouched ($y' = y$), so one might think $y$-light is unaffected — but the boost mixes $t$ and $x$, changing the *time* the pulse takes and thereby giving it an apparent $x$-velocity in $S'$. The total speed stays $c$ (the second postulate is robust), while the direction tilts by $\tan\theta' = \gamma v$ — relativistic aberration, the effect that makes stars appear shifted toward the direction of the Earth's motion and that concentrates a fast emitter's radiation into a forward cone (relativistic beaming). The general lesson for problem-solving: when boosting a velocity, never assume a transverse component is inert — compute all components against the *new* time coordinate, because the time transformation is what redistributes the velocity. Speed invariance holds only for light; for massive particles even the speed changes, via the full [[Thm - Relativistic Velocity Addition|velocity-addition law]].
