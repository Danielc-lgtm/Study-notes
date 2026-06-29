---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Relativity of Simultaneity"
  - "Def - The Lorentz Transformation"
  - "Def - Causality and the Light Cone"
  - "Def - The Spacetime Interval"
tags: [physics, special-relativity]
---

# Problem Statement

*(A qualifying-exam-style problem.)* In an inertial frame $S$, two firecrackers explode **simultaneously**: event $A$ at $(t_A, x_A) = (0, 0)$ and event $B$ at $(t_B, x_B) = (0, L)$, with $L > 0$. A second observer in frame $S'$ moves at velocity $v$ along the $+x$-axis of $S$. Work with $c = 1$ unless restoring $c$ clarifies.

1. Find the times $t'_A$ and $t'_B$ that the $S'$ observer assigns to the two explosions, and the time difference $\Delta t' = t'_B - t'_A$. Which explosion does $S'$ judge to occur first?
2. Find the spatial separation $\Delta x'$ that $S'$ assigns to the two explosions, and show it exceeds $L$. Reconcile this with [[Thm - Length Contraction|length contraction]] (which says moving things get *shorter*).
3. Is there any frame in which the two explosions are simultaneous *other* than $S$? Is there a frame in which $B$ precedes $A$? Classify the separation of $A$ and $B$ and use it to answer both questions decisively.
4. Now suppose instead the problem stated that $A$ and $B$ are the *cause* and *effect* of a single physical process (a signal sent from $A$ triggers $B$). Show this is impossible for the given coordinates, and find the minimum time delay $t_B$ (with $x_B = L$ still) that would make a causal link physically possible.

**Recall:**

![[Def - The Relativity of Simultaneity#The Definition]]

The [[Def - The Lorentz Transformation|Lorentz transformation]] from $S$ to $S'$ ($S'$ moving at $v$ along $+x$) is $t' = \gamma(t - vx)$, $x' = \gamma(x - vt)$, with $\gamma = (1-v^2)^{-1/2}$. The [[Def - The Spacetime Interval|interval]] $\Delta s^2 = \Delta t^2 - \Delta x^2$ is [[Thm - Invariance of the Spacetime Interval|invariant]]; its sign gives the [[Def - Causality and the Light Cone|causal classification]] (timelike $\Delta s^2 > 0$, spacelike $< 0$, null $= 0$, in mostly-minus signature).

---

# Convergent Strategy

**Problem class.** A *compute-an-effect plus decide-a-causal-question* problem — the canonical qualifying-exam test of whether the student controls the relativity of simultaneity and the invariant interval together. The [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction#Problem-Solving Strategy|topic strategy]] says: transform the given events, then classify their separation to settle every order/causality question.

**Assumption pattern.** The key datum is "$\Delta t = 0$ in $S$ with $\Delta x = L \ne 0$" — two events *simultaneous and spatially separated* in $S$. This immediately flags a spacelike separation ($\Delta s^2 = -L^2 < 0$), which is the single fact that governs parts 1, 3, and 4. The separation being spacelike means the order is frame-dependent and no causal link is possible.

**Theorem routing.** Part 1 applies the [[Def - The Lorentz Transformation|Lorentz transformation]] to each event's time. Part 2 transforms the spatial coordinates and reconciles the "stretch" with length contraction by noting the proper length is the longer one. Part 3 classifies via $\Delta s^2 = -L^2 < 0$ ([[Def - Causality and the Light Cone]]) and uses $\Delta t' = 0 \Leftrightarrow v = \Delta t/\Delta x$. Part 4 uses the causality condition: a causal link needs timelike-or-null separation, $t_B \ge L$.

**Key decision point.** The crux of part 2 is resisting the trap that "$S'$ measures a *larger* separation $\gamma L$, but length contraction says moving rods are *shorter* — contradiction!". The resolution is that $\gamma L$ is not the contraction of anything: $A$ and $B$ are *events*, not the ends of a rod measured simultaneously in $S'$. The rest-frame separation of two events simultaneous in $S$ is the *proper* length between them, which is the longest; $S'$ sees the larger value because the two explosions are *not* simultaneous in $S'$. Confusing "separation of two events" with "length of a rod" is the intended pitfall.

---

# Legal Operations Used

1. **Apply the Lorentz transformation to map events between frames** (operation 1 from the topic page). Parts 1 and 2 transform $A$ and $B$ from $S$ to $S'$, reading off $\Delta t'$ and $\Delta x'$ directly.

2. **Classify a separation by the sign of its interval** (the causal-classification move, from [[Def - Causality and the Light Cone]]). Computing $\Delta s^2 = -L^2 < 0$ settles parts 3 and 4 at a stroke: spacelike means order-reversible and causally disconnected.

3. **Tilt the line of simultaneity** (operation 5). The reason $S'$ disagrees about simultaneity, and sees a stretched separation, is that its "now" line is tilted relative to $S$'s; part 3's "is there another simultaneous frame?" is answered by where the tilt can land.

4. **Compute an invariant in the most convenient frame** (operation 8). The interval, computed trivially in $S$ as $-L^2$, fixes the proper length $\sqrt{|\Delta s^2|} = L$ and the threshold $t_B = L$ for causality.

---

# Hints

> [!note]- Hint 1
> Apply $t' = \gamma(t - vx)$ to each event. For $A = (0,0)$ you get $t'_A = 0$. For $B = (0, L)$ you get $t'_B = \gamma(0 - vL) = -\gamma vL$. So $\Delta t' = t'_B - t'_A = -\gamma vL < 0$ (for $v > 0$): in $S'$, event $B$ (the one further along $+x$) happens *first*. This is "leading events lead is wrong — leading clocks lag", i.e. the further-along-motion event is earlier in $S'$.

> [!note]- Hint 2
> Apply $x' = \gamma(x - vt)$: $x'_A = 0$, $x'_B = \gamma(L - 0) = \gamma L$. So $\Delta x' = \gamma L > L$. Do not call this a length-contraction violation. $A$ and $B$ are *events*; $\gamma L$ is the separation of two events that are *not simultaneous in $S'$*. To compare with length contraction you would need a rod at rest in one frame measured in another, with both ends read simultaneously — a different setup.

> [!note]- Hint 3
> Compute the interval: $\Delta s^2 = \Delta t^2 - \Delta x^2 = 0 - L^2 = -L^2 < 0$, so $A$ and $B$ are **spacelike**-separated. For spacelike events: (i) they are simultaneous *only* in frames where $\Delta t' = \gamma(\Delta t - v\Delta x) = 0$, i.e. $v = \Delta t/\Delta x = 0/L = 0$ — only $S$ itself. (ii) The order reverses for $v > 0$ (we found $\Delta t' < 0$). So yes, frames with $B$ before $A$ exist; the simultaneous frame is unique ($S$).

> [!note]- Hint 4
> A causal link from $A$ to $B$ needs a signal at speed $\le 1$, i.e. a timelike or null separation: $\Delta s^2 = t_B^2 - L^2 \ge 0$, so $t_B \ge L$. With $t_B = 0$ this fails ($-L^2 < 0$). The minimum delay for a possible causal link is $t_B = L$ (a light signal, null separation); any $t_B > L$ allows a sub-light signal.

---

# Solution

The events are simultaneous in $S$ but spacelike-separated, and that single fact drives everything: $S'$ disagrees about both their order and their separation, the simultaneous frame is unique, and no causal link is possible at the given coordinates.

**Step 1: In $S'$, event $B$ occurs first, by $\Delta t' = -\gamma vL$.**

> [!note]- Derivation
> Apply the [[Def - The Lorentz Transformation|Lorentz transformation]] $t' = \gamma(t - vx)$ to each event:
> $$t'_A = \gamma(0 - v\cdot 0) = 0, \qquad t'_B = \gamma(0 - v\cdot L) = -\gamma vL.$$
> Hence
> $$\Delta t' = t'_B - t'_A = -\gamma vL \qquad\left(\text{with } c: \ \Delta t' = -\frac{\gamma vL}{c^2}\right).$$
> For $v > 0$ this is negative, so $t'_B < t'_A$: in $S'$, the explosion $B$ — the one further along the direction of $S'$'s motion — happens **before** $A$. (An observer moving in the $-x$ direction, $v < 0$, would judge $A$ first.) The magnitude is first-order in $v$ and grows with the separation $L$: this is the relativity of simultaneity, $\Delta t' = -\gamma v\,\Delta x$ for events with $\Delta t = 0$.

**Step 2: In $S'$, the separation is $\Delta x' = \gamma L > L$ — and this is not a contraction violation.**

> [!note]- Derivation
> Apply $x' = \gamma(x - vt)$:
> $$x'_A = \gamma(0 - 0) = 0, \qquad x'_B = \gamma(L - v\cdot 0) = \gamma L,$$
> so $\Delta x' = \gamma L > L$. At first sight this clashes with [[Thm - Length Contraction|length contraction]] — shouldn't a moving observer measure *shorter* distances? No, and seeing why is the heart of the problem. Length contraction is a statement about a **rod**: an object at rest in one frame, whose two ends are recorded *at the same time in the measuring frame*. Here $A$ and $B$ are **events**, fixed points of spacetime, not the simultaneous-in-$S'$ readings of any rod's ends. The number $\gamma L$ is the spatial gap between two events that $S'$ judges to be *non-simultaneous* (Step 1), so it is not a length measurement at all.
>
> To make contact with contraction properly: imagine a rod at rest in $S$ spanning $A$ and $B$, with proper length $L_0 = L$ in $S$. Then $S'$ would measure its length by reading both ends *simultaneously in $S'$*, getting $L_0/\gamma = L/\gamma < L$ — contraction, as expected. The difference between $\gamma L$ and $L/\gamma$ is entirely the difference between "spatial separation of two given events" and "length of a rod read simultaneously in $S'$". The proper separation between $A$ and $B$ (the separation in the frame where they are simultaneous, namely $S$) is $L$, which is the *minimum* spatial separation over frames where the events keep their identity — every other frame, slicing on the bias, assigns a larger gap.

**Step 3: $S$ is the unique simultaneous frame; frames with $B$ before $A$ exist.**

> [!note]- Derivation
> Compute the [[Def - The Spacetime Interval|interval]]: $\Delta s^2 = \Delta t^2 - \Delta x^2 = 0^2 - L^2 = -L^2 < 0$. The separation is **spacelike** ([[Def - Causality and the Light Cone]]), and this is invariant ([[Thm - Invariance of the Spacetime Interval]]). Now:
> - *Simultaneous frames.* A frame $S'$ at velocity $v$ judges the events simultaneous iff $\Delta t' = \gamma(\Delta t - v\,\Delta x) = \gamma(0 - vL) = -\gamma vL = 0$, i.e. iff $v = 0$. So the **only** inertial frame in which $A$ and $B$ are simultaneous is $S$ itself. (Geometrically: the events lie on a single horizontal line of the $S$-diagram, and only the unboosted frame has horizontal simultaneity lines through both.)
> - *Order-reversed frames.* For $0 < v < 1$, $\Delta t' = -\gamma vL < 0$, so $B$ precedes $A$; for $-1 < v < 0$, $A$ precedes $B$. Both orders are realised by physical frames. The order of $A$ and $B$ is genuinely frame-dependent — permissible exactly because, being spacelike-separated, they cannot influence one another.

**Step 4: No causal link at $t_B = 0$; the threshold is $t_B = L$.**

> [!note]- Derivation
> A physical signal from $A$ to $B$ must travel at speed $\le 1$, i.e. along a timelike or null worldline, which requires $\Delta s^2 = \Delta t^2 - \Delta x^2 \ge 0$. With the given coordinates $\Delta s^2 = -L^2 < 0$: the separation is spacelike, no signal connects them, so $A$ **cannot** be the cause of $B$. (Consistent with Step 3: if $A$ could cause $B$, their order could not be reversible, yet it is.)
>
> Keeping $x_B = L$ but allowing $B$'s time to be $t_B$, a causal link becomes possible when
> $$\Delta s^2 = t_B^2 - L^2 \ge 0 \ \Longrightarrow\ t_B \ge L.$$
> The **minimum** delay is $t_B = L$ (restoring $c$: $t_B = L/c$), a *light* signal travelling the distance $L$ at speed $c$ — a null separation, the boundary of the light cone. For any $t_B > L$ a sub-light signal suffices. So the firecrackers could be causally linked only if the second went off at least a light-travel-time after the first; their stated simultaneity rules causation out.

> [!note]- Complete formal solution
> The events $A = (0,0)$ and $B = (0, L)$ are simultaneous in $S$ and spacelike-separated, $\Delta s^2 = -L^2 < 0$. In $S'$ (velocity $v$ along $+x$): $t'_A = 0$, $t'_B = -\gamma vL$, so $\Delta t' = -\gamma vL < 0$ and $B$ occurs first; $x'_A = 0$, $x'_B = \gamma L$, so $\Delta x' = \gamma L > L$. The enlarged separation is not a length-contraction violation, because $A, B$ are events, not the simultaneous-in-$S'$ endpoints of a rod (a rod at rest in $S$ of proper length $L$ would measure $L/\gamma$ in $S'$); $\gamma L$ is the bias-sliced gap between non-simultaneous events. Because $\Delta s^2 < 0$ is invariant, the order is frame-dependent: $\Delta t' = 0$ only for $v = 0$ (so $S$ is the unique simultaneous frame), and $\Delta t' < 0$ for all $v > 0$ (frames with $B$ before $A$ exist). A causal link $A \to B$ needs $\Delta s^2 = t_B^2 - L^2 \ge 0$, impossible at $t_B = 0$; the minimum delay for a possible (null) causal link is $t_B = L$, a light signal. $\blacksquare$

---

# Key Takeaways

**Spacelike separation is a master key: it answers order, simultaneity, and causality at once.** The moment you read "two events simultaneous in $S$ but at different places", compute the interval and find it spacelike ($\Delta s^2 = -L^2 < 0$), and three answers fall out together. The order is frame-dependent (some frame reverses it). The frame in which they are simultaneous is unique (only $v = 0$ here, because $\Delta t' = \gamma(\Delta t - v\Delta x) = 0$ has a single solution). And no causal link is possible (a signal would have to outrun light). Examiners love this configuration precisely because one invariant — the sign of $\Delta s^2$ — controls every sub-question, and a student who computes it first has effectively solved the problem before transforming a single coordinate. The trigger is "simultaneous and separated"; the reflex is "spacelike, hence order-relative and acausal".

**Do not confuse the separation of two events with the length of a rod.** The intended trap in part 2 — that $S'$ measures a *larger* gap $\gamma L$ while length contraction promises *shorter* — catches anyone who has memorised $L = L_0/\gamma$ without internalising what it measures. A length is the distance between the two ends of an object recorded *simultaneously in the measuring frame*; the separation of two given spacetime events is something else entirely, because those events are generally *not* simultaneous in the frame doing the asking. The same pair of points can yield $L$ (proper separation, in the simultaneous frame $S$), $\gamma L$ (event separation in $S'$, where they are non-simultaneous), or $L/\gamma$ (contracted length of a rod spanning them, read simultaneously in $S'$) depending on exactly which measurement you mean. Whenever a "distance" appears in a relativity problem, ask: is this the gap between two specified events, or the simultaneously-read length of an object? The two transform oppositely, and conflating them is the single most common scoring error on problems of this type.

**"Simultaneous in $S$" is a strong, frame-specific datum — never carry it across a boost.** The problem hands you $\Delta t = 0$, which is the cleanest possible starting point in *one* frame and a landmine in any other. The entire exercise is a study in what becomes of that datum after a boost: the simultaneity evaporates ($\Delta t' = -\gamma vL$), the spatial gap stretches ($\gamma L$), the order can flip, and causation is excluded. The transferable discipline is to treat every "at the same time" as bearing an invisible subscript naming its frame, and to recompute it explicitly whenever the frame changes — using $\Delta t' = \gamma(\Delta t - v\Delta x)$, which converts a frame's simultaneity into another's time-ordering. This is the same discipline that resolves the [[Ex - Length contraction and the ladder-in-the-barn paradox|ladder-and-barn paradox]] and that underlies the [[Ex - The relativity of simultaneity (Einstein's train)|Einstein train]]; mastering it on this clean two-event problem is what makes the dressed-up paradoxes routine.
