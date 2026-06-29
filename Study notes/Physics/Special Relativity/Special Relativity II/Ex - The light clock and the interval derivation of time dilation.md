---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Thm - Time Dilation"
  - "Def - The Spacetime Interval"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

Derive the time-dilation factor $\gamma$ by three independent routes and confirm they agree. Work with $c = 1$, restoring $c$ where helpful.

1. **Light clock.** A clock is built from two parallel mirrors a height $h$ apart, with a light pulse bouncing between them; one round trip is one tick. In the clock's rest frame, find the tick period $T_0$. Then, viewing the clock from a frame in which it moves horizontally at speed $v$, find the tick period $T$ by applying Pythagoras to the slanted light path, and show $T = \gamma T_0$.
2. **Why the height does not change.** The light-clock argument needs the mirror separation $h$ to be the same in both frames. Prove that lengths *transverse* to the motion are unchanged, by a symmetry argument with two perpendicular rods.
3. **Interval / Lorentz route.** Re-derive $T = \gamma T_0$ purely algebraically: a clock at rest in $S'$ has two ticks separated by $\Delta x' = 0$, $\Delta t' = T_0$; apply the inverse [[Def - The Lorentz Transformation|Lorentz transformation]] to get $\Delta t$. Then show the same result follows from the invariance of the [[Def - The Spacetime Interval|interval]], and that this route additionally proves the proper time is the *shortest* coordinate time.
4. Confirm all three routes give the identical $\gamma = (1 - v^2)^{-1/2}$, and state which route best displays *why* the dilation occurs (mechanism) versus *that* it occurs (invariance).

**Recall:**

![[Thm - Time Dilation#Statement]]

The [[Def - The Spacetime Interval|interval]] $\Delta s^2 = \Delta t^2 - \Delta x^2$ is [[Thm - Invariance of the Spacetime Interval|invariant]] under [[Def - The Lorentz Transformation|Lorentz transformations]]. The clock's **proper time** is the time between two of its ticks measured in its own rest frame (where the ticks occur at the same place). The speed of light is $c = 1$ in *every* frame, regardless of the clock's motion — the second postulate, and the only physical input the light-clock argument needs.

---

# Convergent Strategy

**Problem class.** A *derive-a-result-multiple-ways* problem, building fluency by triangulating one fact (the factor $\gamma$) from a geometric, a symmetry, and an algebraic argument. The [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction#Problem-Solving Strategy|topic strategy]]'s deepest sanity check — that independent routes must agree — is the whole point.

**Assumption pattern.** Each route leans on a different minimal input. The light clock uses only the constancy of $c$ plus the invariance of transverse length. The Lorentz route uses the transformation directly, with the clock's $\Delta x' = 0$ doing the work. The interval route uses frame-independence of $\Delta s^2$ and yields the "shortest" statement for free.

**Theorem routing.** Part 1 sets up the light clock and applies Pythagoras to the slant path. Part 2 proves transverse invariance by the two-perpendicular-rods symmetry argument (a lemma of [[Thm - Time Dilation]]). Part 3 routes through the inverse [[Def - The Lorentz Transformation|Lorentz transformation]] ($\Delta t = \gamma(\Delta t' + v\Delta x')$ with $\Delta x' = 0$) and then through [[Thm - Invariance of the Spacetime Interval|interval invariance]]. Part 4 compares.

**Key decision point.** The crux of part 1 is realising that the slanted light pulse, though it travels a *longer* path, still moves at exactly $c$ — it is not faster for being slanted. A longer path at the same speed takes longer; that is the entire mechanism. The crux of part 3 is using the *inverse* transformation (rest-frame data known, lab-frame wanted) and setting $\Delta x' = 0$, which collapses the formula to a single $\gamma$.

---

# Legal Operations Used

1. **Use time dilation: a moving clock runs slow by $\gamma$** (operation 3 from the topic page). This exercise *derives* the operation three ways; each route is a self-contained justification of $T = \gamma T_0$.

2. **Apply the Lorentz transformation to map events between frames** (operation 1). Part 3 transforms the two tick-events from the clock's frame to the lab via $\Delta t = \gamma(\Delta t' + v\Delta x')$.

3. **Compute an invariant in the most convenient frame** (operation 8). Part 3's interval route evaluates $\Delta s^2 = T_0^2$ in the clock frame and $\Delta t^2 - \Delta x^2$ in the lab, equating them.

4. **Read off geometry from a spacetime diagram** (operation 9). The light clock's slant path is a geometric (diagram) argument; the right triangle with legs $h$ and $vT/2$ is the picture.

---

# Hints

> [!note]- Hint 1
> Rest frame: the pulse goes straight up and down, distance $2h$, at speed $c = 1$, so $T_0 = 2h$. Moving frame: in one half-tick (time $T/2$) the clock drifts sideways by $v\,T/2$, so the pulse travels the hypotenuse of a right triangle with vertical leg $h$ and horizontal leg $vT/2$. That hypotenuse equals $c\cdot(T/2) = T/2$. Set up the Pythagoras equation and solve for $T$.

> [!note]- Hint 2
> Suppose transverse lengths *did* contract, by some factor $f(v)$. Take two identical rods held perpendicular to the relative motion, one in each frame. By the symmetry of relativity, each frame must see the other's rod shrink by the same $f(v)$. But the tips' relative position (whose rod is longer) is a single physical fact both must agree on — so $f(v) < 1$ and $f(v) > 1$ are both contradictory, forcing $f(v) = 1$.

> [!note]- Hint 3
> The clock is at one place in $S'$: $\Delta x' = 0$. You know primed data and want the lab time, so use the *inverse* transformation $\Delta t = \gamma(\Delta t' + v\Delta x')$. With $\Delta x' = 0$ it collapses to $\Delta t = \gamma\Delta t' = \gamma T_0$. For the interval route: $\Delta s^2 = \Delta t'^2 - \Delta x'^2 = T_0^2$ in $S'$, and $= \Delta t^2 - \Delta x^2$ in $S$; equate and solve.

> [!note]- Hint 4
> The light clock shows the *mechanism* (longer path, same speed); the interval route shows *that* the dilation holds and that the proper time is minimal (since $\Delta t^2 = T_0^2 + \Delta x^2 \ge T_0^2$). All three give $\gamma = (1-v^2)^{-1/2}$.

---

# Solution

Three routes converge on the same factor. The light clock makes the mechanism visible — a slanted path of fixed speed takes longer. The Lorentz route is a one-line substitution. The interval route proves the factor frame-independently and shows the proper time is the shortest.

**Step 1: The light clock gives $T = \gamma T_0$.**

> [!note]- Derivation
> *Rest frame.* The pulse travels straight up to the far mirror and back, a total distance $2h$, at speed $c = 1$. One tick is
> $$T_0 = 2h.$$
> *Moving frame $S$ (clock moving at $v$ along $x$).* By Step 2 the mirror separation is still $h$. Let $T$ be the full-tick time in $S$; each one-way leg takes $T/2$, during which the clock drifts sideways by $v\,(T/2)$. The pulse therefore travels the hypotenuse of a right triangle with vertical leg $h$ and horizontal leg $vT/2$, a distance $\sqrt{h^2 + (vT/2)^2}$. Since the pulse moves at $c = 1$, this distance equals $T/2$:
> $$\frac{T}{2} = \sqrt{h^2 + \left(\frac{vT}{2}\right)^2}.$$
> Square: $T^2/4 = h^2 + v^2T^2/4$, so $(T^2/4)(1 - v^2) = h^2$, giving
> $$T = \frac{2h}{\sqrt{1 - v^2}} = \gamma\,(2h) = \gamma T_0.$$
> The moving clock's tick is longer by $\gamma$. The mechanism is transparent: the pulse covers a longer (slanted) path at the *same* speed $c$, so the tick takes proportionally longer — and the proportion is the hypotenuse-to-height ratio, which is exactly $\gamma$.

**Step 2: Transverse lengths are unchanged.**

> [!note]- Derivation
> Suppose lengths perpendicular to the motion transformed by a factor $f(v)$ depending only on the relative speed. Let frames $S$ and $S'$ move relative to each other along $x$, each carrying a rod of rest length $\ell$ held along $y$ (transverse). By the principle of relativity neither frame is preferred, so $S$ measures $S'$'s rod as $f(v)\ell$ and, by the identical rule, $S'$ measures $S$'s rod as $f(v)\ell$. Bring the two rods to coincide along $y$ as the origins pass — whether one tip falls inside the other is a single, frame-independent physical fact (a transverse coincidence is local and unambiguous). If $f(v) < 1$, $S$ says $S'$'s tip is inside its own rod while $S'$ says $S$'s tip is inside *its* rod — contradictory, since only one can be inside. Likewise $f(v) > 1$ is contradictory. Hence $f(v) = 1$: **transverse lengths are invariant**, and in particular the light clock's height $h$ is the same in both frames, validating the right triangle in Step 1.

**Step 3: The Lorentz and interval routes.**

> [!note]- Derivation
> *Lorentz route.* The clock sits at one place in its rest frame $S'$, so two successive ticks have $\Delta x' = 0$ and $\Delta t' = T_0$. Applying the inverse [[Def - The Lorentz Transformation|Lorentz transformation]] (rest frame $\to$ lab, sign $+v$) to the differences,
> $$\Delta t = \gamma(\Delta t' + v\,\Delta x') = \gamma(T_0 + 0) = \gamma T_0.$$
> So $T = \gamma T_0$ — the same factor, in one line, with the vanishing $\Delta x'$ doing all the work.
>
> *Interval route.* The [[Def - The Spacetime Interval|interval]] between the two ticks is frame-independent ([[Thm - Invariance of the Spacetime Interval]]). In the clock frame, $\Delta s^2 = \Delta t'^2 - \Delta x'^2 = T_0^2 - 0 = T_0^2$. In the lab frame, $\Delta s^2 = \Delta t^2 - \Delta x^2$, where the clock has moved $\Delta x = v\,\Delta t$ between ticks. Equate:
> $$\Delta t^2 - \Delta x^2 = T_0^2 \ \Longrightarrow\ \Delta t^2 - v^2\Delta t^2 = T_0^2 \ \Longrightarrow\ \Delta t^2(1 - v^2) = T_0^2 \ \Longrightarrow\ \Delta t = \frac{T_0}{\sqrt{1 - v^2}} = \gamma T_0.$$
> The same $\gamma$. Moreover, *without* assuming the clock's motion, $\Delta t^2 = T_0^2 + \Delta x^2 \ge T_0^2$ for any lab-frame spatial separation $\Delta x$, with equality iff $\Delta x = 0$: the **proper time $T_0$ is the shortest coordinate time** any frame assigns, attained only in the rest frame. This invariant statement is the bonus the interval route gives that the others do not.

**Step 4: Agreement and what each route shows.**

> [!note]- Derivation
> All three routes give the identical factor:
> $$T = \gamma T_0, \qquad \gamma = (1 - v^2)^{-1/2} \quad\left(\text{with } c: \ \gamma = (1 - v^2/c^2)^{-1/2}\right).$$
> Their epistemic roles differ. The **light clock** shows *why* the dilation occurs — a concrete mechanism (a longer slant path traversed at the fixed speed $c$) that makes the effect intuitive and, because it uses no property of the clock beyond bouncing light, hints that the effect is universal. The **Lorentz route** is the fastest computation but treats the transformation as a black box. The **interval route** shows *that* the dilation holds in a frame-independent way and, crucially, that the proper time is the *minimum* coordinate time — the invariant content that survives without reference to any particular clock and that generalises (via $\tau = \int\sqrt{ds^2}$) to curved spacetime. Together: the light clock is the picture, the Lorentz line is the calculation, the interval is the invariant truth.

> [!note]- Complete formal solution
> *Light clock.* Rest-frame tick $T_0 = 2h$ (pulse travels $2h$ at $c=1$). In a frame where the clock moves at $v$, one one-way leg has the pulse traverse the hypotenuse $\sqrt{h^2 + (vT/2)^2} = T/2$, where $h$ is unchanged (transverse invariance). Solving, $T = 2h/\sqrt{1-v^2} = \gamma T_0$. *Transverse invariance:* a factor $f(v) \ne 1$ on transverse lengths makes each frame see the other's perpendicular rod tip both inside and outside its own — contradiction — so $f(v) = 1$. *Lorentz route:* the clock has $\Delta x' = 0$, $\Delta t' = T_0$, so $\Delta t = \gamma(\Delta t' + v\Delta x') = \gamma T_0$. *Interval route:* $\Delta s^2 = T_0^2$ (clock frame) $= \Delta t^2 - \Delta x^2 = \Delta t^2(1-v^2)$ (lab), giving $\Delta t = \gamma T_0$; and $\Delta t^2 = T_0^2 + \Delta x^2 \ge T_0^2$ shows the proper time is minimal. All yield $\gamma = (1-v^2)^{-1/2}$; the light clock gives the mechanism, the interval gives the invariance and minimality. $\blacksquare$

---

# Key Takeaways

**The light clock makes time dilation mechanism-independent and therefore universal.** The single most valuable thing about the light-clock derivation is what it *omits*: it uses no property of the clock except that light bounces between mirrors at speed $c$. The slanted pulse covers more distance at the same fixed speed, so the tick lengthens — and since this argument never touches the clock's internal workings, the conclusion cannot depend on them, which is precisely why time dilation applies identically to pendulums, atoms, and beating hearts. Whenever you want to argue that a relativistic effect is a property of *spacetime* rather than of a particular apparatus, the strategy is to derive it from a device whose only physics is the constancy of $c$; the light clock is the canonical example, and its mechanism-freedom is the rigorous backing for the slogan "it is time itself that slows" ([[Ex - Time dilation and the cosmic-ray muon]]).

**Setting $\Delta x' = 0$ is the move that names the proper-time frame.** Across all of relativistic kinematics, the cleanest computations come from spotting the frame in which a pair of events is *co-located* — where $\Delta x' = 0$ — because that single condition collapses the Lorentz transformation to one factor and identifies the proper time. In this exercise it turns the transformation $\Delta t = \gamma(\Delta t' + v\Delta x')$ into the bare $\Delta t = \gamma T_0$. The transferable diagnostic: faced with two events, ask whether some frame puts them at the same place; if so, that frame holds a single clock present at both, reads the proper time, and every other frame's time is $\gamma$ times it. This is the same recognition that makes the muon problem tractable and that underlies the interval route's "$\Delta s^2 = T_0^2$ in the rest frame" — the spatial part of the interval is killed exactly when $\Delta x' = 0$.

**Triangulating a result by independent routes is the deepest correctness check, and each route teaches something different.** Deriving $\gamma$ three ways is not redundancy; it is the practice that builds trust and reveals structure. The light clock supplies intuition (the picture of the slant path), the Lorentz substitution supplies speed (a one-liner), and the interval supplies invariance plus the bonus theorem that proper time is the *shortest* coordinate time. That last is the seed of everything geometric in the later chapters — the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]], the twin paradox, the geodesic principle — and it emerges only from the invariant route, which is why one should always ask what the *invariant* formulation of an effect is, not merely how to compute it in coordinates. The general lesson for problem-solving: when a result can be reached geometrically and algebraically, do both, because the geometric route shows *why* and the algebraic route shows *that*, and the place they are hardest to reconcile is usually where the real content hides.
