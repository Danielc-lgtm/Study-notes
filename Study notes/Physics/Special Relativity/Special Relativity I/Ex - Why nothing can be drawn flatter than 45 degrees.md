---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Spacetime Diagram"
  - "Def - The Lorentz Transformation"
  - "Def - Inertial Frame and the Postulates of Special Relativity"
tags: [physics, special-relativity]
---

# Problem Statement

On a [[Def - Spacetime Diagram|spacetime diagram]] ($ct$ vertical, $x$ horizontal, $c = 1$), the worldline of a massive particle is always *steeper* than the $45^\circ$ light line. This exercise establishes why, and draws out the causal consequences.

1. **The slope of a worldline.** Show that a particle of speed $|u| < c$ has worldline slope $|{\Delta(ct)}/{\Delta x}| = c/|u| > 1$, so massive worldlines are steeper than $45^\circ$, light is exactly $45^\circ$, and a slope shallower than $45^\circ$ would mean $|u| > c$.
2. **A faster-than-light worldline is past-directed in some frame.** Suppose a signal travels at $u > c$ in $S$ (worldline flatter than $45^\circ$). Show, using the [[Def - The Lorentz Transformation|Lorentz transformation]], that there exists an inertial frame $S'$ (with $0 < v < c$) in which the *same* signal travels *backward in time* ($\Delta t' < 0$): the receiver gets it before the sender sends it.
3. **Tachyonic anti-telephone.** Argue that if such superluminal signals existed and the principle of relativity held, one could send a message into one's own past, producing a causal paradox. Conclude that no signal or particle can move faster than light — equivalently, every physical worldline is steeper than $45^\circ$ (timelike or null).
4. **The invariant causal cone.** Show that the partition of the diagram into the future cone, past cone, and spacelike "elsewhere" of an event is the same for all inertial observers, because the $45^\circ$ light cone is frame-independent.

**Recall:**

![[Def - Spacetime Diagram#The Definition]]

The [[Def - The Lorentz Transformation|Lorentz boost]] is $x' = \gamma(x - vt)$, $t' = \gamma(t - vx)$ ($c = 1$). A worldline's *slope* on the diagram is $\Delta(ct)/\Delta x = c/u$ for a particle of speed $u$. The [[Def - Inertial Frame and the Postulates of Special Relativity|principle of relativity]] makes all inertial frames equivalent; *acceleration* (and hence which observer "really" sent a signal) is absolute, but the *time-ordering* of spacelike-separated events is not.

---

# Convergent Strategy

**Problem class.** This is a *causal-structure / impossibility* problem: prove that a kinematic possibility (faster-than-light motion) is forbidden by deriving a contradiction (sending signals into the past). The [[Special Relativity I — Postulates and Lorentz Transformations#Problem-Solving Strategy|topic strategy]] routes causal questions through the sign of the interval and the light-cone geometry.

**Assumption pattern.** The inputs are the worldline-slope relation, the boost, and the principle of relativity. The crucial recognition is that a worldline *flatter* than $45^\circ$ (speed $> c$) is *spacelike*, and spacelike separations have *frame-dependent time order* — so some frame sees the signal going backward in time. Combining that with the relativity principle (so the backward-signalling frame is just as valid) manufactures a causal loop.

**Theorem routing.** Part 1 is the slope relation. Part 2 transforms a spacelike displacement $(\Delta t, \Delta x)$ with $\Delta x > \Delta t$ (i.e. $u = \Delta x/\Delta t > 1$) and finds the $v$ that flips the sign of $\Delta t' = \gamma(\Delta t - v\Delta x)$. Part 3 chains two such signals (forward in one frame, back in another) to close a loop. Part 4 uses the frame-independence of the $45^\circ$ cone (the locus $\Delta s^2 = 0$, preserved by every boost — cf. [[Ex - Light travels at 45 degrees in every frame]]).

**Key decision point.** The decisive realisation is that the sign of $\Delta t' = \gamma(\Delta t - v\Delta x)$ can be made *negative* precisely when $|\Delta x| > |\Delta t|$ (spacelike separation), by choosing $v$ between $\Delta t/\Delta x$ and $1$. For timelike separations ($|\Delta t| > |\Delta x|$) no such $v$ exists, which is *why* timelike order is absolute and spacelike order is not. Recognising that the speed limit is enforced by the *frame-dependence of simultaneity for spacelike separations* — not by any dynamical force — is the whole point.

---

# Legal Operations Used

1. **Operation 9 from the topic page (classify a separation by the sign of its norm / use the light cone).** The argument hinges on the separation being spacelike (flatter than $45^\circ$) versus timelike (steeper).

2. **Operation 1 from the topic page (apply the Lorentz transformation).** Part 2 transforms the displacement to find the frame that reverses its time order.

3. **Operation 8 from the topic page (use the $45^\circ$ light cone structure).** Part 4 invokes the frame-independence of the light cone to establish the invariant causal partition.

---

# Hints

> [!note]- Hint 1
> A particle covering $\Delta x$ in time $\Delta t$ has speed $u = \Delta x/\Delta t$, so worldline slope $\Delta(ct)/\Delta x = c\Delta t/\Delta x = c/u$. For $|u| < c$ this is $> 1$ (steeper than $45^\circ$); $u = c$ gives slope $1$; $|u| > c$ gives slope $< 1$ (flatter).

> [!note]- Hint 2
> For a signal at $u > c$, a displacement is $(\Delta t, \Delta x) = (\Delta t, u\Delta t)$ with $\Delta x = u\Delta t > \Delta t$ (taking $c = 1$, $\Delta t > 0$). Transform: $\Delta t' = \gamma(\Delta t - v\Delta x) = \gamma\Delta t(1 - vu)$. This is negative when $vu > 1$, i.e. $v > 1/u$. Since $u > 1$, $1/u < 1$, so such a $v \in (1/u, 1)$ exists.

> [!note]- Hint 3
> Observer $A$ sends a superluminal signal to $B$ (forward in $A$'s frame). $B$, moving appropriately, sends a superluminal reply that — by part 2 — arrives back at $A$ *before* $A$ sent the original. $A$ receives the reply to a message $A$ has not yet sent: a closed causal loop.

> [!note]- Hint 4
> The light cone is the locus $\Delta s^2 = (ct)^2 - x^2 - y^2 - z^2 = 0$. Every [[Def - The Lorentz Transformation|Lorentz transformation]] preserves $\Delta s^2$, hence preserves the cone $\Delta s^2 = 0$ and the sign of $\Delta s^2$ off it. So all observers agree which events are timelike (inside), null (on), or spacelike (outside) separated.

---

# Solution

A worldline's slope is $c/u$, so sub-light particles are steeper than $45^\circ$ and a flatter line means $u > c$ (Step 1). Such a spacelike signal can be made to run backward in time by a boost (Step 2); chaining two builds a causal loop (Step 3), so superluminal signalling is forbidden and every worldline is timelike or null. The $45^\circ$ cone is frame-independent, giving an invariant causal partition (Step 4).

**Step 1: Worldline slope is $c/|u|$; sub-light means steeper than $45^\circ$.**

> [!note]- Derivation
> A particle moving at constant speed $u$ covers spatial distance $\Delta x = u\,\Delta t$ in coordinate time $\Delta t$. On the diagram (vertical $ct$, horizontal $x$), its worldline has slope
> $$\frac{\Delta(ct)}{\Delta x} = \frac{c\,\Delta t}{u\,\Delta t} = \frac{c}{u}.$$
> - If $|u| < c$ (massive particle): slope $= c/|u| > 1$, *steeper* than the $45^\circ$ light line. A particle at rest ($u = 0$) is vertical (infinite slope).
> - If $|u| = c$ (light): slope $= 1$, exactly $45^\circ$.
> - If $|u| > c$ (hypothetical superluminal): slope $= c/|u| < 1$, *flatter* than $45^\circ$.
>
> So "steeper than $45^\circ$" $\Leftrightarrow$ "sub-light", and a worldline drawn flatter than the light line would necessarily represent faster-than-light motion. The claim to prove is that the flatter case is physically forbidden.

**Step 2: A superluminal signal runs backward in time in some frame.**

> [!note]- Derivation
> Suppose a signal travels at $u > c = 1$ in $S$. Between emission and reception its displacement is
> $$(\Delta t, \Delta x) = (\Delta t,\ u\,\Delta t), \qquad \Delta t > 0,\quad \Delta x = u\,\Delta t > \Delta t$$
> (the separation is *spacelike*: $\Delta x > \Delta t$, so $\Delta s^2 = \Delta t^2 - \Delta x^2 < 0$). Now boost to a frame $S'$ moving at velocity $v$ ($0 < v < 1$) along $x$. The transformed time separation is
> $$\Delta t' = \gamma(\Delta t - v\,\Delta x) = \gamma(\Delta t - v u\,\Delta t) = \gamma\,\Delta t\,(1 - vu).$$
> This is *negative* exactly when $vu > 1$, i.e. when $v > 1/u$. Since $u > 1$, the threshold $1/u < 1$, so there is an allowed boost velocity $v \in (1/u,\ 1)$ — a perfectly legitimate sub-light frame — in which $\Delta t' < 0$. In $S'$ the "reception" event has an *earlier* time coordinate than the "emission" event: the signal arrives before it is sent. (For a *timelike* separation, $|\Delta t| > |\Delta x|$, the factor $1 - vu$ with $|u| < 1$ stays positive for all $|v| < 1$, so no frame reverses the order — timelike order is absolute. The reversal is possible *only* for spacelike separations, which superluminal signals produce.)

**Step 3: Superluminal signalling closes a causal loop — hence is forbidden.**

> [!note]- Derivation
> Build the **tachyonic anti-telephone**. Observer $A$, at rest in $S$, sends a superluminal signal to a distant observer $B$; in $S$ this signal goes forward in time, arriving at $B$ at some event $Q$ later than the emission event $P$. Now let $B$ be equipped to send superluminal replies, and let $B$ move (relative to $A$) with a velocity such that, by the [[Def - Inertial Frame and the Postulates of Special Relativity|principle of relativity]], $B$'s own rest frame $S'$ is one of the frames from Step 2 in which a superluminal signal travels *backward in $A$'s time*. $B$ sends a superluminal reply from $Q$; by Step 2, this reply arrives back near $A$ at an event $R$ with $t_R < t_P$ — *before* $A$ sent the original signal.
>
> $A$ can arrange the reply to instruct "do not send the original signal". Then $A$ receives, before $t_P$, a message telling $A$ not to send the message that triggered the reply — a logical contradiction (the grandfather paradox in signalling form). The contradiction is forced by two ingredients we wish to keep: superluminal signalling (Step 2) and the principle of relativity (which makes $B$'s frame as valid as $A$'s, so the backward-in-time reply is physically realisable). Since the principle of relativity is non-negotiable, superluminal signalling must be impossible. Therefore **no signal or particle can travel faster than light**: every physical worldline has speed $|u| \le c$, hence slope $\ge 1$ — steeper than or equal to $45^\circ$ (timelike or null), never flatter. (This is a *kinematic* prohibition from causality and relativity, independent of any specific force law.)

**Step 4: The causal partition is frame-independent.**

> [!note]- Derivation
> The light cone of an event (take it as the origin) is the set of null-separated events,
> $$\Delta s^2 = (ct)^2 - x^2 - y^2 - z^2 = 0,$$
> the $45^\circ$ cone. It divides spacetime into three regions: the **future cone** ($\Delta s^2 > 0$, $t > 0$ — events reachable from the origin by a sub-light or light signal), the **past cone** ($\Delta s^2 > 0$, $t < 0$ — events that can reach the origin), and the **spacelike elsewhere** ($\Delta s^2 < 0$ — events causally disconnected from the origin).
>
> Every [[Def - The Lorentz Transformation|Lorentz transformation]] preserves $\Delta s^2$ (this is [[Thm - Invariance of the Spacetime Interval|interval invariance]]; concretely, a boost maps the cone to itself, as shown for light lines in [[Ex - Light travels at 45 degrees in every frame|the 45° exercise]]). So all inertial observers agree on the *sign* of $\Delta s^2$ for any pair of events, hence on the three-way classification: which events lie inside the cone (timelike, causally connectible, with a frame-independent time order because no boost reverses timelike order — Step 2), on the cone (null, light-connectible), or outside (spacelike, causally disconnected, with a frame-*dependent* order). The partition into future, past, and elsewhere is therefore an *invariant* of spacetime — the **causal structure** — the same drawing for every inertial observer. This is the geometric foundation of relativistic causality: causal influence propagates only within the cone, and "within the cone" means the same thing to everyone.

> [!note]- Complete formal solution
> A particle of speed $u$ has worldline slope $c/u$: sub-light ($u < c$) gives slope $> 1$ (steeper than $45^\circ$), light gives $1$, superluminal gives $< 1$. For a superluminal signal, the displacement $(\Delta t, u\Delta t)$ is spacelike ($\Delta x > \Delta t$); boosting by $v \in (1/u, 1)$ gives $\Delta t' = \gamma\Delta t(1 - vu) < 0$, so the signal runs backward in time in $S'$ (no such reversal occurs for timelike separations, where $1 - vu > 0$ for all $|v|<1$). By the principle of relativity, $B$'s backward-in-$A$'s-time reply is realisable, so chaining "forward signal $A\to B$" with "backward reply $B\to A$" delivers a message to $A$'s past — a causal contradiction. Hence superluminal signalling is forbidden and every worldline is timelike or null (slope $\ge 1$). Finally, every Lorentz transformation preserves $\Delta s^2$, hence the cone $\Delta s^2 = 0$ and the sign of $\Delta s^2$, so the future/past/elsewhere partition is the same for all observers — an invariant causal structure. $\blacksquare$

> [!warning] Illegal but tempting: concluding spacelike events have a definite order
> Because timelike-separated events have a frame-independent order, it is tempting to assume *all* events do. They do not: for a *spacelike* separation, Step 2 shows different frames disagree about which event is first, and there is no fact of the matter about their order. The error is to import the absolute simultaneity of [[Def - Galilean Spacetime and Its Failure|Galilean spacetime]]. The repair: classify the separation first (sign of $\Delta s^2$). Timelike $\Rightarrow$ order is absolute and causal influence is possible; spacelike $\Rightarrow$ order is frame-dependent and no causal influence is possible. Only the cone-respecting (timelike/null) order is physical.

---

# Key Takeaways

**The speed limit is enforced by causality through the frame-dependence of simultaneity, not by any force — it is kinematic, not dynamical.** The profound content of this exercise is that "nothing exceeds $c$" is not because some interaction pushes back harder and harder (though that is also true dynamically), but because faster-than-light signalling, combined with the principle of relativity, *logically* permits sending messages into one's own past. The mechanism is the sign-flip $\Delta t' = \gamma(\Delta t - v\Delta x) < 0$, available exactly for spacelike separations. The reusable recognition: the prohibition on superluminal motion is a *consistency* requirement of relativity itself, derivable purely from the [[Def - The Lorentz Transformation|Lorentz transformation]] and the equivalence of frames, with no appeal to dynamics. This is why even hypothetical particles and any conceivable propulsion are bound by it — it would take dismantling relativity or causality to evade, not merely a stronger engine.

**Timelike order is absolute, spacelike order is frame-dependent, and the dividing line is the light cone — classify the separation before reasoning about "before" and "after".** The single most transferable diagnostic is to compute the sign of $\Delta s^2$ (equivalently, compare the slope to $45^\circ$) before making any claim about temporal order or causal influence. Timelike-separated events ($\Delta s^2 > 0$, steeper than $45^\circ$) have an order all observers agree on and *can* be causally connected; spacelike-separated events ($\Delta s^2 < 0$, flatter than $45^\circ$) have an order that depends on the frame and *cannot* influence each other. This trichotomy is the backbone of every causal argument in relativity and the resolution of every "but observer $X$ sees it happen first" puzzle — the puzzle only arises for spacelike separations, where there is genuinely no preferred order, and it dissolves once you note that spacelike events cannot affect one another anyway. Reaching for the sign of the interval is the relativistic reflex that replaces the Newtonian assumption of universal time-ordering.

**The light cone is a frame-independent object, and the invariant causal structure it defines is the deepest survivor of the collapse of absolute time.** Although elapsed time, length, simultaneity, and the order of spacelike events are all frame-dependent, the partition of spacetime into the future, past, and elsewhere of each event is *absolute* — every inertial observer draws the identical $45^\circ$ cone, because the cone is the locus $\Delta s^2 = 0$ and the interval is invariant. This is the precise sense in which relativity, despite its name, *increases* the stock of absolutes: it discards Newton's absolute time and space but installs an absolute causal structure firmer than anything before. The transferable insight for problem-solving is that the light cone is the right scaffolding for any question about influence, information flow, or causation: draw the cones, and what is causally possible (inside) and impossible (outside) becomes a matter of geometry that no choice of frame can alter. In curved spacetime this same cone structure survives locally and becomes the defining feature of a Lorentzian metric — the seed of black-hole horizons and cosmological causal boundaries.
