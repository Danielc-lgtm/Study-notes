---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Reversed Triangle Inequality"
  - "Thm - Inertial Worldlines Maximise Proper Time"
  - "Def - Classification of Four-Vectors"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

Two twins, Alice and Bob, part at event $E$. Alice stays at home in inertial frame $S$. Bob travels at speed $v$ to a distant planet, reaching it at event $P$, then immediately turns around and returns at speed $v$, reuniting with Alice at event $R$. In Alice's frame the planet is at distance $d$, so the trip takes total time $2T$ with $T = d/v$. Working with $c = 1$:

1. Find the proper time elapsed for Alice between $E$ and $R$, and for Bob.
2. **The paradox.** From Bob's point of view, *Alice* is the one who moves away and returns; by the symmetry of relativity, should not Alice be the younger one? Resolve this.
3. Give the resolution geometrically, using the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]].
4. Track the resolution on a spacetime diagram: show that at Bob's turnaround, his notion of "what Alice is doing now" jumps discontinuously, and that this jump accounts for the missing time.

**Recall:**

The exercise rests on proper time, the classification of worldlines, and the reversed triangle inequality.

![[Thm - The Reversed Triangle Inequality#Statement]]

The **proper time** along a timelike worldline is the time read by a clock carried along it — the integrated [[Def - The Spacetime Interval|interval]] $\int\sqrt{ds^2}$, equivalently the Minkowski norm $\|U\|$ of a straight timelike segment $U$. Alice's worldline is straight; Bob's is bent at $P$. That a straight timelike worldline carries the *most* proper time between two events is [[Thm - Inertial Worldlines Maximise Proper Time|the geodesic principle of special relativity]]. Acceleration is absolute and detectable ([[Def - Inertial Frame and the Postulates of Special Relativity]]) — Bob feels his turnaround, Alice feels nothing.

---

# Convergent Strategy

**Problem class.** A *resolve-a-paradox* problem. The [[Special Relativity V — Worldlines, Proper Time and Four-Velocity#Problem-Solving Strategy|topic strategy]] says: locate the unstated assumption, which is almost always absolute simultaneity, and the contradiction dissolves.

**Assumption pattern.** Two worldlines with the same endpoints, one straight and one bent. The signpost is the word "symmetry": the claimed symmetry between Alice and Bob is false, and finding *why* is the exercise.

**Theorem routing.** Part 1: time dilation, $\tau_{\text{Bob}} = 2T/\gamma < 2T = \tau_{\text{Alice}}$. Part 2: the symmetry breaks because Bob accelerates and Alice does not — only Bob changes inertial frame. Part 3: the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] $\|U+V\| \ge \|U\|+\|V\|$ makes the straight (Alice) worldline the longest in proper time ([[Thm - Inertial Worldlines Maximise Proper Time]]). Part 4: at the turnaround, Bob's line of simultaneity swings, sweeping a finite chunk of Alice's worldline.

**Key decision point.** The crux is that the situation is *not* symmetric: Alice stays in one inertial frame throughout, Bob occupies two (outbound and inbound) and must accelerate to switch. Acceleration is absolute — Bob feels it, Alice does not — and that physical asymmetry is what the proper-time difference records.

---

# Legal Operations Used

1. **Use time dilation** (operation 3 from the topic page) to compute Bob's elapsed time as seen from Alice's frame.

2. **Classify a worldline** (operation 9 from the topic page). Alice's and Bob's worldlines are timelike; Alice's is straight (one inertial frame), Bob's is bent.

3. **Read off geometry from a spacetime diagram** (operation 8 from the topic page). Part 4 is this operation: drawing Bob's lines of simultaneity before and after the turnaround.

4. **Apply the reversed triangle inequality** (operation 10 from the topic page) to identify the straight worldline as the longest in proper time.

---

# Hints

> [!note]- Hint 1
> Alice is at rest in $S$; her proper time between $E$ and $R$ is just the coordinate time, $2T$. Bob moves at speed $v$; his clock runs slow by $\gamma$, so on each leg his proper time is $T/\gamma$, total $2T/\gamma$. Since $\gamma > 1$, Bob ages less.

> [!note]- Hint 2
> The "symmetry" argument assumes Alice and Bob are interchangeable. They are not. Alice occupies a single inertial frame for the whole journey. Bob occupies *two* — one going out, one coming back — and to switch he must accelerate at $P$. Acceleration is absolute: Bob physically feels the turnaround (he is thrown against a wall of his ship); Alice feels nothing. The symmetry is broken by who accelerates.

> [!note]- Hint 3
> Model Bob's two legs as future-pointing timelike four-vectors $U$ (outbound) and $V$ (inbound). Alice's worldline, with the same endpoints $E$ and $R$, is the single vector $U + V$. The reversed triangle inequality gives $\|U+V\| \ge \|U\| + \|V\|$ — Alice's proper time is at least the sum of Bob's leg times. Straight beats bent.

> [!note]- Hint 4
> Draw the diagram in Alice's frame. Bob's line of simultaneity (his "now" across space) is tilted by his velocity. Going out, it tilts one way; coming back, the other way. At the turnaround event $P$, this line *swings* from one tilt to the other, and as it swings it sweeps across a whole segment of Alice's worldline. That swept segment is the time Alice "ages" during Bob's (idealised instantaneous) turnaround — the missing $2T(1 - 1/\gamma^2)$.

---

# Solution

The twin paradox is not a paradox: the two worldlines are genuinely different — one straight, one bent — and the reversed triangle inequality makes the straight one (Alice's) longer in proper time. The "symmetry" is an illusion, broken by the fact that only Bob accelerates. The plan: Step 1 computes the two proper times by time dilation; Step 2 locates the false assumption; Step 3 recasts the result as the reversed triangle inequality; Step 4 reconciles Bob's own bookkeeping via the relativity of simultaneity.

**Step 1: Alice ages $2T$, Bob ages $2T/\gamma$.**

> [!note]- Derivation
> Alice sits at rest at the origin of $S$ from $E$ to $R$. Her worldline is straight; her proper time is the coordinate time elapsed:
> $$\tau_{\text{Alice}} = 2T.$$
> Bob travels at speed $v$ on each leg. His clock, moving relative to $S$, runs slow by $\gamma$: each leg takes Alice-frame time $T$ but Bob-frame [[Def - Proper Time|proper time]] $T/\gamma$ (this is time dilation, or directly: each leg is a timelike displacement of $S$-coordinates $(\Delta t,\Delta x) = (T, \pm vT)$, with interval $\Delta s^2 = T^2 - v^2T^2 = T^2/\gamma^2$, so proper time $T/\gamma$). Summing the two legs,
> $$\tau_{\text{Bob}} = \frac{T}{\gamma} + \frac{T}{\gamma} = \frac{2T}{\gamma}.$$
> Since $\gamma > 1$, $\tau_{\text{Bob}} < \tau_{\text{Alice}}$: **Bob returns younger than Alice.** For $\gamma$ large the difference is dramatic — Bob could return to find Alice long dead.

**Step 2: Why the symmetry argument fails.**

> [!note]- Derivation
> The paradox is the claim: "From Bob's perspective Alice flies away and returns, so by relativity Alice should be younger — and that contradicts Step 1."
>
> The flaw is the phrase "by relativity". The principle of relativity says all *inertial* frames are equivalent. Alice is in a single [[Def - Inertial Frame and the Postulates of Special Relativity|inertial frame]] for the entire journey: she never accelerates, feels no force, and her worldline is one straight line. Bob is *not* in a single inertial frame. He is in one inertial frame on the outbound leg and a *different* one on the inbound leg, and to pass from one to the other he must accelerate at the turnaround event $P$.
>
> Acceleration is absolute and physically detectable — unlike uniform velocity, which is relative and undetectable. Bob *feels* the turnaround: he is pressed against the wall of his ship, his coffee spills, an accelerometer reads nonzero. Alice feels nothing throughout. There is a real, frame-independent physical difference between the twins, and it is not symmetric. The relativity principle never claimed Bob's situation equals Alice's; it only equates inertial observers, and Bob is not (always) one. The "symmetry" was never there.

**Step 3: The geometric resolution.**

> [!note]- Derivation
> Represent Bob's two inertial legs as future-pointing timelike four-vectors:
> $$U = (T, vT, 0, 0) \quad(\text{outbound}), \qquad V = (T, -vT, 0, 0) \quad(\text{inbound}).$$
> Their sum is $U + V = (2T, 0, 0, 0)$ — and this is precisely the displacement from $E$ to $R$ along *Alice's* worldline (she stays at $x = 0$, so her displacement is purely temporal).
>
> The [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] applies, since $U$ and $V$ are future-pointing timelike:
> $$\|U + V\| \ \ge\ \|U\| + \|V\|.$$
> Now $\|U+V\| = \sqrt{(2T)^2} = 2T = \tau_{\text{Alice}}$, and $\|U\| = \|V\| = \sqrt{T^2 - v^2T^2} = T/\gamma$, so $\|U\|+\|V\| = 2T/\gamma = \tau_{\text{Bob}}$. The inequality reads
> $$\tau_{\text{Alice}} \ \ge\ \tau_{\text{Bob}},$$
> with equality only if $U \parallel V$ — that is, only if Bob never actually turns around. **The straight worldline has the longest proper time** ([[Thm - Inertial Worldlines Maximise Proper Time]]). This is the entire resolution in one line: Alice's worldline is straight, Bob's is bent, and bending costs proper time. The paradox dissolves because the geometry of the two worldlines is genuinely different — there is no symmetry to respect.

**Step 4: The turnaround on the spacetime diagram.**

> [!note]- Derivation
> Draw the diagram in Alice's frame $S$: Alice's worldline is the vertical $t$-axis; Bob's is the bent path $E \to P \to R$. Bob's **line of simultaneity** — the events he regards as "now" — is, in $S$, a line of slope equal to his velocity (the relativity of simultaneity).
>
> *Outbound.* Bob moves at $+v$, so his simultaneity lines have slope $+v$, tilted *up* towards the future as they run from Bob's worldline towards Alice's. Just before reaching $P$, Bob's "now" intersects Alice's worldline at some event $X$, where Alice's clock reads $t_X = T/\gamma^2$ (apply the Lorentz transformation, or: Bob's proper time at $P$ is $T/\gamma$, and from Bob's outbound frame Alice's clock runs slow by another $\gamma$, giving $t_X = T/\gamma^2$).
>
> *Inbound.* After the turnaround Bob moves at $-v$, so his simultaneity lines now have slope $-v$, tilted the other way. Just after $P$, Bob's "now" intersects Alice's worldline at an event $Z$ with $t_Z = 2T - T/\gamma^2$ (by the mirror-image argument from the inbound frame).
>
> *The jump.* At the single event $P$, Bob's line of simultaneity swings from slope $+v$ to slope $-v$. As it swings, the point where it crosses Alice's worldline leaps from $X$ ($t = T/\gamma^2$) to $Z$ ($t = 2T - T/\gamma^2$). In the idealised instantaneous turnaround, Bob's notion of "what Alice is doing now" jumps *discontinuously* over the segment $XZ$ of Alice's worldline, of duration
> $$t_Z - t_X = 2T - \frac{2T}{\gamma^2} = 2T\left(1 - \frac{1}{\gamma^2}\right).$$
> This is the **missing time**. On the outbound and inbound legs, Bob does indeed see Alice's clock running slow — and symmetrically, Alice sees Bob's running slow. But Bob's accounting has a gap: the segment $XZ$ of Alice's life, which Bob's simultaneity skips over entirely during his turnaround. Add it back — $2T/\gamma^2$ (the two legs Bob attributes to Alice) plus $2T(1-1/\gamma^2)$ (the skipped segment) $= 2T$ — and Bob's books balance with Alice's age. A real, non-instantaneous turnaround replaces the discontinuous jump with a rapid but continuous sweep: while Bob accelerates, Alice (by his reckoning) ages very fast. Either way, the asymmetry of acceleration is what closes the gap, and the relativity of simultaneity is the mechanism.

> [!note]- Complete formal solution
> Alice, at rest in $S$, has proper time $\tau_{\text{Alice}} = 2T$. Bob travels at $\pm v$; each leg is a timelike displacement $(\Delta t,\Delta x) = (T,\pm vT)$ with interval $T^2(1-v^2) = T^2/\gamma^2$, so $\tau_{\text{Bob}} = 2T/\gamma < 2T$. The symmetry argument fails because Alice occupies one inertial frame while Bob occupies two and must accelerate at $P$ to switch — acceleration being absolute and felt only by Bob. Geometrically, Bob's legs are future-pointing timelike vectors $U = (T,vT)$, $V = (T,-vT)$ with $U+V = (2T,0)$ Alice's displacement; the reversed triangle inequality $\|U+V\| \ge \|U\|+\|V\|$ gives $2T \ge 2T/\gamma$ — the straight worldline is longest, the special-relativistic geodesic principle. On the spacetime diagram, Bob's line of simultaneity swings from slope $+v$ to $-v$ at $P$, sweeping the segment of Alice's worldline from $t = T/\gamma^2$ to $t = 2T - T/\gamma^2$, of duration $2T(1-1/\gamma^2)$ — the time Alice ages during Bob's turnaround, which exactly closes the accounting. $\blacksquare$

> [!warning] Illegal but tempting: blaming the proper-time deficit on the turnaround acceleration alone
> It is tempting to say "Bob ages less *because* he accelerates at $P$, and the missing time accrues during the acceleration". This is half right and half misleading. The asymmetry is indeed acceleration — only Bob accelerates, and that is what breaks the symmetry — but the *amount* of the deficit, $2T(1 - 1/\gamma)$, is set by the *velocities and durations of the inertial legs*, not by the details of the turnaround. One sees this by making the acceleration phase arbitrarily brief and violent (Gourgoulhon's idealised instantaneous turn) without changing the deficit, or arbitrarily gentle (the "tri-hyperbolic" worldline of constant proper acceleration) and still recovering the same kind of result. The deepest statement (Gourgoulhon, Remark 2.20) is that the twin paradox is *not* intrinsically about acceleration at all: it is the dissymmetry of the two worldlines. In a spacetime with non-simply-connected topology — a spatial torus, say — one twin can circumnavigate the universe and return *without ever accelerating*, both worldlines geodesic, and still age differently. Acceleration is how the dissymmetry is realised in ordinary (simply connected) Minkowski space, but the proper-time difference is a statement about worldline geometry, which is why the clean way to compute it is the reversed triangle inequality, not an integral over the acceleration.

---

# Key Takeaways

**The twin "paradox" is the reversed triangle inequality, and acceleration is what breaks the symmetry.** There is no paradox: Alice's worldline is straight, Bob's is bent, and the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] makes the straight one longer in proper time. The seductive "by symmetry, Alice should be younger" argument fails on a single point — the situation is not symmetric, because Alice stays in one inertial frame and Bob does not. Acceleration is absolute: Bob feels his turnaround, Alice feels nothing, and an accelerometer settles the matter without any appeal to a frame. Whenever a relativity problem presents a symmetry argument that "proves" a contradiction, audit the symmetry: check whether both parties really are inertial throughout. Almost always one of them accelerates, and the acceleration is the asymmetry the paradox pretended did not exist.

**Straight worldlines maximise proper time — the inertial path is the "longest", and every detour costs ageing.** This is the geometric content of the whole exercise and the deepest single fact in Minkowski geometry, the [[Thm - Inertial Worldlines Maximise Proper Time|special-relativistic geodesic principle]]. In Euclidean space the straight line is the *shortest* path; in Minkowski space, between two timelike-separated events, the straight (inertial) worldline is the *longest* in proper time, and any acceleration — any bending of the worldline — strictly reduces the elapsed proper time. The minus signs in the metric flip "shortest" to "longest". Physically: spatial motion subtracts from the interval, so a clock that wanders through space banks less time than one that sits still. The reusable principle: to compare the ageing of observers on different worldlines between the same two events, you do not need any time-dilation bookkeeping — just compare how bent the worldlines are. The straightest ages the most. This is the special-relativistic seed of the geodesic principle of general relativity, where freely-falling worldlines extremise proper time.

**The relativity of simultaneity closes the accounting — the "missing time" is the segment Bob's turnaround skips over.** A reader who insists on Bob's-eye-view bookkeeping can still make it work, and seeing how is the most instructive part. On each leg Bob legitimately sees Alice's clock dilated, so he attributes only $2T/\gamma^2$ of ageing to Alice from the two legs — apparently too little. The resolution is that Bob's "now-slice" of Alice's worldline jumps discontinuously at the turnaround: as his line of simultaneity swings from slope $+v$ to slope $-v$, it sweeps past a finite segment of Alice's life, $2T(1-1/\gamma^2)$ worth, which no leg of Bob's journey accounts for. Add the skipped segment and the books balance. This is the relativity of simultaneity doing its decisive work: "what Alice is doing now" is frame-dependent, and Bob's "now" is not even continuous across his change of frame. The general lesson — and the master key to every relativistic paradox — is that any argument tracking what a distant observer is doing "now" must account for the simultaneity slicing, and a change of frame discontinuously re-slices spacetime. See [[Ex - A round trip to the galactic centre]] for the same geometry pushed to astronomical scales, and [[Ex - Proper time along an accelerated worldline]] for the smooth (finite-acceleration) version of Bob's journey.
