---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - Inertial Frame and the Postulates of Special Relativity"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, so a light ray has a $45^\circ$ worldline and velocities satisfy $|v| < 1$; the $c$-restored forms are given where they are more recognisable. Two inertial frames $S$ and $S'$ are in standard configuration: $S'$ moves at velocity $v$ along the common $x$-axis, and their origins coincide at one event. An **event** is a point of spacetime, with coordinates $(t, x, y, z)$ in $S$ and $(t', x', y', z')$ in $S'$, related by the [[Def - The Lorentz Transformation|Lorentz transformation]] $t' = \gamma(t - vx)$, $x' = \gamma(x - vt)$, with $\gamma = (1-v^2)^{-1/2}$. A **line (or surface) of simultaneity** of a frame is the set of events that frame assigns one common time. We plot $t$ vertically and $x$ horizontally throughout. Full registry on [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction]].

---

# Axiom Motivation

The whole of special relativity hinges on noticing that one Newtonian assumption was never an axiom but a prejudice, and the relativity of simultaneity is the precise statement of what that prejudice got wrong. So the right way to motivate this definition is not to ask "what should simultaneity mean?" but to ask "what did we silently *assume* it meant, and why is that assumption now untenable?"

In Newtonian physics, two events are simultaneous if they happen at the same time, full stop — because there is one universal time $t$, read identically by every observer, and "now" is a well-defined slice through all of space. This is the clause $t' = t$ of the Galilean transformation. It is so natural that for two centuries nobody marked it as an assumption. But it *is* an assumption, and it is the one that the constancy of the speed of light destroys. If light travels at the same speed $c$ for every observer regardless of their motion, then — as the train argument below makes vivid — two observers in relative motion cannot agree on which events are simultaneous. Something has to give, and what gives is the universality of "now".

The desideratum, then, is an operational definition of simultaneity that does *not* presuppose a universal time: a recipe each observer can carry out within their own frame, using only their own clocks and rulers. Here it is. An observer is not a single person at a point but a lattice of clocks at rest throughout the frame, synchronised in advance (for instance by Einstein's convention: send a light pulse from clock $A$ to clock $B$ and back, and set $B$'s clock so that the one-way times are equal). Two events are then *simultaneous in that frame* if the local clocks sitting at the two events — clocks of that frame's lattice, present right where each event happens — read the same time. This definition is purely local: it never compares a distant clock by eye, so it is immune to the time light takes to travel. It is the honest replacement for "they happen at the same universal time".

The content of the definition is what happens when two frames each apply this recipe. Because the two lattices are synchronised by light signals and the two frames move relative to each other, *they synchronise differently*. The events that $S$'s lattice marks simultaneous are not the events that $S'$'s lattice marks simultaneous. To see this is forced, take the one axiom we are not willing to drop — the constancy of $c$ — and ask what it does to the synchronisation procedure. In $S'$, the bulb-at-the-middle-of-the-carriage argument shows light reaches the two ends together; in $S$, where the carriage is moving, the same light (still travelling at $c$, by the axiom) reaches the approaching end first. The two frames' notions of "the light arrived at both ends at once" genuinely differ. There is no further fact that adjudicates between them: simultaneity is *relative*, a property of a pair (event pair, frame), not of the event pair alone.

It is worth dwelling on which assumption we would have to restore to make simultaneity absolute again, because it sharpens what is really going on. If we *dropped* the constancy of $c$ and instead let light's speed add to the source's velocity in the Galilean way, the train argument would collapse and simultaneity would be universal — this is precisely the Newtonian world. So the relativity of simultaneity is logically equivalent, given the other postulates, to the constancy of light's speed; you cannot have one without the other. And if we tried to *keep* absolute simultaneity while also keeping constant $c$, we would have a contradiction, which is exactly the contradiction the train exhibits. The definition is not a free choice; it is the only notion of simultaneity consistent with light behaving the same for everyone.

---

# The Definition

Let $S$ and $S'$ be inertial frames in standard configuration, $S'$ moving at velocity $v$ along the $x$-axis of $S$. Two events are **simultaneous in $S$** if they have equal time coordinate $t$, and **simultaneous in $S'$** if they have equal time coordinate $t'$. The **relativity of simultaneity** is the statement that these two relations are different: events simultaneous in $S$ are in general not simultaneous in $S'$.

Quantitatively, the surfaces of simultaneity of $S$ are the hyperplanes $t = \text{const}$. Substituting the [[Def - The Lorentz Transformation|Lorentz transformation]] $t' = \gamma(t - vx)$, the surfaces of simultaneity of $S'$ — the events with $t' = \text{const}$ — are the hyperplanes
$$
t - vx = \text{const} \qquad\left(\text{with } c \text{ restored: } \ t - \frac{vx}{c^2} = \text{const}\right).
$$
On a spacetime diagram with $t$ vertical and $x$ horizontal, the $S$-simultaneity lines are horizontal, while the $S'$-simultaneity lines are tilted upward with slope $v$ (in units where $c = 1$). Two events with the same $t$ but different $x$ — simultaneous in $S$ — therefore have $t' = \gamma(t - vx)$ differing by $-\gamma v\,\Delta x$ in $S'$:
$$
\Delta t = 0 \ \text{in } S \quad\Longrightarrow\quad \Delta t' = -\gamma v\,\Delta x \quad (\ne 0 \text{ if } \Delta x \ne 0).
$$
The event with the larger $x$ (further along the direction of $S'$'s motion) is assigned the *earlier* $t'$. The effect vanishes if and only if the two events coincide in $x$, or $v = 0$.

The $S'$-simultaneity line is the **$x'$-axis** (and its parallels): it is the locus $t' = \text{const}$, which for $t' = 0$ is $t = vx$, the mirror image, across the $45^\circ$ light line, of the $t'$-axis $x = vt$ (the worldline of $S'$'s spatial origin). As $v \to 1$ both axes scissor symmetrically towards the light line, and because $|v| < 1$ always, the simultaneity line never reaches or exceeds $45^\circ$ — the fact that underlies [[Def - Causality and the Light Cone|causality]].

---

# Relate to Other Fields / Compression

The relativity of simultaneity is, in the language of [[Def - Minkowski Space and the Metric|Minkowski geometry]], the statement that there is no canonical way to split spacetime into "space" and "time". A choice of inertial frame is a choice of how to foliate the affine space $\mathbb{M}$ into parallel spacelike hyperplanes (the simultaneity surfaces) stacked along a timelike direction (the time axis); different frames choose different foliations, tilted relative to one another, and the [[Def - The Lorentz Transformation|Lorentz transformation]] is precisely the change of foliation. This is the relativistic analogue of the fact that a vector space has no preferred basis: just as components depend on a basis, "the time of an event" and "the set of events happening now" depend on a frame.

**True name:** *Simultaneity is a choice of slicing, not a fact about the world.* The horizontal line "all events happening now" that Newtonian intuition draws through the present is not discovered but chosen; a frame in relative motion draws a tilted line with equal right, and no experiment distinguishes them. The operational consequence — the form to carry into every problem — is that "$\Delta t = 0$" is a frame-dependent statement, and the moment you assert two spatially separated events are simultaneous you must name the frame, because $\Delta t' = -\gamma v\,\Delta x$ in any other.

In differential geometry this reappears as the statement that a spacetime has no preferred **time function**; the choice of one is a **slicing** (an ADM foliation in the Hamiltonian formulation of general relativity), and the freedom to re-slice is part of the diffeomorphism gauge freedom. The flat, global version — a family of parallel tilted hyperplanes related by a constant boost — is the special-relativistic seed of that gauge freedom.

---

# Examples / Corollaries

**Is an instance — Einstein's train.** A lightbulb hangs at the middle of a railway carriage of rest length $2\ell$, moving at speed $v$. The two events are "light reaches the back wall" ($B$) and "light reaches the front wall" ($F$). In the carriage frame $S'$ the bulb is equidistant from both walls and light travels at $c$ in both directions, so $B$ and $F$ are simultaneous: $\Delta t' = 0$. In the platform frame $S$ the carriage is moving, so the back wall rushes *towards* the point in space where the light was emitted while the front wall flees from it; since the light still travels at $c$ in $S$ (this is the crux — by the constancy of light's speed, not by any addition of the train's velocity), it reaches the back wall first. $\Delta t \ne 0$: the events are not simultaneous in $S$. The two frames disagree, and neither is wrong.

**Is an instance — two synchronised clocks on a moving rod.** Take two clocks at the ends of a rod at rest in $S'$, synchronised in $S'$ (they read the same $t'$). Viewed from $S$, where the rod moves at $v$, the trailing clock is *ahead* of the leading clock by $\gamma v L_0$ in $S$-time (with $L_0$ the rod's proper length) — the "leading clocks lag" rule. This is the same fact as $\Delta t' = -\gamma v\,\Delta x$, read in the other direction, and it is the mechanism behind [[Thm - Length Contraction|length contraction]]: the two end-readings that are simultaneous in $S$ are taken at different $t'$ in $S'$.

**Is NOT an instance — two events at the same place.** Two events occurring at the *same* spatial point ($\Delta x = 0$) and the same time in $S$ have $\Delta t' = -\gamma v \cdot 0 = 0$: they are simultaneous in *every* frame. Simultaneity is absolute only for coincident events. More generally, the time-*order* of two events is frame-independent whenever their separation is timelike or null ([[Def - Causality and the Light Cone]]); the relativity of simultaneity bites only for spacelike-separated events, which are the ones that can be made simultaneous in some frame.

**Is NOT an instance — the delay of a distant signal.** It is *not* an example of the relativity of simultaneity that a distant explosion is seen late because its light takes time to arrive. That delay is a property of the finite *travel* time of light and is fully corrected for in the definition (each event is timed by a local clock present at it, not by when its light reaches a central observer). The relativity of simultaneity survives that correction; it is a consequence of the *constancy* of $c$, not its finiteness. Conflating the two is the single most common misunderstanding of the concept.

**Corollary — the order of spacelike events can be reversed.** If two events have $\Delta t = 0$ in $S$ but $\Delta x \ne 0$, then in a frame $S'$ moving at $+v$ the event with larger $x$ is earlier, and in a frame moving at $-v$ it is later. So for spacelike-separated events there exist frames in which either one precedes the other, and a frame in which they are simultaneous. No such reversal is possible for timelike-separated events, which secures causality.

**Calibration check.** You have understood the definition if you can (i) write down the $S'$-simultaneity line on an $S$-diagram as $t = vx$ and explain why it is the mirror image of the $t'$-axis across the light line; (ii) compute, for two events $1$ km apart and simultaneous in $S$, the time difference $\Delta t' = -\gamma v\,\Delta x/c^2$ a frame at $v = 0.6c$ assigns, and say which event is earlier there; and (iii) state in one sentence why the relativity of simultaneity is *not* about the time light takes to reach the eye.

---

# Unlocked by This

> [!tip] Length Contraction as a Simultaneity Effect *(from §2.3)*
> The relativity of simultaneity is the engine of [[Thm - Length Contraction|length contraction]]: measuring a rod's length means recording both ends *at the same time*, and because "the same time" tilts between frames, the two frames cut the rod's worldsheet along different lines and get different lengths. Every length contraction is a disguised statement about a tilted simultaneity line.

> [!tip] The Resolution of Every Relativistic Paradox *(from §2.1 and §2.3)*
> The [[Ex - Length contraction and the ladder-in-the-barn paradox|ladder-in-the-barn]] and the [[Ex - The twin paradox|twin paradox]] are both dissolved by this one fact. Whenever two frames reach contradictory conclusions, the contradiction lives in an illegitimate identification of two different simultaneity slices as one "now"; locating the word "simultaneously" and asking "in which frame?" is the master key.

> [!tip] Foliations, Time Functions, and the ADM Split *(from General Relativity)*
> A choice of simultaneity surfaces is a **slicing** of spacetime into spacelike hypersurfaces stacked along a time direction. In general relativity this becomes the **ADM (Arnowitt–Deser–Misner) formulation**: one picks a foliation by spacelike slices, a **lapse** function measuring proper time between them and a **shift** vector measuring how spatial coordinates slide, and Einstein's equations become an evolution of the spatial geometry from one slice to the next. The freedom to re-slice — the flat version of which is the tilt $t - vx = \text{const}$ — is the gauge freedom of general relativity, and the absence of a preferred slicing is why "the state of the universe now" is not a diffeomorphism-invariant notion.
