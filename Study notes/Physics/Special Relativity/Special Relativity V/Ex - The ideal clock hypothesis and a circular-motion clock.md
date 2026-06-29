---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Proper Time"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Worldline of a Particle"
tags: [physics, special-relativity]
---

# Problem Statement

The **ideal clock hypothesis** (sometimes called the clock postulate) asserts that an ideal clock measures the proper time along its worldline, $\tau(E_k, E_{k+N}) = K N$, where the proportionality constant $K$ between elapsed proper time and number of ticks $N$ is the same at every point of the worldline — in particular, $K$ does not depend on the clock's *acceleration*. Working with $c = 1$:

1. State precisely what the ideal clock hypothesis claims, and explain why it is a genuinely independent postulate (not derivable from the kinematics of [[Def - Proper Time|proper time]] alone).
2. A clock moves in a **circle** of radius $r$ at constant speed $v$, completing one revolution in coordinate time $T = 2\pi r/v$. Compute the proper time $\Delta\tau$ it accumulates in one revolution, and compare with an identical clock at rest at the centre.
3. The circling clock is continuously *accelerating* (centripetal acceleration $|\mathbf{a}_{\text{cent}}| = v^2/r$ in the lab frame, proper acceleration $a = \gamma^2 v^2/r$). Show that, under the ideal clock hypothesis, the elapsed proper time depends only on the **speed** $v$, not on the acceleration $a$ — and explain why this is what licenses the CERN muon-storage-ring measurement of time dilation.
4. Discuss when a real device is a good ideal clock: contrast a pendulum and an atomic clock.

**Recall:**

![[Def - Proper Time#The Definition]]

A [[Def - Worldline of a Particle|worldline]] carries a proper time $\tau = \int\sqrt{ds^2} = \int dt/\gamma$. A clock is any device reduced to a point particle, following a timelike worldline, emitting a sequence of "ticks" $E_k$. The [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] $A$ has magnitude $\|A\| = a$, the proper acceleration.

---

# Convergent Strategy

**Problem class.** A *conceptual-plus-computation* problem: part 1 is the conceptual heart (what is an ideal clock?), parts 2–3 are a clean proper-time integral, part 4 is physical judgement. The [[Special Relativity V — Worldlines, Proper Time and Four-Velocity#Problem-Solving Strategy|topic strategy]] says: to find elapsed time for a clock, integrate $d\tau = dt/\gamma$ along its worldline — and crucially, that integrand depends on the *speed* through $\gamma$, never on the acceleration.

**Assumption pattern.** The decisive observation is that $d\tau = dt\sqrt{1 - u^2}$ involves $u$ but *not* $\dot u$ — the proper-time integrand has no acceleration in it. So *if* the clock reads proper time (the ideal clock hypothesis), its reading depends only on its speed history, not its acceleration. Part 1 is about recognising that "the clock reads proper time" is itself a postulate, separate from the geometry.

**Theorem routing.** Part 2 is a one-line integral: constant speed $\Rightarrow$ constant $\gamma \Rightarrow \Delta\tau = T/\gamma$. Part 3 routes through the absence of $\dot u$ in the proper-time integrand, combined with the ideal clock hypothesis. Part 4 routes through the empirical criterion: a device is a good ideal clock if the laws of physics expressed in its proper time take their standard form even under acceleration.

**Key decision point.** The conceptual crux is distinguishing two claims that are easy to conflate: (i) *the geometry* — proper time is $\int dt/\gamma$, a theorem; and (ii) *the physics* — a given clock actually displays this proper time even while accelerating, a postulate. The circular-motion case is the cleanest illustration because the clock is *always* accelerating yet (empirically, and under the hypothesis) reads a proper time set by speed alone.

---

# Legal Operations Used

1. **Compute proper time as $\int dt/\gamma$ along the worldline** (operation related to proper time on the topic page). For constant speed this is immediate: $\Delta\tau = T/\gamma$.

2. **Recognise an invariant** (operation 7 from the topic page). The proper time of one revolution is frame-independent; computing it in the lab frame, where the geometry is simplest, gives the universal answer.

3. **Classify the worldline** (operation 9 from the topic page). The circling clock is timelike with nonzero, constantly-rotating four-acceleration — a helix in spacetime — yet its proper time is set by speed alone.

---

# Hints

> [!note]- Hint 1
> The geometry of proper time ($\tau = \int dt/\gamma$) is a *theorem*. But asserting that a *physical clock* displays this proper time — even while accelerating — is an extra empirical claim. Ask: could there be a clock whose rate depends on its acceleration? Nothing in the kinematics forbids it; the ideal clock hypothesis is the statement that ideal clocks have no such dependence.

> [!note]- Hint 2
> The speed $v$ is constant, so $\gamma = (1 - v^2)^{-1/2}$ is constant along the worldline. Then $\Delta\tau = \int_0^T dt/\gamma = T/\gamma$. The clock at the centre is at rest, so its proper time is the full coordinate time $T$.

> [!note]- Hint 3
> Look at the integrand $d\tau = dt\sqrt{1 - u^2}$: it contains $u$ but not $du/dt$. So the elapsed proper time is a functional of the *speed* history only. The centripetal acceleration $a = \gamma^2 v^2/r$ can be made enormous (small $r$) without changing $\Delta\tau$, as long as $v$ is fixed.

> [!note]- Hint 4
> A device is a good ideal clock if the laws of kinematics and dynamics, written in terms of the time it displays, retain their standard form even when the device accelerates. A pendulum loses periodicity under non-constant acceleration; an atomic clock is governed by transitions insensitive to acceleration up to enormous values.

---

# Solution

The ideal clock hypothesis is the bridge from the *geometry* of proper time to the *physics* of real clocks, and the circular-motion clock is the textbook case that isolates it. The plan: Step 1 states the hypothesis and argues its independence; Step 2 computes the one-revolution proper time; Step 3 shows the result is acceleration-independent and connects to the muon ring; Step 4 judges real devices.

**Step 1: The ideal clock hypothesis and its independence.**

> [!note]- Derivation
> A **clock** is a device (reducible to a point particle) following a timelike worldline $\mathcal{L}$ and emitting a sequence of ticks $\dots, E_{-1}, E_0, E_1, \dots$ along it. An **ideal clock** is one for which the [[Def - Proper Time|proper time]] between ticks is a fixed multiple of the number of ticks:
> $$\tau(E_k, E_{k+N}) = K N,$$
> with the constant $K$ the *same at every point of the worldline*. Equivalently: an ideal clock displays the proper time along its worldline, and its rate is unaffected by acceleration.
>
> Why is this a separate postulate, not a theorem? Because the *geometry* — that the metric arc length $\tau = \int\sqrt{ds^2}$ is the privileged, frame-independent parameter — says nothing about whether any *physical* device tracks it. One can imagine a clock whose ticking rate depends on its acceleration (a clock that "shakes" when jolted). The kinematics of proper time does not forbid such a clock; it merely defines the geometric quantity $\tau$. The ideal clock hypothesis is the empirical assertion that there exist clocks (and we know which: good atomic clocks) whose proportionality constant $K$ is genuinely constant along the worldline, independent of acceleration. It is the physical input that lets us *measure* proper time, and it must be checked experimentally, not assumed.

**Step 2: Proper time of the circling clock.**

> [!note]- Derivation
> The clock moves in a circle of radius $r$ at constant speed $v$, so at every instant its speed is $u = v$ (constant) and $\gamma = (1 - v^2)^{-1/2}$ is constant. The worldline in the lab frame is $\big(t,\ r\cos\omega t,\ r\sin\omega t,\ 0\big)$ with $\omega = v/r$. The infinitesimal proper time is
> $$d\tau = dt\sqrt{1 - u^2} = \frac{dt}{\gamma},$$
> and since $\gamma$ is constant, one revolution (coordinate time $T = 2\pi r/v$) accumulates
> $$\Delta\tau = \int_0^T \frac{dt}{\gamma} = \frac{T}{\gamma} = T\sqrt{1 - v^2}.$$
> The identical clock at rest at the centre has $u = 0$, $\gamma = 1$, so it accumulates the full coordinate time $T$. Therefore the circling clock runs slow by the factor $\gamma$:
> $$\frac{\Delta\tau_{\text{circle}}}{\Delta\tau_{\text{centre}}} = \frac{1}{\gamma} = \sqrt{1 - v^2} < 1.$$
> After one revolution the two clocks are at the same place (the centre clock and the moment the circler returns to its starting angle, lab-simultaneously), so this is a genuine, reunitable comparison — a twin paradox with the traveller on a circular rather than out-and-back worldline.

**Step 3: The result depends on speed, not acceleration.**

> [!note]- Derivation
> The decisive feature is the form of the integrand: $d\tau = dt\sqrt{1 - u^2}$ depends on the *speed* $u$ but contains **no acceleration** $du/dt$ and no centripetal acceleration. So the elapsed proper time is a functional of the speed history alone:
> $$\Delta\tau = \int \sqrt{1 - u^2}\;dt,$$
> with $u$ the only kinematic input. For the circling clock $u = v$ is fixed, so $\Delta\tau = T/\gamma$ *regardless of $r$*. But the proper (centripetal) acceleration is $a = \gamma^2 v^2/r$, which can be made arbitrarily large by shrinking $r$ at fixed $v$. Thus two circling clocks at the same speed but vastly different radii — hence vastly different accelerations — accumulate the *same* proper time. Under the ideal clock hypothesis, where the clock reads exactly this proper time, the clock's rate is therefore set by its speed alone, independent of how violently it is accelerating.
>
> This is precisely what licenses the **CERN muon-storage-ring** measurement. Muons circulating in a storage ring at $v \approx 0.9994\,c$ ($\gamma \approx 29.3$) experience a proper acceleration of order $10^{18}\,g$ — astronomically large — yet their measured lifetime is dilated by exactly the factor $\gamma$ predicted from their *speed*, with no detectable dependence on the acceleration. The muon's decay is its internal clock; the experiment confirms both special-relativistic time dilation *and* the ideal clock hypothesis (the muon clock is unaffected by $10^{18}\,g$), to high precision. Were the muon's "clock" sensitive to acceleration, the storage-ring lifetime would deviate from $\gamma\tau_0$; it does not.

**Step 4: Real devices as ideal clocks.**

> [!note]- Derivation
> An ideal clock is a theoretical idealisation, approximated more or less well by real devices. The operational test: a device is a good ideal clock if the laws of kinematics and dynamics, expressed in terms of the time it displays, take their standard form even when the device accelerates.
>
> A **pendulum** fixed to the Earth is a fair ideal clock at the human scale (its swings are periodic in the proper time of an inertial frame). But under strong, *non-constant* acceleration the pendulum's motion loses its periodicity altogether — its rate depends on the acceleration, so it is a poor ideal clock in an accelerated setting.
>
> An **atomic clock** is far better. Its rate is fixed by a quantum transition frequency, which is insensitive to the clock's state of acceleration up to accelerations comparable to the centripetal acceleration of an electron in the atom, about $10^{23}\,\mathrm{m\,s^{-2}}$ — vastly beyond anything mechanically achievable. So an atomic clock reads proper time essentially independent of acceleration, which is why atomic clocks are the instruments used to verify the twin paradox ([[Ex - The Hafele-Keating experiment|Hafele–Keating]] and Alley) and why proper time is the *physical* time: the laws of physics expressed in atomic-clock time are simplest, because that time tracks the metric.

> [!note]- Complete formal solution
> The ideal clock hypothesis states that an ideal clock's proper time per tick, $K$ in $\tau(E_k, E_{k+N}) = KN$, is constant along its worldline — i.e. the clock reads proper time independent of acceleration. This is an empirical postulate separate from the geometry (which only defines $\tau = \int\sqrt{ds^2}$, not which devices track it). For a clock circling at constant speed $v$, radius $r$, period $T = 2\pi r/v$: the speed is constant so $\gamma$ is constant, and $\Delta\tau = \int_0^T dt/\gamma = T/\gamma = T\sqrt{1 - v^2}$, against the central clock's $T$, a slowdown by $\gamma$. The proper-time integrand $\sqrt{1 - u^2}\,dt$ contains $u$ but not $\dot u$, so $\Delta\tau$ depends only on speed; the centripetal proper acceleration $a = \gamma^2 v^2/r$ can be made arbitrarily large at fixed $v$ without changing $\Delta\tau$. This is why muons in the CERN ring, at $\gamma \approx 29$ and $\sim 10^{18}g$, have lifetimes dilated by exactly the speed-determined $\gamma$ with no acceleration dependence — confirming both time dilation and the ideal clock hypothesis. Atomic clocks approximate ideal clocks (insensitive to acceleration up to $\sim 10^{23}\,\mathrm{m\,s^{-2}}$); pendulums do not under non-constant acceleration. $\blacksquare$

> [!warning] Illegal but tempting: attributing the muon lifetime dilation to its acceleration
> Because the muon in a storage ring is violently accelerated, one might guess its lifetime extension is somehow *caused* by, or sensitive to, that acceleration. It is not: the dilation factor is $\gamma$, computed from the muon's *speed* alone, and the proper-time integrand $\sqrt{1 - u^2}\,dt$ has no acceleration in it. The acceleration's only role is to keep the muon on a closed (circular) path so the comparison can be made; were the muon flying in a straight line at the same speed, its lifetime would be dilated by the same $\gamma$. The ideal clock hypothesis is exactly the statement that the acceleration does *not* enter, and the storage-ring experiment is its confirmation. The diagnostic: if you ever find acceleration entering a proper-time computation, you have either left the ideal clock hypothesis or made an algebra error — the geometry of proper time is built from speed (the metric line element), not acceleration.

---

# Key Takeaways

**Proper time depends on speed, not acceleration — because the line element has no $\dot u$ in it.** The single most useful fact about proper-time computations is that the integrand $d\tau = dt\sqrt{1 - u^2}$ involves only the instantaneous *speed*, never the acceleration. So the elapsed proper time of any clock is a functional of its speed history alone: two clocks that follow the same speed-versus-time profile accumulate identical proper time, no matter how differently they accelerate. This is what makes the circling clock ($u = v$ constant, $a = \gamma^2 v^2/r$ arbitrary) read $T/\gamma$ regardless of radius, and it is what lets the muon-ring experiment cleanly test *speed-induced* time dilation despite enormous accelerations. The trigger: whenever a problem worries you with acceleration in a timing context, remember that acceleration enters proper time only indirectly, through its effect on the *speed* — the proper-time integral itself is acceleration-blind.

**The ideal clock hypothesis is physics, not geometry — and it must be tested.** It is tempting to think "proper time is the time a clock reads" is a definition or a theorem. It is neither: the geometry defines the *quantity* $\tau = \int\sqrt{ds^2}$, but the claim that a *physical device* tracks it — even while accelerating — is an empirical postulate, the ideal clock hypothesis. The distinction matters because it tells you what is being tested in the great clock experiments: not just time dilation, but the proposition that good clocks are acceleration-insensitive. A clock whose rate depended on its acceleration would still exist in a consistent relativity; nature simply provides clocks (atomic transitions) that do not. The reusable lesson: separate the geometric object (proper time, a theorem) from the physical claim (this device reads it, a postulate), and know that the second is on experimental, not logical, footing — confirmed for atomic clocks to extraordinary acceleration, only approximate for mechanical ones.

**Circular motion is a twin paradox with no turnaround — and the asymmetry is still acceleration.** The circling clock and the central clock part and reunite, and the circler is younger by $\gamma$ — a twin paradox. But unlike the [[Ex - The twin paradox|out-and-back version]], there is no single dramatic turnaround event; the circler accelerates *continuously*. The asymmetry between the two clocks is still that one (the circler) is non-inertial — its worldline is a helix in spacetime, with nonzero four-acceleration everywhere — while the other (the centre) is inertial, a straight worldline. The reversed triangle inequality / [[Thm - Inertial Worldlines Maximise Proper Time|geodesic principle]] still decides it: the straight (central) worldline is longest in proper time. This case is a clean reminder that the twin paradox is about *worldline geometry* (straight versus bent), not about any particular turnaround, and that a continuously curved worldline is "bent everywhere" and so loses proper time at every instant. See [[Ex - Proper time along an accelerated worldline]] for the linear (out-and-back) accelerated case.
