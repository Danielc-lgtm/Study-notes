---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Spacetime Diagram"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

On a [[Def - Spacetime Diagram|spacetime diagram]] drawn in frame $S$ (time $ct$ vertical, $x$ horizontal, $c = 1$), a second inertial frame $S'$ moves at velocity $v$ along $x$. Determine, from the [[Def - The Lorentz Transformation|Lorentz transformation]], how $S'$'s coordinate axes appear.

1. **The $ct'$-axis.** Find the equation, in $S$-coordinates, of the locus $x' = 0$ (the worldline of the $S'$ spatial origin). State its slope and the angle it makes with the vertical.
2. **The $x'$-axis.** Find the equation, in $S$-coordinates, of the locus $t' = 0$ (the events $S'$ calls simultaneous with its origin). State its slope and the angle it makes with the horizontal.
3. **The scissoring.** Show that the two axes tilt *symmetrically toward the $45^\circ$ light line* by the same angle $\alpha = \arctan v$, and explain why this symmetry is exactly the second postulate.
4. **Pseudo-orthogonality and the relativity of simultaneity.** Show the $S'$ axes are pseudo-orthogonal (the angles they make with the horizontal are $\alpha$ and $\pi/2 - \alpha$, not $\alpha$ and $\pi/2 + \alpha$), and use the tilt of the $x'$-axis to explain why two events simultaneous in $S'$ are generally not simultaneous in $S$.

**Recall:**

![[Def - Spacetime Diagram#The Definition]]

The relevant transformation is the [[Def - The Lorentz Transformation|Lorentz boost]] $x' = \gamma(x - vt)$, $t' = \gamma(t - vx)$ (with $c = 1$). Slopes are measured as $\Delta(ct)/\Delta x$ from the horizontal $x$-axis; a $45^\circ$ light line $x = ct$ has slope $1$.

---

# Convergent Strategy

**Problem class.** This is a *geometric-from-algebraic* problem: extract the visual structure of the spacetime diagram (where the boosted axes lie) by reading loci off the [[Def - The Lorentz Transformation|Lorentz transformation]]. The [[Special Relativity I — Postulates and Lorentz Transformations#Problem-Solving Strategy|topic strategy]] insists the diagram be a mnemonic for the algebra; this exercise builds the diagram *from* the algebra so the picture is trustworthy.

**Assumption pattern.** The only input is the boost. The two axes are defined by *coordinate conditions* in $S'$ — the $ct'$-axis is "$x' = 0$" and the $x'$-axis is "$t' = 0$" — and the recognition is that each condition, pushed through the transformation, becomes a *line in $S$* whose slope is immediate. The symmetry of the two slopes about the light line is the geometric content of the second postulate.

**Theorem routing.** Set each coordinate condition to zero and solve for the $S$-line: $x' = 0 \Rightarrow x = vt$ (the $ct'$-axis); $t' = 0 \Rightarrow t = vx$ (the $x'$-axis). Compare slopes ($1/v$ from vertical, $v$ from horizontal) and observe they are reflections of each other across slope $1$ — the $45^\circ$ light line.

**Key decision point.** The subtle point is recognising that the $x'$-axis is a line of *simultaneity*, not a worldline, and that its tilt is the geometric face of relative simultaneity. A reader who finds the slope but reads the $x'$-axis as "where $S'$ goes" misses the meaning. The productive interpretation: the $x'$-axis is the set $\{t' = 0\}$, the events $S'$ stamps with the same time; its being tilted relative to the horizontal $\{t = 0\}$ means $S$ and $S'$ disagree about which events are simultaneous.

---

# Legal Operations Used

1. **Operation 1 from the topic page (apply the Lorentz transformation).** Each axis is obtained by imposing a coordinate condition ($x' = 0$ or $t' = 0$) in the boost and solving for the $S$-locus.

2. **Operation 6 from the topic page (read geometry off a spacetime diagram).** The whole exercise is this operation made rigorous: the diagram's structure is derived rather than asserted.

3. **Operation 8 from the topic page (use the $45^\circ$ light structure).** The light line at slope $1$ is the axis of symmetry about which the boosted axes scissor.

---

# Hints

> [!note]- Hint 1
> The $ct'$-axis is where $x' = 0$. From $x' = \gamma(x - vt) = 0$, this is $x = vt$. As a line in the $(x, ct)$ plane with $c = 1$, that is $ct = x/v$ — slope $1/v$ (steeper than $45^\circ$ since $v < 1$).

> [!note]- Hint 2
> The $x'$-axis is where $t' = 0$. From $t' = \gamma(t - vx) = 0$, this is $t = vx$, i.e. $ct = vx$ — slope $v$ (shallower than $45^\circ$).

> [!note]- Hint 3
> Slope $1/v$ (the $ct'$-axis) and slope $v$ (the $x'$-axis) are reflections of each other across slope $1$: if you reflect a line of slope $m$ across the $45^\circ$ line, you get slope $1/m$. The $45^\circ$ light line is the mirror, and that mirror symmetry *is* light having the same speed in both frames.

> [!note]- Hint 4
> The $ct'$-axis makes angle $\arctan(1/v)$ with the horizontal, i.e. $\pi/2 - \arctan v$; the $x'$-axis makes $\arctan v$. So the two axes make angles $\alpha$ and $\pi/2 - \alpha$ with the horizontal, with $\alpha = \arctan v$ — they close up toward the diagonal, unlike perpendicular Euclidean axes.

---

# Solution

Each $S'$ axis is a coordinate locus pushed through the boost: $x' = 0$ gives the $ct'$-axis $ct = x/v$ (Step 1), $t' = 0$ gives the $x'$-axis $ct = vx$ (Step 2). Their slopes $1/v$ and $v$ are mirror images across the $45^\circ$ light line, so the axes scissor symmetrically toward it (Step 3) — pseudo-orthogonally, which is why simultaneity is frame-dependent (Step 4).

**Step 1: The $ct'$-axis is $ct = x/v$, slope $1/v$, tilted $\alpha = \arctan v$ off the vertical.**

> [!note]- Derivation
> The $ct'$-axis is the time axis of $S'$ — the set of events with $x' = 0$, which is the worldline of the $S'$ spatial origin. From the boost,
> $$x' = \gamma(x - vt) = 0 \quad\Longleftrightarrow\quad x = vt.$$
> In the $(x, ct)$ plane with $c = 1$, $x = vt$ is the line $ct = x/v$, of slope (rise over run) $\Delta(ct)/\Delta x = 1/v$. Since $0 < v < 1$, the slope $1/v > 1$: the $ct'$-axis is *steeper* than the $45^\circ$ light line. It makes angle $\arctan(1/v)$ with the horizontal, equivalently it is tilted off the *vertical* by
> $$\alpha = \tfrac{\pi}{2} - \arctan(1/v) = \arctan v.$$
> Physically this is just the worldline of an object moving at $v$ — steeper than light, as every massive worldline must be.

**Step 2: The $x'$-axis is $ct = vx$, slope $v$, tilted $\alpha = \arctan v$ off the horizontal.**

> [!note]- Derivation
> The $x'$-axis is the space axis of $S'$ — the set of events $S'$ calls simultaneous with its origin, i.e. $t' = 0$. From the boost,
> $$t' = \gamma(t - vx) = 0 \quad\Longleftrightarrow\quad t = vx.$$
> In the $(x, ct)$ plane this is $ct = vx$, of slope $\Delta(ct)/\Delta x = v$. Since $v < 1$, the slope is *shallower* than the $45^\circ$ light line. It makes angle
> $$\alpha = \arctan v$$
> with the *horizontal* $x$-axis. Note: this line is a line of *simultaneity*, not a worldline — it is where $S'$ stamps the time $t' = 0$, not where anything travels.

**Step 3: The axes scissor symmetrically toward the light line; symmetry = second postulate.**

> [!note]- Derivation
> The $ct'$-axis has slope $1/v$; the $x'$-axis has slope $v$. These are reciprocals, and reflecting a line of slope $m$ across the $45^\circ$ line (slope $1$) produces a line of slope $1/m$ (the reflection swaps the roles of the $x$- and $ct$-axes). Hence the $ct'$-axis and the $x'$-axis are *mirror images of each other across the $45^\circ$ light line*. Equivalently, the $ct'$-axis tilts down toward the light line from the vertical by $\alpha = \arctan v$, and the $x'$-axis tilts up toward the light line from the horizontal by the *same* $\alpha$ — they close like a pair of scissors blades onto the diagonal.
>
> This symmetry is *exactly the second postulate*. A light ray has $x = ct$ (slope $1$) in $S$, and by the constancy of light it has $x' = ct'$ (slope $1$) in $S'$ too — the *same* $45^\circ$ line is the light line in both frames. For a line to be the bisector of the angle between the $x'$- and $ct'$-axes (so that it is "speed $1$" in $S'$), the two axes must be symmetric about it. So the scissoring symmetry about the $45^\circ$ line is the geometric statement that light has the same speed in both frames. (In contrast, a [[Def - Galilean Spacetime and Its Failure|Galilean]] boost tilts only the time axis — the $ct'$-axis — while leaving the $x'$-axis horizontal: "now" is shared, only "here" tilts.)

**Step 4: Pseudo-orthogonality; the tilted $x'$-axis is the relativity of simultaneity.**

> [!note]- Derivation
> *Pseudo-orthogonality.* The $x'$-axis makes angle $\alpha = \arctan v$ with the horizontal; the $ct'$-axis makes angle $\arctan(1/v) = \pi/2 - \alpha$ with the horizontal. So the two $S'$ axes subtend angles $\alpha$ and $\pi/2 - \alpha$ with the horizontal — they make an angle of $(\pi/2 - \alpha) - \alpha = \pi/2 - 2\alpha$ *with each other*, which is *less* than a right angle. Ordinary Euclidean perpendicular axes would make angles $\alpha$ and $\pi/2 + \alpha$ (angle $\pi/2$ between them). The $S'$ axes instead close up toward the diagonal — this is **pseudo-orthogonality**, the Minkowski analogue of perpendicularity, with the light line (at $\alpha = \pi/4$) pseudo-orthogonal to *itself*. (Pseudo-orthogonality means $\eta$-orthogonality: the $x'$- and $ct'$-axis directions satisfy $\eta(e_{x'}, e_{ct'}) = 0$ with the indefinite metric, even though they are not Euclidean-perpendicular on the page.)
>
> *Relativity of simultaneity.* The $x'$-axis is the locus $t' = 0$ — the events $S'$ calls simultaneous with its origin. In $S$, this is the *tilted* line $ct = vx$, not the horizontal line $ct = 0$ (which is $\{t = 0\}$, the events $S$ calls simultaneous). So the set of events $S'$ deems simultaneous is *different* from the set $S$ deems simultaneous: two events on the $x'$-axis (same $t'$) have *different* $t$ in $S$ (they are at different heights on the diagram). Concretely, two events at $(x_1, ct = vx_1)$ and $(x_2, ct = vx_2)$ with $x_1 \ne x_2$ are simultaneous in $S'$ but occur at $S$-times $vx_1 \ne vx_2$. The tilt of the $x'$-axis *is* the relativity of simultaneity, read directly off the diagram. In [[Def - Galilean Spacetime and Its Failure|Galilean spacetime]] the $x'$-axis would stay horizontal (no tilt), and simultaneity would be absolute; the tilt, of slope $v$, is precisely the position-dependent term $vx$ in the clock equation $t' = \gamma(t - vx)$.

> [!note]- Complete formal solution
> From the boost $x' = \gamma(x - vt)$, $t' = \gamma(t - vx)$: the $ct'$-axis ($x' = 0$) is $x = vt$, i.e. $ct = x/v$, slope $1/v$, tilted $\alpha = \arctan v$ off the vertical; the $x'$-axis ($t' = 0$) is $t = vx$, i.e. $ct = vx$, slope $v$, tilted $\alpha = \arctan v$ off the horizontal. The slopes $1/v$ and $v$ are reciprocal, hence mirror images across the $45^\circ$ light line, so the axes scissor symmetrically toward it; this symmetry is the second postulate (light is slope $1$ — the bisector of the $S'$ axes — in both frames). The axes make angles $\alpha$ and $\pi/2 - \alpha$ with the horizontal, so they are pseudo-orthogonal (closing toward the diagonal). The $x'$-axis being tilted (slope $v$, versus the horizontal $\{t=0\}$) means events simultaneous in $S'$ (same $t'$) occur at different $S$-times $t = vx$ — the relativity of simultaneity. $\blacksquare$

> [!warning] Illegal but tempting: reading lengths and angles with a Euclidean ruler
> It is tempting to measure the angle between the $S'$ axes on the page and call it physical, or to mark equal lengths along the $x$- and $x'$-axes with a ruler. This is wrong: the page is Euclidean but the geometry is Minkowskian. The physical "angle" between axes is governed by the indefinite metric $\eta$ (they are $\eta$-orthogonal despite looking acute on paper), and equal *interval* lengths along the $x$- and $x'$-axes appear *unequal* on the page — the $S'$ unit is calibrated by the hyperbola $x^2 - (ct)^2 = 1$, not by a ruler. The diagram faithfully shows *which* events are which and *which* lines are simultaneity/worldlines, but Euclidean measurements on the paper are not the physical interval — for that, compute $\Delta s^2$.

---

# Key Takeaways

**The boosted axes are coordinate loci, and reading them off the transformation makes the diagram a derived, trustworthy object rather than a vague picture.** The reusable method is to define each axis by a *coordinate condition* and push it through the [[Def - The Lorentz Transformation|Lorentz transformation]]: the time axis of $S'$ is "$x' = 0$", the space axis is "$t' = 0$", and each condition becomes an explicit line in $S$ with a computable slope. This is the disciplined antidote to hand-wavy diagram-reading — every line on a spacetime diagram should be traceable to such a condition. The trigger to apply it: any time you need to know where a moving frame's axes, simultaneity lines, or constant-position lines sit, write the defining coordinate condition and solve. The same method places calibration hyperbolae (constant interval), light cones (constant $\Delta s^2 = 0$), and worldlines (constant velocity) — the entire furniture of the diagram is coordinate conditions pushed through the boost.

**The scissoring of the axes toward the $45^\circ$ light line *is* the constancy of the speed of light, made visual.** The deepest content is that the symmetry of the two boosted axes about the diagonal is not an artistic convention but a theorem: light must be the angle-bisector of the $x'$- and $ct'$-axes precisely because it has slope $1$ (speed $c$) in $S'$ as in $S$. This single picture encodes the second postulate, and it is why the diagram is *the* diagnostic tool of the subject. The transferable recognition: in [[Def - Galilean Spacetime and Its Failure|Galilean]] spacetime only the time axis tilts (the $x'$-axis stays horizontal), so "now" is shared and only "here" is relative; in Minkowski spacetime *both* axes tilt, symmetrically, and the extra tilt of the space axis is the relativity of simultaneity. Whenever you draw two frames, draw the light line first and arrange the axes symmetrically about it — that enforces the second postulate automatically and prevents the most common diagram errors.

**Pseudo-orthogonality replaces perpendicularity, and the tilted simultaneity axis is the geometric source of relative simultaneity — the master key to relativistic paradoxes.** The $S'$ axes are not Euclidean-perpendicular on the page; they are $\eta$-orthogonal, closing toward the diagonal (angles $\alpha$ and $\pi/2 - \alpha$), with the light line self-orthogonal. This is the visual signature of the indefinite metric, and it warns that page-distances and page-angles are not physical — only the interval $\Delta s^2$ is. More importantly, the tilt of the $x'$-axis is the relativity of simultaneity in geometric form: "$S'$'s now" is a different line from "$S$'s now", so the two frames disagree about simultaneous events. This is the picture that resolves every relativistic paradox — the twin paradox (the traveller's now-line swings at turnaround, sweeping a chunk of the stay-at-home's worldline), the ladder-and-barn (the two ends are "simultaneously inside" in one frame's slicing, not the other's). The diagnostic habit: when an argument invokes "at the same time", draw the relevant simultaneity line as a *tilted* $x'$-axis and watch the apparent contradiction become a disagreement about slicing.
