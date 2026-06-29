---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Classification of Four-Vectors"
  - "Def - Minkowski Space and the Metric"
  - "Thm - Invariance of the Spacetime Interval"
tags: [physics, special-relativity]
---

# Problem Statement

Working with $c = 1$ and $\eta = \mathrm{diag}(1,-1,-1,-1)$:

1. Classify each of the following four-vectors as timelike, spacelike, or null, and (for the causal ones) as future- or past-directed:
$$
A = (3,1,1,1), \quad B = (1,1,1,1), \quad C = (1,2,2,0), \quad D = (-2,0,1,0), \quad F = (0,1,0,0).
$$
2. For the spacelike vector $C$, exhibit an explicit Lorentz boost under which the sign of its time component $C^0$ changes, confirming that spacelike vectors have no invariant time-orientation. For the timelike $A$, argue that no boost can change the sign of $A^0$.
3. Show that the classification is preserved under every Lorentz transformation by appealing to the invariance of the scalar square, and identify which quantity an observer would compute to decide, frame-independently, whether two events $P, Q$ can be causally connected.

**Recall:**

![[Def - Classification of Four-Vectors#The Definition]]

The scalar square is computed by the [[Def - Minkowski Space and the Metric|Minkowski matrix]], $X\cdot X = (X^0)^2 - (X^1)^2 - (X^2)^2 - (X^3)^2$, and is [[Thm - Invariance of the Spacetime Interval|Lorentz invariant]]. A boost along $x$ acts as $X'^0 = \gamma(X^0 - vX^1)$, $X'^1 = \gamma(X^1 - vX^0)$, with $\gamma = (1-v^2)^{-1/2}$.

---

# Convergent Strategy

**Problem class.** A *classification* problem, the most basic and most frequent in the chapter: compute one scalar square per vector and read off the type. The [[Special Relativity III — Minkowski Spacetime and the Metric#Problem-Solving Strategy|topic strategy]] notes this is settled entirely by the sign of $X\cdot X$ (plus the sign of $X^0$ for causal vectors).

**Assumption pattern.** Components are given explicitly, so there is nothing to set up — the assumption is simply a list of four-vectors. The only subtlety is part 2, which asks about the *frame-dependence* of the time-sign, recognisable as a question about whether a vector is inside or outside the light cone.

**Theorem routing.** Part 1 is direct application of the Minkowski matrix and the [[Def - Classification of Four-Vectors|classification]]. Part 2 uses the boost formulas to exhibit a sign flip for the spacelike $C$ and the [[Thm - Invariance of the Spacetime Interval|geometry of the cone]] to forbid it for the timelike $A$. Part 3 routes through invariance of the scalar square to frame-independence of the type.

**Key decision point.** The crux of part 2 is that the time-sign of a *spacelike* vector can flip because such a vector lies *outside* the light cone, where a sufficiently fast boost tips $X^0$ negative; the time-sign of a *timelike* vector cannot flip because it lies *inside* the cone, which a boost cannot cross. The natural error is to assume all components flip-able alike; the light-cone geometry is what distinguishes them.

---

# Legal Operations Used

1. **Operation 2 (compute the scalar product by the Minkowski matrix):** one scalar square per vector in part 1.

2. **Operation 3 (classify by the sign of the scalar square):** the core of part 1, refined by the sign of $X^0$ for causal vectors.

3. **Operation 1 / the Lorentz boost (map components between frames):** part 2 applies the boost formulas to track $C^0$ and $A^0$.

4. **Operation 5 (evaluate an invariant in a convenient frame):** part 3 — the scalar square is the invariant that fixes the type for all observers.

---

# Hints

> [!note]- Hint 1
> Compute $X\cdot X = (X^0)^2 - |\mathbf{X}|^2$ for each. For example $A\cdot A = 9 - (1+1+1) = 6 > 0$: timelike. Do the same for $B, C, D, F$. Then for the timelike and null ones, the sign of $X^0$ gives future ($>0$) or past ($<0$).

> [!note]- Hint 2
> For $C = (1,2,2,0)$: $C\cdot C = 1 - 8 = -7 < 0$, spacelike. Boost along $x$: $C'^0 = \gamma(1 - 2v)$. This is negative once $v > 1/2$. So a boost with $v > 1/2$ flips $C^0$ negative — spacelike vectors have no invariant time-sign.

> [!note]- Hint 3
> For $A = (3,1,1,1)$: $A'^0 = \gamma(3 - v\cdot 1) = \gamma(3 - v)$, and since $|v| < 1$ this is always positive. More generally, a timelike vector has $|X^0| > |\mathbf{X}|$, so $X^0 - vX^1 \geq |X^0| - |v||\mathbf{X}| > 0$ for $|v| < 1$: the time-sign of a timelike vector is boost-invariant.

> [!note]- Hint 4
> For part 3: $X\cdot X$ is the same in all frames, so its sign — hence the classification — is frame-independent. To decide if $P, Q$ are causally connectible, compute the [[Def - The Spacetime Interval|interval]] $\Delta s^2 = \eta_{\mu\nu}\Delta x^\mu\Delta x^\nu$ of their separation: timelike or null ($\Delta s^2 \geq 0$) means connectible, spacelike ($\Delta s^2 < 0$) means not.

---

# Solution

Each classification is one scalar square; the time-orientation is one more sign; and frame-independence is the invariance of the scalar square. Step 1 classifies all five; Step 2 exhibits the spacelike sign-flip and the timelike rigidity; Step 3 ties the classification to the invariant interval.

**Step 1: the five classifications.**

> [!note]- Derivation
> Using $X\cdot X = (X^0)^2 - |\mathbf{X}|^2$:
> - $A = (3,1,1,1)$: $A\cdot A = 9 - 3 = 6 > 0$, **timelike**; $A^0 = 3 > 0$, **future-directed**.
> - $B = (1,1,1,1)$: $B\cdot B = 1 - 3 = -2 < 0$, **spacelike** (no time-orientation).
> - $C = (1,2,2,0)$: $C\cdot C = 1 - 8 = -7 < 0$, **spacelike**.
> - $D = (-2,0,1,0)$: $D\cdot D = 4 - 1 = 3 > 0$, **timelike**; $D^0 = -2 < 0$, **past-directed**.
> - $F = (0,1,0,0)$: $F\cdot F = 0 - 1 = -1 < 0$, **spacelike**.
>
> (Note $B$ has equal time and... no: $B\cdot B = 1 - 3 = -2$, spacelike, not null — a vector is null only when $(X^0)^2 = |\mathbf{X}|^2$ exactly, e.g. $(\sqrt3,1,1,1)$.)

**Step 2: the spacelike sign-flip and the timelike rigidity.**

> [!note]- Derivation
> *Spacelike $C = (1,2,2,0)$.* Boost along $x$ with velocity $v$:
> $$C'^0 = \gamma(C^0 - vC^1) = \gamma(1 - 2v).$$
> For $v > 1/2$ (allowed, since $v < 1$), $1 - 2v < 0$, so $C'^0 < 0$: the time component has flipped sign. For instance $v = 0.8$ gives $C'^0 = \gamma(1 - 1.6) = -0.6\gamma < 0$. The scalar square is unchanged: $C'\cdot C' = -7$ still. So a *spacelike* vector's time-orientation is frame-dependent, which is why the [[Def - Classification of Four-Vectors|classification]] assigns no future/past label to spacelike vectors.
>
> *Timelike $A = (3,1,1,1)$.* Boost along $x$:
> $$A'^0 = \gamma(3 - v\cdot 1) = \gamma(3 - v) > 0 \quad\text{for all } |v| < 1.$$
> More generally, a timelike vector satisfies $|X^0| > |\mathbf{X}| \geq |X^1|$, so for any boost direction $X^0 - vX^1 \geq |X^0| - |v|\,|X^1| > |X^1| - |X^1| = 0$ when $|v| < 1$ and $X^0 > 0$. Hence no boost flips the time-sign of a timelike vector: it stays future-directed. Geometrically, $A$ is *inside* the light cone, and a boost scissors the axes towards the cone but never across it; $C$ is *outside* the cone, where the boosted time axis can swing past it.

**Step 3: invariance gives frame-independent classification and the causal criterion.**

> [!note]- Derivation
> Since $X\cdot X$ is [[Thm - Invariance of the Spacetime Interval|Lorentz invariant]], its sign — and therefore the classification timelike/spacelike/null — is the same in every frame: all observers agree on a vector's causal type. For causal vectors the sign of $X^0$ is additionally invariant under orthochronous transformations, so all observers agree on future versus past as well.
>
> To decide whether two events $P, Q$ can be causally connected, an observer computes the [[Def - The Spacetime Interval|interval]] of their separation,
> $$\Delta s^2 = \eta_{\mu\nu}\Delta x^\mu\Delta x^\nu, \qquad \Delta x^\mu = x_Q^\mu - x_P^\mu.$$
> If $\Delta s^2 > 0$ (timelike) or $\Delta s^2 = 0$ (null), the events lie on or inside each other's light cones and a sub-light (or light) signal can join them — causally connectible. If $\Delta s^2 < 0$ (spacelike), no signal can join them. Because $\Delta s^2$ is invariant, this verdict is the same for every observer, even though they disagree on $\Delta t$ and $|\Delta\mathbf{x}|$ separately.

> [!note]- Complete formal solution
> $A\cdot A = 9 - 3 = 6 > 0$ (timelike, future); $B\cdot B = 1 - 3 = -2 < 0$ (spacelike); $C\cdot C = 1 - 8 = -7 < 0$ (spacelike); $D\cdot D = 4 - 1 = 3 > 0$ (timelike, past, since $D^0 = -2$); $F\cdot F = -1 < 0$ (spacelike). For $C$, a boost $C'^0 = \gamma(1 - 2v)$ is negative for $v > 1/2$, flipping the time-sign — spacelike vectors have no invariant orientation, as they lie outside the light cone. For $A$, $A'^0 = \gamma(3 - v) > 0$ for all $|v| < 1$, and generally $|X^0| > |\mathbf{X}|$ keeps $X^0 - vX^1 > 0$, so a timelike vector's time-sign is boost-invariant (it lies inside the cone). The scalar square $X\cdot X$ is invariant, so the classification is frame-independent; two events are causally connectible iff their separation has $\Delta s^2 = \eta_{\mu\nu}\Delta x^\mu\Delta x^\nu \geq 0$. $\blacksquare$

---

# Key Takeaways

**One scalar square decides everything causal, and its sign is frame-independent.** The reflex this exercise drills is the cheapest and most-used in relativity: to classify any four-vector or separation, compute $X\cdot X = (X^0)^2 - |\mathbf{X}|^2$ and read the sign — positive timelike, negative spacelike, zero null. Because the scalar square is a [[Thm - Invariance of the Spacetime Interval|Lorentz invariant]], the answer is the same for every observer, so you may compute in whatever frame is handed to you and trust the result universally. The trigger is any causal question whatsoever — can $P$ influence $Q$, is a worldline physical, is a particle massive or massless — and the answer is always the sign of one scalar square. This single computation is the workhorse on which all of relativistic kinematics rests, and it costs almost nothing.

**The time-sign is invariant for timelike/null vectors but not for spacelike ones, and the light cone is why.** The deeper lesson is the asymmetry between the causal and spacelike cases. A timelike vector lies strictly inside the light cone, where $|X^0| > |\mathbf{X}|$; a boost tilts the time axis towards the null direction but cannot reach it, so it cannot flip $X^0$ — future stays future. A spacelike vector lies outside the cone, where $|X^0| < |\mathbf{X}|$, and a fast enough boost swings the time axis past it, flipping $X^0$ negative. This is the precise origin of the *relativity of simultaneity* for spacelike-separated events: their time-ordering is frame-dependent exactly because their separation's time-sign is not invariant. The transferable diagnostic: if you ever need a quantity's sign to be observer-independent, it must come from a *causal* (inside-or-on-cone) vector, since only there is the time-sign protected; spacelike directions offer no such protection.

**Causal connectibility is the sign of the interval, and this is the operational meaning of the whole classification.** The payoff of the classification is the causal criterion: two events can be causally connected if and only if their separation is timelike or null, $\Delta s^2 \geq 0$, and this is frame-independent because the interval is invariant. This converts a question about physics — can a signal travel from $P$ to $Q$? — into a single arithmetic sign, computable in any frame. The same logic, applied to a worldline's tangent at each point, gives the criterion for a trajectory to be physically allowed: its tangent must be everywhere causal. Whenever a problem asks about influence, signalling, or the order of events, the move is to compute the interval and read its sign; the classification of four-vectors is, at bottom, the statement that this sign is what carries the causal content of spacetime.
