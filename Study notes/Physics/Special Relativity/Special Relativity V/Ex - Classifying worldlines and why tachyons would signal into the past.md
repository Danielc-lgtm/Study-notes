---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Worldline of a Particle"
  - "Def - Classification of Four-Vectors"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

Working with $c = 1$ and signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$:

1. Classify each of the following straight worldlines as timelike (a massive particle), null (a photon), or spacelike (a tachyon), by computing the norm of the tangent: (a) $x^\mu(\lambda) = \lambda(2,1,0,0)$; (b) $x^\mu(\lambda) = \lambda(1,1,0,0)$; (c) $x^\mu(\lambda) = \lambda(1,2,0,0)$; (d) $x^\mu(\lambda) = \lambda(1, \tfrac12, \tfrac12, \tfrac12)$.
2. Prove that the type of a [[Def - Worldline of a Particle|worldline]] (the sign of its tangent's norm) is **Lorentz invariant**, so all observers agree on whether a worldline is a massive particle, a photon, or a tachyon.
3. Show that for a **spacelike** worldline (a tachyon), the time-ordering of two events on it is *not* Lorentz invariant: there is an inertial frame in which the tachyon travels backward in time. Conclude that a tachyon used to carry a signal would let some observer receive the signal before it was sent.
4. Argue that this is why a consistent massive particle follows a worldline that is timelike *everywhere* — and cannot change type partway along.

**Recall:**

![[Def - Worldline of a Particle#The Definition]]

A vector is [[Def - Classification of Four-Vectors|timelike]] if $X \cdot X > 0$, null if $X \cdot X = 0$, spacelike if $X \cdot X < 0$ (mostly-minus). A worldline is the history of a particle; a massive particle's worldline is timelike, a photon's is null. The time-ordering of two events depends on the frame exactly when they are spacelike-separated. A boost along $x$ is the [[Def - The Lorentz Transformation|Lorentz transformation]] $t' = \gamma(t - vx)$, $x' = \gamma(x - vt)$.

---

# Convergent Strategy

**Problem class.** A *classify-and-reason-about-causality* problem — the foundational sorting of worldlines into massive / photon / tachyon, plus the causal argument that excludes tachyons. The [[Special Relativity V — Worldlines, Proper Time and Four-Velocity#Problem-Solving Strategy|topic strategy]] says: classify a worldline by the sign of its tangent's norm, and read causal questions off the [[Def - Photons and Null Geodesics|light-cone]] structure.

**Assumption pattern.** The single computational input is the sign of $V \cdot V$ for the tangent $V$. Everything causal follows from one fact about the indefinite metric: the *sign* of the norm is invariant (so type is absolute), but for spacelike separations the *sign of the time component* is not (so time-ordering is frame-dependent). The exclusion of tachyons is then a causality argument, not a computation.

**Theorem routing.** Part 1 is direct computation of $V \cdot V$. Part 2 routes through the [[Thm - Invariance of the Spacetime Interval|invariance of the interval]]: the norm is invariant, so its sign is too. Part 3 routes through an explicit boost that flips the sign of the time component of a spacelike separation. Part 4 is the consistency argument: type must be constant because a type-changing worldline would have a spacelike stretch, hence a causal pathology.

**Key decision point.** The crux is recognising the asymmetry between timelike and spacelike separations: for timelike, both the norm's sign *and* the time-ordering are invariant (causal order is absolute); for spacelike, only the norm's sign is invariant, while the time-ordering flips between frames (no causal order). This single asymmetry is the entire content of "why tachyons signal into the past".

---

# Legal Operations Used

1. **Classify a worldline by the sign of its tangent's norm** (operation 9 from the topic page). Parts 1–2 are this operation and the proof of its frame-independence.

2. **Compute an invariant** (operation 7 from the topic page). The norm $V \cdot V$ is Lorentz invariant, which is what makes the classification absolute.

3. **Apply a Lorentz transformation to test frame-dependence** (operation 1 from the topic page). Part 3 boosts a spacelike separation to a frame where its time-ordering reverses.

---

# Hints

> [!note]- Hint 1
> For each tangent $V = dx^\mu/d\lambda$, compute $V \cdot V = (V^0)^2 - (V^1)^2 - (V^2)^2 - (V^3)^2$. Positive $\Rightarrow$ timelike (massive); zero $\Rightarrow$ null (photon); negative $\Rightarrow$ spacelike (tachyon).

> [!note]- Hint 2
> The norm $V \cdot V = \eta_{\mu\nu}V^\mu V^\nu$ is a Lorentz scalar (this is the [[Thm - Invariance of the Spacetime Interval|invariance of the interval]], applied to a tangent). A scalar has the same value, hence the same sign, in every frame — so the classification is frame-independent.

> [!note]- Hint 3
> Take two events spacelike-separated, e.g. $\Delta x^\mu = (\Delta t, \Delta x, 0, 0)$ with $\Delta x > \Delta t > 0$ (spacelike: $\Delta t^2 - \Delta x^2 < 0$). Boost: $\Delta t' = \gamma(\Delta t - v\Delta x)$. Choose $v$ between $\Delta t/\Delta x$ and $1$ to make $\Delta t' < 0$ — the time-ordering reverses.

> [!note]- Hint 4
> A worldline that were timelike on one stretch and spacelike on another would have a spacelike segment; by part 3, some observer sees the particle traverse that segment backward in time. Combined with another boost, this enables sending information into one's own past — a causal contradiction. So physical worldlines keep one type throughout.

---

# Solution

This exercise sorts the three kinds of worldline and then deploys the one causal argument that singles out timelike worldlines as the only consistent histories of signal-carrying matter. The plan: Step 1 classifies the examples; Step 2 proves type is invariant; Step 3 shows spacelike worldlines reverse their time-ordering; Step 4 concludes type must be constant.

**Step 1: Classifying the worldlines.**

> [!note]- Derivation
> Compute $V \cdot V = (V^0)^2 - |\mathbf{V}|^2$ for each tangent:
> - **(a)** $V = (2, 1, 0, 0)$: $V \cdot V = 4 - 1 = 3 > 0$ — **timelike**, a massive particle (speed $u = \tfrac12 < 1$).
> - **(b)** $V = (1, 1, 0, 0)$: $V \cdot V = 1 - 1 = 0$ — **null**, a photon (speed $1$).
> - **(c)** $V = (1, 2, 0, 0)$: $V \cdot V = 1 - 4 = -3 < 0$ — **spacelike**, a tachyon (would-be speed $2 > 1$).
> - **(d)** $V = (1, \tfrac12, \tfrac12, \tfrac12)$: $V \cdot V = 1 - (\tfrac14 + \tfrac14 + \tfrac14) = 1 - \tfrac34 = \tfrac14 > 0$ — **timelike**, a massive particle (speed $\sqrt{3}/2 < 1$).
>
> The rule is simply the sign of the norm, equivalently whether the coordinate speed $|\mathbf{V}|/V^0$ is less than, equal to, or greater than $1$.

**Step 2: Type is Lorentz invariant.**

> [!note]- Derivation
> The norm of the tangent, $V \cdot V = \eta_{\mu\nu}V^\mu V^\nu$, is a **Lorentz scalar** — by the [[Thm - Invariance of the Spacetime Interval|invariance of the interval]] applied to the tangent vector, it takes the same value in every inertial frame. (Directly: under $V \to \Lambda V$, $V' \cdot V' = (\Lambda V)^{\mathsf T}\eta(\Lambda V) = V^{\mathsf T}(\Lambda^{\mathsf T}\eta\Lambda)V = V^{\mathsf T}\eta V = V \cdot V$, using $\Lambda^{\mathsf T}\eta\Lambda = \eta$.) Since the *value* of $V \cdot V$ is the same in all frames, so is its *sign*. Therefore the classification — timelike, null, or spacelike — is **frame-independent**: every observer agrees on whether a worldline is a massive particle, a photon, or a tachyon. This is essential for the notion of "particle type" to be physical: mass-vs-massless cannot depend on who is looking.

**Step 3: Spacelike worldlines reverse their time-ordering.**

> [!note]- Derivation
> Take two events on a spacelike worldline, separated by $\Delta x^\mu = (\Delta t, \Delta x, 0, 0)$ with $\Delta x > \Delta t > 0$ (spacelike: $\Delta t^2 - \Delta x^2 < 0$, i.e. the "tachyon" covers more space than time, speed $> 1$). In frame $S$ the second event is later, $\Delta t > 0$. Boost to a frame $S'$ moving at speed $v$ along $x$:
> $$\Delta t' = \gamma(\Delta t - v\,\Delta x).$$
> Choose any $v$ in the range $\dfrac{\Delta t}{\Delta x} < v < 1$ (nonempty since $\Delta t/\Delta x < 1$): then $\Delta t - v\Delta x < 0$, so $\Delta t' < 0$. **In $S'$ the second event is earlier than the first** — the tachyon travels backward in time. Because the time-ordering of spacelike-separated events is frame-dependent, there is no observer-independent "before" and "after" for the two ends of a tachyon's trip.
>
> Now suppose the tachyon carries a *signal* from the first event (the sender) to the second (the receiver). In $S$ the signal goes forward in time; but in $S'$ it is received *before* it is sent. Worse, a sender who could emit tachyons in any frame could, by combining a tachyon sent in one frame with a tachyon reply sent in another, arrange to receive an answer to a message *before sending the message* — a signal into their own past, a genuine causal contradiction (the "tachyonic antitelephone").

**Step 4: Why physical worldlines keep one type throughout.**

> [!note]- Derivation
> The causal pathology of Step 3 is exactly why a consistent particle that can carry information must have a worldline that is **timelike everywhere** (or null, for massless signals). For a timelike separation $\Delta t^2 - \Delta x^2 > 0$, the boost $\Delta t' = \gamma(\Delta t - v\Delta x)$ keeps $\Delta t' > 0$ for *all* allowed $|v| < 1$ (since $|v\Delta x| < |\Delta x| \le |\Delta t|$ would be needed to flip the sign, but $|\Delta x| < |\Delta t|$ for timelike), so the time-ordering of timelike-separated events is **invariant**: cause precedes effect in every frame. Timelike worldlines are therefore causally safe; spacelike ones are not.
>
> This also forbids a worldline from *changing type* partway along. If a worldline were timelike on one stretch and spacelike on another (a massive particle "accelerating through the speed of light"), the spacelike stretch would, by Step 3, be traversed backward in time in some frame — the particle would appear to un-happen, and could carry information into the past. There is no consistent relativistic dynamics for such a worldline. Hence the three classes are mutually exclusive and a physical worldline stays in one: **always timelike** (massive particles, [[Def - Worldline of a Particle]]), **always null** (photons, [[Def - Photons and Null Geodesics]]), or — only as a mathematical curiosity with no consistent dynamics — always spacelike (tachyons, excluded).

> [!note]- Complete formal solution
> Classifying by $V \cdot V = (V^0)^2 - |\mathbf V|^2$: (a) $4-1=3>0$ timelike; (b) $1-1=0$ null; (c) $1-4=-3<0$ spacelike; (d) $1-\tfrac34=\tfrac14>0$ timelike. The norm is a Lorentz scalar ($V'\cdot V' = V^{\mathsf T}\Lambda^{\mathsf T}\eta\Lambda V = V^{\mathsf T}\eta V$), so its sign — the classification — is frame-independent. For a spacelike separation $\Delta x^\mu = (\Delta t, \Delta x, 0,0)$ with $\Delta x > \Delta t > 0$, the boost $\Delta t' = \gamma(\Delta t - v\Delta x)$ becomes negative for $\Delta t/\Delta x < v < 1$, reversing the time-ordering — so a tachyon signal is received before sent in some frame, and combining two such signals sends information into one's past. For timelike separations the ordering cannot flip ($|\Delta x| < |\Delta t|$), so cause precedes effect in all frames; this is why physical worldlines are timelike (or null) everywhere and cannot change type, a type-changing worldline having a causally pathological spacelike segment. $\blacksquare$

> [!warning] Illegal but tempting: thinking a tachyon merely "looks like" it goes backward, harmlessly
> One might dismiss the time-reversal of Step 3 as a harmless optical relabelling — "it only *looks* backward to some observer". It is not harmless, because relativity grants every inertial observer equal standing: if the signal is genuinely received before sent in *some* valid frame, then in *that* frame the effect precedes its cause, and one can build a closed causal loop (the antitelephone) sending information into one's own past. The reason timelike separations escape this is structural, not optical: the time-ordering of timelike-separated events is *invariant*, so "received before sent" never occurs in any frame. The diagnostic: a causal relation is safe only if it is observer-independent, and the indefinite metric guarantees observer-independence exactly for timelike (and null) separations — which is why information-carrying worldlines must be timelike or null, and the speed of light is an absolute ceiling, not a mere appearance.

---

# Key Takeaways

**The sign of the tangent's norm classifies a worldline, and the classification is absolute.** Every worldline is sorted, pointwise, by one number: $V \cdot V > 0$ (timelike, massive particle), $= 0$ (null, photon), or $< 0$ (spacelike, tachyon), equivalently by whether the coordinate speed is below, at, or above $1$. Because the norm is a [[Thm - Invariance of the Spacetime Interval|Lorentz scalar]], its sign is the same in every frame, so "massive vs massless vs tachyonic" is an observer-independent fact — as it must be for particle type to be physical. The reusable reflex: to classify any worldline, four-vector, or separation, compute the sign of its Minkowski norm, and trust that the answer is frame-independent. This single sign organises the entire causal structure of spacetime.

**Time-ordering is invariant for timelike separations, frame-dependent for spacelike — and that is the whole of causality.** The deep asymmetry of the indefinite metric is that for timelike-separated events the time-ordering cannot be reversed by any boost (cause precedes effect in all frames), while for spacelike-separated events it can (no invariant "before"). This single fact is the origin of relativistic causality: events that can influence each other are timelike- or null-separated, and their causal order is absolute; events that are spacelike-separated cannot influence each other, and their order is a matter of frame. The trigger to carry away: whenever a causal question arises ("can $A$ affect $B$?", "is this signal allowed?"), compute the separation's norm — timelike/null means causally connectible with absolute order, spacelike means causally disconnected with no order. This is why the light cone is the boundary of causality.

**Worldlines keep one type throughout because changing type would break causality.** A massive particle cannot accelerate through the speed of light, not as a mere kinematic bound but because a worldline with both timelike and spacelike stretches would have a segment traversed backward in time in some frame, enabling information transfer into the past. So the three classes are mutually exclusive and a physical worldline stays in one — always timelike, always null, or (only as a dynamics-free curiosity) always spacelike. This is the deeper reason behind the speed limit: it is enforced by causality, not by any force. The general principle: the structure of [[Def - Minkowski Space and the Metric|Minkowski space]] permits exactly the causal relations that are observer-independent, and the prohibition on faster-than-light *signalling* (as opposed to faster-than-light *appearances*, which are harmless) is the precise content of "nothing outruns light". See [[Def - Photons and Null Geodesics]] for the light-cone structure that draws the boundary between these regimes.
