---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - Proper Time"
  - "Def - The Spacetime Interval"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and restore $c$ where a formula is more recognisable with it. Two inertial frames $S$ and $S'$ are in standard configuration, $S'$ moving at velocity $v$ along the $x$-axis of $S$, with $\gamma = (1-v^2)^{-1/2} \ge 1$, related by the [[Def - The Lorentz Transformation|Lorentz transformation]] $t' = \gamma(t - vx)$, $x' = \gamma(x - vt)$ and its inverse $t = \gamma(t' + vx')$, $x = \gamma(x' + vt')$. A clock at rest in $S'$ measures its **proper time** $T_0$ between two of its own ticks (two events at the same place in $S'$); $T$ denotes the **coordinate time** between the same two events in $S$. The [[Def - The Spacetime Interval|interval]] is $\Delta s^2 = \Delta t^2 - \Delta x^2$ (mostly-minus signature, timelike $\Delta s^2 > 0$). Full registry on [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction]].

---

# Statement

> **Time dilation.** Let a clock be at rest in the inertial frame $S'$, ticking at intervals $T_0$ of its proper time (so two successive ticks are events at the same spatial point of $S'$, separated by $\Delta t' = T_0$, $\Delta x' = 0$). Then in any inertial frame $S$ in which the clock moves at speed $v$, the coordinate time between the same two ticks is
> $$T = \gamma\, T_0 = \frac{T_0}{\sqrt{1 - v^2}} \qquad\left(\text{with } c: \ T = \frac{T_0}{\sqrt{1 - v^2/c^2}}\right),$$
> with $\gamma = (1 - v^2)^{-1/2} \ge 1$. Since $\gamma \ge 1$, $T \ge T_0$: **a moving clock runs slow.** Equivalently, the proper time $T_0$ — the time read by a single clock present at both events — is the *shortest* coordinate time any inertial frame assigns to that pair of events, and it equals the square root of the invariant interval, $T_0 = \sqrt{\Delta s^2}$.

---

# Motivation

The [[Def - The Lorentz Transformation|Lorentz transformation]] has already told us that elapsed time is frame-dependent, but a transformation law is abstract; time dilation is where that abstraction becomes a number you could, in principle, watch on two clocks. The question it answers is the most natural one a person could ask after meeting the relativity of simultaneity: if observers cannot agree on whether two events are simultaneous, can they at least agree on how *fast* a given clock ticks? The answer is no, and the disagreement has a precise and universal form — every observer sees a moving clock tick slow by the factor $\gamma$.

What makes the result more than a curiosity is its universality across the *kind* of clock. The derivation uses nothing about the clock's mechanism, so the slowing cannot be a mechanical artefact — it is not that a moving pendulum swings lazily or a moving spring stiffens. The same factor $\gamma$ governs a pendulum, a quartz oscillator, a beating heart, the decay of an unstable particle, and the ticking of an atomic transition. The only honest interpretation is that *time itself* runs slow in a moving frame; the clocks merely report it faithfully. This is why the cosmic-ray muon reaches the ground ([[Ex - Time dilation and the cosmic-ray muon]]) and why particle accelerators must account for the extended lifetimes of the unstable particles they produce.

The theorem also installs the chapter's first genuine *invariant*. Behind the frame-dependent coordinate time $T$ stands the frame-independent [[Def - Proper Time|proper time]] $T_0$, the time the clock actually accumulates, equal to $\sqrt{\Delta s^2}$ and the same for every observer. Time dilation is then read as: of all the coordinate times different frames assign to a pair of events, the smallest is the proper time, achieved in the one frame where the events coincide in space. This "proper time is shortest" statement is the seed of the geometry of the next chapters — it is the infinitesimal version of the fact that, in Minkowski space, the straight worldline between two events has the *longest* total proper time, the geometric content of the twin paradox.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "two events occur at the same place in some inertial frame, so a single clock is present at both". The point of input broadening is to recognise this hypothesis in its many disguises.

The first disguised source is **"an object has a stated rest-frame lifetime, period, or duration"**. Any time interval attached to an object *in its own frame* — a particle's half-life, a clock's period, the duration of a process happening at a fixed point of the object — is automatically a proper time, because the start and end events occur at the same place in the object's rest frame. The bridge is that "the object's own duration" $=$ "two events at the same place in the object's frame" $=$ proper time. So whenever a problem says "in its rest frame the muon lives $\tau$" or "the clock ticks every $T_0$ on board", that $\tau$ or $T_0$ is the proper time and the lab sees $\gamma\tau$ or $\gamma T_0$. *Example problem:* a particle with rest-frame lifetime $\tau$ moves at $v$; how far does it travel before decaying? (Answer: $\gamma v\tau$, the dilated lifetime times the speed.)

The second disguised source is **"two events are connected by a timelike worldline that is straight"**. Given any two timelike-separated events, the inertial frame in which they occur at the same place is the rest frame of the straight worldline joining them, and the proper time between them is $\sqrt{\Delta s^2}$. The bridge is the [[Thm - Invariance of the Spacetime Interval|invariance of the interval]]: $\Delta s^2$ is computed in *any* convenient frame and its square root is the proper time. *Example problem:* two events have $S$-coordinates differing by $(\Delta t, \Delta x) = (5, 3)$; what does a clock that is present at both read? (Answer: $\sqrt{25 - 9} = 4$, no boost required.)

The third disguised source is **"a frequency or rate is measured for a moving source"**. A rate is the reciprocal of a period, so a moving source's emitted period is dilated and its observed rate (before any additional Doppler shift from changing distance) is reduced by $\gamma$ — the transverse Doppler effect. The bridge is period $=$ proper time $\Rightarrow$ rate divides by $\gamma$. *Example problem:* an atom moving transverse to the line of sight emits light of rest-frame frequency $\nu_0$; the observed frequency is $\nu_0/\gamma$, a purely time-dilation (second-order Doppler) shift with no first-order component.

**Targets (Output Amplification)**

The conclusion is "$T = \gamma T_0$, the moving clock's tick interval is dilated".

Combine the conclusion with **the symmetry of relativity**. Each of two inertial observers sees the *other's* clock dilated by the same $\gamma$ — there is no contradiction, because they compare different pairs of events (each compares one of its own clocks against a succession of the other frame's clocks). The further result is that "moving clocks run slow" is a *mutual*, consistent relation, and reconciling it requires the [[Def - The Relativity of Simultaneity|relativity of simultaneity]]: the two observers disagree about which clock-readings to compare. The combination is nonobvious because the mutuality looks paradoxical until one tracks the simultaneity slices. *Example:* the resolution of the symmetric mutual-slowness puzzle, and ultimately the [[Ex - The twin paradox|twin paradox]].

Combine the conclusion with **a closed (round-trip) worldline**. If a clock leaves an inertial observer, travels, and returns, the dilations on each leg accumulate, and the travelling clock reads less total time than the stay-at-home clock — an *absolute*, frame-independent difference, because the two clocks are compared at the same two events (departure and reunion) where they are co-located. The further result is the differential ageing of the twin paradox, and its geometric form: the straight worldline has the longest proper time ([[Thm - The Reversed Triangle Inequality]]). The combination is useful because it converts the relative, mutual effect into an absolute, measurable one. *Example:* [[Ex - Hafele–Keating and the flying-clock experiment]], where flown clocks return having ticked less.

Combine the conclusion with **length contraction in the orthogonal frame**. The very same physical fact — the muon reaching the ground — is explained by the Earth frame as time dilation of the muon's lifetime and by the muon frame as [[Thm - Length Contraction|length contraction]] of the atmosphere; the two descriptions agree because $\gamma$ appears once in each. The further result is the consistency check that any single observable can be computed in either frame with the same answer. The combination is nonobvious because the *mechanism* differs (a slow clock versus a short path) while the *outcome* is identical, which is the deepest sanity test in the subject.

---

# Why Is It True

The cleanest way to see why a moving clock must run slow, with no algebra at all, is the **light clock**, and it shows that the effect is forced by the constancy of $c$ together with the one fact about lengths transverse to the motion that does *not* change.

Build a clock from two mirrors a height $h$ apart, with a light pulse bouncing between them; one round trip is one tick. In the clock's rest frame the pulse travels straight up and down, a distance $2h$, so one tick takes $T_0 = 2h$ (with $c = 1$). Now watch the same clock from a frame in which it moves horizontally at speed $v$. The mirrors are displaced sideways between bounces, so the pulse must travel along a slanted path — the hypotenuse of a right triangle whose vertical leg is $h$ and whose horizontal leg is the sideways drift. The pulse therefore covers a *longer* distance per tick. But — and this is the entire content — it still travels at speed $c = 1$, by the second postulate, no faster for being slanted. A longer path at the same speed takes longer: the tick is dilated. The transverse height $h$ is the same in both frames (lengths perpendicular to the motion are uncontracted, by a symmetry argument: a transverse contraction would let two identical rods pass perpendicular to each other each "shorter" than the other, a contradiction), so the geometry is an honest right triangle and Pythagoras delivers the factor exactly.

**The one-sentence mechanism: a moving light clock's pulse has to cover a longer, slanted path at the same speed $c$, so its tick takes longer — by exactly the ratio of hypotenuse to height, which is $\gamma$.**

The algebraic derivation says the same thing in coordinates. The clock sits at a fixed place in its own frame, $x' = 0$, so its two ticks are separated by $\Delta x' = 0$ and $\Delta t' = T_0$. The inverse Lorentz transformation gives the $S$-time directly: $t = \gamma(t' + vx')$, and with $\Delta x' = 0$ this is simply $\Delta t = \gamma\,\Delta t' = \gamma T_0$. The condition $\Delta x' = 0$ — the clock being present at both events — is what selects the proper-time frame and is the whole reason the answer comes out clean.

And the invariant derivation makes the "proper time is shortest" reading transparent. The interval between the ticks is frame-independent: $\Delta s^2 = \Delta t'^2 - \Delta x'^2 = T_0^2 - 0 = T_0^2$ in the clock's frame, and $\Delta s^2 = \Delta t^2 - \Delta x^2$ in $S$. Equating, $\Delta t^2 = T_0^2 + \Delta x^2 \ge T_0^2$, so $\Delta t \ge T_0$ with equality only when $\Delta x = 0$. The proper time is the smallest coordinate time because it is the case where *all* of the interval is "time" and none is "space"; any frame that sees the clock move spends some of the fixed interval-budget on spatial separation, leaving a larger time component. Time dilation is the Pythagorean fact that, with a minus sign, adding spatial separation to a fixed interval *increases* the time.

---

# What Makes This Hard

The algebra is a one-line substitution; the difficulty is conceptual and almost always a bookkeeping slip about which frame holds the clock. The non-obvious step is recognising that $T_0$ must be the *proper* time — the interval measured by a single clock present at *both* events, which forces $\Delta x' = 0$ — and that the inverse transformation $t = \gamma(t' + vx')$, not the forward one, is the one to use when you know the primed (rest-frame) data and want the unprimed. The most common error is to apply $T = \gamma T_0$ with the roles of the two frames swapped, "deriving" that the moving clock runs fast; the second most common is the apparent paradox that each observer sees the other's clock slow, which is consistent only once one tracks the [[Def - The Relativity of Simultaneity|relativity of simultaneity]] and realises the two observers compare different event pairs.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
A clock at rest in $S'$ has its two ticks at the same place, $\Delta x' = 0$, $\Delta t' = T_0$. Feed this into the inverse Lorentz transformation to read off $\Delta t$ in $S$; the $\Delta x' = 0$ collapses everything to $\Delta t = \gamma T_0$. Confirm with the invariant interval, which simultaneously proves the "shortest" claim.

**Subgoal decomposition:**

1. **Identify the rest-frame data.** The clock is at one place in $S'$, so successive ticks have $\Delta x' = 0$ and $\Delta t' = T_0$.
   - *Hint:* "At rest in $S'$" means the spatial coordinate $x'$ does not change between ticks.
   - *Why needed:* The vanishing of $\Delta x'$ is what makes the transformation collapse to a single factor of $\gamma$.

2. **Apply the inverse Lorentz transformation for $t$.** Use $\Delta t = \gamma(\Delta t' + v\,\Delta x')$, the inverse (rest-frame $\to$ lab) form.
   - *Hint:* You know primed quantities and want unprimed; that is the *inverse* transformation, with $+v$.
   - *Why needed:* It expresses the lab-time interval directly in terms of the proper-time interval.

3. **Set $\Delta x' = 0$ and read off the result.** $\Delta t = \gamma\,\Delta t' = \gamma T_0$.
   - *Hint:* The spatial term drops out entirely.
   - *Why needed:* This is the theorem.

4. **Confirm via the interval and get "shortest".** Compute $\Delta s^2 = \Delta t'^2 - \Delta x'^2 = T_0^2$ in $S'$ and $= \Delta t^2 - \Delta x^2$ in $S$; equate to get $\Delta t^2 = T_0^2 + \Delta x^2 \ge T_0^2$.
   - *Hint:* The interval is frame-independent ([[Thm - Invariance of the Spacetime Interval]]); evaluate it in the easy frame.
   - *Why needed:* It re-derives $T \ge T_0$ frame-independently and shows the proper time is the minimum coordinate time.

---

# Lemma Decomposition

> [!note]- Lemma 1: Transverse lengths are unchanged
> **Statement:** A length measured perpendicular to the direction of relative motion is the same in both frames; in particular the height $h$ of the light clock is identical in $S$ and $S'$.
>
> **Hint:** Suppose a transverse length contracted by some factor $f(v)$; consider two identical rods held perpendicular to the relative motion and use the symmetry between the frames.
>
> **Why needed:** The light-clock derivation uses an honest right triangle with vertical leg $h$; if $h$ changed between frames the Pythagorean step would be invalid.
>
> > [!note]- Full proof
> > Let two frames $S$ and $S'$ move relative to each other along $x$, and let each carry a rod of rest length $\ell$ held along the $y$-axis (transverse to the motion). Suppose transverse lengths transform by a factor $f(v)$ depending only on the relative speed: $S$ measures $S'$'s rod to be $f(v)\ell$. By the principle of relativity neither frame is preferred, so $S'$ must measure $S$'s rod to be $f(v)\ell$ by the same rule. Now arrange the two rods to coincide along the $y$-axis at the instant the origins pass (a transverse coincidence is a local, frame-independent fact — the rods either overlap or they don't). If $f(v) < 1$, then $S$ says $S'$'s rod is shorter than its own, i.e. $S'$'s rod tip falls *inside* $S$'s; but $S'$ says $S$'s rod is shorter, i.e. $S$'s rod tip falls inside $S'$'s — a direct contradiction, since the tips' relative position is a single physical fact. Likewise $f(v) > 1$ is contradictory. Hence $f(v) = 1$: transverse lengths are invariant. $\blacksquare$

> [!note]- Lemma 2: The light-clock tick dilates by γ
> **Statement:** A light clock of rest-frame tick $T_0 = 2h$ (one round trip of a pulse between mirrors a height $h$ apart) has tick $T = \gamma T_0$ in a frame where it moves at speed $v$.
>
> **Hint:** In the moving frame the pulse travels the hypotenuse of a right triangle with vertical leg $h$ and horizontal leg $\tfrac12 vT$ per half-tick; equate the slant distance to $c = 1$ times the half-tick time and solve.
>
> **Why needed:** It is the pictorial derivation that makes the universality (mechanism-independence) of time dilation visible, and it confirms the algebraic factor geometrically.
>
> > [!note]- Full proof
> > Work in the frame $S$ where the clock moves at speed $v$ along $x$; let $T$ be the full-tick (round-trip) time in $S$, so each one-way leg takes $T/2$. By Lemma 1 the mirror separation is $h$ in $S$ as well. During one one-way leg the clock drifts horizontally by $v\,(T/2)$, so the pulse, starting at one mirror and ending at the other, travels the hypotenuse of a right triangle with legs $h$ (vertical) and $vT/2$ (horizontal): a distance $\sqrt{h^2 + (vT/2)^2}$. The pulse moves at speed $c = 1$, so this distance equals $T/2$:
> > $$\frac{T}{2} = \sqrt{h^2 + \left(\frac{vT}{2}\right)^2}.$$
> > Squaring, $T^2/4 = h^2 + v^2 T^2/4$, hence $(T^2/4)(1 - v^2) = h^2$, so $T = \dfrac{2h}{\sqrt{1-v^2}} = \gamma\,(2h) = \gamma T_0$. Restoring $c$: $T = \gamma T_0$ with $\gamma = (1 - v^2/c^2)^{-1/2}$. $\blacksquare$

> [!note]- Lemma 3: The proper time is the shortest coordinate time
> **Statement:** For two timelike-separated events, the coordinate time $\Delta t$ in any inertial frame satisfies $\Delta t \ge \sqrt{\Delta s^2} = T_0$, with equality exactly in the frame where the events are co-located.
>
> **Hint:** Use that the interval $\Delta s^2 = \Delta t^2 - \Delta x^2$ is frame-independent and non-negative for timelike separation; solve for $\Delta t$.
>
> **Why needed:** It is the invariant content of the theorem — the statement that survives without reference to any clock — and the bridge to the reversed triangle inequality and the geodesic principle.
>
> > [!note]- Full proof
> > The [[Def - The Spacetime Interval|interval]] $\Delta s^2 = \Delta t^2 - \Delta x^2$ is invariant under [[Def - The Lorentz Transformation|Lorentz transformations]] ([[Thm - Invariance of the Spacetime Interval]]). For a timelike pair $\Delta s^2 > 0$. In the rest frame of the straight worldline joining them, $\Delta x' = 0$, so $\Delta s^2 = \Delta t'^2$, i.e. $\Delta t' = \sqrt{\Delta s^2} =: T_0$ is the proper time. In any other frame $\Delta t^2 = \Delta s^2 + \Delta x^2 = T_0^2 + \Delta x^2 \ge T_0^2$, so $\Delta t \ge T_0$, with equality iff $\Delta x = 0$, i.e. iff the frame is the co-location (rest) frame. Thus the proper time is the minimum coordinate time. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let the clock be at rest in $S'$, ticking at intervals $T_0$ of its proper time. Two successive ticks are events at the same spatial point of $S'$, so their coordinate differences in $S'$ are $\Delta t' = T_0$ and $\Delta x' = \Delta y' = \Delta z' = 0$.
>
> Because the [[Def - The Lorentz Transformation|Lorentz transformation]] is linear, it acts on coordinate differences exactly as on coordinates. The inverse boost (expressing $S$-coordinates in terms of $S'$-coordinates, $S'$ moving at $+v$ in $S$) gives
> $$\Delta t = \gamma(\Delta t' + v\,\Delta x') = \gamma(T_0 + v\cdot 0) = \gamma T_0.$$
> Hence the coordinate time in $S$ between the two ticks is $T = \gamma T_0$, with $\gamma = (1 - v^2)^{-1/2} \ge 1$ (restoring $c$: $\gamma = (1 - v^2/c^2)^{-1/2}$). Since $\gamma \ge 1$, $T \ge T_0$: the moving clock runs slow.
>
> For the invariant characterisation, the interval between the ticks is frame-independent (Lemma 3, via [[Thm - Invariance of the Spacetime Interval]]): in $S'$ it is $\Delta s^2 = T_0^2 - 0 = T_0^2$, and in $S$ it is $\Delta s^2 = \Delta t^2 - \Delta x^2$. Equating, $\Delta t^2 = T_0^2 + \Delta x^2 \ge T_0^2$, so $T_0 = \sqrt{\Delta s^2}$ is the shortest coordinate time, attained in the rest frame ($\Delta x = 0$).
>
> The geometric derivation (Lemmas 1–2) confirms the factor independently: a light clock's pulse traverses the hypotenuse $\sqrt{h^2 + (vT/2)^2} = T/2$ per one-way leg, where the transverse height $h$ is frame-invariant (Lemma 1), yielding $T = 2h/\sqrt{1-v^2} = \gamma T_0$. The agreement of the coordinate, invariant, and light-clock derivations, and the mechanism-independence of the light-clock argument, establish that the dilation is a property of time itself, not of any particular clock. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The decay length of an unstable particle (particle physics).** A particle with rest-frame mean lifetime $\tau$ produced at speed $v$ in a detector travels a mean distance $\gamma v\tau$ before decaying — its *decay length* — because its lifetime is dilated to $\gamma\tau$ in the lab. Detectors for short-lived particles (pions, muons, charmed mesons) are sized to this length, and measuring the decay length is a standard way to infer a particle's lifetime. The application is the bridge "rest-frame lifetime $=$ proper time", and it is nonobvious only in that an elementary, structureless particle has no internal clock yet still "lives longer" when fast — proving the effect is in time, not machinery.

**The transverse Doppler effect (atomic physics / astronomy).** An atom moving with speed $v$ transverse to the line of sight emits light whose observed frequency is *red*-shifted to $\nu_0/\gamma$ purely by time dilation, with no first-order Doppler contribution (the source is, at the instant of emission, neither approaching nor receding). This second-order shift was measured by Ives and Stilwell in 1938 and is a direct laboratory confirmation of $T = \gamma T_0$. The application is "emitted period $=$ proper time $\Rightarrow$ observed rate divides by $\gamma$", and it is surprising because the naive Doppler formula, which keys on radial velocity, predicts *no* shift for transverse motion.

**The Global Positioning System (engineering / general relativity).** GPS satellites carry atomic clocks that, by special-relativistic time dilation from their orbital speed, run slow by about $7\ \mu\text{s}$ per day relative to ground clocks — while general-relativistic gravitational time dilation makes them run *fast* by about $45\ \mu\text{s}$ per day, for a net $+38\ \mu\text{s}$/day that must be corrected or positions would drift by $\sim 10$ km daily. The application combines this theorem with its gravitational analogue ([[Ex - Hafele–Keating and the flying-clock experiment]]); it is out-of-distribution because a relativistic effect of one part in $10^{10}$ turns out to be load-bearing for everyday navigation.

---

# Bridges

- **[[Thm - Length Contraction]]** — the dual effect, and the same factor $\gamma$. Where time dilation lengthens the *time* between two events at the same place, length contraction shortens the *length* of a moving rod; the two are reciprocal sides of one coin, and a single observable (the muon reaching the ground) is explained by time dilation in one frame and length contraction in the orthogonal frame. Both are consequences of the [[Def - The Relativity of Simultaneity|relativity of simultaneity]] acting on the worldline (for time) or worldsheet (for length) of an object.

- **[[Thm - The Reversed Triangle Inequality]]** — the global form of "proper time is shortest". Time dilation says the proper time between two events is the minimum coordinate time *for a single boost*; the reversed triangle inequality says, among *all* worldlines joining two timelike-separated events, the straight (inertial) one has the *longest* total proper time, and any bent worldline accumulates less. The infinitesimal "$\Delta t \ge T_0$" of this theorem integrates, along a bent worldline, into the differential ageing of the [[Ex - The twin paradox|twin paradox]].

- **[[Def - Proper Time]]** — the invariant this theorem reveals. The proper time $T_0 = \sqrt{\Delta s^2}$ is the frame-independent object standing behind the frame-dependent coordinate time $T$; differentiated, $d\tau = \sqrt{ds^2}$ is the natural parameter along a [[Def - Worldline of a Particle|worldline]], the one with respect to which four-velocity and four-acceleration are defined. Time dilation is the statement $dt = \gamma\,d\tau$ relating coordinate time to proper time along a worldline.

- **Gravitational time dilation (general relativity)** — the curved-spacetime sibling. Replacing the flat metric $\eta_{\mu\nu}$ by $g_{\mu\nu}(x)$, the proper time becomes $\int\sqrt{g_{\mu\nu}dx^\mu dx^\nu}$, and the metric component $g_{00}$ that converts coordinate time to proper time varies with position: a clock deeper in a gravitational potential, where $g_{00}$ is smaller, ticks slower than one higher up. Kinematic time dilation (this theorem) and gravitational time dilation together account for the full Hafele–Keating and GPS effects.

---

# Unlocked by This

> [!tip] The Geodesic Principle and Maximal Proper Time *(from General Relativity)*
> "Proper time is the shortest coordinate time" between events co-located in some frame is the local seed of the variational principle of general relativity: a freely-falling body follows the **timelike geodesic** that *extremises* (in fact locally maximises) the proper time $\int\sqrt{g_{\mu\nu}dx^\mu dx^\nu}$ between two events. Gravity is not a force in this picture but the bending of these maximal-proper-time worldlines by spacetime curvature, and the convergence of nearby geodesics is **tidal gravity**. The flat-space fact that a straight worldline ages most ([[Thm - The Reversed Triangle Inequality]]) becomes, with curvature, the statement that gravitating bodies fall along the worldlines of greatest ageing.

> [!tip] The Relativistic Mass–Energy of Motion *(from Relativistic Dynamics)*
> The factor $\gamma$ that dilates time is the same $\gamma$ that appears in relativistic energy $E = \gamma m c^2$ and momentum $\mathbf{p} = \gamma m\mathbf{v}$, because both come from differentiating an object's position with respect to its **proper time** rather than coordinate time. The four-velocity $U = dX/d\tau$ has the extra factor $\gamma = dt/d\tau$ built in, and contracting it with mass gives the four-momentum whose time component is the energy. Time dilation is thus the kinematic root of $E = mc^2$: the rest energy is the energy of a clock ticking its own proper time, and the kinetic part is the surplus from the dilation.
