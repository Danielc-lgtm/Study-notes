---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Classification of Four-Vectors"
  - "Def - The Spacetime Interval"
  - "Thm - Invariance of the Spacetime Interval"
tags: [physics, special-relativity]
---

# Problem Statement

Working with $c = 1$, in a spacetime diagram with $t$ vertical and $x$ horizontal.

1. Fix an event $O$ at the origin. Describe the **light cone** of $O$, and show that the timelike, spacelike, and null regions relative to $O$ are each invariant under Lorentz transformations.
2. For two events $O$ and $Q$ with **timelike** separation, show that all observers agree on their time order — if $Q$ is in $O$'s future for one observer, it is for all.
3. For two events $O$ and $R$ with **spacelike** separation, show that observers *disagree* on their time order: there exist frames in which $R$ is after $O$, before $O$, and simultaneous with $O$.
4. Conclude that **causal influence cannot propagate faster than light**: if a signal from $O$ could reach a spacelike-separated event $R$, then in some frame the signal would arrive *before* it was sent — and explain why a faster-than-light signal is equivalent to backward-in-time signalling.

**Recall:**

The exercise rests on the classification of separations and the invariance of the interval.

![[Def - Classification of Four-Vectors#The Definition]]

The [[Def - The Spacetime Interval|interval]] $\Delta s^2 = \Delta t^2 - \Delta x^2$ is [[Thm - Invariance of the Spacetime Interval|Lorentz invariant]], so its *sign* — the causal class — is the same for all observers. For a timelike or null separation the sign of $\Delta t$ is also invariant; for a spacelike separation it is not.

---

# Convergent Strategy

**Problem class.** A *decide-a-causal-question* and *establish-a-structural-fact* problem. The [[Special Relativity I — Lorentz Transformations and Minkowski Space#Problem-Solving Strategy|topic strategy]] routes causal questions through the sign of the interval and the geometry of the light cone.

**Assumption pattern.** Two events with a given causal class. The signpost is "do observers agree on the order" — answered by whether the time component's sign is Lorentz invariant, which depends on the class.

**Theorem routing.** Part 1: the cone is the null locus $\Delta t^2 = \Delta x^2$; invariance of the interval makes each region invariant. Part 2: for timelike separation, show $\Delta t' = \gamma(\Delta t - v\Delta x)$ cannot change sign because $|\Delta x| < |\Delta t|$ and $|v| < 1$. Part 3: for spacelike separation $|\Delta x| > |\Delta t|$, choose $v$ to make $\Delta t'$ positive, negative, or zero. Part 4: a superluminal signal connects spacelike-separated events, whose order is frame-dependent — so in some frame effect precedes cause.

**Key decision point.** The crux is the inequality $|\Delta x|$ versus $|\Delta t|$: timelike means $|\Delta t| > |\Delta x|$, and *that* is exactly what prevents the boost from flipping $\mathrm{sign}(\Delta t)$; spacelike means $|\Delta x| > |\Delta t|$, and *that* is what allows it.

---

# Legal Operations Used

1. **Classify a separation by the sign of its norm** — every part begins by determining the causal class.

2. **Compute an invariant** — the interval's invariance is what makes the class frame-independent.

3. **Apply the Lorentz transformation** to the time component $\Delta t' = \gamma(\Delta t - v\Delta x)$ and study its sign.

4. **Read off geometry from a spacetime diagram** — the light cone, the future/past/elsewhere regions.

---

# Hints

> [!note]- Hint 1
> The light cone of $O$ is the set of events $Q$ with null separation: $\Delta t^2 = \Delta x^2 + \Delta y^2 + \Delta z^2$, i.e. $|\Delta\mathbf{x}| = |\Delta t|$ — a double cone at $45^\circ$. Inside ($|\Delta t| > |\Delta\mathbf{x}|$) is timelike; outside is spacelike. Since $\Delta s^2$ is invariant, an event inside the cone for one observer is inside for all.

> [!note]- Hint 2
> For timelike separation, $|\Delta x| < |\Delta t|$. Under a boost, $\Delta t' = \gamma(\Delta t - v\Delta x)$. Show $\Delta t'$ has the same sign as $\Delta t$: since $|v| < 1$ and $|\Delta x| < |\Delta t|$, we have $|v\Delta x| < |\Delta t|$, so $\Delta t - v\Delta x$ cannot cross zero.

> [!note]- Hint 3
> For spacelike separation, $|\Delta x| > |\Delta t|$. Now $\Delta t' = \gamma(\Delta t - v\Delta x)$ *can* vanish: set $v = \Delta t/\Delta x$, which satisfies $|v| < 1$, and $\Delta t' = 0$. For $v$ slightly larger or smaller, $\Delta t'$ is negative or positive. So the order is frame-dependent.

> [!note]- Hint 4
> Suppose a signal travels from $O$ to a spacelike-separated $R$ — that means it covers a spatial distance greater than the time available, i.e. faster than light. By Part 3 there is a frame in which $R$ happens *before* $O$. In that frame the signal arrives before it is sent: effect precedes cause. A faster-than-light signal is, in some inertial frame, a signal into the past.

---

# Solution

The light cone partitions spacetime into the causally-connectible (timelike), the causally-disconnected (spacelike), and the boundary (null). Whether two observers agree on the order of two events is decided entirely by which side of the cone they lie on — and that decision is the protection of cause and effect.

**Step 1: The light cone and the invariance of the three regions.**

> [!note]- Derivation
> Fix $O$ at the origin. An event $Q$ at $(\Delta t, \Delta\mathbf{x})$ has null separation from $O$ when $\Delta s^2 = \Delta t^2 - |\Delta\mathbf{x}|^2 = 0$, i.e. $|\Delta\mathbf{x}| = |\Delta t|$. This locus is the **light cone** of $O$ — a double cone, opening at $45^\circ$ on a spacetime diagram (with $c = 1$). It has a **future sheet** ($\Delta t > 0$) and a **past sheet** ($\Delta t < 0$), meeting at $O$.
>
> The cone divides spacetime into three [[Def - Classification of Four-Vectors|regions]]:
> - **Timelike** ($\Delta s^2 > 0$, $|\Delta t| > |\Delta\mathbf{x}|$): *inside* the cone — the future interior and the past interior.
> - **Spacelike** ($\Delta s^2 < 0$, $|\Delta t| < |\Delta\mathbf{x}|$): *outside* the cone — sometimes called "elsewhere".
> - **Null** ($\Delta s^2 = 0$): *on* the cone.
>
> By [[Thm - Invariance of the Spacetime Interval|invariance of the interval]], $\Delta s^2$ has the same value for every observer, so its *sign* is frame-independent. Hence each of the three regions is **Lorentz invariant**: an event inside $O$'s light cone for one observer is inside it for all; the light cone itself maps to itself under every Lorentz transformation. The causal partition of spacetime is observer-independent — all observers draw the same light cone.

**Step 2: Timelike-separated events have a frame-independent order.**

> [!note]- Derivation
> Let $O$ and $Q$ be timelike separated: $\Delta s^2 = \Delta t^2 - \Delta x^2 > 0$, so $|\Delta x| < |\Delta t|$. Suppose $Q$ is in $O$'s future for some observer, $\Delta t > 0$. Under a boost to any other frame ($|v| < 1$),
> $$\Delta t' = \gamma(\Delta t - v\,\Delta x).$$
> Estimate the correction term: $|v\,\Delta x| = |v|\,|\Delta x| < 1\cdot|\Delta t| = |\Delta t| = \Delta t$ (using $|v| < 1$ and $|\Delta x| < |\Delta t|$, and $\Delta t > 0$). So $v\,\Delta x < \Delta t$, hence $\Delta t - v\,\Delta x > 0$, hence
> $$\Delta t' = \gamma(\Delta t - v\,\Delta x) > 0.$$
> $Q$ is in $O$'s future in *every* frame. **All observers agree on the time order of timelike-separated events.** The same holds for null separation ($|\Delta x| = |\Delta t|$, the inequality becomes non-strict but the sign is still preserved for $v < 1$). Causality is safe: if $Q$ can be influenced by $O$, every observer agrees $O$ came first.

**Step 3: Spacelike-separated events have a frame-dependent order.**

> [!note]- Derivation
> Let $O$ and $R$ be spacelike separated: $\Delta s^2 = \Delta t^2 - \Delta x^2 < 0$, so $|\Delta x| > |\Delta t|$. Under a boost,
> $$\Delta t' = \gamma(\Delta t - v\,\Delta x).$$
> Now the correction term can dominate. Consider three choices of $v$ (all with $|v| < 1$, since $|\Delta t/\Delta x| < 1$):
>
> - $v = 0$: $\Delta t' = \Delta t$. Say $\Delta t > 0$, so $R$ is *after* $O$.
> - $v = \Delta t/\Delta x$: then $\Delta t' = \gamma(\Delta t - \tfrac{\Delta t}{\Delta x}\Delta x) = 0$ — $R$ is *simultaneous* with $O$.
> - $v$ slightly larger than $\Delta t/\Delta x$ (still $< 1$, possible since $\Delta t/\Delta x < 1$): then $\Delta t - v\Delta x < 0$, so $\Delta t' < 0$ — $R$ is *before* $O$.
>
> So there exist frames in which $R$ is after, simultaneous with, and before $O$. **Observers disagree on the time order of spacelike-separated events.** This is consistent — it is the [[Ex - The relativity of simultaneity|relativity of simultaneity]] — *precisely because* no signal connects $O$ and $R$: reordering them changes no cause-and-effect relationship.

**Step 4: No causal influence faster than light.**

> [!note]- Derivation
> Suppose, for contradiction, that some signal — a particle, a wave, a message — travels from $O$ and influences an event $R$ that is **spacelike separated** from $O$. To do so, the signal covers spatial distance $|\Delta\mathbf{x}|$ in time $\Delta t < |\Delta\mathbf{x}|$ (spacelike means exactly $|\Delta t| < |\Delta\mathbf{x}|$): its speed exceeds $1$. A faster-than-light signal is precisely one that reaches outside the light cone.
>
> By Step 3, there is an inertial frame in which $R$ occurs *before* $O$ — $\Delta t' < 0$. In that frame, the signal arrives at $R$ before it departs from $O$: **the effect precedes the cause.** Worse, $R$ could be arranged (a relayed reply) to send a faster-than-light signal back to a point on $O$'s own worldline before $O$ — a message to one's own past. This is the route to genuine causal paradox (kill your grandfather, prevent your own departure).
>
> Therefore: *if causality is to hold for all observers, no causal influence may travel faster than light.* Equivalently, every causal worldline must be **timelike or null** — it must stay within the light cone. A faster-than-light signal and a backward-in-time signal are the same thing, related by a Lorentz boost; forbidding one forbids the other. This is why the speed of light is not merely the speed of light but the *universal speed limit on causation*, and why every physical worldline ([[Def - Classification of Four-Vectors]]) is timelike or null. (Note: this forbids the transmission of *information or influence* faster than light; it does not forbid, for instance, a laser spot sweeping across a distant wall faster than $c$, since the spot carries no signal from one point of the wall to the next.)

> [!note]- Complete formal solution
> The light cone of $O$ is the null locus $|\Delta\mathbf{x}| = |\Delta t|$; the interior is timelike, the exterior spacelike. Since $\Delta s^2$ is Lorentz invariant, its sign is frame-independent, so the three regions are each Lorentz invariant. For timelike $O,Q$ ($|\Delta x| < |\Delta t|$): under a boost $\Delta t' = \gamma(\Delta t - v\Delta x)$, and $|v\Delta x| < |\Delta t|$ forces $\Delta t'$ to keep the sign of $\Delta t$ — the order is frame-independent. For spacelike $O,R$ ($|\Delta x| > |\Delta t|$): choosing $v = 0$, $v = \Delta t/\Delta x$, $v > \Delta t/\Delta x$ makes $\Delta t'$ positive, zero, negative respectively — the order is frame-dependent. Hence a signal from $O$ to a spacelike-separated $R$ would, in some frame, arrive before it was sent; demanding causality for all observers forbids faster-than-light influence, so every causal worldline is timelike or null. $\blacksquare$

---

# Key Takeaways

**The sign of the interval is the causal class, and because the interval is invariant, causal structure is observer-independent.** Components of a separation are frame-dependent — $\Delta t$ and $\Delta x$ change under a boost — but $\Delta s^2 = \Delta t^2 - \Delta x^2$ does not, and neither does its sign. So the partition of spacetime into the timelike interior, the spacelike exterior, and the null cone is something *all* observers agree on. Every observer draws the same light cone at every event. This is the structural payoff of [[Thm - Invariance of the Spacetime Interval|interval invariance]]: the relative quantities (time, distance, simultaneity) are the shadows, but the causal skeleton — who can influence whom — is absolute. Whenever a problem asks a causal question, the move is always the same: compute $\Delta s^2$, read off the class, and the answer is frame-independent.

**Timelike order is protected, spacelike order is not — and the dividing inequality is $|\Delta t|$ versus $|\Delta x|$.** The whole of Steps 2 and 3 turns on one comparison. Timelike separation means $|\Delta t| > |\Delta x|$, and since a boost mixes in at most $|v||\Delta x| < |\Delta x| < |\Delta t|$, it can never overwhelm $\Delta t$ and flip its sign — the order is locked. Spacelike separation means $|\Delta x| > |\Delta t|$, and now the boost *can* mix in enough to flip $\Delta t$ — the order is up for grabs. This is the precise, quantitative reason the [[Ex - The relativity of simultaneity|relativity of simultaneity]] operates only on spacelike-separated events and never threatens cause and effect: the events whose order can be reordered are exactly the ones no signal connects. The reusable diagnostic: to know whether a claimed disagreement between frames is legitimate, compare $|\Delta t|$ with $|\Delta x|$ — equivalently, check the sign of $\Delta s^2$.

**Faster-than-light signalling is backward-in-time signalling — the speed of light is the speed limit of causation itself.** The deepest conclusion is that "nothing exceeds $c$" is not a fact about light or about engineering limits; it is a requirement of *causal consistency for all observers*. A signal reaching outside the light cone connects spacelike-separated events, whose order is frame-dependent, so in some frame it arrives before it departs — and a chain of such signals delivers a message to one's own past. The constancy of $c$ promotes $c$ from "the speed of light" to "the maximum speed of any cause" — which is why every physical worldline must be timelike or null, why no massive particle can be accelerated to $c$ ([[Ex - Composing boosts with rapidity]]), and why information can never outrun light even though, say, a swept laser spot can. The lesson generalises: in any relativistic theory, the light cone is the boundary of influence, and respecting it — building only causal, within-the-cone propagation — is the non-negotiable constraint on physical law.
