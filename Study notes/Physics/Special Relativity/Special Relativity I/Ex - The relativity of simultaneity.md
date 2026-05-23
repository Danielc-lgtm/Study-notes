---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - Inertial Frame and the Postulates of Special Relativity"
  - "Def - The Spacetime Interval"
tags: [physics, special-relativity]
---

# Problem Statement

Working with $c = 1$, with $S'$ moving at velocity $v$ along the $x$-axis of $S$:

1. Show that two events $P_1$ and $P_2$ that are **simultaneous in $S$** (equal $t$) but at different places (different $x$) are **not simultaneous in $S'$**, and find the time difference $\Delta t'$ between them in $S'$.
2. Show that the set of events $S$ calls "simultaneous with the origin" ($t = 0$) and the set $S'$ calls so ($t' = 0$) are *different* lines in the spacetime diagram, and find the slope of each. These are the **lines of simultaneity**.
3. **The train gedankenexperiment.** A lightbulb hangs at the midpoint of a moving train carriage. The bulb flashes. A passenger on the train says the light reaches the front and back walls *at the same time*. A person on the platform says it reaches the back wall *first*. Show both are correct, and that the disagreement is forced by the constancy of the speed of light.

**Recall:**

The relativity of simultaneity is the direct consequence of the $t' = \gamma(t - vx)$ clause of the Lorentz transformation.

![[Def - The Lorentz Transformation#The Definition]]

Two events are **simultaneous in a frame** when they have equal time coordinate in that frame. By [[Def - Inertial Frame and the Postulates of Special Relativity|Postulate 2]], light travels at speed $1$ in every frame. The [[Def - The Spacetime Interval|spacetime interval]] $\Delta s^2 = \Delta t^2 - \Delta x^2$ classifies a separation: $\Delta s^2 < 0$ is **spacelike**, and the time-ordering of spacelike-separated events is frame-dependent.

---

# Convergent Strategy

**Problem class.** A *resolve-a-paradox* and *establish-a-structural-fact* problem. The [[Special Relativity I — Lorentz Transformations and Minkowski Space#Problem-Solving Strategy|topic strategy]] flags simultaneity as the single concept underlying every relativistic paradox.

**Assumption pattern.** Two events with a known relation in one frame (equal $t$, different $x$) are given; the question is their relation in the other frame. The signpost is the phrase "at the same time" — which demands the question "in which frame?"

**Theorem routing.** Part 1: apply $t' = \gamma(t - vx)$ to both events and subtract; the equal-$t$ terms cancel, leaving $\Delta t' = -\gamma v\,\Delta x \ne 0$. Part 2: lines of constant $t$ are horizontal; lines of constant $t'$ satisfy $t - vx = \text{const}$, slope $v$. Part 3: track the light from the bulb in each frame; constancy of $c$ plus the motion of the walls produces the disagreement.

**Key decision point.** The non-obvious realisation is that simultaneity is not a property of a pair of events but of a pair *together with a frame*. The $t' = \gamma(t-vx)$ term — the part of the Lorentz transformation that mixes $x$ into $t'$ — is the entire source of the effect; an observer at larger $x$ has their clocks "offset" relative to $S$.

---

# Legal Operations Used

1. **Apply the Lorentz transformation** to two events and subtract, isolating $\Delta t'$.

2. **Read off geometry from a spacetime diagram.** Part 2 is the operation "draw the lines of simultaneity and find their slopes".

3. **Classify a separation by the sign of its norm.** $P_1, P_2$ are spacelike separated, which is *why* their order can be frame-dependent.

4. **Track which frame's simultaneity is in play.** Part 3 is this operation applied to the two arrivals of light at the carriage walls.

---

# Hints

> [!note]- Hint 1
> Let $P_1 = (t, x_1)$ and $P_2 = (t, x_2)$ — same $t$, so simultaneous in $S$. Apply $t' = \gamma(t - vx)$ to each. Subtract: the $\gamma t$ terms cancel, and you are left with $\Delta t' = t_2' - t_1' = -\gamma v(x_2 - x_1)$.

> [!note]- Hint 2
> Lines of constant $t$ in the $(t,x)$ diagram are horizontal. Lines of constant $t'$ satisfy $t' = \gamma(t - vx) = \text{const}$, i.e. $t - vx = \text{const}$, i.e. $t = vx + \text{const}$ — a line of slope $v$. The two families of "simultaneous" lines are tilted relative to each other by an angle depending on $v$.

> [!note]- Hint 3
> In the train (carriage) frame the bulb is at the midpoint and the walls are equidistant and stationary; light travels at $c$ both ways and arrives at both walls at once. In the platform frame the light still travels at $c$ both ways (Postulate 2!), but the back wall is *rushing towards* the point where the flash occurred while the front wall is *receding* — so the light meets the back wall first. The whole effect comes from the walls moving while the light speed stays fixed.

---

# Solution

Simultaneity is not absolute: whether two events happen "at the same time" depends on the frame, and the dependence is forced by the constancy of the speed of light. The $t' = \gamma(t - vx)$ clause of the Lorentz transformation is the algebraic carrier of the effect.

**Step 1: Events simultaneous in $S$ are not simultaneous in $S'$.**

> [!note]- Derivation
> Let $P_1$ and $P_2$ be simultaneous in $S$: $P_1 = (t, x_1)$, $P_2 = (t, x_2)$, same $t$, with $x_1 \ne x_2$. Apply the [[Def - The Lorentz Transformation|Lorentz transformation]] $t' = \gamma(t - vx)$ to each:
> $$t_1' = \gamma(t - v x_1), \qquad t_2' = \gamma(t - v x_2).$$
> Subtract:
> $$\Delta t' = t_2' - t_1' = \gamma\big[(t - vx_2) - (t - vx_1)\big] = -\gamma v\,(x_2 - x_1) = -\gamma v\,\Delta x.$$
> Since $v \ne 0$ and $\Delta x \ne 0$, we have $\Delta t' \ne 0$: **the two events are not simultaneous in $S'$.** The event at larger $x$ occurs *earlier* in $S'$ (if $v > 0$). Two events that an $S$-observer insists happen "at the same moment" are, to an $S'$-observer, separated in time by $\gamma v\,\Delta x$. Simultaneity is frame-dependent.
>
> Note also that $P_1, P_2$ are **spacelike separated**: $\Delta t = 0$ in $S$, so $\Delta s^2 = 0 - \Delta x^2 = -\Delta x^2 < 0$. The frame-dependence of their order is consistent with — indeed required by — the [[Def - Classification of Four-Vectors|classification]]: only timelike-separated events have a frame-independent order.

**Step 2: The lines of simultaneity are tilted.**

> [!note]- Derivation
> On a spacetime diagram with $t$ vertical and $x$ horizontal:
>
> *$S$'s simultaneity lines* are the loci $t = \text{const}$ — **horizontal lines**, slope $0$.
>
> *$S'$'s simultaneity lines* are the loci $t' = \text{const}$. Since $t' = \gamma(t - vx)$, the condition $t' = \text{const}$ is $t - vx = \text{const}$, i.e.
> $$t = vx + \text{const} \quad\Longrightarrow\quad \text{slope } v.$$
> So $S'$'s lines of simultaneity are tilted at slope $v$ relative to $S$'s horizontal ones. (The $t'$-axis itself, $x' = 0$, is the line $x = vt$, of slope $1/v$.) The $x'$-axis and $t'$-axis "scissor" symmetrically towards the $45^\circ$ light ray — the symmetry being the geometric expression of the constancy of $c$.
>
> The picture makes the relativity of simultaneity *visible*: a horizontal $S$-slice and a tilted $S'$-slice through the same spacetime are different sets of events. There is no frame-independent "now".

**Step 3: The train gedankenexperiment.**

> [!note]- Derivation
> A lightbulb hangs at the midpoint $M$ of a train carriage; the carriage moves at velocity $v$. At one event the bulb flashes. Let $F$ be the event "light reaches the front wall" and $B$ the event "light reaches the back wall".
>
> *Carriage frame.* The bulb is equidistant from the two walls, and the walls are at rest. Light travels outward at speed $1$ in both directions (Postulate 2). Equal distances at equal speed take equal time: $F$ and $B$ are **simultaneous** in the carriage frame. The passenger is correct.
>
> *Platform frame.* By Postulate 2, the light *still* travels at speed $1$ in each direction — the same $c$, regardless of the train's motion. But now the walls are moving. While the light is in flight, the back wall *advances towards* the point in space where the flash occurred, and the front wall *recedes from* it. The leftward-going light therefore has a shorter distance to cover and the rightward-going light a longer one. Equal speed, unequal distance: the light reaches the *back wall first*. Event $B$ precedes event $F$ in the platform frame. The platform observer is also correct.
>
> *Why constancy of $c$ forces this.* If light obeyed Galilean addition — $c + v$ towards the source's motion, $c - v$ against it — the two effects (unequal distance, unequal speed) would exactly cancel and both frames would agree the arrivals are simultaneous. It is precisely *because* the speed of light is the *same* in both directions in the platform frame, refusing to compensate for the walls' motion, that the arrivals are unequal there. The relativity of simultaneity is the direct shadow of Postulate 2. Consistency: $F$ and $B$ are spacelike separated (they are the same kind of "two distant events at the same time in one frame" as in Step 1), so their order is allowed to differ between frames, and $\Delta t'_{FB} = -\gamma v\,\Delta x_{FB}$ from Step 1 gives the platform-frame time gap quantitatively.

> [!note]- Complete formal solution
> Let $P_1 = (t,x_1)$, $P_2 = (t,x_2)$ be simultaneous in $S$. By $t' = \gamma(t-vx)$, $\Delta t' = -\gamma v\,\Delta x \ne 0$ — not simultaneous in $S'$. These events are spacelike separated ($\Delta s^2 = -\Delta x^2 < 0$), so a frame-dependent order is permitted. On the spacetime diagram, $S$'s simultaneity lines $t =$ const are horizontal; $S'$'s lines $t' =$ const satisfy $t - vx =$ const, slope $v$ — the two slicings differ. In the train experiment, the carriage frame has the bulb equidistant from stationary walls, so light (speed $1$) reaches both walls together; the platform frame still has light at speed $1$ in each direction, but the back wall advances into the light and the front recedes, so the back is struck first. Both frames are correct; the disagreement is forced by the constancy of $c$, since Galilean addition would make the effects cancel. $\blacksquare$

---

# Key Takeaways

**Simultaneity is a relation between two events *and a frame*, never between two events alone.** The phrase "at the same time" is incomplete until a frame is named. The Lorentz transformation's $t' = \gamma(t - vx)$ clause shows exactly why: the new time coordinate depends on the old *space* coordinate, so observers at different $x$ have their notions of "now" offset. Two events with the same $t$ but different $x$ acquire a time gap $\Delta t' = -\gamma v\,\Delta x$ in any boosted frame. This single fact is the master key to the subject's paradoxes: the twin paradox, the ladder-and-barn, the pole-vaulter — every one is built by treating "now" as if it were frame-independent. Whenever a relativity argument uses "now", "before", "while", or "at the same time", stop and ask "in which frame?", and the paradox dissolves.

**The relativity of simultaneity is the shadow of the constancy of the speed of light — they are the same fact.** The train experiment makes the link airtight. If light obeyed Galilean velocity addition, the two competing effects in the platform frame (the back wall moving into the light, the light moving slower against the train's motion) would precisely cancel, and simultaneity would be absolute. It is *only* because the speed of light is stubbornly the same in both directions, in every frame, that the arrivals come out unequal. So one cannot accept Postulate 2 and keep absolute simultaneity — the two are logically incompatible. The reusable insight: the constancy of $c$ is not an isolated curiosity about light; it is the engine that drives time dilation, length contraction, and the whole geometry of spacetime, and the relativity of simultaneity is the most direct expression of it.

**Spacelike separation is what *permits* a frame-dependent order — and consistency demands it.** The events that two frames can disagree about are exactly the spacelike-separated ones ($\Delta s^2 < 0$): two events "at the same time but different places" in some frame always have negative interval. Timelike-separated events, by contrast, have a frame-independent order, which is what protects causality — cause always precedes effect for everyone. So the relativity of simultaneity is not a licence for chaos: it operates only on pairs of events that no signal could connect, where reordering them changes nothing causal. When checking whether a claimed disagreement between frames is legitimate, compute the interval: a frame-dependent order is allowed for spacelike separation and forbidden for timelike. This is the precise boundary between "harmless relativity of simultaneity" and "would-be violation of cause and effect", and it is drawn by the sign of $\Delta s^2$.
