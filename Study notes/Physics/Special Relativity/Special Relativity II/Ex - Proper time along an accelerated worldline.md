---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Proper Time"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Thm - The Reversed Triangle Inequality"
tags: [physics, special-relativity]
---

# Problem Statement

A particle travels between two events $O$ and $P$ on the time axis of an inertial frame $S$, separated by coordinate time $T$ (so $O = (0,\mathbf{0})$ and $P = (T,\mathbf{0})$ in $S$). One particle, the "stay-at-home", remains at the spatial origin and moves inertially from $O$ to $P$. A second particle, the "traveller", leaves $O$, moves out along the $x$-axis at constant speed $u$ for coordinate time $T/2$, instantaneously reverses, and returns at constant speed $u$, arriving at $P$.

**(a)** Compute the proper time elapsed for each particle between $O$ and $P$, and show the traveller ages less.

**(b)** Now let the traveller follow a *general* worldline $\mathbf{x}(t)$ from $O$ to $P$ with instantaneous speed $u(t)$. Write the proper time as an integral and show that the inertial stay-at-home worldline maximises proper time among all worldlines joining $O$ to $P$.

**(c)** Resolve the apparent paradox: relativity treats all inertial observers symmetrically, so why is the situation between the two particles *not* symmetric?

**Recall:**

![[Def - Proper Time#The Definition]]

The Lorentz factor is $\gamma(u) = (1-u^2/c^2)^{-1/2} \geq 1$, with equality only at $u=0$. The [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] states that for timelike worldlines the straight (inertial) one has the *greatest* proper time.

---

# Convergent Strategy

**Problem class.** This is a *proper-time computation*: evaluate the invariant clock-reading $\tau = \int dt/\gamma$ along a worldline. Part (b) upgrades it to a variational comparison across worldlines.

**Assumption pattern.** Each worldline is specified by its speed profile $u(t)$. Proper time depends *only* on this profile through the integrand $1/\gamma(u) = \sqrt{1-u^2/c^2}$, so the whole problem reduces to integrating a function of $u(t)$.

**Theorem routing.** Part (a) is a direct application of [[Def - Proper Time|the definition of proper time]] on two piecewise-constant-speed worldlines. Part (b) routes through the elementary inequality $\sqrt{1-u^2/c^2} \leq 1$ — the integrand is pointwise maximised by $u = 0$ — which is the differential heart of the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]].

**Key decision point.** The non-obvious move in (b) is recognising that *no calculus of variations is needed*: the integrand $\sqrt{1-u^2/c^2}$ is bounded above by $1$ at every instant, so the integral is bounded above by $T$, achieved only when $u\equiv 0$. The paradox in (c) is resolved by noticing that proper time is a property of the *worldline*, not of an observer, and the two worldlines are geometrically different — one is straight, one is bent.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Special Relativity II — Relativistic Kinematics and Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Use a Lorentz invariant** — proper time is invariant, so it may be computed in the single frame $S$ and the answer is valid for all observers.
2. **Differentiate (here, integrate) with respect to proper time, not coordinate time** — the relation $d\tau = dt/\gamma$ converts the worldline data $u(t)$ into elapsed proper time.

---

# Hints

> [!note]- Hint 1
> Proper time is $\tau = \int dt/\gamma$. For a worldline made of constant-speed segments, $\gamma$ is constant on each segment, so the integral is just (segment coordinate-time) divided by (segment $\gamma$). Do this for each particle.

> [!note]- Hint 2
> For part (b), you cannot assume the worldline is made of straight pieces. Write $\tau = \int_0^T \sqrt{1-u(t)^2/c^2}\,dt$. The integrand is a function of $u(t)$ alone. What is the largest value $\sqrt{1-u^2/c^2}$ can take, and for which $u$?

> [!note]- Hint 3
> Since $\sqrt{1-u^2/c^2} \leq 1$ pointwise, with equality only at $u = 0$, the integral satisfies $\tau \leq \int_0^T 1\,dt = T$, with equality only if $u(t) = 0$ for all $t$ — the stay-at-home worldline.

> [!note]- Hint 4
> For (c): ask which particle's worldline is *straight* in spacetime and which is *bent*. The bend (the turnaround) is an acceleration — a physical, frame-independent event the traveller feels and the stay-at-home does not. The two are not interchangeable.

---

# Solution

Proper time depends only on the speed profile through $\tau = \int\sqrt{1-u^2/c^2}\,dt$, and since the integrand never exceeds $1$, the worldline that stays at rest accumulates the most proper time. The traveller, moving at nonzero speed, integrates a strictly smaller integrand and ages less.

**Step 1: Proper time of the stay-at-home.**

The stay-at-home has $u = 0$ throughout, so $\gamma = 1$ and $\tau_{\text{stay}} = T$.

> [!note]- Derivation
> The stay-at-home worldline is $\mathbf{x}(t) = \mathbf{0}$ for $0\le t\le T$. Its speed is $u = 0$ everywhere, so $\gamma(0) = 1$, and
> $$\tau_{\text{stay}} = \int_0^T \frac{dt}{\gamma} = \int_0^T \sqrt{1-0}\;dt = T.$$
> For an inertial particle at rest, proper time coincides with coordinate time, exactly as [[Def - Proper Time|the definition]] requires.

**Step 2: Proper time of the traveller.**

The traveller moves at speed $u$ for the whole journey (out for $T/2$, back for $T/2$), so $\tau_{\text{trav}} = T/\gamma(u) = T\sqrt{1-u^2/c^2} < T$.

> [!note]- Derivation
> The traveller's worldline has two segments. On the outbound segment, coordinate time runs from $0$ to $T/2$ at constant speed $u$, so the proper time accumulated is $(T/2)/\gamma(u)$. On the inbound segment, coordinate time runs from $T/2$ to $T$ again at constant speed $u$ (speed, not velocity — the magnitude is the same on the way back), contributing another $(T/2)/\gamma(u)$. The instantaneous turnaround occupies zero coordinate time and contributes nothing. Hence
> $$\tau_{\text{trav}} = \frac{T/2}{\gamma(u)} + \frac{T/2}{\gamma(u)} = \frac{T}{\gamma(u)} = T\sqrt{1 - \frac{u^2}{c^2}}.$$
> Since $u > 0$ gives $\gamma(u) > 1$, we have $\tau_{\text{trav}} = T/\gamma(u) < T = \tau_{\text{stay}}$. The traveller ages less. (Note the outbound and inbound legs have equal proper time even though one is in the $+x$ and one in the $-x$ direction, because $\gamma$ depends on speed $u$, not on velocity.)

**Step 3: The inertial worldline maximises proper time (part b).**

For *any* worldline from $O$ to $P$ with speed profile $u(t)$, the proper time is $\tau = \int_0^T\sqrt{1-u(t)^2/c^2}\,dt \leq T$, with equality only for $u\equiv 0$.

> [!note]- Derivation
> Let the traveller follow an arbitrary timelike worldline $\mathbf{x}(t)$ from $O$ at $t=0$ to $P$ at $t=T$, with instantaneous speed $u(t) = |d\mathbf{x}/dt|$. By [[Def - Proper Time|the definition of proper time]],
> $$\tau = \int_0^T \frac{dt}{\gamma\big(u(t)\big)} = \int_0^T \sqrt{1 - \frac{u(t)^2}{c^2}}\;dt.$$
> The integrand is a function of $u(t)$ alone. For every real speed $0\le u < c$,
> $$\sqrt{1 - u^2/c^2} \;\le\; 1,$$
> with equality if and only if $u = 0$. This is an inequality between the *integrands* at each instant $t$, so it integrates:
> $$\tau = \int_0^T \sqrt{1 - u(t)^2/c^2}\;dt \;\le\; \int_0^T 1\;dt \;=\; T = \tau_{\text{stay}}.$$
> Equality holds if and only if the integrands agree almost everywhere, i.e. $u(t) = 0$ for all $t$ — which is precisely the stay-at-home worldline. So among all worldlines joining the two events, **the inertial one has the greatest proper time**, and every other worldline has strictly less. This is the differential statement of the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]]: the "straight line" in Minkowski space is the *longest* timelike path, opposite to the Euclidean case. No variational machinery is needed — the pointwise bound on the integrand does everything.

**Step 4: Resolving the paradox (part c).**

> [!note]- Derivation
> The apparent paradox runs: "relativity says all inertial observers are equivalent, so each should see the other's clock run slow, and there is no reason for one to age more — yet they disagree." The resolution is that the premise is false for *this* problem. The stay-at-home occupies a single inertial frame from $O$ to $P$. The traveller does **not**: the turnaround is an acceleration, and during it the traveller is not in any one inertial frame. The two worldlines are therefore not related by a symmetry — one is straight in spacetime, the other has a corner.
>
> Proper time is a property of a *worldline*, computed by the integral in [[Def - Proper Time|the definition]], exactly as Euclidean arc length is a property of a path. Two different paths between the same endpoints can have different lengths; there is no paradox in that. The traveller's worldline is longer in coordinate time but, because of the indefinite Minkowski metric, *shorter* in proper time. The acceleration at the turnaround is a physical, frame-independent event — the traveller feels it as a jolt, the stay-at-home feels nothing — and it is the objective marker that breaks the symmetry. Symmetric treatment of inertial observers applies only to genuinely inertial worldlines; the traveller's is not one.

> [!note]- Complete formal solution
> **(a)** The stay-at-home worldline has $u \equiv 0$, $\gamma \equiv 1$, so $\tau_{\text{stay}} = \int_0^T dt = T$. The traveller moves at constant speed $u$ for the whole trip, in two equal coordinate-time legs of duration $T/2$, so
> $$\tau_{\text{trav}} = 2\cdot\frac{T/2}{\gamma(u)} = \frac{T}{\gamma(u)} = T\sqrt{1-u^2/c^2} < T.$$
> The traveller ages less by the factor $1/\gamma(u)$.
>
> **(b)** For an arbitrary timelike worldline with speed $u(t)$,
> $$\tau = \int_0^T\sqrt{1-u(t)^2/c^2}\,dt \le \int_0^T 1\,dt = T,$$
> using $\sqrt{1-u^2/c^2}\le 1$ pointwise, with equality iff $u\equiv 0$. Hence the inertial stay-at-home worldline uniquely maximises proper time among all worldlines from $O$ to $P$.
>
> **(c)** The two worldlines are not symmetric: the stay-at-home is inertial throughout, the traveller accelerates at the turnaround. Proper time is a worldline invariant, not an observer-relative quantity; different worldlines between the same events have different proper times, and the acceleration is the physical, frame-independent feature distinguishing them. $\blacksquare$

---

# Key Takeaways

**Proper time is the integral $\int dt/\gamma$, and computing it is just integrating a function of speed.** The single most important practical fact about proper time is that it depends on the worldline *only through the speed profile* $u(t)$: the direction of motion never enters, since $\gamma$ depends on $u = |\mathbf{u}|$. So any "how much does the traveller age" problem — the twin paradox, an orbiting satellite's clock, a particle in an accelerator — reduces to writing down $u(t)$ and integrating $\sqrt{1-u^2/c^2}$. For piecewise-constant speeds the integral is a finite sum; for a smooth profile it is an honest integral. The trigger phrase is "time experienced by" or "time elapsed on the clock of" — whenever you see it, reach for $\tau = \int dt/\gamma$, not for any frame-hopping argument.

**A pointwise bound on the integrand beats the calculus of variations.** Part (b) looks like an optimisation problem — maximise a functional over all worldlines — and one's instinct is to set up an Euler–Lagrange equation. But the integrand $\sqrt{1-u^2/c^2}$ is bounded above by $1$ *at every instant*, independently of what the rest of the worldline does, so the integral is bounded above by $T$ with the bound saturated only by $u\equiv 0$. The optimum is found by a one-line pointwise inequality. This is a recurring pattern: when a functional's integrand has a pointwise extremum at a value achievable everywhere simultaneously, the constrained optimum is that value, and no variational calculus is required. The reversed triangle inequality of Minkowski geometry is exactly this phenomenon — the straight worldline wins because its integrand is pointwise maximal.

**Proper time is a worldline invariant, which is what dissolves the twin "paradox".** The paradox survives only as long as one thinks of time dilation as a relation *between observers* — "each sees the other slow". Proper time reframes it: the elapsed time is an intrinsic property of a *curve in spacetime*, computed by an integral that knows nothing about observers. Two curves between the same two events generically have different proper times, just as two roads between two cities have different lengths, and that is not paradoxical. The asymmetry between the twins is the asymmetry between a straight worldline and a bent one; the bend is an acceleration, a frame-independent physical event. The general lesson for the whole topic: when a "paradox" arises from comparing observers, re-express the quantity in question as a worldline invariant or a Lorentz scalar, and the paradox evaporates because invariants do not depend on who is looking.
