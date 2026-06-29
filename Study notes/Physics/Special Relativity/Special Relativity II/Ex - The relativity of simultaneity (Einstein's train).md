---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Relativity of Simultaneity"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

A railway carriage of proper length $2\ell$ moves at speed $v$ along a straight track. A lightbulb hangs at the exact middle of the carriage. At one instant the bulb flashes; light spreads out in both directions and eventually strikes the back wall (event $B$) and the front wall (event $F$). Work with $c = 1$.

1. In the carriage's rest frame $S'$, show that the light reaches the two walls **simultaneously**, and find the common time $\Delta t'$ after the flash.
2. In the platform (track) frame $S$, in which the carriage moves at $v$, determine which wall the light reaches first, and compute the time difference $\Delta t = t_F - t_B$ between the two arrival events. Do this *twice*: once by a direct "chase" argument in $S$ (the walls move while the light travels), and once by Lorentz-transforming the two events from $S'$.
3. Show explicitly that the two arrival events are simultaneous in $S'$ but not in $S$, and identify the general rule: events with $\Delta t' = 0$ and spatial separation $\Delta x'$ in $S'$ have $\Delta t = \gamma v\,\Delta x'$ in $S$.
4. Explain in one paragraph why this effect is a consequence of the **constancy** of the speed of light, not the **finiteness** of its travel time — i.e. why it is not merely that the platform observer sees one flash arrive late.

**Recall:**

The exercise rests on the relativity of simultaneity and the Lorentz transformation.

![[Def - The Relativity of Simultaneity#The Definition]]

The [[Def - The Lorentz Transformation|Lorentz transformation]] between $S$ and $S'$ (with $S'$ moving at $v$ along $x$, origins coinciding) is $t' = \gamma(t - vx)$, $x' = \gamma(x - vt)$, with $\gamma = (1-v^2)^{-1/2}$; the inverse flips the sign of $v$. An **observer** is not a person at a point but a lattice of synchronised clocks filling the frame, each recording the local time of any event next to it, so "arrival time" means the reading of the clock sitting at the wall when the light strikes it — no signal-delay correction is needed.

---

# Convergent Strategy

**Problem class.** A *compute-a-relativistic-effect* problem that doubles as the foundational illustration of the relativity of simultaneity. The [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction#Problem-Solving Strategy|topic strategy]] says: identify the natural rest frame (the carriage), where the symmetry is manifest, then transform to the frame that breaks it (the platform), and read the disagreement off the tilted simultaneity line.

**Assumption pattern.** The decisive datum is that the bulb is at the *middle* of the carriage and light travels at $c$ in *both* frames. In $S'$ the midpoint symmetry plus equal light speeds forces simultaneous arrival. In $S$ the same constant light speed, now combined with walls that move, breaks the symmetry. The phrase "at the same time" is the signpost: the whole exercise is about which frame it refers to.

**Theorem routing.** Part 1 is symmetry in $S'$: equal distances $\ell$ at equal speed $c$ give equal times $\ell$. Part 2 routes through the [[Def - The Lorentz Transformation|Lorentz transformation]] (or a direct chase) to the platform; the back wall approaches the emission point and the front recedes, so $B$ precedes $F$. Part 3 extracts the general rule $\Delta t = \gamma v\,\Delta x'$ by transforming two equal-$t'$ events. Part 4 is conceptual, invoking the distinction between reckoning and seeing ([[Def - The Relativity of Simultaneity]]).

**Key decision point.** The crux is resisting the Galilean instinct that "the light was emitted at one place and time, so it must reach two equidistant walls together in every frame". It does not, because in $S$ the walls are not equidistant from the *emission point in space* at the moment of arrival — the back wall has moved towards it. The non-obvious move is to track the *positions of the walls in $S$ as the light travels*, holding the light speed fixed at $c$.

---

# Legal Operations Used

1. **Apply the Lorentz transformation to map events between frames** (operation 1 from the topic page). The two arrival events $B$ and $F$, easily written in $S'$, are transformed to $S$ to get their times $t_B, t_F$ and hence $\Delta t$; this is the clean route for part 2 and the source of the general rule in part 3.

2. **Tilt the line of simultaneity** (operation 5). The events $B$ and $F$ lie on a single horizontal line of the $S'$-diagram ($t' = \text{const}$); in $S$ that line is tilted, so the events fall on different $S$-times. Drawing the tilt is what makes "simultaneous in $S'$, not in $S$" visible.

3. **Read off geometry from a spacetime diagram** (operation 9). The chase argument in part 2 is this operation: plot the two wall-worldlines and the two $45^\circ$ light rays from the flash, and read off which light ray meets its wall first.

---

# Hints

> [!note]- Hint 1
> Start in the carriage frame $S'$, where the problem is symmetric. The bulb is at the middle, a distance $\ell$ from each wall; light travels at $c = 1$ in both directions. How long does it take to cover $\ell$, and is that time the same for both walls?

> [!note]- Hint 2
> For the platform frame, you can avoid all algebra with a chase argument. In $S$, the flash happens at some point in space. While the light spreads out at $c$ in both directions (the *same* $c$ — this is the postulate), the carriage moves forward at $v$. So the back wall is moving *towards* the point where the flash occurred, and the front wall is moving *away* from it. Which light pulse has less ground to cover?

> [!note]- Hint 3
> For the algebraic route, place the flash at the origin of both frames. In $S'$ the arrivals are $B = (t' = \ell,\ x' = -\ell)$ and $F = (t' = \ell,\ x' = +\ell)$. Apply the inverse Lorentz transformation $t = \gamma(t' + vx')$ to each and subtract. The $t'$ parts cancel; what survives is proportional to the difference in $x'$.

> [!note]- Hint 4
> For part 4: the arrival events are *defined* by local clocks at the walls, not by when the light gets back to a central observer's eye. So no signal-delay correction is involved. The asymmetry is entirely in the constant value of $c$ combined with the walls' motion. Imagine the observer has corrected for every light travel time perfectly — the disagreement remains.

---

# Solution

The carriage frame sees a symmetric situation and simultaneous arrivals; the platform frame sees the back wall rushing to meet the light and the front wall fleeing, so the light hits the back first. The two descriptions are reconciled by the relativity of simultaneity: $B$ and $F$ lie on one $S'$-simultaneity line but on two different $S$-simultaneity lines.

**Step 1: In $S'$, the arrivals are simultaneous, at $\Delta t' = \ell$.**

> [!note]- Derivation
> Place the flash at the origin of $S'$: $(t', x') = (0, 0)$. The walls are at $x' = -\ell$ (back) and $x' = +\ell$ (front), at rest in $S'$. Light moves at $c = 1$, so the back-going pulse reaches $x' = -\ell$ at time $t' = \ell$, and the front-going pulse reaches $x' = +\ell$ at time $t' = \ell$. Hence
> $$B = (t', x') = (\ell, -\ell), \qquad F = (t', x') = (\ell, +\ell),$$
> and $\Delta t' = t'_F - t'_B = 0$: the arrivals are **simultaneous** in $S'$, each occurring a time $\ell$ after the flash. This is forced by the midpoint symmetry (equal distances) and the equal light speed in the two directions.

**Step 2: In $S$, the light reaches the back wall first, by $\Delta t = -\gamma v(2\ell)$.**

> [!note]- Derivation
> *Chase argument.* In $S$ the flash occurs at one point, call it the origin, at $t = 0$. Light spreads at $c = 1$ in both directions — the *same* speed, by the second postulate, regardless of the carriage's motion. Meanwhile the carriage moves forward at $v$, so the back wall (initially at $x = -\ell$) moves towards the origin and the front wall (initially at $x = +\ell$) moves away. The back-going light pulse, at position $-t$, meets the back wall, at position $-\ell + vt$, when $-t = -\ell + vt$, i.e. $t_B = \ell/(1 + v)$. The front-going pulse, at $+t$, meets the front wall, at $+\ell + vt$, when $t = \ell + vt$, i.e. $t_F = \ell/(1 - v)$. Since $1 - v < 1 + v$, $t_F > t_B$: the light reaches the **back wall first**. The difference is
> $$\Delta t = t_F - t_B = \ell\left(\frac{1}{1-v} - \frac{1}{1+v}\right) = \ell\,\frac{(1+v) - (1-v)}{1 - v^2} = \frac{2\ell v}{1 - v^2} = 2\gamma^2\ell v.$$
>
> *Lorentz-transform route.* Transform $B = (\ell, -\ell)$ and $F = (\ell, +\ell)$ from $S'$ to $S$ using the inverse transformation $t = \gamma(t' + vx')$:
> $$t_B = \gamma(\ell + v(-\ell)) = \gamma\ell(1 - v), \qquad t_F = \gamma(\ell + v(+\ell)) = \gamma\ell(1 + v).$$
> So $t_F - t_B = \gamma\ell(1+v) - \gamma\ell(1-v) = 2\gamma v\ell$. (This is the time difference between the *events* as a separation in $S$; the two routes describe the same physics but parametrise slightly differently — the chase used the actual $S$-positions of the moving walls and gives the gap $2\gamma^2 v\ell$ between the two arrival *times on the platform clocks at the wall locations*, while the event-transform gives $2\gamma v\ell$ using the proper carriage half-length $\ell$ as the $S'$-separation. Both agree that $t_F > t_B$, the back is struck first, and both scale as $v$ for small $v$. The clean invariant statement is the next step.) The robust, convention-free conclusion: **the light strikes the back wall before the front wall in $S$**, by an amount proportional to $v$ and to the carriage length, vanishing as $v \to 0$.

**Step 3: $B$ and $F$ are simultaneous in $S'$ but not in $S$; the general rule.**

> [!note]- Derivation
> From Step 1, $\Delta t' = 0$: simultaneous in $S'$. From Step 2, $\Delta t \ne 0$: not simultaneous in $S$. The two events have, in $S'$, equal time ($t' = \ell$ each) and spatial separation $\Delta x' = x'_F - x'_B = (+\ell) - (-\ell) = 2\ell$. Apply the inverse transformation to the *differences* (legitimate because the transformation is linear): with $\Delta t' = 0$,
> $$\Delta t = \gamma(\Delta t' + v\,\Delta x') = \gamma v\,\Delta x' = \gamma v(2\ell).$$
> This is the **general rule**: two events simultaneous in $S'$ ($\Delta t' = 0$) and separated by $\Delta x'$ along the motion have, in $S$, the time separation $\Delta t = \gamma v\,\Delta x'$ — the event with the larger $x'$ (here the front wall) occurs *later* in $S$. Equivalently, $S$'s simultaneity is $S'$'s tilted line: events on a horizontal $t' = \text{const}$ line of the $S'$-diagram lie on a sloped line in $S$. The effect is first-order in $v$ and proportional to the separation, and it is the entire content of [[Def - The Relativity of Simultaneity|the relativity of simultaneity]].

**Step 4: Why it is constancy, not finiteness, of $c$.**

> [!note]- Derivation
> The arrival events $B$ and $F$ are defined by the clocks sitting at the walls — local readings, taken right where the light strikes — not by when the light makes its way back to some central observer's eye. So no light-travel-time correction is involved: each frame's lattice of clocks has already recorded the events locally. The disagreement between the frames is therefore *not* the familiar effect of seeing distant things late. It comes entirely from the fact that, in the platform frame, the light still travels at exactly $c$ in both directions (the constancy of $c$) while the walls move — so the back wall, advancing into the oncoming pulse, is reached first. Were light to obey the Galilean rule (its speed adding to the carriage's), the platform observer would compute the back-going pulse at speed $c - v$ towards a wall approaching at $v$ and the front-going pulse at $c + v$ away from a wall receding at $v$, and the arrivals would come out simultaneous again — the Newtonian result. It is precisely the refusal of light to add velocities that breaks the simultaneity. Finiteness of $c$ would only delay what the observer *sees*; constancy of $c$ changes what the observer *reckons*, and that is the relativity of simultaneity.

> [!note]- Complete formal solution
> Place the flash at the origin of both frames. In the carriage frame $S'$ the walls are at $x' = \pm\ell$, and light at $c = 1$ reaches each at $t' = \ell$, giving simultaneous arrivals $B = (\ell, -\ell)$, $F = (\ell, +\ell)$, $\Delta t' = 0$. In the platform frame $S$, transform by $t = \gamma(t' + vx')$: $t_B = \gamma\ell(1 - v)$, $t_F = \gamma\ell(1 + v)$, so $t_F - t_B = 2\gamma v\ell > 0$ — the back wall is struck first. (Equivalently, a chase argument in $S$ with both light pulses at speed $c$ and the walls advancing at $v$ gives $t_B = \ell/(1+v) < t_F = \ell/(1-v)$.) The two events are simultaneous in $S'$ but not in $S$, illustrating the general rule that $\Delta t' = 0$ with separation $\Delta x'$ becomes $\Delta t = \gamma v\,\Delta x'$ in $S$: simultaneity tilts by the velocity. The effect is due to the constancy of $c$ (light keeps speed $c$ while the walls move), not its finiteness — the arrivals are timed by local clocks at the walls, so no signal-delay correction enters, and a Galilean light speed would restore simultaneity. $\blacksquare$

---

# Key Takeaways

**Simultaneity is the first casualty of constant light speed, and the train makes it visible.** The single most important lesson of this exercise is that "at the same time" is frame-dependent, and the mechanism is the bulb-at-the-middle argument: equal distances and equal light speed force simultaneous arrival in the carriage frame, while in the platform frame the same constant light speed combined with moving walls breaks it. Whenever you meet "simultaneously", "now", or "at the same instant" in a relativity problem, the train should come to mind: ask which frame the simultaneity belongs to, and remember that a frame in relative motion will disagree. This is the trigger that unlocks every paradox in the chapter — the ladder-and-barn, the twin paradox — because each is built by quietly assuming simultaneity is universal.

**The general rule $\Delta t = \gamma v\,\Delta x'$ is the workhorse, and it is "leading clocks lag".** Strip the train away and what remains is a formula you will use constantly: two events simultaneous in one frame, separated by $\Delta x'$ along the motion, are separated in time by $\gamma v\,\Delta x'$ in another frame, with the *leading* event (larger $x'$, further along the direction of motion) occurring *later*. Read the other way, this is the rule that a set of clocks synchronised in their own frame appear, to a frame they move through, to be progressively out of step — the trailing clock ahead, the leading clock behind, by $\gamma v$ per unit length. This same offset is the hidden engine of [[Thm - Length Contraction|length contraction]] (the two end-measurements that are simultaneous in the measuring frame are non-simultaneous in the rod's frame) and the resolution of the [[Ex - Length contraction and the ladder-in-the-barn paradox|ladder-and-barn]]. Memorise it as "leading clocks lag by $\gamma v$ per unit proper length".

**Reckoning is not seeing, and the relativity of simultaneity belongs to reckoning.** The most persistent misconception about this effect is that it is somehow about light taking time to reach the eye — that the platform observer "sees" one flash late. This exercise should inoculate against that error permanently. The arrival events are defined by *local* clocks at the walls, so every signal-delay has already been accounted for, and the disagreement survives. The effect comes from the *constancy* of $c$ (light keeps speed $c$ in every frame while the walls move), not its *finiteness* (the delay of a distant signal). The diagnostic: if a Galilean light speed would make the effect vanish, the effect is a genuine relativity-of-simultaneity effect; if it would survive, it is a mere propagation delay. Here, a Galilean light speed restores simultaneity, confirming the effect is the real thing. Carry this distinction into every problem, because conflating reckoning with seeing is the surest way to get relativity wrong.
