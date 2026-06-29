---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Relativity of Simultaneity"
  - "Def - The Spacetime Interval"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, so light rays have $45^\circ$ worldlines and $|v| < 1$. We work on [[Def - Minkowski Space and the Metric|Minkowski space]] with the **mostly-minus** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, so the [[Def - The Spacetime Interval|interval]] between two events separated by $(\Delta t, \Delta x, \Delta y, \Delta z)$ is $\Delta s^2 = \Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$, and a **timelike** separation has $\Delta s^2 > 0$, **spacelike** has $\Delta s^2 < 0$, **null** (lightlike) has $\Delta s^2 = 0$. Events are points $P, Q, R$ of spacetime; we plot $t$ vertically and $x$ (and one transverse direction, where a cone needs picturing) horizontally. Full registry on [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction]].

> [!warning] Convention
> Gourgoulhon and many field-theory texts use the opposite, **mostly-plus** signature $\eta = \mathrm{diag}(-1,+1,+1,+1)$, in which a timelike separation has $\Delta s^2 < 0$. We use mostly-minus throughout, so *timelike $\Leftrightarrow \Delta s^2 > 0$*. When importing a formula from a mostly-plus source, flip the overall sign of the metric and swap the inequality directions on the timelike/spacelike conditions.

---

# Axiom Motivation

The relativity of simultaneity is liberating and alarming in equal measure. Liberating, because "now" turns out to be a free choice; alarming, because it seems to put the order of events up for grabs, and if observers cannot agree on which of two events came first, what becomes of cause and effect? If I can find a frame in which the cause comes after the effect, causality is in ruins. The motivation for this definition is to show that the damage is *bounded*: there is a precise, frame-independent structure — the light cone — that says exactly which event-orderings are negotiable and which are absolute, and it is engineered so that cause-and-effect is never one of the negotiable ones.

The key observation is the one that closes [[Def - The Relativity of Simultaneity|the relativity of simultaneity]]: a moving frame's line of simultaneity has slope $v$ on a spacetime diagram, and because every physical frame has $|v| < 1$, that line can never tilt past $45^\circ$. So while different frames tilt their "now" lines this way and that, *no frame can tilt its now-line past the light line*. This single bound is what saves causality. Draw the two $45^\circ$ light rays through an event $P$. They divide spacetime into four regions: the wedge above $P$ (the future), the wedge below (the past), and the two side wedges (jointly the "elsewhere"). Any other frame's simultaneity line through $P$, having slope less than $1$ in magnitude, stays within the side wedges — it can never swing an above-$P$ event below $P$, or vice versa. Therefore *all frames agree that future-wedge events are after $P$ and past-wedge events are before $P$*. Only for elsewhere events — the spacelike-separated ones — can the order be reversed, and those are exactly the events $P$ cannot reach.

This dictates what the definition must capture. We want a partition of the events relative to $P$ into three classes: those whose order relative to $P$ all observers agree on and which $P$ can causally influence (the future, and dually the past), and those whose order is frame-dependent and which are causally cut off from $P$ (the elsewhere). The classifying quantity must be frame-independent, or the classification would itself be relative and useless. The [[Thm - Invariance of the Spacetime Interval|interval is exactly such a quantity]]: $\Delta s^2$ is the same in every frame, so its *sign* is too, and the sign is precisely the [[Def - Classification of Four-Vectors|timelike/spacelike/null trichotomy]]. Timelike ($\Delta s^2 > 0$): inside the cone, order-invariant, causally connectible. Spacelike ($\Delta s^2 < 0$): outside, order-ambiguous, causally disconnected. Null ($\Delta s^2 = 0$): on the cone, connectible only by light. The light cone is the boundary $\Delta s^2 = 0$, the locus of the $45^\circ$ rays, and it is the frame-independent skeleton of causal structure.

Why must this be the definition and not a looser one? Suppose we tried to allow influence to propagate slightly outside the cone — a signal a hair faster than light. The bound on simultaneity lines then turns against us. If a signal travels from $P$ to a spacelike-separated event $Q$ (outside $P$'s future cone), then because $Q$ is in $P$'s elsewhere there exists a frame in which $Q$ is *earlier* than $P$. In that frame the signal arrives before it was sent: the effect precedes the cause. Worse, a second observer could send a faster-than-light reply, and by chaining the two one could send a message into one's own past and create a paradox (warn yourself not to send the message you just sent). So the requirement "no influence propagates outside the light cone" is forced by the demand that no observer ever sees an effect precede its cause — and that requirement is *identical* to "nothing travels faster than light", because a worldline stays inside the cones exactly when it is everywhere timelike or null, i.e. slower than or equal to light. Causality and the light-speed limit are the same statement. The definition is not a convention; it is the unique structure that makes cause-and-effect frame-independent.

---

# The Definition

Fix an event $P$ in [[Def - Minkowski Space and the Metric|Minkowski space]]. For another event $Q$, let $\Delta X = Q - P$ be the displacement, with [[Def - The Spacetime Interval|interval]] $\Delta s^2 = \eta(\Delta X, \Delta X) = \Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$.

The **light cone of $P$** is the set of events at zero interval from $P$,
$$
\mathcal{C}(P) = \{\, Q : \Delta s^2 = 0 \,\} = \{\, Q : \Delta t^2 = \Delta x^2 + \Delta y^2 + \Delta z^2 \,\},
$$
the locus reachable from $P$ by a light ray. It consists of two nappes meeting at $P$: the **future light cone** ($\Delta t > 0$) and the **past light cone** ($\Delta t < 0$).

The light cone partitions the rest of spacetime by the sign of the interval, which is Lorentz-invariant ([[Thm - Invariance of the Spacetime Interval]]):

- $Q$ is in the **future** of $P$, written $P \prec Q$, if $\Delta s^2 > 0$ and $\Delta t > 0$ — timelike-separated and later. Equivalently $Q$ lies inside the future light cone. All inertial observers agree $Q$ is after $P$, and $P$ can causally influence $Q$ (a sub-light signal can run from $P$ to $Q$).
- $Q$ is in the **past** of $P$ if $\Delta s^2 > 0$ and $\Delta t < 0$ — timelike-separated and earlier; $Q$ lies inside the past light cone, all observers agree $Q$ is before $P$, and $Q$ can influence $P$.
- $Q$ is in the **elsewhere** of $P$ if $\Delta s^2 < 0$ — spacelike-separated. $Q$ lies outside both nappes; no signal can connect $P$ and $Q$; and there exist inertial frames in which $Q$ is before $P$, after $P$, or simultaneous with $P$. The temporal order of $P$ and $Q$ is frame-dependent.
- $Q$ is on the light cone if $\Delta s^2 = 0$: connectible to $P$ only by a light ray.

Two events are **causally connected** if one is in the future or past of the other (their separation is timelike or null); they are **causally disconnected** (or **causally independent**) if spacelike-separated. A worldline is **causal** (physically allowed for a massive or massless particle, or any signal) if and only if every infinitesimal displacement along it is timelike or null — equivalently, the worldline is everywhere at $45^\circ$ or steeper on a spacetime diagram, with speed $\le 1$.

The defining property, the **causality (chronology) condition**, is that physical influence propagates only along causal worldlines: $P$ can affect $Q$ only if $Q$ is in the future light cone of $P$. This is equivalent to the statement *nothing propagates faster than light*, and it guarantees that the time-order of any cause–effect pair is the same in every inertial frame.

---

# Categorical / Structural Definition

The light-cone partition equips spacetime with the structure of a **partially ordered set**. Define $P \preceq Q$ to mean $Q$ lies in the causal future of $P$ (i.e. $\Delta s^2 \ge 0$ and $\Delta t \ge 0$, including $P = Q$). This relation is reflexive, antisymmetric (if $P \preceq Q$ and $Q \preceq P$ then $P = Q$, because timelike/null future and past cones meet only at the apex), and transitive (the sum of two future-pointing causal vectors is future-pointing causal — this is the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] in the timelike case, and an easy cone-geometry argument in general). It is a *partial* order, not a total one: spacelike-separated events are incomparable, neither $P \preceq Q$ nor $Q \preceq P$.

The deep structural fact is that this causal order, together with the conformal (light-cone) structure, almost determines the geometry. **Zeeman's theorem** states that any bijection of Minkowski space (dimension $\ge 1+1$) preserving the causal order $\preceq$ in both directions is the composition of a Lorentz transformation, a translation, and an overall dilation — that is, the **causal automorphisms are exactly the conformal Poincaré transformations**. So the causal order is not extra structure layered on Minkowski space; it encodes the geometry up to scale. This is the precise sense in which "the order of events" is the primary physical datum and the metric is recoverable from it, and it is the flat prototype of the deep general-relativistic principle that the causal structure of a spacetime determines its conformal class.

---

# Relate to Other Fields / Compression

The light cone is the **conformal structure** of spacetime made concrete. Two Lorentzian metrics with the same light cones at every point differ only by a positive position-dependent rescaling $g \mapsto \Omega^2 g$; since causal relations depend only on which vectors have $\Delta s^2 \gtrless 0$, they depend only on the cone, hence only on the conformal class of the metric. This is why causal questions and conformal questions are the same questions, and why **Penrose diagrams** — which compactify an entire spacetime onto a finite picture by a conformal rescaling — preserve all causal relations while shrinking infinite distances: the rescaling keeps every cone at $45^\circ$.

**True name:** *The light cone is the set of points at zero interval, and it is the absolute speed limit drawn in spacetime.* The operational form to carry into problems: to settle any causal question — can $A$ influence $B$, can two observers disagree on their order, is a trajectory allowed — compute the sign of $\Delta s^2 = \Delta t^2 - \Delta x^2$. Positive means timelike, inside the cone, order-fixed, causally connectible; negative means spacelike, outside, order-reversible, causally cut off; zero means on the cone, light-connectible. Everything causal reduces to that one sign.

In algebraic and Lorentzian geometry this is the foundation of **causal theory** (the work of Penrose, Hawking, Geroch): chronological and causal futures $I^+(P)$, $J^+(P)$, achronal sets, Cauchy surfaces, global hyperbolicity, and the singularity theorems are all built on the light-cone structure introduced here, transported to a curved manifold where the cones tip and deform from point to point.

---

# Examples / Corollaries

**Is an instance — two events on a single light ray.** Events $P = (0,0)$ and $Q = (1,1)$ have $\Delta s^2 = 1 - 1 = 0$: they are null-separated, lying on the light cone of each other. A light pulse emitted at $P$ in the $+x$ direction arrives at $Q$. Every frame agrees they are connectible by light and that $Q$ is later (the order of null-separated events, like timelike, is invariant). This is the boundary case separating the causally connectible from the causally independent.

**Is an instance — a timelike pair whose order is absolute.** $P = (0,0)$ and $Q = (2,1)$ have $\Delta s^2 = 4 - 1 = 3 > 0$, timelike with $\Delta t > 0$: $Q$ is in $P$'s future. A particle moving at $v = \Delta x/\Delta t = 1/2 < 1$ travels from $P$ to $Q$, so $P$ can influence $Q$. No frame reverses the order: applying a boost, $\Delta t' = \gamma(\Delta t - v\Delta x) = \gamma(2 - v)$ stays positive for all $|v| < 1$. The order of timelike-separated events is frame-independent.

**Is an instance — a spacelike pair whose order is relative.** $P = (0,0)$ and $R = (1,2)$ have $\Delta s^2 = 1 - 4 = -3 < 0$, spacelike: $R$ is in $P$'s elsewhere. No signal connects them (that would need speed $\Delta x/\Delta t = 2 > 1$). The order *is* reversible: $\Delta t' = \gamma(1 - 2v)$ is positive for $v < 1/2$, zero at $v = 1/2$ (a frame in which $P$ and $R$ are simultaneous), and negative for $1/2 < v < 1$ (a frame in which $R$ precedes $P$). This is the relativity of simultaneity in its sharpest form, and it is harmless precisely because $P$ and $R$ cannot influence each other.

**Is NOT an instance — a faster-than-light worldline.** A trajectory from $P = (0,0)$ to $R = (1,2)$ would have speed $2 > 1$ and a spacelike displacement; it is *not* a causal worldline and no particle or signal can follow it. If it could, then since $R$ is in $P$'s elsewhere, a frame exists in which the signal arrives ($R$) before it is sent ($P$) — an effect preceding its cause. The exclusion of such worldlines is exactly the causality condition.

**Is NOT an instance — the phase velocity of a wave.** It is tempting to think nothing at all can exceed $c$, but the *phase velocity* of a wave (the speed of its crests) can exceed $c$ without violating causality, because no information rides on a bare crest. What must stay sub-light is the **group velocity**, the speed at which a modulation — an actual signal — propagates. So "nothing travels faster than light" is precisely "nothing that carries information has a spacelike worldline"; a phase pattern is not a counterexample.

**Corollary — no perfectly rigid body exists.** Push one end of a rod. If the far end responded instantly, the push would propagate along a spacelike worldline, transmitting information faster than light and connecting elsewhere-separated events — forbidden. In reality the push launches a compression (sound) wave through the rod, and the far end moves only when the wave arrives; the wave's speed is below $c$. So "there are no rigid bodies" is the same statement as "nothing propagates outside the light cone", applied to mechanical disturbances.

**Calibration check.** You have understood the definition if you can (i) classify the pairs $(0,0)$–$(3,1)$, $(0,0)$–$(1,1)$, and $(0,0)$–$(1,3)$ as timelike, null, or spacelike and say for each whether the order is frame-fixed; (ii) explain in one sentence why a faster-than-light signal lets some observer see the effect precede the cause; and (iii) state why "no rigid bodies" follows from the causality condition.

---

# Unlocked by This

> [!tip] The Speed-of-Light Ceiling on Velocity Addition *(from §2.3)*
> That causal worldlines must stay inside the light cone is the geometric face of the ceiling property of [[Thm - Relativistic Velocity Addition|velocity addition]]: composing sub-light boosts never produces a faster-than-light velocity, because the composition keeps the worldline timelike. The cone is the boundary no chain of boosts can cross.

> [!tip] Causal Structure on a Lorentzian Manifold *(from General Relativity)*
> On a curved spacetime the light cone exists at every point — it is the zero set of the metric $g_{\mu\nu}(x)$ in the tangent space — but the cones **tilt and deform** from event to event, and how they fit together globally is the **causal structure**. The **chronological and causal futures** $I^+(P)$ and $J^+(P)$, **Cauchy surfaces**, and **global hyperbolicity** are all built from it. A **black-hole horizon** is where the future cones tip so far inward that every future-directed worldline is dragged toward the singularity; **closed timelike curves** are pathological spacetimes where the cones tip enough to let a causal worldline return to its own past. The flat cone of this page, made rigorous as a Lorentz-invariant cone, is the local model every curved spacetime reduces to in the tangent space at each event.

> [!tip] Conformal Compactification and Penrose Diagrams *(from General Relativity)*
> Because causal relations depend only on the light cones, and the cones depend only on the metric up to a positive rescaling $g \mapsto \Omega^2 g$, one can **conformally compactify** a spacetime: rescale so that infinite proper distances become finite while every cone stays at $45^\circ$. The result is a **Penrose (conformal) diagram**, a finite picture whose boundary — future and past null infinity $\mathscr{I}^\pm$, spatial and timelike infinity, and horizons — displays the entire causal structure at a glance. This is the standard tool for analysing black holes, cosmological horizons, and the global causal anatomy of any spacetime, and it rests entirely on the light cone introduced here.

> [!tip] Microcausality in Quantum Field Theory *(from Quantum Field Theory)*
> The causality condition becomes, in relativistic quantum field theory, the axiom of **microcausality**: field operators at spacelike-separated points must **commute** (or anticommute, for fermions), $[\phi(x), \phi(y)] = 0$ whenever $x - y$ is spacelike. This is the quantum statement that measurements at causally disconnected events cannot interfere, and it is what forbids superluminal signalling at the level of operators. Combined with positivity of energy it forces the existence of antiparticles (the **spin–statistics** and **CPT** theorems), so the humble light cone of this page is, in the end, why antimatter exists.
