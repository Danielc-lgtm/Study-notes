---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Inertial Frame and the Postulates of Special Relativity"
  - "Def - The Lorentz Transformation"
  - "Def - Spacetime Diagram"
tags: [physics, special-relativity]
---

# Problem Statement

An inertial observer $O$ carries a single ideal clock and a source of light, and nothing else — no pre-installed coordinate grid, no synchronised distant clocks. Following Einstein's 1905 operational prescription, $O$ is to build an [[Def - Inertial Frame and the Postulates of Special Relativity|inertial coordinate system]] on all of spacetime using only the clock, light signals, and the second postulate.

1. **Coordinatising a distant event (the radar method).** $O$ wishes to assign coordinates $(t, x)$ to a distant event $A$. $O$ emits a light signal at clock-reading $t_1$, the signal reflects off $A$ and returns to $O$ at clock-reading $t_2$. State the time and position $O$ assigns to $A$, and justify each from the constancy of $c$.
2. **Einstein synchronisation.** Using this, state the rule by which $O$ declares a distant clock (at rest in $O$'s frame) to be synchronised with $O$'s own. Show this is equivalent to: a light signal sent from $O$ at $t_1$ and reflected back arriving at $t_2$ defines the reflection event to be simultaneous with $O$'s clock-reading $\tfrac12(t_1 + t_2)$.
3. **Simultaneity is a convention, and it is frame-dependent.** Show on a [[Def - Spacetime Diagram|spacetime diagram]] that the set of events $O$ calls "simultaneous with $t = 0$" is the $x$-axis, while a second inertial observer $O'$ in relative motion, applying the *same* radar procedure, declares a *different* set (the tilted $x'$-axis) simultaneous. Conclude that simultaneity is not a fact about the world but a synchronisation convention internal to each frame.
4. **Consistency with the Lorentz transformation.** Verify that the line of simultaneity $O'$ obtains by the radar method is exactly the locus $t' = 0$ predicted by the [[Def - The Lorentz Transformation|Lorentz transformation]] $t' = \gamma(t - vx)$.

**Recall:**

![[Def - Inertial Frame and the Postulates of Special Relativity#The Definition]]

The **radar method** assigns coordinates to a distant event by bouncing a light signal off it and timing the round trip. On a [[Def - Spacetime Diagram|spacetime diagram]] (time $ct$ vertical, $x$ horizontal, $c = 1$), light travels at $45^\circ$ and the simultaneity line $t' = 0$ of a frame moving at $v$ has slope $v$. The relevant transformation is $t' = \gamma(t - vx)$, so $t' = 0 \Leftrightarrow t = vx$.

---

# Convergent Strategy

**Problem class.** This is a *conceptual-foundations / operational-definition* problem: rather than computing a number, it asks you to construct the coordinate system from primitive operations and thereby expose that a notion taken for granted (simultaneity) is actually a convention. The [[Special Relativity I — Postulates and Lorentz Transformations#Problem-Solving Strategy|topic strategy]] flags simultaneity as the buried assumption behind every paradox; this exercise builds simultaneity from scratch to show *why* it is frame-dependent.

**Assumption pattern.** The only physical input is the second postulate — light travels at $c$ in $O$'s frame, the same speed out and back. This single fact licenses the radar assignment: because the outbound and return legs have equal speed, the reflection happens at the *midpoint* in time and the distance is half the round-trip light-travel. The recognition is that "the speed is the same both ways" is exactly what makes $\tfrac12(t_1 + t_2)$ the natural definition of "simultaneous".

**Theorem routing.** Part 1 and 2 use only the constancy of $c$. Part 3 uses the [[Def - Spacetime Diagram|spacetime diagram]] geometry (light at $45^\circ$, two observers' light cones). Part 4 closes the loop by checking the radar-derived simultaneity line against the [[Def - The Lorentz Transformation|Lorentz transformation]]'s $t' = 0$ locus — confirming the operational construction reproduces the algebraic transformation, which is the deep consistency the exercise is built to display.

**Key decision point.** The non-obvious realisation is that the *choice of midpoint* $\tfrac12(t_1+t_2)$ is a *convention* — it assumes the one-way speed of light equals the two-way speed, which can never be measured without already-synchronised clocks. The natural alternative (Reichenbach's $\epsilon$-synchronisation, with the reflection at $t_1 + \epsilon(t_2 - t_1)$ for any $\epsilon \in (0,1)$) is internally consistent for other $\epsilon$; the choice $\epsilon = \tfrac12$ is the *standard* convention because it is the only isotropic one. Recognising that simultaneity rests on a conventional choice is the entire conceptual payoff.

---

# Legal Operations Used

1. **Operation 1 from the topic page (apply the Lorentz transformation / use the constancy of $c$).** The radar assignment is built directly from "light has speed $c$ both ways", and part 4 checks against the Lorentz transformation.

2. **Operation 6 from the topic page (read geometry off a spacetime diagram).** Part 3 is essentially this operation: drawing two observers' light signals and their resulting simultaneity lines to see that they differ.

3. **Operation 8 from the topic page (classify by light cones / use the $45^\circ$ structure).** The radar signals are $45^\circ$ light rays, and their intersection with the worldlines is what defines the coordinates.

---

# Hints

> [!note]- Hint 1
> The signal travels out and back at the same speed $c$ (second postulate). So the reflection event $A$ is, in $O$'s reckoning, at the time exactly *halfway* between emission and reception, and at a distance equal to $c$ times *half* the round-trip time. Write these as formulas in $t_1, t_2$.

> [!note]- Hint 2
> Synchronisation: a distant clock (at rest in $O$'s frame) is synchronised with $O$'s if it reads $\tfrac12(t_1 + t_2)$ at the reflection event. Equivalently, "simultaneous with $O$'s reading $\tau$" means: the reflection of a signal sent at $\tau - \Delta$ and received at $\tau + \Delta$.

> [!note]- Hint 3
> On the diagram, $O$'s worldline is the vertical $ct$-axis. A radar signal to an event on the $x$-axis goes down-and-out then up-and-back symmetrically, so emission and reception are at $t = -x$ and $t = +x$, with midpoint $t = 0$ — the $x$-axis is $O$'s simultaneity line. Now do the same for $O'$ whose worldline is tilted (slope $1/v$): the symmetric midpoint construction gives a *tilted* line.

> [!note]- Hint 4
> For part 4: $O'$ moves at $v$, worldline $x = vt$. A signal $O'$ sends and receives symmetrically about a reflection event $E$ on the $x'$-axis. Compute the slope of the locus of such $E$; you should find slope $v$, matching $t' = \gamma(t - vx) = 0 \Leftrightarrow t = vx$.

---

# Solution

The radar method assigns to an event the *midpoint time* and *half-distance* of a reflected light signal (Steps 1–2), a construction that rests on the second postulate and on the *convention* that light's one-way speed equals its two-way speed. Because each observer applies the construction in their own frame, the resulting simultaneity lines tilt with velocity (Step 3), and the tilt is exactly the $t' = 0$ locus of the Lorentz transformation (Step 4).

**Step 1: $O$ assigns to $A$ the time $\tfrac12(t_1 + t_2)$ and position $\tfrac12 c(t_2 - t_1)$.**

> [!note]- Derivation
> $O$ emits the signal at clock-reading $t_1$ and receives the reflection at $t_2$. By the [[Def - Inertial Frame and the Postulates of Special Relativity|second postulate]], the signal travels at speed $c$ on *both* legs (out to $A$ and back), and the two legs cover the same distance $d$ to $A$. So each leg takes time $d/c$, and the total round-trip time is $t_2 - t_1 = 2d/c$, giving
> $$x_A = d = \frac{c\,(t_2 - t_1)}{2}.$$
> The reflection event $A$ occurs at the *midpoint* in time: the signal reaches $A$ after time $d/c$ from emission, i.e. at
> $$t_A = t_1 + \frac{d}{c} = t_1 + \frac{t_2 - t_1}{2} = \frac{t_1 + t_2}{2}.$$
> Thus $O$ assigns $A$ the coordinates $\big(t_A, x_A\big) = \big(\tfrac12(t_1 + t_2),\ \tfrac12 c(t_2 - t_1)\big)$. Both formulas use *only* that the speed is $c$ and equal both ways; no pre-existing distant clock or ruler was assumed. With $c = 1$: $t_A = \tfrac12(t_1 + t_2)$, $x_A = \tfrac12(t_2 - t_1)$.

**Step 2: Einstein synchronisation — the reflection is simultaneous with $O$'s reading $\tfrac12(t_1 + t_2)$.**

> [!note]- Derivation
> A distant clock $C$, at rest in $O$'s frame, is declared **synchronised** with $O$'s clock if $C$ reads $\tfrac12(t_1 + t_2)$ at the moment the radar signal reflects off it. Equivalently, the event "$C$ reflects the signal" is defined to be **simultaneous** with the event "$O$'s clock reads $\tfrac12(t_1 + t_2)$". Stated symmetrically: a signal sent at $t_1 = \tau - \Delta$ and received at $t_2 = \tau + \Delta$ (so $\tau = \tfrac12(t_1 + t_2)$, $\Delta = \tfrac12(t_2 - t_1)$) defines its reflection event to be simultaneous with $O$'s reading $\tau$. This is **Einstein synchronisation**.
>
> The hidden convention: this rule *assumes* the signal takes equal time on each leg — that the one-way speed of light equals the two-way speed. The two-way speed is measurable with a single clock (emit and receive at the same place), but the one-way speed cannot be measured without *already* having synchronised clocks at the two ends, which is what we are trying to define. So $\epsilon = \tfrac12$ (reflection at the midpoint) is a *choice*. Reichenbach's generalisation places the reflection at $t_1 + \epsilon(t_2 - t_1)$ for any $\epsilon \in (0,1)$, all internally consistent; $\epsilon = \tfrac12$ is selected because it is the unique *isotropic* choice (light treated identically in $+x$ and $-x$ directions), which is the natural convention in an inertial frame. Simultaneity is thus, at bottom, conventional.

**Step 3: Different observers declare different events simultaneous; simultaneity is frame-dependent.**

> [!note]- Derivation
> Draw the [[Def - Spacetime Diagram|spacetime diagram]] in $O$'s frame ($c = 1$): $O$'s worldline is the vertical $t$-axis.
>
> *$O$'s simultaneity line.* To find the events $O$ calls simultaneous with $t = 0$, take an event $A = (0, x_A)$ on the $x$-axis. The radar signal to it is emitted at $t_1 = -x_A$ (a $45^\circ$ line down-left from $A$ to the $t$-axis) and received at $t_2 = +x_A$ (a $45^\circ$ line up-left). The midpoint is $\tfrac12(t_1 + t_2) = 0$ — so $O$ assigns $A$ the time $0$. Every event on the $x$-axis is reached this way, so **$O$'s simultaneity line is the $x$-axis**, $t = 0$.
>
> *$O'$'s simultaneity line.* Now let $O'$ move at velocity $v$, worldline $x = vt$ (slope $1/v$, steeper than $45^\circ$). $O'$ performs the *identical* radar procedure with $O'$'s own clock. Consider an event $E$ that $O'$ will call simultaneous with the moment $O'$ passes the origin. $O'$ emits a signal *before* reaching the origin and receives it *after*, symmetrically about the origin *in $O'$'s clock*. Because $O'$'s worldline is tilted, the two $45^\circ$ light rays from $O'$'s emission and reception events meet at an event $E$ that is *not* on the $x$-axis but on a line *tilted upward*. Carrying out the construction (next step computes the slope) shows $O'$'s simultaneity line is the line $t = vx$ — the **tilted $x'$-axis** — which is a *different* set of events from $O$'s $x$-axis.
>
> Therefore $O$ and $O'$, applying the same operational rule, disagree about which distant events are simultaneous with a given local moment. Neither is wrong: each has correctly synchronised clocks *within their own frame* by the isotropic convention. Simultaneity is not a property of pairs of events but a relation *relative to a frame's synchronisation* — it is frame-dependent, the conceptual core of relativity.

**Step 4: The radar simultaneity line is exactly $t' = 0$ from the Lorentz transformation.**

> [!note]- Derivation
> Compute the slope of $O'$'s simultaneity line directly. $O'$ moves on $x = vt$. Let $O'$ pass the origin at its clock-zero. $O'$ emits a signal at an earlier event $P_1$ on its worldline, at $O'$-clock-reading $-\Delta'$, and receives the reflected signal at a later event $P_2$, at $+\Delta'$. In $O$'s coordinates, by symmetry of the radar construction in $O'$'s frame, the reflection event $E$ that $O'$ calls simultaneous with its clock-zero is the intersection of the two light rays from $P_1$ and $P_2$.
>
> The clean way to get the slope: $O'$'s line of simultaneity is, by the radar definition, the locus of reflection events for signals emitted and received symmetrically (in $O'$'s clock) about a given moment. This is precisely the set $\{t' = \text{const}\}$ in $O'$'s coordinates. From the [[Def - The Lorentz Transformation|Lorentz transformation]],
> $$t' = \gamma(t - vx),$$
> so the simultaneity line $t' = 0$ (through the origin) is
> $$t - vx = 0 \quad\Longleftrightarrow\quad t = vx,$$
> a line through the origin of slope $v$ in the $(x, t)$ plane — exactly the tilted $x'$-axis. This matches the radar construction: the operational midpoint rule, applied in $O'$'s frame, *reproduces* the $t' = 0$ locus of the Lorentz transformation. The two routes — Einstein's operational synchronisation and the algebraic boost — agree, which is the consistency check the exercise was built to demonstrate. The tilt of the simultaneity line (slope $v$, versus $O$'s slope $0$) is the geometric face of the relativity of simultaneity.

> [!note]- Complete formal solution
> By the second postulate the radar signal travels at $c$ on both legs over equal distance $d$, so the round trip takes $t_2 - t_1 = 2d/c$, giving position $x_A = \tfrac12 c(t_2 - t_1)$ and time $t_A = t_1 + d/c = \tfrac12(t_1 + t_2)$. Einstein synchronisation declares the reflection simultaneous with $O$'s reading $\tfrac12(t_1 + t_2)$ — the unique isotropic ($\epsilon = \tfrac12$) choice, a convention since the one-way light speed is not independently measurable. On the spacetime diagram, $O$'s simultaneity line is the $x$-axis ($t = 0$): an event $(0, x_A)$ has radar emission/reception at $t = \mp x_A$, midpoint $0$. An observer $O'$ on $x = vt$ applying the same rule obtains the simultaneity locus $t = vx$ (slope $v$), a *different* line. This matches the Lorentz transformation: $t' = \gamma(t - vx) = 0 \Leftrightarrow t = vx$. Hence simultaneity is a frame-internal synchronisation convention, frame-dependent, and the operational and algebraic constructions agree. $\blacksquare$

---

# Key Takeaways

**Coordinates in relativity are operationally constructed, not God-given, and the construction is the radar method.** The single most clarifying idea here is that an inertial frame is not a pre-existing grid floating in space but something an observer *builds* with a clock and a flashlight: time is the clock reading, distant time is the midpoint of a reflected signal, distant position is half the round-trip light-travel. Once you internalise this, the strange features of relativity stop being paradoxes and become consequences of *how the coordinates were made*. The trigger to invoke the operational view: whenever a problem hinges on "what does observer $X$ measure?" or "are these events simultaneous for $X$?", ask how $X$'s coordinates were operationally defined — almost always the answer is the radar/light-signal construction, and the apparent paradox dissolves into the recognition that two observers built their grids with light signals that they slice differently.

**Simultaneity is a convention internal to each frame, and that single fact is the master key to every relativistic paradox.** "At the same time" is not a relation between two events alone; it is a relation *relative to a frame's synchronisation convention*, fixed by the isotropic ($\epsilon = \tfrac12$) radar rule within that frame. Two inertial observers in relative motion synchronise correctly by their own lights and still disagree about which distant events are simultaneous, because their light-signal slicings of spacetime tilt relative to one another. This is the content behind the [[Def - Spacetime Diagram|tilted x′-axis]]: lines of constant $t'$ are not lines of constant $t$. The transferable diagnostic — the one that unlocks the twin paradox, the ladder-and-barn, and every "but isn't it symmetric?" objection — is to hunt down every use of "now", "simultaneously", "at the same time", "while", and ask *in which frame*, then draw the two simultaneity lines and watch the disagreement become geometric rather than contradictory.

**Operational definitions and algebraic transformations must agree, and checking they do is a powerful consistency test.** The exercise closes by verifying that the simultaneity line built operationally (radar midpoints in $O'$'s frame) coincides exactly with the $t' = 0$ locus of the [[Def - The Lorentz Transformation|Lorentz transformation]]. This is not a coincidence: the Lorentz transformation can be *derived* from the radar construction plus the constancy of $c$ (this is the Einstein route of 1905, complementary to the [[Ex - The k-calculus (Bondi) derivation|k-calculus]] and to the [[Thm - Uniqueness of the Lorentz Transformation from the Postulates|algebraic uniqueness]] derivations). The general principle: when a physical quantity can be reached by two independent routes — one operational/physical, one formal/algebraic — their agreement is a stringent check on both, and a *disagreement* signals either a conceptual error in the operational setup or an algebra mistake. Building the same object two ways and confirming they match is among the most trustworthy moves in all of physics, and it is the reason one can be confident the Lorentz transformation describes the real world and not merely a self-consistent formal game.
