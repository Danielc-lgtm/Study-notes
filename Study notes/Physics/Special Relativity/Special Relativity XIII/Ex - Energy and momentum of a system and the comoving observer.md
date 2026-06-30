---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Energy and Momentum Relative to an Observer"
  - "Def - Four-Momentum and Rest Mass"
  - "Thm - Conservation of Four-Momentum"
tags: [physics, special-relativity]
---

# Problem Statement

A system of particles has total [[Def - Four-Momentum and Rest Mass|four-momentum]] $P = \sum_a P_a$. An [[Def - Observer and Local Rest Space|observer]] $\mathcal{O}$ has four-velocity $U_0$.

1. Show that the energy and three-momentum of the *system* measured by $\mathcal{O}$ are the sums of the individual energies and momenta: $E = \sum_a E_a$ and $\mathbf{p} = \sum_a \mathbf{p}_a$.
2. Show that a **comoving observer** (one moving with the system, i.e. $U_0 = P/M$ where $M$ is the system's invariant mass) measures zero total momentum, $\mathbf{p} = \mathbf{0}$, and total energy equal to the system mass, $E = M$.
3. Show that if the system is **isolated** and $\mathcal{O}$ is **inertial**, both the energy and the momentum it measures are constant in time: $dE/dt = 0$ and $d\mathbf{p}/dt = \mathbf{0}$.

Work with $c = 1$.

**Recall:**

![[Thm - Energy and Momentum Relative to an Observer#Statement]]

The total four-momentum of an isolated system is conserved ([[Thm - Conservation of Four-Momentum]]). The invariant mass is $M = \sqrt{P\cdot P}$, and a comoving observer has four-velocity $U_0 = P/M$ (the normalised total four-momentum). The energy measured by $\mathcal{O}$ is $E = P\cdot U_0$, the momentum the orthogonal projection $\mathbf{p} = P - (P\cdot U_0)U_0$.

---

# Convergent Strategy

**Problem class.** A *structural* problem of the [[Special Relativity XIII — Energy and Momentum#Problem-Solving Strategy|relate-measurements-to-an-observer]] type: the energy and momentum a given observer measures are obtained by contracting and projecting the four-momentum with that observer's four-velocity. Additivity (part 1) and the comoving frame (part 2) follow from linearity of the contraction; constancy (part 3) follows from conservation.

**Assumption pattern.** A system's total four-momentum, an observer's four-velocity. The signpost for part 2 is "comoving observer", whose four-velocity is the normalised total four-momentum $U_0 = P/M$; for part 3 the signposts are "isolated" (so $P$ is conserved) and "inertial" (so $U_0$ is constant).

**Theorem routing.** All three parts use $E = P\cdot U_0$ and $\mathbf{p} = \perp_{U_0}P$ from [[Thm - Energy and Momentum Relative to an Observer]]. Part 1 uses linearity of the contraction and projection over the sum $P = \sum P_a$. Part 2 substitutes $U_0 = P/M$. Part 3 combines conservation ($P$ constant, [[Thm - Conservation of Four-Momentum]]) with $U_0$ constant (inertial observer).

**Key decision point.** The crux of part 2 is recognising that the comoving observer's four-velocity is the *normalised total four-momentum* $U_0 = P/M$ — this is the relativistic definition of "moving with the system". The non-obvious content of part 3 is that constancy of the *measured* energy and momentum requires *both* the four-momentum to be conserved *and* the observer's four-velocity to be constant (inertial); a non-inertial observer would measure changing energy even for an isolated system.

---

# Legal Operations Used

1. **Use $E = P\cdot U_0$ to read the energy an observer measures** (operation 5 from the topic page). The energy and momentum of the system relative to $\mathcal{O}$ are the contraction and projection of the total four-momentum.

2. **Go to the centre-of-momentum frame** (operation 3). The comoving observer in part 2 is exactly the centre-of-momentum observer, $U_0 = P/M$, in which the total momentum vanishes.

3. **Write down the total four-momentum and set it equal before and after** (operation 1). Part 3 uses conservation of the total four-momentum for the isolated system.

---

# Hints

> [!note]- Hint 1
> The energy and momentum of the system are $E = P\cdot U_0$ and $\mathbf{p} = \perp_{U_0}P$ with $P = \sum_a P_a$. The contraction and projection are *linear*, so they distribute over the sum: $E = \sum_a P_a\cdot U_0 = \sum_a E_a$.

> [!note]- Hint 2
> A comoving observer has four-velocity $U_0 = P/M$ (the system's total four-momentum, normalised so $U_0\cdot U_0 = 1$; check $P\cdot P = M^2$). Compute $E = P\cdot U_0 = P\cdot(P/M) = M^2/M = M$, and $\mathbf{p} = P - (P\cdot U_0)U_0 = P - M\cdot(P/M) = 0$.

> [!note]- Hint 3
> For an isolated system $P$ is constant in time (conservation of four-momentum). For an inertial observer $U_0$ is also constant. The energy $E = P\cdot U_0$ is then a contraction of two constants, hence constant; same for $\mathbf{p} = \perp_{U_0}P$.

---

# Solution

The energy and momentum of a system relative to an observer are the sums of the parts', obtained by contracting/projecting the total four-momentum; a comoving observer sees zero momentum and energy equal to the system mass; and for an isolated system viewed by an inertial observer both are constant. Part 1 uses linearity; Part 2 substitutes the comoving four-velocity $U_0 = P/M$; Part 3 combines conservation with the constancy of an inertial $U_0$.

**Step 1: Energy and momentum are additive.**

> [!note]- Derivation
> The energy of the system relative to $\mathcal{O}$ is the contraction of the *total* four-momentum with $U_0$:
> $$E = P\cdot U_0 = \Big(\sum_a P_a\Big)\cdot U_0 = \sum_a (P_a\cdot U_0) = \sum_a E_a,$$
> using linearity of the inner product in its first argument; each $E_a = P_a\cdot U_0$ is the energy of particle $a$ measured by $\mathcal{O}$. Similarly the momentum is the orthogonal projection of the total:
> $$\mathbf{p} = \perp_{U_0}P = P - (P\cdot U_0)U_0 = \sum_a\big(P_a - (P_a\cdot U_0)U_0\big) = \sum_a\perp_{U_0}P_a = \sum_a\mathbf{p}_a,$$
> again by linearity. So the energy and momentum of a system are the sums of the individual energies and momenta — additivity holds for energy and momentum (unlike mass, which is the *length* of the sum, not the sum of lengths).

**Step 2: The comoving observer.**

> [!note]- Derivation
> A **comoving observer** moves with the system as a whole; its four-velocity is the normalised total four-momentum,
> $$U_0 = \frac{P}{M}, \qquad M = \sqrt{P\cdot P},$$
> which is a unit timelike vector ($U_0\cdot U_0 = P\cdot P/M^2 = M^2/M^2 = 1$), provided $M > 0$ (the system is not purely collinear massless particles). The energy this observer measures is
> $$E = P\cdot U_0 = P\cdot\frac{P}{M} = \frac{P\cdot P}{M} = \frac{M^2}{M} = M,$$
> the **invariant mass** of the system. The momentum is
> $$\mathbf{p} = P - (P\cdot U_0)U_0 = P - M\cdot\frac{P}{M} = P - P = \mathbf{0}.$$
> So the comoving observer measures zero total momentum and energy equal to the system mass: this is the **centre-of-momentum frame**, and it confirms $M = E_{\text{cm}}$. The system "is at rest" relative to the comoving observer — its total momentum vanishes — even though the individual particles inside it are moving.

**Step 3: Conservation for an inertial observer.**

> [!note]- Derivation
> Suppose the system is **isolated**. By [[Thm - Conservation of Four-Momentum|conservation of four-momentum]], the total four-momentum is constant in time: $dP/d\tau = 0$, so $P$ is the same four-vector at every instant. Suppose also that $\mathcal{O}$ is **inertial**: its four-velocity $U_0$ is constant (an inertial observer moves uniformly, so $dU_0/d\tau = 0$).
>
> Then the energy measured by $\mathcal{O}$,
> $$E = P\cdot U_0,$$
> is the inner product of two *constant* four-vectors, hence constant: $\frac{dE}{dt} = \frac{d}{dt}(P\cdot U_0) = \frac{dP}{dt}\cdot U_0 + P\cdot\frac{dU_0}{dt} = 0 + 0 = 0.$ Likewise the momentum
> $$\mathbf{p} = P - (P\cdot U_0)U_0$$
> is built from the constants $P$ and $U_0$, so $\frac{d\mathbf{p}}{dt} = \mathbf{0}$. Therefore an inertial observer measures *constant* total energy and total momentum for an isolated system — the relativistic statement that energy and momentum are conserved. (The two conditions are both needed: a *non-inertial* observer, whose $U_0$ changes, would measure a changing energy even for an isolated system, because the contraction $P\cdot U_0$ would change through $U_0$.)

> [!note]- Complete formal solution
> The energy and momentum of the system relative to $\mathcal{O}$ are $E = P\cdot U_0$ and $\mathbf{p} = \perp_{U_0}P$ with $P = \sum_a P_a$. **(1)** By linearity, $E = \sum_a P_a\cdot U_0 = \sum_a E_a$ and $\mathbf{p} = \sum_a\perp_{U_0}P_a = \sum_a\mathbf{p}_a$: energy and momentum are additive. **(2)** A comoving observer has $U_0 = P/M$ ($M = \sqrt{P\cdot P}$, $U_0\cdot U_0 = 1$); then $E = P\cdot(P/M) = M$ and $\mathbf{p} = P - M(P/M) = \mathbf{0}$: zero momentum, energy equal to the mass. **(3)** For an isolated system $P$ is constant (conservation) and for an inertial observer $U_0$ is constant, so $E = P\cdot U_0$ and $\mathbf{p} = \perp_{U_0}P$ are constant: $dE/dt = 0$, $d\mathbf{p}/dt = \mathbf{0}$. $\blacksquare$

---

# Key Takeaways

**Energy and momentum are additive; mass is not.** This exercise makes the contrast sharp. The energy and momentum of a system are the *sums* of the parts', because they are linear functionals (contraction and projection) of the total four-momentum, which is itself the sum. But the mass is the *length* of that total four-momentum, and length is not linear, so $M \ne \sum m_a$ in general. The reusable diagnostic: when combining particles, add their four-momenta; then energy and momentum come from the sum by contraction/projection (additive), while mass comes from the sum by taking a norm (non-additive). This is why a hot gas (more internal energy) is heavier than a cold one even though the particle count is the same, and why the [[Ex - The invariant mass of a system of particles|invariant mass of a system]] requires the full squared-sum calculation.

**The comoving observer is the centre-of-momentum frame, and its four-velocity is the normalised total four-momentum.** The relativistic definition of "moving with the system" is $U_0 = P/M$ — the total four-momentum, normalised. In this frame the total momentum vanishes and the energy equals the system mass $M$. This is the single most useful frame in collision physics, and recognising that "comoving" $=$ "centre-of-momentum" $=$ "$U_0 = P/M$" is what lets you evaluate invariants there. The trigger is any multi-particle system whose mass or threshold is wanted: go to the frame $U_0 = P/M$, where the kinematics trivialise. This is the same frame that makes [[Ex - Threshold energy for particle production|production thresholds]] tractable, where at threshold all products are at rest.

**Conservation of measured energy needs both an isolated system and an inertial observer.** It is tempting to say "energy is conserved for an isolated system" without qualification, but the *measured* energy $E = P\cdot U_0$ depends on the observer's four-velocity $U_0$ as well as on $P$. For $E$ to be constant in time, *both* $P$ must be constant (the system isolated, conservation of four-momentum) *and* $U_0$ must be constant (the observer inertial). A non-inertial observer — one who accelerates — measures a *changing* energy for an isolated system, because the contraction $P\cdot U_0$ changes through the changing $U_0$, not through any change in the system. The reusable lesson: conserved quantities are properties of the *system* (the four-vector $P$), and turning them into measured numbers requires contracting with an observer; the measured number is constant only when the observer is too. This distinction matters in general relativity and cosmology, where there is no global inertial observer and "energy conservation" must be stated carefully.
