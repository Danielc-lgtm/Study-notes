---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Causality and the Light Cone"
  - "Def - The Spacetime Interval"
  - "Thm - Invariance of the Spacetime Interval"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and the mostly-minus signature, so the [[Def - The Spacetime Interval|interval]] between events separated by $(\Delta t, \Delta x)$ is $\Delta s^2 = \Delta t^2 - \Delta x^2$, with timelike $\Delta s^2 > 0$. Consider an event $P$ at the origin.

1. Describe the **light cone** of $P$ and the three regions it bounds (future, past, elsewhere), and classify a general event $Q = (\Delta t, \Delta x)$ as timelike-, spacelike-, or null-separated from $P$ by the sign of $\Delta s^2$.
2. Prove that the three regions are **Lorentz-invariant**: a boost cannot move an event from inside the future cone to the elsewhere, etc. (Use the invariance of the interval and the sign of $\Delta t$.)
3. Prove that **timelike-separated** events have a frame-independent time order, while **spacelike-separated** events do not: for the latter, exhibit a boost velocity that makes $\Delta t' = 0$ (simultaneous) and one that makes $\Delta t' < 0$ (order reversed). Find the threshold velocity in terms of $\Delta t, \Delta x$.
4. Conclude that a faster-than-light influence is equivalent to backward-in-time signalling, and hence that every physical (causal) worldline must be timelike or null — at or below the speed of light. State the corollary that there are no perfectly rigid bodies.

**Recall:**

![[Def - Causality and the Light Cone#The Definition]]

The [[Thm - Invariance of the Spacetime Interval|interval is invariant]]: under a [[Def - The Lorentz Transformation|Lorentz transformation]] $t' = \gamma(t - vx)$, $x' = \gamma(x - vt)$, the quantity $\Delta s^2 = \Delta t^2 - \Delta x^2$ is unchanged. An event $Q$ is in the **causal future** of $P$ if it can be reached from $P$ by a signal travelling at or below $c$; the **causality condition** is that physical influence propagates only to the causal future.

---

# Convergent Strategy

**Problem class.** A *causal-question* problem: decide which event-orderings are absolute and which are negotiable, and why. The [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction#Problem-Solving Strategy|topic strategy]] says: classify the separation by the sign of $\Delta s^2$, then use the invariance of that sign to settle frame-dependence.

**Assumption pattern.** The decisive facts are two invariances. The interval $\Delta s^2$ is Lorentz-invariant, so its *sign* (the timelike/spacelike/null class) is frame-independent. And for timelike or null separations the sign of $\Delta t$ is also invariant, so the *order* is too. The whole structure follows from deciding which of these signs a boost can flip.

**Theorem routing.** Part 1 is the classification by $\text{sign}(\Delta s^2)$ ([[Def - Causality and the Light Cone]]). Part 2 routes through [[Thm - Invariance of the Spacetime Interval|interval invariance]]: the class is the sign of an invariant. Part 3 routes through the explicit boost $\Delta t' = \gamma(\Delta t - v\Delta x)$: solve $\Delta t' = 0$ for $v$ and check whether the required $v$ is physical ($|v| < 1$). Part 4 chains "spacelike $\Rightarrow$ order reversible in some frame" with "a signal connecting spacelike events $\Rightarrow$ effect before cause in that frame".

**Key decision point.** The crux is recognising that a boost can flip the sign of $\Delta t$ *only* when the separation is spacelike. Setting $\Delta t' = \gamma(\Delta t - v\Delta x) = 0$ requires $v = \Delta t/\Delta x$, which has $|v| < 1$ exactly when $|\Delta t| < |\Delta x|$, i.e. exactly for spacelike separation. For timelike separation the required $v$ would exceed $1$ and is unphysical, so the order cannot be reversed. The single inequality $|\Delta t| \lessgtr |\Delta x|$ governs everything.

---

# Legal Operations Used

1. **Classify a separation by the sign of its interval** (the causal-classification move, from [[Def - Causality and the Light Cone]]). Computing $\text{sign}(\Delta s^2) = \text{sign}(\Delta t^2 - \Delta x^2)$ assigns each event to future/past (timelike), elsewhere (spacelike), or the cone (null) — the backbone of all four parts.

2. **Compute an invariant in the most convenient frame** (operation 8 from the topic page). The interval is the invariant; its frame-independence is what makes the classification frame-independent in part 2.

3. **Apply the Lorentz transformation to map events between frames** (operation 1). Part 3 transforms the time coordinate, $\Delta t' = \gamma(\Delta t - v\Delta x)$, and solves for the boost that makes it vanish or change sign.

4. **Read off geometry from a spacetime diagram** (operation 9). The light cone at $45^\circ$, the tilted simultaneity lines never exceeding $45^\circ$, and the regions they carve out are the picture behind every step.

---

# Hints

> [!note]- Hint 1
> Everything is governed by one comparison: is $|\Delta t|$ bigger or smaller than $|\Delta x|$? If bigger, the separation is timelike (inside the cone); if smaller, spacelike (outside); if equal, null (on the cone). The light cone is the locus $\Delta t = \pm\Delta x$, the two $45^\circ$ lines through $P$.

> [!note]- Hint 2
> For invariance of the classification: the interval $\Delta s^2 = \Delta t^2 - \Delta x^2$ is the same in every frame, so its sign is too — no boost can turn a positive interval negative. For invariance of the *order* within the timelike class, you additionally need that $\text{sign}(\Delta t)$ cannot flip; that is what part 3 establishes.

> [!note]- Hint 3
> Under a boost, $\Delta t' = \gamma(\Delta t - v\Delta x)$. To make the two events simultaneous in $S'$, set $\Delta t' = 0$ and solve for $v$. You get $v = \Delta t/\Delta x$. Now ask: is this a *physical* velocity, $|v| < 1$? It is exactly when $|\Delta t| < |\Delta x|$ — the spacelike case. For timelike separation the required $v$ exceeds $1$ and no such frame exists.

> [!note]- Hint 4
> Suppose a signal could travel from $P$ to a spacelike-separated $Q$ (faster than light, since $|\Delta x| > |\Delta t|$). By part 3 there is a frame in which $Q$ is *earlier* than $P$ — so in that frame the signal arrives before it is sent. That is backward-in-time signalling. Forbidding it forces every signal's worldline to be timelike or null. The rigid-body corollary: a push cannot reach the far end of a rod faster than the rod's internal sound speed, which is below $c$.

---

# Solution

The sign of the invariant interval sorts every event-pair into three classes. Inside the light cone (timelike) the order is absolute and influence is allowed; outside (spacelike) the order is frame-dependent and influence is forbidden; on the cone (null) only light connects. Causality is preserved precisely because nothing crosses the cone, which is the same as nothing exceeding $c$.

**Step 1: The light cone and the three regions.**

> [!note]- Derivation
> The **light cone** of $P = (0,0)$ is the set of events $Q = (\Delta t, \Delta x)$ reachable from $P$ by a light ray, i.e. with $\Delta s^2 = \Delta t^2 - \Delta x^2 = 0$, the two $45^\circ$ lines $\Delta t = \pm\Delta x$ (in $1+1$ dimensions; in $1+3$, the cone $\Delta t^2 = \Delta x^2 + \Delta y^2 + \Delta z^2$). It has two nappes: the **future** ($\Delta t > 0$) and the **past** ($\Delta t < 0$). Off the cone, classify by the sign of $\Delta s^2$:
> - $\Delta s^2 > 0$ ($|\Delta t| > |\Delta x|$): **timelike**, inside the cone. If $\Delta t > 0$, $Q$ is in $P$'s future; if $\Delta t < 0$, in its past.
> - $\Delta s^2 < 0$ ($|\Delta t| < |\Delta x|$): **spacelike**, outside the cone — the **elsewhere**.
> - $\Delta s^2 = 0$: **null**, on the cone.
>
> A particle from $P$ at speed $u$ traces $\Delta x = u\,\Delta t$, with $|\Delta x/\Delta t| = |u| < 1$, so its endpoint is timelike-separated; light traces the null cone. Thus the future cone is exactly the set of events a sub-light-or-light signal from $P$ can reach.

**Step 2: The three regions are Lorentz-invariant.**

> [!note]- Derivation
> The interval $\Delta s^2 = \Delta t^2 - \Delta x^2$ is invariant under [[Def - The Lorentz Transformation|Lorentz transformations]] ([[Thm - Invariance of the Spacetime Interval]]): $\Delta t'^2 - \Delta x'^2 = \Delta t^2 - \Delta x^2$. Therefore its *sign* is the same in every inertial frame, and the timelike/spacelike/null classification is frame-independent — no boost can move an event from inside the cone (timelike) to outside (spacelike), or vice versa, because that would change the sign of an invariant.
>
> The future/past split *within* the timelike class also survives, and this needs the extra fact, proved in Step 3, that for timelike (and null) separation $\text{sign}(\Delta t)$ is invariant. Granting it: a boost preserves both $\text{sign}(\Delta s^2)$ and (for $\Delta s^2 \ge 0$) $\text{sign}(\Delta t)$, so "future cone", "past cone", and "elsewhere" are each Lorentz-invariant regions. The light cone is the invariant boundary, fixed because $\Delta s^2 = 0$ maps to $\Delta s^2 = 0$.

**Step 3: Timelike order is absolute; spacelike order is relative.**

> [!note]- Derivation
> Under a boost of velocity $v$, the time separation transforms as $\Delta t' = \gamma(\Delta t - v\,\Delta x)$. Ask when a frame makes the two events **simultaneous**, $\Delta t' = 0$:
> $$\Delta t - v\,\Delta x = 0 \ \Longrightarrow\ v = \frac{\Delta t}{\Delta x}.$$
> This velocity is **physical** ($|v| < 1$) if and only if $|\Delta t| < |\Delta x|$ — precisely the **spacelike** case. So:
> - *Spacelike* ($|\Delta t| < |\Delta x|$): the threshold velocity $v_* = \Delta t/\Delta x$ satisfies $|v_*| < 1$. At $v = v_*$ the events are simultaneous; for $v$ slightly larger than $v_*$, $\Delta t' = \gamma(\Delta t - v\Delta x)$ changes sign (since $\Delta x \ne 0$), so the **order reverses**. Hence there exist frames in which $Q$ precedes $P$, follows $P$, or is simultaneous with $P$: the order is frame-dependent.
> - *Timelike* ($|\Delta t| > |\Delta x|$): the would-be $v_* = \Delta t/\Delta x$ has $|v_*| > 1$, unphysical, so *no* boost makes the events simultaneous, and $\Delta t' = \gamma(\Delta t - v\Delta x)$ keeps the sign of $\Delta t$ for all $|v| < 1$ (indeed $\Delta t - v\Delta x \ge \Delta t - |v||\Delta x| > \Delta t - |\Delta x| \cdot 1 \ge 0$ when $\Delta t > |\Delta x| > 0$). The **order is absolute**.
>
> Concretely: $P = (0,0)$, $Q = (1, 2)$ is spacelike ($\Delta s^2 = 1 - 4 = -3$); $v_* = 1/2$ makes them simultaneous, and $v > 1/2$ puts $Q$ before $P$. Whereas $Q = (2, 1)$ is timelike ($\Delta s^2 = 3$); $\Delta t' = \gamma(2 - v) > 0$ for all $|v| < 1$, so $Q$ stays in $P$'s future.

**Step 4: No faster-than-light influence; no rigid bodies.**

> [!note]- Derivation
> Suppose a physical influence travelled from $P$ to a spacelike-separated event $Q$ — necessarily faster than light, since $|\Delta x| > |\Delta t|$ means average speed $|\Delta x/\Delta t| > 1$. By Step 3, there is an inertial frame $S'$ in which $Q$ occurs *before* $P$. In $S'$ the effect ($Q$) precedes its cause ($P$): the signal arrives before it is sent. Worse, a second observer at $Q$ could send a faster-than-light reply reaching $P$'s past, closing a loop in which one influences one's own past — a logical contradiction. To forbid this, physical influence must never connect spacelike-separated events: every signal, particle, or causal worldline must have a **timelike or null** separation between successive points, i.e. travel at or below $c$. This is the **causality condition**, and it is *identical* to the speed limit: a worldline stays inside the light cones exactly when its speed is $\le 1$.
>
> *Corollary — no rigid bodies.* If you push one end of a rod and the far end moved instantly, the disturbance would connect spacelike-separated events (the push here-now and the far-end-motion there-now), transmitting information faster than light. So the far end cannot respond until a signal — a compression (sound) wave through the material — reaches it, and that wave travels below $c$. A perfectly rigid body, in which a push is felt everywhere at once, would violate causality; hence none exists. "No rigid bodies" is the mechanical face of "nothing outruns light".

> [!note]- Complete formal solution
> The light cone of $P = (0,0)$ is $\{\Delta t = \pm\Delta x\}$ (null, $\Delta s^2 = 0$), bounding the timelike interior ($|\Delta t| > |\Delta x|$, $\Delta s^2 > 0$, split into future $\Delta t > 0$ and past $\Delta t < 0$) and the spacelike exterior or elsewhere ($|\Delta t| < |\Delta x|$, $\Delta s^2 < 0$). The class is the sign of the invariant $\Delta s^2 = \Delta t^2 - \Delta x^2$, hence frame-independent ([[Thm - Invariance of the Spacetime Interval]]); the future/past split survives because, for $\Delta s^2 \ge 0$, $\text{sign}(\Delta t)$ is also boost-invariant. Under $\Delta t' = \gamma(\Delta t - v\Delta x)$, the events are simultaneous when $v = \Delta t/\Delta x$, which is physical ($|v| < 1$) exactly for spacelike separation; there the order reverses for $v$ past the threshold, while for timelike separation no such frame exists and the order is absolute. A faster-than-light influence would connect spacelike-separated events, and by the above there is a frame in which the effect precedes the cause — backward-in-time signalling, forbidden. Hence every causal worldline is timelike or null (speed $\le c$), and as a corollary no perfectly rigid body exists, since a push propagates only at the material's sub-light sound speed. $\blacksquare$

---

# Key Takeaways

**One inequality, $|\Delta t|$ versus $|\Delta x|$, decides every causal question.** The entire causal structure of special relativity reduces to comparing the time separation of two events with their spatial separation. If $|\Delta t| > |\Delta x|$ the separation is timelike: the events are inside each other's light cones, causally connectible, and their order is the same for everyone. If $|\Delta t| < |\Delta x|$ it is spacelike: outside the cones, causally independent, with an order that some frame reverses. The boundary $|\Delta t| = |\Delta x|$ is the light cone itself. Whenever a problem asks "can $A$ cause $B$?", "will observers agree on the order?", or "is this trajectory allowed?", compute $\Delta s^2 = \Delta t^2 - \Delta x^2$ and read off the sign — that single number answers all three. The trigger is any causal or ordering question; the move is always to form the interval.

**Order-reversal and faster-than-light travel are the same impossibility.** This exercise welds two facts that look separate: that spacelike-separated events can have their order reversed by a boost, and that nothing can travel faster than light. They are one fact. The boost that reverses the order of two spacelike events is physical *precisely because* connecting them would require superluminal speed; so "the order can be reversed" and "no signal connects them" are two readings of $|\Delta x| > |\Delta t|$. Forbid effect-before-cause and you forbid faster-than-light influence, and vice versa — the speed limit is not an extra postulate bolted onto relativity but the exact condition that keeps causality frame-independent. The transferable diagnostic: any proposed faster-than-light signal can be turned, by a suitable boost, into a message to the past, so superluminal signalling and causality violation always stand or fall together.

**Invariance of a sign is the engine of frame-independence.** The reason causal structure survives the relativity of simultaneity is structural and worth abstracting: a quantity that is frame-independent has a frame-independent sign, and a *class* defined by that sign is therefore the same in all frames. The interval $\Delta s^2$ is the invariant; its sign is the causal class; so the causal class is absolute even though times, lengths, and the order of spacelike events are not. This is the same move that makes a particle's rest mass frame-independent (the sign and value of $P\cdot P$) and a four-vector's character invariant. Whenever you want to show some qualitative feature is observer-independent in relativity, look for the invariant whose sign or value encodes it — here, find the interval, and the causal structure comes for free. The corollary that no rigid body can exist is the same principle applied to mechanics: instantaneous rigidity would make a sign (the order of a push and its distant response) frame-dependent in a way that violates causality, so material disturbances must crawl below $c$. See also the companion exercise [[Ex - The relativity of simultaneity (Einstein's train)]] for the simultaneity side of the same coin, and [[Ex - The twin paradox]] for the proper-time consequences of timelike worldlines.
