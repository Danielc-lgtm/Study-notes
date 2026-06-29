---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - The Relativity of Simultaneity"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and restore $c$ where a formula reads more naturally with it. Two inertial frames $S$ and $S'$ are in standard configuration, $S'$ moving at velocity $v$ along the common $x$-axis, with $\gamma = (1-v^2)^{-1/2} \ge 1$, related by the [[Def - The Lorentz Transformation|Lorentz transformation]] $t' = \gamma(t - vx)$, $x' = \gamma(x - vt)$ and inverse $x = \gamma(x' + vt')$, $t = \gamma(t' + vx')$. A rod lies along the $x'$-axis at rest in $S'$, occupying $0 \le x' \le L_0$; $L_0$ is its **proper length**. $L$ denotes the length the rod is measured to have in $S$, where it moves at speed $v$. The **worldsheet** of the rod is the strip its two endpoints sweep out in spacetime. Full registry on [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction]].

---

# Statement

> **Length contraction.** Let a rod of proper length $L_0$ lie at rest in the inertial frame $S'$, along the direction of relative motion. In any inertial frame $S$ in which the rod moves at speed $v$ along its length, its measured length — the spatial distance between its two ends taken *at one instant of $S$-time* — is
> $$L = \frac{L_0}{\gamma} = L_0\sqrt{1 - v^2} \qquad\left(\text{with } c: \ L = L_0\sqrt{1 - v^2/c^2}\right),$$
> with $\gamma = (1 - v^2)^{-1/2} \ge 1$. Since $\gamma \ge 1$, $L \le L_0$: **a moving rod is contracted.** The contraction is only along the direction of motion; lengths transverse to the motion are unchanged. The proper length $L_0$ — the length in the rod's own rest frame — is the *greatest* length any inertial frame assigns.

---

# Motivation

Time dilation came almost for free once the Lorentz transformation was in hand; length contraction looks like its obvious mirror image, and the formula $L = L_0/\gamma$ is indeed dual to $T = \gamma T_0$. But length contraction hides a subtlety that time dilation does not, and the entire conceptual payoff of the theorem is in confronting it. The subtlety is this: *what does it even mean to measure the length of a moving rod?* For a stationary rod you lay a ruler against it and read off both ends at your leisure. For a moving rod you cannot — by the time you have marked the far end and walked to the near end, the rod has moved. You must mark *both ends at the same instant*. And "the same instant" is exactly the frame-dependent notion that [[Def - The Relativity of Simultaneity|the relativity of simultaneity]] has just made treacherous.

So length contraction is not really a fact about rulers shrinking; it is a fact about *simultaneity*. The two endpoint-marking events that are simultaneous in the measuring frame $S$ are *not* simultaneous in the rod's frame $S'$ — in $S'$ the far end is marked at a different time than the near end, and because the rod is moving, the two marks do not span the rod's full proper length. This is why the moving rod comes out short: $S$ is, from $S'$'s point of view, measuring the rod's ends at two different moments and catching it "between" the full extent. The motivation for stating the theorem carefully, with the phrase "at one instant of $S$-time" front and centre, is to make this unavoidable: drop the simultaneity clause and the theorem is meaningless.

The reward for taking the clause seriously is the resolution of the most famous paradox in the subject, the ladder-and-barn ([[Ex - Length contraction and the ladder-in-the-barn paradox]]). A ladder longer than a barn can be made to fit inside it — both doors momentarily shut with the ladder wholly within — in the barn's frame, while in the ladder's frame the barn is shorter still and the ladder never fits. The two frames reach opposite conclusions about "is the ladder inside the barn", and the contradiction is real until one realises that "inside the barn" means "both ends within the walls *simultaneously*", and that the simultaneity is exactly what the two frames disagree about. Length contraction, properly understood, is the relativity of simultaneity wearing a ruler.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a rod (or any extended object) is at rest in some frame, with a known proper length, and is being measured in a frame where it moves along its length". Recognising the disguises:

The first disguised source is **"a distance is fixed in one frame and traversed in another"**. A muon falling through the atmosphere sees the *atmosphere* as a moving rod: the column of air, at rest in the Earth frame with proper height $H_0$, is contracted to $H_0/\gamma$ in the muon's frame. The bridge is that any rest-frame distance (the depth of the atmosphere, the length of a racetrack, the separation of two stars) is a proper length, and a frame moving through it measures the contracted value. *Example problem:* a spaceship crosses the $4.2$-light-year gap to Proxima Centauri at $v$ such that $\gamma = 4.2$; in the ship's frame the gap is $1$ light year, crossed in proportionally less proper time.

The second disguised source is **"two events simultaneous in $S$ define a spatial separation"**. Whenever a problem gives two events with $\Delta t = 0$ in $S$, their spatial separation $\Delta x$ is an $S$-length, and the corresponding rest-frame separation is $\gamma\,\Delta x$ (the proper length is the *longer* one). The bridge is the contraction formula read backwards, via the [[Def - The Relativity of Simultaneity|tilted simultaneity line]]. *Example problem:* two firecrackers go off simultaneously in $S$ a distance $D$ apart; in a frame moving at $v$ along the line joining them, the corresponding proper separation is $\gamma D$, and the explosions are not simultaneous.

The third disguised source is **"a moving object's transit time past a fixed marker is measured"**. If an object of unknown length passes a point and its front and back take time $\Delta t$ to pass at speed $v$, the *contracted* length is $L = v\,\Delta t$, from which the proper length is $\gamma v\,\Delta t$. The bridge is that the transit measurement is automatically a single-frame, simultaneous-endpoints measurement. *Example problem:* a train takes $2\ \mu\text{s}$ to pass a signal at $0.8c$; its length in the ground frame is $0.8c \times 2\ \mu\text{s}$, and its proper length is $\gamma$ times that.

**Targets (Output Amplification)**

The conclusion is "$L = L_0/\gamma$, the moving rod is contracted".

Combine the conclusion with **time dilation in the complementary frame**. The same physical event — an object reaching the end of a path — is explained by one frame as the *path* being contracted and by the other as the *clock* being dilated, and the two give the identical transit, because $\gamma$ enters once in each. The further result is the two-frame consistency check, the deepest sanity test in relativity. *Example:* the muon reaches the ground because the Earth frame dilates its lifetime *or* because the muon frame contracts the atmosphere; computing both ways and matching confirms the bookkeeping ([[Thm - Time Dilation]], [[Ex - Time dilation and the cosmic-ray muon]]).

Combine the conclusion with **the relativity of simultaneity to resolve a "fit" paradox**. Length contraction alone produces apparently contradictory verdicts on whether a long object fits in a short container; adjoining the relativity of simultaneity resolves every such paradox by exhibiting the two endpoint events and showing "both inside at once" is frame-dependent. The further result is the full resolution of the ladder-and-barn and pole-vaulter paradoxes. The combination is nonobvious because contraction by itself seems to give a paradox; only with simultaneity does the paradox dissolve. *Example:* [[Ex - Length contraction and the ladder-in-the-barn paradox]].

Combine the conclusion with **invariance of the transverse area to get volume and density**. Since only the longitudinal dimension contracts and transverse dimensions are fixed, a moving volume contracts by $\gamma$ and a moving charge or mass density is enhanced by $\gamma$. The further result is the transformation of densities and the relativistic concentration of fields — the contracted, pancake-shaped Coulomb field of a fast charge. The combination is useful in electromagnetism, where the contraction of charge density is the origin of magnetic forces. *Example:* the field of a relativistic charged particle, flattened transverse to its motion.

---

# Why Is It True

The honest one-line reason is that **measuring a moving rod's length means catching both its ends at the same instant of *your* time, and "the same instant" cuts the rod's worldsheet along a tilted line that spans less than the full proper length.**

Take it slowly with the worldsheet picture. As time passes, each end of the rod traces a worldline; the two worldlines bound a strip in spacetime — the rod's worldsheet, a slab of width "proper length" measured *along the rod's own simultaneity lines*. In the rod's frame $S'$, the natural way to measure the rod is to read both ends at a single $S'$-time, i.e. to cut the worldsheet along a horizontal line of the $S'$-diagram; that cut has length $L_0$, the proper length, by definition. Now the frame $S$ measures the rod by cutting the *same* worldsheet along a line of constant $S$-time. But a line of constant $S$-time is, on the $S'$-diagram, *tilted* (that is the relativity of simultaneity), and a tilted cut across the slanted strip of the worldsheet intercepts a *shorter* span than the straight cut did. The moving rod is short because $S$ slices its worldsheet on the bias.

Equivalently, in the language of the two endpoint-events: $S$ marks the front end and the back end simultaneously (in $S$). Transform those two marking-events to $S'$. Because they are simultaneous in $S$ but spatially separated, they are *not* simultaneous in $S'$ — in $S'$, the back end is marked *later* than the front (by the leading-clocks-lag rule). In the interval between, the rod (at rest in $S'$) has not moved, but $S$'s "back-end mark" lands at a point that, in $S'$, is short of where the back end was when the front was marked. So $S$'s two simultaneous marks straddle less than the full rod: $L < L_0$. The factor is exactly $\gamma$ because the simultaneity offset is $\gamma v L_0$ in time, the rod's frame sees that as a spatial slippage, and the Lorentz factor bookkeeping returns $L_0/\gamma$.

There is no separate "physical shrinking". From the relativistic standpoint nothing contracts in the sense of being squeezed; the two observers simply measure *different things* — $S$ measures the separation of its two simultaneous marks ($E$ and $B$ in the standard diagram), while $S'$ measures the separation of *its* two simultaneous marks ($E$ and $A$). They are different pairs of events on the same worldsheet, and they have different spatial extents. The contraction is the geometry of slicing a worldsheet two ways, not a force.

---

# What Makes This Hard

The single non-obvious step, and the one where essentially everyone stumbles, is that the moving-frame length measurement *requires the two endpoint readings to be simultaneous in the measuring frame*, and that this simultaneity is broken in the rod's frame. People who treat length contraction as a bare formula $L = L_0/\gamma$, dual to time dilation, get the right number but cannot resolve the ladder-and-barn, because the resolution lives entirely in the simultaneity clause they skipped. The most common concrete error is to contract the wrong object in a two-body problem (each frame contracts the *other* object, never its own, and no frame contracts both), and the second is to forget that contraction acts only along the motion, leaving transverse dimensions alone.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write the worldlines of the rod's two ends as lines in $S$ (using the inverse Lorentz transformation on $x' = 0$ and $x' = L_0$). Then impose the measurement condition — *read both ends at the same $S$-time*, say $t = 0$ — and compute the spatial separation of the two ends at that instant. The simultaneity condition is the whole of the work.

**Subgoal decomposition:**

1. **Write the two end-worldlines in $S$.** The near end is $x' = 0$, the far end $x' = L_0$; transform each to $S$.
   - *Hint:* Use $x = \gamma(x' + vt')$ with $x' = 0$ and $x' = L_0$ to get the front and back worldlines parametrically.
   - *Why needed:* The length is the separation of these two worldlines, but only along an $S$-simultaneity line.

2. **Impose simultaneity in $S$.** Choose a single instant $t = 0$ in $S$ and find where each worldline crosses it.
   - *Hint:* The near end passes $x = 0$ at $t = 0$; for the far end, solve its worldline for $x$ at $t = 0$, which forces a *non-zero* $t'$ for that end.
   - *Why needed:* This is the measurement definition, and the non-zero $t'$ is the relativity of simultaneity doing the work.

3. **Read off the separation.** The $S$-distance between the two crossing points is $L$.
   - *Hint:* Following the far end back along its trajectory to make it simultaneous (in $S$) with the near end shifts its position from $\gamma L_0$ to $\gamma L_0 - v(\gamma v L_0) = L_0/\gamma$.
   - *Why needed:* This is the theorem, $L = L_0/\gamma$.

4. **Confirm the proper length is maximal.** Note $L_0$ is recovered as $v \to 0$ and is the largest value, since $\gamma \ge 1$.
   - *Hint:* $\gamma \ge 1$ with equality iff $v = 0$.
   - *Why needed:* It records that the rest-frame length is the longest, dual to "proper time is shortest".

---

# Lemma Decomposition

> [!note]- Lemma 1: A length measurement is two simultaneous endpoint events
> **Statement:** The length of a moving rod in $S$ is, by definition, the spatial separation $|x_{\text{front}} - x_{\text{back}}|$ of its two ends recorded at one common value of $S$-time.
>
> **Hint:** Ask what could possibly go wrong if the two endpoint positions were recorded at different times while the rod moves.
>
> **Why needed:** Without fixing the simultaneity convention the "length" is undefined; this lemma is the definition the whole theorem rests on, and the source of the contraction.
>
> > [!note]- Full proof
> > A rod moving at speed $v$ in $S$ occupies, at $S$-time $t$, the interval $[x_{\text{back}}(t), x_{\text{front}}(t)]$, with both ends advancing at $v$. If one recorded $x_{\text{front}}$ at time $t_1$ and $x_{\text{back}}$ at a later time $t_2 > t_1$, the back end would have advanced by $v(t_2 - t_1)$ in the interim, and the difference $x_{\text{front}}(t_1) - x_{\text{back}}(t_2)$ would be *smaller* than the rod by $v(t_2 - t_1)$ — an artefact of the time mismatch, not a length. To measure a length one must therefore freeze the rod at a single instant: record both ends at one common $S$-time $t_1 = t_2$. This is forced, not conventional, and it is the unique definition that gives the rod's spatial extent in $S$. $\blacksquare$

> [!note]- Lemma 2: The endpoint worldlines in S
> **Statement:** In $S$, the back end of the rod follows $x_{\text{back}} = vt$ and the front end follows $x_{\text{front}} = vt + L_0/\gamma$; equivalently the front-end worldline is $x = \gamma L_0 + vt'$ in terms of its own proper time parameter.
>
> **Hint:** Transform the rest-frame worldlines $x' = 0$ and $x' = L_0$ to $S$ using $x = \gamma(x' + vt')$ and $t = \gamma(t' + vx')$, then eliminate $t'$.
>
> **Why needed:** It provides the explicit lines whose simultaneous-in-$S$ separation is the contracted length.
>
> > [!note]- Full proof
> > The back end is at $x' = 0$ for all $t'$; transforming, $x = \gamma(0 + vt') = \gamma vt'$ and $t = \gamma(t' + 0) = \gamma t'$, so $x_{\text{back}} = vt$. The front end is at $x' = L_0$ for all $t'$; transforming, $x = \gamma(L_0 + vt')$ and $t = \gamma(t' + vL_0)$. Solve the time equation for $t'$: $t' = t/\gamma - vL_0$. Substitute into the position: $x = \gamma L_0 + \gamma v(t/\gamma - vL_0) = \gamma L_0 + vt - \gamma v^2 L_0 = vt + \gamma L_0(1 - v^2) = vt + L_0/\gamma$, using $\gamma(1-v^2) = 1/\gamma$. Thus $x_{\text{front}} = vt + L_0/\gamma$. $\blacksquare$

> [!note]- Lemma 3: The contracted length and its maximality
> **Statement:** At any fixed $S$-time, $x_{\text{front}} - x_{\text{back}} = L_0/\gamma =: L \le L_0$, with equality iff $v = 0$; and $L_0$ is the maximal length over all inertial frames.
>
> **Hint:** Subtract the two worldlines of Lemma 2 at common $t$; then use $\gamma \ge 1$.
>
> **Why needed:** It is the theorem statement, including the "proper length is greatest" claim.
>
> > [!note]- Full proof
> > From Lemma 2, at a common $S$-time $t$, $x_{\text{front}} - x_{\text{back}} = (vt + L_0/\gamma) - vt = L_0/\gamma$. So the measured length in $S$ is $L = L_0/\gamma$. Since $\gamma = (1-v^2)^{-1/2} \ge 1$ with equality iff $v = 0$, we have $L \le L_0$, equality iff the rod is at rest in $S$. Any inertial frame moving relative to the rod has $v \ne 0$, hence $\gamma > 1$ and $L < L_0$; the rest frame ($v = 0$) gives the maximum $L = L_0$. Thus the proper length is the greatest length assigned by any inertial frame. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> A rod of proper length $L_0$ lies at rest in $S'$ along the $x'$-axis, its ends at $x' = 0$ (back) and $x' = L_0$ (front), for all $t'$. We measure its length in $S$, where it moves at speed $v$.
>
> *The measurement.* By Lemma 1, the length in $S$ is the spatial separation of the two ends recorded at one common value of $S$-time. Take that instant to be $t = 0$.
>
> *The endpoint positions in $S$ at $t = 0$.* The back end's worldline (from $x' = 0$) is $x_{\text{back}} = vt$, so at $t = 0$ it is at $x_{\text{back}} = 0$. The front end's worldline (from $x' = L_0$), computed in Lemma 2 by transforming $x = \gamma(x' + vt')$, $t = \gamma(t' + vx')$ and eliminating $t'$, is $x_{\text{front}} = vt + L_0/\gamma$, so at $t = 0$ it is at $x_{\text{front}} = L_0/\gamma$.
>
> *Reading off.* The measured length is
> $$L = x_{\text{front}} - x_{\text{back}} = \frac{L_0}{\gamma} - 0 = \frac{L_0}{\gamma} = L_0\sqrt{1 - v^2}.$$
> Restoring $c$: $L = L_0\sqrt{1 - v^2/c^2}$. Since $\gamma \ge 1$, $L \le L_0$, with equality iff $v = 0$: the moving rod is contracted, and the rest-frame (proper) length $L_0$ is the maximal length (Lemma 3).
>
> *The role of simultaneity.* The two events $(t = 0,\ x = 0)$ and $(t = 0,\ x = L_0/\gamma)$ are simultaneous in $S$. Transforming the front-end event to $S'$ gives $t'_{\text{front}} = \gamma(0 - v\,L_0/\gamma) = -vL_0 \ne 0$, while the back-end event has $t'_{\text{back}} = 0$: the two measurements are *not* simultaneous in the rod's frame $S'$. This is the relativity of simultaneity ([[Def - The Relativity of Simultaneity]]); it is the reason the moving frame finds a shorter length, and it is what is suppressed if one treats the formula as a bare dual of time dilation.
>
> *Transverse directions.* The boost leaves $y, z$ unchanged, so a rod held perpendicular to the motion is uncontracted; contraction acts only along the direction of relative velocity. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The relativistic heavy-ion collider (nuclear physics).** Gold nuclei accelerated to $\gamma \approx 100$ at RHIC, and lead nuclei to $\gamma \approx 2700$ at the LHC, are Lorentz-contracted in the beam direction from spheres into thin pancakes — flattened by the factor $\gamma$. The geometry of the collision, and the initial conditions of the quark–gluon plasma that forms, depend on modelling the colliding matter as contracted disks rather than spheres. The application is the bridge "rest-frame size $=$ proper length $\Rightarrow$ beam-frame size divides by $\gamma$", and it is nonobvious in that the *shape* of a fundamental object becomes frame-dependent.

**The pancake Coulomb field and synchrotron radiation (electromagnetism).** The electric field of a charge at rest is spherically symmetric; for a charge moving at $\gamma \gg 1$, length contraction flattens the field into a disk transverse to the motion, with the longitudinal extent reduced by $\gamma$ and the transverse field enhanced. This concentration is why an ultrarelativistic charge passing a detector delivers a sharp, brief transverse field pulse, and it underlies the angular collimation of synchrotron radiation into a forward cone of half-angle $\sim 1/\gamma$. The application combines length contraction with the transformation of fields, and it is surprising because a static, isotropic field becomes a frame-dependent pancake.

**Crossing the galaxy within a human lifetime (astronautics, thought-experiment).** A traveller accelerating to a Lorentz factor of $\gamma \sim 10^4$ would find the $\sim 10^5$-light-year diameter of the Milky Way contracted to $\sim 10$ light years, crossable in a few years of proper time — even though the Earth frame records $\sim 10^5$ years elapsing. The application is "rest-frame distance $=$ proper length $\Rightarrow$ traveller-frame distance divides by $\gamma$", dual to the time-dilation account in the Earth frame, and it is the cleanest illustration that length contraction and time dilation are two views of one fact: the trip is short for the traveller because the *distance* is short (their view) or because their *clock* is slow (Earth's view).

---

# Bridges

- **[[Thm - Time Dilation]]** — the reciprocal effect, sharing the factor $\gamma$. Time dilation lengthens the time between two events at the same place; length contraction shortens the length of a moving rod. A single observable — an object reaching the end of a path — is explained by length contraction in the object's frame and time dilation in the path's frame, the two agreeing because $\gamma$ enters once in each. Both descend from the [[Def - The Relativity of Simultaneity|relativity of simultaneity]], time dilation via the worldline and length contraction via the worldsheet of the object.

- **[[Def - The Relativity of Simultaneity]]** — the cause, not merely a relative. Length contraction *is* the relativity of simultaneity applied to a measurement: the two simultaneous-in-$S$ endpoint readings are non-simultaneous in $S'$, by exactly the offset $\gamma v L_0$, and that offset is the whole of the contraction. Every length contraction is a tilted cut through a worldsheet, and every "fit" paradox is resolved by exhibiting the two endpoint events and asking in which frame they are simultaneous.

- **[[Ex - Length contraction and the ladder-in-the-barn paradox]]** — the canonical stress test. The ladder-and-barn shows that contraction *alone* yields contradictory verdicts ("the ladder fits" vs "it does not"), and that the contradiction dissolves only when the relativity of simultaneity is adjoined: "both ends inside the barn at once" is true in the barn frame and false in the ladder frame because the two doors-shut events are simultaneous in one and not the other.

- **Charge-density transformation and magnetism (electromagnetism)** — the field-theoretic consequence. Because only the longitudinal dimension contracts, a moving charge distribution has its density enhanced by $\gamma$; applied to the positive lattice and drifting electrons of a current-carrying wire, the differential contraction in a test charge's rest frame unbalances the charge densities and produces a net electric field — which is the magnetic force seen in the wire's frame. Length contraction is thus a hidden ingredient of magnetism.

---

# Unlocked by This

> [!tip] Lorentz Contraction of the Field of a Moving Charge *(from Electromagnetism)*
> Applying length contraction to the field lines of a point charge turns the spherically symmetric Coulomb field into a **pancake** flattened transverse to the motion: the longitudinal extent shrinks by $\gamma$, the transverse field strengthens, and an ultrarelativistic charge carries an almost planar burst of transverse field. The frame-dependent rearrangement of these contracted fields, applied to the charges in a current-carrying wire, *is* the **magnetic force** — magnetism is electrostatics seen after a boost, with length contraction and the relativity of simultaneity supplying the apparent charge imbalance. This is the cleanest demonstration that $\mathbf{E}$ and $\mathbf{B}$ are frame-dependent slices of one tensor $F_{\mu\nu}$.

> [!tip] Proper Length, Rigidity, and Born-Rigid Motion *(from Relativistic Mechanics)*
> Once length is frame-dependent, the notion of a **rigid body** must be rebuilt, because a body cannot keep a fixed length in *every* frame at once. The relativistic replacement is **Born rigidity**: a body is rigid if every infinitesimal element keeps its proper length, measured in the momentarily comoving frame, throughout the motion. A theorem of Herglotz and Noether then shows that Born-rigid motions are extremely restricted — a Born-rigid body cannot be set spinning from rest, and its accelerated motions form only a small family — which is the rigorous form of "there are no perfectly rigid bodies" ([[Def - Causality and the Light Cone]]). The proper length of this page is the invariant that Born rigidity preserves.
